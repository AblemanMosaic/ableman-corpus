# Beneficiary-Resolved Tax Expenditure Governance

## A Governance Substrate for Tracing Public Subsidy into Enterprise Utility or Taxable Personal Utility

### "Every Subsidized Path Must Land Somewhere"

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Beneficiary-Resolved Tax Expenditure Governance models tax expenditures as public subsidy flows. Each subsidized transaction or asset event $(X)$ is represented in a benefit graph $(G=(V,A,\tau,\mu,\pi))$ with typed edges, evidence weights, and provenance bindings. Every subsidized path terminates in an enterprise sink, personal sink, escrow sink, refusal sink, or appealable conversion sink. The framework composes tax expenditure theory, IRC §§61/162/167/274, fringe-benefit doctrine, economic substance, FATCA/CRS-style beneficiary resolution, and VAT/input-credit logic.

## 1. Claim and Bound

BRTEG governs access to public subsidy, not general consumption.

The framework is bounded in four ways. **Substantively**, it traces only subsidized flows — transactions and asset events that receive tax-preferred treatment — and is silent on after-tax economic activity. **Doctrinally**, it is a governance substrate, not a tax-code redesign: it operates within existing statutory categories (IRC §§61, 162, 167, 274) rather than altering them. **Epistemically**, its core theorem holds only under complete evidence, bounded MAC and attribution error, and enforced conversion; outside these conditions it falls back to safe harbor, escrow, or human review. **Definitionally**, it does not attempt to resolve irreducibly ambiguous benefit zones — diffuse brand value, morale, reputation, research spillovers, and mixed social/professional utility — but routes them to declared fallbacks.

```text
subsidy flow
-> graph attribution
-> enterprise utility or taxable personal utility
-> escrow/refusal/conversion when unresolved or inadmissible
```

## 2. Doctrinal Anchoring

- **Claim:** Tax preference as subsidy  
  **Anchor:** Surrey  
  **Function:** subsidy treatment

- **Claim:** Converted benefit as income  
  **Anchor:** IRC §61  
  **Function:** inclusion

- **Claim:** Enterprise necessity  
  **Anchor:** IRC §162  
  **Function:** substantiation

- **Claim:** Asset-use requirement  
  **Anchor:** IRC §167  
  **Function:** recapture

- **Claim:** Meals/travel limits  
  **Anchor:** IRC §274  
  **Function:** admissibility priors

- **Claim:** Substance over form  
  **Anchor:** Economic substance  
  **Function:** anti-relabeling

- **Claim:** Human beneficiary resolution  
  **Anchor:** FATCA/CRS  
  **Function:** ownership tracing

- **Claim:** Transaction governance  
  **Anchor:** VAT/input credits  
  **Function:** admissibility rails

## 3. Notation

$(X)$: transaction or asset event.

$(B(t))$: total utility.

$(E(t))$: enterprise utility.

$(P(t))$: personal utility.

$(\hat{P}_i(t))$: normalized allocation share.

$(G=(V,A,\tau,\mu,\pi))$: benefit graph.

$(\tau)$: edge type.

$(\mu)$: evidence weight.

$(\pi)$: provenance binding.

$(f_\theta)$: attribution function.

$(\delta)$: decision error bound.

$(\epsilon_M)$: MAC estimation error.

$(\epsilon_P)$: attribution error.

$(\epsilon=\epsilon_M+\epsilon_P)$.

$(Q_\alpha(\mathrm{MAC}))$: conditional MAC baseline.

$(L)$: luxury excess.

$(r)$: conversion tax rate.

$$
B(t)=E(t)+P(t)
$$

$$
\sum_i \hat{P}_i(t)=\frac{P(t)}{B(t)}
$$

## 4. Operational Attribution

Utility is operationalized from observable feature families, not subjective claims.

A declarative label establishes enterprise necessity only if supported by independent evidence.

## 5. Benefit Graph

$$
G=(V,A,\tau,\mu,\pi)
$$

Minimum edge schema:

```text
source
target
tau
mu
pi
time
purpose
model version
```

Conservation:

$$
\sum_{a\in in(v)} w_a = \sum_{a\in out(v)} w_a
$$

for all non-source, non-sink nodes.

Valid sinks:

```text
enterprise
personal
escrow
refusal
appealable conversion
```

## 6. Identifiability

Unique attribution exists iff sufficient evidence, finite beneficiaries, and consistent edge algebra permit computation of $(f_\theta(G,\mathcal{R},t))$ within $(\delta)$.

Otherwise:

$$
[\hat{P}]={\hat{P}^{(1)},...,\hat{P}^{(k)}}
$$

and bounded pessimism selects the least over-attributing admissible allocation.

## 7. Minimum Adequate Cost

$$
Q_\alpha(\mathrm{MAC})
$$

is the conditional adequate-cost quantile for a similarly situated enterprise.

$$
L=\max(0,C-Q_\alpha(\mathrm{MAC}))
$$

Quantiles reduce heavy-tail and thin-market manipulation.

## 8. Temporal Rule

Utility attribution is accrual-based; conversion may occur at point-of-sale, reconciliation, or audit finalization; deferred benefits require lifecycle reconciliation.

## 9. Provenance and Privacy

Artifacts:

```text
purpose declaration
receipt
usage record
ownership attestation
beneficiary attestation
attribution record
decision record
appeal record
```

Decision output:

$$
(\mathcal{R}',f_\theta,\hat{P},\delta)
$$

Internal adjudication may use sensitive data; public disclosure is limited to aggregates, hashes, and model statistics.

## 10. Architecture

```text
Policy: thresholds, purposes, MAC baselines.
Execution: evidence capture, attribution, reporting.
Trusted oracle: binding determinations.
Nonbinding oracle: evidence, priors, estimates.
```

## 11. Safe Harbor

Apply standardized treatment whenever:

$$
C < \tau_s
$$

or

$$
\mathrm{Var}(\hat{P}) < \epsilon_s
$$

where $(\tau_s)$ is the published de minimis threshold and $(\epsilon_s)$ is the published attribution-variance threshold.

## 12. Worked Example

Mixed-use vehicle:

```text
Actual cost C:            $24,000
Q_alpha(MAC):                  $15,000
Enterprise share:         60%
Personal share:           40%
```

Result:

```text
Enterprise admission:     $9,000
Total conversion:         $15,000
```

Appeal:

```text
Corrected usage records reduce personal share to 30%.

30% < rho

Recapture avoided.
Conversion reduced.
State:
CONVERTED -> APPEALED -> REVERSED -> FINAL
```

## 13. Attack Model

- **Evasion:** Fragmentation  
  **Signal:** threshold clustering  
  **Mitigation:** beneficial-owner aggregation  
  **Residual Risk:** unrelated collusion

- **Evasion:** Proxy beneficiaries  
  **Signal:** recurring indirect access  
  **Mitigation:** ownership/control graph  
  **Residual Risk:** informal proxies

- **Evasion:** MAC inflation  
  **Signal:** comparator outliers  
  **Mitigation:** conditional MAC datasets  
  **Residual Risk:** thin markets

- **Evasion:** Time shifting  
  **Signal:** usage drift  
  **Mitigation:** lifecycle reconciliation  
  **Residual Risk:** long horizons

- **Evasion:** Relabeling  
  **Signal:** purpose/usage mismatch  
  **Mitigation:** independent evidence  
  **Residual Risk:** fabricated narratives

- **Evasion:** Graph inflation  
  **Signal:** excessive path complexity  
  **Mitigation:** regularization  
  **Residual Risk:** legitimate complexity

- **Evasion:** Offshore opacity  
  **Signal:** unresolved foreign chain  
  **Mitigation:** FATCA/CRS priors, escrow  
  **Residual Risk:** noncooperative jurisdictions

- **Evasion:** Co-consumption  
  **Signal:** shared luxury use  
  **Mitigation:** allocation rules  
  **Residual Risk:** social ambiguity

## 14. Deployment

Pilot BRTEG on large firms claiming tax-preferred treatment in high-risk mixed-use categories.

Expand only if unsupported subsidy claims fall by at least 20%, appeal reversals remain below 5%, and compliance cost remains below 10% of recovered subsidy value.

Apply the same thresholds to all future category expansions.

## 15. Validation

Metrics:

```text
false positives
false negatives
appeal reversals
compliance cost
recovered subsidy value
MAC calibration error
audit yield
opacity substitution
```

BRTEG is weakened if appeal reversals remain high, compliance burden exceeds recovered subsidy value, or opacity substitution outpaces attribution.

## 16. Bounded Reduction Theorem

Assumptions:

A1. Complete evidence.

A2. Finite beneficiaries.

A3. Consistent edge algebra.

A4. Conservation into valid sinks.

A5. Bounded MAC error:

$$
|\widehat{Q}_\alpha - Q_\alpha| \le \epsilon_M
$$

A6. Bounded attribution error:

$$
|\hat{P}-P| \le \epsilon_P
$$

A7. Positive conversion rate:

$$
r>0
$$

A8. Rational agents maximize expected after-tax utility.

A9. Bounded obfuscation return.

Define:

$$
\epsilon=\epsilon_M+\epsilon_P
$$

Theorem.

Under A1–A9, BRTEG weakly decreases subsidized luxury substitution relative to baseline tax-preferred treatment and strictly decreases it whenever:

$$
rL>\epsilon
$$

Proof.

Baseline treatment preserves subsidy value on luxury excess $(L)$. BRTEG identifies $(L)$ within $(\epsilon_M)$, attributes the resulting personal share within $(\epsilon_P)$, and forces all subsidized paths into valid sinks through conservation. Personal utility generated by $(L)$ is converted at rate $(r)$. The after-tax advantage of subsidized luxury therefore decreases by at least $(rL-\epsilon)$. If $(rL>\epsilon)$, the decrease is strict; otherwise it is weak or indeterminate.

## 17. Non-Applicability

The theorem does not apply under:

```text
incomplete evidence
unbounded MAC or attribution error
unenforced conversion or dominant obfuscation
```

## 18. Limitations

Irreducibly ambiguous benefit zones include diffuse brand value, firm-wide morale, reputation, research spillovers, and mixed social/professional utility.

Fallbacks:

```text
safe harbor
escrow
human review
sector schedule
de minimis exclusion
```

## 19. Conclusion

BRTEG is a governance substrate, not a tax-code redesign, for tracing public subsidy into enterprise utility or taxable personal utility.

## Corpus-Wide Reference Positioning

This paper argues that beneficiary-Resolved Tax Expenditure Governance models tax expenditures as public subsidy flows. Its nearest external comparison fields are markets, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Optimization can make a chosen objective efficient while preserving a bad objective, missing distributional harms, strategic behavior, or inadmissible states. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Harry Markowitz. "Portfolio Selection." *The Journal of Finance* 7(1), 1952, pp. 77-91. DOI: 10.1111/j.1540-6261.1952.tb01525.x. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x **Relationship:** Predecessor risk-return optimization model; included to distinguish scalar optimization from governance-aware admissibility.

**[E2]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E3]** U.S. Department of the Treasury. *Tax Expenditures*. Office of Tax Analysis. [home.treasury.gov source](https://home.treasury.gov/policy-issues/tax-policy/tax-expenditures) **Relationship:** Primary official baseline for the definition and estimation limits of U.S. federal tax expenditures.

**[E4]** OECD. *Recommendation of the Council on Artificial Intelligence*. OECD/LEGAL/0449, adopted 2019 and updated 2024. [legalinstruments.oecd.org source](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449) **Relationship:** Adjacent policy standard for accountability, traceability, transparency, safety, and human-centered values.

**[E5]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E6]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

### Ableman corpus

**[A1]** Adam Ableman. *Constitutional Markets*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1D49CCBB6E47B403`;  
source SHA-256  
`BB97EAC6F1861C2ED17DC0E0B75D47B04716E7FF3E3AC2A9B2F6CABCC67A5250`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *ACG for Quants*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-8A19CB4C1BD55BCA`;  
source SHA-256  
`2FEA83087B8DA79472BBA449C9D5B252B6DBA67C2EAF0DF41C206B1B0EEEF254`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Quant Insights for ACG Systems*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-EAEEDA4A34808C9B`;  
source SHA-256  
`F668C40E0FE27BDBFDC881BFA97735D61F00335A6FC3DF9488A4BCFCFFB19631`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Governance Incentive Engineering*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-294436DA22D85E3A`;  
source SHA-256  
`30B4151092AA9C1157214B00B695BD39A137C010DFE3BC631A64073F946ACD4A`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

Surrey, S. S. *Pathways to Tax Reform: The Concept of Tax Expenditures*. Harvard University Press, 1973.

Internal Revenue Code, 26 U.S.C.: §61 (Gross income defined); §162 (Trade or business expenses); §167 (Depreciation); §274 (Disallowance of certain entertainment, etc., expenses).

Foreign Account Tax Compliance Act (FATCA), 26 U.S.C. §§1471–1474.

OECD. *Standard for Automatic Exchange of Financial Account Information in Tax Matters* (Common Reporting Standard, CRS). 2nd ed., 2017.

Economic substance doctrine, 26 U.S.C. §7701(o).

European Commission. *Council Directive 2006/112/EC of 28 November 2006 on the common system of value added tax* (VAT input-credit framework).

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20602489](https://doi.org/10.5281/zenodo.20602489)
