# Constraint-Bearing Composability

## An Ontology of Constraint Carriage, Component Standing, and Architectural Admission

### Parts become a structure when their relations can bear the present; they become an architecture when those relations can bear what comes next.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Composability is commonly treated as a binary property: components either can or cannot be combined. This framing obscures distinctions among aggregation, formation, compatibility, retention, realization, invariant preservation, component standing, recursive closure, and architectural admissibility.

This paper introduces **Constraint-Bearing Composability**, a diagnostic ontology for analyzing compositional validity. Its central descriptive object is **constraint carriage**: the allocation of responsibility for preserving designated invariants among observers, environment, component-intrinsic structure, interfaces, mediators, internal organization, architecture, and constitutional rules. Carriage is decomposed along two independent axes, locus and granularity, and assessed for adequacy against a declared disturbance envelope.

The framework begins with six primitives: components, relations, context, disturbance envelope, required invariants, and carriage allocation. It then separates four judgment layers routinely collapsed under the word *composition*. A relation may be proposed; a composite may form; the formed composite may or may not be valid; and a governing regime may or may not admit reliance upon it. Formation is ontic, so invalid and unadmitted composites remain representable objects of diagnosis. Standing---justified eligibility to be treated as a bounded component---is a cross-cutting status rather than a fifth layer, and exposure is distinguished from justified exposure.

Composition is non-monotonic with respect to admissibility: pairwise-compatible parts may yield a globally inadmissible configuration through dependency cycles, authority amplification, privacy leakage, semantic contradiction, resource exhaustion, or correlated failure.

The framework complements hierarchy theory, modularity, interface theory, contract-based design, and compositional reasoning without replacing their formalisms. It asks a prior question: what carries the constraints by which a composition remains valid, under which disturbances, and at what scale may the resulting whole justifiably be relied upon?

---

## 1. Introduction

A pile, a stack, a joint, a component, and an architecture all contain more than one part.

They are not the same kind of whole.

A pile of irregular blocks is held together primarily by containment, proximity, or an observer's decision to classify the objects as one collection. A vertical stack of regular cubes exhibits a constitutive relation: geometry permits alignment, while gravity and a level surface preserve the arrangement. Yet the stack separates when lifted, inverted, or disturbed laterally.

Interlocking bricks exhibit another capability. Their interface actively resists separation and misalignment. Joined parts can be moved, rotated, and incorporated into larger assemblies. When such an assembly forms a stable wall panel with exposed attachment points, the wall may itself become a bounded component in a room or building.

The difference is not adequately captured by saying that one arrangement is simply "more composable" than another. Several distinct questions are involved:

* Has a relation merely been proposed, or has a composite actually formed?
* Is the formed relation compatible with the participating components?
* What carries the constraint required to preserve the relation?
* Which disturbances can the relation survive?
* Which properties must remain invariant?
* Does the whole expose a boundary, and is that exposure justified?
* Can it participate in further composition?
* Does the complete configuration remain admissible?
* What evidence supports these claims?
* Has reliance upon the result been permitted?

The framework developed here supplies a common vocabulary for answering those questions.

> **Constraint-Bearing Composability is the capability of bounded components to enter a relation whose constraint-carriage allocation supports the realization of a whole with designated invariants, the preservation of those invariants throughout a declared disturbance envelope, and, where applicable, the resulting whole's justified use as a component in further composition.**

This is the paper's canonical definition.

The framework is a **diagnostic ontology of compositional validity**, not a universal scalar ranking and not a substitute for domain-specific engineering, proof, testing, certification, or governance. Its purpose is to distinguish kinds of compositional claim, locate the mechanisms carrying those claims, expose residual assumptions, and reveal where local validity may fail under higher-order combination.

The physical example provides an intuitive entry point, but the structure recurs elsewhere. A software function may accept another component's output while misinterpreting its units. A protocol adapter may connect two systems while discarding failure semantics. An institutional office may receive a procedurally valid delegation that exceeds the delegator's jurisdiction. A research summary may be inserted into a larger argument while losing the conditions that justified its claims. A financial instrument may be legally combined with another while creating nonlinear correlated exposure.

In each case, connection or formation is possible.

The deeper question is whether the resulting relation can bear the consequences of connection.

Compact entity records appear in Appendix A.4 and a consolidated notation index in Appendix A.5.

---

## 2. Primitive Model

A compositional configuration is represented as:

$$
\begin{aligned}
\Sigma = \langle &\mathcal{N}, \mathcal{R}, \Gamma, \Lambda, K, \chi\rangle
\end{aligned}
$$

where:

| Symbol | Meaning |
| --- | --- |
| $\mathcal{N}$ | Participating components |
| $\mathcal{R}$ | Relations among those components |
| $\Gamma$ | Environmental, architectural, and governance context |
| $\Lambda$ | Disturbance envelope |
| $K$ | Required invariants |
| $\chi$ | Constraint-carriage allocation |

These six primitives are sufficient for the analyses developed here. They are not claimed to exhaust every possible ontology or formal theory of composition.

### 2.1 Components

A component is an entity treated as sufficiently bounded for the purpose of a proposed composition. Its boundary may be physical, computational, informational, semantic, contractual, organizational, or jurisdictional.

A component need not be elementary. It may already be a complex composition. What matters is that it presents an identifiable exterior through which another relation may be proposed. A compact component record is given in Appendix A.4.

### 2.2 Relations

A relation specifies how components interact or are intended to interact.

The relation mode $\mu$ may designate attachment, alignment, containment, sequencing, invocation, exchange, delegation, inference, transformation, mediation, or aggregation.

The same components may be validly composable under one relation and invalid under another. A beam may be safe in compression and unsafe in tension. A dataset may be admissible for aggregate analysis and inadmissible for individual identification. An office may possess authority to advise but not to command.

Composition is relation-sensitive.

### 2.3 Context and Its Projections

The context $\Gamma$ contains conditions not reducible to any component considered alone. These may include gravity, temperature, material tolerances, operating-system services, available memory, network conditions, legal jurisdiction, architectural rules, identity systems, evidentiary standards, historical state, prior delegations, and resource ceilings.

The context decomposes into four parts:

$$
\begin{aligned}
\Gamma = \langle &E_{\Gamma}, K_{\Gamma}, P_{\Gamma}, H_{\Gamma}\rangle
\end{aligned}
$$

| Field | Meaning |
| --- | --- |
| $E_{\Gamma}$ | Contextual guarantees supplied by the environment |
| $K_{\Gamma}$ | Architectural and constitutional invariants |
| $P_{\Gamma}$ | Admission rules of the governing regime |
| $H_{\Gamma}$ | Relevant history and lineage |

Validity and admission must not be indexed by the same undifferentiated context, or the distinction between them collapses at the level of notation. The framework therefore uses two projections:

$$
\Gamma_{\mathrm{val}}
=
\left\langle
E_{\Gamma},
K_{\Gamma},
H_{\Gamma}
\right\rangle
\qquad
\Gamma_{\mathrm{adm}}
=
\left\langle
P_{\Gamma},
K_{\Gamma},
H_{\Gamma}
\right\rangle
$$

Validity-class predicates---compatibility, retention, realization, preservation, validity, standing, and architectural admissibility---are indexed by $\Gamma_{\mathrm{val}}$. Only the admission decision is indexed by $\Gamma_{\mathrm{adm}}$.

The two projections share $K_{\Gamma}$ and $H_{\Gamma}$, so architectural invariants and history bear on both questions, while the regime's admission rules $P_{\Gamma}$ bear only on permission and the environment's guarantees $E_{\Gamma}$ bear only on what the composition actually achieves. Whether a composite preserves its invariants is thereby formally independent of whether any authority has permitted reliance upon it.

Architectural admissibility, developed in Section 13, is a validity-class predicate evaluated at configuration scale under $\Gamma_{\mathrm{val}}$. It asks whether a configuration satisfies architectural and constitutional invariants, not whether a regime has issued a permission.

The projections also bound what may be designated an invariant. Because validity-class predicates are indexed by $\Gamma_{\mathrm{val}}$, which does not contain $P_{\Gamma}$, an invariant whose truth depends upon the regime's current admission rules cannot be evaluated by them: the information required is not in scope. Invariants referring to admission *history* remain evaluable, since $H_{\Gamma}$ is shared by both projections. A composite may therefore be required to preserve the property that its authority was validly delegated at some past moment, but not the property that it is presently admitted. The restriction is enforced by the indexing rather than by stipulation, and it is what prevents the distinction between validity and admission from being reintroduced through the invariant set.

A compositional judgment made without context is usually incomplete.

### 2.4 Disturbance Envelope

The disturbance envelope $\Lambda$ is the declared set of conditions throughout which a compositional claim is intended to hold. It may include force, motion, vibration, fatigue, temperature, latency, concurrency, partial failure, adversarial input, semantic ambiguity, uncertainty, authority pressure, version change, and evidentiary degradation.

No relation bears every conceivable disturbance. Compositional claims are therefore envelope-relative, even when their envelope remains unstated.

### 2.5 Properties, Invariants, and Guarantees

A **property** is any describable feature of a component, relation, configuration, or history.

An **invariant** is a property designated as required to remain true throughout the relevant disturbance envelope.

A **guarantee** is an externally exposed commitment that designated properties will hold under declared assumptions.

If $P$ is the relevant property set, then:

$$
K \subseteq P
$$

A guarantee exposed by component $C$ may assert:

$$
G:\;
A
\Rightarrow
\operatorname{Preserves}_{\Gamma_{\mathrm{val}}}(C,K,\Lambda)
$$

The distinction is structural. A component may possess many properties irrelevant to a particular composition. An invariant is selected because its loss would invalidate the compositional claim. A guarantee exposes a commitment concerning such preservation to an external actor.

### 2.6 Constraint-Carriage Allocation

The constraint-carriage allocation $\chi$ identifies where responsibility for preserving $K$ throughout $\Lambda$ resides.

Carriage decomposes along two independent axes. The first is **locus**:

$$
\begin{aligned}
\chi = \langle &\chi_O, \chi_E, \chi_G, \chi_I, \chi_M, \chi_U, \chi_A, \\
&\chi_Q\rangle
\end{aligned}
$$

| Term | Carriage locus |
| --- | --- |
| $\chi_O$ | Observer, classification, or containment |
| $\chi_E$ | Environmental conditions |
| $\chi_G$ | Component-intrinsic geometry, material, or structure |
| $\chi_I$ | Interfaces |
| $\chi_M$ | Mediators |
| $\chi_U$ | Internal organization of the resulting whole |
| $\chi_A$ | Architecture |
| $\chi_Q$ | Constitutional or highest-order admissibility rules |

The second axis is **granularity**---whether the allocation is recorded for a component, a relation, or a complete configuration---and is developed in Section 6.1. A locus allocation may be stated at any granularity, and the axes should not be confused: $\chi_G$ names a *locus* internal to a component, whereas $\chi(C)$ names the allocation recorded *for* a component, which may itself distribute across several loci.

Constraint carriage is an allocation, not a transition and not a judgment of adequacy. It describes the current distribution of preserving work.

The central diagnostic question is:

> **What is doing the work required to keep this composition valid?**

---

## 3. Aggregation, Realization, and Constitutive Relation

The distinction between aggregation and composition depends upon whether relations among the participating components are constitutive of the relevant whole.

### 3.1 Aggregation

Aggregation is common containment, proximity, or membership without a constitutive relation among the aggregated members. Examples include blocks in a bin, files in a directory, sources in a reading list, and employees on a roster.

The aggregate may depend upon an external container, classification, or observer. If that container is itself modeled as a component, the larger arrangement containing the items and the container may constitute a composition. The items considered only as co-members remain an aggregate.

### 3.2 Realization and Preservation

Constitutive relations typically do more than keep an existing whole intact. They bring the whole and its defining properties into being.

A chemical reaction generates a compound. Joining structural parts creates a load path that did not previously exist. An inference produces a conclusion. A legal act creates an office or an obligation. In each case the relation is not maintaining a pre-existing property but establishing one.

The framework therefore distinguishes:

* **realization:** bringing the whole and its designated properties into being;
* **preservation:** keeping those properties true under disturbance.

The realization predicate is envelope-free:

$$
\operatorname{Realizes}_{\Gamma_{\mathrm{val}}}
\left(
\left\langle \mathcal{N},\mathcal{S} \right\rangle,
K
\right)
$$

It holds when the relation set $\mathcal{S}$ over participants $\mathcal{N}$ establishes a whole in which $K$ initially holds. The envelope belongs to preservation alone:

$$
\operatorname{Preserves}_{\Gamma_{\mathrm{val}}}
\left(
\left\langle \mathcal{N},\mathcal{S} \right\rangle,
K,
\Lambda
\right)
$$

Neither predicate entails the other, and the separation is not merely terminological. A composite may be correctly realized at formation and fail under the very first disturbance: a joint may be properly made and then creep, a delegation may be validly issued and then exceeded, an inference may be soundly drawn and then lose its warrant when a cited source is withdrawn. Conversely, a relation may contribute to preserving a whole it played no part in bringing into being, as when external bracing stabilizes a structure it did not create.

The two capabilities may also be carried by different mechanisms. Realization is often carried by an act, a procedure, or a transformation, while preservation is carried by geometry, interfaces, custody, or governance that persists after the act is complete. Constraint carriage should therefore be recorded for both, and a composition whose realizing mechanism is well evidenced tells one little about whether its preserving mechanism is adequate.

### 3.3 The Constitutive-Relation Criterion

A relation is constitutive with respect to an invariant set $K$ and disturbance envelope $\Lambda$ when it belongs to at least one minimal relation set that both realizes $K$ and preserves it throughout $\Lambda$.

Writing $\Theta(\mathcal{S})$ for the conjunction:

$$
\Theta(\mathcal{S})
\;\equiv\;
\operatorname{Realizes}_{\Gamma_{\mathrm{val}}}
\left(
\left\langle \mathcal{N},\mathcal{S} \right\rangle,
K
\right)
\;\land\;
\operatorname{Preserves}_{\Gamma_{\mathrm{val}}}
\left(
\left\langle \mathcal{N},\mathcal{S} \right\rangle,
K,
\Lambda
\right)
$$

a relation $R$ is constitutive when:

$$
\begin{aligned}
&\exists\,\mathcal{S} \subseteq \mathcal{R}:\quad R \in \mathcal{S} \; \\
&\land \; \Theta(\mathcal{S}) \; \\
&\land \; \forall\,\mathcal{S}' \subsetneq \mathcal{S}:\; \\
&\ne g\,\Theta(\mathcal{S}')
\end{aligned}
$$

The final conjunct establishes minimality: no proper subset of $\mathcal{S}$ suffices.

Minimality is taken with respect to the conjunction, not to either conjunct separately. Within a minimal $\mathcal{S}$, the relations doing the realizing work and those doing the preserving work may be disjoint, so a relation may be constitutive by virtue of either contribution. Where an analysis needs to distinguish them, the two conjuncts may be minimized independently, yielding a minimal realizing set and a minimal preserving set that need not coincide; the bracing example above is exactly such a case.

The criterion permits redundant systems. A relation may remain constitutive even when removing it does not immediately destroy the whole, provided it belongs to some minimal sufficient relation set.

The distinction can therefore be stated as:

$$
\operatorname{Aggregation}
\not\Rightarrow
\operatorname{Composition}
$$

Composition begins when one or more relations among participating components realize and preserve the properties by which the whole is identified or used.

---

## 4. Four Layers of Compositional Judgment

The word *composition* often collapses several logically different events. The framework separates four layers.

### 4.1 Proposal

A relation may be proposed without being realized:

$$
\operatorname{Proposed}_{\Gamma_{\mathrm{val}}}
(C_1,C_2,R)
$$

A proposal identifies intended participants, relation mode, disturbance envelope, required invariants, and anticipated carriage.

### 4.2 Formation

A composite forms when the proposed or accidental relation is actually instantiated:

$$
\operatorname{Forms}
(C_1,C_2,R,C_3)
$$

Formation is ontic. It says that a resulting object or configuration exists. It does not imply compatibility, invariant preservation, standing, or admission.

Components may be forcibly, accidentally, or defectively joined. Invalid compositions remain real objects of analysis. The corresponding formation operator is given in Section 10.5.

### 4.3 Validity

A formed composite is valid with respect to a context, its relations, envelope, and invariant set when it preserves the required invariants:

$$
\operatorname{Valid}_{\Gamma_{\mathrm{val}}}
(C_3 \mid \varrho,\Lambda,K)
$$

The second argument $\varrho$ is a relation or a relation set: a single relation when the claim concerns one connection, and the constitutive relation set of Section 10.6 when it concerns the composite as a whole. As with $\operatorname{Preserves}$, scope is carried by the argument rather than by predicate arity.

Validity is claim-relative. The same formed object may be valid for one purpose or envelope and invalid for another. An unindexed assertion of validity is therefore incomplete.

### 4.4 Admission

Admission is an authoritative judgment permitting use or reliance within a governing regime:

$$
\operatorname{Admitted}_{\Gamma_{\mathrm{adm}}}
(C_3,p,\mathcal{E}_A)
$$

where $p$ is the admitted purpose and $\mathcal{E}_A$ is the admission evidence object of Section 8.5.

The dependency is therefore:

$$
\begin{aligned}
&\text{proposal} \\
&\rightarrow \text{formation} \\
&\rightarrow \text{validity judgment} \\
&\rightarrow \text{admission judgment}
\end{aligned}
$$

No arrow implies that the next stage necessarily succeeds. Because validity is evaluated under $\Gamma_{\mathrm{val}}$ and admission under $\Gamma_{\mathrm{adm}}$, the two judgments are formally independent: neither entails the other, and each defective combination remains expressible.

### 4.5 Standing Is Not a Fifth Layer

The four layers above concern events and judgments about events: a relation is proposed, a composite forms, its invariant preservation is assessed, and a regime decides whether reliance is permitted.

**Standing**---the justified eligibility of a formed composite to be treated as a bounded component for a declared purpose---is not a fifth event in this sequence. It is a **cross-cutting status** concerning whether reliance upon a boundary is warranted. Standing is developed in Section 8.3, and the relationship a well-governed admission regime should maintain between standing and admission is stated in Section 8.6. Because standing is a status rather than a stage, it may be acquired, retained, narrowed, or lost independently of any particular admission decision.

---

## 5. Compatibility, Retention, and Invariant Preservation

### 5.1 Compatibility

Compatibility is a local predicate concerning whether a proposed relation satisfies the applicable requirements of its participants and context:

$$
\operatorname{Compatible}_{\Gamma_{\mathrm{val}}}
(C_1,C_2,R)
$$

Compatibility is predictive and normative. It indicates that the relation is expected to be establishable without immediate contradiction of local conditions.

Compatibility is not required for formation. Incompatible parts can be forced together. Incompatible services can exchange malformed messages. Incompatible authorities can issue contradictory orders. Compatibility instead concerns whether the relation is locally well-formed for its intended use.

### 5.2 Retention

A formed relation is retentive when it remains established throughout the disturbance envelope:

$$
\operatorname{Retains}_{\Gamma_{\mathrm{val}}}
(C_3,R,\Lambda)
$$

Retention concerns persistence of relation. It does not imply preservation of every required invariant.

### 5.3 Invariant Preservation

A formed composition is invariant-bearing when it preserves the designated invariants throughout the disturbance envelope:

$$
\operatorname{Preserves}_{\Gamma_{\mathrm{val}}}
(C_3,K,\Lambda)
$$

The preservation predicate takes a uniform three-place form in which the first argument is the **subject**: a component, a composite, a relation set with its participants, or a complete configuration. Scope is determined by the subject rather than by predicate arity.

Retention is a special case in which continued attachment or correspondence is itself the principal invariant.

A relation may persist while losing alignment, semantic meaning, privacy, authority, evidentiary support, performance, or failure containment. A pair of services may remain connected while corrupting shared state. A delegation may remain procedurally active while exceeding its authorized scope. A summary may remain linked to a source while misrepresenting its conclusion.

Persistence is therefore weaker than invariant preservation.

---

## 6. Constraint Carriage

### 6.1 Carriage as Allocation

Constraint carriage describes the present allocation of responsibility for preserving a composition.

Section 2.6 decomposed carriage by locus. The second axis is **granularity**. An allocation may be recorded for a component, $\chi(C)$; for a relation, $\chi(R)$; or for a complete configuration, $\chi(\Sigma)$. Each is itself a locus allocation of the form given in Section 2.6. The axes are independent: granularity states *for what* the allocation is recorded, locus states *by what* the preserving work is done.

Configuration-level carriage is derived from the components, relations, mediators, and context:

$$
\chi(\Sigma)
=
\operatorname{AggregateCarriage}_{\Gamma_{\mathrm{val}}}
\left(
\{\chi(C)\},
\{\chi(R)\}
\right)
$$

The aggregation is not necessarily additive. Multiple mechanisms may jointly preserve one invariant, substitute for one another, or interact nonlinearly.

### 6.2 Constraint Internalization

Constraint internalization is a transition in which preserving responsibility moves inward, from an external context into component-intrinsic structure, an interface, a mediator, or the internal organization of a composite. Examples include a gravity-supported stack becoming an interlocking assembly, a manually supervised workflow becoming governed by explicit validation, an informal practice becoming a ratified procedure, and an uncited claim becoming bound to retrievable evidence.

Internalization may improve durability, autonomy, or inspectability. It may also increase cost, rigidity, coupling, or concentration of failure.

The design objective is not maximum internalization. It is appropriate carriage.

### 6.3 Constraint Externalization

Constraint externalization is a transition in which preserving responsibility moves outward or is exported to the environment. Examples include a service requiring clients to implement retries, a component relying upon external authentication, a summary requiring readers to recover omitted qualifications, and an institution relying upon informal oversight.

Externalization is not inherently defective. Every component exports assumptions. Failure occurs when the exported burden is hidden, unsupported, or assigned to a context incapable of carrying it.

### 6.4 Carriage Adequacy

Carriage adequacy is a judgment concerning whether the allocation $\chi$ can preserve $K$ throughout $\Lambda$:

$$
\operatorname{AdequateCarriage}_{\Gamma_{\mathrm{val}}}
(\chi,K,\Lambda)
$$

Carriage may be environmental, intrinsic, interfacial, mediated, organizational, architectural, or constitutional. Its adequacy depends upon the claimed use, not upon proximity to a component's interior.

Sometimes gravity should be allowed to carry gravity's share.

---

## 7. Paired Illustration: Bricks and Evidence

A comparison between interlocking bricks and evidence modules shows the ontology's cross-domain structure.

- **Question:** Components  
  **Interlocking bricks:** Bricks and subassemblies  
  **Evidence module:** Claims, observations, sources, warrants

- **Question:** Relation  
  **Interlocking bricks:** Attachment and alignment  
  **Evidence module:** Evidentiary support and inference

- **Question:** Context  
  **Interlocking bricks:** Gravity, material tolerances, temperature  
  **Evidence module:** Definitions, source access, analytical standards

- **Question:** Disturbances  
  **Interlocking bricks:** Inversion, shear, vibration, wear  
  **Evidence module:** Copying, summarization, contradiction, scope drift

- **Question:** Invariants  
  **Interlocking bricks:** Attachment, geometry, load path  
  **Evidence module:** Provenance, scope, uncertainty, warrant

- **Question:** Constraint carriage  
  **Interlocking bricks:** Shape, material, friction, studs, tubes  
  **Evidence module:** Citations, custody, inference rules, review

- **Question:** Candidate standing  
  **Interlocking bricks:** Stable subassembly with exposed interfaces  
  **Evidence module:** Bounded and inspectable evidence package

- **Question:** Higher-order risk  
  **Interlocking bricks:** Hidden weak joints  
  **Evidence module:** Evidence laundering or unsupported inference

The mechanisms differ. A brick connection bears physical forces; an evidence relation bears justificatory structure.

The common pattern is nevertheless precise:

1. bounded components enter a relation;
2. a resulting composite forms;
3. the relation exists within a context;
4. designated mechanisms carry the work of realizing and preserving required invariants;
5. disturbances threaten those invariants;
6. the resulting whole may or may not earn standing;
7. higher-order composition may introduce new failure modes.

The framework claims structural correspondence, not identity of mechanism.

---

## 8. Capability, Structure, and Standing

Three questions are routinely conflated: what a relation can do, where an object sits in a larger organization, and whether reliance upon its boundary is warranted. This section separates them and specifies the records through which each is stated.

### 8.1 Relational Capacity as a Profile

Relational capacity should not be represented as a single universal score. It is modeled as a profile:

$$
\begin{aligned}
\operatorname{RC}(X) = \langle &K_X, \Lambda_X, \rho_X, \delta_X\rangle
\end{aligned}
$$

where $K_X$ is the set of invariants preserved, $\Lambda_X$ the supported disturbance envelope, $\rho_X$ the preservation margin, and $\delta_X$ the degradation and failure-containment behavior.

The profile records capability. Whether that capability has been shown is a separate matter, recorded through the evidence object of Section 8.5.

Two relations may be incomparable. One may preserve a broad set of semantic invariants under low load; another a narrow mechanical invariant under extreme load. One may fail abruptly, another degrade gracefully. One may depend on environmental carriage, another on an interface.

Carriage location is annotated separately through $\chi$. An environmentally retained relation and an interface-retained relation may possess equivalent relational capacity within the same envelope. Their mechanisms differ; their capability need not.

A partial comparison is possible when one profile preserves at least the same invariants, through at least the same envelope, with at least the same margin and no worse degradation behavior. Many real profiles remain only partially ordered.

### 8.2 Structural Role and Nesting Depth

Structural position also requires two independent measures, because the familiar vocabulary of roles does not form a single ordered scale. A primitive bolt may be a bounded component without ever having been an assembly. A subsystem may contain a complete architecture. An architecture may operate as a component within a federation.

The first measure is **structural role**, which is set-valued and configuration-indexed, because one object may occupy several roles at once: an architecture acting as a component within a federation holds both roles simultaneously, and neither description is a mistake.

$$
\begin{aligned}
\operatorname{Roles}_{\Sigma}(X) \subseteq \{&\text{entity}, \text{collection}, \text{assembly}, \\
&\text{component}, \text{subsystem}, \text{system}, \\
&\text{architecture}, \text{ecology}\}
\end{aligned}
$$

| Role | Meaning |
| --- | --- |
| Entity | A bounded thing considered without internal compositional analysis |
| Collection | Members sharing containment or classification without constitutive relations |
| Assembly | Members whose constitutive relations realize a whole |
| Component | An object presenting an identifiable exterior for use in further relations |
| Subsystem | An organized part fulfilling a delimited function within a larger whole |
| System | An organized whole pursuing its own purposes |
| Architecture | A governed organization of components under shared rules |
| Ecology | Multiple architectures interacting across partially distinct standards, assumptions, or governance regimes, often through mediators |

The second measure is **nesting depth**, which is path-relative:

$$
\operatorname{Depth}_{\Sigma}(X,w)
\in
\mathbb{N}
$$

where $w$ is a constitutive or containment path from the outermost boundary of $\Sigma$ to $X$, and the value is the number of boundary crossings along $w$.

Depth is stated per path rather than as a single number or a set of numbers. An object reachable through several constitutive paths has one depth for each, and retaining the path preserves the lineage that a bare set of integers would discard: knowing that a component sits at depths two and five is far less useful than knowing which two routes reach it, since those routes are what a failure analysis must follow. Depth is also configuration-relative, so the same object has different depths in different configurations.

Roles, depth, capability, and standing are mutually independent. An object may hold the role of component, sit at depth four along one path and depth two along another, carry a relational-capacity profile specified separately, and possess no standing at all. An undocumented script may be structurally bounded and repeatedly embedded in workflows while lacking justified guarantees.

Examples of ecologies include markets, federated software environments, multinational legal systems, and the public web.

### 8.3 Standing

Standing is the justified eligibility of a composition to be treated as a bounded component for a declared purpose. It is purpose-indexed:

$$
\operatorname{Standing}_{\Gamma_{\mathrm{val}}}
(C,p)
$$

A composition may possess standing for one purpose and not another.

Standing is a derived predicate rather than a primitive one. It holds when some applicable diagnostic record establishes that the composite is valid for the claim that record states, that its evidence is adequate to the reliance intended, and that its boundary is adequate to the purpose:

$$
\begin{aligned}
&\operatorname{Standing}_{\Gamma_{\mathrm{val}}}(C,p) \;\Longleftrightarrow\; \exists\,\mathcal{D}:\; \operatorname{Applies}(\mathcal{D},C,p) \; \\
&\land \; \operatorname{Valid}_{\Gamma_{\mathrm{val}}} \left( C \mid \operatorname{Constitution}(C), \Lambda_{\mathcal{D}}, K_{\mathcal{D}} \right) \; \\
&\land \; \operatorname{AdequateEvidence}(\mathcal{E}_{\mathcal{D}},p) \; \\
&\land \; \operatorname{AdequateBoundary}(C,p)
\end{aligned}
$$

Here $\operatorname{Constitution}(C)$ is the constitutive relation set retained with $C$ by the formation update of Section 10.6, and $\Lambda_{\mathcal{D}}$, $K_{\mathcal{D}}$, and $\mathcal{E}_{\mathcal{D}}$ are that record's envelope, invariants, and evidence.

Because $C$ is not itself a field of $\mathcal{D}$, applicability is checked through the record's evidence object, whose subject field carries the entity under analysis:

$$
\operatorname{Applies}(\mathcal{D},C,p)
\;\Longleftrightarrow\;
s_{\mathcal{E}_{\mathcal{D}}} = C
\;\land\;
\operatorname{Covers}(q_{\mathcal{D}},p)
$$

where $\operatorname{Covers}(q,p)$ holds when the capability claim $q$ extends to the purpose $p$.

The existential binds every variable that would otherwise appear free on the right: standing asserts that an adequate justification exists, not that any particular document has been consulted. Boundary adequacy is fixed by $C$'s own exposed record and so takes no further argument.

Standing is not confined to composites. For a component never formed from parts, such as a primitive fastener or an atomic service, $\operatorname{Constitution}(C)=\varnothing$ and the validity conjunct becomes a claim about the component itself rather than about any internal structure. The empty case is admissible, not excluded.

The conjuncts correspond to the questions standing answers: does the composite do what is claimed, is that claim supported, and is the exterior through which it will be used sufficient for the intended reliance. Boundary adequacy requires controlled identity, defined interfaces, explicit assumptions, justified guarantees, a declared disturbance envelope, known failure conditions, and lifecycle state.

The derivation makes plain why standing is justificatory rather than simply another validity predicate. Validity concerns what the composite preserves; standing concerns whether an external party is warranted in depending on it without reopening its interior. A composite may be valid and still lack standing, because no evidence has been assembled or because the boundary conceals what a user would need to know.

Encapsulation alone does not establish standing:

$$
\operatorname{Encapsulation}
\not\Rightarrow
\operatorname{Standing}
$$

### 8.4 The Diagnostic Record

A capability claim is stated through a unified diagnostic record:

$$
\begin{aligned}
\mathcal{D} = \langle &q, \Lambda, K, \chi, \mathcal{E}, A_{\mathrm{res}}, \Phi, \\
&V\rangle
\end{aligned}
$$

| Symbol | Meaning |
| --- | --- |
| $q$ | Capability claim |
| $\Lambda$ | Disturbance envelope |
| $K$ | Required invariants |
| $\chi$ | Constraint-carriage allocation |
| $\mathcal{E}$ | Evidence object |
| $A_{\mathrm{res}}$ | Residual assumptions |
| $\Phi$ | Failure conditions |
| $V$ | Version and lifecycle state |

This record is used in the worked profiles of Section 15 and reproduced in full in Appendix C.

### 8.5 Evidence Objects

Evidence appears at several scopes: supporting a component's guarantees, a proposed or formed relation, or an admission decision. Rather than a separate symbol for each, the framework uses one scoped object:

$$
\mathcal{E}
=
\left\langle
s,
c,
m,
r,
u,
\pi
\right\rangle
$$

| Field | Meaning |
| --- | --- |
| $s$ | Subject: the component, relation, composite, or configuration |
| $c$ | Claim the evidence bears upon |
| $m$ | Evaluation method |
| $r$ | Result obtained |
| $u$ | Uncertainty and known limits |
| $\pi$ | Provenance |

Methods may include measurement, mechanical testing, formal proof, simulation, conformance testing, fault injection, operational history, inspection, independent replication, and semantic review. The ontology standardizes the structure of the evidence claim; it does not prescribe one universal measurement method across domains.

Scoped instances are written $\mathcal{E}_C$ for component evidence, $\mathcal{E}_R$ for relation evidence, and $\mathcal{E}_A$ for admission evidence. When $\mathcal{E}$ appears inside a diagnostic record $\mathcal{D}$, its subject and claim fields are fixed by that context: the subject $s$ is the entity under analysis and the claim $c$ is the record's capability claim $q$. These fields are bound rather than omitted, which is what allows Section 8.3 to identify a record's subject by reading $s$.

### 8.6 Status Vocabularies

Evidentiary support, justified boundary, and permitted reliance are three different questions and require three different state vocabularies. Collapsing them produces lists in which an evidentiary term and a governance term appear as alternatives to one another.

| Status class | States |
| --- | --- |
| Evidentiary status | unsupported, preliminary, demonstrated, independently supported, contradicted, stale |
| Standing status | candidate, qualified, constrained, demoted, lost |
| Admission status | pending, admitted, active, suspended, revoked, expired, retired |

Admission does not create capability. Revoking admission does not necessarily destroy capability or standing; it removes permitted reliance within the admitting regime. Standing is lost only when the justification for bounded reliance is itself undermined. Evidence may become stale without any decision being taken at all.

For admissions that rely upon an object as a bounded component, a well-governed regime should satisfy:

$$
\operatorname{Admitted}_{\Gamma_{\mathrm{adm}}}(C,p,\mathcal{E}_A)
\Rightarrow
\operatorname{Standing}_{\Gamma_{\mathrm{val}}}(C,p)
$$

The reverse does not follow:

$$
\operatorname{Standing}_{\Gamma_{\mathrm{val}}}(C,p)
\not\Rightarrow
\exists\,\mathcal{E}_A:\;
\operatorname{Admitted}_{\Gamma_{\mathrm{adm}}}(C,p,\mathcal{E}_A)
$$

A capable and well-supported component may be denied admission because of policy, jurisdiction, timing, resource limits, or architectural conflict.

Because the two predicates are indexed by different context projections, the implication above is a normative property of well-governed regimes rather than a theorem. Its failure is precisely the defect catalogued in Section 16.16.

---

## 9. An Illustrative Path Through the Ontology

The following path is pedagogical. It is not a hierarchy of universal superiority, a necessary developmental sequence, or a claim that every system should maximize internal carriage.

**Aggregation.** Objects share containment or classification without a constitutive relation among the members. Constraint carriage resides mainly in the container, context, or observer.

**Environment-supported composition.** Regularity permits alignment while environmental conditions preserve the relation. A stack relies upon geometry, gravity, and orientation.

**Interface-retained composition.** An interface preserves the relation across disturbances that would dissolve the environmentally supported arrangement. Some preserving responsibility has been internalized.

**Invariant-bearing composition.** The formed relation preserves specified properties under intended operational disturbances. Persistence has become a broader capability.

**Standing and architecture.** A bounded assembly earns standing and may participate in higher-order structures governed by configuration-level rules.

This is one possible trajectory. Systems may exhibit deep nesting with weak boundaries, strong local capacity without architectural closure, or extensive structural depth with poor evidentiary support.

---

## 10. Mediation, Formation, and Recursive Closure

This section treats how compositions are actually brought about: directly or through intermediaries, what the resulting configuration update does, what the composite may expose, and whether the result remains eligible for further composition.

### 10.1 Direct Composition

Direct composition occurs through the native interfaces of participating components. No translating intermediary is required, although the relation still depends upon context.

### 10.2 Mediated Composition

When two components cannot establish the intended direct relation, a mediator may enable a larger composition. Let $M$ be a mediator between $A$ and $B$. The mediated path is:

$$
A
\xrightarrow{\;R_1\;}
M
\xrightarrow{\;R_2\;}
B
$$

Examples include physical adapters, voltage converters, protocol gateways, compilers, schema translators, interpreters, legal instruments, organizational liaisons, currency exchanges, and evidence summaries.

The mediator does not erase incompatibility. It carries the work of transforming, translating, buffering, authenticating, or governing it.

### 10.3 Mediation Burden

A mediator introduces assumptions, transformations, latency, authority, information loss, version dependencies, resource demands, and failure modes.

A plug adapter may preserve geometry while failing to preserve voltage compatibility. A schema translator may preserve field structure while corrupting meaning. A summary may preserve a conclusion while losing uncertainty.

Mediators are both engines of composability and concentrated sites of compositional risk.

### 10.4 Mediator Paths

A composition may depend upon several mediators:

$$
A
\xrightarrow{\;R_1\;}
M_1
\xrightarrow{\;R_2\;}
M_2
\xrightarrow{\;R_3\;}
B
$$

Each step may accumulate semantic loss, latency, dependency, authority, ambiguity, and failure probability. The validity of the complete path cannot necessarily be inferred from the validity of each edge.

### 10.5 Typed Formation

Let $\mathcal{C}_{\sigma}$, $\mathcal{C}_{\tau}$, and $\mathcal{C}_{\upsilon}$ be component classes. A relation-sensitive formation operator is partial:

$$
\operatorname{form}_{R}:\;
\mathcal{C}_{\sigma}
\times
\mathcal{C}_{\tau}
\rightharpoonup
\mathcal{C}_{\upsilon}
$$

For $C_1 \in \mathcal{C}_{\sigma}$ and $C_2 \in \mathcal{C}_{\tau}$, the expression:

$$
\operatorname{form}_{R}(C_1,C_2)=C_3
$$

means only that the formation succeeded and produced $C_3$. It does not assert that $C_3$ is valid or admitted.

The operator is partial because some formations cannot occur at all: no instantiation of the relation is physically, computationally, or institutionally possible for those participants. **Partiality tracks realizational impossibility, not incompatibility, invalidity, or non-admission.** Incompatible but joinable participants lie inside the operator's domain, and their forced or defective composites are precisely the objects the framework must retain.

The operator and the formation predicate of Section 4.2 describe the same event in two notations:

$$
\operatorname{Forms}(C_1,C_2,R,C_3)
\;\Longleftrightarrow\;
\operatorname{form}_{R}(C_1,C_2)=C_3
$$

### 10.6 Formation Update

The formation update is written:

$$
\Sigma_F
=
\Sigma
\oplus_F
\left[
(C_1,C_2,R)
\mapsto
C_3
\right]
$$

The update performs four conceptual operations:

1. $C_3$ is added to the configuration;
2. $C_1$, $C_2$, and $R$ are retained as the constitutive subgraph of $C_3$;
3. lineage is recorded in the historical context $H_{\Gamma}$;
4. configuration-level carriage $\chi(\Sigma)$ is recomputed.

Formation does not erase the parts.

### 10.7 Constitutive and Exposed Views

The framework distinguishes two views of the resulting configuration.

The **constitutive view** retains internal components, internal relations, mediators, assumptions, evidence, and failure paths.

The **exposed view** presents the boundary and interfaces of $C_3$. Writing $F_i$ for the exposed interface set of component $C_i$, the composite interface set $F_3$ may preserve interfaces inherited from $C_1$ or $C_2$, hide internal interfaces, transform interfaces, generate new interfaces, or reserve interfaces for later use. Schematically:

$$
F_3
\subseteq
\operatorname{ProjectInterfaces}_{\Gamma_{\mathrm{val}}}
(F_1,F_2,R)
$$

### 10.8 Exposure and Justified Exposure

Exposure is an act, not an entitlement. Systems routinely publish, package, or advertise composites that have not earned standing, and the framework must be able to describe that situation rather than exclude it by construction.

Actual exposure is written:

$$
\Sigma_S
=
\operatorname{Expose}(\Sigma_F,C_3)
$$

and occurs whether or not it is warranted. Justified exposure is a separate predicate:

$$
\operatorname{JustifiedExposure}_{\Gamma_{\mathrm{val}}}
(\Sigma_F,C_3,p)
\;\Longleftrightarrow\;
\operatorname{Standing}_{\Gamma_{\mathrm{val}}}(C_3,p)
$$

This parallels the framework's central move. Three separations follow the same pattern:

* formation can occur without validity;
* exposure can occur without standing;
* reliance can occur without admission.

Each defective state remains representable rather than being rendered impossible by the formalism. Section 16 catalogues the corresponding failures.

When exposure is justified, the constitutive subgraph nevertheless remains recoverable for inspection, demotion, migration, and failure analysis. This is earned abstraction without destructive concealment.

### 10.9 Residual Assumptions and Composite Guarantees

Real compositions normally retain environmental assumptions.

Let $C_1$ and $C_2$ expose assumptions $A_1,A_2$ and guarantees $G_1,G_2$. Partner guarantees and the contextual guarantees $E_{\Gamma}$ may discharge some assumptions. The remainder are exported to the composite:

$$
A_3
=
\operatorname{Residual}_{\Gamma_{\mathrm{val}}}
(A_1,A_2,G_1,G_2,R)
$$

Validity does not require:

$$
A_3=\varnothing
$$

Residual assumptions must instead be explicit, internally consistent, supportable within the intended context, and proportionate to the guarantees exposed by the composite.

The composite may expose only guarantees justified by the formed relation:

$$
G_3
\subseteq
\operatorname{Consequences}_{\Gamma_{\mathrm{val}}}
(G_1,G_2,R,A_3)
$$

A composition that hides its residual assumptions or overstates its consequences possesses an unreliable boundary, even when its internal mechanisms function.

### 10.10 Recursive Closure

A formed composite exhibits recursive closure when it belongs to a recognized component class and may participate in another formation.

Recursive closure is not necessary for standing. A sealed safety component, finalized legal instrument, or fixed evidentiary record may possess a justified boundary while intentionally terminating recursion.

Recursive closure is not sufficient for standing. An undocumented script may be repeatedly embedded in workflows without exposing trustworthy assumptions or guarantees.

Thus:

> **Standing concerns justified bounded reliance. Recursive closure concerns eligibility for further formation.**

A recursively usable composite may preserve inherited interfaces, hide internal interfaces, expose transformed interfaces, generate new interfaces, or reserve capacity for later composition. Recursive systems are especially powerful when formation does not consume every future interface.

### 10.11 Recursive Fragility

Each layer may also lose performance margin, semantic precision, evidence, authority traceability, fault isolation, and reversibility.

A system can become structurally deeper while becoming less trustworthy. Recursive composition should therefore track what each layer inherits, transforms, exports, conceals, and loses.

---

## 11. Composability and Compositionality

**Composability** concerns whether components can enter a valid relation and form a usable whole.

**Compositionality** concerns whether relevant properties of that whole can be derived or bounded from the components, their relation, and the governing context.

The distinction is established in the formal literature on component-based and contract-based design. It is restated here because the two terms remain routinely conflated in general architectural usage, and because later sections depend upon keeping them apart.

A system may be readily composable while remaining weakly compositional. Plugins may install cleanly while interacting unpredictably. Financial instruments may be contractually combinable while producing opaque correlated risk. Evidence modules may be easy to concatenate while supporting conclusions that cannot be derived from their individual warrants.

The stronger analytical objective is not merely to establish that a composite forms, but to determine whether its relevant properties follow from component properties, relation semantics, residual assumptions, constraint carriage, and architectural context.

Contract-based design and interface theories provide formal machinery for portions of this task (de Alfaro & Henzinger, 2001; Benveniste et al., 2018). Constraint-Bearing Composability places that machinery within a wider diagnostic account of formation, carriage, standing, and configuration-level admissibility.

---

## 12. Diachronic Composability

Composability is often evaluated as though components and contexts remain fixed. They do not.

**Diachronic composability** is the capability of a composition to preserve or validly transform its relations across time.

A composition may decay because a component is revised, a protocol is deprecated, a dependency disappears, a material wears, authority expires, a legal regime changes, semantic definitions drift, evidence becomes stale, environmental guarantees fail, or mediators change behavior.

A composition may survive change through substitution, state migration, interface revision, adaptation, narrowed guarantees, newly exported assumptions, renewed testing, reauthorization, and preservation of lineage.

Change raises the question of identity continuity:

> When does a revised composition remain the same compositional object?

Continuity may depend upon explicit lineage, controlled transformation, continuity of purpose, continuity of authority, bounded changes to guarantees, and retained historical custody.

Diachronic composability therefore intersects with versioning, provenance, standing, and admission.

---

## 13. Architectural Admissibility

### 13.1 Configurations, Not Edges

Architectural admissibility is evaluated over the complete configuration:

$$
\operatorname{Admissible}_{\Gamma_{\mathrm{val}}}(\Sigma)
$$

It may depend upon topology, dependency cycles, mediator paths, aggregate resource demand, shared dependencies, authority accumulation, information flow, and historical sequence.

Pairwise judgments alone cannot establish it. For binary relations, let $\operatorname{src}(R)$ and $\operatorname{dst}(R)$ identify the relation endpoints; for symmetric modes such as attachment or alignment the assignment is arbitrary and the predicate is order-insensitive. Then:

$$
\left(
\forall R \in \mathcal{R}:\;
\operatorname{Compatible}_{\Gamma_{\mathrm{val}}}
\left(
\operatorname{src}(R),
\operatorname{dst}(R),
R
\right)
\right)
\not\Rightarrow
\operatorname{Admissible}_{\Gamma_{\mathrm{val}}}(\Sigma)
$$

Every edge may be locally compatible while the graph is globally inadmissible.

### 13.2 Non-Monotonic Admissibility

Let $\Sigma$ be an admissible configuration, $C$ a component valid for its own declared relation, envelope, and invariants, and $R$ a locally compatible relation attaching it.

The extension update adds a component and an edge without producing a composite:

$$
\begin{aligned}
\Sigma' = \Sigma \oplus (C,R) = \langle &\mathcal{N}', \mathcal{R}', \Gamma, \Lambda', K', \chi'\rangle
\end{aligned}
$$

where $\mathcal{N}' = \mathcal{N} \cup \{C\}$ and $\mathcal{R}' = \mathcal{R} \cup \{R\}$.

The envelope and invariant set are written $\Lambda'$ and $K'$ because extension may change which disturbances are claimed and which obligations apply: a new component may introduce a concurrency regime the configuration did not previously face, or bring an information-flow invariant into scope that was previously vacuous. Where an architecture fixes its envelope and invariants constitutionally, $\Lambda' = \Lambda$ and $K' = K$; that identity is a property of the regime and should be stated rather than assumed. The carriage allocation $\chi'$ is recomputed in every case.

The extension update $\oplus$ and the formation update $\oplus_F$ of Section 10.6 are distinct: the former enlarges the configuration graph, the latter additionally introduces a composite and its constitutive subgraph.

It does not follow that the extended configuration remains admissible:

$$
\begin{aligned}
&\operatorname{Admissible}_{\Gamma_{\mathrm{val}}}(\Sigma) \; \\
&\land \; \operatorname{Valid}_{\Gamma_{\mathrm{val}}}(C \mid R_C,\Lambda_C,K_C) \; \\
&\land \; \operatorname{Compatible}_{\Gamma_{\mathrm{val}}} \left( \operatorname{src}(R), \operatorname{dst}(R), R \right) \not \\
&\Rightarrow \operatorname{Admissible}_{\Gamma_{\mathrm{val}}}(\Sigma')
\end{aligned}
$$

The extension may create a dependency cycle, resource exhaustion, authority amplification, privacy leakage, correlated failure, semantic contradiction, or an unbounded information path.

Admissibility is therefore non-monotonic under compositional extension.

### 13.3 Local Validity and Global Inadmissibility

Examples include two authorized datasets combining into re-identification (Sweeney, 2002; Narayanan & Shmatikov, 2008); two valid delegations producing authority amplification (Miller, 2006); two safe financial positions creating correlated exposure (Coval, Jurek, & Stafford, 2009); two supported claims yielding an unsupported conclusion; two secure components creating an insecure information-flow path; and two reliable services forming a cyclic failure cascade.

The first and third are documented at length. Data releases satisfying a disclosure standard on their own may still identify individuals once linked against auxiliary records, and statistical de-anonymization succeeds against high-dimensional micro-data even when the release has been perturbed and the adversary's background knowledge is partly mistaken (Sweeney, 2002; Narayanan & Shmatikov, 2008). In structured finance, the tranching of pooled assets substitutes risks that are largely diversifiable for risks that are highly systematic, so positions each assessed as safe may carry an exposure visible only at the level of the combined structure (Coval, Jurek, & Stafford, 2009).

Composition creates a new object of judgment. This configuration-level requirement is one of the ontology's principal differentiators: architectural admissibility cannot generally be recovered by summing local compatibility verdicts.

---

## 14. Constitutional Composability

This paper uses **constitutional** as a technical architectural term.

A constitutional rule is a system-level admissibility constraint governing which identities, authorities, relations, transformations, and effects may receive admission within a compositional regime. The term inherits intuitive force from legal constitutions but is not restricted to political institutions. Constitutional constraints may govern software authorization, evidence custody, engineering safety, organizational jurisdiction, data privacy, resource allocation, and identity continuity.

A system is constitutionally composable when admitted compositions preserve the rules by which the system determines what it is permitted to become. Examples include: no unauthorized authority amplification; no identity collision; no unlogged external effect; no unsupported promotion of claims; no prohibited information flow; no composition beyond resource ceilings; and no admission without adequate lineage.

Miller's work on robust composition and object-capability systems is particularly relevant here because it distinguishes possession of permissions from effective authority and analyzes how composition can create unintended authority (Miller, 2006).

### 14.1 Authority Accumulation and Amplification

**Authority accumulation** is the increase in reachable authority produced as valid delegations, references, or capabilities are combined. Accumulation is not necessarily invalid.

**Authority amplification** occurs when composition produces authority not justified by the participants' legitimate grants, scopes, or delegation paths.

The constitutional task is not to prohibit every increase in effective capability. It is to distinguish authorized accumulation from unauthorized amplification.

### 14.2 Refusal

A system unable to refuse invalid composition is not maximally composable. It is merely permissive.

Selective refusal preserves the meaning of valid composition.

---

## 15. Worked Profiles

Three profiles apply the diagnostic record across materially unlike domains. The first two trace capabilities that hold; the third traces one that fails. Each is summarized here, and the complete records appear in Appendix C.

### 15.1 Interlocking Bricks

Five claims trace the same physical system through progressively stronger capabilities.

**Alignment.** Compatible bricks establish repeatable position and orientation on a regular grid. Carriage is almost entirely component-intrinsic geometry, and the claim holds only for undeformed parts within manufacturing tolerance.

**Retention.** Joined bricks remain connected under inversion and moderate handling. Carriage shifts to the interface: interference fit, friction, and material elasticity. This is the transition at which the environment stops doing the preserving work.

**Invariant-bearing capacity.** The connection transfers limited tension, compression, and shear while preserving attachment and bounded deformation. Carriage becomes distributed across material, interface geometry, connection count, and the higher-order load path, and the residual assumption is that larger structures distribute load within local connection capacity.

**Standing.** A stable subassembly may be transported and reintegrated as one bounded component. The claim depends on internal joints that are no longer individually inspected, which is precisely why hidden internal damage is its characteristic failure condition.

**Recursive closure.** The subassembly may participate in a larger structure, provided higher-order loads remain within inherited limits and exposed interfaces are not exhausted.

The brick system's capability arises from a profile combining regular geometry, retention, bounded load transfer, reversibility, substitutability, standing, and preserved external interfaces.

### 15.2 Evidence Module

The same five stages apply to a bounded research object containing a claim, observations, cited sources, an inference warrant, uncertainty, provenance, and version identity.

**Alignment.** The module can enter an analysis using compatible definitions, units, and temporal scope. Carriage rests on schemas, metadata, and receiving-context validation.

**Retention.** The claim remains bound to its evidence after copying or transfer. Carriage rests on content identity, citations, custody records, and archival systems. The residual assumption, that referenced evidence remains retrievable, is the one most often violated in practice.

**Invariant-bearing capacity.** The module preserves warranted meaning under summarization and incorporation into a larger argument. The invariants are scope, uncertainty, provenance, contradiction status, and warrant; the failures are scope expansion, certainty inflation, and contradiction suppression.

**Standing.** The package may be relied upon as a bounded analytical component within its declared question and evidentiary standard. Standing here requires inspectability of sources, transformations, assumptions, warrants, and uncertainty.

**Recursive closure.** The module may support a higher-order conclusion without losing its original support conditions, provided the receiving analysis imports assumptions, uncertainty, and contradiction status rather than only the conclusion.

The structural correspondence is exact even though no mechanism is shared. Text may be easy to copy while justification dissolves.

Syntactic portability is not epistemic composability.

### 15.3 A Failing Profile: Linked Datasets

The two profiles above trace capabilities that hold. A framework for compositional validity should also show what a failure looks like when recorded through the same instrument, and where the record locates it.

Consider a configuration containing two released datasets, prepared by different custodians, each satisfying a disclosure standard on its own terms.

**The component records, as filed.** Dataset $A$ publishes coarsened demographic attributes. Its claim is that no individual is identifiable from the release alone; its envelope covers inspection of that release in isolation; its invariant is non-identifiability; its evidence is a disclosure check performed against the release. Dataset $B$ publishes fine-grained behavioral records under a pseudonymous key, with a corresponding claim, envelope, and check. Each would pass an audit of the component it describes. Whether each is also correct depends on how its claim is read, and the two readings yield different diagnoses; they are separated below.

**The formation.** A third party joins the two on shared quasi-identifiers. A composite forms. Nothing prevents it, formation being ontic (Section 4.2); no admission was sought, and under a component-scoped regime none was required, since both parts were released as public artifacts.

**Which conjunct fails.** The composite claim would be that the join preserves non-identifiability. It does not. But the defect is not where component-scoped assurance looks for it:

* $\operatorname{Compatible}$ holds: the schemas align and the join is well formed.
* $\operatorname{Forms}$ holds: the composite exists.
* $\operatorname{Preserves}$ fails for the composite, though it held for each part.
* Neither component's validity judgment was wrong. Each remains valid for its own $\varrho$, $\Lambda$, and $K$.

This is the configuration-level pattern of Section 13.2: admissible parts, a locally compatible relation, an inadmissible whole (Sweeney, 2002; Narayanan & Shmatikov, 2008).

**Two readings, two failure paths.** Whether the component records are defective depends on how their claims are read. The framework separates the readings rather than blending them, because they locate the defect in different places.

*Case A: isolation-scoped claims.* Read strictly, each record claims only non-identifiability from its own release, with an envelope covering inspection of that release alone. On those terms the records are valid and $A_{\mathrm{res}}$ is correctly empty: auxiliary linkage lies outside the declared envelope, so its absence is not an assumption the claim depends upon. Each component holds standing for the purpose its record declares. The failure is then twofold, and neither part of it is a component defect. First, a standing-purpose mismatch: users and institutions relied upon the releases for a broader purpose --- non-identifiability in the world --- than any record covered, and standing is purpose-indexed (Section 8.3). Second, no configuration-level record or admission gate existed for the join, so the broader question was never anyone's to answer.

*Case B: public non-identifiability claims.* Read as such releases are often in fact presented --- as assurances that individuals will remain non-identifiable following public release --- the envelope becomes the real data environment, and the diagnosis changes. The absence of a linkable auxiliary release is then a genuine residual assumption; the invariant is carried partly by $\chi_E$ rather than by the coarsening or keying alone; and leaving $A_{\mathrm{res}}$ empty is the hidden externalization of Section 16.3. On this reading the component record is defective before any join occurs, because it attributes to $\chi_G$ a share of the carriage that the environment was in fact supplying.

The two cases are not a hedge. They are distinct failure paths that a component audit cannot tell apart and this record can: in Case A the paperwork is correct and the reliance placed upon it is not; in Case B the paperwork itself misstates where the constraint is carried.

**What both readings share.** Under either, publishing the second dataset changed $E_{\Gamma}$, and protection that had been adequate across the pair became inadequate without either component changing at all. Under either, no party was positioned to notice this from its own record alone. And under either, the configuration-level judgment --- the one predicate ranging over $\Sigma$ rather than over $\mathcal{N}$ --- was never made, because no procedure required it.

**What the framework prescribes.** Not that either release should have been forbidden. That the join is an event requiring its own judgment: a formation whose admissibility is evaluated over the configuration, against an invariant that nothing in either part was carrying. Where no such gate exists, a configuration acquires a defect no component-scoped certificate could have detected, and every party's paperwork remains in order.

---

## 16. Failure Modes

**16.1 False composability.** Components appear compatible while hidden assumptions conflict.

**16.2 Environmental subsidy.** Continuous external repair or supervision creates the appearance of robust composition.

**16.3 Hidden externalization.** A component exports constraint-bearing work without declaring it as an assumption.

**16.4 Destructive composition.** The act of joining destroys prior interfaces, identities, or future compositional options.

**16.5 Premature standing.** A boundary is trusted before internal organization supports its exposed guarantees.

**16.6 Unjustified exposure.** A composite is published, packaged, or advertised as a component before it has earned standing for the purpose implied by the exposure.

**16.7 Nonclosing composition.** The result functions but cannot participate in further formation where further formation is required.

**16.8 Semantic drift.** Interfaces remain stable while their meanings diverge.

**16.9 Invariant leakage.** Local behavior is preserved by exporting costs, failures, or risks to the environment.

**16.10 Recursive fragility.** Small losses at each layer accumulate into major higher-order unreliability.

**16.11 Mediator capture.** An intermediary becomes indispensable and acquires unreviewed control over the relation.

**16.12 Combinatorial explosion.** Individually valid relations create too many configurations to evaluate safely.

**16.13 Authority amplification.** Valid permissions or delegations combine into an effect that no participant was entitled to authorize.

**16.14 Temporal decay.** A once-valid composition remains active after its evidence, assumptions, dependencies, or authority have changed.

**16.15 Formation without validity.** A composite forms and becomes operational before invariant preservation has been established.

**16.16 Admission without standing.** A regime authorizes reliance upon an object whose boundary, guarantees, or evidence do not justify treating it as a component.

---

## 17. Design Principles

1. **Separate proposal, formation, validity, and admission.** A relation can be proposed without forming, form without being valid, and be valid without being admitted.

2. **Separate exposure from justified exposure.** Publishing a boundary is an act; earning it is a status.

3. **Identify constraint carriage.** Determine what carries the work required to realize and preserve each invariant.

4. **Declare the disturbance envelope.** A composability claim without an envelope is generally overbroad.

5. **Separate retention from invariant preservation.** A relation may persist while meaning, safety, alignment, or authority fails.

6. **Internalize proportionally.** Move constraint inward only when the new allocation better fits the intended use.

7. **Expose residual assumptions.** Do not hide burdens that remain with the context.

8. **Treat mediators as components.** Adapters, translators, and gateways require their own evidence and failure analysis.

9. **Preserve reversibility where evolution matters.** Avoid destructive bonds when repair, substitution, or learning is expected.

10. **Grant standing only when earned.** Packaging is not proof of bounded reliability.

11. **Preserve constitutive lineage through abstraction.** Higher-order objects should retain access to the components and relations supporting their guarantees.

12. **Test configurations, not merely parts.** Valid components may form an inadmissible architecture.

13. **Evaluate relation paths.** Accumulated consequences may remain invisible at individual interfaces.

14. **Make refusal native.** Reliable composability requires rejection of invalid combinations.

15. **Govern evidentiary, standing, and admission status separately.** Loss of admission does not imply loss of capability; loss of standing requires failure of justified bounded reliance; staleness of evidence requires neither.

16. **Match evidence to consequence.** Expansive, irreversible, or hazardous compositions require stronger support.

---

## 18. Related Work and Differential Contribution

### 18.1 Hierarchy, Decomposability, and Aggregativity

Simon's account of hierarchy and near-decomposability explains how stable intermediate forms enable complex systems to develop and remain intelligible (Simon, 1962). Alexander's work on form and pattern examines how local relations participate in larger coherent structures (Alexander, 1964; Alexander et al., 1977). Wimsatt's treatment of aggregativity, emergence, and limited decomposition bears directly on the distinction between mere collections and wholes whose properties depend upon organization (Wimsatt, 2007).

The present framework inherits the importance of hierarchy but asks what carries the constraints by which an intermediate form remains stable enough to function as a component.

### 18.2 Modularity and Product Architecture

Parnas emphasized decomposition according to information-hiding decisions rather than arbitrary subdivision (Parnas, 1972). Baldwin and Clark developed modularity through shared design rules supporting independent development and substitution (Baldwin & Clark, 2000). Ulrich analyzed product architecture through the mapping of functional elements to physical components and the specification of interfaces among them (Ulrich, 1995). Component-software theory likewise examines interfaces, replaceability, and assembly (Szyperski, 2002).

Constraint-Bearing Composability distinguishes structural boundedness from standing and asks what justifies reliance upon the exposed boundary.

### 18.3 Contracts, Interfaces, and Program Correctness

Hoare's axiomatic treatment of programs established a foundational form of reasoning from preconditions to postconditions (Hoare, 1969). Meyer's design-by-contract approach brought explicit assumptions and guarantees into software component design (Meyer, 1992). Interface automata and contract-based design formalize compatibility, assumptions, guarantees, refinement, and composition more rigorously than this conceptual paper attempts (de Alfaro & Henzinger, 2001; Benveniste et al., 2018).

The present framework does not replace those formalisms. It distinguishes formation from validity, constraint carriage from interface syntax, environmental retention from interface retention, capability from evidence and admission, exposure from justified exposure, encapsulation from standing, and local compatibility from architectural admissibility.

### 18.4 Architectural Mismatch and Local-to-Global Failure

Garlan, Allen, and Ockerbloom showed that apparently reusable software components may fail to integrate because of hidden architectural assumptions (Garlan, Allen, & Ockerbloom, 1995).

The present framework generalizes the problem. Local validity may fail under extension because composition alters topology, reallocates constraint, creates new paths, changes scale, and introduces invariants visible only at configuration level.

### 18.5 Robust Composition and Authority

Miller's account of robust composition addresses the relationship between access control, concurrency, object capabilities, and authority (Miller, 2006). This work is especially relevant to constitutional composability because it shows that authority cannot be inferred merely from nominal permissions and that composition may create unintended effective power.

Constraint-Bearing Composability treats authority amplification as one instance of a broader pattern: locally valid relations may combine into a globally inadmissible configuration.

### 18.6 Differential Contribution

The framework is not reducible to contract theory, interface automata, modularity theory, or hierarchy theory, because those traditions generally begin with components, boundaries, or interfaces already sufficiently individuated to model.

Constraint-Bearing Composability begins earlier and ranges more broadly. It asks whether objects are merely aggregated or genuinely composed; whether a proposed relation actually forms; what carries the realizing and preserving constraints; whether the formed composite preserves its designated invariants; whether exposure of its boundary is justified; and whether the complete configuration remains admissible across scale and time.

---

## 19. What This Framework Does Not Claim

The framework does not claim that all composability lies on one universal ladder; that internal carriage is superior to environmental support; that all domains share identical material mechanisms; or that a conceptual profile replaces domain-specific testing or proof.

It does not claim to introduce assume-guarantee contracts; that modularity guarantees compositionality; that encapsulation guarantees standing; or that certification creates capability.

It does not claim that compatibility is required for a composite to form; that exposure implies standing; that admission and standing are the same status; that valid components imply an admissible configuration; that structural role or nesting depth implies reliability or legitimacy; that every composition requires constitutional review; that every relation should be reversible; or that composability can be represented by one universal scalar measure.

The framework supplies a shared structure for diagnosis. It does not erase domain expertise.

---

## 20. Scope and Conditions of Inadequacy

This paper advances definitional, descriptive, and normative claims, and each class should be judged by its own standard.

**Definitional claims.** The paper distinguishes aggregation, realization, constitutive relation, proposal, formation, validity, compatibility, retention, invariant preservation, exposure, justified exposure, standing, admission, recursive closure, architectural admissibility, constraint carriage, internalization, externalization, and carriage adequacy. These should be judged by clarity, coherence, and explanatory usefulness.

**Descriptive claims.** The paper proposes that structurally similar compositional problems recur across physical, computational, epistemic, institutional, and economic systems. These should be evaluated through comparative application.

**Normative claims.** The paper argues that consequential compositions should distinguish formation from validity and exposure from standing, declare disturbance envelopes, expose residual assumptions, preserve constitutive lineage, represent mediators explicitly, support refusal, undergo review proportional to consequence, and remain subject to demotion and revocation. These should be judged by whether they improve reliability, intelligibility, adaptability, or legitimacy.

**Conditions of inadequacy.** The ontology would require revision if important compositional distinctions cannot be expressed through its primitives; if the constitutive-relation criterion fails to distinguish aggregations from compositions; if realization cannot be separated from preservation in practice; if constraint carriage fails to discriminate among materially different compositions; if standing adds no explanatory value beyond encapsulation; if mediated composition cannot be analyzed consistently; if evidentiary status, standing, and admission cannot be kept distinct; if formation and validity cannot be separated without contradiction; if cross-domain application depends only upon metaphor; or if independent analysts cannot use the diagnostic record to reach meaningfully comparable judgments.

The last of these is an empirical claim rather than a conceptual one, and it is directly testable: independent analysts applying the record of Appendix B to the same documented cases, with agreement measured field by field. Such a study is planned, and the framework should be treated as unvalidated on this point until it has been carried out.

The framework should therefore be treated as a candidate conceptual component: bounded, inspectable, revisable, and subject to the demands it places upon other compositions.

---

## 21. Conclusion

Constraint-Bearing Composability provides five practical gains. It separates the existence of a composite from its validity and admission. It distinguishes realizing a whole from preserving one. It reveals where the work of maintaining a composition is actually carried. It distinguishes structural position from justified standing, and exposure from the entitlement to be relied upon. And it explains why locally valid parts may still form a globally inadmissible configuration.

These distinctions support better interface design, more honest abstraction, stronger evidence practices, and constitutional governance of higher-order systems. The decisive question is not merely whether parts can be joined, nor whether every constraint can be moved inward, but which mechanisms and boundaries are capable, inspectable, and entitled to carry each constraint required by the whole.

Parts become a structure when their relations can bear the present; they become an architecture when those relations can bear what comes next without surrendering the conditions that made the earlier structure worthy of trust.

---

## Appendix A: Compact Diagnostic Model

## A.1 Primitive Configuration

$$
\begin{aligned}
\Sigma = \langle &\mathcal{N}, \mathcal{R}, \Gamma, \Lambda, K, \chi\rangle
\end{aligned}
$$

| Primitive | Diagnostic question |
| --- | --- |
| Components $\mathcal{N}$ | What bounded entities participate? |
| Relations $\mathcal{R}$ | How do they interact? |
| Context $\Gamma$ | What environmental, architectural, and governance conditions apply? |
| Envelope $\Lambda$ | Which disturbances must the composition survive? |
| Invariants $K$ | What properties must remain true? |
| Carriage $\chi$ | What carries the work of realizing and preserving those properties? |

## A.2 Judgment Layers and Cross-Cutting Statuses

The four judgment layers concern events and judgments about events:

- **Layer:** Proposal  
  **Question:** What relation is intended?  
  **Context:** $\Gamma_{\mathrm{val}}$

- **Layer:** Formation  
  **Question:** What composite actually formed?  
  **Context:** none; formation is ontic

- **Layer:** Validity  
  **Question:** Which invariants does it preserve under the envelope?  
  **Context:** $\Gamma_{\mathrm{val}}$

- **Layer:** Admission  
  **Question:** Has a governing regime permitted reliance?  
  **Context:** $\Gamma_{\mathrm{adm}}$

The following are statuses rather than layers. They are not stages in the formation sequence and may change independently of it:

| Status | Question |
| --- | --- |
| Evidentiary status | How well is the capability claim supported? |
| Standing status | Is the boundary justified for a declared purpose? |
| Admission status | What is the current lifecycle state of the permission? |

## A.3 Core Predicates

- **Predicate:** $\operatorname{Compatible}_{\Gamma_{\mathrm{val}}}(C_1,C_2,R)$  
  **Meaning:** The proposed binary relation satisfies applicable local requirements

- **Predicate:** $\operatorname{Forms}(C_1,C_2,R,C_3)$  
  **Meaning:** The relation is instantiated and produces $C_3$

- **Predicate:** $\operatorname{Realizes}_{\Gamma_{\mathrm{val}}}(X,K)$  
  **Meaning:** The subject establishes a whole in which $K$ initially holds

- **Predicate:** $\operatorname{Preserves}_{\Gamma_{\mathrm{val}}}(X,K,\Lambda)$  
  **Meaning:** Required invariants survive the envelope for the subject $X$

- **Predicate:** $\operatorname{Retains}_{\Gamma_{\mathrm{val}}}(C_3,R,\Lambda)$  
  **Meaning:** The formed relation persists throughout the envelope

- **Predicate:** $\operatorname{Valid}_{\Gamma_{\mathrm{val}}}(C_3 \mid \varrho,\Lambda,K)$  
  **Meaning:** The composite preserves its designated invariants; $\varrho$ is a relation or relation set

- **Predicate:** $\operatorname{Standing}_{\Gamma_{\mathrm{val}}}(C,p)$  
  **Meaning:** Derived over an applicable record: validity, evidence adequacy, boundary adequacy for $p$

- **Predicate:** $\operatorname{JustifiedExposure}_{\Gamma_{\mathrm{val}}}(\Sigma_F,C_3,p)$  
  **Meaning:** Exposure of the composite boundary is warranted

- **Predicate:** $\operatorname{Admitted}_{\Gamma_{\mathrm{adm}}}(C,p,\mathcal{E}_A)$  
  **Meaning:** Reliance is permitted under the governing regime

- **Predicate:** $\operatorname{Admissible}_{\Gamma_{\mathrm{val}}}(\Sigma)$  
  **Meaning:** The complete configuration satisfies system-level constraints

The subject $X$ of $\operatorname{Realizes}$ and $\operatorname{Preserves}$ may be a component, a composite, a relation set paired with its participants, or a configuration. Scope is carried by the subject, not by predicate arity.

## A.4 Entity Records

**Component.**

$$
\begin{aligned}
C = \langle &\operatorname{id}, B, F, A, G, \Lambda, \mathcal{E}_C, V\rangle
\end{aligned}
$$

| Field | Meaning |
| --- | --- |
| $\operatorname{id}$ | Controlled identity |
| $B$ | Boundary |
| $F$ | Exposed interfaces |
| $A$ | Assumptions exported to the context |
| $G$ | Guarantees exposed to external actors |
| $\Lambda$ | Declared disturbance envelope |
| $\mathcal{E}_C$ | Component evidence object |
| $V$ | Version and lifecycle state |

**Relation.**

$$
\begin{aligned}
R = \langle &C_1, C_2, \tau, \mu, \Lambda_R, K_R, \chi(R), \\
&\mathcal{E}_R\rangle
\end{aligned}
$$

| Field | Meaning |
| --- | --- |
| $C_1,C_2$ | Participants |
| $\tau$ | Interface correspondence |
| $\mu$ | Relation mode |
| $\Lambda_R$ | Relation-specific disturbance envelope |
| $K_R$ | Relation-specific invariant set |
| $\chi(R)$ | Relation-level carriage allocation |
| $\mathcal{E}_R$ | Relation evidence object |

**Context and projections.**

$$
\Gamma
=
\left\langle
E_{\Gamma},
K_{\Gamma},
P_{\Gamma},
H_{\Gamma}
\right\rangle
\qquad
\Gamma_{\mathrm{val}}
=
\left\langle
E_{\Gamma},
K_{\Gamma},
H_{\Gamma}
\right\rangle
\qquad
\Gamma_{\mathrm{adm}}
=
\left\langle
P_{\Gamma},
K_{\Gamma},
H_{\Gamma}
\right\rangle
$$

**Evidence object.**

$$
\mathcal{E}
=
\left\langle
s,
c,
m,
r,
u,
\pi
\right\rangle
$$

**Diagnostic record.**

$$
\begin{aligned}
\mathcal{D} = \langle &q, \Lambda, K, \chi, \mathcal{E}, A_{\mathrm{res}}, \Phi, \\
&V\rangle
\end{aligned}
$$

## A.5 Notation Index

- **Symbol:** $\Sigma$  
  **Meaning:** Compositional configuration  
  **Defined in:** 2

- **Symbol:** $\mathcal{N},\mathcal{R}$  
  **Meaning:** Component and relation sets  
  **Defined in:** 2

- **Symbol:** $\Gamma$  
  **Meaning:** Context  
  **Defined in:** 2.3

- **Symbol:** $\Gamma_{\mathrm{val}},\Gamma_{\mathrm{adm}}$  
  **Meaning:** Validity and admission projections of the context  
  **Defined in:** 2.3

- **Symbol:** $E_{\Gamma},K_{\Gamma},P_{\Gamma},H_{\Gamma}$  
  **Meaning:** Contextual guarantees; architectural invariants; admission rules; history  
  **Defined in:** 2.3

- **Symbol:** $\Lambda$  
  **Meaning:** Disturbance envelope  
  **Defined in:** 2.4

- **Symbol:** $K$  
  **Meaning:** Required invariants  
  **Defined in:** 2.5

- **Symbol:** $P$  
  **Meaning:** Property set  
  **Defined in:** 2.5

- **Symbol:** $\chi$  
  **Meaning:** Carriage allocation, loci $\chi_O$ through $\chi_Q$  
  **Defined in:** 2.6

- **Symbol:** $\chi(C),\chi(R),\chi(\Sigma)$  
  **Meaning:** Carriage at component, relation, configuration granularity  
  **Defined in:** 6.1

- **Symbol:** $\mu$  
  **Meaning:** Relation mode  
  **Defined in:** 2.2

- **Symbol:** $\tau$  
  **Meaning:** Interface correspondence  
  **Defined in:** A.4

- **Symbol:** $\mathcal{S}$  
  **Meaning:** Candidate minimal sufficient relation set  
  **Defined in:** 3.3

- **Symbol:** $\Theta(\mathcal{S})$  
  **Meaning:** Conjunction of realization and preservation for $\mathcal{S}$  
  **Defined in:** 3.3

- **Symbol:** $w$  
  **Meaning:** Constitutive or containment path within a configuration  
  **Defined in:** 8.2

- **Symbol:** $\operatorname{RC}(X)$  
  **Meaning:** Relational capacity profile  
  **Defined in:** 8.1

- **Symbol:** $\rho,\delta$  
  **Meaning:** Preservation margin; degradation behavior  
  **Defined in:** 8.1

- **Symbol:** $\operatorname{Roles}_{\Sigma}(X)$  
  **Meaning:** Structural roles, set-valued  
  **Defined in:** 8.2

- **Symbol:** $\operatorname{Depth}_{\Sigma}(X,w)$  
  **Meaning:** Nesting depth along constitutive path $w$  
  **Defined in:** 8.2

- **Symbol:** $p$  
  **Meaning:** Declared purpose  
  **Defined in:** 4.4, 8.3

- **Symbol:** $\mathcal{D}$  
  **Meaning:** Diagnostic record  
  **Defined in:** 8.4

- **Symbol:** $\operatorname{Applies}(\mathcal{D},C,p)$  
  **Meaning:** The record's subject is $C$ and its claim covers $p$  
  **Defined in:** 8.3

- **Symbol:** $\operatorname{Covers}(q,p)$  
  **Meaning:** The capability claim extends to the purpose  
  **Defined in:** 8.3

- **Symbol:** $\operatorname{Constitution}(C)$  
  **Meaning:** Constitutive relation set retained with $C$  
  **Defined in:** 8.3, 10.6

- **Symbol:** $\varrho$  
  **Meaning:** Relation or relation set argument of validity  
  **Defined in:** 4.3

- **Symbol:** $\mathcal{E}$  
  **Meaning:** Evidence object, scoped $\mathcal{E}_C,\mathcal{E}_R,\mathcal{E}_A$  
  **Defined in:** 8.5

- **Symbol:** $q$  
  **Meaning:** Capability claim  
  **Defined in:** 8.4

- **Symbol:** $s,c,m,r,u,\pi$  
  **Meaning:** Evidence subject, claim, method, result, uncertainty, provenance  
  **Defined in:** 8.5

- **Symbol:** $A_{\mathrm{res}},\Phi,V$  
  **Meaning:** Residual assumptions; failure conditions; version  
  **Defined in:** 8.4

- **Symbol:** $\operatorname{form}_{R}$  
  **Meaning:** Partial formation operator  
  **Defined in:** 10.5

- **Symbol:** $\oplus_F$  
  **Meaning:** Formation update, introduces a composite  
  **Defined in:** 10.6

- **Symbol:** $\oplus$  
  **Meaning:** Extension update, adds component and edge  
  **Defined in:** 13.2

- **Symbol:** $F_i,A_i,G_i$  
  **Meaning:** Interfaces, assumptions, guarantees of $C_i$  
  **Defined in:** A.4

- **Symbol:** $\operatorname{src},\operatorname{dst}$  
  **Meaning:** Relation endpoints  
  **Defined in:** 13.1

**Note on schematic operators.** Several operators are specified by their role rather than by a general definition: $\operatorname{AggregateCarriage}$ (6.1), $\operatorname{AdequateEvidence}$, $\operatorname{AdequateBoundary}$, and $\operatorname{Covers}$ (8.3), $\operatorname{ProjectInterfaces}$ (10.7), and $\operatorname{Residual}$ and $\operatorname{Consequences}$ (10.9). Each must be instantiated for a domain before the framework can be applied there, and each marks the point at which domain-specific engineering, proof, measurement, or governance practice enters. Their schematic status is deliberate: supplying universal definitions would commit the ontology to domain assumptions it explicitly disclaims in Section 19.

---

## Appendix B: Diagnostic Record Template

**Capability claim $q$:** what the composition is claimed to realize, preserve, or accomplish.

**Disturbance envelope $\Lambda$:** conditions throughout which the claim must hold.

**Required invariants $K$:** properties that must remain true.

**Constraint carriage $\chi$:** observer or container, environment, intrinsic structure, interface, mediator, internal organization, architecture, constitution.

**Evidence $\mathcal{E}$:** method $m$, result $r$, uncertainty $u$, provenance $\pi$.

**Residual assumptions $A_{\mathrm{res}}$:** what the context must continue to supply.

**Failure conditions $\Phi$:** what invalidates or demotes the claim.

**Version and lifecycle state $V$:** applicable identity, revision, and status.

**Structural roles and depth:** $\operatorname{Roles}_{\Sigma}(X)$, and $\operatorname{Depth}_{\Sigma}(X,w)$ for each constitutive path $w$ by which the object is reached.

**Evidentiary status:** unsupported, preliminary, demonstrated, independently supported, contradicted, stale.

**Standing status:** candidate, qualified, constrained, demoted, lost.

**Admission status:** pending, admitted, active, suspended, revoked, expired, retired.

---

## Appendix C: Complete Worked Records

## C.1 Interlocking Bricks

### C.1.1 Alignment

**$q$:** Compatible bricks establish repeatable position and orientation on a regular grid.
**$\Lambda$:** Ordinary assembly using undeformed components within specified manufacturing tolerances.
**$K$:** Geometric correspondence and permitted orientation.
**$\chi$:** Component-intrinsic geometry and interface geometry.
**$m$:** Dimensional inspection and repeated assembly trials.
**$r$:** Repeatable fitting and stable grid alignment.
**$u$:** Variation from manufacturing tolerances, wear, contamination, deformation.
**$A_{\mathrm{res}}$:** Materials remain dimensionally stable and compatible.
**$\Phi$:** Warping, obstruction, incompatible scale, partial engagement.
**$V$:** Applicable brick geometry and manufacturing specification.

### C.1.2 Retention

**$q$:** Joined bricks remain connected under inversion and moderate handling.
**$\Lambda$:** Forces below the tested separation threshold.
**$K$:** Continued attachment and bounded misalignment.
**$\chi$:** Interface interference, friction, material elasticity, geometry.
**$m$:** Pull-force testing, inversion trials, repeated connection cycles.
**$r$:** Observed persistence under specified handling conditions.
**$u$:** Wear, material age, temperature, variation in engagement force.
**$A_{\mathrm{res}}$:** Components are fully engaged and undamaged.
**$\Phi$:** Excessive load, heat deformation, incomplete engagement, accumulated wear.
**$V$:** Applicable component design and material revision.

### C.1.3 Invariant-Bearing Capacity

**$q$:** The connection transfers limited tension, compression, and shear while preserving attachment and bounded deformation.
**$\Lambda$:** Model-scale use within tested geometry and loading.
**$K$:** Attachment, geometric integrity, acceptable deformation.
**$\chi$:** Distributed across material, interface geometry, connection count, higher-order load path.
**$m$:** Mechanical testing and controlled structural trials.
**$r$:** Measured load transfer and observed structural persistence.
**$u$:** Scale effects, concentrated loads, fatigue, hidden weak joints.
**$A_{\mathrm{res}}$:** Higher-order structures distribute loads within local connection capacity.
**$\Phi$:** Leverage, fatigue, unsupported span, concentrated load, accumulated tolerance.
**$V$:** Specific assembly geometry, connection pattern, material state.

### C.1.4 Standing

**$q$:** A stable subassembly may be transported and reintegrated as one bounded component.
**$\Lambda$:** Handling below the weakest internal joint's failure threshold.
**$K$:** Internal organization, identity, external interface availability.
**$\chi$:** Internal joints, subassembly geometry, handling procedure, exposed interfaces.
**$m$:** Repeated manipulation, inspection, transport, reintegration.
**$r$:** The subassembly remains identifiable and operational across repeated use.
**$u$:** Hidden connections and internal load redistribution.
**$A_{\mathrm{res}}$:** Internal connections remain sound and exposed interfaces remain compatible.
**$\Phi$:** Weak internal joints, exhausted interfaces, geometric distortion, undocumented internal damage.
**$V$:** Identified subassembly revision and component lineage.

### C.1.5 Recursive Closure

**$q$:** The subassembly may participate in a larger structure.
**$\Lambda$:** Higher-order loads remain within inherited limits.
**$K$:** Subassembly identity, interface compatibility, load-path continuity.
**$\chi$:** Shared among subassembly internals, external interfaces, higher-order architecture.
**$m$:** Repeated higher-order composition and load-path inspection.
**$r$:** Successful reuse in larger assemblies.
**$u$:** Accumulated tolerance, interface exhaustion, emergent load concentration.
**$A_{\mathrm{res}}$:** Scale effects do not invalidate lower-order relations.
**$\Phi$:** Interface exhaustion, accumulated misalignment, excessive load, architectural mismatch.
**$V$:** Higher-order configuration and lineage state.

## C.2 Evidence Module

### C.2.1 Alignment

**$q$:** The module can enter an analysis using compatible definitions, units, and temporal scope.
**$\Lambda$:** Transfer into a receiving argument with declared semantic conventions.
**$K$:** Meaningful correspondence of terms, units, entities, timeframes.
**$\chi$:** Schemas, definitions, metadata, receiving-context validation.
**$m$:** Schema validation, unit checking, semantic review.
**$r$:** Established correspondence between source and receiving representations.
**$u$:** Ambiguous terms, incomplete metadata, domain shift.
**$A_{\mathrm{res}}$:** The receiving analysis preserves imported definitions and scope.
**$\Phi$:** Unit mismatch, semantic drift, temporal mismatch, ambiguous terminology.
**$V$:** Applicable schema, terminology, source revision.

### C.2.2 Retention

**$q$:** The claim remains bound to its evidence after copying or transfer.
**$\Lambda$:** Storage, transmission, and reuse preserving provenance metadata.
**$K$:** Evidentiary lineage, content identity, citation correspondence.
**$\chi$:** Content identity, citations, custody records, manifests, archival systems.
**$m$:** Manifest verification, content comparison, citation retrieval.
**$r$:** Stable content identity and retrievable supporting sources.
**$u$:** Source disappearance, mutable content, incomplete archival capture.
**$A_{\mathrm{res}}$:** Referenced evidence remains available or adequately preserved.
**$\Phi$:** Citation loss, source substitution, provenance break, unsupported summary.
**$V$:** Identified evidence-package revision and source state.

### C.2.3 Invariant-Bearing Capacity

**$q$:** The module preserves warranted meaning under summarization and incorporation into a larger argument.
**$\Lambda$:** Transformations that do not strengthen the claim beyond its evidence.
**$K$:** Scope, uncertainty, provenance, contradiction status, warrant.
**$\chi$:** Explicit claim boundaries, inference rules, uncertainty annotations, review, lineage.
**$m$:** Reproducible derivation and independent analytical review.
**$r$:** Reviewers can reconstruct the claim from retained evidence and warrant.
**$u$:** Interpretive disagreement, omitted context, source-selection effects.
**$A_{\mathrm{res}}$:** Receiving analysts respect declared limitations and uncertainty.
**$\Phi$:** Scope expansion, certainty inflation, contradiction suppression, evidence laundering.
**$V$:** Applicable analysis, source set, inference revision.

### C.2.4 Standing

**$q$:** The evidence package may be relied upon as a bounded analytical component.
**$\Lambda$:** Uses within its declared question, scope, and evidentiary standard.
**$K$:** Inspectability of sources, transformations, assumptions, warrants, uncertainty.
**$\chi$:** Internal provenance, review procedures, schema, custody, external admission rules.
**$m$:** Lineage audit, methodological review, independent reconstruction.
**$r$:** Complete and inspectable support for the package's exposed claims.
**$u$:** Unknown omitted evidence and residual model dependence.
**$A_{\mathrm{res}}$:** No material source class has been excluded without disclosure.
**$\Phi$:** Premature abstraction, hidden selection, opaque inference, stale evidence.
**$V$:** Identified evidence-module revision and review state.

### C.2.5 Recursive Closure

**$q$:** The module may support a higher-order conclusion without losing its original support conditions.
**$\Lambda$:** Higher-order analysis imports assumptions, uncertainty, contradiction status.
**$K$:** Evidentiary support conditions and lineage.
**$\chi$:** Dependency graphs, explicit imports, provenance, receiving-architecture rules.
**$m$:** Dependency tracing and reconstruction of the higher-order inference.
**$r$:** The higher-order conclusion remains linked to the module's support conditions.
**$u$:** Interaction among modules and emergent inferential dependencies.
**$A_{\mathrm{res}}$:** The module is not treated as stronger than its validated claim.
**$\Phi$:** Provenance compression, unsupported transitive inference, evidence laundering.
**$V$:** Higher-order analysis revision and dependency state.

## C.3 Failing Profile: Linked Datasets

The first two records below are the component records as each custodian filed them. Both are internally consistent under the isolation-scoped reading of Section 15.3; under the broader reading, both understate their residual assumptions. The third is the configuration record that no party produced, and whose absence is the defect on either reading.

### C.3.1 Dataset A, as Filed

**$q$:** No individual is identifiable from this release.
**$\Lambda$:** Inspection of the release in isolation.
**$K$:** Non-identifiability of individuals.
**$\chi$:** Recorded as component-intrinsic coarsening of demographic attributes.
**$m$:** Disclosure check against the release.
**$r$:** No individual isolated by the check.
**$u$:** Sensitivity of the check to attribute granularity.
**$A_{\mathrm{res}}$:** Recorded as empty. Correct under the isolation-scoped reading; understated under the broader reading.
**$\Phi$:** Insufficient coarsening; unique attribute combinations.
**$V$:** Release revision and coarsening parameters.

### C.3.2 Dataset B, as Filed

**$q$:** No individual is identifiable from this release.
**$\Lambda$:** Inspection of the release in isolation.
**$K$:** Non-identifiability of individuals.
**$\chi$:** Recorded as pseudonymous keying of behavioral records.
**$m$:** Disclosure check against the release.
**$r$:** No individual isolated by the check.
**$u$:** Sensitivity of the check to record sparsity.
**$A_{\mathrm{res}}$:** Recorded as empty. Correct under the isolation-scoped reading; understated under the broader reading.
**$\Phi$:** Key reversal; sparse high-dimensional records.
**$V$:** Release revision and keying scheme.

### C.3.3 The Linked Configuration, as It Should Read

**$q$:** The join of $A$ and $B$ on shared quasi-identifiers preserves non-identifiability.
**$\Lambda$:** Any environment in which both releases, or either release and comparable auxiliary data, are simultaneously available to one party.
**$K$:** Non-identifiability of individuals across the configuration.
**$\chi$:** At configuration scale, no declared mechanism carries the invariant. Neither the coarsening of $A$ nor the keying of $B$ extends to the joined data. Whatever protection existed across the pair was environmental: the absence of the linkage that the join itself supplies. Publication of the second release removed that carrier without altering either part.
**$m$:** Linkage analysis across the released pair, not disclosure checking within either.
**$r$:** Individuals identifiable in the joined data.
**$u$:** Extent of further auxiliary data available to an adversary; whether other unlinked releases carry the same latent dependency.
**$A_{\mathrm{res}}$:** That no further auxiliary release supplies additional linkage --- an assumption no party can support, since none controls the environment it refers to.
**$\Phi$:** Any release, by any party, that supplies the missing linkage; equivalently, any change to $E_{\Gamma}$ that removes the environmental carrier.
**$V$:** The configuration as of the second release; both component revisions unchanged.

Under the isolation-scoped reading, the component records are not corrected by this analysis: they remain accurate about their own subjects, and the defect is the missing third record together with the reliance placed upon the first two. Under the broader reading, the component records additionally understate their residual assumptions. What the configuration record supplies on either reading is the entry no component record had a field for: at the scale of the join, the carrier of the invariant was never inside either component, and no party was positioned to notice that from its own paperwork alone.

---

## Appendix D: Provisional Vocabulary

**Admission**
An authoritative decision permitting use or reliance within a governing regime.

**Aggregation**
Common containment, proximity, or membership without a constitutive relation among the aggregated members.

**Architectural admissibility**
Satisfaction by a complete configuration of system-level and history-sensitive constraints, evaluated under the validity projection of the context.

**Capability**
What a composition can realize or preserve within a declared disturbance envelope.

**Carriage adequacy**
The ability of a constraint-carriage allocation to preserve designated invariants throughout the disturbance envelope.

**Compatibility**
Satisfaction of the applicable local requirements for an intended relation.

**Composability**
The capability of components to enter valid compositional relations under declared conditions.

**Composition**
A formed whole whose constitutive relations realize and preserve the properties by which the whole is identified or used.

**Compositionality**
The extent to which properties of a whole may be derived or bounded from its components, relations, assumptions, and context.

**Constitutional composability**
Composition that preserves the system-level rules determining which identities, authorities, relations, transformations, and effects may receive admission.

**Constitutive relation**
A relation belonging to at least one minimal relation set that both realizes the relevant invariants and preserves them throughout the disturbance envelope.

**Constraint-Bearing Composability**
The diagnostic ontology developed in this paper for analyzing formation, constraint carriage, realization and preservation, standing, exposure, and architectural admission.

**Constraint carriage**
The allocation of responsibility for preserving a composition among observers or containers, environment, component-intrinsic properties, interfaces, mediators, internal organization, architecture, and constitutional rules.

**Constraint externalization**
A transition in which preserving responsibility moves or is exported outward.

**Constraint internalization**
A transition in which preserving responsibility moves inward toward component-intrinsic structure, an interface, mediator, or internal organization.

**Diachronic composability**
The capability to preserve or validly transform compositional relations across time.

**Disturbance envelope**
The conditions, loads, and changes throughout which a capability claim is intended to remain valid.

**Encapsulation**
Presentation of internal complexity through a bounded exterior.

**Evidence object**
A scoped record of subject, claim, method, result, uncertainty, and provenance.

**Evidentiary status**
The degree of support for a capability claim.

**Exposure**
The act of presenting a composite through a boundary, independent of whether that presentation is warranted.

**Formation**
Instantiation of a relation that produces a resulting composite, regardless of validity or admission.

**Guarantee**
An externally exposed commitment that specified properties will hold under declared assumptions.

**Invariant**
A property required to remain true throughout a compositional event or disturbance envelope.

**Justified exposure**
Exposure of a composite boundary for a purpose for which the composite holds standing.

**Mediated composition**
Composition enabled through an intermediary that translates, transforms, constrains, routes, buffers, or authenticates a relation.

**Nesting depth**
The number of boundary crossings from the outermost boundary of a configuration to an object along a specified constitutive or containment path. Stated per path rather than as a single value.

**Preservation**
Keeping designated properties true throughout a declared disturbance envelope. Preservation is envelope-relative and does not entail realization.

**Property**
Any describable feature of a component, relation, configuration, or history.

**Proposal**
Specification of an intended relation, including participants, mode, envelope, required invariants, and anticipated carriage, prior to and independent of formation.

**Realization**
Bringing a whole and its designated properties into being, such that those properties initially hold. Realization is envelope-free and does not entail preservation.

**Recursive closure**
Eligibility of a formed compositional result to participate in another formation.

**Relational capacity**
The profile of invariants, disturbance envelope, preservation margin, and degradation behavior associated with a relation or composite.

**Residual assumption**
A condition not discharged by the composition and therefore exported to its context.

**Retention**
Persistence of a formed relation throughout a declared disturbance envelope.

**Standing**
The justified eligibility of a composition to be treated as a bounded component for a declared purpose; derived from validity, evidence adequacy, and boundary adequacy.

**Structural role**
The organizational kinds an object occupies within a configuration, drawn from entity, collection, assembly, component, subsystem, system, architecture, and ecology. Set-valued, since one object may occupy several roles at once.

**Validity**
Preservation of designated invariants throughout the declared disturbance envelope under the validity projection of the context.

---

## Corpus-Wide Reference Positioning

This paper argues that composability is commonly treated as a binary property: components either can or cannot be combined. Its nearest external comparison fields are formal, provenance, storage. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Fixity and preservation can keep bytes stable while representation dependencies, executability, interpretation, and institutional custody decay. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** George C. Necula. "Proof-Carrying Code." *POPL '97*, 1997, pp. 106-119. DOI: 10.1145/263699.263712. https://doi.org/10.1145/263699.263712 **Relationship:** Predecessor for binding machine-checkable evidence to executable artifacts; the present paper may demand broader semantic or constitutional obligations.

**[E2]** Xavier Leroy. "Formal Verification of a Realistic Compiler." *Communications of the ACM* 52(7), 2009, pp. 107-115. DOI: 10.1145/1538788.1538814. https://doi.org/10.1145/1538788.1538814 **Relationship:** Predecessor verified-compilation result used to distinguish proven translation preservation from broader governance claims.

**[E3]** Patrick Cousot and Radhia Cousot. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." *POPL '77*, 1977. DOI: 10.1145/512950.512973. https://doi.org/10.1145/512950.512973 **Relationship:** Predecessor formal framework for sound approximation and fixpoint reasoning.

**[E4]** Leslie Lamport. *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Addison-Wesley, 2002. https://lamport.azurewebsites.net/tla/book.html **Relationship:** Predecessor specification discipline for state machines, safety, liveness, and refinement.

**[E5]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E6]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

**[E7]** OpenSSF. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. 2026. https://slsa.dev/spec/v1.2/ **Relationship:** Adjacent software-supply-chain assurance standard, especially relevant to provenance and verification boundaries.

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

**[A6]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Alexander, C. (1964). *Notes on the Synthesis of Form*. Harvard University Press.

Alexander, C., Ishikawa, S., Silverstein, M., Jacobson, M., Fiksdahl-King, I., & Angel, S. (1977). *A Pattern Language: Towns, Buildings, Construction*. Oxford University Press.

Baldwin, C. Y., & Clark, K. B. (2000). *Design Rules, Volume 1: The Power of Modularity*. MIT Press.

Benveniste, A., Caillaud, B., Nickovic, D., Passerone, R., Raclet, J.-B., Reinkemeier, P., Sangiovanni-Vincentelli, A., Damm, W., Henzinger, T. A., & Larsen, K. G. (2018). Contracts for system design. *Foundations and Trends in Electronic Design Automation, 12*(2--3), 124--400.

Coval, J., Jurek, J., & Stafford, E. (2009). The economics of structured finance. *Journal of Economic Perspectives, 23*(1), 3--25.

de Alfaro, L., & Henzinger, T. A. (2001). Interface automata. In *Proceedings of the 8th European Software Engineering Conference Held Jointly with the 9th ACM SIGSOFT International Symposium on Foundations of Software Engineering* (ESEC/FSE-9) (pp. 109--120). Association for Computing Machinery.

Garlan, D., Allen, R., & Ockerbloom, J. (1995). Architectural mismatch: Why reuse is so hard. *IEEE Software, 12*(6), 17--26.

Hoare, C. A. R. (1969). An axiomatic basis for computer programming. *Communications of the ACM, 12*(10), 576--580, 583.

Meyer, B. (1992). Applying "design by contract." *Computer, 25*(10), 40--51.

Miller, M. S. (2006). *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control* [Doctoral dissertation, Johns Hopkins University]. Baltimore, MD.

Narayanan, A., & Shmatikov, V. (2008). Robust de-anonymization of large sparse datasets. In *Proceedings of the 2008 IEEE Symposium on Security and Privacy* (pp. 111--125). IEEE Computer Society.

Parnas, D. L. (1972). On the criteria to be used in decomposing systems into modules. *Communications of the ACM, 15*(12), 1053--1058.

Simon, H. A. (1962). The architecture of complexity. *Proceedings of the American Philosophical Society, 106*(6), 467--482.

Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557--570.

Szyperski, C. (2002). *Component Software: Beyond Object-Oriented Programming* (2nd ed.). Addison-Wesley.

Ulrich, K. T. (1995). The role of product architecture in the manufacturing firm. *Research Policy, 24*(3), 419--440.

Wimsatt, W. C. (2007). *Re-Engineering Philosophy for Limited Beings: Piecewise Approximations to Reality*. Harvard University Press.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.21632061](https://doi.org/10.5281/zenodo.21632061)
