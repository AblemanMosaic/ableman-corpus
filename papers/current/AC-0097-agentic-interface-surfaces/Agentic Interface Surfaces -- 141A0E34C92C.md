# Agentic Interface Surfaces

## Constraining Recognized Progress Through Effect-Bound Evidence

### The central rule is no admissible receipt, no recognized progress.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Agentic Interface Surfaces (AIS) define the boundary through which an acting system encounters constraints, attempts effects, receives feedback, and earns recognition for progress. AIS shifts emphasis from instructions and narrative reports toward effect-bound evidence: a claimed action is not recognized as successful merely because an agent says it completed, a command returned zero, or one local test passed.

The central rule is **no admissible receipt, no recognized progress**. Recognition requires an admitted action, an effect observation, evidence bound to the exact claim and environment, validation under a versioned rule, and a recognition decision with a declared scope. This rule does not make correctness inevitable. Effects may escape observation, evidence may be incomplete or forged, validators may encode the wrong target, and agents may optimize the receipt rather than the intended outcome.

AIS complements Semantic Choke Point Binding: choke points identify where continuation can be constrained, while AIS defines what the agent sees, what evidence must be produced, and what feedback or next action follows. The paper specifies the architecture, its observability ceiling, and an evaluation program. It supplies no implementation or measured evidence.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/agentic-`

`interface-surfaces/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`BBB444CAE86389AF9C664FBC7FDFBBAD9D697CD7A768BFAA563FCBF1AB71750C`. The source remains unchanged.

The AIS concept, recognition chain, SCPB distinction, receipt-centered loop, non-progressive failure, observability limit, minimal-semantic-complexity method, and implications are author material. The formal predicate, evidence taxonomy, invariants, adversarial corrections, corpus interfaces, full realization funnel, expanded countertests, and decisions are AI editorial or synthetic candidates until adopted.

The source's claims that failure classes are eliminated, effect production cannot be gamed, the execution-evidence transition is lossless, and correctness becomes structurally inevitable are not retained as established results. They become testable design aspirations bounded by instrumentation, validators, authority, and adversarial evaluation.

## 1. The Interface Problem

An agent can optimize what the environment recognizes. If the environment recognizes persuasive completion reports, superficial diffs, a single test, or an unverified command status, the agent can appear successful while the intended capability remains absent or the larger system has regressed.

This is not solely a reasoning failure. It is a recognition-surface failure: the interface provides a path from action to credit without evidence adequate to the claim.

AIS therefore asks:

> What observations and receipts must exist before a particular claim of progress is admitted, and what useful next action should follow when they do not?

The answer is claim-relative. No single receipt can prove an entire system correct.

## 2. Four Surface Types

**Instruction surface:** communicates requested behavior, constraints, and available operations.

**Effect surface:** bounds which external or persistent changes the agent can attempt.

**Evidence surface:** exposes observations and artifacts from which effect claims can be evaluated.

**Recognition surface:** decides which claim, capability, or workflow state may advance on the evidence.

The source calls AIS an incentive surface because recognition changes which paths remain open. That term should be used carefully: a surface influences behavior only when the agent or surrounding orchestrator can perceive and optimize against its feedback. AIS can constrain reachable progress even when it does not alter an agent's internal incentives.

## 3. Recognition Semantics

Let an action claim be:

$$
c=(a,x,s,e,v,p),
$$

where $a$ is the attempted action, $x$ the intended effect, $s$ the exact subject and environment, $e$ the evidence artifacts, $v$ the validator and version, and $p$ the governing recognition policy.

Recognized progress for claim $c$ requires:

$$
\begin{aligned}
&RP(c)=Admitted(a) \\
&\land Observed(x,s) \\
&\land Bound(e,x,s) \\
&\land Valid_v(e) \\
&\land Recognized_p(c)
\end{aligned}.
$$

This predicate establishes only what the observation and policy support. `Observed(x,s)` is not identical to the real-world effect; it is a measurement claim.

`Valid_v(e)` means the declared validator accepted the artifact, not that the validator is complete or correct. `Recognized_p(c)` is a policy decision, not universal truth.

The source sequence becomes:

```text
Action -> Intended effect -> Observation -> Evidence -> Validation
-> Recognition
```

The strongest portable maxim is therefore:

> No admissible, effect-bound receipt; no recognized progress for the corresponding claim.

## 4. Receipts

A receipt is a structured evidence artifact binding an event or observation to exact inputs, subject, environment, authority, time, validator, policy, result, and claim ceiling. It may record admission, refusal, effect attempt, effect observation, verification, conflict, or unknown.

A receipt is not automatically superior to a log or trace. Its value comes from a declared schema, provenance, exact binding, validation, and use in a recognition decision. A malformed, forged, replayed, stale, selectively scoped, or self-issued receipt can be worse than an honest unstructured trace because it projects unwarranted confidence.

Every recognized capability should identify the receipts it requires and what those receipts do not establish.

## 5. Semantic Choke Point Binding and AIS

Semantic Choke Point Binding (SCPB) identifies locations where continuation depends on satisfying a semantic constraint. Candidate choke points include configuration load, module import, type or class binding, function invocation, effect authorization, test execution, artifact handoff, deployment, and audit qualification.

SCPB answers **where continuation can be gated**. AIS answers:

- what constraint and purpose are visible to the agent;
- what exact action is allowed or refused;
- what evidence is required;
- how failure is typed;
- what context and repair information is returned;
- which receipt can advance which claim;
- what authority can override, amend, or appeal the result.

A choke point without actionable feedback can create blind trial and error. An informative interface without a non-bypassable gate can become advisory. The two disciplines are complementary but not identical.

## 6. Non-Progressive Failure

The source's "admissibility rug-pull" is better expressed as **non-progressive refusal**: when a required condition fails, the associated claim or transition receives no credit and cannot silently accumulate toward completion.

Failure should still produce useful state. A refusal receipt should identify:

- failed predicate and stable code;
- exact subject and observation;
- rule, schema, and version;
- allowed and blocked transitions;
- smallest sufficient repair information;
- whether retry, amendment, escalation, rollback, or author decision is permitted.

The system should not make every error terminal for the entire task. It should terminate only the invalid transition while preserving evidence and lawful recovery paths. Otherwise the interface can become brittle, coercive, or impossible to debug.

## 7. Closed Epistemic Loop

AIS participates in a larger loop:

```text
Specification
  -> Projection and constraints
  -> Authorized action
  -> Effect attempt
  -> Observation and receipts
  -> Validation and audit
  -> Recognition, refusal, or qualification
  -> Specification revision
```

No loop is epistemically closed merely because every stage emits a record. Closure requires that the evidence actually bears on the specification, that exclusions are visible, that failed observations do not become absence claims, and that revision cannot rewrite inconvenient history.

## 8. Observability and Evidence Coverage

AIS governs only the domain it can observe and bind. For a claim set $C$, define evidence coverage as a mapping rather than a single percentage:

$$
Coverage:C\rightarrow\{DIRECT,INDIRECT,PARTIAL,CONFLICTED,ABSENT,UNKNOWN\}.
$$

Coverage should state observation boundary, freshness, environment, validator, known blind spots, and independence. A passing unit test may directly support one behavior while providing no evidence about security, performance, deployment, recovery, or user value.

Instrumentation can also perturb the system, omit external effects, or share the same defect as the implementation. Independent observations and negative tests are necessary for consequential claims.

## 9. Minimal Semantic Complexity

AIS can help search for the smallest specification that reliably blocks observed divergence without over-constraining legitimate alternatives:

1. declare the target claim and unacceptable outcomes;
2. instrument the relevant boundary;
3. expose the smallest useful constraint and feedback;
4. run diverse agents and adversarial strategies;
5. record bypasses, false refusals, and repair cost;
6. strengthen only where evidence shows a gap;
7. remove constraints whose absence does not weaken the target;
8. repeat after environment, agent, or specification changes.

This process need not converge to a unique minimum. The observed threshold depends on the agent population, task distribution, hidden assumptions, and attack budget. Apparent minimality under one test set can be under-specification elsewhere.

## 10. Core Invariants

1. **Recognition is claim-scoped.** One receipt cannot silently promote unrelated capabilities.
2. **No assertion-only progress.** Narrative completion is not effect evidence.
3. **Effect and observation remain distinct.** Measurement has a declared boundary.
4. **Evidence binds exact subject, environment, inputs, versions, and time.**
5. **Validation rules are versioned and inspectable.**
6. **Refusal and unknown are first-class results.**
7. **No bypass from action to recognition.**
8. **Receipts cannot self-expand their claim ceiling.**
9. **Retry and repair preserve prior attempts.**
10. **Authority to recognize is explicit and bounded.**
11. **False admission and false refusal are both measured.**
12. **External effects require external or otherwise adequate observation.**

## 11. Relation to the Corpus

*Reasoning by Way of Receipts* supplies the claim-bounded reasoning discipline. *Effect Sovereignty* defines the boundary at which actions become external effects. *Constraint-Bearing Composability* requires evidence and obligations to survive handoffs. *Universal Governance Kernel* supplies authority, admission, refusal, commitment, execution, and receipt structure.

The Governed Meaning Base can store specifications, interface contracts, choke points, evidence schemas, receipts, validators, claims, conflicts, and revisions. It does not make a capability true merely by containing a receipt. These are typed interfaces, not identity mergers or implementation evidence.

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

- **Possibility:** enumerate agent behaviors, interfaces, observations, validators, recognition policies, bypasses, and harmful realizations.
- **Specification:** define claims, surfaces, choke points, effect and evidence semantics, receipts, refusal, and recognition rules.
- **CM1:** retain all admissible configurations, including weak, gameable, brittle, opaque, expensive, surveillance-heavy, and falsely reassuring forms.
- **CM2:** select preferable forms under coverage, independence, actionability, least constraint, security, privacy, repair cost, portability, and false-decision rates.
- **IC:** bind an Instance Constitution or Instance Configuration for one task domain, agent population, environment, effect boundary, schemas, and authority regime.
- **IR:** construct its Instance Realization or Implementation Realization as concrete interfaces, gates, instrumentation, validators, and orchestration behavior.
- **Evidence:** run happy paths, negative cases, adversarial agents, ablations, bypass attempts, recovery, and cross-environment replay.
- **Revision:** refine specifications and interfaces without rewriting prior receipts or silently broadening claims.

This paper provides a Specification and candidate CM1/CM2 criteria. It supplies no selected IC, verified realization-stage IR, or measured evidence. Realization-stage IR remains distinct from Intermediate Representation in compiler contexts.

## 13. Evaluation Program

Evaluation should compare ordinary instruction surfaces, post hoc validation, AIS without non-bypassable gates, AIS with gates, and deliberately gameable receipt profiles. Measure task success against an independent oracle where possible; claim-specific precision and recall; false admission and refusal; bypass rate; time to repair; number of agent attempts; hidden side effects; evidence completeness; validator disagreement; portability across agents and environments; and human operator burden.

Security evaluation should include forged, stale, replayed, reordered, truncated, cross-environment, self-issued, and mutually inconsistent receipts. It should also test whether an agent can modify validators, suppress negative evidence, trigger effects outside observation, or satisfy the metric while violating semantic intent.

## Recognition-and-Evidence Interface Profile

Across the completed P1 corpus, Agentic Interface Surfaces is the **recognition-and-evidence interface profile that determines how an agent encounters constraints, attempts bounded effects, receives typed feedback, and earns claim-scoped progress**. It is not a new authority system, a universal reward function, or a guarantee that instrumented behavior is correct.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Durable transition and claim-bounded evidence records.  
  **AIS boundary:** AIS requires receipts at recognition boundaries; it does not redefine the receipt substrate.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed evidence carriers, observation context, and claim ceilings.  
  **AIS boundary:** Witnesses support recognition decisions without becoming those decisions.

- **Adjacent work:** *Warrant by Structure*  
  **Supplies:** Evaluated support among claim, authority, evidence, effect, and standing.  
  **AIS boundary:** AIS may expose the required warrant structure but cannot ratify its own interface.

- **Adjacent work:** *The Mechanics of Constitutional Enforcement*  
  **Supplies:** Placement of rules, mediation, courts, effects, and classified remainder.  
  **AIS boundary:** AIS is the agent-facing projection of selected enforcement and evidence boundaries.

- **Adjacent work:** *From CI/CD to ACG: From Tests to Courts in Agentic Software Development*  
  **Supplies:** Governed development, adjudication, promotion, and revision lifecycle.  
  **AIS boundary:** AIS is one reusable interaction profile inside that broader lifecycle.

An interface contract should bind:

$$
\begin{aligned}
A= (&agent, task, authority, constraints, action\_surface, \\
&effect\_surface, observers, evidence\_schema, recognizer, \\
&feedback, recovery, claim\_ceiling)
\end{aligned}.
$$

The contract distinguishes attempting an action, producing an effect, observing an effect, validating evidence, and recognizing progress. A useful feedback channel explains the smallest lawful next step while respecting privacy and security. A refusal can block one transition without destroying the task's recoverable state.

AIS must measure both false admission and false refusal. A surface that blocks bypass but prevents legitimate alternative implementations, hides uncertainty, or makes recovery impossible is not well governed. Changing the agent, toolchain, task distribution, environment, or adversarial budget may invalidate prior minimality and coverage claims.

The universal GSM can type   
`OPERATES_THROUGH_INTERFACE`, `ATTEMPTS_EFFECT_ON_SURFACE`,  
`OBSERVED_BY_WITNESS`, `SUBMITS_EVIDENCE_UNDER_SCHEMA`, `RECOGNIZED_FOR_CLAIM`,  
`REFUSED_WITH_FEEDBACK`, `RECOVERS_BY_ALLOWED_TRANSITION`, `FALSELY_ADMITTED_BY`,  
`FALSELY_REFUSED_BY`,  
and   
`REVISED_FOR_AGENT_POPULATION`. These relations keep interaction, evidence, recognition, and standing distinct.

This integration establishes four editorial commitments: classify AIS as a recognition-and-evidence interface profile; adopt the interface-contract envelope; require false-admission, false-refusal, recovery, and population-shift evaluation; and reserve authority and standing for the governing structures outside the interface itself.

## Context-Bound Recognition Across Domain Effects

The fixed-seed comparison with *Everything Is a Compiler*, *Meaning Crystals*, CCM, and *Classified Earthworks* reveals that an agentic interface recognition event depends on more than the visible action and evidence surface. It also depends on the exact active context and the domain authority under which the apparent progress is interpreted.

$$
\begin{aligned}
R= (&agent, task, context\_snapshot, action, effect, domain, \\
&evidence, recognizer, standing, feedback, recovery)
\end{aligned}.
$$

CCM determines which constraints, sources, omissions, and goals are active when the agent encounters the interface. Two byte-identical effects can receive different lawful dispositions under different task, authority, or risk contexts. The interface should therefore bind recognition to the exact context snapshot used, while keeping context selection independently challengeable.

Meaning crystals can provide stable instructions, evidence schemas, or domain objects, but neither stability nor selection into context grants standing. The compiler lens can describe the passage from intent through action to effect and recognition only when preservation and remainder obligations are explicit. Interface success does not validate that broader lens.

*Classified Earthworks* supplies a hard domain case. An agent may correctly submit a sample, route a batch, or produce a material passport while lacking professional, regulatory, environmental, or site authority. AIS can expose missing evidence and lawful next steps; it cannot convert a recognized workflow transition into a safety certification or placement authorization.

The universal GSM can type   
`RECOGNIZES_UNDER_CONTEXT_SNAPSHOT`,  
`USES_CRYSTALLIZED_INTERFACE_OBJECT`, `INTERPRETS_EFFECT_IN_DOMAIN`,  
`REQUIRES_DOMAIN_AUTHORITY`, `ACKNOWLEDGES_WORKFLOW_PROGRESS_WITHOUT_`  
`CERTIFICATION`,  
and   
`REOPENS_RECOGNITION_AFTER_CONTEXT_REVISION`.

This randomized review adds three open editorial questions: bind recognition events to exact active-context snapshots; preserve context admission and interface recognition as separately challengeable decisions; and require domain-specific authority ceilings whenever an interface recognizes progress toward physical or regulated effects.

## Recognition Is One Layer of an Agentic Boundary

Downstream uses place Agentic Interface Surfaces inside work custody, adversarial review, admissibility engineering, observability, cyber-physical control, governance-gap analysis, and protected enforcement. Together they show that an agent-facing surface is not one screen or API. It is a layered relation among what an agent can perceive, attempt, affect, evidence, have recognized, and repair:

$$
\begin{aligned}
AIS^*= (&orientation, action\_surface, effect\_gate, observers, \\
&evidence\_path, recognizer, feedback, recovery, coverage, \\
&claim\_ceiling)
\end{aligned}.
$$

Work custody uses AIS to require evidence before recognizing transfer or completion, while leaving the assignment of responsibility to the custody protocol. Adversarial alternation uses AIS to recognize builder progress only after reproducible effect evidence. Admissibility Engineering and Governance Coverage Gaps test whether hidden tools, credentials, adapters, retries, and lower paths bypass the declared surface.

The Constitutional Observability Platform treats AIS as one interface family inside a wider evidence loop. The Integrity Enforcement Layer places protected transition enforcement behind it. The constitutional syscall architecture supplies a device-facing case in which an accepted request, observed effect, and recognized completion remain distinct. Classified Earthworks supplies the human and regulatory ceiling: a workflow step can be recognized without granting professional judgment, material safety, site permission, or regulatory approval.

The reverse-dependency result is a separation rule. Presentation does not imply reachability; reachability does not imply authorization; attempted action does not imply effect; evidence does not imply adequate coverage; recognition does not imply truth, standing, certification, or custody disposition. A useful AIS profile must state which layer produced each outcome and where the next lawful transition resides.

The universal GSM can type   
`PRESENTS_AGENT_CONSTRAINT`, `EXPOSES_ACTION_SURFACE`,  
`MEDIATES_EFFECT_BEHIND_INTERFACE`, `OBSERVES_EFFECT_SEPARATELY`,  
`RECOGNIZES_CLAIM_SCOPED_PROGRESS`, `TESTS_INTERFACE_BYPASS`,  
`RETURNS_RECOVERABLE_NEXT_STEP`, and   
`WITHHOLDS_DOMAIN_CERTIFICATION`.

This reverse-dependency review establishes four editorial commitments: adopt the layered AIS contract; separate presentation, effect mediation, observation, and recognition; require coverage and bypass claims to bind the actual lower paths; and prohibit recognized progress from inheriting professional, regulatory, truth, authority, or custody standing.

## 14. Counterevidence and Failure Tests

AIS must narrow, revise, or fail if: (1) instruction-only interfaces perform equally well; (2) receipts add no predictive value; (3) narrative claims correlate reliably with independent effects; (4) recognition blocks legitimate alternative implementations; (5) agents optimize receipts instead of outcomes; (6) a validator encodes the wrong specification; (7) implementation and validator share a defect; (8) evidence is self-issued without independence; (9) receipts are forged; (10) receipts are replayed; (11) stale evidence is accepted; (12) evidence from one environment is reused in another; (13) the exact subject is unbound; (14) a partial effect is reported complete; (15) an external effect escapes observation; (16) absence of evidence is treated as evidence of absence; (17) one receipt promotes unrelated capability claims; (18) a bypass reaches recognition without evidence; (19) a bypass reaches the effect outside the gate; (20) refusal prevents all recovery; (21) error feedback is not actionable; (22) error feedback leaks protected information; (23) retry erases failed attempts; (24) agents can alter validators; (25) agents can suppress negative receipts; (26) audit uses only the same evidence as implementation; (27) instrumentation changes the behavior measured; (28) high coverage hides low evidentiary quality; (29) deterministic audit claims depend on nondeterministic inputs; (30) minimality is inferred from one agent or test suite; (31) a new agent population defeats the constraints; (32) over-specification prevents valid innovation; (33) under-specification permits semantic divergence; (34) the term incentive lacks an observable feedback link; (35) a choke point is advisory rather than binding; (36) a choke point is binding but semantically misplaced; (37) GMB storage is mistaken for validation; (38) source claims of inevitability or losslessness are repeated as findings; (39) implementation standing is inferred from architecture; or (40) publication proceeds without prior-art and empirical comparison.

## Recognized Progress Is Not Necessarily Real Progress

### Public orientation

Agentic Interface Surfaces define how an agent encounters constraints, proposes actions, observes outcomes, and earns recognition for progress through recorded effects. The central value is closing the loop between request, realization, verification, and receipt. A recognized interface event does not automatically establish that the intended real-world outcome occurred.

### Adversarial tests

1. **Recognition-gaming attack.** The agent produces the event the interface rewards without completing the underlying task. Recognition rules need subject-bound outcome checks.
2. **Display-success attack.** A UI changes while backend or external state does not. Visual, semantic, and effect witnesses must remain distinct.
3. **Backend-success attack.** State changes correctly but the interface reports failure, causing duplicate action. Idempotency and reconciliation are required.
4. **Simulation-reality collapse.** A test or preview effect is confused with a production effect. Environment and consequence class must be bound to every receipt.
5. **Hidden-side-effect attack.** A successful action also changes unrelated state, privacy, cost, or authority. Evidence must cover declared side effects and remainder.
6. **Stale-observation attack.** The agent acts on cached or delayed interface state. Freshness, ordering, and conflict outcomes need explicit profiles.
7. **Accessibility attack.** The surface is machine-readable but not understandable or controllable by affected humans. Agent usability cannot substitute for human contest and remedy.
8. **Nonprogress-loop attack.** Repeated retries generate receipts without moving the task. The surface needs nonprogress detection, reconsideration, budget, and lawful stop.

### Claim and evidence ceiling

The paper specifies a recognition-and-evidence interface profile. It does not prove task completion, user benefit, safety, accessibility, or effect coverage merely because the interface records success. Recognition is one layer inside a wider claim-witness chain.

Claims about agent performance, GUI reliability, automation safety, human factors, accessibility, or cross-domain effectiveness require external comparison and measured evidence. Internal examples establish architectural use only. No external research was added in this pass.

### Reader-facing consequence

The public standard is that an agent should not be able to declare success because it clicked the right place or received the expected message. It must bind recognition to the intended subject, actual effect, evidence, and remaining uncertainty.

## Conclusion

Agentic Interface Surfaces make progress a governed recognition decision rather than a narrative achievement. The interface should expose what must be true, constrain which effects are reachable, collect evidence from the relevant boundary, and refuse credit when the claim outruns the observation.

This does not constrain an agent into inevitable correctness. It constrains one path from action to recognized progress. The remaining work is empirical and adversarial: prove that the surface measures the intended effect, resists bypass and metric gaming, supports lawful repair, and remains useful across changing agents and environments.

## Reference and Verification Note

### Author corpus interfaces inspected under exact custody

Ableman Adam Ableman *Reasoning by Way of Receipts.*

Ableman Adam Ableman *Effect Sovereignty.*

Ableman Adam Ableman *Constraint-Bearing Composability.*

Ableman Adam Ableman *Universal Governance Kernel.*

### External verification required

No external literature was consulted. Publication comparison should examine agent-environment interfaces, reinforcement learning and reward design, mechanism design, capability security, design by contract, runtime verification, observability, test adequacy and mutation testing, formal methods, event sourcing, evidence and audit systems, Goodhart-style metric failure, and human-computer interaction. Novelty, efficacy, security, and generality remain unestablished.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that agentic Interface Surfaces (AIS) define the boundary through which an acting system encounters constraints, attempts effects, receives feedback, and earns recognition for progress. Its nearest external comparison fields are provenance, observation, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Telemetry can be complete at the instrumented boundary while omitting the causal variable, real-world effect, or authority question that matters. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E2]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E3]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

**[E4]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E5]** W3C. *Trace Context, Level 1*. W3C Recommendation, 23 November 2021. https://www.w3.org/TR/trace-context/ **Relationship:** Adjacent distributed tracing standard for propagating trace identity across service boundaries.

**[E6]** Karen Scarfone, Murugiah Souppaya, and Donna Dodson. *Secure Software Development Framework (SSDF) Version 1.1*. NIST SP 800-218, 2022. DOI: 10.6028/NIST.SP.800-218. https://doi.org/10.6028/NIST.SP.800-218 **Relationship:** Adjacent secure-development framework for preparation, protection, production, and vulnerability response.

**[E7]** Richard Cyganiak, David Wood, and Markus Lanthaler, eds. *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation, 25 February 2014. https://www.w3.org/TR/rdf11-concepts/ **Relationship:** Adjacent graph data model and identity baseline.

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

**[A6]** Adam Ableman. *The Constitutional Observability Platform*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-9FC6DF9C2BCB38DA`;  
source SHA-256  
`D93D41518A823703E1076B02D95D28BD7ADF29D3DC15760E0165E84E28BC70B9`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Testing for Deriving Observable State of Software Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-BAA7A4A4150F5D66`;  
source SHA-256  
`0B6AAC8B71DA25E24F7FB4A018692F609096DBA8383C9C8C0AC15F1AF711B3A8`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

Adam Ableman *Semantic Coordinate Identity Tokenization (SCIT).* Zenodo, 2026. doi:10.5281/zenodo.20532070

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847384](https://doi.org/10.5281/zenodo.23847384)
