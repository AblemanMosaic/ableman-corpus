# Governance as Compilation

## A Bounded Process Architecture for Translating Meaning, Authority, and Law into Effect

### A governance compiler can make selected stages and obligations explicit; it cannot manufacture legitimacy or eliminate ambiguity.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Compiler architecture offers a useful design pattern for governance: staged translation, typed intermediate representations, constraint checking, explicit failure, lowering, effect boundaries, and evidence. Jnana applies this pattern to the path by which language, proposals, law, authority, procedures, and capabilities become actions.

The source argues that governance and compilation solve structurally identical problems and that meaning compiles into legitimate action. The revised claim is bounded. Governance includes interpretation, negotiation, discretion, contest, values, jurisdiction, and social authority that do not reduce cleanly to deterministic translation. A governance compiler can make selected stages and obligations explicit; it cannot manufacture legitimacy or eliminate ambiguity.

This paper defines a governance-compilation envelope, stage contracts, semantic remainder, branch and refusal semantics, authority and effect separation, and correspondence evidence. It distinguishes the process from Crystallized Governance's constitutional artifact, Jnana II's transformation substrate, Everything Is a Compiler's general analytical lens, and MCIR's Intermediate Representation role.

The result is a specification for governable translation, not a claim that law is software, all governance is compilable, or a Jnana compiler presently exists.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. The custody and comparison manifest is   
`work/paper-saturation-v1/evidence/governance-`

`as-compilation/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`CDF08D293A12DDEA5972E6E8AC35CB2D6FB5462DFD13561DFADA258B246DB4DE`. The source remains unchanged.

The compiler analogy, Jnana mapping, meaning-to-machine gradient, refusal correspondence, AI proposer role, and constitutional-computation conclusion are author material. Formal limits, stage contracts, corpus distinctions, tests, counterevidence, and decisions added here are AI editorial or synthetic candidates until adopted. No external research was conducted.

## 1. The Bounded Analogy

Compilers translate under declared grammars and target models. Governance translates claims and proposals under language, law, authority, evidence, procedure, and material conditions. Both can benefit from staged interfaces and explicit failure. They are not identical.

A compiler's output need not be legitimate, and a legitimate decision need not be deterministic. Human interpretation can be constitutive rather than a defect. Governance frequently preserves plural possibilities, equitable discretion, and contest rather than reducing all degrees of freedom.

The paper therefore treats compilation as an architecture for **bounded governed translation**.

## 2. Governance-Compilation Envelope

Define:

$$
\mathcal{G}_p:(N,Q,L,A,E,C)\rightarrow(D,P,X,U,W),
$$

where $p$ is a domain profile, $N$ source meaning and context, $Q$ a proposal or question, $L$ applicable law, $A$ authority, $E$ evidence, $C$ requested capabilities, $D$ a decision, $P$ a procedural plan, $X$ resulting artifact or effect authorization, $U$ unresolved or refused remainder, and $W$ receipts and witnesses.

The function notation does not imply determinism. The same lawful input may permit several decisions, require deliberation, or return `DEFER`,  
`ESCALATE`, or `NOT_COVERED`.

## 3. Stage Contracts

Each stage should declare:

- accepted input types and identities;
- authority to interpret or transform;
- output type and standing;
- obligations expected to persist;
- allowed loss or abstraction;
- unresolved and refused remainder;
- evidence and correspondence checks;
- exceptions and escalation; and
- version and revision relation.

This prevents a later stage from acquiring authority merely because earlier material flowed into it.

## 4. A Governance Compilation Path

A candidate path is:

1. **Intake:** bind source, context, proposal, and standing.
2. **Semantic parsing:** identify terms, claims, ambiguity, conflict, and jurisdiction candidates.
3. **Normalization:** produce a typed Intermediate Representation while preserving source correspondence and remainder.
4. **Law and authority resolution:** identify applicable law, hierarchy, delegation, conflict, and gaps.
5. **Admissibility:** admit, refuse, defer, escalate, or return not-covered.
6. **Procedural planning:** generate a bounded action plan and requested capabilities.
7. **Effect mediation:** authorize and mediate external effects at the declared boundary.
8. **Witness:** record artifacts, effects, partial failures, observations, and claim ceilings.
9. **Revision:** reopen language, law, authority, or implementation through explicit lineage.

The path may branch, loop, or terminate. It is not necessarily a single pipeline.

## 5. Jnana Layer Mapping

GCNL can support controlled semantic intake. MCIR can carry canonicalized meaning under a declared profile. MCIR-Law can evaluate bounded admissibility questions. GCML or PEIR can express procedural realization. Constitutional syscalls and Domain Effects can mediate capabilities and consequences. ReceiptLog can bind evidence.

These are proposed roles. GCNL cannot remove all ambiguity; MCIR cannot represent everything; a law engine cannot decide outside its language; procedural realization can diverge; effect paths can bypass mediation; and receipts can be incomplete.

## 6. Stabilization Without Semantic Erasure

Each stage may reduce one kind of uncertainty while introducing another. Parsing chooses an interpretation; normalization may merge distinctions; law resolution may reveal conflict; planning may add implementation assumptions; effect mediation may encounter reality not represented in the model.

The compiler should carry:

- alternative parses;
- unresolved terms;
- disputed authority;
- missing evidence;
- non-computable judgment;
- protected material;
- target incapacity; and
- translation loss.

Stabilization is governed selection with remainder, not automatic convergence on one meaning.

## 7. Refusal, Deferment, and Error

Syntax error is only a partial analogy for governance refusal. A proposal may be well formed but unauthorized, harmful, outside jurisdiction, unsupported, premature, or constitutionally prohibited. It may also require human judgment rather than rejection.

Typed outcomes include `MALFORMED`, `UNAUTHORIZED`, `INADMISSIBLE`, `INSUFFICIENT_EVIDENCE`,  
`CONFLICT`, `DEFER`, `ESCALATE`, `NOT_COVERED`,  
and `ADMIT`. Each needs a reason, evidence class, effect status, and revision path.

Refusal prevents an unauthorized transformation only where all relevant effect paths are governed.

## 8. Authority and Legitimacy

Authority is an input to the compilation regime, not a product of successful compilation. A machine can verify a token, delegation, quorum, or procedure under a profile. It cannot by that fact establish social legitimacy, moral right, legal validity outside the profile, or consent.

The output should therefore say "admitted under law $L_v$ and authority $A$" rather than "legitimate." Legitimacy may depend on source authority, rights, process, outcomes, and continuing contest.

## 9. Effect and Evidence

A procedural plan is not an effect. An effect authorization is not the effect. A receipt is not proof that the effect corresponded to intent. Keep distinct:

$$
Proposal\neq Decision\neq Plan\neq Grant\neq Effect\neq Evidence.
$$

Partial effects, retries, compensation, unknown outcomes, and irreversible consequences require explicit representation. Evidence should bind the observation regime and claim ceiling.

## 10. AI as Proposer

AI can draft language, propose an Intermediate Representation, identify conflicts, suggest law or procedures, and generate plans. It receives no standing or effect authority from fluency. Proposal, interpretation, admission, grant, effect, and witness should remain separable roles.

The architecture must test prompt, tool, plugin, filesystem, network, credential, package, and human approval paths that may bypass the declared compiler. A constrained proposer is real only if unmediated routes are unavailable or visibly outside the claim.

## 11. Corpus Role Separation

**Governance as Compilation** defines the staged process. **Crystallized Governance** defines the bounded constitutional artifact and source correspondence. **Jnana II** defines the transformation substrate and authority membrane. **Everything Is a Compiler** supplies the wider analytical thesis but does not establish the governance architecture.

**MCIR** is the proposed governed Intermediate Representation. **Meaning as Binding** explains why admitted semantic relations constrain later stages. The **Governed Meaning Base (GMB)** can retain sources, stages, authority, laws, decisions, remainder, effects, evidence, conflicts, and revisions. The universal **GSM** can type stage relations without turning sequence into legitimacy or causation.

## 12. Realization Funnel

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

- **Possibility:** enumerate pipeline, branching, deliberative, hybrid, human-centered, and non-compilable profiles.
- **Specification:** define stage contracts, authority, law, capabilities, outcomes, remainder, effects, and evidence.
- **CM1:** retain admissible configurations, including ambiguous, plural, costly, or incomplete forms.
- **CM2:** prefer configurations by fidelity, rights, inspectability, safety, accessibility, and cost.
- **IC:** select an Instance Constitution or Instance Configuration for one bounded governance process.
- **IR:** produce an Instance Realization or Implementation Realization of parsers, representations, gates, planners, effect mediators, and receipts.
- **Evidence:** test stage correspondence, refusal, bypass, partial failure, contest, effects, and revision.
- **Revision:** amend source, law, stage contracts, and realization through explicit lineage.

This paper reaches Specification and proposes CM1/CM2. It does not select an IC or produce an IR.

In this funnel, IR denotes realization. It remains distinct from Intermediate Representation in MCIR and compiler architecture.

## 13. Evaluation Program

Evaluate a bounded rule process with real source texts, ambiguity, authority conflict, exceptions, and effects. Compare narrative-only, conventional policy-as-code, and governance-compiler conditions. Independent reviewers should inspect source correspondence, remainder, decisions, and effects.

Measures should include source coverage, unresolved remainder, inter-parser agreement, law and authority resolution accuracy, false admission and refusal, not-covered detection, bypass rate, effect mismatch, appeal reversals, latency, accessibility, user comprehension, and maintenance burden.

## Stage-Contract Theory of Governed Translation

Across the completed P1 corpus, Governance as Compilation is the **stage-contract theory of governed translation from source meaning and proposals toward decisions, procedures, grants, effects, evidence, and revision**. It supplies the connecting process grammar for many corpus systems while preserving interpretation, plurality, dispute, and non-compilable remainder. It is broader than one language or substrate and narrower than the claim that all governance is computation.

- **Adjacent work:** *Crystallized Governance*  
  **Supplies:** The bounded constitutional artifact, source correspondence, remainder, adoption, and amendment profile.  
  **Governance-as-Compilation boundary:** Governance as Compilation governs movement among stages rather than the artifact identity alone.

- **Adjacent work:** *Jnana II: Constitutional Transformation Substrate*  
  **Supplies:** A candidate software substrate for admitted transformations, capabilities, effects, and receipts.  
  **Governance-as-Compilation boundary:** Jnana II can realize selected stage contracts but does not define the general process theory.

- **Adjacent work:** *Everything Is a Compiler*  
  **Supplies:** A broad lens for systems that transform representations under constraints.  
  **Governance-as-Compilation boundary:** The governance paper adds authority, rights, effect, evidence, and legitimacy boundaries.

- **Adjacent work:** *Human Legible Intermediate Representation*  
  **Supplies:** Human-facing proposal and review profiles.  
  **Governance-as-Compilation boundary:** HLIR can occupy an intake/normalization interface without receiving admission or effect standing.

- **Adjacent work:** *Governed Controlled Machine Language (GCML)*  
  **Supplies:** A candidate procedural preservation profile.  
  **Governance-as-Compilation boundary:** GCML, if differentiated, is one post-admission stage rather than the compilation theory itself.

Every edge, not merely every node, requires a contract:

$$
\begin{aligned}
e_i= (&source\_role, target\_role, input\_standing, \\
&transform\_authority, preservation, allowed\_loss, \\
&remainder, decision\_kind, evidence, revision)
\end{aligned}.
$$

For a path $e_1,\ldots,e_n$, end-to-end validity is not inferred from local success. Obligations can conflict, be deferred to a named later stage, or fall into a gap. Branches may remain simultaneously admissible; deliberation may create a decision not deterministically recoverable from inputs; effect evidence may reopen an earlier parse or law resolution.

The process therefore supports `PRESERVE`, `REFINE`, `ABSTRACT_WITH_DECLARED_LOSS`,  
`DEFER_TO_NAMED_STAGE`, `BRANCH`, `ESCALATE`, `REFUSE`,  
and `GAP`. `GAP` is a successful detection outcome, not a compilation success. No edge may widen authority merely because its target representation is more executable.

The universal GSM can type   
`ENTERS_GOVERNANCE_STAGE`, `TRANSLATES_UNDER_STAGE_CONTRACT`,  
`PRESERVES_OBLIGATION`, `REFINES_INTERPRETATION`, `CARRIES_SEMANTIC_REMAINDER`,  
`DEFERS_TO_NAMED_STAGE`, `BRANCHES_ADMISSIBLE_OUTCOME`, `WIDENS_AUTHORITY_WITHOUT_GRANT`,  
`MEDIATES_EFFECT`,  
and   
`REOPENS_PRIOR_STAGE_FROM_EVIDENCE`. These relations make the process usable across corpus systems without collapsing them.

This integration establishes four editorial commitments: designate the paper as the stage-contract theory of governed translation; adopt edge-level contracts and the eight-valued transition result; require end-to-end obligation and authority analysis rather than local validation alone; and preserve plural, deliberative, non-compilable, and evidence-reopening paths as normal constitutional outcomes.

## Need-Triggered, Authority-Audited, Disclosure-Preserving Translation

The fixed-seed comparison with the Cognitive Kernel, Authority Laundering Theory, the Integrity Enforcement Layer, and the Suppression Paradox turns governance compilation into a typed transition contract rather than a sequence of successful transformations:

$$
\begin{aligned}
E_s= (&input, output, meaning, authority, loss, remainder, \\
&protected\_constraint, disclosure\_channel, review, \\
&refusal, evidence)
\end{aligned}.
$$

CogK may initiate a proposal because an exigence deserves attention, but the trigger is not admission. Authority Laundering analysis checks the normative warrant and causal path entering and leaving every stage. IEL mediates downstream effects only after the relevant contract, authority, capability, and evidence conditions are satisfied.

The Suppression Paradox adds a necessary negative channel: a material constraint may need to remain operative even when its payload cannot be disclosed broadly. Compilation must therefore preserve an authorized representation of the blocker, its custodian, scope, review path, appeal path, expiry, and remainder without converting secrecy into unreviewable power.

The universal GSM can type   
`INITIATED_BY_EXIGENCE`, `AUDITS_AUTHORITY_AT_STAGE`,  
`CARRIES_PROTECTED_CONSTRAINT`, `DISCLOSES_TO_AUTHORIZED_REVIEW`, `REFUSES_LOSSY_LOWERING`,  
`MEDIATES_EFFECT_THROUGH_IEL`, and   
`RETAINS_UNCOMPILED_REMAINDER`.

This randomized review establishes four editorial commitments: adopt the expanded stage-edge contract; keep CogK initiation below admission; bind dual authority audit and IEL effect mediation to translation; and require disclosure-preserving carriage of protected constraints and remainder.

## A Composable Stage-Contract Graph

Twenty-four downstream uses confirm Governance as Compilation as a stage-contract theory rather than one fixed pipeline. Input profiles include GCNL, HLIR, Meaning Crystals, Semantic Field Analysis, governed retrieval, and Cognitive Kernel proposals. Representation profiles include GOORRT, MCIR topology, ranked DAGs, and Water's flow vocabulary. Procedural and realization profiles include GCML, Jnana II, continual training, the Implementation Codex, ACG, and frozen automata. Authority and effect profiles include Authority Laundering, IEL, enforcement mechanics, and protected disclosure. Crystallized Governance, TDSS, and *Everything Is a Compiler* bound the artifact, diagnostic, and analogy limits.

The reusable edge contract is:

$$
\begin{aligned}
E= (&subject, source\_stage, target\_stage, input\_profile, \\
&output\_profile, transform, carried\_obligations, \\
&authorized\_loss, remainder, authority, reviewer, \\
&effect\_ceiling, evidence, rollback, invalidation)
\end{aligned}.
$$

The compilation topology is a graph with branches, loops, refusal, re-entry, appeal, and revision. Stages are semantic roles under profiles, not universal filenames or one mandatory language sequence. Route composition is valid only when adjacent contracts agree on subject identity, obligation types, authority, accepted loss, remainder, and evidence. A locally valid edge can still create an invalid end-to-end route.

Changes to a source, law, identity, authority grant, profile, dependency, or evidence basis should propagate typed invalidation to downstream artifacts and effects. `RECOMPILE_REQUIRED`,  
`REVIEW_REQUIRED`, `QUARANTINED`, `HISTORICAL_ONLY`, `UNAFFECTED`,  
and `NOT_COVERED` are distinct outcomes. Recompilation does not erase the predecessor route or prove the successor legitimate.

The universal GSM can type   
`INSTANTIATES_STAGE_PROFILE`, `COMPOSES_STAGE_CONTRACT`,  
`BRANCHES_COMPILATION_ROUTE`, `REENTERS_AFTER_REVIEW`, `FAILS_END_TO_END_COMPOSITION`,  
`PROPAGATES_COMPILATION_INVALIDATION`, `RECOMPILES_WITH_REMAINDER`,  
and   
`WITHHOLDS_LEGITIMACY_AND_EFFECT_STANDING`.

This reverse-dependency review establishes four editorial commitments: adopt the composable edge contract; define compilation as a profiled graph rather than a universal linear sequence; require end-to-end route composition checks; and propagate typed invalidation without rewriting predecessor custody or manufacturing legitimacy.

## 14. Counterevidence and Failure Modes

The proposal should be narrowed or rejected where: (1) governance and compilation are called structurally identical; (2) human meaning is assumed deterministic; (3) parsing erases legitimate ambiguity; (4) normalization merges disputes; (5) law is treated as a type system without remainder; (6) authority emerges from pipeline success; (7) admissibility is called legitimacy; (8) one pipeline excludes plural procedure; (9) discretionary judgment is treated as error; (10) alternative parses disappear; (11) protected material is forced public; (12) refusal is reduced to syntax error; (13) not-covered is unavailable; (14) escalation becomes ambient authority; (15) procedural plan is confused with effect; (16) grant is confused with effect; (17) receipt is confused with correspondence; (18) partial effects are omitted; (19) effect paths bypass mediation; (20) AI fluency receives standing; (21) one actor controls all stages; (22) MCIR profile limits are hidden; (23) stage versions cannot migrate; (24) GMB inclusion becomes validation; (25) sequence is treated as causation; (26) corpus papers are merged; (27) a specification is presented as implemented; (28) deterministic replay is claimed without closure; (29) rights and accessibility are omitted; (30) existing policy systems already provide the bounded capability; (31) measured costs exceed benefits; or (32) external research contradicts novelty or structural claims.

## Translation Architecture Cannot Manufacture Legitimacy

### Public orientation

Governance as Compilation uses compiler ideas - staged representations, explicit contracts, typed failure, lowering, effect boundaries, evidence, and revision - to make the path from language and authority to action inspectable. Governance is not literally software compilation. Interpretation, plural procedure, discretion, contest, jurisdiction, and social authority can be constitutive rather than errors awaiting deterministic resolution.

### Adversarial tests

1. **Pipeline-legitimacy attack.** Successful passage through every stage is treated as proof that the rule, authority, or result is legitimate.
2. **Parse-erasure attack.** One interpretation is selected while plausible alternatives, ambiguity, disagreement, or protected context disappear.
3. **Local-edge attack.** Every adjacent translation contract passes but the end-to-end route changes subject identity, drops an obligation, widens authority, or exceeds an effect ceiling.
4. **Law-as-type-system attack.** Open texture, conflict, equitable discretion, changing jurisdiction, and novel cases are reduced to type errors or forced outputs.
5. **Escalation-laundering attack.** A stage returns defer or not-covered, then an escalation path acquires ambient authority without an explicit grant.
6. **AI-fluency attack.** A persuasive proposal or normalized representation acquires decision standing because the model expresses it coherently.
7. **Invalidation-failure attack.** Changes to source, law, identity, authority, profile, dependency, or evidence do not reopen downstream plans and effects.
8. **Effect-correspondence attack.** A valid decision and plan are treated as evidence that the external effect occurred correctly, completely, once, and within scope.

### Claim and evidence ceiling

The paper proposes a profiled graph of composable stage contracts for bounded governed translation. It does not establish structural identity between governance and compilation, deterministic meaning, legal interpretation, legitimacy, complete obligation preservation, or mediated effect. Recompilation creates a successor route; it does not erase or retroactively validate its predecessor.

Claims about compiler theory, law, administrative process, institutions, due process, AI behavior, workflow languages, formal methods, accessibility, or practical benefit require current external sources and exact evaluated profiles. No external research was added in this pass.

### Reader-facing consequence

The public value is seeing every interpretive and authority-bearing handoff between a proposal and an effect, including what was lost, left unresolved, refused, escalated, or invalidated - without calling the resulting action legitimate merely because the route compiled.

## 16. Conclusion

Governance can benefit from compiler architecture without becoming identical to software compilation. Staged representations, explicit authority, typed decisions, remainder, refusal, effect mediation, evidence, and revision make the path from meaning to action more inspectable.

The process does not produce legitimacy automatically. It can faithfully compile an unjust rule, misparse a contested term, omit a right, or fail to mediate an effect. Its constitutional value lies in exposing those transitions and their boundaries to evidence and contest.

Meaning does not simply compile into legitimate action. Under a bounded governance compiler, proposed meaning can be translated into an action admitted under declared law and authority, with remainder and evidence preserved for revision.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of compiler architecture, semantics and translation, legal interpretation, administrative and constitutional process, executable policy, institutional governance, formal methods, human-in-the-loop systems, AI agents, due process, and existing policy and workflow languages.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Revision.** The present paper does not claim a complete revision treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that compiler architecture offers a useful design pattern for governance: staged translation, typed intermediate representations, constraint checking, explicit failure, lowering, effect boundaries, and evidence. Its nearest external comparison fields are governance, formal, security. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E2]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E3]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E6]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E7]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

### Ableman corpus

**[A1]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Governance Engineering*. Ableman Corpus current edition; work identity `PAPER.PUB.18749870`;  
source SHA-256  
`372169F315D192733856B1F4A3F1038BBC73F57CF3ED9ACABAE72B965A69C8D0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Legitimacy Without Self-Ratification*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-EF2382F9397335AC`;  
source SHA-256  
`0186A39C808F8FDDB5C8F42384DF1A26678928434BD50A0EAE8D4947390F68A2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Ableman Corpus current edition; work identity `PAPER.PUB.21095303`;  
source SHA-256  
`EA129ECBA95F7B07CAA7B33A54F91F52913C94A14DA227EB9A06CFD083E4E5BF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Semantic Compilation*. Ableman Corpus current edition; work identity `PAPER.PUB.18453681`;  
source SHA-256  
`5FF6C636550B04DB0E2F6F94C379BB75AA0BD8781E19B047D7D3BB6D49071AC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

Adam Ableman *Semantic Coordinate Identity Tokenization (SCIT).* Zenodo, 2026. doi:10.5281/zenodo.20532070

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847859](https://doi.org/10.5281/zenodo.23847859)
