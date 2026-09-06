**Serves:** spec-audit TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12

# Four blocking defects, three of them a wrong number the specs would have ratified

Tier-2 spec audit, round 1, 2026-09-05, node `a`, build `aSurfacedLexicon`, streams `tooling`. These
are DESIGNS ONLY: no code from any of the three units exists yet, so every finding below is a defect
in a document, and the cheapest possible moment to fix one. The three subjects, at the blobs they
were read at:

- `TOOL-aSurfacedLexicon-8` —
  `memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-8.md` at blob
  `22d2ec7a1eb4d374f9619f48930b901fbcca0788`
- `TOOL-aSurfacedLexicon-11` —
  `memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-11.md` at blob
  `bc6626871f495c1155cd635b3d881f5ebadd3c1d`
- `TOOL-aSurfacedLexicon-12` —
  `memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-12.md` at blob
  `8da68d1e36bae752ad91f61acb4ebae2c5ef8d69`

All three read at repository HEAD `8db42509`, clean tree, run base `6c670b02`.

**The honest shape of this round, which a reader must not be sold as one clean run.** The four
finder lenses — underspecification, contradiction, unstated-assumption, prior-art — ran to
completion and returned 69 raw findings. The original verify and synthesis stages then DIED on a
session limit, and no report was written at all. The 69 findings were rescued from the run journal
afterwards and put through a second, separate verification pass, whose verdicts this report joins on
the integer id rather than on a `file:line` string, because several findings share an address. So
the finder stage and the verify stage did not run in one session, and the synthesis you are reading
is the second attempt, not the first. Nothing here is unverified — every surviving row carries a
skeptic verdict with its own re-measurement — but the round was not continuous and the report is a
reconstruction.

## Verdict: BLOCKED

## Review shape

Raw findings 69 · confirmed 65 · refuted 4 · precision 0.94. The 65 confirmed findings deduplicate
to 41 distinct defects: 4 blockers, 4 highs, 19 mediums, 14 lows. Blockers by unit: unit 8 one, unit
11 one, unit 12 two.

Precision at 0.94 is far above the ~0.5 floor §8 sets, which says the lenses were well primed and
the surface was rich. The four refutations are listed at the end, because each one was refuted by a
sentence the spec already contains — that is information about the designs, not noise.

## Findings

| # | Sev | Subject | Address | One line |
|---|-----|---------|---------|----------|
| 1 | blocker | unit 12 | S6, AC4, AC5 | The kill-rule reading is 10.6%, not 3.6%, and the real number inverts the ruling |
| 2 | blocker | unit 8 | AC1/AC2/AC4/AC5/AC6 | Five criteria are measured against cells undeclared at this unit's own landing order |
| 3 | blocker | unit 11 | S2, section 10 | The overlay merges at a call site the canon's actual consumers never route through |
| 4 | blocker | unit 12 | S12, AC12 | The charter headroom is 8 bytes, not 285, and S11 names a funding source that frees nothing |
| 5 | high | unit 12 | AC1 | The 77-line ceiling is unreachable: the whole region is 140 lines and the unit adds two blocks |
| 6 | high | unit 12 | S11, section 4, section 7 | The charter is a rendered pair; only the template side is named, and four unguarded legs select on it |
| 7 | high | unit 12 | AC12 | An advisory WARN is made a pass condition, contradicting unit 2's ratified reading |
| 8 | high | unit 11 | S2 vs section 6 | Every criterion that exercises the overlay lives on a leg no boundary runs |
| 9 | medium | units 8, 11 | status headers, Files touched | Two order-6 units write the same two files, inside one function, and neither names the other |
| 10 | medium | unit 12 | S8, AC7 vs F1 | An open fork is pre-decided by a hard criterion that forces the defect the fork exists to avoid |
| 11 | medium | unit 11 | status header, AC5 | The spec is pinned to a base outside the run, and AC5 asserts equality against it |
| 12 | medium | unit 12 | section 5 testing row | The row says one staged break and no new predicate; section 6 carries four REDs and a new refusal |
| 13 | medium | unit 12 | section 4 records | "The roster already reaches 13" — it reaches 14, and the family high-water is 17 |
| 14 | medium | unit 8 | S2 vs sections 5 and 6 | Three distinct refusals are declared, one is graded, and section 5 lists a different three |
| 15 | medium | unit 8 | F2 resolution | The ratified bare-surface refusal reaches neither scope nor acceptance |
| 16 | medium | unit 8 | AC5, S2 | AC5 names no input and no answer, and no spec says what a `file` cell's argument even is |
| 17 | medium | unit 8 | S5 | The convention-only advice path — the tool's whole quiet case — is graded by no criterion |
| 18 | medium | unit 12 | S4, AC3 | S4 describes the narrow named-directory ban unit 2 replaced, and a mechanism unit 2 proves cannot work |
| 19 | medium | unit 8 | F2 census | The census is attributed to a spec that contains no such block, over a superseded population |
| 20 | medium | units 8, 11 | S6, section 4 Inventory | Both units mint identifiers with no cell, no `--suggest` verdict, and no mint table |
| 21 | medium | unit 8 | section 7 leg list | A new module reds the unguarded codebase-map leg; neither the leg nor `symbols.json` is named |
| 22 | medium | unit 8 | section 4 Inventory | The Inventory names one of four re-casing sites, and the named one is unreachable for AC1 |
| 23 | medium | unit 11 | section 4 adopt-lexicon.sh | The stamp refusal needs a CANON-block detection route the existing arm does not have |
| 24 | medium | unit 11 | S8 | The honest limit is required in two carriers and graded in none |
| 25 | medium | unit 12 | section 3 Non-goals | "The seven hyphenated Python filenames" measures 8, and this unit pastes the pin |
| 26 | medium | unit 8 | section 3, F2 | The selector-grammar tense is backwards, and no rule says how a selector'd key is suggested |
| 27 | medium | unit 11 | AC8, AC9 vs F1 | AC8 and AC9 state F1's ruling as fact while F1 is still open |
| 28 | low | unit 12 | S5, S7, section 7 | Three cited line numbers land on the wrong line, one of them on whitespace |
| 29 | low | unit 12 | section 4 Rollout | The build's one recorded ordering hazard is written for a unit that will not be built |
| 30 | low | unit 11 | section 3 final bullet | "Two existing legs gain arms" — three do |
| 31 | low | unit 11 | AC4 | AC4 requires an exit-0 run and states no route to one |
| 32 | low | unit 11 | AC9 | "Near-miss" is undefined, and the criterion grades the population it names |
| 33 | low | unit 11 | S3 | A minus-delete naming no shipped cluster has no defined behaviour |
| 34 | low | unit 11 | section 4 Data model | "The two other callers" is three; one is deleted at build order 1 |
| 35 | low | unit 8 | section 4 SPAN-ANCHORED | An absolute the next paragraph contradicts and two criteria disprove |
| 36 | low | unit 12 | S8 | S8 cites an `### Inventory` sub-head that `memory/TEMPLATE-SPEC.md` does not have |
| 37 | low | unit 11 | section 1, section 8 | "Owner ruling R2" cites an authority the rulings record does not contain |
| 38 | low | unit 8 | section 5 i18n row | A backlog row named as a landing precondition already exists |
| 39 | low | unit 8 | S3, section 4 | The `vocab`/`notail` ordering rule may govern an empty population and nobody can tell |
| 40 | low | unit 8 | S7 | The claim that `kit.toml`'s placeholder list follows the Skill edit is unexplained |
| 41 | low | unit 12 | S5, AC4 | The Q8 prose corrections are routed into Q9's record, which has a different subject |

---

### 1 — blocker — unit 12 — the kill-rule reading is wrong, and the real number inverts the ruling

**Address:** section 2 S6, section 6 AC4 and AC5.
**Folds raw ids:** 1, 29, 54.

Running the signal reproduces `added: 142, offenders: 15, rate_pct: 10.6` on the fresh-file arm —
the arm whose own note says it is "the reading the kill-rule watches". S6 states 3.6%, being 5 of
138. Both operands are wrong. The 138 is the coverage count from the research pass's own line 24,
not the arm's `added`.

The figure is not merely aged: `git diff --name-only 6c670b02..HEAD` returns 28 paths, all `.md`
except `memory/map/generated/inventories.json`, so no armed-language definition entered the window
and the reading at the spec's pinned base is the same one.

The conclusion inverts. The docstring's rule abandons the pressure chain at or below roughly 5%
across two further readings, and PROMOTES it from probation to scheduled on a rate that climbs. 4.3%
to 10.6% is the climb branch. S6's "that makes today the FIRST of the two further readings" is
therefore false, and AC4 and AC5 make writing 3.6% into three append-only supersession notes plus
`memory/builds/dScaffoldedMirror/README.md` a pass condition. A wrong number landing as the
permanent correction for a wrong number, in the one unit whose whole subject is settling this
arithmetic.

**Fix.** Re-run the signal at the landing commit and rewrite S6 with the three operands it prints —
`added`, `offenders`, `rate_pct` — and the command that produced them. Then re-decide the record: at
a rate above the bar, AC5's correction line must say the reading disqualifies today as one of the
two further readings and must name the climb clause instead.

**Left-shift.** Add an acceptance criterion requiring every number written into a record to be the
one the named command prints AT THE LANDING COMMIT, not one carried from a research pass. This is
the build's own rule 2, measure-never-estimate, and it is currently a habit rather than a criterion.

### 2 — blocker — unit 8 — five criteria measured against cells undeclared at this unit's own order

**Address:** section 6 AC1, AC2, AC4, AC5, AC6, against the status header's `order 6` and S1/S2.
**Folds raw ids:** 2, 19, 38, 53.

Unit 6 at order 4 says in its own words that it lands with exactly one `CELLS` row, `py.constant`.
Unit 12 at order 7 is the unit whose S14 writes the full matrix. Unit 4, the grammar unit, ships no
rows at all — its Migration says the conf rewrite that pastes the real bodies is a later unit. So at
unit 8's landing order the tracked declaration holds one cell.

AC1 passes `--as py.type`, AC2 `py.function`, AC4 `js.function`, AC5 `py.file`, AC6 `md.file`. Every
one of those is undeclared at order 6, so each hits this unit's OWN S2 undeclared-cell refusal
instead of the behaviour it asserts. AC6 is worse than unreachable: it observes a refusal naming
`md.file` as `dark`, and what it would actually get is the undeclared refusal, a different message.

This is not only bookkeeping. S1 makes `--as` REQUIRED, so the landing commit makes `--suggest` —
the verb the rendered Skill routes to — unusable for every surface except `py.constant` for a whole
build order, with no flag to turn it off.

The idiom that solves this is already in the build. Units 5, 7 and 13 phrase every armed-cell
criterion against a scratch declaration and say so; unit 5's own words are "Every criterion phrased
against an ARMED cell is therefore measured in a scratch declaration, and each one now says so". A
grep for `scratch` over unit 8 returns nothing.

**Fix.** Add the scratch-declaration preamble to section 6, copied from unit 5, and say per
criterion which declaration it is measured in. Separately decide whether `--as` may be required at
order 6 at all, or whether the requirement waits for the matrix at order 7.

**Left-shift.** Make "every criterion naming a cell names the declaration it is measured in" a line
in `memory/TEMPLATE-SPEC.md`'s acceptance section, so the next spec cannot forget it. Unit 12's S8
is already editing that file.

### 3 — blocker — unit 11 — the overlay merges where the canon's consumers do not read

**Address:** section 2 S2 and section 10 (the reuse audit).
**Folds raw ids:** 37.

S2 puts the overlay merge inside `build_form_index()`. The tree does not route the canon through it.
`tools/lexicon/scaffold_lexicon.py:147` builds `seeded` straight from `canon.CLUSTERS`, and `:192`
calls `canon.read_gloss` and `canon.render_negative`, both of which iterate `CLUSTERS` directly at
`canon.py:100` and `:115`. None of those three touches `build_form_index`.

So an overlay merged only inside `build_form_index` cannot add, delete or re-represent a PROPOSED
row — which section 3 says is the canon's entire function. The consequences are concrete:
`read_gloss` returns the empty string for an unknown representative, and `lexicon.py:504-509`
refuses a `VERBS` row carrying no negative, so an ADD row seeds a declaration the kit's own checker
reds.

The spec cannot see this because section 4's Files-touched line says `scaffold_lexicon.py` takes "no
functional change", and section 10 re-ran `grep -rn build_form_index tools/` — a probe that by
construction cannot see a `CLUSTERS`-direct consumer. A guard that reads the same state the bug
corrupts.

**Fix.** Re-run the reuse audit over `canon.CLUSTERS` and `canon\.` rather than over the one
function name, then move the merge to where all three consumers see it — either `CLUSTERS` becomes a
function returning the merged tuple, or `read_gloss` and `render_negative` route through the index.

**Left-shift.** A reuse audit that greps only the function the spec already chose is the
could-not-fail shape. Add to the spec template's reuse-audit sub-head: grep the DATA the change
affects, not the accessor the design happens to name.

### 4 — blocker — unit 12 — the charter headroom is 8 bytes, and S11's funding source frees nothing

**Address:** section 2 S12, and the AC12 budget premise resting on it.
**Folds raw ids:** 30, 36, 55.

S12 states "48867 of 49152 bytes with 285 free". Running `bash tools/check-template-size.sh` reports
`49144 / 49152 bytes (8 under, 100.0%)`. The 48867 figure is the reading at `d0a18683`, the OLD
base; rev-4 re-pinned the base and re-verified the three conf figures in S1 while leaving this one.

Unit 2 already declared that exact pair dead in writing, in its AC8: the rev-1 pair 48867 / 285 was
measured at `d0a18683` and is dead at this rev's base, so the headroom is EIGHT bytes, not 285.

The second half is what makes this a blocker rather than a stale number. S12 says S11 is paid for
out of the bytes `TOOL-aSurfacedLexicon-2` frees, while unit 2's AC8 only requires its edit to be
"net-neutral or net-negative in bytes" — a guarantee of ZERO freed bytes, not a budget. So S11 adds
content to the charter against 8 bytes of headroom with no funding source, and the `template size`
leg reds on landing. Eight bytes cannot hold a sentence.

**Fix.** Replace the figures with the reading at the run base, cite unit 2's AC8 as the source that
already ruled on them, and either name a real deletion that funds S11 or defer S11 until a measured
saving exists. Re-measure after unit 2 lands rather than asserting the saving in advance.

**Left-shift.** Every byte-budget claim in a spec should carry the command that produced it and the
sha it was measured at, the same way this build already treats pin counts. A budget figure with no
provenance is the one that survives a re-pin.

### 5 — high — unit 12 — AC1's 77-line ceiling cannot be reached and cannot be satisfied

**Address:** section 6 AC1, against S13, S14 and section 4.
**Folds raw ids:** 3, 32, 41, 59.

Measured at the run base: `.lexicon.conf` is 216 lines, 178 of them comments, and region 24-163 is
140 lines of which 139 are comments. AC1 demands the file end up "smaller by at least the 139
comment lines", i.e. 77 lines or fewer.

Deleting the entire region outright lands at 76. The whole budget is spent before one byte is added.
The same unit then pastes a blank-separated `PINS` block (S13, 2n-1 lines), the full `CELLS` matrix
(S14, added at rev-5), and keeps the three surviving decision comments section 4 requires — all into
the same file. The criterion cannot go green without dropping something the unit's own scope
requires.

Two further legs make it worse. The base reading is taken at the wrong tree state: units 2, 5 and 6
all name `.lexicon.conf` in their Files-touched lists and all land before order 7, so 216 is not the
line count this unit starts from. And rev-5 introduced S14 without re-deriving AC1.

**Fix.** Rephrase AC1 as a landing-time delta over the region rather than an absolute file-length
ceiling — "lines 24-163's comment region is gone" plus "the 23 verb rows still print" — and
re-measure the base at the order-7 tree rather than at today's.

**Left-shift.** When a revision adds scope (here S14), the revision log should require re-deriving
every criterion that measures a quantity the new scope changes. rev-5's log records the addition and
revisits nothing.

### 6 — high — unit 12 — the charter is a rendered pair and only one half is in scope

**Address:** section 2 S11, section 4 Files touched, section 7.
**Folds raw ids:** 31.

`grep -n 'forbidden import'` hits the template at :319 AND `AGENTS.md` at :384, where the
`{{LEXICON_CONF}}` token is already substituted. `render_playbook.py:546` defaults `--charter
AGENTS.md`, and the `playbook render wiring` leg carries NO guard key in `tools/gate-legs.json`, so
it runs on every bar and asserts the rendered region equals a fresh render. Three further unguarded
legs select on the same edit: `template size <=48KiB`, `charter size` over `AGENTS.md`, and
`playbook parity`.

Section 4's Files-touched list names neither `AGENTS.md` nor any of those legs, section 7 names no
template-side leg, and AC11 greps the template only. Editing one half of a rendered pair reds the
bar.

The spec gets exactly this two-file discipline right one bullet earlier, for
`SPEC-TEMPLATE.template.md` / `memory/TEMPLATE-SPEC.md` in S9. That is what makes this an omission
rather than a house style.

**Fix.** Add `AGENTS.md` to Files touched, add the four legs to section 7, and extend AC11 to grep
the rendered side too — or state that the render is regenerated in the same commit and gate that.

**Left-shift.** The kit already knows which files are rendered pairs. A spec-time check that flags a
Files-touched list naming one half of a known pair would catch this class without a reader noticing
it.

### 7 — high — unit 12 — AC12 makes an advisory WARN a pass condition

**Address:** section 6 AC12.
**Folds raw ids:** 47, 56.

Unit 2's AC8 rules in writing that the size leg "also WARNs past its recorded high-water
independently of the ceiling, and that warning is advisory and does not satisfy or fail this
criterion." AC12 makes the same WARN a pass condition.

The tree already warns on a clean checkout: `TEMPLATE-SIZE WARN — 48378 -> 49144 (+766)`. So AC12
cannot green unless this unit shrinks the charter by 766 bytes, which neither S11 nor S12 proposes.
And section 4 nowhere measures what unit 2's deletion actually frees, which is the same funding gap
finding 4 records from the other side.

**Fix.** Adopt unit 2's already-ratified reading: AC12 observes the OK line and its ceiling, and
records the WARN as advisory context, not as a condition.

**Left-shift.** Two sibling specs in one build disagreed about what a single gate leg's output
means. The leg's own header should state which of its lines are verdicts and which are advisory —
§7's "a gate's own header states what it does NOT check", applied to output rather than to coverage.

### 8 — high — unit 11 — every criterion that exercises the overlay runs on no boundary

**Address:** section 2 S2 against section 6.
**Folds raw ids:** 4.

AC6 and AC7 call `build_form_index(overlay)` from `selftest.py`, AC5 exercises the no-overlay
default, and AC8/AC9 grade the scaffold guard. AC4 runs the product CLI with a stamped one-row block
but observes only the posture line. Nothing asserts that a declared overlay changes an ANSWER at the
call site S2 spends its entire body choosing.

Section 7 confirms the `lexicon selftest` leg sits in chunk `selftests`, reachable only under
`GATE_SELFTESTS=1`, which no boundary sets. So the arms that do touch the merge are invisible at the
push boundary, and the one arm on the merge bar observes a banner.

**Fix.** Add a criterion that runs the product CLI against a conf carrying an overlay row and
observes the answer CHANGE — a form the shipped canon does not resolve, resolving. Put that arm on a
leg the push boundary runs.

**Left-shift.** This is the green-by-absence class: a unit whose whole subject is a behaviour
change, whose behaviour-change evidence lives on a leg nobody runs. Add to the spec template's gates
row: name, for each acceptance criterion, the leg that carries it and whether a push runs that leg.

### 9 — medium — units 8 and 11 — two order-6 units write the same two files, inside one function

**Address:** both status headers (`order 6`) and both Files-touched tables.
**Folds raw ids:** 23, 49, 64.

Both specs read `order 6`. Both Files-touched lists name `tools/lexicon/lexicon.py` and
`tools/lexicon/selftest.py`. The intersection is inside ONE function: unit 8 replaces
`run_suggest`'s case-inheritance block at `lexicon.py:837-846`, and unit 11 routes its overlay
through the `build_form_index` call site unit 7 grafts into `run_suggest`. Neither spec mentions the
other — a grep for the sibling id in each returns only its own title line.

The build's convention is established and the gap is filed. `memory/backlog/TOOL.md:341`
(`TOOL-aSurfacedLexicon-17`, OPEN) records that the generated Parallel column derives from the order
field alone, names BUILD-METHOD M6's proven-disjointness requirement, and uses the step-5 pair as
its worked example. Units 7 and 13 pinned their sequencing in their own specs after round 2. Units 8
and 11 did not.

**Fix.** Add a Rollout sentence to both specs sequencing the two within order 6 on write-set
intersection, naming the other unit's id.

**Left-shift.** `TOOL-aSurfacedLexicon-17` is the right home: make the generated Parallel column
derive from write sets, not from the order field, so the remembered constraint becomes a gated one.

### 10 — medium — unit 12 — an open fork is pre-decided by a hard criterion

**Address:** section 2 S8 and section 6 AC7, against section 8 F1.
**Folds raw ids:** 14, 43, 67.

F1 is still listed OPEN, with the recommendation to word the new TEMPLATE-SPEC line so it is a no-op
for an adopter with no lexicon kit — naming the cell as an optional qualifier RATHER than an
instruction pointing at a tool the reader may not have. AC7 makes `grep -c -- "--as"
memory/TEMPLATE-SPEC.md` at least 1 a pass condition, and `--as` exists only inside that
instruction.

So the fork is not free: taking F1's own recommendation falsifies AC7. And S9 byte-couples this file
to the memory-tree kit's shipped `SPEC-TEMPLATE.template.md`, so satisfying AC7 ships the defect F1
names into every memory-tree adopter's spec template — as a landing criterion rather than as a
choice.

**Fix.** Ratify F1 before the unit builds. If the AC7 branch wins, record why the dangling reference
is acceptable in an adopter with no kit; if F1's recommendation wins, rewrite AC7 to grep for the
qualifier wording instead.

**Left-shift.** An acceptance criterion that decides an open fork should be impossible to write
unnoticed. Add to the spec template: section 8's open forks are listed by id in section 6's
preamble, and no criterion may name a branch of one.

### 11 — medium — unit 11 — the spec is pinned to a base outside the run

**Address:** section 0 status header (`base d0a18683`) and section 6 AC5.
**Folds raw ids:** 24, 50.

Unit 11's header carries `base d0a18683` while the run base is `6c670b02`, and AC5 makes that stale
base a pass condition: it returns "a mapping equal to the one it returns at base d0a18683". Reading
all fourteen headers, unit 11 is the only SPECCED spec still on the old base.

Nothing here is substantively wrong. `git diff --name-only d0a18683 HEAD -- tools/lexicon/
.lexicon.conf` returns zero files, and every load-bearing cite re-measures at the run base:
`canon.py:84 build_form_index`, `CLUSTERS` at :55-81, the three callers at `lexicon.py:1065`,
`scaffold_lexicon.py:121` and `selftest.py:686`. What is defective is a pass condition anchored to a
tree nobody in this run has checked out, which a later reader must fetch to evaluate.

**Fix.** Re-pin the header to `6c670b02` with a rev line, and re-word AC5 to compare against the run
base.

**Left-shift.** A spec whose header base differs from the build README's run base is
machine-detectable in one line. That belongs on the memory-tree hygiene gate, not in a reviewer's
head.

### 12 — medium — unit 12 — the testing row undercounts its own staged breaks

**Address:** section 5, the testing and left-shift row, against section 6 AC2, AC6, AC9 and AC14.
**Folds raw ids:** 7, 8, 33.

Section 5 says "no new predicate, so no new failing case to stage", and names AC2's pin-block
round-trip as the one observation with a staged break. Section 6 carries four: AC2 ("The RED is
observed"), AC6 (staging the line into `memory/TEMPLATE-SPEC.md` alone "makes it exit non-zero
first, which is the observed RED"), AC9 ("Both observed"), and AC14 ("The RED half is observed
too").

The "no new predicate" half is also wrong on its own terms: S14 sets `UNDECLARED_CELL_ARMED = True`,
which converts unit 6's report-only arm into a refusal — a behaviour change in a predicate, arriving
in this unit. rev-5 added S14 and AC14 and did not revisit section 5.

AC14 compounds it from the other side: it asks for its landing observation "by a check over the
commit rather than over the tree" and names no command and no carrier, and section 7 lists no leg
for it. The tree-side half of AC14 IS named, and the armed arm refuses on every undeclared cell once
the constant is True, so nothing goes ungated — what is missing is the invocation.

**Fix.** Rewrite the row to name all four observations and to record the arming as the new refusal
it is, and give AC14's commit-scoped half a command. The risk is an implementer using the
production-readiness row as the landing checklist.

**Left-shift.** Make the staged-break count in section 5 derived from section 6 rather than authored
— one more instance of derive-over-author, applied inside a document.

### 13 — medium — unit 12 — "the roster already reaches 13" is short by four

**Address:** section 4, "The records, and how a supersession is written here".
**Folds raw ids:** 57.

The build README's front matter carries ids through `TOOL-aSurfacedLexicon-17`; spec file -14 exists
at order 4, and `memory/backlog/TOOL.md` rows :341, :342 and :343 are live OPEN rows for -17, -15
and -16. The roster reaches 14 and the family high-water is 17.

The operative instruction in the same sentence — "a plain 1-up above its own high-water" — is
self-computing, and §2 independently requires a grep-check before minting, so a builder following
process recovers. The stale figure is still wrong by four in the one unit that appends to the
append-only log.

**Fix.** Drop the count. It cannot be right for longer than a commit, and the instruction beside it
does not need it.

**Left-shift.** This is the prose-beside-the-source-that-owns-it class the charter names. A count of
a derived population does not belong in a spec at all.

### 14 — medium — unit 8 — three refusals declared, one graded, and a third list

**Address:** section 2 S2, against section 5 and section 6.
**Folds raw ids:** 6.

S2 names three distinct refusals — undeclared, dark, malformed — and makes the distinctness binding.
Of those, only `dark` is graded, by AC6. AC3 grades the missing-flag refusal, which is S1's, not
S2's.

Section 5's error-state row then lists a DIFFERENT trio — missing `--as`, undeclared cell, dark cell
— plus F1's narrowed refusal, dropping malformed entirely. The spec disagrees with itself about the
population, and nothing observes the distinctness S2 makes binding.

**Fix.** Reconcile section 5 to S2's trio, and add criteria for the undeclared and malformed
refusals that assert the messages differ.

**Left-shift.** Where a spec declares refusals as DISTINCT, an acceptance criterion should compare
the messages rather than merely observe a non-zero exit. Distinctness asserted and never observed is
the gate-satisfied-by-its-own-prose shape.

### 15 — medium — unit 8 — the ratified bare-surface refusal reaches neither scope nor acceptance

**Address:** section 8, the F2 resolution, against sections 2 and 6.
**Folds raw ids:** 10.

The ratified F2 block requires `--as` to refuse a bare surface with a message listing the declared
cells that carry it, and calls that list the thing making the refusal "a menu rather than a wall" —
the stated mitigation for the unquotable-cell cost the same ruling records. S1 and S2 never mention
a bare surface (at best it falls under S2's malformed refusal, which itself has no criterion), and
no criterion exercises it.

A ratified fork resolution that reaches neither scope nor acceptance is unimplemented.

**Fix.** Add the bare-surface case to S2 as its own named refusal, and a criterion passing a bare
surface and observing the cell list in the message.

**Left-shift.** Add to the spec template: every RESOLVED fork names the scope bullet and the
criterion that carry its ruling. A resolution with neither is a decision that will not ship.

### 16 — medium — unit 8 — AC5 has no input, and no spec says what a file cell's argument is

**Address:** section 6 AC5 and section 2 S2.
**Folds raw ids:** 9, 46.

AC5 reads, in full, that when `--as py.file` is passed the answer is a snake stem and no
leading-token check runs. No input identifier, no expected output. It is satisfied by any
already-snake input, and asserts a negative about an unnamed name. Its neighbours AC1, AC2 and AC4
all pin inputs, and AC4 pins three answers by value — so this is a departure from the spec's own
standard.

Underneath it sits a real gap. A `file` cell grades the basename up to its FIRST dot (the research
record measures the last-dot rule disagreeing on 64 graded files), and `_SUBTOKEN_RE` at
`subtokens.py:20` shreds `.` and `/` into separate tokens, so the suggester never computes that
stem. Grepping the whole spec for `.file` returns only AC5, AC6 and the quoting note. What a
file-cell argument IS — a bare stem, a basename, a path — is unaddressed.

**Fix.** State in S2 what `--suggest` accepts for a `file` cell and how it reduces to the graded
stem. Then rewrite AC5 with a named input and a named answer.

**Left-shift.** A criterion with no input cannot fail. Make "every acceptance criterion names an
input and an expected value" a line in the spec template's acceptance section.

### 17 — medium — unit 8 — the convention-only path is graded by nothing

**Address:** section 2 S5.
**Folds raw ids:** 11.

S5's committed message content — the re-cased spelling plus the convention the input already
satisfies — is graded nowhere. AC1 is a suffix hit, AC2 and AC4 are verb hits, AC5 grades no message
at all, AC6 is the dark refusal, AC7 the non-ASCII refusal, AC8 the render. Not one criterion passes
an input that is merely mis-cased under a convention it otherwise satisfies, which is the tool's
quiet everyday case. Section 5's "every refusal names the flag or the cell" does not reach it
either, because this path is not a refusal.

**Fix.** Add a criterion with a named input that hits no verb row and no banned suffix, observing
the re-cased spelling and the convention named.

**Left-shift.** Same class as finding 14: the spec grades its exceptional paths and skips its normal
one. A spec-review question worth adding to the checklist — which criterion covers the case where
nothing is wrong?

### 18 — medium — unit 12 — S4 describes a predicate unit 2 replaced, by a dead mechanism

**Address:** section 2 S4 and section 6 AC3.
**Folds raw ids:** 15.

S4 calls record (c)'s compensating check "the source scan asserting no `tools/lexicon/*.py` imports
`codebase-map`". Unit 2 states the replacement predicate in full and it is neither of those things:
it is that every non-relative import in a `.py` file beside `lexicon.py` names either a stdlib
top-level module or another `.py` file in that directory — explicitly "stronger than the deleted
rule, because it refuses any foreign kit rather than one named directory", with no hand-kept name
list.

Unit 2 then rejects the mechanism S4's wording implies outright: the check "judges IMPORT STATEMENTS
through `extract`, never file text. A whole-file text search is the
`memory/gotchas/absence-assertion-over-whole-file-text.md` class, and it would fire here on its own
documentation."

This wording lands in append-only `memory/DECISIONS.md`, where the only correction is a
supersession.

**Fix.** Restate S4's compensating check in unit 2's own words, and cite unit 2's spec as the
source.

**Left-shift.** Where one unit describes another unit's mechanism, quote it rather than paraphrase.
This is the same rule the charter states about paraphrasing a protocol, applied between two specs in
one build.

### 19 — medium — unit 8 — the F2 census names a source that has no such block

**Address:** section 8, the F2 resolution (the surface census), and section 4 Data model.
**Folds raw ids:** 20, 63.

F2's ruling says it counted "the `CELLS:` block `TOOL-aSurfacedLexicon-4` proposes" and treats that
census as what makes the tie-break decisive. Unit 4 contains no such block — its Migration says the
conf rewrite that pastes the real bodies is a later unit, and its S3 declares FOUR surfaces where
the census has three, dropping `constant`. The block actually counted is the research record's, at
its lines 348-364, whose figures F2 reproduces exactly.

The population is also superseded. Two owner overrides arm cells that the proposed block does not
carry — `sh.function` (Q5) and `py.constant` (Q6) — and both land at order 4, before this unit. F2's
Residual hedges that every measurement is against unit 4's proposal, but its stated re-run trigger
is a changed KEY SHAPE, which arming two cells is not, so a reader inherits the stale count.

Correcting it does not move the ruling — `constant` would be another one-cell surface, which
strengthens the varies-by-surface argument.

**Fix.** Re-attribute the census to the research record, re-count against the armed population at
order 6, and widen F2's re-run trigger to any change in the declared cell set, not only its key
shape.

**Left-shift.** A ruling that cites a census should name the artifact and the sha it counted. This
one names a sibling spec that never held the data.

### 20 — medium — units 8 and 11 — minted identifiers with no cell, no verdict and no mint table

**Address:** unit 8 section 2 S6 and section 4 Inventory; unit 11 section 4 Data model.
**Folds raw ids:** 21, 51.

Unit 8's S6 says only that "the renderer that turns subtokens back into a declared convention lands
in `tools/lexicon/subtokens.py`" — no identifier, no cell. Its `### Inventory` is prose about the
code being replaced, with no mint table. Unit 11's section 4 says `build_form_index()` "grows one
optional parameter" without naming it.

Unit 8's section 7 then asserts that `lexicon naming predicates` "must stay green: this unit adds no
offender and moves no pin" — an assertion about names the spec never writes down.
`VERB_OFFENDER_PIN` is armed at 461 with zero headroom, counted per occurrence, and that leg guards
on `tools/`, so the landing commit selects it.

The prior art is inside this build and is exactly the right shape: unit 4's section 4 Inventory is a
three-column Identifier / Cell / Role table with seven rows, headed "Identifiers this unit mints,
each with the cell that grades it". Unit 7 goes further with a four-row table carrying each
`--suggest` verdict and a stated "Pin delta: ZERO", plus the build-wide obligation that any
identifier added in this build owes its own `--suggest` run before the commit lands.

**Fix.** Add unit 4's mint table to both specs, with each identifier's cell and `--suggest` verdict,
and state the pin delta.

**Left-shift.** Unit 12's S8 is already adding this requirement to the spec template. Make it name
the `--suggest` verdict and the pin delta explicitly, not just the cell.

### 21 — medium — unit 8 — a new module reds the unguarded codebase-map leg

**Address:** section 7 (leg list) against section 2 S6 and section 4 Files touched.
**Folds raw ids:** 22.

`tools/gate-legs.json`'s `codebase-map coverage + freshness` leg carries NO guard key — chunk
`declarations`, subject `repo`, ceiling 300 — so nothing scopes it off any bar; its two neighbouring
codebase-map legs both carry guards, this one does not. `memory/map/generated/symbols.json` already
indexes `tools/lexicon/subtokens.py` by symbol, with live rows for `leading_verb` and `subtokens`.
S6's new renderer is a public definition whose absence from the regenerated artifact reds that leg
at the push boundary.

Section 7 enumerates `lexicon wiring`, `lexicon naming predicates`, `lexicon selftest` and
`memory-tree hygiene` and stops. Section 4's Files touched omits `symbols.json`.

The in-build precedent is unambiguous: unit 2's AC9 names the three unguarded legs whose populations
it moves, including this exact one, and records that all three carry `subject: repo` with no guard
key.

**Fix.** Add the leg to section 7 and `symbols.json` to Files touched, with the
claim-edits-regen-in-the -same-commit rule §1 already states.

**Left-shift.** Unit 2 got this right by enumerating unguarded legs deliberately. Add to the spec
template's gates row a prompt: which legs carry no guard, and does this unit move any of their
populations?

### 22 — medium — unit 8 — the Inventory names one re-casing site of four, and the wrong one

**Address:** section 4 Inventory.
**Folds raw ids:** 39.

The control flow in `run_suggest`: `:802-804` returns on a name with no word characters, `:805-807`
prints OK and returns when the verb is declared, the `:837-846` block the Inventory names sits
inside `if verb in banned:` at `:834`, and `:849-851` is the else. AC1's `FooManager` leads with
`foo`, which is neither declared nor banned, so it exits at `:850` — and the spec's own section 4
table records that exact output.

So the Inventory sub-head, whose job is to name the sites being replaced, names one of four, and the
one it names is unreachable for the unit's first criterion. The same section's Data model does state
the correct semantics — the banned tail when `notail` is armed, the leading token when `vocab` is
armed, and the convention always — so an implementer is not being told to build a re-caser that only
runs in the banned branch.

**Fix.** List all four exit paths in the Inventory with their line ranges and say which the renderer
replaces.

**Left-shift.** An Inventory that names a single line range inside a multi-branch function should be
required to name the function's exits. That is the kind of thing a reuse audit surfaces if it is
asked for exits rather than for one block.

### 23 — medium — unit 11 — the stamp refusal has no CANON-block detection route

**Address:** section 4 Files touched, the `adopt-lexicon.sh` row.
**Folds raw ids:** 45.

`adopt-lexicon.sh:226` reads `ratified=` out of the conf and `:227` refuses UNCONDITIONALLY when it
is empty. S5 makes the new refusal conditional on a `CANON:` block being PRESENT, and section 4's
Migration requires this repo — which declares no block and stamps nothing — to stay green. Section
4's one-line "beside the existing `ratified` arm" names no detection route.

The script's own comment at `:216-217` rules out the obvious shortcut: "A second parser here is the
two-answers-to-one-question class, so this shells out rather than re-implementing the grammar", and
`:218` shells out to `lexicon_conf.py --print-verbs`. So the block-presence question needs a named
call, not a grep.

AC1 through AC3 all pass a conf that HAS a block, so the false-refusal branch — every kit-less
adopter redding the unguarded `lexicon wiring` leg — is gated by nothing.

**Fix.** Name the call that answers "does this conf declare a `CANON:` block", and add a criterion
running `--check` against a conf with no block and observing exit 0.

**Left-shift.** Where a new refusal is conditional, require a criterion exercising the NEGATIVE
branch. A refusal spec'd only on its firing path ships a false positive to everyone who is not the
author.

### 24 — medium — unit 11 — the honest limit is required in two carriers and graded in none

**Address:** section 2 S8.
**Folds raw ids:** 5.

S8 requires the honest limit written into the conf comment and the kit README; section 4's
Files-touched list names both carriers, and section 5's user-docs row repeats the obligation. No
criterion among AC1 through AC9 mentions either file, so an implementation shipping the merge, the
refusals and the posture line passes intact with neither written.

**Fix.** Add a criterion greping both carriers for the limit sentence.

**Left-shift.** §1's Definition of Done already says a user-facing change without an up-to-date page
is not done. A criterion that greps the doc carrier is the cheap machine form of that, and it
belongs in the spec template's user-docs row.

### 25 — medium — unit 12 — "the seven hyphenated Python filenames" measures eight

**Address:** section 3 Non-goals, and the surviving conf comment it preserves.
**Folds raw ids:** 65.

Counting unique non-snake Python basenames at the run base returns 8, the extra one being
`check-kit-placeholders`. The spec states seven twice — once as a non-goal carrying "a pin of 7",
once as the conf comment it will preserve through the rewrite. Under Q2's ratified two-sided
equality a pin of 7 against a measured 8 reds the bar, and this is the unit that pastes the pin
block and keeps the comment, so the stale figure lands in the declaration.

`memory/backlog/TOOL.md:342` (`TOOL-aSurfacedLexicon-15`) already records the same 8 with its
command.

**Fix.** Re-measure at the landing commit, write 8, and cite the command.

**Left-shift.** Same class as findings 1, 4 and 13: an authored count of a derived population. The
pin block is the one place such a count has to be authored, which is exactly why it needs its
command beside it.

### 26 — medium — unit 8 — the selector-grammar tense is backwards and selector'd keys have no rule

**Address:** section 3 Non-goals, and the F2 resolution in section 8.
**Folds raw ids:** 60.

Unit 13 is order 5 and unit 8 is order 6, so the selector'd key grammar ALREADY exists when `--as`
lands. Section 3 writes it as future — "cell keys grow a THIRD component after this unit ships" —
and F2 rules that the full cell "is forward-compatible with that".

The consequential gap is real: S2 resolves the cell against the `CELLS` block and defines refusals
for undeclared, dark and malformed, with no rule for a key carrying a selector clause. Unit 13 never
mentions `--suggest` or `--as` — a grep returns nothing. So neither spec answers which convention a
`cmd_*` name is suggested in, which is the exact surface-blindness section 1 says the unit exists to
remove.

**Fix.** Correct the tense, and state in S2 how a selector'd row participates in cell resolution —
match, ignore, or refuse.

**Left-shift.** When two units in one build extend the same key grammar, the later one should state
the earlier one's shape as landed fact. A spec-review question: does every "after this unit ships"
clause name a unit that actually lands later?

### 27 — medium — unit 11 — AC8 and AC9 state an open fork's ruling as fact

**Address:** section 6 AC8 and AC9, against section 8 F1.
**Folds raw ids:** 27.

Section 8 keeps F1 open — "what shape does the S7 guard predicate take?" — with two named ways out
and a closing recommendation, and it is conspicuously NOT marked resolved, unlike R2 directly above
it, which carries a full RESOLVED (owner, 2026-09-04) line. AC8 already states the ruling as fact
("The predicate is NOT the bare `grep -c CANON tools/lexicon/scaffold_lexicon.py` the research
record proposed") and AC9 grades the narrowed predicate's near-miss.

If F1 lands the other way — reword the comment so the bare grep holds — both criteria are false and
must be rewritten. Unit 8's section 8, where both forks carry explicit ratification blocks with
reasoning, shows this is a missing step rather than a house style.

**Fix.** Ratify F1 with a block in unit 8's shape. The recommended branch is well argued; it needs a
signature, not a rethink.

**Left-shift.** Same left-shift as finding 10 — no criterion may name a branch of an unratified
fork.

### 28 — low — unit 12 — three cited line numbers land on the wrong line

**Address:** section 2 S5, section 2 S7, section 7.
**Folds raw ids:** 34, 52, 68.

`drift_report.py:945` is blank; `def build_lexicon_marginal_offense_rate` is at `:946` and its
docstring opens at `:947`. `memory/backlog/TOOL.md:118` is a `TOOL-cBriefedPilot` row;
`TOOL-dClosedLexicon-2` is at `:121`. `check-testsuite-counts.sh:35` is a comment; the selection is
at `:36`. A fourth cite checks out and is not a defect: `SKILL.template.md:19` really is the
`{{SUGGEST_CLI}}` line.

Cosmetic, but S5 makes that docstring the SOLE carrier of the kill-rule arithmetic and AC4 points
three supersession notes at it, so the one cite that must survive lands on whitespace. An
implementer editing by line number touches an unrelated backlog row.

Unit 11's rev-2 already made exactly this correction for itself, recording that a cluster shape sat
at `:55-80` and not at `:52`, which is a blank line.

**Fix.** Re-derive the three numbers and prefer a symbol-anchored cite where one exists.

**Left-shift.** Line-number cites rot on the next edit. A spec-lint that resolves every `path:line`
cite and checks the line is non-blank would catch the whole class cheaply.

### 29 — low — unit 12 — the one recorded ordering hazard names a parked unit

**Address:** section 4 Rollout, the ordering-hazard paragraph.
**Folds raw ids:** 35, 69.

The build README parks `TOOL-aSurfacedLexicon-10` — its fork lost both options to the M3 veto ladder
— and the Rollout paragraph is written as live guidance for that unit's implementer, disclosing
nothing about the parking. Meanwhile the live collision at order 6 (finding 9) is recorded nowhere.

So the section that reads as the build's ordering record describes work that will not happen and
omits work that will.

**Fix.** Mark the paragraph conditional on unit 10 being unparked, in one clause.

**Left-shift.** When a unit is parked, grep the build for prose that still addresses its
implementer. A one-line check at parking time.

### 30 — low — unit 11 — "two existing legs gain arms" — three do

**Address:** section 3, final bullet.
**Folds raw ids:** 26.

Section 3 says "No new gate leg. Two existing legs gain arms". Section 7 lists three lexicon legs
that each gain arms: `lexicon wiring` (the stamp refusals), `lexicon naming predicates` (the S7
guard) and `lexicon selftest` (which "holds the six arms"). Section 5 confirms six selftest arms
plus the S7 guard's failing case.

Nothing downstream breaks — section 4's Files-touched list spells the six arms out one by one and
section 5 counts them — so no reader deriving a landing checklist misses them.

**Fix.** Change two to three.

**Left-shift.** Same derive-over-author point as finding 12: a count in section 3 that section 7
owns.

### 31 — low — unit 11 — AC4 requires an exit-0 run and states no route to one

**Address:** section 6 AC4, against section 3 and section 8 F2.
**Folds raw ids:** 16.

AC4 requires the posture line observed "on a run that exits 0 as well as one that exits non-zero",
with a stamped `CANON:` block declaring one row. Section 3's "No automatic re-pinning" bullet says
an overlay moves definitions between the debt and unruled buckets "so the run reds until the `PINS:`
block is re-pasted".

The route is in that same sentence — re-paste the block and it greens — so the arm is reachable by
an obvious step rather than unreachable, and AC4's closing "Both cases are observed" forces the
implementer to find it. A missing sentence, not a criterion that cannot pass.

**Fix.** Name the re-paste step in AC4.

**Left-shift.** None warranted. This is one clause.

### 32 — low — unit 11 — "near-miss" is undefined

**Address:** section 6 AC9.
**Folds raw ids:** 17.

AC9 requires the candidate predicate to print "its hits AND its near-misses", and nothing in the
spec defines near-miss; the term is inherited from the charter's §7 rule, which does not define it
either. The criterion is saved from being satisfiable-by-construction only because AC9 pins the
expected output exactly — "the only near-miss it reports is `tools/lexicon/scaffold_lexicon.py:181`"
— so a predicate reporting none fails it. The underlying figure holds: `grep -c CANON
tools/lexicon/scaffold_lexicon.py` returns 1, at `:181`.

**Fix.** Define near-miss for this predicate in one clause — a line matching the loose form but
excluded by the narrowing.

**Left-shift.** The charter's §7 rule that a candidate predicate must print hits and near-misses
would be sharper with a one-line definition of the term beside it.

### 33 — low — unit 11 — a minus-delete naming no shipped cluster has no defined behaviour

**Address:** section 2 S3.
**Folds raw ids:** 18.

S3 says only that a leading minus DELETES a shipped cluster, and section 4's data model repeats it.
Neither says what happens when the named cluster does not exist. Section 5's error-state row
enumerates exactly three refusals and this is not among them. AC6 exercises only the successful
delete, so a silent no-op and a raise both pass it — and a silent no-op means an owner typo is
counted as an owner declaration on the posture line while changing nothing.

**Fix.** One sentence in S3 choosing raise or no-op, and a matching error-state row if it raises.

**Left-shift.** For any declaration verb, the spec template's error-states row should prompt for the
naming-something-absent case. It is the most common undefined branch in a small config grammar.

### 34 — low — unit 11 — "the two other callers" is three, and one of them is deleted

**Address:** section 4 Data model.
**Folds raw ids:** 28.

Section 4 says the optional parameter means "`tools/lexicon/selftest.py:686` and the two other
callers compile unchanged" — three. S2 says "Only two of the three survive to this unit's landing",
because `lexicon.py:1065` sits inside `run_probe`, which `TOOL-aSurfacedLexicon-3` deletes at build
order 1. All three call sites exist at the run base, so the pre-correction count is what section 4
still carries.

rev-2 records that S2 and section 4 "now also record that the :1065 caller is deleted"; S2 got the
arithmetic and the section 4 sentence did not. Nothing downstream breaks — the optional parameter is
right either way.

**Fix.** Correct the sentence to two.

**Left-shift.** A revision that corrects a number should grep the spec for the old number before
closing.

### 35 — low — unit 8 — a span absolute the next paragraph contradicts

**Address:** section 4 Design, the SPAN-ANCHORED paragraph.
**Folds raw ids:** 40.

`_SUBTOKEN_RE` matches only alphanumeric runs. `fetchUserData` spans as (0,5)(5,9)(9,13), covering
every character with no gaps, so AC2's expected `load_user_data` must emit two underscore bytes that
exist in no span; `fetch_v2_data`'s underscores at 5 and 8 sit outside every span, so AC4's expected
`loadV2Data` must delete them. The paragraph's "never regenerates a byte outside a span. That is
binding rather than a preference" is therefore false as an absolute.

The resolution is already one paragraph down: "The refusal is NARROW ... Separators are re-supplied;
`$` and e-acute are not" — verbatim the correction needed.

**Fix.** Fold the separator carve-out into the absolute so the two paragraphs state one rule.

**Left-shift.** None warranted; this is a wording pass.

### 36 — low — unit 12 — S8 cites a sub-head that does not exist

**Address:** section 2 S8, and section 6 AC7's neighbourhood.
**Folds raw ids:** 42.

`memory/TEMPLATE-SPEC.md` has no `### Inventory` heading. `Inventory` appears at `:116` as a name
inside the recurring-sub-heads bullet and at `:182` as prose in the skeleton's section 4, whose
headings stop at `## 4. Design` with no `###` beneath. S8's "in section 4's already canonical `###
Inventory` sub-head" names a place this artifact does not have. AC7 resolves it correctly by
pointing at "the `### Inventory` bullet of the recurring sub-heads", so the ambiguity is between two
sections of the same spec.

**Fix.** Reword S8 to match AC7's location.

**Left-shift.** Same as finding 28's — a cite-resolution lint would catch a named heading that no
target file contains.

### 37 — low — unit 11 — "Owner ruling R2" cites an authority the rulings record does not hold

**Address:** section 1, and section 8's first bullet.
**Folds raw ids:** 62.

The canonical rulings record tabulates Q1 through Q10 and carries no R2. The label is defined in the
research record's section 5 (the canon door) and the owner ruling itself is in the build README in
words, so the substance is fully backed and findable one grep away. It is a missing cite, not a
missing ruling.

**Fix.** Cite the research record's R2 and the README's wording, or renumber to the Q the rulings
record uses.

**Left-shift.** Where a build keeps two records of rulings under different label schemes, one of
them should say how its labels map to the other's. Cheap, once.

### 38 — low — unit 8 — a backlog row named as a landing precondition already exists

**Address:** section 5, the i18n row.
**Folds raw ids:** 58.

The row says the ASCII-only finding "is filed as an unfiled review finding in the research record
and needs its backlog row before this unit builds". `memory/backlog/TOOL.md:343` already carries
`TOOL-aSurfacedLexicon-16` for exactly that. The row landed one commit after this spec's last edit,
so this is stale-by-one-commit prose, and the harm ceiling is a duplicate row in a mutable backlog.

**Fix.** Cite `TOOL-aSurfacedLexicon-16` and drop the precondition.

**Left-shift.** A spec naming an unfiled finding as a precondition should name the id once filed.
The build's wrap-up derivation is the natural place to sweep for that phrase.

### 39 — low — unit 8 — the ordering rule may govern an empty population

**Address:** section 2 S3 and section 4 Data model, against section 6.
**Folds raw ids:** 12.

"The first hit is the answer" orders the `notail` check ahead of the `vocab` check, but AC1 hits
only the suffix arm and AC2 only the verb arm, so an implementation checking the leading token first
is indistinguishable from the specified one. And no spec in the set states which cells arm BOTH —
grepping `notail` across all fourteen specs returns only unit 4's grammar and unit 8's own prose,
never a matrix row. Unit 4's grammar makes both arms optional per row, so the ordering rule may
govern an empty population and nobody can tell.

**Fix.** Either name a cell arming both and add a criterion whose input hits both arms, or say the
ordering is defensive against a population that does not yet exist.

**Left-shift.** A rule stated about a population no declaration populates is dead text. Worth a
question in the spec template: which declared rows does this rule apply to?

### 40 — low — unit 8 — the kit.toml claim is unexplained

**Address:** section 2 S7, against section 6 AC8.
**Folds raw ids:** 13.

`SKILL.template.md:19` is `{{SUGGEST_CLI}} <identifier>` and `kit.toml:38` is the six-name
placeholders list, so appending a literal `--as <cell>` needs no descriptor change and S7's
"kit.toml:38's placeholder list follows" is unexplained. The hazard is smaller than it looks:
`adopt-lexicon.sh:145-147` greps the rendered Skill for a leftover `{{...}}` token and refuses, on
the unguarded `lexicon wiring` leg, so an unsubstituted token cannot ship silently.

**Fix.** Either drop the kit.toml clause or say what about it changes.

**Left-shift.** None warranted.

### 41 — low — unit 12 — the Q8 corrections are routed into a record with a different subject

**Address:** section 2 S5 and section 6 AC4.
**Folds raw ids:** 66.

The rulings record sends the Q8 prose corrections into Q9's record (a), and both the research record
and this spec define record (a) as the `TOOL-dScaffoldedMirror-18` supersession — a different
subject. S5 and AC4 make the corrections id-less in-place notes, so nothing in the append-only log
carries the kill-rule supersession under its own id. The note-beside-the-quoted-claim mechanism is
precedented and cited in this same spec, so nothing is lost except an id.

**Fix.** Either mint an id for the kill-rule supersession or state in S5 that the corrections are
deliberately id-less and why.

**Left-shift.** Where a rulings record routes one question's output into another's record, the
receiving spec should say so explicitly rather than inheriting the routing silently.

---

## Refuted (4)

- **Raw 25** — that unit 11's AC1-AC4 contradict its section 4 Migration. They do not: AC1-AC4 are
  conditionals describing a STAGED state and the Migration describes the LANDED tree. Staging
  exactly this is the charter's own stage-the-break-confirm-RED-unstage discipline, which AC1
  restates in its own words.
- **Raw 44** — that a `CANON:` ADD row whose representative is a shipped alternative has undefined
  behaviour. It is defined in three places: section 4's post-merge disjointness assertion, section
  5's error-states row, and AC7, which requires `build_form_index` to raise rather than resolve by
  iteration order.
- **Raw 48** — that the CELLS matrix's conventions are a mirror of the corpus they grade. The
  anti-mirror rule governs SPELLINGS of concepts, not which case convention a surface declares;
  `md.file dark` grades nothing and so cannot be derived from a population; and the provenance asked
  for is already written in the research record's proposed block, with its measurements.
- **Raw 61** — that unit 11's criteria let a reader commit a deliberately broken conf. AC1 names the
  declaration, section 4's Migration discloses that this repo declares no block, and AC5 pins the
  tracked end-state as having none.

## What is right about these designs

Reporting only the faults would misrepresent the state of this work. Three things stand out.

**The build already invented the fixes for most of these findings, in earlier units.** The
scratch-declaration idiom (findings 2), the mint table with `--suggest` verdicts and a stated pin
delta (finding 20), the enumeration of unguarded legs whose populations a unit moves (finding 21),
and the explicit fork ratification block (findings 10, 27) are all in units 4, 5, 7 and 13, in
exactly the shape the three subjects need. Almost nothing here requires a new discipline — it
requires applying the build's own.

**Corrections propagate, and are recorded.** Unit 2's AC8 already ruled the stale byte pair dead and
ruled the WARN advisory, in writing, before this audit ran. Unit 11's rev-2 corrected its own
off-by-one line cite. `TOOL-aSurfacedLexicon-15`, `-16` and `-17` are filed against three of the
gaps below — the shell pin count, the ASCII-only finding, and the Parallel column's over-claim.
Several findings above are defects only because a correction that exists elsewhere did not reach one
sentence.

**The refutation rate is the good news.** Four of 69 findings were refuted, and every one of them
was refuted by a sentence the spec already contains — a conditional AC, a disjointness assertion, a
measurement in the research record. Specs that survive an adversarial read at 0.94 precision are
specs that were written carefully; the surviving findings cluster hard in one place, which is stale
NUMBERS and criteria measured against the wrong tree state, not in the designs' mechanisms. Three of
the four blockers are a number. That is a very cheap failure mode to fix, and a very expensive one
to have ratified.
