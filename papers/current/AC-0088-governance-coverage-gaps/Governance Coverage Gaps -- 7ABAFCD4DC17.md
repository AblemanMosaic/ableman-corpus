# Governance Coverage Gaps

## Diagnosing Missing Scope, Participation, Discovery, Exception, and Evidence at Capability Boundaries

### An exception removes an obligation only when an authorized, bounded, reviewable rule says so.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

A system can correctly apply every rule it knows about and still exercise capability that no rule governs. This paper develops **Governance Coverage Gaps (GCG)** as a diagnostic framework for that failure. Receipt-bound execution can justify an evaluated action; it cannot by itself establish that every relevant capability was discovered, declared, assigned applicable governance, mediated at grant, observed in use, or represented in the receipt.

The framework distinguishes five gap classes: scope-definition, governance-participation, capability-discovery, exception-authority, and evidence gaps. This expansion preserves the source paper's central distinction between governance that exists but fails to participate and governance that was never defined, while making explicit the independent observation needed to discover undeclared capability. It also corrects an important limit: documented non-participation is not automatically intentional or acceptable. An exception removes an obligation only when an authorized, bounded, reviewable rule says so.

Governance coverage is formalized as a relation among a bounded capability inventory, applicability rules, required governance layers, evidenced participation, authorized exceptions, and an observation regime. "Full coverage" is therefore never an unqualified claim about all possible capability. It is a closure claim relative to a declared system boundary, discovery method, time interval, threat model, and evidence standard.

Integrated with Admissibility Engineering, the Three Hash Rule, the Constitutional Observability Platform, Reasoning by Way of Receipts, Constitutional Computing, Governed Agentic Coding, GMB, and the universal GSM, GCG becomes a method for locating where constitutional machinery is absent rather than merely malfunctioning. This paper supplies a specification and evaluation program, not proof that any implementation has achieved complete governance.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/governance-`

`coverage-gaps/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`9566E16E4D8CC59667C4BFA202358096B3D02C3A1F0D82E36DB51F3D6C127842`. The source remains unchanged.

The central problem, two-path diagnosis, N-determination, capability-grant boundary, receipt limitation, system postures, and examples are author material. The expanded taxonomy, formal model, independent discovery method, exception rule, corpus bridges, tests, counterevidence, and editorial alternatives are AI-assisted contributions explicitly distinguished from the original author material. No external research was conducted.

## 1. The Missing Question

Admissibility and receipts answer consequential questions: Was this operation permitted? Under what authority? Which constraints applied? What result and evidence were produced?

Governance coverage asks an earlier and wider question:

> Was the capability surface itself discovered and bound to governance before capability was granted or exercised?

A system can return a valid receipt for every operation that enters its governed pathway while retaining an unreceipted escape path. It can also govern every declared plugin operation while failing to govern installation code, configuration expansion, repair tooling, administrator bypass, or a lower hardware interface.

The absence is structural. It cannot be repaired merely by making the existing gate stricter.

## 2. Five Independent Gap Classes

The source's two paths should be retained and made more precise.

1. **Scope-definition gap:** a discovered capability has no applicable governance contract.
2. **Participation gap:** applicable governance exists, but one or more required layers do not participate in grant or execution.
3. **Capability-discovery gap:** the inventory or observation regime fails to expose a capability that the system can grant or exercise.
4. **Exception-authority gap:** non-participation is documented but not authorized, bounded, expiring, reviewable, or evidenced.
5. **Evidence gap:** governance may have participated, but available evidence cannot establish coverage or noncoverage.

The first two correspond to pre-governance absence and governance failure. The third explains how the first can be found. The fourth prevents documentation from laundering an omission into legitimacy. The fifth prevents lack of evidence from becoming evidence of coverage.

The classes may coexist. An undeclared repair interface can be both undiscovered and outside scope; after discovery it may acquire a scope rule yet remain unmediated; an authorized emergency exception may still have inadequate evidence.

## 3. Capability-Grant Boundaries

A **capability-grant boundary** is a transition at which an actor, component, process, model, plugin, configuration, or lower layer acquires the practical ability to produce an effect. Grant and invocation are distinct. Governance that begins only at invocation may be too late if installation, loading, discovery, or initialization already created effects.

Boundary candidates include:

- package build and installation hooks;
- plugin discovery, loading, and activation;
- configuration evaluation and template expansion;
- model tool grants and agent delegation;
- credentials, handles, file descriptors, and network routes;
- repair, recovery, migration, import, and administrative paths;
- driver and hardware abstraction escape surfaces; and
- composed capabilities whose combination creates authority absent from each component.

The boundary is not necessarily one code location. In distributed systems it may span declarations, brokers, policy engines, transport, runtime, and external providers. Coverage analysis must follow the full grant chain.

## 4. A Bounded Formal Model

For a system boundary $S$, interval $T$, and observation regime $O$, let:

- $C_{decl}$ be declared capabilities;
- $C_{disc}$ be capabilities discovered by methods independent of governance declarations;
- $C_{obs}$ be capabilities observed as granted or exercised;
- $N(c)$ be the governance layers normatively required for capability $c$;
- $P(c)$ be the layers evidenced as participating;
- $X(c)$ be authorized exceptions; and
- $E(c)$ be the evidence supporting discovery, applicability, participation, and exception claims.

The bounded inventory is:

$$
C^*=C_{decl}\cup C_{disc}\cup C_{obs}.
$$

For each $c\in C^*$, the unfulfilled governance set is:

$$
G(c)=N(c)\setminus\left(P(c)\cup X(c)\right).
$$

This equation is valid only when $N$, $P$, and $X$ are well-defined and adequately evidenced. Otherwise the verdict is indeterminate.

A scope-definition gap exists when $c\in C_{disc}\cup C_{obs}$ but $N(c)$ is undefined. A participation gap exists when $N(c)$ is defined and $G(c)\ne\varnothing$. A discovery gap is inferred only when a later or independent observation exposes capability omitted by the declared discovery procedure; an evaluator cannot enumerate unknown unknowns directly.

No universal scalar "degree of governance" follows without a weighting model. A set-valued coverage profile is safer because one missing high-impact capability may matter more than hundreds of covered low-impact operations.

## 5. N-Determination

The source names the selection of applicable governance layers **N-determination**. This is not simply a count. It is a function from a capability and context to required obligations:

$$
N(c,k)=\{g_1,\ldots,g_n\}.
$$

Context $k$ may include actor, authority, data class, jurisdiction, resource, effect type, environment, time, delegation chain, and risk posture. N-determination needs an authoritative normative source independent of observed participation. Otherwise a system could define its requirements to match what happened and report perfect coverage.

Under-declaration omits an applicable layer. Over-declaration adds irrelevant layers, which can create delay, cost, contradiction, or inaccessible governance. Ambiguity leaves applicability unresolved. All three are diagnostic outcomes; only the first is necessarily a coverage deficit.

## 6. Discovery Cannot Be Derived from Declaration Alone

Comparing declared layers with evidenced participation is necessary but insufficient. It detects missing participants only for capabilities already inside the evaluator's inventory. Pre-governance absence requires an independent discovery channel.

Candidate discovery methods include:

- static enumeration of entry points, permissions, imports, hooks, and effectful APIs;
- runtime tracing across grant and invocation boundaries;
- package, plugin, service, credential, device, and network inventories;
- differential execution under changed policy or denied capability;
- threat modeling and adversarial path exploration;
- dependency and supply-chain analysis;
- interface-to-implementation correspondence checks; and
- reconciliation of intended, declared, observed, and externally available capabilities.

Each method has blind spots. Coverage claims must name which methods ran, what they could observe, what interval they covered, and which paths remained inaccessible. The correct verdict for insufficient observation is **indeterminate**, not full coverage.

## 7. Receipts and Coverage Evidence

Receipts justify what their capture boundary includes. They do not automatically prove that the boundary is complete.

For coverage analysis, a receipt or linked evidence package should bind:

- system boundary and version;
- capability inventory and discovery method;
- actor and authority;
- requested, granted, exercised, and denied capabilities;
- applicable governance set $N(c)$;
- evidenced participants $P(c)$;
- exceptions $X(c)$ with grantor, scope, reason, expiry, and review condition;
- unobserved or inaccessible surfaces;
- result and effect evidence;
- verdict and claim ceiling; and
- revision or remediation link.

The Three Hash Rule can bind intent, artifact, and result, but coverage analysis must also show that the governed artifact and result encompass the relevant capability path. Reasoning by Way of Receipts supplies a mode of inference from such records; it cannot infer unrecorded participation as fact.

## 8. Exceptions and Intentional Partial Governance

The source proposes that documented non-participation is intentional partial governance rather than a gap. Documentation alone is insufficient. A valid exception must be:

- granted by an authority entitled to relax the obligation;
- limited to named capabilities, actors, environments, and effects;
- justified and reviewable;
- time-bound or revision-bound where appropriate;
- visible to dependent decisions;
- unable to silently expand through composition; and
- accompanied by compensating controls or an explicit accepted residual risk.

An exception may make non-participation authorized. It does not make the underlying exposure disappear. Reports should distinguish **covered**, **authorized exception**, **uncovered**, and **indeterminate**.

## 9. Coverage Verdicts and Claim Ceilings

For each capability, the basic verdicts are:

| Verdict | Meaning |
| --- | --- |
| Covered | Required layers participated, with sufficient evidence. |
| Authorized exception | A valid exception displaces named obligations within its bounds. |
| Uncovered | Required participation or scope definition is missing. |
| Indeterminate | Discovery, applicability, participation, or exception evidence is insufficient. |

A system-level statement should aggregate these without hiding severe outliers. "Full coverage" should be written as:

> No uncovered capability was found within boundary $S$, interval $T$, inventory $C^*$, discovery regime $O$, applicability law $N$, and evidence threshold $Q$.

This is a defeasible closure claim, not proof that no unknown capability exists. New evidence reopens it.

## 10. Corpus Integration

**Admissibility Engineering** supplies the machinery for deciding whether a proposed action may proceed. GCG asks whether every relevant capability path reaches that machinery. **The Constitutional Observability Platform** supplies observation and evidence surfaces; GCG states what those surfaces must cover. **The Three Hash Rule** and **Reasoning by Way of Receipts** bind intent, artifact, result, and inference, while GCG tests whether the receipt boundary omits an effect path.

**Constitutional Computing** provides the larger account of inspectable, renegotiable authority across the stack. **Governed Agentic Coding** makes the problem concrete for agents, tools, dependencies, delegation, and software effects. The **Governed Meaning Base (GMB)** can retain capability identities, applicability rules, exceptions, evidence, conflicts, and revisions. The universal **GSM** can type relations among capability, actor, authority, governor, effect, evidence, and gap.

These are complementary roles, not identity mergers. GCG is the diagnostic bridge between capability discovery and governed effect closure.

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

- **Possibility:** enumerate capabilities, grant paths, governance layers, exceptions, observers, and failure classes.
- **Specification:** define the system boundary, $C^*$, $N$, $P$, $X$, evidence requirements, and verdict semantics.
- **CM1:** retain admissible diagnostic configurations, including broad, costly, weak, or undesirable ones.
- **CM2:** prefer configurations that maximize consequential discovery and mediation while controlling cost, latency, privacy, accessibility, and governance burden.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for one system, threat model, interval, and authority regime. The expansions are interchangeable.
- **IR:** produce an **Instance Realization** or **Implementation Realization** such as an inventory compiler, grant mediator, observer, gap analyzer, receipt schema, or dashboard. The expansions are interchangeable.
- **Evidence:** run discovery, bypass, differential, receipt-completeness, exception, and replay tests.
- **Revision:** close, accept, narrow, or reclassify gaps and update discovery after new capability appears.

This paper reaches Specification and proposes CM1/CM2 criteria. It does not select an IC, implement an IR, or demonstrate empirical coverage.

## 12. Evaluation Program

A coverage campaign should test:

1. inventory recall against independently discovered capability;
2. declaration-to-runtime correspondence;
3. applicability accuracy for $N(c,k)$;
4. participation evidence for each required layer;
5. bypass resistance at grant, load, invocation, repair, and administration paths;
6. composed-capability escalation;
7. exception authority, scope, expiry, and visibility;
8. receipt completeness across the effect path;
9. false covered and false uncovered verdicts; and
10. detection latency after a new capability or path appears.

Results should be reported per boundary and effect class, not compressed into one reassuring percentage.

## Capability-Surface Closure Diagnostic

Across the completed P1 corpus, Governance Coverage Gaps is the **capability-surface closure diagnostic that asks whether every consequence-bearing grant and effect path discovered within a bounded system reaches the required governance, evidence, exception, and revision machinery**. It complements action-level admissibility by testing whether relevant actions can escape the action-level gate entirely.

- **Adjacent work:** *Admissibility Engineering*  
  **Supplies:** Constraint binding and counterexample search across enumerated realization pathways.  
  **GCG boundary:** GCG discovers capabilities and grant paths that were omitted from the declared governance surface.

- **Adjacent work:** *Agentic Interface Surfaces*  
  **Supplies:** Action, effect, evidence, feedback, and recognition surfaces for agents.  
  **GCG boundary:** GCG tests whether hidden tools, adapters, credentials, retries, and lower paths bypass those surfaces.

- **Adjacent work:** *The Constitutional Observability Platform*  
  **Supplies:** Role-aware evidence and operational-state projection.  
  **GCG boundary:** The platform supplies observations; GCG evaluates their coverage and unknowns.

- **Adjacent work:** *Jnana II: Constitutional Transformation Substrate*  
  **Supplies:** Transformation, capability, effect, and receipt planes.  
  **GCG boundary:** GCG sets the claim ceiling for Jnana mediation and containment.

- **Adjacent work:** *Constitutionally Governed Infrastructure*  
  **Supplies:** Continuation-control mechanisms such as schedulers, routers, and administrative paths.  
  **GCG boundary:** GCG tests whether their configuration and effects are within declared scope.

A coverage campaign should bind:

$$
\begin{aligned}
G= (&boundary, interval, threat\_model, \\
&declared\_capabilities, independent\_discovery, \\
&observed\_capabilities, grant\_paths, required\_layers, \\
&participating\_layers, exceptions, evidence, verdicts, \\
&unknowns)
\end{aligned}.
$$

Coverage analysis begins at capability acquisition, not only invocation. Installation, configuration expansion, loading, delegation, credential delivery, repair, migration, administration, retries, fallbacks, and composed capabilities may create practical authority before the named operation is called.

The diagnostic should report each capability as `COVERED`, `AUTHORIZED_EXCEPTION`,  
`UNCOVERED_SCOPE`, `UNCOVERED_PARTICIPATION`, `UNDISCOVERED_UNTIL_COUNTEREVIDENCE`,  
`EVIDENCE_INSUFFICIENT`,  
or   
`OUTSIDE_DECLARED_BOUNDARY`. A system-level closure claim is valid only relative to the boundary, interval, inventory, discovery regime, applicability law, effect classes, and evidence threshold; any new path reopens it.

The universal GSM can type   
`DISCOVERS_CAPABILITY_INDEPENDENTLY`,  
`GRANTS_CAPABILITY_AT_BOUNDARY`, `REQUIRES_GOVERNANCE_LAYER`, `PARTICIPATES_IN_GRANT`,  
`AUTHORIZES_BOUNDED_EXCEPTION`, `ESCAPES_GOVERNANCE_SCOPE`, `COMPOSES_HIGHER_CAPABILITY`,  
`LACKS_COVERAGE_EVIDENCE`, `REOPENS_CLOSURE_CLAIM`,  
and   
`REMEDIATES_WITHOUT_PROVING_COMPLETENESS`. These relations make the diagnostic actionable and defeasible.

This integration establishes four editorial commitments: retain GCG as the capability-surface closure diagnostic; adopt the full campaign envelope and seven-valued capability verdict; require independent discovery at grant, load, repair, and composed-capability boundaries; and make every full-coverage statement explicitly bounded, reopenable, and incapable of proving unknown-path absence.

## Semantic and Capability Dual Closure

The fixed-seed comparison with enforcement mechanics, the Identity Spine Doctrine, Ontology Laundering, and receipt reasoning shows that coverage has two coupled but distinct surfaces:

$$
\begin{aligned}
C= (&capability\_paths, semantic\_bindings, \\
&identity\_propagation, mediators, effects, evidence, \\
&unknowns, reopen\_triggers)
\end{aligned}.
$$

Enforcement mechanics can mediate declared capabilities while stale or unpropagated identities cause the rule to govern the wrong semantic subject. Identity Spine transitions can update the central registry while caches, indexes, prompts, compiled projections, provider stores, and external integrations retain old bindings. Both conditions defeat a broad closure claim.

Ontology Laundering supplies an adversarial semantic-change diagnostic. A new meaning may enter through an uncovered configuration, migration, model update, translation, proxy, or administrative path without passing the positive identity and admission protocol. Discovery of such a path establishes a coverage gap, not deliberate laundering; classification still requires its own evidence and alternatives.

Receipts record inventories, discoveries, decisions, remediation, and bounded closure verdicts. Receipt completeness cannot prove unknown-path absence, and a hash-complete archive can still omit an entire capability or semantic propagation surface.

The universal GSM can type   
`COVERS_CAPABILITY_AND_SEMANTIC_BINDING`,  
`DISCOVERS_STALE_IDENTITY_PATH`, `ESCAPES_SEMANTIC_PROPAGATION`,  
`INTRODUCES_ONTOLOGY_CHANGE_OUTSIDE_GATE`, `RECEIPTS_BOUNDED_COVERAGE`,  
and   
`REOPENS_DUAL_CLOSURE_ON_COUNTEREVIDENCE`.

This randomized review establishes four editorial commitments: adopt dual capability/semantic closure; include identity propagation in coverage campaigns; route uncovered semantic change to a separate laundering classification; and prohibit receipt completeness from proving unknown-path absence.

## A Multiplane, Reopenable Coverage Court

Nineteen downstream uses extend Governance Coverage Gaps beyond one capability inventory while preserving one stable diagnostic. The paper is used to test capability acquisition and invocation, concrete effect routes, semantic and ontology propagation, identity migration, observation and evidence paths, standards execution bindings, infrastructure continuation control, and the completeness ceiling of receipts, lineage, enforcement, and conformance claims.

The recurrent campaign object is:

$$
\begin{aligned}
C^*= (&subject\_generation, claim, jurisdiction, planes, \\
&inventories, routes, grants, mediators, observers, \\
&discovery\_methods, independence, exceptions, unknowns, \\
&counterexamples, coverage\_interval, reopen\_triggers, \\
&verdict, evidence, remainder)
\end{aligned}.
$$

`planes` should be a typed vector rather than one scalar: authority, capability grant, invocation, semantic propagation, identity, external effect, observation, evidence, challenge, and remedy may have different coverage. A path can cross an action gate while escaping the identity spine, receipt store, observer, appeal process, or successor propagation. Conversely, an unobserved region is not automatically an uncovered harmful capability; it may be absent, inaccessible, out of jurisdiction, or still unknown.

Coverage is always relative to an exact subject generation, discovery profile, environment, jurisdiction, and interval. New plugins, credentials, caches, prompts, providers, build hooks, routes, model behavior, or counterexamples reopen the verdict. Conformance, a complete-looking receipt chain, successful migration, a signed commitment, or a green enforcement court cannot raise that bounded result to universal closure.

Two broader lexical hits remain rejected: generic "coverage gaps" in the model-first migration evidence list and generic "receipt coverage gaps" in the quantitative-insights paper do not establish a dependency on this framework.

The universal GSM can type   
`TESTS_COVERAGE_PLANE`, `DISCOVERS_UNMEDIATED_ROUTE`,  
`BOUNDS_COVERAGE_TO_GENERATION`, `DECLARES_DISCOVERY_INDEPENDENCE`,  
`REOPENS_ON_CAPABILITY_CHANGE`, `DISTINGUISHES_UNKNOWN_FROM_UNCOVERED`,  
`LIMITS_CONFORMANCE_CLAIM`, and   
`RETAINS_COVERAGE_REMAINDER`.

This reverse-dependency review establishes four editorial commitments: adopt the multiplane coverage vector; bind every verdict to subject, method, environment, and interval; require explicit reopening triggers and unknown states; and prohibit receipts, commitments, conformance, or enforcement success from implying universal closure.

## 13. Counterevidence and Failure Modes

The framework should be narrowed or rejected where: (1) the capability inventory is derived only from declarations; (2) unknown capability is treated as nonexistent; (3) observation covers invocation but not grant or load; (4) $N$ is chosen after observing participation; (5) a documented omission is treated as authorized without a valid exception; (6) an exception has no expiry or review condition; (7) composition creates unmodeled capability; (8) administrator, repair, migration, or recovery paths bypass mediation; (9) hardware or provider effects exceed the abstraction; (10) receipts omit a material effect; (11) receipts record only successful paths; (12) failed and partial operations leave state; (13) the observer can be bypassed or tampered with; (14) the observation regime changes behavior materially; (15) privacy or safety limits make observation incomplete; (16) over-governance creates denial of service or inaccessible operation; (17) one scalar score hides a severe uncovered capability; (18) temporal capability appears outside the sampled interval; (19) capability identity changes across versions; (20) authority to define scope is itself ungoverned; (21) evidence exists but is not bound to the evaluated instance; (22) absence of a record is treated as proof of absence; (23) intentional partial governance is confused with no residual risk; (24) institutional analogies ignore legal or social context; (25) claims of empirical clustering lack a sample and method; (26) an implementation passes its own fixtures but lacks adversarial discovery; (27) GMB inclusion is treated as coverage proof; (28) a declared contract cannot constrain the lower realization; (29) remediation closes one path while opening another; or (30) "complete governance" is asserted without a bounded claim ceiling.

## Coverage Is a Bounded Search Result, Not a Declaration of Completeness

### Public orientation

Governance Coverage Gaps asks how a system can discover capabilities and effect paths that its own rules never declared. It separates grant, invocation, mediation, observation, evidence, challenge, and remedy, then binds any coverage verdict to an exact subject generation, environment, method, jurisdiction, and interval. The framework makes closure claims more honest; it does not prove that every path has been found.

### Adversarial tests

1. **Inventory-circularity attack.** Required governance is derived from the same declaration being evaluated, so undeclared capabilities cannot appear as missing.
2. **Unknown-as-absent attack.** Inaccessible, unobserved, or undiscovered regions are counted as nonexistent rather than indeterminate.
3. **Temporal-escape attack.** A capability appears only during repair, migration, failure, update, expiry, race, or an unsampled interval.
4. **Composition-escape attack.** Two governed modules compose into a new capability, authority path, or external effect absent from either inventory.
5. **Observer-bypass attack.** The mechanism that emits evidence can be bypassed, disabled, tampered with, or shares the subject's compromised root.
6. **Receipt-closure attack.** Complete-looking records are treated as proof that unrecorded routes do not exist.
7. **Over-governance attack.** Excess layers, monitoring, or review create denial of service, privacy harm, inaccessible operation, or incentives to bypass governance.
8. **Remediation-regression attack.** Closing a path opens another route or changes identity, policy, dependencies, or observation without reopening the verdict.

### Claim and evidence ceiling

The paper supplies a multiplane, reopenable coverage diagnostic and a four-way verdict: covered, authorized exception, uncovered, or indeterminate. It does not establish universal closure, complete capability discovery, security, compliance, legitimacy, or absence from missing evidence. Coverage remains relative to the exact subject and discovery campaign.

Any concrete security, access-control, software-supply-chain, institutional, or empirical-clustering claim requires external literature, an independently justified normative inventory, adversarial discovery methods, exact observation boundaries, and reproducible evidence. No external research was added in this pass.

### Reader-facing consequence

The key public question is not only whether rules worked on the actions they saw. It is how the system looked for powers, paths, and effects its rules did not know to name - and what remains unknown after that search.

## 15. Conclusion

Governance failure is not limited to rules that malfunction. Capability can escape because governance was never defined, because required layers did not participate, because the capability was never discovered, because an exception lacked authority, or because evidence cannot establish what happened.

The decisive shift is from asking only why an evaluated action was allowed to asking how the system knows which capabilities existed, which governance applied, where capability was granted, which paths were observed, and what remains outside the claim boundary.

GCG does not prove complete governance. It supplies the architecture for making coverage claims bounded, falsifiable, receipted, and revisable. That is the defensible transition from justified execution toward governed capability closure.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires an authorized review of capability-security literature, access-control and policy-coverage methods, runtime and supply-chain observability, plugin and build-system boundary studies, and any institutional comparison. The source's claim of empirical clustering should remain a hypothesis unless a sample, method, and results are supplied.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that a system can correctly apply every rule it knows about and still exercise capability that no rule governs. Its nearest external comparison fields are governance, provenance, security. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E2]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E3]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E6]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E7]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

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

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

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

DOI: [10.5281/zenodo.23847861](https://doi.org/10.5281/zenodo.23847861)
