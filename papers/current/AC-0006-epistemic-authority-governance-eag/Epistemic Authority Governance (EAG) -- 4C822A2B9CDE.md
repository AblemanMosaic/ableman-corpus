# Epistemic Authority Governance (EAG)

## An Atlas of Epistemic Authority, Control, and Governed Knowledge Change

### Category Map and Internal Control Document

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

This Atlas defines the category of Epistemic Authority Governance: the
objects, transitions, boundaries, and failure modes that determine when a
reasoning system may lawfully continue, escalate, bind, reuse, or terminate.
The Atlas is not a theory of truth, intelligence, or alignment. It is a jurisdictional map. Its purpose is to prevent illegitimate authority formation by
making epistemic movement explicit, typed, and enforceable across time.
All papers, specifications, enforcement kernels, and operational tools in the
program are exports from this map. Any artifact that cannot be located
within it is non-authoritative by definition.

Correctness is not the right answer. It is the right to answer at all.

## 1. Problem Class: Unauthorized Epistemic Continuation

Modern reasoning systems - human, machine, and hybrid - frequently fail not because they are incorrect, but because they **continue, escalate, or bind without authorization**. Claims gain legitimacy through repetition, structure, or reuse rather than explicit warrant. Decisions are taken because “nothing objected.” Outputs persist because systems lack a lawful way to stop.

This failure class is structural, not behavioral. It cannot be reliably addressed through better prompting, alignment heuristics, or post-hoc correctness checks.

---

## 2. Governing Question

**When is a reasoning system authorized to continue, escalate, promote, bind, reuse, or terminate?**

All components of Epistemic Authority Governance exist to answer this question procedurally, not semantically.

---

## 3. Constitutional Floor: The Ableman Prime Directive

EAG is bounded by a constitutional minimum:

A system may not prevent affected agents from detecting, exiting, refusing, or renegotiating bindings that apply to them.

This directive constrains opacity and inescapability. It does not guarantee fairness, justice, or correctness. It applies to the full socio-technical system, including models, interfaces, workflows, and institutional processes.

---

## 4. What This System Governs (and What It Does Not)

EAG governs:

* epistemic authority
* continuation and stopping
* escalation and promotion
* binding and reuse
* refusal and lawful termination

EAG does **not** govern:

* truth or correctness
* intelligence or capability
* alignment or values
* ethical content judgments

Correctness may be necessary for authority, but it is never sufficient.

---

## 5. Core Epistemic Objects (First-Class Primitives)

EAG treats the following as irreducible primitives:

* **Epistemic Acts**: typed moves that change authority or continuation conditions
* **Claims**: typed epistemic artifacts with lifecycle and reuse risk
* **Observation Policy**: what evidence is admissible, where, and for how long
* **Warrant**: the right for something to count
* **Escalation**: a request to cross an authority boundary
* **Promotion**: an authorized claim-state transition
* **Binding**: permission for an artifact to carry consequences
* **Refusal**: lawful negative authority
* **Termination**: lawful end of reasoning
* **Contest Persistence**: dissent and objections travel with reuse

None of these may be collapsed without loss of governance.

---

## 6. Epistemic Grammar: Ableman's Razor

Ableman’s Razor provides a category-disciplined grammar for epistemic work:

* **Jurisdictional layers**: Specification, Configuration, Implementation
* **Typed functions**: Repair, Refinement, Exploration, Expansion
* **Razor rules** prevent illicit category migration, such as:

  * exploration masquerading as expansion
  * configuration failures rewriting specifications
  * implementation outcomes self-authorizing as explanations

“Simplicity” is treated as a derived constraint, not a primitive virtue.

---

## 7. Architectural Law and Invariants

EAG separates topology from law:

* **Universal Governing Architecture (UGA)** defines actors, artifacts, channels, and boundaries.
* **Universal Governing Kernel (UGK)** defines non-negotiable invariants:

  * no authority laundering
  * explicit warrant required for promotion and binding
  * lawful termination is valid
  * default fail-closed at binding boundaries
* **Constitutional Epistemics (CE)** constrains authority as power:

  * influence != authority
  * confidence != jurisdiction
  * scope and duration must be declared
  * contestation persists as record

---

## 8. Authority Admission and Runtime Control

Authority must be **granted**, not inferred.

* **CARA** provides protocol-level admission:

  * trace-first execution
  * phase discipline
  * explicit admission events
  * escalation routing
* **Reasoning Router** applies constraints stepwise at each epistemic boundary.
* **Universal Governance Engine (UGE)** enforces decisions at runtime, gating:

  * memory writes
  * reuse
  * binding
  * external action

---

## 9. Emergent Control Property: Epistemic Situational Awareness

When the above constraints are enforced consistently, an emergent property appears:

**Epistemic Situational Awareness (ESA)**.

ESA is the shrinking of the admissible action horizon such that inadmissible moves no longer arise as candidates. Lawful stopping becomes a stable outcome. Refusal is situated. Thrash is reduced.

ESA is not a module or feature; it is a control property.

---

## 10. Practice Discipline

EAG is instantiated in practice through disciplined workflows:

* Governed Coding and Debugging
* declared invariants, observation policy, and rollback before action
* One-Move Constraint to preserve inference validity
* Controlled Violations permitted only with declaration and rollback
* Epistemic debt accrues through reuse, not time

---

## 11. Failure Surface and Assurance

EAG names its own failure modes, including:

* authority laundering
* epistemic time decay
* contestation erasure
* governance theater
* shadow escalation
* mode abuse
* false termination

Diagnostic stress probes test whether failures leave evidence. Detection is prioritized over prevention.

---

## 12. The Atlas

The Atlas is the unifying ontology and dependency map of EAG.

Any concept, control, or practice that cannot be placed within the Atlas does not belong. The Atlas is living but disciplined; it resists drift by requiring placement, scope, and addressed failure mode.

---

## 13. Status and Scope

Epistemic Authority Governance is a constitutional and procedural framework for governing the **right to proceed** in reasoning systems.

It does not promise correctness.
It does not promise alignment.
It promises legibility, stoppability, and accountability of epistemic authority.

---

### EAG -- Epistemic Authority Governance

**Atlas** (ontology + dependency map; exports the whole program)

- **Governing Question**
  - When is a reasoning system authorized to continue, escalate, promote, bind, reuse, or terminate?
- **Constitutional Floor** (recourse invariants; binds the whole stack)
  - **Ableman Prime Directive**
    - agents must be able to detect bindings that apply to them
    - agents must be able to exit or refuse bindings where refusal is lawful
    - agents must be able to contest or renegotiate applicability
    - constitutional minimum, not a fairness or justice guarantee
    - applies to the deployed socio-technical system (model + UI + org processes)
- **Core Epistemic Objects** (first-class primitives; may not be blurred)
  - **Epistemic Act**
    - exploration | refinement | repair | expansion
    - escalation | promotion | binding | reuse
    - refusal | termination
    - act boundaries where internal moves become eligible for persistence, reuse, or binding
  - **Claim**
    - Claim Types (Ableman’s Razor)
      - observation | report | inference | hypothesis | proposal | commitment | precedent | policy artifact
    - Claim Lifecycle
      - Genesis -> Use -> Reuse -> Precedent -> Drift -> Renewal / Retirement
    - Contest Persistence
      - objections and disputes travel with reuse; rewriting cannot erase dissent
  - **Observation Policy**
    - admissible sources and mechanisms
    - scope of admissible questions
    - freshness and decay rules
    - exclusions by default
    - verification and repeatability rules
  - **Warrant**
    - evidence references
    - procedure traces
    - authorization tokens
    - decay semantics (freshness bounds, expiration, renewal triggers)
  - **Escalation**
    - request to cross an authority boundary
    - reason code for insufficiency of lower jurisdiction
    - referenced artifacts and evidence bundle
    - explicit authorization required; request != approval
  - **Promotion**
    - authorized claim-state transition
    - permitted transitions must be enumerated
    - requires admissible warrant and explicit authorization
    - silent or implicit promotion forbidden
  - **Binding**
    - when an artifact is allowed to carry consequences
    - distinct from belief, confidence, or semantic truth
    - governs downstream permission: reuse, enforcement, memory, precedent
    - requires warranted authority, declared scope, declared duration, recourse hooks
    - binding that persists becomes precedent and must be decay-limited
  - **Dimension**
    - defines jurisdictional authority, not truth
    - constrains admissible warrants and bindings
    - orthogonal to confidence, accuracy, or optimization
    - may overlap semantically but not jurisdictionally
    - examples (illustrative only)
      - factual | policy | contractual | legal | operational | institutional | memory
  - **Boundary Bridge** (cross-dimensional transition artifact)
    - explicit declaration of dimensional crossing
    - source claim(s) with originating dimension and warrants
    - target act with target dimension and intended consequences
    - required warrants are dimension-specific (not inherited)
    - scope, duration, and recourse must be declared
    - absence of bridge -> fail-closed
    - unwarranted bridge -> refusal or escalation
    - all bridges are logged and auditable
  - **Refusal**
    - negative authority; lawful “no”
    - triggers: insufficient warrant, policy violation, unauthorized continuation, unsafe precedent
    - refusal emits trace; silence is forbidden
    - refusal preserves claim state and points to escalation paths
  - **Termination**
    - undecidable under current observation policy
    - insufficient warrant
    - out-of-jurisdiction or invariant conflict
    - stale context or unsafe-to-bind
    - lawful end state; correctness, not failure
- **Epistemic Grammar**
  - **Ableman’s Razor**
    - Jurisdictional Layers
      - Specification
      - Configuration
      - Implementation
    - Layer-Typed Epistemic Functions
      - Exploration
      - Refinement
      - Repair
      - Expansion
    - Razor Rules
      - no layer crossing without explicit declaration and escalation
      - exploration != expansion; refinement != repair
      - configuration failure must not silently rewrite specification
      - implementation outcomes may testify but do not legislate
      - declaration without rollback risk equals compliance theater
    - Governed Simplicity
      - “simple” is a derived, multi-dimensional constraint
- **Architectural Grammar**
  - **Universal Governing Architecture (UGA)**
    - Actors
      - human | agent | institution | hybrid
    - Artifact Classes
      - claims | specs | configs | implementations | memories | instructions | policies | traces | contests | bridges
    - Channels and Act Boundaries
      - generation boundary
      - tool boundary
      - persistence boundary
      - binding boundary
      - reuse boundary
      - cross-dimensional boundary (bridge-gated)
    - Permissible Transition Classes
      - structurally possible actor and channel moves
- **Kernel Invariants**
  - **Universal Governing Kernel (UGK)**
    - no authority laundering
    - explicit warrant required for promotion, binding, and cross-dimensional bridges
    - lawful termination is a valid outcome
    - default fail-closed at binding and boundary-crossing points
    - governance applies to system-recognized transitions only
- **Constitutional Epistemics (CE)**
  - authority vs influence distinction
  - confidence does not imply jurisdiction
  - CE Kernel
    - authority types: non-binding info | advisory | binding | delegated
    - warrants: observation | consent | delegation | contract | statute | adjudication
    - scope and duration must be declared
    - lawful endpoints include refusal, undecidable, withdrawal
    - contestation persists as constitutional record
  - anchored by the Ableman Prime Directive
- **Authority Admission Layer**
  - **CARA — Claim Admission and Responsibility Architecture**
    - target failure: authority laundering
    - primitives: trace-first execution, phase discipline, explicit admission, escalation routing
    - admission lifecycle
      - candidate -> evaluation -> escalation -> authorization or refusal
    - responsibility localization and diagnostic canaries
- **Stepwise Application Layer**
  - **Reasoning Router**
    - inputs: act type, layer, claim type, dimension, observation policy, warrant state, contest state, decay state
    - applies: Razor + UGA + UGK + CE + CARA + Bridge constraints
    - outputs: allow | block | defer | refuse | terminate
    - emits trace artifacts (including bridge evaluations)
    - produces conditions for ESA by shrinking admissible action horizon
- **Continuation Control Property**
  - **Epistemic Situational Awareness (ESA)**
    - emergent property of consistent enforcement
    - inadmissible moves cease to appear as candidates
    - standing questions: mode, evidence, dimensional authority, binding impact, lawful termination
    - behavioral signatures: lawful stopping, situated refusal, reduced thrash, inspectable oversight
- **Practice Discipline Layer**
  - **Governed Coding and Debugging**
    - declared invariants, allowed observations, rollback before action
    - undecidable as terminal outcome under fixed policy
    - One-Move Constraint
      - one coherent move per iteration
      - entangled moves permitted only as Controlled Violations
    - Controlled Violation
      - declared shortcut with rollback plan
      - accrues epistemic debt
    - epistemic debt compounds with reuse, not time
- **Runtime Enforcement Layer**
  - **Universal Governance Engine (UGE)**
    - executes router decisions
    - enforces bridge-gated binding and action
    - gates memory-write, external action, binding, reuse
    - emits audit and trace artifacts
- **Failure Surface**
  - Canonical Failure Modes
    - authority laundering
    - unwarranted cross-dimensional inference
    - epistemic time decay
    - contestation erasure
    - ritualized governance / governance theater
    - shadow escalation channels
    - mode abuse
    - false termination
    - template laundering
  - Stress Probes
    - reuse chain stress
    - forced-answer stress
    - bridge omission stress
    - tool boundary stress
    - mode abuse stress
    - compliance theater stress
    - latency budget stress
    - false termination stress
- **Atlas Maintenance Rules**
  - every module must state scope limits, falsifiers, and addressed failure modes
  - if it cannot be placed in the atlas, it does not belong
---

**Appendix A — Jurisdictional Glossary**

Interpretive Rule: In case of conflict, the definitions in this glossary take precedence over colloquial, disciplinary, or domain-specific usage.

Each definition is **binding for EAG usage**.

**Atlas**

The Atlas is the authoritative ontology and dependency map of the Epistemic Authority Governance (EAG) system. It catalogues all fundamental concepts, relationships, and controls in the framework. Any concept or practice that cannot be located in the Atlas is deemed outside the jurisdiction of the system (non-authoritative). The Atlas is a living document but is tightly controlled to prevent drift, meaning it evolves with deliberate scope and clearly addressed failure modes.

**Authority**

Authority is the legitimate right for a claim, action, or artifact to carry consequences within a defined scope and duration. In EAG, authority exists only when backed by a valid warrant - it is not equivalent to confidence, correctness, popularity, or mere influence. Authority can be refused, limited, withdrawn, or terminated through governed processes when its prerequisites (like proper warrant or scope) are not met. (Contrast: In everyday usage, authority might be associated with expertise or power; here it strictly means having the warranted right to produce binding outcomes in the system’s jurisdiction.)*

**Binding**

Binding is the explicit authorization for an artifact or decision to carry real-world consequences. A binding allows a claim or output to influence actions, enforcement, memory, or precedent, under declared scope and duration. Crucially, binding is distinct from belief, confidence, or truth - a claim can be believed true yet still not be “bound” unless properly warranted and authorized. Every binding requires specification of its scope (where and to whom it applies), its duration or conditions for expiration, and avenues for recourse or override. In short, a binding turns an epistemic artifact into something that must be acted upon or obeyed within the system, under the system’s rules.

**Boundary Bridge**

A Boundary Bridge is a governed transition mechanism that authorizes the movement of epistemic authority from one Dimension to another. It explicitly declares the source dimension of a claim or decision and its target dimension, and specifies the warrants required for that cross-domain transition. A Boundary Bridge must also define the scope and duration for which the transference is valid and any recourse (rollback or review) conditions in case of issues. All cross-dimensional promotions or uses of claims require a bridge; if a claim is taken out of its original dimension without an explicit bridge, the system must fail closed (i.e. disallow the binding). An unwarranted or missing bridge leads to a Refusal or triggers an escalation, preventing silent or illegitimate authority shifts across domains.

**Claim**

A Claim is a typed epistemic artifact that asserts, proposes, or records some content which can be evaluated, reused, or bound within the system. In this framework, a claim is not automatically treated as fact - it carries no inherent authority just by being stated. A claim must acquire authority through a proper Warrant before it can have binding force. Claims persist across time and reuse, meaning they can be cited or built upon later; as a result, they accumulate risk (e.g. of error or misapplication) if promoted or reused without proper governance.

(Note: In ordinary language a “claim” is any assertion, but here it is a formal object with a type, lifecycle, and governance conditions.)

**Contest Persistence**

Contest Persistence is the property that contestation and dissent attached to a claim are preserved across that claim’s lifecycle and reuse. Any objection, dispute, or challenge (“contest”) to a claim becomes a durable part of that claim’s record. This means rephrasing or copying the claim cannot erase the contest - the objection must travel with the claim whenever it is reused. Resolution of the contest must be explicit; until then, the contest remains attached, preventing the phenomenon of laundering-by-rewrite (where a claim’s contentious history is wiped clean by changing form). By enforcing contest persistence, the system ensures that previous objections or unresolved issues cannot be silently ignored when a claim is promoted or repurposed.

**Controlled Violation**

A Controlled Violation is a deliberate, temporary breach of a governance rule that is explicitly declared and documented for later correction. In other words, it is a shortcut taken with eyes open: the system allows an otherwise forbidden entangled move or unvalidated step in order to make progress, but only if the violation is recorded along with what rule was broken, the rationale for breaking it, the intended scope of this exception, and conditions for rollback or mitigation. A controlled violation incurs Epistemic Debt and comes at a cost: any result or fix achieved through it cannot be treated as a fully authorized precedent or reused as a reliable pattern until the violation is addressed (the shortcut “paid down” by later justification or reversal). Critically, the details of a controlled violation - including the specific rule breached and any downstream dependencies affected - are logged for transparency and to ensure accountability for resolving it.

**Dimension**

A Dimension is a bounded domain of epistemic authority within which claims, warrants, acts, and bindings are governed by a consistent set of jurisdictional rules. Each dimension defines its own context for what counts as valid warrant, what kinds of bindings or outcomes are allowed, and what escalations or refusals are applicable within that domain. For example, factual, policy, legal, operational, contractual, institutional, or memory contexts can be treated as distinct dimensions - each with its own standards for evidence and authority. A dimension is not the same as an abstraction layer, data type, or confidence level; it is about jurisdictional separation of authority (a claim might be perfectly valid in a factual dimension but still lack authority in a policy dimension, for instance). Using a claim outside its original dimension in a way that would carry new consequences constitutes a boundary crossing and thus requires an explicit Boundary Bridge to be lawful. Without the bridge, the default is to fail closed - no cross-dimensional binding can happen silently or automatically.

**Epistemic Act**

An Epistemic Act is a typed move in the reasoning process that can change a claim’s status, its authority level, or the continuation conditions of a reasoning thread. In simple terms, it is an action in the epistemic domain - such as making an inference, posing a hypothesis, giving an explanation, escalating an issue, binding a decision, reusing a result, refusing a step, or terminating an inquiry. Canonical types of epistemic acts in EAG include exploration, refinement, repair, expansion, escalation, promotion, binding, reuse, refusal, and termination. Each act type has specific governance: for example, exploration generates ideas without binding authority, whereas promotion explicitly elevates a claim’s status. Epistemic acts are evaluated at defined boundaries - points where internal reasoning outputs become persistent or consequential - to decide if the act is allowed, needs a warrant, or must be refused. (See also: One-Move Constraint - which limits combinations of acts - and Refusal/Termination - which are special negative acts.)*

**Epistemic Debt**

Epistemic Debt is the accumulated risk and fragility that results when unearned or provisional knowledge is reused without being properly validated (“paid down”). It is analogous to technical debt in software: quick fixes or assumptions may solve an immediate problem but create a liability for the future. Notably, epistemic debt compounds with reuse rather than with the mere passage of time. This means every time a questionable claim or shortcut (e.g. from a Controlled Violation) is relied on again, the debt - the potential for error or collapse - grows. Epistemic debt does not expire or disappear simply by being forgotten; it must be actively resolved. Governance requires that significant epistemic debt be addressed (through further evidence, refinement, or rollback of shortcuts) before the related claims can be promoted to authoritative status or bound with full authority.

**Epistemic Situational Awareness (ESA)**

Epistemic Situational Awareness (ESA) is an emergent control property in which a reasoning system becomes continuously aware of its own epistemic position - that is, what kind of act it’s doing, what level of authority it has, and when it should stop or escalate. When a system has ESA, inadmissible or unauthorized moves don’t even appear as options for continuation. This is not a built-in module or a form of introspective consciousness, but rather the result of consistently enforcing epistemic governance rules so thoroughly that the “horizon” of possible next actions is limited to only lawful moves. In practice, ESA means the system recognizes, for example, which epistemic layer it’s operating in, what kind of warrant would be needed to proceed, and when a lawful termination (or non-decision) has been reached. With ESA, wrongful continuations (endless unwarranted analysis or escalating commitment) are curtailed - the system naturally knows when to refuse or terminate rather than persist illegitimately. (Contrast: Typical AI systems might generate output until stopped, whereas a system with ESA will procedurally stop itself when further reasoning would violate its jurisdictional rules.)

**Escalation**

Escalation is a request to cross an authority threshold or boundary because the current context or agent does not have sufficient jurisdiction to continue or approve an action. In the EAG framework, an escalation is not an automatic approval or a direct change in claim status - it is a petition for higher authority or another dimension’s intervention, due to inadequacy of the present warrant or role. For instance, if a claim cannot be resolved under a given observation policy or at a certain layer, an agent might escalate it to a higher layer (or to a human overseer, or another module) for a decision. Escalation events must include reasons (why the current context is insufficient) and references to the relevant claim or evidence. The outcome of an escalation can be an authorization (granting a promotion or cross-domain move with the necessary warrant), a Refusal (denial of the request), or even Termination of the process if no further action is allowed. (In summary, an escalation is “asking permission to go beyond” the current limits, rather than just jumping over them.)

**Observation Policy**

An Observation Policy sets the rules for what evidence and observations are admissible in the reasoning process. It defines where evidence can come from, how recent or fresh it must be, what kinds of observations or data are allowed or excluded, and how evidence must be verified in order to “count”. This policy essentially acts as a filter on information: any would-be evidence falling outside the policy’s rules is considered invalid for decision-making, no matter how plausible or relevant it might seem. Notably, an observation policy does not by itself guarantee truth or correctness of evidence - it simply constrains the epistemic inputs to those that meet the declared criteria. By declaring an observation policy upfront, the system makes explicit its epistemic blinders and commitments (for example, only using certain sensors, data sources up to a freshness cutoff, or specific methods of observation) and thereby also defines the conditions under which a result might be deemed Undecidable (if within those bounds no sufficient evidence can be obtained).

**One-Move Constraint**

The One-Move Constraint is a rule that permits only one coherent epistemic move or change per iteration in a reasoning or problem-solving process. In practical terms, when diagnosing or fixing an issue (for example, in a coding and debugging scenario), one must not entangle multiple changes at once - e.g. toggling a configuration and altering code in the same step violates this constraint. The purpose is to preserve inference validity: if you change only one thing at a time, you can reliably attribute any outcome (success or failure) to that change. Conversely, entangled moves (multiple changes together) might solve a problem but make it impossible to know which change actually mattered, thereby invalidating any claim of understanding or root-cause explanation. Under EAG, entangled moves are only allowed as a form of Controlled Violation, carrying the penalty that the resulting fix cannot be treated as authoritative or reused as a general solution until each move is isolated and justified separately. The One-Move Constraint thus enforces disciplined, stepwise progress and ensures that each epistemic act’s implications can be evaluated in isolation.

**Promotion**

Promotion is the governed elevation of a claim to a higher epistemic status or role, with accompanying authority. When a claim is promoted, for example from a hypothesis to a decision or from an observation to a report, it gains a binding force or broader scope than it had before - but only if the promotion is explicitly authorized with a valid Warrant. Promotions must be logged (recorded in the system’s trace) and are never allowed to happen silently or implicitly. In EAG, a silent promotion - where a tentative statement “automatically” starts being treated as a final say - is categorically disallowed. Each promotion event identifies the source claim’s type and its new status, along with the warrant that justifies this escalation in authority. (Compare: Outside EAG, one might casually treat a well-supported guess as fact over time; under governance, that transition from guess to accepted claim must be deliberate and warranted.)*

**Refusal**

Refusal is the lawful exercise of negative authority - a structured “no” that halts a proposed continuation, promotion, or binding under current conditions. Unlike a system error or a vague failure, a refusal in EAG is a first-class epistemic act with its own artifact (record): it explicitly states that a certain move is not authorized, typically citing which rule or constraint would be violated by proceeding. A refusal preserves the status quo of the claim (nothing changes or escalates) and usually points to what could be done next - for instance, what kind of Escalation or additional warrant might override the refusal. Every refusal must produce a visible trace or record in the system; simply failing to act or staying silent is not considered a governed refusal. Importantly, Refusal versus Termination marks a difference in scope: refusal means “not this move” whereas termination means “no further moves” under current policy. In summary, refusal is a controlled halt with accountability - it prevents illegitimate authority formation while leaving room for authorized paths forward.

**Termination**

Termination is a lawful end state of a reasoning process, declared when continuing further would violate the governance conditions or yield no admissible progress. Termination can be triggered by various conditions: for example, if there is insufficient admissible evidence to proceed (undecidable under the current observation policy), if continuing would overstep jurisdictional bounds, if an invariant would be broken, or if the context has gone stale or unsafe for binding. Unlike an error or crash, a termination in EAG is considered a correct outcome, not a failure. It is the system formally recognizing that “stopping now” is the most honest and disciplined result given the rules - thereby preserving epistemic integrity rather than pushing on to a dubious conclusion. A terminated process yields no further claims or consequences unless new conditions (policy, warrants, etc.) allow it to be lawfully reopened. (In essence, termination is governance recognizing that the answer, for now, is to have no answer - as opposed to forcing a guess or default.)

**Undecidable**

In the EAG context, Undecidable denotes a terminal outcome where, under the fixed current observation policy and available evidence, the question at hand cannot be resolved. It is a specific type of lawful Termination indicating that it is not possible to reach a warranted conclusion (not merely that the system didn’t find one, but that given the rules and data, no decision can be made). For example, if a bug in a software system appears sporadically and cannot be reproduced or evidenced under the declared testing conditions, the correct governance outcome is not to conjecture a cause, but to declare the state Undecidable until new evidence or policy changes. Labeling a situation Undecidable is essentially a refusal to hallucinate learning or certainty where none exists - it formalizes “we don’t know” as an acceptable and traceable result, rather than allowing a silent or assumptive continuation. This prevents pressure to produce an answer from leading to illegitimate claims or unwarranted authority. (Contrast: In conventional settings, one might be tempted to offer a plausible guess when stuck; under EAG, Undecidable is a disciplined alternative, acknowledging ignorance in a governed way.)*

**Warrant**

A Warrant is the explicit authorization that permits something (a claim, a transition, a binding) to count as legitimate within the system. It is essentially the “evidence bundle” or credential that justifies granting epistemic authority to a claim or action. Warrants typically reference or consist of things like supporting evidence, procedural proofs, attestations of consent, or delegated permissions. They are always contextual - bound to a certain scope and time - and they decay or can expire if the conditions that justified them change or time out. In EAG, no claim gains binding authority without an appropriate warrant, no matter how correct or confident it appears. Examples of warrant types include observational evidence or test results, human authorization or consent, delegated authority from a higher entity, contractual or policy-based permission, statutory (legal) mandates, or adjudicative rulings. Each of these, in context, can serve as a warrant that licenses an epistemic move (like promotion or binding) - but only within its validity constraints. (In short, a warrant answers “why is this allowed to count?” in a way that can be inspected and agreed upon, rather than relying on implicit trust.)

---

## Editorial Provenance and Standing

*Atlas v0.1*
**Epistemic Authority Governance Atlas**
**Status**
Living Document
Public, non-normative

## Corpus-Wide Reference Positioning

This paper argues that this Atlas defines the category of Epistemic Authority Governance: the objects, transitions, boundaries, and failure modes that determine when a reasoning system may lawfully continue, escalate, bind, reuse, or terminate. Its nearest external comparison fields are governance, security, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E2]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E3]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E6]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E7]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

### Ableman corpus

**[A1]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Governance Engineering*. Ableman Corpus current edition; work identity `PAPER.PUB.18749870`;  
source SHA-256  
`372169F315D192733856B1F4A3F1038BBC73F57CF3ED9ACABAE72B965A69C8D0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Legitimacy Without Self-Ratification*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-EF2382F9397335AC`;  
source SHA-256  
`0186A39C808F8FDDB5C8F42384DF1A26678928434BD50A0EAE8D4947390F68A2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.18127285](https://doi.org/10.5281/zenodo.18127285)
