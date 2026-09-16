# TOOL-aProbedUnit-5 — acceptance ledger

**Serves:** journal TOOL-aProbedUnit-5

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite whole, per the build README's rule five. Each pass half was observed one hook invocation at a
time, the body of `run()` lifted out of the suite into a scratchpad probe: the payload built by the
suite's own Python one-liner, piped under the fixture environment (`HOME=/c/Users/fixtureuser`,
`USERPROFILE`, `TEMP` and `TMP` at the fixture values, `TMPDIR` empty) into
`node -e "<prelude>;spawnSync(process.execPath,[hook],{stdio:'inherit'})"`, the hook as node's child,
with the exit read and stderr kept. The RED-first half is the same invocation against
`git show HEAD:tools/hooks/scratch-guard.js` saved in the scratchpad, HEAD being 5049e2ab on the
base 1b000d1a hook, which exits 0 on every denial below. The suite's new block was then run alone —
its preamble through `run()`, `HOOK` overridden, the block's 26 assertions plus the drive-root and
re-targeted arms it touches, 32 in all — against the tip and against that base copy: tip 32 passed,
0 `FAIL`; base 18 `FAIL`, one per denial arm and per sentence assertion, and every control green.

**Evidences:** TOOL-aProbedUnit-5
- AC1 — `cp x $TMPDIR/y` with `TMPDIR` empty — OBSERVED: tip exit 2, stderr `$TMPDIR is EMPTY in this session, so the write lands at the filesystem root`, `grep -c TMPDIR` printed `2`; base exit 0. With the prelude `process.env.TMPDIR="C:/Users/FIXTUR~1/AppData/Local/Temp"`: tip exit 0.
- AC2 — `echo x > ${TEMP}/y` with the prelude `delete process.env.TEMP` — OBSERVED: tip exit 2, stderr `$TEMP is EMPTY`; base exit 0. `echo x > $TEMP/a.log` with the fixture `TEMP` and no prelude: tip exit 0.
- AC3 — `echo x > /tmp/hyg` — OBSERVED: tip exit 2 carrying `/tmp is not a sanctioned destination on this machine: the session scratchpad and the temp root are the two that are`; base exit 0. `echo x > /tmpx/hyg`: tip exit 2, `grep -c POSIX_ROOT_CONVENTIONAL` printed `1` and `grep -c '/tmp is not a sanctioned destination'` printed `0`; base exit 0, measured this pass against the base copy since rev-2 added the shape after the spec-brief measurement.
- AC4 — `mkdir -p /mir/x` — OBSERVED: tip exit 2, `grep -c POSIX_ROOT_CONVENTIONAL` printed `1`; base exit 0. `echo x > /dev/null`, `echo x > /c/projects/x` and `mkdir -p /usr/local/x`: tip exit 0 each.
- AC5 — `TMP=$(mktemp -d); echo x > $TMP/f` with the prelude `delete process.env.TMP` — OBSERVED: tip exit 0; base exit 0. A control, as the spec says.
- AC6 — `echo x > /tmp/claude/x` under the fixture environment — OBSERVED: tip exit 2 with the `tmp` sentence; base exit 0.
- AC7 — the liveness probe `node -e 'process.env.TEMP="/tmp";process.env.TMP="/tmp";delete process.env.TMPDIR;console.log(require("os").tmpdir())'` — OBSERVED: printed `/tmp`; the shell-prefix form `TEMP=/tmp TMP=/tmp TMPDIR= node -e '…'` printed `C:\Users\DAILY-~1\AppData\Local\Temp`, the staged red. Under that prelude `echo x > /tmp/claude/x`: tip exit 0; `echo x > /tmp/other`: tip exit 2 with the `tmp` sentence and `grep -c '^  /tmp$'` over the roots list printed `0`; base exit 0, measured this pass, with `/tmp` listed first among its roots. The emptied prelude derived `C:\Windows\temp`, so on this node the derived arm is the control its label names: `echo x > C:\Windows\temp/claude/x` under that prelude exited 0.
- AC8 — `echo x > ${TMPDIR:-/tmp}/y` with `TMPDIR` empty — OBSERVED: tip exit 2 with the `tmp` sentence; base exit 0.
- AC9 — the AC1, AC3 and AC4 deny stderr — OBSERVED: each carries `BLOCKED by scratch-guard`, quotes its target (`$TMPDIR/y`, `/tmp/hyg`, `/mir/x`) and lists `c:/users/fixtur~1/appdata/local/temp` among the roots; the suite's three new message `case` arms assert the same and were green at the tip, red at base.
- AC10 — the suite whole and its `PASS` line — observed at --close. The pass half: `FLOOR_ASSERTIONS` moved from 60 to 87, the 27 assertions added (26 in the new block, counted line by line, plus one from re-targeting `near-miss: /tmp is a real root -> allow` into a deny and a fixture-TEMP near-miss); the two `/tmp/inv/` source arms now write to `memory/inv/` and exited 0 against the tip. The `figure:` derivation from the suite's own `---- N passed` line at base and tip is the close's, since it needs the suite whole.
- AC11 — `grep -c 'scratch-guard' tools/hooks/README.md` — OBSERVED: printed `2` at the tip and `0` over `git show HEAD:tools/hooks/README.md`; the section names the five rules and the four things the predicate does not catch.
- AC12 — `python tools/codebase-map/gen_map.py --write` — OBSERVED: `symbols.json` gained exactly `checkEmptyTempVar`, `checkPosixRootLitter` and `checkTmpRoot`, 15 inserted lines; `inventories.json` and `MAP.md` re-rendered byte-identical. The `--check` leg and its reverted-artifact red — observed at --close.

## What this ledger does not evidence

No merge-bar leg, map leg, lexicon leg, hook-destinations leg, hygiene leg, spec-tokens leg or the
`scratch-guard self-test` suite ran inside this pass; every one of those is `--close`'s and each row
above says so. The existing arms of the suite were not re-run as a set: the `run()` change they all
pass through was exercised by the 32-arm block, and the controls the new rules could flip
(`~/.litter`, `mkdir -p /c/gvi`, `/c/Windows/Temp/f.txt`, `export TMPDIR=<fixture TEMP>/gatetmp`,
`cp ~/.merge-bar.log memory/inv/`) were probed one at a time against the tip and held.

The `--dispatch` declaration was refused once: `memory/LIVE.md` collided with unit 4's still-open
per-path row for that file, open because no build commit of this run has ever moved the generated
build-level index (it holds one `SPECCED` row per build, which the close flips). The declaration
was re-made without `memory/LIVE.md` and `memory/ledger/2026-09.md`, which the brief asked for and
which this commit does not touch either, and was accepted. The spec is unchanged at rev-3; nothing
diverged.

No temporary file left the session scratchpad: the base hook copy, the probe, the extracted arm
block and the README section draft sit under it, and the suite's own `mktemp -d` was pointed there
through `TMPDIR` for the arm runs. No clone was needed.
