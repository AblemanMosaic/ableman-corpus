# Semantic Memory Hierarchies

## The database computes. The archive remembers.

### Hot Databases, Cold Archives, and Governed Movement Between Them

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern software systems commonly flatten all memory roles into a single substrate: the database.

Transactional state, historical records, immutable artifacts, audit trails, search indexes, media metadata, semantic lineage, and long-term archives are frequently treated as equivalent categories of storage merely because they are digitally representable.

The Ottoman architect Mimar Sinan's sixteenth-century hamam (bath-house) designs did not maintain every chamber at maximum thermal intensity simultaneously. Heat was staged, circulated, retained, and transitioned through specialized zones --- a *sicaklik* hot chamber, a *iliklik* warm transitional chamber, and a *sogukluk* cool chamber for rest --- each optimized for different functions in the bather's progression. Semantic Memory Hierarchies apply the same principle to computational memory: databases remain computationally hot, archives remain durable and cool, and governed transitions regulate movement between thermal states. (See Necipoglu 2005 for a comprehensive treatment of Sinan's architectural corpus.)

SMH is a semantic memory architecture that thermally separates computational memory from durable semantic memory, assigns canonical authority to an immutable filesystem-based archive hierarchy, and governs artifact movement between HOT, WARM, COLD, and DEEP tiers via explicit, receipted operations. It does not optimize storage location; it optimizes the role of memory within the system.

In SMH, thermal state refers to the frequency, immediacy, and computational intensity with which artifacts participate in active system operations. SMH separates memory into four governed thermal tiers --- hot computational memory, warm indexed memory, cold canonical archival memory, and deep compressed archival memory --- where databases serve as bounded computational working memory, archives serve as canonical semantic memory, and governed hydration/eviction operations move artifacts between tiers according to access patterns, semantic value, and operational need.

The paper formalizes tiered semantic storage, archive hydration, projection-based filesystem organization, rebuildable indexes, canonical archive authority, and governed storage movement. It also defines the advantage boundary of SMH explicitly: the architecture becomes structurally superior to database-for-everything designs when systems possess significant archival mass, immutable or semi-immutable historical records, auditability requirements, semantic lineage, or cold historical strata that need not remain in active computational memory. Conversely, systems whose data remains almost entirely live, transactional, and actively relational may continue to benefit from database-centric architectures.

SMH therefore does not replace databases.

It restores them to the role they perform best.

---

## 1. Introduction

The relational database became the dominant computational memory substrate of modern software because it solved an important problem:

fast relational computation over structured state.

But over time, databases accumulated responsibilities far beyond this original role.

They became:

* archives,
* historical memory,
* audit substrates,
* semantic lineage stores,
* media indexes,
* legal record repositories,
* and institutional truth engines.

This convergence was convenient.

It was not necessarily optimal.

A modern database often carries:

* decades of cold records,
* massive historical tables,
* immutable artifacts,
* expired operational state,
* and semantically dead historical sediment
  inside the same substrate responsible for active transactional computation.

The result is familiar:

* database bloat,
* degraded hot-path performance,
* expensive migrations,
* fragile monolithic backups,
* operational complexity,
* and increasing epistemic opacity.

The core mistake is subtle:

> not all memory is computational memory.

Some memory exists to:

* prove,
* preserve,
* remember,
* audit,
* reconstruct,
* or survive.

This paper proposes that software systems should structurally distinguish between:

* active computational memory,
  and:
* durable semantic memory.

---

## 2. The Central Doctrine

Semantic Memory Hierarchies rest on four principles:

```
The database computes.
The archive remembers.

Canonical authority lives in the archive.
Computational acceleration lives in the database.

An artifact has one canonical residence
and many navigational addresses.

Time orders memory.
Topic orients memory.
Type audits memory.
Hash proves memory.
```

These principles define a memory hierarchy rather than a storage trick.

The database is not eliminated.

It is thermally specialized.

---

### 2.1 Operational Definitions of Thermal State

Thermal vocabulary recurs throughout this paper. To prevent the metaphor from operating without specification, the following operational definitions apply.

*Thermal state* of an artifact is determined by the conjunction of four measurable properties: *access frequency* (how often the artifact is consulted within a defined window), *access recency* (how recently the last consultation occurred), *mutation rate* (how often the artifact's state changes, with archival artifacts having effectively zero mutation rate), and *computational involvement* (whether the artifact participates in active joins, aggregations, transactional state, or only in retrieval-style access).

The four tiers correspond to bounded regions in this space. *Hot* artifacts exhibit high access frequency, recent access, possible mutation, and active computational involvement. *Warm* artifacts exhibit moderate access frequency, recent-or-near-recent access, low mutation, and primarily retrieval-style involvement. *Cold* artifacts exhibit low access frequency, possibly distant access, zero mutation, and consultation-only involvement. *Deep* artifacts exhibit near-zero access frequency, distant access, zero mutation, and exist primarily for continuity, recovery, or legal preservation.

A constitution governing an SMH deployment specifies the thresholds: what counts as "high" access frequency in this system, what mutation-rate band qualifies as "low," what consultation pattern qualifies as "retrieval-style." The framework does not prescribe canonical thresholds because they depend on the deployment's workload, scale, and operational tempo. The framework prescribes that thresholds *be specified* rather than left implicit, and that artifacts crossing a threshold trigger governed transition between tiers rather than silent drift.

---

## 3. The Four-Tier Semantic Memory Model

SMH separates semantic memory into four governed thermal tiers:

```
HOT    -> active computational memory
WARM   -> indexed nearby archival memory
COLD   -> canonical immutable archive
DEEP   -> compressed/export archival bundles
```

---

### 3.1 Hot Memory

Hot memory is:

* fast,
* transactional,
* mutable,
* bounded,
* relational,
* and computational.

Implemented using:

* SQLite,
* PostgreSQL,
* or equivalent systems.

Hot memory contains:

* active sessions,
* recent operational state,
* working tables,
* temporary hydrations,
* indexes,
* recent artifacts,
* and active semantic computation.

This is where joins happen.
This is where dashboards run.
This is where transactional logic executes.

The database excels here.

But critically:

> the hot tier is bounded.

It is not permitted to become an unbounded civilization-scale archive.

---

### 3.2 Warm Memory

Warm memory bridges active computation and deep archive.

Warm memory consists of:

* recently accessed archive partitions,
* indexed cold artifacts,
* semantically nearby records,
* and high-value retained material.

Warm memory permits:

* rapid retrieval,
* metadata querying,
* and partial semantic access
  without fully hydrating archives into hot computational space.

Warm memory functions similarly to filesystem cache layers, virtual memory paging, or semantic nearline storage. Concrete realizations include Redis or Memcached as recently-loaded archive metadata caches, materialized views or projection tables in the hot database that summarize cold-tier content for rapid query, SQLite or DuckDB instances holding hydrated archive slices, Elasticsearch or Tantivy indexes over cold-tier artifacts, and content-addressed staging directories for recently-fetched archive bundles.

---

### 3.3 Cold Memory

Cold memory is the canonical archive.

Cold memory is:

* immutable,
* hash-verified,
* append-only,
* portable,
* human-legible,
* inspectable,
* and authoritative.

Cold memory lives primarily in filesystem structures.

Example:

```
/archive/canonical/2026/05/17/
  20260517_RetrievalReceipt_sess042_003.csh9ab712.json
```

The filesystem itself becomes partially semantic.

The path encodes:

* chronology,
* artifact class,
* semantic category,
* and partial identity.

Cold memory is not optimized for:

* large relational joins,
* active aggregation,
* or high-frequency mutation.

It is optimized for durability, inspectability, replayability, portability, and semantic continuity. Concrete realizations include POSIX filesystems on local or networked storage, S3-compatible object stores with versioning enabled, IPFS or other content-addressed storage networks, append-only WORM (write-once-read-many) media, and git-style content-hashed repositories. The defining property is not the substrate but the discipline: cold-tier storage commits to immutability, hash-verifiable integrity, and path-based or hash-based addressability that survives independent of the database that may be querying it.

---

### 3.4 Deep Memory

Deep memory contains:

* compressed archive bundles,
* off-site backups,
* export artifacts,
* and long-horizon preservation units.

Deep memory is intentionally operationally distant. It exists not for live interaction, but for continuity, recovery, preservation, and institutional durability. Concrete realizations include LTO tape libraries, AWS Glacier or Azure Archive Storage, optical archive media (M-DISC, archival Blu-ray), offsite encrypted backup vaults, and air-gapped institutional repositories. Retrieval latency is intentionally measured in minutes to hours rather than milliseconds: deep memory's value is its operational distance from active computation, which makes it resilient against the failure modes that affect more accessible tiers.

---

## 4. Governed Movement Between Tiers

Artifacts do not silently move between tiers.

Movement itself is a governed semantic operation.

This is one of the central architectural advances of SMH.

Example:

```
archive query
-> hydrate archive slice into working table
-> compute
-> emit result receipt
-> evict working table
```

This process formalizes:

* archive hydration,
* computational staging,
* and semantic thermal transitions.

Example receipts:

```
ArchiveHydrationReceipt
ArchiveEvictionReceipt
StorageTierTransitionReceipt
```

The movement of semantic memory itself becomes observable.

---

## 5. Projection Discipline

SMH introduces projection discipline:

> An artifact has one canonical residence and many navigational addresses.

Example:

Canonical:

```
/archive/canonical/2026/05/17/
  20260517_CONDEX_claim_sess042_005.cshf3109a.json
```

Projection:

```
/archive/projections/by_topic/ai/grag/
  -> symlink to canonical artifact
```

This distinction matters.

Without it:

* semantic duplication emerges,
* authority ambiguity appears,
* and archives fragment.

The canonical archive remains truth.
Projections remain navigation.

---

## 6. The Advantage Boundary

SMH is not universally superior.

This distinction must remain explicit.

---

### 6.1 Where Database-Only Architectures Win

Database-centric systems remain superior when:

* nearly all records remain hot,
* active relational joins dominate,
* mutation frequency is extremely high,
* transactional consistency is the primary concern,
* and archival mass is minimal.

Examples:

* high-frequency trading engines,
* low-latency telemetry systems,
* live multiplayer synchronization layers,
* short-lived ephemeral state systems.

In such environments,
the archive layer provides little benefit and may introduce unnecessary complexity.

---

### 6.2 Where SMH Becomes Superior

SMH becomes structurally superior when systems possess:

* significant archival mass,
* immutable or semi-immutable historical records,
* semantic lineage,
* audit trails,
* cold historical strata,
* or long-term institutional memory.

Examples:

* email systems,
* legal systems,
* medical records,
* AI semantic archives,
* research systems,
* media libraries,
* governance systems,
* accounting systems,
* compliance archives,
* and semantic operating systems.

In these environments, flattening all memory into a single database creates:

* hot-path degradation,
* database bloat,
* operational opacity,
* and thermal confusion between active state and durable history.

SMH resolves this by thermally separating memory roles.

---

## 7. Why This Improves Performance

The performance advantage of SMH is frequently misunderstood.

The claim is not:

> "filesystems are faster than databases."

The claim is:

> databases perform better when they are allowed to remain computationally hot.

A bounded hot tier:

* stays smaller,
* indexes faster,
* joins faster,
* caches better,
* and avoids carrying cold historical mass unnecessarily.

Cold records remain accessible through:

* hydration,
* warm indexing,
* and projections,
  without permanently burdening the hot tier.

Thus SMH improves performance indirectly by:

* preserving database thermal locality,
* reducing active index mass,
* and externalizing archival burden.

SMH improves performance not by replacing databases, but by preserving computational locality against archival collapse.

The architecture optimizes:

* memory temperature,
  not merely storage location.

---

## 8. Example Deployment

Consider a large-scale email system.

```
HOT
- inbox indexes
- unread state
- active search cache
- current session metadata

WARM
- recent monthly message partitions
- recent attachment metadata
- recently searched archives

COLD
- immutable .eml archive
- canonical attachment filesystem
- historical receipt lineage

DEEP
- yearly compressed bundles
- offsite retention snapshots
- legal preservation exports
```

A user searching old mail does not require every historical message to remain permanently loaded into active relational computation.

Instead:

* the database remains hot and bounded,
* the archive remains durable and canonical,
* and historical partitions hydrate into active computation only when needed.

This distinction scales naturally across:

* legal systems,
* medical archives,
* AI governance systems,
* research environments,
* and semantic operating systems.

---

## 9. Relationship to Existing Architectures

SMH does not claim invention of:

* hierarchical filesystems,
* content-addressed storage,
* database indexes,
* event sourcing,
* append-only archives,
* or semantic file systems.

Rather, SMH contributes thermal semantic memory formalization, governed tier movement, canonical archive authority doctrine, projection discipline, and explicit separation between computational memory and semantic memory.

The novelty is architectural synthesis.

### 9.1 Relationship to the Constitutional Computing Corpus

SMH is one paper in a broader research corpus that develops governance frameworks for computational systems. Several concepts SMH uses --- receipts, governed transitions, canonical authority, projection discipline --- are developed more formally in companion papers, and SMH inherits their architectural commitments rather than redeveloping them.

*Constitutional Storage* (Ableman Ableman 2025c) treats storage itself as a governed admissibility system: occupied state, free state, movement authority, deletion semantics, repair obligations, and emergency reserves are jointly governed under a single constitutional model. SMH composes naturally with Constitutional Storage: the four-tier thermal model can be understood as one possible capacity-jurisdiction structure (in the Constitutional Storage sense) in which hot, warm, cold, and deep are explicitly named jurisdictions with their own admissibility rules. Movement between tiers in SMH is exactly the *governed transition* primitive Constitutional Storage formalizes.

*The Three Hash Rule* (Ableman Ableman, in preparation) develops the receipt framework SMH uses. The *ArchiveHydrationReceipt*, *ArchiveEvictionReceipt*, and *StorageTierTransitionReceipt* artifacts introduced in Section 4 are concrete instances of the role-based receipt typology Three Hash Rule develops: each functions in the receipt role (immutable historical record of the tier transition) and may simultaneously function in the evidence role (constitutional fact consulted by subsequent admissibility decisions about the same artifact's tier eligibility).

*Constitutional Computation* (Ableman Ableman 2025a) defines the foundational governance vocabulary --- canonical authority, admissibility, governed transitions --- that SMH applies to memory hierarchy. The principle *"canonical authority lives in the archive; computational acceleration lives in the database"* (Section 2) is a domain-specific application of the canonical-authority doctrine developed in Constitutional Computation.

*Constitutional Legends* (Ableman Ableman 2025b) develops the jurisdictional projection system that SMH applies to filesystem organization. The principle *"an artifact has one canonical residence and many navigational addresses"* (Section 5) is a direct application of the projection-versus-canonical distinction developed in Constitutional Legends.

*Fractal Governance Architecture* (Ableman Ableman, in preparation) develops the federation-versus-hierarchy distinction that determines how SMH deployments compose across organizational boundaries. A single-organization SMH deployment is a hierarchical constitution: hot, warm, cold, and deep tiers are governed under one constitutional root. A multi-organization SMH deployment (cross-institutional archives, federated medical-records systems, multi-vendor compliance repositories) is a federated constitution: each organization's SMH instance is independently governed, and cross-organization tier movement requires explicit receipt-recognition between the participating constitutions.

SMH does not reproduce these frameworks; it applies them to the memory-hierarchy domain. Readers seeking the formal apparatus underlying the governance primitives invoked here are directed to the companion papers.

---

## 10. Structural Homology with Cognitive Systems

One reason SMH feels natural is that biological cognition already operates similarly.

Human cognition distinguishes:

* active working memory,
* nearby recall,
* long-term memory,
* and deep inaccessible memory.

The brain does not maintain all memories at maximum activation simultaneously.

SMH mirrors this principle computationally.

Hot memory resembles:

* active attention.

Warm memory resembles:

* nearby recall.

Cold memory resembles:

* stable long-term memory.

Deep memory resembles:

* dormant historical preservation.

This is not merely metaphorical.

It reflects a universal constraint:

> systems that remember indefinitely cannot keep everything equally active.

Thermal hierarchy emerges naturally.

---

## 11. Failure of Flat Memory Architectures

Flat database architectures fail gradually rather than catastrophically.

Over time:

* indexes accumulate,
* historical mass expands,
* cold records dominate storage,
* operational queries slow,
* backups become enormous,
* and archival meaning dissolves into monolithic relational sediment.

The database becomes:

* operational engine,
* archive,
* legal memory,
* semantic substrate,
* and institutional history simultaneously.

This thermal collapse is common precisely because databases are so capable.

Their success encourages architectural overloading.

SMH resists this structurally.

---

## 12. Semantic Civilization Infrastructure

The implications extend naturally from enterprise archives toward AI-native semantic systems.

As AI systems increasingly generate:

* semantic artifacts,
* receipts,
* lineage graphs,
* governed outputs,
* and long-term epistemic archives,
  the distinction between:
* computational memory,
  and:
* semantic civilization memory
  becomes increasingly important.

The archive is not merely storage.

It becomes institutional continuity.

This matters for:

* AI governance,
* semantic replay,
* auditability,
* legal memory,
* and long-term epistemic stability.

---

## 13. Conclusion

Databases changed computing because they made active computation tractable.

But active computation is not the same thing as durable memory.

Semantic Memory Hierarchies restore this distinction.

The architecture does not replace databases.

It liberates them from archival overload.

Databases become:

* fast,
* bounded,
* computational,
* and thermally optimized.

Archives become:

* durable,
* inspectable,
* portable,
* canonical,
* and semantically authoritative.

The result is not merely a hybrid storage model.

It is a theory of memory roles inside computational systems.

Hot databases.
Cold archives.
Governed movement between them.

The database computes.

The archive remembers.

---

## Appendix A: Minimal SMH Rule Set

A minimal Semantic Memory Hierarchies constitution should specify:

```
1. Four-tier vocabulary and naming.
2. Thermal threshold definitions (access frequency, recency,
   mutation rate, computational involvement).
3. Canonical-residence rule (every artifact has exactly one
   canonical tier).
4. Projection-versus-canonical distinction.
5. Hot-tier bounding rule (size, mutation rate, or
   computational-involvement cap).
6. Warm-tier admission and eviction rule.
7. Cold-tier immutability and hash-integrity rule.
8. Deep-tier operational-distance rule.
9. Hydration admission rule (cold -> warm or cold -> hot).
10. Eviction admission rule (hot -> warm, warm -> cold).
11. Demotion admission rule (warm -> cold, cold -> deep).
12. Receipt requirements for each tier transition.
13. Reconstruction rule (indexes are derived, not authoritative).
14. Projection authority (canonical artifact is truth;
    projections are navigation only).
15. Cross-constitutional receipt-recognition rule (if multiple
    SMH deployments interoperate).
```

Without these, the system may still store and retrieve artifacts.

It cannot guarantee thermal discipline or canonical authority.

---

## Appendix B: Database-Centric to SMH Translation

| Database-Centric Concept | SMH Translation |
| ------------------------ | --------------- |
| Database as system-of-record | Hot computational tier + cold canonical archive |
| Archive table (cold rows in hot DB) | Cold canonical archive with warm projection |
| Soft delete (logical deletion flag) | Tier demotion with deletion receipt |
| Database backup | Deep memory snapshot |
| Read replica | Warm projection of hot tier |
| Materialized view | Warm-tier projection of cold-tier content |
| Audit log table | Cold-tier receipt lineage |
| Database migration | Schema-aware hot-tier rehydration from cold archive |
| Index | Rebuildable warm-tier projection |
| Database bloat | Thermal collapse: cold mass accumulated in hot tier |
| Archival partition | Cold-tier jurisdiction with hydration receipts |
| WORM table | Cold-tier artifact with constitutional immutability |
| Database compaction | Hot-tier rebalancing plus cold-tier demotion |
| Foreign key to historical record | Reference to cold-tier canonical artifact |
| Stored procedure over archive | Hydrate-compute-emit-evict pattern |

---

## Appendix C: Problem-to-Solution Matrix

- **Problem:** Database bloat from historical accumulation  
  **SMH Solution:** Tier demotion to cold canonical archive  
  **Remaining Cost:** Eviction policy complexity

- **Problem:** Slow joins over mixed hot/cold data  
  **SMH Solution:** Hot-tier bounding + cold hydration on demand  
  **Remaining Cost:** Hydration latency

- **Problem:** Expensive backups of monolithic databases  
  **SMH Solution:** Cold-tier already inherently archivable  
  **Remaining Cost:** Cold-tier custody overhead

- **Problem:** Lost provenance after database migration  
  **SMH Solution:** Cold-tier canonical authority survives migration  
  **Remaining Cost:** Schema-mapping receipts

- **Problem:** Audit-log table overgrowth  
  **SMH Solution:** Receipt lineage in cold tier  
  **Remaining Cost:** Receipt indexing overhead

- **Problem:** Search over cold records is slow  
  **SMH Solution:** Warm-tier projections and indexes  
  **Remaining Cost:** Projection-rebuild cost

- **Problem:** Compliance retention conflicts with operational performance  
  **SMH Solution:** Deep-tier retention with no hot-tier presence  
  **Remaining Cost:** Deep-tier retrieval latency

- **Problem:** Disaster recovery rebuilding hot state  
  **SMH Solution:** Cold tier is the source of truth; hot is reconstructible  
  **Remaining Cost:** Reconstruction time

- **Problem:** Duplicate artifacts across services  
  **SMH Solution:** Canonical residence rule with projection symlinks  
  **Remaining Cost:** Projection-maintenance discipline

- **Problem:** Hot-path degradation under archival load  
  **SMH Solution:** Hot-tier bounding cap  
  **Remaining Cost:** Tier-transition operational cost

- **Problem:** Cross-organization archive interoperability  
  **SMH Solution:** Cross-constitutional receipt recognition  
  **Remaining Cost:** Federation governance overhead

- **Problem:** Schema evolution against historical records  
  **SMH Solution:** Cold-tier canonical artifacts survive schema change  
  **Remaining Cost:** Translation discipline

---

## Corpus-Wide Reference Positioning

This paper argues that modern software systems commonly flatten all memory roles into a single substrate: the database. Its nearest external comparison fields are storage, semantic, software. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Fixity and preservation can keep bytes stable while representation dependencies, executability, interpretation, and institutional custody decay. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. Modularity, secure-development practice, and reproducibility reduce classes of failure but do not guarantee architectural coherence or user sovereignty. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Consultative Committee for Space Data Systems. *Reference Model for an Open Archival Information System (OAIS)*. CCSDS 650.0-M-3, Issue 3, December 2024. https://ccsds.org/Pubs/650x0m3.pdf **Relationship:** Predecessor preservation model for information packages, representation information, and designated communities.

**[E2]** John Kunze et al. *The BagIt File Packaging Format (V1.0)*. RFC 8493, 2018. https://www.rfc-editor.org/rfc/rfc8493 **Relationship:** Adjacent custody and transfer format for payload manifests, fixity, and complete package movement.

**[E3]** Juan Benet. "IPFS - Content Addressed, Versioned, P2P File System." 2014. arXiv:1407.3561. https://arxiv.org/abs/1407.3561 **Relationship:** Predecessor content-addressed network architecture; content identity is compared with, not treated as sufficient for, semantic jurisdiction.

**[E4]** Reproducible Builds Project. *Formal Definition of Reproducible Builds*. [reproducible-builds.org source](https://reproducible-builds.org/docs/formal-definition/) **Relationship:** Adjacent reproducibility practice; byte reproduction is compared with, but not equated to, semantic or constitutional continuity.

**[E5]** Richard Cyganiak, David Wood, and Markus Lanthaler, eds. *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation, 25 February 2014. https://www.w3.org/TR/rdf11-concepts/ **Relationship:** Adjacent graph data model and identity baseline.

**[E6]** Alistair Miles and Sean Bechhofer, eds. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. https://www.w3.org/TR/skos-reference **Relationship:** Adjacent standard for concepts, labels, schemes, notes, and semantic mappings.

**[E7]** W3C OWL Working Group. *OWL 2 Web Ontology Language Document Overview*, Second Edition. W3C Recommendation, 11 December 2012. https://www.w3.org/TR/owl2-overview/ **Relationship:** Adjacent formal ontology standard used to compare declared semantics and inference commitments.

### Ableman corpus

**[A1]** Adam Ableman. *Constitutional Storage*. Ableman Corpus current edition; work identity `PAPER.PUB.20788662`;  
source SHA-256  
`115725C7F7B72C3B720E4EF67F660F329B778D34C4D4232848C6082E849203F7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Cold Boot Continuity as a Deployment Primitive*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-3DB3470715D914D0`;  
source SHA-256  
`4CBB05E90E4ECA37EDA78C0E1FC1FDD180B2D6E0936831B57379AD7124776D4E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Semantic Custody*. Ableman Corpus current edition; work identity `PAPER.PUB.20300952`;  
source SHA-256  
`E3887FE98E6369E39AC3FC2EAC63F2DF7C2AD18AD682B3A745C0CD0AD241D0F0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *From Content-Addressed Storage to Governed Semantic Project Lineage*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F1682AE03F0BA815`;  
source SHA-256  
`5D5D8306514E5FA2C4412D5B468A12681DDCF7002135DC00251A53BF84C79CD6`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *The Implementation Codex*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-872EEF9E301B18DE`;  
source SHA-256  
`1373E9770B5B86EB394BFAF993F5526155D406F4528694B465FDE22A7D525132`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Meaning as Binding*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-5F976917F0B283EA`;  
source SHA-256  
`A470D1A0B9ED7C3CEAB6BB88BE4B642A2BA36427447F787764329FD574DA0C97`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D95CCC4FB7B58BFB`;  
source SHA-256  
`A3B62E50F8BEE125FDAE0D38C2839AFD1CCC138296268BF93217481E38AA48EA`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

### Companion Papers in the Constitutional Computing Research Series

Adam Ableman. 2025a. "Constitutional Computation: Computing Through Authorized Transformation." Constitutional Computing Research Manuscript. https://doi.org/10.5281/zenodo.20624487

Adam Ableman. 2025b. "Constitutional Legends: Jurisdictional Projection Systems for Governed Semantic Participation." Constitutional Computing Research Manuscript. https://doi.org/10.5281/zenodo.20330323

Adam Ableman. 2025c. "Constitutional Storage: Governed Occupancy, Governed Absence, and the Receipted Transitions Between Them." Constitutional Computing Research Manuscript. [DOI to be assigned upon Zenodo deposit.]

Adam Ableman. In preparation. "The Three Hash Rule: Governance Completeness Through Independent Cryptographic Commitments." Manuscript.

Adam Ableman. In preparation. "Fractal Governance Architecture: Constitutional Composability for Federated and Hierarchical Systems." Manuscript.

### Storage Hierarchies and Memory Architectures

McKusick, Marshall Kirk, Joy, William N., Leffler, Samuel J., and Fabry, Robert S. 1984. "A Fast File System for UNIX." *ACM Transactions on Computer Systems* 2(3): 181-197. https://doi.org/10.1145/989.990. Foundational treatment of filesystem layout and free-space management whose cylinder-group locality concept informs SMH's tier-locality discipline.

Rosenblum, Mendel, and Ousterhout, John K. 1992. "The Design and Implementation of a Log-Structured File System." *ACM Transactions on Computer Systems* 10(1): 26-52. https://doi.org/10.1145/146941.146943. Treatment of storage as append-only history with derived current state, an architectural pattern that informs SMH's treatment of cold archives as canonical authority with derived warm-tier projections.

O'Neil, Patrick, Cheng, Edward, Gawlick, Dieter, and O'Neil, Elizabeth. 1996. "The Log-Structured Merge-Tree (LSM-Tree)." *Acta Informatica* 33(4): 351-385. https://doi.org/10.1007/s002360050048. The LSM-tree architecture exemplifies the hot-warm-cold tier separation at the storage-engine level, with SMH generalizing the pattern to the system-architecture level.

Patterson, David A., Gibson, Garth, and Katz, Randy H. 1988. "A Case for Redundant Arrays of Inexpensive Disks (RAID)." *Proceedings of the 1988 ACM SIGMOD International Conference on Management of Data*: 109-116. https://doi.org/10.1145/50202.50214. Hierarchical storage organization for durability and performance that informs SMH's treatment of tier-specific reliability properties.

### Content-Addressed Storage and Append-Only Archives

Benet, Juan. 2014. "IPFS: Content Addressed, Versioned, P2P File System (DRAFT 3)." arXiv:1407.3561. Content-addressed storage architecture relevant to SMH's cold-tier canonical-authority doctrine.

Chacon, Scott, and Straub, Ben. 2014. *Pro Git*, 2nd ed. Apress. https://doi.org/10.1007/978-1-4842-0076-6. Treatment of git's content-addressed object model, an immutable hash-verified archive substrate that exemplifies SMH's cold-tier discipline.

### Cognitive Models of Memory Hierarchy

Atkinson, Richard C., and Shiffrin, Richard M. 1968. "Human Memory: A Proposed System and Its Control Processes." In *The Psychology of Learning and Motivation*, edited by Kenneth W. Spence and Janet T. Spence, 89-195. Academic Press. The multi-store model of memory (sensory, short-term, long-term) that establishes the cognitive precedent SMH's four-tier architecture parallels.

Baddeley, Alan. 2003. "Working Memory: Looking Back and Looking Forward." *Nature Reviews Neuroscience* 4(10): 829-839. https://doi.org/10.1038/nrn1201. Modern treatment of working memory as bounded, active computational substrate, supporting SMH's hot-tier bounding discipline.

Tulving, Endel. 1972. "Episodic and Semantic Memory." In *Organization of Memory*, edited by Endel Tulving and Wayne Donaldson, 381-403. Academic Press. The episodic-semantic distinction in long-term memory that parallels SMH's distinction between historical receipts (episodic) and canonical artifacts (semantic).

### Architectural Precedent for the Hamam Analogy

Necipoglu, Gulru. 2005. *The Age of Sinan: Architectural Culture in the Ottoman Empire*. Princeton University Press. Comprehensive treatment of Mimar Sinan's architectural corpus, including the thermal-zone hamam designs whose principles inform the SMH analogy.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20793071](https://doi.org/10.5281/zenodo.20793071)
