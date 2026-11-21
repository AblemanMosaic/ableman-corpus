#!/usr/bin/env python3
"""Bind a prepared same-DOI edit plan to current local Zenodo observations."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--database", type=Path, required=True)
    args = parser.parse_args()
    plan_path = args.plan.resolve()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    connection = sqlite3.connect(f"file:{args.database.resolve().as_posix()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    records = {
        row["provider_record_id"]: dict(row)
        for row in connection.execute(
            "SELECT provider_record_id, title, doi, publication_date, evidence_json "
            "FROM publication_records WHERE provider='ZENODO'"
        )
    }
    connection.close()
    now = datetime.now(timezone.utc)
    counts: Counter[str] = Counter()
    for item in plan["records"]:
        observed = records.get(str(item["provider_record_id"]))
        if not observed:
            item["live_observation_status"] = "MISSING"
            item["provider_route"] = "REFUSE_UNRESOLVED_RECORD"
            counts[item["provider_route"]] += 1
            continue
        evidence = json.loads(observed["evidence_json"])
        created = evidence.get("created") or evidence.get("modified")
        created_at = datetime.fromisoformat(created.replace("Z", "+00:00"))
        age = (now - created_at).days
        item.update({
            "live_observation_status": "MATCHED_READ_ONLY",
            "provider_created_at": created_at.isoformat(),
            "provider_age_days_at_classification": age,
            "observed_doi": observed["doi"],
            "observed_title": observed["title"],
            "self_service_file_edit_window_likely_open": age <= 30,
        })
        if age <= 30:
            item["provider_route"] = "EDIT_PUBLISHED_FILES_PUBLISH_VERIFY_SAME_DOI"
            item["expected_terminal_state"] = "ONE_RECORD_SAME_DOI_CORRECTED_PDF"
        else:
            item["provider_route"] = "ZENODO_SUPPORT_REQUIRED_FOR_SAME_DOI_FILE_CORRECTION"
            item["expected_terminal_state"] = "NO_AUTOMATED_MUTATION_UNTIL_SUPPORT_ROUTE_IS_RESOLVED"
        counts[item["provider_route"]] += 1
    plan["classified_at"] = now.isoformat()
    plan["live_catalog_observation"] = {
        "records_observed": len(records),
        "provider_mutation": False,
        "latest_versions_only": True,
    }
    plan["provider_policy"] = {
        "file_correction": "Minor file correction is available within 30 days and the correction draft must be published within 45 days of original publication; publishing does not change the DOI.",
        "older_records": "File modification outside the window requires Zenodo support and a duly justified case.",
        "new_versions": "Zenodo new-version records retain prior version history and therefore do not satisfy the requested single-live-version presentation.",
        "api_action": "POST /api/deposit/depositions/:id/actions/edit unlocks an already submitted deposition for editing and requires deposit:actions; file changes require deposit:write.",
        "sources": [
            "https://help.zenodo.org/docs/deposit/manage-records/",
            "https://help.zenodo.org/docs/deposit/manage-files/",
            "https://help.zenodo.org/docs/deposit/manage-versions/",
            "https://developers.zenodo.org/",
        ],
    }
    plan["route_counts"] = dict(sorted(counts.items()))
    write_json(plan_path, plan)
    print(json.dumps({"records": len(plan["records"]), "route_counts": plan["route_counts"]}, indent=2))
    return 0 if not counts.get("REFUSE_UNRESOLVED_RECORD") else 1


if __name__ == "__main__":
    raise SystemExit(main())
