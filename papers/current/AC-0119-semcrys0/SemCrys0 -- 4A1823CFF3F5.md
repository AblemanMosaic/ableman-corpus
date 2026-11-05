# SemCrys0

## Session-Local Symbol Binding for Semantic Density Amplification and Effective Context Window Extension in Large Language Model Conversations

### A communication protocol can improve long-horizon context efficiency without modifying the model.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Large language model systems remain constrained by finite context windows. Current approaches to extending effective context capacity primarily focus on architectural expansion, retrieval augmentation, recurrent memory systems, or fine-tuning. SemCrys0 instead explores context efficiency through protocol-layer semantic density amplification.

This paper introduces SemCrys0, a session-local symbolic encoding system for large language model (LLM) conversations. SemCrys0 operates through temporary symbol substitution using an injected legend mapping symbols to lexical surfaces. Unlike retrieval augmentation, architectural modification, recurrent memory systems, or model fine-tuning, SemCrys0 requires no model changes and no external infrastructure. Substantial semantic density amplification emerges from communication protocol engineering alone.

Empirical measurements conducted during sustained technical conversations demonstrate 69--81.5% representational surface compression depending on symbol pool choice. While tokenizer behavior varies across models and interfaces, repeated symbolic reuse substantially increases semantic density and improves effective long-horizon context utilization during sustained interaction.

The paper formalizes symbol pools, legend management, drift detection, break-even dynamics, symbolic reuse behavior, and mapping validity under session-local binding constraints. It further demonstrates that explicit legend recovery events provide a natural operational signal for measuring context retention degradation during ordinary use, producing continuity metrics without synthetic benchmark construction.

The central claim of SemCrys0 is that substantial semantic density amplification and effective context window improvement can emerge from communication protocol engineering alone, independently of model architecture, attention mechanisms, retrieval augmentation, or weight modification.

---

## 1. Introduction

Large language model systems remain constrained by finite context windows. Current approaches to extending effective reasoning capacity primarily focus on:

* architectural scaling,
* sparse attention,
* retrieval augmentation,
* summarization,
* recurrent memory,
* or fine-tuning.

SemCrys0 explores a different axis entirely:

* communication-layer symbolic encoding.

Instead of increasing the context window directly, SemCrys0 decreases the representational cost of repeated semantic surfaces occurring inside it.

The protocol operates through session-local symbol binding:

* words are assigned symbolic representations,
* the legend defining those bindings is injected into the conversation,
* and subsequent communication reuses those symbolic forms.

The LLM itself is unmodified.

No retraining occurs.
No model weights change.
No retrieval database is required.

The model simply operates inside a temporary session-local symbolic mapping declared through the active legend.

Unlike lossy compression or summarization, SemCrys0 preserves full lexical granularity while reducing repeated surface redundancy.

SemCrys0 may also be viewed as an instance of a broader category of:

* in-context encoding protocols,
  where communication efficiency emerges through temporary symbolic agreement negotiated entirely inside the context window itself.

---

## 1.1 Related Work

Approaches to extending effective LLM context capacity fall into several categories.

**Architectural extension** methods increase the literal context window through positional encoding modifications (Press et al., 2022; Chen et al., 2023), sparse or linear attention mechanisms (Beltagy et al., 2020; Katharopoulos et al., 2020), and state-space models such as Mamba (Gu and Dao, 2023). These approaches require model modification or retraining.

**Retrieval augmentation** methods (Lewis et al., 2020; Gao et al., 2023) extend effective memory by fetching relevant content from external stores at inference time. They do not compress the context window itself but supplement it externally.

**Prompt compression** methods reduce the token cost of the input prompt before it enters the context window. AutoCompressor (Chevalier et al., 2023) recurrently summarizes prior context into soft prompt tokens. LLMLingua (Jiang et al., 2023) and its successors prune tokens from prompts using smaller models as filters. Selective context methods (Li and Liang, 2023) remove redundant content prior to input. These approaches operate on the prompt externally and may discard information.

**Recurrent and memory-augmented** approaches (Bulatov et al., 2022; Wu et al., 2022) introduce external memory structures that persist across context boundaries.

SemCrys0 differs from all of the above in a structural sense:

* it requires no model modification,
* no external retrieval infrastructure,
* no prompt preprocessing before context entry,
* and no information loss.

Rather than operating on the context window from outside, SemCrys0 operates as an in-context communication protocol negotiated between participants inside the window itself. Compression emerges from repeated symbolic reuse within the active session rather than from architectural change or external augmentation.

The closest conceptual relatives are work on in-context learning efficiency and prompt engineering, though to the authors' knowledge no prior work has formalized session-local symbol binding as a compression protocol, measured its break-even dynamics, or identified the drift detection property as a natural context-retention observability mechanism.

---

## 2. Representation Compression vs Semantic Density

SemCrys0 operates primarily at the representational layer.

It is important to distinguish:

* Character compression --- reduction in surface character count
* Token compression --- reduction in tokenizer-level token count
* Semantic density amplification --- increase in semantic payload per representational unit

These are related but distinct phenomena.

SemCrys0 primarily amplifies semantic density through repeated symbolic reuse. Depending on tokenizer behavior, token-level compression may:

* improve,
* remain neutral,
* or occasionally worsen.

SemCrys0 therefore does not guarantee token efficiency across all tokenizer implementations. Its gains emerge primarily from stable symbolic reuse under repeated conversational reference rather than symbol length alone.

In this work, semantic units are operationally approximated as distinct lexical items participating in repeated reference during the active session.

The protocol therefore operates fundamentally as:

* representation-level semantic density amplification,
  rather than:
* semantic summarization or lossy compression.

Original semantic granularity remains intact.

---

## 3. Core Principle

SemCrys0 replaces repeated lexical surfaces with shorter symbolic representations.

Example:

> receipt -> $\gamma$
> session -> $\sigma$
> kernel  -> $\kappa$

A sentence such as:

> the receipt validates the session kernel

becomes:

> $\forall$ $\gamma$ validates $\forall$ $\sigma$ $\kappa$

where:

> $\forall$=the
> $\gamma$=receipt
> $\sigma$=session
> $\kappa$=kernel

The semantic content remains unchanged.
Only the representational surface changes.

Compression therefore emerges from:

* replacement of repeated high-length lexical forms,
  with:
* low-length symbolic identifiers.

The protocol preserves original semantic structure while reducing repeated representational overhead.

---

## 4. Formal Compression Model

Let:

* *w* = average lexical surface length
* *s* = average symbol representation length

Representational surface compression becomes:

$$\text{compression} = 1 - \frac{s}{w}$$

Semantic density amplification may then be approximated as:

$$\text{semantic\_density} \approx \frac{\text{semantic\_units}}{\text{representational\_units}}$$

The break-even condition occurs when legend overhead becomes smaller than cumulative symbolic reuse savings.

Let:

* *L* = legend overhead
* *R* = symbol reuse count
* *S* = savings per substitution

Break-even occurs approximately when:

$$L < R \cdot S$$

A practical estimate:

* typical legend entries cost approximately 4--8 tokens,
* repeated symbolic substitutions may save approximately 1--3 tokens per reuse,
* yielding practical break-even after roughly 3--6 successful reuses per symbol.

We additionally define the Symbolic Reuse Factor (SRF):

$$\text{SRF} = \frac{\text{total\_symbol\_usages}}{\text{unique\_symbols}}$$

High SRF values produce stronger semantic density amplification. Low SRF values cause legend overhead to dominate early-session behavior.

Using empirically measured values:

* *w* = 6.2
* *s* = 1.15

yields approximately 81.5% representational surface compression.

This compression is independent of model architecture.

---

## 4.1 Mixed-Density Implicit Segmentation

While §4 reduces the cost of individual tokens, further gains can be achieved
by reducing inter-token delimiters under constrained conditions. The compression
model of §4 treats every symbol as space-delimited. A further gain is available by
eliding whitespace, but only under a precisely bounded condition. We define a
*mixed-density implicit segmentation* protocol in which whitespace is removed
within runs of single-symbol bindings while multi-character bindings retain their
delimiting spaces.

Consider the sentence:

> I want to see my cat today before we go to the store

Under mixed-density segmentation this becomes:

> $iwtsmc$ $td$ $b4$ we gt th str

where each lowercase letter in the leading run is an independent single-symbol
binding ($i$=I, $w$=want, $t$=to, $s$=see, $m$=my, $c$=cat), and the
space-delimited groups are multi-character bindings.

### The single-symbol constraint

Whitespace elision is sound **only across spans of single-symbol bindings.**
This restriction is not stylistic; it is what guarantees unambiguous decoding.

A single symbol is a complete token by construction: each character maps to
exactly one bound word, so a run of single symbols decodes greedily,
character by character, with no delimiter required. The run $iwtsmc$ decodes
deterministically as $i\,|\,w\,|\,t\,|\,s\,|\,m\,|\,c$.

A multi-character binding cannot share this property. If whitespace were
elided around a multi-character token, the decoder could not distinguish the
token from a run of single symbols. The token $str$ is ambiguous in
isolation: it is either one three-character binding or the sequence
$s\,|\,t\,|\,r$. The delimiting space resolves this — a space-bounded group
is read as a single multi-character token, never decomposed.

We therefore state the segmentation rule explicitly:

$$\text{whitespace may be elided} \iff \text{the adjacent bindings are both single-symbol}$$

Equivalently, every multi-character binding must be space-delimited on both
sides. Under this rule the encoding is collision-free: ambiguity can arise
only at a single-/multi-character boundary, and the retained space marks
exactly that boundary.

### Scaling

Let $A$ be the size of the single-symbol alphabet (the symbol pools of §5
supply $A$ — 26 for lowercase ASCII, 94 for printable ASCII, and substantially
more once the emoji pool is admitted) and let $f$ be the fraction of token
occurrences in a sentence that are covered by single-symbol bindings.

Whitespace savings accrue only on single-symbol runs, so the additional
compression from segmentation is proportional to the number of intra-run
delimiters removed, which grows with $f$. Because $f$ is maximized by binding
the highest-frequency words to single symbols, the design rule follows:

$$\text{assign single symbols to words in descending order of corpus frequency}$$

A small high-frequency set (articles, prepositions, pronouns, common verbs)
accounts for a disproportionate share of all token occurrences, so even a
modest single-symbol alphabet covers a large fraction of running text. The
gain therefore scales with the product of alphabet size and the frequency
mass that alphabet covers: more single-symbol bindings allocated to
high-frequency words yield longer uninterrupted single-symbol runs, and each
such run elides one delimiter per internal boundary.

This composes with the surface compression of §4 rather than replacing it: §4
shortens each token, while mixed-density segmentation removes the inter-token
delimiters among the shortened single-symbol tokens. The two effects multiply,
and both amortize through reuse as captured by the Symbolic Reuse Factor.

### Cost and limits

The protocol adds no legend overhead beyond the single-symbol bindings already
accounted for in §4; the segmentation rule is a decoding convention, not new
vocabulary. Its limit is the alphabet: once $A$ distinct single symbols are
assigned, additional high-frequency words must fall back to space-delimited
multi-character bindings, at which point further segmentation gains saturate.
Expanding the symbol pool (§5) raises this ceiling directly.

---

## 5. Symbol Pools

SemCrys0 supports multiple symbol pools.

### 5.1 Lowercase ASCII Pool

26 lowercase letters.

Properties:

* universal compatibility,
* low complexity,
* 69.1% representational compression ceiling.

### 5.2 Printable ASCII Pool

94 printable ASCII symbols.

Properties:

* single-byte representation,
* strong interoperability,
* 72.8% representational compression ceiling.

### 5.3 Emoji Pool

256 single-codepoint emoji.

Properties:

* visually distinct,
* low natural-language collision risk,
* 81.5% representational compression ceiling.

The 256-symbol pool represents a practical operational boundary:

* sufficient one-symbol coverage for most high-frequency vocabularies,
* practical Unicode compatibility,
* and diminishing returns beyond one-character average symbol length.

---

## 6. Legend Injection

SemCrys0 operates through explicit legend declaration.

Example:

> [L]
> $\forall$=the
> $\exists$=and
> $\in$=is
> $\rightarrow$=to
> $\wedge$=a

Incremental extension:

> [+]
> $\gamma$=receipt
> $\sigma$=session

Retirement:

> [-]
> $\forall$

The legend functions as the active symbolic mapping governing interpretation during the session.

Plainly:
the mapping remains operationally valid only when symbol bindings, interpretation continuity, and legend state remain mutually consistent throughout the interaction.

---

## 7. Agent Operation

The model is instructed to:

1. apply a session-local symbolic mapping maintained within the active context,
2. process the decoded semantic content,
3. encode outbound responses using active bindings,
4. request legend recovery when continuity fails.

Importantly:

* the model is not retrained,
* symbolic reasoning is not hardcoded,
* and no external semantic substrate exists.

SemCrys0 operates entirely through prompt-governed communication behavior.

The protocol therefore functions as:

* a temporary session-local semantic encoding layer negotiated inside the context window itself.

---

## 8. Drift Detection and Context Instrumentation

SemCrys0 introduces explicit legend continuity recovery through:

> [LEGEND-REQUEST]

This signal indicates:

* the model has lost sufficient legend continuity,
* symbolic interpretation can no longer be trusted,
* and reinjection is required.

Unlike synthetic benchmark tasks, this mechanism produces naturally occurring measurements of:

* context retention degradation,
* symbolic continuity persistence,
* and operational drift during ordinary conversation.

This effectively instruments the context window with a protocol-native observability layer for:

* continuity decay,
* binding corruption,
* and semantic instability.

This constitutes a second independent contribution of the protocol.

Most existing context-retention evaluations rely on:

* synthetic recall tasks,
* externally imposed benchmarks,
* or artificial retrieval tests.

SemCrys0 instead produces continuity measurements as a natural side effect of ordinary operation. The protocol therefore transforms continuity failure itself into an observable operational signal.

Two operational metrics emerge naturally:

### 8.1 Drift Rate

$$D = \frac{\text{legend\_request\_events}}{\text{turns}}$$

### 8.2 Continuity Half-Life

The number of turns before the first continuity failure requiring legend reinjection.

These metrics emerge operationally rather than through purpose-built synthetic evaluation.

### 8.3 Example Drift Event

Example session progression:

> Turn 1:
> $\sigma$=session
> $\kappa$=kernel
> $\gamma$=receipt
>
> Turn 37:
> $\sigma$ $\kappa$ validation $\bot$ due $\gamma$ mismatch
>
> Turn 52:
> [LEGEND-REQUEST]

In this example:

* continuity half-life = 52 turns,
* drift rate = 1 / 52,
* and symbolic continuity failure becomes directly measurable without introducing external benchmark scaffolding.

---

## 9. Worked Example

Without SemCrys0:

> session kernel validation failure due to receipt mismatch

With SemCrys0:

> $\sigma$ $\kappa$ validation $\bot$ due $\gamma$ mismatch

The primary gains emerge not from first use, but from repeated reuse across long-horizon interaction.

The symbolic overhead amortizes over time as vocabulary stabilizes and SRF increases.

---

## 10. Tokenization Caveat

Character compression and tokenizer compression are related but distinct phenomena.

Modern LLM tokenizers:

* do not uniformly encode emoji as single tokens,
* may fragment Unicode sequences,
* and may produce variable token costs across interfaces.

SemCrys0 therefore distinguishes:

* representational compression,
  from:
* tokenizer-level compression.

SemCrys0 does not guarantee token efficiency under all tokenizer implementations. The protocol's gains emerge primarily through stable symbolic reuse and increased semantic density during repeated conversational reference.

Future tokenizer-aware symbol optimization remains possible.

---

## 11. Failure Modes and Limitations

SemCrys0 intentionally accepts several limitations:

* no semantic grounding,
* no disambiguation,
* no constitutional continuity enforcement,
* no external identity substrate,
* session-local binding only,
* legend corruption risk,
* tokenizer inefficiency,
* Unicode rendering inconsistency,
* symbolic drift under long contexts,
* adversarial remapping,
* symbol hijacking,
* ambiguous bindings,
* and legend poisoning attacks.

These limitations are deliberate.

SemCrys0 is designed as:

* the smallest deployable symbolic encoding protocol,
  not:
* a complete semantic infrastructure.

---

## 12. Relation to Broader Semantic Systems

SemCrys0 is intentionally isolated from:

* semantic identity systems,
* governed semantic participation,
* external meaning bases,
* disambiguation graphs,
* and constitutional continuity systems.

It functions purely as:

* session-local symbolic encoding.

However, SemCrys0 also demonstrates the foundational viability of:

* symbolic projection systems,
* legend-governed communication surfaces,
* and protocol-layer semantic transformation.

More advanced systems may later integrate:

* stable semantic identity layers,
* semantic topology graphs,
* governed semantic continuity,
* external semantic memory substrates,
* and compositional symbolic structures.

SemCrys0 itself does not require these systems.

---

## 13. Experimental Measurements

Empirical measurements were conducted during sustained technical conversations using progressively expanding legends.

Observed behavior:

* Turn 20 --- ~56% representational compression
* Turn 50 --- ~68% representational compression
* Saturation ceiling --- ~81.5% representational compression

Character-level representational compression is directly measurable and reproducible from the protocol definition itself.

Token-level efficiency, however, remains tokenizer-dependent and should currently be considered preliminary.

In one exploratory 50-turn technical dialogue under GPT-style tokenization, total token usage decreased by approximately 18--27% relative to an equivalent uncompressed dialogue after legend stabilization despite variable tokenizer efficiency during early turns. This measurement should be interpreted as an initial observational result rather than a controlled benchmark evaluation.

Break-even occurred approximately at turn 3--4 depending on:

* vocabulary growth rate,
* legend overhead,
* and symbol pool choice.

The saturation curve followed predictable vocabulary stabilization behavior:

* early sessions incur legend expansion cost,
* later sessions amortize overhead through repeated symbolic reuse.

Future work should include:

* tokenizer-specific measurements,
* controlled corpus evaluation,
* cross-model comparison,
* and long-horizon continuity benchmarking.

---

## 14. Novelty

The novelty of SemCrys0 lies in shifting semantic density amplification from:

* model architecture,
  to:
* communication protocol.

Current approaches typically attempt to:

* increase model memory,
* compress semantic content,
* or retrieve external information.

SemCrys0 instead compresses:

* repeated representational surfaces.

The protocol therefore operates independently of:

* transformer architecture,
* sparse attention mechanisms,
* retrieval augmentation,
* recurrent memory systems,
* or model fine-tuning.

Substantial semantic density amplification emerges from communication-layer optimization alone.

---

## 15. Discussion

SemCrys0 suggests that reasoning capacity may be partially improved through symbolic protocol engineering independently of architectural scaling.

This reframes part of the context-window problem:

* not solely as a memory problem,
  but:
* as a representation efficiency problem.

Because transformer attention operates over token sequences rather than intrinsic semantic units, increasing semantic payload per token directly increases the amount of recoverable meaning within a fixed context window.

The protocol also reveals an unusual property:

* symbolic continuity failures naturally expose context retention degradation.

This creates operational continuity measurements as a side effect of ordinary use.

More broadly, SemCrys0 demonstrates that:

* temporary symbolic languages,
* session-local legends,
* and dynamically governed communication surfaces

can meaningfully alter effective semantic capacity without modifying the underlying model itself.

---

## 16. Conclusion

SemCrys0 demonstrates that semantic density amplification can produce measurable improvements in effective context window utilization through communication protocol engineering alone, without modifying the underlying model and without requiring external infrastructure.

Using only session-local symbol substitution and legend injection, sustained conversations achieve:

* 69--81.5% representational surface compression,
  while increasing semantic density through repeated symbolic reuse.

The protocol is immediately deployable in existing LLM interfaces.

Its central insight is simple:

> the effective semantic capacity of a reasoning system depends not only on the size of its memory, but on the representational efficiency of the communication occurring inside it.

## Corpus-Wide Reference Positioning

This paper argues that large language model systems remain constrained by finite context windows. Its nearest external comparison fields are ai, token, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Retrieval, tool use, and policy layers can reduce unsupported output without eliminating model error, source error, omission, bias, or the environmental and institutional costs of scale. Statistical compression can improve efficiency while destroying distinctions needed for interpretation; semantic labels can conversely overstate stability that usage does not support. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[E6]** Rico Sennrich, Barry Haddow, and Alexandra Birch. "Neural Machine Translation of Rare Words with Subword Units." *ACL 2016*, pp. 1715-1725. DOI: 10.18653/v1/P16-1162. https://doi.org/10.18653/v1/P16-1162 **Relationship:** Predecessor subword tokenization method used as a contrast to semantically governed token boundaries.

**[E7]** Taku Kudo and John Richardson. "SentencePiece: A Simple and Language Independent Subword Tokenizer and Detokenizer for Neural Text Processing." *EMNLP 2018: System Demonstrations*. DOI: 10.18653/v1/D18-2012. https://doi.org/10.18653/v1/D18-2012 **Relationship:** Predecessor tokenizer implementation used to separate statistical segmentation from semantic admissibility.

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

**[A6]** Adam Ableman. *Governed Semantic Tokens: Tokenization as an Admissibility Boundary*. Ableman Corpus current edition; work identity `PAPER.PUB.18469507`;  
source SHA-256  
`5C44175B87C514892A0DC9743E09D03893E970AF5419F2E6D9171651BE2A9A54`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Token Parsimony*. Ableman Corpus current edition; work identity `PAPER.PUB.20382825`;  
source SHA-256  
`EC3AA22D32E2BBA21CFCB6D1FA2AE6EA8AC11B7781D19C51530A2F6D924B2E91`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20370117](https://doi.org/10.5281/zenodo.20370117)
