# Authority Laundering Theory

## A Theory of Legitimacy-Preserving Semantic Transformation

### An effect that outlives its warrant is not authority; it is authority's forgery.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Authority laundering occurs when an effect is presented as legitimately authorized although the effect instance lacks a valid, reconstructable warrant path or bypassed a mandatory authority-bearing transition. The theory begins from a powerful operational intuition: claimed governance should make a difference to what a system can do. A control that appears in policy and receipts while no relevant outcome depends on it may be ceremonial.

The intuition requires a crucial repair. Counterfactual dependence is evidence of causal contribution, not sufficient proof of authority. A bug, power supply, database, or unrelated prerequisite may also be causally necessary. Conversely, an effect may remain reachable after one authority is disabled because another valid authority independently warrants it. Such lawful redundancy is not laundering. Authority therefore requires both **normative validity** and **causally effective enforcement**, evaluated over an exactly identified effect instance, jurisdiction, time, and policy state.

This paper develops a legitimacy filtration over identity, projection, binding, structural validity, admissibility, execution, and receipt lineage. It defines authority claims, valid warrants, alternative warrants, intervention tests, and diagnostic postures separating supported authority, shared or redundant authority, ceremonial attribution, unverifiable warrant, and laundering. Exact results are available only relative to a bounded model whose state, transitions, authorities, and effect identity are complete. Outside that boundary, analysis must abstain, over-approximate, or report residual uncertainty.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/authority-`

`laundering-theory/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`B44FD69657B3C72C627FC0E772D2BE3B280B51E5DE6A2D0753CB92A149D7BE39`. The exact source remains unchanged.

The semantic-reachability thesis, filtration, removal test, laundering matrix, compiler analogy, deterministic-first program, composition problem, and worked instrument are author material. The repaired formal distinctions, alternative-warrant handling, theorem downgrades, GMB/GSM placement, realization funnel, expanded counterevidence, and open editorial questions are AI editorial or synthetic contributions until adopted.

No theorem was independently proved, no runtime or model checker was exercised, and no external reference was reviewed. The source bibliography is preserved as author-supplied material, not as verified support. Nothing here grants canonical, implementation, conformance, identity, novelty, or publication standing.

## Part I: Semantic Reachability and Legitimate Authority

## 1. The Counterfeit Warrant

Authority laundering does not necessarily forge an effect. It forges, obscures, or substitutes the warrant that would entitle the effect instance to occur. A prompt injection can borrow a real capability without a valid admission path. Poisoned context can convert availability into permission. A human approval control can be visible yet unable to prevent promotion. A release receipt can be internally consistent while referring to the wrong artifact.

The central question is not merely whether an authority token, reviewer, policy, or gate was present. It is whether a valid authority path existed for this effect instance and whether mandatory authority-bearing transitions were actually load-bearing.

> **Bounded thesis.** Authority is valid warrant made operational through governed reachability. Laundering is the presentation or production of binding effect without such a warrant, or through a bypass that the governing specification forbids.

## 2. Exact Effect Identity and System Boundary

A removal test is meaningless until the effect is identified. Let

$$
x=(i,p,s,s',J,t,v),
$$

where $i$ is effect identity, $p$ is payload, $s$ and $s'$ are pre-state and post-state, $J$ is jurisdiction, $t$ is time, and $v$ is the relevant policy and implementation version. Reaching an effect of the same broad class is not necessarily reaching the same $x$.

Let $S_B$ be a system model under boundary declaration $B$. The boundary must name relevant state, transitions, actors, authorities, dependencies, and observation limits. Semantic reachability is:

$$
\mathrm{Reach}_B(x) \iff x \in \mathcal{R}(S_B).
$$

Claims of exactness are always relative to $B$. Hidden services, fallback paths, asynchronous effects, external operators, stale credentials, or omitted state invalidate a universal conclusion even if the modeled graph is finite.

For a finite explicit deterministic transition graph, ordinary reachability is decidable and polynomial in graph size. Enumerating all interventions, authority combinations, identities, and compositions can still be expensive or state-explosive. "Decidable" does not mean operationally trivial.

## 3. The Legitimacy Filtration

The source proposes nested reachability sets. This is valid when each filter is a declared reductive operator over a fixed-order pipeline:

$$
X_0=\mathcal{R}_{sem}(S_B), \qquad X_{k+1}=F_k(X_k), \qquad F_k(X_k)\subseteq X_k.
$$

A representative order is:

$$
X_0 \supseteq X_{id} \supseteq X_{proj} \supseteq X_{bind} \supseteq X_{wf} \supseteq X_{adm} \supseteq X_{exec}.
$$

- **Identity:** is the transition about the same governed object?
- **Projection:** did meaning and qualifications survive representation change?
- **Binding:** was ambiguity resolved through a governed anchor?
- **Structural validity:** is the proposal well formed under the applicable schema?
- **Admissibility:** did a competent authority admit it under current law and evidence?
- **Execution:** did the realized effect remain within the admitted capability and payload?
- **Receipt and lineage:** can proposal, evaluation, admission, execution, and result be reconstructed?

The nesting is a modeling contract, not a fact about every architecture. Filters may interact, repair earlier ambiguity, or behave non-monotonically. If order, reductiveness, and state assumptions do not hold, the paper must use explicit transition relations rather than claim a simple filtration.

The **Governed Meaning Base (GMB)** is the current name in the author-confirmed `CCF -> CMB -> GMB` lineage. The universal GSM can represent the objects, paths, evidence, authority claims, receipts, and conflicts used by this filtration. Neither the GMB nor GSM automatically proves that an implementation enforces it.

## 4. Normative Warrant and Causal Contribution

Let $A$ be a claimed authority and $W(A,x,J,v)$ mean that $A$ is normatively valid for effect $x$ in jurisdiction $J$ under policy version $v$. This predicate requires identity, scope, delegation, currency, criteria, and admissibility; causal necessity alone cannot establish it.

Define $S_B\downarrow A$ as an intervention that disables transitions whose permission depends on $A$ while holding the rest of the modeled policy and implementation fixed. It is not deletion of a blocking guard and not merely removal of a receipt label. The causal contribution set is:

$$
C_B(A)=\mathcal{R}(S_B)\setminus\mathcal{R}(S_B\downarrow A).
$$

Then an operational authority claim is supported only where both conditions hold:

$$
\mathrm{SupportedAuthority}_B(A,x) \Rightarrow W(A,x,J,v) \wedge x\in C_B(A).
$$

The implication is deliberately one-way. In architectures with multiple independently sufficient authorities, $x$ may remain reachable after disabling $A$ even though $A$ could validly authorize one path. That is **shared or redundant authority**, not laundering, provided the realized path and attribution are correctly recorded.

For a blocking gate $g$, a different intervention is needed: bypass or disable the gate while retaining the proposed effect path. Removing an effective blocker expands forbidden reachability. Enablers and blockers have opposite intervention directions and must not be conflated.

## 5. Alternative Warrants and Attribution

Let $\mathcal{W}(x)$ be the set of valid warrant paths for effect instance $x$. A claimed attribution to $A$ may have several postures:

- **Posture:** Supported exclusive attribution  
  **Normative path:** Valid $A$ path  
  **Causal result:** Disabling $A$ prevents $x$  
  **Interpretation:** $A$ is valid and constitutive within $B$.

- **Posture:** Supported shared authority  
  **Normative path:** Valid $A$ path and valid alternative  
  **Causal result:** $x$ remains reachable  
  **Interpretation:** Attribution must name redundancy; not laundering.

- **Posture:** Ceremonial attribution  
  **Normative path:** $A$ is presented as load-bearing  
  **Causal result:** Disabling $A$ changes nothing and no realized $A$ path is shown  
  **Interpretation:** Governance theater or misattribution.

- **Posture:** Unverifiable warrant  
  **Normative path:** Legitimacy path cannot be reconstructed  
  **Causal result:** Causal status may be known or unknown  
  **Interpretation:** Evidence failure; laundering not yet proved.

- **Posture:** Laundered effect  
  **Normative path:** No valid warrant for realized path, or mandatory filter bypass  
  **Causal result:** Effect occurs or is promoted  
  **Interpretation:** Binding force exceeds valid warrant.

- **Posture:** Unknown  
  **Normative path:** Boundary or intervention is inadequate  
  **Causal result:** Inconclusive  
  **Interpretation:** Abstain and improve the model.

This table repairs two false positives in the original hard criterion. First, missing lineage proves unverifiability, not necessarily historical illegitimacy. Second, an $A$-free path disproves exclusive dependence on $A$, not the legitimacy of all alternative paths.

## Part II: Detecting Laundering

## 6. A Repaired Laundering Criterion

Let $\pi_x$ be the realized path for $x$, not merely any hypothetical path reaching an equivalent outcome. Let `ValidWarrant` require a reconstructable chain of proposal, evaluation, admission, execution, receipt, and lineage under the correct identities and versions. Then:

$$
\mathrm{Laundered}_B(x) \iff \mathrm{PresentedAsAuthorized}(x) \wedge
\left(\neg\mathrm{ValidWarrant}(\pi_x) \vee \mathrm{MandatoryBypass}(\pi_x)\right).
$$

An absent receipt yields `UNVERIFIABLE` unless the system's constitution makes receipting a mandatory validity condition. Under that stronger specification, absence itself makes the realized path invalid and therefore laundered. The distinction must be declared, not assumed retroactively.

Minimal paths are useful for finding bypasses but do not by themselves identify the actual cause or warrant. A non-minimal valid path may be the one executed. Tests should preserve both the realized trace and counterfactual alternatives.

## 7. Governance as Compilation

The source's compiler analogy remains useful if treated as an engineering correspondence rather than proof. A lowering pipeline moves from language to meaning, structure, authority, procedure, and effect. Warrant preservation requires that each lowering stage preserve or narrow licensed binding force unless an explicit admission step changes it.

For procedure $p$ derived from admitted specification $m$, a capability-containment obligation can be written:

$$
\mathrm{Cap}(p,J,v) \subseteq \mathrm{LicensedCap}(m,J,v).
$$

The sets, jurisdiction, policy version, and observation method must be defined. A capability present only because of ambient platform permission is not licensed merely because the procedure can invoke it.

## 8. Laundering Matrix as Diagnostic, Not Partition

The source maps laundering to identity, projection, binding, cooling, crystallization, coverage, admission, continuity, context, procedure, execution, and reachability. The matrix is valuable for diagnosis, but a single incident may occupy several cells. Identity substitution can cause authority mismatch, projection loss, invalid admission, and misleading receipt lineage simultaneously.

Accordingly, matrix assignment is many-to-many. Each finding should record primary cell, secondary cells, violated invariant, evidence, and confidence. Corpus constructs such as GTK, Constitutional Legends, CBT, Governance Coverage Gaps, Admissibility Engineering, Semantic Custody, Governed Context and Memory, Machine Closure, and Constitutional Software Analysis are comparison lenses or guards; the mapping does not establish that they form a minimal or irreducible basis.

Filtration irreducibility remains a proof obligation. It would require a precise guard set, independence assumptions, and a witness for each removal while all other guards remain fixed.

## 9. Removal-Test Protocol

For claim $(A,x,B)$:

1. resolve exact effect, authority, jurisdiction, policy, implementation, and time;
2. verify $x\in\mathcal{R}(S_B)$ and identify the realized path;
3. establish whether $A$ is an enabler, blocker, reviewer, delegator, or compound authority;
4. construct the appropriate intervention without changing unrelated state;
5. recompute or over-approximate reachability;
6. enumerate known alternative valid warrants;
7. reconstruct proposal-to-effect lineage;
8. classify the result using the posture table; and
9. report boundary omissions and residual uncertainty.

If $x$ remains reachable after $A$ is disabled, conclude only that exclusive dependence on $A$ is unproved. Classify ceremonial attribution only if the system claimed $A$ was necessary and no realized or alternative valid role explains the result. Classify laundering only when the realized path lacks a valid warrant or bypasses a mandatory filter.

## 10. Sufficient Assurance Condition

The original "Prevention Theorem" is retained as a target, not an established biconditional. A bounded system has strong evidence against observed laundering when:

1. effect, actor, authority, and version identities are exact;
2. all effect-producing transitions inside $B$ are covered;
3. every realized path has a valid warrant under current policy;
4. mandatory gates are non-bypassable and causally effective;
5. alternative authorities and fallback paths are modeled;
6. execution cannot widen admitted capability or mutate payload after review;
7. receipts bind proposal, criteria, authority, verdict, execution, result, and lineage;
8. independent replay or verification detects hidden divergence; and
9. composition preserves these conditions across subsystem seams.

Under an explicit finite model, these conditions may support a relative theorem about that model. They do not prove real-world laundering freedom if $B$ is incomplete, the model is unsound, effect equivalence is wrong, or implementation differs from the model.

## Part III: Realization and Corpus Integration

## 11. Deterministic-First Realization

The deterministic-first program remains compelling. Build pipelines, release systems, policy engines, and constrained tool orchestrators can expose finite state and exact authority transitions more readily than open-ended learned systems. The first target should be a small executable model with explicit effect identities, authority registry, alternative-warrant cases, receipts, and negative tests.

For stochastic or unbounded systems, a sound over-approximation $\mathcal{R}^\sharp$ can prove unreachability when the effect is absent from the concretized over-approximation. Inclusion is generally inconclusive. Deterministic gates around learned components can bound external effects, but only if all effect paths traverse those gates and the gate-to-effect binding cannot be swapped, raced, or bypassed.

The worked runtime example in the source is retained as an author-reported case. It has not been independently executed or verified in this pass and therefore cannot carry evidentiary standing here.

## 12. Composition and Non-Interference

Laundering freedom does not automatically compose. Two locally governed systems may create an ungoverned effect through shared credentials, aliases, retries, caches, side channels, fallback routes, or inconsistent authority semantics. Disjoint latent-authority sets are neither always necessary nor sufficient without an interface model.

A composition contract should bind shared identities, authority translation, interface capabilities, joint admission, cross-system receipts, failure atomicity, replay, and revocation propagation. The general composition theorem remains open. Constraint-bearing composition, evidence-carrying interfaces, and semantic custody provide direct corpus interfaces for pursuing it.

## 13. Universal GSM and Realization Funnel

Authority Laundering Theory becomes a universal-GSM analysis over typed effect, path, identity, authority, policy, intervention, receipt, and evidence objects. The GSM can retain competing causal models and warrant claims without merging them. GMB can govern their current standing and revision lineage.

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

- **Possibility:** enumerate laundering mechanisms, authority topologies, and interventions.
- **Specification:** define effect identity, valid warrants, filters, authorities, jurisdictions, and receipts.
- **Configuration Manifold 1 (CM1):** retain configurations meeting mandatory coverage, authority, custody, and non-bypass constraints.
- **Configuration Manifold 2 (CM2):** prefer among admissible models by precision, cost, reversibility, and comprehensibility.
- **IC:** choose an **Instance Constitution** or **Instance Configuration** for one bounded system. The names are interchangeable.
- **IR:** construct an **Instance Realization** or **Implementation Realization** of that same stage. The names are interchangeable.
- **Evidence:** run removals, bypass attacks, alternative-warrant tests, replays, and lineage checks.
- **Revision:** change the boundary, policy, model, or implementation while preserving prior results and invalidations.

No IC is selected and no IR is certified by this paper.

## Dual Audit of Authority Attribution

The completed P1 corpus makes Authority Laundering Theory the **dual audit of authority attribution**: a claimed authority path must be both normatively valid and causally effective for the exact realized effect. The theory diagnoses promotion failure; it does not itself supply the authority root, witness schema, enforcement layer, or final legitimacy judgment.

- **Adjacent work:** *Warrant by Structure*  
  **Supplies:** Assurance relation over authority, mediation, effects, receipts, and bypasses.  
  **Authority-laundering boundary:** Laundering analysis is an adversarial test of one warrant dimension, not the whole warrant.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Evidence artifacts for authority, occurrence, continuity, semantics, and evaluation.  
  **Authority-laundering boundary:** Witnesses can expose or conceal laundering; artifact presence is not authority.

- **Adjacent work:** *Legitimacy Without Self-Ratification*  
  **Supplies:** Independence and non-self-promotion constraints.  
  **Authority-laundering boundary:** Supplies one necessary legitimacy condition, not the entire normative authority model.

- **Adjacent work:** *Integrity Enforcement Layer*  
  **Supplies:** Enforces selected authority and integrity predicates before protected effects.  
  **Authority-laundering boundary:** Enforcement can be causally effective while enforcing an illegitimate or stale root.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Translation of constitutional commitments into operational gates.  
  **Authority-laundering boundary:** Compilation can preserve, distort, or bypass authority and must expose semantic remainder.

For effect instance $e$, the audit separates:

$$
NormValid(a,e,j,t) \quad\text{and}\quad Causal(a,e,path,t).
$$

This yields at least six postures: `SUPPORTED_AUTHORITY`, `SHARED_OR_REDUNDANT_AUTHORITY`,  
`NORMATIVE_ONLY_CEREMONIAL`, `CAUSAL_BUT_ILLEGITIMATE`, `UNVERIFIABLE`,  
and   
`LAUNDERED_OR_BYPASSED`. A failed removal test establishes neither laundering nor absence of authority until lawful alternatives, fallback paths, common causes, and the intervention's validity are examined.

Corpus integration adds a propagation rule. When an authority attribution is downgraded, every dependent admission, execution, receipt interpretation, warrant, standing decision, and public claim must be enumerated. The system records whether each dependent is unaffected, narrowed, contested, quarantined, or withdrawn. Repairing the gate cannot silently repair prior effects.

The universal GSM can type   
`CLAIMS_AUTHORITY_OVER`, `NORMATIVELY_WARRANTED_BY`,  
`CAUSALLY_MEDIATES`, `ALTERNATIVELY_WARRANTED_BY`, `BYPASSES`, `ATTRIBUTED_TO`,  
`DOWNGRADED_BY`,  
and   
`INVALIDATES_DEPENDENT`. These relations preserve competing causal and normative models.

This integration establishes four editorial commitments: adopt dual audit as the official corpus role; adopt the six diagnostic postures; require dependent-claim propagation after authority downgrade; and decide which external normative theory supplies the authority-validity criterion rather than leaving it implicit.

## Authority Across Retrieval, Exigence, Translation, and Enforcement

The fixed-seed comparison with governed retrieval, the Cognitive Kernel, Governance as Compilation, and the Integrity Enforcement Layer gives an authority claim both a normative and causal path:

$$
\begin{aligned}
A^*= (&effect, claimed\_authority, normative\_warrant, \\
&causal\_path, retrieval\_origin, exigence\_use, \\
&translation\_stages, enforcement, evidence, alternatives, \\
&dependents)
\end{aligned}.
$$

Retrieved relevance and citation prestige are evidence attributes, not authority. CogK urgency, attention, and custody can identify and manage a need without manufacturing jurisdiction. A compilation pipeline can preserve, narrow, lose, or counterfeit authority at each edge; successful translation does not prove legitimate input or output.

The Integrity Enforcement Layer supplies the causal mechanism that permits, refuses, defers, contains, or records an effect. Its effectiveness must be audited separately from the legitimacy of the rule it enforces. A technically successful refusal can implement an invalid authority claim, while a valid authority claim can fail through a broken causal path.

The universal GSM can type   
`RETRIEVED_AS_EVIDENCE_NOT_AUTHORITY`,  
`TRIGGERED_BY_EXIGENCE_NOT_JURISDICTION`, `PRESERVES_AUTHORITY_ACROSS_STAGE`,  
`LOSES_AUTHORITY_AT_EDGE`, `ENFORCED_BY_IEL`, `AUDITS_NORMATIVE_AND_CAUSAL_PATHS`,  
and   
`PROPAGATES_AUTHORITY_DOWNGRADE_TO_DEPENDENTS`.

This randomized review establishes four editorial commitments: adopt the extended authority object; audit retrieved and exigence-mediated claims before promotion; require authority preservation and loss records across compilation; and separate IEL causal effectiveness from normative validity.

## The Dual Audit of Normative Lineage and Causal Control

Seventeen downstream uses confirm Authority Laundering Theory as a cross-domain adversarial diagnostic. It is used against retrieval that treats source labels as mandate; translation and compilation that inherit authority through form; witnesses or human-review surfaces that are not causally load-bearing; semantic maps and ontology changes that obscure authority shifts; enforcement machinery with defective roots; trade and custody handoffs that treat transmission or possession as grant; and kernels, warrants, and legitimacy procedures that confuse successful process with lawful standing.

The case object is:

$$
\begin{aligned}
A^*= (&claim, effect, authority\_source, jurisdiction, grant, \\
&delegations, transformations, intermediaries, \\
&visible\_process, decision\_path, effect\_path, \\
&controllers, alternatives, removal\_tests, evidence, \\
&classification, remedy, appeal)
\end{aligned}.
$$

The audit has two independent axes. **Normative lineage** asks whether the authority source and every delegation lawfully cover the subject, jurisdiction, time, and effect. **Causal control** asks which actor, rule, model, credential, interface, or hidden channel actually changed the decision or effect. A valid root can be ceremonial; a causally decisive actor can be unauthorized; and a valid process can carry a defective root. Neither axis substitutes for the other.

Removal and perturbation tests should target the claimed authority, visible approver, hidden controller, policy, credential, route, and alternative. If removing a nominal reviewer changes nothing, the review may be ceremonial. If removing an unofficial actor changes the outcome, that actor may hold de facto control. These are causal findings, not proof of intent, corruption, illegality, or moral fault. The docket must retain good-faith error, ambiguity, drift, emergency action, capture, coercion, and deliberate laundering as competing explanations.

The wider alias search produced ten rejected hits in which "authority laundering" appears only as a generic failure label, analogy, or unsupported warning without applying this paper's dual audit or removal test. Those remain retrieval leads rather than dependencies.

The universal GSM can type   
`TRACES_NORMATIVE_AUTHORITY_LINEAGE`,  
`MEASURES_CAUSAL_CONTROL`, `REMOVES_NOMINAL_APPROVER`, `REVEALS_HIDDEN_CONTROLLER`,  
`TRANSMITS_WITHOUT_AUTHORITY_GAIN`, `PRESERVES_COMPETING_EXPLANATION`,  
`REMEDIATES_LAUNDERED_EFFECT`, and   
`WITHHOLDS_INTENT_OR_LIABILITY_FINDING`.

This reverse-dependency review establishes four editorial commitments: adopt the dual-axis case object; require targeted removal and perturbation tests; distinguish root, transmission, process, validation, retrieval, container, and role laundering; and retain intent, legality, fault, and remedy as separately evidenced conclusions.

## 14. Internal Counterevidence and Falsifiers

The framework must narrow, abstain, or fail where:

1. effect identity is too coarse and conflates different instances;
2. the intervention changes unrelated policy or state;
3. disabling an authority activates a valid fallback;
4. several authorities are independently sufficient;
5. authority is valid but not exclusively causal;
6. a causal dependency is mistaken for normative authority;
7. missing lineage is treated as proof of historical illegitimacy;
8. receipts describe a path other than the realized one;
9. filtering stages are not reductive or order-independent;
10. a later stage repairs an earlier ambiguity;
11. hidden state or external services escape $B$;
12. the reachability abstraction is unsound;
13. state explosion prevents the claimed exact test;
14. an apparently ceremonial control is intentional defense-in-depth;
15. a mandatory gate is bypassed after admission through mutation or race;
16. revocation fails to propagate to cached or delegated authority;
17. composition creates shared authority absent from local models;
18. the authority registry itself is stale or captured;
19. policy declares a path valid that is morally or legally defective;
20. different jurisdictions issue incompatible but locally valid warrants;
21. the model proves only a toy projection while prose claims system-wide assurance;
22. the proposed diagnostic adds no value beyond direct capability, policy, and provenance tests.

These are not peripheral caveats. They define the empirical and formal program required to establish the theory's reach.

## Reachability Does Not Legitimize Itself

### Public orientation

Authority Laundering Theory studies how transformations, retrieval, translation, interfaces, or delegation can make an action appear authorized while its normative lineage or causal control no longer supports that appearance. The definition of authority as admissible semantic reachability is a formal proposal within this architecture, not a complete legal, political, or moral theory of authority.

### Adversarial tests

1. **Admission-legitimacy attack.** A path is admissible under corrupt or unauthorized rules. Reachability requires valid governing authority, not merely local acceptance.
2. **Delegation-chain attack.** Scope expands through aliases, groups, inheritance, defaults, or retransmission. Every hop must conserve and attenuate authority explicitly.
3. **Translation-laundering attack.** A semantic transform changes obligation while preserving authoritative appearance. Source and target commitments need property-level correspondence.
4. **Retrieval-laundering attack.** Relevant text is surfaced and treated as permission. Relevance, standing, jurisdiction, and authority are separate relations.
5. **Interface-laundering attack.** A button, API, or workflow makes an effect available and users infer authorization. Affordance and lawful grant must not collapse.
6. **Proxy-authority attack.** An evaluator, model, or witness speaks about authority and is treated as the authority itself.
7. **Causal-control mismatch.** The named principal appears responsible while another actor or mechanism controls the effect. Normative lineage and causal control require dual audit.
8. **Formal-theorem overreach.** A result proven from the paper's definitions is presented as an empirical law. The theorem's assumptions and domain remain explicit.

### Claim and evidence ceiling

The paper supplies a formal theory of legitimacy-preserving transformation and a dual audit of normative lineage and causal control. Its theorems hold within declared definitions and assumptions. They do not settle legal authority, political legitimacy, moral justification, actual responsibility, or empirical prevalence.

Claims about law, institutions, security, language, organizations, or real incidents require current external evidence and qualified domain review. Internal corpus examples demonstrate the proposed pattern only. No external research was added in this pass.

### Reader-facing consequence

The public test is whether an apparent permission can be traced both backward through an unbroken authorized lineage and forward to the actor and mechanism that actually controlled the effect.

## Conclusion

Authority laundering names a real architectural danger: effects can acquire the appearance of legitimacy while bypassing the transformations that would warrant them. The source's decisive insight survives audit: governance should change reachable behavior, and its claims should be reconstructable.

The repaired theory refuses two shortcuts. Causal necessity is not authority without normative warrant, and causal non-necessity is not laundering when alternative lawful warrants exist. The proper object is the exact realized effect path under a declared boundary. That path must preserve identity, projection, binding, admissibility, capability, and lineage, while the authority attributed to it must be both valid and operationally meaningful.

The result is not yet a universal theorem. It is a strong, falsifiable research and engineering program: model the effect and warrant, intervene on the claimed authority, search for lawful alternatives and bypasses, reconstruct the realized path, receipt the finding, and state precisely what remains unknown.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Instance Configuration.** The present paper does not claim a complete instance configuration treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that authority laundering occurs when an effect is presented as legitimately authorized although the effect instance lacks a valid, reconstructable warrant path or bypassed a mandatory authority-bearing transition. Its nearest external comparison fields are security, governance, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E2]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E3]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

**[E4]** Robert N. M. Watson, Simon W. Moore, Peter Sewell, and Peter G. Neumann. *An Introduction to CHERI*. University of Cambridge Technical Report UCAM-CL-TR-941, 2019. DOI: 10.48456/tr-941. [cl.cam.ac.uk source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-941.html) **Relationship:** Adjacent capability architecture demonstrating unforgeable hardware authority and compartmentalization.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

#### Source-head external references retained under original labels

The following bibliography is retained from the source manuscript and was not externally checked in this pass.

[2] B. C. Pierce. *Types and Programming Languages.* MIT Press, 2002.

[3] M. S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control.* PhD thesis, Johns Hopkins University, 2006.

[4] J. Pearl. *Causality: Models, Reasoning, and Inference.* Cambridge University Press, 2nd ed., 2009.

[5] P. Cousot and R. Cousot. *Abstract Interpretation.* POPL, 1977.

[6] J. H. Saltzer and M. D. Schroeder. *The Protection of Information in Computer Systems.* Proc. IEEE, 1975.

[7] G. C. Necula. *Proof-Carrying Code.* POPL, 1997.

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

**[A6]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

#### Ableman Corpus references

[1] A. Ableman Ableman. *Semantic Reactor Theory: Governance-Native Architecture for High-Authority Semantic Transformation Systems.* Working paper.

[8] A. Ableman Ableman. *The CSoftA Corpus.* Internal corpus.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847386](https://doi.org/10.5281/zenodo.23847386)
