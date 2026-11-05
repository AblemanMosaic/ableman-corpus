#!/usr/bin/env python3
"""Read every generated PDF and report structural page coverage."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

import pdfplumber
from pypdf import PdfReader


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1] / "papers" / "current")
    parser.add_argument("--layout-bounds", action="store_true", help="Inspect extracted word boxes for page-boundary overflow.")
    parser.add_argument("--summary-only", action="store_true", help="Omit individual overflow samples from the report.")
    parser.add_argument("--stop-after-overflows", type=int, default=0, help="Stop a diagnostic sample after this many overflow boxes; zero scans all pages.")
    parser.add_argument("--output", type=Path, help="Write the JSON report to this path as well as stdout.")
    parser.add_argument("--paths-from-report", type=Path, help="Scan only paths listed in top_out_of_page_pdfs in an earlier report.")
    parser.add_argument("--expected-count", type=int, default=196, help="Expected number of PDFs in a full public-edition scan.")
    args = parser.parse_args()
    if args.paths_from_report:
        prior = json.loads(args.paths_from_report.read_text(encoding="utf-8"))
        files = [Path(item["path"]) for item in prior.get("top_out_of_page_pdfs", [])]
    else:
        files = sorted(args.root.rglob("*.pdf"))
    failures = []
    overflow = []
    overflow_count = 0
    overflow_by_pdf: Counter[str] = Counter()
    counts = []
    truncated = False
    for path in files:
        try:
            count = len(PdfReader(str(path)).pages)
            counts.append(count)
            if count < 1:
                failures.append({"path": str(path), "error": "zero pages"})
        except Exception as error:  # diagnostic boundary
            failures.append({"path": str(path), "error": repr(error)})
        if args.layout_bounds:
            try:
                with pdfplumber.open(path) as document:
                    for page_number, page in enumerate(document.pages, 1):
                        for word in page.extract_words():
                            if word["x0"] < -0.5 or word["x1"] > page.width + 0.5 or word["top"] < -0.5 or word["bottom"] > page.height + 0.5:
                                overflow_count += 1
                                overflow_by_pdf[str(path)] += 1
                                if len(overflow) < 50:
                                    overflow.append({"path": str(path), "page": page_number, "text": word["text"], "x0": word["x0"], "x1": word["x1"], "width": page.width})
                                if args.stop_after_overflows and overflow_count >= args.stop_after_overflows:
                                    truncated = True
                                    break
                        if truncated:
                            break
            except Exception as error:
                failures.append({"path": str(path), "error": f"layout inspection: {error!r}"})
        if truncated:
            break
    report = {
        "pdfs": len(files),
        "total_pages": sum(counts),
        "minimum_pages": min(counts) if counts else 0,
        "maximum_pages": max(counts) if counts else 0,
        "failures": failures,
        "out_of_page_word_box_count": overflow_count,
        "out_of_page_pdf_count": len(overflow_by_pdf),
        "top_out_of_page_pdfs": [
            {"path": path, "word_boxes": count}
            for path, count in overflow_by_pdf.most_common(20)
        ],
        "out_of_page_word_boxes": [] if args.summary_only else overflow,
        "scan_truncated": truncated,
        "status": "PASS" if (args.paths_from_report or len(files) == args.expected_count) and not failures and overflow_count == 0 else "FAIL",
    }
    rendered = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
