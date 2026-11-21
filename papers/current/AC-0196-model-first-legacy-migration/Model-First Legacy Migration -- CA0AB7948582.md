# Model-First Legacy Migration

## Recovering Bounded Behavioral Models Without Confusing Observation, Intention, and Law

### Legacy migration is usually framed as translation from one implementation to another.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Legacy migration is usually framed as translation from one implementation to another. That framing leaves the most consequential uncertainty untouched: no one knows which observed behaviors are intended obligations, which are relied-upon accidents, which are defects, and which depend on an environment that the replacement does not reproduce. This paper develops a model-first alternative. A bounded behavioral model is extracted from exact source custody, static structure, observations, operational knowledge, policy, and downstream dependencies; it is then adjudicated before it may become normative. Candidate realizations are compared against both the model and the original system within declared envelopes, equivalence relations, observers, and claim ceilings.

The proposal does not solve general program equivalence or infer intention from behavior alone. It replaces an unaudited rewrite with a governed chain of explicit models, gaps, assumptions, tests, promotion decisions, rollback paths, and revision records. Its strongest capability is not automatic modernization. It is the conversion of hidden dependencies into inspectable and contestable migration obligations while preserving a disciplined refusal to claim beyond observed and justified evidence.

## 1. The Migration Problem

A running legacy system combines at least five things that migration projects routinely collapse:

1. intended requirements;
2. behavior on the states and environments actually observed;
3. accidental behavior on unobserved or rare paths;
4. behavior on which users or neighboring systems have come to rely;
5. institutional rules about what a successor is allowed to preserve, change, or refuse.

Calling the binary "the specification" is descriptively useful but normatively incomplete. The binary is authoritative evidence about what happened under particular conditions. It is not, by execution alone, an authority for what ought to continue. Conversely, a newly written specification is not faithful merely because it is legible.

The model-first thesis is therefore narrower and stronger than "extract a model and regenerate the program":

> A legacy migration becomes governable when behavior, intention, authority, realization, evidence, and residual uncertainty are represented separately; when every correspondence claim is bounded to an explicit envelope; and when a model becomes normative only through an authorized adjudication rather than through extraction alone.

This changes the unit of migration from code translation to **obligation reconstruction**.

## 2. Core Distinctions

### 2.1 Legacy subject

The **legacy subject** is an exactly identified system revision together with the dependencies and environment required to observe it. A filename, repository label, or deployed service name is insufficient custody.

### 2.2 Descriptive model candidate

A **descriptive model candidate** records operations, state, invariants, effects, refusals, nondeterminism, resources, authority crossings, and known unknowns inferred from available evidence. It remains defeasible and does not become correct through serialization.

### 2.3 Normative migration model

A **normative migration model** is a descriptive candidate plus explicit decisions about what a successor must preserve, may vary, should repair, or must refuse. Its authority comes from an identified adjudication process, not from the extractor.

### 2.4 Realization

A **realization** is an implementation configured to satisfy a particular normative model under a declared target profile. It is neither identical to the model nor automatically equivalent to the legacy subject.

### 2.5 Correspondence record

A **correspondence record** identifies two subjects, their exact revisions, the comparison envelope, the observer and oracle, the equivalence relation, the test population, unexplained remainder, and the standing earned. Correspondence is a bounded relation, not an identity assertion.

### 2.6 Claim ceiling

A **claim ceiling** is the strongest conclusion justified by the evidence. It prevents success on an observed sample from becoming a claim about every reachable state, future environment, or hidden dependency.

## 3. A Bounded Formal Model

Let:

* $L$ be an exact legacy subject;
* $M_d$ be a descriptive model candidate;
* $M_n$ be an adjudicated normative migration model;
* $R$ be a candidate realization;
* $\Omega$ be a declared observation and disturbance envelope;
* $Q$ be a set of queries or test traces;
* $\sim_q$ be the accepted equivalence relation for query $q$;
* $O$ be the declared observer and oracle arrangement.

Define an envelope as:

$$
\Omega = \langle I, E, T, F, N, B \rangle
$$

where $I$ is the input class, $E$ the environment, $T$ the time and scheduling conditions, $F$ the injected faults, $N$ the permitted nondeterminism, and $B$ the resource bounds.

A finite correspondence observation may be recorded as:

$$
\operatorname{ObsCorr}_{\Omega,Q,O}(A,B)
=
\bigwedge_{q \in Q}
\left(
\operatorname{Obs}_{O}(A,q) \sim_q \operatorname{Obs}_{O}(B,q)
\right)
$$

This says only that the declared observations correspond for the tested queries under the recorded conditions. It is not universal semantic equivalence.

A migration claim must carry at least:

$$
C = \langle A,B,h_A,h_B,\Omega,Q,O,\sim,\Delta,U,S,V \rangle
$$

where $h_A$ and $h_B$ bind exact artifacts, $\Delta$ records divergences, $U$ records unobserved or unresolved regions, $S$ is the earned standing, and $V$ is the revision lineage.

The tempting inference

$$
\begin{aligned}
&\operatorname{Corr}(L,M_n) \\
&\land \operatorname{Corr}(M_n,R) \\
&\Rightarrow \operatorname{Corr}(L,R)
\end{aligned}
$$

is not valid without additional conditions. Composition requires compatible envelopes, observers, equivalence relations, state abstractions, effect models, and loss declarations. A safe rule is partial:

$$
\operatorname{ComposeCorr}(C_1,C_2)
\rightarrow
\begin{cases}
C_3, & \text{if compatibility and coverage obligations are discharged} \\
\operatorname{Gap}(G), & \text{if information or proof is missing} \\
\operatorname{Refusal}(R), & \text{if obligations conflict}
\end{cases}
$$

Model-mediated migration is valuable precisely because it makes these missing conditions visible.

## 4. Extracting Behavior Without Hallucinating Intention

Observation alone cannot distinguish a requirement from an accident. Static code alone cannot reveal every deployed environment or dependency. Interviews alone cannot establish actual behavior. Extraction therefore combines independent evidence channels:

- **Channel:** exact source and binary custody  
  **What it can support:** what artifact was examined  
  **What it cannot establish alone:** deployed reachability or intended behavior

- **Channel:** static structure  
  **What it can support:** potential operations, state, effects, and paths  
  **What it cannot establish alone:** which paths occur or are institutionally required

- **Channel:** dynamic traces  
  **What it can support:** behavior under observed conditions  
  **What it cannot establish alone:** unobserved behavior or normative legitimacy

- **Channel:** tests and incident records  
  **What it can support:** known expectations and failures  
  **What it cannot establish alone:** completeness or current deployment behavior

- **Channel:** operator and user testimony  
  **What it can support:** intention, reliance, and tacit procedure  
  **What it cannot establish alone:** exact machine behavior

- **Channel:** downstream dependency analysis  
  **What it can support:** behaviors on which other systems rely  
  **What it cannot establish alone:** whether those dependencies should be preserved

- **Channel:** policy, law, and contracts  
  **What it can support:** authoritative obligations  
  **What it cannot establish alone:** actual implementation conformance

Each candidate behavior receives one of four postures:

1. **required invariant** - supported as an intended obligation;
2. **relied-upon incident** - not intended originally, but currently depended upon;
3. **repair candidate** - observed behavior proposed for correction;
4. **unresolved** - evidence is insufficient or contradictory.

An extractor may propose these classifications. It may not promote them by itself.

## 5. The Behavioral Model

A useful migration model is not merely an input/output table. For each bounded subsystem it records:

$$
M = \langle S,Op,Pre,Post,K,Eff,Ref,Auth,Nd,Res,Obs,Dep,Unk \rangle
$$

where:

* $S$ is state and state partitioning;
* $Op$ is the operation set;
* $Pre$ and $Post$ are preconditions and postconditions;
* $K$ is the invariant set;
* $Eff$ is the effect surface;
* $Ref$ is the refusal and failure surface;
* $Auth$ is the authority and jurisdiction model;
* $Nd$ is permitted nondeterminism;
* $Res$ is the resource model;
* $Obs$ is the observable projection;
* $Dep$ is the dependency and environment model;
* $Unk$ is the explicit unknown and disputed region.

The inclusion of $Unk$ is constitutive. A model that cannot represent its unknowns invites the migration team to confuse omission with absence.

## 6. Migration Invariants

The following invariants govern a model-first migration candidate:

1. **Exact-subject binding.** Every source, model, realization, test corpus, compiler, runtime, and policy head is revision-bound.
2. **Description is not authority.** Extraction does not grant a descriptive model normative standing.
3. **Intent is not induced from execution.** Normative classification requires declared authority and contrary evidence remains visible.
4. **Envelope honesty.** Every correspondence claim names inputs, environments, time, faults, nondeterminism, resources, and observers.
5. **Unknown preservation.** Unobserved, contradictory, and uninterpretable regions remain explicit gaps.
6. **Effect completeness.** External effects, denied effects, retries, timeouts, and partial failures are part of the model.
7. **Refusal preservation.** A successor may not convert a required refusal into silent success.
8. **Authority non-expansion.** Migration does not widen permissions, jurisdictions, or standing merely because the target can do more.
9. **Correspondence non-transitivity.** Bridge composition requires its own compatibility and loss review.
10. **Stateful rollback.** Promotion includes a state-reconciliation and rollback model, not only a deployable prior binary.
11. **Independent challenge.** Assurance claims expose their oracle, observer, shared trust roots, and opportunities for independent falsification.
12. **Successor lineage.** Changes to model, classification, envelope, realization, dependency, or evidence create a traceable successor rather than rewriting history.

## 7. Governed Migration Lifecycle

The source proposes extraction, realization, shadow operation, promotion, and outward repetition. A safer lifecycle separates candidate creation from standing:

```text
EXACT_SUBJECT_BOUND
        |
        v
DESCRIPTIVE_MODEL_CANDIDATE
        |
        v
INTENT_AND_DEPENDENCY_ADJUDICATION
        |
        +---- gap / dispute / refusal
        |
        v
NORMATIVE_MODEL_CANDIDATE
        |
        v
REALIZATION_AND_STATIC_CHECKS
        |
        v
SHADOW_OR_SIMULATION
        |
        +---- divergence / unsafe effect / rollback
        |
        v
BOUNDED_QUALIFICATION
        |
        v
CANARY_OR_PARTIAL_PROMOTION
        |
        +---- monitored rollback / state repair
        |
        v
BOUNDED_PROMOTION_AND_CONTINUOUS_DRIFT_REVIEW
```

A "clean window" is not evidence that an open behavior space has been exhausted. Promotion requires an acceptance profile stating duration, traffic and state coverage, fault coverage, excluded regions, divergence threshold, severity policy, rollback readiness, and residual risk. High-consequence systems may never justify full replacement from observational evidence alone.

Shadow execution also has costs and risks: production data may be duplicated, effects may accidentally escape, observers may perturb timing, and state may diverge. Shadowing therefore requires an effect membrane, privacy controls, resource limits, and evidence that the shadow remained non-authoritative.

## 8. Realization Funnel

| Stage | Model-first migration role |
|---|---|
| Possibility | Explore all plausible legacy interpretations, model boundaries, seams, target substrates, repair proposals, and migration paths, including unsafe and undesirable ones. |
| Specification | State exact source custody, operations, state, invariants, effects, refusals, dependencies, authority, unknowns, observer model, and claim ceiling. |
| CM1 | Enumerate admissible descriptive and normative model candidates consistent with the available evidence, including expensive, centralized, privacy-invasive, brittle, or minimally useful candidates. |
| CM2 | Prefer candidates that preserve justified obligations, minimize authority and effect surface, expose uncertainty, support substitution and rollback, protect users, and reduce future semantic debt. |
| Instance Configuration | Select the exact subsystem, source and environment revisions, model candidate, equivalence classes, observer/oracle arrangement, target, thresholds, rollout scope, and rollback plan. |
| Implementation Realization | Build extractors, model validators, realizations, membranes, shadow infrastructure, state synchronizers, comparison tools, and receipt paths for that configuration. |
| Evidence | Run static, dynamic, fault, adversarial, historical, shadow, canary, rollback, drift, dependency, privacy, and independent-observer checks; retain divergences and coverage gaps. |
| Revision | Create successors as source behavior, obligations, dependencies, models, targets, evidence, and decisions change; preserve invalidated claims and migration history. |

The paper is primarily a Specification and process proposal. It does not authorize an Implementation Realization or establish that a particular migration has passed Evidence.

## 9. Capabilities, Restated Within Their Ceilings

### 9.1 Substrate independence

A model can reduce dependence on the source implementation when the model captures the obligations relevant to the target and the correspondence bridges are independently adequate. It cannot make environmental assumptions or hardware behavior disappear.

### 9.2 Composability

Subsystem models can reveal seams and typed dependencies. They do not guarantee good decomposition. At every composition boundary, the migration must identify which component, interface, mediator, environment, architecture, or policy carries each invariant [CBC].

### 9.3 Behavior-preserving change

A model can state what a change intends to preserve and can organize evidence about the affected envelope. It cannot generally prove that no other behavior changed. The honest deliverable is a bounded difference claim plus residual uncertainty.

### 9.4 Intent-incident separation

The architecture makes the distinction recordable and adjudicable. It does not infer intention automatically. Relied-upon accidents may become successor obligations even when they were never original requirements.

### 9.5 Reversible cutover

Shadow, canary, receipts, and rollback can reduce cutover risk. Reversibility is incomplete when the new realization performs irreversible effects, changes persistent schemas, advances external protocols, or creates data the old system cannot interpret.

### 9.6 Durable knowledge recovery

The model, evidence, disputes, and lineage can preserve institutional knowledge more durably than unbound prose. They remain revisioned claims, not rot-proof or infallible documentation. GMB can retain this governed meaning without turning admission into truth [GMB].

## Model-First Continuity Application Profile

Across the completed P1 corpus, Model-First Legacy Migration is the **application profile for recovering bounded behavioral and normative models, qualifying successor realizations, and preserving continuity across legacy replacement**. It is not a new foundational representation theory, a proof of general program equivalence, or permission to treat observed legacy behavior as intended law.

- **Adjacent work:** *From Content-Addressed Storage to Governed Semantic Project Lineage*  
  **Supplies:** Exact predecessor, projection, decision, and successor lineage.  
  **Migration-profile boundary:** Migration uses lineage to preserve how each model and realization was derived.

- **Adjacent work:** *Cold Boot Continuity as a Deployment Primitive*  
  **Supplies:** Reconstructable resumption across environments and providers.  
  **Migration-profile boundary:** A successor must cold-boot its declared model, configuration, evidence, and recovery procedures.

- **Adjacent work:** *Sovereign Software*  
  **Supplies:** Inspectability, reconstructability, substitutability, and renegotiable user boundaries.  
  **Migration-profile boundary:** Migration is successful only within a declared sovereignty and dependency objective.

- **Adjacent work:** *Semantic Fragmentation and Constitutional Structure*  
  **Supplies:** Discovery of obligations split across code, data, operators, policy, and environment.  
  **Migration-profile boundary:** Fragmentation analysis identifies model gaps before a seam is trusted.

- **Adjacent work:** *The Constitutional Observability Platform*  
  **Supplies:** Heterogeneous observation and result-visibility structure.  
  **Migration-profile boundary:** Observers supply bounded correspondence evidence without making the legacy subject an oracle.

A migration instance should bind:

$$
\begin{aligned}
M= (&legacy\_subject, descriptive\_model, \\
&normative\_decisions, unknowns, dependencies, target, \\
&realization, correspondence\_envelope, observers, \\
&promotion, rollback, lineage, residual\_risk)
\end{aligned}.
$$

The descriptive model records observed behavior and gaps. Normative decisions separately classify obligations, defects, relied-upon accidents, repairs, and prohibited behaviors. The successor realization is evaluated against the adjudicated model within an explicit correspondence envelope; observation outside that envelope remains unknown rather than silently absent.

Migration is not a single cutover. Shadowing, canary operation, state reconciliation, dependency substitution, rollback, provider exit, and continuing drift review are distinct configuration choices and evidence burdens. Irreversible effects and state-schema changes require forward recovery or compensation where rollback cannot restore the prior world.

The universal GSM can type   
`DESCRIBES_LEGACY_BEHAVIOR`,  
`ADJUDICATES_AS_NORMATIVE_OBLIGATION`, `PRESERVES_EXPLICIT_UNKNOWN`,  
`REALIZED_BY_SUCCESSOR`, `CORRESPONDS_WITHIN_ENVELOPE`, `OBSERVED_BY_INDEPENDENT_CHANNEL`,  
`PROMOTED_UNDER_MIGRATION_PROFILE`, `ROLLS_BACK_WITH_STATE_RECONCILIATION`,  
`EXITS_LEGACY_DEPENDENCY`,  
and   
`RETAINS_RESIDUAL_MIGRATION_RISK`. These relations compress the work into a reusable application profile.

This integration establishes four editorial commitments: classify the work as a model-first continuity application profile; adopt the migration-instance envelope; require descriptive, normative, realization, and evidence postures to remain separate; and require cold-boot, rollback, dependency-exit, and residual-risk evidence before any bounded promotion claim.

## Adversarially Challenged Migration with Human-Domain Exclusion, Infrastructure Continuity, and Commitment Separation

The fixed-seed comparison with adversarial alternation, The Well-Governed Mind, constitutionally governed infrastructure, and CHC expands the migration profile while making its domain exclusions explicit:

$$
\begin{aligned}
M^*= (&legacy\_subject, descriptive\_model, \\
&normative\_decisions, unknowns, dependencies, \\
&infrastructure\_controls, target, IC, IR, \\
&correspondence\_envelope, commitments, audits, promotion, \\
&rollback, exit, residual\_risk)
\end{aligned}.
$$

Adversarial alternation can challenge model extraction, normative classification, successor behavior, effect membranes, rollback, and residual risk on exact subject generations. It does not prove equivalence beyond the attack and observation envelope.

The Well-Governed Mind marks a domain exclusion: this engineering method must not redescribe a person, therapy, or contested human self-model as a legacy system awaiting replacement. Structural vocabulary may be compared only through an explicit transfer envelope, and no clinical or psychological inference is licensed here.

Constitutionally governed infrastructure adds continuity obligations during migration. Scheduling, routing, credentials, fallbacks, data conversion, provider dependencies, and administrative reachability can make a formally available successor unusable in practice. Migration must therefore preserve or deliberately revise liveness, contestability, accessibility, remedy, and exit.

CHC can commit separately to exact predecessor state, descriptive and normative claim envelopes, configuration, policy, and an epoch-relative admissibility decision. These commitments support custody and replay but do not prove model truth, semantic equivalence, authority, or safe promotion.

Here IC means Instance Constitution or Instance Configuration and realization-stage IR means Instance Realization or Implementation Realization. Either expansion names the same stage; compiler Intermediate Representation remains a separate context-resolved sense.

The universal GSM can type   
`AUDITED_AGAINST_EXACT_LEGACY_GENERATION`,  
`EXCLUDES_HUMAN_REPLACEMENT_ANALOGY`, `PRESERVES_PRACTICAL_CONTINUATION`,  
`COMMITS_TO_MIGRATION_CLAIM_ENVELOPE`, `ADMITS_SUCCESSOR_AT_EPOCH`, `EXITS_DEPENDENCY`,  
and   
`RETAINS_RESIDUAL_MIGRATION_RISK`.

This randomized review establishes four editorial commitments: integrate exact adversarial challenge into migration qualification; add an explicit human-domain exclusion; require practical infrastructure continuity and effective exit; and bind state, model claims, configuration, and admissibility through separate commitments.

## Bounded Continuity Across Descriptive, Normative, and Realized Layers

Six downstream uses apply model-first migration to cryptographic commitment limits, adversarial alternation, infrastructure continuity, ACG overlays, software sovereignty, and cross-domain clinical firewalls. They confirm a migration profile centered on explicit correspondence among an observed legacy subject, descriptive model, normative successor specification, selected configuration, realized system, and evidence. No layer is automatically identical to the one before it.

$$
\begin{aligned}
M^*= (&legacy\_subject, generation, environment, observations, \\
&descriptive\_model, normative\_decisions, \\
&preserved\_capabilities, excluded\_behavior, IC, IR, \\
&correspondence, evidence, cutover, rollback, \\
&stakeholders, remainder, revision)
\end{aligned}.
$$

Observed behavior does not reveal intention, legitimacy, or required preservation. Bugs, workarounds, undocumented dependencies, operator practice, data conventions, timing, security assumptions, and institutional accommodations may be behaviorally real while remaining contested normative inputs. Human-domain expertise determines what may be removed, repaired, or preserved; the extraction system cannot decide this from traces alone.

Correspondence must be claim-specific and challenged before and after cutover. Shadow operation, differential testing, adversarial cases, state and data reconciliation, rollback, provider exit, user remedy, and retained legacy access may all be required. A successful migration does not establish full semantic equivalence, complete dependency control, or transfer of the method into clinical or institutional judgment.

The universal GSM can type   
`OBSERVES_LEGACY_SUBJECT`, `EXTRACTS_DESCRIPTIVE_MODEL`,  
`MAKES_NORMATIVE_MIGRATION_DECISION`, `SELECTS_MIGRATION_IC`, `REALIZES_MIGRATION_IR`,  
`TESTS_CORRESPONDENCE`, `ROLLS_BACK_CUTOVER`, and   
`RETAINS_LEGACY_REMAINDER`.

This review establishes four editorial commitments: adopt the layered migration record; require explicit human-domain normative decisions; make correspondence claim-specific and adversarially tested; and bind cutover, reconciliation, rollback, exit, remedy, and remainder without claiming general equivalence.

## 10. Failure Modes and Counterevidence

The thesis is weakened or refuted for a given migration when:

* extraction cost and model complexity approach or exceed disciplined replacement cost;
* the system's meaningful behavior depends on irreducible physical, social, or organizational context;
* operational traces systematically omit high-consequence paths;
* the old system itself is unsafe, inconsistent, compromised, or an unsuitable oracle;
* stakeholders cannot adjudicate intention, reliance, or repair proposals;
* dynamic code, undefined behavior, concurrency, timing, external services, or hardware defeat the chosen abstraction;
* observer effects make shadow correspondence misleading;
* the model becomes a second legacy system with its own opaque tooling and stale assumptions;
* seams optimize formal neatness while destroying operational or institutional coherence;
* a target preserves outputs while changing authority, privacy, performance, accessibility, or failure behavior;
* rollback cannot restore state or retract external effects;
* correspondence batteries share the same compiler, author, fixtures, assumptions, or blind spots as the realization;
* monitoring success is converted into standing beyond its declared envelope.

The strongest alternative hypothesis is that migration safety comes primarily from socio-technical modernization practice - domain experts, incremental replacement, operational testing, and rollback - while a formal model adds cost without enough additional assurance. A credible evaluation must compare model-first migration with strong non-model-first baselines rather than with unaudited rewrites alone.

## 11. Evidence Status of the Source Examples

The source reports a toy-scale stack involving ECA or Artifact IR models, correspondence batteries, deterministic rendering, hash and receipt binding, MCRM or replay, and a frontier discovery court. It also names trust-root and toolchain-reproduction work as prerequisites. These are valuable evidence leads, but the paper does not supply exact artifact paths, hashes, commands, test populations, negative controls, or independent reproduction records.

This revision therefore preserves the claims as **source-reported preliminary demonstrations** rather than converting them into verified results. Evidence elevation requires an exact evidence appendix that binds:

1. each subject artifact and fixture set;
2. each grammar and model profile;
3. extraction and rendering commands;
4. test and holdout selection;
5. oracle and observer identities;
6. compiler, runtime, and environment custody;
7. expected and observed divergences;
8. negative fixtures and refusal results;
9. independent reproduction, where claimed;
10. the exact claim ceiling earned.

Custody-only excluded corpora were not used as Ableman semantic evidence for this candidate.

## 12. Constitutional Computing and the Rule-of-Law Analogy

The source connects model-first migration to a movement from rule by opaque code toward rule through inspectable law. The comparison is illuminating if kept structural:

* promulgation corresponds to making obligations legible;
* congruence corresponds to testing realization against declared obligations;
* jurisdiction corresponds to a claim ceiling and authority boundary;
* constancy corresponds to revision-bound judgment;
* amendment corresponds to explicit successor and ratification processes;
* refusal corresponds to a first-class outcome rather than forced execution.

Software conformance is not legal legitimacy, and a test harness is not a court merely because it is called one. Human institutions retain authority over purposes, rights, acceptable harms, evidence standards, and contested interpretations. Independence is also graded: a separately executed verifier may still share authorship, specifications, fixtures, dependencies, funding, or infrastructure with the system it evaluates.

The constitutional contribution is therefore not a claim to have cured rule by code. It is an architecture for separating declaration, realization, observation, adjudication, and revision so that opaque execution no longer holds all of those roles by default.

## 13. Corpus Integration

Model-first legacy migration is best understood as an application profile of existing corpus machinery rather than a new foundational primitive:

* **The Substrate Migration Principle** explains why recurring migration failures may justify moving correspondence, authority, and refusal obligations into non-optional compiler, runtime, or deployment boundaries [SMP].
* **GOORRT** prevents collapse among object or state models, operation semantics, and computational realizations. Migration uses correspondence records among these families rather than treating one representation as universally constitutive [GOORRT].
* **GSOL, MCIR, PEIR, and GCML** provide candidate homes for governed operations, canonical commitments, execution-ready structure, and procedural preservation contracts. Their exact division remains an architecture question, not a premise this paper resolves.
* **Constraint-Bearing Composability** supplies the deeper account of seams, invariant carriage, residual assumptions, disturbance envelopes, and diachronic preservation [CBC].
* **Semantic Fragmentation Analysis** can locate obligations that remain split across source, database, operators, environment, policy, and neighboring systems before a seam is accepted [SFA].
* **The Constitutional Observability Platform** supplies heterogeneous observers and result-visibility structures needed to compare declaration with runtime consequences without treating one monitor as the whole truth [COP].
* **Reasoning by Way of Receipts** structures intermediate migration decisions, evidence, refusals, and gaps while denying that receipts prove their own truth [RWR].
* **The Three Hash Rule** separates exact artifact custody, admissibility commitments, and meaning commitments across source, model, realization, and evidence [THR].
* **Semantic Project Lineage** preserves reconstructible predecessors, projections, decisions, and revision relations through a long migration [SPL].
* **Cold-Boot Continuity** tests whether the model, configuration, evidence, and procedures can orient a fresh environment without relying on invisible session memory [CBCB].
* **Sovereign Software** supplies the user-facing objective: a successor should reduce coercive dependency and preserve inspectability, reconstructability, replaceability, and renegotiable boundaries rather than merely modernize implementation language [SS].
* **Dynatology and the realization funnel** distinguish possible, admissible, preferable, selected, implemented, evidenced, and revised migrations [DYN].
* **GMB**, the current Governed Meaning Base in the historical `CCF -> CMB -> GMB` lineage, can retain the model, disputes, evidence, standing, decisions, and successor graph. It is neither the legacy runtime nor the migration oracle [GMB].

This compression matters. The paper contributes a migration profile and capability thesis; it should not duplicate the representational, compositional, observability, lineage, or meaning-base architectures it invokes.

## 14. Research Program

1. Define a minimal migration-model schema including unknowns, authority, effects, nondeterminism, resources, dependencies, and claim ceilings.
2. Define correspondence-record, gap, refusal, divergence, promotion, rollback, and revision schemas.
3. Select one bounded, stateful, effectful legacy subsystem with exact custody and a safe observation environment.
4. Establish a strong conventional incremental-migration baseline for comparison.
5. Build independent static, dynamic, documentary, and stakeholder evidence channels.
6. Measure extraction effort, model size, disagreement, coverage, false confidence, and maintenance cost.
7. Construct adversarial and withheld traces, fault injection, environment changes, dependency substitutions, and malicious realization fixtures.
8. Test bridge composition rather than assuming correspondence transitivity.
9. Exercise shadow, canary, rollback, state reconciliation, and irreversible-effect cases.
10. Study whether the model remains useful and current after the initial migration.
11. Bind every empirical claim to exact artifacts, observers, commands, and negative controls.
12. Conduct current primary-source research on program equivalence, specification mining, active automata learning, program synthesis, conformance testing, differential testing, refinement, verified compilation, strangler migrations, digital twins, software archaeology, and socio-technical modernization.

## The Legacy System Is Evidence, Not Its Own Constitution

### Public orientation

Model-first legacy migration reconstructs a bounded behavioral model before selecting a successor realization. It separates observed behavior, intended obligation, relied-upon accident, defect, environment dependency, and authorized change. A descriptive model becomes normative only through adjudication; neither the running binary nor the extracted model decides by itself what must continue.

### Adversarial tests

1. **Observation-intention attack.** Frequently observed behavior is treated as intended law, while rare or unobserved obligations disappear.
2. **Golden-master attack.** Exact output comparison preserves known defects, unstable ordering, obsolete constraints, unsafe behavior, or environment accidents.
3. **Coverage-closure attack.** Tests, traces, static analysis, interviews, and production logs are treated as complete over unreachable, secret, temporal, concurrent, or failure paths.
4. **Model-oracle attack.** The extracted representation is treated as correct because it is formal, executable, or internally consistent.
5. **Stakeholder-erasure attack.** Operators, users, downstream systems, regulators, and affected people are represented only through machine-observable behavior.
6. **Equivalence-profile attack.** A successor passes declared observers while violating performance, timing, resource, security, accessibility, legal, or social obligations outside them.
7. **Cutover-irreversibility attack.** Data transformation, dual writes, external integrations, or organizational change make rollback impossible despite a nominal plan.
8. **Modernization-overreach attack.** A bounded migration result is generalized into automatic substrate independence, composability, durable knowledge recovery, or general program understanding.

### Claim and evidence ceiling

The paper offers an obligation-reconstruction architecture and capability thesis. It does not solve program equivalence, infer intention from behavior, guarantee complete models, establish normative authority, prove substrate independence, or demonstrate successful migration, reversible cutover, reduced risk, cost advantage, or organizational benefit. Source examples remain evidence at their recorded standing.

Validation requires exact legacy custody and environment, multi-source model construction, adjudicated obligations, hidden and adversarial cases, property-specific equivalence, shadow operation, data and dependency reconciliation, rollback drills, affected-party review, and current external research. No migration or external research was performed in this pass.

### Reader-facing consequence

The practical advance is not automatic rewriting. It is making every preservation, repair, refusal, and tolerated difference visible enough that people can decide what the successor owes before code is allowed to replace the system.

## 15. Conclusion

Model-first legacy migration is promising because it changes what a migration is allowed to hide. Instead of translating an opaque implementation into a new opaque implementation, it constructs an explicit, revisioned account of behavior, obligation, authority, uncertainty, and evidence between them.

The model is not born sovereign. It begins as a descriptive candidate. It becomes normative only through adjudication, and every realization earns only bounded correspondence under declared conditions. This correction strengthens rather than weakens the original capability thesis: the goal is not a magical proof of equivalence, but an architecture in which uncertainty, disagreement, residual dependence, and failure can no longer masquerade as a successful rewrite.

If that architecture proves cheaper, safer, and more reconstructible than strong conventional migration on real systems, it would support a new generation of inspectable and substrate-independent software continuity. Until then, it is a disciplined research program with a precise burden of proof.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Publication form.** This work is retained as a standalone technical companion because its concrete migration method is useful independently; it remains subordinate to the architecture it explains.

## Corpus-Wide Reference Positioning

This paper argues that legacy migration is usually framed as translation from one implementation to another. Its nearest external comparison fields are software, open sovereign, ai. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Modularity, secure-development practice, and reproducibility reduce classes of failure but do not guarantee architectural coherence or user sovereignty. Source availability and reproducible builds improve inspectability but do not alone guarantee comprehensibility, practical exit, hardware control, or sustainable maintenance. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** David L. Parnas. "On the Criteria To Be Used in Decomposing Systems into Modules." *Communications of the ACM* 15(12), 1972, pp. 1053-1058. DOI: 10.1145/361598.361623. https://doi.org/10.1145/361598.361623 **Relationship:** Foundational modularity treatment used to compare information hiding with explicit semantic and governance interfaces.

**[E2]** Ward Cunningham. "The WyCash Portfolio Management System." *OOPSLA '92 Experience Report*, 1992. DOI: 10.1145/157709.157715. https://doi.org/10.1145/157709.157715 **Relationship:** Original technical-debt metaphor used to distinguish implementation debt from semantic debt.

**[E3]** Karen Scarfone, Murugiah Souppaya, and Donna Dodson. *Secure Software Development Framework (SSDF) Version 1.1*. NIST SP 800-218, 2022. DOI: 10.6028/NIST.SP.800-218. https://doi.org/10.6028/NIST.SP.800-218 **Relationship:** Adjacent secure-development framework for preparation, protection, production, and vulnerability response.

**[E4]** Reproducible Builds Project. *Formal Definition of Reproducible Builds*. [reproducible-builds.org source](https://reproducible-builds.org/docs/formal-definition/) **Relationship:** Adjacent reproducibility practice; byte reproduction is compared with, but not equated to, semantic or constitutional continuity.

**[E5]** Free Software Foundation. *The Free Software Definition*. https://www.gnu.org/philosophy/free-sw.html **Relationship:** Normative predecessor for user freedoms; the paper may add reconstruction, governance, or hardware-boundary obligations beyond license rights.

**[E6]** Open Source Initiative. *The Open Source Definition*. https://opensource.org/osd **Relationship:** Adjacent licensing baseline; source availability is not treated as sufficient for operational sovereignty.

**[E7]** Martin Kleppmann et al. "Local-First Software: You Own Your Data, in Spite of the Cloud." *Onward! 2019*, pp. 154-178. DOI: 10.1145/3359591.3359737. https://www.inkandswitch.com/local-first/ **Relationship:** Adjacent local-first design program relevant to user custody, offline operation, and collaboration.

### Ableman corpus

**[A1]** Adam Ableman. *Sovereign Software*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-24C6159B98023A9C`;  
source SHA-256  
`6AAFE79E438B980B75D1910A897F7BA716A10CF1187B68CB1F71405F36725A18`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Software Analysis (CSoftA): A Governance-Based Classification Method for Software Systems*. Ableman Corpus current edition; work identity `PAPER.PUB.20472196`;  
source SHA-256  
`3670B28B7C1AF5467BE4002C47B5F964F8FAF6F257125C2F84CE06904E4FD0DE`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Semantic Fragmentation and Constitutional Structure in Software Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-B307F65B51C503DE`;  
source SHA-256  
`9D2A9D79DE8BC3F2F8ABECA073E4D3607F7623F4368E63F8036081E39B4C75C3`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Governed Coding and Debugging*. Ableman Corpus current edition; work identity `PAPER.PUB.18115533`;  
source SHA-256  
`2469EDA96DBC1E207855A9AD27314A7FAB59FA35E6EFEF9288C30F949376BF16`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Constitutional Operating Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F5FB8FA82270B989`;  
source SHA-256  
`E982E4D6BD4B519EED6A7438367844954D6D5F1C2C4CC0099AAAC4AB9A00D3AB`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Jnana*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-ECEAB04A620F163D`;  
source SHA-256  
`76D921D2975BDCD25D6DFB506F5E85F7AFDBF4D2CCC65F8C45394121F9D90060`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Jnana and the Next Open Source Revolution*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-473AD6FAA1659E24`;  
source SHA-256  
`E73859FD3B4AD4F7ED80E96F93F2D5A0DCB3A2D76C5741813F878B3874D7887D`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

#### Ableman Corpus references

**[SMP]** Adam Ableman. *The Substrate Migration Principle*. Exact reviewed source:   
  `The_Substrate_Migration_Principle.md`,  
SHA-256  
`0B078CB21D7F14AD7439C605CF532D88306C94E6202A133EE4FB56DE891F36ED`.

**[GOORRT]** Adam Ableman. *GOORRT: The Governed Object-Operation-Realization Representation Triad*. Exact reviewed source:   
  `GOORRT- The Governed Object-Operation-`

`Realization Representation Triad.md`,  
SHA-256  
`152AB6781AA827519858E0BD8A1811CB1F2C08F56599CD2A61896115742D1399`.

**[CBC]** Adam Ableman. *Constraint-Bearing Composability*. Exact reviewed source:   
  `Constraint-Bearing Composability.md`,  
SHA-256  
`BEEA0B56DBF7DC5274307E95E08AF0576A9F91A729C1962765361ADA34488B62`.

**[SFA]** Adam Ableman. *Semantic Fragmentation and Constitutional Structure*. Exact corpus head SHA-256  
`4048182A492E8ED731505426801D7A89074DE7311C0B3D975ECD2A2478D845F8`; unpublished AI-assisted integrated edition, with no publication or canonical standing granted here.

**[COP]** Adam Ableman. *The Constitutional Observability Platform*. Exact corpus head SHA-256  
`15CBE49A23A34F881A06EAB32AAFD95E9468EC0B7C19F47A795A34C854DF9E84`; unpublished AI-assisted integrated edition, with no publication or canonical standing granted here.

**[RWR]** Adam Ableman. *Reasoning by Way of Receipts*. Exact corpus head SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`; unpublished AI-assisted integrated edition, with no publication or canonical standing granted here.

**[THR]** Adam Ableman. 2026. *The Three Hash Rule*. Zenodo. DOI:   
  `10.5281/zenodo.20788617`. Exact reviewed Markdown head SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.

**[SPL]** Adam Ableman. *From Content-Addressed Storage to Governed Semantic Project Lineage*. Exact corpus head SHA-256  
`E6D6B39F9443E48CEA44CA8B17681AC73E4A40A8AAD56C1E31B84D8B5DA50499`; unpublished AI-assisted integrated edition, with no publication or canonical standing granted here.

**[CBCB]** Adam Ableman. *Cold Boot Continuity as a Deployment Primitive*. Exact corpus head SHA-256  
`747CDF82833B2769317A3E63F0F6BA9D0A2CFA84C83E5A8CD72442F6E49C59F3`; unpublished AI-assisted integrated edition, with no publication or canonical standing granted here.

**[SS]** Adam Ableman. *Sovereign Software*. Exact corpus head SHA-256  
`D8A2707865C6636485A564546D91F2CCF45AAC80161B94AC56A3DA5CF2EB2C13`; unpublished AI-assisted integrated edition, with no publication or canonical standing granted here.

**[DYN]** Adam Ableman. *Dynatology*. Exact corpus head SHA-256  
`8539BBB8D636C406800A38C7EC47BE36B1EEEBFA04FAE062FF6E53137099BEFC`; unpublished AI-assisted integrated edition, with no publication or canonical standing granted here.

**[GMB]** Adam Ableman. *Governed Meaning Base (GMB)*. Current corpus terminology under the author-confirmed historical lineage `CCF -> CMB -> GMB`; this terminology ruling grants no publication, implementation, conformance, or canonical standing.

The source invokes Rice's theorem, Hyrum's Law, Lawrence Lessig, and Lon Fuller. Exact editions, page references, and the broader external literature remain to be researched and verified for a future evidence-qualified revision readiness.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Semantic Debt.* Zenodo, 2026. doi:10.5281/zenodo.21111666

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848090](https://doi.org/10.5281/zenodo.23848090)
