# The Ableman Wheel

## A Preregistered Protocol Candidate for Topology-Dependent Rotational Response Under Fast Internal Stress Modulation

### The central measurement must be angular-momentum and torque closure over a declared system boundary.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

The Ableman Wheel is a proposed experimental apparatus for asking whether a rotating electromechanical system exhibits a reproducible topology-dependent residual after known external torques, electromagnetic forces, elastic response, thermal effects, estimator behavior, and energy flow are modeled and bounded. The experiment is restricted to rotational dynamics and explicitly excludes propulsion, translation, reactionless thrust, and violations of conservation laws.

The source proposes phase inversion, continuous phase steering, coherence scrambling, graded coherence loss, topology rotation, frequency sweeps, and Delta/Amplitude-Modulated-Wye comparison as structural falsifiers. These controls are useful but not uniquely diagnostic. Driven elastic, electromagnetic, thermal, wiring, and estimator couplings can also invert, steer, preserve calibrated equivalence, or decay under scrambling. Each candidate mechanism therefore needs a quantitative prediction matrix rather than an assertion that one qualitative response eliminates it.

The central measurement must be angular-momentum and torque closure over a declared system boundary. Angular acceleration alone is insufficient. A credible protocol requires calibrated external torque, support reaction, internal momentum storage, electromagnetic energy and field coupling, translational and vibrational motion, thermal state, cable and bearing effects, measurement uncertainty, blinded randomized trials, amplitude scaling, preregistered analysis, and a declared detection limit.

This revision treats the manuscript as an experimental protocol at Specification and early configuration stages, not as a completed apparatus or test. It preserves the clean-null ambition while replacing qualitative disqualification rules with bounded hypothesis tests and evidence obligations. No experiment, simulation, construction, or external literature review was performed.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/the-ableman-`

`wheel/integration-custody-manifest.v0.1.json`,  
SHA-256  
`EC70CFCC0540AD17AC3EE3628D9718AD599AAD2D8CA6F123632CF176C998454E`. The exact source remains unchanged.

The apparatus identity, research question, named controls, jurisdictional limits, and interpretive discipline are author material. The quantitative formalism, critique of discriminator uniqueness, systematics matrix, integration surfaces, countertests, and decisions are AI editorial or synthetic additions until adopted.

No observed effect exists in the supplied evidence. "Participation" remains an operational placeholder and must not be treated as a field, substance, mechanism, anomaly, or measured parameter. Nothing here authorizes construction or operation of rotating, high-current, magnetic, or high-energy hardware.

## 1. Bounded Research Question

The protocol asks:

> After all measured external torques and modeled internal angular-momentum exchanges are included, does a preregistered topology-dependent residual remain that follows declared phase, coherence, pattern-angle, frequency, and amplitude predictions across independent sensors and control configurations?

This wording replaces the less determinate question of whether stress geometry "participates." Internal stress already participates in ordinary elastic, electromagnetic, inertial, and thermal dynamics. The empirical question is whether a reproducible residual remains outside a quantitatively bounded model.

The work does not test propulsion, translation, free energy, reactionless torque, or ontology. Translational, vibrational, and support measurements are nevertheless required as nuisance channels because excluding them from evidence would prevent them from explaining rotational artifacts.

## 2. Conservation and System Boundary

For a declared closed system boundary, angular momentum satisfies:

$$
\frac{dH_{\mathrm{sys},z}}{dt}=\tau_{\mathrm{ext},z}.
$$

$H_{\mathrm{sys},z}$ must include the rotor, wedges, actuators, relevant electromagnetic field momentum, internal moving parts, and any coupled elements inside the boundary. External torque may enter through bearings, supports, cables, air, magnetic coupling, radiation, gravity/tilt coupling, power transfer, instrumentation, or the environment.

A measurement residual may be defined as:

$$
r(t)=\tau_{\mathrm{ext,meas}}(t)-\frac{d\hat{H}_{\mathrm{model},z}(t)}{dt}.
$$

The residual is not a new effect. It is the sum of unmodeled physics, parameter error, timing error, sensor error, numerical processing, and any genuinely unexplained contribution. The protocol must reduce and bound the first classes before interpreting the last.

An Electromagnetic Rotational Transformer (EMRT) cannot enforce conservation by declaration. Its geometry, power path, reaction torques, fields, losses, control law, calibration, and uncertainty must be specified. It may help expose reaction channels, but it is itself part of the system to be modeled and tested.

## 3. Hypothesis Ladder

The source names $H_2$ without fully specifying alternatives. A preregistration should distinguish:

- **$H_0$ - bounded known response:** observations agree with a declared classical electromechanical, structural, thermal, and estimator model within uncertainty.
- **$H_1$ - unmodeled conventional coupling:** a reproducible residual exists but tracks an omitted or misestimated classical channel.
- **$H_2$ - topology-dependent unexplained residual:** after the $H_0/H_1$ mechanisms are bounded, a residual follows the preregistered topology response across independent configurations.

$H_2$ is an anomaly classification, not a mechanism or revision of conservation. Surviving qualitative controls is necessary but insufficient. Interpretation remains at $H_1$ until quantitative systematics and independent replication fail to account for the result.

## 4. Fast-Regime Definition

The source defines one ratio $\eta=\tau_{\mathrm{rise}}/\tau_{\mathrm{int}}$, but the apparatus has many electrical, magnetic, elastic, thermal, control, sampling, and structural timescales. Use a declared vector:

$$
\eta_k=\frac{\tau_{\mathrm{rise}}}{\tau_k}.
$$

"Fast" relative to mode $k$ means the chosen inequality for $\eta_k$ is satisfied with uncertainty. Fast excitation does not deny physics or averaging in general; it preferentially excites bandwidth-limited responses and may strengthen ordinary resonances, eddy-current effects, switching transients, and estimator artifacts. Frequency sweeps must therefore identify transfer functions rather than assuming smooth roll-off is exotic and narrow resonance is classical.

## 5. What the Controls Can Establish

Each control constrains mechanisms only through a quantitative prediction.

- **Control:** 180-degree phase inversion  
  **Useful observation:** odd-parity response  
  **Important surviving alternatives:** synchronous pickup, commanded torque, linear vibration

- **Control:** continuous phase steering  
  **Useful observation:** stable phase transfer  
  **Important surviving alternatives:** driven linear systems, controller coupling, demodulation

- **Control:** coherence scrambling  
  **Useful observation:** dependence on spatial coherence  
  **Important surviving alternatives:** distributed ordinary forces and coherent crosstalk

- **Control:** graded coherence loss  
  **Useful observation:** response versus coherence length  
  **Important surviving alternatives:** array-factor and signal-processing effects

- **Control:** topology rotation  
  **Useful observation:** response follows commanded pattern angle  
  **Important surviving alternatives:** rotating fields, cable geometry, sensor cross-axis response

- **Control:** frequency sweep  
  **Useful observation:** transfer-function structure  
  **Important surviving alternatives:** structural, electrical, thermal, and control dynamics

- **Control:** Delta/AM-Wye comparison  
  **Useful observation:** response under calibrated field equivalence  
  **Important surviving alternatives:** mechanisms shared by the calibrated field pattern

No single failure automatically rejects every meaningful topology-dependent model, and no single success excludes every artifact. The expected parity and scaling of $H_2$ must be derived before data. If an alleged response is even under phase, phase inversion is not the right falsifier; if it is odd, the same behavior may be shared by ordinary synchronous coupling.

## 6. Delta and AM-Wye Equivalence

Electrical labels do not establish physical equivalence. A defensible comparison must demonstrate, within uncertainty, equivalence of the intended spatiotemporal field or stress distribution while separately measuring:

- current and voltage waveforms;
- phase and harmonic content;
- magnetic field maps and leakage;
- stored and dissipated energy;
- thermal gradients;
- force and torque on wiring, stator, support, and rotor;
- switching common mode and EMI; and
- controller timing and sensor coupling.

If these quantities differ, failure of equivalence is not automatically evidence against topology dependence. If they match, ordinary mechanisms driven by the same field geometry may also match. The comparison is a powerful identity check only after the equivalence relation and tolerances are declared.

## 7. Measurement and Apparatus Obligations

The protocol needs more than encoder and IMU acceleration:

1. calibrated applied and reaction torque measurement;
2. encoder, IMU, and independent angular-position channels;
3. translational acceleration, tilt, bearing load, and support vibration;
4. current, voltage, power, field, and thermal measurements;
5. cable, slip-ring, wireless-power, and controller reaction characterization;
6. fixed clocks with measured synchronization and jitter;
7. raw-data retention before filtering or differentiation;
8. fixed analysis code and synthetic-signal validation;
9. rotor balance and structural modal characterization;
10. environmental magnetic, acoustic, airflow, and temperature monitoring; and
11. exact configuration, firmware, calibration, and component custody.

Encoder differentiation can manufacture phase and amplitude structure. The estimator pipeline must be preregistered, independently implemented, tested on injected signals, and checked against torque and support measurements.

## 8. Experimental Design

A credible sequence is:

1. publish the system boundary, equations, $H_0/H_1/H_2$ predictions, and safety envelope;
2. simulate classical electromechanical and structural response with uncertainty;
3. characterize every transfer path with the rotor stationary and rotating;
4. run sham patterns with identical power, heat, timing, and spectral content;
5. randomize and blind condition labels through acquisition and primary analysis;
6. reverse rotation and pattern direction independently;
7. swap wiring, controllers, sensors, materials, and actuator positions;
8. scan amplitude as well as phase, coherence, angle, and frequency;
9. repeat across speeds, temperatures, vacuum/enclosure states where safe, and independent builds;
10. hold out confirmatory conditions after exploratory work; and
11. seek independent replication before interpretive escalation.

The primary outcome must specify effect window, estimator, effect size, uncertainty, multiple-comparison control, exclusion thresholds, and stopping rule. A null result produces a bound only if sensitivity and model coverage are quantified.

## 9. Safety and Authority Boundary

Rotating assemblies, magnetic fields, stored electrical energy, high current, heating, containment, and fragments can cause serious harm. A real protocol requires professional mechanical and electrical review, rated containment, overspeed protection, emergency shutdown, remote operation, interlocks, fire controls, isolation, and jurisdiction-appropriate approvals.

This paper is a research specification. It is not a construction drawing, risk assessment, operating procedure, certification, or authorization to build or energize the apparatus.

## 10. Corpus Integration

The Ableman Wheel is a physical-domain application of **Admissibility Engineering**: hypotheses, signals, and interpretations pass declared gates. **Constitutional Reframing** separates the inherited question from the measurable state, control, evidence, and refusal surfaces. **Semantic Manifold Topology** helps distinguish electrical encoding, field geometry, stress distribution, measurement, residual, and interpretation without declaring them equivalent.

**Reasoning by Way of Receipts** can bind configuration, calibration, trial, analysis, and result; receipt existence does not prove physical truth. **Warrant by Structure** requires effect evidence and closure rather than a well-formed record alone. The **Direct-Coupled Dynamic Torque Reactor** is an adjacent electromechanical state-space proposal and supplies no experimental evidence for this apparatus.

The **Governed Meaning Base (GMB)** is the current name in the `CCF -> CMB -> GMB` lineage. It can preserve hypotheses, apparatus identities, configurations, trials, raw data, analyses, nulls, anomalies, replications, and standing. Inclusion does not validate an effect.

## 11. Realization Funnel

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

- **Possibility:** enumerate apparatus geometries, conventional mechanisms, response symmetries, and measurements.
- **Specification:** define boundary, hypotheses, models, controls, safety, metrology, statistics, and claim ceilings.
- **Configuration Manifold 1 (CM1):** retain designs satisfying conservation, measurement, safety, calibration, and falsifiability constraints.
- **Configuration Manifold 2 (CM2):** prefer among admissible designs by sensitivity, discriminator power, inspectability, cost, repairability, and replication value.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for one apparatus and protocol. The names are interchangeable.
- **IR:** construct an **Instance Realization** or **Implementation Realization** of that apparatus. The names are interchangeable.
- **Evidence:** retain exact builds, calibrations, raw data, nulls, failures, analyses, and independent replications.
- **Revision:** update models, hardware, protocol, or standing while preserving lineage.

The paper reaches Specification and early CM1/CM2 design. It does not establish an IC, IR, constructed apparatus, completed test, anomaly, or implementation authority.

## Governed Physical-Anomaly Protocol

Across the completed P1 corpus, The Ableman Wheel is the **governed physical-anomaly protocol for a topology-dependent rotational residual under conservation, metrology, blinding, safety, and claim-escalation constraints**. It is valuable as a rigorously bounded experimental question, not as evidence of propulsion, new physics, free energy, or a constructed apparatus.

- **Adjacent work:** *Admissibility Engineering*  
  **Supplies:** Constraint-bound experimental pathways and reopenable saturation claims.  
  **Wheel-paper boundary:** The Wheel applies those disciplines to one physical anomaly protocol.

- **Adjacent work:** *Direct-Coupled Dynamic Torque Reactor*  
  **Supplies:** An adjacent electromechanical configuration and control research case.  
  **Wheel-paper boundary:** It supplies no evidence for the Wheel and remains physically distinct.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed instrument, laboratory, operator, and independent replication observations.  
  **Wheel-paper boundary:** Witnesses support bounded measurements without deciding mechanism.

- **Adjacent work:** *Testing for Deriving Observable State of Software Systems*  
  **Supplies:** Evidence-path and oracle assurance logic.  
  **Wheel-paper boundary:** The Wheel specializes evidence-path testing to clocks, sensors, fields, torque, motion, and analysis.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Exact custody of configuration, calibration, run, analysis, result, and revision.  
  **Wheel-paper boundary:** Receipt integrity cannot turn a residual into new physics.

Each preregistered run should bind:

$$
\begin{aligned}
R= (&apparatus, boundary, configuration, controls, \\
&calibration, condition, randomization, blinding, sensors, \\
&raw\_data, analysis, uncertainty, safety, result, \\
&interpretation)
\end{aligned}.
$$

Claim escalation should proceed from `MODEL_CONSISTENT`, `UNRESOLVED_SYSTEMATIC`,  
`REPRODUCIBLE_RESIDUAL`, `TOPOLOGY_ASSOCIATED_RESIDUAL`, `INDEPENDENTLY_REPLICATED_ANOMALY`,  
and only then to a separately justified mechanism proposal. No stage licenses a conservation violation or ontology claim. A null result earns a bound only for the demonstrated sensitivity and covered mechanisms.

Apparatus identity, topology condition, field or stress equivalence, sensor independence, analysis version, and safety state must be exact. Phase, coherence, pattern angle, frequency, and amplitude predictions should be frozen before confirmatory data. Conventional coupling models remain active competitors after qualitative controls and even after initial replication.

The universal GSM can type   
`CONFIGURES_ABLEMAN_WHEEL_PROTOCOL`,  
`BOUNDS_ANGULAR_MOMENTUM_SYSTEM`, `APPLIES_TOPOLOGY_CONDITION`, `MEASURES_REACTION_TORQUE`,  
`CONTROLS_CONVENTIONAL_COUPLING`, `OBSERVES_RESIDUAL_WITH_UNCERTAINTY`,  
`BLINDS_CONFIRMATORY_ANALYSIS`, `REPLICATES_INDEPENDENTLY`, `RETAINS_ANOMALY_STANDING`,  
and   
`DOES_NOT_AUTHORIZE_CONSTRUCTION`. These relations keep physical evidence and interpretation separated.

This integration establishes four editorial commitments: retain the work as the governed physical-anomaly protocol; adopt the run envelope and six-stage claim ladder; require exact apparatus, prediction, equivalence, metrology, blinding, and safety custody; and prohibit escalation from residual to mechanism, conservation revision, or construction without separate evidence and authority.

## Specification-to-Apparatus Trace Without Construction Authority

The fixed-seed comparison with *Meaning as Binding*, the Jnana open-source projection, *The Implementation Codex*, and HLIR exposes a useful realization interface and two false adjacencies. A physical protocol can be made more inspectable by tracing a human-readable proposal through a selected configuration into an exact apparatus and analysis realization:

$$
\begin{aligned}
A= (&HLIR\_proposal, specification, CM1, CM2, IC, \\
&realization\_package, IR, run\_evidence, revision)
\end{aligned}.
$$

HLIR can express alternative apparatus boundaries, controls, predictions, ambiguity, authority references, and evidence needs for human review. The Implementation Codex can bind a selected Instance Constitution / Instance Configuration to parts, dependencies, build phases, calibration, safety gates, software, analysis, and evidence. Neither artifact authorizes construction, operation, human-subject involvement, environmental effect, or a physical claim.

The realized apparatus must remain traceable to the selected configuration while recording deviations, substitutions, interventions, and unmodeled remainder. Passing document or build gates establishes only the tested correspondence claims. It does not establish the anomaly, mechanism, conservation revision, safety, or independent replication.

The adjacencies to *Meaning as Binding* and Jnana produce   
`NO_MATERIAL_RELATION` for the physical hypothesis. Semantic phase/coherence metaphors provide no physical evidence, and a constitutional software substrate provides no Wheel result. General governance components may support custody, but that is an implementation option rather than a domain-theory bridge.

The universal GSM can type   
`PROPOSES_APPARATUS_IN_HLIR`,  
`SELECTS_WHEEL_INSTANCE_CONFIGURATION`, `PACKAGES_APPARATUS_REALIZATION`,  
`DEVIATES_FROM_FROZEN_CONFIGURATION`, `EVIDENCES_RUN_UNDER_REALIZATION`,  
`DOES_NOT_AUTHORIZE_CONSTRUCTION`,  
and   
`HAS_NO_PHYSICAL_EVIDENCE_FROM_SEMANTIC_OR_`  
`JNANA_ADJACENCY`.

This randomized review establishes four editorial commitments: adopt the specification-to-apparatus trace; use HLIR and the Implementation Codex only as non-authorizing proposal and realization interfaces; require exact deviation and substitution records; and enforce metaphor/software firebreaks around the physical hypothesis.

## A Frozen Experiment Dossier Without Construction Authority

Two material downstream uses connect the Ableman Wheel to the realization funnel without granting physical standing. HLIR uses it as a demanding proposal and review case for alternative apparatus configurations, controls, predictions, safety, and evidence needs. The Implementation Codex uses it as a domain profile for converting one selected configuration into a traceable build and experiment package while preserving as-built deviations and new discoveries.

The portable experiment dossier is:

$$
\begin{aligned}
E^*= (&question, hypotheses, apparatus\_alternatives, \\
&selected\_IC, authority, safety, parts, calibration, \\
&controls, predictions, build\_package, as\_built\_diff, \\
&runs, raw\_data, blinding, analysis, verdict, remainder, \\
&revision)
\end{aligned}.
$$

HLIR should preserve ambiguity, competing explanations, and unresolved requirements until an authorized reviewer selects an IC. The Implementation Codex should bind drawings, parts, tolerances, firmware, instrumentation, calibration, procedures, hazards, stop conditions, and analysis code to that selection. Neither artifact authorizes procurement, construction, energization, operation, or human exposure. Those remain separate explicit gates.

The broader search also confirms two nonrelations. The Jnana open-source contribution path supplies no physical evidence or build authority for the Wheel. *Meaning as Binding* shares vocabulary such as phase, coherence, field, and binding but supplies no electromechanical mechanism, measurement, or anomaly evidence. Those firebreaks should remain visible.

The universal GSM can type   
`PROPOSES_APPARATUS_ALTERNATIVE`, `SELECTS_EXPERIMENT_IC`,  
`COMPILES_TO_BUILD_DOSSIER`, `RECORDS_AS_BUILT_DEVIATION`, `BINDS_RUN_TO_CALIBRATION`,  
`WITHHOLDS_CONSTRUCTION_AUTHORITY`,  
and   
`HAS_NO_PHYSICAL_EVIDENCE_FROM_SEMANTIC_`  
`METAPHOR`.

This reverse-dependency review establishes four editorial commitments: adopt the frozen experiment dossier; preserve proposal ambiguity through HLIR until IC selection; bind every build and run to as-built deviations and calibration; and retain explicit construction and metaphor firebreaks.

## 12. Counterevidence and Failure Modes

The protocol must narrow or fail where: (1) $H_2$ has no quantitative prediction; (2) internal stress is not distinguished from ordinary dynamics; (3) the system boundary omits a reaction path; (4) applied torque is not measured; (5) EMRT behavior is unspecified; (6) field or cable coupling explains the residual; (7) translation, tilt, vibration, or bearings explain rotation; (8) encoder filtering manufactures the phase signature; (9) independent sensors share a clock or EMI defect; (10) phase inversion is reproduced by synchronous artifact; (11) scrambling reduces ordinary coherent forces; (12) topology rotation tracks wiring or field geometry; (13) Delta/AM-Wye fields are not equivalent; (14) equivalent fields make ordinary mechanisms equivalent too; (15) frequency response reveals structural or control modes; (16) response lacks stable amplitude scaling; (17) thermal drift predicts the effect; (18) residual vanishes after system identification; (19) randomization or blinding removes the signal; (20) effect size falls below preregistered sensitivity; (21) multiple-comparison correction removes significance; (22) null sensitivity is insufficient for a bound; (23) a second build does not reproduce; (24) independent replication fails; (25) safety constraints prevent the required regime; or (26) external literature shows the response is already expected.

## A Residual Is a Measurement Problem Before It Is a New Mechanism

### Public orientation

The Ableman Wheel is a preregistered experimental-protocol candidate for detecting a topology-dependent rotational residual after ordinary torque, momentum, electromagnetic, elastic, thermal, vibrational, estimator, and environmental effects are modeled. It is not a propulsion device, reactionless-thrust claim, free-energy proposal, observed anomaly, or implemented apparatus.

### Adversarial tests

1. **Boundary-leak attack.** Cables, bearings, supports, air, fields, power transfer, gravity, tilt, radiation, instrumentation, or nearby structures exchange torque or momentum across the declared boundary.
2. **Estimator-residual attack.** Filtering, phase alignment, differentiation, calibration, synchronization, saturation, drift, or model fitting creates the residual.
3. **Elastic-electromagnetic mimic attack.** Ordinary driven coupling follows phase, topology, coherence, frequency, or amplitude controls that were claimed to be unique.
4. **AM-Wye-mismatch attack.** Compared configurations differ in field distribution, impedance, harmonics, heating, wiring geometry, or mechanical loading despite nominal calibration.
5. **Multiple-testing attack.** Flexible windows, frequencies, phases, exclusions, or summary metrics produce a selected anomaly.
6. **Sensor-common-mode attack.** Apparently independent sensors share mounting, timing, processing, environment, power, or calibration error.
7. **Energy-closure attack.** A rotational signal is discussed without complete energy, torque, angular-momentum, translation, and internal-storage accounting.
8. **Safety-escalation attack.** An intriguing preliminary residual justifies higher speed, current, field, stored energy, or hardware modification without a new authority gate.

### Claim and evidence ceiling

The paper specifies a bounded question, controls, measurement obligations, and a hypothesis ladder. It reports no apparatus, simulation, residual, anomaly, field, mechanism, propulsion, translation, conservation violation, or evidence for the operational placeholder participation. Qualitative inversion, steering, scrambling, or coherence effects are not uniquely diagnostic.

Any experiment requires qualified mechanical, electrical, magnetic, fire, facility, instrumentation, and occupational-safety review; preregistration; independent calibration; blinded randomized trials; quantitative nuisance predictions; declared detection limits; and separate construction and operating authority. None was granted here.

### Reader-facing consequence

The responsible path is to make ordinary explanations quantitatively capable of winning, define in advance what would count as a bounded residual, and stop at a null result without turning apparatus complexity into evidence.

## 14. Conclusion

The Ableman Wheel is strongest as a disciplined question. Its value lies in forcing geometry, configuration, measurement, response, and interpretation to remain separate while designing results that can fail cleanly.

That discipline requires more than elegant symmetry controls. It requires a closed accounting boundary, quantitative conventional predictions, independent measurements, declared uncertainty, blinded trials, sensitivity, and replication. If no residual survives, the null is informative only to the achieved bound. If one survives, it is first an anomaly requiring stronger classical and experimental challenge - not a licensed ontology.

The apparatus may be complete as a question. It is not yet complete as an experiment.

## Reference and Verification Note

The source manuscript supplies no bibliography. A future evidence-qualified edition should bind relevant primary literature in rotational dynamics, electromagnetic forces and field momentum, magnetostriction, rotor metrology, system identification, null experiments, statistical preregistration, and apparatus safety. No such external review was performed here.

## Corpus-Wide Reference Positioning

This paper argues that the Ableman Wheel is a proposed experimental apparatus for asking whether a rotating electromechanical system exhibits a reproducible topology-dependent residual after known external torques, electromagnetic forces, elastic response, thermal effects, estimator behavior, and energy flow are modeled and bounded. Its nearest external comparison fields are governance, semantic, formal. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E2]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E3]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Richard Cyganiak, David Wood, and Markus Lanthaler, eds. *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation, 25 February 2014. https://www.w3.org/TR/rdf11-concepts/ **Relationship:** Adjacent graph data model and identity baseline.

**[E6]** Alistair Miles and Sean Bechhofer, eds. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. https://www.w3.org/TR/skos-reference **Relationship:** Adjacent standard for concepts, labels, schemes, notes, and semantic mappings.

**[E7]** W3C OWL Working Group. *OWL 2 Web Ontology Language Document Overview*, Second Edition. W3C Recommendation, 11 December 2012. https://www.w3.org/TR/owl2-overview/ **Relationship:** Adjacent formal ontology standard used to compare declared semantics and inference commitments.

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

**[A6]** Adam Ableman. *Meaning as Binding*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-5F976917F0B283EA`;  
source SHA-256  
`A470D1A0B9ED7C3CEAB6BB88BE4B642A2BA36427447F787764329FD574DA0C97`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D95CCC4FB7B58BFB`;  
source SHA-256  
`A3B62E50F8BEE125FDAE0D38C2839AFD1CCC138296268BF93217481E38AA48EA`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Semantic Manifold Topology.* Zenodo, 2026. doi:10.5281/zenodo.20257244

Adam Ableman *Semantic Memory Hierarchies.* Zenodo, 2026. doi:10.5281/zenodo.20793071

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848339](https://doi.org/10.5281/zenodo.23848339)
