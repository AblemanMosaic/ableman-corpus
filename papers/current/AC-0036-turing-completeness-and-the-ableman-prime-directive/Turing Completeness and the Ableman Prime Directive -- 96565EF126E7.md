# Turing Completeness and the Ableman Prime Directive

## Undecidability and the Bounded Constitutional Containment of Effects

### The Ableman Prime Directive (APD) asks a different question: whether bindings that affect an agent remain detectable, refusable, and renegotiable.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Turing-complete execution offers broad computational expressiveness but admits program properties that no general decision procedure can determine for every program and input. The Ableman Prime Directive (APD) asks a different question: whether bindings that affect an agent remain detectable, refusable, and renegotiable.

The paper's central claim is not that undecidability can be removed or that arbitrary computation can be made fully visible and reversible. It is that a Turing-complete executor can be placed behind a more limited constitutional boundary: a terminating policy evaluator admits bounded plans; an effect membrane constrains external actions; an independent supervisor enforces epochs and resource limits; and external observation produces claim-bounded receipts. These mechanisms can preserve **bounded APD properties for declared effects** even though arbitrary internal behavior remains incompletely predictable.

The result depends on explicit assumptions. Historical evidence is limited by observation coverage; checkpoint rollback does not undo arbitrary external effects; hash chains show integrity relative to trusted inputs and canonicalization rather than factual truth; and a decidable law layer must actually restrict its language and evaluation. This is an architecture and proof-obligation program, not a formal proof or verified implementation.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/turing-`

`completeness-ableman-prime-directive/`  
`integration-custody-manifest.v0.1.json`,  
SHA-256  
`FB837F1876465B1339D4ED44DAF4DB1BEB4A832BC15D84AF3A913E3FC088A47A`. The source remains unchanged.

The APD triad, undecidability tension, layered containment proposal, recovery epochs, receipt-integrity concern, bounded audit, envelope-creep analysis, and fork clarity are author material. The bounded definitions, corrected claim, formal assumptions, proof obligations, corpus interfaces, full realization funnel, expanded countertests, and editorial alternatives are AI-assisted contributions explicitly distinguished from the original author material.

No formal proof, implementation, conformance run, or external literature review was performed. Standard computer-science results are used as orientation but require normal primary-source references for a future evidence-qualified revision.

## 1. Two Different Questions

Turing completeness concerns the class of computations a formal system can express or simulate, subject to unbounded resources in the abstract model. APD concerns the conditions under which a binding effect is legitimate or at least constitutionally contestable.

The questions are therefore:

- **Expressiveness:** what transformations can the execution model represent?
- **Binding governance:** which effects may become externally consequential, under whose authority, with what visibility and recovery path?

Expressiveness does not itself grant authority. Conversely, a governed boundary need not decide every property of the computation behind it in order to constrain selected effects.

## 2. Bounded APD Definitions

The source describes APD through detectability, refusal, and renegotiation. For operational use, each term needs a boundary.

**Detectability:** declared effect attempts and observed outcomes at the governed boundary remain attributable, inspectable, and bound to exact policy, state, authority, and evidence. This does not imply visibility into every internal instruction or hidden physical effect.

**Refusal:** an affected authority or declared policy can prevent further admitted effects, terminate or isolate an execution epoch, and preserve a recoverable governed state. Refusal cannot erase history or guarantee exit without cost from every real-world binding.

**Renegotiation:** the charter, policy, envelope, or continuation can be amended, appealed, replaced, or forked through an explicit governed transition. Renegotiation is not unilateral self-expansion by the running process.

These bounded properties preserve negative power at a declared interface. They do not establish universal legitimacy or moral correctness.

## 3. What Undecidability Does and Does Not Establish

The standard Halting Problem result rules out one total and correct algorithm that decides, for every program $P$ and input $x$, whether $P(x)$ halts. It does not imply that no individual program can be analyzed, that no restricted language can be decidable, or that resource bounds and external timeouts are impossible.

The relevant tension is narrower:

- arbitrary programs can defeat universal prediction of termination and many nontrivial behavioral properties;
- a governance design that requires complete prediction of arbitrary execution cannot be generally realized;
- a governance design can instead restrict admitted plans, bound resources, mediate external effects, and record observed boundary events.

This change does not solve undecidability. It changes the property being governed.

## 4. Containment Architecture

The source proposes five layers:

1. **MCIR:** a canonical Intermediate Representation for declared meaning and transformation intent.
2. **MCIR-Law:** a bounded admissibility evaluator.
3. **PEIR:** the execution representation or runtime plan, potentially Turing-complete.
4. **Domain Effects:** the membrane through which declared external actions pass.
5. **ReceiptLog:** an externally protected record of admitted decisions and observed boundary events.

For the architecture to support the claim, several conditions must hold:

- MCIR-Law uses a language and evaluator that terminate under declared bounds;
- PEIR cannot bypass the effect membrane through alternate channels;
- resource enforcement and epoch termination are controlled outside PEIR;
- the receipt writer and trust root remain outside PEIR's mutation authority;
- every consequential effect class is either mediated or explicitly listed as uncovered;
- policy, canonicalization, identity, and state versions are exact;
- refusal, failure, timeout, partial effect, conflict, and unknown remain distinct outcomes.

Calling a layer decidable or external is insufficient; the boundary must be demonstrated.

## 5. Predictive and Historical Detectability

**Predictive detectability** asks whether the system can determine what an arbitrary computation will do before running it. That goal is unavailable in general.

**Historical detectability** asks what a declared observer can reconstruct from admitted decisions, effect-bound observations, checkpoints, and receipts after or during execution.

Historical detectability is feasible only within an observation boundary. It can fail through unmediated I/O, covert channels, partial instrumentation, compromised observers, ambiguous canonicalization, dropped receipts, or effects that occur outside the represented domain.

The proper claim is:

> Every governed effect observed through the declared membrane should produce a receipt whose scope and blind spots are explicit.

It is not: whatever the computation did is necessarily recorded.

## 6. Recovery Epochs and Refusal

An external supervisor can execute a plan inside an epoch with declared CPU, memory, time, I/O, effect, and receipt budgets. It can checkpoint eligible internal state and terminate the epoch when a bound is reached.

This provides bounded refusal only if:

- the supervisor is outside the executor's authority;
- termination is effective at the relevant substrate;
- checkpoints are complete for the state claimed recoverable;
- external effects are delayed, transactional, idempotent, compensable, or separately governed;
- secrets, network messages, physical actions, and third-party effects are not falsely described as rolled back.

Rollback restores a captured state. It does not undo every external consequence. When reversal is impossible, the system needs compensation, containment, disclosure, or escalation rather than a fictitious rollback claim.

## 7. Receipt Integrity and Claim Ceiling

For an observed event record $E_n$, a receipt chain may be represented as:

$$
R_n=H(d\parallel R_{n-1}\parallel Canon(E_n)\parallel m_n),
$$

where $d$ is domain separation, $Canon$ is a versioned deterministic canonicalization, and $m_n$ binds metadata such as observer, policy, subject, environment, time basis, and claim ceiling.

Under appropriate cryptographic assumptions, protected keys or roots, retained data, and independent verification, such a chain can make later alteration detectable. It does not prove that $E_n$ was true, complete, authorized, or semantically correct. A trusted writer can hash a false observation; a compromised sensor can faithfully commit fabricated data; a running process can emit a truthful receipt about the wrong boundary.

Receipt integrity therefore requires separate proof obligations for:

- cryptographic construction and parameters;
- canonicalization uniqueness;
- writer and root custody;
- subject and environment binding;
- observation adequacy;
- append and omission detection;
- independent verification and recovery.

## 8. Bounded Audit and Comprehensibility

Receipt volume can itself create opacity. A useful audit surface needs canonical schemas, stable identifiers, bounded payloads, indexes, summaries derived from exact records, explicit omissions, and paths from summaries back to evidence.

Aggregation can lose semantic detail. "Without semantic loss" is not assumed; each summary should declare which distinctions it preserves, coarsens, or omits. Bounded audit is a design problem involving latency, storage, privacy, human comprehension, and verification cost.

## 9. Envelope Creep

Repeated requests can expand CPU, time, memory, effect classes, data access, authority, or continuation until the original boundary becomes ceremonial. Envelope modification must therefore be a governed transition with:

- the prior and proposed envelope;
- cumulative growth and duration;
- requesting and deciding authorities;
- reasons and evidence;
- new risks and affected parties;
- rollback or expiry conditions;
- a receipt and challenge path.

The running process cannot be the sole authority for its own expansion. A sequence of individually small admissions must also be evaluated for cumulative effect.

## 10. Forks and Renegotiation

A fork should name the predecessor state, retained and changed law, identity relation, authority, effect boundary, and continuity claim. Receipt discontinuity can reveal missing lineage only when the observer expects a particular chain and has an external root. It cannot by itself label the fork illegitimate.

Renegotiation succeeds when a change is visible, authorized, challengeable, and does not silently rewrite prior obligations. Some terms may be declared immutable within one charter, but the authority and consequences of that declaration remain open to higher-order review or exit where the system promises it.

## 11. Qualified Architectural Claim

Let $B$ be a declared effect boundary, $L$ a terminating admissibility layer, $S$ an external resource supervisor, $W$ an independent observer and receipt writer, and $E$ a Turing-complete executor.

The architecture can preserve bounded APD properties for effects in $B$ only if:

$$
\begin{aligned}
&Total(L) \\
&\land NonBypass(B,E) \\
&\land External(S,E) \\
&\land External(W,E) \\
&\land Coverage(W,B) \\
&\land Recoverable(S,B)
\end{aligned}.
$$

Even then, the conclusion is limited to the stated boundary, threat model, effect classes, and recovery semantics. It does not make all computation lawful or all bindings legitimate. It makes selected external consequences governable under declared assumptions.

## 12. Relation to the Corpus

*MCIR* supplies the declared transformation representation. *Effect Sovereignty* identifies the external-effect boundary. *The Three Hash Rule* separates identity, state, and evidence commitments. *Reasoning by Way of Receipts* bounds conclusions by retained evidence. *Universal Governance Kernel* supplies admission, refusal, commitment, execution, and receipt structure.

The Governed Meaning Base can store policies, envelopes, effects, receipts, conflicts, forks, evidence standings, and revisions. It does not prove containment merely by representing the architecture. These are typed interfaces, not identity mergers or conformance evidence.

## 13. Realization Funnel

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

- **Possibility:** enumerate computation models, effect paths, observation boundaries, authority structures, recovery mechanisms, bypasses, and harmful realizations.
- **Specification:** define bounded APD properties, admissibility, envelopes, supervisors, effects, receipts, forks, and proof obligations.
- **CM1:** retain all admissible configurations, including bypassable, weakly observed, irreversible, opaque, over-centralized, and falsely reassuring forms.
- **CM2:** select preferable forms under least authority, non-bypass, coverage, recovery, performance, privacy, auditability, comprehensibility, and user sovereignty.
- **IC:** bind an Instance Constitution or Instance Configuration for one executor, policy language, substrate, effect set, observer, threat model, and recovery boundary.
- **IR:** construct its Instance Realization or Implementation Realization as a particular contained runtime and verifier.
- **Evidence:** test totality, bypass resistance, timeouts, resource bounds, checkpoint recovery, external effects, receipt integrity, omissions, forks, and adversarial escalation.
- **Revision:** amend policies, boundaries, implementation, and claims through explicit lineage without rewriting failed tests.

This paper supplies a Specification and candidate CM1/CM2 criteria. It does not provide a selected IC, verified realization-stage IR, or formal proof. In MCIR and PEIR, `IR` means Intermediate Representation; in the funnel,

`IR` means Instance Realization or Implementation Realization.

## Bounded Effect-Containment Discipline Under Undecidability

Across the completed P1 corpus, this paper gives the Ableman Prime Directive (APD) a bounded role: it is a **discipline for containing, observing, refusing, recovering, and renegotiating consequential effects when general prediction is impossible**. It does not solve the halting problem, prove arbitrary programs safe, require comprehensibility of all internals, or guarantee that a containment boundary cannot fail.

- **Adjacent work:** *The Integrity Enforcement Layer*  
  **Supplies:** Protected mediation, refusal, and effect boundaries.  
  **APD boundary:** APD states the bounded containment objective; IEL is one architectural realization family.

- **Adjacent work:** *A Constitutional Syscall Architecture for Cyber-Physical Control Systems*  
  **Supplies:** A device-facing effect ABI and reconciliation lifecycle.  
  **APD boundary:** The syscall profile operationalizes APD for cyber-physical actions.

- **Adjacent work:** *The Mechanics of Constitutional Enforcement*  
  **Supplies:** Rule placement, courts, effect atomicity, and classified remainder.  
  **APD boundary:** Those mechanics supply containment and evidence structures.

- **Adjacent work:** *MosaiCOS: A Constitutional Operating System*  
  **Supplies:** A proposed full-stack constitutional OS configuration.  
  **APD boundary:** MosaiCOS may pursue APD compliance over a declared surface without proving universal containment.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Durable decision, effect, verification, refusal, promotion, and revision records.  
  **APD boundary:** Receipts make bounded containment inspectable; they do not guarantee the boundary held.

An APD containment claim should bind:

$$
\begin{aligned}
A= (&subject, effect\_surface, authority, capabilities, \\
&mediators, resource\_bounds, observers, recovery, \\
&refusal, fork\_exit, evidence, remainder)
\end{aligned}.
$$

The claim is only as broad as the enumerated effect surface and trusted computing base. Predictive prevention, runtime mediation, historical detection, rollback, compensation, isolation, revocation, and forkability are different controls. No one control substitutes for all others.

Envelope creep is a primary falsifier: hidden channels, privileged bypasses, new devices, provider-side effects, shared resources, data exfiltration, or authority expansion can move consequential behavior outside the claimed boundary. Recovery epochs must preserve which harms are reversible, compensable, detectable, or irretrievable.

The universal GSM can type   
`CONTAINED_WITHIN_EFFECT_SURFACE`, `MEDIATED_BY_BOUNDARY`,  
`BOUNDED_BY_RESOURCE`, `OBSERVED_BY`, `DETECTED_AFTER_EFFECT`, `RECOVERABLE_BY`,  
`REFUSED_BY_APD`, `EXITS_BY_FORK`, `ESCAPES_ENVELOPE_VIA`,  
and   
`LEAVES_IRREVERSIBLE_REMAINDER`. These relations make APD a scoped claim rather than a slogan.

This integration establishes four editorial commitments: adopt bounded effect-containment discipline as APD's official role; adopt the containment-claim envelope; publish control classes separately; and require envelope-creep and irreversible-remainder analysis for every APD claim.

## Semantic-to-Effect Containment Chain

The fixed-seed comparison with GOORRT, communal computing, GCML, and Semantic Legitimacy Before Context exposes the layers that precede an APD containment claim:

$$
\begin{aligned}
C= (&admitted\_meaning, representation, procedure, \\
&realization, mediators, effect\_surface, observers, \\
&recovery, remainder)
\end{aligned}.
$$

SLBC can admit material for a purpose or mark it effect-eligible, but it does not authorize or contain the later effect. GOORRT can represent the relevant object, operation, and realization commitments, while representation completeness cannot show that the implementation follows them. GCML can carry procedural obligations toward a target, yet language and compiler conformance remain upstream of runtime mediation.

APD begins at the actual realization and effect surface. Every handoff should state which obligations are preserved, refined, deferred, refused, or left as a gap. A deferred obligation must name the load-bearing downstream mechanism. An unbound or bypassable mechanism reopens the containment claim even when all upstream artifacts are internally valid.

Communal computing widens the remainder. Computational and device effects may be bounded while social, reputational, distributive, coercive, or institutional effects remain uninstrumented or irreversible. A public-space APD claim must name those exclusions instead of treating the visible interface as the whole effect surface.

The universal GSM can type   
`ADMITS_MEANING_BEFORE_EFFECT`,  
`REPRESENTS_CONTAINMENT_COMMITMENT`, `CARRIES_APD_OBLIGATION_PROCEDURALLY`,  
`BINDS_OBLIGATION_TO_MEDIATOR`, `CONTAINS_DECLARED_EFFECT_SURFACE`,  
`LEAVES_SOCIAL_EFFECT_REMAINDER`, and   
`REOPENS_ON_UNBOUND_HANDOFF`.

This randomized review establishes four editorial commitments: adopt the semantic-to-effect chain; require explicit obligation status at every handoff; keep effect eligibility below authorization and containment; and require APD claims in public settings to expose social and institutional remainder.

## Two APD Profiles That Must Not Be Silently Collapsed

The frozen P3 field uses the Ableman Prime Directive in two related but non-identical ways. The first is the bounded effect-containment discipline developed in this paper: a terminating admission layer, non-bypassable mediation, external observation, recovery, and explicit remainder over a declared effect surface. The second is a negative-power discipline used by Jnana, split-authority coordination, governance incentives, and the Well-Governed Mind: an affected participant should be able to detect a binding, refuse or contest it where refusal is lawful, exit or fork where available, and renegotiate its application.

These uses can be related without pretending that either entails the other:

$$
APD_E=(effect\_surface,mediators,observers,recovery,bypass,remainder),
$$

$$
\begin{aligned}
APD_N= (&affected\_subject, binding, detectability, refusal, \\
&contest, exit, renegotiation, cost, remainder)
\end{aligned}.
$$

`APD_E` constrains consequential effects.

`APD_N` evaluates practical negative power under a binding. A runtime may contain its declared I/O while leaving an affected person unable to contest, exit, or renegotiate. Conversely, a social or cognitive setting may improve detection and contestability without supplying a computable effect boundary, terminating policy language, or rollback mechanism.

GOORRT, GCML, and Semantic Legitimacy Before Context locate APD downstream of representation, procedure, and semantic admission. Their use confirms that a representation or admitted rule is not yet an effect-containment claim. Communal computing adds public, distributive, reputational, and institutional remainder. The Well-Governed Mind is a bounded cross-domain projection only: it cannot convert software containment evidence into clinical truth or therapeutic authority.

The universal GSM can type   
`SPECIALIZES_APD_EFFECT_CONTAINMENT`,  
`SPECIALIZES_APD_NEGATIVE_POWER`, `RELATES_WITHOUT_ENTAILMENT`,  
`BINDS_APD_TO_AFFECTED_SUBJECT`, `ENTERS_APD_AT_EFFECT_SURFACE`,  
`LEAVES_SOCIAL_OR_CLINICAL_REMAINDER`, and   
`REFUSES_CROSS_DOMAIN_EVIDENCE_TRANSFER`.

This reverse-dependency review establishes four editorial commitments: distinguish the effect-containment and negative-power APD profiles; define their shared kernel and non-entailment; require every APD claim to name affected subjects as well as the governed surface; and preserve a clinical and cross-domain evidence firewall for cognitive applications.

## 14. Counterevidence and Failure Tests

The proposal must narrow, revise, or fail if: (1) MCIR-Law does not terminate; (2) a supposedly decidable rule invokes the Turing-complete executor; (3) PEIR bypasses the effect membrane; (4) unlisted I/O channels exist; (5) the executor can modify the supervisor; (6) the executor can modify the receipt writer; (7) epoch termination fails; (8) checkpoint state is incomplete; (9) rollback is claimed after irreversible external effects; (10) compensation is mistaken for reversal; (11) receipts omit partial effects; (12) receipts record attempted rather than actual effects without distinction; (13) the observer is compromised; (14) canonicalization is ambiguous; (15) chain roots are not externally retained; (16) receipts can be truncated without detection; (17) a valid hash commits false data; (18) receipt volume defeats audit; (19) summaries omit decisive evidence; (20) privacy prevents necessary review; (21) audit disclosure violates legitimate privacy; (22) envelope increments evade cumulative review; (23) authority expansion becomes self-approved; (24) resource exhaustion disables observation; (25) time measurement is controlled by the executor; (26) a timeout is reported as refusal without terminating effects; (27) a fork preserves hash lineage but changes law silently; (28) a legitimate fork is mislabeled illegitimate; (29) detectability is claimed for internal state; (30) refusal is claimed to erase past effects; (31) renegotiation is unavailable to affected parties; (32) APD is treated as universal moral legitimacy; (33) Turing completeness is blamed for failures caused by ordinary architecture; (34) restricted analyzable programs are ignored; (35) historical evidence is mistaken for prediction; (36) the qualified conjunction lacks an executable test; (37) GMB storage is treated as containment proof; (38) a named stack is treated as implemented; (39) cryptographic security is claimed without parameters and threat model; or (40) publication proceeds without formal and prior-art review.

## Containment Changes the Operational Problem, Not Undecidability

### Public orientation

General computation cannot be completely predicted in advance. The Ableman Prime Directive therefore cannot require an oracle for every future behavior. The paper's qualified claim is operational: expressive computation may continue inside boundaries that make consequential effects observable, interruptible, attributable, and recoverable under declared profiles.

### Adversarial tests

1. **Halting-solution overclaim.** Containment is presented as solving the halting problem. It does not; it changes what must be detected and controlled at effect boundaries.
2. **Rice-style semantic overclaim.** A monitor is said to decide arbitrary nontrivial program properties. Enforceable properties must be operationally specified and boundary-observable.
3. **Monitor-recursion attack.** The governor is itself unrestricted and unaudited. The constitutional substrate needs a smaller declared trust and effect surface.
4. **Covert-channel attack.** Computation influences the world through timing, resource use, caches, shared state, or inference channels outside named effects. The remainder must be stated.
5. **Resource-exhaustion attack.** A process remains effect-contained but denies service or makes review impossible. Time, memory, energy, storage, and attention are governed effects.
6. **Interruptibility illusion.** Cancellation is requested after irreversible external work has occurred. Effects require reservation, commit, observation, compensation, and remainder.
7. **Wrapper-bypass attack.** A Turing-complete extension reaches raw capabilities beneath the constitutional layer. Complete mediation must be proven per capability path.
8. **Safety-liveness collapse.** The safest policy is permanent refusal. APD profiles must preserve lawful continuation and expose cost without treating liveness as permission.

### Claim and evidence ceiling

The paper correctly leaves undecidability unsolved and proposes bounded effect containment. Publication must distinguish two APD profiles: a broad normative demand for inspectability and renegotiation, and an operational profile realizable through effect boundaries, budgets, receipts, interruption, and recovery. Neither profile guarantees safe semantics or total observability.

Formal claims concerning Turing completeness, halting, Rice's theorem, reference monitors, capabilities, or containment require precise statements and primary external sources. Realization claims require bypass, covert-channel, resource, and recovery tests. No external research was added in this pass.

### Reader-facing consequence

The practical shift is from trying to predict everything a powerful program will do to controlling when and how uncertain computation can acquire resources, cross boundaries, produce irreversible effects, and continue.

## Conclusion

Undecidability prevents a universal predictive governor for arbitrary computation. It does not prevent every useful form of constitutional control. A system can restrict the language in which effects are admitted, place a Turing-complete executor behind a non-bypassable membrane, enforce resource epochs externally, and record observed boundary events outside the executor's authority.

The achievement is bounded, not absolute. Internal computation remains incompletely predictable; external effects may be irreversible; observations may be partial; receipts may faithfully preserve false inputs. Constitutional containment succeeds only where its assumptions, boundary, evidence, and recovery claims are explicit and tested.

## Reference and Verification Note

### Author corpus interfaces inspected under exact custody

Ableman Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.*

Ableman Adam Ableman *Effect Sovereignty.*

Ableman Adam Ableman *The Three Hash Rule.*

Ableman Adam Ableman *Reasoning by Way of Receipts.*

Ableman Adam Ableman *Universal Governance Kernel.*

### External verification required

No external literature was consulted. Further evidentiary strengthening requires primary-source references and comparison for Turing completeness, computability and the Halting Problem, decidable and total policy languages, reference monitors, sandboxing and isolation, resource accounting, watchdogs, checkpoint and rollback limits, transactional and compensating effects, tamper-evident logging, cryptographic commitments, capability security, and formal verification. No theorem, security property, or novelty claim is certified here.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that turing-complete execution offers broad computational expressiveness but admits program properties that no general decision procedure can determine for every program and input. Its nearest external comparison fields are provenance, security, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E2]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E3]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

**[E4]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E5]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E6]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E7]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

### Ableman corpus

**[A1]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *A Formal Theory of Work Custody*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-C8F2F9BF38C45E29`;  
source SHA-256  
`A80657E21BA277ADF1C229A2AAE221963B97A62EA2AF3EBC36434A916A8EEA44`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Governance Witnesses*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-9E8DA0EFE860DE5D`;  
source SHA-256  
`8BF8C3646040F6E1F5222A8AA92C1106AA1F841E8A2C65402F468C83D59D06E5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

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

DOI: [10.5281/zenodo.23848480](https://doi.org/10.5281/zenodo.23848480)
