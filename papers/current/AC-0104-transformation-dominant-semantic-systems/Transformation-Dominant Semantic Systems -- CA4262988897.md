# Transformation-Dominant Semantic Systems

## A Two-Axis Morphology of Semantic Change and Obligation Carriage

### Transformation and conservation should not be treated as mutually exclusive operation classes.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern semantic systems can generate, translate, summarize, recombine, and propagate meaning at great speed while failing to preserve source, identity, authority, uncertainty, scope, or other commitments across those transformations. This paper proposes a morphology for diagnosing that asymmetry.

Transformation and conservation should not be treated as mutually exclusive operation classes. A large semantic change can faithfully carry declared obligations; a nearly verbatim copy can sever provenance or authority. The revised model therefore uses two independent axes: semantic delta and obligation carriage. Conservation is a profile-relative property of a transformation, not simply a separate kind of operation.

The paper defines a semantic-carriage envelope, typed preservation outcomes, transformation and carriage measures, failure patterns, and an empirical comparison program. It treats hallucination, semantic drift, and institutional incoherence as possible consequences of weak conservation among several competing explanations, not as established products of one architectural imbalance. It connects the diagnostic morphology to Constraint-Bearing Composability, Meta-Binding, Epistemic Lineage, Governance as Compilation, the Governed Meaning Base, and the universal GSM without merging their roles.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. The custody and comparison manifest is   
`work/paper-saturation-v1/evidence/`

`transformation-dominant-semantic-systems/`  
`integration-custody-manifest.v0.1.json`,  
SHA-256  
`7BF649A2BC481C4F8E1DF345D30D4775C8BF13B7CEC6A861DFA013DE15B8C14F`. The source remains unchanged.

The distinction, asymmetry hypothesis, metaphors, examples, predictions, and limitations are author material. Formalization, corpus integration, counterevidence, evaluation, and decisions added here are AI editorial or synthetic candidates until adopted. No system is classified or certified by this paper.

## 1. The Diagnostic Problem

Generation quality and semantic continuity are different achievements. A system can produce novel, coherent language while losing where a claim came from, how certain it was, who authorized it, which scope it occupied, or what transformation changed it. Conversely, a rigid archive may preserve bytes while failing to preserve interpretation, applicability, or living revision.

The useful question is not whether a system transforms or conserves. Every operational semantic system does both to some degree. The question is which commitments it carries, under what profile, across which transformation, with what evidence and loss.

## 2. Two Independent Axes

Let $s$ be an input semantic artifact and $\tau(s)=s'$ an output. Define:

$$
M_p(\tau,s)=(\Delta_p(s,s'),C_p(\tau,s)),
$$

where $\Delta_p$ is semantic change under comparison profile $p$, and $C_p$ is carriage of obligations declared relevant by $p$.

This yields four important regions:

- **Semantic delta:** high  
  **Obligation carriage:** high  
  **Interpretation:** faithful translation, synthesis, or migration

- **Semantic delta:** high  
  **Obligation carriage:** low  
  **Interpretation:** transformative drift or unsupported invention

- **Semantic delta:** low  
  **Obligation carriage:** high  
  **Interpretation:** conservative reproduction with preserved context

- **Semantic delta:** low  
  **Obligation carriage:** low  
  **Interpretation:** superficial copying with broken identity, authority, or provenance

The table is analytical, not a universal ontology. Delta and carriage depend on task, artifact type, observer, and declared commitments.

## 3. Semantic-Carriage Envelope

For a transformation, define an envelope:

$$
E_{\tau}=(I,S,P,A,K,U,R,X,W),
$$

where $I$ is input and output identity, $S$ source and lineage, $P$ transformation profile, $A$ authority and standing, $K$ obligations or invariants expected to carry, $U$ uncertainty and unresolved remainder, $R$ declared revisions and losses, $X$ effect boundary, and $W$ evidence and witnesses.

Each obligation receives one typed outcome: `PRESERVED`, `REFINED`, `WEAKENED`,  
`STRENGTHENED`, `TRANSLATED`, `DROPPED`, `CONFLICTED`, `NOT_APPLICABLE`,  
or `UNKNOWN`. A transformed artifact is conservation-adequate only relative to the accepted outcomes of its profile.

This prevents "same meaning" from hiding legitimate change and prevents fluent output from hiding lost commitments.

## 4. What Counts as Semantic Transformation

Candidate transformation operations include paraphrase, translation, summarization, abstraction, synthesis, decomposition, inference, recombination, migration, normalization, and contextual adaptation. Their labels do not determine their behavior.

A translation can preserve a proposition while changing connotation or legal effect. A summary can preserve a thesis while omitting a decisive exception. A normalization can preserve data values while erasing ordering or source identity. Classification must therefore inspect the envelope and domain profile, not assign permanent morphology to the operation name.

## 5. What Conservation Preserves

Conservation can concern different objects:

- byte, token, or structural identity;
- proposition or defined concept;
- constraint, invariant, or refusal;
- provenance and epistemic lineage;
- authority, jurisdiction, and standing;
- uncertainty, disagreement, and alternatives;
- dependency and version relation;
- effect boundary and permitted use; or
- reconstructability and audit evidence.

Preserving one does not preserve all. Cryptographic identity can prove byte continuity without truth or authority. A paraphrase can conserve a claim without conserving evidence. A legal restatement can conserve wording while changing application.

## 6. Transformation Dominance

A system is transformation-dominant under profile $p$ when its capacity or rate of semantic change substantially exceeds its demonstrated ability to carry the obligations relevant to its uses. This is task-relative, not a stable essence of the substrate.

Let $T_p$ summarize useful transformation capacity and $Q_p$ summarize verified carriage quality. A provisional imbalance indicator is:

$$
D_p=\frac{T_p}{\epsilon+Q_p},
$$

with $\epsilon>0$ preventing division by zero. The indicator is meaningful only when both terms have validated, commensurable measurements. It is not a score to rank LLMs, law, science, social media, evolution, or bureaucracy without domain-specific evidence.

## 7. Hallucination as One Test Case

Weak source, uncertainty, and admissibility carriage can contribute to unsupported output. But hallucination also has other possible causes: ambiguous prompts, missing knowledge, retrieval failure, distribution shift, decoding, tool errors, evaluation mismatch, incentives, and incorrect reference answers.

The morphological hypothesis becomes testable by intervention: hold model and task constant, add or remove specific conservation mechanisms, and measure supported-claim accuracy, citation fidelity, calibration, contradiction, abstention, and recovery. If conservation layers do not improve the targeted failures, the explanation should be narrowed.

Hallucination is not defined here as all semantic transformation without provenance.

## 8. Institutional and Social Systems

Institutions can preserve law, procedure, records, roles, and precedent while also generating drift, exclusion, rigidity, capture, or false continuity. Digital media can accelerate transformation while also preserving archives and traceability. The simple profiles in the source are hypotheses, not findings.

A defensible comparison needs explicit unit of analysis, time window, obligations, authority, measures, counterfactual, and evidence. High conservation is not automatically good: conserving injustice, error, or obsolete identity can be harmful. Healthy conservation must include governed revision and refusal.

## 9. Semantic Metabolism

The metabolism metaphor captures the joint need for generative change and continuity. It should not imply a measured biological homology or a universal carrying capacity. Its operational value lies in asking about inputs, transformations, retained structure, waste or remainder, repair, feedback, energy or resource cost, and failure under load.

Use the metaphor when it yields measurements or design questions; otherwise retain it as pedagogy rather than evidence.

## 10. Agentic Systems

Agentic systems add longitudinal state, tools, delegation, external effects, and coordination. Their conservation needs can include task identity, user intent, source custody, role and authority, constraints, decisions, uncertainty, receipts, intermediate failures, and handoff state.

Conservation is not a memory dump. Carrying irrelevant, expired, private, or adversarial material can itself be unsafe. The profile must specify what persists, what expires, what may be compressed, what requires renewed authority, and what must be deleted or withheld.

## 11. Corpus Integration and Authorial Compression

**Transformation-Dominant Semantic Systems** supplies the diagnostic morphology: semantic delta versus obligation carriage. **Constraint-Bearing Composability** specifies how obligations should survive composition. **Meta-Binding as Operational Invariant** identifies higher-order bindings that must persist across realization. **Epistemic Lineage Engine** tracks how claims descend from sources, transformations, and decisions. **Governance as Compilation** structures staged translation and semantic remainder.

These are complementary, not five names for one mechanism. The diagnostic paper says where an imbalance may exist; the others specify selected conservation machinery.

The **Governed Meaning Base (GMB)** can retain sources, envelopes, typed carriage outcomes, losses, conflicts, effects, and revision lineage. The universal **GSM** can type transformations and their preserved or broken relations without treating connection as fidelity.

## 12. Realization Funnel

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

- **Possibility:** enumerate generative, archival, lineage, authority, hybrid, lossy, and no-transform alternatives.
- **Specification:** define semantic delta, carried obligations, loss types, evidence, authority, privacy, and effect boundaries.
- **CM1:** retain admissible transformation/conservation profiles, including high-change and high-retention variants.
- **CM2:** prefer configurations by task utility, fidelity, calibration, inspectability, privacy, cost, and revisability.
- **IC:** select an Instance Constitution or Instance Configuration for one semantic workflow.
- **IR:** produce an Instance Realization or Implementation Realization of representations, transformations, checks, storage, and receipts.
- **Evidence:** test obligation carriage, useful change, error, recovery, costs, and downstream effects.
- **Revision:** update profiles, mechanisms, and realization from failures and counterevidence.

This paper reaches Specification and proposes CM1/CM2 measures. It does not select an IC or certify an IR. Realization-stage IR remains distinct from Intermediate Representation in MCIR and other compiler contexts.

## 13. Evaluation Program

Construct task suites spanning exact reproduction, paraphrase, translation, summarization, synthesis, multi-step inference, long-running agents, handoffs, and institutional workflows. For each task, predeclare obligations and allowed transformations.

Compare baseline systems with provenance, lineage, constraint-carriage, authority, uncertainty, and receipt mechanisms added singly and in combination. Measure semantic delta, obligation retention, unsupported additions, omission, provenance coverage, authority escalation, uncertainty calibration, reconstructability, reversibility, privacy loss, task success, latency, storage, and human comprehension.

Use causal ablation where possible. Report when conservation reduces useful transformation, preserves error, creates rigidity, or imposes greater cost than benefit.

## 14. Predictions

The framework predicts, conditionally, that: (1) high delta with low carriage will correlate with selected drift measures; (2) explicit lineage will improve reconstructability but not necessarily truth; (3) authority carriage will reduce silent standing escalation where effect paths are actually mediated; (4) calibrated uncertainty and typed remainder will reduce unsupported closure; and (5) optimal profiles will vary by task rather than converge on maximum conservation.

Each prediction can fail without invalidating every use of the morphology.

## Diagnostic Morphology of Governed Semantic Change

The completed P1 corpus supports a precise role for Transformation-Dominant Semantic Systems (TDSS): it is a **diagnostic morphology of semantic change and obligation carriage**. It classifies a workflow's balance between useful transformation and preservation of declared commitments; it does not supply the conservation machinery itself.

- **Adjacent work:** *Meta-Binding as Operational Invariant*  
  **Supplies:** Higher-order obligations that must survive transformations.  
  **TDSS boundary:** Supplies candidates for what the carriage profile should preserve.

- **Adjacent work:** *Epistemic Lineage Engine*  
  **Supplies:** Source, transformation, decision, and revision lineage.  
  **TDSS boundary:** Supplies reconstruction machinery; lineage presence alone does not prove fidelity.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Staged translation, lowering, semantic remainder, and governed transition.  
  **TDSS boundary:** Supplies a transformation architecture; TDSS diagnoses its change/carriage behavior.

- **Adjacent work:** *Semantic Debt*  
  **Supplies:** Accumulated cost of lost, deferred, ambiguous, or unmaintained semantic obligations.  
  **TDSS boundary:** Debt is a downstream consequence and repair burden, not identical to low conservation.

- **Adjacent work:** *Semantic Gravitational Attractors*  
  **Supplies:** Versioned convergence and canonicalization regimes.  
  **TDSS boundary:** Convergence can conserve selected distinctions while transforming or erasing others.

The cross-corpus diagnostic should report a vector rather than one rank:

$$
\begin{aligned}
D_T= (&\Delta_{useful}, C_{required}, L_{accepted}, L_{silent}, \\
&R_{recoverable}, K_{cost})
\end{aligned}.
$$

Here $\Delta_{useful}$ is task-relative semantic change; $C_{required}$ is verified carriage of required commitments; $L_{accepted}$ and $L_{silent}$ separate disclosed from undisclosed loss; $R_{recoverable}$ measures whether prior meaning and obligations can be reconstructed or repaired; and $K_{cost}$ records the resource and privacy cost of preservation. A highly generative system can score well if it carries what the task requires and exposes loss. A byte-preserving archive can score poorly if interpretation, authority, scope, or revision context becomes unusable.

Corpus integration adds one critical distinction: **conservation of an obligation is not conservation of its truth or current validity**. A system should preserve a claim's source, scope, standing, defeaters, and expiry even when the claim is later rejected. Deletion, forgetting, expiry, and redaction can themselves be required obligations.

The universal GSM can type `TRANSFORMS`, `CARRIES_OBLIGATION`, `DISCLOSES_LOSS`,  
`SILENTLY_DROPS`, `PRESERVES_FOR_REVIEW`, `EXPIRES`, `REDACTS_UNDER`, `RECONSTRUCTS_FROM`,  
and `INCURS_DEBT`. These relations keep change, retention, validity, and repair separate.

This integration establishes four editorial commitments: adopt diagnostic morphology as TDSS's official corpus role; adopt the six-part diagnostic vector; distinguish obligation conservation from truth preservation; and route implementation mechanisms to the adjacent works rather than presenting TDSS as a system architecture.

## Orientation Change, Authority Handoffs, Evidence Paths, and Experience-Research Carriage

The fixed-seed comparison with Recursive Semantic Orientation, Split-Authority AI Coordination, the Constitutional Observability Platform, and Qualia Binding and Realization Mapping turns the TDSS diagnostic toward four high-risk transformation surfaces:

$$
\begin{aligned}
D_T^*= (&subject, operation, profile, useful\_delta, \\
&required\_carriage, accepted\_loss, silent\_loss, \\
&recoverability, cost, authority\_edge, evidence\_path, \\
&claim\_ceiling)
\end{aligned}.
$$

An orientation update transforms hypotheses, partitions, unknowns, and active questions. It should preserve source custody, defeated countermodels, claim ceilings, and explicit remainder even when the active model changes. An authority handoff may transform a mandate into specification, realization, verification, or effect instructions; every edge must disclose obligation loss and semantic widening.

An observability path transforms domain state into events, records, assessments, widgets, accessibility representations, and human interpretation. Agreement at one edge does not conserve meaning through the entire path. Qualia research adds a stronger ceiling: transforms among reports, constructs, dimensions, bindings, models, and candidate realizations must preserve evidence kind and residual without promoting predictive success into phenomenal standing.

The universal GSM can type   
`TRANSFORMS_ORIENTATION_STATE`,  
`CARRIES_DEFEATED_COUNTERMODEL`, `TRANSFORMS_AUTHORITY_HANDOFF`, `SILENTLY_WIDENS_MANDATE`,  
`CARRIES_EVIDENCE_ACROSS_PROJECTION`, `PRESERVES_EXPERIENCE_CLAIM_KIND`,  
and   
`REFUSES_PHENOMENAL_PROMOTION`.

This randomized review establishes four editorial commitments: add subject, operation, authority edge, evidence path, and claim ceiling to the diagnostic; apply it to orientation updates; require carriage records at authority handoffs and observability projections; and impose experience-research claim-kind preservation across every transform.

## Obligation Carriage Across Substitution, Compilation, Binding, and Debt

Four downstream uses refine TDSS into an event-level diagnostic. A Cognitive ABI declares obligations that must survive capability substitution. *Everything Is a Compiler* uses the morphology to limit when compiler language explains a transformation. SBQ assesses the binding state produced or preserved after change. Semantic Debt records unresolved burdens that persist after dropped, ambiguous, or costly obligations. Semantic Gravitational Attractors was screened but not retained as a reverse dependency: generic conservation language and convergence do not establish use of the TDSS diagnostic.

The carriage record should be:

$$
\begin{aligned}
C= (&subject, operation, predecessor, successor, \\
&required\_obligations, equivalence, field\_fates, \\
&authorized\_loss, silent\_loss, evidence, dependents, \\
&liabilities, repair, remainder)
\end{aligned}.
$$

TDSS evaluates a bounded transformation event or workflow. SBQ evaluates the resulting binding profile. Semantic Debt tracks unresolved burden across time. These are related but nonidentical postures. A low-carriage event need not create debt if the loss was explicit, authorized, terminal, and consequence-free. A small undisclosed loss may create severe debt when many downstream claims, capabilities, or effects depend on it.

Accepted loss requires an authorized decision relative to a declared profile; the transformer cannot authorize its own convenience loss by recording it. Silent loss should propagate to dependent artifacts and trigger review, downgrade, conflict, repair, or retirement. Substitution equivalence remains profile-relative and must state which obligations and consequences were tested.

The universal GSM can type   
`DIAGNOSES_TRANSFORMATION_EVENT`,  
`DECLARES_REQUIRED_CARRIAGE`, `AUTHORIZES_PROFILE_RELATIVE_LOSS`,  
`SILENTLY_DROPS_OBLIGATION`, `PROPAGATES_CARRIAGE_FAILURE`, `DEGRADES_BINDING_QUALITY`,  
`INCURS_SEMANTIC_DEBT`, and   
`HAS_NO_CONFIRMED_ATTRACTOR_DEPENDENCY`.

This reverse-dependency review establishes four editorial commitments: adopt the carriage record; separate event morphology, resulting binding quality, and accumulated debt; require authorized rather than self-declared loss; and propagate silent loss to dependents without manufacturing an attractor dependency.

## 15. Counterevidence and Failure Modes

The framework should be narrowed or rejected where: (1) transformation and conservation are made exclusive; (2) operation names determine morphology; (3) high change is assumed unfaithful; (4) low change is assumed faithful; (5) a profile is absent; (6) obligations are not predeclared; (7) preservation types are conflated; (8) cryptographic identity implies truth; (9) provenance implies authority; (10) authority implies correctness; (11) reconstructability implies legitimacy; (12) uncertainty is discarded; (13) disagreement is normalized away; (14) loss is hidden; (15) strengthening creates unauthorized obligations; (16) conservation preserves error or injustice; (17) privacy conflicts with lineage; (18) deletion obligations conflict with persistence; (19) hallucination is treated as single-cause; (20) reference answers are wrong; (21) retrieval adds false evidence; (22) institutional examples are anecdotal; (23) system profile tables lack measures; (24) legal systems are called uniformly conservative; (25) social systems are called uniformly transformative; (26) metabolism is treated as biological proof; (27) imbalance measures are incommensurable; (28) high scores hide effect failures; (29) conservation layers can be bypassed; (30) receipts record only claims; (31) carrying stale context worsens decisions; (32) adversarial material persists; (33) GMB inclusion becomes validation; (34) GSM edges become fidelity; (35) corpus mechanisms are merged; (36) a specification is presented as implemented; (37) simpler provenance methods perform equally; (38) useful transformation is impaired; (39) costs exceed benefits; or (40) external research contradicts novelty or causal claims.

## A Diagnostic Morphology, Not a Binary Ontology

### Public orientation

This paper distinguishes transformation-dominant operations that produce new semantic states from conservation-dominant operations that preserve identity, recoverability, and obligations across change. Most real operations mix both. The distinction is proposed as explanatory compression and a source of testable questions, not a universal classification of systems.

### Adversarial tests

1. **False-binary attack.** Mixed operations are forced into one class. Profiles need degrees, dimensions, and context rather than a single label.
2. **Normative-bias attack.** Transformation is equated with progress or conservation with virtue. Either can preserve harm or destroy value.
3. **Scale-shift attack.** An operation transforms locally while conserving system-level function, or the reverse. Classification must state level and object.
4. **Temporal-shift attack.** Short-term conservation produces long-term transformation. Observation horizon is part of the claim.
5. **Identity-presumption attack.** The conserved property is never specified. Conservation requires a declared identity and verification relation.
6. **Novelty-presumption attack.** Surface difference is treated as semantic novelty. Transformation requires a material distinction under a profile.
7. **Biological-analogy attack.** Metabolism, evolution, or homeostasis language is treated as mechanistic equivalence. Analogies must retain domain boundaries.
8. **Measurement-circularity attack.** Operators are classified by the effects used to define the categories. Independent observations and counterexamples are needed.

### Claim and evidence ceiling

The morphology supplies a comparative vocabulary and predictions for governed semantic systems. It does not establish exhaustiveness, natural kinds, optimal balance, or universal laws. The dynamic-equilibrium framing is a research hypothesis, not a measured property of the corpus or other systems.

Claims about biology, organizations, cognition, software evolution, learning, or system performance require external domain evidence and operational measures. Internal corpus examples support explanatory usefulness only. No external research was added in this pass.

### Reader-facing consequence

The accessible question is: when a system changes, what is genuinely new, what must remain continuous, how is that continuity tested, and at what scale and time horizon?

## 17. Conclusion

Semantic transformation and semantic conservation are not opposing substances. They are independent dimensions of governed change. The important question is whether a transformation produces useful semantic difference while carrying the commitments that the task requires and exposing every accepted loss.

This reframing strengthens the source insight. Contemporary systems need not become less generative. They need explicit, testable ways to preserve source, identity, authority, uncertainty, scope, and evidence through generation - and equally explicit permission to revise what should not remain fixed.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of semantic change, information preservation, provenance, data and model lineage, LLM hallucination and calibration, institutional memory and drift, social-media information dynamics, legal and scientific record systems, distributed-system consistency, cognitive architecture, privacy and deletion, and empirical evaluation of conservation mechanisms.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Revision.** This stage is outside the present paper's asserted contribution and evidentiary scope.

## Corpus-Wide Reference Positioning

This paper argues that modern semantic systems can generate, translate, summarize, recombine, and propagate meaning at great speed while failing to preserve source, identity, authority, uncertainty, scope, or other commitments across those transformations. Its nearest external comparison fields are semantic, provenance, observation. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Telemetry can be complete at the instrumented boundary while omitting the causal variable, real-world effect, or authority question that matters. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Semantic Debt.* Zenodo, 2026. doi:10.5281/zenodo.21111666

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848478](https://doi.org/10.5281/zenodo.23848478)
