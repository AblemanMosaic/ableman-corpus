# ACG for Quants

## Point-in-Time Identity, Admissibility, Constraint, Effect, and Attribution Across the Quant Lifecycle

### A quantitative signal may exist without being admissible to become a position, order, or explanation.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Quantitative-finance systems do more than compute. They admit data, bind time-varying identities, transform evidence, test hypotheses, migrate research into production, construct constrained portfolios, authorize market effects, and explain outcomes. Each transition carries an implicit constitution: source and licensing rules, point-in-time requirements, leakage controls, risk and mandate limits, model approvals, execution authority, and retirement conditions.

This paper applies **Ableman Constitutional Governance (ACG)** to that lifecycle. ACG is the corpus-level architectural family in which authority, jurisdiction, identity, admissibility, evidence, refusal, effects, standing, and revision remain explicit. It does not replace econometrics, optimization, market microstructure, model-risk management, security controls, regulation, or professional judgment. It makes their authority and dependency relations inspectable.

The governing principle is **admissibility before consequential reliance**. A file, mapping, factor, backtest, forecast, portfolio, or order proposal does not gain standing merely by existing. It is evaluated for a declared purpose, time, jurisdiction, authority, evidence state, and effect class. Valid outcomes include admission, bounded admission, hold, and refusal. Refusal is not automatically an outage; in high-stakes systems, it can be the correct continuation.

The paper develops point-in-time identity governance, bitemporal data admission, a Factor Semantic Specification, cross-substrate equivalence claims, constitutional portfolio construction, pre-admitted execution envelopes, factor-authority retirement, and bounded attribution. It distinguishes decision receipts from proof of data truth, causal explanation, legal compliance, optimality, or market effect. It also maps the proposal through Possibility, Specification, CM1, CM2, Instance Configuration, Implementation Realization, Evidence, and Revision.

This is a conceptual architecture and research agenda, not investment advice, a trading strategy, a compliance determination, or evidence that an implementation improves returns or reduces risk. External financial, legal, technical, and empirical review remains required for a future evidence-qualified revision or use in a consequential trading system.

## 1. The Quant Stack Is Already a Governance System

A conventional shorthand is:

```text
data -> research -> factors -> risk model -> optimizer -> orders ->
fills -> attribution
```

That diagram hides the decisions that allow each arrow. A vendor delivery is selected and licensed. A record is matched to an entity. A field is interpreted under a schema. A historical observation is judged available at a past decision time. A research result is promoted. A production implementation is accepted as equivalent enough. A portfolio is selected from a feasible set. An order is authorized under live conditions. An attribution claim is accepted as an explanation.

ACG renders those transitions explicitly:

```text
candidate claim
  -> identity and temporal binding
  -> evidence and authority evaluation
  -> typed admissibility disposition
  -> semantic transformation
  -> constrained continuation
  -> consequential effect request
  -> outcome observation
  -> attribution, decay review, and revision
```

The change is not merely more logging. It separates the things that logs often collapse: availability from admissibility, identifier from identity, backtest from evidence, model score from authority, optimizer result from authorized portfolio, order submission from market effect, and performance decomposition from causal explanation.

## 2. Nine Jurisdictions

A mature quant process is a federation of partially independent jurisdictions.

1. **Data jurisdiction:** which sources, fields, schemas, licenses, timestamps, quality conditions, and uses are permitted?
2. **Identity jurisdiction:** which issuer, security, listing, share class, contract, portfolio, account, or counterparty does a record denote, over which interval and under which authority?
3. **Semantic jurisdiction:** what does a field, transformation, feature, factor, forecast, exposure, or risk measure mean?
4. **Research jurisdiction:** which hypotheses, datasets, horizons, leakage controls, multiple-testing corrections, and evaluation standards apply?
5. **Production jurisdiction:** which exact implementation, dependencies, environment, data contract, and operating envelope are admitted?
6. **Portfolio jurisdiction:** which target holdings are admissible under objective, risk, liquidity, cost, mandate, legal, tax, concentration, and operational constraints?
7. **Execution jurisdiction:** which orders may be created, sized, routed, delayed, cancelled, or refused under current conditions?
8. **Attribution jurisdiction:** which supported decomposition or causal claim may explain an outcome?
9. **Retirement jurisdiction:** when does a source, mapping, factor, model, limit, implementation, or authority lose standing?

These boundaries are not necessarily organizational departments. They are semantic and authority boundaries. One service may realize several; one jurisdiction may span several systems. The requirement is that a claim granted in one jurisdiction does not silently inherit standing in another.

## 3. Admissibility Before Consequential Reliance

Let $x$ be a candidate object, $p$ its proposed purpose, $j$ the relevant jurisdiction, $t$ the decision time, $e$ the effect class, and $E_t$ the evidence state admissible at that time. Define:

$$
\begin{aligned}
\mathcal{A}(x,p,j,t,e,E_t) \in \{&\operatorname{ADMIT}, \operatorname{BOUNDED}, \\
&\operatorname{HOLD}, \operatorname{REFUSE}\}
\end{aligned}.
$$

The central rule is:

$$
\begin{aligned}
&\mathcal{A}(x,p,j,t,e,E_t) \notin \{\operatorname{ADMIT},\operatorname{BOUNDED}\} \\
&\Rightarrow  \\
&\ne g\operatorname{ConsequentialReliance}(x,p,j,t,e)
\end{aligned}.
$$

`ADMIT` grants only the named standing.

`BOUNDED` may permit research but not production, quotation but not a join, signal calculation but not order generation, or monitoring but not capital allocation. `HOLD` identifies missing evidence or authority without pretending the claim is false. `REFUSE` identifies a conflict that should not continue under the current constitution.

The rule is consequence-sensitive. Exploratory research should remain permissive enough to discover anomalies and alternatives. The threshold for a live order or regulatory report is different from the threshold for a notebook hypothesis. ACG governs promotion, not curiosity.

## 4. Point-in-Time Identity Governance

A ticker is not an entity. A CUSIP, ISIN, FIGI, vendor identifier, or internal key is not an entity either. Each is a time-bounded claim made within a naming scheme. Corporate actions, relistings, mergers, spinoffs, share-class changes, vendor corrections, and mapping policies can alter the relation.

A governed identity assertion should bind at least:

```text
IdentityAssertion
  assertion_id
  subject_identity_candidate
  external_identifier
  identifier_scheme_and_revision
  entity_type
  source_authority
  valid_time_interval
  transaction_time_interval
  confidence_or_disposition
  conflicts_and_alternatives
  override_authority
  predecessor_assertions
  affected_dependents
```

The two times matter. Valid time states when the assertion purports to describe the world. Transaction time states when the system had admitted that assertion. A historical backtest must not silently use a mapping admitted only later.

If $V(x)$ is valid time and $T(x)$ is transaction time, then the state eligible for an as-of decision at $t$ is not simply every record whose valid time contains $t$. It is the subset that the decision system had admitted by $t$ under the selected restatement policy:

$$
E_t = \{x \mid t \in V(x),\ t \in T(x),\ \mathcal{A}(x, p, j, t, e, E_t)=\operatorname{ADMIT}\}.
$$

This expression is schematic because admissibility may depend recursively on other records. A realization must define termination, conflict, and circularity rules.

## 5. Data Admission and Restatement

Statistical checks identify missingness, staleness, discontinuities, outliers, coverage changes, vendor disagreement, and distribution shift. ACG adds a typed decision and dependency consequence.

A data-admission result should say not just "bad row" but:

* which exact snapshot, partition, schema, field, and subject were evaluated;
* which rule and version applied;
* which source, license, and authority supported use;
* which evidence and comparison windows were used;
* whether the result is admitted, bounded, held, refused, superseded, or requires restatement;
* which downstream datasets, factors, portfolios, reports, and claims may be affected;
* whether later correction changes historical valid state, transaction-time knowledge, or both.

A 90 percent change in market capitalization is not self-explanatory. It may reflect price movement, share-count change, corporate action, unit error, mapping failure, stale data, or vendor correction. Each explanation changes the appropriate response and the downstream debt.

A receipt binds the decision and its inputs. It does not prove the vendor value true, the check complete, or the dependency graph exhaustive. Independent source comparison, physical or market observations, later correction, and human review may contradict it.

## 6. Research and the Factor Semantic Specification

Research may explore. Production must be admitted.

Before promotion, a factor or model should have a **Factor Semantic Specification** that distinguishes the intended economic and computational meaning from any one codebase:

* hypothesis and economic intuition;
* target, horizon, and decision use;
* universe and point-in-time membership rules;
* exact inputs, identity semantics, and availability lags;
* transformations, winsorization, normalization, neutralization, and missing-data policy;
* leakage controls and embargoes;
* training, validation, and test regimes;
* multiple-testing and selection history where relevant;
* rebalance, turnover, capacity, and decay expectations;
* risk, cost, mandate, and compliance interactions;
* known failure modes and refusal conditions;
* evidence state and unresolved alternatives.

This specification is not automatically canonical or correct. It is a reviewable meaning contract. The implementation burden is to preserve the admitted semantics closely enough for the declared use.

## 7. Research-to-Production as a Bounded Equivalence Claim

Research and production commonly use different languages, data engines, libraries, numerical types, parallelism, calendars, and execution environments. Equality on a few samples does not establish semantic equivalence.

Let $f_R$ be the research realization, $f_P$ the production realization, $S$ the Factor Semantic Specification, $X$ a versioned replay and edge-case suite, and $\Delta$ the declared tolerance and comparison relation. A bounded equivalence claim is:

$$
f_R \equiv_{S,X,\Delta} f_P.
$$

The subscript is the point. The claim holds only for the named semantics, data surface, cases, tolerances, dependencies, and environment. It may require exact equality for identifiers and classifications, numerical tolerance for floating-point outputs, rank or portfolio-impact tolerance for signals, and distributional tests for nondeterministic models.

An equivalence package should bind source and target artifacts, dependencies, environment, calendars, seeds, replay data, edge cases, known non-equivalences, comparison code, outputs, reviewer, and expiry. Hash equality of outputs is useful only where exact equality is intended; a matching digest does not explain which semantics were exercised.

## 8. Portfolio Construction as Constitutional Selection

An optimizer does not merely turn expected returns into holdings. It selects one point from a constrained set.

Let $w$ be portfolio weights, $\alpha_t$ expected returns admitted at time $t$, $\Sigma_t$ a risk model, $C_t(w,w_{prev})$ a cost model, and $g_k(w;s_t) \leq 0$ the constraints under state $s_t$. A generic selection is:

$$
w_t^* \in \arg\max_{w \in \mathcal{F}_t}
\left(
\alpha_t^\top w
- \lambda w^\top \Sigma_t w
- C_t(w,w_{prev})
\right),
$$

where

$$
\mathcal{F}_t = \{w \mid g_k(w;s_t) \leq 0\ \text{for all active } k\}.
$$

The feasible set is a constitutional surface: mandate, leverage, concentration, liquidity, borrow, turnover, exposure, legal, tax, and operational rules determine which continuations exist. CM1 is the admissible portfolio-configuration space under the bare rules. CM2 applies declared preferences among admissible configurations. The selected optimizer, parameters, data snapshots, and tolerances form the Instance Configuration for that decision.

An optimizer-decision record should bind the alpha, risk, cost, holdings, constraints, solver, objective, feasible-status result, binding limits, selected target, alternatives or sensitivity where feasible, and final authority. It does not prove global optimality, model truth, legality, or beneficial outcome unless separate evidence supports those claims.

This separation also improves attribution. A factor can be predictive while its expression is blocked by risk, liquidity, cost, or mandate. The system should not relabel every downstream loss of expression as factor failure.

## 9. Execution as Effect Governance

A target portfolio is not yet an order, and an order is not yet a market effect. Execution introduces live prices, spreads, liquidity, venue rules, account state, market impact, partial fills, cancellations, outages, and human intervention.

For latency-sensitive paths, ACG can use **pre-admitted authority envelopes**. An envelope states which instrument, account, side, size, price distance, participation, venue, time window, risk budget, and exception conditions a fast path may use. The hot path need not re-prove the entire portfolio constitution for each event, but it must remain within the envelope and emit enough information for later reconciliation.

The evidence sequence is:

```text
portfolio decision
  -> execution authority envelope
  -> order intent and admission
  -> venue or broker submission observation
  -> acknowledgement, fill, cancellation, or uncertainty
  -> holdings and cash reconciliation
  -> exception, debt, and review
```

Hot-path capture may be minimal, but post-event expansion cannot retroactively authorize an out-of-scope effect. If the fast path exceeds its authority, the system records a violation and invokes the configured containment or recovery process.

No receipt proves that a venue received an order or that a fill occurred merely because the local system says so. Broker, venue, clearing, custody, market-data, and account-state evidence have different trust and timing properties.

## 10. Storage and Computation Are Substrates, Not the Constitution

The source identifies Parquet, Delta Lake, KDB, Spark or Databricks, MCIR, and Jnana as useful components. Their architectural roles are plausible:

* columnar stores can support large evidence scans;
* versioned transactional tables can support schema control and time travel;
* time-series systems can answer low-latency as-of questions;
* distributed engines can recompute and backfill large transformations;
* obligation-carrying representations can preserve semantic and governance commitments across execution substrates.

These are candidate realizations, not requirements or endorsements. A database preserves only the state written through its instrumented paths. Time travel does not guarantee point-in-time truth. Transactionality does not establish semantic legitimacy. A fast as-of join can return the wrong entity with perfect performance. MCIR or Jnana can carry obligations only if the source-to-intermediate-to-runtime transformations preserve and test them.

The constitution belongs in the explicit identities, schemas, authorities, admissibility rules, dependency relations, effect boundaries, and evidence contracts, not in a product name.

## 11. Factor Authority, Decay, and Retirement

A factor is not simply "in production." It has bounded standing under conditions.

An authority record may depend on predictive evidence, economic rationale, data stability, implementation equivalence, crowding, capacity, risk interaction, transaction cost, drawdown, regime, monitoring, and review time. The record should name expiry and retirement triggers.

Different failures require different dispositions:

* prediction decay may reduce or remove capital;
* cost growth may change the admissible horizon or venue;
* source degradation may hold the factor despite intact research evidence;
* identity drift may require restatement;
* implementation drift may return the factor to equivalence review;
* risk mutation may restrict expression without invalidating the signal;
* rationale failure may require a stronger evidentiary reset.

Possible outcomes include continue, continue with bounded capital, quarantine, review, revalidate, restrict, retire, supersede, or retain only for historical attribution. Retirement must preserve historical lineage; deleting the factor from the current registry should not rewrite why past decisions occurred.

## 12. Attribution Is a Bounded Explanation

Attribution is governance memory, but decomposition is not automatically causation. A portfolio return can be decomposed by factor, sector, security, trade, model, constraint, and cost under a selected method. Different methods may distribute interaction terms differently.

An attribution claim should bind:

* the outcome and interval;
* exact holdings, prices, cash flows, corporate actions, and benchmark;
* admitted input and identity state;
* factor, risk, cost, optimizer, execution, and constraint revisions;
* decomposition or causal method;
* assumptions, residual, uncertainty, and alternatives;
* affected governance decisions.

A losing trade may have followed an admissible process. A profitable trade may have violated its authority or relied on contaminated data. Economic outcome and governance integrity are distinct, though both matter.

The strongest attribution test asks whether an alleged cause could have been known and acted upon at the relevant time. Explanations that use later restatements without labeling them are hindsight narratives, not point-in-time accounts.

## 13. Minimal Adoption Profile

A team can begin without replacing its whole stack. A bounded prototype can implement six linked record families:

1. **Data Admission Record:** source, snapshot, schema, license, freshness, checks, disposition, and dependents.
2. **Identity Assertion Record:** mapping, scheme, authority, bitemporal interval, conflict, and override.
3. **Factor Semantic Record:** definition, inputs, transformations, universe, horizon, evidence, and refusal conditions.
4. **Substrate Equivalence Record:** exact realizations, replay surface, tolerances, results, exceptions, and expiry.
5. **Portfolio Decision Record:** inputs, objective, constraints, solver, feasibility, sensitivity, target, and authority.
6. **Attribution and Follow-Up Record:** outcome, method, decomposition, uncertainty, competing explanations, and required revision.

They should be linked, queryable, versioned, and connected to exact source and implementation artifacts. They should not live only in notebooks, PDFs, tickets, chats, or institutional memory.

This is a prototype of record discipline, not proof of ACG conformance. The prototype still needs access control, privacy, retention, independent observation, dependency discovery, incident response, latency measurement, and human contestability.

## 14. Realization Funnel

| Stage | ACG-for-quants responsibility |
|---|---|
| Possibility | Explore signals, datasets, mappings, portfolio regimes, governance policies, and even dangerous or illegal possibilities under containment. |
| Specification | Define identities, jurisdictions, temporal semantics, dispositions, factor meanings, constraint types, effect classes, and claim ceilings. |
| CM1 | Enumerate configurations satisfying the bare specification, including strict, permissive, centralized, federated, expensive, and minimal designs. |
| CM2 | Prefer designs that reduce leakage, identity drift, hidden constraint, unbounded authority, privacy loss, irreproducibility, and catastrophic effect while preserving useful research and timely action. |
| Instance Configuration | Select exact sources, schemas, calendars, algorithms, thresholds, authorities, models, objectives, constraints, brokers, stores, monitors, and recovery rules. |
| Implementation Realization | Build and deploy exact pipelines, registries, factor engines, optimizers, order systems, evidence services, and human workflows. |
| Evidence | Run historical replay, forward shadow evaluation, mutation tests, leakage checks, equivalence suites, incident drills, performance measurement, and independent review. |
| Revision | Restate data, correct identities, update semantics, recalibrate models, change constraints, retire authority, migrate implementations, and preserve dependent history. |

This paper reaches Specification and proposes CM1/CM2 criteria and a minimal prototype. It does not define a complete trading-system Instance Configuration or validate an Implementation Realization.

## 15. Corpus Integration and the Companion Direction

This paper is the application-direction companion to *Quant Insights for ACG Systems*. That paper asks what constitutional governance can learn from quant practice. This paper asks what a quant lifecycle looks like when interpreted through ACG. Their overlapping concepts are deliberate connective tissue; their explanatory directions and audiences differ.

Other direct dependencies include:

* **Admissibility Engineering:** separates available, admissible, implemented, and evidenced surfaces.
* **The Three Hash Rule:** prevents exact state, admissibility commitments, and meaning commitments from collapsing into one digest.
* **Reasoning by Way of Receipts:** treats decision records as bounded reasoning carriers rather than proof of truth or effect.
* **Governed Semantic Project Lineage:** connects Factor Semantic Specifications to exact research and production artifacts, builds, configurations, and successors.
* **A Formal Theory of Work Custody:** identifies responsibility for data holds, model review, equivalence debt, incident repair, and retirement without confusing custody with ownership or authority.
* **The Constitutional Observability Platform:** supplies observer, verifier, evidence-health, scenario, and explicit-remainder roles for production claims.
* **GMB**, the current Governed Meaning Base in the historical `CCF -> CMB -> GMB` lineage: stores durable identities, meanings, claims, conflicts, standing, evidence, and revision relations. A purpose-specific quant context or policy projection may be compiled from GMB, but the projection is not identical to the durable state.

## Quant-Lifecycle Constitutional Application Profile

Across the completed P1 corpus, ACG for Quants is the **quant-lifecycle constitutional application profile for point-in-time data, identity, research promotion, model realization, portfolio selection, market effect, attribution, decay, and retirement**. It does not supply investment advice, performance evidence, legal compliance, or authority to trade.

- **Adjacent work:** *Quant Insights for ACG Systems*  
  **Supplies:** Lessons that agentic constitutional governance can learn from quant practice.  
  **ACG-for-Quants boundary:** This paper applies the governance architecture in the opposite direction to a quant lifecycle.

- **Adjacent work:** *Admissibility Engineering*  
  **Supplies:** Separation of possible, admissible, preferred, selected, realized, and evidenced pathways.  
  **ACG-for-Quants boundary:** The quant profile specializes those transitions to data, factors, portfolios, orders, and attribution.

- **Adjacent work:** *From Content-Addressed Storage to Governed Semantic Project Lineage*  
  **Supplies:** Exact research, build, configuration, and successor custody.  
  **ACG-for-Quants boundary:** Quant lineage additionally requires bitemporal data and restatement dependency.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Responsibility for holds, reviews, repairs, incidents, and retirement.  
  **ACG-for-Quants boundary:** Custody does not imply investment authority, ownership, or truth.

- **Adjacent work:** *The Constitutional Observability Platform*  
  **Supplies:** Observer, verifier, scenario, evidence-health, and explicit-remainder roles.  
  **ACG-for-Quants boundary:** COP can support the profile without certifying market models or live effects.

A quant decision chain should bind:

$$
\begin{aligned}
Q= (&data\_state, identity\_state, factor\_semantics, \\
&research\_evidence, promotion, realization, \\
&portfolio\_objective, constraints, target, \\
&order\_authority, execution, outcome, attribution, \\
&revision)
\end{aligned}.
$$

Point-in-time identity is not a preprocessing detail. Entity mapping, corporate action, universe membership, calendar, restatement, license, and availability determine what information and authority existed at the decision time. Research-to-production correspondence must name tolerances, numerics, dependencies, latency, market data, optimizer, and execution assumptions rather than claim implementation equality.

Factor value, admissibility, portfolio feasibility, order authority, execution quality, and post-event attribution are separate claims. Attribution explains under a declared decomposition; it does not establish cause. Model decay or regime change can demote standing without erasing the historical decision state.

The universal GSM can type   
`ADMITS_POINT_IN_TIME_DATA`, `RESOLVES_BITEMPORAL_IDENTITY`,  
`DEFINES_FACTOR_SEMANTICS`, `PROMOTES_RESEARCH_CANDIDATE`, `CLAIMS_SUBSTRATE_EQUIVALENCE`,  
`SELECTS_FEASIBLE_PORTFOLIO`, `AUTHORIZES_MARKET_EFFECT`, `OBSERVES_EXECUTION_OUTCOME`,  
`ATTRIBUTES_UNDER_MODEL`,  
and   
`RETIRES_FACTOR_AUTHORITY`. These relations make the application profile inspectable from research to retirement.

This integration establishes four editorial commitments: retain ACG for Quants as the quant-lifecycle application profile; adopt the decision-chain envelope and point-in-time identity obligations; separate factor, admissibility, feasibility, authority, effect, and attribution claims; and require external domain, legal, privacy, security, and empirical review before any publication or implementation standing.

## Research Promotion, Contained Effect, and Cross-Domain Restraint

The fixed-seed comparison with craft state-estimation research, historical CCF, Jnana, and Continuation Primacy separates useful architecture from accidental analogy:

$$
\begin{aligned}
Q^*= (&research\_PCM, data\_vintage, identity, \\
&factor\_specification, review, promotion, realization, \\
&portfolio, order\_authority, effect, outcome, \\
&attribution, retirement)
\end{aligned}.
$$

Historical crystallization can describe the reversible movement from exploratory research through extraction, stabilization, review, CM1 admission, CM2 preference, and current GMB state. It does not validate the factor or authorize trading. Jnana can provide a candidate containment architecture for representation, policy, lowering, effect mediation, receipts, and projection, subject to separate conformance evidence.

Event-driven craft research and Continuation Primacy have no direct evidentiary relation to the quant lifecycle. Shared state, viability, transition, or continuation vocabulary cannot establish market validity, factor authority, portfolio feasibility, or execution quality.

The universal GSM can type   
`CRYSTALLIZES_QUANT_RESEARCH_CANDIDATE`,  
`PROMOTES_FACTOR_UNDER_PROFILE`, `CONTAINED_BY_JNANA_CONTRACT`,  
`AUTHORIZES_MARKET_EFFECT_SEPARATELY`, `RETIRES_FACTOR_AFTER_DECAY`,  
`HAS_NO_MATERIAL_RELATION_TO_CRAFT_EVIDENCE`,  
and   
`HAS_NO_MATERIAL_RELATION_TO_CONTINUATION_`  
`THESIS`.

This randomized review establishes four editorial commitments: adopt the expanded quant transition; use historical crystallization for research posture only; treat Jnana as an optional separately evidenced containment realization; and retain explicit nonrelations to craft and Continuation Primacy.

## A Time-Indexed Consequence Chain, Not Trading Authority

Two retained downstream uses place ACG for Quants inside historical crystallization and Jnana containment. Two lexical leads from craft state estimation and continuation theory were rejected as nonrelations. The paper's corpus role is therefore a domain application profile that makes the quant lifecycle a time-indexed consequence chain; it does not supply a factor, investment recommendation, legal conclusion, or authority to trade.

$$
\begin{aligned}
Q^*= (&decision\_time, data\_vintage, availability, licenses, \\
&entity\_identity, factor\_semantics, research\_evidence, \\
&promotion, model\_head, realization, objective, \\
&constraints, portfolio, order\_authority, execution, \\
&outcome, attribution, decay, retirement, revision)
\end{aligned}.
$$

Point-in-time identity, information availability, research validity, promotion standing, portfolio feasibility, order authority, market effect, and attribution are separate claims. Restatement creates a successor data and identity state; it must not rewrite the information set under which a historical decision was made. Attribution is relative to a declared decomposition and cannot establish cause.

Historical crystallization can preserve reversible movement from research candidate to reviewed meaning and selected configuration. Jnana can be a separately evidenced containment realization. Neither validates a factor, establishes research-to-production equivalence, satisfies law, or authorizes market effect. Quant-domain competence, current primary sources, licensing, privacy, security, model risk, market microstructure, and jurisdiction-specific legal review remain external publication and implementation gates.

The universal GSM can type   
`BINDS_QUANT_DECISION_TIME`,  
`RESOLVES_POINT_IN_TIME_IDENTITY`, `PROMOTES_FACTOR_UNDER_PROFILE`,  
`SELECTS_PORTFOLIO_UNDER_CONSTRAINT`, `AUTHORIZES_ORDER_SEPARATELY`,  
`OBSERVES_MARKET_EFFECT`, `ATTRIBUTES_UNDER_DECLARED_MODEL`, `RESTATES_WITH_SUCCESSOR`,  
and   
`RETIRES_FACTOR_STANDING`.

This review establishes four editorial commitments: adopt the complete time-indexed consequence record; preserve historical information sets through restatement; separate validity, promotion, feasibility, authority, effect, and attribution; and retain external domain, legal, empirical, privacy, security, and licensing gates.

## Governed Research Is Not Trading Advice

### Public orientation

ACG for Quants applies constitutional governance to the path from data and research through portfolio decisions and market execution. It asks who may promote a hypothesis, which data and models were used, what risks and limits apply, what actually reached an execution venue, and which evidence supports the result. It does not recommend any security, strategy, portfolio, or trade.

### Adversarial tests

1. **Look-ahead attack.** Future information leaks into features, universes, labels, or preprocessing. Every dataset and transform must be time-indexed and reconstructable.
2. **Survivorship attack.** Delisted, failed, unavailable, or rejected instruments disappear from the research set. Universe construction is part of evidence.
3. **Backtest-overfit attack.** Repeated selection turns noise into apparent performance. Search history, multiple testing, holdouts, and abandoned variants require custody.
4. **Cost-and-slippage attack.** Gross simulated returns ignore spread, impact, latency, borrow, fees, capacity, and failed execution. Promotion requires execution-realistic assumptions.
5. **Model-drift attack.** A factor or risk relation changes after promotion. Standing must expire, be monitored, and support retirement or rollback.
6. **Constraint-bypass attack.** A broker, manual action, emergency path, or derived order evades portfolio or risk limits. Effect mediation must bind the actual execution route.
7. **Attribution-overclaim.** A decomposition is treated as causal explanation. Attribution is model-relative and cannot prove why a market moved.
8. **Incentive-conflict attack.** Researchers, managers, venues, or evaluators benefit from promotion or turnover. Conflicts and authority separation require disclosure.

### Claim and evidence ceiling

The paper specifies a governance profile for quantitative research and execution. It does not establish profitability, investment merit, fiduciary compliance, legal compliance, risk reduction, market robustness, or causal insight. Historical performance cannot guarantee future results.

Any empirical finance claim requires exact data rights and versions, universe construction, transformations, code, environment, search history, costs, baselines, uncertainty, out-of-sample evidence, and reproducible execution assumptions. Legal, regulatory, fiduciary, and market-structure claims require current jurisdiction-specific sources and qualified review. No external research was added in this pass.

### Reader-facing consequence

The public value is not a better trading signal. It is an auditable boundary between an idea, a tested model, an authorized portfolio decision, and an actual market effect, with the ability to refuse, reconstruct, and retire each stage.

## 16. Counterevidence and Publication Requirements

The proposal is weakened or must be revised if:

* existing model-risk, data-governance, security, compliance, and trading-control practices already provide the same outcomes with less complexity;
* receipt and approval overhead causes delays or errors larger than the failures it prevents;
* governance records expose strategies, positions, identities, or personal data beyond acceptable bounds;
* formal admissibility creates false confidence or turns uncertain expert judgment into brittle thresholds;
* the identity or dependency graph cannot be maintained accurately enough to support downstream-impact claims;
* research freedom is suppressed without a corresponding reduction in consequential risk;
* equivalence tests pass while portfolio behavior diverges under untested regimes;
* optimizer records create an illusion of explanation without sensitivity, alternative solutions, or model uncertainty;
* authority centralization makes override, recovery, or dissent unsafe;
* post-event attribution repeatedly confuses decomposition, correlation, and cause;
* live shadow trials show no measurable benefit over a simpler baseline.

Further evidentiary strengthening requires a source-by-source review of quantitative-finance data practice, bitemporal databases, entity resolution, backtesting and leakage, model-risk governance, portfolio optimization, market microstructure, execution controls, performance attribution, legal and regulatory obligations, privacy, and operational resilience. Claims must be jurisdiction- and date-scoped. Empirical examples should use licensed or reproducible data and must distinguish illustrative behavior from investment performance.

## 17. Conclusion

The ordinary quant question is whether a signal may contain useful predictive information. The constitutional question is whether that signal, in this exact identity and evidence state, may become this portfolio decision or market effect under the authorities and constraints currently in force.

Neither question replaces the other. Admissibility without economic value is not a strategy. Economic value without admissibility is not a governable system.

ACG for Quants makes the hidden constitution of the lifecycle explicit: point-in-time data and identity, factor meaning, research promotion, substrate migration, feasible-set construction, execution authority, outcome evidence, attribution, decay, and retirement. It permits exploration while demanding stronger standing for promotion and effect.

The aim is not to make finance bureaucratic or to guarantee profit, safety, legality, or truth. It is to ensure that continuation is inspectable: what was admitted, why, under whose authority, from which state, with which constraints, toward which effect, with what evidence, and subject to which revision.

A mature quant architecture needs both signal discipline and continuation discipline. Markets punish systems that cannot distinguish signal from noise. Consequential governance punishes systems that cannot distinguish an available action from an admissible one.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Revision.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that quantitative-finance systems do more than compute. Its nearest external comparison fields are markets, governance, ai. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Optimization can make a chosen objective efficient while preserving a bad objective, missing distributional harms, strategic behavior, or inadmissible states. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E7]** Patrick Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **Relationship:** Predecessor retrieval architecture; comparison centers on provenance, admission, and fail-closed constraints not supplied by retrieval alone.

### Ableman corpus

**[A1]** Adam Ableman. *Constitutional Markets*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1D49CCBB6E47B403`;  
source SHA-256  
`BB97EAC6F1861C2ED17DC0E0B75D47B04716E7FF3E3AC2A9B2F6CABCC67A5250`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Quant Insights for ACG Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-EAEEDA4A34808C9B`;  
source SHA-256  
`F668C40E0FE27BDBFDC881BFA97735D61F00335A6FC3DF9488A4BCFCFFB19631`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

Adam Ableman. *Admissibility Engineering*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *A Formal Theory of Work Custody*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *The Constitutional Observability Platform*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *From Content-Addressed Storage to Governed Semantic Project Lineage*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition in the author-confirmed historical terminology `CCF -> CMB -> GMB`; conceptual claims retain the standing stated in the work.

Adam Ableman. *Quant Insights for ACG Systems*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *The Three Hash Rule*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20788617.

External quantitative-finance, database, model-risk, optimization, execution, attribution, privacy, and legal literature remains required for a future evidence-qualified revision. The internal corpus establishes the receiving architecture; it does not validate the finance-specific claims.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

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

DOI: [10.5281/zenodo.23847366](https://doi.org/10.5281/zenodo.23847366)
