# Constitutional Collective with Optional Overmind (CCOO)

## A Constitutional Theory of Distributed Coordination, Emergent Agency, and Admissible Continuation

### The swarm need not know itself when its participants know what may continue.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

This paper presents the Constitutional Collective with Optional Overmind (CCOO) framework and reports preliminary empirical evidence from its experimental program. The framework treats constitutions not as policies executed by agents but as generative operators determining which continuations are admissible. Coordination is the structure of the admissible continuation relation, not the optimization of trajectories within a state space.

The framework's central distinction is that the object of governance is *continuation*, not *solution*. Unlike constraint satisfaction systems that solve for admissible states, optimization systems that seek optimal trajectories, and viability theory that imposes fixed external constraints, CCOO governs admissible trajectories through constitutional operators that are endogenously generated, locally instantiated, and compositionally constrained.

Within this framework, the paper formalizes a property the experimental program surfaced: *constitutional incompleteness*. A constitution is incomplete with respect to a task when a local amendment can reduce task cost without invoking centralized aggregation. This concept is the empirical lens through which the role of an Overmind is evaluated.

On a stationary and single-drift toy substrate, the experiments report:

- Coherent threat-response coordination by a pure local constitutional collective without any central executive.
- An apparent Overmind advantage of 30-73% regret reduction that resolves, on inspection, into compression of redundant signal-bleed rather than generation of primary coordination.
- A node-local amendment (8-neighbor local-max) that captures approximately 101% of the Overmind's gain and beats it in 56-80% of runs at the three thresholds tested -- the Overmind's advantage was constitutional incompleteness, internalizable downward by a richer local rule.
- Under a single-change-point intensity drift, the static node-local rule remains dominant; existing EMA memory does not recover; the Overmind benefit shrinks toward zero at well-calibrated thresholds.

Within the recorded caveats (stationary and single-change-point substrate; toy environment; no consciousness claims; topology-conditional completeness), the Overmind is optional, non-necessary in the regimes tested, and internalizable downward by local constitutional refinement. The framework's contribution is the lens that made this observable: continuation, not solution, is what is governed.

> Order corresponds to the structure of the admissible continuation relation rather than the optimization of trajectories within a state space.

---

## 1. Introduction

The dominant question of collective systems has historically been:

> How should a coordinator organize a population?

CCOO begins elsewhere.

It asks:

> What if the coordinator is not fundamental?

Across nature and engineering, coherent behavior routinely appears without centralized planners:

* ant colonies,
* immune systems,
* plant signaling networks,
* microbial ecologies,
* markets,
* routing protocols,
* distributed consensus systems.

These systems frequently exhibit coordinated behavior despite possessing no global observer and no executive self-model.

Traditional explanations often describe such phenomena as emergence.

CCOO attempts to describe the mechanism beneath emergence.

The central claim is simple:

> Collective order arises when participation itself becomes constitutionally governed.

---

## 2. The Constitutional Inversion

Most architectures assume:

```text
Perception
    |
Reasoning
    |
Coordinator
    |
Action
```

Even decentralized systems frequently hide a coordinator implicitly within optimization procedures, reward functions, or planning layers.

CCOO inverts this hierarchy.

```text
Constitution
      |
Admissible Continuation
      |
Node Participation
      |
Collective Dynamics
      |
(Optional Overmind)
      |
Action
```

The constitution is not a policy.

The constitution is not a planner.

The constitution is a generative operator defining which continuations remain admissible.

Nodes do not consult the constitution.

Nodes instantiate it.

---

## 3. Constitutional State Structure

Let $S$ denote the global state space.

CCOO assumes factorization:

$$
S=\prod_{i=1}^{n}S_i
$$

with projection operators:

$$
\pi_i:S\rightarrow S_i
$$

mapping global states to node-local states.

Time is indexed discretely.

Let:

$$
s_t\in S
$$

denote system state at time $t$.

Raw continuation is defined by:

$$
F_t\subseteq S\times S.
$$

The global constitutional admissibility relation is:

$$
A_t\subseteq F_t.
$$

A continuation is admissible when:

$$
(s_t,s_{t+1})\in A_t.
$$

Unlike constraint satisfaction systems, which solve for states:

$$
s^\ast\in S,
$$

CCOO governs admissible trajectories:

$$
(s_t,s_{t+1})\in A_t
\quad
\forall t.
$$

The object of governance is therefore continuation rather than solution.

CCOO differs from fixed viability theory and constrained dynamical systems in that admissibility is endogenously generated, locally instantiated, and compositionally constrained rather than externally specified as a fixed viability kernel.

This three-part distinction is the novelty firewall against three nearby formalisms. **Against viability theory**: viability kernels are typically treated here as externally specified viability constraints on a dynamical system; CCOO's admissibility relation is generated by constitutional operators carried by the participants themselves and may change as constitutions evolve (Section 13). **Against distributed constraint optimization (DCOP)**: DCOP seeks assignments that optimize an objective under distributed constraints; CCOO requires no scalar objective and treats the question "what may continue" as primitive rather than derivative of "what maximizes reward." **Against constrained dynamical systems**: constrained dynamical systems impose constraints from outside the system's dynamics; CCOO's constraints are compositional in the sense of Section 7, generated by local node operators and combined through an explicit interaction graph rather than imposed globally. Whenever CCOO is described in subsequent sections, these three contrasts are what distinguish it from the nearest existing formalism in each direction.

---

## 4. Constitutional Continuation

CCOO introduces a constitutional operator:

$$
C:(S,H,\Theta)\rightarrow\mathcal P(S\times S)
$$

where:

* $S$ is the current state,
* $H$ is constitutional history,
* $\Theta$ is constitutional parameterization,
* $\mathcal P$ denotes the power set.

Then:

$$
A_t=C(s_t,h_t,\theta_t).
$$

To preserve locality and prevent collapse into replay-based governance, history is constrained.

Each node maintains bounded history:

$$
h_i\in H_i^{(k)}
$$

or equivalently a sufficient statistic:

$$
\sigma_i=\Sigma(h_i).
$$

The sufficient statistic is bounded:

$$
|\sigma_i|\leq c
$$

and non-invertible:

$$
\Sigma^{-1}(\sigma_i)
$$

contains multiple possible histories.

Thus $\sigma_i$ cannot reconstruct the full trajectory.

Constitutions may therefore be state-dependent, history-dependent, and amendable without requiring unbounded replay of system history.

Admissibility is not required to be derivable from scalar optimization.

In particular, CCOO does not require existence of a global objective:

$$
U:S\rightarrow\mathbb R
$$

such that admissible transitions are exactly those that maximize $U$.

Transitions outside $A_t$ are not prohibited.

They are constitutionally undefined.

This distinction is fundamental.

Traditional systems frequently model failure as a state.

CCOO models failure as the withdrawal of admissible continuation itself.

Order therefore emerges through admissibility rather than enforcement.

---

### 5. Constitutional Execution Semantics

The admissibility relation induces a partial dynamical system. Let $(S,A_t)$ denote the constitutional transition structure at time $t$. The semantic model treats a proposed transition outside $A_t$ as constitutionally undefined. This does not mean the physical, institutional, or software substrate is incapable of producing it. A realization enforces the constitutional boundary only when an execution mediator actually refuses, contains, repairs, or terminates the proposed effect.

For a current state $s_t$, let the typed proposal resolver be

$$
R_t:S\rightarrow S\cup\{\bot\},
$$

where $\bot$ denotes constitutional non-continuation. Extend it by definition with $R_t(\bot)=\bot$ when idempotence is discussed. A successful result must satisfy

$$
R_t(s_t)=s_{t+1}\Rightarrow(s_t,s_{t+1})\in A_t,
$$

and when no admissible continuation is available it returns $\bot$. A concrete resolver may project to an admissible successor, invoke declared repair, escalate, or terminate, but each path requires a visible authority and evidence contract.

Local candidate resolvers do not compose by an unqualified Cartesian product. They propose a tuple that must also satisfy the compatibility relation:

$$
R_t(s_t)=
\begin{cases}
s' & \text{if }\forall i,\ s_i'=R_{i,t}(s_{i,t})\ \text{and }(s_t,s')\in A_t,\\
\bot & \text{otherwise.}
\end{cases}
$$

The resolver may be idempotent on its extended codomain,

$$
R_t(R_t(s))=R_t(s),
$$

but idempotence, locality, and admissibility do not by themselves prove that hidden optimization is absent. That stronger claim requires inspection of the resolver, dependencies, information flows, objectives, and receipts.

## 6. Nodes as Constitutional Participants

Nodes possess:

* local observations,
* local state,
* communication channels,
* constitutional constraints.

Nodes need not possess:

* global awareness,
* centralized authority,
* self-models,
* representations of the collective.

Each node participates through local admissibility evaluation.

Formally:

$$
P_i:O_i\rightarrow T_i.
$$

Node-local constitutional operators satisfy:

$$
C_i:
(S_i,H_i,\Theta_i)
\rightarrow
\mathcal P(S_i\times S_i).
$$

Locality requires $C_i$ to depend only on:

* $\pi_i(s)$,
* bounded neighborhood state,
* $h_i$ or $\sigma_i$.

Local admissibility becomes:

$$
A_{i,t}=C_i(s_{i,t},h_{i,t},\theta_{i,t}).
$$

Collective behavior emerges through interaction among admissible local continuations.

---

## 7. Composition of Admissibility

A central challenge for constitutional collectives is the composition of local admissibility into globally coherent continuation.

Local admissibility alone is insufficient.

Distinct nodes may independently authorize transitions that are mutually incompatible.

Let:

$$
G=(V,E)
$$

denote the constitutional interaction graph.

For each local admissibility relation:

$$
A_{i,t}\subseteq S_i\times S_i,
$$

define the cylinder lift:

$$
A_{i,t}^{\uparrow} = \{(s,s') \in S \times S \mid (s_i, s_i') \in A_{i,t}\}.
$$

CCOO introduces a compatibility relation:

$$
\Phi_t(s,s') = \bigwedge_{(i,j) \in E} \phi_{ij,t}(s_i, s_j, s_i', s_j').
$$

Global admissibility is defined by:

$$
A_t = \left( \bigcap_i A_{i,t}^{\uparrow} \right) \cap \Phi_t.
$$

Equivalently:

$$
(s,s')\in A_t
\iff
\forall i,
(s_i,s_i')\in A_{i,t}
\land
\Phi_t(s,s').
$$

Compatibility therefore factorizes over local interactions rather than arbitrary global logic.

When $G$ contains cycles, pairwise compatibility may not imply global compatibility. CCOO therefore requires either:

* acyclic interaction structure,
* junction-tree-style consistency,
* or an explicit global consistency condition on $\Phi_t$.

This preserves the distributed character of constitutional participation without silently collapsing the model into centralized admissibility.

---

## 8. Viability Conditions

Not every constitution admits continuation.

CCOO therefore introduces viability requirements.

Strong viability:

$$
\forall s\in S,
\exists s'
\text{ such that }
(s,s')\in A_t.
$$

A weaker condition requires existence of at least one infinite admissible path:

$$
(s_0,s_1,s_2,\ldots)
$$

such that:

$$
(s_t,s_{t+1})\in A_t
\quad
\forall t.
$$

Constitutions violating both conditions are constitutionally degenerate.

A local deadlock is distinct from global collapse.

Deadlock occurs when:

$$
\exists s\in S
\text{ such that }
{s'\mid (s,s')\in A_t}=\emptyset.
$$

Global collapse occurs when:

$$
A_t=\emptyset.
$$

Deadlock may be local, reachable, and repairable.

Collapse means the admissibility relation itself no longer supports continuation.

---

## 9. Continuation Topology

To support robustness and stability analysis, CCOO equips the state space with additional structure.

Let:

$$
(S,d)
$$

or equivalently:

$$
(S,\tau)
$$

represent a metric or topological state space.

The admissibility relation:

$$
A_t
\subseteq
S\times S
$$

should be closed under the induced topology.

Constitutional operators should satisfy perturbation robustness.

If:

$$
(s_t,s_{t+1})\in A_t
$$

and:

$$
d(s_t,\tilde{s}_t)<\epsilon,
$$

then there should exist:

$$
\tilde{s}_{t+1}
$$

such that:

$$
(\tilde{s}_t, \tilde{s}_{t+1}) \in A_t
$$

and:

$$
d(s_{t+1},\tilde{s}_{t+1})<\eta.
$$

This expresses an upper-hemicontinuity-style constraint on constitutional continuation.

Small perturbations in state should not induce discontinuous collapse of admissibility.

This provides a continuity foundation for stability analysis and constitutional amendment.

---

### 10. Meaning-Binding as Structural Participation

CCOO uses a bounded operational profile from the corpus's meaning-binding family:

> A distinction is continuation-relevant when it changes the admissible continuation relation.

Let $\Delta:S\rightarrow\{0,1\}$ represent a distinction. Its admissibility sensitivity is witnessed when

$$
A_{\Delta,t}\triangle A_t\neq\emptyset,
$$

or, relative to a declared measure $\mu$,

$$
\mu(A_{\Delta,t}\triangle A_t)>0.
$$

This supports a claim about **causal or constitutional relevance**: the distinction participates in selecting what may continue. It does not, without additional criteria, settle whether the distinction carries semantic content, is understood by a subject, has legitimate authority, or has phenomenal character. Plants, immune cells, routing nodes, and robots can therefore instantiate this operational profile without the paper claiming that all instantiate one undifferentiated kind of human-like meaning.

The distinction matters because a collective can coordinate through distributed continuation-relevance without a centralized representation. The stronger philosophical identity between this profile and meaning remains an author claim and an empirical and conceptual research question.

### 11. Constitutional Incompleteness

The experimental program surfaced a bounded comparison concept: a constitution may be viable and coherent yet leave capability that a richer local rule could capture without central aggregation.

#### Definition

Given a task $\tau$, an environment and topology $e$, an evaluation contract $\chi$, and a declared local amendment class $\mathcal L$, a constitution $C$ is **witnessed incomplete** when there exists $C'\in\mathcal L$ such that:

1. $C'$ reduces the declared task cost relative to $C$ under $\chi$;
2. $C'$ remains within the declared locality, memory, information, and authority bounds;
3. $C'$ uses no additional global state or central aggregation forbidden by the comparison contract; and
4. the result is supported by reproducible evidence within the stated seed, parameter, and topology scope.

A recovered local amendment is a positive witness of incompleteness within that scope. The converse is not available by failed search alone. If no amendment is found, the warranted result is only:

> No improving amendment was found within amendment class $\mathcal L$, search procedure $q$, budget $b$, environment $e$, and evidence contract $\chi$.

It does not establish irreducible centralization or global constitutional completeness. Such a closure claim would require an exhaustive or otherwise justified completeness result for the declared amendment space.

#### Topology and Comparison Dependence

Completeness is relative to the task, topology, observation model, cost, admissibility regime, amendment class, and search budget. A constitution can be witnessed incomplete for one profile and unresolved for another. The paper's local-max result is therefore evidence that one measured Overmind advantage was internalizable within the tested topology; it is not a theorem that all Overmind functions are locally internalizable.

### 12. The Optional Overmind

The Overmind is modeled as an optional proposing and parameterization role, not as a sovereign. Formally, $O:S\rightarrow\Theta$ may propose $\theta_{t+1}$, but a proposal acquires effect only through a declared delegation and amendment path:

$$
\theta_{t+1}=\operatorname{Admit}_{D,A,E}(O(s_t),\theta_t),
$$

where $D$ is delegated scope, $A$ the applicable authority and admissibility contract, and $E$ the evidence obligation. Rate limits such as

$$
d_{\Theta}(\theta_t,\theta_{t+1})\leq\epsilon
$$

are useful but insufficient. Non-sovereignty also requires transparent proposal identity, bounded jurisdiction, local refusal where the constitution grants it, revocation or exit, no unilateral manufacture of standing, auditable information access, and recovery from bad amendments.

The statement that an Overmind changes parameters rather than state does not by itself remove control: changing future admissibility can indirectly control future state. The authority surface must therefore govern both direct effects and parameter-mediated effects.

Within the source-reported toy profile, the tested central contribution appears optional because a named local amendment matched or exceeded its dominant benefit. Outside that profile, optionality remains a hypothesis to test. Claims that an Overmind may emerge or disappear without invalidating the collective also require explicit collective-identity and continuity criteria.

### 13. Constitutional Evolution

Let $\mathcal C$ be a space of constitutions and let $M_{t\rightarrow t+1}$ be a declared migration relation from states governed by $C_t$ to states governed by $C_{t+1}$. Mere nonempty overlap $A_t\cap A_{t+1}\neq\emptyset$ is too weak: the shared transition may be unreachable from the current system, may strand protected obligations, or may not support rollback.

An amendment candidate should instead state at least:

1. the authority and jurisdiction that may amend $C_t$;
2. preserved invariants and obligations;
3. a migration relation for reachable current states;
4. continued or explicitly terminated admissible paths;
5. evidence, rollback, recovery, and failure semantics; and
6. a bound such as $d_{\mathcal C}(C_t,C_{t+1})\leq\epsilon_{\mathcal C}$ when the metric has operational meaning.

The amendment is continuity-preserving only within the states and obligations covered by that contract. Constitutional evolution is therefore a governed bridge between revisions, not simply motion through a metric space of constitutions.

### 14. Proposition Candidates and Proof Obligations

#### Proposition Candidate 1: Global Continuation under Join-Consistent Local Admissibility

For a fixed current state $s$, define each node's candidate successor set

$$
D_i(s)=\{s_i'\mid(s_i,s_i')\in A_{i,t}\}.
$$

Nonempty $D_i(s)$ and separate edge-wise satisfiability are not enough to imply one globally compatible tuple: the assignments that satisfy different incident edges can conflict. A sufficient theorem therefore needs a stronger condition, such as a join tree whose cluster relations are nonempty and pairwise consistent on every separator, or an explicit globally consistent relation $\Phi_t$ with

$$
\left(\prod_iD_i(s)\right)\cap\Phi_t(s,\cdot)\neq\emptyset.
$$

Under that condition, a globally admissible successor exists by construction. Establishing weaker sufficient assumptions, computational complexity, and distributed witness construction remains a proof obligation.

#### Proposition Candidate 2: Robust Retention of a Declared Invariant Set

Closedness of $K$ and $A_t$, pointwise viability in $K$, and an informal upper-hemicontinuity-style condition do not alone establish trajectory-level stability under repeated perturbation. A valid result must quantify perturbations and require robust controlled invariance. One possible assumption is that there exist $\epsilon,\eta>0$ and a selection or resolver $r_t$ such that for every $s$ within $\epsilon$ of $K$ and every allowed disturbance, $r_t(s)$ is admissible and remains within $\eta$ of $K$, with a recurrence bound that prevents error accumulation.

Under a specified metric, disturbance model, time horizon, and recurrence inequality, a stability theorem may then be proved. Until those objects and bounds are supplied, this section records proposition candidates rather than established theorems.

## Bounded Collective Architecture and Experimental Subject

The completed P1 corpus clarifies CCOO's role: it is a **bounded collective architecture and experimental subject** for questions about constitutional continuation and optional higher-order coordination. It is not the general theory of coordinator optionality, continuation, split authority, or governance incentives.

- **Adjacent work:** *The Optional Coordinator*  
  **Supplies:** Function decomposition, substitution, displaced burden, and relative-necessity tests.  
  **CCOO boundary:** CCOO supplies one architecture and experiment to which those tests can be applied.

- **Adjacent work:** *Continuation Primacy*  
  **Supplies:** Reachable, admissible, viable, and terminal continuation vocabulary.  
  **CCOO boundary:** CCOO instantiates a continuation model; its results do not establish the general thesis.

- **Adjacent work:** *Split-Authority AI Coordination*  
  **Supplies:** Separation of proposal, evaluation, authorization, execution, and review powers.  
  **CCOO boundary:** An optional Overmind can still conceal concentrated authority unless powers are decomposed.

- **Adjacent work:** *Governance Incentive Engineering*  
  **Supplies:** Analysis of incentives created by recognition, evidence, and institutional structure.  
  **CCOO boundary:** Lower regret or coordination cost does not establish aligned incentives or legitimacy.

A CCOO experimental profile should bind:

$$
Q=(N,K,O,A,T,R,E),
$$

where $N$ is the participant set and topology, $K$ the local constitutional operators, $O$ the optional Overmind function bundle, $A$ the authority distribution, $T$ the task and environment, $R$ the resource and communication regime, and $E$ the evaluation and evidence protocol. Changing any element may produce a different experiment rather than a replication.

Corpus integration strengthens three boundaries. First, endogenous amendment does not self-legitimate: the authority to amend and the rights of affected participants must be specified. Second, an Overmind may be computationally optional while its information, memory, arbitration, or accountability functions remain necessary and displaced. Third, a toy result supports only the named topology, drift regime, objective, baselines, and measurement procedure.

The universal GSM can type `PARTICIPATES_IN`, `GOVERNED_BY_LOCAL_OPERATOR`,  
`COORDINATED_BY`, `OPTIONALLY_AGGREGATED_BY`, `AMENDED_BY`, `DISPLACES_FUNCTION_TO`,  
`MEASURED_UNDER`,  
and `CONTESTED_BY`. The CCOO identity should remain separate from experimental runs, parameter configurations, result records, and broader collective-governance concepts.

This integration establishes four editorial commitments: adopt bounded collective architecture and experimental subject as CCOO's official corpus role; adopt the seven-part experimental profile; require authority and rights to accompany endogenous amendment claims; and route general coordinator-necessity claims to *The Optional Coordinator* rather than repeating them here.

## Experimental Lineage and Cross-Domain Restraint

The fixed-seed comparison with Digital Gold, Dynatology, the Epistemic Lineage Engine, and the seventeen-system software evidence study strengthens CCOO as an experimental subject rather than a universal collective theory:

$$
\begin{aligned}
X= (&architecture, configuration, run, environment, seed, \\
&authority\_distribution, measurements, artifacts, \\
&lineage, interpretation, standing, remainder)
\end{aligned}.
$$

Dynatology supplies a typed possibility, admissibility, path, refusal, realization, and viability grammar for the experiment. The Epistemic Lineage Engine should bind configuration, code and artifact heads, environment, operations, observations, branches, interpretations, replay class, and revision so later results cannot silently replace predecessors.

Digital Gold is a distinct monetary-automaton thesis. Similar distributed or constitutional language does not transfer consensus, security, identity, economic, or experimental evidence. The seventeen-system study is a different evidence object about existing software structures and also has no direct bearing on CCOO performance.

Those two nonrelations are part of the result. Randomized adjacency should expose false analogy as well as useful interface. The universal GSM can type   
`INSTANTIATES_DYNATOLOGICAL_EXPERIMENT`,  
`RECORDED_AS_LINEAGE_EPISODE`, `BINDS_RUN_CONFIGURATION`, `RETAINS_INTERPRETIVE_REMAINDER`,  
`HAS_NO_MATERIAL_RELATION_TO_MONETARY_AUTOMATON`,  
and   
`HAS_NO_MATERIAL_RELATION_TO_SOFTWARE_CORPUS_`  
`STUDY`.

This randomized review establishes four editorial commitments: adopt the run-level experimental object; bind CCOO results to exact epistemic lineage; preserve the Dynatology interface as a typed profile; and record nonrelations to Digital Gold and the software evidence study.

## 15. Experimental Program

The CCOO research program proceeds through five branches.

### Branch 1 - Overmind Characterization

Conditions:

* Stateless aggregation
* Memory-bearing aggregation
* Performance-monitoring aggregation

Question:

> What capabilities does an increasingly sophisticated Overmind provide?

### Branch 2 - Constitutional Collective

Conditions:

* No Overmind
* Local constitutional participation
* Local bounded memory

Question:

> Can coherent collective behavior emerge without central coordination?

### Branch 3 - Collective + Optional Overmind

Question:

> Does the Overmind contribute capabilities unavailable to the collective itself?

### Branch 4 - Non-Stationary Worlds

Question:

> When do memory and adaptation become necessary?

### Branch 5 - Constitutional Evolution

Question:

> How can constitutions amend themselves without abandoning constitutional admissibility?

---

## 16. Experimental Findings: Stationary and Single-Drift Toy Substrate

The branches in Section 15 have been partially executed against a stationary toy environment (2D mesh, gated pure-transducer perception nodes, typed-token signaling with decay, action-and-cost model, deterministic seeded receipts). The findings below are retained as source-reported preliminary results under the explicit caveats stated at the end of this section. The short report labels are not independently verifiable from the artifacts recovered in this review package.

### 16.1 Branch 1: Overmind Ladder (Central Aggregation Characterization)

Two conditions on a central aggregator were characterized:

- **Condition A** (stateless central executor). Naive frozen constitution ($threshold = 1.0$) over-fires, producing false-positive-dominated regret. The population-tuned static threshold basin centers near 2.5 (single-seed thresholds of 2.0 are seed-fitted, not robust). Named static constitutions: $A_{naive}$ ($threshold = 1.0$) and $A_{candidate}$ ($threshold = 2.5$).

- **Condition B** (stateful central executor; exponential-moving-average signal memory). On the stationary environment, memory is a *tuning substitute*: it beats $A_{naive}$ but offers no advantage over the well-tuned $A_{candidate}$. The best stationary $B$ collapses to memory decay near zero. The hypothesized payoff of memory (adaptivity under drift) is tested separately in Branch 4 below.

### 16.2 Branch 2: Constitutional Collective (Pure Local Participation)

Pure local constitutional participation ($CC1$: no node memory, no central state) achieves coherent threat-response coordination without any central executive on the stationary environment.

### 16.3 Branch 3: Collective + Optional Overmind (Stationary; Report Hash 1d8047b8)

The Overmind under test has two possible acts:

- **Contradiction resolution.** Tiny refinement (a handful of resolutions per run; a few regret units beyond suppression). Matches the prior expectation.
- **Redundancy suppression.** Large effect: cuts $CC1$ regret by 30-73% across thresholds (e.g. at $threshold = 1.0$, regret falls from 1259 to 344) by removing signal-bleed false positives the local collective structurally cannot self-remove under the frozen four-rule constitution.

The Overmind here only *compresses* --- it withdraws redundant defends --- and does not generate the primary threat-detection coordination, which the collective produces.

A node-local amendment was then tested: a local-max clause requiring a node to act only if its signal magnitude is the maximum within a neighborhood.

- **4-neighbor local-max** (report hash $ec4a1565$): internalizes 53-62% of the Overmind gain. The residual is a stencil artifact, since orthogonal diffusion creates diagonal secondary maxima a 4-neighbor stencil cannot see.
- **8-neighbor local-max** (report hash $1f2ecf85$): captures 101.3%, 100.6%, and 101.3% of the Overmind gain at thresholds 1.0, 2.0, and 2.5 respectively (100 seeds each), and beats the Overmind in 80%, 56%, and 53% of runs (ties: 19%, 38%, 40%). The 8-neighbor stencil matches the diagonal leakage structure of 4-connected diffusion.

The verdict registered for all three thresholds (registry text): "8-neighbor local-max captures $\geq$ 90% of the Overmind gain. The residual was a stencil artifact; the Overmind's win is mostly constitutional incompleteness, internalizable downward by a slightly richer local rule."

This is the empirical instantiation of Section 11: the gap closed by a node-local amendment evidenced constitutional incompleteness rather than irreducible centralization.

### 16.4 Branch 4: Non-Stationary Worlds, drift1 (Report Hash 69073b79)

A single-change-point intensity-regime drift was applied at step 150 of 300: pre-drift threat-spawn intensity ranged over $[1, 5]$; post-drift over $[2, 4]$ (option-A drift, staying within the emitting band). 100 seeds. No new adaptive thresholding or new memory semantics were introduced; existing $CC2$ EMA memory was included as a comparator.

- $CC1_{local\_max\_8}$ remains the best static rule under drift (post-drift mean regret $\approx 9.29$ at $threshold = 1.0$; do-nothing ratio $\approx 0.012$). Win rate against $CC1$: 1.00 across thresholds 1.0, 2.0; 0.52 at threshold 2.5 where the static threshold begins to under-fire.
- Existing $CC2$ EMA memory does **not** recover: across all 100 seeds, 0/100 win rate vs. $CC1_{local\_max\_8}$ in the post-drift window (smoothing is not adaptation).
- Overmind benefit shrinks but is not magnitude-neutral: relative gain swings with regime redundancy (0.97 / 0.93 / -0.01 across thresholds 1.0 / 2.0 / 2.5 post-drift). The Overmind never becomes necessary.
- The only crack observed: a high static threshold under-fires in the weaker post-drift regime (false-negative rate up). This *motivates* an adaptive-threshold probe in a later branch but does not authorize one in this paper.

Sub-gate drift indicates an observability/projection boundary rather than an action-admissibility failure.

### 16.5 Recorded Caveats

The following caveats are explicit in the experimental record and apply to every finding above. They are stated here rather than buried per-section because the framework's reach is governed by them.

1. **Stationary and single-change-point substrate only.** Findings extend to non-stationary regimes only as Branch 4+ probes them.
2. **No consciousness claims.** The program evaluates admissibility, continuation governance, collective coordination, and optional aggregation. It does not evaluate consciousness, selfhood, phenomenology, or subjective experience.
3. **No promotion.** No constitution or rule is promoted to a general claim; findings are scoped to the seeds, parameters, and topology under which they were measured.
4. **Toy environment.** The substrate is a finite 2D mesh with simple threat dynamics. Generalization to richer participation topologies, sparser meshes, or qualitatively different dynamics is open.
5. **Topology-conditional completeness.** The 8-neighbor local-max rule works in this experiment because the 8-neighbor stencil matches the diagonal leakage structure of 4-connected diffusion. The constitutional lesson is that admissibility rules must fit the participation topology; the rule itself is not claimed to be universal.
6. **The Overmind's apparent advantage is a property of the frozen constitution under which it was measured.** A constitution that suppresses redundancy node-locally shrinks the Overmind's edge. This is an amendment question (Section 11), not evidence that the Overmind is intrinsically capability-generating in all constitutions.

### 16.6 Summary

Within the bounds of these caveats, the experiments support a reading the original framework anticipated only as a hypothesis: in the regimes tested, coordination capability migrated downward as the constitution became more complete. The collective without an Overmind matched or exceeded the Overmind-augmented collective on the dominant lever of the environment, and a static local rule remained dominant across the one drift regime tested. The Overmind, where measured, was optional, non-necessary, and internalizable downward by local constitutional refinement.

The source-reported findings are summarized below. All numbers are described by the source as 100-seed means on the stationary substrate unless otherwise noted. The labels are retained for possible future binding to an experimental archive; in this package they are short source labels, not verified content hashes.

- **Branch:** Branch 1  
  **Probe:** Stateful central (EMA memory)  
  **Key finding:** Tuning substitute only; collapses to decay $\approx 0$ at well-tuned static threshold  
  **Hash:** --

- **Branch:** Branch 2  
  **Probe:** Pure local collective ($CC1$)  
  **Key finding:** Coherent threat-response coordination without central executive  
  **Hash:** --

- **Branch:** Branch 3  
  **Probe:** Overmind, redundancy suppression  
  **Key finding:** Cuts $CC1$ regret 30--73% by removing signal-bleed false positives  
  **Hash:** $1d8047b8$

- **Branch:** Branch 3  
  **Probe:** 4-neighbor local-max amendment  
  **Key finding:** Captures 53--62% of Overmind gain; residual is a diffusion-diagonal stencil artifact  
  **Hash:** $ec4a1565$

- **Branch:** Branch 3  
  **Probe:** 8-neighbor local-max amendment  
  **Key finding:** Captures 101% of Overmind gain; beats Overmind in 53--80% of runs across thresholds  
  **Hash:** $1f2ecf85$

- **Branch:** Branch 4  
  **Probe:** drift_1 (intensity change-point)  
  **Key finding:** $CC1_{local\_max\_8}$ remains best static rule; EMA memory does not recover (0/100)  
  **Hash:** $69073b79$

---

## 17. Generalized Minimal Executable Model

Section 16 reports a specific instantiation of an executable model already built and run. This section sketches the more general class of minimal models the framework admits, of which the threat-detection coordination probed in Section 16 is one instance.

A minimal executable model may be constructed using finite-state agents operating under local admissibility rules.

Example:

* agents occupy a grid,
* movement remains admissible only when local density remains below threshold $k$,
* no reward function is supplied,
* no centralized controller exists.

Observed quantities include:

* clustering,
* phase transitions,
* deadlock,
* constitutional collapse,
* stability under perturbation,
* admissible path entropy.

Control comparisons should include:

* reward optimization,
* random policy,
* fixed-rule execution.

The purpose of the model is not optimization.

The purpose is to determine whether coherent collective structure emerges from admissibility alone.

---

### 18. Metrics for Constitutional Collectives

The following are measurement families, not definition-complete metrics until their domains and sampling contracts are declared.

#### Binding Density

For finite transition sets, $|A_t|/|F_t|$ is defined when $|F_t|>0$. For continuous or infinite spaces, replace cardinality with an identified measure and state its normalization.

#### Constitutional Integration

$I(A_{i,t};A_{j,t})$ is meaningful only after defining random variables, a probability distribution or empirical sampling process, and what observation of a relation means. Structural overlap or constraint dependence may be preferable when no stochastic model exists.

#### Stability

$d(s_t,s^*)\rightarrow0$ requires an equilibrium $s^*$, a metric, a trajectory or policy, and convergence conditions. Collective stability may instead concern invariant sets, boundedness, recurrence, or recovery.

#### Renegotiability

For finite sets, $|A_{\theta'}\cap A_\theta|/|A_\theta|$ measures retained old admissibility when the denominator is nonzero. It is directional, not symmetric, and does not measure amendment legitimacy, reversibility, or migration safety. Infinite spaces again require a measure.

#### Coherence, Propagation, and Path Entropy

Constitutional coherence needs an equivalence relation over circumstances and a disagreement rule. Constraint propagation depth needs a declared influence graph. Admissible path entropy

$$
H_A=-\sum_{(s,s')\in A_t}p(s,s')\log p(s,s')
$$

requires a normalized distribution and sampling frame. High entropy can indicate expressive continuation or uncontrolled variation; low entropy can indicate useful precision or overconstraint. Interpretation is profile-dependent.

## 19. Failure Modes

Constitutional systems may fail in multiple distinct ways.

### Global Admissibility Collapse

$$
A_t=\emptyset
$$

### Local Deadlock

$$
\exists s\in S
\text{ such that }
{s'\mid (s,s')\in A_t}=\emptyset.
$$

### Fragmentation

The admissibility relation decomposes into disconnected components.

### Oscillatory Admissibility

Continuation cycles persist without convergence.

### Overconstraint

$$
|A_t|\rightarrow0
$$

### Underconstraint

$$
A_t\approx F_t
$$

### Resolution Dominance

System behavior becomes governed primarily by $R_t$ rather than $A_t$.

In this regime the constitution becomes decorative rather than operational.

### Objective Capture

A scalar objective silently determines continuation, reducing constitutional admissibility to disguised optimization.

---

## 20. Comparative Positioning

CCOO differs from four nearby framings: it does not assume self-modeling is required for coherent collective behavior; it treats coordination as a property of admissible participation rather than executive control; it introduces explicit governance structure rather than relying solely on emergent local heuristics; and it prioritizes admissibility over optimization. The central question becomes "What may continue?" rather than "What maximizes reward?"

---

## 21. Relation to Existing Formalisms

CCOO has bridges to several formal traditions. The most important comparisons are with the formalisms it could be mistaken for and is not.

### Constraint Satisfaction

Constraint satisfaction seeks states $s^\ast \in S$ satisfying constraints. CCOO governs admissible trajectories $(s_t, s_{t+1}) \in A_t\ \forall t$. The primitive is continuation, not state.

#### Distributed Constraint Optimization

Distributed constraint optimization seeks assignments that optimize an objective under distributed constraints. CCOO does not require a scalar objective and does not treat coordination as maximization. Its primitive is admissible continuation.

#### Control Theory and Viability

Viability kernels and invariant-preserving trajectories are CCOO's closest formal neighbor. The distinction is that viability kernels are typically treated here as externally specified viability constraints on a dynamical system, whereas CCOO's admissibility relation is generated by constitutional operators carried by the participants themselves and may evolve (Section 13).

#### Other Bridges

Process calculi describe allowed continuation traces; type systems describe type-correct state transitions; category theory describes morphisms between states with hom-set restrictions. CCOO has natural bridges to each, but these are correspondences rather than equivalences -- the novelty in CCOO is not its translatability into these formalisms but its decomposition of admissibility into local operators with compositional structure.

## 22. Applications

Potential application domains include:

* swarm robotics,
* autonomous vehicle fleets,
* distributed sensor networks,
* planetary exploration systems,
* decentralized AI collectives,
* biological modeling,
* institutional governance,
* resilient infrastructure systems.

The architecture is substrate-neutral.

Only admissible continuation is required.

---

### 23. Realization Funnel

CCOO can be expressed through the full corpus funnel:

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

* **Possibility:** conceivable collective structures, including incoherent, harmful, centralized, nonviable, and unrealizable variants.
* **Specification:** roles, topology, state and transition types, locality, authority, admissibility, compatibility, viability, evidence, refusal, and falsification obligations.
* **Configuration Manifold 1 (CM1):** every configuration satisfying the mandatory specification, including undesirable but not prohibited realizations.
* **Configuration Manifold 2 (CM2):** the preferred region under declared objectives and risk posture, such as minimizing unnecessary centralization while preserving robustness and recovery.
* **IC:** the selected **Instance Constitution** or **Instance Configuration** for one environment, topology, task, and authority profile.
* **IR:** the concrete **Instance Realization** or **Implementation Realization** of that same selected stage. The two IR expansions are current and interchangeable; wording alone does not change the stage.
* **Evidence:** observations, reports, receipts, counterexamples, and claim ceilings bound to the realized profile.
* **Revision:** amendments to any earlier stage with retained lineage and explicit migration.

The source-reported experiment is an IR-and-Evidence claim only if its implementation and exact results can be bound. In the present package those artifacts were not recovered, so the manuscript describes such a claim but does not independently establish it.

### 24. Corpus Placement

CCOO is a coordination-domain profile of the larger constitutional-computing program, not a replacement for that program.

1. *Constitutional Computing* supplies the wider thesis that capability can be generated inside explicit constraints; CCOO specializes it to distributed continuation.
2. *Admissibility Engineering* supplies the design discipline for turning constraints, refusals, and evidence obligations into operational selection surfaces.
3. *Terminability* sharpens CCOO's $\bot$ result: legitimate continuation includes the capacity to stop, escalate, or remain unresolved.
4. *Sovereign Software* contributes inspectability, renegotiability, exit, and reconstruction requirements for implementations that claim participant sovereignty.
5. *The Well-Governed Mind* is an adjacent agent-level governance architecture. A constitutional collective and a governed mind may compose, but neither is automatically an instance of the other.
6. *Semantic Legitimacy Before Context* prevents a locally useful signal, parameter, or narrative from gaining standing through usefulness alone.
7. *Governance Witnesses* motivates exact evidence for authority, admission, refusal, and effect. It does not substitute a receipt for truth.
8. *Meaning as Binding* supplies a nearby meaning-binding theory; CCOO uses only the bounded continuation-relevance profile unless the stronger theory is separately defended.

### 25. Governed Meaning Base and Universal GSM Projection

The **Governed Meaning Base (GMB)** is the current name in the author-confirmed `CCF -> CMB -> GMB` lineage. A GMB can host CCOO specifications, constitutions, topology, delegations, amendments, claims, source artifacts, reports, receipts, counterevidence, and revision lineage. It is not the collective, the Overmind, the constitutional authority, or proof that a realization conforms.

The universal GSM should distinguish at least: collective, node, role, local and global state, raw transition, local admissibility relation, compatibility predicate, global admissibility relation, resolver, refusal, topology, neighborhood, constitution, amendment, migration relation, Overmind proposal, delegation, authority, task, cost function, observation contract, report, receipt, evidence item, claim, claim ceiling, effect, failure, and revision.

High-value typed relations include `CARRIES`, `GENERATES`, `LIFTS_TO`, `COMPATIBLE_WITH`,  
`COMPOSES_INTO`, `PROPOSES_AMENDMENT`, `AUTHORIZED_BY`, `REFUSED_BY`, `MIGRATES_THROUGH`,  
`REALIZES_CANDIDATE`, `OBSERVED_BY`, `SUPPORTED_BY`, `COUNTEREVIDENCED_BY`,  
and `SUCCEEDS`. Every consequential relation requires origin class, scope, standing, source or evidence basis, and revision identity.

## Optional Coordination Without Optional Accountability

Eight retained downstream uses position CCOO as one bounded collective architecture within continuation theory, Dynatology, monetary automata, epistemic lineage, qualia-boundary testing, optional coordination, work custody, and software-evidence studies. The evidence supports a comparison among local-only, centrally aggregated, and optionally coordinated systems on declared toy environments. It does not establish a universal collective law, social legitimacy, collective consciousness, or the superiority of an overmind outside those conditions.

The collective configuration is:

$$
\begin{aligned}
K^*= (&participants, local\_constitutions, shared\_rules, \\
&environment, coordination\_problem, \\
&overmind\_capabilities, invocation\_conditions, \\
&proposal\_protocol, adoption\_authority, local\_refusal, \\
&dependency\_graph, custody, exit, recovery, evidence, \\
&inequality, capture, remainder)
\end{aligned}.
$$

An overmind is optional only if the collective can identify its dependency, refuse or remove it under the declared profile, preserve mandatory local and shared constraints, and reach a safe continuation or explicit terminal condition. Intermittent use does not establish optionality when training, identity, keys, registries, communication, recovery, or goal definition remain centrally controlled. Conversely, locality alone does not establish autonomy, coordination quality, fairness, or resilience.

Experiments should compare matched information, compute, communication, and authority budgets across local, mandatory-central, and optional-central conditions. Measures should include task outcome, viability, deadlock, fragmentation, oscillation, latency, resource inequality, minority constraint preservation, hidden coordination burden, capture, exit cost, recovery, and performance under drift. The overmind may propose, summarize, route, or simulate without acquiring adoption authority unless separately granted.

The universal GSM can type   
`INSTANTIATES_CCOO_PROFILE`, `INVOKES_OPTIONAL_OVERMIND`,  
`RETAINS_LOCAL_REFUSAL`, `DEPENDS_ON_HIDDEN_COORDINATOR`, `EXERCISES_OVERMIND_EXIT`,  
`MEASURES_COORDINATION_INEQUALITY`, `RECOVERS_WITHOUT_CENTRAL_NODE`,  
and   
`DOES_NOT_INFER_COLLECTIVE_CONSCIOUSNESS`.

This reverse-dependency review establishes four editorial commitments: adopt the collective configuration record; define operational optionality through removal and recovery; require matched authority and resource budgets plus inequality and capture measures; and preserve separate gates for institutional legitimacy, participant sovereignty, and consciousness claims.

### 26. Counterevidence and Falsification Program

The proposal is weakened or narrowed if any of the following survives serious testing:

1. CCOO can be reduced without explanatory loss to ordinary distributed constraints, viability, control, or optimization under a renamed objective.
2. Local constitutional operators cannot be identified independently of the behavior they are invoked to explain.
3. The composition rule cannot produce global successors without effectively centralized consistency solving.
4. Resolver or compatibility machinery reintroduces the hidden coordinator the architecture claims to avoid.
5. Reported local advantages disappear under preregistered seeds, richer topologies, alternate costs, adversarial disturbances, or exact replication.
6. An Overmind contributes information, memory, counterfactual search, or cross-scale repair that cannot be internalized within the declared locality and resource bounds.
7. Parameter control functions as sovereign state control despite the direct-state prohibition.
8. Constitutional amendments lack authority, safe migration, rollback, or recovery and therefore merely rename online policy updates.
9. Admissibility sensitivity classifies trivial causal differences as meaning while missing semantically important but behaviorally dormant distinctions.
10. Collective identity cannot be preserved or adjudicated across node replacement, topology change, constitutional revision, Overmind emergence, or partition.
11. The proposed metrics change with arbitrary representation or measure choices and fail to predict operational outcomes.
12. The GMB can represent a coherent CCOO account while its sources, evidence, authority, or implementation claims are wrong.

### 27. Publication Standing and Evidence Limits

### Internal Corpus References

**[I1]** Ableman Adam Ableman *Constitutional Computing.* Exact source,  
SHA-256  
`A1EF0D1F7B5DF84A107E986421EAA95827AEDCB801B7DA63F72BEECA6047BE8D`.

**[I2]** Ableman Adam Ableman *Sovereign Software.* Exact source,  
SHA-256  
`D8A2707865C6636485A564546D91F2CCF45AAC80161B94AC56A3DA5CF2EB2C13`.

**[I3]** Ableman Adam Ableman *Terminability.* Exact source,  
SHA-256  
`DB5709B17A67DD138D2438C73978E33679FB866B97F5CD15144CEDBAEA27C74C`.

**[I4]** Ableman Adam Ableman *Admissibility Engineering.* Exact source,  
SHA-256  
`FA80D5895A569839958193735B754BE62EE20E1B399A06CB3BA959614DEBF7A3`.

**[I5]** Ableman Adam Ableman *The Well-Governed Mind.* Exact source,  
SHA-256  
`E94A1667686262FFC639B18488E9517BDA1DA5ECF2FA4A92973B834B8F81643B`.

**[I6]** Ableman Adam Ableman *Semantic Legitimacy Before Context.* Exact source,  
SHA-256  
`1E9058F212FCB00E42E35E927DF2E7F830BC9C9499AAFF469FE65FF8AE137B68`.

**[I7]** Ableman Adam Ableman *Governance Witnesses.* Exact source,  
SHA-256  
`A4F1E85FB60F8A92218109EC44700DFE76B74DAAE0D65FF2B200E34A16FA9AB7`.

**[I8]** Ableman Adam Ableman *Meaning as Binding.* Exact source,  
SHA-256  
`A9EA6370E77A71A997F1D1CAC18EF6213125C6F3E13BEEBC9F5E8BFB94FE0B45`.

**[I9]** Ableman Adam Ableman *Integrating Semantic Manifold Topology.* Exact GMB documentation source,  
SHA-256  
`49A05A424F226A21C81D638727E1165DE1AD55AB1CBDC56EA65D67A1362A4B08`.

**Reference-status note.** These are internal corpus references. No external research, experimental replay, independent replication, peer review, publication, or implementation verification occurred in this pass.

### 28. Conclusion

CCOO proposes a constitutional inversion: coordination is the structure of the admissible continuation relation, not the optimization of trajectories within the state space. Nodes need not know the whole; they need only know how to continue.

The framework began as a hypothesis about the optional status of central coordinators. The experimental program (Section 16) provides preliminary evidence under explicit caveats. In the regimes tested, coordination capability migrated downward as the constitution became more complete: a local-max amendment internalized the Overmind's dominant contribution, and a static local rule remained dominant under the drift regime probed. The Overmind, where measured, was optional, non-necessary, and internalizable.

This shift -- from "the Overmind may be optional" stated as hypothesis to "the Overmind was internalizable" stated as empirical observation under named caveats -- is what the paper's experimental program contributes beyond the framework itself. The framework supplied the lens; constitutional incompleteness (Section 11) supplied the concept; the experiments supplied the evidence.

The purpose of CCOO is not to eliminate coordinators. It is to determine whether coordinators are necessary, and to provide both a framework for that determination and an instance in which it can be carried out. The result for the stationary substrate is one data point. Branch 4 preliminarily extends to non-stationary regimes (drift_1, characterized); Branch 5, on constitutional evolution, remains future work.

The central hypothesis, as before:

> Order corresponds to the structure of the admissible continuation relation $A_t$, not the optimization of trajectories within the state space $S$.

What the experiments add is that, in the regimes so far tested, this relation appears to be locally instantiable to a degree the framework originally treated as an open question.

---

## Optional Coordination Requires Demonstrable Exit

### Public orientation

CCOO studies whether a distributed collective can govern admissible continuation locally while using a central coordinator only when it adds a bounded capability. The central figure called an Overmind may summarize, route, compress, or propose. It is optional only when participants retain adoption authority and the collective can remove it, recover, and continue or terminate safely.

### Adversarial tests

1. **Hidden-coordinator attack.** Identity, keys, training, registries, communication, goal definition, recovery, or compatibility remain centrally controlled even when action selection is local.
2. **Nominal-optionality attack.** The Overmind is invoked intermittently but cannot be removed without unacceptable loss, lockout, or unsafe state.
3. **Locality-as-sovereignty attack.** Local computation is treated as participant autonomy despite inherited rules, unequal resources, unavailable exit, or ungoverned infrastructure.
4. **Resource-budget attack.** Local and central conditions receive unequal information, compute, communication, memory, or authority and their performance is compared as architecture.
5. **Minority-erasure attack.** Global coherence or regret reduction suppresses a locally valid constraint, dissent, safety boundary, or participant right.
6. **Toy-result inflation attack.** Source-reported stationary and single-drift results are generalized without exact code, seeds, configurations, receipts, replication, or richer environments.
7. **Objective-capture attack.** Constitutional admissibility becomes a renamed scalar optimization objective or evaluator preference.
8. **Collective-consciousness attack.** Coordination, shared state, emergence, or an Overmind is treated as evidence of collective experience, selfhood, or moral status.

### Claim and evidence ceiling

The paper contributes a formal collective architecture, an operational test for optional coordination, and source-reported toy experiments. It does not establish universal coordinator eliminability, institutional legitimacy, fairness, participant sovereignty, collective identity, consciousness, or superiority over ordinary distributed control and optimization.

The numerical findings remain source-reported until their exact reports, code, seeds, configurations, receipts, and result calculations are bound and independently replayed. Broader claims require external literature research, matched-resource experiments, adversarial environments, removal-and-recovery exercises, and affected-participant governance. No external research was added in this pass.

### Reader-facing consequence

The public standard for an "optional" central intelligence is practical: can the collective identify the dependency, refuse its proposal, remove it, recover without it, and preserve every mandatory constraint and participant boundary?

## Appendix A: Formal Research Questions

1. What minimal constitutional structures generate stable collective behavior?

2. What classes of collective coordination require an Overmind?

3. What capabilities emerge from local constitutional participation alone?

4. How does bounded memory alter admissibility dynamics?

5. Under what conditions does constitutional evolution remain admissible?

---

## Appendix B: Initial Experimental Roadmap

Phase 0: Infrastructure validation.

Phase 1: Overmind characterization.

Phase 2: Pure constitutional collective.

Phase 3: Collective plus optional Overmind.

Phase 4: Non-stationary environments.

Phase 5: Constitutional evolution.

---

---

## Editorial Provenance and Standing

### Source, Evidence, and Standing
This is an AI-prepared successor revision candidate derived from one exact author manuscript. The integration custody manifest is   
`work/paper-saturation-v1/evidence/`

`constitutional-collective-optional-overmind/`  
`integration-custody-manifest.v0.1.json`,  
SHA-256  
`8DFB520D4E18577DBEAB78227141C573C1117105B63FB99C5EE6EA5A50A4799B`. The exact source remains unchanged. The framework, terminology, formal architecture, experimental narrative, numerical results, caveats, examples, applications, and original references are author material. This pass repairs several formal overclaims, applies the current realization funnel and Governed Meaning Base terminology, maps direct corpus interfaces, adds a universal-GSM projection, and exposes counterevidence and author-decision surfaces. Those changes are AI editorial or synthetic contributions until adopted.
The manuscript names four short report labels for its experimental findings. A bounded search of the supplied Mosaic roots recovered no separate report, receipt, code, seed list, configuration, or result artifact bearing those labels. The numerical results are therefore preserved as **source-reported findings**, not independently verified evidence. External citations were not researched or validated in this pass.
The paper's strongest supported standing in this package is a formal research architecture with source-reported toy results. It does not establish that all distributed systems are constitutional collectives, that every coordinator is eliminable, that the Overmind is universally unnecessary, that admissibility sensitivity is sufficient for semantic meaning, or that any implementation conforms to CCOO.

## Corpus-Wide Reference Positioning

This paper argues that the Constitutional Collective with Optional Overmind (CCOO) framework and reports preliminary empirical evidence from its experimental program. Its nearest external comparison fields are governance, distributed, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Convergence and consensus establish agreement under a fault model; they do not establish that the agreed state is true, authorized, desirable, or semantically equivalent. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E2]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E3]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Leslie Lamport. "Time, Clocks, and the Ordering of Events in a Distributed System." *Communications of the ACM* 21(7), 1978, pp. 558-565. DOI: 10.1145/359545.359563. https://lamport.azurewebsites.net/pubs/time-clocks.pdf **Relationship:** Foundational predecessor for partial order, causality, and distributed event ordering.

**[E6]** Leslie Lamport, Robert Shostak, and Marshall Pease. "The Byzantine Generals Problem." *ACM Transactions on Programming Languages and Systems* 4(3), 1982, pp. 382-401. DOI: 10.1145/357172.357176. https://doi.org/10.1145/357172.357176 **Relationship:** Predecessor fault model for agreement under adversarial or inconsistent participants.

**[E7]** Marc Shapiro et al. *A Comprehensive Study of Convergent and Commutative Replicated Data Types*. INRIA Research Report RR-7506, 2011. https://inria.hal.science/inria-00555588 **Relationship:** Predecessor convergence model for replicated state; convergence is compared with, but not equated to, legitimacy or semantic agreement.

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

**[A6]** Adam Ableman. *Mosaic Internet Protocol (MIP)*. Ableman Corpus current edition; work identity `PAPER.PUB.20115615`;  
source SHA-256  
`C56A63A0B84816BF8AF602C7467221B467312339ACE5F77DB754F804ABF833C0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Optional Coordinator*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-727469A6944DA256`;  
source SHA-256  
`92E8F6743B8DDAFF369D2F40120A384DDE273613B12B27D2FC14610469F5A46E`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

### Author Works (Constitutional Framework Series)

Ableman Adam Ableman (in preparation). *Ableman's Consciousness Ontology (ACO)*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Computing*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Operating Systems*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Robotics*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Semantic Crystallization*. Manuscript.

Ableman Adam Ableman (in preparation). *Constraint-Bound Inference and Invariant Extraction*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Science*. Manuscript.

### External Works

Dennett, D. C. (1987). *The Intentional Stance*. Cambridge, MA: MIT Press.

Holland, J. H. (1998). *Emergence: From Chaos to Order*. Reading, MA: Addison-Wesley.

Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. Boston Studies in the Philosophy of Science, Vol. 42. Dordrecht: D. Reidel Publishing Company.

Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge: Cambridge University Press.

### Related Literatures (Representative Citations)

Bonabeau, E., Dorigo, M., & Theraulaz, G. (1999). *Swarm Intelligence: From Natural to Artificial Systems*. New York: Oxford University Press. *(swarm intelligence)*

Hutchins, E. (1995). *Cognition in the Wild*. Cambridge, MA: MIT Press. *(distributed cognition)*

Stone, P., & Veloso, M. (2000). Multiagent systems: A survey from a machine learning perspective. *Autonomous Robots*, 8(3), 345-383. *(multi-agent reinforcement learning)*

Aubin, J.-P. (1991). *Viability Theory*. Boston: Birkhauser. *(viability theory; comparator formalism, Section 21)*

Yokoo, M. (2001). *Distributed Constraint Satisfaction: Foundations of Cooperation in Multi-agent Systems*. Berlin: Springer. *(distributed constraint optimization; comparator formalism, Section 21)*

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Semantic Crystallization.* Zenodo, 2026. doi:10.5281/zenodo.20310115

Adam Ableman *Constraint-Bound Inference and Invariant Extraction.* Zenodo, 2026. doi:10.5281/zenodo.18175271

Adam Ableman *Semantic Manifold Topology.* Zenodo, 2026. doi:10.5281/zenodo.20257244

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847504](https://doi.org/10.5281/zenodo.23847504)
