**Serves:** diff-review TOOL-aIndexedAnchor-1 TOOL-aIndexedAnchor-2
**Caused-by:** TOOL-aIndexedAnchor-1

# Closing diff review, round 1: aIndexedAnchor, another build's backlog row and README are records, not a build commit

Tier-2 · 2026-11-28 · on `branch/serene-gagarin-3be850` · one finder pass (`gov-diff-reviewer`, run `direct/a0354aafb7b97d249`), one skeptic run (`gov-skeptic`, run `direct/a12fa9e8089375809`), then this synthesis (`gov-synthesizer`, run `direct/a31d3587f02302b18`), each spawned directly by the main loop rather than through `tier2-review.js`. The diff spans 26 files, +1211/−39. Every line ref below is pinned to the blob at the reviewed sha `9968d68c`.

**Reviewed range:** `229f1ddefdef614f2f0619eb5354228cf2c7f572...9968d68ca7fb97828c512e62a8c07efb8ef2d9e7`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

The two items are both LOW, and neither is a blocker, a high or a medium. L1 is a guide sentence that this diff made false. L2 is an output line with no full-phrase assertion in its own suite.

## Review shape

The review had 2 raw findings, and the skeptic confirmed both. None was refuted, merged or left unverified, so precision is 1.00. The two findings describe different defects, so they form 2 items. Adjudicated by item and by raw confirmed finding alike, the tally is 0 BLOCKER, 0 HIGH, 0 MEDIUM and 2 LOW. Each finding keeps its finder grade.

The skeptic ran F1 end to end in a scratch repo, with a control commit. F2 was judged from the test source, and its suites were not run. Both items are promoted to TOOL-aIndexedAnchor-3 in this build's backlog, which carries their [left-shift] entry.

## LOW

### L1: §7 of the asks guide gives a reason that this diff made false (F1)

- **What is wrong:** The repoint rule says a repoint of another build's ask must ride a commit whose subject names no unit id. Its reason is that the kit picks a unit's build commit "by a whole-token subject match plus any path outside the build folder". This diff makes `build_commit` drop every `<builds root>/<slug>/BACKLOG.md` and `README.md` from selection. Every ask lives in a build's `BACKLOG.md` (template lines 28, 93 and 131), so a repoint inside a unit's commit no longer makes it that unit's build commit.
- **Where:** `tools/unattended/ASKS.template.md@55cb7bd1:169-172` and its rendered twin `memory/guides/UNATTENDED-ASKS.md@55cb7bd1:169-172`. Both files are the same blob.
- **Evidence:** The skeptic used a scratch repo with `tools/lib/resolve-python.sh` sourced. Commit `ARCH-tS-1 repoint a foreign ask`, touching `memory/builds/tP/BACKLOG.md` and `memory/builds/tS/s.md`, was not selected (rc=1). The control commit, with the same id touching `memory/builds/tP/other.md`, was selected (rc=0).
- **Consequence:** A run following §7 is given a mechanism the kit no longer has.
- **Fix:** Rewrite §7's reason in the template to match the new exclusion, or drop the no-unit-id constraint if nothing else still needs it. Then re-render `memory/guides/UNATTENDED-ASKS.md`.

### L2: brief-recorded's exclusion line is asserted by prefix only, so it can drift from its pass-order twin unseen (F2)

- **What is wrong:** `check-brief-recorded.sh` now prints `<build folder> <every build's BACKLOG.md and README.md>` in its exclusion line. The only suite assertion on that line checks just the prefix `the record surface excluded from build-commit selection was`. The full phrase is asserted only on the pass-order leg (`tools/unattended/check-pass-order.test.sh@bdf586fa:1108`). No parity check ties the two lines together.
- **Where:** The output line is `tools/unattended/check-brief-recorded.sh@79e14383:1022`. The prefix-only assertion is `tools/unattended/check-brief-recorded.test.sh@8573a233:584`. The twin line is `tools/unattended/check-pass-order.sh@0c4644fd:1036`.
- **Consequence:** brief-recorded's line could revert or drift from pass-order's while every suite stays green.
- **Fix:** Make the `has` at `check-brief-recorded.test.sh:584` assert the full phrase `<build folder> <every build's BACKLOG.md and README.md>`.
