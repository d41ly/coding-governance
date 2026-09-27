**Serves:** spec-audit TOOL-aBatchedArm-5

# Tier-2 spec audit — TOOL-aBatchedArm-5, ROUND 3

*The second fold audit. Round 2 (BLOCKED, 2 blockers, 15 highs, 7 mediums, 1 low, precision 0.49)
was folded into rev-4 of the unit that replaces the pooled mode's `budget x sweep-ceiling-factor`
hang bound in `tools/run-gates/run-selftests.sh` with an evidence-derived one, declares a
`--pooled --calibrate` bootstrap under a serial-sum wall, gives the runner its own tracked evidence
file keyed on the registry tag, and lands the DoD flip dark behind a pasted pooled summary. Every
confirmed row of round 2 is folded and was carried into this round as a prior finding; this round
reads THE FOLD, narrowly — the new landing witness, the re-derived carrier set, the rebuilt fixture,
the rc column, the flip's post-state — and does not re-report what rounds 1 and 2 found. Node `a`,
2026-09-14, ROUND 3. Every finding below survived a skeptic prompted to REFUTE it, and every cited
line, byte count, ledger row and exit path was re-read or re-run in the tree by the author of this
report rather than transcribed from a lens: the runner's `killed` / `walled` / `unrun` branches were
opened at `run-selftests.sh:702-762` and its summary at `:821`, the carrier grep was re-run and
yielded the spec's eight, `SESSION-KICKOFF.md` was re-measured against C7, the kit runner's
`PIPESTATUS` branch was read at `:302-303`, `_resolve_node_tag` and `build_repo` were opened, and
the `run-selftests self-test` ledger row and log tail were read from `<git-dir>`. Each row carries
its address inside the spec, the fix, and the gate that would have caught it before a reviewer had
to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-5.md`@`c4f9d8617b3d01955f4f0c05820a7f326ee72802` — rev-4, the fold of round 2's twenty-five rows in eleven defects. ROUND 3.

The sibling specs are NOT in scope and are not re-graded. Units 3 and 4 are CLOSED at this spec's
base `1c736fd9`; their rows, modes and oracle are read here only as the tree this unit consumes, and
a row below names one of them only where THIS unit's declaration about that sibling is wrong.

**Two owner rulings bind this build and were applied as facts, not findings.** 2026-09-13: build
first and verify once. 2026-09-14: no gate runs until every unit of the build is built. Every AC's
real-row half is therefore observed at the build's final gate pass, and the rows below that touch
the landing are severe precisely because that pass is the ONLY one the build gets and the landing
that follows it has no owner turn.

## Verdict: BLOCKED

One row at BLOCKER, thirteen at HIGH, five at MEDIUM, one at LOW. Those twenty rows collapse to
**twelve distinct defects**; the table below names which rows share one, so a fold that repairs a
defect repairs every row under it rather than twenty separately.

The fold closed what round 2 opened, in shape. The calibrate wall is the serial SUM with a written
step-one branch; GREEN is no longer the flip's gate; `kit.toml:126` becomes `--checks` so the flip
removes a pass; `AGENTS.md:519` is left alone at its cap; readings land after `FP_AFTER`; both
fixture tokens are seeded; the nine held legs are named with the invocation that runs them; the
carrier set is a stated predicate; the node is the registry tag. None of those eleven is re-opened
here. What this round finds is that the fold's replacements carry the same class of hole one level
over, in four places, and that the flip's post-state — the tree AFTER step (4) — was not read.

**The new landing witness misses two of the runner's three non-completion classes** (D-1, the
blocker). The fold replaced the pasted GREEN with `killed 0`, `rc-mismatched 0` and
`fingerprint MATCHED`, and `killed` in the runner is the own-bound TIMEOUT counter only: a row the
run wall killed goes to `walled`, a row the wall stopped before dispatch goes to `unrun`, the RED
summary prints `$killed` and neither list, and an UNRUN row has no rc for `rc-mismatched` to count.
A graded pass whose wall fires prints all three landing tokens beside UNRUN rows and the flip lands
on rows never run — the false-green shape the fold was written to close, one class over. **The
carrier predicate captured two semantic classes and S4 applies one edit to both** (D-2): four of
the eight lines are DoD carriers and four are on-demand or cost pointers that already state the
post-flip fact, and the seven-for-seven dark spelling plus the step-(4) drop rewrites the owner's
dated correction at `SESSION-KICKOFF.md:169` into `--pooled ... only when they ask`, points a cost
question at the mode that withholds cost verdicts, and — measured — reds the kickoff-manifest
ratchet on this unit's own commit by 17 bytes, the exact cap analysis the fold performed for the
charter and not for the manifest. **The post-flip tree was not read** (D-3, D-4): two carriers still
promise `a GREEN verdict from ... --pooled`, which F6 says cannot occur, and the recorded DoD command
prints `unattended gates RED` on a perfect pass forever because the rc-parity signal the fold built
is never wired to the exit status. **The fixture rebuild did not carry the node** (D-7): the M6 fold
keyed every evidence row on the registry tag and made a non-matching node refuse, and `build_repo`
writes no charter, no table and no `GOV_NODE`, so every pooled and calibrate arm takes AC2's refusal
instead of testing its shape. The rest is rc parity accepting a crash that exits 1 (D-5), an rc
column that is a side effect of which reading was slowest (D-6), a leg ceiling the fixture growth
does not budget and the ledger already shows breached (D-8), two refusals with no AC (D-9, D-10), a
wrong provenance cite (D-11) and a typed count that is off by one (D-12). Each row carries its
line.

Under `memory/guides/BUILD-METHOD.md` the loop re-arms on a STRICTLY SMALLER confirmed-blocker
count: round 1 stood at three blocker rows, round 2 at two, this round at one, so the fold converged
again and a round 4 is owed after the next fold. Disposition of the standing blocker: FOLD — it is a
defect in the document this review read, and the mechanism it needs (the runner's own `walled` and
`unrun` lists, already kept at `run-selftests.sh:702`) exists in this unit's scope.

## Review shape

- raw 45 · confirmed 20 · refuted 25 · unverified 0 · precision 0.44

Precision at 0.44 is below the ~0.5 floor `AGENTS.md` §8 sets before tightening scope or priming
rather than adding agents, and it is the third consecutive decline: 0.52 at round 1, 0.49 at round
2, 0.44 here. The number is the pipeline's and is reported as measured. §8 predicts the direction —
over a hardening surface a heavy fan manufactures refuted noise — so a round 4 should prime its
lenses with this report's twelve defects as KNOWN and scope them to the fold's diff, not the whole
spec. Read the confirmed count with the table in hand: four rows hit the carrier-class defect
independently and two hit the landing witness, which the pipeline reports as zero duplicates because
each addresses a different section or a different consequence.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty.

## The twelve defects, and which rows carry each

| Defect | Rows | Severity |
|---|---|---|
| D-1 · the landing witness `killed 0` names the own-bound TIMEOUT counter only; WALL-killed and UNRUN rows are kept in two other lists the summary never prints, so the three tokens read COMPLETE over a pass that never ran a row | id=1, id=19 | blocker / high |
| D-2 · the carrier predicate yields four DoD carriers and four on-demand/cost pointers; S4 applies the dark spelling and the flip to both classes, re-words the owner's dated correction, and reds the manifest ratchet by 17 measured bytes | id=16, id=27, id=3, id=38 | high ×4 |
| D-3 · after step (4) two carriers still promise a GREEN verdict from `--pooled`, the runner's refusal text and `kit.toml:130` still name `--serial` as the DoD path and `--pooled` as dark, and `drop --serial` leaves marker prose inside argv | id=28, id=9 | high / medium |
| D-4 · the recorded post-flip DoD command prints `unattended gates RED` on a perfect pass, forever; the rc-parity signal is built and not wired to the verdict word | id=41 | high |
| D-5 · rc parity cannot witness completion for the eight red-by-design rows: a shard that crashes at 0.3 s exits 1, the same rc it was calibrated at | id=39 | high |
| D-6 · the rc column is the rc of the reading that set the max; a repaired suite mismatches on every graded pass until a whole-population `--reset`, and the post-flip meaning of a mismatch is unstated | id=30, id=40 | high ×2 |
| D-7 · the M6 fold keyed the evidence on the registry tag and made a non-matching node refuse; `build_repo` writes no charter and no arm sets `GOV_NODE`, so every pooled arm takes AC2's refusal; §10 still says the fallback is a hostname | id=21, id=26, id=35 | high ×2 / medium |
| D-8 · `run-selftests self-test` is the ONLY leg observing the fixture ACs, its ceiling is 300 and its only ledger row is `300.333 fail`, and §5 adds roughly fifteen arms with no budget and no `gate-legs.json` in Files touched | id=20 | high |
| D-9 · `--reset <row>`, the one lowering path, has no AC; S3's "Observed by AC4 and AC9" is false for that clause | id=6 | medium |
| D-10 · the absent-`ceiling-margin.txt` refusal has no arm and no red-when | id=7 | medium |
| D-11 · S4 step (3) and F6 cite unit 3 AC11 for the red-by-design fact; the record that owns it is unit 3 AC6 and the README's oracle sentence | id=42 | medium |
| D-12 · "beside the three it already carries" is a typed count of a derived population and it is 4 | id=45 | low |

---

# BLOCKERS

## B1 · id=1 (blocker), id=19 (high) — the landing witness counts one of the runner's three non-completion classes

**Address:** section 2 S1 (the pooled summary's `killed` and `rc-mismatched` counts) · section 2
S2 (`<k> killed` in the calibrate summary) · section 2 S4 step (3) · section 6 AC5 (the landing
half and its red-when) · section 8 F6.

The fold replaced round 2's pasted GREEN with three summary tokens — `killed 0`, `rc-mismatched 0`,
`fingerprint MATCHED` — and S4 step (3) says explicitly that the driver's exit status is NOT the
witness, so nothing else carries the completion fact. Verified at source, the runner keeps THREE
disjoint non-completion classes and the summary prints one. `run-selftests.sh:702` initialises
`killed=0; walled=""; unrun=""`. A row the wall stopped before dispatch is appended to `unrun` and
rendered `UNRUN` at `:716-718`; a row the wall killed is appended to `walled` and rendered `WALL` at
`:719-721` (no verdict file) and `:741-745` (rc 143 with a verdict file); `:746` is the ONLY
increment of `killed`, in the rc 124/137 own-bound branch. The RED summary at `:821` prints
`$killed killed at their own bound` and neither list — and the runner's own comment at `:713-715`
insists an unrun suite must not be reported as killed, because that would tell an operator the
suite had been tried.

S1 reuses that summary line and ADDS `rc-mismatched`, defined as a row whose rc differs from the rc
its evidence row recorded. A WALL row with a verdict file carries rc 143 and would mismatch, so the
finding as filed overstates that case; but an UNRUN row has no verdict file and no rc, so the
natural implementation of `rc-mismatched` counts it nowhere. The graded run keeps a wall — S1
derives it as `ceil(sum of bounds / OUTER)` floored at the largest bound, reachable under LPT
bin-packing when rows run near their bounds, and §4's own argument for the calibrate wall is that
the tree's sweep record shows rows outrunning a divided wall. A graded pass whose wall stops the
dispatch therefore prints `killed 0`, `rc-mismatched 0`, `fingerprint MATCHED` and one `UNRUN` line
per row it never reached; every token AC5 and F6 name is satisfied; step (4) fires; the flip lands
over rows never run. AC5's red-when — "the landing pass kills or rc-mismatches a row and the flip
lands anyway" — names no observation that reaches the WALL or UNRUN class.

The word itself is also unresolvable from the text: S2 uses `<k> killed` for CALIBRATE rows the
wall killed (a calibrate has no per-row bound, so every kill there is a wall kill), while S1's
`killed` is the own-bound counter that EXCLUDES wall kills. A builder reading both cannot tell which
class the landing token means.

**Fix.** In S1 define completion over EVERY row without a self-exited rc — TIMEOUT, WALL and UNRUN
— either as one `not-completed <k>` count or as three named counts on the summary line, `killed <a>
· walled <b> · unrun <c>`; the lists already exist at `:702`, so the counts are a word count each.
State that `rc-mismatched` is computed only over rows with a verdict file, so a reader knows why
UNRUN needs its own term. Carry the same tokens into S4 step (3), AC5's witness and red-when, and
F6. In S2 name the calibrate's kill class `walled` (or define `killed` there as wall-killed by name)
so the two summaries do not share a word for two classes. Add the arm to section 5 testing: a
fixture pooled run under a wall that fires before the last row is dispatched prints `unrun 1` and
the landing predicate does NOT read complete — observed RED first.

**Left-shift gate.** Extend the §5 arm "the pooled summary counting a killed row and an
rc-mismatched row separately" to the three classes: TIMEOUT, WALL and UNRUN each seeded once in
the fixture, each counted under its own token, and the arm asserts the landing predicate (`killed
0`, `walled 0`, `unrun 0`, `rc-mismatched 0`) is FALSE on every one of them. Until built, the
documented fold check: any AC whose witness is a set of summary tokens names every non-completion
class the summary's PRODUCER keeps, read from the producer's variable list (`:702`) and not from the
token names the spec chose.

---

# HIGH

## H1 · id=16, id=27, id=3, id=38 — the carrier predicate yields two classes and S4 applies one edit to both

**Address:** section 2 S4 (lines 87-96, the carrier set and the seven dark lines; lines 106-109,
step (4)) · section 4 Files touched (`:169 is re-worded only at the flip`) · section 5 migration ·
section 6 AC5 (the first half, "seven name `--pooled after calibration`") · section 9 rev-4 (the H3
and H8 folds).

The predicate is stated and, re-run at this base, yields exactly the eight lines S4 enumerates and
not `:142`; round 2's H8 is closed. But the predicate is TEXTUAL and the eight lines it returns are
two classes by ROLE, verified line by line:

- **DoD carriers** — lines stating the serial pass as the criterion: `.githooks/gate-env.sh:27`
  (under `:26`, "the DoD for work touching a kit is a GREEN verdict pasted"),
  `tools/unattended/kit.toml:125` and `:126` (under `:123`, "not done until this prints GREEN"),
  `tools/unattended/run-unattended-gates.sh:27` ("a GREEN verdict from ... pasted").
- **On-demand and cost pointers** — lines that already state the POST-flip fact:
  `AGENTS.md:519` ("On demand: `... --serial`"), `tools/unattended/README.md:66`
  ("`--serial` # the kit's self-tests, ON DEMAND ONLY"), `run-unattended-gates.sh:233` ("To settle
  it, one command: `--selftests --serial`" — a COST question, under `:231-232`'s "derived, not from a
  stopwatch"), and `memory/guides/SESSION-KICKOFF.md:169`, the owner's dated Correction entry:
  "`--checks` yes, `--selftests --serial` only when they ask ... prune when a bar runs them
  automatically".

S4 gives seven of the eight the dark spelling ` --pooled after calibration` beside `--serial` in
this unit and drops `--serial` from all seven at step (4), exempting only `AGENTS.md:519`, which it
swaps eight bytes for eight at the flip. Applied to the second class, each edit produces a false
statement. `:233` becomes a cost pointer at the mode S1 and §3 say withholds every cost verdict —
false now and false after the flip. `README.md:66` loses the on-demand serial line that §5 user
docs says is declared. `:169` becomes `--serial --pooled after calibration only when they ask` in
this unit — placing the DoD pass under "only when they ask", the opposite of what the unit builds
— and is then "re-worded" at the flip with no stated text, by a run with no owner turn, against an
owner-authored ruling whose own prune condition ("when a bar runs them automatically") the flip does
not meet, since a person runs the DoD and not a bar. No ruling in the build README licenses editing
that entry. And `AGENTS.md:519` after its swap reads "On demand: `... --pooled`", naming the DoD
mode as the on-demand one. After step (4) no prose carrier in the tree spells the on-demand cost
pass S4:85-87 says survives as the declared cost pass; only `--help` would.

The measured consequence (id=38): `memory/guides/SESSION-KICKOFF.md` is 25590 LF-normalised bytes
against `manifest-check.sh:169`'s `MAX_MANIFEST_BYTES=25600`, ten under. The dark spelling is 27
bytes; 25617 is 17 over; `kickoff-manifest ratchet`, a §7 leg, reds on this unit's own commit, and
C7's remedy is "trimmed, not have the limit raised". The spec performed exactly this cap analysis
for `AGENTS.md` (9 under, so no dark spelling) and not for its sibling under the identical
constraint. AC5 pins the dark count at seven, so a builder cannot drop `:169` without redding AC5.
Unit 4's landing commit `0422ea2e` already met this cap ("144 bytes trimmed to stay under check 7's
25600"). A manifest BODY edit also owes `last-body-change` beside `last-audit` (C9's stall
baseline; `memory/gotchas` records that the stamps are not one stamp), and S4 step (4) and Files
touched name only `last-audit`. Finally S4 (dark spelling now) and Files touched (`:169 is
re-worded only at the flip`) disagree on the same line.

**Fix.** Split the predicate's yield by ROLE in S4 and list both sets. DoD carriers (`gate-env.sh:27`,
`kit.toml:125`, `:126`, `run-unattended-gates.sh:27`) take the dark spelling now and the flip at
step (4). The four pointers (`AGENTS.md:519`, `README.md:66`, `run-unattended-gates.sh:233`,
`SESSION-KICKOFF.md:169`) are named as byte-unchanged at BOTH steps with the reason — they already
state the post-flip fact — so the `:169` re-wording AND the `AGENTS.md:519` swap are withdrawn; the
charter's `On demand:` sentence is true after the flip and stays. `README.md` gains one ADDED line
naming the pooled DoD at the flip rather than losing the serial one. AC5's first half counts the
DoD set (four dark lines) and names the excluded four; `figure:` derives both; the ledger pastes
both lists. If a record of the flip is wanted in the manifest, add a NEW dated correction entry at
the flip, sized against C7 with the measurement pasted, and stamp `last-audit` AND
`last-body-change` in that commit. Make Files touched agree with S4.

**Left-shift gate.** The parity arm §10 parks in `govkit selfcheck`: every line in the tree matching
the DoD-phrase predicate (`GREEN verdict|not done until|DoD path|DoD command`) spells the SAME argv
as `kit.toml`'s block, and a line outside that predicate is not a carrier — an edit to one is a
finding, not a flip. Until built, two documented fold checks: a predicate that yields lines is
classified by role before ONE edit is applied to all of them; and every capped carrier a unit edits
carries its measured headroom beside the edit — `bash tools/check-template-size.sh AGENTS.md` for
the charter, `tr -d '\r' < memory/guides/SESSION-KICKOFF.md | wc -c` against C7 for the manifest.

## H2 · id=28 — the flip's post-state still promises a GREEN the spec says cannot occur

**Address:** section 2 S4 step (4) · section 8 F6 · section 4 Files touched.

F6 establishes that the driver exits 1 on a perfect pooled pass and that GREEN is therefore not the
criterion. Step (4) is a CLOSED list of flip edits: the seven dark lines drop `--serial`,
`kit.toml:126` becomes `--checks`, the block's binding sentence and `SESSION-KICKOFF.md:169` are
re-worded, `AGENTS.md:519` swaps eight bytes, `last-audit` is re-stamped. Verified at source, after
those edits `.githooks/gate-env.sh:26-27` still reads "the DoD for work touching a kit is a GREEN
verdict pasted into the landing report:" over a line that now spells `--selftests --pooled`, and
`tools/unattended/run-unattended-gates.sh:27` still reads "a GREEN verdict from
`run-unattended-gates.sh --selftests --pooled` pasted" — two carriers demanding the verdict F6
says the command cannot produce. The predicate never reaches two more lines that are false after the
flip: `run-unattended-gates.sh:187`, the runtime refusal text "`--serial` each suite alone, graded
against its budget — the recorded DoD path", printed to every operator who omits a mode; and
`tools/unattended/kit.toml:130`, "landed dark, named by no DoD command until the bound it inherits
is sound (`TOOL-aBatchedArm-5`)". And "drop `--serial`" from a line reading `--serial --pooled after
calibration` leaves `after calibration` inside an argv spelling.

**Fix.** State which of two shapes the flip takes. (a) Derive the flip set with a second predicate
over the DoD phrases (`GREEN verdict|DoD path|DoD command|landed dark|not done until`) beside the
spelling predicate, paste both hit lists classified in the ledger, and re-word every hit at the
flip with the criterion sentence; state the flipped spelling verbatim — `--pooled` alone, the marker
removed. (b) The smaller change, which is H3's fix: make the pooled exit derive from parity, so
GREEN IS the criterion again and F6 dissolves; then only the mode word changes on each carrier, and
`:187` and `:130` still owe their own one-line edits.

**Left-shift gate.** The `govkit selfcheck` parity arm of H1, which reads every carrier against
`kit.toml`'s block. Until built, the documented landing check: after the flip commit the DoD-phrase
predicate run over the tree returns zero lines naming `--serial` or `landed dark`, and the ledger
pastes that empty result.

## H3 · id=41 — the recorded post-flip DoD command prints RED on success, forever

**Address:** section 2 S4 (the flip commit and the re-worded binding sentence) · section 6 AC5
red-when · section 8 F6 · section 4 "Why the flip is the build's landing step".

Verified at source: `run-unattended-gates.sh:302-303` pipes the shared runner through `tee` and sets
`st=1` whenever `PIPESTATUS[0]` is non-zero; `run-selftests.sh`'s pooled branch sets `st=1` on any
FAIL rc (`:750`) and exits `st` (`:831`); eight of the fourteen rows exit 1 by design. So after the
flip the recorded DoD command prints `unattended gates RED` on a perfect pass, permanently — and its
own RED text at `:826-828` tells the operator to confirm with the serial re-run, the pass the flip
removes from the DoD. S1 only ADDS `killed` and `rc-mismatched` to the summary and changes no exit
status; §4 and F6 state that the driver exits 1 on a perfect pass and accept it; S4 says
`kit.toml`'s "not done until this prints GREEN" sentence is "re-worded to bind those two" without
saying the verdict word changes, and AC5's red-when does not cover the case. The tree has decided
this class: `tools/run-gates/ceiling-margin.txt`'s header (`TOOL-dRetiredFork-40`) records a verdict
that fires on a healthy run as "strictly worse than a loose bound", and unit 4 AC7 reds "the
recorded DoD command pointing at a refusal". The fold moved the LANDING criterion to summary tokens
and left the mechanism that grades every LATER kit-work DoD printing RED on parity — an
institutionalised ignored RED.

**Fix.** Make rc parity THE pooled verdict. Under `--pooled` with evidence present, a row whose rc
equals its calibrated rc renders `ok (rc <n> matched)` and the pooled `st` derives from `killed +
walled + unrun + rc-mismatched + soundness`; the kit runner's `st` then means parity and the DoD
sentence keeps "prints GREEN". Re-word the runner's usage line ("answers ONE question — did any
suite fail") to the parity question, and the RED-ambiguity text at `:826-828` so a parity red is
not told to confirm itself serially. Add the arm: a red-by-design fixture row with a matching
calibrated rc yields exit 0 under `--pooled`, a mismatching one exit 1 — observed RED first.
Failing that, spell the re-worded binding sentence's criterion in S4 and add to AC5's red-when:
"the sentence still says GREEN over a command that prints RED on parity". This fix is the lever
under H2 as well.

**Left-shift gate.** The arm above, in `run-selftests self-test`; plus the existing unit 4 AC7 arm
class extended — "the recorded DoD command's exit on a fixture whose every row matches its evidence
is 0" — so a DoD command that reds on a healthy pass reds the leg.

## H4 · id=39 — rc parity cannot witness completion for the eight red-by-design rows

**Address:** section 8 F6 · section 2 S4 step (3) · section 2 S2 (the reading witness) · section 3
Non-goals (the per-row FAIL-set oracle).

S2 records a reading for any row that "exited on its own: rc captured", and S1, S4 (3) and F6 make
rc parity plus `killed 0` the completion witness. For the eight shard rows the calibrated rc is 1
(21 `FAIL` lines, exit 1). A shard that crashes is also rc 1: `check-unattended.test.sh` runs under
`set -u`, so an unbound variable exits 1 at 0.3 s, and any fixture breakage that yields MORE `FAIL`
lines still exits 1. Both the calibrated rc and the graded rc can therefore come from a run that
never did the work, and `rc-mismatched 0` is satisfied by a crash for eight of the fourteen rows the
flip is licensed on. The serial-budget floor keeps such a run from LOWERING the bound, which is what
S1 says it is for; nothing flags it as a non-completion. The record that owns the oracle is the
build README ("The baseline is RED and is the oracle. Equivalence is the `FAIL` line set plus the
executed assertion count") and unit 3 AC6; the class is `memory/gotchas/ab-arm-never-did-the-work.md`
— assert a positive artifact of the work per arm — which §4 cites for the killed case and does not
apply to the crash case. §3's non-goal withholds a FAIL-set ORACLE in the runner, not a completion
witness. The positive artifact already exists and is not read: the shard prints `($n assertions
executed in $MODE against a floor of $FLOOR)` at `check-unattended.test.sh:3269` on every run, and
the pool files each suite's output under `$SWEEP_ROOT/<j>/out`.

**Fix.** Carry a cheap positive artifact beside rc in the evidence row — the `^FAIL` line count, or
the executed-assertion figure parsed from the filed output — captured at calibrate and compared at
grade, so parity is (rc, artifact); or at minimum, for a row whose calibrated rc is non-zero,
require the filed output to carry the suite's own floor line. Say in S3 that this widens the column
shape (eight fields) and `--check`'s grammar with it. Add the arm: a fixture row seeded rc 1 whose
graded run exits 1 in under a second is mismatched — observed RED first.

**Left-shift gate.** That arm, in `run-selftests self-test`. Until built, the documented fold check
the ab-arm gotcha already states: a witness over a row whose oracle is RED names a positive artifact
of the work, never the exit status alone.

## H5 · id=30, id=40 — the rc column is a side effect of which reading was slowest

**Address:** section 2 S2 (the `rc` column, lines 59-60) · section 2 S3 (`--reset <row>`, lines
68-70) · section 5 risks · section 8 F6.

S2 pins the `rc` column to "the rc of the reading that set the max" while seconds are monotone. So
a REPAIRED suite (rc 1 → 0, typically faster) never raises its row and keeps the stale rc through
every later `--calibrate`; it rc-mismatches on every graded pass until `--reset <row>`; and
conversely a calibrate that happens to set a new max while a suite is broken silently makes the
broken rc the baseline. S3 puts `--reset <row>` on "the same invocation" as `--pooled --calibrate`,
which S2 says runs EVERY row the invocation selects, and the runner's only filter is `--kit`
(`run-selftests.sh:116`) — so clearing one repaired row costs a whole-population calibrate, 20530 s
of serial budget for the fourteen unattended rows under the serial-sum wall. §5 risks states the
seconds direction ("never lowered except by `--reset`") and nothing about rc. The post-flip meaning
of a mismatch — whether an rc change in either direction blocks the DoD until a person resets — is
unstated. The class is `memory/gotchas/one-value-field-records-a-mixed-outcome.md` and
`TOOL-aCollapsedScan-9`'s "a ceiling that cries wolf gets ignored": a standing mismatch that is not
a regression, on the count the landing and every later kit-work DoD rest on.

**Fix.** Make the `rc` column the LATEST completed reading's rc — monotone binds seconds only — and
say so in S2 and in the file's header. Write the post-flip rule: a mismatch in either direction is a
decision, and the verdict names the acceptance (`--calibrate` to take the new rc, `--reset <row>` to
lower). Then either let `--reset <row>` narrow the calibrate to the reset rows (a reset row is
uncalibrated by construction, so the refusal has nothing to refuse) or state the full-population
cost in §5 risks as the price. Add the arm: a second calibrate with a LOWER reading and a DIFFERENT
rc updates rc and not seconds — observed RED first.

**Left-shift gate.** That arm, in `run-selftests self-test`. Until built, the documented fold check
from the gotcha: a one-value field that records a mixed outcome says which outcome it records, in
its own header.

## H6 · id=21, id=26 — the M6 fold keyed the evidence on a node the fixture cannot resolve

**Address:** section 2 S3 (the node rule) · section 4 Files touched (the fixture rebuild) · section
6 AC2 (the third clause) · section 6 AC9 (`the node is a registry tag`) · section 4 "Why the node
is the registry tag".

S3 makes the node the charter's §2 registry TAG — `GOV_NODE` when set, else `USERNAME`/`USER`
resolved against the registry table "the way `_resolve_node_tag` does", REFUSING by name when no row
matches — and `--check` grades "the node is a registry tag". Verified at source:
`drift_report.py:1790-1804` matches the user against rows of the charter file at the repo root
(`_CHARTER_CANDIDATES = ("AGENTS.md", "CLAUDE.md")` at `:1745`, or the project layer's `CHARTER`),
and returns `None` with no charter. `build_repo` (`run-selftests.test.sh:36-118`) copies ONLY the
runner into a bare `git init` and writes no charter and no table; no arm string in the suite sets
`GOV_NODE`, and `GOV_NODE` is set nowhere in the tree (its one reader is `derive-ceilings.py:180`).
Files touched enumerates the fixture seed's TOKEN dimension exhaustively — `pooled@2x1`,
`pooled@1x2`, the rows arms append — and says nothing about the node dimension. So at build time
every pooled, sweep and calibrate arm (AC1, AC3, AC7, AC9, the re-cut wall arms) either takes S3's
own refusal — no registry row — or the build defaults the node silently, the exact class S3 forbids;
every seeded evidence row has no node value that can match; and AC2's "a node that resolves to no
registry row refuses naming the user" has no fixture table to be non-matching against. The suite
reds on its first run and stays red until the fixture is redesigned, which the spec does not
describe. S3 also does not say where the shipped BASH runner reads the table: the §12 kit-literal
sub-claim in the finding does not hold — `run-gates.gov.test.sh:204` already spells
`CHARTER="$ROOT/AGENTS.md"` and the install-prefix gate bans `tools/<kit>/` literals, not root
files — but the source has to be named.

**Fix.** Files touched states how the fixture resolves a node, and names WHICH of the two shapes,
because they need different arm setups: either `build_repo` writes a charter stub (`AGENTS.md`)
carrying one registry row that maps the CURRENT user (`${USERNAME:-$USER}`) to a fixture tag, with
every seeded evidence row keyed on that tag; or every pooled arm exports `GOV_NODE=<tag>`. AC2's
third clause then stages the opposite — delete the row, or unset the variable. S3 states the
runner's table source (`$ROOT/AGENTS.md`, then `CLAUDE.md`, the precedent at
`run-gates.gov.test.sh:204`) and the row regex it reuses from `_resolve_node_tag`.

**Left-shift gate.** A positive arm in `run-selftests self-test`: a pooled verdict in the fixture
NAMES the fixture's tag in its "bounded by" line, so a runner that defaults the node silently reds
the arm rather than passing on a value nobody checked.

## H7 · id=20 — the only leg that observes the fixture ACs is already killed at its ceiling, and the growth is unbudgeted

**Address:** section 7 (`run-selftests self-test` as "the ONLY leg that executes the fixture arms")
· section 5 testing · section 4 Files touched.

Verified: `tools/gate-legs.json` declares `run-selftests self-test` at `ceiling: 300`;
`<git-dir>/gate-ledger.tsv` holds exactly one row for it, `300.333 fail`;
`<git-dir>/gate-logs/run-selftests_self-test.log` ends `exit 124` — killed at its own bound;
`tools/run-gates/ceiling-evidence.txt` carries no row for it; and `selftest-budgets.txt:102`
declares the suite at 60 s from a 28 s reading taken 2026-09-07, before the suite grew to 55 arms
(`SELFTEST_FLOOR=55` at `test.sh:31`) carrying 30 s, 5 s and 3 s sleep fixtures. §5 adds roughly
fifteen arms — two calibrates, each running every fixture row under a serial-sum wall, pooled wall
arms, the re-cut `SELFTEST_WALL=10` and `SELFTEST_WALL=5` arms — and §7's "floor to move: the
suite's own" is `SELFTEST_FLOOR`, the ARM-COUNT floor, not the ceiling. Files touched names neither
`gate-legs.json` nor the budget row. §7 makes this leg the ONLY witness for AC1, AC2, AC6, AC7,
AC8, AC9 and the fixture halves of AC3 and AC4 at the final `GATE_FULL=1 GATE_SELFTESTS=1` pass; a
repeat kill there leaves every fixture AC unobserved by a truncation — the `ab-arm` class §4 invokes
for the calibrate — and the landing pastes a verdict with no witness behind it. The charter's
cost-is-a-verdict rule is unaddressed at the spec's own witness.

**Fix.** Add `tools/gate-legs.json` and `tools/run-gates/selftest-budgets.txt:102` to Files touched.
The unit either re-declares the leg's ceiling with the reason beside it — one observed run of `bash
tools/run-gates/run-selftests.test.sh` at the DoR, its wall pasted — or sizes the new arms' sleeps
and seeds to stay under 300 s and asserts that with the leg's ledger row at the final pass; §7
states which. Either way the final pass's landing record pastes that ledger row beside the verdict.

**Left-shift gate.** The gate exists — the runner's ceiling and the `every held leg is budgeted,
every budget row resolves` leg already in §7 — and the defect is that the spec did not budget to it.
The documented DoR check: a spec that adds arms to a leg pastes that leg's LAST ledger row and its
declared ceiling beside the arm list, so a leg already at its bound is a DoR fact and not a
final-pass surprise.

---

# MEDIUM

## M1 · id=6 — `--reset <row>`, the one lowering path, has no acceptance criterion

**Address:** section 2 S3 (`--reset <row>`, and "Observed by AC4 and AC9") · section 6.

S3 makes `--reset <row>` the one lowering path, says it "prints as a decision", and closes with
"Observed by AC4 and AC9". AC4 observes `--rank` and the real-tree `pooled@` grep; AC9 observes
`--check` shape errors and the unparseable-file refusal; no AC in section 6 mentions `--reset`. The
attribution is false for that clause. The only act that can make a bound unsafe has an arm in §5
testing and no contract line a ledger can answer, and its stated constraint (the same invocation
as `--calibrate`) has no observed refusal.

**Fix.** Add to AC3, or as a new AC: `--pooled --calibrate --reset <row>` lowers exactly that row
and prints the decision; `--reset` off `--calibrate`, or naming a row the file lacks, refuses by
name; red when any other row moves or the reset runs silently. If H5's fix narrows the calibrate to
the reset rows, say so here.

**Left-shift gate.** The refusal arms above in `run-selftests self-test`, each observed RED first.
Documented fold check: every S-item clause that names a verb or flag names the AC that observes it,
and the AC's text contains the flag.

## M2 · id=7 — the absent-margin refusal has no arm and no red-when

**Address:** section 2 S1 (the `$HERE/ceiling-margin.txt` refusal) · section 5 testing · section 6
AC1 · section 4 "why it refuses in three places".

S1 says the runner refuses when `$HERE/ceiling-margin.txt` is absent and attributes S1 to AC1, AC2
and AC7. AC1 observes only the present-margin bound, and its red-when (a factor bound, no reading
named, a tiny reading) would not catch a silent zero-margin default. §5 testing enumerates its arms
"each observed RED first" and omits this refusal; §4's own list of the places the mode refuses names
three and not this one. The spec's each-refusal-observed-RED discipline is broken for exactly this
refusal, and an unobserved refusal silently becomes a default.

**Fix.** Add the absent-margin arm to section 5 testing and to §4's refusal list, and add to AC1's
red-when: "or a pooled run proceeds with the margin file absent".

**Left-shift gate.** That arm. Documented fold check: the count of refusals an S-item names equals
the count of refusal arms §5 lists, derived by grep for "refuses" over §2.

## M3 · id=9 — step (4)'s closed list leaves GREEN promises and marker prose behind

**Address:** section 2 S4 step (4).

The same defect as H2, filed against the step's wording: it re-words only `kit.toml`'s binding
sentence and `:169`, while `.githooks/gate-env.sh:26-27` and `run-unattended-gates.sh:27` also
carry the GREEN promise and are merely "dropped `--serial`" from, leaving "a GREEN verdict from
`--selftests --pooled`" — the verdict F6 says cannot occur — and leaving `after calibration` inside
the argv line.

**Fix.** H2's: enumerate the flip set by a second predicate and state the flipped spelling
verbatim. No separate fold is owed once H2 is folded.

**Left-shift gate.** As H2.

## M4 · id=35 — §10 still says the node falls back to a hostname

**Address:** section 10 (the second bullet, lines 442-444) versus section 2 S3 (lines 66-68).

Verified verbatim: §10's second bullet says the runner reuses `GOV_NODE` "with the hostname as the
fallback the script does not have", while S3 says the fallback is `USERNAME`/`USER` resolved
against the registry table, "never a hostname", §4 "Why the node is the registry tag" repeats it,
AC2 requires a refusal naming the user, and §10's fourth bullet names `_resolve_node_tag`. The spec
carries two answers to one question — a rev-3 leftover the M6 fold did not reach — and the stale one
is the defect M6 was folded to remove. A builder reading §10 implements it.

**Fix.** Re-word §10's second bullet to name the registry-tag fallback and drop the hostname
clause. Fold it with H6.

**Left-shift gate.** Documented fold check: a rev log that names a folded defect greps the whole
spec for the retired term (`hostname`) and pastes the zero.

## M5 · id=42 — the landing criterion's provenance cites the wrong AC

**Address:** section 2 S4 step (3) · section 8 F6.

Both fold sites cite "unit 3 AC11" for the fact that the eight shard rows are RED by design with
21 `FAIL` lines and exit 1. Unit 3's AC11 is the stranded-block floor arm ("that shard REDS its
floor"). The record that owns the fact is unit 3 AC6 ("the `FAIL` set across the eight shards is
identical to the unsharded `FAIL` set"), observed in unit 3's rev-8 log ("the eight `FAIL` sets
union to the unsharded 21 and are identical to BASE's 21"), and the build README's "The baseline is
RED and is the oracle". A reader verifying the basis of F6 lands on an arm about something else.

**Fix.** Re-point both cites to unit 3 AC6 and the README's build-level rule.

**Left-shift gate.** Documented fold check: a cite of the form `unit N ACk` is opened and the AC's
text contains the fact cited; a hygiene predicate could join the pair, and is not worth building for
one cite.

---

# LOW

## L1 · id=45 — "the three it already carries" is a typed count of a derived population, and it is four

**Address:** section 2 S3 (the `project-owned` rule).

`grep -c 'role = "project-owned"' tools/run-gates/kit.toml` is 4 at this base (lines 41, 57, 67,
77: the six self-test suites, the gov harness, `ceiling-evidence` plus `ceiling-margin`, and
`selftest-budgets`). No grouping of those by reason yields three. A stale figure beside the file
that owns it, the class the charter's §6 and §7 name.

**Fix.** Drop the number: "beside the project-owned rules it already carries".

**Left-shift gate.** The charter's rule already covers it; the documented fold check is a grep of
the spec for `the (two|three|four|five|six|seven|eight) it already` and `<n> of them` beside a file
path, each hit either derived at build time with a `figure:` or deleted.

---

## What the fold should do first

Ordered by leverage, not by severity: one decision under each defect repairs every row under it.

1. **Count every non-completion class in the landing witness (B1).** `killed`, `walled`, `unrun`
   and `rc-mismatched` on the summary line, from the lists the runner already keeps; carry the
   tokens into S4 (3), AC5 and F6; one word per class across S1 and S2.
2. **Wire rc parity to the pooled exit (H3), which dissolves H2 and M3.** GREEN means parity, the
   binding sentence keeps its word, `:187` and `:130` owe one line each. If the exit is NOT to
   change, say so and enumerate the flip set by the DoD-phrase predicate instead.
3. **Classify the carrier set by role (H1).** Four DoD carriers take the dark spelling and the
   flip; four pointers — `:169`, `:233`, `README.md:66`, `AGENTS.md:519` — are byte-unchanged at
   both steps, the `:169` re-wording and the `:519` swap withdrawn, the manifest's C7 headroom
   measured beside the charter's, both stamps named.
4. **Give the fixture a node (H6, M4).** A charter stub with one registry row, or `GOV_NODE` on
   every pooled arm; AC2 stages the opposite; §10's hostname clause deleted.
5. **Make the rc column the latest reading's and write the mismatch rule (H5, M1).** Monotone binds
   seconds only; a mismatch is a decision with a named acceptance; `--reset <row>` gets an AC and,
   if it narrows the calibrate, say so.
6. **Read a positive artifact beside rc for the red rows (H4).** The `^FAIL` count or the
   executed-assertion line, captured at calibrate.
7. **Budget the leg the fixture ACs live in (H7).** Paste its last ledger row at the DoR; re-declare
   the ceiling with a reason or size the arms under it; `gate-legs.json` and the budget row in
   Files touched.
8. **Add the absent-margin arm (M2), re-point the AC11 cites (M5), drop the count (L1).**

Once folded, a round 4 reads the fold; the loop re-armed at one blocker against two, and the
precision trend says to prime that round with these twelve defects as known and scope it to the
fold's diff.
