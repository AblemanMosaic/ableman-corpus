#!/usr/bin/env python3
"""Remove internal review-loop residue from a public paper projection.

The governed source heads remain unchanged.  This module operates only on a
reader-facing projection after author rulings have been recorded.  It keeps
substantive review additions, evidence limits, open research questions, and
AI/source-custody disclosure while removing instructions addressed to the
author and obsolete prepublication status language.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class ResidueFinding:
    code: str
    line: int
    excerpt: str

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


BLOCKING_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("DECISION_HEADING", re.compile(r"(?im)^#{1,6}\s+.*(?:author decisions?|publication decisions?).*$")),
    ("AUTHOR_INSTRUCTION", re.compile(r"(?i)\b(?:before publication,?\s+)?the author should decide\b")),
    ("DECISION_SUMMARY", re.compile(r"(?i)\badds? (?:four|\d+) author decisions?\b")),
    ("AUTHOR_REVIEW_CANDIDATE", re.compile(r"(?i)\bauthor-review candidate\b")),
    ("REVIEW_PASS_HEADING", re.compile(r"(?im)^#{1,6}\s+P[2-5]\b.*$")),
    ("DEFERRED_RENDER", re.compile(r"(?i)\brendering is intentionally deferred\b")),
    ("NO_PUBLICATION_EFFECT", re.compile(r"(?i)\bno publication or rendering effect follows\b")),
    ("NOT_PUBLICATION_STATUS", re.compile(r"(?i)\bready for author substantive review,? not publication\b")),
    ("AUTHOR_REVIEW_SOURCE", re.compile(r"(?i)\b(?:unpublished\s+)?author-review source\b")),
    ("AUTHOR_REVIEW_SUCCESSOR", re.compile(r"(?i)\bcandidate for author review\b")),
    ("PREPUBLICATION_INSTRUCTION", re.compile(r"(?i)\bbefore (?:external )?publication\b")),
    ("PENDING_AUTHOR_REVIEW", re.compile(r"(?i)\bpending author review\b")),
)


def scan_publication_residue(text: str) -> list[ResidueFinding]:
    findings: list[ResidueFinding] = []
    for code, pattern in BLOCKING_PATTERNS:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            excerpt = re.sub(r"\s+", " ", match.group(0)).strip()[:240]
            findings.append(ResidueFinding(code, line, excerpt))
    return sorted(findings, key=lambda item: (item.line, item.code))


def _heading(line: str) -> tuple[int, str] | None:
    match = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
    if not match:
        return None
    return len(match.group(1)), match.group(2)


def _without_number(title: str) -> str:
    return re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", title).strip()


def _decision_only_heading(title: str) -> bool:
    bare = _without_number(title).lower()
    return (
        bare.startswith("author decisions")
        or bare.startswith("publication decisions")
        or bare.startswith("publication decision surface")
        or bare == "author decisions retained"
    )


def _rename_heading(title: str) -> str:
    replacements = (
        (r"Publication Standing and Author Decisions", "Publication Standing and Evidence Limits"),
        (r"Research Agenda and Author Decisions", "Research Agenda and Open Questions"),
        (r"Research and Author Decisions", "Research Agenda and Open Questions"),
        (r"GMB, Universal GSM, Counterevidence, and Author Decisions", "GMB, Universal GSM, and Counterevidence"),
        (r"Corpus Integration, Counterevidence, and Publication Decisions", "Corpus Integration and Counterevidence"),
        (r"Counterevidence, Attack Surface, and Publication Decisions", "Counterevidence and Attack Surface"),
    )
    for old, new in replacements:
        title = re.sub(old, new, title, flags=re.I)
    # Review-lens prefixes are useful in the ledger, not in the paper title.
    title = re.sub(r"^P[2-4]\s+[^:]+:\s*", "", title, flags=re.I)
    title = re.sub(r"^P5\s+Adversarial and Publication-Readiness Review:\s*", "", title, flags=re.I)
    return title


def _drop_decision_sections(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    output: list[str] = []
    skip_level: int | None = None
    removed = 0
    for line in lines:
        parsed = _heading(line)
        if skip_level is not None:
            if parsed and parsed[0] <= skip_level:
                skip_level = None
            else:
                removed += 1
                continue
        if parsed:
            level, title = parsed
            if _decision_only_heading(title):
                skip_level = level
                removed += 1
                continue
            line = "#" * level + " " + _rename_heading(title)
        output.append(line)
    return "\n".join(output), removed


def _drop_instruction_tail(text: str) -> tuple[str, int]:
    """Drop a decision instruction and its list through the next heading.

    Combined sections retain their evidence-status material before the trigger;
    the author-facing decision surface and its non-effect disclaimer are removed.
    """
    trigger = re.compile(
        r"(?i)^(?:this .*?ready for author substantive review,? not publication\.\s*)?"
        r"(?:before publication,?\s+)?the author should decide(?: whether to)?(?::|\b)"
    )
    lines = text.splitlines()
    output: list[str] = []
    skipping = False
    removed = 0
    for line in lines:
        if not skipping and trigger.search(line.strip()):
            skipping = True
            removed += 1
            continue
        if skipping:
            if _heading(line):
                skipping = False
                output.append(line)
            else:
                removed += 1
            continue
        output.append(line)
    return "\n".join(output), removed


def remediate_publication_projection(text: str) -> tuple[str, dict[str, int]]:
    """Return a reader-facing projection and a deterministic change summary."""
    original = text
    text, decision_section_lines = _drop_decision_sections(text)
    text, instruction_lines = _drop_instruction_tail(text)

    substitutions: tuple[tuple[str, str, int], ...] = (
        (r"(?i)\bAI-prepared author-review candidate\b", "AI-assisted integrated edition", 0),
        (r"(?i)\bauthor-review candidate\b", "AI-assisted integrated edition", 0),
        (r"(?i)\bAI-prepared successor revision candidate for author review\b", "AI-assisted integrated successor edition", 0),
        (r"(?i)\b(?:unpublished\s+)?author-review source\b", "separately custodied reviewed source", 0),
        (r"(?i)\bseparate AI-prepared revision candidate\b", "separate AI-assisted integrated edition", 0),
        (r"(?i)\bAI-prepared editorial or synthetic proposals pending author review\b",
         "AI-assisted editorial or synthetic contributions explicitly distinguished from the original author material", 0),
        (r"(?i)\bpending author review\b", "explicitly distinguished from the original author material", 0),
        (r"(?i)\badds four author decisions:", "establishes four editorial commitments:", 0),
        (r"(?i)\badds (\d+) author decisions:", r"establishes \1 editorial commitments:", 0),
        (r"(?i)\bauthor decisions are AI editorial or synthetic candidates until adopted\.",
         "editorial alternatives are AI-assisted contributions explicitly distinguished from the original author material.", 0),
        (r"(?i)\bauthor decisions are AI editorial or synthetic additions until adopted\.",
         "editorial alternatives are AI-assisted contributions explicitly distinguished from the original author material.", 0),
        (r"(?i)\bauthor decisions\b", "open editorial questions", 0),
        (r"(?i)\bBefore external publication, an authorized review should\b", "A future evidence-qualified edition should", 0),
        (r"(?i)\bBefore publication as reproducible evidence,", "Before this can be treated as reproducible evidence in a future edition,", 0),
        (r"(?i)\bBefore publication-ready implementation claims,", "Before making implementation-ready claims,", 0),
        (r"(?i)\bbefore publication was not\b", "for an evidence-qualified revision was not", 0),
        (r"(?i)\bBefore publication,", "For a future evidence-qualified revision,", 0),
        (r"(?i)\bbefore external publication\b", "for a future evidence-qualified revision", 0),
        (r"(?i)\bbefore publication\b", "for a future evidence-qualified revision", 0),
        (r"(?i)\bPublication additionally requires\b", "Further evidentiary strengthening requires", 0),
        (r"(?i)\bPublication requires\b", "Further evidentiary strengthening requires", 0),
        (r"(?i)\bpublication readiness\b", "evidence readiness", 0),
        (r"(?i)\bPublication-Readiness\b", "Evidence-Readiness", 0),
        (r"(?i)\bpublication standing not granted here\b", "publication does not alter separate canonical standing", 0),
        (r"(?i)\bDOI and publication standing not granted\b", "DOI and publication identity are recorded separately", 0),
        (r"(?i)\bnot publication-ready citations in this candidate\b", "unverified research leads in this edition", 0),
    )
    substitution_count = 0
    for pattern, replacement, flags in substitutions:
        text, count = re.subn(pattern, replacement, text, flags=flags)
        substitution_count += count

    # Obsolete local rendering instructions must never enter a public paper.
    text, deferred_count = re.subn(
        r"(?ms)^Rendering is intentionally deferred.*?^No publication or rendering effect follows.*?(?=^#{1,6}\s|\Z)",
        "",
        text,
        flags=re.I,
    )
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text, {
        "decision_section_lines_removed": decision_section_lines,
        "instruction_tail_lines_removed": instruction_lines,
        "substitutions": substitution_count,
        "deferred_render_blocks_removed": deferred_count,
        "changed": int(text != original),
    }

