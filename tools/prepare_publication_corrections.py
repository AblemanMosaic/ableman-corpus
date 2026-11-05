#!/usr/bin/env python3
"""Prepare a local, provider-closed correction candidate for the corpus.

The command copies an existing corpus projection, removes the author-withheld
AFS paper, remediates public-review residue, synchronizes known publication
metadata, renders every changed paper with plain Pandoc output mode, and emits
an exact same-DOI file-edit plan.  It never contacts Zenodo or GitHub.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from publication_residue import remediate_publication_projection, scan_publication_residue


AFS_WORK_ID = "AMCS-LOCAL-WORK-9CC31EEBBC3976CE"


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def safe_component(title: str, limit: int = 88) -> str:
    value = re.sub(r'[<>:"/\\|?*]', " - ", title)
    value = re.sub(r"\s+", " ", value).strip(" .")
    return value[:limit].rstrip(" .") or "Untitled"


def publication_rows(db_path: Path) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    connection = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    by_work: dict[str, dict[str, Any]] = {}
    by_title: dict[str, dict[str, Any]] = {}
    try:
        sql = """
        SELECT pm.associated_work_id, pm.title, pm.provider_record_id,
               COALESCE(pm.publication_date, pr.publication_date) AS publication_date,
               pr.doi, pr.provider_url, pr.provider, pr.imported_at
        FROM publication_metadata pm
        JOIN publication_records pr
          ON pr.provider=pm.provider AND pr.provider_record_id=pm.provider_record_id
        """
        for row in connection.execute(sql):
            item = dict(row)
            if item.get("associated_work_id"):
                by_work[item["associated_work_id"]] = item
            by_title[re.sub(r"\W+", " ", item["title"].casefold()).strip()] = item
    finally:
        connection.close()
    return by_work, by_title


def record_for(metadata: dict[str, Any], by_work: dict[str, dict[str, Any]], by_title: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    record = by_work.get(metadata["work_id"])
    if record:
        return record
    key = re.sub(r"\W+", " ", metadata["title"].casefold()).strip()
    return by_title.get(key)


def replace_doi_footer(text: str, doi: str | None) -> str:
    text = re.sub(r"(?ms)\n---\n\nDOI:\s*.*?\s*\Z", "", text.rstrip())
    if not doi:
        return text.rstrip() + "\n"
    normalized = re.sub(r"^https?://doi\.org/", "", doi, flags=re.I).strip()
    return text + f"\n\n---\n\nDOI: [{normalized}](https://doi.org/{normalized})\n"


def paper_files(directory: Path) -> tuple[Path, Path, Path, Path]:
    def one(pattern: str) -> Path:
        matches = list(directory.glob(pattern))
        if len(matches) != 1:
            raise ValueError(f"expected one {pattern} in {directory}, found {len(matches)}")
        return matches[0]
    return one("*.md"), one("*.pdf"), one("*.html"), one("*.receipt.json")


def render(md_bytes: bytes, prefix: str, temp_root: Path) -> tuple[bytes, bytes, str]:
    temp_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=prefix, dir=temp_root) as temp_name:
        temp = Path(temp_name)
        md_path = temp / "paper.md"
        pdf_path = temp / "paper.pdf"
        html_path = temp / "paper.html"
        md_path.write_bytes(md_bytes)
        for output in (pdf_path, html_path):
            result = subprocess.run(
                ["pandoc", str(md_path), "-o", str(output)],
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
            if result.returncode:
                raise RuntimeError(f"pandoc failed for {prefix}: {result.stderr.strip()}")
        version = subprocess.run(
            ["pandoc", "--version"], check=True, capture_output=True,
            text=True, encoding="utf-8",
        ).stdout.splitlines()[0]
        return pdf_path.read_bytes(), html_path.read_bytes(), version


def metadata_subject(metadata: dict[str, Any]) -> dict[str, Any]:
    excluded = {"formats", "release_root_sha256", "receipt_path", "metadata_path"}
    return {key: value for key, value in metadata.items() if key not in excluded}


def age_days(value: str | None) -> int | None:
    if not value:
        return None
    try:
        observed = date.fromisoformat(value[:10])
    except ValueError:
        return None
    return (datetime.now(timezone.utc).date() - observed).days


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--workbench-db", type=Path, required=True)
    args = parser.parse_args()

    source = args.source_repo.resolve()
    target = args.target.resolve()
    if source == target or source in target.parents:
        raise ValueError("target must be a separate sibling directory")
    if target.exists():
        raise FileExistsError(f"refusing to replace existing target: {target}")
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(".git", ".candidate", "tmp", "__pycache__"))

    by_work, by_title = publication_rows(args.workbench_db.resolve())
    corpus_path = target / "metadata" / "corpus.json"
    corpus = json.loads(corpus_path.read_text(encoding="utf-8"))
    original_papers = {item["work_id"]: item for item in corpus["papers"]}

    # The author explicitly withheld AFS pending its AMCAS successor treatment.
    for directory in (target / "papers" / "current").iterdir():
        if not directory.is_dir():
            continue
        metadata = json.loads((directory / "metadata.json").read_text(encoding="utf-8"))
        if metadata["work_id"] == AFS_WORK_ID:
            shutil.rmtree(directory)
    (target / "metadata" / "papers" / f"{AFS_WORK_ID}.json").unlink(missing_ok=True)

    results: list[dict[str, Any]] = []
    edit_plan: list[dict[str, Any]] = []
    final_records: list[dict[str, Any]] = []
    for directory in sorted((target / "papers" / "current").iterdir()):
        if not directory.is_dir():
            continue
        metadata_path = directory / "metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        md_path, pdf_path, html_path, receipt_path = paper_files(directory)
        original_text = md_path.read_text(encoding="utf-8-sig")
        before = scan_publication_residue(original_text)
        corrected, changes = remediate_publication_projection(original_text)
        after = scan_publication_residue(corrected)
        if after:
            raise ValueError(f"blocking publication residue remains in {md_path}: {after[:5]}")

        record = record_for(metadata, by_work, by_title)
        old_doi = (record or {}).get("doi") or metadata.get("doi")
        old_record_id = (record or {}).get("provider_record_id") or metadata.get("provider_record_id")
        old_provider_url = (record or {}).get("provider_url") or metadata.get("provider_url")
        needs_edit = bool(before)
        if needs_edit and (not record or not old_doi or not old_record_id):
            raise ValueError(f"published record association required for same-DOI edit: {metadata['accession_id']}")
        corrected = replace_doi_footer(corrected, old_doi)
        md_bytes = corrected.encode("utf-8")
        pdf_bytes, html_bytes, pandoc_version = render(
            md_bytes, f"ac-{metadata['accession_id']}-", target / ".render-tmp"
        )

        if record:
            normalized = re.sub(r"^https?://doi\.org/", "", record["doi"], flags=re.I)
            metadata["doi"] = f"https://doi.org/{normalized}"
            metadata["provider_record_id"] = record["provider_record_id"]
            metadata["provider_url"] = record["provider_url"]
            metadata["provider"] = record["provider"]
            metadata["publication_date"] = record["publication_date"]
            metadata["publication_association"] = "VERIFIED_PROVIDER_RECORD"

        md_hash = sha256_bytes(md_bytes)
        pdf_hash = sha256_bytes(pdf_bytes)
        html_hash = sha256_bytes(html_bytes)
        metadata_hash = sha256_bytes(canonical_bytes(metadata_subject(metadata)))
        recipe = {
            "pandoc_version": pandoc_version,
            "pdf_command": "pandoc INPUT.md -o OUTPUT.pdf",
            "html_command": "pandoc INPUT.md -o OUTPUT.html",
            "note": "No custom template, TeX option, or styling parameter was supplied.",
        }
        recipe_hash = sha256_bytes(canonical_bytes(recipe))
        root_subject = {
            "accession_id": metadata["accession_id"],
            "work_id": metadata["work_id"],
            "edition": "CURRENT_GITHUB_CORPUS_EDITION",
            "markdown_sha256": md_hash,
            "pdf_sha256": pdf_hash,
            "html_sha256": html_hash,
            "metadata_sha256": metadata_hash,
            "render_recipe_sha256": recipe_hash,
        }
        release_root = sha256_bytes(canonical_bytes(root_subject))
        basename = f"{safe_component(metadata['title'])} -- {release_root[:12]}"

        for path in (md_path, pdf_path, html_path, receipt_path):
            path.unlink()
        md_out = directory / f"{basename}.md"
        pdf_out = directory / f"{basename}.pdf"
        html_out = directory / f"{basename}.html"
        receipt_out = directory / f"{basename}.receipt.json"
        md_out.write_bytes(md_bytes)
        pdf_out.write_bytes(pdf_bytes)
        html_out.write_bytes(html_bytes)
        formats = {
            "markdown": {"path": md_out.relative_to(target).as_posix(), "sha256": md_hash, "bytes": len(md_bytes)},
            "pdf": {"path": pdf_out.relative_to(target).as_posix(), "sha256": pdf_hash, "bytes": len(pdf_bytes)},
            "html": {"path": html_out.relative_to(target).as_posix(), "sha256": html_hash, "bytes": len(html_bytes)},
        }
        metadata["release_root_sha256"] = release_root
        metadata["formats"] = formats
        metadata["receipt_path"] = receipt_out.relative_to(target).as_posix()
        metadata["metadata_path"] = metadata_path.relative_to(target).as_posix()
        prior_receipt = json.loads((source / original_papers[metadata["work_id"]]["receipt_path"]).read_text(encoding="utf-8"))
        receipt = {
            **prior_receipt,
            "release_root_sha256": release_root,
            "root_subject": root_subject,
            "formats": formats,
            "metadata_sha256": metadata_hash,
            "render_recipe": recipe,
            "projection_changes": prior_receipt.get("projection_changes", []) + [
                "Removed author-facing review-loop instructions and obsolete prepublication status language while retaining substantive integrations, evidence limits, open research questions, and AI/source-custody distinctions.",
                "Prepared a provider-closed same-DOI file-correction projection; the existing Zenodo DOI remains embedded and no replacement DOI is requested.",
            ],
            "non_effects": sorted(set(prior_receipt.get("non_effects", []) + ["ZENODO_MUTATION", "GITHUB_PUSH"])),
        }
        write_json(receipt_out, receipt)
        write_json(metadata_path, metadata)
        write_json(target / "metadata" / "papers" / f"{metadata['work_id']}.json", metadata)
        final_records.append(metadata)
        result = {
            "accession_id": metadata["accession_id"],
            "work_id": metadata["work_id"],
            "title": metadata["title"],
            "residue_findings_before": len(before),
            "residue_findings_after": len(after),
            "changes": changes,
            "same_doi_file_edit_required": needs_edit,
            "release_root_sha256": release_root,
        }
        results.append(result)
        if needs_edit:
            days = age_days((record or {}).get("publication_date") or metadata.get("publication_date"))
            edit_plan.append({
                "accession_id": metadata["accession_id"],
                "work_id": metadata["work_id"],
                "title": metadata["title"],
                "provider_record_id": old_record_id,
                "doi": old_doi,
                "provider_url": old_provider_url,
                "publication_date": (record or {}).get("publication_date") or metadata.get("publication_date"),
                "age_days_at_preparation": days,
                "self_service_file_edit_window_likely_open": days is not None and days <= 30,
                "prepared_markdown_path": formats["markdown"]["path"],
                "prepared_pdf_path": formats["pdf"]["path"],
                "expected_doi_after_edit": old_doi,
                "publish_effect": "NOT_AUTHORIZED",
            })

    final_records.sort(key=lambda item: item["accession_number"])
    corpus["papers"] = final_records
    corpus["excluded_by_author_ruling"].append({
        "title": "The Ableman Format Specification (AFS)",
        "reason": "AUTHOR_WITHHELD_PENDING_AMCAS_SUCCESSOR_REVIEW",
        "accession_id": "AC-0101",
    })
    corpus["counts"] = {
        **corpus.get("counts", {}),
        "works_expected": len(final_records),
        "works_built": len(final_records),
        "published_version_associations": sum(bool(item.get("doi")) for item in final_records),
        "verified_provider_metadata_associations": sum(item.get("publication_association") == "VERIFIED_PROVIDER_RECORD" for item in final_records),
        "replacement_doi_reservations_required": 0,
        "same_doi_file_edits_required": len(edit_plan),
        "reserved_accessions_withheld_from_public_projection": 3,
    }
    write_json(corpus_path, corpus)

    report_dir = target / "evidence" / "publication-residue-remediation-2026-11-05"
    report = {
        "schema": "ableman.publication-residue-remediation.v0.1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_repo": str(source),
        "candidate_repo": str(target),
        "integration_status": "SIDECAR_PARTIAL",
        "provider_effect": "NONE",
        "github_effect": "NONE",
        "counts": {
            "papers_in_candidate": len(final_records),
            "papers_with_blocking_residue_before": len(edit_plan),
            "papers_with_blocking_residue_after": 0,
            "afs_withheld": 1,
            "same_doi_file_edits_planned": len(edit_plan),
        },
        "results": results,
    }
    write_json(report_dir / "REMEDIATION-REPORT.json", report)
    write_json(report_dir / "ZENODO-SAME-DOI-EDIT-PLAN.json", {
        "schema": "ableman.zenodo-same-doi-edit-plan.v0.1",
        "effect_gate": "EXPLICIT_AUTHOR_AUTHORIZATION_REQUIRED",
        "ordering": [
            "read back the published record and bind its current DOI and file identity",
            "invoke the Zenodo edit action for the existing deposition",
            "verify the correction draft retains the same DOI and record identity",
            "replace the published PDF inside the correction draft with the exact prepared PDF",
            "verify the draft file hash and PDF-only file set",
            "publish the correction draft and independently read back the record",
            "refuse unless the DOI is unchanged and the corrected PDF hash matches",
            "rebuild GitHub corpus with the unchanged verified DOI",
            "replace Git history with one canonical commit only after separate GitHub effect verification",
        ],
        "records": edit_plan,
    })
    shutil.rmtree(target / ".render-tmp", ignore_errors=True)
    print(json.dumps(report["counts"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
