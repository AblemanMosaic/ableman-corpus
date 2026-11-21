# The Integrity Enforcement Layer

## A Constitutional Substrate for Refusal-Centric Systems

### "The measure of trust is not what a system permits, but what it can refuse without ambiguity."

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Most software systems are optimized for successful execution. Their primary question is:

> Can the requested action be performed?

Governance systems, integrity systems, audit systems, provenance systems, and constitutional systems face a different question:

> Can an action be refused correctly, consistently, durably, and verifiably?

This distinction is foundational.

A conventional application often presents successful operation as evidence of trustworthiness. A governance system also requires principled refusal. Neither success nor refusal is sufficient by itself; each must be scoped, evidenced, and connected to observed effects. It must reject forged authority, corrupted records, invalid lineage, inconsistent state, replayed requests, malformed inputs, and unverifiable claims. Failure to refuse correctly is itself a governance failure.

This paper proposes the Integrity Enforcement Layer (IEL), a constitutional substrate positioned beneath governance logic and above storage, execution, and transport mechanisms. The IEL centralizes adversarial validation, verification semantics, corruption handling, atomic mutation, and contextual reconstruction into a single enforcement spine.

The purpose of the IEL is not to define governance. Governance defines meaning. The IEL enforces the declared admissibility and integrity conditions under which a governance result may acquire protected effects. It does not define truth or trust in the abstract.

---

## 1. Introduction

Modern software commonly treats adversarial behavior as an edge case.

Governance systems cannot.

In ordinary applications, correctness is demonstrated through successful execution. In integrity systems, correctness is demonstrated through successful refusal.

A banking system proves itself by refusing fraudulent transfers.

A certificate authority proves itself by refusing invalid certificates.

A governance kernel proves itself by refusing illegitimate governance.

This inversion creates a fundamental architectural challenge.

The system must ensure that every subsystem:

* validates before mutation,
* distinguishes corruption from absence,
* preserves historical context,
* performs atomic mutations,
* avoids hidden state changes,
* expresses precisely what has been verified.

Experience suggests that implementing these principles independently within each subsystem leads to drift. The same classes of failures emerge repeatedly across manifests, archives, receipts, verifiers, transports, policy systems, and authority systems.

The Integrity Enforcement Layer is proposed as a solution to this repetition.

---

## 2. The Refusal Problem

Most architectures are designed around execution.

The request enters.

Validation occurs.

The action executes.

A result is returned.

This model is insufficient for governance.

Governance introduces a second responsibility:

The refusal itself becomes a governed artifact.

A refusal must be:

* correct,
* durable,
* explainable,
* attributable,
* reproducible,
* auditable.

An integrity system therefore contains two products:

1. Actions.
2. Refusals.

Historically, engineering effort concentrates on the first.

The IEL is motivated by the observation that trustworthy refusal is a load-bearing and frequently under-specified product of governance systems.

---

## 3. The Integrity Gap

Many systems possess verification mechanisms.

Fewer systems possess verification discipline.

A recurring failure pattern appears across governance software:

The claim becomes larger than the proof.

Examples include:

* linkage verification presented as integrity verification,
* signature verification presented as context verification,
* receipt existence presented as receipt validity,
* authority declaration presented as authority legitimacy.

In such cases, verification exists but its scope is ambiguous.

The IEL introduces explicit verification semantics to eliminate this ambiguity.

---

## 4. Architectural Position

The IEL sits beneath governance semantics but above implementation details.

```text
Applications

Governance Layer

Integrity Enforcement Layer

Storage / Transport / Runtime
```

Applications define intent.

Governance defines meaning.

The IEL defines admissibility.

Storage and transport persist or convey commitments and outcomes under their own failure models. They do not determine admissibility, but IEL claims remain false if those substrates are assumed infallible.

### 4.1 Operative Primitives

| Primitive | Meaning |
| --- | --- |
| Protected effect | A state change or externally relevant action whose admission is governed. |
| Integrity profile | The declared invariants, evidence requirements, verification dimensions, refusal conditions, and atomic boundary for a class of effects. |
| Integrity context | The exact identity, authority, policy, epoch, state, admissibility, meaning, and validator frame under which a request is evaluated. |
| Verification claim | A scoped statement that named dimensions were checked against named commitments under a named profile. |
| Refusal | A governed terminal outcome denying the requested effect for explicit reasons. |
| Defer | A non-terminal outcome withholding decision until declared evidence or authority becomes available; it is not success or refusal. |
| Mutation plan | The complete intended effect set and commit boundary evaluated before authoritative mutation begins. |
| Classified remainder | Work or effects not completed atomically, retained as explicit indeterminate, compensating, or recovery state rather than hidden partial success. |
| Integrity receipt | A record binding request, context, profile, evidence, decision, attempted effects, committed effects, refusal or remainder, and resulting state. |

The IEL does not decide the substantive meaning of governance. It enforces the declared integrity conditions under which a governance decision may acquire effects.

---

## 5. Foundational Laws

The IEL is built upon five proposed constitutional invariants, each interpreted through an explicit integrity profile.

### 5.1 Compact Formal Contract

Let $q$ be a request, $C$ its integrity context, $P$ the applicable integrity profile, $E$ the evidence set, $M$ the proposed mutation plan, and $o$ the terminal outcome. Then:

$$
\begin{aligned}
&\operatorname{Commit}(M) \\
&\Rightarrow \operatorname{ValidContext}(C) \\
&\land \operatorname{Applicable}(P,q,C) \\
&\land \operatorname{Satisfied}(P,E) \\
&\land \operatorname{Authorized}(q,C) \\
&\land \operatorname{AtomicOrClassified}(M,P)
\end{aligned}.
$$

The terminal outcome must be explicit:

$$
\begin{aligned}
o \in \{&\operatorname{PERMIT}, \operatorname{REFUSE}, \\
&\operatorname{DEFER}, \operatorname{INDETERMINATE}\}
\end{aligned}.
$$

No outcome may be inferred from the absence of an error. `INDETERMINATE` is required when the system cannot prove either complete commitment or complete non-effect. A receipt records the basis and consequences of the outcome; receipt existence does not by itself establish correctness, completeness, or standing.

### Law A: Validation Before Mutation

No protected state may change until every refusal condition declared applicable by the governing profile has been evaluated, or the operation terminates with an explicit defer or indeterminate outcome.

Implications:

* no admission before authority verification,
* no receipt before semantic validation,
* no nonce consumption before request acceptance,
* no archive mutation before integrity checks.

---

### Law B: Corruption Is Not Absence

Missing state and corrupt state are fundamentally different conditions.

```text
Missing -> bootstrap may be possible under an antecedent profile
Corrupt -> fail closed for the affected boundary; quarantine,
repair, bounded degradation, or halt must be explicit
```

The IEL forbids silent conversion between the two.

---

### Law C: Verification Must State Its Scope

Verification results must describe exactly what was proven.

The IEL defines:

```text
LINKAGE
BODY
CONTEXT
IDENTITY
QUORUM
FULLY_VERIFIED
```

A system may never claim a dimension or named verification profile that it has not established. The dimensions need not form a total order, and `FULLY_VERIFIED` means only that every dimension required by a declared profile was established for the scoped subject.

---

### Law D: Read Paths Must Not Mutate Authoritative State

Observation must not create history.

Verification.

Attestation.

Status inspection.

Audit.

Projection.

All must remain free of changes to authoritative state, decision inputs, standing, evidence, and governed history. If caches or telemetry are permitted, they must be isolated, declared, and incapable of altering the observed outcome.

---

### Law E: Multi-Step Mutations Must Be Atomic

No operation may silently present a partial effect as a completely committed truth. The integrity profile must declare the atomic boundary and classify any remainder, compensation, recovery duty, or indeterminate external effect.

Atomicity is not a storage concern alone.

It applies equally to:

* manifests,
* archives,
* receipts,
* seals,
* validator sets,
* governance transitions.

---

## 6. Core Components

### 6.1 IntegrityContext

Represents the trust boundary under which evaluation occurs.

Provides:

* deployment identity,
* authority frame,
* policy frame,
* epoch frame,
* validator frame.

---

### 6.2 VerificationLevel

Represents verified scope.

```text
LINKAGE
BODY
CONTEXT
IDENTITY
QUORUM
FULLY_VERIFIED
```

These names become structured claim dimensions or profiles rather than an assumed universal ladder. Each result binds the scoped subject, exact commitments, method, evidence, profile, and limitations.

---

### 6.3 CorruptionKind

Provides a canonical corruption taxonomy.

```text
MISSING
MALFORMED
CORRUPT
FORGED
STALE
ORPHANED
AMBIGUOUS
UNVERIFIED
```

The goal is shared language across all subsystems.

---

### 6.4 ReadOnlyGuard

Enforces mutation-free execution.

Any attempted mutation of protected state causes refusal. Declared diagnostic side effects, if permitted, remain outside the protected decision state and must not alter the result.

---

### 6.5 MutationTransaction

Provides atomic governance mutation.

All protected changes within the declared atomic boundary become one constitutional operation. External or distributed effects that cannot be made atomic require refusal, compensation, or an explicit classified remainder.

---

### 6.6 ReceiptContextResolver

Reconstructs historical context from evidence.

Verification must not depend on current state.

Verification must depend on receipt-time state.

---

### 6.7 Adversarial Harness

Provides reusable hostile testing.

Every subsystem inherits the same adversarial test suite.

---

## 7. Inheritance of Integrity

The most significant property of the IEL is inheritance.

Applications should not merely inherit governance records.

Applications should be able to inherit governance discipline through complete mediation and verified configuration; inheritance is never automatic merely because a library or substrate is present.

An application built atop a governance substrate should automatically receive:

* replay protection,
* refusal receipts,
* verification semantics,
* corruption taxonomy,
* atomic mutations,
* adversarial testing infrastructure.

This transforms integrity from a feature into an environmental condition.

---

## 8. Relationship to Existing Traditions

The IEL does not emerge from a single predecessor.

It is a synthesis.

Its ancestry includes:

### Reference Monitors

Always-invoked enforcement mechanisms.

### Capability Systems

Authority represented as explicit capability.

### Policy Engines

Admission control before execution.

### Transaction Systems

Atomic mutation and durability guarantees.

### Provenance Systems

Traceable historical evidence.

### Constitutional Systems

Higher-order constraints governing lower-order behavior.

The IEL combines these traditions around a single objective:

Trustworthy refusal.

---

## 9. The Adversarial Perspective

The IEL treats every relevant trust and effect boundary as adversarially testable.

Not because hostility is expected.

Because trust claims require proof.

Every subsystem must be evaluated against:

* malformed input,
* replay,
* corruption,
* omission,
* partial failure,
* inconsistent context,
* temporal drift,
* forged authority.

The objective is not paranoia.

The objective is determinism under adversity.

---

## 10. The Constitutional Model

Governance systems traditionally describe what is permitted.

The IEL describes what is impossible.

This distinction mirrors constitutional law.

Ordinary governance may evolve.

Constitutional constraints exist above ordinary governance.

In this sense, the IEL functions as a constitutional substrate.

Subsystems may disagree about meaning.

Subsystems may evolve.

Subsystems may be replaced.

The constitutional layer persists across ordinary subsystem change but may itself evolve only through its declared amendment, migration, and evidence rules.

---

## 11. Stack and Corpus Integration

The IEL is one layer in a larger constitutional-computing stack, not a synonym for that stack.

| Structure | Relation to IEL |
| --- | --- |
| FGA | Supplies the governed-transition grammar and admissibility form that an IEL profile can enforce. |
| Three Hash Rule | Keeps state, admissibility configuration, and meaning commitment distinct; an IEL check must not let one matching commitment stand in for another. |
| CK | Supplies a portable constitutional contract or profile. IEL enforcement should remain profile-driven rather than making CK dependent on one implementation. |
| UGK | Provides an executable reference realization and receipt/certification substrate in which IEL obligations such as verifier-boundary discipline and EffectAtomicity may be implemented and tested. Implementation proof remains scope-bounded. |
| CGP | Adds capability, evidence, posture, sufficiency, and execution surfaces over the kernel; posture is not automatically effect authority. |
| GMB and universal GSM | Preserve governed meaning and semantic commitments. IEL mediates protected GMB mutations but does not decide semantic truth merely because material is stored. |
| *Semantic Debt* | Diagnoses drift, opacity, overcoupling, standing collapse, and lossy translation in the very integrity surfaces IEL depends on. |
| *Semantic Legitimacy Before Context* | Requires candidate context to earn admissibility before becoming operative. |
| *Reasoning by Way of Receipts* | Makes reasoning and decision transitions reconstructable while denying that receipts create truth or independence. |
| *A Formal Theory of Work Custody* | Separates responsibility to advance or repair an integrity work item from authority to approve its effects. |
| *Legitimacy Without Self-Ratification* | Prevents a subject-controlled evidence route from being sufficient for the highest standing of that subject's own integrity claims. |

The author-confirmed terminology lineage is `CCF -> CMB -> GMB`; **Governed Meaning Base (GMB)** is current. CCF and CMB remain historical names in exact source language and lineage explanations.

Current UGK/FGA/IEL/CGP skill material is used here only as a compressed orientation candidate. Its reported r165 pedagogical checks and implementation concepts are not treated as a canonical release, global completion, or source-independent proof. Generated constitutional projection, human implementation navigation, conformance results, runtime authority, and release certification remain distinct.

## 12. Realization Funnel

| Stage | IEL content |
| --- | --- |
| Possibility | Integrity can become an inherited environmental condition rather than a collection of local checks. |
| Specification | Define effects, profiles, contexts, verification dimensions, terminal outcomes, corruption dispositions, receipts, atomic boundaries, remainders, and amendment rules. |
| CM1 | Enumerate admissible enforcement designs, including centralized and distributed mediators, fail-closed and bounded-degradation profiles, exact atomic and compensating patterns, and explicit non-action. |
| CM2 | Prefer designs that minimize authority, expose scope, preserve exact commitments, distinguish corrupt from missing, classify partial effects, and remain testable under adversarial conditions. |
| Instance Configuration | Select protected effects, policies, epochs, identities, trust domains, verification profiles, corruption rules, timeouts, recovery paths, storage and transport adapters, and audit surfaces. |
| Implementation Realization | Implement guards, context resolution, mutation planning, effect mediation, receipts, classified remainders, adversarial harnesses, and operator explanations. |
| Evidence | Bind exact code or artifacts, profiles, fixtures, environments, commands, outputs, negative courts, effect observations, receipts, limitations, and independent review. |
| Revision | Amend profiles and mechanisms under governed procedures while preserving prior contexts, receipts, migrations, defeaters, and affected claims. |

This paper chiefly specifies the IEL and its CM1 design family. The proposed components are CM2 candidates. A particular UGK module, verifier, gate, archive, or deployment is an Instance Configuration or Implementation Realization whose standing cannot be inherited from this paper.

## The Decision-to-Effect Enforcement Contract

The completed P1 corpus places the Integrity Enforcement Layer (IEL) at a precise boundary: IEL is the **decision-to-effect enforcement contract** that prevents a governance result from acquiring protected effects unless its exact subject, authority, evidence, and integrity conditions are satisfied. It is not the governance constitution, semantic substrate, evidence base, or whole executable kernel.

- **Adjacent work:** *Universal Governance Kernel*  
  **Supplies:** Candidate executable governance primitives, receipts, and certification surfaces.  
  **IEL boundary:** UGK can implement an IEL profile; implementation identity and proof remain separate.

- **Adjacent work:** *Agentic Interface Surfaces*  
  **Supplies:** What agents see, which effects they may attempt, what evidence they receive, and how progress is recognized.  
  **IEL boundary:** AIS describes the interaction and recognition surface; IEL enforces protected transitions behind it.

- **Adjacent work:** *Legitimacy Without Self-Ratification*  
  **Supplies:** Independence and authority limits on evidence and standing.  
  **IEL boundary:** IEL must not accept a subject-controlled path as sufficient for its strongest claim.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Who holds the scoped duty to investigate, repair, or advance an integrity item.  
  **IEL boundary:** Custody does not grant authority to change policy or admit effects.

- **Adjacent work:** GMB and universal GSM  
  **Supplies:** Meaning, sources, claims, standing, conflicts, and revisions.  
  **IEL boundary:** IEL protects selected mutations and effects; it does not determine semantic truth.

The enforcement envelope is:

$$
\begin{aligned}
I= (&subject, request, profile, authority, evidence, context, \\
&effect, receipt, remainder)
\end{aligned}.
$$

An IEL disposition is one of `PERMIT`, `REFUSE`, `DEFER`, `INDETERMINATE`,  
or `PARTIAL_EFFECT`. `PARTIAL_EFFECT` is essential when an external action cannot be made exactly atomic: the system must classify what occurred, what remains, what compensation is possible, and which claims are invalidated. A refusal is correct only relative to a declared profile and evidence set; refusal volume is not itself integrity.

Corpus integration adds a non-circularity requirement. The profile, verifier, context resolver, evidence source, and effect observer must expose their independence and shared dependencies. If they are all derived from the subject being checked, the IEL may provide a useful consistency check but cannot claim independent integrity enforcement.

The universal GSM can type `REQUESTS_EFFECT`, `CHECKED_UNDER_PROFILE`, `AUTHORIZED_BY`,  
`EVIDENCED_BY`, `PERMITTED_BY`, `REFUSED_BY`, `LEFT_REMAINDER`, `COMPENSATED_BY`,  
and `INVALIDATES_CLAIM`. These relations preserve the difference between a decision, an attempted effect, an observed effect, and recognition.

This integration establishes four editorial commitments: adopt decision-to-effect enforcement contract as IEL's corpus role; adopt the enforcement envelope and `PARTIAL_EFFECT`; require explicit independence/shared-dependency disclosure; and decide which UGK realization, if any, will become the first bounded IEL case study through a separate evidence gate.

## Authority-Audited Enforcement with Protected Constraint Channels and Learning Boundaries

The fixed-seed comparison with Authority Laundering Theory, Governance as Compilation, the Suppression Paradox, and governed continual training positions IEL as a causal enforcement boundary whose own rule and update paths remain reviewable:

$$
\begin{aligned}
I^*= (&proposal, compiled\_decision, normative\_warrant, \\
&capability, protected\_constraint, permit, refuse, defer, \\
&appeal, effect, receipt, learning\_boundary, \\
&requalification)
\end{aligned}.
$$

Authority Laundering analysis audits the rule, delegation, and dependent claim entering IEL. Governance as Compilation supplies a typed decision-to-effect contract, including declared loss and remainder. The Suppression Paradox requires a protected channel through which a material blocker can cause refusal or deferment without exposing its full payload to every actor.

Governed continual training cannot silently learn around a refusal, weaken a verifier, reinterpret an authority boundary, or promote a new enforcement rule. Any update that changes IEL behavior requires separately authorized admission, evaluation, rollback, and requalification. Prior receipts are evidence of prior behavior, not authority for the new behavior.

The universal GSM can type   
`ENFORCES_COMPILED_DECISION`, `AUDITS_RULE_AUTHORITY`,  
`CARRIES_PROTECTED_BLOCKER`, `SUPPORTS_REFUSE_DEFER_APPEAL`, `EMITS_EFFECT_RECEIPT`,  
`BLOCKS_SELF_AUTHORIZING_UPDATE`, and   
`REQUIRES_POST_UPDATE_REQUALIFICATION`.

This randomized review establishes four editorial commitments: adopt the authority-audited IEL object; bind compiled decisions to mediated effects; create protected refusal, deferment, and appeal channels; and impose an explicit learning boundary with requalification after material change.

## Integrity Enforcement as a Bounded Mutation Service

Eleven retained downstream uses apply IEL to AFS profiles, authority laundering, cyber-physical effects, compilation, continual training, Jnana, enforcement mechanics, suppression testing, APD containment, structural warrant, and comparative software evidence. They support a reusable refusal-centric mutation service, not a universal trusted layer.

$$
\begin{aligned}
I^*= (&subject, generation, operation, policy, authority, \\
&preconditions, verification\_profile, read\_set, \\
&write\_set, transaction, effect\_boundary, witnesses, \\
&result, recovery, remainder, expiry, successor)
\end{aligned}.
$$

Validation before mutation requires binding the exact subject and generation, not merely a path or label. Read-only operations must declare and test hidden writes through caches, timestamps, indexes, telemetry, learning, and external services. Corruption, absence, staleness, ambiguity, and unsupported format are distinct outcomes. Atomicity is bounded by the transaction and cannot hide irreversible external effects.

IEL itself requires authority, update, bypass, liveness, denial-of-service, self-verification, recovery, and protected-constraint audits. Verification profiles must state dimensions, oracle, trusted base, negative vectors, and claim ceiling. A successful refusal or commit proves only the bound operation under that profile.

The universal GSM can type   
`SUBMITS_INTEGRITY_MUTATION`, `VALIDATES_BEFORE_MUTATION`,  
`DISTINGUISHES_CORRUPTION_FROM_ABSENCE`, `DETECTS_HIDDEN_READ_WRITE`,  
`COMMITS_BOUNDED_TRANSACTION`, `CLASSIFIES_EFFECT_REMAINDER`, and `AUDITS_IEL_BYPASS`.

This review establishes four editorial commitments: adopt the bounded mutation-service record; require exact subject generation and hidden-write tests; type corruption, absence, staleness, and ambiguity separately; and subject IEL itself to authority, bypass, liveness, recovery, and independent-verification review.

## 13. Failure Modes, Counterexamples, and Limits

1. **Unbounded refusal.** A system can refuse everything and still be useless or illegitimate. Refusal correctness requires liveness, proportionality, and governed appeal or amendment.
2. **Incomplete validation.**   
`All refusal conditions` is meaningful only relative to a declared profile; unknown conditions cannot be claimed evaluated.
3. **Corruption overreaction.** Corruption should fail closed for the affected boundary, but universal process halt may destroy availability or recovery. Quarantine, bounded degradation, repair, and stop are profile decisions.
4. **Verification-ladder collapse.** LINKAGE, BODY, CONTEXT, IDENTITY, and QUORUM are not necessarily one total order. `FULLY_VERIFIED` is meaningful only as all dimensions required by a named profile.
5. **Read-path ambiguity.** Observation must not mutate authoritative state. Isolated caches, access telemetry, or health counters may be permissible only when they cannot change the observed decision, standing, evidence, or history and are explicitly outside the protected state.
6. **Distributed atomicity limit.** Exact all-or-nothing mutation may be unavailable across external systems. The IEL must classify remainders and compensations rather than claim atomicity it cannot prove.
7. **Verifier compromise.** Centralizing enforcement creates a high-value failure point. The verifier boundary, implementation, configuration, and supply chain require their own evidence and cannot self-ratify.
8. **Context reconstruction failure.** Historical verification can be impossible when policy, epoch, identity, or meaning commitments were not retained exactly.
9. **Refusal-code theater.** A typed refusal without sufficient evidence, correct scope, and observed non-effect is not trustworthy refusal.
10. **Bypass and confused deputy.** An application can route around the IEL or induce a mediator to exercise broader authority than the requester holds.
11. **Availability attack.** Expensive checks, indefinite defer, or adversarial inputs can turn the integrity layer into denial of governance.
12. **Semantic drift.** Shared enums and profiles can preserve stable bytes while their meanings change; GMB, migration, and Three Hash commitments remain necessary.

The IEL architecture has not been established here as complete, minimal, universally applicable, or empirically superior to reference monitors, policy-enforcement points, transaction systems, provenance systems, or domain-specific designs. Those are research and implementation questions.

## 14. Future Directions

Several extensions become possible:

* formal verification of IEL primitives,
* cryptographic context sealing,
* adversarial conformance certification,
* machine-verifiable refusal proofs,
* constitutional inheritance across distributed systems,
* integrity-preserving agent architectures,
* governance-aware execution environments.

The IEL is intended as a foundation rather than a complete solution.

---

## Refusal-Centric Integrity Without a Monolithic Oracle

### Public orientation

The Integrity Enforcement Layer centralizes hostile-boundary validation, scoped verification, corruption handling, contextual reconstruction, and atomic mutation beneath governance meaning. It is designed to refuse malformed or untrusted transitions deterministically. Centralization also creates a high-value trust, liveness, and denial-of-service boundary.

### Adversarial tests

1. **Verifier-compromise attack.** The layer that validates integrity is itself modified or misconfigured. Boot trust, measured identity, independent witness, and recovery are required.
2. **Profile-confusion attack.** An artifact passes one verification dimension and is treated as globally valid. Every result binds a named profile and claim ceiling.
3. **TOCTOU attack.** Subject state changes between verification and use. Atomic binding or revalidation is necessary at the effect boundary.
4. **Partial-mutation attack.** A failure occurs after some state changed. Prepare, commit, rollback, compensation, and residual state must be explicit.
5. **Context-reconstruction attack.** Missing context is rebuilt from stale, forged, or unauthorized sources. Reconstruction requires lineage and conflict handling.
6. **Replay-and-downgrade attack.** Older valid state or weaker policy is reintroduced. Freshness, monotonic constraints, and authorized rollback need separate rules.
7. **Refusal-denial-of-service.** Malformed or expensive inputs consume the verifier or block lawful work. Resource and liveness budgets are part of integrity.
8. **Monolithic-oracle attack.** IEL results are treated as semantic truth or governance authority. The layer verifies declared properties; it does not decide policy or meaning.

### Claim and evidence ceiling

The paper specifies a bounded mutation and verification service with named capabilities and profiles. It does not establish formal correctness, complete corruption detection, atomicity across all external effects, security against every adversary, or production performance.

Implementation claims require exact code, build, dependencies, threat model, mutation suite, concurrency and crash tests, recovery evidence, and independent reproduction. External security and systems comparisons require resolvable sources. No external research was added in this pass.

### Reader-facing consequence

The public benefit is a place where malformed, stale, corrupted, or wrongly scoped transitions can be refused before they rewrite governed state, while every refusal explains which property failed and which lawful recovery remains.

## 15. Publication Standing and Evidence Limits

### 15.1 Current Standing

This candidate is a developed architectural proposal and corpus integration. It does not provide an exact implementation identity, source package, threat model, test corpus, adversarial court, performance result, deployment history, or independently reproduced verification package. The five laws, components, maturity profile, and verification dimensions therefore have design standing only unless tied to separately admitted evidence.

The source bibliography is retained but was not externally revalidated during this closed-corpus pass. Citations, genealogy, comparative claims, and the relation to reference monitors, capability systems, policy engines, transactions, provenance, and constitutional systems require primary-source verification for a future evidence-qualified revision readiness.

PDF rendering remains deferred until textual and semantic saturation. The authorized baseline is ordinary Pandoc mode:

```text
pandoc INPUT.md -o OUTPUT.pdf
```

### 15.3 Corpus Sources

- Adam Ableman, *The Integrity Enforcement Layer*. Exact author source SHA-256  
`FF7A53289D84BAEC82B89E55A9DA6088A8FD194399ABB6A57BFB739F3008B46B`.
- Adam Ableman, *Semantic Debt*. Exact reviewed source SHA-256  
`36BAE578CF1926981488982AB8C406E0EACB662E25E8B5F18F187A6E53AF933F`.
- Adam Ableman, *Reasoning by Way of Receipts*. Exact reviewed source SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`.
- Adam Ableman, *A Formal Theory of Work Custody*. Exact reviewed source SHA-256  
`49C38F60B95E107F8B3D864ACAFB4C49067A146C807E5248307DE7B009AD4696`.
- Adam Ableman, *Semantic Legitimacy Before Context*. Exact reviewed source SHA-256  
`1E9058F212FCB00E42E35E927DF2E7F830BC9C9499AAFF469FE65FF8AE137B68`.
- Adam Ableman, *The Three Hash Rule*. Zenodo, 2026. DOI:   
  `10.5281/zenodo.20788617`; exact reviewed source SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.
- Governed Meaning Base terminology ruling: `CCF -> CMB -> GMB`, with GMB current. This establishes terminology lineage only.
- UGK/FGA/IEL/CGP Context Skill, r165 pedagogical-surface authoring-lane candidate. Used for stack-boundary orientation only; not treated as canonical law or release proof.

The primitives, formal contract, stack map, GMB relation, realization funnel, limits, claim ceilings, and author-decision surface are AI-prepared editorial synthesis explicitly distinguished from the original author material. They grant no author, publication, canonical, implementation, conformance, certification, deployment, or effect standing.

## 16. Conclusion

Most software seeks successful execution.

Integrity systems seek trustworthy refusal.

This distinction creates a category of architectural problems that cannot be solved through isolated validation checks or subsystem-specific hardening.

The Integrity Enforcement Layer is proposed as a constitutional enforcement substrate that centralizes adversarial validation, verification semantics, corruption handling, contextual reconstruction, and atomic mutation.

Its purpose is not to determine what governance means.

Its purpose is to ensure that governance claims remain trustworthy.

A governance system should not be trusted merely because it succeeds.

It should also demonstrate that it refuses correctly, classifies uncertainty and partial effects honestly, preserves liveness, and does not exceed its evidence or authority.

The Integrity Enforcement Layer exists to make that refusal systematic.

---

## Appendix A: Integrity Capability Profile

Level 0 -- Executes

The system performs requested actions.

Level 1 -- Refuses

The system rejects invalid requests.

Level 2 -- Explains

Refusals are attributable and understandable.

Level 3 -- Verifies

Claims are supported by evidence.

Level 4 -- Preserves

Historical truth survives corruption and failure.

Level 5 -- Governs

Integrity becomes inheritable.

---

## Appendix B: Verification Dimensions and Named Profile

| Level          | Meaning                                       |
| -------------- | --------------------------------------------- |
| LINKAGE        | Structural chain continuity verified          |
| BODY           | Data commitments verified                     |
| CONTEXT        | Historical context reconstructed and verified |
| IDENTITY       | Authority and identity bindings verified      |
| QUORUM         | Collective agreement verified                 |
| FULLY_VERIFIED(profile) | All dimensions required by the named profile established for the scoped subject |

---

## Appendix C: Proposed Constitutional Invariants

1. Validation Before Mutation
2. Corruption Is Not Absence
3. Verification Must State Its Scope
4. Read Paths Must Not Mutate
5. Multi-Step Mutations Must Be Atomic

These invariants form the constitutional basis of the Integrity Enforcement Layer.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that most software systems are optimized for successful execution. Its nearest external comparison fields are security, governance, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E2]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E3]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

**[E4]** Robert N. M. Watson, Simon W. Moore, Peter Sewell, and Peter G. Neumann. *An Introduction to CHERI*. University of Cambridge Technical Report UCAM-CL-TR-941, 2019. DOI: 10.48456/tr-941. [cl.cam.ac.uk source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-941.html) **Relationship:** Adjacent capability architecture demonstrating unforgeable hardware authority and compartmentalization.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

### Ableman corpus

**[A1]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Constitutional Syscalls*. Ableman Corpus current edition; work identity `PAPER.PUB.18737229`;  
source SHA-256  
`5F14356180812262778F8574C292F4F6B560993042E5358B02EAB9CF0F7DE14C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governance Engineering*. Ableman Corpus current edition; work identity `PAPER.PUB.18749870`;  
source SHA-256  
`372169F315D192733856B1F4A3F1038BBC73F57CF3ED9ACABAE72B965A69C8D0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The following bibliography is retained from the author source and was not externally revalidated during this closed-corpus pass.

Anderson, J. P. *Computer Security Technology Planning Study*.

Lampson, B. *Protection*.

Saltzer, J. H., and Schroeder, M. D. *The Protection of Information in Computer Systems*.

Miller, M. S. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*.

Weitzner, D. et al. *Transparent Accountable Data Mining*.

The Update Framework (TUF).

in-toto Supply Chain Framework.

Object Capability Model.

Reference Monitor Concept.

Policy Enforcement Point / Policy Decision Point Architectures.

Transactional Atomicity and Write-Ahead Logging Systems.

Constitutional Governance Theory.

Governance Kernel (UGK) Development Notes and Adversarial Review Findings.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Semantic Debt.* Zenodo, 2026. doi:10.5281/zenodo.21111666

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848354](https://doi.org/10.5281/zenodo.23848354)
