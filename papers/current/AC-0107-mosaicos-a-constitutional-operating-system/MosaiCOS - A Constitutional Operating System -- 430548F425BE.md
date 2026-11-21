# MosaiCOS: A Constitutional Operating System

## Constitutional OS Discipline, Configuration-Manifold Analysis, and a Proposed MosaiCOS Instance

### Kernel mechanisms become governable only when identity, authority, decision, effect, evidence, and revision remain distinguishable.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Operating systems mediate memory, process execution, storage, devices, and communication, but their security mechanisms do not automatically constitute a reviewable governance order. An access-control decision may be enforced without binding the exact subject, authority chain, policy revision, intended effect, observed outcome, and later repair route into one inspectable lineage.

This paper proposes the **Constitutional Operating System (COS)** discipline: a specification framework for operating systems whose consequential operations are attributable to stable constitutional identities, admitted under finite delegated authority, subject to typed decisions and refusals, and connected to evidence and revision through integrity-protected records. COS is not an operating system and does not prescribe one kernel architecture. It defines obligations that candidate realizations must interpret, implement, and test.

**MosaiCOS** is the paper's proposed Instance Configuration for general-purpose constitutional computing. It combines process and artifact identities, constitutional capability tokens, pre-effect decision commitments, post-effect observations, typed refusal, declared governance and bootstrap boundaries, governed sessions, hardware-effect attribution, and epoch succession. These are proposals and proof obligations, not evidence that a conforming kernel already exists.

The paper corrects three important category errors. First, a hash-linked receipt can preserve a decision record without proving that the record is truthful, complete, independently observed, or causally effective. Second, a stable program identity is not the same as a unique execution-instance identity or a continuity relation across restart. Third, a user-space governance layer on Linux or OpenWrt may be a valuable transition profile without thereby becoming a COS-conforming kernel.

The source's comparisons among Linux, seL4, Redox, Genode, and Fuchsia are therefore retained as hypotheses for a primary-source protocol-archaeology study, not as established compliance findings. The paper supplies that study design, a full Possibility-Specification-CM1-CM2-Instance Configuration-Implementation Realization-Evidence-Revision map, conformance levels, counterevidence conditions, and a bounded deployment spectrum. No implementation, conformance, novelty, or superiority claim is granted by this candidate.

## 1. The Problem: Mechanisms Without a Constitutional Account

An operating system already makes governance-like decisions. It decides which process may read a file, which principal may map a device, which packet may leave an interface, and which executable may enter memory. Conventional mechanisms can perform those decisions correctly for their threat models. The constitutional question is different:

* Which exact subject and artifact requested the operation?
* Under which authority chain and policy revision was the request evaluated?
* Which part of the system was responsible for the decision?
* Was the decision bound before the consequential effect?
* Which observer supports the claim that the effect did or did not occur?
* Which relevant paths were outside mediation or observation?
* How can a refusal, debt, exception, or later revision be contested and repaired?

Access control, capabilities, isolation, logging, measured boot, and formal verification can each answer part of this account. None should be dismissed merely because it uses a different vocabulary. COS asks whether the parts compose into an inspectable relation among specification, configuration, realization, evidence, and revision.

The paper's central thesis is therefore narrower than "existing operating systems do not govern." Existing systems implement many forms of policy and institutional control. The thesis is:

> A constitutional operating system must make the authority and meaning of consequential kernel decisions inspectable without treating security mechanisms, audit records, or cryptographic integrity as sufficient evidence of the whole governance claim.

This formulation allows comparison without defining every difference as failure. It also places a burden on COS: if a simpler combination of capabilities, audit, attestation, and independent observation provides equivalent accountability at lower cost, the stronger architecture is not justified merely by its terminology.

## 2. Discipline, Instance, Realization, and Evidence

Four objects must remain distinct.

1. **COS discipline** is a specification-level set of constitutional obligations.
2. **MosaiCOS Instance Configuration** is one proposed selection among admissible configurations.
3. **MosaiCOS realization** is an exact implementation artifact, environment, and deployment that claims to realize that configuration.
4. **MosaiCOS evidence state** is the bounded record supporting or contradicting particular claims about that realization.

The relation is not identity:

$$
\operatorname{COSSpec}
\not\equiv
\operatorname{MosaiCOSIC}
\not\equiv
\operatorname{Implementation}
\not\equiv
\operatorname{Evidence}.
$$

A specification can be coherent while no implementation conforms. An implementation can execute while violating its specification. A receipt chain can be internally valid while failing to observe a bypass. Evidence can support one claim without supporting the system as a whole.

The source corpus also contains **MosaicOS** and **MosaiCOS** system codices and release candidates. Lexical similarity and shared source trees do not settle whether every named artifact is the same logical system, a renamed lineage, a profile, or a distinct project. This paper preserves that identity question for author adjudication rather than silently merging those records.

## 3. The Inherited Operating-System Floor

COS is additive. A claimed realization must first provide or explicitly delegate the ordinary substrate needed for its declared scope: memory protection where multiple protection domains exist, scheduling, persistent storage where promised, device I/O, lifecycle control, inter-process or inter-component communication, and network transport where offered.

COS does not require one scheduling policy, file system, language, or microkernel. It governs the constitutional obligations attached to those mechanisms. A capability model can be inherited; the COS question is how capability identity, delegation, revocation, exercise, and evidence are bound. A measured boot chain can be inherited; the COS question is which claim it supports, which components remain outside measurement, and how succession is governed.

This separation prevents two opposite errors:

* **mechanism laundering:** treating the presence of a security primitive as proof of constitutional governance; and
* **constitutional laundering:** describing a policy layer in constitutional language while the consequential substrate remains outside its mediation and evidence boundary.

## 4. Identity Is a Typed Family, Not One Hash

The source proposed one Process Mosaic ID derived from a genesis artifact and spawning authority chain. That formula is useful for lineage but insufficient as unique process-instance identity: two concurrent instances of the same artifact under the same authority would collide, and a digest alone does not prove possession, liveness, or authorized succession.

COS therefore distinguishes at least four identities:

* **artifact identity** commits to exact program or plan bytes and relevant build representation;
* **constitutional profile identity** commits to the policy, configuration, capability schema, and semantic regime under which the artifact is admitted;
* **execution-instance identity** distinguishes one spawn or activation from another; and
* **continuity identity** relates predecessor and successor instances across restart, migration, checkpoint, or epoch transition.

One possible typed construction is:

$$
A = H(\operatorname{artifact} \parallel \operatorname{representation}),
$$

$$
P = H(A \parallel \operatorname{constitution} \parallel \operatorname{configuration}),
$$

$$
I = H(P \parallel \operatorname{spawnReceipt} \parallel \operatorname{instanceNonce} \parallel \operatorname{instanceKey}),
$$

with continuity expressed by an authorized relation

$$
I_{n} \xrightarrow{\operatorname{successionReceipt}} I_{n+1}.
$$

These formulas are candidate schemas, not a cryptographic protocol specification. Canonical serialization, domain separation, key lifecycle, nonce generation, replay resistance, privacy, collision assumptions, recovery, and revocation must be selected and tested at Instance Configuration and Implementation Realization.

## 5. The Nine COS Invariants

The following invariants are retained as the proposed COS specification. A profile that omits one may still be useful, but it must call itself partial rather than silently redefining full conformance.

### COS-S-01: Constitutional Attribution

Every consequential kernel-mediated operation is attributable to an exact execution instance, artifact and profile lineage, presented authority, governing rule set, request identity, and declared semantic operation. Attribution does not imply moral legitimacy or factual truth. It makes the claim reviewable.

### COS-S-02: Typed Constitutional Identity

Artifact, constitutional profile, execution instance, and continuity relations are distinct, integrity-protected, and resistant to accidental aliasing across domains. Runtime topology identifiers such as PID may remain useful implementation handles but must not be mistaken for the constitutional identity.

### COS-S-03: Finite, Delegated, and Revocable Authority

Consequential operations require authority that is finite in resource, operation, scope, time, delegation depth, and consequence class. Delegation and revocation are explicit. Bootstrap and recovery authority are not magically authority-free; they are declared exceptions with bounded custody and evidence obligations.

### COS-S-04: Pre-Effect Decision Commitment and Post-Effect Reconciliation

Before a consequential effect, the system commits to the request identity, decision, authority, policy and configuration revision, intended effect, and predecessor record. After execution, an observer appropriate to the claim records completion, refusal, failure, uncertainty, or absence of observation.

Let $D$ be a decision record and $O$ an outcome observation:

$$
D = H(r, I, a, p, c, d, e, D_{prev}),
$$

$$
O = H(D, o, m, y, t, O_{prev}),
$$

where $r$ is request identity, $I$ is instance identity, $a$ is authority, $p$ is policy, $c$ is configuration, $d$ is disposition, $e$ is intended effect, $o$ is observer identity, $m$ is observation method, $y$ is observed outcome, and $t$ is time evidence.

Integrity of $D$ shows that the committed record has not changed under the hash and custody assumptions. It does not prove that the evaluator was correct, the clock was sound, the effect occurred, the observer was independent, or every path was covered. Those are separate claims.

### COS-S-05: Typed Refusal, Hold, and Failure

A negative result identifies the layer at which continuation became inadmissible or unsupported. The full realization funnel provides a richer taxonomy than the source's compact S/C/I labels:

* `SPECIFICATION_REFUSAL`: the requested semantics contradict the declared domain rules;
* `CM1_EXCLUSION`: the candidate configuration is not admissible under the specification;
* `CM2_NONPREFERENCE`: admissible but rejected by the selected preference constitution;
* `INSTANCE_CONFIGURATION_REFUSAL`: excluded by this concrete configuration;
* `IMPLEMENTATION_UNAVAILABLE`: admitted and configured but not implemented;
* `IMPLEMENTATION_FAILURE`: attempted realization failed;
* `EVIDENCE_HOLD`: the effect or required assurance cannot yet be established;
* `AUTHORITY_REFUSAL`: the subject lacks eligible authority for this request.

A deployment may encode these into a smaller wire taxonomy, but it must preserve the distinction needed for remediation.

### COS-S-06: Declared Governance and Coverage Boundary

The realization declares which operations, devices, services, recovery paths, interrupts, direct-memory-access paths, privileged tools, and external components it governs. It also declares what it does not govern. Conformance claims must name the discovered capability surface and the unmediated or unobserved remainder.

### COS-S-07: Governed Constitutional Sessions

For exchanges within the claimed governance scope, communicating instances establish a session that binds peer identities, protocol and semantic versions, negotiated capabilities, authority, transcript commitments, expiry, and termination. Not every byte requires a separate constitutional ceremony; the session defines which subsequent operations inherit which bounded standing.

### COS-S-08: Hardware-Effect Attribution

Hardware effects within scope are tied to an admitted request, delegated authority, device or resource identity, decision record, and outcome observation. The observer and method must match the claim. A software receipt cannot alone prove a physical GPIO transition, radio transmission, DMA boundary, or user-visible display.

### COS-S-09: Bootstrap and Succession Declaration

The pre-governance bootstrap surface, initial authority, recovery path, update mechanism, rollback conditions, and epoch succession rules are declared and committed. No system can produce a governed receipt before the machinery required to produce that receipt exists. The honest obligation is to minimize and expose the predecessor trust boundary, then reconcile it from the first governed state.

## 6. The Universal Realization Funnel

The original source compressed specification, configuration, and implementation into S/C/I. The universal GSM makes the choices and failure points more precise:

| Stage | COS responsibility |
|---|---|
| Possibility | Explore operating-system governance regimes, including undesirable, infeasible, or nonconstitutional possibilities. |
| Specification | Define the nine obligations, identity domains, consequence classes, claim ceilings, and conformance vocabulary. |
| CM1 | Enumerate configurations that satisfy the bare obligations. A point that uses ambient unlimited authority or omits evidence is outside CM1 unless the specification explicitly permits it. |
| CM2 | Prefer configurations by security, sovereignty, inspectability, availability, performance, privacy, portability, recoverability, and cost. Preference requires a declared constitution; it is not implied by admissibility. |
| Instance Configuration | Select concrete algorithms, schemas, kernel architecture, capability representation, storage, observers, hardware targets, update rules, and deployment profile. |
| Implementation Realization | Produce exact source, build graph, binary or plan, boot image, runtime environment, configuration, and deployment state. |
| Evidence | Test mediation coverage, identity, authority, decision ordering, physical and software effects, refusal typing, bypass, crash recovery, performance, privacy, and negative controls. |
| Revision | Change the specification, preference constitution, instance configuration, implementation, or evidence claims while preserving predecessor identity, debt, migration, and rollback. |

The nine design dimensions in the source - capability, identity, receipts, syscall governance, sessions, hardware mediation, execution substrate, bootstrap, and epoch governance - are useful axes, but their option lists mix admissible and inadmissible points. Ambient authority and absent receipts belong in the wider Possibility space when they contradict the COS specification. CM1 begins only after the invariant filter.

## 7. Protocol Archaeology as a Research Program

The source compares Linux, seL4, Redox, Genode, and Fuchsia. Those comparisons are valuable orientation, but this version-family head contains no current primary-source citations, exact versions, test artifacts, or reproducible scoring method. The matrix must therefore be treated as a hypothesis register.

### 7.1 Comparison Contract

For each target, a defensible review should bind:

* exact project, release, source revision, architecture, and configuration;
* the native identity, capability, IPC, driver, boot, audit, update, and recovery models;
* the semantic correspondence between native mechanisms and each COS invariant;
* evidence for `SATISFIED`, `PARTIAL`, `NOT_SATISFIED`, `UNKNOWN`, or `NOT_APPLICABLE`;
* whether the gap is an additive adapter, pervasive augmentation, architectural replacement, or unresolved question;
* performance, availability, security, and governance costs of the proposed change;
* an independent reviewer and reproducible evidence package.

### 7.2 Current Hypotheses, Not Findings

The source advances the following hypotheses for later testing:

1. Pre-effect governance-decision commitments coupled to post-effect reconciliation are not a general kernel property of the selected comparison systems.
2. Capability-oriented and component-oriented designs such as seL4, Genode, and Fuchsia may have smaller structural adaptation gaps than conventional monolithic designs.
3. Linux's pervasive PID use and ambient privileged paths make deep constitutional attribution expensive.
4. A Rust or formally constrained substrate may reduce some implementation risks but does not itself provide constitutional governance.
5. A clean-slate or constitution-first design may produce a more coherent obligation surface than incremental retrofit.

These remain falsifiable. In particular, Linux may support a constitutional identity plane without replacing every internal PID use; a mediated overlay may cover the declared effects; or an existing microkernel plus a small verified adapter may outperform a new kernel. The phrase "cannot be augmented" is therefore too strong until an explicit impossibility argument rules out such profiles.

External research is deliberately not performed in this revision pass. A current primary-source review is a publication blocker.

## 8. MosaiCOS as a Proposed Instance Configuration

The paper proposes the following CM2 preferences: finite authority over ambient privilege, typed identities over overloaded identifiers, declared mediation over implicit coverage, pre-effect decision binding over post-hoc reconstruction alone, independent observations over self-report alone, user-space drivers where their isolation benefit exceeds cost, memory-safe or semantically constrained implementation substrates, explicit bootstrap custody, and receipted succession.

From those preferences, a candidate MosaiCOS Instance Configuration follows.

### 8.1 Candidate Dimension Selections

1. **Capability model:** signed, domain-separated, canonically serialized capability objects with explicit grantor, grantee, resource, operation, scope, delegation, expiry, revocation, and consequence class.
2. **Identity model:** separate artifact, profile, instance, continuity, principal, device, and session identifiers. BLAKE3 and Ed25519 are candidate algorithms, not specification-level mandates.
3. **Decision and evidence records:** append-only commitments under a declared retention and witness profile; decision, attempt, outcome observation, reconciliation, contest, and revision are distinct record types.
4. **Operation governance:** consequence-classified mediation. Pure or low-risk operations may be covered by session or batch commitments; high-consequence effects require operation-specific admission and observation.
5. **Session model:** mutual typed identity binding, capability negotiation, semantic and protocol version commitments, transcript linkage, expiry, revocation, and termination.
6. **Hardware model:** least-authority device mediation with effect-specific observers and an explicit physical-world remainder.
7. **Execution substrate:** a staged path from a testable Rust realization toward PEIR or another obligation-carrying intermediate representation if evidence shows the added layer preserves rather than obscures obligations.
8. **Bootstrap model:** a minimal measured predecessor, exact plan or binary commitments, declared initial authority, recovery and rollback, and first-state reconciliation.
9. **Epoch model:** typed succession between exact predecessor and successor states, with carried debt, capability migration or revocation, compatibility claims, rollback bounds, and witness evidence.

### 8.2 Selection Is Not Proof of Optimality

The Configuration Manifold can make alternatives explicit; it cannot mechanically prove that MosaiCOS is uniquely optimal without a preference constitution and comparative evidence. "Recommended" means recommended by the paper's declared preferences, not entailed by domain physics.

Candidate alternatives include adapting seL4, Genode, Fuchsia, a Linux security and identity plane, or a userspace constitutional runtime. Each may dominate a clean-slate kernel for a particular cost, assurance, compatibility, or deployment profile. MosaiCOS remains a valuable proposal even if one of those realizations becomes the preferred implementation path.

## 9. Prototype Sufficiency and Conformance Levels

The source named five load-bearing elements: process identity, capability token, kernel receipt chain, typed refusal, and bootstrap commitment. Those elements are an excellent **minimal thesis demonstrator**, but they cannot both be sufficient for full COS conformance and coexist with nine mandatory invariants that include sessions, hardware attribution, and succession.

This candidate resolves the contradiction by defining levels:

| Level | Meaning |
|---|---|
| `COS-SPECIFIED` | The system or document defines how each invariant would be satisfied and names unresolved obligations. |
| `COS-PROTOTYPE` | An exact artifact demonstrates the five-element thesis on a bounded operation surface; omitted invariants and bypasses are explicit debts. |
| `COS-REALIZED` | An exact implementation claims all nine invariants for a declared capability and deployment surface. |
| `COS-EVIDENCED` | An evidence package supports that realization claim with negative controls, bypass testing, independent observation, reproducible verification, and explicit remainder. |

No named artifact receives one of these standings merely because the paper describes it. Standing attaches to an exact artifact and evidence package under an eligible review process.

The five prototype elements become:

1. typed constitutional instance and artifact identity;
2. finite delegated capability representation;
3. pre-effect decision commitment plus post-effect reconciliation record;
4. typed refusal or hold disposition;
5. declared bootstrap predecessor and first governed state.

This profile demonstrates the constitutional transition but carries explicit debts for sessions, hardware-effect evidence, full coverage, epoch succession, performance, recovery, and long-duration operation.

## 10. Kernel-to-Network Composition

MosaiCOS, a governed execution substrate, and MIP/AMIP can form a cross-layer evidence lineage, but three local hash chains do not automatically form one continuous proof. Composition requires an explicit linkage contract.

At minimum, a cross-layer transaction binds:

```text
CrossLayerTransaction
  transaction_id
  initiating_instance_id
  kernel_request_and_decision_commitments
  execution_plan_and_gate_commitments
  network_session_and_frame_commitments
  authority_and_capability_lineage
  semantic_operation_and_version
  predecessor_and_successor_links
  outcome_observers_and_methods
  time_and_ordering_evidence
  unresolved_remainder
```

The verifier must test not only hash continuity but also correspondence: that the kernel request is the execution operation claimed, the execution operation is the network request claimed, and the observed effect belongs to the same transaction. Provider translation, buffering, retries, concurrency, partial failure, and replay can otherwise create plausible but false joins.

A shared receipt schema may reduce tooling cost, but schema uniformity is not semantic equivalence. Process, network, artifact, capability, and transaction identifiers require domain separation and explicit translation rules.

## 11. Deployment Profiles and Their Debts

### 11.1 General-Purpose MosaiCOS

The target is a desktop, server, cloud, or single-board-computer operating system with all nine invariants over a declared kernel surface. A Rust transition kernel and a later PEIR-based substrate are alternative realization paths. Neither is granted standing here.

### 11.2 MosaiCOS Lite

A constrained single-process microcontroller profile can bind firmware identity, static authority, boot state, governed I/O requests, and bounded evidence. It may be a useful COS prototype, but static nonrevocable capabilities, a ring buffer that evicts history, absence of independent physical observers, and whole-image update semantics are conformance debts. Eviction changes the claim from complete append-only history to a declared retention window. A hash mismatch before receipt machinery exists must be represented by an external boot witness or later recovery evidence; "halt, no receipt" cannot satisfy universal refusal evidence by itself.

### 11.3 AMR-COS

An Ableman Mosaic Router profile composes router application governance with an operating-system substrate. The application, routing policy, network backends, host OS, drivers, and hardware must remain separate evidence surfaces. A governance layer running on Raspberry Pi OS can be an AMR constitutional application profile without proving the host kernel is COS-realized.

### 11.4 AMR-COS Lite on OpenWrt

An OpenWrt package can govern routing decisions and emit valuable evidence while relying on `netifd`,  
`nftables`,  
drivers, bootloaders, and the Linux kernel for enforcement. It is therefore a transition and compatibility profile unless those lower layers are brought within the declared COS mediation and evidence boundary. Calling the package a full constitutional OS would otherwise launder application-layer governance into kernel-level conformance.

### 11.5 Cross-Profile Equivalence

Profiles are not constitutionally equivalent merely because they use related hashes or receipt shapes. Equivalence requires a named relation: shared identity schema, shared obligation satisfaction, protocol interoperability, trace translation, or behavior under selected observations. Resource-bounded profiles may legitimately satisfy narrower contracts.

## 12. Evidence and Evaluation Program

An evidence package for a claimed COS realization should bind:

* exact source, dependencies, toolchain, build graph, binary or plan, configuration, boot image, and hardware or virtual platform;
* the declared capability surface and automated discovery of privileged or bypass paths;
* policy, preference constitution, Instance Configuration, identity and serialization schemas;
* admission, refusal, hold, execution, failure, crash, restart, update, rollback, and recovery traces;
* independent observers for software state and selected physical effects;
* performance, availability, storage, privacy, energy, and operator-cost measurements;
* mutation or fault-injection evidence showing that tests detect missing mediation, reordered records, forged identity, stale policy, unauthorized capability, and omitted effect;
* verifier identity, version, inputs, outputs, and reproducibility instructions;
* unresolved limitations, competing explanations, and open editorial questions.

### 12.1 Core Tests

1. **Unauthorized operation:** a request lacking capability must not produce the effect; the negative disposition must identify the responsible layer and evidence limits.
2. **Concurrent identity:** two instances of the same artifact and authority must have distinct execution identities while preserving their shared artifact and profile lineage.
3. **Restart continuity:** a successor must not impersonate its predecessor merely by reusing a stable artifact hash; continuity requires an authorized succession relation.
4. **Decision/effect ordering:** a consequential effect cannot precede its decision commitment under the observed clock and mediation boundary.
5. **Crash gap:** interruption after admission but before completion remains detectable and recoverable without claiming an effect that was not observed.
6. **Bypass mutation:** an intentionally unmediated route must be detected by capability-surface discovery or an independent observer.
7. **Receipt forgery:** internally consistent forged or omitted records must not be accepted as evidence of truth or completeness merely because their hashes verify.
8. **Epoch transition:** predecessor debt, capabilities, sessions, and compatibility claims must be explicitly carried, revoked, or refused.
9. **Cross-layer mismatch:** a kernel record joined to the wrong execution or network transaction must be rejected.
10. **Resource bound:** receipt and mediation costs must be measured under realistic workload, saturation, storage pressure, network loss, and failure.

### 12.2 Comparative Baselines

Evaluation should compare at least:

* a conventional OS with native security and audit configuration;
* the same OS with a userspace constitutional layer;
* an adapted capability-oriented or component-oriented system;
* a MosaiCOS prototype over an identical workload.

Outcomes should include security defects detected, false refusals, bypass coverage, recovery time, latency, throughput, storage growth, energy, operator comprehension, contestability, and independent-verification cost. A favorable receipt count is not a substitute for these outcomes.

### 12.3 Status of Source-Reported Realizations

The source reports CC Computing builds, gate tests, a MosaiCOS-on-Linux v0.1, and future Rust and PEIR paths. This version-family head does not bind the exact artifacts and evidence required to verify those claims. They remain source-reported leads and integration targets. Application-layer evidence cannot, by itself, prove kernel-layer conformance.

## 13. Integration with the Ableman Corpus

MosaiCOS becomes clearer when read as one realization of a larger constitutional-computing fabric:

* **Constitutional Computing** supplies the general proposition that constraints and authority must survive into executable effect.
* **Admissibility Engineering** supplies the method for distinguishing a declared surface from the constrained, implemented, and evidenced surface.
* **The Three Hash Rule** warns against collapsing exact state, admissibility commitments, and meaning commitments into one digest. COS identity and receipts should preserve those distinctions.
* **Reasoning by Way of Receipts** treats receipts as intermediate reason carriers with bounded claim ceilings, not proof tokens.
* **A Formal Theory of Work Custody** clarifies who is responsible for unresolved transitions, evidence, and repair without confusing custody with ownership or authority.
* **The Constitutional Observability Platform** supplies heterogeneous observers, verification, evidence-health, and explicit remainder needed to test kernel claims.
* **Governed Semantic Project Lineage** supplies artifact, build, configuration, and succession lineage across implementation revisions.
* **GMB**, the current Governed Meaning Base in the historical `CCF -> CMB -> GMB` terminology lineage, can hold the durable identities, claims, conflicts, decisions, evidence, and revision relations from which a specific OS constitution or policy projection is compiled. GMB is not the kernel and does not make the kernel conform.
* **MIP/AMIP and the Crystal Network** provide network and distributed-knowledge composition surfaces; cross-layer linkage must remain explicit.

This integration makes MosaiCOS more than a list of kernel features. It is an implementation target for constraint carriage from semantic specification through configuration, artifact realization, effect, evidence, and revision.

## Full-Stack Constitutional OS Demonstrator

The completed P1 corpus positions MosaiCOS as the **full-stack constitutional operating-system demonstrator and proposed Instance Constitution / Instance Configuration for the wider Constitutional OS discipline**. It connects identity, authority, sessions, effects, evidence, bootstrap, and succession across an operating substrate. It is not the discipline itself, a proven optimal configuration, or a production-qualified implementation by virtue of the name.

- **Adjacent work:** *Sovereign Software*  
  **Supplies:** Inspectability, reconstructability, delegation, replacement, and exit across dependency closure.  
  **MosaiCOS boundary:** MosaiCOS proposes an OS realization path; sovereignty requires separate actor- and capability-relative evidence.

- **Adjacent work:** *The Ableman Format Specification (AFS)*  
  **Supplies:** Profiles, schemas, and scoped conformance claims.  
  **MosaiCOS boundary:** A MosaiCOS profile may conform to AFS only under exact artifacts, validators, and evidence.

- **Adjacent work:** *The Mechanics of Constitutional Enforcement*  
  **Supplies:** Semantic placement, courts, mediation, effects, and receipts.  
  **MosaiCOS boundary:** MosaiCOS composes enforcement mechanics into an OS setting.

- **Adjacent work:** *A Constitutional Syscall Architecture for Cyber-Physical Control Systems*  
  **Supplies:** A minimal effect ABI and lifecycle for device-facing actions.  
  **MosaiCOS boundary:** The syscall architecture is one boundary profile; MosaiCOS spans the wider operating substrate.

- **Adjacent work:** *Universal Governance Kernel (UGK)*  
  **Supplies:** A reusable candidate governance-kernel architecture.  
  **MosaiCOS boundary:** UGK may implement a kernel role within MosaiCOS without becoming the complete OS or proving conformance.

A MosaiCOS conformance subject should bind:

$$
\begin{aligned}
O= (&discipline\_version, IC, IR, identity\_roots, \\
&authority\_model, kernel, effect\_surface, sessions, \\
&profiles, bootstrap, succession, evidence)
\end{aligned}.
$$

Here IC means Instance Constitution or Instance Configuration and realization-stage IR means Instance Realization or Implementation Realization. The discipline, selected configuration, source tree, build, runtime, deployment, device integration, and evidence package remain separate identities.

Profile names such as Lite or domain-specific variants must enumerate removed obligations, altered threat models, and reduced claim ceilings. Cross-profile equivalence cannot be inferred from common APIs or shared source. Bootstrap and succession must state which root authorizes the initial state, how successors are admitted, and what happens when evidence, hardware, or constitutional state diverges.

The universal GSM can type   
`INSTANTIATES_CONSTITUTIONAL_OS_DISCIPLINE`, `SELECTS_OS_IC`,  
`REALIZED_AS_OS_IR`, `BOOTS_FROM_ROOT`, `GOVERNS_SESSION`, `MEDIATES_EFFECT_SURFACE`,  
`ATTRIBUTES_HARDWARE_EFFECT`, `CONFORMS_TO_PROFILE`, `REDUCES_PROFILE_OBLIGATION`,  
`SUCCEEDS_DEPLOYMENT`,  
and   
`EVIDENCED_BY_OS_COURT`. These relations prevent a system name from carrying unearned maturity.

This integration establishes four editorial commitments: adopt full-stack constitutional OS demonstrator as MosaiCOS's official corpus role; adopt the conformance-subject envelope; require profile-specific obligation and claim-ceiling disclosure; and preserve discipline/IC/IR/build/runtime/deployment/evidence identities.

## Evidence-Loop Realization, Consciousness Non-Inference, Physical-Control Profile, and Transformation-Substrate Composition

The fixed-seed comparison with the Constitutional Observability Platform, Qualia Binding and Realization Mapping, the Direct-Coupled Dynamic Torque Reactor, and Jnana II clarifies four possible MosaiCOS compositions:

$$
\begin{aligned}
O^*= (&discipline\_version, IC, IR, identity\_roots, authority, \\
&kernel, effect\_surface, sessions, observation\_roles, \\
&transformation\_substrate, domain\_profiles, bootstrap, \\
&succession, evidence, remainder)
\end{aligned}.
$$

COP roles can supply scenario execution, evidence health, verification, interface recognition, situated assessment, and projection fidelity. A MosaiCOS realization may combine these roles only while preserving their claim ceilings and shared failure domains. Qualia research has no direct evidentiary dependence on MosaiCOS: neither constitutional scheduling, self-observation, nor situated-awareness surfaces establish consciousness or experience.

DCDTR can serve as a bounded cyber-physical domain profile whose controller, estimator, torque allocation, degraded modes, and hardware effects require explicit device capabilities and safety mediation. This transfers an architectural stress case, not vehicle feasibility or performance evidence.

Jnana II may provide a constitutional transformation substrate for software, policy, configuration, package, and agentic toolchain changes within or targeting an OS environment. MosaiCOS and Jnana II remain distinct: one is an OS demonstrator/profile; the other is a transformation-substrate profile. Their composition requires explicit representation, law, capability, execution, effect, evidence, recovery, and platform-boundary contracts.

The universal GSM can type   
`REALIZES_EVIDENCE_LOOP_ROLE`,  
`DOES_NOT_INFER_CONSCIOUSNESS_FROM_`  
`OBSERVABILITY`, `HOSTS_PHYSICAL_CONTROL_PROFILE`,  
`COMPOSES_WITH_TRANSFORMATION_SUBSTRATE`, `PRESERVES_OS_SUBSTRATE_IDENTITY`,  
`MEDIATES_HARDWARE_EFFECT`, and   
`LEAVES_PLATFORM_REMAINDER`.

This randomized review establishes four editorial commitments: extend the OS subject with observation, transformation, and domain-profile roles; preserve a consciousness non-inference boundary; treat DCDTR as a physical-control stress profile without empirical transfer; and define Jnana II composition without identity merger or conformance implication.

## A Full-Stack Demonstrator with an Explicit Trusted Remainder

Twelve retained downstream uses place MosaiCOS beneath capability contracts, constitutional syscalls, collective coordination, adversarial epistemology, physical-control profiles, GOORRT, Jnana, Jnana II, AFS, COP, semantic infrastructure, and APD-bounded computation. They confirm MosaiCOS as a proposed full-stack Constitutional OS demonstrator and configuration family, not the Constitutional OS discipline itself and not a production-qualified kernel.

$$
\begin{aligned}
O^*= (&discipline\_version, IC, IR, source, build, deployment, \\
&hardware, firmware, kernel, user\_space, identity\_roots, \\
&authority\_roots, sessions, capabilities, \\
&effect\_membranes, observers, receipts, profiles, \\
&bootstrap, succession, recovery, evidence, \\
&trusted\_remainder)
\end{aligned}.
$$

Here IC may mean Instance Constitution or Instance Configuration, while realization-stage IR may mean Instance Realization or Implementation Realization. Discipline, selected configuration, source, build, runtime, deployment, hardware integration, and evidence package remain distinct. Profile reduction must enumerate removed obligations, changed threat assumptions, unavailable remedies, and reduced claim ceilings.

No kernel fully governs the hardware, firmware, supply chain, operator, recovery root, external service, or observer merely by naming those boundaries. Bootstrap must identify the root of trust and the point where antecedent authority enters. Succession must preserve predecessor identity, migration, rollback, and unresolved state. Independent observation and recovery must not share every failure domain with the subject.

The universal GSM can type   
`INSTANTIATES_CONSTITUTIONAL_OS`, `SELECTS_OS_IC`,  
`REALIZES_OS_IR`, `BOOTS_FROM_DECLARED_ROOT`, `MEDIATES_OS_EFFECT`,  
`ATTRIBUTES_HARDWARE_BOUNDARY`, `REDUCES_PROFILE_OBLIGATION`, `OBSERVED_OUTSIDE_OS_DOMAIN`,  
`SUCCEEDS_OS_DEPLOYMENT`, and   
`RETAINS_TRUSTED_REMAINDER`.

This review establishes four editorial commitments: retain demonstrator and configuration-family standing; adopt the complete OS subject record; require profile-reduction, bootstrap, succession, independent-observation, and trusted-remainder declarations; and prohibit component composition or system naming from implying conformance, optimality, deployment, or consciousness.

## 14. Counterevidence and Failure Conditions

The proposal is weakened or requires revision if:

* native operating-system mechanisms already satisfy the same obligations under a simpler, well-evidenced composition;
* pre-effect recording creates unacceptable latency, storage, wear, energy use, or availability loss;
* batching or asynchronous effects make the decision/effect boundary semantically unstable;
* cryptographic identities expose sensitive lineage or enable durable tracking;
* authority registries centralize power or make recovery impossible;
* receipt production becomes a denial-of-service target or can be selectively bypassed;
* self-observation repeatedly disagrees with independent physical or state observation;
* typed refusals become misleading because failures cross multiple layers;
* a clean-slate kernel expands the trusted computing base more than an adapted verified system;
* users cannot understand, contest, or repair constitutional decisions;
* the GMB, policy compiler, verifier, or observer becomes an unreviewed oracle;
* cross-layer chains preserve hashes while losing semantic correspondence;
* the cost of exact evidence exceeds the consequence-adjusted benefit.

The strongest counterexample would be a smaller architecture that offers equal or better mediation coverage, independent evidence, recovery, sovereignty, and performance without a new kernel. The research program should actively seek that result.

## 15. Limits and Claim Ceiling

This paper does not establish:

* that the nine invariants are exhaustive or minimal;
* that no existing shipping OS satisfies any particular invariant;
* that Linux, seL4, Redox, Genode, or Fuchsia has the gap assigned by the source;
* that MosaiCOS is the first, only, or optimal constitutional operating system;
* that a MosaiCOS kernel, Lite device, router OS, or PEIR substrate currently conforms;
* that BLAKE3, Ed25519, Rust, PEIR, user-space drivers, or a microkernel are required by COS;
* that receipt integrity proves effect, correctness, completeness, non-bypassability, or moral legitimacy;
* that constitutional governance prevents compromise by hardware, firmware, kernel, operator, supply-chain, or authority failures.

It establishes a coherent proposal: a constitutional OS discipline can be specified through typed identity, finite authority, pre-effect decision commitment, post-effect evidence, refusal semantics, declared coverage, sessions, hardware attribution, and bootstrap succession; MosaiCOS is one proposed configuration of that discipline; and both can be tested under an explicit evidence contract.

## Demonstrator, Discipline, and Trusted Remainder

### Public orientation

MosaiCOS presents constitutional operating-system design as a practical route to user sovereignty: identities, capabilities, refusals, effects, and receipts become inspectable and renegotiable up to a declared hardware boundary. The paper proposes an OS discipline and a named instance. It is not evidence that a production operating system already satisfies every claim.

### Adversarial tests

1. **Bypass attack.** A device, driver, firmware component, DMA path, recovery mode, or privileged service acts outside the governed route. Complete mediation must be demonstrated per effect class.
2. **Trusted-base creep.** More policy and observability move into privileged code until the trusted computing base becomes unauditable. TCB size, interfaces, and justification require measurement.
3. **Capability-confusion attack.** Delegation, inheritance, namespace aliasing, or stale handles expand authority. Capabilities must bind subject, object, operation, scope, time, attenuation, and revocation.
4. **Receipt-before-effect race.** Concurrency, buffering, or device behavior lets an effect escape before durable evidence. Ordering and failure atomicity need implementation-level tests.
5. **Recovery-authority attack.** Emergency or repair paths bypass normal law and become permanent. Recovery profiles need bounded authority, visibility, expiry, and post-event review.
6. **Usability failure.** Sovereignty controls are too complex, inaccessible, or costly for ordinary users. Inspectability without comprehensibility or remedy is insufficient.
7. **Performance and energy attack.** Constitutional enforcement produces unacceptable latency, throughput loss, storage growth, or power cost. These are empirical tradeoffs, not dismissible implementation details.

### Claim and evidence ceiling

The defensible current claim is that the paper specifies a full-stack constitutional OS architecture and evaluation program with an explicit trusted remainder. Source-reported prototypes or components must be bound to exact versions, environments, tests, and limitations before they support implementation claims.

The paper does not yet prove production security, complete mediation, hardware-rooted sovereignty, performance acceptability, accessibility, or user benefit. Comparative OS claims require resolvable external sources and reproducible evaluation. No external research was added in this pass.

### Reader-facing consequence

The paper should foreground what changes for a person: software effects can be attributed, constrained, refused, inspected, contested, and reconstructed without surrendering the conventional OS primitive floor. The name MosaiCOS should remain the proposed instance; the Constitutional Operating System is the broader discipline.

## 16. Conclusion

The important shift is not from ungoverned computers to computers with more logs. It is from an implicit relation among identity, privilege, policy, effect, and evidence to an explicit and contestable one.

COS names the discipline. MosaiCOS names a proposed Instance Configuration and system lineage whose exact identity still requires author adjudication across the wider corpus. A realization must then earn its claims one artifact, boundary, effect, and evidence relation at a time.

The load-bearing rule is not that a receipt makes an effect legitimate. It is that no consequential effect should silently outrun its declared identity, authority, decision, observation, and revision obligations. A pre-effect commitment can show what the system decided to do. A post-effect observer can support what happened. A coverage account can show what neither record could see. A revision path can keep disagreement and repair alive.

That is a stronger architecture than post-hoc narration and a narrower claim than perfect governance. It is also falsifiable. If MosaiCOS cannot preserve these distinctions under concurrency, crash, bypass, resource pressure, update, adversarial authority, and independent observation, then the proposal has not yet crossed from specification into evidenced realization.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that operating systems mediate memory, process execution, storage, devices, and communication, but their security mechanisms do not automatically constitute a reviewable governance order. Its nearest external comparison fields are governance, software, security. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Modularity, secure-development practice, and reproducibility reduce classes of failure but do not guarantee architectural coherence or user sovereignty. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E2]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E3]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** David L. Parnas. "On the Criteria To Be Used in Decomposing Systems into Modules." *Communications of the ACM* 15(12), 1972, pp. 1053-1058. DOI: 10.1145/361598.361623. https://doi.org/10.1145/361598.361623 **Relationship:** Foundational modularity treatment used to compare information hiding with explicit semantic and governance interfaces.

**[E6]** Ward Cunningham. "The WyCash Portfolio Management System." *OOPSLA '92 Experience Report*, 1992. DOI: 10.1145/157709.157715. https://doi.org/10.1145/157709.157715 **Relationship:** Original technical-debt metaphor used to distinguish implementation debt from semantic debt.

**[E7]** Karen Scarfone, Murugiah Souppaya, and Donna Dodson. *Secure Software Development Framework (SSDF) Version 1.1*. NIST SP 800-218, 2022. DOI: 10.6028/NIST.SP.800-218. https://doi.org/10.6028/NIST.SP.800-218 **Relationship:** Adjacent secure-development framework for preparation, protection, production, and vulnerability response.

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

**[A6]** Adam Ableman. *Sovereign Software*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-24C6159B98023A9C`;  
source SHA-256  
`6AAFE79E438B980B75D1910A897F7BA716A10CF1187B68CB1F71405F36725A18`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Constitutional Software Analysis (CSoftA): A Governance-Based Classification Method for Software Systems*. Ableman Corpus current edition; work identity `PAPER.PUB.20472196`;  
source SHA-256  
`3670B28B7C1AF5467BE4002C47B5F964F8FAF6F257125C2F84CE06904E4FD0DE`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Adam Ableman. *Admissibility Engineering*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *A Formal Theory of Work Custody*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *Constitutional Computing: Structured Abundance*. Unpublished corpus source; exact publication identity requires verification.

Adam Ableman. *The Constitutional Observability Platform*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *From Content-Addressed Storage to Governed Semantic Project Lineage*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition in the author-confirmed historical terminology `CCF -> CMB -> GMB`; conceptual claims retain the standing stated in the work.

Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *The Three Hash Rule*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20788617.

Current primary-source literature and implementation review for Linux, seL4, Redox, Genode, Fuchsia, capability systems, measured boot, kernel audit, and operating-system identity remains required for a future evidence-qualified revision.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848092](https://doi.org/10.5281/zenodo.23848092)
