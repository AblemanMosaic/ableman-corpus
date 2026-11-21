# EMRT Conceptual Schematics

## Frames, Power Paths, Control, and Telemetry

### Every rotating box still owes the ledger a reaction.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## 1. Scope and standing

These conceptual schematics accompany the published Electro-Mechanical Rotational Transformer (EMRT) manuscript and technical brief. They describe reference frames, functional power paths, controls, and observation channels for a two-machine simulation. They are **not fabrication drawings, wiring diagrams, safety drawings, component selections, or operating instructions**.

No bearing arrangement, shaft fit, insulation system, containment design, conductor size, fuse, ground bond, creepage distance, clearance, snubber, precharge circuit, regenerative sink, or safe rating is specified. The source-isolated three-phase-short case is a model condition, not a recommended hardware shutdown. Hardware was not run and calibration was not supplied.

Electro-Mechanical Rotational Transformer (EMRT) is the author-confirmed name and expansion used by this publication. The Direct-Coupled Dynamic Torque Reactor and the Ableman Wheel remain separate work identities.

## 2. Frames and torque transfer

![Two-machine EMRT topology and reference frames.](../assets/emrt-topology.png)

### 2.1 Laboratory frame

The external housing, M1 case, M2 rotor shaft, stationary source, and supervisory observation surface are fixed in the laboratory frame.

### 2.2 Carrier frame

M1's rotor shaft drives the carrier. M2's case and windings, its averaged converter, capacitor, and load rotate with the carrier at angular speed $\omega$.

### 2.3 Relative machine speeds

| Machine | Case motion | Rotor motion | Rotor-to-case speed |
|---|---|---|---:|
| M1 | fixed | $+\omega$ | $+\omega$ |
| M2 | $+\omega$ | fixed | $-\omega$ |

Positive M2 rotor torque produces equal negative carrier-case torque. The fixed shaft reacts torque into the housing while its laboratory shaft power remains zero. The carrier supplies M2's generating mechanical power.

### 2.4 Carrier equation

$$
J\dot{\omega}=\tau_1-\tau_2-\tau_{bearing}-\tau_{iron}.
$$

The moving inertia $J$ includes the declared wheel or carrier inertia, M1 rotor inertia, and M2 case-side inertia. A virtual-inertia control term may change torque response, but it does not change physical mass.

## 3. Electrical and energy paths

![Declared power and energy paths.](../assets/emrt-energy-ledger.png)

### 3.1 Stationary side

The stationary source feeds an averaged M1 converter. M1 electrical terminal power becomes magnetic storage change, copper loss, declared iron and converter losses, and mechanical shaft power.

### 3.2 Rotating side

Carrier mechanical power enters M2 through its rotating case. M2 electrical output feeds an averaged rotating converter and DC link. The capacitor buffers the link; the C1 resistor consumes $V_{bus}^2/R_{load}$.

### 3.3 Total ledger

$$
E_{in}-E_{load}-E_{loss}-E_{dump}=\Delta(E_{kin}+E_{mag}+E_{cap}).
$$

The dump or regenerative-sink port is explicit even when zero. Energy may not be assigned to an unnamed residual. Heat is tracked through separate lumped nodes so declared electrical loss is not counted twice.

### 3.4 Functional block status

| Block | C1 standing | Not implied |
|---|---|---|
| M1 and M2 converters | Averaged voltage-command blocks | Transistor bridge, gate drive, switching loss, EMC, or safe design |
| DC capacitor | Assigned simulation value | Ripple-current rating, precharge, discharge, enclosure, or fault safety |
| Resistor load | Assigned simulation value | Construction, cooling, isolation, or rated dissipation |
| Source | Assigned bidirectional stiff source | Battery, supply, regenerative sink, or protection implementation |
| Thermal nodes | Lumped assigned calculation | Material field solution or validated cooling design |

## 4. Control and observation paths

![Control, observation, and optional telemetry paths.](../assets/emrt-control-telemetry.png)

### 4.1 Local controls

Each machine has a local current PI controller with bounded averaged $dq$ voltage and anti-windup. M2 regulates its DC-link energy. M1 may use fixed torque, speed feedback, filtered M2 reaction-torque feedforward, or their combination.

### 4.2 Feedforward path

The stationary fixed-shaft torque sensor supplies a causal observation through an assigned 3 ms filter. It does not transmit the onboard load command and does not provide instantaneous truth about rotating state.

### 4.3 Refusal path

Declared current, voltage, speed, bus, temperature, and sensor-validity limits stop future simulation. The stop is a prediction refusal. It is not an emergency stop, safety relay, independent protection channel, or authority to operate hardware.

## 5. Mechanical telemetry

### 5.1 Downlink

```text
stationary transmitter
    -> deliberate M1 torque modulation
    -> carrier speed / M2 electromagnetic response
    -> rotating observation of M2 terminal q voltage
    -> frame detector and later truth scoring
```

### 5.2 Uplink

```text
rotating transmitter
    -> deliberate conductance modulation
    -> M2 generating torque / source response
    -> stationary observation of source current
    -> frame detector and later truth scoring
```

C1 sends one 192-bit frame at 10 bit/s in each direction with assigned Gaussian observation noise. Successful decoding in that deterministic test is not a measured error rate, channel capacity, synchronization proof, or authentication result. A stiff stationary voltage source has no voltage data observable in this model. Tight DC regulation can suppress the rotating voltage signature.

## 6. Optical telemetry concept

```text
two optical data carriers
        |
        v
four complementary detectors
   |                     |
   +-- detector sums ----+--> data demodulation
   |
   +-- normalized differences --> track phase estimate
```

The default assigned case uses 20 and 30 kHz carriers, 80 kHz detector bandwidth, 320 ksample/s sampling, 1 percent gain mismatch, and assigned observation noise. It recovers eight bits and estimates track phase with about 0.000140 mechanical radian RMS error. The angle is modulo one track, not an absolute revolution identity. Data-off and dropout controls produce erasures; 10 percent detector-gain mismatch increases the RMS error to about 0.000978 rad.

A conventional two-way encoder does not automatically become a full-duplex data link. Independent duplex channels, measured detector response, optical containment, clock acquisition, authentication, and authorization remain separate obligations.

## 7. Bench realization boundary

The schematic becomes a hardware design only after all of the following are separately supplied and reviewed:

- selected machines and converters with phase, line, current, voltage, speed, torque, thermal, and insulation ratings;
- shaft, bearing, carrier, support, balance, guarding, containment, and overspeed analysis;
- source, precharge, discharge, regeneration, dump, fuse, breaker, ground, and emergency-stop design;
- calibrated torque, voltage, current, speed, temperature, and vibration instrumentation;
- failure analysis for sensor loss, controller loss, communication loss, source loss, load rejection, short circuit, and mechanical seizure;
- a staged low-power commissioning plan; and
- independent authority for physical actuation.

Until then, the diagrams remain explanatory projections of a software model.

## 8. Corpus and evidence boundary

The DCDTR source provides adjacent language for governed torque, storage, and thermal composition. The Ableman Wheel provides an adjacent discipline of narrow experimental jurisdiction and structural falsifiability. Reasoning by Way of Receipts provides an adjacent discipline for binding results to exact configurations. Effect Sovereignty provides an adjacent distinction between observation and authorized effect. None of those relations merges the works or validates EMRT hardware.

The sealed source schematics, source map, simulation results, and evidence binding remain unchanged. This AI-assisted successor edition was authorized by the author for publication after review. No external research, hardware run, calibration, corpus identity merger, or implementation authorization occurred during conversion.

---

Corpus source and companion formats:  
[https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)  
DOI: [https://doi.org/10.5281/zenodo.23933291](https://doi.org/10.5281/zenodo.23933291)

---

DOI: [10.5281/zenodo.23933291](https://doi.org/10.5281/zenodo.23933291)
