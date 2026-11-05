# Semantic Debt

## A Two-Axis Ontology of Meaning Failure in Software, Governance, and Agent-Built Systems

### The system may still speak, but can its meanings still be recovered?

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Software systems do not only accumulate technical debt. They accumulate semantic debt: the future cost of meaning that is underdefined, misplaced, contradictory, stale, fragmented, opaque, overcoupled, overclaimed, inadmissible, or only recoverable through inference. Technical debt concerns the burden created by implementation shortcuts, architectural compromises, postponed refactoring, or quality degradation. Semantic debt concerns a different layer: the decay of recoverable meaning. A system may compile, pass tests, and remain operational while its terms drift, its categories collapse, its authority assumptions hide, its decisions vaporize, its evidence becomes inadmissible, and its claims outrun what its artifacts can support.

This paper proposes a two-axis ontology of semantic debt. The first axis defines seven semantic subdomains: lexical debt, ontological debt, boundary debt, procedural debt, evidentiary debt, authority debt, and claim debt. The second axis defines nine debt modes: underdefinition, contradiction, fragmentation, staleness, opacity, overcoupling, inadmissibility, overclaim, and lossy translation. Together, these axes give semantic debt a coordinate system. A debt item is not merely named. It is located by what kind of meaning is failing and by how that failure manifests.

The paper gives special attention to semantic fragmentation. Fragmentation is not a peer subdomain beside lexical, ontological, boundary, procedural, evidentiary, authority, and claim debt. It is a cross-cutting distribution failure that can affect any of them. The precise motivating subtype is semantic locality debt: the cost incurred when meaning exists somewhere in a system but not in a stable, canonical, locally recoverable home.

The ontology is intended to be operational. The semantic debt matrix leads directly to governing artifacts: glossaries, non-claims files, claim ledgers, standing graphs, migration contracts, receipt schemas, and semantic debt ledgers. These artifacts turn semantic debt from an interpretive complaint into a governable engineering object. The framework is especially relevant to agent-built systems, where plausible automation can introduce acronym drift, status collapse, authority inference, claim inflation, and boundary leakage while preserving apparent functionality. This candidate also locates the ontology in the Governed Meaning Base and universal GSM, where debt can be attached to exact semantic objects, relations, projections, evidence dependencies, and revision obligations without confusing storage with standing.

## 1. Introduction: The Hidden Debt of Meaning

A software system can continue functioning while its meaning decays.

The tests still pass. The package still builds. The API still responds. The dashboard is still green. Yet the system may no longer be able to answer basic semantic questions:

* What does this status mean?
* Is this artifact validated, admitted, executed, or standing-bearing?
* What authority permitted this effect?
* What claim does this receipt support?
* What is explicitly not claimed?
* Which policy version governed this transition?
* Was this refusal an error, or successful boundary preservation?
* Did this refactor preserve meaning, or only behavior?
* Can this system be migrated without semantic loss?

These are questions of semantic recoverability. When a system cannot answer them from stable artifacts, it has accumulated semantic debt.

Technical debt has become a central metaphor in software engineering. Kruchten, Nord, and Ozkaya describe technical debt as a metaphor that moved beyond rhetoric into a practical framework for understanding tradeoffs, future change, and explicit management of development compromises. Modern technical debt research likewise emphasizes that unmanaged debt threatens long-lived and complex systems and requires explicit management.

Semantic debt is adjacent to this tradition but points to a different layer. It is not primarily the cost of bad code. It is the cost of lost, unstable, scattered, or inadmissible meaning.

A useful contemporary definition of semantic debt describes it as the accumulated cost created when terms, categories, entities, examples, translations, and relationships remain underdefined, contradictory, outdated, or weakly maintained, forcing readers and AI systems to infer structure that should have been declared. This paper generalizes that insight from interpretive corpora into software systems, governance artifacts, agentic development, and constitutional computing.

The central claim is simple:

> A system may still run after its meaning has become expensive to recover.

## 2. Hard Definitions

This paper uses several terms strictly. These definitions are introduced once here and used consistently afterward.

### 2.1 Semantic Debt

Semantic debt is the accumulated future cost of meaning that is underdefined, misplaced, contradictory, stale, fragmented, opaque, overcoupled, overclaimed, inadmissible, or only recoverable through inference.

A system has semantic debt when its semantic structure cannot be reliably recovered from its artifacts.

Semantic debt is not reducible to technical debt. Technical debt concerns implementation and architectural compromises; semantic debt concerns failures of recoverable meaning. The two can overlap: one shortcut may create both, and some semantic debt may be reasonably modeled as a specialized technical-debt family for a particular engineering program. The analytical distinction matters more than a universal disjointness claim.

Semantic debt is not documentation debt. Documentation debt concerns missing or stale explanatory material. Semantic debt concerns the system's meanings themselves, whether those meanings are expressed in code, schema, tests, receipts, policies, names, claims, decisions, runtime traces, or documentation.

Semantic debt is not ambiguity. Ambiguity is one possible mode of semantic debt. Semantic debt also includes category collapse, authority concealment, evidence gaps, claim inflation, policy drift, stale standing, and lossy migration.

### 2.2 Semantic Fragmentation

Semantic fragmentation is a cross-cutting debt mode in which meaning is scattered across multiple surfaces without a stable canonical home.

Fragmentation can affect terms, categories, boundaries, procedures, evidence, authority, and claims. It is not one subdomain beside the others. It is a distribution failure that may appear inside any subdomain.

### 2.3 Semantic Locality Debt

Semantic locality debt is the cost incurred when meaning exists somewhere in a system but not in a stable, canonical, locally recoverable home.

This is the precise motivating subtype behind the original concern about semantic fragmentation. The problem is not merely that meaning is distributed. The problem is that the system lacks an authoritative place where a future human, tool, or agent can recover that meaning without archaeology.

The governing principle is:

> Every meaningful distinction should have a stable home.

### 2.4 Semantic Recoverability

Semantic recoverability is the degree to which a system's meanings can be reconstructed from stable artifacts without relying on unstated human memory, guesswork, or convention.

A system has high semantic recoverability when a future reviewer can identify its terms, categories, boundaries, procedures, evidence, authority, claims, non-claims, and standing from canonical artifacts.

A system has low semantic recoverability when those answers require scattered code reading, stale documents, runtime trace interpretation, historical chats, and developer memory.

### 2.5 Governed Admissibility

Governed admissibility is the property by which a semantic artifact may support a particular claim under explicit rules.

An artifact is not admissible for a governed claim merely because it exists. A log, trace, test result, screenshot, receipt, manifest, or attestation must satisfy the claim's declared identity, provenance, scope, authority, custody, and sufficiency requirements. An observation may be evidence in the ordinary epistemic sense while remaining inadmissible for a particular governed claim. Receipt binding improves reconstruction and integrity; it does not manufacture truth, independence, representativeness, or authority.

In short:

```text
non-binding trace != evidence
artifact existence != admissibility
receipt existence != standing
```

### 2.6 Standing

Standing is a governed status granted to a package, artifact, receipt, transition, claim, or subsystem under explicit rules.

Standing is not confidence. Standing is not test success. Standing is not execution. Standing is a scoped status that persists or changes according to standing transition rules.

A major source of semantic debt is the collapse of validation, admission, execution, and standing into one vague notion of "works."

### 2.7 Scope, Obligation, and Unit of Analysis

Semantic debt is not every ambiguity, distribution, disagreement, or missing definition. It exists relative to a **semantic recovery obligation**: a future actor, claim, transition, migration, or effect requires a meaning that the relevant artifacts cannot recover at acceptable cost and standing.

Let $o$ be a declared recovery obligation and $m$ a meaning required by it. A candidate debt condition exists when:

$$
\begin{aligned}
&\operatorname{Required}(m,o) \\
&\land  \\
&\ne g \operatorname{Recoverable}(m,o,A) \\
&\land \operatorname{ExpectedFutureCost}(m,o,A) > \tau_o
\end{aligned},
$$

where $A$ is the available artifact set and $\tau_o$ is the obligation-specific tolerance. The threshold is not universal: a private sketch, a public specification, a medical control, a migration contract, and an executable authority rule carry different recoverability requirements.

The unit of analysis may be a term, concept, relation, category, boundary, procedure, evidence dependency, authority grant, claim, non-claim, translation edge, or complete semantic pathway. Debt can attach to the object itself, to its placement, or to the relation between an object and the obligation it is expected to satisfy.

Plurality is not automatically debt. Two communities may legitimately use different definitions. Distribution is not automatically fragmentation. A meaning may have several synchronized projections. The debt arises when the plurality or distribution is unmarked, unrecoverable, falsely collapsed, or unable to support the required transition.

## 3. The Two-Axis Ontology

The core contribution of this paper is a two-axis ontology.

Semantic debt is classified along two axes:

1. Semantic subdomain: what layer of meaning is indebted?
2. Debt mode: how is that layer indebted?

The first axis identifies the kind of semantic material involved. The second identifies the failure pattern.

```text
semantic debt item
  = subdomain + mode + affected artifact + consequence + repayment
  action
```

The seven subdomains are:

```text
lexical
ontological
boundary
procedural
evidentiary
authority
claim
```

The nine modes are:

```text
underdefinition
contradiction
fragmentation
staleness
opacity
overcoupling
inadmissibility
overclaim
lossy translation
```

Together they form a seven by nine diagnostic coordinate system. A single debt instance may occupy several cells, but the axes remain distinct.

Examples:

```text
Unexplained acronym GESD
  = lexical debt + underdefinition

Package admission treated as execution standing
  = ontological debt + overclaim

Policy check hidden inside filesystem adapter
  = authority debt + opacity
  = boundary debt + overcoupling

Receipt exists but does not bind prior state
  = evidentiary debt + inadmissibility

Python-to-C migration loses refusal modes
  = boundary debt + lossy translation
  = procedural debt + inadmissibility
```

The matrix is the step from concept to discipline. It lets developers, reviewers, tools, and agents locate debt precisely enough to govern it.

## 4. Axis One: Seven Semantic Subdomains

The seven subdomains are distinct in presentation even though real debt instances often occupy more than one.

### 4.1 Lexical Debt

Lexical debt is debt in the naming layer: terms, acronyms, labels, identifiers, field names, and code names.

Examples:

* one term has multiple meanings;
* multiple terms refer to the same concept without distinction;
* acronyms proliferate without a glossary;
* stale field names preserve old standing;
* deprecated names remain active without migration mapping;
* "evidence," "log," "trace," and "receipt" are used interchangeably.

Primary remedies:

* glossary;
* acronym registry;
* deprecated-name table;
* field-definition catalog;
* canonical term IDs;
* glossary coverage checks.

Lexical debt is the first fog. If terms cannot be trusted, stronger structures built on them inherit mist.

### 4.2 Ontological Debt

Ontological debt is debt in the category layer: types, entity boundaries, status distinctions, and kinds of things.

Examples:

* validation is treated as admission;
* admission is treated as execution;
* execution is treated as standing;
* standing is treated as maturity;
* receipt existence is treated as evidence sufficiency;
* fixture-scoped status is treated as broad status;
* package status, execution status, and claim status are collapsed into a generic `status`.

The critical distinction is:

```text
validation != admission
admission != execution
execution != standing
standing != broad maturity claim
```

Primary remedies:

* explicit type model;
* standing enum;
* status-transition graph;
* "this is not that" tables;
* schema-level category constraints;
* claim-to-standing mapping;
* migration records for category changes.

Ontological debt is the debt of mistaken kinds.

### 4.3 Boundary Debt

Boundary debt is debt in the jurisdiction layer: contexts, packages, adapters, domains, schemas, and substrates.

Examples:

* a UI status label implies governance standing;
* a test fixture result implies package admission;
* a Python package claim leaks into C-D.MS receipt standing;
* local validation becomes global claim;
* a domain term crosses bounded contexts without translation;
* a port or adapter boundary is treated as a convenience seam rather than an authority boundary.

Primary remedies:

* bounded contexts;
* ports and adapters;
* jurisdiction labels;
* context maps;
* translation records;
* substrate migration contracts;
* scope fields;
* non-claims.

Boundary debt is the debt of unmarked crossings.

### 4.4 Procedural Debt

Procedural debt is debt in the transition layer: state changes, decisions, migrations, repairs, admissions, refusals, and standing changes.

Examples:

* a package becomes "admitted" without an admission decision record;
* a roadmap advances without a standing transition record;
* a repair changes evidence but does not distinguish repair standing from new standing;
* a migration changes data but not the semantic status of migrated fields;
* a README changes status while the canonical index remains stale;
* a policy refactor changes behavior without a migration record.

Primary remedies:

* decision records;
* admission, refusal, and defer records;
* standing transition records;
* migration receipts;
* repair receipts;
* roadmap-to-index consistency checks.

Procedural debt is the debt of unrecorded passage.

### 4.5 Evidentiary Debt

Evidentiary debt is debt in the proof layer: receipts, manifests, traces, provenance, indexes, hashes, and auditability.

Examples:

* logs exist but are not receipt-bound;
* test output is not tied to artifact hashes;
* a build result lacks source, environment, and policy binding;
* a receipt omits prior state or next state;
* a verification report is hash-stable but semantically stale;
* evidence artifacts exist but are not indexed;
* a claim references "the run" but no canonical run receipt exists.

This paper distinguishes observations and traces from **admissible claim-supporting evidence**. Runtime logs, console output, screenshots, metrics, and ordinary traces may be relevant observations, but they do not support a governed claim until the declared admissibility profile is satisfied. Receipt binding is one important mechanism, not a universal truth condition.

Primary remedies:

* receipts;
* manifests;
* hash seals;
* content addressing;
* provenance graphs;
* evidence chains;
* fixture replay;
* claim-to-evidence maps;
* admissibility predicates.

Evidentiary debt is the debt of behavior without proof.

### 4.6 Authority Debt

Authority debt is debt in the permission layer: policy, capability, warrant, execution authority, and claim authority.

Examples:

* a function writes to disk because it can;
* a subprocess launches because the script reached that line;
* a validator mutates state;
* a package executes because it passed validation;
* a tool infers permission from availability;
* a policy decision is hidden inside an adapter;
* a compiler is invoked without execution authority;
* a claim is made because an artifact exists, not because standing was granted.

Primary remedies:

* explicit governed context;
* authority references;
* capability sets;
* policy surfaces;
* adapter mediation;
* least-authority execution;
* refusal codes;
* admission records.

Authority debt is the debt of action without warrant.

### 4.7 Claim Debt

Claim debt is debt in the assertion layer: claims, non-claims, standing claims, maturity claims, equivalence claims, and scope.

Examples:

* "validated" is presented as "admitted";
* "fixture-scoped" is presented as general;
* "receipt exists" is presented as "schema-conformant receipt standing";
* "runs locally" is presented as governed execution;
* "migration succeeded" is presented as equivalence;
* "one self-reference passed" is presented as self-hosting;
* a README implies a stronger status than the canonical index supports.

Primary remedies:

* non-claims file;
* claim ledger;
* claim-to-evidence mapping;
* standing transition records;
* scope tags;
* active blocking claims;
* explicit revocation of non-claims.

Claim debt is the debt of saying more than the system can support.

## 5. Axis Two: Nine Debt Modes

The seven subdomains identify what layer is indebted. The nine modes identify how the debt manifests.

### 5.1 Underdefinition

Underdefinition occurs when a semantic object exists but lacks sufficient definition.

Examples:

* acronym without expansion;
* status without transition rules;
* refusal code without meaning;
* policy version without policy surface;
* receipt field without binding semantics.

Typical remedies:

* definitions;
* schemas;
* glossary entries;
* transition rules;
* field constraints;
* examples and counterexamples.

### 5.2 Contradiction

Contradiction occurs when two or more semantic surfaces assert incompatible meanings.

Examples:

* README says "preflight only" while a decision record grants standing;
* batch index says the next rung is the current rung;
* one schema treats `status` as validation while another treats it as standing;
* non-claims block a claim that another artifact asserts as granted;
* policy permits an effect that the authority model forbids.

Typical remedies:

* canonical source hierarchy;
* consistency checks;
* contradiction detector;
* claim ledger;
* standing graph validation;
* stale artifact retirement.

### 5.3 Fragmentation

Fragmentation occurs when meaning is scattered across multiple surfaces without a stable canonical home.

Examples:

* authority rules split across code, README, tests, and operator memory;
* proof split across logs, reports, screenshots, and filenames;
* acronym meaning distributed across transcripts;
* standing status spread across roadmap, index, seal, and README;
* refusal semantics appear only in negative tests and comments.

Typical remedies:

* stable canonical homes;
* glossary entries;
* claim ledger;
* standing graph;
* receipt schema;
* non-claims file;
* artifact index;
* semantic debt ledger.

Fragmentation is cross-cutting. Semantic locality debt is the specific form of fragmentation where the missing element is a stable canonical home.

### 5.4 Staleness

Staleness occurs when a semantic surface was once correct but no longer matches current standing, behavior, policy, schema, or evidence.

Examples:

* README says the next milestone is a batch already completed;
* an index field preserves an old status name;
* a glossary definition survives after the term changes;
* a non-claim remains active after an admissible revocation but was not updated;
* a policy description references an obsolete capability model.

Typical remedies:

* freshness checks;
* canonical index comparison;
* standing timestamp validation;
* stale term detection;
* deprecation records;
* update obligations in release gates.

### 5.5 Opacity

Opacity occurs when meaning is present but hidden inside implementation details, conventions, or side effects.

Examples:

* policy decision embedded in an adapter if statement;
* authority inferred from an environment variable;
* migration meaning encoded only in SQL;
* refusal code constructed dynamically with no registry;
* claim implied by a script name.

Typical remedies:

* extracted policy surfaces;
* explicit registries;
* typed models;
* static analysis;
* receipt emission;
* code-to-artifact mapping;
* decision records.

### 5.6 Overcoupling

Overcoupling occurs when meanings that should remain distinct are bound together so tightly that one cannot change without silently affecting the other.

Examples:

* policy and execution share one function;
* state migration and standing migration are coupled;
* logging and evidence emission use the same path;
* validation and admission use the same status field;
* UI labels drive governance decisions;
* adapter availability implies authority.

Typical remedies:

* separation of core and adapters;
* typed status distinctions;
* policy interfaces;
* effect requests;
* standing transition records;
* claim layers;
* bounded contexts.

### 5.7 Inadmissibility

Inadmissibility occurs when a semantic artifact cannot support the claim it is asked to support.

Examples:

* receipt lacks state hashes;
* test report lacks artifact hashes;
* policy decision lacks authority reference;
* migration record lacks source and target hashes;
* claim references non-binding traces;
* standing transition lacks transition record;
* refusal has no typed code.

Typical remedies:

* admissibility predicates;
* schema checks;
* receipt binding;
* artifact hashes;
* authority references;
* claim-to-evidence validation.

### 5.8 Overclaim

Overclaim occurs when a claim exceeds its evidence, standing, scope, or authority.

Examples:

* local fixture success becomes broad reliability;
* package admission becomes execution standing;
* execution standing becomes execution occurred;
* schema validation becomes schema-conformant standing;
* migration success becomes equivalence;
* equivalence becomes self-hosting.

Typical remedies:

* non-claims;
* claim ledger;
* scope fields;
* standing graph;
* refusal of unsupported claims;
* maturity-level separation.

### 5.9 Lossy Translation

Lossy translation occurs when software, data, schemas, policies, or receipts move across representations while losing semantic obligations.

Examples:

* Python behavior is ported to C but refusal semantics disappear;
* JSON fields migrate to a database without preserving constraints;
* receipt schema changes but authority binding becomes optional;
* domain model becomes API contract but loses bounded-context assumptions;
* governance policy becomes prose and loses totality;
* natural-language claim becomes machine status without scope.

Typical remedies:

* migration contracts;
* mapping functions;
* dual hashes;
* equivalence obligations;
* policy refinement checks;
* receipt preservation checks;
* loss reports.

## 6. The Semantic Debt Matrix

The semantic debt matrix is the center of the ontology. It combines seven subdomains with nine modes. It is not a claim about empirical frequency. It is a diagnostic space: each cell names a possible kind of meaning failure and suggests a different remediation path.

```text
                 Underdef Contra Frag Stale Opaque Coupled Inadm Overclaim Lossy
Lexical x x x x x - - - x
Ontological x x x x x x x x x
Boundary x x x x x x x x x
Procedural x x x x x x x x x
Evidentiary x x x x x x x x x
Authority x x x x x x x x x
Claim x x x x x x x x x
```

The sparse cells are intentional. Some combinations are less natural than others. For example, lexical inadmissibility is usually mediated through evidentiary or claim debt rather than appearing as a primary cell. The matrix is not a taxonomy of all observed incidents. It is a map of diagnostic possibility.

### 6.1 High-Value Matrix Examples

```text
Lexical + underdefinition
  Example: GESD appears without expansion.
  Risk: operators infer meaning from context.
  Remedy: add glossary entry and link from roadmap.

Lexical + staleness
  Example: old field name preserves previous standing.
  Risk: tools read obsolete meaning as current.
  Remedy: add deprecation table and migration mapping.

Ontological + overclaim
  Example: validation is treated as admission.
  Risk: local check becomes unauthorized status ascent.
  Remedy: enforce validation/admission distinction in standing graph.

Ontological + overcoupling
  Example: one `status` field stores validation, admission, and
  execution state.
  Risk: category collapse.
  Remedy: split status into typed fields.

Boundary + lossy translation
  Example: Python package is ported to C but refusal modes vanish.
  Risk: behavior is preserved while governance semantics are lost.
  Remedy: require migration contract with refusal mapping.

Boundary + opacity
  Example: adapter boundary hides policy decision.
  Risk: authority crossing cannot be inspected.
  Remedy: extract policy surface and effect request record.

Procedural + contradiction
  Example: README says preflight while decision record grants standing.
  Risk: canonical transition cannot be identified.
  Remedy: source hierarchy and consistency gate.

Procedural + staleness
  Example: roadmap next rung points to current rung.
  Risk: process loops or false completion.
  Remedy: roadmap/index cross-check.

Evidentiary + inadmissibility
  Example: receipt lacks prior-state hash.
  Risk: claim cannot be supported.
  Remedy: require receipt schema check.

Evidentiary + fragmentation
  Example: proof split across logs, screenshots, and filenames.
  Risk: no claim-supporting evidence chain.
  Remedy: bind artifacts into receipt or manifest.

Authority + opacity
  Example: filesystem write authority inferred from environment
  variable.
  Risk: hidden permission path.
  Remedy: require explicit authority reference.

Authority + overcoupling
  Example: validation function also mutates state.
  Risk: checking becomes acting.
  Remedy: separate validator from executor.

Claim + overclaim
  Example: fixture success is described as self-hosting.
  Risk: maturity inflation.
  Remedy: active non-claim and standing gate.

Claim + contradiction
  Example: NONCLAIMS.md blocks a claim asserted by README.
  Risk: incompatible claim surfaces.
  Remedy: claim ledger evaluation.
```

A semantic debt review should classify each issue by matrix coordinate and assign a repayment action.

## 7. From Matrix to Governing Artifacts

The matrix becomes useful when each debt coordinate points to an artifact capable of preventing, detecting, or repaying it. These artifacts are not a second introduction to the theory. They are the enforcement layer implied by the matrix.

### 7.1 Glossary

Primary coverage:

```text
lexical debt
underdefinition
fragmentation
staleness
lossy translation
```

The glossary defines terms, acronyms, standing states, refusal codes, policy names, claim names, and deprecated names. It prevents name drift and gives tools a canonical vocabulary.

### 7.2 Non-Claims File

Primary coverage:

```text
claim debt
overclaim
contradiction
staleness
standing confusion
```

The non-claims file records what the system does not currently assert. It blocks unsupported maturity claims and prevents evidence from being inflated into standing.

### 7.3 Claim Ledger

Primary coverage:

```text
claim debt
evidentiary debt
inadmissibility
contradiction
overclaim
```

The claim ledger maps claims to supporting receipts and blocking non-claims. It answers what the system may currently assert.

### 7.4 Standing Graph

Primary coverage:

```text
ontological debt
procedural debt
claim debt
overclaim
staleness
```

The standing graph defines permissible standing transitions, revocations, downgrades, and scoped maturity claims. It prevents validation, admission, execution, and standing from collapsing into one status.

### 7.5 Migration Contract

Primary coverage:

```text
boundary debt
procedural debt
lossy translation
inadmissibility
```

The migration contract maps meanings across versions, schemas, languages, substrates, packages, and governance levels. It prevents behavior-preserving translations from becoming meaning-losing translations.

### 7.6 Receipt Schema

Primary coverage:

```text
evidentiary debt
authority debt
inadmissibility
opacity
fragmentation
```

The receipt schema defines what fields must be bound for a trace to become evidence. It binds state, policy, authority, artifacts, effects, refusals, and claims.

### 7.7 Semantic Debt Ledger

Primary coverage:

```text
all subdomains
all modes
```

The semantic debt ledger records debt items by coordinate, risk, affected artifact, and repayment action. It turns the matrix into trackable engineering work.

## 8. Semantic Debt Ledger

A semantic debt ledger records known semantic debt items.

A minimal ledger entry should include:

```text
debt_id
title
subdomain
mode
affected_artifacts
description
risk
blocked_claims
related_nonclaims
severity
repayment_action
owner
status
introduced_by
detected_by
resolved_by
```

Example:

```text
debt_id: SD-LEX-001
title: GESD acronym undefined
subdomain: lexical
mode: underdefinition
affected_artifacts: roadmap, verifier report
risk: operator confusion; false standing inference
repayment_action: add GESD to GLOSSARY.md and link from roadmap
status: open
```

Example:

```text
debt_id: SD-CLAIM-004
title: Receipt existence implies schema standing
subdomain: claim, ontological
mode: overclaim, category collapse
affected_artifacts: README
risk: standing inflation
blocked_claims: schema_conformant_receipt_standing
repayment_action: add non-claim and require standing transition record
status: open
```

The ledger turns semantic debt into governable work.

## 9. Semantic Debt Interest

Semantic debt interest is the increasing cost of future interpretation, change, migration, audit, or governance caused by unresolved semantic debt.

Forms of interest include:

* longer onboarding time;
* agent confusion;
* incorrect refactors;
* false claims;
* unsafe automation;
* migration loss;
* duplicated terminology;
* evidence reconstruction cost;
* policy drift;
* audit failure;
* standing inflation;
* inability to admit or refuse artifacts mechanically.

Semantic debt interest compounds when multiple debts interact.

Examples:

```text
lexical debt + claim debt
  -> ambiguous claims

boundary debt + authority debt
  -> hidden authority leakage

evidentiary debt + procedural debt
  -> unprovable transition

ontological debt + overclaim
  -> false maturity ascent
```

The most expensive semantic debts are those that make future evidence impossible.

## 10. Proper and Improper Semantic Defragmentation

Semantic defragmentation is the act of reorganizing a system so its meanings become more locally recoverable, better bounded, and more admissible.

Proper semantic defragmentation:

* moves terms into a glossary;
* separates validation, admission, execution, and standing;
* extracts policy from implementation;
* binds traces into receipts;
* restores non-claims;
* names refusal modes;
* adds standing records;
* creates migration mappings;
* updates stale indexes;
* separates effects from core logic.

Improper semantic defragmentation is a refactor, cleanup, compression, abstraction, or migration that reduces apparent complexity while increasing semantic debt.

Examples:

* merging policy and execution because it is shorter;
* deleting refusal tests because success tests pass;
* replacing receipts with logs;
* removing non-claims because they seem negative;
* collapsing multiple statuses into one field;
* renaming terms without migration table;
* moving authority checks into UI code;
* treating a fixture-specific result as general standing.

Improper semantic defragmentation explains why some clean systems become less governable. They are cleaner in implementation shape and poorer in semantic shape.

## 11. Detection Methods

Semantic debt can be detected by human review, static tooling, dynamic checks, agent audits, and governance gates.

### 11.1 Lexical Detection

Checks:

* glossary coverage;
* undefined acronyms;
* deprecated term usage;
* synonym collisions;
* overloaded field names;
* term-definition drift.

### 11.2 Ontological Detection

Checks:

* status enum review;
* type hierarchy review;
* category-collapse detection;
* standing graph validation;
* "this is not that" invariant checks.

### 11.3 Boundary Detection

Checks:

* context-map review;
* adapter/core separation;
* forbidden dependencies;
* cross-substrate claim checks;
* scope field validation.

### 11.4 Procedural Detection

Checks:

* decision record coverage;
* roadmap/index consistency;
* standing transition records;
* migration receipt coverage;
* repair record distinction.

### 11.5 Evidentiary Detection

Checks:

* receipt schema conformance;
* artifact hash coverage;
* evidence chain completeness;
* trace-to-receipt distinction;
* claim-to-evidence satisfiability.

### 11.6 Authority Detection

Checks:

* effect-without-authority detection;
* capability surface review;
* policy totality;
* adapter mediation;
* hidden subprocess/network/filesystem access in core.

### 11.7 Claim Detection

Checks:

* claim ledger evaluation;
* non-claim preservation;
* unsupported claim detection;
* maturity-level separation;
* scope mismatch detection.

## 12. Semantic Debt and Agentic Software Development

Agentic development makes semantic debt easier to create and easier to detect.

AI agents can generate code that passes local tests while violating project meanings. They may rename concepts, merge statuses, delete comments, infer missing authority, flatten domain distinctions, or treat natural-language instructions as optional style. The result can be high functional utility with low semantic integrity.

Semantic debt theory gives agentic development a diagnostic target. It says not only "the agent violated instructions," but which semantic subdomain was damaged and by what mode.

### 12.1 Normative Failure Modes for Agents

Agentic systems should treat the following as first-class semantic hazards.

#### Acronym Drift

An agent introduces or reuses an acronym without a glossary entry.

Debt coordinate:

```text
lexical + underdefinition
lexical + fragmentation
```

Required guard:

```text
No new acronym, standing term, refusal code, claim kind, or verifier
lane name without glossary update.
```

#### Status Collapse

An agent collapses validation, admission, execution, and standing into a single status.

Debt coordinate:

```text
ontological + overcoupling
claim + overclaim
```

Required guard:

```text
Typed status fields and standing graph validation.
```

#### Authority Inference

An agent infers permission from code reachability, filesystem access, API credentials, or prior success.

Debt coordinate:

```text
authority + opacity
authority + overclaim
```

Required guard:

```text
No effect admission without explicit authority reference and policy
permit.
```

#### Claim Inflation

An agent describes a local result as a broader maturity claim.

Debt coordinate:

```text
claim + overclaim
ontological + category collapse
```

Required guard:

```text
Claim ledger check and active non-claim preservation.
```

#### Boundary Leakage

An agent moves policy into adapters, imports substrate-specific behavior into core logic, or lets UI language imply governance standing.

Debt coordinate:

```text
boundary + overcoupling
authority + opacity
```

Required guard:

```text
Adapter isolation, context boundary checks, and migration contracts.
```

#### Evidence Substitution

An agent treats logs, traces, summaries, or console output as evidence.

Debt coordinate:

```text
evidentiary + inadmissibility
evidentiary + fragmentation
```

Required guard:

```text
Only artifacts satisfying the declared claim-admissibility profile
can support governed claims; receipts bind transitions but do not by
themselves establish truth or sufficiency.
```

### 12.2 Agent Operating Rule

A coding agent operating under semantic debt governance should obey:

```text
Do not introduce, rename, delete, merge, or promote a semantic
object unless the corresponding governing artifact is updated.
```

Examples:

```text
new term -> glossary update
new claim -> claim ledger update
new limitation -> non-claim update
new status -> standing graph update
new evidence -> receipt schema or manifest update
new migration -> migration contract update
new debt -> semantic debt ledger update
```

Agentic development makes semantic debt easier to create and easier to detect. The difference is whether the project gives agents canonical surfaces to respect.

## 13. Relationship to Constitutional Semantic Engineering

Semantic Debt and Constitutional Semantic Engineering are paired concepts.

```text
Semantic Debt
  diagnoses meaning failure

Constitutional Semantic Engineering
  builds systems to prevent, detect, and repay meaning failure
```

CSE repays semantic debt by making meaning, authority, effects, evidence, refusal, standing, and non-claims first-class artifacts.

Semantic debt explains why CSE matters. CSE provides engineering mechanisms to keep semantic debt from compounding silently.

## 14. Semantic Debt in the Governed Meaning Base

The author-confirmed terminology lineage is `CCF -> CMB -> GMB`. **Governed Meaning Base (GMB)** is the current name. CCF and CMB remain historical names in exact titles, quotations, source descriptions, and lineage explanations; they are not separate present-day architectures.

GMB gives the Semantic Debt ontology a corpus-scale operating surface. It can preserve stable identities, names and aliases, definitions, typed relations, boundaries, claims, non-claims, evidence dependencies, authority, standing, source custody, disputes, projections, and revisions. The universal Governed Semantic Model supplies the common representational grammar; GMB is the governed meaning architecture in which exact corpus material and reviewed semantic structures can be traversed and revised.

A stable home does not require one physical file. It requires a recoverable identity and an explicit authority relation among representations. A canonical concept may therefore have an exact source expression, a compact token, a slug, a concise explanation, a full semantic neighborhood, and several pedagogical projections without incurring locality debt, provided their derivation and standing remain inspectable.

Within the current Semantic Zoom tooling, RPZ surfaces illustrate this separation:

| Surface | Semantic-debt function |
| --- | --- |
| RPZ0 | Supplies a compact retrieval token without pretending the token is the concept. |
| RPZ1 | Supplies a stable slug and canonical display surface while retaining collision handling and aliases. |
| RPZ2 | Supplies a portable concise explanation whose compression losses can be compared with the fuller record. |
| RPZ3 | Supplies definition, role, provenance, standing, adjacency, and artifact context for deeper recovery. |

GMB does not eliminate semantic debt. It can accumulate stale aliases, unmarked contradictions, false identity merges, detached evidence, standing drift, overcompressed explanations, and misleading canonicalization. The debt matrix therefore becomes an audit layer over GMB nodes, relations, artifacts, and projections.

The corpus interfaces are typed:

| Corpus work or structure | Relation to Semantic Debt |
| --- | --- |
| *Semantic Legitimacy Before Context* | Prevents semantically indebted or standing-ambiguous material from silently becoming operative context. |
| *Reasoning by Way of Receipts* | Preserves bounded reasoning transitions, alternatives, decisions, debts, and revisions; a receipt provides reconstruction, not automatic truth. |
| *The Three Hash Rule* | Separates exact object state, admissibility configuration, and meaning commitment so matching one cannot conceal debt in another. |
| *A Formal Theory of Work Custody* | Makes the live responsibility for repayment or adjudication recoverable without turning custody into semantic correctness. |
| *Admissibility Engineering* | Turns debt-sensitive claim and transition requirements into inspectable schemas, gates, refusals, and bypass tests. |
| Constitutional Semantic Engineering | Provides preventive and reparative engineering mechanisms; Semantic Debt provides the diagnostic coordinate system. |
| GMB and universal GSM | Supply the governed corpus substrate and common semantic grammar against which locality, translation, standing, and claim debt can be inspected. |

These are interfaces, not automatic work-identity or system-identity mergers. Storage in GMB does not grant truth, author approval, publication status, or canonical standing.

## 15. Minimal Governance Model

A semantic debt governance model should include seven artifacts:

```text
glossary
non-claims file
claim ledger
standing graph
migration contract
receipt schema
semantic debt ledger
```

Together these artifacts provide a minimal discipline for semantic governance. They are a profile, not a universal requirement: lower-consequence contexts may need fewer surfaces, while high-consequence systems may need stronger identity, custody, independence, and review structures.

## 16. Realization Funnel

| Stage | Semantic Debt content |
| --- | --- |
| Possibility | Meaning failure can be treated as a governable future-cost structure rather than an unavoidable by-product of complexity. |
| Specification | Define recovery obligations, units of analysis, subdomains, modes, debt records, consequences, repayment duties, standing, and closure conditions. |
| CM1 | Enumerate admissible diagnostic coordinates, recovery surfaces, repayment strategies, intentional deferrals, exceptions, and non-action paths, including harmful or misleading repairs. |
| CM2 | Prefer configurations that improve recoverability without erasing plurality, laundering authority, centralizing interpretation unnecessarily, or destroying exact source custody. |
| Instance Configuration | Select scope, audience, obligations, thresholds, severity rules, canonical surfaces, claim dependencies, detectors, owners, and review cadence for a particular corpus or system. |
| Implementation Realization | Realize glossaries, GMB entries, semantic indexes, non-claims, claim ledgers, standing graphs, migration contracts, receipt profiles, debt ledgers, and verifiers. |
| Evidence | Bind detected debt to exact artifacts, dependency paths, failures, reviewer observations, measurements, repayment changes, counterexamples, and residual limitations. |
| Revision | Admit, defer, repay, reopen, or reclassify debt while preserving prior meanings, reasons, affected claims, and migration consequences. |

The paper chiefly contributes Specification and CM1. Its preferred artifacts and anti-collapse rules contribute CM2. Any concrete debt scanner, GMB profile, severity metric, or admission gate is an Instance Configuration or Implementation Realization and requires separate evidence.

## 17. Formal Sketch

Let a semantic debt item be:

$$
d = \langle A, M, X, r, c \rangle
$$

Where:

* $A$ is the affected semantic subdomain.
* $M$ is the debt mode.
* $X$ is the affected artifact set.
* $r$ is the risk or consequence.
* $c$ is the corrective obligation.

Let the set of semantic subdomains be:

$$
A \in \{Lex, Ont, Bound, Proc, Evid, Auth, Claim\}
$$

Let the set of modes be:

$$
\begin{aligned}
M \in \{&Underdef, Contra, Frag, Stale, Opaque, Coupled, Inadm, \\
&Overclaim, Lossy\}
\end{aligned}
$$

A semantic debt ledger is then:

$$
D = \{d_1, d_2, ..., d_n\}
$$

A system is semantically admissible for a claim $k$ only if:

$$
supports(k) \land \neg blocked(k) \land \neg critical\_debt(k,D)
$$

Where $critical\_debt(k,D)$ holds when unresolved debt items affect the semantic surfaces needed to support $k$.

For example, a claim of schema-conformant receipt standing is blocked if unresolved debt affects receipt schema definition, receipt binding, standing transition records, or active non-claims.

Semantic debt is therefore not only descriptive. It can participate in claim evaluation.

### 17.1 Claim-Relative Criticality

The source formalization becomes operational when debt is evaluated against an explicit claim dependency set. Let $Dep(k)$ be the semantic artifacts and relations required to support claim $k$. Then:

$$
\begin{aligned}
&\operatorname{critical\_debt}(k,D) \\
&\iff \exists d \in D: \operatorname{Open}(d) \\
&\land \operatorname{Affected}(d) \cap Dep(k) \\
&\neq \emptyset \\
&\land \operatorname{Severity}(d,k) \ge \tau_k
\end{aligned}.
$$

This rule avoids two opposite errors. It does not allow unrelated debt anywhere in a large corpus to block every claim, and it does not allow debt on a load-bearing dependency to be ignored because the claim has other support.

A debt record should therefore preserve at least:

$$
d = \langle id,A,M,X,O,r,c,e,s,t,p \rangle,
$$

where $id$ is stable identity; $A$ and $M$ are subdomain and mode; $X$ is the affected artifact or semantic-object set; $O$ is the recovery obligation; $r$ is risk; $c$ is corrective obligation; $e$ is evidence; $s$ is status and standing; $t$ is temporal state; and $p$ is provenance. This extends rather than invalidates the compact five-field sketch above.

### 17.2 Interest as a Review Heuristic

Semantic debt interest is not yet an empirically calibrated quantity. A useful review heuristic is:

$$
I(d,t) = E_d \cdot P_d \cdot C_d(t) \cdot U_d,
$$

where $E_d$ is exposure across claims or consumers, $P_d$ is propagation potential, $C_d(t)$ is expected correction or recovery cost over time, and $U_d$ is consequence weight. The expression orders questions; it does not establish commensurable measurements or predict realized cost.

## Maintenance Accounting for Meaning Obligations

The completed P1 corpus positions Semantic Debt as **maintenance accounting and diagnostic taxonomy for meaning obligations whose recovery, interpretation, governance, or repair has become costly or unreliable**. It does not replace the specific theories of fragmentation, binding, identity, authority, evidence, or transformation that diagnose why the obligation failed.

- **Adjacent work:** *Transformation-Dominant Semantic Systems*  
  **Supplies:** A diagnostic of transformation, required carriage, accepted and silent loss, recoverability, and cost.  
  **Semantic-debt boundary:** TDSS measures a change event or workflow; debt records the resulting unresolved burden across time.

- **Adjacent work:** *Global Term Key: Constitutional Lexical Identity Through Disambiguated Semantic Binding*  
  **Supplies:** Lexical identity and disambiguation contracts.  
  **Semantic-debt boundary:** GTK failures can create lexical debt; GTK is not the whole debt ledger.

- **Adjacent work:** *Semantic Binding Quality (SBQ)*  
  **Supplies:** Binding coherence, coverage, and fragility.  
  **Semantic-debt boundary:** Low SBQ may predict debt, but disagreement or low score is not automatically a debt entry.

- **Adjacent work:** *What Software Systems Actually Receipt, Govern, and Hide*  
  **Supplies:** Visibility gaps among actions, governed surfaces, and recorded evidence.  
  **Semantic-debt boundary:** Hidden or unreceipted behavior can create procedural or evidentiary debt; the visibility analysis remains distinct.

- **Adjacent work:** *Semantic Fragmentation and Constitutional Structure*  
  **Supplies:** Structural fragmentation and possible constitutional responses.  
  **Semantic-debt boundary:** Fragmentation is one debt mode; some plurality is legitimate and some debt is not fragmentation.

The accountable unit is a debt entry rather than a metaphorical total:

$$
\begin{aligned}
DebtEntry= (&obligation, subject, subdomain, mode, cause, \\
&affected\_claims, evidence, interest\_basis, remediation, \\
&custodian, status, revision)
\end{aligned}.
$$

A **defect** is an observed failure against a requirement. A **risk** is a possible future loss. A **disagreement** may be legitimate plurality. **Complexity** may be irreducible. **Debt** exists when a declared semantic obligation is left unresolved or made materially more expensive to discharge, while continuation is permitted under an explicit posture. Conflating these categories manufactures debt and pressures unjustified normalization.

Semantic interest must be reported as an evidence-linked maintenance heuristic, not a universal financial scalar. Observable indicators can include repeated reinterpretation, widening disagreement, repair time, migration failures, dependency propagation, lost provenance, delayed review, or increasing claim ceilings required to compensate for uncertainty. Weighting those indicators remains profile- and decision-relative.

The universal GSM can type   
`INCURS_SEMANTIC_DEBT`, `OWES_OBLIGATION`, `AFFECTS_CLAIM`,  
`CAUSED_BY_LOSS`, `PROPAGATES_TO`, `ACCRUES_UNDER`, `CUSTODIED_BY`, `REMEDIATED_BY`,  
`ACCEPTED_UNDER_CEILING`, `DISPUTED_AS_DEBT`,  
and `REVISED_BY`. The ledger can coexist with plural semantics by representing contests and non-debt findings explicitly.

This integration establishes four editorial commitments: adopt maintenance accounting for meaning obligations as the official corpus role; adopt the debt-entry object; enforce the defect/risk/disagreement/complexity/debt separation; and treat semantic interest as a bounded evidence-linked heuristic unless a validated metric is later established.

## Recoverable Infrastructure Obligations

The fixed-seed comparison with SBQ, Governed Semantic Cartography, Semantic Computing Infrastructure, and Cold Boot Continuity turns an isolated debt entry into a recoverable propagation record:

$$
\begin{aligned}
D^*= (&entry, origin, affected\_bindings, views, services, \\
&capsules, interest\_observations, remediation, \\
&closure\_witnesses, reopen\_triggers)
\end{aligned}.
$$

SBQ can supply bounded diagnostic evidence, including instability, distortion, or constraint misalignment. It does not decide that an obligation exists or that a finding is debt. The debt ledger must record the governing obligation, acceptance posture, custodian, affected dependents, and the evidence that distinguishes debt from defect, risk, disagreement, or irreducible complexity.

Cartographic views can expose debt or hide it through projection and locality. Each affected coordinate or path should link to open entries and known remediation state. A pedagogical projection may simplify the debt explanation, but it must preserve recovery to the full entry and cannot display a clean map while silently dropping consequential unresolved obligations.

Semantic infrastructure can propagate debt through shared identity, storage, compilation, navigation, cache, and interface services. The ledger should distinguish origin from propagation and name the dependency path rather than charging every consumer with the same cause. Infrastructure replacement does not retire debt unless closure witnesses show that the obligation was discharged or legitimately removed.

Cold-boot capsules must carry applicable open debt, disputed classifications, and reopen triggers. Recovering artifacts while forgetting their semantic liabilities produces a false continuity claim. The universal GSM can type   
`PROPAGATES_DEBT_THROUGH_SERVICE`,  
`AFFECTS_ATLAS_VIEW`, `CARRIED_IN_CONTINUITY_CAPSULE`, `SUPPORTED_BY_SBQ_SIGNAL`,  
`DISTINGUISHES_DEBT_ORIGIN`, `CLOSED_BY_WITNESS`, and   
`REOPENED_BY_DEPENDENCY_CHANGE`.

This randomized review establishes four editorial commitments: adopt the debt-propagation record; require atlas views and shared services to expose applicable entries; carry open debt and disputes through cold boot; and require closure witnesses rather than migration or disappearance alone.

## Obligation-Bound Semantic Debt Accounting

Seventeen downstream uses apply Semantic Debt to cold boot, epistemic orientation and lineage, compilers, cartography, crystals, ontology laundering, migration, SBQ, semantic infrastructure, attractors, integrity enforcement, optional coordination, qualia research, transformation systems, MCIR engineering, and comparative software analysis. They confirm its corpus role as maintenance accounting for unresolved semantic obligations. Ambiguity, low quality, complexity, age, disagreement, or incompleteness is not automatically debt.

The debt entry is:

$$
\begin{aligned}
D^*= (&obligation, subject, generation, beneficiaries, origin, \\
&domain, mode, principal, interest, criticality, evidence, \\
&dependencies, repair\_options, accepted\_risk, expiry, \\
&status, disposition)
\end{aligned}.
$$

An entry requires a scoped obligation: something owed to a user, maintainer, interpreter, dependent claim, migration, authority boundary, evidence chain, or future reconstruction. `principal` records the unresolved semantic work or loss;

`interest` records additional burden or risk caused by deferral. Interest is a review heuristic unless its units, baseline, and observation method are measured. Debt can be knowingly accepted, disputed, transferred with consent, discharged, superseded, or declared unrecoverable; none of those outcomes may be inferred from silence.

Debt propagation follows typed dependencies rather than lexical similarity. A changed definition may invalidate claims, profiles, tests, interfaces, translations, and decisions, but only where a binding is demonstrated. Repair can also destroy legitimate plurality, historical meaning, privacy, or compatibility. Defragmentation therefore requires a declared preservation and remainder contract.

The universal GSM can type   
`OWES_SEMANTIC_OBLIGATION`, `ACCRUES_SEMANTIC_INTEREST`,  
`DEPENDS_ON_DEBTED_BINDING`, `ACCEPTS_SEMANTIC_RISK`, `DISPUTES_DEBT_ENTRY`,  
`REPAIRS_WITH_REMAINDER`, `DISCHARGES_SEMANTIC_DEBT`,  
and   
`DOES_NOT_EQUATE_QUALITY_WITH_DEBT`.

This reverse-dependency review establishes four editorial commitments: adopt the obligation-bound debt entry; distinguish principal, interest, criticality, and accepted risk; require typed propagation and preservation contracts; and prohibit ambiguity, age, low SBQ, or complexity from becoming debt without an owed obligation.

## 18. Counterexamples, Failure Modes, and Limits

The ontology can itself create semantic debt if applied without restraint.

1. **Legitimate plurality.** Competing definitions may be necessary. Forcing one canonical term can erase domain or community differences.
2. **Legitimate distribution.** Meaning may be intentionally distributed across independent authorities or projections. One stable identity and derivation graph can be safer than one centralized file.
3. **Premature closure.** A glossary can freeze a concept whose meaning should remain contested or provisional.
4. **Governance overhead.** Receipts, ledgers, and standing graphs can cost more than the recovery obligation justifies.
5. **False precision.** Numerical severity or interest scores can conceal uncertain judgments and become targets of Goodharting.
6. **Detector error.** Acronym, contradiction, staleness, and claim checks can yield false positives or miss context-sensitive debt.
7. **Canonical-source capture.** Declaring a source canonical can launder the authority of the party that controls it.
8. **Repair-induced loss.** Renaming, merging, deduplicating, or compressing can destroy provenance, minority interpretations, refusal semantics, or historical meaning.
9. **Infinite documentation regress.** Every governing artifact introduces terms and relations that may themselves require governance.
10. **Evidence category error.** Receipt binding improves admissibility and reconstruction but does not create truth, independence, representativeness, or causal validity.

The ontology has not yet been empirically validated as a complete classification, a predictor of maintenance cost, or a demonstrated improvement over alternative knowledge-governance methods. The seven-by-nine matrix is a proposal. Sparse cells, overlaps, and category boundaries require comparative cases and adversarial review.

Debt repayment should therefore satisfy a proportionality rule:

$$
\operatorname{Repay}(d)
\Rightarrow
\operatorname{ExpectedRecoveryGain}(d)
>
\operatorname{GovernanceCost}(d)
$$

unless an overriding safety, legal, constitutional, or evidence-preservation obligation applies.

## 19. Open Problems

Several problems remain open.

### 19.1 Severity Metrics

How should semantic debt severity be measured? Possible factors include claim impact, authority impact, migration impact, evidence impact, agent confusion risk, and cost to repair.

### 19.2 Automated Debt Detection

Which forms of semantic debt can be detected statically? Lexical underdefinition and stale references may be straightforward. Ontological collapse and claim inflation may require stronger semantic models.

### 19.3 Semantic Debt Interest

How should interest be estimated? Semantic debt may compound nonlinearly when lexical, ontological, evidentiary, and claim debts interact.

### 19.4 Cross-System Debt Propagation

How does semantic debt propagate through APIs, packages, schemas, model outputs, documentation, and agent instructions?

### 19.5 Non-Claim Synthesis

Can systems automatically infer appropriate non-claims from missing evidence, failed tests, incomplete migrations, or unsupported standings?

### 19.6 Semantic Debt in Machine Learning Systems

ML systems introduce additional semantic debt through dataset labels, prompt instructions, embeddings, latent representations, evaluation gaps, and benchmark overclaims.

### 19.7 Formal Ontology Standard

The proposed ontology may be developed into a machine-readable standard for debt ledgers, claim ledgers, and governance checks.

## Semantic Debt Is Not a Universal Defect Score

### Public orientation

Semantic debt is the future cost created when important meaning becomes unstable, scattered, stale, contradictory, overclaimed, inadmissible, or recoverable only by inference. Software may continue running while nobody can reliably say what a term, rule, decision, or artifact means. The concept is diagnostic; it is not a scalar verdict on a project or author.

### Adversarial tests

1. **Documentation-debt collapse.** Missing prose is treated as the whole problem. Meaning may be encoded in schemas, tests, interfaces, data, policy, models, names, or social practice.
2. **Technical-debt collapse.** An implementation compromise is labeled semantic debt without an unstable meaning relation. The categories may interact but are not identical.
3. **Metric-Goodhart attack.** Teams optimize a debt score by adding definitions or links that do not improve recoverability or consistency. Metrics need sampled human and operational validation.
4. **False-positive attack.** Legitimate plurality, uncertainty, or local vocabulary is classified as debt. Disagreement and contextual variation require preservation, not forced normalization.
5. **False-negative attack.** A clean ontology hides stale evidence, authority conflicts, inaccessible sources, or projection loss. Surface coherence is insufficient.
6. **Interest-metaphor overreach.** Future cost is assumed to compound like finance. "Interest" requires a declared cost model, time horizon, dependency graph, and observation method.
7. **Ownership laundering.** A debt record assigns blame without reconstructing authority, constraints, or historical context. Custody and causal responsibility remain separate.
8. **AI-cleanup attack.** Generated harmonization silently replaces authored distinctions. AI suggestions remain proposals with provenance, diffs, reversibility, and author review.

### Claim and evidence ceiling

The paper contributes a semantic-debt taxonomy, detection agenda, and relation to governed meaning. It does not establish a universal ontology, objective project ranking, causal link to failure, or validated economic cost. Automated detection yields leads, not adjudicated debt.

Claims about prevalence, cost, productivity, incident risk, machine learning, or organizational outcomes require external evidence and measured studies. Internal corpus examples demonstrate applicability inside this architecture only. No external research was added in this pass.

### Reader-facing consequence

The public test is whether a future maintainer or agent can recover what a system's important terms and decisions mean, why they have standing, where they conflict, and how they may be revised without reconstructing the answer from accidents.

## 20. Publication Standing and Evidence Limits

### 20.1 Current Standing

This candidate presents a developed conceptual ontology, diagnostic matrix, governing-artifact mapping, agentic failure taxonomy, formal sketch, GMB integration, and research program. It does not present an empirical validation of completeness, inter-rater reliability, predictive power, detector accuracy, repayment effectiveness, or semantic-debt interest.

The external bibliography is retained from the author source but was not externally revalidated in this closed-corpus pass. References dated 2026, web resources, DOI metadata, quotations, priority claims, and characterizations of adjacent literature require primary-source verification for a future evidence-qualified revision readiness. No novelty claim should exceed that later review.

PDF rendering remains deferred until textual and semantic saturation. The authorized baseline is ordinary Pandoc mode:

```text
pandoc INPUT.md -o OUTPUT.pdf
```

### 20.3 Corpus Sources

- Adam Ableman, *Semantic Debt*. Exact author source SHA-256  
`36BAE578CF1926981488982AB8C406E0EACB662E25E8B5F18F187A6E53AF933F`.
- Adam Ableman, *Reasoning by Way of Receipts*. Exact reviewed source SHA-256  
`8D884B96597EA6303A324173A7CE2D8C735A952E91FBE4C9EB6509FA6D6B195F`.
- Adam Ableman, *A Formal Theory of Work Custody*. Exact reviewed source SHA-256  
`49C38F60B95E107F8B3D864ACAFB4C49067A146C807E5248307DE7B009AD4696`.
- Adam Ableman, *Admissibility Engineering*. Exact reviewed source SHA-256  
`FA80D5895A569839958193735B754BE62EE20E1B399A06CB3BA959614DEBF7A3`.
- Adam Ableman, *Semantic Legitimacy Before Context*. Exact reviewed source SHA-256  
`1E9058F212FCB00E42E35E927DF2E7F830BC9C9499AAFF469FE65FF8AE137B68`.
- Adam Ableman, *The Three Hash Rule*. Zenodo, 2026. DOI:   
  `10.5281/zenodo.20788617`; exact reviewed source SHA-256  
`03F60317CC9AFB36DDBCF9BF1C6D185611666CC4D9AB290BD4BCC17DF4579B7C`.
- Governed Meaning Base terminology ruling: `CCF -> CMB -> GMB`, with GMB current. This establishes terminology lineage only.

The title correction, GMB/RPZ integration, corpus relations, realization-funnel placement, formal extensions, counterexamples, claim ceilings, and decision surface are AI-prepared editorial synthesis explicitly distinguished from the original author material. They grant no author, publication, canonical, identity, implementation, or conformance standing.

## 21. Conclusion

Semantic debt is the debt of meaning that can no longer be safely recovered.

It appears when terms drift, categories collapse, boundaries leak, procedures go unrecorded, evidence becomes inadmissible, authority hides, and claims outrun support. It is not merely poor documentation, nor merely technical debt under another name. It is the accumulated future cost of unstable meaning.

The ontology proposed here separates semantic debt into seven subdomains: lexical, ontological, boundary, procedural, evidentiary, authority, and claim debt. It also identifies nine cross-cutting modes: underdefinition, contradiction, fragmentation, staleness, opacity, overcoupling, inadmissibility, overclaim, and lossy translation. This two-axis model clarifies why semantic fragmentation is not a peer subdomain but an orthogonal distribution failure. The more precise subtype originally motivating the framework is semantic locality debt: the loss of stable homes for meaningful distinctions.

The matrix is the paper's central instrument. It turns semantic debt into a coordinate system. The governing artifacts then turn that coordinate system into practice: glossary, non-claims file, claim ledger, standing graph, migration contract, receipt schema, and semantic debt ledger.

The result is a proposed governance model. Semantic debt can be recorded, classified, prioritized, checked, repaid, and blocked from supporting claims when a concrete profile defines its obligations, thresholds, evidence, and authority. It can become part of admission, refactor, migration, corpus-integration, GMB, and agent-development workflows, but its benefit remains an empirical question.

Semantic debt names the cost of unrecoverable meaning. Constitutional Semantic Engineering offers one path for refusing it before it compounds.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm2.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Instance Configuration.** The present paper does not claim a complete instance configuration treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that software systems do not only accumulate technical debt. Its nearest external comparison fields are software, semantic, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Modularity, secure-development practice, and reproducibility reduce classes of failure but do not guarantee architectural coherence or user sovereignty. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** David L. Parnas. "On the Criteria To Be Used in Decomposing Systems into Modules." *Communications of the ACM* 15(12), 1972, pp. 1053-1058. DOI: 10.1145/361598.361623. https://doi.org/10.1145/361598.361623 **Relationship:** Foundational modularity treatment used to compare information hiding with explicit semantic and governance interfaces.

**[E2]** Ward Cunningham. "The WyCash Portfolio Management System." *OOPSLA '92 Experience Report*, 1992. DOI: 10.1145/157709.157715. https://doi.org/10.1145/157709.157715 **Relationship:** Original technical-debt metaphor used to distinguish implementation debt from semantic debt.

**[E3]** Karen Scarfone, Murugiah Souppaya, and Donna Dodson. *Secure Software Development Framework (SSDF) Version 1.1*. NIST SP 800-218, 2022. DOI: 10.6028/NIST.SP.800-218. https://doi.org/10.6028/NIST.SP.800-218 **Relationship:** Adjacent secure-development framework for preparation, protection, production, and vulnerability response.

**[E4]** Reproducible Builds Project. *Formal Definition of Reproducible Builds*. [reproducible-builds.org source](https://reproducible-builds.org/docs/formal-definition/) **Relationship:** Adjacent reproducibility practice; byte reproduction is compared with, but not equated to, semantic or constitutional continuity.

**[E5]** Richard Cyganiak, David Wood, and Markus Lanthaler, eds. *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation, 25 February 2014. https://www.w3.org/TR/rdf11-concepts/ **Relationship:** Adjacent graph data model and identity baseline.

**[E6]** Alistair Miles and Sean Bechhofer, eds. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. https://www.w3.org/TR/skos-reference **Relationship:** Adjacent standard for concepts, labels, schemes, notes, and semantic mappings.

**[E7]** W3C OWL Working Group. *OWL 2 Web Ontology Language Document Overview*, Second Edition. W3C Recommendation, 11 December 2012. https://www.w3.org/TR/owl2-overview/ **Relationship:** Adjacent formal ontology standard used to compare declared semantics and inference commitments.

### Ableman corpus

**[A1]** Adam Ableman. *Sovereign Software*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-24C6159B98023A9C`;  
source SHA-256  
`6AAFE79E438B980B75D1910A897F7BA716A10CF1187B68CB1F71405F36725A18`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Software Analysis (CSoftA): A Governance-Based Classification Method for Software Systems*. Ableman Corpus current edition; work identity `PAPER.PUB.20472196`;  
source SHA-256  
`3670B28B7C1AF5467BE4002C47B5F964F8FAF6F257125C2F84CE06904E4FD0DE`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Semantic Fragmentation and Constitutional Structure in Software Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-B307F65B51C503DE`;  
source SHA-256  
`9D2A9D79DE8BC3F2F8ABECA073E4D3607F7623F4368E63F8036081E39B4C75C3`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Governed Coding and Debugging*. Ableman Corpus current edition; work identity `PAPER.PUB.18115533`;  
source SHA-256  
`2469EDA96DBC1E207855A9AD27314A7FAB59FA35E6EFEF9288C30F949376BF16`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Constitutional Operating Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F5FB8FA82270B989`;  
source SHA-256  
`E982E4D6BD4B519EED6A7438367844954D6D5F1C2C4CC0099AAAC4AB9A00D3AB`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Meaning as Binding*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-5F976917F0B283EA`;  
source SHA-256  
`A470D1A0B9ED7C3CEAB6BB88BE4B642A2BA36427447F787764329FD574DA0C97`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D95CCC4FB7B58BFB`;  
source SHA-256  
`A3B62E50F8BEE125FDAE0D38C2839AFD1CCC138296268BF93217481E38AA48EA`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

The following bibliography is retained from the author source. It was not externally revalidated during this closed-corpus pass.

Avgeriou, P., Ozkaya, I., Chatzigeorgiou, A., Ciolkowski, M., Ernst, N. A., Koontz, R. J., Poort, E., and Shull, F. (2024). Technical Debt Management: The Road Ahead for Successful Software Delivery. arXiv. https://arxiv.org/abs/2403.06484

Cockburn, A. (2005). Hexagonal Architecture: The Original 2005 Article. HaT Technical Report 2005.02. https://alistair.cockburn.us/hexagonal-architecture

Dorval, G. (2026). Semantic Debt: Canonical Definition. [gautierdorval.com source](https://gautierdorval.com/en/definitions/semantic-debt/)

Evans, E. (2003). Domain-Driven Design: Tackling Complexity in the Heart of Software. Addison-Wesley Professional.

Jansen, A. G. J. (2008). Architectural Design Decisions. University of Groningen doctoral thesis. [research.rug.nl source](https://research.rug.nl/en/publications/architectural-design-decisions)

Kruchten, P., Nord, R. L., and Ozkaya, I. (2012). Technical Debt: From Metaphor to Theory and Practice. IEEE Software, 29(6), 18-21. DOI: 10.1109/MS.2012.167.

Lebo, T., Sahoo, S., McGuinness, D., Belhajjame, K., Cheney, J., Corsar, D., Garijo, D., Soiland-Reyes, S., Zednik, S., and Zhao, J. (2013). PROV-O: The PROV Ontology. W3C Recommendation. https://www.w3.org/TR/prov-o/

Miller, M. S., Yee, K. P., and Shapiro, J. S. (2003). Capability Myths Demolished. Systems Research Laboratory, Johns Hopkins University. [papers.agoric.com source](https://papers.agoric.com/papers/capability-myths-demolished/full-text/)

Nogueira, F., Silva, N., and Conte, T. (2026). One Size Fits All? An Empirical Comparison of ADR Templates regarding Comprehension, Usability, and Ease of Adoption. arXiv. https://arxiv.org/abs/2604.27333

Ozkan, O., Babur, O., and van den Brand, M. (2023). Domain-Driven Design in Software Development: A Systematic Literature Review on Implementation, Challenges, and Effectiveness. arXiv. https://arxiv.org/abs/2310.01905

Parnas, D. L. (1972). On the Criteria to Be Used in Decomposing Systems into Modules. Communications of the ACM, 15(12), 1053-1058. DOI: 10.1145/361598.361623.

Rios, N., Ribeiro, L. F., Caires, V., Mendes, T., and Spindola, R. O. (2014). Towards an Ontology of Terms on Technical Debt. IEEE International Workshop on Managing Technical Debt. DOI: 10.1109/MTD.2014.9.

Sharma, R. K. (2026). ContextCov: Deriving and Enforcing Executable Constraints from Agent Instruction Files. arXiv. https://arxiv.org/abs/2603.00822

Tofan, D. (2015). Understanding and Supporting Software Architectural Decisions: For Reducing Architectural Knowledge Vaporization. University of Groningen doctoral thesis. [research.rug.nl source](https://research.rug.nl/en/publications/understanding-and-supporting-software-architectural-decisions-for)

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.21111666](https://doi.org/10.5281/zenodo.21111666)
