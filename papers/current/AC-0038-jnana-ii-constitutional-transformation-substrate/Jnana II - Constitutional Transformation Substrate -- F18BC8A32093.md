# Jnana II: Constitutional Transformation Substrate

## Transformation Admissibility, Authority Containment, and Evidence Under AI Acceleration

### Replay requires explicit closure and may be exact, deterministic, equivalence-class, or observational.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Software assurance usually evaluates programs, artifacts, or executions more directly than the authority and law governing the transformations that produced them. Compilers, build pipelines, configuration, CI, package hooks, deployment systems, and AI-generated rewrites may introduce dependencies, capabilities, effects, and policy changes whose authority is partly ambient or retrospectively narrated.

Jnana II proposes a **constitutional transformation substrate** in which transformation regimes, admission rules, capability grants, effect boundaries, and receipts become explicit governed artifacts. Its strongest thesis is not that program correctness can be replaced by constitutional review. It is that program correctness and transformation admissibility answer different questions: whether a result satisfies a technical property, and whether the transformation was permitted to bind under declared law, authority, capability, and effect limits.

The architecture organizes MCIR, MCIR-Law, Constitutional Invariants, PEIR, Domain Effects, and ReceiptLog into a proposal-admission-lowering-effect-witness path. The revision sharply bounds the claims. Canonical representation gives an artifact standing within a declared Jnana profile, not existence in general. A decidable law layer does not make arbitrary execution predictable. Effect membranes govern only mediated paths. Actual effects may be partial or irreversible. Receipts prove recorded relations, not truth or legitimacy. Replay requires explicit closure and may be exact, deterministic, equivalence-class, or observational.

The paper adds an authority envelope, negative-power obligations, coverage testing, failure atomicity, recovery, an incremental adoption ladder, GMB/GSM integration, and a full evaluation program. It remains a specification candidate: no implementation, universal containment, deterministic replay, hardware adaptation, or transformation-correctness result is established.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. The custody and comparison manifest is   
`work/paper-saturation-v1/evidence/jnana-ii-`

`constitutional-transformation-substrate/`  
`integration-custody-manifest.v0.1.json`,  
SHA-256  
`9385155F925B1C15BA88D5133F97665833E5C8D295F66F3B7492CCBF4D9FA652`. The source remains unchanged.

The Jnana II architecture, named components, constrained-proposer model, negative-power thesis, hardware discussion, and migration outline are author material. The formal envelope, bounded claims, recovery and coverage requirements, corpus integration, tests, counterevidence, and decisions added here are AI editorial or synthetic candidates until adopted. No external research was conducted.

## 1. Program Correctness and Transformation Admissibility

A type check, proof, test, reproducible build, or artifact hash can support a bounded property claim. It does not by itself answer:

- who authorized the transformation;
- which law and version applied;
- whether the tool and dependencies were admitted;
- whether capability or effect scope expanded;
- whether an exception or break-glass path was used;
- what partial effects occurred on failure; or
- which evidence supports promotion of the result.

Jnana II calls this second family **transformation admissibility**. It complements rather than supersedes technical correctness.

## 2. The Constitutional Transformation Envelope

Represent a governed transformation as:

$$
T=(I,P,L,A,C,G,\Gamma,X,W,R),
$$

where $I$ binds exact inputs and predecessor identity, $P$ the proposal, $L$ applicable law, $A$ authority, $C$ requested capabilities, $G$ the gate decision, $\Gamma$ the admitted transformation regime and environment, $X$ resulting artifacts and external effects, $W$ evidence and receipts, and $R$ recovery and revision state.

The path is:

$$
\begin{aligned}
&I \\
&\rightarrow P \\
&\rightarrow (L,A,C) \\
&\rightarrow G \\
&\rightarrow \Gamma \\
&\rightarrow X \\
&\rightarrow W \\
&\rightarrow R
\end{aligned}.
$$

A refusal, deferment, escalation, or partial-failure record is a valid result. A gate decision does not guarantee that downstream mediation is complete.

## 3. MCIR as a Governed Carrier

MCIR can represent program semantics, compiler passes, gates, identity regimes, capabilities, laws, and effect declarations under a chosen profile. Canonicalization supports stable identity only for material admitted to that profile and canonicalization law.

The source says that a transformation that cannot be canonically represented does not exist within Jnana. The bounded claim is: it receives no Jnana standing under that profile. The external transformation may still exist and may still affect the system through an uncovered path. Unrepresentable or unresolved material should be refused, isolated, or explicitly carried as remainder rather than erased.

## 4. MCIR-Law and Admission

MCIR-Law is proposed as a decidable law and gate layer over bounded artifacts and questions. A decision may return `ADMIT`,  
`REFUSE`, `DEFER`, `ESCALATE`, or `NOT_COVERED`. It should bind:

- proposal and artifact identity;
- law and constitutional-invariant versions;
- authority and delegation chain;
- requested capability and effect classes;
- evidence obligations and unresolved material;
- result, reason, and expiry;
- exception or emergency status; and
- appeal and revision path.

Decidability applies only to the declared gate language and inputs. It does not decide arbitrary behavior or guarantee that reality matches the model.

## 5. Constitutional Invariants

Constitutional Invariants constrain how ordinary law and transformation regimes may change. Candidate invariants include:

1. no effect authority without an explicit grant;
2. no grant widening without constitutionally authorized change;
3. no law mutation that silently weakens receipt or witness obligations;
4. no promotion of AI output into author, maintainer, or constitutional standing by generation alone;
5. no exception path without identity, scope, time, evidence, and closure;
6. no retroactive relabeling of an unauthorized effect as authorized;
7. no claim of replay beyond its demonstrated class; and
8. no claim of complete mediation without coverage evidence.

These are candidate specifications, not proven enforced properties.

## 6. PEIR and Execution

PEIR is proposed as an expressive execution layer below the decidable admission surface. The architecture does not solve general program behavior or make Turing-complete execution safe by declaration.

Containment depends on concrete mediation, resource limits, isolation, host and hardware assumptions, recovery, and tested correspondence between admitted representation and realized execution. "All actual behavior is visible and reversible" is too strong. Behavior outside instrumentation may be invisible; physical, network, financial, disclosure, and human effects may be irreversible.

The supported goal is bounded observability, mediation, and compensating recovery for declared effect classes.

## 7. Domain Effects and Capability Sovereignty

Domain Effects define interfaces between computation and external consequence. Each effect request should declare class, target, parameters, authority, duration, expected result, compensation, and evidence.

No ambient syscall authority is an architectural objective, not a present fact. The threat model must cover direct syscalls, subprocesses, build scripts, package hooks, network clients, credentials, plugins, drivers, firmware, humans, and emergency channels. Governance Coverage Gaps tests whether a path can reach an effect without crossing the declared membrane.

An effect membrane cannot govern what it cannot observe or interpose upon.

## 8. Partial Failure, Atomicity, and Recovery

A transformation can emit an artifact, modify state, send a request, expose a secret, and then fail. A single pass/fail status hides this structure.

The receipt should record:

- intended and attempted effects;
- completed, failed, unknown, and compensating effects;
- retained intermediate artifacts;
- rollback or repair attempts;
- residual risk and next authority; and
- whether retry is safe, idempotent, or prohibited.

Atomicity is a property to demonstrate at a defined boundary, not a default assumption. Recovery may restore a local artifact without undoing an external consequence.

## 9. ReceiptLog and Replay Classes

ReceiptLog binds transformation evidence and lineage. A receipt is useful only with exact identities, governed keys, observation limits, and preserved payload custody.

Replay should be classified:

- **exact artifact replay:** identical retained result bytes;
- **deterministic execution replay:** identical result under declared closed inputs and runtime;
- **equivalence-class replay:** different result satisfying a declared relation;
- **observational replay:** repeated tests produce results within declared bounds; or
- **non-replayable with reconstruction:** history can be inspected but not rerun.

Reproducibility does not establish legitimacy, and legitimacy does not establish reproducibility.

## 10. AI as Constrained Proposer

AI may propose code, MCIR changes, gate rules, law amendments, capability changes, tests, and explanations. Proposal is not authority. The architecture should ensure that a model cannot obtain effect merely by describing it, cannot author its own grant, and cannot choose the evidence standard by which its result is promoted.

This separation fails if the same agent controls proposal, interpretation, admission, effect, and witness without independent constraints. Human review alone is not sufficient if the interface hides scope, dependencies, or partial effects. Automation may assist every role while preserving distinct authority and receipts.

## 11. Negative Power

Negative power is the capacity to refuse, stop, exit, fork, revoke, recover, and renegotiate without an unauthorized effect being treated as inevitable. It requires:

- visible binding and capability scope;
- a usable stop or refusal path;
- revocation and expiry;
- provider and dependency exit where claimed;
- governed break-glass behavior;
- appeal and amendment;
- reconstruction or migration material; and
- evidence of what occurred before refusal.

Negative power is bounded by physical reality, safety duties, shared-resource rights, and the chosen constitution. It is not an unlimited individual veto over every system.

## 12. Hardware and Host Boundary

Firmware hashes, verified boot, admitted backends, syscall bridges, and device profiles may strengthen a bounded platform claim. They do not prove hardware behavior or remove supply-chain, microcode, management-engine, peripheral, physical-access, timing, side-channel, and availability assumptions.

Each platform profile should state the lowest trusted boundary, excluded components, update and recovery authority, measurement regime, and claim ceiling. Hardware sovereignty is not established merely by representing a firmware image in MCIR.

## 13. Incremental Adoption Ladder

- **Level:** 0  
  **Adoption target:** exact inputs, proposals, results, and receipts  
  **Claim ceiling:** custody only

- **Level:** 1  
  **Adoption target:** capability and effect inventory  
  **Claim ceiling:** declared inventory, not coverage

- **Level:** 2  
  **Adoption target:** proposal/authority separation and typed gate outcomes  
  **Claim ceiling:** bounded admission process

- **Level:** 3  
  **Adoption target:** admitted transformation profiles and replay classification  
  **Claim ceiling:** conformance for tested profiles

- **Level:** 4  
  **Adoption target:** mediated build, package, tool, and deployment effects  
  **Claim ceiling:** coverage limited to tested paths

- **Level:** 5  
  **Adoption target:** host, recovery, provider-exit, and hardware profiles  
  **Claim ceiling:** assurance limited to declared boundary

Advancement requires evidence from the current level. A receipt-only system must not claim effect containment.

## 14. Corpus Integration

**Jnana** supplies the original governed-genome architecture. Jnana II narrows its transformation and authority implications. **Water: MCIR as the Engineering of Governed Change** supplies transformation-carriage detail. **Constitutionally Governed Infrastructure** broadens the runtime and institutional boundary. **Governance Coverage Gaps** supplies the escape-path audit.

**The Three Hash Rule** binds governing input, judgment or operation, and result. **Reasoning by Way of Receipts** supplies claim-bounded inference. The **Governed Meaning Base (GMB)** can retain law, authority, representations, grants, effects, evidence, exceptions, conflicts, and revisions. The universal **GSM** can type these relations without making representation equal realization or receipt equal truth.

## 15. Realization Funnel

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

- **Possibility:** enumerate constitutional, incremental, centralized, federated, and legacy-wrapping regimes.
- **Specification:** define identity, law, authority, capabilities, effects, receipts, refusal, recovery, and claim ceilings.
- **CM1:** retain admissible configurations, including costly, partial, centralized, or undesirable ones.
- **CM2:** prefer configurations by sovereignty, containment, inspectability, accessibility, performance, and migration burden.
- **IC:** select an Instance Constitution or Instance Configuration for one bounded toolchain and platform.
- **IR:** produce an Instance Realization or Implementation Realization of schemas, gates, compilers, membranes, stores, and interfaces.
- **Evidence:** run custody, bypass, conformance, effect, partial-failure, replay, recovery, provider-exit, and platform tests.
- **Revision:** amend law and architecture through successor identity, migration, and receipts.

This paper reaches Specification and proposes CM1/CM2 and adoption criteria. It does not select a complete IC or produce an IR.

In this funnel, IR denotes the realization stage and remains distinct from Intermediate Representation in MCIR.

## 16. Evaluation Program

Evaluation should include untrusted AI proposals, hidden dependencies, capability widening, compiler and policy upgrades, build and install hooks, direct syscall and subprocess paths, plugin and credential effects, denied and deferred operations, partial failure, rollback, compromised receipts, replay divergence, concurrent changes, break-glass events, provider removal, schema migration, and platform recovery.

Measures should include uncovered capability rate, bypass success, false admission and refusal, obligation loss, effect mismatch, unknown residual effects, replay class, reconstruction success, recovery time, user comprehension, performance cost, accessibility burden, and governance capture risk.

## Constitutional Transformation Substrate Profile

Across the completed P1 corpus, Jnana II is the **constitutional transformation substrate profile for software and agentic toolchains**. It proposes a coordinated surface for exact proposals, MCIR carriers, bounded law, capability grants, procedural lowering, effect mediation, receipts, recovery, and provider exit. It does not replace program correctness, prove complete mediation, or establish that a Jnana realization exists.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** The general stage-contract theory of governed translation.  
  **Jnana II boundary:** Jnana II configures that theory for software transformation and effect paths.

- **Adjacent work:** *The Implementation Codex*  
  **Supplies:** IC-to-IR realization package with phases, bindings, gates, tests, and journals.  
  **Jnana II boundary:** A Codex can package a Jnana realization without becoming the substrate's semantic identity.

- **Adjacent work:** *A Constitutional Syscall Architecture for Cyber-Physical Control Systems*  
  **Supplies:** A specialized effect-mediation profile at a cyber-physical boundary.  
  **Jnana II boundary:** Constitutional syscalls are one membrane realization, not the whole transformation substrate.

- **Adjacent work:** *Governance Coverage Gaps*  
  **Supplies:** Audit of capabilities and effects that escape declared governance.  
  **Jnana II boundary:** Coverage evidence sets the ceiling of every Jnana containment claim.

- **Adjacent work:** *The Ableman Format Specification (AFS)*  
  **Supplies:** Artifact roles, profiles, canonical encodings, validators, and conformance fixtures.  
  **Jnana II boundary:** AFS can standardize Jnana artifacts without proving their execution or authority.

The substrate should expose six independently testable planes: representation, law and admission, capability authority, transformation execution, external effect, and evidence/recovery. A plane boundary is valid only when the mapping, authority, bypass model, and failure behavior are explicit. One component may implement several planes, but their claims remain distinct.

A realization profile should bind:

$$
\begin{aligned}
J= (&representation, law, invariants, authority, capabilities, \\
&lowering, executor, effect\_membrane, witness, recovery, \\
&exit, coverage, platform\_boundary)
\end{aligned}.
$$

The corrected funnel clarifies that this document remains at Specification. IC may mean Instance Constitution or Instance Configuration. Realization-stage IR may mean Instance Realization or Implementation Realization and must not be conflated with MCIR's Intermediate Representation. A schema set, reference CLI, mediated toolchain, host profile, and hardware-bounded platform are progressively stronger IR classes, not one binary implementation claim.

The universal GSM can type   
`CONFIGURES_JNANA_SUBSTRATE`,  
`REPRESENTS_TRANSFORMATION_IN_MCIR`, `EVALUATES_UNDER_MCIR_LAW`,  
`GRANTS_BOUNDED_CAPABILITY`, `LOWERS_TO_EXECUTION_PROFILE`, `CROSSES_EFFECT_MEMBRANE`,  
`WITNESSES_PARTIAL_EFFECT`, `RECOVERS_LOCAL_STATE`, `EXITS_PROVIDER`,  
and   
`BOUNDS_CLAIM_AT_PLATFORM`. These relations turn the architecture into a testable profile rather than a totalizing system label.

This integration establishes four editorial commitments: retain Jnana II as the constitutional transformation substrate profile; adopt the six-plane separation and realization-profile envelope; define progressively stronger IR classes and their evidence gates; and make coverage, partial effects, recovery, provider exit, and platform boundary mandatory claim ceilings.

## OS Composition and Safety-Critical Physical Transformation at the Randomized Edge

The clipped fixed-seed edge comparison with MosaiCOS and the Direct-Coupled Dynamic Torque Reactor provides two demanding realization profiles without broadening Jnana II into a total system:

$$
\begin{aligned}
J^*= (&representation, law, invariants, authority, capabilities, \\
&lowering, executor, effect\_membrane, witness, recovery, \\
&exit, coverage, OS\_boundary, physical\_safety\_boundary, \\
&remainder)
\end{aligned}.
$$

MosaiCOS may host or consume a Jnana II realization for software, package, policy, session, service, and configuration transformations. The OS constitution, selected IC, realized IR, Jnana substrate, source tree, build, runtime, deployment, and evidence package remain separate subjects. Neither profile proves the other conforms.

DCDTR supplies a safety-critical physical-domain stress case. Controller or calibration changes may be proposed and lowered through Jnana planes, but effect mediation must terminate at explicit device capabilities, hardware identity, timing constraints, safety interlocks, qualified authority, and independently measured plant behavior. A passing software receipt does not establish torque, energy, thermal, emissions, or vehicle safety claims.

The universal GSM can type   
`COMPOSES_WITH_OS_ENVIRONMENT`,  
`TRANSFORMS_CONTROLLER_ARTIFACT`, `TERMINATES_AT_HARDWARE_BOUNDARY`,  
`REQUIRES_PHYSICAL_SAFETY_AUTHORITY`, `WITNESSES_PARTIAL_PHYSICAL_EFFECT`,  
`RECOVERS_SOFTWARE_NOT_WORLD_STATE`, and   
`TRANSFERS_NO_VEHICLE_EVIDENCE`.

This randomized review establishes four editorial commitments: add OS and physical-safety boundaries to the realization profile; preserve distinct MosaiCOS/Jnana subjects; treat DCDTR as a bounded transformation stress case; and state that software recovery, replay, and receipts cannot restore or prove external physical state.

## A Host-Composition Contract for the Transformation Substrate

Ten retained downstream uses place Jnana II inside other architectures without merging their identities. Governance as Compilation supplies the general stage theory. Crystallized Governance supplies a constitutional artifact profile. Jnana and its open-source projection supply wider architectural and contribution contexts. UGK may supply transition functions. MDSP can profile Jnana II as one domain standard. MosaiCOS can host it. Governance Coverage Gaps bounds mediation claims. Direct-Coupled Dynamic Torque Reactor supplies a safety-critical physical stress profile. *Everything Is a Compiler* treats it as an engineered architecture, not proof of the universal lens. Digital Gold supplied only a bibliographic mention and is not retained as a dependency.

The composition contract is:

$$
\begin{aligned}
C= (&host, substrate\_profile, representations, law, \\
&capabilities, execution, effect\_membrane, receipts, \\
&replay, recovery, exit, platform\_boundary, coverage, \\
&conformance, remainder)
\end{aligned}.
$$

Each host must name which Jnana II planes it realizes, which external mechanisms supply omitted planes, and where effects can bypass the substrate. Hosting, calling, profiling, or sharing MCIR artifacts does not establish identity or conformance. UGK transaction logic, OS scheduling, package management, hardware drivers, professional engineering, and domain law remain separately governed dependencies.

Composition testing should cover partial failure across substrate and host, duplicate and late effects, rollback after external change, receipt disagreement, capability revocation, provider exit, unavailable recovery dependencies, and host updates that invalidate a previously qualified membrane. A successful replay may establish computational reconstruction while leaving physical or institutional effects unreplayed.

The universal GSM can type   
`HOSTS_JNANA_SUBSTRATE_PROFILE`, `SUPPLIES_EXTERNAL_PLANE`,  
`COMPOSES_UGK_TRANSACTION`, `MEDIATES_DOMAIN_TRANSFORMATION`,  
`BYPASSES_SUBSTRATE_EFFECT_PATH`, `REVOKES_CAPABILITY_AFTER_HOST_CHANGE`,  
`REPLAYS_WITH_EXTERNAL_REMAINDER`, and   
`CONFORMS_WITHOUT_IDENTITY_MERGER`.

This reverse-dependency review establishes four editorial commitments: adopt the host-composition contract; require plane coverage and bypass disclosure; test cross-boundary partial failure, revocation, replay, recovery, and exit; and preserve host, UGK, domain, OS, and Jnana II identity and authority boundaries.

## 17. Counterevidence and Failure Modes

The proposal should be narrowed or rejected where: (1) transformation correctness is presented as replacing program correctness; (2) all conventional tooling is described as ambient; (3) existing security and provenance mechanisms are ignored; (4) canonical representation is confused with existence; (5) MCIR profile limits are hidden; (6) decidable law is applied to undecidable behavior; (7) gate admission is treated as execution safety; (8) PEIR correspondence is untested; (9) all behavior is called visible; (10) irreversible effects are called reversible; (11) effect paths bypass the membrane; (12) build or package hooks retain ambient authority; (13) partial effects are hidden by one status; (14) rollback is assumed atomic; (15) receipts omit environment or dependencies; (16) signatures are treated as authority; (17) deterministic replay lacks closure; (18) equivalence is selected after results; (19) AI proposal gains standing by fluency; (20) one actor controls proposal, law, admission, effect, and witness; (21) constitutional invariants can be weakened by ordinary law; (22) break-glass use is silent; (23) negative power ignores shared rights or safety; (24) provider exit is claimed without reconstruction; (25) firmware hashes are treated as hardware behavior; (26) lower platform layers exceed the claim boundary; (27) migration levels are conflated; (28) GMB inclusion becomes validation; (29) adjacent papers are merged by thematic overlap; (30) a specification is presented as a working substrate; (31) measured overhead or complexity defeats the use case; or (32) external technical research shows the novelty or feasibility claim is overstated.

## Govern Transformations Without Confusing Admission and Correctness

### Public orientation

Jnana II proposes a substrate in which transformation proposals, law, authority, capability grants, admitted environments, external effects, receipts, recovery, and revision become explicit. Technical correctness and transformation admissibility answer different questions. A lawful transformation can be technically wrong; a technically correct artifact can result from an unauthorized or unsafe transformation.

### Adversarial tests

1. **Admission-correctness collapse.** An admitted transformation is treated as correct, secure, safe, useful, or semantically faithful.
2. **Canonical-existence attack.** Material outside MCIR or the selected profile is treated as nonexistent rather than unrepresented, unresolved, or an uncovered effect path.
3. **Decidability-overreach attack.** A decidable bounded law language is presented as deciding arbitrary behavior, social conflict, or future effects.
4. **Membrane-coverage attack.** Governed syscalls or Domain Effects are assumed complete while direct host, dependency, hardware, network, administrator, or recovery paths remain.
5. **Partial-effect attack.** Failure after some irreversible or external action is represented as atomic refusal or clean rollback.
6. **Receipt-truth attack.** ReceiptLog proves legitimacy, reality, completeness, or causal responsibility beyond the recorded relation.
7. **Host-composition attack.** A compliant Jnana component runs within a host whose scheduler, filesystem, credentials, update path, or recovery authority violates the claimed envelope.
8. **Negative-power bypass.** Refusal and nonpromotion rights exist in the model but deadlines, defaults, emergency paths, or resource control force continuation.

### Claim and evidence ceiling

Jnana II is a constitutional transformation-substrate specification candidate. It does not establish an implementation, universal containment, transformation correctness, complete mediation, deterministic replay, hardware adaptation, failure atomicity, or recovery. Canonical representation grants only profile-relative standing, not general existence or authority.

Systems, security, compiler, operating-system, hardware, distributed-transaction, formal-methods, and human-governance claims require current primary-source comparison and exact adversarial realization evidence. No external research was added in this pass.

### Reader-facing consequence

The public question becomes: was this exact transformation authorized under the right law, tools, capabilities, host, and effect boundary - and separately, did it produce the technically and semantically correct result?

## 19. Conclusion

AI acceleration increases the rate at which software, configuration, dependencies, and authority assumptions can change. The central Jnana II insight is that those transformations need a constitutional surface: exact proposal, law, authority, capability, gate, transformation, effect, witness, and recovery.

That surface cannot make arbitrary execution decidable or all effects reversible. It cannot govern escape paths it does not mediate, and it cannot turn receipts into legitimacy. Its contribution is more precise: it makes transformation authority an explicit object of design and testing alongside program behavior.

Jnana II is therefore best understood as a specification for bounded lawful transformation. Its next proof is not rhetorical completeness. It is a small, adversarially tested toolchain profile that can demonstrate where authority begins, where it ends, which effects cross the membrane, and what remains outside the constitution.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of compiler and build architecture, formal methods, capability systems, sandboxing and isolation, software supply-chain security, reproducible builds, package and CI systems, AI coding tools, operating-system mediation, firmware and verified boot, hardware trust boundaries, and related constitutional or policy-as-code systems.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that software assurance usually evaluates programs, artifacts, or executions more directly than the authority and law governing the transformations that produced them. Its nearest external comparison fields are governance, security, formal. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847983](https://doi.org/10.5281/zenodo.23847983)
