# TOOL-aProbedUnit-4 — acceptance ledger

**Serves:** journal TOOL-aProbedUnit-4

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite whole, per the build README's rule five. Each pass half was observed one arm at a time: the
suite's preamble (`sed -n '1,/^# ---- AC2: THE ARGS GUARD/p'`, 105 lines) sourced into a `bash -c`
child whose cwd was `tools/workflows` — `$0` must be the bare `bash`, since this node's tool shell
reports `/usr/bin/bash` and the preamble's `HERE` then resolves to `/usr/bin` and its guard exits 2
— then `run_wf` over the named fixture, once against the landed pair and once against `git show
HEAD:` copies of both scripts in the session scratchpad. Landed: 30 assertions, 0 `FAIL`. Base: the
absent, relative and mismatched fixtures each print `RESULT`, and every positive arm is `FAIL`.

**Evidences:** TOOL-aProbedUnit-4
- AC1 — `run_wf` over `$UNITS` with `"scratch":"/tmp/s",` deleted by `sed`, paired with `returns CONVERGED 0` — OBSERVED: `THROW unattended-build: args must carry an explicit \`scratch\`, an ABSOLUTE path to the session scratchpad`; with `"scratch":"tmp/s"` the same `THROW`; `$UNITS` as landed prints `RESULT`. Against the base script all three print `RESULT`.
- AC2 — the same fixture with `"scratch":"C:\\tmp\\s"` — OBSERVED: the `prompt:spec:tB:g0:` line spells `goes under C:/tmp/s`, the `RESULT` line's `dispatch.args` carries `"scratch":"C:/tmp/s"`, and `hasnt_` finds neither `C:\tmp` on a prompt line nor `C:\\tmp` in the `RESULT`.
- AC3 — `run_wf "$UNITS" "$(returns CONVERGED 0)"` — OBSERVED: `prompt:spec:tB:g0:`, `prompt:spec:tB:g1:` and `prompt:audit:record:r1:` each carry `goes under /tmp/s`, `a bare mktemp, or any OTHER path outside the repository` and `goes under %TEMP%/<short-name>, never inside the worktree`, and none carries `any path outside` or `core.longpaths`; the `NON-CONVERGENT 2` fixture's `prompt:dispose:tB:` line carries the same. `grep -c 'any OTHER path outside the repository'` printed `1` over the template and `1` over the render. The byte parity of the pair is `review-protocol parity (kit vs dogfood)` — observed at --close.
- AC4 — the `RESULT` line of that run — OBSERVED: `"args":{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","mode":"unattended","driver":…,"ground":…` — `scratch` beside the six.
- AC5 — `CHILD_ARGS` pasted as it stood at base, `printf`'d with `unattended`, against `$C` — OBSERVED: `THROW unattended-unit: args must carry an explicit \`scratch\``; with `"scratch":"/tmp/s"` added and `"ground":"G. "` unchanged, `THROW unattended-unit: the \`ground\` text names no \`/tmp/s\``; with `"ground":"G. goes under /tmp/s. "` too, `RESULT` and the trace line `prompt:unit:A-tB-1:G. goes under /tmp/s.  Build exactly ONE…`. `grep -cE '^(async )?function ' tools/workflows/unattended-unit.js` printed `1`. The map leg's count is `codebase-map coverage + freshness` — observed at --close. The three inline fixtures that sit behind the new checks were also run alone: `:118` still prints `carries no \`units\``, and the two `mode` fixtures still print `"atttended"` and `must carry an explicit \`mode\``.
- AC6 — `grep -c scratch` printed `1` over `tools/unattended/SKILL.template.md`, `1` over `.claude/skills/unattended/SKILL.md` (line 579, inside the "Drive the build as ONE program" bullet), `2` over `memory/map/features/review-harnesses.md`, `13` over the template and `13` over the render; `grep -cF 'scratch: "<absolute session scratchpad>"'` printed `1` over the template and `1` over the render. `adopt-unattended.sh --check`, `check-protocol-parity.test.sh` and `check-workflow-syntax.js` are `unattended skill wiring`, `review-protocol parity (kit vs dogfood)` and `workflow script syntax` — observed at --close.
- AC7 — `grep -c scratch tools/workflows/unattended-build.test.sh` printed `42`, at or above the pinned floor of 16 (the 16 fixture lines, matched by the predicate `"repo":"/tmp/r","slug":"tB",` which hit exactly 16 lines at base, plus the arms); the four labels `scratch: the parent REFUSES args with no scratch`, `scratch: the parent REFUSES a relative scratch`, `scratch: a backslash scratch is folded before it reaches a prompt` and `scratch: the child REFUSES a ground that names no scratch` each printed `1`. The whole-suite run and its `--- <n> arms` line — observed at --close.

## What this ledger does not evidence

No merge-bar leg, parity leg, wiring leg, syntax leg, map leg, hygiene leg or harness suite ran
inside this pass; every one of those is `--close`'s and each row above says so. The suite whole is
AC7's close half and it is the run that sees all sixteen fixtures at once; this pass saw only the
fixtures its arms name, plus the three inline ones AC5's row lists, run alone.

The spec moved to rev-4 before code, on the brief's M2 AMEND from unit 3's pass: the rev-3
`core.longpaths=true` clone clause became the ONE exception — a git clone or a fixture repository
goes under `%TEMP%/<short-name>`, never inside the worktree and never at a drive root. AC3's third
token is the exception's bytes and `core.longpaths` joined its must-not list; section 9 carries the
line. F1 stays RESOLVED, its observation unchanged.

No temporary file left the session scratchpad: the base copies, the preamble and the arm script
sit under it, and no clone was needed.
