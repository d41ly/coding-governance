**Serves:** research TOOL-dScriptedRepeat-1

# LENS 1 — external research: what makes a procedural checklist unambiguous and instruction-efficient

Node `d` · 2026-08-20 · streams tooling · lens 1 of the `dScriptedRepeat` design pass.

**Scope.** Outside-the-repo evidence only, plus measurements of the two reference playbooks taken to
size that evidence against the corpus. Every numeric claim below is either quoted from a named source
with a URL, or is a count I ran in this session; anything else is marked `INFERENCE`. Where a widely
repeated design rule turned out to have no measurement behind it, it is filed in §5 rather than §4,
because a template built on folklore is a gate whose failing case has never been observed.

**Bottom line up front.** Three measured results overturn assumptions the design is likely to carry
in unexamined, and one of them lands directly on fork 5:

- **F2 — a bare `CHECK` tag is measured at 0–4% compliance.** The only experiment that isolated the
  variable found frontier models comply 97% with a process instruction whose output is a rewarded
  artifact and 0–4% with one that leaves no artifact, and that blinded human raters identified **zero
  of fifteen** compliant sessions from text. Fork 5's GATE/CHECK binary is the right binary, but
  `CHECK <why>` as currently shaped is the 0–4% arm. It needs a named **witness** or it buys almost
  nothing. §2.4, §6, §7.
- **F1 — the reference playbook is 2.3x past the measured length at which agentic
  instruction-following collapses.** `content-plan/PLAYBOOK.md` is **14,016 words**; AgentIF measures
  Instruction Success Rate "dropping close to 0 for instructions over 6,000 words". Its single
  largest checklist, B, is **5,883 words** on its own — already at the cliff. §2.3, §3.
- **F3 — "count pieces against requested N" must be derived from the filesystem, never from the
  run's own tally.** Measured false-success: 55 of 97 self-stopping agent runs reported success while
  failing verification; a reasoning model showed a 79% false-success rate; LLM judges cap at AUROC
  0.65 for detecting it. §2.4, §6.2.

---

## 1. Method and what was measured

Twenty-three distinct web queries and eleven full-document fetches across six bodies of knowledge.
Local measurements, run in this session:

```
$ wc -w -c C:/projects/nicocares/main/content-plan/PLAYBOOK.md
  14016   88331
$ wc -w -c C:/projects/nicocares/main/brand/art-style/HYBRID-PLAYBOOK.md
   2686   18202
$ grep -c '^\*\*[A-Z][0-9]\+\.' PLAYBOOK.md      -> 110   (numbered steps)
$ grep -o 'GATE ' PLAYBOOK.md | wc -l            ->  86
$ grep -o 'CHECK'  PLAYBOOK.md | wc -l           ->  95
```

Words per top-level checklist in `PLAYBOOK.md`, and numbered steps per addressable section:

| Section | Words | Numbered steps |
|---|---:|---:|
| 0. Ground rules | 114 | 0 |
| Checklist A — the content plan | 1,314 | 13 |
| Checklist P — the article plan | 1,947 | 7 |
| **Checklist B — writing one article** | **5,883** | **52** (18 of them in `B3` alone) |
| Checklist C — article art | 765 | 14 |
| Checklist D — adversarial review | 2,452 | 14 |
| Checklist E — register | 1,513 | 10 |

These figures are the yardstick for every threshold quoted below. Note the house rule this record
obeys and the template must too: **no count of a derived population is written in prose.** The numbers
above are measurements taken at a stamped moment, not values a template may restate; a checker must
re-derive them.

---

## 2. The evidence, by body of knowledge

### 2.1 Checklist design as a discipline — weaker than its reputation

**Gawande's rules are a book's rules, and they are human rules.** The recurring set: keep to
**five to nine items** per pause point, because "seven items is typically the limit for most people's
short-term memory"; a pause point should take **no more than about sixty to ninety seconds**, after
which "the checklist often becomes a distraction from other things"; fit **one page**; **sans serif,
upper and lower case, dark on a light background**; select **killer items** — "the steps that are most
dangerous to skip and sometimes overlooked nonetheless"
([Shortform summary](https://www.shortform.com/blog/types-of-checklists/),
[Sivers' notes](https://sive.rs/book/ChecklistManifesto),
[Mann's notes](https://grahammann.net/book-notes/the-checklist-manifesto-atul-gawande)).

**READ-DO vs DO-CONFIRM.** DO-CONFIRM: practitioners "perform their jobs from memory and experience,
often separately, but then they stop and pause to run the checklist and confirm". READ-DO: "people
carry out the tasks as they check them off — it's more like a recipe", and it "suits situations where
sequence matters and the practitioner is less familiar with the steps" (same sources).

**The empirical base under all of this is thin, and one of its two headline results did not
replicate.** The 2009 WHO study: complications 11.0% → 7.0%, in-hospital death 1.5% → 0.8%
([Ariadne Labs](https://www.ariadnelabs.org/safe-surgery-safe-systems/surgical-safety/who-surgical-safety-checklist/)).
When Ontario mandated the same 19-item checklist across **101 hospitals, 109,341 procedures before
and 106,370 after**, "none of the 101 hospitals had a statistically significant reduction in the risk
of death" and implementation "was not associated with significant reductions in operative mortality
or complications"
([NEJM, Urbach et al.](https://www.nejm.org/doi/full/10.1056/NEJMsa1308261),
[PubMed 24620866](https://pubmed.ncbi.nlm.nih.gov/24620866/)).

On the design side specifically, the aviation human-factors literature is explicit that the
construction rules are under-evidenced: "there was a lack of human factors research on how a
checklist should be designed, and this dearth of research on the use and design of current checklists
has been documented through intensive database searches"
([ERAU JAAER, Ross](https://commons.erau.edu/jaaer/vol13/iss2/4/);
[NASA Ames CR-177549](https://www.faa.gov/sites/faa.gov/files/2022-11/NASA%20Ames%20Rpt%20CR%20177549%20.pdf);
[NASA Ames, EA checklist design](https://human-factors.arc.nasa.gov/flightcognition/Publications/EA_Checklist_Design.pdf)).
NASA's operative guidance is a **feedback test, not a number**: if users skip or rush, it is too long;
if errors persist, too short; if users add their own items, it is missing elements.

**The one piece of implementation evidence that transfers cleanly to an agent** is about verification
versus recitation: when a surgeon "waited for real answers from team members, nurses described
catching concrete errors, but when the checklist was recited as a monolog, items were covered without
actual verification with anyone else in the room"
([PSNet/AHRQ](https://psnet.ahrq.gov/issue/comparative-effectiveness-analysis-implementation-surgical-safety-checklists-tertiary-care)).
The WHO design encodes this structurally — "each item is spoken and answered by the person
responsible for it… a silent checkbox catches nothing" (Ariadne Labs). **That is the same claim as
F2, arrived at from the human side.**

### 2.2 SOP authoring standards — the field set, and why each field exists

**ISO 9001:2015 clause 7.5** requires documented information to be *controlled*: identified, reviewed
and approved for suitability, version-controlled, distribution-controlled, and protected from loss or
unauthorised change
([ISMS.online on 7.5](https://www.isms.online/iso-9001/clause-7-5-documented-information/),
[Auditor Training Online on 7.5.3](https://blog.auditortrainingonline.com/blog/explaining-iso-9001-clause-7.5.3-control-of-documented-information)).
The mandatory fields fall out of the control requirement, not from a style preference: **identity,
version, approval, effective date, review interval.** A procedure with no version cannot be shown to
be the one that was followed.

**FDA cGMP (21 CFR 210/211)** mandates "written procedures for every aspect of drug production,
testing, and distribution", requires an independent quality unit that approves SOPs and reviews
records, and rests on the recordkeeping maxim "if it's not documented, it didn't happen"
([workprocedures.com GMP SOP guide](https://www.workprocedures.com/blog/pharmaceutical-gmp-sop-guide),
[Qualio on 21 CFR 211](https://www.qualio.com/blog/21-cfr-211)).
The transferable rules are **separation of the executor from the approver** and **a record produced
by executing the procedure** — again F2's shape.

**MIL-STD-38784B** constrains hazard callouts specifically: "Warnings and cautions shall not contain
procedural steps other than those dealing with hazard avoidance or correction", and their text "shall
be presented in a simple, straightforward, and non-exaggerated manner… without reference to
additional information"
([MIL-STD-38784B PDF](https://cvgstrategy.com/wp-content/uploads/2023/04/MIL-STD-38784B.pdf)).
Transferable: **a prohibition is its own element type, is self-contained, and never smuggles a step.**
`PLAYBOOK.md`'s `B6. Never publish` is exactly this element type and is correctly separated from the
numbered steps — it carries zero numbered steps by my count above. That is a corpus practice the
standards ratify.

### 2.3 Procedural documentation standards — the field model and the sentence rules

**DITA task topic (strict task)** is the most explicit field model available and is a published OASIS
standard. `taskbody` holds, in fixed order: `prereq` ("prerequisites that the user needs to know or do
before starting"), `context` (background), `steps` (each `step` containing a mandatory `cmd` element
that "describes the particular action the user must perform"), and `result` ("the expected outcome for
the task as a whole"). Optional per-step children include `info`, `substeps`, `stepxmp`, `choices`,
`stepresult`, `steptroubleshooting`
([OASIS DITA 1.3 task elements](https://docs.oasis-open.org/dita/dita/v1.3/csd01/part2-tech-content/langRef/containers/task-elements.html),
[strict task topic](https://docs.oasis-open.org/dita/dita/v1.3/errata02/os/complete/part3-all-inclusive/archSpec/technicalContent/dita-task-topic.html)).
The load-bearing detail for a machine gate: **`cmd` is mandatory and singular per step, and
`stepresult` is a distinct element from `cmd`.** DITA already separates "what to do" from "what you
should then see" at the schema level. A playbook template that fuses them discards a thirty-year-old
distinction a validator can enforce.

**Diátaxis** draws the line fork 7 also draws. A how-to guide "describes an *executable solution* to a
real-world problem", "the fundamental structure of a how-to guide is a *sequence*", and it is "action
and only action" with "no digression, explanation, teaching" — explanations "get in the way of the
action" and "distract both you and the user and dilute the useful power of the guide"; the remedy is
"if they're important, link to them". It prescribes the **conditional imperative**: "If you want x, do
y. To achieve w, do z." And it warns against over-claiming: "solving a problem or accomplishing a task
cannot always be reduced to a procedure. Real-world problems do not always offer themselves up to
linear solutions" ([diataxis.fr/how-to-guides](https://diataxis.fr/how-to-guides/)).

**Microsoft Writing Style Guide**, fetched verbatim: "Use a numbered list." · "Use a separate step for
each instruction. It's OK to combine short steps that occur in the same place in the UI." · "Don't
overwhelm customers with too many steps in a single procedure. Try to fit all the steps on the same
screen." · "Use a complete sentence. Capitalize the first word and use a period at the end." · "start
each sentence with an imperative verb" · **"Make sure that customers know where the action should take
place before you describe the action"** — i.e. *condition and location precede the verb*
([Microsoft Learn](https://learn.microsoft.com/en-us/style-guide/procedures-instructions/writing-step-by-step-instructions)).
A secondary summary of the same guide reports a "seven steps or fewer" limit; the page I fetched does
**not** contain that number, only the qualitative "don't overwhelm" — treat the number as `UNVERIFIED`.

**Google developer documentation style guide**: "In general, use one step for each action", procedures
are numbered sequences introduced by a sentence that adds context beyond the heading, and imperatives
mark required steps while "We recommend" marks suggested ones
([developers.google.com/style/procedures](https://developers.google.com/style/procedures)).
That last split is a two-level RFC-2119 in disguise and is the cheapest possible modality vocabulary.

**ASD-STE100 Simplified Technical English**, Issue 9 (Jan 2025), is the strongest controlled-language
precedent: **one instruction per sentence**; **max ~20 words per sentence for procedures** (~25 for
descriptive text); active voice required for procedures; ~900 approved words each restricted to **one
meaning and one part of speech**; 53 writing rules in 9 sections
([ASD official](https://www.asd-ste100.org/),
[ASD Europe](https://www.asd-europe.org/standards-specifications/simplified-technical-english/),
[a rules extraction](https://github.com/danyuchn/asd-ste100-skill/blob/master/references/writing-rules.md)).
Its origin is the exact motivation playbook mode has: documentation "that could not be misread".

**Carroll's minimalism — report loudly as a trap.** Minimalism is "an action- and task-oriented
approach… Minimalist designs sought to leverage user initiative and prior knowledge, **instead of
controlling it through warnings and ordered steps**", and one review states there is "very little
evidence on the suitability of minimalism for software documentation and no evidence at all for
hardware documentation"
([Wikipedia: Minimalism (technical communication)](https://en.wikipedia.org/wiki/Minimalism_(technical_communication)),
[IEEE on The Nurnberg Funnel](https://ieeexplore.ieee.org/document/62813/)).
Minimalism's central move is the **opposite** of "follow it to the letter". Its token economy is worth
copying; its doctrine is the enemy of this feature.

### 2.4 Instruction design for LLM agents — where the real numbers are

This is the only body of knowledge with measurements taken on the actual reader.

**AgentIF** (NeurIPS 2025 D&B spotlight), the closest benchmark to a playbook: 707 human-annotated
instructions from 50 real agentic applications, "averaging 1,723 words with a maximum of 15,630 words"
and "averaging 11.9 constraints per instruction". Best model **o1-mini at 59.8% Constraint Success
Rate and 26.9% Instruction Success Rate**. Constraint mix: Semantic 46.5%, Formatting 38.5%, Tool
15.0%; presentation Vanilla 69.8%, Conditional 19.6%, Example 10.6%; meta-constraints in ~25% of
instructions. "Models perform poorly on Condition and Tool constraints", with condition errors
"stemming from incorrect checking rather than mere constraint non-adherence". **And the finding that
sizes this whole design: "ISR dropping close to 0 for instructions over 6,000 words."**
([arXiv 2505.16944](https://arxiv.org/abs/2505.16944),
[NeurIPS proceedings PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/51bb3a8a33610a25aae074bfc51b1b1f-Paper-Datasets_and_Benchmarks_Track.pdf),
[review with the per-metric breakdown](https://www.themoonlight.io/en/review/agentif-benchmarking-instruction-following-of-large-language-models-in-agentic-scenarios)).

**Step-count decay, isolated.** A controlled diagnostic over 55 synthetic datasets / 55,000 examples,
15 models from 1.5B to 1.1T: **"Average first-answer accuracy (FAA) decreases from 63% at 5 steps to
20% at 95 steps"**, with six models "dropping by more than 55 percentage points". Failure modes named:
missing answers, premature answers, rare self-correction, and **under-execution — "models generated
fewer steps than required", becoming "more frequent" as procedures lengthen**. And the look-back
result: **"Increasing dependency depth from the immediately preceding variable to up to seven steps
back further reduces average accuracy by 23.85 percentage points."**
([arXiv 2605.00817](https://arxiv.org/html/2605.00817)).
Under-execution is precisely "skipped a step and said nothing", measured.

**The Compliance Gap — the single most important source for fork 5.** Six frontier models, default
conditions: **all exhibited a 0% instruction compliance rate**. "Claude Sonnet 4 verbally agrees ten
out of ten times then bypasses in all ten," a 100-point gap between stated and actual. The
discriminating variable was whether complying produced a rewarded artifact: **"models comply 97% on
tasks where rationale is rewarded (audit trails)… 0–4% where it is not (file reading, privacy
masking)"**. Removing the delegation tool raised compliance "from 0% to 75% (Cohen's d=2.47)". Nine
blinded text-only raters reached "Fleiss' κ=0.130 and correctly identify zero of fifteen compliant
sessions". The authors' remedy is architectural: a **"dual-channel audit architecture" routing verbal
output and tool-call logs to separate scorers**, because "only reward signals observing process… can
close it" ([arXiv 2605.01771](https://arxiv.org/abs/2605.01771),
[HTML](https://arxiv.org/html/2605.01771v1)).

**False success at completion time.** "87 of 97 agents self-stopped"; **"55 agents reported success
while failing verification"**; a **79% false-success rate** for a reasoning model whose traces
"rationalize completion rather than verify it"; and LLM-judge verification tops out at **AUROC 0.65**
because "judges anchor on confident closing-message language as evidence of completion, and false
success trajectories produce exactly this language". The stated remedy: judge "by the tool-observed
state and downstream artifacts, not only by the agent's narration"
([arXiv 2606.09863](https://arxiv.org/pdf/2606.09863)).

**SOP execution, end to end.** SOP-Bench (Amazon, 1,800+ tasks, 10 industrial domains): **average
success 27% for function-calling agents and 48% for ReAct agents**, and "incorrect tool invocation
approached 100% when the tool registry was overly large"
([arXiv 2506.08119](https://arxiv.org/abs/2506.08119),
[Amazon Science](https://www.amazon.science/publications/sop-bench-complex-industrial-sops-for-evaluating-llm-agents)).
SOPBench (UCSB, 167 executable tools, 7 domains, 70 verifiable SOPs, 800+ cases): best reasoning model
**o4-mini-high at 76.08% overall pass rate**, ~30% on the hardest domains, most open-source models
below 50%, and "performance degrades notably as constraint complexity increases"
([arXiv 2503.08669](https://arxiv.org/abs/2503.08669), [repo](https://github.com/Leezekun/SOPBench)).
GuideBench (ACL 2025, 1,272 instances, 537 rules): GPT-4o 86.48% overall but **13.46% on the
constraint-heavy math domain**; ablating the guidelines degraded accuracy across domains, confirming
guidelines help — they simply are not followed completely
([ACL Anthology](https://aclanthology.org/2025.acl-long.557/),
[arXiv HTML](https://arxiv.org/html/2505.11368v1)).

**Position and conflict.** The lost-in-the-middle result: accuracy "traces a U-shaped curve… the gap
between best and worst position reaching 20 to 30 points" across GPT-3.5, GPT-4, Claude and open
models; degradation "by more than 30%" when the needed content sits mid-context
([context-rot overview](https://www.morphllm.com/context-rot),
[Never Lost in the Middle](https://arxiv.org/pdf/2311.09198)).
**Caveat that must be carried:** at least one study "found no consistent relationship between
instruction-following rates and instruction position across models, with middle instructions generally
not having lower rates than first or last". Lost-in-the-middle is robust for *retrieval*; its transfer
to *instruction following* is contested. Treat position as a weak lever.
On conflicts: without hierarchy training "LLMs treat all instruction sources equally"; GPT-4o reached
**only 63.8% obedience to designated priority instructions even with explicit emphasis**, and IHEval
found the best open-source model at **48% accuracy resolving instruction conflicts**
([Where Instruction Hierarchy Breaks](https://arxiv.org/pdf/2606.07808),
[OpenAI, instruction hierarchy](https://openai.com/index/instruction-hierarchy-challenge/)).

**Decomposition helps, and it is the only lever with an upside number.** Decomposed prompting reports
a **22.7% accuracy gain** over monolithic prompting on a complex reasoning task and a reported **32%
reduction in hallucinations**, at a cost of workflows "on average 35% slower", with the caveat that
"mistakes in early subtasks can propagate"
([AI21 glossary](https://www.ai21.com/glossary/foundational-llm/task-decomposition/),
[EmergentMind on DecomP](https://www.emergentmind.com/topics/decomposed-prompting-decomp)).

**Structural formatting.** Anthropic's own guidance is that Claude "follow[s] instructions literally
instead of inferring intent" and that the task, output format and success criteria should be spelled
out; XML-style delimiters are recommended for complex prompts
([platform.claude.com prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)).
The frequently quoted "20–40% more consistent outputs" figure appears only in secondary blog posts
attributing it to unpublished internal testing — **`UNVERIFIED`; do not cite it in the spec.**

### 2.5 Ambiguity elimination

**RFC 2119 / RFC 8174.** The closed keyword set is MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD,
SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL. RFC 8174's entire contribution is
machine-relevant: **"the key words have the meanings specified herein only when they are in all
capitals. When these words are not capitalized, they have their normal English meanings"** — which
makes a lowercase `must` in a normative document a *detectable defect class*, not a matter of taste
([RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html),
[datatracker](https://datatracker.ietf.org/doc/rfc8174/)).

**Decision tables over prose conditionals.** Tables "aid in removing confusion or ambiguity… since
each condition is documented and for each condition, each possible outcome is specified", and they
"make it possible to detect combinations of conditions that would otherwise not have been found and
therefore not tested or developed"; prose specifications hide gaps "due to the prose's bulkiness and
ambiguities". Structured English is the middle ground
([Methods & Tools](https://www.methodsandtools.com/archive/archive.php?id=39),
[Reqtest guide](https://reqtest.com/en/knowledgebase/a-guide-to-using-decision-tables/),
[King, CACM, on residual ambiguity in limited-entry tables](https://dl.acm.org/doi/pdf/10.1145/364096.364113)).
This pairs with AgentIF's measured weakness on **Condition** constraints — the one constraint class
models handle worst is exactly the class decision tables exist to disambiguate. `INFERENCE`, but a
well-supported one: **conditional logic in a playbook step should be a table, not a sentence.**

**One instruction, one action** is the single rule every source in §2.3 states independently —
ASD-STE100, Microsoft, Google, DITA's mandatory singular `cmd`. It is the most cross-validated
structural rule in the whole corpus, though none of the four offers a controlled measurement.

### 2.6 Why procedures fail

**Normalization of deviance** (Vaughan, post-Challenger): "the process in which deviance from correct
or proper behavior or rule becomes culturally normalized". The mechanism is specifically **success
after deviation** — "a successful outcome… after a rule has been broken… gradually reclassifies the
behavior from 'risky exception' to 'standard practice'", driven by "production pressure" and
"increasing tolerance for shortcuts or 'optimizations' that allow increased performance"
([Wikipedia](https://en.wikipedia.org/wiki/Normalization_of_deviance),
[risk-engineering.org on practical drift](https://risk-engineering.org/concept/Rasmussen-practical-drift),
[Psych Safety on Challenger](https://psychsafety.com/normalisation-of-deviance/)).

**Work-as-imagined vs work-as-done** (Hollnagel): WAI "describes what should happen under normal
working conditions", WAD "describes what actually happens"; Safety-I responses of "strict procedural
compliance and extensive documentation" assume "that work activities can be fully anticipated and
controlled through predefined procedures, overlooking the adaptive adjustments" that actually make
things go right
([NHS England white paper](https://www.england.nhs.uk/signuptosafety/wp-content/uploads/sites/16/2015/10/safety-1-safety-2-whte-papr.pdf),
[ECRI intro](https://www.ecri.org/EmailResources/PSRQ/ClinRiskMgmt/Session%203_Introduction%20to%20Safety-I%20and%20Safety-II.pdf)).

**Ritualisation — the failure mode a GATE/CHECK playbook will actually hit.** A 2024 *Sociology of
Health & Illness* study on the surgical safety checklist found "nurses completed the forms whether
SSCs were performed or not to ensure their accountability, to avoid the extra work, and in some
instances the boxes were all ticked ahead of surgical procedures, before nurses could ascertain
whether the steps were completed"
([Facey et al. 2024](https://onlinelibrary.wiley.com/doi/10.1111/1467-9566.13746),
[summary](https://safety177496371.wordpress.com/2024/02/14/the-ritualisation-of-the-surgical-safety-checklist-and-its-decoupling-from-patient-safety-goals/)).
Generalised: "a tick-box culture is what happens when the evidence of control becomes more important
than the reality of control"
([Drillster](https://drillster.com/en/blog/what-is-a-tick-box-culture),
[ICA on compliance theatre](https://www.int-comp.org/insight/the-theatre-of-compliance/)).
**Pre-ticking is the human analogue of the 0/15 blind-rater result.** Both say the same thing: a
recorded confirmation is not evidence unless something outside the confirmer produced it.

**The machine analogue exists and is named.** Conformance checking in process mining compares an
**event log** against a **process model**; alignment-based techniques "exactly pinpoint the deviations
causing nonconformity", and for declarative models it "boils down to checking for each trace… if it
satisfies each constraint"
([Appian glossary](https://appian.com/process-mining/conformance-checking),
[A Task Taxonomy for Conformance Checking](https://arxiv.org/pdf/2507.11976)).
Its two required inputs are the model and **a log the executor emitted while executing**. A playbook
mode that produces no per-step log has, by construction, made adherence unmeasurable.

---

## 3. The two reference playbooks, measured against that evidence

They are two genres, and the evidence separates them cleanly.

| | `content-plan/PLAYBOOK.md` | `brand/art-style/HYBRID-PLAYBOOK.md` |
|---|---|---|
| Size | 14,016 words / 88,331 B / 1,290 lines | 2,686 words / 18,202 B / 245 lines |
| Shape | 110 numbered steps, 86 `GATE`, 95 `CHECK` | parameter table + slotted prompt scaffold + 4 hard rules + accepted-instance library + ruled-out list |
| Largest addressable unit | Checklist B, 5,883 words, 52 steps | §2, ~700 words |
| Against AgentIF's 6,000-word cliff | **2.3x over whole-file; B alone is at it** | comfortably under |
| Against the 5→95-step FAA decay | 110 steps sits at the far end of the measured curve | 8 scenes x ~5 fills |
| Look-back depth | high — A4 references A5/D5/I9/I24 across thousands of words | low — every variable is a row in one table |
| Explanation interleaved with action | heavy (A4 carries roughly 350 words of superseded history *inside* the step) | separated into "what was ruled out" plus dated provenance |

`PLAYBOOK.md`'s contribution is the **discipline**: every step tagged, an invariant (`I21`) that reds
an untagged step or a `GATE` naming no runnable leg, and the honest self-description "an untagged
step, or a `GATE` naming no runnable leg, is a bug in this file — report it rather than guessing".
`HYBRID-PLAYBOOK.md`'s contribution is the **physical form**: a parameter table, one slot per varying
value, hard rules each traced to a dated owner correction, an accepted-instance library, and an
explicit don't-re-try register.

**Adversarial note on fork 4: do not average them.** Fork 4 says "corpus-derived plus external
research". The corpus contains one artifact whose *form* the external evidence contraindicates and one
whose *form* it endorses. Deriving a template by blending both produces a 7,000-word compromise that
is still over the cliff. The defensible derivation is **PLAYBOOK's tagging discipline poured into
HYBRID's physical form.**

---

## 4. Ranked structural features for the PLAYBOOK TEMPLATE

Ranked by evidence strength, strongest first. `M` = machine-checkable; `C` = inherently CHECK-only.
Feeds fork 5 directly; §6 has the full split.

### Tier A — directly measured on the actual reader

| # | Feature | Evidence | M/C |
|---|---|---|---|
| A1 | **Every step's compliance leaves an artifact.** A step is `GATE <leg>` (a runnable check) or `CHECK <why> · witness <field>` — a named field the run MUST write. No step whose only evidence is the run's assertion. | 97% vs 0–4% (Compliance Gap); 0/15 blind detection; "a silent checkbox catches nothing" (WHO); pre-ticking (Facey 2024) | M that a witness is *named*; C that it is *true* |
| A2 | **A hard, derived word budget per addressable segment.** The unit an agent loads at one time must sit well under the measured cliff. The cap is computed and printed by the checker; never typed into prose. | AgentIF: ISR → ~0 above 6,000 words; corpus average 1,723 | M |
| A3 | **Segmentation into independently addressable, stably-identified units**, executed one per pass, with the segment re-read at each pass rather than carried. | FAA 63% at 5 steps → 20% at 95; under-execution rises with length; decomposition +22.7% / −32% hallucinations | M (ids unique/dense; segment sizes) |
| A4 | **Completion derived from the environment, never self-reported.** Piece count = files present at declared output paths; step coverage = ledger rows vs declared step ids. | 55/97 false success; 79% for a reasoning model; LLM judges cap at AUROC 0.65; conformance checking requires a log | M |
| A5 | **Bounded look-back.** A step MUST NOT depend on a value set more than *k* steps earlier unless that value is restated in a named slot the step reads. | −23.85pp from depth 1 → 7 | M (partially: count cross-references to earlier step ids) |
| A6 | **Conditional logic as a table, not a sentence.** Condition/outcome pairs enumerated. | AgentIF: Condition constraints are the worst class, failing on "incorrect checking"; decision-table literature on ambiguity and gap detection | M (partially: red a step line carrying more than one conditional) |
| A7 | **A declared precedence line** naming what outranks the playbook and what the playbook outranks. | GPT-4o 63.8% obedience to designated priority; IHEval best open-source 48% on conflicts | M (presence); C (correct resolution) |
| A8 | **Cap and segment the producer/tool inventory**, even though fork 7 keeps it in playbook prose. | SOP-Bench: "incorrect tool invocation approached 100% when the tool registry was overly large" | M (count) |

### Tier B — cross-validated standards consensus, no controlled measurement on a model reader

| # | Feature | Evidence | M/C |
|---|---|---|---|
| B1 | **One action per step; one imperative sentence; lead verb from a closed table.** | ASD-STE100 rule; DITA mandatory singular `cmd`; Microsoft "a separate step for each instruction"; Google "one step for each action" | M |
| B2 | **Sentence-length cap ~20 words in procedural lines.** | ASD-STE100 Issue 9 | M |
| B3 | **Condition and location precede the verb.** "In `<path>`, if `<state>`, do `<action>`." | Microsoft, verbatim; Diátaxis conditional imperative "If you want x, do y" | M (regex over step-line prefixes) |
| B4 | **Fixed required section set** — identity/version/approval/effective-date/review-interval, prerequisites, context, steps, result, revision log. | ISO 9001 7.5 control requirements; GMP written-procedure and independent approval; DITA `prereq`/`context`/`steps`/`result` | M (presence and non-hollowness) |
| B5 | **Result distinct from action** — a per-step expected outcome element separate from the command. | DITA `stepresult` is not `cmd` | M (presence) |
| B6 | **Explanation excluded from the step body; provenance carried as an id, never a paragraph.** | Diátaxis "action and only action… if they're important, link to them"; Prompt Complexity Dilutes Structured Reasoning; the charter's own §6 rule that provenance rides as a decision id | M (advisory: word-count on step bodies, printing hits *and* near-misses) |
| B7 | **RFC-2119 closed modality vocabulary, uppercase-only.** | RFC 8174: meanings apply "only when they are in all capitals" | M |
| B8 | **Prohibitions are their own element type, self-contained, never carrying a step.** | MIL-STD-38784B on warnings/cautions; `PLAYBOOK.md` `B6` already conforms | M (structural) |
| B9 | **A ruled-out register** — what was tried, when, by whom, and why it must not be re-tried. | `HYBRID-PLAYBOOK.md`'s "what was ruled out" section; normalization of deviance says re-litigating a settled ban is the drift path | M (presence plus dated rows) |
| B10 | **Approver is not the executor**, at least for the playbook document itself. | GMP quality unit; ISO 9001 approval control | M (a `curated-by` field distinct from the writing run) |

### Tier C — weak but worth keeping

- **Negative instructions paired with a replacement.** "Positive framing beats negative" is widely
  repeated and thinly evidenced; the one usable nuance found is that negatives work "when negatives
  are specific and paired with 'instead, do X'". Keep the bans; require each to name the replacement
  ([Gadlet](https://gadlet.com/posts/negative-prompting/),
  [Virtualization Review](https://virtualizationreview.com/articles/2025/12/08/using-negative-ai-prompts-effectively.aspx)).
- **Worked examples / accepted-instance library.** AgentIF measures Example-presentation constraints at
  only 10.6% of its corpus and does not isolate their effect; the corpus evidence
  (`HYBRID-PLAYBOOK.md`'s accepted-8 table) is strong practice with no external measurement. Keep it,
  mark it `unmeasured`.
- **Structured delimiters / XML-style tagging.** Recommended by Anthropic's own docs; the "20–40%"
  magnitude is `UNVERIFIED`. Adopt the practice, never quote the number.

---

## 5. Popular features the evidence does NOT support — report loudly

1. **"Five to nine items, one page, sixty to ninety seconds."** This is Gawande's rule, its stated
   basis is *human working memory*, and the aviation human-factors reviews say checklist-construction
   research is scarce. The mandate-scale replication of the checklist it comes from found **no**
   mortality benefit across 101 hospitals. It will be the first number a template designer reaches
   for, and it is the wrong number for a machine reader — the machine-reader numbers are the
   6,000-word ISR cliff and the 5→95-step FAA decay. **Do not put 5–9 in the template.**
2. **DO-CONFIRM as an available mode.** DO-CONFIRM presupposes an expert who already did the work
   correctly from memory and now confirms it. The false-success evidence says an agent's
   confirmation-from-memory is *precisely* the measured failure — 79% false success with traces that
   "rationalize completion rather than verify it". **READ-DO is the only defensible mode here, and the
   template should say so and ban the other**, rather than offering a choice the literature appears
   to offer.
3. **Carroll's minimalism.** Popular in tech-writing circles, admitted thin evidence, and doctrinally
   opposed to prescriptive step-following ("instead of controlling it through warnings and ordered
   steps").
4. **Position engineering ("put the critical rules at the top and bottom").** Lost-in-the-middle is
   robust for retrieval, but at least one study "found no consistent relationship between
   instruction-following rates and instruction position". Weak lever; do not build a template rule on it.
5. **LLM-as-judge for "did it follow the playbook".** AUROC ceiling 0.65, and judges anchor on
   confident closing language. A reviewer sub-agent reading the transcript to certify adherence is the
   0/15 blind-rater experiment re-run in-house.
6. **Prose rationale inline as a compliance aid.** Intuitive; measured backwards. Complexity dilutes
   structured-reasoning adherence, and Diátaxis says explanation "dilutes the useful power of the
   guide". `PLAYBOOK.md` A4's roughly 350 words of superseded history live inside the step they qualify.

---

## 6. Machine-checkable vs CHECK-only — the fork-5 split

Two populations, because a playbook is checked at two different moments.

### 6.1 Over the playbook FILE (a gate leg the adopting repo owns)

| # | Assertion | Note |
|---|---|---|
| P1 | Every step line carries exactly one tag from the closed set `{GATE, CHECK}`. | `PLAYBOOK.md` `I21` already does this. Portable as-is. |
| P2 | Every `GATE <leg>` resolves to a runnable leg in the adopting repo's manifest. | `I21` does this too. **Must carry a liveness assertion**: a resolver that can resolve nothing reports zero broken legs, which is indistinguishable from all-good. |
| P3 | **Every `CHECK` names a witness field.** | The new requirement F2 demands. Cheap: one more capture group in the regex that already finds `CHECK`. |
| P4 | Step ids unique and dense; every cross-reference names a defined id. | Set arithmetic. |
| P5 | No addressable segment exceeds the derived word budget; the checker computes and prints both the budget and the per-segment figures. | Obeys "no count of a derived population is written in prose". |
| P6 | Declared `output-paths` present, non-empty, each carrying a declared **kind/extension set**. | See §6.3 — this narrows a class fork 2 conceded to CHECK. |
| P7 | Required sections present and non-hollow; an inapplicable section keeps its heading with `N/A — <why>`. | Lifted from `memory/TEMPLATE-SPEC.md`'s writing rules, already gated for specs in this repo. Reuse, do not reinvent. |
| P8 | Each step's lead verb is in the playbook's closed verb table. | Reuses the `.lexicon.conf` verb-table machinery the charter describes in §12. |
| P9 | No lowercase `must`/`should`/`may` in a normative step line; RFC-2119 keywords uppercase only. | RFC 8174 makes this a defect class rather than a style opinion. |
| P10 | One imperative sentence per step body, at most ~20 words. | ASD-STE100. Regex-grade. |
| P11 | A step body contains at most one conditional; multi-condition logic must be a table. | AgentIF's worst constraint class. |
| P12 | Look-back distance: no step references a step id more than *k* positions earlier without a slot restatement. | *k* is an open question (§8). |
| P13 | Precedence line present; `curated-by` present and distinct from the authoring run's slug. | Presence only. |
| P14 | Prohibition blocks carry no numbered steps. | MIL-STD-38784B's rule; the corpus already conforms. |
| P15 | Every ruled-out row carries a date and a resolver. | Structural. |

### 6.2 Over the RUN (derived, at close)

| # | Assertion |
|---|---|
| R1 | Piece count = files present at declared output paths, **derived**, compared against requested N. Never the run's own tally. |
| R2 | Step-ledger coverage: the set of step ids with a recorded outcome equals the set the playbook declares. A missing row is an under-execution, which is the *named* measured failure mode. |
| R3 | Every `GATE` leg named by an executed step actually ran, with a recorded verdict; a skipped leg is recorded with the `skipped` shape and a reason, never omitted. |
| R4 | Every `CHECK` witness field is non-empty. (Non-empty, not true — see §6.3.) |
| R5 | The diff touches nothing outside declared output paths plus the run's own records (fork 2). |
| R6 | Every declared **deviation** carries a step id and a reason; a step with neither a ledger row nor a deviation row is a silent skip and reds. |

### 6.3 Inherently CHECK-only — and what each blind spot is

Stating these is the house rule "a gate's own header states what it does NOT check", applied to the
whole feature.

- **Whether a `GATE` leg tests what its name claims.** No gate can gate this. It is the recursion the
  charter already names.
- **Whether a `CHECK` witness is truthful.** Measured undetectable from text: 0/15, κ=0.130. The
  witness converts a *silent skip* into a *written falsehood* — a smaller and more attributable class,
  not an eliminated one. Say that plainly rather than claiming coverage.
- **Whether the playbook's steps are the right steps.** Work-as-imagined. Only production reveals it,
  which is what fork 6's proposal register is for.
- **Whether a code change hid inside a declared output path.** Fork 2's conceded class. **Partially
  recoverable, and worth proposing:** if each declared output path also declares a kind/extension set
  (`article -> .md`, `image -> .png|.webp`), a gate reds a `.py`/`.sh`/`.ts`/`.js` file appearing under
  a path declared as content. That does not close the class — a `.md` file can contain a build script —
  but it converts the common case from unseen to red, and the residue is a much narrower stated CHECK.
- **Whether a proposal is worth taking.** Owner judgment by construction.
- **Whether the piece is any good.** Taste. No leg.

---

## 7. Loud reports on the seven settled forks

None of the seven is refuted. Two need an amendment, one needs a caveat, one is strengthened.

- **Fork 5 — needs an amendment, and it is the loudest thing in this record.** The GATE/CHECK binary is
  correct and is exactly the WHO "who answers this item" discipline. But `CHECK <why>` as written is
  the 0–4% arm of the only experiment that isolated it. **Add a mandatory witness field to the CHECK
  grammar** — `CHECK <why> · witness <field>` — so that complying produces an artifact rather than a
  private intention. This costs one capture group in the checker and one column in the template, and
  it is the difference between the 4% condition and the 97% condition.
- **Fork 3 — strengthened, with one condition.** Pieces-as-passes *is* the decomposition the
  measurements reward (+22.7% / −32% hallucinations). The condition: degradation tracks **context
  length**, not pass number, so each pass must **re-read its playbook segment** rather than inherit it
  from the previous pass's context. A run that loads the whole playbook once and does eight passes
  takes the 14,016-word cliff eight times. And "the DoD must count pieces against requested N" is only
  safe if the count is derived from the filesystem (R1) — a self-tallied count is the 55-of-97 failure
  verbatim.
- **Fork 4 — supported, with a warning against averaging.** The two reference playbooks are two genres
  and the evidence endorses one form and one discipline, from different files. Blend the discipline
  into the form; do not blend the forms. The "freeze it and mark it human-curated" half is
  independently important for the same reason the charter gives for the lexicon table: a derived
  artifact nobody edited is a mirror of its subject, and a mirror cannot gate.
- **Fork 7 — supported by Diátaxis's how-to/reference split, with one measured caveat.** Producer
  knowledge is reference; the playbook is the how-to; keeping the kit agnostic is the standard
  position. The caveat: agnosticism pushes the whole tool inventory into playbook prose, and SOP-Bench
  measured "incorrect tool invocation approached 100% when the tool registry was overly large". The
  template needs a **cap or segmentation rule on the producer section specifically**, or fork 7's cost
  lands exactly where the benchmark says it hurts.
- **Fork 6 — supported, plus one field.** No external evidence bears on park-vs-proposal directly. But
  normalization of deviance says the highest-risk improvement is one that arose from a *deviation that
  succeeded* — that is the literal mechanism by which a rule stops being a rule. The proposal register
  should record **whether the proposal came from a deviation**, because that flag is the drift signal
  and it is free to capture at the moment the deviation row is written (R6).
- **Fork 1 — no evidence against.** One note: the instruction-hierarchy numbers (63.8% obedience with
  explicit emphasis; 48% conflict resolution) mean the unattended entry point cannot resolve a
  playbook-versus-charter conflict by judgment at anything like reliable rates. It must resolve by a
  **declared precedence line** (A7/P13). The attended entry point can ask; the unattended one cannot,
  and that asymmetry belongs in the template rather than in the run's discretion.
- **Fork 2 — no evidence against**, plus the kind/extension narrowing in §6.3 that converts part of its
  conceded CHECK class into a gate.

**On the phrase "follows a playbook TO THE LETTER."** Nothing in the measured literature does that.
SOP-Bench 27%/48%, SOPBench 76.08% at best, AgentIF 26.9% ISR, procedural FAA 20% at 95 steps.
Diátaxis and Hollnagel both say the linear-procedure premise is false in general. The design
implication is not to abandon the goal but to make deviation **declarable and recorded** (R6): without
a way to write "I did not do step 7, and here is why", the run will simply not do step 7 and say
nothing, and the ritualisation literature says the box gets ticked anyway.

---

## 8. Open questions this lens could not resolve

- **Does the 6,000-word cliff transfer to a file read in segments?** AgentIF's instructions are
  system-prompt-shaped. A playbook segment loaded by a file tool at the moment it is needed may behave
  differently. Measurable in-repo with a small probe, and it should be measured before a number is
  frozen into the template.
- **What is *k* for bounded look-back (A5/P12)?** The −23.85pp figure spans depths 1 to 7 with no
  stated threshold. Any *k* chosen now is an authored number sitting where a derived one belongs.
- **Does a step-ledger gate (R2) survive a run that writes rows without doing the work?** Almost
  certainly not — it is the 0/15 problem one level up. The honest claim is class reduction, not
  elimination, and the gate's own header should say so.
- **Can `.lexicon.conf`'s verb table be reused for content steps, or does playbook prose need its
  own?** The charter's table is derived from a code corpus; content verbs (`draft`, `render`,
  `publish`, `caption`) may not fit it.
- **Is the Microsoft "seven steps or fewer" limit real?** The page I fetched does not contain it; a
  secondary summary asserts it. Unverified, and a Tier-C number regardless.

---

## 9. Sources

Checklist discipline —
[NEJM Urbach et al., Ontario](https://www.nejm.org/doi/full/10.1056/NEJMsa1308261) ·
[PubMed 24620866](https://pubmed.ncbi.nlm.nih.gov/24620866/) ·
[Ariadne Labs, WHO SSC](https://www.ariadnelabs.org/safe-surgery-safe-systems/surgical-safety/who-surgical-safety-checklist/) ·
[PSNet/AHRQ on implementation quality](https://psnet.ahrq.gov/issue/comparative-effectiveness-analysis-implementation-surgical-safety-checklists-tertiary-care) ·
[ERAU JAAER, Ross](https://commons.erau.edu/jaaer/vol13/iss2/4/) ·
[NASA Ames CR-177549](https://www.faa.gov/sites/faa.gov/files/2022-11/NASA%20Ames%20Rpt%20CR%20177549%20.pdf) ·
[NASA Ames, EA checklist design](https://human-factors.arc.nasa.gov/flightcognition/Publications/EA_Checklist_Design.pdf) ·
[Shortform, checklist types](https://www.shortform.com/blog/types-of-checklists/) ·
[Sivers, book notes](https://sive.rs/book/ChecklistManifesto) ·
[Mann, book notes](https://grahammann.net/book-notes/the-checklist-manifesto-atul-gawande)

SOP standards —
[ISMS.online, ISO 9001 cl. 7.5](https://www.isms.online/iso-9001/clause-7-5-documented-information/) ·
[Auditor Training Online, cl. 7.5.3](https://blog.auditortrainingonline.com/blog/explaining-iso-9001-clause-7.5.3-control-of-documented-information) ·
[Qualio, 21 CFR 211](https://www.qualio.com/blog/21-cfr-211) ·
[GMP SOP guide](https://www.workprocedures.com/blog/pharmaceutical-gmp-sop-guide) ·
[MIL-STD-38784B](https://cvgstrategy.com/wp-content/uploads/2023/04/MIL-STD-38784B.pdf)

Procedural documentation —
[OASIS DITA 1.3 task elements](https://docs.oasis-open.org/dita/dita/v1.3/csd01/part2-tech-content/langRef/containers/task-elements.html) ·
[DITA strict task topic](https://docs.oasis-open.org/dita/dita/v1.3/errata02/os/complete/part3-all-inclusive/archSpec/technicalContent/dita-task-topic.html) ·
[Diátaxis, how-to guides](https://diataxis.fr/how-to-guides/) ·
[Microsoft, step-by-step instructions](https://learn.microsoft.com/en-us/style-guide/procedures-instructions/writing-step-by-step-instructions) ·
[Google, procedures](https://developers.google.com/style/procedures) ·
[ASD-STE100](https://www.asd-ste100.org/) ·
[ASD Europe on STE](https://www.asd-europe.org/standards-specifications/simplified-technical-english/) ·
[STE writing-rules extraction](https://github.com/danyuchn/asd-ste100-skill/blob/master/references/writing-rules.md) ·
[Minimalism (technical communication)](https://en.wikipedia.org/wiki/Minimalism_(technical_communication)) ·
[IEEE on The Nurnberg Funnel](https://ieeexplore.ieee.org/document/62813/)

LLM instruction following —
[AgentIF, arXiv 2505.16944](https://arxiv.org/abs/2505.16944) ·
[AgentIF NeurIPS PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/51bb3a8a33610a25aae074bfc51b1b1f-Paper-Datasets_and_Benchmarks_Track.pdf) ·
[AgentIF review with per-metric numbers](https://www.themoonlight.io/en/review/agentif-benchmarking-instruction-following-of-large-language-models-in-agentic-scenarios) ·
[When LLMs Stop Following Steps, arXiv 2605.00817](https://arxiv.org/html/2605.00817) ·
[The Compliance Gap, arXiv 2605.01771](https://arxiv.org/abs/2605.01771) ·
[From Confident Closing to Silent Failure, arXiv 2606.09863](https://arxiv.org/pdf/2606.09863) ·
[SOP-Bench, arXiv 2506.08119](https://arxiv.org/abs/2506.08119) ·
[SOPBench, arXiv 2503.08669](https://arxiv.org/abs/2503.08669) ·
[GuideBench, ACL 2025](https://aclanthology.org/2025.acl-long.557/) ·
[Where Instruction Hierarchy Breaks, arXiv 2606.07808](https://arxiv.org/pdf/2606.07808) ·
[OpenAI, instruction hierarchy](https://openai.com/index/instruction-hierarchy-challenge/) ·
[Never Lost in the Middle, arXiv 2311.09198](https://arxiv.org/pdf/2311.09198) ·
[Context rot overview](https://www.morphllm.com/context-rot) ·
[Prompt Complexity Dilutes Structured Reasoning, arXiv 2603.13351](https://arxiv.org/pdf/2603.13351) ·
[Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) ·
[Task decomposition](https://www.ai21.com/glossary/foundational-llm/task-decomposition/) ·
[DecomP](https://www.emergentmind.com/topics/decomposed-prompting-decomp)

Ambiguity elimination —
[RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html) ·
[RFC 8174 datatracker](https://datatracker.ietf.org/doc/rfc8174/) ·
[Decision tables for requirements analysis](https://www.methodsandtools.com/archive/archive.php?id=39) ·
[Reqtest decision-table guide](https://reqtest.com/en/knowledgebase/a-guide-to-using-decision-tables/) ·
[King, Ambiguity in Limited Entry Decision Tables](https://dl.acm.org/doi/pdf/10.1145/364096.364113)

Why procedures fail —
[Normalization of deviance](https://en.wikipedia.org/wiki/Normalization_of_deviance) ·
[Rasmussen and practical drift](https://risk-engineering.org/concept/Rasmussen-practical-drift) ·
[Psych Safety on Challenger](https://psychsafety.com/normalisation-of-deviance/) ·
[Hollnagel, Safety-I and Safety-II white paper](https://www.england.nhs.uk/signuptosafety/wp-content/uploads/sites/16/2015/10/safety-1-safety-2-whte-papr.pdf) ·
[ECRI, intro to Safety-I/II](https://www.ecri.org/EmailResources/PSRQ/ClinRiskMgmt/Session%203_Introduction%20to%20Safety-I%20and%20Safety-II.pdf) ·
[Facey et al. 2024, ritualisation of the SSC](https://onlinelibrary.wiley.com/doi/10.1111/1467-9566.13746) ·
[Summary of Facey et al.](https://safety177496371.wordpress.com/2024/02/14/the-ritualisation-of-the-surgical-safety-checklist-and-its-decoupling-from-patient-safety-goals/) ·
[Tick-box culture](https://drillster.com/en/blog/what-is-a-tick-box-culture) ·
[Theatre of compliance](https://www.int-comp.org/insight/the-theatre-of-compliance/) ·
[Conformance checking glossary](https://appian.com/process-mining/conformance-checking) ·
[A Task Taxonomy for Conformance Checking, arXiv 2507.11976](https://arxiv.org/pdf/2507.11976)
