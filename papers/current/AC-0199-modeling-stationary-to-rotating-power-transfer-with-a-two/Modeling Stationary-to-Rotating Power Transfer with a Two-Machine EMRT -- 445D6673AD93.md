# Modeling Stationary-to-Rotating Power Transfer with a Two-Machine EMRT

## A Governed Reference Model, Simulation Study, and Bench Validation Plan

### The wire may stay still; the torque does not disappear.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

An Electro-Mechanical Rotational Transformer (EMRT) is a two-machine arrangement that can deliver electrical power to a rotating carrier without a galvanic power contact in the modeled transfer path. One motor has a fixed case and drives the carrier; a second machine has its case, windings, converter, capacitor, and load on the carrier while its rotor shaft is fixed to the housing. This paper makes the resulting reference frames, reaction torques, electrical ports, stored energy, losses, and thermal states explicit in an averaged surface permanent-magnet synchronous-machine model. Under assigned, uncalibrated parameters, a load step from 24 W to 48 W at 100 rad/s produces a maximum carrier-speed deviation of 0.02879 rad/s with filtered reaction-torque feedforward plus speed feedback. The two-second run draws 127.782 J from the stationary source, delivers 86.398 J to the rotating resistor, and closes the integrated energy ledger to within 1.18e-08 J. Mechanical telemetry and a separate optical signaling concept are evaluated under assigned noise. The results establish reproducibility and accounting properties of one reference simulation. They do not establish hardware performance, comparative efficiency, historical priority, a novel energy mechanism, or permission to construct or operate a machine.

## 1. Source, evidence, and standing

This manuscript is an AI-assisted editorial conversion of the sealed EMRT C1 research package prepared under the author's direction. Its technical claims, numerical results, figures, and qualifications descend from the exact C1 evidence set. The conversion adds corpus-standard structure, an explicit claim ladder, primitives, invariants, configuration dimensions, realization stages, cross-corpus comparisons, and publication metadata. The author reviewed and adopted this publication edition.

The evidence available here is local software evidence. Hardware was not run; calibration certificates were not supplied; the modeled parameters and noise levels are assigned; novelty was not established; and external acceptance is absent. The software evidence has `authority_effect: NONE`. Electro-Mechanical Rotational Transformer (EMRT) is the author-confirmed name and expansion for the two-machine arrangement described here.

The Direct-Coupled Dynamic Torque Reactor (DCDTR) is an exact, separately custodied Ableman framework that motivates explicit torque, storage, thermal, and admissibility constraints. It does not specify, validate, or become identical to EMRT. The Ableman Wheel is also a separate experimental work identity. Similarities among rotating systems do not merge their artifacts, claims, or evidence.

## 2. Research question and claim ladder

The engineering question is narrow:

> When a generator's case and winding terminals rotate while its shaft is fixed, how should stationary electrical input, carrier torque, rotating electrical demand, stored energy, losses, and observation paths be represented and tested?

The paper makes four bounded claims.

1. **Topological claim.** The two-machine arrangement supplies a physically ordinary path from stationary electrical input through M1 mechanical torque to M2 electrical output on a rotating carrier.
2. **Accounting claim.** The reduced model can keep independent electrical, mechanical, storage, loss, dump, and thermal ledgers whose residuals remain small under the tested numerical configurations.
3. **Control claim.** In the assigned reference model, filtered fixed-shaft reaction-torque feedforward and speed feedback reduce speed droop relative to fixed torque and feedback-only policies.
4. **Experimental claim.** The model produces falsifiable measurement and comparison requirements for a guarded low-power bench trial.

The paper does **not** claim that the arrangement is historically novel, more efficient than slip rings or inductive rotary transfer, ready for fabrication, safe at any named rating, reactionless, self-powering, or validated outside simulation.

## 3. System identity and topology

Let the external housing be fixed in the laboratory. M1 has a fixed case and a rotor shaft that drives a carrier at angular speed $\omega$. M2 has a case, windings, converter, capacitor, and resistor fixed to that carrier, while its rotor shaft is held by the stationary housing.

![Two-machine EMRT topology and reference frames.](../assets/emrt-topology.png)

The relative rotor-to-case speed is $+\omega$ for M1 and $-\omega$ for M2. Positive M2 rotor torque therefore produces equal negative torque on the rotating case. The stationary M2 shaft may react nonzero torque while having zero laboratory angular speed and zero laboratory shaft power. The M2 rotating case remains a nonzero mechanical power port. The carrier supplies the mechanical power converted by M2, so M1 or stored kinetic energy must pay for the load and losses.

Describing the modeled transfer path as free of galvanic contact does not erase these reactions. It only states that the modeled stationary-to-rotating power path crosses through mechanical coupling rather than a sliding electrical contact.

## 4. Primitive set

The minimum descriptive objects are:

- a stationary housing and stationary electrical source;
- M1 fixed stator/case, rotor, shaft, converter, and loss ports;
- a rotating carrier with total moving inertia $J$;
- M2 rotating case, stator windings, converter, DC bus, capacitor, and load;
- an M2 rotor shaft fixed to the housing;
- rotor-to-case angular speed and equal-and-opposite torque reactions;
- electrical, magnetic, kinetic, and capacitor energy stores;
- copper, iron, converter, bearing, windage, and thermal-loss ports;
- a reserved dump or regenerative-sink port;
- local current, voltage, speed, angle, temperature, and torque observations;
- optional mechanical and optical telemetry paths; and
- evidence objects binding configuration, source, results, and review state.

These primitives are descriptive, not a bill of materials. They do not specify bearings, insulation, containment, wiring, fusing, clearances, grounding, or safe operating limits.

## 5. Invariants and refusal conditions

The model is governed by the following invariants.

1. **Frame invariant.** M1 and M2 electrical speeds are computed from their own rotor-to-case relative speeds, not from an undifferentiated laboratory speed.
2. **Reaction invariant.** M2 rotor torque and case torque are equal and opposite; generator action cannot disappear from the carrier equation.
3. **Fixed-support invariant.** Zero laboratory shaft power at the fixed M2 rotor does not imply zero reaction torque or zero carrier power.
4. **Energy invariant.** Source energy equals load energy, declared losses, dump energy, and net change in stored kinetic, magnetic, and capacitor energy within numerical residual.
5. **Thermal invariant.** Loss energy may enter a thermal ledger but may not be counted twice as both an unexplained loss and a second energy source.
6. **Independent-port invariant.** Electrical and mechanical terminal powers are calculated independently; neither is defined as the other's balancing remainder.
7. **Provenance invariant.** Assigned values remain labeled assigned. A simulation fit cannot silently become calibration.
8. **Comparison invariant.** Control policies are compared from declared initial state, load schedule, limits, and service target. Lower source draw accompanied by loss of speed or stored energy is not higher efficiency.
9. **Evidence invariant.** A small numerical residual verifies accounting under a model; it does not verify the model against hardware.
10. **Authority invariant.** A readable telemetry channel does not grant permission to actuate equipment.

Prediction refuses to continue when declared current, voltage, speed, bus, temperature, or sensor-validity boundaries are crossed. Such refusal is a software-domain boundary, not proof of hardware protection.

## 6. Machine and energy equations

The averaged model uses the peak, amplitude-invariant balanced $dq$ convention. For each machine,

$$
v_d = R i_d + L_d\frac{di_d}{dt} - p\omega_{rel}L_q i_q,
$$

$$
v_q = R i_q + L_q\frac{di_q}{dt} + p\omega_{rel}(L_d i_d + \psi),
$$

$$
\tau = \frac{3}{2}p\left[\psi i_q + (L_d-L_q)i_di_q\right].
$$

The admitted surface-machine configuration sets $L_d=L_q$. Electrical terminal power, stored magnetic energy, and the machine balance are

$$
P_{ac}=\frac{3}{2}(v_di_d+v_qi_q),
$$

$$
E_{mag}=\frac{3}{4}(L_di_d^2+L_qi_q^2),
$$

$$
P_{ac}-\frac{3}{2}R(i_d^2+i_q^2)-\tau\omega_{rel}=\frac{dE_{mag}}{dt}.
$$

The last identity was checked algebraically over 500 seeded parameter-and-state samples, including saliency in the general machine primitive. Copper resistance uses an assigned linear coefficient of $0.00393/K$ at $20$ deg C. Constant magnetic parameters and lumped iron and converter losses do not constitute a material field solution.

The carrier, bus, and total energy equations are

$$
J\frac{d\omega}{dt}=\tau_1-\tau_2-\tau_{bearing}-\tau_{iron},
$$

$$
\frac{dE_{cap}}{dt}=-P_{ac2}-P_{inverter2}-\frac{V_{bus}^2}{R_{load}},
$$

$$
E_{in}-E_{load}-E_{loss}-E_{dump}=\Delta(E_{kin}+E_{mag}+E_{cap}).
$$

![Declared power and energy paths.](../assets/emrt-energy-ledger.png)

The baseline uses an assigned bidirectional stiff stationary source. A separately declared source-isolated experiment uses an ideal three-phase short rather than an unmodeled open or freewheel circuit. Initial rotational and capacitor energy remain in the ledger. The dump port is reserved but zero in C1; excess energy may not be silently discarded.

## 7. Control and numerical method

Local current PI controllers command bounded averaged $dq$ voltages. Voltage magnitude is screened at $V_{dc}/\sqrt{3}$ with back-calculation anti-windup. M2 locally regulates DC-link energy and uses a bounded low-current root for steady generation demand. M1 is evaluated under four policies:

- fixed torque;
- speed feedback;
- filtered reaction-torque feedforward; and
- feedforward plus speed feedback.

Feedforward observes M2 fixed-shaft reaction torque through an assigned 3 ms filter. It does not assume instantaneous access to the rotating load signal. Optional virtual inertia uses acceleration feedback, while a separate speed-error term provides damping. Both act through the source power port; neither changes physical mass or guarantees stability.

The plant is integrated with RK4 while controller voltage is held between discrete updates. Load and fault boundaries split time steps. Because controller integration is discrete, the complete closed loop is not claimed to have fourth-order convergence. The baseline time step is 0.2 ms with 2 ms recording; a half-step run measures numerical sensitivity.

![Control, observation, and optional telemetry paths.](../assets/emrt-control-telemetry.png)

## 8. Assigned experiments and results

The first four runs differ only in M1 compensation policy. They are operating-point comparisons under assigned parameters, not hardware efficiency tests.

| Policy | Source energy (J) | Load energy (J) | Maximum speed error (rad/s) | Minimum bus voltage (V) |
|---|---:|---:|---:|---:|
| Fixed torque | 66.668 | 86.395 | 19.67918 | 23.97784 |
| Feedback only | 127.848 | 86.398 | 0.38119 | 23.97785 |
| Feedforward | 127.685 | 86.398 | 0.03222 | 23.97785 |
| Feedforward plus feedback | 127.782 | 86.398 | 0.02879 | 23.97785 |

The fixed-torque run draws less source energy because it consumes stored rotation and loses service. It is therefore not an efficiency winner. At the final baseline operating point, the rotating load receives 48.000 W at 24.000 V and 2.000 A, stationary input is 70.845 W, and M2 electromagnetic braking magnitude is 0.54800 N m. That instantaneous conversion ratio is neither mission efficiency nor a selected motor rating.

Reducing capacitance from 50 mF to 5 mF lowers the minimum bus voltage from 23.97785 V to 23.78687 V. Limiting the stationary source to 12 V produces 53.853 rad/s maximum speed error and severe service degradation. In the source-isolated short case, source energy is exactly zero and the load is supplied from initial stored energy; this is not sustained power transfer.

The baseline maximum energy residual is $1.18\times10^{-8}$ J. Halving the time step changes integrated load energy by 0.000192 J and peak speed-error magnitude by 0.00038 rad/s. Twelve seeded Latin-hypercube cases vary four assigned parameter groups over $\pm10$ percent. This is sensitivity sampling within a declared box, not a confidence interval, uncertainty distribution, or coverage proof.

## 9. Signaling experiments

The mechanical downlink deliberately modulates M1 torque while a rotating receiver observes M2 terminal $q$ voltage. The uplink modulates onboard conductance while a stationary receiver observes source current. Observation samples, not transmitted truth labels, enter the detector; decoded bits are compared with truth only during later scoring.

Each deterministic trial sends a 192-bit frame at 10 bit/s using 30 and 50 Hz FSK. The downlink uses 0.1 N m torque modulation with 50 microvolt assigned Gaussian observation noise. The uplink uses 10 percent conductance modulation with 100 microampere assigned Gaussian current noise. Both recover the payload and CRC in this one case. Zero observed errors in one short frame is not a characterized bit-error rate. No-link controls test erasure behavior. The stiff stationary voltage source provides no voltage data observable in this model, and tight DC-bus regulation can suppress a rotating voltage signature.

The separate optical concept uses four detectors. Complementary detector sums carry emitter modulation while normalized differences estimate track phase. The default assigned 20/30 kHz carrier pair, 80 kHz detector bandwidth, and 320 ksample/s clock recover eight bits with approximately 0.000140 mechanical radian RMS track-angle error. The estimate is modulo one track; absolute revolution identity is not inferred. A data-off control produces erasures, an imposed dropout is visible, and 10 percent detector-gain mismatch raises RMS error to approximately 0.000978 rad. These are assigned simulation results, not encoder-retrofit or hardware data-rate claims.

## 10. Configuration dimensions

The work separates the following dimensions so that changing one does not silently change another:

- **frame:** laboratory, carrier, rotor-to-case;
- **energy domain:** stationary electrical, mechanical, rotating electrical, stored, loss, thermal;
- **port role:** source, converter, reaction, store, load, dump, observation;
- **parameter provenance:** assigned, measured, identified, calibrated;
- **controller policy:** fixed, feedback, feedforward, combined, optional virtual inertia;
- **communication path:** torque-to-voltage, load-to-current, optical quadrature;
- **evidence class:** algebraic check, deterministic simulation, sensitivity run, UI receipt, measured bench evidence;
- **safety standing:** model screen, independent protection, rated component limit, operating authorization.

## 11. Realization stages

The following stage map is a local editorial projection. The phrase "realization funnel" is not treated here as a separately resolved controlled term.

| Stage | EMRT state |
|---|---|
| Possibility | A non-galvanic stationary-to-rotating power path using two ordinary machines and a shared carrier. |
| Specification | Frames, ports, equations, controls, evidence obligations, and refusal boundaries. |
| CM1 | Physically or formally admissible configurations, including source-starved, unstable, inefficient, or otherwise undesirable cases. |
| CM2 | Preferred configurations that preserve service, bounded states, independent protection, measurement quality, and matched comparisons. |
| Instance Configuration | The exact assigned C1 baseline and named fault/sensitivity variants. |
| Implementation Realization | A bounded Windows synchronous simulator; no hardware and no network control path. |
| Evidence | Hash-bound local results, deterministic replays, balance checks, and UI receipts; no external acceptance. |
| Revision | Measured machine characterization, low-power bench work, matched alternatives, uncertainty treatment, and author review. |

## 12. Failure modes and countertests

The most important failure modes are not hidden behind aggregate success.

- **Frame collapse:** treating all angular speeds as laboratory speed gives the wrong M2 electrical sign.
- **Reaction deletion:** omitting M2 case torque creates an apparent source of carrier power.
- **Storage laundering:** calling lower source energy an efficiency gain while consuming kinetic or capacitor energy.
- **Loss laundering:** using an unexplained residual as a dump or heat port.
- **Calibration laundering:** presenting assigned parameters or noise as measured hardware behavior.
- **Numerical laundering:** treating ledger closure as model validation.
- **communication laundering:** treating one decoded deterministic frame as a channel characterization.
- **safety laundering:** treating simulation stops as independent hardware protection.
- **identity laundering:** treating EMRT as DCDTR, the Ableman Wheel, or an established corpus identity without adjudication.

Required countertests include sign reversal and power-flow checks; matched initial and terminal storage; source-voltage and source-isolation tests; sensor-loss refusal; time-step sensitivity; parameter sensitivity; no-link and data-off controls; independent torque, electrical, thermal, and speed observations; and comparison against conventional rotary-transfer alternatives under matched service.

## 13. Corpus relationships

EMRT is best understood as a bounded engineering realization candidate adjacent to, but not identical with, several Ableman works.

- **Direct-Coupled Dynamic Torque Reactor.** Supplies a broader framework for governed multi-substrate torque, storage, and thermal composition. EMRT contributes a narrower two-machine reference model and bench-measurement contract. The corpus concepts "Governed Multi Substrate Energy Manifold," "Sibling Consequences of Mechanical Coupling," and "Objective Pluralism and Domain Constraints" are reviewed-provisional integration syntheses, not EMRT source wording.
- **The Ableman Wheel.** Shares concern for narrow experimental jurisdiction and structural falsifiability. It remains a separate apparatus, hypothesis set, and work identity.
- **Reasoning by Way of Receipts.** Provides an adjacent evidentiary discipline: successful computation should remain bound to configuration, source, result, and claim ceiling. EMRT's local receipts do not promote simulation into hardware evidence.
- **Effect Sovereignty.** Clarifies why telemetry and model controls do not authorize physical actuation. Future hardware integration would require separately governed effects and independent safety authority.

These are comparison links, not derivation claims, identity mergers, or external validation.

## 14. Limits and next experiments

The model omits switching waveforms, saturation, hysteresis, distributed eddy currents, shaft flexibility, detailed bearing and windage physics, cooling flow, and structural containment. Fixed losses and cooling coefficients are assigned. Regulation-loop delay and noise need measured transfer functions. The optical error metric covers a track period rather than absolute revolution identity. Communication framing lacks clock acquisition, channel authentication, and authorization to control equipment.

The next defensible sequence is:

1. select actual machines, converters, sensors, and a low-power resistor load;
2. measure resistance, inductance, magnet flux, inertia, loss, delay, noise, and thermal behavior;
3. establish independent overspeed, overcurrent, overvoltage, thermal, precharge, guarding, containment, and regenerative-sink protections;
4. run a low-power stationary test before any rotating-load configuration;
5. close electrical, torque, speed, storage, loss, and thermal ledgers with calibrated instruments;
6. compare control policies from matched initial and terminal storage with identical delivered service;
7. compare mechanical telemetry against regulation and loading, and optical telemetry against an independent encoder; and
8. only then compare slip rings, inductive rotary transfer, or other machines on efficiency, mass, maintenance, noise, cost, and failure behavior.

## 15. Conclusion

The two-machine EMRT model makes stationary-to-rotating power transfer explicit as electrical-to-mechanical-to-electrical conversion. Under one assigned configuration, coordinated source torque reduces speed droop and buffers a rotating load while generator braking, losses, and stored energy remain visible. The work's present contribution is a reproducible reference model, a disciplined energy ledger, and a falsifiable bench plan. It is not a new energy mechanism, implemented machine, demonstrated efficiency advantage, or priority claim.

## References

### External technical sources

[1] MathWorks. [*PMSM documentation*](https://www.mathworks.com/help/simscape-electrical/ref/pmsm.html). Balanced $dq$ voltage and torque convention.

[2] Modelica Association. [*PartialBasicMachine interface*](https://doc.modelica.org/Modelica%203.2.3/Resources/helpWSM/Modelica/Modelica.Electrical.Machines.Interfaces.PartialBasicMachine.html). Relative rotor and support motion.

[3] National Bureau of Standards. [*Copper Wire Tables*](https://nvlpubs.nist.gov/nistpubs/Legacy/hb/nbshandbook100.pdf). Handbook 100.

[4] Texas Instruments. [*Quick Response Control of PMSM Using Fast Current Loop*](https://www.ti.com/lit/an/spracl1b/spracl1b.pdf). SPRACL1B, 2020.

[5] Fraunhofer IPMS. [*Li-Fi Ligion*](https://www.ipms.fraunhofer.de/en/Components-and-Systems/Components-and-Systems-Data-Communication/Li-Fi-Data-Communication/Li-Fi-Ligion.html). Optical rotary data communication example.

### Ableman corpus

[A1] Adam Ableman. *Direct-Coupled Dynamic Torque Reactor*. Exact source head SHA-256 `1A88545BA054458260F82862F7BB9D658000C1326CDF8CA63216A2E4FBCA8B91`. Separate logical work; unpublished or no publication link in the supplied corpus index.

[A2] Adam Ableman. *The Ableman Wheel*. Exact source head SHA-256 `D011E7E025951AF869FDDBE768950719D0F15FCF6CFCBF9830131A9E1BFB2343`. Separate logical work; unpublished or no publication link in the supplied corpus index.

[A3] Adam Ableman. *Reasoning by Way of Receipts*. Exact source head SHA-256 `8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`. Adjacent evidence-governance work; no identity effect.

[A4] Adam Ableman. *Effect Sovereignty*. Exact source head SHA-256 `3CEC03F772430AC144ACD9F6C9CECF30D34C51C8B9F8B97F07E3FE7536171729`. Adjacent effect-governance work; no implementation authority.

## Research, provenance, and artifact statement

The sealed C1 source PDFs, source map, research results, and evidence binding remain unchanged. This publication edition is AI-assisted and was authorized for publication after author review. No external literature search was performed during this conversion. Existing references were retained from the sealed source package; corpus links were added from the governed Ableman semantic index. The conversion does not establish novelty, peer review, hardware validation, safety certification, corpus identity merger, or implementation authority.

---

Corpus source and companion formats:  
[https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)  
DOI: [https://doi.org/10.5281/zenodo.23933287](https://doi.org/10.5281/zenodo.23933287)

---

DOI: [10.5281/zenodo.23933287](https://doi.org/10.5281/zenodo.23933287)
