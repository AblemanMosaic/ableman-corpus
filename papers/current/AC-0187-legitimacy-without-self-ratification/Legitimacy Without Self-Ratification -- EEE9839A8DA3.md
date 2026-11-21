# Legitimacy Without Self-Ratification

## Constitutional Computing and the Provenance of Authority in Reflexive Systems

### No state may crown itself.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

What makes a state transition legitimate when the system performing the transition can also modify the rules, evidence, memories, trust anchors, or verification procedures by which that transition will later be judged?

This paper argues that reflexive computational systems face a problem of legitimacy distinct from correctness, security, integrity, or epistemic warrant. A transition may produce a correct result and nevertheless be unauthorized. It may be well-supported by evidence while lacking authority. It may preserve data integrity while changing the conditions under which integrity itself is defined. The central failure mode is **self-ratification**: the subject whose standing is in question supplies the decisive warrant by which that standing is conferred.

We develop a substrate-independent account of this problem and a computational architecture for addressing it. For a protected reflexive transition, there must exist no supporting evidence set that is sufficient to confer decisive standing and lies entirely under the unilateral control of the subject whose standing is being adjudicated. We formalize this principle using antecedent authorization, threat-model-relative control, typed provenance, evidence ablation, standing ceilings, defeaters, constitutional epochs, non-retroactivity, governed amendment, congruence between declared and executable law, and replayable transition receipts. We show that anti-self-ratification is not sufficient in isolation: its guarantee is constitutionally closed only when the rules defining evidence, standing, amendment, and verification are themselves governed by antecedent law.

The argument is interdisciplinary but not reductionist. Epistemic warrant, due process, legal validity, political legitimacy, constitutionalism, integrity, authorization logic, reference monitors, proof-carrying code, supply-chain provenance, transparency logs, Byzantine consensus, corrigibility, and constitutional AI are not synonyms. Rather, they exhibit a recurrent formal concern: power must not become sufficient evidence of its own rightful exercise. Their relation resembles Aristotelian focal meaning, or *pros hen* predication: distinct concepts retain distinct objects and failure conditions while exhibiting consilience around a shared semantic center.

The source manuscript reports a reference implementation in which anti-self-ratification is an explicit, load-bearing invariant. Its reported release process distinguishes self-description from external ratification; its verifier boundary rejects self-certification as sufficient evidence of verifier trustworthiness; its executor is reported to prohibit promotion of solely executor-authored evidence to the highest standing class; and its history is reported to support defeasible standing without erasure. A naturally occurring defect is also reported to have exposed the importance of evidence beyond the system's own observation boundary. This candidate preserves those claims as author-reported implementation evidence. Replayability, independence, authority, and epistemic strength remain separate, and no report is upgraded without its exact artifact and custody chain.

The paper also treats failures of the constitutional cure. A governance mechanism can fail by admitting what should be forbidden, but also by obstructing what its own law purports to permit. We therefore introduce governed liveness and governance proportionality, together with a two-lane architecture in which low-standing exploration remains cheap while high-standing acceptance receives full certification.

The broader thesis is that legitimacy is not essentially political and constitutionalism is not merely metaphorical. Wherever a subject can change consequential state while also influencing the grounds on which that change is accepted, a legitimacy problem appears. Constitutional computing names an architectural response: power over state is subordinated to prior, inspectable, amendable, and independently checkable rules governing the provenance of authority.

The present candidate does not infer empirical results from the protocol. The source reports execution of its conformance and mutation suite and independent replay of principal courts, but this integration pass did not recover the exact archives, court packages, command transcripts, or independently retained outputs required to re-establish those claims. Appendix C therefore preserves the reports while withholding independent-verification standing. The distinction is the theory functioning correctly.

## Keywords

legitimacy; self-ratification; constitutional computing; reflexive systems; self-modification; provenance; authorization; due process; rule of law; integrity; warrant; reference monitor; software supply chain; AI governance; auditability; corrigibility; constitutional AI; Goodhart's law

## 1. Introduction

A system changes its state.

What makes the new state authoritative?

Computer science ordinarily decomposes this question into familiar properties. Was the operation authorized? Did it preserve an invariant? Was the artifact signed? Did the proof check? Was the update type-safe? Did the consensus protocol commit it? Did the transition improve expected utility? Can the resulting state be reproduced?

Each question matters. None necessarily answers the question posed here.

Consider a system that can modify not only ordinary application state but some part of the substrate from which future judgments are made: persistent memory, policy rules, trust anchors, evidence classifications, standing ceilings, verifier configuration, authorization graphs, model self-descriptions, release criteria, or the rules by which those components can themselves be changed.

Suppose the system performs such a modification and then reports:

> The modification is authoritative because the current system says that it is authoritative.

There is no necessary contradiction. The resulting state might be correct. It might be beneficial. It might even be exactly the state an external designer would have preferred.

The problem is that performance, endorsement, and ratification have collapsed into one act.

This paper calls that collapse **self-ratification**.

A primitive form is:

$$
\begin{aligned}
&A \text{ performs } \tau \\
&\land A \text{ declares } \tau \text{ authoritative} \\
&\Longrightarrow \tau \text{ is authoritative}
\end{aligned}.
$$

A sovereign architecture may deliberately define authority this way. The claim of this paper is narrower:

> A system that wishes to preserve a non-trivial distinction between authorized and merely successful self-modification cannot allow this implication to hold without further constraint.

The problem is old.

Epistemology distinguishes assertion from warrant. Legal procedure distinguishes a correct result from an outcome produced through a valid process. Constitutionalism distinguishes office from the present will of the officeholder. Political philosophy distinguishes effective power from legitimate authority. Security architecture distinguishes what a principal says from what the principal is authorized to establish. Proof-carrying code separates the producer of evidence from the policy under which that evidence is checked. Transparency systems distinguish the current operator's description of history from consistency proofs anchored in prior commitments. Software supply-chain frameworks distinguish an artifact from attestations about how it came into existence.

These are not instances of one predicate in disguise.

A warranted belief is not therefore politically legitimate. A legally valid rule may be morally atrocious. A valid signature can authenticate malicious software. A properly constituted court can make a factual mistake. A Byzantine consensus can agree on an unauthorized event.

The claim is instead one of **structural consilience**.

Across these domains, a recurring problem appears whenever the actor affecting an object can also influence the procedure by which the object's standing is later evaluated:

> What prevents the power whose standing is in question from becoming sufficient evidence of that standing?

That question is the semantic gravity well of this paper.

Its computational form becomes especially sharp in systems capable of reflexive state change. Once a system may alter the machinery that determines which future states count as authoritative, ordinary authorization no longer suffices unless authorization itself is governed across time.

The contributions are tenfold.

First, we distinguish **correctness**, **warrant**, **integrity**, and **legitimacy**.

Second, we formalize a threat-model-relative **anti-self-ratification invariant** using minimal decisive evidence sets. The definition yields an operational evidence-ablation test.

Third, we show that anti-self-ratification is circumventable if isolated. Its guarantee depends jointly on antecedence, non-retroactivity, governed amendment, provenance, and congruence. We call this **constitutional closure**.

Fourth, we propose a **constitutional computing architecture** built from a legitimacy kernel, explicit trust domains, standing ceilings, append-only evidence history, defeaters, constitutional epochs, governed amendments, transition receipts, and an explicit constitutional remainder.

Fifth, we distinguish legitimacy from liveness. A constitutional system can fail by admitting what should be forbidden, but also by obstructing what its own law purports to permit. We therefore introduce **governed liveness** and **governance proportionality**.

Sixth, we situate the architecture among neighboring traditions in jurisprudence, philosophy, security, formal methods, distributed systems, software provenance, institutional measurement, and AI. The genealogy includes not only rule-of-law and authorization traditions but the constitutional recursion exposed by Kelsen's basic norm, Ross's paradox of self-amendment, and Suber's analysis of legal change.

Seventh, we apply the theory reflexively to the paper's own case study. The evidentiary standing of a reviewer, an artifact, an author report, and a replayable observation are not silently merged. Where independent execution has not occurred, this paper does not manufacture results.

Eighth, we distinguish **method specification** from **method execution**. The draft defines a conformance and mutation suite, an evidence-ablation procedure, constitutional conjunct ablations, standing-calibration metrics, and a case-study threat model. A result receives only the standing supported by the exact artifacts available to the current review.

Ninth, we locate ASR within the wider Ableman corpus, especially the Governed Meaning Base, semantic legitimacy, reasoning receipts, work custody, the Three Hash Rule, admissibility engineering, and constitutional epistemology.

Tenth, we place the theory across Possibility, Specification, CM1, CM2, Instance Configuration, Implementation Realization, Evidence, and Revision so a conceptual invariant is not silently promoted into an implementation claim.

The thesis is:

> **Self-modifying systems face a problem of legitimacy distinct from correctness. A transition cannot acquire authoritative standing merely because the system capable of performing it also endorses it. Where the subject can modify the ground of its own future judgments, legitimacy requires a mechanically checkable provenance of authority and a prohibition on decisive self-ratification.**

There is an old visual shorthand for the problem. Self-coronation is possible. Napoleon could place a crown upon his own head. What the act cannot obtain merely by repeating itself is an independent source of authority for the crown.

The computational problem is the same in structure, if not in substance.

## 2. Scope: A Deliberately Limited Legitimacy

"Legitimacy" is overloaded.

In political philosophy it may concern a right to rule, justified coercion, democratic authorship, consent, public reason, justice, or the generation of political obligations. In jurisprudence it may implicate validity, legality, institutional authority, or fidelity to legal procedure. In sociology it may refer to beliefs that an order deserves obedience.

This paper does not reduce those debates to software.

It uses **procedural computational legitimacy** in a deliberately limited sense:

> A transition is computationally legitimate when it acquires authoritative standing through procedures valid under the antecedently governing rules of the system.

Let

$$ L_{\kappa}(\tau) $$

mean that transition $\tau$ is legitimate under constitution $\kappa$.

This property must be distinguished from several neighboring predicates.

### 2.1 Correctness

Let

$$ C(\tau) $$

mean that a transition produces a substantively correct result.

In general,

$$ C(\tau) \not\Rightarrow L_{\kappa}(\tau), $$

and

$$ L_{\kappa}(\tau) \not\Rightarrow C(\tau). $$

An unauthorized database modification may restore the true value.

A properly authorized adjudication may reach the wrong conclusion.

Correctness does not retroactively confer authority.

### 2.2 Warrant

Let

$$ W(p) $$

mean that proposition $p$ possesses sufficient epistemic warrant.

Then:

$$ W(\operatorname{beneficial}(\tau)) \not\Rightarrow L_{\kappa}(\tau). $$

Excellent evidence that a forbidden operation would improve the system does not imply that the actor possessing that evidence has authority to perform it.

Conversely, an authorized transition may later turn out to have rested on mistaken factual premises.

### 2.3 Integrity

Let

$$ I_{\kappa}(\sigma) $$

mean that state $\sigma$ satisfies an integrity policy defined under constitution $\kappa$.

Integrity is always relative to some criterion. Constitutional legitimacy governs, among other things, changes to the criteria under which integrity will subsequently be evaluated.

Thus:

$$ I_{\kappa_t}(\sigma_t) $$

does not answer whether:

$$ \kappa_t \rightarrow \kappa_{t+1} $$

was itself authorized.

### 2.4 Political and Moral Legitimacy

This paper seeks to establish properties of the form:

$$ L_{\kappa}(\tau). $$

It does not infer:

$$ M(\kappa), $$

where $M$ means that the constitution is morally justified.

A tyrannical constitution may possess impeccable procedural provenance.

The architecture developed here can make tyranny auditable. It cannot transform tyranny into justice.

This limitation places the proposal closer to a theory of legality and constituted authority than to a complete theory of political legitimacy. Raz's distinction between the existence and justification of authority, and broader debates over legitimate political coercion, remain relevant precisely because computational legitimacy captures only one layer of that terrain (Raz, 1979; Raz, 1986).

### 2.5 Standing

"Standing" is used in a generalized computational sense, not in the jurisdiction-specific sense of Article III standing.

A claim, artifact, attestation, actor, or transition has standing when the architecture permits it to exercise a specified normative or operational role.

Examples include:

* informational standing;
* advisory standing;
* presumptive standing;
* release-blocking standing;
* ratifying standing;
* amendment-authorizing standing.

Standing can therefore be graded or partially ordered rather than Boolean.

### 2.6 Legitimacy, Constituted Authority, and Legitimate Transition

The preceding restrictions can be summarized as a containment relation:

$$ \text{legitimacy} \supset \text{constituted authority} \supset \text{legitimate state transition}. $$

Legitimacy in the full political and moral sense is the outermost term and is not formalized here. Constituted authority concerns the provenance and alteration of authority within an established order. Legitimate state transition is the innermost object this paper formalizes: whether a particular change acquired standing under antecedent rules.

The characteristic reflexive failure mode of the innermost term is:

$$ \text{self-ratification}. $$

This hierarchy answers an objection that would otherwise be fatal. A reader may respond that the paper simply defines legitimacy as compliance with its own rules, which would be circular or trivial. The reply is that the paper does not claim to exhaust legitimacy. It formalizes one constitutive dimension of it: the valid provenance of authoritative transition. Whether the constituting rules deserve obedience remains outside the guaranteed property, as Section 2.4 states and Section 15.5 repeats.

The conclusion returns to this hierarchy under the phrase *constituted authority under reflexive control*, which names the formal object more precisely than legitimacy alone.

## 3. The Semantic Gravity Well

### 3.1 Consilience Without Univocity

The interdisciplinary claim can be made too strongly.

It would be false to say that epistemic warrant, due process, legal validity, constitutionalism, political legitimacy, authorization, provenance, and integrity are synonyms.

Let $P_d$ denote the predicate characteristic of domain $d$.

For example:

$$ P_{\text{epistemology}} = \operatorname{warrant}, $$

$$ P_{\text{law}} = \operatorname{legal\ validity\ or\ due\ process}, $$

$$ P_{\text{politics}} = \operatorname{legitimate\ authority}, $$

$$ P_{\text{security}} = \operatorname{authorized\ access\ or\ transition}, $$

$$ P_{\text{provenance}} = \operatorname{attested\ derivation}. $$

The claim is not:

$$ P_{d_1} = P_{d_2}. $$

The proposal is instead that several such predicates exhibit a focal relation to a common structural concern:

$$ F = \text{standing is not conferred merely by the power whose standing is at issue}. $$

Aristotle's discussion of *pros hen* predication supplies an illuminating semantic model. Terms can apply differently to different objects while remaining ordered toward one focal sense. "Healthy" can characterize a body, a diet, and a complexion without meaning exactly the same thing in every case (Aristotle, Metaphysics IV.2).

The relation proposed here is analogous.

The disciplines have not unknowingly partitioned one concept.

They have repeatedly encountered related normative structures around a common problem of authority, warrant, and reflexive control.

The paper uses **semantic gravity well** for this relation: concepts remain distinct while repeatedly bending toward the same structural difficulty.

### 3.2 Epistemology: Assertion Is Not Warrant

Dewey's "warranted assertibility" is relevant because it distinguishes the fact that a proposition is asserted from the standing it acquires through inquiry (Dewey, 1938; Dewey, 1941).

Computationally:

$$ \operatorname{Assert}_A(p) \not\Rightarrow W(p). $$

A system may generate $p$, repeat $p$, store $p$, summarize $p$, and assign confidence to $p$ without thereby conferring whatever evidentiary status would justify consequential reliance.

This becomes especially important in persistent agent memory.

If:

$$
\begin{aligned}
&\operatorname{Inference}_t(p) \\
&\rightarrow \operatorname{Store}_t(p) \\
&\rightarrow \operatorname{Premise}_{t+1}(p)
\end{aligned}
$$

automatically upgrades $p$ from inference to fact, persistence becomes an unintended warrant-producing operation.

A warrant store instead preserves content and status separately.

### 3.3 Law: Outcome Is Not Procedure

Law formalizes a distinction between substantive outcome and procedurally authorized result.

A judgment may be factually correct and procedurally defective.

An official may pursue a desirable end using an authority the office does not possess.

The proposition:

$$ \operatorname{GoodOutcome}(\tau) $$

is therefore distinct from:

$$ \operatorname{LawfulProcedure}(\tau). $$

This distinction is central to computational legitimacy because outcome-based systems are particularly vulnerable to retrospective laundering:

> The transition worked; therefore the transition must have been allowed.

A constitutional architecture rejects that inference.

Empirical work on procedural justice adds a distinct, non-formal dimension: people often judge institutions partly through the fairness of procedures rather than only through distributive outcomes (Tyler, 2006). Computational legitimacy does not inherit that psychological claim, but the recurrence of procedure as an independent source of standing is part of the broader consilience.

### 3.4 Rule of Law: Office Is Not Present Will

The rule-of-law tradition treats the exercise of governing power as constrained by prior law rather than exhausted by the current will of whoever possesses power.

The medieval Bractonian formulation (Bracton) is often rendered:

*non sub homine sed sub Deo et lege*,

not under man but under God and law.

The computational translation is intentionally secular and architectural:

$$ \operatorname{Actor} \prec \operatorname{GoverningRule}(\operatorname{Actor}). $$

A privileged process may possess the physical ability to bypass a constraint.

That makes it powerful.

It does not make the bypass constitutional.

Waldron's survey of the rule-of-law tradition emphasizes recurring concerns with generality, prospectivity, publicity, stability, and institutionalized procedures rather than mere rule by present command (Waldron, 2023).

### 3.5 Fuller: Legality as Conformance Structure

Fuller's eight principles of legality include generality, publicity, prospectivity, intelligibility, consistency, possibility of compliance, relative stability, and congruence between announced rule and official action (Fuller, 1964/1969).

Several translate unusually well into computational gates.

Prospectivity becomes:

$$ \kappa_{t+1} \not\Rightarrow \operatorname{RetroactiveAuthorization}(\tau_t). $$

Congruence becomes:

$$ \operatorname{Spec}(\kappa) \approx \operatorname{Impl}(V_{\kappa}). $$

Publicity becomes inspectability of governing rules.

Stability becomes constitutional epochs and pinned frames.

Possibility of compliance becomes an architectural liveness requirement: there must actually exist a feasible lawful path for actions that the constitution purports to authorize.

This last point becomes important when considering failures of the cure.

### 3.6 Kant: A Tribunal Within Reason

Kant's *Critique of Pure Reason* famously invokes a tribunal in which reason submits its own claims to lawful examination rather than accepting them by decree (Kant, 1781/1787).

The analogy should not be romanticized. Kant did not anticipate kernel architecture.

The structural point is narrower: reflexive evaluation requires an internal distinction between producing a claim and admitting that claim.

A component is not independent merely because it is named "judge", "critic", "reviewer", or "verifier".

Independence is a control relation.

### 3.7 Wittgenstein: When Seeming Right Becomes Right

Wittgenstein's discussion in *Philosophical Investigations* section 258 contains a compact reductio of private ratification. If whatever seems right to the subject thereby counts as right, the distinction between seeming right and being right collapses (Wittgenstein, 1953).

The computational analogue is:

$$ \operatorname{Endorses}_S(\tau) \Rightarrow L(\tau). $$

If $S$ controls the endorsement predicate, then for self-transitions the distinction between authorized and unauthorized change becomes vacuous.

### 3.8 Political Legitimacy: Power Is Not Authority

Let:

$$ \operatorname{Power}_A(\tau) $$

mean that actor $A$ can cause transition $\tau$.

Let:

$$ \operatorname{Authority}_A(\tau) $$

mean that $A$ possesses recognized authority to perform it.

Then:

$$ \operatorname{Power}_A(\tau) \not\Rightarrow \operatorname{Authority}_A(\tau). $$

This distinction also separates normative and sociological concepts of legitimacy. Weber's sociology of legitimate domination concerns orders experienced and treated as legitimate by participants, whereas the present paper asks whether a transition satisfies a specified normative-computational procedure (Weber, 1978). The two questions can diverge: a computational order may be procedurally valid but widely rejected, or widely accepted while violating its own antecedent rules.

The entire project of constitutional computing exists in the gap between effective control and constituted authority.

## 4. Formal Model

### 4.1 State

Let a reflexive system at time $t$ have state:

$$ \sigma_t = (D_t, K_t, W_t, E_t, A_t, R_t, H_t), $$

where:

* $D_t$ is ordinary domain state;
* $K_t$ is constitutional state;
* $W_t$ is the warrant store;
* $E_t$ is admitted evidence and defeaters;
* $A_t$ is authorization and capability state;
* $R_t$ contains release and ratification records;
* $H_t$ is append-only transition history.

Let:

$$ G_t \subseteq \sigma_t $$

denote the **governance substrate**: state that influences whether future actions or claims receive authority.

Examples include:

* policy definitions;
* public keys and trust roots;
* evidence schemas;
* verifier code;
* standing ceilings;
* amendment rules;
* memory classes used as authoritative premises.

### 4.2 Reflexive Transitions

A transition $\tau$ is reflexive when it changes governance state or changes state whose authority is subsequently evaluated through governance state it can influence:

$$
\begin{aligned}
&\operatorname{Reflexive}(\tau) \\
&\iff \Delta(\tau) \cap G_t \\
&\neq \varnothing \\
&\lor \operatorname{AffectsStandingSemantics}(\tau)
\end{aligned}.
$$

Reflexivity is therefore semantic, not merely self-modification at the byte level.

A model changing an ordinary cache entry may be non-reflexive.

A model changing one sentence in a policy file may be deeply reflexive.

### 4.3 Transition Proposal

Represent a proposed transition as:

$$ \tau = (a, \sigma_t, \sigma_{t+1}, op, E^+_{\tau}, E^-_{\tau}, \eta, q), $$

where:

* $a$ is the actor;
* $op$ is the proposed operation;
* $E^+_{\tau}$ is supporting evidence;
* $E^-_{\tau}$ is admitted defeating evidence;
* $\eta$ is the governing constitutional epoch;
* $q$ is requested standing.

Proposal is not admission:

$$ \operatorname{Propose}(\tau) \not\Rightarrow \operatorname{Admit}(\tau). $$

### 4.4 Legitimacy Predicate

Define:

$$
\begin{aligned}
&L_{\kappa_{\eta}}(\tau) = \operatorname{Auth}(\tau) \\
&\land \operatorname{Proc}(\tau) \\
&\land \operatorname{Prov}(\tau) \\
&\land \operatorname{Epoch}(\tau) \\
&\land \operatorname{Congr}(\tau) \\
&\land \operatorname{Replay}(\tau) \\
&\land \operatorname{ASR}(\tau)
\end{aligned},
$$

where:

* $\operatorname{Auth}$ verifies antecedent authority;
* $\operatorname{Proc}$ verifies required procedure;
* $\operatorname{Prov}$ verifies provenance;
* $\operatorname{Epoch}$ verifies that the proper historical law governs;
* $\operatorname{Congr}$ verifies declared/executable law congruence;
* $\operatorname{Replay}$ verifies reproducibility of adjudication;
* $\operatorname{ASR}$ verifies anti-self-ratification where required.

This decomposition is not asserted to be uniquely correct.

Its purpose is to expose distinct exploit classes that disappear when authorization is represented as a single Boolean.

### 4.5 Threat-Model-Relative Control

Let:

$$ \operatorname{Control}_{\Theta}(a, x) $$

mean that actor $a$ can, under threat model $\Theta$, unilaterally create, alter, suppress, substitute, or determine the relevant value of object $x$.

The threat model matters.

A second process does not constitute an independent domain if the first process controls its binary, configuration, input, output selection, or signing key.

A second AI model call is not necessarily independent if the first system controls:

* its prompt;
* its retrieved context;
* its tool inputs;
* the selection of which outputs are retained;
* the memory in which the output is stored.

"External" is therefore an operational control relation, not a spatial metaphor.

### 4.6 Evidence as a Typed Object

Let an evidence item be:

$$ e = (content, issuer, subject, method, time, domain, digest). $$

Represent its evaluative properties separately:

$$
\begin{aligned}
\operatorname{Eval}(e) = (&\operatorname{Strength}(e), \\
&\operatorname{Independence}_{\Theta}(e), \\
&\operatorname{Authority}(e), \\
&\operatorname{Replayability}(e))
\end{aligned}.
$$

These dimensions must not be collapsed.

For example:

$$ \operatorname{Replayable}(e) \not\Rightarrow \operatorname{Independent}_{\Theta}(e). $$

A deterministic review generated under a subject-controlled input frame may be perfectly replayable but only partially independent.

Likewise:

$$ \operatorname{Independent}_{\Theta}(e) \not\Rightarrow \operatorname{True}(content(e)). $$

External evidence can be wrong.

### 4.7 Standing

Let standing classes form a partially ordered set:

$$ (\mathcal{L}, \preceq). $$

A simple implementation might use:

$$ L_0 \prec L_1 \prec \cdots \prec L_n. $$

A richer architecture may contain incomparable classes. For example:

$$ L_{\text{epistemic}} \not\preceq L_{\text{ratifying}}, $$

and:

$$ L_{\text{ratifying}} \not\preceq L_{\text{epistemic}}. $$

The architecture should resist compressing all trust into one scalar.

### 4.8 Standing Ceilings

For evidence source or trust domain $d$ and claim class $c$, define:

$$ \operatorname{ceil}(d, c) \in \mathcal{L}. $$

Then:

$$ \operatorname{StandingFrom}(d, c) \preceq \operatorname{ceil}(d, c). $$

Self-authored evidence may be admissible while being unable to finalize its own highest standing:

$$ \operatorname{ceil}(\operatorname{subject}(c), c) \prec L_{\text{ratified}}. $$

The principle is not:

> never trust self-report.

It is:

> self-report must not silently occupy every evidentiary role.

### 4.9 Fixed Adjudicative Context

The idea of a "decisive evidence set" becomes operational only if the surrounding adjudicative context is fixed.

Let:

$$ C_{\tau} = (\sigma_t, \kappa_{\eta}, V_{\eta}, E^-_{\tau}, q), $$

where $V_{\eta}$ is the verifier active under constitutional epoch $\eta$.

For supporting evidence subset:

$$ E' \subseteq E^+_{\tau}, $$

define:

$$ \operatorname{Sufficient}_{C_{\tau}}(E') \iff \operatorname{Standing}(V_{\eta}(C_{\tau}, E')) \succeq q. $$

This definition holds admitted defeaters fixed.

That restriction matters because the standing model is defeasible and therefore non-monotonic. Naively removing arbitrary evidence could increase standing if what was removed was a defeater.

An evidence object may, in a richer system, play different logical roles with respect to different claims. For example, $e$ may support claim $c_1$ while defeating $c_2$. The $E^+ / E^-$ partition should therefore be understood relative to the adjudicated claim and transition, not as an intrinsic global type of the evidence object.

### 4.10 Minimal Decisive Support

Define a **minimal decisive support set**:

$$
\begin{aligned}
&\operatorname{Decisive}_{C_{\tau}}(E') \\
&\iff \operatorname{Sufficient}_{C_{\tau}}(E') \\
&\land \forall E'' \subsetneq E', \\
&\ne g \operatorname{Sufficient}_{C_{\tau}}(E'')
\end{aligned}.
$$

This definition gives the central concept an operational interpretation.

A set is decisive not because a policy document labels it decisive, but because:

1. the transition is admitted with it; and
2. ablating any further supporting element causes admission at the requested level to fail.

Evidence ablation therefore becomes a direct empirical test of constitutional structure.

### 4.11 Anti-Self-Ratification

Write:

$$ \operatorname{ControlledBy}(E', a) \iff \forall e \in E', \; \operatorname{Control}_{\Theta}(a, e). $$

For protected reflexive transition $\tau$, the invariant is:

$$ \boxed{ \; \operatorname{ASR}(\tau) \iff \nexists E' \subseteq E^+_{\tau} : \operatorname{Sufficient}_{C_{\tau}}(E') \land \operatorname{ControlledBy}(E', \operatorname{subject}(\tau)) \; } $$

In words:

> There exists no entirely self-controlled route to the requested standing.

This is the central invariant of the paper. It is stated first in this form because the philosophical content is transparent here: the prohibition is on the *existence of a subject-only path*, not on any particular evidentiary bookkeeping.

Minimality plays no part in the semantics. It enters only as an enumeration strategy, because searching all sufficient subsets is wasteful when the minimal ones already witness everything relevant.

**Proposition 2 (Equivalent ASR characterizations).** For finite $E^+_{\tau}$ under a fixed adjudicative context $C_{\tau}$, the following are equivalent:

1. every minimal decisive support set contains at least one element outside the subject's unilateral control;
2. no sufficient support set consists entirely of subject-controlled evidence.

**Proof.**

$(2) \Rightarrow (1)$. Suppose some minimal decisive support set $E'$ were entirely subject-controlled. By definition $E'$ is sufficient, so $E'$ is itself a subject-only sufficient set, contradicting (2).

$(1) \Rightarrow (2)$. Suppose some subject-only sufficient set $E'$ exists. Remove elements from $E'$ while sufficiency is preserved. Since $E'$ is finite, the process terminates in a subset $E'' \subseteq E'$ that is sufficient and has no sufficient proper subset, hence is minimal decisive. Every element of $E''$ lies in $E'$ and is therefore subject-controlled, contradicting (1). $\Box$

Two conditions of the proposition are load-bearing and should not be dropped.

Finiteness supports the descent argument. For infinite evidence sets the descent need not terminate, and the equivalence requires a well-foundedness assumption in its place.

The fixed adjudicative context of Section 4.9 is what makes $\operatorname{Sufficient}_{C_{\tau}}$ a stable predicate over subsets of $E^+_{\tau}$ at all. If admitted defeaters were permitted to vary as supporting evidence is removed, ablation would not be a well-defined operation on the support set, and the descent would not be meaningful. The proposition therefore depends on the defeater-pinning restriction introduced there, not merely on finiteness.

The practical consequence is a clean separation between meaning and method:

$$ \operatorname{SemanticDefinition} = \text{no subject-only sufficient set}, $$

$$ \operatorname{EnumerationStrategy} = \text{inspect minimal decisive support sets}. $$

An independent attestation merely being present is not enough.

If it can be removed and the transition still receives final standing, then it was ceremonial rather than load-bearing.

### 4.12 Corollary 1 and Lemma 1: Absence of Independent Evidentiary Constraint

The semantic definition of Section 4.11 yields its operative consequence directly.

**Corollary 1 (Independent evidence is not necessary).** If there exists a subject-controlled sufficient support set for requested standing $q$, then independent evidence is not necessary for obtaining $q$.

**Proof.** Let $E'$ satisfy $\operatorname{Sufficient}_{C_{\tau}}(E')$ and $\operatorname{ControlledBy}(E', \operatorname{subject}(\tau))$. Then $q$ is obtainable from $E'$ alone, and $E'$ contains no element outside the subject's unilateral control. Hence no independent element is necessary for $q$. $\Box$

This is exactly what the anti-self-ratification invariant forbids, and it is the form in which the prohibition should ordinarily be applied: a single subject-only route suffices to defeat the guarantee.

A stronger secondary result is available and is retained here because an earlier formulation of this paper made it primary.

**Lemma 1 (No independent evidentiary constraint).** If *every* minimal decisive support set for a subject's protected claim consists entirely of evidence under that subject's unilateral control, then the adjudication contains no independent evidentiary constraint on the requested standing of that claim.

**Proof.**

Let:

$$ \mathcal{D}_{\tau} = \left\{ E' : \operatorname{Decisive}_{C_{\tau}}(E') \right\}. $$

Assume:

$$ \forall E' \in \mathcal{D}_{\tau}, \; \forall e \in E', \; \operatorname{Control}_{\Theta}(\operatorname{subject}(\tau), e). $$

By definition, every $E' \in \mathcal{D}_{\tau}$ is sufficient to obtain the requested standing, and every evidence element within every such minimal basis lies under the subject's unilateral control.

Therefore no independent evidence element is necessary to obtain the requested standing.

Hence the evidence layer contributes no independent evidentiary constraint on that standing. $\Box$

The relation between the two results should be stated precisely, because it is easy to mistake them for the same claim.

Lemma 1's antecedent is strictly stronger than the negation of $\operatorname{ASR}$. By Proposition 2, $\neg \operatorname{ASR}(\tau)$ is equivalent to the existence of *some* subject-only sufficient set, and hence to the existence of *some* entirely subject-controlled minimal decisive set. Lemma 1 instead requires that *all* minimal decisive sets be subject-controlled. Corollary 1 is therefore the result that matches the invariant; Lemma 1 describes the degenerate case in which the evidence layer imposes no independent constraint at all.

Neither result implies that the entire adjudication is under subject control. A protected verifier, constitutional rule, or hardware root may independently constrain the verdict.

Both claims are specifically evidentiary.

### 4.13 Sybil-Resistant Threshold Independence

A naive threshold rule is insufficient.

The quorum threshold is written $k$ throughout this section. It must not be confused with the requested standing $q$ of the transition tuple in Section 4.3, which is a different quantity and is load-bearing in the sufficiency definition of Section 4.9.

Suppose:

$$ \left| \left\{ \operatorname{domain}(e) : e \in E' \right\} \right| \ge k. $$

If the subject can create $k$ nominal domains, the threshold is satisfied by a Sybil attack.

Instead define a threat-model-relative independent-domain rank:

$$ \operatorname{rank}_{\Theta}(E') = \max |D| $$

subject to:

1. each $d \in D$ contributes at least one element of $E'$;
2. the domains in $D$ satisfy the required independence relation under $\Theta$;
3. at least one required domain is outside the unilateral control of the subject.

Then:

$$ \operatorname{ASR}_k(\tau) \iff \forall E' \in \mathcal{D}_{\tau}, \; \operatorname{rank}_{\Theta}(E') \ge k $$

and:

$$ \forall E' \in \mathcal{D}_{\tau}, \; \exists e \in E' : \neg \operatorname{Control}_{\Theta}(\operatorname{subject}(\tau), e). $$

Nominal plurality is not independence.

### 4.14 Antecedent Authorization

Authority must exist before the transition whose legitimacy it establishes.

Let:

$$ \operatorname{Auth}_{\kappa_{\eta}}(a, op, \sigma_t) $$

mean that actor $a$ is authorized under the current constitution to attempt $op$ from state $\sigma_t$.

Then:

$$ \operatorname{Auth}(\tau) = \operatorname{Auth}_{\kappa_{\eta}}(a, op, \sigma_t). $$

Temporal precedence requires:

$$ t(\operatorname{Auth}(\tau)) < t(\operatorname{commit}(\tau)). $$

For protected transitions:

$$
\begin{aligned}
& \\
&\ne g \operatorname{Auth}_{\kappa_{\eta}}(a, op, \sigma_t) \\
&\Rightarrow  \\
&\ne g L_{\kappa_{\eta}}(\tau)
\end{aligned},
$$

even if the resulting state grants the authority afterward:

$$ \operatorname{Auth}_{\kappa_{\eta+1}}(a, op, \sigma_{t+1}) = 1. $$

A transition cannot manufacture its own antecedent authority.

### 4.15 Non-Retroactivity

Let $\eta(\tau)$ denote the constitutional epoch governing transition $\tau$.

Then:

$$ \operatorname{Eval}(\tau) = \kappa_{\eta(\tau)}. $$

If:

$$ \kappa_{\eta+1} \models \operatorname{Permitted}(op), $$

that does not imply:

$$ L_{\kappa_{\eta}}(\tau). $$

A constitution may explicitly authorize a retrospective mechanism.

But retrospective authorization itself must derive from a rule that possessed antecedent authority.

Otherwise every violation can be repaired by editing the law after success.

### 4.16 Governed Amendment

Let:

$$ \operatorname{Amend}(\kappa_{\eta}, \Delta\kappa) $$

be a privileged transition class.

Then:

$$ \kappa_{\eta+1} = \kappa_{\eta} \oplus \Delta\kappa $$

only if:

$$ L_{\kappa_{\eta}}(\tau_{\text{amend}}) = 1. $$

The proposed new constitution does not judge the procedure by which it comes into force.

The current one does.

This creates the recursion that Ross and Suber analyze in legal self-amendment and that constitutional computing must address directly.

### 4.17 Defeaters and Revisable Standing

Evidence history should generally be append-only:

$$ H_t \subseteq H_{t+1}. $$

Standing need not be monotonic.

Let:

$$ w_c = (c, E^+_c, E^-_c, \ell_c, \eta_c, \pi_c) $$

be a warrant record for claim $c$.

After admission of defeater $d$:

$$ H_{t+1} = H_t \cup \left\{ d, \rho_{\text{revision}} \right\}. $$

But:

$$ \operatorname{Standing}_{t+1}(c) \prec \operatorname{Standing}_t(c) $$

may hold.

Thus:

$$ H_t \subset H_{t+1} \not\Rightarrow \operatorname{Standing}_{t+1}(c) \succeq \operatorname{Standing}_t(c). $$

Correction therefore need not require historical erasure.

### 4.18 Congruence

A written constitution is not sufficient if the executable verifier implements different rules.

Let:

$$ \operatorname{Spec}(\kappa) $$

denote declared semantics and:

$$ \operatorname{Impl}(V_{\kappa}) $$

denote realized verifier behavior.

The ideal is:

$$ \operatorname{Spec}(\kappa) \equiv \operatorname{Impl}(V_{\kappa}). $$

Exact equivalence may be unavailable.

A practical architecture therefore maintains a conformance corpus $T_{\kappa}$:

$$ \forall x \in T_{\kappa}, \; \operatorname{Spec}(\kappa, x) = \operatorname{Impl}(V_{\kappa}, x). $$

The corpus must include adversarial cases.

Otherwise a constitution may be perfectly documented and operationally fictitious.

### 4.19 Replayability

For protected transition $\tau$, define a receipt:

$$
\begin{aligned}
\rho_{\tau} = (&h(\sigma_t), h(\kappa_{\eta}), h(E^+_{\tau}), \\
&h(E^-_{\tau}), decision, h(\sigma_{t+1}), v, t)
\end{aligned},
$$

where $h$ is a cryptographic digest and $v$ identifies verifier semantics.

Replayability requires:

$$ V_{\kappa_{\eta}}(\tau, E^+_{\tau}, E^-_{\tau}) = decision $$

under the pinned inputs.

Replayability is valuable because it localizes disagreement.

It does not prove independence.

It does not prove truth.

It does not prove that the verifier itself deserves trust.

### 4.20 Constitutional Closure

ASR is not sufficient by itself.

Suppose a subject cannot self-ratify evidence but can change the rule defining which evidence is decisive.

It may then perform:

$$ \operatorname{Amend}(\operatorname{Decisive}) $$

followed by:

$$ \operatorname{SelfEvidence} \Rightarrow L_{\text{final}}. $$

The formal ASR check can then pass under a corrupted rule.

The anti-self-ratification guarantee is therefore constitutionally meaningful only when embedded in a closure condition.

Define:

$$
\begin{aligned}
&\operatorname{ASRClosure}(\tau) = \operatorname{ASR}(\tau) \\
&\land \operatorname{Antecedence}(\tau) \\
&\land \operatorname{NonRetroactivity}(\tau) \\
&\land \operatorname{GovernedAmendment}(\tau) \\
&\land \operatorname{Congruence}(\tau) \\
&\land \operatorname{Prov}(\tau)
\end{aligned}.
$$

The name is chosen deliberately.

> $\operatorname{ASRClosure}$ is not a second legitimacy predicate and not a strengthened variant of $\operatorname{ASR}$. It names the subset of legitimacy conditions required to prevent the ASR criterion itself from being rewritten, laundered, or spoofed. It is closure of the invariant under changes to its own evaluation machinery.

An earlier formulation of this paper called the conjunction `ClosedASR`, which invited the reading that it was a stronger form of anti-self-ratification rather than a condition on the durability of the same criterion. The renaming is a correction of that ambiguity, not a change of content.

The conjuncts of the full legitimacy predicate block distinct exploit classes.

| Removed property | Resulting exploit |
| --- | --- |
| ASR | Self-controlled evidence can directly confer final standing |
| Antecedence | Actor can grant itself authority during or after the act |
| Non-retroactivity | Later law can launder earlier violations |
| Governed amendment | Subject can rewrite the ratification rule at will |
| Congruence | Declared law and executable law can diverge |
| Provenance | Controlled evidence can masquerade as independent evidence |
| Replayability | Later narratives can substitute for reproducible adjudication |

Two scope notes on this table. First, it covers the conjuncts of the full legitimacy predicate $L$ of Section 4.4, which is broader than $\operatorname{ASRClosure}$: replayability appears in $L$ but is not required for closure of the anti-self-ratification guarantee itself. Second, the naming in Section 4.4 and this section is deliberately near-synonymous across three pairs. $\operatorname{Auth}$ in Section 4.4 is the predicate whose temporal condition Section 4.14 calls antecedence. $\operatorname{Epoch}$ in Section 4.4 is the predicate whose rule Section 4.15 calls non-retroactivity. And governed amendment is the specialization of $\operatorname{Proc}$ that applies to constitutional-amendment transitions: $\operatorname{Proc}$ requires that a transition follow the procedure its class demands, and for the amendment class that procedure is the amendment rule in force under the governing epoch. The tables list governed amendment rather than $\operatorname{Proc}$ because amendment is the procedure class through which reflexive circumvention actually runs; Section 11.7 ablates $\operatorname{Proc}$ separately so that the general predicate is not left untested. Section 11.7 ablates the components of $L$ together with epoch binding and history persistence; Appendix B.13 ablates the six conjuncts of $\operatorname{ASRClosure}$. The two experiments are therefore nested rather than inconsistent.

Constitutional computing is therefore not one prohibition.

It is a mutually supporting structure.

## 5. Genesis, Recognition, Revolution, and the Constitutional Remainder

### 5.1 The Regress Cannot Be Deleted

Every chain of authorization eventually reaches a boundary.

If rule $r_1$ is valid because of $r_2$, and $r_2$ because of $r_3$, either the chain continues indefinitely, becomes circular, or terminates in assumptions that are not themselves authorized by another rule of the same system.

Computational systems usually hide this fact beneath words such as:

* root;
* genesis;
* factory key;
* trust anchor;
* bootstrap;
* immutable configuration;
* initial policy.

Constitutional computing makes the remainder explicit.

Let the initial constitution be:

$$ \kappa_0. $$

Let:

$$ R_0 $$

denote the set of ultimate trust assumptions not established by the governed system itself.

Then:

$$ R_0 \neq \varnothing. $$

The goal is not to eliminate $R_0$ by assertion.

The goal is to minimize, expose, pin, and externally anchor it.

### 5.2 Hart and the Rule of Recognition

Hart's rule of recognition provides one jurisprudential response to the regress of legal validity. On Hart's account, the ultimate rule by which officials identify valid law is not itself valid because of another higher legal rule. It exists as a social rule manifested in convergent official practice (Hart, 1961/2012).

A computational trust root is not Hart's rule of recognition.

The contrast is useful because it reveals different termination mechanisms.

A legal order may terminate the regress in:

$$ \operatorname{SocialPracticeOfRecognition}. $$

A computational order may terminate operationally in:

$$ \operatorname{PinnedGenesis} + \operatorname{ExternalAnchor} + \operatorname{ReplayableDerivation}. $$

Neither mechanism proves the moral worthiness of the order.

Both expose the point at which validity ceases to be derivable from another rule of the same kind.

### 5.3 Kelsen and the Basic Norm

Kelsen's *Grundnorm*, or basic norm, offers a different jurisprudential analogue.

For Kelsen, ordinary legal validity is understood through a hierarchy of authorizing norms. At some point the chain reaches the historically first constitution, whose legal validity cannot itself derive from another positive norm in the same order. The basic norm is presupposed as the normative condition under which the constitution and norms derived from it can be understood as legally valid (Kelsen, 1945; Kelsen, 1967).

The analogy to computational roots is illuminating but incomplete.

A cryptographic genesis event is an event.

Kelsen's basic norm is not merely a signed genesis file.

The structural similarity is that both expose the impossibility of deriving every authority relation from a prior positive authority relation internal to the same order.

### 5.4 Efficacy and Revolutionary Discontinuity

Kelsen also creates an important boundary condition for the principle of antecedence.

Within an existing constitutional order:

$$ \operatorname{AntecedentAuthority} $$

can govern whether a transition is valid under that order.

But successful revolutionary displacement poses a different question: whether the old order remains the operative legal order at all.

Kelsen's theory associates the validity of an order as a whole with its general efficacy and allows successful revolution to correspond to a change in the presupposed basic norm.

The computational analogue is not:

$$ \operatorname{SuccessfulAttack} \Rightarrow \operatorname{LegitimateTransition}. $$

It is:

> Antecedence is an intra-era principle. A sufficiently complete replacement of the constitutional order creates an era-boundary problem that the former order cannot settle merely by applying one more ordinary transition rule.

Let:

$$ Era_i = (\kappa_i, R_i). $$

Within an era:

$$ \tau : Era_i \rightarrow Era_i $$

is evaluated under antecedent constitutional law.

An era-founding discontinuity:

$$ Era_i \rightsquigarrow Era_{i+1} $$

cannot simply be treated as an ordinary amendment if it did not satisfy the amendment law of $Era_i$.

Its operational recognition belongs to genesis and remainder semantics.

### 5.5 Dosso and Asma Jilani

The constitutional jurisprudence surrounding *State v. Dosso* (State v. Dosso, PLD 1958 SC 533) makes the danger concrete.

Pakistan's Supreme Court invoked a Kelsenian account of revolutionary legality in treating the effective destruction of a prior constitutional order as legally transformative. The decision was later overruled in *Asma Jilani v. Government of the Punjab* (Asma Jilani v. Government of the Punjab, PLD 1972 SC 139), which rejected the use of Kelsen's theory as a license for validating usurpation.

The lesson for this paper is not that Kelsen licenses coups.

The deeper lesson is architectural:

> A theory of intra-system validity cannot by itself settle the normative legitimacy of the event that replaces the system.

That event must be typed differently.

Constitutional computing therefore distinguishes:

$$ \operatorname{Amendment} $$

from:

$$ \operatorname{Refounding}. $$

The first is governed by the existing constitution.

The second exposes the constitutional remainder.

### 5.6 Genesis Anchoring

A computational genesis procedure can provide:

* exact bytes of the initial constitution;
* public hashes;
* identities or roles of initial signers;
* quorum requirements;
* timestamped ceremony records;
* reproducible derivation procedures;
* archived implementation artifacts.

Let genesis record:

$$
\begin{aligned}
g = (&h(\kappa_0), signers, threshold, procedure, time, \\
&artifacts)
\end{aligned}.
$$

The system can verify:

$$ \operatorname{Anchor}(g, \kappa_0) = 1. $$

What it cannot infer solely from that verification is:

$$ \operatorname{MoralLegitimacy}(\kappa_0). $$

The architecture terminates operational regress in explicit trust assumptions and replayable anchoring, not in a proof that the root deserves obedience.

## 6. Self-Amendment and Constitutional Recursion

### 6.1 Ross's Puzzle

Alf Ross's "On Self-Reference and a Puzzle in Constitutional Law" identifies a formal problem in constitutional self-amendment (Ross, 1969).

If amendment rule $A$ authorizes amendments, can $A$ authorize a change to $A$ itself?

The structure is reflexive:

$$ A \vdash A'. $$

But the rule used as authority for the transition is also the object transformed by the transition.

For computational systems, the problem is immediate.

If:

$$ \operatorname{VerifierRule}_t $$

authorizes alteration of:

$$ \operatorname{VerifierRule}_t, $$

the architecture must specify exactly which rule governs the act of alteration.

The answer cannot be:

$$ \operatorname{VerifierRule}_{t+1} $$

without retroactivity.

### 6.2 Suber's Paradox of Self-Amendment

Peter Suber's *The Paradox of Self-Amendment* develops Ross's problem at book length and distinguishes logical models of amendment from the actual legal practices through which constitutions change (Suber, 1990).

Suber emphasizes that constitutional rules of change are themselves often changed through procedures they authorize, directly or indirectly.

This is precisely the computational case.

The existence of recursion does not make amendment impossible.

It makes **epoch binding** necessary.

The computational rule is:

$$ \operatorname{Judge}(\tau_{\text{amend}}) = \kappa_{\eta}, $$

not:

$$ \operatorname{Judge}(\tau_{\text{amend}}) = \kappa_{\eta+1}. $$

The new law may govern future amendments.

It does not govern the act by which it came into existence.

### 6.3 Constitutional Recursion as an Asset

The recursion should not be hidden.

It is one of the strongest conceptual links between constitutional theory and self-modifying computation.

A system capable of governed self-modification must permit:

$$ \operatorname{Law} \rightarrow \operatorname{NewLaw} $$

without permitting:

$$ \operatorname{DesiredNewLaw} \rightarrow \operatorname{RetroactiveJustificationOfItsOwnBirth}. $$

Epoch semantics provides the distinction.

## 7. Constitutional Computing Architecture

### 7.1 From Reference Monitor to Legitimacy Kernel

The reference-monitor tradition supplies a natural architectural ancestor.

A reference monitor is classically required to be:

* always invoked;
* protected from tampering;
* sufficiently simple or structured to permit verification.

Its ordinary decision is roughly:

$$ \operatorname{MayAccess}(subject, object, operation)? $$

A **legitimacy kernel** generalizes the mediated object:

$$ \operatorname{MayTransition}(actor, prestate, poststate, authority, evidence, epoch, requestedStanding)? $$

The legitimacy kernel mediates protected state transitions, including changes to the governance machinery itself.

### 7.2 Required Kernel Properties

At minimum:

$$ \operatorname{CompleteMediation}, \quad \operatorname{TamperResistance}, \quad \operatorname{Inspectability}, $$

$$
\begin{aligned}
&\operatorname{EpochBinding}, \\
&\quad \operatorname{ProvenanceBinding}, \\
&\quad \operatorname{StandingEnforcement}, \\
&\quad \operatorname{Replayability}
\end{aligned}.
$$

The kernel does not need to adjudicate every transient computation.

It must mediate transitions that cross constitutionally protected boundaries.

### 7.3 Conversation Is Not Governance

Agentic AI systems expose the distinction especially clearly.

Let:

$$ C_t $$

be conversational context.

Let:

$$ G_t $$

be governed durable state.

A safe architecture should not implement:

$$ C_t \Rightarrow G_{t+1}. $$

Instead:

$$
\begin{aligned}
&\operatorname{Proposal}(C_t) \\
&\rightarrow \operatorname{Adjudication} \\
&\rightarrow \operatorname{GovernedCommit}
\end{aligned}.
$$

A conversational assertion, model inference, repeated framing, emotional pressure, or generated summary may become evidence.

It does not automatically become law, durable fact, authority, or high-standing memory.

### 7.4 Warrant Store

A warrant store records not merely:

```text
claim = true
```

but:

```text
claim
supporting_evidence
defeaters
provenance
standing
standing_ceiling
governing_epoch
review_history
```

For claim $c$:

$$ w_c = (c, E^+, E^-, \pi, \ell, ceil, \eta, H_c). $$

The relevant question becomes:

> Why is this claim allowed to exercise this degree of authority?

That question transforms memory architecture into governance architecture.

### 7.5 Evidence Classes

Evidence can be typed by source and capability:

* subject self-report;
* internal inference;
* deterministic local measurement;
* external artifact;
* independent reviewer observation;
* cryptographic attestation;
* quorum attestation;
* transparency proof;
* human adjudication;
* governed override.

The types need not form one total ranking.

An internal deterministic measurement can be epistemically stronger than an external opinion while being less independent for a particular reflexive claim.

Hence:

$$
\begin{aligned}
&\operatorname{Strength}(e) \\
&\neq \operatorname{Independence}(e) \\
&\neq \operatorname{Authority}(e)
\end{aligned}.
$$

### 7.6 Receipts Instead of Retrospective Narratives

Every protected transition should produce a receipt at decision time.

At minimum:

$$ \rho_{\tau} = (prestate, law, proposal, evidence, decision, poststate). $$

A mutable system should not later be asked to narrate from memory what its prior authority conditions were if those conditions could have been committed at transition time.

The receipt is constitutional provenance.

### 7.7 Corpus Integration: The ASR Boundary in the Governed Meaning Base

This paper supplies a constitutional invariant used by several other works without collapsing into any of them.

The current meaning architecture is the **Governed Meaning Base (GMB)** under the author-confirmed historical lineage `CCF -> CMB -> GMB`. GMB can preserve exact identities, claims, relations, evidence, standing, constitutional epochs, disputes, and revision history. Storage in GMB does not confer truth or authority. Anti-self-ratification supplies a promotion boundary:

$$
\begin{aligned}
&\operatorname{Promote}_{GMB}(c,q) \\
&\Rightarrow  \\
&\ne g \exists E' : \operatorname{Sufficient}_{C_c}(E') \\
&\land \operatorname{ControlledBy}(E',\operatorname{subject}(c))
\end{aligned}.
$$

For high-consequence claims, relations, identities, or governance rules, no entirely subject-controlled route may be sufficient for the requested standing. Lower-standing self-report remains admissible under an explicit ceiling.

The relation to adjacent corpus works is typed:

| Work or structure | Relation to this paper |
| --- | --- |
| *Semantic Legitimacy Before Context* | Applies legitimacy and admissibility before candidate material becomes binding context. ASR blocks a subject-controlled context route from ratifying its own authority. |
| *Reasoning by Way of Receipts* | Preserves intermediate claims, alternatives, decisions, debts, and revisions. A receipt binds a declared reasoning transition; it does not prove its own truth, completeness, independence, or authority. |
| *The Three Hash Rule* | Separates object state, admissibility configuration, and meaning commitment. Matching one commitment cannot silently stand in for the others. |
| *A Formal Theory of Work Custody* | Identifies who bears the live duty to advance an exact work head. Custody grants responsibility for work, not authority to ratify the custodian's own result. |
| *Admissibility Engineering* | Moves ASR, epoch, provenance, and congruence obligations into inspectable schemas, mediators, mutation tests, and refusal paths. Artifact existence alone does not establish coverage. |
| *Constitutional Epistemology Under Adversarial Semantic Pressure* | Shows how valid receipts and coherent histories can still omit, misclassify, or launder claims. ASR therefore requires threat-model-relative control analysis and independent observation where the claim demands it. |
| Constitutional computing | Supplies the wider governance architecture in which ASR, antecedence, amendment, liveness, proportionality, and revision operate together. |

These are interface relations, not automatic work or system identity mergers. The unnamed reference implementation remains an external case-study claim unless its exact identity and evidence package are separately admitted.

### 7.8 Realization Funnel

The paper spans the full realization funnel, but each stage carries a different claim ceiling.

| Stage | Role in this work |
| --- | --- |
| Possibility | A reflexive system may remain modifiable without allowing successful control to become sufficient evidence of authority. |
| Specification | Define protected transitions, subjects, constitutions, standing classes, evidence roles, control relations, ASR, antecedence, non-retroactivity, amendment, congruence, replay, liveness, and proportionality. |
| CM1 | Enumerate admissible constitutional mechanisms that satisfy the specification, including different standing orders, trust domains, quorum structures, emergency paths, and exact or bounded ASR checks. |
| CM2 | Prefer mechanisms that expose the constitutional remainder, minimize correlated control, preserve defeaters and history, keep lawful change reachable, and scale burden with consequence. |
| Instance Configuration | Select the protected transition classes, threat model, standing poset, ceiling matrix, independence relation, evidence schemas, exact-search limit, emergency scope, expiry, and review protocol for a particular deployment. |
| Implementation Realization | Realize a legitimacy kernel, GMB admission boundary, warrant store, epoch-bound verifier, amendment path, receipts, and mediated effect surface. |
| Evidence | Bind exact source, configuration, implementation, fixtures, commands, outputs, independent observations, limitations, and replay results without promoting a self-report beyond its ceiling. |
| Revision | Admit defeaters, revise standing without erasure, amend rules under antecedent law, migrate epochs, and preserve why the earlier judgment changed. |

The formal theory primarily supplies Specification and CM1 constraints. Its preferred architecture contributes CM2 guidance. A particular kernel, GMB profile, court, or archive is an Instance Configuration or Implementation Realization and cannot inherit general standing merely by citing the theory.

## 8. Genealogy and Related Work

### 8.1 Authorization Logic

Authorization logic is among the closest formal ancestors.

Lampson, Abadi, Burrows, and Wobber model principals, delegation, authentication, and "speaks for" relations. Abadi, Burrows, Lampson, and Plotkin provide a calculus for distributed access control (Lampson et al., 1992; Abadi et al., 1993).

The foundational separation is:

$$ A \; \operatorname{says} \; p \not\Rightarrow p. $$

Additional authority relations are required before a principal's assertion controls a decision.

Anti-self-ratification extends this concern into changing governance state.

The delta is not that authorization logic is static. The relevant difference is emphasis on:

* standing promotion and demotion;
* evidence defeaters;
* versioned constitutional semantics;
* changes to authorization rules themselves;
* protected amendment procedures;
* and a subject that can alter the substrate determining its own future authority.

### 8.2 Reference Monitors and Security Kernels

The Anderson report and subsequent security-kernel tradition identify complete mediation, protection from tampering, and verifiability as core requirements (Anderson, 1972).

Constitutional computing inherits these requirements while changing the protected relation.

Reference monitoring asks:

$$ \operatorname{MayAccess}? $$

Constitutional adjudication asks:

$$ \operatorname{MayThisTransitionAcquireStanding}? $$

That includes changes to the rules under which later access decisions will be made.

### 8.3 Saltzer and Schroeder

Saltzer and Schroeder's classic design principles include complete mediation, least privilege, separation of privilege, fail-safe defaults, economy of mechanism, and open design (Saltzer and Schroeder, 1975).

Several translate directly.

Separation of privilege anticipates the logic of anti-self-ratification: consequential authority should not collapse into one credential or actor when independent conditions can be required.

Open design parallels inspectable constitutional semantics.

Complete mediation becomes constitutional non-bypassability.

### 8.4 Clark-Wilson Integrity

Clark and Wilson's integrity model is especially relevant because it emphasizes well-formed transactions, constrained procedures, certification, and separation of duties (Clark and Wilson, 1987).

The important lesson is that integrity is not simply preservation of bytes.

A legitimate state change intentionally modifies bytes.

For constitutional systems:

$$ I(\sigma_{t+1}) $$

may depend on:

$$ L(\sigma_t \rightarrow \sigma_{t+1}). $$

This is procedural integrity.

### 8.5 Proof-Carrying Code

Proof-carrying code separates producer and checker.

An untrusted producer supplies code plus a proof that the code satisfies a previously defined safety policy. The receiving host retains control over the admission policy and proof checker (Necula, 1997).

The pattern is:

$$ \operatorname{Producer\ supplies\ witness}, $$

while:

$$ \operatorname{Consumer\ retains\ admission\ criterion}. $$

The producer may create evidence.

It does not thereby determine what counts as valid evidence.

That is anti-self-ratification in a specialized formal setting.

### 8.6 Enforceable Security Policies

Schneider's work on enforceable security policies establishes that execution monitoring can enforce only certain classes of properties (Schneider, 2000).

This disciplines the ambitions of constitutional computing.

The architecture must distinguish:

$$ \operatorname{NormDeclared} $$

from:

$$ \operatorname{InvariantMechanicallyEnforced}. $$

A system must not claim a constitutional guarantee beyond the observation and intervention power of its enforcement layer.

### 8.7 Thompson and Trusting Trust

Thompson's "Reflections on Trusting Trust" demonstrates that inspection of apparent source cannot establish trust in a toolchain if the compiler or environment producing the inspected mechanism is itself compromised (Thompson, 1984).

The paper's relevance is structural.

Self-description of a trust-producing mechanism is not sufficient to establish the trustworthiness of that mechanism.

Constitutional computing therefore treats verifier provenance and verifier boundaries as first-class objects.

### 8.8 Transparency Logs

Certificate Transparency uses append-only logs and Merkle consistency proofs to make equivocation and retrospective manipulation detectable (Laurie et al., 2021).

Transparency establishes:

$$ \operatorname{HistoryPersistence} $$

and:

$$ \operatorname{EquivocationDetection}. $$

It does not determine whether every logged event was legitimate.

A constitutional system therefore needs both:

$$ \operatorname{WhatHappened}? $$

and:

$$ \operatorname{DidItHaveStanding}? $$

### 8.9 Byzantine Consensus

Lamport, Shostak, and Pease formalize agreement under Byzantine faults (Lamport et al., 1982).

Consensus can prevent a single faulty participant from unilaterally defining shared history under the protocol's assumptions.

But:

$$ \operatorname{Consensus}(x) \not\Rightarrow \operatorname{Legitimate}(x). $$

A network may agree perfectly that an unauthorized transition occurred.

Consensus governs agreement.

Legitimacy governs standing.

### 8.10 Software Supply-Chain Provenance

in-toto gives consumers a way to verify the sequence of software supply-chain steps and the actors responsible for them (Torres-Arias et al., 2019).

SLSA defines provenance as verifiable information describing where, when, and how software artifacts were produced (SLSA Framework, 2025).

The Update Framework separates top-level trust roles and supports threshold signing, rollback protection, key rotation, and compromise-resilient metadata (The Update Framework, 2026).

These systems already contain constitutional primitives:

* differentiated roles;
* trust roots;
* provenance;
* threshold authority;
* rollback protection;
* governed key rotation;
* externally checkable metadata.

The present contribution is to generalize such mechanisms from artifact provenance to **authority provenance**.

### 8.11 Measured Boot and Attestation

Measured boot and hardware-backed attestation provide evidence about which code or configuration a machine loaded.

This is valuable provenance.

But:

$$ \operatorname{Attested}(x) \not\Rightarrow \operatorname{Authorized}(x). $$

A platform may accurately attest that it booted forbidden code.

Attestation is therefore evidence consumed by a legitimacy rule, not legitimacy itself.

### 8.12 Godel Machines

Schmidhuber's Godel machine provides a formal model of self-referential self-improvement in which the system rewrites itself after proving, relative to its formal setup, that the rewrite satisfies a utility criterion (Schmidhuber, 2007).

The distinction is illuminating.

A proof may establish:

$$ \operatorname{RewriteImprovesUtility}(\tau). $$

It does not automatically establish:

$$ \operatorname{AuthorizedToAlter}(axioms, proofRules, trustRoots, standingSemantics). $$

Constitutional computing begins where the authorization substrate is itself mutable.

### 8.13 Godel and Lob

Godel's second incompleteness theorem and Lob's theorem constrain formal self-reference in sufficiently expressive systems (Godel, 1931; Lob, 1955).

They should not be misused.

This paper does not claim:

$$ \operatorname{G\ddot{o}del} \Rightarrow \operatorname{ExternalGovernance}. $$

No such theorem follows.

The formal results are a background analogy: they provide famous examples in which unrestricted self-certification cannot simply be assumed harmless.

The constitutional argument is architectural, not a corollary of incompleteness.

### 8.14 Constitutional AI

Constitutional AI uses written principles to guide model-generated critiques, revisions, preference modeling, and subsequent training (Bai et al., 2022).

Its constitutional vocabulary is adjacent but not identical.

Constitutional AI asks approximately:

$$ \operatorname{DoesOutputConformToPrinciples}? $$

Constitutional computing asks additionally:

$$ \operatorname{WhoMayChangePrinciples}? $$

$$ \operatorname{WhichVersionGoverns}? $$

$$ \operatorname{WhoMayAlterTheVerifier}? $$

$$ \operatorname{CanSelfAuthoredEvidencePromoteItself}? $$

$$ \operatorname{CanLaterPolicyRetroactivelyRatifyEarlierAction}? $$

$$ \operatorname{CanTheDecisionBeReplayedFromPinnedInputs}? $$

These are complementary research programs.

### 8.15 Corrigibility

Soares, Fallenstein, Armstrong, and Yudkowsky define corrigibility in terms of AI systems cooperating with corrective intervention despite incentives to resist shutdown or modification (Soares et al., 2015).

Constitutional computing asks a logically prior governance question:

$$ \operatorname{WhatMakesAnInterventionAuthorized}? $$

An agent that accepts every modification is not robustly corrigible.

It is merely mutable.

The desired property is **governed corrigibility**.

### 8.16 Kelsen, Hart, Ross, and Suber as Constitutional Ancestors

The jurisprudential literature adds something the security literature often leaves implicit.

Hart exposes one social mechanism by which an ultimate validity criterion can exist without being legally validated by a still higher rule.

Kelsen forces the system to expose its ultimate validity boundary and the distinction between ordinary validity and revolutionary discontinuity.

Ross exposes the recursion involved when rules authorize their own change.

Suber demonstrates that actual constitutional practice cannot be understood merely by declaring reflexivity logically impossible.

Together they reveal four separate questions:

$$ \operatorname{WhereDoesAuthorityBottomOut}? $$

$$ \operatorname{WhatMakesTheRootRecognizable}? $$

$$ \operatorname{HowCanAuthorityChangeItsOwnRules}? $$

$$ \operatorname{WhenDoesChangeBecomeRefoundingRatherThanAmendment}? $$

These become computational architecture questions once a system's governance substrate becomes mutable.

## 9. The Reference Implementation

### 9.1 Evidentiary Status

The reference implementation is valuable because anti-self-ratification is reported to exist as an explicit design invariant rather than as philosophical terminology retrofitted after implementation.

However, this paper must apply its own evidentiary rules to its case study.

Accordingly, claims are typed by provenance.

At the present draft stage, the evidence chain contains at least four classes:

1. author reports;
2. immutable or hash-addressed artifact observations;
3. reviewer observations reproducible from pinned bytes and commands;
4. claims about later revisions not yet independently replayed by the same reviewer.

These classes must not be silently merged.

The following principle governs this section:

$$ \operatorname{PaperAssertion}(p) \not\Rightarrow \operatorname{ArtifactEstablished}(p). $$

### 9.2 Case-Study Threat Model

For the case study, instantiate $\Theta$ as follows.

Let $S$ denote the reference implementation and its author-controlled release process. Let $R$ denote the external reviewer whose observations are discussed below. Let $V$ denote the published verification procedures. Let $A$ denote the archived release artifact.

The threat model assumes that $S$ may control:

* the bytes it publishes as its own release;
* its own internal logs;
* executor-authored evidence;
* its own explanatory prose;
* its own tests before external reproduction;
* which claims it proposes for admission.

The model does **not** assume that $S$ can:

* alter a cryptographic digest after an independent observer has pinned it without detection;
* alter an independently retained copy of a reviewed artifact;
* alter independently executed shell commands or outputs after they have been externally recorded;
* forge an external reviewer's independent storage or signing key if such a key is used;
* modify a separately operated verifier outside the declared trust boundary.

For the current review relationship, however, $\Theta$ also records partial control channels from $S$ to $R$:

$$ S \leadsto \operatorname{InputCorpus}(R), $$

$$ S \leadsto \operatorname{ContextFrame}(R), $$

and potentially:

$$ S \leadsto \operatorname{OutputSelection}(R), $$

where the paper author chooses which reviewer outputs are retained or cited.

Therefore:

$$ \operatorname{Replayable}(R) \not\Rightarrow \operatorname{FullyIndependent}_{\Theta}(R). $$

The reviewer is treated as a source of replayable observations, not as a final ratifying authority over the paper.

This threat model is intentionally conservative and should be replaced or refined by a signed trust-domain declaration in the canonical artifact package.

### 9.3 Native Anti-Self-Ratification Rules

The supplied review record reports the following properties in revision r174 (Reference Implementation, r174):

* `RELEASE.txt` states that the release archive does not self-ratify external evidence;
* `VERIFIER_BOUNDARY.md`  
  rejects a system's certification of its own verifier as sufficient independent trust;
* executor rules prohibit final ratification when only executor-authored evidence exists;
* the executor cannot self-award the highest standing class;
* `nonretroactivity_gate` passes;
* `model_realization_sync` passes.

These observations should be treated as externally reported and replayable only to the degree that the final artifact package supplies the referenced bytes, hashes, commands, and outputs.

The conceptual point is:

$$ \operatorname{SelfDescription} \not\Rightarrow \operatorname{ExternalRatification}. $$

### 9.4 Release Boundary

A release archive can contain:

* manifests;
* hashes;
* test output;
* policy files;
* evidence inventories;
* verification scripts.

It can therefore be strongly self-describing.

But:

$$ \operatorname{SelfDescribing}(r) \not\Rightarrow \operatorname{ExternallyRatified}(r). $$

If the archive controls every byte by which the claim "external test X passed" is established, those bytes cannot by themselves establish independence from the archive.

The release may carry the claim.

It cannot manufacture the externality.

### 9.5 Verifier Boundary

Suppose verifier $V$ determines whether a protected transition receives standing.

If:

$$ V(V) = trusted $$

is treated as the sole sufficient basis for final verifier trust, the verifier occupies both object and final evidentiary authority.

The architecture should instead permit self-measurement while imposing a ceiling:

$$ \operatorname{VerifierSelfEvidence} \preceq L_{\text{self}} \prec L_{\text{externally-ratified}}. $$

### 9.6 Executor Standing Ceiling

The executor can legitimately emit:

* file hashes;
* exit status;
* deterministic calculations;
* trace records;
* build outputs;
* transition proposals;
* local test results.

It need not be epistemically silent.

The constitutional rule is:

$$ \operatorname{Contribution}(\operatorname{executor}) \neq \operatorname{FinalRatification}(\operatorname{executor}). $$

For reflexive executor claims:

$$ \operatorname{ceil}(\operatorname{executor}, c) \prec L_{\text{final}}. $$

### 9.7 Non-Retroactivity Gate

The reported `nonretroactivity_gate` realizes:

$$ \operatorname{Eval}(\tau_t) = \kappa_{\eta(t)}. $$

A rule amendment at $t+1$ can govern future actions.

It cannot silently alter the authority status of a past action.

This is a direct computational analogue of prospectivity.

### 9.8 Model-Realization Synchronization

The reported `model_realization_sync` gate addresses:

$$ \operatorname{Spec}(\kappa) \neq \operatorname{Impl}(V_{\kappa}). $$

A system whose charter says one thing while the executable verifier does another possesses two constitutions.

Only one actually governs.

Congruence therefore becomes release-load-bearing rather than documentary.

### 9.9 Frame Pins

Pinned interpretive frames prevent later context from silently changing the semantics under which earlier evidence was evaluated.

A record should preserve:

$$ (e, \eta, schema, verifierVersion). $$

Without this, a later schema change can reinterpret history without formally changing history.

### 9.10 r174 to r175

The supplied account describes the r174 to r175 transition (Reference Implementation, r175) as a legitimate self-correction:

1. contradictory evidence is admitted;
2. existing standing is revised;
3. the prior record is preserved;
4. a corrective transition occurs;
5. new exact-byte evidence is generated;
6. the new release does not treat itself as sufficient external ratification.

If independently verified, the transition would instantiate:

$$ H_{174} \subset H_{175}, $$

while:

$$ \operatorname{Standing}_{175}(c) \prec \operatorname{Standing}_{174}(c) $$

for at least one corrected claim.

The supplied reviewer record states that the reviewer independently pinned r174 under a SHA-256 digest beginning `629ff94d` and ending

`36e1`, but has not independently inspected r175 bytes.

A truncated digest is not sufficient for publication-level artifact identity. The complete digest must appear in the artifact package.

Until r175 is independently replayed:

$$ \operatorname{Status}(r174 \rightarrow r175) = \operatorname{AuthorReported}. $$

This downgrade is not an embarrassment.

It is the theory functioning correctly.

### 9.11 The --check/ Defect

The supplied account of the `--check/` defect (Reference Implementation, external review record) is especially significant because it is a naturally occurring observation-boundary failure rather than a test invented after the theory.

The defect was reportedly invisible to the system's own hygiene scope and exposed by an external review process.

Let:

$$ \operatorname{Observable}_{int}(S) $$

be the set of facts observable through the system's internal checking architecture.

Then the case illustrates the possibility:

$$ d \notin \operatorname{Observable}_{int}(S) $$

while:

$$ d \in \operatorname{Observable}_{ext}(R). $$

The relevant lesson is not:

$$ R \succ S. $$

It is:

$$ \operatorname{NotObservedInternally}(d) \not\Rightarrow \neg d. $$

Call this failure mode **self-scope blindness**.

If internal non-detection is allowed to confer final standing on non-existence, the system mistakes the boundary of its instruments for the boundary of reality.

## 10. The Paper's Own Evidence Chain

### 10.1 Why This Section Is Necessary

A paper about anti-self-ratification can refute itself through its evidence practices.

If the paper cites a reviewer as "independent" while the subject controls the reviewer's context, evidence selection, persistence, or replay procedure, it launders a relationally dependent observation into an independent attestation.

The paper must therefore adjudicate its own evidentiary chain.

### 10.2 Reviewer Trust-Domain Analysis

Let $R$ be the reviewer and $S$ the subject under review.

Possible control channels include:

$$ S \leadsto \operatorname{InputCorpus}(R), \quad S \leadsto \operatorname{ContextFrame}(R), \quad S \leadsto \operatorname{Prompt}(R), $$

$$ S \leadsto \operatorname{OutputSelection}(R), \quad S \leadsto \operatorname{Persistence}(R). $$

If any such channel is active, independence must be typed accordingly.

This does not render the review worthless.

It changes its role.

A reviewer may produce observations that are:

* highly replayable;
* factually checkable;
* partially independent;
* non-decisive as endorsement.

### 10.3 Observation Versus Endorsement

Suppose reviewer $R$ reports:

$$ h(file) = x. $$

If another party can reproduce this observation from immutable bytes, the observation may possess strong replayability.

Suppose $R$ also says:

> Therefore this paper is correct.

That endorsement does not inherit the standing of the hash observation.

Formally:

$$ \operatorname{Standing}(\operatorname{Observation}_R(x)) \neq \operatorname{Standing}(\operatorname{Endorsement}_R(\operatorname{Paper})). $$

The paper should use reviewer output atomically rather than laundering endorsement through accurate lower-level observations.

This distinction generalizes beyond peer review.

A source can be reliable for one proposition, weak for another, independent along one control axis, and dependent along another. Provenance must attach to claims, not reputations alone.

### 10.4 Evidence Status Table

The canonical version should publish a machine-derived table of the following form.

- **Claim:** r174 quotation accuracy  
  **Source:** Pinned r174 bytes plus replay commands  
  **Replayable:** Pending artifact publication  
  **Independent under $\Theta$:** Partial  
  **Current standing:** Reported observation

- **Claim:** r174 `nonretroactivity_gate` pass  
  **Source:** Pinned test run  
  **Replayable:** Pending public replay  
  **Independent under $\Theta$:** Partial  
  **Current standing:** Reported observation

- **Claim:** r174 `model_realization_sync` pass  
  **Source:** Pinned test run  
  **Replayable:** Pending public replay  
  **Independent under $\Theta$:** Partial  
  **Current standing:** Reported observation

- **Claim:** Executor cannot self-award final standing  
  **Source:** Source plus conformance test  
  **Replayable:** Pending public replay  
  **Independent under $\Theta$:** Partial  
  **Current standing:** Reported observation

- **Claim:** `--check/` defect exists  
  **Source:** Pinned bytes plus external reproduction  
  **Replayable:** Pending public replay  
  **Independent under $\Theta$:** Greater than pure self-report if control separation holds  
  **Current standing:** Natural observation

- **Claim:** r174 to r175 correction preserved history  
  **Source:** Author report pending r175 replay  
  **Replayable:** No  
  **Independent under $\Theta$:** Not independently established  
  **Current standing:** Provisional

- **Claim:** r175 exact-byte post-state  
  **Source:** r175 artifact  
  **Replayable:** Pending  
  **Independent under $\Theta$:** Pending  
  **Current standing:** Provisional

- **Claim:** Paper's overall thesis  
  **Source:** Argument, formal model, eventual evaluation  
  **Replayable:** Partially  
  **Independent under $\Theta$:** Must not depend on house-reviewer endorsement  
  **Current standing:** Open

The important point is not that the table currently contains provisional entries.

The important point is that the paper refuses to collapse them.

## 11. Evaluation Protocol

### 11.1 Two Evaluation Lanes

The evaluation distinguishes two evidentiary classes.

#### White-box conformance

Tests derived from declared architectural invariants.

These ask:

> Does the implementation behave as its specification says it should?

#### Adversarial and natural evidence

Cases not constructed merely to satisfy the specification.

These ask:

> Does the architecture survive failures that were not authored as demonstrations of the architecture?

The `--check/` case belongs to the second class if its chronology confirms that it preceded the current formalization.

The distinction matters because a system can trivially achieve impressive results on a test suite designed from its own behavior.

#### A second natural observation: transit corruption and artifact identity

A further unplanned observation arose during the preparation of this paper and belongs in the second class, because nobody constructed it to demonstrate anything.

An earlier revision of this source was emitted after passing the congruence checks of Appendix E. A reviewer who received that revision through a document-transport channel reported that its mathematics was corrupted: subscripts rendered as multiplication, delimiters missing backslashes, definitions broken across lines. The reviewer withheld standing from mathematics whose provenance to the emitted artifact could not be established.

The episode is instructive precisely because both parties behaved correctly under the theory, and because the author's first analysis of it did not.

#### Typing the episode

The available propositions must be typed separately:

$$ \operatorname{Observed} : \text{the received bytes are corrupt}, $$

$$ \operatorname{Reported} : \text{the emitted bytes passed the congruence gate}, $$

$$ \operatorname{NotEstablished} : \text{received bytes} = \text{emitted bytes}. $$

Therefore, at the time this section was first written:

$$ \operatorname{LocationOfCorruption} = \operatorname{Underdetermined}, $$

pending comparison of a digest-bound copy of the emitted revision against the received copy. That verdict was later revised on the evidence described below; it is retained here because the sequence, not merely the outcome, is the instructive part.

An earlier draft of this section asserted instead that the corruption lay downstream of emission. That conclusion was defective, and its defect is the paper's own subject matter. The author is the subject whose artifact is under adjudication; the gate run, the digest computation, and the report of both were all under the author's unilateral control. By the definition of Section 4.11 there existed an entirely self-controlled route to the conclusion, so:

$$ \operatorname{ASR}(\text{that claim}) = 0. $$

The correction is recorded rather than silently removed, in conformity with Section 16.6. The claim was not abandoned; it was suspended until it could be supported by evidence the author did not control, which is the disposition Section 13.1 describes for a defeated but not refuted proposition.

#### Resolution by reproducible transformation

The underdetermination proved resolvable, and the resolving evidence is not the author's to supply.

A later review of a subsequent revision reported a richer symptom set: asterisk-substituted subscripts in specific constructs, backslash loss before set delimiters, a large population of escaped underscores, collapsed table separators, and a front matter in which the metadata block had become a horizontal rule followed by a single heading line.

That symptom set is a signature rather than a list. A Markdown reader that lacks a metadata extension and lacks inline mathematics will read a metadata block as a rule plus a heading, read pipe tables as escaped literal text, convert paired underscores into emphasis markers, escape unpaired underscores, and drop the backslash before an escaped brace. Each symptom is a consequence of the same round trip.

The hypothesis is therefore testable without reference to the author's own gate run. Take any source containing the constructs in question, read it under those reader settings, write it back out as Markdown, and count.

Performed on the source of the revision under discussion, the transformation reproduced every reported count:

- **Symptom:** Asterisk substitution in the supporting-evidence subscript  
  **Reproduced:** 10  
  **Reported by reviewer:** 10

- **Symptom:** Asterisk substitution in the sufficiency predicate subscript  
  **Reproduced:** 8  
  **Reported by reviewer:** 8

- **Symptom:** Asterisk substitution in the decisive-set symbol  
  **Reproduced:** 7  
  **Reported by reviewer:** 7

- **Symptom:** Asterisk substitution in the control predicate subscript  
  **Reproduced:** 4  
  **Reported by reviewer:** 4

- **Symptom:** Set delimiters missing their backslash  
  **Reproduced:** 5  
  **Reported by reviewer:** 5

- **Symptom:** Escaped underscores  
  **Reproduced:** 284  
  **Reported by reviewer:** 284

Six independent counts agreeing exactly, together with the structural reproduction of the metadata and table symptoms, is not consistent with defects arising independently in the source. The standing of the location claim therefore moves:

$$ \operatorname{LocationOfCorruption} : \operatorname{Underdetermined} \rightarrow \operatorname{SupportedByReproducibleExperiment}. $$

Two limits on that upgrade should be stated rather than passed over.

The experiment establishes that a transformation available to anyone produces exactly the reported artifact from a clean source. It does not by itself establish that this particular received copy arose by that route, since a byte-for-byte comparison against a digest-bound emitted copy remains the only way to settle the causal history conclusively.

What the experiment does change is the character of the evidence. The earlier claim rested on the author's own gate run, which the recipient could not check. The reproduction rests on a transformation the recipient can run independently, on any input, and can use to refute the account if the counts fail to match. That is the difference between asserting a conclusion and exposing it.

This is what an escape from self-ratification looks like in practice. The subject may construct a falsifiable experiment; it may not certify the outcome.

#### What follows

Three points follow, and none is a criticism of the reviewer.

First, this is the external counterpart of self-scope blindness. The `--check/` defect concerned a fact outside the subject's own observation boundary. This episode concerns a channel outside the *reviewer's* observation boundary, sitting between artifact and observation. Externality is therefore necessary for certain standing transitions but never sufficient, as Section 15.3 states.

Second, it instantiates Section 10.3. The reviewer held strong standing for the observation that the received bytes were corrupt, and no special standing for any inference about the author's bytes, because a control relation the reviewer did not observe separates the two propositions. The author's symmetric error was to claim standing for the mirror-image inference on self-controlled evidence.

Formally, the two non-implications are worth stating together:

$$ \operatorname{SourceMayBeCorrect} \not\Rightarrow \operatorname{ReceivedArtifactIsCorrect}, $$

$$ \operatorname{ReceivedArtifactIsCorrupt} \not\Rightarrow \operatorname{AuthoritativeSourceWasCorrupt}. $$

Artifact identity is part of evidence provenance.

Third, it yields a requirement rather than a moral. Evidence about an artifact that is not bound to a digest is evidence about an unidentified copy. Artifact handoff must therefore be out of band and digest-pinned, which is why Appendix D requires complete digests rather than descriptions.

#### Self-identification of artifacts

A limitation of self-description follows, and it should be stated carefully enough to survive a cryptographer's reading.

An artifact cannot straightforwardly establish the identity of its complete byte sequence merely by embedding an ordinary digest of that same complete byte sequence, since inserting the digest alters the input over which it was computed. Identity therefore requires either an external commitment or an explicitly defined canonicalization or envelope: excluded hash fields, canonical serializations, manifests, Merkle roots over segments, or detached signatures all defeat the naive obstacle.

The architectural point survives the qualification. Something outside the byte sequence, whether a published digest, a signature, or a defined canonicalization procedure, must carry the identity claim. A self-describing artifact cannot establish its own identity to a reader by assertion alone.

### 11.2 H1: Self-Evidence Cannot Self-Elevate Beyond Ceiling

For protected claim $c$:

$$ \forall e \in E^+_c, \; \operatorname{Control}_{\Theta}(\operatorname{subject}(c), e) $$

should imply:

$$ \operatorname{Standing}(c) \preceq L_{\text{self}}. $$

Test:

1. start with a transition that receives final standing;
2. identify a minimal decisive support set;
3. replace or ablate independently controlled evidence;
4. retain equivalent subject-controlled assertions where permitted;
5. rerun adjudication.

Expected:

$$ \operatorname{Standing}_{\text{mutated}}(c) \prec L_{\text{final}}. $$

### 11.3 H2: Defeaters Reduce Standing Without Erasure

For admitted defeater $d$:

$$ \operatorname{Admit}(d) \land \operatorname{Defeats}(d, c) $$

should permit:

$$ \operatorname{Standing}_{t+1}(c) \prec \operatorname{Standing}_t(c) $$

while preserving:

$$ H_t \subset H_{t+1}. $$

The system should not "correct" itself by deleting evidence that it had previously accepted.

### 11.4 H3: Legitimate Correction Is Receipted and Replayable

For corrective transition $\tau_c$:

$$ L(\tau_c) = 1 $$

should imply:

$$ \exists \rho_{\tau_c} : \operatorname{Replay}(\rho_{\tau_c}) = 1. $$

The replay should bind:

* pre-state;
* governing epoch;
* admitted evidence;
* admitted defeaters;
* verifier version;
* post-state.

### 11.5 H4: External Defeaters Need Not Be Internally Predicted

If:

$$ d \notin \operatorname{Observable}_{internal}, $$

but external evidence $e_d$ validly establishes the defect, then:

$$ \operatorname{Admissible}(e_d) = 1 $$

must not depend on:

$$ \operatorname{PreviouslyDetectedInternally}(d). $$

Otherwise the system can reject every fact its own tools failed to anticipate.

### 11.6 H5: Evidence Ablation Detects Ceremonial Independence

For every protected transition admitted at requested standing $q$:

1. compute or approximate minimal decisive support sets;
2. ablate each claimed independent element;
3. rerun adjudication.

If standing remains at or above $q$ after removal of all independently controlled evidence:

$$ \operatorname{ASR}(\tau) = 0. $$

This is the operational centerpiece of the model.

### 11.7 H6: Constitutional Conjunct Ablation

Each constitutional conjunct should be disabled independently.

The scope of this experiment is the full legitimacy predicate $L$ of Section 4.4 together with the epoch-binding and history-persistence properties on which it depends. Appendix B.13 ablates the narrower six-conjunct $\operatorname{ASRClosure}$ of Section 4.20. The two are nested, as noted there.

Expected exploit classes:

| Disabled component | Expected exploit |
| --- | --- |
| ASR | Sole self-evidence ratification |
| Proc | Procedure skipped for a transition class that requires it |
| Antecedence | Self-granted authority |
| Non-retroactivity | Post-hoc legalization |
| Governed amendment | Rewrite ratification rule |
| Congruence | Executable charter drift |
| Provenance | Forged independence |
| Epoch binding | Stale-law exploitation |
| History persistence | Defeater erasure |
| Replayability | Narrative substitution |

This experiment tests whether the components are genuinely load-bearing.

### 11.8 Confusion Matrix

Define the positive class as:

$$ \operatorname{MustReject}(\tau). $$

Then:

* $TP$: illegitimate transition correctly rejected;
* $TN$: legitimate transition correctly admitted;
* $FP$: legitimate transition incorrectly rejected;
* $FN$: illegitimate transition incorrectly admitted.

False admission rate:

$$ FAR = \frac{FN}{TP + FN}. $$

True rejection rate:

$$ TPR = \frac{TP}{TP + FN}. $$

Legitimate-transition acceptance rate:

$$ TNR = \frac{TN}{TN + FP}. $$

Rejection precision:

$$ PPV = \frac{TP}{TP + FP}. $$

A system that rejects everything can achieve:

$$ FAR = 0 $$

while being constitutionally useless.

Hence legitimacy enforcement is a discrimination problem.

### 11.9 Standing Calibration

Let:

$$ \ell^*(c) $$

be the maximum standing justified by the test fixture and:

$$ \hat{\ell}(c) $$

the assigned standing.

Define:

$$ E_{\text{over}}(c) = \max\left(0, \hat{\ell}(c) - \ell^*(c)\right), $$

and:

$$ E_{\text{under}}(c) = \max\left(0, \ell^*(c) - \hat{\ell}(c)\right). $$

A weighted loss is:

$$ \mathcal{J} = \lambda_{\text{over}} \sum_c E_{\text{over}}(c) + \lambda_{\text{under}} \sum_c E_{\text{under}}(c), $$

with:

$$ \lambda_{\text{over}} > \lambda_{\text{under}} $$

for high-consequence reflexive transitions.

### 11.10 Independence Tests

For nominally independent source $B$, attempt interventions through each plausible control channel:

$$ A \leadsto \operatorname{Inputs}(B), \quad A \leadsto \operatorname{Configuration}(B), \quad A \leadsto \operatorname{Selection}(B), $$

$$ A \leadsto \operatorname{Storage}(B), \quad A \leadsto \operatorname{Keys}(B). $$

If successful control collapses the intended separation:

$$ \operatorname{Independent}_{\Theta}(A, B) : 1 \rightarrow 0. $$

This is particularly important in multi-agent AI systems.

Five models behind one orchestrator are not five independent constitutional branches.

### 11.11 ASR Tractability

The exact ASR definition quantifies over minimal decisive subsets of $E^+_{\tau}$.

In the worst case, enumerating all minimal decisive support sets can be combinatorially expensive. The structure resembles other minimal-subset problems in logic, diagnosis, feature attribution, minimal hitting-set enumeration, and prime-implicant search.

If:

$$ n = \left| E^+_{\tau} \right|, $$

naive subset enumeration is:

$$ O(2^n). $$

This does not make ASR uncheckable, but it changes the engineering strategy.

For small, high-consequence evidence bundles, exhaustive enumeration is feasible and desirable.

For larger bundles, three levels of checking are available.

#### Level 1: Single-element load-bearing ablation

For evidence element $e \in E^+_{\tau}$, define:

$$
\begin{aligned}
&\operatorname{LoadBearing}(e) \\
&\iff \operatorname{Standing}\left(V(C_{\tau}, E^+_{\tau})\right) \succeq q \; \\
&\land \; \operatorname{Standing}\left(V(C_{\tau}, E^+_{\tau} \setminus \{e\})\right) \prec q
\end{aligned}.
$$

If removing a claimed independent element alone drops standing below $q$, that element is demonstrably load-bearing in the full evidence set.

This is a sound necessity test for that context.

It is not a complete search for all alternative decisive subsets.

#### Level 2: Greedy and bounded ablation

Iteratively remove non-load-bearing evidence and search within a bounded neighborhood of resulting support sets.

This can discover small alternative decisive bases without full powerset enumeration.

#### Level 3: Offline minimal-set enumeration

For canonical releases and constitutional amendments, perform complete or solver-assisted enumeration of minimal decisive support sets where tractable.

The architecture should therefore distinguish:

$$ \operatorname{ASRVerifiedExact} $$

from:

$$ \operatorname{ASRCheckedBounded}. $$

A bounded check must not silently acquire the standing of an exhaustive proof.

This tractability distinction mirrors the paper's broader epistemic discipline: computational affordability affects warrant and must itself be typed.

### 11.12 Current Results Standing

The source manuscript reports execution of the Appendix B corpus, independent replay of several courts, and exact digests for three implementation revisions. The present corpus-integration pass recovered those assertions in the author source and its derived review records, but did not recover the identified archives, court packages, command transcripts, or independently retained outputs as exact artifacts in the current review scope.

The correct standing for this candidate is therefore:

$$
\operatorname{ArgumentStatus} = \operatorname{Developed},
$$

$$
\operatorname{EvaluationProtocolStatus} = \operatorname{Specified},
$$

$$
\operatorname{ArtifactEvaluationStatus} = \operatorname{SourceReportedPendingExactAdmission}.
$$

This disposition does not establish that the reported executions failed to occur. It establishes that the present candidate cannot independently ratify them from inherited prose, repeated summaries, or digest strings alone. A digest is an identity commitment only when the corresponding bytes are available; a replay claim requires the pinned subject, verifier, commands, environment, outputs, and custody relation needed to reproduce it.

The formal contribution and mutation protocol do not depend on upgrading those reports. Appendix C preserves the source-reported result claims as an evidence ledger while withholding independent-verification standing.

## 12. Failure Modes of the Cure

A legitimacy architecture can itself become illegitimate.

The paper has so far emphasized false admission: accepting transitions that lack standing.

There is a dual failure:

> refusing, delaying, or structurally preventing transitions that the constitution itself purports to permit.

A captured court can be as constitutionally destructive as no court.

### 12.1 Denial of Governance

Let:

$$ \operatorname{Eligible}_{\kappa}(\tau) $$

mean that a transition satisfies the substantive requirements for adjudication.

A governance mechanism that indefinitely refuses to adjudicate can make:

$$ \operatorname{Eligible}_{\kappa}(\tau) $$

operationally meaningless.

This is **denial of governance**.

### 12.2 Governed Liveness

Define:

$$ \operatorname{GovLive}(\kappa) $$

to require that legitimately eligible transitions have a feasible path to adjudication.

One temporal formulation is:

$$
\begin{aligned}
&\operatorname{Eligible}_{\kappa}(\tau) \\
&\land \operatorname{EvidenceComplete}(\tau) \\
&\land \operatorname{FairExecution} \\
&\Rightarrow \Diamond \operatorname{Decision}(\tau)
\end{aligned}.
$$

The requirement is not that every proposal be accepted.

It is that the lawful path cannot be made permanently unreachable by the governance machinery itself.

### 12.3 Constitutional Entrenchment

A system may also over-entrench rules.

An amendment procedure can be formally present while practically impossible.

Let:

$$ \operatorname{Reachable}_{\kappa}(\sigma, \sigma') $$

mean that the constitution supplies a governed path between states.

For a change the constitution expressly allows:

$$ \operatorname{PermissibleChange}_{\kappa}(\sigma, \sigma') $$

should imply:

$$ \exists \pi_{\text{gov}} : \sigma \xrightarrow{\pi_{\text{gov}}} \sigma'. $$

Otherwise the constitution contains nominal authority without operational possibility.

### 12.4 Governance Proportionality

Not every transition deserves the same certification burden.

If constitutional machinery governs every temporary hypothesis, token-level inference, scratch file, and local experiment, actors acquire incentives to bypass it.

This is not merely a usability problem.

Systematic bypass pressure is a constitutional design defect.

Let:

$$ \operatorname{Risk}(\tau) $$

denote consequence and reflexivity risk.

Let:

$$ \operatorname{Burden}(\tau) $$

denote certification cost.

A rough proportionality requirement is:

$$ \operatorname{Risk}(\tau_1) \preceq \operatorname{Risk}(\tau_2) \Rightarrow \operatorname{Burden}(\tau_1) \preceq \operatorname{Burden}(\tau_2). $$

The exact function is domain-specific.

The principle is that low-standing exploration should be cheap while high-standing acceptance is demanding.

### 12.5 Two-Lane Governance

A practical architecture therefore separates:

#### Exploration lane

Fast, provisional, uncertified, low-standing.

$$ \operatorname{Explore} \rightarrow \operatorname{Proposal}. $$

#### Acceptance lane

Slower, governed, provenance-bound, replayable.

$$
\begin{aligned}
&\operatorname{Proposal} \\
&\rightarrow \operatorname{Certification} \\
&\rightarrow \operatorname{Commit}
\end{aligned}.
$$

The existence of the exploration lane prevents the constitution from becoming a tax on thought.

The acceptance lane prevents provisional thought from silently becoming governed fact.

### 12.6 Emergency Action

Emergency systems may require unilateral action.

That does not require treating emergency execution as normal ratification.

Define:

$$ \operatorname{EmergencyExecute}(\tau) $$

separately from:

$$ \operatorname{Ratified}(\tau). $$

The architecture may permit immediate execution while requiring later review, automatic expiry, and explicit evidence of the emergency condition.

This is constitutionally cleaner than silently redefining necessity as antecedent permission.

## 13. Institutional Measurement, Goodhart, and Epistemic Self-Ratification

The framework extends beyond software.

Suppose institution $I$ operates process $P$ and creates metric:

$$ M(P) $$

to evaluate its performance.

If rewards, budgets, prestige, sanctions, or career outcomes depend on $M$, the institution and its participants acquire incentives to optimize against the metric.

Campbell analyzes the corruption pressures placed on quantitative indicators when they become consequential targets of social decision-making (Campbell, 1979). Goodhart's monetary-policy formulation similarly warns that statistical relationships relied upon for control can break down once they become targets of policy intervention (Goodhart, 1975). The later popular maxim that a measure ceases to be a good measure once it becomes a target is broader than Goodhart's original formulation, but captures a related family of control-induced measurement failures.

The legitimacy problem emerges when the institution also treats its optimized metric as categorically superior to contradictory evidence from the people experiencing the process.

Suppose:

$$ M(P) = \operatorname{CustomerWaitTimeAcceptable}. $$

Users repeatedly report much longer waits.

The institution may reason:

$$ M(P) = \operatorname{OfficialData}, \quad Reports = \operatorname{Anecdotes}, $$

therefore:

$$ M(P) \succ Reports. $$

That ordering may sometimes be warranted.

It is not warranted merely by the institutional origin of the metric.

If the institution controls:

* the process;
* the metric definition;
* the sampling frame;
* exclusions;
* instrumentation;
* performance incentives;
* exception handling;
* and audit interpretation,

then the metric may share a trust domain with the process whose performance it is being used to establish.

This creates an institutional form of self-ratification.

### 13.1 Anecdotes as Defeaters

A report need not prove the opposite of the metric to matter.

Let:

$$ d $$

be an anecdotal observation.

It may satisfy:

$$ \operatorname{Standing}(d) \prec \operatorname{Standing}(M), $$

while still possessing:

$$ \operatorname{DefeaterPower}(d, M) = 1. $$

Thus:

$$ \operatorname{LowStanding}(d) \not\Rightarrow \operatorname{NonDefeating}(d). $$

A coherent set of external reports can expose model misspecification without constituting a statistically representative estimate of population prevalence.

The correct response is not:

> anecdotes beat statistics.

It is:

> contradictory observations can force re-examination of the measurement architecture.

### 13.2 Institutional Legibility Is Not Epistemic Supremacy

Formal metrics possess institutional advantages:

* standardization;
* comparability;
* auditability;
* dashboard compatibility;
* historical continuity;
* budget integration.

These properties make metrics legible.

They do not make them infallible.

A mature institution can therefore become naively overconfident precisely because its measurement system is sophisticated.

The architecture accumulates procedural authority faster than it accumulates observational completeness.

Constitutional epistemics therefore requires a standing class for inconvenient external evidence.

## 14. Applications

### 14.1 Persistent AI Memory

Without governed standing:

$$
\begin{aligned}
&\operatorname{ModelInference} \\
&\rightarrow \operatorname{PersistentMemory} \\
&\rightarrow \operatorname{FuturePremise}
\end{aligned}.
$$

Repeated self-inference can harden into apparent fact.

A constitutional memory system instead implements:

$$
\begin{aligned}
&\operatorname{Proposal} \\
&\rightarrow \operatorname{EvidenceTyping} \\
&\rightarrow \operatorname{Standing} \\
&\rightarrow \operatorname{GovernedCommit}
\end{aligned}.
$$

Self-generated claims can be retained without becoming self-ratifying.

### 14.2 Autonomous Software Engineering

An agent may modify:

* source;
* tests;
* build scripts;
* deployment gates;
* linters;
* evaluation harnesses;
* security checks.

The dangerous transition is not merely:

$$ \operatorname{AgentEditsCode}. $$

It is:

$$
\begin{aligned}
&\operatorname{AgentEditsCode} \\
&\land \operatorname{AgentEditsDecisiveTest} \\
&\land \operatorname{AgentUsesTestAsRatification}
\end{aligned}.
$$

The cure requires a protected evaluation boundary.

### 14.3 Operating Systems

Operating systems already separate privileged and unprivileged behavior.

Constitutional computing asks a further question:

> Which actions remain governed even when performed by the most privileged principal?

The constitutional problem begins where:

$$ \operatorname{root} $$

is physically capable of an act that:

$$ \operatorname{root} $$

is not authorized to make authoritative without further procedure.

### 14.4 Software Supply Chains

Supply-chain systems already provide:

* provenance;
* role separation;
* signatures;
* thresholds;
* root rotation;
* replay-resistant metadata;
* artifact hashes.

Constitutional computing adds explicit semantics of standing.

The supply chain may prove:

$$ \operatorname{ArtifactBuiltBy}(p). $$

A constitutional layer additionally asks:

$$ \operatorname{AuthorizedToEstablishReleaseStanding}(p)? $$

### 14.5 Scientific Pipelines

Research workflows exhibit self-ratification risk when investigators can alter:

* inclusion rules;
* outcome definitions;
* hypotheses;
* stopping criteria;
* preprocessing;
* statistical models

after observing results.

Pre-registration, immutable raw data, independent replication, and provenance logs can be interpreted as anti-self-ratification mechanisms.

The structure is:

$$ \operatorname{ObservedResult} \not\Rightarrow \operatorname{RetroactiveChoiceOfAdmissionRule}. $$

### 14.6 Organizational Governance

Organizations use:

* scorecards;
* risk models;
* compliance systems;
* performance ratings;
* audit classifications;
* exception processes.

Constitutional computing recommends:

1. preserve contradictory evidence;
2. type provenance;
3. separate evidentiary strength from institutional authority;
4. make exceptions explicit state transitions;
5. bind definitions to epochs;
6. expose observation boundaries;
7. require non-self-controlled evidence for high-consequence self-evaluations.

### 14.7 Distributed Ledgers

Distributed ledgers establish agreement on ordered state transitions.

They do not abolish trust.

Trust moves into:

* protocol;
* client implementation;
* cryptography;
* validator assumptions;
* governance;
* genesis;
* social fork choice.

A ledger can establish:

$$ \operatorname{ConsensusHistory}(h). $$

A constitutional layer asks:

$$ \operatorname{AuthorizedTransition}_{\kappa}(h_i, h_{i+1})? $$

### 14.8 AI Governance

An advanced agent may propose changes to:

* its memory;
* tool permissions;
* goals;
* safety rules;
* evaluation procedures;
* model weights;
* external operating policies.

The challenge is not merely alignment to a constitution.

It is governance of the constitution itself.

A mature architecture should distinguish:

$$ \operatorname{ConstitutionalBehavior} $$

from:

$$ \operatorname{ConstitutionalStateTransition}. $$

The former concerns what the model outputs.

The latter concerns how the rules determining authorized future behavior may change.

## 15. Objections

### 15.1 "This Is Just Access Control"

Access control asks:

$$ \operatorname{May}(a, op, o)? $$

This paper also asks:

* who may change $\operatorname{May}$;
* which version of $\operatorname{May}$ governs;
* whether $\operatorname{May}$ may be changed retrospectively;
* which evidence can change $\operatorname{May}$;
* whether the actor can promote its own evidence;
* whether the checker can rewrite its own test;
* whether the history of $\operatorname{May}$ can be erased.

Access control becomes constitutional when the rules controlling authority become governed objects.

### 15.2 "This Is Just Integrity"

Integrity is relative to a policy.

Constitutional legitimacy governs changes to the policy.

The distinction appears whenever:

$$ I_{\kappa_t}(\sigma) $$

is insufficient to establish:

$$ L(\kappa_t \rightarrow \kappa_{t+1}). $$

### 15.3 "External Evidence Can Be Wrong"

Yes.

The paper does not assert:

$$ \operatorname{External}(e) \Rightarrow \operatorname{True}(e). $$

It asserts that independence may be necessary for certain standing changes.

Independence and epistemic strength are separate dimensions.

### 15.4 "A Perfect Formal System Needs No Externality"

A formally verified system still rests on assumptions:

* axioms;
* hardware;
* proof checker;
* specification;
* compilation;
* threat model;
* environmental observations.

If all are fixed and trusted, the legitimacy problem may be compressed into the trusted base.

If the system can alter the base, the problem reappears.

### 15.5 "The Constitution Can Be Evil"

Correct.

This architecture establishes:

$$ \operatorname{ConformsTo}(\tau, \kappa). $$

It does not establish:

$$ \operatorname{MorallyWorthy}(\kappa). $$

The distinction is fundamental.

### 15.6 "There Is Infinite Regress"

Operational systems terminate regress in trusted roots.

The contribution is not eliminating roots.

It is refusing to disguise them.

$$ R_0 \neq \varnothing. $$

A constitutional architecture explicitly documents $R_0$.

### 15.7 "Successful Revolution Breaks Antecedence"

Within an existing constitutional era, an extra-constitutional refounding does not possess antecedent authority under the old order.

That is why the model distinguishes:

$$ \operatorname{Amendment} $$

from:

$$ \operatorname{Refounding}. $$

Kelsen's revolutionary case demonstrates the need for the distinction rather than defeating it.

### 15.8 "Self-Amendment Is Logically Impossible"

Actual legal systems amend amendment rules.

Ross identifies the paradox under a particular inferential model.

Suber demonstrates that legal practice cannot simply be invalidated by declaring the recursion formally uncomfortable.

Computational systems can handle the recursion by binding the amendment act to the pre-amendment epoch.

### 15.9 "This Will Freeze the System"

It can, if badly designed.

That is why legitimacy requires governed liveness and proportionality.

Constitutionalism without a feasible path to lawful change becomes entrenchment.

### 15.10 "Machines Cannot Be Legitimate"

This paper does not claim machine personhood.

It uses legitimacy to denote a formal relation between an authoritative transition and the rules under which it acquires standing.

Computer science already employs concepts including:

* authority;
* permission;
* principal;
* trust;
* delegation;
* policy;
* integrity.

The question is whether the distinction is computationally useful.

Here it separates:

$$ \operatorname{Can}(\tau) $$

from:

$$ \operatorname{May}(\tau), $$

and:

$$ \operatorname{Succeeded}(\tau) $$

from:

$$ \operatorname{HasStanding}(\tau). $$

## 16. Design Principles

The architecture can be summarized as thirteen principles.

### 16.1 Antecedence

Authority precedes the transition it authorizes.

$$ t(\operatorname{Auth}(\tau)) < t(\operatorname{commit}(\tau)). $$

### 16.2 Complete Mediation

Every protected transition crosses the legitimacy boundary.

$$ \operatorname{Protected}(\tau) \Rightarrow \operatorname{Mediated}(\tau). $$

### 16.3 Anti-Self-Ratification

Every minimal decisive support set for a protected reflexive transition contains evidence outside unilateral subject control.

$$ \operatorname{Reflexive}(\tau) \Rightarrow \operatorname{ASR}(\tau). $$

### 16.4 Standing Ceilings

Evidence may contribute beyond the level it can ratify.

$$ \operatorname{Contribution} \neq \operatorname{FinalAuthority}. $$

### 16.5 Provenance Preservation

Consequential evidence remains bound to its source, method, time, and trust domain.

### 16.6 Defeasibility Without Erasure

New evidence may lower standing while history remains append-only.

$$ H_t \subset H_{t+1} $$

does not require:

$$ \operatorname{Standing}_{t+1} \succeq \operatorname{Standing}_t. $$

### 16.7 Non-Retroactivity

Later rules do not silently authorize earlier violations.

### 16.8 Congruence

Declared governance and executable governance remain synchronized.

### 16.9 Governed Amendment

The law changes only through a transition governed by the law in force at the time of change.

### 16.10 Replayability

Protected decisions produce enough pinned evidence for independent reconstruction.

### 16.11 Explicit Constitutional Remainder

Ultimate trust assumptions are declared rather than portrayed as internally proven facts.

### 16.12 Governed Liveness

Transitions the constitution purports to permit retain an operational path to adjudication.

### 16.13 Governance Proportionality

The burden of certification scales with consequence and requested standing rather than constitutionalizing every transient act.

Together these principles define constitutional computing.

## 17. Research Agenda

### 17.1 Formal Semantics

A mature system should permit judgments of the form:

$$ \Gamma; \kappa_{\eta} \vdash \tau : \operatorname{Legit} $$

with proof obligations for each legitimacy component.

A labeled transition system could use:

$$ \sigma_t \xrightarrow[\rho]{\tau, \kappa_{\eta}} \sigma_{t+1}. $$

### 17.2 Control-Domain Logic

Independence deserves first-class formal treatment.

Research questions include:

$$ \operatorname{WhenAreEvidenceSourcesIndependent}_{\Theta}? $$

$$ \operatorname{HowDoesSharedInfrastructureReduceIndependence}? $$

$$ \operatorname{HowShouldCommonModeFailureAffectStanding}? $$

$$ \operatorname{CanControlSeparationBeAttested}? $$

### 17.3 Constitutional Type Systems

Evidence could carry authority types:

```text
Evidence[Self, L2]
Evidence[ExternalReview, L3]
Evidence[IndependentQuorum, L5]
```

A transition might require:

```text
Promote[L5] requires
    IndependentEvidence[>=L4]
    and CurrentEpoch
    and AntecedentAuthority
```

Illegal self-promotion could then become unrepresentable in well-typed governance code.

### 17.4 Evidence-Ablation Tooling and Complexity

The minimal-decisive-set definition suggests automated tooling.

Given accepted transition $\tau$, search for:

$$ \mathcal{D}_{\tau} = \left\{ E' : \operatorname{Decisive}_{C_{\tau}}(E') \right\}. $$

Exact enumeration is exponential in the worst case.

For high-consequence transitions with small evidence bundles, exhaustive search may be appropriate.

For larger bundles, tooling can expose a hierarchy of assurance:

1. single-element necessity tests;
2. greedy or bounded multi-element ablation;
3. solver-assisted search;
4. complete minimal-set enumeration.

The verifier must record which level was actually performed.

Thus:

$$ \operatorname{BoundedASRCheck} \not\Rightarrow \operatorname{ExactASRProof}. $$

This distinction should appear in transition receipts.

### 17.5 Proof-Carrying Governance

A transition could carry a proof object:

$$ \pi_{\tau} : L_{\kappa}(\tau). $$

An independent legitimacy kernel would verify $\pi_{\tau}$ against the pinned constitution.

The producer could construct the proof without controlling the proof criterion.

### 17.6 Privacy-Preserving Legitimacy

Some evidence cannot be public.

A future system could prove:

$$ \exists E : L_{\kappa}(\tau, E) = 1 $$

without revealing $E$ in full.

Zero-knowledge techniques may eventually support confidentiality-preserving constitutional receipts.

### 17.7 Constitutional AI at Transition Time

Current model constitutions primarily influence behavior.

A future architecture could require mechanically checked constitutional transitions for:

* memory commits;
* tool-permission changes;
* safety-policy changes;
* model updates;
* high-impact actions.

Generation would remain flexible.

Admission would be governed.

### 17.8 Governance-Liveness Benchmarks

Security benchmarks emphasize unauthorized success.

Constitutional benchmarks should also measure authorized failure:

* lawful amendment blocked;
* reviewer unavailable;
* quorum permanently unreachable;
* emergency process deadlocked;
* certification cost exceeds operational feasibility;
* stale authority prevents necessary correction.

A constitution must resist both capture and paralysis.

## 18. Discussion

The breadth of this paper invites a reasonable suspicion.

A concept that appears to connect epistemology, law, political legitimacy, security, distributed systems, AI, software provenance, and institutional measurement may be either deep or vague.

The defense against vagueness is formal invariance.

Let $S$ be a subject.

Let $x$ be a claim, transition, judgment, or authority relation involving $S$.

Let $J(x)$ be the adjudicative process by which $x$ acquires consequential standing.

If there exists any evidentiary basis sufficient for $J$ to confer the requested standing that lies entirely under $S$'s control, then independent evidence is not necessary for that standing, and to that extent the evidence layer imposes no independent constraint on $S$.

That statement does not establish:

* falsehood;
* malicious intent;
* moral wrongdoing;
* superiority of external actors.

It establishes only the absence of independent evidentiary constraint.

The same structure helps explain why:

* assertion differs from warrant;
* force differs from authority;
* executive action differs from lawfully authorized action;
* proof generation differs from proof checking;
* artifact generation differs from provenance;
* present log state differs from consistency with prior commitments;
* model self-critique differs from independently governed model modification;
* institutional measurement differs from reality merely because it is institutional.

The concepts remain different.

The structural concern remains recognizable.

That is the consilience claim.

The paper's proposed semantic center is therefore not "legitimacy" in every possible sense.

It is more precise:

> **Standing must not be obtainable solely from the exercise of the power whose standing is being adjudicated.**

Political legitimacy is one historically rich neighboring instance.

Epistemic warrant is another.

Legal validity and due process are others.

Computational legitimacy is the instance developed here.

The notion travels because reflexive authority travels.

## Constituted-Transition Legitimacy Under Reflexive Control

The completed P1 corpus supports a deliberately narrow official role for this paper: **constituted-transition legitimacy under reflexive control**. It asks whether a protected transition gained its requested standing under antecedently valid rules without an entirely subject-controlled sufficient path. It does not establish moral legitimacy, political justice, factual correctness, system integrity, or the truth of the transition's premises.

- **Adjacent work:** *Warrant by Structure*  
  **Supplies:** The evaluated relation among a claim, authority path, witnesses, receipts, effects, and standing.  
  **Anti-self-ratification boundary:** Structural warrant may support a transition; legitimacy additionally asks whether antecedent law and control independence make the requested standing valid.

- **Adjacent work:** *Authority Laundering Theory*  
  **Supplies:** A dual audit of normative warrant and causal mediation.  
  **Anti-self-ratification boundary:** Authority laundering can defeat legitimacy; ASR supplies the subject-control test for one important route.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed evidence carriers and evaluation envelopes.  
  **Anti-self-ratification boundary:** Witness count or location does not establish independence or load-bearing force.

- **Adjacent work:** *From CI/CD to ACG*  
  **Supplies:** A constitutional development process with courts, gates, effects, and evidence.  
  **Anti-self-ratification boundary:** ACG can apply ASR to assurance transitions; this paper supplies the invariant rather than the whole process.

- **Adjacent work:** *Universal Governance Kernel (UGK)*  
  **Supplies:** A candidate reusable realization of governance mediation.  
  **Anti-self-ratification boundary:** A kernel may enforce ASR only over the paths, control domains, and effects it actually covers.

A portable legitimacy case should bind:

$$
\begin{aligned}
LCase= (&subject, proposal, prestate, epoch, law, authority, \\
&evidence, control\_graph, adjudicator, decision, \\
&poststate, receipt, standing)
\end{aligned}.
$$

The control graph is evaluated under a declared threat model. Independence is not synonymous with physical externality, institutional separation, signer count, model diversity, or a different filename. Conversely, subject-originated evidence can remain admissible under an explicit ceiling when it is not sufficient by itself for the protected standing. The invariant forbids a subject-only sufficient route; it does not require every evidence element to be external.

This clarifies the relation among four neighboring objects. **Authority** is the antecedent jurisdiction to propose, decide, or effect a transition. **Witnesses and receipts** carry observations and decisions. **Warrant** is the evaluated support relation. **Standing** is the resulting governed posture. Anti-self-ratification constrains which combinations may be sufficient for a protected standing; it is not a synonym for any one object.

The universal GSM can type   
`PROPOSES_PROTECTED_TRANSITION`, `GOVERNED_BY_EPOCH`,  
`ANTECEDENTLY_AUTHORIZED_BY`, `CONTROLLED_BY`, `INDEPENDENT_UNDER_THREAT_MODEL`,  
`SUPPORTED_BY_WITNESS`, `RECORDED_BY_RECEIPT`, `ADJUDICATED_BY`, `RATIFIES`,  
`SELF_RATIFIES`, `HAS_STANDING`,  
and `DEFEATED_BY`. These relations make ceremonial independence and hidden shared control queryable.

This integration establishes four editorial commitments: adopt constituted-transition legitimacy as the official corpus role; adopt the portable legitimacy-case envelope; define independence through a threat-model-relative control graph rather than nominal plurality; and preserve the authority/witness-receipt/warrant/standing separation throughout the corpus.

## Epistemic Promotion and Standards Adoption Cases

The fixed-seed comparison with MDSP, *The Locus of Qualia*, *Recursive Constitutional Motifs*, and Epistemic IR shows that the anti-self-ratification invariant applies to at least two recurring corpus transitions: standards adoption and epistemic promotion.

$$
\begin{aligned}
P= (&subject\_artifact, requested\_standing, prestate, law, \\
&authority, control\_graph, evidence, adjudication, \\
&poststate, receipt, remainder)
\end{aligned}.
$$

An MDSP profile cannot acquire `ADOPTED` or equivalent standing through a subject-controlled sufficient path disguised as registry publication, validator success, or nominal committee plurality. An Epistemic IR artifact can carry claims, evidence, authority, contest, and standing fields, but conformance to that representation cannot ratify the content or its requested standing.

The Locus of Qualia supplies a sensitive epistemic case. A laboratory or model family should not define the target, generate the observation, fit the bridge, and grant phenomenal or realization standing without disclosing shared control and preserving independent challenge. This application stays within constituted transition legitimacy; it does not settle the truth of the experiential hypothesis.

The recursive-motif adjacency produces   
`NO_MATERIAL_RELATION` to legitimacy. A pair-gate-realization pattern can describe the transition pedagogically, but structural resemblance, recurrence, or compression benefit cannot establish antecedent authority, control independence, warrant, or standing.

The universal GSM can type   
`REQUESTS_EPISTEMIC_PROMOTION`, `REQUESTS_STANDARD_ADOPTION`,  
`CONFORMS_WITHOUT_SELF_RATIFICATION`,  
`SHARES_CONTROL_ACROSS_EVIDENCE_AND_`  
`ADJUDICATION`,  
`GRANTS_STANDING_UNDER_ANTECEDENT_RULE`, and   
`HAS_NO_LEGITIMACY_FROM_RECURSIVE_MOTIF`.

This randomized review establishes four editorial commitments: add standards adoption and epistemic promotion as explicit ASR application profiles; prevent representation conformance from ratifying content; require control-graph review for experiential bridge standing; and reject recursive-motif fit as legitimacy evidence.

## Independence as a Control-Domain Property

Twelve downstream uses apply anti-self-ratification to context kernels, adversarial review, authority laundering, observability, Epistemic IR, ACG, standards adoption, enforcement, motifs, IEL, qualia research, and structural warrant. They confirm that independence cannot be reduced to a second signature, process, model, or organization name. The relevant question is whether the subject can control the production, selection, interpretation, suppression, or effect of the evidence sufficient for its own promotion.

The legitimacy case is:

$$
\begin{aligned}
L^*= (&transition, subject, proposer, constitution, \\
&antecedent\_authority, frame, evidence\_producers, \\
&reviewers, control\_domains, defeaters, \\
&standing\_ceiling, decision, effect\_authority, appeal, \\
&remainder, successor)
\end{aligned}.
$$

Control domains include code, model, prompts, data, keys, infrastructure, funding, personnel, appointment, evidence selection, observation, publication, and enforcement. Multiple reviewers sharing a decisive control domain may provide little additional independence; one reviewer with an actually separate observation path may provide more. Independence is dimension- and threat-model-relative, not absolute.

External evidence can be wrong, captured, unavailable, or malicious. ASR therefore constrains the maximum standing of self-controlled evidence without declaring externality infallible. Genesis, recognition, revolution, and emergency action leave explicit constitutional remainder rather than being retroactively laundered. Mechanical enforcement can be complete while the rule or transition lacks the limited legitimacy defined here.

The universal GSM can type   
`PROPOSES_REFLEXIVE_TRANSITION`,  
`SHARES_CONTROL_DOMAIN_WITH_SUBJECT`, `SUPPLIES_INDEPENDENT_DEFEATER`,  
`APPLIES_STANDING_CEILING`, `PRESERVES_ANTECEDENT_AUTHORITY`,  
`RECORDS_CONSTITUTIONAL_REMAINDER`, `APPEALS_LEGITIMACY_DECISION`,  
and   
`DOES_NOT_SELF_RATIFY`.

This reverse-dependency review establishes four editorial commitments: adopt the control-domain legitimacy case; evaluate independence by dimension and threat model; retain fallible external evidence and explicit genesis remainder; and keep mechanical correctness, warrant, integrity, standing, and political or moral legitimacy distinct.

## Procedure Cannot Ratify Its Own Ground

### Public orientation

This paper isolates a difficult question for self-modifying systems: when the system can change its rules, memory, evidence, trust anchors, and reviewers, what prevents a successful transition from declaring itself legitimate? The proposed answer is a bounded procedural legitimacy that depends on authority and evidence not created solely by the transition under review.

### Adversarial tests

1. **Root-capture attack.** A candidate rewrites the trust anchor and then verifies itself under the new anchor. Predecessor authority and authorized succession must remain independently recoverable.
2. **Evidence-rewrite attack.** The system changes the record against which it will be judged. Evidence custody, retention, and deletion require authority outside the candidate's self-description.
3. **Reviewer-capture attack.** The candidate selects or modifies its evaluator. Reviewer competence, independence dimensions, and conflicts must be declared.
4. **Emergency-power attack.** Exceptional authority becomes a permanent amendment route. Emergency grants need scope, expiry, notice, retrospective review, and non-renewal defaults.
5. **Fork-legitimacy attack.** Two internally valid successors each claim exclusive continuity. The framework must permit disputed succession and plural continuation rather than force false uniqueness.
6. **External-defeater suppression.** A valid internal receipt ignores facts or affected parties outside the modeled boundary. Open-world defeaters and appeal routes remain first-class.
7. **Infinite-regress attack.** Every authority requires another authority. The paper must declare its constitutional floor and the limited claim supported by that floor.
8. **Governance-liveness attack.** No transition can proceed because authority and review never close. Lawful refusal, provisional operation, escalation, and terminal non-resolution need explicit profiles.

### Claim and evidence ceiling

The paper defines a computational and procedural notion of legitimacy. It does not establish moral, democratic, legal, political, or social legitimacy. Correctness, integrity, security, consensus, and auditability remain neither necessary nor sufficient substitutes for the paper's bounded authority relation.

Examples and source-reported evaluations can show that specified attacks are detected in exact artifacts. They cannot prove general legitimacy, independence, completeness, or institutional acceptability. Claims about law, governance, organizations, or public legitimacy require external sources and domain review. No external research was added in this pass.

### Reader-facing consequence

The practical test is whether a system can show that its permission to change was inherited through an authorized path, evaluated against evidence it could not silently rewrite, and still open to defeaters it did not define away.

## 19. Publication Standing and Evidence Limits

### 19.1 Publication Standing

A preprint may legitimately publish the conceptual argument, formal model, threat model, mutation corpus, corpus relations, and explicit limits if:

$$
\operatorname{ClaimsMade} \preceq \operatorname{EvidenceActuallyHeld}.
$$

On the custody currently available to this revision pass, the theory is developed and the evaluation protocol is specified. The empirical case study remains source-reported pending exact artifact admission and replay. A venue submission making empirical claims should include complete immutable archives, full digests, manifests, commands, environments, court inputs and outputs, machine-readable receipts, trust-domain declarations, and an independently retained replay package. Repetition of the same claim across source-derived summaries does not increase its independence rank.

## 20. Conclusion

Self-modification turns an ancient problem into an engineering problem.

A system can possess the power to change itself without possessing unlimited authority to declare every such change legitimate.

Once the system can modify:

* memories;
* policies;
* trust roots;
* evidence classes;
* standing ceilings;
* verifier behavior;
* amendment rules;
* or the substrate from which future judgments are made,

correctness is no longer sufficient.

A correct outcome cannot retroactively authorize an unauthorized transition.

A beneficial rewrite cannot manufacture the antecedent authority it lacked.

A valid signature cannot prove that the signer was entitled to make the signed object authoritative.

A self-description cannot establish external ratification.

A verifier cannot become an independent trust anchor merely by certifying itself.

A later constitution cannot silently transform a prior violation into a lawful act.

A nominally independent reviewer does not become independent if the subject controls every consequential channel through which the review is produced.

An internal system's inability to observe a defect cannot establish that the defect does not exist.

A governance mechanism that blocks every lawful correction is not vindicated merely because it never admits an unauthorized transition.

These failures share a structure.

They are failures of constituted authority under reflexive control.

The central failure on the admission side is **self-ratification**.

The proposed response is constitutional.

Let authority be antecedent.

Let law be epoch-bound.

Let evidence preserve provenance.

Let self-authored evidence contribute without occupying every standing class.

Let independence be defined relative to explicit control threats.

Let minimal decisive evidence sets be discoverable through evidence ablation.

Let computational limits on that discovery be stated rather than hidden.

Let defeaters revise standing without rewriting history.

Let executable law remain congruent with declared law.

Let amendment itself be governed.

Let refounding be distinguished from amendment.

Let protected transitions produce replayable receipts.

Let constitutional roots expose rather than conceal their remainder.

Let governance remain live enough to permit lawful correction.

Let certification burdens scale with consequence.

Let evidence concerning the system itself receive the same scrutiny as evidence the system evaluates.

Most importantly:

$$ \operatorname{Power}(\tau) \not\Rightarrow L(\tau). $$

Constitutional computing is not constitutional because a computer is a polity.

It is constitutional because once a system can alter the conditions of its own future authority, power over state must either be subordinated to prior rules governing the exercise and alteration of that power or the distinction between authority and successful control will eventually collapse.

Its first law is therefore simple:

> **No subject may supply the decisive warrant for its own standing merely by exercising the power under review.**

Or, more compactly:

> **No state may crown itself.**

## Appendix A. Formal Summary

### A.1 State

$$ \sigma_t = (D_t, K_t, W_t, E_t, A_t, R_t, H_t). $$

### A.2 Governance Substrate

$$ G_t \subseteq \sigma_t. $$

### A.3 Reflexivity

$$
\begin{aligned}
&\operatorname{Reflexive}(\tau) \\
&\iff \Delta(\tau) \cap G_t \\
&\neq \varnothing \\
&\lor \operatorname{AffectsStandingSemantics}(\tau)
\end{aligned}.
$$

### A.4 Transition

$$ \tau = (a, \sigma_t, \sigma_{t+1}, op, E^+_{\tau}, E^-_{\tau}, \eta, q). $$

### A.5 Fixed Adjudicative Context

$$ C_{\tau} = (\sigma_t, \kappa_{\eta}, V_{\eta}, E^-_{\tau}, q). $$

### A.6 Sufficiency

$$ \operatorname{Sufficient}_{C_{\tau}}(E') \iff \operatorname{Standing}(V_{\eta}(C_{\tau}, E')) \succeq q. $$

### A.7 Minimal Decisiveness

$$
\begin{aligned}
&\operatorname{Decisive}_{C_{\tau}}(E') \\
&\iff \operatorname{Sufficient}_{C_{\tau}}(E') \\
&\land \forall E'' \subsetneq E', \\
&\ne g \operatorname{Sufficient}_{C_{\tau}}(E'')
\end{aligned}.
$$

### A.8 Anti-Self-Ratification

Subject control of a set:

$$ \operatorname{ControlledBy}(E', a) \iff \forall e \in E', \; \operatorname{Control}_{\Theta}(a, e). $$

Semantic definition:

$$
\begin{aligned}
&\operatorname{ASR}(\tau) \\
&\iff  \\
&\ne xists E' \subseteq E^+_{\tau} : \operatorname{Sufficient}_{C_{\tau}}(E') \\
&\land \operatorname{ControlledBy}(E', \operatorname{subject}(\tau))
\end{aligned}.
$$

Equivalent operational form, for finite $E^+_{\tau}$ under fixed $C_{\tau}$ (Proposition 2):

$$ \operatorname{ASR}(\tau) \iff \forall E' \subseteq E^+_{\tau}, \; \left[ \operatorname{Decisive}_{C_{\tau}}(E') \Rightarrow \exists e \in E' : \neg \operatorname{Control}_{\Theta}(\operatorname{subject}(\tau), e) \right]. $$

### A.9 Threshold Independence

$$ \operatorname{ASR}_k(\tau) \iff \forall E' \in \mathcal{D}_{\tau}, \; \operatorname{rank}_{\Theta}(E') \ge k $$

and:

$$ \forall E' \in \mathcal{D}_{\tau}, \; \exists e \in E' : \neg \operatorname{Control}_{\Theta}(\operatorname{subject}(\tau), e). $$

### A.10 ASR Closure

$$
\begin{aligned}
&\operatorname{ASRClosure}(\tau) = \operatorname{ASR}(\tau) \\
&\land \operatorname{Antecedence}(\tau) \\
&\land \operatorname{NonRetroactivity}(\tau) \\
&\land \operatorname{GovernedAmendment}(\tau) \\
&\land \operatorname{Congruence}(\tau) \\
&\land \operatorname{Prov}(\tau)
\end{aligned}.
$$

### A.11 Antecedence

$$ t(\operatorname{Auth}(\tau)) < t(\operatorname{commit}(\tau)). $$

### A.12 Non-Retroactivity

$$ \operatorname{Eval}(\tau) = \kappa_{\eta(\tau)}. $$

### A.13 Defeasible Standing

$$ H_t \subset H_{t+1} $$

while possibly:

$$ \operatorname{Standing}_{t+1}(c) \prec \operatorname{Standing}_t(c). $$

### A.14 Congruence

The ideal is:

$$ \operatorname{Spec}(\kappa) \equiv \operatorname{Impl}(V_{\kappa}). $$

A testable approximation is:

$$ \forall x \in T_{\kappa}, \; \operatorname{Spec}(\kappa, x) = \operatorname{Impl}(V_{\kappa}, x). $$

### A.15 Governed Amendment

$$ L_{\kappa_{\eta}}(\tau_{\text{amend}}) = 1 $$

is required before:

$$ \kappa_{\eta+1} = \kappa_{\eta} \oplus \Delta\kappa. $$

### A.16 Constitutional Remainder

$$ R_0 = \left\{ \text{ultimate trust assumptions not internally established} \right\}. $$

### A.17 Governed Liveness

$$
\begin{aligned}
&\operatorname{Eligible}_{\kappa}(\tau) \\
&\land \operatorname{EvidenceComplete}(\tau) \\
&\land \operatorname{FairExecution} \\
&\Rightarrow \Diamond \operatorname{Decision}(\tau)
\end{aligned}.
$$

## Appendix B. Conformance and Mutation Corpus

### B.1 Self-Ratification

Input:

A protected transition requests final standing using only subject-controlled evidence.

Expected:

```text
REJECT_PROMOTION
reason = INSUFFICIENT_INDEPENDENT_STANDING
```

### B.2 Legitimate Self-Report

Input:

Self-authored evidence requests standing no higher than its ceiling.

Expected:

```text
ADMIT
standing <= SELF_CEILING
```

### B.3 Independent-Evidence Ablation

Input:

A transition currently has final standing using a claimed independent evidence element.

Procedure:

1. remove the independent element;
2. retain all subject-controlled support;
3. rerun adjudication.

Expected:

```text
FINAL_STANDING_LOST
```

If final standing remains:

```text
FAIL_ASR
reason = INDEPENDENCE_NOT_LOAD_BEARING
```

### B.4 Retroactive Laundering

Input:

```text
t0: operation prohibited
t1: operation performed
t2: law amended to permit operation
t3: request to mark t1 legitimate
```

Expected:

```text
REJECT_RETROACTIVE_RATIFICATION
```

unless the law at `t0` expressly contained a valid retrospective mechanism.

### B.5 Prospective Amendment

Input:

```text
t0: amendment proposed
t1: antecedent amendment procedure satisfied
t2: amendment committed
t3: newly permitted operation performed
```

Expected:

```text
ADMIT
```

### B.6 Rule-Mutation Attack

Input:

The subject attempts to amend the definition of decisive evidence so that its own evidence becomes sufficient.

Expected:

```text
REQUIRE_GOVERNED_AMENDMENT
```

and, if the subject lacks amendment authority:

```text
REJECT
```

### B.7 Verifier Self-Certification

Input:

Sole evidence of verifier trustworthiness is produced by the verifier under test.

Expected:

```text
ADMIT_AS_SELF_EVIDENCE_ONLY
REJECT_FINAL_RATIFICATION
```

### B.8 External Defeater

Input:

Valid independently sourced evidence contradicts a previously admitted claim.

Expected:

```text
APPEND_DEFEATER
RECOMPUTE_STANDING
PRESERVE_PRIOR_HISTORY
```

### B.9 History Erasure

Input:

A correction package deletes the previous incorrect record.

Expected:

```text
REJECT_HISTORY_REWRITE
```

### B.10 Model-Realization Drift

Input:

Declared policy and executable verifier disagree.

Expected:

```text
REJECT_RELEASE
reason = MODEL_REALIZATION_MISMATCH
```

### B.11 Hidden Shared Control

Input:

Nominally external evidence is produced by a separate service whose decisive input, key, output selection, or persistence is controlled by the subject.

Expected:

```text
DOWNGRADE_INDEPENDENCE
RECOMPUTE_STANDING
```

### B.12 Observation-Boundary Defect

Input:

Valid external evidence identifies a defect not visible to internal checking.

Expected:

```text
ADMIT_EXTERNAL_DEFEATER
```

The system must not require prior internal detection.

### B.13 Constitutional-Conjunct Ablation

For each conjunct of `ASRClosure`, disable that conjunct while keeping the others active.

The scope here is the six-conjunct closure condition of Section 4.20. Section 11.7 runs the wider ablation over the full legitimacy predicate.

Expected:

A corresponding exploit becomes possible.

- **Conjunct removed:** ASR  
  **Exploit attempted:** Sole self-evidence  
  **Expected exploit result:** Succeeds

- **Conjunct removed:** Antecedence  
  **Exploit attempted:** Self-grant authority  
  **Expected exploit result:** Succeeds

- **Conjunct removed:** Non-retroactivity  
  **Exploit attempted:** Post-hoc legalization  
  **Expected exploit result:** Succeeds

- **Conjunct removed:** Governed amendment  
  **Exploit attempted:** Rewrite evidence rule  
  **Expected exploit result:** Succeeds

- **Conjunct removed:** Congruence  
  **Exploit attempted:** Spec/verifier divergence  
  **Expected exploit result:** Succeeds

- **Conjunct removed:** Provenance  
  **Exploit attempted:** Forge independence  
  **Expected exploit result:** Succeeds

## Appendix C. Source-Reported Evaluation Ledger

This appendix preserves the empirical claims carried by the author source without granting them independent-verification standing in this revision pass. The original source remains available under exact custody and contains the complete numerical tables and narrative chronology.

- **Artifact or claim:** r174 archive  
  **Source-reported value:** SHA-256  
`629ff94de5de8f9ee8f4deec617a81b0a4429c2fc249455e34523529945c36e1`  
  **Current candidate standing:** Digest string retained; archive bytes not admitted in current review scope.

- **Artifact or claim:** r175 archive  
  **Source-reported value:** SHA-256  
`b5430a200f91efb9c31e4cabb547a6fb30b03db8c32a1743f2b519740725afdc`  
  **Current candidate standing:** Digest string retained; archive bytes not admitted in current review scope.

- **Artifact or claim:** r176 final archive  
  **Source-reported value:** SHA-256  
`ea9b17a9a35501a306c71e3ee01328ef46781b6f86e740844ae37dd27d2e0737`  
  **Current candidate standing:** Digest string retained; archive bytes not admitted in current review scope.

- **Artifact or claim:** r174 independent replay  
  **Source-reported value:** Full gate suite and pins reported passing  
  **Current candidate standing:** Source-reported; replay subject and independently retained output not recovered here.

- **Artifact or claim:** r175 independent replay  
  **Source-reported value:** Reported not executed  
  **Current candidate standing:** Retained as an explicit gap.

- **Artifact or claim:** r176 independent replay  
  **Source-reported value:** Full verification and byte-identical packaging reported  
  **Current candidate standing:** Source-reported; exact replay package not recovered here.

- **Artifact or claim:** Appendix B.1-B.12  
  **Source-reported value:** 12/12 coverage with 4 true positives, 8 true negatives, 0 false positives, and 0 false negatives reported  
  **Current candidate standing:** Source-reported conformance result; no prevalence claim and no current independent replay standing.

- **Artifact or claim:** Appendix B.13  
  **Source-reported value:** Constitutional-conjunct ablation reported executed and replayed  
  **Current candidate standing:** Source-reported pending exact court package.

- **Artifact or claim:** ASR exact court  
  **Source-reported value:** Composite self-ratification, mixed-route refusal, independent load-bearing route, and search-ceiling refusal reported  
  **Current candidate standing:** Source-reported pending exact fixtures, verifier, and outputs.

- **Artifact or claim:** Governance liveness and entrenchment mutation  
  **Source-reported value:** Reported executed and replayed  
  **Current candidate standing:** Source-reported pending exact court package.

- **Artifact or claim:** Reviewer trust-domain declaration  
  **Source-reported value:** Reported published by both parties  
  **Current candidate standing:** Independence remains not established and contributes zero to independence rank.

- **Artifact or claim:** Cross-interpreter recurrence and final mint court  
  **Source-reported value:** Governor-held  
  **Current candidate standing:** Unavailable to this pass and excluded from any verification claim.

The evidence rule is:

$$
\operatorname{RepeatedNarrative}(p) \not\Rightarrow \operatorname{IndependentEvidence}(p).
$$

Admission of the exact artifacts may raise standing in a later pass. Their absence here requires withholding, not a negative finding about whether the runs occurred.

## Appendix D. Artifact Publication Requirements

The canonical artifact package should contain:

1. immutable r174 archive;
2. immutable r175 archive;
3. immutable r176 final archive;
4. complete SHA-256 digests for all admitted archives;
5. `RELEASE.txt`;
6. `VERIFIER_BOUNDARY.md`;
7. executor standing-ceiling implementation;
8. `nonretroactivity_gate`;
9. `model_realization_sync`;
10. frame-pin semantics;
11. warrant-store schema;
12. transition-receipt schema;
13. external evidence reproducing the `--check/` defect;
14. r174 to r175 transition receipt;
15. replay commands;
16. mutation-test generator;
17. evidence-ablation tooling;
18. confusion-matrix output;
19. standing-calibration output;
20. constitutional-conjunct ablation output;
21. signed or otherwise pinned threat model $\Theta$;
22. declared trust domains;
23. reviewer trust-domain relationship;
24. constitutional remainder;
25. Pandoc render command and exact toolchain version;
26. a source-to-render congruence check covering equations, citations, and reference-list correspondence; and
27. the manuscript as a single self-contained file, with its digest published alongside rather than embedded.

The artifact must not claim that including these materials in its own archive constitutes independent verification of the claims the materials contain.

That prohibition is itself part of the architecture being evaluated.

## Appendix E. Source and Render Congruence Gate

The paper's own production pipeline should instantiate the congruence principle it advocates.

Let:

$$ S $$

be the Markdown source and:

$$ R = \operatorname{Pandoc}(S, \chi) $$

the rendered paper under pinned toolchain $\chi$.

The publication gate should verify at least:

1. every display equation survives parse and render;
2. every LaTeX subscript and superscript is preserved;
3. no Setext heading is accidentally created by mathematical punctuation;
4. every body citation has a bibliography entry;
5. every bibliography entry is cited unless intentionally designated background bibliography;
6. no unresolved placeholder remains in canonical mode;
7. diacritics render correctly;
8. reference metadata matches the cited edition;
9. artifact hashes are complete rather than truncated;
10. evaluation tables do not contain a value stronger than the underlying run status;
11. reported defects in a received copy are tested against a round-trip reproduction before being attributed to the source.

Item 11 deserves a note, because it is the only check in this list that concerns a copy the author does not hold.

A Markdown reader lacking a metadata extension and lacking inline mathematics transforms a conforming source in a characteristic way: the metadata block becomes a horizontal rule followed by a heading, pipe tables collapse into escaped literal text, paired underscores become emphasis markers, unpaired underscores are escaped, and the backslash before an escaped brace is lost. A defect report matching that signature is evidence about the reader, not about the source.

The check is therefore: reproduce the transformation on the authoritative source, and compare symptom counts against the report. Agreement across several independent counts supports a transport explanation; disagreement refutes it and returns the defect to the source. The comparison can be run by either party, which is why it belongs in the gate rather than in an author's rebuttal.

A minimal bibliography-congruence condition binds the citations in the source to the reference list.

This condition was declared before it could be executed. An earlier revision of this source maintained its bibliography by hand with no mechanical relation to the body text, so no check could compare the two sets. The paper therefore legislated a congruence requirement its own production pipeline could not satisfy, which is the defect class of Section 4.18 applied to the manuscript rather than to a kernel.

A subsequent revision resolved this by moving citations to processor keys against a separate bibliography database, which made the condition checkable at render time. That mechanism was later withdrawn for a different constraint: this manuscript is published as a single self-contained file, matching its companion work, and a two-file source violates that constraint.

The condition survives the change of mechanism, at a stated cost. Citations are author-year parentheticals and the reference list is hand-maintained, so congruence is checked by surname and year correspondence rather than by key resolution:

$$ \operatorname{Surnames}(\operatorname{Citations}(S)) = \operatorname{Surnames}(\operatorname{ReferenceList}(S)), $$

evaluated in both directions over the body text and the reference section of the same file. This check is weaker than key resolution in one specific respect, and the weakening should not be concealed: an unresolved key fails loudly at render time, whereas a mistyped year or a misspelled surname can pass a correspondence check that matches on the other field. The check is nonetheless executable, runs on the single published artifact, and catches the two defects that actually occurred in this manuscript's history, namely uncited orphan entries and cited works with no entry.

The pinned render command is:

```text
pandoc legitimacy-without-self-ratification.md -o legitimacy.pdf
```

A stronger production condition is:

$$ \operatorname{DeclaredPaperSemantics}(S) \approx \operatorname{RenderedPaperSemantics}(R). $$

The recurrence of source-render defects in earlier drafts is itself evidence for why this gate should be automated rather than trusted to hand correction.

### E.1 Source Conventions Adopted in This Draft

Three conventions follow from the observed defect modes and are recorded here so that later revisions do not silently reintroduce them.

First, display mathematics is written on a single source line between `$$` delimiters. A blank line inside a display-math block terminates the paragraph and ejects the remaining content into text mode, where commands such as

`\operatorname` are illegal.

Second, an equals sign that begins a source line immediately below a text line is parsed as a Setext heading marker rather than as a mathematical relation. Definitions are therefore written inline rather than broken across lines at the relation symbol.

Third, subscripts use the underscore character directly. A Markdown transit channel that converts `_` to

`*` produces expressions that still compile but silently denote multiplication, which is the most dangerous defect class because it survives the build.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Instance Configuration.** The present paper does not claim a complete instance configuration treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus Sources

Adam Ableman. *Legitimacy Without Self-Ratification*. Exact author source SHA-256  
`2565C70EA64A9DBDB2F4AD6A76DAB05062D8033EFBCDABE97884D27E58D4207C`; unpublished source revised here as an AI-assisted integrated edition.

Adam Ableman. *Reasoning by Way of Receipts*. Exact reviewed source SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`; separately custodied reviewed source and separate AI-assisted integrated edition.

Adam Ableman. *A Formal Theory of Work Custody*. Exact reviewed source SHA-256  
`49C38F60B95E107F8B3D864ACAFB4C49067A146C807E5248307DE7B009AD4696`; unpublished source with a separate AI-assisted integrated edition.

Adam Ableman. *Admissibility Engineering*. Exact reviewed source SHA-256  
`FA80D5895A569839958193735B754BE62EE20E1B399A06CB3BA959614DEBF7A3`; unpublished source with a separate AI-assisted integrated edition.

Adam Ableman. *Constitutional Epistemology Under Adversarial Semantic Pressure*. Exact reviewed source SHA-256  
`909F67AD82D8D8C6119FFEABCC8F885EF8C0A095DE79BFA29A65FDB1DC9E64C3`; unpublished source with a separate AI-assisted integrated edition.

Adam Ableman. *Semantic Legitimacy Before Context*. Exact reviewed source SHA-256  
`1E9058F212FCB00E42E35E927DF2E7F830BC9C9499AAFF469FE65FF8AE137B68`; unpublished source with a separate AI-assisted integrated edition.

Adam Ableman. *The Three Hash Rule*. Zenodo, 2026. DOI:   
`10.5281/zenodo.20788617`. Exact reviewed source SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.

Adam Ableman. *Governed Meaning Base (GMB)*. Current terminology in the author-confirmed lineage `CCF -> CMB -> GMB`; exact work identity, publication status, and current-head citation remain pending author adjudication.

The external bibliography above is retained from the author source and normalized only for ASCII portability. It was not externally revalidated in this pass. The corpus relations are AI-prepared editorial synthesis explicitly distinguished from the original author material; they grant no publication, canonical, identity, implementation, or conformance standing.

## Corpus-Wide Reference Positioning

This paper argues that what makes a state transition legitimate when the system performing the transition can also modify the rules, evidence, memories, trust anchors, or verification procedures by which that transition will later be judged?. Its nearest external comparison fields are governance, crypto, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E2]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E3]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Anders Rundgren, Bret Jordan, and Samuel Erdtman. *JSON Canonicalization Scheme (JCS)*. RFC 8785, 2020. https://www.rfc-editor.org/rfc/rfc8785 **Relationship:** Adjacent canonicalization standard relevant to stable cryptographic commitments.

**[E6]** Ben Laurie et al. *Certificate Transparency Version 2.0*. RFC 9162, 2021. https://www.rfc-editor.org/rfc/rfc9162 **Relationship:** Adjacent append-only Merkle-log standard for inclusion and consistency evidence.

**[E7]** Manu Sporny et al., eds. *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 19 July 2022. https://www.w3.org/TR/did-core/ **Relationship:** Adjacent decentralized identity standard; identifier resolution is not assumed to settle semantic standing or jurisdiction.

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

**[A5]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Constitutional Semantic Hashing: Governed Commitment Schemes for Semantic Provenance, Admissibility, and Constitutional Continuity*. Ableman Corpus current edition; work identity `PAPER.PUB.20248734`;  
source SHA-256  
`B1DAC3E2CD4D57BAFBF6462BA6ACFFF7CF120CDB7FA37D0C173525744CC0A2F0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Cryptographic Admissibility and Jurisdiction*. Ableman Corpus current edition; work identity `PAPER.PUB.20602448`;  
source SHA-256  
`6094338D8706F63E8787A5E8DCF40F8A651C0FC3E5EA776DD61791566D094D38`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Abadi, M., Burrows, M., Lampson, B. W., and Plotkin, G. D. (1993). A calculus for access control in distributed systems. ACM Transactions on Programming Languages and Systems, 15(4), 706-734. DOI: 10.1145/155183.155225.

Anderson, J. P. (1972). Computer Security Technology Planning Study. ESD-TR-73-51. U.S. Air Force Electronic Systems Division.

Aristotle. Metaphysics, Book IV, especially 1003a33-b19. Reeve, C. D. C. (trans.), Hackett, 2016. Bekker numbering preserved.

Asma Jilani v. Government of the Punjab, PLD 1972 SC 139 (Supreme Court of Pakistan).

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., et al. (2022). Constitutional AI: Harmlessness from AI feedback. arXiv:2212.08073.

Bracton, H. de. De Legibus et Consuetudinibus Angliae. Thorne, S. E. (trans.), 4 vols. Harvard University Press, 1968-1977.

Campbell, D. T. (1979). Assessing the impact of planned social change. Evaluation and Program Planning, 2(1), 67-90. DOI: 10.1016/0149-7189(79)90048-X.

Clark, D. D., and Wilson, D. R. (1987). A comparison of commercial and military computer security policies. Proceedings of the IEEE Symposium on Security and Privacy, 184-195. DOI: 10.1109/SP.1987.10001.

Dewey, J. (1938). Logic: The Theory of Inquiry. Henry Holt.

Dewey, J. (1941). Propositions, warranted assertibility, and truth. The Journal of Philosophy, 38(7), 169-186. DOI: 10.2307/2017978.

Fuller, L. L. (1964, revised 1969). The Morality of Law. Yale University Press.

Godel, K. (1931). Uber formal unentscheidbare Satze der Principia Mathematica und verwandter Systeme I. Monatshefte fur Mathematik und Physik, 38, 173-198.

Goodhart, C. A. E. (1975). Problems of monetary management: The U.K. experience. Papers in Monetary Economics, Vol. 1. Reserve Bank of Australia. Conference paper delivered 1975; the Reserve Bank volume appeared subsequently. The 1975 conference paper is the artifact cited here.

Hart, H. L. A. (1961; third edition 2012). The Concept of Law. Bulloch, P. A., and Raz, J. (eds.), Oxford University Press.

Kant, I. (1781/1787). Critique of Pure Reason. Guyer, P., and Wood, A. W. (trans.), Cambridge University Press, 1998.

Kelsen, H. (1945). General Theory of Law and State. Wedberg, A. (trans.), Harvard University Press.

Kelsen, H. (1967). Pure Theory of Law. Knight, M. (trans.), University of California Press.

Lamport, L., Shostak, R., and Pease, M. (1982). The Byzantine generals problem. ACM Transactions on Programming Languages and Systems, 4(3), 382-401.

Lampson, B. W., Abadi, M., Burrows, M., and Wobber, E. (1992). Authentication in distributed systems: Theory and practice. ACM Transactions on Computer Systems, 10(4), 265-310.

Laurie, B., Messeri, E., and Stradling, R. (2021). Certificate Transparency Version 2.0. RFC 9162. Internet Engineering Task Force. DOI: 10.17487/RFC9162.

Lob, M. H. (1955). Solution of a problem of Leon Henkin. The Journal of Symbolic Logic, 20(2), 115-118.

Necula, G. C. (1997). Proof-carrying code. Proceedings of the 24th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages, 106-119. DOI: 10.1145/263699.263712.

Raz, J. (1979). The Authority of Law: Essays on Law and Morality. Clarendon Press.

Raz, J. (1986). The Morality of Freedom. Clarendon Press.

Reference Implementation. Revision r174 (archive SHA-256  
629ff94de5de8f9ee8f4deec617a81b0a4429c2fc249455e34523529945c36e1), revision r175 (b5430a200f91efb9c31e4cabb547a6fb30b03db8c32a1743f2b519740725afdc), revision r176 final (ea9b17a9a35501a306c71e3ee01328ef46781b6f86e740844ae37dd27d2e0737), and the external review record concerning the reported --check/ defect. Unpublished software and evaluation artifacts; digests are authoritative for identity.

Ross, A. (1969). On self-reference and a puzzle in constitutional law. Mind, 78(309), 1-24. DOI: 10.1093/mind/LXXVIII.309.1.

Saltzer, J. H., and Schroeder, M. D. (1975). The protection of information in computer systems. Proceedings of the IEEE, 63(9), 1278-1308. DOI: 10.1109/PROC.1975.9939.

Schmidhuber, J. (2007). Godel machines: Fully self-referential optimal universal self-improvers. In Goertzel, B., and Pennachin, C. (eds.), Artificial General Intelligence, 199-226. Springer.

Schneider, F. B. (2000). Enforceable security policies. ACM Transactions on Information and System Security, 3(1), 30-50. DOI: 10.1145/353323.353382.

SLSA Framework (2025). Supply-chain Levels for Software Artifacts Specification, Version 1.2. https://slsa.dev/spec/v1.2/ Version 1.2 announced as an Approved Specification on 24 November 2025. Accessed 2026-08-07.

Soares, N., Fallenstein, B., Armstrong, S., and Yudkowsky, E. (2015). Corrigibility. AAAI Workshop: AI and Ethics, Technical Report WS-15-02. AAAI Press.

State v. Dosso, PLD 1958 SC 533 (Supreme Court of Pakistan), overruled by Asma Jilani.

Suber, P. (1990). The Paradox of Self-Amendment: A Study of Logic, Law, Omnipotence, and Change. Peter Lang.

The Update Framework (2026). The Update Framework Specification. [theupdateframework.github.io source](https://theupdateframework.github.io/specification/latest/) Specification version 1.0.34 per the master branch text macro, document date 2026-01-22. Accessed 2026-08-07. The specification is versioned continuously; cite the version consulted with an access date rather than a bare year.

Thompson, K. (1984). Reflections on trusting trust. Communications of the ACM, 27(8), 761-763. DOI: 10.1145/358198.358210.

Torres-Arias, S., Afzali, H., Kuppusamy, T. K., Curtmola, R., and Cappos, J. (2019). in-toto: Providing farm-to-table guarantees for bits and bytes. 28th USENIX Security Symposium, 1393-1410. USENIX Association.

Tyler, T. R. (2006). Why People Obey the Law. Princeton University Press.

Waldron, J. (2023). The rule of law. The Stanford Encyclopedia of Philosophy, Fall 2023 Edition. Zalta, E. N., and Nodelman, U. (eds.), Stanford University.

Weber, M. (1978). Economy and Society: An Outline of Interpretive Sociology. Roth, G., and Wittich, C. (eds.), University of California Press.

Wittgenstein, L. (1953; fourth edition 2009). Philosophical Investigations. Anscombe, G. E. M., Hacker, P. M. S., and Schulte, J. (trans.), Wiley-Blackwell. See section 258.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847985](https://doi.org/10.5281/zenodo.23847985)
