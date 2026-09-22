# TOOL-aWokenSentinel-4 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-4

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite, per the build README's rule three. The pass verified with the direct checks the spec's
section 6 names: each arm block of `tools/unattended/stall-recorder.test.sh` run ALONE over the
suite's sourced prologue, from a runner assembled under the session scratchpad with `HERE` pointed
at the kit under test and the real-driver arm's `git init` fixture under `%TEMP%/sr-fx`; the new
arm of `tools/unattended/adopt-unattended.test.sh` run alone the same way on a fixture seeded and
adopted under `%TEMP%/sr-ad`; the merger, the adopter's `--check`, `check-hook-destinations.sh`,
`gen_map.py --check`, `lexicon.py` and `check-install-prefix.sh` each run ONCE as the checker the
criterion names, never as the bar. Those stand in for the `unattended skill wiring`, `hook
destinations`, `install-prefix`, `codebase-map coverage + freshness`, `lexicon naming predicates`,
`govkit selfcheck`, `unattended kit gate`, `memory hygiene` and `spec tokens` legs, which run once
at the close.

**Evidences:** TOOL-aWokenSentinel-4
- AC1 — the AC1 block alone printed `pass=5 fail=0`: the record at `BUILDING` with `session: absent` and a payload carrying `error` `rate_limit` read `rc=0`, empty stdout, no `stall.fx.log`; a payload whose `session_id` is the literal `absent` read the same. The same block with the prologue's `cp` pointed at an absent hook file printed `pass=4 fail=1`, the failure reading `AC1 unbound rc: expected [0], got [1]` — RED before the hook file exists. OBSERVED.
- AC2 — the AC2 block alone printed `pass=7 fail=0`: `rc=0`, empty stdout, one sidecar line, second field the session, third field `rate_limit`, the tail from the fourth field on parsed by python deep-equal to the payload fed, the first field matching `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`. OBSERVED.
- AC3 — the AC3 block alone printed `pass=6 fail=0`: no `error` key, `error` as an object `{"type":"rate_limit","retry":3}`, and `error` as `""` each read a third field of `unknown`, the object riding the payload deep-equal, three lines after the three feeds. OBSERVED.
- AC4 — the AC4 block alone printed `pass=2 fail=0`: `error` `server error 500` read a third field of `server-error-500` and the tail parsed deep-equal to the payload. OBSERVED.
- AC5 — the AC5 block alone printed `pass=5 fail=0`: `printf 'not json' | node "$HOOK"` read `rc=0`, empty stdout, no sidecar; a JSON payload with no `session_id` read the same. OBSERVED.
- AC6 — the AC6 block alone printed `pass=6 fail=0`: two payloads appended two lines with the first byte-identical to its earlier read and the second's class `overloaded`; a fixture whose `.git` is a file holding `gitdir: <path>` landed the line under `<path>/unattended/` and `find` over the fixture printed one `stall.fx.log`. OBSERVED.
- AC7 — `python tools/settings-merge.py --fragment tools/unattended/stall-recorder.fragment.json` printed `settings-merge: wired stall-recorder * hook into .claude/settings.json`; `python -c` over the file printed one `StopFailure` group, matcher `*`, one command `node "${CLAUDE_PROJECT_DIR}/tools/unattended/stall-recorder.js"`; a second run left `git hash-object .claude/settings.json` unchanged. OBSERVED.
- AC8 — `bash tools/unattended/adopt-unattended.sh --check` printed `unattended: hooks: 3 fragment(s) wired` and `unattended: in sync`, `rc=0`; with the `StopFailure` group deleted from a copy under the scratchpad declared through `GOV_SETTINGS_JSON` it printed `unattended: the stall-recorder hook is UNWIRED — … carries no StopFailure entry under matcher * naming stall-recorder.js`, `rc=1`. The new adopter-suite arm alone, on a seeded and adopted fixture, printed `ARM_DONE n=5 st=0`; the same arm with `HERE` pointed at a kit copy lacking `stall-recorder.fragment.json` printed `st=1`, both `hit` lines missing — the break the spec names. OBSERVED.
- AC9 — with the new files staged, `bash tools/check-hook-destinations.sh` printed `hook-dest: 10 fragment(s) against 253 declared destination(s)` and `hook-dest: clean — every declared hook path resolves`, `rc=0`, one fragment over the `9 fragment(s)` the same checker printed before the fragment was staged; with `hook_path` pointed at `stall-recorder-absent.js` first it printed `FAIL tools/unattended/stall-recorder.fragment.json declares hook_path … which NO kit.toml rule ships`, `rc=1`. OBSERVED.
- AC10 — the AC10 block alone, on a `git init` fixture seeded by the adopter suite's `seed()` under `%TEMP%/sr-fx`, printed `pass=6 fail=0`: the copied driver's `--liveness fx` read `last-stall: none` before the payload; after one `rate_limit` payload, `rc=0` with empty stdout, the `last-stall:` line equalled `tail -n 1` of the fixture's `.git/unattended/stall.fx.log` and carried `rate_limit {"session_id"`. OBSERVED.
- AC11 — `python tools/codebase-map/gen_map.py --check` printed `STALE: … memory/map/generated/symbols.json` and `rc=1` with the new file present; after `--write` it printed nothing and `rc=0`, the delta being `extractErrorClass` and `main` under `tools/unattended/stall-recorder.js`. OBSERVED.
- AC12 — `python tools/lexicon/lexicon.py` printed `js.function.conv 0 of 145 against camel — violation 0` and `rc=0`; its first run read `verb offenders 984 over pin 983` with the one new offender `compare_payload` in the suite, renamed `check_payload` on the lexicon's own `--suggest`. `bash tools/check-install-prefix.sh` printed `carried-prefix clean — 138 recorded file(s), 40 hand-justified, none rising`, `rc=0`, after `tools/run-gates/selftest-budgets.txt` rose 16 to 17 by hand and the suite's own row landed; its first run read `ROSE tools/run-gates/selftest-budgets.txt 16 -> 17` and `UNRECORDED tools/unattended/stall-recorder.test.sh 1`. OBSERVED.
- AC13 — `grep -c 'stall-recorder.test.sh' tools/unattended/kit.toml` printed `1`; the suite's own S4/AC13 block printed `0` for it before the descriptor row landed and `1` after. OBSERVED.

## What this ledger does not evidence

No kit gate, hygiene leg, spec-token leg, lexicon leg as a leg, install-prefix leg as a leg,
hook-destinations leg as a leg, map leg or `*.test.sh` suite ran whole inside this pass; every one
is `--close`'s. The suite's `FLOOR_ASSERTIONS` is pinned at 40 from 45 executed across the ten
blocks run alone (5 7 6 2 5 6 4 3 6 plus the `run_hook` guard's one), which the whole suite
observes at the close and this pass did not. The budget row is sized from 16 s of wall across
those ten runs, each paying the prologue, x1.5 floored at 60. The `error` field stays UNVERIFIED
on this fleet (spec §3): every arm FEEDS the payload it asserts on, and the first stall the wired
hook records is the measurement. The `--dispatch` for this pass omitted `memory/LIVE.md` and
`memory/ledger/2026-09.md`, which the brief says to declare: the verb refused the first
declaration because unit 16's row on `memory/LIVE.md` is still open — the generated index did not
move on that unit's commit and a row on it never closes (`memory/gotchas/`, the dispatch class) —
and this pass writes neither, as no unit commit of this build has.
