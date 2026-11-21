# Constitutionally Governed Infrastructure

## From Software Schedulers to Institution-Scale Continuation Control

### Terrain, weather, component failure, and passive physical constraints can shape possibility without possessing discretion or legitimate power.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Infrastructure determines more than throughput. Queues, schedulers, routers, allocation rules, eligibility checks, administrative pipelines, and communication channels shape which continuations are available, timely, affordable, visible, or practically unreachable before an explicit decision is made. This paper develops **Constitutionally Governed Infrastructure (CGI)** as a framework for bringing materially consequential continuation-control machinery inside constitutional review.

The claim requires an important distinction. Not every causal influence exercises authority. Terrain, weather, component failure, and passive physical constraints can shape possibility without possessing discretion or legitimate power. Infrastructure becomes constitutionally relevant when a mechanism materially and persistently controls access, order, timing, allocation, disclosure, or effect under rules or configurations that can be selected, delegated, contested, captured, or changed. Such control may express legitimate authority, delegated authority, de facto power, or unauthorized authority migration. Those categories must not be collapsed.

CGI therefore requires more than receipts. A governed infrastructure surface must bind mechanism identity, jurisdiction, authority, policy, configuration, inputs, outputs, affected subjects, reasons, evidence, challenge, remedy, liveness, emergency behavior, privacy, security, revision, and measurable outcomes. Reconstructability is necessary but does not itself establish fairness, legitimacy, correctness, or accountability.

The source's Universal Governance Kernel (UGK) scheduler is retained as an internal architectural example rather than an empirical demonstration. Its concepts of earned independence, constitutional scheduling, and infrastructure receipts generate testable obligations, but the supplied paper contains no implementation evidence, performance benchmark, scheduler trace, or deployment comparison. The paper also limits its extension from software to institutions and civilizational systems: a common constitutional grammar may travel, while domain law, rights, evidence, remedies, and failure costs do not automatically transfer.

This revision formalizes effective continuation structure, defines constitutional coverage, integrates CGI with Dynatology, Constitutional Computation, Governance Coverage Gaps, receipts, work custody, constraint-bearing composition, GMB, and the universal GSM, and locates the framework in the full realization funnel. It remains a proposal and specification, not a proven institutional or technical system.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/`

`constitutionally-governed-infrastructure/`  
`integration-custody-manifest.v0.1.json`,  
SHA-256  
`4FA496B64F2E2BBD0C2EE8AE2E933EE91DE181B60E915F73F2DB2833F0322FA1`. The exact source remains unchanged.

The CGI proposal, continuation-control thesis, authority-migration framing, UGK scheduling example, earned independence, constitutional scheduling, infrastructure receipts, Dynatology relationship, and civilizational extension are author material. The formal model, categorical distinctions, coverage contract, evidentiary correction, measurement obligations, countertests, and decision surface are AI editorial or synthetic additions until adopted.

No external research was conducted. The source-supplied bibliography is preserved later as unverified author material. No legal, political, institutional, implementation, conformance, canonical, or publication standing is granted.

## 1. Infrastructure Precedes Many Decisions

Political and administrative analysis often begins with explicit decisions: who decides, under what authority, by what procedure, and with what avenue of challenge. Yet explicit decisions occur inside constructed environments.

Applications enter queues. Cases enter calendars. Goods enter routes. Computation enters schedulers. Information enters ranking and distribution systems. Each environment shapes the set, cost, latency, reliability, and visibility of later choices. A permit that never reaches review, a case scheduled after its practical value expires, or a task starved of resources can be functionally decisive without a formal denial.

CGI begins with a bounded thesis:

> Infrastructure that materially controls consequential continuations should be treated as a constitutional subject rather than dismissed as a neutral implementation detail.

This does not mean all infrastructure is malicious, that all delay equals denial, or that every physical constraint exercises authority. It means the mechanisms through which governing rules become practical access and effect belong inside the scope of governance.

## 2. Influence, Control, Power, and Authority

Four concepts must remain distinct:

- **causal influence:** any condition that changes an outcome or possibility;
- **infrastructural control:** a mechanism's capacity to alter availability, order, timing, cost, allocation, disclosure, or effect;
- **de facto power:** control that materially shapes subjects' options whether or not it is authorized; and
- **authority:** a normatively or constitutionally recognized power to make a specified decision or produce a specified effect.

An algorithm may exercise delegated authority. A private platform may possess de facto power without public authority. A misconfigured queue may create consequential control without anyone intentionally exercising discretion. A storm may restrict access without exercising either power or authority.

The original statement that any mechanism influencing continuation "exercises authority" is therefore too broad. A stronger constitutional principle is:

> Any configurable or governable mechanism that materially, persistently, and consequentially controls continuations creates an authority-relevant surface. Its legitimate powers, de facto powers, delegated powers, failures, and unauthorized effects must be classified and governed.

This formulation preserves the paper's central concern without turning causation into authority by definition.

## 3. Formal Model of Effective Continuation

Let $P(s)$ be the raw set of transitions physically or logically possible from state $s$. Let $A_J(s) \subseteq P(s)$ be the transitions admitted under jurisdiction $J$. Let $E_I(s) \subseteq P(s)$ be the transitions enabled by infrastructure configuration $I$.

The effective continuation set is:

$$
C_{I,J}(s)=P(s)\cap A_J(s)\cap E_I(s).
$$

Membership alone is insufficient. Infrastructure also changes the practical accessibility of a transition. For $t \in C_{I,J}(s)$ define an access vector:

$$
k_I(s,t)=(\ell,c,r,d,p),
$$

where $\ell$ is latency, $c$ cost, $r$ reliability, $d$ discoverability, and $p$ allocation or completion probability under the declared model. Additional domain dimensions may include safety, privacy, legal exposure, energy, capacity, or human burden.

Infrastructure $I$ has **material continuation control** over transition $t$ when an available change in its rules or configuration alters membership in $C_{I,J}(s)$ or changes a declared component of $k_I(s,t)$ beyond a materiality threshold relevant to affected rights, obligations, services, risks, or outcomes.

The threshold is not universal. A millisecond may be material in a safety controller and immaterial in a permit queue. A small ranking change may be material when it systematically suppresses access. CGI therefore requires domain-specific materiality, not merely mathematical sensitivity.

## 4. Authority Migration

**Authority migration** occurs when a consequential decision surface moves from an explicitly governed role into a mechanism, configuration, optimization objective, data pipeline, exception path, or operational convention that lacks equivalent constitutional coverage.

Migration can be intentional or accidental. Examples include:

- a legislature declares eligibility while an undocumented data transform decides who appears eligible;
- a policy grants equal access while a scheduler repeatedly starves one class of request;
- an institution publishes appeal rights while routing prevents affected people from reaching the appeal channel;
- a human retains nominal approval while defaults, ranking, time pressure, and interface design determine nearly every result; or
- an emergency path becomes the ordinary path without amendment.

The diagnostic question is not simply "who made the final decision?" It is:

> Which mechanisms materially determined the effective continuation set and access vector, under whose authority, with which evidence, and with what path to challenge and remedy?

## 5. Constitutional Infrastructure Contract

A CGI profile should cover at least the following surfaces:

1. **mechanism identity:** exact scheduler, queue, model, rule set, version, and operator;
2. **jurisdiction:** the regime that governs each decision and boundary crossing;
3. **authority:** who may configure, invoke, override, inspect, and amend the mechanism;
4. **policy/configuration separation:** which constraints are invariant and which are chosen parameters;
5. **input custody:** provenance, admissibility, privacy, integrity, and temporal validity of inputs;
6. **decision semantics:** the possible outcomes and their exact meanings;
7. **reason and evidence:** why a transition was enabled, delayed, prioritized, refused, or escalated;
8. **effect boundary:** which consequential actions can follow and through which gate;
9. **receipts:** typed records for proposal, admission, scheduling, effect, verification, and override;
10. **challenge and remedy:** who can contest, correct, reverse, compensate, or amend an outcome;
11. **liveness and availability:** deadlines, starvation prevention, bounded deferral, capacity failure, and continuity;
12. **rights and distribution:** disparate burden, exclusion, accessibility, and protected interests;
13. **privacy and security:** disclosure limits, observability boundaries, abuse resistance, and incident response;
14. **emergency behavior:** declared powers, duration, review, rollback, and anti-normalization controls;
15. **revision:** lineage, amendment authority, migration, compatibility, and retirement; and
16. **measurement:** outcomes, error rates, latency, throughput, burden, overrides, appeals, reversals, and unknowns.

Visibility, attribution, and reconstructability support this contract. They are not substitutes for it.

## 6. Constitutional Scheduling

A conventional scheduler maps queued work and resource state into an execution order. A constitutional scheduler additionally exposes the law and evidence of that mapping.

For queue state $Q$, resource state $R$, policy $L$, and configuration $I$, let:

$$
\sigma(Q,R,L,I)\rightarrow (D,\rho),
$$

where $D$ is a typed decision such as admit, schedule, defer, refuse, preempt, escalate, or override, and $\rho$ is the associated receipt contract.

Constitutional scheduling requires more than determinism. A deterministic policy can still be unjust, captured, unavailable, or incorrectly scoped. The scheduler must bind its authority, admissible inputs, priorities, tie-breaking, resource claims, deadlines, failure behavior, affected obligations, and challenge path.

Priority is not merely a number. It may encode rights, safety, age, urgency, contractual promise, fairness, dependency, cost, or political choice. CGI requires those semantics to remain explicit rather than disappearing inside an optimization function.

## 7. Earned Independence and Its Limits

The source proposes that operations execute independently only when independence is demonstrated through chain-verifiable evidence; otherwise they serialize. This is a valuable anti-race principle but not a universal safety theorem.

Let $o_i \perp o_j$ mean that the declared reads, writes, authorities, obligations, effects, and failure domains of operations $o_i$ and $o_j$ do not conflict under a named independence model. Parallel execution is admissible only if the model and evidence support that relation.

However, serialization can also be harmful. It may cause deadline failure, starvation, priority inversion, capacity collapse, or denial of service. When independence is unknown, the lawful fallback may be serialize, defer, refuse, isolate, acquire stronger evidence, or escalate. The choice depends on declared safety and liveness obligations.

Thus "uncertainty collapses toward safety" should be replaced with:

> Uncertainty selects the least-authorized continuation that satisfies the applicable safety, liveness, rights, and continuity constraints; when no such continuation is established, the system refuses or escalates explicitly.

## 8. Infrastructure Receipts

An infrastructure receipt can help answer why one operation proceeded before another, but receipt existence does not establish accountability. A useful scheduling receipt should bind:

- queue and request identities;
- relevant input and policy versions;
- scheduler and configuration identity;
- authority and jurisdiction;
- priority and tie-break semantics;
- resource and dependency observations;
- decision, reason, and confidence or unknowns;
- deadline and liveness state;
- effect identity or explicit absence of effect;
- disclosure and privacy posture;
- challenge, remedy, and replay references; and
- verifier identity and result where applicable.

Receipts must be usable by affected parties or legitimate reviewers within appropriate privacy and security boundaries. A perfectly reconstructable abuse remains abuse. A log that no one can challenge does not constitutionalize the system.

## 9. UGK as a Bounded Internal Case

The source describes a UGK scaling architecture in which scheduling, priority, backpressure, deferral, and refusal become governed operations. This is an important design case. The paper does not, however, provide the artifacts necessary to claim that a scheduler "survived constitutionalization" operationally or that governance introduced no unacceptable cost.

A demonstrated result would require at minimum:

- an exact scheduler and policy implementation;
- threat and capability models;
- test workloads and baselines;
- receipt examples and replay;
- safety and liveness properties;
- throughput, latency, capacity, and failure measurements;
- starvation, priority inversion, and overload tests;
- bypass and privilege-escalation attacks;
- audit, challenge, correction, and rollback trials; and
- evidence that the constitutional surface covers every material effect path.

Until then, the UGK section is a specification-level architectural example and source of obligations, not empirical evidence of operational viability.

## 10. Institutions and Civilizational Systems

The institutional analogy is plausible but must remain typed. A permit office, court calendar, logistics network, energy system, financial market, and communication network have different authority sources, rights, hazards, time constants, stakeholders, confidentiality rules, and remedies.

What may generalize is a constitutional grammar:

1. identify continuation-control mechanisms;
2. classify their causal influence, de facto power, and authority;
3. bind jurisdiction and legitimate configuration powers;
4. expose rules, evidence, outcomes, and unknowns;
5. preserve challenge, remedy, liveness, privacy, and revision; and
6. test whether governance covers every material effect route.

What does not automatically generalize is the exact scheduler, receipt schema, admissibility predicate, priority rule, or remedy. Civilization-scale claims require institutional and empirical research beyond the evidence supplied here.

## 11. Relationship to Dynatology

Dynatology studies structured potentiality: what could exist, what conditions enable it, and how possibilities are organized and selected. CGI is an applied constitutional projection over one part of that terrain.

Dynatology asks which continuations exist and how the possibility space is structured. CGI asks which infrastructure materially shapes effective continuation, who may configure it, under what law, with what evidence, and how subjects can contest its effects.

The relationship is complementary, not hierarchical identity. Dynatology does not by itself establish authority. CGI does not exhaust the study of possibility. Together they connect possibility geometry to constitutional responsibility.

## 12. Corpus Integration

**Constitutional Computation** supplies the general claim that computation can carry inspectable constitutional structure rather than treating governance as an external policy layer. **Ableman Constitutional Governance** supplies an adjacent governance framework, but its publication identity remains on review hold; this paper neither resolves nor promotes that identity.

**UGK** supplies the bounded kernel and scheduling example. **Governance Coverage Gaps** converts the CGI concern into a coverage question: does governance participate across every material capability and effect path? **Reasoning by Way of Receipts** supplies typed reconstruction without equating records with truth. **A Formal Theory of Work Custody** clarifies which actor or process is responsible for work through time. **Constraint-Bearing Composability** asks whether constitutional obligations survive infrastructure boundaries and component composition.

The **Governed Meaning Base (GMB)**, current in the `CCF -> CMB -> GMB` lineage, can retain infrastructure identities, policy and configuration versions, authority bindings, decisions, receipts, challenges, remedies, evidence, and revisions. The universal GSM can represent the primitives, invariants, dimensions, and adjacencies of those records. Inclusion in GMB or GSM is not proof that the infrastructure is legitimate or conformant.

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

- **Possibility:** enumerate infrastructure domains, continuation-control mechanisms, constitutional grammars, affected subjects, and possible remedies.
- **Specification:** define control, materiality, jurisdiction, authority, rights, coverage, receipt, challenge, liveness, privacy, security, and revision obligations.
- **Configuration Manifold 1 (CM1):** retain architectures satisfying the minimum constitutional contract and domain constraints.
- **Configuration Manifold 2 (CM2):** prefer admissible architectures by coverage, fairness, contestability, liveness, legibility, security, cost, performance, repairability, and public value.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for one infrastructure domain, mechanism, policy, jurisdiction, and evidence contract. The names are interchangeable.
- **IR:** build an **Instance Realization** or **Implementation Realization** with exact components, roles, rules, interfaces, and effect paths. The names are interchangeable.
- **Evidence:** retain measurements, receipts, audits, attacks, appeals, reversals, burdens, failures, and affected-party observations.
- **Revision:** amend rules or realization while preserving lineage, rights, evidence, and rollback.

This paper reaches Specification and proposes CM1/CM2 evaluation criteria. It does not establish a complete IC, a conforming IR, a deployed scheduler, an institutionally valid constitution, or evidence of civilizational feasibility.

## 14. Evaluation Program

CGI should be evaluated through both structural and outcome evidence:

1. inventory every material capability and effect path;
2. identify which paths lack authority, policy, observation, challenge, or remedy;
3. replay representative decisions from exact inputs and rules;
4. measure throughput, latency, deadline misses, starvation, overload, and recovery;
5. test priority inversion, manipulation, bypass, hidden defaults, and unauthorized override;
6. compare burdens and outcomes across affected groups and cases;
7. test disclosure minimization and legitimate review access;
8. exercise appeal, correction, rollback, compensation, and amendment;
9. inject incomplete, conflicting, stale, and adversarial evidence;
10. test cross-jurisdiction transfer and obligation carriage; and
11. publish claim-bounded results, including unknowns and failed coverage.

No single metric proves constitutional governance. High throughput can coexist with arbitrary exclusion; perfect replay can coexist with unjust rules; complete receipts can coexist with an ungoverned bypass.

## Constitutional Continuation-Control Profile

Across the completed P1 corpus, Constitutionally Governed Infrastructure is the **constitutional continuation-control profile for mechanisms that shape practical access before or around an explicit decision**. It locates scheduling, routing, eligibility, allocation, backpressure, disclosure, and administrative reachability inside the governed effect surface without calling every causal condition an authority.

- **Adjacent work:** *Dynatology*  
  **Supplies:** Structured possibility and realization conditions.  
  **CGI boundary:** CGI governs configurable mechanisms that materially shape which possibilities remain practically reachable.

- **Adjacent work:** *Universal Governance Kernel (UGK)*  
  **Supplies:** A kernel-scale example of admission, scheduling, refusal, and evidence.  
  **CGI boundary:** UGK is one realization family; CGI is the domain-independent infrastructure profile.

- **Adjacent work:** *Governance Coverage Gaps*  
  **Supplies:** Detection of consequential capabilities or effects outside governance scope.  
  **CGI boundary:** CGI specializes the search to continuation-control machinery and practical access.

- **Adjacent work:** *The Mechanics of Constitutional Enforcement*  
  **Supplies:** Non-bypassable mediation, effect gates, courts, and receipts.  
  **CGI boundary:** CGI adds liveness, priority, burden, challenge, and remedy obligations to infrastructure control.

- **Adjacent work:** *The Constitutional Observability Platform*  
  **Supplies:** Role-aware projection of state, standing, effects, and evidence.  
  **CGI boundary:** Observability exposes the control surface but does not establish legitimate scheduling or allocation.

The paper's integrative object is not a queue alone but a constitutionalized continuation surface:

$$
K=(P,A,E,U,J,W,L,C,R,X),
$$

where $P$ is physical or logical possibility, $A$ authorized continuation, $E$ enabled continuation, $U$ practically usable continuation, $J$ jurisdiction, $W$ warrant, $L$ liveness, $C$ contestability, $R$ remedy, and $X$ exact evidence. A system may have a nonempty authorized set while making every useful member too late, costly, undiscoverable, or unreliable to exercise.

The main new corpus connection is therefore between possibility geometry and institutional effect. Constitutional computation governs more than the final ALLOW or REFUSE event when earlier infrastructure can starve, rank, price, hide, defer, or redirect a continuation. Conversely, infrastructure governance must not imply that a weather event, hardware limit, or passive terrain feature possesses authority. The relevant threshold is persistent, material, and governable control under a selectable or contestable rule or configuration.

The universal GSM can type   
`SHAPES_EFFECTIVE_CONTINUATION`, `NARROWS_PRACTICAL_ACCESS`,  
`EXERCISES_DE_FACTO_CONTROL`, `OPERATES_UNDER_DELEGATED_AUTHORITY`,  
`MIGRATES_AUTHORITY_TO_CONFIGURATION`, `RISKS_STARVATION`, `PRESERVES_LIVENESS`,  
`SUPPORTS_CHALLENGE`, `PROVIDES_REMEDY`,  
and   
`REMAINS_DISTINCT_FROM_PASSIVE_CAUSE`. These relations prevent both authority inflation and infrastructure invisibility.

This integration establishes four editorial commitments: retain CGI as the constitutional continuation-control profile; adopt the $P/A/E/U$ separation and full constitutionalized-continuation envelope; require liveness, contestability, remedy, and affected-party evidence alongside receipts; and keep UGK, Dynatology, observability, enforcement, and CGI as typed neighbors rather than merged identities.

## Human-Domain Firewall, Migration Continuity, Commitment Limits, and Governed Resolution

The fixed-seed comparison with The Well-Governed Mind, model-first legacy migration, CHC, and Constitutional Binding Theory tests continuation control across human, technical, cryptographic, and semantic boundaries:

$$
\begin{aligned}
K^*= (&possibility, authorization, enablement, usability, \\
&jurisdiction, warrant, liveness, accessibility, \\
&binding\_rule, commitments, contest, remedy, migration, \\
&exact\_evidence)
\end{aligned}.
$$

The Well-Governed Mind does not supply institutional evidence for CGI. It instead enforces a cross-domain firewall: infrastructure that affects care, cognition, education, or participation requires domain law, accessibility analysis, qualified review, and affected-party evidence before architectural vocabulary supports a claim.

Model-first legacy migration exposes how infrastructure authority and de facto control can move during replacement. A successor may preserve nominal policy while dropping routing, fallback, accessibility, notice, remedy, or provider-exit capabilities. Operational continuity and changed burdens must therefore be evaluated, not inferred from successful cutover.

CHC can commit to exact configurations, claim envelopes, policies, and epoch-relative decisions, but a hash or signature cannot prove liveness, legitimacy, usability, or remedy. Constitutional Binding Theory describes how an identity, request, entitlement, route, or policy anchor resolves to a target under context and law; deterministic resolution can still enact defective rules.

The universal GSM can type   
`SHAPES_HUMAN_ACCESS_UNDER_FIREWALL`,  
`MIGRATES_CONTINUATION_CONTROL`, `COMMITS_TO_INFRASTRUCTURE_CONFIGURATION`,  
`DOES_NOT_PROVE_LIVENESS_BY_HASH`, `RESOLVES_ACCESS_ANCHOR_UNDER_LAW`,  
`CONTESTS_BINDING_RULE`, and   
`PROVIDES_PRACTICAL_REMEDY`.

This randomized review establishes four editorial commitments: add a human-domain evidence firewall; require migration-specific continuation and burden tests; separate cryptographic commitment from live constitutional performance; and model infrastructure routing as governed resolution without equating deterministic output with legitimate authority.

## A Nested Continuation-Control Plane

Three downstream uses confirm Constitutionally Governed Infrastructure as a continuation-control profile with nested technical realizations. Jnana II uses it to extend transformation governance into runtime and institutional effect paths. Governance Coverage Gaps tests whether configuration and consequences escape the declared infrastructure surface. The Direct-Coupled Dynamic Torque Reactor specializes scheduling, allocation, liveness, and control obligations to safety-critical physical energy distribution without transferring empirical findings across domains.

The downstream interface is:

$$
\begin{aligned}
I^*= (&domain, mechanisms, resources, requests, subjects, \\
&authority, power, jurisdiction, policy, scheduling, \\
&allocation, routes, deadlines, liveness, accessibility, \\
&safety, privacy, effects, coverage, challenge, remedy, \\
&evidence, revision)
\end{aligned}.
$$

Infrastructure is nested: a governed application may depend on an ungoverned scheduler, credential plane, network, provider, firmware controller, emergency route, or human administrative process. Each layer may shape effective continuation and may carry different authority, evidence, and remedy. A parent contract cannot claim closure merely because one child component is governed; the dependency and bypass surface must be enumerated or left explicitly unknown.

Physical and institutional projections require domain law and evidence. A scheduling grammar can travel; safety thresholds, rights, materiality, deadlines, failure costs, and remedies do not travel automatically. The DCDTR relation is therefore a specialization interface, not proof that CGI has been implemented or validated in a physical plant.

The universal GSM can type   
`CONTROLS_CONTINUATION_AT_LAYER`,  
`DEPENDS_ON_INFRASTRUCTURE_LAYER`, `BYPASSES_GOVERNED_CONTINUATION_ROUTE`,  
`SPECIALIZES_SCHEDULING_FOR_PHYSICAL_DOMAIN`, `PRESERVES_DOMAIN_FIREWALL`,  
`TESTS_NESTED_INFRASTRUCTURE_COVERAGE`, and   
`RETAINS_UNGOVERNED_DEPENDENCY_UNKNOWN`.

This reverse-dependency review establishes four editorial commitments: adopt the nested continuation-control plane; require dependency and bypass coverage at every layer; preserve domain-specific law and evidence for physical or institutional profiles; and prevent a governed component from promoting the whole infrastructure to constitutional standing.

## 15. Counterevidence and Failure Modes

CGI should be narrowed or rejected where: (1) passive causation is mislabeled as authority; (2) de facto power and legitimate authority are collapsed; (3) materiality has no domain-specific threshold; (4) the possible, admissible, enabled, and practically accessible sets are conflated; (5) a queue delay is called denial without a declared deadline or harm model; (6) constitutionalization covers logs but not effect paths; (7) the governing policy is itself outside review; (8) configuration changes silently alter rights or obligations; (9) receipts cannot be connected to actual effects; (10) affected subjects cannot access a meaningful explanation; (11) challenge exists without correction or remedy; (12) privacy is sacrificed for auditability; (13) secrecy prevents legitimate review with no compensating mechanism; (14) deterministic operation is mistaken for legitimacy; (15) serialization causes starvation, deadline failure, or denial of service; (16) claimed independence omits shared resources or failure domains; (17) emergency powers become ordinary operation; (18) overrides lack expiry, review, or rollback; (19) governance machinery becomes a new capture point; (20) the verifier, auditor, or receipt store is outside constitutional coverage; (21) optimization proxies displace declared policy; (22) the system is formally fair but inaccessible in practice; (23) cross-jurisdiction transfer drops obligations; (24) an unobserved fallback bypasses the governed path; (25) implementation overhead makes critical services unavailable; (26) the UGK case lacks exact artifacts or measurements; (27) software grammar is transferred to institutions without domain law or empirical validation; (28) the source-supplied bibliography does not support the claims attributed to it; (29) CGI duplicates another corpus identity without a differentiated capability; or (30) external evidence shows that a proposed institutional or technical generalization is false.

## Infrastructure Controls Access Without Automatically Possessing Authority

### Public orientation

Constitutionally Governed Infrastructure studies queues, schedulers, routers, allocation rules, administrative pipelines, and other mechanisms that shape which continuations are available, timely, affordable, visible, or practically unreachable. These mechanisms can exercise delegated authority, de facto power, or unauthorized control. Passive causation and physical constraint are not themselves authority.

### Adversarial tests

1. **Causation-authority attack.** Any condition affecting an outcome is labeled an authority surface, erasing the difference among weather, failure, configuration, power, and legitimate delegation.
2. **Nested-closure attack.** A governed application promotes its scheduler, provider, network, credentials, firmware, emergency route, and human administration to governed status without evidence.
3. **Delay-denial attack.** Latency is classified as constitutional denial without a domain deadline, materiality threshold, affected right, or harm model.
4. **Formal-fairness attack.** Equal rules produce inaccessible, systematically delayed, unaffordable, or practically unreachable continuations for some subjects.
5. **Receipt-accountability attack.** A trace exists but affected subjects cannot obtain explanation, challenge, correction, remedy, or proof of actual effect.
6. **Optimization-migration attack.** A ranking, scheduling, or allocation proxy acquires decisive power while the declared policy remains nominally unchanged.
7. **Emergency-capture attack.** Overrides and break-glass routes lack expiry, review, rollback, and independent evidence, then become ordinary infrastructure.
8. **Institutional-transfer attack.** A software scheduling grammar is applied to civic, legal, economic, or physical systems without domain rights, law, expertise, evidence, and remedies.

### Claim and evidence ceiling

The paper offers a continuation-control profile and nested infrastructure contract. It does not establish that every causal influence has authority, that one component governs its dependencies, that observed scheduling is legitimate or fair, or that the UGK example is implemented. Technical, institutional, physical, and civilizational projections remain hypotheses.

Claims about infrastructure governance, public administration, law, rights, algorithms, scheduling, institutions, safety, fairness, or social outcomes require current external research, exact implementations, affected-party evidence, and qualified domain review. No external research was added in this pass.

### Reader-facing consequence

The public question is who or what practically controls access, timing, allocation, visibility, and remedy - including every hidden dependency - and whether that control is authorized, challengeable, and materially fair in the relevant domain.

## 17. Conclusion

Infrastructure often governs practical possibility before an institution issues a visible decision. That observation is constitutionally important, but it does not make every causal influence an authority. CGI is strongest when it identifies the narrower surface where configurable, consequential continuation control carries delegated authority, de facto power, or the risk of authority migration.

Constitutionalizing that surface requires more than a log. It requires authority, jurisdiction, policy, configuration, effect, evidence, challenge, remedy, liveness, rights, privacy, security, and revision to remain connected. A scheduler, queue, router, or administrative pipeline is governed only when every material route through which it shapes consequential continuations is inside that contract.

The research contribution is therefore a specification and evaluation program: govern not only explicit decisions, but also the machinery that determines which decisions can be reached, when, at what cost, and with what possibility of correction.

## Corpus-Wide Reference Positioning

This paper argues that infrastructure determines more than throughput. Its nearest external comparison fields are cps, governance, open sovereign. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Runtime monitors and fallback controllers only protect modeled safety envelopes and can fail through sensor error, timing assumptions, unsafe recovery, or omitted hazards. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Source availability and reproducible builds improve inspectability but do not alone guarantee comprehensibility, practical exit, hardware control, or sustainable maintenance. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Edward R. Griffor et al. *Framework for Cyber-Physical Systems: Volume 1, Overview*. NIST SP 1500-201, 2017. DOI: 10.6028/NIST.SP.1500-201. https://doi.org/10.6028/NIST.SP.1500-201 **Relationship:** Adjacent cyber-physical systems framework for trustworthiness, timing, data, and lifecycle concerns.

**[E2]** J. Tanner Slagel et al. "A Formal Verification Framework for Runtime Assurance." *NASA Formal Methods*, 2024. NASA NTRS 20230017350. https://ntrs.nasa.gov/citations/20230017350 **Relationship:** Adjacent runtime-assurance formalization, useful for comparing failover safety with constitutional admission and effect recognition.

**[E3]** Nancy G. Leveson and John P. Thomas. *STPA Handbook*. MIT, 2018. https://psas.scripts.mit.edu/home/books-and-handbooks/ **Relationship:** Adjacent systems-theoretic hazard analysis method; used to test treatment of unsafe control and system-level constraints.

**[E4]** Robert N. M. Watson, Simon W. Moore, Peter Sewell, and Peter G. Neumann. *An Introduction to CHERI*. University of Cambridge Technical Report UCAM-CL-TR-941, 2019. DOI: 10.48456/tr-941. [cl.cam.ac.uk source](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-941.html) **Relationship:** Adjacent capability architecture demonstrating unforgeable hardware authority and compartmentalization.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

### Ableman corpus

**[A1]** Adam Ableman. *Constitutional Robotics*. Ableman Corpus current edition; work identity `PAPER.PUB.18750683`;  
source SHA-256  
`D10DF9B6B7F742D9EEABF01BC5DFC3755BB4EBF548E8CB5F215BB9D94678F514`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *A Constitutional Syscall Architecture for Cyber-Physical Control Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F46D86D479F89BAC`;  
source SHA-256  
`5E696B753A10BD3C3D36B675A84B95CCF2234F024A6B277BF121E76BFCBCBD18`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Constitutional Syscalls*. Ableman Corpus current edition; work identity `PAPER.PUB.18737229`;  
source SHA-256  
`5F14356180812262778F8574C292F4F6B560993042E5358B02EAB9CF0F7DE14C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

The source manuscript names works by Adam Ableman concerning Constitutional Governance, Constitutional Computation, UGK, Dynatology, Constitutional Collective with Optional Overmind, Cryptographic Admissibility and Jurisdiction, and CARA, together with works attributed to Douglass North, Elinor Ostrom, Langdon Winner, Lawrence Lessig, Herbert Simon, Stafford Beer, and W. Ross Ashby. No external citation, edition, quotation, or claim-to-source binding was verified in this pass. The CARA reference is preserved only as source bibliography and was not used for Ableman semantic integration. Further evidentiary strengthening requires an authorized primary-source bibliography audit.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Cryptographic Admissibility and Jurisdiction.* Zenodo, 2026. doi:10.5281/zenodo.20602448

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847621](https://doi.org/10.5281/zenodo.23847621)
