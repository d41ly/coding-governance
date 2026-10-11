# TOOL-aPrimedIndex-10 — the in-place landing checks the allow record against what it pushed

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-1 · base c7604c36 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aPrimedIndex-10-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-10-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`push-main.sh --land` pushes `HEAD`, but it checks the pre-push hook's allow record against the
prepared merge's sha. Under `LANDER_MODE=in-place` the close commits its records on top of the
prepared merge, so the two differ, and every in-place landing, this build's included, reports
`landed UNGATED`, exits 4 and writes no lander marker. The reconcile with origin/main brought the
check in (TOOL-aSignalledHook-1); arm 16 of the lander suite is red on origin/main for it. Separately,
the post-merge fixture unsets the hooks path, so no hook writes the record and arms pm1 to pm8, 26
and 29 read exit 4 on a push that landed.

## 2. Scope (IN)

- **S1** — `cmd_land` captures the sha it pushes, `HEAD`, before the push and passes it to
  `check_push_allow`. Observed by AC1.
- **S2** — The `work6` fixture installs a stub pre-push hook that writes the allow record for the
  pushed sha, instead of unsetting the hooks path. Observed by AC2.

## 3. Non-goals (OUT)

- `check_push_allow` and the hook's allow write are unchanged.
- The attended path already reads the sha it pushes and is unchanged.

### Edges

- **consumes-from** `TOOL-aPrimedIndex-4` — the lander paths this build regenerates on.

## 4. Design

`cmd_land` reads `git rev-parse --verify HEAD` into a local just before `git push`, the attended
path's shape, and hands that to `check_push_allow` in place of the prepared sha `t`. The stub hook
reads git's ref lines from stdin and writes `<local sha><TAB>stub` to `$(git rev-parse --git-dir)/pre-push-allow`,
the file the lander clears and reads, as the real hook does at its success exit.

### Files touched (estimate)

- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `memory/map/features/push-main.md`

## 5. Production-readiness checklist

- security: the check still requires the hook's record to name the pushed commit; it now names the
  commit actually pushed.
- perf / scale: one `rev-parse` per attempt.
- error / empty / loading states: unchanged; a missing or mismatched record still exits 4.
- observability: the UNGATED line names the pushed sha, which is now the one git pushed.
- risks: none beyond the comparison's operand.
- testing: arm 16 and the post-merge arms, in one run of the lander suite.
- migration: none.
- user docs: N/A.

## 6. Acceptance criteria

- **AC1** — When arm 16 lands a prepared merge with a commit on top of it, `--land` exits 0.
  Red when: it exits 4 naming the prepared sha, as it does at c7604c36.
- **AC2** — When the post-merge fixture lands behind its stub hook, pm1 to pm8, 26 and 29 read
  exit 0 and no `landed UNGATED` line. Red when: any reads exit 4, as they do at c7604c36.

## 7. Gates

`push-main self-test` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness`

New arm: tools/push-main.test.sh · covers AC1 AC2 · arm 16's prepared merge with a records commit on top, and the post-merge fixture behind an allowing stub hook · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, adopted from the lander suite's attribution after the reconcile.

## 10. Reuse audit

The operand follows the attended path's `pushed=$(git rev-parse --verify …)` in `tools/push-main.sh`;
the stub hook follows the suite's existing `killed-hook` fixture. No existing seam fits a hook that
allows: the suite's only stub hook is the killed one, and `reuse_lookup.py` ranks only generic
`write` and `pre` helpers, none a hook.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
