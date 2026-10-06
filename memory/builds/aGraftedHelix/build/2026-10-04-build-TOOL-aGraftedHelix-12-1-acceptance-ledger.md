# Acceptance ledger — TOOL-aGraftedHelix-12

**Serves:** journal TOOL-aGraftedHelix-12

Node `a`, 2026-10-05. The build commit is `eea57b04`, over the spec's rev-4 commit `862a0dd5`. No merge
bar and no self-test suite ran in this pass. The criteria were observed by the driver suite's new
claim-cell block run ALONE behind the suite's prologue and the claim block's `gh_` helpers, as a slice
under `tools/unattended/` with its fixtures under `%TEMP%`: 61 executed against the prologue's 20,
green against the kit, in 270 s and again in 286 s. Each cell was then observed RED against a staged
break in a driver copy. A copy whose row lookup never finds the slug, so every claim reads `none`,
redded the 28 cells that are not `none` and left the four `none` cells green. A copy whose `none` row
writes only at `--preflight` redded the take-over, holder and status `none` cells. The first draft of
that break, with no `none` row at all, redded `none/preflight` and stopped every base from building.
The first run of the `none`-for-all break left eight cells green, which is why rev-4 added the `lost`
outcome. The copies and slices were deleted after each run. The whole suite is the main loop's at
VERIFYING, and the slice count, 41, is the evidence for its raised floors.

**Evidences:** TOOL-aGraftedHelix-12
- AC1 — `UNATTENDED check 89 FAILED` — the cells `held/preflight` and `unknown/preflight`, each
  `--preflight tFresh --keepalive-id k2` under `CLAUDE_CODE_SESSION_ID=s-new`, read `1 89 same same -`:
  exit 1, check 89, the claim ref unmoved, and `memory/builds/tFresh/RUN.md` absent before and after.
  The cells `terminal/take-over` (a foreign `landed` claim) and `unknown/take-over`, each a
  `--resume tRun --keepalive-id k2` under `s-new` reaching `run_takeover` on a record whose newest
  commit is dated 2000, read the same tuple with the run-state file byte-unchanged. Red under the break that
  read every claim as `none`: `1 90 same same lost` in all four.
- AC2 — `--beat` — over the claim fixture after `--preflight tRun --keepalive-id k1`, `--beat tRun`
  printed `unattended: beat — tRun · skipped: the beat is not yet due` and `git ls-remote` printed
  the same sha before and after; with the claim reseeded to `s-other` live it printed
  `skipped: the claim is not this run's: tRun · node other · session s-other`, no
  `skipped: verdict`, and the sha did not move. Red when the `beat:*` row renewed instead of declining: `renewed` and a moved sha;
  red when `beat:mine` dropped its due test: `renewed` over the young beat and a moved sha.
- AC3 — `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` — run as
  `python tools/govkit/govkit.py epoch --base 862a0dd59` at the build commit it printed
  `epoch: unattended · clean · 1.64` and named no carrier left behind; `bash tools/check-kit-versions.sh`
  printed `clean — 16 declared carrier(s) under tools/`.
