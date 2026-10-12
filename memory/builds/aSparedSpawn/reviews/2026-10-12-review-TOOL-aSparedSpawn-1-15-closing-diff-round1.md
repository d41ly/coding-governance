**Serves:** diff-review TOOL-aSparedSpawn-1 TOOL-aSparedSpawn-2 TOOL-aSparedSpawn-3 TOOL-aSparedSpawn-4 TOOL-aSparedSpawn-5 TOOL-aSparedSpawn-6 TOOL-aSparedSpawn-7 TOOL-aSparedSpawn-8 TOOL-aSparedSpawn-9 TOOL-aSparedSpawn-10 TOOL-aSparedSpawn-11 TOOL-aSparedSpawn-12 TOOL-aSparedSpawn-13 TOOL-aSparedSpawn-14 TOOL-aSparedSpawn-15

# Tier-2 closing diff review: aSparedSpawn, ROUND 1

*This is the closing review of build aSparedSpawn (gov, node `a`, 2026-10-12). It covers the
cumulative diff of the build's fifteen units at the integration boundary. The units cut
process-creation cost in the gate runner (`tools/run-gates/run-gates.sh`), the unattended driver
(`tools/unattended/`) and the self-test suites, and do correctness work on the reuse path. The base
b9b24646f is the run branch's reconcile merge with origin/main 69e0ff0f5. Every commit after it
belongs to this build, and the five commits before that merge are spec and records only. Every
finding below survived a skeptic prompted to REFUTE it.*

**Reviewed range:** b9b24646fc42217a536293fb712bafc91a500793...f479ba4294038a7dc869ea41795a639993a3b084. **ROUND:** 1.

## Verdict: CLEAN WITH FIXES

No blocker survived. Three HIGH findings must be fixed before the close lands. Id 3 lets a
red that an age-forced execution just observed be followed by the stale cached `ok` at the same
key, including at push. Id 6 is an A/B instrument that certifies runs which executed nothing, and
the next width change would be tuned from it. Id 20 is a spawn-budget leg that reports `GATE ok`
on CI's bash after grading no row. Two MEDIUM findings, ids 9 and 10, make the build's own HEAD
bar red today: a generated pin file and a spawn-idiom registry both drifted from their
populations. Those gates are redding correctly, but the close cannot push until both are repaired.
The tally is 17 items covering 21 confirmed findings: 0 blocker, 3 HIGH items (3 findings), 8
MEDIUM items (11 findings) and 6 LOW items (7 findings).

## Review shape

Intensity full: raw 23, confirmed 21, refuted 2, unverified 0 (0 uncertain), precision 0.91.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| correctness | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| seams | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| verification | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| intent | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |

Adjudicated tally, by item: 0 BLOCKER, 3 HIGH, 8 MEDIUM, 6 LOW (17 items). By raw confirmed
finding: 0 blocker, 3 high, 11 medium, 7 low (21 findings). The ids returned with this report
carry the same split.

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and 0
  duplicates were dropped.
- Fixes on confirmed findings: 13 judged sound, 8 judged UNSOUND, 0 with no fix proposed, 0 NOT
  JUDGED. An unjudged fix would be the finder's proposal and nothing more; none occurs here.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 5 RE-GRADED by the skeptic (ids 1, 4,
  9, 10 and 15, each from high to medium).
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 16 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 75 items, each assigned to exactly one of the 5 lenses (15 each to security,
  correctness, seams, verification and intent).
- By design: the caller's byDesign list was fed to every lens.

Every integrity count is zero, so this run is complete. Refuted: id 2 (no caller of
`run-held-wsl.sh` exports `GIT_DIR`) and id 5 (the `--only 15` overlap is specified and announced).

## Security model applied

These are local developer and CI gates, not a network service. The trust boundary is that a gate
never reports green for bytes that did not run. A reused verdict never stands in for an
authoritative full bar, except where the owner ruled: unit 13 reuses remote and history legs at
pre-push, at the exact sha, stamped scoped, and never full. No change may let a push land on a red
it would previously have caught. Ids 1, 3 and 12 sit on that boundary. Ids 4, 15 and 20 sit on
"never green for bytes that did not run".

## HIGH

### H1. An age-forced execution that reds leaves the stale cached `ok` in place (id 3)

- **Where:** `tools/run-gates/run-gates.sh:3100`, with the disagreement loop at `:4562` and the
  cache block at `:4819`.
- **Defect:** when the S7 age bound forces a leg to execute, the runner writes `$WORK/$i.aged` and
  nothing reads it. The disagreement loop iterates only `*.sampled`. An aged execution that reds
  against the cached `ok` therefore neither erases the entry nor quarantines the leg. The cache
  block then resets the age counter to 0 for every executed leg, red ones included, so the stale
  `ok` gets a fresh 10-run allowance. The same holds for any non-sampled execution that reds
  against a cached `ok`.
- **Impact:** S7 promises that a wrong entry lives at most 10 runs. In push mode, a retried push of
  the same sha with the same tip and base has the same key, so the leg is reused unless the 25%
  draw picks it. The push can land green on a leg that just went red at that sha. It needs a wrong
  entry first, from an under-declared read or a flaky leg, hence high rather than blocker.
- **Fix (skeptic judged it SOUND):** treat every executed leg like a sampled one. After the serial
  retry, run the disagreement loop over `*.aged` as well as `*.sampled`, or more generally over any
  executed leg whose effective rc is non-zero and whose key has an `ok` entry. Erase that entry and
  quarantine the leg against its row hash, as the S6 branch does. Delete the `.aged` marker if it
  stays unread. Coordinate with L4 (id 14), which touches the same marker.
- **Left-shift gate:** an evidence-suite arm that seeds a cache `ok` for a leg, sets its age to 10,
  makes the leg exit 1, and asserts that the entry is gone afterwards and that the next reuse run
  executes the leg rather than printing `GATE reuse`.

### H2. The width A/B instrument certifies arms that executed nothing (id 6)

- **Where:** `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh:50`,
  with the artifact count at `:59`.
- **Defect:** each arm runs held self-test legs with `GATE_FULL=1` but without `GATE_SELFTESTS=1`.
  `GATE_FULL` deliberately does not ask for held legs (`run-gates.sh:2674`), so every leg is written
  `ondemand` and printed `GATE held` (`:3440`). The bar refuses with "executed NOTHING" and exit 1,
  which the script ignores. The positive artifact `grep -cE '^GATE [a-z]+ '` counts the `held`
  lines, so the column reads `art=yes`.
- **Impact:** all six rows record roughly one-second walls certified as real work. Those rows are
  meant to replace the provisional `CALIBRATE_THETA=90` and the row widths, so the next change would
  pick a width from noise. This misleads the next change, hence high.
- **Fix (skeptic judged it SOUND):** set `GATE_SELFTESTS=1` in the arm's environment. Count only
  executed verbs as the artifact (`^GATE (ok|FAIL) `, with `retry` interims excluded), and require
  exactly one such line per manifest leg. Re-run the A/B before any width knob moves.
- **Left-shift gate:** a documented check for A/B instruments in this repo (the "an A/B arm must
  prove it ran" class): the artifact pattern must exclude every non-executing verb the runner can
  print (`held`, `skipped`, `reuse`), and the instrument must fail on a non-zero bar exit.

### H3. The spawn-budget leg reports `GATE ok` after grading no row (id 20)

- **Where:** `tools/gate-lint/fork-count.sh:168` (`check_budgets`), with the rows in
  `memory/project/fork-ceilings.txt`.
- **Defect:** every declared row is for bash 5.3. On any other bash every row prints `skipped`, the
  summary reads `0 passed · 0 red · N skipped`, and `check_budgets` returns `[ "$red" = 0 ]`, which
  is 0. `remote-ci.yml` runs the full bar on windows-latest, whose Git Bash the unit 8 spec names as
  5.2, so the CI bar certifies a fork budget it never measured. The script contradicts itself:
  `read_budgets` refuses a file with no row because that "graded NOTHING", yet a file whose rows all
  name another version grades nothing and exits 0. A mistyped `--only <id>` also exits 0.
- **Impact:** owner ruling F1(a) accepts a `skipped` shape for an undeclared version, but its stated
  reason, keeping the stale-ceiling red meaningful on each platform, assumes rows exist for each
  platform. None exist for 5.2, so the leg is in effect the rejected option (c), reported green.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** in
  `check_budgets`, return 2 when `ok + red == 0` (nothing was graded), with a line naming the
  running bash. Keep per-entrypoint version skips as the `skipped` shape that ruling (a) requires.
  Add bash 5.2 rows measured on CI's bash so the CI bar grades something. Add a selftest arm in
  which a file declaring only another bash version exits 2.
- **Grade note:** the skeptics on the two duplicates of this defect (M1, ids 4 and 15) graded it
  medium, because the leg is a cost budget and node a's 5.3 bar does grade it. This reviewer agrees
  with medium on consequence, but id 20's binding grade is high and it is reported here as high.
  The three findings should be fixed as one change.
- **Left-shift gate:** the selftest arm in the fix, plus a refusal arm for an `--only` id that
  matches no declared row (see M1).

## MEDIUM

### M1. The same vacuous spawn-budget pass, and the `--only` typo (ids 4, 15)

- **Where:** `tools/gate-lint/fork-count.sh:168`.
- **Defect:** the defect is the one in H3. Id 4 adds that `--only <id>` naming no row prints
  `0 passed · 0 red · 0 skipped` and exits 0. Id 15 adds that the summary line says a skipped row is
  not a pass while the exit status says it is.
- **Fix for id 4 (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):**
  refuse with exit 2 an `--only` id that names no declared row, listing the declared ids. For the
  all-skipped case, add bash 5.2 rows for the entrypoints to `memory/project/fork-ceilings.txt`,
  measured on CI's Git Bash, in the same change as making `ok + red == 0` exit 2. Without those
  rows, keep exit 0 when every row is skipped.
- **Fix for id 15 (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):**
  measure and declare rows for bash 5.2 (CI's windows-latest bash) in
  `memory/project/fork-ceilings.txt`. Once rows exist for every bash that runs the bar, make a run
  that grades zero rows on a declared-elsewhere file print a distinct, prominent note naming the
  running bash. Keep it a refusal only for the bar's own platforms.
- **Reconciling the three corrected fixes:** they agree on the order of work. Declare 5.2 rows
  first, then make a zero-graded run refuse (H3, id 4) or announce (id 15). Once the 5.2 rows exist,
  a zero-graded run on a bar platform means the rows are missing, which should refuse. Choose one
  rule and state it in the script header.
- **Left-shift gate:** the H3 selftest arm, and an arm that runs `--only no-such-id` and expects
  exit 2 with the declared ids listed.

### M2. The build's own HEAD bar is red on two drifted registries (ids 9, 10)

- **Where:** `tools/govkit/subject-pins.tsv:47` (id 9) and `memory/project/spawn-idiom-sites.txt:199`
  (id 10).
- **Defect, id 9:** unit 5 added the `held-halves selftest` leg to `tools/gate-legs.json:1202` but
  never added its row to the generated `subject-pins.tsv`. Unit 8 later hand-edited the pin file and
  still left it out. `govkit selfcheck` prints "gate leg 'held-halves selftest' has no row in
  tools/govkit/subject-pins.tsv — a NEW leg reds".
- **Defect, id 10:** the spawn-idiom registry was last written in unit 4 (eaab1dd38). Units 7, 9,
  12, 13 and 14 moved the counted sites. The leg's exact argv exits 1 with seven findings:
  `run-gates.sh` cat-file 15 to 16, `run-gates.test.sh` cat-file 23 to 24, printf-subst 2 to 3 and
  var-pipe 136 to 141, `run-gates.evidence.test.sh` cat-file 11 to 14, `.githooks/pre-push.test.sh`
  cat-file 8 to 12, and `check-unattended.sh` var-pipe 26 to 25. The last one fell, which the
  shrink-only rule also reds.
- **Impact:** both legs run on every default bar, so f479ba4 cannot get a green bar and every push
  from it is red. The gates are doing their job; nothing false is certified.
- **Fix for id 9 (skeptic judged it SOUND):** regenerate with
  `python tools/govkit/govkit.py selfcheck --write`, which adds
  `held-halves selftest<TAB>kit<TAB>selftests`, and commit the result in the same change. Do not
  hand-edit the generated file.
- **Fix for id 10 (skeptic judged it SOUND):** remove the new forking sites, for example
  `$(cat …)` to `$(<…)` or `read`. Otherwise re-measure and update each row, and lower
  `check-unattended.sh` var-pipe to 25, so the leg runs green at HEAD.
- **Left-shift gate:** both drifts come from units landing without running the default bar's
  declaration and product chunks. A per-pass check in the unit builder that runs the
  `govkit selfcheck` and `shell hygiene` legs (both cheap) would catch each at the unit that caused
  it rather than at the close.

### M3. Push-time reuse cannot match an entry earned outside a git hook (ids 11, 21)

- **Where:** `tools/run-gates/run-gates.sh:2912` (`REUSE_DIGEST`, around `:2891-2913`), with
  `.githooks/pre-push:36` and the hook's exports at `:1507`, `:1517` and `:1547-1549`.
- **Defect:** the toolchain and environment digest hashes the exported `PATH`, every `GIT_*`
  variable, and the `type -P` path of each leg tool. Git exports `GIT_EXEC_PATH` and prepends its
  exec path to `PATH` for every hook, and the hook deliberately keeps `GIT_EXEC_PATH`. Measured on
  this node: a plain shell resolves `git` to `/mingw64/bin/git`, a git child resolves it to
  `/mingw64/libexec/git-core/git`. The hook also exports `GATE_ATTRIBUTE`, `GATE_INHERITED_RED`,
  `GATE_INHERITED_RED_MAX_AGE` and `GATE_DOCS_BASE` before the bar, and none is excluded from the
  digest.
- **Impact:** every remote and history key from a developer, DoD or unattended bar misses at push.
  Spec 13's "a push right after a green bar at the same sha and tip reuses the trio" cannot happen,
  except for a retried push whose earning run was itself a hook run. It fails safe (a miss, never a
  false hit), but the owner-ruled saving is inert. AC12 and AC13 set `GATE_REUSE_PUSH` directly on
  the runner, so they prove the design only by construction.
- **Fix for id 11 (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** drop
  `GIT_EXEC_PATH` and the raw `env PATH=` line from the digest. Let the `tool` lines carry what PATH
  decides: resolve them with `type -P` under a PATH whose leading entry is removed when it ends in
  `/libexec/git-core`. `git version` is already hashed. Add an arm that earns an entry from a plain
  bar and reuses it through a real `git push` hook invocation.
- **Fix for id 21 (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** leave
  out of the digest's env loop `GIT_EXEC_PATH` and the hook-only knobs `GATE_ATTRIBUTE`,
  `GATE_INHERITED_RED`, `GATE_INHERITED_RED_MAX_AGE` and `GATE_DOCS_BASE`, which decide red
  attribution or leg selection, not a leg's own ok. Hash PATH with a leading `$GIT_EXEC_PATH`
  component (in both its native and MSYS spellings) stripped, or have pre-push restore the pre-git
  PATH and unset those knobs for the digest. Bump `REUSE_SCHEMA`. Add an end-to-end arm: earn with a
  direct bar, push through the real `.githooks/pre-push` with a scoped decision, and assert
  `GATE reuse` on a remote leg.
- **Reconciling the two corrected fixes:** they are compatible. Id 21's is the superset; apply it,
  and take id 11's rule for resolving the `tool` lines.
- **Left-shift gate:** the end-to-end arm both corrected fixes name. It is the only arm that can see
  this class, because any arm driving the runner directly shares the earning run's environment.

### M4. The push bar inherits `GATE_REUSE_SAMPLE` and `GATE_REUSE_DAY` from the caller (id 1)

- **Where:** `.githooks/pre-push:1436` (the scrub at `:1436-1457`), with the reads at
  `tools/run-gates/run-gates.sh:2937` and `:2947`.
- **Defect:** the hook clears `GATE_REUSE` and `GATE_REUSE_PUSH` but not `GATE_REUSE_SAMPLE` or
  `GATE_REUSE_DAY`, and the runner reads both whatever the reuse mode. An exported
  `GATE_REUSE_SAMPLE=0` means no remote or history leg is ever drawn at push. A pinned
  `GATE_REUSE_DAY` lets the memory hygiene row (`gate-legs.json:1451`, base+clock+history) match an
  earlier day's entry at push. `GATE_REUSE_*` is also excluded from the key digest, so the inherited
  value does not change the key.
- **Impact:** spec S10 says the S6 sample applies unchanged at push. The hook's own comment says an
  inherited `GATE_REUSE_PUSH` "would let the environment decide which legs a vetted runner spares",
  and that reason applies equally here. Graded medium: the developer's shell must export the knob
  and a wrong cache entry must exist, and the S7 age bound still forces execution (but see H1 and
  M5 for how weak that bound is today).
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** in
  `.githooks/pre-push`, unset `GATE_REUSE_SAMPLE` and `GATE_REUSE_DAY` beside `GATE_REUSE_PUSH` for
  every bar, a STUB included, and add each to `ENV_CLEARED` when it was set. Leave the runner
  reading both: they are its own suite's seams. Add a `pre-push.test.sh` arm that exports
  `GATE_REUSE_SAMPLE=0` and asserts the "not honoured from the environment" line names it.
- **Left-shift gate:** the arm in the fix, generalised: enumerate every `GATE_REUSE*` name the
  runner reads and assert each is either cleared by the hook or listed as a deliberate pass-through.
  That catches the next knob as well.

### M5. The S7 age counter is keyed by leg name in a shared cache (id 12)

- **Where:** `tools/run-gates/run-gates.sh:3097` (the reuse block, `:3097-3101`), with the reset in
  the cache block near `:4818`.
- **Defect:** the counter lives at `$REUSE_CACHE/age.<name key>` in the common-dir cache that every
  worktree shares. Any execution of that leg resets it to 0, in any worktree, under any key, on a
  clean or dirty tree. An execution under key K2 never re-checks K1's entry.
- **Impact:** alternating runs in another worktree or on a dirty tree keep resetting the counter, so
  K1 can be served past 10 consecutive reuses, bounded only geometrically by the 25% sample. Spec 13
  itself specifies `age.<name key>`, but its S7 promise that "a wrong entry survives at most that
  long" does not follow from that mechanism. Contained: it lengthens a stale entry's life.
- **Fix (skeptic judged it SOUND):** keep the consecutive-reuse count per cache key: store it in the
  entry itself, or as `age.<key>` beside it. Reset it only when that key's leg executes. Or have the
  10th reuse delete or expire the entry, so the next run must re-earn it. Amend spec 13 S7 to match.
- **Left-shift gate:** an evidence arm with two keys for one leg: reuse K1 nine times, execute the
  leg under K2, then assert K1's next reuse still counts toward its bound and is forced at the tenth.

### M6. Arms 9k and 9m place a signal with a fixed sleep (id 16)

- **Where:** `tools/run-gates/run-gates.test.sh:3074`.
- **Defect:** 9k's sleeper runs 12 s and 9m's 15 s, with a 2 s ceiling. The worker writes `.defer`
  only after its own post-processing, and the tail retry starts after the reader wakes on that
  worker's `.rc`. Unit 3's ledger and the 9l comment measure that release at 10 to 14 s on node a,
  so the retry starts at roughly 12 to 16 s, at or after the sleeper's end.
- **Impact:** on the owner's node, 9k's "tail retry's row starts before the sleeper's row ends", its
  `.defer` peek, and 9m's "set-aside tail attempt timed out beside the sleeper" can read
  `after-drain` or 0, and the canary reds on a correct runner. That is the load-dependent flake
  unit 15 set out to remove.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** have each
  sleeper poll on facts with a 120 s hang bound. In 9k:
  `i=0; while [ ! -e "$TMPDIR/../1.retry.pid" ] && [ $i -lt 1200 ]; do sleep 0.1; i=$((i+1)); done`,
  then `ls "$TMPDIR/.." > "$HV_PEEK"` and exit 0 (nothing removes `1.defer`, so it is still
  listed). In 9m: poll the same way until `$TMPDIR/../1.retry.rc` exists, which means the tail
  attempt started and timed out beside the sleeper, then exit. Alternatively, size the fixed sleeps
  as ceiling + 2×14 s and cite the measured release in the comment.
- **Left-shift gate:** a lint over the `*.test.sh` suites that flags a fixture `sleep <N>` whose
  comment or neighbouring arm asserts an ordering against another process, the
  fixed-sleep-does-not-place-a-signal class. Where that is too noisy, add the class to the review
  checklist.

### M7. No arm guards a retried green out of the reuse cache (id 17)

- **Where:** `tools/run-gates/run-gates.test.sh:2930`, with the cache writer near
  `tools/run-gates/run-gates.sh:4813`.
- **Defect:** arm 9d once checked that a ledger row reading `retried` is never reused. It now checks
  only that, with the cache gone, an `ok` row runs. The cache writer keeps a retried green out of
  the cache only because it reads `$WORK/$i.rc`, the first attempt's result, and nothing asserts
  that.
- **Impact:** a refactor folding the tail-retry result into `.rc` would cache a retried green as
  proven, and later runs would serve it as `GATE reuse` with no arm going red. The code is correct
  today, so this is a test gap.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** put the check
  in 9f (the contended fixture), not 9c, before `unset HV_FLAG`. Take `_rec` as the newest
  `$H1/.git/gate-run/*/`, then read the contended leg's key from field 7 of `${_rec}1.leg`; it is leg
  1, not `0.leg`. Assert that `$H1/.git/gate-cache/${k:0:2}/$k` does not exist. As the control, read
  the spinner's key from field 7 of `${_rec}0.leg` and assert its cache entry does exist. Do not
  rerun the fixture after `HV_FLAG` is unset.
- **Left-shift gate:** the arm in the fix is the gate.

### M8. The evidence suite's floor lags unit 13's arms (id 18)

- **Where:** `tools/run-gates/run-gates.evidence.test.sh:156` (`FLOOR_ASSERTIONS`), checked at
  `:1979`.
- **Defect:** `FLOOR_ASSERTIONS` is still 151, last raised by unit 4. Commit ca969ce3a (unit 13)
  added 73 ok/nope/skipped call lines and removed 11, roughly 30 or more executed assertions. Units
  1, 3 and 4 each raised the floor; unit 13's records say nothing about it.
- **Impact:** an early exit that strands every unit-13 reuse, sample, quarantine and push-mode arm
  still clears `n -ge FLOOR`, and the suite passes.
- **Fix (skeptic judged it SOUND):** raise `FLOOR_ASSERTIONS` by the unit-13 arms, counted as units
  1, 3 and 4 counted theirs, with a "RAISED 151 -> N by TOOL-aSparedSpawn-13" line. Mark it OWED:
  observed at VERIFYING, as the other floors in this build are.
- **Left-shift gate:** have check-arms (unit 14's home for floors and ceilings) compare each suite's
  declared floor against the arms a diff adds. A commit that adds executed `ok`/`nope` lines to a
  floored suite without a RAISED line then reds at that commit, not at the close.

## LOW

### L1. `held_halves.py` reads runner stdout in text mode (id 7)

- **Where:** `tools/run-gates/held_halves.py:150` (`load_half`).
- **Defect:** universal-newline mode turns a bare CR in a failing leg's echoed output into a newline
  before `parse_verdicts` (`profile_bar.py:103`) runs. That undoes the LF-only split that stops leg
  output injecting a `GATE <verb> <name>` row.
- **Impact:** contained. Most injections end in a refusal, and the failing half's verdict keeps the
  exit red. A narrow case remains in which an injected line replaces an interim retry row and skews
  the per-leg display or the parity rows.
- **Fix (skeptic judged it SOUND):** open the stdout file with `newline=""`, or read bytes and
  decode, so `parse_verdicts` receives the runner's exact bytes.
- **Left-shift gate:** a `held_halves` selftest arm whose failing-leg output contains
  `\rGATE ok    <other leg>` and asserts the per-leg view is unchanged. Note the memory entry
  that MSYS awk and grep drop CR, so the arm must be in Python.

### L2. Two heartbeat rules disagree on an `EPOCHSECONDS` fallback (id 8)

- **Where:** `tools/run-gates/run-gates.sh:1382`, the ticker at `:1433`, and `write_work_owner` near
  `:1815`.
- **Defect:** the ticker writes `${EPOCHSECONDS:-$(ts_now)}`, and the comment at `:1422-1423` says
  `ts_now` is kept as the fallback. Meanwhile `ts_hb`, `ts_try_reap`, `TS_NONCE`, `ts_start` and
  `write_work_owner` now read `$EPOCHSECONDS` bare, and this diff removed `write_work_owner`'s
  `${EPOCHSECONDS:-$(date +%s)}` fallback.
- **Impact:** no supported host lacks `EPOCHSECONDS` (Git Bash and the Linux CI run bash 5), and the
  base already used it bare under `set -u` elsewhere. What remains is a misleading comment and a
  misleading lone fallback.
- **Fix (skeptic judged it SOUND):** pick one rule. Either drop the `${EPOCHSECONDS:-$(ts_now)}`
  fallback and state that bash 5 is required, or restore the fallback at every converted site.
- **Left-shift gate:** none worth building; a one-rule comment at the top of the runner is enough.

### L3. A sample run overwrites the red attempt's durable log (id 13)

- **Where:** `tools/run-gates/run-gates.sh:4572`, with `runleg` at `:3326-3331` and `report_one`
  at `:3479` and `:3965`.
- **Defect:** `runleg "$i" .sample` writes the durable log to `leg_log "${names[$i]}"`, named by leg
  name alone, which overwrites `<git-dir>/gate-logs/<leg>.log`. `FAILED_LEGS` already points there
  as the `log:` for the red first attempt.
- **Impact:** on a `nondeterministic` outcome the pointer opens a passing `exit 0` log. Only the
  operator-facing log is affected. The `.retry` path had the same overwrite at base.
- **Fix (skeptic judged it SOUND):** in `runleg`, skip the gate-logs write when the suffix is
  `.sample`, or write those runs to `<leg>.sample.log`, so the pointer keeps naming the attempt that
  redded the run.
- **Left-shift gate:** an evidence arm on the nondeterministic path asserting the `log:` file holds
  the failing attempt's exit code.

### L4. Reuse markers never reach the leg's own line (ids 14, 22)

- **Where:** `tools/run-gates/run-gates.sh:3100` (id 14) and `:3112` (id 22), with `report_one`
  from `:3420`.
- **Defect, id 14:** when a leg reaches the age bound, the runner writes `$WORK/$i.aged` holding its
  key, and nothing reads it. The record cannot tell an age-forced execution from an ordinary miss.
- **Defect, id 22:** spec 13 lines 150 and 242 say a sampled leg's line says it was sampled. The
  code only writes `.sampled`, `report_one` prints the plain `GATE ok`/`GATE FAIL` line, and a green
  sample is mentioned only in a stderr note at `:4569`.
- **Impact:** verdicts are unaffected. Anyone measuring how often the sample or age bound fires
  cannot read it from the leg lines or the run record.
- **Fix for id 14 (skeptic judged it SOUND):** delete the write, or have `report_one` or the run
  record read `.aged` and print an `(aged)` tail on the leg's `GATE ok/FAIL` line, the way spec S6
  asks a sampled leg's line to say it was sampled. If H1's fix makes the disagreement loop read
  `.aged`, keep the marker and add the tail.
- **Fix for id 22 (skeptic judged it SOUND):** in `report_one`, when `$WORK/$i.sampled` exists, add
  a tail to the leg's line, for example `GATE ok    <leg>  (sampled against a cached ok)`. Do this
  under the two-space tail contract so name-splitting readers still work, or else amend spec §4 to
  describe the stderr note that was actually built.
- **Left-shift gate:** the dead-plumbing class (a `$WORK/<i>.<suffix>` written with no reader) is
  greppable. A runner selftest arm can list every `$WORK/$i.<suffix>` write and assert each suffix
  also appears in a read or glob.

### L5. A failed key measurement is silent (id 19)

- **Where:** `tools/run-gates/run-gates.sh:2813` (`build_input_keys`), and `REUSE_DIGEST`.
- **Defect:** when the bulk half fails (awk, mapfile, the key-file write, hash-object, or a count
  mismatch), it returns 0 and leaves the remaining legs' keys reading `-`. An empty `REUSE_DIGEST`
  does the same for every leg. Neither prints anything.
- **Impact:** under `GATE_REUSE` or `GATE_REUSE_PUSH` nothing is reused or cached, and the run looks
  exactly like a cold cache. Fail-safe; only diagnostics are lost.
- **Fix (skeptic judged it SOUND):** when the bulk half or the digest fails and the reuse mode is
  not off, or a cache write was otherwise due, print one
  "run-gates: reuse — the input keys could not be measured (<which step>), so nothing is reused or
  cached this run" line on stderr.
- **Left-shift gate:** an evidence arm that breaks the digest step (for example a fault seam
  shadowing `hash-object`) and asserts the line appears.

### L6. Spec 14's AC11 contradicts its own S10 (id 23)

- **Where:** `memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-14.md:295`.
- **Defect:** AC11 grades "the six checks'" environment exits routed through `die_env`. S10
  (rev-3, line 114) says "the other five checks' nine sites" (27, 29, 56, 69, 88). The shipped
  helper is `print_env_failure` (`unattended.sh:779`), called at nine sites across exactly those
  five checks.
- **Impact:** spec text only. Whoever grades AC11 at VERIFYING will look for a sixth check and a
  helper name that does not exist.
- **Fix (skeptic judged it SOUND):** rewrite AC11 to name five checks (27, 29, 56, 69, 88), the nine
  sites, and the helper `print_env_failure`, so it agrees with S10 and with the rev-4 note on helper
  names.
- **Left-shift gate:** none practical; this is the two-answers-to-one-question class, caught by the
  spec's own revision pass.

review-shape kind=diff-review round=1 intensity=full at=synth raw=23 confirmed=21 refuted=2 unverified=0 blocker=0 high=3 medium=11 low=7 agents=11 out-tokens=327099

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | .githooks/pre-push:1436 | high | medium | confirmed | Confirmed. .githooks/pre-push:1436-1457 scrubs only GATE_LEGS, GATE_REUSE, GATE_SPAWN_CMD, GATE_SPAWN_FLOOR, GATE_VERDICT_FAULT, GATE_DOCS_BASE and GATE_REUSE_PUSH. run-gates.sh:2937 still reads GATE_REUSE_SAMPLE and :2947 still reads GATE_REUSE_DAY whatever REUSE_MODE is, including push. So an exported GATE_REUSE_SAMPLE=0 means no remote or history leg is ever drawn at push. A pinned GATE_REUSE_DAY lets the memory hygiene row match an earlier day's entry at push, because it declares base+clock+history and push mode admits any leg with history. That row is at gate-legs.json:1451. The hook's own comment gives the reason GATE_REUSE_PUSH is scrubbed: an inherited value 'would let the environment decide which legs a vetted runner spares'. That reason applies equally to these two knobs. Graded medium, not high: the path needs the developer's shell to export the knob (the suites set it only inside their own fixture subshells) and a wrong cache entry to exist. The S7 age bound still forces execution within 10 runs. | unsound | - |
| 2 | security | tools/run-gates/run-held-wsl.sh:194 | medium | - | refuted | No reachable path could be established. run-held-wsl.sh is an operator tool run by hand from the Windows side: its header lists `bash <prefix>/run-gates/run-held-wsl.sh [--paired\|--setup]`. A grep finds no hook, runner, workflow or script that invokes it; only held_halves.py, kit.toml and README.md name it. The scenario 'git exports GIT_DIR for hooks' would need a hook to call this script, and none does. An operator's interactive shell does not export GIT_DIR. The finder graded it medium and the inherited-GIT_DIR precondition cannot be shown reachable, so it is refuted. | sound | inherited-git-dir-pins-the-work-tree-to-the-cwd |
| 3 | correctness | tools/run-gates/run-gates.sh:3100 | high | high | confirmed | Confirmed. When _age>=10, run-gates.sh:3100 writes $WORK/$i.aged and the leg executes, but nothing ever reads `.aged`. The disagreement loop at :4562 iterates only `*.sampled`, so an aged execution that reds against the cached `ok` neither erases the entry nor quarantines the leg. The cache block at :4819 then resets age to 0 for every executed leg, red ones included, and writes no entry on red. The stale `ok` under the same key therefore survives with a fresh 10-run allowance. That contradicts S7: 'a wrong entry survives at most that long'. In push mode, a retried push of the same sha with the same tip and base has the same key, so the leg is reused unless the 25% draw picks it. The push can then land green on a leg that just went red at that sha. Graded high, not blocker: it needs a wrong entry in the first place, such as an under-declared read or a flaky leg. | sound | - |
| 4 | correctness | tools/gate-lint/fork-count.sh:168 | high | medium | confirmed | Confirmed. In tools/gate-lint/fork-count.sh, check_budgets ends with `[ "$red" = 0 ]`. When every row is skipped, the script prints '0 passed · 0 red · N skipped' and exits 0. Every row in memory/project/fork-ceilings.txt is declared for bash 5.3, so on CI's Git Bash 5.2 the 'spawn budget' leg reads GATE ok having counted nothing. An --only id that matches no row also exits 0 with '0 passed · 0 red · 0 skipped'. Spec 8 §5 says an empty population refuses with 2 and a skipped entrypoint 'is never a pass', and read_budgets already refuses an empty file for that reason. Owner ruling F1(a) makes a single undeclared version print skipped; it does not make a vacuous whole run a pass. Graded medium: the leg is a performance budget and counts properly on 5.3 nodes, so no correctness verdict is affected. | unsound | vacuous-selector-empty-population |
| 5 | correctness | tools/unattended/check-unattended.sh:5916 | medium | - | refuted | By design and documented. Spec 7 line 55 states that a number naming both a core check and a post-28 header (15) 'selects the post-28 block alone'. check-unattended.sh:147-148 repeats this. Core checks 1-27 are deliberately not selectable one at a time because they share state. The liveness line also lists `core` under 'skipped', so a scoped run does not claim the core fail-15 branches ran. | sound | liveness-negative-from-another-population |
| 6 | correctness | memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh:50 | high | high | confirmed | run-gates.sh:2674 states that GATE_FULL deliberately does NOT ask for held legs. At 2696-2698 a leg with subject=kit or chunk=selftests is written as 'ondemand' whenever GATE_SELFTESTS is empty, and report_one at 3440 prints `GATE held  <name>  (self-test, ...)`. The width-ab.sh arm (line 50) sets GATE_FULL=1 but never sets GATE_SELFTESTS, and its manifest is described as 'held self-test legs'. So every leg is held. The bar then takes the 'executed NOTHING' refusal at 4737 and exits 1, and the script ignores that exit. `grep -cE '^GATE [a-z]+ '` counts the held lines, so gl >= nlegs and art=yes. Each row therefore certifies a run that did no work, and the best-wall width that will replace the provisional width knobs is picked from noise. No push gate is involved, but the tool will mislead the next change, so this is high. | sound | ab-arm-never-did-the-work |
| 7 | correctness | tools/run-gates/held_halves.py:150 | low | low | confirmed | held_halves.py is new in this diff; it is absent at the base. load_half opens stdout in default text mode, which applies universal newlines and turns a bare CR into LF. parse_verdicts (profile_bar.py:103) splits on LF only, specifically so that leg output cannot inject verdict rows. The runner echoes a failing leg's output with `sed 's/^/    /'`, which leaves embedded CRs in place, so `\rGATE ok    X` becomes its own matching line. Most injections end in a refusal rather than a green: check_halves refuses on a duplicate, on an out-of-population name, or on wrong-host placement, and the failing half's verdict keeps the exit red. A narrow case remains in which an injected line replaces an INTERIM retry row and skews the per-leg display or the parity rows. The effect is contained, so this is low. | sound | text-mode-read-eats-a-bare-cr |
| 8 | correctness | tools/run-gates/run-gates.sh:1382 | low | low | confirmed | The inconsistency is real and the diff introduced it. The ts_hb, TS_NONCE, ts_start and write_work_owner sites were converted from ts_now/date to bare $EPOCHSECONDS, and the base's `${EPOCHSECONDS:-$(date +%s)}` fallback at write_work_owner was dropped. Meanwhile the ticker keeps `${EPOCHSECONDS:-$(ts_now)}`, and the comment at 1422-1423 claims ts_now is 'kept as the fallback where the shell has no EPOCHSECONDS'. The claimed runtime impact is not reachable on any supported host: Git Bash and the Linux CI both run bash 5. The base already used bare EPOCHSECONDS under `set -u` at the mempause, reap-deadline and wall-loop sites. Also, `$(( EPOCHSECONDS - ts_start ))` uses a bare name, so it would hit an unbound-variable error under set -u, not the `$(( - ))` the finder describes. What remains is a misleading comment and a misleading lone fallback, so this is low. | sound | - |
| 9 | seams | tools/govkit/subject-pins.tsv:47 | high | medium | confirmed | gate-legs.json:1202 declares 'held-halves selftest' (subject kit, chunk selftests), and the base has no such leg. tools/govkit/subject-pins.tsv has no row for it: grep finds none. The pin file was touched in this range only by d5e7fc276 (unit 8). govkit.py:2958-2963 fails selfcheck for any live leg missing from the pins. 'govkit selfcheck' is a repo-subject leg in chunk declarations with no guard, so it runs on default bars and is red at HEAD. The gate catches the defect itself: it blocks the build's push but cannot ship a wrong green. The effect is contained, so this is medium rather than high. | sound | - |
| 10 | seams | memory/project/spawn-idiom-sites.txt:199 | high | medium | confirmed | I ran the leg's exact argv read-only: `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`. It exits 1 with exactly the 7 findings cited, including check-unattended.sh var-pipe at 26 declared against 25 measured, which the shrink-only rule also reds. The registry was last written in eaab1dd38 (unit 4), and later units moved the counted sites. The leg 'shell hygiene (a fork spent on builtin work)' is repo-subject in chunk product with no guard, so it runs on every default bar and is red at HEAD. As with id 9, the gate reds correctly rather than certifying anything false. It blocks the push and the effect is contained, so this is medium. | sound | - |
| 11 | seams | tools/run-gates/run-gates.sh:2912 | medium | medium | confirmed | Confirmed. REUSE_DIGEST (run-gates.sh:2891-2913) hashes every exported GIT_* and PATH, plus `type -P` for each leg's argv[0]. .githooks/pre-push:38 scrubs GIT_DIR and its siblings but deliberately keeps GIT_EXEC_PATH, and it never normalises PATH before it calls the runner. I measured this on this node. A plain shell has GIT_EXEC_PATH unset and `type -P git` = /mingw64/bin/git. A git child (alias, which gets the same env as a hook) has GIT_EXEC_PATH=C:/Program Files/Git/mingw64/libexec/git-core, PATH prefixed with /mingw64/libexec/git-core, and `type -P git` = /mingw64/libexec/git-core/git. So the digest, and every key built from it, differs between a plain bar and the hook's bar. In push mode the runner only looks up keys, so an entry earned by a developer or unattended bar outside a hook can never be hit. Spec 13's 'a push right after a green bar at the same sha and tip reuses the trio' cannot happen. The failure is a miss, which means more work, never a false green. Hence medium. | unsound | - |
| 12 | seams | tools/run-gates/run-gates.sh:3097 | medium | medium | confirmed | Confirmed. The reuse block (3097-3101) reads and increments `$REUSE_CACHE/age.${heldkeys[$i]}`. That is a per-leg-name file in the shared common-dir cache. The cache block (~4818) writes it back to 0 whenever the leg executes in any run, in any worktree, under any key, clean tree or dirty. The comparison it skips is the one that matters: an execution under key K2 never re-checks K1's entry. Alternating runs in another worktree or on a dirty tree therefore keep resetting the counter, and K1 can be reused past 10 consecutive reuses. Only the 25% sample then bounds it, geometrically and not at 10. Spec 13 itself specifies `age.<name key>` and 'reset to 0 by any execution', but its S7 promise that 'a wrong entry survives at most that long' does not follow from that mechanism. The code delivers neither the spec's guarantee nor the README's. Contained: it lengthens a stale entry's life, and the sample still catches it eventually. | sound | join-key-widened-by-a-shared-location |
| 13 | seams | tools/run-gates/run-gates.sh:4572 | low | low | confirmed | Confirmed. The sample loop (4562-4585) calls `runleg "$i" .sample` only when the leg's effective verdict was red. runleg (3326-3331) writes the durable log to `leg_log "${names[$i]}"`, which is named by leg name alone and ignores the suffix. So the sample run overwrites gate-logs/<leg>.log. report_one (3479, 3965) has already put that path into FAILED_LEGS as the `log:` pointer for the red attempt. On a `nondeterministic` outcome the pointer opens an `exit 0` log. The .retry path had the same overwrite at base, but the .sample path, where the second run is expected to differ, is new. Only the operator-facing log is affected; the verdict is not. | sound | - |
| 14 | seams | tools/run-gates/run-gates.sh:3100 | low | low | confirmed | Confirmed. `git grep` finds `.aged` only at the write, run-gates.sh:3100. There is no glob or read of it anywhere in tools/, whereas `.sampled` has its consumer at 4562. Write-only dead plumbing. The only record of an age-forced execution is the stderr note. No behavioural effect. | sound | - |
| 15 | verification | tools/gate-lint/fork-count.sh:168 | high | medium | confirmed | Confirmed. Every row in memory/project/fork-ceilings.txt is declared for 5.3. check_budgets skips every row whose version differs from the running bash's major.minor. With zero graded rows it ends on `[ "$red" = 0 ]`, so it exits 0, and the 'spawn budget (forks per hot entrypoint)' product leg in tools/gate-legs.json reports ok. remote-ci.yml runs the full bar on windows-latest under Git for Windows bash. Spec 8's F1 notes that this bash is 5.2. So CI grades nothing and reports green. Owner ruling F1(a) does allow the skipped shape for an undeclared version. Its stated rationale, though, is to keep 'the stale-ceiling red meaningful on each platform', and that presupposes rows for CI's bash. As shipped, the leg is in effect the rejected option (c), and it reports green. The read_budgets path already treats 'graded NOTHING' as a refusal, so the two zero-population cases disagree. Graded medium rather than high: this is a cost budget, not a correctness verdict, and node a's 5.3 pre-push bar does grade it. | unsound | - |
| 16 | verification | tools/run-gates/run-gates.test.sh:3074 | medium | medium | confirmed | In the runner, the worker writes `.defer` only after it has finished its own post-processing: the reap, leg_log, write_redacted and derive_foreign. run_tail_retry starts the retry only after the reader wakes on that worker's `.rc`. Unit 3's own acceptance ledger and the 9l comment measure this release at 10 to 14 s after the first attempt ends on node a. The direct check behind that ledger used a 20 s sleeper with a 3 s ceiling (AC1) and a 25 s sleeper (AC4). The canary arms cut these to 12 s (9k) and 15 s (9m) with a 2 s ceiling. So the tail retry starts at roughly 12 to 16 s, which is at or after the sleeper's end. In 9k the sleeper's `ls` at 12 s can also come before `.defer` is written. Either way `in-tail` reads `after-drain` and the peek reads 0. 9m's `.tail.leg` start versus the sleeper's end has the same race. This is the load-dependent ordering unit 15 set out to remove. | unsound | fixed-sleep-does-not-place-a-signal |
| 17 | verification | tools/run-gates/run-gates.test.sh:2930 | medium | medium | confirmed | 9d once checked that a ledger row reading `retried` is never reused. It now checks only that, with the cache deleted, an `ok` row runs. The cache writer (run-gates.sh around line 4813) keeps a retried green out of the cache only because it reads `$WORK/$i.rc`, the first attempt's result. Nothing asserts that. 9f's contended fixture checks the ledger row reads `retried`, but the ledger is no longer the reuse store. A grep of the evidence suite for retry and timeout finds only AC12's eight-field row check, with no arm on cache absence or non-reuse. The property is real and nothing tests it, but the current code is correct, so the effect is limited to a test gap. | unsound | - |
| 18 | verification | tools/run-gates/run-gates.evidence.test.sh:156 | medium | medium | confirmed | FLOOR_ASSERTIONS is still 151, last raised by unit 4, and its RAISED log has no unit-13 line. Commit ca969ce3a (unit 13) adds 73 ok/nope/skipped call lines to the evidence suite and removes 11. At about one executed assertion per ok/nope pair, that is roughly 30 or more new executed assertions. Units 1, 3 and 4 each raised the floor for their arms, and unit 13's records say nothing about the floor. With the floor lagging, an early exit that strands all of unit 13's reuse, sample, quarantine and push-mode arms still clears `n -ge FLOOR` (line 1979). | sound | - |
| 19 | verification | tools/run-gates/run-gates.sh:2813 | low | low | confirmed | build_input_keys (added by unit 4) has several silent `return 0` paths: the awk slice, mapfile, the key-file write, hash-object, and a count mismatch. Each leaves the remaining bulk legs' INPUT_KEYS unset, which read as '-'. REUSE_DIGEST (added by unit 1) falls back to an empty string on failure, which turns every key into '-'. Neither path prints anything, so under GATE_REUSE or GATE_REUSE_PUSH nothing is reused or cached, and the run looks like a cold cache. The failure is fail-safe and never a wrong verdict. The base's per-leg input_key had the same silent dash, but these failure paths are new in this diff. The only effect is lost diagnostics. | sound | degradation-known-but-unreported |
| 20 | intent | tools/gate-lint/fork-count.sh:168 | high | high | confirmed | In check_budgets, a row is skipped whenever `ver` differs from the running bash's major.minor. When every row is skipped, the summary reads `0 passed · 0 red · N skipped` and the function returns `[ "$red" = 0 ]`, which is 0, so the runner prints GATE ok. Every row in memory/project/fork-ceilings.txt declares 5.3. The unit 8 spec twice names CI's bash as 5.2, and remote-ci.yml runs the GATE_FULL bar under Git-Bash on windows-latest. So on CI this leg grades nothing and still reports green. The script contradicts its own rule: read_budgets refuses with exit 2 when a file declares no row, because that 'graded NOTHING — a refusal and not a pass', yet a file whose rows all name another version grades nothing and exits 0. Owner ruling F1 (a) does accept a skipped shape for an undeclared version, but its stated reason (keep the stale-ceiling red meaningful on each platform) assumes rows exist for each platform, and no 5.2 rows were added. Graded high rather than blocker: the leg is new, so no red previously caught can now land, and the local 5.3 bar still grades. | unsound | - |
| 21 | intent | tools/run-gates/run-gates.sh:2912 | medium | medium | confirmed | Confirmed. REUSE_DIGEST (run-gates.sh at f479ba4, around lines 2891-2912) hashes every exported GATE_*/GIT_*/PATH variable, except GATE_REUSE*, GATE_TURNSTILE_HELD, GATE_RUN_ID, GATE_BASE and GATE_PUSH_BASE. I checked on this host: a child of git (`git -c alias.envx='!env' envx`) sees GIT_EXEC_PATH='C:/Program Files/Git/mingw64/libexec/git-core' and a PATH starting with /mingw64/libexec/git-core. A direct shell has neither. pre-push:36 deliberately keeps GIT_EXEC_PATH and never restores PATH before `$gate` (line 1618). The mismatch is wider than the finding says: before the bar the hook also exports GATE_ATTRIBUTE, GATE_INHERITED_RED, GATE_INHERITED_RED_MAX_AGE (lines 1547-1549) and GATE_DOCS_BASE (lines 1507/1517). None of these is excluded and a direct bar does not set them. So every remote/history key from a direct or DoD bar misses at push time. The 'push right after a green bar' scenario in spec 13 (line 179) cannot fire, except for a retried push whose earning run was also a hook run. This fails safe (a miss, never a false hit), so medium: the owner-ruled saving is inert, and the AC12/AC13 arms prove it only by construction. | unsound | armed-but-unreachable-rule |
| 22 | intent | tools/run-gates/run-gates.sh:3112 | low | low | confirmed | Spec 13 lines 150 and 242 say a sampled leg's line says it was sampled. In the code, the draw (run-gates.sh:3111-3113) only writes `$WORK/$i.sampled` and leaves the leg to dispatch. report_one (line 3420 on) has no `.sampled` branch and prints the plain `GATE ok    <name>` / `GATE FAIL` line. A green sample is mentioned only in the stderr note at line 4569. Red samples get the named `nondeterministic`/`cache disagreement` lines. The spec and the build disagree, but verdicts are unaffected: low. | sound | - |
| 23 | intent | memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-14.md:295 | low | low | confirmed | Spec 14, as changed in this diff: S10 (lines 110-114) names checks 27, 29, 56, 69 and 88 and 'the other five checks' nine sites'. AC11 (line 295) still says 'the six checks'' and `die_env`. The shipped helper is `print_env_failure` (unattended.sh:779). It is called at nine sites across exactly those five checks: 27 x2, 29, 56 x3, 69, 88 x2. The Inventory note (line 217) allows the helper to be renamed through lexicon, which softens the name mismatch. The six/five count is still a real internal contradiction for whoever grades AC11. It affects only the spec text: low. | sound | two-answers-to-one-question |
