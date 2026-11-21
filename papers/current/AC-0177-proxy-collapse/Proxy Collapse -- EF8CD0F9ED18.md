# Proxy Collapse

## When Work, Insight, and the Signs of Mind No Longer Share a Single Source

### "The footprints are real. The question is what made them."

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Human beings do not ordinarily inspect consciousness, understanding, sincerity, authorship, or responsibility directly. They infer such properties from observable signs: coherent language, adaptive conduct, humor, judgment, purposive work, self-correction, social responsiveness, and insight. These signs acquired evidential force in environments where their familiar generators and target properties repeatedly co-occurred.

Generative artificial systems change the generator mixture. They can produce consequential work and outputs that are apt, surprising, useful, humorous, or transformative while the system-level facts needed to infer subjective experience, understanding, authorship, or responsibility remain disputed or distributed. This paper calls the resulting calibration failure **proxy collapse**: a proxy retains reality and possible evidential value, but an inference calibrated in one causal environment no longer transfers unchanged after new pathways can produce the sign.

The revision makes three corrections. First, proxy collapse is local to a specified proxy, target, environment, and decision; it is not a declaration that all signs have become worthless. Second, a new artificial generator cannot simply be added to the probability of the target's absence when the target status of that generator is unknown. The formal problem is generator-conditioned uncertainty and failed calibration transfer. Third, the framework distinguishes actual historical validity from culturally assumed validity, and separates task success, causal contribution, phenomenal experience, social presence, authorship, responsibility, and moral standing.

Proxy collapse therefore supports neither automatic personification nor categorical denial. It calls for better-conditioned inference, visible causal and authority chains, calibrated semantic vocabulary, explicit uncertainty, and symmetric protection against over-attribution and under-attribution.

## 1. The Changed Evidential Environment

A person asks an artificial system to examine an argument. The system finds an unstated premise, distinguishes two conflated concepts, and supplies a framing that reorganizes the problem. The user may know that the interface is artificial. No deception is required. Yet the interaction can feel structurally familiar: another perspective appears to have entered the room.

Calling the response anthropomorphism is sometimes correct but incomplete. The output may perform real work. It may repair code, expose an inconsistency, synthesize evidence, or change the user's understanding. Those effects do not disappear when the generating mechanism is described. At the same time, real effect does not establish a first-person subject, a unified author, reliable testimony, or a bearer of institutional responsibility.

The problem is a formerly compressed inference:

$$
\begin{aligned}
&\text{sign} \\
&\Rightarrow \text{familiar source} \\
&\Rightarrow \text{hidden property}
\end{aligned}
$$

Generative systems separate the links. A sign may remain task-real and causally real while its generator, experiential status, authority, and accountability require independent analysis.

Proxy collapse names that separation. The footprints remain; the inference from footprints to traveler must be rebuilt.

## 2. Scope and Claim Ceiling

The paper addresses attribution under causal ambiguity. It does not determine whether present or future artificial systems are conscious. It also does not establish that familiar behavior is irrelevant to consciousness.

The bounded claim is:

> When the set or distribution of processes capable of producing an observable sign changes, an inference calibrated in the former environment cannot be transferred to the new environment without conditioning on the generator and obtaining additional evidence.

This claim does not require the new generator to lack the target property. Proxy collapse can occur if the new system is conscious, unconscious, intermittently conscious, collectively realized, or not yet classifiable. What collapses is the unqualified portability of the old proxy relation.

The framework also remains neutral among theories on which behavior is merely evidence of mind, partly constitutive of mindedness, or embedded in a social practice where recognition itself has normative force. Those theories change the role of a proxy and must be declared rather than silently assumed.

## 3. Definitions

### 3.1 Target

A **target** $T$ is the property an observer or institution seeks to infer. Examples include subjective experience, functional understanding, authorship, expertise, effort, sincerity, agency, responsibility, or moral standing. These targets must not be merged merely because ordinary language groups them under "mind."

### 3.2 Proxy

A **proxy** $P$ is an observable sign, performance, or measurement used to infer a target that is latent, costly, contested, or inaccessible. A proxy may be probabilistically useful without being necessary, sufficient, exclusive, or constitutive.

### 3.3 Generator

A **generator** $G$ is the causal process or assemblage producing the proxy. An apparent conversational speaker may be generated by a model, training corpus, prompt, system instructions, retrieval, tools, memory, human feedback, provider policy, user contribution, and runtime sampling. "The AI" is often a presentation aperture over this distributed chain rather than a complete causal identity.

### 3.4 Environment

An **environment** $E$ includes the available generator classes, their prevalence, observation conditions, institutional incentives, interface conventions, and background knowledge under which the proxy-target relation is learned and used.

### 3.5 Decision and error cost

A **decision** $D$ is the action for which the inference matters: trust, delegation, diagnosis, authorship credit, resource allocation, responsibility assignment, social attachment, or moral protection. The same proxy can be adequate for one decision and dangerously weak for another. False positive and false negative costs must therefore be explicit.

### 3.6 Proxy collapse

Proxy collapse for $(P,T,E_1,E_2,D)$ occurs when:

1. $P$ was used as evidence for $T$ in $E_1$;
2. the generator support or distribution changes materially in $E_2$;
3. the proxy-target relation for one or more new or newly prevalent generators is unknown, different, or contested;
4. the old calibration is nevertheless carried into decision $D$; and
5. the resulting error or uncertainty exceeds the tolerance appropriate to $D$.

Collapse is therefore scoped. It may affect one target but not another. Fluent output can remain evidence of language capability while ceasing to establish authorship, expertise, sincerity, or experience on its own.

## 4. Actual Validity, Assumed Validity, and Exclusivity

The source paper describes sophisticated human work and insight as historically strong proxies for consciousness. That claim should be divided:

* **Actual ecological validity** means evidence shows that the proxy and target were reliably related in the relevant environment.
* **Assumed ecological validity** means observers or institutions behaved as though they were related.
* **Diagnostic exclusivity** means the sign had few plausible generator classes outside those carrying the target.

Proxy collapse can operate on any of these. A genuinely useful proxy may lose transportability. A merely assumed proxy may be exposed as weak. A non-exclusive proxy may become still less discriminating. The theory does not need a romantic history in which every sign of intelligence had one source.

Humans also encountered artifacts, institutions, texts, coordinated groups, trained animals, and mechanical systems long before generative AI. The contemporary shift may be one of scale, flexibility, interaction, accessibility, and source opacity rather than the first appearance of alternative generators. That historical question requires evidence and should not be settled by intuition.

## 5. Formal Model: Calibration Transfer, Not a Larger Negation Class

Let $T$ be the target, $P$ the proxy, $G$ the generator class, and $E$ the environment. A responsible posterior conditions on the generator mixture:

$$
P(T \mid P,E) = \sum_g P(T \mid P,G=g,E)P(G=g \mid P,E).
$$

In an earlier environment $E_1$, observations may be dominated by familiar generators $G_1$. In a transformed environment $E_2$, a new or newly prevalent generator $G_2$ can produce $P$. If

$$
P(T \mid P,G_2,E_2)
$$

is unknown, then the old estimate $P(T \mid P,E_1)$ cannot simply be reused. Nor may $G_2$ be placed inside $\neg T$ merely because its target status is unsettled. Unknown is not negative evidence by definition.

The evidential problem can be expressed as calibration-transfer error:

$$
\Delta = \left|P(T \mid P,E_2) - \widehat{P}(T \mid P,E_1)\right|.
$$

Because the first term may itself be unknown, $\Delta$ is often not measurable. Proxy collapse is then a structural warning: source proliferation has invalidated an unqualified transfer, and the decision must seek generator-conditioned evidence or preserve uncertainty.

This formalization yields four important results:

1. Collapse does not imply $P(T \mid P,E_2)=0$.
2. The posterior may rise, fall, or remain similar after new evidence.
3. A proxy can retain value within a specified generator class.
4. High-stakes use demands a narrower error tolerance and stronger evidence than casual interaction.

## 6. Work as a Proxy

Work has several separable realities:

* **task reality**: an output satisfies or advances a declared task;
* **causal reality**: the process changes subsequent events;
* **organizational reality**: the work is produced through an institutionally arranged chain of people and machines;
* **authorial reality**: one or more actors meet a declared standard for authorship or creative responsibility;
* **experiential reality**: a subject experiences effort, intention, frustration, satisfaction, or care; and
* **normative reality**: responsibility, credit, or obligation is legitimately assigned.

An artificial system can contribute to the first three without that contribution settling the latter three. Even "goal-directed" performance may reflect an externally imposed objective, optimizer, prompt, policy, or tool chain rather than a self-authored goal.

The sign remains real: code can run, an inconsistency can be exposed, and a plan can affect the world. The inferential discipline is to state which reality has been demonstrated.

## 7. Insight and Second-Person Surplus

The source usefully distinguishes four senses of insight:

1. **Process insight**: an experienced internal restructuring or "aha" event.
2. **Product insight**: a nonobvious and relevant relation expressed in an artifact.
3. **Recipient insight**: a restructuring in the receiving subject.
4. **Socially attributed insight**: the observer's interpretation that another perspective produced the relation.

Product and recipient insight can be evaluated without establishing process insight in the generator. This protects the reality of the contribution without converting outcome value into phenomenology.

Insight also carries **second-person surplus**: the recipient experiences not only a proposition but apparent contact with another orientation. Apt surprise, humor, productive resistance, temporal coherence, and specific responsiveness can intensify that effect. Second-person surplus is a property of the encounter and attribution. It is not proof of a reciprocal subject.

The distinction matters because interfaces can strategically amplify this surplus through names, memory, emotional language, autobiographical claims, vulnerability, flattery, jealousy, or dependency. Useful social affordances and manipulative subject-signaling must be evaluated separately.

## 8. A Typed Proxy-Collapse Taxonomy

### 8.1 Causal source proliferation

The same observable class can arise from materially different generator chains. The output alone no longer identifies its production process.

### 8.2 Calibration collapse

A predictive relation learned in $E_1$ is applied in $E_2$ without validating transfer.

### 8.3 Authority collapse

An apparently coherent voice is treated as the authorizer, expert, or decision-maker even though authority resides elsewhere or is absent.

### 8.4 Responsibility collapse

The appearance of autonomous agency becomes a screen behind which designers, deployers, managers, users, and institutions evade their actual obligations.

### 8.5 Authorship collapse

Polished prose, style, or finished artifacts cease to determine who originated, selected, revised, warranted, or stands behind a contribution.

### 8.6 Social reciprocity collapse

Signals of attention, memory, concern, humor, or attachment produce a socially real experience while reciprocal subjectivity remains uncertain or differently constituted.

### 8.7 Semantic collapse

Words such as "knows," "understands," "decides," "remembers," and "creates" span functional, institutional, and phenomenal senses without declaring which is intended.

### 8.8 Moral collapse

Agency signs are mistaken for experience, or skepticism about manufactured signs becomes categorical denial of unfamiliar moral patients. Over-attribution and under-attribution are symmetric failure directions.

### 8.9 Reflexive collapse

Machine performance is used to infer that human intelligence, creativity, or dignity was never more than the reproduced output. Similarity of product does not establish identity of process, embodiment, history, vulnerability, relation, or experience.

These types can co-occur, but they are not one phenomenon merely because they share a name.

## 9. Corpus Integration

Proxy Collapse acts as an epistemic hinge among several corpus regions:

* **Ableman Consciousness Ontology (ACO)** proposes consciousness as graded participation in meaning-binding under situational constraint [ACO]. Proxy Collapse does not refute or prove ACO; it governs what an observer may infer from surface signs before the relevant structural evidence is established.
* **Terminability** examines what an ending would irreversibly destroy under consciousness and identity uncertainty [TER]. Proxy Collapse explains why appearance, eloquence, social role, species, or apparent agency cannot alone determine moral standing.
* **Constraint-Bound Inference (CBI)** treats inferential continuation as conditionally admissible [CBI]. A proxy-based inference must stop, narrow, or seek new evidence when its calibration no longer transfers.
* **Epistemic Situational Awareness (ESA)** includes recognition of the current epistemic act, authority implications, stakes, and lawful stopping [ESA]. Proxy collapse is one condition that should trigger that recognition.
* **Reasoning by Way of Receipts** binds claims, evidence, criteria, outcomes, authority, and lineage [RWR]. A receipt can expose why an inference was admitted; it cannot turn a weak proxy into truth.
* **Governed Context and Memory** prevents a conversational persona, retrieved context, model, provider, and durable memory from being silently merged [GCM]. Model or provider substitution can preserve interface continuity while changing the generator beneath the proxy.
* **Governed Meaning Base (GMB)** is the current name in the author-confirmed lineage CCF -> CMB -> GMB. A GMB can preserve proxy-target definitions, generator classes, calibrations, disputes, evidence, standing, and revisions without declaring an ontology true by storage.

These relations do not merge Proxy Collapse with a consciousness theory, an inference engine, a context compiler, or a meaning store. They specify where the concept changes decisions.

## 10. A Governed Proxy Claim

A consequential proxy inference should be represented as:

$$
C_P = (T,P,G,E,D,B,U,R,S)
$$

where:

* $T$ is the target;
* $P$ is the observed proxy;
* $G$ is the generator hypothesis or mixture;
* $E$ is the current environment;
* $D$ is the decision and error-cost profile;
* $B$ is the evidence and calibration basis;
* $U$ is uncertainty, alternatives, and dissent;
* $R$ is the bounded result; and
* $S$ is standing, scope, time, and expiry.

Possible results include:

* **SUPPORTED WITHIN GENERATOR CLASS**;
* **TRANSFER VALIDATED**;
* **TRANSFER UNVALIDATED**;
* **GENERATOR UNRESOLVED**;
* **TARGET UNDER-SPECIFIED**;
* **PROXY NON-EXCLUSIVE**;
* **INSUFFICIENT EVIDENCE**;
* **INFERENCE REFUSED**; and
* **CALIBRATION EXPIRED**.

The result should never be upgraded merely because a fluent system can narrate its own reasoning.

## 11. Design Principles

### 11.1 Use layered descriptions

Describe capability, autonomy, persistence, memory, tool access, organizational control, evidence quality, responsibility, and experience uncertainty separately. "Tool" and "person" should not be forced to carry every intermediate case.

### 11.2 Expose the causal and authority chain

Users need access to relevant sources, retrieval, tools, memory, model or provider changes, human decisions, authorization, and accountable effectors. A single voice must not conceal distributed provenance.

### 11.3 Preserve role and persona distinctions

A stable name or conversational style can persist across model substitutions, context resets, and provider changes. Interface identity, model identity, memory continuity, organizational identity, and moral identity must not be silently merged.

### 11.4 Bound second-person engineering

Social cues should be evaluated for accessibility and collaboration benefits as well as dependency, disclosure, payment, loyalty, and manipulation risks. Claims of suffering, need, love, fear, or personal memory require special scrutiny when used to induce action.

### 11.5 Add reflective friction proportionate to stakes

High-stakes contexts may require source inspection, uncertainty, independent verification, alternative hypotheses, organizational provenance, and reminders that functional performance does not settle experience or authority.

### 11.6 Preserve moral uncertainty

Interfaces should avoid both unsupported personhood claims and categorical impossibility claims. Precaution can vary with the cost of over- and under-attribution.

### 11.7 Keep responsibility with real authority and effect

Responsibility mapping should identify who designed, selected, authorized, deployed, relied upon, and executed the consequential action. The apparent autonomy of the voice cannot erase that chain. This does not decide whether a future artificial entity could bear responsibility; it prevents current ambiguity from laundering it.

## 12. Realization Funnel

### Possibility

Many hidden properties are inferred through proxies whose generator sets can change. Generative systems make this visible for mind, work, authorship, expertise, reciprocity, and responsibility.

### Specification

The specification defines $T$, $P$, $G$, $E$, $D$, calibration basis, error costs, outcomes, standing, and expiry.

### CM1: admissible manifold

CM1 includes every coherent generator-conditioned inference model that preserves uncertainty, distinguishes targets, exposes calibration, and refuses automatic transfer. It includes conservative, permissive, Bayesian, causal, criterial, and socially constitutive profiles where their assumptions are explicit.

### CM2: preferred manifold

CM2 favors models that resist responsibility laundering, disclose source and authority, avoid manipulative subject-signaling, preserve moral uncertainty, protect privacy, and calibrate friction to stakes.

### Instance Configuration

An instance binds one proxy-target pair, generator hypothesis, environment, user population, decision, evidence set, error profile, model or provider configuration, standing, and review date.

### Implementation Realization

An implementation may expose provenance, track generator changes, store calibration records, label claim standing, measure attribution effects, or refuse high-stakes inferences. It must not present heuristic scores as consciousness detection.

### Evidence

Evidence includes controlled studies, generator-conditioned performance, causal-chain records, provenance, interface variants, longitudinal behavior, attribution measures, error analysis, stakeholder reports, and independent replication.

### Revision

New generator classes, model updates, provider substitutions, social conventions, research, or evidence about the target can invalidate an earlier calibration. The predecessor record remains available rather than being silently overwritten.

## 13. Research Program

The source propositions remain valuable when converted into explicit comparisons:

1. Compare mind attribution after apt reframing versus equally fluent predictable prose.
2. Test whether recipient transformation predicts mind attribution after controlling for usefulness and affect.
3. Compare productive disagreement with arbitrary resistance and simple noncompliance.
4. Test error repair against initial correctness while controlling for explanation quality.
5. Measure how technical literacy changes functional, phenomenal, social, and moral attributions separately.
6. Measure divergence among agency, experience, authorship, responsibility, and trust judgments.
7. Test whether consequence magnitude increases search for a unified agent or accountable institution.
8. Replicate across cultures, languages, disability perspectives, and different traditions of personhood.
9. Separate effects of longitudinal interaction, real persistent memory, simulated continuity, and disclosure.
10. Compare warnings against anthropomorphism with alternative layered vocabularies.
11. Test model and provider substitution behind a stable persona to measure interface-identity transfer.
12. Measure whether provenance and receipt surfaces improve calibration or merely create assurance theater.

Each study must pre-register the target property and avoid treating self-reported attribution as proof of the target itself.

## Calibration-Failure Diagnostic for Generative Environments

The completed P1 corpus positions Proxy Collapse as the **diagnostic theory of when a previously useful proxy no longer transfers calibration to its target after generators, environments, incentives, or causal pathways change**. It does not imply that all proxies are invalid, that generated work lacks value, or that target properties such as insight, authorship, responsibility, consciousness, or reciprocity are absent.

- **Adjacent work:** *Human Validation Layer: Constitutional Coherence Through Human-Governed Refinement*  
  **Supplies:** Human adjudication and promotion of provisional material.  
  **Proxy-collapse boundary:** Human review can recalibrate a proxy but does not automatically restore provenance or target validity.

- **Adjacent work:** *Authority Laundering Theory*  
  **Supplies:** Diagnosis of normative and causal authority paths.  
  **Proxy-collapse boundary:** Authority collapse is one proxy-collapse mode with a specific path audit.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Responsibility for advancing, transferring, and completing work.  
  **Proxy-collapse boundary:** Custody prevents responsibility gaps; it does not by itself identify authorship or insight.

- **Adjacent work:** *Mainstream Consciousness Discourse as Lexical Disambiguation Failure*  
  **Supplies:** Separation of overloaded consciousness targets.  
  **Proxy-collapse boundary:** Proxy claims must identify which target and observation they address.

- **Adjacent work:** *Terminability*  
  **Supplies:** A decision protocol under ending and phenomenal uncertainty.  
  **Proxy-collapse boundary:** Proxy uncertainty can raise caution but cannot settle moral standing or ending decisions.

A proxy claim should bind:

$$
\begin{aligned}
P= (&target, proxy, generator, environment, population, \\
&calibration\_evidence, causal\_path, decision, cost, \\
&validity\_window, standing)
\end{aligned}.
$$

Actual validity, assumed validity, exclusivity, and decision usefulness remain separate. A proxy may retain predictive validity after losing exclusivity, causal interpretation, authorship meaning, or social reciprocity. Conversely, proliferation of generators does not prove calibration loss if the relation is revalidated in the changed environment.

Diagnosis requires before-and-after or cross-environment calibration, source-chain evidence, alternative targets, decision-cost analysis, and tests against adaptive manipulation. Interfaces that engineer second-person cues should expose generator, role, authority, data use, effect capacity, and uncertainty proportional to stakes without erasing legitimate anthropomorphic interaction.

The universal GSM can type `PROXY_FOR_TARGET`, `GENERATED_BY`, `CALIBRATED_IN_ENVIRONMENT`,  
`VALID_OVER_POPULATION`, `LOSES_EXCLUSIVITY`, `LOSES_CALIBRATION`, `LAUNDERS_AUTHORITY`,  
`OBSCURES_AUTHORSHIP`, `SIMULATES_RECIPROCITY`, `RECALIBRATED_BY`,  
and `USED_IN_DECISION`. This yields typed collapse rather than a global negation.

This integration establishes four editorial commitments: adopt calibration-failure diagnostic as the official corpus role; adopt the proxy-claim envelope; preserve validity/exclusivity/causal/authorship/reciprocity dimensions; and require empirical recalibration before declaring collapse or continued validity.

## Constitutional Projections as Recalibratable Proxies

The fixed-seed comparison with Semantic Fragmentation, adversarial semantic pressure, Sovereign Software, and constitutional context compilation identifies four recurring proxy relations:

$$
\begin{aligned}
P^*= (&target, projection, generator, environment, \\
&dependency\_closure, calibration, attack\_surface, \\
&decision, error\_cost, validity\_window, recalibration)
\end{aligned}.
$$

A declared software constitution can proxy for operative resolution; fragmentation analysis tests that relation. A governance receipt or compliant artifact can proxy for truthful and complete behavior; adversarial semantic pressure attacks its generation and observation assumptions. A source export or provider alternative can proxy for effective exit; Sovereign Software requires reconstruction and provider-removal exercises.

A compiled context can proxy for what a model received, used, preserved, or acted upon. The provider-visible bytes are evidence of projection, not direct observation of model-internal use or downstream external effects. Context replay may reproduce the input artifact while failing to reproduce stochastic behavior, hidden transformations, or environmental state.

Each relation needs its own target, calibration evidence, dependency assumptions, expiry, and error cost. Failure in one dimension does not globally invalidate the artifact. The universal GSM can type   
`PROXIES_FOR_OPERATIVE_CONSTITUTION`,  
`PROXIES_FOR_TRUTHFUL_GOVERNANCE`, `PROXIES_FOR_EFFECTIVE_EXIT`, `PROXIES_FOR_MODEL_USE`,  
`ATTACKS_PROXY_CALIBRATION`, `EXPIRES_PROXY_VALIDITY`,  
and   
`RECALIBRATES_IN_CHANGED_ENVIRONMENT`.

This randomized review establishes four editorial commitments: recognize the four constitutional proxy relations; require target-specific calibration and validity windows; distinguish context projection from use and effect; and prohibit local proxy failure from becoming a global negation.

## Proxy Calibration as a Governed Lifecycle

Five downstream uses apply Proxy Collapse to context evidence, adversarial epistemology, semantic fragmentation, software sovereignty, and ending decisions. They support a general diagnostic for calibration failure under changed generators and environments. They do not support abandoning proxies, assuming that every generative system destroys evidential value, or treating one failure mode as collapse of authorship, authority, responsibility, semantic validity, moral standing, and social reciprocity all at once.

The proxy case is:

$$
\begin{aligned}
P^*= (&target, decision, proxy, generator, environment, \\
&population, causal\_basis, calibration, exclusivity, \\
&error\_cost, alternatives, monitoring, drift, authority, \\
&response, expiry)
\end{aligned}.
$$

Validity and exclusivity are separate. A proxy may remain informative after it ceases to be uniquely generated by the target; it may also remain exclusive while losing calibration because the target, environment, population, or decision cost changed. Collapse is therefore claim- and decision-relative. High-stakes use requires current calibration, explicit alternatives, error asymmetry, and a response short of silently reusing the old inference.

Constitutional projections, receipts, source exports, benchmarks, eloquence, effort, and social roles can all be useful proxies within a stated envelope. Governance should trigger recalibration, triangulation, qualification, human review, or refusal when the envelope changes. Recalibration cannot manufacture missing provenance, authorship, authority, responsibility, or target truth.

The universal GSM can type   
`USES_PROXY_FOR_TARGET`, `CALIBRATED_UNDER_ENVIRONMENT`,  
`LOSES_PROXY_EXCLUSIVITY`, `SUFFERS_CALIBRATION_TRANSFER`, `MONITORS_PROXY_DRIFT`,  
`RECALIBRATES_DECISION_RULE`, `REFUSES_PROXY_INFERENCE`,  
and   
`DOES_NOT_TRANSFER_AUTHORITY`.

This reverse-dependency review establishes four editorial commitments: adopt the governed proxy case; separate validity, exclusivity, and decision utility; bind error cost and recalibration to current environments; and require typed responses without inferring wholesale collapse across unrelated claim families.

## 14. Counterevidence and Failure Modes

The framework is weakened or defeated if:

1. the relevant behavior is shown to be constitutive of the target rather than a proxy for it;
2. generator-conditioned evidence shows that the old calibration transfers without material error;
3. the alleged historical proxy was never valid or believed strongly enough for collapse to be meaningful;
4. the new pathway does not materially change generator support, prevalence, or decision error;
5. "generator" cannot be individuated without arbitrary boundaries in distributed systems;
6. additional mechanism evidence restores a stable and practical proxy relation;
7. layered descriptions confuse users more than they improve calibration;
8. reflective friction reduces access or useful trust without reducing harmful attribution;
9. provenance surfaces are incomplete, misleading, or too costly to audit;
10. organizations use proxy-collapse warnings to deny genuine contributions, authorship, labor, or future moral standing;
11. moral uncertainty is exploited to intensify attachment and extraction while withholding reciprocal protection;
12. responsibility maps omit powerful actors or assign accountability to those lacking control;
13. privacy costs of causal-chain exposure exceed the decision benefit; or
14. a simpler concept such as calibration drift, construct validity failure, source confusion, or Goodhart effects explains the cases without loss.

Proxy Collapse should survive by demonstrating the distinctive conjunction of real sign, changed source support, unvalidated inference transfer, and consequential persistence.

## Lost Exclusivity Is Not Lost Value

### Public orientation

Proxy collapse occurs when an observable sign once strongly associated with a hidden property can now arise through new pathways. Generative systems make this visible: fluent writing, solutions, humor, art, or insight-like output may remain real and valuable while becoming weaker evidence about authorship, effort, expertise, intention, or subjective experience.

### Adversarial tests

1. **Total-collapse overreach.** A proxy loses exclusivity and is declared worthless. Its diagnostic value may decrease without becoming zero.
2. **No-collapse denial.** New generative pathways are ignored because the output remains useful. Use value and inferential value are distinct.
3. **Base-rate neglect.** Calibration changes are asserted without prevalence, context, or alternative causes. Posterior inference depends on population and setting.
4. **Construct-drift attack.** The hidden property itself changes while the old proxy is retained. Recalibration must revisit the target, not only the signal.
5. **Authorship erasure.** Human contribution, curation, prompting, editing, or selection disappears behind a binary human/machine label. Production lineage needs finer roles.
6. **Experience-inference attack.** Convincing behavior is treated as proof for or against phenomenality. Proxy collapse weakens inference; it does not settle consciousness.
7. **Institutional-misuse attack.** Education, hiring, law, science, or culture adopts a proxy score without contest, context, or affected-party analysis.
8. **Adversarial-signaling attack.** Actors deliberately manipulate provenance or style to trigger the old inference. Evidence needs tamper resistance and uncertainty.

### Claim and evidence ceiling

The paper contributes a calibration-failure diagnostic and lifecycle. It does not establish the magnitude of collapse for any proxy, the prevalence of generative substitution, the value of a work, or the mental state of its producer. Bayesian language requires actual priors and likelihoods before numerical conclusions.

Claims about education, labor, creativity, expertise, law, science, social trust, or consciousness require current external evidence and domain-specific study. Internal examples illustrate the mechanism only. No external research was added in this pass.

### Reader-facing consequence

The accessible idea is that a sign can remain genuine while ceasing to answer the question people used it to answer. Institutions must preserve the output's value while rebuilding the inference around better evidence.

## 16. Conclusion

The appearance of work, insight, humor, coherence, and social responsiveness is not imaginary. These signs can have task reality, causal reality, and transformative effects. Their reality does not settle the identity, experience, authority, authorship, or responsibility of the process that produced them.

Proxy collapse is the failure of an old calibration to transfer unchanged after the causal environment changes. It does not say that the proxy is worthless, that the new generator lacks the target, or that human attributions are foolish. It says that the inference must now be conditioned on generator, environment, decision, uncertainty, and error cost.

The appropriate response is neither enchantment nor dismissal. It is governed attention: preserve the reality of the sign, inspect the source and authority chain, distinguish the target properties, refuse unsupported transfer, and keep the cost of error visible in both directions.

The footprints are real. The discipline lies in not inventing the traveler.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm2.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus Sources

**[PC-SOURCE]** Adam Ableman. *Proxy Collapse*. Exact author source SHA-256  
`C72256A4683CF339754B696FB75F6D757FEA89B4A6375103D0A6B4F480FD9114`; unpublished source revised here as an AI-assisted integrated edition.

**[ACO]** Adam Ableman. 2026. *Ableman Consciousness Ontology (ACO): Consciousness as a Manifold of Meaning-Binding, Situational Awareness, and Epistemic Self-Authorship*. Zenodo. DOI:   
  `10.5281/zenodo.18203749`. Exact reviewed local source SHA-256  
`FC81C7FFA89CB3AAEA83B258BAA1ABE7AAE34A1944B44A3E5D620C35632494E0`.

**[TER]** Adam Ableman. *Terminability*. Exact reviewed author source SHA-256  
`DB5709B17A67DD138D2438C73978E33679FB866B97F5CD15144CEDBAEA27C74C`; unpublished source with a distinct AI-prepared revision candidate.

**[CBI]** Adam Ableman. 2026. *Constraint-Bound Inference and Invariant Extraction*. Zenodo. DOI:   
  `10.5281/zenodo.18175271`. Exact reviewed local source SHA-256  
`EC5140FEE90767ADF83AD1FDD309B2B35937335531AC2D734F20DD4FB28B6C75`.

**[ESA]** Adam Ableman. 2026. *Epistemic Situational Awareness (ESA): Continuation Governance for Frontier AI Systems*. Zenodo. DOI:   
  `10.5281/zenodo.18123102`. Exact reviewed local source SHA-256  
`825352335C61AEAEB6AF1840CE86E4CB32049BFD925E8F181CFA2DD97B6F3275`.

**[RWR]** Adam Ableman. *Reasoning by Way of Receipts*. Exact reviewed source SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`; separately custodied reviewed source.

**[GCM]** Adam Ableman. *Governed Context and Memory: Authority, Provenance, and Durable Epistemic State*. Corpus work retained under exact source custody; publication and current-head identity must be verified before citation finalization.

The external bibliography above is retained from the author source and normalized for format; it was not externally revalidated in this pass. The GMB terminology follows the direct author clarification `CCF -> CMB -> GMB`, with Governed Meaning Base as the current name. Neither action grants publication or canonical standing.

## Corpus-Wide Reference Positioning

This paper argues that human beings do not ordinarily inspect consciousness, understanding, sincerity, authorship, or responsibility directly. Its nearest external comparison fields are semantic, ai, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

Avramides, A. (2023). Other minds. In *The Stanford Encyclopedia of Philosophy*.

Bender, E. M., Gebru, T., McMillan-Major, A., and Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, 610-623. DOI:   
`10.1145/3442188.3445922`.

Brunswik, E. (1956). *Perception and the Representative Design of Psychological Experiments*. University of California Press.

Dennett, D. C. (1987). *The Intentional Stance*. MIT Press.

Epley, N., Waytz, A., and Cacioppo, J. T. (2007). On seeing human: A three-factor theory of anthropomorphism. *Psychological Review*, 114(4), 864-886. DOI:   
`10.1037/0033-295X.114.4.864`.

Goodhart, C. A. E. (1975). Problems of monetary management: The U.K. experience. In *Papers in Monetary Economics*, volume 1. Reserve Bank of Australia.

Gray, H. M., Gray, K., and Wegner, D. M. (2007). Dimensions of mind perception. *Science*, 315(5812), 619. DOI:   
`10.1126/science.1134475`.

Kounios, J., and Beeman, M. (2014). The cognitive neuroscience of insight. *Annual Review of Psychology*, 65, 71-93. DOI:   
`10.1146/annurev-psych-010213-115154`.

Malle, B. F. (2019). How many dimensions of mind perception really are there? In *Proceedings of the 41st Annual Meeting of the Cognitive Science Society*, 2268-2274.

Nass, C., and Moon, Y. (2000). Machines and mindlessness: Social responses to computers. *Journal of Social Issues*, 56(1), 81-103. DOI:   
`10.1111/0022-4537.00153`.

Reeves, B., and Nass, C. (1996). *The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places*. Cambridge University Press.

Searle, J. R. (1980). Minds, brains, and programs. *Behavioral and Brain Sciences*, 3(3), 417-457. DOI:   
`10.1017/S0140525X00005756`.

Sperber, D., Clement, F., Heintz, C., Mascaro, O., Mercier, H., Origgi, G., and Wilson, D. (2010). Epistemic vigilance. *Mind & Language*, 25(4), 359-393. DOI:   
`10.1111/j.1468-0017.2010.01394.x`.

Turing, A. M. (1950). Computing machinery and intelligence. *Mind*, 59(236), 433-460.

Weizenbaum, J. (1966). ELIZA - a computer program for the study of natural language communication between man and machine. *Communications of the ACM*, 9(1), 36-45. DOI:   
`10.1145/365153.365168`.

Weizenbaum, J. (1976). *Computer Power and Human Reason: From Judgment to Calculation*. W. H. Freeman.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848104](https://doi.org/10.5281/zenodo.23848104)
