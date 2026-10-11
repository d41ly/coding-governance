# TOOL-aBriskPreflight-10 — the tracked pre-commit hook is executable again

**Status:** SPECCED · rev-1 · 2026-10-11 · node a · Tier-1 · base 271a9004 · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`.githooks/pre-commit` is tracked `100755` again. `origin/main` carries it `100644` since the
aDistilledCharter reconcile merge `60bea5e80`, so on a POSIX checkout git skips the hook — the
branch guard and the staged hygiene gate are dormant there — and `check-wiring.sh --check` prints
`UNWIRED hooks — .githooks/pre-commit is tracked 100644` in every checkout whose `core.hooksPath`
names its own `.githooks`. This build met it as a refused fixture preflight (check 4) during its own
A/B, after its mid-build merge of `origin/main` brought the mode in. Adopted under the discoveries
rule: it makes an observable this repo already measures — that wiring arm — strictly better, and
makes nothing it measures worse.

## 2. Scope (IN)

- **S1** — The index mode of `.githooks/pre-commit` becomes `100755`, its blob unchanged, through
  `git update-index --chmod=+x`. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Any byte of the hook. The blob id does not move.
- Every other hook's mode: `commit-msg`, `pre-push` and `pre-rebase` are already `100755`.
- Who regressed it, and a gate on the merge that did: the hook-mode arm already reports it, and the
  merge bar it would have met was not run at that landing.

## 4. Design

One index operation. `git update-index --chmod=+x .githooks/pre-commit` stages the mode with the blob
the index already holds; on this Windows node the working file's bit is not graded, which is why the
wiring arm reads the index and not the filesystem.

## 5. Acceptance criteria

- **AC1** — `git ls-files -s .githooks/pre-commit` prints mode `100755` at the pass commit, and its
  blob id equals the one `git ls-tree origin/main -- .githooks/pre-commit` prints (`e93bdaa0`).
  Red when: the mode reads `100644`, or the blob id moved, which would mean the hook's bytes changed.
- **AC2** — In a throwaway clone whose `core.hooksPath` is its own `.githooks`, `check-wiring.sh --check`
  prints `ok       hooks     — every tracked hook in .githooks is executable` with the pass commit's
  index, and prints the `UNWIRED  hooks` line naming `pre-commit` with its parent's.
  Red when: the pass commit's run still prints that `UNWIRED` line, or the parent's run does not,
  which would mean the arm never graded the regressed mode.
  fixture: a clone under `%TEMP%`, never this worktree, whose `core.hooksPath` names another checkout.

## 6. Gates

`check-wiring self-test` · `memory hygiene`

This unit adds no leg.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-11 · initial draft, authored by the main loop under the discoveries rule.

## 9. Reuse audit

No code is written: the repair is the one `git update-index --cacheinfo`/`--chmod` act the hook-mode
arm's own `--fix` performs (`check_hook_modes` in `tools/check-wiring.sh`), applied by hand because
`--fix` refuses to stage a mode for a directory another checkout supplies. No existing seam is
extended; none is needed.

Recall terms used: none — the defect is located by `git ls-tree` and the arm that reports it; there
is no prior decision to recall about a mode a merge dropped.
