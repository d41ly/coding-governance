**Serves:** spec-audit TOOL-aBatchedArm-5

# Tier-2 spec audit — TOOL-aBatchedArm-5, ROUND 4

*The third fold audit. Round 3 (BLOCKED, 1 blocker, 13 highs, 5 mediums, 1 low, precision 0.44)
was folded into rev-5 of the unit that replaces the pooled mode's `budget x sweep-ceiling-factor`
hang bound in `tools/run-gates/run-selftests.sh` with an evidence-derived one, declares a
`--pooled --calibrate` bootstrap under a serial-sum wall, makes the pooled VERDICT mean parity with
the calibrated baseline, and lands the DoD flip dark as the build's landing step. Every confirmed
row of round 3 is folded and was carried into this round as a prior finding; this round reads THE
FOLD'S DIFF ONLY — the new S4 (the parity verdict), the re-numbered S5 (carriers by role, the
landing order), AC10, AC11, the F6 re-resolution, and the section 4, 5 and 7 sentences the fold
touched — and does not re-report what rounds 1 through 3 found. Node `a`, 2026-09-14, ROUND 4.
Every finding below survived a skeptic prompted to REFUTE it, and every cited line, count and exit
path was re-read or re-run in the tree by the author of this report rather than transcribed from a
lens: the runner's render loop was opened at `run-selftests.sh:701-753` and its guards at
`:776-808`, the seven pooled test arms were read at their lines in `run-selftests.test.sh`, the
DoD-phrase predicate and the carrier predicate were each re-run over the tracked tree and their
yields counted by location, unit 3's AC4 was read at `spec/…-3.md:200-212` and its ledger's shard
table at `build/…-3-1-acceptance-ledger.md:212-221`, the shard checker's exit was traced to
`check-unattended.test.sh:3270` and its last line, and the `run-selftests self-test` ledger row was
read from `<git-dir>/gate-ledger.tsv`. Each row carries its address inside the spec, the fix, and
the gate that would have caught it before a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-5.md`@`fa0041be845d870b109ea01d686fe723ea1ca17e` — rev-5, the fold of round 3's twenty rows in twelve defects. ROUND 4.

## Verdict: BLOCKED

Two rows at BLOCKER, six at HIGH, two at MEDIUM. Those ten rows collapse to **four distinct
defects**; the table below names which rows share one, so a fold that repairs a defect repairs every
row under it rather than ten separately.

The fold closed what round 3 opened, in shape. The exit is re-based on parity and GREEN is the
landing word again; the summary counts `killed`, `walled`, `unrun` and `mismatched` from the lists
the runner keeps; the carrier predicate's eight lines are classified by role and the four pointers
are byte-unchanged at both steps; the fixture gets a charter stub with a registry row; `--reset
<row>` has AC10; the leg killed at its ceiling is named with its re-declaration owed at the final
pass. None of those is re-opened here. What this round finds is that the fold's replacements carry
the same class of hole one level over, in four places — three of them the exact class the round
that was folded named.

**The DoD-phrase predicate was written into the landing step without being run over the tree**
(D-1, the blocker). Re-run at this base it yields 87 lines: the charter's own §7 left-shift rule at
`AGENTS.md:265` and the size-gated template's copy at `:193`, eight frozen archive snapshots, the
runner's own DoD header at `run-selftests.sh:15`, and 71 build records including six lines of this
spec. Step (4) says the flip commit's CONTENTS are that predicate's hits re-worded, which read as
written edits the charter rule that §3's last non-goal says is not this run's to touch; and AC5's
post-commit witness — the same predicate returning zero lines naming `--serial` or `landed dark` —
cannot read zero on this tree by any correct flip, because 18 of its 21 such lines are records. The
witness also does not SEE three of the four argv carriers the flip exists to change, since
`gate-env.sh:27` and `kit.toml:125`/`:126` match only the carrier predicate. Round 3's H1 rule —
classify a predicate's yield by role before one edit is applied to all of it — was applied to the
carrier predicate and not to the second predicate the same paragraph introduced. **The parity
re-shape reaches pooled arms the re-cut list does not name** (D-2): §7 scopes the enumeration to
"every pooled arm the factor arithmetic reached" and AC6 to the `--serial` arms, but `test.sh:340`
asserts the exact RED text S4 orders re-worded and reds by construction, and four sibling arms keep
their want-strings only under a rendering rule S4 does not state. **The five-term `st` derivation
drops two red sources the render loop already has** (D-3): the could-not-start row at `:723` (no
verdict file, no wall breach — the `set -u` worker-death class the runner's own comment records)
and the peak-over-bound guard at `:786` are neither `killed`, `walled`, `unrun` nor `mismatched`,
so a literal build prints GREEN with four zeros over a row that never started — round 3's B1 one
class down. **The reading condition is weaker than the witness a CLOSED sibling already ratified**
(D-4): unit 3's AC4 rules a timed invocation a reading only with the suite's trailer present; S2
records one on "exited on its own" plus a `^FAIL` count, and ten of the fourteen DoD rows baseline
at (0, 0), which is exactly what an early `exit 0` produces.

**Convergence, and the disposition.** `memory/guides/BUILD-METHOD.md` re-arms the loop only on a
confirmed-blocker count STRICTLY SMALLER than the round before. Round 1 stood at three blocker
rows, round 2 at two, round 3 at one; this round stands at two rows, which are one defect. Counted
either way — two rows, or one defect — the figure is not strictly smaller than one, so under the
method's own rule the loop does not re-arm on this round and every standing blocker is DISPOSED
here. Disposition of D-1: FOLD — it is a defect in the document this review read, and the
mechanism it needs is a path scope on a `git grep` plus a by-role list of the lines it yields at
this base, both of which the spec already does for the carrier predicate. Nothing here needs a
mechanism this build lacks, so nothing is PROMOTED. The descent 3, 2, 1 that entered this round
does not continue through it, and this report says so rather than counting the two rows as one to
make it appear to.

## Review shape

- raw 23 · confirmed 10 · refuted 13 · unverified 0 · precision 0.43

Precision at 0.43 is below the ~0.5 floor `AGENTS.md` §8 sets, and is the fourth consecutive
decline: 0.52, 0.49, 0.44, 0.43. The number is the pipeline's and is reported as measured. This
round already took §8's remedy — its lenses were primed with round 3's twelve defects as KNOWN and
scoped to the fold's diff — and the raw count fell from 45 to 23 while the refuted share held, so
the residue is a hardening surface producing refuted noise, which is what §8 predicts. Read the
confirmed count with the table in hand: four rows hit the DoD-phrase predicate independently and
three hit the re-cut list, which the pipeline reports as zero duplicates because each addresses a
different section or a different consequence.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty.

## Scope, and the two rulings

The sibling specs are NOT in scope and are not re-graded. Units 3 and 4 are CLOSED at this spec's
base `1c736fd9`; their rows, modes and oracle are read here only as the tree this unit consumes,
and D-4 names one of them only because THIS unit's declaration is weaker than the sibling's
ratified rule on the same rows.

**Two owner rulings bind this build and were applied as facts, not findings.** 2026-09-13: build
first and verify once. 2026-09-14: no gate runs until every unit of the build is built. Every AC's
real-row half is therefore observed at the build's final gate pass, and the rows below that touch
the landing are severe precisely because that pass is the ONLY one the build gets and the landing
that follows it has no owner turn.

## The four defects, and which rows carry each

| Defect | Rows | Severity |
|---|---|---|
| D-1 · the DoD-phrase predicate is unscoped: read literally the flip edits the charter's §7 rule and the sized template, and its post-commit zero-lines witness is unsatisfiable over the tree while blind to three of the four argv carriers | id=6, id=12, id=3, id=20 | blocker ×2 / high ×2 |
| D-2 · the parity re-shape reaches pooled arms §7's factor-scoped re-cut list and AC6's serial-only guard never name; `:340` reds by construction, four siblings survive only under an unstated rendering rule | id=2, id=9, id=21 | high ×2 / medium |
| D-3 · `st` derived from five terms drops the could-not-start row and the peak-over-bound guard; a literal build prints GREEN with four zeros over a suite that never started | id=14, id=4 | high / medium |
| D-4 · a reading is recorded on `rc` plus a `^FAIL` count where unit 3 AC4 (CLOSED) requires the suite's trailer; ten of fourteen DoD rows baseline at (0, 0), the pair an early `exit 0` produces | id=19 | high |

Row severities are as filed, with one adjudication: id=21 is carried at MEDIUM rather than the
HIGH it was filed at, because its skeptic confirmed sub-point (a) alone and refuted (c) and (d) —
the reasons are under H1. The two BLOCKER rows are kept at BLOCKER because each establishes the
landing-step defect from a different side (id=6 from AC5's red-when, id=12 from the carrier
predicate's own unstated exclusion), and the integers this report returns are those two and the
six HIGH rows.

---

# BLOCKERS

## B1 · id=6 (blocker), id=12 (blocker), id=3 (high), id=20 (high) — the DoD-phrase predicate is unscoped, and both the flip's contents and its witness hang on it

**Address:** section 2 S5 step (4) (lines 122-132: "whose contents are the DoD-phrase predicate's
hits … re-worded", and "the DoD-phrase predicate re-run after the commit returning zero lines
naming `--serial` or `landed dark`") · section 6 AC5 (lines 339-350, the landing half, its
`figure:` clause and the last red-when) · section 3, the last non-goal (line 152) · section 4 "Why
the flip is the build's landing step".

Round 3's H1 established the rule and rev-5 applied it to one of two predicates in the same
paragraph. S5 now runs the CARRIER predicate, classifies its eight lines by role, and names the
four pointers as byte-unchanged; then step (4) introduces a SECOND predicate —
`GREEN verdict|not done until|DoD path|DoD command|landed dark` — and uses it twice, as the
definition of the flip commit's contents and as the post-commit witness, with no scope, no count,
no enumerated yield and no classification. It was not run over the tree before it was written in.
Re-run at this base, `git grep -nE` over the tracked tree returns **87 lines**:

- **8 outside the records** — `.githooks/gate-env.sh:26`, `AGENTS.md:265`,
  `coding-governance-agents.template.md:193`, `tools/run-gates/run-selftests.sh:15`,
  `tools/unattended/kit.toml:123` and `:130`, `tools/unattended/run-unattended-gates.sh:27` and
  `:187`.
- **8 in `memory/archive/`** — frozen template snapshots.
- **71 in `memory/builds/`** — including this spec's own lines 123, 128, 131, 158, 350 and 525,
  unit 4's CLOSED spec at `:123` and `:182`, `aFusedCharter-2:254`, `aSurfacedLexicon-12:163` and
  `:371`, and the review records.

Filtered to the lines that name `--serial` or `landed dark` — the witness's own filter — **21
remain, 3 under `tools/` (`kit.toml:130`, `run-unattended-gates.sh:27`, `:187`) and 18 in
records** the flip cannot edit. Four consequences follow, each verified rather than inferred.

First, step (4) read as written points the flip at `AGENTS.md:265` and the template's `:193` — the
charter's §7 rule "not done until a regression test covers its CLASS", which has nothing to do with
the serial mode — and at the archive snapshots. §3's last non-goal says the charter's on-demand
sentence is not this run's to re-word, and `AGENTS.md` is the file S5 itself measures 9 bytes
under its cap; an edit there is a `charter size` red on the flip commit. A run with no owner turn
reading the step literally does that edit.

Second, the post-commit witness cannot read zero. Eighteen of the twenty-one lines it filters to
are frozen records — this spec's own `:131` is the witness text itself, and `:350` is AC5's
red-when — so "zero lines naming `--serial` or `landed dark`" is RED by construction at every
commit, and AC5's landing half either ledgers red forever or the lander narrows the predicate
silently at build time to make it pass. That is the false-green shape one level up from the one F4
says unit 4's AC7 reds.

Third, the witness does not see the lines the flip exists to change. `.githooks/gate-env.sh:27`,
`kit.toml:125` and `:126` — three of the four argv carriers — match the CARRIER predicate and not
the phrase predicate; the phrase hits in those files are `:26` and `:123`, the prose lines above
them. A flip that leaves `gate-env.sh:27` spelling `--serial` passes AC5's stated post-commit check,
and AC5's red-when never names an argv left on `--serial`.

Fourth, `tools/run-gates/run-selftests.sh:15` — the runner's own DoD header, "touching a kit is a
GREEN verdict from it pasted into the landing report" — matches the phrase, names no mode, is true
under parity, and is classified nowhere: neither a carrier, nor a pointer, nor excluded.

The carrier predicate carries the same defect in miniature (id=12). S5 says it "yields eight lines
at this base"; over the whole tracked tree it yields **32**, four of them in this spec, and the
eight are the yield only with `memory/builds/` excluded — an exclusion written nowhere. AC5's
`figure:` clause says both sets are "DERIVED by the S5 predicates at build time", and the derivation
as stated does not reproduce the figure the spec types. The only scope under which either predicate
returns what the spec says is inferable solely from that count, which is not how a landing step is
allowed to be read.

**Fix.** Give BOTH predicates a declared path scope in S5, repeated in AC5's `figure:` clause, and
enumerate each yield at this base by role the way S5 already does for the carrier set:

- Carrier predicate, scoped
  `-- .githooks/gate-env.sh AGENTS.md memory/guides/SESSION-KICKOFF.md tools/unattended/` — the
  eight lines, four carriers and four pointers, as S5 has them.
- DoD-phrase predicate, scoped
  `-- .githooks/gate-env.sh tools/unattended/ tools/run-gates/run-selftests.sh` — eight lines at
  this base: re-worded at the flip (`gate-env.sh:26`, `kit.toml:123`, `:130`,
  `run-unattended-gates.sh:27`, `:187`); byte-unchanged with the reason (`run-selftests.sh:15`
  names no mode and is true under parity); and the lines OUTSIDE the scope named as excluded by
  path with the reason — `AGENTS.md:265` and the template's `:193` are the charter's §7 rule, the
  archive is frozen, the records are frozen.

Restate step (4)'s contents as the scoped phrase set re-worded PLUS the four carriers' argv spelled
`--pooled`, and restate the post-commit witness as BOTH scoped predicates re-run: the carrier
predicate returns the four pointer lines byte-identical to BASE and the four carriers spelling
`--pooled` with no `--serial`; the phrase predicate returns zero lines naming `--serial` or
`landed dark` within its scope. Mirror both in AC5's red-when — "an argv carrier still spells
`--serial` after the flip" and "any line outside the two scopes moved". Add to §3 that records,
snapshots, the template and the charter's §7 rule match the phrase and are not carriers.

**Left-shift gate.** The `govkit selfcheck` parity arm §10 already parks, with its SCOPE declared
in the arm: every line within the carrier scope matching the DoD-phrase predicate spells the same
argv as `kit.toml`'s block, and the arm's own header states which paths it does not read. Until
built, the documented fold check the charter's §7 already states and this fold broke: a predicate
written into a spec is run over the real tree BEFORE it is wired, its yield pasted with hits and
near-misses, and classified by role before one edit is applied to all of it — applied to EVERY
predicate a spec names, not to the first one a reviewer happened to catch.

---

# HIGH

## H1 · id=2 (high), id=9 (high), id=21 (medium) — the parity re-shape reaches pooled arms the re-cut list does not name

**Address:** section 7, the "New arm" paragraph (lines 411-416: "every pooled arm the factor
arithmetic reached is RE-CUT … and enumerated") · section 6 AC6 (lines 351-355, the `--serial`
arms only) · section 2 S4 (lines 91-103, the `MISMATCH` render and the RED-ambiguity re-wording)
· section 4 Files touched (lines 246-247, the seed-sizing sentence).

Rev-4's log records "every pooled arm re-cut is enumerated (H6, M4)" as a requirement this build
confirmed. Rev-5 then added S4, a re-cut that is NOT factor arithmetic, and did not extend the
enumeration. §7's list is CLOSED and scoped to the factor set — the factor `TIMEOUT` arm, `run wall
140s`, the UNRUN arm, `SELFTEST_WALL=10`, `SELFTEST_WALL=5`, the retired factor-absent arm — and
AC6 guards the serial arms only; no parity-reached class exists in either. `--pooled|--sweep)
MODE=sweep` at `run-selftests.sh:123` is one path, so every `--sweep` and `--pooled` arm in
`run-selftests.test.sh` runs the parity render. Read at their lines:

- **`:340` reds by construction.** The arm "a RED pooled run points at the `--serial` re-run, by
  its own path" stages `suite-red.sh` and wants the literal `the serial re-run: $R --serial`, which
  is `run-selftests.sh:829` — the RED-ambiguity text S4 orders re-worded "since a parity red is not
  told to confirm itself serially". Under the new spec the arm asserts a behaviour the spec removes;
  it must be re-cut to the parity wording or retired, and the spec names it nowhere.
- **`:260` and `:371` survive only under a rule S4 does not state.** Both swap `free one`'s suite
  and want the suite's own `FAIL` line beneath its row (`FAIL something`,
  `FAIL scratch-under-tmpdir`), which today is the FAIL branch's
  `grep -E '^(FAIL|nope|.*FAILED)' "$d/out" | head -4` at `:752`. Under S4 those rows are
  `MISMATCH` against a (0, 0) seed — they keep rc 1 by that — and keep their want-string only if the
  `MISMATCH` branch prints the suite's output beneath it as the FAIL branch does. S4 says nothing
  about it, and that output is the only debug surface a pooled red has.
- **`:325` is factor arithmetic the list claims to cover.** The arm swaps `free one` to `suite-mid`
  (sleeps 5 s) at budget 4, and its own comment derives the bound as "4 x 2 = 8 s" — the factor.
  Under S1 the bound is `max(4, <seed>) + max(<floor>, <fraction> x that)`, so the arm completes
  only if the fixture margin plus the `free one` seed clears 5 s; §4's seed-sizing sentence sizes
  seeds for the `SELFTEST_WALL=10` and `SELFTEST_WALL=5` arms only, and the fixture margin's
  fraction is unnamed. This arm belongs to "every pooled arm the factor arithmetic reached" by its
  own comment, and the enumeration that claims that set does not name it.

The skeptic REFUTED id=21's sub-points (c) and (d) — that `NO cost verdict was issued` at `:252`
and `:313` and `cost withheld` at `:297` and `:325` are removed by S4 — and this report agrees:
§3's first non-goal keeps the cost verdict "still withheld under `--pooled`", S5 keeps
`run-unattended-gates.sh:233` byte-unchanged as a cost question, and the kit runner's parser at
`run-unattended-gates.sh:304` still reads `cost verdict(s) WITHHELD`, so those emissions survive
unless a builder departs from a named non-goal. That is why id=21 is carried at MEDIUM: what it
adds on (a) is already in id=2 and id=9, and what it adds on (c) and (d) is a survival the spec
should STATE so a builder cannot depart from it by accident, not a red.

The cost of the omission is set by the rulings: `run-selftests self-test` is the ONLY leg behind
AC1, AC2 and AC6 through AC11, it is already killed at its 300 s ceiling (`300.333 fail`, exit
124), and under no-gate-until-the-end the builder follows §7's enumeration and the miss surfaces
at the single final pass, where the ceiling re-declaration §7 owes is then taken over a red leg.
§4 Design and §7 Gates disagree on what the parity change touches.

**Fix.** S4 states verbatim which existing emissions survive parity and how: the parity clause is
APPENDED to the row after `cost withheld`, never in its place; the `MISMATCH` branch keeps the
beneath-row output grep; the GREEN and RED summary lines keep `NO cost verdict was issued` and the
`cost verdict(s) WITHHELD` line the kit runner parses. §7 adds a second enumeration beside the
factor set, the PARITY-REACHED arms — `:252`, `:260`, `:297`, `:313`, `:325`, `:340`, `:371` —
each marked re-cut or unchanged, `:340` re-cut to the parity wording, `:260` and `:371` re-labelled
as mismatch reds, `:325` with its seed sized above its 5 s sleep and named in §4's seed-sizing
sentence. AC6 gains the clause "every pre-existing pooled arm not enumerated in §7 is GREEN
unchanged", red when one moved. Cite `TOOL-aPooledSweep-2` S2 in §10 as the per-row rule S4
preserves.

**Left-shift gate.** The arms themselves, each observed RED first. Until built, the documented
fold check: a rev log that claims "every pooled arm re-cut is enumerated" is checked by grepping
the test file for every arm that invokes the mode the fold re-shaped (`--pooled|--sweep`) and
pasting the list beside the enumeration, so the two are the same set by construction and not by a
scope word ("the factor arithmetic reached") a later fold outgrows.

## H2 · id=14 (high), id=4 (medium) — the five-term `st` derivation drops red sources the render loop already has

**Address:** section 2 S4 (lines 94-99: "the pooled `st` derives from `killed + walled + unrun +
mismatched + soundness`", and "`mismatched` computed over rows with a verdict file only") · section
6 AC11 (lines 377-386, the summary clause and the last red-when) · section 10, the
completion-oracle bullet (lines 561-565: "the runner's three non-completion lists") · section 9
rev-5 (lines 456-458).

Verified at `run-selftests.sh:701-753` and `:776-790`, the render loop sets `st=1` in SEVEN
places, and S4's five terms name four of them plus the fingerprint:

- `:706` — a row whose state is not `ok`: "this row could not be resolved into a runnable suite".
- `:711` with `:723` — a row with NO verdict file and NO wall breach: "no verdict was written, so
  this suite could not start". This is the worker-death class the runner's own `run_sweep_one`
  comment at `:626-627` records — `set -u` kills the arm "silently, in a background job, leaving
  no verdict file". It is not `killed` (`:746`, rc 124/137 — there is no rc at all), not `walled`
  (`:742`, rc 143 under a breached wall, or `:719`, no file under a breached wall), not `unrun`
  (`:716`, no scratch dir under a breached wall), and by S4's own rule not `mismatched`, since
  that is "computed over rows with a verdict file only".
- `:742`, `:746`, `:750` — `walled`, `killed`, and the FAIL branch S4 replaces with parity.
- `:786` — "THE POOL RAN WIDER THAN ITS BOUND", the composite-width guard, which is `soundness`
  only if that word is stretched past the tree fingerprint at `:799-808` that S4 means by it.

S4 states the exit "derives from" the five terms and the summary line "prints all four counts by
name", and "GREEN means: every row ran to its own end under its bound and matched its baseline, and
the tree is sound". A literal build of that sentence prints GREEN and `killed 0 · walled 0 · unrun
0 · mismatched 0` over a row that never started, and that summary is what S5 step (3) pastes and
AC5 reads as the landing witness. AC11 stages one fixture row into each of the four named classes
and its red-when — "any non-completion class is absent from the summary" — is failed by the spec's
own summary line, which names four classes where the runner has five outcomes short of completion.
§10 and the rev-5 log both say "the runner's three non-completion lists"; the runner has three
LISTS and a fourth outcome that is in none of them. This is round 3's B1 — a summary counting fewer
non-completion classes than the runner has — reproduced one class down, on the first fold after
it was found.

**Fix.** S4 states that the runner's existing `st` sources are all KEPT and that the ONLY change is
that a completed row whose (rc, fails) matches its evidence row no longer sets `st` — so the
unresolved-row red at `:706`, the could-not-start red at `:723` and the peak-over-bound guard at
`:786` survive by name. Name the could-not-start class on the summary line as a fifth word (e.g.
`unstarted <e>`), or fold it into `unrun` WITH its reason printed, and say which; name the
unresolved-row class beside it. Redefine GREEN as "every row ran to its own end" plus the runner's
existing guards, not the five terms alone. AC11 gains a red-when — "a row with no verdict file and
no wall breach reads GREEN" — and stages one such row: an argv whose worker dies before writing
`v` (an unbound-variable line under `set -u` is the cheapest, and is the class the comment names),
expecting RED with that class named on the summary. Correct §10's and rev-5's "three" to the
derived count.

**Left-shift gate.** Extend AC11's fixture arm from four seeded classes to every `st=1` branch the
render loop has, read from the loop rather than from the spec's token names, and assert the landing
predicate is FALSE on each. The documented fold check is round 3 B1's, restated because it was
folded and not kept: any AC whose witness is a set of summary tokens names every non-completion
outcome the summary's PRODUCER has, enumerated by grepping `st=1` in the producer, not by the
classes the spec chose to count.

## H3 · id=19 (high) — the reading condition is weaker than the witness a CLOSED sibling ratified on the same rows

**Address:** section 2 S2 (lines 49-70: "records a reading ONLY for a row that exited on its own —
rc captured … together with the row's POSITIVE ARTIFACT, the count of `^FAIL` lines") · section 2
S4 (the (rc, fails) pair as the parity grade) · section 4 "Why the evidence shape and not a
factor" (line 176: the `^FAIL` count "makes a fast red visible to the VERDICT") · section 5 risks
("cannot match a baseline with a non-zero `fails`") · section 10, the completion-oracle bullet ·
section 6 AC3 and AC11.

A record in this same build already decided what a READING of these exact rows is.
`TOOL-aBatchedArm-3` AC4 (rev-8, CLOSED, ratified), read at `spec/…-3.md:207-212`: "Every timed
invocation … is a reading only if the suite's own TRAILER is present in its captured output — the
line at the text `this leg ran shard` for a shard, the `PASS (…)` line for a green unsharded run,
and for a red-but-complete unsharded run the last `FAIL` line followed by exit … A timing with no
trailer is an arm that did not reach its end … and is recorded as NO READING." Unit 3's acceptance
ledger applied it verbatim (`:246-247`, "both READINGS by the trailer rule"). This unit's S2 records
a reading on "exited on its own — rc captured" plus the `^FAIL` count, and S4 grades parity on that
pair.

The pair cannot witness completion for most of the population. Unit 3's ledger table at
`build/…-3-1-acceptance-ledger.md:212-221` shows shards 3, 4, 6 and 8 at 0 `FAIL` lines; every
`st=1` in `check-unattended.test.sh` prints a `FAIL` line and the checker exits `$st` at its last
line, so a 0-`FAIL` shard whose count meets its floor exits 0 — four of the "eight red-by-design
rows [that] exit 1 when complete" in fact exit 0, and the ledger is the record. Those four plus the
six green non-shard suites baseline at **(0, 0) — ten of the fourteen DoD rows** — which is exactly
the pair an early `exit 0` produces. §4's sentence that the `^FAIL` count "makes a fast red visible
to the VERDICT" is true for the four red shards, and §5's "cannot match a baseline with a non-zero
`fails`" concedes the gap by its own wording. S4's "GREEN means every row ran to its own end" is
therefore false for a majority of the population under the `ab-arm-never-did-the-work` class S2
itself invokes: the calibrate can record a truncated run as the baseline, and the graded pass can
print `ok (rc 0, 0 FAIL matched)` over a suite that exited before its arms ran, and the landing's
parity GREEN would be a verdict this build's own AC4 rule says is not a reading.

The decided witness is cheap. The executed-count line
`(<n> assertions executed in shard k/8 against a floor of F)` is printed on EVERY shard run, green
or red (`check-unattended.test.sh:3269`, with the comment saying why), and the runner already keeps
each row's output at `$d/out` (`run-selftests.sh:642`), so the witness is one grep over a file the
runner has. One correction to the finding's remedy, verified: `check-brief-recorded.test.sh` and
`check-pass-order.test.sh` exit `$st` with no `PASS` trailer, so the trailer rule is not universal
across the six non-shard rows — it holds for the eight shard rows, and the (0, 0) class stands
regardless. §3's "no FAIL-set oracle" non-goal is untouched: the trailer is not the `FAIL` set.

**Fix.** S2: a row is a reading only when its filed output carries the suite's trailer per
`TOOL-aBatchedArm-3` AC4, cited by id; a completed exit with no trailer writes NO reading and is
named under its own word (`untrailed`), red like `walled`. For a suite that prints an executed
count, record it as a ninth column and compare it in the pair; for the two non-shard suites with no
trailer, state that the witness is rc plus `^FAIL` only and say so in the file header, so the gap
is declared and not silent. S4: the same absence at grade is `MISMATCH` (or its own word), never
`ok`. §10 adds unit 3 AC4 as the reused witness beside the README rule. AC3 and AC11 each gain a
red-when: a trailer-less row is recorded, or matched.

**Left-shift gate.** A fixture arm in `run-selftests self-test`: a suite that prints nothing and
exits 0 under `--pooled --calibrate` writes NO reading and reds the calibrate under `untrailed`,
and the same suite under `--pooled` against a seeded (0, 0) row renders `MISMATCH`, observed RED
first. Until built, the documented fold check: a spec whose ACs re-grade rows a CLOSED sibling
already graded cites the sibling's witness rule by id and states where it is weaker and why —
because a build that carries two definitions of "a reading" for one row will use the cheaper one.

---

# MEDIUM

The two MEDIUM rows are carried under the defects above — id=21 under H1, id=4 under H2 — and no
defect in this round stands at MEDIUM alone.

---

## What the fold should do first

Ordered by leverage, not by severity: one decision under each defect repairs every row under it.

1. **Scope and classify the DoD-phrase predicate (B1).** Path scope on both predicates, repeated
   in AC5's `figure:`; the phrase yield enumerated by role at this base — five re-worded at the
   flip, `run-selftests.sh:15` byte-unchanged, the charter rule and the records excluded by path;
   the post-commit witness re-runs BOTH scoped predicates, and AC5's red-when names an argv left on
   `--serial`. The disposition is FOLD, and this item is the whole of it.
2. **Enumerate the parity-reached arms and pin the survivals (H1).** `:252`, `:260`, `:297`,
   `:313`, `:325`, `:340`, `:371` in §7 as re-cut or unchanged; S4 states that the parity clause
   is appended after `cost withheld`, the `MISMATCH` branch keeps the output grep, and the
   `WITHHELD` lines survive; AC6 gains the unenumerated-arm clause.
3. **Keep every `st=1` source and name the fifth class (H2).** The could-not-start row and the
   peak guard survive by name; a fifth summary word or `unrun` with its reason; AC11 stages a
   worker that dies before writing `v`.
4. **Adopt unit 3 AC4's trailer rule (H3).** `untrailed` beside `walled`; the executed count as a
   ninth column where a suite prints one; the two trailer-less suites declared as rc-plus-FAIL
   only; `MISMATCH` on absence at grade.

Once folded, the fold is what the method's exit measures; under the STRICTLY-SMALLER rule this
round's count of two rows (one defect) against round 3's one does not re-arm the loop, so the
standing blocker is FOLDED here as its disposition rather than carried into a round 5, and the
build proceeds on the folded rev with this record and its disposition in the build README's
BUILD-LEVEL RULES slot.
