# TOOL-aPrimedKeepalive-6 — hygiene checks 22 and 23 take the `--staged` guard all three of their siblings carry

**Status:** INPROGRESS · rev-2 · 2026-08-27 · node a · Tier-1 · base b4e1d5be · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-7 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/check-memory-hygiene.sh --staged` is the pre-commit fast leg. The block holding
checks 22 and 23 does not honour that mode, so every commit in this repo walks every tracked build
record and every closed Tier-2 spec. This build's own first commit timed out at 120 s on it. Add the
guard its three siblings already have.

## 2. Scope (IN)

- **S1** — the block at `tools/memory-tree/check-memory-hygiene.sh:1113`, currently opening on
  `if [ -n "$alcut" ]`, is guarded so it does not run under `--staged`, in the spelling its siblings
  at `:1051`, `:1066` and `:1076` use.
- **S2** — the change is measured: the pre-commit leg's wall clock before and after, on this node,
  recorded in the unit's journal record.
- **S3** — the guard's own liveness is asserted. The full (non-`--staged`) run must still execute
  checks 22 and 23, observed rather than assumed, because a guard that skips in both modes is a
  silently deleted check.

## 3. Non-goals (OUT)

- Any other check's scope. Three siblings already carry this guard and are not touched.
- Any change to what checks 22 and 23 ASSERT. This is a scope guard, not a predicate edit.
- Making the pre-commit leg fast in general. Other legs may also be slow; this unit fixes the one
  the owner's prompt names and the one this build measured.
- A gate on wall-clock cost for the hygiene leg. Charter §7 wants suites to declare a ceiling; that
  is a separate unit nobody has specced and it is named here so the omission is deliberate.

## 4. Design

### The asymmetry, verified at BASE

| Line | Checks | Opens on |
|---|---|---|
| `:1051` | 13–16 | `if [ "$STAGED" = 0 ]` |
| `:1066` | 17–19 | `if [ "$STAGED" = 0 ]` |
| `:1076` | 13–19 row grammar | `if [ "$STAGED" = 0 ]` |
| `:1113` | 22–23 | `if [ -n "$alcut" ]` — **no mode guard** |

Checks 22 and 23 join every acceptance criterion of every CLOSED Tier-2 unit against every
`**Evidences:**` block in every tracked record under `builds/*/build/` and `builds/*/reviews/`. That
population is corpus-wide and does not change because a commit stages three files.

### Why skipping under `--staged` is correct and not a relaxation

The file states its own split at `:9`: *"pre-commit fast leg (set-checks tree-wide, file-checks on
staged paths)"*, and at `:732`: *"CI's full run is the tree-wide truth"*. Checks 22 and 23 are a
coverage join over terminal specs — the class its three siblings are in, and every one of those is
already guarded. The full bar at the push boundary keeps running them, so nothing loses coverage
between a commit and a push.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` — one line. The kit's `HYGIENE.template.md` and
`memory/HYGIENE.md` describe the checks, not their mode guards, and are re-read at build time to
confirm neither states a guarantee this change would falsify.

### Alternatives rejected

**Make the join incremental under `--staged`.** More code, a second population to keep correct, and
it answers a question the pre-commit leg is not supposed to answer. Rejected on the file's own
stated split.

## 5. Production-readiness checklist

- security — N/A, a mode guard on a local check.
- perf / scale — this IS the perf item; S2 measures it.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the full run still names checks 22 and 23; S3 observes that.
- risks — the one risk is silently disarming the checks in BOTH modes, which S3's liveness
  assertion is written to catch.
- testing + left-shift gates — the full bar exercises the unguarded path on every push.
- migration / rollback — one line; revert is the rollback.
- user docs — none; `HYGIENE.md` documents predicates, not mode guards.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs on a tree with files
  staged, its wall clock is at least an order of magnitude below the recorded pre-change figure, and
  both figures are in the unit's journal record.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs with no `--staged`, checks
  `22` and `23` still execute — observed by their own output lines, not inferred from a green exit.
- **AC3** — When a commit is made in this worktree after the change, the pre-commit hook completes
  well inside the 120 s that timed out before it, observed on an actual `git commit`.
- **AC4** — When the change is staged as a BREAK — the guard inverted so the block runs only under
  `--staged` — the full run stops reporting checks 22 and 23, confirming the guard is the thing
  deciding, and the break is then unstaged.

## 7. Gates

`memory tree hygiene` on the full bar, and `bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft. Authored under a standing mandate as an ADOPTED discovery: the
  owner's prompt cites this fix by its measurement, `aGroundedOrientation` parked it twice, and it
  taxes every commit of this build until it lands.
- rev-2 · 2026-08-27 · AC4 as drafted was UNFALSIFIABLE and running it is what showed that: checks
  22 and 23 print nothing when green, so grepping for their absence after inverting the guard
  returns 0 whether or not the guard decides anything. That is this corpus's own
  `fixture-passes-by-finding-nothing` class, occurring in an acceptance criterion rather than in
  code. Replaced by a real staged break — an acceptance criterion no journal record evidences,
  inserted into a CLOSED Tier-2 spec's §6 — asserted RED on the full run and absent under `--staged`.

## 10. Reuse audit

The seam is the guard spelling itself, cited by path: `tools/memory-tree/check-memory-hygiene.sh`
`:1051`, `:1066` and `:1076` each open their block with `if [ "$STAGED" = 0 ]`. This unit extends
that existing seam to the one block missing it rather than inventing a mechanism — the file already
carries `STAGED`, `in_scope()` and `STAGED_MD` for exactly this purpose.

Recall terms used: `hygiene staged guard pre-commit fast leg acceptance ledger check 22 23 corpus
walk wall clock`. The `reuse_lookup.py` pass over "skipping a corpus-wide check in the pre-commit
fast leg" returned the hygiene kit's own dossier and no competing mechanism.
