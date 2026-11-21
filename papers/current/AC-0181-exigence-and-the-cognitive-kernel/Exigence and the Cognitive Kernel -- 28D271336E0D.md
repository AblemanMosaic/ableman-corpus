# Exigence and the Cognitive Kernel

## A Governed Account of What Calls for Transition

### Pressure is not authority, notice is not truth, and a call for change is not yet permission to act.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Computational systems routinely model tasks, priorities, deadlines, permissions, attention, and action, but they rarely possess a unified account of why a particular state presently calls for transition. This paper introduces **Exigence** as a first-class computational primitive: the graph-derived condition by which an object, process, agent, institution, or environment presently calls for some admissible change. Exigence is neither priority nor urgency. Priority is declared ordering; urgency concerns time sensitivity; Exigence arises from the live relationship between state, dependency, consequence, opportunity, authority, capability, care, safety, and constraint.

The paper situates Exigence within a broader **Cognitive Kernel**, or CogK, that separates observation, salience, epistemic interpretation, Exigence, standing, attention, custody, sufficiency, policy, authorization, execution, receipt, and outcome. These elements are treated not as interchangeable stages but as distinct projections over shared governed reality. The separation allows systems to distinguish what is observed from what is believed, what matters from what may be done, and what may be done from what actually occurred.

The resulting architecture supports lawful refusal, receipt-before-effect, context compilation, agent orchestration, institutional modeling, attention governance, household coordination, autonomous systems, games, simulated societies, and the progressive crystallization of expensive semantic reasoning into deterministic machinery. It also permits the modeling of pathological Exigence topologies such as fixation, suppression, inflation, avoidance, fragmentation, and over-propagation. These structures need not be used to diagnose humans. They can instead serve as integrity and execution-gate models for detecting recurrent computational trajectories that should be refused, escalated, reinterpreted, or repaired.

The central claim is that Exigence is a candidate connective layer between a passive world model and governed transition. Its value depends on keeping an Exigence claim distinct from observation, salience, standing, attention, policy, authorization, effect, and outcome. The Cognitive Kernel thereby offers a general substrate for systems that must decide what currently matters, who holds the next move, what conditions are sufficient, what transitions are lawful, and when action must stop.

## 1. Introduction

A task list records work.

A scheduler orders work.

A notification system surfaces work.

A planner proposes work.

An executor performs work.

None of these, by themselves, answer a more fundamental question:

> What in the present state of reality now calls for transition?

Conventional systems usually approximate this question through combinations of priority labels, due dates, alerts, dependencies, service-level agreements, utility functions, interrupt classes, and human judgment. These mechanisms are useful but conceptually fragmented. A due date may indicate temporal pressure without indicating consequence. A high-priority task may remain inactionable because authority or evidence is missing. A loud notification may capture attention despite low significance. A slowly degrading bridge, medication supply, security boundary, or institutional capability may remain nearly invisible until failure becomes acute.

The concept of **Exigence** addresses this gap.

Exigence is the live, situated call for transition that emerges from the relationship between an object and its surrounding governed world. It is not simply stored on the object. It is derived from topology: dependencies, blocked successors, risks, temporal windows, obligations, institutional standing, available resources, human needs, and admissible futures.

An unpaid bill approaching its due date may acquire Exigence. If payment is impossible because an account is locked, the actionable Exigence propagates toward resolving the account lock. If authority is missing, the authority request becomes the relevant next object. If repeated execution attempts fail without new evidence, model repair may become more exigent than another retry.

This movement is central. Exigence does not merely rank objects. It helps locate where reality is actually waiting.

The Cognitive Kernel introduced in this paper places Exigence within a governed architecture for perception, interpretation, attention, authority, execution, and learning. It is intended for systems in which action must be explainable, bounded, reversible where possible, and capable of lawful refusal.

## 2. Exigence

### 2.1 Definition

Exigence is:

> The graph-derived condition by which a present state calls for an admissible transition.

The definition contains four important commitments.

First, Exigence is **state-relative**. A condition may be non-exigent in one state and highly exigent in another.

Second, it is **graph-derived**. Its significance arises through relationships rather than isolated object properties.

Third, it is **transition-oriented**. Exigence concerns pressure toward change, not merely importance.

Fourth, it is **constitutionally bounded**. A state may strongly call for change without authorizing every possible response.

### 2.2 Priority, Urgency, Salience, and Exigence

These terms should remain distinct.

**Priority** is a declared or computed ordering.

**Urgency** concerns diminishing time before consequence or opportunity loss.

**Salience** concerns what captures notice or processing.

**Exigence** concerns what the modeled reality presently calls to be resolved.

A loud alarm may be salient but false.

A maintenance defect may be low-salience but highly exigent.

A project may be declared high-priority but presently blocked.

A medical prescription may not yet be urgent, yet its refill process may already be exigent because pharmacy, insurance, and appointment delays require advance action.

This distinction allows a system to preserve silent but meaningful states.

For example:

```text
Household object:
Clean bathroom toilet

Green:
Tracked, available in household view, not shown in notifications

Yellow:
Visible in upcoming work

Red:
Eligible for active reminder

Reevaluation:
Daily
```

The object exists throughout. Its Exigence changes. Its visibility and interruption eligibility are separate projections.

### 2.3 Exigence as Topology

Exigence may emerge through:

* dependency pressure;
* safety exposure;
* temporal decay;
* opportunity windows;
* care obligations;
* constitutional duties;
* maintenance accumulation;
* authority gaps;
* information deficits;
* resource shortages;
* social commitments;
* reversibility loss;
* downstream congestion;
* unresolved contradiction.

Suppose a release is waiting on verification. The release itself may appear exigent, but the actionable transition belongs to the missing verifier artifact. If that artifact cannot be produced because the executor lacks access, custody may need to move to an authorized role. If no such role exists, the institutional design itself becomes the object of concern.

Exigence therefore propagates toward the nearest unresolved prerequisite capable of changing the state.

### 2.4 Formal Object: Exigence as a Typed Claim

Let the governed world at time $t$ be a typed graph $G_t=(V_t,E_t)$. For object $v$, an interpreting role may propose an Exigence claim

$$
x_t(v) = (d,\rho,\omega,\kappa,\eta,\chi,\lambda),
$$

where $d$ is the typed transition demand, $\rho$ its dependency and propagation path, $\omega$ its temporal window, $\kappa$ its consequence and reversibility profile, $\eta$ its evidence and uncertainty, $\chi$ its candidate custodian/capability relation, and $\lambda$ its scope and jurisdiction. This is deliberately not one universal score.

The claim becomes *admitted Exigence* only through a standing decision:

$$
S(x_t,G_t,C_t,J_t) \in \{\operatorname{ADMIT},\operatorname{REFUSE},\operatorname{DEFER}\},
$$

under constitutional state $C_t$ and jurisdiction $J_t$. Admission still does not authorize an effect. Policy, sufficiency, and authority must bind an exact candidate transition separately.

The non-collapse invariants are therefore:

$$
\begin{aligned}
&\text{salience} \not \\
&\Rightarrow \text{Exigence},\qquad \text{Exigence} \not \\
&\Rightarrow \text{standing},\qquad \text{standing} \not \\
&\Rightarrow \text{authorization},\qquad \text{authorization} \not \\
&\Rightarrow \text{successful outcome}
\end{aligned}.
$$

Exigence may propagate toward one or more unresolved prerequisites, but there need not be a unique nearest prerequisite. Several incomparable blockers can coexist, and propagation itself is an evidence-bounded inference subject to contest and revision.

## 3. The Cognitive Kernel

The Cognitive Kernel is a structured account of how a governed system notices, interprets, recognizes, orders, authorizes, acts, refuses, and learns.

Its principal elements are:

```text
OBSERVATION
What information entered the system?

SALIENCE
What became noticeable?

EPISTEMIC POSITION
What does an interpreting role currently believe the observation means?

EXIGENCE
What state now appears to call for transition?

STANDING
Which asserted needs or claims are constitutionally recognized?

ATTENTION
What receives scarce processing or display capacity?

CUSTODY
Who or what presently holds the next move?

SUFFICIENCY
Are the required information, authority, capability, artifacts,
resources, and opportunity present?

POLICY
What ordering, constraints, and precedence rules apply?

AUTHORIZATION
Which exact transition is presently permitted?

EXECUTION
What change is attempted?

RECEIPT
What was performed, refused, deferred, superseded, or failed?

OUTCOME
What actually changed in governed reality?
```

These elements should not be collapsed into a single score or opaque decision function. They are distinct projections, often produced by different roles and governed by different authorities.

### 3.1 Observation

Observation records admitted information without prematurely converting it into meaning.

Examples include:

* a sensor reports an obstacle at 0.8 feet;
* a bill is due in seven days;
* an agent has repeated the same repair six times;
* a bridge inspection reports material degradation;
* an NPC encounters smoke near a bakery;
* a user has postponed a task three times.

Observations may themselves carry provenance, freshness, confidence, and admissibility status.

### 3.2 Salience

Salience represents what became noticeable.

It is not proof of significance. Systems are vulnerable when salience automatically governs action. Attackers, interfaces, institutional incentives, and noisy environments can manufacture salience.

The Cognitive Kernel therefore treats salience as input to interpretation, not as authority.

### 3.3 Epistemic Position

An Epistemic Position is an inspectable interpretation of admitted observations.

It may include:

* a proposed meaning;
* confidence;
* supporting evidence;
* rival explanations;
* unresolved uncertainty;
* model assumptions;
* recommended next inquiry.

For example:

```text
Observation:
Front sensor reports 0.8 feet.

Epistemic Position:
A nearby obstacle probably blocks safe forward acceleration.

Confidence:
High.

Rival possibilities:
sensor fault;
temporary obstruction;
calibration error.
```

The Epistemic Position may be rich, probabilistic, semantic, and expensive to produce. It need not itself authorize action.

### 3.4 Exigence

Exigence is inferred from the relationship between the interpreted state and the available transition graph.

In the sensor example, the immediate Exigence may be:

```text
Resolve forward-path safety before acceleration.
```

This is not equivalent to "stop forever." It identifies what must be addressed before the requested transition becomes admissible.

### 3.5 Standing

Standing determines which Exigence claims are recognized by the governing constitution.

A system may receive many assertions:

* a user requests immediate execution;
* an agent claims a deadline;
* a department claims emergency authority;
* an NPC claims ownership;
* a service claims criticality.

Standing prevents every asserted need from automatically governing action.

An attacker may manufacture urgency. A supervisor may insist that all work is critical. A game faction may claim jurisdiction it does not possess. Standing asks whether the claim is recognized, by whom, and within what scope.

### 3.6 Attention

Attention allocates scarce processing, presentation, and interruption capacity.

An object may be fully modeled yet excluded from notifications.

An object may remain retrievable yet absent from an LLM context window.

An institutional problem may be visible to auditors but not interrupt a frontline executor.

Attention is therefore a projection policy over admitted state and Exigence, not the same thing as Exigence itself.

### 3.7 Custody

Custody answers:

> Who presently has the next move?

Exigence answers:

> How strongly does the present state call for that move?

The pairing is essential.

An object can have high Exigence and no custodian.

A role can hold custody but lack authority.

Custody can be assigned nominally while the artifacts, information, or decision rights remain elsewhere. This produces phantom delegation.

### 3.8 Sufficiency

Sufficiency asks whether the custodian possesses what is required for transition.

Relevant dimensions include:

* information;
* evidence;
* authority;
* capability;
* tools;
* artifacts;
* resources;
* time;
* opportunity;
* physical access;
* valid dependencies.

Insufficiency should not be treated as personal failure. It should create a new object or redirect Exigence toward the missing condition.

### 3.9 Policy

Policy orders recognized Exigencies and constrains possible responses.

A constitutional policy might establish:

* safety before throughput;
* human dignity before productivity maximization;
* receipt before effect;
* provenance before execution;
* care obligations before routine convenience;
* irreversible harm before reversible delay;
* rest as possessing independent standing;
* no hidden authority expansion.

Policy need not force all Exigencies into a total ordering. Many situations are better modeled by partial orders and hard precedence classes.

### 3.10 Authorization

Authorization binds a specific transition to a specific state, authority, scope, and set of predicates.

It should answer:

* what may occur;
* by whom;
* against which object;
* under which evidence;
* within what time or freshness window;
* subject to which revalidation conditions.

Authorization should not be assumed durable when its predicates may change.

### 3.11 Execution

The Executor should remain as small as possible.

It need not repeat the semantic work of the Steward or policy work of the Governor. It should determine whether the exact requested transition remains admissible under current critical facts.

For example:

```text
Requested transition:
Accelerate from zero.

Current trusted fact:
Front distance = 0.8 feet.

Rule:
No forward acceleration below 1 foot.

Result:
Refuse.
```

The Executor may revalidate only the minimal predicates bound into authorization:

* sensor freshness;
* current state;
* authority validity;
* rule identity;
* environmental threshold.

If these changed after the Epistemic Position was formed, the Executor should emit:

```text
AUTHORIZATION_STALE
RE-EVALUATION_REQUIRED
```

### 3.12 Receipt and Outcome

Receipt records what the system did or refused to do and why.

Outcome records what actually changed.

These are not identical. An execution receipt may report that a transfer was attempted. The outcome may be that the bank rejected it. The resulting state generates new Exigence.

Receipts make cognition and execution inspectable over time. They support replay, audit, model repair, accountability, and history generation.

## 4. Roles Within the Kernel

The Cognitive Kernel can be projected across multiple constitutional roles.

### 4.1 Steward

The Steward maintains the richest current interpretation.

It asks:

* What changed?
* What does it mean?
* Which Exigencies arise?
* What evidence supports them?
* What rival explanations remain?
* What is uncertain?
* What deserves reevaluation?

The Steward may use expensive semantic computation, including large language models, simulation, analogical reasoning, and contextual inference.

### 4.2 Governor

The Governor determines:

* which claims have standing;
* which policies apply;
* which Exigencies outrank others;
* which tradeoffs are permitted;
* which authority may be delegated;
* which transitions require ratification;
* which rules may become binding.

The Governor transforms interpretation into constitutional order.

### 4.3 Executor

The Executor determines whether an exact transition is permitted now.

Its minimality is a strength. Rich cognition belongs upstream. The Executor protects the effect boundary.

### 4.4 Auditor or Adjudicator

An Auditor or adjudicator evaluates:

* whether observations were admissible;
* whether interpretations exceeded evidence;
* whether standing was properly granted;
* whether authorization matched policy;
* whether execution matched authorization;
* whether receipts correspond to outcomes;
* whether new rules deserve admission.

### 4.5 Foundry or Model-Repair Process

When recurring cases exceed the current model, the Foundry proposes new object types, predicates, pathology detectors, propagation rules, and deterministic machinery.

The system may propose its own repair. It may not silently ratify itself.

## 5. Pathological Exigence Topologies

Cognitive and psychiatric literature contains rich descriptions of altered salience, fixation, avoidance, inhibition, compulsive repetition, fragmentation, suppression, and inappropriate generalization. A computational system need not use these models to diagnose humans. It can instead abstract them into formal topologies of malformed execution.

The question becomes:

> Has the system entered a recurrent structural region in which its Exigence processing no longer responds lawfully to evidence, context, outcome, or constraint?

### 5.1 Fixation

One object remains dominant despite contradictory evidence, failed outcomes, or newly available alternatives.

```text
Same strategy attempted repeatedly.
No new evidence admitted.
Failure receipts accumulate.
Exigence ranking remains unchanged.
```

A gate may refuse another identical retry and require:

* model revision;
* new evidence;
* custody transfer;
* strategy diversification;
* Steward review.

### 5.2 Avoidance

A class of high-Exigence objects is persistently displaced by easier, more visible, or more rewarding work.

Examples include:

* cosmetic improvements displacing integrity repairs;
* easy tests displacing failing safety paths;
* visible production displacing maintenance;
* short-term institutional wins displacing structural obligations.

The system should investigate whether avoidance arises from:

* insufficient capability;
* missing authority;
* poor specification;
* incentive design;
* hidden cost;
* inappropriate policy;
* malformed ontology.

### 5.3 Inflation

Too many objects are classified as acute.

This destroys meaningful attention allocation and permits alert-based coercion.

Possible repairs include:

* typed Exigence;
* evidence thresholds;
* propagation limits;
* hard distinction between safety and commercial pressure;
* partial ordering;
* notification budgets;
* adversarial review of elevation claims.

### 5.4 Suppression

Serious conditions remain underrepresented.

Examples include:

* missing provenance treated as minor;
* maintenance debt hidden by successful operation;
* repeated refusal receipts ignored;
* human exhaustion excluded from planning;
* degraded redundancy treated as normal.

Suppression can create the appearance of efficiency while accumulating systemic risk.

### 5.5 Fragmentation

Attention and custody shift so frequently that no bounded transition reaches closure.

A system may generate many partial plans, context compilations, and attempts without finishing any admissible unit.

A repair may freeze new admissions and require one bounded closure target.

### 5.6 Over-Propagation

A local condition spreads across too much of the graph.

One failed test may halt an unrelated release. One rumor may trigger institutional panic. One sensor anomaly may disable an entire robot fleet.

The system should require evidence for each propagation edge.

### 5.7 Stale Exigence

A resolved object continues to govern attention and execution.

Terminal receipts should collapse or transform its Exigence unless a new condition explicitly reopens it.

### 5.8 Pathological Manifold Regions

These patterns can be understood as regions of a computational behavior manifold.

A governed system may identify that it is:

* remaining trapped in a narrow transition basin;
* refusing to enter necessary state regions;
* repeatedly cycling through equivalent states;
* amplifying local signals into global prohibitions;
* suppressing evidence that would require model revision;
* collapsing all distinctions into one acute state.

The purpose is not metaphorical diagnosis. It is to define integrity gates over recurrent execution structures.

## 6. Receipt-Before-Effect

Receipt-before-effect makes the Cognitive Kernel operational at the execution boundary.

A refusal should not merely return an error. It should identify:

* the pattern detected;
* the attempted effect;
* the evidence considered;
* the policy applied;
* the authority of the gate;
* the state that prevented execution;
* the permitted successor transitions.

For example:

```text
REFUSAL RECEIPT

Pattern:
EXIGENCE_FIXATION

Attempted effect:
Repeat repair strategy S.

Evidence:
Six previous failures.
No new input.
Strategy identity unchanged.
Contradictory verifier result admitted.

Permitted successors:
Revise hypothesis.
Acquire new evidence.
Transfer custody.
Escalate to Steward.
```

This creates lawful refusal space.

The system does not merely say:

```text
NO
```

It says:

```text
NOT THIS TRANSITION,
FROM THIS STATE,
UNDER THIS EVIDENCE.

THESE OTHER TRANSITIONS REMAIN AVAILABLE.
```

That distinction is foundational for safe agentic execution.

### 6.1 Decision, Effect, and Standing

"Receipt-before-effect" is best understood as a non-bypassable authorization commitment at the effect boundary, not as a claim that all evidence can exist before the physical world is touched. The lifecycle separates:

1. proposal and current-state binding;
2. admissibility decision or refusal/defer;
3. effect attempt;
4. effect observation;
5. verification against the claim boundary;
6. promotion to eligible standing; and
7. later revision, revocation, or reconciliation.

A decision receipt does not prove that the effect occurred. An execution report does not verify itself. If an effect occurs without conforming evidence, the result is an orphaned effect requiring reconciliation, not a clean non-event and not an automatically admitted state.

This refinement connects the Cognitive Kernel to Reasoning by Way of Receipts: the durable object is a typed receipt graph, not one undifferentiated success record.

## 7. FSC and DSC

The Cognitive Kernel supports a progression from expensive semantic reasoning to deterministic execution.

### 7.1 FSC

The Flexible Semantic Compiler, or FSC, handles:

* ambiguous interpretation;
* latent Exigence discovery;
* rival hypothesis generation;
* novel topology recognition;
* contextual recommendation;
* ontology repair;
* policy proposal;
* explanation;
* semantic gap stitching.

It may rely on LLMs or other broad inference systems.

### 7.2 DSC

The Deterministic Semantic Compiler, or DSC, handles admitted, structured, repeatable cases.

Examples include:

```text
IF prescription_days_remaining <= 7
AND refill_available = false
THEN create MEDICATION_CONTINUITY exigence.
```

```text
IF task deferred three times
AND each refusal cites AUTHORITY_MISSING
THEN open AUTHORITY_TOPOLOGY_REVIEW.
```

```text
IF identical execution strategy fails repeatedly
WITHOUT new evidence
THEN refuse another retry
AND require model revision.
```

The DSC provides:

* low cost;
* replayability;
* testability;
* boundedness;
* receipts;
* deterministic outcomes;
* inspectable policy.

### 7.3 Crystallization

The maturation loop is:

```text
Observed state
    v
DSC evaluates known predicates
    v
Bounded action or classification
    v
Receipt and outcome
    v
FSC reviews anomalies
    v
FSC proposes a richer model
    v
Adjudicator tests and recommends admission or rejection under the
governing authority
    v
New DSC capability
```

The FSC remains available as semantic scout and model critic. The DSC progressively absorbs stabilized understanding.

## 8. Self-Bootstrapping Constitutional Exigence

A constitutional Exigence model bootstraps itself when the adequacy of its own model becomes an object of Exigence.

A naive system may begin with:

```text
Task
Priority
Due date
Assignee
```

It then observes residual failures:

* high-priority work remains unresolved;
* low-priority prerequisites block entire projects;
* agents repeat failed strategies;
* authority gaps appear as performance failures;
* rest is ignored;
* alert volume destroys attention;
* context retrieval repeatedly includes irrelevant material.

These unexplained residuals create a meta-Exigence:

```text
The current model cannot adequately explain
or govern observed transition failures.
```

The system may then propose:

* separate salience from Exigence;
* introduce custody;
* model authority;
* add refusal states;
* recognize restorative Exigence;
* constrain propagation;
* create pathology detectors;
* distinguish notification from state.

The bootstrap sequence must remain constitutional:

```text
observe
propose
simulate
challenge
adjudicate
admit
activate
monitor
rollback
```

The model may identify the need for its own growth. It may not self-ratify the resulting authority.

What this offers the naive model is structured self-transcendence without uncontrolled self-modification.

## 9. Context Compilation

Context compilation for an LLM call is fundamentally an attention-allocation problem.

The compiler must determine:

> Which parts of the available world presently bear on the next admissible transition?

Similarity and recency are insufficient. A semantically similar artifact may be obsolete. A constitutionally controlling rule may be lexically distant. A resolved historical issue may pollute the call. A current refusal receipt may be indispensable.

An Exigence-aware context compiler can assign roles such as:

```text
CONSTITUTION
ACTIVE_OBJECT
CURRENT_EXIGENCE
CUSTODY
BLOCKING_ARTIFACT
AUTHORITY
RECENT_RECEIPT
RIVAL_HYPOTHESIS
RESOLVED_HISTORY
BACKGROUND
```

It can then apply policies such as:

```text
Always include:
Controlling constitutional rules.
Active custody.
Current refusal conditions.
Critical fresh observations.
Relevant terminal receipts.

Include when budget permits:
Historical explanation.
Analogous cases.
Secondary preferences.

Exclude:
Superseded instructions.
Resolved transient states.
Untrusted claims.
Inactive high-similarity material.
```

### 9.1 Fidelity Allocation

Exigence can also govern representation fidelity.

```text
Red object:
Full state, evidence, and receipts.

Yellow object:
Structured summary.

Green object:
Identifier, compact state, and retrieval pointer.

Dormant object:
Excluded.
```

This parallels notification policy.

A household task may remain modeled but absent from the current context. A release authority chain may receive full fidelity even if it is not the most recent text.

### 9.2 Context Compilation Receipts

Before each call, the system may emit:

```text
CONTEXT COMPILATION RECEIPT

Target transition:
Repair authorization failure.

Included:
Active failure receipt.
Authority contract.
Current implementation region.
Previous failed strategy.

Compressed:
Roadmap.
Historical architecture notes.

Excluded:
Unrelated UI discussion.

Reason:
Token budget allocated by admitted Exigence policy.
```

This makes model context inspectable and contestable.

### 9.3 Meaning-Base and Crystal-Context Integration

An Exigence-aware compiler requires a governed semantic substrate. The CMB/Hyperpedia layer supplies source-bound concepts, relations, disputes, evidence, and standing; the compiler produces a bounded crystal context capsule for a specific target transition. The capsule should bind:

* target transition and current Exigence claim;
* controlling specification and configuration;
* included source regions and semantic entries;
* exclusions and compression losses;
* unresolved conflicts and explicit ignorance;
* authority and expiry boundary; and
* receipt and revision pointers.

The Crystal Network can distribute candidate observations, Exigence claims, evidence, or context components, but each receiving jurisdiction re-evaluates standing. Network propagation is not attention entitlement and does not create authority by repetition.

## 10. AOK Workspace

AOK Workspace is one application profile in which the Cognitive Kernel could support a unified operational environment; it is not the definition of the kernel.

### 10.1 Exigence Map

The workspace can show:

* rising objects;
* silent green objects;
* active yellow objects;
* interrupt-eligible red objects;
* blocked Exigencies;
* propagation paths;
* missing custodians;
* custody without sufficiency;
* authority congestion;
* model inadequacy.

### 10.2 Quiet-State Computing

Most software treats modeled state as notification material.

The Cognitive Kernel permits:

```text
Green:
Tracked but silent.

Yellow:
Visible but non-interrupting.

Red:
Eligible for interruption.

Blue:
Waiting on an external condition.

Purple:
Requires judgment.

Black:
Execution prohibited.
```

The exact colors are presentation policy, not ontology. The deeper distinction is between state, Exigence, visibility, and effect.

### 10.3 Attention Budgets

Attention can be governed as a scarce resource.

Examples include:

* maximum number of active red objects;
* protected focus periods;
* sleep and family-time suppression;
* override classes;
* maximum routine notifications;
* context-token budgets;
* agent invocation budgets;
* escalation limits.

### 10.4 Agent Routing

The kernel can route work by structure:

```text
Known deterministic case:
DSC worker.

High ambiguity:
FSC semantic agent.

Authority conflict:
Governor.

Execution-ready transition:
Executor.

Persistent anomaly:
Steward review.

Novel topology:
Foundry process.

Disputed standing:
Authorized adjudication path.
```

### 10.5 Lawful Refusal

A human or agent can refuse by citing:

* missing authority;
* missing artifact;
* insufficient evidence;
* policy conflict;
* stale authorization;
* unsafe topology;
* capability deficit;
* unresolved rival interpretation.

The refusal becomes a new governed object rather than a dead end.

### 10.6 Idle Reflection

Idle compute can investigate:

* recurrent deferrals;
* unexplained Exigence;
* stale custody;
* hidden prerequisites;
* model pathology;
* FSC-to-DSC crystallization opportunities;
* context compilation failures;
* repeated user corrections;
* institutional bottlenecks.

All findings remain inspectable hypotheses rather than hidden personality judgments.

## 11. Household and Personal Coordination

The Cognitive Kernel can support ordinary life without turning it into an oppressive optimization system.

A bill may be modeled as:

```text
Green:
Received, due in more than ten days.
Tracked but silent.

Yellow:
Due within ten days.
Visible in upcoming work.

Red:
Due within three days,
autopay failed,
or balance appears insufficient.
```

If payment is blocked:

```text
Derived Exigence:
Resolve account lock,
transfer funds,
or contact provider.
```

A household maintenance object may combine:

* elapsed time;
* visible condition;
* expected guests;
* available supplies;
* current capacity;
* care or hygiene standing;
* opportunity windows.

Rest can also possess standing.

It should not be modeled solely as a productivity input. Sleep, health care, social connection, hygiene, exercise, and recovery are legitimate human realities. A constitutional policy for human work should not optimize throughput at the expense of the person.

The system should be able to conclude:

```text
No acute admitted Exigence requires interruption.

Rest is presently admissible and warranted.
```

## 12. Institutional Modeling

Institutions can be represented as governed transition systems containing:

* roles;
* authorities;
* claims;
* standing;
* custody;
* obligations;
* artifacts;
* procedures;
* Exigencies;
* receipts;
* appeals;
* outcomes.

### 12.1 Administrative Systems

Consider a permit application.

```text
Current state:
Awaiting structural review.

Custody:
Engineering department.

Exigence:
High.

Reasons:
Statutory review period nearing limit.
Construction financing window closing.

Blocker:
Soil report absent.
```

The actionable Exigence may sit with the applicant or an external professional responsible for the report. The department may retain review custody while lacking sufficiency to proceed.

This avoids falsely classifying every delay as departmental negligence.

### 12.2 Government Queues

Public systems may distinguish:

* legal deadlines;
* severity of harm;
* reversibility;
* vulnerable populations;
* availability of alternatives;
* emergency status;
* public safety;
* constitutional rights;
* evidentiary confidence.

A queue should not necessarily be governed by arrival time alone.

### 12.3 Courts

Courts already reason about forms of Exigence when evaluating interim relief, irreparable harm, jurisdiction, standing, evidentiary sufficiency, and procedural timing.

A formal model could expose:

* alleged harm;
* propagation path;
* reversibility;
* uncertainty;
* authority to intervene;
* harm created by intervention;
* duration of temporary standing;
* required revalidation.

### 12.4 Governments

A government can publish distinct Epistemic Positions rather than collapsing all interpretation into one voice.

Possible projections include:

* executive position;
* opposition position;
* fiscal analysis;
* judicial position;
* scientific advisory position;
* local government position;
* affected-community position.

The system can preserve disagreement while still adjudicating action.

### 12.5 Institutional Pathologies

The Cognitive Kernel can expose:

**Authority congestion**
Many high-Exigence transitions converge on one approver.

**Custody orphaning**
An important object has no present custodian.

**Phantom delegation**
A task is assigned, but authority and artifacts remain elsewhere.

**Epistemic monopoly**
Only one role may interpret evidence.

**Notification inflation**
Everything is made acute.

**Institutional avoidance**
Visible short-term work repeatedly displaces maintenance, safety, or low-salience claims.

**Policy staleness**
Executors enforce rules based on conditions that no longer hold.

These are structural findings, not moral verdicts.

## 13. Computing Domains

### 13.1 Operating Systems

The kernel can describe:

```text
Observation:
Device buffer nearing overflow.

Salience:
Interrupt raised.

Exigence:
Service device before data loss.

Attention:
CPU time allocated.

Custody:
Driver.

Sufficiency:
Required lock available.

Policy:
Real-time service outranks background work.

Execution:
Drain buffer.

Receipt:
Operation completed.

Outcome:
Buffer restored to safe range.
```

This provides semantic governance above ordinary scheduler mechanics.

### 13.2 Distributed Systems

A failed replica may be salient but low Exigence if redundancy remains healthy. A subtle checksum discrepancy may have low salience but high integrity Exigence.

The system can distinguish:

* service impact;
* quorum risk;
* repair opportunity;
* replication debt;
* authority to reconfigure;
* evidence freshness;
* propagation scope.

### 13.3 Security and Integrity

Urgency is frequently used to bypass controls.

The Cognitive Kernel can refuse:

```text
High Exigence asserted.
Standing absent.
Provenance absent.
Execution denied.
```

Receipt-before-effect prevents manufactured salience or urgency from becoming execution authority.

### 13.4 Databases

Relevant Exigencies include:

* transaction contention;
* replication lag;
* backup freshness;
* schema migration;
* integrity repair;
* storage exhaustion;
* query latency;
* recovery readiness.

The model can represent consequences and dependencies rather than only resource cost.

### 13.5 Robotics

A robot may observe unexpected resistance while moving an object.

```text
Observation:
Force exceeds expected range.

Epistemic Position:
Object may be obstructed or fragile.

Exigence:
Resolve environment uncertainty.

Policy:
Preserve safety before task completion.

Authorization:
Continued force revoked.

Execution:
Release force and inspect.

Receipt:
Motion halted.

Outcome:
No damage detected.
```

### 13.6 Autonomous Vehicles

The Steward may maintain a rich environmental interpretation. The Governor admits driving policy. The Executor applies minimal, fresh predicates.

```text
Do not accelerate from zero
when trusted front distance is below threshold.
```

This separation permits semantic richness without bloating the effect gate.

## 14. Games and Simulated Societies

Video games provide a compelling demonstration because they continuously model what matters to characters, factions, players, and worlds.

Older simulation-heavy role-playing games introduced day and night cycles, schedules, work routines, and local pathing. These systems created the appearance of inhabited worlds, but their agents often remained trapped in brittle local rules. Two guards meeting in a narrow passage might repeatedly demand that the other stand aside because each possessed a rule without a higher-order account of congestion, alternative action, custody, social convention, or escalating model failure.

The Cognitive Kernel offers a way beyond scripted routine.

### 14.1 Characters as Governed Agents

A character may possess:

* identity;
* occupation;
* commitments;
* relationships;
* values;
* observations;
* Epistemic Positions;
* Exigencies;
* custody;
* capabilities;
* fatigue;
* resources;
* authority;
* memory;
* policy ordering.

Personality can be modeled not merely as adjectives but as stable tendencies in adjudicating competing Exigencies.

A guard may place public safety before self-preservation.

A mercenary may place contract and payment before civic duty.

A healer may prioritize care.

A fanatic may elevate one mission above nearly all competing claims.

The same world state can therefore produce different lawful interpretations and actions.

### 14.2 Emergent Social Pressure

Suppose a bakery catches fire.

The event propagates differently:

* the baker experiences livelihood and family Exigence;
* nearby guards acquire public-safety custody;
* healers prepare for injury;
* water carriers gain suppression work;
* officials acquire coordination obligations;
* merchants anticipate supply disruption;
* thieves perceive opportunity;
* children seek safety.

The event is not merely a scripted quest trigger. It changes the graph.

### 14.3 Schedules Become Default Policies

Schedules remain useful but should become defeasible defaults.

```text
08:00 Open shop.
12:00 Eat.
18:00 Visit tavern.
22:00 Sleep.
```

A fire, missing child, arrest order, injury, blocked road, or urgent obligation may lawfully override routine.

This yields characters who maintain life patterns without being imprisoned by them.

### 14.4 LLM Gap Stitching

Deterministic machinery can handle:

* pathing;
* ownership;
* inventories;
* schedules;
* money;
* authority;
* custody;
* combat rules;
* physical state;
* institutional procedures.

LLM calls can activate when the simulation encounters semantic gaps:

* novel negotiation;
* ambiguous social conflict;
* improvised planning;
* explanation;
* dialogue;
* rumor interpretation;
* institutional argument;
* unusual composite events.

The FSC interprets the novel case. Stable results may later crystallize into DSC rules.

### 14.5 Event-Driven Cognition

Large societies need not simulate every character continuously.

A sleeping farmer with no local change may remain dormant.

A nearby attack, weather shift, market disruption, death, order, or family event awakens relevant graph regions.

Exigence localizes computation.

This permits very large populations with selective semantic depth.

### 14.6 Institutions in Games

Guilds, courts, armies, churches, markets, and governments can use the same kernel.

A king differs from a stable worker not because the king uses a different cognitive architecture, but because the king possesses wider authority, custody, visibility, and institutional dependencies.

Bureaucracy becomes simulated rather than decorative.

Tax failures may delay repairs. Delayed repairs may degrade bridges. Trade may slow. Prices may rise. Crime may increase. Military readiness may fall.

The resulting history emerges from connected receipts.

### 14.7 Inspectable History

A simulation can be paused and queried:

* Why did this town decline?
* Why did the captain refuse promotion?
* Why did the famine spread?
* Which authority bottleneck caused the uprising?
* Which policy repeatedly suppressed maintenance?
* Why did two neighboring settlements diverge?

The answer can be reconstructed from observation, interpretation, Exigence, custody, policy, execution, and outcome receipts.

Games thereby become scientifically inspectable social simulations.

### 14.8 Player-Facing Projection

The same world state can be projected differently:

```text
Green:
Simulated but not shown.

Yellow:
Visible in journal or map.

Red:
Eligible for HUD interruption.

Black:
Action prohibited.

Blue:
Waiting on external state.

Purple:
Requires player judgment.
```

This reduces quest-log overload while preserving a living world.

### 14.9 Emergent Narrative

Narrative selection can ask:

> Which unresolved state has accumulated sufficient Exigence to call for a scene?

Promises, betrayals, grief, political tension, hidden identity, institutional failure, and social debt can all accumulate transition pressure.

A scene occurs because the world has become unstable in its present form, not merely because a timer fired.

## 15. General Society Modeling

The Cognitive Kernel can support simulations containing hundreds, thousands, or millions of agents.

Each agent need not possess continuous human-level cognition. Most behavior can arise from:

* deterministic routines;
* local policies;
* event-driven reevaluation;
* bounded world models;
* role-specific standing;
* typed Exigence;
* selective FSC invocation;
* receipted memory.

Such systems could model:

* cities;
* firms;
* armies;
* courts;
* families;
* markets;
* schools;
* political movements;
* religious institutions;
* supply networks;
* online communities;
* disaster response;
* robot swarms.

The purpose is not necessarily predictive social science. It may be exploratory, educational, adversarial, artistic, or institutional.

The critical advantage is inspectability. Outcomes can be explained through the same kernel that produced them.

## 16. Anti-Goodhart Constraints

Exigence must not become another target score.

Optimizing directly for "low Exigence" could incentivize:

* hiding work;
* suppressing observations;
* closing objects dishonestly;
* transferring custody without support;
* lowering thresholds;
* fragmenting tasks;
* ignoring slow risks;
* manufacturing green status.

The governing principle should be:

> Unresolved Exigence should increase understanding before increasing pressure.

The system should optimize neither maximum urgency nor minimum visible backlog. It should seek healthy Exigence flow:

* accurate recognition;
* lawful ordering;
* adequate custody;
* sufficient support;
* bounded transition;
* honest receipt;
* model repair;
* legitimate rest.

For machines, aggressive execution optimization may be appropriate within policy.

For humans, optimization must preserve dignity, autonomy, health, recovery, and the right to refuse.

### 16.1 Human-Sovereignty and Institutional Limits

No Exigence model should infer human obligation merely from observability, predicted benefit, institutional demand, or repeated notification. In human-facing systems, detectability, refusal, renegotiation, privacy, explanation, appeal, and exit are non-substitutable constraints. A household or workplace profile must permit the person to reject the model's interpretation, suppress non-safety projections, inspect what produced an escalation, and prevent latent personality or psychiatric judgments from acquiring standing.

Institutional use adds further limits: unequal data visibility, power asymmetry, strategic reporting, missing affected communities, and contested values can make a topologically coherent Exigence map politically or morally illegitimate. The kernel can expose a decision structure; it cannot manufacture democratic, legal, clinical, or moral authority.

## 17. A General Object Model

A mature governed object may contain:

```text
GovernedObject {
    identity
    state
    observations[]
    salience_events[]
    epistemic_positions[]
    exigence_claims[]
    admitted_exigence
    standing
    attention_policy
    custody
    sufficiency
    constraints
    candidate_transitions[]
    authorizations[]
    execution_attempts[]
    receipts[]
    outcomes[]
    presentation_policies[]
    model_repair_history[]
}
```

An Exigence representation should likely be typed rather than scalar.

Possible dimensions include:

* safety;
* dependency;
* temporal;
* maintenance;
* constitutional;
* care;
* restorative;
* opportunity;
* integrity;
* social;
* economic;
* epistemic;
* environmental.

The resulting structure may support partial ordering rather than forcing all conditions into one universal rank.

## Need-to-Attention-to-Custody Control Loop

Across the completed P1 corpus, Exigence and the Cognitive Kernel (CogK) has one sharp role: it is the **need-to-attention-to-custody control loop** that governs when a perceived pressure becomes recognized work, receives resources, reaches sufficiency, or terminates. It does not convert urgency into authority, salience into truth, custody into ownership, or an attention decision into permission to effect change.

- **Adjacent work:** *The Well-Governed Mind*  
  **Supplies:** The larger architecture of cognitive governance and self-revision.  
  **CogK boundary:** CogK supplies the control loop from observation through work and outcome.

- **Adjacent work:** *Technical Brief: Recursive Semantic Orientation and Complex Systems Cognition*  
  **Supplies:** The revisable investigation state, probes, countermodels, and stopping.  
  **CogK boundary:** RSO is an investigation method that CogK may schedule and reassess.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Responsibility, transfer, return, and terminal disposition for exact work.  
  **CogK boundary:** CogK identifies and prioritizes work; custody defines who must advance or disposition it.

- **Adjacent work:** *A Constitution for the Context Window*  
  **Supplies:** Constitutional construction of invocation context.  
  **CogK boundary:** CogK can request context and set attention goals but cannot bypass context admission.

- **Adjacent work:** *A Cognitive ABI for Capability-Centered Computing*  
  **Supplies:** Contracts, qualification, routing, and substitution for cognitive and effect capabilities.  
  **CogK boundary:** CogK calls capabilities through the ABI; attention is not eligibility or authority.

A kernel cycle should bind:

$$
\begin{aligned}
K= (&observation, salience, epistemic\_position, exigence, \\
&standing, attention, custody, sufficiency, policy, \\
&authorization, execution, outcome, receipt)
\end{aligned}.
$$

Every arrow is defeasible. An observation may be wrong; salience may be manipulated; an exigence claim may be rejected; standing may be bounded; attention may be deferred; custody may transfer; sufficiency may fail; policy may refuse; authorization may expire; execution may diverge; and a receipt may establish less than the outcome claimed.

Pathological topologies must remain observable: fixation, avoidance, inflation, suppression, fragmentation, over-propagation, and staleness. Reducing the number of visible exigencies is not success if the system hides, transfers, or prematurely closes work. Quiet-state computing is legitimate only when open obligations, deadlines, risks, and custody are still represented.

The universal GSM can type `OBSERVED_AS`, `SALIENCE_ASSIGNED`, `CLAIMS_EXIGENCE`,  
`HAS_EPISTEMIC_STANDING`, `ALLOCATED_ATTENTION`, `CUSTODIED_BY`, `SUFFICIENT_FOR`,  
`GOVERNED_BY_POLICY`, `AUTHORIZED_FOR`, `EXECUTED_AS`, `RESULTED_IN`, `RECEIPTED_BY`,  
and   
`PATHOLOGICALLY_PROPAGATES_TO`. Source-native AOK application examples remain illustrations and do not enter the Ableman corpus as current system identity or standing through this integration.

This integration establishes four editorial commitments: adopt need-to-attention-to-custody loop as CogK's official corpus role; adopt the kernel-cycle object; require explicit defeasibility at every transition; and preserve quiet state as an accountable posture rather than absence of visible work.

## Evidence-Seeking Exigence and Authority-Safe Transition

The fixed-seed comparison with Continuation Primacy, governed retrieval, Authority Laundering Theory, and Governance as Compilation expands the Cognitive Kernel from an attention loop into a bounded evidence-to-transition interface:

$$
\begin{aligned}
K^*= (&observation, exigence, purpose, retrieval, evidence, \\
&continuation\_options, attention, custody, \\
&stage\_contract, authority, execution, outcome, \\
&reconsideration)
\end{aligned}.
$$

Governed retrieval can answer a CogK knowledge need, but retrieval rank, citation, institutional label, and repeated use do not create authority. Continuation Primacy supplies an option-classification lens over reachable, admissible, viable, preferred, and terminal trajectories; it does not dictate persistence or termination.

Authority Laundering analysis tests whether felt urgency, allocated attention, custody, retrieved evidence, or organizational position is being promoted into normative warrant without a valid authority path. Governance as Compilation can carry an admitted proposal through typed stages with explicit input, output, loss, remainder, review, and refusal obligations.

The universal GSM can type   
`TRIGGERS_EVIDENCE_SEEKING`, `RETRIEVES_UNDER_PURPOSE`,  
`CLASSIFIES_CONTINUATION_OPTIONS`, `AUDITS_EXIGENCE_AUTHORITY`,  
`COMPILES_ADMITTED_TRANSITION`, `PRESERVES_UNRESOLVED_REMAINDER`,  
and   
`RECONSIDERS_AFTER_OUTCOME`.

In a realization-funnel context, IC may mean Instance Constitution or Instance Configuration, and IR may mean Instance Realization or Implementation Realization. These interchangeable expansions do not turn the Cognitive Kernel into an implementation or authorize an effect.

This randomized review establishes four editorial commitments: adopt the evidence-seeking kernel cycle; integrate continuation as an option lens; require anti-laundering review of urgency, attention, and retrieved authority; and define a typed compilation handoff for admitted transitions.

## A Defeasible Need-to-Transition Scheduler

Eight retained downstream uses place the Cognitive Kernel beside capability routing, context compilation, authority-laundering analysis, context lifecycle, continuation options, staged governance compilation, governed retrieval, and the pedagogical custody surface. They confirm a defeasible need-to-attention-to-custody scheduler: it determines what presently calls for transition and how the call is processed, not what is true or what may be done.

$$
\begin{aligned}
K^*= (&observation, source, salience, epistemic\_position, \\
&exigence, purpose, standing, continuation\_options, \\
&attention, custody, sufficiency, policy, capability, \\
&authorization, execution, outcome, reconsideration, \\
&receipt, expiry)
\end{aligned}.
$$

Every transition may refuse, defer, narrow, transfer, expire, or reopen. Pressure is not authority; urgency is not priority; salience is not truth; attention is not custody; custody is not capability; sufficiency is not authorization; execution is not successful outcome. Evidence seeking must preserve purpose, source standing, cost, alternatives, and stopping.

Fixation, avoidance, inflation, suppression, fragmentation, over-propagation, and staleness are graph and policy pathologies rather than mere scalar extremes. Quiet state is legitimate only when open obligations, latent risk, leases, deadlines, and recovery remain queryable. A scheduler that minimizes visible exigence by hiding work has failed.

The universal GSM can type   
`OBSERVES_FOR_EXIGENCE`, `CLAIMS_NEED_FOR_TRANSITION`,  
`CLASSIFIES_CONTINUATION_OPTION`, `ALLOCATES_ATTENTION`, `ASSIGNS_NEXT_MOVE_CUSTODY`,  
`TESTS_SUFFICIENCY`, `QUALIFIES_CAPABILITY`, `AUTHORIZES_TRANSITION_SEPARATELY`,  
`RECONSIDERS_AFTER_OUTCOME`, and   
`EXPIRES_EXIGENCE_CLAIM`.

This review establishes four editorial commitments: adopt the complete defeasible scheduler record; preserve every non-substitution boundary; type pathological topology and accountable quiet state; and require purpose-bound evidence seeking, capability qualification, independent authorization, expiry, outcome review, and reconsideration.

## Need Does Not Confer Authority

### Public orientation

Exigence names a graph-derived reason to consider transition: a mismatch, risk, opportunity, obligation, or unresolved condition becomes significant enough to demand attention. The Cognitive Kernel separates observation, belief, salience, recognition, actionability, authority, execution, and learning so urgency cannot silently become permission.

### Adversarial tests

1. **Urgency-inflation attack.** A system raises salience to bypass ordinary review. Exigence intensity and authority remain separate.
2. **Suppression attack.** Institutionally inconvenient needs never reach attention. Detection coverage, dissent, and appeal need explicit paths.
3. **False-belief attack.** An erroneous model generates a coherent but spurious exigence. Evidence, uncertainty, and countermodels must travel with the proposal.
4. **Fixation attack.** One unresolved need monopolizes attention despite low marginal progress. Budgets, reconsideration, and competing obligations are required.
5. **Fragmentation attack.** Related signals are handled independently so no systemic need is recognized. Aggregation must preserve source and uncertainty.
6. **Over-propagation attack.** A local issue is generalized across domains, people, or institutions. Scope and jurisdiction must constrain propagation.
7. **Authority-leap attack.** Recognition of need becomes authorization to execute. Mandate, capability, effect grant, and adjudication remain independent gates.
8. **Human-pathology projection.** Computational integrity topologies are used to diagnose or control people. The paper prohibits clinical and person-level inference.

### Claim and evidence ceiling

The paper contributes a computational scheduler and control-loop vocabulary. It does not establish a psychological theory, clinical model, complete account of motivation, or validated model of society. General-society examples are analogical research surfaces, not authorization for institutional deployment.

Claims about human cognition, mental health, organizations, public policy, or social behavior require current external evidence, affected-party analysis, and qualified domain review. Internal corpus integration cannot validate these transfers. No external research was added in this pass.

### Reader-facing consequence

The accessible insight is that noticing a problem, believing it matters, deciding it is actionable, possessing authority, and actually intervening are different transitions. A safe agent must preserve those differences even under pressure.

## 18. Theoretical Consequence

The Cognitive Kernel distinguishes four forms of computation that are often collapsed:

```text
Descriptive computation:
What is happening?

Epistemic computation:
What may it mean?

Constitutional computation:
Which meanings, claims, and needs have standing?

Executive computation:
What may happen next?
```

Exigence sits between interpretation and authorized transition.

It states:

> Given the admitted model of reality, this state presently calls for change.

It does not, by itself, determine:

* whether the call is legitimate;
* whether it may interrupt;
* who must answer;
* what response is lawful;
* whether sufficient conditions exist;
* whether execution remains safe;
* whether the resulting outcome is successful.

Those questions belong to the rest of the kernel.

### 18.1 Realization Funnel

- **Stage:** Possibility  
  **Cognitive-Kernel work:** A system may model what calls for transition without collapsing pressure into authority.  
  **Current standing:** Conceptual possibility.

- **Stage:** Specification  
  **Cognitive-Kernel work:** Define observations, interpretations, Exigence claims, standing, attention, custody, sufficiency, policy, authorization, execution, receipts, and outcomes.  
  **Current standing:** Candidate specification.

- **Stage:** CM1  
  **Cognitive-Kernel work:** Enumerate vector, graph, rule-based, probabilistic, human-reviewed, centralized, distributed, safe, unsafe, coercive, and minimal realizations.  
  **Current standing:** Partially explored.

- **Stage:** CM2  
  **Cognitive-Kernel work:** Prefer non-scalar, inspectable, source-bound, contestable, quiet-by-default, APD-compatible, and failure-aware configurations.  
  **Current standing:** Preference criteria proposed.

- **Stage:** Instance Configuration  
  **Cognitive-Kernel work:** Fix a domain, ontology, authorities, evidence, propagation rules, budgets, thresholds, rights, threat model, and stopping rules.  
  **Current standing:** Not fixed by this paper.

- **Stage:** Implementation Realization  
  **Cognitive-Kernel work:** Build one configured kernel, compiler, workspace, simulation, or control system.  
  **Current standing:** Examples and profiles only; no universal implementation standing.

- **Stage:** Evidence  
  **Cognitive-Kernel work:** Run replay, adversarial salience, false-positive/negative, propagation, orphaned-effect, human-impact, and cost tests.  
  **Current standing:** Required and incomplete.

- **Stage:** Revision  
  **Cognitive-Kernel work:** Amend models and policies while preserving prior claims, receipts, harms, and dependent decisions.  
  **Current standing:** Required loop.

The paper therefore reaches a detailed Specification with CM1 and CM2 guidance. Its domain examples do not establish validated Instance Configurations.

### 18.2 Counterevidence and Falsification

The proposal is weakened if Exigence cannot be distinguished reliably from priority, urgency, salience, or utility; if propagation adds no explanatory or operational value; if the kernel produces more coercion or alert load than the systems it replaces; if a scalar score reappears implicitly through policy; if receipts fail to reconstruct why attention or authority moved; if humans cannot contest inferred needs; or if simpler domain-specific state machines perform equally well with fewer governance costs.

Evidence should include negative and null cases, not only demonstrations in which the proposed taxonomy fits. Social simulations, households, institutions, robotics, and autonomous vehicles require separate validation and cannot borrow standing from one another.

## 19. Conclusion

Exigence provides a computational account of what presently matters for transition.

The Cognitive Kernel places that account inside a governed architecture that separates observation from interpretation, significance from salience, standing from assertion, attention from importance, custody from capability, authorization from execution, and receipt from outcome.

This separation supports systems that can:

* remain quiet when states are healthy;
* surface rising conditions without coercion;
* redirect blocked work toward missing prerequisites;
* diagnose structural rather than merely personal failure;
* detect pathological execution topologies;
* refuse lawfully before effect;
* compile LLM context by live need;
* route work among semantic and deterministic agents;
* model institutions and governments;
* coordinate households and workplaces;
* govern autonomous machines;
* simulate societies and histories;
* progressively crystallize semantic understanding into deterministic rules;
* identify when their own models have become inadequate.

The deepest contribution is not a better priority system.

It is a model of how a governed system moves from reality to action without treating notice as truth, pressure as authority, or execution as success.

The Cognitive Kernel asks:

```text
What happened?

What might it mean?

What now calls for transition?

Which claim has standing?

What deserves attention?

Who holds the next move?

What is missing?

What is lawful?

What may execute now?

What was refused or performed?

What actually changed?

What must the system learn?
```

A system capable of answering these questions is no longer merely processing tasks. It is maintaining an inspectable relationship between world, meaning, need, authority, action, and consequence.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that computational systems routinely model tasks, priorities, deadlines, permissions, attention, and action, but they rarely possess a unified account of why a particular state presently calls for transition. Its nearest external comparison fields are security, ai, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E2]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E3]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

**[E4]** Robert N. M. Watson, Simon W. Moore, Peter Sewell, and Peter G. Neumann. *An Introduction to CHERI*. University of Cambridge Technical Report UCAM-CL-TR-941, 2019. DOI: 10.48456/tr-941. [cl.cam.ac.uk source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-941.html) **Relationship:** Adjacent capability architecture demonstrating unforgeable hardware authority and compartmentalization.

**[E5]** Patrick Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **Relationship:** Predecessor retrieval architecture; comparison centers on provenance, admission, and fail-closed constraints not supplied by retrieval alone.

**[E6]** Shunyu Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. arXiv:2210.03629. https://arxiv.org/abs/2210.03629 **Relationship:** Predecessor agent pattern for interleaving reasoning and action; used to distinguish action traces from governed effects.

**[E7]** Elham Tabassi. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1, 2023. DOI: 10.6028/NIST.AI.100-1. https://doi.org/10.6028/NIST.AI.100-1 **Relationship:** Adjacent risk-management framework used to test whether the paper operationalizes governance beyond voluntary process guidance.

### Ableman corpus

**[A1]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *The Integrity Enforcement Layer*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-505307E9E6571B63`;  
source SHA-256  
`F858AB32E0937B796353CAE573DD4183FDF4F179A3E1E7E40C4E0C6BF1AB0018`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Constitutional Syscalls*. Ableman Corpus current edition; work identity `PAPER.PUB.18737229`;  
source SHA-256  
`5F14356180812262778F8574C292F4F6B560993042E5358B02EAB9CF0F7DE14C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *CARA: Constrained Artificial Reasoning Architecture*. Ableman Corpus current edition; work identity `PAPER.PUB.18099715`;  
source SHA-256  
`F8F74F0CD58F5414D9A29EBE958E49751892D07A028CB51197F8201B18AAB40E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *A Constitution for the Context Window*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-CF26BA0E123F472F`;  
source SHA-256  
`60395402368E146F115CCE53D0E5A15B8FB23C90ED5B24CA92AB8515B2009965`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Adam Ableman. *Constitutional Computation*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20624488.

Adam Ableman. *Ableman's Razor: A Typed Grammar for Ontology Exploration, Configuration Collapse, and Implementation Feedback*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18113475.

Adam Ableman. *Epistemic Situational Awareness (ESA): Continuation Governance for Frontier AI Systems*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18123102.

Adam Ableman. *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18453681.

Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18601631.

Adam Ableman. *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18633797.

Adam Ableman. *Effect Sovereignty: System Calls as the Constitutional Interface for Reality-Touching Effects*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18737323.

Adam Ableman. *Semantic Custody*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20300952.

Adam Ableman. *Semantic Crystallization*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20310115.

Adam Ableman. *Reasoning by Way of Receipts*. Authorized Ableman Corpus current edition; canonical concept standing remains governed separately from publication.

External sources are still required for the paper's comparisons to attention theory, scheduling, human factors, psychiatric and cognitive literature, Goodhart effects, institutional decision-making, operating systems, distributed systems, robotics, autonomous vehicles, and simulation research. Those claims remain design analogies and research hypotheses until a source-by-source review is completed.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *Semantic Crystallization.* Zenodo, 2026. doi:10.5281/zenodo.20310115

Adam Ableman *Ableman's Razor: A Typed Grammar for Ontology Exploration, Configuration Collapse, and Implementation Feedback.* Zenodo, 2026. doi:10.5281/zenodo.18113475

Adam Ableman *Effect Sovereignty: System Calls as the Constitutional Interface for Reality-Touching Effects.* Zenodo, 2026. doi:10.5281/zenodo.18737323

Adam Ableman *Epistemic Situational Awareness (ESA): Continuation Governance for Frontier AI Systems.* Zenodo, 2026. doi:10.5281/zenodo.18123102

Adam Ableman *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI.* Zenodo, 2026. doi:10.5281/zenodo.18633797

Adam Ableman *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality.* Zenodo, 2026. doi:10.5281/zenodo.18601631

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847744](https://doi.org/10.5281/zenodo.23847744)
