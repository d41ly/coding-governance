# TOOL-dDeclaredLoop-58 — the LF-only criterion reads a counted, non-empty CLI output before it looks for a CR

**Status:** DEFERRED · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 5 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-58-deviation-581.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-58-deviation-581.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 51 at HIGH**, its item **H5**, alone in that item. `TOOL-dDeclaredLoop-38` AC1
runs `commit_trailers.py tokens HEAD~3..HEAD` over `TOOL-dDeclaredLoop-23`'s AC1 fixture, which builds
exactly three commits, so `HEAD~3` names nothing: git answers `unknown revision` with rc 128, the CLI
prints nothing or raises, and `od -c` finds no `\r` in an empty file. The only observation of the
LF-only producer fix passes on a build that leaves CRLF in place, and so does the `routed_commits.py`
arm `TOOL-dDeclaredLoop-38` §7 stages from it. This unit takes the report's corrected fix. It repairs
`TOOL-dDeclaredLoop-38`.

## 2. Scope (IN)

- **S1** — The criterion's range: `commit_trailers.py tokens HEAD` over the fixture, which names every
  commit reachable from the tip, so all three print. This supersedes `TOOL-dDeclaredLoop-38` AC1's
  `HEAD~3..HEAD`, not its population or its `od -c` read. Observed by AC1.
- **S2** — A count before the absence check: the output file must hold exactly three lines, each
  opening with a 40-hex sha, and only then is `\r` looked for. An empty or short file is red on its own,
  so the absence check can no longer pass on nothing. Observed by AC1, AC2.
- **S3** — The `routed_commits.py` arm `TOOL-dDeclaredLoop-38` §7 declares reads the CLI's bytes the
  same way: it captures stdout as bytes from `tokens HEAD` over the fixture, asserts three lines, then
  asserts no `b"\r"`; its staged failure, a scratch copy without the `reconfigure` call, reds on the
  CR, and a range naming nothing reds on the count. Observed by AC2, AC3.

## 3. Non-goals (OUT)

- The producer fix and the shell wrapper's CR strip: `TOOL-dDeclaredLoop-38` S1 and S2.
- A template rule that every absence criterion asserts a counted output first, the finding's
  left-shift: a governance carrier no clause of this build names; S2 and S3 are this criterion's
  instance, and the class is recorded at the close.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-38` — the LF-only `commit_trailers.py` CLI and its declared `routed_commits.py` arm, whose criterion this unit re-observes

## 4. Design

### Evidence

- `TOOL-dDeclaredLoop-23` AC1 builds its fixture "with three commits"; a `git log HEAD~3..HEAD` over a
  three-commit repository exits 128 with `unknown revision` (the report's probe, id 51, on
  git 2.54.0.windows.1).
- `TOOL-dDeclaredLoop-23` §4: `tokens <revs>` prints one line per commit, `<sha> PASSTRAILER <ids>` or
  `<sha> <subject tokens>`, so three commits print three sha-led lines.

### The observation

```bash
python commit_trailers.py tokens HEAD > "$out"        # in the fixture repository
[ "$(grep -cE '^[0-9a-f]{40} ' "$out")" = 3 ] || red "expected three sha-led lines"
od -c "$out" | grep -q '\\r' && red "a CR reached the output"
```

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`

### Alternatives rejected

- **`HEAD~2..HEAD`.** It prints two of three commits and keeps a range whose length the fixture fixes
  by hand; `tokens HEAD` follows the fixture.
- **Asserting a non-zero exit is red.** The CLI may print nothing and exit 0 on an empty range; the
  count is the observation that cannot pass on nothing.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one CLI call over a three-commit fixture.
- error / empty / loading states — S2 makes the empty output a red of its own.
- observability — the arm names which assertion failed, the count or the CR.
- risks — a fixture that grows a fourth commit reds the count; the figure is PINNED to
  `TOOL-dDeclaredLoop-23` AC1's three commits and moves with that fixture.
- testing — AC1 to AC3 as probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python commit_trailers.py tokens HEAD` runs on win32 in the fixture repository
  `commit_trailers.py --fixture` builds, with its output redirected to a file, `grep -cE '^[0-9a-f]{40} '`
  over the file prints `3` and `od -c` of it shows no `\r`.
  Red when: the range names nothing and the file is empty, or the CLI writes CRLF.
  figure: PINNED, the three commits of `TOOL-dDeclaredLoop-23` AC1's fixture.
- **AC2** — When the arm in `routed_commits.py` runs with the range `HEAD~3..HEAD` substituted in a
  scratch copy, it fails on the count, not on the CR check.
  Red when: the empty output passes the arm, as it passes `TOOL-dDeclaredLoop-38` AC1 today.
- **AC3** — When the arm runs over a scratch copy of the canonical `commit_trailers.py` with its
  `reconfigure` call removed, it fails naming the CR.
  Red when: the arm counts lines and never reads bytes, so CRLF passes.

## 7. Gates

`routed-commits selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 AC2 AC3 · the counted CLI bytes over the fixture, staged by an empty range and by a copy writing CRLF · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 51 (HIGH, item H5).

## 10. Reuse audit

The seam is the arm `TOOL-dDeclaredLoop-38` already declares in `tools/memory-tree/routed_commits.py`
and the fixture `TOOL-dDeclaredLoop-23` builds; this unit changes the range and adds a count, no new
fixture. `python tools/codebase-map/reuse_lookup.py "count output lines before asserting no carriage
return"` ranked `before`, `counts`, `check_line`, `read_git_output` and `render_line`, none an absence
check over a CLI's bytes, so no existing seam fits beyond the arm itself.

Recall terms used: commit_trailers tokens HEAD fixture three commits CRLF od empty output absence count routed_commits
