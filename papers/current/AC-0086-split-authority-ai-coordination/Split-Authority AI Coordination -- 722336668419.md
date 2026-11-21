# Split-Authority AI Coordination

## A Constitutional Protocol for Separating Mandate, Specification, Execution, Verification, and Effect in Human-AI System Construction

### A Coder necessarily interprets during lowering and must surface gaps rather than pretend to execute without interpretation.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

AI-assisted construction often lets one conversational agent interpret a request, choose an architecture, write artifacts, run tests, judge success, and present the result. This concentration is efficient, but it hides where intent became specification, where specification became implementation, who authorized deviations, which evidence supports success, and whether an external effect occurred. A coherent output can therefore validate the assumptions that produced it.

The source paper introduces **Split-Authority AI Coordination (SAAC)**, using Governor, Coder, Codex, and Journal roles to separate semantic authority from execution. This revision preserves that insight while expanding the protocol into five authority-bearing functions: mandate, specification stewardship, execution, independent verification, and external effect. The Codex is a versioned contract binding these functions; the Journal becomes a custody-preserving evidence and correction ledger rather than an informal feedback channel.

The central correction is that role separation does not itself create legitimate authority or correctness. A Governor receives a bounded mandate; it does not own the user's meaning. A Coder necessarily interprets during lowering and must surface gaps rather than pretend to execute without interpretation. A verifier can establish only the claims supported by its observations and tests. An effect authority can commit only within a named capability and jurisdiction. Logical roles can still collude, share correlated failures, or be instantiated by one model under multiple prompts. Independence, non-collusion, source custody, claim ceilings, and recovery must be tested.

SAAC therefore makes a narrower claim than the source. Under an exact Codex, bounded role authorities, independently checkable evidence, declared variability, and explicit effect gates, split authority can make specification drift and self-validation more visible and easier to refuse. It does not guarantee identical outputs, specification completeness, correctness, legitimacy, or cross-model reproducibility. The paper supplies a formal transition protocol, conflict and deadlock rules, cold-boot and provider-substitution obligations, counterevidence, conformance requirements, and placement in the full realization funnel.

## 1. Problem and Claim Ceiling

A unified construction agent may perform all of the following:

* infer the principal's objective;
* decide which requirements matter;
* write or revise the specification;
* select tools, dependencies, and architecture;
* produce implementation artifacts;
* run tests and choose what counts as evidence;
* interpret failures;
* declare completion;
* trigger external effects.

The problem is not that one model can never perform several tasks. The problem is that the resulting claim has no visible authority topology. A reader cannot tell whether a requirement came from the principal, a specification steward, an executor convenience, a test limitation, or a post hoc explanation.

SAAC's thesis is:

> Construction becomes more governable when mandate, specification, execution, verification, and external effect are represented as distinct authorities connected by exact artifacts, explicit decisions, and independently checkable evidence.

This paper does not establish that:

* semantic authority belongs inherently to a Governor role;
* a Codex is complete, correct, legitimate, or self-authorizing;
* a Coder can implement rich specifications without interpretation;
* logical role separation implies organizational, provider, model, data, or infrastructure independence;
* multiple agents are safer merely because they are multiple;
* passing gates proves all intended behavior or external effects;
* heterogeneous models should produce byte-identical implementations;
* every error is cleanly attributable to specification or execution;
* iteration converges monotonically toward completeness;
* the reported empirical improvement in the source is publication-grade evidence;
* any implementation, deployment, or external action is authorized here.

The bounded claim is architectural: explicit authority and evidence boundaries can expose failure classes that a unified conversational loop tends to hide.

## 2. Roles, Authorities, and Artifacts

SAAC distinguishes a **role** from the person, model, process, or organization that realizes it. One actor may realize several roles across a program, but incompatible roles should not be combined for the same governed transition unless the exception is explicit and the claim ceiling is reduced.

### 2.1 Principal or Mandate Authority

The **Principal** supplies or delegates the objective, scope, values, constraints, resources, and effect authority. The principal may be a person, team, institution, or prior constitutional process.

The principal does not need to write the technical specification. It retains standing over the mandate and must be able to detect, contest, revise, or withdraw delegated bindings within the declared regime.

### 2.2 Governor or Specification Steward

The **Governor** translates the mandate and accepted evidence into a versioned Codex. It declares requirements, invariants, tolerable ambiguity, interfaces, phases, refusal conditions, test obligations, and claim ceilings.

The Governor's authority is delegated and bounded. It cannot invent the principal's objective, widen jurisdiction, authorize external effects, validate its own completeness, or treat silence as permission.

### 2.3 Coder or Executor

The **Coder** lowers the admitted Codex into implementation candidates and execution records. It may choose among explicitly permitted realization alternatives.

The Coder cannot avoid interpretation altogether. Every lowering selects representations, algorithms, dependencies, defaults, and environment behavior. Its obligation is therefore not **no interpretation**, but **no silent semantic invention**. When the Codex underdetermines a governance-relevant choice, the Coder emits `GAP` or

`DEFER` rather than laundering its choice into the specification.

### 2.4 Verifier

The **Verifier** evaluates the candidate against the exact Codex, environment, evidence contract, and claim ceiling. It should be independent enough for the claimed risk: separate prompts are weak separation; distinct code paths, tools, providers, data, organizations, or human review may provide stronger separation.

Verification returns a bounded finding, not truth. The verifier cannot grant authority absent from the mandate or prove unobserved external effects.

### 2.5 Effect Authority

The **Effect Authority** holds the capability to commit a candidate into an external or canonical domain. Examples include merging code, deploying a service, publishing a record, changing data, sending a message, or operating hardware.

Execution success is not effect authority. Verification success is not effect authority. The effect boundary remains separately authorized, scope-bound, time-bound, and receipted.

### 2.6 Codex and Journal

The **Codex** is the versioned construction contract binding mandate, requirements, invariants, interfaces, permitted variation, tests, authorities, environments, evidence, effects, nonclaims, and revision rules.

The **Journal** is an append-only or equivalently tamper-evident evidence and correction ledger. It records proposals, gaps, assumptions, decisions, executions, observations, failures, refusals, effect attempts, disputes, and successor relations. It is not authoritative merely because it is a log.

## 3. Formal Protocol

A configured SAAC instance is:

$$
P = \langle M, G, X, V, E, K, J, Q \rangle,
$$

where:

* $M$ is the exact mandate and delegation state;
* $G$ is the specification-steward role;
* $X$ is the executor role;
* $V$ is the verification role;
* $E$ is the effect authority;
* $K$ is the versioned Codex family;
* $J$ is the evidence and correction journal;
* $Q$ is the quorum, conflict, recovery, and succession policy.

For Codex version $K_t$, the normal flow is:

$$
K_t = Specify_G(M_t, state_t, evidence_t),
$$

$$
(I_t, r_X) = Execute_X(K_t, env_X),
$$

$$
(d_t, r_V) = Verify_V(K_t, I_t, env_V, evidence_t),
$$

where:

$$
d_t \in \{ADMIT, DEFER, REFUSE, GAP\}.
$$

An external commit is possible only when the configured effect rule admits it:

$$
\begin{aligned}
&Commit_E(I_t) \text{ may occur only if } d_t = ADMIT \\
&\land Capability_E(target, effect, scope, time) \\
&\land Q_t
\end{aligned}.
$$

`ADMIT` supports only the exact claim tested.

`DEFER` identifies missing resolvable evidence or authority. `REFUSE` states a rule-bound inadmissibility. `GAP` states that the representation, identity, specification, environment, or observation is insufficient to decide.

Codex revision is a governed successor transition:

$$
K_{t+1} = Amend_G(K_t, M_t, J_t, authority_t).
$$

The predecessor remains reconstructable. A failing implementation does not automatically authorize a change to the mandate. A Governor cannot retroactively edit $K_t$ to make $I_t$ conform; it must create $K_{t+1}$ and preserve the failed relation to $K_t$.

## 4. Separation Invariants

The protocol depends on behavioral separation, not job titles.

### 4.1 No Self-Granting Authority

No role may manufacture the authority by which its own output becomes binding. The Governor needs mandate authority; the Coder needs an admitted Codex; the Verifier needs an exact evidence scope; the Effect Authority needs a capability and commit policy.

### 4.2 No Silent Semantic Widening

The Coder may realize permitted variability but may not silently widen requirements, authority, effects, jurisdiction, or claims. The verifier must test obligation carriage across lowering and composition [CBC].

### 4.3 No Self-Verification at the Claimed Independence Level

The same model can perform an exploratory self-check, but that evidence cannot be labeled independent. Independence claims must name the separated failure modes and shared dependencies.

### 4.4 No Verification-to-Effect Collapse

A passing verdict does not itself merge, deploy, publish, transmit, or mutate. The effect authority remains distinct and may still refuse.

### 4.5 No Journal-to-Truth Collapse

A journal entry proves that a record was retained under a named process. It does not prove the record's factual correctness, authority, completeness, or external effect.

### 4.6 No Role Permanence

Provider, model, and human identities may change. Authority attaches to declared roles, credentials, mandates, artifacts, and epochs, not to the persistent reputation of one model session.

## 5. Codex Completeness and Tolerable Ambiguity

The source asks the Governor to ensure that the Codex is complete and predicts convergence toward completeness. Rich specifications are rarely complete in an absolute sense. The operational target is **saturation relative to a declared realization surface and claim** [AE].

A Codex should distinguish:

* **closed constraints**, where all conforming implementations must agree;
* **permitted variation**, where different implementations may choose freely;
* **decision parameters**, selected in Instance Configuration;
* **evidence obligations**, which establish bounded claims;
* **known gaps**, intentionally unresolved;
* **out-of-scope regions**, excluded from the current claim;
* **revision triggers**, which require a successor Codex.

Let $R(i)$ be the realization surface of invariant $i$ and $C(K,i)$ the portion constrained by Codex $K$. The saturation gap is:

$$
Gap(K,i) = R(i) \setminus C(K,i).
$$

SAAC does not require eliminating every gap. It requires that governance-relevant gaps be closed, refused, or declared as tolerable ambiguity. Unrecognized gaps remain a source of plausible-but-wrong realization.

Iteration may improve the Codex, expose a wrong mandate, create regressions, overfit one executor, or increase complexity. Convergence must be measured and can fail. The Journal preserves these failures rather than assuming monotonic progress.

## 6. Correctness Is a Vector of Claims

The statement **correct** is incomplete without a claim dimension and evidence scope. A SAAC candidate may have:

* **structural conformance**: required artifacts, types, and interfaces exist;
* **behavioral conformance**: named behaviors hold under specified tests;
* **constitutional conformance**: authorities, jurisdictions, refusals, and obligations were preserved;
* **evidentiary conformance**: results bind to exact subject, method, environment, and evidence;
* **effect conformance**: a named external effect occurred as intended;
* **operational fitness**: performance, usability, accessibility, and recovery meet bounds;
* **semantic fidelity**: implementation behavior preserves the admitted meaning within declared tolerances.

No role can validate all dimensions merely by running the system. A test suite observes only a bounded surface. A successful effect can still be unauthorized. An authorized effect can still be harmful or incorrect. A byte-identical output can reproduce the same specification error.

The completion claim should therefore be a tuple:

$$
\begin{aligned}
Claim = \langle &K_t, I_t, env, verifier, evidence, dimensions, scope, \\
&nonclaims, ceiling\rangle
\end{aligned}.
$$

## 7. Verification, Courts, and Evidence

The verifier needs access to evidence independent of the Coder's narrative. Minimum bindings include:

* mandate, Codex, and predecessor roots;
* source and dependency roots;
* executor identity, tools, configuration, and environment;
* implementation and build roots;
* tests, fixtures, oracles, and expected failure modes;
* execution receipts and raw observations;
* effect intents and effect evidence;
* unresolved gaps, nondeterminism, and excluded claims.

Reasoning by Way of Receipts treats receipts as typed evidence-bearing transitions rather than decorative logs [RWR]. The Three Hash Rule distinguishes subject, procedure, and result bindings [THR]. These mechanisms strengthen SAAC only when the underlying artifacts and observations are independently inspectable.

Verification must include adversarial cases that can pass ordinary tests: omitted requirements, receipt-without-behavior, authority laundering, wrong environment, stale Codex, hidden dependency, partial implementation, forged identity, unsupported completion, and an effect that occurred without a durable receipt.

## 8. Journal-Driven Correction Without Recursive Capture

The Journal supplies memory across iterations, sessions, models, and providers. It should record:

* the exact subject and Codex version;
* the role and authority producing each entry;
* observed failure or ambiguity;
* raw evidence and interpretation separately;
* proposed correction and affected invariants;
* decision outcome and reason;
* successor roots and invalidated claims;
* conflicts, dissent, deferrals, refusals, and gaps.

The Journal does not update the Codex automatically. Otherwise the execution and observation loop can rewrite its own constitution. A journal entry becomes a revision input; the Governor or other authorized amendment process must create a successor, and the verifier must evaluate the transition.

Journal pressure can also be adversarial. An executor may flood the ledger with low-value gaps, frame its convenience as a specification defect, or omit evidence that would identify an execution failure. Intake, prioritization, provenance, and refusal must therefore be governed.

## 9. Model and Provider Substitution

SAAC should prefer **conformance equivalence** over byte identity. Different compliant executors may produce different code structures, algorithms, explanations, or performance profiles while satisfying the same closed constraints.

Byte-identical results require the Codex to bind every relevant input and source of variation, including tools, dependencies, platforms, locale, clocks, randomness, ordering, network responses, and serialization. Even then, identity is a measured property, not a consequence of role separation.

Provider substitution requires:

1. a portable Codex and exact custody bundle;
2. a role and capability declaration for the successor;
3. no ambient access to prior provider secrets or hidden state;
4. reconstruction of the active mandate, Codex, Journal, open gaps, and claim ceilings;
5. replay or qualification under the successor environment;
6. explicit treatment of behavior differences;
7. no claim that model diversity implies independent reasoning.

Cold Boot Continuity treats reconstruction in a fresh environment as a deployment primitive [CBCP]. A Cognitive ABI supplies an adjacent interface for replacing capability providers while preserving evidence-bearing obligations [CABI]. SAAC supplies the authority topology governing which provider may occupy which role.

## 10. Scaling, Correlation, and Collusion

Multiple Coders can explore alternative realizations, but shared training, prompts, tools, dependencies, datasets, or infrastructure create common-mode failures. Multiple Verifiers can repeat the same blind spot. A Governor and Verifier run by the same organization may remain institutionally coupled.

An independence statement should name dimensions such as:

* model family and provider;
* prompt and context construction;
* implementation language and toolchain;
* test and oracle provenance;
* data and dependency sources;
* infrastructure and credentials;
* organizational control and incentives;
* human review and effect authority.

Quorum is not legitimacy. A majority of correlated agents can agree on an unauthorized or wrong result. The quorum policy $Q$ must remain subordinate to mandate, constitutional constraints, and effect authority.

## 11. Conflict, Deadlock, and Emergency

Split authority deliberately creates the possibility of refusal and deadlock. That is a safety property until the system must decide what to do next.

Required states include:

* Governor-Coder interpretation conflict;
* Coder-Verifier evidence conflict;
* Verifier disagreement;
* mandate ambiguity;
* unavailable role or expired authority;
* no admissible implementation;
* effect uncertainty;
* irreconcilable jurisdictional rules;
* recovery after partial external effect.

The default response is not for one role to absorb another's authority. It is `DEFER`,  
`REFUSE`, `GAP`, escalation, fork, or bounded termination.

An emergency path, if any, must be predeclared with trigger, holder, scope, duration, logging, expiry, recovery, review, and claim consequences. Break-glass use should lower assurance and cannot be retroactively relabeled normal conformance.

## 12. Human Authority, Privacy, and Negative Power

SAAC can constrain AI coordination while still centralizing power in the Governor or exposing users through the Journal. Constitutional use therefore requires:

* visible mandate and delegation;
* practical contest of a Governor interpretation;
* selective disclosure and data minimization;
* no requirement to reveal irrelevant private reasoning or identity;
* accessible refusal, correction, exit, substitution, and fork paths;
* retention and deletion rules consistent with evidence needs;
* protection against retaliation for reporting gaps or failures;
* separation between observation needed for verification and ambient surveillance.

The Ableman Prime Directive places detectability, refusal, exit, and renegotiation of bindings at the center of governed computing [APD]. SAAC supports those capacities only when they are reachable in the configured socio-technical system, not merely named in the Codex.

## 13. Worked Example: A Bounded Software Change

Assume a user authorizes a feature that exports one report from a local application without changing unrelated data or making network calls.

### 13.1 Mandate

The Principal states the required report, local-only boundary, protected data, accepted formats, and no-network invariant.

### 13.2 Codex

The Governor creates $K_1$ with:

* exact repository and source roots;
* feature behavior and nonclaims;
* protected paths and data classes;
* no-network and no-unrelated-mutation invariants;
* permitted library choices;
* acceptance, negative, privacy, and rollback tests;
* evidence and effect boundaries;
* known gaps and escalation rules.

### 13.3 Execution

The Coder produces implementation $I_1$. It discovers that the source does not define how to handle an unsupported field type. Because that choice affects output meaning, it emits `GAP` rather than silently serializing the value.

### 13.4 Revision

The Governor consults the Principal or delegated policy and creates $K_2$, preserving $K_1$ and the gap receipt. The Coder creates $I_2$.

### 13.5 Verification

The Verifier checks positive behavior, protected paths, network isolation, unsupported fields, replay, and exact roots. It returns `ADMIT` for a local candidate package with a claim limited to the tested environment.

### 13.6 Effect

The Effect Authority decides whether to install or merge. A passing verification does not perform that mutation. After effect, a separate observation verifies the installed state. If the commit result is ambiguous, the Journal records `EFFECT_UNKNOWN` and initiates reconciliation.

This example shows the protocol's benefit: the under-specified semantic choice becomes visible, predecessor custody remains intact, verification cannot deploy, and a possible effect is not erased by a missing receipt.

## 14. Corpus Placement and Governed Meaning Base

SAAC is an authority-topology and coordination protocol. Its adjacent corpus relations are:

* **Constitutional Computing** supplies the separation of law, authority, admissibility, execution, effect, evidence, and revision [CC].
* **Admissibility Engineering** supplies the saturation-gap and artifact-layer constraint discipline for the Codex [AE].
* **Constraint-Bearing Composability** tests whether Codex obligations survive modules, adapters, and downstream composition [CBC].
* **A Formal Theory of Work Custody** distinguishes work, artifact, role, delegation, handoff, and result custody [FTC].
* **A Constitution for the Context Window** governs which sources and standing enter each agent role [CCW].
* **A Cognitive ABI** supplies provider- and model-substitution interfaces with evidence-bearing obligations [CABI].
* **Cold Boot Continuity** supplies reconstruction and qualification across fresh environments [CBCP].
* **Operational Epistemic Situational Awareness in Agentic Orchestration** supplies adjacent state and continuation awareness for multi-agent work [OESA].
* **GSOL** can represent governed operations before machine lowering [GSOL].
* **Reasoning by Way of Receipts** and **The Three Hash Rule** supply evidence and binding discipline [RWR] [THR].

The **Governed Meaning Base (GMB)** is current in the author-confirmed lineage `CCF -> CMB -> GMB`. It can preserve mandates, Codices, journals, role profiles, evidence, disputes, gaps, decisions, effects, and revisions. GMB does not become the Principal, Governor, Verifier, or Effect Authority by storing their records. Hyperpedia can project the coordination history for readers and agents while preserving authorship and standing.

## 15. Authorial Compression and External Comparison

SAAC should remain a distinct corpus construct only if its differential obligations exceed ordinary multi-agent prompting or generic separation of duties:

1. exact mandate-to-Codex delegation;
2. no silent semantic invention during lowering;
3. independent verification with declared dependency dimensions;
4. verification-to-effect separation;
5. predecessor-bound Journal correction;
6. explicit `DEFER`, `REFUSE`, `GAP`, and effect-ambiguity states;
7. provider substitution and cold-boot qualification;
8. claim ceilings and non-transferability across configurations.

If these obligations are already fully supplied by Constitutional Computing, work custody, Cognitive ABI, admissibility engineering, and receipt machinery, SAAC may be better presented as a concrete orchestration profile rather than a new foundational system.

Further evidentiary strengthening requires external comparison with separation of duties, dual control, least privilege, capability systems, N-version programming, diverse redundancy, software architecture, formal specification, multi-agent systems, Byzantine-fault models, human-in-the-loop governance, and institutional checks and balances. No external research was conducted in this pass. Novelty and empirical priority remain unestablished.

## Agentic Authority-Topology Profile

Across the completed P1 corpus, Split-Authority AI Coordination is the **agentic authority-topology profile for separating mandate, specification, realization, verification, and external effect in AI-assisted construction**. Its contribution is not the number of agents but the exact distribution of binding authority, custody, evidence, conflict, and negative power across roles and artifacts.

- **Adjacent work:** *A Cognitive ABI for Capability-Centered Computing*  
  **Supplies:** Provider-neutral capability descriptions and substitution obligations.  
  **SAAC boundary:** SAAC configures authority among role realizations that may satisfy those capability contracts.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Live responsibility, handoff, succession, and result-custody relations.  
  **SAAC boundary:** SAAC assigns custody across one construction protocol without redefining work custody generally.

- **Adjacent work:** *Admissibility Engineering*  
  **Supplies:** Constraint saturation, gaps, and pathway assurance.  
  **SAAC boundary:** SAAC places admissibility checks at specification, realization, verification, and effect boundaries.

- **Adjacent work:** *Operational Epistemic Situational Awareness in Agentic Orchestration*  
  **Supplies:** Current-state and continuation orientation for orchestrated work.  
  **SAAC boundary:** OESA informs role decisions; SAAC governs which role may bind them.

- **Adjacent work:** *The Implementation Codex*  
  **Supplies:** IC-to-IR realization package with phases, gates, evidence, and journals.  
  **SAAC boundary:** A Codex is SAAC's construction contract, not an autonomous authority source.

A configured authority topology should bind:

$$
\begin{aligned}
A= (&mandate\_authority, specification\_authority, \\
&realization\_custody, verification\_authority, \\
&effect\_authority, artifacts, dependencies, independence, \\
&quorum, conflict, recovery, contest)
\end{aligned}.
$$

Role separation is a graph property, not a label. Model, provider, prompt, context, tools, data, organization, credentials, test oracle, and effect path can create common-mode control even when role names differ. Every independence claim must name which failure dimensions are separated and which remain shared.

SAAC should return `ADMIT`, `DEFER`, `REFUSE`, `GAP`, `CONFLICT`,  
or `EFFECT_UNKNOWN` at the relevant boundary. A verification result cannot cause the external effect by itself. Deadlock, unavailable roles, emergency paths, role succession, and provider substitution require explicit rules; urgency cannot silently collapse authority into the most capable agent.

The universal GSM can type   
`DELEGATES_MANDATE_AUTHORITY`, `STEWARDS_SPECIFICATION`,  
`HOLDS_REALIZATION_CUSTODY`, `VERIFIES_UNDER_DECLARED_INDEPENDENCE`,  
`CONTROLS_EXTERNAL_EFFECT`, `SHARES_COMMON_MODE_DEPENDENCY`, `ESCALATES_SEMANTIC_GAP`,  
`ENTERS_ROLE_CONFLICT`, `SUBSTITUTES_PROVIDER`,  
and   
`PRESERVES_NEGATIVE_POWER`. These relations make the profile portable and testable.

This integration establishes four editorial commitments: retain SAAC as the agentic authority-topology profile; adopt the topology envelope and six-valued outcome vocabulary; require dimension-specific independence and common-mode disclosure; and classify SAAC as an orchestration profile rather than a new foundational system unless its differential obligations remain unprovided elsewhere.

## Anti-Convergence Authority, Revisable Orientation, Obligation-Carrying Handoffs, and Evidence-Loop Separation

The fixed-seed comparison with Semantic Gravitational Attractors, Recursive Semantic Orientation, transformation-dominant semantic systems, and the Constitutional Observability Platform gives the authority topology four additional common-mode tests:

$$
\begin{aligned}
A^*= (&mandate, specification, realization, verification, \\
&effect, orientation, artifacts, dependencies, \\
&equivalence\_regimes, carriage, observers, independence, \\
&conflict, recovery, contest)
\end{aligned}.
$$

Semantic convergence across prompts, schemas, models, or canonical artifacts can make role outputs easier to compare while also synchronizing the same defect. Shared terminology or hashes do not imply shared authority, semantic correctness, or independent verification.

Recursive Semantic Orientation may supply each role with a bounded current-state model, explicit unknowns, and stopping rationale. It remains an input to role judgment, not a source of mandate or effect authority. Transformation-dominant diagnostics apply to delegation, lowering, handoff, review, and revision: every edge should state which obligations were carried, transformed, lost, refused, or left as remainder.

The Constitutional Observability Platform can supply claim-scoped observers, evidence paths, projection fidelity, and visible `GAP`,  
`CONFLICT`, `STALE`, `UNOBSERVED`,  
and `UNKNOWN` states. Observer roles must remain distinct from specification, verification, and effect authority, and a shared platform cannot independently certify its own control domain.

The universal GSM can type   
`SHARES_CANONICAL_ARTIFACT_WITHOUT_AUTHORITY`,  
`ORIENTS_ROLE_UNDER_CEILING`, `CARRIES_OBLIGATION_ACROSS_HANDOFF`, `REPORTS_HANDOFF_LOSS`,  
`OBSERVED_BY_DISTINCT_ROLE`, `SHARES_PLATFORM_FAILURE_DOMAIN`,  
and   
`REFUSES_SELF_CERTIFICATION`.

This randomized review establishes four editorial commitments: add convergence-regime and orientation risks to the authority topology; require obligation-carriage records at every role handoff; integrate decomposable evidence-loop roles without authority collapse; and treat common platforms and canonical artifacts as disclosed independence limitations.

## Authority Topology, Not Agent Multiplicity

Eight downstream uses apply SAAC to collectives, observability, recursive orientation, semantic attractors, optional coordination, transformation systems, trade authority chains, and work custody. They support SAAC as an orchestration profile for separating mandate, specification, execution, verification, and effect. Multiple agents, providers, or organizations do not create split authority when they share decisive control, collude, inherit one grant, or can silently substitute for one another.

$$
\begin{aligned}
S^*= (&subject, mandate, roles, actors, control\_domains, \\
&grants, artifacts, handoffs, custody, independence, \\
&conflicts, deadlock, emergency, evidence, \\
&effect\_authority, appeal, expiry, successor)
\end{aligned}.
$$

Each role needs a scoped grant, negative powers, inputs, outputs, claim ceiling, and handoff conditions. One actor may occupy several roles only with declared loss of independence and narrowed claims. Distinct actors may still be one control domain through shared prompts, data, model, code, keys, infrastructure, employer, or incentive. Journals preserve attributable state but do not become truth or authority.

Deadlock, disagreement, provider loss, compromise, emergency, and human unavailability require typed outcomes. Emergency combination of roles must be time-limited, receipted, independently reviewed, and unable to retroactively ratify itself. Substitution must preserve obligations, authority limits, refusal behavior, custody, and evidence, not merely output shape.

The universal GSM can type `ASSIGNS_SAAC_ROLE`, `GRANTS_ROLE_AUTHORITY`,  
`SHARES_DECISIVE_CONTROL_DOMAIN`, `COLLAPSES_ROLE_WITH_DISCLOSURE`,  
`TRANSFERS_OBLIGATION_CUSTODY`, `INVOKES_EMERGENCY_ROLE_COMBINATION`,  
and   
`SEPARATES_VERDICT_FROM_EFFECT`.

This review establishes four editorial commitments: retain SAAC as an authority-topology profile; adopt the role and control-domain record; require negative powers, handoff, deadlock, and emergency semantics; and measure independence by decisive control rather than participant count.

## 16. Counterevidence and Failure Modes

SAAC fails or requires revision when:

* the Governor rewrites the Principal's objective without visible delegation;
* the Codex omits a governance-relevant choice and the Coder silently fills it;
* the Coder optimizes for gate tests while violating unobserved intent;
* the Governor defines correctness and also controls the Verifier's observations;
* logical roles share correlated models, prompts, data, tools, or institutional incentives;
* a Journal records claims without raw evidence or predecessor bindings;
* Codex revision retroactively erases a failed implementation or invalidated claim;
* multiple agents agree because they copy the same error;
* byte-identical outputs reproduce a specification defect;
* permitted variability is mistaken for divergence or divergence is hidden as variability;
* verification passes while an external effect is absent, wrong, duplicated, or unknown;
* effect capability leaks into the Governor, Coder, or Verifier role;
* deadlock pressure causes silent authority consolidation;
* emergency use becomes a permanent bypass;
* private user data is exposed to satisfy broad observability demands;
* participation, contest, or provider substitution is only nominal;
* the protocol's cost and latency exceed the risk of the governed task;
* a simpler compiler, review, capability, transaction, or CI process supplies equivalent assurance;
* the claimed empirical improvement cannot be reproduced from exact artifacts;
* no one can determine which role or artifact caused a failure.

The strongest counterexample is **constitutional theater**: the system names every role and produces every receipt, but one actor controls the mandate interpretation, Codex, tests, credentials, and effect path. The topology appears split while authority remains unified.

## 17. Evidence and Conformance Program

A bounded SAAC conformance claim should require:

1. exact mandate, delegation, Codex, source, dependency, and environment roots;
2. role identities, authority scopes, expiry, revocation, and conflict rules;
3. evidence that incompatible roles are behaviorally separated at the claimed level;
4. Codex closed constraints, permitted variation, gaps, nonclaims, and revision rules;
5. no-silent-invention tests and required gap escalation;
6. structural, behavioral, constitutional, evidentiary, effect, and operational claim dimensions;
7. independent-oracle and common-mode-dependency analysis;
8. adversarial fixtures for test gaming, receipt forgery, stale Codex, and authority laundering;
9. effect success, refusal, timeout, duplication, partial commit, and ambiguity tests;
10. Journal append, ordering, truncation, equivocation, privacy, and successor tests;
11. deadlock, unavailable-role, break-glass, expiry, and recovery tests;
12. provider substitution and fresh-environment cold boot;
13. multiple compliant implementations exercising permitted variation;
14. composition tests proving obligations survive downstream interfaces;
15. accessible human contest, refusal, exit, revision, and fork paths;
16. claim-ceiling tests that reject transfer from one configuration or court to another;
17. an exact empirical package for any reproducibility or reliability improvement claim;
18. independent review of at least one low-consequence vertical slice.

Conformance attaches to the named Codex version, roles, artifacts, environment, tests, and evidence. It does not establish that SAAC is universally correct or that any other multi-agent system conforms.

## 18. Realization Funnel

| Stage | SAAC role |
|---|---|
| Possibility | Explore role topologies, mandates, Codex forms, executor and verifier diversity, quorum rules, harmful centralizations, collusion, deadlock, privacy models, and alternative coordination architectures. |
| Specification | Define roles, authority scopes, artifacts, transitions, outcomes, separation invariants, evidence, effects, recovery, claim dimensions, and nonclaims. |
| CM1 | Enumerate configurations satisfying the specification, including nominally split but correlated, centralized, expensive, surveillance-heavy, deadlock-prone, or inaccessible variants. |
| CM2 | Prefer configurations with bounded delegation, practical negative power, independent evidence, privacy, substitution, clear gaps, low correlated failure, recovery, and proportional cost. |
| Instance Configuration | Bind exact principals, agents, providers, models, prompts, contexts, Codex roots, tools, repositories, environments, credentials, verifiers, effect targets, quorums, and courts. |
| Implementation Realization | Build the orchestration, role adapters, Codex compiler, executor, verifier, journal, effect membrane, recovery, and interfaces under separate authority. |
| Evidence | Execute ordinary, adversarial, cross-model, substitution, cold-boot, composition, deadlock, privacy, effect, and recovery tests; preserve failures and uncertainty. |
| Revision | Create successor mandates, Codices, role assignments, tools, policies, courts, and claims when evidence, authority, environment, threats, or objectives change. |

The source paper supplies the core authority-separation proposal. This revision supplies a fuller Specification. Neither paper alone proves a complete Implementation Realization or evidence-qualified instance.

## More Agents Do Not Mean Authority Is Split

### Public orientation

Split-Authority AI Coordination separates mandate, specification, execution, verification, and external effect so one opaque process cannot silently define a task, build the answer, select the evidence, judge success, and commit the result. This is an authority-topology proposal, not a claim that multiple models, agents, or organizations are independent merely because they have different names.

### Adversarial tests

1. **Common-control attack.** Distinct roles share decisive prompts, models, data, code, tools, credentials, infrastructure, employer, or incentives.
2. **Governor-capture attack.** The Governor rewrites the Principal's mandate, defines tests, selects evidence, and controls the Verifier while appearing only to specify.
3. **Test-gaming attack.** The Coder satisfies the visible Codex and fixtures while violating unobserved intent or protected interests.
4. **Journal-oracle attack.** Attributed records become accepted as truth, authority, or complete evidence without independent observation.
5. **Effect-leakage attack.** A Governor, Coder, or Verifier can install, publish, spend, message, or mutate protected state despite nominal role separation.
6. **Deadlock-consolidation attack.** Delay or disagreement is used to silently combine roles and preserve the result as permanently authorized.
7. **Emergency-ratification attack.** Break-glass authority becomes self-justifying, unbounded, or capable of retroactively validating its own action.
8. **Substitution-shape attack.** A replacement provider produces the expected envelope while dropping obligations, refusals, custody, privacy, or evidence semantics.

### Claim and evidence ceiling

SAAC specifies a role, grant, handoff, custody, verification, and effect-separation profile. It does not make a mandate legitimate, a Codex complete, correlated evaluators independent, passing tests true, or external effects successful. Independence is dimension- and claim-specific; one actor may fill several roles only with disclosed loss of standing.

Claims of security, correctness improvement, provider neutrality, organizational independence, cost effectiveness, or general coordination benefit require exact realizations, adversarial campaigns, common-mode analysis, human contest, and external comparison. No external research was added in this pass.

### Reader-facing consequence

The public test is who can reinterpret the mandate, change the rules, build the candidate, choose what is observed, issue the verdict, and cause the real-world effect - and whether any one control domain can secretly do all six.

## 19. Research Agenda and Open Questions

1. Decide whether SAAC is a distinct protocol or an orchestration profile of Constitutional Computing, Cognitive ABI, work custody, admissibility engineering, and receipts.
2. Accept or revise the five authority-bearing functions: mandate, specification, execution, verification, and effect.
3. Decide which incompatible roles may ever be realized by the same person, model, provider, or organization and how standing changes.
4. Define the minimum Codex schema, permitted-variation contract, Journal schema, and outcome taxonomy.
5. Accept conformance equivalence rather than byte identity as the default cross-model target.
6. Define independence dimensions and quorum rules for different risk levels.
7. Define deadlock, emergency, expiry, recovery, and effect-ambiguity semantics.
8. Define human contest, privacy, refusal, substitution, exit, and fork requirements.
9. Select any future low-consequence reference implementation only under separate implementation authority.
10. Authorize external research for a future evidence-qualified revision-readiness, novelty, or empirical-improvement claims.

## 20. Conclusion

Split-Authority AI Coordination begins with a simple and durable insight: the same opaque process should not silently define the task, realize it, select its evidence, judge its success, and commit its effects.

The mature form of that insight is not a two-agent ritual. It is an authority and custody protocol. A Principal supplies a bounded mandate. A Governor creates a versioned Codex. A Coder produces a candidate while surfacing semantic gaps. A Verifier issues a scope-bound finding from independently checkable evidence. An Effect Authority decides whether anything becomes externally consequential. A Journal preserves the exact path and feeds authorized successor revision.

This structure does not make a bad mandate good, a partial Codex complete, a correlated court independent, or a passing test true. It makes those limitations visible and gives the system lawful places to stop. Different executors may remain different. Correctness remains multidimensional. Deadlock may be preferable to silent authority consolidation. External effect remains a separate gate.

SAAC's defensible result is therefore:

> AI-assisted construction becomes more inspectable, substitutable, and governable when authority-bearing functions are separated by exact contracts, explicit outcomes, evidence, and effect boundaries, and when no role can silently promote its own output.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Evidence.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that aI-assisted construction often lets one conversational agent interpret a request, choose an architecture, write artifacts, run tests, judge success, and present the result. Its nearest external comparison fields are ai, governance, security. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E7]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

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

**[SAAC-SOURCE]** Adam Ableman. *Split-Authority AI Coordination*. Exact author source SHA-256  
`AB9D992A4668946DB17F530B31BDD6DD35C6C247769D33F4C48897E29B337064`; unpublished source revised here as an AI-assisted integrated edition.

**[CC]** Adam Ableman. *Constitutional Computing*. Exact reviewed source SHA-256  
`A1EF0D1F7B5DF84A107E986421EAA95827AEDCB801B7DA63F72BEECA6047BE8D`; supplied Zenodo title match, with exact publication identity retained separately.

**[AE]** Adam Ableman. *Admissibility Engineering*. Exact reviewed source SHA-256  
`FA80D5895A569839958193735B754BE62EE20E1B399A06CB3BA959614DEBF7A3`; separately custodied reviewed source.

**[CBC]** Adam Ableman. *Constraint-Bearing Composability*. Exact reviewed source SHA-256  
`BEEA0B56DBF7DC5274307E95E08AF0576A9F91A729C1962765361ADA34488B62`; supplied Zenodo title match, with exact publication identity retained separately.

**[FTC]** Adam Ableman. *A Formal Theory of Work Custody*. Exact reviewed source SHA-256  
`49C38F60B95E107F8B3D864ACAFB4C49067A146C807E5248307DE7B009AD4696`; separately custodied reviewed source.

**[CCW]** Adam Ableman. *A Constitution for the Context Window*. Exact reviewed source SHA-256  
`C4F6CC466FA4306C595AFF66D9EBD4F396E45B91876E1D32A5027FCF465312EE`; separately custodied reviewed source.

**[CABI]** Adam Ableman. *A Cognitive ABI for Capability-Centered Computing*. Exact reviewed source SHA-256  
`F7A7034BB9E382C91AEA693BD656040A93C5C5B504FE70425A31561CEECDC084`; separately custodied reviewed source.

**[CBCP]** Adam Ableman. *Cold Boot Continuity as a Deployment Primitive*. Exact reviewed source SHA-256  
`747CDF82833B2769317A3E63F0F6BA9D0A2CFA84C83E5A8CD72442F6E49C59F3`; unpublished technical companion.

**[OESA]** Adam Ableman. *Operational Epistemic Situational Awareness in Agentic Orchestration*. Exact reviewed source SHA-256  
`7712462638A0BEDB1412B7F089C39D226AE24864FA15D7C667753AEE23795B1B`; separately custodied reviewed source.

**[GSOL]** Adam Ableman. *GSOL v0.1: Governed Semantic Operation Language*. Exact reviewed source SHA-256  
`44F8689BF2FD50670CD25347FB2363491115CA7C049C2BBF71D7286A226DD1AC`; supplied Zenodo title match, with exact publication identity retained separately.

**[RWR]** Adam Ableman. *Reasoning by Way of Receipts*. Exact reviewed source SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`; separately custodied reviewed source.

**[THR]** Adam Ableman. 2026. *The Three Hash Rule*. Zenodo. DOI:   
  `10.5281/zenodo.20788617`. Exact reviewed Markdown source SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.

**[APD]** Adam Ableman. *Turing Completeness and the Ableman Prime Directive*. Exact reviewed source SHA-256  
`80F4FCB00B214D22BF0E0A2D67E726DBA4410BAA751300A24DAAD2610E6C395E`; separately custodied reviewed source.

No external research was conducted in this pass. Current primary-source comparison and a conventional bibliography are required for a future evidence-qualified revision readiness, novelty, or empirical-improvement claims.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Governed Semantic Operation Language.* Zenodo, 2026. doi:10.5281/zenodo.21214886

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848231](https://doi.org/10.5281/zenodo.23848231)
