# TOOL-aLightenedLoop-5 — acceptance ledger

**Serves:** journal TOOL-aLightenedLoop-5

No merge bar, no self-test suite and no gate ran in this pass. The criteria a probe can reach were
observed by two scratch probes of the built hook, neither of them the suite: `probe-l5.sh`, which
copies the hook beside a counting stub driver and stops it over `git init` fixtures under
`%TEMP%/l5p`, and `parity-l5.sh`, which clones this branch to `%TEMP%/l5c`, places the hook at
`846d51d3` beside the built one, plants a `RUN.md` binding one session and stops both hooks against
the real driver. Both clones were removed afterwards. The suite's new arms in
`tools/unattended/stop-guard.test.sh` were written and not run; their RED-first observations and the
suite's executed count against the raised `FLOOR_ASSERTIONS` are the close's.

The owner's parity captures, from `parity-l5.sh` on node `a`: at each phase the base hook, the built
hook's miss and its following hit were each run with the sidecar deleted, and `cmp` over stdout, exit
code, stderr and the sidecar line with `utc` removed printed nothing for every pair. BUILDING read
LIVE, blocked `run-open` at block 1/6 with 440 bytes of stdout; HELD read HELD and LANDED read <!-- PINNED 2026-11-14 -->
TERMINAL, each allowing with empty stdout; every run exited 0. Timings, base then miss then hit:
BUILDING 4126 ms, 3815 ms, 447 ms; HELD 3743 ms, 3690 ms, 417 ms; LANDED 3839 ms, 4120 ms, <!-- PINNED 2026-11-14 -->
538 ms. <!-- PINNED 2026-11-14 -->

One staging choice the close should know: AC4's session move calls `readLiveness` directly through
`node -e` with a second session id against the same lease, because one `RUN.md` names one session
and a second id cannot be bound by it through the hook's own payload path.

**Evidences:** TOOL-aLightenedLoop-5
- AC1 — `parity-l5.sh` — at BUILDING (LIVE), HELD and LANDED (TERMINAL), `cmp` between the base
  hook's run and the built hook's miss, and between the base and the built hook's hit, printed
  nothing over stdout, exit code, stderr and the sidecar line without `utc`; each exited 0.
- AC2 — `parity-l5.sh` — the hit beat the base run at every phase: 447 ms against 4126 ms at <!-- PINNED 2026-11-14 -->
  BUILDING, 417 ms against 3743 ms at HELD, 538 ms against 3839 ms at LANDED, node `a`. <!-- PINNED 2026-11-14 -->
- AC3 — `probe-l5.sh` — two unchanged stops on a `git init` fixture read `count=1`, and
  `liveness.fx.json` held the key, the stub's stdout and a numeric deadline. The suite arm
  `L5-AC3` is the close's to observe, with its RED on `checkSession` calling `runLiveness`.
- AC4 — `probe-l5.sh` — an append to `landed.fx.log`, `git update-ref refs/remotes/origin/main` and
  `git config branch.fx.remote origin` each raised the count by one, and a further unchanged stop
  did not. The full nine-move `L5-AC4` arm and its per-part staged breaks of `deriveLivenessKey`
  are the close's.
- AC5 — `probe-l5.sh` — a stored LIVE with `last-move` 10 and `stale-bound` 5 was not served: the <!-- PINNED 2026-11-14 -->
  second stop read `count=2`; the far `deadline` of AC3 was served. The `L5-AC5` arm with
  `STOP_GUARD_LIVENESS_BOUND_MS` is the close's.
- AC6 — `probe-l5.sh` — a STALE read left only `stop.fx.log` in the sidecar directory, no
  `liveness.fx.json`. The other three unstored shapes run in the `L5-AC6` arm, the close's.
- AC7 — `probe-l5.sh` — a torn `liveness.fx.json` and a directory at that path each produced exit
  0 and a sidecar line reading `verdict` LIVE, with no temp file left behind. The `cmp` against a
  run with no cache is the `L5-AC7` arm, the close's.
- AC8 — `deriveLivenessKey` — over a HEAD-only `.git` nested in a `git init` repository, called
  from inside it through `node -e`, printed `null`. The `L5-AC8` arm is the close's.
- AC9 — `grep -n 'liveness.<slug>.json' tools/unattended/README.md` — printed line 262 and the <!-- PINNED 2026-11-14 -->
  `STOP_GUARD_LIVENESS_CACHE` grep line 265, both inside "The sidecar" (lines 254 to 266); and <!-- PINNED 2026-11-14 -->
  `git diff 846d51d3 -- tools/unattended/gate-guard.js` printed nothing.
- AC10 — `python tools/codebase-map/gen_map.py --check` — the close's to observe; this pass ran
  `--write`, after which `symbols.json` carries `deriveLivenessKey` and `readLiveness`.
- AC11 — `STOP_GUARD_LIVENESS_CACHE` — with it `off`, two stops read `count=2` and left no
  `liveness.fx.json`; a valid entry left by an unset stop was not served with it `off` (`count=4`)
  and `cmp` printed `unchanged` over its bytes; with it `OFF` the entry was served. The `L5-AC11`
  arm is the close's.
- AC12 — `grep -n 'does not reproduce' tools/unattended/stop-guard.js` — printed line 48 and the <!-- PINNED 2026-11-14 -->
  `STOP_GUARD_LIVENESS_CACHE` grep line 50, both above `'use strict'` at line 90; the grep for <!-- PINNED 2026-11-14 -->
  `reads no mtime, transcript or git` printed nothing.
