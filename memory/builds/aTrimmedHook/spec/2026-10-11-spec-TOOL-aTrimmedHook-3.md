# TOOL-aTrimmedHook-3 — `commit-msg` starts the unattended driver only when a run names the branch

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-KICK-aTrimmedHook-1-runlog-2270b345.md](../build/2026-10-11-build-KICK-aTrimmedHook-1-runlog-2270b345.md) | journal | KICK-aTrimmedHook-1 TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-2 TOOL-aTrimmedHook-4 TOOL-aTrimmedHook-5 TOOL-aTrimmedHook-6 TOOL-aTrimmedHook-7 |
| [2026-10-11-build-TOOL-aTrimmedHook-3-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aTrimmedHook-3-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md) | research | TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-2 KICK-aTrimmedHook-1 |
| [2026-10-11-prompt-TOOL-aTrimmedHook-3-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aTrimmedHook-3-1-build-brief.md) | journal | — |
| [2026-10-11-review-TOOL-aTrimmedHook-1-closing-diff-round1.md](../reviews/2026-10-11-review-TOOL-aTrimmedHook-1-closing-diff-round1.md) | diff-review | TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-2 KICK-aTrimmedHook-1 |

<!-- /gen:spec-records -->

## 1. Goal

`.githooks/commit-msg` runs `tools/unattended/unattended.sh --check-commit` on every commit. The
driver's top-level initialisation costs about 50 s on node a (2026-10-11, detached HEAD, 71-78 host
bash processes) before its first question, whose answer is almost always "no run is bound to this
branch". This unit asks that question in the hook first, with the driver's own predicate, and starts
the driver only when it can matter.

## 2. Scope (IN)

- **S1 — the pre-filter.** Before the driver call, the hook reads the current branch's full ref with
  `git symbolic-ref -q HEAD` and lists tracked run-state files naming it with
  `git ls-files -- ':(glob)**/builds/*/RUN.md' | xargs -r grep -lF -- ": <ref>"`. No ref, or no hit,
  skips the driver. A hit runs it exactly as at BASE. Observed by AC1 and AC2.
- **S2 — the header.** The hook's comment block states that the pre-filter is the driver's own first
  narrowing (`check_commit_message`, ~12829-12831 at BASE), widened to any memory root by the glob so
  the error direction is "run the driver", and that its silence is the driver's own silent answer.
  Observed by AC3.

## 3. Non-goals (OUT)

- **N1** — no change to `tools/unattended/unattended.sh`; no lazy initialisation of the driver.
- **N2** — the "conf present, kit absent" note and the merge-only transition audit below it are
  unchanged.
- **N3** — no change to the hook's mode or to `tools/check-wiring.sh`, which grades the hook's wiring
  and its 100755 mode.

### Edges

none

## 4. Design

The driver narrows its candidates with exactly this pair before reading any record's phase or
holder: `ref=$(GIT symbolic-ref -q HEAD) || return 0`, then
`GIT ls-files -- ":(glob)$M/builds/*/RUN.md" | xargs -r grep -lF -- ": $ref"`. The hook cannot read
`$M` without sourcing the driver, so it globs `**/builds/*/RUN.md`, a superset; a candidate the
driver's own pattern would not have listed only costs a driver run, which then answers silently as
at BASE. A record whose phase is terminal still passes the pre-filter, for the same reason. The skip
prints nothing, because the driver prints nothing on that path today: the verdict is unchanged, only
the process is saved.

### Files touched (estimate)

- `.githooks/commit-msg`

### Alternatives rejected

- **Lazy initialisation of the driver's verbs** (the prompt's second option). A 14k-line driver's
  init order is shared by every verb, so the change would reach far beyond this question; the hook
  pre-filter is one predicate the driver already states.

## 5. Production-readiness checklist

- security — N/A — the hook reads tracked files and the branch ref; no new input surface.
- perf / scale — three spawns in place of the driver's ~50 s initialisation, on every commit no run
  names.
- error / empty / loading states — a detached HEAD skips, as the driver returns 0 there.
- observability — none added: the skipped path is silent at BASE too.
- risks — a run-state file outside `**/builds/*/` would be missed; the driver's own glob is
  `$M/builds/*/RUN.md`, which the superset covers for any `MEMORY_ROOT`.
- testing — AC1 and AC2 in a scratch repository; no suite.
- migration — none.
- user docs — N/A — no `help/` page and no kit README covers this gov-only hook.

## 6. Acceptance criteria

- **AC1** — When `bash .githooks/commit-msg <msg>` runs in a scratch clone whose branch no tracked
  `RUN.md` names, with a stub `tools/unattended/unattended.sh` that writes a marker file, the marker
  is not written.
  Red when: the marker is written.
  cost: seconds; the scratch clone lives under a short `%TEMP%` root.
- **AC2** — When the same clone tracks a run-state file under a build folder carrying
  `run-branch: refs/heads/<its branch>`, the marker is written.
  Red when: the marker is absent. Observed RED first with the pre-filter's `grep` pattern broken.
- **AC3** — When `grep -in 'first narrowing' .githooks/commit-msg` runs, it prints the header line S2
  adds.
  Red when: it prints nothing.

## 7. Gates

`branch-guard self-test` · `check-wiring self-test`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · AC2 names the fixture's run-state file in prose, after the spec-token check refused a path no tree tracks

## 10. Reuse audit

The seam is the driver's own narrowing in `check_commit_message` (`tools/unattended/unattended.sh`,
~12829-12831 at BASE), replayed in the hook. `python tools/codebase-map/reuse_lookup.py "find the
run-state record naming the current branch"` returned only name-stem matches (`run`, `records`,
`run_arms`, `branches`).

Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit
