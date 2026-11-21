#!/usr/bin/env python3
"""Verify that public Markdown and rendered PDFs contain no review residue."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
from pathlib import Path

from publication_residue import scan_publication_residue


def pdf_text(path: Path, command: str | None) -> str:
    # Verify an exact copied byte stream at a short disposable locator instead
    # of shortening the paper's descriptive custody path.
    with tempfile.TemporaryDirectory(prefix="pdfverify-", dir=Path.cwd()) as temp_name:
        short_path = Path(temp_name) / "paper.pdf"
        shutil.copyfile(path, short_path)
        if command:
            import subprocess
            result = subprocess.run(
                [command, short_path.name, "-"], cwd=short_path.parent,
                capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
            if result.returncode:
                raise RuntimeError(result.stderr.strip() or f"pdftotext exit {result.returncode}")
            return result.stdout
        import fitz
        with fitz.open(short_path) as document:
            return "\n".join(page.get_text() for page in document)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--pdftotext", help="Optional explicit Poppler pdftotext executable")
    parser.add_argument("--expected-count", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    papers_root = root / "papers" / "current"
    markdown_files = sorted(papers_root.rglob("*.md"))
    pdf_files = sorted(papers_root.rglob("*.pdf"))
    findings: list[dict[str, object]] = []
    pdf_failures: list[dict[str, str]] = []
    token_markdown = token_pdf = 0
    for path in markdown_files:
        text = path.read_text(encoding="utf-8-sig")
        token_markdown += int("{{ZENODO_REPLACEMENT_DOI}}" in text)
        for finding in scan_publication_residue(text):
            findings.append({"format": "markdown", "path": str(path), **finding.as_dict()})
    for path in pdf_files:
        try:
            text = pdf_text(path, args.pdftotext)
        except Exception as error:
            pdf_failures.append({"path": str(path), "error": repr(error)})
            continue
        token_pdf += int("ZENODO_REPLACEMENT_DOI" in text)
        for finding in scan_publication_residue(text):
            findings.append({"format": "pdf", "path": str(path), **finding.as_dict()})
    report = {
        "schema": "ableman.publication-residue-verification.v0.1",
        "markdown_files": len(markdown_files),
        "pdf_files": len(pdf_files),
        "expected_count": args.expected_count,
        "replacement_doi_tokens": {"markdown": token_markdown, "pdf": token_pdf},
        "blocking_findings": findings,
        "pdf_extraction_failures": pdf_failures,
        "status": "PASS" if (
            len(markdown_files) == args.expected_count
            and len(pdf_files) == args.expected_count
            and not findings
            and not pdf_failures
        ) else "FAIL",
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
