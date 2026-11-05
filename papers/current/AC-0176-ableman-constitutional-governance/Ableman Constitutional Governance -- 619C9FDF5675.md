# Ableman Constitutional Governance

## Interpretation, Admissibility, Authority, and Lineage in Identity-Bearing Systems

### How anything remains itself while becoming something new.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract
Systems change. Software is updated, constitutions are amended, models are realized, certificates are rotated, artifacts are replicated, standards are superseded, and institutions acquire successors. Yet change alone does not establish continuity. Ableman Constitutional Governance, or ACG, proposes that governed continuity requires four jointly necessary functions: an Interpretation Regime establishing what the governed object is and what counts as preserving its identity; an Admissibility Law distinguishing legitimate transformation from arbitrary mutation; an Authority Binding making that law operative rather than advisory; and Lineage Continuity relating predecessor, transformation, and successor through time. ACG was developed as a governance discipline, but its recurrence across model realization, execution, custody, kernel design, software succession, regulatory modification, standards processes, cryptographic trust, and scientific versioning suggests a broader hypothesis: ACG may describe the minimum constitutional form required whenever a system claims that a changed object is the legitimate continuation of a prior object. This paper develops that hypothesis, distinguishes the four functions through natural ablations, explains why fused rival models lose diagnostic power, and argues that kernelization is a specialized application of ACG because an operative kernel must define inherited identity, admissible descendants, binding conformance authority, and version lineage. Preliminary external validation found substantial cross-domain support. A frozen v0.1 instrument produced 69 of 72 exact judgments across two same-session passes. A contamination-declared coder from a different model family later agreed on 65 of 72 and 68 of 72 judgments against those passes, with minimum component kappas of 0.857 and 0.880, respectively, while finding no candidate falsifier. Those results remain evidence under instrument v0.1 only. A clarified instrument v0.2 is introduced here by explicit supersession for future independent review. The present claim is bounded: ACG is a falsifiable functional-necessity conjecture for governed identity continuity, not yet a universal theorem and not a sufficient condition for safety, justice, liveness, semantic adequacy, or trustworthy execution.

## 1. Introduction: The Problem of Legitimate Continuity

A thing changes. Under what conditions is it still the same thing?

The question appears simple while change is trivial. A file copied without alteration appears to preserve identity. A document with one corrected comma appears continuous with its predecessor. The problem becomes harder when the transformation changes structure, semantics, authority, behavior, location, or institutional standing.

Consider several events:

- a software release replaces an older release;
- a cryptographic key succeeds a revoked key;
- a constitutional amendment modifies governing text;
- a model is compiled into an executable artifact;
- an API representation is migrated into a successor version;
- a regulated device is modified after clearance;
- an artifact is transferred to another storage node;
- a standards body supersedes one recommendation with another.

In each case, a successor may exist. Existence does not establish legitimacy.

A software package may be authentic yet unauthorized. A certificate may be valid yet unrelated to the predecessor it appears to replace. A compiled binary may execute successfully while failing to preserve source meaning. A replicated artifact may possess a valid signature while lacking local recognition. A constitutional amendment may be substantively attractive but procedurally void.

These failures reveal four questions inside every legitimate-continuation claim:

1. What is the object whose identity is said to continue?
2. Which transformations are permitted?
3. What makes those permissions binding?
4. How is the successor related to the predecessor through time?

Ableman Constitutional Governance names the corresponding functions:

$$
\mathrm{ACG} = \mathrm{IR} + \mathrm{AL} + \mathrm{AB} + \mathrm{LC},
$$

where:

- $\mathrm{IR}$ is the Interpretation Regime;
- $\mathrm{AL}$ is the Admissibility Law;
- $\mathrm{AB}$ is the Authority Binding;
- $\mathrm{LC}$ is Lineage Continuity.

The claim is functional. A system need not use these terms. It must, however, perform their equivalents somewhere if it claims operatively that a changed object legitimately inherits the identity, authority, or standing of an earlier object.

The deeper subject of ACG is therefore not governance in the narrow sense of committees, voting, or policy. Its subject is:

> The lawful continuity of identity-bearing systems under transformation.

## 2. The Four Functions of ACG

### 2.1 Interpretation Regime

An Interpretation Regime determines what the governed object is and what it means for that object to remain continuous through change.

It answers questions such as:

- Which properties are identity-bearing?
- Which changes preserve identity?
- Which changes create a new object?
- Is identity attached to bytes, meaning, role, lineage, location, authority, or a combination?
- Which representation is canonical?
- When two representations differ, are they equivalent, corresponding, related, or unrelated?

An Interpretation Regime may use content hashes, canonical serialization, semantic schemas, type identities, accession numbers, legal definitions, name-bearing specimens, repository paths, constitutional texts, model identities, or declared equivalence relations.

Identity is not self-interpreting. A digest can establish that two byte strings are identical. It cannot independently establish that two different byte strings express the same law, implement the same model, or continue the same institutional office. Those conclusions require an interpretation regime appropriate to the claim.

Without $\mathrm{IR}$, a system cannot reliably answer:

> What exactly survived the transformation?

The predicted failure is identity ambiguity: substitution, equivocation, category confusion, or inability to distinguish continuity from resemblance.

### 2.2 Admissibility Law

An Admissibility Law determines which transformations are accepted as legitimate.

It answers:

- Which transitions are allowed?
- Which evidence must precede them?
- Which invariants must remain true?
- Which changes require fresh admission?
- Which operations are forbidden?
- Which failures produce refusal, rollback, or recovery?
- When is a migration adequate?
- When is a successor merely different?

An admissibility law may be expressed as a transition topology, type system, validation rule set, threshold condition, regulatory decision tree, compatibility policy, amendment procedure, or conformance profile.

Without $\mathrm{AL}$, recognized authority can become arbitrary. An actor may be entitled to choose, but the system lacks a principled distinction between an admitted transformation and an authorized mutation.

The predicted failure is transformation arbitrariness:

> The system may know who can decide, but not what makes the decision valid.

### 2.3 Authority Binding

Authority Binding makes the admissibility law operative rather than advisory.

It answers:

- Who may judge admissibility?
- What gives that judgment standing?
- Which keys, roles, institutions, courts, thresholds, or capabilities are recognized?
- Can a violation prevent admission or reduce standing?
- Who may alter the law?
- Who hears appeal?
- What is the jurisdiction of the authority?

Authority may be cryptographic, institutional, procedural, local, federated, capability-based, threshold-based, judicial, or socially recognized.

Authority need not physically prevent every nonconforming act. A person may print a nomenclaturally invalid name. A developer may publish a falsely versioned package. A machine may execute code outside a protocol.

The relevant test is narrower:

> Does the system confer, deny, preserve, or downgrade recognized standing on the basis of the rule?

Without $\mathrm{AB}$, the law may be exact but optional.

The predicted failure is advisory governance: the rule describes what should happen but cannot distinguish earned conformance from self-assertion.

### 2.4 Lineage Continuity

Lineage Continuity relates predecessor, transformation, and successor through time.

It answers:

- Which object preceded this one?
- Is the new object a successor, fork, replacement, rollback, migration, correction, or unrelated artifact?
- Does the predecessor retain historical standing?
- Is the successor backward compatible?
- What was superseded?
- What was revoked?
- Can the system return to an earlier state?
- Does a new version retroactively alter old conformance?

Lineage is not merely chronology. A timestamp list can show that events occurred in sequence. A commit graph can record ancestry. Neither necessarily determines which descendant is the legitimate successor for a declared jurisdiction.

Lineage Continuity therefore requires a typed relation relevant to standing:

$$
\mathrm{Predecessor}
\xrightarrow{\text{admitted transformation}}
\mathrm{Successor}.
$$

Without $\mathrm{LC}$, a system may validate each state individually while remaining unable to distinguish renewal from replacement, supersession from revocation, or migration from substitution.

The predicted failure is succession ambiguity.

## 3. The ACG Necessity Conjecture

Let a system $S$ claim that object $x'$ is the legitimate continuation of object $x$ under transformation $t$.

For that claim to be operative, ACG conjectures that $S$ requires functional mechanisms establishing:

$$
\begin{aligned}
&\mathrm{IR}(x,x') \\
&\land \mathrm{AL}(t) \\
&\land \mathrm{AB}(\mathrm{AL}) \\
&\land \mathrm{LC}(x,t,x')
\end{aligned}.
$$

The terms mean:

- $\mathrm{IR}(x,x')$ identifies the object and continuity relation being claimed;
- $\mathrm{AL}(t)$ determines whether the transformation is admissible;
- $\mathrm{AB}(\mathrm{AL})$ determines why the admissibility judgment has operative standing;
- $\mathrm{LC}(x,t,x')$ binds predecessor, transformation, and successor into a continuing lineage.

This is presently a functional-necessity conjecture. It is not a sufficiency theorem.

An ACG-complete system may still possess an unjust law, corrupt authority, defective implementation, compromised trust root, inadequate interpretation regime, unsafe effect boundary, unavailable service, or fabricated evidence.

ACG asks whether continuity is constitutionally formed. It does not guarantee that the constitution is wise, secure, or good.

## 4. Why the Four Functions Must Remain Distinct

A theory becomes suspicious when it can explain every case only by renaming. ACG gains force from systems in which its components separate naturally.

### 4.1 Identity Is Not Lineage

Content-addressing systems can identify exact immutable objects. Changing the content changes the identifier. Yet an immutable content identifier alone does not say which new identifier is the legitimate successor of the old one.

IPFS Content Identifiers provide content-derived identity. IPNS adds authenticated mutable naming that can point a stable name toward changing content over time [@ipfs-cid; @ipfs-ipns].

Therefore:

$$
\mathrm{IR} \neq \mathrm{LC}.
$$

The question "What is this?" differs from "How does this legitimately follow from that?"

### 4.2 Admissibility Law Is Not Authority Binding

Semantic Versioning provides detailed rules for classifying changes as major, minor, or patch releases. It also defines precedence among version strings. Publishers can nevertheless declare versions without an independent universal court establishing that their classification is truthful [@semver].

Therefore:

$$
\mathrm{AL} \neq \mathrm{AB}.
$$

A law can be precise while remaining advisory.

### 4.3 Validity Is Not Succession

X.509 certification-path validation determines whether a certificate path is valid relative to a trust anchor and defined constraints. It establishes a binding between a subject identity and a public key. Two independently valid end-entity certificates do not thereby form a governed predecessor-successor lineage [@rfc5280].

Therefore:

$$
\mathrm{IR} + \mathrm{AL} + \mathrm{AB}
\nRightarrow
\mathrm{LC}.
$$

A succession relation requires more than repeated validity.

### 4.4 Witness Continuity Is Not Authority over Witnessed Content

Certificate Transparency uses append-only logs, signed tree states, inclusion proofs, and consistency proofs. These mechanisms can demonstrate continuity and detect log equivocation. They do not themselves establish that every logged certificate was legitimately issued [@rfc9162].

Therefore:

$$
\mathrm{ACGComplete}(\mathrm{Log})
\nRightarrow
\mathrm{Authorized}(\mathrm{LoggedObject}).
$$

A witness may possess a complete constitutional structure for its own history without acquiring authority over the events it records.

## 5. ACG and the Mechanics of Constitutional Enforcement

ACG identifies the functions a constitutional transformation requires. Constitutional enforcement concerns how those functions become operative in a machine.

A recurring distinction is the placement of semantics.

A rule may be encoded as checked data:

$$
\mathrm{count} \geq 7,
$$

or as transition topology:

$$
S_0 \rightarrow S_1 \rightarrow \cdots \rightarrow S_7.
$$

A counter can record that seven events occurred while forgetting whether they were distinct or ordered. A state chain can preserve those distinctions through the existence and absence of transitions.

This yields the Semantic Placement Principle:

> Where a meaning lives determines how it can fail.

Data-borne semantics depend on complete and correct checks. Topology-borne semantics constrain valid reachability. When the topology is canonically represented and cryptographically bound to identity, weakening the rule changes the identity-bearing constitutional artifact.

This does not eliminate the nonconforming executor problem. Structural semantics make violations unrepresentable to a conforming executor. Constitutional mediation must additionally ensure that a nonconforming executor cannot silently convert arbitrary behavior into an authorized effect.

ACG and structural enforcement operate at different levels:

- ACG asks which constitutional functions must exist.
- Structural enforcement asks how some functions can be encoded so violations become unreachable to conforming implementations.
- Custody asks whether the exact admitted structure is the structure being used.
- Effect mediation asks whether nonconforming execution can still cause consequential external effects.

No layer silently inherits the standing of another.

## 6. Kernelization as a Specialized Application of ACG

An architecture describes how systems relate. A kernel does something stronger:

> A kernel establishes inherited semantic law for downstream systems.

When a system claims conformance to a kernel, it does not merely understand a shared vocabulary. It agrees that certain distinctions and invariants govern its descendants.

An abstraction becomes kernel-like when it gains:

1. normative inheritance;
2. invariant preservation;
3. conformance adjudication;
4. downstream semantic consequence.

Decomposing those requirements analytically reconstructs the ACG functions.

A kernel must define what counts as an implementation, descendant, mandatory model element, and identity-preserving variation. That is $\mathrm{IR}$.

It must define which mappings, extensions, escapes, and migrations are conforming. That is $\mathrm{AL}$.

It must define who judges conformance, what evidence is required, and what standing a partial conformer receives. That is $\mathrm{AB}$.

It must define version relations, supersession, migration, deprecation, revocation, and historical conformance. That is $\mathrm{LC}$.

This supports the proposition:

> Kernelization is a specialized application of ACG.

More precisely:

> An operative kernel is an ACG-complete model made inheritable.

This is analytic convergence inside the same constitutional-computing corpus, not independent external confirmation. The external recurrence discussed later provides the independent evidence. The kernel analysis contributes internal coherence, explanatory compression, and a practical admission discipline.

## 7. Kernel Inheritance and Conformance

Kernel inheritance does not require identical implementation.

Let $K$ be a kernel and $S$ a downstream system. Conformance requires a mapping:

$$
\phi : S \rightarrow K
$$

such that relevant downstream transitions preserve the kernel's required invariants:

$$
s \rightarrow s'
\implies
\phi(s) \rightarrow_K \phi(s').
$$

The mapping may be bounded to a subset, host profile, execution corridor, artifact class, or optional profile. Conformance should therefore not be binary.

A useful kernel-conformance scale includes:

- `FULL_CONFORMANCE`;
- `BOUNDED_CONFORMANCE`;
- `PROFILE_CONFORMANCE`;
- `ADAPTER_ONLY`;
- `PARTIAL_WITH_LIMITATIONS`;
- `NONCONFORMANT`;
- `UNASSESSED`.

This scale is distinct from the ACG validation instrument's standing classes. Kernel-conformance standing grades a descendant's preservation of an inherited kernel model. ACG validation standing grades whether a continuity mechanism exhibits $\mathrm{IR}$, $\mathrm{AL}$, $\mathrm{AB}$, and $\mathrm{LC}$ within a declared jurisdiction.

- **Vocabulary:** ACG validation standing  
  **Object judged:** Continuity mechanism  
  **Question:** Does it instantiate the four ACG functions?

- **Vocabulary:** Kernel-conformance standing  
  **Object judged:** Downstream implementation  
  **Question:** To what extent does it preserve the inherited model?

An adapter capable of exchanging kernel-shaped artifacts does not necessarily inherit the kernel's internal model. Syntax compatibility cannot be laundered into semantic conformance.

A conformance record should identify:

- kernel identity and version;
- subject identity;
- claimed scope;
- mapping identity;
- preserved invariants;
- declared escapes;
- external authority boundaries;
- limitation records;
- court results;
- claim ceiling;
- supersession lineage.

## 8. Courts and Witnesses Need Constitutional Addresses

A conformance court is not merely a test suite. It must have a constitutional address.

The address must answer:

- Who defines the law?
- Who executes the tests?
- Who supplies evidence?
- Who authorizes the verdict?
- Who hears appeal?
- Who may amend the court?
- Who preserves the record?

If one component defines, executes, adjudicates, amends, and custodies its own conformance law, it effectively owns the whole constitutional object.

A mature architecture should distinguish at least four court types.

### 8.1 Kernel-Local Courts

These judge implementations claiming conformance to one kernel.

### 8.2 Corridor Courts

These govern transitions between layers or kernels, including:

- model to realization;
- realization to executable artifact;
- executable artifact to runtime effect;
- effect to receipt;
- receipt to recognized standing.

Corridor courts enforce non-implication rules such as:

$$
\mathrm{RealizationCorrectness}
\nRightarrow
\mathrm{ExecutionAuthority},
$$

$$
\mathrm{ExecutionSuccess}
\nRightarrow
\mathrm{SemanticCorrespondence},
$$

and

$$
\mathrm{SemanticCorrespondence}
\nRightarrow
\mathrm{EffectAuthorization}.
$$

### 8.3 Composition Courts

These determine whether individually conforming components form a conforming composite system.

### 8.4 Mechanic-Admission Courts

These determine whether the vocabulary, trusted mechanics, or court structure should change.

The court that executes a law need not author it. The component that witnesses an event need not authorize it. The system that custodies a verdict need not decide it.

### 8.5 Independent Witnessing

Witnessing is a cross-cutting constitutional function. Its defining question is not merely whether evidence exists, but whether the evidence crosses an independent trust boundary.

A witness controlled entirely by the actor under evaluation cannot by itself establish independence from that actor. A witness may testify to observation, consistency, absence, contradiction, or effect correspondence. It must not silently inherit authority over the object or event it witnesses.

This paper does not decide whether witnessing requires a distinct Universal Witness Kernel, a shared profile, or composition among governance, execution, and custody systems. That classification remains a mechanic-admission question. The present obligation is narrower: every corridor that relies on independent testimony must identify the witness, its jurisdiction, its authority or evidentiary standing, and the lineage of its records.

## 9. Supersession, Amendment, and Non-Retroactivity

A ratified constitutional object should not be amended in place.

Kernel evolution should occur through supersession:

$$
K_1 \rightarrow K_2.
$$

The predecessor remains an immutable historical object. The successor carries an explicit relationship to it.

Useful relations include:

- `COMPATIBLE_EXTENSION`;
- `CLARIFYING_SUPERSESSION`;
- `MIGRATION_REQUIRED`;
- `INCOMPATIBLE_SUCCESSOR`;
- `SECURITY_SUPERSESSION`;
- `DEPRECATION_ONLY`;
- `REVOCATION_OF_STANDING`.

These relations must not be collapsed.

Supersession changes which model is preferred or required for future work. Revocation claims that earlier standing was invalidly earned. Deprecation discourages new use while preserving prior validity.

A system conforming to $K_1$ does not automatically become nonconformant merely because $K_2$ exists.

Migration is itself a governed realization:

$$
\mathrm{System}@K_1
\xrightarrow{\text{governed migration}}
\mathrm{System'}@K_2.
$$

It requires source and target identities, a mapping, preserved and changed invariants, limitation records, migration courts, a new conformance judgment, and rollback or coexistence rules.

W3C distinguishes superseded, obsolete, rescinded, and restored Recommendations through different procedures and continuing consequences [@w3c-process]. Rust Editions permit language evolution while preserving interoperability and allowing packages to migrate independently [@rust-editions]. Kubernetes API deprecation policy likewise preserves migration and decoding obligations rather than treating removal as an untyped disappearance [@kubernetes-deprecation].

The paper itself follows this rule. The scoring language in Appendix B is instrument v0.2, not an in-place rewrite of v0.1. All statistics reported under v0.1 remain v0.1-only evidence.

## 10. ACG as a Meta-Invariant of Constitutional Systems

An emerging constitutional-computing architecture distinguishes several functional organs:

- a Universal Modeling Kernel, or UMK, for modeled possibility;
- a Universal Governance Kernel, or UGK, for admissibility, authority, standing, and refusal;
- a Universal Realization Kernel, or URK, for preserving meaning through embodiment in a target;
- a Universal Execution Kernel, or UEK, for admitted execution, capability mediation, effects, and recovery;
- CGSOS for identity, custody, storage, recognition, replication, and reconstruction;
- CER for constitutional admission of changes to trusted mechanics;
- an explicit UCM composition profile for cross-organ law.

Together these describe a candidate functional anatomy of a Universal Constitutional Machine.

ACG does not replace these systems. It governs the constitutional completeness of their own transformation claims.

A modeling kernel must govern continuity of models. A governance kernel must govern succession of its laws and courts. A realization kernel must distinguish source meaning from target testimony. An execution kernel must distinguish successful execution from authorized effect. A custody system must distinguish possession from local recognition. A mechanic-admission razor must govern its own supersession without allowing a candidate version to authorize itself.

ACG therefore functions as a meta-invariant:

> Every operative constitutional organ must define identity, admissibility, authority, and lineage for the transformations it claims to govern.

This does not make ACG a sovereign super-kernel. It is a completeness condition applied to each organ within its jurisdiction.

## 11. External Evidence

The larger claim must be tested outside the systems that produced it. The following cases were selected because they arise in materially different technical, legal, regulatory, and scientific traditions.

### 11.1 Secure Software Updates

The Update Framework uses trusted roles, signature thresholds, hashes, metadata versions, and expiry information to verify update metadata and target files while resisting rollback, freeze, and mix-and-match attacks [@tuf-spec].

Its structure is recognizably ACG-shaped:

- $\mathrm{IR}$ binds metadata and target identity;
- $\mathrm{AL}$ specifies the verification workflow;
- $\mathrm{AB}$ is supplied by trusted roles and thresholds;
- $\mathrm{LC}$ is preserved through version and rollback rules.

Its jurisdiction is bounded. Verified acquisition does not itself establish installation or runtime authorization.

### 11.2 DNSSEC Trust-Anchor Rollover

RFC 5011 describes automated, authenticated, and authorized updating of DNSSEC trust anchors. Existing trust enables governed addition and succession of new anchors through explicit state, hold-down, and revocation mechanisms [@rfc5011].

This is a clear instance of authority descending through lineage rather than being manufactured by the successor.

### 11.3 Constitutional Amendment

Article V of the United States Constitution defines proposal and ratification procedures under which an amendment becomes valid as part of the continuing Constitution [@article-v].

The case separates substantive desirability from constitutional admissibility. A proposed text does not acquire constitutional standing merely by existing or attracting support. It must pass the declared authority and lineage procedure.

### 11.4 Regulatory Modification

FDA guidance distinguishes modifications that may remain under an existing device's authorization from changes requiring a new premarket submission. The purpose is to make the decision process predictable, consistent, and transparent [@fda-510k].

The question is not simply whether the modified device exists or functions. It is whether the changed device may legitimately inherit the market standing of the previously authorized device.

FAA Supplemental Type Certificates similarly govern major changes to approved type designs, including compatibility with previously approved modifications [@faa-stc; @faa-compatibility].

### 11.5 Standards and Proposal Processes

W3C Recommendation status, IETF standards procedures, and Python PEP governance distinguish mere publication from recognized standing [@w3c-process; @rfc2026; @pep1].

These systems show that institutional authority may be operative within a declared jurisdiction even when it cannot physically prevent noncompliant speech or implementation.

### 11.6 Scientific Sequence Versioning

NCBI accession.version identifiers preserve a stable accession while incrementing a version suffix when sequence data changes [@ncbi-sequence-ids].

This case is important because lineage identity persists while content changes. It demonstrates that constitutional identity need not be reducible to byte identity.

### 11.7 Version Control and Content Identity as Partial Cases

Git objects are immutable and content-identified; commits record parents and form a directed history. Git therefore provides strong object identity and ancestry mechanics. Its core object model does not determine which branch head is the universally legitimate successor for a project [@git-data-model; @git-user-manual].

This is a claim boundary rather than a defect:

$$
\mathrm{IR} + \mathrm{RecordedLineage}
\nRightarrow
\mathrm{GovernedSuccession}.
$$

Similarly, immutable content identifiers establish exact object identity without automatically providing successor authority.

## 12. Validation Status and Instrument Supersession

### 12.1 Instrument v0.1

A frozen v0.1 instrument defined the four components, component-specific scoring criteria, falsifier conditions, anti-forcing rules, rival decompositions, and standing classes [@acg-instrument-v01].

The initial same-session dual-pass pilot produced:

- 69 exact agreements across 72 component judgments;
- 0.9583 exact agreement;
- quadratic-weighted kappas of 1.000 for $\mathrm{IR}$, 0.889 for $\mathrm{AL}$, 1.000 for $\mathrm{AB}$, and 0.952 for $\mathrm{LC}$.

A later coder from a different model family locked a record before unblinding but had already read a summary containing control expectations and three prior disagreement topics. The coder correctly declared the pass semi-independent rather than independent.

Against the two initial passes, the new coding achieved:

- 65 of 72 exact component agreements against pass A;
- 68 of 72 against pass B;
- minimum component kappa of 0.857 against pass A;
- minimum component kappa of 0.880 against pass B;
- identical standing classes against pass B;
- detection of all four synthetic ablations;
- no candidate falsifier;
- replicated loss of diagnostic power in fused rival models.

Those results support cross-model intelligibility and instrument stability. They do not discharge the independence gate.

Calibration mutations are training and instrument checks, not external evidence. Future reliability reports should therefore make external-case agreement primary and report calibration performance separately.

### 12.2 Instrument v0.2

The cross-model pass identified ambiguity in how v0.1 graded mechanisms that record ancestry or precedence without conferring operative successor standing. It also exposed boundary questions concerning authority over records versus authority over the exact continuity claim.

Instrument v0.2 is a `CLARIFYING_SUPERSESSION` of v0.1. It preserves:

- the four components;
- the score range;
- the necessity conjecture;
- the falsifier rule;
- the standing classes;
- the rival-model protocol.

It changes:

- the scope gate by adding a continuity-claim type;
- the $\mathrm{IR}$ criteria for externally supplied object identity;
- the $\mathrm{AB}$ criteria for record authority versus successor-standing authority;
- the $\mathrm{LC}$ criteria for recorded lineage versus lineage used to confer standing;
- the statistical protocol by separating external cases from calibration cases.

All v0.1 statistics remain evidence under v0.1 only. A retrospective v0.2 sensitivity pass is reported as measurement analysis, not as new validation evidence.

The sensitivity pass altered six of 72 component scores relative to pass A, three relative to pass B, and one relative to the contamination-declared coder. The direction was bidirectional: the clarified lineage criteria moved the Git and Semantic Versioning cases toward the later coder's minority scores, while the clarified authority criterion retained the pilot's lower score for the NCBI case. No candidate falsifier appeared, and the v0.2 standing classes matched pass B on all 18 cases. These results reduce concern that the clarification merely selected one coder's full record, but they do not substitute for clean independent coding.

## 13. Rival Decompositions

### 13.1 Fusing Interpretation and Lineage

A rival model might combine $\mathrm{IR}$ and $\mathrm{LC}$ into one category called identity continuity.

This loses diagnostic resolution. An immutable digest can identify an object exactly while providing no successor relation. A lineage record can connect objects historically while leaving the identity criterion externally defined.

The repair for missing $\mathrm{IR}$ differs from the repair for missing $\mathrm{LC}$.

### 13.2 Fusing Law and Authority

A rival model might combine $\mathrm{AL}$ and $\mathrm{AB}$ into governance.

This also loses resolution. Semantic Versioning contains detailed rules but lacks a universal binding court. Conversely, an authority may possess power to designate a successor while lacking principled transformation rules.

The repair for absent law differs from the repair for absent authority.

### 13.3 Reducing ACG to Identity and Governance

A two-part model can classify systems broadly but cannot distinguish exact identity from legitimate descent, permissible change from authorized judgment, recorded history from operative supersession, or validation from continuity.

A fused model may reproduce ACG's binary results only by silently reconstructing the separated functions inside larger labels.

ACG's advantage is diagnostic locality:

> When a continuity claim fails, ACG predicts what kind of function is missing and what sort of repair is required.

## 14. The Governed-Effect Completeness Hypothesis

A related four-part decomposition emerged from the separation of semantic, execution, custody, and effect courts:

$$
\begin{aligned}
&\mathrm{GovernedEffectStanding} \stackrel{?}{=} \mathrm{SemanticAdequacy} \\
&\land \mathrm{ExecutorConformance} \\
&\land \mathrm{CustodyFidelity} \\
&\land \mathrm{EffectIntegrity}
\end{aligned}.
$$

This formula is not a settled result. It is a working hypothesis.

Its purpose is to prevent the following laundering paths:

- semantic adequacy silently becoming evidence of executor conformance;
- executor conformance silently becoming evidence of custody fidelity;
- custody fidelity silently becoming evidence that an external effect was authorized;
- effect occurrence silently becoming evidence that source meaning was preserved.

The hypothesis has not undergone the ablation, rival-model, or external-validation program applied to ACG. It remains on the research docket.

Questions include:

- Are all four functions independently necessary?
- Does authority mediation belong inside effect integrity or require another term?
- Is independent witnessing a fifth function or evidence supporting the four?
- Can a simpler decomposition preserve the same diagnostic power?
- Which historical systems added which repair after each function failed?

## 15. Falsification and Claim Ceiling

ACG should lose standing if a mature mechanism is found that:

1. genuinely makes an operative legitimate-continuation claim;
2. is correctly scoped;
3. lacks one ACG function;
4. does not import that function from another component or external boundary;
5. nevertheless sustains the claim.

ACG should also be revised if:

- two components prove functionally inseparable across cases;
- a simpler decomposition predicts the same failures with equal diagnostic precision;
- mappings depend only on metaphor;
- or the model cannot make prospective predictions.

The present evidence does not establish that ACG is a mathematical theorem, universally sufficient, a complete theory of governance, a safety proof, or a guarantee of legitimate authority.

Its current standing is:

> ACG has substantial cross-domain support as a four-part functional model of governed identity continuity. Systems making operative succession claims repeatedly instantiate functional equivalents of Interpretation Regime, Admissibility Law, Authority Binding, and Lineage Continuity within the relevant jurisdiction, while partial systems lacking a component exhibit the predicted claim ceiling.

## 16. Research Program

### 16.1 Clean Independent Coding

The immediate gate requires:

- at least two genuinely independent reviewers;
- no prior exposure to expected scores or disagreement loci;
- locked records before unblinding;
- component-level agreement reporting;
- calibration reported separately from external cases;
- blind adjudication;
- preservation of disagreement history.

### 16.2 Prospective Prediction

The stronger test should begin with defective historical mechanisms before their repairs are revealed.

Reviewers should predict:

- which ACG function is missing;
- what failure should occur;
- what kind of repair should later appear.

A theory earns deeper standing when it predicts repairs rather than merely classifying completed systems.

### 16.3 Natural Negative Cases

The corpus should include more systems with ambiguous object identity, authority without transformation law, chronology without successor standing, local authority without global jurisdiction, and multiple competing lineage claims.

### 16.4 Formalization

Further work should determine whether ACG can be represented in temporal logic, typed transition systems, category-theoretic transformations, or another formalism without losing its institutional and semantic meaning.

### 16.5 Kernel Admission

Candidate kernels should provide an ACG record before admission:

```text
kernel_identity
interpretation_regime
admissibility_law
authority_binding
lineage_model
conformance_court
witness_boundary
escape_record
supersession_rules
rollback_criterion
claim_ceiling
```

A proposed kernel lacking one field should remain a theory, protocol, profile, or framework rather than silently acquiring inherited authority.

## 17. Constitutional Status of the Present Paper

The following ledger prevents the synthesis from granting claims more standing than their evidence supports.

| Claim | Present standing |
|---|---|
| ACG consists of $\mathrm{IR}$, $\mathrm{AL}$, $\mathrm{AB}$, and $\mathrm{LC}$ | Core theory |
| The four functions are diagnostically separable | Supported by natural and synthetic ablations |
| ACG recurs across external domains | Substantially supported |
| ACG is necessary for every governed-continuity claim | Falsifiable conjecture |
| ACG is jointly sufficient | Not established |
| Kernelization is an application of ACG | Analytically supported within the originating corpus |
| UCM cross-organ non-implications require explicit constitutional homing | Architectural requirement supported by corridor analysis |
| The Governed-Effect Completeness formula is necessary and sufficient | Working hypothesis only |
| Witnessing requires a distinct universal kernel | Open mechanic-admission question |
| Instrument v0.1 statistics apply under v0.2 wording | Explicitly refused |
| Instrument v0.2 is ready for clean independent review | Earned by clarifying supersession and sensitivity analysis |
| Independent inter-rater validation | Open |
| ACG is a universal theorem | Not claimed |

## 18. Discussion: A Grammar of Becoming

ACG began as a discipline for constitutional governance. Its broader significance emerged indirectly.

Storage systems needed to distinguish possession from recognition. Realization systems needed to distinguish successful translation from preserved meaning. Execution systems needed to distinguish computation from authorized effect. Kernel systems needed to distinguish shared architecture from inherited law. Version systems needed to distinguish ordering from legitimate succession. Witness systems needed to distinguish recorded truth from authority over what was recorded.

Across these cases, the same questions returned:

- What is the thing?
- What change is valid?
- What makes the judgment binding?
- How does the changed thing remain related to what came before?

This recurrence suggests that ACG may connect domains usually separated: ontology, law, authority, and history.

An identity system without admissibility can identify arbitrary mutations. An admissibility system without authority can recommend but not govern. An authority system without lineage can replace without preserving continuity. A lineage system without interpretation can connect names whose identity meaning remains undefined.

ACG proposes that these are not independent conveniences. They form a constitutional whole.

The poetic claim can therefore be stated carefully:

> ACG may be the grammar by which an identity-bearing system becomes something new without silently ceasing to be itself.

## 19. Conclusion

Every transformation creates a temptation to collapse distinct claims.

A new artifact exists, therefore it is the successor.

A signature verifies, therefore the claim is true.

A model executes, therefore the realization is faithful.

A hash matches, therefore the semantics are preserved.

A rule is written, therefore it governs.

A history is recorded, therefore the lineage is legitimate.

ACG refuses these shortcuts.

It requires an Interpretation Regime to say what continues. It requires an Admissibility Law to say which transformation is valid. It requires an Authority Binding to say why that law has operative standing. It requires Lineage Continuity to say how predecessor and successor remain constitutionally related.

Together, these functions provide a disciplined account of governed identity through change.

Their implications extend beyond institutional governance. They shape software updates, model realization, artifact custody, kernel inheritance, execution authority, regulatory modification, standards succession, and cryptographic trust.

The broadest claim remains unearned. ACG is not yet a universal law.

It has nevertheless moved beyond an internal design intuition. It is now a falsifiable cross-domain theory with natural ablations, diagnostic rival tests, a versioned validation instrument, substantial cross-model stability, and a clear path toward independent verification.

The present horizon can be stated in one sentence:

> Anything may change; ACG asks what must be true before the changed thing may legitimately inherit the name, authority, and history of what came before.

## Appendix A: ACG Diagnostic Matrix

- **Question:** What object is continuing?  
  **Function:** Interpretation Regime  
  **Predicted absence failure:** Identity ambiguity

- **Question:** Which transformation is valid?  
  **Function:** Admissibility Law  
  **Predicted absence failure:** Arbitrary mutation

- **Question:** What makes the judgment operative?  
  **Function:** Authority Binding  
  **Predicted absence failure:** Advisory or self-declared compliance

- **Question:** How does the successor descend from the predecessor?  
  **Function:** Lineage Continuity  
  **Predicted absence failure:** Succession ambiguity

## Appendix B: Proposed ACG Validation Instrument v0.2 Scoring Criteria

The criteria in this appendix belong to ACG Validation Instrument v0.2. They supersede v0.1 prospectively and do not amend it in place. All statistics in this paper were earned under v0.1 unless explicitly labeled as v0.2 sensitivity analysis.

### B.1 Continuity-Claim Type

Before component scoring, classify the claim as one of:

- `OPERATIVE_SUCCESSION`;
- `RECORDED_LINEAGE`;
- `ADVISORY_CLASSIFICATION`;
- `IDENTITY_ONLY`;
- `NO_CONTINUITY_CLAIM`;
- `SCOPE_ERROR`.

### B.2 Interpretation Regime

- Score 2: The mechanism defines both the governed object and the criteria by which identity or continuity across the relevant transformation is determined.
- Score 1: A stable identifier or representation exists, but the underlying object of continuity or sameness criterion is imported from naming convention, user assertion, or another system.
- Score 0: The mechanism cannot determine which object is claimed to persist.
- Score U: Evidence is insufficient.

### B.3 Admissibility Law

- Score 2: Explicit operative rules distinguish admissible from inadmissible transformations.
- Score 1: Rules exist but are optional, local, incomplete, conventional, or partly externalized.
- Score 0: No rule distinguishes valid transformation from arbitrary change.
- Score U: Evidence is insufficient.

### B.4 Authority Binding

- Score 2: A declared authority, verifier, court, threshold, or enforcement mechanism can confer, deny, or downgrade the exact standing named by the continuity claim.
- Score 1: Authority is limited to recording, formatting, publication, local configuration, or social recognition while the claimed legitimate-succession standing remains external or only partly bound.
- Score 0: Compliance and standing are self-asserted or merely advisory.
- Score U: Evidence is insufficient.

### B.5 Lineage Continuity

- Score 2: A typed predecessor-successor, migration, supersession, rollback, or consistency relation is used by an operative mechanism to confer, deny, preserve, or downgrade successor standing within the declared jurisdiction.
- Score 1: A lineage, order, ancestry, or precedence relation is retained and materially used for navigation, comparison, compatibility, recording, or advisory classification, but it does not itself confer full operative successor standing, or that standing relation is externalized.
- Score 0: No relevant predecessor-successor relation exists beyond independent identity, arbitrary chronology, or unrelated validity.
- Score U: Evidence is insufficient.

The complete frozen instrument, falsifier rule, anti-forcing rules, and reporting protocol are shipped with this paper package.

## Appendix C: Instrument Supersession Record

| Field | Record |
|---|---|
| Predecessor | ACG Validation Instrument v0.1 |
| Successor | ACG Validation Instrument v0.2 |
| Relation | `CLARIFYING_SUPERSESSION` |
| Trigger | Ambiguity in recorded lineage, advisory precedence, externally supplied identity, and record authority |
| Preserved | Four functions, score range, falsifier rule, standing classes, rival tests |
| Changed | Scope typing, IR wording, AB wording, LC wording, calibration reporting |
| Retroactive effect | None |
| Prior statistics | Remain v0.1-only evidence |
| Future use | Clean independent review |
| Rollback condition | v0.2 reduces clarity or reliability, introduces directed scoring bias, or erases a distinction preserved by v0.1 |

## Appendix D: ACG and the Constitutional Organ Stack

- **Organ or profile:** UMK  
  **Primary question:** What can be modeled?  
  **ACG obligation:** Model identity and version continuity

- **Organ or profile:** UGK  
  **Primary question:** What may stand?  
  **ACG obligation:** Law, authority, judgment, and court succession

- **Organ or profile:** URK  
  **Primary question:** What realization preserves meaning?  
  **ACG obligation:** Source-target interpretation and realization lineage

- **Organ or profile:** UEK  
  **Primary question:** What may execute and cause effects?  
  **ACG obligation:** Execution authority, effect admission, and recovery lineage

- **Organ or profile:** CGSOS  
  **Primary question:** What exact artifact is recognized and preserved?  
  **ACG obligation:** Custody identity, local admission, and replication lineage

- **Organ or profile:** CER  
  **Primary question:** When should mechanics change?  
  **ACG obligation:** Self-amendment, court authority, and supersession

- **Organ or profile:** Independent witnessing  
  **Primary question:** What testimony may be credited without relying solely on the actor evaluated?  
  **ACG obligation:** Witness identity, admissible observations, independent standing, and record lineage

- **Organ or profile:** UCM composition profile  
  **Primary question:** How do the organs compose?  
  **ACG obligation:** Cross-organ non-implication and corridor law

## Appendix E: Kernel Admission Questions

A proposed kernel should answer:

1. What insufficiency justifies kernelization?
2. What model becomes inherited?
3. What is the kernel's jurisdiction?
4. Which invariants must descendants preserve?
5. What counts as conformance?
6. Which court adjudicates conformance?
7. What standing may partial conformers claim?
8. Which escapes are typed?
9. What evidence must cross an independent witness boundary?
10. How is a successor kernel admitted?
11. What evidence would demote the kernel to a profile, protocol, framework, or theory?

## Standing and Claim Boundary

This paper is a conceptual, formal, or architectural contribution unless it explicitly binds a statement to a cited external source or an exact carried evidence artifact. Unbound statements about implementation, validation, performance, safety, universality, or proof are research claims or design obligations, not established operational facts. Corpus-internal references establish conceptual lineage and comparison, not independent external confirmation.

## Corpus-Wide Reference Positioning

This paper argues that systems change. Its nearest external comparison fields are governance, security, provenance. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Unforgeable capabilities can constrain exercise of authority while still leaving allocation, delegation, revocation, and social legitimacy incorrectly specified. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

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

**[A1]** Adam Ableman. *Constitutional Theory*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-D2D97C4042FD281F`;  
source SHA-256  
`FACC256EDDE5A7D7EA18133CFC9C060CFB8C3811B0221E1969E62347F2BB69CF`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Governance Engineering*. Ableman Corpus current edition; work identity `PAPER.PUB.18749870`;  
source SHA-256  
`372169F315D192733856B1F4A3F1038BBC73F57CF3ED9ACABAE72B965A69C8D0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Universal Governance Kernel (UGK)*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-1F9BFB2BF8370226`;  
source SHA-256  
`AA5106EA71E5DF120E141435C280DFC532715CA5DE0C75B8862BB7784ECCFACD`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Legitimacy Without Self-Ratification*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-EF2382F9397335AC`;  
source SHA-256  
`0186A39C808F8FDDB5C8F42384DF1A26678928434BD50A0EAE8D4947390F68A2`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Effect Sovereignty*. Ableman Corpus current edition; work identity `PAPER.PUB.18737323`;  
source SHA-256  
`1DB8A34946A8705F6F4BA4FC3B12B251FC7C83DBDF217F9DDFF55529C8612EE7`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Receipt-Bound Capabilities: Membrane Tokens for Governed Interaction with Reality*. Ableman Corpus current edition; work identity `PAPER.PUB.18601631`;  
source SHA-256  
`6DE46F821594AB11BFB7F8373368C452BD89E5BD4EB172B88D9467E87CF74C33`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Integrity Enforcement Layer*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-505307E9E6571B63`;  
source SHA-256  
`F858AB32E0937B796353CAE573DD4183FDF4F179A3E1E7E40C4E0C6BF1AB0018`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

1. Ableman, A. *Ableman Constitutional Governance: Interpretation Regime, Admissibility Law, Authority Binding, and Lineage Continuity.* Ableman Corpus edition.

2. Ableman, A. *The Mechanics of Constitutional Enforcement: Ratchets, Roles, Receipts, and Identity-Bearing State.* Ableman Corpus edition.

3. Ableman, A. *ACG External Validation Instrument, version 0.1.* Unpublished validation instrument and case corpus.

4. The Update Framework. *Specification, Security Model, Roles, and Metadata.*

5. StJohns, M. *RFC 5011: Automated Updates of DNS Security Trust Anchors.* RFC Editor, 2007.

6. Cooper, D., et al. *RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List Profile.* RFC Editor, 2008.

7. Laurie, B., et al. *RFC 9162: Certificate Transparency Version 2.0.* RFC Editor, 2021.

8. Kubernetes Project. *API Deprecation Policy and Deprecated API Migration Guide.*

9. World Wide Web Consortium. *W3C Process Document.*

10. Rust Project. *The Rust Edition Guide.*

11. Preston-Werner, T. *Semantic Versioning 2.0.0.*

12. Git Project. *Git Data Model, User Manual, and Git Objects.*

13. IPFS Project. *Content Identifiers and the InterPlanetary Name System.*

14. United States Food and Drug Administration. *Deciding When to Submit a 510(k) for a Change to an Existing Device.*

15. Python Software Foundation. *PEP 1: PEP Purpose and Guidelines* and *PEP 13: Python Language Governance.*

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848570](https://doi.org/10.5281/zenodo.23848570)
