# Semantic Binding Quality (SBQ)

## A Structural Framework for Evaluating Meaning Stability

### SBQ describes the degree to which a binding forms a coherent, generative, and stable relation within a semantic network.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

If meaning emerges through relational bindings between structures, the mere presence of a binding does not guarantee semantic integrity. Bindings vary in stability, coherence, generativity, and resistance to distortion. Some bindings become foundational elements of scientific, legal, and computational systems, while others remain fragile, parasitic, or misleading. This paper introduces **Semantic Binding Quality (SBQ)** as a structural framework for evaluating the integrity of semantic bindings.

SBQ describes the degree to which a binding forms a coherent, generative, and stable relation within a semantic network. High-SBQ bindings exhibit strong integration with surrounding structures, produce new derivations or system capabilities, and remain robust under perturbation. Low-SBQ bindings exhibit fragility, distortion, or parasitic stability.

The framework presented here proposes several dimensions of SBQ, including structural coherence, generativity, perturbation stability, constraint alignment, and minimal distortion. These dimensions together form a basis for evaluating semantic structures within philosophical systems, scientific theories, legal frameworks, and computational architectures.

The paper further argues that constitutional computational substrates--including the current Governed Meaning Base (GMB) lineage, historically named CCF and CMB--may support explicit SBQ evaluation through governance invariants and admissibility constraints. Formalizing SBQ may enable future systems to evaluate not only whether a binding is admissible, but whether it constitutes a structurally sound contribution to a semantic system.

---

## Scope and Formal Object

SBQ evaluates an **identified, typed binding claim**, not a vague association. Let

$$
b=(u,\rho,v,J,C,t,e),
$$

where $u$ and $v$ are identified semantic objects, $\rho$ is the relation type, $J$ is jurisdiction, $C$ is context and intended use, $t$ is time/version, and $e$ is evidence. A quality profile is then:

$$
SBQ(b\mid P)=\langle k,g,p,a,d,r,c,x\rangle_P,
$$

where a declared profile $P$ defines coherence $k$, generativity $g$, perturbation behavior $p$, constraint alignment $a$, distortion cost $d$, evidentiary adequacy $r$, contestability/revisability $c$, and dependency risk $x$. These dimensions need not be commensurable. A scalar score is optional and dangerous unless its weights, missing-data policy, uncertainty, and decision purpose are explicit.

High stability can indicate entrenchment rather than truth. High generativity can amplify a false premise. Centrality can reflect historical lock-in. Constraint alignment can preserve an unjust constitution. Low distortion relative to one ontology can erase another. SBQ therefore describes quality under a profile; it does not certify truth, legitimacy, morality, authority, or universal value.

## 1. Introduction

The relational ontology of meaning proposes that meaning emerges through **binding acts** between structures rather than residing in objects or minds alone. Once bindings stabilize within networks of dependency, they form the semantic infrastructure of knowledge systems.

However, the presence of a binding does not guarantee its quality. Semantic systems routinely contain bindings that are:

* fragile,
* distorting,
* parasitic,
* or incapable of generating further structure.

Conversely, certain bindings become foundational. Scientific axioms, legal principles, mathematical definitions, and communication protocols demonstrate extraordinary persistence and generativity.

These observations suggest the need for a structural framework capable of evaluating the **quality of semantic bindings**.

This paper introduces the concept of **Semantic Binding Quality (SBQ)** as a multidimensional measure of binding integrity. SBQ describes the structural properties that distinguish stable, generative bindings from fragile or distorting ones.

---

## 2. The Presence-Quality Distinction

A binding record may assert $b=(u,
ho,v)$ without establishing that the endpoints are correctly identified, that $
ho$ is the right relation, or that the evidence supports it. Presence, admissibility, quality, truth, authority, and standing are separate postures.

The source's original high/moderate/low table is removed from this candidate because it assigned ranks to Newtonian mechanics, software interfaces, and conspiracy narratives without a common profile or evidence. A valid comparison must hold the binding type, jurisdiction, purpose, evidence class, and evaluation dimensions sufficiently constant. SBQ should produce a vector with reasons and uncertainty, not an unexplained moralized label.

## 3. Dimensions of Semantic Binding Quality

SBQ emerges from multiple structural dimensions. These dimensions are not independent but interact within semantic systems.

### 3.1 Structural Coherence

Structural coherence describes the degree to which a binding integrates consistently with surrounding semantic structures.

Coherent bindings:

* reduce contradictions,
* align with existing definitions,
* and compose smoothly with neighboring bindings.

Incoherent bindings introduce tension within the semantic network and require continual patching or reinterpretation.

---

### 3.2 Generativity

Generativity measures the capacity of a binding to produce new structures or derivations.

Some bindings enable extensive downstream reasoning. Mathematical axioms and foundational protocols often generate large families of derived structures.

Generativity can be conceptualized as:

```text
generativity(binding) = number_of_derivable_structures
```

Bindings with high generativity expand the semantic phase space of a system.

---

### 3.3 Stability Under Perturbation

High-quality bindings remain stable under changes in surrounding conditions.

Perturbations may include:

* new empirical observations,
* alternative models,
* domain extensions,
* or system scaling.

Bindings that collapse under minor perturbations exhibit low SBQ.

---

### 3.4 Constraint Alignment

Bindings must respect structural constraints inherent to the systems they inhabit.

Examples include:

* physical laws in scientific theories,
* jurisdictional rules in legal systems,
* protocol invariants in communication networks.

Bindings that violate fundamental constraints inevitably destabilize semantic systems.

---

### 3.5 Minimal Distortion

Low-quality bindings often require extensive corrective mechanisms such as:

* exceptions,
* compatibility layers,
* ad hoc reinterpretations.

These corrective structures signal distortion within the semantic relation.

High-SBQ bindings achieve alignment with minimal distortion.

---

## 4. Semantic Energy as a Limited Analogy

The semantic-energy landscape is a heuristic, not a physical quantity or validated metric. The source relation $SBQ\propto 1/E_{semantic}$ becomes meaningful only if a profile defines energy, units or normalization, boundary conditions, and observations. Without those, the equation is metaphorical.

A safer use is to treat "energy" as a placeholder for declared repair burden: contradiction penalties, exception count, translation loss, evidence gaps, maintenance cost, and sensitivity to perturbation. Even then, lower repair burden is not automatically better; a simplistic or coercively standardized model can appear smooth because it suppresses dissent and edge cases. The analogy should generate hypotheses, not settle admission or ranking.

## 5. Binding Attractors, Dependency, and Meaning-Inertia

Bindings can accumulate dependents and become costly to change. That produces **meaning-inertia**, but dependency count is not quality. Widely reused protocols may be valuable, obsolete, or unavoidable; legal and scientific foundations may be productive while remaining revisable; a false narrative can also become a strong attractor.

An SBQ profile should therefore distinguish generative reuse from lock-in, evidence-backed stability from social entrenchment, and reversible dependence from brittle monoculture. Dependency centrality belongs beside recovery cost, substitutability, contestability, and revision history. A high-degree binding creates a larger obligation to audit downstream impact when revised; it does not earn higher standing automatically.

## 6. SBQ in the Governed Meaning Base

The **Governed Meaning Base (GMB)** is the current name in the author-confirmed `CCF -> CMB -> GMB` lineage. Historical CCF mechanisms in the source remain lineage examples, not proof that a current GMB implementation performs SBQ evaluation. GMB can store typed binding claims, profiles, evidence, counterevidence, scores or qualitative findings, disputes, decisions, dependencies, and revision lineage.

Admissibility and quality remain separate. Mandatory identity, authority, evidence, safety, and jurisdiction constraints belong in CM1. SBQ may inform CM2 preference among already admissible bindings. A high SBQ estimate cannot compensate for missing authority or failed mandatory constraints, and a low estimate does not authorize deletion of source evidence or dissent.

## 7. SBQ and the Configuration--Implementation Trap

Many contemporary software systems bind semantic meaning at the level of **implementation artifacts** rather than domain specifications.

This practice produces fragile bindings that are difficult to reuse or compose.

Relocating stable semantic contracts toward Specification may improve selected SBQ dimensions by:

* improving structural coherence,
* enabling greater generativity,
* and reducing distortion across implementations.

Constitutional computational substrates support this relocation by governing the specification space itself.

---

## 8. Toward Computational Evaluation of SBQ

Formalizing SBQ opens the possibility of computational evaluation.

Potential indicators include:

* contradiction density within semantic graphs,
* derivation depth of downstream structures,
* stability under simulated perturbations,
* dependency network centrality.

These indicators may provide profile-specific observations, but none is an automatic measure of integrity: centrality can be lock-in, derivation depth can amplify error, and contradiction density depends on modeling quality.

Future systems could therefore assist in identifying:

* fragile semantic structures,
* parasitic narratives,
* or opportunities for stronger bindings.

---

## 9. Implications for Knowledge Systems

SBQ provides a framework for understanding the evolution of knowledge systems.

Scientific progress, legal development, and technological infrastructure can be interpreted as processes of discovering or constructing higher-quality bindings.

Domains may mature when well-supported, contestable bindings become useful shared foundations; apparent stability can also reflect path dependence or exclusion.

This perspective suggests that progress in knowledge systems corresponds not merely to accumulating facts but to improving the **quality of semantic bindings** within the system.

---

## 10. Universal GSM and Realization Funnel

Within the universal GSM, SBQ is an evaluation profile over typed edges and their evidence. GTK membership asks whether names resolve to the same identity; GOORRT correspondence asks what relation holds among representations; Semantic Fragmentation locates incompatible structures; Constitutional Semantic Engineering supplies governance; Admissibility Engineering separates mandatory acceptance from preference; receipts preserve evaluated transitions. SBQ compares quality without merging these operations.

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

Possibility proposes bindings and profiles. Specification defines endpoints, relation types, invariants, evidence, and dimensions. **Configuration Manifold 1 (CM1)** contains bindings meeting mandatory admissibility. **Configuration Manifold 2 (CM2)** compares preferable admissible bindings under declared SBQ profiles. **IC** means **Instance Constitution** or **Instance Configuration** interchangeably and selects one profile and binding set. **IR** means **Instance Realization** or **Implementation Realization** interchangeably and contains actual registries, graphs, evaluators, interfaces, and effects. Evidence records tests and judgments. Revision changes bindings or profiles while preserving lineage.

## Multidimensional Binding-Quality Diagnostic

Across the completed P1 corpus, Semantic Binding Quality (SBQ) is the **multidimensional diagnostic profile for evaluating the coherence, generativity, perturbation stability, constraint alignment, and distortion of a declared binding**. It is not meaning itself, truth, legitimacy, consciousness, a universal scalar, or standing by score.

- **Adjacent work:** *Meaning as Binding*  
  **Supplies:** The compact semantic-binding ontology.  
  **SBQ boundary:** SBQ evaluates an identified binding; it does not define the binding's semantic identity.

- **Adjacent work:** *The Locus of Meaning*  
  **Supplies:** Jurisdictions, consequences, recursive binding, and semantic locus.  
  **SBQ boundary:** Those structures define what a quality profile must preserve in a domain.

- **Adjacent work:** *Semantic Debt*  
  **Supplies:** Maintenance burden from unresolved or costly semantic obligations.  
  **SBQ boundary:** Poor SBQ may create debt; a low score is not automatically a debt entry.

- **Adjacent work:** *Transformation-Dominant Semantic Systems*  
  **Supplies:** Change, obligation carriage, loss, recovery, and cost diagnostics.  
  **SBQ boundary:** TDSS evaluates transformations; SBQ evaluates the resulting or persistent binding profile.

- **Adjacent work:** *Semantic Gravitational Attractors*  
  **Supplies:** Governed convergence and canonicalization regimes.  
  **SBQ boundary:** Stability around an attractor may improve or mask quality depending on what is preserved.

An SBQ assessment should bind:

$$
\begin{aligned}
S= (&binding, jurisdiction, profile, dimensions, tests, \\
&perturbations, baselines, results, tradeoffs, \\
&uncertainty, standing)
\end{aligned}.
$$

The dimensions form a vector or partial order, not an assumed weighted sum. Structural coherence can coexist with low truth or poor authority. Generativity can produce useful consequences or uncontrolled overextension. Stability can reflect resilient meaning or rigid error. Constraint alignment depends on the validity and scope of the constraints. Minimal distortion depends on a declared preservation target.

Goodhart risk is central. Once an SBQ measure governs promotion, systems can optimize the observable score while hiding residual ambiguity, minority interpretations, cost, or failure outside the benchmark. Profiles therefore require ablations, counterexamples, adversarial perturbations, held-out jurisdictions, and qualitative review of residuals.

The universal GSM can type `ASSESSED_FOR_SBQ`, `COHERENT_UNDER_PROFILE`, `GENERATIVE_OF`,  
`STABLE_UNDER_PERTURBATION`, `ALIGNED_WITH_CONSTRAINT`, `DISTORTS_TARGET`,  
`TRADES_OFF_WITH_DIMENSION`, `GOODHARTED_BY`, `DEFEATED_BY_COUNTEREXAMPLE`,  
and `HAS_SBQ_STANDING`. A score never silently becomes semantic standing.

This integration establishes four editorial commitments: adopt multidimensional binding-quality diagnostic as SBQ's official corpus role; adopt the assessment envelope; prohibit universal scalar aggregation without a declared decision profile; and require Goodhart, residual, and cross-jurisdiction tests before operational use.

## Quality-Gated Atlas Maintenance Without Quality Sovereignty

The fixed-seed comparison with GCNL, GTK, Governed Semantic Cartography, and Semantic Debt places SBQ inside a governed assessment chain:

$$
\begin{aligned}
Q= (&binding, identity, proposal\_context, views, profile, \\
&dimension\_vector, perturbations, results, debt\_signals, \\
&decision\_ceiling, revision)
\end{aligned}.
$$

GCNL supplies the bounded proposal context and residual meaning; GTK supplies the identity under assessment. These must be fixed before a quality result is interpreted. A high score cannot establish that the right occurrence was bound, and a low score cannot silently replace, split, or retire a GTK.

Cartographic projections provide valuable perturbations. A binding that appears coherent in one view may fragment under another projection, evidence cut, standing cut, or traversal path. Cross-view robustness is evidence about a declared profile, not proof that one projection is neutral or complete. Default views must not become the training target that defines quality circularly.

Semantic Debt receives SBQ findings only through an explicit obligation decision. A failed quality expectation can be a defect, risk, legitimate disagreement, irreducible complexity, or debt. It becomes debt only when a declared obligation remains unresolved or materially harder to discharge while continuation is permitted under a recorded posture.

SBQ may recommend review, comparison, or remediation. It cannot itself change a registry, atlas route, debt status, standing, admission, or effect permission. The universal GSM can type   
`ASSESSES_IDENTIFIED_BINDING`,  
`PERTURBS_ACROSS_ATLAS_VIEW`, `REPORTS_DIMENSION_VECTOR`, `SIGNALS_POSSIBLE_SEMANTIC_DEBT`,  
`REFUSES_SCALAR_SOVEREIGNTY`, `REQUIRES_OBLIGATION_DECISION`, and `REVISES_SBQ_PROFILE`.

This randomized review establishes four editorial commitments: bind every SBQ assessment to lexical identity and proposal context; test quality across declared atlas projections; separate quality failure from semantic-debt admission; and prohibit SBQ from changing identity, standing, registry state, or permission by score.

## Identity-Bound Quality Without Quality Sovereignty

Fourteen downstream uses confirm SBQ as a diagnostic profile applied after subject identity, purpose, and jurisdiction are fixed. It evaluates controlled-language proposals, atlas views, context bindings, human-review cases, semantic mappings, meaning relations, field analyses, debt conditions, and consciousness-research models. The uses repeatedly refuse the same promotion: quality does not decide identity, admission, truth, authority, phenomenality, or canonical standing.

The evaluation object should be:

$$
\begin{aligned}
Q^*= (&subject\_identity, binding\_profile, purpose, \\
&jurisdiction, observers, dimensions, denominators, \\
&perturbations, baselines, uncertainty, tradeoffs, \\
&evidence, ceiling, expiry, reassessment)
\end{aligned}.
$$

Coherence, generativity, stability, constraint alignment, and distortion must be reported as a vector with declared denominators and counterexamples. No scalar can compensate for a mandatory constraint failure or erase a minority meaning. A high score can describe a stable but false, illegitimate, harmful, or overfit binding; a low score can identify a fragile representation without authorizing an identity split.

Goodhart testing should vary prompts, observers, projections, translations, user groups, task contexts, perturbation families, and adversarial optimization against the metric. Results expire when identity, profile, purpose, evidence, or the population of relevant cases changes. Dependents should cite an exact SBQ generation rather than the framework name.

The universal GSM can type   
`EVALUATES_BINDING_QUALITY`, `BINDS_QUALITY_TO_IDENTITY`,  
`FAILS_MANDATORY_QUALITY_DIMENSION`, `PERTURBS_BINDING_PROFILE`, `GOODHARTS_QUALITY_METRIC`,  
`EXPIRES_QUALITY_RESULT`, and   
`DOES_NOT_GRANT_SEMANTIC_STANDING`.

This reverse-dependency review establishes four editorial commitments: adopt the identity- and purpose-bound evaluation object; retain a noncompensatory quality vector; require adversarial Goodhart and cross-observer testing; and prohibit SBQ from deciding identity, admission, truth, authority, or phenomenal claims.

## 11. Counterevidence and Goodhart Risks

SBQ should be narrowed or rejected where: (1) evaluators cannot agree on relation identity; (2) dimensions collapse contested values into technical scores; (3) generativity rewards prolific falsehood; (4) stability rewards entrenchment; (5) coherence suppresses legitimate anomaly; (6) constraint alignment preserves defective constraints; (7) minimal distortion favors dominant ontologies; (8) centrality becomes circular evidence of quality; (9) simulated perturbations do not predict real revision; (10) metrics are gamed; (11) missing evidence is treated as zero rather than unknown; (12) scores travel outside their jurisdiction; (13) temporal drift invalidates old profiles; (14) minority meanings are penalized; (15) evaluator authority is hidden; (16) scalar aggregation reverses dimension-level judgments; or (17) SBQ adds no predictive value beyond explicit evidence and ordinary graph diagnostics.

Evaluation requires annotated bindings, multiple adjudicators, profile-specific tasks, uncertainty, inter-rater variation, perturbation protocols, prospective predictions, counterexample retention, fairness analysis, Goodhart attacks, and comparison with simpler baselines. No such validation is present here.

## Quality Must Not Become Semantic Sovereignty

### Public orientation

Semantic Binding Quality evaluates an already identified binding for a declared purpose and jurisdiction across dimensions such as coherence, generativity, perturbation behavior, constraint alignment, distortion, resilience, contestability, and explanatory value. It is a diagnostic vector, not a universal score and not an authority that decides which meanings are true, legitimate, canonical, or allowed to exist.

### Adversarial tests

1. **Generativity-falsehood attack.** A binding receives high quality because it produces many derivations, even when those derivations are false or harmful.
2. **Stability-entrenchment attack.** Social power, path dependence, institutional lock-in, or repeated copying is scored as robust meaning.
3. **Coherence-suppression attack.** An anomaly, dissent, minority interpretation, or novel evidence is penalized for disrupting the dominant network.
4. **Constraint-defect attack.** Alignment with an unjust, obsolete, incomplete, or unauthorized constraint increases the score.
5. **Scalar-compensation attack.** Strong performance on convenient dimensions hides failure of a mandatory safety, authority, fidelity, or fairness dimension.
6. **Evaluator-sovereignty attack.** Hidden profile designers, raters, or model judges gain power to define good meaning without jurisdiction or contest.
7. **Metric-Goodhart attack.** Agents optimize prompts, projections, terminology, and graph structure for the measured dimensions rather than the intended semantic quality.
8. **Quality-travel attack.** A result outlives its identity, purpose, evidence, observers, perturbation family, or relevant population and is reused elsewhere.

### Claim and evidence ceiling

SBQ is a claim-relative, identity-bound, noncompensatory quality diagnostic. It does not establish truth, authority, admissibility, standing, identity, phenomenality, moral value, or universal quality. High SBQ can describe a stable false or harmful binding; low SBQ does not authorize deletion, rejection, or identity split.

The dimensions, indicators, evaluator agreement, perturbation validity, fairness, predictive value, and benefit over simpler evidence and graph diagnostics require external scholarship and empirical validation. No dataset, metric, campaign, or domain study was added in this pass.

### Reader-facing consequence

The public benefit is a transparent quality profile that shows why a binding appears useful or fragile, who defined the test, which failures cannot be averaged away, and when the result expires - without turning quality scoring into control over meaning.

## 13. Corpus Integration Sources

This pass used exact heads for GTK, GOORRT, Semantic Fragmentation, Constitutional Semantic Engineering, Admissibility Engineering, Reasoning by Way of Receipts, and GMB semantic-manifold documentation. Their hashes are bound in the custody manifest. Comparison creates no identity merger, quality judgment, implementation, or standing.

## 14. Conclusion

The relational ontology of meaning identifies bindings as the fundamental units of semantic structure. However, the existence of a binding does not guarantee its integrity.

This paper introduces **Semantic Binding Quality (SBQ)** as a framework for evaluating the structural integrity of semantic relations.

Bindings vary along dimensions such as structural coherence, generativity, stability under perturbation, constraint alignment, and minimal distortion. These dimensions together determine the degree to which a binding can serve as a stable foundation for knowledge systems.

Constitutional computational substrates demonstrate that philosophical insights about meaning can be encoded directly within computational architectures. By formalizing SBQ, future systems may be able to evaluate and improve the quality of semantic structures within both human and machine knowledge systems.

Understanding and optimizing semantic binding quality may therefore represent a critical step toward more robust knowledge infrastructures and more coherent computational environments.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

---

## Editorial Provenance and Standing

### Source, Evidence, and Standing
This is an AI-prepared successor revision candidate derived from one exact author manuscript. The integration custody manifest is   
`work/paper-saturation-v1/evidence/semantic-`

`binding-quality/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`B7981763C8C05CBE13CD2084F52F83332C56A6F2766D1A36B22285FFB84527D9`. The exact source remains unchanged. The binding-quality thesis, five proposed dimensions, semantic-energy and attractor analogies, historical constitutional-substrate examples, configuration/implementation argument, indicators, implications, and conclusion are author material. This pass makes SBQ a claim-relative vector rather than an ungrounded universal score, separates quality from truth, authority, popularity, stability, and admissibility, moves current architecture prose from historical CCF to GMB, places quality selection in CM2 after CM1 admissibility, and adds counterevidence and open editorial questions. Those additions are AI editorial or synthetic contributions until adopted.
No metric, dataset, evaluator, perturbation campaign, or domain study was executed. The source's scientific, legal, mathematical, networking, and narrative examples were not externally assessed. No publication, canonical standing, identity merger, conformance assignment, quality certification, or implementation authority is granted.

## Corpus-Wide Reference Positioning

This paper argues that if meaning emerges through relational bindings between structures, the mere presence of a binding does not guarantee semantic integrity. Its nearest external comparison fields are semantic, provenance, security. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E7]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

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

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constitutional Semantic Engineering.* Zenodo, 2026. doi:10.5281/zenodo.21111455

Adam Ableman *Semantic Debt.* Zenodo, 2026. doi:10.5281/zenodo.21111666

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848209](https://doi.org/10.5281/zenodo.23848209)
