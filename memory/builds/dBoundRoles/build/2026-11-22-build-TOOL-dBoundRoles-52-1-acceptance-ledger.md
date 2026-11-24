**Serves:** journal TOOL-dBoundRoles-52

# TOOL-dBoundRoles-52 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit, on the worktree before the pass commit at base
`54b98253e`. Unit 47's pass already landed the render pair on `gov-orienter` as arm 42 of
`tools/roles/adopt-roles.test.sh` (`5b02247d4`), typed `--input question=` beside handed `--input prompt=`, and its
spec at rev-3 already restates S1, AC1, AC2 and its `New arm:` line for that pair with a revision-log line naming this
unit, so this pass edits no line of the suite and no line of unit 47's spec (S3, F4). The render probes ran
`tools/roles/handoff.py render` in a git fixture repository under the host temp folder, short-pathed, holding a copy
of this tree's roles, loop and playbook-register files with the roles kit scaffolded by its adopter (exit 0), the
policy kit absent, and a build folder `tFix` whose scratch spec's prose, outside any fence, quotes the backticked
`record:TOOL-tFix-9@000000000000`: the commands arm 42 runs, typed by hand. No gate, suite or bar ran in the pass:
arm 42's assertions, the RED-first observation of the `New arm:` line on its staged break, and the legs the spec's
gate line lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-52
- AC1 — `--role gov-orienter` — `render --role gov-orienter --build tFix --unit TOOL-tFix-1 --input prompt=memory/builds/tFix/spec/2026-11-23-spec-TOOL-tFix-1.md` with a question holding the backticked `record:TOOL-tFix-9@000000000000` exited 1, its stderr naming that span once, as resolving to no fact this work order hands, and the prompts folder held no file; with the question in plain words it exited 0 and wrote `2026-11-23-prompt-TOOL-tFix-1-1-orienter.md`. Neither render refused an input at argument parsing: `tools/roles/agents/gov-orienter.agent.md@f79d225b:11` reads `field.input.question, field.input.prompt?`. OWED: arm 42's assertions at the close.
- AC2 — `gov-orienter` — before any edit of the case, the plain-words render `handoff.py render --role gov-orienter --build tFix --unit TOOL-tFix-1 --input prompt=memory/builds/tFix/spec/2026-11-23-spec-TOOL-tFix-1.md --input 'question=which seam fits'` ran on the tree unit 47 left, exited 0 and wrote `memory/builds/tFix/prompts/2026-11-23-prompt-TOOL-tFix-1-1-orienter.md` in the fixture; the pair is seen accepted, and the case needed no re-roling.
- AC3 — `--role gov-builder` — AMENDED by `TOOL-dBoundRoles-60`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-60-deviation-604.md`: unit 47's revision log names `S1`, `AC1`, `AC2` and `TOOL-dBoundRoles-52`, its AC1 and AC2 name `gov-orienter` and `input:prompt`, and the case commented `TOOL-dBoundRoles-47` renders `--role gov-orienter` (`TOOL-dBoundRoles-60` S25). As this unit's pass read it: `grep -n -- '--role gov-builder' tools/roles/adopt-roles.test.sh` prints only lines of arm 35 and arm 40 (`tools/roles/adopt-roles.test.sh@07d196eb:1968` to `tools/roles/adopt-roles.test.sh@07d196eb:2283`), none in arm 42, the case whose comment names `TOOL-dBoundRoles-47` (`tools/roles/adopt-roles.test.sh@07d196eb:2348`); unit 47's spec `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-47.md` carries, at rev-3, a revision-log line naming `TOOL-dBoundRoles-52` S1 for the move to `gov-orienter`. No line of the case or of that spec was edited by this pass.

**Found at HEAD, not acted on:** the spec's Evidence bullet counts five readers of `input:question` (pin: `c93f676e2`).
At `54b98253e` the grep it names returns eight (DERIVED: `grep -c 'field.input.question' tools/roles/agents/*.agent.md`).
The new readers are `gov-architect`, `gov-planner` and `gov-prompt-writer`, and `gov-architect` reads `input:spec`
beside it. The choice of `gov-orienter` stands as F3 resolved it, since the case is already landed there and the
specs consuming it name that role; the stale count is the spec writer's to correct.
