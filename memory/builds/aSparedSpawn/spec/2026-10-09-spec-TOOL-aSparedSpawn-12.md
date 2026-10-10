# TOOL-aSparedSpawn-12 — the held self-test tier, selected by the kit whose shipped bytes moved

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Give the held self-test tier a third mode between "held" and "everything": a held suite executes only
when its owning kit's shipped bytes, or the suite file itself, moved since the last recorded green
run of that suite. aMeteredSweep's round-two research replayed that rule over the last 30
first-parent commits on `main` and it ran 13% of the held tier's leg-seconds, and nothing at all on 23
of the 30 (`2026-10-09-build-TOOL-aMeteredSweep-1-research2-reuse.md` §4, rule A; PINNED, measured at
node `a` on 2026-10-09 over the profiled bar at fa68a767, ±2x). That is cheap enough to ask whether the
tier belongs back on the push boundary, which is the owner's question in §8.

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
  Observed by AC2, AC6.
- **S4** — The last-run record. One small file per held leg under the git common dir, holding the
  `HEAD` sha and the manifest row hash, written tmp-then-rename. It is written only when the leg
  EXECUTED with verdict `ok` on a tree whose `TREE_CLEAN` reads `yes`; a red, a retried pass or a
  timeout clears it. Observed by AC5.
- **S5** — The safety net: a recorded sha more than `GATE_SELFTESTS_MAX_LAG` first-parent commits
  behind `HEAD` executes the leg, so every held suite runs at least once per that many landings.
  Default 10, the value of `GATE_FULL_MAX_LAG` in `.githooks/pre-push`. Observed by AC4.
- **S6** — `govkit.py shipped --epoch` prints only the rows whose role is in `EPOCH_ROLES`, from the
  same derivation `derive_epoch_state` reads, so "this kit moved" has one answer for the version-bump
  rule and for selection. Observed by AC8.
- **S7** — The stamp and the boundary. `gate-full-green` writes `selftests changed` for such a run.
  `check_green_record` in `.githooks/pre-push` treats a `changed` record as covering a push that runs
  in `changed` mode, and never as covering one that runs every self-test. Observed by AC7.
- **S8** — The figure. The selection instrument the research ran (`select_sim.py`) is committed
  beside this unit's record and replayed after the build, so the 13% is re-derived from the rule as
  built. A records-only Python file is graded by the lexicon leg, so its function names are taken
  from the declared verb table before it is committed. Observed by AC9.

## 3. Non-goals (OUT)

- Turning `changed` mode ON at any boundary. Whether `.githooks/gate-env.sh` sets it is F1, and this
  unit builds the mode whatever F1 says.
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
2. Group the remaining legs by recorded sha and run ONE `git diff --name-only <sha>` per distinct
   sha (working tree included), plus one `rev-list --count --first-parent <sha>..HEAD` per distinct
   sha for the lag. After a full run every record shares one sha, so the common case is two spawns.
3. Resolve the selection sets from `govkit.py shipped --epoch` and `govkit.py shipped`, one call each
   per bar, and join the changed paths against them.
4. A leg selected executes as a normal leg. A leg not selected writes the held rc with its reason.

The record directory is per git COMMON dir, as `gate-full-green.shared` and the turnstile already are,
so every worktree on a node shares it and the primary's push sees a branch worktree's run.

Why "since the last recorded run" and not "since `BASE`": a record moves only when the suite went
green on a clean tree, so a red suite keeps executing until it is fixed, and a branch whose `BASE`
predates a kit move still runs that kit's suite once rather than on every bar.

govkit is a sibling kit, so the runner reaches it through the sibling-kit render token the hooks kit
README names (§12 of the charter), never by literal. UNVERIFIED: the token's spelling and how it
resolves in the dogfood tree; the builder reads it from that README first.

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
- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- the selection instrument, committed under this build's own build folder (S8)

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
- perf / scale: two `git` spawns per distinct recorded sha plus two `govkit.py` calls per bar, only in `changed` mode; nothing in the default mode.
- error / empty / loading states: no record, a bad record, an absent govkit and a non-ancestor sha all execute the leg; each held line names its reason.
- observability: every held leg prints its reason and recorded sha; the run header records the mode; the guard fallback prints the legs it applied to.
- risks: an under-declared selection set holds a suite that should have run; S5's lag bound caps how long, and a full run that reds an unselected suite is a declaration miss to file.
- testing: canary arms in the run-gates suite on a fixture with a stub govkit; a govkit selftest arm for `--epoch`; a pre-push arm for the coverage relation.
- migration: none; the version bumps under §4 Migration.
- user docs: `tools/run-gates/README.md` documents the mode, the record and the lag bound; the charter's merge-bar paragraph is unchanged unless F1 turns it on.

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
- **AC7** — When `check_green_record` reads a recorded green carrying `selftests changed`, it accepts it
  for a push in `changed` mode at that sha and forces for a push that runs every self-test. Red when:
  the second case is accepted, which would trust a partial tier as the whole one.
- **AC8** — When `python tools/govkit/govkit.py shipped --epoch` runs on this tree, every printed role
  is one of `EPOCH_ROLES`, and its rows are exactly the `shipped` rows in those roles. Red when: a
  `project-owned` or `generated` row is printed, or an epoch-role row is missing.
- **AC9** — When the committed selection instrument replays the built rule over the last 30
  first-parent commits on `main`, it prints the share of held leg-seconds selected and the count of
  commits selecting nothing. Red when: the share exceeds the 23% of rule B, meaning the set as built
  is the wide one. figure: DERIVED at observation; the research's 13% and 23 of 30 are the PINNED
  expectation, measured 2026-10-09 on node `a`, ±2x. cost: seconds, one `git diff` per commit.

## 7. Gates

`govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `recall floor arms` · `run-gates canary` · `pre-push self-test` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · a selection that ignores the moved path, then a record left behind by a red leg · none
New arm: tools/govkit/selftest.py · covers AC8 · `--epoch` printing a project-owned row · none
New arm: .githooks/pre-push.test.sh · covers AC7 · a `changed` record accepted for an every-self-test push · none

## 8. Open questions

- **F1 — May `changed` mode go back on the push boundary?** The owner ruled on 2026-08-27 that
  self-tests run on demand only, at every boundary (`.githooks/gate-env.sh` header).
  - (a) Yes, selected-only: `gate-env.sh` exports `GATE_SELFTESTS` as `changed`, so a push that moved
    a kit runs that kit's suites and a records-only push runs none. Reverses the 2026-08-27 ruling.
  - (b) No: the mode exists for developer and Definition-of-Done runs only; the ruling stands.
  - Recommendation: (a). The ruling's stated reason was cost on pushes that touch no kit source, and
    under this rule those pushes run no suite.
- **F2 — The "run everything every N" safety net: which N?**
  - (a) N=10, the same number as `GATE_FULL_MAX_LAG`, so the two lag bounds speak one value.
  - (b) A smaller N, more coverage of declaration misses at more cost.
  - (c) No age bound; rely on whoever runs the whole tier by hand.
  - Recommendation: (a), N=10.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "select held self-test legs by which kit shipped bytes moved"`
ranks the run-gates affordance seam `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` and no selection helper;
the unit extends govkit's `cmd_shipped` and the `EPOCH_ROLES` set `derive_epoch_state` already reads
(`tools/govkit/govkit.py`), and the existing held-tier branch in `tools/run-gates/run-gates.sh`,
rather than deriving "this kit moved" a second time. Prior records: TOOL-dUnstalledConvoy-26 and
TOOL-dUnstalledConvoy-27 (the held tier and the `selftests` coverage relation), TOOL-dUnstuckLanding-24.

Recall terms used: GATE_SELFTESTS held self-tests on demand push boundary owner ruling kit subject
selftests chunk gate-env pre-push epoch shipped
