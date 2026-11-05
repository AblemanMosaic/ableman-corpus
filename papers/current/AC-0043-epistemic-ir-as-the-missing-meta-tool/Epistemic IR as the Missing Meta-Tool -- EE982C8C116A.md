# Epistemic IR as the Missing Meta-Tool

## Toward Auditable and Contestable Constitutions of Knowledge

### MCIR already proposes a canonical intermediate representation for governed transformation.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Knowledge systems do more than store propositions. They decide what may count as a claim, which evidence may support it, whose judgment may alter its standing, when uncertainty requires deferment, and how decisions can be contested or revised. Those governance commitments are usually distributed across prose, software, institutional practice, standards, and tacit authority.

This paper develops **Epistemic Intermediate Representation (Epistemic IR)** as a candidate representation profile for making that machinery explicit. An Epistemic IR artifact binds an exact claim to its interpretation, scope, epistemic posture, standing, provenance, evidence, applicable standards, authority dependencies, adjudication state, contest history, and revision lineage. An external, versioned admission regime may evaluate the artifact and emit a bounded decision receipt. The representation does not decide truth, manufacture authority, or make a receipt self-validating.

Corpus-wide comparison produces an important compression. MCIR already proposes a canonical intermediate representation for governed transformation. Constitutional Epistemics, Epistemic Authority Governance, Epistemic Situational Awareness, Admissibility Engineering, reasoning receipts, and the Governed Knowledge Loop already supply much of the governance machinery. Epistemic IR should therefore remain a **candidate epistemic profile of MCIR** unless it demonstrates semantics or conformance obligations that the general representation cannot express. Its strongest present contribution is not another foundational substrate, but a portable claim-governance profile that makes admission, refusal, deferment, contest, and revision inspectable without confusing procedural standing with truth.

## 1. The Problem: Knowledge Governance Is Usually Implicit

A statement becomes consequential through more than its words. It may be reused as evidence, promoted into institutional memory, treated as precedent, bound to a decision, or translated into action. Each transition depends on hidden or distributed choices:

* which interpretation of the statement is in force;
* which evidence is admissible and sufficiently current;
* which standard and version applies;
* which actor has jurisdiction for the requested transition;
* which exceptions, private zones, and nonclaims remain attached;
* which outcome states and appeal paths are available;
* when a prior decision expires or must be revised.

Ordinary prose rarely carries this structure in one inspectable artifact. Software often implements only a fragment of it. Institutional procedure may supply the remainder without machine-readable linkage. The result is not merely ambiguity. It is **unlocated epistemic governance**: a claim can acquire standing or downstream force without a single representation showing why that change was admissible.

The source paper describes logic, scientific method, statistical inference, legal procedure, peer review, and philosophical epistemology as partial constitutions of knowledge. That is a useful research hypothesis, not yet a demonstrated historical survey. The stronger claim that no prior framework provides comparable machinery requires current primary-source research and must not support a novelty claim in this revision.

## 2. Definition and Nonclaims

**Epistemic IR** is a versioned, typed representation profile for carrying epistemic artifacts and the governance commitments that control their standing, reuse, contest, and revision across transformations.

Its proposed minimum objects are:

1. claim artifacts;
2. interpretations and semantic identities;
3. epistemic postures and standing states;
4. provenance and evidence bindings;
5. standard, policy, and authority references;
6. admission rules and outcome lattices;
7. decision, refusal, deferment, and gap receipts;
8. contests, appeals, exceptions, expiry, and revision lineage.

An Epistemic IR artifact is not:

* a truth oracle;
* a proof that its evidence is accurate or sufficient;
* a source of institutional or democratic legitimacy;
* permission to bind a person or produce an external effect;
* a substitute for domain methods, law, peer review, or stewardship;
* proof that one ontology is neutral across communities;
* proof that an AI system is an epistemic authority;
* a completed schema, compiler, runtime, or conformance standard.

The representation can expose a governance dependency. It cannot legitimate that dependency merely by naming it.

## 3. Authorial Compression: Profile Before New Substrate

The source presents Epistemic IR as a missing meta-tool. The corpus now contains a more general candidate substrate: **MCIR**, a canonical representation for governed transformation [MCIR]. MCIR already makes admissibility, authority, transformation semantics, and capability exposure structurally visible. Creating a separate foundational IR without a differential obligation would duplicate machinery and fracture the representation stack.

The recommended provisional relation is:

```text
MCIR                         general governed-transformation substrate
  + epistemic profile claim, evidence, standard, standing, contest,
  revision
  = Epistemic IR candidate domain/profile name pending conformance
  evidence
```

Epistemic IR earns distinct profile identity only if it specifies and tests obligations such as:

* claim-role and epistemic-posture separation;
* evidence support and evidence-freshness semantics;
* scoped admission to a named role rather than generic acceptance;
* authority-import and oracle-dependency disclosure;
* contest persistence through reuse and projection;
* standards migration and decision invalidation;
* false-admission, false-refusal, and premature-closure measurement.

If these obligations can be expressed entirely as an ordinary MCIR schema, the novelty lies in the **epistemic conformance profile**, not in a second root representation. If MCIR cannot preserve one of them without semantic loss, a concrete counterexample should identify the missing capability before a new foundational identity is retained.

This compression does not erase the paper. It sharpens its role: the paper specifies what governed knowledge claims require from an intermediate representation.

## 4. Separate the Epistemic Axes

Epistemic systems become unsafe when distinct questions collapse into one status label.

- **Axis:** artifact role  
  **Example values:** observation, report, inference, hypothesis, proposal, commitment, precedent, policy  
  **Question:** What kind of epistemic object is this?

- **Axis:** posture  
  **Example values:** asserted, assumed, derived, estimated, reported, contested, unknown  
  **Question:** How is the content presented?

- **Axis:** support state  
  **Example values:** absent, cited, checked, corroborated, contradicted, stale, disputed  
  **Question:** What support relationship has been evaluated?

- **Axis:** procedural standing  
  **Example values:** draft, submitted, admitted, deferred, refused, contested, superseded, retired  
  **Question:** What happened under a named process?

- **Axis:** authority scope  
  **Example values:** none, advisory, delegated, binding within scope  
  **Question:** What consequences may this actor or artifact legitimately carry?

- **Axis:** effect state  
  **Example values:** no effect, proposed effect, authorized effect, executed effect, reverted effect  
  **Question:** What occurred outside the representation?

Accuracy does not imply authority. Evidence does not imply truth. Validation does not compel admission. Admission does not authorize every reuse. A receipt does not prove its premises. Execution success does not prove understanding.

The source uses `ADMIT`, `DEFER`,  
and `REFUSE`. These are not universal judgments on content. They are outcomes relative to a declared jurisdiction, law or policy version, purpose, time, evidence state, and requested role. The complete statement is not "claim admitted" but "claim admitted as role R, for purpose P, within scope S, by authority A, under law L, at time T, subject to conditions C and expiry X."

## 5. Candidate Artifact Model

Let an epistemic claim artifact be:

$$
\begin{aligned}
C = \langle &id, content, meaning, role, posture, standing, scope, \\
&provenance, evidence, lineage, conditions, exceptions, \\
&nonclaims\rangle
\end{aligned}.
$$

Let the applicable governance context be:

$$
\begin{aligned}
G = \langle &jurisdiction, law, standards, authorities, oracleRefs, \\
&admissibility, outcomes, privacy, contest, time\rangle
\end{aligned}.
$$

Let evaluation be a partial function:

$$
\begin{aligned}
Evaluate_G(C, request) \rightharpoonup \{&ADMIT(role,scope), DEFER(requirements), REFUSE(reasons), \\
&GAP(missing)\}
\end{aligned}.
$$

Partiality matters. A malformed artifact, unresolved identity, absent law head, missing authority evidence, or unsupported target may prevent a legitimate decision. Such a condition should become a typed gap rather than an invented answer.

Every completed evaluation emits a decision record:

$$
\begin{aligned}
R = \langle &subjectHash, meaningRef, lawRef, evidenceRefs, \\
&authorityRef, request, decision, reasons, time, expiry, \\
&contestPath\rangle
\end{aligned}.
$$

The record binds the decision to its inputs. It does not certify that the law was just, the evidence true, the authority legitimate outside its recorded scope, or the implementation correct. Those remain separate claims with separate evidence.

## 6. Admission Is a Transition, Not a Truth Predicate

An epistemic lifecycle may include:

```text
DRAFT -> SUBMITTED -> CHECKED -> ADMITTED(role, scope)
                     |          |
                     | +-> CONTESTED -> REVISED | SUPERSEDED | RETIRED
                     +-> DEFERRED(requirements)
                     +-> REFUSED(reasons)
                     +-> GAP(missing structure)
```

No arrow is automatic. Each transition names:

* the source and target state;
* the actor and asserted authority;
* the applicable law or policy head;
* the evidence and standard versions inspected;
* the conditions, expiry, and nonclaims;
* the contest or appeal route;
* the resulting receipt.

Role and state also remain distinct. An observation can be draft, submitted, admitted for a bounded purpose, contested, or superseded. A hypothesis does not become a fact merely by reaching `ADMITTED`. It earns only the standing that the named procedure is authorized to grant.

## 7. The Oracle Problem Is an Authority-Import Problem

The source uses **oracle** for measurements, prior assignments, institutional standards, interpretive judgments, and peer-review bodies. These are heterogeneous. A measurement source, a normative authority, a semantic interpreter, and an adjudicator should not share one untyped role.

A safer dependency record is:

$$
\begin{aligned}
O = \langle &id, kind, provider, claimType, jurisdiction, method, \\
&version, freshness, authorityBasis, contestPath, limits\rangle
\end{aligned}.
$$

At minimum, `kind` distinguishes:

* observation or measurement source;
* evidentiary evaluator;
* semantic or interpretive dependency;
* standard or policy source;
* normative authority;
* adjudicator.

Naming an oracle makes a dependency visible; it does not make the dependency authoritative. The system must still check provider identity, method, version, freshness, jurisdiction, delegation, revocation, conflicts, and contestability. An oracle output cannot widen its own scope, create the authority that validates it, or silently survive replacement of the applicable standard.

## 8. Preservation Invariants

An Epistemic IR profile should preserve at least these invariants:

1. **Exact-source custody.** The artifact binds or resolves to the exact source it represents.
2. **Meaning identity.** Interpretation and semantic identity are explicit and versioned.
3. **Axis separation.** Role, posture, support, standing, authority, and effect remain distinct.
4. **Support non-equivalence.** Evidence support is not silently promoted to truth.
5. **Validation non-equivalence.** Structural validity is not admission or authorization.
6. **Scoped admission.** Every admission names role, purpose, scope, jurisdiction, law, and time.
7. **Authority non-generation.** A compiler, evaluator, or receipt cannot manufacture authority.
8. **Dependency visibility.** External observations, standards, interpretations, and authorities are typed.
9. **Freshness.** Expired evidence, standards, delegations, and decisions cannot remain current silently.
10. **Contest persistence.** Material objections travel with reuse, projection, and promotion.
11. **Private-zone preservation.** Governance does not imply universal disclosure of protected content.
12. **Loss visibility.** Translation and projection emit residual, omission, and uncertainty records.
13. **Refusal and deferment.** Missing conditions produce bounded negative or suspended outcomes.
14. **No self-promotion.** An artifact cannot grant itself higher standing or binding force.
15. **Receipt boundedness.** A receipt proves only the recorded procedure and bindings actually evidenced.
16. **Revision lineage.** Successors preserve what changed, why, under whose authority, and which prior decisions became invalid.

These are candidate obligations, not claims that an implementation presently satisfies them.

## 9. Worked Example: A Bounded Model-Evaluation Claim

Suppose a team submits:

> Model M meets the deployment reliability threshold.

Ordinary prose hides several decisions. An Epistemic IR candidate separates them:

```text
claim_role: REPORT
posture: ASSERTED
content: model M met metric R >= 0.97
meaning_ref: metric-registry/R/v3
scope: benchmark B, dataset D, environment E
evidence_refs: run-set H1, evaluator V2
standard_ref: reliability-policy/v5
requested_transition: ADMIT as deployment-supporting evidence
authority_ref: evaluation-board/delegation-17
freshness: valid through 2026-12-31
nonclaims:
  - no claim of safety outside E
  - no authorization to deploy
  - no claim that benchmark B captures every failure mode
```

If the evidence hash matches and the metric was computed correctly but the delegation expired, structural checking may pass while admission defers or refuses. If the policy changed from v5 to v6, the prior result may remain a historical fact while losing current standing. If the claim is admitted as **deployment-supporting evidence**, it still does not authorize deployment; an external effect regime must decide that separately.

The example shows the value of the representation: it prevents a successful test result from silently becoming a universal reliability claim, an authority grant, and an execution command.

## 10. Relation to the Ableman Corpus

Epistemic IR is most useful as a bridge among existing machinery:

* **MCIR** supplies the candidate canonical governed-transformation substrate [MCIR].
* **Constitutional Epistemics** distinguishes influence, confidence, jurisdiction, warrant, and binding authority [CE].
* **Epistemic Authority Governance** provides claim types, promotion, binding, refusal, termination, contest persistence, and the governing question of the right to proceed [EAG].
* **Epistemic Situational Awareness** locates acts, layers, authority consequences, and lawful stopping at runtime [ESA].
* **Admissibility Engineering** separates candidate construction from admission under explicit conditions [AE].
* **Reasoning by Way of Receipts** treats intermediate decisions as evidence-bearing but not self-proving [RWR].
* **The Governed Knowledge Loop** places analysis, crystallization, structural integration, frontier detection, and revision inside a continuing knowledge lifecycle [GKL].
* **Constitutional Epistemology Under Adversarial Semantic Pressure** supplies omission, laundering, posture, evidence, and authority threat surfaces [CESP].
* **The Three Hash Rule** motivates separation among exact artifact custody, governing commitments, and meaning commitments [THR].
* **Governed Controlled Natural Language** can provide a human-authorable front end, pending its own profile and identity adjudication [GCNL].

**Governed Meaning Base (GMB)** is the current name in the historical `CCF -> CMB -> GMB` lineage. GMB can store exact sources, candidate interpretations, Epistemic IR artifacts, evidence relations, admission decisions, contests, receipts, and revisions. Storage in GMB does not grant truth, standing, or permission. Hyperpedia can project the same governed objects for human study while preserving links back to exact sources and standing.

A provisional representation path is:

```text
source prose or GCNL candidate
  -> Epistemic IR profile candidate on MCIR
  -> external admission under declared epistemic law
  -> bounded promotion or GMB mutation
  -> optional operational lowering
  -> evidence, contest, and revision
```

This path is a comparison target, not an adjudicated universal stack.

## 11. Configuration Manifold

An Epistemic IR is not one inevitable schema. Its configuration manifold includes:

* centralized, federated, individual, institutional, and mixed authority models;
* closed, public, selectively disclosed, and privacy-preserving evidence regimes;
* strict, permissive, probabilistic, plural, and appeal-heavy admission policies;
* immutable, append-only, revisable, expiring, and revocable standing models;
* single-ontology, mapped-ontology, and explicitly incommensurable semantic regimes;
* human, machine, hybrid, and institutionally delegated adjudication;
* local, portable, federated, and cross-jurisdictional artifact exchange.

**CM1** contains configurations that satisfy the declared representation specification and basic non-generation, custody, and transition invariants. It can still include brittle, coercive, inaccessible, centralized, or surveillance-heavy realizations.

**CM2** prefers configurations that reduce authority concentration, disclosure pressure, ontology lock-in, false admission, false refusal, premature closure, contest erasure, translation loss, and authoring burden while improving auditability, accessibility, exit, forkability, correction, and evidence freshness.

**Instance Configuration** selects one exact schema, identity regime, law head, standards registry, authority registry, evidence store, evaluator, receipt format, privacy model, appeal path, projection set, and conformance suite for one realization.

## Candidate MCIR Epistemic Conformance Profile

Across the completed P1 corpus, Epistemic IR is strongest as the **candidate epistemic conformance profile on MCIR that requires claim role, meaning, evidence, standing, authority, scope, contest, expiry, loss, and revision to survive together**. It is not yet a second foundational Intermediate Representation, a truth language, or an authority source. The unresolved architectural question is whether its obligations require a named profile or are already expressible through MCIR plus adjacent contracts.

- **Adjacent work:** *Representational Topology in MCIR: AST, DAG, and Emergent Governance Capabilities*  
  **Supplies:** Local AST, canonical DAG, and separate receipt-lineage topology.  
  **Epistemic-IR boundary:** Epistemic IR constrains what epistemic commitments those structures must carry.

- **Adjacent work:** *Admissibility Engineering*  
  **Supplies:** Candidate construction, constraint surfaces, negative outcomes, and evidence.  
  **Epistemic-IR boundary:** The profile represents admission requests and results without making admission truth.

- **Adjacent work:** *Epistemic Situational Awareness and the Governed Knowledge Loop*  
  **Supplies:** Runtime posture and temporal epistemic lifecycle.  
  **Epistemic-IR boundary:** Epistemic IR is a portable artifact profile feeding those capabilities.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Bounded inference from procedure, decision, effect, and evidence records.  
  **Epistemic-IR boundary:** Receipts accompany conformance and admission without self-promoting the artifact.

- **Adjacent work:** *The Governed Knowledge Loop*  
  **Supplies:** Observation, crystallization, integration, contradiction, evaluation, and revision.  
  **Epistemic-IR boundary:** The profile gives loop artifacts a shared machine-legible contract.

A conforming artifact should bind:

$$
\begin{aligned}
E= (&source, semantic\_identity, claim\_role, posture, \\
&support, standing, scope, evidence, authority, \\
&dependencies, contest, conditions, expiry, loss, \\
&nonclaims, lineage)
\end{aligned}.
$$

The profile must prove a differential. If ordinary MCIR with declared schemas and lifecycle records preserves every obligation with equal authorability, interoperability, and assurance, the separate Epistemic IR name should be absorbed. If it remains, conformance means only that the artifact satisfies the named profile; truth, legitimacy, institutional authority, and effect permission remain external judgments.

In this title, `IR` means Intermediate Representation. In the realization funnel,

`IR` means Instance Realization / Implementation Realization. An Epistemic IR artifact may be used within a realization-stage IR, but the acronym collision never creates identity between representation and realization.

The universal GSM can type   
`CONFORMS_TO_EPISTEMIC_PROFILE`, `REPRESENTS_CLAIM_ROLE`,  
`HAS_EVIDENCE_POSTURE`, `REQUESTS_SCOPED_ADMISSION`, `PRESERVES_CONTEST`,  
`EXPIRES_WITH_AUTHORITY`, `EMITS_TRANSLATION_LOSS`, `LOWERED_FROM_HUMAN_AUTHORING`,  
`RETAINED_IN_GOVERNED_LOOP`,  
and   
`ABSORBED_IF_NO_DIFFERENTIAL`. These relations turn novelty into a testable architecture decision.

This integration establishes four editorial commitments: classify Epistemic IR provisionally as an MCIR epistemic conformance profile; adopt the conformance envelope; require a differential comparison against unprofiled MCIR and simpler structured records; and preserve the Intermediate Representation versus Instance/Implementation Realization distinction in every use.

## Epistemic Obligation Placement Across Three Graphs

The fixed-seed comparison with legitimacy, recursive motifs, Governance Witnesses, and the three-graph MCIR contract locates Epistemic IR obligations across distinct representations:

$$
\begin{aligned}
E= (&authoring\_assertion, canonical\_claim, witness\_set, \\
&receipt\_lineage, standing, contest, expiry, loss)
\end{aligned}.
$$

The authoring AST preserves what was proposed and by whom. The canonical DAG identifies resolved claim, evidence, authority, and dependency objects under explicit equivalence rules. The receipt graph preserves admission, refusal, witness evaluation, standing change, contest, expiry, and revision. A hash or conformance result for one graph cannot stand in for the others.

Governance Witnesses supplies the evidence-carrier contract. Epistemic IR can encode witness identity, method, coverage, relevance, and ceiling, but cannot convert the carrier into truth or sufficiency. *Legitimacy Without Self-Ratification* constrains promotion: an artifact must not ratify its own standing merely because it contains internally consistent authority and evidence fields.

Recursive motifs remain `PEDAGOGICAL_ONLY`. A motif may help explain the proposed claim-gate-realization-evidence structure, but its recurrence supplies no differential for retaining Epistemic IR as a separate named profile. The profile survives only if it improves authorability, interoperability, preservation, or assurance over ordinary MCIR schemas.

The universal GSM can type   
`AUTHORED_AS_EPISTEMIC_AST`,  
`RESOLVED_AS_CANONICAL_CLAIM_DAG`, `EVALUATED_IN_RECEIPT_GRAPH`,  
`CARRIES_WITNESS_WITH_CEILING`, `REQUESTS_STANDING_WITHOUT_SELF_RATIFICATION`,  
`PRESERVES_CONTEST_ACROSS_GRAPH`, and   
`USES_MOTIF_AS_PEDAGOGY_ONLY`.

This randomized review establishes four editorial commitments: adopt the three-graph obligation placement; keep witness carrier, evaluation receipt, and standing decision separate; apply anti-self-ratification to epistemic promotion; and exclude motif fit from the profile differential.

## An MCIR Epistemic Conformance Profile

Five downstream uses place Epistemic IR beside Cognitive ABI representations, Governance Witnesses, anti-self-ratification, recursive motifs, and MCIR topology. They confirm the paper's own authorial compression: Epistemic IR is best treated as a candidate MCIR epistemic conformance profile, not a new universal substrate and not the realization-stage IR of the funnel.

$$
\begin{aligned}
E^*= (&claim, subject, scope, proposition, status, support, \\
&counterevidence, alternatives, uncertainty, authority, \\
&standing, obligations, witnesses, admission, expiry, \\
&revision)
\end{aligned}.
$$

Claim status, evidence kind, warrant, confidence, authority, standing, and admission remain separate axes. A profile can represent an oracle's output without importing the oracle's authority. Missing, withheld, contradicted, unresolved, stale, and out-of-scope are typed states. Motifs, summaries, and model evaluations become claims about exact subjects rather than evidence merely by being encoded.

Translations among Epistemic IR, Workflow IR, Action IR, GCNL, MCIR, and evidence graphs require explicit identity, preservation, and remainder contracts. A graph topology may aid traceability but cannot prove warrant. Promotion requires an external policy and standing decision; the artifact cannot ratify itself.

The universal GSM can type   
`CONFORMS_TO_EPISTEMIC_IR_PROFILE`,  
`REPRESENTS_EPISTEMIC_CLAIM`, `CARRIES_COUNTEREVIDENCE`, `WITHHOLDS_EPISTEMIC_PROMOTION`,  
`TRANSLATES_WITH_EPISTEMIC_REMAINDER`, `EXPIRES_EPISTEMIC_STATUS`,  
and   
`DOES_NOT_SELF_RATIFY`.

This review establishes four editorial commitments: retain MCIR-profile standing; adopt the epistemic claim record; require typed negative and stale states plus translation remainder; and keep representation, evidence, warrant, authority, standing, admission, and truth distinct.

## 12. Failure Modes and Counterevidence

The proposal should weaken or fail under evidence that:

* ordinary signed records plus existing workflow standards preserve the same obligations with less complexity;
* MCIR already expresses the full epistemic profile without any distinct extension;
* authors cannot understand or reliably produce the artifacts;
* formalization suppresses tacit, minority, qualitative, or context-dependent knowledge;
* the ontology fixes one institution's worldview and makes disagreement appear malformed;
* governance metadata creates unacceptable surveillance or coerced disclosure;
* receipts encourage procedural compliance theater while evidence quality declines;
* evaluators disagree materially on identical artifacts;
* false refusal blocks legitimate inquiry or false admission launders weak claims;
* admission thresholds become optimization targets and invite Goodhart effects;
* contest, appeal, and exit exist in the schema but not in deployed practice;
* mappings across communities erase distinctions or manufacture equivalence;
* stale decisions retain standing after evidence, authority, or standards change;
* operators, registries, or infrastructure providers become an undeclared sovereign layer;
* the cost of maintaining the representation exceeds its value for the target domain.

Three source claims require particular qualification.

First, the representation is not neutral. Every schema selects objects, relations, omissions, and decision states. It can make commitments explicit and comparable, but neutrality must not be inferred from structure.

Second, machines are not logically necessary for epistemic governance. They may become operationally valuable at scale. The threshold at which they become necessary is an empirical and institutional question, not an axiom.

Third, declared authority is insufficient. Authority may be clearly declared yet illegitimate, expired, coerced, mis-scoped, or unreviewable. Declaration is a prerequisite for inspection, not the completion of legitimacy.

## 13. Conformance and Evaluation Program

Before making implementation-ready claims, the profile needs:

1. a normative schema and canonical encoding;
2. exact semantic identity and reference-resolution rules;
3. typed claim, evidence, standard, authority, decision, contest, and revision objects;
4. positive, negative, boundary, malformed, stale, revoked, and ambiguous fixtures;
5. independent encoders, decoders, and evaluators;
6. mutation tests proving that governance-relevant changes alter the canonical artifact;
7. replay tests binding decisions to exact law, evidence, authority, and time;
8. translation-loss and round-trip tests;
9. false-admission, false-refusal, and unresolved-gap measurement;
10. expiry, revocation, appeal, contest-persistence, and successor-invalidation tests;
11. privacy and selective-disclosure threat tests;
12. plural-ontology and cross-jurisdiction mapping tests;
13. authorability and accessibility studies;
14. comparison against simpler structured-record and workflow baselines;
15. one low-consequence end-to-end domain profile with independent review.

Passing representation conformance cannot establish truth, justice, legal validity, institutional legitimacy, or authorization for external effect.

## 14. Realization Funnel

| Stage | Epistemic IR role |
|---|---|
| Possibility | Explore claim models, state lattices, evidence relations, standard regimes, authority structures, privacy models, contest mechanisms, ontologies, lowerings, and harmful or unusable configurations. |
| Specification | Define grammar, schema, canonicalization, identities, types, lifecycle transitions, loss records, admission interface, receipts, failure codes, conformance, and nonclaims. |
| CM1 | Enumerate all configurations satisfying the specification and minimum invariants, including centralized, expensive, brittle, exclusionary, or surveillance-heavy variants. |
| CM2 | Prefer configurations with bounded authority, persistent contest, privacy, accessibility, semantic pluralism, correction, forkability, low loss, and measured refusal/admission error. |
| Instance Configuration | Select the exact profile, law head, registries, stores, actors, evaluators, receipt format, privacy model, appeal path, targets, environment, and tests. |
| Implementation Realization | Build encoders, validators, evaluators, registries, stores, projections, admission adapters, mutation interfaces, and receipt paths for that configuration. |
| Evidence | Execute conformance, replay, mutation, adversarial, expiry, privacy, accessibility, authorability, comparison, and independent-implementation tests; retain disagreement. |
| Revision | Create successors when schema, meaning, evidence, standards, authority, law, outcomes, targets, or findings change; preserve migrations and invalidated claims. |

The source paper supplies a compelling possibility and architectural thesis. It does not yet supply a normative specification, implementation, or empirical evaluation.

## Epistemic Structure Without Epistemic Sovereignty

### Public orientation

Epistemic IR is an Intermediate Representation for claims, sources, standards, warrants, defeaters, adjudication, and outcome transitions. It makes epistemic governance inspectable and portable. The representation and the AI systems operating it do not become authorities over truth merely because reasoning has been structured.

### Adversarial tests

1. **Schema-as-truth attack.** A claim fits the IR and is treated as correct. Well-formedness, admissibility, warrant, and truth remain distinct.
2. **Imported-authority attack.** A citation or institution is encoded with standing beyond its jurisdiction, date, or competence. Authority imports need scope and expiry.
3. **Source-staleness attack.** Evidence is superseded, retracted, inaccessible, or contextually obsolete. Dependency and invalidation propagation are required.
4. **Adjudicator-capture attack.** One model generates claims, assigns standards, weighs evidence, and promotes outcomes. Roles and human decision gates must remain visible.
5. **Graph-inconsistency attack.** Claim, evidence, authority, and receipt graphs disagree while each is locally valid. Cross-graph correspondence needs explicit tests.
6. **Defeater-suppression attack.** Negative evidence is omitted or down-ranked. Counterevidence custody and search remainder must be first-class.
7. **Privacy and privilege attack.** Structuring evidence exposes protected sources, identities, or deliberation. Visibility and use require separate policy.
8. **Formalization-overreach.** Numeric confidence or typed status suggests more precision than the evidence supports. Uncertainty and unresolved conflict must survive lowering.

### Claim and evidence ceiling

The paper proposes an MCIR epistemic conformance profile and evaluation program. It does not establish a universal epistemology, automated truth adjudication, complete evidence collection, unbiased evaluation, or semantic equivalence across domains.

Claims about argumentation systems, knowledge representation, evidence law, scientific inference, fact checking, or AI evaluation require external comparison and domain review. Internal examples demonstrate expressibility only. No external research was added in this pass.

### Terminology boundary

In **Epistemic IR**, IR means **Intermediate Representation**. This is distinct from realization-stage IR, which may mean Instance Realization or Implementation Realization.

### Reader-facing consequence

The public value is an auditable claim path: what was asserted, which standard applied, which sources and defeaters were considered, who had authority to decide, and how later evidence can reopen the result.

## 15. Research Agenda and Open Questions

1. Decide whether Epistemic IR remains a distinct profile name, becomes an MCIR epistemic conformance profile, or is absorbed into EAG/CE machinery.
2. Define the differential obligations that cannot be expressed by unprofiled MCIR.
3. Replace the untyped oracle category with explicit dependency and authority kinds.
4. Define the claim-role, posture, support, standing, authority, and effect axes.
5. Define scoped admission, expiry, contest, appeal, and invalidation semantics.
6. Define exact interaction with GMB, GCNL, MCIR, GSOL, EAG, ESA, GKL, and receipts without forcing a disputed universal stack.
7. Select one low-consequence profile only under separate implementation authorization.
8. Conduct primary-source research into knowledge representation, argumentation, provenance, scientific workflow, evidence standards, policy languages, legal knowledge representation, formal epistemology, and institutional governance before historical or novelty claims.

## 16. Conclusion

Epistemic IR identifies a real representational need: knowledge claims should not acquire standing, reuse authority, or downstream force through invisible transitions. A portable artifact can make claim role, interpretation, evidence, standards, authority dependencies, admission, contest, and revision inspectable.

The corpus also changes the architectural conclusion. This need does not yet justify a second foundational IR. MCIR already supplies a general governed-transformation substrate; CE, EAG, ESA, Admissibility Engineering, receipts, GKL, and GMB supply adjacent governance and lifecycle machinery. Epistemic IR is presently strongest as the profile that asks whether those components preserve epistemic commitments together.

The governing principle remains valuable but incomplete:

> Authority must be declared before it is exercised.

To that principle this revision adds: declaration does not legitimate authority; admission does not establish truth; and structure must remain contestable, revisable, and bounded before it may carry consequences.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that knowledge systems do more than store propositions. Its nearest external comparison fields are formal, provenance, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E2]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E3]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

**[E4]** Leslie Lamport. *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Addison-Wesley, 2002. https://lamport.azurewebsites.net/tla/book.html **Relationship:** Predecessor specification discipline for state machines, safety, liveness, and refinement.

**[E5]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E6]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E7]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

### Ableman corpus

**[A1]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Ableman Corpus current edition; work identity `PAPER.PUB.21095303`;  
source SHA-256  
`EA129ECBA95F7B07CAA7B33A54F91F52913C94A14DA227EB9A06CFD083E4E5BF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Governed Semantic Compilation*. Ableman Corpus current edition; work identity `PAPER.PUB.18453681`;  
source SHA-256  
`5FF6C636550B04DB0E2F6F94C379BB75AA0BD8781E19B047D7D3BB6D49071AC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Hybrid Semantic Compiler Architectures*. Ableman Corpus current edition; work identity `PAPER.PUB.21228038`;  
source SHA-256  
`EBCD6DDDA9B547639AEBED79FB68069473CF1248E41C527B48C9624BBE2C0496`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Admissibility Engineering*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F1E33B5E973B0900`;  
source SHA-256  
`CDC80271268802CA5CB4DE3624B992FB2FF07D677BF945C4B349BD307C4C2A6E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Everything Is a Compiler*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-30FB8F95BD990A47`;  
source SHA-256  
`FE0F88A1F125317285BE4378E5F27ACC9FEB83ADE3FF329A3DA9F9CB026DF9A9`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

#### Ableman Corpus references

**[MCIR]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Exact reviewed source SHA-256  
`762E10A91D94B949F5C862CEB732BE976A0CDF74C828061353AAED4CF5024510`; supplied Zenodo title match, with exact publication identity retained separately.

**[CE]** Adam Ableman. *Constitutional Epistemics*. Exact reviewed source SHA-256  
`AC27B7E22BBC4B4CD16D2AC6C78EAF4F82D6C984277693EE9B2AED10C9B12E3B`; publication identity overlap remains under review.

**[EAG]** Adam Ableman. *Epistemic Authority Governance Atlas v0.1*. Exact reviewed Markdown source SHA-256  
`C1D4AFDBA6129E9D5A2E37351C168A455D0A55E41E3A520AC39AF42DF0B1CEBE`; the supplied registry contains a title-matched PDF publication record, which is not silently substituted for this source artifact.

**[ESA]** Adam Ableman. *Epistemic Situational Awareness*. Exact reviewed source SHA-256  
`825352335C61AEAEB6AF1840CE86E4CB32049BFD925E8F181CFA2DD97B6F3275`; supplied Zenodo title match, with exact publication identity retained separately.

**[AE]** Adam Ableman. *Admissibility Engineering*. Exact reviewed source SHA-256  
`FA80D5895A569839958193735B754BE62EE20E1B399A06CB3BA959614DEBF7A3`; separately custodied reviewed source.

**[RWR]** Adam Ableman. *Reasoning by Way of Receipts*. Exact reviewed source SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`; separately custodied reviewed source.

**[GKL]** Adam Ableman. *The Governed Knowledge Loop*. Exact reviewed source SHA-256  
`C8CF0E10ACD0A1CCD91789363F1B28E1D7E8DC1865396C27DAAB6A40C6D32C7C`; separately custodied reviewed source.

**[CESP]** Adam Ableman. *Constitutional Epistemology Under Adversarial Semantic Pressure*. Exact reviewed source SHA-256  
`909F67AD82D8D8C6119FFEABCC8F885EF8C0A095DE79BFA29A65FDB1DC9E64C3`; separately custodied reviewed source.

**[THR]** Adam Ableman. 2026. *The Three Hash Rule*. Zenodo. DOI:   
  `10.5281/zenodo.20788617`. Exact reviewed Markdown source SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.

**[GCNL]** Adam Ableman. *Governed Controlled Natural Language*. Exact reviewed author source SHA-256  
`B0317502B2B10790942DCE3CBFDE58C13E648890AB64A172BB9AE18CA1896D72`; the separate expanded revision remains an AI-assisted integrated edition.

No external research was conducted in this pass. The source paper's historical comparisons and the broader novelty claim require current primary-source verification for a future evidence-qualified revision readiness.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847641](https://doi.org/10.5281/zenodo.23847641)
