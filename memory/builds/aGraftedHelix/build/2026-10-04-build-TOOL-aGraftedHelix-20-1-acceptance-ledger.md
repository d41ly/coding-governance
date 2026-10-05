# Acceptance ledger — TOOL-aGraftedHelix-20

**Serves:** journal TOOL-aGraftedHelix-20

Node `a`, 2026-10-05. The build commit is `598f7fd5`, over the spec's rev-7 commit `11ca8be1`, which
reconciled AC3's date shim and AC6's `s3` fixture with the suite before any code. No merge bar and
no self-test suite ran in this pass. The driver criteria were observed by the suite's new
prior-session block run ALONE behind the suite's prologue and the claim block's `gh_` helpers, as a
slice under `tools/unattended/` with its fixtures under a short `%TEMP%` root: 71 executed against
the prologue's own 20, green against the kit in 125 s. Each arm was then observed RED with one break
staged in the driver in place, seven breaks in all, the driver restored byte for byte after each run
and its hash checked. The slice was deleted after the last run. AC4 was observed by a scratch
repository sourcing the library directly. The whole suite is the main loop's at VERIFYING, and the
slice count, 51, is the evidence for its raised floors.

**Evidences:** TOOL-aGraftedHelix-20
- AC1 — `UNATTENDED check 90 FAILED` — in the slice, a record and claim preflighted under `s1`, then
  the holder's `--resume tRun --keepalive-id k1` under `s2` with unit 1's racer shim on `PATH`, which
  moves `refs/gov/runs/tRun` before forwarding the push: it exited non-zero printing check 90, the
  record's `session` read `s1`, its hash was unchanged, both `git diff --name-only` and
  `git diff --cached --name-only` named no run-state file, and the racer's claim stood. Red under the
  break that moved the CAS back after `write_lease`: `session` read `s2`, the hash moved, and the
  working copy named `memory/builds/tRun/RUN.md`.
- AC2 — `prior-session: s1` — the `s2` call whose claim push the shim made exit 124 exited 0 printing
  `claim not written`, the record read `session: s2` and `prior-session: s1`, the claim on the bare
  origin still named `session: s1`, and the record was staged; the second `s2` call with no shim
  exited 0, printed no `UNATTENDED check 90 FAILED`, left the claim naming `s2` and
  `prior-session: absent`, staged. With the bare origin renamed away for the first call it printed
  `claims not read` and every assertion held the same, the second call made with it restored. Red
  under the break that removed S3's widening: the second call exited 1 with check 90 and the claim
  stayed `s1`, in both arms. Red under the break that left `prior-session` unwritten: the fact read
  empty and the second call exited 1 with check 90, in both arms.
- AC3 — `lease-utc` — under a `date` shim answering `date -u` with the stamp format one more second
  ahead per read, the landing `s2` call exited 0, the shim's count reached at least two, the claim's
  `lease-utc` equalled the record's byte for byte, and `grep -c '^prior-session:'` printed 0. With
  the record committed and the claim re-seeded at a beat a third of `RESUME_STALE_BOUND` old, the
  next `s2` call exited 0, the claim ref moved, and `git status --porcelain` printed nothing. Red
  under the break whose claim CAS read its own clock: `2026-10-05T05:09:44Z` against the record's
  `2026-10-05T05:09:43Z`. Red under the break that cleared the fact over a record without it:
  `git status --porcelain` printed `M  memory/builds/tRun/RUN.md`.
- AC4 — `check_lease_only_diff` — sourced from `tools/unattended/lib-unattended.sh` in a scratch
  repository whose committed run-state file differed from its working copy only by an added
  `prior-session: s1` line, it returned 0; with `phase: RUNNING` changed to `HELD` as well it returned
  1. Sourced from the parent commit's library, the first case returned 1.
- AC5 — `bash tools/check-kit-versions.sh` — at the build commit it printed
  `kit-versions: clean — 16 declared carrier(s) under tools/`, and
  `python tools/govkit/govkit.py epoch --base 11ca8be15` printed `epoch: unattended · clean · 1.68`,
  naming no carrier left behind; the unattended version moved 1.67 -> 1.68 in 27 files.
- AC6 — `UNATTENDED check 89 FAILED` — after the 124 call, its record committed under a 2000 date,
  the `s2` call under `CLAUDE_PID=4242` with `--keepalive-id k2` printed the restart row's
  `TAKES THE RUN OVER in its place`, exited 0, printed no check 89, and left the claim naming `k2` and
  `s2`. Reset to that commit with the claim re-seeded under `s1` and `k1` at a beat older than the
  bound, the `s3` call with `k3` printed `presumed-stopped` and `claim taken over — tRun · node`
  naming `session s1`. Red under the break that removed S8's widening: the restart exited 1 with
  check 89 and the claim stayed `k1` and `s1`. Red under the break that handed the record to every
  take-over: no `claim taken over` line printed.
