# Reasoning by Way of Receipts

## From Admissible Proposal to Verified State Transition

### A receipt is not the justification itself. It is the durable structure that makes bounded justification inspectable.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern computational systems record extensive traces while rarely binding a
state transition to the authority, jurisdiction, criteria, evidence, and
verification under which that transition acquires standing. Logs describe
events, traces reconstruct flows, and metrics summarize outcomes, but these
artifacts do not by themselves establish whether an action was admissible,
whether its reported effect occurred, or what downstream reliance the result
may legitimately support.

This paper introduces **reasoning by way of receipts**: a model of governed
computation in which an epistemic or operational proposal may enter canonical
state only through a typed, lineage-bearing receipt protocol. A receipt is not
itself truth, proof, or complete explanation. It is an inspectable commitment
linking a proposal, governing specification, jurisdiction, authority context,
decision, observed effect, evidence, verification result, predecessor state,
and permitted standing. We distinguish decision, refusal, effect,
verification, promotion, and revision receipts and specify the conditions
under which they may compose into a justification graph.

The resulting model separates physical execution from constitutional
recognition. An effect may occur without acquiring governed standing, while
refusal, hold, escalation, and non-decision remain valid receipted outcomes.
This distinction connects semantic ingress, epistemic promotion,
reality-touching capability, governed memory, and institutional action within
a common transition grammar.

The contribution is not the claim that receipts eliminate interpretation.
It is that receipts can bind the materials, authority, and limits of
interpretation closely enough for justification to become reconstructable,
contestable, and revisable rather than merely narrated after the fact.

## 1. The Missing Layer in Computation

Contemporary systems are deeply instrumented yet epistemically shallow. They
can often answer:

* What happened?
* When did it happen?
* Which component emitted the event?
* How often did a measured outcome occur?

They often cannot answer, in a structurally binding way:

* Why was this transition admitted?
* Which jurisdiction and authority governed it?
* Which specification and policy version were applied?
* What evidence supports the claimed effect?
* What exactly was verified?
* What standing may later systems assign to the result?
* How may the decision be contested, revoked, or revised?

This gap is not simply a shortage of logging. Logs, traces, metrics, audit
records, and event streams can all be useful evidence, but their existence does
not establish a complete relation among authority, admissibility, effect,
evidence, verification, and standing.

Empirical analysis across real software systems reinforces this distinction.
Receipt surfaces vary from absent traces through optional logs to mandatory
operational ledgers; governance is often stronger at system boundaries than in
system interiors; and layered decision mechanisms frequently fail to expose a
unified account of why an outcome occurred [1]. Observability is therefore not
receipt completeness, and receipt existence is not yet justification.

The missing layer is a transition protocol that makes the movement from
proposal to recognized state explicit, typed, and inspectable.

## 2. Scope and Nonclaims

Reasoning by way of receipts concerns **externalized epistemic and operational
transitions**. It governs proposals that may alter canonical state, memory,
authority, persistent artifacts, or the world outside the reasoning process.
It does not claim control over private mental activity, latent model state, or
every intermediate token generated inside a model.

The framework makes five bounded claims:

1. A governed transition can bind its decision basis and evidentiary
   obligations at the time the transition is evaluated and realized.
2. Typed receipts can make the resulting transition independently
   reconstructable within a declared scope.
3. Refusal and non-decision can be represented as successful governance
   outcomes rather than missing data.
4. Receipt graphs can support compositional reasoning when their edges,
   standing rules, and jurisdictional interpretation are explicit.
5. Canonical state can be prevented from advancing when required receipts or
   verification obligations are absent, provided the receipt protocol is
   non-bypassable.

The framework does not claim that:

* a receipt is automatically true;
* a signature establishes legitimate authority;
* evidence establishes more than its declared verification scope;
* a valid receipt makes the underlying policy just;
* a receipt chain is automatically a valid argument;
* every physical effect can be reversed;
* institutional transparency follows automatically from record production;
* narrative explanation becomes unnecessary;
* receipt production alone creates consciousness, understanding, or
  intelligence.

These nonclaims are load-bearing. Without them, a receipt can become another
symbol through which unearned authority is laundered.

## 3. Primitive Distinctions

The framework begins by separating concepts that conventional systems often
collapse.

- **Primitive:** Proposal  
  **Function:** Names an intended transition  
  **What it does not establish by itself:** Permission, execution, or success

- **Primitive:** Jurisdiction  
  **Function:** Selects the governing domain  
  **What it does not establish by itself:** Justice or correctness of its rules

- **Primitive:** Authority  
  **Function:** Enables a binding decision within scope  
  **What it does not establish by itself:** Evidence that an effect occurred

- **Primitive:** Admissibility  
  **Function:** Evaluates whether a proposal may proceed  
  **What it does not establish by itself:** Successful execution

- **Primitive:** Effect  
  **Function:** A reality-touching or state-changing occurrence  
  **What it does not establish by itself:** Its own meaning or legitimacy

- **Primitive:** Receipt  
  **Function:** Persistently binds a governed event to inspectable structure  
  **What it does not establish by itself:** Truth, proof completeness, or sufficient evidence

- **Primitive:** Evidence  
  **Function:** Supports or refutes a claim through a declared relation  
  **What it does not establish by itself:** Authority to bind the claim

- **Primitive:** Verification  
  **Function:** Checks a claim or artifact against criteria and returns a typed result  
  **What it does not establish by itself:** Universal truth beyond the check

- **Primitive:** Standing  
  **Function:** States what bounded reliance is permitted  
  **What it does not establish by itself:** Identity, authorship, or correctness in every context

- **Primitive:** Lineage  
  **Function:** Connects the event to predecessor states and dependencies  
  **What it does not establish by itself:** Validity of every predecessor

- **Primitive:** Refusal  
  **Function:** Produces a typed negative outcome  
  **What it does not establish by itself:** System error or permanent prohibition

- **Primitive:** Revision  
  **Function:** Reopens or changes prior structure through a governed path  
  **What it does not establish by itself:** Erasure of history

The distinction between **receipt** and **evidence** is especially important. A
receipt records that a governed evaluation, attempt, observation, or promotion
was represented as occurring. Evidence supports an inference about the world
or system. A receipt may bind evidence, but the receipt does not automatically
make that evidence sufficient.

Likewise, verification is an operation with a declared claim boundary. A
cryptographic hash may verify byte identity. It does not verify semantic
accuracy. A test may verify behavior under a fixture. It does not verify a
universal guarantee. A signed decision may verify attribution. It does not
verify legitimate jurisdiction.

## 4. The Governed Transition Lifecycle

### 4.1 State, proposal, and governing context

Let:

* $\Sigma_t$ be the canonical state at time $t$;
* $p$ be a proposed transition;
* $J$ be the applicable jurisdiction;
* $C_v$ be the governing constitution, specification, or policy at version
  $v$;
* $A$ be the admissibility operator;
* $\Omega_p$ be the evidentiary obligations attached to $p$.

The admissibility decision is:

$$
\begin{aligned}
d = A(p, \Sigma_t, J, C_v) \quad\text{where}\quad d \in \{&\mathrm{ALLOW}, \mathrm{REFUSE}, \mathrm{HOLD}, \\
&\mathrm{ESCALATE}\}
\end{aligned}.
$$

The decision produces a decision receipt $r_d$. The receipt binds the proposal,
jurisdiction, authority basis, governing version, evaluated criteria, decision,
and predecessor state. It does not yet claim that an allowed effect succeeded.

If $d$ is REFUSE, HOLD, or ESCALATE, canonical state does not advance:

$$
\Sigma_{t+1} = \Sigma_t.
$$

The negative or suspended outcome remains visible through a typed receipt.

### 4.2 Effect attempt and observation

If $d$ is ALLOW, an implementation may attempt the effect:

$$
x = E(p, \Sigma_t).
$$

The effect attempt occurs at a declared execution boundary. Observation
produces an effect record $o$:

$$
o = O(x).
$$

An effect receipt $r_e$ binds the attempted operation, execution boundary,
reported outcome, and evidence-bearing observations. It must distinguish at
least:

* completed effect;
* refused or blocked effect;
* failed effect;
* indeterminate effect;
* effect attempted without adequate evidence;
* no effect attempted.

This separation matters because physical execution and epistemic recognition
can diverge. An external backend may change the world and then fail to return a
conforming receipt. The governed system must not pretend that nothing physical
happened. It records an **orphaned effect condition**: the effect cannot advance
canonical state as a verified result, but remediation may be required because
an unrecognized physical consequence may exist.

### 4.3 Verification and promotion

The evidence is evaluated against the proposal's obligations:

$$
q = V(o, \Omega_p, J, C_v)
\quad\text{where}\quad
q \in \{\mathrm{PASS},\mathrm{FAIL},\mathrm{INDETERMINATE}\}.
$$

The verification receipt $r_v$ binds the evidence, verifier, criteria, result,
and claim boundary. A promotion operator then determines whether the transition
may alter canonical state:

$$
m = P(p, d, q, r_d, r_e, r_v)
\quad\text{where}\quad
m \in \{\mathrm{COMMIT},\mathrm{REFUSE},\mathrm{HOLD}\}.
$$

Canonical state advances only when promotion is committed:

$$
\Sigma_{t+1} =
\begin{cases}
\Delta(\Sigma_t, p, o), & \text{if } m = \mathrm{COMMIT},\\
\Sigma_t, & \text{otherwise.}
\end{cases}
$$

The promotion receipt $r_p$ records the standing acquired by the result. A
successful effect does not self-promote into explanation, precedent, memory,
or authority. Promotion is a separate governed act.

### 4.4 The transition invariant

The central invariant is:

> No proposal acquires canonical standing merely because it was generated,
> allowed, executed, observed, or signed. Canonical standing changes only
> through a declared promotion operation whose authority, evidence, and claim
> boundary are receipted.

This is stronger than logging and narrower than truth certification. It governs
what the system may rely upon.

### 4.5 Refinement of Justificatory Computation

The corpus ontology defines **Justificatory Computation** as a regime in which
execution and justification are the same act. The present account preserves
the intended non-separability while refining its temporal interpretation.
Admission, effect, observation, verification, and promotion need not occur at
one instant or inside one artifact. They form one governed transaction only
when their boundaries and dependencies are explicitly bound.

Accordingly, *intrinsic justification* means that an implementation cannot
obtain canonical standing while bypassing the required decision, evidence, and
verification structure. It does not mean that execution alone proves its own
validity. This refinement retains the distinction between descriptive and
justificatory regimes while preventing an executed effect from serving as its
own warrant.

## 5. A Family of Receipts

The word *receipt* names a family of typed artifacts rather than a single
undifferentiated record.

### 5.1 Decision receipt

A decision receipt records which proposal was evaluated, which law applied,
who or what had evaluation authority, what criteria were evaluated, and whether
the proposal was allowed, refused, held, or escalated.

### 5.2 Refusal receipt

A refusal receipt is a specialized decision receipt that records the failed or
undefined predicates, preserves state, and states whether reconsideration,
additional evidence, or escalation is permitted. Refusal is evidence that the
gate participated; it is not evidence that the gate was correct.

### 5.3 Effect receipt

An effect receipt records the attempted interaction with an implementation or
external substrate. It binds the capability used, target, execution boundary,
observable result, and evidence returned by that boundary [3].

### 5.4 Verification receipt

A verification receipt records a check and its exact proof boundary. It says
which claim was tested, against which evidence and criteria, under which tool
or evaluator version, and with which result.

### 5.5 Promotion receipt

A promotion receipt records the transition from transient or provisional
material to a state with greater downstream standing. This is the receipt type
most directly connected to semantic compilation [4], governed coding [7], and
checkpoint promotion in governed training [8].

### 5.6 Revision receipt

A revision receipt records amendment, supersession, revocation, correction, or
reopening. It preserves the prior receipt and states which dependencies must be
re-evaluated. Revision changes standing without rewriting history.

### 5.7 Transaction envelope

A single implementation may package these receipts into one transaction
envelope:

$$
R_t = \{r_d, r_e, r_v, r_p, r_a\},
$$

where $r_a$ is present only when amendment or revision occurs. Packaging does
not erase the logical distinctions among the contained receipt roles.

A minimal receipt envelope should bind:

```text
receipt_id
receipt_type
proposal_id
operation_type
target
jurisdiction_id
authority_reference
policy_id
policy_version
policy_hash
prestate_reference
decision_or_outcome
effect_summary
evidence_references
verification_result
verification_scope
standing_effect
predecessor_receipts
time_or_sequence
integrity_material
disclosure_policy
challenge_status
```

Different domains may add fields, but omission of a field must not silently
expand what the receipt is allowed to establish.

## 6. Reasoning by Way of Receipts

Reasoning by way of receipts is not merely the accumulation of execution
records. It is the controlled movement of claims and actions across typed
transition boundaries.

> **Reasoning by way of receipts** is a model of computation in which proposals,
> decisions, effects, evidence, verification, promotion, and revision remain
> explicitly related through lineage-bearing artifacts whose standing is
> bounded and inspectable.

The receipt structure forms a directed graph:

$$
G_R = (V_R, E_R),
$$

where vertices are receipts or governed semantic objects and edges are typed
relations. Useful relation types include:

```text
AUTHORIZES
DEPENDS_ON
OBSERVES
SUPPORTS
VERIFIES
REFUSES
PROMOTES
SUPERSEDES
REVOKES
CONTESTS
```

A chain of hashes establishes linkage. It does not establish a valid argument.
A receipt graph supports a bounded justification only when:

1. each receipt satisfies its declared schema;
2. integrity and predecessor bindings verify;
3. jurisdiction and authority are resolvable;
4. evidence is admissible for the claim being made;
5. the verification operation establishes the advertised proof level;
6. the receiving jurisdiction recognizes imported evidence without importing
   authority by default;
7. no critical dependency has been revoked or superseded without a declared
   resolution path;
8. the conclusion does not exceed the standing of its dependencies.

Under these conditions, later reasoning can depend on earlier governed states
without collapsing into untraceable narrative reconstruction. Narrative
remains useful for explanation and pedagogy, but it becomes answerable to a
structured warrant surface.

## 7. The Realization Funnel

Receipt-bound computation becomes clearer when projected through the complete
realization funnel.

| Stage | Receipt-oriented question |
| --- | --- |
| Possibility | Which transitions, interpretations, and outcomes are conceivable? |
| Specification | What constitutes a valid proposal, receipt, claim, and governed transition? |
| CM1 | Which configurations satisfy the minimum specification, including harmful, weak, or degenerate ones? |
| CM2 | Which admissible configurations are preferable under security, legitimacy, privacy, evidentiary, and usability criteria? |
| Instance Configuration | Which jurisdiction, policy version, authority roots, schemas, disclosure rules, and verification obligations govern this instance? |
| Implementation Realization | Which gates, adapters, verifiers, stores, and effect mechanisms enact the selected configuration? |
| Evidence | What did the implementation demonstrably do, and what do the resulting receipts establish? |
| Revision | What evidence or contest changes the specification, configuration, implementation, or standing of prior results? |

This projection prevents a minimum technically admissible receipt mechanism
from being mistaken for a desirable one. A system may satisfy CM1 by producing
receipts while still centralizing authority, leaking private information, or
making contestation impossible. CM2 makes those preference and legitimacy
questions explicit. Instance Configuration then fixes the selected policies
for a particular deployment.

## 8. A Closed Epistemic Membrane

The receipt protocol occupies the middle of a larger corpus architecture:

```text
raw signal
  -> governed semantic tokenization
  -> declared semantic state
  -> governed semantic compilation
  -> proposed epistemic or operational transition
  -> receipted admissibility and promotion
  -> receipt-bound capability
  -> external effect
  -> evidence and verification
  -> governed memory and revision
```

Governed Semantic Tokens regulate what may enter as authority-bearing meaning
[5]. Governed Semantic Compilation regulates which generated continuations may
persist or acquire authority [4]. The receipt protocol binds the decision,
effect, evidence, and promotion. Receipt-Bound Capabilities regulate
reality-touching egress by requiring evidence from the execution boundary [3].
The Governed Knowledge Loop preserves lineage and governs subsequent mutation
[9].

The resulting membrane is symmetric:

* raw signals do not become meaning by default;
* generated meaning does not become state by default;
* authorized proposals do not become successful effects by default;
* reported effects do not become verified claims by default;
* verified claims do not acquire unlimited standing by default;
* established standing does not become permanent by default.

Each boundary requires its own governed transition.

## 9. Receipts as a Substrate for Epistemic Situational Awareness

Receipts provide an evidentiary substrate for Epistemic Situational Awareness
(ESA), but receipt accumulation is not sufficient to create ESA.

ESA governs whether reasoning may continue, escalate, bind, reuse, or lawfully
terminate [6]. To support that control property, a system must be able to ask:

1. What epistemic mode is active?
2. Which realization or epistemic layer contains the artifact?
3. Which evidence and receipt lineage support it?
4. What standing would reuse create?
5. Which continuations are admissible under the active jurisdiction?
6. Has Blocked, Undecidable, refusal, or lawful termination been reached?

Receipts answer only part of this inquiry. They supply inspectable history,
authority references, verification boundaries, and standing transitions. ESA
uses those materials to shape the action horizon.

This yields a disciplined relationship:

> Receipts make epistemic position inspectable; ESA makes that position
> operationally consequential.

## 10. Worked Example I: An Agentic Code Change

Consider an agent asked to repair a failing parser.

### 10.1 Proposal

The agent proposes patch $p_{47}$. The proposal is a preview, not a commit. It
binds:

* repository and base revision;
* files allowed to change;
* claimed purpose;
* expected behavior;
* known uncertainty;
* required tests;
* rollback target.

### 10.2 Instance configuration

The active instance configuration specifies:

* the repository head;
* applicable coding and security policies;
* the permitted filesystem scope;
* test and static-analysis obligations;
* who may authorize broader changes;
* which results may be promoted into memory or root-cause explanation.

### 10.3 Admission and execution

The gate checks identity, scope, forbidden paths, dependency conditions, and
test availability. If admitted, a decision receipt is emitted. A bounded
capability authorizes application of the patch. The effect receipt records the
actual changed bytes and resulting worktree state.

### 10.4 Verification

Tests, linters, and targeted behavioral checks execute. Their outputs become
evidence. The verification receipt states only what those checks establish.

If the tests pass, the system may promote the patch to a commit. It may record:

```text
behavior restored under declared tests
```

It may not automatically record:

```text
root cause proven
all regressions excluded
parser universally correct
```

Those are stronger claims requiring different evidence and authority. This is
the separation between successful implementation and justified explanation
developed in Governed Coding and Debugging [7].

### 10.5 Refusal and revision

If tests are unavailable, the result may be HOLD or INDETERMINATE rather than a
fabricated success. If the patch touches an unauthorized file, the transition
is refused. If later evidence reveals a regression, a revision receipt can
revoke the patch's prior standing without erasing its history.

## 11. Worked Example II: A Governed Training Update

In a Governed Training Regime, the optimizer proposes a parameter update
$\Delta_t$ rather than exercising ambient authority over model state [8].

The update-level gate evaluates:

* training jurisdiction and dataset identity;
* protected parameter regions;
* update magnitude and invariant constraints;
* safety and regression checks;
* active training-law version.

The gate returns ALLOW, REFUSE, HOLD, or ESCALATE and produces a decision
receipt. If allowed, the update is applied to a candidate state. Evaluation
artifacts then provide evidence about the candidate checkpoint.

A checkpoint promotion receipt may be issued only when the required evidence
pack verifies. The receipt establishes that the checkpoint satisfied the
declared promotion ritual. It does not establish that the model is universally
safe, aligned, truthful, or robust.

The resulting chain makes parameter evolution reconstructable:

```text
training specification
  -> optimizer proposal
  -> admissibility decision
  -> candidate update
  -> evaluation evidence
  -> verification
  -> checkpoint promotion or refusal
```

This is reasoning by way of receipts at the level of model-state evolution.

## 12. Institutional Generalization

The same grammar can operate in institutions, but the mapping is not automatic.

| Computational construct | Institutional counterpart |
| --- | --- |
| Proposal | Motion, petition, application, recommendation |
| Jurisdiction | Legal, organizational, or procedural domain |
| Authority | Office, mandate, delegation, or charter |
| Admissibility criteria | Applicable rules and evidentiary requirements |
| Decision receipt | Formal decision and recorded basis |
| Effect receipt | Evidence that the ordered action was carried out |
| Promotion | Entry into precedent, policy, entitlement, or institutional memory |
| Revision | Appeal, amendment, revocation, correction, or rehearing |

Fractal Governance Architecture supplies the cross-scale qualification: the
transition form may recur across operational, institutional, protocol, and
constitutional levels, while the applicable authority, policy, evidence, and
interpretation remain jurisdiction-specific [10]. A receipt issued in one
jurisdiction may carry evidence into another, but authority does not transfer
by default.

Institutional receipts can support:

* reconstruction of decision paths;
* attribution of authority;
* detection of bypass or missing participation;
* contestation and appeal;
* selective public transparency.

They do not automatically produce justice, legitimacy, or public disclosure.
Receipts may contain private or dangerous information. A mature system must
separate the integrity commitment from its disclosure projection, allowing
independent verification without universal exposure.

## 13. Corpus-Wide Integration: Durable Transition-Accountability Substrate

Across the completed P1 corpus, Reasoning by Way of Receipts supplies the **durable transition-accountability substrate connecting proposals, decisions, refusals, effects, observations, verifications, promotions, and revisions**. It does not claim that a receipt is a proof, witness, warrant, effect, truth, authority, or standing decision.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed evidence carriers and evaluation envelopes.  
  **Receipt boundary:** A receipt may reference or contain witnesses; a witness can exist without being a transition receipt.

- **Adjacent work:** *Warrant by Structure*  
  **Supplies:** The evaluated relation among claim, authority path, evidence, effects, and standing.  
  **Receipt boundary:** Receipts are inputs to warrant assessment, not the assessment itself.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Responsibility, transfer, return, and terminal disposition for exact work.  
  **Receipt boundary:** Custody changes should be receipted; a receipt does not create custody without protocol satisfaction.

- **Adjacent work:** *From CI/CD to ACG: From Tests to Courts in Agentic Software Development*  
  **Supplies:** Constitutional development, adjudication, effect, evidence, and revision lifecycle.  
  **Receipt boundary:** Receipts are the durable records spanning that process, not the court or governor.

- **Adjacent work:** *Epistemic Lineage Engine*  
  **Supplies:** Source, transformation, decision, and revision lineage for claims.  
  **Receipt boundary:** Receipt graphs supply events and bindings; epistemic lineage interprets their knowledge relations.

The transaction envelope can be stated as:

$$
\begin{aligned}
T= (&prestate, proposal, context, authority, decision, \\
&effect\_attempt, observations, verification, promotion, \\
&revision, poststate, remainder)
\end{aligned}.
$$

Each field may have its own receipt and evidence ceiling. A decision receipt records what was admitted or refused under a context. An effect receipt records an attempt and bounded observations. A verification receipt records a property evaluation. A promotion receipt records a standing change. A revision receipt records why a prior posture changed. Hash binding protects exact record identity; it does not establish accuracy, completeness, independence, or legitimacy.

Receipt closure requires that every protected transition terminate in a declared disposition and that orphaned or uncertain effects remain visible. Reconstruction is possible only to the extent that state identity, ordering, nondeterministic inputs, external observations, schemas, and missing events are covered. Replay of records is not necessarily re-execution of effects.

The universal GSM can type   
`PROPOSED_IN_TRANSACTION`, `DECIDED_BY_RECEIPT`,  
`REFUSED_BY_RECEIPT`, `EFFECT_ATTEMPT_RECORDED_BY`, `OBSERVED_BY_WITNESS`,  
`VERIFIED_BY_RECEIPT`, `PROMOTED_BY_RECEIPT`, `REVISED_BY_RECEIPT`,  
`LEAVES_ORPHANED_EFFECT`, `RECONSTRUCTABLE_FROM_RECEIPTS`,  
and   
`HAS_RECEIPT_CLAIM_CEILING`. These relations make receipt reasoning composable without overclaim.

This integration establishes four editorial commitments: adopt durable transition-accountability substrate as the official corpus role; adopt the transaction envelope; formalize the witness/receipt/warrant/standing separation; and require orphaned-effect, reconstruction, and claim-ceiling semantics in every receipt profile.

## 13A. P3 Randomized Cross-Neighborhood Review: Semantic-Change Receipt Chain

The fixed-seed comparison with Governance Coverage Gaps, Ontology Laundering, GCNL, and GTK adds a portable chain for semantic change:

$$
\begin{aligned}
R= (&proposal\_receipt, resolution\_receipt, \\
&admission\_receipt, transition\_receipt, \\
&propagation\_receipt, effect\_receipt, review\_receipt)
\end{aligned}.
$$

GCNL can supply the exact human-authored proposal and residual meaning. GTK resolution binds the occurrence, candidate senses, alternatives, policy, and selected lexical identity. Admission decides whether the proposed semantic change may bind for the named purpose. Transition and propagation receipts preserve predecessor, successor, affected dependents, coverage, and failures.

Ontology Laundering classification occurs only after those records are evaluated with authority, burden, alternatives, effects, counterevidence, and intent-neutral categories. The receipts do not establish laundering, legitimacy, semantic equivalence, or truth. They make the inference inspectable and revisable.

Governance Coverage Gaps limits every completion claim. A full-looking receipt chain can cover only discovered semantic and capability paths; new caches, prompts, projections, or consumers reopen the propagation verdict. Absence receipts must name the observation boundary and unavailable regions.

The universal GSM can type   
`RECEIPTS_SEMANTIC_PROPOSAL`, `RECEIPTS_GTK_RESOLUTION`,  
`RECEIPTS_PURPOSE_ADMISSION`, `RECEIPTS_IDENTITY_TRANSITION`,  
`RECEIPTS_PROPAGATION_ATTEMPT`, `RECEIPTS_OBSERVED_SEMANTIC_EFFECT`,  
and   
`REOPENS_RECEIPT_INFERENCE`.

This randomized review establishes four editorial commitments: adopt the semantic-change receipt chain; preserve proposal residual and GTK alternatives; keep laundering and legitimacy as evaluated conclusions rather than receipt fields; and bind propagation completeness to a reopenable coverage boundary.

## The Receipt Kernel Under Its Downstream Uses

The complete P3 field uses *Reasoning by Way of Receipts* across work custody, context admission, learning, evidence loops, project lineage, adversarial audit, artifact profiles, transformation substrates, split authority, and boundary accountability. Those dependents reveal a stable kernel and several prohibited promotions:

$$
\begin{aligned}
R^*= (&subject, predecessor, proposal, authority, gate, \\
&decision, effect\_attempt, observation, verification, \\
&standing, successor, remainder, revision, profile)
\end{aligned}.
$$

Work-custody receipts identify handoff and disposition without proving competent completion. Context receipts reconstruct admission and displacement without making active context true. Learning receipts preserve promotion, retirement, and residual influence without validating the learned object. Evidence-loop and audit receipts bind exact subjects and findings without certifying coverage or independence.

Project-lineage and cold-boot uses require receipts to bind exact artifact generations, environments, dependencies, and replay classes. AFS and Jnana II uses require receipt profiles whose schemas, planes, and effect boundaries are explicit. Split-authority and boundary-accountability uses require the receipt issuer, evaluator, effect authority, observer, and affected subject to remain distinguishable.

The reverse-dependency result is therefore not that every governed system needs one universal receipt schema. It is that downstream profiles should refine a common transition-accountability kernel while declaring consequence class, evidence path, authority topology, privacy, expiry, reconstruction scope, and claim ceiling. A receipt family that cannot express `UNKNOWN`,  
`CONFLICT`, `PARTIAL_EFFECT`, `STALE`, `UNOBSERVED`,  
or `REMAINDER` will encourage false closure.

The universal GSM can type   
`PROFILES_RECEIPT_FOR_DOMAIN`,  
`BINDS_EXACT_TRANSITION_SUBJECT`, `RECONSTRUCTS_WITHOUT_PROVING`, `RETAINS_PARTIAL_EFFECT`,  
`EXPIRES_RECEIPT_STANDING`, `PROPAGATES_REVISION_TO_DEPENDENT`,  
and   
`REFUSES_UNIVERSAL_SCHEMA_COLLAPSE`.

This reverse-dependency review establishes four editorial commitments: retain the transition-accountability kernel; make receipt profiles explicit rather than universalizing one schema; require consequence, authority, evidence-path, privacy, expiry, and remainder fields where material; and add typed incomplete outcomes across downstream profiles.

## 13. Failure Modes and Adversarial Conditions

### 13.1 Boundary theater

A system can emit receipts without evaluating the claimed predicates. The
receipt then proves that a record was produced, not that the gate participated.
Countermeasures include evaluator attestations, independently replayable
decision traces, challenge tests, and meta-receipts covering gate execution.

### 13.2 Forged or misleading receipts

Integrity controls can detect modification and attribution failure, but a
properly signed receipt may still contain false claims. Independent evidence
and verification remain necessary.

### 13.3 Receipt-proof collapse

A receipt may be treated as proof merely because it exists. The cure is an
explicit verification scope and a rule that downstream claims cannot exceed
the proof level actually established.

### 13.4 Authority laundering

A valid signer, prior approval, or familiar institution may be treated as
authority outside its jurisdiction. Receipts must bind authority scope and the
receiving system must evaluate that scope independently.

### 13.5 Cross-jurisdiction semantic drift

Two domains may interpret the same field differently. Cross-domain reuse
requires an explicit bridge that preserves meaning and admissibility or emits a
failure witness [10].

### 13.6 Orphaned effects

An effect may occur physically while evidence production fails. Treating the
event as nonexistent can compound harm. The system must preserve canonical
uncertainty, emit an incident or fault receipt where possible, and initiate a
domain-specific reconciliation procedure.

### 13.7 Receipt flooding

Excessive receipt production can make verification unusable. Receipts require
typed aggregation, retention policy, semantic indexing, and selective
projection without breaking exact lineage.

### 13.8 Governance capture

Explicit governance can still encode unjust rules. Receipts make the governing
structure visible; they do not make it good. Amendment, contestation, plural
oversight, and bounded authority remain necessary.

### 13.9 Irreversible or non-observable effects

Some domains cannot provide complete observation, deterministic replay, or
rollback. The receipt must expose that limitation rather than representing a
partial observation as complete verification.

## 14. Evaluation and Falsification Program

The proposed phase shift from descriptive to justificatory computation should
be tested rather than assumed.

### 14.1 Reconstruction test

Give independent evaluators the same receipt bundle, governing specification,
and verifier implementation. Measure whether they reconstruct the same
decision, effect classification, verification result, and standing change.

Failure condition: materially divergent reconstruction under identical declared
inputs.

### 14.2 Bypass test

Attempt to advance canonical state through every effect surface without a valid
promotion receipt.

Failure condition: canonical state advances through an unreceipted path.

### 14.3 Proof-boundary test

Present valid receipts whose evidence establishes a narrow claim and ask whether
the system accepts a stronger claim.

Failure condition: receipt existence or signature is accepted as proof beyond
the declared verification scope.

### 14.4 Refusal completeness test

Exercise invalid, incomplete, ambiguous, and unauthorized proposals.

Failure condition: negative outcomes disappear as errors, silence, or
unstructured exceptions rather than producing typed refusal, hold, escalation,
or incident records.

### 14.5 Cross-jurisdiction test

Submit a receipt valid in one jurisdiction to another jurisdiction with
different authority and evidentiary rules.

Failure condition: authority transfers merely because the foreign receipt is
cryptographically valid.

### 14.6 Comparative utility test

Compare conventional logs and traces with receipt bundles for incident
reconstruction, policy audit, appeal, and state replay.

Failure condition: the receipt protocol produces no reproducible improvement
in reconstructability, contestability, or bounded claim evaluation while adding
material operational cost.

### 14.7 Revision propagation test

Revoke or supersede a critical predecessor receipt and inspect dependent
claims.

Failure condition: downstream standing remains unchanged without an explicit
independence determination or re-verification.

## 15. Implications

### 15.1 Computing

Receipt-bound transitions make authority, evidence, and standing inspectable at
the point where state changes. Debugging becomes not only trace inspection but
evaluation of what each transition was allowed to establish. Replay can target
the governed decision and verification logic rather than blindly re-executing
the external world.

### 15.2 Artificial intelligence

Agentic systems can be allowed broad proposal capability while retaining narrow
effect and promotion authority. The model proposes; externalized governance
determines what may become state. Refusal, hold, escalation, and non-decision
become ordinary outcomes rather than signs that intelligence has failed.

### 15.3 Knowledge systems

Receipts can serve as structural memory for governed knowledge mutation. They
preserve how a claim entered the corpus, which evidence supported it, what
standing it acquired, and how later evidence revised it. The Governed Knowledge
Loop turns this memory into a recursive process of analysis, crystallization,
frontier detection, mutation, and renewed analysis [9].

### 15.4 Institutions

Institutions gain a basis for reconstructable decision-making and contestable
authority. The benefit is not automatic transparency but the ability to produce
appropriate internal and public projections from the same integrity-preserving
decision lineage.

## Receipts Make Justification Inspectable Without Becoming the Justification

### Public orientation

Reasoning by Way of Receipts binds a proposed state transition to its governing specification, jurisdiction, authority context, decision, attempted and observed effects, evidence, verification, predecessor, permitted standing, and revision lineage. Decision, refusal, effect, verification, promotion, and revision are distinct receipts. Their composition can make bounded justification reconstructable and contestable; it cannot remove interpretation or prove the world matches the record.

### Adversarial tests

1. **Receipt-proof attack.** A signed, hashed, complete, or internally consistent receipt is treated as truth, proof, legitimacy, correctness, or successful effect.
2. **Boundary-theater attack.** The receipted path is rigorous while alternate tools, humans, networks, caches, credentials, physical processes, or institutional routes bypass it.
3. **Authority-laundering attack.** An unauthorized or defective authority assertion propagates through valid receipt composition and gains apparent standing.
4. **Observation-effect attack.** A command response, log, self-report, or proxy is recorded as the intended real-world effect without independent observation.
5. **Cross-jurisdiction attack.** Receipts compose across incompatible purposes, laws, definitions, evidence standards, or authority domains.
6. **Semantic-drift attack.** Schemas and terms retain identifiers while their interpretation changes, making historical composition appear valid.
7. **Flood-and-opacity attack.** Receipt volume, nesting, selective disclosure, or cryptographic detail makes review practically impossible and hides decisive omissions.
8. **Revision-orphan attack.** Revocation, correction, expiry, or predecessor defects fail to propagate to dependent claims, states, decisions, and projections.

### Claim and evidence ceiling

The paper specifies a typed transition-accountability substrate and falsification program. It does not establish truth, sufficient justification, legitimate authority, complete evidence, actual effect, complete mediation, privacy, security, scalability, institutional validity, or implementation conformance. Hash and signature checks prove only their exact cryptographic claims under declared assumptions.

Validation requires exact schemas and canonicalization, key and authority governance, independent effect observation, bypass and forgery courts, cross-jurisdiction refusal, semantic-version tests, selective-disclosure and privacy review, dependency propagation, human reconstruction studies, baselines, and current external research. No deployment or external research was performed in this pass.

### Reader-facing consequence

The public benefit is not more logging. It is the ability to reconstruct why a state transition was proposed, who could decide it, what actually happened, what evidence was checked, what standing followed, and what must change when any link later fails.

## 16. Conclusion

Receipts do not transform computation merely by adding records. They transform
the conditions under which state may legitimately change.

In reasoning by way of receipts:

* proposals do not become decisions by implication;
* decisions do not become effects by assertion;
* effects do not become evidence by occurrence alone;
* evidence does not become proof without verification;
* verification does not become unlimited standing;
* standing does not become permanent without revision paths.

The decisive shift is therefore not from event logs to larger event logs. It is
from implicit promotion to governed transition.

A receipt is not the justification itself. It is the durable structure that
makes a bounded justification inspectable, composable, contestable, and
revisable.

Once that structure becomes non-bypassable, computation can move beyond merely
describing what happened. It can state what was proposed, what was permitted,
what occurred, what was verified, what may now be relied upon, and exactly where
its warrant ends.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Appendix A. Minimal Receipt Profiles

### A.1 Decision receipt

```yaml
receipt_type: decision
proposal_id: p-47
jurisdiction_id: repository-maintenance
authority_reference: maintainer-policy-v3
policy_hash: sha256:...
prestate_reference: commit:...
decision: ALLOW
criteria_results:
  scope: PASS
  identity: PASS
  dependencies: PASS
predecessor_receipts: []
standing_effect: effect-attempt-authorized
```

### A.2 Verification receipt

```yaml
receipt_type: verification
proposal_id: p-47
effect_receipt: r-effect-47
verifier: parser-regression-suite-v5
evidence_references:
  - test-report:...
verification_result: PASS
verification_scope:
  - declared-parser-regression-cases
nonclaims:
  - universal-correctness
  - root-cause-proof
standing_effect: eligible-for-promotion-review
```

### A.3 Revision receipt

```yaml
receipt_type: revision
subject_receipt: r-promotion-47
revision_action: SUPERSEDE
basis:
  - regression-report:...
dependent_recheck_required: true
standing_effect: prior-promotion-suspended
```

These examples are illustrative profiles, not canonical schemas. Their purpose
is to expose the distinctions that an implementation must preserve.

## Corpus-Wide Reference Positioning

This paper argues that modern computational systems record extensive traces while rarely binding a state transition to the authority, jurisdiction, criteria, evidence, and verification under which that transition acquires standing. Its nearest external comparison fields are provenance, governance, observation. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Telemetry can be complete at the instrumented boundary while omitting the causal variable, real-world effect, or authority question that matters. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E2]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E3]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

**[E4]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

### Ableman corpus

**[A1]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *A Formal Theory of Work Custody*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-C8F2F9BF38C45E29`;  
source SHA-256  
`A80657E21BA277ADF1C229A2AAE221963B97A62EA2AF3EBC36434A916A8EEA44`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Governance Witnesses*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-9E8DA0EFE860DE5D`;  
source SHA-256  
`8BF8C3646040F6E1F5222A8AA92C1106AA1F841E8A2C65402F468C83D59D06E5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

#### Ableman Corpus references

[1] Adam Ableman, *What Software Systems Actually Receipt, Govern, and
Hide: Findings from a 17-System Constitutional Corpus*, Ableman Corpus edition, 2026.

[2] Adam Ableman, *Constitutional Computation*, Zenodo, 2026.
https://doi.org/10.5281/zenodo.20624488

[3] Adam Ableman, *Receipt-Bound Capabilities: Membrane Tokens for
Governed Interaction with Reality*, Zenodo, 2026.
https://doi.org/10.5281/zenodo.18601631

[4] Adam Ableman, *Governed Semantic Compilation: Lawful Continuation,
Refusal Semantics, and Epistemic Promotion in Large Language Models*, Zenodo,
2026. https://doi.org/10.5281/zenodo.18453681

[5] Adam Ableman, *Governed Semantic Tokens: Tokenization as an
Admissibility Boundary*, Zenodo, 2026.
https://doi.org/10.5281/zenodo.18469507

[6] Adam Ableman, *Epistemic Situational Awareness (ESA): A
Phenomenological Control Property of Governed Reasoning Systems*, Zenodo, 2026.
https://doi.org/10.5281/zenodo.18121270

[7] Adam Ableman, *Governed Coding and Debugging: A Claim-Governance
Grammar for Human-AI Agentic Workflows*, Zenodo, 2026.
https://doi.org/10.5281/zenodo.18115533

[8] Adam Ableman, *Governed Training Regimes: Admissible Parameter
Transformation Under Law*, Zenodo, 2026.
https://doi.org/10.5281/zenodo.18623302

[9] Adam Ableman, *The Governed Knowledge Loop: A Constitutional
Bootstrapping Architecture for Semantic Computing Infrastructure*, Ableman Corpus edition, 2026.

[10] Adam Ableman, *Fractal Governance Architecture*, Zenodo, 2026.
https://doi.org/10.5281/zenodo.20754189

[11] Adam Ableman, *Constitutional Binding Theory: Governed Anchor
Resolution as a Universal Pattern in Semantic Systems*, Ableman Corpus edition, 2026.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23845806](https://doi.org/10.5281/zenodo.23845806)
