# Direct-Coupled Dynamic Torque Reactor

## Programmable Inertial Response, Multi-Actuator Torque Allocation, and Governed Electromechanical Propulsion

### Similarity to series-hybrid and range-extender topologies must be treated as a prior-art and identity question, not answered by terminology.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

The **Direct-Coupled Dynamic Torque Reactor (DCDTR)** is a proposed propulsion architecture in which an internal-combustion or other thermal converter is mechanically coupled to a controllable motor-generator but decoupled from wheel speed. A DC electrical bus, traction motors, and one or more storage substrates mediate the path to the wheels. The principal design object is therefore not a mechanical gear hierarchy but a controlled energy-and-torque system coordinating generation, storage, traction, thermal state, emissions, and mission demand.

The proposal combines several ideas: stabilized engine operating regions; fast generator-torque control; multi-timescale storage; wheel-level electric traction; state estimation; constrained energy management; and an explicit admissibility layer for safety, component limits, emissions, and degraded modes. Its strongest novel contribution may be the integrated governance and explanatory architecture rather than any single hardware element. Similarity to series-hybrid and range-extender topologies must be treated as a prior-art and identity question, not answered by terminology.

This revision separates physical state, control input, disturbance, parameter, and output variables; distinguishes a constraint set from its controlled viability kernel; repairs the mission objective; bounds the programmable-inertia analogy; separates realizability, control feasibility, comparative benefit, and constitutional-reframing claims; and adds safety, fault, empirical, GMB/GSM, and realization-funnel surfaces. No engineering or external literature validation was performed.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/direct-`

`coupled-dynamic-torque-reactor/integration-`  
`custody-manifest.v0.1.json`,  
SHA-256  
`5E73E45896E564CE4323A0393BA5170F131D8014B717F55CA20F8FA50110E798`. The exact source remains unchanged.

The DCDTR architecture, mechanisms, analogies, three-layer proposal, quantitative examples, cited technologies, falsification pathways, and bibliography are author material. The corrected formal partition, narrower claim ladder, safety obligations, GMB/GSM placement, realization funnel, countertests, and open editorial questions are AI editorial or synthetic contributions until adopted.

No cited technology specification, commercial implementation, mathematical model, bibliography entry, or comparative claim was externally checked. No prototype, simulation, controller, stability proof, safety analysis, or drive-cycle study was performed. Nothing here authorizes construction or establishes safety, feasibility, novelty, superiority, conformance, canonical standing, or evidence readiness.

## 1. Architectural Proposal

The intended topology is:

```text
thermal converter <-> directly coupled motor-generator
                              |
                           DC bus
                    /          |          \
              storage      auxiliaries   traction inverter(s)
                                               |
                                        electric wheel drive
```

"Direct-coupled" refers to the converter-to-generator shaft relation, not converter-to-wheel coupling. The engine or thermal converter may operate at selected speed-load regions while the electrical system supplies wheel demand. Ultracapacitors and a physical flywheel are optional configurations, not definitional requirements; their inclusion must be justified against mass, cost, loss, packaging, safety, and reliability.

The term **reactor** is architectural metaphor: several energy substrates and actuators interact within controlled constraints. It does not imply nuclear reaction, new thermodynamics, or that ordinary energy-balance laws have been superseded.

## 2. Four Claim Layers

The source's three layers are refined into four independently testable layers:

1. **Topology realizability:** components with adequate ratings can be connected in the proposed topology.
2. **Control feasibility and safety:** a controller and estimator can keep the realized system stable and within constraints across nominal, transient, and fault conditions.
3. **Comparative advantage:** a specified DCDTR configuration outperforms named baselines on matched missions after mass, cost, losses, emissions, reliability, repairability, and lifecycle effects are included.
4. **Constitutional reframing:** governed multi-substrate composition is a productive explanatory and design abstraction for propulsion.

Partial series-hybrid precedents could support Layer 1 while weakening novelty. They do not establish Layer 2 or 3. Formal coherence can motivate Layer 4 but cannot prove engineering benefit. Each claim must retain its own evidence and falsifiers.

## 3. Repaired State-Space Model

The source mixes states, controls, disturbances, and time in one set. A candidate model separates them:

$$
x=[\omega_e,E_f,V_{dc},z_b,z_u,T_e,T_g,T_i,T_b,\xi_w]^T,
$$

where $x$ contains engine speed, optional flywheel energy, bus voltage, battery and optional ultracapacitor states, component thermal states, and cumulative wear or degradation state $\xi_w$.

$$
u=[\dot m_f,\tau_g,\tau_{tr},P_b,P_u,\tau_f,q_{th}]^T
$$

contains fuel or thermal-converter command, generator torque, traction torque, storage powers, optional flywheel exchange, and thermal-management commands. Disturbance and mission input

$$
d=[P_{dem},v,\gamma,T_{amb},\mu_{road},a_{aux}]^T
$$

contains demanded traction power, vehicle speed, road grade, ambient temperature, road friction, and auxiliary load. Parameters $\theta$ include component maps, masses, efficiencies, capacities, limits, degradation models, and controller versions. Outputs satisfy:

$$
\dot x=f(x,u,d;\theta), \qquad y=h(x,u,d;\theta)+\eta.
$$

Exact state content is configuration-specific. A reduced model must state what omitted dynamics are bounded, observed, or left unknown.

## 4. Constraint Set and Viability Kernel

Let the operating constraint set be:

$$
K=\{(x,u,d)\mid c_i(x,u,d;\theta)\leq 0,\ i=1,\ldots,m\}.
$$

$K$ may contain thermal, electrical, mechanical, emissions, traction, drivability, storage, actuator-rate, vibration, and degraded-mode limits. It is not automatically a smooth manifold.

The controlled viability kernel is the stronger object:

$$
\mathrm{Viab}(K)=\{x_0\mid \exists u(\cdot)\ \text{such that}\ (x(t),u(t),d(t))\in K\ \forall t\in[0,T]\}.
$$

A state can lie inside $K$ yet be unable to remain there because of delay, energy shortage, actuator saturation, temperature momentum, or disturbance. The controller must reason about recoverability and future constraint satisfaction rather than current bounds alone.

Mandatory safety, hardware, emissions, and authority constraints belong in CM1. Efficiency, comfort, wear, cost, and reserve preferences may shape CM2 only among admissible trajectories.

## 5. Energy Balance and Mission Objective

A model must conserve energy within declared losses and storage changes. At a chosen boundary:

$$
P_{fuel}+P_{grid}=P_{wheel}+P_{aux}+P_{loss}+\frac{dE_{store}}{dt}+\frac{dE_{rot}}{dt}.
$$

Terms and sign conventions must be configuration-specific. The architecture does not create energy; it allocates conversion, buffering, and loss across time.

For a fixed mission, maximizing delivered traction energy is unsafe and ill-posed because mission demand normally constrains useful delivery. A candidate problem is:

$$
\min_{u(\cdot)} \int_0^T \ell(x,u,d;w)\,dt+\Phi(x(T))
$$

subject to dynamics, $K$, mission tracking, reserve, and terminal constraints. The cost may include fuel, grid energy, emissions, degradation, thermal stress, noise/vibration/harshness, tracking error, and monetary or lifecycle terms. Weight vector $w$ is a declared preference and jurisdictional choice, not a physical constant. Multi-objective or lexicographic formulations may be preferable where safety and stakeholder goals cannot be defensibly scalarized.

## 6. Programmable Inertial Response

Choose extraction-positive generator torque. An ideal shaft balance is:

$$
I_e\dot\omega_e=\tau_c-\tau_g-\tau_{loss}.
$$

If an ideal controller commands

$$
\tau_g=\tau_{base}+I_v\dot\omega_e,
$$

then algebraically

$$
(I_e+I_v)\dot\omega_e=\tau_c-\tau_{base}-\tau_{loss}.
$$

This motivates **programmable inertial response**, but it is not literal inertia. Real generator torque is delayed, filtered, quantized, saturated, energy-constrained, and coupled to bus voltage and storage acceptance. Estimation noise makes direct derivative feedback hazardous. Negative or rapidly varying $I_v$ can reduce damping or destabilize the shaft. A realized claim requires closed-loop stability, passivity or energy bounds, torsional-mode analysis, saturation handling, and fault behavior.

The controller may synthesize damping, speed regulation, transient shaping, or harmonic rejection. Each behavior should be named separately rather than treated as proof of one universal programmable mechanical property.

## 7. Multi-Timescale Torque and Energy Allocation

The architecture coordinates converter power, generator torque, storage, traction motors, and optional flywheel response across timescales. To avoid conflict with the established wheel-level meaning of "torque vectoring," the broader operation is called **multi-actuator torque and energy allocation** here.

Allocation must respect actuator bandwidth, stored energy, conversion losses, thermal headroom, traction limits, reserve requirements, and forecast uncertainty. Fast response does not imply sustained energy. Ultracapacitors, flywheels, and batteries provide different power-energy-duration profiles and losses; none is universally required.

A practical realization may use hierarchical control: fast inner current and torque loops, shaft-speed and bus-voltage loops, supervisory model-predictive or rule-based energy management, mission forecasting, and an independent safety layer. The paper does not select or validate such a controller.

## 8. Efficiency Regions and Comparative Baselines

Operating a thermal converter near favorable speed-load regions may reduce some conversion losses. The net vehicle result also depends on generator, inverter, bus, storage, traction motor, gearing, cooling, aftertreatment, start-stop, cold-start, and auxiliary losses. Stable engine operation can conflict with catalyst temperature, reserve, noise, or transient requirements.

Comparison must include at least:

- a conventional internal-combustion drivetrain;
- a contemporary parallel or power-split hybrid;
- a well-tuned series hybrid or range extender;
- a battery-electric architecture where mission-feasible; and
- the DCDTR configuration with every optional substrate charged against mass, volume, cost, and loss.

The relevant outcome is mission-level performance, not engine-map efficiency alone.

## 9. Mechanical-Coupling Claims

The source identifies several pathologies as sibling consequences of mechanically coupling combustion to wheel dynamics. This is a useful causal hypothesis, but removing that coupling does not automatically remove each pathology. Electric traction still uses gears, bearings, shafts, tires, and thermal systems; engine transients, catalyst warm-up, vibration, and storage constraints remain. Conventional hybrids already decouple some demands.

Each claimed consequence should become a causal diagram and matched test. Total complexity must count power electronics, cooling, sensors, wiring, storage, software assurance, cybersecurity, repair tooling, and supply chain in addition to eliminated clutch or transmission elements.

## 10. Fuel and Infrastructure Modularity

Separating thermal conversion from wheel demand can localize some fuel-specific behavior, but alternative fuels still affect tanks, seals, injectors, combustion maps, safety systems, emissions aftertreatment, certification, packaging, mass, infrastructure, and service procedures. A common electrical interface is not a complete substrate abstraction.

Vehicle-to-grid, vehicle-to-load, waste-heat use, and stationary dispatch are optional system capabilities, not unique consequences of DCDTR. The "energy shard" concept should be evaluated as a network profile with explicit authority, market, interconnection, cybersecurity, availability, and degradation constraints.

## 11. Safety, Faults, and Degraded Operation

A credible architecture must specify independent protection and safe-state behavior for:

- generator torque loss, reversal, or saturation;
- engine overspeed or unintended fueling;
- inverter, bus, isolation, or contactor faults;
- battery or capacitor overcurrent and thermal events;
- flywheel containment and bearing faults where present;
- estimator divergence, sensor loss, timing delay, and data corruption;
- traction-motor or wheel-speed disagreement;
- controller crash, update failure, and cyber compromise;
- cooling failure and aftertreatment temperature excursions;
- common-mode power or communication loss; and
- towing, emergency shutdown, limp-home, and service isolation.

The governance layer cannot be the same single point of failure as the controlled plant. Hardware limits, independent monitors, fault containment, and verified fallback paths are part of Layer 2 control feasibility, not later implementation detail.

## 12. Evaluation Program

The recommended evidence sequence is:

1. define a bounded reference topology and matched baselines;
2. publish component maps, mass, limits, losses, and uncertainties;
3. build a reproducible plant and estimator model;
4. establish controllability, observability, stability, and viable-region claims;
5. test nominal and adversarial missions in simulation;
6. perform hardware-in-the-loop controller and fault tests;
7. construct a subscale or dynamometer realization;
8. run matched drive cycles and transient tests;
9. assess emissions, thermal behavior, degradation, reliability, repairability, cost, and lifecycle effects; and
10. reproduce results independently.

Layer 1 should be divided by subsystem and configuration rather than declared globally. Layer 3 succeeds only if constitutional reframing yields better specifications, tests, or designs than simpler series-hybrid language.

## 13. Universal GSM and Realization Funnel

DCDTR is a domain application of constitutional reframing and admissibility engineering. The universal GSM can represent plant states, controls, disturbances, component identities, physical constraints, safety invariants, preferences, claims, evidence, failures, and revisions without confusing a model with a built vehicle.

The **Governed Meaning Base (GMB)** is the current name in the `CCF -> CMB -> GMB` lineage. GMB may carry the research objects and their standing; it does not govern a vehicle merely because the paper is indexed there. The Ableman Format Specification separates domain physics from configuration choices and realized instances. The Constitutional Observability Platform supplies an interface for evidence and operational claims. Event-Driven Craft Processes and Constitutional Reframing are comparison works, not proof that their domain analogy transfers.

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

- **Possibility:** enumerate propulsion topologies, storage combinations, controls, missions, and fuel interfaces.
- **Specification:** state physical laws, identities, safety invariants, interfaces, claim layers, and evidence requirements.
- **Configuration Manifold 1 (CM1):** retain configurations meeting mandatory physics, control, safety, emissions, authority, and verification constraints.
- **Configuration Manifold 2 (CM2):** prefer among admissible configurations by efficiency, cost, reliability, repairability, lifecycle, comfort, and sovereignty.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for one vehicle and mission family. The names are interchangeable.
- **IR:** construct an **Instance Realization** or **Implementation Realization** of that design. The names are interchangeable.
- **Evidence:** retain models, tests, failures, calibration, receipts, uncertainty, and comparisons.
- **Revision:** change models, constraints, hardware, software, and claims while preserving lineage.

This paper occupies Possibility and Specification, with preliminary CM1/CM2 criteria. It grants no IC, IR, or construction authority.

## Governed Physical-System Configuration Case

Across the completed P1 corpus, the Direct-Coupled Dynamic Torque Reactor is the **governed physical-system configuration case for hybrid torque, energy, storage, and mechanical-coupling research**. Its value to the corpus is that physical laws, safety invariants, estimator uncertainty, preferences, configuration choice, built realization, and measured evidence cannot be collapsed. It is not a demonstrated vehicle architecture, an efficiency result, or construction authorization.

- **Adjacent work:** *The Ableman Format Specification (AFS)*  
  **Supplies:** Separation of domain physics, specification, configuration, instance choice, realization, evidence, and revision.  
  **DCDTR boundary:** DCDTR supplies one domain case whose physics and safety claims must survive that separation.

- **Adjacent work:** *Admissibility Engineering*  
  **Supplies:** Pathway enumeration, constraint binding, counterexample search, and reopenable saturation.  
  **DCDTR boundary:** It tests controller, fault, power, and effect paths without proving performance.

- **Adjacent work:** *The Constitutional Observability Platform*  
  **Supplies:** Projection of state estimates, constraints, warnings, claims, and evidence.  
  **DCDTR boundary:** Displays and estimators remain fallible views of the plant.

- **Adjacent work:** *Event-Driven Craft Processes as State-Estimation Problems*  
  **Supplies:** A neighboring partially observed hybrid-state formalism.  
  **DCDTR boundary:** Shared mathematics does not transfer empirical findings across domains.

- **Adjacent work:** *Constitutionally Governed Infrastructure*  
  **Supplies:** Constitutional treatment of scheduling, allocation, liveness, and control machinery.  
  **DCDTR boundary:** DCDTR specializes those concerns to safety-critical physical energy allocation.

A bounded configuration dossier should bind:

$$
\begin{aligned}
D= (&mission, plant, components, interfaces, states, controls, \\
&disturbances, estimators, constraints, \\
&safety\_architecture, objectives, baselines, faults, \\
&evidence, unknowns)
\end{aligned}.
$$

The domain-physics layer must include energy and power conservation, component maps, thermal and mechanical limits, emissions, latency, degradation, and uncertainty. CM1 removes configurations that cannot satisfy mandatory physics and safety constraints. CM2 preferences such as efficiency, cost, repairability, fuel flexibility, comfort, or sovereignty cannot rescue a configuration excluded from CM1.

The case also sharpens the corrected funnel vocabulary. IC may mean Instance Constitution or Instance Configuration; realization-stage IR may mean Instance Realization or Implementation Realization. A simulated controller, hardware-in-the-loop bench, dynamometer assembly, and road vehicle are different IR classes with different evidence and authority. None follows automatically from a paper-level specification.

The universal GSM can type   
`MODELS_PHYSICAL_PLANT`, `SELECTS_DCDTR_CONFIGURATION`,  
`ESTIMATES_HYBRID_STATE`, `ALLOCATES_TORQUE`, `PRESERVES_ENERGY_BALANCE`,  
`VIOLATES_SAFETY_INVARIANT`, `ENTERS_DEGRADED_MODE`, `COMPARES_MATCHED_BASELINE`,  
`MEASURES_REALIZED_PERFORMANCE`,  
and   
`REMAINS_UNBUILT_PROPOSAL`. These relations make the domain case useful without laundering engineering standing.

This integration establishes four editorial commitments: retain DCDTR as the governed physical-system configuration case; adopt the configuration dossier; require separate model, simulation, bench, prototype, vehicle, and comparative-performance claims; and keep every build, safety, regulatory, or deployment act behind a separate implementation gate.

## Experience-Research Nonrelation, OS Runtime Boundary, and Governed Transformation of Physical Control

The clipped fixed-seed edge comparison with Qualia Binding and Realization Mapping, MosaiCOS, and Jnana II separates an irrelevant conceptual resemblance from two potentially useful implementation boundaries:

$$
\begin{aligned}
D^*= (&mission, plant, components, interfaces, states, controls, \\
&disturbances, estimators, constraints, safety, \\
&objectives, OS\_profile, transformation\_profile, \\
&effect\_membrane, baselines, faults, evidence, unknowns)
\end{aligned}.
$$

Qualia Binding and Realization Mapping has no material evidentiary relation to the DCDTR. Shared words such as state, dimension, binding, realization, observation, or mapping do not support a mechanical model, experience claim, control policy, or cross-domain empirical inference.

MosaiCOS could be one candidate OS environment for deterministic scheduling, capability mediation, device identity, evidence custody, bootstrap, and succession. The DCDTR controller and plant remain distinct from the OS, and no OS architecture proves timing, safety, or physical performance.

Jnana II could govern transformations to controller code, calibration, policies, models, dependencies, and effect paths through representation, law, capability, lowering, effect, witness, recovery, and exit planes. Physical construction and actuation still require a selected IC, a separately authorized IR, professional engineering review, safety analysis, hardware tests, regulation, and measured evidence.

The universal GSM can type   
`HAS_NO_MATERIAL_RELATION_TO_QUALIA_EVIDENCE`,  
`RUNS_UNDER_OS_PROFILE`, `TRANSFORMED_UNDER_JNANA_PROFILE`,  
`CROSSES_HARDWARE_EFFECT_MEMBRANE`, `REQUIRES_PHYSICAL_SAFETY_GATE`,  
and   
`REMAINS_UNBUILT_PROPOSAL`.

This randomized review establishes four editorial commitments: record the qualia comparison as an explicit nonrelation; add an OS-runtime boundary without performance implication; define a governed controller-transformation profile; and preserve every physical build, actuation, safety, and regulatory effect behind separate authority and evidence gates.

## A Cyber-Physical Realization Stress Profile

Four downstream uses position DCDTR as a stress profile rather than as evidence of a built vehicle. Jnana II tests whether governed transformation terminates at exact device capabilities, hardware identity, timing, interlocks, qualified authority, and measured plant behavior. MosaiCOS treats the controller and estimator as a cyber-physical domain profile whose effects cross an operating-system boundary. Event-driven craft work shares a partially observed hybrid-state formalism without empirical transfer. The Ableman Wheel is a distinct electromechanical case and supplies no anomaly evidence.

The cyber-physical dossier is:

$$
\begin{aligned}
D^*= (&plant\_model, hardware\_identity, controller, estimator, \\
&device\_capabilities, timing, safety\_interlocks, \\
&calibration, mission, configuration, baselines, \\
&simulation, bench, prototype, vehicle, effects, failures, \\
&degraded\_modes, evidence, revision)
\end{aligned}.
$$

Software proposal, lowering, scheduling, replay, rollback, and receipts stop at the physical boundary unless an independently observed plant result extends the evidence. Replaying controller state cannot restore torque, thermal state, stored energy, wear, emissions, or an external-world effect. A safe simulation, deterministic OS, or valid receipt cannot certify hardware timing, physical safety, or matched-mission performance.

The claim ladder must stay stage-specific: architecture, model, simulation, bench subsystem, prototype, integrated vehicle, and comparative performance are different claims with different evidence and authority. Qualia Binding and Realization Mapping remains an explicit   
`NO_MATERIAL_RELATION`; shared state, observation, dimension, or realization language transfers neither mechanical nor experiential evidence.

The universal GSM can type   
`INSTANTIATES_CYBER_PHYSICAL_STRESS_PROFILE`,  
`BINDS_CONTROLLER_TO_HARDWARE_IDENTITY`, `MEDIATES_DEVICE_CAPABILITY`,  
`OBSERVES_PLANT_EFFECT`, `CANNOT_REPLAY_PHYSICAL_STATE`, `ADVANCES_PHYSICAL_CLAIM_STAGE`,  
and   
`HAS_NO_QUALIA_EVIDENCE_RELATION`.

This reverse-dependency review establishes four editorial commitments: adopt the cyber-physical dossier; enforce the software-to-plant evidence boundary; retain the stage-specific physical claim ladder; and preserve the qualia nonrelation and all construction gates.

## 14. Counterevidence and Failure Modes

The proposal must narrow or fail where: (1) it is substantively equivalent to an existing series-hybrid profile; (2) component ratings or packaging are infeasible; (3) the viability kernel is empty for required missions; (4) controller delay destabilizes shaft dynamics; (5) virtual-inertia control amplifies noise or torsional modes; (6) bus or storage limits prevent transient buffering; (7) conversion-chain losses erase engine-island gains; (8) cold-start and aftertreatment dominate emissions; (9) optional storage adds more mass and loss than benefit; (10) software and power-electronic complexity exceeds removed mechanical complexity; (11) reliability or repairability worsens; (12) common-mode faults defeat redundancy; (13) cybersecurity creates unsafe actuation paths; (14) estimator errors violate constraints; (15) degraded modes cannot meet minimum safety; (16) fuel changes require whole-vehicle redesign; (17) V2G or heat integration accelerates degradation; (18) matched baselines outperform DCDTR; (19) lifecycle cost or environmental impact worsens; (20) users reject noise, response, or service characteristics; (21) infrastructure and certification costs dominate; (22) model uncertainty invalidates optimization; (23) constitutional language adds no testable design value; or (24) cited component and literature claims do not survive external review.

## A Governed Hybrid Architecture Remains an Unvalidated Vehicle System

### Public orientation

The Direct-Coupled Dynamic Torque Reactor proposes a thermal converter mechanically coupled to a controllable motor-generator, electrically decoupled from wheel speed, with a DC bus, traction motors, optional storage, state estimation, and constraint-aware energy management. Its constitutional framing may make objectives, constraints, faults, and evidence clearer. It does not establish novelty, feasibility, safety, efficiency, emissions benefit, or superiority to series-hybrid and range-extender designs.

### Adversarial tests

1. **Prior-art-identity attack.** New terminology obscures that the topology or control strategy is already standard, patented, commercial, or technically equivalent to an existing hybrid architecture.
2. **Programmable-inertia attack.** Fast generator torque is described as changing physical inertia rather than producing bounded closed-loop torque response with delay and saturation.
3. **Energy-accounting attack.** Conversion, storage, thermal, auxiliary, transient, and control losses disappear from system-level efficiency claims.
4. **Viability-constraint attack.** Pointwise component limits are mistaken for a controlled viability kernel under disturbances, delays, uncertainty, and failures.
5. **Drive-cycle attack.** Benefits on selected cycles or mission assumptions fail under cold start, grade, towing, heat, aging, low state of charge, or degraded operation.
6. **Fault-propagation attack.** DC-bus, inverter, isolation, cooling, storage, sensor, software, actuator, and mechanical faults combine outside the declared safety model.
7. **Storage-option attack.** Ultracapacitor, battery, flywheel, or other storage is included for conceptual completeness without mass, packaging, safety, cost, life, and maintenance justification.
8. **Governance-safety attack.** Receipts, admissibility rules, or explainable control are treated as substitutes for physical safety engineering and certification.

### Claim and evidence ceiling

The paper provides a corrected system model, claim ladder, safety obligations, and evaluation plan. It does not establish a prototype, stable controller, viable kernel, physical safety, emissions compliance, efficiency improvement, fuel flexibility, component life, cost, novelty, or comparative advantage. Reactor and programmable inertia remain bounded architectural analogies.

Any physical realization requires verified component data, prior-art and patent review, high-fidelity simulation, hardware-in-loop and fault injection, control and stability analysis, energy and emissions measurement, functional-safety engineering, regulatory review, and separately authorized construction and testing. None occurred in this pass.

### Reader-facing consequence

The proposal is best read as a transparent way to define and test an electrified torque-and-energy architecture, with ordinary hybrid baselines allowed to win and safety permitted to rule out the configuration entirely.

## 16. Conclusion

DCDTR is best understood as a candidate governed series-propulsion architecture and research program. Its central insight is useful: once thermal conversion is decoupled from wheel speed, propulsion can be designed as coordinated control of generation, storage, traction, thermal state, emissions, and mission demand rather than as refinement of one mechanical path.

The insight does not yet prove present feasibility, superiority, safety, or novelty. Those claims depend on exact topology, component maps, stable control, viable missions, matched baselines, fault behavior, lifecycle accounting, and external verification. By separating those questions and locating the work at Possibility, Specification, and early configuration analysis, the paper becomes a strong portable context artifact for disciplined engineering rather than an implicit authorization to build.

## Author-Supplied Reference Note

The source manuscript includes references in control theory, viability theory, optimal control, hybrid propulsion, power electronics, energy storage, and a companion craft-process paper. They remain author-supplied bibliography and were not externally verified in this pass. The exact source and bibliography are preserved under the custody hash above.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Instance Configuration.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** The present paper does not claim a complete revision treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that the Direct-Coupled Dynamic Torque Reactor (DCDTR) is a proposed propulsion architecture in which an internal-combustion or other thermal converter is mechanically coupled to a controllable motor-generator but decoupled from wheel speed. Its nearest external comparison fields are energy, cps. The sources in [E1], [E2], [E3], [E4], [E5], [E6] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Simulation and component analogies do not establish net energy performance, controllability, fatigue life, containment safety, or economic viability without physical validation. Runtime monitors and fallback controllers only protect modeled safety envelopes and can fail through sensor error, timing assumptions, unsafe recovery, or omitted hazards. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Thomas Bowen, Ilya Chernyakhovskiy, Kaifeng Xu, Sika Gadzanku, and Kamyria Coney. *USAID Grid-Scale Energy Storage Technologies Primer*. NREL/TP-6A20-76097, 2021. DOI: 10.2172/1808490. https://doi.org/10.2172/1808490 **Relationship:** External engineering baseline for flywheel architecture, response, lifetime, and energy-versus-power tradeoffs.

**[E2]** Thomas G. Habetler et al. "Direct Torque Control of Induction Machines Using Space Vector Modulation." *IEEE Transactions on Industry Applications* 28(5), 1992, pp. 1045-1053. DOI: 10.1109/28.158828. https://doi.org/10.1109/28.158828 **Relationship:** Predecessor electromechanical torque-control method; included to force clear differentiation from any novel reactor claim.

**[E3]** Edward R. Griffor et al. *Framework for Cyber-Physical Systems: Volume 1, Overview*. NIST SP 1500-201, 2017. DOI: 10.6028/NIST.SP.1500-201. https://doi.org/10.6028/NIST.SP.1500-201 **Relationship:** Adjacent cyber-physical systems framework for trustworthiness, timing, data, and lifecycle concerns.

**[E4]** Nancy G. Leveson and John P. Thomas. *STPA Handbook*. MIT, 2018. https://psas.scripts.mit.edu/home/books-and-handbooks/ **Relationship:** Adjacent systems-theoretic hazard analysis method; used to test treatment of unsafe control and system-level constraints.

**[E5]** J. Tanner Slagel et al. "A Formal Verification Framework for Runtime Assurance." *NASA Formal Methods*, 2024. NASA NTRS 20230017350. https://ntrs.nasa.gov/citations/20230017350 **Relationship:** Adjacent runtime-assurance formalization, useful for comparing failover safety with constitutional admission and effect recognition.

**[E6]** Robert N. M. Watson, Simon W. Moore, Peter Sewell, and Peter G. Neumann. *An Introduction to CHERI*. University of Cambridge Technical Report UCAM-CL-TR-941, 2019. DOI: 10.48456/tr-941. [cl.cam.ac.uk source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-941.html) **Relationship:** Adjacent capability architecture demonstrating unforgeable hardware authority and compartmentalization.

### Ableman corpus

**[A1]** Adam Ableman. *Constitutionally Governed Infrastructure*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-EF5747107D56F516`;  
source SHA-256  
`9C708BA381108EEA252404DF33F7B3B1648EC9CF5F2ACF00BAB88C6A15540926`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Robotics*. Ableman Corpus current edition; work identity `PAPER.PUB.18750683`;  
source SHA-256  
`D10DF9B6B7F742D9EEABF01BC5DFC3755BB4EBF548E8CB5F215BB9D94678F514`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *A Constitutional Syscall Architecture for Cyber-Physical Control Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F46D86D479F89BAC`;  
source SHA-256  
`5E696B753A10BD3C3D36B675A84B95CCF2234F024A6B277BF121E76BFCBCBD18`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Constitutional Syscalls*. Ableman Corpus current edition; work identity `PAPER.PUB.18737229`;  
source SHA-256  
`5F14356180812262778F8574C292F4F6B560993042E5358B02EAB9CF0F7DE14C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *The Ableman Wheel*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-224FDEED47E909A6`;  
source SHA-256  
`2E23634CE570B84E21854380ADD235EBF83C26C996402ADFF5EFF4A8CE329123`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Event-Driven Craft Processes as State-Estimation Problems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-45D8DDF80127D803`;  
source SHA-256  
`936C0B8B481E811D204A60C0848B406BFFC90CA7D74711DD45C6A691E1924062`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Semantic Memory Hierarchies.* Zenodo, 2026. doi:10.5281/zenodo.20793071

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

DOI: [10.5281/zenodo.23847635](https://doi.org/10.5281/zenodo.23847635)
