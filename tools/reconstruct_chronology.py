#!/usr/bin/env python3
"""Freeze the initial chronological accession sequence for the paper corpus.

The accession is permanent.  Historical dates remain separately inspectable
and sortable, so a later-discovered older work can be appended without
renumbering the already admitted corpus.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


SCHEMA = "ableman.corpus-accession-ledger.v0.1"
ACCESSION_PREFIX = "AC"
EXCLUDED_TITLE_PREFIXES = ("Project57",)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def iso_from_epoch(value: float) -> str:
    return datetime.fromtimestamp(value).astimezone().isoformat(timespec="microseconds")


def public_locator(member: dict[str, Any]) -> str:
    return f"{member['root_id']}:{member['relative_path'].replace(chr(92), '/')}"


def resolve_local_date(work: dict[str, Any], refresh_filesystem: bool) -> tuple[str, dict[str, Any]]:
    candidates: list[tuple[float, dict[str, Any], str]] = []
    for member in work.get("members", []):
        recorded = float(member.get("modified_epoch") or 0)
        if not recorded:
            continue
        timestamp = recorded
        observation = "AUTHORITATIVE_REGISTRY_RECORDED_MTIME"
        if refresh_filesystem:
            path = Path(member["path"])
            try:
                if path.is_file() and sha256_file(path) == member.get("sha256"):
                    timestamp = path.stat().st_mtime
                    observation = "LIVE_FILE_MTIME_WITH_MATCHING_SHA256"
                elif path.is_file():
                    observation = "REGISTRY_MTIME_RETAINED_CURRENT_HASH_DRIFT"
                else:
                    observation = "REGISTRY_MTIME_RETAINED_SOURCE_CURRENTLY_MISSING"
            except OSError:
                observation = "REGISTRY_MTIME_RETAINED_SOURCE_UNREADABLE"
        candidates.append((timestamp, member, observation))
    if not candidates:
        raise ValueError(f"no dated family member for {work['cluster_id']}: {work['title']}")
    timestamp, member, observation = min(candidates, key=lambda item: (item[0], public_locator(item[1])))
    iso = iso_from_epoch(timestamp)
    evidence = {
        "kind": "VERSION_FAMILY_FILE_MTIME",
        "locator": public_locator(member),
        "sha256": member.get("sha256"),
        "observation": observation,
        "version_family_id": work.get("version_family_id"),
        "family_member_count": len(work.get("members", [])),
    }
    return iso, evidence


def chronology_markdown(ledger: dict[str, Any]) -> str:
    lines = [
        "# Ableman Corpus Historical Accession Sequence",
        "",
        "This is the frozen initial accession sequence. Accession identifiers are permanent; chronology remains a separately sortable evidence field. File timestamps establish the earliest currently documented local corpus date, not necessarily the date an idea was first conceived.",
        "",
        "| Accession | Earliest documented date | Basis | Title |",
        "|---|---:|---|---|",
    ]
    for item in ledger["accessions"]:
        title = item["title_at_freeze"].replace("|", "\\|")
        lines.append(f"| {item['accession_id']} | {item['earliest_documented_date']} | {item['chronology_basis']} | {title} |")
    lines.extend(("", f"Ledger root: `{ledger['ledger_root_sha256']}`", ""))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--successor-ledger", type=Path, required=True)
    parser.add_argument("--paper-registry", type=Path, required=True)
    parser.add_argument("--publication-ledger", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path)
    parser.add_argument("--freeze-date", required=True)
    parser.add_argument("--refresh-filesystem", action="store_true")
    args = parser.parse_args()

    successors = [
        item for item in read_json(args.successor_ledger)
        if not item["title"].startswith(EXCLUDED_TITLE_PREFIXES)
    ]
    registry_doc = read_json(args.paper_registry)
    registry = {item["cluster_id"]: item for item in registry_doc["works"]}
    publications_doc = read_json(args.publication_ledger)
    publications = {str(item["record_id"]): item for item in publications_doc["records"]}

    dated: list[dict[str, Any]] = []
    for item in successors:
        work_id = item["work_id"]
        if work_id.startswith("PAPER.PUB."):
            record_id = work_id.removeprefix("PAPER.PUB.")
            publication = publications.get(record_id)
            if not publication:
                raise ValueError(f"missing publication record {record_id} for {item['title']}")
            timestamp = publication.get("uploaded") or f"{publication['publication_date']}T00:00:00-08:00"
            evidence = {
                "kind": "ZENODO_PUBLICATION_RECORD",
                "provider": "zenodo",
                "record_id": record_id,
                "doi": publication.get("doi"),
                "provider_url": publication.get("zenodo_page"),
                "uploaded": publication.get("uploaded"),
            }
            publication_date = publication.get("publication_date")
            basis = "FIRST_PUBLICATION_TIMESTAMP"
            confidence = "HIGH"
        else:
            work = registry.get(work_id)
            if not work:
                raise ValueError(f"missing local version family for {work_id}: {item['title']}")
            timestamp, evidence = resolve_local_date(work, args.refresh_filesystem)
            publication_date = None
            basis = "EARLIEST_VERSION_FAMILY_FILE_MTIME"
            confidence = "MEDIUM"
        dated.append({
            "work_id": work_id,
            "title_at_freeze": item["title"],
            "earliest_documented_timestamp": timestamp,
            "earliest_documented_date": timestamp[:10],
            "chronology_basis": basis,
            "chronology_confidence": confidence,
            "first_publication_date": publication_date,
            "first_complete_draft_date": None,
            "work_origin_date": None,
            "corpus_admission_date": args.freeze_date,
            "chronology_evidence": evidence,
        })

    dated.sort(key=lambda item: (
        item["earliest_documented_timestamp"],
        item["title_at_freeze"].casefold(),
        item["work_id"],
    ))
    for number, item in enumerate(dated, 1):
        item["accession_number"] = number
        item["accession_id"] = f"{ACCESSION_PREFIX}-{number:04d}"
        item["accession_frozen"] = True

    root = hashlib.sha256(canonical_bytes(dated)).hexdigest().upper()
    ledger = {
        "schema": SCHEMA,
        "freeze_date": args.freeze_date,
        "status": "FROZEN_INITIAL_SEQUENCE",
        "authority": "AUTHOR_AUTHORIZED_CHRONOLOGICAL_ACCESSION_POLICY",
        "identity_effect": "PERMANENT_CORPUS_ACCESSION_ASSIGNMENT_ONLY",
        "semantic_identity_effect": "NONE",
        "policy": {
            "initial_assignment": "ASCENDING_EARLIEST_DOCUMENTED_TIMESTAMP_THEN_TITLE_THEN_WORK_ID",
            "published_date_basis": "ZENODO_UPLOAD_TIMESTAMP_WITH_PUBLICATION_DATE",
            "local_date_basis": "EARLIEST_MTIME_ACROSS_THE_ADMITTED_VERSION_FAMILY_IN_THE_TWO_AUTHORIZED_PAPER_ROOTS",
            "future_assignment": "APPEND_NEXT_ACCESSION_WITHOUT_RENUMBERING_EXISTING_WORKS",
            "historical_display": "SORT_BY_EARLIEST_DOCUMENTED_TIMESTAMP_INDEPENDENTLY_OF_ACCESSION_WHEN_LATER_BACKFILL_REQUIRES_IT",
        },
        "claim_ceiling": "Dates establish the earliest documentary evidence used by this accession pass. A filesystem timestamp is not proof of first conception or first composition; publication timestamps establish publication chronology, not necessarily drafting chronology.",
        "source_roots": [
            {"root_id": item["root_id"], "scope": "AUTHOR_SPECIFIED_PAPERS_TREE_INCLUDING_DRAFTS"}
            for item in registry_doc.get("roots", [])
        ],
        "source_ledgers": {
            "successor_ledger_sha256": sha256_file(args.successor_ledger),
            "paper_registry_sha256": sha256_file(args.paper_registry),
            "publication_ledger_sha256": sha256_file(args.publication_ledger),
        },
        "counts": {
            "accessions": len(dated),
            "published_timestamp_basis": sum(1 for item in dated if item["chronology_basis"] == "FIRST_PUBLICATION_TIMESTAMP"),
            "local_family_timestamp_basis": sum(1 for item in dated if item["chronology_basis"] == "EARLIEST_VERSION_FAMILY_FILE_MTIME"),
        },
        "accessions": dated,
        "ledger_root_sha256": root,
    }
    write_json(args.output, ledger)
    if args.markdown_output:
        args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_output.write_text(chronology_markdown(ledger), encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "accessions": len(dated),
        "first": dated[0],
        "last": dated[-1],
        "ledger_root_sha256": root,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
