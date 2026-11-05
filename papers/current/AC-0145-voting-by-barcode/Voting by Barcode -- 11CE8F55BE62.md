# Voting by Barcode

## Secret Ballot Security Gaps, Provenance Horizons, Identity-Anonymity Separation, and Unreceipted Authority Transitions for Both Mail-In and In-Person Voting

### Mail-in voting introduces an extended period during which voter identity, ballot custody, verification decisions, and administrative actions remain linked.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Most debates surrounding election integrity focus on fraud, access, turnout, or tabulation accuracy. This paper examines whether mail-in ballots and persistent barcode systems can satisfy verifiable governance standards, or whether they inherently create extended provenance gaps before anonymity is established.

Our analysis examines a different question:

**Can independent parties verify that every consequential decision affecting a ballot was made according to uniform rules before anonymity was established?**

The framework developed here distinguishes between actions that merely occur and actions that produce sufficient evidence to be independently reconstructed, audited, and verified.

An authority receipt is evidence that binds:

* actor
* authority
* object
* operation
* timestamp
* resulting state

An authority receipt must also be tamper-evident and authority-binding, such that the transition cannot later be reinterpreted or altered without detection.

Mail-in voting introduces an extended period during which voter identity, ballot custody, verification decisions, and administrative actions remain linked. During this pre-anonymization period, numerous consequential transitions may occur, including authentication, signature verification, challenge resolution, cure opportunities, acceptance determinations, and chain-of-custody transfers.

A transition is consequential if it can affect whether a ballot is accepted, rejected, delayed, or subjected to differential processing.

Many existing safeguards seek to constrain these processes. Public observers, audits, chain-of-custody procedures, video monitoring, statistical reporting, and legal prohibitions all contribute to transparency.

However, transparency is not equivalent to verifiability.

The principal concern identified in this analysis is therefore not fraud, but the existence of consequential authority transitions occurring before ballot anonymity is established that cannot be independently reconstructed through verifiable evidence.

**Normative Implication:** Under a standard of verifiable governance rather than institutional trust, mail-in ballots combined with persistent barcode systems create structural provenance gaps that are difficult (if not impossible) to close. They are therefore incompatible with full pre-anonymization reconstructability.

## Threat Model

This paper is concerned with verifiability rather than demonstrated misconduct.

It does not argue that abuse has occurred.

It does not estimate the probability that abuse will occur.

It does not require assumptions regarding malicious actors.

Instead, it examines whether independent observers possess sufficient evidence to determine that critical decisions were made according to uniform rules and legitimate authority.

The relevant question is therefore not:

"Did something improper happen?"

The relevant question is:

"Would independent parties possess sufficient evidence to determine whether it happened?"

This distinction is important.

The analysis concerns evidence sufficiency, not intent attribution.

It concerns reconstructability, not accusation.

## Provenance Horizons

Every safeguard possesses a provenance horizon.

A provenance horizon is the point beyond which independent verification ends.

A provenance horizon can be empirically located by identifying the earliest consequential transition in the processing pipeline for which independent observers lack sufficient evidence to reconstruct the transition.

Public observers possess provenance horizons.

Video systems possess provenance horizons.

Audits possess provenance horizons.

Chain-of-custody records possess provenance horizons.

Statistical reports possess provenance horizons.

Legal prohibitions possess provenance horizons.

A safeguard's usefulness is therefore bounded not merely by its existence, but by the extent of its provenance horizon.

The existence of logs does not imply reconstructability. Logs may be incomplete, non-authoritative, non-binding, non-public, or insufficiently granular to determine which transitions occurred under which authority.

The central question is therefore:

**Where does independent verification end relative to the decisions that matter most?**

If consequential acceptance decisions occur beyond the provenance horizon, those decisions remain dependent upon institutional trust rather than independently verifiable evidence.

Election systems generally perform well at demonstrating procedural visibility and outcome auditability.

They are often substantially weaker at demonstrating complete pre-anonymization reconstructability.

## Minimal Completeness Criterion

A voting system satisfies pre-anonymization provenance completeness if every consequential transition prior to identity-anonymity separation produces an authority-bound, tamper-evident receipt sufficient for independent reconstruction.

This criterion does not require disclosure of vote content.

Nor does it require public exposure of sensitive voter data.

It requires that consequential transitions be reconstructable by authorized independent review without relying solely on institutional assertion.

The criterion is intentionally narrow.

It concerns the pre-anonymization period because that is where identity-linked selection decisions occur.

## Identity Exists Before Anonymity

Ballot processing necessarily begins with an identifiable voter.

Before anonymity is established, election systems may access:

* voter registration records
* signature records
* address information
* voting status
* party affiliation where maintained
* demographic information where available

Election laws generally prohibit the use of political affiliation, race, ethnicity, or other protected characteristics in acceptance decisions.

However, prohibition and impossibility are distinct concepts.

The technical infrastructure used to authenticate voters may possess access to information that could serve as demographic or political proxies.

This creates a period during which identity-linked decisions occur before anonymity is established.

The concern is structural rather than accusatory.

Any architecture that permits consequential decisions while identity remains attached creates a decision surface that does not exist after anonymity has been achieved.

## Identity-Anonymity Separation as a Security Property

The security property of a secret ballot is not merely eventual anonymity.

The critical property is demonstrable anonymity.

Identity and vote content must become separated at a verifiable point.

Demonstrable anonymity requires irreversibility, which requires that no technically or procedurally admissible mechanism remains by which identity-to-ballot linkage could be reconstructed within the system or from its retained artifacts

In practice, perfect instantaneous separation may be difficult or impossible to achieve. The relevant objective is therefore to minimize the duration of identity linkage while maximizing the verifiability of the separation point.

Where barcodes, serial numbers, ballot identifiers, envelope identifiers, or other persistent references exist, anonymity depends upon procedural assurances that:

* identity mappings are not retained alongside vote contents
* linkages are destroyed or isolated
* identifiers do not survive into counted ballot records
* reconstruction pathways do not remain available

Mail voting extends the duration of identity linkage.

However, the underlying concern is not unique to mail voting.

Any voting architecture that introduces persistent identifiers faces the same question:

**Can independent parties verify the point at which identity and vote become irreversibly separated?**

Where this separation cannot be independently demonstrated, anonymity itself resides beyond the provenance horizon.

More generally, any system that separates identity from outcome must be able to demonstrate where and how that separation became irreversible. Otherwise anonymity remains an assertion rather than a verifiable property.

## Persistent Identifiers and In-Person Voting

Although mail voting is often the focus of election-integrity debates, the underlying analytical framework applies more broadly.

Many in-person voting systems introduce persistent identifiers at various stages of the voting process.

Examples may include:

* ballot serial numbers
* ballot-on-demand printing systems
* provisional ballot tracking numbers
* scanner-generated records
* digital poll-book associations
* precinct-to-central-tabulation custody records

In some jurisdictions, voter check-in systems, ballot issuance systems, and central scanning systems may temporarily coexist within the same administrative workflow, creating periods in which identity-linked records and ballot-linked records exist simultaneously.

The mere existence of identifiers does not establish a security problem.

The relevant question is whether independent parties can verify that identity-to-ballot linkages are irreversibly severed before vote content enters durable records.

Mail voting extends the duration and complexity of identity linkage.

It does not create the underlying concern.

The broader issue is any architecture in which persistent identifiers and vote records coexist within the same administrative lifecycle.

## Authority Receipts and Silent Identity Transitions

The most significant governance concern arises from transitions that may occur without independently verifiable receipts.

Examples include:

* barcode creation
* barcode assignment
* voter-to-barcode linkage
* database retrieval
* signature verification outcomes
* challenge determinations
* cure notifications
* acceptance decisions
* manual overrides
* linkage severance

Each transition may materially affect ballot status.

Yet the public generally receives no authority-bound receipt describing the transition.

The presence of authority receipts is necessary but not sufficient for provenance completeness. Receipts must also be complete, non-omissible, and resistant to selective generation or suppression. Systems in which transitions can occur without receipt generation, or in which receipts can be selectively withheld, remain subject to the same provenance limitations.

A barcode itself is not an authority receipt.

A barcode may identify, route, retrieve, correlate, or track.

It does not inherently establish:

* who created the linkage
* under what authority the linkage exists
* how the linkage was used
* when the linkage was severed
* whether the linkage was ever combined with vote content

The deeper issue is that persistent identifiers create referential persistence without necessarily creating evidentiary accountability.

An identifier may function as an indexing primitive that permits retrieval and correlation while producing little evidence regarding how those capabilities were exercised.

The result is an accountability asymmetry.

Observers may see ballots move.

Administrators may report outcomes.

Audits may verify totals.

But many of the authority transitions governing those outcomes may remain largely invisible.

## Example of an Authority Receipt

An ideal receipt for a signature-verification decision might contain:

* ballot identifier
* action performed
* verification method
* responsible system or official
* governing authority permitting the action
* timestamp
* resulting status
* integrity verification record

Such a receipt would not reveal vote content.

Its purpose would be to permit independent reconstruction of consequential administrative decisions.

The central question is not whether a particular implementation is practical.

The central question is whether consequential transitions can occur without generating equivalent evidence.

## Risk Category 1: Database Lookup Symmetry

Modern ballot processing relies heavily upon database retrieval.

The same mechanisms capable of retrieving signature records are frequently capable of retrieving additional voter information associated with the same record.

This creates database lookup symmetry.

If an identifier can retrieve one voter attribute, it can potentially retrieve others.

Whether additional attributes are exposed, hidden, ignored, or utilized depends upon software configuration, workflow design, and oversight.

Potential risks include:

* differential scrutiny
* selective review
* asymmetric cure opportunities
* targeted delays
* unequal verification thresholds

The concern is not whether such actions are authorized.

The concern is whether independent parties possess evidence sufficient to demonstrate that they did not occur.

## Risk Category 2: Public Observation and Provenance Horizons

Public observer programs and video monitoring represent meaningful existing safeguards and improve transparency.

Observers may witness:

* ballot intake
* sorting activities
* signature verification procedures
* extraction processes
* tabulation operations

However, observation is not provenance.

Different observers may possess different provenance horizons depending on their level of access. A system achieves public verifiability only if the provenance horizon available to independent external observers encompasses all consequential pre-anonymization transitions.

These safeguards possess clear provenance horizons.

Observers generally cannot verify:

* transportation events before arrival
* database queries executed during barcode scans
* software decision thresholds
* configuration changes
* internal audit logs
* after-hours processing
* post-event log integrity
* historical linkage relationships between identifiers and records

An observable process can still contain substantial segments of authority execution that cannot be independently reconstructed.

Public observation therefore improves transparency while leaving significant portions of decision-making beyond the provenance horizon.

## Risk Category 3: Chain-of-Custody Fragmentation

Ballots pass through multiple custodians before tabulation.

Typical transfer points include:

* voter possession
* collection boxes
* postal systems
* transportation networks
* election facilities
* sorting systems
* verification systems
* extraction teams
* tabulation facilities

Each transfer introduces opportunities for:

* delay
* misrouting
* loss
* unauthorized handling
* selective processing

Existing controls reduce risk.

They do not eliminate provenance gaps.

Most importantly, the public rarely possesses a continuous receipt chain spanning every consequential transfer.

## Risk Category 4: Insider Threats and Attack-Surface Geometry

Insider threats exist in all election systems.

The distinguishing characteristic of expanded mail voting is not the existence of insiders.

It is the geometry of the attack surface.

Mail voting substantially lengthens the pre-anonymization period during which identity-linked decisions may occur.

This increases the number of consequential transitions occurring before anonymity is established.

The theoretical risks described here are not merely hypothetical. In 2000, computer programmer Clint Curtis testified at a U.S. Congressional Hearing that he was contacted by Florida Congressman Tom Feeney and asked to create vote-switching software for Florida's electronic voting machines. Curtis's whistleblower testimony documents that the architecture of black-box voting systems creates vulnerability surfaces that technical insiders can exploit when given opportunity.

This historical precedent is relevant because it confirms a key structural concern: consequential transitions in voting systems can occur without generating verifiable evidence. The same provenance horizon problem this paper identifies for mail-in ballots and barcode systems exists in electronic voting systems where software decisions are not accompanied by authority receipts.

The concern is not necessarily overt misconduct.

The concern is the existence of consequential transitions that remain difficult to independently reconstruct.

## Risk Category 5: Insufficient Provenance of Rejection Statistics

Reported rejection rates are frequently presented as evidence of system integrity.

These figures may be accurate.

However, aggregate outcomes do not constitute provenance.

A rejection statistic does not independently demonstrate:

* how ballots were flagged
* how thresholds were selected
* how overrides occurred
* how cure opportunities were distributed
* whether standards were applied uniformly

A low aggregate rejection rate provides no independent evidence of equal treatment.

Without granular receipts, rejection statistics remain institutional claims regarding outcomes rather than independently verifiable demonstrations of process neutrality.

The question is not merely whether rejection rates are low.

The question is whether the process producing those rates can be independently reconstructed and verified.

## Risk Category 6: Audit Scope Limitations

Election audits perform an important function.

Most focus on confirming that accepted ballots were tabulated correctly.

However, tabulation verification occurs after many consequential transitions have already taken place.

This reveals an important asymmetry.

Election systems often audit aggregation effectively while providing comparatively weaker evidence regarding selection.

Audits may not fully answer:

* Which ballots were challenged?
* Which ballots were flagged?
* Which ballots received discretionary review?
* Which ballots entered cure procedures?
* Which ballots experienced administrative delay?
* Which ballots were never accepted?

A system may accurately count accepted ballots while providing limited visibility into the decisions that determined acceptance.

## Reform Opportunities

The objective of reform is not merely security.

The objective is verifiable governance.

Potential reforms include:

* immutable receipts for consequential processing decisions
* cryptographically verifiable provenance chains
* comprehensive logging of database access
* publicly auditable, tamper-evident records of barcode-to-record interactions during processing, with vote content excluded
* strict separation between verification systems and nonessential voter attributes
* publication of anonymized process metrics
* continuous custody documentation
* independent auditing of automated decision systems
* bipartisan review of verification workflows
* blinded processing wherever feasible

Any reform effort must also acknowledge legitimate tensions between privacy, throughput, legal requirements, and provenance completeness.

These constraints do not imply that full receipt completeness is trivial to achieve, particularly given tensions with ballot secrecy, operational throughput, and legal standards of admissibility.

The objective is not complete visibility.

The objective is maximizing independent verifiability without compromising ballot secrecy.

## Legitimacy and Provenance Integrity

A high-stakes social consent system like voting exposes itself to crushing legitimacy concerns from all sides.

These concerns arise from:

* true incidents that occur
* true structural risks that exist
* unfounded rumors that cannot be readily refuted

The presence of genuine vulnerabilities does not require that all allegations be true.

The problem is that the absence of provenance integrity-based evidence makes it impossible to refute unfounded claims.

When consequential transitions occur beyond the provenance horizon, the system cannot provide the evidence that would be necessary to demonstrate process neutrality.

This creates a self-reinforcing cycle:

* Lack of verifiable evidence -> legitimate skepticism
* Legitimate skepticism -> amplified rumors
* Amplified rumors -> further legitimacy erosion
* Further legitimacy erosion -> demand for more evidence
* More evidence required -> none available

The system then becomes dependent on institutional trust precisely when trust is most strained.

This is not a problem of bad actors alone.

It is a problem of evidentiary architecture.

A system that cannot refute unfounded claims because it lacks the evidence to do so invites perpetual legitimacy crisis by design.

The presence of real vulnerabilities (such as the Clint Curtis case) further compounds this problem by providing grounds for reasonable skepticism that cannot be distinguished from unreasonable allegations.

Without provenance completeness, the system cannot separate the two.

## Conclusion

The central issue examined in this analysis is not whether election fraud has been proven.

Nor is it whether election officials are acting in good faith.

The issue is whether consequential transitions occurring before ballot anonymity is established are independently verifiable.

Mail voting extends the duration and complexity of the pre-anonymization period.

Persistent identifiers in both mail and in-person voting systems create additional questions regarding demonstrable identity-anonymity separation.

Many of the resulting transitions are observable.

Far fewer are independently reconstructable.

The most important question is therefore not whether ballots were ultimately counted.

It is whether every consequential transition affecting those ballots produced sufficient evidence to be independently reconstructed, audited, and verified.

Trustworthy systems are not those that merely report outcomes.

Trustworthy systems are those that make consequential transitions impossible to perform without generating evidence.

The principal challenge identified here is therefore not ballot counting.

It is the existence of provenance horizons within the identity-linked lifecycle of the ballot and the resulting dependence upon institutional trust where independent verification ends.

## Appendix A: Relationship to Ableman Constitutional Systems (ACS)

The analytical framework employed in this paper derives from Ableman Constitutional Systems (ACS), a broader governance and observability framework concerned with authority, admissibility, provenance, and state transitions.

This framework is complementary to end-to-end verifiable voting systems, which focus on ensuring that cast ballots are correctly included in tabulation. The present analysis instead focuses on the evidentiary completeness of pre-anonymization transitions that determine which ballots are accepted into that set.

Within ACS, consequential actions are ideally accompanied by authority receipts that bind actor, authority, object, operation, timestamp, and resulting state. The concepts of provenance horizons, identity-anonymity separation, and authority receipts used throughout this paper are applications of those broader principles to election administration.

The arguments presented in this paper do not depend upon acceptance of ACS as a complete framework. They may instead be interpreted more generally as claims regarding observability, accountability, provenance, and independent verification within complex administrative systems.

\newpage

## Appendix B: Formalization Sketch

Let $S_t$ denote system state at time $t$.

Let $T_i$ denote a consequential state transition.

Let $R_i$ denote the evidence associated with $T_i$.

A transition is independently reconstructable over an interval if sufficient evidence exists to uniquely infer the transition from the resulting record.

A system is independently reconstructable over interval $[t_0, t_n]$ if every consequential transition in that interval has a corresponding record sufficient for independent reconstruction.

A provenance horizon occurs wherever consequential transitions exist for which sufficient reconstructive evidence is unavailable.

Under this formulation, a system approaches provenance completeness as the set of consequential transitions lacking corresponding evidence approaches zero.

The central analytical question becomes whether critical pre-anonymization transitions occur before or after the provenance horizon.

This formalization is offered only as an interpretive aid. The arguments presented in the main text do not depend upon acceptance of any specific mathematical model.

## Corpus-Wide Reference Positioning

This paper argues that most debates surrounding election integrity focus on fraud, access, turnout, or tabulation accuracy. Its nearest external comparison fields are voting, crypto. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Auditability and cryptographic verification must coexist with ballot secrecy, accessibility, coercion resistance, dispute procedures, and operational chain of custody. A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** U.S. Election Assistance Commission. *Voluntary Voting System Guidelines, Version 2.0*. 2021. [eac.gov source](https://www.eac.gov/documents/voluntary-voting-system-guidelines-version-20) **Relationship:** Adjacent voting-system standard for auditability, software independence, evidence, accessibility, and dispute resolution.

**[E2]** Ben Laurie et al. *Certificate Transparency Version 2.0*. RFC 9162, 2021. https://www.rfc-editor.org/rfc/rfc9162 **Relationship:** Adjacent append-only Merkle-log standard for inclusion and consistency evidence.

**[E3]** Jerome H. Saltzer and Michael D. Schroeder. "The Protection of Information in Computer Systems." *Proceedings of the IEEE* 63(9), 1975, pp. 1278-1308. DOI: 10.1109/PROC.1975.9939. https://doi.org/10.1109/PROC.1975.9939 **Relationship:** Foundational protection principles used as a comparison point for least authority, mediation, and inspectability.

**[E4]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E5]** Anders Rundgren, Bret Jordan, and Samuel Erdtman. *JSON Canonicalization Scheme (JCS)*. RFC 8785, 2020. https://www.rfc-editor.org/rfc/rfc8785 **Relationship:** Adjacent canonicalization standard relevant to stable cryptographic commitments.

**[E6]** Manu Sporny et al., eds. *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 19 July 2022. https://www.w3.org/TR/did-core/ **Relationship:** Adjacent decentralized identity standard; identifier resolution is not assumed to settle semantic standing or jurisdiction.

**[E7]** Juan Benet. "IPFS - Content Addressed, Versioned, P2P File System." 2014. arXiv:1407.3561. https://arxiv.org/abs/1407.3561 **Relationship:** Predecessor content-addressed network architecture; content identity is compared with, not treated as sufficient for, semantic jurisdiction.

### Ableman corpus

**[A1]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Cryptographic Admissibility and Jurisdiction*. Ableman Corpus current edition; work identity `PAPER.PUB.20602448`;  
source SHA-256  
`6094338D8706F63E8787A5E8DCF40F8A651C0FC3E5EA776DD61791566D094D38`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *The Three Hash Rule*. Ableman Corpus current edition; work identity `PAPER.PUB.20788617`;  
source SHA-256  
`F6FA73D083B70711A8C817F7779751D1506FEBA0E356DB9805BB1570663731B5`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Constitutional Semantic Hashing: Governed Commitment Schemes for Semantic Provenance, Admissibility, and Constitutional Continuity*. Ableman Corpus current edition; work identity `PAPER.PUB.20248734`;  
source SHA-256  
`B1DAC3E2CD4D57BAFBF6462BA6ACFFF7CF120CDB7FA37D0C173525744CC0A2F0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Self-Certifying Proof-Carrying Identity for Registrar-Free Namespace Networks*. Ableman Corpus current edition; work identity `PAPER.PUB.20114888`;  
source SHA-256  
`1AFDBD390D3BF28224727FE150FFB30CA1810D997778CC8702B6CD20C4FA5B45`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Semantic Hashing: Hashes as Declared Equivalence Classes of Meaning*. Ableman Corpus current edition; work identity `PAPER.PUB.18500533`;  
source SHA-256  
`7DA63A76DDF492FFC289F486923FB430879DC148CF3BB16EB0E755E2D4AB9C14`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *Governed Authority Chains for International Trade*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-B6ABC7DDD0E90CEB`;  
source SHA-256  
`E46132D7DB5B0C5B12615AAFBD64512C3EF9F87CB280FDEFC6B9543360147BE1`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20672054](https://doi.org/10.5281/zenodo.20672054)
