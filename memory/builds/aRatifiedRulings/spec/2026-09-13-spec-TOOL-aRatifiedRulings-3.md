# TOOL-aRatifiedRulings-3 — the hygiene self-test's project-key arms stop re-running the checker over the whole corpus

**Status:** SPECCED · rev-3 · 2026-09-13 · node a · Tier-2 · base 16da4c6a · streams tooling · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md](../reviews/2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md) | spec-audit | TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-4 |
| [2026-09-13-review-TOOL-aRatifiedRulings-1-round2.md](../reviews/2026-09-13-review-TOOL-aRatifiedRulings-1-round2.md) | spec-audit | TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-4 |

<!-- /gen:spec-records -->

## 1. Goal

Build owner ruling `TOOL-aLeakedHandle-8`: `memory-hygiene self-test` gets CHEAPER, and its 900 s
ceiling in `tools/gate-legs.json` is not re-declared. The ruling names the direction and a diagnosis;
this spec measured the suite on this tree, tested three mechanisms against the numbers, and builds
the one that survived: the project-key arms at the tail of
`tools/memory-tree/check-memory-hygiene.test.sh` stop running the whole checker over a `git archive`
of this repository and run it over the 29-file tree the suite already builds and already asserts
clean, one run per arm, with every arm asserting the VALUE it grades rather than an exit code.

## 2. Scope (IN)

- **S1** — The project-key section of `tools/memory-tree/check-memory-hygiene.test.sh` runs over
  the check-16 note fixture the suite builds at lines 2178-2196 (a fresh `git init`, one build
  folder, one spec, a charter, a `memory/project/` registry), which the suite already asserts clean
  at rc 0 and which today is `rm -rf`'d after one run. The `git archive HEAD` of this repository, the
  overlay `cp` of the working checker, `GOVROOT` and the fixture commit at lines 2222-2233 are
  removed. Observed by AC1 and AC2.
- **S2** — The clean run over that tree serves the check-16 note arms AND the project-key control
  arm ("the fixture is clean with no key set"): one invocation, three assertions. That invocation
  is the one at `check-memory-hygiene.test.sh:2198` today, the direct `bash "$HERE/check-memory-hygiene.sh"`
  whose rc and output land in `_b1rc` and `_b1out`; the control reads those two variables and
  nothing routed through `pk_out`. Each arm that must observe an ABORT captures rc and stdout from
  ONE invocation instead of a `pk_rc` run followed by a `pk_out` run. Observed by AC1.
- **S3** — The arms that grade a RED assert the finding's text, never rc alone: the violated
  `BUILD_SLUG_RE` arm reads `HYGIENE check 4 FAILED` and the folder line naming `memory/builds/tOne`;
  the `PROJECT_REGISTRY_EXTRA` arm commits BOTH `my-registry.txt` and `unlisted-probe.txt` under
  the fixture's `memory/project/` and reads check 3 naming the probe and not the registry; the
  control arm reads rc 0 AND the `READ_PATH_CEILING is declared` notice the fixture's conf provokes,
  so a clean verdict carries proof the run reached check 16. Observed by AC5.
- **S4** — No assertion is removed. The executed count `n` the suite prints does not fall below the
  count measured before the change, and every `ok` label the section prints today is printed after.
  The `FLOOR_ASSERTIONS` comparison MOVES from `check-memory-hygiene.test.sh:2212-2213` to
  immediately above the `PASS` line at `:2306`, so the value it grades is the value the `PASS` line
  prints, and the constant is RAISED to that post-change `n` in the same commit that measures it
  (§8 F2). Observed by AC4.
- **S5** — The suite's cost is measured on this node twice, by the method in
  `memory/gotchas/process-creation-is-the-suite-cost.md`: a PAIRED standalone reading, the same
  traced invocation before and after on the same box back-to-back (AC2), and the one full bar the
  run buys BY HAND as `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` (AC3). The
  landing bar produces no such row: `.unattended.conf`'s `GATE_CMD` is
  `bash tools/run-gates/run-gates.sh`, `.githooks/pre-push` reads `GATE_SELFTESTS` and never sets
  it, so the leg is held on every boundary (§7) and a landing push's green is not the AC3
  observation. Both readings go into the unit's acceptance ledger with the checker-invocation count
  beside each figure, whatever they read: the standalone pair's counts come from each run's own
  trace (AC2), and the full-bar row, which the runner runs untraced, carries the count AC1 derives
  from the arm list. The standalone pair must show the cut; the full-bar row is OBSERVED against the
  untouched ceiling and its red has the disposition AC3 and §8 F3 state, because this repo's own
  record says the loaded reading is not derivable from the quiet one. Observed by AC2 and AC3.
- **S6** — Every arm this unit adds or moves has its failing case observed RED by hand before it
  lands, from a driver that refuses a run which executed fewer arms than the section holds.
  Observed by AC6.

## 3. Non-goals (OUT)

- **The 900 s `ceiling` of `memory-hygiene self-test` in `tools/gate-legs.json` is NOT edited.**
  Not raised, not lowered, not re-derived. The ruling forbids the raise; a lowering is the owner's
  call over readings this unit produces, and the file that owns the number states its own
  derivation rule. Whether the number then moves is a separate decision with a measurement behind
  it.
- **This leg's budget row in `tools/run-gates/selftest-budgets.txt` is NOT edited.** Its header says
  it is calibrated from the worst retained reading times 1.5 over `gate-run` windows; one
  post-change reading is not a window. Re-calibration is a follow-up by that file's own rule, and
  the figure lives there, not here.
- **`tools/memory-tree/check-memory-hygiene.sh` and its delegates are NOT changed.** Candidate C
  in §4 measured the engine's per-invocation floor and it is real, and it is engine work: it moves
  a behaviour-bearing line of a file in `check-verdict-epoch.sh`'s scan set, owes the five-carrier
  kit bump, and re-baselines `hygiene-parity.test.sh`. Handed off with its numbers.
- **No leg is added, split or renamed.** Candidate D in §4 is refused on the declared-population
  rule and on the ceiling: N shards under one 900 s bound is the re-declaration the ruling refused,
  spelled as N × 900.
- **No assertion is deleted to buy time**, and the two other self-tests the 2026-09-07 park found
  red at BASE (`govkit selftest`, `codebase-map adopter e2e`) are not this unit's.
- **The main-tree section and the scratch trees are NOT restructured.** They are the two largest
  rows of the region table in §4 after the project-key section, and that table is where their share
  is read rather than a figure restated here; every one of their re-runs varies a conf or a tree
  state that the arms read, and the ruling names the project-key section. What they cost is
  recorded so the next unit starts from a number.

### Edges

- **consumes-from** external — a full concurrent bar on this node, `GATE_FULL=1 GATE_SELFTESTS=1`
  at the width `tools/run-gates/gate-profiles.txt` picks for it, is the load condition AC3 observes
  under. Nothing in the tree can substitute for it, because the breach the ruling answers was only
  ever seen there and because the quiet-to-loaded relationship for this suite is on record as not a
  multiplier (§4); the run pays it once and copies the row into the ledger before the runner prunes
  the window.
- **hands-off** external — the per-invocation floor of the checker itself: 8.0 s over a 29-file
  tree, of which `corpus_ids.py --check` is 3.2 s because it re-enters the checker in a print mode
  after probing every `bash` on PATH, times the 66 invocations one suite run makes. That is a unit
  on the engine, with the bump obligation §3 names, and it is the lever after this one. If AC3
  reads red, its row is that unit's input, parked per §8 F3; this unit does not promote it.
- **hands-off** external — re-calibration of the `selftest-budgets.txt` row and any lowering of the
  ceiling, both from post-change readings, both by the rule each file states.

## 4. Design

### The cost, measured

Method: `memory/gotchas/process-creation-is-the-suite-cost.md`, which is `time bash <invocation>`
read as user+sys against real, plus one traced run under `PS4='+ ${EPOCHREALTIME} ${LINENO} '`
so every checker invocation's wall clock is the gap to the next trace line. Node `a`, worktree at
`16da4c6a`, 2026-09-13, box quiet (three and two `bash.exe` processes at start, read with `ps -W`).
Every figure below is PINNED to that measurement; the ledger re-derives them after the change.

| reading | real | user | sys | rc |
|---|---|---|---|---|
| suite, plain | 790.7 s | 187.7 s | 355.8 s | 1 |
| suite, traced | 598.7 s | 168.1 s | 290.1 s | 1 |
| one checker run, archive fixture (min of 3) | 28.0 s | 8.0 s | 10.6 s | 1 |
| one checker run, 29-file fixture (min of 3) | 8.0 s | 1.5 s | 2.6 s | 0 |
| one checker run, invalid key, archive fixture | 0.08 s | 0.00 s | 0.05 s | 2 |

Two consecutive quiet runs differ by 1.32×. The gotcha says wall clock on this node is not
measurable to better than a factor of two, and the acceptance below is written against that spread
rather than against one reading: AC2 is a paired reading of the same invocation back-to-back, with
the deterministic invocation count (AC1) as the claim actually written down, which is the proxy
the gotcha itself says to prefer.

This tree holds two more standalone readings of the suite that are NOT in the table, and both are
admitted here so the spread is honest. `memory/builds/aJoinedCanon/RUN.md` records about 660 s on
2026-09-07 at the park; `TOOL-aPooledSweep-4` records 1126 s serial and 972 s pooled on the same
day, inside a sweep A/B whose box state is not recorded, so it cannot be called quiet and cannot be
excluded either. The whole standalone band this suite has ever shown on node `a` is therefore
598.7 s to 1126 s, a 1.88× spread, which is the gotcha's factor of two seen on this suite. A
pinned wall-clock bound anywhere inside that band is a coin flip, and no criterion below pins one.

**The loaded reading is not derivable from the quiet one, and this spec does not derive it.** The
records this repo holds on the relationship for THIS suite: the park saw about 660 s standalone
killed past the 900 s ceiling under `GATE_FULL=1 GATE_SELFTESTS=1` at width 8, at least 1.36×;
`TOOL-dRetiredFork-40` measured 443 s under load against 583 s quiet, the wrong way round, and
concluded "the relationship is not a multiplier and cannot be guessed"; and a different hygiene leg
went 48 s quiet to 139 s inside a full bar, 2.9×. Three readings, three ratios, one of them below
one. The post-cut standalone projection is 433 s on the traced reading and 811 s on the 1126 s
reading at the same share (the 0.72 derived under "The mechanism"); times 0.76, 1.36 and 2.9 that
is 329 s to 2352 s, which straddles the ceiling from both sides. So the full-bar figure is OBSERVED by AC3 and never predicted, and AC3
carries the disposition for a red rather than an arithmetic that says it cannot happen.

The suite is RED at `16da4c6a`. The first project-key arm reports `the fixture is not clean unset
(rc=1) — every arm below is meaningless`, and the archive run's output says why: check 21 and check
14 red on this build's own four ids, cited by the run mandate and the README roster and defined by
no spec H1 yet. That is the class `TOOL-aPooledSweep-4` diagnosed on 2026-09-07 with a different
finding: the archive fixture inherits the live corpus's hygiene state, so the control arm is red
whenever the tree is, including mid-build. Once the four specs of this build land, the same fixture
reds again on a different check: every live spec dated at or after `BASE_RESOLVE_CUTOFF` names a
`base` sha that a fresh `git init` with one commit cannot resolve. The three `FAIL` lines beneath
the control (`RECORD_SERVES_CUTOFF`, `ENTRY_CAP_UNIT=chars`, `=bytes`) are that same red seen
through arms that expected rc 0, and the violated-slug arm printed `ok` on it, which is a
presence-not-value assertion satisfied by an unrelated red.

Where the traced run's 598.7 s go, by suite region, with the checker invocations counted from the
trace (66 per run: 47 over scratch trees, 19 in the project-key section):

| region | checker runs | checker s | other s | share |
|---|---|---|---|---|
| main fixture build, lines 1-847 | 0 | 0.0 | 5.5 | 1% |
| main-tree assertions and conf re-runs, lines 848-1480 | 15 at 6.2-18.5 s | 180.2 | 16.0 | 33% |
| scratch trees, lines 1481-2176 | 28, of which 7 aborts | 145.2 | 19.2 | 27% |
| check-16 note fixture and its run, lines 2177-2206 | 1 | 8.6 | 2.3 | 2% |
| archive fixture build, lines 2222-2233 | 0 | 0.0 | 17.9 | 3% |
| project-key arms, lines 2235-2303 | 19, of which 12 aborts | 202.7 | 2.3 | 34% |

The project-key section plus the fixture it builds is 222.9 s of 598.7 s, 37%. Seven full runs at
25-31 s each are 201 s of it; the twelve aborts are 1.4 s together; the archive's `git add -A` and
commit are 15.6 s. The ruling's diagnosis is right about the section and wrong about the pair:
`pk_rc` followed by `pk_out` on an invalid key costs 0.16 s, because the checker refuses at line 170
of `check-memory-hygiene.sh` before it resolves python. What costs is that the seven runs that DO
proceed walk 1902 tracked files, and that a fixture is built to hold them.

One archive run spends 11.2 s in its five python delegates (`corpus_ids.py --check` 7.2 s,
`gen_build_index.py --check` 1.8 s, `gotchas.py --check` 1.4 s, `--print-bindings` 0.5 s,
`row_grammar.py --check` 0.2 s) and makes 186 external spawns (grep 102, awk 30, sort 14, git 11,
sed 7, python 7). One 29-file run spends 4.4 s in the same delegates (`corpus_ids.py` 3.2 s of it)
and makes 119 spawns (grep 75, awk 17, sort 10, python 6, git 4). Python startup alone is 0.29 s on
this node; a grep is 0.03 s.

### Candidates and the tests that decide them

Reached through M12: the ruling gives a direction, the mechanism was not chosen. Each candidate's
losing test was written before the measurements above were taken; the result column is what the
numbers then said.

| candidate | mechanism | would LOSE if |
|---|---|---|
| A — batch the valid-key arms into one conf | fewer runs over the same archive fixture: `BUILD_SLUG_RE` valid, `RECORD_SERVES_CUTOFF` past and `ENTRY_CAP_UNIT=chars` in one conf asserting rc 0, so seven full runs become three | the archive fixture is red for a reason no key controls, so no batching yields a `PASS`; or the four runs saved are inside the run-to-run noise |
| B — run the arms over the suite's own small clean tree | fixture size: the check-16 note fixture already exists, is already asserted clean, and is the shape every other scratch arm in this suite uses | one run over it is not materially cheaper than one over the archive; or the tree cannot host one of the four keys' red cases; or it is not clean at rc 0 |
| C — cut spawns inside the checker on the paths the suite exercises most | the per-invocation floor, paid 66 times a run | the floor sits in the python delegates rather than in shell spawns, so a shell de-spawn cannot reach it; or the yield is bounded the way `TOOL-aTracedSpawn-2` found |
| D — shard the suite so the bar runs it as N legs | manifest: N argv rows, N names | the total does not fall; or each new name owes a `memory/map` claim, a `tools/govkit/subject-pins.tsv` row and a `selftest-budgets.txt` row by the declared-population rule; or the bound becomes N × 900 |

What the numbers said:

- **A LOSES on its first test.** The archive fixture is red at `16da4c6a` on checks 21 and 14, and
  it reds on `base` resolution once this build's specs land, so no batching over it yields a `PASS`.
  On the 29-file tree the four runs it would save are 32 s against a 190 s spread between two quiet
  readings, so its second test could not have changed the pick either. Attribution is its price: rc
  0 over three keys names none of them when it fails.
- **B SURVIVES.** 8.0 s against 28.0 s per run, rc 0 on every one of three readings, and the archive
  build (17.9 s) and the separate control run (8.6 s) disappear with it. Check 4 names
  `memory/builds/tOne` under `^zzz[A-Za-z]+$`, and check 3 names a committed probe under
  `PROJECT_REGISTRY_EXTRA`, so every red case has a host.
- **C LOSES for this unit and is the next one.** The floor is 8.0 s on a 29-file tree and 4.4 s of
  it is python startup plus `corpus_ids.py --check` at 3.2 s, which probes every `bash` on PATH with
  `-c :` and re-runs the checker in a print mode. That is engine work with the bump obligation §3
  names, and it cannot be one mechanism with B. Its yield is recorded rather than lost: about 3 s
  times 66 invocations, roughly 200 s a run, comparable to B's.
- **D LOSES on all three.** Every shard rebuilds the main fixture (5.5 s) and pays the
  per-invocation floor for its own runs, so the sum rises; each shard is a new inventory key; and N
  legs under one untouched ceiling is the re-declaration the ruling refused, written as a
  multiplication.

Pick, by M3's rule: B is the only survivor of its own test, and it keeps one run per arm, so every
arm still names what it graded. The ruling's sentence "one run must serve several" is met where a
run genuinely can serve several — the clean run over the small tree serves the two check-16 note
arms and the project-key control — and is not stretched over arms that read different conf states,
because the measured price of keeping them separate is 32 s inside a 190 s noise band.

### The mechanism

The check-16 note fixture at lines 2178-2196 is built in a subshell into `_b1`, run once at line
2198, asserted clean and asserted to print the `READ_PATH_CEILING is declared` notice, then removed
at line 2206. This unit keeps it and makes it the project-key tree:

- `pk_set` writes the fixture's base conf (its four lines plus the `READ_PATH_CEILING` line that
  provokes the notice) and appends the arm's one key line, exactly as today but from a literal
  rather than from a copy of `.memory-tree.conf`. The gov conf is no longer read: the arms grade
  the KEY against the checker, not gov's values against gov's corpus, and the one thing the gov conf
  contributed was the live corpus's `PROJECT_REGISTRY_EXTRA`, which the archive run reports as a
  notice on every invocation.
- `pk_out` becomes the one runner: it runs `"$HERE/check-memory-hygiene.sh"` from the fixture root,
  the way the `_b1` arm already does, captures stdout and stderr, and returns the checker's rc. Every
  arm that today calls `pk_rc` then `pk_out` calls it once. `pk_rc` is REMOVED, and
  `VERB_OFFENDER_PIN` in `.lexicon.conf` is lowered in the same commit to the value
  `python tools/lexicon/lexicon.py --check` prints. There is no "keep it as a wrapper" branch: the
  pin is an equality in both directions (`lexicon.py` reds UNDER the pin as well as over it, and
  `--list` names `pk_rc` as a P1 offender at line 2240), so removing the definition always moves
  the pin and the only consistent shape is remove-and-lower together.
- The control arm reads `_b1rc` and `_b1out` from the existing run at `check-memory-hygiene.test.sh:2198`:
  rc 0, and the notice present. No second run, and nothing routed through `pk_out`, which is why
  its staged break (AC5, AC6) is applied to that invocation and not to the runner.
- The violated-slug arm asserts `HYGIENE check 4 FAILED` and `memory/builds/tOne (bad folder name`
  in the captured output. The registry arm commits `memory/project/my-registry.txt` beside the
  `unlisted-probe.txt` it already commits and asserts the probe is named and the registry is not.
  The six abort arms keep their `2:*KEY*` case over rc and output from the single run.
- The `FLOOR_ASSERTIONS` comparison at lines 2212-2213 moves to immediately above the `PASS` line
  at line 2306, and the constant is raised to the post-change `n`. Today the comparison sits BEFORE
  the project-key section, so it grades `n` minus that section's thirteen increments while the
  `PASS` line prints the final `n`; a floor pinned to the printed number would red the suite on its
  first run. Hoisting the comparison makes the pin mean the printed number. `tools/check-testsuite-counts.sh`
  reads the `FLOOR_ASSERTIONS=<n>` line and a comparison against it by shape, not by position, so
  the move is invisible to that leg.
- The section's cost after the change, predicted from the table: six runs at 8.0 s under a key plus
  the one clean run the control now shares with the check-16 note arms, six aborts at 0.08 s, no
  archive build, no separate control run — about 57 s where 222.9 s were. On the traced reading
  that is 598.7 − (222.9 − 57) = 433 s, a ratio of 0.72; the plain reading at the same share
  projects to 569 s at the same 0.72. AC2 asserts the ratio, not a wall figure, because 0.72 is a
  property of the mechanism and any single wall reading is a property of the box.

### Data model

N/A — no conf key, no file format and no record shape changes. The fixture tree is the one the
suite already writes, plus one committed registry file under its `memory/project/`.

### Inventory

No leg, no conf key and no file is minted. Shell function names in this suite are graded by the
`sh.function` cell of `.lexicon.conf`, and `pk_set`, `pk_rc` and `pk_out` are among the P1
offenders this file already contributes to `VERB_OFFENDER_PIN`, which is a two-sided equality
(`python tools/lexicon/lexicon.py --list` names them at lines 2235, 2240 and 2241).
Removing `pk_rc` lowers the offender count by exactly one and the pin moves with it in the same
commit, to the value `python tools/lexicon/lexicon.py --check` prints on the tree, never a value
predicted here. That edit is certain, not conditional, per "The mechanism". A new helper, if one
is wanted, leads with a declared verb (`run` is in the table; `pk` is not, per `--suggest`).
The carried-literal row for this file in `tools/install-prefix-carried.txt` may fall when the
`$KIT_REL/check-memory-hygiene.sh` invocations go; a fall is permitted by that file's rule and the
count is read off `bash tools/check-install-prefix.sh`.

### Migration

N/A — nothing persisted changes shape. `tools/memory-tree/check-memory-hygiene.test.sh` is outside
`check-verdict-epoch.sh`'s scan set (the engine and its six delegates), so no kit version moves for a
suite-only change; `check-kit-versions.sh` grades constants and markers, none of which this unit
touches.

### Rollout

The leg is `chunk: selftests`, `subject: kit`, guarded on `tools/lib/` and `tools/memory-tree/`, and
held by `run-gates.sh` unless `GATE_SELFTESTS=1`, which no boundary sets. The change therefore lands
with ZERO boundary-enforced coverage of the suite it edits; the compensating checks are the direct
invocation, `bash tools/run-gates/run-selftests.sh --kit tools/memory-tree` for the budget verdict,
and the one full bar AC3 buys. Nothing is flagged dark: the suite either passes or it does not, and
a red suite is what it is today.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh` — the project-key section, the check-16 note
  fixture's teardown, and the `FLOOR_ASSERTIONS` comparison hoisted to above the `PASS` line; the
  only product file.
- `.lexicon.conf` — `VERB_OFFENDER_PIN`, lowered by one when `pk_rc` goes; value read off the tool.
- `tools/install-prefix-carried.txt` — this file's row, only if its carried count falls; value read
  off the gate.
- `memory/map/features/memory-tree-hygiene.md` — refreshed on touch: today it names the self-test as
  the dossier's and says nothing about what its project-key arms run over, so the refresh is one
  sentence or nothing.
- The unit's acceptance ledger, a journal record under the build's own record folder, carrying the
  before and after figures with their invocation counts.

### Alternatives rejected

- Candidates A, C and D, each with the test that rejected it, in the table above.
- Keeping an archive-of-this-repo control run "because it proves gov's own slugs satisfy a pattern".
  It proves gov's folder names against a pattern STRICTER than the default the `memory hygiene` leg
  already grades them under on every bar; that is a fact about gov's slugs, not about the key, and
  it is the run that carries the false red.
- Lowering the ceiling or the budget in the same commit "because the numbers now allow it". Both
  files state a derivation rule over retained readings and this unit produces one reading.

## 5. Production-readiness checklist

- security — N/A: a self-test over `mktemp -d` scratch trees under a `trap` that removes them; no
  tracked path is written by any arm, and the `git archive` of this repository disappears.
- perf / scale — the subject of the unit. Before and after figures are §4 and the ledger; the
  residual cost structure is the §4 region table for the main-tree and scratch rows and the 8.0 s
  per-invocation floor beneath it, recorded there so the next unit starts from a number rather
  than from a diagnosis, and not restated here where it would be a second answer.
- error / empty / loading states — a run that could not START is told from a red: the control arm
  asserts rc 0 plus a positive notice, the red arms assert finding text, and the abort arms assert rc
  2 plus the key's name. The small tree is asserted non-empty for every check-12 population by the
  checker's own `pop_guard`, which is what the rc 0 control proves.
- observability — the section prints one `ok` or `FAIL` line per arm and the suite prints
  `PASS (n assertions)`; the ledger carries real, user, sys, rc and the invocation count per reading.
- risks — (1) the four keys are graded against a 29-file corpus, so a key whose defect shows only
  at scale is not caught here; every key is validated in the preset block before any walk, and the
  `memory hygiene` leg runs the checker over the real tree on every bar. (2) Wall clock on this
  node varies 1.88× across the standalone readings §4 admits and the loaded reading is not a
  multiple of the quiet one; AC2 is therefore a back-to-back ratio with the invocation count as the
  deterministic claim, and AC3 is the full-bar observation whose red is disposed by §8 F3 rather
  than argued away. (3) `VERB_OFFENDER_PIN` and the carried-literal row can red the bar if a helper
  departs and the pin is not re-read; Inventory names both. (4) The hoisted floor comparison reds
  the suite itself if the constant is set above the `n` the section actually executes; AC4 reads
  the pin off the `PASS` line for that reason.
- testing — the arms themselves, each with its failing case observed RED first (AC6); the driver
  refuses a run that executed fewer arms than the section holds.
- migration — N/A: no shape moves and no kit version is owed, see §4 Migration.
- user docs — N/A: no user-facing surface; the dossier refresh in Files touched is the only prose.

## 6. Acceptance criteria

- **AC1** — When `PS4='+ ${LINENO} ' bash -x tools/memory-tree/check-memory-hygiene.test.sh`
  runs to completion with stderr captured, the trace shows no `git archive` line, and the count of
  checker invocations over the check-16 note fixture's tree equals the number the arm list needs:
  one clean run shared by the two check-16 note arms and the project-key control, six runs under a
  key that proceed, and six that abort, thirteen in all, where the 2026-09-13 trace showed the
  project-key section alone making 19 (12 through `pk_rc`, 7 through `pk_out`) over an archive
  fixture, plus a separate clean run, and a `git archive` at line 2227. This is the deterministic
  observation of the ruling's word CHEAPER; AC2's wall clock is its evidence.
  Red when: the trace still carries a `git archive`, or the count of invocations over that tree
  exceeds the arm list's need — an abort arm still making two, a control still making its own — or
  a proceeding run's cwd is not the check-16 note fixture's root.
  figure: the before counts 19 and 1 are PINNED, read from the 2026-09-13 trace on node `a`; the
  after count is DERIVED from the arm list at observation time and resolves to 13 on the arm list
  this spec holds.
- **AC2** — When `time PS4='+ ${LINENO} ' bash -x tools/memory-tree/check-memory-hygiene.test.sh 2><trace>`
  runs on node `a`, with `TIMEFORMAT='real %R user %U sys %S'` set in the calling shell and
  `<trace>` a fresh file per run, as a PAIRED reading — before at `16da4c6a` from a frozen
  `git clone --local` under a short root, after at the landed tip, interleaved before-after-before-after
  on the same box with the same `ps -W` process count at each start — the minimum `real` of the two
  after runs is at most 0.8 times the minimum `real` of the two before runs, every after run exits
  0 and prints `PASS (n assertions)`, and each of the four readings goes into the ledger with the
  checker-invocation count read from ITS OWN trace file beside it, counted the way AC1 counts: 20
  for a before run (the 19 over the archive fixture plus the one clean run at line 2198) and 13 for
  an after run. That count is the per-reading artifact that the run executed the section and not a
  stub, and it is the only artifact a before run has, because the suite is red at `16da4c6a` (§4)
  and prints no `PASS` line. All four readings are the TRACED class of the §4 table, which is the
  class 0.72 and therefore 0.8 were derived on (433 s of the 598.7 s traced reading); the plain
  790.7 s reading is not a term of this ratio. The trace costs the ratio nothing it can measure:
  §4's traced reading was the FASTER of its two quiet runs, so the trace's own cost sits inside the
  1.32× run-to-run noise §4 records, and it is the same on both sides of the pair.
  Red when: the after-over-before ratio exceeds 0.8, or an after run exits non-zero or prints no
  `PASS` line, or a reading is recorded without a count read from its own trace, or a before run's
  count is not 20 or an after run's count is not 13 — the section did not run to its end and the
  wall figure timed a partial suite. The bound is derived from
  the mechanism, not from a reading: §4 predicts 0.72 (433 s of 598.7 s traced), and 0.8 leaves the
  residual noise of a back-to-back pair eight points. A change that only cuts four of the seven
  archive runs — candidate A's shape — saves about 112 s of the traced 598.7 s, a ratio of 0.81,
  and prints no `PASS` line, so it reds on both halves. A pair that lands between 0.72 and 0.8 is
  green; one above 0.8 with AC1 green is re-measured once with a second interleaved pair per the
  gotcha's take-the-minimum rule and reds if it stays above, because the ruling's word is CHEAPER
  and an invocation count alone does not prove a wall clock fell on this box.
  cost: four suite runs on this node, about 40 to 75 minutes by the standalone band §4 admits.
  fixture: the before clone lives under a short root such as `%TEMP%`, not the session scratchpad,
  because `git clone --local` into the scratchpad's path fails with "Filename too long" on this
  node; and it is FROZEN — no commit lands in it between the two before runs, since a suite run
  over a tree that moved under it measures nothing.
  figure: no wall figure is pinned; 0.8 is DERIVED from §4's 0.72 as stated; the four readings are
  DERIVED by the command; the before count 20 is PINNED from the 2026-09-13 trace AC1 cites and
  the after count 13 is DERIVED from the arm list as AC1 derives it.
- **AC3** — When `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs on node `a`
  after the change, the run's `.leg` row for `memory-hygiene self-test` under the runner's
  `gate-run` window records status `ok`, rc 0 and seconds below the ceiling `tools/gate-legs.json`
  declares for that leg, and the ledger copies that row with its seconds whatever they read.
  Red when: the row records rc 124 or 137, which is the ceiling kill the 2026-09-07 park recorded at
  900.481 s and 900.240 s, or seconds at or above the ceiling with any status.
  Disposition of a red, stated here because no number in this spec implies this criterion holds
  (§4: the quiet-to-loaded relationship is on record as not a multiplier): the row is recorded red
  in the ledger with its seconds and invocation count; it is parked in the build README's
  "Parked decisions" as the ruling's next input, with candidate C's figures from §4 beside it; the
  ceiling stays untouched per §3; and this unit does not promote candidate C, per §8 F3. The
  unit's other criteria decide its landing, because the leg is held on every boundary and a red row
  blocks no push, but the close then states that the build README's expected improvement for this
  leg is NOT met by this unit alone.
  cost: one full bar with the self-tests, whose leg-sum was 4926 s with a 1565 s longest leg on node
  `d` on 2026-08-23; the run pays it once and no other criterion needs it.
  permission: `GATE_SELFTESTS=1` is on demand and no boundary sets it (owner, 2026-08-27); the run
  sets it by hand for this observation, which is the sanctioned use.
  fixture: the runner prunes the `gate-run` window, so the row is copied into the ledger in the
  same pass that observes it. The bar as a whole is expected RED on the two self-tests the
  2026-09-07 park found red at BASE; this criterion reads one leg's row and says nothing about the
  bar's verdict.
  figure: DERIVED — the seconds are whatever the row holds; the ceiling is read from
  `tools/gate-legs.json` at observation time, never from this file, and the 900 written in §1 and §3
  is the ruling's word for it, not a second declaration.
- **AC4** — When the suite passes, the `n` in its `PASS (n assertions)` line is at least 374,
  `FLOOR_ASSERTIONS` in `tools/memory-tree/check-memory-hygiene.test.sh` EQUALS that printed `n`,
  the comparison against it is the last statement before the `PASS` line so the value graded is the
  value printed, and every `ok` label the project-key section printed in the 2026-09-13 baseline
  output is printed by the section after the change.
  Red when: `n` is below 374; or the constant is below the printed `n` (slack, the OPEN reading of
  §8 F2 that a build which never raises the pin would satisfy) or above it (the suite reds itself,
  which is what a pin read off the `PASS` line does while the comparison still sits at line 2212,
  before the section's thirteen increments); or the comparison is anywhere but immediately above the
  `PASS` line; or an `ok` label is gone — an arm removed to buy time is exactly what this criterion
  exists to refuse. The slack half is observed by `grep -nE '^FLOOR_ASSERTIONS=' tools/memory-tree/check-memory-hygiene.test.sh`
  against the `PASS` line of the same run.
  figure: 374 is PINNED, read as the counter's final value from the 2026-09-13 trace because a red
  suite prints no `PASS` line; 235 is the value at `16da4c6a` and is superseded; `n` after and the
  constant are DERIVED, the constant from the `PASS` line of the run that measures it.
- **AC5** — When the violated-slug arm runs with `BUILD_SLUG_RE="^zzz[A-Za-z]+$"`, it asserts
  `HYGIENE check 4 FAILED` and `memory/builds/tOne (bad folder name` in the captured output; when
  the registry arm runs with `PROJECT_REGISTRY_EXTRA="my-registry.txt"` and both `my-registry.txt`
  and `unlisted-probe.txt` committed under the fixture's `memory/project/`, it asserts check 3 names
  the probe and does not name the registry; and the control arm asserts rc 0 AND the
  `READ_PATH_CEILING is declared` notice, read from the `_b1rc` and `_b1out` of the invocation at
  line 2198, not from `pk_out`.
  Red when: any assertion is satisfied by rc alone, staged per ASSERTION because one break cannot
  tell an rc-only form from a value form on every arm. The violated-slug arm — staged by pointing `pk_out` at a
  script path that does not exist so it exits 127 with no check-4 text, on which the rc-only form
  `[ "$r" != 0 ]` prints `ok` and the value form reds; that is the state the 2026-09-13 baseline
  recorded for this arm, which printed `ok` on a fixture that was red for a reason no key controls.
  The registry arm's "does not name the registry" half is staged by making `pk_set` a no-op so
  `PROJECT_REGISTRY_EXTRA` never reaches the conf and check 3 names both files; its "names the
  probe" half is staged by dropping the probe commit. The control arm's notice half is staged by
  dropping the `READ_PATH_CEILING` line from the fixture's conf for that one run, which leaves rc 0
  and no notice, so an rc-only control prints `ok` and the value form reds; the 127 break does not
  reach this arm at all, since it reads line 2198, and would red an rc-only control anyway.
- **AC6** — When each assertion this unit adds or moves has its subject reverted in place and the
  section is re-run BY HAND, the arm that owns it prints `FAIL` and the suite exits non-zero, one
  observation per assertion recorded before the reverts are unstaged, the breaks being exactly the
  ones AC5 names plus the abort arms' own: `pk_set` made a no-op (the violated-slug arm, the six
  abort arms and the registry arm's registry half go red), `pk_out` pointed at a missing path (the
  violated-slug arm's value form goes red where its rc-only form stayed `ok`), the probe commit
  dropped (the registry arm's probe half goes red), and the `READ_PATH_CEILING` line dropped from
  the check-16 fixture conf for that one run (the control arm's notice half goes red at rc 0). The
  ledger row per break names the break AND the invocation the arm read, line 2198 or `pk_out`.
  At least one break is observed through the whole named invocation,
  `bash tools/memory-tree/check-memory-hygiene.test.sh`; the rest may be observed through the
  section run from its own prologue. Whatever runs REFUSES a run whose count of `ok` and `FAIL`
  lines from the section differs from the arm count the section holds.
  Red when: an assertion passes with its subject reverted, or a value assertion's only staged break
  is one that also reds its rc-only form (the 127 break applied to the control), or an observation
  is taken from a run whose arm count nothing asserted — a break that reds nothing and a harness
  that never started print the same empty `FAIL` list, which is what the parent build's first driver
  did for six breaks.
  permission: the leg is held on every boundary, so nothing performs this observation but the hand
  run; the same holds for AC1, AC2, AC4 and AC5, and §7 says so once.

## 7. Gates

`memory-hygiene self-test` · `memory hygiene` · `testsuite counts (every bar self-test prints one)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `spec tokens (a spec's own names resolve)`

**What that list does NOT mean, because its first name is held.** `memory-hygiene self-test` is
`chunk: selftests` and `subject: kit` in `tools/gate-legs.json`, guarded on `tools/lib/` and
`tools/memory-tree/`, and `run-gates.sh` holds every leg matching either chunk or subject unless
`GATE_SELFTESTS=1`, which no boundary sets (owner ruling, 2026-08-27). The guard is passed by this
unit's diff, so a bar that lifts the hold would run it; no bar lifts the hold. Every criterion in §6
is therefore observed by the direct invocation `bash tools/memory-tree/check-memory-hygiene.test.sh`,
by `bash tools/run-gates/run-selftests.sh --kit tools/memory-tree`, or by the one full bar AC3 buys
as `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. A green ordinary bar observes
none of it.

The other names bind at boundaries and are the legs this diff can red: `memory hygiene` because the
checker is unchanged and must stay green over the real tree; `testsuite counts` because it reads the
`PASS (n assertions)` shape and the `FLOOR_ASSERTIONS` line; `harness arms` because it reads this
suite for a positive assertion naming each `fail` branch's text, and a restructured section must keep
them; `lexicon naming predicates` and `install-prefix (shipped surface)` for the two pins §4
Inventory names; `every held leg is budgeted` because the leg's budget row is untouched and must
still resolve; `leg ceilings clear their evidenced maximum` because the ceiling is untouched and the
evidence file is not refreshed; `spec tokens` over this file.

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · one staged break per ASSERTION, as AC5
and AC6 list them: `pk_out` at a missing path for the violated-slug arm's value form; `pk_set` a
no-op for the abort arms, the violated-slug arm and the registry arm's registry half; the probe
commit dropped for the registry arm's probe half; the `READ_PATH_CEILING` conf line dropped for the
control arm's notice half at rc 0; each confirmed red before being unstaged · `FLOOR_ASSERTIONS`
moves UP to the post-change `n` per §8 F2, read off the `PASS` line of the run that measures it,
and its comparison moves to immediately above that line.

## 8. Open questions

- **F1 — batch the valid-key arms into one conf, or keep one run per arm?** The ruling's sentence
  "one run must serve several" reads as the first; §4's measurement says the runs that pair are the
  aborts, which cost 0.16 s a pair, and that batching the proceeding runs on the small tree saves
  32 s inside a 190 s noise band while costing attribution. Recommendation: one run per arm.
  RESOLVED (agent, 2026-09-13, delegated): one run per arm over the small tree, the ruling's sentence
  met where a run genuinely serves several (the clean run serving the check-16 note arms and the
  control) and not stretched over arms that read different conf states. The mechanism was
  delegated by the ruling, which names a direction; the pick follows the table in §4 and M3's rule.
- **F2 — raise `FLOOR_ASSERTIONS` to the measured count, or leave it at 235?** The suite's own
  comment above the constant says the tighter surviving pin wins over recomputing, which argues for
  raising it to the post-change `n` so a block of arms stranded past an exit reds by the floor rather
  than by luck. Against: a floor at the exact count reds the next legitimate arm removal in an
  unrelated unit, and 235 has been the value since the merge that set it. Recommendation: raise it to
  the post-change `n` less nothing, per the suite's precedent, in the same commit that measures it.
  RESOLVED (agent, 2026-09-13, delegated): `FLOOR_ASSERTIONS` is RAISED to the post-change executed
  count in the same commit that measures it, per the suite's own precedent that the tighter
  surviving pin wins, and the comparison is hoisted to immediately above the `PASS` line so the
  pinned number is the printed one (S4, AC4). The counter-argument is the ratchet working as
  designed: an unrelated unit that removes an arm SHOULD red until someone re-pins on purpose,
  because a floor with slack is how a block of arms stranded past an exit goes unnoticed. The slack
  the owner might prefer is exactly the slack that hides the class this pin exists to catch. The
  hoist is part of the pick rather than a separate fork: a raised pin graded at line 2212, before
  the section's thirteen increments, reds the suite on its first run, so the mark cannot be met
  without it.
- **F3 — when AC3 reads red, promote candidate C into this build, or park the row?** The ruling's
  answer is "cheaper" and its measurement is the full bar; §4 shows no quiet reading predicts the
  loaded one, so a red is a live possibility and not a hypothetical. Promoting C lands it in one
  build with its measurement, but it is a fifth unit under a four-unit mandate, moves an engine line
  in `check-verdict-epoch.sh`'s scan set, and owes the five-carrier kit bump that unit 2's F1
  assigns to the closing pass. Parking the row leaves the ruling's expected improvement unmet by
  this unit alone and says so. Recommendation: park.
  RESOLVED (agent, 2026-09-13, delegated): park. The red row is recorded in the ledger and written
  into the build README's "Parked decisions" as the ruling's next input, with candidate C's §4
  figures beside it; the ceiling stays untouched; the unit lands on its other criteria and its close
  names the unmet improvement. Adding a unit and a kit bump is a build-plan change the delegated
  mechanism choice does not reach, and the owner's own README rule already makes whether the number
  then moves "a separate decision with a measurement behind it" — the parked row is that measurement.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft, from the ruling and two timed runs on node `a`.
- rev-2 · 2026-09-13 · §2 S2 S4 S5 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 AC6 · §7 · §8 F2 F3 · folded
  round-1 spec audit clusters H (id 45), G (ids 5, 46), I (ids 7, 22), J (ids 20, 31), K (ids 23,
  24). H: the loaded reading is not derived from a multiplier — this repo's own record
  (`TOOL-dRetiredFork-40`) says the relationship is not one — so AC3 stays the full-bar observation
  and gains a red disposition, F3. G: AC2 is a paired back-to-back ratio with AC1's invocation count
  as the deterministic claim; the 600 s pin is gone and the two omitted readings are admitted. I:
  one staged break per assertion, the control's applied to line 2198 at rc 0. J: F2's body agrees
  with its mark, and the floor comparison hoists to above the `PASS` line. K: the 55% figure points
  at the §4 table; `pk_rc` goes and the pin lowers, no wrapper branch.
- rev-3 · 2026-09-13 · S5 · AC2 · folded round-2 spec audit clusters J (id 14), K (id 15). J: S5
  names the hand-run `GATE_FULL=1 GATE_SELFTESTS=1` bar as AC3's observation and says why the
  landing bar produces no such row (`GATE_CMD`, `.githooks/pre-push`). K: AC2's four readings are
  traced runs, each ledger count read from its own trace, on the class 0.8 was derived from; the
  full-bar row's count is AC1's derived one, said once in S5.

## 10. Reuse audit

The seam this unit extends is inside the suite it edits: the check-16 note fixture built at
`tools/memory-tree/check-memory-hygiene.test.sh` lines 2178-2196, run at line 2198 and removed at
line 2206, plus the `pk_set` / `pk_rc` / `pk_out` helpers at lines 2235-2241. The fixture is already
the shape every other scratch arm in this suite uses, is already asserted clean, and already
provokes a notice at rc 0, which is the positive artifact the control arm needs. Nothing new is
built to hold it.

The map probe found none of that and no claim here rests on it.
`python tools/codebase-map/reuse_lookup.py "one hygiene checker run serves several self-test arms,
conf composed per fixture state"` returned a shortlist ranked on the `run`, `check` and `load_conf`
name stems across the python kits and named nothing in this suite; its own coverage line reports
`unscanned layers: .sh`, so it is blind to the entire shell half of this unit, and the "no existing
seam fits" it would imply is unfounded on that probe alone. Both seams above were found by reading
the file and by the trace in §4, and the probe's silence is recorded as a miss of the probe rather
than as an absence of a seam.

Recall terms used: `hygiene selftest pk_rc pk_out fixture spawn ceiling checker arm conf de-spawn
process-creation cost-is-a-verdict FLOOR_ASSERTIONS`, against the question "why does the hygiene
self-test re-run the whole checker per arm and what bounds a suite's cost". That query returned
`TOOL-aLeakedHandle-8` itself, `TOOL-aPooledSweep-4` (the diagnosed control-arm red), the
`dFramedEntrypoint` enforcement record (181.9 s for this leg on 2026-08-24), `TOOL-dRetiredFork-40`
(443 s under load against 583 s quiet), `TOOL-aBatchedLintel-1` (checks 12 and 7 already collapsed
to one awk each, which is why candidate C's remaining floor is python and not awk) and
`TOOL-dRetiredFork-31` (583 s, "invoking the adopter four more times is not free"), each cited above
where it bears.
