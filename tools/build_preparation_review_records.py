#!/usr/bin/env python3
"""Emit information-only P/PPI records for the correction preparation pass."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ucm-root", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.ucm_root.resolve() / "src"))
    from uclop.canonical import root  # type: ignore
    from ucm.research_reviews import (  # type: ignore
        build_finding_adjudication,
        build_review_finding,
        build_review_lens_pack,
        build_saturation_assessment,
        build_successor_ledger,
    )

    source = args.source.resolve()
    candidate = args.candidate.resolve()
    output = args.output.resolve()
    source_root = digest(source / "MANIFEST.json")
    successor_root = digest(candidate / "MANIFEST.json")
    evidence_dir = candidate / "evidence" / "publication-residue-remediation-2026-11-05"
    remediation_root = digest(evidence_dir / "REMEDIATION-REPORT.json")
    regression_root = digest(evidence_dir / "PUBLICATION-RESIDUE-VERIFY.json")
    plan_root = digest(evidence_dir / "ZENODO-REPLACEMENT-PLAN.json")

    ruling = {
        "schema": "ableman.author-ruling.local-preparation.v0.1",
        "ruling": "Proceed with preparatory work and pause for authorization before the publish leg.",
        "scope": "Local correction candidate, rendering, verification, and effect-closed publication planning.",
        "non_effects": ["GITHUB_PUSH", "ZENODO_MUTATION", "PUBLICATION"],
        "date": "2026-11-05",
    }
    write_json(output / "AUTHOR-RULING.json", ruling)
    ruling_root = root(ruling)
    lens_pack = build_review_lens_pack(
        lens_pack_id="ABLEMAN.PUBLICATION.RESIDUE.PREP.v0.1",
        subject_class="ABLEMAN_CORPUS_PUBLIC_PROJECTION",
        lenses=[
            {
                "lens_id": "CUSTODY_AUTHORSHIP",
                "title": "Custody and authorship preservation",
                "objective": "Preserve exact source custody and distinguish author material from AI-assisted editorial integration.",
                "review_class": "CUSTODY",
                "required_context_roles": ["CORPUS_CONTEXT", "SUBJECT"],
                "deterministic_check_ids": ["SOURCE_SUCCESSOR_RECEIPT_PRESENT"],
                "review_questions": ["Does the public projection retain source custody without converting AI synthesis into author-original material?"],
                "exclusions": ["No author standing is created by this check."],
            },
            {
                "lens_id": "PROVIDER_EFFECT_GATE",
                "title": "Provider effect gate",
                "objective": "Bind every external mutation to a later explicit authorization and exact replacement plan.",
                "review_class": "PROCESS",
                "required_context_roles": ["CORPUS_CONTEXT", "SUBJECT"],
                "deterministic_check_ids": ["PROVIDER_EFFECT_NONE", "REPLACEMENT_PLAN_COMPLETE"],
                "review_questions": ["Are Zenodo and GitHub effects closed during preparation?"],
                "exclusions": ["No DOI reservation, upload, publication, deletion, or Git push is authorized."],
            },
            {
                "lens_id": "PUBLICATION_RESIDUE",
                "title": "Reader-facing publication residue",
                "objective": "Remove author-facing review instructions and stale prepublication labels without removing substantive research content.",
                "review_class": "EDITORIAL",
                "required_context_roles": ["CORPUS_CONTEXT", "SUBJECT"],
                "deterministic_check_ids": ["MARKDOWN_RESIDUE_ZERO", "PDF_RESIDUE_ZERO"],
                "review_questions": ["Does any public paper still instruct the author to decide publication matters or describe itself as awaiting publication?"],
                "exclusions": ["Open research questions and evidence limitations remain visible."],
            },
            {
                "lens_id": "RENDERING_PARITY",
                "title": "Markdown, PDF, and HTML parity",
                "objective": "Require the corrected meaning surface to survive plain Pandoc rendering in every companion representation.",
                "review_class": "FORMATTING",
                "required_context_roles": ["SUBJECT"],
                "deterministic_check_ids": ["PLAIN_PANDOC_ONLY", "REPRESENTATION_HASHES_BOUND"],
                "review_questions": ["Do the rendered artifacts remain readable and exact-hash bound to the corrected Markdown?"],
                "exclusions": ["This check does not establish scholarly truth or novelty."],
            },
        ],
        limitations=sorted([
            "The review is local and does not replace external peer review.",
            "The review does not authorize publication or provider mutation.",
            "The review establishes structural cleanliness only for the declared residue patterns and sampled visual pages.",
        ]),
    )
    write_json(output / "LENS-PACK.json", lens_pack)
    finding = build_review_finding(
        finding_id="ABLEMAN.PUBLICATION.RESIDUE.001",
        review_id="ABLEMAN.PUBLICATION.PREP.2026-11-05",
        lens_pack_root=lens_pack["lens_pack_root"],
        lens_id="PUBLICATION_RESIDUE",
        subject_root=source_root,
        source_anchor={
            "path": "papers/current",
            "section": "Corpus-wide reader-facing public projection",
            "location_start": 0,
            "location_end": 199,
            "excerpt_sha256": source_root,
        },
        severity="HIGH",
        change_class="EDITORIAL",
        summary="Published paper projections retained author-facing decision sections and stale prepublication workflow language.",
        rationale="The residue misstates publication status, exposes internal review machinery to readers, and can be corrected without deleting substantive integrations, open questions, evidence limits, or custody distinctions.",
        evidence_roots=sorted([remediation_root, regression_root]),
        counterevidence_roots=[],
        affected_concept_ids=["CORPUS.PUBLICATION.CUSTODY"],
        affected_artifact_ids=["ABLEMAN.CORPUS.PUBLIC.PROJECTION"],
        proposed_action="Use the prepared 198-paper projection and its 108-record DOI replacement gate; keep AFS withheld and keep all provider effects closed until explicit authorization.",
        reviewer_identity_root=hashlib.sha256(b"Codex local editorial preparation 2026-11-05").hexdigest(),
        limitations=sorted([
            "No external scholarly review was performed.",
            "Provider deletion policy may prevent a literal one-record-only history.",
        ]),
    )
    write_json(output / "FINDING.json", finding)
    adjudication = build_finding_adjudication(
        finding_root=finding["finding_root"],
        disposition="ACCEPTED",
        reason_codes=["AUTHOR_PREPARATION_AUTHORIZED", "PUBLIC_STATUS_INCONSISTENCY_CONFIRMED"],
        author_decision_root=ruling_root,
        applied_change_root=remediation_root,
        superseded_by_finding_root=None,
        remaining_obligation_ids=["EXPLICIT_PUBLISH_LEG_AUTHORIZATION", "ZENODO_SUPPORT_SEMANTIC_DEBT"],
        regression_review_required=True,
        notes="Accepted for local preparation only. Publication, deletion, DOI reservation, and GitHub push remain closed.",
    )
    write_json(output / "ADJUDICATION.json", adjudication)
    ledger = build_successor_ledger(
        ledger_id="ABLEMAN.PUBLICATION.PREP.LEDGER.2026-11-05",
        logical_work_id="ABLEMAN.CORPUS.PUBLIC.PROJECTION",
        source_root=source_root,
        successor_status="CREATED",
        successor_root=successor_root,
        lens_pack_root=lens_pack["lens_pack_root"],
        accepted_finding_roots=[finding["finding_root"]],
        adjudication_roots=[adjudication["adjudication_root"]],
        accepted_change_roots=[remediation_root],
        semantic_change_roots=[],
        editorial_change_roots=[remediation_root],
        added_claim_roots=[],
        removed_claim_roots=[],
        cross_reference_delta_roots=[],
        regression_evidence_roots=[regression_root],
        unresolved_finding_roots=[],
        predecessor_ledger_root=None,
        producer_operation_root=plan_root,
        status="SUCCESSOR_CREATED",
    )
    write_json(output / "SUCCESSOR-LEDGER.json", ledger)
    saturation = build_saturation_assessment(
        assessment_id="ABLEMAN.PUBLICATION.PREP.SATURATION.2026-11-05",
        subject_root=successor_root,
        lens_pack_root=lens_pack["lens_pack_root"],
        pass_roots=[ledger["successor_ledger_root"]],
        new_substantive_findings_by_pass=[1],
        accepted_substantive_changes_by_pass=[1],
        severity_weighted_yield_by_pass=[3],
        repeated_finding_count_by_pass=[0],
        regression_count_by_pass=[0],
        coverage_delta_basis_points={
            "corpus_linkage": 0,
            "counterevidence": 0,
            "evidence": 0,
            "pedagogical_accessibility": 10000,
        },
        unresolved_high_severity_roots=[],
        thresholds={
            "minimum_passes": 2,
            "window_size": 2,
            "maximum_new_findings": 0,
            "maximum_accepted_changes": 0,
            "maximum_weighted_yield": 0,
            "maximum_regressions": 0,
        },
        nonclaims=sorted([
            "This assessment does not establish publication readiness.",
            "This assessment does not establish scholarly truth, novelty, or peer review.",
        ]),
    )
    write_json(output / "SATURATION.json", saturation)
    print(json.dumps({
        "lens_pack_root": lens_pack["lens_pack_root"],
        "finding_root": finding["finding_root"],
        "successor_ledger_root": ledger["successor_ledger_root"],
        "saturation_result": saturation["result"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
