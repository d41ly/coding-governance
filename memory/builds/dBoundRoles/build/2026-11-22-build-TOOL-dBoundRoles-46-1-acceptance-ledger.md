**Serves:** journal TOOL-dBoundRoles-46

# TOOL-dBoundRoles-46 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `faad60aef`: a scratch adopter under the host temp folder, short-pathed,
holding a `.git` folder, a `.claude/roles.json` whose `gov-researcher` row carries the `role-sha`
`roles_lib.derive_section_sha` gives its `## Role` section, and prompt files under `memory/builds/bx/prompts/`, each
a `## Task` section whose `### input:question` block opens with its fact line, its marker's task-sha recomputed over
the hand-edited section by `roles_lib.derive_section_sha`. Each payload was piped to a copy of the hook beside a copy
of `tools/hooks/scratch-guard.js`, and the same cases to the hook at base, `git show HEAD:tools/hooks/agent-cap.js`.
The suite's own `write_handoff` fixture was then cut out of `tools/hooks/agent-cap.test.sh`, run to a second scratch
adopter and its variants piped through both hooks. No gate, suite or bar ran in the pass: the `New arm:` rows the
spec declares, their RED-first observation, and the legs its gate line lists are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-46
- AC1 — `node tools/hooks/agent-cap.js` — a fact line, a whole `gov:handoff` marker line and a `Framed by:` line in the question block, each fenced and the fact line unfenced too, each exited 2 naming `input:question` and the line of the file, as `input:question: line 21 of the file reads "<!-- gov:fact key=cmd:printf@0123456789ab class=claimed -->", an executor line inside a typed block`; the plain value, fenced and unfenced, exited 0 with an empty stderr, and a fact line inside an `input:spec` block was not read by the step. The hook at base exited 0 on every case. The `tfact`, `tmark` and `tframed` variants of `write_handoff` exited 2 naming lines 21, 20 and 20 of the file and `tplain` 0, where the base hook admitted all four; the `ok`, `fact` and `fenced` variants kept exit 0 and `open` its refusal. The step is `tools/hooks/agent-cap.js#checkTypedBlocks`, called from `#checkHandoffSpawn`. OWED: the `rule6 BR46 AC1` rows of `tools/hooks/agent-cap.test.sh`, RED first against a `checkHandoffSpawn` with its typed-block step cut out, and the `agent-cap self-test` leg at the close.
- AC2 — `node tools/hooks/agent-cap.js` — a question block holding a four-backtick line nothing in it closes, a closing four-backtick line in the next block, exited 2 naming `input:question: the block leaves a fence opened at line 19 of the file unclosed`, where the base hook admitted it, since the walk of the whole section ends outside every fence; the `topen` variant of `write_handoff` gave the same answer. OWED: the `rule6 BR46 AC2` row at the close, RED first with the typed-block step cut out.
- AC3 — `TYPED_INPUTS` — `node -e` printing the sorted export of `tools/hooks/agent-cap.js` printed `diff question`, and `python -c` printing the names in `handoff.INPUT_NAMES` not in `handoff.PATH_INPUTS` from `tools/roles/` printed `diff question` (DERIVED); the suite's AC3 lines, run alone in a shell over the same two readers, printed both sets equal. OWED: the `rule6 BR46 AC3` row at the close, RED first against a `TYPED_INPUTS` missing a name.
- AC4 — `grep -n 'typed input' tools/hooks/README.md` — printed the rule-6 section's sentence, `A typed input's block is authored text (TOOL-dBoundRoles-46): in a ### input:<name> block whose name`, the sentence naming the fact, marker or `Framed by:` line and the fence left open as denials.
