# Semantic Legitimacy Before Context

## A Constitutional Framework for Trustworthy Reasoning Systems

### Context may propose; only legitimately admitted meaning may bind.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern information systems use similarity, co-occurrence, retrieval, ranking, memory, and prior interaction to construct context. These signals are useful for discovery, but usefulness does not establish identity, truth, authority, jurisdiction, admissibility, or permission to affect a decision.

This paper develops the **Legitimacy-Before-Binding Principle**: contextual material may enter a candidate or exploratory surface before full adjudication, but it may not acquire governing standing, bind semantic state, authorize inference, or produce consequential effect until the relevant legitimacy conditions have been evaluated. This formulation preserves the original Legitimacy-Before-Context insight while avoiding an impossible requirement that a system know which context matters before using context to discover it.

Legitimacy is not treated as a single confidence score or intrinsic property of text. It is a jurisdiction-relative decision over exact identity, provenance, authority, scope, epistemic support, transformation lineage, temporal validity, conflicts, and intended effect. Evaluation produces typed outcomes--admit, refuse, hold, or admit with bounded standing--and a receipt whose claim ceiling does not exceed the evidence.

The resulting architecture separates **candidate context** from **binding context**. Candidate context can be broad, approximate, plural, and uncertain. Binding context is the governed projection eligible to influence a specified reasoning or effect surface. The Governed Meaning Base (GMB) preserves the durable semantic state, while constitutional context compilation constructs invocation-specific projections under declared rules.

The paper is a conceptual and architectural proposal. It does not prove that legitimacy can be perfectly determined, that admitted claims are true, or that an authority is morally justified. Its contribution is the ordering rule: contextual relevance may nominate material, but it cannot silently promote that material into semantic or operational authority.

## 1. The Problem: Relevance Is Not Standing

Search, recommendation, knowledge graphs, retrieval systems, and language models infer useful relationships from context. Similarity, proximity, repetition, links, and statistical association can identify material worth considering. They cannot by themselves answer:

* Is this the intended entity or revision?
* Is the source eligible to make this claim in this jurisdiction?
* Is the evidence sufficient for the proposed use?
* Has the material been transformed or quoted outside scope?
* Is it current, revoked, contested, or superseded?
* May it guide a model, bind a project, or authorize an effect?

When systems collapse relevance into standing, nearby material can borrow authority; repetition can masquerade as support; retrieved instructions can impersonate policy; model synthesis can return as evidence; and a persuasive projection can become more influential than its source permits.

The problem is not that context exists before legitimacy. Exploratory context is often how a system discovers candidate sources and conflicts. The problem is **promotion without adjudication**: context gains binding force because it is present, ranked highly, repeated, or convenient.

## 2. Core Distinctions

### 2.1 Candidate Context and Binding Context

**Candidate context** is material eligible for search, comparison, challenge, or possible admission. It may be noisy, contradictory, low-confidence, hostile, incomplete, or outside current authority. Its presence carries no automatic standing.

**Binding context** is material admitted for a specified purpose, scope, time, jurisdiction, and effect class. It may guide a model or govern a decision only to the extent of that standing.

The distinction prevents the retrieval layer from becoming an implicit constitutional layer.

### 2.2 Legitimacy, Truth, and Authority

Legitimacy is not truth. A procedurally admissible claim can be false. A true observation can be inadmissible for a particular effect because its identity, custody, acquisition, privacy, or authority is defective.

Authority is also not truth. Authority identifies who may make or bind a kind of declaration under a given order. It does not make the declaration epistemically correct or morally justified.

### 2.3 Provenance and Reliability

Provenance establishes a traceable relation to origins and transformations. It does not establish reliability merely by existing. A false claim can have perfect provenance, and a provenance chain can be complete relative to an instrumented path while an unobserved path remains.

### 2.4 Context and Meaning

Context can alter interpretation without changing source bytes. A binding decision must therefore identify not only the artifact but also the relevant semantic regime, qualifiers, transformation, and surrounding obligations. This is why the GMB lineage and meaning commitments cannot be reduced to retrieval metadata.

## 3. The Legitimacy-Before-Binding Principle

Let $x$ be candidate material, $p$ its proposed purpose, $j$ the governing jurisdiction, $t$ the relevant time, and $e$ the intended effect class. Define a legitimacy evaluation:

$$
\begin{aligned}
L(x,p,j,t,e) \rightarrow \{&\operatorname{ADMIT}, \operatorname{REFUSE}, \\
&\operatorname{HOLD}, \operatorname{BOUNDED}\}
\end{aligned}.
$$

The principle is:

$$
\begin{aligned}
& \\
&\ne g\operatorname{Admitted}(x,p,j,t,e) \\
&\Rightarrow  \\
&\ne g\operatorname{BindingEffect}(x,p,j,t,e)
\end{aligned}.
$$

This does not prohibit the system from retrieving, displaying, comparing, or challenging $x$. It prohibits those exploratory operations from silently conferring binding standing.

An `ADMIT` result grants only the standing named by the decision.

`BOUNDED` may allow quotation but not instruction, retrieval but not persistence, local reasoning but not external effect, or advisory use but not governing use. `HOLD` preserves uncertainty and identifies what evidence or authority is missing. `REFUSE` is a typed outcome, not disappearance.

## 4. Legitimacy Evaluation Surface

A legitimacy decision may require:

| Dimension | Question |
|---|---|
| Identity | Which exact entity, revision, representation, and semantic regime is this? |
| Provenance | From which sources and transformations did it derive? |
| Authority | Who may assert or bind this kind of material? |
| Jurisdiction | Which order, corpus, project, or decision surface governs? |
| Scope and purpose | For what use and audience is the material eligible? |
| Epistemic support | What evidence, method, calibration, and alternatives support it? |
| Temporal status | Is it current, stale, revoked, superseded, or future-effective? |
| Conflict | Which incompatible claims, laws, or interpretations remain? |
| Transformation | Which qualifications, uncertainty, dissent, or obligations may be lost? |
| Effect class | What consequence would binding this material permit? |

Not every decision needs the strongest possible evidence on every dimension. The required profile depends on consequence. A low-risk exploratory query may admit weakly sourced candidates; a medical, legal, financial, infrastructure, or autonomous-effect decision requires stronger evidence and authority.

## 5. Constitutional Semantic Pipeline

The architecture separates discovery from promotion:

```text
source and observation surfaces
  -> candidate discovery
  -> identity and provenance binding
  -> legitimacy and admissibility evaluation
  -> conflict, alternative, and counterevidence search
  -> typed disposition
  -> purpose-bounded context projection
  -> inference or effect request
  -> independent effect authorization where required
  -> receipt, observation, and revision
```

Candidate generation may use contextual similarity, models, human suggestions, or network discovery. The legitimacy gate is downstream of discovery but upstream of binding and effect. This placement preserves search power without allowing search rank to become authority.

Every promotion should produce a decision record naming the evaluated object, purpose, jurisdiction, evidence, alternatives, outcome, standing, expiry, and appeal or revision route. The receipt binds the decision; it does not prove that the evidence was true or complete.

## 6. GMB and Invocation Context

The current architecture is the **Governed Meaning Base (GMB)** under the author-confirmed historical lineage `CCF -> CMB -> GMB`. GMB is the durable semantic state and custody surface: identities, concepts, claims, relations, standing, evidence, conflicts, decisions, and revision lineage can persist there without being flattened into one prompt.

Constitutional context compilation produces a purpose-specific projection from that state. The relation is:

$$
\operatorname{GMBState}
\xrightarrow{\text{legitimacy and admissibility}}
\operatorname{BindingContext}_{p,j,t,e}
\xrightarrow{\text{realization}}
\operatorname{PresentedContext}.
$$

The presented context is not identical to GMB state. It is a bounded projection whose omissions, transformations, order, provider representation, and claim ceiling require evidence. Meaning as Binding explains why presence is insufficient; Governed Context & Memory governs the invocation surface; The Three Hash Rule keeps state, admissibility, and meaning commitments distinct; Semantic Custody preserves responsibility for semantic transformation; Reasoning by Way of Receipts preserves intermediate decisions and debts.

## Semantic Promotion Gate

Across the completed P1 corpus, Semantic Legitimacy Before Context is the **semantic promotion gate that prevents candidate material from gaining binding standing merely through retrieval, repetition, proximity, fluency, or inclusion in a prompt**. Its precise claim is legitimacy before binding context, not legitimacy before discovery or exploratory comparison.

- **Adjacent work:** *A Constitution for the Context Window*  
  **Supplies:** Governance of selection, ordering, omission, compression, instruction priority, and provider realization.  
  **SLBC boundary:** SLBC decides which candidate materials may bind for the stated purpose before that projection is assembled.

- **Adjacent work:** *Constitutional Binding Theory: Governed Anchor Resolution as a Universal Pattern in Semantic Systems*  
  **Supplies:** Identity and anchor resolution under explicit governance.  
  **SLBC boundary:** Correct resolution is necessary but does not itself confer epistemic or effect standing.

- **Adjacent work:** *Constitutional/Crystallized Meaning Base (CMB)*  
  **Supplies:** Historical source architecture in the `CCF -> CMB -> GMB` lineage.  
  **SLBC boundary:** Current synthesis uses GMB; durable inclusion remains distinct from purpose-specific admission.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Records of proposal, evaluation, disposition, evidence, and revision.  
  **SLBC boundary:** A receipt binds the gate event but does not prove the candidate true or legitimate.

- **Adjacent work:** *Constitutional Epistemology Under Adversarial Semantic Pressure*  
  **Supplies:** Claim ceilings, counterevidence, uncertainty, and resistance to authority laundering.  
  **SLBC boundary:** SLBC operationalizes a pre-binding decision surface for those epistemic obligations.

A promotion request should bind:

$$
\begin{aligned}
Q= (&candidate, identity, source, transformations, purpose, \\
&jurisdiction, time, effect\_class, evidence, authority, \\
&conflicts, alternatives, privacy, expiry, appeal)
\end{aligned}.
$$

Its disposition should distinguish `DISCOVERABLE`, `RETRIEVABLE`, `QUOTABLE`, `ADVISORY`,  
`BINDING_FOR_PURPOSE`, `PERSISTABLE`, `EFFECT_ELIGIBLE`, `HOLD`,  
and `REFUSE`. These standings are not a monotone ladder in every jurisdiction: material can be quotable but not persistable, retrievable but not disclosable, or binding for a narrow internal calculation but ineligible for external effect.

The gate must remain plural and contestable. Institutional authority can be defective; minority evidence can be novel but important; a true fact can be privacy-inadmissible; a false claim can have perfect provenance. Consequence-proportionate profiles, declared alternatives, expiry, appeal, and independent downstream effect authorization prevent legitimacy from becoming centralized censorship or an epistemic oracle.

The universal GSM can type   
`DISCOVERS_CANDIDATE_CONTEXT`, `RESOLVES_SEMANTIC_IDENTITY`,  
`REQUESTS_BINDING_STANDING`, `ADMITS_FOR_PURPOSE`, `LIMITS_EFFECT_CLASS`,  
`HOLDS_FOR_CONFLICT`, `REFUSES_CROSS_JURISDICTION_REUSE`, `EXPIRES_ADMISSION`,  
`APPEALS_SEMANTIC_DISPOSITION`,  
and   
`REQUIRES_SEPARATE_EFFECT_AUTHORIZATION`. These relations supply the missing granularity between relevance and consequence.

This integration establishes four editorial commitments: classify SLBC as the semantic promotion gate; adopt the complete promotion-request envelope and typed standing vocabulary; require plural, consequence-proportionate, expiring, and appealable legitimacy profiles; and preserve discovery, retrieval, binding, persistence, and effect authorization as separate transitions.

## Identity-to-Effect Promotion Chain

The fixed-seed comparison with APD, GCML, enforcement mechanics, and the Identity Spine Doctrine clarifies that semantic identity, binding standing, procedural use, enforcement, and effect are distinct transitions:

$$
\begin{aligned}
P= (&identity\_decision, purpose\_standing, procedure, \\
&placement, mediation, effect\_authorization, containment, \\
&evidence, appeal)
\end{aligned}.
$$

The Identity Spine can admit, link, split, fork, supersede, or refuse a concept identity. That decision resolves what candidate material is about; it does not decide whether the material is admissible for a purpose. SLBC assigns the purpose-specific posture and must react when an identity changes or enters review.

GCML may lower binding material into a procedural profile while preserving its purpose, expiry, privacy, and effect limits. Enforcement mechanics can place and mediate the resulting rule, but mechanical completeness cannot cure a defective semantic admission or antecedent authority. APD containment applies only at the declared realized effect surface.

The gate should therefore emit downstream invalidation obligations. If identity, evidence, jurisdiction, authority, or expiry changes, affected context builds, procedures, enforcement structures, effect authorizations, and caches enter `RECOMPUTE_REQUIRED`,  
`CONTESTED`, `QUARANTINED`,  
or another typed posture rather than silently retaining standing.

The universal GSM can type   
`RESOLVES_IDENTITY_BEFORE_PROMOTION`,  
`ADMITS_FOR_BINDING_PURPOSE`, `LOWERS_WITH_PURPOSE_LIMIT`, `PLACED_AS_ENFORCEABLE_RULE`,  
`AUTHORIZED_FOR_EFFECT_SEPARATELY`, `CONTAINED_UNDER_REALIZED_SURFACE`,  
and   
`INVALIDATES_DOWNSTREAM_PROMOTION`.

This randomized review establishes four editorial commitments: adopt the identity-to-effect promotion chain; keep identity and purpose standing separate; require downstream invalidation after material changes; and preserve semantic admission, effect authorization, and APD containment as independent decisions.

## A Multidimensional Promotion Gate with Invalidation Propagation

Eighteen retained downstream uses place Semantic Legitimacy Before Context across context compilation, commitments, cold boot, communal computing, collective coordination, context management, crystallization, adversarial epistemology, procedural lowering, human-legible representation, human validation, identity governance, anti-self-ratification, retrieval, semantic debt, fragmentation analysis, enforcement, and interface-frame risk. This breadth confirms a promotion gate, not a binary truth oracle or centralized censorship mechanism.

$$
\begin{aligned}
L^*= (&candidate, identity, source, transformations, purpose, \\
&jurisdiction, time, epistemic\_posture, privacy, \\
&effect\_class, evidence, counterevidence, authority, \\
&conflicts, alternatives, disposition, expiry, appeal, \\
&dependents, invalidation, revision)
\end{aligned}.
$$

Discovery, retrieval, quotation, advisory use, binding-for-purpose, persistence, procedural lowering, effect eligibility, and effect authority are non-identical and need not form one monotone ladder. A true claim may be privacy-inadmissible; a false claim can have exact provenance; an authoritative source can be wrong; a novel minority claim can be legitimate to investigate without becoming binding.

Every promotion binds a purpose and consequence class. Material change in identity, source, transformation, evidence, authority, jurisdiction, privacy, or expiry propagates typed obligations to dependent contexts, caches, procedures, models, decisions, and effect authorizations. Valid outcomes include `HOLD`,  
`CONFLICT`, `CONTESTED`, `QUARANTINED`, `RECOMPUTE_REQUIRED`,  
and `REFUSE`; refusal requires grounds, scope, expiry where appropriate, and an appeal or revision path.

The universal GSM can type   
`REQUESTS_SEMANTIC_PROMOTION`, `ADMITS_FOR_PURPOSE`,  
`LIMITS_PROMOTION_EFFECT_CLASS`, `PRESERVES_PRIVACY_REFUSAL`, `CONTESTS_PROMOTION`,  
`EXPIRES_PROMOTION`, `INVALIDATES_DEPENDENT_CONTEXT`, `REQUIRES_RECOMPUTATION`,  
and   
`AUTHORIZES_EFFECT_SEPARATELY`.

This review establishes four editorial commitments: adopt the expanded promotion and invalidation record; retain multidimensional nonmonotone dispositions; require plural, appealable, consequence-proportionate profiles; and propagate material change without collapsing identity, truth, legitimacy, admission, persistence, procedure, or effect authority.

## 7. Failure and Counterevidence Conditions

Legitimacy-first systems can fail through:

* **authority capture:** an institution defines itself as the only legitimate speaker;
* **epistemic exclusion:** marginalized or novel evidence cannot satisfy incumbent profiles;
* **false precision:** a score hides contest, plurality, or missing evidence;
* **circular legitimation:** the evaluator derives authority from the material it evaluates;
* **bootstrap opacity:** foundational identities or authority are left undeclared;
* **staleness:** a once-admitted claim continues after its basis changes;
* **context starvation:** overstrict gates prevent discovery or useful low-risk reasoning;
* **laundered transformation:** a summary or model output inherits more standing than its sources;
* **jurisdiction collapse:** standing in one corpus or purpose is reused in another;
* **cost and delay:** evaluation overhead exceeds consequence-adjusted value.

The proposal is weakened if context-first systems with explicit uncertainty and independent effect controls perform as well at lower cost; if legitimacy profiles cannot be calibrated; if admission decisions reproduce institutional bias; or if users cannot inspect and contest the grounds of refusal. These are empirical and governance questions, not exceptions to be defined away.

## 8. Realization-Funnel Placement

| Stage | Legitimacy-before-binding responsibility |
|---|---|
| Possibility | Explore candidate meanings, contexts, authorities, and even undesirable legitimacy regimes. |
| Specification | Define identities, dimensions, outcomes, jurisdictions, claim ceilings, and effect boundaries. |
| CM1 | Enumerate configurations that satisfy the bare model, including captured or exclusionary regimes. |
| CM2 | Prefer transparent, plural, revisable, sovereignty-preserving, evidence-sensitive, and consequence-proportionate regimes. |
| Instance Configuration | Select actual registries, evaluators, evidence profiles, thresholds, expiry, appeal, and effect policies. |
| Implementation Realization | Implement discovery, evaluation, GMB mutation, context projection, provider realization, and effect mediation. |
| Evidence | Test identity, provenance, conflicts, bias, false admission, false refusal, staleness, bypass, cost, and user contestability. |
| Revision | Amend profiles and decisions while preserving predecessor standing, disputes, receipts, and migration history. |

This paper primarily proposes a Specification principle and CM2 preferences. It does not select a complete legitimacy constitution, certify a GMB implementation, or establish empirical benefit.

## 9. Evaluation Program

A comparative evaluation should distinguish:

* candidate-recall and discovery loss;
* false admission and false refusal by consequence class;
* authority and jurisdiction leakage;
* unsupported-claim propagation depth;
* time to detect revocation or staleness;
* preservation of qualifiers through transformation;
* user ability to inspect, contest, and repair decisions;
* machine, human, latency, and privacy cost;
* performance against a simpler context-first system with downstream effect controls.

Negative controls should include relevant but unauthorized text, authoritative but irrelevant text, true but privacy-inadmissible evidence, false claims with perfect provenance, stale previously admitted policy, prompt-injected retrieved instructions, paraphrases that strengthen source claims, and cross-jurisdiction reuse.

No novelty, reliability, or superiority claim is established until this protocol is executed against exact systems and independently reviewed. A current external literature review is also required for a future evidence-qualified revision.

## Legitimacy-First Is a Load-Bearing Profile, Not a Universal Retrieval Rule

### Public orientation

Semantic Legitimacy Before Context argues that authority-sensitive reasoning should not let relevance or usefulness substitute for identity, provenance, standing, and admissible binding. Material should enter consequential context through a promotion gate. Approximate retrieval and exploratory reasoning may still use context-first methods when their outputs remain appropriately bounded.

### Adversarial tests

1. **Authority-capture attack.** The legitimacy gate suppresses dissenting or unfamiliar sources. Issuer, jurisdiction, appeal, plural standing, and provisional lanes are required.
2. **Grounding-regress attack.** Every context item requires prior legitimacy, which itself requires context. The architecture needs declared roots and bounded provisional reasoning.
3. **Exploration-suppression attack.** Low-standing hypotheses cannot be examined because they are not already admitted. Inquiry and consequential reliance need different lanes.
4. **Context-first counterexample.** Approximate retrieval solves a benign task without prior promotion. The thesis must remain claim- and consequence-relative.
5. **Invalidation-gap attack.** A source loses standing but derived contexts and decisions remain active. Dependency and invalidation propagation are required.
6. **Binding-mismatch attack.** A legitimate source is bound to the wrong subject or sense. Legitimacy and correct resolution are distinct tests.
7. **Latency and scarcity attack.** Full adjudication makes timely action impossible. Profiles need budgets, cached standing, expiry, deferral, and emergency rules.
8. **Legitimacy-as-truth attack.** Admitted material is treated as fact. Standing authorizes a role under rules; it does not guarantee truth.

### Claim and evidence ceiling

The defensible thesis is conditional: legitimacy-first promotion becomes load-bearing where reasoning must support verification, authority-sensitive inference, or consequential effects. The paper does not show that every retrieval, brainstorming, or pattern-recognition task needs the same gate.

Claims about reasoning accuracy, retrieval quality, safety, latency, institutional legitimacy, or comparative performance require external evidence and experiments. Internal corpus relations establish architectural necessity under declared assumptions only. No external research was added in this pass.

### Reader-facing consequence

The public result is a context window that can distinguish "useful to consider" from "authorized to rely on," preserve why an item was admitted, and withdraw its downstream influence when its standing fails.

## 10. Conclusion

The central mistake of context-first reasoning is not using context. It is allowing contextual salience to confer standing.

Semantic Legitimacy Before Context is therefore best read as **legitimacy before binding context**. Search, models, networks, and people may generate candidates freely within declared containment boundaries. Promotion into durable meaning, governing context, or consequential inference requires a typed legitimacy and admissibility decision.

This ordering preserves both exploration and constitutional restraint. It allows context to discover possibilities while preventing relevance, fluency, repetition, or proximity from silently becoming authority. It also preserves uncertainty: when legitimacy cannot yet be established, the system can hold, qualify, or refuse rather than invent confidence.

The result is not guaranteed truth. It is a system that can say why material was allowed to bind, for what purpose, under which authority, with what evidence, until when, and with which unresolved alternatives. That is a narrower claim than trustworthy reasoning in full, but it is an essential part of making reasoning inspectable and revisable.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that modern information systems use similarity, co-occurrence, retrieval, ranking, memory, and prior interaction to construct context. Its nearest external comparison fields are ai, governance, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E7]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

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

**[A6]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Adam Ableman. *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18633797.

Adam Ableman. *Semantic Custody*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20300952.

Adam Ableman. *The Three Hash Rule*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20788617.

Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition in the historical CCF -> CMB -> GMB lineage; conceptual claims retain the standing stated in the work.

Adam Ableman. *Meaning as Binding*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *A Constitution for the Context Window*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

External literature research and source verification remain required for a future evidence-qualified revision.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI.* Zenodo, 2026. doi:10.5281/zenodo.18633797

Adam Ableman *Semantic Custody.* Zenodo, 2026. doi:10.5281/zenodo.20300952

Adam Ableman *Semantic Debt.* Zenodo, 2026. doi:10.5281/zenodo.21111666

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848223](https://doi.org/10.5281/zenodo.23848223)
