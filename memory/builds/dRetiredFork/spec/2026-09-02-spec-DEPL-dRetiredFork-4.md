# DEPL-dRetiredFork-4 — the lf-pin pathspec goes over stdin

**Status:** CLOSED · rev-4 · 2026-09-03 · node d · Tier-1 · base b0108f13 · streams deployer · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-DEPL-dRetiredFork-4-1-acceptance-ledger.md](../build/2026-09-03-build-DEPL-dRetiredFork-4-1-acceptance-ledger.md) | journal | — |
| [2026-09-03-prompt-DEPL-dRetiredFork-4-1-build-brief.md](../prompts/2026-09-03-prompt-DEPL-dRetiredFork-4-1-build-brief.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md](../reviews/2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md) | diff-review | DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit apply` crashes with a traceback on a large adopter under Windows. The renormalize step's
dirty check passes every lf-pinned path as argv — `git diff --name-only HEAD -- <lf_paths>` — which
exceeds the 32 KiB command line. Measured on inCMS, whose `.gitattributes` is 28 KB:
`FileNotFoundError: [WinError 206] The filename or extension is too long`. It is WORSE than a
refusal because it fires AFTER the write loop and AFTER configure, leaving the target with new files
staged, a conf scaffolded, a Skill rendered, a stale write lock under its governance dir, and no
receipt update — a half-applied install from a verb that reported nothing. This is
`TOOL-aFlaggedScaffold-4`.

## 2. Scope (IN)

- **S1** — Pass the pathspec via `--pathspec-from-file=-` with `--pathspec-file-nul` over stdin,
  which removes the argv bound entirely rather than raising it.
- **S2** — The same treatment at every other site that builds a pathspec from a derived population,
  found by grep rather than by memory — one fixed call site leaves the class open.
- **S3** — An arm that constructs a pathspec exceeding 32 KiB and observes the command succeed;
  observed RED first against the current code.
- **S4** — The crash must become a REFUSAL if it can still happen for any reason, never a traceback
  after a partial write. A verb whose failure mode is a half-applied install owes an explicit
  rollback or an explicit refusal.

## 3. Non-goals (OUT)

- Rewriting the renormalize step's logic. Only how the path list reaches git.
- The stale write lock left by a previous crash. `DEPL-dCarriedReceipt-12` added the O_EXCL lock;
  cleaning an orphan is a separate concern.

## 6. Acceptance criteria

- **AC1** — When a fixture's lf-pin set exceeds 32 KiB of pathspec, `python
  tools/govkit/govkit.py apply --target <fixture>` completes; the pre-change command raised
  `WinError 206`.
- **AC2** — When the run cannot complete for any other reason, it REFUSES before the write loop
  rather than raising after it. Observed via `python tools/govkit/govkit.py apply --target <fixture>`.
- **AC2b** — A grep over `tools/govkit/govkit.py` for every site building a pathspec from a derived
  population returns ZERO still passing it as argv, and each converted site is named in the
  acceptance ledger. S2 requires the CLASS and rev-1 observed only the one reported call site — the
  charter's named failure, committed by a scope item that states the rule against itself.
- **AC3** — `python tools/govkit/selftest.py` passes with S3's arm added.
- **AC4** — `python tools/govkit/govkit.py selfcheck` exits `0`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix`.

## 8. Open questions

none - the crash is measured and the pathspec-over-stdin fix is the only mechanism
that clears a 32 KiB command line without dropping a path. This section is present
because a section 8 with neither an item nor a `none` form is a refusal, not a pass, and both
this spec's readers grade it that way.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding H13. S2 required the fix at every pathspec-building site and §6
  observed only the reported one, so the unit could pass with the class still open; AC2b is the
  class-wide observation.
- rev-3 . 2026-09-02 . added the section 8 `none` declaration both readers require;
  no design content changed.

- rev-4 . 2026-09-03 . BUILT. `git_pathspec` feeds the pathspec over stdin with
  `--pathspec-from-file=-` and `--pathspec-file-nul`, removing the 32 KiB bound rather than raising
  it. AC2b's CLASS is closed: five sites converted, and `index_read` named as deliberately outside
  it because it already chunks at 400. Four of the five were invisible to the crash report, which is
  why rev-2 added the class-wide criterion.

  BOTH HALVES OF THE ARM FIRE ON THIS HOST: a 40,500-byte pathspec succeeds over stdin with all 500
  paths reaching git, and the SAME list through argv still dies. The skip branch for a
  larger-command-line platform announces itself and was not needed.

  The change made TWO declarations stale and the gate caught both: the new function reds until
  SHELL_EXEC_SITES declares it, and `_cmd_update`'s row -- which existed for exactly the BinOp shape
  this unit removed -- redded on "declared but no longer spawning", with a paired map in the
  selftest redding the same way when only one side was taken out.

