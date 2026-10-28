**Serves:** journal TOOL-dSafePassage-58

# TOOL-dSafePassage-58 — acceptance ledger

The unit as built, at spec rev-1. Its write set is `tools/push-main.test.sh` only where AC2 or AC4
finds the arm's skip line or place wrong (§4 Rollout). AC2 found one skip line naming the arm, below
its guard, and AC4 found the arm placed, so the suite is not written. S1, S3 and S6 to S10 are
readings of TOOL-dSafePassage-52 and TOOL-dSafePassage-57, observed below. This pass writes only this
ledger and the spec's status header.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
(Windows, bash under Git for Windows) over this worktree at 2ee9d0d1, by TOOL-dSafePassage-57's §4 arm
probe and this spec's §4 placement probe, each written verbatim to the run's scratchpad with only
`f=${f:-tools/push-main.test.sh}` in place of the fixed `f=`, so a scratch copy is read by setting `f`.
The scratch copies were made from `tools/push-main.test.sh` at 2ee9d0d1 by `sed` and `awk`.

Owed at the close: the `New arm:` line of §7 (tools/push-main.test.sh, covers AC2 AC4), observed RED
on a suite copy with the arm's guard between the `skip — 28-32` echo and its `fi`, and on a copy with
the arm block above the `^_mt_rc=` scan run under `env -u _mt_rc`, and GREEN in gov's own tree, where
the suite prints the derived-count arm's `ok` line and no `skip —` line spelling `derived-count arm`.
The §7 legs `push-main self-test`, `foreign-prefix parity (every self-test at three prefixes)`,
`harness arms (fail branches armed or pinned)`, `kit/dogfood doc parity` and `spec tokens (a spec's
own names resolve)` run at the close's bar. S9 is NOT OBSERVED, as §2 states: the `kit/dogfood doc
parity` leg at the close grades a truncated live copy.

**Evidences:** TOOL-dSafePassage-58
- AC1 — `no arm` — with `f` set to a scratch copy whose line 1406 guard reads `[ -f "$HERE/$_mt_rc/check-arm.py" ]`, the arm probe printed `no arm`, exited 1 and printed no `ok-branch`; over `tools/push-main.test.sh` it printed `ok-branch`.
- AC2 — `1428` — `grep -n 'skip — .*derived-count arm' tools/push-main.test.sh` printed one line, 1428, `skip — 37 no memory-tree kit (check-arms.py) beside this lander, so the derived-count arm did not run`, below the guard at line 1406.
- AC3 — `alone rc=127` — after `export _mt_rc=memory-tree`, the arm probe printed `ok-branch`, `_: line 1: _mt_rc: unbound variable` and `alone rc=127`, with no `after` line.
- AC4 — `placed: scan=1028 fi=1240 arm=1402 final=1592` — the placement probe over `tools/push-main.test.sh` exited 0; over a scratch copy with the guard line moved to line 1240, between the `skip — 28-32` echo and its `fi`, and the count helper's `check-arms.py` path renamed, it printed `misplaced: scan=1028 fi=1241 arm=1240 final=1592` and exited 1.
- AC5 — `no anchor: scan=1028 skip= fi= final=1592` — over a scratch copy whose `skip — 28-32` message reads `skip — 28 to 32`, the placement probe exited 1.
- AC6 — `unbound variable` — `env -u _mt_rc bash <scratch file>` over a file holding `set -u` and `if [ -n "$_mt_rc" ]; then echo ok; fi` printed `<file>: line 2: _mt_rc: unbound variable` and exited 1, not 127.
- AC7 — `6927841f` — from `60d90cb7` to HEAD, one commit carries `Pass: TOOL-dSafePassage-52`, and its `git show --name-only` lists none of `memory/HYGIENE.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/ANNOTATION-STYLE.md` or `memory/TEMPLATE-SPEC.md`: the render was not run, so this is `no edit`, never coverage of S8.
