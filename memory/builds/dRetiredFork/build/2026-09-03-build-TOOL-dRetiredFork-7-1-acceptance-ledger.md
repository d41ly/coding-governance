# TOOL-dRetiredFork-7 — acceptance ledger

**Serves:** journal TOOL-dRetiredFork-7

**Evidences:** TOOL-dRetiredFork-7
- AC1 — `bash tools/workflows/check-review-join.sh` — a scratch tree whose harness drops a wave with `.filter(Boolean)` and takes no arity exits 1 naming `tools/workflows/h.js:3`; the SAME fixture against the pre-change script exited 0
- AC2 — `bash tools/workflows/check-review-join.sh` — the same wave with `const lensesDead = LENSES.length - live.length` read again exits 0, reporting 1 file judged
- AC3 — `bash tools/workflows/check-review-join.sh` — a tree that dispatches agents while arm 2 judges none exits 2, REFUSED; the pre-change script exited 0
- AC4 — `bash tools/workflows/check-review-join.sh --explain` — run over gov's tree BEFORE wiring: 7 files scanned, 3 JUDGED (`drift-audit-code.js`, `drift-audit-state.js`, `tier2-review.js`) with counters read 12, 12 and 13 times, 4 not judged, zero LIVE hits. Near-miss recorded: `unattended-build.js` dispatches agents but has no falsy drop, so the arm correctly does not apply. F2's FACT-QUESTION is answered — gov's own harnesses already count their waves
- AC5 — `bash tools/check-kit-versions.sh` — exits 0 after the 1.4 to 1.5 bump AND exits 1 naming `tier2-review.js gov:kit review-harness@ marker (1.4) != its meta.version (1.5)` with that marker alone reverted

## What AC5 found, which is the reason it was written two-sided

The RED could not be produced at first: the `gov:kit review-harness@` marker was paired by NOTHING,
so reverting it left the gate at exit 0. A version marker no gate checks is not a carrier, it is a
comment — and it could have drifted a whole release silently. `check-kit-versions.sh` now pairs BOTH
ids on that file against its `meta.version`. rev-2 added AC5's second half precisely because a bare
post-bump green cannot fail; it earned its keep on first use.

## And one correction to my own first cut of S3

The liveness refusal as first written fired whenever arm 2 judged nothing, which broke a legitimate
pre-existing arm whose fixture tree has no harness at all. "No harness here" and "harnesses here and
none judged" are different facts and only the second is a liveness failure. Tightened, and the AC3
fixture rewritten to dispatch agents without a falsy drop so it still exercises the refusal.
