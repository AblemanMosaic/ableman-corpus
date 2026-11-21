# EMRT Technical Brief

## Stationary Power for a Rotating Electrical Load

### The load may rotate; the ledger still has to balance.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

The Electro-Mechanical Rotational Transformer (EMRT) is a two-machine arrangement that delivers electrical power to a rotating load without a galvanic stationary-to-rotating contact in the modeled transfer path. A stationary-case motor drives a carrier. A second machine carries its case, windings, converter, capacitor, and load on that carrier while its rotor shaft is fixed to the housing. The carrier supplies the generator's mechanical power, so reaction torque, source power, stored energy, losses, and heat must remain explicit. A bounded Windows simulator demonstrates this accounting under assigned parameters and produces a bench-validation plan. It does not demonstrate a finished machine, a safe construction, comparative efficiency, historical priority, or a new energy mechanism.

## 1. Publication and evidence standing

This is an AI-assisted editorial conversion of the sealed EMRT C1 technical brief, reviewed and authorized by the author for publication. Hardware was not run, calibration was not supplied, and all current performance values are simulation results under assigned parameters. Electro-Mechanical Rotational Transformer (EMRT) is the author-confirmed name and expansion used by this publication.

The Direct-Coupled Dynamic Torque Reactor and the Ableman Wheel are comparison targets, not alternate names for this module. No identity merger or construction authority follows from this document.

## 2. Architecture in one page

![Two-machine EMRT topology and reference frames.](../assets/emrt-topology.png)

- **M1:** fixed case, rotating shaft, drives the carrier from a stationary electrical source.
- **Carrier:** supports M1's driven shaft, M2's rotating case, M2 converter, capacitor, and load.
- **M2:** rotating case and windings, fixed rotor shaft, converts carrier mechanical power into onboard electrical power.
- **Fixed housing:** reacts the M2 rotor torque at zero laboratory shaft speed.
- **Rotating DC link:** supplies an onboard resistor in the C1 model.

M2's fixed shaft may carry nonzero torque at zero laboratory power. The rotating case is still a mechanical power port. When M2 generates, its case torque brakes the carrier. M1 or stored kinetic energy must supply that demand.

## 3. What the current application provides

The Windows application exposes assigned speed, stationary source voltage, rotating bus voltage, load resistance, capacitance, and ambient temperature. Mosaic UI controls select compensation policies, fault experiments, and scientific trace sets. Plots show power, torque, speed, voltage, current, fundamental reactive power, temperature, and balance residuals. Export preserves the exact run configuration and traces in a fresh hash-bound directory.

The application is a bounded synchronous simulator, not real-time firmware. It has no hardware or network-control path. Current, voltage, speed, bus, temperature, and sensor-validity limits stop future prediction, but those screens are not hardware ratings or independent protection.

## 4. Baseline result

The assigned reference case runs at 100 rad/s. The load steps from 24 W to 48 W. With filtered M2 reaction-torque feedforward plus M1 speed feedback:

| Quantity | C1 result |
|---|---:|
| Maximum carrier-speed deviation | 0.02879 rad/s |
| Stationary-source energy, 2 s | 127.782 J |
| Rotating-load energy, 2 s | 86.398 J |
| Minimum rotating-bus voltage | 23.97785 V |
| Maximum integrated energy residual | 1.18e-08 J |
| Final load operating point | 48.000 W at 24.000 V and 2.000 A |
| M2 electromagnetic braking magnitude | 0.54800 N m |

These values verify one software configuration. They are not component ratings, uncertainty bounds, or measured hardware performance.

## 5. What the control comparison shows

| M1 policy | Maximum speed error (rad/s) | Interpretation |
|---|---:|---|
| Fixed torque | 19.67918 | Stored rotation supplies part of the load; service degrades. |
| Speed feedback | 0.38119 | Feedback restores speed but reacts after error. |
| Torque feedforward | 0.03222 | Filtered fixed-shaft reaction torque anticipates load. |
| Feedforward plus feedback | 0.02879 | Best result in the assigned C1 comparison. |

The comparison does not show that one policy is generally optimal. It shows that a causal fixed-shaft torque observation can improve the assigned model without assuming direct access to the onboard load signal.

Reducing the capacitor from 50 mF to 5 mF increases bus disturbance. Restricting the source to 12 V produces 53.853 rad/s maximum speed error and degrades delivered service. Isolating the stationary source gives exactly zero source energy and runs the load from initial stored energy. None of these cases permits energy to appear without a declared source or store.

## 6. Evidence and accounting rules

![Declared power and energy paths.](../assets/emrt-energy-ledger.png)

The following rules are mandatory for interpreting any EMRT result:

1. calculate electrical and mechanical terminal power independently;
2. retain equal-and-opposite M2 reaction torque;
3. account for kinetic, magnetic, and capacitor storage;
4. declare copper, iron, converter, bearing, windage, dump, and thermal ports;
5. compare controllers under matched service and storage conditions;
6. distinguish assigned, measured, identified, and calibrated parameters;
7. treat a small numerical residual as accounting evidence, not hardware validation; and
8. retain the exact configuration and source binding for each result.

## 7. Communication options

The mechanical downlink modulates M1 torque and observes M2 terminal $q$ voltage on the carrier. The uplink modulates onboard conductance and observes stationary source current. One deterministic 192-bit frame at 10 bit/s was recovered in each direction under assigned Gaussian observation noise. Zero errors in one short simulation is not a characterized channel error rate.

The separate optical concept uses complementary detector sums for data and normalized differences for track phase. Under assigned 20/30 kHz carriers, 80 kHz detector bandwidth, and 320 ksample/s sampling, it recovers eight bits with approximately 0.000140 rad RMS track-angle error. The angle is modulo one track, not an absolute revolution identity. Data-off and dropout controls produce erasures. Ten percent detector-gain mismatch raises the RMS angle error.

Neither channel supplies authentication, clock-acquisition proof, permission to actuate machinery, or a hardware data-rate result.

## 8. What must precede a prototype

- Select actual machines, converters, sensors, bearings, support geometry, and a low-power dummy load.
- Measure resistance, inductance, magnet flux, inertia, losses, sensor delay, sensor noise, and thermal response.
- Establish phase and line conventions, ratings, precharge, fusing, grounding, insulation, guarding, containment, overspeed protection, overcurrent protection, thermal protection, watchdog behavior, and a regenerative sink or rated dissipation path.
- Close electrical, torque, speed, storage, loss, and thermal ledgers with calibrated instruments.
- Compare policies from matched initial and terminal storage while delivering identical service.
- Compare against slip rings, inductive rotary transfer, and relevant existing machines before claiming an advantage.

The near-term research target is a guarded, low-power resistor-load demonstrator with independent energy accounting. The present software is a basis for designing that experiment, not permission to operate a rig.

## 9. Corpus position

- *Direct-Coupled Dynamic Torque Reactor* is a broader governed-energy framework; it does not specify or validate EMRT.
- *The Ableman Wheel* supplies an adjacent example of narrow experimental jurisdiction and falsifiability; it is a separate apparatus and work identity.
- *Reasoning by Way of Receipts* helps keep successful computation bound to its configuration and claim ceiling.
- *Effect Sovereignty* helps distinguish observation from permission to produce physical effects.

These are contextual bridges only. They do not establish derivation, endorsement, identity, novelty, or implementation authority.

## 10. Review decision

The work is published as a simulation paper and experimental plan. It is not ready to be represented as validated electromechanical hardware. The technical brief and schematics are separately citable companions to the academic manuscript.

## References

[1] MathWorks. [*PMSM documentation*](https://www.mathworks.com/help/simscape-electrical/ref/pmsm.html).

[2] Modelica Association. [*PartialBasicMachine interface*](https://doc.modelica.org/Modelica%203.2.3/Resources/helpWSM/Modelica/Modelica.Electrical.Machines.Interfaces.PartialBasicMachine.html).

[3] National Bureau of Standards. [*Copper Wire Tables*](https://nvlpubs.nist.gov/nistpubs/Legacy/hb/nbshandbook100.pdf). Handbook 100.

[4] Texas Instruments. [*Quick Response Control of PMSM Using Fast Current Loop*](https://www.ti.com/lit/an/spracl1b/spracl1b.pdf). SPRACL1B, 2020.

[5] Fraunhofer IPMS. [*Li-Fi Ligion*](https://www.ipms.fraunhofer.de/en/Components-and-Systems/Components-and-Systems-Data-Communication/Li-Fi-Data-Communication/Li-Fi-Ligion.html).

[A1] Adam Ableman. *Direct-Coupled Dynamic Torque Reactor*. Exact source head SHA-256 `1A88545BA054458260F82862F7BB9D658000C1326CDF8CA63216A2E4FBCA8B91`.

[A2] Adam Ableman. *The Ableman Wheel*. Exact source head SHA-256 `D011E7E025951AF869FDDBE768950719D0F15FCF6CFCBF9830131A9E1BFB2343`.

## Research, provenance, and artifact statement

This brief is an AI-assisted conversion of sealed local evidence, authorized by the author for publication after review. No external research, hardware run, calibration, safety review, corpus identity merger, or implementation authorization occurred during conversion.

---

Corpus source and companion formats:  
[https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)  
DOI: [https://doi.org/10.5281/zenodo.23933289](https://doi.org/10.5281/zenodo.23933289)

---

DOI: [10.5281/zenodo.23933289](https://doi.org/10.5281/zenodo.23933289)
