#!/usr/bin/env python3
"""Apply exact author-withholding rulings to an existing public projection.

This tool is intentionally narrower than a corpus rebuild. It preserves every
unaffected release bundle byte-for-byte, removes only explicitly named public
projection bundles and metadata records, and leaves the accession ledger and
governed source custody untouched.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


WITHHELD = {
    "AMCS-LOCAL-WORK-9CC31EEBBC3976CE": {
        "accession_id": "AC-0101",
        "bundle": "AC-0101-the-ableman-format-specification-afs",
        "title": "The Ableman Format Specification (AFS)",
        "reason": "AUTHOR_WITHHELD_PENDING_AMCAS_SUCCESSOR_REVIEW",
    },
    "AMCS-LOCAL-WORK-21CC00303A2E8D3C": {
        "accession_id": "AC-0185",
        "bundle": "AC-0185-technical-brief-context-compiled-consciousness-mode",
        "title": "Technical Brief: Context-Compiled Consciousness Mode for Language Models",
        "reason": "AUTHOR_WITHHELD_PENDING_INDEPENDENT_PROJECT57_REPLICATION_AND_EXTERNAL_SOURCE_REVIEW",
    },
    "AMCS-LOCAL-WORK-02E0AB0D4874ACB3": {
        "accession_id": "AC-0192",
        "bundle": "AC-0192-qualia-binding-and-realization-mapping",
        "title": "Qualia Binding and Realization Mapping",
        "reason": "AUTHOR_WITHHELD_PENDING_EMPIRICAL_DATA_BASELINES_ETHICS_AND_EXTERNAL_SCHOLARLY_REVIEW",
    },
}


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--apply", action="store_true", help="perform the bounded removal")
    args = parser.parse_args()
    root = args.root.resolve()
    corpus_path = root / "metadata" / "corpus.json"
    corpus = json.loads(corpus_path.read_text(encoding="utf-8"))
    records = corpus.get("papers")
    if not isinstance(records, list):
        raise ValueError("metadata/corpus.json does not contain a papers list")

    by_id = {record["work_id"]: record for record in records}
    for work_id, ruling in WITHHELD.items():
        record = by_id.get(work_id)
        if record is None:
            continue
        if record.get("accession_id") != ruling["accession_id"] or record.get("title") != ruling["title"]:
            raise ValueError(f"withholding identity mismatch for {work_id}")

    remaining = [record for record in records if record["work_id"] not in WITHHELD]
    if len(remaining) != 195:
        raise ValueError(f"expected 195 projected records after withholding, found {len(remaining)}")
    expected_accessions = {"AC-0101", "AC-0185", "AC-0192"}
    present_accessions = {record["accession_id"] for record in records if record["work_id"] in WITHHELD}
    if present_accessions not in (expected_accessions, set()):
        raise ValueError(f"partial or unexpected withholding state: {sorted(present_accessions)}")

    if not args.apply:
        print("DRY_RUN_OK: 3 exact public bundles and metadata records are eligible for withholding")
        return 0

    public_root = (root / "papers" / "current").resolve()
    metadata_root = (root / "metadata" / "papers").resolve()
    for work_id, ruling in WITHHELD.items():
        bundle = (public_root / ruling["bundle"]).resolve()
        if bundle.parent != public_root:
            raise ValueError(f"unsafe bundle path: {bundle}")
        if bundle.exists():
            shutil.rmtree(bundle)
        metadata = (metadata_root / f"{work_id}.json").resolve()
        if metadata.parent != metadata_root:
            raise ValueError(f"unsafe metadata path: {metadata}")
        if metadata.exists():
            metadata.unlink()

    corpus["papers"] = remaining
    corpus["excluded_by_author_ruling"] = [
        {
            "title": "Project57: Meta-Binding Testing Protocol",
            "reason": "AUTHOR_NOT_READY_RULING",
            "accession_id": None,
        },
        *[
            {
                "title": ruling["title"],
                "reason": ruling["reason"],
                "accession_id": ruling["accession_id"],
            }
            for ruling in WITHHELD.values()
        ],
    ]
    corpus["counts"] = {
        "works_expected": len(remaining),
        "works_built": len(remaining),
        "published_version_associations": sum(
            record["publication_association"] != "NO_VERIFIED_CURRENT_VERSION_ASSOCIATION" for record in remaining
        ),
        "verified_provider_metadata_associations": sum(
            record["publication_association"] == "VERIFIED_PROVIDER_RECORD" for record in remaining
        ),
        "associated_but_metadata_unresolved": sum(
            record["publication_association"] == "PUBLISHED_VERSION_ASSOCIATED_METADATA_UNRESOLVED"
            for record in remaining
        ),
        "without_verified_current_version_association": sum(
            record["publication_association"] == "NO_VERIFIED_CURRENT_VERSION_ASSOCIATION" for record in remaining
        ),
        "reserved_accessions_withheld_from_public_projection": len(WITHHELD),
    }
    write_json(corpus_path, corpus)
    print("APPLIED: 195 public works; AC-0101, AC-0185, and AC-0192 remain reserved but are withheld from projection")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
