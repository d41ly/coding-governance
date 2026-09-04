# What the spec format is missing, and what it costs — the findings

**Serves:** none — the findings half of a research build that precedes any spec. Its measurement
sibling is `2026-09-04-build-TOOL-aWeighedCanon-1-spec-format-measurements.md`. Nothing here is a
decision; anything acted on becomes its own unit in its own build.

Method: five disjoint evidence lenses over the corpus, then an adversarial verify pass prompted to
REFUTE. 34 findings raised, **29 confirmed, 5 refuted — precision 0.85**, against the charter's
0.5 retune threshold. Ten agents, 1.64M tokens, 422 tool calls, 23.5 minutes wall.

**Every confirmed finding below is quoted in its POST-SKEPTIC form.** Twenty-six of the 29 came
back narrowed, and several had their headline numbers corrected downward by the skeptic that
checked them. Where a first-pass number appears anywhere in this repo's chat history and disagrees
with a number here, this record is the one that was checked.

---

## The short answer

The format is a **shape contract**. Check 12 grades whether the ten sections are present, ordered,
non-empty, and free of skeleton placeholders. That is enforced well and it is not nothing — it is
why 436 of 479 specs carry a parseable, navigable structure.

But three things are true at once, and together they answer the owner's question.

**1. The gate is heaviest where specs least often fail.** Of 1,503 section references across the 52
spec-audit reviews, §2 Scope draws 315 and §4 Design draws 375 — 45.9% of all references — and both
receive only two assertions from check 12: heading in canonical order, and body not empty. Nothing
grades their content. Meanwhile §9 and §8, whose predicates are the most precisely specified in the
whole check, draw 21 and 40 references respectively. Forty-five of the 52 audits returned BLOCKED.

*Correction carried from the skeptic:* §6 Acceptance (268 references) is NOT in the ungraded set —
the acceptance-witness arm at `check-memory-hygiene.sh:1020-1048` grades it across 372 of 479 specs.
The original finding claimed 63.7% and three sections; what survives is 45.9% and two.

**2. The format specifies documents, not relationships.** This is the single largest missing thing
and it accounts for nine of the 29 confirmed findings. Detailed below.

**3. The revision loop — which 88% of specs enter — is the corpus's dominant defect source, and the
template's entire instruction for it is one clause.** Also detailed below.

What the format is NOT is expensive ceremony. That hypothesis was tested directly and refuted; see
"What the format does well".

---

## Theme A — the format numbers things for citation and then joins nothing

The template numbers §2 items `S1, S2…` and §6 items `AC1, AC2…` explicitly "so reviews and build
summaries can cite them stably." It then never asks anything to be joined to anything. Every section
is an island, and the seams between islands are where builds break.

### A1 · Scope items are never joined to the criteria that observe them — HIGH

Over the 460 specs carrying both numbered lists, **only 408 of 3,061 S ids (13.3%) are named
anywhere in their own §6, and 260 specs (56.5%) name none at all.** The template joins §6 forward to
the acceptance ledger but never joins §2 to §6; the closest it comes is a passive assertion that
scope items are "verifiable at DoD".

The citation rate measures habit, not coverage. The evidence that scope items genuinely go
unobserved is the review corpus: **16 distinct builds confirm the class.** In `dRetiredFork` round 1
it is the set's dominant failure with five rows, one of them a BLOCKER on that build's own named
highest-risk mitigation.

Not covered by `TOOL-aBoundedVerdict-32`, `TOOL-dTieredTribunal-24`, or anything else in the backlogs.

### A2 · The spec-to-ledger join is by label only, and it is provably wrong on a green unit — HIGH

Check 23 iterates the SPEC's labels and looks each up in a ledger map
(`check-memory-hygiene.sh:1509-1516`). It never walks the ledger's labels, and it compares no
content. So a ledger line keyed to a label the spec never wrote is invisible, and a line keyed to
`AC4` that answers `AC5`'s question passes.

`DEPL-dRetiredFork-3` is the worked case, and it is **CLOSED and green**. Spec `AC3` asks what
happens when a render produces an EMPTY artifact; ledger `AC3` answers about non-zero exit routing
through `classify_outcome`. Four of twelve labels answer a different criterion, and the ledger
invents a thirteenth the spec never wrote.

This is `TOOL-aBoundedVerdict-32` approached from the opposite side. That row says nothing gates a
criterion against the TREE; this says nothing gates a ledger answer against its own CRITERION —
a join that needs no tree access at all.

A weaker sibling, separately confirmed: **307 of 1,377 ledger answers (22.3%) cite no backticked
token their criterion named**, and nothing compares the two sets.

### A3 · No section asks what would make a criterion FAIL — HIGH

The charter binds every new gate to an observed failing case, and every signal to a liveness
assertion. `BUILD-METHOD` M3 demands a liveness assertion of a `FACT-QUESTION` probe. **The spec
format never asks a criterion to name the break that turns it red.**

Builders answer it anyway, out of band: **93 of 479 specs mention a staged break or a red-first run**
with no section asking for one, clustering in §6 (79 lines) and §5 (30) — authors putting the answer
where the template has no question. Eleven build records exist whose entire subject is that witness.
`TEMPLATE-SPEC.md` contains none of those strings.

Where nobody answered it, criteria that could not fail reached close.

### A4 · Nothing declares what a unit owes or receives from its siblings — MEDIUM

**450 of 479 specs (94%) sit in multi-spec build folders.** The multi-spec case is the norm, not the
exception. The template's only cross-unit field is the PERMITTED `order <n>`, carried by 159 of 479
specs — and `order` expresses sequence, never an edge.

Nothing asks a unit to name what it consumes from or hands off to a sibling. The confirmed
cross-unit defects are edge failures, not ordering failures: `dRetiredFork` H4 hands 39 sites to a
unit whose declared population excludes the carrying file.

Related and separately confirmed (MEDIUM): **no section asks what a unit's acceptance depends on
that the unit does not build**, so a sibling's scope cut or a landing on `main` silently invalidates
criteria. Seven amendments of that shape were confirmed, four of them in one spec.

### A5 · Three more unasked questions, each paid for in amendments — MEDIUM

Of **81 acceptance criteria amended at build time** across 32 records (5.5% of 1,404 AC lines):

- **23 were amended over cost or permission.** §6 asks for the observation and never its price or
  its permission to run. `grep -ciE 'cost|budget|minutes|hours'` over `TEMPLATE-SPEC.md` returns
  **0** — the silence is total. This is the largest binnable amendment class, though 33 of the 81
  resist binning, so "largest cause" is proven only among classes that bin.
- **8 pinned a measured literal that was stale by build time.** The writing rules say verify at
  WRITING time and never ask whether a figure is derived.
- **6 named a live instance or fixture the tree did not contain.**

And separately (MEDIUM): **§7 never asks where a new gate's ARM lives** — which test file gains it,
which helper it uses, whether its suite is one this run may execute. At least four criteria were
amended because the arm landed elsewhere than the spec said; in one case the misplacement surfaced
only at the closing review, after the change had silently dropped 42 of 85 legs from every profile.

---

## Theme B — the revision loop is unmanaged, and it is the dominant defect source

### B1 · Folds create the majority of the next round's defects — HIGH

**Five builds independently measured this across nine round-level measurements, and every one found
the fold created the majority of the next round's confirmed findings:** 65–72% (`dBriefedPass`),
69% twice (`dTieredTribunal-1`), 88.9% wide / 61.1% narrow (`dTieredTribunal-11`), 42 of 62
(`dFramedEntrypoint`), four of five blockers (`dRetiredFork` r2), both blockers (`aGradedMandate` r2).

The fold path is the most travelled route in the corpus — only 12.0% of specs are still at rev-1.

**The template's entire fold instruction is one clause inside §4**: *"Review corrections fold in
here; bump the header rev and log it in §9."* `BUILD-METHOD.md:134` says the same. **Neither names a
re-read set.** An author folding a correction into §4 is never told which other sections that edit
may have invalidated — and the confirmed-finding distribution does not migrate across rounds
(§2+§4+§6 is 63.5% at round 1, 59.1% at round 2, 65.0% at round 3), so the fold keeps breaking the
same three sections.

### B2 · §9 absorbs a third of all growth and tells the next reader almost nothing — HIGH

Measured by git replay over **all 411 multi-commit specs: §9 takes 33.5% of growth against §4's
15.9%.** §9's growth exceeds §4's and §6's combined (71,838 B vs 54,380 B).

*Method note, and it matters.* The measurement record's cross-sectional table put §9 at 25.2% of
growth. That method compares different specs at different rev bands, not one spec over time. The
git replay is the stronger instrument and its number supersedes the earlier one. Both agree on
direction and on §9 being the largest single sink; the replay is what carries the argument.

And the content is thin: **of 1,665 rev lines across 468 specs, only 492 (29.5%) name any section,
S id or AC id.** 70.5% record that a fold happened and nothing about what moved. The template makes
§9 the resumption surface — "the rev high-water a resumed session reads" — and its own skeleton
example models exactly the uninformative form the corpus then copies.

This is the mechanism behind B1. A reader cannot re-read what a fold invalidated because the log
does not say what the fold touched.

**Do not read this as "cut §9".** The skeptic pushed back and was right: §9 is load-bearing in four
other places — `HYGIENE.md:300` mandates that a ledger's `AMENDED` form name the §9 line that logs
it, and findings A5, B2 and A4 all rest on §9 lines as their evidence carrier. The finding is that
the entry is unstructured, not that it is unnecessary.

---

## Theme C — sections whose enforcement or content does not match the corpus

### C1 · §7's gate names resolve against nothing, and prose §7 opts out silently — HIGH

`tools/check-spec-tokens.py` is the only thing that resolves a §7 gate name against
`tools/gate-legs.json`. It reads **only a line that is nothing but backticked tokens**, and only on
non-terminal specs. **Of the 31 live specs, 18 have a §7 with no such line at all** — including 10
of the 14 units of `aSurfacedLexicon`, the build that is live right now. Not one of their gate names
is checked.

`TEMPLATE-SPEC` never states the list shape that makes the join fire, and `grep -n
"check-spec-tokens" memory/TEMPLATE-SPEC.md` returns nothing. An author writing §7 as prose — which
the section's one-sentence body invites — opts out of the only check on it and is never told.

The cost is already visible: **34 §7 occurrences across 12 near-miss spellings do not resolve**
against the 93 rows of the manifest. `memory-tree hygiene` for `memory hygiene` 12 times across 3
builds; `memory tree hygiene` 6; `memory-hygiene` 5; `line-length` 3.

### C2 · §10's predicate fails on most of the specs it nominally governs — HIGH, but mostly historical

**203 of the 346 Tier-2 specs dated on or after `SPEC10_CUTOFF` (58.7%) fail the checker's own
two-fact §10 predicate.**

*The skeptic materially narrowed this and the narrowing is the point:* **189 of those 203 are
terminal records** (183 CLOSED, 6 WONTDO) that no builder will ever reground against. The live
exposure is **12 specs** (9 SPECCED, 3 INPROGRESS) plus 2 DEFERRED. And **all 64 specs the evidence
arm actually grades pass it.** The arm is clean everywhere it is armed; what the number describes is
the grandfathered tail the cutoff deliberately parked.

`BUILD-METHOD.md:209` makes regrounding step 5 "re-run the recall probe with the terms recorded in
that spec's §10". For those 12 live specs, that step resolves to nothing.

### C3 · Two of the ten §5 rows are dead in this corpus — MEDIUM

**a11y is answered N/A in 394 of 397 specs (99%); i18n in 248 of 282 (88%).** Against risks 0/407,
testing 0/432, observability 14/428 (3%), migration 21/428 (5%).

That is the correct shape for a shell-and-Python repo with no UI and no localized strings, and
`.memory-tree.conf` has no key declaring the §5 row set the way it declares `DISCIPLINES` and the
cutoffs. **39 Tier-2 specs already drop at least one of the ten rows** and the gate cannot see it —
it grades only that §5 is non-empty, so a dropped row is indistinguishable from an answered one.

Two honest bounds on this. The rows are carried by the COPIED SKELETON, not compelled by a gate, so
an adopter can already edit them. And the saving is not tokens: the 642 dead rows are 22,287 bytes,
**0.26% of the corpus.** This is an author-attention finding, not a cost one.

### C4 · `base` is shape-checked and never resolved — MEDIUM

Check 12 asserts the `base` field is 8 hex characters (`check-memory-hygiene.sh:983`) and never
resolves the object. **9 of the 86 distinct base values name commits absent from this non-shallow
clone**, carried by 22 spec files across five builds. All 22 are CLOSED, so a resolver would catch
nothing existing and is purely forward-looking.

### C5 · The ledger population is defined by a filename convention nobody enforces — MEDIUM

**39 of 113 records carrying an `Evidences` block are not named `*acceptance-ledger*`.** The
structural definition is the block, not the filename.

*The skeptic rejected the proposed fix and was right:* `TEMPLATE-SPEC.md:208` already points at
`HYGIENE.md` for the grammar and explicitly declines to restate it. Adding a locator sentence to §6
is the paraphrase-beside-its-source class this repo refuses. Recorded as a fact about the corpus,
not as a template defect.

### C6 · A defect in the template's own prose — LOW

`memory/TEMPLATE-SPEC.md:16` says `SPEC10_CUTOFF` is *"DECLARED in `.memory-tree.conf` beside the
three other cutoffs."* Both halves are wrong: the conf declares **six** cutoffs, and `SPEC10_CUTOFF`
is not among them — it lives at `check-memory-hygiene.sh:42` and reaches a blank conf by forward
resolution at `:90`.

Nothing is broken; the value resolves correctly either way. But a reader following the template to
the conf finds nothing, and the count beside it is stale. It is the charter's own two rules — *point
at the source rather than restating it*, and *no count of a derived population is written in prose*
— broken by the document that teaches the format. Found independently of the fan-out, by
`grep -nE '^[A-Z_]+CUTOFF=' .memory-tree.conf`.

---

## What the format does well — measured, and reported because a fault-hunt selects for faults

**The ceremony is nearly free.** This was the lens's own hypothesis and it came back a negative
result: cutting the skeleton would save essentially nothing, and the numbering demonstrably
survives into downstream use — 59 section-7 bodies name `tools/gate-legs.json` by path, 250 name
`run-gates.sh`. The format's cost is not its boilerplate.

**A related and sharper negative.** The claim that `TEMPLATE-SPEC.md` is 67.5% prose about the
checker rather than about writing was **refuted** — the byte split reproduces but the headline does
not follow from it.

**Acceptance ledgers are real coverage.** 147 of 154 CLOSED Tier-2 units owing one (95.5%) are
evidenced by a journal-kind record. Check 22 does what it claims.

**§5 mostly earns its place.** Only 26.9% of its 4,107 bullets are N/A — measured expecting far
worse. Three bullets in four say something. C3 above concerns two specific rows, not the section.

**§1 does not churn.** 1.3x growth from rev-1 to rev-6+ across 474 specs. Whatever revision does to
these documents, it is not relitigating what the unit is for.

**The five grandfathered headerless specs are correctly grandfathered** — two predate
`SPEC_FORMAT_CUTOFF`, three carry no filename date. Checked, not assumed.

### A hypothesis that died under its own control

The mandated `"When <action>, <observable result>"` phrasing was tested for outcome benefit against
1,413 joined ledger lines. The raw comparison looked significant (Fisher p = 0.0016) — and then
**collapsed under one control**: a `"When X, Y"` criterion structurally cannot open with its
backticked token, while a bare-assertion criterion can, so the token-mismatch metric was measuring
sentence shape rather than outcome. Refuted.

The honest state is that **there is no evidence the mandated phrasing helps, and none that it
hurts.** Anyone proposing to keep or drop it is arguing from taste, and should say so.

---

## Two known problems this pass did NOT find, stated so absence is not read as coverage

- **Whether a conforming spec is actually more useful to a builder than a non-conforming one.** No
  instrument in this corpus can answer it. Every finding above is about the format's internal
  consistency, its enforcement, and its downstream amendment cost — all proxies. The direct question
  would need a controlled comparison this corpus cannot supply.
- **Whether the churn is the format's fault or the work's.** The Tier-1/Tier-2 split (27.4% vs 7.0%
  right-first-time) is confounded: tier is assigned by risk, and risk correlates with difficulty.
  B1's fold measurement is the closest thing to a causal answer, and it indicts the fold PROCEDURE
  rather than the section canon.

---

## If anything gets built, this is the order

Ranked by confirmed severity against implementation cost. None of this is a decision.

1. **Give §9 a structured entry** — a rev line names the sections it touched. It is the mechanism
   behind the corpus's dominant defect class (B1), it is a grammar change to one line, and 70.5% of
   existing lines already fail it. Pairs with a re-read rule in the fold instruction.
2. **Join §2 to §6.** A scope item names the criterion that observes it, or says why none does.
   Confirmed by 16 builds; 13.3% current citation rate means the convention exists and is unused.
3. **Make check 23 compare ledger content, not just labels.** A doc-local join needing no tree
   access, with a worked failing case already on disk in a CLOSED, green unit.
4. **Ask §6 for the failure mode.** 93 specs answer it unprompted; the charter requires it of gates
   and never of the specs that specify them.
5. **Fix §7's silent opt-out** — either state the backticked-list shape in the section, or make
   `check-spec-tokens.py` read prose. 18 of 31 live specs are currently ungraded.
6. **Ask §6 for cost and permission.** Largest binnable amendment class, 23 of 81.
7. **Declare the §5 row set in `.memory-tree.conf`.** Attention, not tokens — 0.26% of corpus bytes.
8. **Fix `TEMPLATE-SPEC.md:16`.** Two-line correction, no behavior change.

Items 1–4 are where the evidence is strongest. Items 5–8 are cheap and independent.

## The refuted five, listed so nobody re-raises them

| # | Claim | Why it died |
|---|---|---|
| 5 | The writing rules are twelve bullets and zero gates | Nine bullets, and two of them ARE gated — the empty-body walk and the canon equality |
| 7 | `order <n>` permitted-not-required breaks the README's derived region | Counts reproduce; the population argument does not |
| 18 | The mandated `When X, Y` phrasing measurably hurts | Collapsed under one control — it measured sentence shape, not outcome |
| 29 | 262 code identifiers live only in §9, so §9 is un-skippable | Regex artifact; 110 of 262 appear elsewhere in the same spec |
| 33 | The template is 67.5% prose about the checker | Byte split reproduces, headline does not follow |
