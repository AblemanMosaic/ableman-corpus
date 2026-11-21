# Constraint-Bound Inference and Invariant Extraction

## Order as a Property of Non-Continuation

### The resulting form of knowledge - negative certainty - establishes order under chaos without assuming global predictability, convergence, optimality, or teleology.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Chaotic systems fail to produce order not primarily because of incorrect local transitions, but because continuation persists beyond the domain where governing constraints meaningfully apply. This paper introduces **Constraint-Bound Inference (CBI)**, **Continuation-Bound Constraint (CBC)**, and **Invariant Extraction Under Constraint (IEUC)** as a unified mathematical technique for extracting order from such systems. The framework replaces prediction, optimization, and control with a structural notion of admissibility: motion - conceptual or operational - is permitted only where continuation remains defined. Governed continuation relations are formalized, constraints are defined as properties preserved under admissible motion, and IEUC is presented as a collapse-driven invariant discovery operator. The resulting form of knowledge - **negative certainty** - establishes order under chaos without assuming global predictability, convergence, optimality, or teleology.

---

## 1. Continuation as the Primitive Disorder

In many chaotic systems, instability does not arise from incorrect local transitions, but from the absence of termination semantics. Continuation is treated as a default right. Motion persists not because it is warranted, but because nothing requires it to justify itself.

This pattern appears across learning systems that retrain on their own outputs, distributed infrastructures that propagate stale or inconsistent state, economic simulations where feedback amplifies rather than dampens, and governance mechanisms where escalation never triggers because no condition formally fails. In each case, continuation itself becomes the dominant causal force.

Most responses attempt to restore order by refining prediction, strengthening control, or optimizing trajectories. These approaches presuppose that order must be driven into the system. This paper advances a colder premise: in chaotic systems, order is encountered only when continuation is withdrawn. Structure appears not in what the system does next, but in what it is no longer permitted to do.

---

## 2. Formal Core

### 2.1 State Space and Continuation

Let $S$ be a state space.

Let
$$
F \subseteq S \times S
$$
be the raw continuation relation, where $(s,s') \in F$ denotes that $s'$ is a possible successor of $s$ absent governance.

Let
$$
C \subseteq S
$$
be a constraint manifold representing admissible states.

The governed continuation relation is defined as
$$
F_C = \{(s,s') \in F \mid s \in C \wedge s' \in C\}.
$$

A continuation step is admissible if and only if it lies in $F_C$. No semantics are assigned to transitions outside this relation. They are not errors, failures, or low-probability outcomes. They are **undefined**.

Undefined transitions generate no artifacts, cannot be reasoned about, ranked, or compared, and terminate the space of admissible inference rather than merely halting execution. Undefinedness, rather than falsity, is the governing semantic outcome. This is not semantic minimalism but resistance to interpretive capture: silence is not converted into evidence.

---

### 2.2 Constraint-Bound Inference

Inference is modeled as path construction in the directed graph $(C, F_C)$.

An inference step is admissible if it corresponds to an edge in $F_C$. Any inference that would require leaving $C$ is undefined rather than penalized, deprioritized, or corrected.

Most systems treat inference as free and execution as regulated. Constraint-Bound Inference breaks this assumption. Inference itself is an act that must justify its own continuation. What may be inferred at all is conditional on admissible motion.

This constitutes a reversal of epistemic burden: **continuation must explain itself**.

The inferential horizon is determined not by confidence thresholds, stopping heuristics, or optimization criteria, but by where continuation remains defined.

---

### 2.3 Continuation-Bound Constraint

Constraints are defined as properties of admissible continuation rather than predicates checked after transition.

Let
$$
I : S \to \{0,1\}
$$
be a predicate over states.

The predicate $I$ is a continuation-bound constraint if
$$
\forall (s,s') \in F_C,\quad I(s)=1 \Rightarrow I(s')=1.
$$

In this first sense, invariants appear as preservation properties: predicates that survive all admissible motion.

If $I(s)=1$ and no $s'$ exists such that $(s,s') \in F_C$, then continuation from $s$ is impossible: $s$ is a **collapse point** under $F_C$, which IEUC uses to recover necessary conditions for admissible motion.

Constraint violation is therefore a non-state: the absence of any valid next state. Continuation-bound constraints govern motion by withdrawing permission, not by issuing prohibitions.

---

### 2.4 Invariant Extraction Under Constraint

Invariant Extraction Under Constraint is the mechanism by which invariants are discovered through collapse rather than posited axiomatically.

An invariant is any predicate $I : S \to \{0,1\}$ preserved under all admissible continuations:
$$
\forall (s,s') \in F_C,\quad I(s)=1 \Rightarrow I(s')=1.
$$

In IEUC, invariants reappear under a second aspect: not merely as preservation properties, but as survivors of collapse.

Continuation is repeatedly attempted under $F_C$. States from which no admissible successor exists mark collapse points. Collapse is not merely a graph-theoretic boundary; it is an epistemic event. It is the moment where continuation can no longer conceal the structure governing it, forcing necessary conditions for motion to become explicit.

IEUC characterizes predicates whose violation is necessary for such collapse and retains those predicates preserved under all admissible continuations. The resulting invariants are structurally necessary relative to the explored continuation space, observation granularity, and constraint manifold. They are not guaranteed to be unique or globally minimal.

Collapse may reflect either exhaustion of admissibility or limits of observation and probing. IEUC records only non-traversability, not truth. It does not claim the world ends here; it claims that this way of moving cannot proceed silently.

They are earned. Continuation is allowed to speak until it contradicts itself.

---

### 2.5 Structural Properties

**Proposition 1 (Conjunction closure of IEUC invariants).**
The family of invariants discovered by IEUC is closed under finite conjunction.

If $I_1$ and $I_2$ are preserved under all admissible continuations, then $I_1 \land I_2$ is also preserved.

This closure allows invariant structure to accumulate incrementally without introducing inconsistency or overconstraint, even under partial or adversarial exploration.

---

## 3. A Perverse Example of Collapse

Let
$$
S = \mathbb{R}^2
$$
with raw continuation defined by
$$
(x,y) \mapsto (x+1,y-1).
$$

Define a scoring function
$$
J(x,y) = x - y,
$$
which strictly increases under raw continuation. A naïve optimizer would permit unbounded continuation.

Let the constraint manifold be
$$
C = \{(x,y) \in S \mid |x| + |y| \le 10\}.
$$

IEUC extracts the invariant
$$
I(x,y) := (|x| + |y| \le 10).
$$

Within $C$, continuation improves the score while gradually exhausting admissibility. At the boundary, continuation ceases not because optimization failed, but because legitimacy did.

Only collapse reveals the invariant. In the IEUC view, this invariant is not assumed; it is recovered as the necessary condition for continuation to remain defined within $C$.

Prediction and optimization succeed while admissibility quietly erodes.

---

## 4. Geometry and Modality of Non-Continuation

Each state carries a modality determined by the existence or absence of admissible successors. Possibility corresponds to continuability. Necessity corresponds to preservation under all admissible motion.

The governed continuation relation induces a topology-like structure over (S). Admissible regions are closed under continuation. Collapse points function as semantic boundaries rather than failure states.

Invariants are not truths asserted about the system. They are what remains speakable once illegitimate continuations are withdrawn.

---

## 5. Negative Certainty

The framework does not aim to predict outcomes, guarantee convergence, or ensure optimal trajectories. It yields **negative certainty**: knowledge of where continuation is impossible.

Negative certainty is asymmetric. It does not accumulate authority or license overreach. It bounds what a system may claim, infer, or propagate, rather than what it must achieve.

In chaotic environments where prediction fails and control backfires, negative certainty is the only form of certainty that remains reliable.

---

## 6. Relation to Adjacent Frameworks

This framework is adjacent to safety properties, viability kernels, partial transition systems, and partial functions in computability theory. It diverges along three axes.

Constraints are not assumed to be fully specified a priori, but are discovered through collapse. Constraint violation yields undefinedness rather than falsity or error. Inference itself, not merely execution, is structurally bound to admissible continuation.

These differences shift constraints from external checks to internal conditions of motion, meaning, and authority.

In governed reasoning systems, (F_C) can be read as the set of legally admissible continuations, and invariants discovered by IEUC become candidate governance constraints on future inference and action.

---

## 7. Continuation, Power, and Refusal

Continuation is not neutral. In systems with asymmetric power, the ability to continue - to propagate state, inference, or commitment without interruption - is itself a form of authority.

Silence is a form of motion. Unchallenged continuation is governance.

Constraint-Bound Inference prevents powerful systems from laundering continuation through inference. Continuation-Bound Constraint ensures that escalation, binding, reuse, and memory propagation cannot proceed without admissibility. Invariant Extraction Under Constraint provides a method for discovering the boundaries of legitimate action by forcing continuation to confront its own limits.

This framework refuses to guarantee good outcomes, fairness, or safety. It does not prevent harm. It does not optimize for benevolence. It ensures only that harm cannot proceed without leaving a trace, because it cannot proceed silently.

---

## 8. Conclusion

Constraint-Bound Inference, Continuation-Bound Constraint, and Invariant Extraction Under Constraint together form a mathematical technique for extracting order from chaotic systems by withdrawing continuation as a default right.

Order is not imposed. It is encountered at the boundary where motion becomes undefined.

The framework does not conquer chaos. It waits for chaos to exhaust its permissions - and listens to the silence that follows.

---

## Appendix A - Mathematical Lineage of Constraint-Bound Inference

*Order discovered through restricted continuation and forced collapse*

### Purpose

This appendix documents canonical mathematical instances in which knowledge is obtained **not by unconstrained construction**, but by **restricting admissible continuation** and extracting certainty from the boundary where continuation collapses. These examples span antiquity to modern mathematics and demonstrate a recurring epistemic maneuver: **truth is revealed by what cannot continue**.

The goal is not to claim historical authors “used CBI,” but to show that **CBI names and unifies a move mathematics has repeatedly relied on**, often implicitly.

---

## A.1 Classical Foundations

### Euclid - Euclid's Algorithm (Greatest Common Divisor)

* **Continuation stream:** Repeated reduction of two numbers by replacing one with a remainder.
* **Admissibility constraint:** Each reduction step must preserve the common divisor.
* **Collapse boundary:** The process must terminate when the remainder becomes zero.
* **Invariant extracted:** The final non-zero remainder is the greatest common divisor.
* **CBI reading:** Order is revealed by allowing only reductions that preserve a constraint; termination exposes the invariant.

---

### Euclid - Infinitude of Primes

* **Continuation stream:** Attempt to complete a finite enumeration of all primes.
* **Admissibility constraint:** Closure under multiplication and addition by one.
* **Collapse boundary:** Any finite list can be extended to a contradiction.
* **Invariant extracted:** No finite continuation can exhaust the primes.
* **CBI reading:** Non-termination is not failure; it is the structural conclusion.

---

### Euclid - Incommensurability (Irrationality) Proofs

* **Continuation stream:** Reduction of ratios to a “fully simplified” form.
* **Admissibility constraint:** A fully reduced form must terminate.
* **Collapse boundary:** Repeated divisibility contradicts termination.
* **Invariant extracted:** The assumed rational continuation is inadmissible.
* **CBI reading:** A claim to completion collapses under a preserved invariant.

---

### Archimedes - Method of Exhaustion

* **Continuation stream:** Refining upper and lower bounds by admissible approximations.
* **Admissibility constraint:** The true value must remain between the bounds.
* **Collapse boundary:** The gap can be made arbitrarily small.
* **Invariant extracted:** The value is determined by what survives all admissible refinements.
* **CBI reading:** Knowledge is fixed by refusing continuation that violates enclosure.

---

## A.2 Early Modern Non-Continuation Techniques

### Pierre de Fermat - Infinite Descent

* **Continuation stream:** Constructing ever-smaller solutions from an assumed solution.
* **Admissibility constraint:** Positive integers cannot descend indefinitely.
* **Collapse boundary:** Infinite descent contradicts well-ordering.
* **Invariant extracted:** The original solution cannot exist.
* **CBI reading:** Continuation is forbidden by the termination semantics of the domain.

---

### Reductio ad Absurdum (Proof by Contradiction)

* **Continuation stream:** Extend an assumption through admissible logical steps.
* **Admissibility constraint:** Logical consistency must be preserved.
* **Collapse boundary:** Contradiction.
* **Invariant extracted:** The negation of the assumption.
* **CBI reading:** Continuation is pursued until it loses the right to exist.

---

## A.3 Structural Limits and Indistinguishability

### Georg Cantor - Diagonal Argument

* **Continuation stream:** Attempt to enumerate an entire class (e.g., real numbers).
* **Admissibility constraint:** Enumeration claims completeness.
* **Collapse boundary:** Construction of an element not in the list.
* **Invariant extracted:** No enumeration continuation can be complete.
* **CBI reading:** Any compressed listing merges distinctions; collapse exposes the blind spot.

---

### Kurt Gödel - Incompleteness

* **Continuation stream:** Attempt to prove all truths within a formal system.
* **Admissibility constraint:** Consistency of the system.
* **Collapse boundary:** Self-reference forces undecidable statements.
* **Invariant extracted:** Truth exceeds admissible proof continuation.
* **CBI reading:** Continuation under internal warrants cannot cover the full semantic space.

---

## A.4 Modern Mathematics: Explicit Constraint-Bound Invariants

### Compactness Arguments (Analysis / Topology)

* **Continuation stream:** Construct sequences of approximations.
* **Admissibility constraint:** Boundedness / compactness prevents escape.
* **Collapse boundary:** Without the constraint, continuation dissipates.
* **Invariant extracted:** Existence or convergence emerges from permitted continuation.
* **CBI reading:** Existence proofs are permission proofs.

---

### Energy Methods & A Priori Estimates (PDEs)

* **Continuation stream:** Extend solutions forward in time.
* **Admissibility constraint:** Certain quantities must remain bounded.
* **Collapse boundary:** Blow-up is continuation failure.
* **Invariant extracted:** Conserved or controlled quantities govern existence.
* **CBI reading:** Continuation is conditional, not assumed.

---

### Lyapunov Functions (Dynamical Systems)

* **Continuation stream:** Trajectories evolve over time.
* **Admissibility constraint:** A monotone quantity cannot increase.
* **Collapse boundary:** Motion must settle into a constrained set.
* **Invariant extracted:** The limiting set is determined by non-violation.
* **CBI reading:** Stability is what remains when motion is restricted.

---

### Grigori Perelman - Ricci Flow with Surgery

* **Continuation stream:** Geometric evolution of manifolds.
* **Admissibility constraint:** Singularities invalidate free continuation.
* **Collapse boundary:** Forced stop at singularities.
* **Invariant extracted:** Topological information preserved across regulated continuation.
* **CBI reading:** Collapse is acknowledged and continuation resumes only under explicit rules.

---

### Embedded Contact Homology (ECH) - Constraint-Bound Invariant Construction

*(Illustrated via David Michael Farris, PhD dissertation, 2011)*

* **Continuation stream:** Study geometric structures by varying them within a tightly controlled class of admissible deformations.
* **Admissibility constraint:** Only specific, well-defined geometric configurations are allowed to contribute to the invariant; unauthorized configurations are excluded by definition.
* **Collapse boundary:** If admissibility rules are relaxed, the construction ceases to produce a stable or well-defined outcome.
* **Invariant extracted:** A deformation-robust homological invariant that remains unchanged under all admissible continuations.
* **CBI reading:** Embedded Contact Homology exemplifies constraint-bound inference: knowledge is obtained not by free geometric exploration, but by *restricting continuation* and extracting what survives all permitted deformations. Farris’ dissertation provides a concrete, modern instance of this epistemic move in practice.

*ECH was developed by Michael Hutchings and others; the reference to Farris highlights a concrete dissertation-level instantiation where the constraint-bound nature of the construction is particularly transparent.*

---

### Closing (Appendix A)

Across these examples, mathematical certainty arises not from free exploration, but from **disciplined refusal**. Continuation is allowed only while constraints hold; invariants are revealed at the boundary where continuation must stop.

---

## Appendix B - Constraint-Bound Inference Beyond Mathematics

*Continuation, authority, and refusal in operational systems*

### Purpose

This appendix shows that the same epistemic move - **restricting continuation and treating collapse as informative** - reappears in systems where action, not just truth, is at stake.

---

## B.1 Computer Science & Software Systems

### Type Systems

* **Continuation stream:** Program execution.
* **Admissibility constraint:** Only well-typed programs may run.
* **Collapse boundary:** Type error halts execution.
* **Invariant extracted:** Safety properties preserved by typing.
* **CBI reading:** Execution is a privilege, not a default.

---

### Formal Verification

* **Continuation stream:** Program behaviors.
* **Admissibility constraint:** Verified preconditions.
* **Collapse boundary:** Unverified paths are disallowed.
* **Invariant extracted:** Correctness within proven bounds.
* **CBI reading:** Behavior is defined only under warrant.

---

## B.2 Governance & Institutions

### Policy Drift

* **Continuation stream:** Policies remain binding over time.
* **Admissibility constraint:** Continued relevance and evidence.
* **Collapse boundary:** Conditions change, but policy persists.
* **Invariant extracted:** Institutional inertia without warrant.
* **CBI reading:** Unauthorized continuation accumulates epistemic torque.

---

### Escalation Failures

* **Continuation stream:** Local decisions become binding.
* **Admissibility constraint:** Scope of authority.
* **Collapse boundary:** Small decisions produce large harm.
* **Invariant extracted:** Authority laundering.
* **CBI reading:** Continuation crossed a boundary without permission.

---

## B.3 AI Systems & Agentic Control

### Tool Use & Action

* **Continuation stream:** Plans leading to real-world actions.
* **Admissibility constraint:** Evidence, consent, and risk thresholds.
* **Collapse boundary:** Action taken on tentative interpretation.
* **Invariant extracted:** Irreversibility demands gating.
* **CBI reading:** Acting is not reasoning; it requires higher warrant.

---

### Memory & Learning

* **Continuation stream:** Persistent memory updates.
* **Admissibility constraint:** Reliability and relevance.
* **Collapse boundary:** False beliefs ossify.
* **Invariant extracted:** Memory must be permissioned.
* **CBI reading:** Learning is a controlled continuation, not accumulation.

---

## B.4 Safety, Operations, and Infrastructure

### "Stop-the-Line" Systems

* **Continuation stream:** Production or deployment.
* **Admissibility constraint:** Safety validation.
* **Collapse boundary:** Anomaly triggers halt.
* **Invariant extracted:** Human and system safety.
* **CBI reading:** Stopping is a first-class operation.

---

### Incident Response

* **Continuation stream:** Automated systems running.
* **Admissibility constraint:** Trust in current state.
* **Collapse boundary:** Uncertainty forces suspension.
* **Invariant extracted:** Damage containment.
* **CBI reading:** Refusal preserves order.

---

### Closing (Appendix B)

Outside mathematics, failure to restrict continuation produces not just incorrect conclusions, but irreversible harm. Constraint-bound inference thus generalizes from a method of proof to a method of governance, system design, and control.

---

## Appendix C - Prospective High-Impact Domains for Epistemic Continuation Auditing (ECA)

This appendix outlines domains in which failures are routinely traceable to **unauthorized continuation** - situations where processes proceed without renewed warrant. The entries below are **prospective and diagnostic**, identifying where ECA would surface stop-rules, warrant thresholds, and invariants, rather than proposing implementations.

---

### C.1 Cybersecurity

* **Continuation stream:** Authentication, authorization, execution, lateral movement.
* **Free continuation today:** Credentials, sessions, and trust relationships persist after conditions change.
* **Failure mode:** Silent escalation, persistence, and blast-radius expansion following partial compromise.
* **ECA contribution:** Make *trust decay* explicit; require periodic re-warranting of execution and privilege. Treat continued access as a revocable right, not a default.

---

### C.2 Critical Infrastructure

* **Continuation stream:** Automated control loops (power, water, transport, industrial systems).
* **Free continuation today:** Automation proceeds despite degraded sensors, stale models, or partial outages.
* **Failure mode:** Cascading failures, unsafe physical states, delayed human intervention.
* **ECA contribution:** Identify warrant-expiry points where automation must halt, downgrade, or hand off. Extract invariants tied to safe operating envelopes and refuse continuation outside them.

---

### C.3 Autonomous Vehicles

* **Continuation stream:** Perception -> planning -> actuation.
* **Free continuation today:** Local confidence propagates into irreversible motion under uncertainty.
* **Failure mode:** Edge-case collisions and brittle behavior when context shifts.
* **ECA contribution:** Enforce explicit justification thresholds for motion; elevate refusal and safe handoff as first-class outcomes when warrants weaken or conflict.

---

### C.4 Military & Security Systems

* **Continuation stream:** Intelligence assessment -> decision -> engagement.
* **Free continuation today:** Tentative interpretations harden into binding orders across organizational layers.
* **Failure mode:** Authority laundering, premature escalation, irreversible harm.
* **ECA contribution:** Make escalation boundaries explicit; require typed warrants for cross-domain binding. Treat continuation across authority levels as conditional and auditable.

---

### C.5 Large-Scale Software Operations

* **Continuation stream:** Build -> deploy -> operate -> update.
* **Free continuation today:** Pipelines auto-advance despite ambiguous signals or partial test coverage.
* **Failure mode:** Production incidents and rapid propagation of faults.
* **ECA contribution:** Insert stop-rules keyed to warrant sufficiency (evidence freshness, reversibility, blast radius). Preserve invariants around safety and rollback.

---

### C.6 Institutional Governance

* **Continuation stream:** Policies, mandates, and procedures persisting over time.
* **Free continuation today:** Decisions remain binding after their evidentiary basis expires.
* **Failure mode:** Policy drift, misalignment with current conditions, loss of legitimacy.
* **ECA contribution:** Establish warrant lifetimes and reauthorization gates; surface invariants tied to consent, scope, and accountability.

---

**Summary:**
Across these domains, harm correlates with continuation that outlives its warrant. ECA provides a diagnostic lens to identify where continuation should be conditional, where collapse is informative, and which invariants must govern refusal, escalation, or handoff.

---

## Editorial Provenance and Standing

### Acknowledgment / Preface
I would like to thank David Michael Farris for his 2011 doctoral dissertation on Embedded Contact Homology, which served as the conceptual catalyst for this work. Encountering a modern mathematical construction in which admissible continuation is so tightly constrained (and in which a robust invariant emerges precisely from what is excluded) helped clarify and motivate the abstraction developed here.
The present framework does not derive from the technical content of that work, nor does it claim any continuity of results. Rather, Farris’ dissertation provided a concrete instance in which a recurring epistemic maneuver became visible: the production of knowledge by restricting continuation and extracting what survives. Any errors or overextensions in the abstraction that follows are entirely my own.

## Corpus-Wide Reference Positioning

This paper argues that chaotic systems fail to produce order not primarily because of incorrect local transitions, but because continuation persists beyond the domain where governing constraints meaningfully apply. Its nearest external comparison fields are formal, open sovereign, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. Source availability and reproducible builds improve inspectability but do not alone guarantee comprehensibility, practical exit, hardware control, or sustainable maintenance. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E2]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E3]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

**[E4]** Leslie Lamport. *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Addison-Wesley, 2002. https://lamport.azurewebsites.net/tla/book.html **Relationship:** Predecessor specification discipline for state machines, safety, liveness, and refinement.

**[E5]** Free Software Foundation. *The Free Software Definition*. https://www.gnu.org/philosophy/free-sw.html **Relationship:** Normative predecessor for user freedoms; the paper may add reconstruction, governance, or hardware-boundary obligations beyond license rights.

**[E6]** Open Source Initiative. *The Open Source Definition*. https://opensource.org/osd **Relationship:** Adjacent licensing baseline; source availability is not treated as sufficient for operational sovereignty.

**[E7]** Martin Kleppmann et al. "Local-First Software: You Own Your Data, in Spite of the Cloud." *Onward! 2019*, pp. 154-178. DOI: 10.1145/3359591.3359737. https://www.inkandswitch.com/local-first/ **Relationship:** Adjacent local-first design program relevant to user custody, offline operation, and collaboration.

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

**[A6]** Adam Ableman. *Sovereign Software*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-24C6159B98023A9C`;  
source SHA-256  
`6AAFE79E438B980B75D1910A897F7BA716A10CF1187B68CB1F71405F36725A18`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Jnana*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-ECEAB04A620F163D`;  
source SHA-256  
`76D921D2975BDCD25D6DFB506F5E85F7AFDBF4D2CCC65F8C45394121F9D90060`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.18175271](https://doi.org/10.5281/zenodo.18175271)
