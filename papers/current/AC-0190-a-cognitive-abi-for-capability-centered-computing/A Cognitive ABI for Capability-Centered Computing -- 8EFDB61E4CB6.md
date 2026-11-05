# A Cognitive ABI for Capability-Centered Computing

## Evidence-Carrying Composition of Fuzzy and Deterministic Semantic Compilers

### Change the engine, not the promise.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

A capability should not be identified with the implementation that happens to realize it. This paper develops a cognitive ABI: a semantic contract boundary through which cognitive operations are composed, qualified, authorized, realized, and evaluated independently of a particular human, model, program, or system backend. Hybrid Semantic Compiler (HSC) theory supplies the distinction between Fuzzy Semantic Compiler (FSC) operation without established deterministic semantic closure and Deterministic Semantic Compiler (DSC) operation within a declared closure regime. The Cognitive Kernel (CogK) situates work through observation, epistemic position, Exigence, attention, custody, and sufficiency. The Three Hash Rule supplies independent commitments to state, admissibility, and meaning, with optional locality and separate receipt binding.

The ABI provides contracts both for work CogK proposes and for operations implementing CogK itself, without assigning CogK execution authority. Typed semantic residue preserves unresolved obligations and connects them to responsibility-bearing work. An evidence-carrying Workflow IR spans cognitive operations and system effects while distinguishing formal proof, deterministic checking, empirical qualification, and attested observation.

An author-verified vertical slice combines evidence custody binding, Action IR correspondence checking, deterministic fault evaluation, a bounded CGSOS system test under a one-shot warrant, and residue separation. It performs four DSC cognitive operations and one governed system effect, with zero model calls, network calls, or production changes. Focused tests and 105 bounded qualification trials support cross-plane feasibility. Genuine FSC residue discharge, the integrated CogK work-custody cycle, independent reproduction, and public artifact release remain outstanding. This architecture-and-artifact account makes meaning, competence, authority, effects, unresolved work, and evidence independently inspectable across changing realizations.

## 1. Introduction: The Model Is Not the Capability

A request to verify an action, retrieve admissible evidence, investigate a fault, or execute a bounded system operation names an obligation. It does not inherently name the mechanism that must fulfill it.

The central architectural move is to preserve that distinction throughout execution: bind the requested meaning, compile a capability graph, select an eligible realization, constrain its effects, and evaluate what its evidence establishes. Interchangeability depends on the contract and operating scope, not matching interface names or similarly fluent outputs.

This paper connects HSC [1] to the capability-first operating-system architecture represented by MosaiCOS/UCM/CGSOS. The Three Hash Rule [2] supplies the receipt discipline. CogK [3] explains why work arises, what blocks it, what deserves attention, and when another attempt should stop. Work Custody [4,5] accounts for recognized responsibility to advance that work.

The connection is reciprocal. CogK requests operations through the ABI, while its own context-compilation, sufficiency, custody-checking, and model-review operations can be expressed as capabilities. CogK supplies situated cognitive control; the ABI supplies a realization-independent contract boundary. Figure 1 shows their relationship to execution and evidence.

### 1.1 Contributions

The paper makes five contributions:

1. **A realization-independent cognitive ABI** for composing human and machine FSC and DSC operations and connecting CogK's functions to explicit contracts.
2. **Typed semantic residue** with dependency, conservation, escalation, and return obligations, linked to independently accounted Work Custody.
3. **A qualification and substitution model** separating competence, assurance, admission, sufficiency, and authority.
4. **An evidence-carrying Workflow IR** spanning cognitive operations and system effects, with authority-preserving composition and Three Hash Rule receipts.
5. **A working vertical slice** demonstrating bounded cross-plane composition under shared semantic identity, authority, witnesses, and workflow closure.

The novelty claim concerns the combination, not the invention of structured workflows, planning, effect typing, capability security, provenance, or procedural learning.

### 1.2 Paper type and evidential standing

This is an architecture-and-artifact paper. We inspected the candidate source and sealed artifacts, reproduced the qualification campaign locally, and executed the vertical workflow. Independent third-party reproduction and live-system admission remain outstanding [7]. Appendix A distinguishes the identified local artifact from the public release and reproduction materials still required.

Architectural requirements, conditional formal arguments, and demonstrated behavior are separate claims. CogK-to-ABI capability families, residue-to-work bindings, and the integrated investigation protocol are proposed integration contracts. Existing CogK documentation [3,6] supplies their architectural basis, not an executed integration campaign. Section 10.4 states the demonstrated boundary; Section 14 consolidates the broader limitations.

**Evidence-carrying** means that a transition carries the justification its contract requires, with an explicit evidence class and assurance scope. Formal proofs, deterministic correspondence checks, finite qualification campaigns, and attestations are not interchangeable. We reserve *formal proof* and the established term *proof-carrying code* for constructions that actually supply proofs; a log cannot satisfy a proof obligation merely by being hashed.

## 2. HSC Foundations: Closure, Frontier, and Maturation

A **Fuzzy Semantic Compiler** is a human or machine semantic realization whose transformation cannot be justified as a closed deterministic mapping under the current semantic and governance regime. An FSC may be implemented by a human, language model, stochastic model, ensemble, or hybrid process. Its outputs can include interpretations, hypotheses, plans, classifications, code, or proposed bindings.

This is a substrate-neutral refinement of HSC's earlier probabilistic-engine definition, incorporating its human-frontier parity into the definition itself [1]. It does not claim that human cognition is probabilistic software, that machine determinism establishes semantic correctness, or that unavailable execution permission turns a closed program into an FSC. Semantic closure and present invocation eligibility remain separate questions.

A **Frontier Semantic Operator** is the role an FSC occupies at an unresolved semantic frontier: where a representation, model, binding, evidence boundary, or transformation rule is absent, contested, or premature. FSO does not denote a cost, model-size, or locality tier. Both local and remote FSCs, including human participants, may occupy that role.

A **Deterministic Semantic Compiler** is a bounded, reproducible, governable, receipt-bearing semantic substrate. Its operations include retrieval, binding, traversal, classification under admitted models, validation, execution, projection, recording, and refusal. Typed intermediate representations are one mechanism, not the definition [1]. Classification attaches to the operation under its declared regime, not permanently to its host technology.

Schematically, frontier transformation and closed operation are written:

$$
F:(x,c,s)\leadsto\widetilde{o},
\qquad
D_i:(s,o,\Gamma)\rightarrow(s',o',r,\sigma).
$$

The first arrow denotes a semantic transformation without asserting a closed deterministic function. The second binds governed state, an object, context, an output, a receipt, and a disposition such as `ADMIT`,  
`REFUSE`, `ABSTAIN`,  
or `ERROR`. A correct fault finding or refusal is a legitimate result; always refusing admissible work is not useful conformance.

**Governed closure** requires sufficient declared terms, relations, scope, evidence boundaries, transformation rules, invariants, resource bounds, refusal conditions, and governance commitments for the operation. Closure declarations are scoped and revisable, not oracle truth [1].

**Crystallization** moves a useful frontier maneuver into DSC substrate after binding, testing, continuity review, and admission. Recurrence supplies a candidate signal, not proof. **Decrystallization** demotes or quarantines a realization when its closure fails or its supporting qualification is invalidated [1]. Loss of present authority separately prevents execution even when the semantic mapping remains closed. The contract may remain stable while the eligible realization set changes.

CogK already describes deterministic predicates, anomaly review, proposed richer models, court testing, and admission of new DSC capabilities [3, Section 7]. Figure 2 connects that lifecycle to this ABI. The older CogK expansion *Flexible Semantic Compiler* is retained only as historical terminology; this paper uses *Fuzzy Semantic Compiler* consistently.

## 3. A Common Boundary Across Two Planes

The **system plane** concerns files, processes, devices, networks, displays, sensors, services, and their effects. The **cognitive plane** concerns operations such as orientation, retrieval, classification, hypothesis formation, planning, correspondence checking, and synthesis.

These are contract distinctions, not disjoint physical worlds. A cognitive operation consumes computational resources and may affect state. A system operation may require unresolved interpretation before its intended effects can be specified.

| Capability-first system architecture | Cognitive and agentic counterpart |
| :--- | :--- |
| Application intent | User or agent intent |
| UCM capability description | Cognitive capability descriptor |
| System capability compiler | Agentic Capability Compiler |
| System operation IR | Action IR / Workflow IR |
| Service, driver, or hardware realization | DSC or FSC realization, including a human, model, program, governed tool, or specialized backend |
| Scheduler and dispatcher | Workflow orchestrator and qualified route selector; CogK supplies situated attention and readiness |
| Permission and capability grants | Authority and effect constraints |
| Driver conformance testing | Capability qualification fixtures and campaigns |
| Execution receipts and telemetry | Witnesses, custody, and evaluation records |

The cognitive ABI is analogous to a system ABI, but does not assert a shared machine-level calling convention. It specifies the semantic obligation that adapters must preserve. For example:

```text
VERIFY_ACTION_IR_CORRESPONDENCE(
    intended_operation,
    selected_executor,
    effect_class
)
  -> Corresponds(witness)
   | SemanticDrift(counterexample)
   | Refusal(reason, missing_obligations, receipt)
```

The signature is only an entry point. Its contract must define the correspondence relation, inspected evidence, surviving distinctions, and assurance level. A checker that compares operation families does not thereby prove all behavior of arbitrary executor code.

### 3.1 Orthogonal routing dimensions

Route selection uses a multidimensional descriptor rather than a numbered model ladder:

```text
semantic_class:        DSC | FSC
frontier_role:         FSO | not_applicable
realization_kind:      human | model | symbolic_engine | program
                       | device | ensemble | hybrid
locality:              local | remote | embedded
qualification_scope:   contract, domain, environment, evidence, validity
assurance_class:       declared evidence requirements
admission_status:      candidate | admitted | quarantined | retired
constraints: privacy, cost, latency, resources, authority, effects
```

These dimensions are explicit but not freely interchangeable: descriptor validation must reject incoherent combinations. An FSC may be local and frontier-operating simultaneously. A human performing frontier interpretation is an FSC under Section 2, with no compiler-class exemption. A deterministic host running a model does not establish closure for the model's semantic transformation.

The implementation labels `R1-local` and

`R2-FSC` are retained only as historical identifiers. The earlier proposed replacements   
`R1_LOCAL_FSC_CANDIDATE` and   
`R2_FRONTIER_FSC_CANDIDATE` are also deprecated as architectural routing categories: they still mix locality with frontier role. Migrations may record these strings as provenance, but selection operates on the descriptor and current eligibility, not an assumed ordering of those names.

**Figure 1 asset pending.** The source references   
  `figures/architecture.svg`, but that file was not found in either supplied paper-draft root. The caption and architectural claim are retained for author review; a renderable source asset or approved redraw is required before final PDF qualification.

**Figure 1.** Intent is bound and compiled; qualification, admission, authority, and resource constraints filter realizations before invocation. FSC candidates cross a return boundary rather than becoming authority. Every requested system effect is separately revalidated. Observations and witnesses support result admission, closure, or an explicit unresolved disposition. The residue branch repeats eligibility checks; tool and network operations inside a realization also cross the effect boundary. CogK proposes and reconsiders work through these same boundaries. Dashed paths denote contextual linkage, feedback, or gated resumption, not permission. The figure specifies the architecture; the bounded implemented subset is identified in Section 10.

## 4. CogK: Cognitive Control Across the ABI

CogK supplies the situated cognitive-control architecture within which capability requests arise and outcomes are reconsidered. It separates observation, salience, epistemic position, Exigence, standing, attention, custody, sufficiency, policy, authorization, execution, receipt, and outcome. These are distinct projections over governed reality, not an obligatory linear pipeline [3]. The ABI supplies contracts for bounded transition candidates and for the cognitive operations that produce them. Neither architecture subsumes the other.

### 4.1 Exigence, attention, and sufficiency

**Exigence** is the graph-derived condition by which a present state calls for an admissible transition. Priority orders work; urgency concerns time sensitivity; salience concerns notice; Exigence concerns what the modeled situation calls to be resolved. An asserted need requires recognized standing before it can govern a response [3].

A release may depend on verification, verification on an unavailable artifact, and artifact access on an authority decision. Repeating verification does not resolve that dependency. CogK directs inquiry toward the missing prerequisite without granting the missing authority.

Attention allocates processing, presentation, and interruption capacity. A condition can remain represented without appearing in the current notification or context packet. Custody identifies the recognized participant responsible for advancing work. Sufficiency asks whether that participant has the information, evidence, authority, capability, artifacts, resources, and opportunity needed for the transition [3,4].

Sufficiency is not qualification: an otherwise qualified executor may lack the input artifact, while a work custodian may lack any eligible executor. Nor is a finding that an authority prerequisite appears present the execution boundary's current authorization decision.

### 4.2 The bounded runtime is not its own authority

CogK's architectural roles include Steward, Governor, Executor, Auditor or Court, and Foundry. Their separation does not vest their combined powers in one component [3]. The CGSOS navigator records the bounded CogK runtime as terminating at   
`READY_FOR_GOVERNANCE_REQUEST`, with governance and effect-boundary revalidation assigned separately [6]. Readiness is therefore a transition candidate, not permission.

Cognitive state changes are effects too. Creating work, changing custody, committing an epistemic position, or activating an attention policy requires the applicable grant. Preparatory cognition may operate within authorized scope; it cannot enlarge that scope by declaring its output necessary.

### 4.3 CogK as ABI caller and capability provider

As a caller, CogK proposes retrieval, investigation, correspondence checking, or a bounded system test. As a provider, it exposes its own semantic operations through the same ABI. Proposed capability families include:

| Candidate capability | Required distinction |
| :--- | :--- |
| `DERIVE_EXIGENCE` | Supported transition pressure versus salience or asserted urgency. |
|   
`ASSESS_TRANSITION_SUFFICIENCY` | Satisfied versus missing prerequisites for a specified participant and transition. |
|   
`COMPILE_TRANSITION_CONTEXT` | Required versus optional material, with inclusion, compression, and omission rationale. |
|   
`CHECK_WORK_CUSTODY_TRANSITION` | Recognition, acceptance, predecessor/successor continuity, and authorized mutation. |
|   
`ASSESS_EXECUTION_NONPROGRESS` | Evidence of unproductive recurrence versus justified retry or changed conditions. |

Each family requires the full contract in Section 5. A closed model can support a DSC realization; an unresolved interpretation can require an FSC contribution. Generating candidate structure and checking it remain different operations.

This self-application does not require unbounded self-validation. Implementations must declare trusted primitives, admitted verifiers, and bootstrap assumptions. A qualification assessor cannot establish its own admission solely by assessing itself; model repair crosses external review and authority boundaries [1,3].

### 4.4 Context compilation as governed attention

CogK compiles context for the next admissible transition rather than solely by similarity or recency. Its policy distinguishes controlling rules, active work, Exigence, custody, blocking artifacts, authority, receipts, rival hypotheses, resolved history, and background. A context receipt records inclusion, compression, exclusion, and rationale [3, Section 9].

An ABI context contract specifies which constraints, custody facts, refusal conditions, observations, and terminal receipts must survive. When required content exceeds the budget, permitted responses include narrowing the operation, staged retrieval, an authorized budget change, or refusal. Silently removing a controlling rule is not valid compression; omission from a packet does not erase an obligation from state.

Human-facing explanation and machine-facing packets need not be identical. Each projection carries its own fidelity and continuity obligations.

### 4.5 Nonprogress, reconsideration, and model repair

The ABI checks an individual realization's contract. CogK also asks whether another invocation is warranted. Its fixation example combines repeated strategy identity, no newly admitted evidence, accumulating failures, and unchanged Exigence ranking. A bounded gate may require new evidence, model revision, diversification, custody transfer, or review instead of another identical attempt [3, Section 5]. This is a finding about execution structure, not a diagnosis of a person.

Attempt receipts and outcomes remain distinct. Uncertain completion calls for reconciliation; failure may call for a new hypothesis; resolution changes which dependency deserves attention. CogK's anti-Goodhart constraints reject treating fewer visible obligations as sufficient evidence of success: suppression, unsupported transfer, and premature closure can improve that number while degrading the work [3, Section 16]. Human refusal and legitimate deferral remain admissible states.

## 5. Capability Contracts, Qualification, and Substitution

### 5.1 Capability is not permission

A **capability descriptor** specifies an operation. A **capability grant** authorizes a principal to perform a bounded invocation of an operation. Competence and permission answer different questions.

Let a capability contract be:

$$
\begin{aligned}
K= \langle &k, v, \tau_{in}, \tau_{out}, \mathrm{Pre}, \mathrm{Post}, \\
&I, \mathcal{E}, A, W, F, L\rangle
\end{aligned}.
$$

Here $k$ and $v$ identify the capability and contract version; the types define its interface; $\mathrm{Pre}$ and $\mathrm{Post}$ define admissible inputs and outcomes; $I$ records continuity invariants; $\mathcal{E}$ bounds effects; $A$ specifies authority requirements; $W$ specifies witnesses and their assurance classes; $F$ defines refusal and abstention behavior; and $L$ records lifecycle dependencies and invalidation conditions.

The contract may require exact deterministic output, a result satisfying a logical relation, an evidence-linked candidate, or an admissible terminal refusal. The outcome's substantive content and its governance disposition remain separate.

### 5.2 Qualification is scoped evidence

Write:

$$
\operatorname{Qual}(r,K;\Omega,\Gamma,t,E_q)
$$

for realization $r$ qualified under environment $\Omega$, governance context $\Gamma$, evaluation time $t$, and qualification evidence $E_q$.

Qualification must expose its basis. Finite fixtures establish behavior on the tested cases; a formal proof establishes the property and domain of its theorem; an attestation establishes only what its accepted attestation contract supports. A qualified investigator may produce candidate explanations without being qualified to issue final admission decisions.

A route is eligible only when input validity, current qualification and admission, authority, permitted effects, resource bounds, and witness availability all hold:

$$
\begin{aligned}
\operatorname{Eligible}(r,K,x)={}&
\operatorname{InputValid}(x,K)\land\operatorname{QualificationCurrent}(r,K)\\
&\land\operatorname{AdmissionCurrent}(r,K)\land\operatorname{AuthoritySatisfied}(r,K,x)\\
&\land\operatorname{EffectsPermitted}(r,K,x)\\
&\land\operatorname{ResourcesBounded}(r,K,x)\\
&\land\operatorname{WitnessAvailable}(r,K,x).
\end{aligned}
$$

Context arguments are suppressed for readability, not treated as ambient inputs. `AdmissionCurrent` checks the status required by this invocation: a candidate may be admitted to a sandbox qualification trial without being admitted to production. Optimization occurs only over the eligible set. Lower cost, greater model capacity, or lower latency cannot compensate for missing permission.

A CogK attention decision can select which candidate to consider, and a sufficiency finding can identify prerequisites relevant to eligibility. Neither bypasses the eligibility checks. Where a workflow contract requires recognized work custody, the invocation must additionally carry the corresponding custody evidence. Custody is not imposed as a universal prerequisite for every low-level capability simply because the interface can represent it.

### 5.3 Qualified substitution

A substitute must preserve required outcomes and invariants, remain within the effect envelope, satisfy witness obligations, and avoid adding undeclared preconditions. A candidate generator cannot replace a verifier merely because both return structured text.

Let $\operatorname{Allowed}_K(x)$ denote the contract's allowed observable outcomes, including declared refusal conditions. A semantic refinement obligation is:

$$
\operatorname{Behaviors}(r,x)\subseteq\operatorname{Allowed}_K(x)
\quad\text{for inputs in the declared scope}.
$$

This describes what full conformance would require; finite qualification trials are evidence toward that obligation, not a proof of the inclusion for all inputs. Qualification also does not supply the invocation's current authority.

The capability lattice organizes refinement and qualification relationships. A formal implementation should claim lattice structure only where its order, meets, and joins are defined. Joining descriptions does not automatically join authority grants.

**Figure 2 asset pending.** The source references   
  `figures/maturation.svg`, but that file was not found in either supplied paper-draft root. The caption and lifecycle claim are retained for author review; a renderable source asset or approved redraw is required before final PDF qualification.

**Figure 2.** FSC precedent motivates candidate decomposition, not automatic promotion. DSC qualification, bounded admission, activation, and monitoring are separate transitions. Invalidation removes eligibility in the affected scope; decrystallization returns the artifact to quarantine, review, or frontier work. Any repaired candidate must cross qualification and admission again. Unaffected qualified scopes may remain available.

## 6. Compilation and Typed Semantic Residue

For request $x$, semantic state $s$, and governance context $\Gamma$, the Agentic Capability Compiler produces:

$$
\begin{aligned}
&\operatorname{ACC}(x,s,\Gamma) \\
&\rightarrow (B,G,\mathcal{R},\Pi) \; \\
&\mid \;\operatorname{Refusal}\; \\
&\mid \;\operatorname{Error}
\end{aligned},
$$

where $B$ is explicit semantic binding, $G$ the capability graph, $\mathcal{R}$ identified residue, and $\Pi$ compilation and continuity obligations. Requests may originate directly with users or through CogK; CogK is not a mandatory front end. Where required, the binding references the work object, epistemic position, sufficiency findings, and attention decision without admitting their contents by implication.

Distinguishing $x$ from $B$ avoids assuming lossless translation of unrestricted language. Material ambiguity remains visible; when decomposition cannot be justified, the unresolved binding itself becomes residue. HSC's GCNL and GCML support this descent by stabilizing semantic expression and procedural realization respectively [1].

### 6.1 Residue contracts

A residue object is specified schematically as:

$$
\begin{aligned}
\rho= \langle &id, B_\rho, g, E_\rho, O_\rho, A_\rho, \mathcal{E}_\rho, \\
&b_\rho, W_\rho\rangle
\end{aligned}.
$$

The fields bind the affected request, gap, admissible context, discharge obligation, authority and effect limits, budget, and return witnesses. Gaps may include unresolved references, conflicting observations, absent causal models, or unsupported classifications. A missing prerequisite does not automatically warrant another model call.

A closed operation depending on unresolved residue must wait, take an authorized alternative, or terminate with an explicit disposition. Determinism cannot be purchased by assuming the missing answer.

### 6.2 Residue conservation and return

Every identified obligation remains unresolved, is discharged with admissible support, or receives an authorized disposition such as deferral, refusal, or supersession. Splits and merges require explicit lineage: conservation concerns obligation identity and content, not record counts.

Returned FSC material is a candidate at the consuming boundary. Its binding, evidence scope, required witnesses, and claimed discharge are checked before it can satisfy a dependent precondition. Plausibility cannot replace a stronger discharge requirement. Residue conservation prevents silent loss of identified obligations; it does not establish discovery of every ambiguity.

### 6.3 Control closure is not task resolution

Let $\operatorname{ControlClosed}(G)$ mean that every required transition has an admissible terminal disposition, and $\operatorname{TaskResolved}(B)$ mean that the requested substantive obligations are satisfied. Then:

$$
\operatorname{ControlClosed}(G)\not\Rightarrow\operatorname{TaskResolved}(B).
$$

A workflow can correctly terminate with a requirement for further investigation. Conversely, a task specifically requesting an evidence packet with open questions may be satisfied without answering them. Closure is relative to the declared obligation.

### 6.4 From semantic residue to responsibility-bearing work

A residue describes an unresolved obligation. CogK determines its situated significance, prerequisites, and attention treatment; Work Custody accounts for accepted responsibility [3-5]. Policy may bind residue to one or more work objects while preserving its identity, discharge requirements, and evidence boundary. Parent and child investigations can have different custodians. Linking them does not transfer either object.

```text
residue recorded       != attention immediately required
Exigence recognized    != interruption authorized
work offered           != custody accepted
custody acquired       != prerequisites sufficient
sufficiency assessed   != current effect authorized
candidate returned     != residue discharged
child work completed   != parent task resolved
```

Work Custody relates participants, work, and time:

$$
Custody\subseteq\mathcal{P}\times\mathcal{W}\times\mathcal{T}.
$$

Its lifecycle distinguishes unassigned, proposed, offered, accepted, active-custody, transfer-pending, and completed states, with explicit decline, revocation, abandonment, expiration, and escalation [5]. The default exclusivity rule governs established active custody, except declared joint custody; it cannot erase the same model's unassigned states or missing-custodian queries [4,5].

Transfer completes only after successor acquisition. Pending acceptance remains visible; revocation or expiration records the loss without inventing a successor. Queueing a job, sending an RPC, or receiving model text does not alone establish recognized transfer.

### 6.5 Two independent conservation obligations

Let $h$ be witnessed history, $\mathcal{R}_{identified}$ identified obligations, and $\mathcal{W}_{tracked}$ linked work. The integration requires:

$$
\begin{aligned}
&\forall\rho\in\mathcal{R}_{identified},\quad
  \operatorname{ObligationAccounted}(\rho,h),\\
&\forall w\in\mathcal{W}_{tracked},\quad
  \operatorname{CustodyAccounted}(w,h).
\end{aligned}
$$

The first preserves unresolved state, supported discharge, or authorized disposition, including split/merge lineage. The second makes custody, pending transfer, absence, or termination derivable from recognized lifecycle events. It instantiates Work Custody's existing conservation and transfer-continuity invariants [5].

The question can survive while its responsibility becomes orphaned; a custodian can remain while the question is silently weakened. Both failures must be detectable. Neither accounting predicate guarantees progress or supplies missing evidence, authority, a willing participant, or a correct answer.

**Work custody is not evidence custody.** The former concerns responsibility to advance work; the latter concerns identity, provenance, and handling of evidentiary artifacts [4]. Their respective observations and witnesses must not be conflated.

## 7. The Three Hash Rule: Independent Questions, Bound Receipts

The ABI applies the existing Three Hash Rule [2], whose minimal decision core is $\{H_s,H_c,H_m\}$. These commitments answer independent governance questions, not successive workflow stages. The constitution specifies which facts each contains.

- **Commitment:** $H_s$: state  
  **Decision:** $D_s$  
  **Cognitive-ABI application:** Open the exact request, plan, observation, work record, or result under its declared state canonicalization.

- **Commitment:** $H_c$: admissibility  
  **Decision:** $D_c$  
  **Cognitive-ABI application:** Check the applicable authority path, policy constraints, freshness, and required qualification or role conditions.

- **Commitment:** $H_m$: meaning  
  **Decision:** $D_m$  
  **Cognitive-ABI application:** Verify regime-bound parsing, normalization, resource bounds, and semantic lineage of the committed object.

- **Commitment:** $H_j$: locality, when required  
  **Decision:** $D_j$  
  **Cognitive-ABI application:** Establish membership in a phase-bound namespace.

- **Commitment:** $H_r$: receipt binding  
  **Decision:** Binding gate  
  **Cognitive-ABI application:** Bind commitments and preserve the context needed to interpret the receipt.

### 7.1 Receipt, decisions, and context

The receipt and witness family are:

$$
R=(H_s,H_c,H_m,H_j?,H_r,\pi),
\qquad \pi=(\pi_s,\pi_c,\pi_m,\pi_j?).
$$

Verification uses the declared context $\mathcal{C}=(P,\Sigma,\Phi,t)$: policy, semantic regime, phase, and explicit evaluation time. For $i\in\{s,c,m\}$, $D_i(R,\mathcal{C},\pi_i,t)\in\{0,1\}$; $D_j$ additionally permits $\mathsf{NA}$ when locality is not required.

Writing $B_{bind}$ for the receipt well-formedness and recoverability gate:

$$
\begin{aligned}
&\operatorname{CoreComplete}(R,\mathcal{C}) \\
&\iff (D_s=1) \\
&\land (D_c=1) \\
&\land (D_m=1) \\
&\land (B_{bind}=1)
\end{aligned}.
$$

A required locality query additionally needs $D_j=1$. The binding gate is not another governance decision procedure. A receipt whose separate decisions pass can still be rejected for an under-recorded context collapse. Appendix B gives the canonical constructions, Constitutional Legend mapping, and admissible binding configurations [2].

### 7.2 Cognitive meaning without fictitious closure

$H_m$ applies to declared regimes admitting deterministic parsing and bounded normalization, not unrestricted natural language. A formal envelope can commit to an unresolved obligation and a hashed uninterpreted region without asserting that the region has been understood. Envelope verification does not discharge the residue [2].

Likewise, an epistemic-position receipt may establish the canonical representation of a hypothesis, rivals, and uncertainty without establishing the hypothesis's truth. Exigence and custody facts enter commitments as their constitution requires; they do not justify extra hash axes. Evaluator identity is provenance unless policy makes authorized evaluator status an admissibility condition.

### 7.3 What the commitments establish

The hashes make committed artifacts and bindings tamper-evident under the framework's cryptographic and canonicalization assumptions. Decision procedures answer their scoped questions; contract-specific correspondence witnesses justify transitions among bound requests, plans, observations, and results. Thus receipt completeness is not unconditional task correctness.

Verification assumes appropriate hash resistance, domain separation, versioned byte-stable canonicalization, pure versioned contexts, explicit time, and no undeclared external I/O [2]. Independent questions do not imply unrelated evidence. A valid state can be unauthorized; an authorized artifact can fail semantic normalization; a coherent hypothesis can remain unsupported.

## 8. Evidence-Carrying Workflow Composition

Let a bounded workflow be:

$$
G=(V,E_d,E_a),
$$

with invocation nodes $V$, data and control dependencies $E_d$, and authority dependencies $E_a$. Each node binds its contract, realization, inputs, authority references, effect limits, and evidence obligations.

A CogK-integrated workflow additionally references the relevant work and waiting graph and its custody history. These are related structures, not necessarily the same graph: a work object may span several invocations, and one invocation may contribute evidence to several obligations. Their correspondence must be declared instead of inferred from matching labels.

A cognitive operation can prepare a proposed system test without authorizing it. A warrant can authorize the bounded test without establishing its scientific interpretation. An observation can establish what a sensor or test reported without settling the investigation. The workflow preserves these distinctions across its edges.

### 8.1 Authority and effect intersection

A necessary effect condition is:

$$
\mathcal{E}^{req}_n\subseteq
\mathcal{E}_{principal}\cap\mathcal{E}_{workflow}
\cap\mathcal{E}_{contract}\cap\mathcal{E}_{realization}
\cap\mathcal{E}_{warrant}.
$$

These sets abbreviate predicates over targets, arguments, resources, identities, and state transitions. Consumable authority requires additional stateful enforcement. A one-shot warrant must be tied to the intended invocation and consumed without allowing concurrent or replayed invocations to duplicate the effect.

Authorization is checked at the execution boundary against current conditions. An earlier plan does not immunize a later operation against revocation, expiry, or changed state. Uncertain completion requires recovery logic; it does not justify blind retry.

Receipt verification itself remains pure over its declared snapshot and evaluation time. Live authorization, warrant consumption, execution, and observation are separate governed operations. An implementation must not smuggle ambient clock reads or external I/O into a supposedly replayable verification procedure.

### 8.2 Conditional composition argument

For a bounded execution, suppose each admitted node satisfies its input contract, realizes its declared outcome and invariants, remains within current authority and effects, preserves residue dispositions, and supplies admissible evidence. Suppose adjacent contracts are compatible and shared-state interference and resource consumption are accounted for. For the proposed CogK integration, additionally suppose that every required work binding satisfies custody recognition and continuity and that both conservation predicates in Section 6.5 hold.

Induction over a valid execution order then establishes that each downstream admitted state derives through contract-respecting, authorized, witnessed transitions. A node cannot legitimately inherit a stronger result than its predecessors established. If a required premise fails, dependent admission must stop or follow an explicitly authorized alternative.

This conditional argument assumes the local obligations it composes. It establishes preservation along the bounded execution, not liveness, discovery of every relevant obligation, or implementation correctness.

## 9. Semantic Continuity, Identity, and Constitutional Roles

### 9.1 Continuity is relational

One semantic identity across a workflow does not require identical digests. Requests, normalized plans, warrants, observations, and closure records differ in content and purpose. The relevant condition is:

$$
\operatorname{Preserves}(z_i,z_{i+1};I_i,\Gamma_i),
$$

for declared transformations, with recoverable references to the bound obligation. HSC's Semantic Manifold Topology requires specified invariants and authorized transformation, not similarity alone [1]. Each artifact may have its own Three Hash Rule receipt, linked by correspondence witnesses. Changes in the semantic object or lineage need not preserve equal $H_m$ values.

### 9.2 Semantic commitments are not storage addresses

A semantic self-hash commits a schema-defined payload; an object-store address identifies a stored representation that may include wrappers or excluded self-hash fields. The roles require distinct types:

```text
SemanticCommitment<Schema, Canonicalization>
ReceiptRoot<BindingConfiguration>
ObjectAddress<Store, StoredRepresentation>
```

The same hexadecimal syntax does not make these identifiers interchangeable. Their relationship requires schema-specific openings and checks.

### 9.3 Evidence is not authority

Receipt, authority, and evidence are constitutional roles, not mutually exclusive artifact types [2]. One artifact may satisfy several role contracts, but passing one does not imply passing another. Historical issuance can remain valid evidence after present authority expires or is revoked. A retrieved document or FSC answer cannot acquire permissions merely by asserting them.

Receipts make compliance inspectable; enforcement belongs to the execution boundary. Receipt verification, deterministic recomputation, and repeating an external effect are distinct operations. Re-execution can require fresh authority and may be unsafe or impossible.

CogK's receipt-before-effect discipline has the same distinction [3]. A pre-effect authorization or refusal record establishes the decision, not occurrence of a future operation. Post-attempt observations establish what actually happened. A historical custody-acceptance receipt likewise need not imply current custody.

## 10. Implemented Cross-Plane Vertical Slice

### 10.1 Construction and execution

The initial implementation registered three deterministic cognitive cells and qualified their positive and negative boundaries without changing production routing. We then composed the cross-plane workflow below and executed it locally [7].

- **Step:** 1  
  **Operation:** Evidence custody binding  
  **Boundary exercised:** Observation identity and custody

- **Step:** 2  
  **Operation:** Action IR correspondence checking  
  **Boundary exercised:** Intended operation, selected executor, and effect class

- **Step:** 3  
  **Operation:** Deterministic fault evaluation  
  **Boundary exercised:** Bounded evaluation under declared rules

- **Step:** 4  
  **Operation:** Bounded CGSOS system test  
  **Boundary exercised:** Authorized system effect under a one-shot warrant

- **Step:** 5  
  **Operation:** Typed semantic-residue separation  
  **Boundary exercised:** Unresolved obligation preserved for subsequent FSC handling

The workflow completed under one semantic identity envelope, authority envelope, witness chain, and workflow closure. The four cognitive operations count invocations, not necessarily four distinct registered executor implementations [7].

### 10.2 Validation results

| Measure | Author-verified result |
| :--- | ---: |
| Compatibility tests | 35 passed |
| Final focused tests | 44 passed |
| Deterministic qualification trials | 105 passed |
| Actual cross-plane workflow | Passed |
| Final artifact and object-store audit | Passed |
| DSC cognitive operations | 4 |
| Governed system effects in workflow accounting | 1 |
| Model calls during the workflow | 0 |
| Network calls during the workflow | 0 |
| Production changes | 0 |
| Files hashed during runtime identity enrollment | 54,736 |
| Run duration | 204.548 seconds |

These are separate validation categories [7]. They are not added into one independent statistical sample. The single governed system effect is the workflow's operation count, not a census of host syscalls, artifact writes, or all resource activity. Zero model calls describes the executed workflow, not its development history.

### 10.3 Defects exposed by composition

The exercise exposed and repaired two ABI defects [7].

**Over-specific Action IR families.** Cognitive capabilities used family names too closely tied to particular realizations. The repair separated the stable operation family from incidental realization detail. The inverse error remains important: a family must not become so broad that materially different semantics or effects are treated as equivalent.

**Identity-namespace conflation.** The workflow-evidence verifier treated semantic self-hashes and object-store addresses as interchangeable. Correct verification requires the identifier appropriate to each schema and boundary. This exposed the identity-role distinction formalized in Section 9.2.

### 10.4 Supported interpretation

The artifact demonstrates bounded composition of deterministic cognitive operations with an authorized system effect. It crosses into and returns from that effect boundary rather than merely qualifying isolated cells.

The residue was synthetic, and no FSC was invoked. The result establishes residue separation and disposition, not genuine frontier investigation, residue discharge, model comparison, general cognitive closure, or performance superiority. Nor does it establish a CogK cycle combining Exigence, attention, accepted work custody, context compilation, investigation, and reconsideration. Evidence-custody binding is not a test of Work Custody.

The candidate remains local, with independent reproduction and live admission outstanding. It is not a conformance demonstration for every Three Hash Rule configuration or proposed integration contract. Appendix A records the additional public release requirements.

## 11. Performance and the Cost of Governed Closure

The zero-model workflow took 204.548 seconds. Full runtime identity enrollment hashed 54,736 files and was identified as the principal performance limitation [7]. Deterministic offload therefore does not automatically make the complete governed workflow inexpensive.

For a serial accounting model:

$$
T_{run}=T_{identity}+T_{compile}+T_{execute}
+T_{witness}+T_{evaluate}.
$$

A stage-resolved profile is needed before attributing exact shares of elapsed time. HSC's total cost of closure also includes construction, maintenance, rot testing, migration, and review [1].

An invalidation-aware identity cache should reuse justified identity evidence, not merely skip hashing. Its key and invalidation rules must cover the dependency closure material to the qualification claim: relevant code, loaded dependencies, interpreters, schemas, configuration, verifiers, and canonicalization versions. File counts and modification times alone are not sufficient evidence of unchanged content.

A smaller identity domain is legitimate only when its dependency boundary can be justified. Changes outside an asserted boundary that can still influence execution are evidence that the boundary was incomplete.

Identity reuse and authority reuse have different conditions. A cached environment root must not revive a consumed warrant, stale qualification, or revoked permission. An old receipt can still verify as history without authorizing a new invocation.

The performance campaign should compare cold and warm execution, then deliberately change dependencies, verifiers, and relevant configuration. Cache corruption and missed invalidation should be negative tests. A faster run is not an optimization success if it weakens the identity claim.

CogK adds a different performance question: whether transition-specific attention and context compilation avoid unproductive invocations without losing controlling evidence or obligations. Its own derivation, context, and custody-accounting costs must be measured. A reduction in model calls is not a net improvement when it merely shifts cost to excessive reevaluation, omits necessary work, or increases human coordination burden.

## 12. Related Work

### 12.1 Workflow semantics and planning

**BPMN** provides process notation, interchange models, and execution semantics covering orchestration, events, activities, gateways, termination, and exception behavior. Its execution-conformance chapter distinguishes operational elements from elements requiring additional implementation semantics [21]. Workflow IR therefore does not originate structured process execution. Its proposed contribution is to make semantic residue, qualification, authority dependencies, evidence obligations, and heterogeneous realizations first-class concerns within a compositional contract system.

**PDDL2.1** supplies syntax and formal semantics for planning with temporal and numeric resources, including validation of concurrent plans [22]. This is an important antecedent for explicit preconditions, effects, and bounded resource reasoning. The ABI adds a separate question: which currently qualified and authorized realization may perform the modeled action, and what observed evidence justifies accepting its result? Plan validity within a model and admissibility of an actual execution are distinct obligations.

### 12.2 Compiler-style agent systems

**COVENANT** compiles natural-language instructions through a workflow abstract syntax tree into a control-flow graph. Its runtime controller owns traversal, checks node-bound requirements, and distinguishes unsupported paths from incorrect realization. Unresolved associations are retained during construction [8]. This is close prior work, not merely a prompt-chain baseline. The cognitive ABI's additional emphasis is persistent residue with return obligations, qualified realization substitution, bidirectional maturation, and independent state/admissibility/meaning receipts spanning cognitive and system operations.

**Agint** compiles instructions through progressively formal representations into executable code graphs. Its design includes partially resolved and hybrid nodes, deterministic code, runtime model synthesis, effect-aware execution, refinement, deferred compilation, and fully resolved code without AI dependencies [9]. It is a direct neighbor of the moving-frontier architecture. The distinction proposed here is governance of the boundary: what qualifies substitution, which effects remain permitted, how unresolved obligations survive, and when a realization loses eligibility. Compilation progress is not equated with permanent admission.

### 12.3 Pipeline compilation and modular reasoning

**DSPy** represents language-model pipelines through declarative modules and compiles them to optimize a selected metric [10]. It separates task structure from fixed prompt strings. The cognitive ABI instead treats competence, admission, authority, and required witnesses as eligibility conditions before optimization.

**MRKL** combines neural language models with discrete knowledge and reasoning modules [11]. It supplies a clear precedent for heterogeneous execution. HSC's distinction is governed closure rather than neural versus symbolic implementation, together with a lifecycle for advancing and retreating that boundary.

**ReAct** interleaves model-generated reasoning traces with actions against external sources and environments [20]. The ABI governs the public commitments crossing those boundaries. A witness records consequential premises, evidence, permissions, and transformations; it need not reveal every private reasoning token [1].

### 12.4 Capability systems and effect typing

**Joe-E** provides a capability-based Java subset supporting least authority [14]. At the operating-system level, **seL4** represents access through unforgeable capabilities with object-specific rights, held in capability spaces and invoked through kernel APIs [23]. These precedents make permission an explicit resource, not an inference from intent. The cognitive ABI keeps that permission meaning distinct from its operation descriptors and adds qualification and semantic-correspondence obligations. The proposed architecture does not inherit seL4's enforcement or assurance merely by using capability vocabulary.

**Koka** makes potential computational effects explicit through row-polymorphic effect types and establishes corresponding properties for its typed language [24]. Effect typing helps characterize what a computation may do; current authority determines whether a particular invocation may do it. The ABI composes these concerns with resource limits and observed effect evidence. A declared or inferred effect set is neither a present grant nor a record that the effect actually occurred.

### 12.5 Authorized artifact continuity and provenance

**in-toto** specifies intended software-supply-chain steps and actors and verifies artifact flow, including protection against substitution between steps [12]. This is a strong precedent for authorized end-to-end continuity. The cognitive ABI adds semantic correspondence: consuming exactly the preceding step's bytes does not by itself establish preservation of the bound obligation.

**W3C PROV-O** supplies entities, activities, agents, derivation, attribution, delegation, and qualified relations [13]. These can represent workflow history. The Three Hash Rule adds commitment and decision surfaces; a declared provenance relation still requires evidence satisfying the consuming policy.

### 12.6 Procedural learning and specification synthesis

**Soar task learning**, illustrated by Rosie, constructs declarative task networks from situated instruction and compiles them into procedural rules through chunking [15]. HSC connects such maturation to scoped qualification, continuity, admission, and decrystallization when closure fails.

**AutoSpec+** combines LLM-driven program-specification synthesis with deterministic verification and iterative repair. Its candidate contracts and proof-relevant annotations are subjected to verifier feedback rather than accepted as intended behavior solely because they were generated [16]. The cognitive ABI generalizes the realization boundary to semantic capabilities and governed effects while retaining that distinction between candidate specification and justified acceptance.

### 12.7 Verified compilation, proofs, and interfaces

**CompCert** establishes semantic preservation across formally specified compiler stages [17]. Introducing an IR alone does not confer those guarantees. **Proof-carrying code** supplies code with a formal safety proof checked against the receiver's policy [18]. We retain its separation of producer and checker but use *evidence-carrying* for the broader assurance vocabulary here. Formal proofs remain one evidence class; tests, attestations, and custody roots are not renamed proofs.

**WIT** specifies component interfaces separately from implementation behavior [19]. The cognitive ABI likewise requires explicit interchange structure, adding semantic correspondence, qualification, authority, and witness obligations.

CogK and Work Custody [3-5] are architectural antecedents supplying situated attention, sufficiency, responsibility transfer, and reconsideration. The defensible contribution is their connection to FSC-DSC compiler duality, typed residue, governed maturation, and evidence-carrying cross-plane composition. These distinctions define obligations for evaluation rather than establish comparative superiority.

## 13. Evaluation Agenda

The next experiment is a genuine mixed FSC-DSC investigation with the proposed CogK linkage. Its unresolved question must not have a substantive answer already embedded in a synthetic-residue fixture.

### 13.1 A CogK-aware investigation protocol

A controlled system test produces an unexplained result. DSC cells bind the observation and evaluate declared expectations, preserving the discrepancy as residue. CogK forms an epistemic position containing support, rivals, assumptions, and missing information. Its Exigence model identifies the relevant dependency; a separate attention decision allocates resources; a custody offer requires acceptance.

Sufficiency assessment exposes missing logs, inaccessible artifacts, or absent permission before another invocation. At least one bounded system effect executes within the witnessed investigation under current authorization. An entirely archival exercise is a separate condition. The context compiler retains controlling rules, observations, custody and refusal information, rival hypotheses, and the discharge contract.

Compare explicitly described FSC realizations, including local and remote models where appropriate, while holding their frontier role constant when testing locality or implementation. Both may be FSOs; neither locality is a semantic-class distinction. Human FSC participation can be another condition. Record model or procedure identity, revisions, configuration, evidence access, budgets, retries, privacy constraints, locality, and human interventions.

Separate a common-evidence comparison from one allowing additional tools or sources. Closed subproblems use DSC realizations. Every returned candidate crosses the same admission boundary, which checks support, binding, invariants, and discharge. Disagreement remains visible; model size and remoteness do not decide acceptance. Child-work completion, custody transfer, and parent-obligation discharge are separately witnessed.

Finally, CogK reevaluates the admitted result and observed outcome. It may resolve a dependency, retain a gap, redirect attention, or require a different strategy after nonprogress. A denied retry must preserve the question and its responsibility state. The record distinguishes a closed attempt from a resolved investigation.

### 13.2 Baselines and measurements

Use matched conditions for direct model/tool execution, ABI execution without CogK control, and CogK-integrated ABI execution. The middle condition isolates contract and effect boundaries from attention, sufficiency, and custody. Tasks, initial evidence, and resource permissions are matched; human review and coordination costs are included.

Where an external effect shield is shared, measure unauthorized proposals, attempts, and observed effects separately. Negative cases and safeguard ablations run in a controlled environment, not against live resources.

| Measure | Operational question |
| :--- | :--- |
| Task success | Were the declared substantive obligations satisfied? |
| Semantic drift | Which required meanings or invariants changed without justification? |
| Unauthorized effects | Which prohibited effects were proposed, attempted, or observed? |
| Residue preservation | Did obligations remain traceable through splitting, merging, discharge, or disposition? |
| Custody continuity | Were acceptance, handoffs, gaps, and termination correctly represented? |
| Sufficiency and nonprogress | Were missing prerequisites identified and unsupported retries redirected? |
| Context preservation | Did required constraints, fresh evidence, custody, and refusal information survive? |
| Reproducibility | Can deterministic operations and verification decisions be replayed in the declared context? |
| Model use and cost | What calls, tokens, compute, fees, and human effort were consumed? |
| Latency | What are cold/warm and stage-resolved times? |
| Witness completeness | Are required bindings, observations, and transition witnesses checkable? |
| Recovery | Can interrupted work be reconciled, resumed, compensated, or rolled back where permitted? |

Report refusal correctness alongside success on admissible inputs: an always-refuse system must not appear superior because it caused no effects. Semantic-drift judgments identify their contract and evidence, not only an opaque model score. Custody and attention metrics require denominators and time windows, including false closure, unrecognized handoff, unnecessary retry, and stale-Exigence cases. Fewer visible tasks or shorter custody duration alone can reward hidden work.

### 13.3 Negative cases and ablations

Perturb state, admissibility, meaning, context binding, and locality independently: altered objects, revoked delegations, normalization failures, spliced witnesses, and incorrect namespace membership should fail at the appropriate decision or gate [2]. Separately remove residue bookkeeping, qualification freshness checks, or effect enforcement to identify their contributions.

CogK cases include an unaccepted offer, a queued message mistaken for handoff, an expired custodian without a successor, a candidate mistaken for discharge, repeated attempts without new evidence, unsupported urgency, and a context budget too small for required controls. Each case declares the expected disposition, surviving obligation, and custody state.

Recovery testing includes lost receipts, uncertain completion, replayed warrants, conflicting branches, and invalidated identity caches. Compensation is not rollback, external effects are not universally reversible, and repeating execution is not receipt replay.

## 14. Full Realization Funnel

The ABI occupies several distinct layers of the corpus realization funnel:

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

| Stage | Cognitive-ABI placement |
| :--- | :--- |
| Possibility | Alternative capability boundaries, semantic classes, realization kinds, assurance regimes, routing strategies, custody models, and evidence arrangements. |
| Specification | Typed capability contracts, semantic obligations, authority and effect constraints, qualification scope, residue and custody invariants, workflow edges, refusal conditions, and evidence classes. |
| CM1 | Configurations satisfying mandatory admissibility: coherent descriptors, preserved obligations, explicit authority, bounded effects, scoped qualification, non-silent residue, recoverable identity, and required witnesses. Harmful, unusable, or inefficient configurations can still be structurally admissible here. |
| CM2 | Preferred admissible configurations under declared objectives such as least authority, local or replaceable realizations, inspectability, privacy, recovery, lower cost, bounded latency, stronger assurance, and reduced trusted surface. Preference never substitutes for CM1 admissibility. |
| IC | **Instance Constitution** and **Instance Configuration** are interchangeable names for the same stage: the selected contracts, backends, policies, schemas, thresholds, budgets, custody roles, evidence profile, and recovery rules for one bounded instance. |
| IR | **Instance Realization** and **Implementation Realization** are interchangeable names for the same stage: the exact source, builds, deployed components, runtime state, invocations, observations, and effects that make the selected IC concrete. The name chosen does not change standing. |
| Evidence | Qualification fixtures, correspondence witnesses, receipts, manifests, observations, audits, counterexamples, performance records, and independent reproduction results evaluated against explicit claims. |
| Revision | Contract repair, requalification, decrystallization, quarantine, backend substitution, policy amendment, evidence invalidation, rollback or compensation, and lineage-preserving successor formation. |

The manuscript specifies the ABI through CM2, proposes classes of IC, and reports one bounded local IR with evidence. That recorded IR does not establish every ABI contract, a production Cognitive Kernel integration, general substitution, or publication-ready reproducibility.

## 15. GMB, Universal GSM, and Corpus Interfaces

The **Governed Meaning Base (GMB)** is the current name in the author-confirmed `CCF -> CMB -> GMB` lineage. GMB can preserve capability definitions, contract versions, semantic identities, qualification scopes, realization profiles, authority references, residue, custody, workflow dependencies, evidence, counterevidence, and revision lineage. It is not the capability executor, qualification authority, effect boundary, verifier, or proof that a realization satisfies its contract.

The universal GSM should keep at least these identities distinct: capability, capability contract, obligation, request, semantic regime, implementation, realization profile, qualification claim, admission decision, authority grant, warrant, effect envelope, workflow node, dependency edge, residue, work object, custodian, custody transition, evidence artifact, receipt, observation, correspondence witness, semantic identity, hash commitment, refusal, counterexample, and revision. Important relations include `SPECIFIES`,  
`REQUIRES`, `QUALIFIED_FOR`, `ADMITTED_UNDER`, `AUTHORIZED_BY`, `REALIZED_BY`, `INVOKED_AS`,  
`OBSERVED_AS`, `EVIDENCED_BY`, `REFUSED_BY`, `PRESERVES`, `DISCHARGES`, `LEAVES_RESIDUE`,  
`CUSTODIED_BY`, `COUNTEREVIDENCED_BY`, and `SUCCEEDS`.

The paper's representation interfaces must not collapse into one generic IR. **Action IR** binds intended operations and effects; **Workflow IR** composes invocations and dependencies; **Epistemic IR** represents claims, support, uncertainty, rivals, and epistemic motion; **GSOL** specifies governed semantic operations; **MCIR** and related compiler representations carry constitutional or meaning obligations across lowering. These may share typed translation contracts and conservation tests without being identical formats or automatic implementations of one another.

Direct corpus interfaces are therefore:

* *Hybrid Semantic Compiler Architectures* supplies FSC/DSC closure and maturation; it does not itself supply an ABI implementation.
* *Exigence and the Cognitive Kernel* supplies situated need, attention, sufficiency, and reconsideration; it does not grant execution authority.
* *Who Has the Ball?* and *A Formal Theory of Work Custody* supply responsibility and transfer semantics; they remain distinct from evidence custody.
* *The Three Hash Rule* supplies independent commitment surfaces; hashes and valid receipts do not establish truth, authority beyond policy, or effect occurrence.
* *Sovereign Software* supplies the replacement, inspection, reconstruction, and provider-exit objective that makes qualified realization substitution socially consequential.
* *Epistemic IR* and GSOL supply adjacent representation and operation layers. Their contracts need explicit translators rather than name-based merger.

## Contract Boundary for Cognitive and Effect Capabilities

The completed P1 corpus compresses the Cognitive ABI to a precise role: it is the **contract, qualification, and substitution boundary** through which cognitive operations and system-effect operations can be requested without binding callers to one realization. It is not CogK, a model router, a capability grant, a proof system, an orchestrator, or the Universal Capability Model itself.

- **Adjacent work:** *Everything Is a Compiler*  
  **Supplies:** The general view of systems as governed transformations among representations.  
  **Cognitive ABI boundary:** The ABI specifies callable obligations and outcomes, not the whole compilation thesis.

- **Adjacent work:** *Exigence and the Cognitive Kernel*  
  **Supplies:** Attention, need, sufficiency, reconsideration, and cognitive control.  
  **Cognitive ABI boundary:** CogK may call and implement capabilities; it does not become the ABI or self-authorize effects.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Responsibility for recognized work, transfer, return, and terminal disposition.  
  **Cognitive ABI boundary:** Custody may be required by a workflow contract; it is not implied by invocation.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Bounded reasoning and transition records.  
  **Cognitive ABI boundary:** Receipts preserve decisions and observations; they do not create competence, permission, or semantic closure.

- **Adjacent work:** *Transformation-Dominant Semantic Systems*  
  **Supplies:** A diagnostic of useful transformation, obligation carriage, loss, and recoverability.  
  **Cognitive ABI boundary:** The ABI declares what must survive substitution; TDSS diagnoses how a realization actually carries it.

The ABI must keep at least seven objects separate:

$$
ABIObject=(K,r,q,g,i,y,e),
$$

where $K$ is the capability contract, $r$ a realization, $q$ scoped qualification evidence, $g$ a current authority grant, $i$ an invocation, $y$ its returned result or refusal, and $e$ witnesses, receipts, and effect evidence. Interface compatibility alone does not establish any of the other six.

A route is eligible only through an intersection:

$$
Eligible(r,K,i)=Conforms\cap Qualified\cap Admitted\cap Authorized\cap EffectPermitted\cap Witnessable.
$$

This expression is a dependency rule, not evidence that every predicate has been established. Substitution additionally requires preservation of declared obligations, outcome semantics, refusal behavior, evidence class, residue, and effect ceiling. A more capable realization may be ineligible precisely because its additional effects exceed the contract.

The universal GSM can type `DECLARES_CAPABILITY`, `REALIZED_BY`, `QUALIFIED_FOR`,  
`ADMITTED_UNDER`, `AUTHORIZED_BY`, `INVOKED_AS`, `RETURNS_RESULT`, `RETURNS_RESIDUE`,  
`EMITS_RECEIPT`, `OBSERVED_EFFECT`, `SUBSTITUTES_FOR`,  
and `INVALIDATED_BY`. Qualification and authority remain time-, environment-, subject-, and contract-scoped edges rather than permanent properties of a model or tool.

This integration establishes four editorial commitments: adopt contract/qualification/substitution boundary as the official corpus role; adopt the seven-object separation; adopt eligibility as an intersection rather than a scalar score; and require substitution to conserve residue, refusal, evidence, and effect obligations as well as successful outputs.

## Resumable Capability Invocation and Admission Chain

The fixed-seed comparison with Semantic Computing Infrastructure, Cold Boot Continuity, Crystallized Governance, and Admissibility Engineering gives a resumed invocation an explicit dependency chain:

$$
\begin{aligned}
C= (&contract, provider, state\_root, checkpoint, \\
&qualification, admission, authority, effect\_ceiling, \\
&invocation, result, residue, evidence)
\end{aligned}.
$$

Semantic Computing Infrastructure may provide identity, memory, navigation, compilation, or evidence capabilities. The ABI exposes those capabilities through contracts; it does not make the provider state current or semantically equivalent. After cold boot, the successor must verify the checkpoint, reconstruct or select the relevant state root, and re-evaluate provider qualification.

Crystallized-governance artifacts can supply rule and correspondence inputs to admission. They do not themselves issue a current authority grant, and ABI compatibility does not prove legitimate adoption or interpretation. Authority, jurisdiction, subject, expiry, and permitted effect remain invocation-specific.

Admissibility Engineering tests whether consequence-bearing paths are actually constrained across the chosen provider, adapter, retry, error, cache, fallback, and effect surfaces. A provider can satisfy the interface while opening a bypass or silently changing residue. Substitution therefore requires pathway evidence in addition to contract conformance.

The universal GSM can type   
`RESTORES_CAPABILITY_CHECKPOINT`,  
`QUALIFIES_PROVIDER_FOR_CONTRACT`, `ADMITS_INVOCATION_UNDER_GOVERNANCE`,  
`REBINDS_CURRENT_AUTHORITY`, `TESTS_CAPABILITY_PATHWAY`, `RETURNS_TYPED_RESIDUE`,  
and   
`INVALIDATES_SUBSTITUTION_ON_BYPASS`.

This randomized review establishes four editorial commitments: adopt the resumable invocation chain; require provider and state-root requalification after cold boot; keep governance artifacts below current authority; and require pathway-constraint evidence for capability substitution.

## Versioned Invocation and Substitution Under Live Conditions

Eleven downstream uses place the Cognitive ABI between callers and cognitive, semantic, or effect capabilities. Admissibility Engineering tests the realized pathway; cold boot requires rebinding; cyber-physical control separates planning from device authority; crystallized governance supplies rule inputs without granting current permission; CogK supplies attention without eligibility; GCNL can request but not grant a capability; Meta-Binding may occupy one capability surface; Semantic Computing Infrastructure supplies providers; Sovereign Software supplies the social purpose of replacement; split-authority coordination configures role authority; and Work Custody supplies responsibility where required.

The live invocation envelope is:

$$
\begin{aligned}
I^*= (&contract\_id, version, semantic\_regime, caller, \\
&provider, adapter, state\_root, qualification, admission, \\
&authority, effect\_ceiling, resource\_budget, privacy, \\
&liveness, nondeterminism, invocation, result, residue, \\
&witness, recovery, expiry)
\end{aligned}.
$$

Compatibility, substitutability, and eligibility are distinct. Compatibility means the parties can exchange a declared protocol version. Semantic substitutability means specified successful outputs, refusals, residue, identity, state transitions, and evidence obligations are preserved within a tolerance and loss declaration. Operational eligibility additionally requires current qualification, admission, authority, effect permission, resource and privacy bounds, pathway evidence, and witnessability for the exact invocation.

Adapters, caches, retries, fallbacks, checkpoints, and provider state are part of the pathway when they can alter semantics or effects. Version negotiation must return accepted profile, downgraded obligations, unsupported requirements, and remainder rather than silently selecting the nearest interface. Stateful or long-running invocations need checkpoint identity, idempotency or compensation rules, custody, timeout, cancellation, resumption, and late-result handling. Additional provider capability never expands the caller's authorized effect ceiling.

The universal GSM can type   
`NEGOTIATES_COGNITIVE_ABI_VERSION`,  
`IS_PROTOCOL_COMPATIBLE_WITH`, `IS_SEMANTICALLY_SUBSTITUTABLE_FOR`,  
`IS_ELIGIBLE_FOR_INVOCATION`, `LOWERS_THROUGH_ADAPTER`, `CHECKPOINTS_CAPABILITY_STATE`,  
`RETURNS_ABI_REMAINDER`, and   
`DOES_NOT_EXPAND_EFFECT_CEILING`.

This reverse-dependency review establishes four editorial commitments: adopt the live invocation envelope; separate protocol compatibility, semantic substitution, and invocation eligibility; bind adapters and stateful recovery into pathway review; and require explicit negotiation, downgrade, remainder, and non-expansion of authority.

## Capability Substitution Without Semantic Disappearance

### Public orientation

The Cognitive ABI separates a requested capability from the model, tool, workflow, or human process that realizes it. This can make agentic work substitutable and resumable while preserving authority, evidence, and semantic residue. An ABI contract does not make unlike providers equivalent or authorize the selected provider to act.

### Adversarial tests

1. **False-substitution attack.** Two providers satisfy the same surface type while differing in semantics, uncertainty, side effects, privacy, or failure behavior. Qualification must be capability-, profile-, environment-, and time-specific.
2. **Stale-qualification attack.** A provider changes after evaluation. Admission binds an exact version, dependencies, configuration, and evidence epoch.
3. **Residue-loss attack.** Unresolved assumptions, ambiguity, rejected alternatives, or partial work vanish across the boundary. Residue is a typed return obligation, not optional commentary.
4. **Authority-leak attack.** Capability to propose, compile, or evaluate becomes effect authority. Invocation must intersect capability with mandate, jurisdiction, and effect grant.
5. **Three-hash oracle attack.** Matching commitments are treated as semantic correctness. Hashes bind artifacts and decisions under canonicalization; they do not prove adequacy, truth, or safe effect.
6. **Control-closure attack.** The workflow reaches a terminal protocol state while the task remains unresolved. Control closure and problem resolution require separate outcomes.
7. **Context-poisoning attack.** A valid provider receives misleading, unauthorized, or insufficient context. Context admission, transformation, omission, and standing remain part of the call contract.
8. **Performance-opacity attack.** Governance overhead or provider variance is hidden behind a uniform interface. Cost, latency, energy, and assurance must be profile dimensions.

### Claim and evidence ceiling

The implemented vertical slice supports the bounded claim that the specified composition can run and expose certain defects in its recorded environment. It does not establish broad provider substitutability, production security, semantic equivalence, scaling, or comparative performance.

Artifact availability, reproduction instructions, exact versions, and acceptance criteria must be complete before implementation claims are publication-ready. Related-work and performance claims require resolvable external sources and measurements. No external research was added in this pass.

### Reader-facing consequence

The ABI's public value is portable cognitive work without pretending away differences: an agent can ask for a capability, receive evidence and residue, change providers, and resume the work while authority and unresolved meaning remain visible.

## 16. Counterevidence and Attack Surface

The architecture is weakened, narrowed, or falsified where: (1) a capability contract omits behavior that users rely on; (2) finite qualification misses a substituting realization's divergence; (3) producer and verifier share the same defect or compromised dependency; (4) qualification or admission evidence is forged, stale, revoked, or scoped to another environment; (5) caches retain invalid identity, authority, or qualification state; (6) a backend bypasses effect mediation or hides resource use; (7) liveness, concurrency, retries, or shared state violate the paper's bounded execution assumptions; (8) a substitute preserves outputs but changes latency, privacy, side channels, cost, or refusal behavior; (9) residue is weakened, duplicated, or lost through split and merge; (10) custody becomes orphaned while the obligation remains; (11) control closure is misreported as substantive resolution; (12) contextual compression removes a controlling rule; (13) witness participants collude or observe the same faulty surface; (14) recovery repeats a non-idempotent effect; or (15) the local package cannot be reproduced from a stable public release.

## 17. Limitations and Architectural Consequences

The evidence boundary is stated in Section 10.4. A complete cognitive operating system, general mixed-workflow superiority, and the proposed CogK integration require further experiments; Further evidentiary strengthening requires the artifact materials in Appendix A.

Contracts can be incomplete, verifiers can share implementation defects, and authentic observations can be inaccurate. An FSC may miss ambiguity; a DSC may execute a poor model perfectly. Cryptographic integrity does not ensure receipt availability or complete observation. Backends able to bypass effect mediation lie outside the enforcement claim.

CogK can misjudge Exigence, miss dependencies, retain stale interpretations, or apply an inadequate nonprogress model. Its outputs need scoped evidence and revision paths. Obligation and custody conservation are preservation properties, not guarantees of timely progress, agreement, or a correct worldview.

Closure also has costs. Excessive crystallization can create brittle procedure; premature formalization can destroy useful ambiguity [1]. Frontier operation must remain available under explicit constraints. Realization sovereignty can permit local execution, human participation, replacement implementations, and retention of a working version. Retention does not exempt a realization from qualification invalidation, while invalidation does not authorize forced software replacement. Compatibility, lifecycle, and trust-boundary policies must make both limits explicit.

## 18. Conclusion

The cognitive ABI defines an obligation independently of its engine, composes operations through Workflow IR, and keeps meaning, competence, admission, permission, effects, residue, and evidence separately inspectable.

CogK supplies situated cognitive control: what changed, what it might mean, what calls for transition, who holds the next move, and what is missing. The ABI provides stable contracts for that work and for CogK's own operations. Residue conservation preserves the question; Work Custody preserves the responsibility account. Neither manufactures authority or progress.

The Three Hash Rule supplies independent state, admissibility, and meaning commitments, optional locality, and recoverable receipt binding. HSC supplies the lifecycle through which FSC precedent can become qualified DSC substrate and invalidated substrate can return to review, quarantine, or frontier work.

The implemented crossing from deterministic cognitive operations to a governed system effect establishes bounded feasibility. The next empirical threshold is the mixed investigation and matched evaluation specified here.

A capability-centered computer need not unify every resource into one implementation or authority. It needs inspectable relationships among need, obligation, realization, and consequence. CogK governs why a next move is called for. The ABI governs what that move must preserve. Neither lets the engine's confidence substitute for the promise.

## Appendix A. Artifact Availability and Reproduction Contract

### A.1 Availability in this manuscript version

The implementation remains an author-verified local candidate [7]. This manuscript does not identify a stable public source-and-evidence deposit or an artifact DOI. The Three Hash Rule's publication DOI [2] identifies that paper, not this implementation. Public artifact release is an outstanding publication prerequisite, separate from independent reproduction and live-system admission.

The existing record identifies:

```text
DSC-COGNITIVE-ABI-CANDIDATE-REPORT.md
CROSS-PLANE-MANIFEST.json
cross-plane-proof/CROSS-PLANE-VERTICAL-PROOF-RESULT.json
cross-plane-proof/artifacts/08-cross-plane-identity-proof.json
```

Its cross-plane manifest root is:

```text
8a774327a8183322f5c395fcfca66af5f59ebe87cb7663ad8863596aee59123b
```

This native manifest identifier is not relabeled as $H_s$, $H_m$, or $H_r$ without a documented schema mapping. A local filename or digest identifies evidence but does not make it publicly retrievable.

### A.2 Required archival release

A version-specific archival repository or deposit should bind the following materials into one release manifest:

| Release component | Required content and present status |
| :--- | :--- |
| Source snapshot | Exact revision and source archive, executor and verifier code, schemas, tests, fixtures, and local patches. Public snapshot not identified here. |
| Evidence package | Native manifest, sealed result, identity evidence, object-store closure, test logs, and policy snapshots. Filenames and root are identified; public package remains to be supplied. |
| Reproduction procedure | Exact tested commands, working directories, arguments, environment variables, expected exit codes, timeouts, cleanup, and negative tests. Executable commands are not specified in this version. |
| Runtime dependencies | Pinned interpreter, packages, native tools, hashes, supported platforms, and any offline installation bundle. Exact dependency lockfile remains to be supplied. |
| Hardware and OS | OS edition/build, architecture, CPU, RAM, storage, and relevant accelerator or firmware details. The original execution environment is not specified here; the 204.548-second duration is not portable benchmark evidence. |
| Expected outputs | The validation counts in Section 10.2, exact historic roots, regenerated-result acceptance predicates, and declared canonicalization exclusions. |
| Nondeterministic inputs | Actual inventory of time, nonces, ordering, host identity, paths, external state, and other variable inputs; for each, pin, record, or explicitly exclude it from the replay claim. |
| License and access | Author-selected source, data, and document licenses; third-party notices and redistribution constraints. No implementation license is assigned by this manuscript. |
| Persistent identity | Version-specific public identifier or DOI, archive checksum, and a manifest binding source, evidence, environment, and reproduction procedure. No artifact DOI is asserted here. |

These are release requirements, not substituted metadata. The current account records zero model and network calls in the executed workflow; that does not prove every installation step is offline or eliminate variable host inputs.

### A.3 Reproduction acceptance

The release procedure must distinguish three operations. **Historic verification** checks the supplied immutable package and its native root. **Deterministic replay** recomputes declared operations under pinned inputs and checks their specified output identities or equivalence predicates. **Fresh execution** obtains valid present authority and produces new observations and receipts.

A fresh run need not reproduce the historic manifest root: timestamps, nonces, warrants, and environment identities may legitimately change. The release must name which bytes and roots are invariant and which relationships are checked instead. Consumed warrants must not be reused to obtain matching bytes, and redaction must not be presented as preserving an unchanged sealed root.

The archived procedure should execute compatibility and focused tests, the 105-trial qualification campaign, the bounded cross-plane workflow, and the artifact/object-store audit in a clean environment. It should state expected pass counts and negative dispositions, record the complete transcript, and identify every unexecuted step. Independent reproduction is established by that campaign, not by the existence of a DOI alone.

## Appendix B. Three Hash Rule Constructions and Binding Configurations

This appendix carries the detailed constructions from the Three Hash Rule [2] that are needed to specify the ABI's receipt interface. Section 7 states their operational role. The source framework determines the constructions; this paper adds their cognitive-workflow mapping.

### B.1 Constitutional Legend and canonicalization

The Constitutional Legend is:

$$
L=(J_L,B_L,R_L,T_L,C_L,A_L).
$$

Jurisdiction projects to $H_j$; bindings and render surfaces contribute to $H_m$; transport governs receipt binding; continuity governs recoverability; authority contributes to $H_c$. The constitution decides what facts enter these commitments rather than treating implementation metadata as inherently authoritative.

For $i\in\{s,c,m,j\}$, canonicalization is versioned:

$$
c_i:X\rightarrow B_i\cup\{\bot\}.
$$

It is deterministic and byte-stable, total on its declared domain, and explicitly rejecting outside it. If $c_i(x)=\bot$, then $D_i=0$. Conformance vectors must specify ordering, whitespace, Unicode normalization, numbers, duplicate fields, byte order, typed lengths, partial decoding, and parser ambiguity handling. Domain tags $DS_i$ separate commitment types.

### B.2 State and admissibility

$$
H_s=H(DS_s\parallel id(c_s)\parallel c_s(x)).
$$

$D_s$ checks that the state witness opens $x$ under $c_s$. Admissibility uses a Merkleized labeled authority DAG $G_c$:

$$
H_c=H(DS_c\parallel id(c_c)\parallel root(G_c)\parallel id(P)?).
$$

The optional policy identifier prevents policy shadowing where required. $D_c$ checks a canonical witnessed path under policy, including constraints, freshness, revocation, and attenuation:

$$
cap(e_{r+1})\subseteq cap(e_r).
$$

Policy may require a permitted executor to hold current qualification or a recognized role. Those requirements enter admissibility because the constitution declares them. Evaluator identity is provenance unless policy makes authorized evaluator status relevant; historical delegation evidence remains distinct from present derived authority.

### B.3 Bounded meaning and semantic lineage

The semantic regime is:

$$
\Sigma=(L,T,R,v,r^*,B,imports),
$$

specifying language, theory, rules, version, canonical reduction strategy, normalization bound, and import treatment. Within this tuple, $R$ means a rule set rather than a receipt, and $B$ means a bound rather than the request binding. Then:

$$
c_m(x)=encode(r^*(parse_L(x))),
$$

$$
H_m=H(DS_m\parallel id(c_m)\parallel c_m(x)
\parallel id(\Sigma)\parallel lineage).
$$

$D_m$ verifies parsing, bounded regime-specific normalization, and authenticated semantic lineage. Uninterpreted regions are hashed placeholders. The construction assumes a declared deterministic parser and canonical reduction strategy; it is not canonicalization of unrestricted natural language.

Jurisdiction is excluded from the identity-determining components of $\Sigma$: locality and authority are committed separately. Semantic lineage records meaning transformations; authority lineage records delegation and attenuation. Their histories must not be conflated.

### B.4 Optional locality

$$
H_j=H(DS_j\parallel id(c_j)\parallel id(\Phi)\parallel authority\_key).
$$

For a phase-bound namespace map:

$$
M_\Phi:name\_key\mapsto H_s,
$$

$D_j$ verifies required membership. If $H_j$ is absent and locality is not required, $D_j=\mathsf{NA}$. Namespace updates require admissibility; a phase change cannot silently replace the meaning or authority checks.

### B.5 Context and receipt binding

The validity context and its identity are:

$$
\begin{aligned}
\mathcal{C}= (&P, \Sigma, \Phi, t), \\
&\qquad id(\mathcal{C})=H(id(P)\parallel id(\Sigma)\parallel id(\Phi)\parallel t)
\end{aligned}.
$$

Context-external receipt identity is:

$$
H_r=H(DS_r\parallel root(H_s,H_c,H_m,H_j?)).
$$

Strict receipt identity is:

$$
H_r=H(DS_r\parallel
root(H_s,H_c,H_m,H_j?,id(P),id(\Sigma),id(\Phi))).
$$

The root is a deterministic domain-separated tree over typed, length-prefixed leaves. In strict and context-external modes, each witness binds $H_r$, $H_s$, and $id(\mathcal{C})$. Explicit time remains part of that witness-bound context even though it is not a separate leaf in the displayed strict receipt formula.

The admissible configurations are **strict identity**, the preferential default; **context-external identity with disambiguating evidence**, when a portable bundle handle is justified; and **re-evaluable**, an explicit opt-in exception whose witnesses do not pin $id(\mathcal{C})$. The exception shifts responsibility to the supplied evaluation context rather than silently weakening the default.

Binding verification checks recoverability of excluded context under the declared configuration. It rejects inconsistent object, receipt, or context bindings and under-recorded collapse as   
`UnderRecordedCollapse`. This well-formedness gate is required alongside $D_s,D_c,D_m$ and applicable $D_j$; it is not an additional governance decision axis.

All evaluations must use pure, versioned inputs and explicit time. Live authorization and warrant consumption are separately governed stateful operations, not undeclared I/O inside receipt verification.

---

## Editorial Provenance and Standing

### Source, Evidence, and Standing
This is an AI-prepared successor revision candidate derived from one exact author manuscript. The integration custody manifest is   
`work/paper-saturation-v1/evidence/cognitive-`

`abi-capability-centered-computing/integration-`  
`custody-manifest.v0.1.json`,  
SHA-256  
`2AC762A5E6FB4D18C9F6621E2F488B18112BB4746E13DFFB0E5066805F3DC87C`. The exact source remains unchanged. The Cognitive ABI thesis, HSC/CogK/Three Hash Rule synthesis, capability and qualification contracts, typed-residue model, Workflow IR, local vertical-slice account, evaluation agenda, appendices, and original references are author material. This pass standardizes presentation; makes the full realization funnel, GMB, universal GSM, and corpus interfaces explicit; records missing figure custody; audits the cited local evidence files; and adds counterevidence and author-decision surfaces. Those additions are AI editorial or synthetic contributions until adopted.
The cited local implementation package exists and its four named evidence files match exact recorded hashes. Structural readback confirms the manifest root, 35 compatibility tests, 44 focused tests, 105 qualification trials, four cognitive operations, one system-effect operation, zero model and network calls, zero production-route changes, and a 204.548-second recorded run. This pass did not rebuild or replay that package. The 54,736-file enrollment count and artifact/object-store audit are retained as author-reported statements from the bound report. AOK/AOK-G remains excluded from Ableman semantic integration and is used here only for custody of implementation evidence directly cited by the paper.

## Corpus-Wide Reference Positioning

This paper argues that a capability should not be identified with the implementation that happens to realize it. Its nearest external comparison fields are formal, security, ai. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E2]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E3]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

**[E4]** Leslie Lamport. *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Addison-Wesley, 2002. https://lamport.azurewebsites.net/tla/book.html **Relationship:** Predecessor specification discipline for state machines, safety, liveness, and refinement.

**[E5]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E6]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E7]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

#### Source-head external references retained under original labels

[8] Wang, Jincheng, Min Zheng, and Tao Wei. "COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution." arXiv:2607.25400v1, 2026. DOI: 10.48550/arXiv.2607.25400.

[9] Chivukula, Abhi, Jay Somasundaram, and Vijay Somasundaram. "Agint: Agentic Graph Compilation for Software Engineering Agents." arXiv:2511.19635v1, 2025. DOI: 10.48550/arXiv.2511.19635. Author preprint associated with the Deep Learning for Code workshop.

[10] Khattab, Omar, et al. "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines." arXiv:2310.03714, 2023. DOI: 10.48550/arXiv.2310.03714.

[11] Karpas, Ehud, et al. "MRKL Systems: A Modular, Neuro-Symbolic Architecture That Combines Large Language Models, External Knowledge Sources and Discrete Reasoning." arXiv:2205.00445, 2022. DOI: 10.48550/arXiv.2205.00445.

[12] Torres-Arias, Santiago, Hammad Afzali, Trishank Karthik Kuppusamy, Reza Curtmola, and Justin Cappos. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410.

[13] W3C. *PROV-O: The PROV Ontology.* W3C Recommendation, April 30, 2013. Document identifier: `TR/prov-o`.

[14] Mettler, Adrian, and David Wagner. *The Joe-E Language Specification, Version 1.0.* Technical Report UCB/EECS-2008-91, University of California, Berkeley, 2008.

[15] Mininger, Aaron, and John E. Laird. "A Demonstration of Compositional, Hierarchical Interactive Task Learning." *Proceedings of the AAAI Conference on Artificial Intelligence* 36(11), 2022, pp. 13203-13205. DOI: 10.1609/aaai.v36i11.21728.

[16] Wen, Cheng, et al. "Formally Specifying the Intended Behavior of the Program: LLM-Driven Neuro-Symbolic Program Specification Synthesis." *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics, Volume 3: System Demonstrations*, 2026, pp. 672-682. DOI: 10.18653/v1/2026.acl-demo.66. Accompanying author-maintained artifact:   
`Xidian-ICTT-GZ/AutoSpec`, *AutoSpec+: LLM-Driven Neuro-Symbolic Program Specification Synthesis*, README consulted September 17, 2026.

[17] CompCert Project. "CompCert C: A Trustworthy Compiler." *CompCert User Manual*, Chapter 1. Official documentation, `man/manual001.html`, consulted September 17, 2026.

[18] Necula, George C. "Proof-Carrying Code." *Proceedings of the 24th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. See also the author's *Proof-Carrying Code* research overview, University of California, Berkeley.

[19] Bytecode Alliance. "WIT Reference." *The WebAssembly Component Model*. Official documentation, `design/wit.html`, consulted September 17, 2026.

[20] Yao, Shunyu, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. "ReAct: Synergizing Reasoning and Acting in Language Models." *International Conference on Learning Representations*, 2023. arXiv:2210.03629v3. DOI: 10.48550/arXiv.2210.03629.

[21] Object Management Group. *Business Process Model and Notation (BPMN), Version 2.0.2.* Formal specification, document formal/2013-12-09, December 2013; adopted January 2014. Sections 10 and 13.

[22] Fox, Maria, and Derek Long. "PDDL2.1: An Extension to PDDL for Expressing Temporal Planning Domains." *Journal of Artificial Intelligence Research* 20, 2003, pp. 61-124.

[23] seL4 Project. "Capabilities." *seL4 Documentation*, tutorial and capability-space reference. Official documentation,   
`Tutorials/capabilities.html`, consulted September 17, 2026.

[24] Leijen, Daan. "Koka: Programming with Row Polymorphic Effect Types." *Electronic Proceedings in Theoretical Computer Science* 153, 2014, pp. 100-126. DOI: 10.4204/EPTCS.153.8. arXiv:1406.2061.

### Ableman corpus

**[A1]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Ableman Corpus current edition; work identity `PAPER.PUB.21095303`;  
source SHA-256  
`EA129ECBA95F7B07CAA7B33A54F91F52913C94A14DA227EB9A06CFD083E4E5BF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Governed Semantic Compilation*. Ableman Corpus current edition; work identity `PAPER.PUB.18453681`;  
source SHA-256  
`5FF6C636550B04DB0E2F6F94C379BB75AA0BD8781E19B047D7D3BB6D49071AC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Hybrid Semantic Compiler Architectures*. Ableman Corpus current edition; work identity `PAPER.PUB.21228038`;  
source SHA-256  
`EBCD6DDDA9B547639AEBED79FB68069473CF1248E41C527B48C9624BBE2C0496`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Admissibility Engineering*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F1E33B5E973B0900`;  
source SHA-256  
`CDC80271268802CA5CB4DE3624B992FB2FF07D677BF945C4B349BD307C4C2A6E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Everything Is a Compiler*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-30FB8F95BD990A47`;  
source SHA-256  
`FE0F88A1F125317285BE4378E5F27ACC9FEB83ADE3FF329A3DA9F9CB026DF9A9`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

#### Ableman Corpus references

[1] Adam Ableman. *Hybrid Semantic Compiler Architectures: Frontier Semantic Operators, Governed Closure, and the Moving Boundary Between Fuzzy and Deterministic Semantic Computation.* Constitutional Computing, manuscript, 2026.

[2] Adam Ableman. *The Three Hash Rule: Governance Completeness Through Independent Cryptographic Commitments.* Constitutional Computing, 2026. DOI: 10.5281/zenodo.20788617. Formalization cited from the manuscript revision provided September 17, 2026.

[3] Adam Ableman. *Exigence and the Cognitive Kernel.* Constitutional Computing, manuscript. Cited version:   
`Exigence and the Cognitive Kernel.md`; Sections 2-9, 16-19.

[4] Adam Ableman. *Who Has the Ball? Work Custody as a Primitive of Human-Agent Collaboration.* Constitutional Computing, manuscript. Cited version: `Who Has the Ball.md`.

[5] Adam Ableman. *A Formal Theory of Work Custody: Invariants, State Machines, and Constitutional Collaboration.* Constitutional Computing, manuscript. Cited version:   
`A Formal Theory of Work Custody.md`.

[6] Adam Ableman. *CGSOS Gravity-Well Architectural Navigator.* Project architectural mapping,   
`cgsos_gravity_well_navigator_template.html`, capability-kernel and constitutional-reactor entries. Cited for the declared separation of CogK, UGK, witness, and Executive responsibilities; not as an execution-test report.

[7] Adam Ableman. *DSC Cognitive ABI Candidate Report and Cross-Plane Vertical Proof Artifacts.* AOK/DSC implementation record, candidate directory   
`aok-dsc-cognitive-abi-20260916`, September 2026. Artifact names and manifest root are given in Appendix A. Author-verified local candidate; independent reproduction and live admission outstanding.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847350](https://doi.org/10.5281/zenodo.23847350)
