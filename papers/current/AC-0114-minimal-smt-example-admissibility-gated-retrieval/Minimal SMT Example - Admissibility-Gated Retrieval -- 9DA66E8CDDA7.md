# Minimal SMT Example: Admissibility-Gated Retrieval

## Node Admission, Edge Admission, and Path Participation

### When the transition evidence is absent, the system returns CONTINUITY UNKNOWN rather than projecting continuity or fabricating a preferred interpretation.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Semantic similarity can retrieve two nearly identical artifacts without establishing that one continues, supersedes, rebinds, or inherits authority from the other. This technical companion gives a minimal Semantic Manifold Topology (SMT) example in which two documents are individually admitted under different policy versions but no admissible continuity edge connects them.

The result is not that the second document is necessarily inadmissible. It is that retrieval, node admission, continuity, and participation in a governed traversal are separate judgments. Similarity proposes candidates; a versioned schema evaluates nodes, relations, and paths. When the transition evidence is absent, the system returns `CONTINUITY_UNKNOWN` rather than projecting continuity or fabricating a preferred interpretation.

The example is hypothetical. It specifies expected semantics and tests, not an implemented retrieval result.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact source file. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/minimal-smt-`

`admissibility-gated-retrieval/integration-`  
`custody-manifest.v0.1.json`,  
SHA-256  
`247EB1F9B1EAE249EAB6276F2318FB30FCB28AFF4C96F7CE31E334E46FEF6E0D`. The source remains unchanged.

The source's minimal example and core distinctions are retained. Its conversational/editorial passages and unrelated environment-specific framing are excluded from semantic integration. The 0.997 similarity value is illustrative, not a measured result.

## 1. SMT in This Paper

SMT means **Semantic Manifold Topology**, not satisfiability modulo theories. The method represents semantic objects, perspectives, typed relations, admissibility conditions, and governed transformations. This minimal example needs only a typed graph; it does not claim that the graph satisfies the stronger mathematical conditions of a manifold.

## 2. Scenario

An index retrieves two hypothetical records:

### Document A

```json
{
  "document_id": "A",
  "lane": "governor",
  "authority_ref": "policy_v1",
  "grounding_posture": "grounded",
  "node_admission": "admitted"
}
```

### Document B

```json
{
  "document_id": "B",
  "lane": "governor",
  "authority_ref": "policy_v2",
  "grounding_posture": "grounded",
  "node_admission": "admitted"
}
```

The retrieval layer reports an illustrative cosine similarity:

```text
similarity(A, B) = 0.997
```

The system has no bound transition contract, rebinding receipt, continuity declaration, or verified inheritance rule between `policy_v1` and

`policy_v2`.

## 3. Four Distinct Judgments

**Retrieval** asks whether an artifact is a useful candidate for inspection.

**Node admission** asks whether an artifact may enter the governed working set under its own source, authority, standing, and scope.

**Edge admission** asks whether a proposed relation between artifacts is supported and permitted.

**Path participation** asks whether a node may contribute through a particular traversal, reasoning path, or answer under the admitted relations and task.

Retrieval is neither admission nor participation. Node admission does not imply every proposed edge from that node is admitted.

## 4. Proposed Continuity Edge

Let:

$$
e=(A,continues\_as,B).
$$

Continuity evaluation uses a schema $\Sigma$ and evidence set $W$:

$$
J_e(e,W,\Sigma)\in\{ADMITTED,REFUSED,CONFLICTED,INSUFFICIENT,UNKNOWN\}.
$$

For this example, the schema requires:

- identity or version-family relation;
- authority-transition rule;
- valid rebinding or inheritance evidence;
- scope and time compatibility;
- semantic transformation or continuity declaration;
- no unresolved revocation or conflict.

Because those elements are absent, the result is:

```text
node(A) = ADMITTED under policy_v1
node(B) = ADMITTED under policy_v2
edge(A continues_as B) = INSUFFICIENT
continuity(A, B) = NOT_ESTABLISHED
```

`REFUSED` would require a schema rule or evidence that prohibits the edge.

`UNKNOWN` is appropriate when the evaluator cannot determine whether required evidence exists or is accessible. The worked case uses `INSUFFICIENT` because the stipulated witness basis is known to omit the required transition artifacts.

## 5. Similarity as Candidate Generation

Similarity is not irrelevant. It is useful for discovery, clustering, deduplication leads, and proposing relations. Its claim ceiling is lower than continuity:

$$
HighSimilarity(A,B)\nRightarrow Continuity(A,B).
$$

Near-identical text can occur across revoked policy, copied artifacts, adversarial substitution, separate authorities, incompatible epochs, or independent derivation. Conversely, a legitimate revision may have low lexical or embedding similarity.

The system should retain the similarity relation while refusing to promote it into identity, continuity, equivalence, supersession, or authority inheritance.

## 6. Path Participation

For a query $q$ and traversal path $p$, define:

$$
\begin{aligned}
&Participates(B,p,q)=Retrieved(B,q) \\
&\land NodeAdmitted(B) \\
&\land PathAdmitted(p,q)
\end{aligned}.
$$

If $p$ depends on the unestablished edge $A\rightarrow B$, then B cannot participate **as A's continuation**. B may still participate independently under `policy_v2` if the query, authority, scope, and other path edges allow it.

This is the important restraint: the system does not discard a useful artifact merely because one relation failed, and it does not use the artifact through a relation that lacks standing.

## 7. Interpretation Unknown

`INTERPRETATION_UNKNOWN` is a first-class disposition when several readings are plausible but the available evidence cannot authorize one. It records:

```text
candidate interpretations
evidence considered
missing or conflicted requirements
schema and authority used
allowed bounded uses
blocked projections
next evidence that could resolve the state
```

Unknown is not a failure to reason. It is a result of reasoning under an evidence ceiling. It must not become a permanent excuse: the system should identify whether new observation, author decision, authority resolution, or source recovery could reduce the uncertainty.

## 8. Minimal Evaluation Procedure

```text
1. retrieve candidates by declared retrieval methods
2. preserve retrieval scores and model/version metadata
3. resolve exact artifact and source custody
4. evaluate each node under its own standing
5. propose typed edges rather than infer them silently
6. evaluate each required edge under a versioned schema
7. evaluate the complete task path
8. admit, qualify, refuse, defer, conflict, or preserve unknown
9. emit an evaluation receipt with basis and claim ceiling
```

Pseudocode:

```text
candidates = retrieve(query)
nodes = evaluate_nodes(candidates, schema, time)
edges = propose_edges(nodes, query)
edge_results = evaluate_edges(edges, evidence, schema, time)
path = build_path(nodes, edge_results, query)

if path.required_edge in {INSUFFICIENT, UNKNOWN, CONFLICTED, REFUSED}:
    return bounded_result(path, blocked_relation, next_evidence)
return participate(path)
```

## 9. Relation to the Corpus

*Semantic Manifold Topology - Worked Example* supplies the broader method. *Retrieval-Augmented Reasoning under Constitutional Constraints* separates candidate retrieval from governed reasoning. *Reasoning by Way of Receipts* constrains what the transition records can support. *Governed Context and Memory* governs which retrieved artifacts enter active context.

The Governed Meaning Base can store exact nodes, candidate similarities, typed edge proposals, evaluations, receipts, conflicts, and unknowns. It must not convert stored proximity into identity. These interfaces do not merge the papers or transfer standing.

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

- **Possibility:** enumerate retrieval candidates and possible relations.
- **Specification:** define node, edge, path, evidence, and outcome semantics.
- **CM1:** retain admissible interpretations, including wrong, weak, harmful, and unknown paths.
- **CM2:** select preferable retrieval and evaluation profiles under accuracy, latency, provenance, and restraint criteria.
- **IC:** select an Instance Constitution or Instance Configuration for a corpus and query class.
- **IR:** construct its Instance Realization or Implementation Realization.
- **Evidence:** run fixtures and adversarial retrieval/evaluation tests.
- **Revision:** update schemas, edges, standings, and examples without rewriting source custody.

This technical companion supplies a worked Specification and candidate test fixture. It does not implement an IC or IR. Realization-stage IR remains distinct from Intermediate Representation in MCIR and retrieval compiler contexts.

## 11. Test Matrix

Tests should cover: identical content under different authority; different content under valid continuity; expired policy; revoked policy; missing transition record; invalid rebinding; conflicting continuity declarations; copied artifact with new identity; same identity with changed hash; low similarity with valid lineage; high similarity with independent derivation; inaccessible evidence; malformed receipts; stale evaluation time; node admitted but edge refused; edge admitted but path blocked; artifact independently usable; and unknown later resolved by new evidence.

## Retrieval-Admission Microcase

The completed P1 corpus positions this paper as the **minimal worked microcase for separating retrieval candidacy, node admission, edge admission, path participation, and interpretation standing in Semantic Manifold Topology**. It is a pedagogical and conformance fixture, not the full SMT theory or evidence that one retrieval policy generalizes.

- **Adjacent work:** *Governed Semantic Cartography*  
  **Supplies:** Coordinates, projections, traversal, and path-global admission.  
  **Minimal-example boundary:** The microcase exercises one retrieval path through that navigation surface.

- **Adjacent work:** *Semantic Field Analysis*  
  **Supplies:** Relations, tensions, gaps, and bounded field analysis.  
  **Minimal-example boundary:** SFA may generate candidate edges; this case adjudicates a small retrieval relation.

- **Adjacent work:** *Global Term Key: Identity Primitives in Governed Knowledge Systems*  
  **Supplies:** GTK record, resolver, adjacency, and conformance machinery.  
  **Minimal-example boundary:** GTK resolves the nodes; node resolution does not admit an edge or path.

- **Adjacent work:** *Semantic Legitimacy Before Context*  
  **Supplies:** Admission discipline before content becomes binding context.  
  **Minimal-example boundary:** The retrieval case applies that distinction to a concrete path.

- **Adjacent work:** *Warrant by Structure*  
  **Supplies:** The evaluated relation among claim, authority path, evidence, and standing.  
  **Minimal-example boundary:** A path can supply structural support without making its interpretation true or sufficient.

A retrieval case should bind:

$$
\begin{aligned}
R= (&query, registry, nodes, candidate\_edges, \\
&node\_decisions, edge\_decisions, path\_decision, \\
&interpretation, evidence, standing, remainder)
\end{aligned}.
$$

Similarity proposes candidates; it does not establish identity, continuity, derivation, relevance, or path admissibility. A node can be admitted while a proposed edge is refused. Admitted edges can form a path that is globally refused. A path can be admitted while its interpretation remains unknown or disputed.

The fixture should preserve negative results and the reason for each judgment. Repeated retrieval under another registry, profile, corpus snapshot, or time may yield a different decision without retroactively changing the earlier result.

The universal GSM can type   
`RETRIEVED_AS_CANDIDATE`, `RESOLVED_AS_NODE`,  
`PROPOSED_EDGE_TO`, `NODE_ADMITTED_UNDER`, `EDGE_ADMITTED_UNDER`, `PARTICIPATES_IN_PATH`,  
`PATH_REFUSED_BY`, `INTERPRETATION_UNKNOWN`, `SUPPORTED_BY_RETRIEVAL_EVIDENCE`,  
and   
`REVISED_UNDER_PROFILE`. These relations make the example reusable as a test fixture.

This integration establishes four editorial commitments: classify the paper as a retrieval-admission microcase; adopt the retrieval-case envelope; preserve node/edge/path/interpretation decisions independently; and publish negative and unknown outcomes as first-class fixtures.

## From Retrieval Admission to Governed Use

The fixed-seed comparison with the Optional Coordinator, GOV anchors, Meta-Binding, and GOORRT extends the microcase by separating admitted retrieval from downstream use:

$$
\begin{aligned}
U= (&query, nodes, edges, path, interpretation, use\_purpose, \\
&representation\_jurisdiction, constraint\_uptake, effect, \\
&evidence)
\end{aligned}.
$$

A GOV anchor can supply a deterministic candidate link from a source location to a task record, yet the record's relation to another concept or action still requires the appropriate edge and path judgment. GOORRT adds jurisdiction: an object representation, operation representation, and realization representation may all be admitted while their claimed correspondence remains refused or unknown.

Meta-Binding begins after retrieval and admission. The system must represent the governing constraint, operate over its relation to the task, and show a controlled behavioral difference. Repeated retrieval, context inclusion, citation, or verbal explanation does not establish constraint use.

The Optional Coordinator adjacency produces   
`NO_MATERIAL_RELATION`. A retrieval graph can help participants find information, but path admission does not show that arbitration, allocation, enforcement, recovery, accountability, or other coordinator functions were substituted.

The universal GSM can type   
`ADMITS_RETRIEVAL_FOR_USE_PURPOSE`, `ROUTES_FROM_GOV_ANCHOR`,  
`CROSSES_REPRESENTATION_JURISDICTION`, `REFUSES_CORRESPONDENCE_DESPITE_NODE_ADMISSION`,  
`USES_RETRIEVED_CONSTRAINT`, and   
`HAS_NO_COORDINATOR_OPTIONALITY_FROM_PATH`.

This randomized review establishes four editorial commitments: add governed use after interpretation standing; record representation jurisdiction and correspondence separately; require behavioral uptake before a Meta-Binding claim; and reject retrieval-path topology as coordinator-substitution evidence.

## A Retrieval Fixture That Ends Before Governed Use

Four downstream uses confirm that this minimal example is a reusable boundary fixture rather than a complete retrieval system. Governed Semantic Cartography uses it as one bounded traversal test. GOV uses it after anchor discovery to decide whether linked records may participate in a path. GOORRT uses it before correspondence among object, operation, and realization representations. Meta-Binding uses it before asking whether a retrieved constraint actually changes later operation.

The resulting chain is:

$$
\begin{aligned}
&Candidacy \\
&\rightarrow NodeAdmission \\
&\rightarrow EdgeAdmission \\
&\rightarrow PathAdmission \\
&\rightarrow InterpretationStanding \\
&\rightarrow UseAdmission \\
&\rightarrow ConstraintUptake \\
&\rightarrow EffectEvidence
\end{aligned}.
$$

Each arrow requires its own subject, profile, evidence, decision, and remainder. A deterministic anchor can improve candidate discovery without admitting an edge. An admitted path can support navigation without proving correspondence. Context inclusion, citation, verbal explanation, and repeated retrieval do not demonstrate constraint uptake. A controlled behavioral difference does not by itself establish that the intended semantic relation caused the effect.

The Optional Coordinator comparison remains a deliberate nonrelation. Graph traversal can help participants find information, but this fixture supplies no evidence that allocation, arbitration, enforcement, recovery, custody, or accountability functions have been replaced.

The universal GSM can type   
`GENERATES_RETRIEVAL_CANDIDATE`, `ADMITS_NODE_SEPARATELY`,  
`ADMITS_EDGE_SEPARATELY`, `ADMITS_PATH_GLOBALLY`, `GRANTS_INTERPRETATION_STANDING`,  
`ADMITS_USE_FOR_PURPOSE`, `TESTS_CONSTRAINT_UPTAKE`, `OBSERVES_DOWNSTREAM_EFFECT`,  
and   
`REFUSES_COORDINATOR_SUBSTITUTION_INFERENCE`.

This reverse-dependency review establishes four editorial commitments: extend the fixture through governed use while preserving every prior gate; require subject/profile/evidence/remainder at each transition; retain Meta-Binding and effect evidence above retrieval admission; and preserve the Optional Coordinator result as an explicit nonrelation.

## 12. Counterevidence and Failure Tests

The example must narrow or fail if: (1) policy labels alone determine authority; (2) individual admission is mistaken for continuity; (3) similarity is treated as irrelevant to candidate discovery; (4) similarity is promoted to identity; (5) missing evidence is mislabeled refusal; (6) known insufficiency is mislabeled universal unknown; (7) B is discarded despite independent admissibility; (8) B participates through a blocked edge; (9) a valid low-similarity revision is rejected; (10) a copied high-similarity artifact inherits authority; (11) node and edge schemas use incompatible times; (12) an expired transition remains active; (13) a rebinding receipt does not bind both endpoints; (14) path evaluation ignores one required edge; (15) evaluation receipts omit excluded evidence; (16) retrieval model/version is not recorded; (17) context admits a result beyond the query authority; (18) unknown silently becomes admitted; (19) an author decision is fabricated from system inference; (20) the GMB merges near-duplicate nodes; (21) the paper claims a measured 0.997 result; (22) SMT is confused with satisfiability modulo theories; (23) graph structure is overstated as a mathematical manifold; or (24) the same fixture cannot be reproduced from retained inputs.

## Similarity Retrieves Candidates; It Does Not Create Continuity

### Public orientation

This minimal SMT companion separates four judgments: retrieval candidacy, node admission, edge admission, and path participation. Two highly similar documents may each be admitted under different policies while no evidence supports a continuity edge. The correct bounded result is `CONTINUITY_UNKNOWN`, not an inferred successor or preferred interpretation.

### Adversarial tests

1. **Similarity-continuity attack.** High lexical or embedding similarity is treated as version lineage, supersession, equivalence, or inherited standing.
2. **Node-edge attack.** Admission of both endpoint nodes is treated as admission of the relation between them.
3. **Edge-path attack.** One admitted edge is treated as permission for every traversal, query purpose, or downstream use.
4. **Policy-version attack.** Admission under policy v1 is compared with admission under v2 as though criteria, authority, and effects were unchanged.
5. **Schema-self-validation attack.** A typed graph and rule evaluator are treated as proof that the selected policy is legitimate and complete.
6. **Missing-edge-negative attack.** Absence of continuity evidence is treated as proof of discontinuity or conflict rather than unknown.
7. **Score-fiction attack.** The illustrative 0.997 value is repeated as a measured retrieval result.
8. **Fixture-system attack.** Expected behavior in a hypothetical microcase is reported as an implemented SMT, retrieval, or admission system.

### Claim and evidence ceiling

The paper specifies a hypothetical fixture, semantics, and test matrix. It does not report an implemented index, measured similarity, executed schema, validated policy, admitted corpus record, or real continuity judgment. SMT here means Semantic Manifold Topology, and the example needs only a typed graph rather than a mathematical manifold claim.

Implementation evidence would require exact fixtures, policy and schema versions, positive and negative edges, unknown outcomes, path-purpose rules, hostile metadata, evaluator outputs, and replay. No implementation or external research occurred in this pass.

### Reader-facing consequence

The example teaches a crucial refusal: when two records look alike but their governed relation is unsupported, preserve both nodes, preserve the uncertainty, and do not let retrieval manufacture history.

## Conclusion

Retrieval finds candidates. Admission evaluates artifacts. Continuity evaluates relations. Participation evaluates complete task paths. These operations can agree, disagree, or remain unresolved.

The minimal lesson is not that similarity has no value. It is that similarity cannot silently carry identity, continuity, or authority. A governed system preserves the useful candidate while refusing the unsupported edge.

## Reference and Verification Note

### Author corpus interfaces inspected under exact custody

Ableman Adam Ableman *Semantic Manifold Topology - Worked Example.*

Ableman Adam Ableman *Retrieval-Augmented Reasoning under Constitutional Constraints.*

Ableman Adam Ableman *Reasoning by Way of Receipts.*

Ableman Adam Ableman *Governed Context and Memory.*

### External verification required

No external literature was consulted. Publication comparison should examine vector retrieval, embeddings, graph and manifold representations, provenance, access control, retrieval-augmented generation, temporal knowledge graphs, and uncertainty-aware retrieval. The example remains hypothetical until implemented and measured.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Publication form.** This work is retained as a standalone technical companion because its concrete migration method is useful independently; it remains subordinate to the architecture it explains.

## Corpus-Wide Reference Positioning

This paper argues that semantic similarity can retrieve two nearly identical artifacts without establishing that one continues, supersedes, rebinds, or inherits authority from the other. Its nearest external comparison fields are ai, formal, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Patrick Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **Relationship:** Predecessor retrieval architecture; comparison centers on provenance, admission, and fail-closed constraints not supplied by retrieval alone.

**[E2]** Shunyu Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. arXiv:2210.03629. https://arxiv.org/abs/2210.03629 **Relationship:** Predecessor agent pattern for interleaving reasoning and action; used to distinguish action traces from governed effects.

**[E3]** Elham Tabassi. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1, 2023. DOI: 10.6028/NIST.AI.100-1. https://doi.org/10.6028/NIST.AI.100-1 **Relationship:** Adjacent risk-management framework used to test whether the paper operationalizes governance beyond voluntary process guidance.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Emily M. Bender et al. "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *FAccT '21*, 2021. DOI: 10.1145/3442188.3445922. https://doi.org/10.1145/3442188.3445922 **Relationship:** Counterpressure concerning scale, environmental cost, documentation, and social risk; included to prevent governance proposals from becoming capability-only narratives.

**[E6]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E7]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

### Ableman corpus

**[A1]** Adam Ableman. *CARA: Constrained Artificial Reasoning Architecture*. Ableman Corpus current edition; work identity `PAPER.PUB.18099715`;  
source SHA-256  
`F8F74F0CD58F5414D9A29EBE958E49751892D07A028CB51197F8201B18AAB40E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *A Constitution for the Context Window*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-CF26BA0E123F472F`;  
source SHA-256  
`60395402368E146F115CCE53D0E5A15B8FB23C90ED5B24CA92AB8515B2009965`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Governed Context & Memory (GCM)*. Ableman Corpus current edition; work identity `PAPER.PUB.18633797`;  
source SHA-256  
`3F17ACD8AB9C6DC66C23D22098628C70042854B198C3ABFCBFA3EC7DC27B9C08`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Retrieval-Augmented Reasoning under Constitutional Constraints*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-384489D4604BEC4D`;  
source SHA-256  
`133DA35C0F27F35BAA1F53DFEE415068AD2D24FF713F8CDAFA2FDC8F748AC15C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Split-Authority AI Coordination*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-35D1BAECD5CB17AD`;  
source SHA-256  
`06FB6133170879FA8308684F0DA33F5813EAF3B5488291C2D7D234BEB6FDFEC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Ableman Corpus current edition; work identity `PAPER.PUB.21095303`;  
source SHA-256  
`EA129ECBA95F7B07CAA7B33A54F91F52913C94A14DA227EB9A06CFD083E4E5BF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Semantic Compilation*. Ableman Corpus current edition; work identity `PAPER.PUB.18453681`;  
source SHA-256  
`5FF6C636550B04DB0E2F6F94C379BB75AA0BD8781E19B047D7D3BB6D49071AC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Semantic Manifold Topology.* Zenodo, 2026. doi:10.5281/zenodo.20257244

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

DOI: [10.5281/zenodo.23848088](https://doi.org/10.5281/zenodo.23848088)
