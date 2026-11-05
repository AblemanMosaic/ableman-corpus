# Quant Insights for ACG Systems

## Point-in-Time Admissibility, Identity, Risk, and Decay in Constitutional Computing

### A governed decision must preserve not only what is known, but what was admissibly knowable when continuation occurred.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Quantitative-finance infrastructure has developed under persistent pressure from unstable data, identity drift, time leakage, model decay, hidden constraints, implementation divergence, transaction costs, and adversarial conditions. This paper asks which of those operational disciplines transfer to Ableman Constitutional Governance (ACG): a family of systems in which continuation depends on explicit authority, admissibility, evidence, refusal, and revision.

The transfer is architectural rather than financial. Its central object is *point-in-time admissibility*: a decision should be evaluated against the evidence, identity bindings, law, schemas, authorities, and refusal conditions valid at the time of decision, without silently importing later knowledge. From that premise the paper derives bitemporal state, jurisdictional identity bindings, admission-before-computation, production refusal, cross-substrate equivalence burdens, constraint attribution, governance backtesting, decay monitoring, and a layered constitutional data plane.

The comparison has limits. Financial optimization does not supply moral legitimacy; governance harms cannot always be priced; historical replay is not causal proof; and metrics can make unmeasured people or values disappear. The paper therefore treats quant practice as a source of candidate mechanisms and failure tests, not as authority over constitutional design.

The result is a specification and research agenda. It formalizes the temporal core, locates the proposal in the realization funnel, relates it to the wider Ableman corpus, and identifies the evidence required before any claimed transfer should be treated as validated.

---

## 1. Purpose

Quantitative finance offers Ableman Constitutional Governance a mature example of what happens when decisions depend on unstable data, shifting identities, noisy evidence, adversarial environments, time-sensitive action, and post-hoc accountability.

The deepest lesson is not about trading.

The deepest lesson is that every high-stakes reasoning system eventually becomes a point-in-time governance system.

A quant stack must decide what was knowable, what was valid, what was tradable, what was constrained, what was too stale, what was too risky, what had changed, and what could still be relied upon. These are not merely financial questions. They are constitutional questions.

ACG systems can learn from quant practice because quant infrastructure has already evolved under brutal pressure:

* bad data creates false signals
* stale data creates false history
* weak identifiers create wrong joins
* hidden assumptions create model failure
* research code drifts during productionization
* constraints silently shape outcomes
* execution changes theory into consequence
* attribution must separate cause from noise
* models decay even when they once worked

ACG should absorb these lessons without becoming finance-shaped. The goal is not to imitate quant systems, but to generalize their hard-won architecture into constitutional computing.

The core insight is this:

A governed system must not merely preserve rules. It must preserve the state of admissible meaning at the moment continuation occurred.

### 1.1 Terms and Transfer Boundary

**Ableman Constitutional Governance (ACG)** denotes the corpus-level approach in which authority, jurisdiction, admissibility, evidence, refusal, effects, standing, and revision remain explicit rather than being collapsed into behavior or configuration. It is an architectural family, not one implementation.

**Quant practice** in this paper denotes operational patterns associated with point-in-time datasets, identifiers, research-to-production migration, constraints, attribution, backtesting, risk, transaction costs, and regime change. The paper does not claim that every quantitative-finance system implements every pattern well.

The transfer relation is therefore:

$$
\text{quant mechanism} \longrightarrow \text{ACG design hypothesis} \longrightarrow \text{bounded test},
$$

not

$$
\text{quant convention} \longrightarrow \text{constitutional authority}.
$$

Where the paper uses words such as *should* or *must*, they express a candidate ACG design obligation. They do not report that the obligation has already been implemented or empirically validated.

## 2. Point-in-Time Truth

One of the most valuable quant insights is point-in-time discipline.

A historical computation must not use what is known now. It must use what was admissibly known then.

This principle generalizes directly into ACG.

Any governed system that evaluates prior actions, prior claims, prior identities, or prior decisions must distinguish:

* current truth
* historical truth
* restated truth
* corrected truth
* known-at-the-time truth
* admissible-at-the-time truth

These are not the same.

A constitutional system must never silently replace historical admissibility with present knowledge. Doing so creates a form of governance leakage. It lets the future contaminate the past.

In finance, this creates look-ahead bias. In ACG, it creates constitutional anachronism.

For example, when reviewing an agent's prior decision, the system must not ask only whether the decision looks correct now. It must ask:

What evidence was admitted at that time?

What law hash was active?

What authority bindings existed?

What schemas were valid?

What identity mappings were in force?

What refusal conditions were known?

What downstream actions were permitted?

A decision can be wrong in hindsight but admissible at the time. A decision can be profitable or convenient in hindsight but constitutionally invalid at the time.

ACG should therefore make point-in-time admissibility a primitive.

A receipt should not merely say what happened. It should say under what temporal jurisdiction the happening was evaluated.

### 2.1 Bitemporal Admissibility

Let a governed record $x$ carry two temporal dimensions:

* valid time $V(x) = [v_0,v_1)$, the interval during which the record claims to describe the world; and
* transaction time $T(x) = [t_0,t_1)$, the interval during which the governance system had admitted that record.

The as-of corpus at decision time $t$ is

$$
K_t = \{x \mid t \in T(x)\}.
$$

For proposal $p$, jurisdiction $j$, and active constitutional state $C_t$, point-in-time admissibility is a typed decision

$$
A(p,K_t,C_t,j) \in \{\operatorname{ALLOW},\operatorname{REFUSE},\operatorname{DEFER}\}.
$$

`DEFER` is distinct from

`REFUSE`: it states that the current evidence or authority is insufficient for decision, not that the proposal is prohibited. A receipt for $A$ must bind at least the proposal, decision time, valid-time assumptions, admitted evidence root, governing commitments, jurisdiction, decision, and proof boundary.

Later correction produces a new transaction-time state; it does not rewrite $K_t$. Retrospective evaluation may compare the decision with later knowledge, but it must label the comparison as hindsight rather than silently altering the decision's original epistemic boundary.

### 2.2 Identity as a Jurisdictional Binding

An identity assertion is not a bare label but a tuple

$$
I = (s,n,o,j,V,a,e,r),
$$

where $s$ is naming scheme, $n$ is identifier value, $o$ is the identified object, $j$ is scope or jurisdiction, $V$ is valid interval, $a$ is asserting authority, $e$ is evidence, and $r$ is replacement/conflict policy. Two records sharing $n$ need not share $o$; two identifiers naming $o$ need not be interchangeable across $j$ or $V$.

This formalizes the paper's identity rule and connects it to Semantic Custody: artifact identity, logical-work identity, version-family identity, publication identity, and concept identity remain separately governed even when a workflow links them.

## 3. Identity Is Not a Label

Quant systems learn quickly that identifiers are treacherous.

Tickers change. Companies merge. Securities split. Vendors disagree. Internal IDs drift. A single apparent object may refer to different entities across time. Multiple identifiers may refer to the same entity under different schemes. A naive join can poison the entire system.

ACG should generalize this lesson:

No identifier is self-authorizing.

A label is not an identity. A name is not an authority. A reference is not a binding. A hash is not a full semantic claim unless its jurisdiction is declared.

Every governed system needs identity receipts.

For ACG, identity should be treated as a time-bound, authority-bound, scope-bound claim:

* what object is being identified
* by which naming scheme
* under which authority
* within which valid interval
* for which domain of use
* with which confidence or proof
* with which conflict policy
* with which replacement or retirement rule

This applies far beyond finance.

In MCIR, an artifact identity must not collapse source identity, build identity, semantic identity, runtime identity, and publication identity into one string.

In Jnana, a knowledge object must not collapse citation, concept, claim, evidence bundle, and interpretive frame into one reference.

In agent systems, a user instruction, system policy, memory item, tool result, and external claim must each carry distinct identity jurisdiction.

The quant lesson is severe: bad identity does not stay local. It propagates downstream until it becomes false reasoning.

## 4. Data Admission Before Computation

Quant systems do not merely compute over data. They fight to determine whether the data deserves to be computed over.

ACG should treat this as a central architectural rule:

Computation must be downstream of admission.

A system should not ask, "Can I process this input?" before asking, "Is this input authorized to participate in this process?"

Data admission should include:

* source authority
* schema validity
* freshness
* completeness
* internal consistency
* conflict with prior state
* conflict with other sources
* scope of permitted use
* downstream dependency impact
* refusal conditions

This matters for all ACG systems.

A constitutional agent should not summarize a document unless the document's identity, source, version, and relevance have been admitted.

A governance engine should not evaluate a claim unless its evidence bundle is admissible.

A build system should not compile an artifact unless its source, dependency graph, compiler, and policy state are admitted.

A receipt system should not accept a receipt merely because the receipt is well-formed. It must ask whether the receipt is authorized, fresh, non-replayed, and jurisdictionally valid.

The quant pattern is clear:

Availability is not admissibility.

In ACG, this becomes law.

## 5. Refusal as a Production Feature

Quant systems often halt factors, quarantine data, block trades, suspend signals, or trigger human review when upstream conditions fail.

This is directly aligned with ACG's refusal discipline.

The key insight from quant practice is that refusal must be operationally normal. It cannot be treated as an embarrassing exception. If a system only knows how to continue, it will eventually continue through poison.

ACG should design refusal as a first-class production feature:

* refusal receipts
* refusal codes
* refusal propagation
* refusal dashboards
* refusal recovery paths
* refusal replay
* refusal attribution
* refusal retirement triggers

A refusal should answer:

What was refused?

Why was it refused?

Which predicate failed?

Which authority made the refusal?

Which downstream systems were blocked?

What evidence would be required to admit later?

Was this refusal protective, excessive, stale, or contested?

This is where quant practice gives ACG a practical posture. In high-stakes domains, "no action" is not absence. It is often the most important action the system takes.

A good constitutional system does not merely execute lawful continuations. It preserves the right to stop.

## 6. Research and Production Must Remain Distinct

Quant teams often allow exploratory research to happen in flexible environments, then impose stricter gates before production deployment.

ACG should preserve this distinction.

Not every thought needs full constitutional ceremony. Not every sketch, hypothesis, draft, notebook, prototype, or local experiment should be treated as production law. Exploration requires looseness. Production requires admission.

The danger is phase confusion.

A research artifact may be suggestive but not admissible. A prototype may be useful but not authoritative. A local experiment may demonstrate possibility but not justify deployment. A passing test may support confidence but not prove semantic closure.

ACG systems should therefore maintain clear phase boundaries:

* exploration
* hypothesis
* specification
* implementation
* validation
* admission
* production
* monitoring
* retirement

Quant systems teach that the handoff between research and production is one of the most dangerous zones in the stack. Meaning can drift when a model moves from notebook to service, from small data to distributed computation, from one language to another, or from batch mode to live execution.

ACG should treat every such migration as a constitutional event.

## 7. Substrate Equivalence as a General Requirement

Quant practice often involves translating research logic across substrates: R, Python, Spark, KDB, C++, databases, streaming systems, and portfolio engines.

The ACG generalization is powerful:

Whenever meaning moves across substrate, equivalence must be witnessed.

This applies to:

* Python to C
* notebook to production service
* natural language policy to machine-readable law
* semantic specification to executable gate
* receipt schema to database table
* local test to distributed runtime
* one model provider to another
* human review to automated admission
* old ontology to revised ontology

The system must ask:

What meaning is supposed to be preserved?

What differences are tolerated?

What edge cases were tested?

What state was replayed?

What output changed?

What change is explainable?

What change violates the semantic contract?

This is not merely software testing. It is constitutional migration control.

In MCIR terms, every substrate migration should produce an equivalence claim. In Jnana terms, every transformation of knowledge representation should preserve traceable semantic custody.

Quant systems make this obvious because a tiny implementation difference can alter portfolio weights, trades, risk, and performance. ACG systems should assume the same danger anywhere executable meaning moves.

## 8. Constraints Are Law, Not Configuration

Quant optimizers reveal a crucial truth: constraints shape reality.

A portfolio is not built from alpha alone. It is built from alpha filtered through risk, costs, liquidity, leverage, turnover, exposure, concentration, mandate, and operational constraints.

ACG should generalize this insight:

Constraints are not secondary settings. They are governing law.

In many systems, constraints hide in configuration files, environment variables, prompts, tool wrappers, thresholds, schemas, validators, defaults, and informal procedures. But if a constraint determines what continuations are possible, it is part of the constitution whether or not anyone names it.

ACG systems should therefore elevate constraints into explicit governance objects.

Each constraint should have:

* identity
* scope
* authority
* rationale
* active interval
* enforcement mechanism
* override rule
* interaction with other constraints
* receipt obligations
* retirement condition

This matters because hidden constraints produce hidden causality.

If an agent refuses an action, did it refuse because of law, missing evidence, tool limitation, policy conflict, risk threshold, malformed input, stale memory, or implementation failure?

If a system produces an output, did it do so freely, or because constraints silently narrowed the field?

Quant attribution teaches ACG that downstream outcomes cannot be explained without knowing which constraints bound the decision.

## 9. Attribution as Governance Memory

Quant systems use attribution to explain performance: what worked, what failed, what exposure mattered, what cost intervened, what risk dominated, what signal decayed.

ACG should treat attribution as governance memory.

Every consequential outcome should be explainable through its admitted causes:

* what input was admitted
* what transformation occurred
* what constraints bound
* what refusal did or did not happen
* what authority permitted continuation
* what state changed
* what downstream effect followed
* what alternative was blocked
* what evidence supports the explanation

The point is not to narrate after the fact. The point is to preserve causal reconstructability.

A constitutional system without attribution becomes mythic. It may have receipts, but no living account of how those receipts produced consequence.

Quant systems also warn against lazy attribution. A bad outcome may be blamed on a model when the real cause was data. A factor may be blamed for underperformance when constraints prevented expression. A trade may be blamed on execution when the optimizer generated an unstable target. A human may be blamed when the system gave them poisoned evidence.

ACG should therefore make attribution jurisdictional.

Each explanation must identify what kind of cause is being claimed:

* data cause
* identity cause
* semantic cause
* model cause
* constraint cause
* execution cause
* authority cause
* environment cause
* decay cause
* refusal cause

This would make ACG systems not only auditable, but intelligible.

## 10. Model Decay and Constitutional Decay

Quant systems understand that models decay.

A strategy can work, then weaken. A factor can become crowded. A signal can disappear. A data source can degrade. A market regime can change. A cost model can become stale. A risk model can lose calibration.

ACG should extend this into the idea of constitutional decay.

A law, policy, schema, ontology, classifier, validator, prompt, memory rule, refusal predicate, or authority registry may be valid at one time and inadequate later.

The system should not assume that once-admitted governance remains eternally sound.

Constitutional artifacts need monitoring:

* Is the predicate still catching the intended failure mode?
* Is the schema still expressive enough?
* Has the environment changed?
* Are refusals increasing unexpectedly?
* Are overrides increasing?
* Are downstream systems routing around the rule?
* Are stale rules blocking legitimate continuations?
* Are new risks outside the current constitution?
* Has semantic drift accumulated?

Quant practice suggests that every governance object should carry a decay profile or review condition.

Some rules are stable. Some are experimental. Some are emergency patches. Some are domain-specific. Some depend on external law. Some depend on evolving model behavior. Some should expire unless renewed.

ACG should therefore distinguish permanent constitutional commitments from provisional operating constraints.

Not every rule deserves immortality.

## 11. Backtesting for Governance

Quant systems test strategies against historical data. ACG can adapt this idea into governance backtesting.

A governance backtest asks:

If this constitution had been active over prior events, what would it have admitted, refused, flagged, escalated, or misclassified?

This can be applied to:

* refusal predicates
* evidence gates
* authority rules
* schema migrations
* identity matching policies
* agent tool-use policies
* receipt validation systems
* semantic equivalence checks
* memory admission rules
* publication rules

Governance backtesting would reveal:

* false refusals
* missed violations
* fragile predicates
* overbroad gates
* under-specified authorities
* costly escalations
* hidden dependency failures
* brittle schemas
* replay gaps
* ungoverned edge cases

This is especially important because a constitution that sounds good in prose may fail under event history.

Quant systems teach that intuition is not enough. A rule must be tested against paths.

ACG should therefore develop scenario libraries, adversarial event histories, replay packs, and constitutional stress tests.

The goal is not to prove perfection. The goal is to discover how the constitution behaves under pressure before the world does.

## 12. Risk Models for Governance Systems

Quant systems do not merely estimate return. They estimate risk: exposure, covariance, concentration, drawdown, leverage, liquidity, tail events, and unintended bets.

ACG systems need analogous risk models.

Governance risk is not only the risk that a rule is violated. It includes the risk that the system becomes unable to detect, explain, refuse, recover, or renegotiate.

An ACG risk model might track:

* authority concentration
* schema fragility
* receipt coverage gaps
* semantic drift
* validator disagreement
* refusal-rate anomalies
* override frequency
* dependency opacity
* replay incompleteness
* source monoculture
* identity ambiguity
* policy conflict density
* substrate migration exposure
* stale memory reliance
* untested edge-case surface

This is one of the richest quant-to-ACG transfers.

A portfolio manager asks:

Where are my hidden exposures?

An ACG system should ask:

Where are my hidden governance dependencies?

A system may appear healthy while relying too heavily on one authority, one schema, one model, one database, one validator, one interpretation layer, or one unexamined assumption.

Risk modeling turns governance from static rule compliance into dynamic exposure management.

## 13. Transaction Costs and Governance Costs

Quant systems know that theoretical alpha can be destroyed by transaction costs.

ACG systems need the parallel concept of governance costs.

Every receipt, validation, refusal, replay, equivalence check, audit, and escalation has cost. Too little governance permits poison. Too much governance suffocates continuation.

The problem is not to maximize governance indiscriminately. The problem is to allocate governance where it changes admissibility.

ACG should therefore distinguish:

* cheap checks
* expensive checks
* hot-path checks
* cold-path checks
* precomputed checks
* sampled checks
* mandatory gates
* advisory warnings
* escalation triggers
* post-hoc reconciliation

The quant lesson is that friction matters. A system with beautiful governance that cannot operate will be routed around. A system with no governance will act blindly. The mature design is layered.

For example:

* hot path: minimal sufficient admission
* warm path: enriched validation
* cold path: full replay and audit
* exception path: human or higher-authority review
* retirement path: revoke stale rules or artifacts

This allows ACG to remain practical without surrendering its constitutional discipline.

## 14. Live State Versus Historical Memory

Quant architecture distinguishes live trading systems from historical research systems. Both matter, but they serve different temporal functions.

ACG should make the same distinction.

Live state answers:

What is admissible now?

Historical memory answers:

What was admissible then?

These require different substrates and different guarantees.

A live governance system needs fast access to current authority, identity, policy, schema, and refusal state. A historical governance system needs durable replay, versioned evidence, time travel, and reconstructable lineage.

The architectural implication is clear:

* hot state for current admissibility
* cold memory for replay and audit
* bridge layer for as-of reconstruction
* semantic layer for meaning preservation
* receipt layer for authority transitions

This prevents a common error: treating the latest database state as if it were the whole truth.

A constitutional system must remember not only what is true now, but what was authorized before the truth changed.

## 15. Alternative Data and Epistemic Contamination

Quant systems ingest alternative data: web data, satellite data, credit card data, shipping data, sentiment data, employment data, and many other strange signals. These sources create immense epistemic risk.

ACG should study this carefully because agentic systems face a similar problem.

Modern AI systems ingest tool outputs, user memory, web results, retrieved documents, model-generated summaries, embeddings, logs, transcripts, and inferred preferences. These are all alternative data streams.

The quant lesson is that exotic data can create hidden leakage, legal risk, identity ambiguity, survivorship bias, privacy risk, and false precision.

ACG should therefore apply stricter admission to high-entropy data sources:

* Where did the data come from?
* What does it actually measure?
* What does it pretend to measure?
* What populations are missing?
* What time delay exists?
* What legal or ethical limits apply?
* What transformations occurred before arrival?
* What incentives shaped its production?
* What would make it invalid?
* What downstream claims may rely on it?

This is especially relevant to Jnana. Knowledge systems must not confuse signal density with truth. A large corpus can still be jurisdictionally weak.

## 16. Portfolio Thinking for Constitutional Systems

A quant portfolio is a collection of exposures. ACG can borrow portfolio thinking to manage constitutional architecture.

A governance system should not rely on a single defense. It should maintain a diversified control portfolio:

* schema validation
* authority verification
* semantic hashing
* state hashing
* replay
* cross-substrate equivalence
* refusal receipts
* anomaly detection
* human review
* adversarial tests
* version pinning
* provenance checks
* lineage graphs
* decay monitoring
* independent rebuilds

Each control has strengths, weaknesses, costs, and correlations. Some fail together. Some cover the same surface. Some create false confidence. Some are cheap but shallow. Some are deep but expensive.

Portfolio thinking asks:

Where is the system overexposed?

Where is it under-hedged?

Which controls are correlated?

Which risks are unpriced?

Which checks produce actual admissibility value?

Which checks are theater?

This is valuable for ACG because constitutional systems can become overconfident in a favorite mechanism. Hashing is powerful, but not enough. Receipts are powerful, but not enough. Human review is powerful, but not enough. Formal schemas are powerful, but not enough.

A mature system needs a balanced governance portfolio.

## 17. Stress, Regime Change, and Constitutional Robustness

Quant systems are judged not only in normal markets, but under stress: crashes, liquidity shocks, volatility spikes, correlations going to one, broken assumptions, missing data, and adversarial conditions.

ACG systems need equivalent stress regimes.

A constitution should be tested under:

* missing evidence
* conflicting authorities
* stale schemas
* malicious receipts
* replay attacks
* model disagreement
* tool failure
* partial outages
* overloaded validators
* ambiguous user instructions
* adversarial prompts
* corrupted memory
* dependency compromise
* high-speed decision pressure
* emergency override conditions

The question is not whether the system behaves beautifully when all inputs are clean. The question is whether it preserves constitutional shape when continuation becomes difficult.

Quant systems teach that many models die when assumptions synchronize against them. ACG systems should therefore test correlated failure:

What happens when identity, freshness, and authority all become uncertain at once?

What happens when the system must act quickly but evidence is incomplete?

What happens when refusing everything causes harm, but admitting weak evidence causes different harm?

These are not edge cases. They are constitutional weather.

### 17.1 Limits and Negative Transfer Tests

Quant-to-governance transfer fails when a mechanism imports assumptions that constitutional systems must reject. The following are explicit negative tests:

* **Metric capture:** a measurable proxy replaces an unmeasured right, person, or value.
* **Optimization legitimacy:** improved aggregate performance is treated as authority to impose a distribution of harms.
* **Backtest certainty:** historical fit is treated as causal proof or future reliability.
* **Stationarity assumption:** a rule validated in one regime is carried into another without detecting the change.
* **Liquidity analogy:** reversibility in a market is confused with reversibility of social, legal, or physical effects.
* **Risk commensuration:** distinct harms are forced into one scalar risk score and thereby made substitutable.
* **Data entitlement:** availability of a data stream is treated as permission to collect, retain, infer from, or act on it.
* **Survivorship governance:** only successful continuations remain visible, while refusals, abandoned paths, and harmed populations disappear from evaluation.
* **Speed priority:** latency pressure is allowed to erase non-bypassable authority or safety obligations.
* **Control correlation:** several checks derived from the same model or source are counted as independent assurance.

A proposed transfer is admissible only if its test can expose these failures and if its claim remains bounded to the configuration actually tested.

## 18. From Alpha to Admissible Advantage

Quant systems search for alpha: a signal that improves expected outcome.

ACG systems should search for admissible advantage: a way to improve continuation without violating governance.

This distinction matters.

An AI agent may find a shortcut. A database may allow a faster write path. A model may infer missing data. A tool may produce a plausible answer. A user may request an action that would be convenient. None of these is automatically admissible.

ACG should treat every advantage as suspect until governed.

The quant discipline asks:

Is this signal real, or is it leakage?

ACG asks:

Is this continuation lawful, or is it semantic leakage?

This creates a powerful parallel:

* alpha can be fake because it uses future data
* governance can be fake because it uses future justification
* alpha can be fake because identifiers are wrong
* governance can be fake because authority is misbound
* alpha can be fake because transaction costs are ignored
* governance can be fake because enforcement costs are ignored
* alpha can decay
* governance can decay
* alpha requires attribution
* governance requires attribution

The bridge is not metaphorical. It is structural.

## 19. Practical Import for MCIR and Jnana

For MCIR, quant insights imply that every intermediate representation should carry temporal, identity, and authority context.

An MCIR object should not only describe what it is. It should describe when it was admissible, under which law, with which dependencies, and through which transformation lineage.

MCIR should therefore support:

* point-in-time replay
* substrate equivalence claims
* valid-time identity bindings
* transformation receipts
* refusal states
* semantic drift detection
* authority-scoped hashes
* decay and retirement metadata

For Jnana, quant insights imply that knowledge must be treated like a live portfolio of claims, not a static library.

A knowledge system should track:

* claim authority
* evidence freshness
* source disagreement
* identity ambiguity
* conceptual drift
* citation decay
* restatement events
* confidence changes
* downstream reliance
* retirement or supersession

Jnana should be able to answer:

What did this knowledge object mean when it was admitted?

What does it mean now?

What changed?

Who or what had authority to change it?

Which downstream claims relied on the old version?

Should those claims be replayed?

This is the quant point-in-time problem generalized into semantic memory.

### 19.1 Connections Across the Ableman Corpus

| This paper | Corpus relation |
|---|---|
| Point-in-time admissibility | Extends Constitutional Computation and Epistemic Situational Awareness with explicit temporal state. |
| Time- and authority-bound identity | Applies Semantic Custody's separation of artifacts, works, versions, publications, and concepts. |
| Admission before computation | Operationalizes Governed Semantic Compilation and the CM1-to-CM2 preference boundary. |
| Typed refusal | Connects refusal semantics to Reasoning by Way of Receipts and Receipt-Bound Capabilities. |
| Cross-substrate equivalence | Supplies a temporal and evidentiary profile for MCIR and constraint-bearing compilation. |
| State/admissibility/meaning separation | Uses the independent commitments of The Three Hash Rule. |
| Live state and historical memory | Profiles Governed Context and Memory plus the Hyperpedia/crystallized meaning-base architecture. |
| Risk and decay | Adds monitoring and revision triggers to constitutional governance rather than assuming permanent adequacy. |

These relations do not merge the named systems. They specify where the quant-derived discipline supplies a reusable profile or missing dimension.

## 20. Design Pattern: The Constitutional Data Plane

A quant-inspired ACG system can be organized around a constitutional data plane.

The data plane should not merely move bytes. It should move admitted state.

Core components:

1. **Ingress gate**
   Validates source, schema, freshness, authority, and completeness.

2. **Identity resolver**
   Resolves entity bindings, valid intervals, conflicts, and scope.

3. **Snapshot registry**
   Preserves point-in-time admitted state.

4. **Transformation ledger**
   Records semantic transformations, implementation versions, and input-output hashes.

5. **Equivalence harness**
   Tests substrate migrations and semantic preservation.

6. **Constraint engine**
   Applies active law, policy, risk limits, and refusal predicates.

7. **Hot-path state store**
   Answers current and as-of admissibility questions quickly.

8. **Cold-path receipt lake**
   Preserves durable, replayable, versioned evidence.

9. **Attribution engine**
   Explains outcomes through admitted causes.

10. **Decay monitor**
    Detects when models, rules, schemas, identities, or authorities lose reliability.

This is the infrastructure ACG needs if it is to govern real systems rather than only describe governance in principle.

### 20.1 Realization Funnel for a Constitutional Data Plane

| Stage | Required work |
|---|---|
| Possibility | Consider quant-derived mechanisms without treating finance as constitutional authority. |
| Specification | Define bitemporal records, identity bindings, typed admission, receipts, attribution classes, decay triggers, and risk surfaces. |
| CM1 | Enumerate permissible designs, including strict, permissive, centralized, federated, cheap, expensive, safe, unsafe, and intentionally minimal realizations. |
| CM2 | Prefer configurations that preserve non-substitution, privacy, point-in-time replay, explicit ignorance, independent assurance, and bounded costs. |
| Instance Configuration | Fix one domain, data schema, authority model, latency budget, threat model, tests, and stopping rules. |
| Implementation Realization | Build the configured ingress, identity, state, transformation, constraint, receipt, attribution, and decay services. |
| Evidence | Run historical replay, forward shadow operation, adversarial cases, cost measurement, and subgroup/harm analysis. |
| Revision | Update rules, models, identities, and confidence while preserving prior temporal state and dependent claims. |

This paper reaches Specification and supplies CM1/CM2 criteria. It does not define one complete Instance Configuration or validate a production realization.

## Temporal Evidence and Risk Evaluation Profile

The completed P1 corpus positions Quant Insights for ACG Systems as the **temporal evidence, leakage-control, decay, stress, and governance-cost evaluation profile for constitutional agentic systems**. It transfers selected point-in-time and backtesting disciplines from quantitative practice without asserting that constitutional governance is a financial portfolio or that financial success validates governance.

- **Adjacent work:** *From CI/CD to ACG: From Tests to Courts in Agentic Software Development*  
  **Supplies:** The constitutional development, adjudication, effect, and evidence lifecycle.  
  **Quant-profile boundary:** This paper supplies temporal and risk evaluation methods for that lifecycle.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed evidence carriers and evaluation envelopes.  
  **Quant-profile boundary:** Point-in-time rules constrain which witnesses were available and admissible at decision time.

- **Adjacent work:** *Epistemic Lineage Engine*  
  **Supplies:** Source, transformation, decision, and revision lineage.  
  **Quant-profile boundary:** Lineage makes vintages and later corrections reconstructable; it does not remove leakage by itself.

- **Adjacent work:** *Constitutional Epistemology Under Adversarial Semantic Pressure*  
  **Supplies:** Threats from omission, manipulation, correlated evidence, and valid-looking records.  
  **Quant-profile boundary:** The quant profile supplies temporal and stress tests for some adversarial pathways.

- **Adjacent work:** *What Software Systems Actually Receipt, Govern, and Hide*  
  **Supplies:** Visibility and governance gaps in ordinary systems.  
  **Quant-profile boundary:** The data-plane profile exposes which live and historical surfaces were actually observed.

A governance evaluation should bind:

$$
\begin{aligned}
Q= (&decision\_time, knowledge\_time, data\_vintage, \\
&identity\_regime, policy\_version, model\_version, costs, \\
&outcome, witnesses, revision)
\end{aligned}.
$$

Event time, observation time, availability time, admission time, decision time, effect time, and later correction time are separate. A backtest may use only the identities, data, policies, costs, and capabilities admissibly available at the simulated decision time. Later knowledge belongs in revision analysis, not the original decision record.

Financial analogies remain bounded. Alpha, portfolio, decay, regime, and transaction-cost language becomes useful only when translated into explicit governance variables and failure tests. A metric that predicts an outcome can still be inadmissible, manipulable, unjustified, or too costly. Risk aggregation cannot compensate for non-compensatory constitutional constraints.

The universal GSM can type `OBSERVED_AT_TIME`, `AVAILABLE_AT_TIME`, `ADMITTED_AT_TIME`,  
`DECIDED_AT_TIME`, `EFFECTED_AT_TIME`, `KNOWN_UNDER_VINTAGE`, `BACKTESTED_WITHOUT_LEAKAGE`,  
`DECAYS_UNDER_REGIME`, `STRESSED_BY_SCENARIO`, `INCURS_GOVERNANCE_COST`,  
and   
`REVISED_AFTER_LATE_DATA`. These relations make temporal validity inspectable.

This integration establishes four editorial commitments: adopt temporal evidence/risk evaluation profile as the official corpus role; adopt the bitemporal evaluation envelope; require leakage-free policy/model/identity/data vintages; and treat financial vocabulary as a translated heuristic rather than proof of general governance laws.

## Point-in-Time Analytics, Orientation, and Conformance

The fixed-seed comparison with Semantic Field Analysis, the GMB, Operational ESA, and AFS turns point-in-time discipline into a reusable evaluation chain:

$$
\begin{aligned}
Q^*= (&GMB\_snapshot, AFS\_profile, data\_vintage, \\
&identity\_regime, policy\_version, analysis\_run, \\
&operational\_capsule, decision, effect, late\_evidence, \\
&revision)
\end{aligned}.
$$

SFA diagnostics must use the projection, identities, standing, parameters, and evidence admissibly available at the simulated decision time. GMB queries preserve the historical cut and distinguish later correction from original knowledge. Operational ESA records the live goal, custody, environment, conflicts, unknowns, and stop conditions without rewriting the historical decision basis.

AFS may specify schemas and conformance obligations for temporal evidence, orientation capsules, and evaluation records. A conforming artifact does not prove that its timestamps are accurate, its identity regime is correct, its witnesses are independent, or its decision was justified.

Late evidence produces a revision episode and possibly a new standing decision; it does not leak backward into the original backtest. The universal GSM can type   
`CONFORMS_TO_TEMPORAL_EVIDENCE_PROFILE`,  
`ANALYZED_AT_DECISION_CUT`, `QUERIED_FROM_HISTORICAL_GMB`, `ORIENTED_BY_LIVE_ESA`,  
`RECEIVES_LATE_EVIDENCE`, `REVISES_WITHOUT_TEMPORAL_LEAKAGE`,  
and   
`WITHHOLDS_CONFORMANCE_AS_TRUTH`.

This randomized review establishes four editorial commitments: adopt the combined temporal chain; bind SFA and GMB views to decision-time knowledge; distinguish live ESA from historical state; and keep AFS conformance below evidentiary validity.

## A Temporal Evaluation Profile, Not a Financial Governance Model

One retained downstream use, ACG for Quants, applies the paper's point-in-time discipline to a full quant lifecycle. The bounded search found no other material downstream dependency. The transferable contribution is therefore a temporal evidence, leakage-control, decay, stress, and governance-cost evaluation profile, not a claim that constitutional systems are portfolios or that financial success validates governance.

$$
\begin{aligned}
Q^*= (&subject, decision\_time, event\_time, observation\_time, \\
&availability\_time, admission\_time, effect\_time, \\
&correction\_time, data\_vintage, identity\_regime, \\
&policy\_version, model\_version, witnesses, costs, \\
&outcome, stress\_profile, decay, late\_evidence, \\
&revision)
\end{aligned}.
$$

Historical replay may use only the data, identities, authorities, policies, models, capabilities, costs, and witnesses admissibly available at the simulated decision time. Later correction produces revision and possibly changed standing; it does not leak backward into the original information set. A conforming timestamp schema does not prove clock accuracy, source availability, identity correctness, witness independence, or justified decision.

Alpha, portfolio, regime, backtest, decay, attribution, and transaction-cost language is useful only after translation into explicit governance variables and negative-transfer tests. Risk aggregation cannot compensate for a noncompensatory constitutional floor. Live value, historical explanatory value, and authority to continue require different evidence.

The universal GSM can type   
`BINDS_GOVERNANCE_DECISION_TIME`, `AVAILABLE_AT_TIME`,  
`ADMITTED_AT_TIME`, `KNOWN_UNDER_VINTAGE`, `BACKTESTED_WITHOUT_LEAKAGE`,  
`STRESSED_UNDER_REGIME`, `DECAYS_UNDER_PROFILE`, `INCURS_GOVERNANCE_COST`,  
`RECEIVES_LATE_EVIDENCE`, and   
`REVISES_WITHOUT_TEMPORAL_REWRITE`.

This review establishes four editorial commitments: retain temporal evaluation-profile standing; adopt the complete multi-time record; prohibit late-data leakage and unqualified financial analogy; and require accuracy, identity, independence, cost, stress, decay, and noncompensatory-floor evidence separately.

## Point-in-Time Governance Without Finance-Shaped Universality

### Public orientation

Quant Insights transfers selected disciplines from quantitative systems into high-stakes reasoning: point-in-time data, identity resolution, snapshots, transformation lineage, constraints, attribution, and decay. The general contribution is temporal evaluation. It is not a claim that governance should be modeled as finance or that financial methods transfer without loss.

### Adversarial tests

1. **Future-leakage attack.** A later fact enters a reconstruction of what was knowable at decision time. Every source, transform, and constraint needs effective time and observation time.
2. **Identity-revision attack.** An entity is renamed, merged, split, or corrected after a decision. Point-in-time identity and later successor knowledge must coexist.
3. **Snapshot-incompleteness attack.** A snapshot omits unavailable, rejected, or off-platform information. Completeness remains source- and boundary-relative.
4. **Attribution-as-causality attack.** A decomposition is presented as why an outcome occurred. Attribution is model-relative unless causal methodology is justified.
5. **Decay-metric attack.** Age or performance change is treated as universal epistemic decay. Decay must be claim-, domain-, and evidence-specific.
6. **Risk-translation attack.** Financial risk language obscures ethical, legal, physical, or social consequence. Domain-native harms and authority must remain primary.
7. **Storage-as-governance attack.** Hot/cold tiers or databases are treated as policy. Storage location does not confer standing, retention authority, or relevance.
8. **Negative-transfer attack.** Competitive optimization, probabilistic assumptions, or market metaphors distort a non-financial domain. Every transfer needs explicit disanalogies and stopping rules.

### Claim and evidence ceiling

The paper contributes a temporal evidence and risk-evaluation profile. It does not establish a financial governance model, trading insight, causal attribution, universal decay law, or suitability for a concrete high-stakes domain.

Claims about quantitative finance, databases, temporal reasoning, risk, decisions, or cross-domain outcomes require external sources and domain evaluation. Internal corpus integration establishes architectural portability questions only. No external research was added in this pass.

### Reader-facing consequence

The accessible result is that a consequential decision should preserve what was actually available, identifiable, constrained, and authorized at the time - not silently judge the past with future knowledge.

## 21. The Deeper Lesson

Quant systems live in a world where reality does not hold still.

Data changes. Entities change. Markets change. Models change. Costs change. Constraints change. What worked yesterday may fail tomorrow. What looked true historically may have been unknowable at the time. What appears to be a clean signal may be leakage. What appears to be a bad model may be bad data. What appears to be discretion may be hidden constraint.

ACG systems live in the same kind of world.

The constitutional mistake is to imagine governance as a static rulebook standing above motion.

The quant insight is that governance must itself be dynamic, temporal, testable, replayable, and humble before drift.

A mature ACG system should therefore behave less like a static rulebook and more like a governed, replayable state machine:

Every claim has a timestamp.

Every identity has a jurisdiction.

Every transformation has a receipt.

Every constraint has authority.

Every refusal has a reason.

Every migration has an equivalence burden.

Every model has a decay horizon.

Every outcome deserves attribution.

Every continuation must earn admission.

That is the gift quant systems offer ACG: not a financial metaphor, but an operational discipline for governing meaning under pressure.

ACG gives quant systems constitutional closure.

Quant systems give ACG temporal realism.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm2.** The present paper does not claim a complete cm2 treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Instance Configuration.** The present paper does not claim a complete instance configuration treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that quantitative-finance infrastructure has developed under persistent pressure from unstable data, identity drift, time leakage, model decay, hidden constraints, implementation divergence, transaction costs, and adversarial conditions. Its nearest external comparison fields are markets, governance, formal. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Optimization can make a chosen objective efficient while preserving a bad objective, missing distributional harms, strategic behavior, or inadmissible states. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Harry Markowitz. "Portfolio Selection." *The Journal of Finance* 7(1), 1952, pp. 77-91. DOI: 10.1111/j.1540-6261.1952.tb01525.x. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x **Relationship:** Predecessor risk-return optimization model; included to distinguish scalar optimization from governance-aware admissibility.

**[E2]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E3]** U.S. Department of the Treasury. *Tax Expenditures*. Office of Tax Analysis. [home.treasury.gov source](https://home.treasury.gov/policy-issues/tax-policy/tax-expenditures) **Relationship:** Primary official baseline for the definition and estimation limits of U.S. federal tax expenditures.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E6]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E7]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

### Ableman corpus

**[A1]** Adam Ableman. *Constitutional Markets*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1D49CCBB6E47B403`;  
source SHA-256  
`BB97EAC6F1861C2ED17DC0E0B75D47B04716E7FF3E3AC2A9B2F6CABCC67A5250`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *ACG for Quants*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-8A19CB4C1BD55BCA`;  
source SHA-256  
`2FEA83087B8DA79472BBA449C9D5B252B6DBA67C2EAF0DF41C206B1B0EEEF254`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Governance Incentive Engineering*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-294436DA22D85E3A`;  
source SHA-256  
`30B4151092AA9C1157214B00B695BD39A137C010DFE3BC631A64073F946ACD4A`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Beneficiary-Resolved Tax Expenditure Governance*. Ableman Corpus current edition; work identity `PAPER.PUB.20602489`;  
source SHA-256  
`C9DFFC852939E257E3EA6CDE9C474707FA1BEE300360C6D402B5E91F2999C52A`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

Adam Ableman. *Constitutional Computation*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20624488.

Adam Ableman. *Epistemic Situational Awareness (ESA): A Phenomenological Control Property of Governed Reasoning Systems*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18121270.

Adam Ableman. *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18453681.

Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18601631.

Adam Ableman. *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18633797.

Adam Ableman. *Semantic Custody*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20300952.

Adam Ableman. *The Three Hash Rule*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20788617.

Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

This revision does not yet contain the external quantitative-finance, bitemporal-database, model-risk, backtesting, market-microstructure, or data-governance literature needed to support its transfer claims. A publication candidate requires a source-by-source external review. The internal corpus references establish the receiving architecture; they do not validate the quant analogies.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Epistemic Situational Awareness (ESA): A Phenomenological Control Property of Governed Reasoning Systems.* Zenodo, 2026. doi:10.5281/zenodo.18121270

Adam Ableman *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI.* Zenodo, 2026. doi:10.5281/zenodo.18633797

Adam Ableman *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality.* Zenodo, 2026. doi:10.5281/zenodo.18601631

Adam Ableman *Semantic Custody.* Zenodo, 2026. doi:10.5281/zenodo.20300952

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848108](https://doi.org/10.5281/zenodo.23848108)
