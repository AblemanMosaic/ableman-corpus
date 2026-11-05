# Who Has the Ball?

## Work Custody as a Primitive of Human-Agent Collaboration

### Yet they routinely fail to answer one of the simplest operational questions: Who has the ball?

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern collaboration systems successfully model many aspects of cooperative work, including projects, documents, conversations, tasks, ownership, permissions, workflows, and automation. Yet they routinely fail to answer one of the simplest operational questions:

> **Who has the ball?**

This question is deceptively fundamental. It does not ask who owns a project, who is accountable for an outcome, who was originally assigned a task, or who possesses authority over a resource. Rather, it asks who currently holds the live responsibility, context, and expectation to advance a particular unit of work.

Existing collaboration systems approximate this concept through fragmented mechanisms such as assignees, ownership fields, Kanban cards, RACI matrices, incident handoffs, or chain-of-custody procedures. However, these mechanisms typically model planning, accountability, or artifact provenance rather than the current possession of responsibility-bearing work.

This paper proposes **Work Custody** as a first-class primitive of collaboration. Work Custody is a temporally bounded constitutional relation describing which participant or execution role presently holds an accepted, scoped obligation to advance a work object, how custody is acquired and transferred, and how the collaboration system maintains shared queryable recognition among authorized participants. The record does not itself confer capability, authority, accountability, or moral or legal responsibility.

The proposed protocol grammar can be used across human-human, human-agent, and agent-agent collaboration, while participant type, capability, authority, accountability, and legal or moral responsibility remain distinct. It offers a candidate operational primitive for constitutional collaboration environments.

---

## 1. Introduction

Organizations spend extraordinary effort discovering something their software should already know.

Questions such as:

* Who is working on this?
* Who needs to act next?
* Where is this blocked?
* Why has nothing happened for three days?
* Who is waiting on me?
* Who currently owns the next move?

are among the most common questions in engineering, research, medicine, manufacturing, military operations, government, and knowledge work.

Most collaboration tools answer these questions indirectly.

They expose:

* assignments,
* ownership,
* comments,
* timestamps,
* workflow stages,
* tickets,
* chat histories,
* notifications.

Humans then reconstruct current operational reality through meetings, memory, and inference.

This reconstruction is both expensive and error-prone.

The missing abstraction is not another project-management feature.

It is the absence of an explicit model of current operational possession.

---

## 2. The "Ball"

Teams often describe responsibility informally by saying:

> "Alice has the ball."

This phrase carries several meanings simultaneously.

It implies:

* Alice knows she possesses the work.
* Others know Alice possesses the work.
* Alice is expected to advance it.
* The work is not presently waiting on another custodian.
* Responsibility will eventually be transferred.
* The transfer will be observable.

Despite its ubiquity, few collaboration systems model this state directly.

Instead, users infer it from unrelated metadata.

---

## 3. Existing Partial Models

Many existing systems contain fragments of Work Custody.

### 3.1 Assignment

Assignments answer:

> Who should perform this task?

Assignments do not necessarily imply:

* acceptance,
* awareness,
* active responsibility,
* possession,
* transfer,
* current operational state.

---

### 3.2 Ownership

Ownership is generally persistent.

Repositories, documents, or projects may have owners.

Ownership rarely changes during execution.

Custody changes frequently.

---

### 3.3 Accountability

Frameworks such as RACI distinguish responsibility and accountability.

These are planning constructs.

They do not generally model live possession of work.

---

### 3.4 Workflow State

Workflow engines model stage transitions.

They answer:

> What state is this work in?

They often cannot answer:

> Who currently possesses the obligation to move it?

---

### 3.5 Chain of Custody

Evidence handling records every transfer of physical or digital artifacts.

This concept is remarkably close to the proposed model.

However, it protects artifact provenance rather than operational collaboration.

This paper generalizes custody from artifacts to responsibility-bearing work.

---

## 4. Work Custody

We define Work Custody as follows.

**Definition**

Work Custody is a constitutional relation naming the participant or execution role currently expected to attempt, route, monitor, or otherwise advance a scoped work object until custody is transferred, released, completed, expired, revoked, or escalated under declared rules.

Unlike ownership, custody is expected to change.

Unlike assignment, custody requires acceptance.

Unlike authority, custody does not imply unlimited decision rights.

Unlike accountability, custody is operational rather than managerial.

---

## 5. Core Relations

A collaboration system should distinguish at least the following relations.

```text
OWNS

HAS_AUTHORITY

IS_ACCOUNTABLE

HAS_CUSTODY

WAITING_ON

DEPENDS_ON
```

These relations are not interchangeable.

A participant may own an artifact while another participant has authority to approve changes, while a third currently holds custody of today's work.

---

## 6. Custody Lifecycle

Work Custody proceeds through explicit states.

```text
UNASSIGNED -> OFFERED -> ACCEPTED -> ACTIVE_CUSTODY
ACTIVE_CUSTODY -> TRANSFER_PENDING -> ACTIVE_CUSTODY(successor)
ACTIVE_CUSTODY -> RELEASED | COMPLETED | EXPIRED | REVOKED | ESCALATED
```

A transfer may require more than one event. During a pending handoff, the predecessor remains visible, the proposed successor is identified, acceptance is unresolved, and the protocol states who retains active custody. This makes ambiguous and failed handoffs representable rather than assuming that a sent message completed the transfer.

---

## 7. Constitutional Invariants

A collaboration environment adopting Work Custody should satisfy several invariants.

### I. Conditional Exclusive Custody

An atomic active obligation has exactly one active custodian unless joint, replicated, quorum, or partitioned custody is explicitly declared. The work object must be decomposed when different participants hold different advancement obligations.

---

### II. Assignment Does Not Create Custody

Assigning work merely proposes a future custody relationship.

Acceptance is separate.

---

### III. Custody Requires Recognition

Custody exists only after explicit acquisition.

Silent assumptions are insufficient.

---

### IV. Transfer Is Explicit

Custody changes only through recognized transfer events.

---

### V. Shared Queryable Recognition

All authorized collaborators can resolve the current custody record within the disclosure and freshness limits of the workflow. A queryable record improves coordination; it does not by itself prove that every participant noticed or understood the state.

Operational responsibility hidden only inside private mental models defeats the purpose of the representation.

---

### VI. Every Transfer Produces History

Custody transfers become historical records.

Questions such as:

* Who previously held this?
* Why was it transferred?
* How long did each participant hold it?

become mechanically answerable.

---

## 8. Waiting

Work frequently cannot progress because another participant possesses a prerequisite.

Accordingly, Work Custody introduces an additional constitutional relation:

```text
WAITING_ON
```

This relation identifies the external dependency preventing the custodian from advancing work.

This distinction allows the system to differentiate:

"I have the ball."

from

"I have the ball, but someone else must act first."

---

## 9. One Protocol Grammar, Different Kinds of Participants

The custody protocol can address humans, organizations, AI agents, deterministic components, workflow engines, courts, and external services through one typed participant interface. That syntactic symmetry is useful for orchestration, but it must not erase substantive differences.

A human or institution may bear moral, professional, contractual, managerial, or legal responsibility. An AI agent or deterministic component can occupy an operational custody slot only because an authorized constitution treats it as the currently expected executor, router, monitor, or holder of a bounded work lease. The non-human component does not acquire rights, accountability, authority, or standing merely because a database names it as custodian. A court normally adjudicates or qualifies rather than advancing the work itself; an external service participates only for the operations its contract and capabilities actually support.

Accordingly, every custody record should identify the participant kind, capability basis, authority basis, escalation principal, and accountable human or institution where the jurisdiction requires one. Protocol uniformity supports composition. Typed differences prevent responsibility and authority laundering.

Example:

```text
Researcher -> Research Agent -> Validator -> Review Court -> Publisher
```

This line is not one undifferentiated chain of responsibility. The researcher may authorize and remain accountable; the agent may draft; the validator may test; the court may adjudicate a bounded claim; and the publisher may possess a distinct release authority. Each transition must say which work object and obligation moved, which did not, and what acceptance means for the successor.

## 10. Shared Queryable Recognition

The practical contribution is not merely recording custody but making the current record available and intelligible to authorized collaborators. The source called this common operational knowledge. Formal common knowledge is stronger than visibility or queryability: every participant knowing a fact does not necessarily establish that everyone knows that everyone knows it. This paper therefore claims **shared queryable recognition**, not an unproved epistemic fixed point.

At minimum, an authorized collaborator should be able to resolve the current custody record, its freshness, scope, acceptance state, blocking relations, and transfer status without reconstructing chat history. Systems may add notifications, acknowledgements, subscriptions, or quorum rules when a workflow requires stronger awareness. A hidden, stale, partitioned, or access-denied record does not support the same operational claim as a current record witnessed by the affected participants.

The collaboration surface should answer:

> Who has the ball, for which obligation, under what authority, until when, and who must act if the custodian cannot continue?

That longer question exposes the conditions concealed by a bare assignee field.

## 11. Consequences for Collaboration Systems

A system supporting Work Custody can answer questions such as:

* Who currently has the ball?
* Which work has no custodian?
* Which work has ambiguous custody?
* Which work has been idle longest?
* Who is overloaded?
* Who is waiting on me?
* Who am I waiting on?
* Which transfers repeatedly fail?
* Where does work become trapped?

These become simple runtime queries rather than organizational investigations.

---

## 12. Relation to Constitutional Collaboration

Within a constitutional collaboration architecture, Work Custody complements rather than replaces existing primitives.

A work object may simultaneously possess:

* an owner,
* an accountable party,
* authority constraints,
* standing,
* current custodian,
* waiting relations,
* execution receipts.

Separating these concepts reduces ambiguity while making collaborative state machine-checkable.

---

## 13. Discussion

The novelty of Work Custody does not arise from inventing the notion of custody itself.

Evidence handling, emergency management, clinical handoffs, and logistics all contain custody-like concepts.

The contribution is their unification into a domain-independent collaboration primitive governing live responsibility-bearing work.

This synthesis permits collaboration systems to model operational possession with the same precision that version-control systems model source code or databases model transactions.

---

## 14. A Minimal Work-Custody Contract

The paper is the pedagogical entry point; *A Formal Theory of Work Custody* is the technical companion. A minimal record can be represented as:

$$
\kappa=(w,c,m,s,a,e,g,h,x,q),
$$

where $w$ is exact work identity, $c$ the current custodian, $m$ participant and custody mode, $s$ the scoped advancement obligation, $a$ acceptance evidence, $e$ expiry or review condition, $g$ authority basis, $h$ context or handoff-root identity, $x$ current status and blocking relations, and $q$ the escalation or accountability route. This is a candidate schema, not an adopted canonical form.

The governing invariants become more precise:

1. **Identity:** custody applies to an exact work object or declared partition, not a title-shaped approximation.
2. **Acceptance:** offer or assignment alone does not create accepted custody.
3. **Conditional exclusivity:** an atomic active obligation has one custodian unless joint, replicated, quorum, or partitioned custody is explicitly modeled.
4. **Non-laundering:** custody grants no authority, standing, capability, ownership, or accountability not independently present.
5. **Continuity:** while transfer is pending, the protocol states whether the predecessor retains custody, joint custody applies, or an explicit escrow role holds it.
6. **Context sufficiency:** the successor receives or can resolve the information required for the accepted scope; a receipt that proves transfer but omits indispensable context does not prove a usable handoff.
7. **Freshness and liveness:** custody expires, renews, escalates, or becomes visibly stalled under declared rules; it cannot persist silently forever.
8. **Waiting transparency:** `WAITING_ON` names a typed dependency and expected actor or condition without pretending that the current custodian can satisfy it.
9. **Receipt boundary:** a receipt establishes a recorded transition under its witnesses; it does not prove awareness, competence, progress, or successful outcome beyond its evidence.
10. **Recovery:** orphaned, declined, abandoned, revoked, expired, partitioned, or unreachable custody has a declared resolution path.

## 15. Universal GSM and Realization-Funnel Placement

In the universal **Governed Semantic Model (GSM)**, Work Custody is a typed relation among a work identity, participant identity, scoped obligation, acceptance state, authority basis, context root, evidence, time, and revision history. The **Governed Meaning Base (GMB)** is the current name in the author-confirmed `CCF -> CMB -> GMB` lineage. A GMB can preserve custody meanings, records, receipts, and projections; it does not itself assign custody or authorize work.

The complete realization funnel locates the proposal:

$$
\begin{aligned}
&P \\
&\rightarrow S \\
&\rightarrow CM_1 \\
&\rightarrow CM_2 \\
&\rightarrow IC \\
&\rightarrow IR \\
&\rightarrow E \\
&\rightarrow R
\end{aligned}.
$$

**Possibility** contains alternative custody models, modes, and handoff protocols. **Specification** defines work identity, roles, states, transitions, invariants, refusal, expiry, and evidence obligations. **Configuration Manifold 1 (CM1)** contains all custody configurations satisfying mandatory admissibility. **Configuration Manifold 2 (CM2)** selects preferable admissible arrangements under declared objectives such as low coordination burden, clear escalation, privacy, fairness, load, and resilience. **IC** may mean **Instance Constitution** or **Instance Configuration** interchangeably; it binds one workflow's custody rules, participants, clocks, authority, and evidence profile. **IR** may mean **Instance Realization** or **Implementation Realization** interchangeably; it is the actual database, orchestration engine, user interface, notifications, receipts, and agent-runtime behavior. **Evidence** tests whether custody is queryable, accepted, current, useful, and correctly transferred. **Revision** repairs the model when handoffs fail, agents lose context, workload shifts, authority changes, or empirical results contradict the design.

For agentic orchestration, a custody record is a control-plane orientation primitive: it tells a newly booted agent what work it may attempt, the context capsule it must resolve, what evidence is owed, who can accept a handoff, and where refusal or escalation goes. It does not replace a capability grant, execution authorization, or exact artifact boundary.

## 16. Direct Corpus Interfaces

The formal companion owns the state-machine and algebraic development. *Reasoning by Way of Receipts* explains how custody transitions can become attributable evidence without turning the receipt into authority. Cognitive ABI supplies typed capability and qualification information needed before a participant can accept custody. *Split-Authority AI Coordination* prevents one custody holder from collapsing proposal, checking, adoption, and execution powers. *Authority Laundering Theory* explains why an assignee, active agent, or completed step must not be mistaken for an authorized decision-maker. ACG supplies a larger development workflow in which custody can move among agents, validators, courts, and effect boundaries. GMB preserves the cross-paper meaning and lineage of these relations.

These are interfaces, not mergers. Work Custody answers who presently holds a scoped advancement obligation. Authority answers what actions are permitted. Capability answers what can be performed. Accountability answers who answers for outcomes. Standing answers what may count. Receipts answer what transition was recorded under which evidence. Waiting relations answer what condition currently blocks advancement.

## Human-Facing Work-Custody Protocol

The completed P1 corpus indicates that Who Has the Ball? should be retained as the **human-facing collaboration protocol and pedagogical surface for Work Custody**, not as a second foundational theory. The formal theory defines work identity, custody, transfer, leases, conflict, and completion; this paper makes the live question legible to mixed human-agent teams.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** The general formal model, invariants, concurrency, leases, and evidence obligations.  
  **This paper's boundary:** Who Has the Ball? supplies the minimal interaction grammar and reader-facing explanation.

- **Adjacent work:** *Exigence and the Cognitive Kernel*  
  **Supplies:** Recognition, attention, sufficiency, and transition of work pressure.  
  **This paper's boundary:** CogK helps determine what deserves work; custody states who currently bears the duty to advance it.

- **Adjacent work:** *The Optional Coordinator*  
  **Supplies:** Conditions under which coordination can remain local and substitutable.  
  **This paper's boundary:** Queryable custody can reduce coordinator dependence without proving all coordination optional.

- **Adjacent work:** *Cold Boot Continuity as a Deployment Primitive*  
  **Supplies:** Resumption of exact workfront and custody state.  
  **This paper's boundary:** A capsule carries custody evidence; a valid transfer still requires recognition and acceptance.

- **Adjacent work:** *Constitutional Collective with Optional Overmind (CCOO)*  
  **Supplies:** A bounded collective topology with optional coordination.  
  **This paper's boundary:** Work custody is one coordination primitive usable in that topology, not the collective architecture itself.

The human-facing custody view should bind:

$$
\begin{aligned}
Ball= (&work\_id, head, custodian, participants, status, \\
&blockers, next\_action, transfer\_offer, acceptance, \\
&lease, receipt)
\end{aligned}.
$$

The metaphor must not obscure the non-collapse rules: assignment is not custody; ownership is not custody; activity is not custody; possession of files is not custody; attention is not custody; and an offered transfer is not completed until accepted under the protocol. Joint custody requires an explicit profile rather than an unstructured list of responsible parties.

Waiting is a governed state only when the dependency, expected actor or event, review time, expiry, escalation path, and retained custodian are known. Otherwise `WAITING` can conceal orphaned work. A completed task likewise requires a terminal disposition and evidence appropriate to the work, not merely a status label.

The universal GSM can type `CUSTODIED_BY`, `ASSIGNED_TO`, `OFFERS_TRANSFER_TO`,  
`ACCEPTS_CUSTODY`, `WAITS_ON`, `BLOCKED_BY`, `LEASED_UNTIL`, `JOINTLY_CUSTODIED_UNDER`,  
`RETURNS_TO`, `TERMINALLY_DISPOSITIONED_AS`,  
and `RECEIPTED_BY`. The view projects the formal model without replacing it.

This integration establishes four editorial commitments: classify the paper as the human-facing protocol companion to the formal theory; adopt the Ball view; require explicit joint-custody profiles; and require waiting and completion to expose their evidence and escalation contracts.

## Custody Subject and Terminal Semantics

The fixed-seed comparison with HLIR, the constitutional syscall architecture, GTK, and Terminability reveals a necessary question before asking who has the ball: **custody of what exact subject and toward what terminal condition?**

$$
\begin{aligned}
C= (&work\_id, subject, head, purpose, custodian, \\
&authority\_surface, live\_effects, dependencies, \\
&terminal\_criteria, disposition, evidence)
\end{aligned}.
$$

GTK can resolve a work name, subject term, status, or dependency without establishing that two records identify the same live work. HLIR proposal custody may end at admission, refusal, withdrawal, or accepted handoff. A cyber-physical effect intent remains live through late, partial, or unknown outcomes until reconciliation or an explicitly bounded terminal disposition.

Terminability concerns the moral and decision structure of ending a subject or continuation under uncertainty. Work completion, cancellation, or archival is not automatically the ending of the work's subject. Conversely, a custodian responsible for an ending decision does not acquire moral, legal, device, or institutional authority merely through custody. The authority surface and escalation path must be separately named.

This prevents a dangerous status collapse: `DONE` for a drafting task,

`REFUSED` for an effect request, `STOPPED` for a process, `DELETED` for state, and `FORECLOSED` for a continuation thread have different objects and consequences. A human-facing Ball view should render the subject and terminal semantics, not only the assignee and status label.

The universal GSM can type   
`CUSTODIES_WORK_ABOUT_SUBJECT`,  
`RESOLVES_WORK_IDENTITY_WITH_GTK`, `DISTINGUISHES_TASK_END_FROM_SUBJECT_END`,  
`RETAINS_CUSTODY_FOR_UNKNOWN_EFFECT`, `LACKS_ENDING_AUTHORITY_DESPITE_CUSTODY`,  
and   
`TERMINALLY_DISPOSITIONS_EXACT_WORK_SUBJECT`.

This randomized review establishes four editorial commitments: add exact subject and purpose to the Ball view; type terminal criteria and dispositions by object; keep custody distinct from ending and effect authority; and retain custody while consequential outcomes remain partial, late, or unknown.

## The Ball View as a Governed Custody Projection

Six downstream uses confirm that this paper is the human-facing projection of Work Custody rather than a second custody theory. The formal companion supplies the state machine; Cognitive ABI uses custody as a separately evidenced invocation condition; the constitutional syscall paper retains a custodian while physical effects are pending or unknown; GTK resolves the identity of the work; HLIR carries proposal custody across review and lowering; and Terminability separates ending a task from ending its subject.

The queryable projection should therefore bind:

$$
\begin{aligned}
B^*= (&work\_identity, subject, generation, scope, purpose, \\
&custodian, recognition\_set, eligibility, \\
&authority\_boundary, state, next\_move, dependencies, \\
&lease, transfer, evidence, terminal\_disposition, \\
&remainder, view\_policy)
\end{aligned}.
$$

The record shown to one participant may legitimately differ from the record shown to another because privacy, labor, safety, or institutional constraints can limit visibility. The underlying custody claim must still have an exact generation, shared resolution rule, and authorized query path. A dashboard is a projection of the custody relation, not its source of truth; stale, partitioned, or inaccessible views must expose their freshness and uncertainty.

Custody persists across delegated work when the original custodian retains the duty to observe, reconcile, escalate, or disposition the result. It cannot be silently dropped merely because a request was sent, an agent is active, a device acknowledged receipt, or a court began review. A transfer closes only when the offered subject, obligations, context, authority boundary, evidence debt, and recovery path are accepted for the same work generation.

The universal GSM can type `PROJECTS_BALL_VIEW`, `RECOGNIZES_CUSTODY_GENERATION`,  
`RETAINS_CUSTODY_DURING_DELEGATION`, `ACCEPTS_CUSTODY_ENVELOPE`, `EXPOSES_VIEW_FRESHNESS`,  
`WITHHOLDS_CUSTODY_DETAIL_UNDER_POLICY`, `DISTINGUISHES_WORK_FROM_EVIDENCE_CUSTODY`,  
and   
`DOES_NOT_GRANT_EFFECT_AUTHORITY`.

This reverse-dependency review establishes four editorial commitments: retain the paper as the governed human-facing projection of the formal theory; adopt the expanded Ball record; require transfer of obligations, context, evidence debt, and recovery conditions; and make privacy, freshness, and partial visibility explicit without permitting hidden orphaning.

## 17. Counterevidence and Failure Modes

The proposal should be narrowed or rejected where: (1) teams can answer the same questions reliably from existing assignment and workflow fields without extra protocol cost; (2) acceptance clicks create ritual rather than accurate state; (3) exclusive custody discourages collaboration or hides shared responsibility; (4) participants game custody to avoid workload metrics or blame; (5) a dashboard is stale, partitioned, or inaccessible; (6) agents accept work they cannot perform; (7) custody is used to launder execution authority; (8) transfer receipts exist but context is missing; (9) joint or federated work cannot be decomposed without distortion; (10) `WAITING_ON` becomes a blame graph; (11) expiry produces churn or unsafe abandonment; (12) privacy and labor concerns make universal visibility harmful; (13) optimization rewards rapid handoff over completion quality; (14) automated reassignment breaks legitimate discretion or continuity; (15) the system confuses process state with moral or legal responsibility; or (16) measured coordination benefit does not exceed the modeling and maintenance burden.

Empirical comparison should measure handoff ambiguity, orphaned work, time to identify the next actor, context loss, false ownership inference, stall duration, escalation burden, user comprehension, and adverse strategic behavior against competent assignment-based and workflow-based baselines. Meeting reduction is a hypothesis, not a present finding.

## The Ball Is a Human-Facing Projection of Work Custody

### Public orientation

Who Has the Ball? introduces Work Custody through the everyday question of who currently holds the accepted, scoped duty and context to advance a work object. Its role is pedagogical and interface-facing. The formal state-machine, bitemporal, generation, lease, recovery, and concurrency details belong in the companion Formal Theory of Work Custody; this paper should project them without creating a second incompatible protocol.

### Adversarial tests

1. **Assignee-custodian attack.** Assignment, ownership, accountability, workflow state, or artifact possession is displayed as live accepted custody.
2. **Ball-authority attack.** Holding the next move grants approval, disclosure, publication, execution, or decision authority.
3. **Silent-handoff attack.** A message, meeting statement, status update, or reassignment is treated as accepted transfer.
4. **Stale-dashboard attack.** The interface hides version, scope, generation, expiry, capability, or a failed receiver and still shows one confident name.
5. **One-ball attack.** Work that legitimately needs joint, shard, quorum, alternate, or recovery custody is forced into a single-owner metaphor.
6. **Human-agent-equivalence attack.** Shared protocol syntax implies equal consent, persistence, accountability, legal status, or moral responsibility.
7. **Common-knowledge attack.** Queryable state is described as formally common knowledge although access, interpretation, freshness, and system mediation differ.
8. **Projection-kernel drift attack.** The simple reader-facing model changes transfer semantics or creates standing inconsistent with the formal companion.

### Claim and evidence ceiling

The paper offers a human-facing concept and minimal contract. It does not establish novelty, formal common knowledge, organizational improvement, meeting reduction, live acceptance, complete mediation, legal or moral responsibility, or a tested implementation. It is a projection of the Work Custody architecture, not an independent identity merger or competing kernel.

Evaluation requires matched human and agent handoffs, stale and failed-transfer cases, nonexclusive configurations, accessibility and privacy review, comprehension studies, and conformance to the formal companion. No runtime, organization, or external research was tested in this pass.

### Reader-facing consequence

The interface succeeds if a collaborator can see who has the next move, for which exact work and scope, whether they accepted it, whether they can act, when custody expires, who is waiting, and what recovery is underway.

## 19. Corpus Integration Sources

This pass used exact local heads for the formal companion (SHA-256  
`49C38F60B95E107F8B3D864ACAFB4C49067A146C807E5248307DE7B009AD4696`), *Reasoning by Way of Receipts* (

`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`), Cognitive ABI (  
`F7A7034BB9E382C91AEA693BD656040A93C5C5B504FE70425A31561CEECDC084`), *Split-Authority AI Coordination* (  
`AB9D992A4668946DB17F530B31BDD6DD35C6C247769D33F4C48897E29B337064`), *Authority Laundering Theory* (  
`DC7233E10A7597BB3802E54D5A7C5154700A425CF6332203C38592918413D47E`), ACG (  
`99E107467C6A3EE1368EC97A7D49065B5686227863879785E2CBE53755229AC1`), and GMB semantic-manifold documentation (  
`49A05A424F226A21C81D638727E1165DE1AD55AB1CBDC56EA65D67A1362A4B08`). Exact comparison custody does not establish truth, identity merger, implementation, or standing.

## 20. Future Work

Several research directions remain.

These include:

* formal custody algebra,
* joint custody semantics,
* distributed custody across organizations,
* custody transfer protocols,
* human-agent negotiation,
* constitutional governance integration,
* empirical measurement of meeting reduction,
* visualization of custody flow,
* custody-aware workflow optimization.

---

## 21. Conclusion

Many collaboration failures arise not because work is poorly defined but because responsibility is poorly localized in time.

Ownership is too persistent.

Assignment is too static.

Authority is too broad.

Workflow stages are too impersonal.

Work Custody identifies the missing operational primitive:

the current, explicitly recognized possession of responsibility-bearing work.

When combined with explicit transfer semantics and common operational knowledge, collaboration systems gain the ability to answer one of the oldest questions in organized work:

> **Who has the ball?**

Answering that question accurately, continuously, and constitutionally may reduce a class of coordination overhead that organizations currently address through meetings, reminders, and informal social reconstruction.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

---

## Editorial Provenance and Standing

### Source, Evidence, and Standing
This is an AI-prepared successor revision candidate derived from one exact author manuscript. The integration custody manifest is   
`work/paper-saturation-v1/evidence/who-has-the-`

`ball/integration-custody-manifest.v0.1.json`,  
SHA-256  
`C0E755BCBED77ED9038BDE37E2950FCC574299C08025CF46B33C1C42EF1B03B8`. The exact source remains unchanged. The entry question, Work Custody proposal, distinctions from assignment/ownership/authority/accountability, lifecycle, waiting relation, collaboration queries, and original conclusion are author material. This pass standardizes the Ableman paper header and hierarchy, distinguishes one custody protocol from identical responsibility, adds a scoped custody record and transfer rules, places the idea in the universal GSM and realization funnel, links its formal companion and direct corpus interfaces, and adds counterevidence and open editorial questions. Those changes are AI editorial or synthetic contributions until adopted.
No runtime, organization, handoff, custody ledger, or agent orchestration was tested. The paper does not establish novelty, meeting reduction, common knowledge in the formal epistemic sense, or that a non-human component can bear moral or legal responsibility. It proposes a governance representation for review. No publication, canonical standing, identity merger, conformance assignment, or implementation authority is granted.

## Corpus-Wide Reference Positioning

This paper argues that modern collaboration systems successfully model many aspects of cooperative work, including projects, documents, conversations, tasks, ownership, permissions, workflows, and automation. Its nearest external comparison fields are provenance, ai, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E2]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E3]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

**[E4]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E5]** Patrick Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **Relationship:** Predecessor retrieval architecture; comparison centers on provenance, admission, and fail-closed constraints not supplied by retrieval alone.

**[E6]** Shunyu Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. arXiv:2210.03629. https://arxiv.org/abs/2210.03629 **Relationship:** Predecessor agent pattern for interleaving reasoning and action; used to distinguish action traces from governed effects.

**[E7]** Elham Tabassi. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1, 2023. DOI: 10.6028/NIST.AI.100-1. https://doi.org/10.6028/NIST.AI.100-1 **Relationship:** Adjacent risk-management framework used to test whether the paper operationalizes governance beyond voluntary process guidance.

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

**[A6]** Adam Ableman. *CARA: Constrained Artificial Reasoning Architecture*. Ableman Corpus current edition; work identity `PAPER.PUB.18099715`;  
source SHA-256  
`F8F74F0CD58F5414D9A29EBE958E49751892D07A028CB51197F8201B18AAB40E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *A Constitution for the Context Window*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-CF26BA0E123F472F`;  
source SHA-256  
`60395402368E146F115CCE53D0E5A15B8FB23C90ED5B24CA92AB8515B2009965`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

Adam Ableman *Semantic Coordinate Identity Tokenization (SCIT).* Zenodo, 2026. doi:10.5281/zenodo.20532070

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848568](https://doi.org/10.5281/zenodo.23848568)
