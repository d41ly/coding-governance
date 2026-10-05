# Acceptance ledger — TOOL-aGraftedHelix-19

**Serves:** journal TOOL-aGraftedHelix-19

Node `a`, 2026-10-05. The build commit is `6a1a2feb`, over the spec's rev-3 commit `df5f7cb8`, which
reconciled the spec with the built driver before any code: the function spells `same`,
`foreign-unknown` and `status`, and meets a fifth mode, `beat`. No merge bar and no self-test suite
ran in this pass. The criteria were observed by slices under `tools/unattended/`, behind the suite's
prologue and the claim block's `gh_` helpers, with fixtures under a short `%TEMP%` root. The claim-cell
block with the mode-refusal arm executed 74 against the prologue's 20, green, before the
refused-`--beat` pair was added. The mode-refusal arm alone, with that pair, executed 27, green. The
derived-set assertion was also run alone over the kit's driver and a copy with a phantom mode. Each
arm was then observed RED against staged driver copies, deleted after each run. The whole suite is
the main loop's at VERIFYING, and the slice counts are the evidence for its floors, raised by 15.

**Evidences:** TOOL-aGraftedHelix-19
- AC1 — `CLAIM_READS` — `grep -E '^CLAIM_(READS|MODES)=' tools/unattended/unattended.sh` at the
  build commit printed two lines; the quoted value of `CLAIM_READS` counted 8 words under `wc -w`
  and that of `CLAIM_MODES` 5, the function's eight classes and its five modes (spec rev-3, §9).
- AC2 — `CLAIM_MODES` — in the slice, a scratch driver whose `CLAIM_MODES` lacked `status` ran
  `--hold tRun --code platform-limit --until owner --reason "the mode axis" --reaped k1` over the
  held claim fixture and printed `UNATTENDED check 92 FAILED` naming `mode status` and
  `CLAIM_MODES preflight take-over holder beat`; the claim ref on the bare origin read the same sha
  before and after. With the membership test also removed from the copy, the same call moved that
  sha, `73e8e446` to `38e317ba`, and the arm redded on both assertions. The `--beat` half: a copy
  lacking `beat` over no claim printed `skipped: the claim write table refused the call` and
  created none; red when that branch was removed, the call then creating a claim.
- AC3 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base df5f7cb82` printed `epoch: unattended · clean · 1.66`,
  naming no carrier left behind; the unattended version moved 1.65 -> 1.66 in 27 files.

The suite-only observations, left to the main loop's run at VERIFYING: S3's derived-set assertion
redded over a copy whose `CLAIM_MODES` gained `phantom`, naming the eight cells `<class>/phantom`
as having no typed outcome, and was green over the kit's driver. The eight new `beat` cells were
green against the kit. Against a copy whose `beat:mine` never wrote and whose `beat:*` row was
removed, `mine/beat` and the six declining cells redded and `none/beat` stayed green.
