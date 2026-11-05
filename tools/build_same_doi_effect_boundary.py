from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROUTE = "EDIT_PUBLISHED_FILES_PUBLISH_VERIFY_SAME_DOI"
EXCLUDED_ACCESSION = "AC-0163"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("plan", type=Path)
    parser.add_argument("authorization", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    root = args.candidate.resolve()
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    authorization = json.loads(args.authorization.read_text(encoding="utf-8"))
    records = [record for record in plan["records"] if record["provider_route"] == ROUTE]

    if len(records) != authorization["authorized_record_count"]:
        raise SystemExit("AUTHORIZED_RECORD_COUNT_MISMATCH")
    if any(record["accession_id"] == EXCLUDED_ACCESSION for record in records):
        raise SystemExit("SEMANTIC_DEBT_ROUTE_REFUSED")

    artifacts = []
    required = []
    support_files = [
        (args.plan.resolve(), "control/ZENODO-SAME-DOI-EDIT-PLAN.json", "runner: authorized record plan"),
        (args.authorization.resolve(), "control/AUTHORIZED-SAME-DOI-CORRECTION-CAMPAIGN.json", "runner: author authority and exclusions"),
    ]
    workbench = root.parent / "ableman-corpus-publication-workbench"
    for relative in (
        "acpw/__init__.py",
        "acpw/same_doi_corrections.py",
        "acpw/credentials.py",
        "acpw/providers/__init__.py",
        "acpw/providers/zenodo.py",
        "acpw/providers/http.py",
    ):
        support_files.append((workbench / relative, f"runner/{relative}", "runner: local governed campaign execution"))
    for source, destination, required_by in support_files:
        if not source.is_file():
            raise SystemExit(f"RUNNER_SUPPORT_MISSING:{source}")
        artifacts.append({
            "source_path": source.resolve().as_posix(),
            "destination_path": destination,
            "sha256": sha256(source.resolve()),
            "required_by": required_by,
        })
        required.append(destination)
    for record in records:
        relative = record["prepared_pdf_path"].replace("\\", "/")
        source = (root / Path(relative)).resolve()
        if root not in source.parents or not source.is_file():
            raise SystemExit(f"PREPARED_PDF_MISSING_OR_OUTSIDE_CANDIDATE:{record['accession_id']}")
        observed = sha256(source)
        expected = record["prepared_pdf_sha256"].lower()
        if observed != expected:
            raise SystemExit(f"PREPARED_PDF_HASH_DRIFT:{record['accession_id']}")
        destination = f"zenodo/{record['provider_record_id']}/{source.name}"
        artifacts.append({
            "source_path": source.as_posix(),
            "destination_path": destination,
            "sha256": observed,
            "required_by": f"Zenodo same-DOI correction for {record['accession_id']}",
        })
        required.append(destination)

    manifest = {
        "schema": "codex.exact-artifact-boundary.v1",
        "boundary_id": "ableman-corpus-zenodo-same-doi-correction-2026-11-05",
        "artifacts": artifacts,
        "runner_required_paths": required,
        "allow_extra_artifacts": False,
        "policy": {
            "maximum_transfers": len(records),
            "maximum_invocations": len(records) + 2,
            "maximum_retries": 0,
            "preserve_prior_custody": True,
            "terminal_capture": ["stdout", "stderr", "exit_code", "terminal_receipt", "per_record_terminal_receipt"],
        },
        "authority_binding": {
            "authorization_path": args.authorization.resolve().as_posix(),
            "authorization_sha256": sha256(args.authorization.resolve()),
            "authorized_record_count": len(records),
            "excluded_accession_ids": [EXCLUDED_ACCESSION],
            "excluded_providers": ["OSF"],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "artifacts": len(artifacts), "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
