# A Constitutional Syscall Architecture for Cyber-Physical Control Systems

## Core ABI, Effect Adjudication, and Evidence for Robotics Platforms

### An authorization receipt proves only that a named policy state admitted a request.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

This paper specifies a constitutional programming architecture for cyber-physical control. An effect-pure computational core proposes world-touching operations; a boundary evaluates them against scoped authority, versioned constraints, current context, and timing obligations. Actuation, sensing, time, persistence, and communication become explicit constitutional crossings rather than ambient privileges.

The central correction is that admissibility is not execution. A complete effect lifecycle distinguishes proposal, admission, dispatch, device acceptance, physical observation, and evidentiary standing. An authorization receipt proves only that a named policy state admitted a request. It does not prove that a driver accepted it, an actuator moved, the intended physical effect occurred, or the surrounding world remained safe. Cyber-physical governance therefore requires typed receipts, independent observations, bounded unknown states, non-bypassability evidence over the whole trusted computing base, and an emergency path that does not depend on the ordinary adjudicator remaining healthy.

The architecture is presented as a proposal and evaluation program, not as demonstrated safety, real-time performance, replay equivalence, certification, or standards conformance.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/`

`constitutional-syscall-architecture-cyber-`  
`physical/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`53BF4F2280B5F2029BF160F8B4161E72C3CADB3190BF5B739846FE6CD7930694`. The source remains unchanged.

The architectural thesis and source-native constructs are author material. Lifecycle, formal, safety-boundary, evidence, integration, test, and decision additions are AI editorial or synthetic candidates until adopted. No robot, controller, boundary, driver, or safety system was implemented or tested. No external reference or standard was checked.

## 1. Constitutional Effect Separation

The architecture separates four logical regions:

1. **Computational core:** produces typed proposals but lacks direct effect authority.
2. **Constitutional boundary:** decides whether a proposal is admissible under a bound policy state.
3. **Effect substrate:** dispatches admitted operations through drivers, transports, devices, and physical interfaces.
4. **Witness and evidence surface:** observes requested and actual outcomes and assigns bounded evidentiary standing.

The governing invariant is conditional, not self-proving:

> No in-scope world-touching operation may occur except through an admitted effect path, and no claim of effect may exceed the available observation.

"In-scope" must be enumerated. Motors can coast, gravity acts, batteries fail, networks inject traffic, sensors age, interrupts fire, and human operators can touch equipment without a software syscall. The boundary governs mediated commands; it does not constitutionalize physics merely by naming an API.

## 2. Minimal Effect ABI

The source proposes five categories:

```text
ACTUATE
SENSE
TIME
PERSIST
COMMUNICATE
```

A request envelope should bind at least:

```text
EffectRequest {
  request_id
  operation
  typed_parameters
  requester_identity
  requested_capability
  policy_ref
  context_ref
  deadline
  freshness_requirement
  idempotency_key
  provenance
}
```

Operation-specific schemas remain necessary. Torque, brake, and velocity requests require units, frames, bounds, and validity intervals. Sensor reads require source, calibration, timestamp, quality, and freshness. Time calls must distinguish monotonic time, wall time, duration, and deadline. Persistence and communication require destination, confidentiality, retention, and retry semantics.

A small ABI reduces the constitutional surface only if extensions cannot bypass its obligations.

## 3. Effect Lifecycle and Typed Outcomes

Let $r$ be an effect request, $a$ authority state, $c$ observed context, and $p$ policy version. Admission is:

$$
A(r,a,c,p) \rightarrow (o,q),
$$

where $o$ is a typed decision and $q$ is a structured reason. Admission outcomes include:

```text
AUTHORIZE
SIMULATE
DEFER
REFUSE
CANCEL
UNKNOWN
```

`AUTHORIZE` means only that dispatch is permitted under the bound inputs. The full lifecycle is:

$$
\begin{aligned}
&PROPOSED \\
&\rightarrow ADJUDICATED \\
&\rightarrow DISPATCHED \\
&\rightarrow ACCEPTED \\
&\rightarrow OBSERVED \\
&\rightarrow EVIDENCE
\end{aligned}.
$$

Each arrow can fail, time out, or become unknown. A robust result vocabulary therefore includes `DISPATCH_FAILED`,  
`DEVICE_REJECTED`, `EFFECT_OBSERVED`, `EFFECT_NOT_OBSERVED`, `PARTIAL_EFFECT`,  
`CONFLICTED_OBSERVATION`, and `OUTCOME_UNKNOWN`.

This separation prevents the architecture from treating a policy decision or log entry as proof of physical success.

## 4. Authority Is Scoped, Not Merely Ranked

A scalar lattice such as $L_0 \leq L_1 \leq L_2 \leq L_3$ cannot express all relevant authority. Authority should be a scoped capability:

$$
\begin{aligned}
\alpha = (&subject, operation, object, bounds, context, validity, \\
&delegation, provenance)
\end{aligned}.
$$

An authority can permit braking but not acceleration, one robot but not another, one geofence but not a neighboring zone, or one time window but not indefinite repetition. More rank does not automatically mean broader jurisdiction.

Multiple authorities require a declared composition algebra. A simple sequence is insufficient when authorities disagree, operate over disjoint scopes, or return stale results. Composition must define precedence, conjunction, veto, conflict, abstention, timeout, evidence, and recovery. Refusal need not always dominate: an expired or out-of-scope refusal is not equivalent to a valid safety veto.

## 5. Binding Between Admission and Effect

Physical context can change after admission but before actuation. The architecture should bind:

- the request and typed parameters;
- the policy and contract version;
- the authority state;
- the context snapshot and freshness window;
- the effect adapter and device identity;
- the deadline and cancellation semantics.

If any required binding changes before dispatch or acceptance, the request is re-adjudicated or refused. Repetition does not create authority.

The Three Hash Rule supplies a nearby custody discipline: bind the intended subject, the frozen governed artifact, and the observed result rather than allowing one hash to stand for the whole transition. The exact three-hash mapping for cyber-physical effects remains an author and implementation decision; this paper does not claim that a hash proves physical reality.

## 6. Receipts and Witnesses

At least three receipt classes are needed:

1. **Adjudication receipt:** what request was evaluated against which authority, context, and policy, with what decision.
2. **Dispatch receipt:** what adapter or device endpoint accepted or rejected which admitted request.
3. **Effect observation receipt:** what independent witness observed, with calibration, timestamp, uncertainty, and coverage.

Receipts support reasoning only within their observation boundaries. A boundary-generated receipt cannot independently prove the boundary was not bypassed. A motor-controller acknowledgment cannot prove wheel motion. A wheel encoder cannot alone prove vehicle displacement. Witness independence and coverage must be declared.

The Governed Meaning Base can preserve operation schemas, authority scopes, policy lineage, receipt types, tests, and revision relations. It does not turn stored assertions into evidence automatically.

## 7. Non-Bypassability and the Trusted Computing Base

The statement "all effects traverse the boundary" is a whole-system property. Its trusted computing base can include boot configuration, runtime, scheduler, memory protection, middleware, drivers, direct-memory-access devices, firmware, buses, credential stores, update paths, operator interfaces, clocks, log sinks, and recovery mechanisms.

Wrapping a middleware topic is insufficient if a controller, plugin, driver, maintenance interface, or compromised component can reach hardware through another path. Non-bypassability evidence should include path enumeration, negative tests, privilege analysis, boot and configuration binding, runtime integrity checks, and physical interface review.

The claim must also be scoped. The system may prove that a defined software path is mediated without proving that every possible physical or administrative effect is controlled.

## 8. Real-Time and Safety Paths

Real-time feasibility requires measured worst-case behavior, not the labels "fast path" and "slow path." Each control loop must declare deadline, jitter budget, policy-evaluation bound, queue behavior, cache invalidation cost, timeout result, and overload posture.

Slow adjudication must not block a hard deadline without a predeclared safe response. Precomputed envelopes can support bounded fast paths, but only if their context, validity, and revocation semantics are explicit.

Emergency stop should not rely solely on the ordinary boundary, network, controller, clock, or log remaining healthy. A defensible design uses independent and preferably diverse stop or energy-isolation paths appropriate to the hazard analysis. "Fail safe" is not universal: an abrupt stop can itself be hazardous, and some systems must remain fail-operational long enough to reach a safer state.

## 9. Sensing, Time, and Simulation

Sensing is a constitutional crossing because imported information changes what the core may infer and do. Yet mediation does not guarantee truth. Sensor identity, calibration, timestamp, uncertainty, occlusion, spoofing risk, and transformation lineage must travel with the observation.

Time is also plural. Monotonic time supports intervals; wall time supports external coordination; logical time orders distributed events. Replay must preserve which form was used and which nondeterministic inputs were recorded.

An identical ABI does not establish simulation/hardware equivalence. Simulation replaces a physical effect with a model-mediated result. Correspondence requires explicit tolerances, domain assumptions, calibration, coverage, and tests across the simulation-to-hardware boundary.

## 10. Logging, Replay, and Evidence Ceilings

A log entry can record request, decision, bound state, and later observations. Append-only and hashable are design intentions, not proof of tamper evidence, completeness, availability, or correct observation. Custody, sequencing, omission detection, key management, clock behavior, and independent witnesses remain relevant.

Replay can reproduce recorded adjudication when code, policy, inputs, ordering, and nondeterminism are sufficiently bound. It cannot replay the physical world. Deterministic decision replay and physical outcome reconstruction are different claims.

Accordingly:

$$
Standing(claim) \leq Coverage(receipts,witnesses,custody).
$$

This paper supplies no evidence that the proposed system meets a real-time deadline, prevents bypass, makes simulation equivalent to hardware, satisfies a safety standard, or improves safety.

## 11. Failure and Recovery Semantics

The architecture must define behavior for boundary crash, policy-store unavailability, stale context, authority conflict, network partition, duplicate request, delayed cancellation, device reset, partial actuation, missing witness, full log, corrupted clock, power loss, and restart after uncertain effect.

Recovery cannot assume the last authorized command either occurred or did not occur. Unknown outcome is a first-class state. Before resumption, the system may require physical re-observation, reconciliation, safe-state acquisition, or human inspection.

Liveness is also constitutional. A boundary that refuses everything may preserve one safety invariant while destroying mission, rescue, medical, or stability obligations. Availability targets and lawful degraded modes must be specified alongside refusal.

## 12. Relation to the Corpus

*Effect Sovereignty* supplies the general core-world distinction and effect-boundary thesis. This paper specializes that thesis for cyber-physical control and adds operation-specific timing, observation, hardware, and recovery obligations.

*Reasoning by Way of Receipts* constrains what can be inferred from adjudication, dispatch, and observation records. *The Three Hash Rule* supplies a custody pattern for binding intent, governed artifact, and result. *Agentic Interface Surfaces* provides a nearby account of executable interfaces that recognize progress through evidence-bearing effects. These are typed interfaces, not automatic identity or evidentiary inheritance.

## 13. Realization Funnel

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

- **Possibility:** enumerate ways computational proposals can relate to physical effects.
- **Specification:** define the ABI, authority, lifecycle, timing, safety, and evidence obligations.
- **CM1:** include every admissible realization, including slow, over-restrictive, unsafe, or weakly observed variants.
- **CM2:** select preferable variants under hazard, sovereignty, performance, assurance, and reversibility criteria.
- **IC:** bind one Instance Constitution or Instance Configuration to a platform and operating domain.
- **IR:** construct an Instance Realization or Implementation Realization of boundary, adapters, witnesses, recovery, and evidence.
- **Evidence:** test timing, bypass resistance, effect correspondence, failures, and claims.
- **Revision:** change contracts, architecture, or standing when evidence or operating conditions change.

This paper is a Specification and CM1/CM2 architecture candidate. It does not instantiate an IC, build an IR, or supply platform evidence. Realization-stage IR is distinct from Intermediate Representation in MCIR and other compiler contexts.

## 14. Evaluation Program

A credible evaluation should include:

- ABI completeness and extension tests;
- direct and indirect bypass attempts;
- authority-scope, expiry, delegation, and conflict tests;
- worst-case execution time and jitter measurements;
- cache staleness and revocation races;
- duplicate, reordered, and delayed request tests;
- partial-actuation and lost-acknowledgment recovery;
- independent effect-observation coverage;
- sensor spoofing, staleness, and calibration faults;
- simulation/hardware correspondence under declared tolerances;
- log omission, reordering, corruption, and custody tests;
- power loss, restart, partition, and degraded-mode behavior;
- emergency-stop independence and common-cause failure analysis;
- learned-controller adaptation under refusal without reward hacking.

## Cyber-Physical Effect-Boundary ABI Profile

Across the completed P1 corpus, the Constitutional Syscall Architecture is the **cyber-physical effect-boundary ABI profile for proposing, adjudicating, dispatching, observing, reconciling, and receipting device-facing actions**. It does not make a safe controller by interface design alone, eliminate hard real-time paths, or prove that all physical effects pass through the mediated boundary.

- **Adjacent work:** *The Integrity Enforcement Layer*  
  **Supplies:** General protected effect mediation and refusal.  
  **Syscall-architecture boundary:** The syscall paper specializes mediation to robotics and cyber-physical effects.

- **Adjacent work:** *The Mechanics of Constitutional Enforcement*  
  **Supplies:** Rule placement, court separation, ratchets, effect atomicity, and remainder.  
  **Syscall-architecture boundary:** The syscall ABI is one concrete boundary profile for those mechanics.

- **Adjacent work:** *A Cognitive ABI for Capability-Centered Computing*  
  **Supplies:** Capability contracts, qualification, routing, substitution, and effect ceilings.  
  **Syscall-architecture boundary:** Cognitive planning may propose calls; device authority and effect evidence remain separately bound.

- **Adjacent work:** *MosaiCOS: A Constitutional Operating System*  
  **Supplies:** A proposed full operating-system configuration.  
  **Syscall-architecture boundary:** The syscall ABI can be an OS subsystem without inheriting whole-system standing.

- **Adjacent work:** *Testing for Deriving Observable State of Software Systems*  
  **Supplies:** Bounded observation and state-derivation tests.  
  **Syscall-architecture boundary:** Device observations support reconciliation; they do not make hidden physical state fully known.

An effect invocation should bind:

$$
\begin{aligned}
E= (&principal, capability, target, command, prestate, \\
&authority, safety\_profile, deadline, admission, \\
&dispatch, witnesses, outcome, remainder, receipt)
\end{aligned}.
$$

Proposal, admission, reservation, dispatch, physical effect, observation, verification, commit, and recovery are different events. A pre-effect decision cannot attest to a future physical outcome. A post-effect receipt may establish only the observation captured by its witnesses. Unknown, late, duplicated, partially applied, and irreversible effects require explicit outcomes.

Non-bypassability is a claim about the trusted computing base and actual effect paths. Emergency and hard real-time paths may use preauthorized bounded profiles, but their scope, expiry, telemetry, reconciliation, and override authority remain inspectable. Simulation evidence does not transfer automatically to physical deployment.

The universal GSM can type `PROPOSES_SYSCALL`, `REQUIRES_DEVICE_CAPABILITY`,  
`ADMITTED_UNDER_SAFETY_PROFILE`, `RESERVED_FOR_EXECUTION`, `DISPATCHED_TO_DEVICE`,  
`OBSERVED_BY_SENSOR`, `RECONCILED_WITH_PRESTATE`, `PARTIALLY_EFFECTED`, `BYPASSED_MEDIATOR`,  
`RECOVERED_BY`,  
and   
`RECEIPTED_WITH_CEILING`. These relations preserve the physical uncertainty boundary.

This integration establishes four editorial commitments: adopt cyber-physical effect-boundary ABI profile as the official corpus role; adopt the effect-invocation envelope; require explicit partial, late, duplicate, unknown, and irreversible outcomes; and make non-bypassability and simulation-to-physical transfer separately evidenced claims.

## Effect-Intent Custody and Resolved Identity

The fixed-seed comparison with the Implementation Codex, HLIR, *Who Has the Ball?*, and GTK adds a cross-layer effect-intent contract:

$$
\begin{aligned}
I= (&intent\_id, proposal\_head, custodian, term\_bindings, \\
&capability, target, authority, admission, dispatch, \\
&observation, reconciliation, terminal\_disposition)
\end{aligned}.
$$

HLIR can express the proposed effect and unresolved alternatives. The Implementation Codex can package the selected device profile, dependencies, safety assumptions, and effect-boundary realization. Neither artifact is a dispatched command. The syscall boundary must bind the exact admitted intent and reject widening introduced during lowering or realization.

Work Custody becomes safety-relevant while an effect is pending, partially applied, late, unknown, or under recovery. A named custodian must remain responsible for observation, reconciliation, escalation, and terminal disposition even if device control, review authority, and recovery execution belong to different actors. Custody does not itself grant any of those authorities.

GTK can resolve the lexical and semantic identity of capabilities, targets, safety profiles, outcomes, and recovery operations under a versioned registry. Resolver success is neither capability possession nor effect authority. Ambiguity, version conflict, or jurisdiction mismatch should stop or qualify admission rather than be silently normalized.

The universal GSM can type   
`CUSTODIES_EFFECT_INTENT`, `BINDS_SYSCALL_TERM_WITH_GTK`,  
`LOWERS_PROPOSAL_WITHOUT_DISPATCH`, `REJECTS_INTENT_WIDENING`,  
`RETAINS_CUSTODY_DURING_EFFECT_UNKNOWN`, `RECONCILES_PARTIAL_PHYSICAL_EFFECT`,  
and   
`RESOLVES_IDENTITY_WITHOUT_GRANTING_AUTHORITY`.

This randomized review establishes four editorial commitments: adopt the effect-intent contract; retain custody through unknown and recovery states; bind capability and target terms through versioned resolution; and make resolver, proposal, realization, admission, dispatch, and physical effect distinct events.

## The Cross-Layer Trace to a Physical Effect

Nine downstream uses place the constitutional syscall at the final governed crossing of a longer chain. GTK resolves the identity of capabilities, targets, safety profiles, and outcomes. Governance as Compilation and GCML carry stage and procedural obligations toward an effect membrane. HLIR expresses a reviewable proposal. The Implementation Codex packages the selected device configuration and boundary realization. Jnana II and MosaiCOS can host the membrane as one subsystem. APD states the bounded containment objective. Work custody keeps an unresolved physical intent owned through observation and recovery.

The complete trace is:

$$
\begin{aligned}
T= (&proposal, term\_bindings, selected\_IC, \\
&realization\_package, call\_intent, authority, admission, \\
&reservation, dispatch, physical\_effect, observation, \\
&reconciliation, custody, terminal\_disposition)
\end{aligned}.
$$

No upstream artifact is a device command. Resolver success does not grant capability. Procedural reachability does not grant authority. A conforming Implementation Codex does not prove the membrane is non-bypassable. Admission and dispatch do not prove an effect. Device acknowledgment and sensor observation have separate ceilings. Unknown, partial, late, duplicate, cancelled-after-effect, and irreversible outcomes must retain custody until a terminal disposition is justified.

Every lowering boundary should bind the exact predecessor intent and declare preserved, refined, deferred, refused, or widened fields. Undeclared widening of target, magnitude, duration, timing, safety profile, or recovery scope invalidates the call. Emergency and real-time paths remain profiles with bounded preauthorization, expiry, telemetry, reconciliation, and independent stop obligations.

The universal GSM can type   
`RESOLVES_EFFECT_TERM`, `LOWERS_EFFECT_PROPOSAL`,  
`PACKAGES_DEVICE_CONFIGURATION`, `PROPOSES_CONSTITUTIONAL_SYSCALL`,  
`REJECTS_EFFECT_INTENT_WIDENING`, `DISPATCHES_SEPARATELY_FROM_ADMISSION`,  
`OBSERVES_PHYSICAL_EFFECT_WITH_CEILING`, and   
`RETAINS_CUSTODY_UNTIL_RECONCILED`.

This reverse-dependency review establishes four editorial commitments: adopt the full cross-layer effect trace; require explicit preservation and widening checks at each lowering; retain custody through all nonterminal effect outcomes; and require emergency, real-time, simulation, and bypass claims to carry separate evidence profiles.

## 15. Counterevidence and Claim-Boundary Tests

The proposal must narrow or fail if: (1) an unmediated hardware path exists; (2) admission is reported as physical success; (3) a log can be emitted before effect; (4) device acknowledgment is mistaken for motion; (5) witnesses share the same failure source; (6) context expires before actuation; (7) authority rank crosses jurisdiction; (8) multi-authority conflicts lack a deterministic rule; (9) refusal deadlocks a safety-critical loop; (10) the emergency path depends on the failed component; (11) worst-case latency misses deadlines; (12) cache reuse survives revocation; (13) duplicate retries create repeated actuation; (14) cancellation arrives after irreversible effect; (15) restart assumes an unknown effect did not occur; (16) sensors are stale or spoofed; (17) time sources jump or disagree; (18) simulation parity exceeds measured correspondence; (19) physical replay is claimed from decision replay; (20) log custody cannot detect omission; (21) policy updates race active commands; (22) extensions bypass the base ABI; (23) an operator or maintenance port bypasses authority; (24) firmware or DMA bypasses middleware; (25) a safe stop creates a new hazard; (26) over-refusal destroys required liveness; (27) learning adapts around refusal; (28) contract semantics are ambiguous; (29) external standards do not support the attributed claim; (30) the demonstration platform lacks an adequate hazard analysis; (31) cryptographic binding does not bind physical observation; (32) evidence coverage is too narrow for the paper's conclusion; (33) implementation details expand the trusted base beyond review; (34) the same request has non-idempotent device semantics; (35) policy compromise authorizes unsafe effects; or (36) the architecture cannot state which effects remain outside its jurisdiction.

## Physical Effects Require More Than a Valid Syscall

### Public orientation

Constitutional robotics turns world-touching operations into structured syscalls: an effect-pure core proposes action, a constitutional boundary checks identity, authority, contracts, state, and limits, and the resulting actuation receives a typed outcome and receipt. This improves inspectability. It does not guarantee physical safety, stability, or complete control.

### Adversarial tests

1. **Sensor-spoof attack.** Valid authorization operates on false state. Sensor identity, calibration, plausibility, redundancy, and uncertainty must enter adjudication.
2. **Timing attack.** A correct command arrives too late or in the wrong order. Deadlines, jitter, clock source, freshness, and safe timeout behavior are contract fields.
3. **Control-instability attack.** Individually admissible actions destabilize the closed loop. The syscall boundary must compose with verified control envelopes and rate limits.
4. **Physical-remainder attack.** Refusal or cancellation occurs after momentum, heat, pressure, charge, or mechanical motion persists. Recovery must model irreversible and decaying effects.
5. **Emergency-override attack.** A safety bypass becomes an unbounded authority path. Override identity, scope, duration, logging, and post-event review are mandatory.
6. **Partition attack.** The controller loses network, authority, time, or evidence services. The local safe state and degraded mode must not depend on unavailable adjudication.
7. **Human-override failure.** A person cannot understand, reach, or safely use the stop mechanism. Human factors and accessibility are part of the safety case.
8. **Actuator-bypass attack.** Firmware, manual controls, maintenance tools, or alternate buses reach the physical effect outside the syscall path. Complete mediation is hardware- and topology-relative.

### Claim and evidence ceiling

The paper specifies a cyber-physical effect-boundary ABI and evaluation agenda. It does not establish safety certification, control stability, real-time correctness, hazard coverage, human-factors adequacy, or implementation readiness for any physical system.

Every realization claim requires exact hardware, firmware, plant model, sensors, actuators, timing, network, hazards, safety envelope, test environment, independent witness, and residual-risk record. Current robotics, control, functional-safety, and regulatory sources plus qualified engineering review are required. No external research was added in this pass.

### Reader-facing consequence

The accessible result is that an AI should not touch the physical world through an unstructured tool call. Every actuation should cross a boundary that can say who requested it, what state justified it, which limits applied, what actually happened, and how the system entered a safe remainder.

## Conclusion

Cyber-physical systems should not inherit world-touching authority merely because a controller can produce a command. A constitutional syscall architecture makes requests, authority, policy, outcomes, and evidence explicit. Its strongest contribution is not the claim that one boundary makes a robot safe, but the separation of questions that ordinary stacks can blur: what was proposed, what was permitted, what was dispatched, what physically happened, what was observed, and what may now be claimed.

That separation creates an architecture that can be tested. Until those tests exist, the work remains a specification for governed physical effects, not a certification of them.

## Reference and Verification Note

### Author corpus interfaces inspected under exact custody

Ableman Adam Ableman *Effect Sovereignty.*

Ableman Adam Ableman *Reasoning by Way of Receipts.*

Ableman Adam Ableman *The Three Hash Rule.*

Ableman Adam Ableman *Agentic Interface Surfaces.*

### External verification required

The source mentions ROS-style middleware, F1TENTH-class platforms, IEC 61508, ISO 10218, and ANSI/RIA R15.06. No external source was consulted in this pass. Publication should verify terminology, applicability, bibliographic details, current editions, and every standards-alignment statement against primary sources.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Evidence.** This stage is outside the present paper's asserted contribution and evidentiary scope.
- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that this paper specifies a constitutional programming architecture for cyber-physical control. Its nearest external comparison fields are cps, security, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Runtime monitors and fallback controllers only protect modeled safety envelopes and can fail through sensor error, timing assumptions, unsafe recovery, or omitted hazards. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Edward R. Griffor et al. *Framework for Cyber-Physical Systems: Volume 1, Overview*. NIST SP 1500-201, 2017. DOI: 10.6028/NIST.SP.1500-201. https://doi.org/10.6028/NIST.SP.1500-201 **Relationship:** Adjacent cyber-physical systems framework for trustworthiness, timing, data, and lifecycle concerns.

**[E2]** J. Tanner Slagel et al. "A Formal Verification Framework for Runtime Assurance." *NASA Formal Methods*, 2024. NASA NTRS 20230017350. https://ntrs.nasa.gov/citations/20230017350 **Relationship:** Adjacent runtime-assurance formalization, useful for comparing failover safety with constitutional admission and effect recognition.

**[E3]** Nancy G. Leveson and John P. Thomas. *STPA Handbook*. MIT, 2018. https://psas.scripts.mit.edu/home/books-and-handbooks/ **Relationship:** Adjacent systems-theoretic hazard analysis method; used to test treatment of unsafe control and system-level constraints.

**[E4]** Robert N. M. Watson, Simon W. Moore, Peter Sewell, and Peter G. Neumann. *An Introduction to CHERI*. University of Cambridge Technical Report UCAM-CL-TR-941, 2019. DOI: 10.48456/tr-941. [cl.cam.ac.uk source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-941.html) **Relationship:** Adjacent capability architecture demonstrating unforgeable hardware authority and compartmentalization.

**[E5]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E6]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E7]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

### Ableman corpus

**[A1]** Adam Ableman. *Constitutional Robotics*. Ableman Corpus current edition; work identity `PAPER.PUB.18750683`;  
source SHA-256  
`D10DF9B6B7F742D9EEABF01BC5DFC3755BB4EBF548E8CB5F215BB9D94678F514`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Constitutionally Governed Infrastructure*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-EF5747107D56F516`;  
source SHA-256  
`9C708BA381108EEA252404DF33F7B3B1648EC9CF5F2ACF00BAB88C6A15540926`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Constitutional Syscalls*. Ableman Corpus current edition; work identity `PAPER.PUB.18737229`;  
source SHA-256  
`5F14356180812262778F8574C292F4F6B560993042E5358B02EAB9CF0F7DE14C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *The Integrity Enforcement Layer*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-505307E9E6571B63`;  
source SHA-256  
`F858AB32E0937B796353CAE573DD4183FDF4F179A3E1E7E40C4E0C6BF1AB0018`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constitutional Robotics: System Calls as the Programming Model for Actuation, Sensing, and Epistemic World Interaction.* Zenodo, 2026. doi:10.5281/zenodo.18750683

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847356](https://doi.org/10.5281/zenodo.23847356)
