# Adversarial Alternation Under Human Governance

## A Case Study in AI-Built, AI-Audited Verification Infrastructure

### Those observations do not establish that alternation outperforms one careful agent.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

This paper reports a two-day case study in which two AI sessions alternated between builder and auditor roles while one human Governor retained scope, disposition, and ratification authority. The subject was a small verification and evidence-recovery system whose claims could be quarantined when a dependency failed and restored only after re-derivation and human ratification.

The case suggests a practical hardening loop: freeze the candidate, replay it cold, attack beyond packaged tests, reproduce every accepted finding before repair, convert each counterexample into a permanent regression, and prevent artifacts from conferring standing on themselves. The source reports that later builder errors were caught by earlier auditor tests and that the last ledger round had no findings under its probe set.

Those observations do not establish that alternation outperforms one careful agent. The sessions were role-separated but not shown to be epistemically independent; they were probably from the same model family. There was no baseline, the program was small, the author participated, probe sets changed, and findings were counted in inconsistent units. The frozen archives and full reports were not rerun in this review. The defensible contribution is therefore an evidence-bounded method specification and a set of hypotheses for controlled evaluation, not a causal effect claim.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/adversarial-`

`alternation-human-governance/integration-`  
`custody-manifest.v0.1.json`,  
SHA-256  
`505545448B44404FFAFB834396A2AFEDCED2A1E2FE4AD39286D47E14937AD242`. The source remains unchanged.

The case record, SIER architecture, round descriptions, reported defect classes, evidence tiers, limitations, and future-work proposals are author material. Formalization, corpus integration, the universal GSM decomposition, the realization funnel, expanded countertests, and editorial alternatives are AI-assisted contributions explicitly distinguished from the original author material.

No external research was conducted. The implementation archives, audit reports, full artifact digests, permanent tests, and ratification conversation records described by the manuscript were not present in this review package. This paper therefore says **source-reported** where direct replay or artifact authentication would be required. A SHA-256 prefix identifies a possible artifact; it does not authenticate its origin, completeness, or standing.

## 1. The Problem

A proof can be valid for the wrong statement. A receipt can be well-formed but refer to the wrong subject. A test can pass because it never reaches the intended gate. A later defect in a tool can invalidate claims that depended on earlier results. These are not merely implementation mistakes; they are failures to preserve the relation among a claim, its dependencies, its evidence, and the authority that may grant or restore standing.

The source begins with MUXFIX: Python's treatment of `True == 1` caused an encoder to confuse a constant true bit with propositional variable 1. The proof checker accepted a valid proof, but the encoded formula was not the formula the system claimed to prove. The source reports this as the event that motivated revocable verification claims.

Two questions follow:

1. What must a claim record so a later defect can quarantine every dependent claim without erasing history?
2. Can role-separated AI sessions, alternating under retained human authority, find and permanently encode failures that builder self-testing misses?

The first is an architecture question. The second is an empirical question. This case provides a worked protocol and observations; it does not resolve the comparative question.

## 2. The System Under Study

The source describes three layers:

- **Layer:** UCM Agent Kit  
  **Function:** Checks equivalence and properties for small i32 dataflow programs using packaged proof and search machinery.  
  **Intended protection:** Wrong program claims.

- **Layer:** Material admission gate  
  **Function:** Re-derives a claim from original programs, formula, and proof instead of trusting a receipt alone.  
  **Intended protection:** Receipt-shaped forgery and evidence substitution.

- **Layer:** SIER ledger  
  **Function:** Records claims with typed edges to the exact implementations on which they depend and propagates declared defects.  
  **Intended protection:** Stale evidence surviving a broken dependency.

The ledger states reported by the source are `QUALIFIED`, `SUSPECT`,  
`REQUALIFICATION_PROPOSED`, `REQUALIFIED`, `WITHDRAWN`,  
and `RETROFIT_UNVERIFIED`. A release layer adds closed-world manifests, deterministic archives, replay, and evidence-admission gates.

The scale is intentionally narrow. The source reports a sovereign solver near 75 search nodes per second, a 144-case meaning check, and a 4,681-sequence state-machine court. These figures describe the case system; they do not establish performance, general soundness, or deployment readiness.

## 3. Claims, Dependencies, Defects, and Standing

Let a claim record be:

$$
c=(p,s,D,E,v,l),
$$

where $p$ is the proposition, $s$ the exact subject, $D$ the dependency set, $E$ the evidence set, $v$ the validator and policy versions, and $l$ the current standing label.

Let $D^*(c)$ be the transitive dependency closure of $c$. A declared unresolved defect $d$ affecting dependency $x$ requires quarantine when:

$$
x\in D^*(c).
$$

This rule should be monotone in the conservative direction: newly discovered dependence or defect may lower standing automatically, but absence of a known defect cannot silently prove qualification.

Restoration requires more than settlement of the defect record. In the source architecture:

$$
Restore(c) = Rederive(c,E',v') \land DependenciesClear(c) \land Ratify_h(c),
$$

where $h$ is the authorized human role. A validator can propose restoration; it cannot ratify its own conclusion. Here, **standing** means the program's human-adjudicated status under its declared process. It is not identical to truth, social legitimacy, legal authority, or external certification.

## 4. The Alternation Protocol

The roles were:

- **Governor:** retained scope, custody transfer, disposition, and ratification authority;
- **builder:** produced a candidate and declared its claim ceiling;
- **auditor:** replayed and attacked the frozen candidate from a fresh extraction.

The source reports that the Governor ferried frozen, hashed archives between sessions and that the sessions did not communicate directly. This provides artifact and communication separation. It does not by itself provide model-family diversity, epistemic independence, or independent custody.

The reusable loop is:

```text
Candidate
  -> frozen handoff
  -> cold replay of packaged tests
  -> attacks through real entry points
  -> reproducible findings and gate dispositions
  -> builder reproduction on the shipped subject
  -> repair
  -> permanent regression
  -> human disposition
  -> next frozen candidate
```

Four rules organize the method:

1. **Reproduce before repair.** Confirm an accepted finding on the exact shipped version before changing it.
2. **Retain counterexamples.** Every accepted counterexample becomes a permanent test or explicit unresolved case.
3. **Count refusal as an outcome.** Missing evidence should yield a typed refusal or incomplete verdict rather than false progress.
4. **No self-standing.** Builder, auditor, artifact, receipt, and test count cannot confer their own authority.

These rules are valuable only when their execution is evidenced. A written instruction does not prove that a particular round followed it.

## 5. What the Source Reports

The manuscript reports the following round-level observations. Counts are preserved in their original units because some rows count findings, some classes, some blocking items, and some gates.

- **Lineage:** Ledger  
  **Round:** Pre-SIER  
  **Source-reported result:** 3 findings, including MUXFIX, forged-tier admission, and correlated pair failures.

- **Lineage:** Ledger  
  **Round:** Q2 prototype  
  **Source-reported result:** 3 findings.

- **Lineage:** Ledger  
  **Round:** Q2.1  
  **Source-reported result:** 8 findings.

- **Lineage:** Ledger  
  **Round:** Q2.2  
  **Source-reported result:** 9 findings plus 1 design question.

- **Lineage:** Ledger  
  **Round:** Q2.3  
  **Source-reported result:** 7 findings in 4 classes.

- **Lineage:** Ledger  
  **Round:** Q2.4  
  **Source-reported result:** 3 blocking findings plus 2 gates.

- **Lineage:** Ledger  
  **Round:** Q2.5  
  **Source-reported result:** 2 findings.

- **Lineage:** Ledger  
  **Round:** Q2.6  
  **Source-reported result:** 0 findings under 38 reported adversarial checks.

- **Lineage:** Release  
  **Round:** RC1  
  **Source-reported result:** 4 findings.

- **Lineage:** Release  
  **Round:** RC2  
  **Source-reported result:** 1 class.

- **Lineage:** Release  
  **Round:** RC3-c2  
  **Source-reported result:** 2 minor findings.

- **Lineage:** Release  
  **Round:** RC3 Turn A  
  **Source-reported result:** 0 blocking findings; 2 documented limits.

- **Lineage:** Later work  
  **Round:** Policy overlay  
  **Source-reported result:** 0 blocking findings under 15 reported challenges.

- **Lineage:** Later work  
  **Round:** Six-horizon build  
  **Source-reported result:** 0 blocking findings; 3 horizons remained `PARTIAL`.

- **Lineage:** Later work  
  **Round:** S2 authority pilot  
  **Source-reported result:** 2 medium findings.

These rows should not be summed. They overlap lineages, use different units, change probe sets, and mix defects, classes, gates, design questions, and documented limits. The source abstract, analysis, and conclusion also contain incompatible aggregate numbers and starting counts. This candidate therefore removes the aggregate claim that a particular total number of defects was found or permanently encoded. Further evidentiary strengthening requires a third-party recount from the exact reports under one declared counting policy.

Likewise, movement from a higher number to zero is not yet an effect measurement. A zero means no finding under a particular round's available probes, scope, and budget. It does not mean no defect exists.

## 6. Recurring Failure Families

The manuscript's most useful synthesis is not the count but the recurrence of six families:

- **Failure family:** Reachable mutable state  
  **General form:** A caller, returned object, or nested field can launder a quarantined state.  
  **Required design response:** Deep ownership boundaries, immutable records, post-condition checks, and mutation attacks.

- **Failure family:** Collapsed identity  
  **General form:** Multiple defects, incidents, subjects, or obligations share one key.  
  **Required design response:** Composite identity with explicit namespace, generation, subject, and incident.

- **Failure family:** Presence mistaken for qualification  
  **General form:** A shaped object, signed receipt, or printed `PASS` is accepted without semantic validation.  
  **Required design response:** Bind evidence to subject, method, environment, result, and claim ceiling.

- **Failure family:** Filesystem custody  
  **General form:** Extra files, paths, links, caches, or traversal escape the manifest's intended world.  
  **Required design response:** Closed-world enumeration, containment, link policy, path normalization, and cold extraction.

- **Failure family:** Self-derived checks  
  **General form:** Both sides of a comparison share the same defect or the independent anchor is derived from the implementation.  
  **Required design response:** Separately authored anchors, heterogeneous checks, seeded faults, and negative controls.

- **Failure family:** Missing history  
  **General form:** Rollback, truncation, or late insertion makes invalid state appear current.  
  **Required design response:** Append-only lineage, external heads or high-water marks, policy versioning, and witnessed termination.

A finding should therefore be generalized into a family hypothesis. The permanent test must retain the original counterexample, while the next audit searches for sibling routes rather than assuming the class is closed.

## 7. Permanent Counterexamples as Institutional Memory

The source reports several occasions on which tests written in an earlier audit caught a later builder error. If the underlying records verify those episodes, they illustrate a larger point: an audit creates durable value when its counterexample becomes part of the system's future recognition surface.

For accepted finding $f_i$, let $t_i$ be a regression that fails on the shipped defective subject and passes only when the relevant behavior is repaired. The retained court is:

$$
T_{n+1}=T_n\cup\{t_i\}.
$$

The union is necessary but insufficient. A test may stop reaching its target, become vacuous, share a defect with the implementation, or be bypassed by an outer gate. Each permanent test therefore needs a target declaration, a known-fail fixture or mutation, an observed reachability signal, and a claim ceiling.

This connects the case to Agentic Interface Surfaces: the builder earns recognized progress only through effect-bound evidence, while typed refusals preserve useful state without pretending the effect occurred. It connects to Reasoning by Way of Receipts because each transition should carry a bounded reason artifact rather than narrative assurance alone.

## 8. Independence Is Multidimensional

Calling the auditor **independent** compresses several different properties:

- role separation;
- session separation;
- communication separation;
- frozen artifact separation;
- key or custody separation;
- model-family diversity;
- prompt and training diversity;
- evidence independence;
- disposition independence;
- organizational independence.

The source establishes or reports some of the first four and reserves final disposition to the human Governor. It does not establish the remaining forms. The accurate term for this case is **role-separated adversarial audit**. Epistemic independence remains an experimental variable.

This distinction matters because correlated agents can share omissions, assumptions, favored abstractions, and failure modes. Alternation can deepen a shared blind spot as easily as it can expose a local one.

## 9. Evidence Tiers and Claim Ceilings

The source proposes four useful evidence tiers:

1. hash-pinned material independently reproduced by a second role;
2. reproducible but narrow evidence, or evidence checked by only one party;
3. organizational assertions, conversational authority, or key custody accepted without external verification;
4. unestablished claims.

This hierarchy should be applied at the level of each claim, not assigned once to an entire system. A release can have tier-1 byte reproduction, tier-2 behavior, tier-3 authority, and tier-4 general soundness simultaneously.

In this review, even the source's tier-1 claims remain source-reported because the exact archives and full digests were not available for replay. That does not negate the case record; it limits what this candidate can independently assert.

## 10. Primitives, Invariants, Dimensions, and Adjacencies

### 10.1 Primitives

Candidate primitives are candidate archive, subject root, role, authority grant, claim, dependency edge, defect, incident, obligation, evidence item, validator, policy version, audit probe, finding, disposition, regression, ratification, refusal, and lineage event.

### 10.2 Invariants

The method should preserve:

- exact subject identity across report, replay, finding, repair, and regression;
- non-self-ratification;
- automatic conservative demotion on unresolved dependencies;
- restoration only after re-derivation and authorized ratification;
- one identity per distinct defect incident and obligation;
- immutable history of findings and dispositions;
- closed-world custody for release claims;
- explicit distinction among no finding, no probe, refusal, partial evidence, and pass;
- evidence that a regression reaches its intended target;
- preservation of source and author/AI boundaries.

### 10.3 Dimensions

Relevant experimental dimensions include builder and auditor model families, role permanence versus alternation, information asymmetry, archive size, system complexity, attack budget, probe novelty, regression retention, identity design, authority mechanism, artifact isolation, evidence tier, human review effort, repair latency, false-positive rate, missed-defect rate, and transfer to new domains.

### 10.4 Adjacencies

The paper has typed interfaces with:

- **Reasoning by Way of Receipts:** a decision and transition should expose its bounded evidentiary basis;
- **The Three Hash Rule:** custody separates artifact bytes, claimed subject, and governing context instead of treating one digest as sufficient;
- **Constraint-Bearing Composability:** a repaired component cannot silently discard inherited obligations when recomposed;
- **Agentic Interface Surfaces:** a builder's progress is recognized only through admissible effect evidence and typed refusal;
- **Governed Meaning Base:** claims, dependencies, findings, disputes, evidence levels, and revisions can be stored as source-bound semantic objects.

These connections improve interpretation. They do not prove identity, derivation, interoperability, or implementation conformance.

## 11. Universal GSM Representation

The case can be represented as a graph whose central objects are claims, artifacts, actors, findings, dependencies, evidence, and dispositions. Typed edges include `DEPENDS_ON`,  
`PRODUCED_BY`, `AUDITED_BY`, `FOUND_IN`, `REPRODUCED_ON`, `REPAIRED_BY`, `ENCODED_AS_TEST`,  
`RATIFIED_BY`, `QUARANTINES`, `SUPERSEDES`, and `CONTRADICTS`.

Every edge should retain source coordinates, exact artifact identity where available, author/AI status, evidence tier, confidence, scope, and revision history. A zero-finding audit remains an event with scope and probe set; it must not become a timeless property of the subject.

The GMB can expose two projections from the same fabric:

- a human case narrative explaining what failed, why it mattered, and what changed;
- an agent surface that retrieves obligations, open attacks, known counterexamples, authority limits, and admissible next actions.

## 12. Realization Funnel

$$
\begin{aligned}
&Possibility \\
&\rightarrow Specification \\
&\rightarrow CM_1 \\
&\rightarrow CM_2 \\
&\rightarrow IC \\
&\rightarrow IR \\
&\rightarrow Evidence \\
&\rightarrow Revision
\end{aligned}.
$$

- **Possibility:** enumerate builder-auditor arrangements, attack strategies, custody models, authority structures, failure modes, and both beneficial and harmful outcomes.
- **Specification:** define roles, subjects, claim semantics, dependency propagation, findings, evidence tiers, gates, and restoration rules.
- **CM1:** retain every admissible configuration, including weakly separated, correlated, expensive, gameable, or operationally brittle forms.
- **CM2:** select preferable forms under defect discovery, false refusal, cost, authority legibility, diversity, privacy, custody, and recovery criteria.
- **IC:** bind an Instance Constitution or Instance Configuration selecting exact roles, models, keys, archives, probes, gates, policies, budgets, and human authorities.
- **IR:** construct an Instance Realization or Implementation Realization of that configuration as an exact runnable alternation and evidence system.
- **Evidence:** retain frozen candidates, replay results, attack traces, findings, reproductions, repairs, regressions, refusals, dispositions, and ratifications.
- **Revision:** update the specification and selected configuration without rewriting the prior lineage.

This paper contributes a Specification, a case-informed CM1/CM2 analysis, and source-reported evidence about one realization. It does not independently certify the IC or realization-stage IR. If a source artifact uses `IR` to mean **Intermediate Representation**, that remains a separate, context-resolved sense; it is not renamed by this funnel.

## 13. Evaluation Program

The primary comparative experiment should freeze one specification and allocate matched budgets to at least:

1. one builder with self-review;
2. one builder plus a separate same-family auditor;
3. one builder plus a different-family auditor;
4. alternating builder and auditor roles;
5. a human or mixed human-AI audit condition;
6. alternation without permanent regressions;
7. alternation without reproduce-before-repair;
8. alternation without retained human disposition.

Seed known defects but also score unseeded findings. Blind the adjudicator to condition where feasible. Measure distinct confirmed defect families, time to reproduction, false findings, repair regressions, surviving seeded defects, new-defect injection, coverage of declared horizons, human labor, compute cost, and claim calibration. Report exact subjects and counting rules.

The result may show that alternation helps, hurts, changes defect types, or is useful only under particular separations and budgets. A negative or conditional result would still improve the architecture.

## Builder-Auditor Alternation Protocol and Case Study

Across the completed P1 corpus, Adversarial Alternation Under Human Governance is the **case study and reusable protocol for alternating AI builders and auditors while human authority retains claim, escalation, and stopping control**. It is not evidence that alternating models are independent, that defects converge to zero, or that human involvement automatically prevents self-ratification.

- **Adjacent work:** *Human Validation Layer: Constitutional Coherence Through Human-Governed Refinement*  
  **Supplies:** Human adjudication and promotion workflow.  
  **Alternation boundary:** HVL governs review standing; alternation supplies a repeated build-audit pattern.

- **Adjacent work:** *Legitimacy Without Self-Ratification*  
  **Supplies:** Threat-model-relative independence and standing ceilings.  
  **Alternation boundary:** Alternation must demonstrate control independence rather than infer it from role labels.

- **Adjacent work:** *From CI/CD to ACG: From Tests to Courts in Agentic Software Development*  
  **Supplies:** Constitutional development, courts, effects, evidence, and revision.  
  **Alternation boundary:** Alternation is one ACG workflow profile.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed evidence carriers and evaluation envelopes.  
  **Alternation boundary:** Audits emit witnesses; witness existence does not prove defect coverage.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Durable transition, refusal, verification, and revision records.  
  **Alternation boundary:** Receipts preserve the sequence and open findings without certifying the infrastructure.

An alternation campaign should bind:

$$
\begin{aligned}
C= (&subject, baseline, builder, reviewer, roles, models, \\
&contexts, rounds, findings, repairs, regressions, \\
&permanent\_tests, human\_decisions, standing)
\end{aligned}.
$$

Independence is multidimensional: model, prompt, context, evidence source, toolchain, organization, operator, and control domain. Changing only a role prompt does not create an independent reviewer. Human approval is meaningful only when the human has adequate evidence, competence, time, and authority and can refuse or stop the campaign.

Every accepted defect should become a permanent counterexample or explicitly justified non-regression obligation. Repeated clean rounds are evidence only over the exercised attack surface. Saturation requires measured marginal yield and stable coverage, not fatigue or absence of newly imagined attacks.

The universal GSM can type `BUILT_IN_ROUND`, `AUDITED_IN_ROUND`, `FOUND_DEFECT`,  
`REPAIRED_BY_SUCCESSOR`, `REGRESSED_ON_COUNTEREXAMPLE`, `PERMANENTLY_TESTED_BY`,  
`INDEPENDENT_UNDER_DIMENSION`, `HUMAN_ADJUDICATED_BY`, `STOPPED_UNDER_RULE`,  
and   
`HAS_CAMPAIGN_STANDING`. These relations preserve the case-study boundary.

This integration establishes four editorial commitments: adopt builder-auditor alternation protocol as the official corpus role; adopt the campaign envelope; require multidimensional independence reporting; and define saturation by coverage and marginal yield rather than clean-round count alone.

## Exact Audit Subjects, Semantic Findings, Domain Firewalls, and Migration Challenge

The fixed-seed comparison with governed project-state lineage, The Locus of Meaning, The Well-Governed Mind, and model-first legacy migration strengthens adversarial alternation by specifying what an audit finding is about and where its method must not be transferred:

$$
\begin{aligned}
C^*= (&campaign, subject\_generation, claim\_binding, builder, \\
&auditor, independence, findings, reproductions, repairs, \\
&counterexamples, human\_decisions, domain\_limits, \\
&migration\_use, standing, remainder)
\end{aligned}.
$$

Project-state lineage binds every round to an exact subject, toolchain, configuration, probe set, and predecessor. The Locus of Meaning requires each finding to identify the claim, jurisdiction, interpretation, consequence, and evidence it challenges; matching words or test identifiers do not establish that two findings are the same defect.

The Well-Governed Mind has no direct methodological transfer from software alternation. Alternating agents must not be presented as clinical assessors, therapeutic reviewers, or evidence for a cognitive mapping. At most, the comparison warns that role labels, repeated agreement, and apparent independence do not create domain competence or authority.

Model-first legacy migration can use alternation to challenge descriptive models, normative classifications, successor realizations, correspondence envelopes, rollback, and residual risk. The audit still cannot infer original intent from behavior or establish equivalence outside the tested envelope.

The universal GSM can type   
`AUDITS_EXACT_SUBJECT_GENERATION`, `CHALLENGES_CLAIM_BINDING`,  
`DISTINGUISHES_DEFECT_IDENTITY`, `PRESERVES_DOMAIN_FIREWALL`,  
`COUNTERTESTS_MIGRATION_MODEL`, `REPRODUCES_BEFORE_REPAIR`, `RETAINS_RESIDUAL_UNCERTAINTY`,  
and   
`STOPS_UNDER_HUMAN_RULE`.

This randomized review establishes four editorial commitments: adopt the exact subject-and-claim campaign envelope; bind defect identity to semantic jurisdiction and consequence; record an explicit non-transfer firewall for clinical and cognitive domains; and use alternation as a bounded migration challenge without general equivalence standing.

## Audit Protocol Reuse Without Methodological Overreach

The frozen P3 field contains four material downstream uses of adversarial alternation. Governed project-state lineage binds exact campaign subjects, findings, repairs, and retained failures. Model-first migration uses alternation to challenge descriptive models, normative classifications, successor realizations, correspondence, rollback, and residual risk. The Locus of Meaning uses it as a bounded countertest for reidentification and binding overextension. The Well-Governed Mind uses it only as a research-review analogy under a clinical jurisdictional firewall.

These uses refine the campaign object:

$$
\begin{aligned}
C^*= (&campaign, subject\_generation, claim\_binding, builder, \\
&auditor, independence, attack\_surface, findings, \\
&reproductions, repairs, counterexamples, \\
&human\_decisions, domain\_limits, standing, remainder)
\end{aligned}.
$$

The reusable core is reproduce-before-repair, exact subject custody, permanent counterexamples, dimension-specific independence, human stopping authority, and marginal-yield reporting over a declared attack surface. The method does not establish semantic truth, program equivalence, clinical validity, or domain competence merely because roles alternate.

Reverse dependency adds a portability condition: every new domain must declare the auditable subject, defect identity rule, oracle, evidence source, reviewer competence, common-mode dependencies, prohibited inferences, and stopping criterion. Where those cannot be specified, the relation remains an analogy or research question rather than a protocol instance.

The universal GSM can type   
`INSTANTIATES_ALTERNATION_PROFILE`,  
`BINDS_EXACT_AUDIT_SUBJECT`, `CHALLENGES_DOMAIN_CLAIM`, `DECLARES_REVIEWER_COMPETENCE`,  
`PRESERVES_METHOD_DOMAIN_FIREWALL`, and   
`RETAINS_UNAUDITED_REMAINDER`.

This reverse-dependency review establishes four editorial commitments: retain the bounded audit-protocol role; add claim binding, attack surface, domain limits, and remainder to the campaign record; require a portability contract for every downstream application; and prohibit clean rounds or role alternation from acquiring truth, equivalence, clinical, or independence standing.

## 14. Counterevidence and Failure Tests

The method must narrow, revise, or fail if: (1) matched self-review performs as well; (2) alternation adds latency without confirmed defects; (3) auditor findings have high false-positive rates; (4) the builder learns to optimize the known audit surface; (5) role switching leaks assumptions; (6) same-family and different-family audits do not differ; (7) both roles miss seeded faults; (8) a finding cannot be reproduced on the shipped subject; (9) a repair changes the subject before reproduction; (10) a regression does not fail on the original defect; (11) a regression is vacuous; (12) an outer gate prevents the test from reaching its target; (13) a test and implementation share the same oracle; (14) a receipt is accepted for another version; (15) a printed `PASS` substitutes for semantic evidence; (16) an unqualified actor mints standing; (17) an artifact ratifies itself; (18) settlement restores standing without re-derivation; (19) upstream restoration silently restores downstream claims; (20) a new claim ignores an older defect; (21) dependency closure is incomplete; (22) two obligations collapse under one identifier; (23) duplicate roots overwrite quarantined state; (24) caller-owned mutation changes admitted state; (25) returned-object mutation changes admitted state; (26) nested metadata bypasses the seal; (27) extra files escape a manifest; (28) path traversal escapes the archive root; (29) links escape custody; (30) empty directories or caches change behavior; (31) replay writes into source custody; (32) rollback restores revoked policy; (33) journal truncation permits replay; (34) an absent attack is reported as a pass; (35)

`PARTIAL` is promoted to complete; (36) zero findings becomes a general soundness claim; (37) changing probe sets are compared as one metric; (38) incompatible counting units are summed; (39) artifact prefixes are treated as authentication; (40) conversational authority is described as cryptographic fact; (41) role separation is called epistemic independence; (42) a participant-written catalog is treated as independently complete; (43) the audit package omits the audit runner; (44) the strongest replay needs an absent file; (45) the paper claims scale from toy programs; (46) independent meaning is derived from builder code; (47) private material crosses the handoff boundary; (48) permanent tests grow without minimization or retirement rules; (49) human ratification becomes a rubber stamp; or (50) publication proceeds before exact recount and primary-source verification.

## Alternating Roles Are Not Independent Evidence by Default

### Public orientation

This case study describes an AI builder, an AI auditor, and a human Governor hardening a small verification system through frozen candidates, cold replay, adversarial probes, reproduced findings, permanent regressions, quarantine, re-derivation, and human ratification. The method is a promising governance pattern. One case cannot establish that alternation is better than careful self-review or genuinely independent audit.

### Adversarial tests

1. **Independence-theater attack.** Builder and auditor share model family, prompts, libraries, fixtures, assumptions, training, or operator framing while being counted as independent.
2. **Moving-probe attack.** Later rounds use different attack surfaces, making lower finding counts look like convergence.
3. **Test-memorization attack.** A repair passes accumulated regressions while the underlying invariant remains wrong or adjacent cases remain untested.
4. **Artifact-substitution attack.** The reviewed archive, replay subject, manifest, evidence, and claimed release are not the same exact object.
5. **Receipt-standing attack.** A validly shaped receipt, passing report, or ledger state grants standing without re-derivation and authorized ratification.
6. **Governor-bottleneck attack.** Human review becomes ceremonial, overloaded, underspecified, or dependent on the same AI summaries.
7. **Survivorship attack.** Successful rounds and accepted findings are retained while abandoned paths, false positives, costs, and missed defects disappear.
8. **Scale-transfer attack.** Results from a small verification subject are generalized to large, stateful, concurrent, physical, social, or high-stakes systems.

### Claim and evidence ceiling

The supplied manuscript supports a source-reported case and an evidence-bounded protocol. It does not establish comparative defect reduction, independence, convergence, general soundness, human control, scalability, cost advantage, or successful cold replay of the cited archives. Finding counts with changing units and probes are descriptive, not a learning curve.

Publication-grade empirical claims require exact archives and reports, authenticated lineage, replay, fixed and adaptive probe sets, explicit independence dimensions, baselines, blind allocation where feasible, cost accounting, missed-defect analysis, and replication. No archive replay or external research occurred in this pass.

### Reader-facing consequence

The public lesson is a disciplined contest between roles: freeze what is being judged, require reproducible findings, turn counterexamples into durable tests, keep claims revocable, and reserve standing for an authorized human decision supported by exact evidence.

## Conclusion

The case's strongest idea is not that two AI sessions are automatically independent or that a falling finding count proves convergence. It is that verification infrastructure should remember how it was wrong. A finding becomes institutionally useful when it is reproduced on an exact subject, generalized into a failure family, retained as a reachable counterexample, and connected to a human-governed disposition without erasing prior state.

Adversarial alternation is therefore a candidate process architecture: a way to produce durable counterevidence, not a guarantee of correctness. The source reports promising episodes in which earlier auditor tests caught later builder errors. Controlled comparisons, exact recounting, heterogeneous audit, and independently replayable custody are required before stronger claims can be made.

## Reference and Verification Note

### Author corpus interfaces inspected under exact custody

Ableman Adam Ableman *Reasoning by Way of Receipts.*

Ableman Adam Ableman *The Three Hash Rule.*

Ableman Adam Ableman *Constraint-Bearing Composability.*

Ableman Adam Ableman *Agentic Interface Surfaces.*

### External verification required

No external literature was consulted. The source names work on truth-maintenance systems, correlated multiversion failure, Goal Structuring Notation, The Update Framework, Certificate Transparency, in-toto, LRAT checking, and AI debate. Those are unverified research leads, unverified research leads in this edition. Further evidentiary strengthening requires primary-source verification, exact bibliographic reconstruction, and comparison against the actual claims made here.

## Appendix: Source-Reported Artifact Prefixes

The source lists the following SHA-256 prefixes: canonical core `d8d7235d`; canonical evidence

`320b22eb`; SIER Q2.1 `3d3890c2`; Q2.2 `de6d0cd6`; Q2.3 `3bcafc3c`; Q2.4 `190a5019`; Q2.5 `c9373a8a`; Q2.6 `01b9ca71`; Q2.7 `cde66ad7`; release RC1 `9a1b9c3a`; RC2 `031e9d6d`; RC3 `960a4586`; RC3-c2 `cdfecf1a`; RC3 Turn A `ec5fa7df`; RC4 `a47ef3ca`; closure receipt `5d53c341`; Governor disposition packet `422d5af2`; MATGATE kit `51980b71`; prefix kit `bc9f8254`; S2 source `9407ed19`; and review ingress `ca8c19e2`.

These prefixes are preserved as source-reported locators only. Full digests and original manifests are required for verification.

## Corpus-Wide Reference Positioning

This paper argues that this paper reports a two-day case study in which two AI sessions alternated between builder and auditor roles while one human Governor retained scope, disposition, and ratification authority. Its nearest external comparison fields are provenance, open sovereign, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Source availability and reproducible builds improve inspectability but do not alone guarantee comprehensibility, practical exit, hardware control, or sustainable maintenance. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E2]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E3]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

**[E4]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E5]** Free Software Foundation. *The Free Software Definition*. https://www.gnu.org/philosophy/free-sw.html **Relationship:** Normative predecessor for user freedoms; the paper may add reconstruction, governance, or hardware-boundary obligations beyond license rights.

**[E6]** Open Source Initiative. *The Open Source Definition*. https://opensource.org/osd **Relationship:** Adjacent licensing baseline; source availability is not treated as sufficient for operational sovereignty.

**[E7]** Martin Kleppmann et al. "Local-First Software: You Own Your Data, in Spite of the Cloud." *Onward! 2019*, pp. 154-178. DOI: 10.1145/3359591.3359737. https://www.inkandswitch.com/local-first/ **Relationship:** Adjacent local-first design program relevant to user custody, offline operation, and collaboration.

### Ableman corpus

**[A1]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *A Formal Theory of Work Custody*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-C8F2F9BF38C45E29`;  
source SHA-256  
`A80657E21BA277ADF1C229A2AAE221963B97A62EA2AF3EBC36434A916A8EEA44`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Governance Witnesses*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-9E8DA0EFE860DE5D`;  
source SHA-256  
`8BF8C3646040F6E1F5222A8AA92C1106AA1F841E8A2C65402F468C83D59D06E5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Sovereign Software*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-24C6159B98023A9C`;  
source SHA-256  
`6AAFE79E438B980B75D1910A897F7BA716A10CF1187B68CB1F71405F36725A18`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Jnana*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-ECEAB04A620F163D`;  
source SHA-256  
`76D921D2975BDCD25D6DFB506F5E85F7AFDBF4D2CCC65F8C45394121F9D90060`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847376](https://doi.org/10.5281/zenodo.23847376)
