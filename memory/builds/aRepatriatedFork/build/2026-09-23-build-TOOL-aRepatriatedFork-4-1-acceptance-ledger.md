# TOOL-aRepatriatedFork-4 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-4

One unit pass under the mandate. It ran no merge bar and no self-test suite. Every criterion below
was observed by a direct run of a gate, or of the new arms sliced out of their suite with the
suite's own prologue. No adopter tree was read or written: the foreign layout is a fixture.

## The fixtures

- **Base bytes**: `check-verifier-fanout.sh` and `check-review-join.sh` as `git show a7c78ad2:` wrote
  them, copied to the scratchpad. The new arms ran against these first.
- **Foreign layout**: a scratch repo under `%TEMP%` with both gates at `scripts/workflows/`, the hook
  at `scripts/hooks/agent-cap.js`, and the harnesses under `.claude/workflows/` and `.claude/hooks/`.
- **Staged breaks**: one verifier-fanout copy with the marker test forced true, and one review-join
  copy whose union reads `\.claude` instead of `\.claude/workflows`. Each redded exactly its arm.

**Evidences:** TOOL-aRepatriatedFork-4
- AC1 — `bash tools/workflows/check-verifier-fanout.sh` — printed `clean — 7 workflow script(s)`, exit 0, in gov's tree
- AC2 — `tools/workflows/check-verifier-fanout.sh` — at the `scripts/` fixture it exited `1` naming `.claude/workflows/incident.js`; the a7c78ad2 bytes exited `1` with `the population is empty`
- AC3 — `export const meta` — the unmarked `.claude/workflows/helper.js` carrying the banned shape was not named; the marker-forced break copy named it and its arm went red
- AC4 — `bash tools/workflows/check-review-join.sh --explain` — printed `population under tools/ or .claude/workflows/` and `3 file(s) judged by arm 2`, exit 0
- AC5 — `tools/workflows/check-review-join.sh` — at the `scripts/` fixture it exited `1` naming `.claude/workflows/review.js:`; the a7c78ad2 bytes exited `1` with `no JavaScript under scripts/`
- AC6 — `.claude/hooks/` — the same run did not name `ban-table.js`, which carries the same join; the `\.claude` break copy named it and its arm went red
- AC7 — `tools/workflows/check-review-join.sh` — with neither directory holding JavaScript it printed `no JavaScript under scripts/ or .claude/workflows/`, exit 1
- AC8 — `git grep -n 'apply no marker filter' -- tools/workflows` — no line, exit 1
- AC9 — `bash tools/check-kit-versions.sh` — exit `0` at 1.9; with `review-harness@` alone reverted to 1.8 it exited 1 naming `gov:kit review-harness@ marker (1.8) != its meta.version (1.9)`
