# The Three Hash Rule

## Governance Completeness Through Independent Cryptographic Commitments

### A state may verify and still be inadmissible. A signature may verify and still fail standing. A text may persist and still change meaning.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

This paper introduces the Three Hash Rule: a governance-completeness model in which object state, admissibility, and meaning are committed independently as $H_s$, $H_c$, and $H_m$. A fourth commitment, $H_j$, supplies optional jurisdictional locality for cross-phase systems. The minimal complete set is $\{H_s, H_c, H_m\}$: $H_s$ decides state, $H_c$ decides admissibility, and $H_m$ decides meaning. $H_j$ does not enlarge single-phase completeness, but adds locality queries over phase-bound namespaces. The novelty is the separation: governance completeness is not produced by a stronger signature or a richer content hash, but by independent commitments whose decision procedures cannot safely collapse into one another.

## 1. Introduction

Content hashes decide object identity; signatures decide key possession or authorship evidence; neither alone decides admissibility, semantic interpretation, or jurisdictional locality. Governance failures are therefore state failures, admissibility failures, semantic failures, locality failures, or binding/context failures. The Three Hash Rule states that these domains must be separately committed, separately witnessed, and separately decided.

The Three Hash Rule does not specify what facts must enter each commitment; it specifies that the four governance questions are independent and must be answered independently. The *constitution* decides what facts enter $H_s$ (state), what conditions enter $H_c$ (admissibility), what semantics enter $H_m$ (meaning), and what jurisdictional structure enters $H_j$ (locality). Identities, authorities, evidentiary requirements, evaluator qualifications, and procedural prerequisites enter the architecture only when the constitution elevates them into a specific layer's commitment. The framework is therefore substrate-neutral with respect to *what* governance evaluates while being strict about *how* governance commits to its evaluations.

## 1.5 The Constitutional Legend Frame

The Three Hash Rule commitments and the receipt binding modes are projections of a single object: a Constitutional Legend $L = (J_L, B_L, R_L, T_L, C_L, A_L)$. Each component is an independently governable layer of the governance architecture, and each Three Hash Rule construct projects onto one of them. (The legend components are subscripted to disambiguate them from the semantic regime tuple introduced in Section 8, which uses some of the same letters with different meanings.)

- **Legend component:** $J_L$ jurisdiction  
  **What it governs:** admissible semantic scope (domain, language, participation boundary)  
  **Three Hash Rule projection:** $H_j$ (locality)

- **Legend component:** $B_L$ bindings  
  **What it governs:** authorized canonical sense $\leftrightarrow$ lexical mappings  
  **Three Hash Rule projection:** binding layer of $H_m$ (meaning)

- **Legend component:** $R_L$ render surfaces  
  **What it governs:** permitted representational forms  
  **Three Hash Rule projection:** surface layer of $H_m$

- **Legend component:** $T_L$ transport  
  **What it governs:** encoding, serialization, transmission admissibility  
  **Three Hash Rule projection:** receipt binding mode (Section 4) -- the configuration manifold

- **Legend component:** $C_L$ continuity  
  **What it governs:** identity, interpretive, projection continuity invariants  
  **Three Hash Rule projection:** recoverability invariant (Section 4.5), Specification-tier

- **Legend component:** $A_L$ authority  
  **What it governs:** certifies admissibility under the legend  
  **Three Hash Rule projection:** $H_c$ (admissibility)

Two consequences of this framing carry argumentative weight in later sections. First, the separation thesis of the Three Hash Rule is the legend's own thesis: $J_L$, $B_L$, $R_L$, $T_L$, $C_L$, and $A_L$ are independently governable layers, and the cryptographic commitments inherit that separation rather than asserting it bare. Second, the receipt binding mode and the question of where law is committed are the legend's $T_L$ and $J_L / A_L$ components, respectively; both resolve by separation, not by folding additional content into $H_m$.

## 2. Assumptions

The framework assumes collision resistance, second-preimage resistance, preimage resistance, domain separation, canonicalization correctness, byte-stability across conforming implementations, pure and versioned $(P,\Sigma,\Phi)$, explicit evaluation time $t$, and no unstated external I/O during verification. All security, independence, and completeness claims are conditional on these assumptions.

## 3. Receipts and Decision Procedures

A governance receipt is:

$$
R := (H_s,H_c,H_m,H_j?,H_r,\pi)
$$

where:

$$
\pi := (\pi_s,\pi_c,\pi_m,\pi_j?)
$$

is the witness family.

A validity context is:

$$
\mathcal{C}:=(P,\Sigma,\Phi,t)
$$

where $P$ is admissibility policy, $\Sigma$ is semantic regime, $\Phi$ is governance phase, and $t$ is evaluation time.

Define:

$$
id(\mathcal{C}) := H(id(P)\parallel id(\Sigma)\parallel id(\Phi)\parallel t)
$$

The receipt supports decision procedures:

$$
D_s(R,\mathcal{C},\pi_s,t)\in \{0, 1\}
$$

$$
D_c(R,\mathcal{C},\pi_c,t)\in \{0, 1\}
$$

$$
D_m(R,\mathcal{C},\pi_m,t)\in \{0, 1\}
$$

$$
D_j(R,\mathcal{C},\pi_j,t)\in \{0, 1, \mathsf{NA}\}
$$

- **Commitment:** $H_s$  
  **Procedure:** $D_s$  
  **Question:** state

- **Commitment:** $H_c$  
  **Procedure:** $D_c$  
  **Question:** admissibility

- **Commitment:** $H_m$  
  **Procedure:** $D_m$  
  **Question:** meaning

- **Commitment:** $H_j$  
  **Procedure:** $D_j$  
  **Question:** locality

A receipt is governance-complete iff:

$$
D_s=1 \land D_c=1 \land D_m=1
$$

and binding verification (Section 4.5) succeeds. The core decisions establish governance-completeness over the three core questions; binding verification establishes that the receipt identity itself satisfies the recoverability invariant. A receipt that passes all four core decisions but fails binding verification is rejected as inadmissible.

$H_j$ is required only for locality queries across phase-bound namespaces. For single-phase governance, $(D_j=\mathsf{NA})$ does not defeat completeness.

### Constitutional Roles: Receipt, Authority, and Evidence

A subtle but important distinction is required before discussing how receipts participate in subsequent governance. *Receipt-ness, authority-ness, and evidence-ness are not properties of artifacts; they are constitutional roles that artifacts may play.* The framework therefore distinguishes three constitutional roles whose validity criteria differ, rather than three classes of artifact whose ontologies differ:

* **Receipt role.** Validity established by *integrity, provenance, availability, and auditability*. The receipt role asks whether the artifact authentically and durably establishes that a governed transition occurred. An artifact in the receipt role is *historically immutable* in its constitutional standing: the act it attests cannot be undone, only superseded. The role is *non-authoritative with respect to current capability*: passing the receipt test does not, by itself, grant power, permission, or capability. It establishes that an event occurred; it does not perform the event afresh.

* **Authority role.** Validity established by *integrity, currency (not expired, not revoked), scope, and participation in admissibility*. The authority role asks whether the artifact constitutes valid present capability under policy. An artifact in the authority role is subject to revocation, expiration, suspension, and transfer: the present authority it carries can change while the historical fact of its issuance remains fixed.

* **Evidence role.** Validity established by *freshness, attestation chain, and re-evaluability under the consuming policy*. The evidence role asks whether the artifact establishes a constitutional fact that policy may consult. Evidence artifacts may be re-evaluated under different policies, and their constitutional weight depends on the consuming evaluation.

These are roles, not artifact types. A single artifact may simultaneously satisfy multiple role contracts. A passport is both a receipt of identity verification and an authority artifact granting border crossing. A board resolution is both a receipt of the vote tally and an authority granting designated spending. A namespace certificate is both a receipt of allocation and an authority over namespace control. The constitution determines which roles a given artifact is admitted to play, and which validity criteria apply in each role; the artifact itself implements whichever role contracts it satisfies.

The same artifact may pass one role test and fail another. An expired JWT may remain a perfectly valid receipt of past issuance --- its integrity, provenance, and auditability are unchanged by the passage of time --- while ceasing to be valid authority because the currency criterion fails. The constitutional question is therefore not *"is this artifact a receipt or an authority artifact?"* but *"is this artifact being evaluated under the receipt role or the authority role, and does it satisfy the validity criteria for that role?"*

A governed transition may produce evidence in multiple roles. The act of issuing a JWT produces a receipt of issuance (under the receipt role: durable, auditable) and an authority artifact (under the authority role: present, revocable). These may be realized as a single artifact carrying both role contracts, or as separate artifacts each carrying one. In practice they are often realized separately, because the role contracts point in opposite directions: the receipt role wants durability, inspectability, and long-term retention; the authority role often wants confidentiality, short lifespan, and tight control over distribution. The framework does not require role separation but recognizes that distinct security requirements typically motivate it.

Receipts in the receipt role may still be *constitutionally relevant* to subsequent admissibility decisions even though the role is non-authoritative. Policy at $H_c$ may consult prior receipts to answer questions such as *"was authority delegated?"*, *"was namespace allocated?"*, or *"was amendment ratified?"*. The receipt does not grant the delegation, allocation, or ratification by being consulted; it attests that the delegating, allocating, or ratifying transition occurred, and the present-time admissibility decision derives authority by treating that attestation as evidence under policy. This preserves the independence of the four hash layers: each commits independently to its own question, while the facts that policy considers when answering any one question may include prior receipts whose persistence is itself a constitutional fact.

The role-based formulation sharpens revocation semantics. Revocation, expiration, and transfer operate on the authority role: they change which artifacts pass the authority test going forward. They do not operate on the receipt role: an artifact's receipt-role validity is determined by integrity, provenance, availability, and auditability, none of which is affected by the artifact's present authority status. After revocation, an artifact may pass the receipt test (it still attests that issuance occurred) while failing the authority test (its present capability is gone). The constitutional record is therefore append-only history; current authority is derived state computed from that history. What gets revoked is the artifact's authority-role validity, not the historical fact the receipt-role attests.

### Storage, Compliance, and Escalation

Three architectural commitments follow from the role-based formulation.

**Storage neutrality.** A constitution need not require centralized receipt storage. It may require only that receipts satisfying the receipt role be *producible*, *available*, and *verifiable* when invoked. Receipt custody may be centralized, distributed, counterparty-held, participant-managed, archival, or any combination thereof, depending on the jurisdiction's availability and audit requirements. A driver's license is participant-managed because the holder's incentives align with retention; board-approval receipts are typically dual-retained by board and project owner; constitutional amendments often require public archival. The framework expresses all of these patterns under the same grammar: the constitutional question is whether the receipt can be produced and verified when needed, not where it is stored. (FGA Section 13 develops the cross-constitutional implications of storage neutrality: when constitutions are mutually independent, participant-held receipts cross constitutional boundaries through receipt-recognition policies rather than through shared storage infrastructure.)

**Compliance, not enforcement.** Receipts do not mechanically enforce compliance. They make compliance, noncompliance, discharge, supersession, and escalation *decidable under policy*. A receipt of an admitted decision creates a durable basis against which future conduct can be evaluated; it does not physically prevent deviation. The constitutional question after a binding decision is not "will the decided action occur?" but "did the actual conduct conform to the decided action, and what remedies are available if it did not?" The framework's commitment is to make compliance and its absence *legible*, not to make compliance *mechanical*.

**Escalation as evidence-use.** A receipt may be used in escalation, appeal, repair, or remediation proceedings when a receiving constitution recognizes it as evidence of a prior governed transition. Escalation is recourse pursued by parties with constitutionally recognized standing and incentive; it is not automatic. The framework supports escalation through the same evidence-role machinery that supports ordinary admissibility evaluation: the receiving constitution's recognition policy admits the prior receipt as a fact, and its own admissibility predicate determines what consequences follow. Escalation paths therefore need not be defined by the originating constitution: a receiving constitution may independently recognize prior receipts as admissible evidence, which is essential for governance designs in which no global root governs all constitutions involved.

## 4. Receipt Binding

The receipt binding mode is the projection of the legend's $T_L$ (transport) component. It is a configuration choice within an admissible space, not a single binary fork. Two modes are defined here; the configuration manifold (Section 4.6) lists the admissible instance configurations and their selection rule.

**Context-external mode** (portable identity, witness-pinned verification):

$$
H_r := H(DS_r\parallel root(H_s,H_c,H_m,H_j?))
$$

**Strict mode** (self-describing identity):

$$
H_r := H(DS_r\parallel root(H_s,H_c,H_m,H_j?,id(P),id(\Sigma),id(\Phi)))
$$

where $root(\cdot)$ is a deterministic domain-separated hash tree over length-prefixed typed leaves.

In context-external and strict modes, every $\pi_i$ MUST bind $H_r$, $H_s$, and $id(\mathcal{C})$. A verifier rejects if any $\pi_i$ opens to a different $H_r$, $H_s$, or $id(\mathcal{C})$, or if any object reference inside $\pi_i$ disagrees with $H_s$. The re-evaluable instance configuration (Section 4.6) is the documented exception: its witnesses do not pin $id(\mathcal{C})$ by design, so a verifier may evaluate the receipt under a context it supplies. Re-evaluable is opt-in and must be explicitly declared by the deployment; the default $\pi_i$-binding requirement above applies to all receipts that have not opted in.

The modes differ in what the *receipt identity* itself folds in. Strict mode produces self-describing identities: chain links, caches, and aggregations carrying only $H_r$ remain context-determinate without consulting the witnesses. Context-external mode produces portable identities that may stably refer across contexts at the cost of requiring the witnesses for full context determination.

## 4.5 Binding Verification and Recoverability

Binding verification is not a governance decision procedure; it is a receipt well-formedness gate that runs alongside the four core decisions. It checks that whatever context dimensions are excluded from $H_r$ under the active binding mode are either recoverable from witnesses or explicitly recorded by a disambiguating collapse witness. A receipt may satisfy $D_s = D_c = D_m = D_j = 1$ and still be rejected as malformed if binding verification fails, with error code $\mathtt{UnderRecordedCollapse}$ (Appendix B).

In practice the check is structural: for each context dimension excluded from $H_r$ (e.g. $id(P)$ when $H_c$ omits it; $id(\Phi)$ when $H_j$ is absent), the verifier confirms that a disambiguating witness records the conflation. This makes the check operationally decidable from $(R, \mathcal{C})$ alone, without comparison between receipts.

The governing invariant is *lineage continuity*: the past must be preserved in, or recoverable from, current state. Receipt-the-collapse applies the same pattern the paper uses elsewhere (hashed placeholders in Section 8, explicit failure witnesses in Section 9): silent collapse is inadmissible; receipted collapse with a disambiguating witness is admissible if non-ideal.

In strict mode the identity is self-describing; context-external mode produces a portable identity at the cost of requiring witnesses for full context determination. A third configuration (re-evaluable) opts out of context pinning entirely; see Appendix F for the three admissible configurations and their selection rule.

## 5. Canonicalization Axiom

For $i \in \{s, c, m, j\}$, each commitment has a versioned canonicalization function:

$$
c_i: X \rightarrow B_i \cup \{\bot\}
$$

and:

$$
H_i := H(DS_i\parallel id(c_i)\parallel c_i(\cdot))
$$

If $(c_i(x)=\bot)$, then $(D_i=0)$. Canonicalization functions MUST be deterministic, byte-stable, versioned, total on declared domains, explicitly rejecting outside them, and accompanied by conformance test vectors. Structured encodings must define ordering, whitespace, Unicode normalization, numeric representation, duplicate-field handling, byte order, length prefixing, and partial decoding behavior. Semantic parsers must define grammar ambiguity handling and deterministic tie-breaking.

## 6. $Hs$: State

$$
H_s := H(DS_s\parallel id(c_s)\parallel c_s(x))
$$

$D_s$ decides whether $\pi_s$ opens $x$ to $H_s$ under $c_s$. $H_s$ provides object identity and integrity only.

## 7. $Hc$: Admissibility

$H_c$ is the commitment over admissibility under the policy and authority structure. Together with $H_j$ (Section 9), it carries the components of the "rulebook" that distinguish receipts across jurisdictions and policy regimes; the meaning commitment $H_m$ deliberately does not.

Let:

$$
G_c=(V,E,\ell)
$$

be a Merkleized labeled DAG. Vertices represent principals, roots, keys, credentials, services, or roles. Edges represent delegations, claims, capabilities, revocations, or endorsements. Labels satisfy $(\ell(e)\in\mathcal{L})$, where $(\mathcal{L})$ is a decidable constraint algebra closed under conjunction.

$$
H_c := H(DS_c\parallel id(c_c)\parallel root(G_c)\parallel id(P)?)
$$

where $(id(P)?)$ is included when policy shadowing must be prevented.

### Admissibility Definition

For receipt $R$, context $(\mathcal{C})$, and witness $\pi_c$, $(D_c=1)$ iff $\pi_c$ proves a canonical path in $G_c$ from a trusted root to $(signer(x,\pi_s))$, the path is included in $(root(G_c))$, and:

$$
[\![ \ell(p) ]\!]_P(t)=\top
$$

under deterministic policy evaluation.

The canonical path must satisfy capability attenuation:

$$
cap(e_{r+1})\subseteq cap(e_r)
$$

for all consecutive edges. $G_c^*$, the proof subgraph carried by $\pi_c$, must be acyclic or include a cycle-breaking proof. Freshness is enforced by epoch or nonce binding. Root updates require threshold approval over epoch-scoped roots. Revocation is hard or soft; precedence is ordered:

$$
hard_revocation > soft_revocation > delegation > claim
$$

No revoked path may resurrect without a later valid delegation. If multiple satisfying paths exist, $(canon_path(G_c,P,t))$ selects one; if no canonical path is derivable, $(D_c=0)$.

Revocation in this precedence ordering operates on the current authority state derivable from $G_c$, not on the historical receipts that recorded prior delegations. A revocation entry is itself a governed transition with its own receipt; it changes the derived authority state by appending a new fact to the constitutional history rather than by modifying or erasing earlier facts. The receipt of the original delegation remains immutable; the authority it conferred does not, once revoked.

### Evaluator as Implementation

The decision procedure $D_c$ is the constitutionally specified function that produces the admissibility verdict. An *evaluator* is an implementation of $D_c$ rather than a parameter of admissibility itself. Two evaluators executing the same constitutional $D_c$ on the same inputs $(R, \mathcal{C}, \pi_c, t)$ should reach the same admissibility conclusion; if they do not, this is diagnostic of either constitutional incompleteness (a hidden dependency the policy has not declared), evaluator malfunction, or an unauthorized evaluator producing a non-canonical decision.

The evaluator's identity is therefore a *provenance* fact recorded in the receipt's witness family $\pi$ rather than a semantic *input* to $D_c$. Evaluator authorization enters the architecture as a constitutional concern --- and contributes to $H_c$ via the authority graph $G_c$ --- only when the constitution explicitly requires that admissibility depend on evaluation by an authorized evaluator class. In that case, the authorization claim travels as evidence in $\pi_c$ rather than as a separate parameter of the decision procedure.

This distinction matters for the independence claim and for the threat model (Section 13). A malicious or unauthorized evaluator that produces a receipt under a constitution that does not authorize it is not a $D_c$ failure but an authority-graph failure: $\pi_c$ does not establish a canonical path from a trusted root to the purported signer, and the receipt is rejected regardless of whether the evaluator's *computation* of $D_c$ was internally correct. The framework supports both deterministic constitutions (in which any qualified evaluator computes the same $D_c$) and discretionary constitutions (in which the constitution explicitly delegates judgment to an evaluator class such that different qualified evaluators may legitimately reach different conclusions) through the same authority-graph machinery; the discretionary case is expressed by allowing $G_c$ to authorize evaluator classes whose internal disagreement is constitutionally permitted.

## 8. $Hm$: Meaning

The construction in this section applies only to semantic regimes admitting deterministic parsing and bounded canonical normalization. Examples include typed configuration languages, Datalog-class policy systems, proof objects, restricted rewriting systems, and other explicitly specified formal languages. The framework does not claim canonical semantic normalization for unrestricted natural language or arbitrary expressive logics.

A semantic regime is:

$$
\Sigma := (L,T,R,v,r^*,B,imports)
$$

where $L$ is language, $T$ is theory, $R$ is rule set, $v$ is version, $r^*$ is canonical reduction strategy, $B$ is normalization bound, and $imports$ specifies treatment of external resources.

$$
c_m(x)=encode(r^*(parse_L(x)))
$$

$$
H_m := H(DS_m\parallel id(c_m)\parallel c_m(x)\parallel id(\Sigma)\parallel lineage)
$$

Here $id(\Sigma)$ commits the *identity-determining* components of the semantic regime: language $L$, theory $T$, rule set $R$, version $v$, canonical reduction strategy $r^*$, normalization bound $B$, and import policy. It explicitly *excludes* jurisdiction: the canonical semantic identity is jurisdiction-stable by design. Jurisdiction is committed in $H_j$ (Section 9) and authority is committed in $H_c$ (Section 7); these are the de-collapsers of receipt identity across legal or policy contexts, not $H_m$. The same canonical sense under different jurisdictions therefore hashes to the same $H_m$ and is distinguished at the receipt level by $H_j$ and $H_c$.

### Semantic Verification Definition

For receipt $R$, context $(\mathcal{C})$, and witness $\pi_m$, $(D_m=1)$ iff $\pi_m$ proves deterministic parsing, regime-bound normalization under $\Sigma$, satisfaction of resource bounds, and authenticated semantic lineage for $H_m$.

Semantic lineage is distinct from admissibility lineage. Authority lineage in $H_c$ traces the chain of delegations and capability attenuations from a trusted root to the signer ($\text{Root} \to \text{Org} \to \text{Service} \to \text{Key}$). Semantic lineage in $H_m$ traces the canonical transformation history of the meaning itself ($\text{Parse} \to \text{Normalize} \to \text{Lift} \to \text{Normalize}$). The two graphs answer different governance questions and must not be conflated.

If $\Sigma$ is non-confluent, $r^*$ is mandatory and included in $(id(\Sigma))$. External resources are either content-addressed into $H_m$ or explicitly excluded by hash. Uninterpreted regions are represented as hashed placeholders. Normalization must satisfy $(T_\Sigma(|x|)\le B)$, or $(D_m=0)$.

Define byte equivalence $x\equiv_b y$ and semantic equivalence $x\equiv_m y$.

### Semantic Soundness Theorem

Under the regime assumptions of Section 8 (deterministic parsing; canonical reduction strategy $r^*$; bounded normalization under $\Sigma$):

$$
H_m(x)=H_m(y)\Rightarrow x\equiv_m y
$$

The proof burden is that the canonicalization $c_m$ is injective up to semantic equivalence within $\Sigma$: if $c_m(x) = c_m(y)$ then $x$ and $y$ reduce to the same canonical form under $r^*$, which by the regime's semantic interpretation entails $x \equiv_m y$. This is one of the two statements in this paper that earns the "theorem" label (the other being Order-Independence in Section 12), because it is a meaningful consequence of the regime assumptions rather than an unfolding of definitions.

Bounded completeness holds only inside the normalization class of $\Sigma$:

$$
x\equiv_m y\Rightarrow H_m(x)=H_m(y)
$$

$H_m$ is not injective over byte representations. Cross-regime lifting from $\Sigma_i$ to $\Sigma_j$ is permitted only with $(V_{lift}(f,\pi_{lift})=1)$, where $(f:\Sigma_i\preceq\Sigma_j)$ is total over its declared domain. Semantic diffs $(\delta_\Sigma(x))$ record added, removed, changed, and unchanged judgments.

## 9. $Hj$: Locality

$H_j$ commits jurisdiction and locality. When present, it is the de-collapser of receipt identity across distinct jurisdictions: the same canonical meaning under $\Phi_i$ versus $\Phi_j$ produces distinct $H_j$ and therefore distinct $H_r$. $H_j$ does not duplicate the role of $H_m$ or $H_c$; it answers a separate governance question about namespace and locality.

$$
\Phi := (P,\Sigma,roots,params,version,map_root?)
$$

$$
id(\Phi) := H(DS_\Phi\parallel id(P)\parallel id(\Sigma)\parallel H(roots)\parallel params\parallel version\parallel map_root?)
$$

$$
H_j := H(DS_j\parallel id(c_j)\parallel id(\Phi)\parallel authority_key)
$$

Names are canonicalized by $c_{name}$, with map key:

$$
name_key := H(DS_{name}\parallel c_{name}(name))
$$

A namespace map is:

$$
M_\Phi:name_key\mapsto H_s
$$

and $(D_j=1)$ iff $\pi_j$ proves membership of $(name_key\mapsto H_s)$ in $(M_\Phi)$ under $H_j$. Non-membership proofs return $(D_j=0)$. If $H_j$ is absent and no locality query is required, $(D_j=\mathsf{NA})$.

Namespace updates require admissibility under $D_c$. Cross-phase morphisms $(f:\Phi_i\rightarrow\Phi_j)$ must preserve $D_c$ and $D_m$ over declared domains or emit explicit failure witnesses.

## 10. Necessity and Sufficiency

This section makes two scoped claims. Each is supported by a specific argumentative device, and neither is claimed to exceed its scope.

### Necessity of Each Axis (Ablation Argument)

For each $i \in \{s, c, m\}$, removing $H_i$ from the receipt eliminates a distinct class of governance decision:

- Removing $H_s$ destroys state determination.
- Removing $H_c$ destroys admissibility determination.
- Removing $H_m$ destroys semantic determination.

The ablation table in Section 15 makes this concrete: each row records the decidability class lost when one axis is removed. Each of the three commitments is therefore necessary for governance-complete decision making.

### Joint Sufficiency for the Modeled Threats

The set $\{H_s, H_c, H_m\}$ is *jointly sufficient* for the three core threat classes enumerated in Section 13: state failures are caught by $D_s$, admissibility failures by $D_c$, and semantic failures by $D_m$. The threat model contains two additional rows that the core three do not catch and are not meant to catch: **binding/context** failures are addressed by $H_r$ and the binding-verification layer (Section 4.5), and **namespace/locality** failures by $H_j$ and $D_j$ when phase-bound namespaces are in scope. The full architecture therefore comprises five mechanisms for five failure classes, with $\{H_s, H_c, H_m\}$ the minimal *decision core* and $H_r$, $H_j$ providing the binding and locality layers. The framework does not assert exhaustive coverage of all conceivable governance failures; sufficiency is relative to the threat classes catalogued in this paper. A proposed sixth mechanism would be warranted only if it catches a threat the five miss.

### Ablation Corollary

No strict subset of $\{H_s, H_c, H_m\}$ retains the necessity property above: removing any one axis collapses one governance question, as established by the ablation argument.

## 11. Independence

Two independence claims are made: a decisional claim (the headline) and a cryptographic claim (the hygiene property).

### Decisional Independence Proposition

For every ordered pair $i \neq j$ with $i, j \in \{s, c, m\}$, there exist receipts for which $D_i = 1$ and $D_j = 0$. The six statements together establish that no decision procedure is implied by any other.

Witness sketches:

- $D_s = 1, D_c = 0$: a valid object with revoked or expired authority.
- $D_s = 1, D_m = 0$: a valid object whose canonical encoding fails normalization under $\Sigma$.
- $D_c = 1, D_s = 0$: an admissible petition referring to an object whose state hash does not open under $\pi_s$.
- $D_c = 1, D_m = 0$: an authorized actor submitting content that does not parse under the declared regime.
- $D_m = 1, D_s = 0$: a semantically valid text bound to the wrong state hash.
- $D_m = 1, D_c = 0$: a well-formed semantic object presented without admissible authority.

These six counterexamples are the substantive content of the independence thesis: the three decision procedures cannot be safely collapsed into one another.

### Cryptographic Independence (Hygiene)

As a separate non-derivability hygiene property: for $i \neq j$, $H_i$ is non-derivable from $H_j$ under the assumptions of Section 2. For any PPT adversary $A$:

$$
Adv^{pred}_{i\rightarrow j}(A) \le \epsilon(\lambda)
$$

unless $A$ is given the missing canonical domain information required to compute $H_j$. Domain separation prevents cross-domain reconstruction because the $DS_i$-domain digest reveals neither the $DS_j$-domain input nor $c_j(\cdot)$ without violating the stated hash assumptions. This is a standard domain-separation observation; the decisional independence above is the architecturally substantive claim.

## 12. Composition

### Order-Independence Theorem

The evaluation order of $(D_s,D_c,D_m,D_j)$ is irrelevant iff each procedure is pure, side-effect free, and evaluated over the same $R$, $H_r$, $(\mathcal{C})$, $t$, and receipt-bound $\pi_i$.

If $P$ reads wall-clock time instead of $t$, then $D_c$ may vary by evaluation order. Therefore time is part of $(\mathcal{C})$, not ambient verifier state.

## 13. Threat Model

- **Attack class:** Binding/context  
  **Examples:** (failures defined in Section 4)  
  **Mitigations:** $H_r$, $id(\mathcal{C})$, shared $H_s$, strict mode; recoverability gate (Section 4.5)

- **Attack class:** Admissibility  
  **Examples:** authority laundering, capability escalation, stale delegation, path ambiguity  
  **Mitigations:** Merkle proofs, attenuation, revocation precedence, $canon_path$, root governance

- **Attack class:** Semantic  
  **Examples:** equivocation, downgrade, normalization bombs, resource substitution  
  **Mitigations:** $(id(\Sigma))$, $r^*$, bounds, resource commitments, lineage, $V_{lift}$

- **Attack class:** Namespace  
  **Examples:** squatting, aliasing, phase confusion, front-running  
  **Mitigations:** $(id(\Phi))$, $c_{name}$, membership proofs, admissibility-gated updates, batching

## 14. Complexity

- **Procedure:** $D_s$  
  **Construction:** $O(\lvert x \rvert)$  
  **Verification:** $O(1)$ after hash availability

- **Procedure:** $D_c$  
  **Construction:** $O(\lvert E \rvert)$  
  **Verification:** $O(\lvert path \rvert \cdot \log n)$

- **Procedure:** $D_m$  
  **Construction:** $T_\Sigma(\lvert x \rvert) \le B$  
  **Verification:** $O(\lvert \pi_m \rvert)$, or $O(k)$ trace steps

- **Procedure:** $D_j$  
  **Construction:** $O(1)$ plus map update  
  **Verification:** $O(\log N)$

Update costs are $(O(\log n))$ for Merkleized $G_c$ edge updates and $(O(\log N))$ for namespace updates. Typical targets are receipts below 10 KB, admissibility paths of 3--12 edges, logarithmic namespace proofs, and batchable signature and Merkle verification.

## 15. Ablation

- **Available commitments:** $H_c, H_m, H_j$  
  **Lost decidability:** state  
  **System class:** ungrounded governance evidence

- **Available commitments:** $H_s, H_m, H_j$  
  **Lost decidability:** admissibility  
  **System class:** semantic content-addressing without standing

- **Available commitments:** $H_s, H_c, H_j$  
  **Lost decidability:** meaning  
  **System class:** admissible state without regime-bound meaning

- **Available commitments:** $H_s, H_c, H_m$  
  **Lost decidability:** locality  
  **System class:** complete single-phase governance

- **Available commitments:** $H_s, H_m$  
  **Lost decidability:** admissibility, locality  
  **System class:** semantic archive

## 16. Primary Test Vector

Input:

```json
{"rule":"allow","limit":5}
```

Context:

```text
P=P_7
Sigma=Sigma_3
Phi=Phi_2
t=1700000000
id(\mathcal{C})=b3:77aa9011
```

Commitments, truncated:

```text
H_s=b3:4f91a2c8
H_c=b3:5180bb73
H_m=b3:8c02ef19
H_j=b3:220f19ca
H_r=b3:aa09c441
```

Witnesses:

```text
pi_s=state canonicalization proof
pi_c=Root->Org->Service->Key with Merkle siblings
[b3:a101,b3:9f22,b3:44de]
pi_m=parse/reduction trace under Sigma_3
pi_j=membership proof name_key|->H_s in M_Phi
```

Expected:

```text
verify(R,C)=(D_s=1,D_c=1,D_m=1,D_j=1)
```

Failure cases are given in Appendix C.

## 17. Unified Governance Kernel

The Unified Governance Kernel (UGK) instantiates the Three Hash Rule as a receipt discipline: a UGK receipt is a structured proof over independent governance questions rather than a signed object with metadata attached. The four commitments map directly onto UGK's verification surfaces, with $H_j$ activated only when phase-bound namespaces are in scope.

## Conclusion

The Three Hash Rule makes governance completeness a property of independent commitments and explicit decision procedures: state, admissibility, and meaning are separately committed, separately witnessed, and separately decided. $H_j$ extends the model to locality without enlarging the minimal complete core.

The resulting architecture is austere: object, evidence, meaning, and---when needed---phase. Each can fail independently. Each can be verified independently. Together they make governed systems inspectable, reproducible, and falsifiable.

## Appendix A: Receipt Schema

```text
Receipt {
  version: uint32
  mode: enum { ContextExternal, ContextBound, ReEvaluable }
  H_s: Hash
  H_c: Hash
  H_m: Hash
  H_j: Optional<Hash>
  H_r: Hash
  pi: WitnessFamily
}

WitnessFamily {
  pi_s: Witness
  pi_c: Witness
  pi_m: Witness
  pi_j: Optional<Witness>
}

Context {
  P: PolicyID
  Sigma: SemanticRegimeID
  Phi: PhaseID
  t: Time
}
```

## Appendix B: Error Taxonomy

```text
OK
NotApplicable
NonCanonical
ContextMismatch
ReceiptBindingFailure
ExpiredEdge
RevokedEdge
NoCanonicalPath
CapabilityEscalation
NormalizationFailure
ResourceBoundExceeded
LiftFailure
NamespaceNonMember
PhaseMismatch
InvalidMerkleProof
UnderRecordedCollapse
InvalidTransformProof
UnsupportedVersion
DomainTagCollision
ExternalResourceMissing
```

## Appendix C: Negative Test Cases

Expired edge:

```text
t=1800000000
Service->Key expired before t
verify(R,C)=(D_s=1,D_c=0,D_m=1,D_j=1)
reason_c=ExpiredEdge
```

Namespace non-member:

```text
pi_j proves absence of name_key in M_Phi
verify(R,C)=(D_s=1,D_c=1,D_m=1,D_j=0)
reason_j=NamespaceNonMember
```

Context mismatch:

```text
P=P_8
id(\mathcal{C}')!=id(\mathcal{C})
verify(R,C')=(D_s=1,D_c=0,D_m=0,D_j=0)
reason=ContextMismatch
```

Under-recorded collapse:

```text
Two receipts with distinct (id(P), id(Sigma)) but identical H_r
(context-external mode), no disambiguating collapse witness present.
core=(D_s=1, D_c=1, D_m=1, D_j=1)
binding=0
verify=reject
reason=UnderRecordedCollapse
```

The collapse itself does not defeat any individual core decision procedure: $D_s$, $D_c$, $D_m$, and $D_j$ all pass. Binding verification fails at the recoverability check (Section 4.5) because the receipt does not carry sufficient information to recover the distinguished governance facts. The receipt is inadmissible because binding verification is a required gate alongside the core decisions, not because admissibility ($D_c$) itself fails.

## Appendix D: Encoding and APIs

Receipts use a typed canonical schema equivalent to CBOR, SSZ, or another byte-stable typed encoding. Every field is length-prefixed, tagged, byte-order specified, and versioned. $H_r$ is always computed as a domain-separated hash tree over typed leaves. Algorithm agility uses multihash or multicodec-style identifiers.

```text
verify(R, C) -> [(Domain, Result, ErrorCode)]
prove_admissibility(G_c, path, C) -> pi_c
normalize(x, Sigma) -> (c_m(x), pi_m)
resolve(H_j, name, pi_j) -> H_s | NonMember
lift(H_m, Sigma_i, Sigma_j, pi_lift) -> H_m'
```

## Appendix E: Benchmarks

```text
G_c path depth vs D_c verification time
graph size vs Merkle proof size
normalization cost across Sigma classes
namespace size vs D_j cost
batch verification savings
adversarial graph inflation
normalization bombs
context mismatch attempts
witness splicing attempts
```

Reports should include construction cost, verification cost, witness size, receipt size, p50/p90/p99 latency, and memory footprint.

## Appendix F: Binding Configurations

The receipt binding mode is one degree of freedom in receipt design, with three admissible configurations:

- **Strict identity (preferential default).** Context folded into the identity; identities are self-describing; cross-references that carry only $H_r$ remain context-determinate.
- **Re-evaluable (opt-in exception).** Witnesses do not pin $id(\mathcal{C})$; a verifier may evaluate the receipt under a context it supplies. This shifts trust onto whoever supplies the context and must be labeled opt-in, never default.
- **Context-external with disambiguating collapse witness (admissible when warranted).** A stable cross-context bundle identity, with the conflation recorded so lineage stays recoverable. Selected only when a real situation needs a context-portable bundle handle.

When multiple configurations are admissible for a deployment, the selection rule is: enable the configurations the situation warrants; default to the preferential configuration (strict identity). The admissible space is not collapsed to a single point; the preferential point is the default.

## Appendix G: References

### G.1 Author's Related Work

Ableman Adam Ableman *Self-Certifying Proof-Carrying Identity*. Zenodo. https://doi.org/10.5281/zenodo.20114887

Ableman Adam Ableman *Cryptographic Admissibility and Jurisdiction*. Zenodo. https://doi.org/10.5281/zenodo.20602447

Ableman Adam Ableman *Constitutional Semantic Hashing*. Zenodo. https://doi.org/10.5281/zenodo.20248733

Ableman Adam Ableman *Cryptographic Phase*. Zenodo. https://doi.org/10.5281/zenodo.18503393

This paper (The Three Hash Rule): https://doi.org/10.5281/zenodo.20788617

---

### G.2 Self-Certifying Names, Keys, and Identity Infrastructure

Mazières, D. *Self-Certifying File System*. Ph.D. dissertation, Massachusetts Institute of Technology, 2000.

Mazières, D., Kaminsky, M., Kaashoek, M. F., and Witchel, E. “Separating Key Management from File System Security.” *Proceedings of the 17th ACM Symposium on Operating Systems Principles* (SOSP ’99), 1999, pp. 124–139. https://doi.org/10.1145/319151.319162

Fu, K., Kaashoek, M. F., and Mazières, D. “Fast and Secure Distributed Read-Only File System.” *Proceedings of the 4th USENIX Symposium on Operating Systems Design and Implementation* (OSDI 2000), 2000, pp. 181–196.

Benet, J. “IPFS — Content Addressed, Versioned, P2P File System.” arXiv:1407.3561, 2014. https://arxiv.org/abs/1407.3561

Smith, S. M. “Key Event Receipt Infrastructure (KERI).” arXiv:1907.02143, 2019. https://arxiv.org/abs/1907.02143

---

### G.3 Authorization, Trust Management, and Capability Security

Ellison, C., Frantz, B., Lampson, B., Rivest, R., Thomas, B., and Ylonen, T. “SPKI Certificate Theory.” RFC 2693, IETF, 1999. https://datatracker.ietf.org/doc/rfc2693/

Blaze, M., Feigenbaum, J., and Lacy, J. “Decentralized Trust Management.” *Proceedings of the 17th IEEE Symposium on Security and Privacy*, 1996, pp. 164–173. https://doi.org/10.1109/SECPRI.1996.502679

Lampson, B. W. “A Note on the Confinement Problem.” *Communications of the ACM*, vol. 16, no. 10, 1973, pp. 613–615. https://doi.org/10.1145/362375.362389

Levy, H. M. *Capability-Based Computer Systems*. Digital Press, 1984. ISBN 9780932376220.

Miller, M. S., Yee, K.-P., and Shapiro, J. S. “Capability Myths Demolished.” Technical Report SRL2003-02, Systems Research Laboratory, Johns Hopkins University, 2003.

---

### G.4 Proof-Carrying Code, Proof Systems, and Verified Computation

Necula, G. C. “Proof-Carrying Code.” *Proceedings of the 24th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages* (POPL ’97), 1997, pp. 106–119. https://doi.org/10.1145/263699.263712

Parno, B., Howell, J., Gentry, C., and Raykova, M. “Pinocchio: Nearly Practical Verifiable Computation.” *Proceedings of the 2013 IEEE Symposium on Security and Privacy*, 2013, pp. 238–252. https://doi.org/10.1109/SP.2013.47

Ben-Sasson, E., Chiesa, A., Genkin, D., Tromer, E., and Virza, M. “SNARKs for C: Verifying Program Executions Succinctly and in Zero Knowledge.” *Advances in Cryptology — CRYPTO 2013*, Lecture Notes in Computer Science, vol. 8043, 2013, pp. 90–108. https://doi.org/10.1007/978-3-642-40084-1_6

Ben-Sasson, E., Bentov, I., Horesh, Y., and Riabzev, M. “Scalable, Transparent, and Post-Quantum Secure Computational Integrity.” Cryptology ePrint Archive, Report 2018/046, 2018. https://eprint.iacr.org/2018/046

Ben-Sasson, E., Bentov, I., Horesh, Y., and Riabzev, M. “Fast Reed-Solomon Interactive Oracle Proofs of Proximity.” *45th International Colloquium on Automata, Languages, and Programming* (ICALP 2018), LIPIcs vol. 107, article 14. https://doi.org/10.4230/LIPIcs.ICALP.2018.14

---

### G.5 Term Rewriting, Semantics, and Logic-Based Policy

Baader, F., and Nipkow, T. *Term Rewriting and All That*. Cambridge University Press, 1998. https://doi.org/10.1017/CBO9781139172752

Ceri, S., Gottlob, G., and Tanca, L. “What You Always Wanted to Know About Datalog (And Never Dared to Ask).” *IEEE Transactions on Knowledge and Data Engineering*, vol. 1, no. 1, 1989, pp. 146–166. https://doi.org/10.1109/69.43410

Codd, E. F. “A Relational Model of Data for Large Shared Data Banks.” *Communications of the ACM*, vol. 13, no. 6, 1970, pp. 377–387. https://doi.org/10.1145/362384.362685

Halpern, J. Y., and van der Meyden, R. “A Logic for SDSI’s Linked Local Name Spaces.” arXiv:cs/0001026, 2000. https://arxiv.org/abs/cs/0001026

Halpern, J. Y., and van der Meyden, R. “A Logical Reconstruction of SPKI.” arXiv:cs/0208028, 2002. https://arxiv.org/abs/cs/0208028

---

### G.6 Verifiable Credentials, Content Addressing, and Supply-Chain Attestation

Sporny, M., Thibodeau, T. Jr., Herman, I., Cohen, G., and Jones, M. B., eds. *Verifiable Credentials Data Model v2.0*. W3C Recommendation, 15 May 2025. https://www.w3.org/TR/vc-data-model-2.0/

Multiformats Project. *CID: Self-Describing Content-Addressed Identifiers for Distributed Systems*. https://github.com/multiformats/cid

IPLD Project. *InterPlanetary Linked Data Specifications*. https://ipld.io/specs/

Torres-Arias, S., Afzali, H., Kuppusamy, T. K., Curtmola, R., and Cappos, J. “in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes.” *Proceedings of the 28th USENIX Security Symposium*, 2019, pp. 1393–1410.

in-toto Project. *in-toto Attestation Framework*. https://github.com/in-toto/attestation

Supply-chain Levels for Software Artifacts (SLSA). *SLSA Specification*. https://slsa.dev/spec/

Supply-chain Levels for Software Artifacts (SLSA). *SLSA Provenance*. https://slsa.dev/spec/v1.0/provenance

---

### G.7 Cryptographic Commitments and Authenticated Data Structures

Merkle, R. C. “Protocols for Public Key Cryptosystems.” *Proceedings of the 1980 IEEE Symposium on Security and Privacy*, 1980, p. 122. https://doi.org/10.1109/SP.1980.10006

Merkle, R. C. “A Digital Signature Based on a Conventional Encryption Function.” *Advances in Cryptology — CRYPTO ’87*, Lecture Notes in Computer Science, vol. 293, 1988, pp. 369–378. https://doi.org/10.1007/3-540-48184-2_32

Goodrich, M. T., Tamassia, R., and Triandopoulos, N. “Efficient Authenticated Data Structures for Graph Connectivity and Geometric Search Problems.” arXiv:0908.4116, 2009. https://arxiv.org/abs/0908.4116

Papamanthou, C., Tamassia, R., and Triandopoulos, N. “Authenticated Hash Tables.” *Proceedings of the 15th ACM Conference on Computer and Communications Security* (CCS ’08), 2008.

---

### G.8 Dense Hashing and Compact Indexing Context

Yao, A. C. “Uniform Hashing Is Optimal.” *Journal of the ACM*, vol. 32, no. 3, 1985, pp. 687–693. https://doi.org/10.1145/3828.3836

Farach-Colton, M., Krapivin, A., and Kuszmaul, W. “Optimal Bounds for Open Addressing Without Reordering.” *Proceedings of the 65th IEEE Symposium on Foundations of Computer Science* (FOCS 2024), 2024, pp. 594–605. https://doi.org/10.1109/FOCS61266.2024.00045

Bender, M. A., Kuszmaul, W., and Zhou, R. “Tight Bounds for Classical Open Addressing.” *Proceedings of the 65th IEEE Symposium on Foundations of Computer Science* (FOCS 2024), 2024, pp. 636–657. https://doi.org/10.1109/FOCS61266.2024.00047

Bender, M. A., Conway, A., Farach-Colton, M., Kuszmaul, W., and Tagliavini, G. “Tiny Pointers.” arXiv:2111.12800, 2021. https://arxiv.org/abs/2111.12800

Bender, M. A., Farach-Colton, M., Kuszmaul, J., Kuszmaul, W., and Liu, M. “On the Optimal Time/Space Tradeoff for Hash Tables.” *Proceedings of the 54th Annual ACM SIGACT Symposium on Theory of Computing* (STOC 2022), 2022, pp. 1284–1297. https://doi.org/10.1145/3519935.3519969

## Corpus-Wide Reference Positioning

This paper argues that the Three Hash Rule: a governance-completeness model in which object state, admissibility, and meaning are committed independently as $H s$, $H c$, and $H m$. Its nearest external comparison fields are crypto, governance, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: A valid hash, signature, or inclusion proof establishes a bounded cryptographic relation, not meaning, authority, safety, or jurisdiction by itself. A written constitution can legitimate domination as easily as constrain it unless amendment, participation, enforcement, and appeal remain effective in practice. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** Anders Rundgren, Bret Jordan, and Samuel Erdtman. *JSON Canonicalization Scheme (JCS)*. RFC 8785, 2020. https://www.rfc-editor.org/rfc/rfc8785 **Relationship:** Adjacent canonicalization standard relevant to stable cryptographic commitments.

**[E2]** Ben Laurie et al. *Certificate Transparency Version 2.0*. RFC 9162, 2021. https://www.rfc-editor.org/rfc/rfc9162 **Relationship:** Adjacent append-only Merkle-log standard for inclusion and consistency evidence.

**[E3]** Manu Sporny et al., eds. *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 19 July 2022. https://www.w3.org/TR/did-core/ **Relationship:** Adjacent decentralized identity standard; identifier resolution is not assumed to settle semantic standing or jurisdiction.

**[E4]** Juan Benet. "IPFS - Content Addressed, Versioned, P2P File System." 2014. arXiv:1407.3561. https://arxiv.org/abs/1407.3561 **Relationship:** Predecessor content-addressed network architecture; content identity is compared with, not treated as sufficient for, semantic jurisdiction.

**[E5]** Elinor Ostrom. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press, 1990. DOI: 10.1017/CBO9780511807763. https://doi.org/10.1017/CBO9780511807763 **Relationship:** Predecessor institutional account of rule-governed collective action and polycentric governance.

**[E6]** Wil Waluchow and Dimitrios Kyritsis. "Constitutionalism." *Stanford Encyclopedia of Philosophy*, substantive revision 2023. https://plato.stanford.edu/entries/constitutionalism/ **Relationship:** Adjacent legal-philosophical account of limited authority; included to expose differences between political and computational constitutionalism.

**[E7]** Lawrence Lessig. *Code: Version 2.0*. Basic Books, 2006. https://codev2.cc/ **Relationship:** Predecessor argument that software architecture regulates behavior; the paper's contribution may be to make such regulation inspectable and revisable.

### Ableman corpus

**[A1]** Adam Ableman. *Constitutional Semantic Hashing: Governed Commitment Schemes for Semantic Provenance, Admissibility, and Constitutional Continuity*. Ableman Corpus current edition; work identity `PAPER.PUB.20248734`;  
source SHA-256  
`B1DAC3E2CD4D57BAFBF6462BA6ACFFF7CF120CDB7FA37D0C173525744CC0A2F0`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *Cryptographic Admissibility and Jurisdiction*. Ableman Corpus current edition; work identity `PAPER.PUB.20602448`;  
source SHA-256  
`6094338D8706F63E8787A5E8DCF40F8A651C0FC3E5EA776DD61791566D094D38`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *Self-Certifying Proof-Carrying Identity for Registrar-Free Namespace Networks*. Ableman Corpus current edition; work identity `PAPER.PUB.20114888`;  
source SHA-256  
`1AFDBD390D3BF28224727FE150FFB30CA1810D997778CC8702B6CD20C4FA5B45`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Semantic Hashing: Hashes as Declared Equivalence Classes of Meaning*. Ableman Corpus current edition; work identity `PAPER.PUB.18500533`;  
source SHA-256  
`7DA63A76DDF492FFC289F486923FB430879DC148CF3BB16EB0E755E2D4AB9C14`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

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

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.20788617](https://doi.org/10.5281/zenodo.20788617)
