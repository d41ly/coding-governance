**Serves:** spec-audit TOOL-aBatchedArm-5

# Tier-2 spec audit — TOOL-aBatchedArm-5, ROUND 1

*Adversarial pre-code pass over the unit that replaces the pooled mode's `budget x
sweep-ceiling-factor` hang bound in `tools/run-gates/run-selftests.sh` with an evidence-derived one,
declares a `--pooled --calibrate` bootstrap, gives the runner its own tracked evidence file, and
re-points the DoD carriers from `--serial` to `--pooled`. Node `a`, 2026-09-14, ROUND 1. Every
finding below survived a skeptic prompted to REFUTE it, and every cited line, population and exit
status was re-read or re-run in the tree by the author of this report rather than transcribed from a
lens. Each row carries its address inside the spec, the fix, and the gate that would have caught it
before a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-5.md`@`a4047abf00b254c0bcb71fe01ef7ba9cbbbbb98a` — rev-2, never reviewed. rev-1 was corrected pre-audit by its author after a seam claim (readings in `ceiling-evidence.txt`) was verified false at source; that correction is the rev-2 log and is not re-graded here.

The four sibling units are NOT in scope. Units 3 and 4 are CLOSED at this spec's base `1c736fd9`
and their rows and modes are read here only as the tree this unit consumes. Where a row below names
one of them, it is because THIS unit's declaration about that sibling is wrong, not because the
sibling is being reviewed.

**Two owner rulings bind this build and were applied as facts, not findings.** 2026-09-13: a build
agent runs no self-test on every step, builds first and verifies once at the end. 2026-09-14: no gate
runs until every unit of the build is built. Every row that asks for an observation therefore asks
for it at the build's final gate pass or in the fixture, never mid-build. Nothing below asks the
builder to run a real row early.

## Verdict: BLOCKED

Three rows at BLOCKER, thirteen at HIGH, eleven at MEDIUM, one at LOW. Those twenty-eight rows
collapse to **eleven distinct defects**; the table below names which rows share one, so a fold that
repairs a defect repairs every row under it rather than twenty-eight separately.

Two of the eleven are enough on their own, and they compound. **The unit prices one population and
grades another** (D-1): AC3 calibrates "the real eight shard rows", but the command AC5 grades and
the carriers will name, `run-unattended-gates.sh --pooled`, delegates to
`run-selftests.sh --kit tools/unattended --pooled`, and that filter resolves to fourteen rows today
(`--list`, run for this report), six of which get no calibration under the spec's own cost line. S1
makes any uncalibrated row refuse the whole run, so AC5's GREEN is unreachable as written. And **the
flip is landed as text before the observation that is supposed to license it** (D-2): S4 calls it the
unit's LAST commit, but the evidence file it depends on is written only at the deferred final pass and
must be committed after, so "last" is false in fact; in the window between, every DoD carrier on
`main` names a command S1 refuses on every row — the exact state unit 4 AC7's red-when forbids by
name — and no line says what happens to the flipped carriers if that pass kills a row. The 2026-09-14
ruling defers the OBSERVATION; nothing in it orders the flip commit ahead of it.

Behind those two, the design has three open seams a builder would resolve four different ways: a
refusal and a fallback both stated for the same uncalibrated row (D-3); a run wall with no stated
derivation once the factor is gone, borrowing a profile wall the runner's own comment refuses and the
fixture does not contain (D-4); and a "reused rule" that drops the three parts of
`derive-ceilings.py` that make it self-correcting — ok-only readings, a raise on every write, and a
recorded lowering path (D-5). The rest is mechanical and each row carries its line number.

## Review shape

- raw 54 · confirmed 28 · refuted 26 · unverified 0 · precision 0.52

Precision at 0.52 sits just above the ~0.5 floor `AGENTS.md` §8 sets before tightening scope rather
than adding agents. The refuted half was mostly lenses re-deriving unit 4's already-closed rows or
reading rev-1's seam claim that rev-2 had already withdrawn, so the fan was scoped right for the
target and priming on the rev-2 log would raise the number next round. Read the confirmed count with
the table in hand: four lenses hit the population mismatch independently and five hit the reused
rule, which the pipeline reports as zero duplicates because each row addresses a different section.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty.

## The eleven defects, and which rows carry each

| Defect | Rows | Severity |
|---|---|---|
| D-1 · AC3 calibrates eight shard rows; AC5 and the flipped carriers grade the fourteen `--kit tools/unattended` rows; under S1 the DoD refuses and the cost line prices the wrong pass | id=13, id=42, id=1, id=32 | blocker ×2 / high / medium |
| D-2 · the flip lands as text before its licensing observation, "last commit" is false, the window names a refusal as the DoD, no revert on red, no merged-tree re-derivation | id=41, id=2, id=53 | blocker / high / medium |
| D-3 · S1/AC2 refuse an uncalibrated row; §3 non-goal 3 runs it at the inherited factor bound — two answers to one question | id=14, id=43 | high ×2 |
| D-4 · the run wall has no stated derivation once the factor is gone; S2 borrows the profile wall the runner refuses and the fixture lacks; the factor's fate is unstated | id=3, id=31, id=44 | high ×3 |
| D-5 · the reused RULE is reused in part: readings from FAIL and WALL rows count, a row is frozen at its first reading, no `--reset`, and node is a column rather than a key | id=18, id=29, id=30, id=45, id=48 | high ×4 / medium |
| D-6 · the runner's existing self-test does not survive S1: fixture rows have no evidence, no margin file and no `run-gates.sh`, and §7's floor assumes they do | id=27 | high |
| D-7 · AC4's `--rank exits 0` is red at the spec's own base for unit 3's DERIVED shard-8 reading, so its green certifies another unit's row | id=28, id=20 | high / medium |
| D-8 · "the four DoD carriers" is a typed count over a population a grep derives as eight lines in six files, and AC5's red-when contradicts S4's retained serial cost pass | id=5, id=50 | medium ×2 |
| D-9 · `tools/run-gates/kit.toml` ships the new evidence file to adopters under `include = "**"`, and Files touched omits it and the manifest re-stamp | id=11, id=22, id=36, id=47 | medium ×4 |
| D-10 · §7 is under-derived against unit 4's own rule: the guarded canaries, the lexicon leg and `unattended skill wiring` all fire on this unit's files | id=23 | medium |
| D-11 · the parse refusal is asserted and unobserved, and `--calibrate` beside any mode other than `--pooled` is unspecified | id=25 | low |

---

# BLOCKERS

## B1 · id=13 — AC3 calibrates eight rows; the command AC5 grades resolves to fourteen

**Address:** section 6 AC3 (`fixture:` and `cost:`) · section 6 AC5 · section 2 S1 and S2.

AC3 scopes its real-row calibration to "the real eight shard rows at the build's final gate pass,
which is also unit 3's AC4 arm two", and its `cost:` line prices "one pooled pass of the eight shard
rows". Unit 3's AC4 arm two filters on the one suite file, `check-unattended.test.sh`. AC5's witness
is `bash tools/unattended/run-unattended-gates.sh --pooled`, and verified at
`tools/unattended/run-unattended-gates.sh:302` that path delegates to
`run-selftests.sh --kit tools/unattended --pooled`. Run for this report, `--kit tools/unattended
--list` resolves fourteen rows: the eight shards plus `unattended adopter e2e`, `brief-recorded
selftest`, `cross-component`, `driver selftest`, `pass-order selftest` and `playbook selftest`,
declared total 20530 s. S1 says a row with no pooled observation REFUSES the pooled run naming
itself, and AC2 makes that refusal execute no suite.

So as written, after AC3's calibration the AC5 run refuses naming six rows and executes nothing.
The flip's own acceptance can never be observed, and the carriers name a refusal. The cost line is
also wrong for the pass it prices: the floor of the real pass is the longest row in the fourteen, and
that is `unattended driver selftest` at a 3860 s budget, not any shard.

**Fix.** S2 and AC3: the calibration population at the final pass is the DoD command's RESOLVED
population, derived at observation by `run-selftests.sh --kit tools/unattended --list`, never a typed
count; the invocation is `run-selftests.sh --kit tools/unattended --pooled --calibrate`. AC3's
`cost:` prices one pooled pass of that population with its longest row as the floor. AC5's second
half names the same derivation. Keep "eight" only where the spec cites unit 3's rows as a subset of
that reading.

**Left-shift gate.** A `--check` arm of `run-selftests.sh` that, for every `--kit` filter a carrier
names, lists the rows in that filter with no evidence row under the current condition token — so an
uncalibrated row in a DoD population is visible on the bar rather than at the first DoD run. Until
built, the documented fold check: every AC whose witness is a command names the same population as
the S item that prepares it, and a `cost:` line that counts rows cites the command that derives the
count.

## B2 · id=42 — the same defect, filed against the cost line and the fallback branch

**Address:** section 6 AC3 `fixture:`/`cost:` · section 6 AC5 · section 2 S2.

Same seam as B1, kept as its own row because it addresses what happens under EACH of the spec's two
answers for an uncalibrated row (see D-3). Under S1's refusal the first pooled DoD refuses naming six
rows and executes nothing. Under §3 non-goal 3's fallback those six run at `budget x 2`, and the
2026-09-08 full-sweep record's TSV slots 51-57 show that bound killing five of them — the very run
this unit exists to stop recording. "Eight" is additionally a count of a derived population typed in
prose, the defect charter §7 names, and it is the wrong count for the criterion it prices.

**Fix.** As B1. The unit-3 subset remains what unit 3's AC4 arm two reads; it is not the whole of
this unit's calibration.

**Left-shift gate.** As B1.

## B3 · id=41 — the flip lands as text before the observation that licenses it

**Address:** section 2 S4 · section 4 "Why the flip is last" · section 6 AC5 · section 5 migration.

S4 lands the carrier flip "as text" inside this unit and defers its observation, AC3's calibration
and AC5's green pass, to the build's final gate pass. The spec's own §4 says the re-pointing
"happens only after the bound that would grade it is the evidence one and has been seen green over
every row it will grade". Both cannot be true. The records this spec's rev-1 log claims as its source
say the same as §4: unit 4's round-2 B1 prescribed that this unit "flips the default as the last step
of its scope AFTER an observed non-killing run", and its left-shift rule says an S item moving a DoD
argv must "cite the last recorded run of the new argv, or declare land dark". Charter §1 lands risky
behaviour dark and flips it on only after in-place verification.

The window is concrete. After the flip commit, `.githooks/gate-env.sh`, `tools/unattended/kit.toml`,
`AGENTS.md` and the kit runner's header record `run-unattended-gates.sh --pooled` as the Definition
of Done while the last recorded run of that argv killed five of seven rows and the new bound has
passed only a stub fixture. Under S1 the command refuses on every row — "the recorded DoD command
pointing at a refusal", which unit 4 AC7 reds by name. §5 says the carriers are "reversible by one
line each" and nothing says a red final pass reverts them, so a red leaves a CLOSED unit with the flip
on `main` and no stated revert.

**Fix.** Sequence the flip after the pass that observes it. The carriers stay `--serial` (unit 4's
dark landing) until the build's final gate pass reads AC3 and AC5's second half green, and the
re-pointing commit is the build's landing step, ledgered as owed until then. If the flip must be
inside this unit's commits, it is `land dark` by unit 4 r2 B1's own rule: each carrier names both
spellings with the pooled one marked unverified until the pass — never a DoD line naming a command
with no passing run. Make §4's sentence true either way, and add to S4 the ordered landing lines: the
final pass runs calibrate; the evidence file is committed; `run-unattended-gates.sh --pooled` runs and
its GREEN is pasted; ONLY THEN the flip lands. On a red at the third step the carriers stay
`--serial`, AC5 is ledgered amended naming the red, and the unit does not close.

**Left-shift gate.** The `unattended skill wiring` leg already reads `kit.toml` and
`run-unattended-gates.sh`; extend it to resolve each DoD carrier's argv and assert the runner accepts
it past its refusal arms (a `--list` of the resolved population with every row evidenced), so a
carrier naming a refusing command reds on the bar. Until built, the documented check is unit 4 r2
B1's own rule: an S item moving a DoD argv cites the last recorded run of that argv or declares land
dark.

---

# HIGH

## H1 · id=1 — the population mismatch, filed against S2's calibration scope

**Address:** section 6 AC3 and AC5 · section 2 S2.

The B1 defect from the calibration side: AC3 pins its real-row calibration to unit 3 AC4 arm two,
whose invocation reaches only `check-unattended.test.sh`'s rows, while S1 and AC2 make every
unevidenced row in the DoD population refuse. The six non-shard rows have no calibration anywhere in
the spec. Worse, §3's third bullet says uncalibrated rows "keep their inherited bound", so the spec
never reckons with those six at all — it either refuses on them or runs them under the factor (D-3).

**Fix.** As B1: the calibration population is the kit runner's whole `--kit tools/unattended`
population, derived by `--list`.

**Left-shift gate.** As B1.

## H2 · id=2 — "the unit's LAST commit" is false, and nobody is named to commit the evidence

**Address:** section 2 S4 · section 4 "Why the flip is last" · section 5 migration.

S3 makes `selftest-pooled-evidence.txt` tracked and "written only by `--pooled --calibrate`". S4
defers that calibration to the final pass. So a commit of that file AFTER the flip commit is
mandatory, and "last" cannot hold. Nothing names who commits it, who re-ledgers AC3 and AC5 from
amended to observed, or what happens to the flipped carriers if the real pass kills a row. Verified
against unit 4 AC7 and the runner: in the gap, every carrier names a command S1 refuses on every row.

**Fix.** The ordered landing lines in B3's fix, written into S4. Alternatively land the carriers dark
(both lines, `--serial` as the DoD, `--pooled` as "after calibration") and flip in a follow-up
commit that the ledger owes.

**Left-shift gate.** As B3.

## H3 · id=14 — S1 refuses; §3 falls back; the builder cannot tell which survives

**Address:** section 2 S1 · section 6 AC2 · section 3 non-goal 3.

S1: a row with no pooled observation "REFUSES the pooled run naming itself, never falls back to a
factor". AC2's red case calls any fallback "a factor wearing a refusal's name". §3 non-goal 3: "every
other row keeps its inherited bound until someone calibrates it", and in this build's vocabulary the
inherited bound is `budget x sweep-ceiling-factor` (this spec's §1, unit 4 §3). A bare
`run-selftests.sh --pooled` — the `--sweep` alias every recorded invocation carries — reaches the
whole population, of which everything outside the fourteen is uncalibrated. It either refuses on the
first such row or runs it under the factor S1 forbids. Two different builds satisfy different
sections, and the builder cannot decide from the text whether the `sweep-ceiling-factor:` header
(`selftest-budgets.txt`), its refusal arm (`run-selftests.sh:490-495`) and the
`TIMEOUT ... at its <budget x factor>s bound` line (`:748`) survive.

**Fix.** Pick one and write it in S1. If refusal: delete §3's fallback sentence, say the
whole-population `--pooled`/`--sweep` refuses until calibrated naming the rows, and retire the factor
header and its arm. If fallback: rewrite S1 and AC2 so the refusal is per-row-with-no-evidence-AND-
no-factor, print `inherited bound` beside every such row so a kill under it is attributable, and drop
"never falls back".

**Left-shift gate.** One self-test arm exists for exactly one of the two behaviours over an
unevidenced fixture row; whichever the fold picks, the other is unreachable and the arm is its
witness. Documented fold check: a non-goal may withhold a behaviour, never define one an S item
already defines differently.

## H4 · id=43 — the same contradiction, against unit 4 r1 B5's "stated either way"

**Address:** section 2 S1 · section 6 AC2 · section 3 non-goal 3.

Same seam as H3, kept because it grades the spec against the record it claims to answer. Unit 4's
round-1 B5 fix asked for one behaviour for an uncalibrated row, "stated either way"; rev-2 states
both. AC2's red case is precisely what non-goal 3 licenses.

**Fix.** As H3.

**Left-shift gate.** As H3.

## H5 · id=3 — the run wall has no derivation once the per-row bound is evidence

**Address:** section 2 S1 and S2 (the run wall).

Verified in the runner. `SWEEP_FACTOR` is refused when absent at `:490-495`. `SWEEP_LARGEST` and the
run wall are both products of `budget * SWEEP_FACTOR` at `:507` and `:533-538`, the wall being
`ceil(sum / OUTER)` clamped to the largest per-suite bound. `SELFTEST_WALL` overrides at `:540-551`,
and `:555-560` exits 2 when the wall is below the largest bound. S1 replaces the per-row bound but
never says what the wall derives from afterwards, never mentions `sweep-ceiling-factor`, and never
mentions the wall-vs-largest invariant. A builder who keeps the factor-derived wall can have an
evidence bound (max reading plus `max(120, 1.0 x max)`) exceed it, so the runner either exits 2
forever or wall-kills a row inside its own bound — the "error, not a policy" the runner's own
comment names. A builder who drops the factor per "never falls back to a factor" has no wall at all.
S2's calibrate wall borrows `--print-profile`'s `wall`, which `:514-518` explicitly refuses to
borrow, without acknowledging the refusal. No AC observes any of these choices.

**Fix.** S1: the graded pooled run's wall is derived from the evidence bounds by the same shape,
`ceil(sum of bounds / OUTER)` floored at the largest bound. S2: name the calibrate wall's source (see
H7 for the two candidates) and say `SELFTEST_WALL` still overrides. Say whether
`sweep-ceiling-factor:` is deleted from `selftest-budgets.txt` or kept unread, and give AC1 a
`Red when` for a wall still derived from the factor.

**Left-shift gate.** The existing arm "a run wall BELOW the largest per-suite bound REFUSES" is the
witness for the invariant; the spec keeps it and adds its evidence-bound twin, staged RED with an
evidence row larger than the derived wall.

## H6 · id=31 — the same wall gap, against the fixture

**Address:** section 2 S1 and S2 (the whole-run wall) · section 6 AC3 `fixture:`.

Same seam as H5, filed against AC3's fixture arm. `build_repo` at `run-selftests.test.sh:36-40`
copies only the runner into a repo with no `run-gates.sh`, so `W` already falls back to 2 and no
`wall` row exists there. S2's "profile's whole-run wall" therefore does not resolve in the fixture,
and AC3's fixture arm has no wall to bound its rows with.

**Fix.** As H5 and H7.

**Left-shift gate.** As H5.

## H7 · id=44 — the calibrate wall is the borrow two records already refused

**Address:** section 2 S2 · section 4 "Why the bootstrap is a declared mode" · section 6 AC3 `fixture:`.

"Under the profile's whole-run wall only" is the borrow `TOOL-aPooledSweep-1` rev-3 (§4, F2) recorded
as wrong: the `--print-profile` wall sat below the population's largest per-suite bound and killed
clean sweeps, which is why `run-selftests.sh:514-518` derives its own. Unit 4's round-1 H1 then
prescribed the replacement — "an explicit `SELFTEST_WALL` that is REQUIRED for the calibration pass
and refused when unset" — and this spec neither adopts nor rebuts either record. With per-suite
bounds withheld under `--calibrate`, the existing `SELFTEST_WALL`-below-largest refusal compares
against nothing, so the calibration either runs unbounded (the state `TOOL-aPooledSweep-1` S7
forbids) or the builder invents a source.

**Fix.** S2 names the calibrate wall's source, one of two: `SELFTEST_WALL` REQUIRED for
`--calibrate` and refused when unset (H1's shape), or derived from the serial budgets — sum over
`OUTER`, floored at the largest serial budget, `TOOL-aPooledSweep-1` F2's derivation with the factor
dropped. AC3's fixture stages it; §7's new arm observes the unset-wall refusal RED.

**Left-shift gate.** A self-test arm: `--pooled --calibrate` with no resolvable wall REFUSES naming
`SELFTEST_WALL`, staged RED in the fixture, where no profile wall exists by construction.

## H8 · id=18 — a FAIL or WALL-killed calibration writes its truncation as evidence

**Address:** section 2 S2 · section 6 AC3 · section 2 S1's "reused as a rule" · section 4 "Why the bootstrap is a declared mode".

S1 reuses `derive-ceilings.py`'s rule. Verified at source, that rule's `read_runs`
(`derive-ceilings.py:90-104`) counts `ok` rows only, with the stated reason that "a leg that FAILED
may have failed fast". S2 and AC3 record "each row's reading" with no completion condition, name only
`OVER BUDGET` and `TIMEOUT` as withheld verdicts, and state neither whether a FAIL or WALL-killed
row's seconds become evidence nor the calibrate run's exit status. This is decisive here rather than
cosmetic: unit 3's rev-8 records all eight shards RED at base (the 21-FAIL set its §3 forbids
touching), so every shard exits non-zero today. Under the reused ok-only clause calibration writes no
shard reading and S1 refuses forever; under "each reading" a wall-killed row writes a truncated
maximum the next graded run bounds at roughly 2x a non-completion and kills. Two opposite builds
satisfy the text, and a calibrate run that exits 0 over a FAIL is the "calibration that looked like a
verdict" §4 calls the false-green shape.

**Fix.** S2 and AC3: a reading is recorded only for a suite that exited on its own — rc captured,
not killed by wall or bound, trailer present where the suite prints one; a row that did not writes
NO reading and is named; the calibrate run exits RED on any such row; the summary line is a shape the
kit runner's `sweep GREEN` / `WITHHELD` parser cannot mistake for a verdict. AC3's red case adds "a
non-ok row's seconds land in the file". State what calibration over the eight currently-RED shards
means for this unit's final pass, since unit 3's rows are red at base by its own record.

**Left-shift gate.** A self-test arm: a stub suite that exits non-zero under `--calibrate` leaves no
row in the evidence file and the run exits non-zero, staged RED first.

## H9 · id=29 — the same ok-only gap, filed against the permanence of a bad first reading

**Address:** section 2 S2 · section 6 AC3 · section 5 risks.

Same seam as H8 with its consequence spelled: a fail-fast first reading plus `max(120, 1.0 x max)`
sets a bound of roughly 2x a truncated run, the next healthy run is killed at it, and with no
re-observation path (H10) the bad bound is permanent — the opposite of §5's "errs toward not
killing".

**Fix.** As H8, plus H10's raise path.

**Left-shift gate.** As H8.

## H10 · id=30 — no second observation exists, so "raising an existing row only upward" can never fire

**Address:** section 2 S2 versus section 6 AC3 and section 5 risks · section 2 S3.

S2's calibrate "runs rows that have no pooled observation". S3 says the file is "written only by
`--pooled --calibrate`". Graded `--pooled` writes nothing and no `--reset` exists. Yet AC3 says
"raising an existing row only upward" and §5 says a loose bound holds "until re-observed". Neither
can happen under S2 and S3 as written: a row's first reading is its bound forever, and hand-editing
a "written only by" file is the only remedy. A quiet-box first reading plus the 1.0 fraction is 2x
headroom, which the sweep record's 3-15x dilation exceeds.

**Fix.** Pick one and state it: `--calibrate` runs every row `--kit` selects, evidenced or not, and
raises monotone (delete "that have no pooled observation" from S2); or graded `--pooled` appends its
rc 0 readings monotone the way `derive-ceilings.py --write` does on every bar. Then AC3's raise
clause has a fixture arm.

**Left-shift gate.** A self-test arm: a second calibrate over an evidenced fixture row with a lower
reading leaves the max intact; a higher one raises it; staged RED first.

## H11 · id=45 — the reused RULE is missing the three parts that make it self-correcting

**Address:** section 2 S1, S2, S3 · section 5 risks · section 6 AC3.

The defect D-5 whole, verified at source. (a) `read_runs` skips every row whose status is not `ok`;
S2 records "each row's reading" under the wall with no completion witness, so a wall-killed shard
writes its kill time as evidence, which unit 3 AC4's trailer rule and
`memory/gotchas/ab-arm-never-did-the-work.md` define as NO READING. (b) every `--write` folds in
every new reading and raises; S3's "written only by `--calibrate`" over S2's "rows with no
observation" freezes a row at its first reading. (c) `derive-ceilings.py` has `--reset <leg>` as the
recorded lowering path (`:173`, `:205`, `:270`); S3 has none, so §5's "loose bound until re-observed"
has neither a re-observation nor a reset. The consequence is `TOOL-dRetiredFork-40`'s class: a graded
`--pooled` kill on a busier day (`TOOL-aSurfacedLexicon-22` measured one leg at 267 s clean and
killed at 5400 s under contention) can never raise the row, and "a bound that fires on normal
concurrent execution teaches everyone to ignore the verdict".

**Fix.** The three parts, in S1-S3: a reading is recorded only for a suite that exited on its own;
`--calibrate` runs EVERY row in the population and raises monotone; `--reset <row>` is the one
lowering spelling, recorded as a decision somebody made. Then the "reused as a rule" claim is true.

**Left-shift gate.** The H8 and H10 arms, plus a `--check` over the evidence file asserting every
row's max is the max of its readings and its readings count is at least one — a hand-edited or
truncated row reds on the bar.

## H12 · id=27 — the runner's existing self-test does not survive S1

**Address:** section 2 S1 · section 7 · section 6 AC1 `fixture:`.

Verified: `build_repo` (`run-selftests.test.sh:36-40`) copies only `run-selftests.sh` into the
fixture — no `run-gates.sh` (so `W` falls back to 2), no `ceiling-margin.txt`, no evidence file — and
a grep for `--sweep`/`--pooled` over the test file lands on 44 lines, the arms over the fixture rows
`held one` and `free one`, which carry no pooled evidence. Under S1 ("a row with NO pooled observation
REFUSES") and S1's "the file refuses when absent", those arms red as written, and the `run wall 140s`
and TIMEOUT arms (a 1 s budget, a 2 s bound, a 3 s sleep) assert the factor-derived shape S1 removes.
With the real margin's 120 s floor, that TIMEOUT arm would need a 120 s-plus sleep inside a leg
whose ceiling is 300 s. §7's "floor to move: up by the arms added" and AC1's "fixture with one staged
evidence row" both assume the existing suite survives untouched; it does not, and the fixture
rebuild is nowhere in the spec.

**Fix.** State in S1 or §7 that `build_repo` gains a fixture `ceiling-margin.txt` with a small floor
and an evidence file seeded for every fixture row under the fixture's own condition token(s),
CAPTURED from a run the way the fixture's own generated `roundtrip.sh` stub
(`run-selftests.test.sh:85-87`) already captures the runner's condition tag into a budget row — two
tokens exist there, the `W=2` default and the `SELFTEST_OUTER_WIDTH=1` arms — never typed; and that
the two factor-shape arms are rewritten to the evidence shape. Re-derive §7's floor from that.

**Left-shift gate.** The `run-selftests self-test` leg, guarded on the runner, is the gate and it
reds on the first build; the left-shift is at spec time — a documented fold check that a spec
introducing a refusal greps the fixture for the rows the refusal reaches and prices their rebuild in
§7.

## H13 · id=28 — AC4's `--rank exits 0` is red at the spec's own base, for another unit's row

**Address:** section 6 AC4.

Reproduced for this report: `run-selftests.sh --rank` exits 1 at HEAD `88dcf88a` and at base
`1c736fd9`, because `unattended gate selftest shard 8/8`'s fourth column
(`selftest-budgets.txt:121`) reads "DERIVED, not measured …", which no CONDS regex matches. That row
is unit 3's, re-measured at the final gate pass per its rev-8. AC4 asserts exit 0 and its red-when
says a refusal "means a pooled reading leaked into the budget file", which is false at base. Unlike
AC3 and AC5, AC4 is not deferred to the final pass, so its green arm is unobservable inside this unit
and its red case is indistinguishable from the refusal already firing for an unrelated row. Only the
grep half, "no `pooled@` token", observes this unit's claim.

**Fix.** Make the witness the thing S3 actually claims: in the fixture, `--rank` exits 0 after a
calibrate run; on the real tree, `grep -c 'pooled@' tools/run-gates/selftest-budgets.txt` is 0 and
`--rank`'s unbacked list after calibration equals the list before it. Note that exit 0 arrives only
with unit 3's shard-8 reading, an ordering the spec does not state today.

**Left-shift gate.** A documented DoR check the witness rule already implies: every AC witness on the
real tree is RUN once at spec time at the spec's base, and one that is red for a reason outside the
unit is rewritten before the spec is audited.

---

# MEDIUM

## M1 · id=32 — the cost and "longest row" lines price the wrong population

**Address:** section 6 AC3 and AC5 (cost and fixture lines).

The D-1 defect, filed against the figures. The fourteen-row filter's longest row is
`unattended driver selftest` at a 3860 s budget, longer than any shard; AC3's "one pooled pass of
the eight shard rows" and AC5's "longest row inside its evidence bound" both name the eight-row
population. The finder's "25-40 min" figure for eight rows is not in the spec's cost line; the
population mismatch stands without it.

**Fix.** As B1: the population is "every row `--kit tools/unattended` selects, read from `--list`",
and the cost line derives from that set.

**Left-shift gate.** As B1.

## M2 · id=53 — nothing re-derives the bound on the MERGED tree

**Address:** section 2 S4 · section 6 AC5 (the landing).

`TOOL-aLoosenedCeiling-3` (`memory/DECISIONS.md:82`) rules that a ceiling is re-derived on the
MERGED tree, never carried from a base the merge superseded, and `tools/install-prefix-carried.txt`
records `main` adding a seventh unattended suite at a previous landing merge. The evidence bound is a
ceiling. S4 pins AC3's calibration and AC5's green to the pre-merge final pass; the spec says nothing
about the merged tree. A row arriving from `main` has no evidence, so the first post-merge DoD run —
the one the carriers now name — refuses (or under §3's fallback runs at the killed bound), and the
recorded green covers a population the merge superseded.

**Fix.** S4 states that the calibration and AC5's second half are re-taken on the merged tree before
the push, per `TOOL-aLoosenedCeiling-3`, and that a refusal there blocks the landing rather than the
push proceeding on the pre-merge green.

**Left-shift gate.** The B3 gate on the wiring leg, which runs on the merged tree at the push
boundary by construction.

## M3 · id=20 — AC4's exit-0 half depends on an ordering the spec does not state

**Address:** section 6 AC4.

Same seam as H13, filed against the dependency: AC4's green arrives only when unit 3's owed serial
re-measurement of shard 8 lands first, and a green then certifies that row rather than this unit's
claim.

**Fix.** As H13.

**Left-shift gate.** As H13.

## M4 · id=5 — "the four DoD carriers" is a typed count, and AC5's red-when reds the intended end state

**Address:** section 2 S4 · section 6 AC5 · section 4 Files touched.

S4 cites "the four DoD carriers `TOOL-aBatchedArm-4` S6 names". Unit 4 S6 contains no count of
four: it lists kit-runner sites in six files (`run-unattended-gates.sh:26-27` and `:203`,
`gate-env.sh:27`, `kit.toml:125-126`, `AGENTS.md:519`, `README.md:66`, `SESSION-KICKOFF.md:168-169`).
"Four" comes only from unit 4's AC7 (four files, six line sites). A grep for `--serial` beside the
kit runner over the tree today lands on eight lines in six files: `.githooks/gate-env.sh:27`,
`AGENTS.md:519`, `tools/unattended/kit.toml:125` and `:126`, `run-unattended-gates.sh:27` and
`:233`, `tools/unattended/README.md:66`, `memory/guides/SESSION-KICKOFF.md:169`. An observer
following the cite cannot determine which lines AC5 grades. And AC5's red-when, "any carrier still
names `--serial`", reds S4's own retained `--selftests --serial` cost pass, so the intended end state
is red by the criterion's own clause.

**Fix.** S4 enumerates the flipped lines by `path:line`, derived by the grep at fold time, and names
the ONE line that carries `--selftests --serial` as the declared cost pass (and where, since
`AGENTS.md` sits at its charter-size cap). AC5's red-when becomes "any enumerated DoD line names
`--serial`, or no line declares the serial cost pass".

**Left-shift gate.** A parity arm in the `unattended skill wiring` leg: every line naming
`run-unattended-gates.sh` beside a mode spells the DoD mode, except exactly one line declared as the
cost pass — the shape `tools/check-playbook-parity.sh` already uses for retyped constants.

## M5 · id=50 — the teaching sites and the owner's correction entry keep `--serial` after the flip

**Address:** section 2 S4 · section 4 Files touched · section 6 AC5.

Same seam as M4, filed against the two sites the flip leaves behind. After the flip `AGENTS.md:519`
reads `--pooled` while `tools/unattended/README.md:66` still reads
`--serial # the kit's self-tests, ON DEMAND ONLY`, and `memory/guides/SESSION-KICKOFF.md:169` — the
owner's standing instruction of 2026-08-23, recorded as a correction entry that OVERRIDES stale doc
claims by its own semantics — names only `--serial`. Two answers to one question, with the correction
entry outranking the carriers. Unit 4's round-2 B1 left-shift requires every carrier listed in Files
touched by grepping the basename; the spec substitutes a count.

**Fix.** Files touched and AC5 enumerate the carriers by the grep; the SESSION-KICKOFF correction
entry is re-worded to the mode the DoD now names, in the same commit, with its `last-audit`
re-stamped (M8).

**Left-shift gate.** As M4.

## M6 · id=11 — the new evidence file ships to every adopter of the run-gates kit

**Address:** section 4 Files touched (estimate) · section 2 S3.

Verified: `tools/run-gates/kit.toml:18-19` is `include = "**"`, role `engine`, and
`ceiling-evidence.txt`, `ceiling-margin.txt` (`:66-67`) and `selftest-budgets.txt` (`:76-77`) are
withheld only by explicit `project-owned` rules whose comments name exactly this defect: this node's
readings of gov's own rows are a population an adopter does not have. A new tracked
`selftest-pooled-evidence.txt` under that directory ships by default via `govkit apply`. Files
touched omits `kit.toml` and never mentions withholding, while reasoning carefully about the
install-prefix carry for the same file. No gate reds on an over-shipped data file. The finder's
second half — a `tools/`-prefixed literal in the runner — is refuted: the runner derives sibling
paths as `$HERE/...` and §7 lists the install-prefix leg that would red one; the `kit.toml`
omission alone is real and unguarded.

**Fix.** Files touched adds `tools/run-gates/kit.toml` with one
`[[files]] include = ["selftest-pooled-evidence.txt"] role = "project-owned"` rule citing the same
gotcha its siblings cite, `memory/gotchas/pin-copied-from-another-corpus.md`; name which AC observes
it or mark it NOT OBSERVED with the reason.

**Left-shift gate.** A descriptor lint in the govkit registry check: every tracked `.txt` beside a
kit's runner must be named by an explicit rule, so a `**` pool never absorbs a data file silently.
Charter §7 already requires the shipped population to be DECLARED; this is the arm that makes a new
file under `**` a declaration rather than a default.

## M7 · id=36 — the same over-ship, filed against the descriptor's own comments

**Address:** section 4 Files touched.

Same seam as M6, kept because the finder verified the sibling rules' stated reasons independently:
each of the three `project-owned` carve-outs exists because the file holds THIS repo's readings taken
on this node, which is exactly `selftest-pooled-evidence.txt`'s class.

**Fix.** As M6.

**Left-shift gate.** As M6.

## M8 · id=22 — Files touched omits `kit.toml` and the manifest re-stamp §7's own leg needs

**Address:** section 4 Files touched · section 7 Gates.

Two omissions, both verified. First, the M6 over-ship. Second, `tools/run-gates/run-selftests.sh` is
on `memory/guides/SESSION-KICKOFF.md`'s `watch:` line (`:6`), and `manifest-check.sh` check 5 reds
a staged change to a watched file with no `last-audit` re-stamp — so the `kickoff-manifest ratchet`
leg §7 lists reds on the files-touched set as written. Unit 4 S6 handled the same by editing the
manifest in the same commit; this spec lists the leg and omits the file.

**Fix.** Files touched adds `tools/run-gates/kit.toml` (the M6 rule) and
`memory/guides/SESSION-KICKOFF.md` (the re-stamp, and the M5 re-wording).

**Left-shift gate.** The ratchet leg is the gate; the left-shift is documented — a spec that touches
a `watch:`ed file lists the manifest in Files touched.

## M9 · id=47 — the same over-ship, filed against the install-prefix reasoning

**Address:** section 2 S3 · section 4 Files touched (estimate).

Same seam as M6, kept because it names the asymmetry: Files touched reasons about
`install-prefix-carried.txt` for a file whose rows name row names and need no carry, and omits the
descriptor that actually decides where the file goes.

**Fix.** As M6.

**Left-shift gate.** As M6.

## M10 · id=48 — the key is (row, token) and node is a column; the consumed record says node is a condition

**Address:** section 2 S3 (the key) · section 2 S1.

S3 keys rows per (row name, condition token) with node as data, and the file is tracked so it
travels. Unit 3's rev-8 — a consumes-from edge — recorded a checker invocation at 47-60 s on node
`a` against roughly 2 s on the host `TOOL-aTracedSpawn-2` records, and said the 20-minute target "is
a node d question". That spread a `max(120, 1.0 x max)` headroom cannot absorb. §3 non-goal 2
withholds the HOST's load condition, not node identity, which the runner already knows and already
writes. §5's "errs toward not killing" holds only within one node: a fast node calibrating a row
first leaves the slow node with an observed row that S2's `--calibrate` skips and `--pooled` kills at
roughly 2x the fast reading, with no raise path (H11).

**Fix.** Key the evidence on (row, token, node) with `GOV_NODE` as the node — `derive-ceilings.py`'s
own spelling — so refusal and calibration are per node; or fold the node into the token.

**Left-shift gate.** A self-test arm: an evidence row under another node's key does not satisfy this
node's `--pooled`, staged RED with a fixture row keyed to a foreign node.

## M11 · id=23 — §7 is under-derived against unit 4's own rule over the same files

**Address:** section 7 leg line, against `TOOL-aBatchedArm-4` section 7.

Unit 4 derived its leg line over the same two runner files by the rule "every leg whose guard covers
a touched path" and listed `run-gates canary`, `run-gates gov canary` and
`lexicon naming predicates`. Verified in `tools/gate-legs.json`: `run-gates canary` (guard `tools/`),
`run-gates gov canary` (guard `tools/run-gates/`) and `lexicon naming predicates` (guard `tools/`,
grades every touched `.sh`) all fire on this unit's files, and S4's carriers also wake
`unattended skill wiring`, which reads `kit.toml` and `run-unattended-gates.sh`. This spec lists none
of them. Under the ruling that defers every gate to the final pass, §7 is what the ledger records as
owed, so an under-derived list is wrong rather than terse.

**Fix.** Re-derive §7 by unit 4's stated rule over this unit's Files touched (after M6 and M8 add
theirs) and list the guarded legs it yields.

**Left-shift gate.** A small derivation over `tools/gate-legs.json` — touched paths in, guarded legs
out — that a spec-audit can run and a fold can paste; documented until built.

---

# LOW

## L1 · id=25 — the parse refusal is unobserved, and `--calibrate` beside other modes is unspecified

**Address:** section 5 error states against sections 6 and 7 · section 2 S2 against `TOOL-aBatchedArm-4` S2's grammar.

§5 asserts "an evidence file that will not parse refuses rather than defaulting"; §5 testing and §7
name exactly three arms and none is that refusal, in a suite whose own header says it holds "the
failing case for every refusal `run-selftests.sh` carries". And S2 defines `--calibrate` only as
`--pooled --calibrate` under a grammar (unit 4 S2) where the mode is a declared positional;
`--serial --calibrate`, `--check --calibrate` and bare `--calibrate` are unspecified in a runner
whose whole design refuses undeclared shapes, so a builder invents the answer, and a
`--serial --calibrate` that runs the serial loop and writes nothing is a silent path in a mode whose
point is announcing itself.

**Fix.** Add the unparseable-file refusal to §7's `New arm` list with its staged break, and one S2
sentence: `--calibrate` with any mode or verb other than `--pooled` REFUSES naming the pair.

**Left-shift gate.** The two arms named in the fix; the second is one case in the runner's existing
mode-refusal arm.

---

## What a fold should do first

Four decisions precede any redraft, and each is a scope call rather than a wording one.

1. **Which population the unit calibrates and grades** (B1, B2, H1, M1). The DoD command resolves
   to `--kit tools/unattended`, fourteen rows today and derived by `--list`, never typed. Every
   `cost:` line, the "longest row" clause and S2's calibration scope follow from that one sentence.
2. **When the flip lands** (B3, H2, M2). Either the carriers stay `--serial` until the final pass is
   green and the flip is the build's landing step, ledgered as owed; or the flip is inside this unit
   as `land dark`, both spellings on each carrier with the pooled one marked unverified. Either way
   §4's "only after … seen green" becomes true, the landing lines are ordered in S4, a red at the
   real pass has a stated outcome, and the merged-tree re-derivation is named.
3. **One answer for an uncalibrated row, and what the wall becomes** (H3-H7). Refuse or fall back,
   stated once, with the factor header and its arm retired or kept accordingly; the graded wall
   derived from the evidence bounds by the existing shape; the calibrate wall from `SELFTEST_WALL`
   or the serial budgets, never the profile row the runner refuses and the fixture lacks.
4. **The rule reused whole** (H8-H11, M10). Ok-only readings with a RED calibrate on any other,
   every row in the population raised monotone on every calibrate, `--reset <row>` as the lowering
   path, and the node in the key. With those, "reused as a rule" is a true sentence and §5's
   "errs toward not killing" holds across nodes.

After those, the mechanical set — the fixture rebuild and its two factor-shape arms (H12), AC4's
witness (H13, M3), the carrier enumeration and the one declared cost line (M4, M5), the `kit.toml`
rule and the manifest re-stamp (M6-M9), the re-derived §7 (M11) and the two L1 arms — is a single
pass over S1-S4, §4 Files touched, §6 and §7, each with a line number already in hand. The base need
not move: `1c736fd9` still holds units 3 and 4 CLOSED and the eight rows present, and nothing here
asks for an observation before the final gate pass the two rulings name.
