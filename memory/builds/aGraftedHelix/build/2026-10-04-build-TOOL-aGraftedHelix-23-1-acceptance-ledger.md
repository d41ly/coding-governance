# Acceptance ledger — TOOL-aGraftedHelix-23

**Serves:** journal TOOL-aGraftedHelix-23

Node `a`, 2026-10-05. The build commit is `aeab6521`, over the spec's rev-6 commit `32980803`, which
moved AC5's sequence-d restart short of the closing call before any code. No merge bar and no
self-test suite ran in this pass. The criteria were observed by the suite's new prior-session set
block run ALONE behind the suite's prologue, the claim block's `gh_` helpers and unit 20's
prior-session helpers, as slices under `tools/unattended/` with fixtures under a short `%TEMP%`
root: 181 executed against the prologue's own 20 and the slice's one setup `mutate`, green against
the kit. Unit 20's block, whose two cleared-state assertions now read the empty set, ran the same
way: 72 executed, green. Each arm was then observed RED against a scratch copy of the driver with
one break, or one group of breaks whose arms are disjoint, staged beside a copy of the library; the
kit's driver was never edited for a break. The slices were deleted after the last run. The whole
suite is the main loop's at VERIFYING, and the block count, 160, is the evidence for its raised
floors.

**Evidences:** TOOL-aGraftedHelix-23
- AC1 — `prior-session: s1 s2` — in the slice, sequences a, b, c and d each left that line byte for
  byte before the closing s3 call, which exited 0, printed no check 90, left the claim naming s3 and
  the set empty. In a the no-session `--beat` printed `renewed`, in b the s2 `--dispatch` exited 0,
  and after each the claim named s2 and the set read s1. Red under unit 20's absent-only write: the
  line read `prior-session: s1` and the a, b and c closing calls exited 1 with check 90. Red under
  `--beat` and `--dispatch` emptying the set: the set read empty after them in a, b and c. Red under
  the set written as the read claim's session alone: d's set read empty and its closing call
  answered check 90.
- AC2 — `git status --porcelain` — sequences e and f left `prior-session: s1 s2` with the claim at
  s1, and each closing call exited 0 with no check 90 and an empty set. Over the committed base and
  an aged claim, the landed s1 renewal moved the claim ref and `git status --porcelain` printed
  nothing; the s1 renewal whose push exited 124 printed unit 1's `claim not written` announce line,
  exited 0, printed nothing for porcelain and left no prior-session line. Red under the pre-call
  session written unconditionally: e and f read `prior-session: s2` and both closing calls answered
  check 90. Red under the clear written while empty: porcelain printed the staged run-state file.
  Red under the add unscoped from write_lease due: porcelain printed the staged run-state file and
  the record held one prior-session line.
- AC3 — `CLAUDE_CODE_SESSION_ID` — preflighted with it unset, record and claim named `absent`; the
  s2 call whose push exited 124 left the set reading `absent`, and the closing s2 call exited 0 with
  no check 90, the claim at s2 and an empty set. Red under `absent` read as no fact: the closing call
  exited 1 with check 90 and the claim stayed `absent`.
- AC4 — `unattended: claim not written` — after one incomplete s2 call, the s2 `--dispatch` of
  sequence b exited 0 with no check 90 and moved the claim to s2 with the set at s1. In a second
  copy, the incomplete call staged the record, which was committed and the branch pushed: the claim
  still named s1 and the set s1, and the s2 `--hold` printed neither check 2 nor that line, left
  the claim `held` and the set s1. Red under the set read at the `--resume` row only: `--dispatch`
  exited 1 with check 90, and `--hold` printed that line and left the claim `live`.
- AC5 — `UNATTENDED check 89 FAILED` — after sequence d short of its closing call, claim at s1, the
  s3 restart under pid 4244 and keepalive k3 printed `TAKES THE RUN OVER`, no check 89, and left
  the claim at k3 and s3. After sequence c short of its closing call, claim at s2 and set s1 s2, the
  same restart did the same; over the `absent` lease, the s2 restart under k2 left k2 and s2. Red
  under the whole-value comparison: d and c exited 1 with check 89 and the claim stayed k1. Red
  under the first member alone: c did. Red under an `absent` member skipped: the `absent` leg did.
- AC6 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base 329808030` printed `epoch: unattended · clean · 1.70`,
  naming no carrier left behind; the unattended version moved 1.69 -> 1.70 in 27 files.
