#!/usr/bin/env python3
"""Verify local corpus bundles and optionally refresh the repository manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


EXPECTED_PUBLIC_WORKS = 198
WITHHELD_WORK_IDS = {
    "AMCS-LOCAL-WORK-9CC31EEBBC3976CE",
    "AMCS-LOCAL-WORK-21CC00303A2E8D3C",
    "AMCS-LOCAL-WORK-02E0AB0D4874ACB3",
}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest().upper()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def repair_receipt_paths(root: Path) -> int:
    changed = 0
    for path in root.glob("papers/current/**/*.receipt.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        modified = False
        for key, source_set in (("predecessor", "corpus-199-heads/papers"), ("source_successor", "corpus-199-reference-successors-v0.1/papers")):
            item = data.get(key, {})
            absolute = item.pop("path", None)
            if absolute:
                item["logical_path"] = f"{source_set}/{Path(absolute).name}"
                modified = True
        if modified:
            write_json(path, data)
            changed += 1
    return changed


def verify(root: Path) -> list[str]:
    errors: list[str] = []
    corpus = json.loads((root / "metadata" / "corpus.json").read_text(encoding="utf-8"))
    accession_ledger = json.loads((root / "metadata" / "accession-ledger.json").read_text(encoding="utf-8"))
    papers = corpus.get("papers", [])
    if len(papers) != EXPECTED_PUBLIC_WORKS:
        errors.append(f"expected {EXPECTED_PUBLIC_WORKS} public metadata records, found {len(papers)}")
    project57 = [item for item in papers if item["title"].startswith("Project57")]
    if project57:
        errors.append("Project57 must not appear in the public corpus edition")
    leaked_withheld = [item for item in papers if item.get("work_id") in WITHHELD_WORK_IDS]
    if leaked_withheld:
        errors.append("author-withheld experimental works must not appear in the public corpus edition")
    semantic_debt = [item for item in papers if item["title"] == "Semantic Debt"]
    if len(semantic_debt) != 2 or len({item["work_id"] for item in semantic_debt}) != 2:
        errors.append("the two Semantic Debt work identities were not preserved")
    accessions = accession_ledger.get("accessions", [])
    if len(accessions) != 201:
        errors.append(f"expected 201 permanent accessions, found {len(accessions)}")
    numbers = [item.get("accession_number") for item in accessions]
    if numbers != list(range(1, 202)):
        errors.append("accession numbers are not the permanent contiguous sequence 1..201")
    if len({item.get("accession_id") for item in accessions}) != len(accessions):
        errors.append("duplicate accession identifiers")
    if len({item.get("work_id") for item in accessions}) != len(accessions):
        errors.append("duplicate work identities in accession ledger")
    chronology = [item.get("earliest_documented_timestamp", "") for item in accessions]
    if chronology != sorted(chronology):
        errors.append("initial accession sequence is not chronological")
    accession_by_work = {item["work_id"]: item for item in accessions}
    expected_public_numbers = [
        item.get("accession_number") for item in accessions if item.get("work_id") not in WITHHELD_WORK_IDS
    ]
    if [item.get("accession_number") for item in papers] != expected_public_numbers:
        errors.append("corpus metadata is not ordered by accession")
    for item in papers:
        accession = accession_by_work.get(item["work_id"])
        if not accession:
            errors.append(f"paper missing from accession ledger: {item['work_id']}")
            continue
        if item.get("accession_id") != accession.get("accession_id"):
            errors.append(f"accession mismatch for {item['work_id']}")
        receipt_path = root / item["receipt_path"]
        metadata_path = root / item["metadata_path"]
        if not receipt_path.is_file() or not metadata_path.is_file():
            errors.append(f"missing metadata or receipt for {item['work_id']}")
            continue
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        if receipt.get("accession_id") != item.get("accession_id"):
            errors.append(f"receipt accession mismatch for {item['work_id']}")
        if receipt.get("release_root_sha256") != item.get("release_root_sha256"):
            errors.append(f"release-root mismatch for {item['work_id']}")
        for role, record in item.get("formats", {}).items():
            artifact = root / record["path"]
            if f"papers/current/{item['accession_id']}-" not in record["path"]:
                errors.append(f"format path is not accession-stable: {record['path']}")
            if not artifact.is_file():
                errors.append(f"missing {role} for {item['work_id']}")
            elif digest(artifact) != record["sha256"]:
                errors.append(f"hash mismatch: {record['path']}")
        doi = item.get("doi")
        doi_match = re.fullmatch(r"(?:https?://doi\.org/)?(10\.5281/zenodo\.\d+)", doi or "", flags=re.I)
        provider_verified = item.get("provider_effect") == "ZENODO_PUBLISHED_VERIFIED"
        if provider_verified and not doi_match:
            errors.append(f"missing or invalid verified Zenodo DOI for {item['work_id']}: {doi!r}")
        elif provider_verified and doi_match:
            normalized_doi = doi_match.group(1)
            markdown_record = item.get("formats", {}).get("markdown", {})
            markdown_path = root / markdown_record.get("path", "")
            if markdown_path.is_file():
                markdown = markdown_path.read_text(encoding="utf-8")
                corpus_locator = (
                    "Corpus source and companion formats:  \n"
                    "[https://github.com/AblemanMosaic/ableman-corpus]"
                    "(https://github.com/AblemanMosaic/ableman-corpus)  \n"
                )
                doi_endings = {
                    f"DOI: [{normalized_doi}](https://doi.org/{normalized_doi})",
                    f"DOI: [https://doi.org/{normalized_doi}](https://doi.org/{normalized_doi})",
                }
                if corpus_locator not in markdown:
                    errors.append(f"corpus locator is not in approved two-line form: {markdown_record.get('path')}")
                if not any(markdown.rstrip().endswith(ending) for ending in doi_endings):
                    errors.append(f"verified DOI is not final Markdown end matter: {markdown_record.get('path')}")
            html_record = item.get("formats", {}).get("html", {})
            html_path = root / html_record.get("path", "")
            if html_path.is_file() and f"https://doi.org/{normalized_doi}" not in html_path.read_text(encoding="utf-8"):
                errors.append(f"verified DOI missing from HTML: {html_record.get('path')}")
        for key in ("predecessor", "source_successor"):
            source = receipt.get(key, {})
            if "path" in source or ":\\" in source.get("logical_path", ""):
                errors.append(f"machine-specific path in {item['receipt_path']}")
    return errors


def refresh_manifest(root: Path) -> str:
    files = []
    for path in sorted(root.rglob("*")):
        if (
            path.is_file()
            and ".candidate" not in path.parts
            and ".git" not in path.parts
            and "__pycache__" not in path.parts
            and "tmp" not in path.relative_to(root).parts
            and path.suffix != ".pyc"
            and path.name != "MANIFEST.json"
        ):
            files.append({"path": path.relative_to(root).as_posix(), "sha256": digest(path), "bytes": path.stat().st_size})
    manifest = {"schema": "ableman.corpus-local-build.v0.2", "files": files}
    manifest["content_root_sha256"] = hashlib.sha256(canonical_bytes(files)).hexdigest().upper()
    write_json(root / "MANIFEST.json", manifest)
    return manifest["content_root_sha256"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--repair-receipt-paths", action="store_true")
    parser.add_argument("--refresh-manifest", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.repair_receipt_paths:
        print(f"receipt paths repaired: {repair_receipt_paths(root)}")
    errors = verify(root)
    if errors:
        print("VERIFY: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VERIFY: PASS ({EXPECTED_PUBLIC_WORKS} public current-edition bundles; 3 accessions reserved and withheld)")
    if args.refresh_manifest:
        manifest_root = refresh_manifest(root)
        report_path = root / ".candidate" / "BUILD-REPORT.json"
        if report_path.is_file():
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["manifest_root_sha256"] = manifest_root
            report["post_build_verification"] = "PASS"
            write_json(report_path, report)
        print(f"manifest root: {manifest_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
