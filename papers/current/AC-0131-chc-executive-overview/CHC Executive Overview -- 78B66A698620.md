# CHC Executive Overview

## State Identity, Semantic Identity, and Policy-Relative Admissibility

### The third is a decision evaluated from state, claims, evidence, authority, context, freshness, and policy.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Cryptographic Homological Compilation (CHC) proposes that three questions be represented separately:

```text
What exact state is this?
What claims are bound to that state?
May this state act here, now, under this policy and evidence?
```

The first two questions can be addressed by distinct, canonicalized cryptographic commitments. The third is a decision evaluated from state, claims, evidence, authority, context, freshness, and policy. A signature authenticates a statement relative to a key; it does not by itself establish that the signer has current authority, that the statement is true, or that the subject is admissible.

CHC is therefore an architecture for keeping artifact identity, semantic-claim identity, and admissibility from collapsing into one apparent fact. This overview specifies that separation and its claim ceiling. It does not supply a cryptographic protocol, implementation, or security proof.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. The custody manifest is   
`work/paper-saturation-v1/evidence/chc-`

`executive-overview/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`204E0C0991F10A908FC37A885AC10AC0E126CA0419F7E6B9C8A008E9EC8C9A43`. The source remains unchanged.

The CHC name, three-domain separation, jurisdictions, two hashes, policy-relative admissibility, receipts, freshness, revocation example, recursive toolchain application, and comparison targets are author material. Canonicalization requirements, decision envelope, authority correction, threat model, corpus integration, funnel, countertests, and editorial alternatives are AI-assisted contributions explicitly distinguished from the original author material.

No external research or cryptographic validation was performed.

## 1. The Separation

### 1.1 State Identity

Let $J$ be a declared **State Jurisdiction**: the exact boundary whose state is being identified. It may be a file, tree, binary, image, deployment snapshot, runtime capture, or knowledge artifact. Let $Canon_s$ be its versioned canonicalization:

$$
H_s=Hash(algorithm_s,Canon_s(J)).
$$

The tuple must bind the algorithm, canonicalization profile, jurisdiction rule, exclusions, and bytes or reconstructable state. `H_s` alone does not reveal the boundary and does not prove origin, safety, semantics, or behavior.

### 1.2 Semantic Identity

Let $M$ be a structured claim envelope referring to $H_s$ and containing claims, schemas, issuers, provenance, scope, and expiry. Then:

$$
H_m=Hash(algorithm_m,Canon_m(M)).
$$

`H_m` commits to canonicalized claim material. It does not prove that the claims are true, complete, authorized, or semantically equivalent to another envelope. Any claim of semantic stability requires a declared equivalence regime and adversarial examples.

### 1.3 Admissibility

At time $t$, an evaluator considers policy $P_t$, evidence $E_t$, authority state $A_t$, context $C_t$, and the two identities:

$$
D_t=Eval(P_t,E_t,A_t,C_t,H_s,H_m).
$$

The result should be typed, for example:

$$
D_t\in\{ADMIT,REFUSE,DEFER,UNKNOWN,CONFLICT,EXPIRED\}.
$$

Admissibility is not a third intrinsic identity unless a particular system hashes the complete decision envelope. It is a policy-relative judgment whose subject, inputs, evaluator, time, scope, result, and claim ceiling should be receipted.

## 2. Authentication, Authority, and Admissibility

The source's useful normalization is:

```text
signed = evidence
```

More precisely, a valid signature supports a bounded claim that a holder of a corresponding key signed particular bytes under a specified algorithm. Additional evidence is required to establish key custody, signer identity, delegated capability, current authority, jurisdiction, purpose, freshness, and non-revocation.

Authority does not emerge from admissibility. Authority is an input and governed relation that the admissibility process evaluates. Nor does admissibility create truth. It decides whether a subject may proceed under one policy and context.

## 3. Mutable Admissibility Over Stable State

A software release may retain the same $H_s$ and $H_m$ while its signing key is revoked, a vulnerability is discovered, a jurisdiction changes, an approval expires, or new evidence conflicts with an earlier receipt. The current decision can change without rewriting history:

$$
(H_s,H_m,D_{t_1}=ADMIT)\rightarrow(H_s,H_m,D_{t_2}=REFUSE).
$$

Conversely, a policy change can admit an unchanged artifact. The receipt must therefore bind policy and evidence versions rather than treating admissibility as a permanent attribute of the artifact.

## 4. Receipts and Freshness

A CHC receipt should include:

- exact subject jurisdiction and $H_s$;
- semantic envelope identity $H_m$;
- policy, authority, trust-root, and evaluator versions;
- evidence set and exclusions;
- relevant time, epoch, or checkpoint;
- decision, reason codes, and scope;
- uncertainty, conflict, and missing inputs;
- expiry and reevaluation triggers;
- signer and signature where required;
- previous and superseding receipt links.

Freshness is claim-relative. A recent timestamp does not prove fresh vulnerability information, non-revocation, current policy, or current deployment state. The evaluator must state what freshness means for each input.

## 5. Recursive Toolchain Jurisdictions

Applications, compilers, assemblers, linkers, build environments, signing services, and deployment controllers can each be treated as jurisdictions. This supports the question: **what produced the producer?**

Recursion does not eliminate trust. It exposes a finite trust base, bootstrap boundary, or unresolved premise. A complete CHC claim should identify where recursion stops and what evidence supports that stopping point.

## 6. The Three Hash Rule Interface

The Two-Hash architecture in the source identifies exact state and a semantic-claim envelope; admissibility is evaluated separately. The Three Hash Rule warns against using one digest as a proxy for object state, governing or admissibility commitments, and meaning commitments.

These views can be compatible if the system explicitly binds:

- an exact-state commitment;
- a semantic-meaning or claim commitment;
- a governing policy/admissibility commitment or decision-envelope commitment.

That does not require exactly three physical hash fields in every serialization. It requires the commitments to remain independently addressable and non-interchangeable.

## 7. Threat Model and Failure Modes

CHC must address ambiguous jurisdiction boundaries, canonicalization collisions, algorithm substitution, claim-envelope omission, equivocation, stale or revoked authority, rollback, freeze, replay, split views, missing transparency, compromised keys, confused deputies, policy downgrade, evidence laundering, evaluator compromise, time-source failure, dependency substitution, non-deterministic builds, hidden runtime state, and semantic overclaim from digest equality.

Hashes can detect some changes to committed material. They cannot show that omitted material was irrelevant, that canonicalization preserved meaning, that a policy is legitimate, or that an observed execution corresponds to the committed artifact.

## 8. Primitives, Invariants, Dimensions, and Adjacencies

**Primitives:** jurisdiction, canonicalization profile, hash algorithm, state commitment, claim envelope, semantic commitment, policy, authority relation, evidence, receipt, epoch, decision, refusal, conflict, expiry, revocation, and appeal.

**Invariants:** jurisdiction is explicit; algorithms and canonicalizers are versioned; state and semantic commitments are not substituted for one another; signatures do not self-authorize; decisions bind exact inputs and scope; revocation cannot rewrite history; unknown is first-class; and a receipt cannot exceed its evidence.

**Dimensions:** jurisdiction granularity, canonicalization strictness, hash agility, semantic schema, authority model, freshness horizon, evidence independence, privacy, transparency, latency, availability, revocation propagation, and recursive depth.

**Adjacencies:** The Three Hash Rule supplies commitment separation; Reasoning by Way of Receipts supplies bounded decision evidence; Receipt-Bound Capabilities can connect admissibility to effect authority. These interfaces do not prove that a CHC implementation exists.

## 9. GMB and Universal GSM Projection

The Governed Meaning Base can retain jurisdictions, exact versions, commitments, claims, issuers, policies, authority grants, revocations, evidence, receipts, decisions, conflicts, and revisions. The universal GSM can type `IDENTIFIES_STATE`,  
`CLAIMS_ABOUT`, `SIGNED_BY`, `AUTHORIZED_BY`, `EVALUATED_UNDER`, `ADMITTED_BY`,  
`REFUSED_BY`, `REVOKED_BY`, and `SUPERSEDES`.

Storage in GMB does not make a claim true or an artifact admissible. The current evaluator must resolve an exact projection under a declared policy.

## 10. Realization Funnel

$$
\begin{aligned}
&Possibility \\
&\rightarrow Specification \\
&\rightarrow CM_1 \\
&\rightarrow CM_2 \\
&\rightarrow IC \\
&\rightarrow IR \\
&\rightarrow Evidence \\
&\rightarrow Revision
\end{aligned}.
$$

- **Possibility:** enumerate jurisdictions, commitment schemes, trust models, policy regimes, threats, and failure outcomes.
- **Specification:** define canonicalization, identities, authority, evidence, decision, refusal, freshness, revocation, and receipt semantics.
- **CM1:** retain all admissible cryptographic and operational configurations.
- **CM2:** select preferable configurations under security, agility, privacy, availability, auditability, and cost criteria.
- **IC:** bind an Instance Constitution or Instance Configuration selecting algorithms, schemas, roots, evaluators, clocks, policies, and recovery rules.
- **IR:** build an Instance Realization or Implementation Realization.
- **Evidence:** execute vectors, conformance tests, attacks, interoperability tests, revocation exercises, and recovery trials.
- **Revision:** change algorithms, policies, schemas, or trust roots without conflating the new system with the old.

Any compiler `IR` or named representation retains the separate meaning **Intermediate Representation**. Realization-stage

`IR` has the interchangeable expansions above.

## Cryptographic Commitment-Separation Profile

Across the completed P1 corpus, CHC is the **cryptographic commitment-separation profile that keeps exact state, claims about that state, and current policy-relative admissibility independently addressable**. It is not a separate theory of truth, a source of authority, a security proof, or an implementation of the wider corpus merely because it uses hashes and receipts.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Durable decision, evidence, refusal, expiry, and revision records.  
  **CHC boundary:** A CHC receipt records an evaluation; it does not make a commitment accurate or authorized.

- **Adjacent work:** *Identity Spine Doctrine*  
  **Supplies:** Stable identity and lineage across artifacts, projections, and revisions.  
  **CHC boundary:** CHC supplies cryptographic state and claim commitments inside a larger identity spine.

- **Adjacent work:** *Global Term Key: Identity Primitives in Governed Knowledge Systems*  
  **Supplies:** Resolved lexical and semantic identity records.  
  **CHC boundary:** A GTK identity can be referenced by a claim envelope; digest equality does not perform disambiguation.

- **Adjacent work:** *Meta-Binding as Operational Invariant*  
  **Supplies:** Preservation of binding force across transformations.  
  **CHC boundary:** CHC commits to declared claims; it does not prove that transformations preserved their force.

- **Adjacent work:** *Semantic Legitimacy Before Context*  
  **Supplies:** Admission discipline before content becomes binding context.  
  **CHC boundary:** CHC provides exact commitment inputs to an admission decision, not the legitimacy of that decision.

A CHC evaluation should bind:

$$
\begin{aligned}
C= (&state\_jurisdiction, state\_canonicalizer, \\
&state\_commitment, claim\_schema, claim\_canonicalizer, \\
&claim\_commitment, authority, policy, evidence, context, \\
&epoch, evaluator, decision, receipt)
\end{aligned}.
$$

Each commitment is meaningful only with its jurisdiction, canonicalization profile, algorithm, exclusions, and reconstruction rules. The admissibility decision is mutable over stable commitments because authority, policy, evidence, vulnerability state, context, or freshness may change. A digest of the decision envelope can identify that decision but does not turn admissibility into an intrinsic property of the artifact.

Recursive toolchain application terminates at an explicit bootstrap or trust boundary. Every recursive claim must expose the finite base, unresolved premises, unavailable evidence, and recovery plan. Algorithm agility, canonicalizer revision, authority revocation, and policy succession create linked successors rather than silently reusing prior identity.

The universal GSM can type   
`COMMITS_TO_EXACT_STATE`, `COMMITS_TO_CLAIM_ENVELOPE`,  
`CANONICALIZED_UNDER_PROFILE`, `EVALUATED_FOR_ADMISSIBILITY`, `ADMITTED_AT_EPOCH`,  
`REFUSED_AFTER_REVOCATION`, `EXPIRES_WITH_EVIDENCE`, `TERMINATES_AT_TRUST_BOUNDARY`,  
`SUCCEEDED_BY_ALGORITHM_PROFILE`,  
and   
`DOES_NOT_PROVE_SEMANTIC_EQUIVALENCE`. These relations integrate CHC without conflating identity, meaning, authority, or standing.

This integration establishes four editorial commitments: classify CHC as a cryptographic commitment-separation profile; adopt the complete evaluation envelope; require explicit recursive trust termination and successor handling; and prohibit state hashes, claim hashes, signatures, or decision hashes from self-establishing truth, authority, equivalence, or permanent admissibility.

## Migration Commitments, Live Infrastructure Limits, Semantic Resolution, and Boundary Evidence

The fixed-seed comparison with model-first legacy migration, constitutionally governed infrastructure, Constitutional Binding Theory, and The Path Was Open clarifies what cryptographic commitments can and cannot carry:

$$
\begin{aligned}
C^*= (&jurisdiction, canonicalizer, algorithm, \\
&state\_commitment, claim\_commitment, binding\_profile, \\
&authority, policy, epoch, evidence, boundary\_coverage, \\
&evaluator, decision, receipt, successor)
\end{aligned}.
$$

Migration can use separate commitments for legacy state, extracted descriptive models, normative decisions, selected IC, candidate IR, correspondence evidence, and promotion. Digest continuity does not establish behavioral or semantic equivalence, and an admitted successor does not inherit the predecessor's authority or standing without an explicit rule.

Constitutionally governed infrastructure supplies the live-performance counterexample: exact configuration and decision receipts can coexist with starvation, inaccessible remedies, hidden fallbacks, priority inversion, or bypass. CHC identifies what was evaluated; it does not prove that the committed surface was complete or practically usable.

Constitutional Binding Theory supplies the resolution profile needed to interpret an anchor, claim, policy, key, or state identity. Canonicalization and deterministic resolution remain governed choices with exclusions and remainder. The Path Was Open adds boundary evidence: a committed declaration and passing receipt do not exclude unmodeled concrete effect routes.

The universal GSM can type   
`COMMITS_TO_MIGRATION_STAGE`,  
`SUCCEEDED_BY_DISTINCT_ADMISSIBILITY`, `RESOLVES_COMMITMENT_ANCHOR_UNDER_PROFILE`,  
`OMITS_LIVE_INFRASTRUCTURE_PROPERTY`, `WITNESSED_BY_BOUNDARY_GAP`, `EXPIRES_AT_EPOCH`,  
and   
`DOES_NOT_PROVE_COVERAGE_OR_EQUIVALENCE`.

This randomized review establishes four editorial commitments: adopt stage-specific migration commitments; record live infrastructure properties outside hash proof; bind commitment interpretation to an explicit anchor-resolution profile; and require boundary-coverage evidence and gap witnesses beside every admissibility receipt.

## Commitment Separation Under Migration, Infrastructure, Binding, and Boundary Uses

Four strong downstream uses in the frozen P3 field test CHC beyond its compact overview. Model-first migration uses separate commitments for predecessor state, descriptive models, normative decisions, selected configuration, realization evidence, and promotion. Constitutionally governed infrastructure shows that exact commitments can coexist with starvation, inaccessible remedy, hidden fallback, or bypass.

Constitutional Binding Theory requires each commitment to be interpreted under a versioned canonicalization and anchor-resolution profile. *The Path Was Open* shows that a committed boundary declaration and valid receipt do not prove that all concrete effect routes were modeled or mediated.

The compact object should therefore retain:

$$
\begin{aligned}
C^*= (&jurisdiction, canonicalizer, algorithm, \\
&state\_commitment, claim\_commitment, binding\_profile, \\
&authority, policy, epoch, evidence, coverage, evaluator, \\
&decision, receipt, successor)
\end{aligned}.
$$

The reverse dependencies confirm CHC's useful role as commitment separation, while narrowing four likely overclaims: cryptographic identity is not semantic identity; a signed claim is not authority; policy-relative admission is not truth; and an exact decision receipt is not coverage or live-performance proof. Algorithm, canonicalizer, policy, authority, and evidence changes create linked successors rather than silent reinterpretation.

The universal GSM can type   
`COMMITS_TO_MIGRATION_STAGE`,  
`INTERPRETED_UNDER_BINDING_PROFILE`, `OMITS_LIVE_PERFORMANCE_PROPERTY`,  
`WITNESSED_BY_BOUNDARY_GAP`, `SUCCEEDED_BY_POLICY_EPOCH`, and   
`DOES_NOT_PROVE_COVERAGE`.

This reverse-dependency review establishes four editorial commitments: preserve the commitment-separation role; add binding profile and coverage fields to the compact model; require stage-specific commitments and successor epochs; and state the live-performance and boundary-coverage proof limits in the executive summary.

## 11. Counterevidence and Failure Tests

CHC must narrow, revise, or fail if: (1) a jurisdiction is ambiguous; (2) excluded files affect behavior; (3) symlinks escape the boundary; (4) canonicalization is non-deterministic; (5) algorithm identifiers are omitted; (6) algorithm substitution passes; (7) two states collide under the operational profile; (8) semantic fields are omitted; (9) reordering changes meaning unexpectedly; (10) different meanings canonicalize identically; (11) identical meaning claims cannot survive benign serialization; (12) $H_s$ is used as semantic proof; (13) $H_m$ is used as truth proof; (14) a signature grants authority automatically; (15) key identity is confused with human identity; (16) revoked authority still admits; (17) stale policy still admits; (18) rollback restores revoked trust; (19) freeze suppresses updated metadata; (20) a receipt is replayed against another subject; (21) the evaluator omits its version; (22) evidence omissions are invisible; (23) `UNKNOWN` becomes

`ADMIT`; (24) conflict becomes absence; (25) refusal lacks a reason and recovery path; (26) clock failure creates false freshness; (27) transparency clients receive split views; (28) compromise cannot be recovered; (29) hash agility changes identity without lineage; (30) recursive verification hides its trust base; (31) build identity is confused with runtime identity; (32) a container digest is treated as deployment-state proof; (33) policy legitimacy is inferred from hashing; (34) admission is described as truth; (35) authority is said to emerge from a decision; (36) privacy-sensitive claims leak; (37) evidence is self-issued; (38) comparison systems are mischaracterized; (39) homological terminology is asserted without definition; (40) a two-hash profile contradicts the Three Hash Rule without explanation; (41) no reference implementation or vectors exist; or (42) publication proceeds without cryptographic review.

## Two Commitments and a Decision Must Remain Three Different Claims

### Public orientation

CHC separates exact state identity, semantic-claim identity, and policy-relative admissibility. A state commitment says which canonical bytes or reconstructable state are in scope. A semantic commitment says which claim set is bound under its own regime. Admissibility is a fresh decision over state, claims, evidence, authority, context, and policy. None can safely stand in for the others.

### Adversarial tests

1. **Boundary-ambiguity attack.** The state hash omits files, metadata, dependencies, environment, runtime, mutable services, or physical state that matter to the claim.
2. **Canonicalization-collision attack.** Different meaningful states normalize to one canonical form, or equivalent states fail to normalize consistently across implementations.
3. **Semantic-hash-truth attack.** A committed claim set is treated as true, complete, correctly interpreted, or legitimately authored.
4. **Signature-authority attack.** A valid signature proves key control but is treated as current jurisdiction, delegation, competence, or lawful authority.
5. **Freshness-replay attack.** A previously admissible subject reuses old evidence, policy, authority, time, or revocation state.
6. **Recursive-toolchain attack.** Each compiler and verifier is hashed while the composition, bootstrap, hardware, environment, and effect boundary remain unclosed.
7. **Policy-equivalence attack.** Two policies return the same outcome and are treated as semantically or institutionally equivalent.
8. **Cryptographic-aura attack.** The CHC name, hashes, signatures, and receipts create a security-proof impression unsupported by a protocol and threat analysis.

### Claim and evidence ceiling

The overview specifies a commitment-separation architecture and threat model. It does not supply a cryptographic protocol, implementation, proof, collision or preimage analysis, canonicalization correctness, key governance, complete jurisdiction, source authenticity, semantic truth, legitimate authority, or sound admissibility policy. Cryptographic Homological Compilation remains a name; no homological mathematical result is established here.

Validation requires exact jurisdictions and exclusions, canonicalization specifications and cross-implementations, adversarial collisions, semantic-schema governance, key and delegation lifecycle, revocation and freshness tests, recursive toolchain closure, policy comparison, and current cryptographic and formal research. None occurred in this pass.

### Reader-facing consequence

CHC should help a reviewer ask three separate questions without cryptographic theater: what exact state is this, what exact claims are bound to it, and may it act here and now under independently justified authority, evidence, and policy?

## CHC in One Sentence

CHC keeps exact state, claims about that state, and the current permission to act separately addressable so that a change in one cannot silently masquerade as a change in the others.

## Reference and Verification Note

The exact internal comparison set inspected for this candidate includes *The Three Hash Rule*, *Reasoning by Way of Receipts*, and *Receipt-Bound Capabilities*. No external systems were inspected. Further evidentiary strengthening requires primary-source comparison with the external systems named in the source and independent review of the cryptographic and authorization claims.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Publication form.** This work is retained as a standalone technical companion because its concrete migration method is useful independently; it remains subordinate to the architecture it explains.

## Corpus-Wide Reference Positioning

This paper argues that cryptographic Homological Compilation (CHC) proposes that three questions be represented separately: text What exact state is this?. Its nearest external comparison fields are crypto, provenance, observation. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Telemetry can be complete at the instrumented boundary while omitting the causal variable, real-world effect, or authority question that matters. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Anders Rundgren, Bret Jordan, and Samuel Erdtman. *JSON Canonicalization Scheme (JCS)*. RFC 8785, 2020. https://www.rfc-editor.org/rfc/rfc8785 **Relationship:** Adjacent canonicalization standard relevant to stable cryptographic commitments.

**[E2]** Ben Laurie et al. *Certificate Transparency Version 2.0*. RFC 9162, 2021. https://www.rfc-editor.org/rfc/rfc9162 **Relationship:** Adjacent append-only Merkle-log standard for inclusion and consistency evidence.

**[E3]** Manu Sporny et al., eds. *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 19 July 2022. https://www.w3.org/TR/did-core/ **Relationship:** Adjacent decentralized identity standard; identifier resolution is not assumed to settle semantic standing or jurisdiction.

**[E4]** Juan Benet. "IPFS - Content Addressed, Versioned, P2P File System." 2014. arXiv:1407.3561. https://arxiv.org/abs/1407.3561 **Relationship:** Predecessor content-addressed network architecture; content identity is compared with, not treated as sufficient for, semantic jurisdiction.

**[E5]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E6]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E7]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

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

**[A4]** Adam Ableman. *Self-Certifying Proof-Carrying Identity for Registrar-Free Namespace Networks*. Ableman Corpus current edition; work identity `PAPER.PUB.20114888`;  
source SHA-256  
`1AFDBD390D3BF28224727FE150FFB30CA1810D997778CC8702B6CD20C4FA5B45`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Semantic Hashing: Hashes as Declared Equivalence Classes of Meaning*. Ableman Corpus current edition; work identity `PAPER.PUB.18500533`;  
source SHA-256  
`7DA63A76DDF492FFC289F486923FB430879DC148CF3BB16EB0E755E2D4AB9C14`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

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

DOI: [10.5281/zenodo.23847480](https://doi.org/10.5281/zenodo.23847480)
