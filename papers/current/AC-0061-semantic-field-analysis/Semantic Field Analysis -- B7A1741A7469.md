# Semantic Field Analysis

## Reachability, Tension Detection, and Invariant-Preserving Navigation in Governed Semantic Systems

### Semantic Field Analysis (SFA) is a proposed diagnostic method for examining those interactions as versioned, governed graph projections.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Large governed knowledge systems accumulate claims, assumptions, constraints, evidence, refusals, and typed relationships whose interactions cannot be understood by document retrieval alone. **Semantic Field Analysis (SFA)** is a proposed diagnostic method for examining those interactions as versioned, governed graph projections.

SFA does not treat basins, convergence, collapse, or drift as intrinsic properties of an undifferentiated corpus. Each result is relative to a declared projection: node and edge types, identity resolution, jurisdiction, time, standing, evidence policy, lens, thresholds, and treatment of uncertainty. Under such a projection, SFA can propose support-cohesion regions, tension boundaries, admissible paths, dependency-sensitive convergence candidates, and version-to-version structural changes.

These outputs are diagnostic candidates, not truth, authority, or automatic governance decisions. Dense agreement may reflect duplicated sources or shared error. Contradiction may be scoped rather than globally inconsistent. Change may be correction rather than drift. The paper defines a typed field model, repairs the invariant-preserving path condition, integrates SFA with the Governed Meaning Base (GMB), universal GSM, semantic cartography, binding quality, fragmentation analysis, and governed semantic compilation, and specifies countertests and an evaluation program.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/semantic-`

`field-analysis/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`3438748F405554FFD1537127AC00D0C123F17911F7E0B94F7BA4A5D48DB73AD9`. The exact source remains unchanged.

The field-level thesis, basins, collapse ridges, invariant paths, convergence, drift, and GSC relationship are author material. The typed projection model, formal repairs, GMB/GSM placement, corpus interfaces, counterevidence, evaluation plan, and editorial alternatives are AI-assisted contributions explicitly distinguished from the original author material.

No graph analysis or external research was performed. No result here establishes truth, novelty, implementation, conformance, canonical standing, identity merger, or evidence readiness.

## 1. Problem and Scope

Document retrieval answers which artifacts mention a term. SFA asks how explicitly represented semantic objects behave within a selected governed relation structure. The distinction matters because one artifact may support, qualify, contradict, refine, depend on, cite, supersede, or merely resemble another. Treating all edges alike manufactures structure that the corpus never declared.

SFA therefore operates only after identity, relation type, provenance, standing, scope, and version are sufficiently explicit. It may analyze author material, AI synthesis, disputed candidates, and historical states, but it must keep those postures visible.

The bounded thesis is:

> A governed corpus can expose diagnostically useful structural patterns when analysis is performed over typed, versioned, provenance-bearing projections whose assumptions and uncertainty remain inspectable.

## 2. Typed Semantic Field

Let the governed semantic corpus at version $t$ be a typed attributed multigraph:

$$
G_t=(V_t,E_t,\tau_V,\tau_E,A_V,A_E,P),
$$

where $V_t$ contains identified semantic objects, $E_t$ contains directed typed relations, $\tau_V$ and $\tau_E$ assign node and edge types, $A_V$ and $A_E$ hold provenance, standing, jurisdiction, time, evidence, and uncertainty, and $P$ is the governing policy state.

An SFA result is computed over a projection:

$$
G^q_t=\Pi_q(G_t),
$$

where profile $q$ declares included types, jurisdictions, standing classes, time window, identity rules, relation semantics, weights, thresholds, and missing-data treatment. Results from different profiles are not automatically comparable.

The word **field** is a functional metaphor for this navigable relation environment. It does not assert a physical field, continuous geometry, or model-internal representation.

## 3. Semantic Basins as Profile-Relative Candidates

A semantic basin is not simply a strongly connected component. Support may be directed, qualification may reduce a claim, and circular citation may create density without independent support. Define a basin candidate $B\subseteq V(G^q_t)$ under profile $q$ using declared measures such as:

- within-region support or dependency cohesion;
- source independence and evidence diversity;
- low unresolved mandatory contradiction under the chosen scope;
- boundary conductance or retention under permitted traversal;
- standing and uncertainty distribution; and
- sensitivity to removal of high-degree nodes or duplicated sources.

A basin indicates structural cohesion under $q$, not truth, consensus, quality, or authority. A propaganda cluster, circular citation network, or shared mistaken premise can form a strong basin. SFA should therefore return the profile, contributing edges, dependency families, counterevidence, and sensitivity results with every basin label.

## 4. Tension Boundaries and Collapse

The source's **collapse ridge** is retained as a strong term for a narrow condition. A contradiction edge alone does not prove collapse. Artifacts may concern different jurisdictions, times, definitions, or epistemic postures; a governed corpus can also preserve unresolved disagreement without explosion.

A **tension boundary** exists where typed claims or constraints cannot be jointly traversed under profile $q$ without qualification, branching, or adjudication. A **collapse condition** is stronger:

$$
\mathrm{Collapse}_q(R) \iff \neg\exists c\in CM_1(R,q),
$$

meaning that no configuration of region $R$ satisfies the mandatory invariants declared by $q$. This definition makes collapse relative to explicit invariants and Configuration Manifold 1 rather than a visual graph feature.

SFA should report whether a boundary is definitional mismatch, scoped disagreement, evidentiary conflict, temporal supersession, identity collision, policy incompatibility, or genuine no-admissible-configuration collapse.

## 5. Invariant-Preserving Paths

The original condition $I(n_1)\subseteq I(n_k)$ is insufficient: endpoint sets do not show that intermediate transitions preserved anything, and set inclusion can mistake newly asserted invariants for satisfaction.

For path $p=(v_0,e_1,v_1,\ldots,e_k,v_k)$, define:

$$
\mathrm{Admissible}_q(p) \iff
\bigwedge_{i=1}^k \mathrm{Allowed}_q(e_i,v_{i-1},v_i)
\wedge
\bigwedge_{j\in I_q} \mathrm{Preserved}_j(p).
$$

`Allowed` checks edge type, direction, identity, jurisdiction, time, standing, evidence, and authority.

`Preserved` is invariant-specific and must be operationally defined. A path may be admissible for explanation but not for authority, publication, implementation, or causal inference.

Path output should include the exact edges, rejected alternatives, unresolved gaps, governing profile, and a claim ceiling. Similarity or adjacency alone cannot serve as an admissible reasoning step.

## 6. Navigation and Projection

Field navigation begins from an identified node or question and selects a lens. A useful sequence is:

```text
resolve identity and standing
  -> choose profile and projection
  -> inspect typed neighborhood
  -> traverse permitted paths
  -> compare cohesion and tension regions
  -> inspect exact evidence and counterevidence
  -> return findings with limits
```

This aligns SFA with Governed Semantic Cartography: cartography supplies coordinates, projections, and traversal semantics; SFA supplies diagnostic operators over a selected projection. Semantic Manifold Competence concerns the ability to navigate and operate appropriately. Neither is identical to SFA.

## 7. Convergence Without False Independence

Multiple paths reaching a compatible claim form a **convergence candidate**, not independent confirmation. Paths may share a source, model, author, assumption, extraction error, or upstream artifact. SFA should compute dependency overlap before describing convergence as corroborative.

At minimum, a convergence report should distinguish:

- multiple renderings of one source;
- several paths with a shared ancestor;
- independent evidence families;
- lexical convergence without identity agreement;
- compatible conclusions under different qualifications; and
- centrality caused by curation or linking policy.

Convergence can identify a useful conceptual hub while remaining silent about truth. Popularity, degree, and structural centrality are not authority.

## 8. Change, Drift, and Distortion

Let $G^q_t$ and $G^q_{t+1}$ be comparable projections. A semantic change record is:

$$
\Delta_q(t,t+1)=\mathrm{Diff}(G^q_t,G^q_{t+1}),
$$

including node, edge, identity, standing, evidence, invariant, and policy changes. **Drift** should be reserved for change away from a declared invariant or intended reference. Other changes may be correction, refinement, expansion, deletion, merger proposal, or policy revision.

Signals such as contradiction density, basin fragmentation, or unsupported-node growth require normalization for corpus size, source duplication, review backlog, and profile changes. A sudden structural shift is an investigation trigger, not automatic damage.

## 9. GMB and Universal GSM Placement

The **Governed Meaning Base (GMB)** is the current name in the author-confirmed `CCF -> CMB -> GMB` lineage. Historical CCF wording in the source is retained as lineage, not as the current architecture name.

GMB governs semantic objects, standing, disputes, evidence, and revision. The universal GSM supplies typed identities, relations, primitives, invariants, dimensions, and adjacencies. SFA is an analytic projection over that governed fabric. It does not replace GMB, define the whole GSM, or authorize mutations based on its diagnostics.

GTK supports lexical identity resolution. Semantic Fragmentation distinguishes incompatible structures. Semantic Binding Quality evaluates relation quality under a declared profile. Governed Semantic Compilation controls promotion into semantic state. SFA analyzes selected postures and relations after or across those operations. These are interfaces, not identity mergers.

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

- **Possibility:** propose field models, profiles, measures, and visualizations.
- **Specification:** define node and edge types, identities, profiles, invariants, outputs, and claim ceilings.
- **Configuration Manifold 1 (CM1):** retain analytically admissible configurations satisfying mandatory identity, custody, type, authority, and evidence rules.
- **Configuration Manifold 2 (CM2):** prefer among admissible measures and projections for a stated task.
- **IC:** choose an **Instance Constitution** or **Instance Configuration** for a specific corpus. The names are interchangeable.
- **IR:** build an **Instance Realization** or **Implementation Realization** of that same stage. The names are interchangeable.
- **Evidence:** compare output with annotated cases, counterexamples, reviewer judgments, and known graph changes.
- **Revision:** change profiles, thresholds, identities, relations, and algorithms while preserving lineage.

This paper proposes a method. It selects no IC and certifies no IR.

## 11. Automation and Output Contract

Automated SFA may compute candidate regions and paths, but every result should carry:

- corpus and projection version;
- profile and parameter hashes;
- included and excluded standing classes;
- node and edge identity basis;
- relation-type semantics;
- source-dependency treatment;
- uncertainty and sensitivity analysis;
- exact evidence links;
- counterexamples or rejected alternatives; and
- the permitted interpretation and prohibited inferences.

Results should be receipted and reproducible where possible. Human or agent review may accept, revise, contest, or refuse a diagnostic; no metric promotes itself into semantic authority.

## Diagnostic Analytics Profile Over the Governed Semantic Fabric

Across the completed P1 corpus, Semantic Field Analysis is the **diagnostic analytics profile for finding cohesion, tension, admissible paths, convergence candidates, and change within a selected governed semantic projection**. It is not a replacement for the Governed Meaning Base, semantic cartography, identity resolution, binding evaluation, compilation, or author adjudication.

- **Adjacent work:** *Governed Semantic Cartography*  
  **Supplies:** Coordinate, projection, traversal, and path-global admission semantics.  
  **SFA boundary:** SFA runs diagnostics over a declared cartographic projection.

- **Adjacent work:** *Semantic Fragmentation and Constitutional Structure*  
  **Supplies:** Fragmentation types, incompatible structures, and repair targets.  
  **SFA boundary:** SFA may detect candidate fragmentation patterns without resolving them automatically.

- **Adjacent work:** *Semantic Binding Quality (SBQ)*  
  **Supplies:** Profile-relative evaluation of semantic bindings.  
  **SFA boundary:** SBQ evaluates relation quality; SFA analyzes larger projected structures using such evaluations.

- **Adjacent work:** *Theory of Semantic Computing Infrastructure*  
  **Supplies:** Semantic storage, transformation, retrieval, and governance capabilities.  
  **SFA boundary:** SFA is one analytic capability hosted by that infrastructure.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Admission, lowering, remainder, and receipted transformation.  
  **SFA boundary:** SFA output becomes governed state only through a separate compilation and promotion decision.

An analysis run should bind:

$$
\begin{aligned}
F= (&corpus\_snapshot, projection, identity\_policy, \\
&edge\_semantics, standing\_filter, measures, parameters, \\
&dependency\_model, results, sensitivity, counterexamples, \\
&claim\_ceiling)
\end{aligned}.
$$

This envelope makes an SFA finding replayable as a result of a particular view rather than an intrinsic property of the whole corpus. Every basin, tension boundary, path, convergence candidate, or drift signal must retain the included and excluded nodes, source-family dependencies, rejected alternatives, and sensitivity to profile or threshold changes.

SFA should prefer the simplest adequate operator. If a typed query, dependency trace, contradiction search, or source-family deduplication explains the finding, the field vocabulary adds no independent result. More complex analytics earn use only when they expose a materially useful interaction that simpler operations miss.

The universal GSM can type   
`ANALYZED_UNDER_PROJECTION`, `FORMS_BASIN_CANDIDATE`,  
`CROSSES_TENSION_BOUNDARY`, `HAS_ADMISSIBLE_PATH_UNDER`, `CONVERGES_WITH_SHARED_DEPENDENCY`,  
`CHANGES_RELATIVE_TO_REFERENCE`, `SENSITIVE_TO_PARAMETER`, `EXCLUDES_STANDING_CLASS`,  
`CONTESTED_BY_COUNTEREXAMPLE`,  
and   
`PROMOTION_REQUIRES_ADJUDICATION`. These relations make diagnostics inspectable without turning the graph into an oracle.

This integration establishes four editorial commitments: classify SFA as a diagnostic analytics profile; adopt the analysis-run envelope; require simple-baseline and sensitivity comparisons; and prohibit SFA results from self-promoting into identity, truth, authority, or canonical standing.

## Temporally Versioned Diagnostic Run

The fixed-seed comparison with the seventeen-system evidence study, the MCIR DAG theorem, the GMB, and Quant Insights for ACG makes an SFA result time- and substrate-specific:

$$
\begin{aligned}
F^*= (&GMB\_snapshot, reference\_profile, projection, \\
&identity\_policy, standing\_cut, method\_version, \\
&parameters, data\_vintage, decision\_time, results, \\
&sensitivity, counterexamples, lineage, ceiling)
\end{aligned}.
$$

The seventeen-system paper is one versioned evidence application of the method. Its case revisions and category changes should be lineaged rather than overwritten. A closed DAG reference layer can improve reconstructability while remaining silent about edge semantics, missing evidence, reviewer quality, or result validity.

The GMB hosts the governed source, identity, relation, evidence, standing, dispute, and revision state over which the projection is drawn. SFA output is a diagnostic candidate until separately admitted. Quant temporal discipline requires the run to use only the data, identities, policies, and evidence admissibly available at its declared decision time when making point-in-time claims.

Later corrections may produce a successor analysis without retroactively changing what was knowable. The universal GSM can type   
`ANALYZES_GMB_SNAPSHOT`,  
`USES_REFERENCE_CLOSURE_PROFILE`, `APPLIES_SFA_METHOD_VERSION`,  
`USES_ADMISSIBLE_DATA_VINTAGE`, `LINEAGES_DIAGNOSTIC_SUCCESSOR`,  
`SENSITIVE_TO_TEMPORAL_CUT`, and   
`REQUIRES_SEPARATE_PROMOTION`.

This randomized review establishes four editorial commitments: adopt the temporally versioned run object; bind analyses to GMB and reference profiles; preserve point-in-time evidence discipline; and lineage successors without retroactive knowledge leakage.

## A Reproducible Semantic-Analysis Run

Ten downstream uses show Semantic Field Analysis as a shared method rather than a store, map, solver, or verdict engine. GMB supplies governed state; cartography supplies maintained map layers; field analysis inspects a bounded projection. Craft work uses it before comparing variables. Governance Incentive Engineering adds actors, strategies, burdens, and interventions. SMT retrieval may adjudicate candidate edges produced by SFA. Quant evaluation and recursive orientation use it as one time-bounded probe. Semantic-fragmentation work specializes it to hidden operative constitutions, and the seventeen-system study is one empirical application.

Every analysis run should bind:

$$
\begin{aligned}
R^*= (&source\_snapshot, projection, profile, question, \\
&identities, edge\_semantics, standing, observer, metrics, \\
&baselines, sensitivity, countermaps, findings, evidence, \\
&remainder, expiry, revision)
\end{aligned}.
$$

The run is reproducible only relative to its snapshot, projection, metric and inference profile. Cohesion, basin, tension, pressure, gap, path, and convergence are diagnostic outputs whose meaning depends on edge types, weights, standing, and observer choices. They do not become physical fields, causal forces, identity decisions, admissibility results, or author judgments through visualization or mathematical form.

Sensitivity should perturb projection, edge inclusion, weights, standing filters, baseline, time window, and observer assumptions. Countermaps preserve plausible alternate fields. A finding that disappears under a nearby admissible profile should be reported as profile-sensitive rather than promoted as a corpus fact.

The universal GSM can type   
`RUNS_SEMANTIC_FIELD_ANALYSIS`, `PROJECTS_FROM_GMB_SNAPSHOT`,  
`GENERATES_CANDIDATE_EDGE`, `SPECIALIZES_TO_HIDDEN_CONSTITUTION`,  
`PERTURBS_ANALYSIS_PROFILE`, `PRESERVES_COUNTERMAP`, and   
`EXPIRES_ANALYTIC_FINDING`.

This reverse-dependency review establishes four editorial commitments: adopt the reproducible-run envelope; bind all field language to exact analytic semantics; require sensitivity and countermaps; and keep SFA outputs nonbinding until separately adjudicated.

## 12. Counterevidence and Failure Modes

SFA must narrow or fail where:

1. lexical similarity is mistaken for node identity;
2. edge types are collapsed into generic adjacency;
3. inferred edges are presented as declared commitments;
4. source duplication creates false cohesion or convergence;
5. circular citation appears as independent support;
6. contradiction is unscoped across time or jurisdiction;
7. a disagreement is incorrectly called collapse;
8. endpoint invariants hide an invalid intermediate transition;
9. a profile silently excludes dissent or low-standing evidence;
10. thresholds are selected after observing the desired result;
11. centrality is treated as truth or authority;
12. graph sparsity reflects missing ingestion rather than conceptual isolation;
13. dense linking reflects curator preference rather than semantic structure;
14. a field change is correction rather than harmful drift;
15. profile changes make temporal comparisons invalid;
16. uncertain or contested edges are coerced into binary values;
17. metric optimization creates Goodhart effects;
18. computational scale forces sampling that hides boundary cases;
19. visualization geometry implies distances not present in the graph; or
20. simpler typed queries explain the result as well as the field vocabulary.

## 13. Evaluation Program

A credible SFA evaluation requires versioned benchmark graphs containing known identity collisions, duplicated sources, shared assumptions, scoped contradictions, genuine no-admissible-configuration cases, valid and invalid paths, corrections, and policy changes. Candidate methods should be tested for precision, recall, calibration, sensitivity to profile changes, robustness to adversarial linking, reproducibility, reviewer usefulness, and explanatory fidelity.

Baselines should include ordinary typed graph queries, strongly connected components, community detection, dependency analysis, contradiction queries, and source-family deduplication. SFA earns standing only where its combined profile and outputs add value beyond those simpler operations.

## Analysis Over a Governed Field, Not Governance by Analytics

### Public orientation

Semantic Field Analysis examines an admitted corpus as a directed, temporally versioned field. It can identify coherent basins, contradiction ridges, paths, convergence, drift, and distortion. It observes the governed semantic fabric; it does not admit sources, invent standing, resolve disputes, or infer truth.

### Adversarial tests

1. **Graph-construction attack.** Results reflect omitted, duplicated, or misclassified nodes and edges. Every run must bind its exact graph projection and exclusions.
2. **Inferred-edge laundering.** Model similarity becomes an asserted semantic relation. Extracted, inferred, proposed, disputed, and authored edges need separate standing.
3. **Topology-as-truth attack.** Centrality or reachability is treated as importance, correctness, or authority. Metrics describe a projection only.
4. **Contradiction-misclassification.** Difference, scope, temporal succession, or alternative vocabulary is labeled contradiction. Classification requires evidence and review.
5. **Temporal-drift attack.** Two runs compare different source or model generations without attribution. Snapshot, operator, and dependency identities are mandatory.
6. **Convergence-independence attack.** Similar results from tools sharing embeddings, prompts, data, or code are treated as independent confirmation.
7. **Scale-opacity attack.** Approximation, truncation, sampling, or indexing changes findings. Computational shortcuts and error bounds must be reported.
8. **Analytics-authority attack.** A diagnostic output automatically changes GMB standing or policy. SFA recommendations remain zero-authority proposals.

### Claim and evidence ceiling

The paper defines a reproducible diagnostic run and output contract. It does not establish objective semantic geometry, complete contradiction detection, truth, causality, or governance authority. Basins and ridges are operator- and projection-relative.

Claims about graph methods, embeddings, clustering, information retrieval, scalability, or human interpretability require external comparison and evaluation. Internal runs can test reproducibility and utility within the corpus but not general validity. No external research was added in this pass.

### Reader-facing consequence

The public benefit is a map of where ideas reinforce, diverge, conflict, or drift, with every result tied to the exact corpus and analytic choices that produced it and no metric allowed to rewrite the underlying authority record.

## 15. Conclusion

Semantic Field Analysis can turn a large corpus from an opaque document mass into an inspectable relation environment. Its value does not come from the field metaphor alone. It comes from disciplined projection: exact identities, typed edges, explicit standing, declared invariants, source dependency, versioned profiles, and recoverable evidence.

Under those conditions, basins can identify structural cohesion, tension boundaries can localize adjudication needs, admissible paths can expose governed reasoning routes, convergence can be qualified by dependency, and graph change can be separated from harmful drift. None of these results authorizes itself. SFA is most useful when it makes the corpus easier to question without making the graph an oracle.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that large governed knowledge systems accumulate claims, assumptions, constraints, evidence, refusals, and typed relationships whose interactions cannot be understood by document retrieval alone. Its nearest external comparison fields are semantic, software, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. Modularity, secure-development practice, and reproducibility reduce classes of failure but do not guarantee architectural coherence or user sovereignty. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** David L. Parnas. "On the Criteria To Be Used in Decomposing Systems into Modules." *Communications of the ACM* 15(12), 1972, pp. 1053-1058. DOI: 10.1145/361598.361623. https://doi.org/10.1145/361598.361623 **Relationship:** Foundational modularity treatment used to compare information hiding with explicit semantic and governance interfaces.

**[E7]** Ward Cunningham. "The WyCash Portfolio Management System." *OOPSLA '92 Experience Report*, 1992. DOI: 10.1145/157709.157715. https://doi.org/10.1145/157709.157715 **Relationship:** Original technical-debt metaphor used to distinguish implementation debt from semantic debt.

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

**[A6]** Adam Ableman. *Sovereign Software*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-24C6159B98023A9C`;  
source SHA-256  
`6AAFE79E438B980B75D1910A897F7BA716A10CF1187B68CB1F71405F36725A18`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Constitutional Software Analysis (CSoftA): A Governance-Based Classification Method for Software Systems*. Ableman Corpus current edition; work identity `PAPER.PUB.20472196`;  
source SHA-256  
`3670B28B7C1AF5467BE4002C47B5F964F8FAF6F257125C2F84CE06904E4FD0DE`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Semantic Manifold Competence.* Zenodo, 2026. doi:10.5281/zenodo.20533169

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

DOI: [10.5281/zenodo.23848213](https://doi.org/10.5281/zenodo.23848213)
