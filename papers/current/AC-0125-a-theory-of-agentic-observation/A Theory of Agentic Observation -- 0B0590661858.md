# A Theory of Agentic Observation

## Semantic Projection Interfaces, Parsimonious Observation Surfaces, and the Governance of Cognitive Bandwidth

### The cheapest token is not the compressed token, but the unobserved substrate whose address, shape, and relevance were already sufficient.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern AI systems scale primarily through larger models, longer context windows, greater retrieval bandwidth, and increasingly massive datacenter infrastructure. Yet the dominant architecture of agentic systems still assumes a primitive observation model: tools expose raw substrate directly to the model, and the model itself performs filtering, reduction, interpretation, and relevance extraction after observation has already occurred.

This paper argues that the observation surface itself is the neglected optimization layer in agentic systems.

We introduce a theory of *agentic observation*: the study of how autonomous systems transform substrate reality into cognitively consumable semantic projections. We propose that most current agentic tooling is epistemically inefficient because it emits substrate dumps rather than minimally sufficient semantic projections. This creates structural inflation of token usage, inference cost, latency, cognitive pollution, and datacenter demand.

We define the *Parsimonious Observation Surface* (POS): a tool-interface paradigm in which tools emit the minimum semantically sufficient projection necessary for the next admissible decision, while preserving explicit escalation paths into deeper substrate detail when required.

To operationalize this framework, we introduce typed Decision Classes, calibrated utility functions, Well-Formed Sufficiency, Delta-indexed minimality, Observation Contracts, Projection Calculus, Address Algebra, Escalation Graphs, Projection Normal Forms, Witness-Carrying and Proof-Carrying Projections, policy lattices, incremental observation, and observation-planning metrics.

We argue that token cost is fundamentally a bandwidth-governance problem; that long-context scaling partially masks poor interface design; that semantic projection is a more foundational optimization layer than prompt compression; and that local/edge AI systems become substantially more viable when observation bandwidth is reduced at the tool boundary rather than merely compressed after emission.

Future agentic systems will require explicit theories of observation, projection, admissibility, semantic sufficiency, calibration, uncertainty, and observation economics in order to remain computationally sustainable as AI infrastructure scales.

***

## 1. Introduction

The modern AI stack is expanding under a peculiar assumption:

> reality should be observed first, and compressed later.

This assumption permeates current agentic tooling.

A file reader emits entire files.
A grep operation emits hundreds of raw matches.
A diff operation emits full hunks before significance is established.
A test runner streams logs continuously regardless of inferential value.
A retrieval system injects giant context blocks so the model may determine relevance after the fact.

The prevailing architecture treats the model itself as the primary reduction engine.

This creates a paradox:
the more powerful the model becomes, the less pressure exists to design intelligent observation surfaces.

Long-context models become landfills with attention.

Instead of redesigning the interface between tools and cognition, the field increasingly scales:

* context windows,
* datacenters,
* inference budgets,
* retrieval pipelines,
* and memory systems.

The result is epistemic inefficiency at planetary scale.

This paper proposes an alternative direction:
not merely compressing tokens, but redesigning observation itself.

***

## 2. The Observation Problem

Agentic systems fundamentally operate by observing substrate state.

A tool invocation is an observation act.

Every tool therefore implicitly answers four questions:

1. What portion of substrate is exposed?
2. In what representation?
3. At what semantic resolution?
4. Under what escalation policy?

Current systems answer poorly.

Example:

```bash
grep -R "foo" .
```

typically emits:

* full paths,
* repeated content,
* raw line bodies,
* redundant context,
* terminal formatting,
* often hundreds or thousands of lines.

Yet most downstream agent decisions require far less.

The next decision is usually one of:

* continue,
* fetch deeper,
* branch,
* ignore,
* inspect a specific region,
* compare candidates.

The raw dump is therefore epistemically excessive.

We define this as:

### Substrate Overexposure

> the emission of substrate detail beyond the minimum semantically sufficient projection required for the next admissible cognitive transition.

Substrate overexposure creates:

* token waste,
* context pollution,
* retrieval churn,
* degraded attention allocation,
* inference amplification,
* repeated semantic filtering,
* and unnecessary infrastructure scaling.

***

## 3. Definitions and Assumptions

The theory uses the following notation consistently.

| Symbol        | Meaning                                                |
| ------------- | ------------------------------------------------------ |
| $S_u$         | underlying substrate                                   |
| $P$           | projection emitted from $S_u$                          |
| $\Delta$      | finite typed decision class                            |
| $d$           | admissible decision                                    |
| $U(d \mid P)$ | calibrated expected utility of decision $d$ under projection $P$ |
| $C(P)$        | projection cost                                        |
| $H_\Delta(P)$ | posterior entropy over decisions in $\Delta$ given $P$ |
| $\gamma(P)$   | decision margin                                        |
| $A$           | address tuple                                          |
| $G=(V,E)$     | escalation graph                                       |
| $S(P,\Delta)$ | sufficiency predicate                                  |

The framework assumes:

1. $\Delta$ is finite and typed for the relevant next-step decision.
2. $U(d \mid P)$ is estimated by calibrated predictors and periodically audited.
3. Projection functions operate over declared substrate domains with known address semantics.
4. Robustness claims require a domain-specific perturbation metric $d(S_u,S_u')$.
5. $C(P)$ is scalarized only for exposition; the canonical implementation model preserves the Pareto frontier over tokens, latency, and energy unless a policy explicitly supplies scalar weights.

These assumptions do not make POS universal.

They make it testable.

***

## 4. Decision Classes

The key observation of POS systems is that observation is always relative to a bounded next-step decision space.

We define a *Decision Class*:

$$
\Delta = \{d_1, d_2, \dots, d_n\} \tag{1}
$$

where $\Delta$ represents the finite set of admissible next cognitive transitions available to the observing agent.

Examples:

$$
\Delta_{\text{nav}} = \{\texttt{open}, \texttt{skip}, \texttt{branch}\} \tag{2}
$$

$$
\begin{aligned}
\Delta_{\text{debug}} = \{&\texttt{inspect\_file}, \texttt{compare\_versions}, \\
&\texttt{run\_tests}, \texttt{stop}\}
\end{aligned}\tag{3}
$$

POS systems target sufficiency relative to $\Delta$, not universal understanding.

The objective is not:

> fully understand substrate.

The objective is:

> support the next admissible transition with minimum observation cost.

***

## 5. Well-Formed Sufficiency

Let $S_u$ denote the underlying substrate and $P$ denote a projection emitted from that substrate.

A projection is sufficient relative to $\Delta$ when it preserves the same next admissible decision as direct substrate observation, or exposes a unique bounded escalation edge.

We define the *Sufficiency Predicate*:

$$
S(P,\Delta)=1 \tag{4}
$$

iff:

$$
\arg\max_{d\in\Delta}\mathbb{E}[U(d \mid P)] = \arg\max_{d\in\Delta}\mathbb{E}[U(d \mid S_u)] \tag{5}
$$

or there exists a unique typed escalation edge:

$$
\exists! e_i \in G \tag{6}
$$

such that $e_i$ exposes the precise additional information required to resolve the decision.

Because argmax may be unstable under ties, POS systems require a global tie-breaking rule:

* lexicographic ordering,
* prior-weighted ordering,
* or policy-defined decision precedence.

Without tie-breaking, sufficiency is not well formed.

***

## 6. Calibration of Utility

The term $U(d \mid P)$ cannot remain an informal preference estimate.

POS systems define $U(d \mid P)$ through calibrated predictors that estimate expected decision utility under projection $P$.

These predictors are evaluated using proper scoring rules such as:

* Brier score,
* log score,
* calibration error,
* regret against substrate-derived decisions.

Periodic recalibration occurs through:

* Witness-Carrying Projection audits,
* Proof-Carrying Projection verification,
* human-in-the-loop overrides,
* and retrospective substrate checks.

Calibration prevents projection systems from becoming confidently wrong.

A POS surface therefore does not merely emit compact projections.

It must learn whether its projections actually preserve decision quality.

***

## 7. $\Delta$-Indexed Minimality

POS systems seek not merely sufficient projections, but approximately minimal sufficient projections.

We define:

$$
P^*_\Delta = \arg\min_P C(P) \quad \text{s.t.} \quad S(P,\Delta)=1 \tag{7}
$$

where:

* $P^*_\Delta$ is the minimal-cost sufficient projection,
* and $C(P)$ denotes projection cost.

Tools attempt to approximate:

$$
P \approx P^*_\Delta \tag{8}
$$

and report an estimated optimality gap:

$$
\eta = \frac{C(P)}{C(P^*_\Delta)} \tag{9}
$$

Because $P^*_\Delta$ may not be directly computable, POS tools report intervals:

$$
[\eta_L, \eta_U] \tag{10}
$$

using:

* lower bounds from information-theoretic limits,
* lower bounds from decision entropy,
* lower bounds from schema constraints,
* upper bounds from achieved projection cost,
* and dual certificates from Projection Calculus.

### Proposition 1 -- Minimality Depends on Sufficiency

$P^*_\Delta$ is meaningful only after $\Delta$, $S(P,\Delta)$, calibrated $U$, and the tie-breaking rule are fixed.

Otherwise the minimization target is underdetermined.

Minimality is not "smallness."

It is minimum cost subject to decision-preserving sufficiency.

***

## 8. Information Lower Bounds

Observation cannot be reduced arbitrarily.

For a task with decision class $\Delta$, any sufficient projection must preserve enough information to distinguish relevant decision states.

A lower-bound intuition is:

$$
C(P) \ge \Omega(H(\Delta) - I(P;\Delta^\perp)) \tag{11}
$$

where:

* $H(\Delta)$ is decision uncertainty,
* $I(P;\Delta^\perp)$ represents information carried by $P$ that is irrelevant to $\Delta$.

This connects POS to Fano-style limits:
when the projection lacks enough information to distinguish decisions, error becomes unavoidable.

The sublinear observation claim is therefore bounded, not magical.

For many indexed, sketched, or topology-preserving tasks, sufficient observation may be sublinear in substrate size.

But for rare critical events, adversarial distributions, or unindexed substrates, larger observation may be required.

***

## 9. Semantic Projections

We define a *semantic projection* as:

> a bounded representation of substrate state preserving only distinctions relevant to a declared inferential purpose.

A semantic projection is not a summary.

A summary attempts to restate meaning.

A projection instead preserves:

* identity,
* location,
* shape,
* status,
* magnitude,
* relevance,
* escalation affordances,
* uncertainty bounds,
* and continuity hooks,

while deliberately suppressing irrelevant substrate detail.

Example:

Raw substrate:

```text
482 matching lines across 31 files...
```

Semantic projection:

```text
hits=482 files=31
top:
1 core/parser.py@[22,81,91]
2 runtime/env.py@[14,77]
fetch:
--file core/parser.py --range 1:120
```

The projection preserves cardinality, locality, navigation, escalation path, and inferential direction.

It suppresses redundant content, low-value line bodies, repeated context, formatting overhead, and unnecessary substrate exposure.

***

## 10. Observation Contracts as Types

POS systems require explicit contracts governing projection behavior.

We define an *Observation Contract*:

$$
\mathcal{O} = (p, \Delta, \Sigma, G) \tag{12}
$$

where:

* $p$ = inferential purpose,
* $\Delta$ = admissible decision class,
* $\Sigma$ = projection schema,
* $G=(V,E)$ = escalation graph.

Observation contracts function as types.

A tool is therefore a typed projection function:

$$
T: S_u \rightarrow P \tag{13}
$$

where $P$ must satisfy $\Sigma$, expose valid addresses, respect policies, and preserve sufficiency or escalation.

Projection contracts support variance rules over decision classes.

If:

$$
\Delta_1 \preceq \Delta_2 \tag{14}
$$

then $\Delta_1$ refines $\Delta_2$.

A projection sufficient for a refined decision class may be reused for a coarser task when policy permits.

This enables projection reuse across related agent loops.

***

## 11. The Parsimonious Observation Surface

We define the *Parsimonious Observation Surface* (POS):

> a tool-interface discipline in which tools emit the minimum semantically sufficient projection necessary for the next admissible decision, while preserving explicit escalation paths into deeper substrate layers.

POS systems are characterized by:

* address-first design,
* fetch-on-demand escalation,
* bounded default observation,
* semantic density maximization,
* inferential sufficiency targeting,
* typed projections,
* calibrated utility,
* witness or proof support,
* substrate suppression unless required,
* and explicit governance policies.

A POS tool does not answer:

> What data exists?

It answers:

> What is the smallest observation sufficient to continue reasoning coherently?

***

## 12. Governance of Observation

Observation escalation should itself be governed.

This governance loop combines entropy, margin, marginal utility, escalation edges, and policy constraints. It determines whether a projection is sufficient, whether further observation is justified, and which additional substrate edge is admissible if sufficiency has not yet been reached.

### 12.1 Decision Entropy

We define decision entropy as posterior entropy over decisions in $\Delta$ given $P$:

$$
H_\Delta(P) \tag{15}
$$

This is not entropy over projection uncertainty in general.

It is uncertainty over the admissible next decision.

POS systems enforce two-threshold hysteresis:

$$
\tau_{\text{low}} < \kappa_{\text{high}} \tag{16}
$$

with stateful gating:

* if $H_\Delta(P) \le \tau_{\text{low}}$, escalation is forbidden unless the decision margin fails;
* if $H_\Delta(P) \ge \kappa_{\text{high}}$, escalation is required;
* between thresholds, prior state is preserved.

### 12.2 Decision Margin

Sufficiency may fail even when entropy appears low.

We define the *Decision Margin*:

$$
\gamma(P) = \max_d \mathbb{E}[U(d \mid P)] - \max_{d \neq d^*} \mathbb{E}[U(d \mid P)] \tag{17}
$$

where $d^*$ is the current best decision.

If:

$$
\gamma(P) < \gamma_{\min} \tag{18}
$$

then escalation is required, even when entropy appears low.

#### Proposition 2 -- Entropy Alone Is Insufficient

Low $H_\Delta(P)$ does not guarantee robust decision sufficiency if $\gamma(P)$ is small.

A projection may concentrate probability mass while leaving the top two decisions nearly tied.

Therefore escalation governance requires both entropy and margin.

### 12.3 Marginal Utility

Observation systems should stop observing once additional substrate loses inferential value.

We define marginal utility:

$$
MU(t) = \frac{\partial U}{\partial t} \tag{19}
$$

representing expected utility gain per additional token.

POS systems enforce:

$$
MU(t) < \lambda \Rightarrow \text{stop} \tag{20}
$$

This prevents projection inflation.

### 12.4 Escalation Graphs

Observation surfaces require explicit escalation structure.

We define an *Escalation Graph*:

$$
G = (V, E) \tag{21}
$$

where nodes are projections and edges are bounded substrate expansions.

Each edge contains:

$$
\begin{aligned}
e_i = (&\text{cost}, \text{added\_info}, \text{preconditions}, \\
&\mathbb{E}[\text{IG}])
\end{aligned}\tag{22}
$$

An escalation edge is admissible iff:

1. its preconditions are checkable within $P$;
2. its cost bound is certified;
3. its policy labels are satisfiable;
4. its target projection type is known;
5. its address dependencies are resolvable.

This prevents hidden-cost escalation.

The planner selects escalation edges according to:

$$
\frac{\mathbb{E}[\text{IG}]}{C} \tag{23}
$$

subject to policy constraints and budget state.

The output of this governance loop becomes the input to incremental observation: once observation is justified, the system must decide whether to refine, reuse, delta-update, or escalate rather than simply re-read substrate.

***

## 13. Address Algebra

Address-first systems require stable address semantics.

We define an address tuple:

$$
A = (s, p, r, v, h) \tag{24}
$$

where:

* $s$ = scope,
* $p$ = path,
* $r$ = span/range,
* $v$ = version,
* $h$ = content hash.

For cross-modal POS, addresses extend to:

$$
A = (m, s, p, r, v, h, c) \tag{25}
$$

where:

* $m$ = modality,
* $c$ = coordinate system.

Examples:

* text span:   
  `text:repo:core/`  
  `parser.py:78:92:git:abc123:sha256...`
* image box: `image:frame42:box(x,y,w,h):v7:sha256...`
* trace window: `trace:serviceA:t0:t1:v12:sha256...`

Address Algebra supports:

* joins,
* meets,
* delta computation,
* continuity preservation,
* temporal localization,
* causal slicing,
* and cross-tool composition.

***

## 14. Projection Types and Projection Normal Form

POS systems require typed projections with explicit invariants.

Core projection types include:

| Projection Type | Function                                 |
| --------------- | ---------------------------------------- |
| CardinalityType | counts, distincts, heavy hitters         |
| TopologyType    | graphs, diffs, dependency structures     |
| SliceType       | bounded windows                          |
| VerdictType     | pass/fail + witnesses                    |
| IndexType       | inverted indices and scores              |
| TemporalType    | time-indexed windows and causal slices   |
| CrossModalType  | modality-specific locators and witnesses |

Each projection additionally possesses a canonical representation:

### Projection Normal Form (PNF)

PNF defines:

* canonical ordering,
* deterministic encoding,
* stable hashing,
* equality semantics,
* cross-language serialization,
* and cache-compatible representation.

Projection hash:

$$
h_P = \text{Hash}(\text{PNF}(P)) \tag{26}
$$

Collision policy:

1. compare hash;
2. if collision suspected, fall back to structural equality;
3. if structural equality fails, invalidate cache and escalate.

PNF enables:

* cache reuse,
* deterministic comparison,
* $\Delta$-equivalence detection,
* auditability,
* and platform-stable projection exchange.

#### Proposition 3 -- PNF Preserves $\Delta$-Equivalence

If PNF is canonical and semantics-preserving, then:

$$
P \sim_\Delta Q \Rightarrow \text{PNF}(P) \sim_\Delta \text{PNF}(Q) \tag{27}
$$

PNF may change representation, ordering, and serialization, but it may not change calibrated utilities over $\Delta$.

Therefore cache equality and $\Delta$-equivalence remain aligned.

***

## 15. Minimal Grammar for Projections

A minimal PNF grammar may be expressed as:

```ebnf
projection      ::= header body witnesses proofs edges bounds policies
header ::= "contract" id "type" ptype "delta" delta_id "hash" hash
body            ::= field*
field           ::= key ":" value
value           ::= scalar | list | map | address
address ::= "addr(" modality "," scope "," path "," range ","
version "," hash ")"
witnesses       ::= "witnesses" "[" witness* "]"
proofs          ::= "proofs" "[" proof* "]"
edges           ::= "edges" "[" edge* "]"
bounds          ::= "bounds" map
policies        ::= "policies" "[" label* "]"
edge ::= "edge(" id "," cost "," preconditions "," added_info ")"
```

This grammar is intentionally small.

The purpose is not expressive maximalism.

The purpose is deterministic projection exchange.

***

## 16. $\Delta$-Equivalence Classes

Different projections may be decision-equivalent.

We define:

$$
P \sim_\Delta Q \iff \forall d \in \Delta, \mathbb{E}[U(d \mid P)] = \mathbb{E}[U(d \mid Q)] \tag{28}
$$

POS systems may replace projections with cheaper $\Delta$-equivalent representatives:

$$
\min_{P_i \in [P]_\Delta} C(P_i) \tag{29}
$$

This formalizes semantic substitutability under bounded decision spaces.

$\Delta$-equivalence substitution preserves argmax decisions by construction.

***

## 17. Projection Calculus

Projection generation itself can be formalized.

We define *Projection Calculus* as the algebra of substrate reduction operators.

- **Operator:** restrict  
  **Notation:** $R_\Omega(S_u)$  
  **Function:** reduce substrate to scope $\Omega$

- **Operator:** aggregate  
  **Notation:** $\text{Agg}(P)$  
  **Function:** compress distributions

- **Operator:** index  
  **Notation:** $\text{Idx}(S_u)$  
  **Function:** expose navigational structure

- **Operator:** sample  
  **Notation:** $\text{Samp}_k(S_u)$  
  **Function:** bounded representative extraction

- **Operator:** sketch  
  **Notation:** $\text{Sketch}_{\epsilon,\delta}(S_u)$  
  **Function:** probabilistic approximation

- **Operator:** attach-address  
  **Notation:** $\text{Addr}(P,A)$  
  **Function:** preserve escalation continuity

- **Operator:** summarize-to-symbol  
  **Notation:** $\text{Sym}(P)$  
  **Function:** replace stable semantics with symbols

- **Operator:** redact  
  **Notation:** $\text{Redact}_L(P)$  
  **Function:** remove policy-disallowed fields

- **Operator:** fuse  
  **Notation:** $\text{Fuse}(P_1,P_2)$  
  **Function:** merge compatible projections

- **Operator:** normalize  
  **Notation:** $\text{PNF}(P)$  
  **Function:** canonicalize representation

Several laws follow.

### Restriction Idempotence

$$
R_\Omega(R_\Omega(S_u)) = R_\Omega(S_u) \tag{30}
$$

#### Escalation Monotonicity

Escalation may increase substrate exposure but may not destroy prior address continuity.

#### Composition Compatibility

Projection composition is valid only when shared addresses, policies, uncertainty bounds, and $\Delta$-closure are preserved.

Projection cost may be scalarized for simple cases:

$$
C(P) = \alpha |P| + \beta L(P) + \gamma_E E(P) \tag{31}
$$

where:

* $|P|$ = token size,
* $L(P)$ = latency,
* $E(P)$ = energy cost.

However, the canonical implementation model preserves the vector:

$$
C(P) = (\text{tokens}, \text{latency}, \text{energy}) \tag{32}
$$

and optimizes over a Pareto frontier unless a policy explicitly supplies scalar weights.

This prevents hidden tradeoff collapse.

***

## 18. Projection Composition

Projection composition is valid only under address and decision compatibility.

Let $P_2 \circ P_1$ denote composition.

Composition is valid iff:

1. $P_1$ and $P_2$ share a compatible address space;
2. their contracts are policy-compatible;
3. $\Delta$-closure holds;
4. their uncertainty bounds can be reconciled.

If these conditions fail, the system inserts a normalization projection.

Projection fusion merges multiple compatible projections into a single typed projection using address joins, duplicate-witness elimination, and bound reconciliation.

***

## 19. Incremental Observation

Many agentic systems are persistent.

They do not observe once.

They observe repeatedly across time.

Incremental observation governs this temporal continuity: instead of restarting from raw substrate, the system refines partial projections, preserves locality, emits sparse saliency, computes deltas, and reuses cache-valid prior observations.

### 19.1 Anytime Projections

Some observations should progressively refine over time.

We define an anytime projection sequence:

$$
P^{(1)} \subset P^{(2)} \subset \dots \tag{33}
$$

with:

$$
C(P^{(i+1)}) \ge C(P^{(i)}) \tag{34}
$$

and non-decreasing decision margin:

$$
\gamma(P^{(i+1)}) \ge \gamma(P^{(i)}) \tag{35}
$$

The agent may stop when either:

$$
S(P^{(i)}, \Delta) = 1 \tag{36}
$$

or the budget is exhausted.

### 19.2 Semantic Locality

Observation cost is partially driven by attention fragmentation.

We define semantic locality:

$$
L_s \tag{37}
$$

which penalizes cross-address cognitive jumps.

Projection planners prefer locality-preserving observation chains minimizing:

$$
\sum_i L_s(P_i, P_{i+1}) \tag{38}
$$

### 19.3 Sparse Attention Hints

Projections may emit sparse saliency maps:

$$
\sigma: A \rightarrow [0, 1] \tag{39}
$$

subject to a top-$k$ constraint.

Downstream models treat $\sigma$ as an attention prior, not as a substitute for proof.

### 19.4 Delta-Projections

Long-running agents repeatedly re-observe evolving substrate.

We define:

$$
\Delta P_t = P_t - P_{t-1} \tag{40}
$$

Delta projections support incremental recomputation through pipelines.

For composed projections:

$$
\Delta(P_2 \circ P_1) = \Delta P_2 \circ P_1 \oplus P_2 \circ \Delta P_1 \tag{41}
$$

This permits incremental update without recomputing the full observation chain.

### 19.5 Cache Coherence

Projection caches are maintained through:

* version vectors,
* address hashes,
* bounded staleness,
* causal clocks,
* slice freshness guarantees,
* and partial invalidation rules.

Cache consistency modes include:

| Mode              | Rule                                             |
| ----------------- | ------------------------------------------------ |
| Strong            | reuse only when versions match exactly           |
| Bounded-staleness | reuse if age ($\le \Delta t$)                    |
| Causal            | reuse if vector-clock dependencies are satisfied |

***

## 20. Witness-Carrying and Proof-Carrying Projections

Projection minimization introduces epistemic risk.

We therefore define two composable evidence layers.

### 20.1 Witness-Carrying Projections

Witness-Carrying Projections (WCPs) contain minimal evidence bundles preserving:

* hashes,
* counters,
* samples,
* witnesses,
* confidence scores,
* and derivation metadata.

Each witness bundle exposes:

$$
c_w \tag{42}
$$

verified through:

* stratified sampling,
* spot-checks,
* and sublinear audits.

For estimating key rates, a practical witness sampling bound is:

$$
k = O\left( \frac{1}{\epsilon^2} \log \frac{1}{\delta} \right) \tag{43}
$$

WCP metadata must declare:

* sample size,
* sampling frame,
* confidence level,
* error tolerance,
* and audit method.

### 20.2 Proof-Carrying Projections

Proof-Carrying Projections (PCPs) attach succinct cryptographic derivation proofs:

* Merkle paths,
* inclusion proofs,
* content-authenticity hashes,
* derivation commitments.

A standard PCP verification API checks proof material against $h$ in:

$$
A = (s, p, r, v, h) \tag{44}
$$

Failure semantics:

* invalid proof -> reject projection;
* missing proof -> downgrade confidence;
* unverifiable address -> escalate;
* mismatched hash -> invalidate cache and fetch substrate.

WCP and PCP are not alternatives.

WCP supplies epistemic confidence.

PCP supplies derivation verification.

A projection may carry either, both, or neither, depending on risk class and policy.

When both are present, PCP verification gates admissibility of the evidence bundle, while $c_w$ estimates the statistical adequacy of the verified witnesses.

***

## 21. Projection Lipschitzness and Robustness

POS systems must remain stable under bounded substrate perturbation.

Let $d(S_u, S_u')$ be a domain-specific distance metric, such as:

* edit distance,
* graph cut distance,
* schema distance,
* temporal divergence,
* trace distance.

A projection function is Lipschitz-stable when:

$$
\left| \frac{U(\cdot \mid P(S_u))}{U(\cdot \mid P(S_u'))} \right|_\infty \le L \cdot d(S_u, S_u') \tag{45}
$$

The perturbation metric must be selected per substrate domain and decision class. A code-edit distance may be appropriate for parser debugging, while graph-cut distance may be appropriate for dependency analysis and temporal divergence may be appropriate for trace debugging. Robustness claims are only meaningful when this metric captures the changes that matter for $\Delta$.

Without robustness guarantees, projections become manipulable observation surfaces.

***

## 22. Policy Lattices and Information-Flow Governance

Observation governance policies compose algebraically.

We define a *Policy Lattice* supporting:

* meet,
* join,
* monotonic tightening.

Policies include:

* privacy,
* cost,
* latency,
* security,
* retention,
* jurisdiction,
* and audit constraints.

Monotonicity requirement:

> tightening policy may not increase exposed substrate.

However, lattice meet may produce deadlock.

POS systems therefore define prioritized joins with minimal relaxation:

$$
\delta_{\text{relax}} \tag{46}
$$

Every relaxation is audit-logged.

Projection fields additionally carry security labels.

For labels $L_h$ and $L_l$, POS requires non-interference:

$$
NI(L_h \nrightarrow L_l) \tag{47}
$$

except through approved aggregators.

This is enforced by the type system over Projection Calculus operators.

***

## 23. Observation Planning

Observation itself can be planned strategically.

We define cost-to-go:

$$
J(P) \tag{48}
$$

representing expected remaining observation cost.

The planner optimizes:

$$
C(P_i) + \mathbb{E}[J(P_{i+1})] \tag{49}
$$

while minimizing regret:

$$
R = U(d^* \mid S_u) - U(d_P \mid P) \tag{50}
$$

where:

* $d^*$ = optimal substrate decision,
* $d_P$ = projection-induced decision.

Regret decomposes into:

$$
R = R_{\text{proj}} + R_{\text{model}} + R_{\text{policy}} \tag{51}
$$

This isolates gains attributable to the observation surface itself.

A reference planner may use A* over projection space:

```text
open_set := initial projections
while open_set not empty:
    P := lowest C(P)+J(P)
    if S(P, Delta): return P
    for edge in admissible_edges(P):
        P' := apply(edge)
        if h_P not visited and not Delta-equivalent to cheaper projection:
            enqueue(P')

***

## 27. Failure Modes and Remediation

- **Failure:** Underprojection  
  **Description:** Necessary distinctions omitted  
  **Remediation:** mandatory escalation

- **Failure:** Overprojection  
  **Description:** Excess substrate exposed  
  **Remediation:** contract tightening

- **Failure:** Escalation Ambiguity  
  **Description:** No clear fetch path  
  **Remediation:** edge validation

- **Failure:** Semantic Drift  
  **Description:** Projection meaning changes  
  **Remediation:** symbol migration

- **Failure:** Address Loss  
  **Description:** locality destroyed  
  **Remediation:** address algebra repair

- **Failure:** Projection Inflation  
  **Description:** compact form grows verbose  
  **Remediation:** MU stop rule

- **Failure:** Decision Oscillation  
  **Description:** Delta flips repeatedly  
  **Remediation:** hysteresis

- **Failure:** Witness Spoofing  
  **Description:** invalid evidence  
  **Remediation:** PCP verification

- **Failure:** Budget Starvation  
  **Description:** premature stop  
  **Remediation:** exploration floor

- **Failure:** Policy Deadlock  
  **Description:** no admissible edge  
  **Remediation:** relaxation ladder

***
## 28. Empirical Evaluation

POS should be evaluated through controlled A/B protocols. For each task family, the benchmark defines substrate $S_u$, decision class $\Delta$, ground-truth next decision $d^*$, policy configuration, and substrate snapshot. Raw-substrate, heuristic-filtered, conventional-summary, and POS systems are then compared on the same task sequence.

Core metrics include:

| Metric             | Definition                                           |
| ------------------ | ---------------------------------------------------- |
| Sufficiency rate   | fraction of steps where $S(P,\Delta)=1$              |
| Overexposure ratio | $C(P)/C(P^*_\Delta)$ or estimated $\eta$             |
| Regret             | $U(d^* \mid S_u) - U(d_P \mid P)$                    |
| Escalation rate    | fraction of steps requiring deeper fetch             |
| Token amortization | token cost over full agent loop                      |
| Latency            | wall-clock decision time                             |
| Energy             | joule estimate per observation loop                  |
| Cache hit rate     | reuse of prior projections                           |
| Witness confidence | average $c_w$                                        |
| Proof failure rate | PCP verification failure frequency                   |

Benchmark suites should include debugging tasks, retrieval tasks, CI tasks, log analysis, trace analysis, cross-modal inspection, and multi-agent orchestration.

***

## 29. Theoretical Observation Bound

Under bounded decision classes, indexed substrates, calibrated utility, and Lipschitz assumptions, many tasks admit projections satisfying:

$$
C(P) = O(\log |S_u|) \tag{56}
$$

through sketches, indices, topology projections, heavy-hitter summaries, bounded witnesses, and address-preserving escalation.

This formalizes the possibility of sublinear observation.

The observing agent need not ingest substrate proportional to substrate size.

However, this bound is conditional.

It may fail under:

* rare critical events,
* adversarially hidden signals,
* non-stationary utility,
* unindexed substrates,
* continuous or very large $\Delta$,
* domains where sketches suppress decisive outliers,
* and substrates that violate Lipschitz assumptions.

***

## 30. Running Example -- Parser Fault Localization

Goal:
locate a faulty parser rule.

Decision class:

$$
\begin{aligned}
\Delta = \{&\text{inspect\_file}, \text{compare\_versions}, \\
&\text{run\_tests}, \text{stop}\}
\end{aligned}\tag{57}
$$

Observation Contract:

$$
\begin{aligned}
\mathcal{O} = (&\text{parser fault localization}, \Delta, \\
&\text{TopologyType}, G_{\text{debug}})
\end{aligned}\tag{58}
$$

Initial projection:

```text
ProjectionType: CardinalityType
failures=12
modules=3
top:
parser.py@[22,81]
lexer.py@

***

## 31. Datacenters, Edge AI, and Observation Economics

The implications extend beyond token billing.

If agentic systems continuously over-observe substrate, infrastructure scales around avoidable epistemic waste.

This means:

* more inference,
* more memory,
* more bandwidth,
* more cooling,
* more datacenter construction,
* more energy expenditure,
* larger cloud dependence.

POS systems suggest a different future:
smaller observation loops,
higher semantic density,
and substantially reduced inference demand.

The key insight:

> local inference becomes more viable when the observation surface itself is parsimonious.

A smaller cognitive loop requires less model capacity.

Thus observation theory directly impacts hardware viability.

***

## 32. Limitations

POS does not eliminate the need for deep substrate access.

It governs when such access is justified.

Several limitations remain.

First, $U(d \mid P)$ may be non-stationary.
If utility changes faster than calibration, sufficiency decisions degrade.

Second, $\Delta$ may be large, continuous, or poorly specified.
POS works best when next-step decision classes are finite and typed.

Third, adversarial substrates may be constructed to defeat projection assumptions.
Rare decisive events are especially dangerous when sketches or summaries suppress tails.

Fourth, Lipschitz assumptions may fail.
Small substrate edits can sometimes produce discontinuous semantic consequences.

Fifth, policy lattices may deadlock.
Privacy, latency, security, and cost constraints can jointly forbid every useful escalation edge.

Sixth, projection models may learn bad compression habits.
A projection surface can become a subtle bottleneck if optimized against incomplete feedback.

These limits do not invalidate POS.

They define the boundary where disciplined escalation, audit, proof, or full substrate access becomes necessary.

***

## 33. The Missing Theory

Current AI systems possess:

* theories of training,
* theories of optimization,
* theories of retrieval,
* theories of memory,
* theories of alignment,
* theories of scaling.

But they largely lack:

* theories of observation.

Tools are still treated as substrate emitters rather than epistemic interfaces.

Without explicit observation theory, systems compensate through brute-force cognition.

That path is computationally expensive and structurally inelegant.

***

## 34. Scope and Limits of the Claim

The strongest claim of this paper is not that all observation can be made small.

It is that much current agentic observation is unnecessarily large because tools emit substrate before decision relevance is established.

POS is therefore a theory of governed reduction, not a denial of deep inspection.

When $\Delta$ is finite, utility is calibrated, substrate has usable address structure, and projection assumptions hold, observation can often be made sublinear.

When those conditions fail, POS should escalate, audit, or fetch raw substrate.

The discipline lies in knowing which case one is in.

***

## 35. Conclusion

The future of agentic systems may depend less on larger models than on better observation.

The dominant architecture today assumes:

observe broadly,
compress later,
reason afterward.

This paper proposes the inverse:

observe minimally,
escalate selectively,
preserve inferential continuity.

A raw substrate dump assumes cognition should emerge from abundance.

A semantic projection assumes cognition should emerge from disciplined observation.

The difference between those assumptions may ultimately determine:

* the scalability of agentic systems,
* the economics of inference,
* the sustainability of datacenter growth,
* the viability of local AI,
* and the cognitive architecture of machine intelligence itself.

The cheapest token is not the compressed token.

It is the token never emitted because the semantic projection was already sufficient.

***

## Appendix A -- Symbol Glossary

| Symbol        | Meaning                                    |
| ------------- | ------------------------------------------ |
| $S_u$         | underlying substrate                       |
| $P$           | projection                                 |
| $\Delta$      | decision class                             |
| $S(P,\Delta)$ | sufficiency predicate                      |
| $U(d \mid P)$ | expected utility of decision $d$ under projection $P$ |
| $C(P)$        | projection cost                            |
| $P^*_\Delta$  | minimal sufficient projection for $\Delta$ |
| $\eta$        | optimality gap                             |
| $H_\Delta(P)$ | decision entropy                           |
| $\gamma(P)$   | decision margin                            |
| $A$           | address tuple                              |
| $G=(V,E)$     | escalation graph                           |
| $R$           | regret                                     |
| $J(P)$        | cost-to-go                                 |
| $L_s$         | semantic locality                          |
| $h_P$         | projection hash                            |
| $c_w$         | witness confidence                         |

***

## Appendix B -- Proof Sketches

### B.1 $\Delta$-Equivalence Substitution

If:

$$
P \sim_\Delta Q
$$

then for every $d \in \Delta$:

$$
\mathbb{E}[U(d \mid P)] = \mathbb{E}[U(d \mid Q)]
$$

Therefore the argmax decision under $P$ is identical to the argmax decision under $Q$, assuming the same tie-breaking rule.

Thus $Q$ may replace $P$ without changing the next admissible decision.

***

### B.2 PNF Preservation

If PNF is semantics-preserving, then canonicalization changes only representation, not decision utility.

Therefore:

$$
P \sim_\Delta \text{PNF}(P)
$$

and if $P \sim_\Delta Q$, then:

$$
\text{PNF}(P) \sim_\Delta \text{PNF}(Q)
$$

This allows canonical hashes to support cache reuse without breaking decision equivalence.

***

### B.3 Sublinear Observation via Sketches and Indices

For indexed substrates, many decision classes require only:

* counts,
* top-$k$ elements,
* locality maps,
* or bounded witnesses.

Sketches and indices can compute these in:

$$
O(\log |S_u|)
$$

or sublinear access under appropriate assumptions.

Thus a sufficient projection may be sublinear even when the substrate is large.

***

### B.4 Non-Interference Under Projection Calculus

If every Projection Calculus operator is type-checked against information-flow labels, and disallowed high-to-low flows are rejected, then emitted low-security projections cannot depend on high-security substrate fields except through approved aggregators.

Therefore:

$$
NI(L_h \nrightarrow L_l)
$$

holds by operator composition.

***

### B.5 Anytime Convergence Under Hysteresis

Given an anytime projection sequence with non-decreasing decision margin and two-threshold entropy hysteresis, escalation cannot oscillate indefinitely near a single threshold.

The system either:

* reaches sufficiency,
* exhausts budget,
* or stabilizes in the hysteresis band until new information arrives.

***

## Corpus-Wide Reference Positioning

This paper argues that modern AI systems scale primarily through larger models, longer context windows, greater retrieval bandwidth, and increasingly massive datacenter infrastructure. Its nearest external comparison fields are observation, ai, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Telemetry can be complete at the instrumented boundary while omitting the causal variable, real-world effect, or authority question that matters. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** OpenTelemetry Authors. *OpenTelemetry Specification*. https://opentelemetry.io/docs/specs/otel/ **Relationship:** Adjacent observability standard for traces, metrics, logs, and context propagation; telemetry is not equated with adjudicated evidence.

**[E2]** W3C. *Trace Context, Level 1*. W3C Recommendation, 23 November 2021. https://www.w3.org/TR/trace-context/ **Relationship:** Adjacent distributed tracing standard for propagating trace identity across service boundaries.

**[E3]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E4]** Karen Scarfone, Murugiah Souppaya, and Donna Dodson. *Secure Software Development Framework (SSDF) Version 1.1*. NIST SP 800-218, 2022. DOI: 10.6028/NIST.SP.800-218. https://doi.org/10.6028/NIST.SP.800-218 **Relationship:** Adjacent secure-development framework for preparation, protection, production, and vulnerability response.

**[E5]** Patrick Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS 2020*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **Relationship:** Predecessor retrieval architecture; comparison centers on provenance, admission, and fail-closed constraints not supplied by retrieval alone.

**[E6]** Shunyu Yao et al. "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*. arXiv:2210.03629. https://arxiv.org/abs/2210.03629 **Relationship:** Predecessor agent pattern for interleaving reasoning and action; used to distinguish action traces from governed effects.

**[E7]** Elham Tabassi. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1, 2023. DOI: 10.6028/NIST.AI.100-1. https://doi.org/10.6028/NIST.AI.100-1 **Relationship:** Adjacent risk-management framework used to test whether the paper operationalizes governance beyond voluntary process guidance.

### Ableman corpus

**[A1]** Adam Ableman. *The Constitutional Observability Platform*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-9FC6DF9C2BCB38DA`;  
source SHA-256  
`D93D41518A823703E1076B02D95D28BD7ADF29D3DC15760E0165E84E28BC70B9`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Testing for Deriving Observable State of Software Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-BAA7A4A4150F5D66`;  
source SHA-256  
`0B6AAC8B71DA25E24F7FB4A018692F609096DBA8383C9C8C0AC15F1AF711B3A8`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Epistemic Situational Awareness (ESA)*. Ableman Corpus current edition; work identity `PAPER.PUB.18123102`;  
source SHA-256  
`D43BD7CF219AB9A6EAF715CFA8CBFA32FCB8A11B8DFCADE004E00595D5F68503`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *CARA: Constrained Artificial Reasoning Architecture*. Ableman Corpus current edition; work identity `PAPER.PUB.18099715`;  
source SHA-256  
`F8F74F0CD58F5414D9A29EBE958E49751892D07A028CB51197F8201B18AAB40E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *A Constitution for the Context Window*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-CF26BA0E123F472F`;  
source SHA-256  
`60395402368E146F115CCE53D0E5A15B8FB23C90ED5B24CA92AB8515B2009965`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Context & Memory (GCM)*. Ableman Corpus current edition; work identity `PAPER.PUB.18633797`;  
source SHA-256  
`3F17ACD8AB9C6DC66C23D22098628C70042854B198C3ABFCBFA3EC7DC27B9C08`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Anthropic. *Context Engineering for AI Agents.*

Anthropic. *Building Effective Tools for AI Agents.*

LangChain. *Context Engineering Documentation.*

Model Context Protocol (MCP) discussions on tool schema minimization and response filtering.

Research on information theory, semantic compression, bounded rationality, probabilistic sketches, partial-state observation systems, sparse attention architectures, and edge AI inference systems.

Unix philosophy and composable tool-interface design traditions.

Distributed systems literature on projection, indexing, delta synchronization, caching, and partial-state replication.

Literature on proper scoring rules, calibration, information-flow control, Merkle proofs, streaming algorithms, and approximate query processing.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20437813](https://doi.org/10.5281/zenodo.20437813)
