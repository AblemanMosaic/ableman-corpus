# Dynatology

## A Science of Structured Potentiality

### Before there are agents, meanings, markets, institutions, or intelligences, there exists a structure governing what may become.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

This paper introduces Dynatology, the study of structured potentiality.

The term derives from the Greek:

$$
\textit{dynatos}
$$

meaning possible, capable, or possessing the capacity to become.

Most scientific frameworks begin with entities, states, or agents. Dynatology begins with possibility itself. More precisely, it begins with the structure governing possibility.

The framework proposes that geometry is induced by admissibility over instantiated state space. Possible futures are neither uniformly reachable nor equally admissible. They occupy structured regions connected by continuations, constrained by admissibility, and transformed by constitutional operators.

The paper introduces:

* structured potentiality,
* possibility geometry,
* dynatopology,
* continuation fields,
* constitutional operators,
* admissibility inference.

A formal dynatological system is defined as the triple:

$$
\mathcal D := (S, \Omega, A)
$$

where:

* $S$ is a state space of instantiated configurations,
* $\Omega \subseteq S \times S$ is a conceivability relation,
* $A \subseteq \Omega$ is an admissibility relation.

The viability kernel $V \subseteq S$ and the family of admissibility-modifying operators $C$ are derived from $A$ rather than postulated as primitives. The viability kernel is computable in $O(|S| + |A|)$ on a finite admissibility graph (Section 28).

Dynatology provides a substrate-neutral framework for studying physical, biological, computational, economic, social, and cognitive systems through a common language of structured possibility. An empirical instance is reported in Section 28: in the Constitutional Collective with Optional Overmind (CCOO) framework, refinement of the admissibility relation from a 4-neighbor to an 8-neighbor local-max rule produced monotone expansion of the viability kernel, capturing approximately 101% of capability previously requiring centralized aggregation across 100 seeds.

The central claim:

> The deepest object of inquiry is not what exists, but the structure governing what may become.

---

## 1. Introduction

Most disciplines begin by identifying fundamental objects.

Physics studies matter.

Biology studies organisms.

Economics studies agents.

Computer science studies computations.

Psychology studies minds.

Despite their differences, these approaches typically assume:

```
Entity
      |
State
      |
Interaction
      |
Future
```

Possibility appears as a consequence of existing things.

Dynatology proposes the inverse.

It asks:

> What if structured potentiality is primary and entities are secondary?

The framework studies not merely what exists but the structure governing what may exist, what may continue, and what may become.

Admissibility is not merely constraint; it is the generative structure from which all realizable futures are drawn.

---

## 2. Ontological Typing

A recurring source of confusion across disciplines is the conflation of states, possibilities, continuations, and participants.

Dynatology distinguishes these objects explicitly.

Let:

$$
S
$$

denote a state space consisting of instantiated configurations.

Let:

$$
\mathcal P
$$

denote a possibility space.

Then:

$$
\mathcal P
\supseteq
S
$$

and generally:

$$
\mathcal P
\not\equiv
S.
$$

Possibility therefore exceeds actuality.

However, for operational analysis, possible continuations are represented relationally.

Let:

$$
\Omega
\subseteq
S \times S
$$

denote conceivable transitions.

Let:

$$
A
\subseteq
S \times S
$$

denote admissible transitions.

Then:

$$
A \subsetneq \Omega \subseteq S \times S.
$$

The distinction between $\Omega$ and $A$ is crucial.

Conceivability is not admissibility.

Reachability is not possibility.

Admissibility is structured possibility under governing constraints.

For each state:

$$
s \in S,
$$

define:

$$
\Omega(s) := \{s' \mid (s,s') \in \Omega\}.
$$

In stochastic formulations, conceivability bounds support:

$$
P_A(s' \mid s) = 0
\quad
\forall s' \notin \Omega(s).
$$

A useful strengthening defines conceivability as constitutional reachability under some admissibility regime:

$$
\Omega := \bigcup_{C \in \mathcal C} A_C.
$$

Thus a transition is conceivable if some constitutional configuration can admit it.

---

## 3. Formal Dynatological Systems

The minimal formal object is

$$
\mathcal D=(S,\Omega,A),\qquad A\subseteq\Omega\subseteq S\times S.
$$

Given declared path semantics, the continuation fields, reachability preorder, reachability topology, and finite-graph viability kernel can be derived from $A$. They require no additional primitive relation.

Other objects used by the paper are **not uniquely derivable from $A$ alone**. A named constraint factorization $\{C_i\}$, amendment operator, edge weights, transition probabilities, participant map, state distribution, utility, authority assignment, evidence semantics, and system boundary are additional structures or interpretations. Many different constraint families can induce the same $A$, so the induced relation does not recover why an edge was admitted or refused.

A typed extension may therefore be written

$$
\mathcal D^+=(S,\Omega,A;w,P,\mathcal C,\mathcal M,\chi),
$$

where the semicolon marks optional declared structure: weights $w$, probabilities $P$, constraints or constitutions $\mathcal C$, amendment or migration operators $\mathcal M$, and an observation/evidence contract $\chi$. Results must state which structure they require.

The view that $S$ itself is induced by constitutional reachability is a possible ontological interpretation, not part of the minimal triple. It additionally requires an initial domain, constitution class, and reachability semantics and must avoid defining the state space circularly through paths whose endpoints already presuppose that space.

## 4. Possibility Space Semantics

The triple admits several disciplined interpretations. As a transition structure, $S$ contains modeled configurations, $\Omega$ modeled conceivable transitions, and $A$ admitted transitions. As a Kripke-style frame, the relations can be accessibility relations once the relevant modal language is supplied. As a directed graph, paths and reachability can be studied directly.

Category-theoretic treatment requires more than relabeling edges as morphisms: identities and composition must be defined and closed, and distinct paths may need to remain distinct. A free category generated by the admissibility graph is one valid construction, but it is additional structure rather than an automatic identity with the graph.

Every interpretation is relative to a model boundary and granularity. $\Omega$ is not the set of all metaphysically possible events unless an independent argument establishes that scope. A transition absent from $\Omega$ may be inconceivable under the model, omitted, unresolved, or represented at another scale.

## 5. The Dynatological Distinction

Dynatology is close to transition systems, control theory, viability theory, modal logic, and dynamical systems.

Its distinction is not that it invents transitions, constraints, or reachability.

The distinction is fourfold.

First, admissibility is treated as a primary ontological object rather than an auxiliary rule imposed upon already primary entities.

Second, transformations of admissibility are treated as first-class phenomena.

Third, agents, meaning, intelligence, hierarchy, markets, and institutions are defined as derived invariants or operators over possibility structure.

Fourth, the same formal grammar is used across substrates.

Dynatology therefore does not replace existing formalisms.

It provides a unifying interpretation of what those formalisms share.

---

## 6. Possibility Geometry

Let $w:A\rightarrow\mathbb R_{\geq0}$ assign nonnegative edge weights. The directed admissible path cost is

$$
d_A(s,s')=\inf_{\gamma:s\leadsto s'}\sum_{(u,v)\in\gamma}w(u,v),
$$

with $d_A(s,s')=\infty$ when no admissible path exists. Under these assumptions $d_A$ is generally an **extended directed pseudodistance**: it satisfies $d_A(s,s)=0$ and the directed triangle inequality, but need not be symmetric, and distinct states can have zero distance when zero-weight paths exist. It is a metric only under stronger conditions, including finiteness, symmetry, and identity of indiscernibles.

The weights can represent cost, time, energy, probability penalty, institutional friction, or computational burden only when their units and composition rules are declared. Different weights on the same relation produce different geometries.

## 7. Dynatopology

Define $s\preceq s'$ when $s'$ is reachable from $s$. This is a preorder. If the Alexandrov topology is chosen so that open sets are upward-closed, then

$$
s\in U\ \text{and}\ s\preceq s'\Rightarrow s'\in U.
$$

Equivalently, $F^{(*)}(s)\subseteq U$ for every $s\in U$. The topological closure of $X$ under this orientation is the **downward** reachability set

$$
\operatorname{Cl}(X)=\{s\mid\exists x\in X,\ s\preceq x\},
$$

whereas the source's forward-reach set $\{s'\mid\exists x\in X,\ x\preceq s'\}$ is the upward closure or future cone of $X$. Reversing the open-set convention reverses these roles, so every use must state its orientation.

Dynatopology can then study reachability classes, strongly connected components, boundaries, continuity, and admissibility-preserving maps without conflating a future cone with topological closure.

## 8. Admissibility

Admissibility is the central organizing relation.

In hard-constraint systems, admissibility factorizes as:

$$
A := A_{\text{phys}} \cap A_{\text{info}} \cap A_{\text{const}}.
$$

where:

* $A_{\text{phys}}$ captures physical feasibility,
* $A_{\text{info}}$ captures informational availability,
* $A_{\text{const}}$ captures constitutional or normative permissibility.

Equivalently:

$$
A(s,s') := \bigwedge_i C_i(s,s').
$$

Realistic systems may require soft or probabilistic admissibility.

In that case:

$$
A(s,s') := \prod_i C_i(s,s')
$$

for graded predicates, or:

$$
P_A(s' \mid s)
\propto
\prod_i \phi_i(s,s').
$$

Hard admissibility is recovered when:

$$
A(s,s') \iff P_A(s' \mid s) > 0.
$$

This connects physical constraint, computation, governance, uncertainty, and partial compliance.

---

## 9. Refusal and the Negative Geometry of Possibility

The relation $A \subseteq \Omega$ specifies which continuations are admissible. It says relatively little about the ontological character of what is not. This section closes that gap.

Define the refusal relation:

$$
R := \Omega \setminus A.
$$

$R$ is not a new primitive. It is fully determined by $\Omega$ and $A$, and adds no information to the formal system $\mathcal D = (S, \Omega, A)$. Its role is interpretive: it names the negative half of admissibility.

### 9.1 Two Faces of the Same Structure

Every constitution operates simultaneously as a structure of permission and a structure of refusal. The relation $A$ records which transitions the constitution licenses; $R$ records which conceivable transitions the constitution actively excludes to preserve identity, viability, or coherence. These are not separate facts: they are the positive and negative views of a single partition of $\Omega$.

The direction of explanation differs:

- The admissibility reading says: *this transition occurs because the constitution permits it.*
- The refusal reading says: *this transition does not occur because admitting it would violate the conditions the constitution exists to preserve.*

Both readings refer to the same set of judgments. The refusal reading carries explanatory weight the admissibility reading does not: it names *why* a continuation is excluded, in terms of what the system would lose by admitting it.

### 9.2 Refusal as Constitutional Preservation

A continuation $(s, s') \in R$ is conceivable but excluded. Under the refusal reading, this exclusion is interpreted as preservation: admitting the transition would violate one or more constitutional predicates whose conjunction defines admissibility (Section 3). Refusal is therefore the active maintenance of the structural integrity the constitution exists to support.

This reading makes the following four restatements available:

- Admissibility becomes positive constitutional permission.
- Refusal becomes negative constitutional preservation.
- Viability becomes the sustained survival of refusal-compliant trajectories: a state is viable when an infinite continuation exists that never crosses into $R$.
- Identity becomes persistence through selective refusal: a participant identity (Section 16) is sustained by continually refusing the continuations that would disrupt it.

The formal definitions of viability and identity in Sections 12 and 16 are unchanged. The refusal reading offers a complementary interpretive frame: what those sections describe as the existence of admissible paths is equivalently described as the sustained avoidance of refused paths.

### 9.3 A Unifying Structural Phenomenon

The refusal reading provides a common structural form for phenomena that are usually classified separately:

- A wall refusing a particle's transit.
- A logical system refusing a contradictory inference.
- An institution refusing an unsupported action.
- A biological system refusing continuation past viability collapse.
- A constitutional rule refusing an unauthorized petition.

Each is, structurally, a case of $(s, s') \in \Omega$ with $(s, s') \notin A$. The constitutional substrate differs (physical law, logical inference, institutional rule, biological viability, governance regime), but the dynatological pattern is identical: a conceivable continuation excluded by the constitution that defines what may continue. Naming this pattern *refusal* gives it a single vocabulary across substrates.

### 9.4 Status of the Concept

Formally, refusal adds no new primitive: $R$ is definable from $\Omega$ and $A$, and every formal claim about refusal can be made by quantifying over $\Omega \setminus A$. Ontologically, refusal names the missing half of admissibility --- the half a strictly positive presentation of admissibility leaves unspoken.

Admissibility tells the system what may become.

Refusal explains why everything else does not.

---

## 10. Temporal Structure
Dynatology assumes discrete time unless otherwise specified.

Let:

$$
t \in \mathbb N.
$$

Admissible continuation satisfies:

$$
(s_t,s_{t+1}) \in A.
$$

A path is a function:

$$
\gamma:\mathbb N \rightarrow S
$$

such that:

$$
\forall t,
\quad
(\gamma(t),\gamma(t+1)) \in A.
$$

Continuous formulations are treated separately in Section 24.

---

## 11. Continuation Fields

For state:

$$
s,
$$

the forward continuation field is:

$$
F(s) := \{s' \mid (s,s') \in A\}.
$$

The backward continuation field is:

$$
F^{-1}(s) := \{s' \mid (s',s) \in A\}.
$$

The k-step continuation field is:

$$
F^{(k)}(s) := \{s' \mid s \leadsto_k s'\}.
$$

The unlimited reachability field is:

$$
F^{(*)}(s) := \{s' \mid s \leadsto s'\}.
$$

These objects provide local and horizon-based geometry for future-space.

---

## 12. Viability

For the infinite-path semantics used here,

$$
\begin{aligned}
V_A=\{&s\in S\mid\exists\gamma:\mathbb N\rightarrow S, \\
&\ \gamma(0)=s, \ \forall t, \\
&\ (\gamma(t),\gamma(t+1))\in A\}
\end{aligned}.
$$

Finite-horizon viability $V_A^{(k)}$ requires an admissible path of length $k$. Other domains may require termination, goals, safety, bounded resources, or progress. Those requirements produce different viability objects and must not be inferred from the infinite-path definition.

Positive edge cost is not a general progress criterion: it can mean resource expenditure rather than advancement and can make a cycle arbitrarily costly while still counting as viable under the definition above. Nontrivial progress requires a separately declared ranking, goal, liveness condition, or recurrence contract.

## 13. Participation

An admissible trajectory is a mathematical path. Calling a trajectory a participant is an optional ontological interpretation, not a consequence of the triple. Empirical participant identity usually also requires a projection from whole-system state to a persisting subsystem, boundary conditions, lineage rules, and an equivalence or continuity criterion.

Dynatology can therefore represent a participant by a tuple such as

$$
P_i=(B_i,\pi_i,\Gamma_i,\sim_i),
$$

where $B_i$ declares the boundary, $\pi_i$ projects system states to participant states, $\Gamma_i$ is the projected trajectory, and $\sim_i$ states the lineage criterion. This preserves the proposal that participation depends on continuation while avoiding the claim that every admissible whole-system path is itself an agent or participant.

## 14. Meaning

A distinction $\Delta$ is **continuation-relevant** when its intervention changes a declared transition relation, distribution, reachability set, or consequence profile. This is a causal or structural result. Calling it semantic meaning is a stronger interpretation that may require uptake, role, jurisdiction, persistence, or consequence conditions supplied by the corpus's meaning-binding works.

The comparison $A_\Delta\neq A$ is informative only when $\Delta$, the intervention, model boundary, and relation-estimation method are specified independently of the result. Distributional measures require normalized transition distributions and treatment of zero support; mutual information requires random variables and a sampling distribution.

## 15. Intelligence

Viability preservation can be a minimal objective or substrate for some forms of intelligence, but it is not by itself a discriminating definition. Passive stability, a self-loop, or a fixed homeostatic mechanism can preserve viability. Stronger intelligence claims require declared capacities such as model-based adaptation, generalization, planning, learning, counterfactual evaluation, or governance under novelty.

Dynatology may therefore measure a policy's viability performance,

$$
J_V(\pi)=\Pr_\pi(s_t\in V_A\ \forall t),
$$

without identifying every maximizer of $J_V$ as intelligent.

## 16. Identity

The directed cost $d_A$ is not generally symmetric, so it cannot directly support the source's claim that $\epsilon$-closeness is symmetric. A bounded symmetric comparison can instead be declared, for example

$$
\bar d_A(s,s')=\frac{\min\{d_A(s,s'),d_A(s',s)\}}{1+\min\{d_A(s,s'),d_A(s',s)\}},
$$

when at least one direction is finite, with a declared value of $1$ when both are infinite. Other symmetrizations may be more appropriate. A discounted trajectory comparison can then use $\bar d_A$.

Threshold closeness remains a tolerance relation and is not transitive in general. Consequently $[\Gamma]_{\sim_\epsilon}$ is not an equivalence class unless a separate equivalence construction is chosen. Single-linkage closure is one option but can chain arbitrarily distant trajectories; identity conclusions therefore depend on the selected lineage rule and cannot be derived from admissibility alone.

## 17. Coordination

Coordination requires jointly admissible continuation.

For participants $P_i$ and $P_j$, lift the system to product space:

$$
S^{(2)} := S \times S.
$$

Let:

$$
C_{\text{joint}}:S \times S \rightarrow {0,1}.
$$

Define joint admissibility:

$$
\begin{aligned}
&A^{(2)}((s_i,s_j),(s'_i,s'_j)) := A(s_i,s'_i) \\
&\land A(s_j,s'_j) \\
&\land C_{\text{joint}}(s'_i,s'_j)
\end{aligned}.
$$

Coordination occurs when:

$$
A^{(2)}((s_i,s_j),(s'_i,s'_j)).
$$

Coordination is not mere overlap of futures.

It is compatibility of future-making.

---

## 18. Hierarchy

Hierarchy is an operator acting upon admissibility.

Let:

$$
H:2^{S\times S} \rightarrow 2^{S\times S}.
$$

The hierarchical admissibility relation is:

$$
A' := H(A).
$$

A hierarchy is monotone when:

$$
A_1 \subseteq A_2
\Rightarrow
H(A_1)\subseteq H(A_2).
$$

A hierarchy is contractive when:

$$
H(A)\subseteq A.
$$

Contractive hierarchy restricts future-space.

Some hierarchies expand admissibility.

Expansion occurs when:

$$
\exists C \in \mathcal C
\text{ such that }
H(A)=A\cup A_C.
$$

Technological innovation, legal authorization, and institutional capacity may all expand admissible continuation.

Expansion therefore requires explicit constitutional justification rather than being assumed.

---

## 19. Markets

Markets modify possibility geometry through economic constraints.

To type budget constraints, augment state:

$$
S := S_{\text{world}} \times S_{\text{resources}}.
$$

Define:

$$
\text{budget}(s,s')
:=
B(s)
\geq
\sum_i p_i x_i(s \rightarrow s').
$$

Market admissibility is:

$$
A_{\text{market}}(s,s') := A(s,s') \land \text{budget}(s,s').
$$

Prices may be treated as Lagrange multipliers shaping feasibility.

For example:

$$
\max
\sum_t U(s_t)
\quad
\text{subject to}
\quad
(s_t,s_{t+1})\in A,
\quad
\sum_i p_i x_i \leq B.
$$

Optimization occurs inside admissibility.

It does not replace admissibility.

---

## 20. Evolution

Evolution modifies constitutional structure.

Let:

$$
\mathcal C :=
{C \mid C \text{ defines admissibility on } S}.
$$

The selection operator is:

$$
\mathcal S:\mathcal C \rightarrow \mathcal C.
$$

Evolution proceeds by:

$$
C_{t+1} := \mathcal S(C_t).
$$

A deterministic selection criterion may be:

$$
\mathcal S(C)
:=
\arg\max_{C'}
\mathbb E[R_V^{C'}].
$$

A stochastic evolutionary criterion may be:

$$
\Pr(\mathcal S(C)=C')
\propto
\exp(\beta \cdot \text{fitness}(C')).
$$

Evolution is therefore structured modification of possibility geometry.

---

## 21. Incompleteness

The gap $A\setminus\widehat A$ describes **model incompleteness**: admissible transitions absent from an internal or inferred model. It is distinct from CCOO's task-relative **constitutional incompleteness**, where an improving local amendment exists within a declared amendment class. The two can interact but must not share a definition merely because both concern unrealized capability.

In finite empirical work, $A\setminus\widehat A$ is usually not directly observable because $A$ is itself unknown. Evidence can show discovered omissions relative to an independently supported transition, or bound search completeness within a declared model class. Failure to observe a transition does not classify it as inadmissible.

## 22. Composition of Dynatological Systems

For $\mathcal D_1=(S_1,\Omega_1,A_1)$ and $\mathcal D_2=(S_2,\Omega_2,A_2)$, a product state space is $S_1\times S_2$. Componentwise products of $\Omega_i$ and $A_i$ are available when the systems are independent. Coupled systems additionally require an interaction or compatibility relation, shared-resource semantics, temporal synchronization, and possibly bridge maps between state vocabularies.

Thus composition is not determined by the two triples alone. A composition profile can be written

$$
\mathcal D_1\otimes_B\mathcal D_2=(S_1\times S_2,\Omega_B,A_B),
$$

where $B$ declares the coupling. Global admissibility can be empty even when each component is locally viable, and pairwise compatibility need not imply global consistency. Claims of modular composition require explicit conservation, conflict, and evidence obligations.

## 23. Stochastic Extension

A stochastic kernel $P(s'\mid s)$ has a support relation $A_P=\{(s,s')\mid P(s'\mid s)>0\}$. This recovers possible transitions under that kernel, not automatically normative or constitutional permission. Conversely, an admissible edge can receive zero observed frequency in finite data or zero probability under one policy.

To combine stochastic dynamics with governance, retain separate objects for physical or modeled support, policy-induced probability, and authorized admissibility. Collapsing them loses the distinction between impossible, unchosen, unobserved, and prohibited.

## 24. Continuous Extension

For continuous systems, let:

$$
S \subseteq \mathbb R^n.
$$

The admissible differential inclusion is:

$$
\dot{s} \in F(s).
$$

A continuous flow can induce discrete dynatology through discretization.

Given vector field:

$$
f:S\rightarrow S
$$

and step size:

$$
\epsilon,
$$

define:

$$
A_{\epsilon}
:=
\{(s,s') \mid \|s'-(s+\epsilon f(s))\|<\delta\}.
$$

Continuous dynatology connects to control theory, viability theory, and dynamical systems.

Discrete admissibility becomes the graph approximation of continuous flow constraints.

---

## 25. Admissibility Inference Problem

Positive transition observations establish occurrence, not the entire admissibility relation. An unobserved edge can be inadmissible, rare, unreachable under the observed policy, outside the sampling budget, or omitted by measurement. Admissibility inference therefore requires a generative observation model plus some combination of negative evidence, interventions, refusal records, mechanism knowledge, or authority rules.

Given a hypothesis class $\mathcal H$, observation contract $\chi$, and data $\mathcal O$, one may estimate

$$
\widehat A=\arg\max_{A'\in\mathcal H}\Pr(\mathcal O\mid A',\chi),
$$

but the likelihood must state how $A'$ induces transition probabilities and how censoring, policy, noise, and unreachable states are handled. Indicator and distance-threshold models are useful hypothesis classes, not universal forms of admissibility. Identifiability, held-out prediction, intervention response, and uncertainty bounds are required before an inferred edge receives consequential standing.

## 26. A Worked Example

Consider a grid world.

Let:

$$
S := \mathbb Z^2.
$$

Let $\Omega$ include all conceivable moves between adjacent or non-adjacent grid positions.

Let $A$ consist only of four-neighbor movement:

$$
A = \{((x,y),(x+1,y)),((x,y),(x-1,y)),((x,y),(x,y+1)),((x,y),(x,y-1))\}.
$$

For state:

$$
s=(0,0),
$$

the continuation field is:

$$
F(s) = \{(1,0),(-1,0),(0,1),(0,-1)\}.
$$

Before any wall is added:

$$
R_C(0,0)=\infty.
$$

Now introduce a wall at:

$$
x=0
$$

blocking transitions from:

$$
(0,y)
$$

to:

$$
(1,y).
$$

The new relation is:

$$
A' \subseteq A.
$$

If the world is unbounded, the wall increases separation without making reachability finite.

If the world is bounded and the wall separates regions, then:

$$
K_D \uparrow
$$

and for states trapped inside a bounded region:

$$
R_C \downarrow.
$$

A single admissibility modification changes continuation fields, reachability distance, connected components, and viability under goal constraints.

This is a minimal dynatological event.

---

## 27. Metrics

All distributional metrics require a distribution:

$$
p:S \rightarrow [0,1]
$$

with:

$$
\sum_{s\in S}p(s)=1
$$

when $S$ is finite.

Possibility entropy is:

$$
H_P := -\sum_{s \in S} p(s)\log p(s).
$$

Possibility entropy measures uncertainty over *which state* the system occupies. It does not measure dynatological structure --- the branching of admissible futures from each state.

Dynatological entropy measures future branching directly. For state $s$, let $P_A(s' \mid s)$ be the (observed or induced) frequency of admissible transitions to $s'$. Define the per-state dynatological entropy:

$$
H_A(s) := -\sum_{s' \in F(s)} P_A(s' \mid s) \log P_A(s' \mid s).
$$

The average dynatological entropy under distribution $p$ is:

$$
\bar H_A := \mathbb{E}_{s \sim p}[H_A(s)] = \sum_{s \in S} p(s)\, H_A(s).
$$

$\bar H_A$ measures the diversity of admissible futures across the state distribution. A rigid constitution that admits few continuations per state has low $\bar H_A$; an expressive constitution with many admissible continuations has high $\bar H_A$. This metric tracks the dynatological thesis more directly than $H_P$, which is silent about future structure.

Reachability is:

$$
R_C(s) := |\{s' \mid s \leadsto s'\}|.
$$

Connectivity count is:

$$
K_D := |\{\text{connected components of }(S,A)\}|.
$$

Admissibility volume is:

$$
|A|.
$$

Let:

$$
(S,A)\cong(S',A')
$$

mean there exists a bijection:

$$
\phi:S\rightarrow S'
$$

such that:

$$
(s,s')\in A
\iff
(\phi(s),\phi(s'))\in A'.
$$

Metrics should be invariant under isomorphism when they describe structure alone:

$$
(S,A)\cong(S',A')
\Rightarrow
K_D=K_D'
$$

and:

$$
R_C(s)=R_C'(\phi(s)).
$$

Entropy is invariant when the state distribution is transported by $\phi$.

---

## 28. Propositions, Algorithms, and Claim Corrections

### Proposition 1: No Positive-Length Participation under Empty Admissibility

If $A=\emptyset$, no positive-length admissible trajectory exists. Whether a participant exists nevertheless depends on the participant definition and whether zero-length, terminal, or externally sustained participants are allowed. The graph result does not by itself settle the ontology of participants.

#### Proposition 2: Finite Infinite-Path Viability

For a finite directed graph, $s\in V_A$ exactly when $s$ can reach a directed cycle, including a self-loop. The cycle's strongly connected component need not be closed: a path may remain on a cycle even if outgoing edges also exist.

The greatest-fixed-point elimination algorithm

$$
X_{k+1}=\{s\in X_k\mid\exists s'\in X_k,\ (s,s')\in A\},\qquad X_0=S
$$

computes $V_A$. With predecessor counts and a queue of states that lose their last successor, it runs in $O(|S|+|A|)$. Alternatively, compute all cyclic strongly connected components and backward reachability from them. Searching only closed components is incorrect for existential path semantics.

#### Corollary: Monotonicity under Edge Inclusion

If $A\subseteq A'$ on the same state space and both use the same infinite-path semantics, then $V_A\subseteq V_{A'}$. The reverse inclusion holds under contraction. This is a formal set-theoretic result and does not say whether a policy, constraint rule, or performance metric realizes edge inclusion.

#### CCOO Comparison: Not an Empirical Instance of the Corollary

The source reports that an 8-neighbor local-max rule outperformed a 4-neighbor rule and a central comparator in a toy CCOO experiment. That comparison does not by itself establish $A\subseteq A'$: checking a larger neighborhood can make a local-max predicate stricter, and the reported capability or regret measure is not the viability-kernel set $V_A$. Without exact transition relations and kernel computation, the result is evidence about source-reported task performance, not an empirical verification of monotone viability expansion.

#### Proposition 3: Automorphism Invariance

A graph automorphism preserves paths, reachability, strongly connected components, and infinite-path viability. Weighted distances or probabilities are preserved only when the automorphism also preserves the corresponding weights or kernel.

#### Theorem 1: Preserved-Cycle Sufficiency

In a finite graph, if every $s\in V_A$ retains under $A'$ a path to a directed cycle retained under $A'$, then $V_A\subseteq V_{A'}$. This is a sufficient condition, close to restating the finite viability characterization; it is not a quantitative perturbation-stability theorem without a perturbation metric and robustness margin.

## 29. Relationship to Existing Fields

Dynatology provides a proposed common interpretive grammar for transition systems, reachability, viability, modal accessibility, stochastic support, control, and continuous flows. It does not subsume these fields without explicit translations that preserve their additional structures, assumptions, and theorems. An MDP includes actions, rewards, policies, and probabilities; control theory includes dynamics, controls, disturbances, and target or safety sets; category theory requires composition and identities; physical theories carry empirical quantities and laws not present in the triple.

The strongest current distinction is organizational: Dynatology centers the comparison among conceivability, admissibility, realization, refusal, and amendment across domains. Its ontological claim that structured potentiality is prior to entities is a separate philosophical hypothesis. Novelty and intellectual priority remain unestablished without external literature review.

## 30. Relationship to Computational Ontologies

Several research programs seek to derive physical law from computational substrates, including cellular automata, graph rewriting systems, and digital physics. These approaches typically begin with a generating rule and investigate the structures that emerge from repeated application of that rule.

The central inversion is ontological. Most computational ontologies treat rules, update mechanisms, or generative processes as primitive and derive possibility from their operation. Dynatology reverses this relationship. Possibility structure is treated as primary, while rules, constitutions, laws, and update mechanisms are interpreted as generators, restrictions, or transformations of admissibility relations within possibility space.

A computational ontology specifies a mechanism generating trajectories through possibility space. Dynatology studies the structure of possibility space itself. The two approaches are therefore complementary rather than competing.

In this sense, computational ontologies can be viewed as particular constructions within a broader dynatological framework.

Formally, Dynatology introduces a framework for analyzing possibility structures independent of substrate. Philosophically, it advances the stronger hypothesis that possibility structure is ontologically prior to the entities and dynamics commonly treated as fundamental.

---

## 31. Comparative Positioning

Physics studies matter.

Biology studies life.

Economics studies allocation.

Computer science studies computation.

Dynatology studies structured potentiality.

Its object is neither a substrate nor an entity.

Its object is the geometry and topology of possibility induced by admissibility.

---

## 32. Applications

Potential applications include:

* constitutional governance,
* artificial intelligence,
* biological systems,
* market design,
* institutional analysis,
* distributed computing,
* cognitive science,
* evolutionary theory.

The framework is substrate-neutral.

Only structured possibility is required.

---

## 33. Full Realization Funnel

Dynatology's $\Omega/A$/realization distinction interfaces with, but does not replace, the full corpus funnel:

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

Possibility $P$ contains conceivable formulations and realizations. Specification $S$ fixes the modeled domain, types, constraints, authority, observations, and falsifiers. **Configuration Manifold 1 (CM1)** contains configurations meeting mandatory admissibility. **Configuration Manifold 2 (CM2)** retains configurations preferred under declared objectives and risks. **IC**, expanded interchangeably as **Instance Constitution** or **Instance Configuration**, selects a governed slice. **IR**, expanded interchangeably as **Instance Realization** or **Implementation Realization**, makes that slice concrete. Evidence evaluates the realization under a claim contract; Revision updates any earlier layer while preserving lineage.

Dynatology can describe transitions within or among these stages, but $A$ should not be identified with every kind of admissibility at once. Physical feasibility, specification compliance, preference, authority, implementation behavior, and evidentiary standing require typed relations.

## 34. Corpus Placement

* *Continuation Primacy* develops the priority of continued existence and transformation; Dynatology supplies a broader possibility structure. Neither title similarity nor shared continuation language proves derivation or identity.
* *Admissibility Engineering* turns admissibility into a design discipline with explicit constraints, refusal, evidence, and implementation obligations.
* *Constitutional Incompleteness* uses a task- and amendment-relative concept distinct from Dynatology's internal-model gap.
* *Constitutional Evolution* adds authority, migration, lineage, rollback, and selection conditions missing from the bare operator $C_t\mapsto C_{t+1}$.
* CCOO applies continuation structure to distributed coordination, but its task metrics are not automatically viability-kernel measures.
* ATC applies the grammar to consciousness research while explicitly withholding phenomenal conclusions.
* *Meaning as Binding* supplies stronger semantic conditions than relation change alone.
* *Constitutional Computing* supplies the wider architecture in which constraint is productive rather than merely restrictive.

These are typed interfaces, not mutual validation.

## 35. Governed Meaning Base and Universal GSM Projection

The **Governed Meaning Base (GMB)** is the current name in the author-confirmed `CCF -> CMB -> GMB` lineage. It can host typed dynatological models, alternative boundaries, transition evidence, constraint decompositions, refusals, model uncertainty, and revision histories. It is not the possibility space itself, the authority that defines all admissibility, or proof of ontological primacy.

The universal GSM should distinguish: model, state, boundary, granularity, conceivable transition, admitted transition, observed transition, refused transition, refusal reason, constraint, constitution, authority, weight, probability kernel, policy, path, reachability class, future cone, topological closure, viability definition, viability kernel, participant projection, identity rule, meaning claim, intelligence claim, composition bridge, amendment, evidence item, claim ceiling, counterevidence, and revision.

High-value relations include `CONCEIVABLE_UNDER`, `ADMISSIBLE_UNDER`, `OBSERVED_AS`,  
`REFUSED_BY`, `JUSTIFIED_BY`, `WEIGHTED_BY`, `REACHES`, `VIABLE_UNDER`, `PROJECTS_TO`,  
`COMPOSES_THROUGH`, `REALIZES_CANDIDATE`, `SUPPORTED_BY`, `COUNTEREVIDENCED_BY`,  
and `SUCCEEDS`.

## General Grammar of Structured Possibility

The completed P1 corpus positions Dynatology as the **general grammar and research program of structured possibility, admissibility, realization, refusal, continuation, and revision**. It supplies a way to ask what can occur under which constraints and through which paths. It is not an empirically established universal science, a replacement for domain models, or proof that every domain shares one possibility geometry.

- **Adjacent work:** *Continuation Primacy*  
  **Supplies:** The analytic priority of continuation conditions in persistent systems.  
  **Dynatology boundary:** Continuation is one dynatological relation; Dynatology covers possibility, admission, path, refusal, and realization more generally.

- **Adjacent work:** *Admissibility Theory of Consciousness*  
  **Supplies:** A graded application to self-situated admissibility organization.  
  **Dynatology boundary:** ATC is a domain research program, not evidence for universal dynatological laws.

- **Adjacent work:** *Recursive Constitutional Motifs*  
  **Supplies:** A pedagogical heuristic for recurring pair, gate, and realization patterns.  
  **Dynatology boundary:** Motifs compress recurring shapes; Dynatology states the general possibility and path questions.

- **Adjacent work:** *The Optional Coordinator*  
  **Supplies:** A bounded topology and substitution thesis about coordination.  
  **Dynatology boundary:** Coordinator optionality is one testable configuration family, not a general corollary without declared premises.

- **Adjacent work:** *Semantic Legitimacy Before Context*  
  **Supplies:** Admission rules applied before semantic material enters binding context.  
  **Dynatology boundary:** Context admission is one governed cut through a wider possibility field.

A domain-specific dynatological system should bind:

$$
\begin{aligned}
D= (&domain, states, transitions, constraints, admission, \\
&path\_rules, realization\_map, observations, viability, \\
&revision)
\end{aligned}.
$$

Possible, admissible, preferred, selected, realized, observed, viable, and legitimate are different predicates. Their relations must be specified rather than arranged as an automatic ladder. A state may be physically possible but constitutionally inadmissible; admissible but undesirable; selected but unrealized; realized but unobserved; observed but nonviable; or viable under an illegitimate regime.

Cross-domain generalization requires a typed morphism that states which states, transitions, constraints, refusals, and observations are preserved. Shared vocabulary or graph shape is insufficient. A theorem proved for finite transition systems does not automatically extend to stochastic, continuous, open, reflexive, or partially observed systems.

The universal GSM can type `POSSIBLE_IN`, `ADMISSIBLE_UNDER`, `PREFERRED_UNDER`,  
`SELECTED_AS_IC`, `REALIZED_AS_IR`, `OBSERVED_BY`, `VIABLE_OVER`, `REFUSED_BY_CONSTRAINT`,  
`REACHABLE_VIA_PATH`, `MORPHISM_PRESERVES`,  
and `REVISED_BY_EVIDENCE`. Here IC and realization-stage IR use their author-confirmed interchangeable expansions.

This integration establishes four editorial commitments: adopt general grammar of structured possibility as Dynatology's official corpus role; adopt the domain-system envelope; enforce the eight-predicate non-collapse rule; and require preservation-explicit morphisms before claiming cross-domain laws.

## Preservation-Explicit Domain Morphisms and Lineage

The fixed-seed comparison with the Classified Earthworks brief, Digital Gold, CCOO, and the Epistemic Lineage Engine provides four demanding domain mappings rather than evidence for a universal law:

$$
\begin{aligned}
\phi= (&source\_domain, target\_grammar, state\_map, \\
&transition\_map, constraint\_map, refusal\_map, \\
&observation\_map, preserved, discarded, counterexample)
\end{aligned}.
$$

Earthworks routes involve material identity, site conditions, hazards, processing, placement, monitoring, and recall. Digital Gold involves monetary states, ordering, finality, forks, identity, and amendment. CCOO involves participant topology, local operators, optional aggregation, authority, and experimental environment. Each may instantiate a dynatological profile only to the extent that the mapping names what is preserved and what is lost.

The Epistemic Lineage Engine can record how a domain model, morphism, theorem candidate, experiment, counterexample, and revision changed. Lineage does not establish that the mapping is correct or that a shared graph shape has the same meaning across domains.

Failed morphisms are informative. If physical observations, economic acceptance, collective authority, stochastic openness, or partial observability cannot be carried without distortion, the general claim must narrow. The universal GSM can type   
`MAPS_DOMAIN_TO_DYNATOLOGICAL_GRAMMAR`,  
`PRESERVES_UNDER_MORPHISM`, `DISCARDS_DOMAIN_STRUCTURE`, `COUNTEREXAMPLES_GENERALIZATION`,  
`RECORDED_IN_EPISTEMIC_LINEAGE`, and   
`NARROWS_CROSS_DOMAIN_CLAIM`.

This randomized review establishes four editorial commitments: adopt the morphism object; require explicit preserved and discarded structure; use domain failures to narrow generalization; and record morphism evolution in lineage without treating ancestry as proof.

## Typed Possibility Claims and Preservation Contracts

Fourteen downstream uses apply Dynatology to consciousness research, earthworks, collectives, infrastructure, continuation, monetary systems, epistemic lineage, compilers, constitutional development, migration, qualia models, recursive motifs, and shared experience. The reuse supports a general grammar for structured potentiality, but it also makes an inference firewall necessary. A transition represented by a model is not thereby physically possible, normatively admissible, authorized, reachable from the actual state, viable over time, selected, realized, observed, or established.

The dynatological claim object is:

$$
\begin{aligned}
D^*= (&domain, state\_identity, model, observer, \\
&transition\_class, constraints, admissibility\_authority, \\
&reachability, viability, preference, selection, \\
&realization, evidence, time, uncertainty, remainder)
\end{aligned}.
$$

Every relation should state its modality and evidence basis. `CONCEIVABLE`, `REPRESENTABLE`,  
`PHYSICALLY_POSSIBLE`, `SPECIFICATION_VALID`, `ADMISSIBLE`, `AUTHORIZED`, `REACHABLE`,  
`VIABLE`, `PREFERRED`, `SELECTED`, `REALIZED`, `OBSERVED`,  
and `ESTABLISHED` are not synonyms and need not form a simple total order. Admissibility may be physical, logical, epistemic, constitutional, legal, ethical, or profile-specific; its deciding authority and claim ceiling must travel with the result.

Cross-domain use requires a preservation contract specifying mapped states, transitions, constraints, time, observers, excluded structure, and the proposition preserved in each direction. A useful morphism may preserve reachability while not preserving viability, authority, identity, probability, or meaning. Failed preservation is evidence about the mapping, not evidence that either domain lacks structure.

The universal GSM can type   
`ASSERTS_DYNATOLOGICAL_MODALITY`,  
`DISTINGUISHES_MODEL_FROM_WORLD`, `PRESERVES_REACHABILITY_UNDER_MAP`,  
`FAILS_VIABILITY_PRESERVATION`, `BINDS_ADMISSIBILITY_AUTHORITY`,  
`REALIZES_SELECTED_CONTINUATION`, `OBSERVES_WITH_UNCERTAINTY`,  
and   
`RETAINS_DYNATOLOGICAL_REMAINDER`.

This reverse-dependency review establishes four editorial commitments: adopt the typed possibility claim; require explicit domain, observer, authority, evidence, and uncertainty; require preservation contracts for cross-domain mappings; and keep ontological primacy and universal applicability as defeasible research claims rather than consequences of the notation.

## 36. Counterevidence and Falsification Program

Dynatology is weakened or narrowed if: (1) the triple adds no explanatory or predictive value beyond ordinary labeled transition systems; (2) $\Omega$ and $A$ cannot be identified independently of observed trajectories; (3) cross-domain translations discard the very structures that matter; (4) refusal reasons cannot be recovered from the negative relation; (5) participant, meaning, intelligence, or identity claims depend entirely on observer-selected boundaries; (6) topology or geometry results change under undeclared orientation or weights; (7) inference cannot distinguish prohibited from merely unobserved transitions; (8) composition requires centralized or extra-relational machinery omitted from the triple; (9) ontology claims do no work in formal or empirical results; (10) proposed metrics fail invariance or discrimination tests; (11) formal claims fail on finite counterexamples; or (12) GMB representation remains coherent while the modeled world, authority, evidence, or boundary is wrong.

## A General Grammar of Possibility Must Preserve Domain Difference

### Public orientation

Dynatology studies structured potentiality: states, continuations, admissibility, viability, refusal, and the transformations that change what can become. Its strongest current role is a general comparison grammar for possibility spaces. It is not yet an established science, an ontologically primary theory, or evidence that social, physical, biological, computational, and semantic domains share one mechanism.

### Adversarial tests

1. **Possibility-reification attack.** A modeling space is treated as a mind-independent substance or causal layer without an ontological argument and evidence.
2. **Domain-collapse attack.** State, transition, admissibility, refusal, viability, or participation is assumed to mean the same thing across incompatible domains.
3. **Constraint-legitimacy attack.** A reachable region or enforced rule is treated as normatively admissible, desirable, or authorized.
4. **Observer-completeness attack.** The modeled possibility set is treated as the full space despite unknown states, hidden transitions, novelty, and representation limits.
5. **Metric-decoration attack.** Distance, curvature, field, topology, and geometry language appears without typed operands, invariants, proofs, or empirical interpretation.
6. **Preservation-free mapping attack.** A result transfers between domains without declaring what the mapping preserves, loses, or reverses.
7. **Retrospective-fit attack.** Any outcome can be redescribed as structured potentiality, leaving no discriminating prediction or falsifier.
8. **Novelty-by-renaming attack.** Existing modal, dynamical, control, viability, planning, graph, process, or decision frameworks already supply the operative content.

### Claim and evidence ceiling

The paper supplies definitions, finite structural propositions, algorithms, and a cross-domain research program. It does not establish ontological primacy, disciplinary independence, empirical superiority, universal scope, novelty, or a shared causal mechanism. Every domain projection requires its own typed semantics, admissibility authority, preservation contract, counterexamples, and evidence.

External philosophical, mathematical, scientific, and prior-art comparison remains required. No experiment, replay, or external research was performed in this pass.

### Reader-facing consequence

Dynatology is most useful when it lets a reader ask: what futures are represented, what transitions connect them, which constraints exclude them, who or what supplies those constraints, what remains viable, and which parts of that description survive translation to another domain?

## 37. Publication Standing and Evidence Limits

## Internal Corpus References Added by This Pass

The integration custody manifest binds exact sources for *Continuation Primacy*, *Admissibility Engineering*, *Constitutional Incompleteness*, *Constitutional Evolution*, CCOO, ATC, *Meaning as Binding*, *Constitutional Computing*, and GMB documentation. These references support internal comparison only; no external research, experiment replay, or independent formal peer review occurred.

## 38. Conclusion

This paper introduces Dynatology, the study of structured potentiality.

The framework defines a formal dynatological system:

$$
\mathcal D := (S, \Omega, A)
$$

from which meaning, intelligence, identity, coordination, hierarchy, markets, and evolution emerge as derived phenomena.

Geometry is induced by admissibility over state space.

Topology is induced by reachability.

Conceivability is represented by $\Omega$.

Admissibility is represented by $A$.

Constitutions modify admissibility.

Participants instantiate admissible trajectories.

The central hypothesis:

> The deepest object of inquiry is not what exists, but the geometry and topology governing what may become.

If correct, many existing disciplines become special cases of a more general science.

That science is Dynatology.

---

## Appendix A: Formal Research Questions

1. Which topological invariants characterize possibility spaces?

2. How should admissibility be inferred empirically?

3. What classes of constitutional operators preserve dynatopology?

4. How do viability kernels evolve under admissibility perturbation?

5. Can possibility geometry be compared across substrates?

6. What constitutes a complete dynatological description?

---

## Appendix B: Initial Research Roadmap

Phase 0: Formalization of dynatological systems.

Phase 1: Admissibility inference.

Phase 2: Dynatopological invariants.

Phase 3: Viability analysis.

Phase 4: Constitutional operators.

Phase 5: Cross-domain validation.

Phase 6: Unified possibility theory.

---

---

## Editorial Provenance and Standing

### Source, Evidence, and Standing
This is an AI-prepared successor revision candidate derived from one exact author manuscript. The integration custody manifest is   
`work/paper-saturation-v1/evidence/dynatology/`

`integration-custody-manifest.v0.1.json`,  
SHA-256  
`598C75C439CF6AF814771B36C51D2E8BF68CE12F86710ED00CD47C8AB94C39AB`. The exact source remains unchanged. The Dynatology name, possibility-primacy thesis, core triple, derived domains, applications, examples, experimental narrative, research questions, and original references are author material. This pass repairs formal errors and overclaims, applies the current realization funnel and GMB terminology, maps direct corpus interfaces, adds a universal-GSM projection, and creates counterevidence and author-decision surfaces. Those changes are AI editorial or synthetic contributions until adopted.
The paper's finite-graph propositions can be assessed internally, but its ontological primacy, cross-domain usefulness, novelty, and external comparisons require separate philosophical, mathematical, and literature review. Its CCOO paragraph is retained only as a source-reported comparison: the referenced experiment does not establish a set inclusion between transition relations or measure a viability kernel. No external research or experimental replay occurred in this pass.

## Corpus-Wide Reference Positioning

This paper argues that dynatology, the study of structured potentiality. Its nearest external comparison fields are semantic, formal, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Richard Cyganiak, David Wood, and Markus Lanthaler, eds. *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation, 25 February 2014. https://www.w3.org/TR/rdf11-concepts/ **Relationship:** Adjacent graph data model and identity baseline.

**[E2]** Alistair Miles and Sean Bechhofer, eds. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. https://www.w3.org/TR/skos-reference **Relationship:** Adjacent standard for concepts, labels, schemes, notes, and semantic mappings.

**[E3]** W3C OWL Working Group. *OWL 2 Web Ontology Language Document Overview*, Second Edition. W3C Recommendation, 11 December 2012. https://www.w3.org/TR/owl2-overview/ **Relationship:** Adjacent formal ontology standard used to compare declared semantics and inference commitments.

**[E4]** Mark D. Wilkinson et al. "The FAIR Guiding Principles for Scientific Data Management and Stewardship." *Scientific Data* 3, 2016, 160018. DOI: 10.1038/sdata.2016.18. https://doi.org/10.1038/sdata.2016.18 **Relationship:** Predecessor stewardship principles for findability, accessibility, interoperability, and reuse.

**[E5]** Peter Gardenfors. *Conceptual Spaces: The Geometry of Thought*. MIT Press, 2000. [mitpress.mit.edu source](https://mitpress.mit.edu/9780262572194/conceptual-spaces/) **Relationship:** Predecessor geometric treatment of concepts; cited as comparison, not as validation of the paper's manifold terminology.

**[E6]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E7]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

### Ableman corpus

**[A1]** Adam Ableman. *Meaning as Binding*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-5F976917F0B283EA`;  
source SHA-256  
`A470D1A0B9ED7C3CEAB6BB88BE4B642A2BA36427447F787764329FD574DA0C97`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D95CCC4FB7B58BFB`;  
source SHA-256  
`A3B62E50F8BEE125FDAE0D38C2839AFD1CCC138296268BF93217481E38AA48EA`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Semantic Manifold Topology*. Ableman Corpus current edition; work identity `PAPER.PUB.20257244`;  
source SHA-256  
`B8F28CC652A73A3EE4CF6FD0E23C1ABC922A6660319B2FB4CC1CCAAA606EC64A`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Global Term Key: Identity Primitives in Governed Knowledge Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-358AC09F5A13587E`;  
source SHA-256  
`AFB29CFCB4B58A78B79709AD453CEE9088CCB2AE40F30A70260F1B54F5160579`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Semantic Legitimacy Before Context*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-091E34BA93992CE4`;  
source SHA-256  
`DEB7626CE1AB54F4B541347DCC3C4E14DC4F682230ACCCE1A93D1D536A50C44C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *MCIR: A Canonical Intermediate Representation for Governed Transformation*. Ableman Corpus current edition; work identity `PAPER.PUB.21095303`;  
source SHA-256  
`EA129ECBA95F7B07CAA7B33A54F91F52913C94A14DA227EB9A06CFD083E4E5BF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Semantic Compilation*. Ableman Corpus current edition; work identity `PAPER.PUB.18453681`;  
source SHA-256  
`5FF6C636550B04DB0E2F6F94C379BB75AA0BD8781E19B047D7D3BB6D49071AC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

### Author Works (Dynatological and Constitutional Series)

Ableman Adam Ableman (in preparation). *Continuation Primacy*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Meaning*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Intelligence*. Manuscript.

Ableman Adam Ableman (in preparation). *The Optional Coordinator*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Evolution*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Incompleteness*. Manuscript.

### External Works

Aristotle. *Metaphysics*.

Aristotle. *Physics*.

Whitehead, A. N. (1929). *Process and Reality*. Macmillan.

Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition*. D. Reidel.

Aubin, J.-P. (1991). *Viability Theory*. Birkhauser.

Holland, J. H. (1998). *Emergence: From Chaos to Order*. Addison-Wesley.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

Adam Ableman *Semantic Coordinate Identity Tokenization (SCIT).* Zenodo, 2026. doi:10.5281/zenodo.20532070

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847639](https://doi.org/10.5281/zenodo.23847639)
