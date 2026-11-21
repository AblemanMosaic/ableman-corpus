# Constitutional Context Management (CCM)

## Working-State Governance, Relevance as Admission, and Hash-Bound Attention in Generational Systems

### CCM transforms context from a transient token buffer into a typed, hash-bound, admissible set of active commitments.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Contemporary AI systems rely on context windows as ephemeral substrates for reasoning. These windows are finite, mutable, and opaque, leading to silent drift in meaning, loss of invariants, and unobservable degradation of system behavior. While Governed Context & Memory (GCM) establishes persistence, provenance, and hash-bound memory, it does not govern what is *active* at any given moment.

This paper introduces **Constitutional Context Management (CCM)**, a framework for governing working state. CCM transforms context from a transient token buffer into a **typed, hash-bound, admissible set of active commitments**. It defines context artifacts, context lanes, and relevance as a governed admission function. It introduces context hashing for drift detection, amendment semantics for controlled evolution, and refusal as a first-class response to context insufficiency.

We formalize a separation:

* GCM governs persistence across time
* CCM governs activation in the present

Together, they produce continuity without drift.

We argue that reliable reasoning, long-horizon interaction, and safe agent execution require governance not only of memory, but of **attention itself**.

---

## 1. The Failure of Ungoverned Context Windows

Modern systems implicitly define:

```
Context approximately Token Window
```

This approximation is operationally convenient but incomplete: a provider token window is one serialization surface, not a sufficient model of governed working state.

The context window:

* decays under length constraints
* truncates without semantic awareness
* is reordered or summarized without constraint
* is not inspectable as a structured entity

By itself, it supplies no declared governance contract.

This produces a distinct failure mode:

> **Definition (Context Drift).**
> Context Drift occurs when the effective working state of a system diverges from its declared or intended constraints due to untracked mutation, truncation, or recomposition of context.

Unlike memory loss, context drift is silent.

The system continues to produce coherent outputs while no longer operating under the same commitments.

This is not a failure of intelligence.

It is a failure of governance.

---

## 2. Context as Binding, Not Storage

From GCM, we distinguish:

* Memory -- persistent, external, retrievable artifacts
* Context -- working attention

CCM refines this further:

> **Context is the binding layer that determines which meaning is active.**

Formally:

```
Meaning = f(Memory, Context Binding)
```

Two systems with identical memory can produce divergent outputs if their context binding differs.

Therefore:

* Governing memory is insufficient
* Governing context is required

---

## 3. From Token Streams to Context Artifacts

CCM replaces monolithic context with **Context Artifacts**.

> **Definition (Context Artifact).**
> A context artifact is a discrete, typed, hash-bound unit of meaning with declared provenance and admission policy.

Each artifact contains:

* canonical content
* type
* provenance (user, system, retrieval)
* semantic hash under a declared context lens
* admission constraints
* relevance bindings

Working context becomes:

```
W = {C_1, C_2, C_3, ...}
```

Context is no longer only a stream. It is a typed, task-relative configuration of commitments whose ordering and projection may also matter.

### 3.1 Typed active-context record

Let a context artifact be a typed record rather than undifferentiated prompt text:

$$
\begin{aligned}
C_i = \langle &id_i, v_i, \tau_i, \ell_i, r_i, p_i, \sigma_i, d_i, x_i, \\
&a_i\rangle
\end{aligned},
$$

where $id_i$ and $v_i$ identify the artifact and revision, $\tau_i$ is its type, $\ell_i$ its lane, $r_i$ a content reference, $p_i$ provenance, $\sigma_i$ epistemic or governance standing, $d_i$ declared dependencies, $x_i$ conflicts, and $a_i$ its admission requirements. This is a proposed schema, not a claim that every context representation needs these exact fields.

For task $q_t$, candidate pool $C$, policy/configuration $\Phi_t$, and budget $B_t$, selection produces a typed active state:

$$
W_t = S(q_t, C, \Phi_t, B_t).
$$

The serialized provider input is a projection, not the state of record:

$$
P_t = \Pi(W_t, \alpha_t),
$$

where $\alpha_t$ is the declared provider-adapter profile. $W_t$, $P_t$, and the model's hidden execution state must not be treated as identical.

---

## 4. Context Lanes (Structural Separation of Meaning)

> **Definition (Context Lane).**
> A context lane is a governed channel that constrains which artifacts may be active and how they interact.

CCM defines the following canonical lanes:

* **Identity Lane** -- role, system identity, operating stance
* **Invariant Lane** -- non-negotiable rules and definitions
* **Goal Lane** -- current objectives
* **Constraint Lane** -- operational limits and boundaries
* **Working Knowledge Lane** -- retrieved or active facts
* **Speculative Lane** -- explicitly marked inference (optional)

Each lane:

* enforces type constraints
* prevents cross-lane overwrite
* has independent admission rules
* is hash-governed

This is intended to prevent common collapse modes:

* goals rewriting invariants
* speculation overwriting facts
* summaries mutating constraints

### 4.1 Lanes are profiles, not self-authenticating authority

The six lanes are a useful default profile, not an exhaustive or automatically canonical taxonomy. A domain may need evidence, delegation, temporal, privacy, effect, or contest lanes. Conversely, a small task may lawfully omit optional lanes. Lane membership does not make content true or authoritative: it constrains how a record may be interpreted and combined.

Cross-lane references are necessary. A goal may depend on working knowledge; a constraint may narrow a tool capability; a speculative claim may point to the evidence whose absence keeps it speculative. The invariant is therefore not "lanes never interact" but "cross-lane influence is typed, inspectable, and unable to overwrite a stronger lane without the authorized transition for that lane."

---

## 5. Relevance, Admissibility, and Selection

Similarity may generate candidates, but it cannot by itself decide what enters working state. CCM separates four questions:

1. **Validity:** Is the artifact well-formed and its referenced content available?
2. **Admissibility:** May it participate under the applicable authority, provenance, scope, and lane rules?
3. **Relevance:** Does it bear on the current task under a declared relation or retrieval rule?
4. **Closure:** Can the selected set fit the budget without losing required dependencies, counterevidence, or controlling constraints?

A compact admission judgment is:

$$
A(q_t,C_i,\Phi_t) \rightarrow
\{\text{ADMIT},\text{REFUSE},\text{HOLD}\}.
$$

Selection then operates only over admissible candidates:

$$
W_t = S\bigl(q_t,\{C_i\mid A(q_t,C_i,\Phi_t)=\text{ADMIT}\},\Phi_t,B_t\bigr).
$$

`HOLD` matters because missing provenance, unresolved contradiction, or an unavailable dependency is not equivalent to a definitive rejection. Relevance determines what may matter *after* legitimacy and admissibility are considered; it is not authority to admit an artifact.

The selection function must declare tie-breaking, dependency closure, conflict handling, ordering, truncation, and nondeterminism. Otherwise two systems can share the same artifact store and policy label while silently producing materially different active states.

## 6. Modes of Context Binding

CCM supports multiple binding mechanisms:

1. **Declared Binding (Human)**

   * explicit tags, anchors, or pinned artifacts

2. **Generative Binding (LLM)**

   * model-mediated selection

3. **Residual Binding**

   * continuation from prior working state

4. **Indexed Binding**

   * precomputed graph or embedding structures

These modes are composable but governed by admission policy.

No binding mechanism bypasses lane constraints.

---

## 7. Independent Commitments and Drift Detection

The source proposed a single hash over a set of artifact hashes. That is insufficient when order, multiplicity, lane position, selected revision, dependency closure, policy, semantic regime, query binding, or provider projection can change meaning. A CCM profile should instead preserve independent commitments.

Following the separation discipline of *The Three Hash Rule*, a context receipt may carry:

* $H_s$: the canonical active-state commitment, including artifact identities, revisions, typed lanes, and any semantically relevant order or multiplicity;
* $H_c$: the admissibility and configuration commitment, including policy, authority, selection profile, budget, and admitted/refused/held decisions;
* $H_m$: the meaning-regime commitment, including lens, canonicalization, interpretation, and required semantic resources;
* $H_r$: a receipt-binding commitment over the task, the preceding commitments, dependency/conflict closure, and the exact projected provider input;
* $H_j$: an optional locality or phase commitment when namespace or phase is material.

This is a CCM integration profile, not a claim that the published Three Hash Rule already implements CCM. Hash equality proves equality of committed canonical inputs under the named algorithms and regimes. It does not by itself prove semantic correctness, completeness, authority, absence of omitted context, or equivalence outside that regime.

Define a context receipt as:

$$
R_t = \langle q_t,H_s,H_c,H_m,H_r,H_j,\pi_t,o_t \rangle,
$$

where $\pi_t$ contains the evidence needed to recompute or verify the commitments and $o_t$ records admitted, refused, held, omitted, and budget-displaced artifacts. Drift is not merely any hash change. It is a mismatch between the actual transition and the transition authorized or predicted under the applicable configuration.

## 8. Transition and Amendment Semantics

Active context is supposed to change between tasks. Treating every change in $W_t$ as a constitutional amendment would make ordinary retrieval impossible. CCM therefore distinguishes four transition classes:

- **Transition:** deterministic recomputation  
  **Example:** a new task selects a different admissible subset under unchanged rules  
  **Required treatment:** new receipt; no constitutional amendment

- **Transition:** governed operational update  
  **Example:** a new evidence artifact is admitted or an obsolete working item is retired under existing authority  
  **Required treatment:** lineage-bearing update receipt

- **Transition:** constitutional amendment  
  **Example:** lane authority, denial rule, selection law, required commitment, or amendment authority changes  
  **Required treatment:** authorized amendment under prior effective law

- **Transition:** undeclared drift  
  **Example:** actual state or projection differs from its authorized inputs or receipt  
  **Required treatment:** refuse, hold, or escalate; preserve the mismatch

An amendment record must identify the predecessor, proposed successor, authority, procedure, changed commitments, effective scope, migration rule, and rollback or refusal posture. The component proposing a change does not acquire authority to ratify its own expansion merely by placing the proposal in context.

## 9. Context Admission as Governance Gate

Context is not passively accumulated.

It is admitted.

Each artifact must pass:

* type validation
* lane compatibility
* invariant consistency checks
* provenance requirements

Admission failure results in:

* rejection
* or escalation

This enforces:

> Not all available context is admissible context.

---

## 10. Context Sufficiency and Capability Claims

The source expression   
`Capability <= Integrity(W_active)` is directionally useful but dimensionally underspecified. CCM should make a task-relative establishment claim instead. Let $Req(q_t)$ be the declared required-context profile and $Cov(W_t,Req(q_t))$ the evidence-backed coverage judgment. Then:

$$
Ready(q_t,W_t)=Valid(W_t)\land Admissible(W_t)\land Closed(W_t,Req(q_t)).
$$

If `Ready` is false or cannot be established, the claimed task capability is not established. The system may narrow the task, seek missing context, return a qualified answer, hold for review, or refuse. It must not silently promote missing evidence into a complete context claim.

This rule has an open-world boundary: $Req(q_t)$ can itself be incomplete or wrong. A serious profile therefore needs declared discovery obligations, counterevidence search, and a receipt for what was searched and omitted. CCM governs a stated context boundary; it does not prove that nothing relevant exists outside it.

## 11. Refusal and Context Insufficiency

CCM extends GCM's principle of explicit ignorance.

If:

```
Required_Context(Q) not-subset-of W_active
```

Then:

```
Respond(Q) = REFUSE or "INSUFFICIENT CONTEXT"
```

Refusal is not failure.

It is:

> Preservation of working-state integrity.

---

## 12. Context as Configuration Topology

Working context forms a structured graph:

* nodes = context artifacts
* edges = relevance, dependency, contradiction
* layers = lanes

This produces a **Context Topology**, not a window.

This topology is:

* inspectable
* queryable
* hash-checkable
* evolution-traceable

---

## 13. Relationship to the Governed Meaning Base and Historical JN References

The source names JN as its canonical semantic substrate. Current corpus terminology uses **Governed Meaning Base (GMB)** under the author-confirmed lineage `CCF -> CMB -> GMB`. Newly generated current-architecture prose therefore uses GMB. JN remains exact historical source language and a distinct system/lineage candidate; this pass does not silently declare JN and GMB identical.

Under the current integration model:

* GMB holds governed semantic records, sources, claims, standing, relations, counterevidence, and revision lineage.
* CCM selects and binds a task-relative active projection from those records.
* The provider context window receives a serialized projection of that active state.
* Receipts link the projection and decisions back to the exact records and configuration that produced them.

GMB admission does not automatically make an artifact active, and CCM activation does not make an artifact true. Storage, standing, admissibility, relevance, activation, projection, execution, and effect remain distinct stages.

## 14. Externalizing the Context Window

The LLM context window becomes a declared projection $P_t = \Pi(W_t,\alpha_t)$ rather than the source of truth. Reproducibility requires more than a stable active-state root: it requires the same projection algorithm and version, provider adapter, tokenizer or serialization contract when material, ordering, truncation rule, and nondeterminism posture.

The projection should be inspectable and receipt-bound. It is deterministic only when its declared projection profile is deterministic; the architecture must not promise determinism while delegating unrecorded selection or rewriting to a model or provider.

## 15. Observability and Control

CCM exposes working state:

* active artifact list
* lane composition
* context hash
* drift/amendment logs
* admission decisions

Users can query:

* "What context is active?"
* "What changed?"
* "Why was this admitted?"

Context becomes visible.

---

## 16. Working-State Governance

CCM can be summarized as:

> Governance of what the system is currently allowed to treat as active meaning.

This reframes context entirely.

Not:

* storage
* buffer
* prompt

But:

* constraint surface
* commitment set
* admissible working state

---

## 17. Agentic and Runtime Implications

Agent failures can arise from unstable context, hidden mutation, unresolved contradiction, prompt injection, omitted dependencies, stale retrieval, or unbounded inference. CCM proposes stable multi-step context binding, reproducibility surfaces, explicit admission decisions, and safe degradation. These benefits remain design hypotheses until a specified runtime profile is implemented and evaluated.

The source named GER/AOK as an intended runtime setting. AOK/AOK-G material is custody-only and excluded from the current Ableman semantic integration scope. This candidate therefore retains that historical source relationship without using AOK as evidence, authority, or an Ableman-system dependency. CCM remains runtime-neutral unless the author later adopts a specific implementation profile.

## 18. Corpus Integration and Layer Boundaries

CCM belongs between governed semantic state and runtime execution:

1. **GMB** retains governed semantic records and lineage.
2. **GCM** governs persistent memory, retrieval boundaries, and ignorance/refusal posture.
3. **Semantic Legitimacy Before Context** requires grounding and admissibility before contextual usefulness can support reasoning.
4. **CCM** constructs the active, task-relative working state and records admission, omission, conflict, and projection decisions.
5. **Reasoning by Way of Receipts** requires explanations to remain linked to exact premises, evidence, scope, and decision lineage.
6. **Admissibility Engineering** constrains realizations so context requirements are structural rather than prompt-only aspirations.
7. A separately authorized runtime may execute under the resulting context; effect authorization remains independent.

The stack does not imply that storage, context selection, reasoning, and execution are one system identity. They are interoperating roles whose exact implementations and authority boundaries require profiles.

## 19. Worked Example: Current Name with Historical Sources

Suppose a task asks for the current name of the corpus's governed meaning architecture. The candidate pool includes an older CCF artifact, a later CMB paper, and a direct author ruling that the lineage is `CCF -> CMB -> GMB` with GMB current.

A similarity-only retriever might select the longer CMB paper and answer with CMB. CCM instead records:

* all three artifacts are relevant;
* the older artifacts remain admissible as historical evidence;
* the direct ruling has current terminology authority for this question;
* the answer uses GMB while citing CCF and CMB as historical lineage;
* no source title or quotation is silently rewritten;
* the selection and omission record explains why the current ruling controlled the answer.

The example illustrates a central point: governing context does not mean deleting obsolete or conflicting material. It means preserving material with typed standing and controlling how it may affect the current task.

## 20. Universal GSM Placement

CCM introduces or depends on the following distinct semantic entities: context artifact, artifact revision, lane profile, lane assignment, active-state set, task, query, selection profile, budget, admission judgment, refusal, hold, omission, dependency, conflict, semantic lens, canonicalization regime, projection profile, provider adapter, active-state commitment, admissibility commitment, meaning commitment, receipt binding, amendment, operational update, drift event, sufficiency judgment, execution request, and effect judgment.

Important adjacencies include:

* an artifact **HAS_REVISION** an artifact revision;
* an artifact revision **ASSIGNED_UNDER** a lane profile;
* an admission judgment **EVALUATES** an artifact revision for a task;
* an active state **SELECTED_UNDER** a policy, budget, and selection profile;
* an active state **DEPENDS_ON** admitted artifacts and declared closure;
* a projection **DERIVED_FROM** an active state under an adapter profile;
* a receipt **BINDS** the task, decisions, commitments, and projection;
* a drift event **CONTRADICTS** an expected or authorized transition;
* an amendment **SUCCEEDS** a prior constitutional configuration.

Lexical co-occurrence or matching hashes do not establish these identity or derivation relations. Each consequential edge requires source or receipt support.

## 21. Realization Funnel

- **Stage:** Possibility  
  **CCM role:** Enumerate context records, lane systems, selection strategies, semantic regimes, budgets, conflict policies, projection adapters, refusal postures, and harmful or null configurations.

- **Stage:** Specification  
  **CCM role:** Define the artifact schema, authority model, admission outcomes, commitments, transition classes, dependency/conflict closure, receipt contract, and falsifiers.

- **Stage:** CM1  
  **CCM role:** Retain every admissible configuration, including expensive, overly restrictive, privacy-invasive, unstable, incomplete, or low-utility configurations.

- **Stage:** CM2  
  **CCM role:** Prefer configurations that preserve controlling constraints and counterevidence, minimize silent omission, expose uncertainty, remain inspectable, and fit declared resource/privacy limits.

- **Stage:** Instance Configuration  
  **CCM role:** Choose exact lanes, laws, lenses, algorithms, budgets, adapters, sources, versions, tie-breakers, and review authorities for one deployment.

- **Stage:** Implementation Realization  
  **CCM role:** Build the store connector, selector, canonicalizer, receipt emitter, projection adapter, refusal path, amendment path, and operator surface.

- **Stage:** Evidence  
  **CCM role:** Preserve test vectors, admitted/refused/held/omitted records, commitment openings, drift probes, projection comparisons, attack results, and human-review outcomes.

- **Stage:** Revision  
  **CCM role:** Amend configuration through prior authority, repair algorithms, migrate records, retain predecessor receipts, and record claim movement.

The present paper operates mainly at Specification and early Configuration. It does not authorize or prove an Implementation Realization.

## Governed Active Working-State Layer

The completed P1 corpus positions Constitutional Context Management (CCM) as the **governed active working-state layer that selects, binds, updates, expires, and receipts context across a sequence of tasks or invocations**. It is not long-term semantic state, one compiled provider window, model memory, or truth by inclusion.

- **Adjacent work:** *A Constitution for the Context Window*  
  **Supplies:** The invocation-scoped constitutional compiler, courts, Context IR, provider projection, and receipts.  
  **CCM boundary:** CCM manages the longer-lived working state from which particular context builds are requested.

- **Adjacent work:** *Constitutional/Crystallized Meaning Base (CMB)*  
  **Supplies:** The historical meaning-base work in the current CCF-to-CMB-to-GMB lineage.  
  **CCM boundary:** Current GMB stores governed semantic state; CCM selects and maintains a task-relative active slice.

- **Adjacent work:** *Technical Brief: Recursive Semantic Orientation and Complex Systems Cognition*  
  **Supplies:** Hypotheses, partitions, unknowns, probes, and stopping.  
  **CCM boundary:** An orientation state can guide CCM relevance without becoming identical to active context.

- **Adjacent work:** *Exigence and the Cognitive Kernel*  
  **Supplies:** Need, attention, custody, sufficiency, and reconsideration.  
  **CCM boundary:** CogK supplies attention pressure; CCM performs governed context selection and amendment.

- **Adjacent work:** *Semantic Legitimacy Before Context*  
  **Supplies:** The admissibility question before material becomes binding context.  
  **CCM boundary:** CCM operationalizes ongoing admission, displacement, and revalidation over working state.

An active-context state should bind:

$$
\begin{aligned}
C= (&work\_id, base\_snapshot, lanes, candidates, \\
&active\_bindings, selection\_basis, omissions, budget, \\
&expiry, receipts, revision)
\end{aligned}.
$$

The GMB snapshot, candidate set, selected working state, invocation Context IR, provider-visible prompt, model output, and external effect remain separate. Hash binding proves commitment to exact bytes or structures under a scheme; it does not prove relevance, completeness, correctness, authority, or semantic equivalence.

Relevance is a governed admission claim, not a similarity score. Selection must expose task, jurisdiction, time, authority, evidence, risk, budget, and displacement consequences. Expiry and eviction require a preservation or loss record where removed material remains relevant to custody, safety, dispute, or revision.

The universal GSM can type   
`CANDIDATE_FOR_ACTIVE_CONTEXT`,  
`SELECTED_UNDER_RELEVANCE_PROFILE`, `BOUND_IN_CONTEXT_LANE`, `DISPLACED_BY`,  
`EXPIRES_FROM_WORKING_STATE`, `PRESERVED_IN_GMB`, `PROJECTED_TO_CONTEXT_BUILD`,  
`HASH_COMMITTED_AS`, `INSUFFICIENT_FOR_TASK`,  
and   
`REVISED_BY_CONTEXT_RECEIPT`. These relations distinguish managed attention from epistemic standing.

This integration establishes four editorial commitments: adopt governed active working-state layer as CCM's official corpus role; adopt the active-context record; preserve the GMB/CCM/ContextBuild/provider-window/output/effect separation; and require relevance, displacement, expiry, and loss to be receipted under explicit profiles.

## Context as Experimental and Decision State

The fixed-seed comparison with *Meaning Crystals*, Agentic Interface Surfaces, *Classified Earthworks*, and Project57 exposes two under-specified CCM roles: active context is both a decision state for consequential work and an experimental condition when behavior is being measured.

$$
\begin{aligned}
U= (&work, context\_snapshot, selection, omissions, standing, \\
&freshness, interface, decision, effect, evidence, \\
&revision)
\end{aligned}.
$$

A context-use receipt should bind what was available, selected, omitted, expired, and provider-visible at the moment a decision, interface recognition, or measured response occurred. It should not imply that all selected material was true or authoritative. Meaning crystals remain candidate context objects whose stability, freshness, standing, and task fitness are evaluated separately.

Agentic interfaces consume the active context indirectly through the agent's recognized constraints and progress conditions. A context revision can therefore change interface behavior without any code or surface change. When that happens, the new recognition regime should be attributable to a context transition rather than presented as an unchanged interface contract.

*Classified Earthworks* demonstrates the consequence boundary: omitting batch lineage, current test results, jurisdiction, or site conditions can turn an apparently coherent context into an unsafe routing state. Project57 demonstrates the experimental boundary: the exact context template, ordering, omissions, memory, system instruction, and provider projection are treatment variables, not incidental prompt metadata.

The universal GSM can type   
`RECEIPTS_CONTEXT_USE`,  
`TREATS_CONTEXT_AS_EXPERIMENTAL_CONDITION`, `CHANGES_RECOGNITION_BY_CONTEXT_REVISION`,  
`OMITS_SAFETY_CRITICAL_CONTEXT`, `BINDS_MEASURED_RESPONSE_TO_CONTEXT`,  
and   
`SELECTS_CRYSTAL_WITHOUT_PROMOTING_STANDING`.

This randomized review establishes four editorial commitments: adopt a context-use receipt; classify context as a controlled experimental condition when responses are measured; require context-to-interface change attribution; and identify safety-critical omission classes for consequential domain decisions.

## Context as a Reconstructable Decision Substrate

Five downstream uses apply CCM to context-window constitutions, earthwork decisions, agent interfaces, meaning crystals, and Meta-Binding tests. They confirm that CCM governs the active working set, not the whole GMB, a memory store, or a hidden prompt. Its product is a versioned decision substrate whose inclusions, exclusions, freshness, standing, and insufficiencies can be reconstructed.

$$
\begin{aligned}
C^*= (&task, subject, generation, purpose, lanes, candidates, \\
&admitted, excluded, ordering, budgets, authority, \\
&freshness, standing, dependencies, omissions, receipts, \\
&expiry, successor)
\end{aligned}.
$$

Relevance is a scoped admission judgment, not truth or importance in general. Lane membership does not authenticate content. Compression, ordering, repetition, omission, tool output, system messages, and retrieval timing can all alter the effective decision surface. A context result must therefore expose controlling exclusions and unresolved dependencies, not merely the material loaded.

Cold boot requires reconstruction from exact source identities, admission decisions, lane rules, budgets, and successor lineage. Hashes can detect drift in a declared artifact but cannot prove that the candidate set was complete, the authority valid, the summary faithful, or the context sufficient. Insufficiency and refusal are lawful outcomes.

The universal GSM can type   
`ADMITS_TO_ACTIVE_CONTEXT`, `EXCLUDES_WITH_CONTEXT_REASON`,  
`BINDS_CONTEXT_LANE`, `REPORTS_CONTEXT_OMISSION`, `EXPIRES_CONTEXT_BINDING`,  
`RECONSTRUCTS_DECISION_CONTEXT`, and   
`DOES_NOT_CONFER_TRUTH`.

This review establishes four editorial commitments: adopt the reconstructable context record; treat relevance as scoped admission; make omission, order, freshness, and insufficiency first-class; and require exact reconstruction evidence without promoting hashes or summaries into semantic proof.

## 22. Failure Modes and Falsification Program

A CCM profile is weakened or falsified within its stated scope if any of the following occurs:

1. A materially different ordered or lane-typed active state produces the same state commitment without a declared equivalence rule.
2. A lens erases a distinction that its specification says it preserves.
3. A stable receipt verifies while the provider receives a materially different projection.
4. A required dependency or controlling counterexample is omitted while closure reports success.
5. A speculative record influences an invariant or fact lane without a typed, authorized transition.
6. Prompt content expands its own authority merely by being selected into context.
7. Two implementations using the same deterministic profile select different states without recording nondeterminism.
8. A withdrawn or superseded revision remains active without explicit historical standing.
9. An unavailable source is silently replaced by model recall.
10. Any normal task-to-task selection change is misreported as constitutional drift, making the system unusably amendment-heavy.
11. A constitutional rule changes as an ordinary operational update, laundering amendment authority.
12. Privacy-sensitive material is committed or exposed beyond its declared disclosure profile.
13. Refusal occurs despite an admissible, sufficient context whose required proof is available.
14. The system claims completeness without a declared search boundary or omission receipt.

Evaluation should include positive, negative, mutation, truncation, prompt-injection, stale-revision, conflicting-evidence, missing-source, ordering, budget-pressure, adapter-mismatch, and replay tests. Passing those tests establishes only the tested profile and threat model.

## Govern the Present Without Pretending It Is Complete

### Public orientation

Constitutional Context Management governs the active working state used for a present decision. It treats admitted instructions, evidence, definitions, constraints, uncertainties, and omissions as typed and provenance-bearing commitments rather than as an invisible prompt buffer. The goal is reconstructable orientation and bounded refusal, not a claim that a context can contain everything relevant.

### Adversarial tests

1. **False-sufficiency attack.** The context passes a completeness check because the checklist omitted the decisive category. Sufficiency must be claim-, task-, and consequence-scoped.
2. **Stale-state attack.** A once-valid instruction, fact, permission, or dependency remains active after amendment, revocation, or environmental change.
3. **Provenance-as-truth attack.** A source is known exactly and is therefore treated as correct, authoritative, current, or relevant.
4. **Context-poisoning attack.** Adversarial material enters through retrieval, user content, tools, inherited state, or summaries and is promoted into an operative commitment.
5. **Compression-loss attack.** Summarization preserves fluency but erases qualifiers, dissent, negative evidence, standing, or unresolved obligations.
6. **Privacy-and-secrecy attack.** Reconstructability expands retention or disclosure of sensitive material beyond the task's legitimate need.
7. **Liveness attack.** Repeated sufficiency and governance checks prevent useful work or make refusal the only stable state. The policy needs consequence-proportional continuation rules.
8. **Layer-collapse attack.** CCM, the GMB, retrieval, the universal GSM, and a model context window are treated as one store or one authority surface.

### Claim and evidence ceiling

The paper specifies a governed active-working-state layer with admission, amendment, sufficiency, omission, and refusal semantics. It does not guarantee complete knowledge, correct retrieval, truth, authority, privacy, safety, or good decisions. A context receipt establishes only the bounded state and procedures it actually covers.

Claims about comprehension, error reduction, privacy, security, latency, cost, organizational performance, or model behavior require exact implementations, comparison baselines, and external evidence. The GMB can supply governed records to CCM, but it does not automatically determine the active context; CCM can prepare a context, but it does not acquire GMB standing. No external research was added in this pass.

### Reader-facing consequence

For a reader, the proposal turns "what did the agent know?" into an inspectable question: what was admitted, what was excluded, what had changed, what remained uncertain, and why the system continued or refused.

## 23. Publication Standing and Evidence Limits

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.

---

## Editorial Provenance and Standing

### Source, Identity, and Claim Standing
This is an AI-prepared successor revision candidate derived from one exact author source. The source remains unchanged. The integration custody manifest is   
`work/paper-saturation-v1/evidence/`

`constitutional-context-management/integration-`  
`custody-manifest.v0.1.json`,  
SHA-256  
`9E94E95A00068B6C607C4E6C11FB4D4031D8583D19E92A180F1FB00F8E547AA1`. The integration custody manifest binds that source and six exact internal comparison works by path, size, and SHA-256. Exact custody does not prove the candidate's claims, establish identity among the works, or grant publication standing.
This paper is best treated provisionally as the concise conceptual architecture for governed active context. *Governed Context & Memory (GCM)* supplies the earlier persistence-and-retrieval frame. *A Constitution for the Context Window* is a much larger later treatment of constitutional context compilation, courts, amendments, adapters, delegation, effects, receipts, and conformance. Their adjacency is strong, but this pass does not merge their work identities or declare CCM a version of either paper.
The paper makes architectural and normative proposals. It does not report an implemented CCM runtime, controlled evaluation, security proof, cognitive-science result, or evidence that current AI products satisfy the model. Statements about what a CCM system "will" do are design obligations, not observed product behavior.

## 24. Conclusion

Memory without governance produces drift across time.

Context without governance produces drift across steps.

CCM resolves the second failure.

By transforming context into:

* typed
* hash-bound
* admitted
* observable

it establishes a stable working state.

The central shift is structural:

> Context is not data.
> Context is a set of active commitments.

When those commitments are governed:

* relevance becomes enforceable
* drift becomes detectable
* refusal becomes necessary
* reasoning becomes stable

A system operating under CCM will not proceed under insufficient context.

It will not silently mutate its commitments.

It will not substitute inference for grounding.

Instead, it will preserve its working state--and when that state is insufficient, it will stop.

Not as limitation.

As proof that the system is still intact.

## Corpus-Wide Reference Positioning

This paper argues that contemporary AI systems rely on context windows as ephemeral substrates for reasoning. Its nearest external comparison fields are ai, governance, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[A5]** Adam Ableman. *Split-Authority AI Coordination*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-35D1BAECD5CB17AD`;  
source SHA-256  
`06FB6133170879FA8308684F0DA33F5813EAF3B5488291C2D7D234BEB6FDFEC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

#### Ableman Corpus references

**[1]** Ableman Adam Ableman *Governed Context & Memory (GCM).* Exact reviewed author source,  
SHA-256  
`F85726AC84A47C608FABF3704BFBC790FB0D393690430374916D45C6FC83C8DB`.

**[2]** Ableman Adam Ableman *A Constitution for the Context Window.* Exact reviewed author draft,  
SHA-256  
`C4F6CC466FA4306C595AFF66D9EBD4F396E45B91876E1D32A5027FCF465312EE`.

**[3]** Ableman Adam Ableman *Semantic Legitimacy Before Context.* Exact reviewed author source,  
SHA-256  
`1E9058F212FCB00E42E35E927DF2E7F830BC9C9499AAFF469FE65FF8AE137B68`.

**[4]** Ableman Adam Ableman *Reasoning by Way of Receipts.* Exact reviewed author source,  
SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`.

**[5]** Ableman Adam Ableman *The Three Hash Rule.* Exact reviewed published author source,  
SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.

### Editorial source notes retained from predecessor

**[6]** Ableman Adam Ableman *Admissibility Engineering.* Exact reviewed author source,  
SHA-256  
`FA80D5895A569839958193735B754BE62EE20E1B399A06CB3BA959614DEBF7A3`.

**Reference-status note.** These are internal corpus references. No external literature search, current-product comparison, implementation replay, security audit, or independent validation was performed in this pass.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847508](https://doi.org/10.5281/zenodo.23847508)
