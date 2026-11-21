# Classified Earthworks

## A Governed Materials-Intelligence Architecture for Soil Recovery, Hydroengineering, and Landscape Restoration

### Screening and separation can concentrate hazards and create wastewater, dust, emissions, or residuals.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Classified Earthworks is a proposed field-scale architecture for turning heterogeneous soil, excavation spoil, sediments, mineral fines, and biomass into source-traceable material classes whose possible uses are bounded by sampling, testing, transformation, engineering review, and continuing evidence. It joins materials recovery to landscape water design and makes each excavation both a custody event and a potential observation of soil, geology, and hydrology.

The system is not a claim that local material is safe, that firing preserves its chemistry, that infiltration is desirable at every site, or that a passport certifies performance. Source material can be heterogeneous, contaminated, unstable, saline, reactive, culturally sensitive, legally restricted, or unsuitable for reuse. Screening and separation can concentrate hazards and create wastewater, dust, emissions, or residuals. Hydrologic interventions can mobilize contamination, destabilize slopes, damage habitat, or affect downstream rights.

This paper defines a batch and use-class contract, custody chain, decision outcomes, transformation boundaries, material passport, safety and professional-authority gates, data-governance model, pilot evidence ladder, and realization funnel. Its central contribution is a governed routing architecture: material is characterized and assigned only to uses supported by the evidence and jurisdiction of a declared project profile.

## Source, Evidence, and Standing

This is an AI-assisted integrated edition derived from one exact author manuscript. Its custody and comparison manifest is   
`work/paper-saturation-v1/evidence/classified-`

`earthworks/integration-custody-`  
`manifest.v0.1.json`,  
SHA-256  
`3C9EAA862406B663ED627C1470B128304C0BF0975A8A26100E216EEA5F86D612`. The source remains unchanged.

The platform concept, product lines, applications, passport, data tiers, pilot path, metrics, and vision are author material. Formal contracts, safety qualifications, corpus integrations, tests, and decisions are AI editorial or synthetic candidates until adopted. No material, site, product, treatment, threshold, or deployment is approved here.

## 1. The Materials-Intelligence Thesis

Earthwork projects commonly encounter material described only as dirt, fill, fines, mulch, sediment, or waste. These names conceal origin, composition, variability, contamination, geotechnical behavior, hydrologic effect, biological maturity, and legal status.

Classified Earthworks proposes a disciplined alternative:

$$
\begin{aligned}
&source \\
&\rightarrow custody \\
&\rightarrow sample \\
&\rightarrow characterize \\
&\rightarrow classify \\
&\rightarrow transform? \\
&\rightarrow verify \\
&\rightarrow route \\
&\rightarrow monitor
\end{aligned}.
$$

The question is not how to reuse everything. It is which use, treatment, isolation, disposal, or non-use outcome is justified for each bounded batch.

## 2. Batch and Use-Class Contract

Represent a batch as:

$$
B=(id,S,C,H,T,U,R,W),
$$

where $id$ is batch and lineage identity, $S$ source and custody, $C$ measured composition, $H$ heterogeneity and uncertainty, $T$ tests and methods, $U$ candidate uses and prohibitions, $R$ regulatory and professional-review status, and $W$ observations, witnesses, and monitoring.

A proposed use $u$ is admissible only under a project profile $p$ and current evidence $e$:

$$
\begin{aligned}
Admit(B,u,p,e)\in\{&APPROVE, CONDITIONAL, HOLD, RETEST, REPROCESS, ISOLATE, \\
&DISPOSE, NOT\_COVERED\}
\end{aligned}.
$$

`APPROVE` means approved only within the specified profile, quantity, placement, epoch, and maintenance conditions. A material passport records the decision; it does not create the authority or evidence behind it.

## 3. Classification Is Sampling-Bound

Mixed earth and biomass are spatially and temporally heterogeneous. A sample result applies only under its sampling design, custody, laboratory method, detection limits, batch definition, and uncertainty. One clean aliquot cannot certify a pile.

The program should define segregation before sampling, representative and targeted sampling, duplicate and blank strategy where appropriate, hold times, chain of custody, laboratory competence, resampling triggers, and how material movement invalidates or subdivides a batch.

Unknown or suspect material remains segregated. Absence of a detected contaminant is not proof of universal cleanliness.

## 4. Routing Architecture

Inputs may include topsoil, subsoil, excavation spoil, bedrock grindings, storm sediment, rocks, gravel, green waste, forestry residues, compost or mulch fines, and imported amendments. Their candidate routes include direct reuse, blending, physical separation, biological treatment, thermal transformation, structural evaluation, controlled isolation, remediation, or regulated disposal.

Routing must preserve mass balance. The process cannot count only desirable products while ignoring wash water, sludge, dust, oversize, ash, rejected biomass, emissions, concentrated contaminants, or energy and water consumption.

Every output becomes a new batch with parent lineage and new test requirements.

## 5. Fines: Value and Hazard

Fine particles can provide mineral surfaces, water retention, nutrient interaction, or feedstock value. They can also seal pores, clog drainage, mobilize contaminants, create dust, shrink or swell, and alter structural behavior.

The source principle "Keep the chemistry. Change the geometry" is too strong for transformation. Firing can change mineral phases, porosity, leachability, volume, and emissions. Composting, pyrolysis, pelletizing, washing, and inoculation can also change chemistry and biology.

A safer design principle is:

> Preserve recoverable function where testing supports it; govern every change in chemistry, biology, and geometry.

## 6. Candidate Product Lines

### 6.1 Fired Mineral Granules

Mineral fines may be evaluated as feedstock for porous or graded aggregate. Suitability depends on mineralogy, contaminants, firing regime, energy, emissions, dust, expansion or shrinkage, strength, abrasion, leaching, freeze-thaw behavior, and field compatibility. The source's claimed drainage, buffering, or root-zone benefits remain hypotheses until tested against conventional media.

### 6.2 Organic Pellets and Compost Products

Organic fractions require source control and tests appropriate to maturity, pathogens, contaminants, salinity, nutrients, phytotoxicity, decomposition, odor, vectors, oxygen demand, and storage. Pellet shape does not make an unsafe or unstable feedstock suitable.

### 6.3 Biochar and Blends

Biochar performance depends on feedstock, process conditions, contaminants, particle size, charging, soil, climate, and use. Claims about carbon permanence, filtration, drought resilience, or microbial benefit require bounded evidence. Pyrolysis also creates process hazards and co-products that must remain inside the mass and emissions balance.

### 6.4 Mineral Fill and Drainage Media

Structural, slope, retaining, road, drainage, and infiltration uses require project-specific geotechnical and civil engineering. Organic-rich or degradable material is excluded unless the design and evidence explicitly allow it. Classification does not replace compaction control, stability analysis, hydraulic design, or inspection.

## 7. Hydroengineering Boundaries

Landscape water design seeks to slow, route, store, infiltrate, reuse, or safely overflow water. Those objectives can conflict. Infiltration may be harmful where contamination, unstable slopes, expansive soils, high groundwater, vulnerable aquifers, buried infrastructure, cultural resources, or downstream impacts are present.

A project should declare water sources, design storms and exceedance, inflow quality, pretreatment, hydraulic loading, overflow and safe-failure paths, inspection, maintenance, drought and fire behavior, monitoring, and responsible authority.

No terrace, swale, basin, recharge gallery, drain, or subsurface work is authorized by the conceptual example in this paper.

## 8. Geologic Intelligence Without Extraction

Excavation can yield useful observations of horizons, parent material, moisture, particle distribution, plasticity, density, mineralogy, groundwater, and contamination. A data event should bind observation method, spatial precision, uncertainty, access, ownership or stewardship, and permitted use.

More data is not automatically beneficial. Parcel-level findings can create health, liability, land-value, mineral, groundwater, sovereignty, ecological, archaeological, or security consequences. Sampling plans must address notice, consent where applicable, Indigenous and tribal governance, cultural-resource procedures, public-health escalation, retention, correction, and deletion or restriction where law permits.

The system should read earth without claiming an unrestricted right to extract data from land or communities.

## 9. Material Passport

A passport should include:

- batch, parent, source, custody, mass or volume, and segregation history;
- sampling plan, laboratory, methods, dates, detection limits, results, and uncertainty;
- transformations, additives, process parameters, emissions or residual disposition;
- use classes, prohibited uses, spatial and temporal limits, and expiry or retest triggers;
- regulatory and professional reviews;
- placement location and responsible custodian;
- monitoring, maintenance, observed performance, incidents, and revisions; and
- access class, community or data obligations, and audit history.

Passport identity is not certification. A use claim is bounded by its evidence and may be suspended when lineage breaks, conditions change, or monitoring fails.

## 10. Custody, Witness, and Governed Meaning

**A Formal Theory of Work Custody** supplies a useful separation between work identity, custodian, transfer, and completion. Here, every batch and sample requires an attributable custodian across intake, segregation, laboratory transfer, transformation, storage, transport, placement, and monitoring.

**Governance Witnesses** clarifies that a receipt records an observation under a regime; it does not prove the full material claim. Laboratory results, scale records, process logs, photographs, placement inspections, sensors, and community reports have different scopes.

The **Governed Meaning Base (GMB)** can retain exact methods, batches, passports, use-class definitions, evidence, disputes, and revision lineage. The universal **GSM** can type source-of, sampled-by, transformed-into, tested-under, approved-for, prohibited-for, placed-at, monitored-by, and supersedes relations without turning an edge into safety.

## 11. Corpus Role

**Classified Earthworks** is the materials-intelligence and routing platform. **Hydroengineering and Geologic Intelligence Modules** is the broader companion for landscape sensing, design, and modular system architecture. Work Custody governs batch responsibility; Governance Witnesses governs observation claims.

The interface is strong, but the works should remain identity-distinct. The applied domain does not create general authority for AMCS infrastructure, and the semantic architecture does not certify environmental practice.

## 12. Realization Funnel

$$
\begin{aligned}
&Possibility \\
&\rightarrow Specification \\
&\rightarrow CM_1 \\
&\rightarrow CM_2 \\
&\rightarrow IC \\
&\rightarrow IR \\
&\rightarrow Evidence \\
&\rightarrow Revision
\end{aligned}.
$$

- **Possibility:** enumerate direct reuse, separation, transformation, isolation, disposal, centralized, mobile, and no-action alternatives.
- **Specification:** define batches, sampling, tests, use classes, custody, safety, data rights, decisions, and evidence.
- **CM1:** retain technically, legally, environmentally, and socially admissible configurations, including conservative disposal.
- **CM2:** prefer configurations by safety, performance, reversibility, lifecycle impacts, local value, cost, and community acceptability.
- **IC:** select an Instance Constitution or Instance Configuration for one site, jurisdiction, material stream, and responsible team.
- **IR:** produce an Instance Realization or Implementation Realization of facilities, procedures, equipment, data systems, and monitoring.
- **Evidence:** validate each product, site, operation, claim, and failure response.
- **Revision:** update classifications, passports, configurations, and realizations from field evidence.

This paper reaches Specification and sketches CM1/CM2. It does not select an IC, produce an IR, or authorize a pilot. Realization-stage IR remains distinct from Intermediate Representation in MCIR and related compiler contexts.

## 13. Pilot Evidence Ladder

Before field deployment, an authorized program would need sequential gates:

1. desk review of jurisdiction, standards, hazards, rights, and alternatives;
2. bounded feedstock and sampling study;
3. laboratory characterization and transformation trials;
4. mass, water, energy, emissions, and residual balance;
5. product-specific bench tests and comparator controls;
6. contained test cells with recovery and disposal plans;
7. independently reviewed small field demonstration;
8. monitored scaling with stop, quarantine, recall, and remediation capacity.

Each gate can refuse continuation. Success in one feedstock, site, or use class does not transfer automatically.

## 14. Evaluation Program

Measure sampling representativeness, classification error, contaminant capture, mass closure, water and energy demand, emissions, residuals, worker exposure, product variability, leaching, durability, hydraulic behavior, clogging, structural behavior, vegetation outcomes, ecological effects, maintenance, failure recovery, data-access compliance, community impacts, and lifecycle cost.

Compare each proposed product and intervention with no-action, conventional disposal, conventional imported material, and simpler local-reuse alternatives. Report failures, rejected batches, and uncertain outcomes alongside reuse rate.

## Governed Material-Routing Domain Architecture

Across the completed P1 corpus, Classified Earthworks is the **governed material-routing domain architecture for soil, spoil, sediment, mineral fines, biomass, transformed products, and site-specific use decisions**. It applies general custody, witness, admissibility, and meaning-base machinery to material recovery without creating new safety authority or treating classification as certification.

- **Adjacent work:** *Technical Brief: Classified Earthworks System*  
  **Supplies:** Concise system and deployment framing.  
  **Classified Earthworks boundary:** The paper supplies the deeper material, evidence, safety, and refusal model.

- **Adjacent work:** *Technical Brief: Hydroengineering and Geologic Intelligence Modules*  
  **Supplies:** Landscape-water and geologic observation modules.  
  **Classified Earthworks boundary:** Those modules are adjacent applications, not proof that a batch or intervention is safe.

- **Adjacent work:** *A Formal Theory of Work Custody*  
  **Supplies:** Custodian, transfer, acceptance, return, and terminal disposition.  
  **Classified Earthworks boundary:** Material and sample custody specialize the general work-custody protocol.

- **Adjacent work:** *Governance Witnesses*  
  **Supplies:** Typed observations, methods, environments, and claim ceilings.  
  **Classified Earthworks boundary:** Tests and monitoring become witnesses without certifying the whole batch.

- **Adjacent work:** *Reasoning by Way of Receipts*  
  **Supplies:** Durable records of sampling, transformation, decision, placement, and revision.  
  **Classified Earthworks boundary:** Receipts preserve the route but do not create professional or regulatory authority.

A routing decision should bind:

$$
\begin{aligned}
R= (&batch, lineage, sampling, tests, uncertainty, \\
&transformation, mass\_balance, use\_class, jurisdiction, \\
&authority, decision, placement, monitoring, residuals)
\end{aligned}.
$$

Every transformation creates a successor batch and a new evidence burden. Sampling, laboratory results, engineering review, regulatory disposition, material passport, placement, and monitored performance are different postures. No one posture substitutes for the others. `ISOLATE`,  
`DISPOSE`, `RETEST`,  
and `NOT_COVERED` remain successful governed outcomes when reuse is not justified.

The architecture should preserve the full mass, water, energy, emission, and residual balance. A high reuse rate that omits sludge, dust, wash water, concentrated contaminants, rejected biomass, or downstream harm is a routing failure. Site and community data also remain governed objects with access, retention, correction, and disclosure boundaries.

The universal GSM can type `ORIGINATES_AS_BATCH`, `SAMPLED_UNDER_PLAN`, `TESTED_BY_METHOD`,  
`TRANSFORMED_INTO_BATCH`, `RETAINS_MASS_BALANCE`, `CANDIDATE_FOR_USE_CLASS`,  
`REFUSED_FOR_USE`, `PLACED_UNDER_AUTHORITY`, `MONITORED_FOR_PERFORMANCE`,  
and   
`LEAVES_MATERIAL_RESIDUAL`. These relations make the architecture inspectable without converting a semantic edge into environmental evidence.

This integration establishes four editorial commitments: classify the work as a governed material-routing domain architecture; adopt the routing-decision envelope; require successor-batch and full-balance accounting; and preserve non-use, disposal, privacy, professional authority, and site-specific refusal as first-class outcomes.

## Decision Context and Evidence-Path Assurance

The fixed-seed comparison with Agentic Interface Surfaces, CCM, Project57, and *Testing for Deriving Observable State of Software Systems* adds one material contract and one explicit non-relation. A material-routing decision is only as bounded as both the active decision context and the evidence path supporting the batch claim.

$$
\begin{aligned}
D= (&batch, use\_proposal, context\_snapshot, evidence\_path, \\
&authority, decision, effect, monitoring, expiry, reopen)
\end{aligned}.
$$

CCM supplies the task-relative context in which lineage, sampling, tests, jurisdiction, site conditions, and use criteria were selected. The observability profile tests whether laboratory, sensor, custody, derivation, display, and monitoring evidence actually reaches the decision under declared latency and independence. A current-looking dashboard cannot repair a missing sample plan, circular oracle, inaccessible raw record, or stale site condition.

AIS may expose lawful routing steps, refusals, evidence gaps, and recovery to an operator or agent. Recognition of a completed workflow step remains distinct from professional review, regulatory permission, material safety, and observed post-placement performance.

The randomized adjacency to Project57 produces   
`NO_MATERIAL_RELATION`. Both works use protocols, controlled conditions, instruments, and receipts, but those abstractions are already supplied by general experimental and evidentiary machinery. The response-level meta-binding construct and the material-routing domain do not gain a direct semantic dependency merely from procedural resemblance.

The universal GSM can type   
`BINDS_MATERIAL_DECISION_CONTEXT`,  
`ASSURES_BATCH_EVIDENCE_PATH`, `EXPIRES_SITE_SPECIFIC_EVIDENCE`,  
`REOPENS_AFTER_MONITORING_SIGNAL`,  
`RECOGNIZES_ROUTING_STEP_WITHOUT_SAFETY_`  
`CERTIFICATION`,  
and   
`HAS_NO_MATERIAL_RELATION_TO_PROJECT57_`  
`CONSTRUCT`.

This randomized review adds three open editorial questions: adopt the decision-context/evidence-path contract; require evidence expiry and reopening rules for site-specific routing; and record Project57 as a reviewed no-material-relation adjacency rather than manufacturing a corpus link.

## From Material Identity to Site Effect and Recall

Five retained downstream uses show that Classified Earthworks is the parent material-routing architecture, not a generic metaphor. The reader-facing technical brief projects it. The hydroengineering and geologic-intelligence brief specializes it for site and water decisions. CCM binds the active decision context. AIS exposes lawful next steps without certifying them. Observable-state testing checks whether sampling, laboratory, custody, sensor, placement, and monitoring evidence reaches the decision. Other screened analogies, including Project57 and frozen-compiler comparisons, do not create material-domain dependencies.

The complete material-to-site chain is:

$$
\begin{aligned}
M= (&parent\_batch, successor\_batch, sample, classifier, \\
&route, transformation, use\_proposal, site, context, \\
&professional\_review, regulatory\_standing, release, \\
&transport, placement, observed\_effect, monitoring, \\
&recall, remediation)
\end{aligned}.
$$

Each posture has a separate ceiling. Laboratory classification does not establish engineering suitability. Suitability does not establish legal permission. Permission does not establish operational release. Release does not prove correct transport or placement. Placement does not prove performance. A material passport carries the chain and its restrictions; it is not any one of those decisions.

Batch split, blend, transformation, movement, and storage create lineage events that may change representativeness or use validity. Site selection creates a new Instance Constitution or Instance Configuration whose evidence cannot be inferred from the feedstock alone. Monitoring must be able to reopen the release, locate affected successor batches and placements, quarantine remaining material, issue a recall, and bind remediation responsibility. A clean aggregate reuse percentage cannot close the program while residual mass, water, emissions, rejected fractions, or placed failures remain unresolved.

The universal GSM can type   
`SPLITS_MATERIAL_BATCH`, `BLENDS_WITH_NEW_EVIDENCE_BURDEN`,  
`CLASSIFIES_WITHOUT_RELEASING`, `SELECTS_SITE_SPECIFIC_IC`,  
`RELEASES_UNDER_DISTINCT_AUTHORITY`, `OBSERVES_PLACED_EFFECT`, `REOPENS_MATERIAL_DECISION`,  
`RECALLS_SUCCESSOR_BATCH`, and   
`RETAINS_REMEDIATION_CUSTODY`.

This reverse-dependency review establishes four editorial commitments: adopt the full material-to-site chain; separate classification, suitability, permission, release, placement, and performance; require lineage-aware reopening and recall; and preserve residual balance and remediation custody through terminal disposition.

## 15. Counterevidence and Failure Modes

The proposal should be narrowed or rejected where: (1) a sample is treated as a pile; (2) heterogeneity is omitted; (3) nondetection is called clean; (4) source custody breaks; (5) suspect material is mixed; (6) dilution masks contamination; (7) separation concentrates untracked hazards; (8) wash water or sludge is omitted; (9) dust or worker exposure is omitted; (10) firing is said to preserve chemistry; (11) firing changes leachability adversely; (12) energy or emissions exceed benefits; (13) granules abrade or fail; (14) organic products are immature or contaminated; (15) biochar claims fail for the feedstock; (16) structural use lacks engineering; (17) slope stability worsens; (18) infiltration mobilizes contamination; (19) groundwater or downstream rights are harmed; (20) overflow is undersized; (21) extreme events exceed safe failure; (22) basins clog; (23) salinity accumulates; (24) habitat or cultural resources are damaged; (25) passport is mistaken for certification; (26) batch lineage breaks; (27) monitoring is absent; (28) recall or remediation is impossible; (29) private data becomes public; (30) public-health findings are suppressed; (31) tribal or community governance is bypassed; (32) product claims lack comparators; (33) reuse percentage hides residuals; (34) lifecycle cost exceeds alternatives; (35) GMB inclusion becomes validation; (36) GSM relations imply safety; (37) corpus works are merged; (38) a specification is presented as implemented; (39) cited practitioners are treated as endorsers; or (40) external research, law, or standards contradict feasibility.

## Classify for Bounded Routing, Including Isolation and Non-Use

### Public orientation

Classified Earthworks is the domain architecture behind the reader-facing technical brief. It treats excavation and landscape material as exact batches whose source, custody, sampling, composition, heterogeneity, hazards, transformations, candidate uses, professional review, destinations, monitoring, and recall remain linked. Its objective is justified routing, not universal reuse.

### Adversarial tests

1. **Representative-sample attack.** Limited samples erase spatial, depth, temporal, handling, moisture, and transformation heterogeneity.
2. **Screening-concentration attack.** Separation creates hazardous fines, dust, wash water, emissions, leachate, or concentrated contaminants omitted from useful-product accounting.
3. **Treatment-cleanliness attack.** Heat, composting, washing, blending, or biochar processing is assumed to destroy or immobilize every relevant hazard.
4. **Use-class-transfer attack.** Evidence for one batch, site, exposure route, engineering function, crop, or jurisdiction is reused elsewhere.
5. **Infiltration-good attack.** Water retention or infiltration is treated as beneficial despite contamination transport, slope, habitat, structure, groundwater, and downstream-right effects.
6. **Passport-certification attack.** A material passport is treated as legal release, professional approval, safety certification, or performance guarantee.
7. **Recovery-pressure attack.** Circularity and waste-reduction goals discourage isolation, disposal, refusal, or leaving culturally and ecologically sensitive material undisturbed.
8. **Data-extraction attack.** Excavation intelligence becomes a route to collect, commercialize, or disclose geological, cultural, property, ecological, or community knowledge without authority.

### Claim and evidence ceiling

The paper specifies a governed materials-intelligence architecture, batch contract, routing outcomes, passport, pilot ladder, and evaluation program. It approves no material, threshold, test panel, transformation, product, site, intervention, or deployment. It does not establish safety, efficacy, structural performance, agronomic benefit, remediation, circularity, economics, regulatory compliance, or environmental improvement.

Any physical work requires exact batch and site evidence, accredited methods where applicable, full residual and exposure accounting, qualified domain review, affected-community and Indigenous-data obligations, safe handling and failure plans, recall capability, and separate authority. No testing or implementation occurred in this pass.

### Reader-facing consequence

The architecture should make the non-use outcomes as visible and legitimate as reuse: route, condition, pilot, defer, refuse, isolate, remediate, dispose, or leave undisturbed according to exact evidence and jurisdiction.

## 17. Conclusion

Classified Earthworks offers a compelling integration: treat disturbed earth and biomass as heterogeneous materials requiring evidence, and treat each handling step as both a custody event and an opportunity to learn about land and water.

Its value depends on disciplined refusal. Some batches should be isolated or disposed. Some sites should not infiltrate. Some data should not be public. Some transformations will not outperform conventional alternatives. A regenerative materials platform becomes credible when it can prove not only what material may become, but why a particular use is warranted, who bears responsibility, what remains unknown, and how the decision can be revised.

## Reference and Verification Note

No external source was searched in this pass. Further evidentiary strengthening requires authorized primary-source review of soil science, geotechnical and civil engineering, hydrology and hydrogeology, environmental chemistry and toxicology, contaminated materials and waste law, ceramics, composting, biochar and pyrolysis, lifecycle assessment, worker safety, ecological restoration, stormwater and recharge design, Indigenous and tribal data governance, cultural resources, material-passport standards, and the practitioners named in the source.

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm1.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.
- **Possibility Space.** The present paper does not claim a complete possibility space treatment. That stage remains successor work and cannot be inferred from the architecture described here.
- **Revision.** The present paper does not claim a complete revision treatment. That stage remains successor work and cannot be inferred from the architecture described here.

## Corpus-Wide Reference Positioning

This paper argues that classified Earthworks is a proposed field-scale architecture for turning heterogeneous soil, excavation spoil, sediments, mineral fines, and biomass into source-traceable material classes whose possible uses are bounded by sampling, testing, transformation, engineering review, and continuing evidence. Its nearest external comparison fields are earth, governance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Material classes are sampling- and method-dependent; heterogeneous sites, contaminant transport, and regulatory thresholds can defeat a neat classification-to-action mapping. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** U.S. Army Corps of Engineers. *Sediment Investigations*, Engineer Manual EM 1110-2-4000. 14 February 2025. [publications.usace.army.mil source](https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM%201110-2-4000_FINAL_14Feb2025.pdf) **Relationship:** Primary engineering guidance for material characterization and classification; included to ground classification claims in field and laboratory practice.

**[E2]** U.S. Environmental Protection Agency. *Guidance for Cleaning Up Groundwater, Soil and Air at Hazardous Waste Cleanup Facilities*. [epa.gov source](https://www.epa.gov/hw/guidance-cleaning-groundwater-soil-and-air-hazardous-waste-cleanup-facilities) **Relationship:** Primary remediation guidance emphasizing media transfer, exposure, and site-specific cleanup decisions.

**[E3]** Edward R. Griffor et al. *Framework for Cyber-Physical Systems: Volume 1, Overview*. NIST SP 1500-201, 2017. DOI: 10.6028/NIST.SP.1500-201. https://doi.org/10.6028/NIST.SP.1500-201 **Relationship:** Adjacent cyber-physical systems framework for trustworthiness, timing, data, and lifecycle concerns.

**[E4]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

### Ableman corpus

**[A1]** Adam Ableman. *Technical Brief: Classified Earthworks System*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-F4D74EA1DCD91309`;  
source SHA-256  
`3DCF2DFF9430B987F1D4BD8785D9A6ABB6309037FFC65ADA46F58AFD606DFFD8`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Technical Brief: Hydroengineering and Geologic Intelligence Modules*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-066CA7D56F2416A8`;  
source SHA-256  
`396731CC5A67026E88FD6028CD6A553066F7F7C352FA8072CC44389EBB93E94A`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Water: MCIR as the Engineering of Governed Change*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-91A910961BA1B5AF`;  
source SHA-256  
`1C0B814A76E0724FAD8ECC7A71DBBFC55B3C13E8ED03ED6F399496A70C2587CD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

Adam Ableman *Fractal Governance Architecture.* Zenodo, 2026. doi:10.5281/zenodo.20754189

Adam Ableman *Governed Semantic Compilation: Lawful Continuation, Refusal Semantics, and Epistemic Promotion in Large Language Models.* Zenodo, 2026. doi:10.5281/zenodo.18453681

Adam Ableman *MCIR: A Canonical Intermediate Representation for Governed Transformation.* Zenodo, 2026. doi:10.5281/zenodo.21095303

Adam Ableman *Semantic Coordinate Identity Tokenization (SCIT).* Zenodo, 2026. doi:10.5281/zenodo.20532070

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23847484](https://doi.org/10.5281/zenodo.23847484)
