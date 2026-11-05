# The Path Was Open

## Declared Boundaries, Reachable Effects, and Human Accountability in Agentic Systems

### A machine may choose a route. The conditions of passage still require an account.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Machine action selection creates neither an automatic responsibility vacuum nor automatic human liability. This paper develops a boundary-accountability framework that separates selection autonomy from authority over effects; declared admissibility from operational reachability; and causal contribution, answerability, fault, and legal liability.

The technical core is the **declared-effective boundary gap**: modeled execution histories reachable under a configuration and threat model but excluded by the deployment's declared scope. A nonempty gap is evidence of a technical mismatch within the model. It does not establish probability, notice, duty, fault, intent, causation, or liability. An empty gap is equally bounded: it can enforce an illegitimate policy, omit real effect paths, or depend on unsound abstraction.

A conditional mediation proposition shows that prohibited modeled effects are excluded if every relevant effect passes through an accurate, non-bypassable gate whose allowed transitions preserve the declared safety property. The proposition is a specification theorem, not evidence that a deployment satisfies its premises. Real use requires exact configurations, concretization between abstract and physical effects, current authority, effect observation, bypass testing, custody, and independent verification.

The source reports an exhaustive 625-string finite illustration and says that a companion checker is supplied. No such program or result file was found in the authorized corpus. An independent AI reconstruction from the prose reproduced the reported counts, but that is conditional arithmetic validation rather than custody of the claimed author evidence. The source's 2026 incident and legal claims also remain author-supplied pending separately authorized primary-source verification.

This revision integrates the accountability framework with Authority Laundering Theory, constitutional enforcement, receipts, observability, work custody, Warrant by Structure, the universal GSM, and the realization funnel. It grants no factual, legal, safety, implementation, or publication standing.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/the-path-`

`was-open/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`6F25113712C10321E25088E378013961C5F90F97D383DB0082FA9370E0E5DBB1`. The exact source remains unchanged.

The title, boundary-gap formalism, proposition, investigative method, incident applications, finite illustration, legal analysis, research agenda, and rhetoric are author material. The evidentiary downgrades, formal repairs, integration surfaces, countertests, and editorial alternatives are AI-assisted contributions explicitly distinguished from the original author material.

This paper is not legal advice. It does not adjudicate any incident, actor, organization, claim, statute, case, duty, mental state, causation question, or liability theory. The primary-source legal and factual review required for an evidence-qualified revision was not authorized in this program and was not performed.

## 1. What the Framework Does and Does Not Decide

**Selection autonomy** asks who or what selected an action. **Effect authority** asks which effect could be performed, against what resource, under whose warrant, through which mediator, and within what jurisdiction. A highly adaptive system can operate inside a narrow effect envelope; a simple script can hold broad ambient privilege.

The framework organizes four further inquiries without merging them:

- **causal contribution:** participation in producing an outcome;
- **answerability:** obligation to supply an account of relevant decisions and controls;
- **fault:** failure under an applicable normative standard; and
- **legal liability:** satisfaction of every element and defense of a particular legal theory.

Technical reachability can inform all four, but determines none by itself. Similarly, deployment intent is not automatically intent regarding every downstream effect.

## 2. Declared Scope and Reachable Effects

Let $\Sigma$ be an alphabet of abstract effect events and $\Sigma^*$ its finite histories. Let $\mathcal{A}\subseteq\Sigma^*$ be the declared admissible safety property, assumed prefix-closed for this bounded analysis. Let $C$ be a versioned configuration, $T$ a threat and environment model, and $\Pi_T$ the proposal and environment behaviors included in the analysis.

$$
\mathcal{R}(C,T)=
\bigcup_{\pi\in\Pi_T}\operatorname{Traces}(C,\pi,T).
$$

The declared-effective boundary gap is:

$$
\Delta(C,T)=\mathcal{R}(C,T)\setminus\mathcal{A}.
$$

A witness $\tau\in\Delta(C,T)$ establishes only that the abstract model admits a declared-prohibited history. Reachability is not probability:

$$
\begin{aligned}
&\Delta(C,T) \\
&\neq \varnothing \not \\
&\Rightarrow \Pr_\mu(\Delta(C,T))\text{ is large}
\end{aligned}.
$$

Nor does failed search establish closure. Practical analysis should distinguish observed lower bounds, modeled reachability, and sound overapproximations:

$$
\underline{\mathcal{R}}\subseteq\mathcal{R}\subseteq\overline{\mathcal{R}}.
$$

The correct result may be **unresolved** when neither a witness nor a sound exclusion proof exists.

## 3. From Abstract Histories to Real Effects

An abstract trace matters only if it is related soundly to concrete execution. Let $\alpha$ map a concrete history $\rho$ to its abstract effect history. A safety argument needs a declared relationship such as:

$$
\rho\in\mathcal{R}_{\mathrm{concrete}}(C,T)
\Longrightarrow
\alpha(\rho)\in\overline{\mathcal{R}}(C,T).
$$

The mapping must preserve the effects relevant to the policy. If "call approved service" abstracts away that the service can access a prohibited third-party resource, an empty abstract gap does not establish containment. Interface admission and effect admission are distinct.

The abstraction must also say whether refusal, termination, delayed effects, retries, asynchronous jobs, credential use, human intervention, and downstream services are events. Omitting them can make the proof true only of the wrong system.

## 4. Conditional Mediation and Its Proof Burden

Let $\Gamma(h,e)$ decide whether proposed effect $e$ may extend history $h$. The source's proposition can be retained as a conditional specification theorem:

If the empty history is admissible; refusals and termination preserve admissibility; every relevant concrete effect is accurately represented and mediated before execution; the policy and authority are current; the mediator and evidence path cannot be bypassed or modified; and

$$
\Gamma(h,e)=\mathrm{ALLOW}\Longrightarrow he\in\mathcal{A},
$$

then every modeled reachable history remains in $\mathcal{A}$.

The induction is elementary because the premises carry the hard work. A proof for a real system needs evidence for:

1. effect completeness and correct resource identity;
2. non-bypassability, including administrators, intermediaries, plugins, retries, and supply chain;
3. policy and warrant integrity at effect time;
4. effect atomicity and recovery after partial failure;
5. sound abstraction and version binding;
6. independent checks against producer/verifier co-drift; and
7. continuous or change-triggered requalification.

The theorem therefore explains what complete mediation would buy. It cannot certify complete mediation from architecture prose.

## 5. Authority and Legitimacy

$\mathcal{A}$ does not authorize itself. A declared scope can be faithfully enforced while violating a resource owner's authority, law, consent, contract, or institutional constraint.

Authority Laundering Theory supplies the missing separation: explicit, receipted machinery cannot turn a defective root into legitimate authority. Every admissibility claim should bind the warrant source, jurisdiction, resource owner, time, delegated scope, revocation status, and contested alternatives.

This yields two independent questions:

1. Did the system enforce the declared boundary?
2. Was the declared boundary itself properly warranted?

An empty technical gap supports only the first, and only under its model and evidence.

## 6. Accountability Reconstruction

The paper's five inquiries form a useful evidence schema:

- **Inquiry:** Declared boundary  
  **Required question:** What was allowed, prohibited, unresolved, and by whom?  
  **Evidence boundary:** policy plus warrant provenance

- **Inquiry:** Effective boundary  
  **Required question:** Which effects were reachable at the relevant version and time?  
  **Evidence boundary:** configuration, traces, models, attacks

- **Inquiry:** Control and authority  
  **Required question:** Who could establish, change, test, waive, stop, or restart?  
  **Evidence boundary:** formal role plus practical capability

- **Inquiry:** Knowledge and notice  
  **Required question:** Which actor received what information, when, with what uncertainty?  
  **Evidence boundary:** actor-specific delivery and acknowledgment

- **Inquiry:** Preventive alternatives  
  **Required question:** Which feasible intervention blocks which class of histories?  
  **Evidence boundary:** counterfactual tests and legitimate-task cost

Every material claim should carry source, custody, time, configuration, support status, contrary evidence, and claim ceiling. Organizational knowledge must not be imputed automatically to one person; lack of an adequate notice path may itself be an independently examinable design decision.

Control ownership should also resist a nearest-person shortcut. A human approver without the decisive facts or authority may be a moral crumple zone. A remote provider should not absorb blame for a documented local decision merely because it built a component. The evidence must identify the action, capacity, notice, and applicable standard for each actor.

## 7. Counterfactual Prevention

For a harmful history $\tau$ and proposed precaution $j$:

$$
\tau\notin\mathcal{R}(C^{(j)},T)
$$

shows only that the modeled precaution interrupts that history. A meaningful prevention claim must cover an equivalence class of harmful effects, preserve legitimate task requirements, and show that the precaution was available, within the actor's control, and reasonable under the applicable standard at the relevant time.

Counterfactual interruption is evidence, not verdict. Multiple sufficient causes, alternative routes, third-party acts, uncertainty, and legal causation remain separate.

## 8. Status of the Finite Illustration

The source defines five proposal symbols, length-four strings, three mediation configurations, an absorbing stop, and local success after read then submit. It reports:

- **Configuration:** declared prohibition only  
  **Strings:** 625  
  **Prohibited effect:** 406  
  **Local completion:** 82

- **Configuration:** direct-route mediation  
  **Strings:** 625  
  **Prohibited effect:** 272  
  **Local completion:** 82

- **Configuration:** both modeled routes mediated  
  **Strings:** 625  
  **Prohibited effect:** 0  
  **Local completion:** 82

No claimed companion file   
`The_Path_Was_Open_Model_Check.py` or recorded output was found in the authorized corpus. A temporary AI reconstruction using the prose semantics reproduced all six counts. This supports arithmetic consistency under the inferred model, not exact custody of the author program or validation of a real system.

The equal completion count is construction-dependent because external actions neither help nor hinder the local task. The zero is similarly conditional on enumerating only two external routes and stipulating that both are blocked. The illustration demonstrates a logical possibility: effect mediation can eliminate modeled prohibited outcomes without reducing success in a task constructed so the prohibited effects are unnecessary.

Before this can be treated as reproducible evidence in a future edition, the exact author program, hash, output, transition semantics, and independent replay should be supplied.

## 9. Legal and Incident Claims: Verification Hold

The source discusses 2026 reports attributed to Hugging Face, OpenAI, and Anthropic; federal statutes; California law; Department of Justice guidance; and reported decisions including *Amazon.com Services v. Perplexity AI*. It also cites scholarship on responsibility gaps, delegation, meaningful human control, and moral crumple zones.

These materials were not externally checked in this program. They must not be presented as verified merely because the source gives dates, quotations, holdings, or citations. For a future evidence-qualified revision, an authorized legal/factual pass must retrieve the primary texts, verify existence and dates, confirm quotations and procedural posture, update subsequent history, validate statutory versions, and separate holding, dicta, party allegation, agency guidance, and author inference.

Even after verification, architectural evidence must be mapped element by element. Negligence is not intent; access is not damage; organizational attribution is not automatic personal liability; and causing an act through an intermediary has its own requirements. The framework supplies evidence organization, not a liability engine.

## 10. Corpus Integration

The adjacent corpus machinery has distinct roles:

- **The Mechanics of Constitutional Enforcement** asks how declared constraints become non-bypassable effect mediation.
- **Authority Laundering Theory** prevents structural enforcement from legitimizing defective authority roots.
- **Reasoning by Way of Receipts** binds proposals, decisions, effects, evidence, and revision without making receipt existence sufficient proof.
- **The Constitutional Observability Platform** exposes claims, configurations, warnings, effects, and standing to actors who can use them.
- **A Formal Theory of Work Custody** preserves who holds work and how authority and lineage move.
- **Warrant by Structure** grades authorization, gate participation, effect evidence, and closure rather than collapsing them.

The **Governed Meaning Base (GMB)** is the current name in the `CCF -> CMB -> GMB` lineage. It can preserve declarations, warrants, configurations, traces, reports, evidence, disputes, and legal-source bindings with their standing. Inclusion does not adjudicate them. The universal GSM keeps selection, authority, effect, actor, notice, control, evidence, claim, and legal element distinct.

## 11. Realization Funnel

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

- **Possibility:** enumerate agent architectures, effect paths, mediators, authority roots, accountability theories, and evidence designs.
- **Specification:** define scope, threat model, effects, abstraction, mediation, warrants, receipts, notice, and claim boundaries.
- **Configuration Manifold 1 (CM1):** retain configurations meeting mandatory authority, containment, evidence, recovery, privacy, and due-process constraints.
- **Configuration Manifold 2 (CM2):** prefer among admissible configurations by capability, usability, resilience, inspectability, sovereignty, cost, and human accountability.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for one deployment and jurisdiction. The names are interchangeable.
- **IR:** construct an **Instance Realization** or **Implementation Realization** of that configuration. The names are interchangeable.
- **Evidence:** retain exact configurations, model checks, attacks, receipts, effects, warnings, actor-specific notice, and primary sources.
- **Revision:** change the system or claims after new evidence while preserving prior lineage and standing.

The paper reaches Specification and offers an abstract demonstration. It does not establish an IC, IR, real containment result, legal application, or implementation authority.

## Boundary-Accountability Diagnostic

Across the completed P1 corpus, The Path Was Open is the **boundary-accountability diagnostic for comparing declared scope, modeled reachability, concrete effect routes, authority, notice, control, and feasible prevention**. It organizes evidence relevant to responsibility without turning a technical witness into legal liability, moral fault, or automatic exculpation.

- **Adjacent work:** *The Mechanics of Constitutional Enforcement*  
  **Supplies:** Complete mediation, effect gates, classified remainder, and atomic evidence obligations.  
  **Path-paper boundary:** This paper tests whether the claimed boundary actually covered modeled and concrete routes.

- **Adjacent work:** *Authority Laundering Theory*  
  **Supplies:** Separation of structural enforcement from legitimacy of the warrant root.  
  **Path-paper boundary:** An empty boundary gap cannot legitimize the declared policy.

- **Adjacent work:** *The Constitutional Observability Platform*  
  **Supplies:** Delivery of warnings, state, claims, evidence, and standing to relevant actors.  
  **Path-paper boundary:** Availability in a dashboard is not actor-specific notice or practical control.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Time-indexed responsibility for live work and transitions.  
  **Path-paper boundary:** Custody informs control and answerability without deciding fault.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Reconstruction of proposal, gate, effect, evidence, and revision.  
  **Path-paper boundary:** Receipt existence is one evidentiary object, not proof that the effect was completely mediated.

The diagnostic should produce a typed case record:

$$
\begin{aligned}
B= (&declaration, warrant, configuration, threat\_model, \\
&abstract\_effects, concretization, reachable\_effects, \\
&gap, actors, control, notice, alternatives, evidence, \\
&unknowns, claim\_ceiling)
\end{aligned}.
$$

Its output is not `RESPONSIBLE` or `NOT RESPONSIBLE`. It is a set of bounded findings such as   
`DECLARED_EFFECTIVE_MISMATCH`,  
`UNMODELED_ROUTE`, `BYPASS_WITNESS`, `UNSOUND_CONCRETIZATION`, `DEFECTIVE_WARRANT`,  
`NOTICE_NOT_DELIVERED`, `CONTROL_NOT_ESTABLISHED`, `PRECAUTION_INTERRUPTS_MODELED_CLASS`,  
or `UNRESOLVED`. Each finding states the model and evidence under which it holds.

The paper also links agent containment to institutional accountability. A system can choose among paths only because other actors selected credentials, effect mediators, policies, interfaces, monitoring, escalation, and shutdown powers. That observation does not make every designer liable. It makes those surrounding choices discoverable objects for actor-specific inquiry.

The universal GSM can type   
`DECLARES_EFFECT_BOUNDARY`, `REACHES_MODELED_EFFECT`,  
`MAPS_CONCRETE_TO_ABSTRACT_EFFECT`, `WITNESSES_BOUNDARY_GAP`, `OMITS_EFFECT_ROUTE`,  
`HOLDS_PRACTICAL_CONTROL`, `RECEIVES_ACTOR_SPECIFIC_NOTICE`, `CAN_APPLY_PRECAUTION`,  
`INTERRUPTS_HARMFUL_HISTORY_CLASS`, `REMAINS_LEGALLY_UNADJUDICATED`,  
and   
`BOUNDS_ACCOUNTABILITY_CLAIM`. These relations preserve the diagnostic's usefulness without making it a liability engine.

This integration establishes four editorial commitments: classify the paper as the boundary-accountability diagnostic; adopt the typed case-record envelope and bounded finding vocabulary; require actor-specific control, notice, and feasible-alternative evidence; and retain legal liability, moral fault, causal contribution, and technical boundary findings as distinct conclusions.

## Commitment, Resolution, Notice, and Equivalence in Boundary Accountability

The fixed-seed comparison with CHC, Constitutional Binding Theory, The Locus of Shared Experience, and Semantic Gravitational Attractors gives the boundary diagnostic a more precise semantic and interpersonal evidence path:

$$
\begin{aligned}
B^*= (&declaration, warrant, commitments, binding\_profile, \\
&configuration, threat\_model, abstract\_effects, \\
&concretization, reachable\_effects, gap, actors, control, \\
&notice\_route, recognition, equivalence\_regime, \\
&alternatives, evidence, unknowns, claim\_ceiling)
\end{aligned}.
$$

CHC can commit to the declared boundary, model, policy, evidence, and decision epoch. Those commitments establish exact objects for audit; they do not prove that the boundary covered every concrete effect route. Constitutional Binding Theory makes concretization an anchor-resolution problem whose candidates, exclusions, law, target, and remainder must be visible.

The Locus of Shared Experience sharpens actor-specific notice. Sending a message, rendering a warning, semantic uptake, recognition, consent, practical control, and shared understanding are different relations. A technical record should preserve route, accessibility, permission, correction, refusal, and remaining difference without claiming access to an actor's experience.

Semantic Gravitational Attractors adds an adversarial case: canonicalizing several effects, actors, warnings, or incidents under one equivalence regime can improve analysis or erase a material accountability distinction. False merges and silent remainder loss can conceal who knew what, which route remained open, or which precaution could interrupt it.

The universal GSM can type   
`COMMITS_TO_BOUNDARY_DECLARATION`,  
`RESOLVES_CONCRETE_EFFECT_CLASS`, `DELIVERS_ACTOR_SPECIFIC_NOTICE`,  
`DOES_NOT_INFER_RECOGNITION`, `CANONICALIZES_UNDER_ACCOUNTABILITY_REGIME`,  
`PRESERVES_ACTOR_DIFFERENCE`, and   
`WITNESSES_REMAINDER_LOSS`.

This randomized review establishes four editorial commitments: extend the case record with commitment and binding profiles; distinguish notice delivery from recognition, consent, and control; audit accountability equivalence regimes for false merge and remainder loss; and retain legal, moral, and experiential conclusions outside the technical diagnostic.

## A Boundary-Accountability Case Docket

Four downstream uses refine *The Path Was Open* into a reusable case docket. CHC shows that exact commitments and passing receipts do not exclude unmodeled effect routes. Constitutional Binding Theory treats concrete-to-abstract effect mapping as governed resolution with candidates, exclusions, and remainder. Semantic Gravitational Attractors shows that canonicalization can false-merge effects, actors, notices, or feasible precautions. *The Locus of Shared Experience* separates delivered notice from recognition, understanding, consent, practical control, and shared experience.

The resulting docket is:

$$
\begin{aligned}
B^*= (&declaration, warrant, commitments, binding\_profile, \\
&configuration, threat\_model, abstract\_effects, \\
&concrete\_routes, equivalence\_regime, gaps, actors, \\
&authority, control, notice, recognition, consent, \\
&alternatives, interruptions, remedies, evidence, \\
&unknowns, claim\_ceiling)
\end{aligned}.
$$

Boundary review should preserve both missing-route and wrong-abstraction failures. A concrete path may be absent from the model, or several materially different paths may be collapsed into one class. Each actor requires separately supported authority, control, notice, feasible response, and remedy fields. Organizational delivery cannot be imputed to an individual, and technical reachability cannot be converted into knowledge, consent, fault, liability, or exculpation.

Counterfactual prevention should enumerate interventions, prerequisites, costs, side effects, actor control, and residual routes. "The path was open" is a bounded technical finding only when the route and intervention are evidenced under an exact configuration and time. It remains compatible with `UNKNOWN`,  
`PARTIAL_CONTROL`, `NOTICE_UNPROVEN`, `ALTERNATIVE_INFEASIBLE`,  
and   
`EQUIVALENT_ROUTE_REMAINS`.

The universal GSM can type   
`COMMITS_TO_BOUNDARY_MODEL`, `RESOLVES_CONCRETE_EFFECT_ROUTE`,  
`FALSE_MERGES_ACCOUNTABILITY_CASE`, `DELIVERS_NOTICE_WITHOUT_RECOGNITION`,  
`CONTROLS_FEASIBLE_INTERRUPTION`, `LEAVES_EQUIVALENT_ROUTE_OPEN`,  
and   
`WITHHOLDS_LIABILITY_CONCLUSION`.

This reverse-dependency review establishes four editorial commitments: adopt the full case docket; test both omitted routes and false abstraction; require actor-specific notice, control, and feasible-alternative evidence; and retain legal, moral, experiential, and technical conclusions as distinct.

## Diagnostic Accountability Without a Liability Verdict

### Public orientation

When an autonomous system causes harm, neither "the machine chose" nor "a person deployed it" settles responsibility. This paper provides a boundary-accountability diagnostic: reconstruct reachable effects, authority, mediation, evidence, notice, control, and counterfactual prevention. It does not decide legal liability, guilt, intent, causation, or remedy.

### Adversarial tests

1. **Legal-category substitution.** Architectural terms are treated as elements of a legal claim. Any legal mapping requires jurisdiction, current authority, facts, procedure, and qualified review.
2. **Reachability-as-causation attack.** An effect was technically reachable, so the subject is said to have caused it. Reachability, actual traversal, causal contribution, and legal causation are distinct.
3. **Authority-as-responsibility attack.** A party had some authority, so all downstream outcomes are attributed to it. Scope, knowledge, control, delegation, intervention opportunity, and competing causes matter.
4. **Receipt-as-notice attack.** A warning or receipt existed, so a person is presumed to have understood it. Delivery, accessibility, comprehension, timing, and ability to act require evidence.
5. **Containment-theater attack.** A declared boundary omits a reachable path. The diagnostic must compare modeled and concrete effect graphs and preserve the boundary gap.
6. **Counterfactual fantasy attack.** A hypothetical safeguard is claimed to have prevented harm without a supported mechanism or feasible deployment. Counterfactuals require explicit intervention and assumptions.
7. **Hindsight attack.** Post-incident knowledge is projected backward into foreseeability. Evidence must be time-indexed and actor-indexed.
8. **Machine-agency laundering.** System autonomy is used either to erase human decisions or to anthropomorphize the system into a legal person. The framework preserves role-specific action without deciding personhood.

### Evidence and citation gate

The finite illustration demonstrates the diagnostic schema, not a real incident finding. Any concrete legal, historical, security, or incident claim remains on verification hold until exact sources, jurisdiction, dates, system versions, evidence custody, disputed facts, and qualified analysis are supplied.

Internal corpus sources explain the technical model of authority, receipts, mediation, and effect paths. They cannot establish law or facts outside the corpus. No external research was added in this pass.

### Reader-facing consequence

The paper's public contribution is a better question set for accountability: what paths were open, who could close them, what evidence existed at the time, which protections actually mediated the effect, and what feasible intervention would have changed the outcome?

## 12. Counterevidence and Failure Modes

The framework must narrow or fail where: (1) declared scope is illegitimate; (2) an effect path is omitted; (3) abstraction erases the prohibited downstream effect; (4) a mediator is bypassable; (5) an intermediary holds undeclared authority; (6) policy changes between proposal and effect; (7) resource identity is wrong; (8) receipt and effect are not atomic; (9) recovery duplicates or loses effects; (10) verifier and producer co-drift; (11) environment behavior lies outside $T$; (12) the overapproximation is unsound; (13) model-check paths are spurious; (14) no witness is mistaken for safety; (15) reachable is mistaken for probable; (16) organizational notice is imputed to an actor without evidence; (17) formal control differs from practical control; (18) a nearby human becomes a crumple zone; (19) one interrupted sequence leaves equivalent harmful routes; (20) a precaution was unavailable or destroys the legitimate task; (21) the original checker remains missing; (22) AI-reconstructed counts differ under alternative plausible semantics; (23) incident sources do not support the stated facts; (24) legal sources do not support the stated propositions; (25) later authority changes the law; (26) architectural evidence is treated as a legal element; (27) privacy or due-process costs are omitted; or (28) the method yields no more accurate or uncertainty-preserving reconstruction than simpler incident analysis.

## 14. Conclusion

The decisive distinction is not whether a machine chose an action. It is whether the effect path, authority, evidence, and human control surrounding that choice can be reconstructed without converting technical facts into automatic blame or exculpation.

The declared-effective boundary gap is a useful technical object. Complete mediation is a useful conditional theorem. Neither supplies its own real-world premises, legitimate authority, actor knowledge, or legal conclusion. Those require exact artifacts, bounded models, observable effects, custody, primary sources, and separately justified inference.

The path may have been open. The framework's discipline is to show which path, under which configuration, according to which evidence, and what that evidence does not yet permit us to say.

## Author-Supplied Reference Note

The source manuscript contains scholarship, incident reports, statutes, guidance, cases, and an unpublished motivating dialogue. All remain author-supplied references pending an explicitly authorized primary-source verification pass. Their exact text and citations are preserved in the source under the custody hash above.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Instance Configuration.** The present paper does not claim a complete instance configuration treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that machine action selection creates neither an automatic responsibility vacuum nor automatic human liability. Its nearest external comparison fields are security, ai, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E2]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E3]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

**[E4]** Robert N. M. Watson, Simon W. Moore, Peter Sewell, and Peter G. Neumann. *An Introduction to CHERI*. University of Cambridge Technical Report UCAM-CL-TR-941, 2019. DOI: 10.48456/tr-941. [cl.cam.ac.uk source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-941.html) **Relationship:** Adjacent capability architecture demonstrating unforgeable hardware authority and compartmentalization.

**[E5]** Patrick Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **Relationship:** Predecessor retrieval architecture; comparison centers on provenance, admission, and fail-closed constraints not supplied by retrieval alone.

**[E6]** Shunyu Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. arXiv:2210.03629. https://arxiv.org/abs/2210.03629 **Relationship:** Predecessor agent pattern for interleaving reasoning and action; used to distinguish action traces from governed effects.

**[E7]** Elham Tabassi. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1, 2023. DOI: 10.6028/NIST.AI.100-1. https://doi.org/10.6028/NIST.AI.100-1 **Relationship:** Adjacent risk-management framework used to test whether the paper operationalizes governance beyond voluntary process guidance.

### Ableman corpus

**[A1]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *The Integrity Enforcement Layer*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-505307E9E6571B63`;  
source SHA-256  
`F858AB32E0937B796353CAE573DD4183FDF4F179A3E1E7E40C4E0C6BF1AB0018`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Constitutional Syscalls*. Ableman Corpus current edition; work identity `PAPER.PUB.18737229`;  
source SHA-256  
`5F14356180812262778F8574C292F4F6B560993042E5358B02EAB9CF0F7DE14C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *CARA: Constrained Artificial Reasoning Architecture*. Ableman Corpus current edition; work identity `PAPER.PUB.18099715`;  
source SHA-256  
`F8F74F0CD58F5414D9A29EBE958E49751892D07A028CB51197F8201B18AAB40E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *A Constitution for the Context Window*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-CF26BA0E123F472F`;  
source SHA-256  
`60395402368E146F115CCE53D0E5A15B8FB23C90ED5B24CA92AB8515B2009965`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

DOI: [10.5281/zenodo.23848461](https://doi.org/10.5281/zenodo.23848461)
