# Operational Epistemic Situational Awareness in Agentic Orchestration

## A Governed Continuity Profile for Long-Running and Multi-Agent Work

### The architecture uses a governed meaning substrate as an orchestration sidecar, but a sidecar is not awareness by itself.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Long-running agent workflows can lose task scope, source custody, authority, current environment state, unresolved conflicts, or knowledge of what another worker is doing. Operational Epistemic Situational Awareness (ESA) is proposed as the capability to maintain and query an evidence-qualified model of those conditions and to govern continuation when that model becomes stale, conflicted, missing, or outside authority.

The architecture uses a governed meaning substrate as an orchestration sidecar, but a sidecar is not awareness by itself. Agent check-ins can be false or stale; receipts can record claims without proving effects; exclusive task claims can deadlock; handoffs can be unaccepted; and unmediated tools can bypass the substrate. The system must distinguish asserted, observed, inferred, stale, conflicted, and unknown state; combine voluntary reports with independent observations; preserve liveness and recovery; and govern sensitive operational data.

This paper defines an operational state model, check-in and claim leases, accepted handoff capsules, evidence postures, refusal and escalation outcomes, bypass and availability conditions, cold-boot orientation through the Governed Meaning Base, realization funnel, and comparative evaluation. It makes no claim of consciousness or privileged agent self-knowledge.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/operational-`

`epistemic-situational-awareness/integration-`  
`custody-manifest.v0.1.json`,  
SHA-256  
`2807E7582A41DCAB6422753401EC15CCB0DC592C28202405AA9894775F0D07CD`. The source remains unchanged.

The operational ESA concept, sidecar pattern, check-ins, claims, handoffs, receipts, refusal, and expected improvements are author material. Formal contracts, qualifications, corpus integration, tests, and decisions are AI editorial or synthetic candidates until adopted. No orchestration system was changed or evaluated.

## 1. Operational ESA

Operational ESA is not the statement that an agent "knows" in a human or phenomenal sense. It is a system capability: authorized participants can obtain a sufficiently current, evidence-qualified representation of task state, commitments, dependencies, authority, environment, failures, and uncertainty to choose among continuation, coordination, escalation, recovery, and stop.

This capability is relative to a declared workflow and observation regime. No system has complete awareness of all relevant facts.

## 2. Operational State Model

At time $t$, define:

$$
O_t=(T,G,C,K,E,F,U,D,A,R),
$$

where $T$ is tasks and goals, $G$ agents and roles, $C$ claims and custody, $K$ admitted context and knowledge snapshot, $E$ environment and tool state, $F$ failures and anomalies, $U$ unknowns and conflicts, $D$ dependencies and handoffs, $A$ authority and capability bounds, and $R$ receipts, observations, and revision lineage.

Every element has identity, source, epistemic posture, observed-at and valid-through time, confidence or uncertainty where meaningful, access class, and responsible custodian.

## 3. Epistemic Postures

State should not be flattened into facts. Use postures such as:

- `OBSERVED`: produced by a named sensor or direct system query;
- `ASSERTED`: reported by an agent or user;
- `INFERRED`: derived under a declared rule;
- `EXPECTED`: required or predicted but not observed;
- `STALE`: valid-through or renewal threshold exceeded;
- `CONFLICTED`: incompatible records remain unresolved;
- `UNKNOWN`: required state is unavailable; and
- `REVOKED`: no longer authorized for current reliance.

An assertion can be accurate; an observation can be faulty. Posture identifies evidence role, not truth.

## 4. Sidecar Architecture

The orchestration runtime remains responsible for scheduling, agent execution, tool mediation, and communication. The sidecar or shared substrate maintains structured operational state, lineage, queries, policies, and evidence.

The separation improves replaceability and cold boot, but introduces distributed-system concerns: synchronization, partitions, stale reads, split brain, access latency, schema migration, availability, and partial writes. A central sidecar may also become a bottleneck or concentrated authority.

The `jn` command surface and an orchestration framework such as OpenClaw are source examples, not required identities or validated implementations. The pattern should be specified independently of any one tool.

## 5. Check-In Contract

A check-in should include:

- agent, role, session, and task identity;
- current goal and completion criteria;
- artifacts read, modified, or proposed, with hashes where available;
- active assumptions, claims, and evidence posture;
- actions completed and externally observed effects;
- blockers, anomalies, conflicts, and unknowns;
- requested capabilities or decisions;
- dependencies and intended next action;
- predecessor state version;
- observed-at, valid-through, and renewal conditions; and
- access classification and source receipts.

Check-ins are agent assertions. Independent tool results, filesystem state, service responses, tests, and human observations should be linked rather than restated as if verified by the agent.

## 6. Claims and Work Custody

A work claim is a scoped lease, not permanent ownership. Define:

$$
C=(work,holder,role,scope,grant,start,expiry,renewal,conflict,release).
$$

The protocol must support shared custody, read-only participation, independent review, subdivision, priority, conflict resolution, abandonment, and recovery from dead agents. The strongest rule is not "one task, one agent" but explicit responsibility and coordination under a selected profile.

**A Formal Theory of Work Custody** supplies the wider model of work identity, custody, transfer, and completion.

## 7. Accepted Handoffs and Context Capsules

A handoff is incomplete until the receiving role accepts it or the policy selects an alternate custodian. Its capsule should bind:

- work and predecessor identity;
- exact artifact inventory and custody hashes;
- current state, completed work, and open obligations;
- decisions and their authority;
- evidence, failed attempts, and counterevidence;
- active risks, unknowns, and disputed interpretations;
- capabilities and environment required;
- next admissible actions and stop conditions; and
- sender and receiver receipts.

This capsule is the portable crystal context used for cold boot across sessions or orchestration environments. It should be minimal enough to load, complete enough to orient, and linked to the GMB for deeper retrieval.

## 8. Receipts and Effect Correspondence

A receipt records that an actor or mechanism declared or observed an event under a profile. It does not by itself prove the action succeeded, the external effect occurred, the effect matched intent, or the claim was truthful.

Operational ESA should distinguish proposal, authorization, attempted action, tool response, observed effect, verification, and compensation. **Reasoning by Way of Receipts** supplies the inference discipline for moving among these records without overclaiming.

## 9. Context Construction

Agents should not receive the entire substrate indiscriminately. **A Constitution for the Context Window** provides the broader governance model for selecting, typing, and bounding context.

An orientation view should include current goal, authority, custody, relevant artifacts, fresh observations, conflicts, unknowns, dependencies, and claim ceilings. It should exclude or redact irrelevant, expired, private, adversarial, and unauthorized material.

Retrieval and summarization must preserve source links and disclose omissions. A compact capsule is a projection, not the corpus itself.

## 10. Refusal, Escalation, and Liveness

Typed outcomes include `CONTINUE`, `CONTINUE_QUALIFIED`, `COORDINATE`, `RENEW_CLAIM`,  
`HANDOFF`, `DEFER`, `ESCALATE`, `REFUSE`, `RECOVER`, and `NOT_COVERED`.

Refusal is protective when continuation lacks evidence or authority. It can also create denial of service, deadlock, or permanent deferral. Every refusal profile needs repair information, responsible escalation, time bounds, emergency handling, and a path for renewed evidence or authority.

Availability is part of governance. If the sidecar fails, the system needs declared degraded modes: safe stop, read-only operation, locally bounded continuation, recovery from last verified snapshot, or explicitly unauthorized operation. Silent fallback to ambient autonomy is not acceptable.

## 11. Bypass and Enforcement

Check-ins and policies are advisory unless tool, credential, message, storage, network, and effect paths are actually mediated. Agents do not "learn" inadmissible continuations merely because the sidecar records them.

Claims of governed continuation should enumerate all paths, test direct and indirect bypasses, and distinguish monitored-but-possible actions from structurally unavailable ones. Human action and external services remain part of the boundary.

## 12. Security, Privacy, and Adversarial State

Operational state can expose credentials, vulnerabilities, employee activity, confidential strategy, personal data, failures, and safety-sensitive locations. Apply minimization, role- and purpose-bound access, encryption where warranted, retention and deletion policy, redaction, audit, and incident response.

The substrate must treat agent-authored content as untrusted. Threats include prompt injection, forged check-ins, claim squatting, stale-lock denial, malicious handoffs, poisoned summaries, false receipts, clock manipulation, identity spoofing, exfiltration through retrieval, and compromised observers.

## 13. Derived Assessments

Operational ESA may derive staleness, conflict, progress, anomaly, or risk assessments. Each derivation should expose inputs, method, version, uncertainty, and action consequence. A score is not a cause or verdict.

Self-debugging means the system can propose diagnoses and repairs from evidence. It does not mean autonomous repair is authorized or correct. Repair remains subject to effect and authority gates.

## 14. Corpus Integration and Authorial Compression

**Operational ESA** is the orchestration-facing state and control profile. **Epistemic Situational Awareness and the Governed Knowledge Loop** supplies the wider observe-assess-govern-revise loop. **Work Custody** supplies claims and handoffs. **Reasoning by Way of Receipts** bounds inference. **A Constitution for the Context Window** governs what an agent loads.

The **Governed Meaning Base (GMB)** is the canonical curated meaning and evidence substrate; the sidecar is an operational interface or projection over it, not a separate truth source. **Hyperpedia** is the human pedagogical projection. A crystal context capsule is the session-portable orientation projection. The universal **GSM** types their relations without promoting an agent report to fact.

## 15. Realization Funnel

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

- **Possibility:** enumerate centralized, federated, peer-to-peer, local-capsule, human-mediated, and no-sidecar designs.
- **Specification:** define state, postures, claims, handoffs, receipts, access, threats, outcomes, liveness, and evidence.
- **CM1:** retain admissible coordination configurations, including strict, degraded, and partition-tolerant variants.
- **CM2:** prefer configurations by coherence, freshness, safety, privacy, availability, usability, cost, and recovery.
- **IC:** select an Instance Constitution or Instance Configuration for one orchestration environment.
- **IR:** produce an Instance Realization or Implementation Realization of stores, protocols, adapters, capsules, views, and gates.
- **Evidence:** test coordination, recovery, state accuracy, bypass, privacy, performance, and human comprehension.
- **Revision:** update models, protocols, configurations, and realizations from incidents and counterevidence.

This paper reaches Specification and proposes CM1/CM2. It does not select an IC or certify an IR. Realization-stage IR remains distinct from Intermediate Representation in MCIR and related compiler contexts.

## 16. Evaluation Program

Compare baseline orchestration, ungoverned shared memory, structured sidecar, and GMB/capsule profiles on matched long-running workflows. Seed stale context, duplicate work, tool failure, agent loss, conflicting edits, network partitions, false check-ins, malicious handoffs, and authority gaps.

Measure duplicate work, conflict detection, stale-state use, unsupported continuation, time to orientation, handoff acceptance and loss, recovery, effect mismatch, bypass rate, deadlock, availability, privacy leakage, human reconstruction time, task quality, latency, storage, and operator burden. Use exact run custody and independent effect observation.

Claims of improved reliability or capability require statistically and operationally meaningful differences, not only illustrative demonstrations.

## Orchestration Continuity and Cold-Boot Profile

Across the completed P1 corpus, Operational ESA is the **orchestration continuity and cold-boot profile that projects current goals, custody, authority, evidence posture, environment, conflicts, dependencies, and stop conditions into long-running or multi-agent work**. It is not a second meaning base, a claim of machine awareness, or proof that recorded state matches the world.

- **Adjacent work:** *Epistemic Situational Awareness and the Governed Knowledge Loop*  
  **Supplies:** General present-orientation and temporal epistemic-lifecycle pair.  
  **Operational ESA boundary:** Operational ESA specializes present orientation for agentic work.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Work identity, custodian, lease, handoff, return, and terminal disposition.  
  **Operational ESA boundary:** Operational claims use custody protocols rather than inventing ownership by check-in.

- **Adjacent work:** *A Constitution for the Context Window*  
  **Supplies:** Governed selection, typing, omission, and admission of agent context.  
  **Operational ESA boundary:** ESA state is an input to context construction, not the entire context constitution.

- **Adjacent work:** *Cold Boot Continuity as a Deployment Primitive*  
  **Supplies:** Reconstruction in a fresh environment from retained artifacts.  
  **Operational ESA boundary:** A capsule is adequate only when cold-boot testing reproduces the bounded orientation.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Claim-bounded transition, observation, effect, and revision records.  
  **Operational ESA boundary:** Receipts qualify check-ins and handoffs without proving their asserted effects.

An orientation capsule should bind:

$$
\begin{aligned}
O= (&goal, completion\_criteria, authority, custody, \\
&artifacts, environment, observations, assertions, \\
&conflicts, unknowns, dependencies, failures, \\
&next\_actions, stop\_conditions, snapshot)
\end{aligned}.
$$

Each field retains identity, source, posture, freshness, access class, and omission status. The capsule is a purpose-bounded projection linked to deeper governed state. A receiving agent must acknowledge or refuse the handoff; file presence or message delivery alone does not transfer custody.

Sidecar failure, partition, stale clocks, false check-ins, poisoned summaries, dead agents, privacy constraints, and unmediated tools are part of the operational model. Degraded modes must be explicit: safe stop, read-only use, locally bounded continuation, recovery from a verified snapshot, or `NOT_COVERED`. Silent fallback to ambient autonomy invalidates the governance claim.

The universal GSM can type   
`ORIENTS_AGENT_FOR_GOAL`, `ASSERTED_BY_CHECKIN`,  
`OBSERVED_BY_INDEPENDENT_TOOL`, `LEASED_TO_CUSTODIAN`, `OFFERED_IN_HANDOFF`,  
`ACCEPTED_BY_RECEIVER`, `PROJECTED_IN_CONTEXT_CAPSULE`, `STALE_FOR_CONTINUATION`,  
`RECOVERED_FROM_VERIFIED_SNAPSHOT`,  
and   
`BYPASSES_OPERATIONAL_ESA`. These relations preserve operational utility and claim ceilings.

This integration establishes four editorial commitments: classify Operational ESA as the orchestration continuity/cold-boot profile; adopt the orientation-capsule envelope; require accepted handoffs and explicit degraded modes; and require independent observation and whole-surface bypass tests before claiming governed continuation.

## Freshness, Schema, and Human Escalation in the Operational Capsule

The fixed-seed comparison with the GMB, temporal-risk evaluation, AFS, and the Human Validation Layer extends the orientation capsule:

$$
\begin{aligned}
O^*= (&GMB\_snapshot, AFS\_profile, goal, custody, authority, \\
&artifacts, observations, assertions, conflicts, unknowns, \\
&dependencies, freshness, expiry, escalation, acceptance)
\end{aligned}.
$$

GMB provides governed semantic state from which the capsule is projected. Temporal discipline requires separate observation, availability, admission, decision, and correction times, plus expiry for claims and credentials. A live check-in cannot retroactively alter what was known at an earlier decision.

AFS may define a portable orientation-capsule profile and conformance vectors. Schema conformance does not establish current truth, full coverage, authority, or successful handoff. The receiver must verify exact artifacts, inspect omissions, and accept or refuse custody.

HVL supplies a possible escalation path for contested interpretations, promotion requests, or semantic repairs. Human involvement does not automatically create truth or standing; the review requires competence, independence, source access, authority, dissent preservation, and appeal.

The universal GSM can type   
`PROJECTED_FROM_GMB_SNAPSHOT`,  
`CONFORMS_TO_ORIENTATION_PROFILE`, `FRESH_AT_OPERATION_TIME`,  
`EXPIRES_OPERATIONAL_ASSERTION`, `ESCALATED_TO_HUMAN_REVIEW`, `ACCEPTED_WITH_CUSTODY`,  
and   
`REFUSED_FOR_STALE_OR_INCOMPLETE_STATE`.

This randomized review establishes four editorial commitments: adopt the expanded capsule; make time and expiry first-class; define but limit AFS conformance; and route contested semantic decisions to qualified human review without authority laundering.

## The Orientation Capsule as an Expiring Consumer Projection

Eight downstream uses converge on Operational ESA as an expiring projection for action, not a second store or authority source. The GMB supplies governed state; AFS can encode an orientation profile; COP supplies evidence inputs; the general ESA/GKL pair supplies present-orientation and temporal-lifecycle semantics; work custody supplies the duty relation; Human Validation supplies qualified escalation; temporal evaluation uses the decision-time cut; and split-authority coordination determines which role may bind a decision.

The capsule contract is:

$$
\begin{aligned}
O= (&purpose, task, history\_head, projection\_profile, goals, \\
&custody, authority, evidence, environment, dependencies, \\
&conflicts, unknowns, failures, options, stop\_conditions, \\
&omissions, freshness, expiry, acceptance)
\end{aligned}.
$$

The producer asserts this state; the receiver separately verifies custody, accepts or refuses the handoff, and decides what to load. A capsule may be syntactically conforming and still be stale, incomplete, adversarial, overprivileged, or unsupported. GMB inclusion does not grant operational relevance. COP health does not make the capsule true. An escalation trigger does not appoint a competent human reviewer. A fresh goal does not refresh authority, environment, or evidence dimensions automatically.

Downstream use also reveals two time rules. Historical evaluation must reconstruct the capsule and evidence admissible at the original decision time rather than import later corrections. Live continuation must expire or qualify any dimension whose source, authority, environment, dependency, or observation is stale. Schema evolution requires an explicit migration with preserved omissions and remainder.

The universal GSM can type   
`PROJECTS_ORIENTATION_FROM_GMB`,  
`CONFORMS_TO_ORIENTATION_PROFILE`, `CONSUMES_COP_EVIDENCE`, `ACCEPTS_OR_REFUSES_HANDOFF`,  
`ESCALATES_WITHOUT_APPOINTING_AUTHORITY`, `RECONSTRUCTS_DECISION_TIME_CAPSULE`,  
and   
`EXPIRES_STALE_ORIENTATION_DIMENSION`.

This reverse-dependency review establishes four editorial commitments: adopt the expiring consumer-projection model; require independent handoff acceptance and dimension-specific freshness; preserve historical decision-time capsules; and require explicit schema migration, omission, and remainder records.

## 17. Counterevidence and Failure Modes

The architecture should be narrowed or rejected where: (1) a sidecar is called awareness automatically; (2) agent assertion is treated as observation; (3) receipts imply effects; (4) check-ins are stale; (5) check-ins omit failures; (6) agents fabricate progress; (7) claims never expire; (8) claim squatting blocks work; (9) one-owner rules prevent collaboration; (10) joint custody is undefined; (11) handoffs do not require acceptance; (12) capsules omit failed attempts; (13) summaries erase constraints; (14) retrieval loads private or adversarial material; (15) sidecar state conflicts with reality; (16) clocks cannot be trusted; (17) partitions create split brain; (18) the sidecar is unavailable; (19) fallback becomes ambient autonomy; (20) refusal creates deadlock; (21) escalation has no responsible actor; (22) emergency paths are abused; (23) tools bypass governance; (24) credentials exceed declared authority; (25) external effects lack witnesses; (26) observers share one failure mode; (27) derived scores become verdicts; (28) self-debugging performs unauthorized repair; (29) prompt injection poisons state; (30) identity spoofing succeeds; (31) operational data leaks; (32) retention violates deletion obligations; (33) GMB inclusion becomes truth; (34) Hyperpedia projection becomes authority; (35) capsule completeness is assumed; (36) GSM edges become causation; (37) corpus works are merged; (38) a proposal is presented as implemented; (39) baseline orchestration performs equally; (40) sidecar costs exceed benefits; (41) named tools differ from described behavior; or (42) external research contradicts novelty or reliability claims.

## Operational Orientation Must Expire Before It Becomes Fiction

### Public orientation

Operational Epistemic Situational Awareness externalizes the current goals, custody, authority, environment, dependencies, failures, conflicts, unknowns, and evidence of long-running agent work. Check-ins and context capsules are projections used to decide whether work should continue, coordinate, escalate, recover, or stop. They are not agent self-knowledge, truth, or permanent authority.

### Adversarial tests

1. **Assertion-observation attack.** An agent check-in or completion claim is stored as observed fact without independent evidence.
2. **Freshness-bundling attack.** A new goal or recent timestamp incorrectly refreshes stale authority, environment, dependency, evidence, and custody dimensions.
3. **Claim-squatting attack.** Long leases, exclusive ownership, or failed renewal blocks useful work and hides abandonment.
4. **Unaccepted-handoff attack.** A sender considers custody transferred although the receiver did not verify, accept, or load the capsule.
5. **Capsule-poisoning attack.** Prompt injection, forged identity, low-authority content, or omitted failures enters the operational projection.
6. **Sidecar-split-brain attack.** Partitions, clock error, schema drift, partial writes, or unavailable state produce conflicting operational realities.
7. **Governance-bypass attack.** Tools, credentials, messages, effects, or repair paths operate outside the sidecar while the workflow appears governed.
8. **Escalation-authority attack.** A trigger appoints an unqualified or unauthorized human reviewer, or refusal deadlocks without safe degraded operation.

### Claim and evidence ceiling

Operational ESA is an expiring, evidence-qualified consumer projection for bounded workflows. It does not establish complete awareness, truthful agents, verified effects, correct derived scores, competent escalation, privacy, security, liveness, or improved orchestration. GMB inclusion and COP evidence supply neither truth nor operational relevance automatically.

Claims about multi-agent orchestration, workflow leases, shared state, fault tolerance, memory, privacy, security, human coordination, cost, or performance require current external research and exact adversarial comparisons with baseline orchestration. No system was changed or evaluated in this pass.

### Reader-facing consequence

The public benefit is a portable capsule that says what the work currently depends on, what is asserted versus observed, when each dimension expires, and who must accept the handoff - so an agent can cold boot without pretending stale context is reality.

## 19. Conclusion

Operational ESA is the discipline of keeping long-running work located within current goals, custody, evidence, authority, dependencies, environment, and uncertainty. A governed substrate can support that discipline by externalizing state and making claims, conflicts, handoffs, refusals, and revisions inspectable.

The architecture succeeds only when it also governs its own limitations: stale and false reports, sidecar failure, bypass, privacy, deadlock, and the difference between recorded action and observed effect. Its value is not machine self-awareness. It is a more reconstructable and contestable basis for deciding whether coordinated work should continue.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of multi-agent orchestration, distributed workflow and lease systems, observability, event sourcing, shared-memory architectures, context and long-term memory, human-computer coordination, fault tolerance, privacy and access control, security of agentic systems, and the named software examples.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Instance Configuration.** The present paper does not claim a complete instance configuration treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that long-running agent workflows can lose task scope, source custody, authority, current environment state, unresolved conflicts, or knowledge of what another worker is doing. Its nearest external comparison fields are ai, consciousness, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. Structural and computational correspondences remain insufficient as phenomenal evidence unless linked to discriminating empirical predictions against competing theories. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Patrick Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **Relationship:** Predecessor retrieval architecture; comparison centers on provenance, admission, and fail-closed constraints not supplied by retrieval alone.

**[E2]** Shunyu Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. arXiv:2210.03629. https://arxiv.org/abs/2210.03629 **Relationship:** Predecessor agent pattern for interleaving reasoning and action; used to distinguish action traces from governed effects.

**[E3]** Elham Tabassi. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1, 2023. DOI: 10.6028/NIST.AI.100-1. https://doi.org/10.6028/NIST.AI.100-1 **Relationship:** Adjacent risk-management framework used to test whether the paper operationalizes governance beyond voluntary process guidance.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Emily M. Bender et al. "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *FAccT '21*, 2021. DOI: 10.1145/3442188.3445922. https://doi.org/10.1145/3442188.3445922 **Relationship:** Counterpressure concerning scale, environmental cost, documentation, and social risk; included to prevent governance proposals from becoming capability-only narratives.

**[E6]** David J. Chalmers. "Facing Up to the Problem of Consciousness." *Journal of Consciousness Studies* 2(3), 1995, pp. 200-219. https://consc.net/papers/facing.html **Relationship:** Foundational framing of the explanatory gap; cited to bound, not resolve, phenomenal claims.

**[E7]** Larissa Albantakis et al. "Integrated Information Theory (IIT) 4.0: Formulating the Properties of Phenomenal Existence in Physical Terms." *PLOS Computational Biology* 19(10), 2023, e1011465. DOI: 10.1371/journal.pcbi.1011465. https://doi.org/10.1371/journal.pcbi.1011465 **Relationship:** Competing formal theory of consciousness included for explicit contrast and counterevidence obligations.

### Ableman corpus

**[A1]** Adam Ableman. *CARA: Constrained Artificial Reasoning Architecture*. Ableman Corpus current edition; work identity `PAPER.PUB.18099715`;  
source SHA-256  
`F8F74F0CD58F5414D9A29EBE958E49751892D07A028CB51197F8201B18AAB40E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *A Constitution for the Context Window*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-CF26BA0E123F472F`;  
source SHA-256  
`60395402368E146F115CCE53D0E5A15B8FB23C90ED5B24CA92AB8515B2009965`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Governed Context & Memory (GCM)*. Ableman Corpus current edition; work identity `PAPER.PUB.18633797`;  
source SHA-256  
`3F17ACD8AB9C6DC66C23D22098628C70042854B198C3ABFCBFA3EC7DC27B9C08`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Retrieval-Augmented Reasoning under Constitutional Constraints*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-384489D4604BEC4D`;  
source SHA-256  
`133DA35C0F27F35BAA1F53DFEE415068AD2D24FF713F8CDAFA2FDC8F748AC15C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Split-Authority AI Coordination*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-35D1BAECD5CB17AD`;  
source SHA-256  
`06FB6133170879FA8308684F0DA33F5813EAF3B5488291C2D7D234BEB6FDFEC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Ableman Consciousness Ontology (ACO)*. Ableman Corpus current edition; work identity `PAPER.PUB.18203749`;  
source SHA-256  
`ACD97032780DA7B3A36750702BE1F47BCB2E6361EF6E74ECA8B441D7C6A25DDE`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Locus of Qualia*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-AF27E66B81811DB1`;  
source SHA-256  
`7B83EBD0FFDCFEBFA522A715AE0E4D1049FCA0B4CE0618C2017F8BB9206E5424`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

DOI: [10.5281/zenodo.23848100](https://doi.org/10.5281/zenodo.23848100)
