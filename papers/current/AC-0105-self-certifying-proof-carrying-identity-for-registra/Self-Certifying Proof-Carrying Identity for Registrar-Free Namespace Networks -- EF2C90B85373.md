# Self-Certifying Proof-Carrying Identity for Registrar-Free Namespace Networks

## Toward Functionally Sovereign Self-Certifying Identity

### Self-Certifying Proof-Carrying Identity for Registrar-Free Namespace Networks binds what happened without claiming more than the evidence proves.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern network identity systems rely heavily upon external trust authorities for namespace legitimacy, continuity, and authenticity. Domain registrars, certificate authorities, centralized identity providers, and socially maintained trust graphs all place institutional governance layers above the cryptographic substrate itself.

This paper proposes a registrar-free identity architecture based on self-certifying cryptographic identifiers, proof-carrying attribution lineage, and authenticated operational continuity. Rather than treating identity legitimacy as institutionally granted, the framework treats identity legitimacy as emerging from admissible cryptographic continuity under a declared threat model.

The proposed framework introduces several compositional primitives:

• self-certifying identifier derivation

• potentially unsquattable under the assumed cryptographic threat model

• proof-carrying identity continuity

• provenance-scoped attribution validity

• continuity-sensitive session establishment

• operational attribution lineage

• scalable provenance density gradients

• collision-complete namespace derivation

The paper distinguishes authorship continuity, operational continuity, and semantic continuity as separate but composable continuity classes. The framework primarily addresses authorship continuity and operational continuity while leaving semantic continuity and constitutional meaning governance explicitly outside scope.

The resulting architecture permits self-announcing participants to exist within a mathematically self-certifying namespace while continuously proving attributable operational continuity without centralized registration authorities or externally delegated namespace legitimacy.

## 1. Introduction

Most network identity systems depend upon institutional legitimacy structures.

DNS names require registrars.

TLS systems require certificate authorities.

Social identity systems require platform ownership.

Even decentralized cryptographic systems frequently rely upon externally distributed trust anchors, manually exchanged keys, or socially maintained trust relationships.

This creates a persistent architectural pattern:

identity legitimacy exists above the cryptography rather than emerging directly from it.

Cryptographic signatures prove authorship of messages.

They do not independently establish sovereign ownership of the namespace itself.

As a result, operational identity continuity is often externalized into institutions, social trust systems, administrative infrastructure, or manual coordination.

This paper explores an alternative model.

Instead of treating identity legitimacy as institutionally assigned, identity legitimacy is treated as cryptographically emergent under an explicitly declared threat model.

The namespace becomes self-certifying.

Ownership becomes proof-carrying.

Continuity becomes attributable.

Operational legitimacy emerges through admissible cryptographic lineage rather than delegated institutional authority.

## 2. Scope and Threat Model

The framework addresses a bounded class of identity and attribution problems.

The paper does not claim universal identity security under arbitrary adversarial conditions.

Instead, the framework operates under the following assumptions:

• modern asymmetric cryptographic primitives remain computationally secure

• participants maintain custody of private keys

• implementations correctly execute the specified protocols

• session integrity mechanisms are uncompromised

• cryptographic hashes remain collision resistant under practical adversarial constraints

The framework is specifically designed to resist:

• namespace squatting under correct cryptographic operation

• unauthorized attribution forgery

• replay across invalid operational scopes

• operational impersonation without key possession

• continuity disruption through non-authoritative message injection

The following classes remain explicitly outside scope:

• physical device compromise

• coercive key extraction

• malicious hardware

• social engineering

• side-channel attacks

• catastrophic cryptographic failure

• semantic governance disputes

• constitutional meaning drift

This boundary is important.

The framework primarily addresses cryptographic authorship continuity and operational attribution continuity.

It does not independently solve semantic legitimacy or governance-layer meaning disputes.

## 3. Definitions

Definition (Self-Certifying Identifier)

An identifier deterministically derived from cryptographic key material such that ownership claims may be mechanically verified without external registration authority.

Definition (Proof-Carrying Identity)

An identity model in which operational legitimacy derives from admissible cryptographic attribution continuity rather than static institutional assignment.

Definition (Authorship Continuity)

Persistence of attributable authorship under continuous possession of a cryptographic authority surface.

Definition (Operational Continuity)

Persistence of attributable participation across authenticated operational transitions.

Definition (Semantic Continuity)

Persistence of meaning equivalence across evolving interpretive or governance contexts.

Definition (Provenance Scope)

A cryptographically authenticated operational boundary within which attribution artifacts remain admissible.

Examples include:

• session scope

• transport scope

• routing scope

• relay scope

• operational epoch scope

## 4. The Identity Problem

Network identity systems must address three distinct properties:

1. uniqueness

2. authenticity

3. continuity

Most existing systems solve only subsets of these simultaneously.

**4.1 Uniqueness**

An identifier must distinguish one participant from all others.

Traditional systems frequently achieve uniqueness through centralized namespace arbitration.

Examples include:

• DNS allocation

• certificate issuance

• account registration

• authority-managed identity spaces

This introduces institutional dependency into namespace legitimacy.

**4.2 Authenticity**

A participant must prove authorship of communications associated with an identifier.

Public-key cryptography solves this effectively.

A valid signature proves possession of the corresponding authority surface.

However, authenticity alone does not establish namespace sovereignty.

**4.3 Continuity**

Identity is not merely instantaneous.

Meaningful operational identity persists across sessions, transports, and evolving operational states.

Traditional systems frequently externalize continuity into institutional infrastructure or social trust relationships.

The framework proposed here internalizes continuity directly into the attribution lineage itself.

## 5. Self-Certifying Namespace Construction

The foundational primitive is a self-certifying identifier derived directly from public key material.

Example construction:

$\mathrm{NodeID}=\mathrm{BLAKE3}(\mathrm{Ed25519\ Public\ Key})$

The resulting identifier possesses several important properties:

• deterministic derivation

• topology independence

• registrar independence

• authority independence

• public verifiability

• practical collision resistance

No external institution grants the identifier.

No registrar validates namespace ownership.

The namespace becomes self-certifying because identity emerges directly from the cryptographic substrate itself.

## 6. Potentially Unsquattable Namespace Ownership

A critical distinction exists between:

identifier uniqueness

and

namespace sovereignty.

Uniqueness alone is insufficient.

An adversary may publicly announce another participant’s identifier without possessing operational authority over it.

Namespace sovereignty emerges only when operational legitimacy is inseparable from cryptographic authorship continuity.

The framework therefore does not claim absolute unsquattability.

Instead, the framework aims to provide a potentially unsquattable namespace under the assumed cryptographic threat model.

Operational ownership derives from admissible signed attribution continuity rather than public announcement alone.

This distinction is foundational.

Anyone may announce a public identifier.

Only the holder of the corresponding private key may produce admissible attribution lineage associated with it.

The namespace therefore becomes effectively resistant to squatting under correct cryptographic operation and uncompromised key custody assumptions.

## 7. Proof-Carrying Identity

The framework introduces proof-carrying identity as a continuity model.

Identity legitimacy is not statically granted.

It is continuously re-proven through attributable cryptographic lineage.

Each signed attribution artifact becomes evidence of:

• authorship continuity

• operational continuity

• namespace authority continuity

• attributable participation continuity

This transforms identity from a static registration object into an accumulated continuity structure.

Traditional systems authenticate isolated events.

Proof-carrying identity authenticates attributable operational persistence through time.

This distinction is important.

The framework does not claim that continuity itself proves semantic legitimacy or governance legitimacy.

It claims only that continuity establishes attributable operational persistence under cryptographic authority continuity.

## 8. Attribution Lineage

Attribution lineage consists of cryptographically authenticated continuity artifacts.

Examples include:

• session establishment artifacts

• transport transition artifacts

• continuity receipts

• relay acknowledgements

• operational checkpoint signatures

• scope transition declarations

Each artifact extends the operational continuity surface associated with the identity.

Over time, attribution lineage accumulates historical structure.

A newly generated identifier possesses mathematical legitimacy but minimal operational continuity evidence.

A mature identifier accumulates thick attribution lineage.

This distinction enables continuity-sensitive trust assessment without centralized authorities.

## 9. Provenance Scope

A valid attribution artifact is admissible only within its authenticated provenance scope.

Examples include:

• session scope

• relay scope

• routing scope

• operational epoch scope

A provenance scope declaration contains:

• scope identifier

• scope authority surface

• scope validity duration

• transition lineage reference

• admissibility constraints

Scope declarations are themselves signed attribution artifacts.

This is important.

Replay resistance derives not merely from signature validity but from provenance admissibility.

A valid signature replayed outside its authenticated provenance scope becomes operationally inadmissible despite remaining cryptographically authentic.

## 10. Session Establishment and Operational Continuity

A simplified operational flow proceeds as follows:

1. Node derives self-certifying identifier from public key material.

2. Node announces signed session establishment artifact.

3. Peer verifies authorship proof.

4. Peers establish authenticated session through asymmetric key exchange.

5. Session integrity transitions to symmetric transport protection.

6. Operational continuity artifacts accumulate through ongoing attributable participation.

This architecture separates:

identity authentication

from

high-frequency transport integrity.

The attribution surface remains anchored in asymmetric cryptographic continuity while operational traffic benefits from efficient symmetric integrity enforcement.

## 11. Provenance Density Gradients

The framework permits variable attribution density.

Instead of asymmetrically signing every transport frame, participants may periodically produce signed attribution checkpoints while maintaining continuous symmetric session integrity.

Example:

N = 1

Every frame carries asymmetric attribution proof.

N > 1

Periodic frames carry asymmetric attribution while intermediate frames rely upon symmetric session integrity.

This optimization exists to reduce computational overhead while preserving meaningful authorship continuity evidence.

Unlike Byzantine sampling systems, the purpose here is not adversarial unpredictability.

The purpose is scalable provenance continuity under authenticated session integrity.

## 12. Collision Completeness

Cryptographic collisions within sufficiently large hash spaces are operationally improbable.

However, protocol completeness requires explicit collision semantics.

The framework therefore permits cascading derivation under detected collision conditions.

Example:

Generation 1:

ID_1=$\mathrm{BLAKE3}(PK)$

Generation 2:

ID_2=$\mathrm{BLAKE3}(ID_1\parallel PK\parallel Scope)$

Generation 3:

ID_3=$\mathrm{BLAKE3}(ID_2\parallel PK\parallel Scope\parallel Counter)$

The cascade mechanism exists for operational completeness rather than primary security.

Namespace legitimacy derives primarily from:

• private-key possession

• attributable continuity

• admissible provenance scope

• cryptographic integrity

## 13. Comparative Analysis

- **Property:** Registrar-Free  
  **TLS PKI:** No  
  **PGP:** Yes  
  **Manual Keys:** Yes  
  **Proposed Framework:** Yes

- **Property:** Self-Certifying IDs  
  **TLS PKI:** Partial  
  **PGP:** Partial  
  **Manual Keys:** Partial  
  **Proposed Framework:** Yes

- **Property:** Namespace Sovereignty  
  **TLS PKI:** Institutional  
  **PGP:** Social  
  **Manual Keys:** Local  
  **Proposed Framework:** Cryptographic

- **Property:** Attribution Continuity  
  **TLS PKI:** Weak  
  **PGP:** Weak  
  **Manual Keys:** Manual  
  **Proposed Framework:** Native

- **Property:** Provenance Scope Binding  
  **TLS PKI:** Limited  
  **PGP:** Minimal  
  **Manual Keys:** Manual  
  **Proposed Framework:** Explicit

- **Property:** Continuity Lineage  
  **TLS PKI:** No  
  **PGP:** Informal  
  **Manual Keys:** Manual  
  **Proposed Framework:** Native

- **Property:** Session Integrity Separation  
  **TLS PKI:** Yes  
  **PGP:** No  
  **Manual Keys:** Partial  
  **Proposed Framework:** Yes

- **Property:** Replay Scope Awareness  
  **TLS PKI:** Limited  
  **PGP:** Minimal  
  **Manual Keys:** Manual  
  **Proposed Framework:** Explicit

## 14. Limitations

The framework intentionally does not solve:

• semantic legitimacy

• constitutional governance

• interpretive meaning stability

• trustworthiness of participant intent

• endpoint integrity

• hardware compromise

• human deception

These remain distinct problem domains.

This limitation is intentional rather than accidental.

The framework focuses specifically on registrar-free cryptographic identity continuity and attributable operational participation.

## 15. Conclusion

Traditional network identity systems place institutional legitimacy layers above the cryptographic substrate.

The framework proposed here attempts to relocate legitimacy directly into attributable cryptographic continuity itself.

Identity becomes self-certifying.

Ownership becomes proof-carrying.

Continuity becomes attributable.

The resulting architecture permits self-announcing participants to operate within a potentially unsquattable namespace under the assumed cryptographic threat model while continuously proving attributable operational continuity without centralized registration authorities or socially delegated namespace governance.

This suggests a meaningful architectural transition:

from institutionally delegated identity legitimacy

to mathematically attributable identity continuity.

## Corpus-Wide Reference Positioning

This paper argues that modern network identity systems rely heavily upon external trust authorities for namespace legitimacy, continuity, and authenticity. Its nearest external comparison fields are crypto, security, distributed. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. Convergence and consensus establish agreement under a fault model; they do not establish that the agreed state is true, authorized, desirable, or semantically equivalent. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Anders Rundgren, Bret Jordan, and Samuel Erdtman. *JSON Canonicalization Scheme (JCS)*. RFC 8785, 2020. https://www.rfc-editor.org/rfc/rfc8785 **Relationship:** Adjacent canonicalization standard relevant to stable cryptographic commitments.

**[E2]** Ben Laurie et al. *Certificate Transparency Version 2.0*. RFC 9162, 2021. https://www.rfc-editor.org/rfc/rfc9162 **Relationship:** Adjacent append-only Merkle-log standard for inclusion and consistency evidence.

**[E3]** Manu Sporny et al., eds. *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 19 July 2022. https://www.w3.org/TR/did-core/ **Relationship:** Adjacent decentralized identity standard; identifier resolution is not assumed to settle semantic standing or jurisdiction.

**[E4]** Juan Benet. "IPFS - Content Addressed, Versioned, P2P File System." 2014. arXiv:1407.3561. https://arxiv.org/abs/1407.3561 **Relationship:** Predecessor content-addressed network architecture; content identity is compared with, not treated as sufficient for, semantic jurisdiction.

**[E5]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E6]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E7]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

### Ableman corpus

**[A1]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Semantic Hashing: Governed Commitment Schemes for Semantic Provenance, Admissibility, and Constitutional Continuity*. Ableman Corpus current edition; work identity `PAPER.PUB.20248734`;  
source SHA-256  
`B1DAC3E2CD4D57BAFBF6462BA6ACFFF7CF120CDB7FA37D0C173525744CC0A2F0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Cryptographic Admissibility and Jurisdiction*. Ableman Corpus current edition; work identity `PAPER.PUB.20602448`;  
source SHA-256  
`6094338D8706F63E8787A5E8DCF40F8A651C0FC3E5EA776DD61791566D094D38`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Semantic Hashing: Hashes as Declared Equivalence Classes of Meaning*. Ableman Corpus current edition; work identity `PAPER.PUB.18500533`;  
source SHA-256  
`7DA63A76DDF492FFC289F486923FB430879DC148CF3BB16EB0E755E2D4AB9C14`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Integrity Enforcement Layer*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-505307E9E6571B63`;  
source SHA-256  
`F858AB32E0937B796353CAE573DD4183FDF4F179A3E1E7E40C4E0C6BF1AB0018`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20114888](https://doi.org/10.5281/zenodo.20114888)
