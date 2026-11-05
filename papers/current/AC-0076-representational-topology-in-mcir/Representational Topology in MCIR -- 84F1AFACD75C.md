# Representational Topology in MCIR

## AST, Typed DAG, Receipt Lineage, and Their Governance Obligations

### The comparison is not a contest between two unrelated data structures.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

MCIR representation is constitutional because structure determines which containment, sharing, authority, dependency, transformation, and lineage relations can be expressed and checked. This paper evaluates a specific candidate profile: a scoped tree for human authoring, a typed directed acyclic graph for canonical sharing and dependency, and a separately protected receipt-lineage graph for proposals, decisions, executions, and revisions.

The comparison is not a contest between two unrelated data structures. A tree is a restricted DAG. The relevant differences arise from single-parent containment, reference and sharing law, edge typing, cycle policy, canonical identity, and mutation semantics. An AST does not automatically confer scoped authority or deterministic evaluation; a DAG does not automatically confer provenance, semantic equivalence, or institutional realism. Those properties require explicit law and evidence.

The three-representation profile is promising because it separates local authorial structure, canonical reuse, and historical custody. It also creates new risks: compilation can lose scope or order, shared nodes can widen authority, canonical graph edits can diverge from the authoring source, and mutable lineage can rewrite the explanation of past effects. The architecture is therefore defined through correspondence, ownership, projection, identity, and receipt obligations.

This work is narrower than the adjacent *MCIR Topologies* design-space paper. It develops one candidate configuration and its tests. Whether it remains a standalone companion, becomes a profile within the broader paper, or is integrated into the canonical MCIR work is an author decision; no merger is performed here.

## Source, Evidence, and Authorship Standing

This is an AI-assisted integrated edition derived from one exact source artifact. Its custody manifest is   
`work/paper-saturation-v1/evidence/`

`representational-topology-in-mcir/integration-`  
`custody-manifest.v0.1.json`,  
SHA-256  
`E76F6087891FD8CF987EF6D14E0943A97D2545EFF44186BEC1DBE315BC187033`. The source remains unchanged.

The source carries a title and paper structure but no standard author metadata. Its exact claims are source material; sentence-level human authorship is not inferred. Formal obligations, corpus integration, tests, counterevidence, and decisions added here are AI editorial or synthetic candidates until adopted.

## 1. The Specific Architecture Under Review

The candidate architecture has three representations:

1. **Authoring tree:** a human-legible scoped structure with references.
2. **Canonical typed DAG:** a normalized representation of shared objects, typed dependency, and convergence.
3. **Receipt-lineage graph:** a distinct record of proposals, authority, decisions, transformations, effects, verification, and revision.

These are representations with different authority and mutation rules, not merely three database views. A system must say which claims are authoritative in each layer and how disagreement is resolved.

## 2. AST and DAG Are Related, Not Opposites

A rooted tree is a directed acyclic graph with additional restrictions: one parent for each non-root node, connectedness, and a unique path from the root. An AST adds language-specific node meanings, ordering, and child roles.

The material contrast is therefore:

- **containment-first structure:** single-parent ownership, local order, and nesting;
- **sharing-first structure:** multiple incoming references, explicit dependency, and convergent reuse.

An authoring AST may contain reference nodes whose resolution produces a shared canonical DAG. Conversely, a canonical DAG can be projected into several trees for different audiences. Neither projection is automatically lossless.

## 3. Authoring Tree Obligations

The tree supports local legibility only when its language defines:

- node types and child roles;
- ordering semantics;
- lexical and semantic scope;
- inheritance, override, shadowing, and exception rules;
- reference syntax and resolution;
- authority associated with containment; and
- error and refusal behavior.

Nesting does not itself grant or contain authority. A child node may refer to an external policy, a parent may lack power to override an imported constraint, and apparent local order may not define runtime order. These properties must be declared.

The authoring representation should preserve rationale, annotations, unresolved material, and human-significant order even when those elements do not affect canonical execution identity.

## 4. Canonical Typed DAG Obligations

The canonical graph supports reuse and cross-cutting analysis only when it defines:

- node and edge identity;
- allowed edge types and endpoints;
- multiple-parent semantics;
- cycle prohibition or typed exceptions;
- ownership and revision authority for shared nodes;
- canonical traversal and serialization;
- alias, copy, fork, import, and successor relations;
- dependency impact; and
- obligation propagation.

Typed edges such as `constrains`, `authorizes`, `depends-on`, `escalates-to`,  
and `receipted-by` are not merely labels. Each requires composition and inference rules. For example, authorization should not propagate through every dependency edge, and a `receipted-by` relation does not make the receipt evidence for every claim about the node.

A DAG can make shared substructure explicit. It does not establish semantic equivalence. Canonicalization needs a versioned equivalence and normalization regime whose errors and claim ceiling remain visible.

## 5. Receipt Lineage Must Remain Distinct

The semantic graph describes the current governed structure. Receipt lineage describes how proposals, decisions, transformations, effects, and verifications occurred. Collapsing them risks allowing a current semantic edit to rewrite historical explanation.

The lineage graph should be append-oriented and bind:

- exact input and predecessor identities;
- proposed change and proposer standing;
- authority and admissibility decision;
- transformed artifact identity;
- realized result and effect evidence;
- verification and qualification;
- refusal, partial failure, rollback, and recovery; and
- later supersession without deletion of history.

Lineage edges can point to semantic objects, but semantic mutation must not silently mutate prior receipts.

## 6. Compilation and Correspondence

Let $A$ be the authoring representation, $M$ the canonical graph, and $L$ the receipt lineage. Compilation is:

$$
\Gamma_v(A)=(M,R,W),
$$

where $v$ is the compiler and schema regime, $R$ is the unresolved or refused remainder, and $W$ is a receipt binding source, result, law, and evidence.

At minimum:

1. every authoritative node in $M$ traces to a source construct or an explicitly authorized generated construct;
2. every material source obligation is preserved, refused, or recorded in $R$;
3. canonical identity binds compiler, schema, normalization, and imported dependency versions;
4. the same admitted inputs under the same closed environment produce the same canonical result; and
5. a direct canonical edit either round-trips under a declared law or creates an explicit divergence and new authority surface.

The compiler is part of the constitutional boundary. Its output cannot inherit authority merely because it is deterministic.

## 7. Shared Structure and Blast Radius

Sharing avoids duplication but introduces dependency risk. One policy revision may alter many downstream contexts. A shared node therefore needs an impact query:

$$
Impact(x)=\{y\mid y\leadsto x \text{ through material dependency edges}\}.
$$

The direction and meaning of $\leadsto$ depend on edge type. A complete change procedure identifies affected dependents, their authority domains, compatibility constraints, required re-evaluation, and whether the revision is mutation, successor, fork, or local override.

Without this discipline, canonical reuse can become implicit global authority.

## 8. Affordances and Tradeoffs

- **Property:** primary role  
  **Authoring tree:** legible construction  
  **Canonical typed DAG:** shared governed structure  
  **Receipt lineage graph:** historical custody and evidence

- **Property:** natural strength  
  **Authoring tree:** containment and local order  
  **Canonical typed DAG:** reuse and dependency queries  
  **Receipt lineage graph:** temporal accountability

- **Property:** principal risk  
  **Authoring tree:** duplicated or hidden cross-cutting rules  
  **Canonical typed DAG:** uncontrolled sharing and cognitive load  
  **Receipt lineage graph:** mutable or incomplete history

- **Property:** identity basis  
  **Authoring tree:** source structure plus references  
  **Canonical typed DAG:** versioned canonical graph  
  **Receipt lineage graph:** event/receipt identity and predecessors

- **Property:** mutation posture  
  **Authoring tree:** author revision  
  **Canonical typed DAG:** governed node/edge revision  
  **Receipt lineage graph:** append and supersede

These are biases, not guarantees. Human legibility, correctness, proof tractability, and performance require evidence from actual users and systems.

## 9. Failure and Refusal Semantics

Compilation and projection must distinguish:

- malformed source;
- unresolved reference;
- unauthorized import;
- ambiguous scope;
- illegal or unexpected cycle;
- missing shared-node owner;
- canonicalization conflict;
- obligation loss;
- non-round-trippable canonical edit;
- missing or inconsistent receipt lineage; and
- partial realization.

The safe output is not always a graph. It may be refusal, defer, branch, or an artifact carrying unresolved material with a restricted claim ceiling.

## 10. Corpus Integration and Authorial Compression

The canonical **MCIR** paper defines the representation family this profile serves. **MCIR Topologies** maps the broader design space, including hypergraphs, transition systems, constraints, temporal overlays, and projection strategies. This paper is the narrow profile and proof-obligation companion for the AST/typed-DAG/lineage arrangement.

**Meaning Crystals** supplies representational-stability criteria but does not prove that this profile is stable or correct. **Governed Semantic Project Lineage** supplies successor, custody, and project-history relations beyond the runtime receipt graph. The **Governed Meaning Base (GMB)** can retain topology profiles, identities, projections, evidence, conflicts, and revisions. The universal **GSM** can type their relations while preserving work identity.

The present recommendation is authorial compression, not automatic merger: keep the profile distinct through review, then decide whether it earns a standalone publication or becomes a section/companion of MCIR Topologies or MCIR.

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

- **Possibility:** consider tree, graph, lineage, and alternate representations.
- **Specification:** state the three roles, semantic laws, compiler, identity, mutation, and evidence obligations.
- **CM1:** retain admissible combinations and correspondence regimes.
- **CM2:** prefer configurations by legibility, preservation, reuse, proof, lineage, accessibility, and cost.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for one MCIR domain. The expansions are interchangeable.
- **IR:** produce an **Instance Realization** or **Implementation Realization** with schemas, compiler, stores, editors, and verifiers. The expansions are interchangeable.
- **Evidence:** test determinism, preservation, user comprehension, sharing, impact, lineage, failure, migration, and replay.
- **Revision:** version the schema and compiler, migrate explicitly, and preserve predecessor custody.

This paper reaches Specification and presents one CM1/CM2 candidate. It does not establish a final IC or IR.

## 12. Evaluation Program

The profile should be tested through: (1) nested local scope; (2) imported non-overridable authority; (3) shared-policy revision; (4) multi-parent admissibility; (5) cross-cutting constraint queries; (6) illegal-cycle detection; (7) source-to-canonical traceability; (8) obligation preservation and explicit remainders; (9) deterministic canonicalization; (10) canonical-to-authoring divergence; (11) append-only lineage; (12) partial failure and recovery; (13) schema migration; (14) dependency impact; (15) author comprehension; and (16) auditor reconstruction.

Claims should be property-specific. One successful example cannot establish the architecture as "most complete."

## Three-Graph MCIR Representation Contract

The completed P1 corpus gives Representational Topology in MCIR a sharp role: it is the **three-graph representation contract separating authoring structure, canonical semantic structure, and receipt lineage**. It does not decide the complete MCIR schema, prove that DAGs are universally optimal, or make shared structure safe by default.

- **Adjacent work:** *MCIR Topologies*  
  **Supplies:** The broader topology design space and comparison surface.  
  **This paper's boundary:** This paper isolates the AST-to-DAG-to-receipt separation and its assurance obligations.

- **Adjacent work:** *Water: MCIR as the Engineering of Governed Change*  
  **Supplies:** A wider engineering account of MCIR transformations and governance.  
  **This paper's boundary:** The topology paper supplies one representation contract within that program.

- **Adjacent work:** *The Ableman Format Specification (AFS)*  
  **Supplies:** Format profiles, canonicalization, validators, and conformance claims.  
  **This paper's boundary:** AFS may standardize an MCIR profile; this paper does not establish one by itself.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Governed lowering, semantic remainder, and correspondence obligations.  
  **This paper's boundary:** MCIR topology is a carrier and compiler target, not the whole transformation architecture.

- **Adjacent work:** *Meta-Binding as Operational Invariant*  
  **Supplies:** Obligations that must survive transformations among representations.  
  **This paper's boundary:** Meta-binding states preservation duties; the three graphs expose where they can be tested.

An MCIR representation case should bind:

$$
\begin{aligned}
M= (&source\_artifact, authoring\_AST, canonical\_DAG, \\
&receipt\_graph, schema, canonicalization, correspondence, \\
&evidence, revision)
\end{aligned}.
$$

The **authoring AST** preserves source order, local syntax, comments or annotations where required, and author-facing structure. The **canonical typed DAG** shares resolved semantic objects under explicit identity and equivalence rules. The **receipt graph** records transformations, decisions, evidence, and revisions. A hash of one graph is not the identity of the other two.

Sharing a DAG node widens blast radius. Mutation policy, immutability, versioning, reference counting, cycle refusal, resource bounds, privacy, and access control therefore belong to the representation contract. Deduplication is beneficial only where equivalence is warranted and the downstream obligations of sharing are acceptable.

The universal GSM can type `PARSED_AS_AST`, `LOWERED_TO_CANONICAL_DAG`,  
`RECORDED_IN_RECEIPT_GRAPH`, `CORRESPONDS_UNDER`, `SHARES_NODE_WITH`, `ALIASED_BY`,  
`CYCLE_REFUSED_BY`, `BLAST_RADIUS_INCLUDES`, `CANONICALIZED_UNDER`,  
and `REVISED_TO_GRAPH`. These relations keep topology, identity, and evidence from collapsing.

This integration establishes four editorial commitments: adopt the three-graph contract as the official corpus role; adopt the MCIR representation-case envelope; require graph-specific identities and correspondence evidence; and make shared-node blast radius and mutation policy explicit conformance dimensions.

## Cross-Graph Anchor and Evidence Contract

The fixed-seed comparison with Epistemic IR, Governance Witnesses, the Optional Coordinator, and the GOV source-anchor profile reveals a concrete cross-graph obligation:

$$
\begin{aligned}
A= (&source\_revision, AST\_location, canonical\_subject, \\
&task\_record, receipt\_lineage, correspondence, rebind, \\
&evidence, remainder)
\end{aligned}.
$$

A GOV comment begins at an exact source location normally preserved in the authoring AST. Resolution identifies a canonical task or subject object in the DAG. Work events, decisions, and evidence belong in the separate receipt graph. Moving code, deduplicating nodes, regenerating sources, or revising task identity requires explicit correspondence and rebinding rather than a hash or path being reused across graphs.

Governance Witnesses and Epistemic IR add payload obligations without changing the topology identities. Witness assertions, resolved claim objects, and evaluation receipts can correspond across graphs while retaining different canonicalization, access, privacy, mutation, and evidence rules. A representation profile must state what is intentionally not carried across each edge.

The Optional Coordinator adjacency produces   
`NO_MATERIAL_RELATION`. A tree, DAG, or graph can represent communication and coordination, but representational topology does not establish that a coordinator function is present, necessary, displaced, or successfully substituted.

The universal GSM can type   
`ANCHORS_AST_LOCATION_TO_CANONICAL_SUBJECT`,  
`LINKS_SUBJECT_TO_RECEIPT_LINEAGE`, `REBINDS_AFTER_SOURCE_REVISION`,  
`CARRIES_EPISTEMIC_OBLIGATION_ACROSS_GRAPH`, `LOCATES_WITNESS_ASSERTION`,  
`EMITS_CROSS_GRAPH_REMAINDER`, and   
`HAS_NO_COORDINATOR_OPTIONALITY_EFFECT`.

This randomized review establishes four editorial commitments: adopt the cross-graph anchor contract; prohibit hashes and paths from silently crossing graph identities; require explicit remainder for witness and epistemic payload movement; and record no material relation between representation topology and coordinator optionality.

## Cross-Graph Correspondence and Atomic Change

Five downstream uses confirm the three-graph contract. Epistemic IR specifies which claim and evidence commitments the structures must carry. The DAG theorem proves one closure and acyclicity property for a selected canonical profile. GOORRT governs jurisdiction among representation families. MCIR Topologies generalizes the configuration space. Water projects movement through the graphs without replacing them.

The cross-graph correspondence record is:

$$
\begin{aligned}
G= (&authoring\_AST, canonical\_DAG, receipt\_graph, mappings, \\
&shared\_nodes, authority, transform, \\
&carried\_obligations, authorized\_loss, remainder, \\
&evidence, invalidation, rollback)
\end{aligned}.
$$

Correspondence need not be one-to-one. Several authoring nodes may resolve to one canonical identity; one authoring construct may expand into several canonical nodes; one receipt may cover a transition involving many nodes. The mapping should therefore state cardinality, profile, version, and semantic remainder. A receipt edge remains evidence about a transformation and must not be inserted into the canonical semantic DAG as though it were the governed subject itself.

Shared canonical nodes create blast radius. A change to one identity, schema, or dependency can invalidate many authoring views, compiled projections, receipts, and consumers. Cross-graph changes should be staged atomically at the governance level: prepare mappings and impact analysis, validate the successor graphs, record unresolved dependents, then promote or refuse. Storage-level transactions alone cannot establish semantic atomicity.

The universal GSM can type   
`MAPS_AST_TO_CANONICAL_DAG`, `EXPANDS_ONE_TO_MANY`,  
`COALESCES_MANY_TO_ONE`, `RECEIPTS_GRAPH_TRANSITION_SEPARATELY`, `SHARES_CANONICAL_NODE`,  
`PROPAGATES_TOPOLOGY_INVALIDATION`, `PROMOTES_CROSS_GRAPH_SUCCESSOR`,  
and   
`REFUSES_SEMANTIC_ATOMICITY_CLAIM`.

This reverse-dependency review establishes four editorial commitments: adopt the cardinality-aware correspondence record; keep receipt lineage outside the canonical subject graph; require shared-node blast-radius analysis; and use governed prepare, validate, promote, or refuse semantics for cross-graph change.

## 13. Counterevidence and Failure Modes

The profile should be narrowed or rejected where: (1) AST and DAG are treated as unrelated alternatives; (2) nesting is confused with authority; (3) traversal is confused with evaluation law; (4) sharing is confused with equivalence; (5) dependency edges propagate authorization accidentally; (6) graph cycles are introduced through imports; (7) node ownership is undefined; (8) a shared revision widens authority; (9) canonicalization erases meaningful order; (10) authoring annotations disappear without remainder; (11) generated nodes lack authority; (12) compiler version is not identity-bound; (13) imports change without a new canonical identity; (14) direct canonical edits create a second source of truth; (15) round-trip fidelity is assumed; (16) receipt lineage is mutable; (17) failure and rollback disappear from history; (18) replay omits dependencies; (19) the lineage graph is mistaken for semantic proof; (20) a hash is mistaken for meaning; (21) institutional realism is asserted without evidence; (22) user legibility is assumed; (23) the three representations disagree without a governor; (24) a separate graph adds complexity without measurable benefit; (25) the architecture cannot represent n-ary or temporal semantics required by the domain; (26) GMB inclusion is treated as standing; (27) adjacent works are merged by overlap; or (28) the source's authorship remains unresolved.

## Three Graphs Require One Explicit Correspondence Law

### Public orientation

This paper proposes a human-oriented authoring tree, a canonical typed DAG for shared meaning and dependency, and a separate receipt-lineage graph for historical decisions and effects. The value is not that one data structure is inherently constitutional. It is that containment, sharing, authority, mutation, and historical evidence receive different laws and are reconnected through explicit correspondence.

### Adversarial tests

1. **Nesting-authority attack.** Tree containment is treated as proof that a parent grants, owns, or can override a child's authority.
2. **Sharing-equivalence attack.** Multiple references to a canonical node are treated as semantic agreement or authority inheritance.
3. **Edge-inference attack.** Labels such as depends-on, authorizes, constrains, and receipted-by propagate consequences without declared composition rules.
4. **Direct-canonical-edit attack.** The shared DAG becomes a second authoring source and diverges from human rationale, scope, order, and unresolved material.
5. **Receipt-semantic-collapse attack.** Historical evidence edges enter the governed subject graph and become current meaning or authority.
6. **Blast-radius attack.** A shared-node change silently invalidates many authoring views, compiled artifacts, receipts, and consumers.
7. **Storage-atomicity attack.** A database transaction is reported as semantic atomicity despite incomplete mappings, dependents, obligations, or rollback.
8. **Profile-identity attack.** Overlap with MCIR Topologies or canonical MCIR is used to merge works or infer source authorship without an author decision.

### Claim and evidence ceiling

The paper specifies one candidate three-graph MCIR profile with cardinality-aware correspondence, obligation carriage, remainder, impact analysis, and governed promotion. It does not establish source authorship, standalone work identity, canonical MCIR status, semantic equivalence, lossless round trips, institutional realism, user legibility, or implemented atomicity.

Further evidentiary strengthening requires author adjudication of authorship and relation to MCIR Topologies and canonical MCIR, plus current primary-source research and an exact schema, compiler, negative conformance corpus, usability study, and adversarial change campaign. No external research was added in this pass.

### Reader-facing consequence

The public insight is that the structure people edit, the structure systems share, and the history proving what changed should not be silently treated as the same graph - and every movement among them must expose its loss and authority.

## 15. Conclusion

The constitutional choice is not tree or graph in the abstract. It is how local authorship, shared canonical structure, and historical evidence are divided and then reconnected by explicit law.

A scoped authoring tree can preserve human structure. A typed DAG can support shared identity and dependency analysis. A protected receipt-lineage graph can preserve the history that neither current representation should be allowed to rewrite. The compiler and correspondence contracts are what make the three a governed architecture rather than three inconsistent stores.

This profile is plausible, specific, and testable. It remains a candidate until the author decides its relation to the broader MCIR works and until an implementation demonstrates preservation, usability, and lineage under adversarial change.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of AST and graph semantics, canonicalization, provenance and event sourcing, graph transformation, dependency impact analysis, program representation, and human factors in structured authoring.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Revision.** This stage is outside the present paper's asserted contribution and evidentiary scope.

## Corpus-Wide Reference Positioning

This paper argues that mCIR representation is constitutional because structure determines which containment, sharing, authority, dependency, transformation, and lineage relations can be expressed and checked. Its nearest external comparison fields are formal, provenance, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

DOI: [10.5281/zenodo.23848201](https://doi.org/10.5281/zenodo.23848201)
