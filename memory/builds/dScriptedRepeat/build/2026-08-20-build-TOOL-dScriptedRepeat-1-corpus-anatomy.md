**Serves:** research TOOL-dScriptedRepeat-1

# Lens 2 — corpus anatomy: what a PLAYBOOK TEMPLATE must carry

Node `d` · 2026-08-20 · slug `dScriptedRepeat` · streams `tooling`.

**Method.** Both reference playbooks read in full, byte-level, from `C:/projects/nicocares/main`.
Every number below was derived by a command run in this session and the command is shown. Where a
claim is an inference it says INFERENCE. The nicocares checker was RUN, and three failing cases were
STAGED against it and observed — the tree was byte-restored from a scratchpad snapshot afterwards and
`git status --porcelain` in that repo is empty (md5 `8741ac366732e2bfea9ba84ae8261286` before and
after).

**Headline.** The template's spine is not the GATE/CHECK tag. It is the pair **(declared output
envelope, corpus-level rules)** — and the seven settled forks name the first only obliquely and the
second not at all. The tag contract is real and worth keeping, but the reference implementation of it
is weaker than it reads, in four measured ways, and one of the two reference playbooks does not use
it at all.

---

## 0. The two files, measured

```
$ wc -l content-plan/PLAYBOOK.md brand/art-style/HYBRID-PLAYBOOK.md
  1290 content-plan/PLAYBOOK.md
   245 brand/art-style/HYBRID-PLAYBOOK.md
```

| | `content-plan/PLAYBOOK.md` | `brand/art-style/HYBRID-PLAYBOOK.md` |
|---|---|---|
| lines / bytes | 1290 / 88,331 | 245 / 18,202 |
| top-level sections | 8 (`# title`, `## 0. Ground rules`, 6 `## Checklist <L>`) | 12 (11 H2 + 1 H3 `### 3b`) |
| numbered steps | **110** | 9 numbered items (4 hard rules + 5 new-scene steps) |
| `GATE` tag emissions | **90** (86 single-line + 4 line-wrapped) | **0** |
| `CHECK` tag emissions | **95** | **0** |
| markdown tables | 21 | 4 |
| distinct dates carried | 11 | 3 |
| ratification / acceptance ids | 13 distinct `PKG-*` ids over 26 mentions | 1 session name (`aWovenPortrait`), 0 ids |
| enforcing program | `scripts/check_content_plan.py`, 2,861 lines, a `ci.yml` leg | none — "imagery compliance = owner acceptance" |

Correcting the build README in passing: it records "92 GATE tags, 95 CHECK tags, 110 numbered steps".
110 and 95 are right. **92 is the count of the string `GATE`, not of tags** — two of those 92 are
prose uses of the concept ("a `GATE` naming no runnable leg", "it cites a `GATE`"). The tag count is
90. The README also writes all three numbers in prose, which is the class this repo's own charter
bans.

---

## 1. `content-plan/PLAYBOOK.md` — section-by-section anatomy

### 1.1 The masthead (L1–L20)

Four blocks, and each does a job the other three cannot.

**L3 — the addressee.** `You are planning or writing content for the NicoCares blog. This file is the
whole process.` Second person, and a completeness claim. **Load-bearing.** It is what licenses every
`CHECK` below: if this file is the whole process, an untagged step is a hole rather than a hand-off.
Machine-checkable? No.

**L5–L7 — the tag contract, stated by the document about itself.**

> Every step is tagged **`GATE <leg>`** (a named machine check fails if you get it wrong) or `CHECK`
> (no gate can see this; the reason is stated). An untagged step, or a `GATE` naming no runnable leg,
> is a bug in this file — report it rather than guessing. `GATE I21` enforces both.

**Load-bearing, and the single most transferable line in either file.** Machine-checkable: yes, and
enforced — see §3. Note the parenthetical *"the reason is stated"*: that is the `CHECK <why>` half of
FORK 5, and §3.5 shows it is **not** enforced.

**L9–L16 — where the legs live, plus a correction of this paragraph's own prior text.**

> **The `I*` legs live in `scripts/check_content_plan.py`, which IS a `ci.yml` leg** —
> `.github/workflows/ci.yml:68` runs it unconditionally in the `validate` job…
>
> *(This paragraph said the opposite from 2026-08-12 until 2026-08-14, and a spec that trusted it
> sized four new invariants as local advisories. Corrected by `PKG-aCandidCadence-1` S12. The kickoff
> manifest had it right the whole time, which is the tell: when two docs disagree about a leg, read
> `ci.yml`.)*

Verified: `ci.yml:68` is exactly `run: python scripts/check_content_plan.py`, inside `jobs.validate`,
unconditional. The citation resolves to the byte. **Load-bearing**, and the parenthetical is the
template's first argument for a negative-knowledge slot: the correction is *in the paragraph it
corrects*, not in a changelog.

**L18–L20 — provenance.** `Ratified 2026-08-12, PKG-bInkedFoolscap-1; revised after an adversarial
review that confirmed 44 defects in the first cut. Evidence is in
memory/builds/bInkedFoolscap/build/research/; the review is in memory/builds/bInkedFoolscap/reviews/.`
Both directories exist and hold 8 research records and 13 review records respectively.
**Load-bearing.** Machine-checkable in part: the paths resolve, the "44 defects" figure does not.

**Defect: the masthead stamp does not cover the file.** Checklist P landed 2026-08-14
(`PKG-aPennedScaffold-1`), Checklist D was rebuilt the same day (`PKG-aCandidCadence-4`), D13 landed
2026-08-20 (`PKG-bLimpidQuill-7`). The 2026-08-12 stamp sits above all of them. Only **Checklist E**
carries its own section-level stamp:

```
$ for s in "Checklist A" … ; do awk … | grep -inE "ratified|PKG-…|owner ruling" ; done
--- Checklist E ---
4:Ratified 2026-08-13 (`PKG-aCandidCadence-1`), from five researched technique records and a
```

A, P, B, C, D carry none. Provenance is instead scattered inline at step level. That works, but it is
an accident of diligence, not a structure — the template must make per-section provenance a slot.

### 1.2 `## 0. Ground rules` (L24–L41)

Four paragraphs: what the company legally is, the brand idea, the editorial lane, and a *published*
sentence quoted as the voice fingerprint. No steps, no tags, no ids. **Incidental to the machine,
load-bearing to the writer.** Machine-checkable: no. HYBRID's analogue is split between `README.md`
and `CONSISTENCY-GUIDE.md`, not in the playbook.

Template consequence: this is a **product-context** slot, and it must be OPTIONAL with a
point-at-the-owner form, or every art playbook will restate the brand book.

### 1.3 The six checklists

```
$ python  # step_re = ^\*\*([A-Z][0-9]+(?:\.[0-9]+[a-z]?)?)\.\s
TOTAL STEP HEADINGS: 110
by checklist letter: {'A': 13, 'B': 52, 'C': 14, 'D': 14, 'E': 10, 'P': 7}
dupes: []
```

| Letter | Section title | Steps | With a GATE | CHECK-only | Job |
|---|---|---|---|---|---|
| `A` | the content plan | 13 | 13 | 0 | the CORPUS plan — one row per future piece |
| `P` | the article plan | 7 | 6 | 1 | the PER-PIECE spec, a committed JSON file |
| `B` | writing one article | 52 | 21 | 31 | how to produce one piece |
| `C` | article art | 14 | **1** | 13 | the producer recipe for the piece's image |
| `D` | adversarial review | 14 | 6 | 8 | the review protocol + its record schema |
| `E` | register | 10 | 9 | 1 | voice, five closed values, gate-readable markers |

Derived tag distribution over the 110 steps:

```
GATE only : 25      CHECK only: 54      BOTH: 31      NEITHER: 0
```

**Checklist C is the finding.** Inside the most heavily gated playbook in the corpus, the *art*
checklist is 13/14 CHECK-only. That is the same shape as HYBRID-PLAYBOOK, which is 100% CHECK-only
(and untagged). Gating density is a property of the **medium**, not of the playbook's quality. A
template that assumes the gated shape will produce a fake-gated art playbook.

### 1.4 Step ID scheme

Letters are named by the section headers (`## Checklist A — the content plan`), so the letter meaning
is stated. **The numbering rules are not.** The only statement anywhere is inside one step:

> `D13`. **Runs HERE, with the style passes, despite its number** — ids in this file are permanent
> labels rather than ranks, and CKD-0..CKD-12 are already spent in nine shipped records, so it could
> not be numbered 6 without renumbering history. (L1100–L1102)

That is the *whole* documentation of the scheme, and it lives in the one step that violates document
order. **B7.9 also violates document order** — the file runs B7.6 (L745), B7.6b (L771), **B7.9
(L800)**, B7.7 (L861), B7.8 (L865) — with no explanation at all. So the scheme is
`<Checklist letter><ordinal>[.<sub>][<letter suffix>]`, ids are permanent labels not ranks, sub-steps
and letter suffixes are allowed, document order is free. None of that is written down in one place.
**Template consequence: the ID grammar is a REQUIRED declaration, not a convention** — and see §3.3
for what the letter suffix does to the checker.

### 1.5 Checklist A — the corpus plan (L43–L161)

13 steps, every one carrying a GATE. This is the checklist that has **no analogue in HYBRID** and no
analogue in the seven forks: it plans the SET before any piece exists.

- **A1** cluster vocabulary, `GATE I2/I4`, plus a `CHECK` that no invariant measures the *mix*.
- **A2** `Fill every plan field — REQUIRED_FIELDS is 23.` `GATE I3`. Verified:
  `check_content_plan.py:80-86` holds a 23-name tuple, and **I21 machine-compares the prose number
  against `len(REQUIRED_FIELDS)`**. This is the template's model answer to "a value stated beside the
  source that owns it rots": it is stated *and* gated as a pair.
- **A4** word targets — a 6×2 table of guide bands, plus the corpus-mean rule and **three generations
  of superseded history** (§4).
- **A7** closed status vocabulary, 8 values, `GATE I2`.
- **A9** runway floor: `GATE I15` at four rows briefed-or-later; the working target of eight is
  `CHECK`. A gated floor and an ungated target, explicitly distinguished. **Steal this.**
- **A10** the stub exemption, `GATE I18`, shrink-only and two-directional.

### 1.6 Checklist P — the per-piece plan (L163–L328)

7 steps. The artefact is `content-plan/plans/<slug>.json`, **the filename IS the join key**, bound to
the shipped piece in both directions by `I34`–`I38`. Schema is closed at four levels:

```
PLAN_TOP_KEYS  = {slug, questions, not_this, evidence, deviations, shape, backfilled, declined}
PLAN_Q_KEYS    = {q, anchors, dropped_because}
PLAN_EV_KEYS   = {claim, source, source_says, scope, accessed}
PLAN_DEV_KEYS  = {source, source_says, why}
QUESTION_MIN, QUESTION_MAX = 2, 8      NOT_THIS_MIN, NOT_THIS_MAX = 2, 4
ANCHOR_MIN_CHARS = 20                  SOURCE_SAYS_MIN_CHARS = 40
```

Measured: 13 plan files against 13 selected rows, 69 questions, 60 evidence rows, 0 deviations.

**P5 is the load-bearing one and it is pure `CHECK`.** "The plan does not plan the prose." It
enumerates twelve things the plan must NOT fix, and then contains the sentence a template must copy
verbatim in spirit:

> **A proposal to add a heading list, a section count, a per-section word budget or a paragraph
> outline to this file is a defect, and this sentence is here so a later session reads it before
> helpfully adding one.**

An **anti-slot rule**. It exists because the file measured its own damage: `blog/says-no` at 165
sentences, mean 11.3 words, stdev 4.5, longest sentence 21 words in 15,668 bytes, 60 of 79 paragraphs
exactly two sentences — "Nobody defected; four rules selected for that shape and none opposed it."

**P7** is the honesty rule, and it names its source: *"change is permitted, silent change is not"*
(Cochrane Handbook, in substance). A citation the plan did not carry is declared in `deviations`,
never absorbed.

### 1.7 Checklist B — producing one piece (L330–L886)

52 steps, 43% of the file. Six sub-blocks: **B0** where it physically goes · **B1** structure ·
**B2** what may be in the envelope · **B3** claims and disclosures (18 steps, the compliance core) ·
**B4** register · **B5** sources · **B7** substance · **B6** never publish.

- **B0.1** is the **output envelope**: a literal JSON object with 11 keys, shown in full. `CHECK` —
  "nothing tells you this but this step, and there is no page file." **This is the single most
  important structural element for FORK 2** and it is where the file is currently wrong (§3.1).
- **B1.4** replaced a per-sentence cap with a five-clause DISTRIBUTION contract, machine-measured by
  `scripts/prose_metrics.py`. It carries the reason: the cap produced a metronome across three
  articles. **A rule expressed as a distribution over a set, not a bound on an instance.**
- **B2.1** an explicit tag allowlist (48 tags) plus a *reached-for-and-stripped* list (`dl dt dd
  caption aside main time cite q iframe`). The negative list is worth as much as the positive one.
- **B3** is 18 steps of "what you may not say", each naming its gate or stating the gap the gate has.
  B3.2 is exemplary: `GATE C3` matches `same as`, not `same <noun> as`, **so "same ingredients as
  Ozempic" passes today** — the exact string the FDA quoted in a warning letter. A step that names its
  own gate's hole.
- **B7** is the substance menu, and it is the FORK 6 shape already built: `B7.1` required,
  `B7.2`–`B7.5` a menu with a floor of 3, declines recorded as `{device, why}` in the plan file with a
  closed device vocabulary and a 20-character minimum reason, **and the floor computed as arithmetic
  on the declared set** rather than typed in prose.

### 1.8 Checklist C — the producer recipe (L888–L975)

14 steps, 1 gated (`C10`, `GATE test_v3_media_refs.py`). Fixed model id, an exact 10-hex palette
array, `model_type`, resolution, count, aspect mapping, a measured credit cost, a hands failure rate
("Three of eight heroes failed on hands"), a metadata-stripping recipe **with a note that the
documented command is not installed on this node and a Pillow equivalent**, and a ledger row rule.

This checklist is HYBRID-PLAYBOOK compressed into 88 lines. It is the proof that the two reference
playbooks are the **same genre at two scales**, not two genres.

### 1.9 Checklist D — the review protocol (L977–L1177)

14 passes, `D0`–`D13`, style first. It carries its own record schema at
`content-plan/reviews/<slug>.json` (filename is again the join key), a closed verdict vocabulary
`("PASS","FAIL","N/A")`, a closed severity vocabulary `("blocking","nit")`, and namespaced pass ids
(`CKD-<n>` for a Checklist D pass, `DISC-<n>` for a disclosure predicate) because "the playbook
carries six references that context alone cannot resolve".

Three rules here are template-grade and have nothing to do with content:

1. **`blocking` is defined POSITIVELY and severity is DERIVED, not declared.** Before that, "14 `FAIL`
   verdicts across the nine records, every single one labelled `nit`, none blocking anything."
2. **A PASS must stay reachable.** "A review that can never pass is as broken as one that can never
   fail, it just fails in a way that looks like rigour."
3. **`I33` — a pass that has never once failed is decoration.** It arms per pass at 9 substantive
   verdicts and reds when one has never discriminated. The escape is `DECORATIVE_OK`, "a diffable
   admission, not a default", checked in **both** directions.

**D13 is the cross-piece pass.** "This pass exists because every other pass in this checklist, and
every prose arm in the gate, reads exactly one article. Nine pieces were each reviewed carefully and
passed, and the nine together were a monoculture that no single review could have caught."

### 1.10 Checklist E — register (L1179–L1290)

10 steps, 9 gated. Closed vocabulary of 5 (+1 frozen legacy). Each register carries a
**machine-readable marker** (first-person share, direct-address percentage bands, question count), so
a voice rule is gate-readable. `I44` caps any one register's share of PUBLISHED rows — a corpus-level
gate over a per-piece declaration.

E's opening rule is the exemplar policy and it is the **opposite** of HYBRID's:

> **Every sentence quoted in this checklist is PROHIBITED OUTPUT, not a model.** … E6's example phrase
> reached 8 of 9 shipped bodies verbatim, E7's model refusal reached 5 of 9, and E8's three named
> props are an exact six-token match with `guided`'s prose. An exemplar in a checklist that nine
> writers read is a template, whatever the surrounding paragraph calls it.

---

## 2. `brand/art-style/HYBRID-PLAYBOOK.md` — section-by-section anatomy

12 sections. Zero tags. One dated acceptance stamp at the top. It points at two sibling files.

| § | Title | Job | In PLAYBOOK too? | Load-bearing? | Machine-checkable |
|---|---|---|---|---|---|
| head | What this makes / owner-accepted date / companions | identity, provenance, cross-refs | partly (L3, L18–20) | yes | dates & links yes, claim no |
| 1 | The recipe — a 6-row parameter table + a 2-row ground table | the **invariant call** | yes, as `C4`/`C5` | **yes** | yes: param values vs a call log |
| 2 | The prompt scaffold + four hard rules | **the slot template** + four owner corrections | no analogue | **yes** | scaffold shape yes, rules no |
| 3 | The Recraft reference (how to mint one) | how to regenerate an input the scaffold needs | no | yes | partly (a job id resolves) |
| 3b | Enriched palettes — 3 accent families | corpus-level variety lever | analogous to `I44` | yes | yes: hex sets are data |
| 4 | The scene prompt library — the accepted 8 | **accepted-instance library** | **forbidden** in PLAYBOOK | yes | yes: 8 rows, fields fixed |
| 5 | Adding a NEW scene without drift — 5 steps | the produce-one-piece checklist | = Checklist B | yes | steps 3 & 4 yes |
| 6 | Guardrails (binding) — 5 bullets | non-negotiables | = `## 0` + B3 | yes | 2 of 5 |
| 7 | Production finishing — 5 bullets | the output envelope | = B0.1 | yes | partly |
| 8 | What was ruled out (don't re-try) — 9 bullets | **negative knowledge, consolidated** | present but SCATTERED | **yes** | no |
| 9 | Higgsfield pipeline gotchas — 4 bullets | tool traps | = B7.6b, D0, C9 | yes | no |
| 10 | Recurring the DOCTOR character — 5 bullets | one hard sub-recipe + a measured failure mode | = C3, C6 | yes | element id yes |
| 11 | Model bake-off (run 2026-08-03 — don't redo it) | a **closed experiment**, 6 rows | no analogue | yes | no |

### 2.1 The slot-and-scaffold mechanism (§2), and whether it generalises

The scaffold is a fenced code block of ~11 lines of fixed prose with **two named fills** —
`<SCENE — who + candid action>` and `<SETTING — every object, ALL as paper>` — plus two unmarked
variables named in prose: "Vary only `<SCENE>`, `<SETTING>`, the emotion word, and the aspect. Keep
everything else verbatim — that's what makes the whole set read as one brand."

So the real contract is **4 fills, N invariant clauses, and an explicit keep-the-rest-verbatim rule**.
The sibling `PROMPTS.md §3` states the same mechanism one level more abstractly — a five-clause
scaffold where "Clause 2 (the scene) is the variable; clause 5 is optional" — and
`CONSISTENCY-GUIDE.md` names the contract outright: **"lock 3, vary 2"**.

**Does it generalise beyond images? Yes, and PLAYBOOK already contains two instances of it.**

1. **B3.17**, the standing not-medical-advice block: five sentences "still copied verbatim", zero
   fills, gated by `I22` on every published row. A scaffold with `n=0` fills.
2. **B0.1**, the entry JSON: 11 keys, fixed shape, every value a fill. A scaffold with `n=all` fills.

The generalisation is: **an INVARIANT REGION plus a closed set of NAMED FILLS, with the rule that
everything outside the fills is byte-verbatim.** That is medium-neutral. What does *not* generalise is
which failure mode bites you — see §2.2 — so the template carries the scaffold as an OPTIONAL slot
with an exemplar-policy declaration beside it.

### 2.2 The accepted-instance library (§4), and the contradiction it exposes

8 rows, three columns: scene name, `<SCENE>` fill, `<SETTING>` fill with an italic emotion register
appended and per-row exceptions in a tail (`(tail: no trees, no foliage)`, `(drop the plant/foliage
ban here)`). It is a **fill library**, not an output library. **Load-bearing** — §5 step 5 says
"curate the closest to the accepted set".

**This is where the two playbooks contradict each other outright**, and both positions are backed by
measurement:

| | HYBRID §4 | PLAYBOOK Checklist E preamble |
|---|---|---|
| rule | keep an accepted library, curate against it | every quoted sentence is PROHIBITED OUTPUT |
| evidence | scenes are curated by a human against the set; drift is the failure | E6's phrase reached **8 of 9** bodies verbatim; E7's refusal **5 of 9** |
| why it differs (INFERENCE) | an image library is a *comparand* a human eyeballs; a prose exemplar is a *seed* a model copies | — |

A single template cannot mandate either. It must carry an **exemplar policy** field with two legal
values and a stated reason. That is a genuine finding: it is invisible unless you read both files.

### 2.3 Failure-mode records with measured rates

Two in HYBRID, both in §10, and one is the only one in the file that names its sample:

> **HANDS — the one real failure mode. Measured over 8 heroes, 3 failed.**
> **SAFE — hands holding an OBJECT or flat on a SURFACE:** … All clean first try.
> **FAILS — (a) free or raised-and-spread hands** … **(b) FOLDED ARMS** — looks like a safe closed
> pose but is NOT …
> **Zoom to 100% on the hand region of EVERY frame before shipping** … The folded-arms failure was
> missed on a first pass done at too small a crop scale and had to be caught by the owner.

Its shape is the template's model: **rate · safe set · fail set · the near-miss that looks safe · the
inspection procedure · who caught it last time.** PLAYBOOK C6 restates the same fact in one line
("Three of eight heroes failed on hands") — see §3.10 on that duplication class.

§11's bake-off is the second shape: a **closed experiment**, 6 rows, dated, stamped `don't redo it`,
plus the judging criterion ("Judge on ART FIDELITY and LIKENESS, never resolution") and a
compatibility hard gate. This has no analogue in PLAYBOOK — its experiments live in
`memory/builds/*/build/research/`. **Both placements are defensible; the template must have a slot so
it is a decision rather than an omission.**

---

## 3. Adversarial: where these files break their own rules

Everything in this section was reproduced in this session.

### 3.1 LIVE — `PLAYBOOK.md` B0.1 names a collection that does not exist

B0.1 (L334) is the step that tells a writer where a piece physically goes:

> **B0.1. An article is one object in the `posts` collection's `entries` array**, in
> `package/nicocares-v3/content/collections.json`.

Measured:

```
$ python  # keys of collections.json
doctors  locations  products  journal  reviews  faqs

$ grep -n '_collection(' scripts/check_content_plan.py
2089:    posts = _collection(collections, "journal")
```

There is **no `posts` collection**. It was renamed on 2026-08-14 by `PKG-aCandidRookery-2`
("pharmacies->locations, posts->journal (key, route, label)"). The checker was updated; the playbook
was not. `posts` survives in 5 places (L334, L514, L810, L814, L1163).

**This is the single most damaging finding for FORK 2.** The declared output location is the machine
surface the refusal gate is meant to hang on. In the reference it is prose, the prose is wrong, and
the gate that reads the same file cannot see it because it reads the DATA and the writer reads the
PROSE.

### 3.2 LIVE — `D11` carries a stale line citation *and* the stale key

> Then bump the `posts` count in the literal at `tests/test_v3_seed_profile.py:184`; it is a source
> assertion and does not self-freeze.

Measured: line 184 is `counts[k] = (await db.execute(`. The literal is at **line 192**, and the key
there is `"journal": 9`. Both halves wrong. `scripts/check_citations.py` runs on this file and is
GREEN, because **arm A only catches citations past end-of-file** — and its own docstring says so
first, before anything else:

> **READ THIS BEFORE TRUSTING IT** — the honest limit, stated first rather than buried. **Arm A cannot
> catch any of the three drifts that motivated it.** All three were IN-BOUNDS…

That header is the template's model for "a gate's own header states what it does NOT check". The
defect it cannot catch is nonetheless sitting in the playbook right now.

### 3.3 LIVE, PROVEN — `I21`'s step-id regex mangles a letter-suffixed step

The checker's regex (`check_content_plan.py:2422`) is `^\*\*([A-Z]\d+(?:\.\d+)?)\.` It backtracks
past a letter suffix:

```
I21 step_re sees: 110      true headings: 110
INVISIBLE to I21: ['B5.3a', 'B7.6b']
```

Both are matched, but captured as `B5` and `B7`. Staged and observed — a second suffixed step under
the same stem:

```
$ (added "**B7.6c. …** `CHECK` …")
FAIL I21: playbook step id(s) ['B7'] appear more than once — a duplicate id merges two passes into
one wherever a record joins on it
```

The author is told `B7` is duplicated. **`B7` appears nowhere in the document.** This is recorded as
`PKG-bLimpidQuill-3` — "Reworded around it rather than changing the regex mid-unit" — and that record
cites `scripts/check_content_plan.py:1607`, while `step_re` is at line **2422**. A record about a
citation-shaped defect carries a stale citation.

### 3.4 LIVE, PROVEN — a line-WRAPPED `GATE` tag escapes the invariant-existence check

`I21`'s existence cross-check is `re.findall(r"GATE([^\n]{0,90})", "\n".join(pb))` — **per line**. The
untagged-step arm joins lines and is safe; this arm is not. Staged, with a same-line control:

```
# wrapped:   **B8.1. …** `GATE\ncheck_content_plan.py I999` staged.
content-plan GREEN (52 rows, 9 entries, 46 link edges, 0 advisory warn(s))

# same line: **B8.1. …** `GATE check_content_plan.py I999` staged.
FAIL I21: playbook GATE tag(s) name ['I999'], which this script never emits
```

**A tag naming an invariant that does not exist passes GREEN if the leg name wraps.** And the live
file already contains **4 wrapped tags** — `I23`, `I35`, `I40`, `I44`. The shape is not hypothetical;
it is in production and in current use. Two of the four (`I40`, `I44`) are therefore invariants the
playbook cites that the gate has never validated.

### 3.5 LIVE — `CHECK <why>` is not enforced, and 71 of 95 tags are not in the reason form

The checker's whole test is `has_check = "CHECK" in window`. Derived:

```
`CHECK` occurrences: 95   reason-joined form (`CHECK` — …): 24   other form: 71
```

Examples of the bare form, each a real step: B3.14 `CHECK Named red flags plus an explicit emergency
instruction.` · B3.16 `CHECK` with nothing after it · B4.1 `CHECK` — "a person with obesity", never
"an obese person". The *statement* is there; the **reason no gate can see it** usually is not.

**FORK 5 says "every step is tagged `GATE <leg>` or `CHECK <why>`". The reference implementation
enforces the tag and not the why.** If the kit's gate enforces the `<why>`, it will red 71 of 95 tags
in the very file it was derived from. That is a real design decision with a real migration cost, and
it must be taken deliberately.

### 3.6 LIVE — a bare `GATE C2` names a leg the document never locates, and `LEG_RE` accepts a vibe

Derived: **52 of the 90 GATE tags name a bare id only** (`GATE I13`, `GATE C2`, `GATE C6/C8`), with
the leg implied. The `I*` legs' home is stated at L9. The `C*` legs' home is
**`tests/test_v3_claims.py`**, which is named exactly once in 1290 lines (L600), in a parenthetical
about `I22`, never as the home of `C1`–`C8`. A reader hitting `GATE C2` at B3.1 cannot learn from this
document where C2 lives or how to run it.

And the predicate that decides "this tag names a leg" is a SHAPE:

```python
LEG_RE = re.compile(
    r"\b(?:I\d+|C\d+[a-z]?|check_[a-z_]+\.py|check-[a-z-]+\.sh|test_v3_[a-z_]+\.py"
    r"|html_override\.py|core's)\b")
```

`core's` is in the allowlist. `GATE core's sanitizer` satisfies "names a leg". Only the `I\d+` branch
is cross-checked against a real emitter set. **FORK 5's "every named leg is runnable" is, in the
reference, "every named leg is spelled like something".**

Measured leg wiring:

```
1  check_content_plan.py    <- ci.yml leg
1  check_package_refs.py    <- ci.yml leg
1  check-package-budgets.sh <- ci.yml leg
0  prose_metrics.py         <- library, exercised via check_content_plan's selftest
0  test_v3_lexicon.py       <- NOT an nc CI leg
0  test_v3_media_refs.py    <- NOT an nc CI leg
0  test_v3_seed_parity.py   <- NOT an nc CI leg
```

`ci.yml`'s own header: *"The BRAND TEST SUITE (tests/) imports the inCMS core and runs in inCMS core
CI via the submodule — NOT here."* So 4 of the 7 named legs are not on this repo's merge bar, 3 of
them are enforced in **another repository's** CI, and nothing local asserts they still exist or still
carry the arm the tag claims. B3.10, B3.11 and E8 read as merge-bar enforcement and are cross-repo
promises.

### 3.7 LIVE — counts of derived populations, written in prose

| Where | Claim | Measured now | Verdict |
|---|---|---|---|
| B7.9 (L818) | "Five nc descriptors already do this" (`scope:"entry"` binding `entry.data.*`) | **12** | STALE ×2.4 |
| C9 (L946) | "what the 63 shipped assets already are" | **66** `.webp` in `content/media/` | STALE by 3 |
| C1 (L902) | "29 shipped, owner-accepted assets are referenced nowhere, about 17.4 MB" | **29** stems, **16.3 MB** | count right, bytes off |
| B7.9 (L814) | `faq` "mounted on 14 pages" | **14** page files carry it | correct today |
| A2 (L61) | "REQUIRED_FIELDS is 23" | 23 | correct, **and gated by I21** |

The one that is right and stays right is the one with a gate behind it. Nothing gates the other four.
This is the charter rule "NO count of a derived population is written in prose" failing in the file
the owner named as the reference — four times, in a file that runs a 2,861-line checker on itself.

### 3.8 LIVE — cross-file claim rot between the two playbooks

`HYBRID-PLAYBOOK.md` §6:

> **Attestation:** net-new AI art needs a compliance attestation row before it ships (§9 of the
> package `CLAUDE.md`); **the ledger was retired 2026-07-07, so its home is an open item.**

Measured: `brand/attestations/ART-LEDGER.md` **exists**, 7,105 bytes, and its own header says

> Rehomed 2026-08-12 by `BRAND-bInkedFoolscap-1` (owner fork F3). The previous ledger lived at
> `brand-sources/illustration/ART-MANIFEST.md` and was retired 2026-07-07 at `e7d675a`.

And `PLAYBOOK.md` C13 names the live file: *"Fill only `Asset key`, `Style role`, `Slot` and
`Model + recipe` in `brand/attestations/ART-LEDGER.md`."* **Two playbooks in one repo disagree about
whether an artefact exists.** HYBRID's mtime is 2026-08-08; the rehoming is 2026-08-12. Nothing gates
it, because nothing gates HYBRID at all.

### 3.9 LIVE — a documented CHECK that is documented and not performed

PLAYBOOK C13: *"No asset ships on an unsigned row."* Measured:

```
$ grep -n "^|" brand/attestations/ART-LEDGER.md
68: | Asset key | Style role | Slot | Model + recipe | Commercial-use | Compliance verdict | Reviewer | Date | Checklist version | Weight measured | Alt |
69: |---|---|---|---|---|---|---|---|---|---|---|
70: | `doc-1` | … | | | | | | |
71-73: three hero rows, same trailing empty columns
```

**4 data rows for 66 shipped assets, and every one of the 4 has its 7 signature columns empty.** The
ledger's own header: *"An asset without a complete row here is not untidy; it is unprovable."* The
rule is stated twice, in two files, and discharged zero times.

### 3.10 The three-copy palette, and the duplicated failure rate

```
brand/art-style/PROMPTS.md          4 array literals (owns them)
brand/art-style/HYBRID-PLAYBOOK.md  1 literal (collage lock)
content-plan/PLAYBOOK.md            1 literal (ink-wash lock)
```

The two copies are **currently byte-identical** to their PROMPTS.md originals — verified. Nothing
gates the pair. Same class: the hands failure rate is stated in HYBRID §10 ("Measured over 8 heroes,
3 failed") and again in PLAYBOOK C6 ("Three of eight heroes failed on hands"). Two copies of one
measurement in two mutable files. Caught before rotting, but this is the second-copy class the
charter says to gate or point at.

### 3.11 The one probe in the corpus that cannot move — and it announces itself

The checker's census prints `i29 hits A=0/0 B=0/0 allowlist=0/0`, and P3 names the reason in the
playbook:

> `I29` Family A is a literal alternation over the four sentences one drafting review happened to
> find… Four invented form-shape facts shipped past it… with the census printing `i29 hits A=0/0`.
> **A pin measured by a predicate that cannot reach the population is a measurement of the predicate.**

The denominator `0/0` is the liveness assertion: population zero, hits zero. That is the honest
rendering the charter asks for, and it works. **Steal the `hits/population` census idiom outright.**

---

## 4. Where HISTORY lives, and how much of it there is

Derived over blank-line-separated blocks with a fixed marker set (`used to
(say|read|call|carry|ban|claim)`, `said the opposite`, `superseded`, `had been false`, `was wrong`,
`until 2026-`, ``until `PKG-``, `is **deleted**`, `no longer`, `ruled out`, `don't re-try`, `reverted`,
`thrown away`, `rejected on evidence`, `was an unenforced`, `earlier (draft|reading)`):

```
content-plan/PLAYBOOK.md            : 264 blocks, 24 self-correction / negative-knowledge blocks
brand/art-style/HYBRID-PLAYBOOK.md  :  50 blocks,  4 self-correction / negative-knowledge blocks
```

Additional derived counts on PLAYBOOK.md: `owner ruling` ×4 · ISO dates ×30 (11 distinct) ·
`used to` ×7 · `superseded` ×1 · `is **deleted**` ×2 · `PKG-*` ids ×26 (13 distinct) · `measured` ×11
· `verif*` ×6 · `prohibited output` ×2 · 19 distinct N-of-M claims.

### 4.1 The five history SHAPES, both files

1. **A correction of this file's own prior text, in place** — 24 instances in PLAYBOOK. Canonical form
   at L14: *"This paragraph said the opposite from 2026-08-12 until 2026-08-14, and a spec that trusted
   it sized four new invariants as local advisories. Corrected by `PKG-aCandidCadence-1` S12."*
   Cause · window · consequence · id.
2. **A dated owner ruling that overturns a prior rule** — 4 in PLAYBOOK, 11 date-stamped owner
   corrections in HYBRID. PLAYBOOK A4: *"The flat 2,000-word floor is superseded (owner ruling
   2026-08-14)."*
3. **A deleted field, with its epitaph** — 2 in PLAYBOOK. `must_cover` (A11): *"It was byte-identical
   on 52 of 52 rows … so for a year the corpus carried a coverage contract that recorded nothing."*
4. **A consolidated don't-re-try list** — HYBRID §8, 9 bullets, each `<thing tried>: <why it lost>
   (owner <date>)`; plus §11's closed bake-off. PLAYBOOK has **no such section**; its equivalents are
   scattered across 24 inline blocks.
5. **A measured composition failure — rules nobody defected from, producing a shape nobody chose.**
   Four instances in PLAYBOOK, and this is the class no other document type carries:
   - B1.4: the 20-word cap → mean 10.9/11.3/11.3, stdev 4.1/4.0/4.5, longest exactly 21 in all three.
   - B7.5: takeaways "near the top" + E5 early pivot + E6 fence declaration → **6 of 9 independently
     recorded `shape: "hourglass"`**. *"An article obeying all three IS an hourglass, and no rule in
     this file opposed it."*
   - E6/E7: the exemplar sentences → 8 of 9 and 5 of 9 verbatim.
   - B7: the device menu as a requirement → *"a takeaways-first `<h2>` in 9 of 9 bodies, exactly five
     takeaway bullets in 9 of 9, one comparison table in 9 of 9, an appointment block in 9 of 9."*

**Shape 5 is the reason the template needs both a NEGATIVE-KNOWLEDGE slot and a CORPUS-RULES slot.**
Every one of those four was found by measuring the SET, and none was visible from any single piece.

### 4.2 Both files carry a negative-knowledge section, and they place it differently

| | PLAYBOOK | HYBRID |
|---|---|---|
| placement | inline, beside the rule it corrects | consolidated, §8 + §11 |
| count | 24 blocks | 9 bullets + 6 bake-off rows + 4 gotchas |
| finding rate on read | high — you cannot read the rule without the correction | low — you must go look |
| rot risk | a correction and its rule move together | §8 rotted (§3.8: the ledger claim) |

**Recommendation, derived rather than aesthetic:** the template REQUIRES both. Inline for a correction
of a rule that is still present, so the two cannot separate. A consolidated "ruled out — do not
re-try" region for a thing that has no rule left to sit beside — HYBRID's §8 exists precisely because
a rejected approach has no surviving rule to attach to.

---

## 5. Deriving the template

### 5.1 The REQUIRED sections, and what fills each

For every section: which parts of which playbook fill it, and whether a machine can check it.

| # | Section | Filled by PLAYBOOK | Filled by HYBRID | Machine-checkable |
|---|---|---|---|---|
| **R1** | **Identity** — what this playbook produces, one paragraph, second person | L3 | head, "What this makes" | presence only |
| **R2** | **Provenance** — id, date, owner acceptance, evidence links; **a per-section stamp when a section post-dates the head** | L18–20 + Checklist E's own stamp | head, "Owner-accepted 2026-07-21 (session `aWovenPortrait`)" | dates and link resolution: yes |
| **R3** | **Tag contract** — the GATE/CHECK rule stated by the playbook about itself, naming its enforcing leg | L5–7 + `GATE I21` | **ABSENT — must be authored** | yes: this is the validity gate |
| **R4** | **Declared output envelope** — the exact paths a piece may be written to, plus the shape of one piece | B0.1 (JSON, 11 keys) + `/journal/<slug>` | §7 + §1's slot/aspect table | **yes — FORK 2's whole surface** |
| **R5** | **The invariant call** — the fixed parameters or inputs a piece is produced with | C4/C5 (model, palette, `model_type`, resolution, count, aspect) | §1's 6-row table + §3's plate recipe | yes, as data |
| **R6** | **Non-negotiables** — binding rules that are not steps | `## 0` + B3's 18 compliance steps | §6 "Guardrails (binding)" + §2's 4 hard rules | partly |
| **R7** | **The step checklist** — ids, a declared ID grammar, every step tagged | A/P/B/C/D/E, 110 steps | §2 rules 1–4, §5 steps 1–5, §7, §9, §10 bullets | yes, via R3's gate |
| **R8** | **Declared legs** — every leg named by a GATE, with its invocation and where it runs | D12's ordered run + the `I*` home paragraph | **ABSENT** — honest fill is `gates: none — owner acceptance is the sole criterion` | yes: resolve each to an invocation |
| **R9** | **Corpus rules** — what is true of the SET of N pieces, distinct from any one piece | A4/D5/`I24` corpus mean · `I44` register share · `I38`/`I40`/`I41` convergence · D13 the second piece · `I17` hero uniqueness | rule 4 "carry the body-type range across the whole LIBRARY, not inside every frame" · §3b vary the accent family per image | **yes, and only over the set** |
| **R10** | **Negative knowledge** — inline corrections plus a consolidated ruled-out region | 24 inline blocks | §8 (9 bullets) + §11 | no |
| **R11** | **Failure modes with measured rates** — rate · safe set · fail set · the near-miss that looks safe · the inspection step | C6 (one line) | §10 hands (the full shape) + §9 gotchas | no |
| **R12** | **Exemplar policy** — `library` or `prohibited`, with the reason | Checklist E preamble: **prohibited** | §4: **library** | yes: a closed enum |

Twelve required sections. Both playbooks fill ten of them without distortion. **R3 and R8 are empty in
HYBRID**, and R8's honest fill is a declared null with a reason — which is exactly the "a skip
announces itself" rule applied to a whole playbook.

### 5.2 The OPTIONAL sections

| # | Section | PLAYBOOK | HYBRID |
|---|---|---|---|
| O1 | **Slot scaffold** — invariant region + named fills + keep-the-rest-verbatim | B3.17 (0 fills), B0.1 (all fills) | §2 (4 fills) — the canonical instance |
| O2 | **Accepted-instance library** | forbidden by R12=prohibited | §4, 8 rows |
| O3 | **Per-piece plan artefact + its schema** | Checklist P + `plans/<slug>.json`, 4 closed key sets | §7's provenance bullet |
| O4 | **Review protocol + record schema** | Checklist D, 14 passes, `reviews/<slug>.json` | one line: owner acceptance |
| O5 | **Tool/pipeline gotchas** | B7.6b, C9 (`cwebp` absent), D0 (half-rendering harness) | §9, 4 bullets |
| O6 | **Closed experiments — don't redo** | none (they live in `memory/builds/*/research/`) | §11 bake-off |
| O7 | **Register / voice** | Checklist E, 5 closed values with gate-readable markers | rule 3's 8-value emotion register + a per-scene assignment |
| O8 | **Product context** | `## 0` | in `README.md`/`CONSISTENCY-GUIDE.md`, not the playbook |
| O9 | **Companions** — sibling files this playbook depends on | implicit (`PROMPTS.md` at C0) | head + §3, explicit |

O9 is optional and **is the field that rotted** (§3.8). If the template carries it, the gate should
resolve every companion path — that is free, and it would have caught the ledger claim.

### 5.3 What does NOT fit, and would be lost or forced

Named explicitly, because a template that pretends these fit is worse than one that declares them out.

1. **The exemplar contradiction (§2.2).** Not a gap — a genuine fork, decided per playbook. Forcing
   either value destroys one of the two reference files. Handled by R12 and only by R12.
2. **PLAYBOOK's `## 0` brand/product context.** Forcing it on an art playbook makes it restate the
   brand book. Optional (O8) with a point-at-the-owner form.
3. **Checklist D's 14-pass review protocol with a per-piece record schema and a decorative-pass
   meta-gate.** Ceremony on a 245-line recipe. Optional (O4), with a declared null.
4. **HYBRID's §11 closed experiment.** PLAYBOOK's equivalent lives outside the playbook, in
   `memory/builds/`. Both defensible; the template makes it a decision (O6), not an omission.
5. **B3's 18 compliance steps.** Domain law, not playbook structure. They fill R6 and nothing else,
   and giving them their own section would import one project's regulator into the template.
6. **HYBRID's §9 producer gotchas (async polling, an 8-job concurrency cap, model ids that silently
   coerce).** Under FORK 7 these are playbook prose and stay there (O5). Correct — but note that the
   *checker* is not agnostic: PLAYBOOK's `C10` gate is `test_v3_media_refs.py`, a producer-specific
   leg. **The KIT stays agnostic; the adopting repo's checker does not, and FORK 5 already puts that
   checker in the adopting repo. Consistent — worth saying out loud in the spec.**
7. **Checklist A's corpus PLAN — 13 gated steps that plan the set before any piece exists.** The
   largest structural element in either file with **no home in the seven forks**. It fits R9 only
   partially: R9 is *rules over the set*, Checklist A is *a data file enumerating the set*. See §6.3.

---

## 6. Findings against the seven settled forks

Not re-litigating. Reporting what this lens measured.

### 6.1 FORK 5 — "a playbook is VALID only if every step is tagged and every named leg is runnable"

**Four measured problems with the reference implementation of exactly this rule.**

- The `<why>` half is unenforced; **71 of 95** CHECK tags are not in the reason-joined form (§3.5).
- "Names a leg" is a SHAPE test, `core's` included; only `I\d+` is cross-checked against real emitters
  (§3.6).
- A **line-wrapped** tag naming a nonexistent invariant passes GREEN, proven, and 4 wrapped tags are
  live in the file today (§3.4).
- A letter-suffixed step id mangles and reds with an id that does not exist (§3.3).

**And HYBRID-PLAYBOOK carries zero tags.** Under FORK 5 as written it is INVALID. The owner named it
as evidence, so the rule needs an explicit whole-playbook escape: a declared `gates: none — <why>` at
R8, which makes every step CHECK by construction and keeps the validity claim honest. **Report loudly:
without that escape, one of the two reference playbooks cannot be expressed in the template it was
used to derive.**

Concrete mitigations, all derived from the measured failures:

- Parse the playbook **structurally**, never with a line-anchored regex over markdown. The wrapped-tag
  hole and the id-mangle are both line-regex artefacts.
- Resolve each declared leg to an **invocation** — a command string in R8 the checker actually runs, or
  an explicit out-of-repo declaration naming the CI that runs it — never to a filename shaped like one.
- Enforce the `<why>` with a minimum length, as `I35` already does for `declined[].why` (20 chars) and
  `source_says` (40 chars). Precedent exists in the same file.
- Ship the validity gate with an **observed-failing-case harness**. `plans_gate_selftest.py` is the
  model and its docstring names the trap: *"It asserts on the MESSAGE, not on the exit code … An
  implementer watching for exit 1 would have observed a RED, ticked the acceptance criterion, and
  landed an arm that had never fired."*

### 6.2 FORK 2 — gate the declared OUTPUT PATHS

**Strongly supported, with one correction.** The reference declares its output location in **prose**
(B0.1) and the prose is **wrong** (§3.1) — it has named a nonexistent collection across five
occurrences, while a 2,861-line checker read the correct one on every run.

So: the output-path set must be a **machine-readable field the gate reads**, and if the playbook's
prose also states it, the two must be gated as a pair — the `REQUIRED_FIELDS is 23` idiom, which is
the one prose number in the file that has not rotted.

The class the gate cannot see is not only "a code change inside a declared output path". A second,
measured class: **the declared path itself going stale.** A declared path that resolves to nothing
should red; that is free and it is the only defence against B0.1's failure mode.

### 6.3 FORK 3 — the playbook is the spec; pieces are passes

**Supported, and incomplete.** Both reference playbooks carry rules that are *only* checkable over the
set, and a DoD that counts pieces against N cannot see any of them:

| Corpus rule | Where | What it catches that no per-piece check can |
|---|---|---|
| `I24` corpus word-count MEAN ≥ 2000 | A4, D5 | a corpus drifting short with no per-article culprit |
| `I44` register share ceiling over published rows | E2 | 5 registers shipping one voice — 9 of 9 `wry` |
| `I40` byte-level span convergence across bodies | D13 preamble | the same sentence in >2 of 9 pieces |
| `I41` heading convergence | same | 9 pieces with the same furniture |
| `I17` hero uniqueness across entries | B5.6 | two pieces sharing an asset |
| `I49` contiguous `publish_seq` | B5.3a | an ambiguous "previous piece" for the cross-piece pass |
| D13 the second piece, read back-to-back by a fresh reader | Checklist D | a repeated *move* no byte gate sees |
| HYBRID rule 4 "carry the range across the whole LIBRARY" | §2 | a set diverse per frame and uniform across frames |
| HYBRID §3b "vary the accent family per image" | §3b | a set that reads as one image N times |

**Every one of the four composition failures in §4.1 was found by measuring the set.** A DoD that
counts pieces and declares each piece's legs green will ship N monocultured pieces and report GREEN.
The playbook must be able to declare **set-scoped legs** that run once, after the last pass, and the
DoD must require them. That is an addition to FORK 3, not a contradiction of it.

Second point: Checklist A is a **data file enumerating the set** (`plan.json`, 52 rows, 23 required
fields, a closed 8-value status vocabulary, a runway floor). Under FORK 3, N and the destinations come
from the owner's ask at run start. For N=3 that is fine. For the reference's N=52-over-six-months it
is not, and the reference solved it with a committed, gated plan file. **INFERENCE:** the template
should carry an OPTIONAL R4 sub-form — the output envelope may be *a declared path set* (small N) or
*a committed manifest file with its own schema* (large N) — rather than assuming the first.

### 6.4 FORK 6 — a proposal register distinct from `--park`

**Supported, and the reference shows the failure mode of not having one.** Three of the 13 `PKG-*` ids
cited in the playbook are improvement proposals raised at another repo and **left inline in the
playbook prose**: `PKG-bInkedFoolscap-6` (nofollow), `-7` (`@media:` in richtext), `-8` (no admin
editor for array-of-objects fields). Each reads as a rule while being a wish. A separate register is
right; the reference's answer was `core-asks.md` plus prose, and the prose half is the part that rots.

The shape to steal is `declined`: a **closed target vocabulary, a minimum-length reason, and floor
arithmetic derived from the declared set** rather than a number typed in prose. A proposal register
with `{target, why}` and a minimum `why` length is one `I35` away.

### 6.5 FORK 4 — corpus-derived plus external research

**Caveat worth recording: the corpus is N=2, one repository, one author culture.** Both files were
written by agents under one charter, and they already contradict each other on the single question a
template most needs answered (exemplars, §2.2) and on a matter of fact (§3.8). Deriving a template
from them and freezing it is right; presenting the derivation as *corpus* evidence rather than *two
worked examples* would overstate it. The external half of FORK 4 is doing more work than it looks.

### 6.6 FORK 7 — the kit stays agnostic

**Supported, with one clarification the spec should state.** HYBRID §1/§9/§10/§11 and PLAYBOOK's
Checklist C are 100% producer knowledge and belong in playbook prose. But PLAYBOOK's `C10` gate is
`test_v3_media_refs.py` — a producer-specific leg named by a GATE tag. The KIT is agnostic; the
CHECKER the adopting repo owns (FORK 5) is not, and must not be. Say it, so nobody later reads
"agnostic" as "the validity gate may not know about producers".

### 6.7 FORK 1 — two entry points, one artefact, one gate

**No evidence against.** Nothing in either reference playbook depends on how a run was authorized.
`PLAYBOOK.md` is executed by attended sessions today and its gate is authorization-blind.

---

## 7. Mechanisms worth copying verbatim into the template's gate

Each is in production in `check_content_plan.py` and each answers a house rule directly.

1. **A census of derived figures on every run** — ~35 lines, every number computed, none typed. Answers
   "NO count of a derived population is written in prose". The playbook-tag row is literally
   `playbook steps 110 (110 tagged, 0 untagged)`.
2. **`hits/population` as the liveness idiom** — `i29 hits A=0/0` says "the predicate reached nobody"
   in the same glyphs a clean run uses to say "nobody offended". Answers "a probe that cannot move
   says so".
3. **Self-announcing SKIP lines** — `SKIP I27 clause fixture:…: paragraph-shape clause not applied — 8
   paragraph(s), needs 10 for the percentage to mean anything`. Names the arm, the subject and the
   reason. Answers "a skip must announce itself".
4. **Two-directional shrink-only pins** — every exemption set reds when it GROWS *and* when it fails to
   shrink after the commit that should have drained it. `PLANS_BACKFILL_EXEMPT`, `PLACEHOLDER_PIN`,
   `PLAIN_LEGACY`.
5. **Debt as an allowlist of PAIRS, never a count** — from the source comment: *"A count has REPLACE
   semantics: at a pin of 7, fixing all seven and introducing seven new ones reads GREEN."*
6. **A predicate selftest table with BOTH directions inline** — 42 cases, each `(regex, string,
   expected)`, including the deliberately-narrow negatives. Answers "a gate whose failing case has
   never been observed is an assertion about nothing" for regex arms.
7. **A separate observed-failing-case harness that asserts on the MESSAGE** — `plans_gate_selftest.py`,
   `claims_gate_selftest.py`.
8. **A gate header that states its limits first** — `check_citations.py`'s "READ THIS BEFORE TRUSTING
   IT … Arm A cannot catch any of the three drifts that motivated it."
9. **A meta-gate on decoration** — `I33`: a pass that has never once failed reds, with a diffable
   `DECORATIVE_OK` admission checked in both directions.
10. **The filename IS the join key** — `plans/<slug>.json`, `reviews/<slug>.json`, and a file whose
    declared `slug` disagrees with its filename FAILS ("a copied file would otherwise discharge the
    wrong article").
11. **A floor arm on the parser itself** — `if steps < 50: fail("I20", "…the step regex has stopped
    matching and I21 is selecting almost nothing")`. A gate that notices when it has gone inert.
12. **`[A-Z]` and not `[A-D]`** — the checker's own comment: at `[A-D]` every Checklist E step was
    structurally invisible while the arm reported an unchanged "86 (86 tagged, 0 untagged)". **Gate the
    class, not today's instance.**

---

## 8. Open questions this lens could not close

- **Does the validity gate live in the kit or in the adopting repo?** FORK 5 says the adopting repo
  owns a checker. But R3's tag contract, R7's ID grammar and R8's leg-resolution are playbook-shape
  checks, not domain checks, and every one of the four §3 defects is a playbook-shape defect.
  INFERENCE: the shape half belongs in the kit and the leg half in the adopter. Not settled here.
- **Set-scoped legs need a phase.** They run after the last pass and before close. Whether that is a
  new phase, a DoD item, or a `--close`-time leg is a driver question outside this lens.
- **How is a playbook's own edit history bound to its pieces?** PLAYBOOK carries 24 inline corrections
  with `PKG-*` ids; the kit's playbooks will carry proposal-register ids. Whether a piece records which
  playbook REVISION produced it is unaddressed by any of the seven forks, and §4.1's shape-5 failures
  are only diagnosable if it does.
- **The "44 defects" and "17.4 MB" class.** A figure that was true when written, in a file that is not
  append-only. `check_citations.py` excludes `memory/builds/` for exactly that reason. A playbook is
  mutable, so it has no such excuse — but no discriminator separates historical from present-tense
  prose, and that gate's own calibration REJECTED trying (best variant precision 0.65).
