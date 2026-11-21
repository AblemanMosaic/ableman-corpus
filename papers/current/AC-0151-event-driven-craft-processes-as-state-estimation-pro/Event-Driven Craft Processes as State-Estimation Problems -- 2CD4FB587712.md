# Event-Driven Craft Processes as State-Estimation Problems

## Observability, Viability Constraints, and Latent-State Control in Traditional Craft Practice

### The estimator is the practitioner or algorithm that maps observation and action history into a state estimate.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Traditional crafts often organize continuous or hybrid developmental processes around discrete landmarks: crack in coffee roasting, spring in bread baking, foam transitions in fermentation, gelation in cheesemaking, cone behavior in ceramics, snap in curing, and color changes in heat treatment. This paper proposes that such landmarks should be analyzed as observations of latent process trajectories before they are assumed to be developmental causes.

The distinction requires care. A physical transition is not the same object as a sensor signal; a signal is not the same object as a culturally named landmark; and none of these is itself a state estimator. The estimator is the practitioner or algorithm that maps observation and action history into a state estimate. Some physical events may also change the process, so causal mechanism and informational proxy are not mutually exclusive.

The framework treats craft as partially observed, viability-constrained, hybrid control. It asks whether a traditional landmark carries replaceable information, marks an unavoidable causal transition, identifies one of several viable routes, or accompanies outputs that mask other valued characteristics. Those questions are domain-specific and require controlled intervention, matched outcomes, practitioner validation, and explicit uncertainty.

This revision repairs the event/estimator category error; separates state, control, disturbance, measurement, and landmark classification; distinguishes a safe constraint set from its viability kernel; makes instrumentation and linguistic-transmission claims empirical rather than automatic; integrates human validation, Semantic Manifold Topology, GMB/GSM, and the realization funnel; and supplies a comparative research protocol. No domain experiment or external literature verification was performed.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/event-`

`driven-craft-processes-as-state-estimation-`  
`problems/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`C2F684B530C9108A902CC7152109AF26828E533AEBDD8612354DA97D99A0528D`. The exact source remains unchanged.

The paper's thesis, layered proposal, craft examples, explanatory voice, falsification program, and bibliography are author material. The repaired formal model, sharper claims, integration surfaces, countertests, and decisions are AI editorial or synthetic additions until adopted.

The examples are hypotheses and author interpretations, not evidence that every named event is replaceable, noncausal, masking, or controllable. No craft tradition, practitioner, or community is treated as having endorsed this synthesis. Nothing here authorizes intervention in food, fermentation, kilns, heat treatment, or other safety-relevant processes.

## 1. The Conceptual Entry Point

Traditional event-centered language can perform at least four functions:

1. operational cue for intervention;
2. evidence about latent developmental state;
3. teaching and coordination token;
4. culturally stabilized compression of multimodal expertise.

These functions do not determine whether the underlying physical transition is causal. A crack may be easy to hear and causally relevant; a cone may integrate thermal work while also undergoing its own material transformation; visible spring may reveal gas expansion while participating in structural change. The first question is therefore not "event or mechanism?" but:

> Which physical transition occurred, what was actually observed, how was the landmark classified, what latent variables did it inform, and what causal role did the transition play?

## 2. Five Objects That Must Not Be Collapsed

**Latent process state.** The thermodynamic, chemical, biological, structural, rheological, perceptual, and historical variables needed for the domain model.

**Physical event or transition.** A threshold crossing, phase change, fracture, jump, onset, collapse, or other change in the process itself.

**Measurement.** Acoustic, visual, olfactory, tactile, chemical, thermal, temporal, or instrumental output produced by the process and sensing channel.

**Cultural landmark.** A classified and named pattern in observation history used by a craft tradition for teaching, coordination, or control.

**Estimator.** A practitioner, community method, statistical procedure, or algorithm that maps observation and intervention history into an estimate of latent state.

Calling an event a "state estimator" collapses the last four objects. The corrected claim is that a traditional event or landmark can be an informative measurement used by a practitioner-estimator.

## 3. Hybrid State-Space Model

Let $x(t)$ be latent process state, $u(t)$ deliberate control, $d(t)$ disturbance and environmental input, $\theta$ uncertain parameters, and $y(t)$ observations:

$$
\dot{x}=f_q(x,u,d;\theta)+w,
$$

$$
y=h_q(x,u,d;\theta)+v.
$$

$q$ denotes a discrete process mode, while $w$ and $v$ represent process and observation uncertainty. A physical event surface may be defined by:

$$
g_j(x,u,d;\theta)=0,
$$

with crossing direction, dwell, hysteresis, and reset behavior specified. If the event changes the process, hybrid dynamics permit:

$$
x^+=R_j(x^-,u,d;\theta).
$$

An observed landmark is a classification over measurement history, not the event surface itself:

$$
\ell_j(t)=C_j(y_{[0:t]},u_{[0:t]},c),
$$

where $c$ includes practitioner, instrument, environment, and cultural context. The state estimator is:

$$
\hat{x}(t)=\Phi(y_{[0:t]},u_{[0:t]},c).
$$

This model permits four possibilities: a landmark accurately detects a causal transition; it detects a noncausal correlate; it imperfectly detects a transition; or it reflects classification convention more than stable process structure.

## 4. Viability and Objective

A constraint set is:

$$
K=\{x:\ c_i(x,u,d)\leq 0\ \text{for all mandatory constraints}\}.
$$

It is not automatically the viability kernel. The controlled viability kernel is the subset of states from which some admissible policy can keep the process in $K$ for the required horizon:

$$
\mathrm{Viab}(K)=\{x_0:\exists u(\cdot)\ \text{such that}\ x(t)\in K\ \text{for all required }t\}.
$$

A domain instance must define target outcome $x_T$, path qualities, losses, uncertainty, safety constraints, and practitioner values. A generic objective is:

$$
\min_{u(\cdot)}
\left[
\phi(x(T),x_T)+\int_0^T L(x,u,d)\,dt
\right]
$$

subject to the dynamics, $x(t)\in K$, actuator limits, and uncertainty. The formalism does not tell a community what qualities to value; those enter through an explicit, contestable domain profile.

## 5. Revised Claim Ladder

The source's three layers are preserved but decomposed into five independently testable claims:

1. **Information:** the landmark predicts one or more latent variables or outcomes under specified conditions.
2. **Substitution:** another observation history or estimator supplies comparable decision-relevant information.
3. **Alternative feasibility:** a safe, controllable trajectory reaches a declared target while avoiding, delaying, or changing the event-generating region.
4. **Outcome equivalence or improvement:** blinded or otherwise bounded evaluation finds the alternative comparable or preferable on declared criteria.
5. **Masking:** a named event-associated output causally reduces access to another defined characteristic, and reducing that output restores access.

Information does not establish substitution. Substitution does not establish alternative feasibility. Feasibility does not establish equal quality. Equal quality does not establish masking. A physical event can be an informative proxy and a causal mechanism simultaneously.

Layer 1 in the source corresponds mainly to Claims 3 and 4. Layer 2 corresponds to Claims 1 and 2 but must not presume noncausality. Layer 3 corresponds to Claim 5 and carries the highest domain-specific evidentiary burden.

## 6. What "Suppressing the Event" Can Mean

Experimental designs must distinguish:

- disabling or ignoring the sensor;
- changing the landmark classifier or threshold;
- reducing the observed signal while preserving the physical transition;
- avoiding the physical event surface;
- traversing the same region with different rate or residence time;
- changing the process so the event has a different causal role; and
- reaching a different final state that merely receives the same verbal quality label.

These interventions are not equivalent. A no-crack signal does not prove that fracture-related latent transitions were absent. A low-spring loaf does not prove equivalent internal development. A cone replacement does not prove identical ware transformation. The intervention, state claim, and outcome equivalence must each have evidence.

## 7. Observability, Identifiability, and Instrumentation

More sensors do not automatically make a process observable. Signals may be redundant, noisy, delayed, confounded, poorly calibrated, or insensitive to the variables of interest. Mathematical observability depends on the model and input history; practical state reconstruction also depends on parameter identifiability, excitation, sensor placement, and uncertainty.

Instrumentation can also change the process through sampling, probes, airflow, thermal mass, lighting, handling, or feedback. The claim that "the latent process remains the same" therefore requires a noninterference argument or measurement of perturbation.

Traditional multimodal practice should not be treated as an inferior precursor to instrumentation. An expert may integrate smell, touch, sound, timing, material history, social judgment, and active probing in ways a sensor suite does not reproduce. Instrumentation and practitioner estimation should be compared, combined, and challenged rather than placed in a simple replacement sequence.

## 8. Communication and Event Compression

The event-compression hypothesis is one of the paper's strongest pedagogical ideas: discrete landmarks can compress a high-dimensional trajectory into memorable, teachable tokens. But its historical and cross-cultural scope remains empirical.

Written texts, oral teaching, demonstration, apprenticeship, gesture, metaphor, shared materials, and sensory vocabulary transmit different information. Difficulty naming odors in one linguistic community does not establish that olfactory knowledge is universally linguistically unstable. The cited linguistic literature must be interpreted with attention to language and culture, and it does not by itself prove why a particular craft canon privileged an event.

A comparative study should examine actual manuals, oral instruction, practitioner interviews, vocabulary, error correction, and learning outcomes. The hypothesis predicts that culturally central landmarks will score highly on recognizability, coordination value, and transmission stability, but may discard continuous state information recoverable through apprenticeship or instrumentation.

## 9. Domain Profiles and Worked Examples

The framework is an architecture for comparison, not a transfer of conclusions among domains. Each craft needs a profile containing:

- target community and practice;
- exact physical event and observed landmark;
- candidate state variables and uncertainties;
- controls, disturbances, and safety constraints;
- practitioner estimator and instrumental estimator;
- causal hypotheses and alternative trajectories;
- outcome definitions and sensory or material evaluation;
- cultural and historical evidence;
- failure, harm, and refusal conditions; and
- data ownership, consent, and attribution.

**Coffee roasting** is the author's most developed companion case and should carry the detailed empirical burden for crack avoidance and masking. **Bread baking** remains a hypothesis generator: oven spring combines measurement and mechanism, and no masking result is claimed. **Wood-fired ceramics** illustrates how an artifact such as a cone may integrate thermal work, but ware, cone, atmosphere, and kiln sensing are not interchangeable state surfaces. Cross-craft similarity supports a research program, not a shared causal conclusion.

## 10. Practitioner Knowledge and Human Validation

Expertise may include state estimation, but it also includes action selection, active sensing, embodied calibration, material memory, aesthetic judgment, normative choice, repair, and social accountability. Reducing expertise to reconstruction alone would discard what the formalism is meant to illuminate.

The Human Validation Layer provides an interface: practitioners participate in defining variables, outcomes, vocabulary, acceptable interventions, and interpretation. Their testimony is evidence with scope, not automatic truth; the mathematical model is a projection with scope, not authority over the practice. Disagreement should remain visible rather than averaged into a fictional consensus.

## 11. Evaluation Program

For one bounded craft/event pair:

1. define the physical transition, observed signal, landmark rule, and target outcome;
2. elicit practitioner models and failure boundaries;
3. instrument the process while testing sensor perturbation and calibration;
4. estimate repeatability, false-positive, and false-negative rates for the landmark;
5. fit or propose a state model with explicit uncertainty;
6. compare event-only, multimodal-practitioner, instrument-only, and fused estimators;
7. design interventions that separately manipulate signal, classifier, event region, and residence time;
8. test feasibility and safety before outcome preference;
9. use blinded sensory or material evaluation where applicable;
10. test causal masking with named outputs and mediators;
11. repeat across practitioners, materials, devices, and contexts; and
12. publish failures, model limits, and conditions of non-transfer.

Layered evidence should distinguish observational correlation, predictive validity, intervention, causal mediation, and cross-domain replication.

## 12. Universal GSM and Realization Funnel

The universal GSM can represent process state, mode, control, disturbance, measurement, event surface, landmark classifier, estimator, practitioner, tradition, target, constraint, viability kernel, causal hypothesis, masking relation, evidence, and revision without confusing them.

The **Governed Meaning Base (GMB)** is the current name in the `CCF -> CMB -> GMB` lineage. It can preserve domain profiles, sources, observations, models, disputes, and standing; inclusion does not validate a craft claim. Semantic Manifold Topology supplies continuity questions across latent state, observation, landmark, text, and intervention. Constitutional Reframing supplies the shift from inherited event-centered language to declared state/control/evidence structure. The Direct-Coupled Dynamic Torque Reactor is an adjacent state-space application, not evidence for craft domains.

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

- **Possibility:** enumerate physical processes, observations, estimators, trajectories, outcomes, and craft interpretations.
- **Specification:** define state, controls, disturbances, event surfaces, landmarks, constraints, targets, and evidence.
- **Configuration Manifold 1 (CM1):** retain profiles and trajectories satisfying safety, feasibility, authority, consent, and measurement constraints.
- **Configuration Manifold 2 (CM2):** prefer among admissible approaches by quality, robustness, learning value, accessibility, cost, cultural fit, and practitioner judgment.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for one craft, material, apparatus, community, and study. The names are interchangeable.
- **IR:** construct an **Instance Realization** or **Implementation Realization** of that study or process. The names are interchangeable.
- **Evidence:** retain observations, calibration, outcomes, failures, panels, practitioner testimony, and model uncertainty.
- **Revision:** update the model, terminology, process, and standing while preserving lineage.

The paper reaches Specification and sketches comparative CM1/CM2 criteria. The worked examples are hypotheses, not ICs, IRs, validated domain models, or implementation authority.

## Practitioner-Governed State-Estimation Research Pattern

Across the completed P1 corpus, Event-Driven Craft Processes as State-Estimation Problems is the **practitioner-governed research pattern for testing whether named craft events are signals, transitions, causal mechanisms, compressed teaching landmarks, or combinations of these**. It offers a comparative formal vocabulary while requiring domain experts to define quality, safety, tradition, and useful intervention. It is not a universal reduction of craft to control theory.

- **Adjacent work:** *Semantic Field Analysis*  
  **Supplies:** A method for mapping entities, relations, authority, evidence, and hidden assumptions before synthesis.  
  **Craft-paper boundary:** Each craft requires its own field analysis before variables can be compared.

- **Adjacent work:** *Human Validation Layer: Constitutional Coherence Through Human-Governed Refinement*  
  **Supplies:** Human adjudication of meaning, coherence, and revision.  
  **Craft-paper boundary:** Practitioner validation is constitutive evidence, not decorative review after modeling.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed observations with declared competence, scope, and limits.  
  **Craft-paper boundary:** Instrument readings and practitioner testimony remain different witness classes.

- **Adjacent work:** *Direct-Coupled Dynamic Torque Reactor*  
  **Supplies:** An adjacent hybrid state-space and viability application.  
  **Craft-paper boundary:** Mathematical adjacency does not establish domain equivalence or shared evidence.

- **Adjacent work:** *Semantic Legitimacy Before Context*  
  **Supplies:** Purpose-bounded admission of sources and observations.  
  **Craft-paper boundary:** Oral, embodied, local, and instrument evidence must retain standing without forced homogenization.

A domain profile should bind:

$$
\begin{aligned}
P= (&craft, community, target, state\_hypothesis, controls, \\
&disturbances, event\_surface, signals, landmark, \\
&causal\_role, estimators, viability, interventions, \\
&witnesses, evidence, limits)
\end{aligned}.
$$

The intervention question is not merely whether the named event can be suppressed. Candidate studies should separately test signal substitution, threshold shift, trajectory change, event avoidance, landmark replacement, and teaching-language change. Outcome equivalence must be defined by practitioners and, where appropriate, blinded or instrumented comparison.

Formalization may improve prediction while damaging transmission, access, labor conditions, cultural authority, or the craft's own account of quality. These are not external objections to be noted after technical success; they are CM1/CM2 constraints and evaluation dimensions. A model that cannot represent practitioner disagreement should preserve disagreement rather than average it into false consensus.

The universal GSM can type   
`PROFILES_CRAFT_DOMAIN`, `OBSERVES_EVENT_SIGNAL`,  
`CROSSES_EVENT_SURFACE`, `CLASSIFIES_PRACTITIONER_LANDMARK`,  
`ESTIMATES_LATENT_PROCESS_STATE`, `ATTRIBUTES_CAUSAL_ROLE`,  
`PRESERVES_PRACTITIONER_DISAGREEMENT`, `TESTS_SIGNAL_SUBSTITUTION`,  
`COMPARES_OUTCOME_EQUIVALENCE`,  
and   
`REMAINS_DOMAIN_SPECIFIC`. These relations let the paper generalize a research method without appropriating domain authority.

This integration establishes four editorial commitments: classify the paper as a practitioner-governed state-estimation research pattern; adopt the domain-profile envelope; require intervention-specific and practitioner-defined outcome tests; and treat embodied knowledge, cultural authority, access, labor, and disagreement as first-class constraints rather than residual commentary.

## Profiled Practitioner Evidence and Quantitative Nonrelation

The fixed-seed comparison with AFS, HVL, historical CCF, and ACG for Quants gives each craft study a governed evidence path without reducing it to a generic numeric model:

$$
\begin{aligned}
P^*= (&craft, community, profile, source\_material, \\
&state\_hypothesis, event\_roles, witnesses, \\
&practitioner\_review, intervention, evidence, decision, \\
&residual, revision)
\end{aligned}.
$$

AFS can encode a craft-research profile and portable records. HVL can preserve practitioner competence, dissent, refinement, refusal, and appeal. Historical CCF can describe how exploratory observations become extracted candidates, stabilized claims, CM1-admissible research artifacts, or refused residual before current GMB admission.

ACG for Quants is a financial decision and effect profile with bitemporal identity, market data, portfolio selection, order authority, execution, and attribution. Its quantitative language and state-estimation practices do not directly validate craft models, causal roles, or practitioner outcomes. The random adjacency is recorded as   
`NO_MATERIAL_RELATION` except at the very general level of time-aware evidence discipline already supplied elsewhere.

The universal GSM can type   
`CONFORMS_TO_CRAFT_RESEARCH_PROFILE`,  
`VALIDATED_BY_PRACTITIONER`, `CRYSTALLIZED_FROM_DOMAIN_PCM`, `PRESERVES_EMBODIED_REMAINDER`,  
`REFUSES_UNAUTHORIZED_FORMALIZATION`, `REVISES_AFTER_DOMAIN_EVIDENCE`,  
and   
`HAS_NO_MATERIAL_RELATION_TO_QUANT_TRADING_`  
`PROFILE`.

This randomized review establishes four editorial commitments: adopt the governed craft-evidence object; connect AFS, HVL, and historical crystallization without merging them; preserve embodied and disputed remainder; and record the nonrelation to ACG for Quants.

## A Domain-Portability Contract for State-Estimation Analogies

The Direct-Coupled Dynamic Torque Reactor is the one confirmed downstream use. It treats event-driven craft processes as a neighboring partially observed hybrid-state formalism while explicitly refusing transfer of empirical findings. That relation clarifies what makes the craft framework portable and what must remain local.

Each domain profile should bind:

$$
\begin{aligned}
P^*= (&domain, participants, events, latent\_states, \\
&observations, actions, transitions, constraints, quality, \\
&safety, tradition, expertise, models, identifiability, \\
&interventions, evidence, nontransfer, revisions)
\end{aligned}.
$$

Shared state-space mathematics permits comparison of partial observation, event timing, intervention, viability, and estimation. It does not equate bread, fermentation, ceramic firing, musical performance, clinical work, or electromechanical control. Each domain supplies its own state semantics, acceptable loss, hazard model, quality criteria, temporal scale, instruments, practitioner authority, and validation evidence.

Practitioner knowledge may identify hidden state, misleading proxy, critical transition, and useful intervention. It should be recorded as typed testimony, demonstrated skill, measurement hypothesis, or domain decision rather than either discarded as anecdote or promoted to universal truth. A quantitative model that cannot reproduce practitioner distinctions may be incomplete; practitioner agreement alone does not validate the model.

The universal GSM can type   
`INSTANTIATES_CRAFT_STATE_PROFILE`,  
`SHARES_HYBRID_STATE_FORMALISM`, `REQUIRES_DOMAIN_EXPERTISE`,  
`TREATS_PRACTICE_AS_TYPED_EVIDENCE`, `REFUSES_EMPIRICAL_TRANSFER`,  
`TESTS_PROXY_AGAINST_PRACTITIONER_DISTINCTION`, and   
`REVISES_DOMAIN_MODEL`.

This reverse-dependency review establishes four editorial commitments: adopt the domain-portability contract; distinguish shared formalism from empirical transfer; type practitioner knowledge rather than romanticizing or discarding it; and require domain-specific quality, safety, authority, and validation.

## 13. Counterevidence and Failure Modes

The framework must narrow or fail where: (1) the physical event is necessary for the target outcome; (2) event avoidance changes the target state; (3) an event is both informational and causally indispensable; (4) alternative sensors do not reconstruct decision-relevant state; (5) increased sensing does not improve practical observability; (6) instruments perturb the process; (7) model parameters are unidentifiable; (8) the landmark has high observer or context variance; (9) practitioner estimators outperform instrument-only models; (10) fused estimation offers no gain; (11) the viability kernel excluding the event is empty; (12) the alternative is unsafe or operationally unreachable; (13) outcome equivalence disappears under blinded evaluation; (14) declared masking outputs are not causally linked to reduced access; (15) apparent unmasking is an extraction or presentation artifact; (16) event suppression merely disables the signal; (17) domain profiles cannot be compared without erasing essential differences; (18) written sources underrepresent oral and embodied teaching; (19) olfactory-language claims fail cross-culturally; (20) practitioners reject the model's variables or outcomes; (21) formalization devalues rather than preserves tradition; (22) safety, labor, accessibility, or cost burdens outweigh benefit; (23) the coffee companion evidence does not reproduce; (24) bread or ceramics examples imply more evidence than exists; (25) hybrid discontinuities invalidate the continuous model; (26) the event-compression hypothesis lacks historical evidence; or (27) the framework produces no better predictions or interventions than domain-specific language.

## Formalize Craft Evidence Without Replacing Craft Authority

### Public orientation

Event-Driven Craft Processes treats familiar landmarks in roasting, baking, fermentation, ceramics, curing, and heat treatment as possible observations of hidden process state. A landmark may be informative, causal, both, or neither. The practitioner or algorithm is the estimator; the event is not automatically an estimator, and a mathematical analogy does not authorize changing a safety-relevant process.

### Adversarial tests

1. **Event-estimator collapse.** A physical transition, sensor output, culturally named landmark, and interpreting practitioner are treated as one object.
2. **Proxy-cause collapse.** An informative signal is assumed noncausal, or a causal transition is assumed to be the only useful observation.
3. **Instrumentation-superiority attack.** More sensors are presumed to recover relevant state better than embodied multimodal expertise.
4. **Tradition-romanticization attack.** Practitioner consensus or historical use is treated as causal proof, safety validation, or universal best practice.
5. **Suppression-safety attack.** Avoiding a landmark is described as improvement without proving a viable and safe alternate trajectory.
6. **Outcome-substitution attack.** One measurable output is matched while flavor, texture, durability, toxicity, labor, accessibility, or cultural value changes.
7. **Domain-transfer attack.** Shared state-space notation is used to transfer findings among food, fermentation, kilns, materials, performance, clinical work, and machines.
8. **Extraction-and-attribution attack.** Community knowledge is formalized without participant authority, attribution, benefit, contest, or protection of restricted knowledge.

### Claim and evidence ceiling

The paper offers a comparative research framework for partially observed, viability-constrained craft processes. It does not establish that named landmarks are replaceable, suppressible, noncausal, objectively inferior, or completely measurable. It provides no recipe, operating instruction, food-safety advice, kiln protocol, heat-treatment specification, or intervention authority.

Every domain claim requires practitioner participation, domain safety expertise, controlled intervention, matched multidimensional outcomes, uncertainty analysis, and current external research. Formal similarity does not transfer empirical findings. No external research was added in this pass.

### Reader-facing consequence

The constructive question is: what does the landmark reveal, what does it physically do, how does an expert use it, and could another safe path preserve every outcome the community considers important?

## 15. Conclusion

Event-driven craft practice is a promising class of partially observed control problems, but the event is not one thing. It may be a physical transition, a sensed signal, a named landmark, a causal mechanism, and a teaching token at once. A practitioner or algorithm estimates state by interpreting those objects within history and context.

The revised theory therefore does not demote traditional events. It asks what each event carries, causes, compresses, and conceals. That question can connect formal modeling with craft expertise without granting either automatic authority over the other.

The research program succeeds if it yields better predictions, safer alternative trajectories, clearer causal tests, and more faithful transmission of practitioner knowledge. It fails if its abstractions merely rename craft without improving understanding or evidence.

## Author-Supplied Reference Note

The source manuscript cites viability theory, optimal control, and work on olfactory language and culture, and refers to a coffee-roasting companion. These references and descriptions remain author-supplied and were not externally verified in this pass. Exact corpus interfaces are bound in the custody manifest.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm2.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that traditional crafts often organize continuous or hybrid developmental processes around discrete landmarks: crack in coffee roasting, spring in bread baking, foam transitions in fermentation, gelation in cheesemaking, cone behavior in ceramics, snap in curing, and color changes in heat treatment. Its nearest external comparison fields are craft, observation. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: State estimates and sensory protocols remain sensitive to calibration, hidden variables, operator judgment, and changing materials; repeatability is not universal process control. Telemetry can be complete at the instrumented boundary while omitting the causal variable, real-world effect, or authority question that matters. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Rudolf E. Kalman. "A New Approach to Linear Filtering and Prediction Problems." *Journal of Basic Engineering* 82(1), 1960, pp. 35-45. DOI: 10.1115/1.3662552. https://doi.org/10.1115/1.3662552 **Relationship:** Foundational state-estimation predecessor.

**[E2]** Leslie Pack Kaelbling, Michael L. Littman, and Anthony R. Cassandra. "Planning and Acting in Partially Observable Stochastic Domains." *Artificial Intelligence* 101(1-2), 1998, pp. 99-134. DOI: 10.1016/S0004-3702(98)00023-X. https://doi.org/10.1016/S0004-3702(98)00023-X **Relationship:** Predecessor model for acting under partial observability; used to compare belief-state control with governed epistemic state.

**[E3]** Specialty Coffee Association. *Coffee Value Assessment and Published Standards*. https://sca.coffee/research/coffee-standards **Relationship:** Industry standard for repeatable physical, descriptive, affective, and extrinsic coffee assessment.

**[E4]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E5]** W3C. *Trace Context, Level 1*. W3C Recommendation, 23 November 2021. https://www.w3.org/TR/trace-context/ **Relationship:** Adjacent distributed tracing standard for propagating trace identity across service boundaries.

**[E6]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E7]** Karen Scarfone, Murugiah Souppaya, and Donna Dodson. *Secure Software Development Framework (SSDF) Version 1.1*. NIST SP 800-218, 2022. DOI: 10.6028/NIST.SP.800-218. https://doi.org/10.6028/NIST.SP.800-218 **Relationship:** Adjacent secure-development framework for preparation, protection, production, and vulnerability response.

### Ableman corpus

**[A1]** Adam Ableman. *No-Crack Roasting*. Ableman Corpus current edition; work identity `PAPER.PUB.20724254`;  
source SHA-256  
`7F9C0E59E7F0B2F30BF4FE0515B6A4DE1D4E283E5264FC20CBB6FAEEDEA3F4CD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *A Theory of Agentic Observation*. Ableman Corpus current edition; work identity `PAPER.PUB.20437813`;  
source SHA-256  
`1D11B8E8A166861E5C0A0FF41300B6D5799F931BE00587DDE6617EC424C17FCB`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *The Constitutional Observability Platform*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-9FC6DF9C2BCB38DA`;  
source SHA-256  
`D93D41518A823703E1076B02D95D28BD7ADF29D3DC15760E0165E84E28BC70B9`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Testing for Deriving Observable State of Software Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-BAA7A4A4150F5D66`;  
source SHA-256  
`0B6AAC8B71DA25E24F7FB4A018692F609096DBA8383C9C8C0AC15F1AF711B3A8`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Epistemic Situational Awareness (ESA)*. Ableman Corpus current edition; work identity `PAPER.PUB.18123102`;  
source SHA-256  
`D43BD7CF219AB9A6EAF715CFA8CBFA32FCB8A11B8DFCADE004E00595D5F68503`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Direct-Coupled Dynamic Torque Reactor*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-834A44A92E048219`;  
source SHA-256  
`A4511355B31161B8B84CBA0A5AC8ECDECC322C37FD8BFE56CCDDD2E893FC1539`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Semantic Manifold Topology.* Zenodo, 2026. doi:10.5281/zenodo.20257244

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

DOI: [10.5281/zenodo.23847738](https://doi.org/10.5281/zenodo.23847738)
