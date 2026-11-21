# Warrant by Structure

## How Architecture Can Carry Bounded Justification

### Authority, Receipts, Lowerability, and the Conditions of Structurally Mediated Effects

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Software systems produce effects under mixtures of declared capability, ambient privilege, runtime convention, external dependency, human discretion, and post hoc audit. **Warrant by structure** asks whether an effect was produced through an explicit, authority-bound, rule-evaluated, receipt-producing path whose mediation boundary can itself be tested.

The source manuscript reports a 30-system study and contrasts it with a proposed Veritas Task Engine (VTE). The supplied corpus does not contain the system list, coding guide, raw annotations, denominators, executable VTE artifact, evaluation output, or replication package needed to verify those results. One comparison cell is internally inconsistent: a reduction of 55.2 percentage points from 71.9% implies 16.7%, not approximately 0%. The empirical numbers are therefore retained here as source-reported claims requiring reconstruction, not as established findings.

The durable conceptual contribution is a testable distinction between post hoc description and structurally mediated execution. That distinction requires tighter boundaries than the source supplies. A receipt can bind what a system claims occurred; it does not by itself prove legitimate authority, correct rule evaluation, physical effect, absence of bypass, or complete governance closure. Structural warrant is strongest when authorization, mediation, effect observation, custody, and independent verification are separately represented and jointly bounded.

This revision formalizes those obligations, repairs the arithmetic presentation, defines the proposed metrics, integrates adjacent corpus machinery, supplies a warrant-strength ladder and adversarial tests, and locates the work in the universal GSM and realization funnel. No external research or implementation occurred.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/warrant-by-`

`structure/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`5A623EDA987D8E3F3EDA1D658CE3346FC2C21C810DA9DA381412C8122F40FEEA`. The exact source remains unchanged.

The central concept, study report, VTE proposal, measurement categories, comparative framing, and voice are author material. The formal model, empirical downgrade, repaired metric definitions, proof ladder, integration surfaces, countertests, and decisions are AI editorial or synthetic contributions until adopted.

No supplied evidence proves that the 30-system sample was selected or coded as described, that VTE was implemented, or that its reported properties were observed. No empirical, novelty, security, proof, conformance, canonical, implementation, or publication standing is granted.

## 1. The Bounded Thesis

The source shifts attention from whether a proposition is justified to whether an event could occur only through an admissible structure. The useful claim is narrower:

> Within a declared system boundary, an event has structural warrant to the extent that its authority, decision path, effect, receipt, lineage, and mediation completeness are independently inspectable and resistant to bypass.

This is **mechanism-first justification**, not justification without propositions. Authority declarations, rule predicates, decisions, receipt fields, evidence claims, and boundary statements are all proposition-bearing. The structural contribution is that those claims are tied to executable mediation rather than left only in narrative documentation.

Structural warrant also does not imply moral, legal, or institutional legitimacy. An explicit capability rooted in illegitimate authority may be structurally well mediated and still normatively unwarranted. This is where Authority Laundering Theory constrains the paper: machinery cannot convert a defective root into legitimate authority merely by making it explicit.

## 2. Primitives and Distinctions

**Authority root.** The source from which permission or constraint is claimed.

**Warrant.** A scoped, active authorization connecting a principal, capability, target, jurisdiction, and effect class.

**Capability.** A declared action surface with typed inputs, effects, limits, and refusal conditions.

**Proposal.** A candidate transition that has not yet been admitted or realized.

**Gate.** A rule-evaluation mechanism returning a typed decision.

**Effect.** A change in the governed abstract state or an observed external system.

**Receipt.** A durable binding among identities, authority, proposal, decision, attempted or observed effect, evidence, predecessor, successor, and claim boundary.

**Lineage.** The predecessor and dependency relations required to reconstruct the governed claim.

**Lowerability.** The degree to which an operative source of discretion can be represented as an explicit, inspectable, enforceable object without hiding residual discretion elsewhere.

**Mediation closure.** Evidence, within a stated boundary and threat model, that every relevant effect path is routed through the declared gate and that bypass paths are absent, blocked, or explicitly excluded.

**Intrinsic receipt production.** Receipt creation coupled to the transition protocol rather than reconstructed later. This is weaker than intrinsic justification unless the receipt and effect are atomic and independently verifiable.

## 3. Formal Structural-Warrant Candidate

Let $x$ be a predecessor state, $p$ a proposal, $q$ a principal, $w$ a warrant, $\ell$ an active rule set, $d$ a decision, $x'$ a claimed successor, and $r$ a receipt. A locally mediated transition may be represented as:

$$
d=G(p,q,w,\ell),
$$

$$
x'=T(x,p)\quad\text{only if}\quad d=\mathrm{ALLOW},
$$

$$
r=B(x,p,q,w,\ell,d,x',e,v),
$$

where $e$ is effect evidence and $v$ identifies the verifier and its criteria.

A candidate structural-warrant judgment is:

$$
\begin{aligned}
&W_S(x\rightarrow x'\mid J,\Theta)= \mathrm{Auth} \\
&\land \mathrm{Gate} \\
&\land \mathrm{Bind} \\
&\land \mathrm{Observe} \\
&\land \mathrm{Closure}
\end{aligned},
$$

under jurisdiction $J$ and threat model $\Theta$. Each conjunct requires separate evidence:

- **Auth:** the warrant is valid for the principal, target, capability, jurisdiction, and time;
- **Gate:** the declared rule set actually evaluated the proposal;
- **Bind:** the receipt identifies the relevant predecessor, proposal, decision, and claimed successor;
- **Observe:** evidence supports the claimed effect rather than merely the attempted command;
- **Closure:** relevant bypass paths are excluded or bounded under $\Theta$.

The receipt may carry evidence for these predicates, but it cannot establish all of them merely by existing. A system that signs false receipt fields, executes before durable recording, or permits administrator bypass fails one or more conjuncts even if its schema is perfect.

## 4. Warrant-Strength Ladder

Structural warrant is more useful as a graded claim than a binary label:

- **Grade:** W0 Observed  
  **Minimum structure:** an effect or state is seen  
  **What remains unproved:** attribution, authority, mediation

- **Grade:** W1 Attributed  
  **Minimum structure:** logs or records bind an actor and event  
  **What remains unproved:** valid warrant and complete gate participation

- **Grade:** W2 Admitted  
  **Minimum structure:** explicit warrant and gate decision are receipted  
  **What remains unproved:** realized effect and absence of bypass

- **Grade:** W3 Effect-bound  
  **Minimum structure:** independent evidence binds the realized effect to the admitted proposal  
  **What remains unproved:** complete mediation closure

- **Grade:** W4 Closure-qualified  
  **Minimum structure:** bypass and effect-atomicity tests support closure within a named boundary and threat model  
  **What remains unproved:** claims outside that boundary or future correctness

These grades are AI editorial candidates. They prevent "structured receipt" from being treated as a universal proof state.

## 5. Reconstructable Measurement Protocol

The source's five metrics require denominators and coding rules.

For identified authority instances $A$:

$$
L=\frac{|A_{\mathrm{lowerable}}|}{|A|},\qquad
I=\frac{|A_{\mathrm{implicit}}|}{|A|}.
$$

$L+I=1$ only if the categories are declared exhaustive and disjoint. Partial, disputed, external, and unknown cases otherwise require separate classes.

For observed effect classes $E$ and declared capabilities $C$:

$$
R_S=\frac{|E_{\mathrm{schema\text{-}valid\ receipt}}|}{|E|},
$$

$$
C_D=\frac{|E_{\mathrm{capability\text{-}declared}}|}{|E|},
$$

$$
R_F=\frac{|E_{\mathrm{typed\ refusal}}|}{|E_{\mathrm{refused}}|},
$$

and a closure-facing metric is:

$$
M_C=\frac{|E_{\mathrm{tested\ mediated}}|}{|E_{\mathrm{relevant}}|}.
$$

Counting "capabilities per authority" may describe representation density but does not measure coverage unless the possible effect surface is also enumerated. Each metric needs a sampling unit, observation window, coding manual, ambiguity policy, inter-rater reliability, missing-data rule, and exact source evidence.

## 6. Status of the Reported Study

The source reports 221 authorities across 30 production systems, 71.9% implicit authority, 28.1% lowerable authority, 0% structured receipts, 64.2% absent receipts, and capability density of 0.072. It reports VTE as 83.3% lowerable, 100% structured receipts, and capability density of 1.333.

Those figures are not reproducible from the supplied corpus. The source does not name the 30 systems, provide authority-level rows, define receipt observations, expose VTE code, or supply test results. They must remain **source-reported unverified findings**.

The comparison table also requires repair. If VTE lowerable authority is 83.3% and lowerable versus implicit are complementary, VTE implicit authority is 16.7%; $71.9-16.7=55.2$ percentage points. The source's approximately 0% cell is inconsistent with its own delta. The ratio $1.333/0.072$ is approximately 18.5 using displayed values, so the reported 18.4 ratio may depend on undisclosed unrounded counts.

Before empirical publication, the study needs:

1. a frozen system list and selection rule;
2. per-system versions and observation dates;
3. operational definitions and coding examples;
4. authority, capability, effect, receipt, and refusal rows;
5. adjudication and inter-rater procedures;
6. raw-count derivations for every percentage and ratio;
7. VTE source, build instructions, tests, and effect traces;
8. bypass, failure, and receipt-atomicity tests; and
9. a reproducible analysis script and result manifest.

Until then, VTE is a **constructive design candidate**, not a demonstrated constructive witness.

## 7. Receipts, Proof, and Effect Atomicity

Reasoning by Way of Receipts supplies the core intuition that justification should be bound into execution. Warrant by Structure sharpens the infrastructure question: what mechanism makes the binding unavoidable?

The answer cannot be "a receipt was emitted." At least three artifacts may be required:

- an **admission receipt** showing what the gate evaluated and decided;
- an **effect receipt** or observation showing what the external boundary reports happened; and
- a **verification or promotion receipt** stating which predicates were checked and what standing follows.

The Three Hash Rule can bind predecessor, governed work or proposal, and successor/result identities. Work Custody can preserve who or what holds the work and its lineage. Constitutional Observability can expose claims, evidence, and standing. The Mechanics of Constitutional Enforcement supplies the effect-mediation boundary. None is individually identical with legitimate authority or proof.

If an effect can occur and receipt creation can fail, the system must represent the partial outcome rather than claim atomic justification. If the receipt is written before the effect, it proves only admission or intent. If written after the effect, recovery must distinguish unknown, failed, duplicated, and committed outcomes. Structural warrant therefore depends on explicit effect-atomicity and recovery semantics.

## 8. External Dependencies and Jurisdictions

Naming an external dependency is valuable, but naming does not lower or govern it. A cloud API, human institution, hardware controller, administrator, or social authority may remain outside the local enforcement boundary.

The system should distinguish:

1. local authority it can enforce;
2. imported authority it can authenticate but not originate;
3. external evidence it can verify only to a declared interface;
4. human or institutional discretion it can receipt but not compile away; and
5. unknown or unbounded dependencies that force a lower standing.

Structural warrant is thus jurisdiction-relative. A locally complete receipt chain can still terminate at an external boundary whose behavior remains testimony, attestation, or qualified evidence.

## 9. Universal GSM and Realization Funnel

The universal GSM can represent authority roots, warrants, principals, capabilities, proposals, gates, decisions, effects, receipts, evidence, verifiers, lineages, jurisdictions, bypass paths, standing, and revision without collapsing them into a single "proof" object.

The **Governed Meaning Base (GMB)** is the current name in the `CCF -> CMB -> GMB` lineage. It can preserve the study rows, definitions, receipts, evidence, and disputes; admission to GMB does not prove the claims. Warrant by Structure participates primarily in Computation and Coordination, with Intelligence and Possibility surfaces where agents interpret evidence or design new mediated regimes.

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

- **Possibility:** enumerate authority, mediation, receipt, and observability regimes.
- **Specification:** define primitives, warrant predicates, metrics, threat models, and claim boundaries.
- **Configuration Manifold 1 (CM1):** retain designs satisfying mandatory authority, mediation, effect, receipt, recovery, and bypass constraints.
- **Configuration Manifold 2 (CM2):** prefer among admissible designs by inspectability, performance, usability, sovereignty, repairability, and cost.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for one system and jurisdiction. The names are interchangeable.
- **IR:** construct an **Instance Realization** or **Implementation Realization** of that configuration. The names are interchangeable.
- **Evidence:** retain code, measurements, attacks, receipts, failures, and independent verification.
- **Revision:** repair the specification, implementation, measurement, or standing while preserving lineage.

The paper currently reaches Specification and proposes an empirical program. The supplied VTE description does not establish an IC, IR, implementation, or empirical witness.

## Structural Warrant as an Assurance Relation

The completed P1 corpus places Warrant by Structure as an **assurance relation** connecting a bounded claim to an inspectable authority and effect path. It is not an evidence artifact, a receipt format, an admissibility decision, or final standing.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed evidence artifacts and evaluation envelopes.  
  **Structural-warrant boundary:** Witnesses can support the relation; their existence does not create warrant.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Bounded records of decisions, transitions, refusals, and observations.  
  **Structural-warrant boundary:** Receipts preserve reasoning and events; they may reference witnesses without proving closure.

- **Adjacent work:** *Authority Laundering Theory*  
  **Supplies:** Tests whether attributed authority is normatively valid and causally effective.  
  **Structural-warrant boundary:** A mediated path with a defective authority root is structurally explicit but not legitimately warranted.

- **Adjacent work:** *Integrity Enforcement Layer*  
  **Supplies:** Decision-to-effect enforcement and protected refusal.  
  **Structural-warrant boundary:** IEL may realize mediation; an implementation still needs bypass and effect evidence.

- **Adjacent work:** *Legitimacy Without Self-Ratification*  
  **Supplies:** Independence constraints on a subject's strongest standing.  
  **Structural-warrant boundary:** Self-produced structural evidence cannot alone establish the highest assurance level.

The portable warrant object is:

$$
\begin{aligned}
W= (&claim, subject, authority, path, witnesses, receipts, \\
&effect\ evidence, bypass\ model, standing, ceiling)
\end{aligned}.
$$

The relation is strong only to the extent that the exact subject and effect are bound, authority is legitimate for the jurisdiction, mandatory transitions mediate every relevant path, observations bear on actual effects, and independent review is adequate to the standing claimed. Missing material yields a narrower posture, not a fabricated zero or pass.

This resolves a vocabulary collision. A **witness** is an evidence carrier. A **receipt** records a bounded event, inference, or decision. A **warrant** is the evaluated relation between a claim and its supporting authority/path/evidence. **Standing** is the current governed status assigned to the claim. None is interchangeable with truth or legitimacy.

The universal GSM can type `CLAIM_WARRANTED_BY`, `SUPPORTED_BY_WITNESS`,  
`RECORDED_BY_RECEIPT`, `MEDIATED_THROUGH`, `OBSERVED_EFFECT`, `BYPASSED_BY`, `REVIEWED_BY`,  
and `HAS_STANDING`. The model should permit conflicting warrants and counterwarrants without forcing one conclusion.

This integration establishes four editorial commitments: adopt assurance relation as the official corpus role; adopt the warrant object; adopt the four-object vocabulary separation; and decide whether the reported comparative study should become a separate empirical companion so the conceptual paper does not borrow its unverified standing.

## Domain-Typed Structural Warrant

The fixed-seed comparison with Sovereign Software, constitutional context compilation, Context-Compiled Consciousness Mode, and the Classified Earthworks System shows why structural warrant must remain domain-typed:

$$
\begin{aligned}
W^*= (&claim, domain, subject, authority, path, witnesses, \\
&proxy\_calibration, effect\_class, bypass\_model, \\
&counterwarrant, standing, ceiling, expiry)
\end{aligned}.
$$

A sovereignty claim requires actor-, capability-, closure-, threat-, and time-specific disruption or reconstruction evidence. A context claim requires source-to-projection witnesses and separate evidence for model use, behavior, and external effect. A reflective-context claim can be warranted functionally while phenomenality and moral-status claims remain unwarranted.

The earthworks brief concerns physical materials, contamination, water, deployment, and environmental outcomes. Its warrant would require field sampling, classification performance, process controls, material and site measurements, longitudinal observation, safety evidence, and relevant domain authority. Software receipts or context-court structure cannot substitute for physical-world evidence.

Counterwarrants and domain changes remain first-class. A claim warranted in one site, model, provider, population, or threat model may expire elsewhere. The universal GSM can type `WARRANTED_IN_DOMAIN`,  
`CALIBRATED_TO_PROXY_TARGET`, `SUPPORTED_BY_DISRUPTION_TEST`,  
`SUPPORTED_BY_CONTEXT_WITNESS`, `SUPPORTED_BY_FIELD_EVIDENCE`, `COUNTERWARRANTED_BY`,  
and   
`EXPIRES_OUTSIDE_SCOPE`.

This randomized review establishes four editorial commitments: adopt the domain-typed warrant object; require proxy calibration alongside path structure; separate functional reflective warrant from phenomenality; and require physical evidence for earthworks claims without importing software assurance standing.

## A Claim-Scoped Warrant Vector Across Domains

Thirteen downstream uses establish Warrant by Structure as a widely reused assurance relation. It bounds context claims, interface projections, authority-laundering findings, physical earthworks classifications, functional consciousness-mode claims, DAG theorems, legitimacy transitions, retrieval paths, receipt reasoning, software-sovereignty claims, anomaly experiments, boundary-accountability cases, and governed-change traces. The diversity is evidence for a common question set, not one universal proof standard.

The warrant object should be claim-scoped and vector-valued:

$$
\begin{aligned}
W^*= (&claim, subject, jurisdiction, authority\_root, \\
&decision\_path, mandatory\_mediation, effects, witnesses, \\
&independence, bypass, dependencies, receipts, standing, \\
&expiry, counterevidence, ceiling, remainder)
\end{aligned}.
$$

Report separate support for authority, mediation, effect observation, identity, custody, witness independence, bypass resistance, environmental closure, reconstruction, and current standing. A claim may be strongly warranted on one dimension and unsupported on another. Aggregation must preserve veto conditions and missing dimensions; a high score cannot compensate for an illegitimate authority root, unobserved effect, or open bypass where that property is required.

Warrant inherits the jurisdiction of the claim. Structural support for a DAG property does not warrant semantic correctness. A reproducible context compilation does not warrant phenomenality. Receipts do not warrant the effect they failed to observe. Laboratory classification does not warrant site performance. A provider-exit test does not warrant every sovereignty dimension. Structural warrant also cannot self-ratify legitimacy; antecedent authority and control independence remain separate.

Every warrant expires or reopens when its subject, authority, policy, topology, environment, dependencies, witness control domain, bypass surface, effect route, or evidence changes. Dependents should cite the exact warrant generation and property vector rather than the paper name alone.

The universal GSM can type   
`WARRANTS_CLAIM_DIMENSION`,  
`LACKS_REQUIRED_WARRANT_DIMENSION`, `INHERITS_CLAIM_JURISDICTION`,  
`DEPENDS_ON_WITNESS_CONTROL_DOMAIN`, `EXPIRES_ON_SUBJECT_CHANGE`, `REOPENS_ON_BYPASS`,  
and   
`WITHHOLDS_TRUTH_OR_LEGITIMACY_PROMOTION`.

This reverse-dependency review establishes four editorial commitments: adopt the claim-scoped warrant vector; prohibit compensatory scalar scoring across required dimensions; require exact generation, expiry, and reopening conditions; and preserve domain-specific truth, legitimacy, physical, phenomenal, and standing boundaries.

## 10. Counterevidence and Failure Modes

The thesis must narrow or fail where: (1) an unauthorized effect bypasses the gate; (2) an administrator or supply-chain path is omitted; (3) an explicit authority root is illegitimate; (4) a receipt claims predicates the gate never evaluated; (5) receipt and effect are not atomic; (6) an effect occurs while its receipt is lost; (7) a receipt precedes an effect that never occurs; (8) replay duplicates an effect; (9) recovery cannot distinguish unknown from failed; (10) a verifier shares the same defect as the producer; (11) structured logs provide equivalent evidence at lower cost; (12) the boundary excludes the dominant authority source; (13) external dependency naming is mistaken for control; (14) lowerability merely relocates discretion; (15) measurement categories overlap; (16) denominators differ between systems; (17) the sample selection favors systems with weak receipts; (18) runtime claims cannot be observed from public artifacts; (19) VTE cannot be built or tested; (20) VTE's receipt requirement prevents necessary recovery; (21) empirical values do not reproduce; (22) the regime-level threshold is undefined; (23) capability density does not predict coverage; (24) privacy or security costs exceed the declared benefit; or (25) a simpler capability-and-audit design performs equally well.

## Structure Can Carry Warrant Without Becoming Truth

### Public orientation

Warrant by Structure asks when the organization of a system can contribute evidence about what it was allowed to do and how an effect occurred. Explicit authority, rule evaluation, admissible transitions, capability mediation, lineage, and receipts can make a claim more reconstructable than an unstructured assertion. They do not make the claim true merely because the machinery is orderly.

### Adversarial tests

1. **Wrong-law attack.** A system follows an explicit but invalid, obsolete, or unauthorized rule. Structural conformance cannot supply the missing legitimacy.
2. **Bypass attack.** The governed path is sound while an alternate interface, administrator, dependency, or physical channel can produce the same effect without it.
3. **Receipt-completeness attack.** A well-formed receipt omits the decisive input, refusal, exception, or external action. Receipt validity and evidentiary sufficiency are separate findings.
4. **Effect-atomicity attack.** A receipt records authorization before the effect, or success after only part of the effect. Authorization, execution, observation, and commitment must be bound or explicitly separated.
5. **External-dependency attack.** A local proof relies on a provider, clock, identity service, model, package, or jurisdiction outside the verified boundary.
6. **Inherited-authority attack.** A child artifact or delegated actor appears warranted because its predecessor was warranted. Scope, generation, attenuation, and revocation must be checked at every transfer.
7. **Measurement-substitution attack.** Counts of gates, receipts, hashes, or tests are treated as warrant strength without validating their relevance to the claim.
8. **Domain-transfer attack.** Software assurance structure is carried into legal, scientific, institutional, or interpersonal judgment without domain authority and evidence.

### Claim and evidence ceiling

The paper proposes a claim-scoped structural-warrant relation and a ladder for measuring reconstructability. It does not establish truth, correctness, justice, legal authority, complete evidence, or universal superiority of governed systems. A structurally warranted result remains defeasible by invalid rules, omitted surfaces, external dependencies, contradictory evidence, and a mismatched claim domain.

The reported study remains source-reported unless its exact subjects, fixtures, procedures, observations, and result computations are recovered and independently checked. Claims about performance, assurance improvement, legal effect, institutional behavior, or cross-domain transfer require external evidence and qualified review. No external research was added in this pass.

### Reader-facing consequence

The public value is a sharper question than "does the system have logs?": what exact part of this claim is supported by the system's structure, what could bypass that structure, and what still depends on evidence outside it?

## 12. Conclusion

Warrant by Structure identifies an important design target: software whose authority, decisions, effects, and lineage are not left solely to reconstruction. The idea becomes stronger when it refuses to equate receipt production with proof.

A structurally mediated system can make warranted execution more inspectable and falsifiable. It cannot manufacture legitimate authority, guarantee external effects, or prove its own closure merely by emitting artifacts. Those stronger claims require explicit roots, effect evidence, bypass analysis, independent verification, recovery semantics, and a bounded threat model.

The empirical comparison remains promising but unverified. With a reconstructable dataset and an executable VTE, the paper could test whether structurally warranted regimes are not only conceptually distinct but measurably realizable.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Revision.** The present paper does not claim a complete revision treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that software systems produce effects under mixtures of declared capability, ambient privilege, runtime convention, external dependency, human discretion, and post hoc audit. Its nearest external comparison fields are formal, governance, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E2]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E3]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

**[E4]** Leslie Lamport. *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Addison-Wesley, 2002. https://lamport.azurewebsites.net/tla/book.html **Relationship:** Predecessor specification discipline for state machines, safety, liveness, and refinement.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

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

**[A6]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848560](https://doi.org/10.5281/zenodo.23848560)
