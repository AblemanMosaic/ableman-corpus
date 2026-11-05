# Constitutional Incompleteness

## Capability Gaps, Internalization, and the Evolution of Constitutions

### A constitution may function, remain coherent, and still leave capability on the table.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract
This paper develops a theory of constitutional incompleteness.

Many systems appear successful, coherent, and stable while still relying upon external mechanisms to provide capabilities not present within their constitutional structure. These mechanisms may include managers, coordinators, planners, regulators, optimization layers, or centralized intelligence.

The constitutional perspective treats such situations differently.

Rather than assuming external capability is necessary, the framework asks whether the observed capability can be internalized through constitutional refinement.

The paper introduces:

* constitutional incompleteness,
* capability gaps,
* constitutional internalization,
* local completeness,
* constitutional closure.

A constitution is incomplete with respect to a task when a constitutional amendment exists that improves performance without introducing fundamentally new structural mechanisms. Capability gaps therefore become observable indicators of latent constitutional structure.

The framework proposes that constitutional evolution proceeds through repeated discovery and closure of incompleteness. Constitutions become progressively richer not through accumulation of authority but through internalization of capabilities previously supplied externally.

The central claim:

> A capability gap is evidence of constitutional structure not yet discovered.

---

## 1. Introduction

The dominant question of organizational and computational design has historically been:

> How can additional capability be added?

The common answer is straightforward.

Add:

* more intelligence,
* more authority,
* more coordination,
* more memory,
* more optimization,
* more management.

Capability enters from outside.

The constitutional perspective begins elsewhere.

It asks:

> What capability is already latent within the constitution?

Many systems appear dependent upon external structures that later become unnecessary.

Functions once requiring:

* supervisors,
* schedulers,
* coordinators,
* centralized control,

often become internalized through refinement of local rules.

This observation motivates a different interpretation.

External capability may sometimes indicate constitutional incompleteness rather than constitutional limitation.

---

## 2. The Completeness Assumption

Traditional approaches frequently assume:

```text id="wn4p89"
Capability Gap
      |
External Mechanism
      |
Improved Performance
```

The external mechanism appears necessary.

The constitutional perspective introduces a competing interpretation.

```text id="r0jx5t"
Capability Gap
      |
Constitutional Incompleteness
      |
Constitutional Amendment
      |
Improved Performance
```

The capability existed implicitly.

The constitution had not yet captured it.

---

## 3. Constitutional Incompleteness

Let:

$$
C
$$

denote a constitution.

Let:

$$
\tau
$$

denote a task.

A constitution is incomplete with respect to:

$$
\tau
$$

when there exists an admissible amendment:

$$
C'
$$

such that:

$$
P(C',\tau)
>
P(C,\tau)
$$

without introducing fundamentally new structural mechanisms.

The capability gap identifies incompleteness.

The amendment identifies closure.

---

## 4. Capability Gaps

A capability gap exists whenever observed performance differs from achievable performance.

Let:

$$
P^*
$$

denote attainable performance.

The capability gap becomes:

$$
G_C = P^* - P(C).
$$

Capability gaps are observable.

Their source is not always obvious.

Traditional interpretations often attribute gaps to:

* insufficient intelligence,
* insufficient authority,
* insufficient resources.

The constitutional interpretation introduces an additional possibility:

* insufficient constitutional structure.

---

## 5. Constitutional Internalization

Constitutional internalization occurs when a capability previously supplied externally becomes encoded within constitutional structure.

Let:

$$
E
$$

denote an external capability source.

Internalization occurs when:

$$
P(C')
\approx
P(C+E).
$$

The constitution reproduces the capability.

The external mechanism becomes optional.

Internalization therefore transforms dependency into structure.

---

## 6. Constitutional Closure

Closure occurs when a capability gap disappears.

Let:

$$
G_C
$$

denote capability gap.

Closure occurs when:

$$
G_C
\rightarrow
0.
$$

Closure does not imply perfection.

Closure implies only that the identified capability gap has been absorbed into constitutional structure.

New incompletenesses may remain.

---

## 7. Local Completeness

Completeness is relative.

A constitution may be complete with respect to one task while remaining incomplete with respect to another.

Define:

$$
C
\text{ complete relative to }
\tau
$$

when:

$$
\nexists
C'
$$

such that:

$$
P(C',\tau)
>
P(C,\tau)
$$

within the admissible amendment space.

Completeness therefore remains task-dependent.

---

## 8. Constitutional Search Space

Not all amendments are admissible.

Let:

$$
\mathcal A(C)
$$

denote the admissible amendment space.

Constitutional evolution occurs within:

$$
\mathcal A(C).
$$

Incompleteness is therefore relative to reachable amendments.

An unreachable capability does not constitute constitutional incompleteness.

A reachable capability does.

---

## 9. Internalization Cascades

Closure of one incompleteness frequently reveals another.

Let:

$$
C_0
$$

denote an initial constitution.

Then:

$$
C_0
\rightarrow
C_1
\rightarrow
C_2
\rightarrow
\cdots
$$

may represent successive closures.

Each amendment exposes new structure.

Constitutional evolution becomes iterative.

---

## 10. Constitutional Discovery

The framework interprets constitutional evolution as discovery.

The constitution does not merely accumulate rules.

It reveals latent structure.

Observed capability gaps become clues.

Amendments become discoveries.

Constitutional progress therefore resembles exploration more than construction.

---

## 11. Constitutional Latency

Capabilities may exist implicitly before becoming explicit.

Let:

$$
L(C)
$$

denote latent capability.

Latent capability exists when:

$$
P(C')
>
P(C)
$$

for some admissible amendment:

$$
C'.
$$

The capability was already available within constitutional space.

It had not yet been realized.

---

## 12. External Capability

External mechanisms remain important.

The framework does not assume all capability is internalizable.

Some capabilities may genuinely require:

* hierarchy,
* memory,
* centralized aggregation,
* additional resources.

The distinction remains empirical.

The framework provides a method for testing necessity.

---

## 13. Constitutional Debt

Persistent incompleteness generates constitutional debt.

The constitution repeatedly relies upon external structures to supply missing capability.

Let:

$$
D_C
$$

denote constitutional debt.

Debt increases when:

$$
G_C
$$

persists through time.

Internalization reduces debt.

---

## 14. Biological Examples

Biological evolution frequently appears to internalize capability.

Examples include:

* reflexes replacing deliberation,
* developmental programs replacing environmental dependence,
* immune memory replacing repeated adaptation.

The framework interprets these transitions as constitutional closure.

---

## 15. Computational Examples

Computing systems routinely internalize capability.

Examples include:

* caching replacing repeated computation,
* protocols replacing manual coordination,
* compilers replacing handwritten machine code,
* automation replacing supervision.

Many technological advances may be interpretable as constitutional closure.

---

## 16. Institutional Examples

Institutions exhibit similar dynamics.

Capabilities initially requiring:

* committees,
* supervisors,
* regulators,

may later become embedded within procedures and norms.

The capability remains.

The external structure shrinks.

This is constitutional internalization.

---

## 17. The Constitutional Horizon

A constitution possesses a horizon of discoverable amendments.

Let:

$$
H_C
$$

denote the constitutional horizon.

The horizon consists of reachable improvements not yet realized.

The larger the horizon, the greater the remaining incompleteness.

---

## 18. Propositions

### Proposition 1 (Gap Witness)

Assume:

$$
P(C')
>
P(C)
$$

for an admissible amendment:

$$
C'.
$$

Then:

$$
C
$$

is incomplete relative to the measured task.

#### Proof Sketch

The existence of a superior admissible amendment demonstrates unrealized constitutional capability.

The constitution is therefore incomplete.

---

### Proposition 2 (Closure Criterion)

Assume no admissible amendment exists such that:

$$
P(C')
>
P(C).
$$

Then:

$$
C
$$

is locally complete relative to the admissible amendment space.

#### Proof Sketch

All reachable constitutional improvements have been exhausted.

No remaining capability gap exists within the amendment space.

---

## 19. Experimental Program

The framework proposes five branches.

### Branch 1 - Gap Identification

Measure capability gaps.

### Branch 2 - Amendment Discovery

Search admissible amendment space.

### Branch 3 - Internalization

Attempt capability closure.

### Branch 4 - Horizon Measurement

Estimate remaining incompleteness.

### Branch 5 - Constitutional Evolution

Study iterative closure dynamics.

---

## 20. Metrics

### Capability Gap

$$
G_C.
$$

### Internalization Fraction

$$
I_C
=
\frac{
P(C')-P(C)
}{
P(C+E)-P(C)
}.
$$

### Constitutional Debt

$$
D_C.
$$

### Closure Rate

$$
R_C.
$$

### Horizon Size

$$
|H_C|.
$$

---

## 21. Failure Modes

### False Closure

A capability gap is believed closed when it remains.

### Horizon Blindness

Reachable amendments remain undiscovered.

### External Dependency Lock

Capability remains permanently externalized.

### Constitutional Saturation

Amendments become increasingly difficult to identify.

### Infinite Deferral

Debt accumulates faster than closure occurs.

---

## 22. Comparative Positioning

Traditional theories often ask:

> What additional mechanism is required?

Constitutional incompleteness asks:

> What capability already exists within the constitutional search space?

The shift changes the role of external structures.

External capability becomes evidence.

Not necessarily necessity.

---

## 23. Applications

Potential applications include:

* artificial intelligence,
* institutional governance,
* constitutional design,
* operating systems,
* distributed systems,
* robotics,
* evolutionary theory,
* organizational development.

The framework is substrate-neutral.

Only constitutional structure is required.

---

## Conclusion

This paper proposes a theory of constitutional incompleteness.

A constitution may remain coherent, stable, and functional while still leaving capability unrealized.

Capability gaps become indicators of latent constitutional structure.

Constitutional evolution proceeds through discovery, amendment, and closure.

External mechanisms may provide capability.

Whether that capability is necessary remains an empirical question.

The framework introduces constitutional incompleteness, constitutional closure, constitutional horizons, and internalization as tools for studying this process.

The central hypothesis:

> A capability gap is evidence of constitutional structure not yet realized rather than proof of capability that cannot be internalized.

If correct, constitutions evolve not merely by accumulating authority.

They evolve by discovering themselves.

---

## Appendix A: Formal Research Questions

1. How should constitutional horizons be measured?

2. What determines amendment discoverability?

3. Which capabilities are internalizable?

4. Which capabilities remain external?

5. Does constitutional evolution converge?

---

## Appendix B: Initial Experimental Roadmap

Phase 0: Gap instrumentation.

Phase 1: Amendment search.

Phase 2: Internalization studies.

Phase 3: Horizon mapping.

Phase 4: Evolution experiments.

Phase 5: Closure analysis.

---

## Corpus-Wide Reference Positioning

This paper argues that a theory of constitutional incompleteness. Its nearest external comparison fields are governance, security, formal. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. Formal assurance remains relative to the encoded model, trusted base, and refinement chain; proof does not remove specification error or unmodeled environmental behavior. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E2]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E3]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E6]** Mark S. Miller. *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control*. PhD dissertation, Johns Hopkins University, 2006. http://www.erights.org/talks/thesis/ **Relationship:** Predecessor object-capability treatment of authority and compositional security.

**[E7]** Gerwin Klein et al. "seL4: Formal Verification of an OS Kernel." *SOSP '09*, 2009, pp. 207-220. DOI: 10.1145/1629575.1629596. https://doi.org/10.1145/1629575.1629596 **Relationship:** Predecessor for machine-checked implementation correspondence and capability-based kernel design.

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

**[A6]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

### Author Works (Constitutional Framework Series)

Ableman Adam Ableman (in preparation). *Constitutional Collective with Optional Overmind*. Manuscript.

Ableman Adam Ableman (in preparation). *The Optional Coordinator*. Manuscript.

Ableman Adam Ableman (in preparation). *Constitutional Intelligence*. Manuscript.

### External Works

Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.

Simon, H. A. (1962). The architecture of complexity. *Proceedings of the American Philosophical Society*, 106(6), 467-482.

Holland, J. H. (1998). *Emergence: From Chaos to Order*. Addison-Wesley.

Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.

### Standing and Claim Boundary

This paper is a conceptual, formal, or architectural contribution unless it explicitly binds a statement to a cited external source or an exact carried evidence artifact. Unbound statements about implementation, validation, performance, safety, universality, or proof are research claims or design obligations, not established operational facts. Corpus-internal references establish conceptual lineage and comparison, not independent external confirmation.

### References

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *The Three Hash Rule.* Zenodo, 2026. doi:10.5281/zenodo.20788617

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848647](https://doi.org/10.5281/zenodo.23848647)
