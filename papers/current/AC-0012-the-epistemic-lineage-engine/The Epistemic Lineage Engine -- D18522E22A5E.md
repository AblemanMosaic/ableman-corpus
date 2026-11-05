# The Epistemic Lineage Engine

## A Substrate for Reconstructable, Branching, and Governed Knowledge Change

### The Epistemic Lineage Engine (ELE) is proposed as a substrate for making those changes reconstructable.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Knowledge systems usually preserve selected artifacts and outcomes more reliably than the transformations, alternatives, environments, observations, and authority conditions that produced them. The Epistemic Lineage Engine (ELE) is proposed as a substrate for making those changes reconstructable. Its central unit is a lineage episode binding predecessor state, transformation, successor state, observation, result, branch relations, and evidence.

The source correctly distinguishes lineage from judgment, but several claims require qualification. A snapshot graph can be part of lineage; replay is not always deterministic; observations can have effects; undo does not erase external consequences; alternatives cannot always be retained indefinitely; and no engine can prove that every causally relevant influence was captured. ELE should therefore govern declared lineage closure and its limits rather than claim complete causality.

This paper formalizes an episode envelope, separates exact replay, deterministic replay, equivalence-class replay, procedural reenactment, and historical reconstruction, and adds privacy, retention, redaction, authority, environment, and irreversible-effect requirements. It integrates governed semantic project lineage, Reasoning by Way of Receipts, the Three Hash Rule, Semantic Debt, Governance Coverage Gaps, GMB, and the universal GSM.

ELE does not decide truth, approval, legitimacy, or authorship. It can preserve the materials from which such decisions are inspected. This paper reaches Specification and proposes configuration criteria; it does not establish a running engine, complete lineage capture, or deterministic replay.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. The custody and comparison manifest is   
`work/paper-saturation-v1/evidence/epistemic-`

`lineage-engine/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`F70D0ED3A30B4E590C2E0E1CDC81F0897E39868212EBFD5EC5338BB98B5F068D`. The source remains unchanged.

The ELE thesis, epistemic artifacts, lineage episode, operation algebra, branch and decision account, replay aspiration, governance layering, and application domains are author material. Formal extensions, claim qualifications, corpus integration, tests, counterevidence, and decisions added here are AI editorial or synthetic candidates until adopted. No external research was conducted.

## 1. The Missing Structure

A file snapshot answers "what bytes were retained?" A decision record may answer "what conclusion was announced?" A test log may answer "what one runner observed?" None alone necessarily binds:

- the exact predecessor used;
- the transformation actually applied;
- the environment and dependencies;
- the successor and external effects;
- the alternatives considered or generated;
- the authority under which commitment occurred;
- the observation procedure and result; and
- the limits of reconstruction.

ELE treats these relations as first-class. The problem is not that snapshots are useless. It is that a snapshot without transformation and evidence context cannot support the lineage claims users may infer from it.

## 2. Epistemic Artifacts and State

An **epistemic artifact** is a bounded object that represents a claim, belief, interpretation, intention, model, policy, constraint, or knowledge-bearing configuration. Source code, prompts, schemas, hypotheses, experiments, decisions, and ontologies may qualify under an explicit domain profile.

An **epistemic state** is a declared configuration of such artifacts plus the identity relations needed to interpret them. It is not the entire causal state of the world. State closure must identify included objects, excluded objects, unresolved dependencies, and observation limits.

Two byte-identical artifacts may occupy different epistemic states if authority, standing, context, dependencies, or interpretation differ. Conversely, two byte-different artifacts may be equivalent under a declared profile. ELE must preserve exact identity and profile-relative equivalence without conflating them.

## 3. The Lineage Episode

Define a lineage episode as:

$$
e=(id,P,S_0,\tau,\Gamma,A,S_1,X,O,Y,B,W),
$$

where:

- $id$ is episode identity;
- $P$ is one or more parent episodes;
- $S_0$ is the declared pre-state;
- $\tau$ is the transformation description and executable reference where available;
- $\Gamma$ is environment, dependency, time, randomness, and tool context;
- $A$ is authority and requested effect scope;
- $S_1$ is the post-state;
- $X$ is external, partial, irreversible, or unknown effects;
- $O$ is the observation procedure;
- $Y$ is the result and interpretation boundary;
- $B$ records alternatives, branches, and selection status; and
- $W$ is custody, receipt, and witness material.

An episode can record failure, refusal, partial execution, or an observation-only event. A complete record of declared fields does not establish that all causal influences were captured.

## 4. Core Invariants

ELE should preserve at least:

1. **Predecessor binding:** every non-root episode names its parent state or records why none exists.
2. **Transformation identity:** the operation, version, and parameters are bound or explicitly unavailable.
3. **State/effect separation:** retained artifact state is distinguished from external effects.
4. **Observation separation:** the procedure and its result are distinct from the interpretation placed on it.
5. **Branch persistence:** known alternatives have explicit dispositions rather than silent disappearance.
6. **Standing neutrality:** lineage custody does not grant truth, approval, authorship, or authority.
7. **Claim-bounded replay:** every replay result states its closure and equivalence class.
8. **Revision lineage:** corrections create successor records rather than silently rewriting prior evidence.

These are specification obligations, not claims that an implementation currently enforces them.

## 5. An Expanded Operation Algebra

The source proposes `transform`, `untransform`, `retransform`, `observe`,  
and `reobserve`. Retain the names with bounded semantics.

- **transform:** attempt a declared change and record state plus effects.
- **untransform:** create a compensating or restoring transition; it does not erase history or guarantee reversal of external effects.
- **retransform:** execute a declared transformation again under a newly bound environment and episode identity.
- **observe:** perform a declared observation and record whether it may affect the subject or environment.
- **reobserve:** repeat an observation with a new time, environment, and result.

Additional operations may be profiles rather than primitives: branch, merge, redact, expire, export, challenge, and repair. "If something is known, it must arise from observation" is too strong: knowledge claims may also depend on inference, testimony, proof, inherited records, or definition. ELE should record the warrant type rather than collapse all warrant into observation.

## 6. Replay Taxonomy

Replay has several materially different meanings.

- **Class:** Exact artifact replay  
  **Requirement:** reproduce exact retained bytes  
  **Permitted claim:** artifact equality only

- **Class:** Deterministic execution replay  
  **Requirement:** same closed inputs and deterministic regime produce exact result  
  **Permitted claim:** exact result under declared closure

- **Class:** Equivalence-class replay  
  **Requirement:** result differs but satisfies a declared equivalence relation  
  **Permitted claim:** profile-relative correspondence

- **Class:** Procedural reenactment  
  **Requirement:** repeat the method in a new environment or time  
  **Permitted claim:** comparability, not identity

- **Class:** Historical reconstruction  
  **Requirement:** assemble evidence about a past path that cannot be rerun  
  **Permitted claim:** bounded reconstruction

Many scientific, social, ML, legal, and institutional processes cannot be exactly replayed. Participants change, data disappears, services evolve, stochastic systems diverge, and physical effects are irreversible. ELE remains useful if it reports the strongest supported class rather than calling all reconstruction replay.

## 7. Branches, Alternatives, and Decisions

Branches can record explored alternatives, generated candidates, failed paths, counterfactuals, and successor lines. An alternative that was never instantiated is not a predecessor state merely because it was discussed.

A decision is more than collapse of a frontier. It may select, defer, authorize, refuse, delegate, or preserve plural paths. Unchosen alternatives may remain feasible, become inadmissible, expire, or lose support. Record:

- the option set actually available;
- how each option entered the set;
- decision authority and applicable law;
- evidence and values used;
- selected and unselected dispositions;
- external effects of commitment; and
- appeal, revision, or reopening conditions.

Preserving every alternative forever is neither possible nor always lawful. Retention, summarization, deletion, and redaction should be governed and receipted.

## 8. Observation Is Not Necessarily Effect-Free

Tests can mutate caches, consume resources, expose secrets, change human behavior, alter a measured system, or create legal and privacy consequences. `observe` should mean that the intended semantic state is not transformed, not that no effect occurs.

Every observation should declare its subject, instrument, environment, expected side effects, permissions, result type, uncertainty, and interpretation boundary. A pass result is evidence from one observation regime, not timeless validation.

## 9. Custody and the Three Hash Rule

ELE can use the Three Hash Rule to distinguish law or governing input, operation or judgment, and resulting artifact or effect. Hashes support exact identity; they do not establish semantics, completeness, behavior, or legitimacy.

Receipts should bind episode identity, parents, pre-state, transformation, environment, authority, result, effects, observations, branches, and claim ceiling. Signatures can attest a key's statement but require governed key identity, authority, revocation, and compromise handling.

## 10. Privacy, Secrecy, and Retention

Lineage can expose personal data, security-sensitive configuration, confidential deliberation, protected research subjects, trade secrets, or legally restricted records. "Persistent visibility of alternatives" must therefore be qualified.

A domain profile should define collection minimization, access, encryption, separation of public metadata from protected payloads, retention, expiration, lawful deletion, redaction proofs, source protection, and emergency access. A tombstone may preserve that a governed deletion occurred without retaining prohibited content.

No lineage system should convert the goal of accountability into universal surveillance.

## 11. Relationship to Governance

ELE preserves declared transition history. A governance kernel can ask whether a transformation was authorized, admissible, constitutional, or binding. An evidence system can evaluate observations. A court can adjudicate a bounded dispute. None of these roles is supplied by lineage alone.

Conversely, governance without exact lineage may rely on incomplete or retrospective narratives. The relationship is reciprocal but not identity: lineage supplies traceable material; governance supplies law and decision authority.

## 12. Corpus Integration

**Governed Semantic Project Lineage** extends content addressing toward semantic identity, obligations, and project evolution. ELE supplies a general episode substrate and should not duplicate that work's entire project-level architecture. **Reasoning by Way of Receipts** supplies claim-bounded inference. **The Three Hash Rule** supplies a compact binding among authority, operation, and result.

**Semantic Debt** explains obligations lost or deferred across transitions. **Governance Coverage Gaps** tests which transformations and effects escape capture. The **Governed Meaning Base (GMB)** can retain episodes, identities, standing, conflicts, alternatives, evidence, and revision. The universal **GSM** can type `PRECEDES`,  
`TRANSFORMS`, `OBSERVED_BY`, `AUTHORIZED_BY`, `BRANCHES_FROM`, `COMPENSATES_FOR`,  
`EQUIVALENT_UNDER`, `CONTESTED_BY`, and `REVISES` without turning chronology into causation.

## 13. Realization Funnel

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

- **Possibility:** enumerate event-sourced, snapshot, proof-carrying, distributed, private, and hybrid lineage systems.
- **Specification:** define episode fields, invariants, replay classes, retention, access, and claim ceilings.
- **CM1:** retain admissible configurations, including incomplete, centralized, expensive, or low-retention forms.
- **CM2:** prefer configurations by reconstruction value, privacy, security, accessibility, interoperability, and cost.
- **IC:** select an Instance Constitution or Instance Configuration for a bounded domain.
- **IR:** produce an Instance Realization or Implementation Realization of storage, capture, replay, query, receipt, and access components.
- **Evidence:** test closure, replay, branching, partial failure, privacy, redaction, deletion, scale, and human use.
- **Revision:** migrate schemas and policies while preserving predecessor identity and known loss.

This paper reaches Specification and proposes CM1/CM2 criteria. It does not select an IC, produce an IR, or establish replay performance.

In this funnel, IR denotes the realization stage and remains distinct from Intermediate Representation in compiler-oriented corpus terms.

## 14. Verification Program

A reference candidate should be tested on software change, experimental reasoning, model or prompt revision, and institutional policy cases. Tests should include root creation, branches, merges, failed and partial transformations, observation side effects, missing dependencies, stochastic divergence, compromised witnesses, concurrent updates, schema migration, protected data, authorized deletion, export, provider exit, and reconstruction after component loss.

Measures should include captured versus declared dependencies, unknown-effect rate, replay class achieved, exact and profile-relative divergence, branch recovery, false lineage links, receipt verification, privacy leakage, deletion completeness, storage and compute cost, query latency, and user reconstruction accuracy.

## Epistemic Transition Lineage Substrate

Across the completed P1 corpus, the Epistemic Lineage Engine is the **domain-general transition-lineage substrate for claims, models, policies, interpretations, experiments, prompts, and other epistemic artifacts**. It binds predecessors, transformations, environments, branches, observations, effects, authority references, and reconstruction limits. It preserves what was declared to have happened without deciding truth, causal completeness, governance validity, or promotion.

- **Adjacent work:** *From Content-Addressed Storage to Governed Semantic Project Lineage*  
  **Supplies:** Project-scale heads, obligations, projections, reconstruction, and successor structure.  
  **ELE boundary:** ELE provides a reusable episode model rather than the full project architecture.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Claim-bounded reasoning and evidentiary transitions.  
  **ELE boundary:** ELE can carry reasoning episodes without making lineage itself a warrant.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Who or what holds live responsibility for work through time.  
  **ELE boundary:** Custody may travel along lineage but is not inferred from parentage alone.

- **Adjacent work:** *Governance Coverage Gaps*  
  **Supplies:** Detection of relevant transformations or effects outside the governed surface.  
  **ELE boundary:** ELE records declared closure and unknowns; it cannot prove that no episode was omitted.

- **Adjacent work:** *Semantic Debt*  
  **Supplies:** Obligations and unresolved meaning carried or lost across change.  
  **ELE boundary:** Debt is a typed payload or remainder of lineage, not identical to lineage.

An episode should separate five graphs that are often collapsed: artifact ancestry, transformation execution, authority and custody, observation and evidence, and external effects. Chronological adjacency in one graph does not establish a relation in another. A successor file may not be an authorized successor; an observation can affect the subject; a compensating action can leave an irreversible external residue.

The episode contract should therefore bind:

$$
\begin{aligned}
E= (&parents, prestate, operation, environment, authority, \\
&custody, poststate, effects, observations, \\
&interpretations, alternatives, standing, replay\_class, \\
&privacy, retention, revision)
\end{aligned}.
$$

Replay classes must be declared before result comparison. Exact artifact replay, deterministic execution replay, profile-equivalent replay, observational reproduction, and narrative reconstruction support different claims. Redaction or deletion may intentionally prevent a replay class and must leave an authorized, privacy-preserving break in the evidentiary story rather than a fabricated continuous chain.

The universal GSM can type   
`DESCENDS_FROM_EPISODE`, `TRANSFORMS_EPISTEMIC_STATE`,  
`EXECUTES_UNDER_ENVIRONMENT`, `TRANSFERS_WORK_CUSTODY`, `OBSERVES_WITH_SIDE_EFFECT`,  
`LEAVES_EXTERNAL_RESIDUE`, `RETAINS_UNSELECTED_BRANCH`, `REPLAYS_UNDER_DECLARED_CLASS`,  
`REDACTS_UNDER_AUTHORITY`,  
and   
`REVISES_PRIOR_INTERPRETATION`. These relations turn lineage into a multidimensional substrate rather than a timeline.

This integration establishes four editorial commitments: retain ELE as the epistemic transition-lineage substrate; adopt the five-graph separation and expanded episode contract; require ex ante replay classes and explicit authorized discontinuities for privacy or deletion; and keep lineage, causation, truth, governance, custody, and promotion as distinct relations.

## Lineage of Models, Experiments, Evidence Cases, and Reference Graphs

The fixed-seed comparison with Dynatology, CCOO, the seventeen-system software study, and the MCIR DAG theorem broadens the episode subject while preserving the boundary between history and warrant:

$$
\begin{aligned}
E^*= (&subject\_type, parents, prestate, operation, environment, \\
&authority, custody, poststate, effects, observations, \\
&interpretations, reference\_root, replay\_class, \\
&standing, remainder)
\end{aligned}.
$$

Dynatological domain mappings and theorem candidates need lineage for changed state maps, preserved structure, discarded structure, counterexamples, and narrowed claims. CCOO experiments need exact configuration, seed, environment, artifacts, observations, interpretation, and replay class. The software study needs case and aggregate lineage when categories, denominators, or findings change.

A version-ranked MCIR DAG may store a closed acyclic reference layer for episode artifacts. Epistemic ancestry, revision, compensation, authority, observation, and external-effect relations can be cyclic, cross-version, or open and therefore belong in typed layers rather than being forced into the canonical DAG.

Lineage completeness remains defeasible. A valid reference root does not prove that every material predecessor, observation, effect, or alternative was captured. The universal GSM can type   
`LINEAGES_DOMAIN_MORPHISM`,  
`LINEAGES_EXPERIMENT_RUN`, `LINEAGES_EVIDENCE_CASE`, `REFERENCED_BY_CANONICAL_DAG`,  
`REPRESENTS_CYCLIC_RELATION_OUTSIDE_DAG`, `OMITS_POSSIBLE_EPISODE`,  
and   
`DOES_NOT_WARRANT_BY_ANCESTRY`.

This randomized review establishes four editorial commitments: adopt subject-typed lineage episodes; bind models, experiments, and evidence cases to exact revisions; keep non-DAG relations in explicit layers; and prohibit referential closure or ancestry from establishing epistemic completeness or warrant.

## Typed Epistemic Dependencies and Correction Propagation

Ten downstream uses confirm the Epistemic Lineage Engine as a claim- and model-transition substrate rather than a general file history. CCOO uses it for experimental configurations and interpretations. Dynatology uses it for domain mappings and counterexamples. The MCIR DAG theorem uses it around structural witnesses. Receipt reasoning supplies events. Quant research requires point-in-time vintages. Governed retrieval binds sources and claims. Project lineage interoperates while retaining file-state subjects. GKL governs admission over the recorded history. TDSS uses lineage for reconstruction. The software evidence study binds cases, methods, findings, and aggregate eligibility.

The typed dependency record is:

$$
\begin{aligned}
L= (&subject, epistemic\_object, operation, inputs, output, \\
&claims, evidence, alternatives, decision, standing, \\
&validity\_epoch, dependents, replay\_class, revision, \\
&remainder)
\end{aligned}.
$$

Operations such as observe, retrieve, transform, infer, aggregate, compare, adopt, reject, supersede, and retract require different evidence and do not share one replay meaning. Byte replay reconstructs an artifact. Computational replay repeats a declared operation. Evidentiary replay reconstructs the admissible basis available at a time. Decision replay reconstructs reasoning without pretending that the same authority or environment still exists.

When an input is corrected, revoked, reclassified, or found ineligible, the engine should locate dependent claims, models, decisions, aggregates, and projections. Outcomes include `UNAFFECTED`,  
`RECOMPUTE_REQUIRED`, `DOWNGRADED`, `CONFLICTED`, `HISTORICAL_ONLY`,  
`RETRACTED_FOR_CURRENT_USE`,  
and `UNRESOLVED`. The predecessor remains reconstructable; correction propagation does not rewrite history.

The universal GSM can type   
`PERFORMS_EPISTEMIC_OPERATION`, `DEPENDS_ON_EVIDENCE_EPOCH`,  
`REPLAYS_COMPUTATIONALLY`, `RECONSTRUCTS_DECISION_BASIS`, `PROPAGATES_EPISTEMIC_CORRECTION`,  
`DOWNGRADES_DEPENDENT_CLAIM`, `PRESERVES_ALTERNATIVE_BRANCH`,  
and   
`INTEROPERATES_WITHOUT_PROJECT_LINEAGE_MERGER`.

This reverse-dependency review establishes four editorial commitments: adopt typed epistemic operations; separate artifact, computational, evidentiary, and decision replay; require correction propagation to dependents; and preserve project lineage, receipts, knowledge admission, and epistemic validity as distinct roles.

## 15. Counterevidence and Failure Modes

The proposal should be narrowed or rejected where: (1) snapshots are dismissed despite carrying adequate lineage; (2) narrative rationale is treated as worthless; (3) chronology is treated as causation; (4) declared closure is mistaken for complete causality; (5) transformation identity omits environment or dependencies; (6) external effects are omitted; (7) `untransform` is treated as true inversion; (8) observation is assumed effect-free; (9) deterministic replay is claimed for stochastic or open systems; (10) reenactment is mislabeled exact replay; (11) equivalence relations are chosen after results; (12) missing historical evidence is silently reconstructed; (13) alternatives never actually considered are added retrospectively; (14) all alternatives are retained without cost or legal analysis; (15) deletion is made impossible; (16) redaction silently breaks receipts; (17) privacy and source protection are ignored; (18) hashes are treated as semantic proof; (19) signatures are treated as authority; (20) compromised keys lack recovery; (21) lineage custody becomes truth or approval; (22) governance and lineage are merged; (23) GMB inclusion becomes standing; (24) chronology creates an identity merger; (25) coverage gaps remain unobserved; (26) storage or capture burden changes behavior materially; (27) schema migration loses predecessor meaning; (28) provider exit cannot reconstruct the system; (29) users cannot understand the lineage; (30) cross-domain claims exceed tested profiles; (31) existing provenance or event-sourcing systems already satisfy the bounded need; or (32) external research contradicts novelty or feasibility claims.

## Replayable Lineage Without Post Hoc Truth

### Public orientation

The Epistemic Lineage Engine records meaning-bearing change as explicit branching transitions so ancestry, alternatives, verification, drift, correction, and commitment can be reconstructed. It supplies neutral mechanical lineage. Higher governance decides what the lineage means and which branches have standing.

### Adversarial tests

1. **History-tampering attack.** Earlier events are rewritten or removed without a successor or deletion receipt. Append-only claims require exact storage and verification evidence.
2. **Branch-collapse attack.** Alternatives are merged because they share content or names. Branch identity, rationale, and unresolved conflict must survive.
3. **Replay-environment attack.** Events replay differently because tools, dependencies, randomness, time, or external services changed. Reproducibility claims bind environment and remainder.
4. **Hash-as-meaning attack.** Byte identity is treated as semantic identity, or byte change as semantic change. Content, interpretation, and standing require separate relations.
5. **Lineage-as-causality attack.** An ancestor relation is treated as causal responsibility or evidentiary support. Derivation, influence, support, and authority are distinct edge types.
6. **Correction-propagation failure.** A source is corrected but dependent claims remain active. Dependency indexing and impact review are needed.
7. **Privacy-retention attack.** Permanent lineage preserves sensitive, revoked, or legally constrained material. Cryptographic commitment, access, deletion, and retained proof need policy.
8. **Branch-explosion attack.** Complete history becomes unusable or too expensive. Compaction must preserve identity, audit, and recoverability while declaring loss.

### Claim and evidence ceiling

ELE defines a transition-lineage substrate and verification program. It does not judge truth, correctness, value, approval, authority, policy, causal responsibility, or semantic equivalence. Replay proves only what the bound environment and observations support.

Claims about version control, event sourcing, provenance, reproducible computation, privacy, storage scale, or distributed integrity require external comparison and exact realizations. No external research was added in this pass.

### Reader-facing consequence

The public benefit is that a claim or artifact can be corrected without erasing how it arose: people and agents can inspect prior branches, reproduce what is still reproducible, and see which downstream conclusions must be reconsidered.

## 17. Conclusion

Durable knowledge requires more than retained outcomes. It requires a visible relation among predecessor, transformation, environment, authority, successor, effect, observation, alternative, and revision. ELE offers a compact substrate for that relation.

Its value depends on bounded claims. It cannot recover influences never captured, make irreversible effects disappear, turn reenactment into exact replay, or convert custody into truth. It must also govern what should not be retained.

With those limits, the Epistemic Lineage Engine becomes a strong foundation for reconstructable knowledge change: not an oracle and not a court, but a memory substrate capable of showing what the system says changed, what evidence accompanied the change, what alternatives remain visible, and where reconstruction ends.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of version control, event sourcing, provenance standards, reproducible computation, scientific workflows, ML and data lineage, legal and policy records, records retention and deletion, privacy and security, distributed systems, deterministic replay, and existing lineage products and research.

## Corpus-Wide Reference Positioning

This paper argues that knowledge systems usually preserve selected artifacts and outcomes more reliably than the transformations, alternatives, environments, observations, and authority conditions that produced them. Its nearest external comparison fields are provenance, governance, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E2]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E3]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

**[E4]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

### Ableman corpus

**[A1]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *A Formal Theory of Work Custody*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-C8F2F9BF38C45E29`;  
source SHA-256  
`A80657E21BA277ADF1C229A2AAE221963B97A62EA2AF3EBC36434A916A8EEA44`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Governance Witnesses*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-9E8DA0EFE860DE5D`;  
source SHA-256  
`8BF8C3646040F6E1F5222A8AA92C1106AA1F841E8A2C65402F468C83D59D06E5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governance Engineering*. Ableman Corpus current edition; work identity `PAPER.PUB.18749870`;  
source SHA-256  
`372169F315D192733856B1F4A3F1038BBC73F57CF3ED9ACABAE72B965A69C8D0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Semantic Debt.* Zenodo, 2026. doi:10.5281/zenodo.21111666

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847643](https://doi.org/10.5281/zenodo.23847643)
