# TOOL-aSparedSpawn-16 — the closing review's bar reds and push-soundness fixes

**Status:** OPEN · rev-1 · 2026-10-12 · node a · Tier-2 · base f479ba42 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make the build's own HEAD bar green and close the review's push-soundness holes before the close
lands. The round-1 closing review
(`memory/builds/aSparedSpawn/reviews/2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md`)
found two drifted registries and two stale fork ceilings that red the default bar at f479ba42, six
unarmed exit sites the harness arms leg reds on, a reuse path that keeps a stale `ok` after an
executed red, a push bar that inherits two reuse knobs, a spawn-budget selector that passes on a
typo, an A/B instrument that certifies runs which executed nothing, and an evidence floor that lags
unit 13's arms. This unit fixes each, one scope item per finding.

## 2. Scope (IN)

Every site was re-read at f479ba42; line numbers are that tree's. Each item names the review
finding id it closes.

- **S1** — Finding 9. `tools/govkit/subject-pins.tsv` carries no row for the `held-halves selftest`
  leg that unit 5 added to `tools/gate-legs.json`, so `govkit selfcheck` reds. The row comes from
  `python tools/govkit/govkit.py selfcheck --write`, committed as written; the file is generated and
  is never hand-edited. Observed by AC1.
- **S2** — Finding 10. `memory/project/spawn-idiom-sites.txt` has drifted from its population: the
  leg's argv reports seven findings at f479ba42. They are `cat-file` in `run-gates.sh` (15 declared,
  16 measured), `run-gates.test.sh` (23, 24), `run-gates.evidence.test.sh` (11, 14) and
  `.githooks/pre-push.test.sh` (8, 12); `printf-subst` (2, 3) and `var-pipe` (136, 141) in
  `run-gates.test.sh`; and `var-pipe` in `tools/unattended/check-unattended.sh` (26 declared, 25
  measured). Each forking site this build added in its own files is rewritten first: a `$(cat f)`
  becomes `$(<f)` or a `read`, and a `printf … | grep -c` becomes a builtin test where one reads the
  same answer. Every row is then re-measured and set to exactly what the scan reports, the
  `check-unattended.sh` row lowered to its measured 25. This item lands LAST in the pass, after S4 to
  S6 add their arms, so the registry is measured over the final bytes. Observed by AC2.
- **S3** — `memory/project/fork-ceilings.txt` rows `run-gates-1leg` and `run-gates-2leg` declare
  ceilings 72 and 74 against measured counts of 51 and 53, which the `spawn budget (forks per hot
  entrypoint)` leg reds as STALE (the file's tolerance is max(3, 5 %) above the count). The one-leg
  row falls to its measured count. The two-leg row falls to its measured count plus two, because its
  reason already records a polled reading that varied, and the reason gains that margin and the date
  measured. Both are re-measured after S5, which adds code to the runner's post-pool path. Observed
  by AC3.
- **S4** — `python tools/memory-tree/check-arms.py --check` reds on six unarmed exit sites in
  `tools/run-gates/run-gates.sh` that units 1, 2 and 4 added. Each is armed or pinned:
  - `:1270` (no spawn command resolves) and `:1273` (a rate could not be measured) are reasoned
    sites. Each gains an arm in `tools/run-gates/run-gates.test.sh` beside arm 12a, asserting its
    whole failure text from the calibrate verb run without the rates seam: a blank
    `GATE_SPAWN_CMD` for the first, and `false` as the spawn command for the second.
  - `:1236`, the `|| exit 1` inside `measure_spawn_rate`'s timed subshell, is delegated: its only
    effect is the `:1273` refusal. It gains a `# arm-signature:` marker naming that refusal's text,
    which the `:1273` arm then arms.
  - `:2896` (`git version … || exit 1`) and `:2909` (`[ "${#evs[@]}" -gt 0 ] || exit 1`) exit the
    `REUSE_DIGEST` capture, which prints nothing and leaves the digest empty, so no text exists to
    assert. Each is pinned with a five-field row in `memory/project/unarmed-branches.txt` whose
    reason says so; the silent empty digest is review finding 19, a non-goal here.
  - `:5088`, the bare `exit 1` closing a red run, gains a `# arm-signature:` marker naming the
    `gates RED` summary text an existing canary arm already asserts, or a pin row with a reason if
    no arm asserts a 12-character span of it.

  The canary's `FLOOR_ASSERTIONS` rises by the assertions added, with a `RAISED` line. Observed by
  AC4.
- **S5** — Finding 3, HIGH. In `tools/run-gates/run-gates.sh`'s reuse path, a leg that executes
  while its key holds a cached `ok`, and whose effective result is red, must erase that entry and
  quarantine the leg, as the sampled-disagreement branch at `:4562` does. Today only `*.sampled`
  legs reach that branch, so an age-forced execution (`:3097`-`:3102`) or any other execution under
  a cached key that reds leaves the stale `ok` in place, and the cache block at `:4819` resets the
  age counter to 0. The branch's population widens to every executed leg whose effective rc is
  non-zero and whose key holds an `ok` entry. A sampled leg keeps its classifying re-run and its two
  lines. A leg that was not sampled takes the effective rc as its verdict, which is already its serial
  retry's where it had one, prints `cache disagreement · <leg> · <key>`, loses the entry and is
  quarantined against its row hash. The `$WORK/$i.aged` marker is removed, since the widened branch
  covers the case it was written for and nothing reads it; the age bound's stderr note stays.
  `tools/run-gates/README.md`'s reuse section says an executed red against a cached `ok` erases and
  quarantines whatever drew the execution. Observed by AC5 and AC9.
  - **Readers:** by name: `tools/run-gates/run-gates.sh` writes `.aged` at `:3100`, and no other
    tracked file spells it. by value: NO VALUE READERS — the review's finding 14 confirmed by
    `git grep` that no glob or read of the marker exists, so nothing compares or derives from it.
- **S6** — Finding 1. `.githooks/pre-push` clears `GATE_REUSE_SAMPLE` and `GATE_REUSE_DAY` beside
  `GATE_REUSE_PUSH` (`:1456`-`:1457`), for every bar a STUB included, and appends each to
  `ENV_CLEARED` when it was set, so the `not honoured from the environment by this bar:` line names
  it. The runner keeps reading both, since they are its own suite's seams. An arm in
  `.githooks/pre-push.test.sh` beside the AC15 arm exports `GATE_REUSE_SAMPLE=0` and
  `GATE_REUSE_DAY=1` into a push and asserts the line names each. Observed by AC6.
- **S7** — Finding 4. `tools/gate-lint/fork-count.sh` refuses with exit 2 an `--only` id that names
  no declared row, printing the declared ids, after `read_budgets` and before any row is traced.
  Today `--only no-such-id` prints `0 passed · 0 red · 0 skipped` and exits 0. A `--selftest` arm
  stages that typo against a one-row file and expects the refusal; the selftest's PASS line counts
  three assertions. Observed by AC7.
- **S8** — Finding 6, HIGH.
  `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` sets
  `GATE_SELFTESTS=1` in each arm's environment, so its held legs execute. The positive artifact
  counts only executed verdict lines, `^GATE (ok|FAIL) `, which leaves out `held`, `skip`, `reuse`
  and the `retry` interim, and requires exactly one per manifest leg. An arm whose bar exits non-zero
  records `artifact` as `no` and is never picked as a best wall. Observed by AC8.
- **S9** — Finding 18. `FLOOR_ASSERTIONS` in `tools/run-gates/run-gates.evidence.test.sh` (151 at
  `:156`) rises by the executed assertions unit 13 and this unit's S5 arms add, counted one per
  `ok … || nope` pair as units 1, 3 and 4 counted theirs, with a
  `RAISED 151 -> <new> by TOOL-aSparedSpawn-13 and -16` line. The acceptance ledger marks the
  executed count OWED until the suite runs at VERIFYING. Observed by AC10.

## 3. Non-goals (OUT)

- The review's M3 (findings 11 and 21, push-time reuse missing an entry earned outside a hook), M5
  (finding 12, the age counter keyed by leg name), M6 (finding 16, arms 9k and 9m placing a signal
  with a fixed sleep) and M7 (finding 17, no arm guarding a retried green out of the cache).
- Every LOW item: L1 to L6, findings 7, 8, 13, 14, 19, 22 and 23. S5 removes the `.aged` write that
  finding 14 names, as a side effect of widening the disagreement branch; it adds no `(aged)` tail.
- H3's all-skipped case (finding 20, and finding 15 under M1): a run grading zero rows because every
  row names another bash. It needs bash 5.2 rows measured on CI's Git Bash, which this node cannot
  produce. S7 changes the `--only` typo alone.
- Each non-goal above is carried to the build's exit as an ask.
- Re-running the width A/B. S8 fixes the instrument; the owner runs it before any width knob moves.
- A kit version bump. The main loop bumps every kit this unit touches once, after it.
- Running any suite or the bar inside the build pass. The suites and the bar run once, at VERIFYING.

### Edges

none

## 4. Design

Nine fixes, each where the review located its defect. Three are registry repairs measured from the
tree (S1, S2, S3), and S2 and S3 are measured last because S4 to S6 move the bytes they count. Two
are arms and marks for a meta-gate (S4, S9). Three are behaviour fixes with an arm each (S5, S6,
S7), and one is a record instrument (S8).

### The disagreement branch, widened (S5)

The loop after `run_leg_retry` iterates `"$WORK"/*.sampled` today. It becomes one pass over every
leg index whose `$WORK/$i.rc` names an execution, skipping `reuse`, `ondemand`, `skip` and
`docskip` as the cache block does. For each, the effective rc is `$WORK/$i.retry.rc` where it exists,
else `$WORK/$i.rc`. A leg with a `.sampled` marker runs the existing branch unchanged. Any other leg
whose effective rc is non-zero, whose `INPUT_KEYS[$i]` is a measured key, and whose cache entry under
that key reads `ok` runs the branch's red-again arm: the `cache disagreement` line, the entry erased,
the quarantine file written. No extra run is spent on it, because its retry already gave a second
observation where one was due. The loop spawns nothing per leg: every read is a builtin `read`, so
the one-leg and two-leg fork counts S3 measures do not move.

### Inventory

No new function, variable family or file kind is minted. S5 removes the `.aged` marker file kind.
S4 adds two `# arm-signature:` comments and two pin rows. New arms reuse the helpers their suites
already define (`run_sp_verb` and `check_sp_value` in the canary, `ru_repo` and `ru_run` in the
evidence suite, `run_rp_push` in the pre-push suite), so the lexicon leg and the map's
`symbols.json` see no new definition.

### Files touched (estimate)

- `tools/govkit/subject-pins.tsv`
- `memory/project/spawn-idiom-sites.txt`
- `memory/project/fork-ceilings.txt`
- `memory/project/unarmed-branches.txt`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/README.md`
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/gate-lint/fork-count.sh`
- `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh`

### Alternatives rejected

- **Raise the spawn-idiom rows to their measured counts without removing any site.** The registry
  is shrink-only by design, and the sites this build added are its own to drain.
- **Read `.aged` in the existing loop and leave other executions alone.** A plain bar or a push-mode
  bar can execute a leg whose key holds an `ok` too, so an age-only reader leaves the same stale
  entry in place on those paths.
- **Re-run every non-sampled red once more to classify it.** The serial retry already re-ran a red
  leg, and a second classifying run doubles a red bar's tail for a label.
- **Exit 2 when every row is skipped, in this unit.** Without bash 5.2 rows every CI bar would then
  red; the review's own reconciliation orders the rows first.
- **Arm the two `REUSE_DIGEST` exits by making them print.** That is finding 19's fix, which needs a
  line on stderr and an arm of its own; pinning them now keeps this unit to the reds.

## 5. Production-readiness checklist

- security: S5 and S6 close two paths by which a push could land green on a leg that just went red, or on knobs the environment chose; no new input or write path.
- perf / scale: S5 adds one builtin pass over the leg indices after the pool drains and no spawn; S2 removes forks; S3 records savings already made.
- error / empty / loading states: S7's refusal names the declared ids; S5's erase and quarantine print the existing named line; S8's arm records `no` on a non-zero bar exit rather than a figure.
- observability: S5 reuses the `cache disagreement` line, so a reader counting disagreements sees the new population without a new verb; S6's cleared knobs ride the existing not-honoured line.
- risks: S5 quarantines a leg that reds once on a plain bar under a cached `ok`, until its manifest row changes, the same cost the sampled branch already pays for a flaky leg.
- testing: an evidence arm for S5's aged and plain-bar cases, a pre-push arm for S6, a selftest arm for S7, canary arms for S4, each observed red on a staged break first.
- migration: none for data; an existing stale `ok` is erased the first time its leg executes red.
- user docs: `tools/run-gates/README.md`'s reuse section states the widened erase and quarantine rule.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs after S1, it exits 0 and prints no
  line naming `held-halves selftest`. Red when: the pin file still lacks the row, which is f479ba42's
  state.
- **AC2** — When the shell-hygiene leg's argv,
  `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`,
  runs after every other scope item has landed, it exits 0 with no finding. Red when: any registry
  row differs from the scan, in either direction.
  figure: DERIVED, the scan's own count at observation time.
- **AC3** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-1leg`
  runs, and again with `--only run-gates-2leg`, each prints `fork-count: ok` for its row. Red when:
  either prints `STALE` or `RED`.
  figure: the counts 51 and 53 are PINNED, measured 2026-10-12 at f479ba42 on node a under bash
  5.3.9; the verdict is DERIVED at observation.
- **AC4** — When `python tools/memory-tree/check-arms.py --check` runs, it exits 0 and prints no
  `HYGIENE check-arms: tools/run-gates/run-gates.sh` line. Red when: one of the six sites stays
  unarmed and unpinned, or an arm asserts a shorter text than the site's signature.
  permission: the canary arms themselves execute at VERIFYING; this criterion reads their text.
- **AC5** — When a scratch repository's one-leg bar earns an `ok`, its `age.*` counter is set to 10,
  and the runner runs again with `GATE_REUSE=1` and `GATE_REUSE_SAMPLE=0` while the leg exits 1,
  the run prints `cache disagreement` naming the leg, the entry under its key is gone, and a
  quarantine file exists. Red when: the entry survives the aged red, which is f479ba42's behaviour.
  fixture: the evidence suite's `ru_repo` shape, built in a scratch directory.
- **AC6** — When a scratch clone with `.githooks/pre-push` installed pushes to a local bare remote
  with `GATE_REUSE_SAMPLE=0` and `GATE_REUSE_DAY=1` exported and `GOV_GATE_CMD` naming a stub, the
  hook's `not honoured from the environment by this bar:` line names both. Red when: either name is
  absent from the line, or the stub sees either knob set.
- **AC7** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only no-such-id`
  runs, it exits 2 and lists every declared id; `bash tools/gate-lint/fork-count.sh --selftest`
  prints `PASS (3 assertions)`. Red when: the typo exits 0, which is f479ba42's behaviour.
- **AC8** — When `2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` runs with `AB_LOAD=0` on a frozen
  clone of the tree and a one-leg manifest whose leg sits in the `selftests` chunk, every row's
  `artifact` reads `yes` for a leg exiting 0 and `no` for a leg exiting 1. Red when: the exit-1 leg
  reads `yes`, which it does at f479ba42 because the `GATE held` lines are counted.
  cost: six one-leg bars and one calibration, about two minutes on node a.
- **AC9** — When the scratch repository of AC5 runs a plain bar, with no `GATE_REUSE`, while its leg
  exits 1 and its key holds an `ok`, the entry is erased and the leg quarantined, and the next
  `GATE_REUSE=1` run prints `GATE ok` for it rather than `GATE reuse`. Red when: a plain bar's red
  leaves the entry, or the next reuse run reuses the leg.
- **AC10** — When `grep -n 'RAISED 151 -> ' tools/run-gates/run-gates.evidence.test.sh` runs, it
  prints one line naming `TOOL-aSparedSpawn-13` and `-16`, and `FLOOR_ASSERTIONS` is that line's new
  value. Red when: the floor is still 151, which is f479ba42's state.
  permission: whether the floor sits at or below the executed count is observed when the suite runs
  at VERIFYING, and the ledger marks it OWED until then.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` ·
`shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` ·
`shell-hygiene selftest` · `harness arms (fail branches armed or pinned)` · `run-gates evidence` ·
`run-gates canary` · `run-gates gov canary` · `run-gates turnstile` · `run-gates run-log line` ·
`run-gates adopter e2e` · `profile-bar selftest` · `pre-push self-test` · `pre-push bar self-test` ·
`pre-push run-log line` · `push-main self-test` · `branch-guard self-test` ·
`python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` ·
`transition-audit arms` · `straggler-guard arms` · `recall floor arms` · `recall floor` ·
`memory hygiene` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC5 AC9 · an aged leg and a plain bar's leg each exiting 1 against a cached ok · FLOOR_ASSERTIONS, by S9
New arm: tools/run-gates/run-gates.test.sh · covers AC4 · the calibrate verb with a blank spawn command and with a spawn that fails · FLOOR_ASSERTIONS, by the arms added
New arm: .githooks/pre-push.test.sh · covers AC6 · the two reuse knobs exported into a push · none
New arm: tools/gate-lint/fork-count.sh · covers AC7 · an `--only` id naming no declared row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "quarantine a leg whose cached ok disagrees with an executed red"`
ranks generic `ok` and `leg` helpers and no reuse seam; no new seam is built. Each fix extends the
existing branch that already owns its case: S5 widens the sampled-disagreement quarantine path after
`run_leg_retry` in `tools/run-gates/run-gates.sh` (TOOL-aSparedSpawn-13 S6) rather than adding a
second erase; S6 extends the hook's `ENV_CLEARED` scrub that already clears `GATE_REUSE_PUSH` and
`GATE_DOCS_BASE`; S7 adds its refusal beside `check_budgets` and `read_budgets` in
`tools/gate-lint/fork-count.sh`, whose empty-file refusal is the same shape; S1 uses govkit's own
`selfcheck --write` generator.

Recall terms used: cache disagreement quarantine sampled age bound GATE_REUSE_PUSH ENV_CLEARED
not honoured check_budgets fork ceilings spawn idiom registry subject pins FLOOR_ASSERTIONS
