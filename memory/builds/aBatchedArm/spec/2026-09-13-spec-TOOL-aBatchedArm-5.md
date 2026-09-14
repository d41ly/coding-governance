# TOOL-aBatchedArm-5 — the evidence-derived pooled hang bound, and the flip

**Status:** OPEN · rev-3 · 2026-09-14 · node a · Tier-2 · base 1c736fd9 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`--pooled` exists (`TOOL-aBatchedArm-4`) and the eight shard rows exist (`TOOL-aBatchedArm-3`), and
the pooled run still bounds every row at `budget x sweep-ceiling-factor` — the shape that killed 14
of 58 suites in the full sweep of 2026-09-08 and that three records refused as a predictor. Replace
that bound with the evidence RULE the tree already owns, in the runner's own evidence file, with a
declared calibration mode that grades nothing; and land the DoD flip DARK, so the carriers move to
`--pooled` only as the build's landing step, after the final gate pass has seen the new bound green
over the population those carriers actually name.

## 2. Scope (IN)

- **S1** — a pooled row's HANG bound is derived from OBSERVED pooled readings, not from its serial
  budget: the worst reading recorded under this node and the runner's own condition token
  (`pooled@<outer>x<inner>` at the text `SWEEP_CONDITION=`), monotone, plus
  `tools/run-gates/ceiling-margin.txt`'s headroom of `max(<floor>, <fraction> x max)` READ from that
  file beside the runner (`$HERE/ceiling-margin.txt`; the runner refuses when it is absent — the
  same refusal `derive-ceilings.py` makes, reused as a rule and not imported, because the runner is
  bash). **A row with NO reading under (row, token, node) REFUSES the pooled run naming the row,
  the token and `--calibrate`, and executes no suite — the whole population `--pooled` or `--sweep`
  reaches, not only the filtered one.** There is no fallback: the `sweep-ceiling-factor:` header in
  `selftest-budgets.txt`, its refusal arm at the text `declares no sweep-ceiling-factor`, and the
  `at its <budget x factor>s bound` verdict text are RETIRED in the same commit, so no factor-derived
  bound survives to be fallen back on. **The graded run's WALL** is derived from the evidence bounds
  by the shape the runner already uses for the factor: `ceil(sum of bounds / OUTER)`, floored at the
  largest bound; `SELFTEST_WALL` still overrides and the existing below-the-largest refusal compares
  against the largest evidence bound. Every pooled verdict prints the reading, token, node and date
  it was bounded by. Observed by **AC1**, **AC2** and **AC7**.
- **S2** — the bootstrap is DECLARED: `--pooled --calibrate` runs EVERY row the invocation selects
  (bare, or `--kit <dir>`), evidenced or not, under a wall derived from the SERIAL budgets —
  `ceil(sum of serial budgets / OUTER)`, floored at the largest serial budget, `SELFTEST_WALL`
  overriding — and under no per-row bound. It withholds every verdict, and it records a reading ONLY
  for a row that exited on its own: rc captured, not killed by the wall, the rc written beside the
  seconds. A row the wall killed writes NO reading, is named, and makes the calibrate run exit RED.
  Every reading raises its (row, token, node) row monotone — never lowers it — and the summary line
  is `calibrated <n> row(s), graded none` on green and `calibrated <n> row(s), <k> killed, graded
  none` on red, neither of which the kit runner's `sweep GREEN` / `WITHHELD` parser can read as a
  verdict. `--calibrate` with any verb or mode other than `--pooled` REFUSES naming the pair.
  Observed by **AC3** and **AC8**.
- **S3** — pooled readings live in their OWN tracked file, `tools/run-gates/selftest-pooled-evidence.txt`,
  one row per (row name, condition token, node): `<row>\t<condition>\t<node>\t<max seconds>\t<rc>\t<readings>\t<date>`,
  node being `GOV_NODE` when set and the hostname otherwise, written by `--pooled --calibrate` and
  lowered only by `--reset <row>` on the same invocation, which is a decision somebody made and
  prints as one. The file's SHAPE is graded by `run-selftests.sh --check`, the unguarded bar leg:
  every non-comment line has seven tab fields, seconds and readings parse, readings is at least
  one, no (row, token, node) key repeats, and every row names a row the budget file declares — a
  hand-edited or truncated row reds on the bar. It ships to no adopter: `tools/run-gates/kit.toml`
  gains a `project-owned` rule for it beside the three it already carries for the same reason.
  NOT in `ceiling-evidence.txt` (generated from bar leg files, no condition column, `Do not
  hand-edit`, stale-row note on every bar for a row naming no leg) and NOT in
  `selftest-budgets.txt`'s fourth column, so `--rank`'s refusal of `pooled@` readings
  (`TOOL-aQuenchedHarness-6` S3a) is untouched and shard budgets stay serial. Observed by **AC4**
  and **AC9**.
- **S4** — the flip lands DARK, and the population it grades is DERIVED. The DoD carriers stay
  `--serial` inside this unit. The carrier set is the grep at fold time for `run-unattended-gates.sh`
  beside `--serial`, eight lines in six files at this base: `.githooks/gate-env.sh:27`,
  `AGENTS.md:519`, `tools/unattended/kit.toml:125` and `:126`, `tools/unattended/README.md:66`,
  `tools/unattended/run-unattended-gates.sh:27` and `:233`, and `memory/guides/SESSION-KICKOFF.md:169`
  (the owner's 2026-08-23 correction entry, which outranks the others by its own semantics and is
  re-worded in the same commit as the flip). Inside this unit each of those lines gains, beside
  `--serial`, the words `--pooled after calibration`, so the pooled path is named and marked
  unverified — `land dark`, unit 4 r2 B1's own rule — and one line, `kit.toml:126`'s
  `--all --serial`, is declared the cost pass and keeps `--serial` after the flip. **The flip itself
  is the BUILD's landing step, not this unit's**, in this order on the MERGED tree
  (`TOOL-aLoosenedCeiling-3`: a ceiling is re-derived on the merged tree, never carried): the final
  gate pass runs `run-selftests.sh --kit tools/unattended --pooled --calibrate` over the population
  `run-selftests.sh --kit tools/unattended --list` resolves (fourteen rows at this base, and that is
  the list's number, not this spec's); the evidence file is committed; `run-unattended-gates.sh
  --pooled` runs and its GREEN is pasted; ONLY THEN the seven DoD lines drop `--serial` for
  `--pooled` and the cost line stays. On a red at the third step the carriers stay `--serial`, AC5
  is ledgered amended naming the red, and the build lands without the flip. Observed by **AC5** and
  **AC6**.

## 3. Non-goals (OUT)

- **A contention model that makes a pooled COST verdict sound.** Still withheld under `--pooled`.
  The evidence bound is a HANG bound; it says when a run has stopped answering, never what it cost.
- **Observing the host's LOAD.** `pooled@8x1` names a width and a node, not whether another
  worktree's bar is running. Taking the turnstile or recording beacon state is named and not built;
  the evidence shape tolerates it by being monotone over whatever was observed, and `--calibrate`
  re-run on a loaded day raises the row rather than being refused.
- **Calibrating any row outside the population the DoD command resolves.** A bare `--pooled` over
  the whole declaration refuses until every row it reaches is calibrated, by name; nobody is
  obliged to calibrate them by this unit, and the refusal is the announced-unarmed state. The count
  of those rows is the budget file's to report.
- **Deciding the arity or the 20-minute question.** Unit 3's AC4 arm two is read at the same final
  pass; this unit's bound grades whatever that reading is.

### Edges

- **consumes-from** `TOOL-aBatchedArm-4` — the `--pooled` mode, the kit runner's pooled path, and
  the carriers it landed dark.
- **consumes-from** `TOOL-aBatchedArm-3` — the eight shard rows, part of the population this unit's
  S2 calibrates at the final pass.
- **hands-off** `none`

## 4. Design

### Why the evidence shape and not a factor

Three records and one measurement. `TOOL-dRetiredFork-40` measured 443 s under load against 583 s
quiet and refused to predict one from the other by multiplying. `TOOL-aPooledSweep-2` §3 refused a
factor "derived from one suite … applied to fifty-eight it was never measured on". The full-sweep
record's own remedy is re-sizing against pooled readings. And `derive-ceilings.py` already owns the
rule: worst observed under the condition, monotone, floor-plus-fraction headroom, refusing to report
with no evidence, `--reset` as the one lowering path, and readings only from runs that completed —
all five parts, because a rule reused without its self-correcting parts freezes a bad first reading
forever (round 1, H8 through H11).

### Why the bootstrap is a declared mode, and why it refuses in three places

The evidence shape cannot bound a row that has never been observed, and `--sweep`'s own S7 forbids
an unbounded pooled row. So the first observation is taken under a wall derived from the serial
budgets — never the profile's `wall` row, which `TOOL-aPooledSweep-1` rev-3 found sits below the
largest suite and which the runner already refuses to borrow — in a mode that says it is calibrating
and grades nothing. It refuses a killed row (a truncation is not a reading — the `ab-arm` class),
refuses any mode but `--pooled` (a `--serial --calibrate` that ran the serial loop and wrote nothing
would be silent in a mode whose point is announcing itself), and refuses a file that does not parse.

### Why the flip is the build's landing step and not this unit's

`TOOL-aBatchedArm-4` landed `--pooled` dark because the bound it inherits killed five of the seven
current unattended rows. Re-pointing the carriers is the act that makes the fast path the recorded
DoD verdict, and it happens only after the bound that would grade it is the evidence one and has
been seen green over EVERY row the DoD command resolves — fourteen at this base, not the eight a
draft of this spec typed. Two owner rulings (2026-09-13, 2026-09-14) defer every gate run to one
pass when every unit is built, so the observation that licenses the flip cannot happen inside this
unit; landing the flip as text before it would record a DoD command with no passing run, which is
the false-green shape one level up and what unit 4's AC7 reds by name. Hence dark: both spellings
on every carrier, the pooled one marked, and the flip commit ordered after the pasted GREEN.

### Why the node is in the key

Unit 3 measured a checker invocation at 47 to 60 s on node `a` against the ~2 s another host
records; a 2x headroom cannot absorb that spread. A fast node calibrating first would leave the slow
node with an observed row that grades it at roughly twice a reading it can never meet.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` (the fixture rebuild:
`build_repo` gains a fixture `ceiling-margin.txt` with a small floor and a seeded evidence file for
every fixture row under the fixture's own token and node, captured from a run the way the fixture's
generated stubs are) · `tools/run-gates/selftest-pooled-evidence.txt` (new, tracked, names row
NAMES and no path, so it takes no `install-prefix-carried.txt` row) · `tools/run-gates/kit.toml`
(the `project-owned` rule) · `tools/run-gates/selftest-budgets.txt` (the retired factor header) ·
the eight carrier lines above, dark · `memory/guides/SESSION-KICKOFF.md` (`run-selftests.sh` is
on its `watch:` line, so `last-audit` is re-stamped in the same commit) · this build's records.

## 5. Production-readiness checklist

- security — N/A. Bound derivation and verdict wording.
- perf / scale — the pooled path becomes the recorded one only at the build's landing; its wall
  clock is whatever the final pass measures, graded rather than hand-run from then on.
- error / empty / loading states — a row with no evidence under this node and token REFUSES the
  pooled run by name; a calibration run prints that it graded nothing and reds on a killed row; an
  evidence file that will not parse refuses rather than defaulting; `--calibrate` off `--pooled`
  refuses; `--check` reds a malformed or duplicated evidence row.
- observability — every pooled verdict names the reading, token, node and date it was bounded by,
  so a kill can be read against the reading that set the bound.
- risks — the evidence is monotone over whatever was observed, so a calibration taken on a loaded
  box sets a loose bound for that row until `--reset`; a first reading taken on a quiet box is
  raised by the next `--calibrate`, which runs every row. Stated, and it errs toward not killing.
- testing — the runner's self-test gains arms for: the no-evidence refusal; the calibrate mode
  grading nothing; a bound derived from a staged evidence row; the killed-row RED with no reading
  written; the monotone raise and the `--reset` lowering; the foreign-node row not satisfying this
  node; `--calibrate` off `--pooled` refusing; the unparseable file refusing; `--check` redding a
  duplicated key; the wall derived from evidence bounds and the below-largest refusal against it.
  Each observed RED first.
- migration — the carriers gain the dark spelling in this unit, reversible by one line each; the
  flip is the build's landing step and reverts the same way.
- user docs — the runner's `--help` names `--calibrate` and `--reset`; the kit runner's names the
  dark spelling and the landing order.

## 6. Acceptance criteria

- **AC1** — When a fixture row has a reading in `selftest-pooled-evidence.txt` under the fixture's
  condition token and node, `run-selftests.sh --pooled` bounds it at that reading plus the fixture
  `ceiling-margin.txt`'s headroom, prints the reading, token, node and date it used, and the run's
  wall line is `ceil(sum of bounds / OUTER)` floored at the largest bound.
  `fixture:` the runner's own test fixture with staged evidence rows; no real suite runs.
  Red when: the bound or the wall is the serial budget times any factor, or the verdict names no
  reading.
- **AC2** — When a fixture row has NO reading under this node and token, `run-selftests.sh --pooled`
  REFUSES naming the row, the token and `--calibrate`, and executes no suite; and a row evidenced
  under a FOREIGN node refuses the same way.
  Red when: it runs the row under any bound, which is a factor wearing a refusal's name.
- **AC3** — When `run-selftests.sh --pooled --calibrate` runs over the fixture rows, each is bounded
  by the serial-derived wall only, no `OVER BUDGET` and no `TIMEOUT` verdict is printed, each
  completed row's reading is written with its token, node and rc, an existing row is raised and
  never lowered, and the summary says `calibrated <n> row(s), graded none`; and when one fixture
  row sleeps past the wall, that row writes NO reading, is named, and the run exits RED with
  `<k> killed` in its summary.
  `fixture:` the runner's test fixture inside this unit; the real population at the build's final
  pass, per S4.
  `cost:` at the final pass, one pooled pass of the population `--kit tools/unattended --list`
  resolves, its longest row the floor of that pass.
  Red when: a calibration prints a verdict, a killed row's seconds land in the file, or a second
  calibrate with a lower reading lowers a row.
- **AC4** — When `run-selftests.sh --rank` runs in the fixture after a calibrate, it exits 0; and on
  the real tree `grep -c pooled@ tools/run-gates/selftest-budgets.txt` is 0 before and after the
  unit, and `--rank`'s unbacked list is the same list before and after.
  Red when: a `pooled@` token appears in the budget file, or the unbacked list moved.
- **AC5** — When the eight carrier lines are read as text after this unit's commit, each names
  `--pooled after calibration` beside `--serial` except the one declared cost line; and at the
  build's landing, `bash tools/unattended/run-unattended-gates.sh --pooled` completes GREEN on the
  merged tree over the population `--kit tools/unattended --list` resolves, its GREEN pasted, and
  the flip commit follows it — that half owed until then, in the amended form.
  `cost:` one real pooled pass on the merged tree, at the landing.
  Red when: a DoD line names `--pooled` alone before the pasted GREEN, no line declares the serial
  cost pass, or the landing pass kills a row and the flip lands anyway.
- **AC6** — When the existing `--serial` arms of `run-selftests.test.sh` run after this unit, they
  are GREEN unchanged: the serial mode still issues `OVER BUDGET` cost verdicts, because this unit
  touched no serial path.
  Red when: any pre-existing serial arm moved.
- **AC7** — When `selftest-budgets.txt` is read after this unit, it carries no
  `sweep-ceiling-factor:` header, and `run-selftests.sh --pooled` over the fixture with a factor
  header staged back in ignores it — the bound and wall are the evidence ones.
  Red when: any factor-derived bound or wall prints.
- **AC8** — When `run-selftests.sh --serial --calibrate`, `--check --calibrate` or bare `--calibrate`
  runs, each REFUSES naming the pair and executes no suite.
  Red when: any of them runs a row or writes a reading.
- **AC9** — When `run-selftests.sh --check` runs over an evidence file with a duplicated
  (row, token, node) key, a six-field row, or a row naming no declared budget row, it REDS naming
  the line; and `--pooled` over a file that will not parse REFUSES naming the file.
  Red when: `--check` is green over any of the three, or `--pooled` defaults past the parse.

## 7. Gates

`memory hygiene` · `run-selftests self-test` · `every held leg is budgeted, every budget row resolves`
· `install-prefix (shipped surface)` · `charter size` · `kickoff-manifest ratchet` · `run-gates canary`
· `run-gates gov canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates adopter e2e`
· `profile-bar selftest` · `lexicon naming predicates` · `unattended skill wiring` · `govkit selfcheck`
· `push-main self-test` · `check-wiring self-test`

Derived from `tools/gate-legs.json` by guard over the files touched: every leg whose guard covers
`tools/run-gates/` fires on the runner and its test, the `unattended skill wiring` leg reads
`kit.toml` and `run-unattended-gates.sh`, and the record legs are unguarded. Under the 2026-09-14
ruling every one of them runs at the build's final gate pass and none inside this unit.

New arm: `tools/run-gates/run-selftests.test.sh` · the ten arms §5 testing lists, each staged RED
then unstaged, over a rebuilt fixture that seeds a margin file and an evidence file; the two arms
that assert the factor shape today (`run wall 140s` and the `TIMEOUT` at a factor bound) are re-cut
to the evidence shape · floor to move: the suite's own, up by the arms added.

## 8. Open questions

- **F1 · Does the evidence file take a per-row condition token, or one per run?** Per row.
  RESOLVED (agent, 2026-09-14, delegated): per (row, token, node) in the runner's OWN evidence file;
  rev-1 named `derive-ceilings.py`'s reader as the seam and that was wrong at source — its file has
  no condition column, is generated from bar leg files, and refuses hand rows by its header.
- **F2 · What if unit 3's AC4 measurement misses 20 minutes?** Then the flip still happens if the
  bound is sound — the goal is the owner's target and the flip is about correctness, not speed — and
  the miss is recorded against the host's spawn path per `TOOL-aBatchedArm-4` §4. RESOLVED (agent,
  2026-09-13, delegated): the flip is gated on the bound, not on the 20 minutes.
- **F3 · Refuse or fall back for an uncalibrated row?** RESOLVED (agent, 2026-09-14, delegated):
  REFUSE, and retire the factor so nothing survives to fall back on. A fallback is the bound that
  killed 14 of 58, and a refusal names what to type.
- **F4 · Where does the flip land?** RESOLVED (agent, 2026-09-14, delegated): dark in this unit,
  flipped as the build's landing step after the pasted GREEN on the merged tree. The alternative —
  a DoD line naming a command with no passing run — is the shape unit 4 AC7 reds.
- **F5 · Which wall bounds a calibration?** RESOLVED (agent, 2026-09-14, delegated): the serial
  budgets' sum over `OUTER`, floored at the largest serial budget, `SELFTEST_WALL` overriding; the
  profile row is the borrow `TOOL-aPooledSweep-1` rev-3 refused, and a REQUIRED `SELFTEST_WALL`
  would put a typed number in the DoD.

## 9. Revision log

- rev-3 · 2026-09-14 · §1 · §2 S1 through S4 · §3 · Edges · §4 · §5 · §6 AC1 through AC9 · §7 ·
  F3 · F4 · F5 · §10 · folded spec-audit round 1 (BLOCKED, 3 blockers, 13 highs, 11 mediums, 1
  low, 28 confirmed rows in 11 defects, precision 0.52). The four scope decisions first: the
  population is the DoD command's RESOLVED one (`--kit tools/unattended --list`, fourteen rows at
  this base, never typed — B1, B2, H1, M1); the flip lands DARK here and flips as the build's
  landing step on the merged tree after the pasted GREEN, with the landing order and the red
  outcome written (B3, H2, M2); an uncalibrated row REFUSES and the factor header, its arm and its
  verdict text are retired, the graded wall derived from the evidence bounds and the calibrate wall
  from the serial budgets (H3 through H7); the rule is reused WHOLE — readings only from rows that
  exited on their own with a RED calibrate on a killed one, every row raised monotone on every
  calibrate, `--reset <row>` as the lowering path, node in the key (H8 through H11, M10). Then the
  mechanical set: the fixture rebuild with a seeded margin and evidence file and the two factor-shape
  arms re-cut (H12); AC4's witness is the fixture's `--rank` plus the real tree's `pooled@` grep and
  an unchanged unbacked list, since `--rank` exits 1 at this base for unit 3's derived shard-8 row
  (H13, M3); the carriers enumerated by grep as eight lines in six files with `kit.toml:126`
  declared the cost line and AC5's red-when corrected (M4, M5); the `kit.toml` `project-owned` rule
  and the manifest re-stamp in Files touched (M6 through M9); §7 re-derived over `gate-legs.json`
  (M11); the unparseable-file arm and the `--calibrate`-off-`--pooled` refusal (L1). AC6 is no
  longer a flip diff, since no flip lands here; it is the existing serial arms unchanged.


- rev-2 · 2026-09-14 · §2 S1 · S3 · S4 · §3 · §4 · §6 AC1 · AC3 · AC5 · AC6 · §7 · F1 · §10 · base ·
  pre-audit correction of a seam claim verified false at source, plus the owner rulings. rev-1 put
  pooled readings in `ceiling-evidence.txt` keyed by name and condition token; that file is
  GENERATED from `<git-dir>/gate-run/*/*.leg` by `derive-ceilings.py --write`, has five columns and
  no condition, says `Do not hand-edit`, and its `--check` prints a stale-row note for every row
  naming no manifest leg — so a self-test row there is a second writer to a generated artifact. The
  store is now the runner's own `selftest-pooled-evidence.txt`, same monotone/margin RULE, the
  margin READ from `ceiling-margin.txt`. The 2026-09-14 ruling (no gate until every unit is built)
  moves AC3's and AC5's real-row observations to the build's final gate pass; AC6 becomes a diff.
  The `ceiling evidence` gate leaves §7, since this unit no longer touches its file. Base bumped to
  `1c736fd9`, where units 3 and 4 are CLOSED and the eight rows exist.
- rev-1 · 2026-09-13 · initial draft, from `TOOL-aBatchedArm-4`'s three audit rounds, which
  specified this unit's shape while refusing it inside that one: the evidence-derived bound (r1 B5),
  the flip landed dark and owned here (r2 B1), and the declared bootstrap. Authored now rather than
  after unit 3 because memory hygiene check 14 reds on a cited id with no spec, and the id was cited
  at `9b00bc7b`.
## 10. Reuse audit


- **The seam is the RULE in `tools/run-gates/derive-ceilings.py`** — worst-observed, monotone,
  `max(floor, fraction x max)`, refusing with no evidence — and the margin file it reads,
  `tools/run-gates/ceiling-margin.txt`, verified at source. Its FILE, `ceiling-evidence.txt`, is
  NOT reused: verified at source on 2026-09-14, it is generated from bar leg files, keyed by leg
  name with no condition column, and its header forbids hand rows; rev-1's claim that it was the
  seam was wrong. The condition token `pooled@<outer>x<inner>` is the runner's own at the text
  `SWEEP_CONDITION=`. The `--rank` refusal of `pooled@` at the text `REFUSED = [re.compile(r"pooled@")]`
  is REUSED by keeping pooled readings OUT of the budget file. The
  reuse probe was run —
  `python tools/codebase-map/reuse_lookup.py "derive a pooled hang bound from observed readings under a condition token with monotone evidence and declared headroom"`
  — and returned `read_text`, `read` and `derive_scope`, none of which is this seam; it reports
  `unscanned layers: .sh` and `derive-ceilings.py` is Python it did not rank, so its result is not
  evidence either way. The seam was found by reading `derive-ceilings.py` and the two files beside
  it.
- **The parts of that rule this spec now carries by name**, because round 1 found the reuse was
  the file's header and not the rule: `read_runs` counts completed runs only (`derive-ceilings.py`,
  the text `may have failed fast`); `--write` raises every measured row monotone; `--reset <leg>` is
  the one lowering path; `GOV_NODE` is its node spelling, which the runner reuses with the hostname
  as the fallback the script does not have (it defaults to `a`, which is wrong on every other node
  and is not reused).
- **The kit runner's wiring leg**, `unattended skill wiring`, already reads `kit.toml` and
  `run-unattended-gates.sh`; the carrier parity arm round 1 asked for is its natural home, named
  here and not built by this unit.
- **The retrieval arguments, verbatim:**
  `python tools/memory-recall/query.py "why does the self-test runner run suites serially by default and pool only under sweep, and what was measured about cost attribution under contention" --terms "run-selftests OUTER pool sweep serial budget contention dilation attribution width verdict withheld mode declared"`.
  Run for unit 4; it surfaced `TOOL-dRetiredFork-40`, `TOOL-aPooledSweep-2` and the full-sweep record
  this unit's §4 rests on.
