# Identity Spine Doctrine

## Operational Governance for Global Term Key Admission, Separation, and Revision

### The revised doctrine separates occurrence, surface form, local binding, corpus identity, version, and coordinate.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Governed knowledge systems require a stricter distinction between semantic identity and similarity than ordinary retrieval graphs. The Identity Spine Doctrine specifies an operational profile for admitting and maintaining Global Term Keys (GTKs): corpus-wide anchors for disambiguated semantic bindings.

The source doctrine requires a sparse, stable, evidence-bound identity layer; forbids intuitive merger; treats extractor term identifiers as mechanical facts; and uses graph topology to discover candidates rather than declare identity. This revision preserves those commitments while correcting several absolutes. A surface form can invoke many bindings. A term occurrence may remain unresolved among several candidates. Cross-artifact edges establish relatedness, not identity. Content hashes identify versions, not necessarily the continuing identity of an amended GTK.

The revised doctrine separates occurrence, surface form, local binding, corpus identity, version, and coordinate. It defines an identity assertion, evidence classes, negative and polysemy tests, admission outcomes, revision and fork semantics, impact-weighted correction, and a measurable evaluation program. It positions the doctrine as a governance profile for the GTK architecture rather than a new foundational semantic primitive.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. The custody and comparison manifest is   
`work/paper-saturation-v1/evidence/identity-`

`spine-doctrine/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`DCF6BB04DE5816D37A84E2DCB4E5F2A455DE59CEC3134C8B3AF51E04670568BE`. The source remains unchanged.

The doctrine and its named failure patterns are author material. Formal schemas, qualifications, corpus routing, tests, and decisions added here are AI editorial or synthetic candidates until adopted. No GTK membership, identity merger, or corpus mutation occurs through this paper.

## 1. Identity Is Not Labeling

A word, label, identifier, embedding neighborhood, shared topic, adjacency, or repeated mention does not by itself establish semantic identity. A GTK anchors one disambiguated binding under a declared namespace, profile, and lineage.

The doctrine protects a simple invariant:

> Identity must not be promoted from resemblance without evidence that the same governed binding is intended and preserved.

This does not imply that concepts possess context-free essences. A GTK may be scoped, revised, forked, contested, or retired. The invariant is procedural: the system must expose the basis and limits of every identity assertion.

## 2. Six Objects That Must Remain Distinct

The identity spine separates:

1. **Occurrence:** one located use in an exact artifact version.
2. **Surface form:** the characters or token sequence used there.
3. **Local binding:** the meaning resolved or proposed in that context.
4. **GTK identity:** the corpus-wide governed binding, if admitted.
5. **GTK version:** one immutable state of that identity.
6. **Semantic coordinate:** a registry address or topological location used by SCIT.

One surface form can name several bindings. Several surface forms can name one binding. One occurrence can remain ambiguous. A coordinate can be stable while its metadata changes only under declared lineage rules. Collapsing these objects creates the very identity drift the doctrine is meant to prevent.

## 3. Identity Assertion

Represent a proposed cross-artifact identity as:

$$
\iota=(o_a,o_b,g,p,e^{-},e^{+},c,r),
$$

where $o_a$ and $o_b$ are source-bound occurrences, $g$ the candidate GTK, $p$ the interpretation profile, $e^{+}$ supporting evidence, $e^{-}$ counterevidence, $c$ confidence or adjudication posture, and $r$ the responsible decision and receipt.

An assertion should record exact artifact hash, span or stable locator, extractor version, local label, definition or use context, namespace, effective epoch, and dependencies. The compact source tuple   
`(artifact_id, term_id, label)` is useful for display but insufficient for durable custody when artifacts or extractors change.

## 4. Evidence for Identity

Evidence can include:

- explicit equivalence declared by an authorized source;
- shared definition with matching necessary commitments;
- bidirectional substitutability in the relevant claims without changing consequences;
- preserved invariants across transformations;
- compatible exclusions and refusal conditions;
- lineage showing rename, translation, or controlled revision; and
- independent adjudication against plausible competing bindings.

Repeated labels, embedding proximity, shared assumptions, graph edges, co-citation, paraphrase, or family resemblance are candidate-generation signals only. Even explicit equivalence is bounded by the authority and scope of its source.

An identity decision should survive a **negative test**: identify one observation that would establish difference, and search for it before admission.

## 5. Sparse, Not Arbitrarily Small

GTK should grow more slowly than raw occurrences, terms, and local concepts because it represents reusable corpus identities. But no universal count proves health. A broad multilingual or multi-domain corpus may legitimately need many GTKs; an artificially small registry can erase real distinctions.

Monitor promotion rate, merge reversal rate, unresolved ambiguity, duplicate-identity rate, maintenance cost, reuse, and downstream consequence. Sparsity is a discipline of justified promotion, not a fixed size target.

## 6. Polysemy and Ambiguity

The source rule "one term, one identity" requires a typed reading. One **resolved local binding** should not simultaneously be asserted as two incompatible GTK identities under the same profile. A surface form may map to many GTKs, and an occurrence may remain unresolved among a candidate set.

Allowed postures include `RESOLVED`, `AMBIGUOUS`, `CONTESTED`, `NEW_LOCAL_BINDING`,  
`NO_GTK_REQUIRED`,  
and   
`INSUFFICIENT_EVIDENCE`. Forcing a hard assignment can be worse than preserving ambiguity.

Polysemy is exposed through competing binding sets; it is not hidden by merger. Homonymy, metaphor, domain shift, historical change, translation, and deliberate equivocation should remain inspectable.

## 7. Mechanical Term Identity

Extractor TERM IDs are facts only relative to an artifact version and extractor run. Ordering, numbering, or stable labels must not be inferred across runs unless the extractor contract guarantees it.

A durable occurrence reference should include at least:

$$
(artifact\_hash,extractor\_version,occurrence\_id,locator,surface).
$$

Where byte spans are unstable under normalization, a locator can combine structural path, surrounding hash, and canonicalization profile. A human-readable label accompanies the reference but does not determine identity.

## 8. Topology Generates Candidates, Not Verdicts

High cross-artifact connectivity, repeated terms, shared claims, shared refusals, and overlapping invariants can reveal GTK-null concept families. They justify review. They do not establish identity.

Hub gravity is especially dangerous: a prominent GTK may attract related but non-identical concepts. Candidate generation should therefore include nearest alternatives, edge-type diversity, negative edges, namespace boundaries, and low-frequency outliers.

Topology and embeddings optimize recall; governed adjudication protects precision.

## 9. GTK Admission Workflow

A proposed GTK or membership proceeds through:

1. bind exact source occurrences and local definitions;
2. generate candidate identities and competing bindings;
3. compare invariants, exclusions, consequences, and scope;
4. search for counterexamples and polysemy;
5. classify as admit, defer, contest, split, fork, or refuse;
6. record authority, evidence, confidence, dependencies, and receipt;
7. test affected queries, claims, coordinates, and transformations; and
8. expose appeal, correction, and rollback or compensating lineage.

No automated resolver receives authorial or governance authority merely from accuracy or confidence.

## 10. Version, Amendment, and Fork

A content hash identifies an immutable GTK version. Continuing identity across versions requires a separate lineage identity and amendment relation. Otherwise any metadata or invariant change would create either a new identity silently or a misleading stable hash.

An amendment remains within a GTK only when the admitted identity criterion is preserved. If the invariant floor, scope, exclusions, or consequences change beyond that criterion, the system should fork or supersede rather than overwrite.

Historical versions remain queryable. Consumers must declare whether they follow a fixed version, an approved lineage head, or an epoch-specific view.

## 11. Correction Severity

GTK errors can propagate widely, but not every correction has equal severity. Classify impact by affected claims, artifacts, coordinates, compiled outputs, decisions, effects, reversibility, and exposure time.

A mislabeled unused candidate differs from a merger that authorized effects. Corrections should produce impact analysis, quarantined dependents where needed, a new lineage event, and a record of what cannot be automatically repaired.

## 12. Failure Patterns

- **Drift collapse:** versions change binding while retaining apparent identity.
- **Hub gravity distortion:** related concepts are absorbed by a prominent key.
- **Semantic smearing:** dense association masquerades as stable identity.
- **Paraphrase identity:** wording similarity is treated as equivalence.
- **Topology laundering:** graph position is promoted into identity.
- **Authority laundering:** a resolver's output gains standing it was not granted.
- **Version laundering:** a mutable definition is presented as one immutable object.
- **Ambiguity erasure:** uncertain occurrences are forced into a single GTK.

These are forms of ontology laundering when provisional classification becomes a corpus fact without sufficient evidence and authority.

## 13. Corpus Role and Compression

The two **Global Term Key** papers define the lexical primitive, its binding identity, alias set, competing binding set, invariant floor, adjacency, and resolution mechanics. **SCIT** defines coordinate identity, topology, candidate generation, and runtime resolution. **Meaning as Binding** supplies the broader relational account. **Ontology Laundering** diagnoses unjustified semantic promotion.

The **Identity Spine Doctrine** is the operational governance profile connecting those architectures. It should not be presented as a separate identity primitive or a replacement GTK theory.

The **Governed Meaning Base (GMB)** can custody exact occurrences, local bindings, GTK lineages, evidence, disputes, and revisions. The universal **GSM** can type identity, alias, competition, adjacency, derivation, version, and disagreement without converting an edge into equivalence.

## 14. Realization Funnel

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

- **Possibility:** enumerate registry, local-first, centralized, federated, probabilistic, human, agent, and hybrid identity regimes.
- **Specification:** define object types, identity evidence, postures, authority, lineage, correction, and receipts.
- **CM1:** retain admissible policies, including conservative high-deferral and plural-namespace variants.
- **CM2:** prefer configurations by precision, recall, reversibility, inspectability, cost, and downstream risk.
- **IC:** select an Instance Constitution or Instance Configuration for one corpus and governance regime.
- **IR:** produce an Instance Realization or Implementation Realization of extraction, resolution, registry, adjudication, and query interfaces.
- **Evidence:** measure errors, ambiguity, reversals, drift, impact, and user comprehension.
- **Revision:** amend policies, lineages, and implementations through explicit receipts.

This paper reaches Specification and proposes CM1/CM2 criteria. It does not select an IC, admit a GTK, or certify an IR. Realization-stage IR remains distinct from Intermediate Representation in MCIR and related compiler contexts.

## 15. Evaluation Program

Construct an adjudicated sample across domains, languages, historical periods, paraphrases, homonyms, metaphors, and deliberate collisions. Compare label matching, embedding similarity, graph topology, GTK resolution, and human or hybrid adjudication.

Measure identity precision and recall, ambiguous-case calibration, inter-adjudicator agreement, false merge and false split rates, reversal cost, lineage correctness, query consequence, propagation radius, latency, and maintenance burden. Report performance separately by domain and posture; do not hide deferrals inside accuracy.

## Identity Governance Without Duplicate Foundations

The completed P1 corpus supports a compressed role assignment:

- **Layer:** Lexical identity and resolution  
  **Responsible work:** the two GTK papers  
  **What it must not absorb:** corpus admission authority, complete ontology, or storage authority

- **Layer:** Admission, split, merge, amendment, and correction  
  **Responsible work:** Identity Spine Doctrine  
  **What it must not absorb:** a new concept identity or replacement GTK theory

- **Layer:** General governed binding  
  **Responsible work:** Constitutional Binding Theory  
  **What it must not absorb:** automatic proof that two occurrences share an identity

- **Layer:** Promotion-failure diagnosis  
  **Responsible work:** Ontology Laundering  
  **What it must not absorb:** the positive admission protocol itself

- **Layer:** Custody, retrieval, standing, and lineage  
  **Responsible work:** Governed Meaning Base  
  **What it must not absorb:** authorship, truth, or identity merely from storage

The Identity Spine Doctrine is therefore a **governance profile over GTK membership and lineage**. Its reusable product is an admission decision envelope:

$$
\begin{aligned}
d= (&subject, candidates, evidence, counterevidence, policy, \\
&authority, outcome, impact, receipt)
\end{aligned}.
$$

Allowed outcomes include `ADMIT_NEW`, `LINK_EXISTING`, `DEFER`, `CONTEST`, `SPLIT`, `FORK`,  
`SUPERSEDE`, `RETIRE`,  
and `REFUSE`. A decision can be exact and well-receipted while still being wrong; its value is that the error can be located, contested, and propagated through dependent projections.

Corpus-wide integration also exposes a missing dependency rule. When identity $g$ is split, merged, or superseded, the system must enumerate affected aliases, occurrences, definitions, graph edges, retrieval indexes, compiled projections, claims, and decisions. Dependents are not automatically repaired by changing the registry. They enter a typed posture such as `UNAFFECTED`,  
`RECOMPUTE_REQUIRED`, `CONTESTED`, `QUARANTINED`, or `MANUAL_REVIEW`.

The universal GSM should distinguish `SAME_BINDING_AS`, `NAMES`, `TRANSLATES_AS`,  
`PARAPHRASES`, `NARROWER_THAN`, `BROADER_THAN`, `ADJACENT_TO`, `FORKED_FROM`,  
and `SUPERSEDES`. Only the first is an identity assertion, and it is still scope- and version-bound. The doctrine should reject generic `RELATED_TO` as sufficient evidence for promotion.

This integration establishes four editorial commitments: whether to adopt the governance-profile description as the paper's official corpus role; whether to use the decision envelope above; whether identity changes must trigger dependency posture computation; and whether the positive protocol should explicitly pair with Ontology Laundering as its adversarial diagnostic rather than duplicating that paper's taxonomy.

## Identity-Change Propagation and Laundering Audit

The fixed-seed comparison with SLBC, enforcement mechanics, Governance Coverage Gaps, and Ontology Laundering turns identity governance into a dependency-wide transition rather than a registry edit:

$$
\begin{aligned}
I= (&predecessor, decision, successor, authority, evidence, \\
&dependents, propagation, coverage, counterevidence, \\
&effects, receipt, appeal)
\end{aligned}.
$$

SLBC consumes identity decisions when assigning purpose-specific standing. Enforcement structures may encode identities in data, topology, procedures, caches, or compiled gates. Every split, merge, supersession, or correction should enumerate downstream artifacts and prove or qualify propagation rather than assuming the registry update repaired them.

Governance Coverage Gaps applies to identity change paths as well as effect paths. Hidden indexes, model prompts, resolver caches, provider stores, generated code, archives, and external integrations can retain the predecessor or adopt the successor without passing through the declared spine. Closure is bounded to discovered dependents and must reopen on counterevidence.

Ontology Laundering is the adversarial diagnostic. A formally valid identity decision can still obscure authority, beneficiaries, burdens, alternatives, or incompatibility so that legitimacy appears inherited. The positive spine protocol and negative laundering audit should share exact predecessor/successor custody without collapsing into one verdict system.

The universal GSM can type   
`PROPAGATES_IDENTITY_DECISION_TO_DEPENDENT`,  
`RECOMPUTES_PURPOSE_STANDING`, `INVALIDATES_ENFORCEMENT_BINDING`,  
`ESCAPES_IDENTITY_PROPAGATION`, `AUDITED_FOR_ONTOLOGY_LAUNDERING`,  
`PRESERVES_INCOMPATIBLE_PREDECESSOR`, and   
`APPEALS_IDENTITY_TRANSITION`.

This randomized review establishes four editorial commitments: adopt the dependency-wide identity-transition record; require bounded propagation coverage and reopenable closure; invalidate semantic standing and enforcement bindings when required; and pair the positive protocol with an independent Ontology Laundering audit.

## The Layered Identity Bill of Materials

Nine downstream uses show that the Identity Spine is consumed at several different identity layers. CHC binds immutable commitments. Digital Gold needs asset and automaton continuity. GTK resolves lexical and semantic identity. Coverage and enforcement depend on current semantic subjects. Ontology Laundering challenges unjustified changes. Semantic attractors propose convergence. Project lineage binds exact generations. Semantic Legitimacy assigns purpose-specific standing.

The downstream-stable identity bill of materials is:

$$
\begin{aligned}
S= (&artifact, publication, logical\_work, version\_family, \\
&semantic\_concept, system, implementation\_instance, \\
&deployment, epoch, relations)
\end{aligned}.
$$

Every dependent should state which layer it binds and how it follows change: `PINNED_VERSION`,  
`APPROVED_HEAD`, `EPOCH_VIEW`, `RE_RESOLVE_ON_CHANGE`,  
or `MANUAL_REVIEW`. A new artifact hash does not necessarily create a new logical work. A concept split does not automatically fork a system. A system successor does not silently replace a deployment. One identity transition can affect several layers, but it must not collapse them.

Propagation should detect mixed epochs. Caches, prompts, indexes, compiled projections, commitments, enforcement structures, external integrations, and deployments may simultaneously point to predecessor and successor identities. The result is not automatically invalid, but it requires a compatibility posture, affected-use analysis, and an explicit decision about coexistence, migration, quarantine, or retirement.

The universal GSM can type   
`BINDS_IDENTITY_LAYER`, `PINS_IDENTITY_VERSION`,  
`FOLLOWS_APPROVED_HEAD`, `REQUIRES_RERESOLUTION`, `COEXISTS_ACROSS_IDENTITY_EPOCH`,  
`DETECTS_MIXED_IDENTITY_EPOCH`, `MIGRATES_DEPENDENT_BINDING`,  
and   
`REFUSES_CROSS_LAYER_COLLAPSE`.

This reverse-dependency review establishes four editorial commitments: adopt the layered identity bill of materials; require every consumer to declare its follow policy; treat mixed epochs as a first-class propagation state; and prohibit changes at one layer from silently rewriting the others.

## 16. Counterevidence and Failure Modes

The doctrine should be narrowed or rejected where: (1) GTK is treated as a label; (2) surface and binding are conflated; (3) occurrence and term type are conflated; (4) local and corpus identity are conflated; (5) version hash and continuing identity are conflated; (6) coordinate and concept are conflated; (7) repeated labels prove identity; (8) shared edges prove identity; (9) paraphrases prove identity; (10) explicit equivalence exceeds source authority; (11) definitions omit consequences; (12) exclusions conflict; (13) negative evidence is not sought; (14) one-term-one-identity erases polysemy; (15) ambiguous occurrences are forced; (16) multilingual equivalence is presumed; (17) metaphor is collapsed into literal use; (18) TERM numbering is treated as stable; (19) extractors change silently; (20) locators cannot survive normalization; (21) GTK smallness erases valid distinctions; (22) GTK growth is unconstrained; (23) hubs absorb neighbors; (24) topology becomes a verdict; (25) embeddings become identity; (26) resolver confidence becomes authority; (27) amendments rewrite history; (28) identity-changing amendments avoid forks; (29) consumers cannot pin epochs; (30) corrections omit impact; (31) rollback cannot repair downstream effects; (32) GMB inclusion becomes truth; (33) GSM edges become equivalence; (34) corpus papers are merged; (35) a specification is presented as implemented; (36) measured error exceeds simpler methods; (37) maintenance costs exceed benefits; or (38) external research contradicts novelty or adequacy claims.

## Sparse Identity Requires Evidence, Plurality, and Reversible Correction

### Public orientation

The Identity Spine Doctrine is a governance profile for GTK admission and maintenance. It separates exact occurrences, surface forms, local bindings, corpus identities, immutable versions, and semantic coordinates. Graph topology and similarity generate candidates; they do not decide identity. Admission, separation, ambiguity, fork, retirement, and correction remain explicit outcomes.

### Adversarial tests

1. **Label-identity attack.** Matching strings, acronyms, identifiers, titles, or extractor term IDs are treated as the same binding.
2. **Similarity-merger attack.** Embedding proximity, shared neighbors, co-occurrence, or topical overlap promotes identity without preservation evidence.
3. **Sparse-elite attack.** A small identity spine privileges dominant concepts, languages, disciplines, sources, or institutions and hides the governance of omission.
4. **Essence-freeze attack.** An invariant candidate becomes a context-free essence that blocks legitimate semantic development and plurality.
5. **Hash-continuity attack.** A content hash identifies one version and is treated as the continuing identity of amended or forked GTKs.
6. **Coordinate-identity attack.** A registry location or SCIT coordinate is treated as the semantic object rather than a versioned locator.
7. **Correction-cascade attack.** A mistaken identity propagates through relations and projections while impact-weighted correction misses hidden dependents.
8. **Governance-capture attack.** Admission and appeal power becomes centralized semantic sovereignty without affected-language and community recourse.

### Claim and evidence ceiling

The paper specifies an operational GTK identity-governance profile. It does not admit a GTK, merge identities, establish context-free essences, prove complete identity evidence, guarantee sparse neutrality, implement a registry, or grant canonical or author standing. The doctrine remains a profile of GTK rather than a duplicate foundational primitive.

Validation requires multilingual polysemy and ambiguity sets, positive and negative identity pairs, source and author review, fork and successor cases, hidden-dependent propagation, governance and appeal evaluation, bias analysis, and current external research. None was performed in this pass.

### Reader-facing consequence

The doctrine should make identity decisions rarer, better evidenced, easier to contest, and safer to reverse - while letting related concepts remain related without forcing them to become one thing.

## 18. Conclusion

The identity spine is not a synonym table. It is the governed boundary at which a local, source-bound use may become a reusable corpus identity. Its quality depends less on how many concepts are connected than on how explicitly identity, difference, ambiguity, version, evidence, and authority are preserved.

GTK supplies the primitive. The Identity Spine Doctrine supplies the discipline for using it without allowing similarity to become identity by accident.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of word-sense disambiguation, lexicography, ontology alignment, entity resolution, knowledge graphs, persistent identifiers, content-addressed versioning, multilingual semantics, uncertainty representation, semantic versioning, and corpus adjudication methods.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** The present paper does not claim a complete revision treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that governed knowledge systems require a stricter distinction between semantic identity and similarity than ordinary retrieval graphs. Its nearest external comparison fields are crypto, provenance, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Semantic Coordinate Identity Tokenization (SCIT).* Zenodo, 2026. doi:10.5281/zenodo.20532070

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847975](https://doi.org/10.5281/zenodo.23847975)
