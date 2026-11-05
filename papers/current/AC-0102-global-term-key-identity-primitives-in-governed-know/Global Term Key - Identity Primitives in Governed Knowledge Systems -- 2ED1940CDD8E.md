# Global Term Key: Identity Primitives in Governed Knowledge Systems

## Disambiguated Semantic Binding as a Governed Lexical Interface

### Knowledge systems often use a surface word, embedding neighborhood, graph node, URI, or schema type as though it were already a stable semantic identity.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Knowledge systems often use a surface word, embedding neighborhood, graph node, URI, or schema type as though it were already a stable semantic identity. These devices are valuable, but none alone decides whether two uses carry the same binding, whether one term names several bindings, or whether a binding may be used for a consequential claim. When similarity, co-occurrence, or shared spelling is silently promoted to identity, concept drift, hub gravity, semantic smearing, and polysemy-driven conflation follow.

This paper develops the **Global Term Key (GTK)** as a governed lexical interface around a disambiguated semantic binding. Its original three-part insight remains: a GTK exposes (1) the active binding identity, (2) the aliases admitted for that binding, and (3) the competing bindings reachable from the same surface forms. Corpus integration sharpens the architecture. The coordinate that locates a binding belongs to the Semantic Coordinate Identity Layer at Representation-Pointer Zoom 0 (CSIL/RPZ0). GTK lives at RPZ1: it supplies the governed bound-term, named renderings, aliases, inflections, and competing-binding fan through which that coordinate becomes humanly and computationally navigable. A disambiguation context $D$ selects among candidates without converting probability or convenience into semantic authority.

The invariant floor, definition, and admissible variation associated with a binding are therefore linked specification at RPZ2 and beyond, not all compressed into the key itself. Likewise, adjacency is not universally established by removing one alleged invariant. It is a typed, lens-relative relation that must state which features, ontology, metric, registry, authority, and evidence make two bindings neighbors. Content addressing preserves exact record identity under a declared schema; it does not prove that the record is semantically correct.

GTK thereby becomes a bridge among lexical resolution, semantic coordinates, the Governed Meaning Base (GMB), semantic hashing, governed context formation, and machine-operable semantic languages. The proposal is architectural rather than empirical. It specifies a resolution contract, failure semantics, realization funnel, conformance questions, and counterevidence program. It does not claim that all concepts possess crisp necessary-and-sufficient invariants, that automated disambiguation is infallible, or that this paper establishes novelty relative to current lexical and knowledge-representation research.

## 1. The Identity Problem

### 1.1 Similarity is not identity

A knowledge system may place two terms close together because they share tokens, contexts, embeddings, citations, relations, or users. Proximity can be useful evidence. It is not by itself an identity decision.

Three relations must remain distinct:

| Relation | Meaning |
|---|---|
| Identity | Two references are admitted as reaching the same governed binding under a named registry and version. |
| Similarity | Two distinct bindings share features, contexts, functions, or relations under a declared lens. |
| Conflation | A system treats distinct bindings as one without adequate warrant or an explicit equivalence decision. |

The distinction is constitutional because identity decisions affect what can be inherited. If a claim, constraint, permission, or evidence record attached to one binding silently transfers to a merely similar binding, the system launders semantic standing through proximity.

### 1.2 Surface-form primacy

Words such as `bank`, `chair`, `consensus`, `art`,  
and `game` can participate in several bindings. The question "what does this word mean?" is underspecified until the system knows the domain, use, context, registry, purpose, and candidate sense inventory.

GTK replaces surface-form primacy with binding-oriented resolution:

> Which registered binding is being invoked, through which name, under which context and authority, with what uncertainty and alternatives?

This does not make bindings eternally stable. It creates a place where stability, contest, uncertainty, and revision can be represented rather than hidden inside a token.

### 1.3 Identity layers

At least five identity questions recur:

1. Are these the same exact bytes?
2. Are these the same record version?
3. Are these references assigned the same registry coordinate?
4. Are these two records declared semantically equivalent under a named lens?
5. Do these artifacts concern the same broader concept or work despite remaining distinct versions or projections?

A hash can answer the first question when the canonical bytes and algorithm are known. A registry may answer the third. Neither automatically answers the fourth or fifth. GTK must preserve these layers rather than collapse them into a single word called identity.

## 2. The Integrated GTK Definition

### 2.1 Coordinate, name, intension, and manifold

The current corpus-wide representation stack distinguishes:

- **Zoom:** RPZ0  
  **Function:** Locate  
  **Typical content:** CSIL integer, glyph, URI, or integrity hash bound to a coordinate.

- **Zoom:** RPZ1  
  **Function:** Name  
  **Typical content:** Bound-term, orthographic and phonetic forms, acronym, aliases, inflections, and competing-binding fan. GTK lives here.

- **Zoom:** RPZ2  
  **Function:** Explain  
  **Typical content:** Intension, definition, criteria, invariant candidates, qualifications, and scope.

- **Zoom:** RPZ3  
  **Function:** Relate  
  **Typical content:** Typed manifold of dependencies, adjacencies, conflicts, realizations, evidence, and provenance.

The disambiguation component $D$ is carried with a representation when a surface form does not select one coordinate by itself. In compact form:

$$
\mathrm{CSIL}=\mathrm{RPZ0}+D, \qquad \mathrm{GTK}=\mathrm{RPZ1}+D.
$$

This is a functional distinction, not a claim that one database or implementation must use these exact field names.

### 2.2 The original three-part GTK

The source paper and its distinct local companion define a GTK through [GTK-SOURCE] [GTK-COMPANION]:

1. **Binding identity**: the coordinate selected as active.
2. **Alias set**: other admitted names for that binding.
3. **Competing binding set**: other coordinates reachable from one or more of those surface forms.

That structure remains the GTK's minimum lexical view. The integration correction is that the binding identity is referenced by GTK rather than manufactured by its name record, while the invariant floor and full relational neighborhood remain linked semantic structures rather than being treated as mere strings inside the key.

For registry version $v$, an operational GTK record can be represented as:

$$
G_v(c)=\langle c,N_c,A_c,P_c,L_c,\gamma_c\rangle,
$$

where:

* $c$ is the registry coordinate;
* $N_c$ is the set of admitted named renderings, including orthographic, phonetic, and acronym forms;
* $A_c$ is the set of aliases asserted to reach the same coordinate under a declared equivalence regime;
* $P_c$ is the competing-binding fan for surfaces shared with other coordinates;
* $L_c$ is version and predecessor lineage; and
* $\gamma_c$ carries provenance, authority, standing, jurisdiction, and governance metadata.

The record may link to RPZ2 definitions and RPZ3 relations. It should not pretend that naming, definition, graph topology, evidence, and governance are the same field.

### 2.3 A bound-term is not necessarily one word

A GTK can name a multiword concept, proper noun, acronym, symbolic expression, cross-lingual equivalence candidate, or other governed surface. Conversely, one written word can reach many GTKs. This many-to-many structure is the lexical lattice:

```text
surface form -> candidate coordinates
coordinate -> governed named renderings
coordinate -> admitted aliases
surface form -> competing coordinates
coordinate -> linked RPZ2 specifications
coordinate -> typed RPZ3 relations
coordinate version -> predecessor and successor lineage
```

Calling this structure a lattice is architectural shorthand unless the implemented ordering actually satisfies lattice laws. A realization should say whether it provides a mathematical lattice, a typed graph, a hypergraph, a registry plus indexes, or another structure.

## 3. Resolution is a Governed Operation

Let $s$ be an observed surface, $k$ a context bundle, $p$ a declared purpose, and $R_v$ a registry version. Candidate generation returns:

$$
\mathrm{Cand}_{R_v}(s)=\{c_1,\ldots,c_n\}.
$$

A resolver may rank these candidates, but ranking is not admission. The governed resolution operation is:

$$
\mathrm{Resolve}(s,k,p,R_v)\rightarrow
\begin{cases}
\mathrm{BIND}(c,q,e),\\
\mathrm{DEFER}(r),\\
\mathrm{REFUSE}(r),\\
\mathrm{GAP}(r),\\
\mathrm{CONTESTED}(C,r),
\end{cases}
$$

where $q$ is a calibrated scope or confidence statement, $e$ is the evidence and receipt binding, $r$ is a reason, and $C$ is an unresolved candidate set.

These outcomes distinguish several cases that a forced classifier would collapse:

* `BIND`: one coordinate is admitted for the named purpose and scope.
* `DEFER`: evidence, authority, or context may become sufficient later.
* `REFUSE`: the requested binding operation is inadmissible, unsafe, or outside authority.
* `GAP`: the registry lacks an adequate candidate or required schema.
* `CONTESTED`: multiple candidates or communities retain material standing.

An exploratory search need not generate the same receipt as a binding used to authorize action. The effect surface determines the evidence and authority burden.

### 3.1 No silent invention

A resolver may propose a new candidate coordinate, alias, or relation. It must not silently create canonical standing merely because no existing entry fits. Proposed growth belongs in a candidate working registry with provenance and fresh identity until an authorized promotion decision occurs.

### 3.2 Context helps; context does not self-authorize

Context can narrow candidate bindings. It can also be poisoned, incomplete, private, biased, or constructed under the wrong purpose. The governed-context work in the corpus therefore precedes binding effect: the system records which sources were admitted, transformed, omitted, or withheld before treating context as warrant.

## 4. Lexical Specification and Invariant Floors

### 4.1 What an invariant floor can mean

The source paper attaches an invariant floor to each binding. The defensible integrated claim is narrower:

> A binding may carry a versioned specification of criteria whose violation is declared sufficient to refuse a proposed use or instance under a named domain, purpose, and ontology.

This can be valuable without asserting that every natural-language concept has one timeless essence. Some bindings have crisp formal criteria. Others are prototypes, clusters, family-resemblance structures, contested social classifications, open-textured legal terms, or historically changing practices.

Let $I_v(c)$ be a versioned set of declared criteria and $x$ a proposed instance. A configured admission test may use:

$$
\mathrm{Admit}_{v,p}(x,c)=1
\quad\text{only if}\quad
\forall i\in I_v(c),\;\mathrm{Eval}_{v,p}(x,i)\in\{\mathrm{SAT},\mathrm{QUALIFIED}\}.
$$

The equation describes one policy family. It does not prove that $I_v(c)$ is complete, universally accepted, or correctly measured. `UNKNOWN`,  
`CONTESTED`,  
and inapplicable criteria must remain visible rather than being converted to failure or success by convenience.

### 4.2 Specification is not the key

The GTK names and resolves the binding. Its linked RPZ2 specification explains the criteria, definitions, and qualifications. Keeping these layers separate permits:

* several definitions or community views to reference one coordinate without silent equivalence;
* a successor definition to preserve coordinate lineage while changing its version;
* a contested binding to retain multiple scoped specifications;
* a machine code to stay short while its explanation remains thick; and
* the system to distinguish a name change from a semantic amendment.

### 4.3 Correction of the chair and bird examples

Examples such as chairs and birds are pedagogically useful but cannot establish universal invariant floors. Stools may still support seated bodies; floor chairs may not elevate the body in the expected way; penguins do not show that flight can simply be removed from a generic bird definition; bats do not become adjacent to birds merely because feathers are removed.

The better use of ablation is diagnostic. Remove or alter a declared criterion, then ask which existing coordinates become plausible under the same ontology and lens. The result is a candidate adjacency or counterexample, not an automatic taxonomic fact.

## 5. Adjacency is Typed and Lens-Relative

The source proposal defines neighbors as GTKs whose invariant floors differ by one invariant. That is one possible Hamming-style configuration, not a universal law of semantic adjacency.

For lens $\ell$, registry version $v$, and relation type $t$, define:

$$
\mathrm{Adj}_{v,\ell,t}(c_i,c_j)
$$

only when the relation contract states:

* the compared features or definitions;
* how missing, disputed, or weighted features are handled;
* the distance or structural rule;
* the direction and relation type;
* the authority and evidence for the edge;
* the applicable domain and time; and
* the edge's standing and revision triggers.

Possible relation types include `ALIAS_OF`, `COMPETES_FOR_SURFACE`, `BROADER_THAN`,  
`NARROWER_THAN`, `FUNCTIONALLY_SIMILAR_TO`, `HISTORICAL_SUCCESSOR_OF`, `CONFLICTS_WITH`,  
and   
`ABLATION_CANDIDATE_OF`. They should not be collapsed into a generic neighbor edge.

This correction connects GTK to Governed Semantic Cartography: navigation occurs over registered coordinates and typed paths, while GTK provides the bound-term surface used to name and disambiguate those coordinates.

## 6. Content Addressing and Semantic Hashing

If a canonical GTK record is serialized under schema $S_v$ and canonicalization function $C_v$, a record hash may be:

$$
h=H(S_v\,\|\,C_v(G_v(c))).
$$

This commitment can establish that two parties possess the same canonical bytes under the declared scheme. It can detect record drift and bind a receipt to an exact version. It does not establish that:

* the coordinate denotes the correct concept;
* the alias set is complete or fair;
* competing bindings were not omitted;
* the invariant criteria are true;
* the registry authority is legitimate; or
* two different canonical records are semantically unequal in every respect.

These limitations are the direct contribution of Semantic Hashing, Constitutional Semantic Hashing, and the Three Hash Rule to GTK [SH] [CSH] [THR]. Hash identity, constitutional identity, semantic equivalence, and evidentiary sufficiency are separate claims.

## 7. GTK in the Governed Meaning Base

The current architecture name is **Governed Meaning Base (GMB)** in the author-confirmed lineage `CCF -> CMB -> GMB` [GMB-HISTORICAL-SOURCE]. Historical papers and titles using CCF or CMB remain valid source records, but new current-architecture synthesis uses GMB.

GMB can host the coordinates, GTK records, definition versions, typed relations, evidence bindings, negative edges, disputes, and revision lineage required by the proposal. It does not make a GTK valid merely by storing it. Admission still requires declared authority, policy, evidence, schema, and predecessor state.

The **Constitutional Dictionary (CD)** is best treated here as a candidate lexical profile or projection of GMB unless the author establishes differential obligations that justify independent system standing. A CD interface might expose:

* surface and alias lookup;
* candidate and competing bindings;
* selected coordinate and registry version;
* RPZ2 definitions and qualifications;
* RPZ3 typed relations;
* evidence, standing, authority, and lineage; and
* proposal, contest, refusal, and amendment operations.

This compression is provisional. It does not merge CD and GMB identities or decide whether a future implementation should separate their services.

## 8. Relationship to Other Corpus Machinery

### 8.1 Meaning as Binding

Meaning as Binding supplies the relational thesis: a term becomes usable through a governed relation among symbol, target, context, authority, and consequence [MAB]. GTK is the lexical resolution profile of that broader binding relation, not a replacement for the theory.

### 8.2 Semantic Legitimacy Before Context

Semantic Legitimacy Before Context prevents a useful-looking context from laundering an unsupported binding [SLBC]. GTK supplies a coordinate and named candidate; legitimacy requires provenance, authority, evidence, jurisdiction, and a declared use.

### 8.3 Governed Semantic Cartography

Cartography supplies coordinates, projections, typed traversal, and path governance [GSC]. GTK supplies RPZ1 names and competing-binding routes around those coordinates. An atlas without GTK may be addressable but lexically opaque; GTK without an atlas may resolve names but lack navigable relational structure.

### 8.4 Governed Semantic Tokens

A governed semantic token controls when an observed signal may enter a semantic system and with what provenance [GST]. GTK controls which named binding that admitted signal is proposed to invoke. Token admission and binding resolution are adjacent gates, not identical operations.

### 8.5 GCNL and GCML

Governed Controlled Natural Language can require explicit GTK or coordinate references where ordinary words remain ambiguous [GCNL]. Governed Controlled Machine Language can lower those references into schema-valid machine forms [GCML]. Neither language should infer canonical identity merely from an identical spelling.

### 8.6 Constitutional Binding Theory

Constitutional Binding Theory generalizes anchor resolution across semantic and operational systems [CBT]. GTK is a lexical specialization. The specialization should retain the general theory's authority, context, evidence, refusal, and revision obligations without claiming that every binding problem is lexical.

### 8.7 CSIL, RPZ, and the Semantic Index

CSIL answers where a registered concept is located. RPZ determines how much representation is loaded. GTK supplies the RPZ1 bound-term surface. The semantic index uses stable slugs and coordinates to retrieve them. These are complementary profiles of one semantic access architecture, not four competing definitions of the same object.

## 9. Worked Resolution Example

Consider the surface form `consensus` in a document about governance and distributed systems.

Candidate bindings might include:

* $c_1$: agreement among participants;
* $c_2$: a distributed-protocol decision property;
* $c_3$: a political claim of broad social assent; and
* $c_4$: an organizational decision procedure.

The context contains words such as `quorum`, `fault`, and `replica`,  
so a statistical resolver ranks $c_2$ first. A GTK-aware pipeline still asks:

1. Which registry and version supplied the candidate set?
2. Does the document use `consensus` technically, metaphorically, or both?
3. Is the purpose retrieval, explanation, evidence, or authorization?
4. What evidence supports $c_2$ and what passages still support $c_3$ or $c_4$?
5. Would a wrong binding transfer institutional legitimacy to a technical quorum, or technical assurance to a political claim?

For exploratory retrieval, the system may return all four with ranks. For a binding assertion in a formal specification, it may emit `BIND(c_2)` only for the exact clause and preserve a receipt. If the text deliberately trades on both technical and political meanings, the correct outcome may be

`CONTESTED({c_2,c_3})` or an explicit multi-binding annotation rather than forced disambiguation.

This example shows why polysemy is topological but not harmless. The competing-binding fan makes alternatives visible; governance determines whether one may be selected for a particular effect.

## 10. The Realization Funnel

| Stage | GTK work |
|---|---|
| Possibility | Explore alternative identity schemes, sense inventories, graph models, community ontologies, alias policies, harmful mergers, fragmentation, and open-world growth. |
| Specification | Define coordinate, GTK, rendering, alias, competing binding, definition, relation, lineage, authority, outcome, receipt, privacy, and revision contracts. |
| CM1 | Enumerate admissible registry and resolver configurations, including expensive, fragmented, centralized, biased, privacy-invasive, and low-recall forms. |
| CM2 | Prefer configurations with explicit uncertainty, plural views, false-merge resistance, recoverability, low authority concentration, inspectable provenance, and proportional cost. |
| Instance Configuration | Bind the exact registry version, schemas, languages, domains, candidate generators, models, thresholds, authorities, evidence sources, privacy policy, and effect surface. |
| Implementation Realization | Build registry storage, indexes, resolver, proposal and review interfaces, receipts, typed graph, lineage, access control, and export formats. |
| Evidence | Test exact replay, resolution, abstention, false merge and split, alias integrity, multilingual behavior, adversarial poisoning, fairness, privacy, drift, and recovery. |
| Revision | Produce successor coordinates, names, aliases, definitions, relations, policies, models, and claims while retaining predecessor custody and disputes. |

The source paper reaches a substantial Specification in the corpus-wide realization funnel associated with Ableman's Razor [RAZOR]. It does not by itself establish an evidence-qualified Implementation Realization.

## 11. Evidence and Evaluation

A GTK implementation should not be evaluated by lookup success alone. Useful dimensions include:

| Dimension | Question |
|---|---|
| Candidate coverage | Was the applicable binding present in the candidate set? |
| Resolution accuracy | Was the selected coordinate appropriate under the declared annotation and purpose? |
| Calibration | Do confidence and abstention statements track observed error? |
| False merge | How often are distinct bindings collapsed? |
| False split | How often is one binding fragmented without warrant? |
| Alias integrity | Do aliases preserve scope, register, language, and community differences? |
| Competing-set recall | Are material alternative bindings visible? |
| Lineage continuity | Can prior states and amendment reasons be reconstructed? |
| Adversarial robustness | Can poisoned context, hub gravity, or alias injection force standing transfer? |
| Contestability | Can affected users inspect, challenge, fork, or refuse a binding? |
| Privacy | Does resolution avoid unnecessary disclosure of sensitive context? |
| Portability | Can a fresh environment reconstruct the claimed registry and results from exact artifacts? |

Any empirical claim must bind the exact corpus, registry, annotation protocol, language, domain, resolver, model, prompt, threshold, seeds, adjudicators, metrics, uncertainty, and failure set. This paper supplies no such completed package.

## GTK Record, Resolver, and Conformance Profile

Across the completed P1 corpus, this paper is best compressed as the **engineering specification for GTK records, governed resolution, adjacency, hashing, and conformance**, while *Global Term Key: Constitutional Lexical Identity Through Disambiguated Semantic Binding* remains the broader lexical-identity theory. This is a companion relationship, not an automatic logical-work or publication-identity merger.

- **Adjacent work:** *Global Term Key: Constitutional Lexical Identity Through Disambiguated Semantic Binding*  
  **Supplies:** The foundational lexical-identity, coordinate, binding, and disambiguation thesis.  
  **Engineering-paper boundary:** This paper specifies the implementable record and resolver surface.

- **Adjacent work:** *Constitutional Binding Theory: Governed Anchor Resolution as a Universal Pattern in Semantic Systems*  
  **Supplies:** The general anchor-resolution pattern.  
  **Engineering-paper boundary:** GTK is the lexical specialization with registry and term-specific obligations.

- **Adjacent work:** *Constitutional/Crystallized Meaning Base (CMB)*  
  **Supplies:** The historical meaning-base paper in the current GMB lineage.  
  **Engineering-paper boundary:** Current GMB can host GTK records; storage does not settle their identity or standing.

- **Adjacent work:** *Governed Semantic Cartography*  
  **Supplies:** Coordinates, projections, traversals, and atlas coherence.  
  **Engineering-paper boundary:** GSC consumes resolved coordinates; GTK does not determine every map or path.

- **Adjacent work:** *Meaning as Binding*  
  **Supplies:** The compact ontology of semantic relations under context and constraint.  
  **Engineering-paper boundary:** GTK addresses and disambiguates bindings; it does not exhaust their meaning.

A GTK record should bind:

$$
\begin{aligned}
G= (&coordinate, names, intension, extensions, jurisdictions, \\
&aliases, exclusions, adjacencies, resolver\_policy, \\
&evidence, standing, revision)
\end{aligned}.
$$

The coordinate, preferred name, source label, lexical sense, definition, extension, concept identity, and rendered slug remain separate. A content hash can identify an exact record encoding but does not establish cross-version semantic identity. Resolution must return a typed result, ambiguity set, gap, or refusal rather than silently inventing a coordinate.

Conformance tests should cover alias collision, polysemy, homography, multilingual names, compound terms, historical names, unresolved references, competing registries, jurisdiction shifts, version migration, and negative adjacency. Resolver accuracy, refusal calibration, explanation quality, and identity stability are independent measures.

The universal GSM can type `REGISTERED_AS_GTK`, `HAS_PREFERRED_NAME`, `HAS_ALIAS`,  
`EXCLUDES_SENSE`, `VALID_IN_JURISDICTION`, `ADJACENT_UNDER_LENS`, `RESOLVED_BY_POLICY`,  
`AMBIGUOUS_WITH`, `REFUSED_AS_UNRESOLVED`, `MIGRATED_TO_GTK_VERSION`,  
and   
`HASH_IDENTIFIES_RECORD`. This preserves lexical identity without overloading the key.

This integration establishes four editorial commitments: classify this work as the GTK engineering companion rather than a duplicate foundational paper; adopt the GTK-record envelope; require typed ambiguity/gap/refusal results; and adopt the multi-axis conformance program.

## Resolver-to-Use Contract

The fixed-seed comparison with the constitutional syscall architecture, *Who Has the Ball?*, Terminability, and the Water/MCIR projection shows that resolving a term is only the beginning of an operational use:

$$
\begin{aligned}
U= (&GTK, record\_version, resolver\_policy, result, consumer, \\
&purpose, jurisdiction, authority, effect, receipt, \\
&remainder)
\end{aligned}.
$$

A syscall consumer needs exact capability, target, safety-profile, outcome, and recovery identities, but a resolved term does not grant the capability or authorize the effect. A custody interface needs exact work and subject identities, but the GTK is not the work head, custody record, or transfer receipt.

Terminability makes jurisdiction and sense especially consequential: ending a process, deleting state, interrupting an episode, foreclosing a continuation, and ending a subject cannot share one unqualified key. GTK resolution can expose ambiguity and route the claim to the correct definition; it cannot decide moral standing or the ending disposition.

Water's flow terms require the opposite direction of discipline. A metaphor label such as source, channel, confluence, leak, gate, or sink should resolve to an exact MCIR/GSM object or remain explicitly pedagogical. Registering the metaphor in GTK does not make the mapping technically valid or causally explanatory.

The universal GSM can type   
`RESOLVES_GTK_FOR_USE`, `CONSUMES_RESOLUTION_UNDER_PURPOSE`,  
`REQUIRES_SEPARATE_CAPABILITY_AUTHORITY`, `DISTINGUISHES_WORK_KEY_FROM_WORK_HEAD`,  
`DISAMBIGUATES_ENDING_EVENT`, `MAPS_METAPHOR_TO_TYPED_OBJECT`,  
and   
`RECEIPTS_RESOLUTION_REMAINDER`.

This randomized review establishes four editorial commitments: adopt the resolver-to-use contract; require consumer, purpose, jurisdiction, and version at consequential use sites; keep lexical identity distinct from capability, custody, moral standing, and authority; and require technical metaphor mappings to resolve to typed objects or remain pedagogical.

## Lexical Identity Record and Resolver Interface

Seven downstream uses apply this paper to hash commitments, consciousness discourse, the companion GTK theory, admissibility-gated retrieval, qualia mappings, and shared-experience bridges. They support a concrete lexical identity record and resolver interface. They do not yet settle whether this paper and *Global Term Key: Constitutional Lexical Identity Through Disambiguated Semantic Binding* are one version family, complementary papers, or partially overlapping restatements; that identity decision remains with the author.

$$
\begin{aligned}
K^*= (&surface, occurrence, namespace, term\_identity, sense, \\
&scope, jurisdiction, registry, version, candidates, \\
&resolution, bindings, standing, aliases, conflicts, \\
&provenance, expiry)
\end{aligned}.
$$

The key identifies a governed lexical candidate under a registry and disambiguation context. It is not the full definition, the referent, the truth of a statement, or a permission to act. Same spelling can resolve to different identities; different spellings can alias one identity; one historical identity can split; and an apparent merge can retain unresolved remainder. Unknown and contested are valid resolver outcomes.

Every consumer must bind registry generation and preserve original surface form, context, candidates, decision basis, and standing so re-resolution is possible. Hashing can commit to canonical bytes after resolution but cannot decide the semantic identity. Cross-person or qualia terms require additional subject, measurement, and bridge records.

The universal GSM can type   
`IDENTIFIES_GTK_RECORD`, `RESOLVES_OCCURRENCE_UNDER_REGISTRY`,  
`ALIASES_LEXICAL_SURFACE`, `SPLITS_TERM_IDENTITY`, `RETURNS_CONTESTED_GTK`,  
`RERESOLVES_AFTER_REGISTRY_CHANGE`, and   
`DOES_NOT_IDENTIFY_REFERENT_BY_HASH`.

This review establishes four editorial commitments: classify the work as the identity-record and resolver companion pending author adjudication; adopt the versioned record; require typed unknown, conflict, split, merge, and expiry; and keep lexical identity below full meaning, reference, truth, authority, and phenomenal identity.

## 12. Failure Modes and Counterevidence

GTK is weakened or refuted in a claimed domain when:

* the applicable concepts do not support stable coordinate assignments at the claimed resolution;
* community or historical disagreement is erased by one canonical registry;
* the sense inventory is circularly defined by the same model used to validate it;
* aliases encode cultural or political hierarchy as neutral identity;
* an invariant floor mistakes a prototype or family resemblance for an essence;
* one-invariant ablation produces nonsensical or ontology-dependent neighbors;
* cross-lingual aliases erase non-equivalent conceptual structure;
* open-world novelty is forced into the nearest existing coordinate;
* context poisoning, prompt injection, or hub gravity redirects binding;
* content-addressed equality is presented as semantic correctness;
* a registry administrator can revise bindings without contest or lineage;
* receipts expose private context or create disproportionate surveillance;
* canonicalization cost exceeds the consequence of the use; or
* ordinary scoped identifiers and typed relations provide the same assurance more simply.

The strongest counterexample is a genuinely contested concept for which no single invariant floor or canonical alias set can be justified without suppressing legitimate plural meanings. A mature GTK system must represent the contest, scope, and authority rather than declaring one party's definition universal.

## 13. Authorial Compression

Several labels in the source may describe profiles of existing machinery rather than independent systems:

* GTK is the RPZ1 bound-term and resolution profile around CSIL coordinates.
* The Constitutional Dictionary may be a GMB lexical projection.
* The GTK lattice may be a typed subgraph or index within Governed Semantic Cartography.
* GTK content addressing is an application of Semantic Hashing and record custody.
* GTK admission is an application of Admissibility Engineering [AE].

The test is differential obligation: retain a separate name only when it introduces a stable contract, operation, evidence burden, or failure mode not already supplied by the compared architecture. A useful profile can deserve a name without being promoted to a foundational primitive or independent system.

The current recommendation is to retain GTK as a distinct lexical interface because it defines the bound-term, alias, competing-binding, and resolution contract. Treat CD as a candidate GMB profile pending author decision. Treat one-invariant adjacency as an optional configured operator rather than part of GTK's universal definition.

## 14. Conformance Questions

A bounded GTK conformance claim should answer:

1. What exact coordinate and registry schemas are used?
2. What belongs to RPZ0, RPZ1, RPZ2, and RPZ3?
3. How are aliases distinguished from mere similarity and translation candidates?
4. How are competing bindings generated, reviewed, and versioned?
5. Which outcomes exist besides forced binding?
6. What authority may create, amend, deprecate, merge, split, or fork a coordinate?
7. How are historical and community-specific definitions preserved?
8. How are hash, semantic-equivalence, and conformance claims separated?
9. How are typed adjacencies justified and challenged?
10. What evidence binds a resolution used for consequential action?
11. How are privacy, purpose limitation, and context minimization enforced?
12. Can the registry and claimed results be cold-booted from exact artifacts?
13. What false-merge, false-split, abstention, drift, and adversarial results are reported?
14. What does the conformance claim explicitly not establish?

Passing such a profile would establish conformance only for the named version, configuration, evidence, and scope. It would not establish universal semantic truth.

## 15. Research Agenda and Open Questions

1. Decide whether this paper and *Global Term Key: Constitutional Lexical Identity Through Disambiguated Semantic Binding* are one version family, companion papers, or distinct works. No merger is presumed here.
2. Confirm GTK as `RPZ1 + D` around a CSIL/RPZ0 coordinate, or revise the coordinate/name boundary.
3. Decide whether the invariant floor is required linked RPZ2 specification, optional profile data, or part of the GTK record itself.
4. Decide whether Constitutional Dictionary is an independent architecture or a lexical GMB profile.
5. Accept typed, lens-relative adjacency as the general rule and one-invariant ablation as an optional configured operator.
6. Define the normative GTK, coordinate, alias, competing-binding, definition, lineage, authority, outcome, and receipt schemas.
7. Define treatment of contested, family-resemblance, multilingual, evolving, and community-specific concepts.
8. Select a low-consequence reference corpus and evaluation protocol only under separate implementation authority.
9. Authorize external primary-source research before novelty, comparative, or Evidence-Readiness claims.

## Lexical Identity Without Semantic Dictatorship

### Public orientation

Global Term Key provides a durable identity for a governed lexical binding so aliases, revisions, competing meanings, and lineage need not collapse into strings or similarity scores. A GTK identifies a declared binding under authority and evidence. It does not make that binding true, universally accepted, complete, or permanent.

### Adversarial tests

1. **Namespace-capture attack.** One issuer controls identities across communities. GTKs require issuer and jurisdiction fields plus federation and fork behavior.
2. **Alias-poisoning attack.** A misleading alias redirects retrieval to the wrong binding. Alias admission needs context, evidence, collision checks, and revocation.
3. **False-unification attack.** Similar definitions are merged despite material differences. Competing bindings and non-identity must remain first-class.
4. **Version-drift attack.** A term's invariant floor changes while the key remains stable. Material semantic change requires a successor or explicit versioned binding, not silent reinterpretation.
5. **Resolver-bias attack.** Frequency, embedding similarity, or institutional preference determines the target. Resolver policy, candidate set, evidence, refusal, and appeal must be visible.
6. **Inaccessible-definition attack.** The key resolves to a source the user cannot inspect. Custody, access, and disclosure gaps must be typed.
7. **Context-collapse attack.** One key is used across jurisdictions where obligations differ. Lexical identity does not imply policy or legal equivalence.
8. **Privacy attack.** A binding exposes sensitive provenance, participants, or suppressed terms. Identity and public visibility require separate authority.

### Claim and evidence ceiling

GTK is an identity and resolution proposal. It does not establish a global registry, universal adoption, semantic uniqueness, ontology completeness, or automatic interoperability. Conformance requires canonical encoding, collision behavior, resolver tests, governance, federation, and recovery evidence.

Internal corpus use demonstrates architectural demand and candidate interfaces. Claims about terminology systems, standards, knowledge graphs, identifiers, or adoption require resolvable external comparison. No external research was added in this pass.

### Reader-facing consequence

The public benefit is that a system can say not only which word appeared, but which governed meaning was intended, who declared it, what alternatives existed, how the choice was made, and how later revisions relate without rewriting history.

## 16. Conclusion

The durable contribution of Global Term Key is the move from ungoverned surface forms to explicit, inspectable bindings. The integrated architecture makes that move without asking one object to do every semantic job.

CSIL/RPZ0 locates a coordinate. GTK/RPZ1 names it, exposes admitted aliases, and keeps competing bindings visible under disambiguation. RPZ2 carries definitions, criteria, and qualifications. RPZ3 carries the typed manifold. GMB preserves the governed records, provenance, standing, and lineage. Semantic hashing binds exact versions but does not certify meaning. Admissibility and receipts govern when a proposed resolution may acquire consequence.

This layering strengthens rather than abandons the source thesis. Polysemy becomes navigable topology; similarity stops masquerading as identity; uncertain or contested resolution can stop lawfully; and semantic revision becomes explicit. The result is not a universal dictionary of final meanings. It is a governed interface through which named meanings can be located, examined, contested, used, and revised without silently transferring authority across a shared word.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that knowledge systems often use a surface word, embedding neighborhood, graph node, URI, or schema type as though it were already a stable semantic identity. Its nearest external comparison fields are semantic, crypto, observation. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. Telemetry can be complete at the instrumented boundary while omitting the causal variable, real-world effect, or authority question that matters. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** Anders Rundgren, Bret Jordan, and Samuel Erdtman. *JSON Canonicalization Scheme (JCS)*. RFC 8785, 2020. https://www.rfc-editor.org/rfc/rfc8785 **Relationship:** Adjacent canonicalization standard relevant to stable cryptographic commitments.

**[E7]** Ben Laurie et al. *Certificate Transparency Version 2.0*. RFC 9162, 2021. https://www.rfc-editor.org/rfc/rfc9162 **Relationship:** Adjacent append-only Merkle-log standard for inclusion and consistency evidence.

#### Source-head external references retained under original labels

**[MILLER]** Miller, George A. 1995. "WordNet: A Lexical Database for English." *Communications of the ACM* 38(11): 39-41. Bibliographic entry retained from the exact author source and not independently verified in this pass.

No external research was conducted in this pass. Current primary-source comparison and a conventional bibliography are required for a future evidence-qualified revision-readiness, novelty, or empirical-improvement claims.

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

**[A4]** Adam Ableman. *Semantic Legitimacy Before Context*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-091E34BA93992CE4`;  
source SHA-256  
`DEB7626CE1AB54F4B541347DCC3C4E14DC4F682230ACCCE1A93D1D536A50C44C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Constitutional Semantic Hashing: Governed Commitment Schemes for Semantic Provenance, Admissibility, and Constitutional Continuity*. Ableman Corpus current edition; work identity `PAPER.PUB.20248734`;  
source SHA-256  
`B1DAC3E2CD4D57BAFBF6462BA6ACFFF7CF120CDB7FA37D0C173525744CC0A2F0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Cryptographic Admissibility and Jurisdiction*. Ableman Corpus current edition; work identity `PAPER.PUB.20602448`;  
source SHA-256  
`6094338D8706F63E8787A5E8DCF40F8A651C0FC3E5EA776DD61791566D094D38`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

#### Ableman Corpus references

**[GTK-SOURCE]** Adam Ableman. *Global Term Key: Identity Primitives in Governed Knowledge Systems*. Exact author source SHA-256  
`4DADDB53C80AB79435E3B634F11B64E70A319991248169B665C18C5AAE03BB1D`; unpublished source revised here as an AI-assisted integrated edition.

**[GTK-COMPANION]** Adam Ableman. *Global Term Key: Constitutional Lexical Identity Through Disambiguated Semantic Binding*. Exact author source SHA-256  
`5F4A36BE1B9CB7DA3A174FCA32AEE74974678D628950F9E2600C647045BD24BB`; distinct local work pending author identity adjudication.

**[GMB-HISTORICAL-SOURCE]** Adam Ableman. *Constitutional/Crystallized Meaning Base (CMB)*. Exact historical-title source SHA-256  
`8680F801CDCA0B4C81F7751A788106454D34923993B4E7BBFF68F35A83ED0DA0`; current terminology is Governed Meaning Base (GMB) under the author-confirmed

`CCF -> CMB -> GMB` lineage.

**[MAB]** Adam Ableman. *Meaning as Binding*. Exact reviewed source SHA-256  
`A9EA6370E77A71A997F1D1CAC18EF6213125C6F3E13BEEBC9F5E8BFB94FE0B45`; separately custodied reviewed source.

**[CBT]** Adam Ableman. *Constitutional Binding Theory: Governed Anchor Resolution as a Universal Pattern in Semantic Systems*. Exact reviewed source SHA-256  
`AD0EF1999F2CD00BFD4128E31D3CE755F746BB7160423C041921875FFF1D2DDC`; separately custodied reviewed source.

**[SLBC]** Adam Ableman. *Semantic Legitimacy Before Context*. Exact reviewed source SHA-256  
`1E9058F212FCB00E42E35E927DF2E7F830BC9C9499AAFF469FE65FF8AE137B68`; separately custodied reviewed source.

**[GSC]** Adam Ableman. *Governed Semantic Cartography*. Exact reviewed source SHA-256  
`EB64EFEA1CCFD1DB7DA65E0989F9372DE3C30E0B974A260554D1FE4A089B1AD3`; separately custodied reviewed source.

**[GST]** Adam Ableman. *Governed Semantic Tokens: Tokenization as an Admissibility Boundary*. Exact reviewed source SHA-256  
`9613BB5E6DD226EF18DA862C7F3BB784B93534A27E2746F5378835AEF76737FF`; supplied Zenodo title match, with publication identity retained separately.

**[SH]** Adam Ableman. 2026. *Semantic Hashing: Hashes as Declared Equivalence Classes of Meaning*. Zenodo. DOI:   
  `10.5281/zenodo.18500533`. Exact reviewed source SHA-256  
`0AD135E1A89CE3EE136F36C703C3A415E1209B02FB16A59182F8E29F69127061`.

**[CSH]** Adam Ableman. *Constitutional Semantic Hashing: Governed Commitment Schemes for Semantic Provenance, Admissibility, and Constitutional Continuity*. Exact reviewed source SHA-256  
`1EA97A14C6966F1FA8CCF587E9A95DA1821C152B801561EFE0A908994184F525`; supplied Zenodo title match, with publication identity retained separately.

**[AE]** Adam Ableman. *Admissibility Engineering*. Exact reviewed source SHA-256  
`FA80D5895A569839958193735B754BE62EE20E1B399A06CB3BA959614DEBF7A3`; separately custodied reviewed source.

**[GCNL]** Adam Ableman. *Governed Controlled Natural Language*. Exact reviewed source SHA-256  
`B0317502B2B10790942DCE3CBFDE58C13E648890AB64A172BB9AE18CA1896D72`; separately custodied reviewed source.

**[GCML]** Adam Ableman. *Governed Controlled Machine Language*. Exact reviewed source SHA-256  
`D4E5D935108BDA55157CADDEAD84B94F14868CEDD5CBF72F5184994983AFFB9A`; separately custodied reviewed source.

**[THR]** Adam Ableman. 2026. *The Three Hash Rule*. Zenodo. DOI:   
  `10.5281/zenodo.20788617`. Exact reviewed source SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.

**[RAZOR]** Adam Ableman. 2026. *Ableman's Razor: A Typed Grammar for Ontology Exploration, Configuration Collapse, and Implementation Feedback*. Zenodo. DOI:   
  `10.5281/zenodo.18113475`. Publication reference retained from the exact source bibliography; no local source identity was inferred.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847760](https://doi.org/10.5281/zenodo.23847760)
