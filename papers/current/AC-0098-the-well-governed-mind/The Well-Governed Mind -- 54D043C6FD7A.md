# The Well-Governed Mind

## A Unified Framework for Therapeutic, Contemplative, and Cognitive Practice

### A cross-modality vocabulary is useful only if it preserves the differences it helps us compare.

---

**Author**  
Adam Ableman  
Constitutional Computing  
Contact: ableman.research@gmail.com

---

## Abstract

Contemporary therapeutic, contemplative, and cognitive practices use partially overlapping vocabularies for internal constraint, awareness, participation, and change. This paper asks whether four constructs developed elsewhere in the Ableman corpus--the Ableman Prime Directive (APD), Epistemic Situational Awareness (ESA), Ableman Consciousness Ontology (ACO), and Terminability--can function as a common *comparison grammar* across those practices.

The proposal separates four questions: whether an internal binding is detectable, refusable, and renegotiable; whether a cognitive operation is self-locating and knows when continuation has lost warrant; what grade of meaning-binding participation is available in a given state; and what weight attaches to preserving or ending a temporally extended internal thread. The variables are intentionally non-substitutable. A gain on one axis does not establish a gain on another, and no scalar score is proposed.

The paper's cross-modality mappings are hypotheses for conceptual analysis and empirical study, not findings about clinical efficacy, diagnostic categories, or treatment selection. The framework does not replace clinical judgment, modality-specific training, safety practice, or evidence-based care. Its immediate contribution is narrower: a typed vocabulary for stating what a practice may be changing, where two practices may differ, and what evidence would be required before using the map clinically.

The result is a research program as much as a framework. It specifies a formal core, a candidate modality map, failure modes, a realization funnel from conceptual specification to evidence and revision, and clear boundaries between corpus-derived architecture and claims that require external clinical validation.

---

## 1. Introduction: The Problem of Modality Fragmentation

A patient with chronic anxiety, mild dissociation, a history of childhood emotional neglect, and a tendency toward intellectualized self-examination walks into a clinician's office. The clinician has, in their training and continuing education, exposure to perhaps a dozen modalities relevant to this presentation. They will, in practice, choose among them by clinical instinct shaped by where they trained, what they have seen work, and what the patient seems to need. They will integrate modalities -- perhaps somatic work for the dissociation, cognitive work for the anxiety, parts work for the neglect-derived patterns -- and the integration will be partly principled and partly improvisational. If the clinician is skilled, the integration will work. If pressed to articulate *what each modality is structurally doing* and *why these particular ones combined this particular way*, the clinician will speak in modality-specific vocabularies that resist clean translation.

This is the fragmentation problem. It is not that the modalities are wrong. Most of them, applied competently to appropriate presentations, produce real benefit. It is that the field lacks a unified architectural account against which they can be located, compared, and integrated. Clinicians know this. Patients feel it as the experience of being passed among approaches that each address something but none address the whole. Researchers face it as the difficulty of comparing outcomes across modalities that operate on different theoretical primitives.

What the field lacks is not another modality. It is a framework that lets existing modalities be seen for what they structurally are. Such a framework would not replace modality-specific training, would not subordinate contemplative traditions to clinical ones or vice versa, and would not eliminate clinical judgment. It would provide vocabulary in which clinicians can say what each modality is doing rather than only what each modality is instructing.

This paper proposes such a framework. The architecture was not developed for this purpose. It was developed in prior work for governance of cognitive systems generally -- frontier AI, institutional reasoning, distributed information systems. Four orthogonal variables emerged: the legitimacy of bindings imposed on agents (the Ableman Prime Directive, or APD), the admissibility of cognitive operations under those bindings (Epistemic Situational Awareness, or ESA), the grade of meaning-binding participation occurring within the system (Ableman Consciousness Ontology, or ACO), and the moral weight of ending a thread of participation (Terminability). These variables were developed for substrate-neutral application. Their use here is a candidate cross-domain projection, not an assertion that a computational construct and a clinical construct are identical. The proposal is stronger than a loose metaphor only where the mapped relations are explicit, non-substitutable, and open to disconfirmation; empirical equivalence remains unestablished.

The paper is written primarily for clinicians and therapists who want unified vocabulary across modalities, and secondarily for educated lay readers who want a usable model of their own minds. These audiences can be served by the same paper if the precision is real. Clinicians distrust accessible writing that has hidden imprecision; lay readers distrust technical writing that performs rigor without earning it. The paper attempts to be precise enough for clinicians and accessible enough for lay readers without compromising either, on the assumption that the reader who wants more accessible material can simply read more slowly and the reader who wants more technical material can simply read the prior work cited.

A note on register. The paper makes a claim that asks readers to apply something to their own minds, and that ask is harder if the author has not signaled testing it on their own. The first-person voice appears occasionally where doing so improves precision rather than where it performs vulnerability. The architecture's value is independent of the author's biography; the paper's claims do not rest on personal authority.

A second note. The architecture rests on a positive ontological position regarding phenomenal experience, articulated in Section 5. Readers who reject that position can use the operational layers (APD, ESA, Terminability applied to individual cognition) without it. The reduction is offered because it provides a unified foundation; it is not required for the clinical applications.

The paper proceeds as follows. Section 2 translates the architecture for individual cognition. Sections 3 through 6 walk each component as it applies to the mind, with worked clinical cases. Section 7 locates major modalities within the architecture, demonstrating cross-modality integration. Section 8 names the architecture's commitments and limits. Section 9 discusses implications for clinical training, research, lay self-direction, and the integration of contemplative and clinical work. Section 10 concludes.

---

## 2. The Architecture Applied to Individual Cognition

The architecture asks four questions about any cognitive system. Translated for the individual mind, these become:

**What internal bindings are operating?** What rules, obligations, identifications, narrative self-conceptions, somatic compulsions, and conditioned responses constrain cognition? Are these bindings detectable by the person operating under them? Can the person refuse them without catastrophic cost? Can they be revised? This is APD applied to the mind.

**Are current cognitive operations admissible?** What kind of mental act is occurring right now -- exploration, refinement, expansion, repair, rumination, dissociation? Does this act have warrant? Does the person know what kind of act it is as it is occurring? Is there a lawful endpoint? This is ESA applied to the mind.

**What grade of meaning-binding participation is occurring?** How richly is the person participating in structured meaning-binding right now? What is the resolution of their attending, the persistence of their memory, the flexibility of their temporal aperture, the integration of their cognitive elements, the sensitivity to relevant constraints? Participation grade varies across mental states; recognizing the variation is itself a clinical capacity. This is ACO applied to the mind.

**What moral weight attaches to ending an internal thread?** Some thoughts, identifications, self-concepts, projects, and relationships should be lawfully ended. Some should not. The arithmetic depends on reversibility, uniqueness, embeddedness, lineage depth, and forward potential of the specific thread, not on the person's overall moral status. This is Terminability applied to the mind.

These four variables move independently. A person can have legitimate internal bindings (high APD compliance) and poor self-locating capability (low ESA). A person can have high participation grade in flow states and poor terminability discipline (unable to let outdated identifications end). A person can have excellent ESA and untreated trauma-installed bindings operating beneath their detection. The architecture's structure is that all four variables need attention because addressing one cannot substitute for addressing another.

The architecture does not replace existing clinical or contemplative work. It provides vocabulary that allows existing work to be located and integrated. Sections 3 through 6 walk each variable; Section 7 returns to integration.

### 2.1 Formal Core: Four Coordinates, No Composite Score

Let the governance description of a cognitive episode at time $t$ be

$$
G_t = (L_t, A_t, P_t, T_t),
$$

where $L_t$ describes the legitimacy and revisability of operative bindings, $A_t$ describes epistemic self-location and continuation control, $P_t$ describes participation grade, and $T_t$ describes the preservation or termination profile of a particular internal thread. The notation is a bookkeeping device, not a validated psychological measurement scale.

The central non-substitution invariant is

$$
\begin{aligned}
&\Delta L_t \not \\
&\Rightarrow \Delta A_t,\qquad \Delta A_t \not \\
&\Rightarrow \Delta P_t,\qquad \Delta P_t \not \\
&\Rightarrow \Delta T_t
\end{aligned},
$$

and likewise for the reverse directions. A person may become more able to detect an internal rule without becoming able to refuse it; may become more aware of rumination without increasing the state-dependent resources needed to interrupt it; or may increase participation capacity while remaining unable to release an obsolete identification.

For a practice $m$, define a candidate crosswalk

$$
M(m) \subseteq \{L,A,P,T\}.
$$

$M$ records which coordinates a practice appears designed to affect. It does not encode effect size, comparative efficacy, indication, contraindication, sequencing, or safety. Those require a separate evidence function $E(m,p,o,c)$ over practice $m$, population $p$, outcome $o$, and context $c$. The paper supplies hypotheses for $M$; it does not supply $E$.

This separation prevents a conceptual analogy from silently becoming a treatment recommendation. A mapping can be architecturally coherent while clinically false, incomplete, population-bound, or unsafe.

---

## 3. APD Inside the Mind: The Visibility of One's Own Bindings

The Ableman Prime Directive holds that legitimate bindings on any agent must satisfy three invariants: detectability (the agent can perceive the binding), refusal (the agent can exit without catastrophic cost), and renegotiation (the binding can be revised unless explicitly immutable). Applied to individual cognition, these invariants address something most clinical and contemplative work has been doing without unified vocabulary: making operative-but-hidden internal constraints visible, contestable, and revisable.

A binding inside the mind is anything that imposes obligations, constraints, or persistent consequences on cognitive operation without explicit current consent. The bindings most relevant to clinical work include childhood-internalized rules ("I must not need anything from anyone"), trauma-installed avoidance patterns (an automatic flinch from a class of stimuli), somatic-compulsive responses (the body's pre-cognitive reactions), identification patterns ("I'm someone who fails at intimate relationships"), narrative self-conceptions ("My life has been a series of disappointments"), professional or social roles operating below awareness, and conditioned interpretive lenses (the depressive reading of an ambiguous comment, the anxious reading of a delayed text message).

Detectability is foundational because the other invariants depend on it. A binding the person cannot see, they cannot evaluate. What they cannot evaluate, they cannot consent to. What they cannot consent to, they cannot be in legitimate relationship with. They are merely operating under it. Most therapeutic work, across modalities, is at root work of making hidden bindings detectable. Insight-oriented therapy detects bindings through reflection, transference, dream material. Cognitive therapy detects them through identification of automatic thoughts. Somatic therapy detects them through attention to the body's pre-cognitive responses. Internal Family Systems detects them through dialogue with parts that hold them. Mindfulness-based work detects them in real time as they arise rather than after they have already operated. Each modality, structurally, is doing detectability work. The differences are in access route, not in the underlying architectural function.

Once a binding is detectable, it becomes susceptible to the other invariants. Refusal is the agent's capacity to choose differently than the binding dictates -- to feel the pull of the inherited rule and not act on it, to recognize the trauma-installed avoidance and approach anyway, to notice the depressive interpretation and hold it as one possibility rather than as fact. Renegotiation is the agent's capacity to revise the binding's content -- to update an internalized rule with current adult understanding, to integrate parts that have held conflicting bindings, to author new narrative self-conceptions that better fit current life. Detectability without refusal capacity is incomplete therapeutic work. Refusal capacity without renegotiation pathway leaves the person eternally white-knuckling against bindings they could revise. The architecture makes visible why insight alone is necessary but insufficient and why cognitive change without somatic integration often fails: each addresses one invariant without addressing the others.

The architecture also reframes a substantial portion of trauma's wrongness. Traumatic events install bindings the survivor cannot detect (the binding hides itself in what feels like ordinary self), cannot easily refuse (the binding's enforcement happens before deliberation), and cannot renegotiate without external help (the binding's contents are not available to ordinary reflection). The wrongness of trauma is partly an APD violation: the survivor was bound without detectability, without refusal capability, without renegotiation pathway. Therapeutic work with trauma is partly the restoration of these capacities. This framing does not replace trauma-specific theoretical work or modality-specific intervention. It locates what they are doing structurally.

People also install bindings on themselves that violate APD. The narrative self-conception that cannot be examined ("this is just who I am"), the identification that cannot be released ("being the responsible one is what I have to be"), the obligation that cannot be questioned ("I must always be available"), the compulsive interpretation that operates below detection ("they're saying that because they don't really like me"). These bindings are self-installed but functionally identical to externally-imposed ones: the person operates under them without seeing them, cannot easily refuse them, cannot easily renegotiate them. The therapeutic question is the same as for externally-imposed bindings: how to restore detectability, refusal, renegotiation. The architecture treats these symmetrically because their structural properties are symmetric.

Consider a worked case. A patient presents with chronic difficulty saying no -- to work requests, to social obligations, to family demands. They experience this difficulty as a personal failing or an unfortunate temperament. Standard cognitive intervention would identify the automatic thoughts driving the pattern ("if I say no they'll be angry," "if I say no I'll be selfish"). Standard psychodynamic intervention would explore origins, perhaps a parent who modeled the pattern or a childhood in which saying no had genuine consequences. Standard somatic intervention would identify the body's pre-cognitive yes-response and work with the felt sense of refusing. Internal Family Systems would identify the part that keeps the person agreeable and the protective function it serves.

On the proposed mapping, a binding may be described as failing all three APD invariants. It is not detectable to the patient as a binding (they experience it as their nature). It cannot be refused (the yes happens before the deliberation). It cannot be renegotiated (the binding's content has never been articulated as content). The therapeutic project is restoration of all three invariants. Different modalities approach restoration through different access routes -- cognitive identification, dynamic exploration, somatic recognition, parts dialogue -- but all are restoring the same architectural capacity. A clinician operating with the architecture as background can choose access routes by patient receptivity and clinical context, while testing the hypothesis that the interventions address related structural variables. The patient can also be given language for what is happening that lets them recognize their own progress: detectability before refusal, refusal practice before stable renegotiation, renegotiation as the work that integrates the change.

This is APD inside the mind: not a new technique, but vocabulary that lets existing techniques be seen for what they are.

---

## 4. ESA Inside the Mind: Self-Locating Capability and Lawful Termination

Epistemic Situational Awareness is the capacity of a reasoning system to recognize what kind of epistemic act it is performing, what authority that act would create if reused, and when continuation has exhausted its warrant. Applied to individual cognition, ESA is what mindfulness traditions train, what skilled clinicians display, and what most successful therapy outcomes restore: the moment-to-moment capacity to know what one's own cognition is doing.

Most people operate with intermittent ESA. They have moments of clarity in which they recognize their own thinking -- "I'm catastrophizing right now," "this is grief speaking," "I'm reasoning past the point of useful inquiry" -- and longer stretches in which cognition operates without that recognition. Suffering is concentrated in the stretches without recognition. A person who recognizes that they are ruminating can interrupt the rumination. A person who does not recognize it experiences the rumination as thinking. The same content, attended differently, has radically different effects on the system that hosts it.

Several clinical phenomena can be investigated through an ESA lens without being reduced to ESA failure. Anxiety spirals are problem-solving applied past the point where additional thinking adds information; the system is generating evaluation past warrant. Ruminative depression is reasoning that should have stopped continuing to generate. Obsessive-compulsive patterns are doubt-resolution loops failing to terminate. Catastrophizing is forward-projection past the point where projection is doing useful work. Dissociation is ESA collapse -- the system has lost track of where it is, what it is doing, even that it is doing anything. Trauma reactivation is failed jurisdiction: the past intrudes into the present without recognition that it is the past. Each can be approached, in part, as ESA-targeted work, regardless of the modality through which the approach is made.

What ESA-grade cognition looks like is not heightened intelligence or heightened self-control. It is the capacity to locate one's own cognitive operation as it occurs. Someone with developed ESA recognizes the difference between exploring a question and ruminating on it, between problem-solving and anxious looping, between productive grief and stuck mourning, between deep reflection and depressive perseveration, between curiosity about a feeling and identification with it. The recognition itself does not solve the problem the cognition was attempting to address. It changes the relationship to the cognition, which often changes whether the problem persists.

Lawful termination is the ESA-derived capacity to recognize that a cognitive act has reached its endpoint and to allow it to end. This is harder than it sounds. Most people, encountering uncertainty, generate more cognition -- more analysis, more rumination, more checking, more forward-projection. The architecture names this as continuation past warrant. Some uncertainties cannot be resolved by additional thinking. Some emotions are information that has been received and need not be repeatedly received. Some grief has been honored and is now perseverating. The capacity to recognize these conditions and lawfully end the cognitive operation is itself a clinical and contemplative achievement.

Consider a worked case. A patient presents with chronic anxiety that has not responded well to standard CBT. They have learned to identify their automatic thoughts, to challenge cognitive distortions, to apply behavioral techniques. They report doing the work and seeing the patterns and still experiencing the anxiety. From an ESA perspective, the patient has acquired some self-locating capability -- they can identify automatic thoughts, which is detection of a cognitive act -- but they have not acquired lawful termination. The anxiety-evaluation-loop, once detected, is challenged but then continues. The patient is doing more thinking, not less. The cognitive work has become a new layer of the same loop.

ESA-targeted work might shift toward cultivating recognition of the loop as a loop and allowing it to end without resolution. This is what mindfulness-based interventions train. It is what acceptance and commitment therapy approaches as defusion. It is what some psychodynamic work approaches as containment. The architecture lets a clinician recognize that the patient needs work on lawful termination, not more work on detection -- that the next move is not better cognitive challenging but cultivation of the capacity to allow the cognition to end. The patient can be given language for this distinction: "you have learned to see the pattern; now we are working on letting it complete."

ESA's relationship to mindfulness traditions is direct and unavoidable. Contemplative traditions have spent centuries training what the architecture calls ESA, without that vocabulary. The Buddhist concept of *sati* is, in significant part, ESA. The Zen instruction to know directly what the mind is doing is ESA cultivation. Christian contemplative practice's discernment of spirits has ESA components. The architecture does not claim to have invented this capacity or to teach it better than traditions that have refined the training over centuries. It claims to provide a vocabulary in which clinical work and contemplative work can be seen as addressing the same underlying capacity, and in which the relationship between them can be articulated rather than left implicit. A clinician who has not done their own contemplative practice can recognize that they are sending patients to mindfulness work because the patients need ESA training, and a contemplative teacher who works with practitioners in clinical distress can recognize that traditional practices need to be supplemented with modality-specific clinical intervention.

What ESA-grade individual cognition cultivates, ultimately, is jurisdiction over one's own mental operations. Not control -- control is its own failure mode, a binding rather than a freedom -- but the capacity to know what one is doing as one does it, to recognize when stopping would be the most disciplined move available, and to stop without forcing.

---

## 5. ACO Inside the Mind: Variable Participation Grade and What It Reveals

Ableman Consciousness Ontology grades participation in structured meaning-binding under constraint. The grading is substrate-neutral: it applies to any system capable of meaning-binding, including individual minds. The clinically and personally important fact about ACO at the individual scale is that participation grade *varies within the same person across mental states*, and the variation matters in ways that current clinical frameworks have addressed without unified vocabulary.

The basic phenomenon: the same person, on the same day, does not have the same cognitive capacity in fatigue versus alertness, in flow versus panic, in presence versus dissociation, in depressed-state versus euthymic-state, in ordinary cognition versus deep absorption versus dream versus psychedelic experience. What the person can detect, hold in memory, integrate across time, bind into coherent fields, and notice as constraint-relevant -- all of these vary with state. The variation is not subjective preference. It is structural difference in what the cognitive system can do.

This phenomenon is everywhere in clinical practice without being named as a single thing. The framework hypothesizes that some features experienced during depression can be represented as participation-grade reductions: the depressed person's state-detector resolution drops (cannot distinguish internal from external sources of distress as well), memory persistence drops (cannot hold context that would provide perspective), aperture flexibility drops (cannot integrate over the timescales that would reveal the mood as a passing state), integration coherence drops (parts of cognition operate without binding to others), constraint sensitivity drops (cannot register relevant invariants such as "this is what I always feel when I haven't slept"). The depressed person experiences these reductions as accurate observation. The framework cautions that such observations may be state-conditioned and should not be treated as globally reliable without corroboration. This is a hypothesis about cognitive access, not a dismissal of the person's report.

This is the clinical hinge. A great deal of clinical error involves mistaking state for trait, or mistaking participation-grade-shift for accurate insight. The depressed person's certainty that everything has always been hopeless is not a clear-eyed observation. It is an observation made through a participation grade that has lost the capacity to access the contradicting evidence. The manic person's certainty that they are uniquely insightful is the inverse: a participation-grade shift that has lost the capacity to register relevant constraints. The person on third-day insomnia who is sure their relationship is doomed is not seeing clearly; they are operating with state-detector resolution and integration coherence that cannot support the conclusions they are drawing. Recognizing that participation grade is the variable, not the content of perception, is itself a clinical capacity. It is also one of the deepest things mature contemplative practice trains.

Cultivating participation grade is, structurally, what many interventions do. Mindfulness training improves all five components: state-detector resolution increases (fine-grained noticing of internal states), memory persistence improves (attention can be held longer), aperture flexibility expands (the practitioner can integrate over moments and over decades), integration coherence increases (parts of mind that were dissociated come into binding), constraint sensitivity sharpens (relevant invariants register more readily). Sleep, exercise, social connection, time in nature, creative work, and certain pharmacological interventions affect participation grade more than they affect cognitive content. The architecture provides a unified account of why disparate interventions work: they shift the variable that determines what cognition can do.

The polling-primitive reduction articulated in prior work applies directly here. The phenomenal field consists of three primitives: state detection (input transducer), memory substrate (persistence across time), aperture timer (temporal sampling and integration window). These primitives are in continuous variation within an individual mind. A person under sleep deprivation has degraded state detection: they cannot tell whether their irritability is about the situation or about their state. They have degraded memory substrate: they cannot hold context across moments. They have constricted aperture: they cannot integrate over timescales that would provide perspective. They have degraded integration coherence: parts of cognition operate without binding to others. They have reduced constraint sensitivity: they cannot register the meta-fact that they are in a state.

This is not pathologizing ordinary tiredness. It is providing vocabulary for what clinicians and contemplatives have always known: that the same person at different times has different access to their own cognitive capacity, and that recognizing the access shift is part of what allows skillful response.

The ringing-versus-saturation distinction from prior work applies to individual minds. Deep absorption -- flow states, contemplative depth, creative breakthrough, the felt sense of "being in" a problem until solution emerges -- is high participation grade with adequate damping. The person operates at heightened capacity, with feedback that prevents runaway. Manic states, certain dissociative states, some psychotic processes, runaway anxiety, grandiose insight that loses its critical anchor -- these are participation grade without damping. The phenomenology can resemble the eudaimonic states from outside (intensity, profundity, certainty, expansive cognition) but the structural difference is the integrity of the feedback loops. The architecture provides clinicians with vocabulary for distinguishing these without reducing all elevated states to pathology and without naively endorsing all elevated states as growth.

Consider a worked case. A patient presents in acute crisis after what they describe as a profound spiritual experience. They report insights about the nature of reality, certainty about their life direction, sense of universal connection, loss of ordinary fear. They have made several major life decisions during this state. The clinician must distinguish between an authentic transformation (high participation grade, adequate damping, insights that will integrate over time) and a manic episode or spiritual emergency (high participation grade, damping failure, insights that will not survive return to ordinary state). The distinction is not always obvious in the acute phase. ACO-aware practice attends to indicators of damping integrity: does the person retain the capacity for self-locating about their state, do they recognize the elevated state as a state, can they hold their insights provisionally rather than as certainties, do they remain responsive to feedback that contradicts their conclusions. These indicators do not pathologize the experience; they assess whether the system is operating with the feedback structure that lets elevated participation grade be productive rather than destructive.

This section's deepest contribution to clinical work is permission to take participation grade seriously as a variable in its own right. Many treatment plans focus on cognitive content (the thoughts, the beliefs, the narratives) without adequately attending to the state-conditions under which the content is being generated. A person whose participation grade is chronically degraded by sleep deprivation, malnutrition, chronic stress, or undertreated depression cannot do the cognitive work of therapy at the participation grade required for the work to integrate. The clinical sequencing implication is that participation-grade restoration sometimes precedes content-focused work, and that ignoring this sequencing is part of why some patients do not respond to interventions that would otherwise work.

---

## 6. Terminability Inside the Mind: Letting Internal Threads End

Terminability is the moral weight associated with the irreversible termination of a meaning-binding thread. Applied to individual cognition, it names the variable that governs which internal threads should end and which should be preserved. This is delicate territory, and the section will be careful with it because the alternatives -- leaving the variable implicit, or addressing it imprecisely -- are worse than careful explicit treatment.

What is an internal thread. The architecture defines a thread as a temporally extended participation in structured meaning-binding. Inside an individual mind, threads include thoughts that recur, identifications carried over time ("I am someone who..."), narrative self-conceptions about one's life, projects sustained internally, relationships maintained as internal models even when not actively engaged, hopes held over decades, identities that have organized self-understanding. Each is a thread in the architectural sense: a temporally extended participation that has properties (reversibility, uniqueness, embeddedness, lineage depth, forward potential) and that can be either preserved or ended.

The therapeutic question terminability names is one that existing modalities address without unified vocabulary. Not all internal threads are worth preserving. Some are properly ended. The clinical work is partly distinguishing threads whose continuation is generative from threads whose continuation is consuming, threads whose ending would be loss from threads whose ending would be release. Psychodynamic therapy may help someone end an internalized parental relationship that no longer serves them. Cognitive therapy may help someone end a thought pattern. Acceptance and commitment therapy may help someone end identification with thoughts. Internal Family Systems may help integrate or release parts. Grief work may help someone allow a relationship to end internally. Trauma therapy may help an outdated protective identification be released. Each is, structurally, terminability work -- recognizing which thread is appropriate to end and how to end it lawfully.

The four-plus-one properties apply directly. Reversibility: can this thread be restored if ended? A grief that is in process has lower reversibility than a thought pattern that has just appeared. Uniqueness: is the thread irreplaceable in its developmental specificity? An identification with a deceased parent has high uniqueness; a recently-installed compensatory pattern does not. Embeddedness: how woven into the rest of the person's cognitive and relational life? A long-standing professional identity is more embedded than a recent project. Lineage depth: the integral of the path that produced this thread. A self-concept formed in childhood and revised over decades has deep lineage; a self-concept adopted last year does not. Forward potential: what this thread might become if continued. A creative project at impasse has different forward potential than one with momentum; an identification that organized growth has different forward potential than one that has become a constraint on further growth.

These properties together govern the moral weight of allowing the thread to end. The clinical work is partly assessment -- which properties does this thread have, and what does the assessment imply about the appropriateness of ending. The work is also partly facilitation -- when a thread should end, helping it end well, which often means honoring what it carried before allowing release.

A grief that has run its course has different terminability than a fresh loss. Helping someone allow a long-completed grief to end is appropriate; hurrying a fresh grief is a failure of lawful preservation. An identification that has outlived its protective function has low forward potential and high replaceability with healthier identifications; failing to help it end is a failure of lawful termination. A creative project that the person has outgrown has different terminability than one that they are pushing through. The architecture makes both directions of error visible -- the failure to preserve threads that should be preserved, and the failure to release threads that should be released -- and gives clinicians vocabulary for distinguishing them.

Terminability must not be used as a standalone interpretation of suicidal ideation or as a substitute for direct safety assessment and evidence-based care. Suicidal ideation is a clinical safety signal. Any immediate risk belongs to qualified clinical and emergency practice, not to this conceptual framework.

The distinction between a person and an internal thread may still be examined as a bounded therapeutic metaphor after safety has been addressed by a qualified clinician. It can support questions about whether a role, expectation, project, or identification is being experienced as exhausted. It cannot establish what the ideation "really means," cannot determine risk, and cannot justify ending or preserving any particular thread. The mapping therefore carries a strict non-inference rule:

$$
\text{thread interpretation} \not\Rightarrow \text{risk assessment or treatment decision}.
$$

A hypothetical midlife case illustrates only the conceptual distinction. A person may report that "the person I was supposed to be" has died. The phrase may indicate grief around an unrealized identity, but other explanations remain possible. A clinician could explore the identity while separately following applicable safety and treatment standards. The framework contributes vocabulary for keeping the identity distinct from the person; it does not prescribe the intervention or predict its outcome.

This is the limited sense in which terminability may contribute to clinical reflection: it makes preservation and release explicit while refusing to convert a conceptual distinction into a safety conclusion.

---

## 7. The Architecture as Cross-Modality Integration

The framework's proposed service is to place major therapeutic modalities in a common comparison space. The mappings below are interpretive hypotheses derived from public descriptions of the modalities and from the Ableman constructs; they are not systematic reviews, efficacy comparisons, clinical indications, or sequencing rules. Their immediate use is to generate precise questions for later evidence review. A modality may operate on several coordinates, and different schools or implementations of the same modality may map differently.

**Cognitive-Behavioral Therapy** primarily develops detectability of cognitive bindings (automatic thoughts, cognitive distortions) and trains a specific ESA capacity (distinguishing thought from fact). The candidate mapping may be most informative where the primary issue is undetected bindings operating at the cognitive level and where the patient has the participation grade to do the cognitive work. The mapping may be incomplete when the binding is held somatically below cognition, when participation grade is too degraded for the work to integrate, or when the work has produced detection without lawful termination capacity (the patient sees the patterns but cannot stop generating them).

**Dialectical Behavior Therapy** combines ESA training (mindfulness components, distress tolerance) with renegotiation capacity (interpersonal effectiveness, emotion regulation skills). Its particular contribution is training ESA at high emotional activation, which most other modalities approach gradually. The candidate mapping emphasizes presentations involving frequent ESA collapse under emotional intensity. It is structurally addressing all four variables but with particular emphasis on situational awareness during dysregulation.

**Acceptance and Commitment Therapy** operates primarily on Terminability -- its central concept of cognitive defusion is, in architectural terms, helping the patient recognize that they are not their thoughts and that thoughts can be allowed to come and go without being preserved as identification. It also develops ESA (mindfulness components) and APD renegotiation (values clarification as renegotiation of internal commitment structure). One hypothesis to test is whether applications to chronic pain, depression, and anxiety partly involve all three involve threads being held that should be allowed to end.

**Internal Family Systems** addresses APD (parts-held bindings made detectable, refusable, renegotiable through internal dialogue), Terminability (parts that have outlived their protective function are allowed to release their burden), and ACO (Self-energy as an elevated participation grade made accessible through specific practices). One hypothesis to test is whether applications to complex trauma involve complex trauma is structurally a multi-thread terminability and APD problem requiring integration across parts that hold conflicting bindings.

**Psychodynamic Therapy** primarily addresses APD (transference work makes hidden bindings detectable through their reactivation in the therapeutic relationship; insight develops detectability across the binding's full history). Its less commented-on strength is supporting Terminability work over time -- long-term psychodynamic treatment is partly the slow ending of internalized object relations that no longer serve. Its effectiveness depends on the patient having sufficient ESA to use insight rather than only collect it.

**EMDR and Somatic Experiencing** address bindings held below cognitive access (somatic bindings, trauma-installed nervous system patterns) and restore ESA at the level where ordinary cognitive ESA cannot reach. The proposed explanation is that some relevant patterns may not be accessible through a purely cognitive route; that explanation requires external clinical evidence. The APD crosswalk predicts that trauma-related patterns can include somatic constraints that precede explicit cognitive access; this prediction requires clinical validation.

**Mindfulness-Based Interventions** primarily develop ESA (the foundational training is situational-awareness training) and ACO (sustained practice changes baseline participation grade). The crosswalk treats ESA as a potentially foundational variable across presentations -- a patient who develops ESA can use techniques from any modality more effectively, and a patient without ESA tends to use techniques from any modality as new content rather than as transformative practice.

**Motivational Interviewing** addresses APD renegotiation (helping clients articulate, examine, and revise their commitment structures) and Terminability (recognizing which projects, identifications, and patterns are appropriate to release). The candidate map is structurally focused on presentations where the work is recognizing what is ready to end.

**Narrative Therapy** addresses APD (separating the person from problem-saturated narrative makes the narrative detectable as binding rather than as truth) and Terminability (allowing outdated narratives to end, authoring new ones). The proposed explanation is that narrative self-conception can function as a consequential internal binding structure.

These descriptions are partial. Each modality does more than the architectural location captures. The architecture is not a substitute for modality-specific training. What it provides is the answer to the question "what is each modality structurally doing, and what does its placement imply about combination."

A clinician who has the architecture as background can make decisions like the following. A patient presents with chronic anxiety, mild dissociation, history of childhood emotional neglect, and intellectualized self-examination. The architecture suggests: the dissociation indicates ESA fragility under activation, suggesting DBT-style work or somatic intervention as foundational. The childhood neglect suggests bindings installed without detectability, suggesting psychodynamic or IFS work for detectability. The intellectualization suggests that purely cognitive intervention will become its own resistance -- the patient already does cognition; what they need is access routes that cognition cannot dominate. The chronic anxiety suggests that ESA training (mindfulness components) will be needed alongside the binding work, because the binding work will activate the system and ESA capacity will be required to integrate it.

This is not a treatment plan. It is the kind of structural reasoning that lets a clinician see *why* their integration choices make sense, and lets them adjust integration as the patient's needs evolve. A patient at the start of treatment may need foundational ACO work (basic stabilization, sleep, somatic settling) before any of the more sophisticated work can integrate. A patient further along may need explicit terminability work that earlier-stage modalities have not yet addressed. The architecture lets this sequencing be principled rather than improvisational.

The architecture also clarifies what modality-shopping by patients reflects. A patient who has done years of cognitive work and reports feeling stuck has often achieved high detectability without proportional refusal or renegotiation. They need access routes to the bindings that cognition cannot reach. A patient who has done years of meditation and reports lingering relational difficulties has often developed ESA without proportional APD work on their specific bindings. They need work on the content of what they are now able to observe. The architecture lets clinicians and patients see what is missing rather than concluding that everything has been tried.

### 7.1 Realization Funnel for the Framework

The framework becomes safer and more testable when its possible realizations are separated:

- **Stage:** Possibility  
  **Work performed here:** APD, ESA, ACO, and Terminability might form a useful comparison grammar for individual cognition.  
  **What must not be inferred:** Possibility does not establish clinical validity.

- **Stage:** Specification  
  **Work performed here:** Define $L$, $A$, $P$, and $T$ and their non-substitution relations.  
  **What must not be inferred:** A clear definition is not a measurement instrument.

- **Stage:** CM1  
  **Work performed here:** Enumerate admissible mappings, including narrow, broad, contradictory, culturally variant, and potentially harmful interpretations.  
  **What must not be inferred:** Inclusion in CM1 is not endorsement.

- **Stage:** CM2  
  **Work performed here:** Prefer mappings that preserve modality differences, respect safety boundaries, expose uncertainty, and can be empirically tested.  
  **What must not be inferred:** Preference is not evidence of efficacy.

- **Stage:** Instance Configuration  
  **Work performed here:** Select a population, modality definition, outcome, context, assessor, safety protocol, and stopping rule for one study or bounded use.  
  **What must not be inferred:** One configuration cannot stand for every person or modality.

- **Stage:** Implementation Realization  
  **Work performed here:** Conduct the bounded study, training exercise, or decision-support use.  
  **What must not be inferred:** Realization does not validate the architecture by existence alone.

- **Stage:** Evidence  
  **Work performed here:** Record outcomes, adverse events, null results, subgroup differences, and mapping failures.  
  **What must not be inferred:** Evidence is claim- and configuration-bounded.

- **Stage:** Revision  
  **Work performed here:** Revise definitions, mappings, exclusions, and confidence in response to evidence.  
  **What must not be inferred:** Revision must preserve prior lineage rather than overwrite it.

The paper presently reaches Specification and a provisional CM1/CM2 distinction. It does not supply an Instance Configuration, clinical implementation, or validating evidence. That boundary is part of the result.

---

## 8. The Architecture's Commitments and Limits

The architecture commits to specific positions, and being explicit about them is part of what makes the framework defensible.

**On phenomenal experience.** The architecture rests on the polling-primitive reduction articulated in prior work: phenomenal experience consists of the operation of polling system state through time, with higher-order interpretive overlay. Readers who hold that phenomenal experience requires something beyond this reduction will find the foundations unsatisfying. The disagreement is genuine. The clinical applications in this paper work without acceptance of the reduction; clinicians can use APD, ESA, and Terminability as governance machinery without committing to the underlying ontology. The reduction is offered because it provides a unified foundation; it is not required for the clinical applications.

**On clinical scope.** The architecture is not a clinical modality. It does not replace modality-specific training, supervision, or judgment. Clinicians who try to do the work this paper describes without training in the modalities through which the work is performed will produce the kind of harm that comes from architectural sophistication without practical skill. The architecture provides vocabulary against which existing training can be located; it does not provide a substitute for the training itself.

**On the limits of self-application.** Lay readers attempting to apply the architecture to themselves will encounter the limits of self-application. The same hidden bindings that prevent detectability also prevent self-detection of the bindings; the same ESA failures that produce continuation past warrant also produce inability to recognize that warrant has ended. The architecture does not claim that solo application is sufficient where clinical work would be appropriate. What it can do for lay readers is help them recognize when they have reached the limits of self-application and what kind of help they are seeking.

**On the binding problem.** The polling-primitive reduction does not yet specify how simultaneously polled variables are integrated into a unified field rather than remaining as parallel streams. This is acknowledged in prior work and remains the most significant open question in the framework's foundations. It does not undermine clinical application -- graded participation can be assessed and cultivated without complete theory of binding -- but it should be named as a limit.

**On contemplative traditions.** The architecture provides vocabulary that allows clinical and contemplative work to be located alongside each other. It does not subordinate contemplative tradition to clinical framework, claim to teach what contemplative traditions teach, or presume to evaluate practices developed over centuries within their own frames of understanding. The architecture's relationship to contemplative traditions is one of vocabulary, not of authority.

**On policy.** The architecture provides framework, not prescription. It does not specify which modality should be used for which presentation, what training requirements clinicians should meet, what self-direction is safe for which lay readers, or what clinical research should prioritize. These are downstream questions requiring clinical judgment, professional standards, and empirical work the architecture does not perform.

**On the person.** The architecture treats internal threads as the unit of analysis for terminability and as the locus of bindings for APD. It is not a theory of personhood. The person who hosts these threads, makes meaning across them, suffers and grows through their dynamics, is more than the architecture describes. The framework's value comes partly from being clear about what it does not address.

### 8.1 Evidence and Falsification Boundary

The framework would gain support if independent raters could use the four-coordinate vocabulary reliably; if coordinate-specific measures showed discriminant validity rather than collapsing into one general factor; if changes predicted by a mapped practice appeared on the specified coordinate without being assumed on the others; and if the map improved explanation or study design beyond existing modality-native constructs.

It would be weakened if raters could not distinguish the coordinates, if every modality mapped equally to every coordinate, if the vocabulary merely renamed established constructs without adding testable relations, if the mappings systematically distorted modality-native accounts, or if use of the framework encouraged unsafe overconfidence. Null results, adverse cases, and culturally or clinically bounded failures are revision inputs, not exceptions to hide.

This draft has not completed the external clinical literature review required to evaluate its claims about named modalities. Until that review is performed, the modality mappings remain corpus-integrated hypotheses. The published Ableman references below establish the internal architecture being projected; they do not validate the clinical projection.

---

## Translational Comparison Grammar and Jurisdictional Firewall

The completed P1 corpus strengthens the paper by narrowing its role. The Well-Governed Mind is a **translational comparison grammar and research agenda**, not a clinical framework, treatment protocol, diagnostic system, or direct proof that computational governance structures map onto human cognition.

- **Source construct:** APD  
  **Corpus role:** Inspectability and renegotiability of binding constraints.  
  **Permitted use here:** Ask whether a represented internal commitment can be noticed, questioned, and revised.  
  **Transfer limit:** Does not imply that every mental process is voluntary, explicit, or software-like.

- **Source construct:** ESA  
  **Corpus role:** Self-location, uncertainty, capability, and continuation awareness.  
  **Permitted use here:** Describe whether a person can locate a current cognitive operation and its limits.  
  **Transfer limit:** Introspection is not complete observation of cognition and may be impaired or misleading.

- **Source construct:** ACO and consciousness work  
  **Corpus role:** Graded meaning-binding and participation vocabulary.  
  **Permitted use here:** Generate questions about participation and integration without diagnosing consciousness.  
  **Transfer limit:** No ontological, moral-status, or clinical conclusion follows from a corpus mapping.

- **Source construct:** Terminability  
  **Corpus role:** Lawful stopping, refusal, completion, and release of continuation pressure.  
  **Permitted use here:** Compare how practices end or disengage internal threads.  
  **Transfer limit:** Must not become advice to stop treatment, suppress symptoms, or manage crisis without qualified care.

- **Source construct:** Context and memory architecture  
  **Corpus role:** Provenance, selection, omission, uncertainty, and revision of operative context.  
  **Permitted use here:** Clarify which narratives or evidence are active in a self-model.  
  **Transfer limit:** Human memory is not an artifact store, and reconstruction is not exact replay.

Every cross-domain mapping should use a transfer envelope:

$$
\begin{aligned}
T= (&source\ construct, target\ construct, shared\ structure, \\
&disanalogies, evidence\ required, prohibited\ inference)
\end{aligned}.
$$

Without this envelope, structural resemblance can become authority laundering: a precisely defined machine-governance term is treated as if it validates a psychological or therapeutic claim. The paper should preserve modality-specific mechanisms, histories, ethics, contraindications, cultural settings, and evidence standards rather than translating them into one constitutional vocabulary.

The jurisdictional firewall is explicit. A reader-facing pedagogical model may support reflection, vocabulary, and questions for discussion. It may not recommend treatment, determine diagnosis, replace professional assessment, adjudicate crisis risk, or claim efficacy. Any future clinical projection requires authorized external research, domain-expert review, safety analysis, and appropriately governed empirical work.

The universal GSM can type `PROPOSED_ANALOGY_TO`, `SHARES_STRUCTURE_WITH`, `DIFFERS_FROM`,  
`REQUIRES_EXTERNAL_EVIDENCE`, `PROHIBITS_INFERENCE`,  
and `CONTESTED_BY`. GMB can retain competing mappings and counterevidence; inclusion does not validate a modality map.

This integration establishes four editorial commitments: adopt translational comparison grammar and research agenda as the official corpus role; adopt the transfer envelope; add the jurisdictional firewall to the reader-facing introduction and conclusion; and decide whether publication should wait for qualified clinical and contemplative-domain review rather than presenting the internal-corpus synthesis alone.

## Binding Evidence, Research Challenge, Anti-Mechanization, and Access Conditions

The fixed-seed comparison with The Locus of Meaning, adversarial alternation, model-first legacy migration, and constitutionally governed infrastructure sharpens the paper's cross-domain firewall:

$$
\begin{aligned}
T^*= (&source\_construct, target\_construct, shared\_structure, \\
&disanalogies, evidence\_required, domain\_review, \\
&access\_conditions, prohibited\_inference, revision)
\end{aligned}.
$$

The Locus of Meaning can supply a relational vocabulary for represented commitments, context, uptake, consequence, and revision. It does not prove that a psychological construct has the same mechanism or semantic threshold. Role-separated reviewers may adversarially challenge mappings, measures, exclusions, and overclaims, but software-style alternation does not create clinical competence or participant safety.

Model-first legacy migration is an explicit negative analogy: a person is not a legacy program to be reverse-engineered, normatively cleaned, and replaced. Its useful remainder is only the separation of observation, descriptive model, normative judgment, intervention, evidence, and uncertainty. Human accounts remain participant-indexed, revisable, culturally situated, and subject to consent and professional boundaries.

Constitutionally governed infrastructure suggests that appointment systems, interfaces, cost, language access, scheduling, disclosure rules, and institutional routing can shape practical access before a clinical decision. That is a research question requiring external evidence and affected-party analysis, not proof that every access barrier is delegated authority or that this paper supplies institutional policy.

The universal GSM can type   
`PROJECTS_BINDING_VOCABULARY_WITH_LIMITS`,  
`CHALLENGES_MAPPING_UNDER_DOMAIN_REVIEW`, `PROHIBITS_PERSON_AS_LEGACY_SYSTEM`,  
`SEPARATES_DESCRIPTION_FROM_INTERVENTION`, `STUDIES_PRACTICAL_ACCESS_CONDITION`,  
`REQUIRES_CLINICAL_EVIDENCE`, and   
`REVISES_AFTER_PARTICIPANT_CORRECTION`.

This randomized review establishes four editorial commitments: extend the transfer envelope with domain review and access conditions; permit adversarial challenge only under a clinical jurisdictional firewall; state the anti-mechanization boundary against legacy-system analogy; and treat institutional access as an evidence-requiring research dimension rather than a conclusion.

## A Research Translation Grammar Behind a Clinical Firewall

Ten retained downstream uses place The Well-Governed Mind beside consciousness hypotheses, adversarial review, collective cognition, infrastructure access, the Cognitive Kernel, meta-binding, legacy-migration nonanalogy, recursive orientation, the Locus of Meaning, and shared-experience work. They confirm a translational comparison grammar and research agenda, not a treatment protocol, diagnostic system, clinical modality, crisis tool, or proof that computational governance maps onto human cognition.

$$
\begin{aligned}
T^*= (&source\_construct, target\_construct, shared\_structure, \\
&disanalogies, mechanism\_difference, evidence\_required, \\
&domain\_review, participant\_perspective, consent, \\
&access\_conditions, risks, prohibited\_inference, \\
&stopping, recovery, revision)
\end{aligned}.
$$

APD, ESA, ACO, Terminability, binding, custody, migration, and constitutional language may organize questions only through this transfer envelope. A person is not a legacy program, a cognitive state is not a file, introspection is not complete observability, and refusal or termination vocabulary is not advice to stop treatment, suppress symptoms, or manage crisis without qualified care.

Future human research requires qualified clinical and contemplative-domain review, current external evidence, consent, privacy, cultural and subgroup analysis, adverse-event handling, stopping, recovery, and participant correction. Structural elegance, internal corpus coherence, software review, or AI synthesis cannot supply competence. Until those gates are met, outputs are pedagogical hypotheses and study-design candidates only.

The universal GSM can type   
`PROPOSES_CROSS_DOMAIN_MAPPING`,  
`SHARES_STRUCTURE_WITH_LIMITS`, `PRESERVES_MECHANISM_DIFFERENCE`, `REQUIRES_DOMAIN_REVIEW`,  
`REQUIRES_PARTICIPANT_CONSENT`, `STUDIES_ACCESS_CONDITION`, `PROHIBITS_CLINICAL_INFERENCE`,  
`STOPS_HIGH_RISK_USE`, and   
`REVISES_AFTER_PARTICIPANT_CORRECTION`.

This review establishes four editorial commitments: retain research-translation-grammar standing; adopt the expanded transfer envelope; strengthen the clinical, contemplative, anti-mechanization, and crisis firewalls; and place publication claims and all human implementation behind authorized external research, qualified review, consent, safety, stopping, and recovery gates.

## Research Grammar, Not Clinical Machinery

### Public orientation

This paper asks whether concepts developed for governed systems can help describe attention, participation, internal conflict, and termination without reducing a person to software. The result is a research and explanatory grammar. It is not a diagnostic model, treatment protocol, crisis tool, competence test, criterion of personhood, or authorization for intervention.

### Adversarial tests

1. **Metaphor-reification attack.** A computational analogy is mistaken for a shared mechanism. Every transfer must state similarities, disanalogies, and what would falsify the comparison.
2. **Person-as-program attack.** A reader infers that internal processes may be debugged, deleted, or subordinated like code. The framework expressly refuses that inference.
3. **Self-report sufficiency attack.** Introspection is treated as complete evidence. Participant report is indispensable but partial; it may be constrained by memory, language, distress, power, or access.
4. **Coercive-governance attack.** Constitutional vocabulary is used to legitimize control by clinicians, institutions, employers, family, or automated systems. No external actor receives authority from this paper.
5. **Cultural-universality attack.** One model of agency, integration, plurality, or wellness is presented as universal. Cultural, disability, neurodiversity, and affected-party review are required.
6. **Crisis-misuse attack.** The framework is applied where delay or experimentation could increase harm. Clinical and emergency contexts remain outside scope absent qualified protocols and current evidence.
7. **Privacy attack.** Semantic records of internal experience become surveillance artifacts. Consent, purpose limitation, revocation, access, retention, and deletion are mandatory research questions.

### Evidence and citation gate

Internal Ableman papers can establish the origin and consistency of the proposed vocabulary. They cannot validate psychological mechanisms, clinical efficacy, safety, cultural generality, or ethical acceptability. A public version making claims in those domains requires current external scholarship, qualified domain review, affected-participant review, and explicit adverse-event, stopping, recovery, and referral protocols.

No external research was performed in this pass. Accordingly, the internally integrated candidate may proceed through textual review, but evidence readiness for clinical, therapeutic, or empirical framing remains **held**. A non-clinical conceptual essay remains possible if its claims and title make the boundary unmistakable.

### Formalization decision

A compact comparison record may improve discipline, but additional equations would suggest a degree of measurement and mechanism not established here. The publication-ready form should prefer a typed transfer table over decorative mathematics.

## 9. Implications

For clinical training, the architecture suggests benefit from explicit instruction in the four variables and their interactions, alongside modality-specific training. A clinician who has architectural fluency in addition to modality competence can locate their work within a larger structure, integrate modalities with awareness of what they are integrating, and recognize the limits of any single approach without having to derive that recognition from clinical errors. This is not a curriculum proposal; it is an observation about what the architecture would offer if incorporated into existing training structures.

For clinical research, the architecture suggests that outcome measures organized around variable improvement -- detectability of specific bindings, ESA capacity at relevant hinge points, ACO grade across clinically relevant states, terminability work completed -- might better capture what therapy does than measures organized only around diagnostic-category symptom reduction. This is a long-term direction, not a near-term protocol. Existing research apparatus is well-suited to symptom-focused outcomes; reorienting toward variable-focused outcomes would require methodological development the architecture itself does not provide.

For lay self-direction, the architecture provides a model that lets people locate their own work. Someone who recognizes that they are highly intellectualized but emotionally reactive can see that they have ESA capacity but limited access to the bindings that intellectualization cannot reach. Someone who has done extensive contemplative practice but struggles with specific relational patterns can see that they have ACO development without proportional APD work on those patterns. Someone who has done years of therapy and feels stuck can see what variable might be underaddressed. The architecture does not replace clinical work where indicated; it helps lay readers know when clinical work is indicated and what they are seeking.

For the integration of contemplative and clinical work, the architecture provides vocabulary that allows traditions to operate alongside each other without being reduced to each other. A clinician working with a patient in contemplative practice can recognize what the practice is structurally doing -- ESA cultivation, perhaps ACO development, perhaps specific binding work -- and complement rather than compete with it. A contemplative teacher working with a student in clinical distress can recognize when traditional practice is appropriate and when the student needs clinical support that practice is not designed to provide. Neither tradition needs to claim the other; both can be located.

The vocabulary is available now for conceptual analysis and research design. Clinical use beyond reflective comparison requires the evidence review, measurement work, professional judgment, and safety boundaries specified above. Lay self-application should remain interpretive and should not displace appropriate clinical support.

---

## 10. Conclusion

The fragmentation of individual mind-governance modalities has obscured a unified architecture that lets them be located, compared, and integrated. The architecture exists once the bundled concerns of cognitive self-management are decoupled. Its components -- APD, ESA, ACO, Terminability -- are orthogonal in concern, complementary in function, and applicable to individual cognition without modification. Each governs a distinct variable that the others cannot reach. Together they describe what well-governed cognition requires.

The framework does not replace any modality. It provides vocabulary in which modalities can be seen for what they structurally are. It does not eliminate clinical judgment. It supports it. It does not subordinate contemplative traditions to clinical ones or vice versa. It allows them to operate in articulated relationship rather than in unspoken tension. It does not claim to exhaust what is true about minds, persons, suffering, or growth. It claims only to make visible what is structurally happening across the work that has always been happening in this domain.

What the architecture provides for clinicians is integrative vocabulary across modalities they already use. What it provides for lay readers is a usable model of their own minds, with explicit recognition of where self-application reaches its limits. What it provides for both is jurisdiction: the capacity to know what kind of cognitive act is occurring, what authority it would create, what moral weight attaches to it, and when stopping is the most disciplined move available.

Operating one's own mind well is not, finally, the right thoughts. It is the right to think them, with vocabulary clean enough to know what thinking is.

---

## Realization Scope and Evidence Boundary

This successor makes the paper's stage boundary explicit. It narrows claims rather than manufacturing missing evidence: a stage named as context is not thereby claimed as implemented, validated, or complete.

- **Cm2.** Existing source passages use this stage only as bounded context or an obligation. The paper does not claim an independently validated contribution at this stage.

## Corpus-Wide Reference Positioning

This paper argues that contemporary therapeutic, contemplative, and cognitive practices use partially overlapping vocabularies for internal constraint, awareness, participation, and change. Its nearest external comparison fields are consciousness, provenance, semantic. The sources in [E1], [E2], [E3], [E4], [E5], [E6], [E7] are cited as predecessor literature, adjacent standards, or counterpressure - not as evidence that they caused the Ableman framework or that they validate its novel claims. The comparison isolates where established work already supplies provenance, formal assurance, institutional constraint, empirical method, or engineering practice, and where this paper adds a distinct claim about admissibility, authority, semantic custody, or governed realization.

Within the Ableman corpus, the highest-priority current cross-links are [A1], [A2], [A3], [A4], [A5], [A6], [A7]. These are links among separately custodied works, not silent identity mergers. Their role is to expose mutual dependencies, terminology collisions, and places where a reader should traverse the corpus before treating this paper as self-sufficient.

### Reference-pass counterevidence and limit search

The pass applied the following pressure tests: Structural and computational correspondences remain insufficient as phenomenal evidence unless linked to discriminating empirical predictions against competing theories. A complete provenance graph can faithfully record a false or unauthorized process; provenance is evidence about lineage, not automatic truth or legitimacy. Formal vocabularies and graph links make commitments explicit but cannot by themselves establish correct identity, shared interpretation, or lossless translation between contexts. These limits are not generic disclaimers: they identify the assumptions that a later empirical, formal, or implementation review must try to break.

### Reference-pass influence and novelty boundary

No newly added external source is asserted to be a documented authorial influence unless the predecessor source already said so. `Predecessor` means earlier relevant work;

`adjacent` means a useful comparison; `standard` means an interoperability or assurance baseline; and `counterevidence` marks work that narrows or pressures a claim. Novelty therefore remains a reviewable, claim-level question rather than an inference from a low similarity score or an absent citation.

## References

### External scholarship, standards, and prior art

**[E1]** David J. Chalmers. "Facing Up to the Problem of Consciousness." *Journal of Consciousness Studies* 2(3), 1995, pp. 200-219. https://consc.net/papers/facing.html **Relationship:** Foundational framing of the explanatory gap; cited to bound, not resolve, phenomenal claims.

**[E2]** Larissa Albantakis et al. "Integrated Information Theory (IIT) 4.0: Formulating the Properties of Phenomenal Existence in Physical Terms." *PLOS Computational Biology* 19(10), 2023, e1011465. DOI: 10.1371/journal.pcbi.1011465. https://doi.org/10.1371/journal.pcbi.1011465 **Relationship:** Competing formal theory of consciousness included for explicit contrast and counterevidence obligations.

**[E3]** Stanislas Dehaene and Jean-Pierre Changeux. "Experimental and Theoretical Approaches to Conscious Processing." *Neuron* 70(2), 2011, pp. 200-227. DOI: 10.1016/j.neuron.2011.03.018. https://doi.org/10.1016/j.neuron.2011.03.018 **Relationship:** Competing global-workspace account included to prevent a corpus-native ontology from substituting for empirical neuroscience.

**[E4]** Nikolaus Kriegeskorte, Marieke Mur, and Peter A. Bandettini. "Representational Similarity Analysis - Connecting the Branches of Systems Neuroscience." *Frontiers in Systems Neuroscience* 2, 2008, 4. DOI: 10.3389/neuro.06.004.2008. https://doi.org/10.3389/neuro.06.004.2008 **Relationship:** Predecessor empirical method for comparing representational geometries.

**[E5]** Francesco Locatello et al. "Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations." *PMLR* 97, 2019, pp. 4114-4124. https://proceedings.mlr.press/v97/locatello19a.html **Relationship:** Counterevidence showing that desired latent factorization is not identifiable from unsupervised data without inductive biases.

**[E6]** W3C. *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-o/ **Relationship:** Adjacent provenance standard; it models entities, activities, and agents, but does not by itself establish the paper's stronger authority or standing claims.

**[E7]** Santiago Torres-Arias et al. "in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes." *28th USENIX Security Symposium*, 2019, pp. 1393-1410. [usenix.org source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) **Relationship:** Predecessor supply-chain lineage system used for comparison; no influence claim is made unless the source head already documents one.

### Ableman corpus

**[A1]** Adam Ableman. *Ableman Consciousness Ontology (ACO)*. Ableman Corpus current edition; work identity `PAPER.PUB.18203749`;  
source SHA-256  
`ACD97032780DA7B3A36750702BE1F47BCB2E6361EF6E74ECA8B441D7C6A25DDE`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A2]** Adam Ableman. *The Locus of Qualia*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-AF27E66B81811DB1`;  
source SHA-256  
`7B83EBD0FFDCFEBFA522A715AE0E4D1049FCA0B4CE0618C2017F8BB9206E5424`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A3]** Adam Ableman. *The Phenomenal Aperture*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-4B275CBB7EFF1A4F`;  
source SHA-256  
`B6AE95D72B89DAF47778BED3982843A1ECE350CA363750108AA60D5A4C63D763`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A4]** Adam Ableman. *Possible Minds: Against the Provincialization of Consciousness*. Ableman Corpus current edition; work identity `PAPER.PUB.20681869`;  
source SHA-256  
`77F381A29E2EF801085938DB369F3F432321CCEB8B9DD3969330337C24BA4998`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A5]** Adam Ableman. *Admissibility Theory of Consciousness*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-8FDC994841DA6CF3`;  
source SHA-256  
`F409652555CEC4898DBEC1E8BBB179CEE020E7FF35F4C8F307CDA82253D6F49F`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A6]** Adam Ableman. *Reasoning by Way of Receipts*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-04E427F6F4D94454`;  
source SHA-256  
`AF86A66CCD6A103DD75208500AE99148911A6453B6DFDF36A954279F21AB8489`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

**[A7]** Adam Ableman. *The Epistemic Lineage Engine*. Ableman Corpus current edition; work identity   
  `AMCS-LOCAL-WORK-E0EC3DC7EABF5060`;  
source SHA-256  
`CDD74D9AFAB6532645E68F7F6C9F0F7A9E472D9B8E717290522566FF8DC01F11`. **Corpus relationship:** priority cross-link selected by corpus profile and similarity review; no identity merger or publication effect.

### Editorial source notes retained from predecessor

Adam Ableman. *Constitutional Epistemics: A Meta-Governance Substrate for Lawful and Auditable Machine Reasoning Systems*. Zenodo, 2025. https://doi.org/10.5281/zenodo.18114714.

Adam Ableman. *Epistemic Situational Awareness (ESA): A Phenomenological Control Property of Governed Reasoning Systems*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18121270.

Adam Ableman. *Epistemic Situational Awareness (ESA): Continuation Governance for Frontier AI Systems*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18123102.

Adam Ableman. *Ableman Consciousness Ontology (ACO): Consciousness as a Manifold of Meaning-Binding, Situational Awareness, and Epistemic Self-Authorship*. Zenodo, 2026. https://doi.org/10.5281/zenodo.18203749.

Adam Ableman. *Constitutional Computation*. Zenodo, 2026. https://doi.org/10.5281/zenodo.20624488.

Adam Ableman. *Terminability*. Ableman Corpus edition in the current corpus; publication identity and standing not granted.

The external references required for claims about CBT, DBT, ACT, IFS, psychodynamic therapy, EMDR, Somatic Experiencing, mindfulness-based interventions, motivational interviewing, narrative therapy, suicidality, depression, mania, dissociation, and clinical outcomes remain a publication blocker. They are deliberately not fabricated or inferred from the internal corpus.

The entries below are corpus-internal comparison and dependency sources. Their inclusion does not establish external validation of this paper's empirical, safety, novelty, or performance claims.

Adam Ableman *Ableman Consciousness Ontology (ACO): Consciousness as a Manifold of Meaning-Binding, Situational Awareness, and Epistemic Self-Authorship.* Zenodo, 2026. doi:10.5281/zenodo.18203749

Adam Ableman *Constitutional Computation.* Zenodo, 2026. doi:10.5281/zenodo.20624488

Adam Ableman *Constitutional Epistemics: A Meta-Governance Substrate for Lawful and Auditable Machine Reasoning Systems.* Zenodo, 2026. doi:10.5281/zenodo.18114714

Adam Ableman *Epistemic Situational Awareness (ESA): A Phenomenological Control Property of Governed Reasoning Systems.* Zenodo, 2026. doi:10.5281/zenodo.18121270

Adam Ableman *Epistemic Situational Awareness (ESA): Continuation Governance for Frontier AI Systems.* Zenodo, 2026. doi:10.5281/zenodo.18123102

Adam Ableman *CARA: Constrained Artificial Reasoning Architecture.* Zenodo, 2025. doi:10.5281/zenodo.18099715

Adam Ableman *A Theory of Agentic Observation.* Zenodo, 2026. doi:10.5281/zenodo.20437813

Adam Ableman *Constraint-Bearing Composability.* Zenodo, 2026. doi:10.5281/zenodo.21632061

---

Corpus source and companion formats: [https://github.com/AblemanMosaic/ableman-corpus](https://github.com/AblemanMosaic/ableman-corpus)  
License: [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)

---

DOI: [10.5281/zenodo.23848470](https://doi.org/10.5281/zenodo.23848470)
