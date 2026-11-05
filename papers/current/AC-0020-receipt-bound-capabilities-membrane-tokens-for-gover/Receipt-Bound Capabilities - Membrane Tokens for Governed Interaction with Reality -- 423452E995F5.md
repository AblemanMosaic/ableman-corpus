# Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality

## Membrane Tokens for Governed Interaction with Reality

### Tokens that do not produce receipts are treated as epistemic non-events.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern computational systems rely heavily on tokens: authentication tokens, capability grants, API keys, session identifiers, and permissions. These tokens typically answer a narrow question—*may this action be attempted?*—while remaining silent on a more consequential one: *what evidence must exist that the action actually occurred, and under what constraints?* As a result, systems accumulate side effects without lineage, authority leaks through implicit trust, and execution is permitted to masquerade as fact.

This paper introduces **Receipt-Bound Capabilities (RBCs)**: a token discipline in which the validity of a capability is inseparable from the production of a corresponding receipt. An RBC does not merely authorize an action; it obligates evidence. Redemption of the token is complete only if it yields a verifiable, structured record of effect. Tokens that do not produce receipts are treated as **epistemic non-events**.

RBCs reframe tokens as **membrane primitives** rather than permissions: bounded interfaces through which a governed system may touch reality without surrendering authority or losing memory. By binding permission to proof at the point of interaction, RBCs neutralize untrusted backends, preserve replayability, and relocate legitimacy upstream of execution. This paper formalizes RBCs as a distinct, paper-worthy capability technique and situates them within a broader architecture of admissibility, refusal, and receipted memory.

---

## 1. Tokens Without Memory

Tokens are everywhere, but memory is not.

Most systems treat tokens as bearer objects: possession implies permission. Once redeemed, execution proceeds, and the system may optionally log success or failure. But the token itself does not bind the effect to an admissible epistemic artifact. Effects may occur without proof; claims substitute for evidence; and execution quietly accrues authority by default.

This produces familiar pathologies:

* effects occur without receipts,
* logs narrate rather than attest,
* backends are trusted rather than constrained,
* replay requires re-running the world,
* disputes collapse into interpretation rather than verification.

These failures intensify at system boundaries: operating systems, cloud APIs, blockchains, sensors, LLM tool calls, and foreign runtimes. Tokens open doors, but they do not enforce what must be brought back through the door.

The result is a porous membrane between governed logic and ungoverned reality.

---

## 2. From Permission to Obligation

Capability-based security correctly observes that *who* may act matters less than *what* may be done. Receipt-Bound Capabilities extend this insight further:

> In governed systems, what matters is not only what may be done, but what must be proven afterward.

A **Receipt-Bound Capability** is defined by two inseparable properties:

1. **Authorization** - the token permits a specific class of effect.
2. **Obligation** - the token requires production of a receipt describing that effect.

Redemption without a receipt is invalid.
Receipt without a valid token is invalid.
The two are co-defined.

An action is not complete when it is attempted, nor even when it is claimed to have succeeded, but when it returns admissible evidence of what occurred. RBCs therefore transform tokens from passive permissions into **epistemic contracts**.

RBCs are *membrane capabilities*: tokens that cannot be fully redeemed without generating a bound receipt.

---

## 3. The Membrane, Not the Nerve

Biologically, RBCs correspond not to nerves—which transmit intent—but to **cell membranes**:

* the membrane defines what may pass,
* passage is coupled to structural change,
* interaction with the environment is constrained and observable,
* unrecorded interaction is indistinguishable from non-interaction.

In architectural terms:

* admissibility governs what meanings may exist,
* expression governs what meanings may act,
* **RBCs govern what actions may count as having occurred**.

Without a membrane, an organism cannot maintain integrity.
Without RBCs, a governed system cannot maintain epistemic closure.

---

## 4. Formal Sketch: Receipt-Bound Redemption

An RBC can be defined as a triple $(C, E, R)$, where:

* $C$ is a capability identifier,
* $E$ is a *typed effect family* (including parameters and result types),
* $R$ is a receipt schema binding evidence of execution.

Each receipt schema minimally binds:

* the capability identifier $C$,
* a concrete effect instance $e \in E$ or a deterministic summary thereof,
* the execution boundary (backend or substrate),
* a timestamp or sequence coordinate,
* an outcome classification,
* a hash-stable payload describing results.

**RBC Law.**
An effect attempt $(C, e)$ is epistemically admissible *if and only if* it produces a receipt $r$ such that:

* $r \in R$,
* $r.C = C$,
* $r$ binds $e$ (or a deterministic projection of $e$).

If no such receipt is produced, the attempt is an **epistemic non-event**. The system state machine does not advance. Downstream reasoning must proceed *as if the effect never occurred*, except to register a fault or refusal against the backend.

*Example:* Consider an effect class such as persisting an object to storage. An RBC authorizes the attempt and requires a receipt binding the object identity, persistence boundary, and resulting content hash. If the backend produces no conforming receipt, the system does not advance its internal state; the persistence attempt has no epistemic standing. Execution may have occurred physically, but without a receipt it does not count within the governed system.

Receipts are not logs. They are semantic artifacts eligible for lineage.

---

## 5. Backend Neutralization

RBCs treat backends as untrusted substrates to be **contained**, not trusted.

When a governed system interfaces with a backend—filesystem, network, OS call, cloud API, LLM tool, or foreign runtime—the backend never receives ambient authority. It receives an RBC.

The backend may:

* succeed and produce a receipt,
* fail and produce a receipt,
* or produce nothing.

Only the first two outcomes exist epistemically.

This yields three immediate effects:

1. **Silent escalation is impossible.**
   Absence of a receipt collapses the interaction to non-existence.

2. **Claims without evidence are inert.**
   Assertion alone cannot advance system state.

3. **Backend heterogeneity is neutralized.**
   Diverse substrates are unified under a single membrane semantics.

The token does not encode trust.
It encodes **containment**.

---

## 6. Replay Without Re-Execution

Because RBC redemption is receipt-producing by definition, every reality-touching action becomes replay-addressable.

Replay does not require re-running the backend. It requires replaying the *receipt logic*:

* which capability was minted,
* under what admissibility conditions,
* what receipt was returned,
* how that receipt influenced subsequent state.

Effects become nodes in lineage graphs, not opaque side effects. RBCs therefore integrate directly with receipted memory systems: systems that reason over what has been proven to have occurred, rather than what was claimed or inferred.

---

## 7. Adversarial Pressure and Immune Response

RBCs provide a native immune response to semantic attack:

* **Flooding attacks** - token minting is governed upstream; redemption without receipts is inert.
* **Malicious but admissible actions** - effects are visible, typed, and contestable.
* **Backend deception** - lying requires forging receipts, which produces detectable artifacts.
* **Gap exploitation** - mismatches surface as refusal or explicit receipt mismatch, not silent drift.

RBCs do not eliminate deception.
They eliminate **unaccountable** deception.

As with biological immune systems, the goal is not to prevent all harm, but to preserve system identity under pressure.

---

## 8. Distinction from Prior Work

RBCs are related to, but distinct from, existing techniques:

* **Capability-based security** decides who may do what; RBCs decide what *evidence is mandatory* for an action to count.
* **Audit logs and event sourcing** allow events to be omitted or fabricated; RBCs make the proof artifact structurally necessary for state transition.
* **Proof-carrying code** binds proofs to programs; RBCs bind proofs to *effects*.
* **Zero-trust architectures** remove trust in identity and perimeter; RBCs add **obligated attestations** tied to specific actions.

The novelty lies in binding *permission* and *evidence* at the token level.

---

## 9. What RBCs Are Not

Receipt-Bound Capabilities are not:

* authentication tokens,
* identity credentials,
* access control lists,
* logging frameworks,
* monitoring tools.

They do not decide policy.
They do not infer intent.
They do not interpret meaning.

They ensure that **nothing touches reality without leaving a scar**.

---

## 10. Ingress--Egress Symmetry

Receipt-Bound Capabilities operate at the **egress boundary** of governed systems. Their conceptual counterpart, **Governed Semantic Tokens (GST)**, operates at the **ingress boundary**.

GST governs what is allowed to count as meaning.
RBCs govern what is allowed to count as having occurred.

Together, they form a closed epistemic membrane: meaning does not enter the system without governance, and reality is not touched without evidence. Authority is denied both to raw signals and to raw execution.

---

## 11. Implications

Within governed architectures, RBCs:

* operationalize the execution membrane,
* neutralize heterogeneous backends,
* preserve replayability without re-execution,
* make refusal first-class,
* bind execution to lineage.

Beyond any single system, RBCs suggest a general pattern for interacting with reality without surrendering epistemic control: in AI agents, financial systems, infrastructure orchestration, and civic technology.

---

## 12. Conclusion

Execution is cheap. Evidence is not.

Receipt-Bound Capabilities redefine tokens from permissions into obligations. By binding authority to proof, RBCs relocate legitimacy upstream of runtime and restore the boundary between acting and *having acted*.

In systems that act autonomously and persist beyond direct human oversight, the decisive question is no longer whether an action was allowed, but whether it can be *shown*.

RBCs answer that question mechanically.

A system that cannot demand receipts cannot distinguish action from assertion.

## Corpus-Wide Reference Positioning

This paper argues that modern computational systems rely heavily on tokens: authentication tokens, capability grants, API keys, session identifiers, and permissions. Its nearest external comparison fields are security, provenance, storage. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Fixity and preservation can keep bytes stable while representation dependencies, executability, interpretation, and institutional custody decay. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E2]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E3]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

**[E4]** Robert N. M. Watson, Simon W. Moore, Peter Sewell, and Peter G. Neumann. *An Introduction to CHERI*. University of Cambridge Technical Report UCAM-CL-TR-941, 2019. DOI: 10.48456/tr-941. [cl.cam.ac.uk source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-941.html) **Relationship:** Adjacent capability architecture demonstrating unforgeable hardware authority and compartmentalization.

**[E5]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E6]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E7]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

### Ableman corpus

**[A1]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *The Integrity Enforcement Layer*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-505307E9E6571B63`;  
source SHA-256  
`F858AB32E0937B796353CAE573DD4183FDF4F179A3E1E7E40C4E0C6BF1AB0018`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Constitutional Syscalls*. Ableman Corpus current edition; work identity `PAPER.PUB.18737229`;  
source SHA-256  
`5F14356180812262778F8574C292F4F6B560993042E5358B02EAB9CF0F7DE14C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.18601631](https://doi.org/10.5281/zenodo.18601631)
