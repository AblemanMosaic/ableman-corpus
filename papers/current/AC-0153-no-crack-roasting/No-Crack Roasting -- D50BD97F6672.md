# No-Crack Roasting

## Thermal Boundary Control and Flavor Development in Artisanal Coffee Roasting

### The history of coffee roasting treats the crack as a milestone. This work explores the possibility that it is instead a warning.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Traditional coffee roasting uses first crack as a coarse observable of roast progression. This paper proposes that modern control of latent thermochemical state allows progression to be tracked directly rather than through the proxy of structural failure.

Conventional coffee roasting practice treats first crack and second crack as central developmental milestones. Roast progression is commonly described relative to these audible fracture events, and many roasting methodologies intentionally target specific post-crack development intervals.

This paper proposes a constraint-based roasting paradigm termed *No-Crack Roasting*, in which roast trajectories are intentionally constrained to remain within a feasible thermochemical region that suppresses sustained fracture events. Rather than treating crack as a developmental phase, the method treats crack as an observable manifestation of boundary crossing within a coupled temperature-moisture-pressure system.

The proposed mechanism is selective: pyrolytically-derived burnt and acrid compounds (the masking layer) are predicted to be substantially reduced, while bean-intrinsic flavor compounds (caffeine, chlorogenic acids, trigonelline derivatives, origin-specific phenolics) are predicted to be largely preserved. The predicted operational consequence is that the **origin character of each bean should become more perceptually accessible** under no-crack roasting --- the bright astringency of African beans, the chocolate-tobacco complexity of Indonesian beans, the citrus brightness of Kenyans --- because the bean's native flavor envelope would no longer be masked by pyrolytically-generated burnt-overlay compounds. This prediction is consistent with practitioner observation across the empirical scope described in Section 14; formal sensory-panel validation remains future work (Section 20).

Coffee roasting is modeled as constrained trajectory optimization within a thermochemical state space. We hypothesize that the feasible region excluding fracture events contains trajectories that match or exceed crack-inclusive paths in flavor-relevant objective space under comparable control and endpoint constraints. Under this interpretation, first crack is not itself a developmental phase transition but a structural failure event induced by exceeding a pressure-temperature boundary.

The framework introduces observable and latent roast states, state-estimation methods, thermodynamic constraints, kinetic models, and control-theoretic formulations suitable for future experimental validation. Observations from fourteen coffee origins spanning South America, Central America, Africa, Indonesia, and Papua New Guinea motivate the framework but do not by themselves establish causality. The paper therefore advances no-crack roasting primarily as a falsifiable thermodynamic hypothesis and constrained optimization paradigm rather than as a finalized roasting doctrine.

The proposal is structured in three layers with distinct evidential standing. **Layer 1 (operational)**: no-crack roasting is feasible across the full target-darkness range under stovetop hand-roasting --- supported by extensive practitioner evidence. **Layer 2 (control-theoretic)**: acoustic crack functions as an observable proxy for latent thermochemical state progression, rather than as a developmental mechanism --- conceptually well-supported and largely independent of the masking hypothesis. **Layer 3 (masking theory)**: reduced pyrolysis-product accumulation should improve perceptual access to the bean's non-ash flavor envelope --- the most ambitious claim, requiring future sensory-panel and chemical validation. Layers 1 and 2 stand independently of Layer 3; readers skeptical of Layer 3 may still find Layers 1--2 useful. The three layers are made explicit in Section 1.1.

## 1. Introduction

Coffee roasting has historically been described through audible transitions known as first crack and second crack. These events serve as practical indicators of roast progression and are deeply embedded within roasting culture.

Despite their widespread use, crack events are not themselves flavor compounds, chemical reactions, or developmental mechanisms. They are observable manifestations of physical processes occurring within the bean.

This raises a more precise question than is usually stated. The traditional formulation --- *is crack necessary for flavor development?* --- conflates two distinct possibilities: that crack is a *mechanism* of flavor development (which would make it causally required), or that crack is an *observable* of flavor development (which would make it useful as a state estimator but not causally required).

The present paper takes the second possibility seriously. Under this interpretation, crack has been used operationally as a proxy for roast progression for centuries, alongside other human-scale observables such as visual color, olfactory transition in the volatile output, and tactile and mass-loss feel. The written tradition of coffee roasting emphasizes acoustic milestones because acoustic events are discrete, intersubjectively verifiable, and easy to record in writing; olfactory monitoring of the volatile output --- the moment the smell shifts from Maillard-sweet to pyrolytic-acrid --- is detectable by any human nose but is poorly served by textual transmission, and has therefore been historically underrepresented in the written record despite plausibly widespread operational use.

This paper explores the possibility that desirable flavor development can occur while remaining within a feasible thermochemical region that excludes sustained fracture events, using a combination of modern instrumentation (Section 15) and the same human-scale observables (olfaction, color) that operational roasting practice has always employed.

### 1.1 The Three Layers of the Proposal

**This paper should be read primarily as a theory-and-framework paper motivated by extensive practitioner observation rather than as a completed experimental validation.** The conceptual framework is the primary contribution; the practitioner evidence motivates and constrains the framework; formal experimental validation under controlled conditions is identified throughout as future work (Sections 17, 20). Readers expecting either pure theory (with no empirical contact) or completed empirical study (with statistical power and controlled trials) may find the paper does not match their expectation; what is offered is a theory with explicit empirical motivation and explicit falsification pathways, situated at the stage where craft-derived insights enter formal scientific literature.

The argument advanced in this paper is structured in three distinct layers, each making a claim of different ambition and supported by evidence of different kinds. Distinguishing the layers explicitly is important because they do not stand on equally firm ground, and a reader's response to the strongest claim should not determine their assessment of the weaker claims.

**Layer 1 --- Operational feasibility.** No-crack roasting produces drinkable coffee across the full target-darkness range from light/city through darkest non-burning roast. This is the weakest and most directly supported claim. The evidence is approximately eight years of single-practitioner stovetop practice comprising several hundred batches (Section 14). The Layer 1 claim does not depend on any particular theory of flavor mechanism; it depends only on the operational demonstration that the protocol can be executed and produces a product the practitioner considers acceptable.

**Layer 2 --- Crack as observable proxy, not mechanism.** First crack functions in coffee roasting as a state estimator --- an observable signal that historically coincided with roast progression --- rather than as a developmental mechanism that itself causally contributes to flavor. Under this layer, crack is an instrument like a thermometer or a color chart, and the question of whether the instrument can be replaced by other instruments (modern thermochemical estimators, olfactory state tracking, visual color setpoint) becomes a control-theoretic and instrumentation question rather than a question about what is chemically necessary for good coffee. Layer 2 is conceptually well-supported by the historical observation that multiple human-scale state estimators (visual, olfactory, tactile, auditory) have always coexisted in roasting practice, and that the written tradition's emphasis on acoustic milestones reflects writability rather than necessary primacy (Section 1). Layer 2 is largely independent of Layer 3: even if the masking hypothesis fails empirically, the instrumentation reframe survives.

**Layer 3 --- Masking hypothesis (H2).** Trajectories that produce sustained crack also drive pyrolysis-product accumulation as a sibling consequence (Section 13), and this pyrolysis-product accumulation forms a perceptually dominant masking layer that suppresses access to the bean's non-ash flavor envelope. Reducing this masking layer through no-crack practice is therefore predicted to improve perceptual access to origin character. This is the most ambitious claim and the one most dependent on future experimental validation. The chemistry-based prediction is supported (Section 12), and practitioner observation is consistent with the prediction (Section 14), but formal sensory-panel and chemical-assay validation remains future work (Sections 17, 20).

The three layers map approximately onto the H0/H1/H2 distinctions of Section 2: Layer 2 corresponds to H1 (crack as proxy), and Layer 3 corresponds to H2 (the masking hypothesis). Layer 1 is the operational claim that precedes these and does not require taking a position on the H0/H1/H2 question at all.

If only Layer 1 holds, no-crack roasting is an alternative roasting technique with practitioner-validated feasibility and no theoretical novelty.

If Layers 1 and 2 hold but Layer 3 does not, no-crack roasting is an instrumentation upgrade --- a way to reproduce or refine outcomes that conventional crack-based roasting also achieves, using better state estimators than acoustic fracture.

If all three layers hold, no-crack roasting reduces a previously-unnamed perceptual masking layer and improves access to bean origin character --- a substantive claim about coffee chemistry and perception with potential implications for roasting practice, sensory science, and (per the public-health discussion downstream) population-level coffee exposure to pyrolytic compounds.

The paper develops all three layers because they reinforce each other in the practitioner's experience and admit a coherent formal treatment. But the layered structure is more durable than any single layer: a critique that defeats Layer 3 does not necessarily defeat Layers 1--2, and a critique that defeats Layer 2 does not defeat Layer 1.

A further structural distinction worth previewing here, since it underlies the framework throughout, is that the present work treats **roast darkness**, **fracture state**, and **pyrolysis-product contribution** as *three independent observables* rather than as proxies for a single underlying quantity (Section 12). Conventional roasting practice tends to conflate these --- darker roasts are typically also cracked roasts with substantial pyrolysis-product accumulation, and lighter roasts tend to have all three quantities low. The framework's central claim is that these three observables can be partly decoupled: a dark roast may exhibit reduced fracture and reduced pyrolysis-product contribution relative to a conventional trajectory of the same darkness. Without this conceptual distinction the framework would be incoherent; with it, the empirical question becomes how broad the decoupled region of state space actually is.

#### A Note on the Title

The framework's deeper principle is most naturally stated as the control of pyrolysis-product accumulation: maintain the trajectory in a region where the bean's non-ash flavor envelope develops while the pyrolytic masking layer is held to a contextually appropriate level. Under this principle, fracture suppression is one *implementation* among possibly several --- the one validated by the present work --- because acoustic crack is the practitioner's directly-audible real-time observable of the boundary crossing that drives pyrolysis-product accumulation (Section 13). A more general statement of the principle might be called **low-masking roasting**, with the present work's no-crack technique as the validated implementation in the observed practitioner regime.

The title *No-Crack Roasting* reflects the implementation rather than the principle, by deliberate choice. Acoustic crack is the landmark working roasters know intimately --- every batch most practitioners have ever roasted has included it. Framing the technique in terms of crack speaks directly to that lived experience and invites the operational test: try a trajectory that stays slightly below the line you know, and observe what happens. A more abstract framing in terms of low-masking would lose this point of contact with practitioner knowledge.

Researchers extending the framework to regimes outside the present empirical scope --- where decoupling trajectories might separate fracture from pyrolysis-product accumulation (Section 13, Low-Masking Generalization) --- may find the low-masking framing more general. The title preserves the practitioner's entry point; the body of the paper preserves the principle's generality.

## 2. Hypothesis Space

The traditional question --- *what role does first crack play in roasting?* --- admits three structurally different answers, distinguished here to avoid claim ambiguity. The first treats crack as a *mechanism* of roast development; the second and third treat it as an *observable* of roast development with differing operational consequences.

### H0: Developmental Necessity

First crack is necessary for full flavor development.

Without crack, desirable roast development cannot be achieved. Under H0, crack is a mechanism: the fracture event itself contributes causally to flavor.

### H1: Developmental Proxy

First crack is not itself necessary.

It functions as a state estimator: an observable signal that frequently coincides with thermochemical progress under conventional practice but is not causally required. Under H1, crack is one of several historically available human-scale observables (alongside visual color, olfactory transition, tactile and mass-loss feel) used by roasters as a proxy for the latent state variables that actually drive flavor development.

### H2: Perceptual Masking by Pyrolysis Products

Trajectories that produce sustained first crack also drive substantial pyrolysis-product formation. Under this hypothesis, fracture and pyrolysis-product accumulation are not in a chemical-causal relationship --- the mechanical pop is not itself a chemical reaction --- but rather are *sibling consequences* of the same upstream trajectory crossing into a state-space region where both phenomena are co-produced. The resulting layer of pyrolysis products (ash-associated flavors, pyrolytically-derived bitter compounds such as quinic acid lactones, and other pyrolytic degradation products including PAHs and pyrolytic phenolics; see Section 11) occupies the perceptually dominant foreground of the resulting cup. The pyrolysis layer is not a *developmental contribution* to flavor but a *masking layer* over the non-ash flavor envelope of the underlying bean. Roasting trajectories that suppress sustained fracture --- and which therefore also suppress the boundary-crossing that drives pyrolysis-product formation --- maintain the pyrolysis contribution at perceptually contextual levels (empirically, the practitioner estimates the residual ash-flavor signal at on the order of 5--10% of conventional levels, though this is a sensory estimate of the perceptual signature of $C_p$ rather than a chemical measurement) while leaving the underlying non-ash flavor envelope substantially unchanged in composition.

H2 is a *structural* claim about signal composition, not a *preference* claim about flavor quality. It predicts that under matched-extraction conditions, sensory panels should detect at least as many non-ash flavor descriptors (e.g. fruit, floral, spice, chocolate, tobacco, origin-specific notes --- whichever the bean carries) in no-crack roasts as in conventional roasts of the same bean, with the descriptors rated equal or stronger in perceptual intensity. Whether a given drinker prefers the result --- black, with milk, sweetened, iced, or otherwise modified --- is downstream of this signal-composition claim and is out of scope.

The present work develops the framework under H2 as the working hypothesis, with H1 retained as the fallback claim if matched-endpoint testing fails to reproduce the descriptor-count and intensity predictions across brewing methods and origins.

## 3. Unified Model

The proposed framework can be compressed into a single closed formulation:

$$
\dot{S} = f_S(S, u)
$$

$$
\Omega = \{S \mid A_\Omega(S) \le \epsilon\}
$$

$$
S(t) \in \Omega \quad \forall\, t \in [0, T]
$$

$$
u(t) \in \mathcal{U}
$$

$$
\max_u \int_0^T J(S(t), \dot{S}(t))\,dt
$$

where $S$ is the roast state, $u$ is the vector of control inputs, $\mathcal{U}$ is the admissible control set (subject to actuator limits in heat input, airflow, agitation, and drum speed), $\Omega$ is the fracture-suppressed feasible region, $A_\Omega: S \mapsto \mathbb{R}$ is a band-limited acoustic fracture statistic acting as an observation operator on the state, $\epsilon$ is the selected crack-suppression threshold, and $J$ is a scalarized flavor-relevant objective. The path constraint $S(t) \in \Omega \,\forall\, t$ couples the dynamics, the feasible region, and the objective into a single optimization problem.

### Standing Assumptions

The optimization problem above is well-posed under the following standing assumptions:

- **Feasibility and reachability.** $\Omega \neq \varnothing$, and $\Omega$ is reachable from the initial state $S_0$ under some admissible control $u \in \mathcal{U}$. Without this, the constrained optimization is vacuously infeasible. **The framework does not assume that the fracture-suppressed feasible region is large; only that it is non-empty and operationally reachable. Determining its measure, robustness to control noise, and accessibility under different roasting platforms remains an empirical question.** The practitioner's eight-year evidence base (Section 14) establishes that $\Omega$ is non-empty and reachable under stovetop hand-roasting; how broadly it extends across other equipment configurations and how robustly it can be navigated under non-expert control are open questions whose answers determine the framework's practical significance --- a small $\Omega$ would render the framework intellectually interesting but practically narrow, while a broad $\Omega$ would imply potentially transformative implications for industrial roasting.
- **Boundedness of the control set.** $\mathcal{U}$ is bounded (and, in standard formulations, compact) under the actuator-limit constraints. This rules out unbounded control magnitudes and supports existence of optimal controls under the path constraint.
- **Regularity of the dynamics.** $f_S$ is Lipschitz continuous in $S$ on the operating domain, uniformly in $u \in \mathcal{U}$. This guarantees existence and uniqueness of state trajectories for any admissible control. The component functions $f_T$, $g_P$, $g_\nabla$, and $h$ introduced in Section 8 inherit this regularity through the dependence of $\dot S$ on them.
- **Regularity of the acoustic statistic.** $A_\Omega$ is measurable, and $A_\Omega(S(t))$ is at least piecewise continuous in $t$ along admissible trajectories. This ensures the path constraint $A_\Omega(S(t)) \le \epsilon$ is well-defined and the feasible set is measurable.

These assumptions are mild and typical of constrained optimal control formulations; they are stated explicitly to clarify the scope of the formal claims that follow.

Equivalently: find $u \in \mathcal{U}$ such that the induced trajectory $S(\cdot)$ satisfies the path constraint $S(t) \in \Omega$ for all $t \in [0, T]$, and among such admissible control-trajectory pairs maximize the flavor objective. The terminal time $T$ refers to the end of the controlled process, defined as the moment the bean mass falls below the process temperature threshold for further state evolution; in stovetop hand-roasting (Section 14) this includes both the burner-driven phase and the pot-thermal-battery discharge phase, both of which are under active control and both of which contribute to $C_p$ accumulation along the trajectory. The feasible region $\Omega$ thereby induces a viability constraint, with the viability kernel implicitly defined by $\Omega$, and roasting becomes a viability-constrained optimal control problem in the sense of Aubin's viability theory: the core task is not to reach a target state but to remain within the admissible region while the trajectory evolves under control.

The acoustic statistic $A_\Omega(S(t))$ enters the constraint as an *observable proxy* for the boundary crossing that drives pyrolysis-product formation, rather than as the directly-controlled quantity. In the observed practitioner regime (Sections 13, 14), trajectories that produce sustained fracture also drive pyrolytic-product accumulation, because both are downstream consequences of the same upstream trajectory crossing into the pyrolytic regime. Acoustic fracture is therefore detectable and audible to the practitioner in real time, whereas $C_p$ accumulation is latent and not directly observable; the path constraint $A_\Omega \le \epsilon$ operationalizes the latent constraint on $C_p$ via the observable acoustic surrogate. This proxy relationship is empirically robust in the practiced stovetop regime but is not a chemical-causal claim; alternative trajectories that could in principle decouple fracture from pyrolysis are discussed as a research direction in Section 13.

Roasting is therefore modeled as trajectory optimization through a thermochemical state space subject to fracture-exclusion constraints.

## 4. State Space and Observability

### 4.1 Full Roast State

We model the roast state as:

$$
S = \{T_b, \nabla T, M, P_{int}, \rho_{cell}, a_w, C_p, t\}
$$

where:

* $T_b$ = bean temperature
* $\nabla T$ = internal thermal gradient
* $M$ = moisture content
* $P_{int}$ = internal vapor pressure
* $\rho_{cell}$ = cellular structural density
* $a_w$ = water activity
* $C_p$ = cumulative pyrolysis-product content (the substrate of the masking layer of Section 12; the subscript $p$ here denotes 'pyrolysis')
* $t$ = time

The pyrolysis-product state variable $C_p$ accumulates pyrolytic degradation products as the trajectory crosses the pyrolysis onset (Section 18). Its evolution is specified in Section 10 as part of the kinetic model. Under conventional roasting trajectories, $C_p$ grows rapidly during and after first crack; under no-crack trajectories, $C_p$ grows slowly and remains small.

$C_p$ is not directly observable in real time. It is also not a single chemically well-defined compound class. $C_p$ is best understood as a **theoretical aggregate construct** representing the cumulative perceptual contribution of pyrolytically-derived compounds to the masking layer of Section 12. The compound populations that contribute to $C_p$ include PAHs, quinic acid lactones, guaiacol and syringol, pyrolytic furans at acrid concentrations, late-stage degraded melanoidins, and char-like fragments (see Section 11 for the full bean-intrinsic vs pyrolytically-derived distinction). These compounds do not have a natural common unit of mass or concentration; the framework treats them together because they are co-produced by the same upstream cause (trajectory residence time above $T_{pyro}(M)$) and because their perceptual contribution to the cup is dominated by their aggregate masking effect rather than by any single compound. $C_p$ should therefore be read as a latent theoretical quantity defined operationally by its perceptual signature and by the proxies listed below, rather than as a directly-measurable chemical concentration. An analogy from thermodynamics may help orient the reader's expectations: $C_p$ is a phenomenological state variable in the sense that entropy is. It has well-defined dynamics (Section 10), formal mathematical treatment, and experimental observability through proxies, but is not identifiable with any single microscopic quantity. Like entropy, its usefulness comes from summarizing aggregate behavior at the right level of abstraction for the framework in which it appears, not from being a concentration of a particular chemical species.

Operational proxies include polycyclic aromatic hydrocarbon (PAH) concentration in headspace or roasted samples (cf. Houessou et al. 2007), bean-mass headspace gas composition (CO and CO2 evolution from pyrolytic decomposition in the beans, with the CO/CO2 ratio shifting as the trajectory progresses through the pyrolytic regime; in gas-fired roasters, bean-derived gases must be distinguished from burner combustion products by sampling bean-mass headspace directly rather than the exhaust stack), and optical color metrics (Agtron or surface reflectance darkening as a monotone signature of advancing pyrolysis --- melanoidin accumulation and pyrolytic darkening products in the bean surface). The estimator $\hat{C}_p$ can be constructed analogously to $\hat{P}_{int}$ and $\hat{a}_w$ in Section 4.3; like those estimators, $\hat{C}_p$ is a model-derived inference from observable proxies rather than a direct measurement.

### 4.2 Observable Subspace

The observable subspace includes both instrumental and human-sensory channels. Instrumental observables include those listed in Section 15 (thermal, acoustic, mass-loss, gas-composition, optical). Human-sensory observables include visual color, audible fracture events, olfactory transition in the volatile output, and tactile and mass-loss feel. Olfactory monitoring in particular tracks the transition from Maillard-dominated volatile output (caramel, malt, bread, cocoa notes) to pyrolytic-dominated output (acrid, smoky notes) and is therefore an implicit estimator of $C_p$ crossing a perceptual threshold; this places the working nose in the same formal role as the instrumental $\hat{C}_p$ estimator of Section 4.1.

#### Olfactory Stage Taxonomy

The six-stage scheme presented in this subsection is a **practitioner-derived operational taxonomy** specific to this paper. It is not a published or validated sensory-science classification, and the stage labels (Stage 1 through Stage 6) are this paper's nomenclature rather than reference to external taxonomy. Formal sensory-science characterization of the olfactory transitions described here --- including blind-panel verification that the stage boundaries are intersubjectively distinguishable, and chemical characterization of the volatile-compound shifts at each transition --- would be a natural future-work direction (Section 20). The taxonomy below is presented for operational use within the framework's empirical scope, not as a validated sensory-science scheme.

In operational practice, the volatile output of the roast progresses through a sequence of distinguishable olfactory stages that correspond approximately to thermochemical regions of the state trajectory. The sequence below is observed under direct stovetop roasting where the volatile output reaches the roaster's nose without dilution.

1. **Green / wooden stage.** At low bean temperature, the volatile output resembles the interior of a wooden building --- dry, cellulosic, slightly vegetal. This stage reflects the green bean's native volatile profile heated but largely unreacted.
2. **Waxy stage.** As bean temperature rises, surface and matrix waxes volatilize. The smell shifts to a distinctly waxy character. This stage corresponds to the early evaporative regime ($dM/dt$ large, $T_b$ rising) before substantial Maillard activity begins.
3. **Yellowing stage.** The bean visually yellows; the smell lightens, losing the waxy character and acquiring a faintly grassy or hay-like quality. This stage corresponds to ongoing moisture loss and the onset of pigment changes preceding browning.
4. **Browning / early Maillard stage.** Visual browning begins. The smell acquires the characteristic Maillard signature --- bread, malt, caramel-edge --- as $k_M(T_b, a_w)$ enters its productive range. This is the onset of $E_{na}$ accumulation.
5. **Flavor-development stage.** The smell reaches its deepest, most integrated profile --- the full Maillard envelope plus the bean's origin-specific volatiles. This stage corresponds to maximum $dE_{na}/dt$ at moderate $C_p$ accumulation. Under no-crack operation, the trajectory is held in this regime as long as possible before pyrolytic onset.
6. **Burning / pyrolytic stage.** The smell shifts to acrid, smoky, sharply pungent character. This is the perceptual signature of $C_p$ crossing the olfactory detection threshold for pyrolysis products. The transition from Stage 5 to Stage 6 is the operational analogue of the path constraint $S(t) \in \Omega$ failing.

The Stage 5 / Stage 6 boundary is the operational decision point for no-crack roasting: the goal is to maximize residence time in Stage 5 while preventing crossing into Stage 6. The transition is rapid and the boundary is sharp under direct sensory observation, which makes olfaction a viable real-time estimator of approach to the pyrolytic regime. In the practitioner's observations, Stage 6 onset often preceded sustained acoustic crack activity, suggesting that the olfactory channel may provide earlier warning of approach to the pyrolytic regime than the acoustic channel. Instrumented validation should quantify the temporal offset between Stage 6 onset and sustained crack activity, including how the offset varies across origins, roast trajectories, and equipment configurations; the practitioner observation establishes the phenomenon but not its quantitative structure.

#### Drying-Phase Signature and the Wet-Bulb Effect

The olfactory stage sequence is grounded in a well-documented phase structure of coffee roasting (Schwartzberg 2002; Heyd et al. 2007; Fabbri et al. 2011): an initial *drying phase* in which moisture evaporation dominates the energy balance, followed by *Maillard*, *development*, and (in conventional roasting) *pyrolytic* phases. The drying phase has a distinct operational signature that connects directly to the olfactory taxonomy above.

During the drying phase, the bean's energy balance is dominated by the latent heat of vaporization of water. As long as significant free water remains in the bean, evaporation absorbs incoming thermal energy at a rate that holds bean temperature approximately at the wet-bulb limit (near 100 °C / 212 °F). Color development cannot begin until $T_b$ breaks free of this ceiling, which occurs only when moisture content drops enough that evaporation can no longer absorb the incoming heat. This is why Maillard browning (Stage 4) does not start until Stages 1--3 have completed.

This regime has three operationally important properties:

1. **The maximum water-vapor off-gas rate is approximately stable** within the practitioner's normal range of burner settings. The rate-limiting step is moisture diffusion out of the bean interior, which is a property of the bean rather than of the burner. Higher burner output does not bypass this bottleneck.
2. **The duration of the drying phase is approximately heat-input-invariant** within the practitioner's normal range of burner settings. This is an operational regularity observed across hundreds of batches, not a strict physical invariance: at burner settings below the normal range, drying takes substantially longer (the pot cannot get hot enough to drive sufficient bean-surface heat transfer); at burner settings above the normal range, drying does shorten somewhat (higher pot temperature increases the pot-to-bean temperature difference and therefore the surface heat transfer rate), but the practitioner pays for any reduction in drying time with markedly increased losses to the kitchen environment from the pot exterior and reduced control authority in later phases.
3. **The end of the drying phase is signaled by a noticeable drop in humidity off-gas**, occurring as a crossfade between olfactory Stages 2 (waxy) and 3 (yellowing). Under direct stovetop roasting, this off-gas drop is detectable as a **tactile-humidity** signal: warm humid air leaving the pot is felt directly on the face during Stages 1--2, and the sensation diminishes audibly and tangibly as drying completes.

In the open stovetop configuration, the energy balance during the drying phase differs from the closed-chamber drum-roaster case (Schwartzberg 2002; Heyd et al. 2007), where surplus burner energy that does not drive evaporation is swept through the chamber and lost as exhaust enthalpy via forced airflow. On the open stovetop there is no forced exhaust. Surplus burner energy not absorbed by evaporation is instead stored in the pot thermal mass (raising pot temperature), released to the kitchen environment by radiation and convection from the pot exterior, and lost by passive convection of warm air above the open pot. The pot's thermal mass is therefore being charged throughout the burner-on phase --- this is the same thermal battery that supports the late-phase pot-battery protocol (Section 14), with the charge state at burner-off determined by the full burner-on trajectory rather than only by terminal-phase settings.

This adds a fourth human-sensory observable channel to the framework: **tactile humidity detection at the face**, complementing the olfactory, visual, and auditory channels. Industrial roasting uses exhaust humidity probes for the same purpose; under stovetop hand-roasting, the human face serves the equivalent function.

The control-theoretic implication is that the drying phase is a regime in which the heat-input control variable $u(t)$ is *underdetermined by the state* within the practitioner's normal range --- the bean mass's behavior during Stages 1--3 is not highly sensitive to exact burner setting, because the bean-side mass-transfer bottleneck dominates. Precise control discipline becomes important once the humidity off-gas drops, $T_b$ breaks free of 100 °C, and the trajectory enters the Maillard regime (Stage 4 onward). This regime distinction is taken up in Section 14.

Not all state variables are directly measurable in situ.

Define:

$$
S_o \subset S
$$

where $S_o$ contains observable quantities such as:

* bean temperature
* exhaust temperature
* acoustic spectra
* mass loss
* environmental conditions
* airflow
* chamber humidity
* exhaust gas composition

The remaining variables must be estimated.

### 4.3 State Estimation

Internal pressure is treated as a latent variable reconstructed from observables:

$$
\hat{P}_{int} = f_P(A(t,\omega), m'(t), T_b, \nabla T)
$$

Water activity is likewise estimated indirectly:

$$
\hat{a}_w = f_a(m(t), T_b)
$$

The roasting problem therefore includes both control and state reconstruction. The claim is not that the full state is directly observable, but that sufficiently informative proxies may permit operational control of the fracture boundary.

## 5. Time-Scale Separation

Roasting contains both fast and slow dynamics.

Define:

$$
S = S_{fast} \cup S_{slow}
$$

where $S_{fast}$ includes surface temperature fluctuations, airflow perturbations, transient acoustic emissions, and pressure impulses, while $S_{slow}$ includes moisture diffusion, Maillard progression, structural evolution, and water activity changes.

Control should primarily govern smoothed trajectories in $S_{slow}$ while filtering high-frequency fluctuations in $S_{fast}$. Acoustic impulses remain important as boundary-warning signals, but a stable controller should avoid chasing every fast transient as though it represented a change in developmental state.

This separation is central to no-crack roasting: the operator or machine must respond quickly enough to avoid fracture, but slowly enough to preserve thermal continuity.

## 6. Feasible Region and Acoustic Constraint

Define the fracture-suppressed feasible region:

$$
\Omega = \{S \mid A_\Omega(S) \le \epsilon\}
$$

where $A_\Omega: S \to \mathbb{R}$ is a band-limited acoustic observation operator mapping states to a scalar fracture-emission statistic. Let $A(t, \omega; S)$ denote the acoustic power spectral density measured at the bean surface as a function of time and frequency under state evolution $S(\cdot)$. Then $A_\Omega$ is defined as the band integral:

$$
A_\Omega(S(t)) := \int_{\omega_1}^{\omega_2} A(t, \omega; S(\cdot))\,d\omega
$$

where $[\omega_1, \omega_2]$ is the frequency band associated with fracture-relevant acoustic emissions. The constraint is:

$$
A_\Omega(S(t)) \le \epsilon \quad \forall\, t \in [0, T].
$$

This disambiguates the two roles $A$ plays: $A(t, \omega; S(\cdot))$ is the measured acoustic signal (an observable signal, conditional on the state trajectory), and $A_\Omega: S \to \mathbb{R}$ is the derived state functional (the band-integrated statistic at the current state). Strictly, $A_\Omega$ is a trajectory-induced functional evaluated at time $t$, not a purely Markovian function of the instantaneous state alone; the notation $A_\Omega: S \to \mathbb{R}$ is a slight abuse that suppresses the trajectory dependence for readability. The path constraint $A_\Omega(S(t)) \le \epsilon$ is therefore enforced on the trajectory-induced value at each $t$.

The strict pre-crack manifold is:

$$
\mathcal{M}_{pre} = \{S \mid A_\Omega(S) < \epsilon\}.
$$

Acoustic emissions are not assumed to be perfect measurements of fracture proximity. They are treated as operationally useful proxies. The assumption that acoustic emission is a sufficient statistic for fracture proximity may fail in low-signal or equipment-noise-dominated environments.

## 7. Heat Transfer Regimes

### 7.1 Conduction-Dominant Operation

The manual roasting method employs:

* thick-bottomed conductive vessels
* continuous agitation
* whisk-assisted redistribution
* controlled heat application

These mechanisms reduce thermal localization and promote equilibration across bean surfaces.

### 7.2 Biot Number

The relevant dimensionless parameter is:

$$
Bi = \frac{hL}{k}
$$

where:

* $h$ = convective heat transfer coefficient
* $L$ = characteristic length
* $k$ = thermal conductivity

The hypothesis is not that $Bi \to 0$, but rather that effective crack suppression occurs within an empirical regime satisfying:

$$
Bi < Bi_{crit}
$$

for some process-dependent threshold. This reflects reduced internal thermal gradients rather than a physically unattainable asymptotic limit.

## 8. Pressure, Structure, and Energy Balance

Internal pressure is not free-floating. It is linked to moisture, temperature, pore volume, and structural density.

A minimal heuristic relation is:

$$
P_{int} \sim \frac{M T_b}{V_{pore}}
$$

where $V_{pore}$ is the effective pore volume available for vapor expansion. Cellular density $\rho_{cell}$ enters through its relation to pore volume and fracture tolerance:

$$
V_{pore} = V_{pore}(\rho_{cell})
$$

and:

$$
P_{fracture} = P_{fracture}(M, \rho_{cell}).
$$

Cellular density is not quasi-static: it evolves under thermal and pressure exposure as the bean's structural matrix changes:

$$
\frac{d\rho_{cell}}{dt} = h(T_b, P_{int}).
$$

This evolution equation captures the irreversible structural change of the bean during roasting, including the expansion and porosity evolution that occurs as the cellular matrix is heated and stressed even when fracture itself is suppressed. The sign of $h$ depends on the local regime: in conventional roasting the bean expands (density decreases) as moisture is released and the cellular matrix transforms; under tightly controlled no-crack regimes the expansion is more gradual but typically still dominant over densification.

Thermal gradients couple to pressure accumulation through accelerated localized vaporization. Pressure evolution depends not only on the instantaneous state but on the rate of moisture release, since vapor generation is the driving term:

$$
\frac{dP_{int}}{dt} = g_P\!\left(\nabla T,\ \frac{dM}{dt},\ T_b\right)
$$

with the qualitative relationship:

$$
\frac{\partial P_{int}}{\partial t} \propto \nabla T \cdot k_d(T_b)
$$

The dependence on $dM/dt$ rather than $M$ alone makes pressure a genuinely dynamic variable rather than a quasi-static function of the instantaneous state: fast moisture release drives sharp pressure rises that slow release does not, even at the same instantaneous moisture content.

The bean temperature evolves according to a minimal energy balance:

$$
\frac{dT_b}{dt} = f_T(u(t), T_{env}, M)
$$

where $u(t)$ includes heat input, airflow, agitation, and drum or vessel dynamics. The internal thermal gradient is coupled to the bean's thermal state through the surface-core differential:

$$
\nabla T = g_\nabla(T_b, T_{surface})
$$

where $T_{surface}$ is the bean surface temperature, observable via infrared imaging (Section 15). The qualitative dependence is $\nabla T \propto (T_{surface} - T_b) / L$ for characteristic length $L$, with the precise functional form depending on bean geometry, conductive properties, and the heat-transfer regime. This grounds the gradient as a dynamical variable derived from observable thermal quantities rather than a free parameter.

## 9. Mechanistic Model

### 9.1 Conventional Regime

Large thermal gradients produce:

$$
\nabla T \uparrow
$$

$$
P_{int} \uparrow
$$

$$
\text{Fracture}
$$

$$
\text{Pyrolysis}
$$

This pathway is associated with abrupt pressure release, cellular rupture, rapid porosity change, and increased thermal stress.

### 9.2 No-Crack Regime

Reduced thermal gradients produce:

$$
\nabla T \downarrow
$$

$$
\text{Diffusive Moisture Release}
$$

$$
P_{int} \downarrow
$$

$$
\text{Fracture Suppression}
$$

$$
\text{Extended Maillard Activity}
$$

The central mechanism is therefore not reduced temperature alone but altered transport dynamics.

## 10. Minimal Kinetic Model

Moisture evolution is represented by:

$$
\frac{dM}{dt} = -k_d(T_b,\nabla T)
$$

where $k_d$ is an effective drying rate.

The kinetic model decomposes flavor development into two quantities: the cumulative non-ash flavor envelope $E_{na}$ and the cumulative pyrolysis-product accumulation $C_p$. These evolve via separable kinetics, but the two equations are coupled through their shared dependence on $T_b$ (and hence on the control $u$): the same temperature trajectory drives both $k_M$ and $k_P$, so $E_{na}$ and $C_p$ cannot be controlled independently --- they share a single thermal substrate. The kinetics:

$$
\frac{dE_{na}}{dt} = k_M(T_b, a_w)
$$

$$
\frac{dC_p}{dt} = k_P(T_b)
$$

where $k_M$ is the Maillard and bean-native flavor compound formation rate and $k_P$ is the pyrolytic degradation rate (the pyrolysis-product formation rate). $k_M$ is hypothesized to peak within an intermediate temperature and water-activity region; $k_P$ is hypothesized to increase monotonically with temperature and to accelerate sharply above the pyrolysis onset $T_{pyro}(M)$ (Section 18). The differential equation for $C_p$ should be understood as a **reduced-order phenomenological model** rather than a claim that all constituent compounds (PAHs, quinic acid lactones, guaiacol, syringol, late-stage degraded melanoidins, char fragments) share identical kinetics; the aggregate rate $k_P$ summarizes the population's collective behavior at the level appropriate to the masking-layer abstraction (Section 4.1) and does not constrain the kinetics of individual constituent species.

A flavor-relevant scalar objective can be constructed from $E_{na}$ and $C_p$ as a *signal-to-masking ratio*. A minimal illustrative form is:

$$
J(t) = \frac{E_{na}(t)}{1 + \alpha \, C_p(t)}
$$

where $\alpha > 0$ is a perceptual masking coefficient (the ratio of pyrolysis-product contribution to the perceptual foreground per unit $C_p$, calibrated empirically against sensory descriptor counts; see Section 20). This form is presented as the simplest algebraic expression of the qualitative claim that pyrolysis-product accumulation masks the non-ash envelope rather than destroys it; the form is monotone decreasing in $C_p$ and is acknowledged to be incomplete (Section 14 notes an interior optimum in $C_p$ that this form does not capture). Readers should engage this expression as one specific instantiation of the signal-to-masking principle, not as the definitive flavor objective of the framework. The principle --- that the perceptual cup is a ratio between the non-ash envelope and the masking layer, with the masking layer attenuating the envelope rather than removing it --- survives any specific algebraic form; refinement of the algebra to admit interior optima and other empirical structure is left for future work.

**A scope note on the psychophysical regime.** The signal-to-masking model is intended to describe **suprathreshold perceptual dominance shifts** --- the gross perceptual reorganization that occurs when one compound class (pyrolysis products) shifts from dominating ~95% of the perceptual foreground to occupying ~5--10%. It is not intended to model perception at the limits of detection, where threshold effects, compound-specific masking, adaptation, and subtle interaction effects (well-studied in psychoacoustics and chemosensory signal-detection theory) would matter and would likely defeat the single-coefficient ratio form. The empirical regime the framework addresses is the regime where the ash-flavor signal in conventional roasts is large, the underlying non-ash compound population is also large but perceptually suppressed, and reducing the ash signal substantially shifts which compounds dominate the cup. In this regime, the framework predicts perceptual differences large enough to be operationally observable without requiring threshold-level sensory discrimination. Formal blind-panel sensory science would still be valuable for converting the practitioner observation into peer-reviewable form (Section 20), but the underlying perceptual claim is a claim about gross perceptual dominance, not about psychophysical signal detection at threshold.

The single-coefficient form $\alpha$ is adopted as the minimal model; sensory masking in real perceptual systems is notoriously nonlinear, and future work may require origin-specific masking coefficients, descriptor-specific masking functions, or a matrix-valued $\alpha$ that depends on which non-ash compounds are being masked by which pyrolytic products. The scalar form here is a starting point sufficient to express the qualitative claim, not a commitment to single-parameter sensory psychophysics.

The differential form follows by the quotient rule:

$$
\frac{dJ}{dt} = \frac{k_M(T_b, a_w)}{1 + \alpha \, C_p} - \frac{\alpha \, E_{na} \, k_P(T_b)}{(1 + \alpha \, C_p)^2}
$$

This form encodes the H2 mechanism (Section 12) directly: pyrolysis does not destroy the non-ash envelope within the admissible region --- $E_{na}$ is monotone non-decreasing along trajectories that remain in $\Omega$ (the pre-pyrolytic regime where $k_M > 0$ and $k_M$ is not opposed by Maillard-product degradation) --- but it masks it. Outside $\Omega$, Maillard products themselves degrade at sufficiently high $T_b$, so $E_{na}$ is not in general monotone on arbitrary trajectories; the monotone claim is scoped to admissible trajectories.

The functional form $J = E_{na} / (1 + \alpha C_p)$ is monotone decreasing in $C_p$ and therefore predicts $J$ maximized as $C_p \to 0$. Operational practice (Section 14) indicates this monotonicity does not hold across the full $C_p$ range: at very low $C_p$, the cup loses identity as coffee even though $E_{na}$ would be at or near its maximum. The pyrolysis-product accumulation contributes positively to the perceptual identity *coffee* up to a contextual threshold, beyond which it begins to mask. The current formula is therefore scoped to the regime where $C_p$ is small but above a contextual lower bound $C_p^{min}(\text{target})$ that depends on the target roast darkness. Refinement of the functional form to admit an interior optimum --- e.g. a form whose denominator is non-monotone in $C_p$, or whose numerator includes a positive pyrolysis-identity term at low $C_p$ --- is left for future work. The qualitative finding is robust; the algebraic form is a modeling choice not yet uniquely determined by data.

Two limiting cases within the scoped regime are instructive:

- **Conventional roasting** ($C_p$ large). $J \approx E_{na} / (\alpha C_p)$ falls inversely with pyrolysis-product accumulation. The model predicts that the non-ash envelope is present in the cup but perceptually attenuated by the masking layer.
- **No-crack roasting** ($C_p$ small, near zero). $J \approx E_{na}$. The model predicts that the non-ash envelope is recovered at near-full perceptual weight.

The hypothesis of an extended Maillard window with suppressed pyrolysis corresponds to maximizing $E_{na}$ while constraining $C_p$ to remain small. The path constraint $S(t) \in \Omega$ (Section 3), enforced via the acoustic statistic $A_\Omega(S) \le \epsilon$, operationalizes this in observable terms: the fracture-suppression constraint bounds $C_p$ growth by bounding the regime in which $k_P$ is large.

## 11. Flavor Objective and Path Dependence

The flavor representation factorizes into a vector of non-ash descriptors and the pyrolysis-product masking layer, consistent with the signal-to-masking decomposition of Section 10:

$$
F = (F_{na}, C_{mask})
$$

where $F_{na}$ is the vector of perceptual descriptors:

$$
F_{na} = \{f_{aroma}, f_{acidity}, f_{body}, f_{persistence}\}
$$

and $C_{mask}$ is the perceptual expression of pyrolysis-product accumulation (whose state-space substrate is $C_p$ from Section 4.1). $C_{mask}$ is dominated by *pyrolytically-derived* ash, smoke, acrid, and burnt-bitter compounds, not by bean-intrinsic bitter and astringent compounds (see *Bean-Intrinsic vs Pyrolytically-Derived Bitter Compounds* below). What was previously labelled $f_{bitterness}$ in flat-vector flavor representations is, on closer inspection, two distinct compound classes whose conflation has historically obscured the framework's actual claim: the perceptual signature of $C_{mask}$ is specifically the pyrolytically-derived burnt-bitter overlay, not the bean's intrinsic bitterness profile.

### Bean-Intrinsic vs Pyrolytically-Derived Bitter and Acrid Compounds

Coffee bitterness and astringency arise from multiple chemically distinct compound classes. The framework's claim that no-crack roasting reduces the masking layer $C_p$ refers exclusively to *pyrolytically-derived* compounds, not to *bean-intrinsic* compounds. This distinction is important because the two classes contribute differently to the cup, and the no-crack technique selectively reduces the former while preserving the latter.

**Bean-intrinsic bitter and astringent compounds** (predicted to be preserved under no-crack roasting; part of $E_{na}$):

* **Caffeine** --- bitter, present in green coffee, largely unchanged by roasting at the temperatures relevant here.
* **Chlorogenic acids and their intact derivatives** --- contribute substantial astringency and bright/acidic character. African beans (Kenyan, Ethiopian, Burundian, Rwandan) have particularly high chlorogenic acid content, which is part of why they have their distinctive bright and astringent character. The *intact* chlorogenic acids and their non-pyrolytic derivatives are part of the non-ash envelope.
* **Trigonelline and its non-pyrolytic derivatives** --- including N-methylpyridinium, which contributes a bitterness considered desirable.
* **Bean-native phenolic compounds and diterpenes** --- cafestol, kahweol, and various origin-specific polyphenols contributing structural bitterness and oily mouthfeel.

These compounds are part of the non-ash flavor envelope $E_{na}$ and constitute much of what distinguishes one origin from another. The bright astringency of an Ethiopian Yirgacheffe, the chocolate-tobacco complexity of a Sumatran Mandheling, the citrus brightness of a Kenyan AA --- these are bean-intrinsic profiles, not pyrolytic artifacts. Reducing them would reduce origin character.

**Pyrolytically-derived bitter and acrid compounds** (reduced by no-crack roasting; part of $C_p$):

* **Quinic acid lactones and other pyrolytic decomposition products of chlorogenic acids** --- formed by *thermal decomposition* of chlorogenic acids in the pyrolytic regime. These contribute the harsh, lingering, characteristically dark-roast bitterness --- the "burnt" character, chemically distinct from the intact chlorogenic acids of the bean.
* **Pyrolytic furans and furanones at acrid concentrations** --- at moderate Maillard levels these contribute caramel and bread notes; at pyrolytic concentrations they contribute smoky and acrid character.
* **Guaiacol, syringol, and other pyrolytic decomposition products of cellulose and lignin** --- phenolic compounds with smoky, medicinal, and acrid character. These are pure pyrolysis products with no bean-intrinsic source.
* **Late-stage melanoidins in their pyrolytically-degraded forms** --- earlier-stage Maillard products are sweet and caramel-edged; the same compounds further decomposed at higher temperatures lose those qualities and contribute pyrolytic bitterness.
* **PAHs and char-like fragments** --- toxicologically significant; contribute subtle smoky notes at coffee concentrations.

These compounds are what $C_p$ accumulates and what $C_{mask}$ perceptually expresses. They are not bean-intrinsic; they are produced by the trajectory's residence time above the pyrolytic onset $T_{pyro}(M)$.

**Operational consequence.** The framework predicts that the no-crack technique reduces $C_p$ (the pyrolytically-derived overlay) without substantially reducing the bean-intrinsic compounds that constitute origin character. The empirical observation across the practitioner's eight years of practice is consistent with this prediction: African beans are observed to retain their characteristic bright astringency under no-crack roasting, and the astringency is reported as *more* perceptually accessible than under conventional roasts, consistent with reduced masking by pyrolytic burnt-overlay compounds. Indonesian and Papua New Guinea beans are similarly observed to retain their chocolate-tobacco complexity, with the same reported unmasking effect. The framework predicts that the dominant effect is selective reduction of the pyrolytic overlay while preserving the bean's full bitter-and-astringent compound spectrum; the practitioner's observations are consistent with this prediction. The cup is not less bitter overall; it is *differently* bitter --- with the bitterness and astringency now reflecting the bean's intrinsic chemistry rather than a pyrolytic overlay imposed by the roast trajectory.

The scalar non-ash envelope used in the kinetic model of Section 10 is defined as the preference-weighted sum:

$$
E_{na} := w \cdot F_{na}, \qquad w = \{w_1, w_2, w_3, w_4\}
$$

where $w$ represents preference weights over the non-ash descriptors. This identifies the scalar $E_{na}$ of Section 10 with the weighted vector aggregation above, resolving the apparent dimensional mismatch: $F_{na}$ is the perceptual vector, $E_{na}$ is its scalar projection under the chosen preference weighting. The full flavor scalar combines this with the masking term per Section 10:

$$
J = \frac{E_{na}}{1 + \alpha\, C_p}
$$

This factorization makes explicit that preference (encoded in $w$) is preserved as a downstream parameter while the masking-reduction mechanism (encoded in $\alpha$ and $C_p$) is preference-independent: any choice of $w$ over $F_{na}$ benefits from reducing $C_p$.

Because roasting chemistry is path-dependent, the more precise objective is:

$$
\max_u \int_0^T J(S(t),\dot{S}(t))\,dt
$$

For tractability, some experimental implementations may approximate this with a state-functional $J(S(t))$, but this should be understood as a simplification rather than a claim that roast chemistry is memoryless.

Assume $J$ is continuous or piecewise smooth over $\Omega$. Without this assumption, the optimization problem is not well-posed.

## 12. Thermochemical Hypothesis

We hypothesize that first crack is not a developmental phase transition but a structural failure event induced by exceeding a pressure-temperature boundary. Beyond the boundary, pyrolysis-product formation enters a regime where these compounds become perceptually dominant in the resulting cup.

Predicted decreases (the pyrolysis layer):

* polycyclic aromatic hydrocarbons
* pyrolytic decomposition products
* excessive pyrolytically-derived phenolic compounds (quinic acid lactones, guaiacol, syringol; bean-intrinsic chlorogenic acids and their non-pyrolytic derivatives are predicted to be preserved --- see Section 11)
* ash-associated flavors

Predicted *perceptual* effect on the non-ash envelope:

* the underlying non-ash flavor compounds of the bean (whatever they are for a given origin) become perceptually unmasked rather than chemically preserved
* compounds that were always present under conventional roasting but were dominated by the pyrolysis layer rise relative to it in the cup
* this applies origin-agnostically: dark cherry and tobacco in one bean, citrus and blackcurrant in another, floral and bergamot in a third --- the framework does not predict *which* compounds dominate the unmasked envelope, only that *whatever* the bean carries becomes more perceptually accessible

The distinction between *preservation* (compounds physically protected from degradation) and *unmasking* (compounds chemically present at comparable levels but no longer perceptually dominated by pyrolysis products) is testable. Chemical assay of matched-extraction samples would show similar levels of the underlying compounds under both regimes if the mechanism is unmasking; substantially elevated levels under no-crack if the mechanism is preservation; both effects may contribute to varying degrees. The hypothesis remains subject to direct chemical and sensory validation.

No-crack roasting is independent of conventional light/medium/dark endpoint categories. A roast may reach light, medium, or dark endpoint targets while remaining inside the fracture-suppressed feasible region. The critique advanced here is not a critique of dark-roast sensory development as such, but specifically of ash-associated pyrolysis products that become perceptually dominant when the trajectory crosses the fracture-associated boundary.

### Roast Degree versus Fracture State

Three quantities that conventional roasting practice tends to collapse into a single "roast level" are treated by this framework as **independent observables**:

1. **Roast darkness** --- total Maillard product accumulation, measured by Agtron, surface reflectance, or visual color grade. A function of cumulative thermal exposure (roughly the integral of $k_M(T_b, a_w)$ along the trajectory).
2. **Crack activity** --- audible structural fracture events, captured by the acoustic statistic $A_\Omega(S(t))$. A function of the internal pressure trajectory relative to the fracture boundary $P_{fracture}(M, \rho_{cell})$.
3. **Pyrolysis-product contribution** ($C_p$) --- accumulated pyrolytic degradation products, the substrate of the masking layer. A function of dwell time above the pyrolysis onset $T_{pyro}(M)$.

These three quantities are correlated under conventional roasting practice because most thermal trajectories cross all three boundaries together. They are not, however, the same variable. The framework permits:

- **Dark no-crack roasts**: high cumulative Maillard contribution (visually dark) with the fracture and pyrolysis boundaries unbroached, achieved by extended dwell at moderate temperature below $T_{pyro}$.
- **Light cracked roasts**: short fast trajectories that cross the fracture boundary without accumulating substantial darkness.
- **Cracked-but-low-pyrolysis roasts**: trajectories that briefly cross fracture but exit the pyrolytic regime before significant $C_p$ accumulates.

The paper's working hypothesis (H2) makes a claim about one of these three quantities only: that $C_p$, the pyrolysis-product contribution, masks the non-ash envelope and should be minimized. It makes no claim about roast darkness as a perceptual variable: a dark roast with low $C_p$ is permitted and predicted to retain unmasked non-ash flavor. The title "No-Crack Roasting" names the operational constraint (suppress $A_\Omega$), not a darkness regime; the framework is silent on whether a target roast should be light, medium, or dark in Agtron terms.

## 13. Structural Transformation and Extraction Coupling

Fracture provides effects on two distinct channels that must not be conflated. The framework does not identify darkness with defect. It identifies uncontrolled fracture-associated pyrolysis-product accumulation with masking.

**Extraction channel.** Fracture changes the bean's physical structure in ways that affect how compounds are released into the brew water:

* increased porosity
* increased surface area
* improved degassing pathways
* altered brewing diffusion
* increased dissolved-solids yield per unit time of extraction

These are real benefits to *extraction*, not to the flavor envelope itself. Crack suppression reduces dissolved-solids yield under a fixed brewing protocol, which means the same brewing parameters applied to a no-crack roast produce an under-extracted cup. The modeled non-ash envelope $E_{na}$ is not reduced by crack suppression --- it is the *brewing protocol* that is no longer matched to the bean's altered extraction geometry.

**Masking channel.** Fracture is also a structural marker of the pyrolysis-product threshold (Section 12). Under H2, crossing this threshold is associated with the masking-layer accumulation that the hypothesis identifies.

The two channels are independent. The extraction-channel benefits of fracture can be replicated under no-crack roasting by adjusting the brewing protocol (finer grind, lower coffee-to-water ratio, more aggressive extraction methods such as heavy boil or pressure extraction) to recover comparable dissolved-solids yield. Under such matched-extraction conditions, the masking-channel effect is what differentiates the two regimes.

This distinction has direct implications for experimental design (Section 17): comparing a no-crack roast brewed at conventional parameters against a conventional roast brewed at conventional parameters confounds the channels and is uninformative about H2. Matched-endpoint testing must equalize dissolved-solids load, not just brewing-time protocol.

### Causal Structure of Fracture and Pyrolysis Coupling

The framework's path constraint $A_\Omega(S(t)) \le \epsilon$ treats fracture-suppression as operationally equivalent to pyrolysis-product suppression. It is worth being precise about the causal structure that licenses this equivalence, because the claim is more subtle than it can appear at first reading.

Fracture and pyrolytic-product formation are governed by different physics. Fracture is a *mechanical* event determined by the internal vapor pressure exceeding the bean's structural integrity: $P_{int}(t) \ge P_{fracture}(M, \rho_{cell})$. Pyrolytic-product formation is a *thermal-chemical* phenomenon determined by the bean temperature crossing the pyrolytic-onset threshold: $T_b(t) \ge T_{pyro}(M)$. These are not the same event and neither chemically causes the other --- the mechanical pop is not itself a chemical reaction, and pyrolytic decomposition does not require structural failure to proceed.

The two phenomena are, however, **operationally coupled in the observed practitioner regime** by their shared upstream cause: trajectories that drive bean temperature above $T_{pyro}(M)$ while moisture remains in the bean also produce internal pressures that approach $P_{fracture}$, and trajectories that produce sustained $P_{int} \ge P_{fracture}$ have also typically driven $T_b$ above $T_{pyro}$. The causal structure is:

$$
\text{thermal trajectory} + \text{moisture state} + \text{pressure buildup}
$$

$$
\longrightarrow \quad \text{boundary crossing}
$$

$$
\longrightarrow \quad \text{fracture} \;+\; \text{pyrolysis-product acceleration}
$$

Fracture and pyrolysis-product acceleration are *sibling consequences* of the same upstream cause, not parent-and-child events. The framework's path constraint $A_\Omega \le \epsilon$ is therefore best read as: *manage the trajectory so that the upstream boundary crossing does not occur; use acoustic fracture as the observable indicator that boundary crossing has occurred, since it is the directly-audible sibling of the latent and unmeasurable pyrolysis-product accumulation.*

This precision matters for two reasons. First, it removes an implicit chemical-causation overclaim that would not survive examination: the framework does not claim that crack causes pyrolysis. Second, it makes the framework's empirical scope explicit: the operational coupling between fracture and pyrolysis-product formation is robust *in the observed practitioner regime* but is not a necessary coupling across all possible state-space paths.

It follows that **the framework presently assumes that acoustic fracture is a useful operational surrogate for pyrolysis-product accumulation within the practitioner's observed regime; establishing the strength and limits of this correlation is itself a primary experimental objective for follow-up work.** The practical effectiveness of no-crack roasting depends on this surrogate relationship holding tightly --- if the correlation between $A_\Omega$ and $C_p$ is loose across the practiced regime, the path constraint would not reliably control the latent quantity of interest. Quantifying how tightly acoustic crack and pyrolysis-product accumulation co-vary across roast trajectories, origins, and equipment configurations is one of the highest-priority empirical questions the framework opens.

#### Low-Masking Generalization as Future Work

The shared-upstream-cause structure raises an interesting theoretical possibility: are there trajectories that decouple fracture from pyrolysis-product formation? In principle, yes:

* Aggressive pre-drying trajectories that lower $M$ substantially before $T_b$ approaches $T_{pyro}$ could in principle reach pyrolytic temperatures without significant fracture, because the pressure-buildup component of the boundary crossing would be suppressed by the reduced moisture available for vapor formation.
* Very fast pressure-ramp trajectories at sub-pyrolytic temperatures could in principle produce fracture without significant pyrolysis-product accumulation, if the bean fractured before its temperature reached the pyrolytic-onset threshold.

Such decoupling trajectories are not within the empirical scope of the present work and have not been investigated by the practitioner. They would constitute alternative implementations of a more general principle that might be called **low-masking roasting**: managing the trajectory to limit pyrolysis-product accumulation, with fracture suppression as one operational approach among possibly several. No-crack roasting as developed here remains the primary operational form for the observed stovetop regime, because acoustic fracture is the practical real-time indicator of boundary crossing under realistic hand-roasting control. Whether other regimes admit decoupling trajectories that achieve equivalent low-masking outcomes via different operational paths is a question for experimental investigation outside the present scope.

### Three Mechanisms with Distinct Empirical Signatures

H2 is the dominant working hypothesis of this paper, but the framework supports three potentially distinct mechanisms by which no-crack roasting could improve the cup. They are not mutually exclusive, and the experimental program of Section 20 is designed to distinguish among them.

- **Preservation.** Specific non-ash flavor compounds (Maillard intermediates, bean-native volatiles, lipid-derived aromatics) are physically protected from pyrolytic degradation by trajectories that remain in $\Omega$. *Empirical signature*: chemical assay of matched-extraction samples shows higher levels of these compounds in no-crack roasts than in conventional roasts.
- **Unmasking** (the H2 mechanism formalized in Sections 10--12). Compound levels are not substantially different between regimes; what differs is the perceptual weight of the pyrolysis-product accumulation $C_p$, which masks the non-ash envelope in conventional roasts. *Empirical signature*: chemical assay shows similar non-ash compound levels across regimes, but matched-extraction sensory panels detect more non-ash descriptors per cup and rate them at higher intensity in no-crack samples.
- **Extraction geometry** (the Section 13 extraction channel). Fracture changes the bean's physical structure --- porosity, surface area, degassing pathways --- in ways that alter compound release into brew water. *Empirical signature*: under fixed brewing parameters, no-crack roasts produce under-extracted cups; under matched-TDS brewing, this channel contributes no flavor difference. The extraction-channel effect is therefore detectable by comparing fixed-brewing-parameter results against matched-TDS results.

The three mechanisms have different observable consequences and different falsification routes (Section 20). Preservation requires elevated compound levels; unmasking requires lower pyrolysis-product accumulation in the presence of comparable compound levels; extraction geometry requires the result to disappear under matched-TDS brewing. The framework remains agnostic as to the relative magnitudes of the three contributions in any given roast; the prediction is only that each contributes through a distinguishable channel.

## 14. Experimental Observations

### Operational Evidence Base

The framework developed here is grounded in approximately eight years of single-practitioner stovetop roasting practice by the present author, comprising several hundred batches across the full target-darkness range from light/city through darkest non-burning roast. The empirical scope is **stovetop hand-roasting**, not drum or machine roasting; all observations in this paper come from the hand-roasting configuration described below.

A note on the role of operational detail in this section. The remainder of Section 14 documents specific stovetop technique --- six control sub-inputs (burner, shake, lift, whisk, breath, pot thermal battery), the late-phase pot-battery protocol, the failure mode taxonomy, the cooldown-pops-as-quality-indicator finding. This level of operational detail is included because it constitutes the empirical foundation from which the framework was derived, and because precise documentation of the validated method is necessary for any reader who wishes to evaluate the empirical basis of the claims. The operational detail is therefore the *source* of the framework, not the framework itself. The framework's claims (Layers 1, 2, 3 of Section 1.1) are about state-space structure, observability, and signal-to-masking decomposition, all of which are implementation-general; the stovetop protocol is one validated instantiation of these claims. Machine-roaster configurations and other equipment regimes are expected to support corresponding instantiations (Section 16 maps the control surface; the drum-roaster analogue of the late-phase pot-battery protocol is given there), though experimental validation in those configurations is outside the present empirical scope.

The equipment configuration is intentionally minimal: a thick-bottomed pot with a single handle, an open kitchen stove burner (gas in the practitioner's case, though electric coil or induction admit the same control structure with adjusted dynamics), and a metal whisk used continuously inside the pot during roasting. There is no enclosed roasting chamber, no forced airflow system, no programmable temperature controller, and no instrumented sensor stack. The roasting environment is open to the kitchen.

The thick-bottomed pot is not incidental equipment. It functions as a **thermal battery**: during the burner-driven phase, the pot bottom accumulates stored thermal energy at a rate determined by burner setting and pot thermal mass; during the late phase of the trajectory the pot is removed from the burner but continues to deliver heat to the bean mass from this stored energy, with a discharge time constant set by pot thermal mass and pot-to-bean heat transfer coefficient. This stored-energy delivery is used as a controlled completion mechanism (see *Late-Phase Protocol* below) and is essential to reaching the preferred 5--10% $C_p$ contribution range. A thin pot would not support this protocol, since burner-off would terminate effective heat input immediately.

The four sensory channels used as state estimators are:

* **Nose** --- olfactory stage detection (Section 4.2), the primary real-time state estimator
* **Ears** --- audible crack as the constraint-violation signal (heard only when admissibility has already been overshot)
* **Face** --- tactile humidity detection during the drying phase (Section 4.2)
* **Eyes** --- visual color development as the setpoint readout

The four control inputs available to the practitioner are:

* **Burner setting** --- the primary heat-input rate control (knob position on the stove)
* **Pot agitation (shake)** --- shaking the pot laterally during cooking, distributing heat across the bean mass and breaking up local hot spots
* **Pot-to-burner distance (lift)** --- briefly lifting the pot off the burner during shaking, instantly reducing effective heat input without changing the burner setting
* **Whisking vigor** --- continuous whisk action inside the pot, with whisking vigor (rate and arc) as a continuous parameter affecting bean-to-bean heat transfer and overall thermal homogeneity
* **Direct airflow (breath)** --- blowing directly into the pot to cool the bean mass, providing an additional fast transient heat-output channel independent of burner setting and pot position; admissible as a control input and operationally useful for arresting Stage 5 / Stage 6 transitions when burner reduction alone is too slow
* **Pot thermal battery (stored-energy release)** --- the pot bottom's accumulated thermal energy during the burner-driven phase is released to the bean mass after pot-removal-from-burner, with a long discharge time constant set by pot thermal mass and bean-pot heat transfer; controlled by the timing of pot-removal (which loads the battery to a target state) and by stirring during discharge (which modulates the rate of energy transfer); used to deliver the final contribution of $C_p$ that achieves the preferred 5--10% range

Fourteen distinct origins were evaluated including coffees from South America, Central America, Africa, Indonesia, and Papua New Guinea; no qualitative divergence was observed across origins within practitioner-sensory resolution.

The preferred evaluation blend consisted of:

* 50% Colombia
* 30% Ethiopia
* 20% Papua New Guinea

Observed flavor characteristics appeared directionally consistent across origins, though controlled statistical validation remains necessary.

### Non-Monotonicity at Low Pyrolysis-Product Accumulation

The full darkness range achievable under no-crack practice extends from light/city through what would be visually classified as darkest non-burning roast. Across this range, the practitioner observation is that **pyrolysis-product contribution is not monotonically undesirable**: at very low $C_p$, the cup loses identity as coffee. The darkest end of the no-crack range produces a cup with extreme color development but $C_p$ contribution below approximately 5% of conventional cracked-roast levels; this cup is described by the practitioner as "more like a coffee-flavored tea" --- the visual identity of coffee is preserved, the non-ash envelope is at maximum, but the pyrolysis-product-associated flavors that are part of the perceptual category *coffee* are insufficient.

This finding refines H2. The operational claim is not *minimize $C_p$* but *find the contextually appropriate $C_p$ value for the target roast darkness*. Pyrolysis-product accumulation contributes positively to coffee identity up to a contextual threshold; beyond that threshold it masks. The optimum is an interior point in $C_p$, not a corner. Across the practitioner's roast-darkness range, the optimal $C_p$ is observed to vary with target darkness but remain substantially below the conventional cracked-roast value at every darkness level.

### Control-Theoretic Structure of the Operational Practice

Under stovetop hand-roasting, the operational practice instantiates a control-theoretic structure that aligns with the formal model of Sections 3 and 16:

- **Visual color** functions as the **setpoint**: the target color of the finished beans defines 100% completion for the batch. The practitioner stakes the target color at batch start as the calibration of the endpoint; the trajectory is then steered toward that endpoint.
- **Olfactory state** (Section 4.2 stage taxonomy) functions as the **real-time state estimator**: at every moment in the trajectory, the volatile output gives a direct readout of whether the system is *too hot now*, *not hot enough to progress*, or *progressing at the right rate*. The conclusions available from the smell at any given moment are operational: increase heat, decrease heat, or hold.
- **Heat input** is the **control variable** $u(t)$, decomposed in stovetop practice into six sub-controls: burner setting, pot shake (lateral agitation), pot lift (transient distance from burner), whisking vigor (continuous in-pot agitation), direct airflow (breath blown into the pot for active cooling), and pot thermal battery (stored-energy release after pot-removal-from-burner). These sub-controls have distinct response profiles and operate on distinct time scales: burner setting sets the slowly-adjustable baseline during the burner-driven phase; pot shake, pot lift, and breath all provide fast transient reductions of effective heat input, with breath specifically targeting the bean-mass surface for direct convective cooling; whisking vigor maintains thermal homogeneity throughout and modulates the rate of pot-to-bean energy transfer during pot-battery discharge; the pot thermal battery operates on a longer time scale than any other control input and is used to deliver the final controlled contribution of $C_p$ during the late phase. In machine-roaster configurations, this control surface maps to burner output, drum rotation speed, airflow rate, chamber-load mixing, and post-burner heat-soak management; the present work's empirical validation is limited to the stovetop instantiation.
- **Acoustic crack** is not a primary signal at all. It is a **downstream proxy for constraint violation**: when crack activity becomes audible, the controller has *already* allowed the trajectory to cross the admissible boundary. In skilled practice, crack should not be heard; if it is heard, the batch has been overshot at that moment, and the controller has failed.

Within this structure, the failure modes are operationally distinguishable:

- **Insufficient heat input.** The trajectory stalls: olfactory output remains in an earlier stage (Section 4.2) for too long, and the target color is approached too slowly or not at all. The batch may stall before reaching the target setpoint.
- **Excess heat input.** The trajectory crosses into pyrolytic onset (Stage 6 of Section 4.2): olfactory output shifts to acrid/smoky, $C_p$ accumulates rapidly, and acoustic fracture activity follows. The result is excess ash flavor and (depending on severity) a batch that is partially or fully outside admissibility.
- **Successful trajectory.** Heat input is modulated continuously such that olfactory output progresses through Stages 1--5 (Section 4.2) at the appropriate pace to reach the target visual color at the moment olfactory Stage 5 reaches its operational peak. Whisking maintains thermal homogeneity. Stage 6 onset is detected by smell *before* it would trigger acoustic crack from active burner-driven heat input, and the pot is removed from the burner at that moment to begin the late-phase pot-battery-driven completion (described below).

#### The Ash Flavor Selection Phase

Within the browning regime (Stage 4 onward) the bean mass admits a temperature sub-regime in which $P_{int}$ reaches $P_{fracture}$ for individual beans, producing audible fracture events. This sub-regime --- here called **pop-active browning**, distinguished from earlier **pre-pop browning** in which $E_{na}$ accumulates but $P_{int}$ has not yet reached the fracture threshold --- is the **ash flavor selection phase**. Popping does not occur during the yellowing phase (Stage 3) because bean temperature is still rising through the post-wet-bulb regime and has not yet reached fracture-threshold conditions; popping is exclusively a browning-phase phenomenon.

The practitioner's control task is to titrate the duration of pop-active browning. Zero engagement of this phase is associated with the reported <5% $C_p$ failure mode (the "coffee-flavored tea" cup of the non-monotonicity finding above), where the trajectory completes browning to the target visual color without any beans crossing the fracture boundary. Sustained engagement is associated with the conventional cracked-roast outcome and excess $C_p$. The preferred 5--10% range (a practitioner sensory estimate; see the non-monotonicity discussion above) is reportedly produced by a brief, bounded engagement: 2--5 audible pops, after which the trajectory exits the pop-active regime.

#### Late-Phase Pot-Battery Protocol

The pop-active phase can in principle be engaged at any point during browning. In practice, the operationally preferred implementation is to engage it at the tail end of the trajectory using the pot's thermal battery, for reasons of *control authority* rather than mechanism.

With the burner on during browning, the system has high control authority working against the practitioner: heat input rate is large, and once one bean crosses the fracture threshold the rate of subsequent crossings accelerates rapidly (more beans warming through the threshold per unit time, with the active heat input continuously pushing the system upward). The interval between first pop and rapid sustained popping is short, and landing exactly 2--5 pops requires active suppression by burner reduction and other transient controls, with narrow margin for error.

With the burner off at the tail end of the trajectory, the pot's stored thermal energy is on a monotonically declining trajectory: it dissipates into the bean mass and from the bean mass outward, with no replenishment. Once a small number of beans pop, the system's total embodied heat has already begun decreasing, so the next bean that would have popped is now slightly below threshold by the time its turn comes. **The pop sequence is self-limiting under pot-battery discharge.** This is a qualitatively different control regime from burner-driven popping: not just easier, but operating in a self-terminating energy budget rather than an open-ended one.

The tail-end protocol is therefore:

1. **Burner off, pot to cool stove surface.** Active heat input terminates. The pot's accumulated thermal energy now becomes the sole remaining energy source.
2. **Stir up.** Distribute the stored thermal load across the bean mass, exposing interior beans to surface heat and homogenizing the temperature distribution.
3. **Stop stirring; leave.** With the pot off the burner and stirring halted, the bean mass equilibrates with the pot bottom over a discharge time constant set by pot thermal mass. During this interval 2--5 audible fracture events occur in the bean mass --- the operationally desirable pop sequence.
4. **Stir again.** After the pops subside, resume stirring to homogenize the cooling bean mass and prevent any local hot spots from sustaining further fracture.
5. **Cool to threshold.** Continue stirring intermittently until the bean mass is below the process temperature threshold; then leave to cool passively.

The 2--5 pops produced by this protocol are an **engineered fraction of total $C_p$ accumulation**, not constraint-relaxation artifacts. The pot-battery discharge delivers a controlled, self-limiting dose of pop-active-phase residence time to the bean mass after burner-driven heating has stopped. The dose is calibrated by the timing of pot-removal-from-burner (which loads the battery to a target state) and by stirring discipline during discharge.

The pop count serves as a **quality indicator** for the trajectory. Zero pops indicate the active-phase trajectory ran too cautiously and never reached the pop-active sub-regime --- the <5% failure mode. More than a small bounded number of pops indicate the pop-active sub-regime was engaged longer than intended, either via mistimed burner-off or excessive stored thermal load --- approaching the conventional cracked-roast outcome. The 2--5 range is the operational signature of a brief, controlled engagement of the ash flavor selection phase under self-limiting pot-battery discharge.

The drying phase (Stages 1--3, Section 4.2) and the post-drying phases (Stages 4--5) have qualitatively different control dynamics. During drying, the bean is held near the wet-bulb temperature by latent-heat absorption, and the burner setting is underdetermined by the state within the admissible range; precise control discipline is not required during this period because the bean does not respond strongly to small variations in heat input. Once the humidity off-gas drops (felt as the face sensation diminishing) and $T_b$ breaks free of 100 °C, the trajectory becomes highly responsive to heat input and the four control sub-inputs (burner, shake, lift, whisk) all become operationally significant. This natural regime transition --- from coarse control during drying to fine control during browning and development --- is detected by the practitioner via the combination of olfactory stage progression and tactile humidity sensation, without instrumentation.

This control structure has been validated through the practitioner's operational experience across the full roast-darkness range. It is the **primary validated implementation path** for no-crack roasting, not a fallback to be used in the absence of instrumentation.

**The roast-and-extraction unit.** The framework's perceptual claims are properly understood as claims about the *coupled roast-and-extraction system*, not about the roast alone. The practitioner's operational protocol pairs no-crack roasting with aggressive extraction: ultra-fine grind, low coffee-to-water ratio, and heavy boil extraction (or equivalent pressure extraction at espresso scales). These two halves of the protocol are operationally inseparable. A no-crack roast brewed at conventional extraction parameters does not fully express the framework's predicted outcome --- it produces a cup that may read as thin or under-developed compared to conventional expectations, because conventional extraction does not pull enough of the non-ash compound population out of the bean to fully populate the perceptual foreground. Practitioner experience suggests that aggressive extraction is required to bring the bean's full non-ash flavor envelope into the cup; with the ash population reduced to a practitioner-estimated 5--10% of conventional levels (a sensory estimate of the perceptual signature of $C_p$, not a chemical measurement), the framework predicts that aggressive extraction populates the cup with the non-ash compounds without simultaneously over-extracting an ash dominance --- a prediction consistent with the practitioner's repeated observation across origins and roast endpoints, though not yet formally validated under blind controlled conditions.

This coupling has direct implications for experimental design and for reader expectations. A skeptical taster who applies *conventional* extraction parameters to a no-crack roast and finds the result thin or weak is not testing what the framework claims; they are testing whether no-crack roasting can substitute for conventional roasting under unchanged brewing protocols, which the framework does not predict. The framework's claim is that *under matched aggressive extraction*, the no-crack roast delivers a cup whose perceptual character is dominated by the bean's non-ash flavor envelope rather than by pyrolytic overlay. Sections 13 and 17 develop the matched-TDS experimental requirement that follows from this coupling.

### Epistemic Scope of the Operational Evidence

The operational evidence base supports the following claims at high confidence (in the sense of repeated single-practitioner observation across hundreds of batches):

- The full target-darkness range from light/city through darkest non-burning is achievable under no-crack operation
- Olfactory state estimation + visual color setpoint + continuous heat-input control is a feasible implementation of the framework's control structure
- The failure modes (under-development, ash overshoot) are distinguishable in real time via olfaction
- At very low $C_p$, the cup loses identity as coffee even at maximal color development

It does not, by itself, establish:

- Statistical superiority of no-crack output over conventional roasts in formal blind sensory panels (this is the formal H2 falsification test of Section 20, not yet conducted)
- The functional form of the optimal $C_p$ as a function of target darkness
- Cross-practitioner reproducibility under matched protocols
- Performance under industrial-scale roasting equipment

The operational evidence is appropriate to establish *feasibility and characteristic behavior* of the method, in the sense in which craft practice accumulates knowledge before formal study. Statistical and sensory-panel evidence remains future work as outlined in Sections 17 and 20.

## 15. Instrumentation Requirements

The framework's operational implementation has been validated under hand-roasting practice using olfactory state estimation and visual color setpoint as described in Section 14. Modern instrumentation is therefore *not a prerequisite* for no-crack roasting; it is an extension that enables capabilities the hand-roasting implementation does not support.

The historical role of first crack as an operational state estimator is filled, under modern roasting, by an instrumentation stack that tracks the latent thermochemical state directly rather than through the proxy of structural failure. This stack complements rather than replaces the human-sensory observables (visual color, olfactory transition, tactile feel) that have always been available to roasters; the combination of instrumental and sensory channels allows finer-grained state tracking than either alone.

The specific capabilities that instrumentation adds beyond skilled hand-roasting include: (i) reproduction of the method by operators without the years of practice required to develop reliable olfactory state estimation; (ii) quantitative cross-batch and cross-operator comparison; (iii) matched-endpoint experimental designs for the formal H2 falsification tests of Sections 17 and 20; (iv) automated process control at industrial batch scales where direct olfactory monitoring is not practical; (v) construction of explicit estimators $\hat{P}_{int}$, $\hat{a}_w$, and $\hat{C}_p$ for the latent state variables.

Future validation should include:

### Thermal

* embedded thermocouples
* infrared surface imaging
* surface-core differential measurement

### Acoustic

Acoustic power density should be measured as:

$$
A(t,\omega)
$$

with decomposition across frequency bands.

Potential categories include:

* microfracture bands
* continuous high-frequency emissions
* fracture impulses
* audible crack events

### Mass Transport

* real-time mass-loss curves
* drying-rate estimation
* moisture-release profiles

### Gas Analysis

* CO
* CO2
* exhaust chemistry
* volatile-compound sampling

## 16. Optimal Control Formulation

The control input vector $u(t)$ is a substrate-and-equipment-dependent set whose components vary with the roasting configuration. The present work's empirical validation is for **stovetop hand-roasting** (Section 14), in which the components are:

* **burner setting** (primary heat-input rate control)
* **pot agitation** / shake (lateral mixing)
* **pot-to-burner distance** / lift (transient heat-input reduction)
* **whisking vigor** (continuous in-pot mixing)
* **direct airflow** / breath (active convective cooling of the bean-mass surface)
* **pot thermal battery** (stored-energy release during late-phase pot-off completion; long-time-scale control input loaded by burner-driven phase and discharged by pot-to-bean heat transfer)

In **machine-roaster configurations** (drum, fluid-bed, spouted-bed), the analogous components are:

* heat input (burner power or heating-element control)
* airflow rate
* drum rotation or fluid-bed velocity
* batch-load mass

The formalism below is stated for $u(t)$ generally; the optimal-control problem is well-posed under either control surface, but the empirical claims of this paper are scoped to the stovetop case.

The Late-Phase Pot-Battery Protocol of Section 14 admits a direct drum-roaster analogue. In a drum-roaster configuration, the equivalent implementation is to stop drum rotation at the appropriate moment in browning, which cuts the active control input that distributes heat through the bean mass while allowing the chamber's stored thermal energy to discharge into the now-static bean column in a self-limiting fashion. The 2--5 audible pops occur during this rotation-paused interval; rotation is then resumed (with burner off if not already) to re-engage forced airflow and drive the bean mass below the process temperature threshold. The mechanism is the same as in the stovetop case --- cut the active control input that pumps energy through the system, allow residual stored thermal energy to discharge in a self-limiting fashion, count pops, then resume active control for cooldown --- with drum rotation playing the role that pot-on-burner plays in the stovetop instantiation.

The roasting problem becomes:

$$
\max_u \int_0^T J(S(t),\dot{S}(t))\,dt
$$

subject to:

$$
A_\Omega(S(t)) \le \epsilon
$$

with initial condition:

$$
S(0) = S_0
$$

and terminal constraints such as:

$$
C(S(T)) = C_{target}
$$

where $C(S(T))$ may include endpoint color, mass loss, density, expansion ratio, and selected chemical proxies.

Internal pressure enters as a soft penalty through estimated state reconstruction rather than as an independent hard constraint:

$$
\lambda \hat{P}_{int}(t)
$$

may be included in the objective or penalty term.

The objective is therefore not temperature tracking but trajectory optimization within:

$$
\Omega = \{S \mid A_\Omega(S) \le \epsilon\}
$$

## 17. Comparative Experimental Design

Future validation requires matched-endpoint comparisons on both the roast and the brew.

**Roast-side controls** (equalizing the bean state at end of roasting):

* identical green coffee
* identical batch mass
* identical Agtron color
* matched mass loss
* matched density
* matched expansion ratio
* crack-enabled roast
* crack-suppressed roast
* chemical endpoint class or proxy equivalence

**Brew-side controls** (equalizing what reaches the cup):

* matched total dissolved solids (TDS) yield in the brew
* matched extraction percentage (extraction yield by mass of dissolved compounds relative to dry coffee mass)

The brew-side controls are required because of the two-channel decomposition in Section 13: fracture's extraction-channel benefit (higher dissolved-solids yield per unit brewing time at fixed parameters) is independent of its masking-channel effect. Comparing a no-crack roast brewed at conventional parameters against a conventional roast brewed at conventional parameters confounds the two channels and is uninformative about H2. The no-crack roast may require finer grind, lower coffee-to-water ratio, or more aggressive extraction (heavy boil, pressure extraction) to achieve TDS-matched brews; this brewing adjustment is the operational counterpart of the masked-versus-unmasked comparison.

Agtron alone is insufficient because crack affects porosity, density, and extraction structure. A multi-metric endpoint constraint --- spanning both roast endpoint and brew endpoint --- is required to avoid confounding structural and extraction differences with chemical and perceptual differences.

## 18. Phase Boundaries

Thermochemical phase space may be represented by axes:

* $T_b$
* $M$
* $P_{int}$

with $t$ as a trajectory parameter.

The fracture boundary is:

$$
P_{int} = P_{fracture}(M, \rho_{cell}).
$$

The pyrolysis boundary is:

$$
T_b > T_{pyro}(M).
$$

Both $P_{fracture}$ and $T_{pyro}$ are assumed to be continuous functions of their arguments on the relevant operating domain. Without this assumption, the geometry of phase space is undefined and trajectory optimization within $\Omega$ is not well-posed.

Expected qualitative properties include:

$$
\frac{\partial P_{fracture}}{\partial \rho_{cell}} > 0
$$

and:

$$
\frac{\partial T_{pyro}}{\partial M} < 0
$$

The sign of:

$$
\frac{\partial P_{fracture}}{\partial M}
$$

may depend on whether moisture is treated primarily as a plasticizing factor, a pressure source, or a structural weakening factor. This requires empirical determination rather than assumption.

## 19. Failure Modes

Potential limitations include:

### Underdevelopment

* grassy notes
* enzymatic flavors
* insufficient Maillard progression

### Shelf Stability

* altered moisture retention
* altered degassing behavior

### Control Fragility

* narrow operating margins
* operator sensitivity
* instability near fracture boundaries

### Energy Cost

* increased roast duration
* reduced throughput
* altered commercial economics

### Observability Limits

* poor microphone placement
* equipment noise
* low-signal acoustic environments
* weak correlation between acoustic emissions and internal fracture proximity

### Scalability

* drum systems
* fluid-bed systems
* industrial systems

may behave differently from conduction-dominant manual methods.

## 20. Falsification Criteria

The framework's three-layer structure (Section 1.1) implies that different empirical observations would falsify different layers. The criteria below are grouped by which layer they test. A given observation may refute a stronger layer while leaving weaker layers intact.

### Layer 1 Falsification --- Operational Feasibility

Layer 1 claims that no-crack roasting is feasible across the target-darkness range. It would be refuted by:

* failure of independent practitioners to reproduce no-crack outcomes under matched protocols across multiple sessions
* operational fragility so severe that the practitioner-validated range cannot be extended to other practitioners or other equipment configurations even with training
* fundamental thermodynamic impossibility argument showing that the proposed feasible region $\Omega$ is empty or has measure zero under realistic boundary conditions

Refutation at Layer 1 would invalidate the entire paper, since Layers 2 and 3 depend on Layer 1 being achievable. The reported eight-year single-practitioner evidence makes this the least likely refutation path, but it is logically possible.

### Layer 2 Falsification --- Crack as Proxy, Not Mechanism

Layer 2 claims that acoustic crack functions as an observable proxy for thermochemical state progression rather than as a causally required developmental event. It would be refuted by:

* demonstration that fracture-event chemistry itself --- not merely the temperature regime that produces fracture --- causally contributes to desirable flavor compound formation, independent of the trajectory's thermochemical state
* sensory evidence that no-crack roasts are *intrinsically* incapable of reaching flavor outcomes equivalent or superior to matched-endpoint cracked roasts, under any practitioner skill level or instrumentation regime
* historical or operational evidence that pre-instrumental roasters who used olfactory or visual estimation in place of acoustic milestones produced systematically inferior results, indicating that the acoustic estimator was not merely one among several but causally privileged

Refutation at Layer 2 would invalidate the instrumentation reframe and the proxy interpretation but leave Layer 1 (operational feasibility) intact. The framework would reduce to "an alternative roasting protocol exists" without the conceptual claim that conventional roasting was relying on a coarse instrument.

### Layer 3 Falsification --- The Masking Hypothesis (H2)

Layer 3 claims that pyrolysis-product accumulation forms a perceptually dominant masking layer whose reduction improves access to the bean's non-ash flavor envelope.

It is worth distinguishing two epistemic statuses for this claim. The **phenomenon** --- that no-crack roasts under matched aggressive extraction (Section 14) produce a perceptually distinct cup in which non-ash flavor character dominates rather than pyrolytic overlay --- is supported by the practitioner's hundreds of trials over eight years, and the framework predicts perceptual differences large enough to be operationally observable without requiring threshold-level sensory discrimination. The **formal blind-panel demonstration** of this phenomenon, under controlled matched-extraction conditions with trained sensory panels and statistical power, has not been conducted and remains future work. These are distinct things: the phenomenon's existence is well-supported at the practitioner-observation level, but its formal scientific demonstration in peer-reviewable form is pending. Layer 3 falsification routes test both: whether the phenomenon exists at all (refuted by negative blind-panel results), and whether the formal model's specific structure ($\alpha$ as a single masking coefficient, ratio form, etc.) holds.

Layer 3 would be refuted by:

* matched-extraction sensory panels detect *fewer* non-ash flavor descriptors per cup in no-crack samples than in conventional roasts of the same bean
* matched-extraction sensory panels rate non-ash descriptor *intensity* lower in no-crack samples than in conventional roasts
* chemical assay of the non-ash compound classes (Maillard products, bean-native volatiles, lipid-derived aromatics, etc.) shows substantially lower levels in matched-endpoint no-crack samples than in conventional ones, indicating that the mechanism is *not* unmasking but rather *loss* of those compounds under conventional roasting
* the perceptual masking coefficient $\alpha$ in Section 10 cannot be calibrated to a consistent value across origins and panels --- i.e. the signal-to-masking ratio fails to behave as a single-parameter family
* PAH and pyrolytically-derived compound assay shows no substantial reduction in no-crack roasts compared to conventional matched-endpoint roasts, indicating that the trajectory-based prediction does not hold empirically

Refutation at Layer 3 would invalidate the masking hypothesis (H2) and would invalidate much of the formal kinetic and signal-to-masking machinery of Sections 10--11. However, Layers 1 and 2 would survive: a reader who concludes that Layer 3 is wrong may still take from the paper that no-crack roasting is feasible (Layer 1) and that crack functions as an observable proxy rather than a developmental mechanism (Layer 2).

### General Cross-Layer Criteria

Some criteria apply across multiple layers and would weaken the framework in any combination of refutations:

* no-crack trajectories fail to reproduce across origins or roasting platforms (weakens Layer 1 and undermines the generality of Layers 2--3)
* extraction robustness disappears when density, expansion, and mass loss are controlled (weakens Layer 3 specifically, since the brewing-channel decomposition of Section 13 depends on the masking-channel being the differentiator under matched extraction)

These outcomes provide clear empirical paths for falsification at multiple levels of ambition: operational (Layer 1), instrumentation (Layer 2), and sensory/chemical/formal (Layer 3). The layered structure means the paper can be partially correct: refutation of the strongest layer does not refute the weaker layers, and partial validation of weaker layers does not establish the stronger ones.

## Discussion

The principal contribution of this work is not a roasting recipe but a formal reframing of roasting itself.

Rather than treating crack as a developmental target, the framework models roasting as constrained trajectory optimization within a thermochemical state space.

Under this interpretation, crack becomes one observable manifestation of state-space boundary crossing rather than the organizing principle of roast development.

The key question therefore becomes:

What flavor-optimal trajectories exist within the feasible region that excludes fracture events?

## Conclusion

This paper proposes no-crack roasting as a constrained thermochemical optimization paradigm.

Coffee roasting is modeled as trajectory optimization within a feasible state-space region:

$$
\Omega = \{S \mid A_\Omega(S) \le \epsilon\}
$$

The central hypothesis is that this fracture-suppressed region contains trajectories capable of matching or exceeding crack-inclusive roast paths in flavor-relevant objective space under comparable control and endpoint constraints.

If validated, the implications extend beyond a particular roasting technique. Crack would cease to function as a developmental milestone and instead become one indicator among many describing motion through a thermochemical landscape whose governing structure is fundamentally continuous rather than event-based.

## Appendix A: Observable and Latent Variables

Observable:

* temperatures
* acoustic spectra
* mass loss
* exhaust composition
* airflow
* chamber humidity

Latent:

* internal pressure
* water activity
* cellular density
* pore-volume evolution

with corresponding estimators.

## Appendix B: Acoustic Classification

Class 0:
No detectable fracture activity

Class 1:
Microfracture emissions only

Class 2:
Occasional isolated impulses

Class 3:
Partial first crack

Class 4:
Sustained first crack

Class 5:
Second crack

## Appendix C: Thermochemical Phase Space

Axes:

* $T_b$
* $M$
* $P_{int}$

Trajectory parameter:

* $t$

Fracture boundary:

$$
P_{int} = P_{fracture}(M,\rho_{cell})
$$

Pyrolysis boundary:

$$
T_b > T_{pyro}(M)
$$

Regions:

* feasible region
* pre-crack manifold
* fracture zone
* pyrolysis zone

## Appendix D: Representative Curves

* $T_b(t)$
* $m(t)$
* $A(t,\omega)$
* drying trajectories
* crack-enabled profiles
* no-crack profiles
* endpoint density and expansion curves

## Appendix E: Cross-Substrate Generalization

**Scope note.** This appendix sketches a research direction *suggested by the formalism*. It does not advance experimental claims for any substrate other than coffee. The candidate-substrate list below should be read as enumerating possible directions for future investigation, not as implied extensions already supported by evidence. Application of the framework to any non-coffee substrate would require per-substrate empirical validation and the parameter recalibration described at the end of this appendix.

The formalism developed in this paper is presented for coffee but is substrate-neutral in structure. The signal-to-masking decomposition, the acoustic fracture-suppression constraint, and the path-constrained optimal control formulation apply in principle to any roasted plant material whose flavor development proceeds through Maillard kinetics under thermal control and whose endpoint is approached by a structural fracture or rupture event.

### Substrate-Neutral Elements

The following elements of the framework are substrate-independent:

- The state structure $S = \{T_b, \nabla T, M, P_{int}, \rho_{cell}, a_w, C_p, t\}$. Each component is defined for any plant material under thermal roasting; none is coffee-specific in definition.
- The kinetic decomposition $dE_{na}/dt = k_M(T_b, a_w)$ and $dC_p/dt = k_P(T_b)$. The Maillard rate $k_M$ and the pyrolytic rate $k_P$ are general food-chemistry quantities; their functional forms differ across substrates but their roles in the model do not.
- The signal-to-masking ratio $J = E_{na} / (1 + \alpha C_p)$. Perceptual masking by pyrolysis products is a general property of roasted plant material, not coffee-specific.
- The acoustic fracture-suppression constraint $A_\Omega(S(t)) \le \epsilon$. Any roasted material with an audible fracture, rupture, or expansion event admits an analogous acoustic statistic, though the spectral band $[\omega_1, \omega_2]$ and the threshold $\epsilon$ require per-substrate calibration.
- The viability-constrained optimal control formulation of Section 3.
- The three-mechanism distinction of Section 13 (preservation, unmasking, extraction geometry).

### Candidate Substrates

The framework's mechanism --- "fly low" relative to the fracture boundary, accept a small residual pyrolysis-product signal, recover the non-ash envelope --- has plausible application to:

- **Grains**: barley (especially roasted-barley beverages such as mugicha; malting and dark malt production), wheat, oats, rye, spelt
- **Rice**: roasted-rice tea (genmaicha), puffed-rice products, parched rice
- **Maize**: popcorn, parched corn, masa toasting
- **Legumes**: soybean (roasted as kinako), chickpeas, lupini, lentils, peanuts
- **Tree nuts**: almonds, hazelnuts, walnuts, pistachios, cashews
- **Seeds**: sesame, sunflower, pumpkin, flax
- **Other**: cocoa beans, cacao nibs, chicory root, carob, dandelion root, lotus seed

In each case the same structural pattern applies: a thermal regime exists below the conventional fracture-or-rupture boundary in which the non-ash envelope of the substrate develops while the pyrolysis-product accumulation is held to a small contextual contribution.

### Per-Substrate Recalibration

Application to any non-coffee substrate requires recalibration of the following parameters:

- **Pyrolysis onset temperature** $T_{pyro}(M)$ and PAH formation thresholds. The coffee-specific values from Houessou et al. (2007) and related literature are not transferable to other substrates.
- **Maillard kinetics** $k_M(T_b, a_w)$. Different substrates have different sugar/amino-acid profiles and therefore different Maillard product spectra and rates.
- **Cellular geometry** ($\rho_{cell}$, $V_{pore}$) and the fracture pressure $P_{fracture}(M, \rho_{cell})$. Bean, kernel, nut, and seed structures differ substantially in their mechanical properties and pore architectures.
- **Acoustic fracture signature**. Frequency band $[\omega_1, \omega_2]$ and threshold $\epsilon$ are substrate-specific; popping corn, splitting almonds, and rupturing rice grains each produce distinct acoustic signatures.
- **Perceptual masking coefficient** $\alpha$. The mapping from pyrolysis-product accumulation to perceptual ash dominance is substrate-specific and reflects the underlying non-ash envelope's perceptual scale.

### Status

This appendix records the framework's claimed generality and identifies plausible candidate substrates. It does not advance experimental claims for any substrate other than coffee. Experimental validation of the framework on any non-coffee substrate, and the per-substrate recalibration of the parameters listed above, remain future work.

---

## Corpus-Wide Reference Positioning

This paper argues that traditional coffee roasting uses first crack as a coarse observable of roast progression. Its nearest external comparison fields are craft, observation, cps. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: State estimates and sensory protocols remain sensitive to calibration, hidden variables, operator judgment, and changing materials; repeatability is not universal process control. Telemetry can be complete at the instrumented boundary while omitting the causal variable, real-world effect, or authority question that matters. Runtime monitors and fallback controllers only protect modeled safety envelopes and can fail through sensor error, timing assumptions, unsafe recovery, or omitted hazards. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[A1]** Adam Ableman. *Event-Driven Craft Processes as State-Estimation Problems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-45D8DDF80127D803`;  
source SHA-256  
`936C0B8B481E811D204A60C0848B406BFFC90CA7D74711DD45C6A691E1924062`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

**[A7]** Adam Ableman. *Constitutional Robotics*. Ableman Corpus current edition; work identity `PAPER.PUB.18750683`;  
source SHA-256  
`D10DF9B6B7F742D9EEABF01BC5DFC3755BB4EBF548E8CB5F215BB9D94678F514`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The references below are organized by the technical area the present work draws on. Citations are stated in standard form so the reader can locate the original source.

### Coffee Standards and Sensory Evaluation

Specialty Coffee Association. (2024). *SCA Standard 102-2024: Coffee Value Assessment --- Sample Preparation and Tasting Mechanics*. Specialty Coffee Association. Available at <https://sca.coffee/research/coffee-standards>.

Illy, A., & Viani, R. (Eds.). (2005). *Espresso Coffee: The Science of Quality* (2nd ed.). Amsterdam: Academic Press / Elsevier. ISBN 978-0-12-370371-2.

### Coffee Roasting Modeling --- Heat and Mass Transfer

Schwartzberg, H. G. (2002). Modeling bean heating during batch roasting of coffee beans. In J. Welti-Chanes, G. V. Barbosa-Cánovas, & J. M. Aguilera (Eds.), *Engineering and Food for the 21st Century* (pp. 871--892). Boca Raton, FL: CRC Press.

Heyd, B., Broyart, B., Hernandez, J. A., Valdovinos-Tijerino, B., & Trystram, G. (2007). Physical model of heat and mass transfer in a spouted bed coffee roaster. *Drying Technology*, 25(7--8), 1243--1248. <https://doi.org/10.1080/07373930701438683>

Fabbri, A., Cevoli, C., Alessandrini, L., & Romani, S. (2011). Numerical model of heat and mass transfer during roasting coffee using 3D digitised geometry. *Procedia Food Science*, 1, 742--746. <https://doi.org/10.1016/j.profoo.2011.09.112>

Wang, X., & Lim, L.-T. (2014). A kinetics and modeling study of coffee roasting under isothermal conditions. *Food and Bioprocess Technology*, 7(3), 621--632. <https://doi.org/10.1007/s11947-013-1159-8>

### Coffee Roasting Chemistry --- Volatile and Aroma Compounds

Yeretzian, C., Jordan, A., Badoud, R., & Lindinger, W. (2002). From the green bean to the cup of coffee: investigating coffee roasting by on-line monitoring of volatiles. *European Food Research and Technology*, 214(2), 92--104. <https://doi.org/10.1007/s00217-001-0424-7>

Yeretzian, C., Opitz, S., Smrke, S., & Wellinger, M. (2019). Coffee volatile and aroma compounds --- from the green bean to the cup. In A. Farah (Ed.), *Coffee: Production, Quality and Chemistry* (pp. 726--770). Cambridge: Royal Society of Chemistry. <https://doi.org/10.1039/9781782622437-00726>

Sunarharum, W. B., Williams, D. J., & Smyth, H. E. (2014). Complexity of coffee flavor: a compositional and sensory perspective. *Food Research International*, 62, 315--325. <https://doi.org/10.1016/j.foodres.2014.02.030>

### Pyrolysis and PAH Formation in Roasting

Houessou, J. K., Maloug, S., Leveque, A.-S., Delteil, C., Heyd, B., & Camel, V. (2007). Effect of roasting conditions on the polycyclic aromatic hydrocarbon content in ground Arabica coffee and coffee brew. *Journal of Agricultural and Food Chemistry*, 55(23), 9719--9726. <https://doi.org/10.1021/jf071745s>

Orecchio, S., Ciotti, V. P., & Culotta, L. (2009). Polycyclic aromatic hydrocarbons (PAHs) in coffee brew samples: Analytical method by GC-MS, profile, levels and sources. *Food and Chemical Toxicology*, 47(4), 819--826. <https://doi.org/10.1016/j.fct.2009.01.011>

### Acoustic Emission and Fracture Monitoring

Grosse, C. U., & Ohtsu, M. (Eds.). (2008). *Acoustic Emission Testing: Basics for Research --- Applications in Civil Engineering*. Berlin Heidelberg: Springer-Verlag. <https://doi.org/10.1007/978-3-540-69972-9>

### Heat Transfer and Food Process Engineering

Incropera, F. P., DeWitt, D. P., Bergman, T. L., & Lavine, A. S. (2011). *Fundamentals of Heat and Mass Transfer* (7th ed.). Hoboken, NJ: John Wiley & Sons. ISBN 978-0-470-50197-9.

Singh, R. P., & Heldman, D. R. (2014). *Introduction to Food Engineering* (5th ed.). London: Academic Press / Elsevier. ISBN 978-0-12-398530-9.

### Optimal Control and State Estimation

Bryson, A. E., & Ho, Y.-C. (1975). *Applied Optimal Control: Optimization, Estimation, and Control* (Rev. ed.). Washington, DC: Hemisphere Publishing.

Kirk, D. E. (2004). *Optimal Control Theory: An Introduction*. Mineola, NY: Dover Publications. ISBN 978-0-486-43484-1.

### Viability Theory (Comparator Formalism, Section 3)

Aubin, J.-P. (1991). *Viability Theory*. Systems & Control: Foundations & Applications. Boston: Birkhäuser. ISBN 978-0-8176-3571-8.

Aubin, J.-P., Bayen, A. M., & Saint-Pierre, P. (2011). *Viability Theory: New Directions* (2nd ed.). Berlin Heidelberg: Springer. <https://doi.org/10.1007/978-3-642-16684-6>

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20724254](https://doi.org/10.5281/zenodo.20724254)
