#!/usr/bin/env python3
"""Build the public Ableman Corpus GitHub edition.

This is a projection builder. It never changes governed source heads, contacts a
provider, or assigns author standing. It copies the authorized current
reference-successor set, removes review-only custody appendices from the public
paper body while preserving their source hashes in detached receipts, adds the
repository locator, renders with plain ``pandoc INPUT -o OUTPUT`` commands, and
emits representation-specific hashes under one release root.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import html
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from publication_residue import remediate_publication_projection, scan_publication_residue


REPOSITORY_URL = "https://github.com/AblemanMosaic/ableman-corpus"
AUTHOR = "Adam Ableman"
PAPER_LICENSE = "CC-BY-ND-4.0"
BUILD_SCHEMA = "ableman.corpus-local-build.v0.2"
RECEIPT_SCHEMA = "ableman.corpus-paper-receipt.v0.2"
EXCLUDED_TITLE_PREFIXES = ("Project57",)
WITHHELD_PUBLIC_WORK_IDS = {
    "AMCS-LOCAL-WORK-9CC31EEBBC3976CE": {
        "accession_id": "AC-0101",
        "title": "The Ableman Format Specification (AFS)",
        "reason": "AUTHOR_WITHHELD_PENDING_AMCAS_SUCCESSOR_REVIEW",
    },
    "AMCS-LOCAL-WORK-21CC00303A2E8D3C": {
        "accession_id": "AC-0185",
        "title": "Technical Brief: Context-Compiled Consciousness Mode for Language Models",
        "reason": "AUTHOR_WITHHELD_PENDING_INDEPENDENT_PROJECT57_REPLICATION_AND_EXTERNAL_SOURCE_REVIEW",
    },
    "AMCS-LOCAL-WORK-02E0AB0D4874ACB3": {
        "accession_id": "AC-0192",
        "title": "Qualia Binding and Realization Mapping",
        "reason": "AUTHOR_WITHHELD_PENDING_EMPIRICAL_DATA_BASELINES_ETHICS_AND_EXTERNAL_SCHOLARLY_REVIEW",
    },
}

PROFILE_TERRITORIES = {
    "Intelligence": {"ai", "consciousness", "semantic", "observation", "reasoning"},
    "Computation": {"formal", "software", "security", "crypto", "open-sovereign", "storage", "token", "cps", "distributed"},
    "Coordination": {"governance", "provenance", "markets", "trade", "voting", "institutional"},
    "Possibility": {"semantic", "formal", "consciousness", "craft", "energy", "earth", "time", "possibility"},
}


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


def logicalize_local_paths(value: Any) -> Any:
    """Remove workstation-specific roots from copied semantic metadata."""
    if isinstance(value, dict):
        return {key: logicalize_local_paths(item) for key, item in value.items()}
    if isinstance(value, list):
        return [logicalize_local_paths(item) for item in value]
    if isinstance(value, str) and re.match(r"^[A-Za-z]:[\\/]", value):
        filename = re.split(r"[\\/]", value.rstrip("\\/"))[-1]
        return f"external-source/{filename}"
    return value


def copy_public_json(source: Path, destination: Path) -> None:
    write_json(destination, logicalize_local_paths(json.loads(source.read_text(encoding="utf-8-sig"))))


def copy_public_jsonl(source: Path, destination: Path) -> None:
    rows = []
    for line in source.read_text(encoding="utf-8-sig").splitlines():
        if line.strip():
            rows.append(json.dumps(logicalize_local_paths(json.loads(line)), ensure_ascii=False, separators=(",", ":")))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(rows) + "\n", encoding="utf-8")


def safe_component(title: str, limit: int = 88) -> str:
    value = re.sub(r'[<>:"/\\|?*]', " - ", title)
    value = re.sub(r"\s+", " ", value).strip(" .")
    return value[:limit].rstrip(" .") or "Untitled"


def short_slug(title: str, limit: int = 52) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return (value[:limit].rstrip("-") or "paper")


def parse_json(value: str | None, fallback: Any) -> Any:
    if not value:
        return fallback
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return fallback


def strip_tags(value: str) -> str:
    value = re.sub(r"<br\s*/?>", "\n", value or "", flags=re.I)
    value = re.sub(r"</p\s*>", "\n\n", value, flags=re.I)
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value).strip()


def split_top_level(value: str, delimiter: str = ",") -> list[str]:
    """Split a compact expression without cutting nested argument lists."""
    parts: list[str] = []
    start = 0
    round_depth = square_depth = brace_depth = 0
    for index, char in enumerate(value):
        if char == "(":
            round_depth += 1
        elif char == ")" and round_depth:
            round_depth -= 1
        elif char == "[":
            square_depth += 1
        elif char == "]" and square_depth:
            square_depth -= 1
        elif char == "{":
            brace_depth += 1
        elif char == "}" and brace_depth:
            brace_depth -= 1
        elif char == delimiter and not (round_depth or square_depth or brace_depth):
            parts.append(value[start:index].strip())
            start = index + 1
    parts.append(value[start:].strip())
    return [part for part in parts if part]


def pack_items(items: list[str], width: int = 56) -> list[str]:
    groups: list[str] = []
    current = ""
    for item in items:
        candidate = f"{current}, {item}" if current else item
        if current and len(candidate) > width:
            groups.append(current)
            current = item
        else:
            current = candidate
    if current:
        groups.append(current)
    return groups


MATH_BREAK_OPERATORS = (
    r"\parallel",
    r"\mid",
    r"\Longrightarrow",
    r"\Rightarrow",
    r"\rightarrow",
    r"\neq",
    r"\ne",
    r"\implies",
    r"\iff",
    r"\land",
    r"\lor",
)


def split_top_level_operators(value: str) -> list[str]:
    """Return alternating terms/operators, ignoring operators inside groups."""
    result: list[str] = []
    start = index = 0
    round_depth = square_depth = brace_depth = 0
    while index < len(value):
        char = value[index]
        if char == "(":
            round_depth += 1
        elif char == ")" and round_depth:
            round_depth -= 1
        elif char == "[":
            square_depth += 1
        elif char == "]" and square_depth:
            square_depth -= 1
        elif char == "{":
            brace_depth += 1
        elif char == "}" and brace_depth:
            brace_depth -= 1
        if not (round_depth or square_depth or brace_depth):
            operator = next((item for item in MATH_BREAK_OPERATORS if value.startswith(item, index)), None)
            if operator:
                result.extend((value[start:index].strip(), operator))
                index += len(operator)
                start = index
                continue
        index += 1
    if result:
        result.append(value[start:].strip())
    return result


def wrap_display_math(match: re.Match[str]) -> str:
    """Give long display formulas explicit, content-preserving line breaks."""
    body = match.group(1).strip()
    if "\\begin{aligned}" in body:
        repaired = re.sub(r"(?m)(?<!\\)\\\s*$", r"\\\\", body)
        return "$$\n" + repaired + "\n$$"
    if "\\begin{" in body or "&" in body:
        return match.group(0)
    compact = re.sub(r"\s+", " ", body)
    if len(compact) <= 76:
        return match.group(0)

    tag = ""
    tag_match = re.search(r"\s*(\\tag\{[^{}]*\})\s*$", compact)
    if tag_match:
        tag = tag_match.group(1)
        compact = compact[:tag_match.start()].rstrip()

    punctuation = ""
    if compact[-1:] in ".,;:":
        punctuation, compact = compact[-1], compact[:-1].rstrip()

    tuple_match = re.match(r"^(.*?=)\s*(?:\\left)?\((.*?)(?:\\right)?\)$", compact)
    if tuple_match:
        left = tuple_match.group(1).strip()
        items = split_top_level(tuple_match.group(2))
        if len(items) >= 3:
            groups = pack_items(items)
            lines = []
            for index, group in enumerate(groups):
                prefix = f"{left} (&" if index == 0 else "&"
                suffix = "," if index < len(groups) - 1 else ")"
                if index < len(groups) - 1:
                    suffix += r" \\"
                lines.append(f"{prefix}{group}{suffix}")
            return "$$\n\\begin{aligned}\n" + "\n".join(lines) + f"\n\\end{{aligned}}{tag}{punctuation}\n$$"

    angle_match = None
    if compact.count(r"\langle") == 1 and compact.count(r"\rangle") == 1:
        angle_match = re.match(r"^(.*?=)\s*(?:\\left)?\\langle(.*?)(?:\\right)?\\rangle$", compact)
    if angle_match:
        left = angle_match.group(1).strip()
        items = split_top_level(angle_match.group(2))
        if len(items) >= 3:
            groups = pack_items(items)
            lines = []
            for index, group in enumerate(groups):
                prefix = f"{left} \\langle &" if index == 0 else "&"
                suffix = "," if index < len(groups) - 1 else r"\rangle"
                if index < len(groups) - 1:
                    suffix += r" \\"
                lines.append(f"{prefix}{group}{suffix}")
            return "$$\n\\begin{aligned}\n" + "\n".join(lines) + f"\n\\end{{aligned}}{tag}{punctuation}\n$$"

    set_match = None
    if compact.count(r"\{") == 1 and compact.count(r"\}") == 1:
        set_match = re.match(r"^(.*?)(?:\\left)?\\\{(.*?)(?:\\right)?\\\}$", compact)
    if set_match:
        items = split_top_level(set_match.group(2))
        if len(items) >= 4:
            groups = pack_items(items)
            lines = []
            for index, group in enumerate(groups):
                prefix = f"{set_match.group(1)}\\{{&" if index == 0 else "&"
                suffix = "," if index < len(groups) - 1 else r"\}"
                if index < len(groups) - 1:
                    suffix += r" \\"
                lines.append(f"{prefix}{group}{suffix}")
            return "$$\n\\begin{aligned}\n" + "\n".join(lines) + f"\n\\end{{aligned}}{tag}{punctuation}\n$$"

    pieces = split_top_level_operators(compact)
    if len(pieces) >= 5:
        lines = [f"&{pieces[0].strip()}" + r" \\"]
        for index in range(1, len(pieces), 2):
            operator = pieces[index]
            term = pieces[index + 1].strip()
            suffix = r" \\" if index + 2 < len(pieces) else ""
            lines.append(f"&{operator} {term}{suffix}")
        return "$$\n\\begin{aligned}\n" + "\n".join(lines) + f"\n\\end{{aligned}}{tag}{punctuation}\n$$"

    comma_items = split_top_level(compact)
    if len(comma_items) >= 4 and "\\left" not in compact and "\\right" not in compact:
        groups = pack_items(comma_items)
        lines = []
        for index, group in enumerate(groups):
            suffix = "," if index < len(groups) - 1 else ""
            if index < len(groups) - 1:
                suffix += r" \\"
            lines.append(f"&{group}{suffix}")
        return "$$\n\\begin{aligned}\n" + "\n".join(lines) + f"\n\\end{{aligned}}{tag}{punctuation}\n$$"

    return match.group(0)


def table_cells(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    cells: list[str] = []
    start = 0
    in_code = False
    in_math = False
    index = 0
    while index < len(value):
        char = value[index]
        escaped = index > 0 and value[index - 1] == "\\"
        if char == "`" and not escaped:
            in_code = not in_code
        elif char == "$" and not escaped and not in_code:
            in_math = not in_math
        elif char == "|" and not escaped and not in_code and not in_math:
            cells.append(value[start:index].strip())
            start = index + 1
        index += 1
    cells.append(value[start:].strip())
    return cells


def table_requires_records(block: list[str]) -> bool:
    rows = [table_cells(line) for line in block]
    column_count = max((len(row) for row in rows), default=0)
    content_rows = rows[2:]
    for row in content_rows:
        for cell in row:
            plain = re.sub(r"[`*_]", "", cell)
            if any(len(token) > 28 for token in re.findall(r"[^\s]+", plain)):
                return True
    minimum_width = 0
    for column in range(column_count):
        values = [row[column] if column < len(row) else "" for row in rows]
        minimum_width += min(28, max((len(re.sub(r"[`*_]", "", item)) for item in values), default=0))
    return column_count >= 3 or (column_count == 2 and minimum_width > 76)


def table_to_records(block: list[str]) -> list[str]:
    rows = [table_cells(line) for line in block]
    headers = rows[0]
    output: list[str] = []
    for row_index, row in enumerate(rows[2:], 1):
        fields = []
        for column, header in enumerate(headers):
            value = row[column] if column < len(row) else ""
            if value:
                fields.append((header or f"Field {column + 1}", value))
        if not fields:
            continue
        output.append(f"- **{fields[0][0]}:** {fields[0][1]}  ")
        for label, value in fields[1:]:
            output.append(f"  **{label}:** {value}  ")
        output[-1] = output[-1].rstrip()
        if row_index < len(rows) - 2:
            output.append("")
    return output


def normalize_wide_tables(text: str) -> str:
    lines = text.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        if index + 1 < len(lines) and "|" in lines[index] and re.match(r"^\s*\|?\s*:?-{3,}", lines[index + 1]):
            end = index + 2
            while end < len(lines) and "|" in lines[end] and lines[end].strip():
                end += 1
            block = lines[index:end]
            if table_requires_records(block):
                output.extend(table_to_records(block))
            else:
                output.extend(block)
            index = end
            continue
        output.append(lines[index])
        index += 1
    return "\n".join(output)


def split_machine_token(value: str, width: int = 46) -> list[str]:
    if len(value) <= width:
        return [value]
    pieces = re.findall(r".*?(?:[/\\_-]|$)", value)
    pieces = [piece for piece in pieces if piece]
    if len(pieces) <= 1:
        return [value[index:index + width] for index in range(0, len(value), width)]
    chunks: list[str] = []
    current = ""
    for piece in pieces:
        if current and len(current) + len(piece) > width:
            chunks.append(current)
            current = piece
        else:
            current += piece
        while len(current) > width:
            chunks.append(current[:width])
            current = current[width:]
    if current:
        chunks.append(current)
    return chunks


def normalize_text_fences(text: str) -> str:
    """Reflow presentation-only fenced blocks that contain indivisible long lines."""
    pattern = re.compile(r"(?ms)^```([^\n]*)\n(.*?)\n```$")

    def replace(match: re.Match[str]) -> str:
        output: list[str] = []
        for line in match.group(2).splitlines():
            if len(line) <= 72:
                output.append(line)
                continue
            leading = re.match(r"^\s*", line).group(0)
            content = line[len(leading):]
            assignment = re.match(r"^([^=]+=\{)(.*)(\}\s*)$", content)
            if assignment:
                items = split_top_level(assignment.group(2))
                groups = pack_items(items, 60)
                output.append(leading + assignment.group(1))
                for index, group in enumerate(groups):
                    suffix = "," if index < len(groups) - 1 else ""
                    output.append(f"{leading}  {group}{suffix}")
                output.append(leading + assignment.group(3))
                continue
            if "," in content and ("=" in content or "(" in content or "{" in content):
                items = split_top_level(content)
                if len(items) < 2:
                    items = []
            else:
                items = []
            if items:
                groups = pack_items(items, 68)
                for index, group in enumerate(groups):
                    output.append(leading + group + ("," if index < len(groups) - 1 else ""))
                continue
            words = content.split()
            if len(words) > 1:
                current = ""
                for word in words:
                    candidate = f"{current} {word}".strip()
                    if current and len(candidate) > 68:
                        output.append(leading + current)
                        current = word
                    else:
                        current = candidate
                if current:
                    output.append(leading + current)
                continue
            output.extend(leading + item for item in split_machine_token(content, 58))
        return "```" + match.group(1) + "\n" + "\n".join(output) + "\n```"

    return pattern.sub(replace, text)


def wrap_code_span_lists(line: str) -> str:
    if len(line) <= 108 or line.count("`") < 4:
        return line
    segments = re.split(r"(?<=`),\s+", line)
    if len(segments) < 3:
        spans = list(re.finditer(r"`[^`]+`", line))
        if len(spans) < 2:
            return line
        split_at = spans[1].start()
        indent = re.match(r"^\s*", line).group(0)
        return line[:split_at].rstrip() + "\n\n" + indent + line[split_at:]
    output: list[str] = []
    current = ""
    indent = re.match(r"^\s*", line).group(0)
    for index, segment in enumerate(segments):
        piece = segment + ("," if index < len(segments) - 1 else "")
        candidate = f"{current} {piece}".strip() if current else piece
        if current and len(candidate) > 92:
            output.append(current)
            current = piece
        else:
            current = candidate
    if current:
        output.append(current)
    return ("  \n" + indent).join(output)


def wrap_machine_tokens(text: str) -> str:
    """Wrap long exact locators without modifying the governed source file."""
    text = re.sub(
        r"(?<!`)(\b[A-Za-z0-9][A-Za-z0-9_.-]{48,}\.md\b)(?!`)",
        lambda match: "`" + match.group(1) + "`",
        text,
    )
    text = re.sub(
        r";\s*source SHA-256\s+(`?[A-Fa-f0-9]{64}`?)",
        lambda match: ";  \nsource SHA-256  \n" + match.group(1),
        text,
    )
    text = re.sub(
        r",\s*SHA-256\s+(`?[A-Fa-f0-9]{64}`?)",
        lambda match: ",  \nSHA-256  \n" + match.group(1),
        text,
    )
    text = re.sub(
        r"(SHA-256)\s+(`?[A-Fa-f0-9]{64}`?)",
        lambda match: match.group(1) + "  \n" + match.group(2),
        text,
    )
    text = re.sub(
        r"(?m)^(\s*[*+-])\s+(`[^`]{20,}`)\s+(.{60,})$",
        lambda match: f"{match.group(1)} {match.group(2)}  \n  {match.group(3)}",
        text,
    )
    lines = text.splitlines()
    output: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            output.append(line)
            continue
        if in_fence or line.strip() in {"$$"} or "\\begin{aligned}" in line:
            output.append(line)
            continue

        indent = re.match(r"^\s*", line).group(0)

        def replace(match: re.Match[str]) -> str:
            value = match.group(1)
            continuation = indent + ("  " if line.lstrip().startswith(('-', '*', '+')) else "")
            prefix = "  \n" + continuation if match.start() > 0 and line[:match.start()].strip() else ""
            if len(value) <= 42:
                if len(line) > 100 and len(value) >= 20 and prefix:
                    return prefix + match.group(0)
                return match.group(0)
            if re.fullmatch(r"[A-Fa-f0-9]{64}", value):
                return prefix + match.group(0)
            chunks = split_machine_token(value)
            return prefix + ("`  \n" + continuation + "`").join(chunks).join(("`", "`"))

        output.append(wrap_code_span_lists(re.sub(r"`([^`\r\n]+)`", replace, line)))
    return "\n".join(output)


def compact_long_urls(text: str) -> str:
    """Keep long URL targets while using a compact visible link label."""
    pattern = re.compile(r"(?<!\]\()(?<!<)(https?://[^\s)>]+)")
    def replace(match: re.Match[str]) -> str:
        url = match.group(1).rstrip(".,;")
        punctuation = match.group(1)[len(url):]
        if len(url) <= 54:
            return match.group(0)
        domain = re.sub(r"^www\.", "", re.match(r"https?://([^/]+)", url).group(1), flags=re.I)
        return f"[{domain} source]({url}){punctuation}"
    return pattern.sub(replace, text)


def normalize_layout_projection(text: str) -> str:
    text = normalize_wide_tables(text)
    text = re.sub(r"(?ms)^\$\$\s*\n?(.*?)\n?\s*\$\$$", wrap_display_math, text)
    text = normalize_text_fences(text)
    text = wrap_machine_tokens(text)
    return compact_long_urls(text)


def classify_territories(profiles: list[str]) -> list[str]:
    lower = {item.lower() for item in profiles}
    result = [name for name, terms in PROFILE_TERRITORIES.items() if lower & terms]
    return result or ["Possibility"]


def query_metadata(db_path: Path) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    connection = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    published: dict[str, dict[str, Any]] = {}
    drafts: dict[str, dict[str, Any]] = {}
    try:
        sql = """
            SELECT pm.associated_work_id, pm.title, pm.description, pm.creators_json,
                   pm.keywords_json, pm.license_id, pm.resource_type, pm.version,
                   pm.language, pm.publication_date, pr.doi, pr.provider_url,
                   pr.provider, pr.provider_record_id
            FROM publication_metadata pm
            LEFT JOIN publication_records pr
              ON pr.provider=pm.provider AND pr.provider_record_id=pm.provider_record_id
        """
        for row in connection.execute(sql):
            value = dict(row)
            value["_publication_binding"] = "VERIFIED_PROVIDER_RECORD"
            published[row["associated_work_id"]] = value
        # A work-level publication binding may be governed even when the imported
        # provider artifact remains a separately preserved exact-work identity.
        # This is intentionally a typed fallback, not an identity merge.
        work_sql = """
            SELECT work_id, title, doi, provider, provider_record_id,
                   provider_url, metadata_json
            FROM works
            WHERE publication_status='PUBLISHED_VERSION_ASSOCIATED'
              AND doi IS NOT NULL
        """
        for row in connection.execute(work_sql):
            if row["work_id"] in published:
                continue
            metadata = parse_json(row["metadata_json"], {})
            publication = metadata.get("publication", {}) if isinstance(metadata, dict) else {}
            published[row["work_id"]] = {
                "associated_work_id": row["work_id"],
                "title": row["title"],
                "publication_date": publication.get("publication_date"),
                "doi": row["doi"],
                "provider": row["provider"],
                "provider_record_id": row["provider_record_id"],
                "provider_url": row["provider_url"],
                "_publication_binding": "VERIFIED_WORK_PUBLICATION_BINDING",
            }
        for row in connection.execute("SELECT * FROM work_metadata_drafts"):
            drafts[row["work_id"]] = dict(row)
    finally:
        connection.close()
    return published, drafts


def metadata_for(entry: dict[str, Any], audit: dict[str, Any], published: dict[str, dict[str, Any]], drafts: dict[str, dict[str, Any]], accession: dict[str, Any]) -> dict[str, Any]:
    work_id = entry["work_id"]
    source = {**(drafts.get(work_id) or {}), **(published.get(work_id) or {})}
    raw_doi = (source.get("doi") or "").strip()
    doi_url = (
        raw_doi
        if re.match(r"^https?://", raw_doi, flags=re.I)
        else f"https://doi.org/{raw_doi}"
        if raw_doi
        else None
    )
    description_html = source.get("description") or f"<p>{html.escape(audit.get('abstract') or '')}</p>"
    if work_id in published:
        publication_association = source.get("_publication_binding", "VERIFIED_PROVIDER_RECORD")
    elif entry.get("publication_status") == "PUBLISHED_VERSION_ASSOCIATED":
        publication_association = "PUBLISHED_VERSION_ASSOCIATED_METADATA_UNRESOLVED"
    else:
        publication_association = "NO_VERIFIED_CURRENT_VERSION_ASSOCIATION"
    publication_readiness = "GITHUB_CORPUS_RELEASE_AUTHORIZED"
    return {
        "accession_id": accession["accession_id"],
        "accession_number": accession["accession_number"],
        "accession_frozen": accession["accession_frozen"],
        "work_id": work_id,
        "title": entry["title"],
        "authors": [AUTHOR],
        "description_html": description_html,
        "abstract_text": strip_tags(description_html) or (audit.get("abstract") or ""),
        "keywords": parse_json(source.get("keywords_json"), []),
        "license": source.get("license_id") or "cc-by-nd-4.0",
        "resource_type": source.get("resource_type") or "publication-paper",
        "version": source.get("version") or "1.0",
        "language": source.get("language") or "eng",
        "publication_date": source.get("publication_date"),
        "earliest_documented_date": accession["earliest_documented_date"],
        "earliest_documented_timestamp": accession["earliest_documented_timestamp"],
        "chronology_basis": accession["chronology_basis"],
        "chronology_confidence": accession["chronology_confidence"],
        "first_publication_date": accession["first_publication_date"],
        "first_complete_draft_date": accession["first_complete_draft_date"],
        "work_origin_date": accession["work_origin_date"],
        "corpus_admission_date": accession["corpus_admission_date"],
        "chronology_evidence": accession["chronology_evidence"],
        "doi": doi_url,
        "provider_url": source.get("provider_url"),
        "provider": source.get("provider"),
        "provider_record_id": source.get("provider_record_id"),
        "publication_association": publication_association,
        "publication_readiness": publication_readiness,
        "profiles": entry.get("profiles", []),
        "territories": classify_territories(entry.get("profiles", [])),
        "external_source_ids": entry.get("external_source_ids", []),
        "internal_work_ids": entry.get("internal_work_ids", []),
        "reference_count": audit.get("reference_count", 0),
        "external_reference_count": audit.get("external_reference_count", 0),
        "internal_reference_count": audit.get("internal_reference_count", 0),
        "has_related_work_section": bool(audit.get("has_related_work_section")),
        "standing": entry.get("standing"),
        "publication_effect": "GITHUB_CORPUS_PUBLICATION_AUTHORIZED",
        "provider_effect": "NONE",
    }


def local_markdown(source: Path, doi: str | None) -> bytes:
    text = source.read_text(encoding="utf-8-sig").rstrip()
    for legacy_name in ("Ableman Mazurk, Adam", "Mazurk, Adam Ableman", "Mazurk, A. A.", "Mazurk, A."):
        text = text.replace(legacy_name, AUTHOR)
    text = re.sub(r"\bMazurk\b", "Ableman", text)
    text = re.sub(
        r"`([A-Za-z]:[\\/][^`\r\n]+)`",
        lambda match: f"`source-material/{Path(match.group(1)).name}`",
        text,
    )
    text = re.sub(r"(?ms)\n## Reference-pass custody note\s*\n.*\Z", "", text).rstrip()
    text = re.sub(r"(?i)\bunpublished\s+working\s+paper\b", "Ableman Corpus edition", text)
    text = re.sub(r"(?i)\bunpublished\s+manuscript\b", "Ableman Corpus edition", text)
    text = re.sub(r"(?i)\bunpublished author-review current head\b", "Ableman Corpus current edition", text)
    text = re.sub(r"(?i)\bpublished-associated current head\b", "Ableman Corpus current edition", text)
    text = re.sub(
        r"(?i)\bUnpublished author-review candidate; publication and canonical standing not granted\.",
        "Ableman Corpus current edition; conceptual claims retain the standing stated in the work.",
        text,
    )
    text = re.sub(
        r"(?i)\bUnpublished corpus work; publication and canonical standing not granted\.",
        "Ableman Corpus current edition; conceptual claims retain the standing stated in the work.",
        text,
    )
    text = re.sub(
        r"(?i)\bUnpublished author-review candidate in the historical (.*?); publication and canonical standing not granted\.",
        r"Ableman Corpus current edition in the historical \1; conceptual claims retain the standing stated in the work.",
        text,
    )
    text = re.sub(
        r"(?i)\bUnpublished corpus lineage under (.*?); publication and canonical standing not granted\.",
        r"Ableman Corpus current edition in \1; conceptual claims retain the standing stated in the work.",
        text,
    )
    text = re.sub(
        r"(?i)\bUnpublished author-review candidate developed through the historical (.*?); publication and canonical standing not granted\.",
        r"Authorized Ableman Corpus edition developed through the historical \1; canonical concept standing remains governed separately from publication.",
        text,
    )
    text = re.sub(
        r"(?i)\bUnpublished author-review candidate in the current corpus program; publication and canonical standing not granted\.",
        "Authorized Ableman Corpus current edition; canonical concept standing remains governed separately from publication.",
        text,
    )
    text = re.sub(
        r"(?i)\bUnpublished author-review candidate; (?:publication and canonical|canonical and publication) standing not granted\.",
        "Authorized Ableman Corpus current edition; canonical concept standing remains governed separately from publication.",
        text,
    )
    text = re.sub(
        r"(?i)\bUnpublished author-review candidate; publication standing not granted\.",
        "Authorized Ableman Corpus current edition; canonical concept standing remains governed separately from publication.",
        text,
    )
    text = re.sub(r"(?i)\bUnpublished author manuscript\b", "Ableman Corpus edition", text)
    text = re.sub(r"(?i)\bUnpublished research framework\b", "Ableman Corpus edition", text)
    text = re.sub(
        r"(?i)\bWorking system architecture and release lineage, unpublished\.",
        "Ableman Corpus edition and system release lineage.",
        text,
    )
    text = re.sub(
        r"(?i)\bCurrent corpus terminology under (.*?); publication and canonical standing not granted by that terminology ruling\.",
        r"Current corpus terminology under \1; publication does not alter the separate terminology or concept-standing ruling.",
        text,
    )
    text = re.sub(r"(?i)\bUnpublished working theory\b", "Ableman Corpus edition", text)
    text = text.replace("Source-head Ableman references retained under original labels", "Ableman Corpus references")
    text, _ = remediate_publication_projection(text)
    residue = scan_publication_residue(text)
    if residue:
        summary = "; ".join(f"{item.code}@{item.line}" for item in residue[:12])
        raise ValueError(f"publication residue remains in {source.name}: {summary}")
    text = normalize_layout_projection(text)
    footer = (
        "\n\n---\n\n"
        "Corpus source and companion formats:  \n"
        f"[{REPOSITORY_URL}]({REPOSITORY_URL})  \n"
        f"License: [{PAPER_LICENSE}](https://creativecommons.org/licenses/by-nd/4.0/)\n"
    )
    if doi:
        normalized_doi = re.sub(r"^https?://doi\.org/", "", doi, flags=re.I).strip()
        if not re.fullmatch(r"10\.5281/zenodo\.\d+", normalized_doi):
            raise ValueError(f"unsupported publication DOI for {source.name}: {doi}")
        footer += f"\n---\n\nDOI: [{normalized_doi}](https://doi.org/{normalized_doi})\n"
    return (text + footer).encode("utf-8")


def pandoc_version() -> str:
    return subprocess.run(["pandoc", "--version"], check=True, capture_output=True, text=True, encoding="utf-8").stdout.splitlines()[0]


def render_one(job: dict[str, Any]) -> dict[str, Any]:
    index = job["index"]
    entry = job["entry"]
    accession = job["accession"]
    audit = job["audit"]
    target = Path(job["target"])
    published = job["published"]
    drafts = job["drafts"]
    pversion = job["pandoc_version"]
    source = Path(entry["successor_path"])
    paper_dir = target / "papers" / "current" / f"{accession['accession_id']}-{short_slug(entry['title'])}"
    paper_dir.mkdir(parents=True, exist_ok=True)
    metadata = metadata_for(entry, audit, published, drafts, accession)
    md_bytes = local_markdown(source, metadata.get("doi"))

    with tempfile.TemporaryDirectory(prefix=f"ableman-{index:03d}-") as tmp_name:
        tmp = Path(tmp_name)
        md_tmp = tmp / "paper.md"
        pdf_tmp = tmp / "paper.pdf"
        html_tmp = tmp / "paper.html"
        md_tmp.write_bytes(md_bytes)
        commands = [["pandoc", str(md_tmp), "-o", str(pdf_tmp)], ["pandoc", str(md_tmp), "-o", str(html_tmp)]]
        errors: list[str] = []
        for command in commands:
            result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
            if result.returncode:
                errors.append(f"{' '.join(command[:1] + ['INPUT', '-o', 'OUTPUT'])}: {result.stderr.strip()}")
        if errors:
            return {"ok": False, "index": index, "work_id": entry["work_id"], "title": entry["title"], "errors": errors}

        md_hash = sha256_bytes(md_bytes)
        pdf_hash = sha256_file(pdf_tmp)
        html_hash = sha256_file(html_tmp)
        metadata_subject = {key: value for key, value in metadata.items() if key not in {"formats", "release_root"}}
        metadata_hash = sha256_bytes(canonical_bytes(metadata_subject))
        recipe = {
            "pandoc_version": pversion,
            "pdf_command": "pandoc INPUT.md -o OUTPUT.pdf",
            "html_command": "pandoc INPUT.md -o OUTPUT.html",
            "note": "No custom template, TeX option, or styling parameter was supplied.",
        }
        recipe_hash = sha256_bytes(canonical_bytes(recipe))
        root_subject = {
            "accession_id": accession["accession_id"],
            "work_id": entry["work_id"],
            "edition": "CURRENT_GITHUB_CORPUS_EDITION",
            "markdown_sha256": md_hash,
            "pdf_sha256": pdf_hash,
            "html_sha256": html_hash,
            "metadata_sha256": metadata_hash,
            "render_recipe_sha256": recipe_hash,
        }
        release_root = sha256_bytes(canonical_bytes(root_subject))
        basename = f"{safe_component(entry['title'])} -- {release_root[:12]}"
        md_out = paper_dir / f"{basename}.md"
        pdf_out = paper_dir / f"{basename}.pdf"
        html_out = paper_dir / f"{basename}.html"
        receipt_out = paper_dir / f"{basename}.receipt.json"
        metadata_out = paper_dir / "metadata.json"
        md_out.write_bytes(md_bytes)
        shutil.copyfile(pdf_tmp, pdf_out)
        shutil.copyfile(html_tmp, html_out)

        formats = {
            "markdown": {"path": md_out.relative_to(target).as_posix(), "sha256": md_hash, "bytes": md_out.stat().st_size},
            "pdf": {"path": pdf_out.relative_to(target).as_posix(), "sha256": pdf_hash, "bytes": pdf_out.stat().st_size},
            "html": {"path": html_out.relative_to(target).as_posix(), "sha256": html_hash, "bytes": html_out.stat().st_size},
        }
        receipt = {
            "schema": RECEIPT_SCHEMA,
            "accession_id": accession["accession_id"],
            "accession_number": accession["accession_number"],
            "work_id": entry["work_id"],
            "title": entry["title"],
            "release_root_sha256": release_root,
            "root_subject": root_subject,
            "formats": formats,
            "metadata_sha256": metadata_hash,
            "render_recipe": recipe,
            "predecessor": {
                "logical_path": f"corpus-199-heads/papers/{Path(entry['predecessor_path']).name}",
                "sha256": entry.get("predecessor_sha256"),
            },
            "source_successor": {
                "logical_path": f"corpus-199-reference-successors-v0.1/papers/{Path(entry['successor_path']).name}",
                "sha256": entry.get("successor_sha256"),
            },
            "projection_changes": [
                "Copied the governed reference-successor into a local projection without replacing it.",
                "Normalized legacy author-name forms to Adam Ableman in the local projection.",
                "Replaced workstation-specific inline source paths with logical source-material locators.",
                "Wrapped long predecessor filenames and other machine locators into reconstructable display segments.",
                "Reflowed long display formulas into aligned math without changing their ordered terms.",
                "Rendered width-unsafe Markdown tables as labeled record lists without changing their field values.",
                "Reflowed width-unsafe presentation-only text fences while retaining the governed source head as the exact copy surface.",
                "Added explicit display breaks to long hashes, identifiers, and logical paths; their uninterrupted source values remain in the governed source head and detached custody data.",
                "Kept long external URL targets while shortening only their visible link labels.",
                "Removed the review-only reference-pass custody appendix from the public paper body; exact predecessor and successor custody remains in this detached receipt.",
                "Updated obsolete working-paper and review-head bibliography labels to Ableman Corpus edition labels while retaining separate unpublished evidence and instruments as unpublished.",
                "Removed author-facing review-loop instructions and obsolete prepublication status language while retaining substantive integrations, evidence limits, open research questions, and AI/source-custody distinctions.",
                "Added the repository locator and paper license at the end of the local copy.",
                "Added the verified Zenodo version DOI as final end matter when a publication record is associated.",
                "Rendered companion formats with plain Pandoc output-mode commands.",
            ],
            "standing": "PUBLIC_GITHUB_CORPUS_EDITION",
            "non_effects": ["AUTHOR_STANDING", "CANONICAL_SOURCE_REPLACEMENT", "PROVIDER_EFFECT", "IDENTITY_MERGE"],
        }
        metadata["release_root_sha256"] = release_root
        metadata["formats"] = formats
        metadata["receipt_path"] = receipt_out.relative_to(target).as_posix()
        metadata["metadata_path"] = metadata_out.relative_to(target).as_posix()
        write_json(receipt_out, receipt)
        write_json(metadata_out, metadata)
        return {"ok": True, "index": index, "record": metadata}


def build_contract(target: Path, questions_path: Path) -> None:
    questions = json.loads(questions_path.read_text(encoding="utf-8"))["questions"]
    registry_path = target / "atlas" / "semantic-admission" / "corpus_semantic_contracts.v0.6.jsonl"
    term_index_path = target / "atlas" / "semantic-admission" / "semantic_term_index.v0.6.json"
    bindings = []
    for question in questions:
        bindings.append({
            "binding_id": question["question_id"],
            "concept_ids": [item["concept_id"] for item in question.get("concepts", [])],
            "answer_units": question["answer_units"],
            "coordinate": question["coordinate"],
            "identity_effect": "NONE",
        })
    contract = {
        "schema": "amcs.semantic-use-contract.v0.6",
        "projection": "Ableman Corpus GitHub public edition",
        "projectionRule": "Uses corpus identities for public navigation, current-edition custody, and detached representation receipts. It does not merge identities, alter canonical sources, contact providers, or create author standing.",
        "standing": "PUBLIC_GITHUB_CORPUS_PROJECTION",
        "non_effects": ["author_standing", "identity_merge", "source_mutation", "provider_effect", "external_research"],
        "registry": {
            "path": "atlas/semantic-admission/corpus_semantic_contracts.v0.6.jsonl",
            "records": sum(1 for line in registry_path.read_text(encoding="utf-8").splitlines() if line.strip()),
            "sha256": sha256_file(registry_path),
            "term_index_path": "atlas/semantic-admission/semantic_term_index.v0.6.json",
            "term_index_sha256": sha256_file(term_index_path),
        },
        "semantic_bindings": bindings,
        "uses": {
            "GMB": {"concept_id": "SEMANTIC-KERNEL.GMB", "coordinate_axis": "semantic_substrate", "function": "versioned_contestable_source_bound_meaning_base"},
            "IC": {"concept_id": "SEMANTIC-KERNEL.REALIZATION.IC", "coordinate_axis": "realization_stage", "function": "selected_context_specific_configuration_slice_before_realization"},
            "IR": {"concept_id": "SEMANTIC-KERNEL.REALIZATION.IR", "coordinate_axis": "realization_stage", "function": "actual_realized_instance_subject_to_evidence"},
            "PI": {"concept_id": "SEMANTIC-KERNEL.PI", "coordinate_axis": "coordinate", "function": "select_a_semantic_object_representation_retrieval_depth_lens_disambiguation_and_governance_context"},
            "RPZ": {
                "concept_id": "ATLAS.STRUCTURE.DA0BB30C50B30175", "coordinate_axis": "r", "function": "representation_resolution_of_one_semantic_object",
                "levels": {"RPZ0": "collision-aware reference token or coordinate; not a definition", "RPZ1": "canonical candidate name, bound term, slug, acronym, renderings, and aliases", "RPZ2": "intension or one-hop essence sufficient to distinguish the object in context", "RPZ3": "thick definition and relational manifold with typed adjacency, qualifications, standing, and provenance", "RPZ4+": "generated traversal or exposition compiled on demand and labeled as synthesis"},
            },
            "SZ": {
                "concept_id": "SEMANTIC-KERNEL.SZ", "coordinate_axis": "z", "function": "retrieval_depth_across_semantic_and_source_material",
                "levels": {"SZ0": "minimal machine or session boot", "SZ1": "compact human orientation", "SZ2": "semantic indexes, catalogs, and universal GSM", "SZ3": "full papers, codices, specifications, evidence, and revision dossiers"},
            },
            "ESA": {"concept_id": "ATLAS.CORPUS.25E73C9953042472", "coordinate_axis": "G", "function": "reviewed_provisional_epistemic_state_navigation_only"},
        },
        "source_bound_labels": {
            "condex": "User-preferred public label; no semantic identity inferred by this projection.",
            "Distributed Knowledge Network": "User-preferred public label; no semantic identity inferred by this projection.",
            "Constitutional Computing": "Authorial field label; no separate registry identity inferred by this projection.",
        },
    }
    write_json(target / "SEMANTIC_USE_CONTRACT.json", contract)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workbench", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--skill-root", type=Path, required=True)
    parser.add_argument("--accession-ledger", type=Path)
    parser.add_argument("--workers", type=int, default=max(1, min(4, os.cpu_count() or 1)))
    args = parser.parse_args()
    workbench = args.workbench.resolve()
    target = args.target.resolve()
    skill_root = args.skill_root.resolve()
    source_root = workbench / "data" / "corpus-199-reference-successors-v0.1"
    complete_ledger = json.loads((source_root / "REFERENCE-PASS-LEDGER.json").read_text(encoding="utf-8"))
    ledger = [
        entry
        for entry in complete_ledger
        if not entry["title"].startswith(EXCLUDED_TITLE_PREFIXES)
        and entry["work_id"] not in WITHHELD_PUBLIC_WORK_IDS
    ]
    audit_list = json.loads((workbench / "evidence" / "corpus-reference-pass-v0.1" / "SOURCE-REFERENCE-AUDIT.json").read_text(encoding="utf-8"))
    audit = {item["work_id"]: item for item in audit_list}
    published, drafts = query_metadata(workbench / "state" / "acpw.sqlite")
    accession_path = (args.accession_ledger or (target / "metadata" / "accession-ledger.json")).resolve()
    accession_ledger = json.loads(accession_path.read_text(encoding="utf-8"))
    accessions = {item["work_id"]: item for item in accession_ledger["accessions"]}
    expected_ids = {entry["work_id"] for entry in ledger}
    missing = sorted(expected_ids - set(accessions))
    unexpected = sorted(set(accessions) - expected_ids - set(WITHHELD_PUBLIC_WORK_IDS))
    if missing or unexpected:
        raise ValueError(f"accession ledger mismatch; missing={missing}, unexpected={unexpected}")
    pversion = pandoc_version()

    current = target / "papers" / "current"
    if current.exists():
        shutil.rmtree(current)
    current.mkdir(parents=True)
    metadata_items = target / "metadata" / "papers"
    if metadata_items.exists():
        shutil.rmtree(metadata_items)
    metadata_items.mkdir(parents=True)

    ordered_ledger = sorted(ledger, key=lambda entry: accessions[entry["work_id"]]["accession_number"])
    jobs = [{"index": accessions[entry["work_id"]]["accession_number"], "entry": entry, "accession": accessions[entry["work_id"]], "audit": audit[entry["work_id"]], "target": str(target), "published": published, "drafts": drafts, "pandoc_version": pversion} for entry in ordered_ledger]
    records: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(render_one, job) for job in jobs]
        for complete, future in enumerate(concurrent.futures.as_completed(futures), 1):
            result = future.result()
            if result["ok"]:
                records.append(result["record"])
            else:
                failures.append(result)
            print(f"[{complete:03d}/{len(jobs):03d}] {'OK' if result['ok'] else 'FAIL'} {result.get('title') or result['record']['title']}", flush=True)

    records.sort(key=lambda item: item["accession_number"])
    for record in records:
        write_json(metadata_items / f"{record['work_id']}.json", record)
    corpus = {
        "schema": "ableman.corpus-metadata.v0.2",
        "author": AUTHOR,
        "repository": REPOSITORY_URL,
        "edition_policy": "ONE_CURRENT_INTEGRATED_EDITION_PER_WORK",
        "accession_policy": accession_ledger["policy"],
        "accession_ledger": {
            "path": "metadata/accession-ledger.json",
            "schema": accession_ledger["schema"],
            "root_sha256": accession_ledger["ledger_root_sha256"],
        },
        "standing": "PUBLIC_GITHUB_CORPUS_EDITION",
        "non_effects": ["AUTHOR_STANDING", "PROVIDER_EFFECT", "CANONICAL_SOURCE_REPLACEMENT", "IDENTITY_MERGE"],
        "excluded_by_author_ruling": [
            {
                "title": "Project57: Meta-Binding Testing Protocol",
                "reason": "AUTHOR_NOT_READY_RULING",
                "accession_id": None,
            },
            *[
                {
                    "title": item["title"],
                    "reason": item["reason"],
                    "accession_id": item["accession_id"],
                }
                for item in WITHHELD_PUBLIC_WORK_IDS.values()
            ],
        ],
        "counts": {
            "works_expected": len(ledger),
            "works_built": len(records),
            "published_version_associations": sum(1 for item in records if item["publication_association"] != "NO_VERIFIED_CURRENT_VERSION_ASSOCIATION"),
            "verified_provider_metadata_associations": sum(1 for item in records if item["publication_association"] == "VERIFIED_PROVIDER_RECORD"),
            "associated_but_metadata_unresolved": sum(1 for item in records if item["publication_association"] == "PUBLISHED_VERSION_ASSOCIATED_METADATA_UNRESOLVED"),
            "without_verified_current_version_association": sum(1 for item in records if item["publication_association"] == "NO_VERIFIED_CURRENT_VERSION_ASSOCIATION"),
            "reserved_accessions_withheld_from_public_projection": len(WITHHELD_PUBLIC_WORK_IDS),
        },
        "papers": records,
    }
    write_json(target / "metadata" / "corpus.json", corpus)
    shutil.copyfile(source_root / "EXTERNAL-REFERENCE-LIBRARY.json", target / "metadata" / "EXTERNAL-REFERENCE-LIBRARY.json")
    admission = target / "atlas" / "semantic-admission"
    admission.mkdir(parents=True, exist_ok=True)
    copy_public_jsonl(workbench / "semantic-admission" / "corpus_semantic_contracts.v0.6.jsonl", admission / "corpus_semantic_contracts.v0.6.jsonl")
    copy_public_json(workbench / "semantic-admission" / "semantic_term_index.v0.6.json", admission / "semantic_term_index.v0.6.json")
    questions_path = skill_root / "data" / "question_semantic_bindings.v0.6.json"
    copy_public_json(questions_path, target / "atlas" / "question_semantic_bindings.v0.6.json")
    build_contract(target, questions_path)
    manifest_entries = []
    for path in sorted(target.rglob("*")):
        if (
            path.is_file()
            and ".candidate" not in path.parts
            and ".git" not in path.parts
            and "__pycache__" not in path.parts
            and "tmp" not in path.relative_to(target).parts
            and path.suffix != ".pyc"
            and path.name != "MANIFEST.json"
        ):
            manifest_entries.append({"path": path.relative_to(target).as_posix(), "sha256": sha256_file(path), "bytes": path.stat().st_size})
    manifest = {"schema": BUILD_SCHEMA, "files": manifest_entries}
    manifest["content_root_sha256"] = sha256_bytes(canonical_bytes(manifest_entries))
    write_json(target / "MANIFEST.json", manifest)
    build_report = {
        "schema": BUILD_SCHEMA,
        "pandoc_version": pversion,
        "expected": len(ledger),
        "built": len(records),
        "failed": len(failures),
        "failures": failures,
        "manifest_root_sha256": manifest["content_root_sha256"],
        "standing": "GITHUB_RELEASE_CANDIDATE",
    }
    write_json(target / ".candidate" / "BUILD-REPORT.json", build_report)
    print(json.dumps(build_report, indent=2))
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
