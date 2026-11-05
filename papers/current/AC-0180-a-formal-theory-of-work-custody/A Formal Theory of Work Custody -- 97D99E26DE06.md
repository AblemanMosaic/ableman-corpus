# A Formal Theory of Work Custody

## Invariants, State Machines, and Governed Collaboration

### Operational custody identifies the current duty to advance work; it does not itself confer authority, capability, ownership, or accountability.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

This paper proposes **Work Custody** as a first-class collaboration relation identifying which eligible participant currently holds the bounded operational duty to advance a particular version and scope of a work object. Custody answers "who has the next move?" without collapsing ownership, assignment, authority, accountability, capability, or standing.

The model replaces an informal linear status list with a generation-bound state machine. Offers, acceptances, transfers, releases, revocations, expirations, completion, blockage, and recovery are typed transitions. A normal transfer is a handshake: the predecessor remains primary until the successor accepts and the transfer is promoted. Forced revocation or failure may create an explicit unassigned or recovery-required state; the system preserves accountability for the discontinuity rather than pretending custody never had a gap.

Custody is queryable only relative to exact work identity, version, scope, valid time, transaction time, jurisdiction, and authorization. Receipts bind declarations and observations but do not by themselves prove complete mediation or actual effect. Human and machine participants may share transition syntax while differing in capability, persistence, consent, legal personality, and moral accountability.

The resulting specification supports agent orchestration, cold-boot continuity, governed project memory, and cross-node handoff. It remains a candidate architecture: implementation conformance, organizational benefit, complexity reduction, and comparative performance require exact configurations and empirical evidence.

---

## 1. Motivation

Most collaborative failures are not failures of planning.

They are failures of operational localization.

Organizations frequently know:

* who owns a project,
* who is accountable,
* what workflow stage exists,
* what the deadline is.

Yet they cannot answer:

> Who can move this forward **right now**?

This question motivates Work Custody.

---

## 2. Primitive Definitions

Let:

* **P** be the set of participants.
* **W** be the set of work objects.
* **T** be time.

A custody relation is

$$
\operatorname{Custody} \subseteq P \times W \times G \times T \times S
$$

where $G$ is custody generation and $S$ is custody scope. A tuple $(p,w,g,t,s)$ means that participant $p$ is the recognized custodian for work object $w$, generation $g$, interval $t$, and bounded scope $s$. Work identity includes the exact artifact or logical version-family relation needed to prevent custody from silently moving to a different object.

Unlike ownership,

```text
Owns(p,w)
```

custody is expected to change repeatedly.

---

### 2.1 Custody Record and State

For a work object $w$, define the current custody record as

$$
K_w = (g,C_w,q,\ell,v_t,t_t,a,e,b),
$$

where $g$ is monotonically increasing custody generation; $C_w$ is the set of active custody roles; $q$ is lifecycle state; $\ell$ is lease or liveness condition; $v_t$ is valid time; $t_t$ is transaction time; $a$ is authority basis; $e$ is evidence and receipts; and $b$ is the blocker or waiting set. A default configuration permits at most one **primary** custodian while allowing explicit supporting, reviewing, or observing roles.

Custody is recognized only when the work identity, scope, participant eligibility, acceptance or authorized forced assignment, authority basis, and current generation all match. A stale acceptance for generation $g-1$ cannot acquire generation $g$ custody.

### 2.2 Orthogonal Relations

For participant $p$ and work $w$:

$$
\begin{aligned}
&\operatorname{Custody}(p,w) \not \\
&\Rightarrow \operatorname{Authority}(p,w) \\
&\lor \operatorname{Capability}(p,w) \\
&\lor \operatorname{Ownership}(p,w) \\
&\lor \operatorname{Accountability}(p,w)
\end{aligned}.
$$

Nor do those relations imply custody. A custodian may be blocked by a dependency, lack authority for a consequential effect, or lack the evidence needed to proceed. Standing, custody, capability, authority, and sufficiency are separately evaluated gates.

## 3. Custody Is Independent

Work Custody is intentionally orthogonal to other collaboration relations.

For any work object:

```text
Owner
```

answers

> Who permanently possesses this object?

```text
Authority
```

answers

> Who may authorize changes?

```text
Accountability
```

answers

> Who ultimately answers for outcomes?

```text
Custody
```

answers

> Who presently possesses the obligation to advance this work?

None of these imply one another.

---

## 4. Custody State Machine

The following lifecycle separates events from durable states:

```text
UNASSIGNED
  -> OFFER_PENDING
  -> ACTIVE
  -> TRANSFER_PENDING
  -> ACTIVE (new generation and successor)
  -> COMPLETED | CANCELLED
```

Additional explicit states include `BLOCKED`, `SUSPENDED`, `EXPIRED`, `REVOKED`,  
`ABANDONED`,  
and `RECOVERY_REQUIRED`. `DECLINED` is normally the result of an offer event and returns the work to its prior state; it is not active custody. A failed or forced handoff may lawfully produce `UNASSIGNED` or `RECOVERY_REQUIRED`,  
but never an unexplained disappearance.

A normal transfer from $p_1$ to $p_2$ is a handshake:

$$
\begin{aligned}
&\operatorname{OfferTransfer}(p_1,p_2,w,g) \\
&\rightarrow \operatorname{Accept}(p_2,w,g+1) \\
&\rightarrow \operatorname{PromoteTransfer}(w,g+1)
\end{aligned}.
$$

Until promotion, $p_1$ remains the primary custodian unless an eligible authority explicitly suspends or revokes that custody. The transfer event records the exact work head, pending mutations, blockers, next action, context-capsule reference, authority, and expiry. Every specified transition requires a decision record; effect observation, verification, and promotion remain separate.

---

## 5. Constitutional Invariants

### C1 -- Recognition

Custody has constitutional standing only when recorded against an exact work identity, generation, scope, and eligible participant. Informal expectation may exist socially but is not treated as system state.

### C2 -- Acceptance or Explicit Forced Assignment

An ordinary offer does not confer custody. The successor accepts the exact handoff. Exceptional forced assignment, revocation, or emergency recovery requires separately eligible authority, reason, scope, and reviewability; it is not disguised as consent.

### C3 -- One Primary by Default

Each work generation has at most one primary custodian unless the Instance Configuration declares a joint-custody protocol. Joint custody assigns roles, concurrency and conflict rules, decision rights, and completion conditions rather than creating an unstructured set of equally responsible actors.

### C4 -- Explicit Discontinuity

Custody may disappear because work is completed, cancelled, abandoned, revoked, expired, or lost through failure. The invariant is not uninterrupted possession; it is that every discontinuity becomes a typed state with reason, authority, evidence, and recovery consequences.

### C5 -- Transfer Continuity

In an ordinary transfer, predecessor custody persists until successor acceptance is promoted. If continuation is unsafe or impossible, the system records an explicit gap or recovery state rather than asserting a successful handoff.

### C6 -- Authorized Queryability

Authorized participants can determine current primary custody, generation, scope, validity interval, blockers, and confidence without reconstructing chat history. Privacy, need-to-know, and jurisdiction may restrict who can query which details.

### C7 -- No Authority Escalation

Custody does not confer permission to edit, execute, publish, spend, disclose, delegate, or complete. Every effect remains bounded by independent authority and capability checks.

### C8 -- Capability and Sufficiency

Active custody requires either demonstrated capability and sufficient prerequisites or an explicit blocked/debt state. Assigning work to an agent that cannot retain context, access required evidence, or perform the next action does not create functional continuity.

### C9 -- Work and Version Binding

Every offer, acceptance, transfer, mutation, and completion identifies the exact work object, logical version relation, expected head, and allowed mutation surface. Similar titles or filenames do not transfer custody.

### C10 -- Lease and Liveness

Custody configurations define heartbeat, lease, expiry, and recovery rules appropriate to the participant type. Silence is evidence only under the declared liveness protocol; it is not automatic abandonment.

### C11 -- Bitemporal and Receipted History

The ledger distinguishes when custody is valid in the modeled world from when the system learned or recorded it. Receipts bind decisions and observations; they do not prove wall-clock truth, complete mediation, or effect occurrence without additional evidence.

### C12 -- Minimal Disclosure

Custody records expose only the context required for coordination. Context snapshots are referenced by governed, access-controlled commitments rather than copied wholesale into every receipt.

---

## 6. Custody Algebra

Custody introduces several primitive operators.

Assignment

```text
Assign(p,w)
```

Offer

```text
Offer(p,w)
```

Acceptance

```text
Accept(p,w)
```

Transfer

```text
Transfer(p1,p2,w)
```

Release

```text
Release(p,w)
```

Completion

```text
Complete(w)
```

Waiting

```text
WaitOn(w,x)
```

Escalation

```text
Escalate(w,r)
```

These compose into custody histories whose determinism depends on the declared time, retry, and conflict-resolution model.

---

### 6.1 Operator Contracts

Each operator is a partial function over state rather than an unconditional command. For example,

$$
\operatorname{Accept}(p,w,g) : K_w \rightharpoonup K'_w
$$

is defined only when an unexpired offer for participant $p$, work $w$, and successor generation $g$ exists; participant eligibility and declared acceptance evidence are valid; the work head has not changed incompatibly; and no higher-priority revocation or completion is in force. Equivalent preconditions govern assignment, release, completion, wait, and escalation. Undefined operations refuse or defer with a typed reason.

Operators are idempotent relative to a unique proposal identifier, or else retry can create duplicate transfers. Concurrent proposals require optimistic version checks or an equivalent serialization rule. A history is deterministic only relative to a declared conflict-resolution and time model; receipt order alone does not make distributed execution deterministic.

## 7. Waiting Graphs

Custody alone does not explain stalls.

Introduce

```text
WAITING_ON
```

forming a dependency graph.

Example:

```text
Research waits on -> Legal Review
Legal Review waits on -> Customer Response
```

Cycles become machine detectable.

Idle custody becomes measurable.

---

## 8. Human-Agent Uniformity

Participants may be humans, organizations, AI agents, deterministic components, workflow engines, or constitutional adjudicators. They can share a custody transition grammar, but they are not normatively interchangeable. Humans and organizations may bear legal or moral accountability that software cannot; agents may lack durable memory, consent, independent authority, or persistence across sessions. Each participant type therefore declares capability, identity continuity, liveness, delegation, supervision, and accountability boundaries.

---

## 9. Custody Receipts

Every transition emits a receipt containing

* predecessor,
* successor,
* work identity,
* timestamp,
* reason,
* authority basis,
* acceptance evidence,
* contextual snapshot.

This creates an auditable declared custody ledger only when every in-scope transition is mediated by the receipting boundary. Completeness requires capability-surface coverage and external checks for unreceipted effects; a self-consistent receipt chain alone cannot prove that no transition was omitted.

---

## 10. Runtime Queries

The custody model makes authorized, scoped runtime questions directly evaluable against recorded state.

Examples include:

```text
Who has the ball?

Who had it yesterday?

How many transfers occurred?

Who holds the oldest custody?

Which work has no custodian?

Which custodian exceeds workload limits?

Which waiting dependency dominates latency?

Where are abandoned custody objects?

What percentage of transfers required escalation?
```

These can become database queries over declared state, while disputes, missing mediation, stale records, and effect verification may still require investigation.

---

## 11. Complexity Reduction

Traditional collaboration reconstructs custody from

* chat,
* tickets,
* meetings,
* email,
* memory,
* assumptions.

This reconstruction grows approximately with organizational complexity.

Explicit custody can reduce some reconstruction to direct evaluation of governed state, while adding recording, reconciliation, privacy, and recovery costs. Whether total coordination overhead falls is an empirical question whose answer depends on update discipline, interface quality, organizational scale, exception rate, and the consequences of stale state.

---

## 12. Constitutional Consequences

Work Custody becomes another constitutional primitive alongside

* identity,
* authority,
* standing,
* provenance,
* effect,
* receipt.

Its invariants become machine-verifiable.

Illegal custody states become detectable rather than inferred.

---

### 12.1 Agent Orchestration, GMB, and Cold-Boot Continuity

Work Custody supplies the live-control relation needed by agent orchestration. A cold-boot replacement agent does not inherit vanished memory merely by receiving a task identifier. A resumable custody capsule binds the work identity and head, custody generation, current and proposed custodians, authorized next action, blockers and waiting edges, relevant GMB semantic entries, exact source commitments, authority and capability limits, open debts, required evidence, expiry, and return or transfer protocol.

The **Governed Meaning Base (GMB)** stores or references current semantic and project state under the author-confirmed CCF -> CMB -> GMB lineage. **Semantic Project Lineage** preserves reconstructible project heads and projections. **Governed Context and Memory** controls what state enters an agent invocation. **Reasoning by Way of Receipts** preserves intermediate epistemic transitions. The **Crystal Network** can transport custody offers and evidence across independently governed nodes, but the receiver re-evaluates identity, authority, capability, scope, and acceptance locally.

Custody therefore connects semantic continuity to operational next action without equating memory, context, or network carriage with legitimate possession of the work.

### 12.2 Realization Funnel

- **Stage:** Possibility  
  **Work-custody responsibility:** Explore exclusive, joint, leased, delegated, replicated, human, agent, and federated custody models, including unsafe ones.  
  **Standing here:** Open design space.

- **Stage:** Specification  
  **Work-custody responsibility:** Define work identity, roles, states, transitions, generations, time, authority, capability, receipts, gaps, and recovery.  
  **Standing here:** Candidate specification.

- **Stage:** CM1  
  **Work-custody responsibility:** Enumerate admissible custody configurations, including high-overhead, brittle, coercive, privacy-invasive, or low-value cases.  
  **Standing here:** Partially enumerated.

- **Stage:** CM2  
  **Work-custody responsibility:** Prefer clear, minimally disclosed, reversible, liveness-aware, non-escalating, recoverable, and human-sovereignty-preserving designs.  
  **Standing here:** Preference criteria proposed.

- **Stage:** Instance Configuration  
  **Work-custody responsibility:** Select schema, clocks, leases, roles, joint-custody rules, authorization, privacy, retries, conflict resolution, quorum, and recovery.  
  **Standing here:** Not fixed here.

- **Stage:** Implementation Realization  
  **Work-custody responsibility:** Implement custody storage, mediation, queries, capsules, notifications, and cross-node transfer.  
  **Standing here:** Not established here.

- **Stage:** Evidence  
  **Work-custody responsibility:** Test races, retries, stale acceptance, dead agents, partitions, forced revocation, overload, privacy, bypass, and cold boot.  
  **Standing here:** Required and incomplete.

- **Stage:** Revision  
  **Work-custody responsibility:** Amend custody policy while preserving predecessor histories, pending transfers, dependent work, and contested events.  
  **Standing here:** Required direction.

### 12.3 Failure and Counterevidence Conditions

The proposal is weakened if participants ignore or cannot maintain the ledger; if stale custody becomes more misleading than informal coordination; if default exclusivity creates bottlenecks; if joint custody diffuses responsibility; if acceptance is coerced or spoofed; if custody becomes authority laundering; if agents lose context while retaining active status; if partitions create split-brain custodians; if waiting cycles are legitimate but treated as errors; if privacy costs exceed coordination gains; or if ordinary workflow assignment plus version control provides equivalent outcomes at lower cost.

## 13. Future Directions

Open research includes:

* distributed custody across federated organizations;
* probabilistic custody forecasting;
* custody-aware scheduling;
* automated transfer optimization;
* semantic negotiation of custody;
* custody visualization;
* empirical comparison with assignment-only collaboration systems;
* custody-based reduction in meeting frequency.

---

## Custody as the Next-Move Duty Primitive

The completed P1 corpus gives Work Custody a precise place: it is the **next-move duty primitive** for an exact work identity, generation, and scope. It should not duplicate orchestration, project lineage, context memory, receipt reasoning, or coordination theory.

- **Adjacent work:** *Who Has the Ball?*  
  **Supplies:** Pedagogical and operational account of active responsibility.  
  **Custody boundary:** Functions as the accessible projection; this paper carries the state-machine theory.

- **Adjacent work:** *Governed Semantic Project Lineage*  
  **Supplies:** Work identity, versions, branches, successors, and reconstructable heads.  
  **Custody boundary:** Custody attaches to a lineage subject but does not define that subject's identity.

- **Adjacent work:** *Operational ESA*  
  **Supplies:** What an agent knows about task, context, capability, uncertainty, and stopping.  
  **Custody boundary:** Awareness of custody is not custody, and custody does not imply capability.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Bounded records of offers, acceptance, refusal, transfer, and completion reasoning.  
  **Custody boundary:** A receipt records the claim and transition; it does not prove complete mediation or actual advancement.

- **Adjacent work:** *Agentic Interface Surfaces*  
  **Supplies:** Recognition and refusal conditions at action boundaries.  
  **Custody boundary:** AIS can prevent recognition without custody evidence; it does not decide who ought to receive custody.

- **Adjacent work:** *Optional Coordinator*  
  **Supplies:** Tests whether coordination functions can be internalized.  
  **Custody boundary:** Custody can be distributed without eliminating arbitration, resource allocation, or authority hierarchy.

The shared handoff unit is:

$$
H=(W,g,s,c_{from},c_{to},O,E,K,R),
$$

where $W$ is logical work identity, $g$ generation, $s$ bounded scope, $c_{from}$ and $c_{to}$ custody roles, $O$ open obligations, $E$ evidence and uncertainty, $K$ the minimum context capsule, and $R$ the receipt and recovery contract. A context capsule without current obligations and custody state is memory transfer, not a work handoff. A custody transfer without adequate context can be formally valid yet operationally unusable.

Corpus integration adds a **three-surface separation**:

1. **custody surface:** who has the recognized next-move duty;
2. **authority surface:** what effects that participant may authorize or perform;
3. **recognition surface:** what evidence permits the workflow to count progress or transfer as complete.

These surfaces may be held by different parties. This is essential in human-agent collaboration: an agent may hold custody to investigate, lack authority to deploy, and need human recognition to close the work.

The universal GSM can type `HAS_CUSTODY_OF`, `OFFERED_TO`, `ACCEPTED_BY`, `TRANSFERRED_TO`,  
`RELEASED_BY`, `REVOKED_FROM`, `BLOCKED_ON`, `AUTHORIZED_FOR`, `EVIDENCED_BY`,  
and `RECOGNIZED_BY`. Time, generation, scope, and standing belong on every custody edge.

This integration establishes four editorial commitments: adopt next-move duty primitive as the official corpus role; treat *Who Has the Ball?* as the pedagogical projection; adopt the handoff unit including obligations, evidence, context, and recovery; and adopt the custody/authority/recognition surface separation.

## Custody Across Knowledge Mutation and Fragmented Development

The fixed-seed comparison with Governance Incentive Engineering, the Governed Knowledge Loop, ACG, and Semantic Fragmentation extends custody from a single handoff to a typed responsibility chain:

$$
\begin{aligned}
H^*= (&work, generation, scope, next\_move, custodian, \\
&authority, capability, recognition, dependencies, \\
&remainder, recovery, successor)
\end{aligned}.
$$

GIE interventions require custody for investigation, affected-party response, measurement review, remediation, and reconsideration. GKL proposals require custody across analysis, counterexample handling, author review, mutation, and rollback. In both cases the next-move duty remains separate from authority to change the governed state.

ACG adds development-specific recognition surfaces. A test result, court verdict, gate disposition, effect receipt, and release standing can place different next moves on different custodians. Completion at one surface must not silently release custody for unresolved effects, evidence, or publication claims.

Semantic fragmentation can obscure the actual work subject, generation, decision class, or responsible surface. A custody record over the wrong or incomplete subject creates formal motion without repair. Transfer therefore requires resolution of the operative work identity or an explicit bounded remainder describing what could not be reconstructed.

The universal GSM can type `HAS_NEXT_MOVE_DUTY`, `CUSTODIES_GKL_PROPOSAL`,  
`CUSTODIES_GIE_INTERVENTION`, `CUSTODIES_ACG_REMAINDER`,  
`REQUIRES_WORK_IDENTITY_RESOLUTION`, `TRANSFERS_WITH_FRAGMENTATION_REMAINDER`,  
and   
`RELEASED_AFTER_RECOGNIZED_CLOSURE`.

This randomized review establishes four editorial commitments: adopt the extended responsibility chain; bind intervention and mutation work to custody; preserve separate ACG completion surfaces; and require work-identity resolution or explicit fragmentation remainder before transfer.

## A Bitemporal Next-Move Duty Across Heterogeneous Closure Surfaces

Twenty-one retained downstream uses place Work Custody across capabilities, context compilation, physical effects, quant review, cold boot, communal work, infrastructure, lineage, situational awareness, cognitive exigence, ACG courts, incentives, human validation, operational orientation, receipt reasoning, semantic debt, fragmentation repair, split authority, the knowledge loop, optional coordination, and the pedagogical "Who Has the Ball?" surface. The stable primitive is the recognized next-move duty over an exact work subject, not ownership, authority, capability, accountability, or completion.

$$
\begin{aligned}
W^*= (&work\_identity, generation, scope, next\_move, custodian, \\
&valid\_time, record\_time, acceptance, authority, \\
&capability, dependencies, blockers, waiting\_edges, \\
&evidence, uncertainty, recognition\_surface, lease, \\
&expiry, recovery, remainder, successor)
\end{aligned}.
$$

Custody transfers are bitemporal and generation-bound. Offer, acceptance, release, revocation, lease expiry, forced assignment, and recovery require distinct receipts and race semantics. A formally valid transfer can still be operationally unusable when context, capability, access, or evidence is insufficient. Joint custody requires partitioned duties or an explicit shared closure rule so responsibility does not dissolve.

Completion is surface-specific. A test, court, deployment, effect, evidence, author-review, or publication surface may close while another remains open. Release therefore binds the exact closure recognized and preserves unresolved dependents. Partitions, dead agents, abandoned work, cycles, and privacy-limited handoffs yield typed recovery or remainder rather than invented progress.

The universal GSM can type `HAS_NEXT_MOVE_DUTY`, `OFFERS_WORK_CUSTODY`,  
`ACCEPTS_WORK_GENERATION`, `LEASES_CUSTODY_UNTIL`, `BLOCKED_ON_CUSTODY_EDGE`,  
`RECOGNIZES_SURFACE_CLOSURE`, `RELEASES_WITH_REMAINDER`, `RECOVERS_ABANDONED_WORK`,  
and   
`SUCCEEDS_CUSTODY_GENERATION`.

This review establishes four editorial commitments: adopt the complete bitemporal custody record; require explicit acceptance, lease, race, partition, recovery, and privacy semantics; make closure surface-specific; and prohibit custody, assignment, possession, receipt, or completion at one surface from laundering authority or global completion.

## Custody Names the Next-Move Duty, Not Control of the Work

### Public orientation

Work Custody identifies which eligible participant currently holds the bounded operational duty to advance an exact work object, version, and scope. It answers who has the next move while keeping ownership, assignment, authority, accountability, capability, standing, and actual possession separate. A transfer normally completes only when the successor accepts and the transition is promoted.

### Adversarial tests

1. **Custody-authority attack.** The current custodian acquires permission to approve, publish, deploy, spend, disclose, or alter protected scope merely by holding the next move.
2. **Offer-transfer attack.** A sender treats an offer or message as completed transfer although the receiver never accepted exact custody.
3. **Capability-fiction attack.** An agent accepts custody despite missing files, tools, context, time, competence, credentials, or a viable continuation.
4. **Version-drift attack.** Custody for one artifact, branch, generation, or scope is silently applied to a successor or sibling.
5. **Lease-squatting attack.** Long or renewable leases block useful work, conceal abandonment, or let a failed participant retain nominal custody.
6. **Split-brain attack.** Partitions, retries, clocks, duplicate promotions, or inconsistent stores produce more than one apparent primary custodian.
7. **Receipt-reality attack.** A receipt says custody moved or work completed although the material, state, or effect did not.
8. **Surveillance-query attack.** Queryability exposes sensitive work, participants, failures, location, availability, or organizational relations beyond operational need.

### Claim and evidence ceiling

The paper specifies a generation-bound, bitemporal custody state machine and algebra. It does not establish complete mediation, actual acceptance, participant capability, organizational authority, legal accountability, privacy, liveness, complexity reduction, or orchestration benefit. Human and machine participants may share event syntax without sharing consent, persistence, responsibility, or legal status.

Validation requires concurrent and partitioned state-machine tests, exact object and generation binding, acceptance and recovery exercises, lease and abandonment analysis, capability evidence, privacy review, baseline workflow comparison, and current external research. No implementation or external research was performed in this pass.

### Reader-facing consequence

The public benefit is a reliable answer to who is responsible for the next bounded move, when that duty began and expires, what they can actually do, and how work recovers when no one can continue - without confusing that answer with ownership or authority.

## 14. Conclusion

Work Custody replaces an implicit social convention with an explicit constitutional relation.

By distinguishing custody from ownership, authority, accountability, and assignment, collaboration systems gain an operational primitive for representing who is currently recognized as holding the bounded duty to advance an exact scope of work.

This enables collaboration environments to answer, continuously and mechanically, one of the most fundamental questions in cooperative activity:

> **Who has the ball?**

The answer becomes an explicit, queryable claim in governed shared state--still subject to mediation coverage, freshness, authority, and evidence.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm1.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that work Custody as a first-class collaboration relation identifying which eligible participant currently holds the bounded operational duty to advance a particular version and scope of a work object. Its nearest external comparison fields are provenance, security, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E2]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E3]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

**[E4]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E5]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E6]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E7]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

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

**[A4]** Adam Ableman. *Governance Witnesses*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-9E8DA0EFE860DE5D`;  
source SHA-256  
`8BF8C3646040F6E1F5222A8AA92C1106AA1F841E8A2C65402F468C83D59D06E5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Integrity Enforcement Layer*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-505307E9E6571B63`;  
source SHA-256  
`F858AB32E0937B796353CAE573DD4183FDF4F179A3E1E7E40C4E0C6BF1AB0018`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Adam Ableman. *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18633797.

Adam Ableman. *Semantic Custody*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20300952.

Adam Ableman. *The Three Hash Rule*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20788617.

Adam Ableman. *From Content-Addressed Storage to Governed Semantic Project Lineage*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *Governed Meaning Base (GMB)*. Authorized Ableman Corpus edition developed through the historical CCF -> CMB -> GMB lineage; canonical concept standing remains governed separately from publication.

Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

External comparison to workflow systems, actor models, leases, distributed transactions, work-stealing schedulers, responsibility assignment, incident command, case management, and organizational coordination requires a source-by-source literature review. The complexity-reduction and meeting-reduction claims remain research hypotheses pending comparative evidence.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI.* Zenodo, 2026. doi:10.5281/zenodo.18633797

Adam Ableman *Semantic Custody.* Zenodo, 2026. doi:10.5281/zenodo.20300952

Adam Ableman *Semantic Debt.* Zenodo, 2026. doi:10.5281/zenodo.21111666

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847360](https://doi.org/10.5281/zenodo.23847360)
