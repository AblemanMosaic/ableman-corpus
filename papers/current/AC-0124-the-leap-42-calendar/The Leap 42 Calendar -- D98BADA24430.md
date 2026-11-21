# The Leap 42 Calendar

## A Parsimonious Decimal Calendar and Timekeeping Architecture

### The Shape of a Simpler Year

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Modern civil timekeeping remains structurally irregular: months vary in length, leap behavior is distributed through special rules, and clock time preserves sexagesimal divisions inherited from pre-digital systems. This paper presents **Leap 42**, a decimal calendar and timekeeping architecture whose primary design goal is the elimination of unnecessary irregularity through strict temporal parsimony. The system uses decimal time---ten hours per day, 100 minutes per hour, and 100 seconds per minute---and a ten-month calendar in which months 1--9 each contain 36 days, while month 10 contains 41 days in standard years and 42 days in leap years.

The proposal does not claim novelty for decimal time, which directly echoes French Revolutionary decimal time. Its novelty lies in the calendar geometry: rather than placing balancing days outside the month system as intercalary or festival days, Leap 42 contains all irregularity inside a single terminal month. This creates a piecewise-regular temporal model: nine uniform months followed by one bounded balancing month. The year begins on the winter solstice, providing an astronomically stable and culturally neutral anchor that is independent of any particular civilization's historical epoch.

The paper defines the core model, temporal arithmetic, serialization, Gregorian and Unix interoperability, and derived properties. It argues that Leap 42 is unlikely to replace civil timekeeping in the near term, but may be useful as a computational time base for simulation systems, archival infrastructures, decentralized ledgers, digital governance, and machine-native scheduling environments.

---

\newpage

## 1. Introduction

Calendars are coordination machines.

They organize agriculture, labor, memory, law, finance, software, ceremony, and computation. Yet the dominant Gregorian calendar is not a clean temporal architecture. It is a historical sediment: astronomical correction layered over Roman inheritance, religious authority, imperial administration, and later industrial synchronization.

The result works socially, but it is computationally awkward. Months vary from 28 to 31 days. Leap rules require special handling. Weeks drift across months. Time itself is divided into 24 hours, 60 minutes, and 60 seconds, despite modern computation being overwhelmingly decimal or binary.

Leap 42 asks a simple design question: What would a civil calendar look like if its governing value were parsimony?

The answer proposed here is not perfect symmetry. Astronomical years do not permit perfect decimal subdivision without remainder. Instead, Leap 42 minimizes irregularity by containing it. The system keeps most of the calendar strictly regular and isolates the unavoidable remainder inside a single terminal month.

---

## 2. Historical Context and Related Work

### 2.1 French Revolutionary Decimal Time

French Revolutionary decimal time divided the day into 10 hours, 100 minutes per hour, and 100 seconds per minute. Leap 42 adopts this same structure. Decimal time itself is therefore not novel. The value of reintroducing it here is architectural: decimal time completes the base-10 temporal model and gives the calendar a machine-native clock layer.

### 2.2 French Republican Calendar

The French Republican Calendar used 12 months of 30 days, followed by complementary days outside the ordinary month structure. Leap 42 differs by avoiding extra-calendar days entirely.

### 2.3 Positivist and Fixed Calendar Systems

The Positivist Calendar and International Fixed Calendar pursue regularity through different month structures, especially 13-month arrangements. These systems are useful comparators but do not share Leap 42's ten-month geometry or terminal balancing month.

### 2.4 Global Decimal Calendar

Robert Erasmus's Global Decimal Calendar (2013) is the closest known structural predecessor. It uses 10 months of 36 days and handles remaining days as festival or intercalary periods outside ordinary months. Leap 42 differs in the key design choice: all days remain inside the calendar. The balancing days are absorbed into month 10.

---

## 3. Core Temporal Model

Leap 42 has two linked components: decimal time and decimal calendar geometry.

### 3.1 Decimal Time

A day is divided as follows: 1 day = 10 hours; 1 hour = 100 minutes; 1 minute = 100 seconds. Thus:

$$1 \text{ day} = 100{,}000 \text{ decimal seconds}$$

Each decimal second equals 0.864 SI seconds. Time is represented as the triple (h, m, s) where h is in [0, 9], m is in [0, 99], and s is in [0, 99]. A scalar time-of-day value is defined as:

$$T = h \cdot 10000 + m \cdot 100 + s, \quad T \in [0, 99999]$$

### 3.2 Calendar Geometry

A Leap 42 year contains 10 months. Months 1--9 contain 36 days each. Month 10 contains 41 days in standard years and 42 days in leap years:

$$\text{Normal year:} \quad 9 \times 36 + 41 = 365$$

$$\text{Leap year:} \quad 9 \times 36 + 42 = 366$$

### 3.3 Placeholder Month Names

The informal month names used during development are Oneuary through Tenuary (Oneuary, Twouary, Threeuary, Fouruary, Fiveuary, Sixuary, Sevenuary, Eightuary, Nineuary, Tenuary). These are placeholders only. Leap 42 does not prescribe culturally authoritative month names, nor does it prescribe a universal civilizational Year 0. Month names, epoch events, and hemisphere conventions are cultural decisions. The structure itself is mathematical.

### 3.4 Year Start and Astronomical Anchor

The Leap 42 year begins on the winter solstice. Month 1, Day 1 of every year is defined as the day on which the winter solstice falls. This choice provides three properties: it is astronomically stable across millennia; it is culturally neutral relative to any particular civilization's inherited calendar; and it gives the terminal month a physical interpretation---month 10 absorbs the remainder between the 365- or 366-day decimal year and the actual elapsed time between successive solstices.

The winter solstice anchor does not fix the cultural Year 0. That remains an independent decision. The anchor fixes only the intra-year structure: wherever a given year begins, it begins at the solstice.

### 3.5 Canonical Date Representation

The canonical date form is numeric: (Y, M, D), where Y is the year, M is in [1, 10], and D is the day of month. Month names are labels, not structural components.

### 3.6 Leap Rule

The simplest reference leap rule is Y mod 4 = 0, which produces a 366-day year every fourth year and drifts by approximately one day every 128 years. Because the year is anchored to the winter solstice, the leap predicate has a physical motivation: it keeps Month 1, Day 1 aligned with the solstice over long timescales. Production implementations should therefore substitute the Gregorian-style rule, which closely tracks the actual solar year:

$$\bigl(Y \bmod 4 = 0\bigr) \;\land\; \bigl(Y \bmod 100 \neq 0 \;\lor\; Y \bmod 400 = 0\bigr)$$

Leap 42 treats leap behavior as a predicate LeapRule(Y). The geometry remains unchanged as long as leap days are added only to month 10.

---

## 4. Month Length and Validity

Month length is defined as:

$$\text{Length}(Y, M) = \begin{cases} 36 & M \in [1, 9] \\ 41 + \mathbf{1}[\text{LeapRule}(Y)] & M = 10 \end{cases}$$

A date (Y, M, D) is valid if and only if M is in [1, 10] and 1 <= D <= Length(Y, M). Year length is:

$$\text{YearLength}(Y) = 365 + \mathbf{1}[\text{LeapRule}(Y)]$$

---

## 5. Temporal Arithmetic

### 5.1 Ordinal Date

The ordinal day of year Ordinal(Y, M, D) is computed as follows. For months 1--9:

$$\text{Ordinal} = 36(M - 1) + D$$

For month 10:

$$\text{Ordinal} = 324 + D$$

The maximum ordinal is MaxOrdinal(Y) = 365 + 1 if LeapRule(Y) holds, and 1 <= Ordinal <= MaxOrdinal(Y).

### 5.2 Inverse Ordinal Mapping

Given ordinal o: if o <= 324, then M = ceil(o / 36) and D = o - 36(M - 1). Otherwise M = 10 and D = o - 324. This makes date-to-ordinal and ordinal-to-date conversion fully invertible.

### 5.3 Absolute Day Number

The absolute day number ADN(Y, M, D) provides a monotonic integer timeline. Under the simple four-year leap rule:

$$\text{ADN} = 365Y + \lfloor Y/4 \rfloor + \text{Ordinal}(Y, M, D) - 1$$

More generally:

$$\text{ADN} = 365Y + \sum_{i=0}^{Y-1} \text{LeapRule}(i) + \text{Ordinal}(Y, M, D) - 1$$

### 5.4 Successor and Predecessor

Next(Y, M, D): if D < Length(Y, M), return (Y, M, D+1); else if M < 10, return (Y, M+1, 1); else return (Y+1, 1, 1). Prev(Y, M, D): if D > 1, return (Y, M, D-1); else if M > 1, return (Y, M-1, Length(Y, M-1)); else return (Y-1, 10, Length(Y-1, 10)).

### 5.5 Timestamp

A complete timestamp is represented as (Y, M, D, T) or as the scalar:

$$\text{TS} = \text{ADN} \cdot 100000 + T$$

This gives a single integer timeline with deterministic ordering.

---

## 6. Serialization and Conversion

### 6.1 Canonical String Format

The canonical date format is `YYYY-MM-DD`. The canonical timestamp format is

`YYYY-MM-DDThh.mm.ss`. Example: `0208-10-42T05.50.00`. Canonical padding rules: YYYY minimum four digits zero-padded; MM and DD exactly two digits; hh, mm, ss exactly two digits. Negative years are written as `-0001-01-01`.

### 6.2 Parse/Serialize Invariant

For all valid serialized timestamps, Serialize(Parse(x)) = x. Each valid timestamp has exactly one canonical serialization.

### 6.3 Gregorian Conversion

Gregorian-to-Leap conversion requires: (1) compute the Gregorian day-of-year relative to the winter solstice (not January 1); (2) map that solstice-relative day count into Leap 42 month and day; (3) apply chosen epoch alignment and leap rules. Because Leap 42 years begin at the winter solstice, the solstice-relative day count differs from the standard Gregorian day-of-year by approximately ten to eleven days depending on the year. Implementations must account for this offset; a naive DOY-from-January-1 mapping will produce incorrect results.

Once solstice-relative DOY is obtained, the month mapping follows: if DOY <= 324 then M = ceil(DOY / 36) and D = DOY - 36(M - 1); otherwise M = 10 and D = DOY - 324. Inverse conversion maps (M, D) back via DOY = 36(M-1)+D for M in [1, 9] and DOY = 324+D for M = 10. All conversions must specify source epoch, target epoch, source leap rule, target leap rule, solstice offset for the conversion year, and rounding behavior for time conversion.

### 6.4 Reference Epoch

A software reference implementation may define the epoch as the winter solstice nearest a chosen anchor date. One convenient choice for Unix interoperability is to align Leap 42 Year 0, Month 1, Day 1 with the winter solstice of 1969 (December 22, 1969 UTC), placing the Unix epoch of 1970-01-01 at approximately Leap 42 Year 0, Month 1, Day 10. Implementations must record the exact solstice date used as part of the epoch specification.

The cultural Year 0 remains an independent decision and is not prescribed by the reference epoch. Unix day and second offsets from the chosen epoch are:

$$\text{UnixDays} = \text{ADN} - \text{ADN}_{\text{epoch}}$$

$$\text{UnixSeconds} = (\text{ADN} - \text{ADN}_{\text{epoch}}) \cdot 86400 + \left\lfloor \frac{T \cdot 86400}{100000} \right\rfloor$$

Implementations requiring exactness should preserve rational remainders rather than silently discarding subsecond information.

---

## 7. Derived Properties

### 7.1 Bounded Irregularity

Only month 10 varies. The irregularity measure I = max_M Length(Y, M) - min_M Length(Y, M) = 42 - 36 = 6. All other months are identical in length across all years.

### 7.2 Leap Locality

Leap-year variation is confined to month 10. For all M in [1, 9]: Length(Y, M) = Length(Y+1, M).

### 7.3 Continuous Calendrical Identity

Every day belongs to a valid (Y, M, D). There are no festival days, blank days, or out-of-band dates.

### 7.4 Constant-Time Arithmetic

Date-to-ordinal, ordinal-to-date, leap checking, timestamp comparison, and month length validation are all constant-time operations under the reference model.

### 7.5 Statelessness

Once epoch and leap predicate are specified, all temporal values are fully determined by (Y, M, D, T). No hidden lookup table or historical exception list is required.

### 7.6 Total Ordering

Dates may be ordered by ADN. Timestamps may be ordered by TS = ADN * 100000 + T. Lexicographic ordering of canonical timestamp tuples is equivalent to chronological ordering.

---

## 8. Week and Institutional Fit

Leap 42 separates calendar geometry from week governance. A reference implementation may use a 6-day week because 36 = 6 x 6, giving every standard month exactly six weeks with no weekday drift across months 1--9. Other week systems remain possible: 7-day continuity week, 10-day decimal week, or weekless computational scheduling.

Institutionally, the system is well-suited to fiscal reporting, subscription billing, payroll modeling, simulation calendars, archival partitioning, distributed ledgers, and digital governance. The terminal month can function as an annual reconciliation period for audits, rollover, settlement, and closure.

---

## 9. Limitations and Adoption

Leap 42 is mathematically cleaner than Gregorian timekeeping, but social adoption would be difficult. Major limitations include:

- Entrenched Gregorian infrastructure
- Cultural attachment to the 7-day week
- Behavioral unfamiliarity of decimal hours (1 Leap 42 hour = 2.4 conventional hours)
- Need for leap-rule precision over long time spans
- Transition costs for existing legal and financial systems

The most plausible adoption path is therefore not immediate civil replacement, but computational use: machine-native timestamps, simulations, virtual worlds, archives, AI-agent environments, and decentralized systems.

---

## 10. Novelty Claim

Leap 42 does not claim invention of decimal time. Its novelty claim is the combination of:

- Decimal time
- Ten-month calendar structure
- Nine uniform 36-day months
- One terminal month of 41 or 42 days
- Leap normalization localized to the terminal month
- Year start anchored to the winter solstice
- No intercalary or extra-calendar days
- Continuous date identity
- Simple ordinal and timestamp arithmetic

The key architectural contribution is **single-region irregularity containment**: rather than distributing remainder days across the year or placing them outside the calendar, all irregular behavior is bounded within one terminal month. The winter solstice anchor gives this containment a physical meaning: month 10 holds the astronomical remainder between the decimal year and the solar year, and the leap predicate keeps that remainder bounded over long timescales.

---

## 11. Conclusion

Timekeeping systems are not neutral containers. They encode inherited assumptions about order, labor, astronomy, authority, and computation.

The Gregorian calendar is historically successful, but structurally irregular. Leap 42 offers a contrasting model: not a claim that society must abandon its inherited calendar, but a demonstration that timekeeping can be redesigned as a parsimonious information architecture.

Its central move is simple: make most of the year regular, and place the unavoidable remainder in one bounded terminal month. That choice turns a calendar into a clean temporal data model.

Whether used for civil reform, simulation, archival design, or machine-native chronology, Leap 42 shows that even one of civilization's oldest coordination systems can still be reimagined.

---

## Appendix A -- Example Date

(Y, M, D) = (208, 10, 42) is the final day of a leap year. Placeholder label: Tenuary 42.

---

## Appendix B -- Gregorian Conversion Example

Gregorian March 1 in a non-leap year is day 60.

$$M = \lceil 60 / 36 \rceil = 2, \quad D = 60 - 36 = 24$$

Equivalent Leap 42 date: (Y, 2, 24). Placeholder label: Twouary 24.

---

## Appendix C -- Decimal Time Example

Given T = 55000, SI seconds since start of day:

$$\left\lfloor \frac{55000 \times 86400}{100000} \right\rfloor = 47520$$

T = 55000 corresponds to 13:12:00 in conventional 24-hour time.

---

## Corpus-Wide Reference Positioning

This paper argues that modern civil timekeeping remains structurally irregular: months vary in length, leap behavior is distributed through special rules, and clock time preserves sexagesimal divisions inherited from pre-digital systems. Its nearest external comparison fields are time, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A precise representation of time or epoch does not resolve clock drift, jurisdictional calendar rules, synchronization failure, or the semantics of retroactive change. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** International Organization for Standardization. *ISO 8601-1:2019, Date and time - Representations for information interchange - Part 1: Basic rules*. 2019. https://www.iso.org/standard/70907.html **Relationship:** Adjacent civil-time representation standard; comparison separates notation from governance of calendars and epochs.

**[E2]** Leslie Lamport. "Time, Clocks, and the Ordering of Events in a Distributed System." *Communications of the ACM* 21(7), 1978, pp. 558-565. DOI: 10.1145/359545.359563. https://lamport.azurewebsites.net/pubs/time-clocks.pdf **Relationship:** Foundational predecessor for partial order, causality, and distributed event ordering.

**[E3]** Ben Laurie et al. *Certificate Transparency Version 2.0*. RFC 9162, 2021. https://www.rfc-editor.org/rfc/rfc9162 **Relationship:** Adjacent append-only Merkle-log standard for inclusion and consistency evidence.

**[E4]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

### Ableman corpus

**[A1]** Adam Ableman. *Cryptographic Phase: Declared Time, Semantic Stability, and Epochal Identity*. Ableman Corpus current edition; work identity `PAPER.PUB.18503394`;  
source SHA-256  
`B8A014E0860027477AC8A6066B9501F0C5B8FE011D8E5425E50AA5833168CD89`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Constitutional Synchronization*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-012675C952D76CD2`;  
source SHA-256  
`A2147B7E6431FF6EEC1C6CE6D7A1EB644B04E37402E9514495C83909565F93C1`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Ableman Constitutional Governance*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-79353AF163A4B0F1`;  
source SHA-256  
`FB0D9B2D3D54168FFE70B24308D1B2766D6D663ED24502D475E975939BE97C8B`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Governance Engineering*. Ableman Corpus current edition; work identity `PAPER.PUB.18749870`;  
source SHA-256  
`372169F315D192733856B1F4A3F1038BBC73F57CF3ED9ACABAE72B965A69C8D0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Blackburn, Bonnie, and Leofranc Holford-Strevens. *The Oxford Companion to the Year.* Oxford University Press, 1999.

Comte, Auguste. *Positivist Calendar.* 1849.

Erasmus, Robert. *Global Decimal Calendar.* 2013.

Ableman, Adam. *Ableman's Razor: A Typed Grammar for Ontology Exploration, Configuration Collapse, and Implementation Feedback.* Zenodo, 2026. doi:10.5281/zenodo.18113475

Richards, E. G. *Mapping Time: The Calendar and Its History.* Oxford University Press, 1998.

Romme, Gilbert. *French Republican Calendar Reforms.* National Convention of France, 1793.

Zerubavel, Eviatar. *The Seven Day Circle.* University of Chicago Press, 1989.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20400858](https://doi.org/10.5281/zenodo.20400858)
