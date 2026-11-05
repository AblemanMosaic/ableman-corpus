# Governed Controlled Natural Language (GCNL)

## Human-Authorable Semantic Commitments Before Admission and Execution

### Natural language can express nuance, ambiguity, implication, rhetoric, and context that executable systems cannot safely treat as determinate instruction.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Natural language can express nuance, ambiguity, implication, rhetoric, and context that executable systems cannot safely treat as determinate instruction. This paper develops **Governed Controlled Natural Language (GCNL)** as a human-authorable representation layer that constrains grammar, resolves or exposes references, separates epistemic posture from normative force, records asserted authority and provenance, closes scope, preserves residual ambiguity, and produces a canonical semantic candidate for downstream evaluation.

GCNL does not make a statement true, legitimate, authorized, or executable. Governance metadata is a claim about authority, not authority itself. A GCNL compiler may parse, resolve, type, canonicalize, and refuse malformed input; a separately identified law and admission boundary determines whether the resulting candidate may acquire standing or be lowered into GSOL, GOML, MCIR, GCML, PEIR, or another realization profile. This separation keeps a language tool from becoming an undeclared sovereign.

The paper retains the source's **crystallization gradient** and cooling metaphor while treating them as architectural metaphors rather than thermodynamic measurements. It adds a typed statement model, partial compilation semantics, loss and residual records, preservation invariants, a worked example, configuration selection through CM1/CM2/Instance Configuration, adversarial tests, and explicit authorial-compression criteria. The result is a proposal for governable semantic drafting, not a completed language implementation or a proof that controlled prose eliminates interpretation.

## 1. Why Direct Natural-Language Execution Is Unsafe

Natural language permits polysemy, implicit reference, context-dependent scope, unmarked modality, ellipsis, rhetorical emphasis, and contested authority. These are not defects in human communication. They become hazards when a system silently converts one interpretation into an effect.

A direct path from prose to execution can conceal several transitions:

* a description becomes a factual assertion;
* an assertion becomes a requirement;
* a proposal becomes an admitted rule;
* a named speaker becomes an authorized principal;
* a likely referent becomes a canonical identity;
* an omitted condition becomes an unconditional default;
* a parser's selected reading becomes institutional intent;
* a machine-capable action becomes a permitted action.

The central problem is therefore not merely ambiguity. It is **unmarked semantic and authority escalation**.

GCNL inserts an inspectable boundary between fluid prose and formal semantic artifacts. Its job is to make candidate commitments explicit enough to be challenged, refused, deferred, admitted under external law, or lowered with declared gaps.

## 2. Definition and Nonclaims

**Governed Controlled Natural Language (GCNL)** is a versioned family of constrained, human-authorable languages whose statements have deterministic syntactic parses under a declared grammar and explicit fields for semantic identity, scope, epistemic posture, normative force, asserted authority, provenance, evidence, conditions, exceptions, standing, and nonclaims.

GCNL is **controlled** because a profile limits grammar, vocabulary, reference forms, and statement acts. It is **governed** because it represents the information required for downstream governance and refuses or gaps structurally inadequate candidates. The adjective does not mean that the language itself possesses governing authority.

GCNL does not by definition provide:

* truth or empirical validation;
* legal, moral, institutional, or constitutional legitimacy;
* actual authority merely because an authority identifier is present;
* proof that a reference resolution matches author intent;
* complete elimination of ambiguity or interpretive disagreement;
* admission under any particular law;
* permission to execute or perform external effects;
* a production grammar, parser, compiler, runtime, or conformance suite;
* a new foundational representation merely because the profile has a name.

The source's cooling metaphor remains useful: prose is progressively constrained before it can become a formal candidate. Terms such as *entropy*, *annealing*, and *crystallization* are not physical or information-theoretic claims unless a future profile defines and validates a corresponding metric.

## 3. Do Not Collapse the Statement Axes

The source table places observations, assumptions, derivations, decisions, requirements, prohibitions, refusals, and deferrals on one posture axis. These are not the same kind of thing. A GCNL statement should separate at least six dimensions.

- **Dimension:** statement act  
  **Examples:** DEFINE, ASSERT, REPORT, PROPOSE, REQUIRE, FORBID, DECIDE, QUERY, MAP  
  **Question answered:** What communicative or formal act is attempted?

- **Dimension:** epistemic posture  
  **Examples:** OBSERVED, REPORTED, ASSUMED, ESTIMATED, DERIVED, DISPUTED, UNKNOWN  
  **Question answered:** How is the content claimed to be known?

- **Dimension:** normative force  
  **Examples:** NONE, PERMITTED, RECOMMENDED, REQUIRED, FORBIDDEN  
  **Question answered:** What normative force is asserted?

- **Dimension:** authority claim  
  **Examples:** issuer, role, credential, delegation, jurisdiction, validity interval  
  **Question answered:** Who is claimed to have what authority where and when?

- **Dimension:** lifecycle disposition  
  **Examples:** CANDIDATE, ADMITTED, REFUSED, DEFERRED, GAP, REVOKED, SUPERSEDED  
  **Question answered:** What happened under a named procedure?

- **Dimension:** standing and claim ceiling  
  **Examples:** lexical, syntactic, resolved, typed, admissible, evidenced, executable  
  **Question answered:** What may safely be concluded from the current record?

`REQUIRED` and

`FORBIDDEN` are normative forces, not evidence postures. `REFUSED` and `DEFERRED` are procedural outcomes, not contents of the original claim. `DECIDE` is an act whose validity depends on external authority and procedure. `DERIVED` identifies a derivation relation; the compiler that checks the derivation does not thereby become the source of its premises or institutional authority.

This product-of-fields prevents a syntactically valid line from acquiring force through tag confusion.

## 4. Statement and Profile Model

A GCNL profile is bound to a grammar, schema, vocabulary, canonicalization rule, identity-resolution policy, validation policy, and declared downstream interfaces:

$$
P = \langle G,V,\Sigma,K,I,T,C,D \rangle
$$

where $G$ is grammar, $V$ vocabulary, $\Sigma$ schema, $K$ canonicalization, $I$ identity resolution, $T$ typing rules, $C$ constraint validation, and $D$ declared downstream targets.

A statement candidate is:

$$
\begin{aligned}
S = \langle &id, act, content, refs, scope, epi, norm, auth, prov, ev, \\
&time, cond, exc, standing, nonclaims\rangle
\end{aligned}
$$

The minimum fields are profile-dependent, but omission may not silently widen scope or force. Unknown and disputed values must be representable. Every authority claim should identify its source and validity conditions rather than merely naming a class.

The source's initial act vocabulary remains a useful seed:

```text
DEFINE(entity, properties)
REFER(identifier)
ASSERT(claim)
OBSERVE(record)
ASSUME(hypothesis)
REQUIRE(condition)
FORBID(condition)
DECIDE(proposal)
DEFER(topic)
REFUSE(candidate)
MAP(source, target)
```

The grammar should distinguish the *quoted or proposed act* from the *compiler or admission disposition*. For example, an author may write a candidate `REQUIRE` statement; the parser may accept its syntax; an admission procedure may still refuse its authority or scope.

Free pronouns need not be prohibited universally. A profile may admit controlled anaphora when it produces one reviewable referent. What is prohibited is silent reliance on unresolved or multiply resolved identity.

## 5. Compilation and Admission Are Different Operations

The source pipeline can be decomposed into partial functions:

$$
\begin{aligned}
&\operatorname{Parse}_{P}(text) \\
&\rightarrow AST \\
&\mid \operatorname{SyntaxRefusal}
\end{aligned}
$$

$$
\begin{aligned}
&\operatorname{Resolve}_{P}(AST,context) \\
&\rightarrow R \\
&\mid \operatorname{ReferenceGap} \\
&\mid \operatorname{ReferenceRefusal}
\end{aligned}
$$

$$
\operatorname{Type}_{P}(R)
\rightarrow T \mid \operatorname{TypeRefusal}
$$

$$
\begin{aligned}
&\operatorname{Canon}_{P}(T) \\
&\rightarrow G \\
&\mid \operatorname{CanonicalizationGap}
\end{aligned}
$$

Here $G$ is a canonical governed semantic candidate, not an admitted law or executable artifact.

A separate, versioned admission function evaluates the candidate:

$$
\begin{aligned}
&\operatorname{Admit}_{L}(G,context) \\
&\rightarrow \operatorname{Admitted}(A) \\
&\mid \operatorname{Refused}(R) \\
&\mid \operatorname{Deferred}(D) \\
&\mid \operatorname{Gap}(X)
\end{aligned}
$$

Only an admitted artifact may proceed to a declared lowering relation:

$$
\begin{aligned}
&\operatorname{Lower}_{E}(A,target) \\
&\rightarrow artifact \\
&\mid \operatorname{Gap}(X) \\
&\mid \operatorname{Refused}(R)
\end{aligned}
$$

This replaces the source rule based only on membership in `TrustedRoots`. A root identifier is insufficient: authority can be scoped, delegated, time-bounded, revoked, conditional, role-specific, and procedure-dependent. A compiler may validate an authority claim against supplied evidence and current law; it does not create the authority.

The resulting architecture is:

```text
natural-language source
        |
        v
GCNL profile and text
        |
        v
AST -> reference resolution -> typed semantic candidate
        |
        v
canonical candidate + residual/loss record
        |
        v
external law and admission decision
        |
        v
declared semantic or realization targets
        |
        v
effects only through separately authorized boundaries
        |
        v
receipts, observations, gaps, and revision
```

Refusal can be a correct result. It is not automatically a success: an overbroad refusal policy can suppress legitimate expression, conceal parser weakness, or centralize power. Refusal quality must itself be evaluated.

## 6. Canonicalization Must Preserve Residual Meaning

Deterministic parsing does not prove semantic completeness. A sentence can have one AST while remaining underspecified, context-dependent, normatively disputed, or lossy when projected into a target representation.

Every compilation should retain:

$$
\begin{aligned}
B = \langle &source, profile, AST, resolution, typed, canonical, \\
&residual, gaps, nonclaims, revision\rangle
\end{aligned}
$$

The **residual** contains source material or distinctions not represented in the canonical candidate. A **gap** identifies a missing type, unresolved reference, unsupported modality, authority defect, or target limitation. A **nonclaim** states what the compiler result does not establish.

No rhetorical residue should be discarded merely because MCIR, GSOL, or another target cannot carry it. The system may refuse the lowering, attach a sidecar, preserve the exact source, or require author adjudication. Silent omission is not cooling; it is semantic loss.

## 7. GCNL Preservation Invariants

1. **Exact-source binding.** Every candidate binds the exact source text, profile, parser, vocabulary, schema, and canonicalization revision.
2. **Axis separation.** Epistemic posture, normative force, authority claim, disposition, and standing remain distinct fields.
3. **Authority non-creation.** Parsing, validation, and canonicalization cannot create authority absent from the external regime.
4. **Scope non-widening.** Missing or ambiguous scope cannot become a universal default.
5. **Reference honesty.** Each relevant reference resolves uniquely, remains explicitly ambiguous, or causes a typed gap/refusal.
6. **Posture preservation.** Observation, report, assumption, estimate, derivation, dispute, and unknown status cannot silently collapse.
7. **Normative preservation.** Descriptive material cannot silently become permission, requirement, or prohibition.
8. **Residual custody.** Unrepresented source meaning and target loss remain recoverable and reviewable.
9. **Refusal specificity.** A refusal names the violated rule, evidence, scope, and repair or escalation route when one exists.
10. **Lowering conservation.** Downstream transformations preserve identity, scope, force, authority claims, evidence, conditions, exceptions, gaps, and nonclaims or emit an explicit loss certificate.
11. **Effect separation.** A machine-legible candidate does not authorize external effects.
12. **Revision lineage.** Changes to language profile, source, law, admission, target, or evidence create successors rather than rewriting the prior record.

## 8. Worked Example: From Safety Prose to a Governed Candidate

Consider the prose statement:

> The model is safe and may be deployed.

The statement contains at least four unresolved issues: which model revision, what safety property, which deployment context, and who may authorize deployment.

A GCNL candidate might state:

```text
ASSERT claim_id=safety-observation-17
  subject=model:sha256:EXAMPLE
  content="No severity-1 failure occurred in evaluation run run-17."
  epistemic=OBSERVED
  scope="frozen run-17 under profile eval-3"
  evidence=receipt:run-17
  authority_claim="evaluation recorder may report run results"
  standing="candidate empirical record"
  nonclaims="not a general safety or deployment authorization"

PROPOSE proposal_id=deploy-17
  subject=model:sha256:EXAMPLE
  action="limited canary deployment"
  normative_force=PERMITTED_REQUESTED
  scope="jurisdiction j; population p; interval t"
  depends_on=safety-observation-17
  authority_claim="operator role proposes; release authority not
  supplied"
```

Both statements may parse and canonicalize. The second should not be admitted as a deployment permission because the supplied authority claim does not include release authority and one evaluation run cannot discharge the broader safety burden. A correct result is therefore a candidate plus an authority gap and an evidence gap, not an executable deployment artifact.

This example exposes GCNL's value: it makes the hidden escalation visible. It also exposes its limit: the language does not decide what evidence is enough or who legitimately governs deployment.

## 9. Configuration Manifold and the Specification Razor

The source correctly treats GCNL as a configuration family rather than one fixed language. Relevant axes include:

* linguistic restriction: structured prose to formal grammar;
* vocabulary closure: open terms to enumerated domain lexicon;
* reference discipline: controlled anaphora to explicit identifiers only;
* epistemic granularity: coarse postures to typed evidence models;
* normative granularity: recommendations to explicit deontic relations;
* authority representation: source annotation to signed, scoped delegation chains;
* canonicalization strength: stable AST to canonical semantic graph;
* admission coupling: separate review to mechanically enforced law;
* refusal policy: warnings, typed gaps, hard refusal, or human escalation;
* target distance: documentation, GSOL/GOML, MCIR, GCML/PEIR, or effect systems.

The **Specification Configuration Razor** should select the least restrictive profile that still makes the required ambiguities, authority claims, loss, and failure modes explicit for the intended downstream use. Least restrictive does not mean easiest to parse; it means no extra constraint lacking a demonstrated preservation or assurance role.

The configuration stages are:

* **CM1:** all admissible profiles satisfying the declared semantic, governance, authorability, and target constraints, including profiles that are cumbersome, centralized, brittle, or exclusionary;
* **CM2:** preferred profiles that minimize semantic loss, authoring burden, authority concentration, refusal error, profile proliferation, and downstream ambiguity while maximizing accessibility, inspectability, substitution, and evidence quality;
* **Instance Configuration:** the selected grammar, lexicon, schemas, identity service, posture taxonomy, authority evidence, law head, compiler, target mappings, error policy, and conformance suite for a particular use.

The claim that GCNL is a stable attractor in language-design space remains a hypothesis until comparative evidence shows that this region reliably outperforms simpler structured prose and more formal languages for declared tasks.

## 10. Application Profiles

GCNL can be investigated in domains where prose may influence machine action, but every domain needs its own authority and evidence regime.

- **Profile:** scientific method  
  **Candidate contribution:** distinguish observation, assumption, estimate, derivation, and procedure  
  **Required qualification:** structure does not validate data, methods, or inference

- **Profile:** software change  
  **Candidate contribution:** bind requested change, invariants, dependencies, and nonclaims  
  **Required qualification:** commit prose does not prove implementation conformance

- **Profile:** infrastructure policy  
  **Candidate contribution:** expose scope, authority claim, preconditions, effects, and refusals  
  **Required qualification:** compilation does not authorize deployment

- **Profile:** AI safety case  
  **Candidate contribution:** separate measurements, risk models, mitigations, and decisions  
  **Required qualification:** tags do not make the model safe or the decision legitimate

- **Profile:** standards drafting  
  **Candidate contribution:** stabilize terms, modalities, exceptions, and dependency links  
  **Required qualification:** formalization cannot erase interpretive or political dispute

- **Profile:** legal or regulatory drafting  
  **Candidate contribution:** expose actors, jurisdiction, conditions, provenance, and ambiguity  
  **Required qualification:** GCNL is a drafting aid, not enactment, adjudication, or legal validity

- **Profile:** knowledge base  
  **Candidate contribution:** type claims, evidence, standing, conflict, and revision  
  **Required qualification:** admission does not establish truth or identity

Claims about automatic legal encoding, smart-contract enforcement, legislation, medical decisions, or public authority require domain experts, independent review, rights analysis, and explicit effect authorization. A GCNL profile should make those dependencies visible rather than imply that linguistic control resolves them.

## 11. Relation to Existing and Corpus Machinery

### 11.1 External comparison targets

The source names controlled natural languages such as Attempto and Gellish; legal markup such as LegalRuleML and LegalXML; normative standards vocabulary; formal languages such as TLA+, Alloy, and Coq; epistemic logic; proof-carrying code; scientific reporting; and DevOps conventions. These are plausible comparison targets, not established novelty findings in this revision. Further evidentiary strengthening requires current primary-source, feature-by-feature comparison of grammar, semantics, authority, provenance, refusal, canonicalization, and implementation maturity.

### 11.2 Representation stack

GCNL is upstream of formal object, operation, and realization representations, but the exact route is not yet author-adjudicated.

* **GOML** is a candidate home for governed object, role, institution, authority, identity, and state representations [GOORRT].
* **GSOL** is a candidate home for governed operations, transitions, effects, refusals, gaps, receipts, standing, and time [GSOL].
* **MCIR** carries canonical machine-legible constitutional or compilation commitments; admission law must remain distinct from mere serialization.
* **GCML** proposes a machine-facing procedural contract. Its placement relative to MCIR and PEIR is unresolved and should not be used to force GCNL into one premature pipeline [GCML].
* **PEIR** or other execution IRs carry execution-ready structure; they must not recover authority through reachability or compiler capability.

A provisional non-collapsing view is:

```text
human source -> GCNL canonical candidate
              -> GOML object/state profile and/or GSOL operation profile
              -> external admission under declared law
              -> MCIR and declared procedural/execution projections
              -> effects through explicit membranes
              -> receipts, observations, gaps, and revision
```

This diagram is a comparison hypothesis, not an identity merger or canonical stack ruling.

### 11.3 Corpus integrations

* **Global Term Key** provides collision-resistant semantic identity candidates and explicit sense disambiguation for GCNL references [GTK].
* **Meaning as Binding** explains why a label acquires meaning through relations, source overlays, context, and lineage rather than string equality [MAB].
* **Admissibility Engineering** separates candidate construction from the conditions under which a statement may count or proceed [AE].
* **A Constitution for the Context Window** supplies source, role, scope, standing, and compilation-boundary discipline for agent-readable context [CCW].
* **Semantic Fragmentation Analysis** can detect when authority, evidence, exception, or identity remains distributed outside a superficially complete GCNL statement [SFA].
* **Constraint-Bearing Composability** requires the obligations of statements and modules to survive composition and exposes assumptions exported to context [CBC].
* **Reasoning by Way of Receipts** provides evidence-bearing intermediate decisions without treating receipts as self-proving [RWR].
* **The Three Hash Rule** separates exact artifact custody, admissibility commitments, and meaning commitments [THR].
* **Constitutional Epistemology Under Adversarial Semantic Pressure** supplies a threat model for omission, provenance laundering, posture forgery, and authority smuggling [CESP].
* **Governed Meaning Base (GMB)** is the current name in the historical `CCF -> CMB -> GMB` lineage. It can retain GCNL sources, canonical candidates, conflicts, admissions, refusals, gaps, evidence, and revision. GMB does not make a candidate true or executable.
* **Hyperpedia** can expose human-readable projections and source-linked navigation over this material. A presentation layer must preserve standing and nonclaims rather than flattening every structured sentence into fact.

## 12. Authorial Compression Test

GCNL deserves a distinct language identity only if it supplies a normative grammar, abstract syntax, canonicalization, validation semantics, typed failure behavior, and conformance profile not adequately represented as:

* a controlled-authoring profile for GSOL or GOML;
* a schema for governed semantic records;
* a front end for MCIR;
* a policy-as-code authoring convention;
* a bundle of posture and authority annotations.

If those existing mechanisms can express and validate every GCNL obligation, the name should identify a profile or method rather than another foundational language. If GCNL demonstrates a distinct human-authorable semantic layer with stable round-trip behavior and loss-aware lowering across targets, a separate language family may be justified.

This is an author decision. The current candidate preserves GCNL provisionally and makes its distinctness testable.

## Human-Authorable Proposal Language

The completed P1 corpus gives GCNL a bounded role: it is the **human-authorable proposal language for expressing typed semantic commitments before admission, lowering, or execution**. GCNL makes ambiguity, authority, evidence, scope, refusal, and residual meaning inspectable. It is not unrestricted natural language, MCIR, GCML, an admission decision, executable code, or effect authority.

- **Adjacent work:** *The Ableman Format Specification (AFS)*  
  **Supplies:** Format families, profiles, schema and conformance obligations.  
  **GCNL boundary:** GCNL can be an AFS language profile; AFS is the wider family.

- **Adjacent work:** *Governed Controlled Machine Language (GCML)*  
  **Supplies:** A candidate machine-facing procedural representation.  
  **GCNL boundary:** GCNL is human-facing proposal syntax; lowering to GCML requires a declared correspondence contract.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Staged parsing, translation, admission, lowering, and semantic remainder.  
  **GCNL boundary:** GCNL supplies one source language; the compilation architecture supplies the governed process.

- **Adjacent work:** *A Cognitive ABI for Capability-Centered Computing*  
  **Supplies:** Capability contracts, qualification, substitution, and effect ceilings.  
  **GCNL boundary:** A GCNL statement can request a capability but cannot grant or qualify it.

- **Adjacent work:** *Governed Semantic Cartography*  
  **Supplies:** Coordinates, projections, paths, and atlas views.  
  **GCNL boundary:** GCNL may address coordinates and propose traversals; it does not establish their identity or admissibility.

A statement envelope should bind:

$$
\begin{aligned}
S= (&profile, grammar, identity, claim, scope, modality, \\
&authority\_reference, evidence\_reference, \\
&effect\_intent, refusal, residual, source)
\end{aligned}.
$$

Parsing establishes syntactic structure. Canonicalization establishes identity under exact rules. Binding resolves references under a registry. Admission evaluates the proposal under a policy. Lowering creates a machine-facing representation. Execution attempts an authorized effect. Evidence evaluates what occurred. No successful earlier stage implies the next.

Compilation must preserve unresolved or inexpressible source meaning as typed residual rather than deleting it to obtain a valid form. Two statements that canonicalize alike under one profile may differ under another; two distinct statements may be admitted as equivalent only under an explicit relation and evidence. Human readability does not guarantee shared interpretation.

The universal GSM can type `AUTHORED_AS_GCNL`, `PARSED_UNDER_GRAMMAR`,  
`CANONICALIZED_UNDER_PROFILE`, `BINDS_IDENTITY`, `PROPOSES_CLAIM`, `REFERENCES_AUTHORITY`,  
`REFERENCES_EVIDENCE`, `REQUESTS_EFFECT`, `LEAVES_RESIDUAL`, `ADMITTED_BY`,  
`LOWERED_TO_GCML`,  
and `REFUSED_WITH_REASON`. These relations keep expression, decision, realization, and effect separate.

This integration establishes four editorial commitments: adopt human-authorable proposal language as GCNL's official corpus role; adopt the statement envelope; publish the parse/canonicalize/bind/admit/lower/execute/evidence stage separation; and require typed residual preservation for every non-lossless compilation.

## Semantic Proposal Diff and Quality Non-Authority

The fixed-seed comparison with Ontology Laundering, receipt reasoning, GTK, and SBQ gives a consequential GCNL proposal an explicit semantic-diff contract:

$$
\begin{aligned}
D= (&statement, term\_bindings, predecessor, \\
&proposed\_successor, changed\_claims, changed\_burdens, \\
&residual, evidence, authority\_reference, \\
&quality\_profile)
\end{aligned}.
$$

GTK resolves the terms and candidate senses used by the statement. The proposal must disclose which predecessor meanings, classifications, admissibility rules, obligations, or effects would change. Canonicalization that erases this diff or its residual is a compilation failure even if the resulting statement is syntactically valid.

Stage receipts should preserve parsing, identity binding, diff construction, admission, lowering, refusal, and later effect evidence separately. A receipt can show that the proposal was processed under a rule; it cannot establish that the proposal is legitimate or that the successor ontology is true.

SBQ can evaluate coherence, stability, alignment, generativity, and distortion of proposed bindings. Its vector may inform review, but a high profile cannot admit the proposal, establish identity, erase minority meanings, or defeat an Ontology Laundering inquiry. Optimization against SBQ can itself hide changed burdens and residuals.

The universal GSM can type   
`PROPOSES_SEMANTIC_DIFF_IN_GCNL`, `BINDS_TERM_THROUGH_GTK`,  
`CHANGES_ONTOLOGY_BURDEN`, `PRESERVES_PROPOSAL_RESIDUAL`, `RECEIPTS_GCNL_STAGE`,  
`ASSESSED_BY_SBQ_WITHOUT_ADMISSION`, and   
`TRIGGERS_ONTOLOGY_LAUNDERING_REVIEW`.

This randomized review establishes four editorial commitments: adopt the semantic-diff contract; require changed claims and burdens to remain visible through canonicalization; receipt each stage independently; and prohibit SBQ results from conferring admission or semantic standing.

## Human-Authorable Proposal Language with Residual Meaning

Twelve downstream uses place GCNL between human prose and Cognitive ABI, GMB admission, Epistemic IR, both GTK papers, governance compilation, GOORRT, GCML, cartography, ontology-change review, receipts, and SBQ. This supports a bounded role: GCNL expresses inspectable semantic proposals before admission and execution. It is not natural-language programming with inherited authority and not a lossless replacement for unrestricted language.

$$
\begin{aligned}
N^*= (&text, profile, term\_bindings, claim\_types, scope, \\
&epistemic\_posture, authority\_references, conditions, \\
&exceptions, refusals, residual\_meaning, provenance, \\
&version, expiry)
\end{aligned}.
$$

Canonicalization must preserve the original text, binding decisions, unresolved ambiguity, alternatives, culturally or contextually dependent remainder, and versioned registry. Compilation checks representation and declared obligations; admission separately evaluates policy, authority, evidence, consequence, and standing. No sentence can grant its own authority merely by naming an authorized role or compliant form.

Round-trip and differential tests should compare author intent reports, independent readers, canonical form, MCIR output, GCML or operation proposals, refusals, and residual meaning. Profile conformance establishes only the properties tested by the exact grammar, registry, canonicalizer, and vectors.

The universal GSM can type   
`AUTHORS_GCNL_PROPOSAL`, `BINDS_GCNL_TERM`,  
`PRESERVES_RESIDUAL_MEANING`, `COMPILES_GCNL_CANDIDATE`,  
`ADMITS_SEPARATELY_FROM_COMPILATION`, `REFUSES_GCNL_SELF_GRANT`,  
and   
`INVALIDATES_GCNL_PROFILE_RESULT`.

This review establishes four editorial commitments: adopt the proposal record; preserve original prose, ambiguity, alternatives, and residual meaning; separate compilation, admission, and execution; and require versioned profile, round-trip, differential, and self-grant tests.

## 13. Failure Modes, Counterevidence, and Threats

GCNL's claims should be narrowed or rejected when:

* constrained authors routinely misunderstand or misuse the profile;
* profiles fragment into incompatible dialects faster than they stabilize meaning;
* one deterministic parse still supports materially different interpretations;
* required fields create performative metadata that users fill inaccurately;
* authority identifiers are mistaken for valid authority;
* evidence links are stale, circular, forged, inaccessible, or irrelevant;
* residual meaning is lost during canonicalization;
* a simpler schema or form provides equal assurance with lower burden;
* a formal language provides better correctness and comparable authorability;
* refusal rates disproportionately exclude nonstandard language, disabled users, multilingual authors, or legitimate novelty;
* interpreters game tags to launder assumptions into observations or proposals into requirements;
* downstream systems ignore gaps, exceptions, revocation, or nonclaims;
* admission policy becomes centralized, opaque, or politically unchallengeable;
* round-trip projection changes meaning without detection;
* LLM-generated GCNL is treated as valid merely because it is well formed.

Adversarial cases include identifier collision, scope shadowing, Unicode confusables, hidden negation, quotation-versus-assertion confusion, modality laundering, stale delegation, revoked credentials, cyclic derivation, evidence substitution, parser differentials, schema downgrade, canonicalization collision, target-specific semantic loss, and denial by pathological refusal.

The strongest alternative hypothesis is that explicit structured forms plus ordinary review provide most of the benefit, while a GCNL language adds costly ceremony and false confidence. Evaluation must compare against that baseline.

## 14. Conformance and Evaluation Program

A language proposal needs observable conformance, not only examples. A minimum program includes:

1. a versioned grammar and machine-readable schema;
2. canonical encoding rules and test vectors;
3. a reference parser plus an independently implemented parser;
4. positive, negative, boundary, malformed, ambiguous, adversarial, and accessibility fixtures;
5. reference-resolution, type, scope, posture, force, authority, residual, and loss tests;
6. stable refusal and gap codes;
7. round-trip tests from source to canonical form and back to a human projection;
8. cross-profile migration tests;
9. lowering tests into at least two downstream representation families;
10. semantic-difference tests proving that meaningful changes alter canonical commitments;
11. false-refusal and false-admission measurement;
12. authoring studies comparing GCNL with structured prose and formal specification baselines;
13. threat tests for laundering, confusables, stale authority, evidence substitution, and parser disagreement;
14. independent review of domain profiles before any high-consequence use.

A candidate may earn syntactic, resolved, typed, canonical, admitted, lowered, or executed standing separately. Passing one level cannot imply the next.

## 15. Realization Funnel

| Stage | GCNL role |
|---|---|
| Possibility | Explore grammar families, statement acts, posture taxonomies, normative types, authority models, reference policies, refusal strategies, targets, and domain profiles, including harmful or unusable configurations. |
| Specification | Define the exact grammar, vocabulary, schema, identity rules, types, canonicalization, loss model, law interface, failure codes, target mappings, evidence obligations, and nonclaims. |
| CM1 | Enumerate all admissible GCNL profiles satisfying the specification and target constraints, including overconstrained, centralized, inaccessible, costly, or brittle profiles. |
| CM2 | Prefer profiles minimizing semantic loss, false refusal, author burden, authority concentration, dialect drift, and target coupling while maximizing accessibility, auditability, substitution, and correction. |
| Instance Configuration | Select the exact profile, lexicon, schemas, source, identity service, law head, parser, compiler, targets, environment, authority evidence, error policy, and conformance suite. |
| Implementation Realization | Build and run editors, parsers, resolvers, validators, canonicalizers, admission adapters, lowerers, human projections, and receipt paths for that configuration. |
| Evidence | Execute conformance, adversarial, accessibility, authorability, round-trip, loss, refusal, lowering, and independent-implementation tests; retain disagreement and unexplained remainder. |
| Revision | Create successors when grammar, vocabulary, identity, law, authority, evidence, targets, or findings change; preserve migrations, incompatibilities, and invalidated claims. |

The source supplies a rich Specification and sketches multiple Implementation Realizations. It does not supply a conformance implementation or empirical evidence that GCNL improves outcomes.

## 16. Research and Implementation Agenda

1. Adjudicate whether GCNL is a distinct language family or a governed authoring profile over existing representations.
2. Separate the six statement dimensions in a normative schema.
3. Define a minimal grammar and canonical encoding for one low-consequence domain.
4. Define exact source, residual, gap, refusal, nonclaim, and revision records.
5. Specify the external admission interface without embedding sovereignty in the compiler.
6. Build independent parsers and adversarial conformance fixtures.
7. Compare controlled anaphora with identifier-only profiles.
8. Compare GCNL against structured forms, ordinary controlled prose, and a formal specification language.
9. Test lowering to GSOL/GOML and one computational representation while measuring semantic loss.
10. Evaluate accessibility, multilingual use, false refusal, and dialect fragmentation.
11. Conduct current primary-source research across controlled natural languages, legal knowledge representation, deontic and epistemic logic, policy languages, formal methods, proof-carrying code, semantic parsing, requirements engineering, and human-computer interaction.
12. Keep every implementation and external-effect decision behind a separate authorization gate.

## Controlled Language Must Preserve Residual Meaning

### Public orientation

GCNL offers a human-authorable layer in which ambiguous intent can acquire explicit reference, posture, authority, refusal, and admissibility structure before it reaches constitutional execution. A GCNL statement is a governed proposal. It is not executable law, proof of shared understanding, or permission to act merely because it parses.

### Adversarial tests

1. **Parser-authority attack.** The parser's interpretation becomes binding without author confirmation. Parsing, semantic proposal, adjudication, and execution must remain separate stages.
2. **Residual-loss attack.** Ambiguity, nuance, emotion, exception, or unresolved reference is dropped to obtain a clean form. Residue must be returned, typed, and visible.
3. **Controlled-language exclusion.** Required syntax disadvantages non-experts, disabled users, multilingual authors, or domain communities. Accessibility and alternate authoring interfaces need evaluation.
4. **False-precision attack.** A well-formed sentence appears more certain or complete than its evidence. Syntax, semantic standing, evidence, and authority are independent.
5. **Injection and quotation attack.** Embedded text, references, code, or instructions cross interpretation boundaries. Literal, quoted, delegated, and operative content need explicit modes.
6. **Version-drift attack.** Grammar or term bindings change while old statements are reinterpreted silently. Every parse binds grammar, lexicon, policy, and resolver versions.
7. **Refusal-erasure attack.** The system forces a best guess instead of returning ambiguity, conflict, out-of-scope, or insufficient-authority outcomes.
8. **Round-trip illusion.** Natural language -> GCNL -> natural language appears equivalent while obligations or residual meaning changed. Round-trip tests need property-level comparison.

### Claim and evidence ceiling

The paper specifies a proposal language and conformance agenda. It does not establish that GCNL eliminates ambiguity, preserves all authorial meaning, improves safety or usability, or works across languages and domains. Grammar acceptance is not semantic adequacy.

Claims about controlled natural languages, requirements engineering, accessibility, translation, parser security, or user performance require external comparison and evaluation. Internal corpus connections show architectural placement only. No external research was added in this pass.

### Reader-facing consequence

The public promise is a language in which people can state consequential intent more precisely while seeing what the machine inferred, what it could not carry, and why a proposal was admitted, refused, or returned for clarification.

## 17. Conclusion

GCNL identifies a real missing boundary. Natural language can carry intention, evidence, proposals, and rules, but machine systems should not silently decide which interpretation or authority gets to bind. A governed controlled language can make candidate commitments explicit before they enter formal semantic and computational machinery.

The strongest architecture is not `language -> law` as an automatic gradient. It is:

```text
language -> governed candidate -> external admission -> bounded
realization -> evidence and revision
```

GCNL can improve this path by separating statement act, epistemic posture, normative force, authority claim, procedural disposition, and standing; by preserving exact source and residual meaning; and by refusing unsupported lowering. It cannot supply truth, legitimacy, or permission merely through well-formed syntax.

Meaning need not become cold to become meaningful. It must become explicit enough that a machine cannot mistake interpretive power for legitimate authority.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm2.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Instance Configuration.** The present paper does not claim a complete instance configuration treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that natural language can express nuance, ambiguity, implication, rhetoric, and context that executable systems cannot safely treat as determinate instruction. Its nearest external comparison fields are token, formal, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Statistical compression can improve efficiency while destroying distinctions needed for interpretation; semantic labels can conversely overstate stability that usage does not support. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Rico Sennrich, Barry Haddow, and Alexandra Birch. "Neural Machine Translation of Rare Words with Subword Units." *ACL 2016*, pp. 1715-1725. DOI: 10.18653/v1/P16-1162. https://doi.org/10.18653/v1/P16-1162 **Relationship:** Predecessor subword tokenization method used as a contrast to semantically governed token boundaries.

**[E2]** Taku Kudo and John Richardson. "SentencePiece: A Simple and Language Independent Subword Tokenizer and Detokenizer for Neural Text Processing." *EMNLP 2018: System Demonstrations*. DOI: 10.18653/v1/D18-2012. https://doi.org/10.18653/v1/D18-2012 **Relationship:** Predecessor tokenizer implementation used to separate statistical segmentation from semantic admissibility.

**[E3]** Peter D. Grunwald. *The Minimum Description Length Principle*. MIT Press, 2007. [mitpress.mit.edu source](https://mitpress.mit.edu/9780262072816/the-minimum-description-length-principle/) **Relationship:** Predecessor theory of compression and model selection; compression is not assumed to preserve governance or meaning.

**[E4]** Alistair Miles and Sean Bechhofer, eds. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. https://www.w3.org/TR/skos-reference **Relationship:** Adjacent standard for concepts, labels, schemes, notes, and semantic mappings.

**[E5]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E6]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E7]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

### Ableman corpus

**[A1]** Adam Ableman. *Governed Semantic Tokens: Tokenization as an Admissibility Boundary*. Ableman Corpus current edition; work identity `PAPER.PUB.18469507`;  
source SHA-256  
`5C44175B87C514892A0DC9743E09D03893E970AF5419F2E6D9171651BE2A9A54`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Token Parsimony*. Ableman Corpus current edition; work identity `PAPER.PUB.20382825`;  
source SHA-256  
`EC3AA22D32E2BBA21CFCB6D1FA2AE6EA8AC11B7781D19C51530A2F6D924B2E91`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Constitutional Legends*. Ableman Corpus current edition; work identity `PAPER.PUB.20330324`;  
source SHA-256  
`440CE8A83C2F86C020D1E9E482759F71D08F694F1C2250B5B624AEA0A4237AA7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Global Term Key: Identity Primitives in Governed Knowledge Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-358AC09F5A13587E`;  
source SHA-256  
`AFB29CFCB4B58A78B79709AD453CEE9088CCB2AE40F30A70260F1B54F5160579`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Ableman Corpus current edition; work identity `PAPER.PUB.21095303`;  
source SHA-256  
`EA129ECBA95F7B07CAA7B33A54F91F52913C94A14DA227EB9A06CFD083E4E5BF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Governed Semantic Compilation*. Ableman Corpus current edition; work identity `PAPER.PUB.18453681`;  
source SHA-256  
`5FF6C636550B04DB0E2F6F94C379BB75AA0BD8781E19B047D7D3BB6D49071AC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Hybrid Semantic Compiler Architectures*. Ableman Corpus current edition; work identity `PAPER.PUB.21228038`;  
source SHA-256  
`EBCD6DDDA9B547639AEBED79FB68069473CF1248E41C527B48C9624BBE2C0496`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

#### Ableman Corpus references

**[GOORRT]** Adam Ableman. *GOORRT: The Governed Object-Operation-Realization Representation Triad*. Exact reviewed source SHA-256  
`152AB6781AA827519858E0BD8A1811CB1F2C08F56599CD2A61896115742D1399`; unpublished technical companion, with no publication or canonical standing granted here.

**[GSOL]** Adam Ableman. *GSOL v0.1: Governed Semantic Operation Language*. Exact reviewed source SHA-256  
`44F8689BF2FD50670CD25347FB2363491115CA7C049C2BBF71D7286A226DD1AC`. The source identifies itself as a pre-release specification.

**[GCML]** Adam Ableman. *Governed Controlled Machine Language*. Exact reviewed source SHA-256  
`D4E5D935108BDA55157CADDEAD84B94F14868CEDD5CBF72F5184994983AFFB9A`; unpublished source with unresolved identity and stack placement.

**[GTK]** Adam Ableman. *Global Term Key: Constitutional Lexical Identity Through Disambiguated Semantic Binding*. Exact reviewed source SHA-256  
`5F4A36BE1B9CB7DA3A174FCA32AEE74974678D628950F9E2600C647045BD24BB`; separately custodied reviewed source.

**[MAB]** Adam Ableman. *Meaning as Binding*. Exact reviewed source SHA-256  
`A9EA6370E77A71A997F1D1CAC18EF6213125C6F3E13BEEBC9F5E8BFB94FE0B45`; separately custodied reviewed source.

**[AE]** Adam Ableman. *Admissibility Engineering*. Exact reviewed source SHA-256  
`FA80D5895A569839958193735B754BE62EE20E1B399A06CB3BA959614DEBF7A3`; separately custodied reviewed source.

**[CCW]** Adam Ableman. *A Constitution for the Context Window*. Exact reviewed source SHA-256  
`C4F6CC466FA4306C595AFF66D9EBD4F396E45B91876E1D32A5027FCF465312EE`; separately custodied reviewed source.

**[SFA]** Adam Ableman. *Semantic Fragmentation and Constitutional Structure*. Exact reviewed source SHA-256  
`4048182A492E8ED731505426801D7A89074DE7311C0B3D975ECD2A2478D845F8`; separately custodied reviewed source.

**[CBC]** Adam Ableman. *Constraint-Bearing Composability*. Exact reviewed source SHA-256  
`BEEA0B56DBF7DC5274307E95E08AF0576A9F91A729C1962765361ADA34488B62`; supplied Zenodo title match, with exact publication identity to be finalized separately.

**[RWR]** Adam Ableman. *Reasoning by Way of Receipts*. Exact reviewed source SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`; separately custodied reviewed source.

**[THR]** Adam Ableman. 2026. *The Three Hash Rule*. Zenodo. DOI:   
  `10.5281/zenodo.20788617`. Exact reviewed Markdown source SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.

**[CESP]** Adam Ableman. *Constitutional Epistemology Under Adversarial Semantic Pressure*. Exact reviewed source SHA-256  
`909F67AD82D8D8C6119FFEABCC8F885EF8C0A095DE79BFA29A65FDB1DC9E64C3`; separately custodied reviewed source.

The source paper names Attempto Controlled English, Gellish, LegalRuleML, LegalXML, RFC normative vocabulary, TLA+, Alloy, Coq, epistemic logic, proof-carrying code, policy-as-code, and cross-disciplinary stabilization analogies. No complete external bibliography was supplied, and no external research was conducted in this pass. Primary-source comparison is required for a future evidence-qualified revision readiness or novelty claims.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Governed Semantic Operation Language.* Zenodo, 2026. doi:10.5281/zenodo.21214886

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847882](https://doi.org/10.5281/zenodo.23847882)
