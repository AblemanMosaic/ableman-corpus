#!/usr/bin/env python3
"""Build a self-contained offline copy of the Bridge Atlas.

The generated HTML inlines the interface, map data, curation files, corpus
metadata, logo, and current Markdown papers. It performs no network requests.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "site-bridge" / "Ableman Corpus Atlas Offline.html"


def json_object(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def js_json(value) -> str:
    # A literal closing script tag must never be able to end the data block.
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def browser_file_href(path: str) -> str:
    safe = "-_.!~*'()"
    return "../" + "/".join(quote(part, safe=safe) for part in path.split("/"))


def inline_katex_fonts(css: str, katex_dir: Path) -> str:
    """Replace KaTeX font URLs with data URLs for the single-file edition."""

    def replace(match: re.Match[str]) -> str:
        rel = match.group(1)
        source = katex_dir / rel
        if not source.is_file():
            raise SystemExit(f"Missing KaTeX font: {source}")
        mime = mimetypes.guess_type(source.name)[0] or "application/octet-stream"
        payload = base64.b64encode(source.read_bytes()).decode("ascii")
        return f"url(data:{mime};base64,{payload})"

    return re.sub(r"url\((fonts/[^)]+)\)", replace, css)


def build(output: Path) -> dict:
    index = (ROOT / "site-bridge" / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "site-bridge" / "styles.css").read_text(encoding="utf-8")
    app = (ROOT / "site-bridge" / "app.js").read_text(encoding="utf-8")
    katex_dir = ROOT / "site-bridge" / "vendor" / "katex"
    katex_css = inline_katex_fonts((katex_dir / "katex.min.css").read_text(encoding="utf-8"), katex_dir)
    katex_js = (katex_dir / "katex.min.js").read_text(encoding="utf-8")
    auto_render_js = (katex_dir / "auto-render.min.js").read_text(encoding="utf-8")
    corpus = json_object(ROOT / "metadata" / "corpus.json")

    embedded = {
        "../metadata/corpus.json": corpus,
        "data/atlas.json": json_object(ROOT / "site-bridge" / "data" / "atlas.json"),
        "data/questions.json": json_object(ROOT / "site-bridge" / "data" / "questions.json"),
        "../curation/routes.json": json_object(ROOT / "curation" / "routes.json"),
        "../curation/depth.json": json_object(ROOT / "curation" / "depth.json"),
        "../curation/clusters.json": json_object(ROOT / "curation" / "clusters.json"),
        "../curation/tours.json": json_object(ROOT / "curation" / "tours.json"),
    }
    texts: dict[str, str] = {}
    missing: list[str] = []
    for paper in corpus["papers"]:
        rel = paper["formats"]["markdown"]["path"]
        source = ROOT / rel
        if not source.is_file():
            missing.append(rel)
            continue
        texts[browser_file_href(rel)] = source.read_text(encoding="utf-8-sig")
    if missing:
        raise SystemExit("Missing Markdown files: " + ", ".join(missing[:10]))

    logo_path = ROOT / "site" / "assets" / "mosaic-logo-1024.png"
    logo = "data:image/png;base64," + base64.b64encode(logo_path.read_bytes()).decode("ascii")
    index = re.sub(r'\s*<link rel="stylesheet" href="styles\.css[^\"]*">', "", index, count=1)
    index = re.sub(r'\s*<link rel="stylesheet" href="vendor/katex/katex\.min\.css[^\"]*">', "", index, count=1)
    index = re.sub(r'\s*<script src="app\.js[^\"]*"></script>', "", index, count=1)
    index = re.sub(r'\s*<script src="vendor/katex/katex\.min\.js[^\"]*"></script>', "", index, count=1)
    index = re.sub(r'\s*<script src="vendor/katex/auto-render\.min\.js[^\"]*"></script>', "", index, count=1)
    index = index.replace('../site/assets/mosaic-logo-1024.png', logo)

    style = "\n  <style>\n" + katex_css + "\n" + css + "\n  </style>"
    data = (
        "\n  <script>\n"
        "  window.__ABLEMAN_EMBEDDED__ = " + js_json(embedded) + ";\n"
        "  window.__ABLEMAN_TEXT__ = " + js_json(texts) + ";\n"
        "  </script>"
    )
    runtime = (
        "\n  <script>\n"
        + katex_js.replace("</script", "<\\/script")
        + "\n"
        + auto_render_js.replace("</script", "<\\/script")
        + "\n"
        + app.replace("</script", "<\\/script")
        + "\n  </script>"
    )
    index = index.replace("</head>", style + data + "\n</head>")
    index = index.replace("</body>", runtime + "\n</body>")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(index, encoding="utf-8", newline="\n")
    payload = output.read_text(encoding="utf-8")
    if 'src="app.js' in payload or 'href="styles.css' in payload or 'vendor/katex/' in payload:
        raise SystemExit("External interface assets remain in offline output")
    if "__ABLEMAN_EMBEDDED__" not in payload or "__ABLEMAN_TEXT__" not in payload:
        raise SystemExit("Offline data blocks are missing")
    return {"output": str(output), "bytes": output.stat().st_size, "papers": len(texts), "json_inputs": len(embedded)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    report = build(args.output.resolve())
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
