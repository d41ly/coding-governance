# TOOL-aSparedSpawn-12 — the held self-test tier, selected by the kit whose shipped bytes moved

**Status:** CLOSED · rev-3 · 2026-10-12 · node a · Tier-2 · base 22efab65 · streams tooling · order 3 · ratified 2026-10-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aSparedSpawn-12-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aSparedSpawn-12-acceptance-ledger.md) | journal | — |
| [2026-10-12-build-TOOL-aSparedSpawn-12-direct-checks.sh](../build/2026-10-12-build-TOOL-aSparedSpawn-12-direct-checks.sh) | journal | — |
| [2026-10-12-build-TOOL-aSparedSpawn-12-select-sim.out](../build/2026-10-12-build-TOOL-aSparedSpawn-12-select-sim.out) | journal | — |
| [2026-10-12-build-TOOL-aSparedSpawn-12-select-sim.py](../build/2026-10-12-build-TOOL-aSparedSpawn-12-select-sim.py) | journal | — |
| [2026-10-11-prompt-TOOL-aSparedSpawn-12-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aSparedSpawn-12-build-brief.md) | journal | — |
| [2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md](../reviews/2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md) | diff-review | TOOL-aSparedSpawn-1 TOOL-aSparedSpawn-2 TOOL-aSparedSpawn-3 TOOL-aSparedSpawn-4 TOOL-aSparedSpawn-5 TOOL-aSparedSpawn-6 TOOL-aSparedSpawn-7 TOOL-aSparedSpawn-8 TOOL-aSparedSpawn-9 TOOL-aSparedSpawn-10 TOOL-aSparedSpawn-11 TOOL-aSparedSpawn-13 TOOL-aSparedSpawn-14 TOOL-aSparedSpawn-15 |

<!-- /gen:spec-records -->

## 1. Goal

Give the held self-test tier a third mode between "held" and "everything": a held suite executes only
when its owning kit's shipped bytes, or the suite file itself, moved since the last recorded green
run of that suite. aMeteredSweep's round-two research replayed that rule over the last 30
first-parent commits on `main` and it ran 13% of the held tier's leg-seconds, and nothing at all on 23
of the 30 (`2026-10-09-build-TOOL-aMeteredSweep-1-research2-reuse.md` §4, rule A; PINNED, measured at
node `a` on 2026-10-09 over the profiled bar at fa68a767, ±2x). The mode serves developer and
Definition-of-Done runs; the owner ruled it stays off the push boundary (§8 F1).

## 2. Scope (IN)

- **S1** — `GATE_SELFTESTS` gains the value `changed`. Under it a held leg (`subject` kit or `chunk`
  selftests) executes when any selection condition in S2 holds, and is otherwise held with a line
  that names why: `GATE held  <name>  (self-test, unchanged since <sha8>)`. Every other non-empty
  value keeps today's meaning, run everything. Observed by AC1, AC2.
- **S2** — The selection conditions, any one of which executes the leg:
  - no last-run record for the leg, an unreadable one, or a recorded sha that is not an ancestor of
    `HEAD`;
  - a path in the leg's selection set (S3) differs between the recorded sha and the working tree,
    committed or not;
  - the manifest row's own bytes differ from the row hash in the record;
  - the recorded sha is more than the lag bound behind `HEAD` on the first-parent chain (S5).

  Observed by AC2, AC3, AC4.
- **S3** — A leg's selection set is its owning kit's shipped sources in the roles govkit's
  `EPOCH_ROLES` names, plus the suite file itself. The owner is the govkit entry whose `shipped`
  rows carry the suite file. A leg with no such entry, or a tree where govkit cannot be reached,
  selects by its `guard` plus the suite file, and the bar says so once per run, naming those legs.
  A leg's suite files are the words of its `argv` that carry a `/` and end `.sh`, `.py` or `.js`,
  the rule the foreign-load census already reads; every entry shipping one of them is an owner, and
  the set is their union. A fallback leg with no `guard` selects on any moved path, which is what an
  absent guard already means to the runner. Observed by AC2, AC6.
- **S4** — The last-run record. One small file per held leg under the git common dir, holding the
  `HEAD` sha and the manifest row hash, written tmp-then-rename. It is written only when the leg
  EXECUTED with verdict `ok` on a tree whose `TREE_CLEAN` reads `yes`; a red, a retried pass or a
  timeout clears it. A green on a dirty or moved tree neither writes nor clears, and a leg that did
  not execute (held, skipped, reused) leaves its record as it was. The row hash is the SHA-1 of the
  row's JSON with sorted keys and the file is named by the first 16 hex of the SHA-1 of the leg
  name, both computed by the legs-parse program as its tenth and eleventh fields, so they cost no
  spawn. Records are written under any non-empty `GATE_SELFTESTS`, so a `1` run seeds them.
  Observed by AC5.
- **S5** — The safety net: a recorded sha more than `GATE_SELFTESTS_MAX_LAG` first-parent commits
  behind `HEAD` executes the leg, so no `changed` run holds a suite on a record that old. It bounds
  staleness per run and promises no cadence, since no boundary runs the mode. Default 10 by owner
  ruling F2, the value of `GATE_FULL_MAX_LAG` in `.githooks/pre-push`. Observed by AC4.
- **S6** — `govkit.py shipped --epoch` prints only the rows whose role is in `EPOCH_ROLES`, from the
  same derivation `derive_epoch_state` reads, so "this kit moved" has one answer for the version-bump
  rule and for selection. Observed by AC8.
- **S7** — The stamp, and NO boundary change (owner ruling F1 (b)). `gate-full-green` writes
  `selftests changed` for such a run, never `1`, so a partial tier is never recorded as the whole one.
  `.githooks/pre-push` and `.githooks/gate-env.sh` are not edited: predicate 8 of
  `check_green_record` (`.githooks/pre-push:1237-1246`) already forces whenever the push runs the
  self-tests and the record's field is not `1`, and a push with them held, the 2026-08-27 default,
  accepts the record as it accepts a held one today. A `.githooks/pre-push.test.sh` arm pins both
  directions. Observed by AC7.
- **S8** — The figure. The selection instrument the research ran (`select_sim.py`) is committed
  beside this unit's record and replayed after the build, so the 13% is re-derived from the rule as
  built. A records-only Python file is graded by the lexicon leg, so its function names are taken
  from the declared verb table before it is committed. Observed by AC9.

## 3. Non-goals (OUT)

- Turning `changed` mode on at any boundary, by owner ruling F1 (b). Nothing exports it at pre-push,
  `.githooks/gate-env.sh` keeps its on-demand header and values, `.githooks/pre-push` keeps every
  predicate, and the 2026-08-27 on-demand ruling stands.
- The unattended kit's suites. They run through `run-unattended-gates.sh --selftests`, not through
  `tools/gate-legs.json`, and need the same rule applied there separately. Named follow-up.
- Narrowing the broad `{prefix}/` guards with traced reads (the research's U5). The guard fallback in
  S3 is as wide as those guards are today.
- Any reuse of a verdict. A held leg that is selected executes; one that is not selected is HELD,
  never reported as passed. Content-addressed reuse is `TOOL-aSparedSpawn-13`.
- An explicit owner field on manifest rows for the suites no kit ships. They fall back to their guard.

### Edges

- **consumes-from** external — govkit's per-kit shipped set (`govkit.py shipped` and its
  `EPOCH_ROLES`); without it every held leg degrades to its guard, which S3 announces.

## 4. Design

The held-tier branch in `tools/run-gates/run-gates.sh` (the `subjects`/`chunks` test that writes
`ondemand`) gains a `changed` arm. It runs once per bar, before dispatch:

1. Read every held leg's last-run record from `<git-common-dir>/gate-selftest-last/`. A missing,
   unreadable, non-ancestor or row-hash-mismatched record decides "execute" without a diff.
2. Group the remaining legs by recorded sha and run ONE `git merge-base --is-ancestor <sha> HEAD`,
   one `rev-list --count --first-parent <sha>..HEAD` for the lag and, only when both pass, one
   `git diff --name-only --no-renames <sha>` (working tree included) per distinct sha. After a full
   run every record shares one sha, so the common case is three spawns. The ancestry call is the
   third: no count or diff reads "not an ancestor", and a non-ancestor must execute.
3. Resolve the selection sets from `govkit.py shipped --epoch` and `govkit.py shipped`, one call each
   per bar, and join the changed paths against them.
4. A leg selected executes as a normal leg, and the bar prints `run-gates: selftests changed:
   <name> runs (<reason>)` for it before dispatch; that is the line AC4 reads the lag on. A leg not
   selected writes the held rc with its reason.

The run header gains a `selftests` key carrying the stamp value, and the run-log line's `selftests`
field reads the same value, so no record of a `changed` run says `1`.

Who sets the mode: a developer, or a Definition-of-Done run, in its own environment. No boundary does,
and the push boundary reads a `changed` record through the predicate it already has, so this unit
moves no line of `.githooks/`. The stamp writer at `tools/run-gates/run-gates.sh:3893` and `:3935`
prints `${GATE_SELFTESTS:+1}` today, which would record a `changed` run as `1`; both become the
mode's own value for `changed` and keep `1` for every other non-empty value.

The record directory is per git COMMON dir, as `gate-full-green.shared` and the turnstile already are,
so every worktree on a node shares it and a `changed` run in the primary sees a branch worktree's run.

Why "since the last recorded run" and not "since `BASE`": a record moves only when the suite went
green on a clean tree, so a red suite keeps executing until it is fixed, and a branch whose `BASE`
predates a kit move still runs that kit's suite once rather than on every bar.

govkit is a sibling kit, and the runner is an ENGINE, which the hooks kit README says is not
rendered and reaches a sibling through `resolve_kit_dir` (§12 of the charter), never by literal. So
the selection is ONE inline Python program, opened by the `RKD_PROGRAM` copy the runner already
carries, that resolves `resolve_kit_dir("govkit", "govkit.py", <kit dir>)`, runs `govkit.py
shipped` and `shipped --epoch` as two subprocesses and asks git the step 2 questions; a refusal or
a nonzero exit from either is "cannot be reached". It prints one decision per held leg, which the
guard pass and the report read, so the decision is made once. A leg it names nothing for executes.

### Inventory

- The `changed` value of `GATE_SELFTESTS`; the knob `GATE_SELFTESTS_MAX_LAG`; the record directory
  `gate-selftest-last` under the git common dir; the flag `--epoch` on govkit's `shipped` verb; the
  stamp value `selftests changed`. New function names are taken from `lexicon.py --suggest` at build.

### Migration

- None for data. An older runner reads `changed` as non-empty and runs everything, the safe
  direction. The run-gates, govkit and push-main kits each owe a version bump in every carrier
  (`govkit selfcheck` names them).

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.test.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `.githooks/pre-push.test.sh` — the pin on predicate 8 only; `.githooks/pre-push` is not edited
- the selection instrument, committed under this build's own build folder (S8) as
  `2026-10-12-build-TOOL-aSparedSpawn-12-select-sim.py` with its output beside it, and the pass's
  direct checks as `2026-10-12-build-TOOL-aSparedSpawn-12-direct-checks.sh`

### Alternatives rejected

- **Select by `BASE` diff.** The research's own rule. It re-runs a kit's suite on every bar of a
  branch that moved that kit, and it runs nothing for a suite that was red at `BASE` and still is.
- **Rule B, the wide set (guard, kit directories, `tools/lib/`, the manifest).** 23% of held
  leg-seconds and zero-run on 1 of 30 commits in the same replay, almost all of it from `{prefix}/`
  guards that fire on any `tools/` change.
- **Store the records in `TOOL-aSparedSpawn-13`'s cache.** It would make this unit wait on that one,
  and a selection record is not a verdict to reuse.
- **A row-keyed single file for all records.** Two worktrees' bars finishing together lose a row; one
  file per leg makes every write atomic, and a lost write only means one extra execution.

## 5. Production-readiness checklist

- security: no new trust surface; a forged record can only HOLD a suite, so records are written by the runner alone and a reader refuses a malformed one by executing.
- perf / scale: three `git` spawns per distinct recorded sha, one Python program and the two `govkit.py` calls it makes per bar, only in `changed` mode; nothing in the default mode.
- error / empty / loading states: no record, a bad record, an absent govkit and a non-ancestor sha all execute the leg; each held line names its reason.
- observability: every held leg prints its reason and recorded sha; the run header records the mode; the guard fallback prints the legs it applied to.
- risks: an under-declared selection set holds a suite that should have run; S5's lag bound caps how long, and a full run that reds an unselected suite is a declaration miss to file.
- testing: canary arms in the run-gates suite on a fixture with a stub govkit; a govkit selftest arm for `--epoch`; a pre-push arm pinning how the unchanged predicate reads a `changed` record.
- migration: none; the version bumps under §4 Migration.
- user docs: `tools/run-gates/README.md` documents the mode as a developer and Definition-of-Done tool, the record and the lag bound; the charter's merge-bar paragraph is unchanged (F1 (b)).

## 6. Acceptance criteria

- **AC1** — When a fixture bar runs with `GATE_SELFTESTS` set to `changed` after a recorded green and
  only kit X's engine source moved, the leg X owns executes and kit Y's leg prints
  `GATE held` with `unchanged since`. Red when: Y's leg executes, or X's leg is held.
  fixture: a scratch repo with a stub govkit printing two entries' `shipped` rows.
- **AC2** — When only a held suite's own file moves, or only an unowned leg's `guard` path moves, that
  leg executes and the bar prints the guard-fallback line naming the unowned leg. Red when: either
  leg is held, or the fallback line is absent.
- **AC3** — When a leg's record is deleted, holds a sha that is not an ancestor of `HEAD`, or carries
  a row hash the manifest row no longer has, the leg executes. Red when: any of the three is held.
- **AC4** — When a record sits more than `GATE_SELFTESTS_MAX_LAG` first-parent commits behind `HEAD`
  with no selection path moved, the leg executes and its line names the lag. Red when: it is held.
- **AC5** — When a selected leg goes red, and separately when a green run starts on a tree whose
  `TREE_CLEAN` is `no`, no record is written and a prior one for a red leg is gone. Red when: a record
  exists for the red leg, or the dirty-tree run wrote one.
- **AC6** — When govkit cannot be reached from the runner, every held leg selects by its `guard` and
  the bar says so once. Red when: a leg is held with no diff evidence, or the bar is silent about it.
- **AC7** — When a `changed` run's `gate-full-green` is read by the unedited `check_green_record`, the
  record says `selftests changed`; a push with the self-test switch on forces, and one with it held
  accepts. `git diff --stat` over `.githooks/` shows only the test file. Red when: the stamp reads `1`,
  the switch-on push is accepted, or a line of `.githooks/pre-push` or `.githooks/gate-env.sh` moved.
- **AC8** — When `python tools/govkit/govkit.py shipped --epoch` runs on this tree, every printed role
  is one of `EPOCH_ROLES`, and its rows are exactly the `shipped` rows in those roles. Red when: a
  `project-owned` or `generated` row is printed, or an epoch-role row is missing.
- **AC9** — When the committed selection instrument replays the built rule over the last 30
  first-parent commits on `main`, it prints the share of held leg-seconds selected and the count of
  commits selecting nothing. Red when: the share exceeds the 23% of rule B, meaning the set as built
  is the wide one. figure: DERIVED at observation; the research's 13% and 23 of 30 are the PINNED
  expectation, measured 2026-10-09 on node `a`, ±2x. cost: seconds, one `git diff` per commit.

## 7. Gates

`branch-guard self-test` · `check-wiring self-test` · `dead-path carriers self-test` ·
`foreign-prefix parity (every self-test at three prefixes)` · `govkit acceptance matrix` ·
`govkit refusal join` · `govkit selftest` · `install-prefix self-test` ·
`kit-placeholders self-test` · `lexicon naming predicates` · `pre-push bar self-test` ·
`pre-push run-log line` · `pre-push self-test` · `profile-bar selftest` · `push-main self-test` ·
`python resolver (behaviour + inline parity + idiom ban)` · `recall floor arms` ·
`run-gates adopter e2e` · `run-gates canary` · `run-gates evidence` · `run-gates gov canary` ·
`run-gates run-log line` · `run-gates turnstile` · `settings-merge selftest` ·
`spec-tokens self-test` · `straggler-guard arms` · `transition-audit arms` · `govkit selfcheck` ·
`kit epoch (shipped bytes move, the version moves)` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · a selection that ignores the moved path, then a record left behind by a red leg · none
New arm: tools/govkit/selftest.py · covers AC8 · `--epoch` printing a project-owned row · none
New arm: .githooks/pre-push.test.sh · covers AC7 · a `changed` record accepted for a switch-on push, and a stamp writing `1` for a `changed` run · none

## 8. Open questions

- **F1 — May `changed` mode go back on the push boundary?** The owner ruled on 2026-08-27 that
  self-tests run on demand only, at every boundary (`.githooks/gate-env.sh` header).
  - (a) Yes, selected-only: `gate-env.sh` exports `GATE_SELFTESTS` as `changed`, so a push that moved
    a kit runs that kit's suites and a records-only push runs none. Reverses the 2026-08-27 ruling.
  - (b) No: the mode exists for developer and Definition-of-Done runs only; the ruling stands.
  - Recommendation: (a). The ruling's stated reason was cost on pushes that touch no kit source, and
    under this rule those pushes run no suite.
  - RESOLVED (owner, 2026-10-10): (b) no; `changed` mode serves developer and Definition-of-Done runs, and the 2026-08-27 ruling stands.
- **F2 — The "run everything every N" safety net: which N?**
  - (a) N=10, the same number as `GATE_FULL_MAX_LAG`, so the two lag bounds speak one value.
  - (b) A smaller N, more coverage of declaration misses at more cost.
  - (c) No age bound; rely on whoever runs the whole tier by hand.
  - Recommendation: (a), N=10.
  - RESOLVED (owner, 2026-10-10): (a) N=10.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-10 · §1 §2 §3 §4 §5 §6 §7 S5 S7 AC7 · folded the owner's F1 ruling (b): no push-boundary
  use, so S7 no longer edits `check_green_record` and moves no line of `.githooks/`; the stamp writes
  `selftests changed` and the unedited predicate 8 is pinned in both directions; F2's N=10 is kept.
- rev-3 · 2026-10-12 · §2 §4 §5 S3 S4 S8 AC4 · the build read the code before writing it: the
  ancestry question is a third git spawn per distinct sha, since neither the count nor the diff can
  say "not an ancestor"; govkit is reached by `resolve_kit_dir` inside one inline selection program,
  which settles the rev-2 UNVERIFIED line (an engine is not rendered); a leg's suite files, its
  owners and the unguarded fallback are stated; the record's row hash, file name, and the cases
  that neither write nor clear it are stated; the lag is named on a per-selected-leg line before
  dispatch; the run header and run-log line carry the stamp value; the instrument file names are
  pinned.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "select held self-test legs by which kit shipped bytes moved"`
ranks the run-gates affordance seam `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` and no selection helper;
the unit extends govkit's `cmd_shipped` and the `EPOCH_ROLES` set `derive_epoch_state` already reads
(`tools/govkit/govkit.py`), and the existing held-tier branch in `tools/run-gates/run-gates.sh`,
rather than deriving "this kit moved" a second time. Prior records: TOOL-dUnstalledConvoy-26 and
TOOL-dUnstalledConvoy-27 (the held tier and the `selftests` coverage relation), TOOL-dUnstuckLanding-24.

Recall terms used: GATE_SELFTESTS held self-tests on demand push boundary owner ruling kit subject
selftests chunk gate-env pre-push epoch shipped
