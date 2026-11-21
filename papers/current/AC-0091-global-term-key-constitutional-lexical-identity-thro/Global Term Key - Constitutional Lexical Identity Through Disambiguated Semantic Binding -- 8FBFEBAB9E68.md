# Global Term Key: Constitutional Lexical Identity Through Disambiguated Semantic Binding

## Lexical Disambiguation as Constitutional Anchoring Rather Than Mere Classification

### The central claim is: Invariant lexical structure attaches not to ambiguous surface forms, but to lexically disambiguated concept-bindings.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Language systems routinely perform lexical disambiguation.

Computational linguistics performs **Word Sense Disambiguation (WSD)** to assign meanings to tokens in context. Lexicography groups synonymous meanings into synsets. Knowledge graphs map names to canonical entities. Semantic web systems assign URIs to concepts.

These systems answer a practical question:

**Which meaning is intended here?**

This paper argues that the practical question, while useful, is incomplete.

Disambiguation alone classifies.
It does not constitutionalize.

This paper introduces **Global Term Key (GTK)**: a constitutional lexical primitive that treats the **disambiguated semantic binding** as the unit of invariant analysis rather than the undifferentiated word-form.

Under the current compact definition, **GTK = RPZ1+D**: a disambiguated named view that makes a semantic identity reachable from its machine-oriented CSIL locator. Its RPZ1 structure includes a binding-identity reference, a governed alias set, and a competing-binding set for overloaded surface forms. The binding's bounded intension or invariant-floor candidates belong primarily to RPZ2; its wider typed adjacency belongs primarily to RPZ3. GTK links those layers without collapsing locating, naming, defining, and relating meaning into one object.

Existing lexical and knowledge technologies provide comparison surfaces for sense selection, synonymy, entity reference, and competing meanings. The paper's proposed constitutional addition is governed resolution, membership, provenance, standing, refusal, and revision across the layered identity-and-naming structure; novelty remains to be externally assessed.

The central claim is:

**Invariant lexical structure attaches not to ambiguous surface forms, but to lexically disambiguated concept-bindings.**

Polysemy is therefore not evidence against invariant lexical structure.

It is evidence that one token indexes multiple GTKs.

---

## Current Definition: GTK as RPZ1+D

The operative compact definition is:

$$
\operatorname{GTK}_D(c)=\Pi(c;r=1,z,\theta,D,G),
$$

where $c$ is the semantic identity, $r$ is representational zoom, $z$ is retrieval depth, $\theta$ is the requested lens, $D$ is disambiguation, and $G$ is governance and provenance. The companion location view is:

$$
\operatorname{CSIL}_D(c)=\Pi(c;r=0,z,\theta,D,G).
$$

In compact form, **CSIL = RPZ0+D** and **GTK = RPZ1+D**. RPZ0 locates an identity through a machine reference such as a coordinate, token, hash, glyph, or URI profile. RPZ1 names the resolved identity through written, spoken, abbreviated, inflected, multilingual, or otherwise governed renderings. Disambiguation $D$ prevents the name from floating free of the intended binding. GTK therefore makes a CSIL identity linguistically reachable and navigable rather than merely addressable.

This definition reorganizes rather than discards the source's three-part object:

1. **Binding Identity** points to the resolved semantic identity $c$ and its RPZ0 locator; it is not created by the surface form.
2. **Alias Set** contains governed RPZ1 renderings that may name the same identity under declared language, domain, register, time, and authority conditions.
3. **Competing Binding Set** links a surface form to other candidate identities it may name; membership records a disambiguation alternative, not equivalence.

The **invariant floor** is primarily RPZ2 intension: the bounded account of what the resolved binding means under a declared scope. The **adjacency map** is primarily RPZ3 relational manifold: typed relationships to other identities. A GTK may carry typed links or cached projections to these layers, but collapsing their contents into RPZ1 would erase the difference between locating, naming, defining, and relating meaning.

This placement exposes a live author decision. Some source-native catalog records describe Binding Identity, Alias Set, Competing Binding Set, Invariant Floor, and Adjacency Map as internal GTK components. The RPZ definition treats the latter two as linked semantic layers. Both cannot be silently presented as the same schema; their relationship requires explicit adjudication.

### Resolution Path

A GTK lookup is not a bare dictionary lookup. A candidate procedure is:

```text
surface/context -> candidate identities -> disambiguation D
                -> selected CSIL coordinate at RPZ0
                -> GTK named view at RPZ1
                -> optional RPZ2 definition and RPZ3 manifold expansion
```

Resolution should preserve alternatives, confidence or evidence, context scope, registry version, and refusal conditions. If the available context cannot distinguish candidates at the required claim level, the correct result is ambiguity, a candidate set, or refusal--not a fabricated singular binding.

## 1. The Irreducible Maneuver

At its most reduced form, GTK performs one maneuver:

1. **Resolve the active semantic binding.**
2. **Locate the invariant structure of that binding.**
3. **Map outward to aliases and competing bindings.**
4. **Reason constitutionally from the resolved semantic anchor.**

The move is not classification.

It is constitutional anchoring.

The system no longer asks:

> what does this word mean?

It asks:

> which semantic binding is active, what must it mean, and what is adjacent?

---

### 1.1 The Error of Surface-Form Primacy

Traditional lexical systems often treat the surface word as the primary lookup key.

This creates instability.

Words are often:

* polysemous;
* context-sensitive;
* register-dependent;
* domain-dependent.

Examples:

* bank
* art
* religion
* consciousness
* game

A flat lookup asks:

> what does "bank" mean?

GTK asks:

> which binding of "bank" is active?

This distinction is decisive.

Invariant structure attaches to the binding.

Not the raw token.

---

### 1.2 Binding Before Meaning

The decisive step is not interpretation.

It is binding resolution.

Before constitutional reasoning can begin, the system must identify:

the specific concept-binding currently invoked.

Without this step:

polysemy masquerades as semantic instability.

With it:

polysemy becomes lexical topology.

---

### 1.3 The GTK as a Unified Lexical Primitive

GTK unifies three directions of lexical navigation into one object.

A GTK answers simultaneously:

#### 1. Which word/concept binding call is this?

This is the resolved semantic point.

Examples:

bank(financial institution)
bank(river edge)

This corresponds to:

* WSD
* entity disambiguation
* lemma-sense resolution

---

#### 2. What other words can call this concept?

This is the outward concept-to-name fan.

Examples:

sofa <-> couch
automobile <-> car

This corresponds roughly to:

* synsets
* aliases
* multilingual lexical equivalence sets

---

#### 3. Which other concepts can this word call?

This is the outward name-to-concept fan.

Examples:

bank -> financial institution
bank -> river edge
bank -> aviation maneuver
bank -> memory reserve

This corresponds to:

* polysemy links
* competing sense candidates

Together these create a lattice rather than a lookup table.

---

### 1.4 The GTK as a Constitutional Anchor

Once the binding is resolved, the GTK becomes the anchor for constitutional analysis.

The system may then ask:

* what invariant structure must hold?
* what properties are irreducible?
* what ablation changes the concept?
* what adjacent concepts emerge when structure changes?

This is the paper's proposed extension; novelty is not established here. Existing disambiguation outputs can become inputs to a governed process that resolves an identity and then locates its bounded RPZ2 definition or invariant-floor candidates.

This is Ableman's Razor applied to lexical semantics.

---

## 2. Relationship to Existing Systems

GTK does not replace existing lexical technologies.

It composes with them.

---

### 2.1 Word Sense Disambiguation

WSD resolves which meaning is active in context.

GTK uses this as the binding-selection maneuver.

A WSD result can provide evidence for candidate selection. GTK adds a governed identity-and-naming view and can link the selected identity to separately scoped invariant analysis.

---

### 2.2 WordNet and Synsets

WordNet groups synonymous meanings into synsets and records semantic relations.

GTK absorbs the synset concept as one facet:

the Alias Set.

But GTK adds:

* invariant floors;
* ablation structures;
* adjacency mechanics.

WordNet-like synset and relation structures provide an important comparison surface. GTK's proposed addition is a governed binding to identity, naming alternatives, provenance, and linked claim-relative semantic structure.

---

### 2.3 Knowledge Graphs and URIs

Knowledge graphs assign stable identifiers to entities or concepts.

GTK resembles this in Binding Identity.

But adds the lexical and competitive topology around the identifier.

---

### 2.4 Lexicography and Lemma-Sense Pairs

Traditional dictionaries create lemma-sense entries.

GTK formalizes them constitutionally and computationally.

---

## 3. The Constitutional Layer

GTK introduces a constitutional layer above disambiguation.

The resolved binding becomes a unit that may carry:

* invariant properties;
* contextual manifold properties;
* instance-specific usage;
* amendment history.

This allows lexical entries to become constitutional objects.

Not merely dictionary entries.

---

## 4. Lexical Invariants

A resolved binding may carry a candidate invariant floor, but the floor is claim-relative rather than universal truth. Let $c$ be the resolved identity and let $\sigma$ name language, domain, community, time, granularity, and intended use. Then:

$$
I(c\mid\sigma)=\{p\mid p\text{ is proposed as necessary for }c\text{ under }\sigma\}.
$$

Each property needs a source, standing, counterexample policy, and revision history. Necessary-and-sufficient definitions may be unavailable for family-resemblance, contested, evolving, socially constituted, or open-textured concepts. In those cases GTK can still stabilize identity while the RPZ2 definition records uncertainty, plural formulations, disputed boundaries, or a deliberately shallow invariant floor.

A corpus-native example is **Work Custody**. Under one proposed scope, its candidate core includes an exact work identity, a current scoped advancement obligation, recognized acceptance, and an explicit transfer or release path. Removing acceptance yields something closer to assignment; removing currentness yields a longer-lived ownership or accountability relation; removing scope produces an unsafe blanket responsibility claim. These are hypotheses to test against exact sources and counterexamples, not lexical truths granted by the example.

## 5. Lexical Ablation and Adjacency

Ablation can generate candidate neighbors only when the removed feature, resulting interpretation, and relation type are declared. For a candidate invariant $p$:

$$
\operatorname{Ablate}(c,p,\sigma)\rightarrow\{(c',\rho,e)\},
$$

where $c'$ is a candidate neighboring identity, $\rho$ is the proposed relation, and $e$ is evidence. The result may be an empty set, several incomparable candidates, an invalid object, or a revised definition of $c$. It is not automatically a taxonomic fact.

The original chair and bird examples are pedagogically vivid but do not establish the method: a bench may also support seated bodies; an ostrich remains a bird despite lacking flight; and removing feathers from the definition of bird does not transform a bird into a bat. A rigorous worked example must distinguish a concept's actual properties, stereotypical properties, definitional criteria, historical lineage, and nearby concepts. GTK should preserve failed ablations as counterevidence rather than forcing every removed feature to yield a named neighbor.

## 6. The GTK Lattice

The layered lattice can be described as:

```text
surface form + context -> candidate semantic identities
disambiguation D -> selected CSIL coordinate (RPZ0)
selected coordinate -> GTK governed names and aliases (RPZ1)
GTK -> competing binding references for overloaded surfaces (RPZ1+D)
identity -> bounded definition or invariant-floor candidates (RPZ2)
identity -> typed adjacency and wider semantic manifold (RPZ3)
all layers -> provenance, standing, authority, evidence, and
revision lineage
```

This is a governed navigation stack, not a flat dictionary. A semantic slug is an RPZ1 reference convenience, not the identity itself. Two similar slugs do not prove identical bindings, and one binding may lawfully have several names.

## 7. Polysemy as Topology Rather Than Refutation

Polysemy is often treated as evidence against stable meaning.

GTK reframes it.

Polysemy means:

one token participates in multiple bindings.

It does not imply that each binding lacks invariant structure.

Thus:

"bank" is not unstable.

It is overloaded.

The instability is in the token.

Not the binding.

---

## 8. Constitutional Dictionaries

GTK is the lexical primitive for a Constitutional Dictionary.

A Constitutional Dictionary does not merely define words.

It declares:

* what a concept is;
* what changes it;
* what is adjacent;
* what is inherited;
* what historical amendments occurred.

This transforms dictionaries into semantic instruments.

---

## 9. Relationship to CKL

GTK is foundational to Constitutional Knowledge Language (CKL).

CKL-S-03 asserts:

words admit constitutional decomposition.

GTK provides the mechanism.

GTK becomes the governed RPZ1 naming and resolution interface for lexical constitutionalization; the underlying semantic identity remains distinct from its name layer.

---

## 10. Practical Uses

GTK enables:

* better semantic search;
* more precise AI interpretation;
* lawful lexical reasoning;
* semantic navigation;
* constitutional dictionaries;
* ambiguity detection;
* cross-domain term comparison.

Example:

"consensus" in distributed systems vs politics.

Different GTKs.

Different invariant floors.

Same surface token family.

---

## 11. Failure Modes and Limits

GTK is not universal.

Failure modes include:

* incorrect disambiguation;
* weak invariant identification;
* over-fragmentation into excessive GTKs;
* politically contested invariant floors;
* family-resemblance concepts with sparse invariant cores.

Concepts like:

art
religion
consciousness
game

may produce shallow invariant floors or large manifold regions.

GTK makes this explicit rather than hiding it.

---

## 12. Membership Governance and Nontruth

GTK membership records a naming or competing-binding relationship, not correctness, endorsement, or universal lexical authority. An alias should enter the same GTK only after evidence adequate to the intended scope supports definitional identity or an explicitly weaker relation. Mere embedding similarity, co-occurrence, shared spelling, translation convenience, or model confidence is insufficient for identity merger.

Membership records should include the surface form, language or symbol system, domain, register, community or authority basis where applicable, time/version, relation type, evidence, confidence or dispute state, and provenance. Near-identical labels with materially different definitions remain separate GTKs connected by a typed relation. Expansion should be conservative because a high-degree alias hub can pull unrelated usages into one identity and spread the error across retrieval, synthesis, and governance.

Amendment does not overwrite history. A changed invariant floor, renamed public term, split binding, merged candidate, retired alias, or revised competing-binding set produces lineage and identifies dependent projections that may have become stale. A current preferred name can change while the underlying identity remains stable; conversely, stable spelling can conceal an identity change.

## 13. GMB, Universal GSM, and the Realization Funnel

The **Governed Meaning Base (GMB)** is the current name in the author-confirmed `CCF -> CMB -> GMB` lineage. GMB can store CSIL coordinates, GTK name layers, RPZ2 definitions, RPZ3 relations, evidence, standing, disambiguation records, and revision history. GMB does not make a contested alias true or grant a concept universal authority merely by storing it.

Within the universal **Governed Semantic Model (GSM)**, GTK occupies a projection interface rather than the whole concept:

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

**Possibility** contains candidate identities, names, senses, languages, definitions, and relations. **Specification** states binding identity, disambiguation rules, invariant candidates, membership constraints, and refusal behavior. **Configuration Manifold 1 (CM1)** contains all admissible alias, competing-binding, definition, and relation configurations. **Configuration Manifold 2 (CM2)** contains the preferred admissible naming and navigation arrangements under declared accessibility, precision, cultural, domain, and governance objectives. **IC** means **Instance Constitution** or **Instance Configuration** interchangeably and binds one registry snapshot, language/domain profile, resolver policy, and evidence threshold. **IR** means **Instance Realization** or **Implementation Realization** interchangeably and includes the actual coordinate registry, resolver, index, API, interface, and stored records. **Evidence** measures resolution accuracy, collision, drift, coverage, refusal, and human interpretability. **Revision** changes bindings, names, definitions, or relations with lineage.

## GTK Role Contract

The completed P1 corpus makes it possible to state GTK's role more sharply. Five neighboring works address different questions:

- **Work:** *Constitutional Binding Theory*  
  **Question:** What makes a semantic commitment governed and revisable?  
  **GTK relation:** GTK is one lexical binding profile, not proof that the binding pattern is universal.

- **Work:** *Global Term Key: Identity Primitives in Governed Knowledge Systems*  
  **Question:** What identity-bearing lexical object should persist across uses and versions?  
  **GTK relation:** Supplies the identity-primitive emphasis; this paper supplies resolution mechanics and the RPZ1+D presentation.

- **Work:** *Identity Spine Doctrine*  
  **Question:** When may local uses be admitted, split, merged, revised, or refused?  
  **GTK relation:** Supplies the operational admission and correction profile; it does not redefine GTK's semantic object.

- **Work:** *Meaning as Binding*  
  **Question:** How does meaning arise through typed relations rather than labels alone?  
  **GTK relation:** Supplies the broader relational ontology; GTK is a lexical access surface within it.

- **Work:** *Governed Meaning Base*  
  **Question:** Where are sources, identities, names, disputes, evidence, and lineage retained?  
  **GTK relation:** GMB is the custody and retrieval substrate, not the lexical identity itself.

This division prevents the most likely authorial-compression failure: treating every paper that mentions lexical identity as a separate foundational system. The two GTK papers appear complementary but are not automatically one logical work. Until the author adjudicates their version-family relationship, they remain distinct exact works connected by `OVERLAPS_SCOPE_WITH` and

`PROPOSED_PROFILE_OF` relations.

The cross-corpus contract is:

$$
\begin{aligned}
&Occurrence \\
&\rightarrow CandidateBindingSet \\
&\rightarrow ResolutionReceipt \\
&\rightarrow GTK_{RPZ1+D} \\
&\rightarrow \{RPZ2,RPZ3\}
\end{aligned}.
$$

The arrow into GTK is not automatic promotion. The receipt binds context, alternatives, evidence, resolver, policy, confidence, authority, and refusal conditions. The outgoing links do not place full definitions or the entire semantic graph inside RPZ1. They provide governed traversal to those layers.

The universal GSM should retain at least `HAS_SURFACE_FORM`, `NAMES`, `COMPETES_WITH`,  
`RESOLVED_AS`, `DEFINED_BY`, `ADJACENT_TO`, `CONTESTED_BY`, `VERSION_OF`, `SPLIT_FROM`,  
and `SUPERSEDES`. `NAMES` is not `IDENTICAL_TO`; `ADJACENT_TO` is not `DERIVED_FROM`; and similarity is not admission evidence.

This integration establishes four editorial commitments: whether the two GTK papers are versions, companion papers, or distinct logical works; whether Invariant Floor and Adjacency Map are internal fields or linked RPZ2/RPZ3 projections; whether the Identity Spine Doctrine is the normative admission profile for GTK; and whether the compact identity-to-resolution contract above should replace duplicated architecture across the three works.

## Lexical Identity to Atlas Coordinate

The fixed-seed comparison with receipt reasoning, GCNL, SBQ, and Governed Semantic Cartography clarifies the path from a surface occurrence to a navigable atlas view:

$$
\begin{aligned}
L= (&occurrence, GCNL\_profile, candidate\_senses, \\
&resolution\_receipt, GTK, coordinate, projection, path, \\
&source\_recovery, remainder)
\end{aligned}.
$$

GCNL supplies a bounded linguistic context and preserves ambiguity or residual meaning. The resolution receipt records alternatives, policy, evidence, refusal conditions, and chosen GTK where warranted. GSC may address an atlas coordinate through that GTK and project it under a declared view. A coordinate, default map location, or successful round trip does not independently establish lexical identity.

SBQ evaluates a declared binding after identity and jurisdiction are specified. Coherence, stability, or generativity cannot decide that two occurrences share one GTK, and low quality cannot silently split an identity. Quality results may become evidence in a separately governed identity review under an explicit ceiling.

Every traversal should retain the GTK and registry version actually used. Identity change invalidates or qualifies affected coordinates, aliases, projections, routes, and cached links; the atlas must show conflict or predecessor state rather than silently moving the reader.

The universal GSM can type   
`RESOLVES_OCCURRENCE_TO_GTK`, `RECEIPTS_LEXICAL_ALTERNATIVES`,  
`ADDRESSES_ATLAS_COORDINATE_THROUGH_GTK`, `PROJECTS_WITH_REGISTRY_VERSION`,  
`ASSESSES_BINDING_QUALITY_AFTER_IDENTITY`, `INVALIDATES_ATLAS_ROUTE_AFTER_SPLIT`,  
and   
`RECOVERS_SOURCE_FROM_VIEW`.

This randomized review establishes four editorial commitments: adopt the occurrence-to-atlas chain; require resolution receipts and registry versions in governed views; keep SBQ below identity decisions; and invalidate or qualify atlas structures after GTK change.

## A Versioned Lexical Identity Service

Twenty-six downstream uses make GTK one of the most connected corpus primitives. It supports controlled language, cartography, identity spines, lexical-disambiguation protocols, binding, retrieval, receipts, semantic quality and debt, field analysis, termination records, physical and cyber-physical vocabularies, context review, consciousness research, semantic infrastructure, Water projections, and work custody. The common function is narrower than meaning: GTK resolves a surface occurrence toward a governed lexical identity under a declared context and registry.

The resolution record is:

$$
\begin{aligned}
K^*= (&occurrence, surface, context, jurisdiction, candidates, \\
&selected\_identity, sense, registry\_version, authority, \\
&evidence, standing, aliases, split\_merge, expiry, \\
&receipt, remainder)
\end{aligned}.
$$

GTK remains RPZ1+D: a stable candidate name or key plus disambiguation. It does not contain the full RPZ2-4 definition, prove two source concepts identical, determine truth, or grant permission. Unknown, ambiguous, contested, withheld, deprecated, and out-of-scope are valid results. The companion *Global Term Key: Identity Primitives in Governed Knowledge Systems* remains identity-distinct pending author adjudication.

Registry changes must propagate. A merge, split, alias change, deprecation, or revised sense invalidates or qualifies atlas links, controlled-language statements, receipts, searches, quality results, semantic maps, and dependent reasoning. Consumers should bind the registry generation and retain original surface forms so re-resolution and appeal remain possible.

The universal GSM can type   
`RESOLVES_OCCURRENCE_TO_GTK`, `BINDS_GTK_REGISTRY_VERSION`,  
`RETURNS_LEXICAL_AMBIGUITY`, `SPLITS_LEXICAL_IDENTITY`, `MERGES_WITH_REMAINDER`,  
`INVALIDATES_GTK_DEPENDENT`, `RERESOLVES_ORIGINAL_SURFACE`,  
and   
`DOES_NOT_GRANT_TRUTH_OR_AUTHORITY`.

This reverse-dependency review establishes four editorial commitments: adopt the versioned resolution record; preserve typed nonresolution and original surface forms; propagate split, merge, alias, and deprecation changes to dependents; and retain GTK as lexical identity below meaning, truth, authority, and action.

## 14. Counterevidence and Failure Modes

The expanded proposal should be narrowed or rejected where: (1) disambiguation depends on context unavailable to the resolver; (2) the same community intentionally sustains irreducible ambiguity; (3) no stable identity exists across time or use; (4) aliases encode politically or culturally contested equivalence; (5) translation lacks one-to-one concept correspondence; (6) invariant floors confuse stereotypes with necessary properties; (7) ablation produces no reproducible adjacency; (8) similarity silently becomes identity; (9) high-degree hubs create semantic gravity and collision; (10) a preferred name acquires authority over dissident or local vocabularies; (11) over-fragmentation creates a GTK per utterance; (12) under-fragmentation launders polysemy; (13) registry mutation breaks historical references; (14) different resolvers select incompatible coordinates from the same evidence; (15) the RPZ layers cannot be separated in actual use; (16) privacy-sensitive context is required for resolution; (17) a malicious party poisons aliases or competing-binding sets; (18) refusal rates make the system unusable; or (19) GTK adds no measurable value over a competent identifier-plus-lexicon architecture.

Evaluation needs exact datasets, declared senses or adjudication procedures, ambiguity and refusal metrics, cross-domain and cross-language cases, collision tests, adversarial alias injection, temporal drift, human comprehension, and comparison with simpler baselines. The current paper provides an architecture and hypotheses, not those results.

## A Stable Term Key Must Not Become a Semantic Sovereign

### Public orientation

The Global Term Key is a governed lexical-identity service. Under the current compact definition, GTK is RPZ1+D: a disambiguated named view reached from a CSIL identity through resolution. It connects aliases and competing bindings to deeper RPZ2 explanation and RPZ3 adjacency without collapsing locating, naming, defining, and relating into one object.

### Adversarial tests

1. **Registry-truth attack.** Admission to the GTK registry is treated as proof that a concept exists, is true, is important, or has canonical author standing.
2. **Identity-definition collapse.** A CSIL locator, RPZ1 name, RPZ2 explanation, invariant candidate, and RPZ3 neighborhood are treated as one immutable identity payload.
3. **Alias-capture attack.** A dominant institution, language, discipline, or community controls preferred names and suppresses local, minority, reclaimed, or contested terminology.
4. **False-disambiguation attack.** The resolver forces a sense choice when context is insufficient, mixed, novel, deliberately ambiguous, or operating across several bindings.
5. **Invariant-floor attack.** A proposed invariant becomes a membership test that excludes legitimate variation or converts a theory into lexical fact.
6. **Version-drift attack.** A stable key points through changing membership, explanation, standing, or adjacency without a visible validity epoch and successor relation.
7. **Collision-and-spoof attack.** Confusable labels, aliases, homographs, Unicode, namespace overlap, malicious metadata, or resolver manipulation redirect a binding.
8. **Resolver-authority attack.** Search rank, model confidence, or automatic path resolution silently decides identity where refusal or human adjudication is required.

### Claim and evidence ceiling

The paper specifies a layered lexical identity and resolution proposal. It does not establish that GTK is novel, globally complete, language-neutral, culturally legitimate, collision-free, implemented, canonical, or able to determine truth, meaning, identity, or author standing. The relationship among the current RPZ1+D definition and older invariant-floor or adjacency descriptions remains an author decision, not an automatic merger.

Validation requires multilingual and cross-domain ambiguity sets, adversarial collisions, refusal and mixed-binding cases, version and successor tests, governance and appeal studies, privacy review, resolver baselines, and current comparison with lexical, ontology, semantic-web, identifier, and knowledge-graph systems. No registry, resolver, catalog admission, or external research was performed in this pass.

### Reader-facing consequence

GTK should help a reader and an agent say which meaning-bound name is intended, how it was resolved, what alternatives remain, and where its explanation and relations live - while preserving the right to answer unknown, mixed, contested, or not yet named.

## 16. Corpus Integration Sources

This pass binds the current Ableman semantic kernel (SHA-256  
`E0378C1D739BFBE8EC317EA488857731E5CB5574850907D0808B15A09DE9E27E`), RPZ catalog (

`90CABC7F33308703905B3C681D861A28283A5CACD469A449CEC54ECEC0CE36D5`), semantic slug catalog (  
`11C73B280F188E049CD70F13D3E54DB3A6480933593875F3FF18C4F4F777F124`), *Theory of Semantic Computing Infrastructure* (  
`CC52AEB0FA700AF66C8B2897F76F45FB78177343A0FF274B1BAD2106A6F6E8AB`), the SMT worked example (  
`BAA41D5FCC820805F23676EED9B1542E0DC8744F7D7A145D21F4BE99A0D99BC9`), *Governed Semantic Cartography* (  
`EB64EFEA1CCFD1DB7DA65E0989F9372DE3C30E0B974A260554D1FE4A089B1AD3`), and GMB semantic-manifold documentation (  
`49A05A424F226A21C81D638727E1165DE1AD55AB1CBDC56EA65D67A1362A4B08`). Exact custody does not settle the catalog tension or grant identity, correctness, implementation, or standing.

## 17. What GTK Is Not

GTK is not merely:

* a synonym list;
* a WSD system;
* a dictionary entry;
* a WordNet clone;
* an entity linker.

GTK is a constitutional lexical identity primitive.

It treats semantic binding as the atom of lexical governance.

---

## 18. Conclusion

Words are not stable.

Bindings can be.

By shifting invariant analysis from ambiguous word-forms to disambiguated semantic bindings, GTK transforms lexical disambiguation into constitutional anchoring.

Existing systems identify which meaning is intended.

GTK identifies:

what that meaning must be,
what else may call it,
what else it may call,
and what lies adjacent if its structure changes.

The word is no longer the semantic atom.

The binding is.

And the lattice is the map.

---

## Editorial Provenance and Standing

### Source, Evidence, and Standing
This is an AI-prepared successor revision candidate derived from one exact author manuscript. The integration custody manifest is   
`work/paper-saturation-v1/evidence/global-term-`

`key/integration-custody-manifest.v0.1.json`,  
SHA-256  
`55BBC129BD11C01456CBF17A141696003B5AF56A98231862A49612A13E62D584`. The exact source remains unchanged. The title, binding-before-surface thesis, three-part GTK, lexical lattice, invariant-floor and ablation proposals, CKL relationship, practical uses, limits, and conclusion are author material. The source begins with an author-supplied draft note saying its structural-unification definition is superseded in one important respect by the current resolution-mechanics definition: GTK is RPZ1+D, reached from a CSIL identity through disambiguated path resolution. This pass incorporates that note, distinguishes RPZ0 identity location from RPZ1 naming and RPZ2/RPZ3 meaning, replaces misleading invariant examples, and adds membership governance, GMB/universal-GSM placement, counterevidence, and open editorial questions. Those changes are AI editorial or synthetic contributions until adopted.
The compact kernel and current RPZ catalog support the RPZ1+D framing, while other source-native catalog records still describe invariant-floor and adjacency-map subcomponents inside GTK. This candidate offers a layered reconciliation but does not decide that identity question. No resolver, registry, CSIL assignment, dictionary, ablation procedure, or semantic-search system was executed. External comparisons were not revalidated. No publication, canonical standing, catalog admission, identity merger, conformance assignment, or implementation authority is granted.

## Corpus-Wide Reference Positioning

This paper argues that language systems routinely perform lexical disambiguation. Its nearest external comparison fields are semantic, governance, crypto. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Richard Cyganiak, David Wood, and Markus Lanthaler, eds. *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation, 25 February 2014. https://www.w3.org/TR/rdf11-concepts/ **Relationship:** Adjacent graph data model and identity baseline.

**[E2]** Alistair Miles and Sean Bechhofer, eds. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. https://www.w3.org/TR/skos-reference **Relationship:** Adjacent standard for concepts, labels, schemes, notes, and semantic mappings.

**[E3]** W3C OWL Working Group. *OWL 2 Web Ontology Language Document Overview*, Second Edition. W3C Recommendation, 11 December 2012. https://www.w3.org/TR/owl2-overview/ **Relationship:** Adjacent formal ontology standard used to compare declared semantics and inference commitments.

**[E4]** Mark D. Wilkinson et al. "The FAIR Guiding Principles for Scientific Data Management and Stewardship." *Scientific Data* 3, 2016, 160018. DOI: 10.1038/sdata.2016.18. https://doi.org/10.1038/sdata.2016.18 **Relationship:** Predecessor stewardship principles for findability, accessibility, interoperability, and reuse.

**[E5]** Peter Gardenfors. *Conceptual Spaces: The Geometry of Thought*. MIT Press, 2000. [mitpress.mit.edu source](https://mitpress.mit.edu/9780262572194/conceptual-spaces/) **Relationship:** Predecessor geometric treatment of concepts; cited as comparison, not as validation of the paper's manifold terminology.

**[E6]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E7]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

### Ableman corpus

**[A1]** Adam Ableman. *Meaning as Binding*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-5F976917F0B283EA`;  
source SHA-256  
`A470D1A0B9ED7C3CEAB6BB88BE4B642A2BA36427447F787764329FD574DA0C97`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D95CCC4FB7B58BFB`;  
source SHA-256  
`A3B62E50F8BEE125FDAE0D38C2839AFD1CCC138296268BF93217481E38AA48EA`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Semantic Manifold Topology*. Ableman Corpus current edition; work identity `PAPER.PUB.20257244`;  
source SHA-256  
`B8F28CC652A73A3EE4CF6FD0E23C1ABC922A6660319B2FB4CC1CCAAA606EC64A`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Global Term Key: Identity Primitives in Governed Knowledge Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-358AC09F5A13587E`;  
source SHA-256  
`AFB29CFCB4B58A78B79709AD453CEE9088CCB2AE40F30A70260F1B54F5160579`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Semantic Legitimacy Before Context*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-091E34BA93992CE4`;  
source SHA-256  
`DEB7626CE1AB54F4B541347DCC3C4E14DC4F682230ACCCE1A93D1D536A50C44C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

Adam Ableman *Semantic Coordinate Identity Tokenization (SCIT).* Zenodo, 2026. doi:10.5281/zenodo.20532070

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847756](https://doi.org/10.5281/zenodo.23847756)
