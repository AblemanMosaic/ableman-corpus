# DAG Closure and Acyclicity by Construction in Canonically Referenced MCIR Systems

## Referential Structural Closure Through Immutable Backward Reference

### If every immutable artifact version may reference only strictly earlier immutable versions, then the resulting reference graph is acyclic by construction.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

This note formalizes a precise structural property of canonically referenced MCIR systems. If every immutable artifact version may reference only strictly earlier immutable versions, then the resulting reference graph is acyclic by construction. If admission also checks local schema and every outgoing reference against declared identity, type, scope, authority, and version constraints, then admitted graph state is structurally closed under those checks.

The result is strong but narrower than universal correctness. It does not prove truth, semantic adequacy, policy justice, validator correctness, provenance, replayability, or continued validity after authority revocation or policy change. Canonical identity alone is insufficient if a target can mutate beneath the same identifier. Receipts and content/state bindings are required for custody; revalidation and invalidation propagation are required when governing assumptions change.

This revision preserves the acyclicity proof, replaces the tautological phrase "global correctness" with **referential structural closure**, specifies versioned construction, distinguishes acceptance evidence from truth, integrates the result with constraint-bearing composition, semantic custody, receipts, the Governed Meaning Base (GMB), and the universal GSM, and supplies counterexamples and an evaluation program.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/dag-closure-`

`acyclicity/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`C06628A9024AAA17979CF72F22DA7CDA3ECABA9D9788A744BCB779F51235E4D6`. The exact source remains unchanged. The title spelling correction from

`Constrution` to `Construction` is editorial and does not merge identities.

The construction discipline, theorem, proof, and warrant-by-structure interpretation are author material. The narrowed correctness claim, version discipline, policy-change model, GMB/GSM integration, countertests, and decisions are AI editorial or synthetic contributions until adopted. No implementation or external research was performed.

## 1. Typed Versioned Setup

Let an artifact version be:

$$
v=(id,ver,h,\tau,p,R,L,A,t),
$$

where $id$ is logical identity, $ver$ is immutable version identity, $h$ is content or canonical-state hash, $\tau$ is type, $p$ is payload, $R$ is a finite set of version-bound references, $L$ is applicable law or schema version, $A$ is authority posture, and $t$ is construction rank or receipt time.

A reference must bind   
`(logical identity, version, hash)`, not only a mutable name. Logical identity can persist across revisions; graph edges target immutable versions.

Let $R(v)$ contain the artifact versions referenced by $v$. Version $v$ is **structurally admissible at construction** iff:

1. its local schema is valid under $L$;
2. every target version and hash resolves;
3. every edge type is allowed for the endpoint types;
4. scope, authority, and jurisdiction constraints pass;
5. every target has lower rank than $v$; and
6. the admission act emits a receipt binding input, rules, verdict, artifact version, and resulting graph root.

## 2. Construction Order

Let $\rho:V\rightarrow\mathbb{N}$ assign each admitted version a construction rank. The backward-reference rule is:

$$
\forall v\in V,\ \forall u\in R(v):\ \rho(u)<\rho(v).
$$

Using a natural-number rank provides a strict well-founded order. A timestamp alone is unsafe where clocks collide, reorder, or can be rewritten. A monotone sequence, parent receipt, or comparable admitted rank is required.

Updates create new artifact versions and new edges. In-place mutation of an old version can introduce a cycle or invalidate prior checks without a new construction event, so immutability is required for the theorem as stated rather than merely optional strengthening.

## 3. The Acyclicity Theorem

> **Theorem.** If every reference edge $(v,u)$ satisfies $\rho(u)<\rho(v)$ for a strict order, then $G=(V,E)$ is acyclic.

**Proof.** Assume a directed cycle $v_1\rightarrow v_2\rightarrow\cdots\rightarrow v_n\rightarrow v_1$. The rule gives

$$
\rho(v_2)<\rho(v_1),\ \rho(v_3)<\rho(v_2),\ldots,\rho(v_1)<\rho(v_n).
$$

By transitivity, $\rho(v_1)<\rho(v_1)$, contradicting irreflexivity. Therefore no cycle exists. $\square$

This proof is complete relative to exact edge coverage and enforcement of the rank rule. It says nothing about unrecorded references, runtime call cycles outside the artifact graph, or intentional recursive semantics represented through another layer.

## 4. Referential Structural Closure

Define local structural validity:

$$
\mathrm{LocalOK}(v,L) \wedge \bigwedge_{u\in R(v)}\mathrm{EdgeOK}(v,u,L).
$$

If admission rejects every version failing this predicate, all admitted nodes and recorded edges satisfy the predicate at admission time. Calling that result "global correctness" adds more than the premises prove. The defensible result is:

> **Structural-closure proposition.** For an exact immutable graph built solely through the declared admission function, every admitted node is locally schema-valid and every recorded reference satisfies the edge constraints checked at its construction version.

This is compositional bookkeeping with real value. It is not semantic correctness, truth, completeness, evidence quality, or present-day admissibility.

## 5. What Acyclicity Does and Does Not Establish

A finite version graph with finite references has terminating ancestry traversal. A DAG in the abstract need not have finite ancestry if it is infinite, and acyclicity alone does not establish provenance or replay.

Additional properties require additional contracts:

- **Provenance:** receipts bind producer, authority, inputs, transformation, output, and time.
- **Custody:** content/state hashes bind exact versions and graph roots.
- **Replayability:** transformations and all material inputs are available and deterministic or their uncertainty is declared.
- **Current admissibility:** policy, authority, dependencies, and evidence remain valid or have been revalidated.
- **Semantic correctness:** domain-specific invariants and evidence hold; graph form alone cannot prove them.

## 6. Invalidation and Revalidation

Prior-valid references can become unusable when a law changes, an authority is revoked, evidence is withdrawn, a vulnerability is discovered, or an identity decision is reversed. The immutable historical graph should not be rewritten. Instead, the system emits a typed invalidation, supersession, or standing change and computes affected dependents through reverse reachability.

For changed condition $c$, let:

$$
\mathrm{Affected}(c)=\{v\mid \exists u\in\mathrm{Changed}(c): v\leadsto u\}.
$$

Policy determines whether affected versions remain historical evidence, become unusable for new composition, require revalidation, or trigger replacement. Thus no-global-revalidation is valid only while all governing assumptions remain unchanged and the admission checker was sound.

## 7. Cycles, Recursion, and Layering

Some domains legitimately require mutual recursion, feedback, or strongly connected specifications. A backward-only artifact-dependency graph cannot encode these directly. Options include grouping a recursive component into one admitted unit, using symbolic forward declarations resolved before admission, or representing runtime feedback in a different graph layer.

The theorem applies only to the selected canonical reference relation. It should not be generalized to claim that all cycles are undesirable or absent from the full system.

## 8. Warrant by Structure

Construction can serve as evidence that a named validator accepted a version under named rules at a named time. The strongest safe statement is:

```text
admitted existence proves recorded acceptance under the bound
admission procedure
```

It does not prove that the procedure was correct, complete, current, authorized, or non-bypassable. "Construction is proof" is therefore shorthand whose proof object is the receipt plus the exact validator, law, inputs, artifact version, and graph root.

## 9. Corpus Integration

MCIR supplies the canonical intermediate-representation context, but this note does not decide among disputed MCIR expansions or merge MCIR families. Constraint-Bearing Composability adds the requirement that obligations survive composition. The Three Hash Rule and Semantic Custody bind law, artifact, execution or result state, and lineage. Reasoning by Way of Receipts supplies structured admission evidence. Warrant by Structure supplies the broader proof-by-constructibility thesis.

The **Governed Meaning Base (GMB)** is the current name in the `CCF -> CMB -> GMB` lineage. The universal GSM can represent logical works, immutable versions, hashes, edge types, laws, receipts, invalidations, and revision lineage. Acyclicity is one invariant over a selected relation, not the whole GMB or GSM.

## 10. Realization Funnel

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

- **Possibility:** consider dependency, versioning, recursion, and invalidation strategies.
- **Specification:** define identities, immutable versions, rank, edge types, laws, receipts, and invalidation semantics.
- **Configuration Manifold 1 (CM1):** require exact version binding, backward edges, schema validity, authority, and non-bypassable admission.
- **Configuration Manifold 2 (CM2):** prefer among admissible storage, indexing, receipt, and revalidation designs.
- **IC:** choose an **Instance Constitution** or **Instance Configuration**. The names are interchangeable.
- **IR:** build an **Instance Realization** or **Implementation Realization**. The names are interchangeable.
- **Evidence:** test cycle attempts, mutation, stale law, revocation, deletion, corruption, bypass, replay, and scale.
- **Revision:** add new versions and standing changes without erasing historical graph state.

## Version-Ranked Referential Closure Theorem

The completed P1 corpus gives this paper a narrow technical role: it is the **version-ranked construction and theorem for referential closure and acyclicity in a declared class of canonical MCIR graphs**. It does not establish semantic correctness, absence of recursive meaning, implementation safety, or the superiority of DAGs for every representation.

- **Adjacent work:** *Representational Topology in MCIR: AST, DAG, and Emergent Governance Capabilities*  
  **Supplies:** The three-graph representation contract and topology tradeoffs.  
  **DAG-theorem boundary:** This paper proves one construction property for the canonical DAG layer.

- **Adjacent work:** *Warrant by Structure*  
  **Supplies:** Structural assurance relations and claim ceilings.  
  **DAG-theorem boundary:** Acyclic construction supplies one witness toward a bounded structural claim.

- **Adjacent work:** *The Ableman Format Specification (AFS)*  
  **Supplies:** Profiles, schemas, canonicalization, validators, and vectors.  
  **DAG-theorem boundary:** AFS may make the construction a conformance obligation under an exact profile.

- **Adjacent work:** *Meta-Binding as Operational Invariant*  
  **Supplies:** Obligations preserved across transformations.  
  **DAG-theorem boundary:** Closure says references resolve within the graph; it does not prove the referenced obligations were preserved.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Parsing, lowering, semantic remainder, and correspondence.  
  **DAG-theorem boundary:** The compiler must produce and validate the ranked graph without widening meaning.

A theorem instance should bind:

$$
\begin{aligned}
D= (&schema, version\_order, node\_set, reference\_rule, \\
&construction\_order, closure\_check, cycle\_check, \\
&evidence, standing)
\end{aligned}.
$$

Acyclicity follows only when every admitted edge respects the declared well-founded rank or construction order. Referential closure follows only when every required reference resolves to an admitted node under the exact schema and registry. External references, lazy imports, symbolic recursion, revision edges, receipt lineage, and cross-version mappings require separate layers or rules.

Invalidation and revalidation must propagate through dependents. A graph can remain acyclic while containing stale, unauthorized, contradictory, or semantically defective nodes. Structural warrant therefore stays limited to the theorem's subject and predicates.

The universal GSM can type `RANKED_BEFORE_NODE`, `REFERENCES_ADMITTED_NODE`,  
`CLOSED_UNDER_REFERENCE_RULE`, `ACYCLIC_BY_CONSTRUCTION`, `EXTERNAL_REFERENCE_TO`,  
`RECURSION_REPRESENTED_OUTSIDE_DAG`, `INVALIDATES_DEPENDENT`, `REVALIDATED_UNDER_SCHEMA`,  
and   
`WARRANTED_FOR_STRUCTURE`. These relations isolate the theorem from broader claims.

This integration establishes four editorial commitments: adopt version-ranked referential-closure theorem as the official corpus role; adopt the theorem-instance envelope; enumerate out-of-layer recursion and external-reference cases; and bind structural standing strictly to acyclicity and closure under the named profile.

## Closed Reference Substrate, Not Closed Evidence

The fixed-seed comparison with the Epistemic Lineage Engine, the seventeen-system evidence study, Semantic Field Analysis, and the Governed Meaning Base locates the theorem as one structural service:

$$
\begin{aligned}
D^*= (&profile, schema, registry, version\_rank, nodes, edges, \\
&external\_references, layered\_relations, \\
&closure\_witness, cycle\_witness, invalidation, \\
&revalidation)
\end{aligned}.
$$

The GMB may store entries whose canonical reference layer satisfies this profile. ELE may bind episode artifacts to roots in that layer while keeping ancestry, revision, authority, observation, compensation, and external-effect relations separately typed. Referential closure is relative to the exact registry and admitted external-reference policy.

The software study can package case sources, analysis artifacts, and finding references through a closed graph. SFA can analyze a declared closed projection. Neither use makes source evidence adequate, interpretations correct, field measures valid, or omitted relations nonexistent.

Invalidation must travel from changed or withdrawn nodes into dependent entries, projections, analyses, and case packages. The universal GSM can type   
`IMPLEMENTS_CANONICAL_REFERENCE_LAYER`,  
`HOSTED_IN_GMB_PROFILE`, `ROOTS_LINEAGE_ARTIFACT`, `SUPPORTS_ANALYSIS_PACKAGE`,  
`EXTERNALIZES_NON_DAG_RELATION`, `INVALIDATES_DEPENDENT_PROJECTION`,  
and   
`WITHHOLDS_EVIDENCE_CLOSURE`.

This randomized review establishes four editorial commitments: adopt the expanded structural-service object; profile the DAG as one GMB layer; externalize lineage and recursive relations explicitly; and prohibit graph closure from implying evidence completeness or analytic validity.

## A Property-Scoped Closure Certificate

Three downstream uses confirm the theorem's narrow value. The historical CMB/GMB work may store an entry projection satisfying version-ranked referential closure. Epistemic Lineage Engine may root episode artifacts in that layer while keeping ancestry, authority, observation, and external effects separately typed. MCIR Topologies treats the result as one property of one selected canonical graph profile.

The reusable certificate is:

$$
\begin{aligned}
C^*= (&graph\_generation, schema, registry, node\_set, \\
&edge\_types, rank, construction\_order, \\
&external\_reference\_policy, resolution, layered\_cycles, \\
&proof, witnesses, invalidations, ceiling)
\end{aligned}.
$$

The certificate proves only the declared structural properties under the exact registry and admission rules. Structural closure, semantic completeness, evidence closure, currentness, authorization, consistency, and truth remain different predicates. Symbolic recursion, external references, lazy imports, version succession, and receipt or episode lineage may be lawful in separate layers without falsifying the canonical-DAG result.

Any node, edge, schema, registry, rank, or external-reference-policy change invalidates the affected certificate and propagates revalidation to dependents. A successor may preserve the theorem while changing meaning, authority, or evidence. Consumers should cite the exact graph generation and property set rather than the general paper.

The universal GSM can type   
`CERTIFIES_REFERENTIAL_CLOSURE`,  
`CERTIFIES_ACYCLICITY_UNDER_RANK`, `EXTERNALIZES_RECURSIVE_LAYER`,  
`INVALIDATES_CLOSURE_CERTIFICATE`, `REQUIRES_DEPENDENT_REVALIDATION`,  
and   
`DOES_NOT_PROVE_SEMANTIC_OR_EVIDENCE_CLOSURE`.

This reverse-dependency review establishes four editorial commitments: adopt the property-scoped certificate; separate structural, semantic, evidentiary, and authority closure; require exact generation and external-reference policy; and propagate invalidation and revalidation through every consumer.

## 11. Counterevidence and Failure Modes

The claims fail or narrow where: (1) references target mutable names; (2) old versions mutate; (3) not all edges pass admission; (4) an import path bypasses validation; (5) rank can be forged or reused; (6) forward references are resolved after admission; (7) an edge type permits hidden dependency; (8) deletion leaves unresolved references; (9) validator or schema is defective; (10) policy changes invalidate prior edges; (11) authority is revoked; (12) graph storage is corrupted; (13) receipts bind the wrong version or root; (14) DAG ancestry is infinite; (15) replay depends on missing external state; (16) a valid recursive domain is forced into misleading acyclicity; (17) structural closure is presented as truth; or (18) scale makes reverse-dependency revalidation impractical.

## 12. Evaluation Program

A minimal demonstrator should attempt direct cycles, multi-node cycles, mutable-target swaps, hash mismatches, stale-law admission, authority revocation, bypassed imports, deleted targets, forward references, receipt substitution, recursive-component packaging, and transitive invalidation. It should prove the graph invariant from exported state and compare incremental checks with full recomputation.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Revision.** This stage is outside the present paper's asserted contribution and evidentiary scope.

## 14. Conclusion

Backward references to strictly earlier immutable versions do guarantee acyclicity. Admission-time local and edge checks also give useful structural closure over the exact recorded graph. Those are strong architectural properties precisely because their limits are clear.

They do not make a graph true, semantically complete, permanently admissible, automatically replayable, or immune to policy change. With version immutability, exact identity, receipts, non-bypassable admission, invalidation propagation, and explicit graph layering, the note becomes a rigorous foundation for governed dependency structures rather than an overbroad claim that local validation proves an entire representational universe correct.

## Corpus-Wide Reference Positioning

This paper argues that this note formalizes a precise structural property of canonically referenced MCIR systems. Its nearest external comparison fields are formal, provenance, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

### Public orientation

DAG Closure and Acyclicity by Construction provides a bounded structural result: if every admitted reference edge follows a declared well-founded rank, the resulting versioned reference graph is acyclic. A closure certificate can show that required reference targets are present under a profile. Neither result establishes semantic consistency, evidentiary sufficiency, authority, safety, or correctness.

### Adversarial tests

1. **Hidden-edge attack.** Runtime imports, generated links, aliases, redirects, schemas, environment lookups, or human procedures create dependencies outside the certified edge registry.
2. **Rank-forgery attack.** A malformed, mutable, colliding, or semantically irrelevant rank satisfies the comparison while defeating the intended construction order.
3. **Version-alias attack.** Mutable names, latest pointers, case differences, platform normalization, or successor confusion create cycles or ambiguity outside exact identities.
4. **Recursive-semantics attack.** The graph is structurally acyclic while definitions, obligations, proofs, or interpretations depend circularly on one another.
5. **Closed-falsehood attack.** Every reference resolves and every artifact is false, stale, unauthorized, poisoned, or irrelevant to the dependent claim.
6. **Invalidation-gap attack.** A predecessor changes or is revoked but dependent certificates remain apparently current because propagation is incomplete.
7. **Partial-view attack.** Each subsystem certifies its local DAG while their composition contains cross-boundary cycles or unresolved dependencies.
8. **Theorem-travel attack.** The construction theorem is applied to graphs, edges, or update semantics that do not satisfy its typed assumptions.

### Claim and evidence ceiling

The paper's theorem is conditional on exact node identity, an immutable edge set for the certified snapshot, a well-founded rank, and strict rank decrease on every admitted edge. The closure claim is property- and profile-scoped. It does not prove complete dependency discovery, semantic closure, evidence closure, consistency, correctness, authority, execution safety, or implementation conformance.

Further evidentiary strengthening requires machine-checked fixtures for valid and invalid cases, cross-platform identity tests, hidden-edge and composition tests, invalidation replay, and verification of any external mathematical or systems claims. No implementation or external research was added in this pass.

### Reader-facing consequence

The practical benefit is a certificate saying which exact references were checked, under which edge and rank rules, and which structural property followed - together with an explicit list of the properties that did not.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847631](https://doi.org/10.5281/zenodo.23847631)
