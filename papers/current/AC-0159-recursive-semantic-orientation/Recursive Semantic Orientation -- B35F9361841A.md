# Recursive Semantic Orientation

## A Bounded Method for Building and Revising Working Models of Complex Systems

### Recursive Semantic Orientation (RSO) is a proposed method for acquiring a usable position within that complexity before pursuing exhaustive detail.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Complex systems often exceed the working memory of an investigator or agent because their components, relations, states, boundaries, and unknowns cannot be held together at once. Recursive Semantic Orientation (RSO) is a proposed method for acquiring a usable position within that complexity before pursuing exhaustive detail.

The source method moves from hypothesis to coarse semantic partition, recursive refinement, verification, pattern discovery, focused search, and repetition. This paper preserves that architecture while narrowing its strongest claims. Complexity is not exclusively relational, all inquiry does not begin with an explicit hypothesis, and decomposition does not guarantee a simple or unique explanation. Partitions can conceal cross-cutting relations; familiar patterns can create confirmation bias; deferred retrieval can postpone critical evidence.

RSO is therefore specified as a governed, graph-aware orientation loop. It maintains hypotheses, partitions, unknowns, evidence, questions, budgets, countermodels, and stopping conditions. It supports observation-led as well as hypothesis-led entry, searches for disconfirming evidence, and distinguishes a useful working model from truth, decision authority, or implementation readiness.

## Source, Credit, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. The custody and comparison manifest is   
`work/paper-saturation-v1/evidence/recursive-`

`semantic-orientation/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`0B79867D410C23B591DF53AFF2B516789427E1864748BFDD467FDDB5F87943B5`. The source remains unchanged.

The source credits Alisa Esage and links two videos. This pass preserves that credit as source material but did not inspect the videos, infer endorsement, or perform external research. RSO and its named principles are author material. Formal boundaries, integrations, evaluation design, countertests, and open editorial questions added here are AI editorial or synthetic candidates until adopted.

## 1. The Orientation Problem

An investigator approaching an unfamiliar codebase, institution, device, mathematical theory, or distributed system does not initially possess the model needed to interpret every observation. Retrieval alone can enlarge the unorganized mass. Premature local analysis can hide system-level causes. A first task is to construct enough semantic position to choose the next useful observation.

RSO calls this **orientation before analysis**. Orientation is not prior knowledge of the whole system. It is a provisional account of scope, abstraction level, knowns, unknowns, relevant relations, risks, and next questions.

The aphorism "complexity is relational, not numerical" captures an important contrast between many independent items and a few tightly coupled ones. It should not be treated as a universal definition. Scale, heterogeneity, dynamics, uncertainty, computational hardness, feedback, and observer limits may also contribute to difficulty.

## 2. Orientation State

At time $t$, define an orientation state:

$$
O_t=(S_t,H_t,P_t,U_t,E_t,Q_t,C_t,B_t),
$$

where $S_t$ is scoped subject matter, $H_t$ hypotheses or candidate models, $P_t$ semantic partitions and cross-links, $U_t$ explicit unknowns, $E_t$ evidence and provenance, $Q_t$ open questions and counterquestions, $C_t$ constraints and consequences, and $B_t$ the available time, attention, compute, access, and risk budget.

An orientation update is admissible only when it records what changed, why it changed, which observations support it, what alternatives remain, and which claims exceed the evidence.

## 3. A Flexible Recursive Loop

A bounded RSO episode can proceed as follows:

1. **Scope and position:** identify the subject, task, abstraction level, effect boundary, and stakes.
2. **Sample and observe:** inspect a small but informative set of source-native structures.
3. **Propose models:** form provisional hypotheses, analogies, and partitions.
4. **Name unknowns:** record missing components, relations, transitions, evidence, and jurisdictions.
5. **Map topology:** represent hierarchy, adjacency, dependency, feedback, cycles, exceptions, and cross-cutting concerns.
6. **Test and countertest:** seek supporting, disconfirming, surprising, and out-of-distribution observations.
7. **Retrieve selectively:** acquire documentation or detail when its expected information value exceeds its cost and risk.
8. **Refine or replace:** split, merge, connect, qualify, or discard the current model.
9. **Stop, act, or recurse:** terminate at task-relative sufficiency, proceed under an explicit claim ceiling, or open another cycle.

These operations need not occur in one fixed order. Observation may precede hypothesis. An urgent safety fact may require immediate retrieval. A discovered cross-link may dissolve an earlier partition.

## 4. Coarse Semantic Partitioning

Coarse Semantic Partitioning (CSP) creates large provisional regions such as identity, authority, state, evidence, execution, policy, storage, communication, and unknown. The purpose is navigation, not ontological truth.

A partition should carry its basis, exclusions, confidence, and cross-boundary edges. Because real systems are frequently graphs rather than trees, a component may participate in several regions. Authentication may concern identity, authority, evidence, user experience, and recovery simultaneously.

The useful principle is therefore: structure can precede exhaustive detail, but the first structure remains revisable.

## 5. Explicit Unknowns

Unknowns should be represented as first-class objects rather than omitted or prematurely classified. An unknown record should include location, relation candidates, uncertainty type, consequence if wrong, investigative priority, access limits, and closure evidence.

A named unknown is partially oriented but not necessarily understood. Naming can also create false confidence. The registry must distinguish unknown, unknowable under present access, contested, withheld, not applicable, and not yet investigated.

## 6. Hypotheses, Observations, and Countermodels

Hypotheses guide attention by predicting structures, relations, and failure modes. They do not possess primacy in every inquiry. An observation-led survey, anomaly, user report, or random sample can precede an explicit model.

Every active hypothesis should have:

- observations it explains;
- expected observations not yet found;
- a plausible alternative;
- evidence that would weaken or defeat it;
- the jurisdiction within which it applies; and
- a confidence and revision history.

This preserves the source insight that invalid framing can produce low-value investigation without asserting that one initial hypothesis governs all exploration.

## 7. Pattern-Constrained and Novelty Search

Known patterns make search efficient: a credential path, deployment gate, bus, cache, authority boundary, or state machine has recognizable signatures. But expected-pattern matching can make investigators see only familiar structures.

RSO should pair pattern-constrained search with **novelty search** and **counterpattern search**. For every expected match, ask what structurally different mechanism could produce the same observation, what evidence should be present but is absent, and where the system violates the analogy.

Search is then neither exhaustive wandering nor recognition alone. It is a contest among model-guided, novelty-seeking, and disconfirming probes.

## 8. Retrieval and Detail Timing

Deferred detail acquisition protects working memory when retrieval would overwhelm a weak model. It is not an absolute sequence. Security advisories, interface contracts, destructive-operation warnings, authoritative specifications, or incident evidence may need immediate attention.

Retrieve when expected decision relevance, information gain, consequence reduction, or uncertainty reduction justifies the cost. Defer when material is low-value, duplicative, inaccessible, or likely to collapse the current abstraction level without improving the task.

## 9. Recursive Refinement and Topology

Each region can become the subject of another orientation episode. Refinement may descend through subsystems, but it may also move sideways across adjacencies or upward to a broader constraint. Cycles and feedback mean the method is not merely recursive decomposition.

The topology should retain at least containment, dependency, control, authority, evidence, temporal order, translation, conflict, exception, and uncertainty relations. A hierarchy that omits these edges can appear clear while being operationally false.

## 10. Sufficiency and Stopping

"Explanatory power stabilizes" and "diminishing returns" require observable criteria. Let continuation value be:

$$
V_t=G_t-(K_t+R_t),
$$

where $G_t$ is expected information or decision gain, $K_t$ is investigation cost, and $R_t$ is the risk of delay, error, or intervention. Continue when $V_t$ remains positive or a critical unknown lacks closure.

A task may stop when coverage is adequate for the declared purpose, critical unknowns are bounded, alternatives have been tested, consequences are acceptable, evidence is traceable, and another cycle has low marginal value. A stopped orientation is a task-relative working model, not complete truth.

## 11. Simplicity and Architectural Attractors

Recursive inquiry can reveal invariants and compress many observations into a simpler model. It can also expose irreducible pluralism, path dependence, conflicting objectives, or chaotic dynamics. Simplicity is an achievement to test, not an inevitable destination.

Likewise, systems under similar constraints may converge on recurring structures, but common vocabulary or shape does not prove common mechanism, identity, optimality, or necessity. An architectural-attractor claim needs a comparison class, stated constraints, independent cases, alternative explanations, and evidence of convergence.

Ableman's Razor can guide model selection only under preserved explanatory coverage, visible remainder, and explicit cost. Compression that erases a failure path is not simplicity.

## 12. Agent Capability Surface

An agentic implementation may expose `able_orient`, `able_partition`, `able_hypothesize`,  
`able_gap`, `able_refine`, `able_trace`, `able_surface`, `able_claim`, `able_refute`,  
and `able_validate`. Each operation should declare:

- accepted source and state identities;
- input and output schema;
- evidence and provenance obligations;
- authority and effect ceiling;
- uncertainty and remainder;
- resource budget;
- refusal and escalation outcomes; and
- revision relation to prior state.

An orientation operation cannot silently become permission to execute. A validation operation must identify the profile and evidence under which it validates.

## 13. Corpus Integration

RSO provides the iterative orientation workflow. **The Well-Governed Mind** supplies cognitive governance and self-revision. **A Constitution for the Context Window** governs admitted context. **Governed Semantic Cartography** maps semantic territories and boundaries. **Semantic Field Analysis** analyzes relations and tensions within a field. **Semantic Manifold Topology** supplies multi-relational topology. **Meaning Crystals** package bounded semantic state for transport and reconstruction.

The **Governed Meaning Base (GMB)** can retain sources, orientation states, hypotheses, partitions, unknowns, evidence, countermodels, stop reasons, and revisions. The universal **GSM** can type their relations without treating a lexical match as identity or a working model as truth.

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

- **Possibility:** enumerate hypothesis-led, observation-led, graph, hierarchical, human, agent, and hybrid orientation methods.
- **Specification:** define state, operations, provenance, budgets, outcomes, and stop rules.
- **CM1:** retain admissible workflows, including costly, incomplete, and high-uncertainty variants.
- **CM2:** prefer configurations by fidelity, information gain, safety, accessibility, inspectability, and cost.
- **IC:** select an Instance Constitution or Instance Configuration for one investigative setting.
- **IR:** build an Instance Realization or Implementation Realization of the chosen workflow and capability surface.
- **Evidence:** compare orientation quality, errors, effort, transfer, and downstream decisions.
- **Revision:** update the method, configuration, and implementation from receipts and failures.

This paper reaches Specification and proposes criteria for CM1 and CM2. It does not select an IC or certify an IR. Here IR means realization, not Intermediate Representation as in MCIR or Context IR.

## 15. Evaluation Program

Evaluate RSO on bounded unfamiliar systems against unguided exploration, documentation-first retrieval, and expert-chosen baselines. Use tasks with known architecture, hidden cross-links, misleading patterns, critical unknowns, and consequence-bearing decisions.

Measure time to a useful map, coverage of critical relations, unknown recall, calibration, false structure, hypothesis revision, disconfirmation rate, source traceability, transfer to a second task, decision quality, cognitive or token cost, and harm from delayed retrieval. Separate human, agent, and collaborative results.

## The Revisable Orientation-Control Loop

Across the completed P1 corpus, Recursive Semantic Orientation (RSO) has one non-duplicative role: it is the **revisable orientation-control loop** that decides how an investigator builds, challenges, and updates a working position within an unfamiliar system. It is not the semantic terrain, the stored knowledge base, a cartographic projection, a truth engine, or permission to act.

- **Adjacent work:** *The Well-Governed Mind*  
  **Supplies:** Cognitive governance, self-correction, and bounded stopping.  
  **RSO boundary:** RSO supplies the explicit investigation loop and state record.

- **Adjacent work:** *A Constitution for the Context Window*  
  **Supplies:** Admission and displacement rules for active context.  
  **RSO boundary:** Context is one input to orientation; a context window is not the full orientation state.

- **Adjacent work:** *Governed Semantic Cartography*  
  **Supplies:** Coordinates, projections, traversals, and atlas coherence.  
  **RSO boundary:** A map supports orientation but does not determine the investigator's hypotheses, unknowns, or stopping decision.

- **Adjacent work:** *Semantic Field Analysis*  
  **Supplies:** Analysis of relations, tensions, pressures, and gaps in a bounded semantic field.  
  **RSO boundary:** Field analysis is one probe family within or downstream of an orientation episode.

- **Adjacent work:** *Meaning Crystals*  
  **Supplies:** Portable, reconstructable packages of bounded semantic state.  
  **RSO boundary:** A crystal can carry an orientation snapshot; portability does not make the snapshot true or complete.

The portable control object is:

$$
O_t=(scope,H_t,P_t,U_t,E_t,Q_t,C_t,B_t,ceiling_t),
$$

where hypotheses, provisional partitions, unknowns, evidence, questions, constraints, budget, and claim ceiling are independently represented. A governed update has the form:

$$
\begin{aligned}
&Step(O_t,probe,result,receipt) \\
&\rightarrow O_{t+1} \\
&\mid Stop \\
&\mid Refuse \\
&\mid Escalate
\end{aligned}.
$$

Custody and revision lineage should be monotonic even when beliefs are not: a defeated hypothesis may be removed from the active model while its source, test, defeat reason, and downstream influence remain reconstructable. Likewise, an omitted observation is not an explicit unknown, and an explicit unknown is not evidence of absence.

Five objects remain distinct: **source state** is what was inspected; **orientation state** is the investigator's bounded working position; **map or projection** is a rendering used for navigation; **hypothesis** is a defeasible explanatory candidate; **standing** is a governed assessment of a claim. A decision or external effect may consume these objects but is not identical to any of them.

The universal GSM can type `ORIENTS_TO`, `PARTITIONS_AS`, `TRACKS_UNKNOWN`,  
`PROPOSES_HYPOTHESIS`, `COUNTERMODELED_BY`, `PROBED_BY`, `UPDATED_BY`, `PROJECTED_THROUGH`,  
`STOPPED_UNDER`,  
and   
`EXCEEDS_CLAIM_CEILING`. A GMB can preserve their versions and custody; it does not silently promote a working orientation to corpus truth.

This integration establishes four editorial commitments: adopt revisable orientation-control loop as RSO's official corpus role; adopt the portable state/update contract; require monotonic custody rather than monotonic belief; and preserve the five-object non-collapse rule across human and agent implementations.

## Perspective-Aware, Attractor-Challenged, Authority-Bounded Orientation with Change-Carriage Accounting

The fixed-seed comparison with The Locus of Shared Experience, Semantic Gravitational Attractors, Split-Authority AI Coordination, and transformation-dominant semantic systems expands an orientation episode without turning it into execution governance:

$$
\begin{aligned}
O_t^*= (&scope, hypotheses, partitions, unknowns, evidence, \\
&questions, constraints, perspectives, permissions, \\
&attractor\_risks, authority\_role, change\_carriage, \\
&budget, claim\_ceiling)
\end{aligned}.
$$

Shared-experience bridges require participant-indexed orientation states, directional access, correction, refusal, and withdrawal. The investigator's model of another participant is not that participant's experience or authority. Semantic attractors can stabilize terminology and navigation while also creating confirmation pressure, false convergence, and silent remainder loss.

Split-Authority AI Coordination determines who may propose, revise, verify, admit, or act upon an orientation state. A capable investigator or agent cannot self-grant effect authority. Transformation-dominant diagnostics record what an orientation update changes, carries, discloses as lost, leaves unresolved, and costs to preserve.

A valid stop therefore requires more than local coherence. It should state satisfied questions, unresolved high-consequence unknowns, untested countermodels, remaining participant permissions, attractor exposure, authority limits, and the semantic delta from the predecessor orientation.

The universal GSM can type   
`ORIENTS_UNDER_PARTICIPANT_PERMISSION`,  
`PRESERVES_PERSPECTIVE_DIFFERENCE`, `CHALLENGES_SEMANTIC_ATTRACTOR`,  
`UPDATED_BY_AUTHORIZED_ROLE`, `CARRIES_ORIENTATION_OBLIGATION`,  
`DISCLOSES_ORIENTATION_LOSS`, and   
`STOPS_WITH_EXPLICIT_REMAINDER`.

This randomized review establishes four editorial commitments: adopt the expanded orientation state; preserve participant perspectives and permissions; require attractor countertests and dimension-specific authority; and add semantic change-and-carriage accounting to every material orientation update and stop.

## Versioned Orientation as a Non-Authoritative Control State

Nine downstream uses place Recursive Semantic Orientation between governed knowledge and action without making it an authority source. Context compilation and CCM consume an orientation to request or select bounded context. CogK schedules probes and evaluates sufficiency. Semantic Cartography supplies governed views. Semantic attractors require counterorientation. Split-authority roles may hold different orientation states. GKL uses orientation without granting mutation authority. Shared-experience work keeps participant perspectives distinct. TDSS tracks obligation carriage when orientation changes.

The downstream-stable orientation state is:

$$
\begin{aligned}
O= (&subject, purpose, role, perspective, source\_cut, \\
&hypotheses, countermodels, knowns, unknowns, partitions, \\
&attractors, probes, evidence, claim\_ceilings, stopping, \\
&expiry, predecessor, remainder)
\end{aligned}.
$$

An orientation update should state what was preserved, refined, defeated, dropped, or left unresolved. It may change context requests, search paths, and attention without changing mandate, identity, evidence standing, or effect authority. Different roles and participants may retain incompatible but valid orientation branches; convergence is an outcome to test, not a requirement.

Counterorientation should deliberately sample excluded regions, minority hypotheses, low-connectivity concepts, contrary evidence, and alternative equivalence regimes. Expiry is dimension-specific: new evidence may stale one hypothesis while leaving the source cut or purpose current. Stopping should preserve the frontier and the reason further search was not justified, rather than narrating temporary sufficiency as semantic closure.

The universal GSM can type   
`HOLDS_ORIENTATION_FOR_ROLE`,  
`BRANCHES_PERSPECTIVE_ORIENTATION`, `REQUESTS_CONTEXT_FROM_ORIENTATION`,  
`UPDATES_WITH_CARRIAGE_RECORD`, `COUNTERORIENTS_AGAINST_ATTRACTOR`,  
`EXPIRES_ORIENTATION_DIMENSION`, `STOPS_WITH_FRONTIER_REMAINDER`,  
and   
`DOES_NOT_GRANT_MUTATION_OR_EFFECT_AUTHORITY`.

This reverse-dependency review establishes four editorial commitments: adopt the versioned orientation state; preserve role and perspective branches; require counterorientation and change-carriage records; and keep context, mutation, mandate, and effect authority outside orientation itself.

## 16. Counterevidence and Failure Modes

The proposal should be narrowed or rejected where: (1) complexity is defined only by relations; (2) scale or dynamics are ignored; (3) intimidation is assumed universal; (4) orientation delays urgent evidence; (5) all inquiry is called hypothesis-first; (6) observations are forced into initial frames; (7) partitions erase cross-cutting relations; (8) hierarchy replaces graph topology; (9) named unknowns acquire false closure; (10) unknown and withheld are conflated; (11) uncertainty is uncalibrated; (12) familiar patterns create confirmation bias; (13) novelty search is absent; (14) analogies substitute for mechanism; (15) deferred retrieval hides authoritative warnings; (16) refinement loops indefinitely; (17) stopping criteria are subjective only; (18) simplicity erases exceptions; (19) one explanatory model is presumed; (20) attractors are inferred from anecdotes; (21) convergence is confused with optimality; (22) source credit is treated as endorsement; (23) linked material is cited without review; (24) orientation becomes execution authority; (25) agent operations lack schemas; (26) validation lacks a profile; (27) GMB inclusion becomes truth; (28) GSM edges imply causation; (29) corpus interfaces are merged; (30) a specification is presented as implemented; (31) measured performance does not improve; or (32) external research contradicts universality or novelty claims.

## Orientation Is a Revisable Control State, Not a View From Nowhere

### Public orientation

Recursive Semantic Orientation builds a usable position inside a complex system before exhaustive analysis. It maintains scope, hypotheses, partitions, unknowns, evidence, questions, constraints, countermodels, and budgets through recursive refinement. The result is a working orientation state: useful for choosing the next observation, never identical to the system or automatically authoritative over it.

### Adversarial tests

1. **Partition-blindness attack.** Coarse categories hide cross-cutting relations, feedback, boundary objects, minority cases, and coupled failures.
2. **Hypothesis-lock attack.** The initial frame determines what is noticed, retrieved, and classified, producing an increasingly coherent but false model.
3. **Pattern-familiarity attack.** Known architectures and corpus concepts crowd out novel structure and counterevidence.
4. **Deferred-evidence attack.** Orientation-before-detail postpones a decisive source, observation, stakeholder, or safety fact until after the model has hardened.
5. **Compression-loss attack.** Repeated summaries erase qualifiers, conflicts, low-frequency hazards, provenance, or uncertainty.
6. **Stopping-prematurity attack.** A usable model, reduced surprise, or stable vocabulary is mistaken for completeness or truth.
7. **Perspective-erasure attack.** One investigator's purpose and access become the system's natural boundary while affected or local perspectives disappear.
8. **Orientation-authority attack.** A model chosen for navigation begins to govern decisions, implementation, or people without a separate authority and evidence gate.

### Claim and evidence ceiling

The paper specifies a governed orientation loop and evaluation program. It does not establish that complexity is purely relational, that every inquiry begins with a hypothesis, that recursive decomposition finds a unique simple architecture, or that RSO improves accuracy, speed, transfer, safety, or agent performance. Source credit is preserved; linked videos were not inspected.

Evaluation requires exact task and perspective profiles, competing orientation methods, blind downstream tests, countermodel discovery, compression-loss audits, stopping calibration, affected-perspective review, and current external research. No external research or evaluation was performed in this pass.

### Reader-facing consequence

RSO is successful when it helps an investigator know what model they are currently using, what it omits, which evidence could overturn it, whose perspective it reflects, and which next observation is worth the cost - without pretending orientation is final understanding.

## 18. Conclusion

Recursive Semantic Orientation is best understood as a disciplined way to build, test, and revise a working position within complexity. It begins with bounded scope and provisional structure, preserves unknowns and alternatives, moves across hierarchy and graph relations, retrieves detail when useful, and stops relative to a declared task and risk.

Its aim is not to make every complex system simple. Its aim is to make the investigator's present model explicit enough to challenge, improve, use cautiously, and revise.

## Reference and Verification Note

No external source or linked video was reviewed in this pass. Further evidentiary strengthening requires authorized primary-source research across complex-systems theory, cognitive science, human factors, information foraging, scientific method, debugging, software architecture, search and information retrieval, graph cognition, hypothesis testing, agent evaluation, and the credited methodology.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Instance Configuration.** The present paper does not claim a complete instance configuration treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that complex systems often exceed the working memory of an investigator or agent because their components, relations, states, boundaries, and unknowns cannot be held together at once. Its nearest external comparison fields are semantic, ai, formal. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** Patrick Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **Relationship:** Predecessor retrieval architecture; comparison centers on provenance, admission, and fail-closed constraints not supplied by retrieval alone.

**[E7]** Shunyu Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. arXiv:2210.03629. https://arxiv.org/abs/2210.03629 **Relationship:** Predecessor agent pattern for interleaving reasoning and action; used to distinguish action traces from governed effects.

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

**[A6]** Adam Ableman. *CARA: Constrained Artificial Reasoning Architecture*. Ableman Corpus current edition; work identity `PAPER.PUB.18099715`;  
source SHA-256  
`F8F74F0CD58F5414D9A29EBE958E49751892D07A028CB51197F8201B18AAB40E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *A Constitution for the Context Window*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-CF26BA0E123F472F`;  
source SHA-256  
`60395402368E146F115CCE53D0E5A15B8FB23C90ED5B24CA92AB8515B2009965`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

DOI: [10.5281/zenodo.23848199](https://doi.org/10.5281/zenodo.23848199)
