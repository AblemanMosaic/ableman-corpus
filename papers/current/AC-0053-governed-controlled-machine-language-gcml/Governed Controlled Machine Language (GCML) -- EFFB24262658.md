# Governed Controlled Machine Language (GCML)

## Procedural Stabilization Between Constitutional Meaning and Machine Execution

### Under the interpretation developed here, GCML does not decide what an operation means or whether its originating semantic artifact deserves admission.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Conventional compilation stacks translate programs through intermediate representations designed for transformation, optimization, portability, and execution. In governed computation, another question precedes machine emission: even when a semantic operation is admissible, does the selected procedure preserve its authority, capability, refusal, evidence, and effect obligations?

This paper develops **Governed Controlled Machine Language (GCML)** as a candidate procedural stabilization layer between admitted constitutional meaning and execution-ready realization. Under the interpretation developed here, GCML does not decide what an operation means or whether its originating semantic artifact deserves admission. It binds an admitted operation to a target-neutral procedural plan whose dependency graph, capability budget, effect call sites, resource assumptions, nondeterminism, refusal branches, receipt obligations, and lowering contract are explicit before target-specific emission.

The paper also identifies an unresolved architecture question. The source GCML paper places GCML after MCIR-Law, while the current GSOL v0.1 specification places GCML before MCIR and PEIR and permits several direct lowering targets. Program Execution Intermediate Representation (PEIR) already names the layer where canonical semantic artifacts become executable operational structures. GCML may therefore be a distinct language, a constrained profile of PEIR, a GSOL-to-PEIR lowering contract, or a restatement of machinery already present in those systems. This paper specifies a discriminating contract but does not settle that identity by assertion.

The result is a meaning-to-machine gradient in which each boundary has separate responsibilities: language stabilization, governed operation semantics, canonical meaning, admissibility, procedural selection, execution realization, effect adjudication, and evidence. The proposal supplies formal obligations, an artifact schema, a worked example, conformance tests, failure modes, the full realization funnel, and corpus integration. It does not claim a production compiler, deterministic replay of arbitrary external worlds, universal hardware equivalence, or superiority to existing compiler and capability systems without direct research and implementation evidence.

**Keywords:** governed compilation; intermediate representation; procedural stabilization; MCIR; PEIR; GSOL; capability containment; effect membrane; lowering; replay; receipts.

## 1. The Procedural Governance Gap

Compilation pipelines commonly assume that once source semantics are accepted, backend construction of an execution plan is legitimate. Instruction selection, scheduling, resource allocation, runtime calls, optimization, fallback, and target adaptation are delegated to compilers and runtimes. In ordinary settings this may be appropriate. In systems that claim explicit authority, bounded capabilities, receipted effects, or auditable AI-generated transformations, it leaves a constitutional gap.

The core question is:

> Even if an operation's meaning is admissible, is the procedure chosen to realize it itself admissible under the operation's declared constraints?

Several failures can occur after semantic admission:

* a lowering introduces a capability absent from the source contract;
* an optimization removes a refusal or evidence branch;
* a target backend replaces a declared effect call with an ambient system call;
* scheduling creates a race where the source operation required ordering;
* resource fallback crosses a jurisdiction or privacy boundary;
* replay claims ignore time, randomness, external services, or mutable state;
* machine output remains byte-reproducible while semantic obligations drift.

GCML is proposed as a boundary at which these procedural choices become explicit artifacts rather than ambient compiler discretion.

## 2. Layer Responsibilities and the Identity Question

The corpus contains several neighboring representations. Their responsibilities must be distinguished before GCML can justify a separate identity.

- **Layer or construct:** GCNL  
  **Primary responsibility:** stabilize governed declarative language  
  **What it should not silently decide:** executable procedure

- **Layer or construct:** GSOL  
  **Primary responsibility:** state canonical governed operation semantics, authority, effects, refusal, receipts, claims, nonclaims, standing, time, and lowering obligations  
  **What it should not silently decide:** target scheduling or machine instruction choice

- **Layer or construct:** MCIR  
  **Primary responsibility:** carry canonical machine-legible semantic and constitutional commitments  
  **What it should not silently decide:** whether a particular backend procedure preserves them

- **Layer or construct:** MCIR-Law  
  **Primary responsibility:** admit, refuse, or condition a semantic artifact under declared law  
  **What it should not silently decide:** target-specific execution strategy

- **Layer or construct:** GCML candidate  
  **Primary responsibility:** bind an admitted operation to a target-neutral procedural graph and preservation contract  
  **What it should not silently decide:** redefine source meaning, widen authority, or grant effects

- **Layer or construct:** PEIR  
  **Primary responsibility:** represent execution-ready operational structure, potentially including target or runtime realization  
  **What it should not silently decide:** retroactively alter admitted constitutional meaning

- **Layer or construct:** Effect membrane / constitutional syscall  
  **Primary responsibility:** adjudicate an attempted authority crossing at the moment of effect  
  **What it should not silently decide:** infer authority from procedural reachability

- **Layer or construct:** ReceiptLog or equivalent  
  **Primary responsibility:** retain evidence about decisions and effects  
  **What it should not silently decide:** prove truth, legitimacy, or semantic equivalence by existence alone

This table is a proposed responsibility allocation, not an author-adjudicated ontology. Two source families currently conflict:

1. The GCML source orders `MCIR -> MCIR-Law -> GCML -> Machine Code`.
2. GSOL v0.1 orders   
`GCNL -> GSOL -> GCML -> MCIR / AI-HLIR /`

` PEIR / CEIR / Jnana-facing IRs` and also allows GSOL to lower directly to several of those targets [GSOL, Sections 2 and 33].

The present candidate adopts the first placement provisionally because it gives GCML a testable role: a **post-admission, pre-target procedural contract**. It then inserts PEIR between GCML and machine code whenever PEIR is the execution-ready representation:

```text
GCNL or other governed front end
        |
        v
GSOL operation semantics
        |
        v
MCIR canonical commitments
        |
        v
MCIR-Law admission / refusal / conditions
        |
        v
GCML target-neutral procedural contract
        |
        v
PEIR or another declared execution IR
        |
        v
target code and runtime
        |
        v
effect membrane / constitutional syscalls
        |
        v
receipts and observed consequences
```

If PEIR already carries every GCML field and invariant, GCML is better treated as a PEIR governance profile or a named lowering contract rather than an independent foundational language. A separate GCML identity is justified only by a demonstrable representational or verification capability not already supplied by GSOL, MCIR, PEIR, and their translation-edge contracts.

## 3. Definition and Nonclaims

**Governed Controlled Machine Language (GCML)** is provisionally defined as:

> A canonical, target-neutral procedural representation that binds an admitted semantic operation to an explicit dependency graph, capability budget, effect interface, resource and nondeterminism assumptions, refusal paths, receipt obligations, and lowering proof obligations before execution-ready or machine-specific emission.

GCML is **governed** because every plan is bound to source authority, admission conditions, effect jurisdiction, and evidence obligations. It is **controlled** because its grammar and procedural forms are bounded enough for deterministic validation under a declared profile. It is **machine-facing** because its objects are procedural rather than discursive. It is a **language** only if it has a defined abstract syntax, static semantics, canonicalization, validation, and transformation contract.

GCML does not by definition provide:

* a production compiler or runtime;
* general-purpose source programming;
* semantic admission or policy sovereignty;
* actual effect authority;
* deterministic replay across uncontrolled external state;
* proof that two hardware targets are behaviorally or semantically equivalent;
* proof that a receipt is truthful;
* a new foundational layer merely because it has a name.

## 4. Artifact Model

A GCML artifact $P$ is represented as:

$$
P = \langle i, s, a, O, E_d, C, X, R, N, Q, L, V \rangle,
\tag{1}
$$

where:

* $i$ is the canonical plan identity;
* $s$ binds the exact semantic source, version, and meaning hash;
* $a$ binds the admission decision, authority, conditions, and expiry;
* $O$ is the set of procedural operations;
* $E_d$ is the dependency and ordering relation over operations;
* $C$ is the maximum capability budget;
* $X$ is the set of declared effect requests and membrane contracts;
* $R$ is the set of refusal, rollback, and recovery branches;
* $N$ declares nondeterminism, clocks, randomness, concurrency, and external inputs;
* $Q$ declares resource assumptions and bounds;
* $L$ is the lowering contract and target-feature requirement set;
* $V$ is the verification and receipt obligation set.

An operation node contains at least:

```text
operation_id
operation_semantics_ref
inputs and typed outputs
preconditions
required capabilities
possible effect requests
dependency predecessors
failure and refusal successors
resource and timing assumptions
nondeterminism sources
receipt obligations
claim and nonclaim carry-forward
```

The graph does not itself grant a capability or effect. It states what would be required if the plan is admitted for realization. Effect authority remains at the applicable membrane or syscall boundary.

## 5. Procedural Preservation Invariants

A valid GCML profile should enforce at least the following proposed invariants.

1. **Exact source binding.** The plan identifies the exact GSOL/MCIR source and applicable admission result; a plan cannot float free of the meaning it claims to realize.
2. **Authority non-expansion.** No operation, optimizer, backend, or runtime may acquire authority absent from the source contract and admission conditions.
3. **Capability monotonicity.** The required capability set of every lowering is a subset of, or explicitly authorized refinement within, the admitted capability budget.
4. **Effect completeness.** Every path capable of external effect reaches a declared membrane or syscall contract; ambient effect paths are invalid.
5. **Refusal preservation.** A source refusal, condition, nonclaim, or required hold cannot be optimized away.
6. **Dependency closure.** Every executed operation has its declared predecessors satisfied, refused, or explicitly bypassed under an authorized rule.
7. **Nondeterminism declaration.** Randomness, time, concurrency, scheduling freedom, external inputs, and implementation-defined behavior are explicit.
8. **Resource honesty.** Memory, compute, storage, bandwidth, and latency assumptions material to admissibility or behavior are declared rather than hidden in a backend.
9. **Lowering conservation.** Target lowering preserves required authority, capability, effect, refusal, receipt, claim, nonclaim, standing, and temporal obligations or emits a typed gap.
10. **Receipt obligation.** Decisions and effects produce the evidence required by the plan without converting evidence existence into proof of correctness.
11. **Compiler non-sovereignty.** A compiler may select among admitted procedural alternatives but cannot amend the governing contract by successful emission.
12. **Revision lineage.** Changes to source, law, plan, target profile, optimizer, runtime, or membrane produce a successor relation rather than silent replacement.

These are profile obligations pending author and implementation review. They do not establish that a complete validator exists.

## 6. Lowering and Refusal Semantics

Let $M$ be an admitted semantic artifact, $\rho$ its admission receipt and conditions, and $\tau$ a declared procedural profile. GCML construction is a partial transformation:

$$
\mathcal{G}(M,\rho,\tau)
\rightarrow
P \;|\; \operatorname{Gap}(g) \;|\; \operatorname{Refusal}(f).
\tag{2}
$$

A plan may be emitted only when the semantic source is admitted and a procedural realization exists that satisfies the preservation invariants:

$$
\begin{aligned}
&\operatorname{EmitGCML}(P) \\
&\Rightarrow \operatorname{Admitted}(M,\rho) \\
&\land \operatorname{Realizes}(P,M) \\
&\land \bigwedge_{k \in K} k(P)
\end{aligned}\tag{3}.
$$

The implication is one-way. Passing a GCML validator does not prove the originating meaning true, the policy legitimate, or the eventual runtime faithful. It establishes conformance only to the declared GCML profile and verified inputs.

Lowering from GCML to target representation $T$ returns a target artifact, a gap certificate, or refusal:

$$
\mathcal{L}(P,T)
\rightarrow
A_T \;|\; \operatorname{Gap}(g_T) \;|\; \operatorname{Refusal}(f_T).
\tag{4}
$$

Silent semantic loss is forbidden. An unsupported target feature, unrepresentable refusal branch, widened capability, unavailable evidence mechanism, or unresolved nondeterminism must produce a gap or refusal rather than an apparently successful target artifact.

## 7. Constitutional Syscalls and Effect Membranes

A GCML effect node is a proposal to cross an authority boundary, not a direct grant of effect. It references a constitutional syscall or equivalent membrane contract containing:

```text
effect class and requested operation
target jurisdiction and resource
required authority and warrant
argument and disclosure schema
preconditions and policy head
possible execute, simulate, defer, refuse, or fail outcomes
required evidence and receipt class
rollback or compensation obligations
```

At runtime, the membrane re-evaluates current authority, policy, time, state, and revocation. A plan admitted yesterday may be refused today. GCML therefore carries effect requirements forward without claiming that precompilation can authorize every future crossing.

## 8. Replay, Reproducibility, and Evidence

The source paper states that GCML supports deterministic replay. That claim requires qualification. Three replay levels should remain distinct:

1. **Plan replay:** canonical parsing and validation recover the same procedural graph from the same exact artifact and profile.
2. **Pure-step replay:** deterministic operations over frozen inputs and declared runtime semantics reproduce the same outputs.
3. **Effect replay:** prior effect outcomes are simulated or re-presented from receipts without pretending that the external world has been reproduced.

Live re-execution against clocks, networks, devices, mutable services, people, random sources, concurrent schedulers, or changed policy may legitimately differ or refuse. A receipt can bind what was observed, not guarantee that the observation was complete or truthful.

Reproducible target emission additionally requires exact compiler, optimizer, target profile, environment, dependencies, and canonicalization. Byte-identical output is stronger than semantic conformance in one way and weaker in another: different bytes may validly realize one contract, while identical bytes do not prove the contract was legitimate.

## 9. Worked Example: Governed Report Generation

Consider an admitted operation that reads an authorized dataset, computes a bounded aggregate, writes a report, and records evidence. Its semantic contract prohibits row-level disclosure and external network effects.

A compact GCML-like projection might be:

```yaml
plan: report.aggregate.v1
source:
  semantic_hash: m:example
  admission_receipt: r:example
capability_budget:
  - read:dataset:authorized-view
  - compute:aggregate:count-and-mean
  - write:report:local-output
effects:
  - id: write-report
    syscall: file.write.constitutional
    target: local-output/report.json
    outcomes: [execute, simulate, defer, refuse, fail]
operations:
  - id: load-view
    inputs: [authorized-view]
    output: bounded-record-stream
    forbids: [raw-row-export, network]
  - id: aggregate
    after: [load-view]
    output: aggregate-only
  - id: emit-report
    after: [aggregate]
    effect: write-report
refusal:
  - if: view-not-authorized
    code: AUTHORITY_REQUIRED
  - if: backend-requires-network
    code: CAPABILITY_EXPANSION_REFUSED
receipts:
  - admission-decision
  - aggregate-input-commitment
  - effect-decision
  - output-artifact-hash
nonclaims:
  - aggregate-is-correct-without-independent-check
  - receipt-proves-source-truth
```

A backend that attempts cloud execution because local memory is insufficient cannot silently add network capability. It must select an admitted local alternative, produce a capability-expansion gap, or refuse. A backend may optimize the aggregation loop, but it may not introduce raw-row output or delete the effect refusal branch.

This example is a specification fixture. No parser, validator, lowering engine, dataset, or runtime execution is supplied by the paper.

## 10. Conformance and Test Program

A GCML implementation claim requires more than a parser or serializer. A bounded conformance profile should verify:

* canonical parse and serialization;
* schema and type validity;
* exact semantic-source and admission binding;
* dependency acyclicity or explicitly typed cycles;
* capability containment on every path;
* complete effect routing through declared membranes;
* refusal and nonclaim preservation;
* nondeterminism and resource declarations;
* lowering conservation or typed gaps;
* receipt obligations and external receipt custody;
* target-profile and compiler identity;
* successor lineage after any material change.

Negative fixtures should include hidden effect paths, widened capability, missing refusal, stale admission, revoked authority, unsupported target feature, nondeterministic operation without declaration, resource fallback across jurisdiction, forged or missing receipt, optimizer removal of evidence, and a compiler that emits code despite a gap.

Cross-target tests should compare obligations and allowed observable behavior, not presume byte identity. Independent observers should verify at least some effect and evidence claims outside the compiled process.

## 11. Realization Funnel

| Stage | GCML responsibility |
|---|---|
| Possibility | Explore ways admitted meaning might become procedure, including unsafe, overpowered, nondeterministic, unverifiable, and target-dependent possibilities. |
| Specification | Define GCML syntax, static semantics, artifact schema, preservation invariants, gaps, refusal, canonicalization, conformance, and layer boundaries. |
| CM1 | Enumerate procedural plans satisfying the specification, including inefficient, privacy-invasive, highly centralized, brittle, and otherwise undesirable admissible plans. |
| CM2 | Prefer plans minimizing capability and effect surface, preserving refusals and evidence, bounding resources and nondeterminism, supporting substitution, and avoiding unjustified target dependence. |
| Instance Configuration | Select the exact admitted source, law head, GCML profile, plan, target class, compiler, optimizer, runtime, membrane, resources, observers, and evidence obligations. |
| Implementation Realization | Build and run the parser, validator, planner, lowerer, PEIR or target artifact, runtime, membrane adapters, and receipt path for that configuration. |
| Evidence | Execute positive, negative, adversarial, cross-target, stale-authority, revocation, replay, effect, and independent-observer tests; retain gaps and unexplained remainder. |
| Revision | Create successors when schemas, obligations, plans, compilers, targets, policies, or evidence change; preserve predecessor hashes, migrations, incompatibilities, and failed claims. |

The source paper primarily proposes a Specification and sketches Implementation Realization. The present candidate adds CM1/CM2 criteria and an evidence program, but it does not supply an implementation.

## Procedural Preservation Profile

Across the completed P1 corpus, Governed Controlled Machine Language is best retained provisionally as the **procedural preservation profile between admitted constitutional meaning and target-specific execution**. It must show what procedural structure it preserves beyond MCIR, GSOL, and direct PEIR lowering before it earns a distinct language or system identity.

- **Adjacent work:** *Human Legible Intermediate Representation*  
  **Supplies:** Constitutional authoring surfaces and deterministic lowering into canonical representation.  
  **GCML boundary:** GCML begins after semantic admission and expresses governed procedure rather than human authoring intent.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Stage contracts, preservation, remainder, refusal, authority, and evidence.  
  **GCML boundary:** GCML is one candidate procedural stage/profile inside that larger theory.

- **Adjacent work:** *The Ableman Format Specification (AFS)*  
  **Supplies:** Artifact roles, profiles, canonical encodings, validators, and test vectors.  
  **GCML boundary:** AFS can standardize GCML artifacts but does not supply their procedural semantics.

- **Adjacent work:** *Semantic Fragmentation and Constitutional Structure*  
  **Supplies:** Detection of authority, state, or evidence split across incoherent software surfaces.  
  **GCML boundary:** GCML should make those bindings explicit before backend emission.

- **Adjacent work:** *The Mechanics of Constitutional Enforcement*  
  **Supplies:** Non-bypassable effect gates and classified outcomes.  
  **GCML boundary:** GCML can require gate participation but cannot prove a runtime is non-bypassable.

A GCML artifact should preserve a procedural obligation vector:

$$
\begin{aligned}
O_p= (&authority, capabilities, resources, dependencies, \\
&preconditions, effects, refusals, nondeterminism, \\
&recovery, observation, receipts, remainder)
\end{aligned}.
$$

For each lowering edge $f:L_i\rightarrow L_{i+1}$, the relevant claim is not textual similarity but obligation carriage:

$$
carry_f(O_p)=PRESERVED\mid REFINED\mid DEFERRED\mid REFUSED\mid GAP.
$$

`DEFERRED` must bind the named downstream mechanism that assumes the obligation;

`GAP` cannot compile as success. A target runtime may still violate a perfectly formed GCML artifact, so language conformance, compiler conformance, runtime conformance, and observed effect correctness remain separate.

The universal GSM can type   
`EXPRESSES_GOVERNED_PROCEDURE`, `LOWERS_FROM_ADMITTED_MCIR`,  
`CARRIES_PROCEDURAL_OBLIGATION`, `DEFERS_OBLIGATION_TO_EFFECT_GATE`, `EMITS_PEIR`,  
`REFUSES_UNBOUND_CAPABILITY`, `CLASSIFIES_NONDETERMINISM`, `BINDS_RECOVERY_SEMANTICS`,  
`REPORTS_LOWERING_GAP`,  
and   
`REMAINS_IDENTITY_UNRESOLVED_AGAINST_EXISTING_`  
`IRS`. These relations make the comparison experimentally decidable rather than terminological.

This integration establishes four editorial commitments: retain GCML provisionally as a procedural preservation profile; adopt the procedural-obligation vector and five-valued carriage result; require separate language, compiler, runtime, and effect claims; and defer distinct-language identity until a worked comparison demonstrates information or assurance not preserved by direct MCIR/GSOL-to-PEIR lowering.

## Procedural Obligation Handoff

The fixed-seed comparison with communal computing, APD, Semantic Legitimacy Before Context, and enforcement mechanics makes deferred procedural obligations auditable:

$$
\begin{aligned}
H= (&obligation, source\_standing, GCML\_carrier, \\
&target\_mechanism, coverage, authority, evidence, status, \\
&remainder)
\end{aligned}.
$$

SLBC determines whether source material may bind for the stated purpose. Admission does not itself create a procedure, and effect eligibility remains distinct from effect authority. GCML must preserve the source standing and purpose so that lowering cannot widen a narrowly admitted claim into a general operational rule.

For `DEFERRED`, the artifact must name the mediator, court, syscall, runtime monitor, recovery mechanism, or other component that becomes load-bearing. The Mechanics of Constitutional Enforcement supplies placement and mediation tests; APD supplies the bounded effect-containment objective. A target name or interface declaration is not evidence that the mechanism is non-bypassable or covers the relevant effect.

Communal computing is a domain profile in which admitted civic procedures may be made inspectable and lowered for execution. Procedural conformance cannot establish participant legitimacy, consent, privacy adequacy, jurisdiction, or social acceptance, and should preserve dissent and appeal paths as explicit obligations or remainder.

The universal GSM can type   
`CARRIES_ADMITTED_SOURCE_STANDING`,  
`DEFERS_OBLIGATION_TO_NAMED_MECHANISM`, `TESTS_HANDOFF_COVERAGE`,  
`WIDENS_PURPOSE_DURING_LOWERING`, `ENFORCED_BY_RUNTIME_MEDIATOR`,  
`CONTAINED_UNDER_APD_SURFACE`, and   
`PRESERVES_CIVIC_DISSENT_OBLIGATION`.

This randomized review establishes four editorial commitments: adopt the obligation-handoff record; require source standing and purpose to survive lowering; make every deferred obligation name and evidence its downstream mechanism; and keep civic procedure conformance below legitimacy, consent, and authority.

## A Procedural Obligation-Carriage Profile

Thirteen retained downstream uses place GCML between admitted meaning, capability requests, shared-reality procedures, governed object and operation records, term identities, compilation stages, controlled natural language, semantic cartography, human-legible representations, Jnana, semantic legitimacy, enforcement, and APD-bounded computation. The resulting role is narrower and stronger than a universal machine language: GCML is a candidate procedural obligation-carriage profile whose nonredundancy against MCIR, GSOL, and PEIR remains to be demonstrated.

$$
\begin{aligned}
G^*= (&source\_semantics, admission, operation\_graph, \\
&obligations, capabilities, resources, nondeterminism, \\
&effects, refusals, exceptions, recovery, observers, \\
&receipts, target\_profile, lowering, remainder, version)
\end{aligned}.
$$

Every lowering edge must classify each obligation as `PRESERVED`, `REFINED`, `DEFERRED`,  
`REFUSED`,  
or `GAP`. `DEFERRED` names the exact downstream mechanism and its evidence; `GAP` cannot compile as success. Canonicalization must retain alternative plans and residual meaning where plan choice is constitutionally material. Capability minimization, effect mediation, replayability, and receipt production are separate claims, not consequences of a well-formed artifact.

Four conformance subjects remain distinct: language artifact, compiler or lowerer, target runtime, and observed effect path. A conforming artifact can be compiled maliciously; a conforming compiler can target a bypassable runtime; a governed runtime can be invoked under stale authority. In the realization funnel, `IR` may mean Instance Realization or Implementation Realization. In PEIR, MCIR, and comparable representation names,

`IR` means Intermediate Representation; the two acronym senses must not be merged.

The universal GSM can type   
`CONFORMS_TO_GCML_PROFILE`, `CARRIES_PROCEDURAL_OBLIGATION`,  
`DEFERS_TO_NAMED_MECHANISM`, `REPORTS_PROCEDURAL_GAP`, `LOWERS_UNDER_TARGET_PROFILE`,  
`PRESERVES_PLAN_ALTERNATIVE`, `MEDIATES_GCML_EFFECT`, and   
`OBSERVES_GCML_OUTCOME`.

This review establishes four editorial commitments: retain GCML as a candidate procedural obligation-carriage profile; adopt the complete procedure record and five-valued carriage result; separate artifact, compiler, runtime, and effect conformance; and require a worked nonredundancy comparison before granting a distinct language or system identity.

## 12. Failure Modes and Counterevidence

GCML should be compressed into existing machinery or rejected as a separate layer if:

* PEIR already expresses and validates every proposed GCML field and invariant;
* GSOL lowering contracts plus MCIR sidecars preserve the same obligations without another artifact;
* the proposed target-neutral plan cannot remain independent of backend and runtime semantics;
* capability and effect guarantees cannot be checked compositionally;
* optimizations require proofs or analyses GCML cannot express;
* canonicalization hides meaningful procedural alternatives;
* plan size and verification cost exceed audit or safety benefit;
* receipts remain dependent on the process they claim to audit;
* real systems bypass the artifact through ambient runtime authority;
* cross-target conformance cannot be distinguished from superficial structural similarity;
* replay failures dominate practical workloads;
* implementation teams cannot maintain source, plan, target, and evidence lineage without drift.

Security failure modes include malicious compilers, forged admission receipts, stale policy heads, confused-deputy syscalls, capability aliasing, hidden dynamic loading, undefined behavior, side channels, self-modifying code, opaque accelerators, dependency substitution, and observers sharing the same compromised root.

The source comparison with LLVM IR, WebAssembly, microkernel capabilities, and replay systems remains a hypothesis surface, not a literature finding. Further evidentiary strengthening requires current primary-source research and concrete feature-by-feature comparison before claiming that those systems lack relevant governance, authority, effect, portability, or audit mechanisms.

## 13. Corpus Integration

GCML connects existing corpus machinery through a proposed procedural profile:

* **GCNL** stabilizes governed natural-language proposals before canonical operation semantics [GCNL].
* **GSOL** defines the semantic operation, jurisdiction, authority, effects, refusals, receipts, claims, nonclaims, standing, time, and honest-lowering obligations that GCML must preserve [GSOL].
* **MCIR** carries canonical semantic and constitutional commitments; **MCIR-Law** provides the admission decision and conditions that bind a post-admission plan [MCIR].
* **PEIR** is the closest existing execution-layer comparison. The boundary between GCML and PEIR is unresolved and must be demonstrated rather than named [HLIR].
* **Constitutional Syscalls** and **Effect Sovereignty** enforce present-time jurisdiction at external crossings; GCML records required call sites but does not grant them [CS].
* **Constraint-Bearing Composability** requires obligations to survive module and plan composition; a GCML linker or composer would be a profile of that machinery unless it adds a distinct algorithm or assurance claim [CBC].
* **Reasoning by Way of Receipts** separates evidence-bearing intermediate decisions from final-result narration while denying that receipts prove truth [RWR].
* **The Three Hash Rule** separates exact artifact state, admissibility commitments, and meaning commitments across the source-plan-target chain [THR].
* **The Constitutional Observability Platform** supplies heterogeneous observation and result-visibility surfaces for comparing declared GCML behavior with runtime effects [COP].
* **Semantic Fragmentation Analysis** can diagnose where authority, lowering, fallback, target behavior, or receipts remain ambient despite a GCML declaration [SFA].
* **GMB**, the current Governed Meaning Base in the historical `CCF -> CMB -> GMB` lineage, can retain definitions, obligations, conflicts, evidence, and revision lineage. It is not the procedural runtime and does not grant GCML conformance [GMB].

This integration does not merge GCML with any neighbor. It identifies the comparisons that must be resolved before the architecture can claim a nonredundant layer.

## A Governed Label Does Not Make a Procedure Lawful

### Public orientation

GCML addresses the gap between admitting an operation in principle and selecting the concrete procedure that will perform it. A target-neutral plan can expose capabilities, resources, nondeterminism, refusals, exceptions, effects, recovery, and receipt obligations before machine emission. The unresolved question is whether GCML is a distinct language or a profile already expressible through GSOL, MCIR, PEIR, and constraint-carriage machinery.

### Adversarial tests

1. **Redundancy attack.** Existing GSOL-to-PEIR lowering plus MCIR obligations expresses every GCML field and check. A new name then increases stack complexity without new assurance.
2. **Target-neutrality attack.** Backend-specific concurrency, memory, exception, timing, resource, or effect semantics determine the plan despite claims of neutrality.
3. **Malicious-compiler attack.** A conforming artifact is lowered by a compiler that drops, widens, or fabricates obligations.
4. **Bypass-runtime attack.** The target runtime retains ambient authority, dynamic loading, undefined behavior, side channels, opaque acceleration, or direct effect paths outside GCML.
5. **Canonical-plan attack.** One normalized procedure erases materially different plans, resource costs, risks, or refusal behaviors.
6. **Deferred-obligation attack.** `DEFERRED` becomes a way to report success while no named downstream mechanism actually discharges the obligation.
7. **Conformance-collapse attack.** Artifact, compiler, runtime, effect path, and observed outcome are combined into one green status.
8. **Replay-overclaim attack.** Reproducible plan or target bytes are treated as reproducible behavior despite external state, nondeterminism, hardware, time, and services.

### Claim and evidence ceiling

The strongest current claim is a candidate procedural obligation-carriage profile with five-valued lowering disposition: preserved, refined, deferred, refused, or gap. The paper does not establish a nonredundant language identity, target neutrality, secure compilation, complete capability mediation, deterministic execution, or cross-target equivalence.

Distinct GCML standing requires a worked feature-by-feature comparison with GSOL, MCIR, PEIR, and existing constraint-carriage contracts, followed by negative fixtures and at least one exact lowering and runtime observation. Claims about LLVM, WebAssembly, microkernels, proof-carrying code, effect systems, or reproducible execution require current primary-source research. No external research was added in this pass.

### Reader-facing consequence

The public test is whether every obligation attached to an approved operation can be followed through the chosen plan, compiler, runtime, external effect, and receipt - with any missing handoff reported as a gap rather than hidden inside successful code generation.

## 14. Research and Implementation Agenda

1. Adjudicate GCML's placement relative to GSOL, MCIR, MCIR-Law, and PEIR.
2. Define a minimal abstract syntax and static semantics for the artifact model in Section 4.
3. Specify canonicalization and exact source/admission binding.
4. Implement a validator for capability, effect, dependency, refusal, nondeterminism, resource, and receipt obligations.
5. Define one GCML-to-PEIR or GCML-to-reference-runtime lowering with typed gaps.
6. Build positive and negative fixtures, including a malicious or nonconforming backend.
7. Compare a GCML profile with direct GSOL-to-PEIR lowering on expressivity, assurance, cost, and semantic loss.
8. Test cross-target obligation preservation under exact compiler and runtime custody.
9. Evaluate independent observation, replay levels, revocation, policy change, and external-state drift.
10. Conduct current primary-source research across compiler IRs, proof-carrying code, typed effect systems, capability machines, secure compilation, reproducible builds, deterministic execution, sandboxing, policy-as-code, WebAssembly, LLVM, and microkernels.

## 15. Conclusion

GCML names a genuine governance problem: semantic admission does not guarantee that a compiler-selected procedure preserves authority, capability, refusal, evidence, and effect boundaries. The procedure itself must become inspectable and challengeable before machine emission.

The strongest current interpretation is not that GCML automatically completes a new universal stack. It is that GCML specifies a post-admission, target-neutral procedural contract whose obligations must survive into PEIR, target code, runtime effects, and receipts. That interpretation gives the proposal a testable burden.

If existing PEIR and GSOL machinery already carries the same contract, authorial compression should treat GCML as a profile, serialization, or lowering discipline. If GCML can represent and verify procedural information those layers cannot preserve, a distinct language may be warranted. The paper leaves that decision open while making the comparison concrete.

Computation does not become lawful because a plan is labeled governed. It becomes more governable when meaning, admission, procedure, target realization, effect jurisdiction, and evidence remain distinct; when translation loss becomes a gap rather than a hidden success; and when no compiler or runtime may widen authority merely because it can emit instructions.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Revision.** The present paper does not claim a complete revision treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that conventional compilation stacks translate programs through intermediate representations designed for transformation, optimization, portability, and execution. Its nearest external comparison fields are token, formal, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Statistical compression can improve efficiency while destroying distinctions needed for interpretation; semantic labels can conversely overstate stability that usage does not support. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Rico Sennrich, Barry Haddow, and Alexandra Birch. "Neural Machine Translation of Rare Words with Subword Units." *ACL 2016*, pp. 1715-1725. DOI: 10.18653/v1/P16-1162. https://doi.org/10.18653/v1/P16-1162 **Relationship:** Predecessor subword tokenization method used as a contrast to semantically governed token boundaries.

**[E2]** Taku Kudo and John Richardson. "SentencePiece: A Simple and Language Independent Subword Tokenizer and Detokenizer for Neural Text Processing." *EMNLP 2018: System Demonstrations*. DOI: 10.18653/v1/D18-2012. https://doi.org/10.18653/v1/D18-2012 **Relationship:** Predecessor tokenizer implementation used to separate statistical segmentation from semantic admissibility.

**[E3]** Peter D. Grunwald. *The Minimum Description Length Principle*. MIT Press, 2007. [mitpress.mit.edu source](https://mitpress.mit.edu/9780262072816/the-minimum-description-length-principle/) **Relationship:** Predecessor theory of compression and model selection; compression is not assumed to preserve governance or meaning.

**[E4]** Alistair Miles and Sean Bechhofer, eds. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. https://www.w3.org/TR/skos-reference **Relationship:** Adjacent standard for concepts, labels, schemes, notes, and semantic mappings.

**[E5]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E6]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E7]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

### Ableman corpus

**[A1]** Adam Ableman. *Governed Semantic Tokens: Tokenization as an Admissibility Boundary*. Ableman Corpus current edition; work identity `PAPER.PUB.18469507`;  
source SHA-256  
`5C44175B87C514892A0DC9743E09D03893E970AF5419F2E6D9171651BE2A9A54`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Token Parsimony*. Ableman Corpus current edition; work identity `PAPER.PUB.20382825`;  
source SHA-256  
`EC3AA22D32E2BBA21CFCB6D1FA2AE6EA8AC11B7781D19C51530A2F6D924B2E91`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Constitutional Legends*. Ableman Corpus current edition; work identity `PAPER.PUB.20330324`;  
source SHA-256  
`440CE8A83C2F86C020D1E9E482759F71D08F694F1C2250B5B624AEA0A4237AA7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Governed Controlled Natural Language (GCNL)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-99C179FB694070D1`;  
source SHA-256  
`75A4AE13167785A0761E1F9CB67A9975138166A7B2B06B4FDF37C1A895178193`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Global Term Key: Identity Primitives in Governed Knowledge Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-358AC09F5A13587E`;  
source SHA-256  
`AFB29CFCB4B58A78B79709AD453CEE9088CCB2AE40F30A70260F1B54F5160579`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Ableman Corpus current edition; work identity `PAPER.PUB.21095303`;  
source SHA-256  
`EA129ECBA95F7B07CAA7B33A54F91F52913C94A14DA227EB9A06CFD083E4E5BF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Semantic Compilation*. Ableman Corpus current edition; work identity `PAPER.PUB.18453681`;  
source SHA-256  
`5FF6C636550B04DB0E2F6F94C379BB75AA0BD8781E19B047D7D3BB6D49071AC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

#### Ableman Corpus references

**[GCNL]** Adam Ableman. *Governed Controlled Natural Language (GCNL)*. Corpus paper family; exact publication and version identity must be resolved before citation finalization.

**[GSOL]** Adam Ableman. *GSOL v0.1: Governed Semantic Operation Language*. Exact reviewed source:   
  `GSOL v0.1 Specification.md`,  
SHA-256  
`44F8689BF2FD50670CD25347FB2363491115CA7C049C2BBF71D7286A226DD1AC`. The source is a pre-release specification, not a production runtime.

**[MCIR]** Adam Ableman. *MCIR* and *MCIR-Law* corpus materials. The universal GSM treats MCIR as a canonical constitutional/compilation intermediate representation and MCIR-Law as an admissibility boundary; exact work/version references require registry adjudication.

**[HLIR]** Adam Ableman. *Human-Legible Intermediate Representation: Constitutional Front-Ends for Governed Semantic Systems*. Exact reviewed source:   
  `Human_Legible_Intermediate_Representation.md`,  
SHA-256  
`FE8E5245282E84E1F04E9327AEBFCCB51878F9B8C6494CE2F1C3A42743BAB888`. This source defines PEIR as the layer where canonical artifacts become executable operational structures.

**[CS]** Adam Ableman. *Constitutional Syscalls* and *Effect Sovereignty* corpus paper families; exact publication and version identities require registry resolution.

**[CBC]** Adam Ableman. *Open Constraint-Bearing Composability* and related corpus materials; schema, algorithm, and assurance identities remain separate pending author adjudication.

**[RWR]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

**[THR]** Adam Ableman. 2026. *The Three Hash Rule*. Zenodo. DOI: `10.5281/zenodo.20788617`.

**[COP]** Adam Ableman. *The Constitutional Observability Platform*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

**[SFA]** Adam Ableman. *Semantic Fragmentation and Constitutional Structure in Software Systems*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

**[GMB]** Adam Ableman. *Governed Meaning Base (GMB)*. Current corpus terminology under the author-confirmed historical lineage `CCF -> CMB -> GMB`; the terminology ruling grants no publication, implementation, conformance, or canonical standing.

External scholarly and technical sources remain to be researched and verified for a future evidence-qualified revision readiness.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Governed Semantic Operation Language.* Zenodo, 2026. doi:10.5281/zenodo.21214886

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

Adam Ableman *Semantic Coordinate Identity Tokenization (SCIT).* Zenodo, 2026. doi:10.5281/zenodo.20532070

Adam Ableman *Semantic Memory Hierarchies.* Zenodo, 2026. doi:10.5281/zenodo.20793071

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847878](https://doi.org/10.5281/zenodo.23847878)
