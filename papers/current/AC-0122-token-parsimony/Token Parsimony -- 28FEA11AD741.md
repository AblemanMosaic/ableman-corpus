# Token Parsimony

## Toward Semantic Compression Substrates for Evidence-Bearing Artificial Intelligence

### Why Future AI Systems Will Spend Less Time Reading and More Time Remembering

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern large language model systems are operationally inefficient
observers.

Most contemporary agent architectures repeatedly ingest the same
repositories, logs, transcripts, filesystems, and execution traces
across reasoning cycles, reconstructing situational awareness from raw
substrate exposure instead of preserving compact semantic continuity. As
systems scale, the overwhelming majority of token expenditure shifts
away from reasoning itself and toward repeated reacquisition of
already-known operational state.

Under hyperscale deployment conditions, redundant substrate reacquisition becomes a primary infrastructure burden. Token parsimony reduces not only inference expenditure, but also the upstream transport, synchronization, hydration, and storage costs associated with repeated semantic reconstruction. The result is reduced semantic input bloat across distributed inference substrates and data-center-scale orchestration systems — in practical terms, more computationally efficient AI infrastructure.

This paper introduces **Token Parsimony** as a formal architectural
principle for semantic systems. Token parsimony is the disciplined
minimization of substrate exposure while preserving replay-relevant
semantic continuity, inferential sufficiency, and governance integrity.

We argue that the dominant inefficiency in current agent systems is not
model inference itself, but repeated semantic reacquisition through raw
token consumption. Governed semantic receipts, compact operational
summaries, inferentially sufficient transition artifacts, and
replay-oriented semantic state transitions can dramatically reduce
operational token expenditure while simultaneously increasing
auditability, replayability, and epistemic continuity.

Rather than treating tokens as disposable context bandwidth, token
parsimony treats them as a constrained thermodynamic resource within
semantic reactors. Under this framing, raw output flooding becomes
analogous to energy dissipation in physical systems: computationally
expensive, destabilizing, and semantically redundant.

The paper further argues that token parsimony naturally favors
constitutional semantic architectures. Systems capable of compact
semantic continuity require governed state transitions, semantic
custody, replayable operational lineage, and substrate-aware closure
guarantees. This leads toward a new class of systems in which agents
reason primarily from semantic state transitions rather than repeated
raw substrate observation.

The result is a shift from *context accumulation* toward *semantic
continuity engineering*.

## 1. Introduction

The dominant operational pattern in modern AI systems is profoundly
wasteful.

An agent receives a task. It searches a repository. It loads files. It
scans logs. It reconstructs operational state. Then, in the next
session, another agent performs nearly the same sequence again. The
substrate may have changed only minimally, but the semantic acquisition
process effectively restarts from zero.

As repositories, operational corpora and histories grow, token
expenditure increasingly shifts away from reasoning itself and toward
repeated reacquisition of already-known substrate state. Systems
repeatedly pay the observational cost of rebuilding situational
awareness.

The problem is not merely economic.

Repeated raw observation produces:

- context flooding,
- replay instability,
- epistemic drift,
- semantic inconsistency,
- audit discontinuity,
- hallucination opportunities,
- and degraded operational coherence.

Current architectures implicitly assume that intelligence consists
primarily of repeatedly observing raw substrate.

This paper argues the opposite.

Scalable intelligence increasingly depends upon preserving compact
semantic continuity across operations while minimizing repeated
substrate exposure.

This principle is termed **Token Parsimony**.

## 2. Formal Model

Token parsimony can be described using a minimal operational formalism.

Let:

- $S_t$ denote substrate state at time $t$
- $O(S_t)$ denote raw substrate observation
- $R_t$ denote a semantic receipt
- $T$ denote a semantic transition operator
- $C(x)$ denote token cost of representation $x$

Let:

$$S_t^{\mathcal{Q}} \subseteq S_t$$

represent the minimal substrate subset required for task class
$\mathcal{Q}$.

Define:

$$T : (S_{t-1}, S_t) \rightarrow R_t$$

The transition operator $T$ encodes both the state mutation and its
receipt projection.

Receipt generation must be deterministic with respect to declared
normalization, environment, and capture semantics.

A semantic receipt is therefore defined as:

$$R_t = T(S_{t-1}, S_t)$$

A receipt is valid iff it preserves inferential sufficiency over
$S_t^{\mathcal{Q}}$.

Define the Parsimony Ratio:

$$P = \frac{
\sum_{i=1}^{n} C(O(S_i))
}{
\sum_{i=1}^{n} C(R_i)
}$$

where:

- numerator = cumulative token cost of raw substrate observation,
- denominator = cumulative token cost of semantic continuity artifacts.

Parsimony is meaningful over operational horizons rather than single
transitions.

A parsimonious system therefore seeks to maximize $P$ subject to
inferential sufficiency and bounded escalation constraints.

The objective is not arbitrary compression, but preservation of
operationally necessary meaning with minimal substrate exposure.

## 3. Inferential Sufficiency

The central operational question of token parsimony is:

> "What is the minimum semantic artifact required to preserve future
> inferential validity?"

This leads to the concept of **inferential sufficiency**.

Let:

$$Answer(q \mid x)$$

denote the system's output for task $q$ given representation $x$,
including decisions, generated artifacts, or execution outcomes.

A receipt $R$ is inferentially sufficient for task class $\mathcal{Q}$
iff:

$$\forall q \in \mathcal{Q}, \quad
Answer(q \mid R) = Answer(q \mid S)$$

or triggers bounded escalation.

Equality may be exact or defined over a task-specific equivalence class
(e.g., identical decisions, outputs, or bounded divergence).

Bounded escalation means:

- the system detects insufficiency,
- selectively reacquires substrate,
- and limits additional token expenditure to a bounded retrieval scope.

Formally:

$$C(\text{escalation}) \le
\epsilon \cdot C(O(S_t))$$

for some policy-defined:

$$\epsilon \in (0,1]$$

Escalation policies therefore constrain worst-case token reacquisition
relative to full substrate observation.

Escalation retrieves additional portions of $S_t$ not present in the
current representation when required for $\mathcal{Q}$.

Token parsimony does not eliminate substrate access.

It governs escalation.

The retrieval hierarchy becomes:

1.  semantic receipt,
2.  compact operational summary,
3.  structured fetch,
4.  partial substrate exposure,
5.  full substrate exposure.

Most current systems default immediately to level 5.

Parsimonious systems attempt to remain at the lowest admissible level.

## 4. Receipts as Semantic State Transitions

The central insight of token parsimony is that most operations do not
require reproduction of raw output.

They require preservation of semantic state transitions.

For example, a conventional write operation may emit:

- the full file,
- surrounding context,
- timestamps,
- path metadata,
- and verbose explanation.

A parsimonious system instead emits:

`write:engine.py:hashA->hashB:+14/-2`

This compact representation preserves:

- object identity,
- mutation direction,
- mutation magnitude,
- replay relevance,
- and continuity lineage (the chain of receipts linking prior and
  current state).

Similarly:

`run:smoke_test:exit0:stdout_`

`hash manifest:src:241files:manifest_`  
`hash audit:98receipts:0open:3warnings`

These are not merely compressed outputs.

They are governed semantic transition vectors.

## 5. Receipt Taxonomy

Receipts naturally partition into distinct operational classes.

### 5.1 State Receipts

Represent substrate snapshots or continuity anchors.

Examples:

- manifests,
- directory snapshots,
- inventory hashes.

### 5.2 Transition Receipts

Represent substrate mutations.

Examples:

- writes,
- diffs,
- merges,
- state transitions.

### 5.3 Execution Receipts

Represent runtime operations.

Examples:

- command execution,
- exit codes,
- stdout hashes,
- elapsed time.

### 5.4 Claim Receipts

Represent semantic assertions bound to evidence.

Examples:

- audits,
- investigations,
- governed claims,
- refutations.

This taxonomy becomes increasingly important as systems transition from
observational architectures toward semantic operating environments.

## 6. End-to-End Example

Consider a conventional CI pipeline.

A standard agentic workflow may repeatedly:

- scan the repository,
- load changed files,
- read full build logs,
- inspect test outputs,
- and reconstruct prior operational state.

Suppose:

- repository size = 40 MB,
- build log = 300k tokens,
- test output = 80k tokens,
- repeated across multiple agents.

Operational token cost rapidly becomes enormous.

A parsimonious pipeline instead operates primarily through receipts.

### Step 1 --- Repository Continuity

Instead of rescanning the repository:

`manifest:src:241files:manifest_hash`

If unchanged, no escalation occurs.

### Step 2 --- Build Execution

Instead of ingesting full logs:

`run:build:exit0:stdout_hash`

Only failures trigger escalation.

### Step 3 --- Test Verification

`run:test_suite:exit1:stdout_hash`

Only the failing test shard is fetched during escalation (e.g., 2k
tokens instead of 80k total output).

### Step 4 --- Drift Analysis

`write:parser.py:hashA->hashB:+6/-1`

Agents infer likely affected systems without reacquiring unrelated
substrate.

The result is a receipt-dominant execution regime in which substrate
exposure becomes selective rather than default.

Preliminary architectural analysis suggests reductions on the order of
1--3 magnitudes under receipt-dominant operational patterns.

## 7. Hash Semantics

Token parsimony relies heavily on compact identity primitives such as
hashes.

However, hashes require careful semantic framing.

A hash is not evidence.

A hash is a governed pointer to evidence.

Systems must explicitly define:

- what is hashed,
- normalization rules,
- collision assumptions,
- environmental stability guarantees,
- and capture semantics.

Examples include:

- raw content hashes,
- normalized AST hashes,
- execution trace hashes,
- or manifest hashes.

The following invariant must hold:

$$hash(x) = hash(y) \Rightarrow x \equiv y$$

under the declared normalization regime.

Equivalence is therefore defined by the hashing regime rather than raw
byte identity.

Execution hashes additionally require declared capture semantics:

- full stdout,
- filtered output,
- deterministic projections,
- environment normalization,
- and ordering guarantees.

Adversarial or mis-specified hashing regimes can produce false
equivalence; governance must therefore bind hashes to declared
construction procedures.

Failure to define hashing semantics creates false continuity risks.

Two receipts with identical hashes imply continuity only within the
declared hashing jurisdiction.

## 8. The Thermodynamics of Context

Current AI systems behave thermodynamically poorly.

They repeatedly dissipate computational energy through redundant
substrate observation.

Within the token parsimony model:

- energy corresponds to token expenditure,
- entropy corresponds to semantic uncertainty or loss,
- dissipation corresponds to redundant reacquisition of already-known
  substrate.

Large context windows partially mask this inefficiency but do not solve
it. Increasing context merely enlarges the reactor chamber while
preserving inefficient operational physics.

Under token parsimony:

- receipts replace repeated file reads,
- semantic transitions replace repeated state reconstruction,
- governed hashes replace repeated payload transmission,
- and inferential references replace observational flooding.

The shift resembles the emergence of symbolic accounting systems within
human civilization: compact semantic structures replace repeated
physical enumeration.

## 9. Governance and Semantic Closure

Token parsimony cannot operate reliably without governance.

A compact receipt is only useful if its semantic continuity is trusted.

This creates a direct dependency between:

- token parsimony,
- semantic custody,
- replay integrity,
- governance closure,
- and constitutional continuity.

A receipt lacking:

- provenance,
- admissibility,
- operational lineage,
- or replay guarantees

cannot safely replace substrate observation.

Receipts are assumed to reside in a durable, queryable store with
append-only or governed mutation semantics.

Receipt stores must preserve ordering or causal linkage sufficient to
reconstruct transition lineage.

Thus semantically parsimonious systems naturally favor governed semantic
architectures.

As semantic artifacts become smaller, the operational meaning carried by
each artifact increases dramatically.

This creates governance-compressed semantic state: small symbolic
structures carrying disproportionately large operational authority.

## 10. Failure Modes

Token parsimony introduces new architectural risks.

These include:

- semantic oversummarization,
- inferential insufficiency,
- phantom continuity,
- governance spoofing,
- substrate drift,
- and illegitimate semantic condensation.

Consider a failure example.

A manifest receipt reports:

`manifest:src:241files:manifest_hash`

A hidden deployment artifact was excluded from the hashing scope due to
a configuration bug.

Future reasoning assumes repository continuity and deploys stale
infrastructure.

The failure was not cryptographic.

It was semantic.

The continuity claim exceeded the actual hashing jurisdiction.

This illustrates a central principle:

> Semantic continuity claims are bounded by declared substrate scope.

Governance systems must therefore validate:

- receipt completeness,
- hashing jurisdiction,
- escalation correctness,
- continuity admissibility,
- and inferential scope.

## 11. Escalation Policy

Token parsimony depends upon governed escalation.

Receipts are not universally trusted. They are conditionally sufficient.

An escalation policy determines:

- when semantic continuity is insufficient,
- which retrieval layer to escalate toward,
- maximum allowable escalation cost,
- replay admissibility requirements,
- and recovery behavior.

Upon escalation failure, systems may invalidate dependent receipts and
revert to a higher observation tier.

Escalation transforms token parsimony from blind compression into
adaptive semantic governance.

Without escalation policy, parsimonious systems become brittle.

With governed escalation, they become operationally scalable.

## 12. Substrate Liveness

A governance-complete semantic system can still fail operationally if
its substrate loses liveness.

This paper defines **substrate liveness** as the operational viability
of the substrate required to sustain semantic state transitions.

Examples include:

- lock contention,
- stalled subprocesses,
- deadlocked receipt stores,
- WAL starvation,
- exhausted descriptors,
- and recursive governance contention.

Substrate liveness is orthogonal to semantic legitimacy.

A constitutionally valid system may still become operationally frozen.

This becomes especially important in recursive governance systems where:

- audit systems audit themselves,
- receipt stores recursively inspect receipts,
- and governance substrates recursively govern their own continuity.

Semantic reactors therefore require not only constitutional legitimacy,
but operational thermodynamics.

## 13. Toward Semantic Operating Systems

Token parsimony ultimately implies a new class of operating environment.

Conventional systems are:

- process-centric,
- file-centric,
- or message-centric.

Semantically parsimonious systems become:

- transition-centric,
- receipt-centric,
- and continuity-centric.

Meaning increasingly resides not in repeated substrate exposure, but in
governed semantic transitions.

Agents stop repeatedly rediscovering operational state and instead
inherit compact semantic continuity through replayable receipt
structures.

This transforms semantic systems from observational machines into
continuity-preserving semantic civilizations.

These properties suggest a minimal execution model in which agents
operate over receipt graphs rather than raw substrate.

## 14. Conclusion

The future scalability limits of AI systems are unlikely to emerge
primarily from model intelligence.

They are more likely to emerge from semantic inefficiency.

Current architectures repeatedly spend enormous computational resources
reacquiring operational state that could instead persist as governed
semantic continuity.

Token parsimony reframes the problem fundamentally.

The question is no longer:

> "How large can context windows become?"

but:

> "How little substrate exposure is actually necessary?"

This inversion changes the architecture of intelligent systems
profoundly.

It favors:

- semantic continuity,
- inferential sufficiency,
- governance closure,
- replayable operations,
- compact semantic transitions,
- and substrate-aware escalation.

In such systems, intelligence increasingly shifts away from repeated
observation and toward continuity-preserving semantic operation.

The result is not merely cheaper computation.

It is the emergence of systems capable of reasoning through governed
semantic continuity rather than repeated reacquisition of already-known
state.

## Corpus-Wide Reference Positioning

This paper argues that modern large language model systems are operationally inefficient observers. Its nearest external comparison fields are token, semantic, ai. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Statistical compression can improve efficiency while destroying distinctions needed for interpretation; semantic labels can conversely overstate stability that usage does not support. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Rico Sennrich, Barry Haddow, and Alexandra Birch. "Neural Machine Translation of Rare Words with Subword Units." *ACL 2016*, pp. 1715-1725. DOI: 10.18653/v1/P16-1162. https://doi.org/10.18653/v1/P16-1162 **Relationship:** Predecessor subword tokenization method used as a contrast to semantically governed token boundaries.

**[E2]** Taku Kudo and John Richardson. "SentencePiece: A Simple and Language Independent Subword Tokenizer and Detokenizer for Neural Text Processing." *EMNLP 2018: System Demonstrations*. DOI: 10.18653/v1/D18-2012. https://doi.org/10.18653/v1/D18-2012 **Relationship:** Predecessor tokenizer implementation used to separate statistical segmentation from semantic admissibility.

**[E3]** Peter D. Grunwald. *The Minimum Description Length Principle*. MIT Press, 2007. [mitpress.mit.edu source](https://mitpress.mit.edu/9780262072816/the-minimum-description-length-principle/) **Relationship:** Predecessor theory of compression and model selection; compression is not assumed to preserve governance or meaning.

**[E4]** Alistair Miles and Sean Bechhofer, eds. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. https://www.w3.org/TR/skos-reference **Relationship:** Adjacent standard for concepts, labels, schemes, notes, and semantic mappings.

**[E5]** Richard Cyganiak, David Wood, and Markus Lanthaler, eds. *RDF 1.1 Concepts and Abstract Syntax*. W3C Recommendation, 25 February 2014. https://www.w3.org/TR/rdf11-concepts/ **Relationship:** Adjacent graph data model and identity baseline.

**[E6]** W3C OWL Working Group. *OWL 2 Web Ontology Language Document Overview*, Second Edition. W3C Recommendation, 11 December 2012. https://www.w3.org/TR/owl2-overview/ **Relationship:** Adjacent formal ontology standard used to compare declared semantics and inference commitments.

**[E7]** Mark D. Wilkinson et al. "The FAIR Guiding Principles for Scientific Data Management and Stewardship." *Scientific Data* 3, 2016, 160018. DOI: 10.1038/sdata.2016.18. https://doi.org/10.1038/sdata.2016.18 **Relationship:** Predecessor stewardship principles for findability, accessibility, interoperability, and reuse.

### Ableman corpus

**[A1]** Adam Ableman. *Governed Semantic Tokens: Tokenization as an Admissibility Boundary*. Ableman Corpus current edition; work identity `PAPER.PUB.18469507`;  
source SHA-256  
`5C44175B87C514892A0DC9743E09D03893E970AF5419F2E6D9171651BE2A9A54`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Legends*. Ableman Corpus current edition; work identity `PAPER.PUB.20330324`;  
source SHA-256  
`440CE8A83C2F86C020D1E9E482759F71D08F694F1C2250B5B624AEA0A4237AA7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Governed Controlled Natural Language (GCNL)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-99C179FB694070D1`;  
source SHA-256  
`75A4AE13167785A0761E1F9CB67A9975138166A7B2B06B4FDF37C1A895178193`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Global Term Key: Identity Primitives in Governed Knowledge Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-358AC09F5A13587E`;  
source SHA-256  
`AFB29CFCB4B58A78B79709AD453CEE9088CCB2AE40F30A70260F1B54F5160579`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Meaning as Binding*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-5F976917F0B283EA`;  
source SHA-256  
`A470D1A0B9ED7C3CEAB6BB88BE4B642A2BA36427447F787764329FD574DA0C97`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Governed Meaning Base (GMB)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D95CCC4FB7B58BFB`;  
source SHA-256  
`A3B62E50F8BEE125FDAE0D38C2839AFD1CCC138296268BF93217481E38AA48EA`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Semantic Manifold Topology*. Ableman Corpus current edition; work identity `PAPER.PUB.20257244`;  
source SHA-256  
`B8F28CC652A73A3EE4CF6FD0E23C1ABC922A6660319B2FB4CC1CCAAA606EC64A`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20382825](https://doi.org/10.5281/zenodo.20382825)
