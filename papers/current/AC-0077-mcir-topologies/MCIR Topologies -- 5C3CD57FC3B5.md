# MCIR Topologies

## A Governed Design Space for Legibility, Composition, Execution, Verification, and Evolution

### Without those contracts, a multi-topology architecture can increase semantic drift rather than reduce it.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

The representational topology of an intermediate representation is not a neutral storage choice. It determines which relations are local or shared, which structures can be reused, how scope is expressed, whether cycles are possible, how history is retained, which proofs are tractable, and which changes can be made without silent semantic loss. For MCIR, topology is therefore constitutional.

This paper develops the design space opened by that claim. AST and DAG are not two exhaustive alternatives. A tree is itself a restricted directed acyclic graph, while typing, layering, hyperedges, state-transition semantics, temporal versioning, constraint overlays, and authoring/canonical duality are partly orthogonal dimensions. The paper reorganizes the source taxonomy around a **topology profile** rather than a flat list of competing structures.

The strongest candidate architecture is a coordinated representational family: a scoped tree with references for authoring and local containment; a typed graph for canonical sharing and dependency; a separate receipt-lineage graph for provenance and decision history; and explicit projections into workflow, constraint, temporal, and visualization views. This is a design candidate, not an adjudicated MCIR identity or implementation.

Multiple representations create their own constitutional burden. Each projection must state what it preserves, what it omits, whether round-tripping is permitted, how identity is maintained, and which representation is authoritative for each claim. Without those contracts, a multi-topology architecture can increase semantic drift rather than reduce it.

The result is a specification and evaluation framework for choosing MCIR configurations through CM1 and CM2, selecting an Instance Constitution or Instance Configuration, and eventually producing an Instance Realization or Implementation Realization with evidence. No implementation or canonical standing is asserted.

## Source, Evidence, and Authorship Standing

This is an AI-assisted integrated edition derived from one exact dialogue-shaped source artifact. Its custody manifest is   
`work/paper-saturation-v1/evidence/mcir-`

`topologies/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`F172EDF5FFA065F241FE2A73693D58EC9244EA50D3C76EB2DEBDD8B3515BF46A`. The source remains unchanged.

The artifact begins as a response to prior discussion and does not carry a standard author surface. Exact custody does not establish sentence-level human authorship. Its ideas are retained as source material with provisional authorship; this candidate does not assign author standing to model-generated language. The related `MCIR_AST_DAG.txt` work remains a distinct identity pending author adjudication.

## 1. Specification, Configuration, and Realization

The source makes a valuable separation:

- **Specification** describes the possible representational space and the obligations MCIR must support.
- **Configuration** selects a topology family and its structural affordances.
- **Realization** instantiates schemas, editors, serializers, compilers, stores, runtimes, and verifiers.

The full Ableman realization funnel refines that separation. Specification defines the problem; CM1 retains admissible configurations; CM2 prefers among them; IC selects a bounded configuration; IR realizes it; Evidence tests it; Revision changes it under lineage.

An AST or graph schema is not merely an implementation detail if choosing it changes what can be represented, proven, shared, or governed. Nor is a topology name sufficient as a specification. The configuration must include identity, typing, scoping, mutation, versioning, and projection rules.

## 2. Topology Is Constitutional

Topology allocates semantic power. It decides whether one node may have several parents, whether a relation is first-class, whether local containment outranks shared reference, whether history is mutable, whether concurrency is visible, and whether an invariant can be expressed without external convention.

This produces several constitutional questions:

- Who owns a shared node and who may revise it?
- Does reference import content, authority, obligations, or only identity?
- Which cycles are allowed and which indicate an invalid dependency?
- Is lineage inside the semantic graph or carried by a separate receipt graph?
- Can a projection omit a relation without changing standing?
- Which representation governs when authoring, canonical, execution, and evidence views disagree?

Topology does not itself answer these questions. It determines whether the answers can be stated and checked locally.

## 3. A Topology Profile

Represent an MCIR topology configuration as:

$$
T=(V,E,\tau_V,\tau_E,S,H,Q,L,P,C),
$$

where $V$ is the node set, $E$ relation instances, $\tau_V$ node types, $\tau_E$ relation types, $S$ scope and ownership rules, $H$ sharing and reference rules, $Q$ state-transition semantics, $L$ lineage and version rules, $P$ projection and lowering contracts, and $C$ canonicalization and identity rules.

The tuple makes clear that base graph shape is only one dimension. Two typed DAGs can have different governance because they use different scope, mutation, lineage, or projection laws.

Candidate invariants include:

1. every edge type has declared source, target, authority, and composition semantics;
2. every shared node has ownership and revision rules;
3. every projection declares preserved and omitted obligations;
4. canonical identity binds schema and canonicalization version;
5. lineage cannot be rewritten by semantic mutation; and
6. no execution lowering may silently discard a constraint or refusal.

## 4. Base Structural Families

## 5. Dimensions That Are Not Base Topologies

Several source candidates are better understood as overlays or strategies.

- **Layering** separates authority, admissibility, execution, lineage, and evolution views.
- **Versioning** adds temporal identity and succession to any base structure.
- **Corridors and envelopes** are predicates over states or trajectories, not necessarily graph families.
- **Bimodal authoring/canonical architecture** coordinates two representations through a compiler and correspondence contract.
- **Verification-first** and **evolution-first** describe selection priorities, not shapes.

This reclassification makes the design space compositional. A scoped authoring tree can lower into a typed versioned multigraph with a constraint projection and a separate lineage graph.

## 6. Coordinated Representations

The source's strongest proposal is not one topology but a coordinated family:

1. **authoring representation:** scoped tree with references;
2. **canonical representation:** typed graph supporting sharing and dependency;
3. **receipt-lineage representation:** append-oriented provenance and decision history;
4. **execution projection:** workflow or state-transition semantics where needed;
5. **verification projection:** constraints and proof obligations; and
6. **evolution projection:** versions, migrations, supersession, and constitutional amendment.

The broader corpus currently supports an MCIR candidate centered on AST, DAG, and separate receipt lineage. This paper neither grants that arrangement canonical standing nor replaces it. It explains why such a combination is structurally plausible and what additional contracts it needs.

## 7. Projection and Correspondence Contracts

Let $M$ be the canonical representation and $\pi_i(M)$ a derived view. Each projection needs a contract:

$$
\pi_i:(M,O_i)\mapsto(V_i,R_i),
$$

where $O_i$ is the set of obligations relevant to the view, $V_i$ the projected structure, and $R_i$ an explicit remainder containing omitted, unresolved, or refused material.

For every material predicate $p$ claimed to be preserved:

$$
p(M)\Longleftrightarrow p_i(\pi_i(M))
$$

must either be proved, tested under a declared domain, or left unclaimed. A one-way sound projection may be sufficient; round-trip identity should not be assumed.

If an authoring form compiles to a canonical graph, edits made directly to the canonical form may not be representable in the authoring form. The system must choose among refusal, explicit loss, generated extension, or a new source of authority. Silent reverse projection is unsafe.

## 8. Identity, Mutation, and Shared Structure

Shared nodes create reuse and also blast radius. A revision can affect many dependents. MCIR therefore needs:

- immutable or versioned node identity;
- explicit owner and revision authority;
- dependency impact analysis;
- copy, fork, alias, import, and successor semantics;
- transaction or partial-failure rules;
- cycle policy by edge type; and
- receipts linking proposal, decision, transformed artifact, and result.

Canonical identity must bind the topology schema, type law, ordering and normalization rules, and version. Identical node labels in different topology regimes are not the same canonical object merely because their text matches.

## 9. Configuration Selection

Rather than choosing a topology by taste, evaluate a profile across independent criteria:

| Criterion | Question |
| --- | --- |
| legibility | Can intended users understand local and global structure? |
| expressiveness | Can material relations, scopes, and exceptions be represented? |
| composability | Can governed fragments combine without collision or silent widening? |
| identity | Are sharing, aliasing, versioning, and succession explicit? |
| proof tractability | Which invariants and reachability properties can be checked? |
| execution fidelity | Can lowering preserve obligations and refusal semantics? |
| lineage fidelity | Are decisions and transformations reconstructible? |
| evolvability | Can schemas and policies change without rewriting history? |
| accessibility | Can people inspect and renegotiate the structure? |
| cost | What runtime, storage, authoring, and governance burden is introduced? |

No profile dominates universally. CM2 preference is purpose-relative and must retain tradeoffs rather than collapse them into an unsupported score.

## 10. Corpus Integration

The canonical **MCIR** paper supplies the representation architecture whose topology this work explores. **Representational Topology in MCIR** is an adjacent provisional work focused on AST/DAG capabilities and remains identity-distinct. **Meaning Crystals** supplies a bounded language for representational stability; crystallinity does not select a topology by itself.

**Semantic Manifold Topology** describes semantic neighborhoods and transformations at a different analytical level; geometric adjacency is not the same as MCIR storage topology. **Theory of Semantic Computing Infrastructure** situates MCIR among translation, governance, realization, and evidence layers. The **Governed Meaning Base (GMB)** can catalog topology profiles, schemas, projections, standing, evidence, conflicts, and revision lineage. The universal **GSM** types these relations without merging the works.

## 11. Realization Funnel

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

- **Possibility:** enumerate base structures, overlays, strategies, projections, and combinations.
- **Specification:** define the topology profile, invariants, projection contracts, identity, mutation, and evidence obligations.
- **CM1:** retain every admissible configuration, including costly, overly complex, or undesirable ones.
- **CM2:** prefer configurations by domain-relative legibility, expressiveness, proof, execution, lineage, evolution, accessibility, and cost.
- **IC:** choose an **Instance Constitution** or **Instance Configuration** for a bounded MCIR domain. The names are interchangeable.
- **IR:** produce an **Instance Realization** or **Implementation Realization** such as schemas, editors, compilers, stores, projections, runtimes, or verifiers. The names are interchangeable.
- **Evidence:** test conformance, preservation, round trips, performance, comprehension, adversarial mutation, migration, and replay.
- **Revision:** change the profile through explicit versioning, migration, and successor identity.

This paper reaches Specification and proposes CM1/CM2 criteria. It does not choose a final IC or produce an IR.

## 12. Evaluation Program

Candidate configurations should be evaluated with: (1) representative governance structures; (2) local and cross-cutting authority; (3) shared-policy revision; (4) quorum and n-ary relations; (5) cycles by edge type; (6) concurrent transitions; (7) authoring-to-canonical compilation; (8) projection preservation and remainders; (9) canonicalization determinism; (10) migration across schema versions; (11) lineage reconstruction; (12) obligation carriage into execution; (13) human comprehension and editability; and (14) adversarial malformed, ambiguous, and partially representable inputs.

Results must be reported by property. A configuration can be legible and lossy, expressive and uncheckable, canonical and inaccessible, or provable and too costly.

## MCIR Topology Configuration Grammar

Across the completed P1 corpus, MCIR Topologies is the **configuration grammar and design-space companion for selecting, coordinating, projecting, and evolving MCIR structural families**. It does not establish the canonical MCIR identity, merge adjacent MCIR papers, or choose one universally optimal topology.

- **Adjacent work:** *Representational Topology in MCIR: AST, DAG, and Emergent Governance Capabilities*  
  **Supplies:** Focused three-graph AST, canonical DAG, and receipt-lineage contract.  
  **Topology-paper boundary:** MCIR Topologies generalizes the configuration space and correspondence obligations.

- **Adjacent work:** *DAG Closure and Acyclicity by Constrution*  
  **Supplies:** A bounded construction theorem for referential closure and acyclicity.  
  **Topology-paper boundary:** That theorem covers one property of one selected canonical graph profile.

- **Adjacent work:** *Meaning Crystals*  
  **Supplies:** Representational stability, defects, canonicalization, and reopening.  
  **Topology-paper boundary:** Crystallinity evaluates a representation profile but does not select its topology.

- **Adjacent work:** *Theory of Semantic Computing Infrastructure*  
  **Supplies:** Placement among authoring, transformation, storage, execution, and evidence layers.  
  **Topology-paper boundary:** The topology grammar configures one representation layer inside that infrastructure.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Lowering, preservation, remainder, refusal, and receipts.  
  **Topology-paper boundary:** Compilation governs movement among coordinated representations.

A topology configuration should bind:

$$
\begin{aligned}
T= (&base\_structures, node\_types, edge\_types, scope, \\
&sharing, cycles, state, identity, mutation, lineage, \\
&projections, canonicalization, authority, evidence)
\end{aligned}.
$$

Tree, DAG, general graph, hypergraph, state machine, workflow, and constraint network are not interchangeable labels. Layering, versioning, corridors, verification-first design, and bimodal authoring/canonical architecture are overlays or priorities rather than base shapes. Every coordinated representation requires a directional correspondence contract and explicit remainder.

Shared structure creates governance obligations: owner, revision authority, dependency impact, alias, import, copy, fork, successor, transaction, and cycle policy. Direct edits to derived views must either be refused, translated through an authorized source, or create a new governed source; silent reverse projection creates competing authorities.

The universal GSM can type   
`CONFIGURES_MCIR_TOPOLOGY`, `USES_BASE_STRUCTURE`,  
`OVERLAYS_VERSIONING`, `PROJECTS_TO_EXECUTION_VIEW`, `PRESERVES_OBLIGATION_IN_VIEW`,  
`EMITS_PROJECTION_REMAINDER`, `SHARES_NODE_UNDER_AUTHORITY`, `INVALIDATES_DEPENDENT_NODE`,  
`FORKS_SHARED_STRUCTURE`,  
and   
`REMAINS_IDENTITY_DISTINCT_FROM_MCIR_WORK`. These relations keep configuration exploration from becoming identity adjudication.

This integration establishes four editorial commitments: classify the work as the MCIR topology configuration grammar; adopt the complete topology envelope; require directional projection, remainder, and shared-node governance contracts; and preserve adjacent MCIR identities until explicit author adjudication.

## Governed Topology Migration

The fixed-seed comparison with UGK, ESA/GKL, and *Everything Is a Compiler* reveals that topology selection and topology migration need an explicit transition contract. A topology is not only a static configuration when changing it can alter identity, authority, scope, reachability, conflict visibility, or dependency behavior.

$$
\begin{aligned}
M= (&source\_topology, target\_topology, authority, \\
&preservation, authorized\_loss, remainder, \\
&dependency\_impact, evidence, rollback)
\end{aligned}.
$$

UGK supplies one possible accountable transaction pattern for committing such a migration, but MCIR Topologies does not require UGK as its only governance realization. The essential obligation is that the actor, authority, selected source and target, preservation profile, accepted loss, affected dependents, and recovery path are fixed before an authority-relevant migration takes effect.

ESA/GKL supplies a current and historical view of which topology version, conflicts, dependencies, and unresolved remainders are operative. That view can be stale or incomplete, so it constrains the claim ceiling rather than certifying the migration. A topology change that cannot enumerate or bound affected dependents should yield `IMPACT_UNKNOWN`,  
`DEFER`, or a scoped experimental branch rather than silent global replacement.

The compiler lens applies when the migration declares an input regime, target regime, preservation obligations, loss policy, remainder, and evidence. Not every graph edit earns that description. A direct mutation with no declared preservation contract remains an edit; calling it compilation must not manufacture assurance.

The universal GSM can type   
`PROPOSES_TOPOLOGY_MIGRATION`,  
`COMMITS_MIGRATION_UNDER_AUTHORITY`, `PRESERVES_RELATION_ACROSS_TOPOLOGY`,  
`AUTHORIZES_TOPOLOGY_LOSS`, `REPORTS_DEPENDENCY_IMPACT_UNKNOWN`,  
`ROLLS_BACK_TOPOLOGY_MIGRATION`, and   
`QUALIFIES_AS_COMPILATION_UNDER_PROFILE`.

This randomized review adds three open editorial questions: adopt the topology-migration contract; require pre-effect authority, impact, remainder, and rollback custody for consequential migrations; and reserve compiler language for migrations with explicit preservation and loss obligations.

## A Representation-Role and View-Authority Contract

Nine downstream uses confirm that *MCIR Topologies* functions as a configuration grammar rather than a competing foundational representation. Crystallized Governance and Representational Topology select artifact profiles from it. HLIR and GOV use topology to connect authoring locations to canonical subjects. Governance Witnesses separates assertion, identity, and evaluation across authoring, canonical, and receipt graphs. MDSP packages topology choices as versioned standards profiles. ESA/GKL and *Everything Is a Compiler* make observation and comparison relative to the selected topology. UGK binds the representation regime used by an authority-bearing transaction without making that representation the Governor.

Those uses require a role and authority matrix in addition to a list of graph shapes:

$$
\begin{aligned}
T^*= (&representations, roles, claim\_authority, identities, \\
&translations, preservation, authorized\_loss, remainder, \\
&shared\_nodes, dependencies, migration, compatibility, \\
&evidence, revision)
\end{aligned}.
$$

For each claim class, the profile must state which representation is authoring source, canonical subject, executable projection, evidence carrier, or read-only view; which edits are authoritative; and how disagreement is resolved. No representation is globally canonical merely because it is machine-normalized. A graph used to organize witnesses, tasks, or coordination evidence does not prove witness independence, coordinator substitution, or semantic correctness.

Every downstream package should bind the topology schema and canonicalization version it assumes. A topology migration invalidates or qualifies dependent parsers, standards profiles, witnesses, orientation projections, comparisons, and transactions until their preservation obligations are re-established. Compatibility is directional and property-specific; successful parsing is not semantic or authority compatibility.

The broader alias screen found two nondependencies that should remain explicit. Split-Authority AI Coordination uses "authority topology" in a different analytical sense. *The Optional Coordinator* states that MCIR graph shape has   
`NO_MATERIAL_RELATION` to whether coordinator functions were successfully substituted.

The universal GSM can type   
`ASSIGNS_REPRESENTATION_ROLE`, `GOVERNS_CLAIM_IN_VIEW`,  
`TRANSLATES_UNDER_PRESERVATION_PROFILE`, `INVALIDATES_TOPOLOGY_DEPENDENT`,  
`DECLARES_DIRECTIONAL_COMPATIBILITY`, `BINDS_TRANSACTION_TO_REPRESENTATION_REGIME`,  
and   
`HAS_NO_SUBSTITUTION_RESULT_FROM_GRAPH_SHAPE`.

This reverse-dependency review establishes four editorial commitments: adopt the view-authority matrix; bind downstream claims to exact topology profiles; propagate topology migration to every dependent contract; and preserve explicit nonrelations where graph language does not supply substantive evidence.

## 13. Counterevidence and Failure Modes

The proposal should be narrowed or rejected where: (1) AST and DAG are treated as disjoint categories even though a tree is a restricted DAG; (2) a general graph is called a DAG despite cycles; (3) typing is assumed to supply authority; (4) a topology name substitutes for exact semantics; (5) hyperedges and reified relations are treated as equivalent without proof; (6) Petri nets, workflows, state machines, and statecharts are conflated; (7) a constraint overlay is mistaken for complete operational semantics; (8) corridor or envelope language lacks a state and trajectory definition; (9) versioning rewrites historical identity; (10) shared-node changes silently affect dependents; (11) imports widen authority; (12) alias, copy, fork, and successor are conflated; (13) projection drops an obligation; (14) a remainder is hidden; (15) round-tripping is assumed; (16) direct edits create two authorities; (17) canonicalization omits topology or schema version; (18) receipt lineage is mutable with semantic content; (19) cycles create unbounded authorization or dependency; (20) layering produces inconsistent views; (21) multi-topology synchronization cannot be proven or observed; (22) proof tractability is asserted without a logic and domain; (23) user comprehension is assumed; (24) one profile is described as universally optimal; (25) the current MCIR candidate is treated as author-adjudicated; (26) dialogue-derived text receives author standing; (27) adjacent MCIR works are merged by subject similarity; (28) the implementation cannot preserve refusal; or (29) external technical claims remain unverified.

## Multiple Views Need One Explicit Authority Contract

### Public orientation

MCIR Topologies treats representation shape as a constitutional configuration choice. Trees, typed graphs, hyperedges, constraints, workflows, state transitions, temporal versions, receipts, and visualizations expose different relations and proof surfaces. A coordinated family may be useful only when each view declares its role, identity rules, preserved properties, omissions, and authority.

### Adversarial tests

1. **Topology-label attack.** Calling a structure an AST, DAG, graph, or hypergraph substitutes for exact typing, scope, identity, mutation, cycle, and traversal semantics.
2. **View-authority attack.** Two projections disagree and each consumer assumes its own representation is authoritative.
3. **Round-trip attack.** Authoring and canonical views silently lose ordering, sharing, comments, constraints, provenance, defaults, or ambiguity during conversion.
4. **Shared-mutation attack.** One referenced node changes meaning for multiple parents without visible impact review and authorization.
5. **Cycle-by-projection attack.** Each base structure is acyclic while references, versions, imports, constraints, or view correspondences create effective cycles.
6. **Identity-alias attack.** Copying, interning, canonicalization, and reference reuse conflate structural equality, semantic identity, and artifact identity.
7. **Proof-transfer attack.** A property established in one representation is assumed to hold in another without a preservation theorem or test.
8. **Complexity-burden attack.** Coordinated representations create more synchronization, migration, tooling, performance, and human-comprehension risk than they resolve.

### Claim and evidence ceiling

The paper offers a topology-profile grammar and candidate coordinated representation family. It does not adjudicate MCIR identity, choose a canonical topology, establish lossless projections, prove round-trip correctness, or provide an implementation, performance result, conformance suite, or usability result. The dialogue-shaped source has provisional sentence-level authorship, and the related AST/DAG work remains distinct pending author decision.

Evaluation requires exact schemas and semantics, property-specific correspondence contracts, counterexample fixtures, mutation and version tests, migration and round-trip courts, performance and comprehension evidence, and current external research. No implementation or external research was performed in this pass.

### Reader-facing consequence

The key design question is not tree or graph. It is which view answers which question, what semantic power that view possesses, what every conversion preserves or loses, and how a disagreement is resolved without silently rewriting meaning.

## 15. Conclusion

MCIR topology is not a contest between AST and DAG. It is a governed selection across base structures, relation types, scope, sharing, transition semantics, lineage, canonicalization, and projections. Different representations can serve authoring, canonical analysis, execution, verification, and evolution, but their correspondence must itself be constitutional.

The most promising architecture is layered and bimodal: locally legible authoring, explicitly typed canonical sharing, separately protected receipt lineage, and purpose-specific execution and verification projections. Its value remains a hypothesis until schemas, preservation obligations, conformance tests, and human-use evidence exist.

Topology determines what the system can see and preserve. Governance determines which of those structures may bind, transform, and produce effects. MCIR requires both.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of abstract syntax trees, directed acyclic and multi-graphs, hypergraphs, Petri nets, state machines and statecharts, constraint systems, graph transformation, canonicalization, and representation-preserving compilation.

## Corpus-Wide Reference Positioning

This paper argues that the representational topology of an intermediate representation is not a neutral storage choice. Its nearest external comparison fields are formal, provenance, open sovereign. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Source availability and reproducible builds improve inspectability but do not alone guarantee comprehensibility, practical exit, hardware control, or sustainable maintenance. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E2]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E3]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

**[E4]** Leslie Lamport. *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Addison-Wesley, 2002. https://lamport.azurewebsites.net/tla/book.html **Relationship:** Predecessor specification discipline for state machines, safety, liveness, and refinement.

**[E5]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E6]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E7]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

### Ableman corpus

**[A1]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Ableman Corpus current edition; work identity `PAPER.PUB.21095303`;  
source SHA-256  
`EA129ECBA95F7B07CAA7B33A54F91F52913C94A14DA227EB9A06CFD083E4E5BF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Governed Semantic Compilation*. Ableman Corpus current edition; work identity `PAPER.PUB.18453681`;  
source SHA-256  
`5FF6C636550B04DB0E2F6F94C379BB75AA0BD8781E19B047D7D3BB6D49071AC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Hybrid Semantic Compiler Architectures*. Ableman Corpus current edition; work identity `PAPER.PUB.21228038`;  
source SHA-256  
`EBCD6DDDA9B547639AEBED79FB68069473CF1248E41C527B48C9624BBE2C0496`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Admissibility Engineering*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F1E33B5E973B0900`;  
source SHA-256  
`CDC80271268802CA5CB4DE3624B992FB2FF07D677BF945C4B349BD307C4C2A6E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Everything Is a Compiler*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-30FB8F95BD990A47`;  
source SHA-256  
`FE0F88A1F125317285BE4378E5F27ACC9FEB83ADE3FF329A3DA9F9CB026DF9A9`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

A tree privileges containment, parenthood, local scope, ordered authorship, and readable nesting. References permit shared definitions without making the authoring surface a general graph. This is strong for human construction but requires rules for reference resolution, imported authority, cycles, and shared-node change.

### 4.2 Typed directed graph

A typed graph makes relations such as `constrains`, `authorizes`, `depends-on`,  
`escalates-to`,  
and `receipted-by` explicit. A DAG forbids directed cycles; a general directed multigraph may retain several typed edges between the same nodes and allow selected cycles. The choice must follow semantics, not convenience.

### 4.3 Hypergraph or reified n-ary relation

Quorum, joint authority, multi-condition admissibility, and composite obligation may be n-ary. A hypergraph represents this directly. An ordinary graph can instead reify the relation as a node. The two encodings are not automatically equivalent: identity, order, multiplicity, authority, and projection behavior require a declared correspondence.

### 4.4 State-transition structures

Petri-net-like models, state machines, and statecharts privilege transition, concurrency, synchronization, nesting, guards, and reachability. They are useful projections for workflow and lifecycle domains. They should not be described as interchangeable without exact semantics.

### 4.5 Constraint structures

Constraint networks privilege variables, admissibility predicates, satisfiability, conflicts, and allowable regions. They can support static analysis and scenario search. A solver result is only as meaningful as the encoded variables, domain, and constraint law.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847999](https://doi.org/10.5281/zenodo.23847999)
