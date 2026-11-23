**Serves:** journal TOOL-dBoundRoles-23

# Build brief — TOOL-dBoundRoles-23

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  18. Built and CLOSED so far: TOOL-dBoundRoles-14 at `7a58950fb`, TOOL-dBoundRoles-2 at `8795c820a` and
  TOOL-dBoundRoles-1 at `3b479f2fe`, TOOL-dBoundRoles-37 at `5f7f208fd`, TOOL-dBoundRoles-21 at `4c2cf2a3d`,
  TOOL-dBoundRoles-22 at `8463d5212` (ordered `[[workflow.stages]]` rows, `derive_stage_map`, `read_agent_limit`) and
  TOOL-dBoundRoles-49 at `fa3e705e1` (`derive_seed_expected` and the S3 overlay check in `tools/govkit/selftest.py`) and
  TOOL-dBoundRoles-54 at `ff44a3ec1` (`load_kit_roster`, `derive_overlay_expected`, `derive_overlay_drift`, the two-way
  overlay checks), TOOL-dBoundRoles-55 at `5e3109bd2` (the empty-roster refusal) and TOOL-dBoundRoles-16 at `901778344`
  (the five `[[kind]]` rows, each entry's `kind`, `checklist` and `orientation`, every role's `shapes`, the factories)
  TOOL-dBoundRoles-15 at `3a53454b3` (each role's `budget`, `render_static_block`, R5 over the whole block) and
  TOOL-dBoundRoles-17 at `af9af7ba5` (`MARKER_RE` with named groups and `item=`, R16, `--item`, the work-order legacy home)
  and TOOL-dBoundRoles-6 at `9e14a5ca4` (`render_role_section` and the work-order helpers in `roles_lib`, `role-sha` in the
  index and compared at spawn, rendered paths guarded) and TOOL-dBoundRoles-13 at `8013e23ea` (inputs handed as content
  under keyed fact lines, `handoff.py facts`, the spawn guard's fact-key step, the unit harness's `facts`) and
  TOOL-dBoundRoles-3 at `91902c55c` (`render --item`'s five work-order blocks, `derive_allowance`, `WORK_ORDER_KIND`, the
  card binding at spawn, the loop kit's `declaration` verb) and TOOL-dBoundRoles-38 at `20bbcd800` (handed content fenced
  by `render_handed_fence`, the fence walkers `read_unfenced_lines` and `readUnfencedLines`, every marker and fact reader
  fence-aware, an open fence refused), TOOL-dBoundRoles-45 at `19732006a` (a typed `--input` written unfenced under
  `check_authored_lines`) and TOOL-dBoundRoles-46 at `caed55b4d` (`TYPED_INPUTS` and the typed-block check at spawn) and
  TOOL-dBoundRoles-8 at `57054a8d6` (`resolveRoleRoot`'s third start, G2 and G3 bound with no root) and
  TOOL-dBoundRoles-48 at `914fdf91c` (`check_block_fences`, `derive_block_extents`, `checkBlockFences` at spawn) and
  TOOL-dBoundRoles-9 at `72bf05e01` (the index's `classes` map, `checkRoleClass`, `checkWriteClass`, step 6b) and
  TOOL-dBoundRoles-7 at `05a882032` (`checkShellWrites`, `readWorkOrderAllowance`, `checkRoutedEntry`, the widened
  `scanWriteTargets`) and TOOL-dBoundRoles-5 at `627ce8527` (`check_return`, the `check-return` verb and its
  `SubagentStop` fragment, the harnesses' `retries`) and TOOL-dBoundRoles-10 at `e1464fe49` (`checkDriverRead`,
  `resolvePromptsAuthor`, `check_no_spawn`) and TOOL-dBoundRoles-39 at `d2d1db8c5` (the route test first in
  `check-return`, so a harness stage's stop and an unmarked stop pass silent) and TOOL-dBoundRoles-40 at `afb07e98c`
  (`check_stop_replay` in the govkit self-test) and TOOL-dBoundRoles-4 at `5f0e8eaf8` (`render --for` and
  `render_for_work_order`, `--framed-by` and `read_framing`, the four `### framing:` blocks appended to the `reads`
  fill, `checkFraming` last in rule 6): the `role` and
  `field` tag namespaces, every role
  file's `never:`, `return:`, `layer:` and `acts-as:`, the merged `gov-reviewer`, the four new roles and the roster by
  layer. Build on those as they stand.
- Every roster spec was re-grounded on HEAD before this dispatch, so its citations hold at HEAD or name the earlier
  unit that changes them. Still verify each claim the spec makes about current code against source before your first
  write, and hand a claim that no longer holds back as a divergence rather than building around it.
- TOOL-dBoundRoles-4 landed the four `### framing:` blocks (`render_framing_blocks` in `tools/roles/handoff.py`),
  appended after the `reads` blocks of the work-order template's `reads` fill, with `Framed by:` closing
  `### framing:job`; this unit's frame sorts that fill into `FRAME_SLOTS` order. TOOL-dBoundRoles-21 landed
  `read_policy_setting`, `resolve_stage_efforts` and `resolve_effort`, and TOOL-dBoundRoles-3 the work-order blocks.
  Read each at HEAD and build on it; record every citation you re-ground.
- A first builder (run `wf_a398b95f-aed`) diverged and wrote nothing. The main loop settled its items in
  `build/2026-11-23-build-TOOL-dBoundRoles-23-1-main-loop-decision.md`: read it WHOLE before your first write. It
  binds over the spec where they differ: the population comes from `### framing:population` alone (no lister),
  AC1 follows the slot table over a fixture catalogue role reading `upstream:rows?`, S4 reads `--upstream`, and
  `check_return` gains its read of the work order. Build those items as the decision states, and record each in
  the one deviation record below.
- The paths S4 to S6 cite under `tools/loop/`, `tools/policy/`, `tools/workflows/` and `tools/hooks/` are read, not
  written: none is in the write set. If S6's guard needs a change there, hand it back as a divergence.
- Record every change the spec does not state in ONE deviation record,
  `build/2026-11-23-build-TOOL-dBoundRoles-23-deviation-234.md` (values `report` and `author-recorded`).
- Generated outputs are admitted undeclared and belong in the pass commit: `.claude/roles.json`, `.claude/agents/` and
  the rendered `.claude/skills/*/SKILL.md`, every file `gen_build_index.py --write` rewrites, the dClosedLoop as-built
  view, the charter render (`AGENTS.md` and `.governance/instructions.lock`, via the playbook kit's
  `adopt-playbook.sh --target .`, whenever a role's description, purpose or output changes) and the map generator's
  output. If the docs rule owes a page or README the spec does not name, a fixture pins bytes you change, or a spec
  claim no longer holds at HEAD and the fix is mechanical, make the change inside the write set and record it in that
  deviation record. Hand back as a divergence only a design choice the spec leaves open; any other path outside the
  set: name it in your return and do not write it.
- Name every new shell or Python helper with a verb the naming lexicon declares (`lexicon.py --suggest <name> --as
  sh.function`), and every new JavaScript function too (`--as js.function`).
- Every new Python text read or write, subprocess call included, names `encoding="utf-8"`. No shipped file spells a
  kit path literally: build a path from a variable that names a session, transcript or git directory, or from the
  file's own location, never `tools/<kit>/` and never `"<kit>" / "<literal>"`. Every code citation in a record names
  its full path, and every new hook, verb or policy key gets a usage anchor on its `help/` page. The pass legs red on
  each of these.
## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-23`, its final trailer block carrying `Pass: TOOL-dBoundRoles-23` beside
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage explicit
  paths only, never `git add -A`.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-23-1-acceptance-ledger.md` in the
  pass commit: one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- In every record you write, cite code as `path#symbol` or a blob-pinned `path@<blob8>:<line>`, never a bare
  `path:line`, and put a pin (a sha, a `path:line` or `DERIVED`) on any line quoting a count of lines, files or units.
  Never write a section number beside a counted noun (say "the legs section 7 lists"): the pinned-facts check reads it
  as an unpinned count.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list needs its
  own `--dispatch` with `--writes` naming the FULL set before you stage it, unless the call carries `passBase`, in
  which case you record nothing in the run-state file and name the extra path in your return. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`; its values are `report` and `author-recorded`.
