# Acceptance ledger — TOOL-aGraftedHelix-10

**Serves:** journal TOOL-aGraftedHelix-10

Node `a`, 2026-10-05. The build commit is `d72502d0`, over the spec's rev-3 commit `cf5272c4`. No merge
bar and no self-test suite ran in this pass. The driver criteria were observed by the suite's new
hooked claim block run ALONE behind the suite's prologue and the claim block's `gh_` helpers, as a
slice under `tools/unattended/` with its fixtures under `%TEMP%`: 46 assertions against the
prologue's 20, green. Each arm was observed RED first against a real break: three driver copies
(the push target set back to `CR_URL`, the refusal file's removal deleted, the `set-head` remedy
deleted), one fixture break (`origin/HEAD` deleted instead of recorded), and a fourth driver copy
whose holder never pushes, which reds the journal arm the closing checklist pass tightened. The
breaks were copies, deleted after each run. The whole suite is the main loop's at VERIFYING.

The hook's branch on the REAL hook set, `gate-env.sh` and the straggler guard included, was measured
once outside the driver: a `git clone` of this repository at `77f61756` with `.githooks` wired, its
bare remote beside it, `GOV_DEFAULT_BRANCH` unset, running the invocation §4 states. By name with
`origin/HEAD` recorded it landed `[new reference]` at rc 0 with no refusal file and the journal's END
line reading `decision=skip-nondefault`; by URL, and by name with `origin/HEAD` deleted, it exited 1
and the hook wrote `default-branch`. That is a second implementation of the push, so it evidences
the hook and not the driver.

**Evidences:** TOOL-aGraftedHelix-10
- AC1 — `skip-nondefault` — in the hooked fixture `--preflight tFresh --keepalive-id k1` exited 0
  printing `preflight OK`, `git ls-remote` listed `refs/gov/runs/tFresh`, no `pre-push-refusal`
  existed, and the journal's newest line named `decision=skip-nondefault`. Red under the URL-target
  break: check 91, the hook's `default-branch` refusal file, no claim on the remote.
- AC2 — `beat-utc` — with the claim reseeded under the holder's own fields and a beat a third of
  `RESUME_STALE_BOUND` old, the hooked `--resume tFresh --keepalive-id k1` exited 0, the claim's
  `beat-utc` moved, no refusal file existed, and the journal, cleared first, named
  `skip-nondefault`. Red under the URL-target break and under the never-pushing holder break.
- AC3 — `UNATTENDED check 91 FAILED` — after `git remote set-head origin -d`, `--preflight tFresh`
  exited non-zero with check 91 and not check 90, its message naming
  `the pre-push hook refused it: default-branch` and `git remote set-head origin -a`, with no claim
  on the remote and no run-state file. Red under the break that deleted the composed remedy line.
- AC4 — `bash tools/check-kit-versions.sh` — at the build commit it printed clean over its 16
  declared carriers under `tools/`, and `python tools/govkit/govkit.py epoch --base cf5272c41`
  printed `epoch: unattended · clean · 1.62` and named no carrier left behind.
- AC5 — `UNATTENDED check 91 FAILED` — with `gate-red` seeded in the fixture's `pre-push-refusal`
  and a `git` shim exiting 128 on the claim push, `--preflight tFresh` reported check 91 with
  `git push exited 128`, named neither `gate-red` nor `set-head`, left no refusal file and no
  run-state file. Red under the break that deleted the refusal file's removal: `gate-red` cited and
  the file kept.
- AC6 — `skip-nondefault` — `grep -n -B20 '^write_claim()' tools/unattended/unattended.sh` at the
  build commit matched `skip-nondefault`, `/HEAD` and `GOV_BRANCH_GATE_CMD` in the header comment;
  the same grep over the parent's driver matched none of the three.
- AC7 — `fixture-lacks-a-gate-the-consumer-has` — `gotchas.py --for-paths` over
  `tools/unattended/unattended.sh` and `tools/unattended/unattended.test.sh` at the build commit
  listed it, the record now carrying both paths as backticked anchors; the pinned 2026-10-04 measurement at
  `14e5f265` selected 23 classes without it.
