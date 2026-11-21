# Human-Legible Intermediate Representation

## Constitutional Proposal Profiles for Governed Semantic Systems

### Human and AI authors reason through goals, alternatives, constraints, authority, uncertainty, evidence, and intended effects.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Human and AI authors reason through goals, alternatives, constraints, authority, uncertainty, evidence, and intended effects. Canonical machine representations often optimize different properties: exact structure, identity, validation, transformation, and execution. A Human-Legible Intermediate Representation (HLIR) is proposed as a structured proposal form bridging those concerns without granting proposals canonical or operational standing.

An HLIR is best understood as a family of human-facing authoring and projection profiles over governed semantic objects, not necessarily as a new foundational meaning representation. It makes selected distinctions explicit, retains source and unresolved remainder, and supports a declared lowering function into an MCIR candidate. Lowering, canonicalization, adjudication, admission, authority grant, execution lowering, and external effect remain separate transitions.

This paper defines an HLIR proposal envelope, validity and legibility criteria, deterministic-lowering conditions, refusal outcomes, non-ambient authority rule, full realization-funnel grammar, AI authoring boundary, round-trip and usability requirements, and evaluation program. The older Specification-Configuration-Implementation triad remains a compact pedagogical profile, while the current architecture distinguishes CM1, CM2, Instance Constitution or Configuration, and Instance or Implementation Realization.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/human-`

`legible-intermediate-representation/`  
`integration-custody-manifest.v0.1.json`,  
SHA-256  
`976780BD833AF1AD34D651AFA9C1F3FF5A0CE15C862126DE188E1F134F784046`. The source remains unchanged.

The HLIR concept, layering, properties, SCI example, meta-map, AI role, research questions, and demonstrator are author material. Formal qualifications, role compression, countertests, and decisions are AI editorial or synthetic candidates until adopted. No expression is admitted, canonicalized, compiled, authorized, or executed here.

## 1. The Representation Gap

Natural language, diagrams, forms, code, policy, configuration, and canonical representations offer different balances of expressivity, precision, learnability, ambiguity, and machine tractability. The gap is not simply human thought versus machine execution. Human communities disagree; machine representations embed design choices; canonicalization can erase distinctions; and implementation can diverge from either.

HLIR addresses one bounded problem: how to make a proposal inspectable and mechanically processable before it enters a canonical governed representation.

## 2. HLIR Role

An HLIR is a versioned representation profile that:

- is intended for direct human review and assisted authoring;
- exposes the governance distinctions relevant to its domain;
- binds exact source, definitions, authority references, unknowns, and requested effects;
- has a declared syntax, types, validation, lowering, and refusal behavior;
- preserves semantic remainder and translation loss;
- can project canonical objects back into reviewable form; and
- remains a proposal until a separate adjudication admits it.

Human-readable serialization alone is insufficient. A large JSON or YAML object may be technically readable but operationally illegible. Legibility is measured through successful authoring, review, error detection, disagreement resolution, and comprehension by intended users.

## 3. Proposal Envelope

Represent an HLIR proposal as:

$$
H=(id,v,p,s,d,a,k,u,q,x,e,r),
$$

where $id$ and $v$ identify the proposal and profile version, $p$ the domain and interpretation profile, $s$ exact sources, $d$ declared definitions and stage placement, $a$ authority references, $k$ constraints and obligations, $u$ unknowns and alternatives, $q$ requested capabilities, $x$ intended effects and exclusions, $e$ supporting evidence, and $r$ unresolved remainder and revision lineage.

An authority reference identifies a purported grant or jurisdiction; writing it into HLIR does not create that authority. Requested capabilities remain requests.

## 4. Layered Architecture

A bounded flow is:

$$
\begin{aligned}
&input \\
&\rightarrow structured\ draft \\
&\rightarrow HLIR\ proposal \\
&\rightarrow MCIR\ candidate \\
&\rightarrow adjudication \\
&\rightarrow admitted\ MCIR \\
&\rightarrow execution\ representation \\
&\rightarrow mediated\ effect
\end{aligned}.
$$

Each arrow has its own contract and can refuse, defer, preserve alternatives, or return not-covered. The architecture prevents four common collapses:

1. well formed does not mean admissible;
2. deterministically lowered does not mean canonical;
3. canonical does not mean authorized for effect; and
4. authorized does not mean successfully realized or evidenced.

PEIR appears in the corpus as the post-MCIR execution representation, but its expanded name varies across sources. This paper preserves the acronym and leaves name adjudication to the author rather than silently merging Program and Procedural Execution Intermediate Representation.

## 5. Deterministic Lowering

For profile version $p$ and lowering version $l$, define:

$$
L_{p,l}(H)\rightarrow(M_c,\rho,U),
$$

where $M_c$ is an MCIR candidate, $\rho$ a lowering receipt, and $U$ unresolved or refused remainder. For identical canonical HLIR input and declared dependencies, the output should be reproducible.

Determinism requires closed dependencies, canonical input normalization, explicit defaults, fixed schema and rule versions, deterministic ordering and numeric behavior, and controlled external data. It does not guarantee that the mapping preserves meaning, that the proposal is authorized, or that the MCIR candidate will be admitted.

Two surface-different expressions may lower identically only under a declared equivalence relation. Round-trip projection should reveal information that the canonical form cannot preserve.

## 6. Refusal and Ambiguity

Typed outcomes include `MALFORMED`, `TYPE_ERROR`, `AMBIGUOUS`, `UNRESOLVED_REFERENCE`,  
`UNDECLARED_AUTHORITY`, `CONSTRAINT_CONFLICT`, `LOSS_EXCEEDS_PROFILE`, `DEFER`,  
`NOT_COVERED`, and `LOWERED_CANDIDATE`.

Ambiguity need not always be rejected. An HLIR can preserve bounded alternatives and require later adjudication. Refusal should identify location, violated rule, evidence, standing, requested repair, and whether partial structure remains reusable.

## 7. Non-Ambient Authority

HLIR can require every capability, delegation, jurisdiction, and effect request to be explicit. It cannot prevent ambient authority if another path bypasses the representation, the runtime honors undeclared defaults, credentials exceed declared scope, or reviewers grant proposals automatically.

The non-ambient-authority claim therefore requires whole-path tests from authoring through lowering, adjudication, execution, tools, plugins, credentials, and external effects. The strongest defensible claim is that an HLIR makes undeclared authority structurally visible or refuses it within its mediated path.

## 8. The Realization Funnel as Grammar

The source SCI triad separates possibility, configuration, and implementation, but the current corpus carries a more precise funnel:

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

- **Possibility:** candidate worlds, approaches, and unselected alternatives.
- **Specification:** required structure, behaviors, constraints, and interfaces.
- **CM1:** the admissible configuration manifold, including undesirable but allowed variants.
- **CM2:** preferred or optimized admissible configurations under declared values.
- **IC:** an Instance Constitution or Instance Configuration selecting one governed slice.
- **IR:** an Instance Realization or Implementation Realization making that selection concrete.
- **Evidence:** observations supporting bounded claims about the realization.
- **Revision:** amendments and lineage responding to evidence and changed authority.

An HLIR may address one or several stages, but it must type each statement. The compact SCI form remains a pedagogical projection, not permission to collapse CM1, CM2, IC, evidence, or revision into a single Configuration or Implementation block.

Here IR means the realization-funnel stage. It is distinct from **Intermediate Representation** in HLIR, MCIR, Context IR, Workflow IR, and related names.

## 9. HLIR and MCIR

HLIR and MCIR should not duplicate semantic authority. HLIR optimizes authoring, explanation, review, and proposed structure. MCIR optimizes canonical identity, machine validation, governed transformation, and cross-profile carriage.

Some HLIRs may be reversible views over MCIR; others may contain proposal material that is intentionally absent from admitted canonical form. The relationship is profile-specific. HLIR validity does not establish MCIR conformance, and MCIR precision does not establish human legibility.

## 10. AI Proposal Discipline

AI may translate source material into an HLIR draft, suggest missing fields, compare alternatives, simulate lowering, or explain refusals. Every generated field should retain provenance and confidence. The system should distinguish copied source, extracted structure, inferred value, generated option, and human-adopted decision.

AI receives no standing through use of the grammar. It may not fabricate authority references, silently resolve unknowns, convert proposals into grants, or bypass the HLIR through direct tool or code paths.

## 11. Expressivity and Containment

"Proposal-complete but not behavior-complete" is a useful research target, not yet a formal boundary. An HLIR can regain programming-language complexity through macros, hidden control flow, imports, reflection, defaults, or embedded expressions.

Containment criteria should cover termination or resource bounds where required, effect freedom during lowering, explicit imports, transparent expansion, decidable validation where claimed, restricted metaprogramming, and bounded extension points. Some domains may require an executable DSL; they should not be mislabeled as non-instructional merely because they use constitutional syntax.

## 12. Human Legibility

Legibility depends on audience, task, scale, tools, accessibility, language, notation, organizational incentives, and review time. It can decay as artifacts grow or users rubber-stamp generated proposals.

Required evidence can include comprehension accuracy, error localization, review agreement, authoring time, correction success, cognitive load, accessibility, novice-to-expert transfer, and bypass rate. Editors should expose source, stage, authority, uncertainty, dependencies, lowered projection, and semantic diff rather than only syntax.

## 13. Corpus Integration and Authorial Compression

**HLIR** is the human-facing proposal and projection family. **MCIR** is the canonical governed Intermediate Representation family. **The Ableman Format Specification** provides artifact roles and the realization-layer discipline. **MCIR Topologies** explores AST, DAG, and other structural choices. **Governance as Compilation** supplies stage contracts, remainder, and effect separation.

HLIR should therefore be retained as a representation profile and interface capability, not promoted into a duplicate canonical substrate. Candidate systems such as a "Meaning-Carrying IR" should first be tested as HLIR or MCIR profiles before receiving a new foundational identity.

The **Governed Meaning Base (GMB)** can retain sources, HLIR drafts, profiles, MCIR candidates, refusals, decisions, receipts, and revisions. The universal **GSM** can type proposes, lowers-to, refuses, admits, projects, supersedes, and evidences relations without treating lowering as authorization.

## 14. HLIR Meta-Map

The meta-map should classify HLIR profiles by domain, audience, stages represented, expressivity, authority surface, ambiguity posture, lowering target, reversibility, extension mechanism, evidence needs, and effect boundary. SCI, policy, workflow, infrastructure, data-governance, and domain-science profiles may differ substantially.

Shared target MCIR does not imply one universal syntax. Interoperability depends on common contracts and explicit translation, not uniform appearance.

## 15. Evaluation Program

Build a small profile only after separate implementation authorization. Compare natural-language prompting, direct code or configuration generation, conventional schema or DSL authoring, and HLIR-mediated authoring on the same bounded tasks.

Measure requirement and authority omissions, ambiguity detection, lowering reproducibility, semantic loss, round-trip fidelity, review comprehension, error localization, inter-reviewer agreement, proposal repair, unauthorized capability requests, bypass, task success, latency, cognitive load, and maintenance cost. Use adversarial prompts, stale schemas, conflicting sources, hidden defaults, and alternative valid realizations.

## Human Proposal and Review Layer

Across the completed P1 corpus, Human-Legible Intermediate Representation is the **human proposal, review, and repair layer for governed semantic systems**. It lets people and agents state structured intent, dependencies, authority references, alternatives, ambiguity, and evidence needs before canonical admission. It is not MCIR, an execution plan, an authority source, or realization-stage IR.

- **Adjacent work:** *MCIR Topologies*  
  **Supplies:** Configuration choices for canonical graph and representation families.  
  **HLIR boundary:** HLIR may target those families without becoming canonical merely by lowering.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Stage contracts, typed remainder, refusal, and evidence.  
  **HLIR boundary:** HLIR is one authoring-side stage with an explicit directional lowering contract.

- **Adjacent work:** *The Ableman Format Specification (AFS)*  
  **Supplies:** Artifact roles, profiles, validation, and conformance fixtures.  
  **HLIR boundary:** AFS can standardize HLIR profiles without selecting one universal human syntax.

- **Adjacent work:** *Semantic Legitimacy Before Context*  
  **Supplies:** Legitimacy and admissibility before candidate material becomes binding.  
  **HLIR boundary:** A valid HLIR proposal still requires admission; it cannot self-promote through structure.

- **Adjacent work:** *Governed Controlled Machine Language (GCML)*  
  **Supplies:** Candidate post-admission procedural preservation profile.  
  **HLIR boundary:** HLIR expresses inspectable proposal intent; GCML, if retained, expresses governed procedure.

An HLIR profile should bind:

$$
\begin{aligned}
H= (&audience, domain, purpose, claims, objects, relations, \\
&constraints, authority\_references, ambiguity, \\
&alternatives, evidence\_needs, lowering\_target, \\
&repair\_surface, provenance)
\end{aligned}.
$$

The lowering result is not simply success or failure. It should classify `EXACT`, `REFINED`,  
`AMBIGUOUS`, `CONFLICTING`, `UNDERAUTHORIZED`, `UNDERDETERMINED`, `UNSUPPORTED`,  
`OUT_OF_PROFILE`, or `REFUSED`,  
and retain a typed remainder. An AI-authored field must remain attributable as AI proposal even when a human approves other fields.

Legibility is audience-relative and empirical. A notation can be syntactically friendly while hiding authority, defaults, dependencies, or effect. Evaluation should test whether distinct users can locate consequential differences, challenge unwanted assumptions, predict lowering outcomes, and repair refusals more accurately than with simpler forms or natural-language prompting.

The universal GSM can type   
`PROPOSES_IN_HLIR_PROFILE`, `TARGETS_MCIR_PROFILE`,  
`DECLARES_AMBIGUITY`, `OFFERS_ALTERNATIVE_CONFIGURATION`, `REFERENCES_NONAMBIENT_AUTHORITY`,  
`LOWERS_WITH_REMAINDER`, `REFUSES_UNDERDETERMINED_PROPOSAL`, `ATTRIBUTES_AI_PROPOSED_FIELD`,  
`SUPPORTS_HUMAN_REPAIR`,  
and   
`REMAINS_NONCANONICAL_UNTIL_ADMISSION`. These relations establish HLIR's exact corpus role.

This integration establishes four editorial commitments: retain HLIR as the human proposal-and-review layer; adopt the profile envelope and nine-valued lowering result; require field-level provenance and audience-relative legibility evidence; and preserve strict separation among HLIR, canonical MCIR, procedural GCML, executable representations, and realization-stage IR.

## Proposal Custody and Lowering Handoff

The fixed-seed comparison with *The Ableman Wheel*, the Implementation Codex, the constitutional syscall architecture, and *Who Has the Ball?* reveals that an HLIR proposal needs explicit custody throughout review and lowering:

$$
\begin{aligned}
P= (&proposal\_id, head, custodian, authors, reviewers, \\
&ambiguities, authority\_gaps, target, handoff, \\
&acceptance, remainder, disposition)
\end{aligned}.
$$

Authorship, ownership, edit access, assignment, and work custody are separate. The proposal custodian is responsible for advancing, transferring, qualifying, or terminating the current review state; custody does not grant authority to approve the proposal or its effects. A lowering tool or implementation agent does not silently accept custody merely by reading or transforming the artifact.

The Implementation Codex is a downstream realization package only after a selected Instance Constitution / Instance Configuration exists. The constitutional syscall architecture is farther downstream: an HLIR effect proposal can lower into a candidate invocation, but cannot dispatch a device command or manufacture capability and safety authority through syntactic validity.

The Ableman Wheel provides a physical-domain stress case. HLIR can expose alternative apparatus configurations, controls, predictions, and evidence needs for review. Ambiguity or missing authority should return the proposal to a named custodian with a typed remainder, not be guessed away by the lowering agent.

The universal GSM can type   
`CUSTODIES_HLIR_PROPOSAL`, `OFFERS_PROPOSAL_HANDOFF`,  
`ACCEPTS_PROPOSAL_CUSTODY`, `RETURNS_AMBIGUITY_TO_CUSTODIAN`,  
`LOWERS_TO_REALIZATION_PACKAGE`, `PROPOSES_EFFECT_WITHOUT_DISPATCH`,  
and   
`TERMINALLY_DISPOSITIONS_PROPOSAL`.

This randomized review establishes four editorial commitments: adopt proposal custody as part of HLIR; separate authorship, review authority, custody, and lowering execution; require accepted handoffs and typed return of ambiguity; and prohibit syntactic lowering from dispatching or authorizing effects.

## Bidirectional Review Across the Proposal-to-Effect Chain

Eight downstream uses confirm HLIR as a human proposal and repair family rather than a single universal syntax. Communal computing uses local profiles for negotiated practice. Governance as Compilation and GCML place HLIR before canonical admission and procedural lowering. Semantic-fragmentation analysis requires readable forms to expose hidden authority and fallback. The Implementation Codex, constitutional syscall architecture, and Ableman Wheel carry selected proposals toward software or physical realization. Work custody keeps an unresolved proposal attributable through handoff and disposition.

Those uses require a bidirectional field-carriage record:

$$
\begin{aligned}
B= (&proposal, profile, field, source, stage, \\
&authority\_reference, target, fate, loss, remainder, \\
&reviewer, challenge, successor, effect\_boundary)
\end{aligned}.
$$

For every consequential field, `fate` should be one of `PRESERVED`, `REFINED`, `SELECTED`,  
`TRANSLATED`, `DEFERRED`, `REFUSED`, `DROPPED`,  
or `CONFLICTED`. Lowering must produce both a forward result and a reviewable back-projection or semantic diff. A deterministic output is inadequate if the human cannot see that a constraint narrowed, an alternative disappeared, a default entered, an authority reference changed, or a requested effect widened.

Legibility is therefore longitudinal. It must survive revision, lowering, adjudication, selection of an Instance Constitution or Instance Configuration, realization-stage IR, and return from evidence. The review surface should expose exact predecessor, current proposal head, field provenance, unresolved alternatives, authorized losses, downstream consequences, and who may challenge or accept each transition. Acceptance of a diff is not admission, and admission is not effect authority.

The universal GSM can type   
`PROPOSES_FIELD_IN_HLIR`,  
`CARRIES_FIELD_TO_CANONICAL_CANDIDATE`, `BACKPROJECTS_LOWERING_DIFF`,  
`DROPS_FIELD_WITH_DECLARED_LOSS`, `RETURNS_REMAINDER_TO_CUSTODIAN`,  
`CHALLENGES_PROPOSAL_TRANSITION`, `SELECTS_IC_WITHOUT_EFFECT`,  
and   
`PRESERVES_HUMAN_REVIEW_THROUGH_REVISION`.

This reverse-dependency review establishes four editorial commitments: adopt the bidirectional field-carriage record; require forward lowering plus reviewable back-projection; treat legibility as a longitudinal empirical property; and preserve separate proposal, admission, configuration, realization, evidence, and effect authorities.

## 16. Counterevidence and Failure Modes

The proposal should be narrowed or rejected where: (1) human-readable syntax is called legible without study; (2) one audience stands for all; (3) a large schema becomes compliance theater; (4) authors bypass the layer; (5) AI fills fields users do not inspect; (6) well formed is called admissible; (7) lowering is called canonicalization; (8) canonicalization is called admission; (9) admission is called authorization; (10) authorization is called effect; (11) deterministic output is called correct; (12) dependencies are not closed; (13) defaults are hidden; (14) schema versions drift; (15) numeric or ordering behavior varies; (16) equivalent-input rules are undefined; (17) semantic loss is hidden; (18) round trips erase source distinctions; (19) ambiguity is forced into one parse; (20) authority references fabricate authority; (21) credentials exceed proposals; (22) tools bypass HLIR; (23) embedded code defeats containment; (24) macros hide control flow; (25) imports add ambient meaning; (26) validation is undecidable despite contrary claims; (27) refusal gives no repair path; (28) SCI collapses CM1 and CM2; (29) SCI collapses IC and IR; (30) evidence and revision disappear; (31) realization IR is conflated with Intermediate Representation; (32) PEIR name variance is silently merged; (33) MCIR and HLIR duplicate identity; (34) MCIR candidacy is confused with admission; (35) GMB inclusion becomes validity; (36) GSM edges become authorization; (37) corpus works are merged; (38) a specification is presented as implemented; (39) conventional forms perform equally; (40) legibility costs exceed benefits; (41) accessibility fails; or (42) external research contradicts novelty or adequacy claims.

## Human-Legible Does Not Mean Human-Validated

### Public orientation

HLIR is a family of proposal representations between ambiguous intent and canonical machine form. It aims to make structure, authority, assumptions, alternatives, and residual meaning visible before deterministic lowering. In this name, IR means **Intermediate Representation**. It is distinct from the realization-funnel stage IR, which may mean Instance Realization or Implementation Realization.

### Adversarial tests

1. **Legibility theater.** The syntax is readable to its designers but not to intended reviewers. Legibility requires audience-specific comprehension evidence.
2. **False-validation attack.** A human saw the HLIR, so consent or understanding is presumed. Review exposure, comprehension, agreement, and authorization are separate events.
3. **Lowering-loss attack.** Meaning, alternatives, uncertainty, or refusal conditions vanish in the canonical machine form. Lowering must return typed residue and preservation evidence.
4. **Round-trip illusion.** Machine form reprojects into plausible HLIR that differs from the original proposal. Bidirectional checks need property-level lineage, not textual similarity.
5. **Schema-bias attack.** The representation makes only familiar designs expressible. Extensions, escape hatches, and rejected remainder must remain governable.
6. **AI-authorship laundering.** Generated HLIR appears to be a human specification because it is readable. Authorship and adoption require explicit records.
7. **Authority-injection attack.** A proposal contains or inherits permission it was not entitled to assert. Lowering cannot mint authority.
8. **Accessibility and language attack.** A formal notation excludes domain experts, multilingual users, or disabled reviewers. Alternate projections and evaluation are required.

### Claim and evidence ceiling

The paper defines a meta-map and concrete grammars for human-facing proposal layers. It does not establish universal human legibility, lossless lowering, semantic equivalence, adoption, or suitability for every domain. Specification-Configuration-Implementation is one grammar, not the sole HLIR form.

Claims about comprehension, requirements quality, programming-language design, formal verification, accessibility, or collaboration require external comparison and user studies. Internal worked examples establish feasibility only inside their declared profiles. No external research was added in this pass.

### Reader-facing consequence

The public benefit is a reviewable object between conversation and execution: people can inspect what an agent intends to build, which choices were fixed, what authority it claims, what remains unresolved, and what the machine representation must preserve.

## 18. Conclusion

HLIR can provide a useful constitutional front end when it makes proposals easier to understand, challenge, lower, and refuse while preserving the boundary between expression and authority. Its success does not depend on inventing another canonical meaning substrate. It depends on designing human-facing profiles whose relation to MCIR is explicit, reproducible, loss-aware, and reviewable.

The key discipline is simple: an HLIR proposal may become clearer and more machine-processable without becoming canonical, binding, authorized, or real.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of compiler intermediate representations, programming and domain-specific languages, bidirectional transformations and lenses, projectional editing, formal semantics, policy languages, human-computer interaction, cognitive dimensions of notation, accessibility, AI code generation, structured prompting, canonicalization, and usability evaluation.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm2.** The present paper does not claim a complete cm2 treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Evidence.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that human and AI authors reason through goals, alternatives, constraints, authority, uncertainty, evidence, and intended effects. Its nearest external comparison fields are formal, provenance, security. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

DOI: [10.5281/zenodo.23847890](https://doi.org/10.5281/zenodo.23847890)
