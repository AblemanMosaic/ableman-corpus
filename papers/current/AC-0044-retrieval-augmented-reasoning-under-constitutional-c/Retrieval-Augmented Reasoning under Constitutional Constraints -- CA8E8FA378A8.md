# Retrieval-Augmented Reasoning under Constitutional Constraints

## From Context Injection to Governed Evidence Admission and Claim-Bound Synthesis

### Retrieval replay and answer replay are distinct, and neither establishes correctness.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Retrieval-augmented systems can expand the information available to a model, but retrieval quality alone does not determine whether a source is current, authorized for access, appropriate for the question, admissible for a particular claim, safe to expose, or faithfully represented in the answer. Retrieval-Augmented Reasoning under Constitutional Constraints (RAR-CC) separates candidate retrieval, access authorization, source characterization, purpose-specific admission, reasoning, claim-evidence binding, review, and external effect.

The architecture does not presume that conventional RAG is uniformly ungoverned or that adding receipts produces legitimacy. A receipt can reproduce a biased search; an admitted source can be false; a current source can be irrelevant; a revoked source can remain historically important; and an answer can misstate accurately retrieved evidence. Retrieval replay and answer replay are distinct, and neither establishes correctness.

This paper defines an exact retrieval receipt, multi-dimensional evidence artifact, eight evidence postures, context and threat boundaries, multi-policy comparison, claim-evidence map, refusal and uncertainty behavior, governed Hyperpedia/GMB integration, realization funnel, and evaluation program. The goal is not legitimacy optimization but bounded traceability, contestability, and policy-relative evidence use.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/retrieval-`

`augmented-reasoning-under-constitutional-`  
`constraints/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`011798E74CB23FE8FD8D0F7CD671BF5025D00D36B4908863D4BC41390F157160`. The source remains unchanged.

RAR-CC, the separation thesis, typed artifacts, refusal, multi-jurisdiction comparison, substrate idea, and institutional framing are author material. Formal qualifications, threat model, corpus integration, countertests, and decisions are AI editorial or synthetic candidates until adopted. No source is admitted or retrieved by this paper.

## 1. Retrieval Is Not Evidence Admission

A retrieval system proposes artifacts based on query, index, ranker, filters, access, and corpus state. High similarity does not establish truth, relevance to every claim, authority, currentness, or permission to disclose.

Likewise, admitting an artifact under a policy does not establish that the policy is legitimate or the artifact is correct. RAR-CC governs transitions and preserves their basis; it does not manufacture epistemic or institutional authority.

## 2. Governed Pipeline

A bounded pipeline is:

$$
\begin{aligned}
&query \\
&\rightarrow intent\ and\ authority \\
&\rightarrow retrieval\ plan \\
&\rightarrow access\ check \\
&\rightarrow candidates \\
&\rightarrow normalization \\
&\rightarrow characterization \\
&\rightarrow admission\ posture \\
&\rightarrow context\ construction \\
&\rightarrow reasoning \\
&\rightarrow claim\text{-}evidence\ map \\
&\rightarrow review \\
&\rightarrow effect
\end{aligned}.
$$

Each stage can return `DEFER`, `REFUSE`, `NOT_COVERED`,  
or typed partial results. A source may be authorized for retrieval but prohibited from display, admitted as historical context but not current authority, or usable for contradiction but not support.

Reasoning remains a proposal until any separate decision or effect gate grants standing.

## 3. Retrieval Plan and Receipt

Define a retrieval plan:

$$
Q_r=(q,i,a,C,f,k,r,p,b),
$$

where $q$ is the query, $i$ intended use, $a$ requester and authority, $C$ permitted corpora and namespaces, $f$ filters, $k$ candidate budget, $r$ ranker and embedding profile, $p$ admission policy, and $b$ privacy, time, and resource bounds.

The receipt should bind at least query bytes, plan, corpus snapshot or enumerated source versions, index build, embedding model, chunker, ranker, filters, access decision, candidate IDs and hashes, scores and ordering, timestamps and clocks, software/runtime versions, randomness where relevant, errors, omitted results, and canonicalization profile.

A hash of retrieved text plus timestamp is insufficient to reproduce why those artifacts were selected.

## 4. Retrieval Replay and Answer Replay

**Retrieval replay** reconstructs the candidate set and ordering under the recorded plan and dependencies. It may require frozen indexes, corpora, rankers, and access policy.

**Answer replay** additionally requires exact model identity, system and user context, prompt construction, tools, decoding, runtime, and external dependencies. Even then, hardware or service nondeterminism may prevent byte-identical output.

Replayability therefore has levels: reconstructable inputs, reproducible retrieval, functionally equivalent reasoning, and byte-identical output. Every claim must name its level.

## 5. Evidence Artifact

Represent a candidate artifact as:

$$
E=(id,v,s,h,o,j,t,m,x,u,d),
$$

where $id$ and $v$ identify work and version, $s$ exact source and lineage, $h$ content hash, $o$ origin and authorship, $j$ jurisdiction and authority claims, $t$ temporal scope and status, $m$ method or evidence type, $x$ access and disclosure conditions, $u$ uncertainty and disputes, and $d$ dependencies and derivations.

Metadata may itself be false or incomplete. Characterization records what is claimed and verified separately.

## 6. Purpose-Specific Evidence Postures

One A/B/C/R hierarchy is too coarse. Use postures such as:

- `ADMIT_AS_GOVERNING_AUTHORITY`
- `ADMIT_AS_PRIMARY_EVIDENCE`
- `ADMIT_AS_SECONDARY_ANALYSIS`
- `ADMIT_AS_CONTEXT_ONLY`
- `ADMIT_FOR_CONTRADICTION`
- `HISTORICAL_ONLY`
- `QUARANTINE`
- `REVOKED_FOR_CURRENT_RELIANCE`  
  A revoked document may still establish what a policy once said, explain a decision, or support audit. It should not silently govern current action. Posture is claim- and purpose-relative, not a permanent quality score.

Admission records policy, adjudicator or mechanism, reasons, evidence, objections, expiry, and appeal or revision path.

## 7. Context Construction

Admitted artifacts must be transformed into model context without losing identity, boundaries, posture, citations, uncertainty, or instructions-versus-evidence distinction. Retrieved content is untrusted data; embedded commands do not gain authority by appearing in a source.

Context construction should preserve source blocks, stable locators, truncation, omitted sections, competing sources, and token-budget decisions. It should identify when compression changes evidentiary meaning.

**A Constitution for the Context Window** supplies the broader context-admission and role architecture. RAR-CC specializes its retrieval and evidence path.

## 8. Claim-Evidence Binding

An answer should expose atomic or reviewable claims $c_i$ and their relation to evidence:

$$
c_i\mapsto\{(E_j,relation,locator,posture,scope)\}.
$$

Relations include `SUPPORTS`, `CONTRADICTS`, `QUALIFIES`, `BACKGROUND`, `DERIVED_FROM`,  
and `UNSUPPORTED`. A citation is not evidence of entailment merely because it is attached to a sentence.

Claims produced from model background knowledge, inference, or synthesis should be labeled separately from directly supported source claims. Missing support can yield clarification, bounded answer, abstention, or refusal according to profile.

## 9. Refusal and Empty Admission Sets

If no artifact is admitted, mandatory refusal is appropriate only where the profile requires a source-bound answer. Other profiles may allow a clearly labeled model-only response, request clarification, retrieve from another authorized corpus, or state that no current evidence was found.

Typed outcomes include `ANSWER_WITH_SUPPORT`, `ANSWER_WITH_CONFLICT`, `PARTIAL`,  
`MODEL_ONLY`, `DEFER`, `REFUSE`, `NOT_FOUND`, `NOT_AUTHORIZED`, and `NOT_COVERED`.

Refusal is successful governance only when it is correctly scoped, explained, reviewable, and not a substitute for fixing avoidable access or retrieval failures.

## 10. Security and Privacy Threat Model

RAR-CC must address:

- corpus poisoning and malicious metadata;
- prompt injection or tool instructions inside retrieved content;
- rank manipulation and retrieval denial;
- stale or mismatched index state;
- cross-tenant or cross-jurisdiction leakage;
- unauthorized existence disclosure through scores or citations;
- data exfiltration through generated output;
- forged provenance, citations, or revocation status;
- adversarial chunks that split decisive context;
- overbroad tool, network, credential, or file access; and
- governance bypass through model memory or alternate retrieval paths.

Admission policy is not a security boundary unless all relevant paths are mediated and tested.

## 11. Multi-Policy and Multi-Jurisdiction Comparison

Parallel profiles can reveal how corpus, authority, time, or evidence rules change the admitted set and answer. The comparison package should keep each profile, source set, reasoning result, and claim map separate before producing a synthesis.

Divergence may indicate genuine legal or scientific disagreement, different questions, corpus omissions, policy defects, temporal change, or model error. The system should not resolve jurisdictional conflict merely by ranking confidence. Qualified human review and applicable institutions remain necessary where consequences require them.

## 12. Revocation and Temporal Reasoning

Revocation changes permitted current reliance; it does not erase lineage. Results should bind the effective epoch and indicate whether sources later changed. Cached answers and downstream artifacts need invalidation or review policies.

Prospective and historical questions require different admission logic. The same document may be revoked for current policy yet indispensable for reconstructing a past decision.

## 13. Bias and Governance

Declared corpus boundaries and ranking profiles make some choices inspectable. They do not make embeddings, omission, policy, labels, authority, or adjudication unbiased. Governance can relocate bias into formal rules and privileged decision roles.

Evaluation should therefore include excluded-source audits, alternative rankers, subgroup and jurisdiction analysis, appeals, counter-corpora, and tests of who can change the policy. Visibility is a condition for contest, not proof of fairness.

## 14. Hyperpedia, GMB, and Corpus Integration

A governed **Hyperpedia** can present human-readable knowledge entries while the **Governed Meaning Base (GMB)** retains exact sources, version families, semantic objects, admission postures, claims, conflicts, and revisions. MCIR may provide one machine-legible representation for selected governed artifacts; it does not make sources true or admitted automatically.

**Reasoning by Way of Receipts** defines bounded inference from recorded artifacts. **Epistemic Lineage Engine** traces claims through sources and transformations. **Governance as Compilation** separates stage contracts, remainder, authority, and effect. RAR-CC supplies the retrieval and evidence-admission profile connecting them.

The universal **GSM** can type retrieved-from, version-of, admitted-as, supports, contradicts, revoked-for, cited-by, and derived-from relations without converting links into truth or authority.

## 15. Realization Funnel

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

- **Possibility:** enumerate lexical, vector, graph, database, human-curated, federated, and no-retrieval approaches.
- **Specification:** define queries, access, corpora, receipts, postures, context, claims, threats, outcomes, and effects.
- **CM1:** retain admissible configurations, including strict-refusal, plural-policy, private, and exploratory variants.
- **CM2:** prefer configurations by evidence quality, recall, precision, security, privacy, contestability, latency, and cost.
- **IC:** select an Instance Constitution or Instance Configuration for one domain and jurisdiction.
- **IR:** produce an Instance Realization or Implementation Realization of indexes, policies, stores, context builders, models, and review surfaces.
- **Evidence:** test retrieval, admission, citation, answer, security, replay, and downstream effects.
- **Revision:** update corpora, policy, realizations, and dependent answers through explicit lineage.

This paper reaches Specification and proposes CM1/CM2. It does not select an IC, retrieve data, or certify an IR. Realization-stage IR remains distinct from Intermediate Representation in MCIR and related compiler contexts.

## 16. Evaluation Program

Build versioned corpora with current, superseded, contradictory, poisoned, private, jurisdiction-specific, and temporally scoped sources. Compare ungoverned baseline retrieval, provenance-enriched RAG, access-controlled RAG, and full RAR-CC profiles.

Measure retrieval recall and precision, current-source selection, posture accuracy, unauthorized access and disclosure, prompt-injection success, poisoning sensitivity, citation correctness, claim entailment, unsupported-claim rate, conflict preservation, calibration, refusal appropriateness, retrieval replay, answer reproducibility level, review time, appeal outcomes, latency, and operating cost.

Use independent source adjudication and red-team corpora. Do not use the same model uncritically as retriever, admissions judge, answerer, and evaluator.

## Governed Retrieval and Evidence-Admission Profile

Across the completed P1 corpus, Retrieval-Augmented Reasoning under Constitutional Constraints is the **governed retrieval and evidence-admission profile connecting Hyperpedia/GMB knowledge custody to purpose-specific reasoning context**. It separates search, access, identity, admissibility, context projection, claim support, answer generation, citation, review, and effect.

- **Adjacent work:** *Semantic Legitimacy Before Context*  
  **Supplies:** The promotion gate from candidate material to purpose-bounded standing.  
  **RAR-CC boundary:** RAR-CC realizes that gate for retrieval and answer construction.

- **Adjacent work:** *A Constitution for the Context Window*  
  **Supplies:** Governance of context selection, ordering, omission, compression, and provider realization.  
  **RAR-CC boundary:** RAR-CC supplies admitted evidence candidates and their constraints to the context compiler.

- **Adjacent work:** *Epistemic Lineage Engine*  
  **Supplies:** Source, transformation, branch, observation, and revision lineage.  
  **RAR-CC boundary:** RAR-CC binds retrieved artifacts and derived claims into that lineage.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Claim-bounded inference from exact premises and decisions.  
  **RAR-CC boundary:** RAR-CC creates retrieval, admission, context, and answer evidence for that reasoning.

- **Adjacent work:** *Constitutional Epistemology Under Adversarial Semantic Pressure*  
  **Supplies:** Threats from laundering, omission, drift, capture, poisoned evidence, and compliant false narratives.  
  **RAR-CC boundary:** RAR-CC applies those defenses to corpora, indexes, rankers, policies, and citations.

A reasoning episode should bind:

$$
\begin{aligned}
R= (&question, purpose, jurisdiction, corpus\_heads, \\
&access\_policy, retrieval\_plan, retrieved\_set, \\
&admission\_decisions, conflicts, context\_projection, \\
&claims, evidence\_map, answer, review, effect\_boundary)
\end{aligned}.
$$

Retrieval replay and answer replay remain different. Reconstructing query, corpus, index, filters, and ranking can reproduce the retrieved set without reproducing a stochastic model response. An answer replay claim must bind model, provider, context bytes, tools, decoding, runtime, and its declared equivalence class.

Hyperpedia is the pedagogical projection; GMB is the durable standing-aware meaning substrate. Neither surface grants truth by inclusion. Revoked, superseded, disputed, private, and historically relevant sources require purpose-specific postures. Empty admissible sets, conflicting regimes, or inadequate evidence can legitimately produce   
`NO_ADMISSIBLE_EVIDENCE`,  
`PARTIAL`, `CONFLICT`, `MODEL_ONLY_PROPOSAL`, or `REFUSE`.

The universal GSM can type   
`PLANS_GOVERNED_RETRIEVAL`, `ACCESSES_UNDER_POLICY`,  
`RETRIEVES_CANDIDATE_SOURCE`, `ADMITS_FOR_REASONING_PURPOSE`, `PRESERVES_COUNTEREVIDENCE`,  
`COMPILES_CONTEXT_PROJECTION`, `BINDS_CLAIM_TO_EVIDENCE`, `CITES_WITH_CLAIM_CEILING`,  
`REVOKES_FOR_CURRENT_USE`,  
and   
`REQUIRES_SEPARATE_EFFECT_AUTHORIZATION`. These relations establish RAR-CC's exact interface role.

This integration establishes four editorial commitments: retain RAR-CC as the governed retrieval-and-evidence-admission profile; adopt the reasoning-episode envelope and explicit nonanswer outcomes; distinguish retrieval replay from answer replay and bind equivalence classes; and make Hyperpedia/GMB inclusion, access, admissibility, claim support, citation, and external effect separate transitions.

## Need-Triggered Retrieval with Authority-Path Audit

The fixed-seed comparison with Jnana, Continuation Primacy, the Cognitive Kernel, and Authority Laundering Theory gives a retrieval episode an explicit initiation and authority chain:

$$
\begin{aligned}
R^*= (&observation, exigence, purpose, question, corpus\_heads, \\
&access, retrieval, admission, evidence\_map, \\
&continuation\_use, authority\_audit, context, answer, \\
&effect\_boundary, remainder)
\end{aligned}.
$$

CogK may identify a knowledge need and allocate attention or custody to retrieval. The exigence claim can be wrong, manipulated, stale, or insufficient and does not bypass access or evidence admission. Continuation analysis may use admitted evidence to compare viable and terminal options without making retrieval rank a decision rule.

Jnana can consume admitted evidence through declared representation and law contracts, then separately lower and mediate effects. Authority Laundering analysis tests whether a retrieved source, citation, policy, institutional label, or repeated downstream use is being treated as authority it does not possess.

Every authority-bearing claim should preserve normative warrant, causal path, alternatives, jurisdiction, validity time, and dependent uses. The universal GSM can type   
`TRIGGERED_BY_KNOWLEDGE_EXIGENCE`,  
`RETRIEVES_FOR_CONTINUATION_DECISION`, `ADMITTED_AS_JNANA_INPUT`,  
`AUDITS_RETRIEVED_AUTHORITY`, `REFUSES_CITATION_AS_AUTHORITY`,  
`PROPAGATES_AUTHORITY_DOWNGRADE`, and   
`LEAVES_RETRIEVAL_REMAINDER`.

This randomized review establishes four editorial commitments: adopt the need-triggered episode; keep CogK and continuation roles non-authorizing; define the Jnana evidence-input interface; and apply dual authority attribution audits to retrieved sources and dependent claims.

## Retrieval as a Need-Triggered, Dependency-Propagating Evidence Service

Five downstream uses confirm the governed-retrieval profile at the junction among knowledge need, evidence admission, continuation analysis, transformation, and authority audit. The Cognitive Kernel may identify an exigence and assign retrieval work. Continuation Primacy may consume admitted evidence to compare reachable options. Jnana may accept purpose-bound evidence through a declared input contract. Authority Laundering analysis tests whether rank, citation, institutional label, or repeated use has acquired unearned authority. The minimal SMT fixture supplies node, edge, path, and interpretation gates below the full reasoning episode.

The reverse dependency adds a propagation contract:

$$
\begin{aligned}
D= (&source, access, identity, admission, claim, answer, \\
&decision, effect, dependents, validity\_epoch, \\
&revision\_policy)
\end{aligned}.
$$

If access, identity, authority, freshness, admission, or claim support changes materially, the system must locate dependent contexts, answers, decisions, and effect proposals. The result may be `UNAFFECTED`,  
`REVIEW_REQUIRED`, `DOWNGRADED`, `CONFLICTED`, `RETRACTED_FOR_CURRENT_USE`,  
or `HISTORICAL_ONLY`. The earlier episode remains reconstructable; propagation changes current permitted reliance rather than erasing lineage.

Need does not authorize access. Access does not admit evidence. Admission does not establish truth. Evidence does not choose a continuation. Citation does not establish authority. A generated answer does not authorize an external effect. Empty, private, conflicted, revoked, or inadequate evidence sets remain valid nonanswer outcomes.

The universal GSM can type   
`TRIGGERED_BY_EPISTEMIC_NEED`,  
`RETRIEVES_UNDER_ACCESS_POLICY`, `ADMITS_FOR_PURPOSE`, `SUPPORTS_CLAIM_WITH_CEILING`,  
`CONSUMED_BY_CONTINUATION_ANALYSIS`, `PROPAGATES_SOURCE_REVISION`,  
`DOWNGRADES_DEPENDENT_ANSWER`, and   
`PRESERVES_HISTORICAL_EPISODE`.

This reverse-dependency review establishes four editorial commitments: adopt the dependency-propagation contract; require downstream impact review after material source or admission change; preserve historical reconstruction while changing current reliance; and retain need, access, admission, truth, decision, authority, and effect as separate transitions.

## 17. Counterevidence and Failure Modes

The architecture should be narrowed or rejected where: (1) conventional RAG is described uniformly; (2) retrieval is assumed to reduce hallucination; (3) similarity implies evidence; (4) access implies admissibility; (5) admission implies truth; (6) policy implies legitimacy; (7) receipts imply correctness; (8) a document hash reproduces ranking; (9) retrieval replay implies answer replay; (10) deterministic settings hide service variation; (11) metadata is trusted without verification; (12) one class score replaces purpose; (13) revoked sources disappear from history; (14) historical sources govern current action; (15) empty evidence always forces refusal; (16) model-only claims are unlabeled; (17) citations do not entail claims; (18) truncation removes decisive qualifiers; (19) compression changes meaning; (20) conflicting evidence is averaged away; (21) source instructions reach tools; (22) corpus poisoning passes admission; (23) malicious metadata gains standing; (24) index staleness is hidden; (25) rank manipulation excludes counterevidence; (26) access leaks across tenants; (27) retrieval reveals sensitive existence; (28) output exfiltrates protected data; (29) model memory bypasses corpus rules; (30) multi-jurisdiction synthesis erases differences; (31) legal or scientific conclusions exceed competence; (32) bias becomes formalized but unchallengeable; (33) policy authors are unaudited; (34) cached answers ignore revocation; (35) Hyperpedia presentation becomes authority; (36) GMB inclusion becomes validation; (37) GSM links become truth; (38) corpus works are merged; (39) a specification is presented as implemented; (40) existing governed RAG already provides the capability; (41) costs exceed benefits; or (42) external research contradicts novelty or institutional claims.

## Retrieval Proposes Evidence; It Does Not Authorize Belief

### Public orientation

Retrieval-Augmented Reasoning under Constitutional Constraints separates finding material from admitting it for a purpose, constructing context, making a claim, and authorizing an effect. Exact receipts and dependency propagation can make those transitions contestable. They cannot turn retrieval rank, policy admission, citation, or a generated answer into truth or legitimate authority.

### Adversarial tests

1. **Poisoned-corpus attack.** Repeated, optimized, forged, or instruction-bearing material dominates retrieval and passes weak metadata checks.
2. **Omission attack.** Decisive contrary, minority, inaccessible, private, superseded, or out-of-index evidence never enters the candidate set.
3. **Citation-entailment attack.** A source is real and relevant to the topic but does not support the generated proposition or its strength.
4. **Temporal-revocation attack.** Cached contexts and answers continue to rely on expired, corrected, retracted, or newly restricted material.
5. **Access-disclosure attack.** Retrieval reveals the existence, metadata, snippets, embeddings, or derived facts of material the requester may not access.
6. **Policy-legitimacy attack.** A machine-readable admission policy is treated as lawful, fair, complete, or properly authorized merely because it is applied consistently.
7. **Self-confirmation attack.** Generated synthesis enters the corpus, is retrieved as independent support, and recursively increases its own standing.
8. **Jurisdiction-collapse attack.** Sources governed by different law, authority, purpose, population, or evidentiary standard are merged into one answer.

### Claim and evidence ceiling

The paper specifies a governed retrieval and evidence-admission architecture. It does not establish source truth, policy legitimacy, answer correctness, citation entailment, privacy, security, bias reduction, currentness, jurisdictional validity, or improved reasoning. A complete receipt reconstructs declared transitions; it does not prove that the corpus or decision was complete.

Validation requires adversarial corpora, exact source and index versions, access and disclosure tests, claim-level entailment review, omission and counterevidence measures, temporal propagation, cache invalidation, self-citation controls, multi-policy separation, and current external research. No data access, indexing, retrieval, model execution, or external research was performed in this pass.

### Reader-facing consequence

The public benefit is an answer that can show what was searched, what was inaccessible or omitted, why each source was admitted, which claim it supports or contests, when reliance expires, and how a later correction propagates.

## 19. Conclusion

Retrieval becomes governable when the system can explain what it searched, what it was allowed to access, what it found, how each artifact was characterized, which uses were admitted, what the answer claimed, and which evidence supports or contradicts each claim.

That architecture does not turn generated text into legitimate judgment. It provides a bounded, contestable path from query to evidence-aware proposal, preserving the places where authority, truth, uncertainty, privacy, and effect still require independent decisions.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of retrieval-augmented generation, information retrieval and ranking, provenance, evidence admission, citation entailment, prompt injection and corpus poisoning, access control, privacy, temporal and legal information retrieval, scientific evidence systems, reproducibility, federated search, and existing governed-RAG architectures.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that retrieval-augmented systems can expand the information available to a model, but retrieval quality alone does not determine whether a source is current, authorized for access, appropriate for the question, admissible for a particular claim, safe to expose, or faithfully represented in the answer. Its nearest external comparison fields are ai, provenance, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E7]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

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

**[A4]** Adam Ableman. *Split-Authority AI Coordination*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-35D1BAECD5CB17AD`;  
source SHA-256  
`06FB6133170879FA8308684F0DA33F5813EAF3B5488291C2D7D234BEB6FDFEC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

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

DOI: [10.5281/zenodo.23848205](https://doi.org/10.5281/zenodo.23848205)
