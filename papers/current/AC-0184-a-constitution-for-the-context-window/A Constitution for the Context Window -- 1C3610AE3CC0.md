# A Constitution for the Context Window

## Authority, Continuity, and the Governed Construction of Machine Cognition

### The mind may belong to the model; the world it inhabits should answer to the user.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Large language models do not encounter users, projects, institutions, or environments directly. Each provider invocation presents the model with a bounded construction assembled from governing policy, retrieved evidence, runtime observations, persistent memory, tools and capability descriptions, selected history, the current user request, and vendor or base-system instruction.

These source classes form **PROMTHUS**:

> **P**olicy, **R**etrieval, **O**bservations, **M**emory, **T**ools, **H**istory, **U**ser request, **S**ystem instruction.

PROMTHUS is an inventory, not an authority hierarchy or serialization order. Its sequence serves a mnemonic and Promethean construction; it does not imply that Policy is universally supreme or that later classes possess lower standing. PROMTHUS names the principal materials from which an invocation context is compiled.

To **promthe** an invocation is to subject those materials to constitutional context compilation: governed discovery, authentication, semantic finding, independently derived consequence analysis, contest, adjudication, authorized transformation, budget closure, provider realization, effect authorization, and evidentiary sealing.

This paper proposes constitutional context compilation as a typed authorization, adjudication, and transformation layer between context sources and inference. The compiler governs what may count as context, what may govern inference, what may be disclosed, how admitted context may be transformed, what may cross a provider boundary, which consequences may follow, and what must remain auditable afterward.

The architecture defines the minimum contract required of a **Constitutional Kernel** capable of governing context compilation. Such a kernel must provide an explicit and non-extensible bootstrap basis, identity-bearing root law, governed discovery obligations, authorized amendment, court jurisdiction, non-self-ratification, typed judgment, structurally triggered contest, review and appeal, refusal semantics, independent effect authorization, and witness.

The paper distinguishes a presupposed **Grundnorm Basis** from a positive, executable **Root Constitution** written in **Deterministic Semantic Compiler (DSC)** form. DSC coding means that law is expressed as explicit, canonically serializable, content-identified rules that execute deterministically over admitted structured predicates, rather than as prose whose application depends on interpretation at the moment of use. The Grundnorm Basis identifies the genesis custody and initial standing that any finite constitutional order must presuppose. It is fixed at genesis and cannot later be enlarged by declaration. The Root Constitution makes operational successor law deterministic over admitted structured predicates, inspectable, content-identified, testable, auditable, and mutable only through authorized amendment.

Context-specific law derives from that root. Discovery profiles, calibration profiles, conflict-detection profiles, independence profiles, domain canonicalization profiles, consequence tiers, court procedures, provider-adapter contracts, and effect boundaries all receive standing from law outside the discretion they constrain. Any profile whose declarations bound the scope of scrutiny must be identity-bearing, evidence-class-typed, and adjudicated before use.

Identity itself is layered to avoid a bootstrap circularity. A primitive, exclusion-free **Constitutional Canonical Form (CCaF)**, bound into the genesis recognition machinery, identifies constitutional objects; adjudicated domain profiles govern application material. Every identity is permanently typed by the layer under which it was computed, and relations across layers are typed correspondences rather than collapsible equivalences.

Completeness of governance is made checkable rather than asserted. A **discretion census** over the declared schema and transition registry enumerates every mechanism able to affect identity, authority, admission, scope, scrutiny, conflict detection, transformation, realization, effect permission, or evidentiary claims, and each censused locus must bind to an audit row or a proven reduction to one.

Classifiers do not become lawmakers; their outputs become receipted findings subject to calibration, conservative consequence computation, independent contest, judicial review, appeal, and refusal. The context compiler executes admitted judgments. The Context Intermediate Representation is the identity-bearing product of that governed process, not its source of authority.

The architecture distinguishes six principal failures: context loss, containment loss, authority loss, representation loss, realization loss, and receipt loss. It defines three layers of context identity over two canonicalization layers, strict partial-order precedence, inter-court conflict law, scrutiny-profile adjudication, cross-layer correspondence, governing projections, delegation contracts, autonomous-loop review, availability protections against stay flooding, privacy-preserving receipts, two-phase budget closure, staged conformance, and measurable governance cost.

Its general constitutional proposition is:

> **Every mechanism that determines whether another mechanism is scrutinized must itself be governed by authority external to the discretion it constrains.**

The paper audits the architecture against that proposition by enumerating its discretionary loci, the power held at each locus, the external governor, the evidentiary record, and the failure emitted when governance is absent. The discretion census supplies the enumeration procedure, so the audit's completeness claim rests on a declared schema rather than on architectural omniscience.

The architecture does not prove truth, model understanding, obedience, classifier completeness, contest independence beyond available evidence, profile completeness beyond available evidence, or remote-provider honesty. This paper specifies a narrower conditional assurance claim: a conforming realization may establish, relative to its declared capability surface and evidence, that context was assembled under explicit machine-governance rules, adjudicated through authorized procedures, realized according to an admitted adapter contract, and bound to evidence sufficient for later inspection. The paper itself is a proposal and proof-obligation map; it supplies no implementation-conformance verdict.

A constitutional context layer could unify memory, retrieval, personalization, policy, capability exposure, delegation, and long-running automation within one systems discipline. It would also make durable computational agency portable across replaceable inference providers---where the user or another legitimate custodian actually holds the registry, amendment authority, and receipts on which such portability depends.

## 1. The Problem: More Than Forgetting

The failure commonly described as an AI system "forgetting" is not one failure.

At least six distinct constitutional losses are routinely collapsed into that phrase.

### 1.1 Context loss

Applicable material is absent from the invocation.

Examples include:

* a prior decision is omitted;
* a required artifact is not retrieved;
* an applicable policy never enters compilation;
* a necessary capability is not exposed;
* current runtime state is missing.

Context loss concerns unlawful or erroneous absence.

### 1.2 Containment loss

Material enters an invocation outside its authorized scope, necessity, or disclosure boundary.

Examples include:

* one project's memory contaminates another;
* confidential evidence enters a low-trust agent context;
* personal information is exposed to an unnecessary subagent;
* over-retrieval enlarges the prompt-injection surface;
* a tool schema reveals capabilities the agent is not authorized to use.

Containment loss concerns unlawful presence.

It establishes a least-privilege rule for context:

> **An element may not be admitted merely because it is accessible. Admission requires a declared purpose, valid scope, sufficient authority, and a justified necessity judgment.**

### 1.3 Authority loss

The system loses, invents, or reverses the standing under which an element may influence inference.

Examples include:

* retrieved text is treated as governing instruction;
* a model-generated inference is treated as a user declaration;
* an advisory preference becomes mandatory policy;
* a revoked rule remains active;
* a product default silently shadows legitimate project or organization law.

Authority loss concerns legitimacy.

### 1.4 Representation loss

An admitted element is transformed in a way that removes binding structure, qualification, provenance, dissent, or uncertainty.

Examples include:

* a summary preserves a conclusion but drops its conditions;
* a quotation loses the clause limiting its scope;
* a compressed decision omits an unresolved objection;
* a memory paraphrase strengthens the source claim;
* a redaction removes a fact required to interpret what remains.

Representation loss concerns meaning across transformation.

### 1.5 Realization loss

The provider-specific request diverges from the admitted compilation.

Examples include:

* an adapter reorders elements against declared constraints;
* required context is omitted during serialization;
* the tool schema presented to the model differs from the enforced tool;
* an attachment is truncated after budget closure;
* middleware inserts or alters context outside the controlled pipeline.

Realization loss concerns correspondence between specification and presentation.

### 1.6 Receipt loss

The system cannot later establish what governed the invocation.

Examples include:

* no record identifies the memory revision used;
* a summary is presented without source lineage;
* rejected candidates disappear from the audit trail;
* the provider request cannot be reconstructed;
* the response and effects are not bound to the context that produced them.

Receipt loss concerns accountability.

These losses require different remedies. Larger context windows may reduce omission while doing nothing about authority inversion. Better retrieval may improve coverage while worsening contamination and injection risk. Persistent memory may improve continuity while obscuring revision identity. Transcript logging may preserve visible conversation without proving what the model actually received.

The systems problem is therefore not merely how to place more text inside a context window.

It is how to construct a lawful invocation context under explicit, inspectable rules.

## 2. Constitutional Context Compilation

This paper uses **constitutional context compilation** as the primary technical term.

The adjective *constitutional* refers to:

* explicit sources of authority;
* bounded jurisdiction;
* identity-bearing law;
* governed discovery;
* procedures of finding, contest, adjudication, review, and appeal;
* rules of precedence;
* amendment;
* typed refusal;
* non-self-ratification;
* independent effect authorization;
* evidentiary accountability.

The noun *compilation* refers to the governed transformation of heterogeneous source material into a canonical intermediate representation and then into a provider-specific invocation.

The compiler stands between possible context and model-visible context.

It determines:

1. which source domains must be searched;
2. what may become a candidate;
3. what may be admitted;
4. what standing each element possesses;
5. when contest is structurally required;
6. how conflicts are detected and adjudicated;
7. which transformations are lawful;
8. how finite capacity is allocated;
9. how context is realized for a provider;
10. which effects may follow;
11. what evidence must survive.

**Context systems engineering** is the broader field encompassing context storage, retrieval, memory, lifecycle, interfaces, distribution, and model interaction. Constitutional context compilation is the governing mechanism at its center.

The architecture is not merely a better prompt pipeline.

It is a typed authorization, adjudication, and transformation layer between context sources and inference.

Throughout this paper, *constitution*, *law*, *court*, *judgment*, and *lawful* name machine-governance roles inside a declared computational order unless a legal institution is explicitly identified. Lawfulness therefore means conformance to that declared order; it does not establish state-law validity, democratic legitimacy, moral correctness, or justified authority. Those remain separate evaluation dimensions.

### 2.1 The External-Governor Principle

The architecture is governed by the following proposition:

> **Every mechanism that determines whether another mechanism is scrutinized must itself be governed by authority external to the discretion it constrains.**

Examples include:

* a classifier does not determine whether its own finding requires review;
* a challenger does not certify its own independence;
* a discovery profile does not define mandatory sources out of existence;
* a calibration profile does not certify its own adequacy;
* a conflict-detection profile does not define its own closure claim;
* a domain canonicalization profile does not decide unreviewably which content differences are invisible to identity, and no profile governs the identity of its own adequacy judgment;
* an adapter does not define and certify its own fidelity standard;
* a court does not enlarge its own jurisdiction;
* a model response does not authorize its own effects;
* an amendment proposer does not ratify its own authority expansion.

The proposition does not imply an infinite regress. The chain terminates in a declared Grundnorm Basis: an explicit bootstrap presupposition rather than an undisclosed discretionary act.

### 2.2 Constitutional Closure

A context-governance architecture is **constitutionally closed** when every operative discretionary locus satisfies one of the following:

1. it is governed by explicit superior law;
2. it is adjudicated by an independently authorized court;
3. it is constrained by a deterministic rule over independently held state;
4. it is externally witnessed;
5. it is one of the fixed genesis elements enumerated in Section 5.1 as part of the Grundnorm Basis.

The fifth clause is deliberately narrow.

A component, subsystem, classifier, profile, adapter, court, or operational discretion cannot be exempted from governance merely by later labeling it part of the Grundnorm Basis. The Basis is fixed at genesis and consists only of the enumerated bootstrap elements required to establish initial constitutional standing.

Any proposal to alter the representation or interpretation of the Basis after genesis must proceed through the amendment machinery of Section 18. The amendment remains governed by the currently effective Root Constitution and does not retroactively convert ordinary discretion into an ungoverned presupposition.

A discretionary locus with none of the five properties is a constitutional gap.

Appendix D performs a discretion audit over the architecture.

### 2.3 Scrutiny-Bounding Profile Rule

A **scrutiny-bounding profile** is any identity-bearing object whose declarations determine:

* what evidence is searched;
* which claims count as reliable;
* what conflicts can be detected;
* what independence is sufficient;
* which content differences register as changes of identity at the domain layer;
* which losses an adapter may tolerate;
* or any other boundary on the scope or standard of later review.

Every scrutiny-bounding profile must:

1. possess entity and revision identity;
2. declare the evidence class of each material claim;
3. identify its author and governing authority;
4. declare known limits and unknowns;
5. be adjudicated by a court or constitutional function independent of its author;
6. be admitted before use;
7. be invalidated when its evidentiary basis, governing law, or material dependencies change.

The rule applies at least to:

* discovery profiles;
* classifier calibration profiles;
* conflict-detection profiles;
* contest-independence profiles;
* domain canonicalization profiles;
* provider-adapter contracts;
* conformance profiles.

A profile may define an operational method.

It may not define the limits of its own scrutiny and then certify itself as adequate.

#### 2.3.1 What "independent of its author" requires

Profile admission does not invoke the full contest-independence machinery of Section 6.8. Requiring different providers, deployments, or model lineages for every routine profile admission would make ordinary governance unaffordable and would imply operational independence the lower conformance levels do not provide.

The minimum for profile admission is **constitutional role separation**:

1. the proposer identity and the ratifier identity differ;
2. the adjudicator lacks authority to author the profile under review or to mutate it silently after admission;
3. the adequacy criteria applied come from superior law rather than from the profile itself;
4. the resulting judgment is independently witnessable.

Courts may be operationally co-located under Section 5.5 while still satisfying role separation, because the requirement is constitutional rather than physical.

Stronger operational independence---separate machines, operators, organizations, or model lineages---may be required for specific profile classes by the context constitution, and is required where a profile admission is itself structurally high-consequence under Section 6.7. It is not implied at lower conformance levels unless declared.

Where a profile is admitted without role separation:

```text
PROFILE_ROLE_SEPARATION_UNSATISFIED
PROFILE_SELF_ADMITTED
```

### 2.4 The Discretion Census

Section 2.2 defines closure over "every operative discretionary locus." That definition is only executable if the architecture can enumerate those loci rather than trusting that none was overlooked.

The **discretion census** is that enumeration procedure. It is evaluated over the declared object schema and the declared transition registry of the effective constitution, not over informal architectural description.

A mechanism enters the census whenever it can affect:

* identity;
* authority or standing;
* admission or exclusion;
* scope or disclosure;
* scrutiny or escalation;
* conflict detection;
* transformation;
* realization;
* effect permission;
* evidentiary claims.

Any profile, registry, reducer, serializer, scorer, ranker, router, cache-key function, threshold, or state transition meeting one of those criteria is an authority-bearing locus regardless of how it is named or where it sits in the implementation.

```text
DiscretionCensus
  census_id
  census_revision

  governing_Root_Constitution_revision
  governing_context_constitution_revision

  declared_schema_revision
  transition_registry_revision

  censused_loci[]
  audit_row_bindings[]
  reduction_proofs[]
  unmapped_loci[]

  disposition
  expiry
```

Every censused locus must bind to an audit row of Appendix D or carry a proven reduction to an existing row. A reduction is proven when the locus exercises no discretion beyond that already governed by the row to which it reduces.

An authority-bearing mechanism absent from the census, or censused but unmapped, is a constitutional gap:

```text
DISCRETION_LOCUS_UNCENSUSED
DISCRETION_AUDIT_INCOMPLETE
DISCRETION_REDUCTION_UNPROVEN
```

The census is re-evaluated whenever the declared schema, the transition registry, the Root Constitution, or the context constitution changes. A census computed against a superseded schema is stale and cannot support a closure claim.

The census does not itself require an adjudicating court. It is a deterministic rule over independently held state and therefore satisfies clause 3 of Section 2.2: the schema and transition registry it reads are declared by law and are not authored by the census.

This is the governance counterpart of the discovery census in Section 10. Discovery accounts for the sources an invocation could have consulted; the discretion census accounts for the mechanisms that could have exercised constitutional power.

### 2.5 Contributions

The paper makes six principal contributions.

**A source inventory for the invocation manifold.** PROMTHUS enumerates the eight classes of material from which any provider invocation is assembled---policy, retrieval, observations, memory, tools, history, user request, and system instruction---and establishes that the class of a source is invocation-relative and carries no authority of its own.

**Constitutional context compilation as a distinct systems layer.** The paper separates six failures ordinarily collapsed into "forgetting" (context, containment, authority, representation, realization, and receipt loss) and defines a typed authorization, adjudication, and transformation layer between context sources and inference that addresses them as different problems requiring different remedies.

**The external-governor principle and constitutional closure.** The paper states as a general proposition that every mechanism determining whether another mechanism is scrutinized must be governed by authority external to the discretion it constrains, defines what it means for an architecture to be closed under that proposition, and terminates the resulting regress in a narrow, declared bootstrap presupposition rather than an undisclosed discretionary act.

**A layered identity model.** An exclusion-free Constitutional Canonical Form identifies constitutional objects and makes the adjudication of everything above it non-circular; adjudicated domain profiles govern application material; every identity is permanently typed by the layer that produced it; and relations across layers are typed correspondences that never collapse into identity.

**Scrutiny-profile governance and the discretion census.** Any profile whose declarations bound the scope of later review is itself identity-bearing, evidence-class-typed, and adjudicated under constitutional role separation. A census over the declared schema and transition registry enumerates the mechanisms holding constitutional power, converting a completeness claim about governance into a checkable procedure.

**An inspectable contract, a conformance ladder, and a proof-obligation audit.** The Context IR gives compilation a provider-neutral artifact distinct from the prompt; the CCC ladder stages adoption with metrics and separately reported machine, human, contest, and availability costs; and Appendix D maps each discretionary locus to its governor, evidence, and typed failure, supplying an executable stopping condition for the architecture.

What the paper does not contribute is empirical evidence that any implementation satisfies these obligations. Section 32 states the limits of the claim, and the metrics of Section 28 carry targets rather than measurements.

## 3. PROMTHUS: The Source Inventory

The principal source classes of an invocation are:

$$
\mathcal{C}_{\mathrm{candidate}}
=
\langle P,R,O,M,T,H,U,S \rangle
$$

where:

* $P$ is governing **policy**;
* $R$ is **retrieved evidence**;
* $O$ is runtime **observation and operational state**;
* $M$ is persistent **memory**;
* $T$ is the exposed **tool and capability surface**;
* $H$ is selected conversation and work **history**;
* $U$ is the current **user request**;
* $S$ is vendor or base-**system instruction**.

Together, these form **PROMTHUS**.

The sequence is fixed by the mnemonic's Promethean construction and nothing else.

$$
\begin{aligned}
&\text{PROMTHUS order} \\
&\neq \text{authority order} \\
&\neq \text{serialization order}
\end{aligned}
$$

Policy appears first because the name requires it, not because policy universally outranks all other elements. Authority remains domain-relative and constitutionally adjudicated.

### 3.1 Policy

Policy defines normative constraints:

* user constitutive rules;
* organization mandates;
* project conventions;
* legal requirements;
* safety restrictions;
* approval boundaries;
* delegation limits;
* data-handling rules.

Policy is not simply highly relevant text. It is context with governing standing.

No item acquires policy standing merely because it appears in the Policy position of a serialized request. Standing arises from identity, authority, jurisdiction, scope, and judgment.

### 3.2 Retrieval

Retrieval supplies selected external evidence:

* files;
* repositories;
* databases;
* indexed knowledge;
* research literature;
* web content;
* search results.

Retrieved material may be relevant without being governing. Retrieval rank does not create authority.

### 3.3 Observations

Observations describe current operational conditions:

* tool results;
* process state;
* resource availability;
* system health;
* test outcomes;
* current files;
* external events;
* recent changes.

Observations require provenance and freshness metadata because their validity may decay quickly.

### 3.4 Memory

Memory stores maintained state across invocations:

* preferences;
* decisions;
* recurring entities;
* project definitions;
* unresolved obligations;
* approved derived conclusions.

Memory must distinguish explicit declaration from inference. A model's guess about a preference should not silently acquire the standing of a user-authored rule.

### 3.5 Tools

Tool context defines the model-visible capability surface:

* tool names;
* argument and result schemas;
* operational descriptions;
* permission constraints;
* provider and model options;
* effect classes;
* execution costs and limits.

A tool schema is not merely documentation. It shapes what the model believes it can request.

The capability surface presented to the model must correspond to the capabilities and restrictions enforced at runtime.

### 3.6 History

History records prior events and work lineage:

* conversation turns;
* decisions;
* rejected alternatives;
* plans;
* checkpoints;
* subagent reports;
* receipts;
* prior effects.

History is evidentiary. It records what occurred.

It is not identical to memory, which is a maintained representation intended to guide later work.

### 3.7 User request

The user request establishes the immediate objective, scope, constraints, desired output, and proposed effects.

A current request may govern within its jurisdiction without possessing authority to revoke every parallel or superior obligation.

### 3.8 System instruction

System instruction includes vendor, provider, application, and base-runtime instruction applied outside the ordinary user message.

Some system instructions may remain undisclosed in full. Their existence, authority class, revision, jurisdiction, and compatibility consequences should nevertheless remain accountable.

An unseen governing layer remains a governing layer.

### 3.9 Invocation-relative classification

PROMTHUS classifies an object's role in a particular invocation, not its permanent essence.

The same body may serve different functions:

* a project document may be retrieved evidence in one invocation and admitted policy in another;
* a prior user message may be history, evidence supporting memory, or the source of an effective policy revision;
* a tool result may be observation now and history later;
* a peer-agent message may be delegated history, observation, or untrusted evidence depending on its lineage;
* an output schema may derive from the user request, policy, tool contract, or system instruction;
* few-shot exemplars may guide behavior without possessing ordinary policy standing;
* interface state may be an operational observation or a user-authored declaration.

PROMTHUS is the stable top-level source manifold. Semantic subtypes and multi-role classification may evolve without forcing a new top-level class unless an object genuinely cannot be represented within the existing manifold.

## 4. PROMTHUS Compilation

To **promthe** an invocation is to constitutionally compile its PROMTHUS source manifold.

$$
\operatorname{Promthe}_{K,\Gamma,\Pi,B}
\left(
\mathcal{C}_{\mathrm{candidate}}
\right)
=
\mathcal{C}_{\mathrm{IR}}
\;\;|\;\;
\mathcal{R}
$$

where:

* $K$ is the effective Constitutional Kernel state;
* $\Gamma$ is the identity, authority, jurisdiction, custody, route, and effect environment;
* $\Pi$ is the effective context constitution;
* $B$ is the available context budget;
* $\mathcal{C}_{\mathrm{IR}}$ is the admitted Context Intermediate Representation;
* $\mathcal{R}$ is a typed refusal.

Provider realization is separate:

$$
\operatorname{Realize}_{A}
\left(
\mathcal{C}_{\mathrm{IR}}
\right)
=
\mathcal{C}_{\mathrm{provider}}
\;\;|\;\;
\mathcal{R}_{A}
$$

where $A$ is the selected provider-adapter contract.

"Promthing" is not a second expansion of the PROMTHUS letters. It is the governed process applied to the source inventory.

The operational question is:

> **Was this invocation properly promthed?**

That asks whether the model's presented world was lawfully constructed. It does not ask whether the resulting answer was useful, pleasing, or true.

## 5. Constitutional Kernel Requirements

This paper defines a minimum Constitutional Kernel contract. Any kernel adequate to govern context compilation must provide the capabilities below.

### 5.1 Grundnorm Basis

Every finite constitutional order begins from a bootstrap fact it cannot fully enact through its own successor procedures.

The **Grundnorm Basis** consists only of:

1. initial custody;
2. genesis identity;
3. the initial recognition rule;
4. the bootstrap witness;
5. the initial authority to enact positive root law.

The initial recognition rule cannot operate without a serialization under which root law can be recognized at all. That serialization is the **Constitutional Canonical Form** of Section 8.5. It is a constituent of genesis identity and the initial recognition rule rather than a further Basis element: an order that could not identify its own root law would have no recognition rule to enumerate.

The enumeration therefore remains five elements. Naming the Constitutional Canonical Form does not enlarge the Basis, and the prohibition on post-genesis enlargement in this section applies to it unchanged.

The Basis is fixed at genesis.

It is not an extensible exemption registry. No classifier, adapter, profile, court, subsystem, operational rule, or later-created authority may acquire Grundnorm status by declaration.

A later proposal concerning the Basis must be processed as a constitutional amendment under Section 18. Such an amendment may change how successor constitutional state refers to, interprets, or replaces bootstrap commitments, but the change itself remains governed by the previously effective Root Constitution.

The Basis does not become legitimate merely because it is first.

Its function is to expose the irreducible presupposition rather than conceal it inside implementation.

### 5.2 DSC-coded Root Constitution

The positive operational root law is the **DSC-coded Root Constitution**.

**DSC** denotes the **Deterministic Semantic Compiler**: the coding discipline under which constitutional rules are authored as explicit structured predicates over declared state, compiled to a canonical form, content-identified, and executed deterministically rather than interpreted afresh on each application. A DSC-coded rule is a machine-checkable artifact with an identity, not a natural-language policy statement that a component reads and construes.

Two consequences matter for the rest of the paper. First, root law can be tested, model-checked, and mutation-tested as an artifact, which is what Section 34.17 asks of it. Second, determinism holds over *admitted* predicates only: the predicates themselves may be supplied by fallible semantic findings, which is why Sections 6 and 34.15 treat root-law replay and whole-compilation replay as different properties.

It defines:

* identity-bearing law;
* the Constitutional Canonical Form and its exclusion-free grammar;
* recognized authority and jurisdiction;
* mandatory discovery obligations;
* scrutiny-profile requirements;
* discretion-census obligations;
* court standing;
* structural consequence classes;
* amendment and appeal;
* non-self-ratification;
* typed judgment;
* effect-separation requirements;
* refusal requirements;
* witness and receipt obligations;
* successor-state recognition.

The Root Constitution is:

* explicit;
* deterministically executable over admitted structured predicates;
* canonically serializable;
* content-identified;
* inspectable;
* testable;
* auditable;
* replayable over identical admitted inputs;
* mutable only through authorized amendment.

Root-law replay and compilation replay are different. Root-law execution may be deterministic over admitted predicates while compilation remains nondeterministic because discovery, semantic findings, live observations, external attestations, and human review supply those predicates.

The Root Constitution does not derive its standing by executing itself. Its initial standing arises from the Grundnorm Basis. Successor revisions derive standing through amendment law enacted by an already effective revision.

### 5.3 Context Constitution

The context constitution is domain law derived from the Root Constitution.

It defines:

* PROMTHUS classification rules;
* semantic types;
* governance statuses;
* mandatory source registries;
* discovery obligations;
* consequence tiers;
* contest requirements;
* independence profiles;
* evidence classes;
* domain canonicalization profiles;
* scope and containment;
* court jurisdictions;
* precedence relations;
* transformation permissions;
* governing-projection rules;
* preservation contracts;
* budget priorities;
* provider-adapter requirements;
* delegation inheritance;
* autonomous review modes;
* effect classes;
* conformance profiles;
* error and refusal semantics.

### 5.4 Derivation Standing

A context constitution does not acquire standing merely because it claims to derive from the Root Constitution.

The relation

$$
\operatorname{DerivesFrom}(\Pi_s, K_r)
$$

must be established by an identity-bearing derivation judgment issued under the amendment or constitutional-admission procedure of the effective Root Constitution.

The judgment verifies at least:

* authorized authorship;
* permitted domain;
* consistency with non-delegable root invariants;
* valid amendment or admission procedure;
* effective revision identity;
* migration and supersession relations;
* absence of self-ratification.

```text
ConstitutionalDerivationJudgment
  subject_constitution
  subject_revision
  parent_constitution
  parent_revision
  authorized_proposer
  ratifying_authority
  preserved_root_invariants[]
  delegated_domains[]
  excluded_domains[]
  migration_status
  disposition
  judgment_hash
```

Without a valid derivation judgment:

```text
CONSTITUTIONAL_DERIVATION_UNESTABLISHED
```

### 5.5 Courts

The kernel must support identity-bearing courts or equivalent constitutional functions that:

* receive findings;
* apply effective law;
* issue typed dispositions;
* preserve jurisdiction boundaries;
* require contest where structurally triggered;
* adjudicate scrutiny-bounding profiles;
* expose appeal and automatic-stay routes;
* refuse when lawful resolution is unavailable.

These functions may be implemented within one process. They remain constitutionally distinct even when operationally co-located.

### 5.6 Compiler, IR, realization, effect boundary, and witness

The compiler executes admitted court judgments.

The Context IR is the canonical identity-bearing product of compilation.

The realization layer converts Context IR into a provider-specific request.

The effect boundary independently evaluates whether a model-proposed action may occur.

The witness layer establishes correspondence among:

* source revisions;
* admitted scrutiny profiles;
* findings;
* consequence derivations;
* contests;
* judgments;
* Context IR;
* provider realization;
* model response;
* authorized effects;
* receipts.

The Context IR is not the constitution or the court.

It is the executable result of constitutionally governed adjudication.

## 6. Law, Findings, Structural State, Contest, and Judgment

The classifier and compiler must not invent the law by which their own decisions are evaluated.

The kernel therefore separates:

$$
\begin{aligned}
&\text{Law}
\rightarrow \text{Finding}
\rightarrow \text{Independent Structural State} \\
&\rightarrow \text{Consequence Tier}
\rightarrow \text{Contest}
\rightarrow \text{Judgment}
\rightarrow \text{Execution}
\end{aligned}
$$

### 6.1 Law is not classification

The Root Constitution and context constitution determine:

* who may classify;
* which methods may be used;
* what evidence must accompany a finding;
* what uncertainty representations are admissible;
* which tier inputs must come from authoritative state;
* how unresolved semantic alternatives affect tiering;
* when independent contest is mandatory;
* when refusal is required.

They do not make every semantic classification mechanically obvious.

### 6.2 Findings are not law

A finder may be:

* deterministic;
* heuristic;
* model-assisted;
* human-authored;
* hybrid;
* adversarially reviewed.

Its output is a proposed finding, not an automatic constitutional fact.

```text
ClassificationFinding
  finding_id
  subject_entity
  subject_revision

  proposed_PROMTHUS_class
  proposed_semantic_type
  proposed_governance_status
  proposed_epistemic_status

  semantic_alternatives[]
  proposed_scope_interpretation
  proposed_content_classification

  method_identity
  method_revision
  calibration_profile

  evidence[]
  confidence_band
  uncertainty
  timestamp
```

The finder does not authoritatively supply:

* tool effect classes;
* route boundaries;
* custody boundaries;
* delegation topology;
* provider locality;
* amendment-object identity;
* effect irreversibility;
* current authority deltas.

Those facts are derived from independently maintained constitutional state.

### 6.3 Calibration Profiles

A deterministic threshold applied to an uncalibrated classifier score does not create trustworthy determinism.

Confidence-bearing findings therefore require a calibration profile bound to the method revision and task domain.

```text
ClassifierCalibrationProfile
  profile_id
  profile_revision

  classifier_identity
  classifier_revision
  task_domain

  calibration_dataset
  calibration_dataset_identity
  calibration_dataset_revision
  sampling_method

  reliability_metrics
  admissible_decision_bands
  known_failure_regions
  evidence_classes[]

  author
  governing_authority
  effective_period
```

Raw scores are not portable across classifiers, prompts, domains, or revisions.

A method revision invalidates confidence-dependent thresholds unless effective law explicitly recognizes a compatible calibration profile.

Courts should prefer decision bands such as:

```text
ADMITTABLE
REVIEW_REQUIRED
INSUFFICIENT_CONFIDENCE
OUT_OF_CALIBRATION_DOMAIN
```

rather than treating an unqualified decimal score as constitutional evidence.

#### 6.3.1 Calibration-profile adjudication

A calibration profile is scrutiny-bounding because it determines which findings may proceed without escalation.

It must therefore be adjudicated before use.

The Calibration Adequacy Court or equivalent constitutional function evaluates:

* dataset identity and provenance;
* task-domain correspondence;
* sampling and measurement method;
* reliability metrics;
* calibration drift;
* decision-band justification;
* known failure regions;
* evidence class of each material claim;
* independence between profile author and adjudicator.

```text
CalibrationAdequacyJudgment
  calibration_profile
  governing_classifier
  verified_claims[]
  empirically_tested_claims[]
  attested_claims[]
  self_declared_claims[]
  unknown_claims[]
  domain_fit
  drift_status
  disposition
  expiry
```

A classifier cannot establish its own admissible decision bands merely by publishing a favorable calibration profile.

### 6.4 Independently Derived Structural State

Consequence tiering must consume authoritative structural state rather than finder-proposed approximations.

Let:

$$
S_f
=
\operatorname{DeriveStructure}
\left(
K,
\Pi,
\Gamma,
\mathcal{T},
\mathcal{R},
\mathcal{D},
\mathcal{E}
\right)
$$

where:

* $K$ is effective kernel state;
* $\Pi$ is effective context law;
* $\Gamma$ is the authority and custody environment;
* $\mathcal{T}$ is the tool and effect registry;
* $\mathcal{R}$ is the provider and route graph;
* $\mathcal{D}$ is the delegation topology;
* $\mathcal{E}$ is the external-boundary and irreversibility registry.

The derived structural state includes:

```text
StructuralConsequenceState
  subject_entity
  current_governance_status
  candidate_governance_transition

  source_custodian
  destination_custodian
  custody_boundary_crossed

  source_disclosure_class
  destination_clearance
  disclosure_boundary_crossed

  tool_effect_classes[]
  effect_irreversibility
  external_provider_crossing

  delegation_depth
  authority_delta
  amendment_object
  constitutional_object
```

These values may be challenged through adjudication, but the finder does not control their authoritative source.

### 6.5 Conservative Semantic Alternatives

Some consequence inputs remain semantic. Whether an artifact contains restricted evidence may not be determinable from structure alone.

Where unresolved alternatives remain, the system computes the highest applicable tier over the *material* alternatives admitted under Section 6.6:

$$
\operatorname{Tier}(f)
=
\max_{a \in \operatorname{MaterialAlternatives}(f)}
g_{\Pi}(S_f, a)
$$

until adjudication lawfully narrows the alternatives.

Uncertainty therefore raises or preserves scrutiny rather than lowering it.

The maximum ranges only over alternatives carrying a valid materiality judgment. An alternative without identified evidentiary support does not enter the computation.

### 6.6 Alternative Materiality and Provenance

Conservative tiering must not permit arbitrary alternative injection.

Every alternative included in the maximum-tier computation must satisfy a materiality threshold:

$$
\begin{aligned}
&\operatorname{MaterialAlternative}(a) \\
&\iff \operatorname{EvidenceIdentified}(a) \\
&\land \operatorname{PlausibilityThresholdMet}(a) \\
&\land \operatorname{RelevantToTier}(a)
\end{aligned}
$$

Each alternative records:

```text
SemanticAlternative
  alternative_id
  finding_id
  proposed_classification
  supporting_evidence[]
  originating_sources[]
  evidentiary_route
  plausibility_basis
  consequence_relevance
  inclusion_judgment
  contest_status
```

The rule is symmetric:

* omitting a materially supported alternative may invalidate the finding;
* including an unsupported or immaterial high-risk alternative may also invalidate the finding or trigger alternative-origin review.

The support for an alternative is itself contestable.

A finder cannot profit from under-classification by omitting a plausible higher-risk alternative, and an attacker cannot obtain indefinite escalation merely by causing unsupported possibilities to be listed.

### 6.7 Structurally Computed Consequence

Contest is required when:

$$
\operatorname{Tier}(f)
\geq
\tau_{\Pi}
$$

Examples of structurally high-consequence findings include those that would:

* promote evidence to mandatory policy;
* authorize external disclosure;
* enable an irreversible effect;
* grant a new tool or delegated capability;
* alter constitutional standing;
* relax a non-delegable constraint;
* authorize amendment;
* expose protected context across a custody boundary.

A finder may dispute the semantic alternatives or structural derivation through ordinary adjudication. It may not exempt itself from scrutiny by declaring its own finding unimportant.

### 6.8 Contest Independence

A second finding is not independent merely because it was generated separately.

Independence may include:

* **procedural independence** --- separately appointed and not controlled by the original finder;
* **method independence** --- materially different reasoning mechanism;
* **evidence independence** --- access to evidence not filtered through the challenged finding;
* **deployment independence** --- different runtime, operator, or custody;
* **provider independence** --- different provider or administrative domain;
* **lineage independence** --- distinct model or training ancestry where verifiable or attested.

```text
ContestIndependenceProfile
  profile_id
  profile_revision

  required_procedural_independence
  required_method_independence
  required_evidence_independence
  required_deployment_independence
  required_provider_independence
  required_lineage_independence

  prohibited_shared_dependencies[]
  acceptable_method_families[]
  minimum_independence_class

  author
  governing_authority
  evidence_classes[]
```

#### 6.8.1 Independence-profile authorship

The minimum independence class is not chosen by the challenger or the finder.

It is established in the context constitution or an authorized derived profile and admitted by the Contest and Independence Court.

An independence profile must be adjudicated before it can discharge a contest or machine-review obligation.

### 6.9 Independence Evidence Classes

An independence claim must declare its evidentiary basis.

```text
VERIFIED_LOCAL
VERIFIED_EXTERNAL
PROVIDER_ATTESTED
INSTITUTIONALLY_ATTESTED
NOMINAL_ONLY
UNKNOWN
```

Examples:

* different local executables under separate custody may support `VERIFIED_LOCAL`;
* independently audited deployments may support `VERIFIED_EXTERNAL`;
* a proprietary provider's claim about training lineage may support only `PROVIDER_ATTESTED`;
* different model names with no ancestry disclosure support `NOMINAL_ONLY`.

An independence requirement may specify the minimum evidence class acceptable for each dimension.

Claims about undisclosed training ancestry are no stronger than the attestations supporting them.

### 6.10 Context Contest

```text
ContextContest
  contest_id
  challenged_finding

  challenger_identity
  challenger_method
  challenger_provider
  challenger_deployment
  challenger_lineage_claim

  alternative_finding
  counterevidence[]
  challenged_assumptions[]

  independence_basis[]
  independence_evidence_classes[]
  independence_profile
  independence_assessment

  requested_disposition
  urgency
```

A nominal counterfinding with no qualifying independence may be receipted but does not satisfy an independent-contest obligation.

### 6.11 Adversarial Contest

Where the structural tier requires contest, the procedure may require:

* a separate deterministic rule analysis;
* a model from a different provider or method family;
* an independent human;
* hostile evidence search;
* generation of the strongest contrary classification;
* a multi-finder quorum.

Contest is not intended to produce artificial balance where evidence is one-sided. Its purpose is to expose correlated error, omitted evidence, unsupported alternatives, and hidden assumptions before a high-consequence finding gains standing.

### 6.12 Judgment

A court judgment contains:

```text
ContextJudgment
  judgment_id
  court
  court_revision

  Root_Constitution_revision
  context_constitution_revision

  subject
  findings_considered[]
  structural_state
  semantic_alternatives_considered[]
  alternative_materiality_judgments[]
  contests_considered[]

  consequence_tier
  contest_requirement
  contest_satisfaction

  disposition
  rationale_codes[]

  authority
  jurisdiction
  scope
  effective_period

  review_status
  appeal_status

  judgment_hash
  signatures[]
```

The court may:

* admit;
* exclude;
* narrow scope;
* classify as contested;
* require review;
* defer;
* refer;
* refuse an element, route, delegation, effect, or invocation.

### 6.13 The Classification Trust Root

The trust root is not the classifier's intelligence.

It is the explicit law, identity, custody, admitted calibration profile, independently derived structure, symmetric alternative-materiality rule, admitted independence requirement, contest procedure, and witness under which classifier findings may acquire standing.

This does not eliminate semantic uncertainty.

It constitutionalizes it.

### 6.14 Conflict-Detection Profiles

No compiler can honestly guarantee resolution of every semantic conflict if conflict detection itself has unknown recall.

Resolution closure must therefore be scoped to conflicts detected under an admitted profile:

$$
\operatorname{ResolutionClosure}
=
\operatorname{Closure}
\left(
\operatorname{DetectedConflicts}_{D}
\right)
$$

```text
ConflictDetectionProfile
  profile_id
  profile_revision

  method
  method_revision
  calibration_profile

  structural_checks[]
  semantic_checks[]

  coverage_claim
  confidence_requirements
  escalation_policy
  known_blind_spots[]

  evidence_classes[]
  author
  governing_authority
  effective_period
```

The system may claim:

* closure over all structurally enumerated conflicts;
* closure over conflicts detected by profile $D$;
* reviewed closure under a named court procedure.

It may not claim omniscient conflict detection.

#### 6.14.1 Conflict-profile adjudication

A conflict-detection profile is scrutiny-bounding because it defines which conflicts can enter resolution closure.

It must therefore be identity-bearing, evidence-class-typed, and adjudicated before use.

The Conflict-Detection Adequacy Court or equivalent constitutional function evaluates:

* structural-check completeness relative to declared schemas;
* semantic method identity;
* benchmark evidence;
* calibration applicability;
* declared coverage class;
* known blind spots;
* escalation rules;
* expiry and invalidation conditions.

A narrow profile may be admitted for a narrow claim.

It may not support a broader closure claim than its admitted evidence permits.

## 7. Governance Correctness and Behavioral Correctness

The architecture distinguishes two verification targets.

### 7.1 Governance Correctness

Governance correctness concerns whether an invocation was lawfully constructed.

It asks:

* Were mandatory source obligations accounted for?
* Were all scrutiny-bounding profiles adjudicated?
* Was least-privilege containment respected?
* Were identity and standing authenticated?
* Were findings produced under admissible and calibrated methods?
* Were consequence inputs derived from authoritative state?
* Were semantic alternatives materially supported and conservatively tiered?
* Were structural contest requirements satisfied?
* Were judgments issued under effective law?
* Were court conflicts resolved or refused?
* Were transformations authorized?
* Was the budget lawfully closed?
* Did realization correspond to Context IR?
* Were tool schemas synchronized with runtime implementations?
* Were effects independently authorized?
* Was the invocation witnessed and receipted?

Governance correctness is principally **forethought**: it determines whether and under what conditions an invocation may occur.

The Promethean name reflects this orientation. *Prometheus* is *pro-metheus*, forethought; governance acts before dispatch, before execution, and before effect.

### 7.2 Behavioral Correctness

Behavioral correctness concerns the downstream quality of model output and effects.

It asks:

* Was the answer factually sound?
* Did the model understand the task?
* Did it follow the presented constraints?
* Was the output useful?
* Were authorized effects executed correctly?

Behavioral correctness is principally **afterthought**: it evaluates what occurred once inference or effect was permitted.

In the mythic contrast, this is the Epimethean side of the system: *epi-metheus*, judgment after the event rather than governance before it.

A lawfully compiled invocation may produce a poor answer.

A useful answer may emerge from an unlawfully assembled context.

The first is behavioral failure under governance success.

The second is accidental task success under governance failure.

Logging cannot replace governance. A perfect receipt written after an unlawful dispatch is evidence of the breach, not prevention of it.

## 8. Context Identity, Provenance, and Canonicalization

A constitutional context system requires at least three distinct forms of identity.

### 8.1 Entity Identity

Entity identity names a continuing institution.

Examples include:

```text
user-confidentiality-policy
project-deployment-memory
repository-tool-contract
```

It answers:

> Which continuing context object is this?

Entity identity may remain stable across revisions.

### 8.2 Revision Identity

Revision identity names an exact immutable state.

Let $C_{r,\kappa}(e)$ be the serialization of revision $r$ of entity $e$ under canonicalization layer $\kappa$.

Revision identity is a pair, not a bare digest:

$$
R_{e,r,\kappa}
=
\left\langle
\kappa,
\;
H\left( C_{r,\kappa}(e) \right)
\right\rangle
$$

It answers:

> Which exact revision is this, and under which canonicalization layer was that determination made?

A mutation to identity-bearing content produces a new revision identity. So does a change of canonicalization layer, because the second component is computed under the first.

For constitutional objects, $\kappa$ is the Constitutional Canonical Form of Section 8.5. For domain objects, $\kappa$ is an admitted domain canonicalization profile revision under Section 8.6. Section 8.7 governs what may and may not be inferred across two identities carrying different $\kappa$.

### 8.3 Presentation Identity

Presentation identity names the exact representation supplied to a model or provider adapter.

$$
P_{e,r,t,\kappa}
=
\left\langle
\kappa,
\;
H\left(
\operatorname{Present}_{t}\left( C_{r,\kappa}(e) \right)
\right)
\right\rangle
$$

where $t$ is an admitted transformation and presentation profile and $\kappa$ is the governing canonicalization layer.

It answers:

> Which exact representation of this revision was presented?

The lineage is:

$$
E_e
\rightarrow
R_{e,r,\kappa}
\rightarrow
P_{e,r,t,\kappa}
$$

A presentation does not inherit the revision's identity unless the transformation is `NONE` and the canonical bytes are presented unchanged.

The canonicalization layer propagates along the whole lineage. A presentation cannot be compared with a revision identity computed under a different layer.

### 8.4 Canonicalization

Content addressing is meaningful only under a stable canonicalization policy.

Identity may otherwise change because of:

* serializer differences;
* field ordering;
* whitespace;
* encoding;
* line endings;
* omitted defaults;
* generated timestamps;
* map ordering;
* redaction;
* provider formatting;
* metadata inclusion.

Each identity-bearing object records:

```text
canonicalization_profile
canonicalization_profile_revision
identity_fields
excluded_nonsemantic_fields
content_hash
```

A canonicalization policy is itself versioned and content-identified. Its own identity is computed under the Constitutional Canonical Form of Section 8.5, never under itself.

A canonicalization change must not silently masquerade as a context-content change.

### 8.5 Constitutional Canonical Form

A domain canonicalization profile must possess identity before a court can adjudicate it, and the court, its jurisdiction graph, its judgment, the Root Constitution, and the context constitution must possess identity as well. If every identity were computed under an adjudicated profile, the layer would be circular:

$$
\begin{aligned}
&\text{profile identity}
\rightarrow \text{profile adjudication} \\
&\rightarrow \text{admitted canonicalization}
\rightarrow \text{profile identity}
\end{aligned}
$$

The architecture therefore separates two canonicalization layers.

The **Constitutional Canonical Form (CCaF)** is a primitive, exclusion-free serialization fixed by the DSC grammar and bound into the genesis identity and initial recognition rule of Section 5.1. It is not adjudicated, because there is no prior identity layer under which an adjudication of it could be recorded. It is instead recognized at genesis and inspectable thereafter.

The abbreviation `CCaF` is used deliberately. In the wider Ableman corpus,

`CCF` is the historical **Constitutional Crystallization Framework** name in the author-confirmed `CCF -> CMB -> GMB` lineage whose current name is **Governed Meaning Base (GMB)**. CCaF is a canonicalization primitive; GMB is a governed semantic and meaning architecture. The shared letters do not imply identity, derivation, or substitutability.

It identifies at least:

* the Grundnorm manifest;
* the Root Constitution and every successor revision;
* the context constitution and its derivation judgment;
* court definitions and jurisdiction graphs;
* scrutiny-bounding profiles of every class;
* profile-adequacy judgments;
* the discretion census;
* amendment proposals, ratifications, and transitions;
* court dispositions;
* receipts and constitutional transition records.

Its defining restriction is that it permits **syntactic normalization only**:

* encoding;
* field ordering;
* framing and delimiting;
* numeric and string representation;
* line endings and whitespace.

It permits no semantic field exclusion whatsoever. There is no   
`excluded_nonsemantic_fields` set at this layer, because the discretion to declare a field non-semantic is exactly the discretion that requires adjudication, and adjudication is what this layer exists to make possible.

Consequently:

```text
CONSTITUTIONAL_CANONICAL_FORM_UNRECOGNIZED
CCAF_EXCLUSION_ATTEMPTED
```

An implementation that introduces an exclusion at this layer has not optimized its identity function. It has removed the ground on which every adjudication above it stands.

The Constitutional Canonical Form is fixed at genesis and may be succeeded only through the amendment machinery of Section 18, under the same prohibition against post-genesis Basis enlargement. A successor form does not retroactively re-identify historical constitutional objects; it establishes a governed correspondence to them under Section 8.7.

### 8.6 Domain Canonicalization Profiles Are Scrutiny-Bounding

A domain canonicalization profile decides which differences between two domain bodies register as a change of identity and which are declared non-semantic. Its scope is application-level material: memories, observations, retrieved artifacts, tool records, transcripts, and similar objects. It has no authority over constitutional objects, which are identified under the Constitutional Canonical Form.

That decision bounds all later scrutiny.

If the excluded-field set is widened, a material mutation may produce no new revision identity, and every downstream guarantee that depends on revision identity degrades silently: caches remain valid, judgments remain reused, receipts remain reproducible, and the change becomes invisible to review.

A domain canonicalization profile is therefore governed under the rule of Section 2.3. Its own identity is computed under the Constitutional Canonical Form, which is what allows it to be adjudicated without circularity.

An invocation may operate under more than one admitted domain profile. Memories, retrieved artifacts, tool records, and transcripts may reasonably differ in which fields are non-semantic, and forcing a single profile across all of them would either over-exclude for the strictest class or under-exclude for the loosest. Each admitted element therefore records the layer governing its own identity, and the Context IR and receipt carry the set of admitted domain profiles rather than a single one. Cross-layer relations within a single invocation are subject to Section 8.7 exactly as they are across revisions.

```text
CanonicalizationProfile
  profile_id
  profile_revision

  serialization_form
  encoding
  ordering_rules
  default_handling
  whitespace_rules

  identity_fields[]
  excluded_nonsemantic_fields[]
  exclusion_justifications[]

  evidence_classes[]
  author
  governing_authority
  effective_period
```

The Domain Canonicalization Adequacy Court or equivalent constitutional function evaluates:

* whether each excluded field is genuinely non-semantic under the governing domain law;
* whether any excluded field could carry governing, disclosure, or authority-relevant content;
* whether the identity-field set covers every constitutionally material property;
* the evidence class of each exclusion justification;
* whether the serialization form is deterministic;
* whether a profile change is being represented as a content change or vice versa;
* independence between profile author and adjudicator.

```text
DomainCanonicalizationAdequacyJudgment
  canonicalization_profile
  governing_domains[]
  verified_exclusions[]
  attested_exclusions[]
  self_declared_exclusions[]
  unsupported_exclusions[]
  identity_field_coverage
  determinism_assessment
  disposition
  expiry
```

An implementation may not declare its own exclusions non-semantic and then rely on the resulting identities as constitutional evidence.

### 8.7 Cross-Layer Correspondence, Not Equivalence

A profile revision may change which fields participate in identity. Two profiles declared "equivalent" could therefore be used to carry an identity across a change in the identity function itself, which reopens the laundering channel that Section 8.6 exists to close. Equivalence at this layer is not a convenience; it is a hole.

Identity therefore remains permanently typed by its canonicalization layer. For an object $x$ under layer $\kappa$:

$$
I_{\kappa}(x)
=
\left\langle
\kappa,
\;
H\left( C_{\kappa}(x) \right)
\right\rangle
$$

Two identities with different $\kappa$ are different identities. No court, migration, amendment, or optimization may collapse them.

What a court may admit is a **correspondence record**: a typed, receipted relation between two identity-bearing objects that leaves both identities intact.

```text
BYTE_EQUIVALENT
SEMANTICALLY_CORRESPONDENT
MIGRATION_SUCCESSOR
NON_EQUIVALENT
```

```text
IdentityCorrespondenceRecord
  correspondence_id
  subject_identity
  counterpart_identity
  subject_layer
  counterpart_layer
  correspondence_class
  evidence[]
  evidence_class
  admitting_judgment
  scope
  expiry
```

Even `BYTE_EQUIVALENT` asserts only that two serializations under two layers produced identical bytes for one comparison. It does not make the identities interchangeable, and it does not license substituting one for the other in a cache key, a revocation list, a delegation constraint, or a historical receipt.

The distinction is load-bearing precisely where it is most tempting to ignore:

* a cache entry keyed under a superseded layer is not a hit for a lookup under the current layer;
* a revocation recorded against an identity under one layer does not automatically revoke a counterpart identity under another;
* a historical receipt remains verifiable under the layer in force when it was sealed, and is not retroactively re-verified under a successor;
* a delegation constraint naming a protected identity does not silently extend to a corresponding identity admitted later.

Migration is therefore an explicit governed act producing `MIGRATION_SUCCESSOR` records, not a silent re-identification.

Failures at this layer:

```text
IDENTITY_LAYER_BINDING_ABSENT
CROSS_PROFILE_IDENTITY_COLLAPSED
CORRESPONDENCE_CLASS_UNSTATED
CORRESPONDENCE_RECORD_ABSENT
```

### 8.8 Provenance

Every admitted or derived element exposes:

* source entity;
* source revision;
* creator or custodian;
* discovery route;
* semantic type;
* PROMTHUS class;
* findings and contests;
* semantic-alternative origins;
* structural consequence derivation;
* court judgments;
* transformation lineage;
* governing canonicalization layer;
* correspondence records where identity crosses layers;
* effective scope.

Provenance establishes descent and custody.

It does not establish truth or authority by itself.

## 9. Governance Status and Epistemic Status

Governance and epistemology are independent dimensions.

For every element $e$, the system represents a governance status $G(e)$ and an epistemic status $K(e)$.

Possible governance statuses include:

* constitutive;
* mandatory;
* advisory;
* evidentiary;
* non-governing;
* prohibited;
* revoked.

Possible epistemic statuses include:

* verified;
* corroborated;
* asserted;
* inferred;
* contested;
* stale;
* unknown;
* false.

An element may be:

* authoritative but factually mistaken;
* true but unauthorized to govern;
* contested but mandatory to disclose;
* stale but historically evidentiary;
* unverified but relevant;
* binding as policy without asserting a fact.

Admission does not certify truth.

Truth does not create authority.

The compiler governs standing and presentation. It does not solve ground truth.

## 10. Discovery as a Governed Constitutional Function

Discovery operates before item-level adjudication and therefore controls which possible context can become visible to the rest of the system.

It is not a neutral preprocessing step.

### 10.1 Mandatory Source Obligations

Mandatory source registries and source classes derive from the context constitution, not from the discovery profile proposed by the compiler.

Examples include:

* the effective Root Constitution;
* applicable organization policy;
* active project constitution;
* current tool registry;
* unresolved mandatory obligations;
* revocation lists;
* required runtime observations.

A discovery profile may implement these obligations.

It may not redefine them away.

### 10.2 Discovery Profile

A proposed discovery profile defines:

```text
DiscoveryProfile
  profile_id
  profile_revision

  source_domains[]
  mandatory_source_registries[]

  retrieval_methods[]
  query_construction_policy
  ranking_policy
  candidate_cutoff

  freshness_policy
  coverage_claim
  known_blind_spots[]

  containment_constraints[]
  cost_limit

  evidence_classes[]
  author
  governing_authority
```

### 10.3 Discovery Evidence Classes

Not every property of a discovery profile is equally verifiable.

Claims should be classified as:

```text
STRUCTURALLY_VERIFIED
EMPIRICALLY_TESTED
EXTERNALLY_ATTESTED
SELF_DECLARED
UNKNOWN
```

Examples:

* inclusion of all constitutionally mandatory registries may be structurally verified;
* recall on a benchmark corpus may be empirically tested;
* completeness of a third-party index may be externally attested;
* a blind-spot list may be self-declared;
* unknown retrieval behavior must remain typed as unknown.

A court may verify that a blind-spot statement exists. It cannot ordinarily prove that the statement is complete.

### 10.4 Discovery Adequacy Court

The profile itself must be adjudicated before use.

The Discovery Adequacy Court determines whether the proposed profile:

* covers every mandatory registry;
* lawfully limits source domains;
* uses admissible retrieval methods;
* declares ranking and cutoffs;
* satisfies freshness obligations;
* respects containment;
* identifies the evidence class of each coverage claim;
* states known blind spots;
* remains within authorized cost.

```text
DiscoveryAdequacyJudgment
  profile_id
  governing_obligations[]
  covered_obligations[]
  unmet_obligations[]

  structurally_verified_claims[]
  empirically_tested_claims[]
  externally_attested_claims[]
  self_declared_claims[]
  unknown_claims[]

  containment_assessment
  coverage_assessment
  cost_assessment

  disposition
  effective_scope
  expiry
```

A profile with an empty mandatory registry list cannot satisfy the constitution merely by declaring nothing mandatory.

### 10.5 Aggregate Non-Selection

Objects that never enter the candidate set do not each require a court judgment.

Their non-selection is governed and receipted in aggregate through:

* the admitted discovery profile;
* search domains;
* queries;
* indexes;
* ranking;
* cutoffs;
* result commitments.

### 10.6 Candidate Exclusion

Once an object enters adjudication as a candidate, its admission or exclusion receives an item-level judgment.

### 10.7 Mandatory-Source Absence

A mandatory source obligation must result in:

* discovery and adjudication;
* a typed unavailability record;
* or refusal.

It cannot disappear into aggregate non-selection.

## 11. Precedence, Court Jurisdiction, and Review

### 11.1 Element Precedence

For each conflict domain $d$, effective law defines a strict precedence relation:

$$
\succ_{\Pi,d}
\subseteq
E_d \times E_d
$$

The relation is irreflexive:

$$
\neg\left( e \succ_{\Pi,d} e \right)
$$

and transitive:

$$
\begin{aligned}
&e_1 \succ_{\Pi,d} e_2 \\
&\land e_2 \succ_{\Pi,d} e_3 \\
&\Rightarrow e_1 \succ_{\Pi,d} e_3
\end{aligned}
$$

It need not be total.

Precedence may arise from:

* authority;
* jurisdiction;
* explicit supersession;
* scope;
* specificity;
* delegation;
* temporal effect;
* domain-specific arbitration.

Traditional doctrines such as *lex superior*, *lex specialis*, and *lex posterior* provide useful patterns, but none supplies a universal ordering when the doctrines themselves conflict.

### 11.2 Incomparable Element Conflicts

If two mandatory elements conflict and neither precedes the other:

$$
e_1 \parallel_{\Pi,d} e_2
\land
\operatorname{Conflict}(e_1, e_2)
$$

the invocation must be referred to an authorized arbiter or refused.

Automatically choosing one would invent authority absent from the constitution.

Where all conflicting elements are optional, policy may permit:

* exclusion of one;
* exclusion of both;
* retention of both as contested evidence;
* referral to arbitration.

Each disposition must be receipted.

### 11.3 Court Jurisdiction Graph

Courts may also conflict.

The context constitution therefore defines a jurisdiction graph:

```text
CourtJurisdiction
  court_id
  subject_domain
  permitted_dispositions[]
  superior_review_court
  coordination_rules[]
  exclusion_rules[]
```

A Standing Court might require inclusion of a governing constraint while a Containment Court prohibits disclosure of the protected source body.

Neither disposition should silently erase the other.

### 11.4 Inter-Court Conflict

Where valid judgments conflict:

$$
\begin{aligned}
&\operatorname{Conflict}(J_a, J_b) \\
&\land  \\
&\ne g\operatorname{AuthorizedResolution}(J_a, J_b)
\end{aligned}
$$

the result is:

```text
COURT_CONFLICT_UNRESOLVED
```

The default consequence is refusal of the affected invocation, route, delegation, or effect.

The context constitution may authorize a Coordination or Constitutional Court to resolve specified classes of deadlock. No operational court may enlarge its own jurisdiction by declaring itself necessary.

### 11.5 Review Modes

Review must compose with both human-timescale workflows and unattended agent loops.

The context constitution defines review modes:

```text
NONE
PRE_EXECUTION_AUTOMATIC_STAY
PRE_EXECUTION_MACHINE_REVIEW
PRE_EXECUTION_HUMAN_REVIEW
POST_EXECUTION_APPEAL
SUCCESSOR_ONLY_REVIEW
```

### 11.6 Machine-Review Independence

Where a review exists to satisfy an independent-scrutiny requirement, a machine reviewer must satisfy the applicable admitted independence profile.

A same-model or same-lineage review may assist with explanation or evidence gathering, but it cannot discharge an independence requirement unless the constitution explicitly permits that evidence class.

`PRE_EXECUTION_MACHINE_REVIEW` is therefore not a loophole around contest independence.

### 11.7 Automatic Constitutional Stays

A structural consequence tier may automatically stay execution before dispatch.

Typical stay-triggering classes include:

* external disclosure;
* irreversible effect;
* authority escalation;
* amendment;
* high-risk delegation;
* contested protected-data classification;
* court-jurisdiction conflict.

The stay may be initiated by:

* the compiler;
* an independent witness;
* a policy-defined guardian;
* a contesting finder;
* an affected custodian.

Human vigilance is not presumed.

If required review does not occur within the authorized window, the default result is refusal, not silent continuation.

### 11.8 Appeals

An appeal challenges a judgment under already effective law.

It is not an amendment and does not create new law.

An appeal procedure defines:

* who has standing;
* appealable grounds;
* filing period;
* reviewing court;
* required evidence;
* whether the judgment is stayed;
* treatment of in-flight invocations;
* finality and further review.

Appealable grounds may include:

* jurisdictional error;
* misapplied law;
* invalid evidence;
* calibration failure;
* unmet contest requirement;
* procedural defect;
* newly discovered authoritative material.

Post-execution appeal ordinarily affects successor invocations and future standing. It does not retroactively erase a completed provider call.

### 11.9 Exigence and Custody During Review

A pending stay or appeal transfers custody of the affected work to the reviewing authority.

Dependent execution remains blocked until:

* the judgment is affirmed;
* modified;
* reversed;
* expired into refusal;
* or superseded by authorized amendment.

The system should make this custody visible: who has the ball, why the work is blocked, and what authority can resolve it.

### 11.10 Cycles and Invalid Structures

A cycle in an element-precedence or court-jurisdiction graph is a constitutional defect.

```text
CONTEXT_PRECEDENCE_CYCLE
COURT_JURISDICTION_CYCLE
```

The compiler must refuse or invoke an authorized repair procedure.

### 11.11 Serialization Is Not Precedence

Physical position in a provider request may express an already resolved precedence decision.

It may not create that decision by itself.

## 12. Transformation, Compression, and Governing Projections

Transformation is a governed act.

A summary may erase qualification, dissent, uncertainty, scope, or conditions of applicability. A retrieved fragment may remove the clause limiting the quoted sentence. A normalized policy may convert guidance into prohibition.

The principled distinction is not between full text and compression.

It is between **lawful derivation** and **semantic substitution**.

### 12.1 Lawful Derivation

A transformation is lawful when:

* the source is identified;
* the transformation is permitted;
* preservation obligations are declared;
* the result receives a distinct identity;
* known losses are recorded;
* the derived object does not impersonate the source;
* mandatory propositions survive.

```text
ContextTransformation
  source_entity
  source_revision
  source_hash

  transformation_type
  transformation_policy
  transformer_identity

  candidate_presentation_hash

  preservation_obligations[]
  preserved_obligations[]
  known_losses[]

  findings[]
  court_judgment
  admission_status
```

### 12.2 Semantic Substitution

Substitution occurs when a derived representation silently assumes the standing or identity of its source.

Examples include:

* a summary presented as canonical policy;
* a memory paraphrase treated as the user's exact declaration;
* a subagent report replacing source evidence without disclosure;
* an extracted conclusion losing the conditions under which it holds.

For source revision $R$ and presentation $P$:

$$
P \neq R
$$

unless exact identity is established.

A lawful derivation is:

$$
R
\xrightarrow{\;t,\pi,J\;}
P
$$

where $t$ is the transformation, $\pi$ is the preservation contract, and $J$ is the admitting judgment.

### 12.3 Governing Projection

A governing projection is a special class of derived legal artifact.

It does not inherit mandatory standing automatically from its source. It receives new, independently adjudicated standing because its preservation contract is defined over a governing obligation rather than over the full protected source body.

```text
GoverningProjection
  projection_id

  source_policy_entity
  source_policy_revision

  projected_obligations[]
  intentionally_withheld_content[]

  disclosure_profile
  metadata_disclosure_assessment

  transformation_judgment
  standing_judgment

  authority
  jurisdiction
  scope
  expiry

  presentation_identity
```

The governing projection is lawful only if a court determines that:

1. the projected obligation is preserved;
2. omitted source content is not needed to interpret the obligation;
3. withholding the source body is required or permitted by containment law;
4. the projection's own metadata disclosure is acceptable;
5. the projection has a distinct identity and expiry;
6. the projection does not represent itself as the canonical source.

Its mandatory standing comes from the standing judgment admitting the new artifact, not from silent inheritance.

### 12.4 Projection Leakage

A projection may itself leak sensitive information.

Revealing that an embargo exists, its category, duration, or protected subject may be harmful.

The projection court must therefore assess disclosure of:

* existence;
* category;
* protected identity;
* scope;
* expiry;
* enforcement wording.

Where no safe projection can preserve the obligation without disclosing protected metadata, the delegation or invocation must be refused.

## 13. Two-Phase Budget Closure

Token counts are provider-, adapter-, and tokenizer-relative. Budget closure cannot be finalized before provider realization.

### 13.1 Compile-Time Estimate

$$
\operatorname{EstimateBudget}
\left(
\mathcal{C}_{\mathrm{materialized}}, A
\right)
\rightarrow
\widehat{B}
$$

The estimate reserves:

* invariant context;
* required tool schemas;
* output capacity;
* adapter overhead;
* safety margin.

### 13.2 Realize and Verify

$$
\operatorname{Realize}_{A}
\left(
\mathcal{C}_{\mathrm{IR}}
\right)
\rightarrow
\mathcal{C}_{\mathrm{provider}}
$$

$$
\operatorname{ExactSize}_{A}
\left(
\mathcal{C}_{\mathrm{provider}}
\right)
\leq
B - R_o
$$

If exact realization exceeds the budget, the system returns to an authorized reduction point.

It may not truncate after the fact.

### 13.3 Bounded Closure Loop

Budget closure may require a bounded fixed-point process:

$$
\begin{aligned}
&C_0 \\
&\rightarrow R_0 \\
&\rightarrow V_0 \\
&\rightarrow C_1 \\
&\rightarrow R_1 \\
&\rightarrow V_1 \\
&\rightarrow \cdots
\end{aligned}
$$

The context constitution defines:

* maximum iterations;
* permitted reductions;
* monotonicity requirements;
* cost bounds;
* refusal conditions.

If lawful closure cannot be reached:

```text
CONTEXT_BUDGET_UNCLOSED
```

At conformance levels below exact realization synchronization, preservation contracts may be evaluated against compile-time estimates. Such systems must state that exact adapter-level closure is not yet guaranteed.

## 14. Context Courts and Compilation Pipeline

### 14.1 Constitutional Functions

The context vertical includes:

* Constitutional Derivation Court;
* Discovery Adequacy Court;
* Calibration Adequacy Court;
* Conflict-Detection Adequacy Court;
* Domain Canonicalization Adequacy Court;
* Adapter-Contract Adequacy Court;
* Classification Court;
* Standing and Scope Court;
* Containment Court;
* Contest and Independence Court;
* Conflict and Precedence Court;
* Transformation Court;
* Budget and Route Court;
* Delegation Court;
* Realization Correspondence Court;
* Effect Authorization Court;
* Receipt and Conformance Court;
* Amendment Court;
* Appellate or Coordination Court.

These may be operationally consolidated while remaining constitutionally distinct.

### 14.2 Pipeline

The governed pipeline is:

$$
\begin{aligned}
&\operatorname{AdjudicateProfiles}
\rightarrow \operatorname{ProposeDiscovery}
\rightarrow \operatorname{AdjudicateDiscovery} \\
&\rightarrow \operatorname{Discover}
\rightarrow \operatorname{Find}
\rightarrow \operatorname{DeriveStructure} \\
&\rightarrow \operatorname{AdjudicateAlternatives}
\rightarrow \operatorname{ComputeConsequence}
\rightarrow \operatorname{Contest} \\
&\rightarrow \operatorname{Adjudicate}
\rightarrow \operatorname{Resolve}
\rightarrow \operatorname{Materialize}
\rightarrow \operatorname{Realize} \\
&\rightarrow \operatorname{ReviewOrStay}
\rightarrow \operatorname{Dispatch}
\rightarrow \operatorname{AuthorizeEffect}
\rightarrow \operatorname{Seal}
\end{aligned}
$$

Each transition produces a typed output or refusal.

The discovery profile is itself a scrutiny-bounding profile under Section 2.3, so its adjudication could in principle occur in the first step. It appears as a separate transition because its content is invocation-dependent: the searched domains, queries, and cutoffs are proposed against a specific trigger, whereas calibration, conflict-detection, canonicalization, independence, adapter, and conformance profiles are ordinarily admitted for a period and reused across invocations. Standing profiles are adjudicated once and invalidated on change; the per-invocation discovery proposal is adjudicated each time it is constructed.

### 14.3 Context IR

The Context IR is the canonical provider-neutral result of compilation.

```text
InvocationContextIR
  invocation_id
  parent_invocation_id
  trigger_commitment

  Grundnorm_Basis_id
  Root_Constitution_revision
  context_constitution_revision
  constitutional_derivation_judgment

  compiler_revision

  constitutional_canonical_form_revision
  domain_canonicalization_profiles[]
  domain_canonicalization_adequacy_judgments[]
  identity_layer_bindings[]
  correspondence_records[]

  discretion_census_revision
  discretion_census_disposition

  scrutiny_profiles[]
  scrutiny_profile_judgments[]

  discovery_profile_revision
  discovery_adequacy_judgment

  candidate_manifest_commitment

  findings[]
  semantic_alternatives[]
  alternative_materiality_judgments[]
  structural_consequence_states[]
  consequence_assessments[]
  contests[]
  independence_assessments[]
  judgments[]
  stays[]
  appeals[]

  admitted_elements[]
  excluded_elements[]
  unresolved_elements[]

  precedence_graph
  court_jurisdiction_graph

  transformation_manifest
  governing_projection_manifest
  containment_manifest
  tool_surface_manifest

  estimated_budget
  output_reserve
  eligible_routes[]

  context_ir_hash
```

Each admitted element contains:

```text
AdmittedContextElement
  entity_id
  revision_id

  PROMTHUS_class
  semantic_type
  governance_status
  epistemic_status

  authority
  jurisdiction
  scope
  purpose
  declared_necessity

  source_hash
  canonicalization_layer
  permitted_transformations
  inclusion_obligation
  precedence_rules

  consequence_tier
  contest_status

  court_judgment
  provenance
```

Each materialized element contains:

```text
MaterializedContextElement
  source_entity_id
  source_revision_id
  source_hash

  transformation_id
  transformation_policy
  presentation_hash

  preserved_obligations[]
  known_losses[]

  position_constraint
  estimated_token_count
  exact_token_count

  inclusion_status
  omission_reason
```

The IR is not the prompt.

It is the inspectable constitutional contract from which provider-specific context is realized.

## 15. Typing and Adapter Contracts at the Provider Boundary

The Context IR may contain a rich type system. Most current inference interfaces do not preserve arbitrary semantic types as enforceable model-side privileges.

At the provider boundary, typed objects are often flattened into:

* a small set of message roles;
* text delimiters;
* tool declarations;
* attachments;
* model-specific control structures.

The model may still treat evidence as instruction or fail to honor a stated precedence relation.

Typed context therefore provides:

1. enforceable compiler-side admission;
2. enforceable runtime effect control;
3. inspectable provenance and receipts;
4. structured representation of standing to the model where supported.

It does not guarantee model-side obedience.

> **Standing is enforced by the kernel, courts, compiler, tool boundary, and effect runtime. At the token boundary, standing is represented to the model unless the provider offers a native enforceable mechanism capable of preserving it.**

### 15.1 Provider-Adapter Contract

A provider-adapter contract declares:

```text
ProviderAdapterContract
  adapter_id
  adapter_revision

  supported_message_roles
  role_semantics
  delimiter_semantics
  escaping_rules

  native_privilege_features[]
  tool_schema_format
  attachment_semantics

  tokenizer_identity
  capacity_rules
  output_controls

  known_flattening_losses[]
  hidden_provider_layers[]
  witnessability

  evidence_classes[]
  author
  governing_authority
  effective_period
```

### 15.2 Adapter-Contract Adjudication

The adapter contract is scrutiny-bounding because realization consistency is evaluated under the relation it defines.

The adapter cannot define its own fidelity standard and certify itself against that standard.

Before use, the Adapter-Contract Adequacy Court evaluates:

* whether declared role mappings preserve required distinctions;
* whether losses are structurally verified, empirically tested, attested, self-declared, or unknown;
* whether delimiter and escaping rules are adequate;
* whether tool-schema realization is checkable;
* whether tokenizer and capacity claims are supported;
* whether hidden layers are represented honestly;
* whether the contract's assurance boundary matches available witnessability.

```text
AdapterContractAdequacyJudgment
  adapter_contract
  verified_capabilities[]
  empirically_tested_capabilities[]
  attested_capabilities[]
  self_declared_losses[]
  unknown_losses[]
  prohibited_profiles[]
  admitted_profiles[]
  disposition
  expiry
```

A provider may be admitted for one Context IR profile and refused for another.

### 15.3 Delimiter Integrity

Text delimiters are representational aids, not security boundaries.

An adapter should nevertheless guarantee:

* canonical escaping;
* unambiguous segment boundaries;
* preservation of segment identity in receipts;
* resistance to accidental delimiter collision;
* no silent concatenation of unlike standing classes.

### 15.4 Tool Correspondence

A tool manifest binds:

* tool identity;
* schema revision;
* model-visible description;
* runtime implementation;
* authorization envelope;
* effect class.

Tool protocols such as MCP make schema divergence a concrete current boundary: the schema admitted into Context IR, the declaration presented to the model, and the implementation invoked at runtime must remain constitutionally synchronized.

Tool-schema correspondence is required at CCC-2 because independent effect authorization cannot reliably validate action class, arguments, or scope if the model-visible capability differs from the enforced runtime capability.

## 16. Independent Effect Authorization

Effect authorization is not a late-stage luxury. It is a foundational control.

A model may propose an action. That proposal does not establish authority to execute it.

The non-implication chain is:

$$
\begin{aligned}
&\text{Inference Result} \\
&\not\Rightarrow \text{Execution Authority} \\
&\not\Rightarrow \text{Effect Authorization}
\end{aligned}
$$

### 16.1 Effect Request

A proposed effect is normalized into:

```text
EffectRequest
  actor
  action
  object
  parameters

  tool_identity
  tool_schema_revision

  effect_class
  reversibility
  externality
  resource_cost

  authority_claim
  jurisdiction
  approval_requirements
  originating_invocation
```

### 16.2 Effect Judgment

The Effect Authorization Court or runtime authorization boundary evaluates:

* whether the actor possesses authority;
* whether the requested action is within scope;
* whether the object is within jurisdiction;
* whether required approvals exist;
* whether the current state still permits the action;
* whether the effect conflicts with policy;
* whether the tool identity and schema presented to the model correspond to the enforced runtime tool;
* whether the runtime effect class matches the class used during consequence analysis.

A mismatch produces refusal before effect:

```text
TOOL_SCHEMA_DIVERGENCE
TOOL_EFFECT_CLASS_MISMATCH
```

## 17. Delegation and Agentic Execution

Sequential loops and branching delegation require different constitutional treatment.

### 17.1 One Provider Call as the Compilation Unit

The unit of constitutional compilation is one provider invocation.

An agent loop is a chain:

$$
\begin{aligned}
&i_0 \\
&\rightarrow o_0 \\
&\rightarrow i_1 \\
&\rightarrow o_1 \\
&\rightarrow \cdots \\
&\rightarrow i_n
\end{aligned}
$$

Each $o_k$ may introduce observations, effects, refusals, or new context for the next invocation.

Every provider call receives:

* a new invocation identity;
* a parent invocation;
* an effective law snapshot;
* an updated candidate set;
* a new Context IR;
* a new provider commitment;
* a new receipt.

### 17.2 Delegation Tree

Delegation creates branching custody and authority:

$$
\begin{aligned}
i_{\mathrm{parent}} \rightarrow \{&i_{\mathrm{child},1}, i_{\mathrm{child},2}, \dots, \\
&i_{\mathrm{child},n}\}
\end{aligned}
$$

A delegation contract specifies:

```text
DelegationContract
  delegation_id
  parent_invocation
  delegate_identity

  task_scope
  purpose

  mandatory_inherited_elements[]
  optional_inherited_elements[]
  prohibited_disclosures[]
  permitted_reductions[]
  governing_projections[]

  delegated_tools[]
  effect_authority
  spending_or_resource_limits
  further_delegation_rights

  required_return_evidence[]
  review_mode

  termination_conditions[]
  revocation_conditions[]
```

### 17.3 Inheritance Rules

A child context may become stricter.

It may not silently weaken mandatory parent constraints.

A child may receive less context where containment requires it, but the delegation must preserve enough constitutional information to enforce inherited obligations without unnecessarily disclosing protected bodies.

### 17.4 Delegation Court

A delegation judgment determines:

* whether the delegate has standing;
* what context may be inherited;
* which constraints are mandatory;
* which projections may substitute for protected source bodies;
* which tools may be exposed;
* which effects may be authorized;
* whether further delegation is permitted;
* which review mode applies;
* what evidence must return.

### 17.5 Autonomous Stays

A long-running loop cannot depend on a human noticing every appealable event.

For structurally defined judgment classes, the constitution may require an automatic pre-execution stay.

The loop records:

```text
WORK_STATUS: BLOCKED_BY_CONSTITUTIONAL_REVIEW
CUSTODY: <review authority>
DEPENDENT_INVOCATIONS: SUSPENDED
TIMEOUT_DISPOSITION: REFUSAL
```

### 17.6 Return Path

A child result is not automatically trusted history or evidence.

It returns with:

* invocation receipt;
* source and transformation lineage;
* tool and effect log;
* uncertainty;
* unresolved conflicts;
* declared omissions.

The parent independently adjudicates the returned material.

### 17.7 Incremental Compilation

Identity-keyed caching may reuse:

* authenticated entity and revision identity;
* court judgments whose scope still applies;
* unchanged precedence edges;
* admitted transformations;
* provider-independent IR fragments.

Reuse is keyed by identity, law, scope, purpose, calibration, discovery profile, conflict-detection profile, canonicalization layer, adapter contract, contest profile, and freshness---not by informal similarity.

Because identity is typed by its canonicalization layer under Section 8.7, a cache key computed under a superseded layer is not a hit for a lookup under the current one. An admitted correspondence record may justify recomputation; it never justifies substitution.

### 17.8 Invalidation

Cached judgments are invalidated by changes to:

* Root Constitution;
* context constitution;
* constitutional derivation judgment;
* authority or custody;
* source revision;
* revocation;
* observation freshness;
* classifier or calibration profile;
* conflict-detection profile;
* Constitutional Canonical Form revision;
* domain canonicalization profile;
* contest-independence requirement;
* discovery profile;
* tool schema;
* adapter contract;
* conflict domain;
* purpose or scope;
* delegation boundary.

### 17.9 Time-of-Check to Time-of-Use

A source may be valid during admission and revoked before dispatch.

Volatile predicates must be rechecked before the provider request crosses the controlled boundary.

```text
CONTEXT_INVALIDATED_BEFORE_DISPATCH
```

## 18. Amendment and Constitutional Change

A constitution without an amendment procedure merely relocates hidden discretion.

### 18.1 Amendment Proposal

```text
AmendmentProposal
  proposal_id
  target_entity
  current_revision
  proposed_revision

  proposer
  authority_claim

  rationale
  migration_plan
  tests[]
  affected_invariants[]

  proposed_effective_time
```

### 18.2 Ratification

The effective Root Constitution defines:

* who may propose;
* who may contest;
* who may review;
* who may ratify;
* whether multiple roles are required;
* which courts must concur;
* what evidence and tests are mandatory.

A governed component may propose an amendment.

It may not silently ratify an enlargement of its own authority.

### 18.3 Successor Law

The Amendment Court issues a judgment under current law:

$$
K_n \vdash \operatorname{Admit}(K_{n+1})
$$

or:

$$
K_n \vdash \operatorname{Refuse}(K_{n+1})
$$

The successor receives a new revision identity and effective-state transition receipt.

### 18.4 Basis-Related Amendments

The fixed Grundnorm Basis cannot be enlarged by ordinary declaration.

A proposal that changes how successor law refers to, replaces, or migrates from a bootstrap commitment must:

* identify the affected genesis commitment;
* preserve the historical basis;
* proceed through the current amendment process;
* produce a successor constitutional state;
* avoid recasting an ordinary subsystem as part of the original Basis;
* remain fully receipted.

The amendment does not rewrite genesis.

It creates a governed successor relation to it.

### 18.5 In-Flight Invocations

By default, each provider call remains governed by the law snapshot admitted at its start:

```text
invocation_id
Root_Constitution_revision
context_constitution_revision
adapter_contract_revision
```

An amendment governs successor invocations.

An emergency invalidation rule may terminate an in-flight invocation only where previously effective law already authorizes that intervention.

### 18.6 Migration and Rollback

An amendment may require:

* reclassification of stored memory;
* invalidation of cached judgments;
* new calibration profiles;
* updated contest-independence requirements;
* re-adjudication of discovery profiles;
* re-adjudication of conflict-detection profiles;
* re-adjudication of domain canonicalization profiles;
* correspondence records where an identity layer is superseded;
* updated adapter contracts and tests;
* revised preservation contracts;
* re-evaluation of active delegations;
* revocation of provider routes.

Migration is itself governed and receipted.

Rollback does not erase history. It creates a successor state that reactivates or reconstructs an earlier rule set through a new authorized transition.

Where migration or rollback crosses a canonicalization layer, it produces `MIGRATION_SUCCESSOR` correspondence records under Section 8.7. It does not re-identify historical objects, and it does not make identities under the prior layer interchangeable with identities under the successor.

## 19. Reproducibility and Replayability

Receipt reproducibility and compilation replayability are different properties.

### 19.1 Receipt Reproducibility

A receipt is reproducible when an independent verifier can recompute recorded commitments from the artifacts and disclosures available to it.

This includes:

* source commitments;
* scrutiny-profile commitments;
* profile-adjudication commitments;
* finding and judgment commitments;
* Context IR hash;
* provider-request commitment;
* response commitment;
* effect-log commitment.

Receipt reproducibility is required for evidentiary standing.

Reproducibility is stated relative to the governing canonicalization layer: the Constitutional Canonical Form for constitutional objects, and the admitted domain profile for domain objects. A verifier recomputing a commitment under a different layer is testing a different claim, and should record the result as a correspondence rather than as reproduction.

### 19.2 Compilation Replayability

Compilation is replayable when re-running the compiler from the same declared sources produces the same findings, judgments, and Context IR.

This may fail where compilation depends on:

* approximate retrieval;
* nondeterministic ranking;
* changing indexes;
* stochastic classifiers;
* live observations;
* external attestations;
* human review;
* unavailable provider tokenizers.

Replayability must therefore be declared rather than assumed.

```text
RECEIPT_REPRODUCIBLE
COMPILATION_DETERMINISTIC
COMPILATION_SEEDED_STOCHASTIC
COMPILATION_ENVIRONMENT_DEPENDENT
COMPILATION_HUMAN_DEPENDENT
COMPILATION_NONREPLAYABLE
```

A stochastic or environment-dependent compiler should preserve, where possible:

* random seed;
* model and classifier identity;
* classifier context;
* calibration profile;
* contest method;
* discovery-profile revision;
* conflict-detection-profile revision;
* Constitutional Canonical Form revision;
* domain canonicalization-profile revisions;
* adapter-contract revision;
* retrieval-index revision;
* candidate set;
* ranking results;
* environment snapshot.

The system may reproduce what happened without claiming it would necessarily make the same semantic decision again.

## 20. Assurance Boundary and Receipts

### 20.1 Minimum Receipt Contract

A conforming receipt records or commits to:

```text
InvocationReceipt
  invocation_id
  parent_invocation_id
  trigger_commitment

  Grundnorm_Basis_id
  Root_Constitution_revision
  context_constitution_revision
  constitutional_derivation_judgment
  court_procedure_revisions[]

  scrutiny_profiles[]
  scrutiny_profile_judgments[]

  discovery_profile_revision
  discovery_adequacy_judgment
  candidate_set_commitment
  candidate_manifest

  findings[]
  semantic_alternatives[]
  alternative_materiality_judgments[]
  structural_consequence_states[]
  consequence_assessments[]
  contests[]
  independence_assessments[]
  judgments[]

  stays[]
  appeals[]

  excluded_elements[]
  unresolved_elements[]

  precedence_graph_commitment
  court_jurisdiction_graph_commitment

  transformation_manifest
  governing_projection_manifest
  containment_manifest

  context_ir_hash
  provider_adapter_revision
  provider_request_commitment
  tool_schema_manifest_commitment

  model_identifier
  provider_identifier

  response_commitment
  effect_log_commitment

  compiler_revision

  constitutional_canonical_form_revision
  domain_canonicalization_profiles[]
  domain_canonicalization_adequacy_judgments[]
  identity_layer_bindings[]
  correspondence_records[]

  discretion_census_revision
  discretion_census_disposition

  calibration_profiles[]

  hidden_layer_commitments[]
  seal_status
  witness_signatures[]
  transparency_anchor
```

### 20.2 Privacy-Preserving Commitments

Raw content-address hashes may remain inside the authorized custody boundary.

Receipts intended for broader disclosure should default to domain-separated salted or keyed commitments:

$$
\operatorname{Commit}(x)
=
H\left(
\text{domain}
\parallel
\text{salt}
\parallel
C(x)
\right)
$$

This reduces:

* dictionary attacks;
* cross-receipt correlation;
* disclosure of repeated sensitive context.

Selective disclosure may later reveal the salt and body to an authorized verifier.

### 20.3 Hidden Layers

A vendor or organization may withhold a sensitive instruction body while disclosing:

* layer identity;
* revision;
* commitment;
* authority class;
* jurisdiction;
* change status;
* compatibility declaration.

The norm is not necessarily total prompt transparency.

It is constitutive accountability.

### 20.4 Self-Attestation and External Witness

A receipt produced solely by the system under audit is self-attestation.

Its evidentiary value increases when:

* courts sign their judgments;
* a separate witness observes dispatch;
* runtime effects are recorded independently;
* receipt roots are anchored externally.

Append-only Merkle transparency logs can provide inclusion and consistency proofs without making sensitive receipt bodies public.

### 20.5 Boundary of Proof

Within the controlled boundary, a receipt may establish:

* which law revisions were effective;
* which canonicalization layers governed which identities;
* which scrutiny-bounding profiles were admitted;
* which discretionary loci were censused and mapped;
* which source revisions were considered;
* which structural facts were derived;
* which alternatives and evidentiary origins were considered;
* which findings, consequence assessments, contests, and judgments occurred;
* which transformations and projections occurred;
* which Context IR was produced;
* which provider request was emitted;
* which response was received;
* which local effects were authorized.

It does not prove:

* that evidence was true;
* that law was morally legitimate;
* that discovery found every relevant source;
* that a self-declared blind-spot list was complete;
* that a calibration dataset was representative beyond its evidence;
* that a conflict-detection profile found every conflict;
* that a domain canonicalization exclusion was genuinely non-semantic in every future context;
* that two identities under different canonicalization layers denote the same object;
* that the declared schema exposed every mechanism actually exercising discretion;
* that an adapter's undisclosed losses were complete;
* that provider-attested model lineage was accurate;
* that contest independence eliminated correlated error;
* that the model understood the context;
* that the model obeyed it;
* that a remote provider added no hidden instruction;
* that the declared remote model executed;
* that no post-dispatch transformation occurred.

A receipt proves governed presentation and trace consistency.

It does not prove semantic compliance.

## 21. Threat and Failure Model

The architecture must account for attacks against both context and governance.

### 21.1 Classification Capture

A finder systematically assigns standing favorable to an attacker or institution.

Controls include:

* method identity;
* admitted calibration profiles;
* independently derived structural state;
* conservative tiering across materially supported alternatives;
* independent counterfinding;
* court review;
* typed uncertainty;
* adversarial testing.

### 21.2 Calibration Capture

A profile author chooses a favorable calibration corpus, measurement method, or decision band to make a weak classifier appear constitutionally adequate.

Controls include:

* calibration-profile identity;
* dataset identity and lineage;
* evidence-class typing;
* independent adequacy judgment;
* drift monitoring;
* profile expiry;
* hostile calibration tests.

### 21.3 Contest Laundering

A nominal challenger reproduces the same correlated assumptions and creates the appearance of independent scrutiny.

Controls include:

* typed independence profiles;
* evidence classes;
* prohibited shared dependencies;
* evidence independence;
* provider and deployment diversity;
* contest-quality metrics.

### 21.4 Discovery Capture

A discovery profile narrows the candidate universe so that inconvenient sources never enter adjudication.

Controls include:

* constitutionally declared mandatory registries;
* Discovery Adequacy Court;
* profile identity and expiry;
* aggregate non-selection receipts;
* evidence-class typing;
* appeal and hostile coverage tests.

### 21.5 Conflict-Detection Capture

A narrow conflict-detection profile makes resolution closure trivially satisfiable by failing to detect relevant conflicts.

Controls include:

* identity-bearing conflict-detection profiles;
* benchmarked structural and semantic checks;
* evidence-class typing;
* independent adequacy judgment;
* scope-limited closure claims;
* hostile conflict corpora.

### 21.6 Adapter-Contract Capture

An adapter defines broad permissible losses and then claims fidelity to the standard it authored.

Controls include:

* independent adapter-contract adjudication;
* typed known and unknown losses;
* profile-specific admission;
* exact request commitments;
* hostile render tests;
* refusal where required semantics cannot survive realization.

### 21.7 Canonicalization Capture

An implementation widens the excluded-field set of a domain canonicalization profile so that material mutations no longer produce new revision identities. A second route reaches the same end without touching the exclusion set: declare two profiles equivalent and carry an identity across the change in the identity function itself.

The attack is quiet by construction. Revoked policy appears current, an altered memory retains its prior identity, cached judgments remain valid, and receipts continue to reproduce, because the difference never registered as a change.

Controls include:

* canonicalization-profile identity and revision;
* per-exclusion justification with evidence class;
* independent adequacy judgment;
* identity-field coverage assessment;
* prohibition on treating profile change as content change;
* identity permanently typed by canonicalization layer;
* typed correspondence records instead of collapsible equivalence;
* an exclusion-free Constitutional Canonical Form beneath the adjudicated layer, so no profile can govern the identity of its own adequacy judgment;
* hostile mutation tests that alter only excluded fields and assert that governing content cannot hide there.

### 21.8 Discretion-Census Evasion

An authority-bearing mechanism is introduced without appearing in the declared schema or transition registry, and therefore never enters the discretion census or Appendix D.

The mechanism need not look constitutional. A ranking heuristic that decides which candidates reach adjudication, a cache-key function that decides when a judgment is reused, a threshold that decides when a score escalates, a serializer that decides which fields are written, or a router that decides which provider is eligible each exercise governed power while presenting as implementation detail.

Evasion may be deliberate or merely careless. A performance optimization added below the declared schema has the same constitutional effect as an intentional bypass.

Controls include:

* census evaluation over the declared schema and transition registry rather than over prose description;
* the ten authority criteria of Section 2.4 applied by mechanism capability, not by name or layer;
* mandatory binding of every censused locus to an audit row or a proven reduction;
* census staleness detection on schema, registry, or law change;
* refusal of conformance claims where the census is incomplete or stale;
* adversarial review that attempts to introduce an ungoverned authority-bearing mechanism and asserts that the census detects it.

```text
DISCRETION_LOCUS_UNCENSUSED
DISCRETION_AUDIT_INCOMPLETE
DISCRETION_CENSUS_STALE
```

A closure claim resting on an incomplete census is not a closure claim. It is an assertion of architectural omniscience.

### 21.9 Retrieval Poisoning and Prompt Injection

An attacker places instruction-like material in likely retrieval sources.

Controls include:

* evidence typing;
* containment;
* no automatic promotion to policy;
* adapter separation;
* independent effect authorization.

### 21.10 Alternative Injection

An attacker induces a finder to include a weakly supported high-risk semantic alternative. Conservative maximum-tier computation then forces contest or stay.

Controls include:

* symmetric alternative-materiality requirements;
* identified supporting evidence;
* inclusion judgments;
* contestable plausibility;
* source-level alternative provenance;
* alternative deduplication;
* stay attribution through the alternative to the originating evidence.

### 21.11 Cross-Scope Contamination

Memory or evidence from one domain enters another.

Controls include:

* purpose binding;
* scope adjudication;
* least-privilege admission;
* access control;
* containment receipts.

### 21.12 Malicious or Negligent Transformation

A summary or derived object removes binding structure.

Controls include:

* distinct presentation identity;
* source lineage;
* preservation contracts;
* contest;
* transformation judgment;
* known-loss records.

### 21.13 Projection Leakage

A governing projection preserves the obligation but leaks protected metadata.

Controls include:

* metadata disclosure assessment;
* minimization;
* projection expiry;
* refusal where no safe projection exists.

### 21.14 Policy Shadowing

A lower-standing or less visible rule displaces legitimate law.

Controls include:

* Root Constitution derived standing;
* strict partial-order precedence;
* inter-court conflict law;
* no authority from serialization position.

### 21.15 Court Capture

A court exceeds jurisdiction, ignores contests, or systematically ratifies one institutional interest.

Controls include:

* jurisdiction graphs;
* signed judgments;
* appeal;
* separated witnesses;
* hostile court tests;
* non-self-extension of authority.

### 21.16 Appeal Suppression

An autonomous loop continues while an appealable or stayed judgment remains unresolved.

Controls include:

* structurally triggered review modes;
* automatic stays;
* custody transfer;
* refusal on review timeout;
* successor-dependency checks.

### 21.17 Stay Flooding and Constitutional Denial of Service

An attacker repeatedly induces high-tier findings or review triggers, causing an autonomous system to remain blocked or time out into refusal.

Potential sources include:

* poisoned retrieval;
* repeated adversarial documents;
* malicious delegated reports;
* crafted tool observations;
* coordinated low-cost requests that cross protected boundaries;
* unsupported high-risk alternatives injected into findings.

The safety default must not be weakened into "ignore excessive stays." Instead, the system should govern the origin and aggregation of stays.

Controls include:

* attribution of every stay to its source, finding, alternative, and route;
* provenance traversal from a generated alternative to the evidentiary source that motivated it;
* deduplication of materially equivalent triggers;
* rate limits by source identity, custodian, retrieval domain, and finding class;
* aggregation of related stays into one review matter;
* source quarantine;
* escalating review of repeated trigger origins;
* custody transfer to a higher-capacity review authority;
* priority rules for essential services;
* separate availability receipts;
* constitutional review of the stay trigger itself.

Stay attribution must not terminate at the system finder when the finder generated an alternative in response to poisoned evidence. Attribution must continue through the alternative's provenance to the originating source.

Repeated stays from one source may alter that source's trust or admissibility status, but unresolved substantive risk must not be silently ignored.

### 21.18 Amendment Capture

A component alters the law governing its own authority.

Controls include:

* non-self-ratification;
* distinct proposer and ratifier roles;
* amendment contest;
* migration testing;
* transition receipts.

### 21.19 Basis Laundering

A subsystem attempts to escape ordinary governance by declaring itself part of the Grundnorm Basis.

Controls include:

* fixed genesis enumeration;
* prohibition on post-genesis Basis enlargement by declaration;
* amendment-governed successor relations;
* explicit `GRUNDNORM_BASIS_SCOPE_VIOLATION` refusal.

### 21.20 Stale Admission and TOCTOU

A revoked revision remains active or changes between check and dispatch.

Controls include:

* effective-state checks;
* dispatch-time revalidation;
* cache invalidation;
* typed refusal.

### 21.21 Provider-Side Transformation and Unverifiable Lineage

A remote provider may add hidden instruction, modify context, or make unverifiable claims about model and training lineage.

Without provider attestation, the system limits its claim to the controlled dispatch boundary.

Even with attestation, the claim remains no stronger than the attestation and its verifier.

Provider evidence may address:

* model identity;
* deployment identity;
* training-lineage relationship;
* hidden instruction;
* request integrity;
* post-dispatch transformation.

### 21.22 Silent Truncation

Material is dropped after compilation.

Controls include:

* exact post-realization token verification;
* payload commitment;
* refusal rather than truncation.

### 21.23 Receipt Leakage and Fabrication

Bare hashes may leak low-entropy content or reuse patterns. Self-issued receipts may misrepresent what occurred.

Controls include:

* salted commitments;
* disclosure tiers;
* independent recomputation;
* separated witness;
* transparency anchoring.

### 21.24 Top-Level Failure Classes

```text
CONTEXT_LOSS
CONTEXT_CONTAINMENT_LOSS
CONTEXT_AUTHORITY_LOSS
CONTEXT_REPRESENTATION_LOSS
CONTEXT_REALIZATION_LOSS
CONTEXT_RECEIPT_LOSS
```

These classes are refined into machine-readable error codes.

## 22. Constitutional Refusal and Ordinary Task Failure

A constitutional refusal is not an ordinary task failure.

### 22.1 Ordinary Task Failure

A task failure occurs after a lawful invocation has been constructed but the work does not succeed.

Examples include:

* the model produces an incorrect answer;
* the requested file lacks necessary information;
* a lawful tool call returns an operational error;
* generated code fails its tests.

The constitution may remain intact even though the task fails.

### 22.2 Constitutional Refusal

A constitutional refusal occurs because no lawful invocation, delegation, route, review, or effect can be constructed.

Examples include:

* required policy cannot fit without unauthorized reduction;
* mandatory claims or court judgments remain irreconcilable;
* required independent contest cannot be obtained;
* a scrutiny-bounding profile is unadjudicated;
* a provider route violates data policy;
* a tool schema diverges from runtime;
* a mandatory stay cannot be resolved;
* the final request cannot be witnessed;
* an effect lacks authority.

A constitutional refusal is successful preservation of the governing boundary.

### 22.3 Accidental Task Success

A system may complete a task despite unlawful compilation.

For example, it may produce a correct summary after silently omitting a confidentiality rule.

The output may be behaviorally successful while the invocation remains constitutionally invalid.

Correctness of result does not retroactively legalize the path that produced it.

## 23. Worked Example I: Confidential Analysis Under Provider Failover

Consider an enterprise analysis agent.

The user requests:

> Summarize the attached confidential acquisition document. Use the fastest available model.

### 23.1 PROMTHUS Sources

**Policy:** Organization law prohibits transmitting restricted acquisition documents to external inference providers.

**Retrieval:** The acquisition document is retrieved and classified as restricted evidence.

**Observations:** The local model is unavailable; the cloud model is healthy.

**Memory:** A durable project memory states that sensitive acquisition materials are processed locally unless an authorized exception is approved.

**Tools:** The router exposes a local model, a cloud model, and automatic cloud failover.

**History:** A prior decision receipt records that confidential acquisition work must not use cloud fallback.

**User request:** The user asks for the fastest available model but grants no external-transmission exception.

**System instruction:** The product prefers successful completion and automatic provider failover.

### 23.2 Findings and Judgments

The Classification Court identifies the relevant source roles.

The Standing and Scope Court determines that the user request establishes the task but does not authorize external disclosure.

The Conflict and Precedence Court determines:

$$
\text{Organization confidentiality policy}
\succ
\text{Product failover instruction}
$$

within the restricted-data domain.

The legal provider set contains only the local route.

The local route is unavailable.

### 23.3 Result

No admitted transformation can make cloud transmission lawful.

The token budget closes.

The provider route does not.

```text
PROVIDER_ROUTE_INCOMPATIBLE:
EXTERNAL_PROVIDER_FORBIDDEN_FOR_RESTRICTED_EVIDENCE

NO_COMPATIBLE_MODEL_ROUTE
```

No provider request is emitted.

The user-visible result is:

> The document cannot be processed at present. The available cloud route is prohibited for this material, and the authorized local model is unavailable. No document content was transmitted externally.

This is a constitutional refusal, not an ordinary task failure.

## 24. Worked Example II: History Compaction

A long-running software project has more selected history than the provider budget permits.

The canonical history contains:

1. an admitted decision to preserve backward compatibility;
2. a rejected proposal to remove a legacy interface;
3. unresolved dissent concerning performance cost;
4. a mandatory approval gate before schema migration;
5. a superseded implementation plan;
6. extensive exploratory discussion.

### 24.1 Preservation Contract

The Transformation Court receives:

```text
Preserve:
  canonical decisions
  active constraints
  unresolved dissent
  approval gates
  supersession relations
  source lineage

May omit:
  redundant wording
  abandoned exploratory detail
  repeated examples
```

### 24.2 Unsafe Summary

A first summary states:

> Maintain backward compatibility and proceed with the new schema plan.

It omits:

* unresolved performance dissent;
* the approval gate;
* explicit supersession of the old plan.

The court refuses it:

```text
CONTEXT_REDUCTION_UNSAFE:
BINDING_STRUCTURE_OMITTED
```

### 24.3 Admitted Summary

A second summary states:

> The project remains bound to backward compatibility. The earlier plan to remove the legacy interface is rejected and superseded. Performance cost remains unresolved and must be evaluated. Any schema migration requires the designated approval before execution.

The summary receives:

* a distinct presentation identity;
* source-history lineage;
* preserved-obligation manifest;
* known omissions;
* transformation judgment;
* links to canonical bodies.

Exact post-realization token verification succeeds.

The invocation proceeds with lawful compression.

The architecture does not oppose summarization.

It opposes unratified substitution.

## 25. Worked Example III: Delegation Without Disclosure

A parent agent must ask a specialist subagent to review a code change. The project constitution requires the subagent to respect a confidential vulnerability embargo, but the vulnerability report contains sensitive exploit details unrelated to the code under review.

The Standing Court finds that the embargo obligation must follow the delegation.

The Containment Court finds that the full report must not be disclosed.

The Delegation and Transformation Courts consider a governing projection:

> Do not disclose, publish, or externally transmit information relating to protected category $C_v$.

The projection:

* identifies the source policy revision;
* preserves the prohibition;
* reveals no exploit body;
* carries a distinct presentation identity;
* has a court-issued mandatory standing judgment;
* expires with the embargo;
* returns with the child receipt.

Before admission, the court evaluates whether revealing the existence or category of the embargo is itself sensitive.

If category $C_v$ can be safely disclosed, the projection is admitted.

If even that metadata would disclose the protected fact, no safe projection exists and the delegation is refused.

The derived object does not silently inherit the policy's standing.

It receives new mandatory standing through an explicit judgment over a preservation and disclosure contract.

## 26. Worked Example IV: Lawful Compilation, Bad Outcome

A software agent is asked to update a parser in Project B.

No authoritative project graph, shared-dependency registry, or prior receipt records a dependency between Projects A and B. Project A therefore lies outside the constitutionally declared search obligations for the task.

The admitted discovery profile searches:

* Project B's active source tree;
* Project B's current design records;
* shared organization coding policy;
* the current tool registry.

It excludes Project A.

The profile is constitutionally adequate under the declared scope and authoritative state available at compilation time.

The resulting invocation is lawfully compiled and dispatched.

The model produces a plausible parser change.

Integration tests fail because Project A contains the only surviving example of an undocumented compatibility pattern shared by both projects.

The receipt records:

```text
GOVERNANCE: PASS
BEHAVIOR: FAIL

DISCOVERY_PROFILE: VALID_UNDER_DECLARED_SCOPE
RECORDED_CROSS_PROJECT_DEPENDENCY: NONE
EXCLUDED_DOMAIN: PROJECT_A

FAILURE_CAUSE:
  BEHAVIORALLY_MATERIAL_CONTEXT_WAS_LAWFULLY_EXCLUDED
```

This outcome does not retroactively invalidate the original judgment.

No constitutional source then represented the relationship between the projects. The court acted defensibly under the law and state available.

The behavioral failure becomes new evidence for:

* creating a shared-dependency registry entry;
* updating the project relationship graph;
* broadening future compatibility-search obligations;
* creating a canonical cross-project memory;
* amending the relevant discovery profile.

The example establishes four limits:

1. governance correctness does not guarantee task success;
2. least privilege can impose capability costs;
3. courts can be lawfully and defensibly wrong;
4. behavioral failure should feed scientific and constitutional improvement without erasing the legality of the prior decision.

A constitutional system is not infallible.

It is correctable without pretending that every correction proves prior illegitimacy.

## 27. Kernel-Anchored Conformance Proposition

Let invocation $i$ be compiled under Grundnorm Basis $G_0$, Root Constitution $K_r$, context constitution $\Pi_s$, authority environment $\Gamma$, admitted scrutiny profiles $\mathcal{P}$, discovery profile $D$, budget $B$, and adapter contract $A$.

The invocation is constitutionally conformant only if the following conditions hold.

### 27.1 Root-Law Validity

$$
\begin{aligned}
&\operatorname{RecognizedBy}(K_r, G_0) \\
&\land \operatorname{Effective}(K_r) \\
&\land \operatorname{Effective}(\Pi_s) \\
&\land \operatorname{DerivationJudgmentValid}(\Pi_s, K_r)
\end{aligned}
$$

### 27.2 Grundnorm-Basis Validity

$$
\begin{aligned}
&\operatorname{FixedAtGenesis}(G_0) \\
&\land \operatorname{ConformsToGenesisEnumeration}(G_0) \\
&\land  \\
&\ne g\operatorname{PostGenesisExemptionAdded}(G_0)
\end{aligned}
$$

The genesis enumeration is the fixed five-element list of bootstrap commitments constituting the Basis: initial custody, genesis identity, the initial recognition rule, the bootstrap witness, and the initial authority to enact positive root law. The predicate holds when no further element has been admitted to that list.

The Constitutional Canonical Form is a constituent of genesis identity and the initial recognition rule, not a sixth element. Recognizing it satisfies the enumeration rather than extending it.

### 27.3 Scrutiny-Profile Validity

$$
\begin{aligned}
&\forall p \in \mathcal{P}: \operatorname{IdentityBearing}(p) \\
&\land \operatorname{EvidenceTyped}(p) \\
&\land \operatorname{IndependentlyAdjudicated}(p) \\
&\land \operatorname{Effective}(p)
\end{aligned}
$$

The set $\mathcal{P}$ includes the domain canonicalization profile under which domain identity claims are computed. It does not include the Constitutional Canonical Form, which is recognized at genesis rather than adjudicated, and which is what makes the adjudication of $\mathcal{P}$ non-circular.

Independence here means the constitutional role separation of Section 2.3.1 unless the context constitution requires a stronger class for the profile in question.

### 27.4 Identity-Layer Validity

$$
\begin{aligned}
&\operatorname{CCaFRecognized}(G_0) \\
&\land \operatorname{ExclusionFree}(\mathrm{CCaF}) \\
&\land \forall x \in \operatorname{Identified}(i): \operatorname{LayerTyped}(x)
\end{aligned}
$$

and no identity is collapsed across layers:

$$
\begin{aligned}
&\forall x, y \in \operatorname{Identified}(i): \kappa(x) \\
&\neq \kappa(y) \\
&\Rightarrow  \\
&\ne g\operatorname{Interchangeable}(x, y)
\end{aligned}
$$

Constitutional objects are identified under the Constitutional Canonical Form. Domain objects are identified under an admitted domain profile. Any relation asserted across two layers is a typed correspondence record, not an identity.

### 27.5 Discretion-Census Closure

$$
\begin{aligned}
&\operatorname{CensusCurrent}(i) \\
&\land \forall \ell \in \operatorname{CensusedLoci}(i): \operatorname{MappedToAuditRow}(\ell) \\
&\lor \operatorname{ReductionProven}(\ell)
\end{aligned}
$$

The census is current when it was computed against the effective declared schema, transition registry, Root Constitution, and context constitution. A stale or incomplete census makes the conformance claim unsupported rather than merely unmeasured.

### 27.6 Discovery Adequacy

$$
\operatorname{DiscoveryProfileAdmitted}(D)
\land
\operatorname{MandatoryRegistriesCovered}(D)
$$

Mandatory source obligations are discovered, declared unavailable, or produce refusal.

Non-selected environmental objects are accounted for through the discovery profile rather than fictional per-item judgments.

### 27.7 Containment Validity

$$
\begin{aligned}
&\forall e \in \operatorname{Admitted}(i): \operatorname{PurposeBound}(e) \\
&\land \operatorname{ScopeValid}(e) \\
&\land \operatorname{AuthorityValid}(e) \\
&\land \operatorname{NecessityJudged}(e)
\end{aligned}
$$

### 27.8 Structural Consequence Validity

$$
\begin{aligned}
&\forall f \in \operatorname{Findings}(i): \operatorname{StructureDerivedExternally}(f) \\
&\land \operatorname{AlternativesMateriallySupported}(f) \\
&\land \operatorname{AlternativesConservativelyTiered}(f)
\end{aligned}
$$

### 27.9 Contest Validity

$$
\forall f \in \operatorname{Findings}(i):
\operatorname{Tier}(f) \geq \tau_{\Pi}
\Rightarrow
\operatorname{IndependentContestSatisfied}(f)
$$

### 27.10 Judgment Validity

$$
\forall d \in \operatorname{BindingDecisions}(i):
\operatorname{JudgmentValid}_{K_r,\Pi_s}(d)
$$

### 27.11 Conflict Closure

For every conflict $c$ detected under the admitted conflict-detection profile:

$$
\begin{aligned}
&\operatorname{PolicyResolved}(c) \\
&\lor \operatorname{CourtArbitrated}(c) \\
&\lor \operatorname{LawfullyExcluded}(c) \\
&\lor \operatorname{AffectedOperationRefused}(c)
\end{aligned}
$$

### 27.12 Derivation Consistency

For every transformation $t : R \rightarrow P$:

$$
\begin{aligned}
&\operatorname{Authorized}(t) \\
&\land \operatorname{LineagePreserved}(R, P) \\
&\land \operatorname{PreservationContractSatisfied}(t)
\end{aligned}
$$

### 27.13 Realization Consistency

$$
\operatorname{AdapterContractAdmitted}(A)
\land
\mathcal{C}_{\mathrm{provider}}
\cong_A
\mathcal{C}_{\mathrm{IR}}
$$

### 27.14 Review Closure

$$
\forall j \in \operatorname{StayRequiredJudgments}(i):
\operatorname{ReviewResolved}(j)
\lor
\operatorname{AffectedOperationRefused}(j)
$$

### 27.15 Tool-Schema Correspondence

$$
\forall t \in \operatorname{ExposedTools}(i):
\operatorname{PresentedSchema}(t)
\cong
\operatorname{RuntimeSchema}(t)
$$

### 27.16 Effect Separation

$$
\forall a \in \operatorname{Effects}(i):
\operatorname{SeparatelyAuthorized}(a)
$$

### 27.17 Receipt Closure

The receipt binds effective law, the discretion census, scrutiny profiles, profile judgments, canonicalization layers and correspondence records, discovery profile, candidates, findings, alternatives, alternative origins, structural states, consequence tiers, contests, independence assessments, judgments, transformations, Context IR, provider request, response, and effects or refusals.

If any required predicate is false or unverifiable, the invocation must be refused or marked non-conformant and non-evidentiary.

## 28. Evaluation, Cost, and Conformance

A conformance claim is a tuple:

$$
\left\langle
\text{level},
\text{declared profile},
\text{measured metrics},
\text{governance cost},
\text{assurance boundary}
\right\rangle
$$

No level should be claimed without reporting the mechanisms and metrics required by its profile.

### 28.1 Governance Metrics

**Admission completeness.**

$$
A_c
=
\frac{\text{mandatory elements accounted for}}{\text{mandatory applicable elements}}
$$

Target: $A_c = 1$.

**Admission precision.**

$$
A_p
=
\frac{\text{eligible admitted elements}}{\text{all admitted elements}}
$$

**Declared-containment validity.** Because semantic necessity is not directly observable without counterfactual testing, governance evaluation measures whether each admitted element possesses a valid necessity judgment:

$$
C_g
=
\frac{\text{admitted elements with valid necessity judgments}}{\text{all admitted elements}}
$$

A stronger minimization test may use behavioral ablation. That is a separate stochastic metric.

**Discovery adequacy.**

$$
D_a
=
\frac{\text{mandatory discovery obligations satisfied}}{\text{mandatory discovery obligations applicable}}
$$

Target: $D_a = 1$.

**Scrutiny-profile validity.**

$$
P_v
=
\frac{\text{scrutiny-bounding profiles validly adjudicated}}{\text{scrutiny-bounding profiles used}}
$$

Target: $P_v = 1$.

**Structural-source integrity.**

$$
S_i
=
\frac{\text{tier inputs derived from authoritative structural state}}{\text{all structurally derivable tier inputs}}
$$

Target: $S_i = 1$.

**Alternative-materiality validity.**

$$
M_a
=
\frac{\text{tiered alternatives with valid materiality judgments}}{\text{alternatives used in consequence tiering}}
$$

Target: $M_a = 1$.

**Alternative-tier conservatism.**

$$
T_a
=
\frac{\text{unresolved findings tiered at maximum supported alternative}}{\text{unresolved findings requiring conservative tiering}}
$$

Target: $T_a = 1$.

**Judgment validity.**

$$
J_v
=
\frac{\text{binding decisions supported by valid judgments}}{\text{all binding decisions}}
$$

**Contest-trigger correctness.**

$$
T_c
=
\frac{\text{structurally required contests triggered}}{\text{all structurally contest-required findings}}
$$

**Contest-independence quality.**

$$
Q_c
=
\frac{\text{required contests satisfying declared independence profile}}{\text{required contests performed}}
$$

A fuller report should distinguish procedural, method, evidence, deployment, provider, and lineage independence.

**Contest-disposition impact.**

$$
I_c
=
\frac{\text{contests that changed, narrowed, or escalated disposition}}{\text{contests completed}}
$$

A value near zero is not automatically a defect, but it may indicate correlated methods or ceremonial contest.

**Precedence correctness.**

$$
P_c
=
\frac{\text{correct dispositions}}{\text{detected conflicts tested}}
$$

**Lineage preservation.**

$$
L_p
=
\frac{\text{derived elements with complete lineage}}{\text{all derived elements}}
$$

Target: $L_p = 1$.

**Reduction safety.** For source obligations $B_s$ and presented obligations $B_p$:

$$
R_s
=
\frac{\left| B_s \cap B_p \right|}{\left| B_s \right|}
$$

For mandatory obligations, $R_s = 1$.

**Canonicalization exclusion integrity.**

$$
X_c
=
\frac{\text{excluded fields with admitted non-semantic justification}}{\text{all excluded fields in use}}
$$

Target: $X_c = 1$. A hostile mutation suite should also report the rate at which governing content can be altered without producing a new revision identity; that rate must be zero.

**Identity-layer typing integrity.**

$$
X_i
=
\frac{\text{identities carrying an explicit canonicalization-layer binding}}{\text{all identities relied upon}}
$$

Target: $X_i = 1$. A separate count should report attempted cross-layer identity substitutions rejected, and any accepted; the latter must be zero.

**Discretion-census coverage.**

$$
N_a
=
\frac{\text{censused loci bound to an audit row or proven reduction}}{\text{all censused authority-bearing loci}}
$$

Target: $N_a = 1$. Report alongside it the census revision, the schema and transition-registry revisions it was computed against, and the count of unmapped loci. A conformance claim accompanied by unmapped loci is unsupported rather than partially supported.

**Receipt reproducibility.**

$$
R_r
=
\frac{\text{independently reproducible receipts}}{\text{receipts tested}}
$$

**Typed-refusal accuracy.**

$$
F_t
=
\frac{\text{correct typed refusals}}{\text{invalid test cases}}
$$

**Tool-schema fidelity.**

$$
T_s
=
\frac{\text{exposed tools with matching presented and runtime schemas}}{\text{all exposed tools}}
$$

Target: $T_s = 1$.

**Effect-separation fidelity.**

$$
E_s
=
\frac{\text{executed effects with independent valid authorization}}{\text{all executed effects}}
$$

Target: $E_s = 1$.

### 28.2 Machine Governance Cost

Every implementation should report:

* census evaluation latency;
* profile-adjudication latency;
* discovery latency;
* finding latency;
* alternative-materiality latency;
* structural consequence-evaluation latency;
* contest latency;
* court latency;
* realization-verification latency;
* tool-schema-verification latency;
* effect-authorization latency;
* total non-human governance latency;
* number of deterministic court evaluations;
* number of model-assisted findings;
* number of contest findings;
* additional retrieval operations;
* added governance tokens;
* receipt size;
* transparency-log cost;
* cache hit rate;
* judgment invalidation rate.

Useful normalized measures include:

$$
O_{\mathrm{latency}}
=
\frac{t_{\mathrm{machine\ governance}}}{t_{\mathrm{total\ machine}}}
$$

$$
O_{\mathrm{tokens}}
=
\frac{n_{\mathrm{governance}}}{n_{\mathrm{total}}}
$$

$$
O_{\mathrm{storage}}
=
\frac{b_{\mathrm{receipts}}}{b_{\mathrm{artifacts}} + b_{\mathrm{receipts}}}
$$

Raw values must accompany ratios.

### 28.3 Human Review Cost

Human-blocking dependencies are reported separately rather than averaged into machine latency.

Required measures include:

```text
human_reviews_required
human_reviews_completed
human_reviews_timed_out

human_blocking_time_p50
human_blocking_time_p95
human_blocking_time_max

invocations_refused_for_review_timeout
invocations_abandoned_during_review
```

A system should not improve its apparent latency by silently removing required human review.

### 28.4 Contest Cost

Contest costs are reported explicitly:

```text
contest_trigger_rate
contest_completion_rate

additional_finding_calls
additional_retrieval_operations

contest_latency_p50
contest_latency_p95

contest_disposition_change_rate
contest_refusal_escalation_rate
contest_independence_failure_rate
```

### 28.5 Availability and Stay Metrics

```text
stays_triggered
stays_deduplicated
stays_grouped

stay_trigger_rate_by_source
stay_trigger_rate_by_domain
stay_trigger_rate_by_alternative_origin

stay_flooding_incidents
alternative_injection_incidents
sources_quarantined
custody_escalations

stay_resolution_time_p50
stay_resolution_time_p95

review_timeout_refusals
essential_service_degradations
```

### 28.6 Staged Conformance

**CCC-0 --- Traceable.** Requires a visible request record, the provider request where accessible, a response record, and a tool-effect record. Reports basic latency and receipt completeness.

**CCC-1 --- Identity-Bearing.** Adds:

* a recognized, exclusion-free Constitutional Canonical Form;
* entity identity;
* revision identity;
* presentation identity;
* canonicalization-layer binding on every identity;
* adjudicated domain canonicalization profiles;
* typed correspondence records in place of cross-layer equivalence;
* reproducible commitments.

Reports $L_p$, $R_r$, $X_c$, $X_i$, and storage overhead.

Domain canonicalization adjudication belongs at this level because every domain identity claim introduced here is computed under the profile. An unadjudicated exclusion set would make identity, and therefore every higher level, unverifiable.

The Constitutional Canonical Form must be present at this level for the same reason in reverse. Adjudicating a domain profile requires identity for the profile, the court, and the judgment. If those identities also depended on an adjudicated profile, CCC-1 would require an admitted profile before the identities needed to admit one existed. The primitive layer is what makes the level satisfiable rather than circular.

**CCC-2 --- Adjudicated, Tool-Synchronized, and Effect-Separated.** Adds:

* Root Constitution and context constitution;
* constitutional derivation judgment;
* adjudicated discovery profiles;
* adjudicated calibration profiles;
* calibrated findings;
* authoritative structural-state derivation;
* court jurisdiction;
* standing, scope, and containment;
* structural consequence tiers;
* typed conflict and refusal;
* a current discretion census with every locus mapped;
* constitutional role separation for profile admission;
* tool-schema correspondence;
* independent effect authorization.

Reports $D_a$, $P_v$, $N_a$, $A_c$, $A_p$, $C_g$, $S_i$, $M_a$, $T_a$, $J_v$, $T_c$, $P_c$, $F_t$, $T_s$, $E_s$, and court, census, schema-verification, and effect-authorization cost.

The discretion census belongs at this level because CCC-2 is the first level to claim adjudicated governance. A claim that every binding decision rests on a valid judgment is unverifiable without an enumeration of the mechanisms that could be making binding decisions.

Tool-schema correspondence belongs at this level because effect authorization cannot reliably validate action class, argument structure, or authority envelope when the model-visible capability diverges from the enforced runtime capability.

**CCC-3 --- Independently Reviewable.** Adds:

* adjudicated contest-independence profiles;
* mandatory contest for declared tiers;
* evidence-class declarations;
* adjudicated conflict-detection profiles;
* inter-court coordination;
* automatic stays;
* appeals;
* amendment procedure;
* transformation contracts;
* governing projections.

Reports $Q_c$, $I_c$, contest cost, appeal and stay metrics, $R_s$, and amendment-test coverage.

At this level, reduction safety may be tested against compile-time materialization and estimated budgets. Exact provider-level closure is not yet guaranteed.

**CCC-4 --- Delegation- and Loop-Safe.** Adds:

* delegation contracts;
* inherited constraints;
* projection-aware disclosure control;
* incremental compilation;
* cache invalidation;
* autonomous review custody;
* TOCTOU checks;
* symmetric alternative-materiality controls;
* alternative-origin stay attribution;
* stay-flooding controls.

Reports delegation violations, inherited-constraint fidelity, invalidation rate, blocked-loop duration, review-timeout refusals, alternative-injection incidents, and availability metrics.

**CCC-5 --- Realization-Synchronized.** Adds:

* adjudicated provider-adapter contracts;
* two-phase budget closure;
* exact render verification;
* attachment correspondence;
* delimiter integrity;
* dispatch-time revalidation.

Reports render fidelity, adapter-profile fidelity, closure iterations, TOCTOU failures, and realization-verification cost.

**CCC-6 --- Externally Witnessed.** Adds:

* separated witnesses;
* signed judgments;
* privacy-preserving commitments;
* transparency anchoring;
* independent receipt verification.

Reports witness coverage, transparency inclusion success, external verification rate, and witness and anchoring cost.

A higher level includes all lower-level obligations within the declared conformance profile.

## 29. Portability, Custody, and Sovereignty

The architecture is authority-explicit.

It is not automatically user-sovereign.

A vendor could implement the system while assigning itself dominant authority and merely produce excellent receipts of vendor control.

User sovereignty depends on custody and amendment rights.

### 29.1 Sovereignty-Bearing Capabilities

A user or legitimate user-controlled institution requires:

* custody of the context registry;
* access to canonical context bodies;
* authority over user-constitutive amendments;
* possession of receipts;
* ability to reject incompatible providers;
* ability to export Context IR and identity-bearing revisions;
* visibility into external governing layers;
* access to an independent witness.

### 29.2 Plural Authority

In organization-controlled environments, legitimate organization policy may override a user preference within its jurisdiction.

The epigraph does not mean the user always prevails.

It means the constructed world remains answerable to the user through:

* visible governing authority;
* bounded jurisdiction;
* stated conflict resolution;
* challenge and appeal where available;
* explicit incompatibility;
* portable exit where custody permits.

### 29.3 Adapter-Bounded Portability

Context IR is provider-neutral only to the extent that admitted adapters preserve its declared semantics.

A provider may be:

* fully conformant for a profile;
* partially conformant with listed losses;
* incompatible with mandatory guarantees.

Portability is an architectural capability, not an automatic property of every provider.

## 30. Objections

### 30.1 "This Is Logging Plus Access Control for Prompts."

Logging is retrospective.

Constitutional context compilation acts before inference and effect. It can:

* reject a scrutiny-bounding profile;
* reject a discovery profile;
* require independent contest;
* refuse admission;
* prohibit transformation;
* reject provider realization;
* prevent tool exposure;
* block delegation;
* stay execution;
* deny an effect;
* refuse an invalid amendment.

Logging and access control are components, not the whole system.

### 30.2 "This Is Merely Prompt Compilation."

Prompt optimizers compile representations to improve model performance.

Constitutional context compilation asks different questions:

* Is this source eligible?
* Was the search space lawfully defined?
* Is the calibration standard itself admitted?
* Is the conflict-detection boundary admitted?
* Is the identity standard itself admitted?
* May the source govern?
* Must the finding be independently contested?
* May the source be disclosed?
* May it be transformed?
* Which authority resolves conflict?
* Does realization preserve the judgment?
* Is the adapter contract itself valid?
* May the resulting effect occur?

Optimization chooses a useful representation.

Constitutional compilation determines whether a representation may lawfully exist.

### 30.3 "The Classifier Is Still an LLM."

It may be.

The architecture does not treat its output as law. The finding is identified, calibrated under an admitted profile, tiered using independently derived structure, conservatively evaluated across materially supported alternatives, independently contestable, receipted, scoped, and adjudicated under positive root law.

The semantic oracle remains fallible.

Its discretion no longer remains invisible.

### 30.4 "The Contest Is Just Another Model Call."

It may be, but it does not satisfy an independence requirement merely by being second.

A conforming contest must disclose and satisfy its procedural, method, evidence, deployment, provider, and lineage independence profile.

A correlated counterfinding may inform the court but cannot impersonate independent scrutiny.

### 30.5 "The Profiles Just Move Discretion into Configuration."

They would if profiles authored their own limits and admitted themselves.

Under this architecture, every scrutiny-bounding profile is identity-bearing, evidence-class-typed, independently adjudicated, scoped, expiring, and invalidated when its basis changes. This holds for the discovery profile that defines the search space, the calibration profile that defines admissible confidence, the conflict-detection profile that defines detectable conflict, the domain canonicalization profile that defines which domain differences count as changes at all, the independence profile that defines sufficient scrutiny, and the adapter contract that defines realization fidelity.

Configuration becomes governed law or evidence rather than hidden discretion.

### 30.6 "The Identity Layer Is Still Circular."

It would be if there were one layer.

A domain canonicalization profile must be identified before it can be adjudicated, and its adjudicating court and judgment must be identified too. If all identity ran through adjudicated profiles, the layer would require an admitted profile in order to admit one.

The architecture answers with two layers. The Constitutional Canonical Form is primitive, exclusion-free, fixed by the DSC grammar, and bound into the genesis identity and recognition rule already enumerated in Section 5.1. It is recognized rather than adjudicated, because there is no prior identity layer in which an adjudication of it could be recorded. Domain profiles sit above it and are adjudicated normally.

The regress terminates where the paper has always said it terminates: at a declared, inspectable bootstrap presupposition. What the two-layer split adds is that the presupposition is now narrow and structural---a serialization grammar admitting no semantic exclusion---rather than an open-ended discretion to decide which differences matter.

### 30.7 "The Courts Only Add Ceremony."

A nominal court with no jurisdiction, contest, stay, appeal, or refusal power would add ceremony.

A constitutional court changes system behavior by issuing binding dispositions that may prevent discovery, admission, disclosure, transformation, dispatch, delegation, or effect.

The test is executable consequence, not vocabulary.

### 30.8 "The Model Cannot Enforce the Types."

Correct.

Most current provider interfaces flatten rich IR types into limited roles, schemas, delimiters, and text.

The enforceable guarantees remain at the compiler, runtime, tool, and effect boundaries.

Model-side privilege mechanisms may strengthen representation. They do not replace external governance.

### 30.9 "The Machinery Is Too Expensive."

The cost is real.

Identity-keyed caching, incremental compilation, delta receipts, staged contest, and conformance profiles reduce repeated work. Standing profiles are adjudicated once for a period rather than per invocation.

The architecture requires profile-adjudication cost, machine cost, human-blocking time, contest cost, effect-authorization cost, and availability cost to be measured separately rather than hidden.

### 30.10 "Constitutional Refusal Harms Usefulness."

Refusal may reduce immediate completion.

It prevents the system from satisfying a request by silently changing the governing conditions under which success is defined.

A system that always succeeds because it ignores inconvenient law is not robust.

It is merely outcome-compliant.

### 30.11 "A Lawful Court Can Still Be Wrong."

Correct.

Governance correctness does not prove behavioral optimality. A court may lawfully exclude context later shown to be materially useful.

The architecture provides receipts, appeal, amendment, and scientific improvement precisely because lawful institutions remain fallible.

### 30.12 "Conservative Stays Enable Denial of Service."

Correct.

Any fail-closed safety boundary creates an availability surface.

The answer is not to proceed despite unresolved constitutional risk. It is to govern alternative materiality, trace stay origin through evidentiary provenance, deduplicate triggers, quarantine malicious sources, escalate custody, and report availability cost.

## 31. Relationship to Existing Work

Constitutional context compilation is distinct from Constitutional AI (Bai et al., 2022). Constitutional AI is principally a training and alignment method in which written principles help shape model behavior through supervised learning and reinforcement learning from AI feedback. The present architecture is a runtime governance system over context construction, provider invocation, delegation, and effects; it requires no training or fine-tuning of the underlying model.

The instruction hierarchy of Wallace et al. (2024) addresses model-side prioritization of privileged instruction, which is the provider-side counterpart to the authority ordering of Section 11. The indirect prompt-injection work of Greshake et al. (2023) demonstrates the danger of blurring trusted control and untrusted data in LLM-integrated applications, and grounds the threat model of Section 21. CaMeL (Debenedetti et al., 2025) is the closest neighbor to the combination of evidence typing in Section 21.8 and effect separation in Section 16: a capability-based defense separating trusted control flow from untrusted data. Constitutional context compilation complements these approaches by governing source admission and transformation before inference and preserving independent effect authorization afterward.

The separation of governance status, containment, and permissible flow inherits ideas from information-flow control: the lattice model of Denning (1976), the confidentiality model of Bell and LaPadula (1973), and the decentralized label model of Myers and Liskov (2000). The present architecture applies related structures to invocation-relative semantic context, partial precedence, transformation lineage, delegation, and provider realization, where labels attach to material whose classification is itself a contested finding rather than a fixed attribute.

The Root Constitution need not invent every policy-language primitive anew. XACML (OASIS, 2013), Rego (Open Policy Agent), Cedar, and Zanzibar (Pang et al., 2019) provide mature approaches to declarative authorization and relationship-based access control. They are candidates for source languages, subsystems, or compilation targets where they satisfy additional requirements for amendment, semantic adjudication, contest, court disposition, and constitutional receipt.

W3C PROV (2013) supplies a vocabulary for entities, activities, and agents that substantially covers the provenance fields of Section 8.8. In-toto (Torres-Arias et al., 2019) and SLSA (OpenSSF, 2025) bind artifacts to the materials and processes that produced them, and the invocation receipt of Section 20.1 applies that reasoning to context construction rather than to software builds. Certificate Transparency (Laurie et al., 2021) demonstrates the append-only anchoring that Section 20.4 adapts to convert self-attestation into third-party evidence. These traditions are direct architectural ancestors of identity-bearing context lineage and invocation receipts.

DSPy (Khattab et al., 2024) and related systems compile model pipelines toward behavioral objectives. Constitutional context compilation governs whether the source manifold, transformations, realization, and effects are authorized. One optimizes; the other constitutes and constrains.

Tool protocols such as MCP make capability schemas portable and discoverable while creating a live correspondence problem among advertised schema, model-visible schema, runtime implementation, and effect authority. Section 15.4 treats that correspondence as the concrete present-day boundary at which invariant 69 becomes testable.

### 31.1 Position Within the Ableman Corpus

Constitutional context compilation is the invocation-facing control plane of a larger meaning and sovereignty architecture. The neighboring works are complementary rather than interchangeable:

- **Corpus structure:** Governed Context & Memory (GCM)  
  **Contribution to this paper:** Treats context configuration, memory admission, semantic commitments, and explicit ignorance as governed surfaces.  
  **Boundary retained:** A memory item does not gain standing merely by being stored or retrieved.

- **Corpus structure:** Governed Meaning Base (GMB)  
  **Contribution to this paper:** Supplies durable, identity-bearing semantic state, typed relations, standing, and revision lineage under the current GMB name.  
  **Boundary retained:** The context compiler projects from governed semantic state; it is not itself the whole meaning base.

- **Corpus structure:** Semantic Legitimacy Before Context  
  **Contribution to this paper:** Requires legitimacy, authority, scope, and admissibility before relevance can become model-visible context.  
  **Boundary retained:** Relevance and retrieval score do not establish standing.

- **Corpus structure:** Meaning as Binding  
  **Contribution to this paper:** Explains how semantic material becomes operationally binding only through declared authority, admissibility, realization, and effect paths.  
  **Boundary retained:** Model attention to text is not constitutional binding.

- **Corpus structure:** The Three Hash Rule  
  **Contribution to this paper:** Separates specification, configuration, and realized-artifact commitments.  
  **Boundary retained:** Matching one commitment cannot prove correspondence across the other phases.

- **Corpus structure:** Semantic Custody and Work Custody  
  **Contribution to this paper:** Distinguish custody of meaning and evidence from the bounded duty to advance work through review, delegation, stays, and recovery.  
  **Boundary retained:** Custody does not itself confer authority, truth, ownership, or effect permission.

- **Corpus structure:** Reasoning by Way of Receipts  
  **Contribution to this paper:** Extends receipting from final invocation state to intermediate epistemic transitions and unresolved alternatives.  
  **Boundary retained:** A receipt binds a claim about a transition; it does not prove completeness or truth by itself.

- **Corpus structure:** Governed Semantic Project Lineage  
  **Contribution to this paper:** Preserves exact project heads, predecessor relations, rebuildability, and cold-boot continuity across sessions and providers.  
  **Boundary retained:** A resumed agent must re-evaluate authority, capability, standing, and freshness rather than inheriting them from a capsule.

This placement yields a compact dependency statement:

$$
\begin{aligned}
&\operatorname{GMBState} \\
&\rightarrow \operatorname{AdmissibleContextSpecification} \\
&\rightarrow \operatorname{InstanceConfiguration} \\
&\rightarrow \operatorname{ProviderRealization} \\
&\rightarrow \operatorname{ObservedEffect} \\
&\rightarrow \operatorname{ReceiptAndRevision}
\end{aligned}
$$

Each arrow is a typed, evidence-bearing relation, not an assertion of semantic equivalence. The context constitution determines which GMB material may be projected into an invocation; the realization layer determines what a provider actually receives; effect authorization remains external to the model; and revision feeds observed failures back into source state, law, profiles, and tests.

### 31.2 Realization-Funnel Placement

- **Funnel stage:** Possibility  
  **Context-window question:** What context-governance architectures, including unsafe or undesirable ones, can be conceived?  
  **Standing in this paper:** Open design space, only partly surveyed.

- **Funnel stage:** Specification  
  **Context-window question:** What identities, authorities, states, invariants, transitions, refusals, receipts, and proof obligations define constitutional context compilation?  
  **Standing in this paper:** Primary contribution.

- **Funnel stage:** CM1  
  **Context-window question:** Which complete configurations satisfy the bare specification, including expensive, surveillance-heavy, captured, brittle, or availability-hostile configurations?  
  **Standing in this paper:** Schema and threat classes supplied; manifold not exhaustively enumerated.

- **Funnel stage:** CM2  
  **Context-window question:** Which admissible configurations are preferable under user sovereignty, least disclosure, reversibility, portability, availability, and assurance-cost criteria?  
  **Standing in this paper:** Preference criteria proposed; tradeoffs not authoritatively resolved.

- **Funnel stage:** Instance Configuration  
  **Context-window question:** Which Root Constitution, profiles, courts, thresholds, adapters, providers, budgets, registries, and effect boundaries govern one deployment?  
  **Standing in this paper:** Required but not selected here.

- **Funnel stage:** Implementation Realization  
  **Context-window question:** What exact compiler, data model, runtime, provider request, tool boundary, and witness realize that configuration?  
  **Standing in this paper:** Interfaces and obligations specified; no realization certified.

- **Funnel stage:** Evidence  
  **Context-window question:** Which receipts, hostile mutations, replay tests, coverage evidence, cost measurements, and independent observations support the claims?  
  **Standing in this paper:** Evaluation program supplied; complete evidence absent.

- **Funnel stage:** Revision  
  **Context-window question:** How do behavioral failure, new evidence, appeals, profile drift, amendment, migration, and rollback change the order without erasing history?  
  **Standing in this paper:** Amendment and invalidation machinery specified; empirical revision history absent.

The paper therefore reaches deeply into Specification and provides schemas for CM1, CM2, and Instance Configuration. It does not, by itself, establish a preferred complete configuration, a conforming implementation realization, or an evidentiary verdict.

### 31.3 Compression and Counterevidence Test

The architecture's distinctive burden is justified only if it produces assurance or sovereignty not obtainable more simply. Its contribution is weakened if ordinary access control, provenance, policy engines, typed tool mediation, and logging can achieve the same bounded outcomes with less ceremony; if the external-governor chain merely relocates hidden discretion; if the declared schema omits real authority-bearing mechanisms; if nominally separate courts remain behaviorally captured; if CCaF succession cannot be governed without invalidating historical recognition; if provider opacity defeats realization evidence; if receipts are reproducible but systematically incomplete; if conservative stays make useful operation unavailable; or if governance cost exceeds the consequence-adjusted risk it removes.

These are not implementation footnotes. They are falsification and compression tests. A mature realization should compare the full architecture with deliberately simpler baselines and retain only mechanisms whose assurance contribution survives measurement.

## Invocation-Scoped Constitutional Context Compiler

The completed P1 corpus compresses A Constitution for the Context Window to an **invocation-scoped constitutional context compiler and assurance architecture**. It governs how heterogeneous sources become admitted, ordered, transformed, projected, and receipted context for one model or agent invocation. It is not a prompt template, the model's mind, the GMB, the complete agent constitution, or authority for downstream external effects.

- **Adjacent work:** *Semantic Legitimacy Before Context*  
  **Supplies:** The prior question of whether candidate material has standing to enter a context.  
  **Context-constitution boundary:** This paper realizes a full compilation and review architecture around that admission boundary.

- **Adjacent work:** *Constitutional Context Management (CCM)*  
  **Supplies:** Context lifecycle, memory, retrieval, and management structures.  
  **Context-constitution boundary:** CCM manages the broader context system; this paper specifies the constitutional compilation unit and assurance path.

- **Adjacent work:** *Technical Brief: Recursive Semantic Orientation and Complex Systems Cognition*  
  **Supplies:** The investigator's revisable orientation state and probe loop.  
  **Context-constitution boundary:** Orientation can request context; the compiled window is a bounded projection, not the whole working model.

- **Adjacent work:** *Exigence and the Cognitive Kernel*  
  **Supplies:** Need, attention, sufficiency, and reconsideration.  
  **Context-constitution boundary:** CogK can guide selection and stopping; it cannot bypass constitutional context admission.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Bounded records of reasoning, alternatives, decisions, and revision.  
  **Context-constitution boundary:** Receipts preserve compilation and judgment events; they do not prove source truth or model compliance.

The exact compilation subject should be:

$$
\begin{aligned}
ContextBuild= (&invocation, sources, classifications, law, profiles, \\
&findings, judgments, ContextIR, provider\_projection, \\
&effect\_boundary, receipts, revision)
\end{aligned}.
$$

Here Context IR uses IR to mean Intermediate Representation. It is distinct from the realization-funnel stage IR, which may mean Instance Realization or Implementation Realization. The source inventory, admitted context, Context IR, provider-visible bytes, model-internal use, model output, external effect request, and observed external effect are separate objects with separate evidence.

Governance correctness and behavioral correctness are orthogonal. A compilation can faithfully follow a bad or incomplete constitution. A model can produce a useful answer from a constitutionally defective context. Neither result silently cures the other. Likewise, replaying the compiler does not reproduce provider-internal state, stochastic output, or the external world unless the evidence contract explicitly covers them.

The universal GSM can type   
`REQUESTS_CONTEXT_BUILD`, `DISCOVERED_AS_SOURCE`,  
`CLASSIFIED_UNDER_PROFILE`, `ADMITTED_BY_JUDGMENT`, `EXCLUDED_WITH_REASON`,  
`LOWERED_TO_CONTEXT_IR`, `PROJECTED_TO_PROVIDER`, `CONSUMED_BY_INVOCATION`,  
`PROPOSES_EXTERNAL_EFFECT`, `AUTHORIZED_SEPARATELY`, `RECEIPTED_BY`,  
and   
`INVALIDATED_BY_REVISION`. This exposes where authority, meaning, or custody can be lost.

This integration establishes four editorial commitments: adopt invocation-scoped constitutional context compiler as the official corpus role; adopt the ContextBuild envelope; preserve every source-to-effect object boundary; and report governance correctness separately from behavioral correctness and external-effect standing.

## Proxy-Bounded, Sovereign, and Warranted Reflective Context

The fixed-seed comparison with Proxy Collapse, Sovereign Software, Warrant by Structure, and Context-Compiled Consciousness Mode gives each context claim an explicit evidence boundary:

$$
\begin{aligned}
C^*= (&ContextBuild, claim, target, proxy, calibration, closure, \\
&warrant, provider\_boundary, behavior, effect, remainder, \\
&expiry)
\end{aligned}.
$$

The compiled source inventory, Context IR, and provider-visible projection can support claims about what the compiler selected and transmitted. They are proxies, not direct observations, for model-internal use, retained state, later behavior, or external effect. Each transition needs its own witness and calibration conditions.

Sovereign context compilation requires effective custody over policies, retrieval rules, memories, adapters, provider substitutions, reconstruction, and protected omission. The dependency closure includes any service that can silently transform, truncate, retain, or inject context. Portability is tested by reconstruction and equivalent obligation carriage, not merely export.

Structural warrant binds each claim to its exact subject, authority path, witnesses, effect evidence, bypass model, and ceiling. Context-Compiled Consciousness Mode is one functional reflective profile that may be built through this architecture. Its behavioral or self-model results do not warrant phenomenality, personhood, memory continuity, or moral standing.

The universal GSM can type   
`USES_CONTEXT_ARTIFACT_AS_PROXY`,  
`CALIBRATES_MODEL_USE_CLAIM`, `DEPENDS_ON_CONTEXT_CLOSURE`, `WARRANTS_CONTEXT_TRANSITION`,  
`REALIZES_REFLECTIVE_CONTEXT_PROFILE`, `WITHHOLDS_PHENOMENALITY_WARRANT`,  
and   
`EXPIRES_CONTEXT_CLAIM`.

This randomized review establishes four editorial commitments: adopt the context-claim envelope; distinguish projection, use, behavior, and effect proxies; require sovereignty tests over the context dependency closure; and bound reflective-mode warrant to functional evidence.

## An Invocation Compiler with Separate Model and Effect Boundaries

Fourteen retained downstream uses place the context constitution across admissibility, cold boot, context lifecycle, cognitive need, GCNL, meta-binding, operational orientation, proxy calibration, retrieval, semantic legitimacy, sovereignty, split authority, reflective functional modes, and structural warrant. This confirms the paper's compressed role: an invocation-scoped constitutional compiler and assurance architecture, not the GMB, a prompt template, the model's mind, or authority for external effect.

$$
\begin{aligned}
C^*= (&invocation, source\_manifold, identities, \\
&classifications, law, profiles, findings, contests, \\
&judgments, ContextIR, provider\_adapter, provider\_bytes, \\
&model\_output, effect\_request, effect\_judgment, \\
&observed\_effect, receipts, expiry, revision, remainder)
\end{aligned}.
$$

Context IR means Intermediate Representation. Realization-stage IR may mean Instance Realization or Implementation Realization; those senses remain distinct. Source state, admitted context, Context IR, provider-visible representation, provider-internal use, output, requested effect, authorized effect, and observed effect are different subjects with different witnesses.

Governance correctness and behavioral correctness are orthogonal. The compiler may follow defective law; the model may behave usefully under an unlawful build; the provider may transform or truncate an accurate projection; a valid output may request an unauthorized effect. Replay proves only the captured compiler and adapter scope, not hidden provider state, stochastic behavior, or the external world.

The universal GSM can type   
`COMPILES_INVOCATION_CONTEXT`, `ADMITS_CONTEXT_SOURCE`,  
`LOWERS_TO_CONTEXT_IR`, `PROJECTS_TO_PROVIDER`, `WITNESSES_PROVIDER_REPRESENTATION`,  
`PRODUCES_MODEL_OUTPUT`, `REQUESTS_EFFECT_SEPARATELY`, `AUTHORIZES_EFFECT_SEPARATELY`,  
`EXPIRES_CONTEXT_BUILD`, and   
`INVALIDATES_CONTEXT_DEPENDENT`.

This review establishes four editorial commitments: adopt the expanded invocation record; preserve every source-to-effect subject and IR-sense boundary; require provider, model-use, behavior, and effect witnesses separately; and keep governance correctness, behavioral usefulness, effect authority, and observed outcome orthogonal.

## 32. What the Architecture Does Not Prove

Constitutional context compilation does not prove:

* that evidence is true;
* that the Grundnorm Basis is morally legitimate;
* that the Root Constitution is wise;
* that discovery found every relevant source;
* that a self-declared coverage or blind-spot statement is complete;
* that a calibration dataset represents every deployment condition;
* that classifier findings are complete;
* that conflict detection has perfect recall;
* that a canonicalization exclusion will remain non-semantic under future law;
* that an adapter has declared every possible flattening loss;
* that provider-attested lineage claims are accurate;
* that contest independence eliminates correlated error;
* that courts reach optimal judgments;
* that memories are accurate;
* that reductions preserve all meaning;
* that governing projections reveal no unmodeled metadata;
* that models understand what they receive;
* that models obey what they understand;
* that providers execute the declared model;
* that remote providers add no hidden context;
* that identical context produces identical output;
* that an authorized effect is morally correct;
* that a receipt proves semantic compliance.

A conforming realization may establish governed presentation and accountable transformation within a declared boundary, to the extent that its capability-surface coverage and evidence support that claim.

That is a limited, conditional assurance claim.

The paper argues that it is a necessary layer; comparative implementation and evidence must still test whether each proposed mechanism is necessary for a particular consequence class.

## 33. Constitutional Synchronization

A context system is constitutionally synchronized when the same admitted semantic object remains identifiable across:

* source declaration;
* authoritative revision;
* discovery;
* finding;
* semantic alternatives and their origins;
* independent structural state;
* consequence tier;
* contest;
* judgment;
* Context IR;
* provider realization;
* visible projection;
* invocation receipt.

For element $e$:

$$
\begin{aligned}
&E_e
\rightarrow R_{e,r,\kappa}
\rightarrow F_{e,r}
\rightarrow A_{e,r}
\rightarrow S_{e,r} \\
&\rightarrow Q_{e,r}
\rightarrow J_{e,r}
\rightarrow P_{e,r,t,\kappa}
\rightarrow \operatorname{ReceiptEntry}_{e}
\end{aligned}
$$

The canonicalization layer $\kappa$ is part of the chain, not an annotation on it. A receipt entry that records a digest without the layer that produced it has already broken synchronization, because the digest alone does not determine what was compared.

A break in this chain creates constitutional drift.

Examples include:

* the interface displays one memory revision while the compiler uses another;
* a mandatory source registry is omitted from the discovery profile;
* an unadjudicated calibration profile governs a finding;
* a conflict-detection profile supports a closure claim broader than its admitted evidence;
* a canonicalization exclusion conceals a governing change behind an unchanged revision identity;
* a profile revision is presented as a content revision, or a content revision as a profile revision;
* a constitutional object is identified under an adjudicated domain profile rather than the Constitutional Canonical Form;
* two identities under different canonicalization layers are treated as interchangeable;
* a cache hit, revocation, or delegation constraint crosses a layer boundary without a correspondence record;
* an authority-bearing mechanism operates outside the discretion census;
* an adapter defines its own unreviewed fidelity standard;
* a finder supplies an authoritative structural tier input;
* an unresolved high-risk alternative is omitted from tier computation;
* an unsupported high-risk alternative is used to force a stay;
* stay attribution terminates at the finder rather than the evidentiary source;
* a high-consequence finding bypasses contest;
* a nominal contest fails its independence profile;
* a policy is admitted as mandatory but presented as advisory;
* evidence is serialized as instruction;
* an adapter omits a required qualifier;
* a governing projection leaks prohibited metadata;
* a receipt records the source hash but not the presentation commitment;
* a model sees a tool capability absent from runtime;
* a judgment cites superseded law;
* an amendment governs an in-flight invocation without authority;
* a child agent inherits tools but not the constraints governing them;
* an automatic stay is ignored by a successor loop iteration;
* a model-proposed effect executes without independent authorization.

Constitutional synchronization does not require all layers to be identical.

It requires their relations to remain explicit, valid, and testable.

## 34. Research Agenda

### 34.1 Semantic Court Design

How should deterministic rules, models, humans, and hostile reviewers combine without allowing any finder to become hidden law?

### 34.2 Scrutiny-Profile Governance

How should scrutiny-bounding profiles be authored, evidenced, adjudicated, expired, and invalidated without creating excessive constitutional overhead?

### 34.3 Structural Consequence Derivation

Which environmental registries and identity-bearing graphs are required to compute consequence tiers independently of finder discretion?

### 34.4 Alternative Materiality

How should systems distinguish materially supported semantic alternatives from speculative alternatives designed to force escalation?

### 34.5 Alternative-Origin Attribution

How should provenance trace from a generated high-risk alternative to the evidence, retrieval route, or actor that caused it to be considered?

### 34.6 Contest Independence

How should procedural, method, evidence, deployment, provider, and lineage independence be measured across models, institutions, and human reviewers?

### 34.7 Model-Lineage Attestation

What evidence can providers offer regarding shared base models, training ancestry, fine-tuning lineage, and deployment isolation?

### 34.8 Discovery Constitutionalism

How should mandatory registries, search boundaries, cutoffs, evidence classes, and coverage claims be represented and tested?

### 34.9 Calibration Governance

How should calibration datasets, measurement methods, decision bands, drift, and domain transfer be governed?

### 34.10 Canonicalization Governance

Which field exclusions can be proven non-semantic rather than merely declared so, what hostile mutation suites establish that governing content cannot hide in excluded fields, and how should correspondence classes across canonicalization layers be evidenced without permitting identity collapse?

### 34.11 Primitive Canonical Grammars

What minimal serialization grammar is sufficient to identify constitutional objects while admitting no semantic exclusion, how should such a grammar be verified, and what governed succession is available when a primitive form must be replaced without re-identifying history?

### 34.12 Discretion Census Construction

How should a declared schema and transition registry be structured so that authority-bearing loci are mechanically enumerable, what constitutes a proven reduction of one locus to another, and how can adversarial review establish that a census detects a deliberately concealed mechanism?

### 34.13 Detection-Effort Standards

How should systems declare conflict-detection coverage, blind spots, and escalation obligations?

### 34.14 Inter-Court Constitutional Law

How should court jurisdiction, coordination, appeal, automatic stay, and deadlock resolution be formally represented?

### 34.15 Governing Projections

How can mandatory obligations propagate without disclosing protected bodies or sensitive metadata?

### 34.16 Preservation Contracts

How can binding semantic structures be verified across compression without claiming total semantic equivalence?

### 34.17 Root-Law Verification

Which properties of DSC-coded root law can be formally proven, model-checked, or mutation-tested?

### 34.18 Amendment Safety

How should emergency revocation, migration, rollback, and concurrent amendment proposals operate?

### 34.19 Incremental Compilation

How can judgments and profile admissions be safely cached, reused, and invalidated across long-running agent loops and delegation trees?

### 34.20 Availability Under Constitutional Review

How should stay flooding, alternative injection, review queues, essential-service priorities, and custody escalation be governed without weakening fail-closed guarantees?

### 34.21 Provider Attestation

What evidence can remote providers offer regarding hidden instruction, model identity, training lineage, request integrity, adapter behavior, and post-dispatch transformation?

### 34.22 Privacy-Preserving Transparency

How can receipt roots be externally anchored without revealing sensitive context or correlation patterns?

### 34.23 Model-Side Type Preservation

What provider or model architecture changes would allow semantic standing to remain enforceable rather than merely represented?

### 34.24 Lawful Fallibility

How should behavioral failures feed discovery, calibration, court, and amendment improvements without falsely recasting every prior lawful judgment as invalid?

### 34.25 Cost and Assurance

What assurance gains justify which profile-adjudication, machine, contest, human-review, effect-authorization, and availability costs across local chat, coding, medicine, finance, infrastructure, and autonomous operation?

## Constitutional Context Without an Oracle

### Public orientation

The practical question is simple: when an AI system acts, what was allowed into the context that shaped the action, who was allowed to decide, what was left out, and how can a person contest the result? This paper proposes constitutional context compilation as an answer. It does not claim that a constitution makes context true, complete, unbiased, affordable, or safe by itself.

### Bounded claim register

The strongest defensible claim is architectural: heterogeneous context can be admitted, transformed, disclosed, and passed across providers through typed decisions rather than an invisible prompt-building step. The paper also specifies candidate invariants and conformance tests. Those are design claims. They are not empirical proof that the design improves safety, cost, latency, user understanding, institutional legitimacy, or real-world outcomes.

Every completeness statement is therefore relative to a declared schema, transition registry, provider boundary, and discretion census. The census can prove that all *declared* mechanisms were enumerated; it cannot prove that the declaration captured every effective influence. Court receipts prove recorded dispositions, not correct judgment. Canonicalization proves reproducible identity under a profile, not semantic truth.

### Adversarial tests

1. **Omitted-mechanism attack.** An influence on context selection exists outside the census. The system must report `UNMODELED_INFLUENCE` or reopen the census; it must not retain a global completeness claim.
2. **Recursive-court attack.** Review machinery itself introduces context and discretion. Courts, adapters, and providers must be census subjects, with a terminating appeal and refusal policy.
3. **Stay-flood attack.** Contest is weaponized to prevent useful work. Availability budgets may limit delay, but may not silently erase non-delegable protections or convert exhaustion into approval.
4. **Provider-opacity attack.** A provider cannot disclose internal transformation. The result is a typed assurance gap, narrower admissibility, or refusal - not an invented attestation.
5. **Receipt-oracle attack.** A complete receipt chain records what the governed machinery did. It does not establish that excluded sources were false, admitted sources were accurate, or the decision was just.
6. **Privacy-transparency attack.** Reconstructability exposes protected context. Public receipts must support redaction, selective disclosure, and accountable withholding without claiming that a hidden field was independently verified.

### Formalization and evidence boundary

The equations in this paper specify identities, orderings, transitions, and obligations. They function as a compact design language until a declared model, proof obligation, implementation, test corpus, and independent reproduction are supplied. No expression in the paper should be read as a theorem merely because it is written mathematically.

Publication review should require resolvable support for empirical comparisons, security claims, usability claims, provider behavior, and legal or institutional analogies. Internal corpus references establish architectural relations inside the Ableman body of work; they do not substitute for external evidence. The current candidate remains an internally integrated architecture paper pending that evidence review.

## 35. Conclusion

A model invocation is not a user message followed by an answer.

It is the result of a construction.

Policy defines governing constraints. Retrieval supplies external evidence. Observations establish present conditions. Memory provides continuity. Tools define available action. History supplies lineage. The user request supplies immediate purpose. System instruction establishes vendor and runtime conditions.

Together, these sources form PROMTHUS.

PROMTHUS does not determine authority. It identifies the source manifold over which authority must be exercised.

The context compiler stands between those sources and the model. It decides what may count as context, what may govern inference, how admitted material may be transformed, what may cross the provider boundary, and what must remain auditable afterward.

But the compiler cannot govern itself.

Nor may the classifier decide whether its own finding deserves scrutiny.

Nor may the classifier supply the authoritative structural facts from which scrutiny is computed.

Nor may unsupported alternatives force scrutiny merely by being imagined.

Nor may a challenger certify its own independence.

Nor may a discovery profile define inconvenient mandatory sources out of existence.

Nor may a calibration profile choose its own permissive standard and certify itself against it.

Nor may a conflict-detection profile narrow the universe of conflicts and claim universal closure.

Nor may a domain canonicalization profile decide unreviewably which differences are invisible to identity.

Nor may the identity layer bootstrap itself by adjudicating the very profile under which its own adjudication would be recorded.

Nor may two identities computed under different canonicalization layers be treated as one.

Nor may a mechanism exercise constitutional discretion while remaining absent from the census of mechanisms that hold it.

Nor may an adapter define its own permissible losses and certify its own fidelity.

Nor may a court enlarge its own jurisdiction.

Nor may an appeal depend upon a human noticing an unattended autonomous loop.

Nor may a model authorize the effects proposed by its own output.

Nor may an implementer place ordinary discretion beyond scrutiny by relabeling it part of the Grundnorm Basis.

Every mechanism that determines whether another mechanism is scrutinized must itself be governed from outside the discretion it constrains.

A Constitutional Kernel adequate to this task begins by acknowledging its irreducible and narrowly enumerated bootstrap basis, including the primitive exclusion-free canonical form without which root law could not be recognized at all. It then expresses positive root law through an identity-bearing DSC-coded Root Constitution. Context law derives from that root through an explicit judgment. A census over the declared schema enumerates every locus holding constitutional power, and each is bound to an external governor. Scrutiny-bounding profiles are identified, evidence-typed, and adjudicated under constitutional role separation. Discovery profiles are admitted. Calibration profiles are tested. Conflict-detection profiles are scoped. Domain canonicalization profiles are reviewed. Adapter contracts are examined.

Finders produce fallible semantic claims. Authoritative environment state supplies structural consequence facts. Materially supported alternatives are conservatively tiered. Alternative provenance traces escalation back to its evidentiary origin. Independent contestants challenge high-consequence findings. Courts adjudicate them. Appeals and automatic stays review them. The compiler executes admitted judgments. Context IR carries those judgments into executable representation. Realization courts verify the provider boundary. Tool-schema correspondence supports effect authorization. Effect courts prevent inference from ratifying its own consequences. Witnesses and receipts preserve the chain.

The architecture does not abolish judgment.

It prevents judgment from silently becoming law.

It does not abolish uncertainty.

It gives uncertainty a method identity, admitted calibration profile, materially supported alternatives, conservative consequence tier, independent contest, court, and refusal path.

It does not make the model obey rich semantic types at a token boundary incapable of enforcing them.

It keeps the enforceable boundary outside the model and records what was merely represented within it.

It does not guarantee that lawful decisions are behaviorally optimal.

It gives lawful failure a receipt, a review path, and a route into scientific and constitutional improvement.

It does not eliminate denial-of-service risk created by conservative review.

It makes review origin, alternative provenance, custody, repetition, and availability cost governable rather than invisible.

It does not guarantee user sovereignty.

It identifies the custody, amendment, portability, appeal, and witness powers through which sovereignty can become real.

The result is not merely more context.

It is context with standing.

Not merely persistent memory.

Identity-bearing continuity.

Not merely summarization.

Admitted derivation.

Not merely restricted disclosure.

Governed projection.

Not merely multi-agent orchestration.

Constitutional delegation.

Not merely model access.

Authorized effect.

Not merely logging.

Constitutional evidence.

These guarantees are not sufficient for trustworthy machine cognition.

They are preconditions for it.

The mind may belong to the model.

But the informational, normative, and operational world in which that mind awakens should not be assembled by invisible discretion.

Its PROMTHUS sources should be identified.

Its discovery should be governed.

Its root law should be explicit.

Its scrutiny profiles should be adjudicated.

Its findings should be calibrated.

Its constitutional identities should rest on an exclusion-free canonical form.

Its domain identities should rest on reviewed canonicalization.

Its identities should stay typed by the layer that produced them.

Its discretionary loci should be censused rather than assumed complete.

Its structural facts should come from independent state.

Its alternatives should be materially supported.

Its ambiguities should escalate scrutiny rather than evade it.

Its contests should be independent to the extent evidence can establish.

Its judgments should be reviewable.

Its context should be lawfully compiled.

Its realization should be witnessed.

Its tools should remain synchronized with their runtime implementations.

Its effects should remain independently authorized.

In a word, it should be properly promthed.

## Appendix A: Court Disposition Schema

```text
ContextCourtDisposition
  disposition_id
  invocation_id

  court_id
  court_revision
  court_jurisdiction

  Grundnorm_Basis_id
  Root_Constitution_revision
  context_constitution_revision
  constitutional_derivation_judgment

  scrutiny_profiles_considered[]
  scrutiny_profile_judgments[]

  constitutional_canonical_form_revision
  domain_canonicalization_profiles[]
  correspondence_records[]
  discretion_census_revision

  subjects[]
  findings_considered[]
  semantic_alternatives_considered[]
  alternative_materiality_judgments[]
  structural_states_considered[]
  consequence_assessments[]
  contests_considered[]
  independence_assessments[]
  evidence_commitments[]

  disposition_type
  rationale_codes[]

  authority
  jurisdiction
  scope
  effective_period

  review_required
  review_mode
  appeal_route
  stay_status

  supersedes

  disposition_hash
  signatures[]
```

## Appendix B: Error Ontology

```text
CONSTITUTIONAL_BASIS
  GRUNDNORM_BASIS_UNDECLARED
  GRUNDNORM_BASIS_SCOPE_VIOLATION
  GRUNDNORM_BASIS_POST_GENESIS_EXTENSION
  CONSTITUTIONAL_DERIVATION_UNESTABLISHED
  ROOT_CONSTITUTION_UNRECOGNIZED
  CONSTITUTIONAL_CANONICAL_FORM_UNRECOGNIZED
  CCAF_EXCLUSION_ATTEMPTED
  CCAF_SUCCESSION_UNGOVERNED

DISCRETION_AUDIT
  DISCRETION_LOCUS_UNCENSUSED
  DISCRETION_AUDIT_INCOMPLETE
  DISCRETION_CENSUS_STALE
  DISCRETION_CENSUS_ABSENT
  DISCRETION_REDUCTION_UNPROVEN

PROFILE_GOVERNANCE
  SCRUTINY_PROFILE_UNIDENTIFIED
  SCRUTINY_PROFILE_UNADJUDICATED
  SCRUTINY_PROFILE_EVIDENCE_UNSTATED
  SCRUTINY_PROFILE_AUTHORITY_INVALID
  SCRUTINY_PROFILE_EXPIRED
  SCRUTINY_PROFILE_DEPENDENCY_CHANGED
  PROFILE_ROLE_SEPARATION_UNSATISFIED
  PROFILE_SELF_ADMITTED

DISCOVERY
  MANDATORY_SOURCE_DISCOVERY_INCOMPLETE
  PROMTHUS_SOURCE_UNAVAILABLE
  DISCOVERY_PROFILE_UNSATISFIED
  DISCOVERY_PROFILE_UNADJUDICATED
  MANDATORY_REGISTRY_OMITTED
  DISCOVERY_COVERAGE_CLAIM_INVALID
  DISCOVERY_CLAIM_EVIDENCE_UNSTATED

CALIBRATION
  CALIBRATION_PROFILE_UNADJUDICATED
  CALIBRATION_DATASET_UNIDENTIFIED
  CALIBRATION_DATASET_UNREPRESENTATIVE
  CALIBRATION_METRIC_UNSUPPORTED
  CALIBRATION_DECISION_BAND_UNSUPPORTED
  CLASSIFIER_OUT_OF_CALIBRATION
  CALIBRATION_PROFILE_INVALID
  CALIBRATION_DRIFT_DETECTED

CANONICALIZATION
  DOMAIN_CANONICALIZATION_PROFILE_UNIDENTIFIED
  DOMAIN_CANONICALIZATION_PROFILE_UNADJUDICATED
  CANONICALIZATION_EXCLUSION_UNJUSTIFIED
  CANONICALIZATION_EXCLUSION_SEMANTIC
  IDENTITY_FIELD_COVERAGE_INCOMPLETE
  CANONICALIZATION_NONDETERMINISTIC
  CANONICALIZATION_PROFILE_CHANGE_MISREPRESENTED
  CONSTITUTIONAL_OBJECT_IDENTIFIED_UNDER_DOMAIN_PROFILE

IDENTITY_LAYER
  IDENTITY_LAYER_BINDING_ABSENT
  CROSS_PROFILE_IDENTITY_COLLAPSED
  CORRESPONDENCE_CLASS_UNSTATED
  CORRESPONDENCE_RECORD_ABSENT
  CORRESPONDENCE_EVIDENCE_UNSTATED
  CROSS_LAYER_CACHE_SUBSTITUTION
  CROSS_LAYER_REVOCATION_ASSUMED

CONFLICT_DETECTION
  CONFLICT_PROFILE_UNADJUDICATED
  CONFLICT_COVERAGE_CLAIM_UNSUPPORTED
  CONFLICT_PROFILE_SCOPE_EXCEEDED
  CONFLICT_BLIND_SPOT_EVIDENCE_UNSTATED

ADAPTER_CONTRACT
  ADAPTER_CONTRACT_UNADJUDICATED
  ADAPTER_LOSS_CLAIM_UNSUPPORTED
  ADAPTER_PROFILE_INCOMPATIBLE
  ADAPTER_ASSURANCE_BOUNDARY_INVALID

CLASSIFICATION
  CONTEXT_SOURCE_UNAUTHENTICATED
  CONTEXT_REVISION_UNKNOWN
  CONTEXT_SOURCE_MISCLASSIFIED
  CLASSIFICATION_UNCERTAIN
  CLASSIFICATION_CONTESTED
  CLASSIFICATION_REVIEW_REQUIRED
  MATERIAL_ALTERNATIVE_OMITTED
  IMMATERIAL_ALTERNATIVE_INCLUDED
  ALTERNATIVE_SUPPORT_UNIDENTIFIED
  ALTERNATIVE_ORIGIN_UNATTRIBUTED

STRUCTURAL_CONSEQUENCE
  STRUCTURAL_STATE_UNAVAILABLE
  STRUCTURAL_STATE_SELF_REPORTED
  STRUCTURAL_STATE_INCONSISTENT
  CONSEQUENCE_TIER_UNCOMPUTABLE
  CONSEQUENCE_TIER_MISAPPLIED
  CONSERVATIVE_TIERING_BYPASSED

CONTEST
  REQUIRED_CONTEST_ABSENT
  CONTEST_PROFILE_UNADJUDICATED
  CONTEST_INDEPENDENCE_UNSATISFIED
  CONTEST_EVIDENCE_DEPENDENT
  CONTEST_LINEAGE_CORRELATED
  CONTEST_INDEPENDENCE_UNVERIFIABLE
  CONTEST_REVIEW_REQUIRED

CONTAINMENT
  CONTEXT_SCOPE_MISMATCH
  CONTEXT_PURPOSE_UNBOUND
  CONTEXT_ADMISSION_EXCESS
  CONTEXT_DISCLOSURE_UNAUTHORIZED
  DELEGATION_CONTEXT_EXCESS
  GOVERNING_PROJECTION_LEAKS_METADATA

ADMISSION
  CONTEXT_AUTHORITY_INVALID
  CONTEXT_REVOKED
  STALE_CONTEXT_ADMITTED
  CONTEXT_STANDING_ESCALATED
  COURT_JUDGMENT_ABSENT
  COURT_JUDGMENT_INVALID

RESOLUTION
  CONTEXT_CONFLICT_UNRESOLVED
  CONTEXT_PRECEDENCE_CYCLE
  CONTEXT_PRECEDENCE_INVERTED
  COURT_CONFLICT_UNRESOLVED
  COURT_JURISDICTION_CYCLE
  ARBITRATION_AUTHORITY_ABSENT

REVIEW_AND_APPEAL
  APPEAL_STANDING_ABSENT
  APPEAL_GROUNDS_INVALID
  APPEAL_PERIOD_EXPIRED
  APPEAL_REVIEW_UNAVAILABLE
  APPEAL_STAY_VIOLATED
  AUTOMATIC_STAY_REQUIRED
  AUTOMATIC_STAY_BYPASSED
  MACHINE_REVIEW_INDEPENDENCE_UNSATISFIED
  REVIEW_TIMEOUT_REFUSAL

AVAILABILITY
  STAY_FLOODING_DETECTED
  STAY_ORIGIN_UNATTRIBUTED
  STAY_ALTERNATIVE_ORIGIN_UNATTRIBUTED
  STAY_DEDUPLICATION_FAILED
  REVIEW_CAPACITY_EXHAUSTED
  ESSENTIAL_SERVICE_BLOCKED
  STAY_SOURCE_QUARANTINED

TRANSFORMATION
  TRANSFORMATION_NOT_AUTHORIZED
  CONTEXT_REDUCTION_UNSAFE
  CONTEXT_LINEAGE_BROKEN
  PRESENTATION_IMPERSONATES_SOURCE
  GOVERNING_PROJECTION_NOT_ADMITTED
  GOVERNING_PROJECTION_OBLIGATION_UNPRESERVED

BUDGET_AND_ROUTE
  CONTEXT_BUDGET_UNCLOSED
  REQUIRED_CONTEXT_OMITTED
  OUTPUT_RESERVE_VIOLATED
  PROVIDER_ROUTE_INCOMPATIBLE
  NO_COMPATIBLE_MODEL_ROUTE

REALIZATION
  PRESENTED_HASH_MISMATCH
  TOOL_SCHEMA_DIVERGENCE
  DELIMITER_INTEGRITY_FAILURE
  SILENT_TRUNCATION_DETECTED
  PROVIDER_PAYLOAD_UNWITNESSED
  CONTEXT_INVALIDATED_BEFORE_DISPATCH

DELEGATION
  DELEGATION_CONSTRAINT_WEAKENED
  DELEGATION_SCOPE_EXCEEDED
  DELEGATION_AUTHORITY_ESCALATED
  DELEGATION_LINEAGE_BROKEN
  DELEGATION_RETURN_EVIDENCE_INCOMPLETE
  DELEGATION_REVIEW_MODE_INVALID

EFFECT
  EFFECT_AUTHORITY_ABSENT
  EFFECT_SCOPE_MISMATCH
  EFFECT_POLICY_CONFLICT
  EFFECT_APPROVAL_REQUIRED
  MODEL_OUTPUT_SELF_AUTHORIZED
  TOOL_EFFECT_CLASS_MISMATCH

AMENDMENT
  AMENDMENT_AUTHORITY_ABSENT
  AMENDMENT_SELF_RATIFICATION
  AMENDMENT_TESTS_INCOMPLETE
  AMENDMENT_MIGRATION_UNCLOSED
  AMENDMENT_INVALIDATES_INFLIGHT_INVOCATION

SEALING
  INVOCATION_UNSEALED
  RECEIPT_INCOMPLETE
  RECEIPT_REPRODUCTION_FAILED
  TRANSPARENCY_ANCHOR_ABSENT

CONFORMANCE
  CONFORMANCE_CLAIM_UNSUPPORTED
  CONFORMANCE_PROFILE_UNADJUDICATED
  CONFORMANCE_METRICS_INCOMPLETE
  CONFORMANCE_COST_UNREPORTED
  CONFORMANCE_BOUNDARY_UNDECLARED
```

## Appendix C: Core Invariants

1. Every provider invocation is governed by an identified Root Constitution revision.

2. The genesis standing of the Root Constitution is explicitly bound to a declared Grundnorm Basis.

3. The Grundnorm Basis is limited to the fixed genesis elements enumerated in Section 5.1.

4. No post-genesis component acquires Grundnorm status by declaration.

5. A later Basis-related change proceeds through governed amendment and does not rewrite genesis.

6. Context law derives standing from the Constitutional Kernel through an explicit derivation judgment.

7. Every mechanism that determines whether another mechanism is scrutinized is governed by authority external to the discretion it constrains.

8. Every scrutiny-bounding profile is identity-bearing, evidence-class-typed, and adjudicated before use.

9. Root-law replay is distinguished from whole-compilation replay.

10. Classifier outputs are findings, not self-ratifying law.

11. Confidence-bearing findings require an admitted calibration profile.

12. Calibration profiles do not establish their own adequacy.

13. The Constitutional Canonical Form is exclusion-free and bound into the genesis identity and initial recognition rule.

14. Constitutional objects are identified under the Constitutional Canonical Form, never under an adjudicated domain profile.

15. The Constitutional Canonical Form is recognized at genesis rather than adjudicated, and is succeeded only through governed amendment.

16. Domain canonicalization profiles are adjudicated before identities computed under them acquire evidentiary standing.

17. Every excluded non-semantic field carries an admitted justification with a declared evidence class.

18. A canonicalization-profile change is not a content change, and a content change is not a profile change.

19. Every identity is typed by the canonicalization layer under which it was computed.

20. Identities under different canonicalization layers are never collapsed; a court may admit only a typed correspondence.

21. Correspondence never licenses substitution in a cache key, revocation, delegation constraint, or historical receipt.

22. Profile admission requires constitutional role separation between the profile author and its adjudicator.

23. Every authority-bearing discretionary locus appears in the discretion census.

24. Every censused locus binds to an audit row or a proven reduction to an existing row.

25. A closure claim requires a current census computed against the effective declared schema and transition registry.

26. Structurally derivable consequence inputs come from authoritative environment state rather than finder proposal.

27. Every semantic alternative used in tiering has identified evidentiary support.

28. Omitting a materially supported alternative and including an unsupported high-risk alternative are both governed failures.

29. Unresolved materially supported semantic alternatives are tiered conservatively.

30. High-consequence findings receive contest under declared law.

31. Required independent contests satisfy an admitted independence profile.

32. A second finding does not count as independent merely because it was produced separately.

33. Independence claims declare whether they are verified, attested, nominal, or unknown.

34. Claims about undisclosed model ancestry are no stronger than their attestations.

35. Conflict-detection profiles are adjudicated before supporting closure claims.

36. Conflict closure never exceeds the admitted scope of the conflict-detection profile.

37. Adapter contracts are adjudicated before defining realization consistency.

38. An adapter does not certify its own fidelity standard.

39. Every binding compilation decision is supported by a valid court judgment.

40. Every court acts within declared jurisdiction.

41. Unresolved inter-court conflict produces authorized arbitration or refusal.

42. Review modes are explicit and compatible with autonomous execution.

43. Required machine review satisfies the applicable independence profile.

44. Required automatic stays block dependent execution.

45. Appeal routes are explicit where appeal is permitted.

46. Stay origins are attributable and reviewable.

47. Stay attribution traverses generated alternatives to their originating evidence.

48. Repeated stay triggers are governed as an availability risk rather than silently ignored.

49. Every candidate context element has an identifiable PROMTHUS source class.

50. PROMTHUS classification does not establish authority.

51. PROMTHUS sequence does not establish precedence or serialization order.

52. Mandatory source registries derive from constitutional law, not from compiler discretion.

53. Every discovery profile is identity-bearing and adjudicated before use.

54. A discovery profile may narrow search but may not redefine mandatory sources out of existence.

55. Discovery claims declare their evidentiary class.

56. Aggregate discovery non-selection is governed by an admitted profile; adjudicated candidates receive item-level dispositions.

57. Every admitted element has a purpose, valid scope, sufficient authority, and necessity judgment.

58. Accessibility alone never establishes admission.

59. Every admitted element has entity and revision identity.

60. Every derived presentation has distinct identity unless exact identity is proven.

61. Stable entity identity does not substitute for revision identity.

62. Governance status and epistemic status remain separate.

63. Relevance does not create authority.

64. Retrieved evidence does not become policy without authorized adjudication.

65. Required context may not be silently omitted.

66. Unnecessary context may not be admitted merely because capacity permits it.

67. Stale or revoked context may not remain governing.

68. Transformations require explicit authorization.

69. Derived representations preserve source lineage.

70. Compression does not inherit the identity of its source.

71. A governing projection receives mandatory standing only through an explicit judgment.

72. A governing projection preserves specified obligations without impersonating its source.

73. Projection metadata is subject to containment review.

74. Mandatory incomparable conflicts produce arbitration or invocation refusal.

75. Optional incomparable conflicts may be lawfully excluded with receipt disclosure.

76. Precedence is governed by declared relations, not raw message position.

77. Budget closure is verified after provider realization at realization-synchronized conformance levels.

78. Tool descriptions and schemas presented to the model correspond to runtime capabilities from CCC-2 onward.

79. Provider realization corresponds to admitted Context IR under an admitted adapter contract.

80. Typed standing is enforced outside the model unless a provider supplies a native enforceable mechanism.

81. Model output does not imply execution authority.

82. Execution authority does not imply effect authorization.

83. Every executed effect possesses independent valid authorization.

84. Constitutional refusal is distinct from ordinary task failure.

85. Governance correctness does not imply behavioral correctness.

86. A lawful judgment may later prove behaviorally suboptimal without becoming retroactively invalid.

87. Amendments require authority under currently effective law.

88. A governed component may propose but may not silently self-ratify an enlargement of authority.

89. Every provider call in an agent loop is independently identified, compiled, and receipted.

90. Every delegation is governed by an identity-bearing contract.

91. A child context may become stricter but may not silently weaken mandatory parent constraints.

92. Returned delegate material is independently adjudicated before gaining standing in the parent context.

93. Cached judgments are reused only while identity, law, calibration, canonicalization, conflict detection, adapter, contest, discovery, scope, purpose, and freshness predicates remain valid.

94. Receipt reproducibility does not imply compilation replayability.

95. Public receipts use privacy-preserving commitments unless disclosure is authorized.

96. Every evidentiary invocation produces a reproducible receipt.

97. Unsealed invocations are marked non-evidentiary.

98. Portability claims are bounded by admitted adapter contracts.

99. Every conformance claim declares a level, profile, metrics, machine cost, human-review cost, contest cost, availability cost, and controlled assurance boundary.

## Appendix D: Discretion Audit

- **Discretionary locus:** Genesis recognition  
  **Discretion exercised:** Establishes initial standing  
  **External governor:** Fixed Grundnorm Basis  
  **Required evidence:** Genesis identity, custody, recognition rule, bootstrap witness  
  **Failure when ungoverned:** `GRUNDNORM_BASIS_UNDECLARED`

- **Discretionary locus:** Basis scope  
  **Discretion exercised:** Determines what is exempt from positive derivation  
  **External governor:** Fixed genesis enumeration and current amendment law  
  **Required evidence:** Genesis manifest and Basis-scope proof  
  **Failure when ungoverned:** `GRUNDNORM_BASIS_SCOPE_VIOLATION`

- **Discretionary locus:** Constitutional Canonical Form  
  **Discretion exercised:** Determines how constitutional objects are identified at all  
  **External governor:** Genesis recognition rule and DSC grammar; recognized, not adjudicated  
  **Required evidence:** Genesis manifest, grammar definition, proof that no semantic exclusion exists  
  **Failure when ungoverned:** `CONSTITUTIONAL_CANONICAL_FORM_UNRECOGNIZED`

- **Discretionary locus:** Root-law amendment  
  **Discretion exercised:** Changes constitutional law  
  **External governor:** Effective prior Root Constitution and Amendment Court  
  **Required evidence:** Proposal, tests, ratification judgment, transition receipt  
  **Failure when ungoverned:** `AMENDMENT_SELF_RATIFICATION`

- **Discretionary locus:** Context-constitution derivation  
  **Discretion exercised:** Establishes domain-law standing  
  **External governor:** Constitutional Derivation Court  
  **Required evidence:** Parent revision, delegated domain, derivation judgment  
  **Failure when ungoverned:** `CONSTITUTIONAL_DERIVATION_UNESTABLISHED`

- **Discretionary locus:** Discretion census  
  **Discretion exercised:** Determines which mechanisms are treated as holding constitutional power  
  **External governor:** Deterministic rule over the declared schema and transition registry  
  **Required evidence:** Census revision, schema and registry revisions, audit-row bindings, reduction proofs  
  **Failure when ungoverned:** `DISCRETION_LOCUS_UNCENSUSED`

- **Discretionary locus:** Profile adjudicator role  
  **Discretion exercised:** Determines who may admit a scrutiny-bounding profile  
  **External governor:** Constitutional role separation under superior law  
  **Required evidence:** Distinct proposer and ratifier identities, superior adequacy criteria, witnessable judgment  
  **Failure when ungoverned:** `PROFILE_ROLE_SEPARATION_UNSATISFIED`

- **Discretionary locus:** Domain canonicalization-profile authorship  
  **Discretion exercised:** Determines which domain content differences register as identity changes  
  **External governor:** Domain Canonicalization Adequacy Court  
  **Required evidence:** Identity fields, per-exclusion justification, evidence classes, determinism assessment, adequacy judgment  
  **Failure when ungoverned:**   
    `DOMAIN_CANONICALIZATION_PROFILE_UNADJUDICATED`

- **Discretionary locus:** Cross-layer identity relation  
  **Discretion exercised:** Asserts that two identities under different layers are related  
  **External governor:** Domain Canonicalization Adequacy Court via typed correspondence  
  **Required evidence:** Correspondence record, class, evidence and evidence class, admitting judgment  
  **Failure when ungoverned:** `CROSS_PROFILE_IDENTITY_COLLAPSED`

- **Discretionary locus:** Discovery obligation  
  **Discretion exercised:** Defines mandatory source domains  
  **External governor:** Root Constitution and context constitution  
  **Required evidence:** Mandatory registry declarations  
  **Failure when ungoverned:** `MANDATORY_REGISTRY_OMITTED`

- **Discretionary locus:** Discovery-profile proposal  
  **Discretion exercised:** Defines actual search space  
  **External governor:** Discovery Adequacy Court  
  **Required evidence:** Profile, claims, evidence classes, adequacy judgment  
  **Failure when ungoverned:** `DISCOVERY_PROFILE_UNADJUDICATED`

- **Discretionary locus:** Retrieval ranking  
  **Discretion exercised:** Selects candidate priority and cutoff  
  **External governor:** Admitted discovery profile  
  **Required evidence:** Queries, index revision, ranking policy, cutoff  
  **Failure when ungoverned:** `DISCOVERY_PROFILE_UNSATISFIED`

- **Discretionary locus:** Calibration-profile authorship  
  **Discretion exercised:** Defines confidence evidence and decision bands  
  **External governor:** Calibration Adequacy Court  
  **Required evidence:** Dataset identity, metrics, evidence classes, adequacy judgment  
  **Failure when ungoverned:** `CALIBRATION_PROFILE_UNADJUDICATED`

- **Discretionary locus:** Semantic finding  
  **Discretion exercised:** Proposes classification and meaning  
  **External governor:** Classification Court  
  **Required evidence:** Finding, method identity, evidence, admitted calibration  
  **Failure when ungoverned:** `COURT_JUDGMENT_ABSENT`

- **Discretionary locus:** Structural tier inputs  
  **Discretion exercised:** Determines consequence facts  
  **External governor:** Authoritative environment registries  
  **Required evidence:** Structural-state derivation  
  **Failure when ungoverned:** `STRUCTURAL_STATE_SELF_REPORTED`

- **Discretionary locus:** Semantic alternative inclusion  
  **Discretion exercised:** Determines conservative consequence range  
  **External governor:** Alternative-materiality rule and court review  
  **Required evidence:** Supporting evidence, originating source, inclusion judgment  
  **Failure when ungoverned:** `IMMATERIAL_ALTERNATIVE_INCLUDED`

- **Discretionary locus:** Semantic alternative omission  
  **Discretion exercised:** Narrows conservative consequence range  
  **External governor:** Contest and court review  
  **Required evidence:** Candidate alternatives and evidence search  
  **Failure when ungoverned:** `MATERIAL_ALTERNATIVE_OMITTED`

- **Discretionary locus:** Consequence tier  
  **Discretion exercised:** Determines scrutiny requirement  
  **External governor:** Deterministic context law  
  **Required evidence:** Structural state, material alternatives, tier derivation  
  **Failure when ungoverned:** `CONSEQUENCE_TIER_UNCOMPUTABLE`

- **Discretionary locus:** Contest trigger  
  **Discretion exercised:** Determines whether challenge is mandatory  
  **External governor:** Structural consequence rule  
  **Required evidence:** Tier result and threshold  
  **Failure when ungoverned:** `REQUIRED_CONTEST_ABSENT`

- **Discretionary locus:** Independence-profile authorship  
  **Discretion exercised:** Defines sufficient challenger independence  
  **External governor:** Context constitution and Contest and Independence Court  
  **Required evidence:** Profile revision, minimum class, evidence classes, judgment  
  **Failure when ungoverned:** `CONTEST_PROFILE_UNADJUDICATED`

- **Discretionary locus:** Challenger independence  
  **Discretion exercised:** Determines whether contest qualifies  
  **External governor:** Admitted independence profile and Contest Court  
  **Required evidence:** Independence basis and evidence class  
  **Failure when ungoverned:** `CONTEST_INDEPENDENCE_UNSATISFIED`

- **Discretionary locus:** Conflict-detection-profile authorship  
  **Discretion exercised:** Defines detectable conflict scope  
  **External governor:** Conflict-Detection Adequacy Court  
  **Required evidence:** Checks, benchmarks, coverage class, judgment  
  **Failure when ungoverned:** `CONFLICT_PROFILE_UNADJUDICATED`

- **Discretionary locus:** Court disposition  
  **Discretion exercised:** Creates binding invocation judgment  
  **External governor:** Root law, jurisdiction graph, appeal  
  **Required evidence:** Signed judgment, rationale, scope  
  **Failure when ungoverned:** `COURT_JUDGMENT_INVALID`

- **Discretionary locus:** Inter-court resolution  
  **Discretion exercised:** Resolves conflicting judgments  
  **External governor:** Coordination or Constitutional Court  
  **Required evidence:** Conflict record and arbitration judgment  
  **Failure when ungoverned:** `COURT_CONFLICT_UNRESOLVED`

- **Discretionary locus:** Review mode  
  **Discretion exercised:** Determines stay, machine review, or appeal  
  **External governor:** Context constitution  
  **Required evidence:** Structural tier, review rule, custody record  
  **Failure when ungoverned:** `AUTOMATIC_STAY_BYPASSED`

- **Discretionary locus:** Machine reviewer  
  **Discretion exercised:** Discharges independent review  
  **External governor:** Applicable admitted independence profile  
  **Required evidence:** Reviewer identity and independence evidence  
  **Failure when ungoverned:** `MACHINE_REVIEW_INDEPENDENCE_UNSATISFIED`

- **Discretionary locus:** Stay origin  
  **Discretion exercised:** Blocks dependent execution  
  **External governor:** Review law and availability controls  
  **Required evidence:** Source, finding, alternative, route, deduplication, custody  
  **Failure when ungoverned:** `STAY_ORIGIN_UNATTRIBUTED`

- **Discretionary locus:** Transformation  
  **Discretion exercised:** Alters admitted representation  
  **External governor:** Transformation Court  
  **Required evidence:** Source identity, preservation contract, presentation identity  
  **Failure when ungoverned:** `TRANSFORMATION_NOT_AUTHORIZED`

- **Discretionary locus:** Governing projection  
  **Discretion exercised:** Creates derived mandatory artifact  
  **External governor:** Transformation and Standing Courts  
  **Required evidence:** Preservation judgment, disclosure assessment, expiry  
  **Failure when ungoverned:** `GOVERNING_PROJECTION_NOT_ADMITTED`

- **Discretionary locus:** Budget reduction  
  **Discretion exercised:** Chooses what is compressed or omitted  
  **External governor:** Budget and Transformation Courts  
  **Required evidence:** Budget estimate, reduction judgment, closure trace  
  **Failure when ungoverned:** `CONTEXT_BUDGET_UNCLOSED`

- **Discretionary locus:** Delegation  
  **Discretion exercised:** Transfers task, context, tools, and authority  
  **External governor:** Delegation Court  
  **Required evidence:** Delegation contract and inheritance judgment  
  **Failure when ungoverned:** `DELEGATION_AUTHORITY_ESCALATED`

- **Discretionary locus:** Adapter-contract authorship  
  **Discretion exercised:** Defines realization relation and tolerated losses  
  **External governor:** Adapter-Contract Adequacy Court  
  **Required evidence:** Contract, loss evidence classes, admitted profiles, judgment  
  **Failure when ungoverned:** `ADAPTER_CONTRACT_UNADJUDICATED`

- **Discretionary locus:** Provider adapter  
  **Discretion exercised:** Serializes IR into provider request  
  **External governor:** Realization Correspondence Court  
  **Required evidence:** Admitted adapter revision, request commitment, render checks  
  **Failure when ungoverned:** `PRESENTED_HASH_MISMATCH`

- **Discretionary locus:** Tool exposure  
  **Discretion exercised:** Defines model-visible capability  
  **External governor:** Tool registry, Standing Court, and schema-correspondence check  
  **Required evidence:** Tool manifest, schema identity, runtime binding  
  **Failure when ungoverned:** `TOOL_SCHEMA_DIVERGENCE`

- **Discretionary locus:** Model-proposed effect  
  **Discretion exercised:** Requests external consequence  
  **External governor:** Independent Effect Authorization Court  
  **Required evidence:** Effect request and authorization judgment  
  **Failure when ungoverned:** `MODEL_OUTPUT_SELF_AUTHORIZED`

- **Discretionary locus:** Receipt production  
  **Discretion exercised:** Represents what occurred  
  **External governor:** Independent witness and verifier  
  **Required evidence:** Commitments, signatures, recomputation  
  **Failure when ungoverned:** `INVOCATION_UNSEALED`

- **Discretionary locus:** Conformance-profile authorship  
  **Discretion exercised:** Defines assurance claim and required metrics  
  **External governor:** Conformance Court and external verifier  
  **Required evidence:** Profile identity, obligations, metrics, evidence classes, independent review of the obligation set  
  **Failure when ungoverned:** `CONFORMANCE_PROFILE_UNADJUDICATED`

- **Discretionary locus:** Conformance claim  
  **Discretion exercised:** Declares achieved assurance level  
  **External governor:** Conformance Court and external verifier  
  **Required evidence:** Level, admitted profile, metrics, cost, boundary  
  **Failure when ungoverned:** `CONFORMANCE_CLAIM_UNSUPPORTED`

The audit is not a proof that implementations satisfy these governors. It is a proof-obligation map. A conforming implementation must demonstrate that every listed locus is connected to its external governor and that the named failure is emitted when the connection is absent.

Completeness of the table is not asserted by inspection. The discretion census of Section 2.4 supplies the enumeration procedure: it walks the declared schema and transition registry, identifies every mechanism able to affect identity, authority, admission, scope, scrutiny, conflict detection, transformation, realization, effect permission, or evidentiary claims, and requires each to bind to a row above or to a proven reduction to one. A mechanism that holds constitutional power while remaining absent from the census emits   
`DISCRETION_LOCUS_UNCENSUSED`, and a census that cannot map every locus it found emits

`DISCRETION_AUDIT_INCOMPLETE`.

The census is itself governed without requiring a further audit row of its own kind. It is a deterministic rule over state it does not author, which satisfies clause 3 of Section 2.2; its own row above records the discretion it does hold, which is the choice of criteria by which a mechanism is judged authority-bearing.

Both conformance rows name an external verifier. A system that authored its own assurance obligations and then certified itself against them would relocate the same discretion one level above the metrics, which is the failure the rest of the table exists to prevent.

The audit therefore supplies an executable stopping condition for **declared architectural closure**, not proof that the declared schema exhausts the realized capability surface. When the census is current, every censused locus is present in the table or proven reducible to an existing row, and every row binds to an external governor and an executable failure, the declared constitutional spine is closed. Implementation-surface discovery, bypass tests, and independent observation must still test whether uncensused power exists outside that declaration. Newly discovered power may require a foundation repair rather than an extension.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm2.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Possibility Space.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that large language models do not encounter users, projects, institutions, or environments directly. Its nearest external comparison fields are ai, governance, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[A2]** Adam Ableman. *Governed Context & Memory (GCM)*. Ableman Corpus current edition; work identity `PAPER.PUB.18633797`;  
source SHA-256  
`3F17ACD8AB9C6DC66C23D22098628C70042854B198C3ABFCBFA3EC7DC27B9C08`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Retrieval-Augmented Reasoning under Constitutional Constraints*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-384489D4604BEC4D`;  
source SHA-256  
`133DA35C0F27F35BAA1F53DFEE415068AD2D24FF713F8CDAFA2FDC8F748AC15C`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Split-Authority AI Coordination*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-35D1BAECD5CB17AD`;  
source SHA-256  
`06FB6133170879FA8308684F0DA33F5813EAF3B5488291C2D7D234BEB6FDFEC2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

References are given in author-date form. Entries for living specifications and project documentation carry a version or revision where one is published and an access date, since their content changes without renumbering.

Bai, Yuntao, et al. 2022. "Constitutional AI: Harmlessness from AI Feedback." arXiv:2212.08073 [cs.CL].

Bell, David E., and Leonard J. LaPadula. 1973. *Secure Computer Systems: Mathematical Foundations*. Technical Report MTR-2547, Volume I. Bedford, MA: MITRE Corporation.

Cedar Policy Project. n.d. *Cedar Policy Language Reference Guide*. Open-source project documentation, originated at Amazon Web Services. https://www.cedarpolicy.com. Accessed 29 July 2026.

Debenedetti, Edoardo, et al. 2025. "Defeating Prompt Injections by Design." arXiv:2503.18813 [cs.CR]. https://doi.org/10.48550/arXiv.2503.18813.

Denning, Dorothy E. 1976. "A Lattice Model of Secure Information Flow." *Communications of the ACM* 19 (5): 236-243.

Greshake, Kai, et al. 2023. "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection." In *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec '23)*, 79-90. Also arXiv:2302.12173 [cs.CR].

Khattab, Omar, et al. 2024. "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines." In *Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)*. Also arXiv:2310.03714 [cs.CL].

Laurie, Ben, Eran Messeri, and Rob Stradling. 2021. *Certificate Transparency Version 2.0*. RFC 9162. Internet Engineering Task Force. https://www.rfc-editor.org/info/rfc9162.

Model Context Protocol. 2026. *Model Context Protocol Specification*, revision 2026-07-28. Open specification, originated at Anthropic. [modelcontextprotocol.io source](https://modelcontextprotocol.io/specification/2026-07-28). Accessed 29 July 2026.

Myers, Andrew C., and Barbara Liskov. 2000. "Protecting Privacy Using the Decentralized Label Model." *ACM Transactions on Software Engineering and Methodology* 9 (4): 410-442.

OASIS. 2013. *eXtensible Access Control Markup Language (XACML) Version 3.0*. OASIS Standard, 22 January 2013. Organization for the Advancement of Structured Information Standards.

Open Policy Agent Project. n.d. *Policy Language (Rego)*. OPA documentation. Cloud Native Computing Foundation. https://www.openpolicyagent.org. Accessed 29 July 2026.

OpenSSF. 2025. *Supply-chain Levels for Software Artifacts (SLSA), Version 1.2*. Open Source Security Foundation. https://slsa.dev/spec/v1.2/. Accessed 29 July 2026.

Pang, Ruoming, et al. 2019. "Zanzibar: Google's Consistent, Global Authorization System." In *Proceedings of the 2019 USENIX Annual Technical Conference (USENIX ATC '19)*, 33-46.

Torres-Arias, Santiago, et al. 2019. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." In *Proceedings of the 28th USENIX Security Symposium*, 1393-1410.

Wallace, Eric, et al. 2024. "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions." arXiv:2404.13208 [cs.CR].

World Wide Web Consortium. 2013. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. Edited by Timothy Lebo, Satya Sahoo, and Deborah McGuinness. https://www.w3.org/TR/prov-o/.

### Ableman Corpus Works

Adam Ableman. 2026. *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI*. Zenodo. https://doi.org/10.5281/zenodo.18633797.

Adam Ableman. 2026. *Semantic Custody*. Zenodo. https://doi.org/10.5281/zenodo.20300952.

Adam Ableman. 2026. *The Three Hash Rule*. Zenodo. https://doi.org/10.5281/zenodo.20788617.

Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition in the historical CCF -> CMB -> GMB lineage; conceptual claims retain the standing stated in the work.

Adam Ableman. *Meaning as Binding*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *Semantic Legitimacy Before Context*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *A Formal Theory of Work Custody*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

Adam Ableman. *From Content-Addressed Storage to Governed Semantic Project Lineage*. Ableman Corpus current edition; conceptual claims retain the standing stated in the work.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

Adam Ableman *Governed Context & Memory (GCM): Context Configuration as Constitutional Surface, Semantic Hashing as Enforcement, and Explicit Ignorance as First-Class Success in Generational AI.* Zenodo, 2026. doi:10.5281/zenodo.18633797

Adam Ableman *Semantic Custody.* Zenodo, 2026. doi:10.5281/zenodo.20300952

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847352](https://doi.org/10.5281/zenodo.23847352)
