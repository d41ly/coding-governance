**Serves:** journal TOOL-dBoundRoles-58

# TOOL-dBoundRoles-58 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on its worktree
before the pass commit at base `0eb81c875`. The render probes ran `tools/roles/handoff.py render` in git fixture
repositories under the host temp folder, short-pathed, each holding copies of this tree's roles, loop and
playbook-register files with the roles kit scaffolded by its adopter, the policy kit absent and a build folder `tFix`,
with `CLAUDE_CODE_SESSION_ID` unset. The spawn-guard probes ran the suite's own `write_handoff` fixture, cut out of
`tools/roles/spawn-guard.test.sh` to a scratch adopter, and piped each variant to a copy of the pack beside a copy of
`tools/hooks/scratch-guard.js`, and to the pack as it stands at that base. No gate, suite or bar ran in the pass: the
`New arm:` arms the spec declares, their RED-first observations, and the legs its gate line lists are owed to the main
loop at the close. Every spec this unit's items bump is CLOSED, so the restated text is the After field of
`memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-58-deviation-583.md`, and a criterion that greps a
frozen spec is answered AMENDED, by the main loop's decision
`memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-58-1-main-loop-decision.md`.

## Items a landed unit had already left

- S8 and S9: `tools/roles/spawn-guard.js` runs `main()` under `require.main === module` alone and exports
  `TYPED_INPUTS`, as `TOOL-dBoundRoles-25`'s move carried them; the pass added neither.
- S10: `TOOL-dBoundRoles-25`'s ledger inventory already names `TYPED_INPUTS` exported from the pack; this pass adds the
  suite's rows alone.
- S11 and S26: the exemption already read `TYPED_INPUTS`; S16's reader keeps it, on one line of `checkBlockFences`.
- S12: no code; the case is the suite's `BR58 AC12` rows.
- S18: specs 46 and 48 already cite `roles_lib.derive_section_sha` and no case under `tools/` calls the moved function;
  spec 50's AC7 is restated in the record.

## S15 — the consumers of `parse_spec_h1`, each with its leg

| Consumer | Leg |
|---|---|
| `tools/memory-tree/gen_build_index.py#spec_ids` | `build-index selftest` |
| `tools/memory-tree/id_grammar.py#extract_records`, the memory-recall extractor's anchor | `memory-recall kit selftest` |
| `tools/memory-tree/routed_commits.py` | `routed-commits selftest` |
| `tools/memory-tree/deviation_join.py` | none of its own |

## S32 — no inversion

`git log --reverse --format=%s 8b8b1374c..HEAD` at `0eb81c875` prints the pass of `TOOL-dBoundRoles-3` before that of
`TOOL-dBoundRoles-38`, and that of `TOOL-dBoundRoles-39` before that of `TOOL-dBoundRoles-40`. No inversion is found, so
nothing is parked and no row is owed.

**Evidences:** TOOL-dBoundRoles-58
- AC1 — `--role gov-skeptic` — with `--input diff=` carrying the span and `--input spec=` a scratch spec quoting it, the render exited 1, its stderr naming the span once and the anchor check's refusal alone, and wrote no file; with a plain-words diff it exited 0 and wrote its prompt file. OWED: arm 42's `diff` renders of `tools/roles/adopt-roles.test.sh` at the close.
- AC2 — `input:spec` — the case's own functions, cut out of the suite and run over a fixture whose gov-skeptic `reads` drops `field.input.spec?`, printed `gov-skeptic does not read input:spec`, ran neither render and wrote no file. The helper is `check_role_reads`, as `TOOL-dBoundRoles-53` built it. OWED: arm 42's staged case at the close.
- AC3 — `grep -n 'gov-skeptic' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-50.md` — AMENDED by the main loop's decision, item 4: spec 50 is frozen, and the token `gov-skeptic` stands in the deviation record's restated S8 and AC8 of `TOOL-dBoundRoles-50@rev-6`. Observed too: the kits of `fe9b73c83` and `cf8515f98` rendered equal `## Task` bytes and task-sha `677cd673ab94` on that role.
- AC4 — `--role gov-builder --input spec=<scratch spec>` — exited 0 in a fixture holding no brief record, the spec's bytes between two three-backtick lines under its `record:` fact line. OWED: arm 37's control render at the close.
- AC5 — `python -c` — AMENDED by `TOOL-dBoundRoles-60`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-60-deviation-604.md`: the probe folds each `reads` entry through `roles_lib.parse_read_key` and asserts no native `task:` key and no non-optional `brief:` or `card:` key (`TOOL-dBoundRoles-60` S17). As this unit's pass read it: over `roles_lib.load_roles`, gov-builder's `reads` folded through `roles_lib.parse_read_key` read `input:spec`, `card:route` and `brief:non-goals`, the last two optional: no `task:` key and no required `brief:` key.
- AC6 — `grep -n 'gov-builder' memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-45.md` — AMENDED by `TOOL-dBoundRoles-60`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-60-deviation-604.md`: a revision-log line of unit 45 above rev-2 names `AC1` and `TOOL-dBoundRoles-58`, and unit 45's AC1 holds `gov-builder` (`TOOL-dBoundRoles-60` S26). As this unit's pass read it: AMENDED by the main loop's decision, item 4: spec 45 is frozen, and the token `gov-builder` stands in the deviation record's restated AC1 of `TOOL-dBoundRoles-45@rev-5`, a record of `TOOL-dBoundRoles-58`.
- AC7 — `check_block_fences` — a scratch `handoff.py` placing `### framing:job` holding a three-backtick line before the handed blocks and `### framing:added` holding a five-backtick line after them exited 1 naming `### input:spec` and wrote no file; the same copy with `check_block_fences` returning nothing, `check_open_fence` still reading the walk's end, exited 0, so the case reads red against that break. OWED: arm 38's `BR58 AC7` assertions at the close.
- AC8 — `grep -n 'require.main === module' spawn-guard.js` — printed the one entry line, `if (require.main === module) main()`.
- AC9 — `node -e` — requiring `tools/roles/spawn-guard.js` with stdin closed printed `question,diff` from `TYPED_INPUTS` and exited 0.
- AC10 — `node spawn-guard.js` — the `ok` variant exited 0 with an empty stderr and the `two` variant 2, as at base; the `crlf`, `fenced`, `fact`, `s13`, `nounit`, `dash`, `tplain` and `fwrap` variants kept exit 0 and every refusal of `moved`, `open`, `fflip` and `fwrapx` its reason. Unit 25's inventory names `TYPED_INPUTS`. OWED: the `BR58 AC10` rows of `tools/roles/spawn-guard.test.sh` at the close.
- AC11 — `grep -n 'TYPED_INPUTS' spawn-guard.js` — printed, among the set and the typed check, the exemption's line of `tools/roles/spawn-guard.js#checkBlockFences`, `if (TYPED_INPUTS.includes(b.input)) continue`.
- AC12 — `### input:extra` — the `textra` variant exited 2 naming `input:extra` as a handed block whose next line opens no fence, and 0 against a scratch copy whose `TYPED_INPUTS` names `extra`. OWED: the `BR58 AC12` rows at the close.
- AC13 — `git log --reverse --format=%s` — AMENDED by `TOOL-dBoundRoles-58`, deviation record 583: the run's pass subjects read `build(TOOL-dBoundRoles-<n>): `, so the anchored shape is `^build\(TOOL-dBoundRoles-3\): `, which prints unit 3's pass alone and not unit 37's, whose subject `build(dBoundRoles): TOOL-dBoundRoles-37 lifts ...` it cannot match; the shape the criterion spells prints nothing.
- AC14 — `bash tools/check-dead-paths.sh` — the default mode is the dead-path leg, which a role agent may not run, so its verdict is owed at the close. `bash tools/check-dead-paths.sh --list` on the staged tree printed unwaived hits in `.governance/install.json`, `.governance/steps/roles/` and `tools/roles/kit.toml` alone, the inherited reviewer and house rows the close owns; none is in a file this pass touched, and this pass wrote no dead-path row, so no hit and no stale row is this unit's.
- AC15 — `parse_spec_h1` — over unit 56's fixtures, `gen_build_index.spec_ids` and the extractor's `id_grammar.extract_records` anchor each named the id `parse_spec_h1` returned, the live id of each fixture holding one and none from the unclosed fence. OWED: the legs of the S15 table at the close.
- AC16 — `grep -n "startsWith('### ')" spawn-guard.js` — printed the one line inside `readTaskBlocks`; the `tquoted` variant, a handed spec quoting a fenced `### input:question` heading and a `Framed by:` line, exited 0, where the pack at base refused it naming `input:question`. `checkTypedBlocks`, `checkBlockFences` and `checkFraming` all read `readTaskBlocks`. OWED: the `BR58 AC16` row at the close.
- AC17 — `grep -n 'handed' tools/roles/handoff.py` — the flag is set on one line, in `tools/roles/handoff.py#derive_block_extents`. A probe over the builder's item render, the skeptic's, the orienter's and the prompt writer's `--for` render saw `check_block_fences` and `render_graded_section` handed the same list object, and the graded text equal to the base kit's but for the practices block's envelope, whose opener stands in place of its heading; every render's bytes equal the base kit's.
- AC18 — `git grep -n 'handoff.derive_section_sha'` — AMENDED by `TOOL-dBoundRoles-60`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-60-deviation-604.md`: the match is literal and scoped to `tools` and the specs of units 46, 48 and 50 (`TOOL-dBoundRoles-60` S1 to S3). As this unit's pass read it: AMENDED by the main loop's decision, item 4: over `tools` it printed nothing; over the specs it prints frozen lines of specs 6, 50 and 58 and the unbuilt 60 and 63, and the deviation record's restated AC7 of `TOOL-dBoundRoles-50@rev-6` cites `roles_lib.derive_section_sha` as that of 46 and 48 does.
- AC19 — `grep -c '"subagents"' tools/roles/handoff.py` — printed 1 (DERIVED on the staged tree), and the `resolve_subagent_dir` grep over the file printed nothing; `resolve_agent_transcript` with a run id answered the run's folder, the route test's harness folder read `/subagents/workflows`, and an id off its shape answered None.
- AC20 — `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms` — the leg's argv, read from `tools/gate-legs.json`, is the criterion's own and stands in the deviation record's restated AC12 of `TOOL-dBoundRoles-50@rev-6`. A role agent may not run the leg, so its verdict is owed at the close. Both shell files this unit touches are `*.test.sh` suites, which that argv leaves out, so no finding of it is this unit's; the findings `TOOL-dBoundRoles-50`'s ledger names at its base are not.
- AC21 — `--input question=` — AMENDED by `TOOL-dBoundRoles-60`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-60-deviation-604.md`: each shape graded on every line, `### `, a fact line, a marker line and `Framed by:`, is refused after a carriage return, as arm 37 now holds (`TOOL-dBoundRoles-60` S36). As this unit's pass read it: a first line, a newline, a `\r` and a whole `gov:handoff` marker line exited 1 naming `input:question — line 2 reads as a gov:handoff marker line`; the same with a level-three heading refused as one, and a plain value with CRLF endings rendered. OWED: arm 37's CR case at the close.
- AC22 — `# install deps` — inside a closed three-backtick fence the question exited 0; unfenced it exited 1 naming line 2 as a heading, and a fenced level-three heading still refused. OWED: arm 37's comment cases at the close.
- AC23 — `grep -nE '<unit .* acceptance ledger>'` — AMENDED by the main loop's decision, item 4: spec 51 is frozen, and the deviation record's restated AC2, AC5 and AC7 of `TOOL-dBoundRoles-51@rev-3` and AC4, AC20 and AC22 of `TOOL-dBoundRoles-50@rev-6` each grep a unit's own `**Evidences:**` block. A probe cutting each block as S23 states found the searched token in it: `AC8` and `AC9` in 44's, `MERGE-BAR` in 42's, one line naming `AC14` in 25's (DERIVED on the staged tree), and `TOOL-dBoundRoles-43`, `derive_roles_expected` and `refused` in 50's.
- AC24 — `amended rev-<n>` — AMENDED by the main loop's decision, item 3: a `python` probe over this build's acceptance ledgers found no `amended rev-` answer, no line reading `AMENDED, naming`, and every answer naming `TOOL-dBoundRoles-58` citing deviation record 583, which exists and names the answered unit's spec with its revision.
- AC25 — `input:question` — the `tforge` variant, a whole marker line unfenced in the typed question, exited 2 naming `input:question: line 11 of the prompt reads`, where the pack at base refused it by the count. OWED: the `BR58 AC25` row at the close, RED first with the count moved first.
- AC26 — `TYPED_INPUTS` — the criterion's grep over `tools/roles/spawn-guard.js` printed that constant's line alone.
- AC27 — `grep -n 'lone fence run'` — AMENDED by the main loop's decision, item 4: the token `lone fence run` stands in the deviation record's restated §5 of `TOOL-dBoundRoles-45@rev-5`.
- AC28 — `--input question=` — a question holding one line of a three-backtick fence exited 1 naming `a fence opened at line 2 of the value is never closed`. OWED: arm 37's lone-fence case at the close.
- AC29 — `grep -n 'js.file'` — AMENDED by the main loop's decision, item 4: the token is absent from the deviation record, whose restated §4 of `TOOL-dBoundRoles-46@rev-6` names `js.function` and no constant or file cell; `.lexicon.conf` declares `js.function` and `js.type` cells and no file cell for that language.
- AC30 — `grep -n 'ends inside' tools/roles/roles_lib.py` — AMENDED by `TOOL-dBoundRoles-60`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-60-deviation-604.md`: the observation is by behaviour: `roles_lib.check_block_fences` on a section whose walk ends inside a fence yields no line, and a render of it yields exactly one refusal, 38 S5's (`TOOL-dBoundRoles-60` S14 and S15). As this unit's pass read it: printed one line, the refusal of `tools/roles/roles_lib.py#check_open_fence`, 38 S5's; `check_block_fences` over a section ending inside a fence returned no line, and a render of one exited 1 with that one refusal.
- AC31 — `derive_seed_expected` — imported as a library, it and `cmd_plan` both call `derive_seed_writes` and neither's code object holds the role's word; a default target planned as three `write|seed` rows against three derived (DERIVED), and with one seed's destination present as two `write|seed` and one `KEEP|seed` against three (DERIVED). OWED: the `[dBR-58 AC31]` case of `tools/govkit/selftest.py` at the close.
- AC32 — `grep -n 'unattended.sh --park'` — AMENDED by the main loop's decision, item 4: the token stands in the deviation record's restated S1 of `TOOL-dBoundRoles-51@rev-3`; the S32 section above records that no inversion was found.
- AC33 — `grep -n 'typed input' help/roles.md` — printed the renderer step's refusal and the two bullets under "What the hooks refuse"; `docs_leg.py --fingerprints` printed every stamp the page carries unchanged.
- AC34 — `git ls-files '*SKILL.md' '*SKILL.template.md' | xargs grep -nwE 'Grep|Glob'` — the list holds `skills/deploy-governance/SKILL.md`, and a word search for either name over every file of it printed nothing.
- AC35 — `INPUT_NAMES` — with a scratch `handoff.py` adding `extra` to it, the case's functions printed `the typed input extra maps to a role that reads it: no role is mapped` as a failure. OWED: arm 42's staged case at the close.
