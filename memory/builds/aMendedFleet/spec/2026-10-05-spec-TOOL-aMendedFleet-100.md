# TOOL-aMendedFleet-100 — the shard 2/8 fixture's bare origin commits under its own git identity

**Status:** CLOSED · rev-1 · 2026-10-05 · node a · Tier-1 · base 7af5f564 · streams tooling · order 101

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The unattended gate suite's shard 2/8 reds on every daily held run with
`fatal: unable to auto-detect email address (got 'runneradmin@runnervmfi6oq.(none)')`, the census's
cause C4. Its check-9 ghost-tip arm builds a commit with `git --git-dir="$ORIGIN" commit-tree`
inside the fixture's bare origin, and that bare repository is given no identity. A bare repository
inherits nothing from the scratch worktree beside it, so the call falls back to global config, and
the hosted runner has none. `$ghost` comes back empty, `update-ref` prints `fatal: : not a valid
SHA1`, and the arm's expected message never appears. Node a passes because its user config now
carries a global identity. This unit gives the bare origin its own identity, with the two lines the
driver suite already carries for the same defect, and records the recurrence in the gotcha that owns
the class.

## 2. Scope (IN)

- **S1** — `tools/unattended/check-unattended.test.sh` sets `user.email` and `user.name` on the bare
  origin immediately after `git init -q --bare "$ORIGIN"`, as two separate lines byte-identical to
  `tools/unattended/unattended.test.sh` lines 466 and 467, under a comment that names the
  `commit-tree` the ghost-tip arm runs inside it. Observed by AC1 and AC2.
- **S2** — `memory/gotchas/fixture-inherits-ambient-machine-state.md` gains an "It bit again"
  paragraph naming the suite and its ghost-tip arm in backticks, so the class is selected for a diff
  to that suite, and stating that node a now carries a global identity, so only an emptied global
  config reproduces the failure there. `memory/gotchas/INDEX.md` is re-rendered by
  `python tools/memory-tree/gotchas.py --write` in the same commit. Observed by AC3.

## 3. Non-goals (OUT)

- Setting a global git identity in the remote CI workflow. It would hide every fixture that leans on
  ambient identity rather than fix this one, and the runner having none is what lets the held job
  find them.
- A gate for the class. `git grep -nE -- '--git-dir=[^ ]+ commit-tree'` over the tree finds two
  sites, both unattended suites, and after S1 both bare repositories carry an identity. The hosted
  runner's held job is the standing detector for the class, because it is the one host with no
  identity; the gotcha is its documented check.
- Rewriting the gotcha's original "Where it bit" paragraph, whose statement that node a has no
  identity was true when written. S2 appends the correction instead.
- Moving the unattended kit version. The suite ships as kit bytes, and the build moves every kit
  version it owes once, after the last pass that touches that kit; the close's `kit epoch` leg grades
  that move.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; `git diff --stat 7af5f564 HEAD` is empty for both suites at HEAD
`34a99ad1`. Node d's branch `origin/branch/unattended-build-closing-f90fd9` carries line 303 as
`git init -q --bare "$ORIGIN"` with no identity after it, so there are no bytes of node d's to reuse.

- `tools/unattended/check-unattended.test.sh` line 302 creates the bare origin and line 306 sets its
  `HEAD` symref; nothing between or after sets an identity on it. Line 1386 runs the ghost-tip
  `commit-tree` inside it. Every other `commit-tree` in the suite runs in the scratch worktree, which
  line 162 gives an identity.
- `tools/unattended/unattended.test.sh` lines 462 to 467 carry the same fix for the same arm shape,
  with a comment recording that it was measured on node a.
- Run on node a, 2026-10-05, in a scratch bare repository under the user temp directory, with the
  empty tree from `git mktree`: `GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1 git --git-dir=o.git
  commit-tree <tree> -m ghost` printed `Author identity unknown`; after the two `config user.` lines
  it printed a commit sha. `git config --global --get user.email` answers on node a, which is why the
  suite passes there.
- `python tools/memory-tree/gotchas.py --for-paths tools/unattended/check-unattended.test.sh` does
  not list `fixture-inherits-ambient-machine-state` at base: the gotcha's only unattended anchor is
  `tools/unattended/unattended.test.sh`, and the selection's basename match does not reach this file.

### Files touched (estimate)

- `tools/unattended/check-unattended.test.sh`
- `memory/gotchas/fixture-inherits-ambient-machine-state.md`
- `memory/gotchas/INDEX.md`

### Alternatives rejected

- **`git -c user.email=… -c user.name=…` on the one `commit-tree` call.** It fixes the call and
  leaves the bare origin without an identity for the next arm that commits in it; the driver suite
  set the identity on the repository for that reason.
- **`GIT_AUTHOR_*` and `GIT_COMMITTER_*` exported for the whole suite.** It would mask any future
  fixture that forgets an identity on a node that has none, the very state the gotcha exists for.

## 5. Production-readiness checklist

- security — N/A: a test fixture's scratch repository only.
- perf / scale — two `git config` calls once per suite run.
- error / empty / loading states — N/A: no new state; the arm's existing refusal is what it grades.
- observability — N/A: no output changes on a host with an identity.
- risks — none on a host with an identity; on the runner the arm starts grading what it was written
  to grade, and may then report a real finding it was hiding.
- testing — AC1 to AC3 are seconds on node a; AC4 is the remote observation.
- migration — N/A.
- user docs — N/A: the gotcha is the record.

## 6. Acceptance criteria

- **AC1** — When `grep -n -A8 'git init -q --bare "[$]ORIGIN"$' tools/unattended/check-unattended.test.sh`
  runs, the lines after the bare init include `git --git-dir="$ORIGIN" config user.email t@t.test` and
  `git --git-dir="$ORIGIN" config user.name t`, each on its own line, ahead of the `symbolic-ref`.
  Red when: the identity lines are absent, as at base, or chained with `&&` to the symref line, which
  the suite's own comment there forbids.
- **AC2** — When the lines `grep -E '^git --git-dir="[$]ORIGIN" config user[.]' tools/unattended/check-unattended.test.sh`
  prints are run against a scratch bare repository bound to `$ORIGIN`, and then
  `GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1 git --git-dir="$ORIGIN" commit-tree` runs on the
  empty tree with `-m ghost`, it prints a 40-hex commit sha.
  Red when: the grep prints fewer than two lines, or the commit-tree prints `Author identity unknown`,
  which node a printed for the same scratch repository without those lines on 2026-10-05.
  fixture: the scratch bare repository goes under `%TEMP%` with a short name, never in the worktree.
- **AC3** — When `python tools/memory-tree/gotchas.py --for-paths tools/unattended/check-unattended.test.sh`
  runs, its checklist lists `fixture-inherits-ambient-machine-state`, and
  `python tools/memory-tree/gotchas.py --check` exits 0.
  Red when: S2's paragraph does not backtick the suite's path, so the class stays unselected as at
  base, or `INDEX.md` was not re-rendered and check 17 reds.
- **AC4** — When the first scheduled run of `remote-ci.yml` after landing completes,
  `gh run view <run id> --log-failed` carries no `unable to auto-detect email address` line in the
  `held unattended gate selftest shard 2/8` job, and no `not a valid SHA1` line from its ghost-tip arm.
  Red when: the bare origin still has no identity on the runner and the ghost commit is empty again.
  permission: remote CI after landing, which no unit pass can trigger.
  cost: up to one day, the schedule's period.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: none — S1 repairs an existing arm's fixture and adds no assertion.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the census journal's C4 row, the two unattended suites at
  base, and a scratch reproduction of the runner's empty identity on node a.

## 10. Reuse audit

The seam is `tools/unattended/unattended.test.sh` lines 462 to 467, the driver suite's identity on
its own bare origin, which S1 copies byte for byte; no symbol-level seam fits.
`python tools/codebase-map/reuse_lookup.py "test fixture gives a bare origin repository its own git identity before commit-tree"`
returned only name-stem neighbours such as `run_git`, and prints `unscanned layers: .sh`, so it cannot
see either suite; the seam was found by `git grep` for `commit-tree` over `tools/`. Recall returned
`memory/gotchas/fixture-inherits-ambient-machine-state.md` second, the record of the driver suite's
identical defect.

Where the records and the tree disagree: that gotcha says node a has no git identity at all. Node a
now has a global one, which is why shard 2/8 passes there and reds only on the runner. S2 records it.

Recall terms used: `python tools/memory-recall/query.py "why does a fixture's bare origin need its own git identity before commit-tree on a host with no global identity" --terms "bare origin commit-tree git identity user.email user.name fixture ambient global config hosted runner auto-detect"`
