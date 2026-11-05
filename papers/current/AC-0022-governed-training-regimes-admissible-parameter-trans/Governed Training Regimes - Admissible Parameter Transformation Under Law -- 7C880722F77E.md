# Governed Training Regimes: Admissible Parameter Transformation Under Law

## Admissible Parameter Transformation Under Law

### Training is reframed as semantic compilation under law: optimization is preserved, but authority over model evolution is bounded and reviewable.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern machine learning training regimes treat parameter optimization as a numerical procedure governed primarily by loss minimization. Gradients are computed, updates are applied, checkpoints are written, and evaluation metrics are inspected. Governance, where present, is external and informal-embedded in experiment tracking systems, review processes, or post-hoc audits. Parameter evolution proceeds as ambient authority over model state.

This paper introduces **Governed Training Regimes (GTR)**: a systems-level framework in which training is formalized as a sequence of **admissible parameter state transitions**. A governed regime specifies training intent canonically, constrains execution through an admissibility predicate over proposed updates, and binds state transitions to receipted evidence. Parameter updates may be refused. Checkpoints may be denied promotion. Data defines jurisdiction rather than serving as undifferentiated input.

The defining contribution of GTR is the introduction of a **first-class admissibility operator over parameter state transitions**. Training is reframed as semantic compilation under law: optimization is preserved, but authority over model evolution is bounded and reviewable.

---

## 1. Deployment Context and Threat Model

Governed Training Regimes are designed for settings characterized by:

* Large-scale foundation model training and fine-tuning,
* Multi-team artifact management,
* Incremental checkpoint promotion pipelines,
* Safety- or policy-constrained deployment environments.

In such contexts, parameter evolution has operational and governance consequences. We identify four failure classes:

* **Provenance Drift** - datasets change without canonical binding.
* **Hyperparameter Drift** - optimizer configurations vary without stable specification.
* **Regression Without Ceremony** - degraded checkpoints are promoted.
* **Authority Expansion** - parameter updates alter behavioral capacity without formal admissibility review.

Existing tools-logging systems, experiment trackers, model documentation-record outcomes but do not constrain state transitions. GTR introduces governance at the level of parameter transformation.

---

## 2. Architectural Overview

A Governed Training Regime treats each optimizer step as a proposed transition. The optimizer computes a candidate update $\Delta_t$ from $\theta_t$. An admissibility membrane evaluates
$$\mathcal{A}(\theta_t, \Delta_t, \mathcal{L}) \in \{\mathrm{ALLOW}, \mathrm{REFUSE}, \mathrm{ESCALATE}\}$$

If $\mathrm{ALLOW}$, the canonical state advances to $\theta_{t+1}$. If $\mathrm{REFUSE}$, state remains $\theta_t$ and a refusal receipt is emitted. If $\mathrm{ESCALATE}$, the proposal is routed to supervisory policy (human or automated) and may be deferred or rolled back. Episode-level checks gate whether the run may begin; promotion-level checks gate whether a checkpoint may become canonical.
Governance operates at three annotated layers:

* **Episode-Level** - prior to optimizer invocation (Training-MCIR validation).
* **Update-Level** - at the admissibility membrane.
* **Promotion-Level** - at checkpoint gating.

The optimizer proposes; admissibility governs state advancement.

---

## 3. Formal Core

Let parameter state at step $t$ be $\theta_t \in \mathbb{R}^n$.

An optimizer proposes:

$$
\Delta_t = \mathcal{O}(\theta_t, B_t, H)
$$

where:

* $B_t$ is a batch (hash-identified),
* $H$ is optimizer configuration,
* $\mathcal{O}$ is a numeric optimizer (e.g., AdamW).

Training-Law ($\mathcal{L}$) consists of:

* invariant predicates ($I_k(\theta)$),
* update constraints ($U_j(\theta, \Delta)$),
* protected parameter masks ($P(\theta, \Delta)$),
* evaluation gates ($E(\theta)$).

Define:

$$
\mathcal{A}(\theta_t, \Delta_t, \mathcal{L}) \in \{\text{ALLOW}, \text{REFUSE}, \text{ESCALATE}\}
$$

State evolution becomes:

$$
\theta_{t+1} =
\begin{cases}
\theta_t + \Delta_t & \text{if } \mathcal{A} = \text{ALLOW} \\
\theta_t & \text{if } \mathcal{A} = \text{REFUSE}
\end{cases}
$$

The ESCALATE branch may trigger:

* human review,
* automated supervisory policy,
* rollback,
* batch reprocessing.

Constrained optimization embeds constraints inside the objective.
GTR introduces an external admissibility predicate capable of refusing updates regardless of gradient direction.

---

## 4. Training-MCIR: Canonical Specification

A governed episode binds:

* dataset identity and jurisdiction,
* optimizer configuration,
* objectives,
* invariant declarations,
* evaluation rituals,
* effect surface.

Hyperparameters are law-bound declarations.

Two episodes with identical Training-MCIR must be reproducible or explainable in divergence.

---

## 5. Training-Law: Three Layers

### 5.1 Episode-Level

* Dataset verified.
* Invariants declared.
* Optimizer lawful.
* Effect surface bounded.

### 5.2 Update-Level

Checks may include:

* gradient norm bounds,
* update magnitude limits,
* protected parameter masks (e.g., safety heads, calibration layers),
* invariant preservation ($I_k(\theta_{t+1})$).

Checks may operate on:

* full vectors,
* masked subsets,
* summary statistics,
* head-level aggregates.

### 5.3 Promotion-Level

Checkpoint promotion requires:

* evaluation gates satisfied,
* regression thresholds respected,
* invariants preserved,
* evidence pack complete.

---

## 6. Training-PEIR: Regulated Execution

Execution is constrained by:

* deterministic seed policy,
* capability-scoped dataset access,
* receipted artifact persistence,
* bounded hardware interaction.

Invariant checks scale linearly and may leverage summary statistics to ensure scalability for large models.

---

## 7. Relationship to Prior Work

GTR differs from:

* Trust-region and constrained optimization - numeric bounding only.
* Differential privacy - information leakage constraints.
* Safe RL - behavioral constraints.
* Experiment tracking - recording without gating.
* Formal verification - post-training guarantees.

The defining contribution is a first-class admissibility operator over parameter state transitions.

---

## 8. Minimal Governed Optimizer Loop

delta = optimizer(theta, batch, config) decision = A(theta, delta, law)

if decision == ALLOW: theta = theta + delta elif decision == REFUSE: record_refusal(theta, delta) elif decision == ESCALATE: invoke_supervisor(theta, delta)

## Corpus-Wide Reference Positioning

This paper argues that modern machine learning training regimes treat parameter optimization as a numerical procedure governed primarily by loss minimization. Its nearest external comparison fields are ai, governance, formal. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E7]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

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

**[A6]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.18623302](https://doi.org/10.5281/zenodo.18623302)
