# Mosaic Internet Protocol (MIP)

## Constitutional Networking as a Meta-Language for Plural Internet Universes with Canonical Governance Artifacts and Mechanically Decidable Equality

### Mosaic Internet Protocol (MIP) proposes a different discipline: make disagreement structurally legible.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

The contemporary internet treats disagreement as failure. When networks diverge in governance, routing policy, or constitutional assumptions, the divergence is hidden: protocols time out, connections reset, packets drop --- but no artifact names what happened or why. The result is governance by opacity.

Mosaic Internet Protocol (MIP) proposes a different discipline: **make disagreement structurally legible**. MIP does not attempt to eliminate divergence between networks; it provides the machinery for divergence to be explicit, signed, inspectable, and lawful. A network operating under MIP can say, with a typed and attributable artifact: *this universe is not admissible here*. That refusal is governance success, not communication failure.

MIP achieves this through **hash-addressed universe constitution artifacts**: explicit, canonicalized definitions of identity suites, frame semantics, routing admissibility, namespace governance, and amendment rules. Equality of canonicalized universe artifacts is mechanically decidable via hash comparison across independent implementations --- without negotiation, without authority, without social trust above the mathematics.

MIP operates as a meta-protocol: it does not specify a network, it specifies the language in which networks are constitutionally described. The Ableman Mosaic Internet Protocol (AMIP) is the specific constitutional network this research recommends --- the argued conclusion of applying MIP discipline to the eight-dimension configuration manifold of possible constitutional networks.

Detectability --- not prohibition --- is the primary security posture. Plurality is tolerable. Hidden drift is not.

---

## 1. Problem Statement: Fused Authority and Hidden Drift

Most network stacks conflate:

- Identity
- Location
- Routing authority

This fusion enables silent drift when:

- routing policy changes,
- cryptographic assumptions weaken,
- namespace semantics evolve,
- governance capture occurs.

MIP asserts:

> Identity must be cryptographic and topology-independent.
> Routing must be optimization, not jurisdiction.
> Governance must be explicit, canonical, and hash-addressed.

Plurality is tolerable. Undetectable drift is not.

---

## 2. Detectability as Design Axiom

The architecture is organized around a single enforcement chain:

Canonicalization $\rightarrow$ Hash equality $\rightarrow$ Mechanical comparability $\rightarrow$ Legitimate refusal $\rightarrow$ Plurality without hidden drift.

Canonicalization produces a unique semantic representation under a defined grammar.
Hashing provides collision resistance over canonical bytes.
Hash equality enables mechanical comparison.
Mechanical comparison enables refusal with evidence.
Refusal preserves plurality without semantic ambiguity.

All subsequent sections implement this chain.

---

## 3. Core Definitions

### 3.1 Mosaic ID

A Mosaic ID is a self-certifying identifier derived deterministically from a public key under the universe's identity suite. It is:

- topology-independent
- cryptographically verifiable
- portable across transports

Routing may change location metadata; it may not alter Mosaic ID authority.

Identity sovereignty is enforced at the frame level through **constitutional attribution**: a five-component claim that accompanies governed frames:

- **who**: Mosaic ID --- `BLAKE3(ed25519_pubkey_bytes)`
- **by what authority**: Ed25519 signature under the holder's private key
- **under what regime**: Phase_ID + Epoch_Public_Key (epoch governance)
- **meaning what**: Semantic hash under the declared lens (lens governance)

The private key signature is what makes the namespace unsquattable in practice --- not the mathematical derivation alone. Any party can announce a public key; only the holder of the corresponding private key can produce a valid constitutional attribution claim. The trust chain is cryptography $\rightarrow$ mathematics $\rightarrow$ physics. No social trust layer sits above the mathematics.

A further consequence: **constitutional attribution drift** --- frames whose governance-class semantic hashes diverge from the node's declared universe constitution --- is a detectable violation. A node cannot silently change its behavior without producing a divergence observable by peers. Detectability, not prohibition, is the enforcement mechanism.

### 3.2 Equality vs. Compatibility

- **Universe equality**:   
  `BLAKE3(MIP-JCS-NFC(U1)) = BLAKE3(MIP-JCS-`

`NFC(U2))` --- canonical hash of the universe constitution artifact. The hash is stable within an epoch; it changes only when the constitution itself changes.
- **Universe compatibility**: an explicitly declared relationship (e.g., bridge artifacts).

Hash inequality implies constitutional divergence. Compatibility must be separately declared.

Epoch governance (Cryptographic Phase) scopes the temporal validity of frames issued under a universe --- the epoch authority is declared within the constitution artifact, not folded into the universe hash itself. Lens governance (Semantic Hashing) scopes the semantic equality of governance-class artifacts within the universe. These are orthogonal concerns: the universe hash is constitutionally stable; the epoch and lens context under which frames are evaluated may evolve through declared amendment.

### 3.3 Three-Layer Architecture: MIP, CM, and AMIP

MIP operates across three conceptually distinct layers. Understanding this separation is essential to understanding what MIP claims and what it does not.

**MIP --- the S-layer (domain physics).** MIP is a meta-protocol discipline, not a network. It defines the invariants that any constitutional network must satisfy (\S{}4), the configuration space within which any constitutional network is specified (\S{}5), and the rules under which constitutional artifacts are compared. MIP cannot be "run." It can only be satisfied. BGP, TCP/IP, WireGuard, Tor, and AMIP are all points in the MIP configuration space --- some admissible, some not, some partial.

**The Configuration Manifold --- the CM-layer (navigating the space).** The eight dimensions of \S{}5 constitute a configuration manifold: the complete governance surface of any constitutional network. Existing protocols can be evaluated as points within this manifold --- admissible on some dimensions, inadmissible on others, silent on others still. This analysis is MIP-layer work. It applies to any constitutional network, not just the one this research recommends. The CM layer produces the argued case for which dimension selections are constitutionally sound and why.

**AMIP --- the IC-layer (the recommended protocol).** The Ableman Mosaic Internet Protocol (AMIP) is the specific constitutional network this research recommends. It sits at the same level as TCP/IP: a deployable, operational protocol with specific, argued selections at each of the eight configuration dimensions. AMIP is what you get when MIP discipline is applied to produce a concrete, admissible, fully-specified constitutional internet. The Ableman Mosaic is the AMIP universe instance (AME-0 --- Ableman Mosaic Epoch Zero).

The separation matters because the claims made at each layer are different in kind. MIP's S-layer claims are universal --- they assert what must hold in any constitutional network. The CM-layer claims are analytical --- they assert where existing protocols sit in the manifold and what the admissible choices are. AMIP's IC-layer claims are specific --- they assert that this particular set of selections constitutes a sound, deployable, constitutional internet protocol.

A reader who conflates MIP and AMIP will misread both. MIP is not AMIP. MIP is the language in which AMIP is constitutionally described.

---

## 4. Architectural Invariants

### 4.1 Substrate May Not

- reinterpret namespace semantics
- modify identity derivation
- require plaintext inspection for forwarding
- elevate routing hints into authority

### 4.2 Routing May Not

- rewrite Mosaic IDs
- redefine identity authority
- silently downgrade cryptographic suites
- infer legitimacy from popularity

### 4.3 Namespace May Not

- alter identity semantics
- override universe constitution artifact
- equate discovery with admissibility
- erase divergence without fork artifacts

### 4.4 Governance May Not

- inspect ciphertext payloads
- silently amend lens definitions
- retroactively alter commitments without explicit amendment

### 4.5 Canonicalization Boundary

MCIR serialization must not:

- admit multiple encodings for the same semantic artifact
- conceal divergence via ordering or metadata variance

Canonicalization provides semantic uniqueness under a defined grammar; cryptographic hashing provides collision resistance over canonical bytes. Both are required for equality guarantees.

---

## 5. Universe Constitution Artifact (Minimum Schema)

The universe constitution artifact `U` is an MCIR canonical AST containing eight dimensions. These dimensions constitute the complete governance surface of any constitutional network --- a **configuration manifold** in which every universe is a point. Existing protocols (BGP, WireGuard, Tor) are points within this same manifold, occupying admissible ranges on some dimensions and inadmissible regions on others. Universe equality is decided by comparing canonical hashes of points in the manifold. Manifold navigation --- which protocols satisfy which dimensions and why --- is a configuration-layer concern above the domain physics defined here.

**1. Identity Suite**

- public key curves
- Mosaic ID derivation algorithm
- signature primitives

*Note on cryptographic agility:* The identity suite is an epoch-specific selection. The epoch transition mechanism enables cryptographic migration without protocol changes. Current deployments use Ed25519 (identity signatures) and X25519 (session key exchange). A hybrid classical/post-quantum epoch (Dilithium-3 + Ed25519; Kyber-768 + X25519) is the planned successor, preserving backward compatibility during transition. BLAKE3 is retained across epochs --- its post-quantum security level (128-bit against Grover's algorithm) is sufficient for hash functions at current threat assessments.

**2. Frame Semantics**

- envelope structure
- replay rules
- required cryptographic algorithms
- per-frame attribution signing rate (required / trust-tiered / session-bound)

**3. Routing Specification**

- path object schema
- admissibility predicate definition
- deterministic scoring function
- evaluation resource bounds

**4. Transport Set**

- permitted adapters
- encapsulation rules

**5. Namespace Governance**

- DKN configuration
- manifest schema
- governance-class artifact definitions
- lens registry (LensID, version, hash)

**6. Lens Governance**

- admissible lens artifacts
- upgrade/evolution rules

**7. Amendment and Fork Rules**

- constitution update procedure
- compatibility semantics
- fork detection policy

**8. Evaluation Parameters**

- deterministic evaluator definition
- resource model R
- receipt schema

Initial admission of a universe constitution is governed by local policy; the artifact's admission rules govern subsequent amendments and derivative universes.

---

## 6. Universe Registry and Admission Policy

Relays maintain a local registry of admitted universe constitution hashes.

Admission policies may include:

- permissive acceptance
- signer allowlists
- quorum signatures
- web-of-trust receipts
- offline anchors

Admission policy may centralize or decentralize authority; such centralization is visible in the constitution artifact and therefore comparable.

No implicit root authority is assumed.

---

## 7. Frame Structure

A minimal frame contains:

- `universe_hash`
- `source_id`
- `destination_id`
- `sequence_nonce`
- `route_metadata`
- `ciphertext`
- `integrity_tag`
- `attribution_sig` *(optional --- 64 bytes; present when per-frame signing rate requires it)*

Envelope validation precedes decryption. The `attribution_sig` field carries the Ed25519 signature over the constitutional attribution claim (\S{}3.1) for this frame. Its presence is governed by the universe constitution's declared per-frame signing rate: required on every frame, present at 1/N frames for established sessions under trust-tiered mode, or absent under session-bound mode where the constitutional handshake authenticates the session and AES-GCM provides per-frame integrity.

---

## 8. Path Object Definition

```
path = {
  relay_ids: [M1, M2, ...],
  transport_edges: [(M1, M2, link_type), ...],
  receipts: [delivery_receipt_hashes],
  cost_metrics: {latency, hop_count, reliability}
}
```

Receipts must carry constitutional attribution --- signed by the issuing relay's Ed25519 key under the current epoch authority, carrying the `universe_hash` of the universe in which the receipt was issued. A receipt issued under one epoch is inadmissible under a successor epoch even if the signing key is unchanged, because the epoch authority has transitioned.

Unverifiable receipts are ignored during scoring.

`P_route(F, path)` may depend only on:

- locally verifiable path metadata
- declared and verifiable receipts
- explicitly admitted external oracles (hash-addressed dependencies)

Universes admitting external oracles trade decentralization for declared authority; such dependencies are visible in the constitution hash.

Universes SHOULD minimize external oracle dependencies to preserve routing autonomy.

---

## 9. Ableman Mosaic Internet Protocol (AMIP) --- Recommended Constitutional Instantiation

The Ableman Mosaic Internet Protocol (AMIP) is the specific constitutional network this research recommends. It is not an arbitrary example --- it is the argued conclusion of CM-layer analysis applied to the eight configuration dimensions.

The analysis proceeds as follows. For each dimension, existing protocols are evaluated as points in the MIP configuration manifold:

- **BGP** is inadmissible at Dimensions 1, 2, 3, and 5. Its routing authority is jurisdictional rather than mathematical; its identity model is topological; its equality semantics are absent. Three of MIP's domain invariants are architecturally foreclosed by BGP's design --- it cannot be augmented into admissibility; it must be replaced.
- **TCP/IP + TLS** is admissible as transport infrastructure (Dimension 4) but silent on constitution. TLS with X.509 certificates introduces a social trust layer (certificate authorities) above the cryptography --- inadmissible under MIP-S-05's requirement that the trust chain go no higher than mathematics.
- **WireGuard** is the strongest existing transport substrate --- its identity discipline (static public key as peer identity) is fully admissible under MIP-S-05. But it is constitutionally silent: no universe hash, no RefusalFrame, no receipt schema. It is the best candidate for a constitutional transport layer, not a constitutional protocol.
- **Tor** is the closest existing protocol to admissibility --- onion service addresses are self-certifying public-key-derived identities (fully admissible under MIP-S-05), and Tor's hidden service architecture realizes four of MIP's eight ARC primitives. But Tor's relay governance is inadmissible: directory authorities introduce institutional trust above the mathematics, and circuit construction relies on self-reported bandwidth rather than verifiable receipts.

From this analysis, AMIP makes the following selections:

**Identity:** Ed25519 --- deterministic signatures, no randomness requirement, 128-bit classical security. Mosaic ID derived as   
  `BLAKE3(ed25519_pubkey_bytes)`.
**Session key exchange:** X25519 ECDH --- ephemeral session keys separate from identity keys.
**Frame integrity:** AES-GCM-256.
**Hashing:** BLAKE3 --- 256-bit classical, 128-bit post-quantum (Grover bound).
**Canonical serialization:** MIP-JCS-NFC (RFC 8785 profile with mandatory NFC pre-normalization; see \S{}13).
**Transports:** Ethernet, WiFi (AP and client), Bluetooth, LoRa (via MRM protocol), WiFi mesh.
**Namespace governance:** DKN --- authority-keyed dimension IDs, two-layer trust architecture.
**Routing:** Multi-path, hop caps, receipt-grounded deterministic scoring with epoch-keyed randomized sampling.
**Sybil posture:** Assumes exposure; mitigates via receipt history depth and optional allowlists.
**Fork rule:** Constitution mismatch $\rightarrow$ isolate unless explicit bridge artifact declared.
**Stewardship:** Non-constitutional (TCP/IP-only) devices may transit the AMIP network under declared stewardship modes with typed provenance receipts.
**Genesis epoch:** AME-0 (Ableman Mosaic Epoch Zero).

Each selection traces to a CM-layer finding: this choice is admissible, that choice forecloses invariants, this existing protocol is partial. The Ableman Mosaic Internet Protocol is not a thought experiment --- it is the operational conclusion of applying MIP discipline seriously.

The MIP Constitutional Codex v0.1 includes a benchmark harness (BM-1 through BM-6) specifying the measurements that will empirically validate or falsify these selections: constitutional handshake overhead, receipt chain throughput, P_route evaluation time, per-frame signing cost, LoRa duty cycle interaction, and Byzantine detection latency against BGP withdrawal convergence as baseline. Results will be published when the reference implementation reaches operational status. Failure on any benchmark falsifies the corresponding AMIP selection as an argued conclusion and requires codex amendment.

*AMIP is operationalized in the MIP Constitutional Codex v0.1.*

---

## 10. End-to-End Execution Trace

Universe: Ableman Mosaic Internet Protocol (AMIP), epoch AME-0
Constitution hash: `h(U) = BLAKE3(MIP-JCS-NFC(U))`

1. Node A constructs payload `p`.
2. A builds frame `F` with `h(U)`, `M_A`, `M_B`.
3. A signs and encrypts; attaches constitutional attribution claim if signing rate requires.
4. Relay R validates signature and replay window.
5. R checks `h(U)` against local registry.
6. R evaluates `P_route(F, path)`.
7. R forwards via declared transport.
8. B receives and validates.
9. B decrypts.
10. Payload references governance artifact `G`.
11. B resolves `G` via DKN.
12. B verifies artifact and lens hash.
13. Canonical lens evaluation mismatch detected.
14. B emits constitutional refusal frame (\S{}11).

---

## 11. Refusal Primitive

Refusal is a protocol-defined outcome under a universe constitution.

### 11.1 Refusal Frame Schema

```
{
  universe_hash,
  // BLAKE3(MIP-JCS-NFC(refusing node's admitted constitution))
  refusing_node_id,        // BLAKE3(ed25519_pubkey_bytes) --- Mosaic ID
  refused_frame_digest,    // BLAKE3(refused frame bytes)
  reason_code,             // universe-specific typed vocabulary
  optional_evidence_hash,  // hash of supporting artifact, if applicable
  signature // Ed25519 over BLAKE3(MIP-JCS-NFC(above fields))
}
```

The signature follows the same constitutional attribution discipline as regular frames --- it is not a bare Ed25519 signature over raw bytes but a signature over the canonical hash of the refusal claim, binding the refusal to the refusing node's identity and the current epoch.

Defaults:

- Refusal is locally returned.
- Forwarding beyond one hop is disabled by default.
- Rate limiting uses per-source token buckets keyed by `(source_id)` and

`(refused_frame_digest)`. Rate parameters are declared in the universe constitution's Evaluation Parameters dimension and therefore visible in the universe hash --- rate policy is a constitutional choice, not an implementation detail.

Refusal is scoped to the evaluating universe and does not imply global identity revocation.

### 11.2 Constitutional Attribution Drift

A distinct class of constitutional violation is **attribution drift**: a node whose frame-level semantic hashes diverge from its declared universe constitution without announcing an amendment. This is the silent behavioral change attack --- the node's bytes are well-formed and its signatures are valid, but the governance-class content of its frames no longer corresponds to what it claims to implement.

Attribution drift is detectable --- it does not require the drifting node to announce itself. Observers compare the semantic hashes embedded in governance-class frames against the hashes derivable from the node's announced universe constitution. Divergence is evidence. The response is a typed observation, not a refusal --- refusal applies to frame-level violations; attribution drift is surfaced through the constitutional observability layer.

This closes the gap identified in \S{}15 ("Governance hides in defaults"): under MIP, governance that departs from its declaration becomes visible through semantic hash comparison, not through trust in the node's announcements.

---

## 12. Semantic Hashing Scope

Semantic hashing applies only to governance-class artifacts, including:

- universe constitution artifacts
- lens definitions
- amendment artifacts
- bridge declarations
- routing predicate updates

General content addressing remains byte-hash by default.

---

## 13. Canonicalization as Cryptographic Boundary

### 13.1 Canonicalization Threats

Failure modes include:

- AST encoding ambiguity across languages
- numeric normalization inconsistencies
- Unicode normalization variance
- map key ordering drift
- serializer version skew
- implicit coercion or optimization

### 13.2 Canonicalization Principles

- formally specified grammar
- strict type system
- no duplicate keys
- deterministic ordering by UTF-8 byte lexicographic order (MIP-JCS-NFC pre-normalizes strings to NFC before key ordering and value serialization)
- fixed numeric encoding rules
- exclusion of non-semantic metadata
- mandatory MIP-JCS-NFC conformance suite enforcement

Canonicalization provides semantic uniqueness; hashing provides collision resistance. Both are required.

**MIP-JCS-NFC deviation from RFC 8785:** MIP uses a canonicalization profile called MIP-JCS-NFC. It follows RFC 8785 in all respects except one: string values are Unicode NFC-normalized before serialization. RFC 8785 \S{}3.2.3 explicitly prohibits altering parsed string data. MIP-JCS-NFC departs from this to prevent cross-implementation hash divergence on inputs that differ only in Unicode normalization form (e.g., `caf\'{e}` as precomposed U+00E9 versus decomposed

`e` + U+0301). Without NFC pre-normalization, two implementations receiving the same semantic string from different sources could produce different universe hashes --- breaking MIP-S-03. The deviation is intentional, declared, and named explicitly rather than silently applied under the RFC 8785 name.

**Operational definition:** Mechanical equality (\S{}2, \S{}14) is operationally defined by a normative conformance suite specifying 25 MIP-JCS-NFC+BLAKE3 test vectors. Vector CV-06 and CV-07 test the critical MIP-JCS-NFC deviation from RFC 8785: NFC normalization is applied to strings before serialization: NFD-encoded and NFC-encoded representations of the same string must produce identical canonical bytes and identical BLAKE3 hashes. Vector CV-21 tests the full constitutional attribution claim structure. Any implementation passing all 25 vectors --- plus the NFC equivalence invariant --- satisfies the canonicalization requirement of this section. The conformance suite is defined in the MIP Constitutional Codex.

---

## 14. Cross-Implementation Equality: Conformance Suite

Equality of canonicalized universe artifacts is mechanically decidable via hash comparison. This property is delivered, not aspirational.

The normative conformance suite specifies:

1. 25 MIP-JCS-NFC+BLAKE3 input/output pairs with canonical bytes in hexadecimal and BLAKE3 hashes computed by a reference implementation.
2. A Unicode NFC equivalence invariant: NFD and NFC representations of the same string must produce identical hashes (CV-06 = CV-07).
3. A constitutional attribution claim vector (CV-21): the full five-component attribution structure must hash identically across independent implementations.
4. A runnable conformance test script that exits non-zero on any failure.
5. A common failure modes table mapping symptoms to canonicalization bugs.

Fuzz testing for AST equivalence and a golden hasher for fixtures remain recommended extensions beyond the normative suite.

Identical canonical artifacts must produce identical hashes across independent implementations. The conformance suite is the falsifiable test of this claim.

**Normative location:** MIP Constitutional Codex v0.1,   
  `MIP-S/CX-S/CONFORMANCE_SUITE.md`. **Critical vector:** CV-21 tests the full constitutional attribution claim structure --- passing CV-21 guarantees that AMIP frame attribution is equivalent across independent implementations in any language. Any implementation passing all 25 vectors satisfies the mechanical equality requirement of this section.

---

## 15. Failure Without Constitution

Without constitutional definition:

* Identity collapses into topology
* Routing collapses into authority
* Forks collapse into fragmentation
* Namespaces drift silently
* Governance hides in defaults

Without meta-language:

* Each network claims universality
* Interoperability requires informal compromise
* Authority centralizes through inertia

The result is a monoculture masquerading as inevitability.

---

## 16. Conclusion

The Mosaic Internet Protocol reframes networking as a governed configuration space. It does not propose a better internet. It proposes an internet where disagreement becomes structurally legible.

"Constitutional" in this context means one precise thing: mechanically declared governance constraints, expressed as hash-addressed artifacts, subject to canonical equality verification. Not sovereignty. Not legitimacy in the political sense. Not ontology. A universe constitution is a hash-addressed document. What it grants is detectability --- the ability to know, with a signed artifact, what rules are in force and when they have changed.

It asserts:

* Identity is sovereign and cryptographic.
* Routing is configurable and optimizable.
* Transport is interchangeable.
* Trust is parameterized.
* Namespaces are semantically hash-bound.
* Universes are constitutionally declared.
* Forks are lawful.
* Refusal preserves boundaries.

Most systems try to erase disagreement through forced continuity: same DNS root, same certificate authorities, same routing assumptions, same namespace semantics. MIP takes the opposite position: divergence is inevitable; hidden divergence is the real danger. The protocol does not eliminate disagreement. It makes disagreement inspectable, attributable, and lawful.

Where legacy protocols fused identity with infrastructure, MIP separates them. Where divergence previously required rupture, MIP permits coexistence. Where governance hid in defaults, MIP makes it visible.

And when universes disagree, the network need not collapse. It can simply say --- with a typed, signed, attributable artifact:

This universe is not admissible here.

Refusal is stability. Configuration is sovereignty. Governance is visible.

That is the Mosaic thesis. AMIP is its first executable instantiation.

---

---

## Appendix A: Minimal Sufficiency

*What is the smallest executable set that proves the core MIP claim?*

This appendix answers a necessary question: as the codex set grows --- conformance suite, benchmark harness, post-quantum roadmap, router realization, namespace governance, semantic hashing layers --- which elements are load-bearing, and which are elaborations?

The answer matters for two reasons. First, it tells implementors where to start. Second, it protects the core claim from being buried under contestable engineering choices. The meta-protocol's epistemic integrity depends on knowing what it would take to falsify it.

### The Minimal Constitutional Stack

The following five elements, and only these five, are necessary and sufficient to demonstrate MIP-S compliance:

**1. MIP-JCS-NFC canonicalization** --- a deterministic serialization that produces identical bytes from identical governance-class artifacts across independent implementations. This is the mechanical foundation. Without it, hash equality is not decidable and nothing else follows.

**2. BLAKE3 universe hash** ---   
  `BLAKE3(MIP-JCS-NFC(U))` computed from the universe constitution dict. Two implementations that produce identical hashes from identical constitution dicts satisfy MIP-S-03 (Mechanical Equality). This is the core equality primitive.

**3. Constitutional handshake** --- two peers exchange universe hashes, verify mutual admission, derive a session key, and produce a `handshake_completed` receipt. This demonstrates MIP-S-05 (Identity Sovereignty) and MIP-S-06 (Routing as Optimization) at minimum.

**4. RefusalFrame** --- when universe hashes do not match, the refusing node produces a signed, typed RefusalFrame rather than a silent drop, timeout, or reset. This is the load-bearing primitive. Typed refusal is the concrete manifestation of MIP-S-01 (Detectability Axiom) and MIP-S-04 (Refusal as Protocol Primitive).

**5. Receipt chain** --- at minimum two operations: `handshake_completed` and

`handshake_refused`. These establish that governance events are receipted, auditable, and chain-linked --- MIP-S-07 (Governance Visibility) at its floor.

### What This Does Not Include

The following are AMIP-specific selections or future-arc additions --- they are not required to demonstrate MIP-S compliance:

- P_route multi-path scoring (AMIP AME-0 Dimension 3; routing can be as simple as "admitted registry check")
- DKN namespace governance (AMIP selection; any namespace satisfying MIP-S-07 is admissible)
- Semantic lens evaluation (AMIP selection; hash equality alone satisfies MIP-S-03 at the floor)
- Epoch governance transitions (declared non-guarantee in AME-0; required in AME-1)
- ESA / COP observability surface (future-arc; receipt infrastructure is sufficient)
- The Ableman Mosaic Router (IR-3 realization; transport invariance is demonstrated by IR-1 and IR-2)
- ConstitutionalFastPath optimization (performance; not correctness)
- Stewardship modes (AMIP AME-0 deployment feature; not a MIP-S requirement)

### The Falsifiable Test

Two nodes. One universe constitution dict. Three scenarios:

1. Both nodes compute the same universe hash from the same dict $\rightarrow$ they establish a constitutional session $\rightarrow$ `handshake_completed` receipt produced by both.

2. One node presents a different universe hash $\rightarrow$ the other produces a typed, signed RefusalFrame with   
`reason_code: UNIVERSE_HASH_MISMATCH` $\rightarrow$

`handshake_refused` receipt produced.

3. The conformance suite runs against both implementations $\rightarrow$ all 25 MIP-JCS-NFC+BLAKE3 vectors pass $\rightarrow$ NFC equivalence invariant (CV-06 = CV-07) holds.

If all three scenarios produce the correct outcomes, the core MIP claim is demonstrated. Everything else in the codex set is elaboration, optimization, or AMIP-specific selection.

**AMIP-WG** (the WireGuard instantiation, specified in a companion IC codex) is the reference implementation of this minimal stack on existing internet infrastructure. It implements exactly the five elements above --- constitutional handshake as first WireGuard transport payload, RefusalFrame on universe hash mismatch, four receipt operations --- and nothing more. AMIP-WG is the minimal sufficiency demonstration.

### The Doctrine

Any addition to the minimal stack should pass this test: does it close a gap in the core claim, or does it elaborate an AMIP-specific choice? If the latter, it belongs in the IC or IR codices, not in MIP-S. The meta-protocol stays austere. The recommended protocol can be as rich as the engineering warrants.

---

## Editorial Provenance and Standing

*With the Ableman Mosaic Internet Protocol (AMIP) as Recommended Constitutional Instantiation*
**Version:** 1.0

## Corpus-Wide Reference Positioning

This paper argues that the contemporary internet treats disagreement as failure. Its nearest external comparison fields are distributed, security, crypto. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Convergence and consensus establish agreement under a fault model; they do not establish that the agreed state is true, authorized, desirable, or semantically equivalent. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Leslie Lamport. "Time, Clocks, and the Ordering of Events in a Distributed System." *Communications of the ACM* 21(7), 1978, pp. 558-565. DOI: 10.1145/359545.359563. https://lamport.azurewebsites.net/pubs/time-clocks.pdf **Relationship:** Foundational predecessor for partial order, causality, and distributed event ordering.

**[E2]** Leslie Lamport, Robert Shostak, and Marshall Pease. "The Byzantine Generals Problem." *ACM Transactions on Programming Languages and Systems* 4(3), 1982, pp. 382-401. DOI: 10.1145/357172.357176. https://doi.org/10.1145/357172.357176 **Relationship:** Predecessor fault model for agreement under adversarial or inconsistent participants.

**[E3]** Marc Shapiro et al. *A Comprehensive Study of Convergent and Commutative Replicated Data Types*. INRIA Research Report RR-7506, 2011. https://inria.hal.science/inria-00555588 **Relationship:** Predecessor convergence model for replicated state; convergence is compared with, but not equated to, legitimacy or semantic agreement.

**[E4]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E5]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E6]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E7]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

### Ableman corpus

**[A1]** Adam Ableman. *The Optional Coordinator*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-727469A6944DA256`;  
source SHA-256  
`92E8F6743B8DDAFF369D2F40120A384DDE273613B12B27D2FC14610469F5A46E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Synchronization*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-012675C952D76CD2`;  
source SHA-256  
`A2147B7E6431FF6EEC1C6CE6D7A1EB644B04E37402E9514495C83909565F93C1`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Constitutional Collective with Optional Overmind (CCOO)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-ED07EA7D91B87C5E`;  
source SHA-256  
`0346FA1B79A2A44A6034DEDCE4D0FA0E5C5CCD953F4AD29A88CEE1F290DCC210`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Communal Computing and Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-A6393299A70371DC`;  
source SHA-256  
`302FC6C269369AC4A4A5D8470E56596B6E8813A82530AD9DA64E9FAEEC4D2461`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

DOI: [10.5281/zenodo.20115615](https://doi.org/10.5281/zenodo.20115615)
