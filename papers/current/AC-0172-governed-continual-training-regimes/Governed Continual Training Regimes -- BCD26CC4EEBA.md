# Governed Continual Training Regimes

## Freshness, Forgetting, and Admissible Model Evolution in Hybrid Semantic Compiler Systems

### Do Not Put the World in the Weights

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Governed Continual Training Regimes (GCTR) is a framework for changing models, adapters, routers, semantic substrate, and deployment standing without treating evolution as an ambient side effect of optimization. It extends Governed Training Regimes from admissible parameter transitions to admissible evolution of a model participant inside a living semantic system.

The central design heuristic is: **do not put the changing world in the weights when an inspectable, updateable substrate can carry it.** Current facts, sources, warrants, registries, and revocations normally belong in governed substrate. Bounded behavioral adaptations may belong in adapters or routing policy. General participant competence may require periodic consolidation. Recurrent frontier maneuvers may be crystallized into deterministic semantic operations. This is a routing presumption, not a literal prohibition: base models inevitably encode world regularities, and a single event may require coordinated changes across several layers.

GCTR trains a model to be a better semantic scout: to retrieve, offload, challenge, refuse, preserve evidence boundaries, propose candidate structure, and recognize missing closure. It does not make a model, receipt, scorecard, benchmark, or crystallization process sovereign. Model evolution remains a governed transition with declared authority, scope, evidence, privacy, rollback, standing, temporal validity, and revision.

This revision makes the operative vocabulary explicit; separates target state from governance history; expands the formal system state beyond model parameters; treats hot, warm, cool, and cold freshness as non-exclusive routing profiles; adds layer-specific forgetting claims; binds receipts to limited proof roles; integrates the universal GSM and realization funnel; and supplies countertests and open editorial questions. No external literature verification, training, evaluation, or implementation was performed.

## Source, Evidence, and Standing

This is an AI-prepared successor revision candidate derived from one exact author manuscript. Its custody manifest is   
`work/paper-saturation-v1/evidence/governed-`

`continual-training-regimes/integration-`  
`custody-manifest.v0.1.json`,  
SHA-256  
`3078EA1AA1C0DB5CEE2FB61C79A2BCB23C091D37F8912A8F2413474AF99FE30B`. The exact source remains unchanged.

The GCTR architecture, voice, principal distinctions, examples, appendices, cited methods, and bibliography are author material. The revised formalisms, definitions, invariants, claim boundaries, corpus bridges, countertests, and decisions are AI editorial or synthetic contributions until adopted by the author.

No cited technology, paper, benchmark, empirical result, or implementation claim was externally checked. No private chain of thought is required or presumed collectable. No model or data mutation occurred. Nothing here grants canonical standing, approves a training dataset, authorizes surveillance or trace retention, promotes a checkpoint, admits a GSM, or authorizes implementation or publication.

## 1. Problem and Bounded Thesis

Long-lived AI systems face at least four different problems that ordinary parameter optimization tends to collapse:

1. **World freshness:** active facts, sources, rules, warrants, and project state change.
2. **Participant competence:** the model must improve at retrieval, refusal, evidence handling, tool use, and frontier detection.
3. **Governed forgetting:** a fact, authority, trace, adapter, behavior, lineage dependency, or parameter influence may need to be retired.
4. **Crystallization:** recurring frontier work may deserve conversion into inspectable deterministic substrate.

GCTR claims that these changes should be routed and promoted through an explicit constitutional process. It does not claim that every change is governable by one formalism, that weights can contain no knowledge, that substrate is automatically correct, or that governance eliminates empirical uncertainty.

The claim ladder is:

1. **Conceptual claim:** model evolution can be decomposed into typed, governable update proposals.
2. **Specification claim:** those proposals can carry authority, scope, evidence, refusal, rollback, and standing obligations.
3. **Engineering claim:** a concrete GCTR realization improves freshness, forgetting, boundary behavior, or recoverability under named tests.
4. **Institutional claim:** the realization produces better long-run social or constitutional outcomes than alternatives.

This paper substantially advances Layers 1 and 2. Layers 3 and 4 require implementations, baselines, evidence, and independent challenge.

## 2. Definitions and Primitives

**Model participant.** A base model together with active adapters, routing behavior, tool interfaces, and deployment standing.

**Governed substrate.** Inspectable semantic artifacts and operations, including GMB entries, GSMs, current heads, registries, source bindings, receipts, policies, and deterministic compilers.

**Freshness event.** A discovered change that may require one or more substrate, adapter, router, checkpoint, lineage, evaluation, or standing updates.

**Governed semantic trajectory.** A public, inspectable sequence of requests, retrieved artifacts, declared commitments, operations, decisions, effects, evidence, and receipts. It is not private mental activity or hidden model reasoning.

**Update proposal.** A typed candidate mutation with target, jurisdiction, warrant, expected effect, evidence plan, rollback plan, and claim boundary.

**Admissibility membrane.** The policy and mechanism that permits, refuses, escalates, or gaps an update proposal.

**Promotion.** A separate governed act assigning an artifact or participant a deployment or semantic standing after evaluation.

**Crystallization.** Admission of a recurring frontier maneuver into governed deterministic substrate.

**Decrystallization.** Demotion, quarantine, supersession, or retirement of substrate whose closure conditions no longer hold.

**Rot test.** A repeatable challenge intended to expose staleness, authority drift, projection collapse, verifier co-drift, or counterexamples.

**Receipt.** A durable binding among a declared event, relevant identities, authority, decision, effect, evidence, and claim boundary. A receipt makes a bounded account inspectable; its existence alone does not prove truth, validity, sufficiency, or correct gate participation.

**Gap certificate.** A typed record that an update cannot yet be admitted because required representation, authority, evidence, privacy protection, or lowering is missing.

## 3. Governing State and Transition Semantics

The source models a participant as base parameters, adapters, routing policy, and standing. GCTR requires a wider system state:

$$
X_t=(M_t,\Sigma_t,\Lambda_t,\Pi_t,E_t),
$$

where $M_t$ is the model participant, $\Sigma_t$ the governed semantic substrate, $\Lambda_t$ the data and dependency lineage, $\Pi_t$ the active authority, privacy, and jurisdictional policy, and $E_t$ the evaluation and verifier configuration. Governance history is separate:

$$
Z_t=(X_t,H_t),
$$

where $H_t$ is the append-only or otherwise governed history of proposals, decisions, receipts, contests, and revisions.

An update proposal is:

$$
\Delta_t=(k_t,\tau_t,w_t,q_t,b_t),
$$

where $k_t$ names the target layer or layers, $\tau_t$ the proposed mutation, $w_t$ the warrant and scope, $q_t$ the required evidence and claim boundary, and $b_t$ the rollback or recovery plan.

The membrane returns:

$$
\begin{aligned}
\mathcal{G}(Z_t,\Delta_t)\in\{&\mathrm{ALLOW}, \mathrm{REFUSE}, \mathrm{ESCALATE}, \\
&\mathrm{GAP}\}
\end{aligned}.
$$

If allowed, an authorized transition function produces the candidate successor and a receipt:

$$
(X_{t+1},r_t)=\mathcal{T}(X_t,\Delta_t).
$$

If refused, escalated, or gapped, the protected target state need not change, but governance history does:

$$
X_{t+1}=X_t,\qquad H_{t+1}=H_t\oplus r_t.
$$

This distinction repairs the misleading idea that a refused operation produces no state change at all. It may leave the model or substrate unchanged while producing a refusal, escalation, or gap record. The formalism remains a specification candidate, not an implemented state machine or proof of enforcement.

## 4. Freshness Routing Profiles

The source's hot, warm, cool, and cold categories are useful if treated as routing profiles rather than a total ordering or exclusive partition.

- **Profile:** Hot  
  **Default target:** governed substrate  
  **Typical content:** current facts, sources, warrants, policies, heads  
  **Primary risk:** stale or unauthorized retrieval

- **Profile:** Warm  
  **Default target:** bounded adapter or router  
  **Typical content:** local behavior, jurisdiction, tool discipline  
  **Primary risk:** scope leakage and composition conflict

- **Profile:** Cool  
  **Default target:** consolidated participant competence  
  **Typical content:** general refusal, evidence, offload, and frontier skills  
  **Primary risk:** catastrophic or constitutional forgetting

- **Profile:** Cold  
  **Default target:** deterministic substrate  
  **Typical content:** stable operations, schemas, tests, refusal classes  
  **Primary risk:** premature crystallization and hidden authority

The labels do not imply that cold changes occur least often, that substrate is inherently safer, or that one event has only one destination. Revoking a data source may require a current-head change, training-lineage review, adapter rollback, evaluation update, and possibly parameter unlearning.

A routing function therefore returns a set of candidate changes:

$$
\rho(e_t, Z_t)\subseteq
\{\Sigma,A,R,\theta,\Lambda,E,S\},
$$

not one automatically correct layer. The GCTR membrane then evaluates each proposed change and their composition.

## 5. Primitives, Invariants, and Dimensions

The architecture depends on these invariants:

1. **Warrant before mutation:** no protected update is admitted without active authority for its target and effect.
2. **Standing bounded by evidence:** evaluation or receipt scope limits every downstream claim.
3. **No recurrence-to-truth shortcut:** frequency is candidate evidence, not correctness, desirability, or authority.
4. **Layer-declared forgetting:** every forgetting claim names the affected layer and the influence it does and does not remove.
5. **Target/history separation:** refusal may preserve the target while extending governance history.
6. **Scope-preserving adaptation:** adapters and routers remain jurisdiction-bound under composition, ordering, and fallback.
7. **Current-head discipline:** active sources and warrants are resolved through declared current-head rules rather than model fluency.
8. **Rollback and contestability:** promotion carries a recovery route, contest surface, and temporal review condition.
9. **Safety and rights before optimization:** non-tradeable constraints are not displaced by utility or cost-of-closure scoring.
10. **Public commitment sufficiency:** training may use public commitments and receipted actions without requiring hidden reasoning traces.
11. **Provenance preservation:** source, model, adapter, dataset, evaluator, policy, and predecessor identities remain reconstructable to the declared claim boundary.
12. **Crystallization remains revocable:** admitted substrate is not oracle truth and remains exposed to rot tests and decrystallization.

Every update should be located along at least these dimensions: target layer; temporal horizon; semantic object; authority and jurisdiction; privacy and consent; evidence status; reversibility; blast radius; dependency composition; deployment standing; and cost of closure. These dimensions are orthogonal enough that a single temperature label cannot replace them.

## 6. Governed Semantic Trajectories

The training unit should be richer than prompt-response pairs. A trajectory may bind the request, active profile, retrieval, source qualification, declared commitments, GSOL operation, decision, refusal or gap, tool effect, evidence, human contest, receipt, and later revision.

The training target is not stylistic imitation of receipts. It is competent participation:

- retrieve active rather than stale material;
- use deterministic closure when it exists;
- identify missing or defective closure;
- preserve claims and nonclaims;
- refuse or escalate under missing authority or evidence;
- challenge substrate without treating challenge as admission;
- propose candidate models, tests, and relations without granting them standing; and
- disclose projection loss when semantic objects become prose.

Trace eligibility must be checked before mining as well as before training. Privacy, consent, jurisdiction, retention, source authority, sensitive content, and synthetic origin are admission conditions. Permissive candidate detection cannot mean indiscriminate collection.

## 7. Crystallization Without an Oracle

The phrase **crystallization oracle problem** names an epistemic and governance difficulty. This revision does not claim a formal undecidability theorem. No recurrence statistic, model, reviewer, benchmark, or committee can be presumed infallible or self-authorizing.

A bounded workflow is:

1. admit eligible traces for the declared mining purpose;
2. detect recurring maneuvers across sufficiently diverse contexts;
3. extract a candidate with roles, relations, invariants, refusals, nonclaims, tests, and authority needs;
4. compare the candidate against existing GSM and system identities to avoid restatement;
5. validate positive, negative, adversarial, projection, lineage, and rot cases;
6. measure usefulness and cost without trading away mandatory constraints;
7. obtain an authorized ADMIT, REFUSE, QUARANTINE, or GAP decision;
8. bind the decision and its claim ceiling in a receipt; and
9. monitor the admitted object for decrystallization.

Crystallization must distinguish schema, algorithm, service realization, assurance claim, and foundational primitive. A new name is not evidence of a new identity. A repeated model maneuver may be a useful profile of existing machinery rather than a new system.

## 8. Forgetting and Unlearning

Forgetting is a family of operations, not a binary model property.

- **Substrate retirement** stops an object from being active while preserving permitted historical lineage.
- **Adapter or router rollback** removes bounded behavior or routing policy.
- **Training-lineage removal** identifies affected shards, synthetic descendants, adapters, evaluations, and checkpoints.
- **Behavioral correction** reduces an unwanted response pattern without claiming erasure of a specific datum.
- **Parameter unlearning** attempts to reduce a datum's influence in weights and requires its own definition and verification.
- **Standing demotion** removes deployment authority even when the artifact remains available for study.

No operation may be called unlearning merely because a document disappeared from retrieval. The claim must state what access, influence, behavior, artifact, or authority was removed; what test supports the claim; and what residual pathways remain.

## 9. Receipts, Evidence, and Promotion

GCTR depends on Reasoning by Way of Receipts, but must retain a strict boundary:

```text
receipt existence != correct gate participation
gate participation != sufficient evidence
evaluation success != deployment authority
promotion != permanent truth
```

For a training or crystallization event, a receipt should bind at least the proposal identity, predecessor identity, target and scope, active warrant and policy, input/data manifest, model and adapter identity, evaluator and criteria, result kind, observed effects, evidence references, claim boundary, successor identity, and rollback route.

A Three-Hash-style custody profile may bind predecessor, governed work order or candidate, and successor/result. It is useful for reconstruction but does not establish semantic correctness without appropriate verification. Independent checks, causal ablations, held-out tests, adversarial cases, and human or institutional review remain separate proof obligations.

Promotion is therefore its own operation. Training completion, metric improvement, or receipt production does not automatically promote a checkpoint, adapter, router, dataset, or GSM.

## 10. Evaluation and Causal Claims

The source's evaluation suite is retained and strengthened by four obligations.

First, **matched baselines** must compare GCTR with simpler retrieval, ordinary fine-tuning, adapter-only, policy-only, and no-change controls where applicable.

Second, **ablation** must separate gains caused by the model update from gains caused by substrate, routing, evaluator, prompt, dataset, or policy changes.

Third, **negative capability tests** must measure not only task success but refusal correctness, evidence boundaries, current-head use, privacy, scope leakage, substrate challenge, decrystallization, and recovery.

Fourth, **cost and latency** must include curation, review, storage, verification, contest, rollback, and long-run rot maintenance. Cost-of-closure can guide preference among admissible options; it cannot override mandatory authority, privacy, safety, or rights constraints.

The evidence ladder should proceed from specification review, deterministic schema checks, trace replay, offline evaluation, adversarial and privacy testing, bounded shadow operation, reversible pilot, and independent reproduction. Each stage grants only its declared standing.

## 11. Corpus Integration and Universal GSM

GCTR is an integrative bridge rather than a replacement for its dependencies:

- **Governed Training Regimes** supplies admissible optimizer, update, and promotion transitions.
- **Hybrid Semantic Compiler Architectures** supplies the fuzzy-frontier and deterministic-substrate division of labor.
- **GSOL** supplies typed operation, refusal, effect, receipt, standing, and lowering surfaces.
- **Constitutional Intelligence** supplies the broader criterion of preserving admissible continuation.
- **Reasoning by Way of Receipts** supplies durable transition and justification structures, subject to the proof boundary above.
- **The Ableman Format Specification** supplies separation among specification, configuration, instance choice, realization, evidence, and revision.

The **Governed Meaning Base (GMB)** is the current name in the `CCF -> CMB -> GMB` lineage. GMB can carry model identities, datasets, warrants, GSMs, receipts, evaluations, dependencies, and standings; indexing them does not make them valid or active. The universal GSM represents their roles and typed relations without collapsing a paper, concept, system, implementation, or evidence record into one identity.

Key adjacencies are: GCTR extends GTR; GCTR configures HSC participant evolution; GSOL represents its governed operations; GMB carries its semantic and evidentiary objects; receipts bind its transitions; SMT tests continuity across transformations; and decrystallization connects revision back to frontier exploration. These are typed interfaces, not automatic identity mergers.

## 12. Realization Funnel

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

- **Possibility:** enumerate update targets, training architectures, forgetting mechanisms, routing schemes, and crystallization processes.
- **Specification:** define primitives, invariants, authorities, interfaces, refusal modes, evidence, privacy, and standing.
- **Configuration Manifold 1 (CM1):** retain regimes that meet mandatory authority, safety, privacy, lineage, rollback, and verification constraints.
- **Configuration Manifold 2 (CM2):** prefer among admissible regimes by effectiveness, inspectability, reversibility, cost, latency, sovereignty, and maintainability.
- **IC:** select an **Instance Constitution** or **Instance Configuration** for a particular model, domain, jurisdiction, dataset, and deployment surface. The names are interchangeable.
- **IR:** construct an **Instance Realization** or **Implementation Realization** of that selected regime. The names are interchangeable.
- **Evidence:** retain evaluation packs, failures, contests, receipts, ablations, privacy tests, and reproduction results.
- **Revision:** update or decrystallize the regime while preserving lineage and prior standing.

This paper occupies Specification and offers early CM1/CM2 criteria. Its operation sketches and prototype are design candidates, not an IC, IR, deployed training system, or implementation authorization.

## 13. Minimal Realization Candidate

A first reversible realization should avoid base-model training. It can instrument one bounded agent workflow with:

1. an exact model/adapter/router registry;
2. a small GMB and GSM profile;
3. GSOL-shaped update, refusal, gap, and promotion records;
4. current-head and source qualification rules;
5. trace eligibility and privacy gates;
6. a frozen evaluation and adversarial suite;
7. a human review queue;
8. candidate-pattern mining over admitted public trajectories;
9. quarantine-only candidate GSM output; and
10. replay, rollback, and rot-test support.

The prototype succeeds only if it produces inspectable differences from a simpler logged workflow and survives countertests. It should not admit GSMs or change model parameters by default.

## Governed Learning and Retirement Lifecycle

Across the completed P1 corpus, Governed Continual Training Regimes is the **governed learning, promotion, retirement, and decrystallization lifecycle for a layered intelligence system**. It decides which observed regularities may become retrieval objects, adapters, routing policies, evaluation fixtures, parameter updates, or retired artifacts while preserving authority, provenance, counterevidence, and reversible standing. It is not a command to put current knowledge in weights and not a claim that crystallization can be automated without judgment.

- **Adjacent work:** *Constitutional Epistemology Under Adversarial Semantic Pressure*  
  **Supplies:** Claim, source, standing, uncertainty, and adversarial-pressure discipline.  
  **GCTR boundary:** GCTR applies that discipline to learning and retirement transitions.

- **Adjacent work:** *From Content-Addressed Storage to Governed Semantic Project Lineage*  
  **Supplies:** Exact predecessors, successors, branches, projections, and reconstructability.  
  **GCTR boundary:** GCTR governs which learning artifact receives active standing and why.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed observations whose competence and scope remain explicit.  
  **GCTR boundary:** Witnesses can support an update without becoming self-authorizing labels.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Durable proposal, gate, effect, evidence, and revision records.  
  **GCTR boundary:** Receipts reconstruct a transition but do not validate the learned object.

- **Adjacent work:** *Governance as Compilation*  
  **Supplies:** Preservation, remainder, refusal, and evidence across transformations.  
  **GCTR boundary:** GCTR treats training, adapter construction, routing, and retirement as governed transformations.

A learning transition should be represented as:

$$
\begin{aligned}
L= (&observation, eligibility, target, method, authority, \\
&privacy, predecessor, change, evaluation, decision, \\
&effect, successor, residual, rollback, monitoring)
\end{aligned}.
$$

The target is part of the claim. Retrieval deletion, router rollback, adapter retirement, dataset removal, behavioral suppression, parameter unlearning, and standing demotion are different effects and require different tests. Likewise, a recurring maneuver may justify a search aid or evaluation case without justifying a new primitive, model update, or active GSM object.

The lifecycle should use a two-boundary promotion rule. First, the candidate must survive content evaluation against current corpus identity, negative cases, held-out conditions, privacy, and simpler baselines. Second, an authorized promotion act must specify where the object becomes active, for whom, under which dependencies, and with which rollback. Passing the first boundary does not silently cross the second.

The universal GSM can type   
`OBSERVES_LEARNING_SIGNAL`, `PROPOSES_CRYSTALLIZATION`,  
`TARGETS_RETRIEVAL_LAYER`, `TARGETS_ADAPTER_LAYER`, `TARGETS_PARAMETER_LAYER`,  
`CHALLENGES_EXISTING_IDENTITY`, `PROMOTES_UNDER_AUTHORITY`, `DEMOTES_STANDING`,  
`ATTEMPTS_PARAMETER_UNLEARNING`, `RETAINS_RESIDUAL_INFLUENCE`,  
and   
`DECRYSTALLIZES_AFTER_COUNTEREVIDENCE`. This gives every learning and forgetting claim a specific object and effect.

This integration establishes four editorial commitments: retain GCTR as the governed learning-and-retirement lifecycle; adopt the complete learning-transition envelope; require separate content-evaluation and authorized-promotion boundaries; and require target-specific evidence for retrieval removal, routing rollback, adapter retirement, parameter unlearning, and standing demotion.

## Enforcement-Compatible Learning with Protected Counterevidence and Exact Artifact Lineage

The fixed-seed comparison with the Integrity Enforcement Layer, the Suppression Paradox, the hydroengineering/geologic profile, and governed project-state lineage strengthens GCTR as a lifecycle for changing active intelligence without allowing the learning process to rewrite its own limits:

$$
\begin{aligned}
L^*= (&observation, eligibility, target, method, authority, \\
&protected\_counterevidence, predecessor, change, \\
&evaluation, promotion, enforcement\_compatibility, \\
&successor, rollback, retirement, residual)
\end{aligned}.
$$

IEL supplies a boundary at which a learned router, adapter, retrieval object, policy candidate, or parameter change may affect action. A training result cannot alter an IEL verifier, refusal rule, or authority boundary merely by improving an evaluation score. Material changes require a separately admitted Instance Constitution or Instance Configuration and a separately qualified Instance Realization or Implementation Realization.

The Suppression Paradox requires protected negative evidence, refusals, and affected-party constraints to remain available through authorized representations even when the underlying payload is not eligible for general training. Deletion from a training set does not prove removal from parameters, caches, derived datasets, adapters, or downstream decisions.

Governed project-state lineage binds exact dataset, model, adapter, evaluator, configuration, and receipt predecessors to each successor and rollback. The hydroengineering/geologic profile is a bounded physical-domain stress case: monitoring can propose a model revision, but site evidence, professional judgment, community or tribal governance, permits, and do-not-use constraints cannot be replaced by continual-learning confidence.

The universal GSM can type   
`PROPOSES_LEARNING_SUCCESSOR`,  
`PRESERVES_PROTECTED_COUNTEREVIDENCE`, `REQUIRES_IEL_REQUALIFICATION`,  
`DESCENDS_FROM_EXACT_LEARNING_ARTIFACT`, `RETIRES_WITH_RESIDUAL`,  
`LEARNS_FROM_PHYSICAL_MONITORING`, and   
`TRANSFERS_NO_SITE_AUTHORITY`.

This randomized review establishes four editorial commitments: adopt the enforcement-compatible learning envelope; protect counterevidence and refusal history from training erasure; bind every learned successor to exact project-state lineage; and use physical monitoring as a bounded domain stress profile without transferring site authority or evidence.

## An Under-Promoted Governed Learning Interface

No material downstream dependency on Governed Continual Training Regimes was found in the complete frozen P3 field under its title, acronym, or specific continual-training language. That absence is a result: the paper is internally integrated but not yet serving as an explicit corpus interface. Its standing should not be inflated by generic references to learning, memory, or revision.

The future interface can nevertheless be made precise without claiming use:

$$
\begin{aligned}
L^*= (&subject\_generation, candidate, data, objective, \\
&authority, target\_layer, admission, tests, \\
&counterevidence, canary, promotion, rollback, retirement, \\
&unlearning, residual\_influence, receipts, standing, \\
&successor)
\end{aligned}.
$$

`target_layer` distinguishes weights, retrieval indexes, GMB entries, context capsules, rules, tools, and runtime configuration. A change in one layer must not be described as training another. Promotion requires exact predecessor and candidate identity, data and objective custody, authority, evaluation, protected negative cases, effect observations, and a recovery path. Retirement or deletion must distinguish removal from continuing behavioral influence.

The absence of downstream use suggests a concrete authorial choice: either promote this lifecycle as the learning and retirement interface for later papers, compress it into GKL/context/governance work, or retain it as a standalone research proposal awaiting an empirical program. None of those choices is made by this pass.

The universal GSM can type   
`PROPOSES_LEARNING_TRANSITION`, `TARGETS_LEARNING_LAYER`,  
`TESTS_PROTECTED_COUNTEREVIDENCE`, `PROMOTES_MODEL_GENERATION`,  
`RETIRES_WITH_RESIDUAL_INFLUENCE`, `ROLLS_BACK_LEARNING_STATE`,  
and   
`HAS_NO_CONFIRMED_DOWNSTREAM_DEPENDENCY`.

This reverse-dependency review establishes four editorial commitments: adopt the typed learning-transition envelope; separate weights, retrieval, GMB, context, rules, tools, and configuration; make residual influence first-class; and decide whether the paper becomes a promoted corpus interface, a compressed profile, or an independent experimental program.

## 14. Counterevidence and Failure Modes

GCTR must narrow or fail where: (1) current substrate is less accurate than the model; (2) retrieval latency or availability makes the route unusable; (3) routing introduces more failures than it prevents; (4) hot/warm/cool/cold labels hide overlapping changes; (5) a supposedly bounded adapter leaks scope; (6) adapter composition order changes behavior unexpectedly; (7) governance traces collect data without valid consent; (8) receipt production becomes governance theater; (9) receipts exist but the gate never evaluated predicates; (10) evaluator and candidate co-drift; (11) the same model generates and validates its own training material without independent challenge; (12) recurrence reflects prompt convention, bias, or institutional pressure; (13) useful productive ambiguity is crystallized away; (14) decrystallization is politically or operationally blocked; (15) forgetting removes retrieval but not parameter influence; (16) an unlearning claim lacks a layer-specific definition; (17) removal breaks lawful historical or audit obligations; (18) consolidation improves task metrics while degrading refusal or evidence discipline; (19) safety or rights constraints are traded away as closure cost; (20) stale warrants remain cached; (21) rollback cannot reconstruct the predecessor; (22) private reasoning is treated as required training data; (23) public commitments are insufficiently distinguished from hidden reasoning; (24) causal attribution fails because several layers changed together; (25) held-out or cross-jurisdiction behavior regresses; (26) external literature claims do not survive source verification; (27) the proposal restates existing HSC, GTR, GSOL, or GMB machinery under a new label; (28) governance overhead exceeds benefit for the bounded use case; (29) a stronger simple baseline matches outcomes; or (30) the framework cannot specify what evidence would promote, refuse, or decrystallize a candidate.

## Govern the Learning Lifecycle, Not Just the Checkpoint

### Public orientation

Governed Continual Training Regimes asks how a model can learn, be evaluated, promoted, rolled back, retired, or decrystallized under explicit authority and evidence. The key contribution is lifecycle separation: changing parameters, changing operational standing, and claiming that influence was removed are different events.

### Adversarial tests

1. **False-unlearning attack.** A record says material was removed while residual influence remains. Deletion, exclusion from future training, parameter unlearning, behavioral suppression, and legal disposition are distinct claims.
2. **Promotion-gaming attack.** A candidate overfits the admission suite or exploits evaluator blind spots. Evaluation versions, holdouts, red-team surfaces, and unaudited remainder must be bound.
3. **Evaluator-drift attack.** The promotion standard changes across generations. Comparisons require linked policy epochs and explicit non-comparability where warranted.
4. **Data-poisoning and provenance attack.** Admitted data carries malicious, mislabeled, unauthorized, duplicated, or synthetic influence. Data identity, license, consent, standing, and transformation lineage remain separate.
5. **Catastrophic-forgetting attack.** New admissible behavior erases protected capability or safety constraints. Promotion requires regression and obligation-carriage evidence.
6. **Rollback illusion.** Restoring an earlier checkpoint does not restore external state, caches, downstream derivatives, user effects, or revoked secrets. Recovery must enumerate remainder.
7. **Receipt-as-causality attack.** A complete training receipt is treated as proof that a datum caused or did not cause an output. Causal claims require intervention or other justified methodology.

### Claim and evidence ceiling

The paper specifies a governed learning and promotion architecture. It does not yet prove effective unlearning, reduced harm, improved robustness, lower cost, privacy protection, or causal attribution. Those claims require explicit datasets, baselines, metrics, interventions, environments, and independent evaluation.

Internal corpus relations establish how learning governance composes with receipts, GMB state, artifact lineage, and admissibility. They do not supply empirical machine-learning evidence. No external research was added in this pass.

### Reader-facing consequence

The public promise is that a model update should have the same inspectable questions as any other consequential change: who authorized it, what changed, what evidence justified promotion, what obligations survived, what can be reversed, and what remains in the world after rollback.

## 16. Conclusion

GCTR's strongest contribution is not a new training algorithm. It is a constitutional decomposition of model evolution. World updates, participant learning, forgetting, and crystallization have different targets, authorities, evidence burdens, and failure modes. Treating all of them as "training" hides those differences.

The framework remains provisional. It does not show that a particular model should be trained, that a candidate dataset is admissible, that machine unlearning succeeded, or that a crystallized GSM is correct. It provides the structure required to ask and receipt those questions without confusing proposal, execution, evidence, promotion, and standing.

Train the scout. Govern the world. Receipt the change.

## Author-Supplied Reference Note

The source manuscript includes references concerning retrieval-augmented generation, low-rank adaptation, catastrophic forgetting, machine unlearning, ontology engineering, knowledge extraction, graph constraints, Constitutional Intelligence, GSOL, GTR, and HSC. These remain author-supplied references and descriptions. They were preserved by exact source custody and were not externally verified in this pass.

## Corpus-Wide Reference Positioning

This paper argues that governed Continual Training Regimes (GCTR) is a framework for changing models, adapters, routers, semantic substrate, and deployment standing without treating evolution as an ambient side effect of optimization. Its nearest external comparison fields are ai, provenance, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[A4]** Adam Ableman. *Retrieval-Augmented Reasoning under Constitutional Constraints*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-384489D4604BEC4D`;  
source SHA-256  
`133DA35C0F27F35BAA1F53DFEE415068AD2D24FF713F8CDAFA2FDC8F748AC15C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Split-Authority AI Coordination*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-35D1BAECD5CB17AD`;  
source SHA-256  
`06FB6133170879FA8308684F0DA33F5813EAF3B5488291C2D7D234BEB6FDFEC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

Adam Ableman *Hybrid Semantic Compiler Architectures.* Zenodo, 2026. doi:10.5281/zenodo.21228038

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847872](https://doi.org/10.5281/zenodo.23847872)
