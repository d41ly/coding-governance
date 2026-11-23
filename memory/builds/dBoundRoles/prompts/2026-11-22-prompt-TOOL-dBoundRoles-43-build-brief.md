**Serves:** journal TOOL-dBoundRoles-43

# Build brief — TOOL-dBoundRoles-43

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  28. Built and CLOSED so far: TOOL-dBoundRoles-14 at `7a58950fb`, TOOL-dBoundRoles-2 at `8795c820a` and
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
  fill, `checkFraming` last in rule 6) and TOOL-dBoundRoles-23 at `401c3127a` (`FRAME_SLOTS`, `derive_frame` sorting
  the `reads` fill as `(slot, text, handed)` tuples, `FRAME_LIST_BOUND`, `### row contract`, the return's list bounds
  read back by `read_return_bounds`, `EFFORT_FLOOR` and `check_effort_floor`) and TOOL-dBoundRoles-24 at
  `712869d7d` (`ANCHOR_RE` and `check_anchors` in `roles_lib`, called in `render_handoff` over the composed task
  section after `check_block_fences`, `handed` the keys of the fact blocks the render placed) and TOOL-dBoundRoles-41
  at `cf8515f98` (the graded text: each `reads` tuple carries a fourth item, its graded form, and `check_anchors`
  reads that text while the marker still hashes the full section) and TOOL-dBoundRoles-12 at `66d2468c6` (the
  `check-return-file` verb, `check_scout_return` in the loop kit's `placement.py`, the two placement plants) and
  TOOL-dBoundRoles-11 at `fcc659e0b` (the §8 fork record graded by check 12 and `plan_state`, `resolve_owner_question`
  and the `owner-question` verb, `--dispatch`'s FORKED hold) and TOOL-dBoundRoles-47 at `5b02247d4` (arm 42, the
  cross-unit render pair on `gov-orienter`) and TOOL-dBoundRoles-26 at `0b2d6853c` (the `[return.refusal]` arm
  rendered under every `## Return`, `REFUSAL_ROUTES` and `resolve_refusal_route`, `route-refusal`, `--refused`'s
  `--rule`, `--remedy` and `--actor`, arm 43 with `FLOOR_ASSERTIONS` at 183) and TOOL-dBoundRoles-52 at `c4695a859`
  (no line edited: arm 42 already renders the pair on `gov-orienter`) and TOOL-dBoundRoles-53 at `60b709557`
  (`check_role_reads`, arm 42's read check, control-first order and exit-1 refusal) and TOOL-dBoundRoles-59 at
  `c3425a775` (arm 44 over the tag and native spellings) and TOOL-dBoundRoles-61 at `02eb0e530` (the read check's
  exit branch, arm 45, `FLOOR_ASSERTIONS` at 189) and TOOL-dBoundRoles-18 at `878c60684` (the reviewers' merge step
  `roles/reviewers-to-gov-reviewer` and its `reviewer-merge-` self-test cases) and TOOL-dBoundRoles-82 at `130b9b4bd`
  (`SCALAR_DIRECTIONS`, `rises-only`, `derive_number`, the `rises-` row-kind plants) and TOOL-dBoundRoles-85 at
  `05776c14d` (`ADOPTER_RULE_LEVELS`, a level-5 `adopter-rule` under `block`) and TOOL-dBoundRoles-84 at
  `a448c9048` (`actor` opened on `widens = "changes"`, `changes` in `SCALAR_DIRECTIONS`, `check_actor_patches`
  and its `patch-` plants) and TOOL-dBoundRoles-83 at `24f7be565` (`derive_ref_tag`, `read_leg_names`, the `legs`
  keyword of `check_rows` and `derive_row_composition`, the `exclude-` spelled and leg plants) and TOOL-dBoundRoles-81
  at `b41c49e11` (`check_roles.py --print-rows role|workflow`, `read_roles_rows`, a namespace row's optional `rows`
  reader, the glob source read by `read_source_paths`, the `front-matter-` plants) and TOOL-dBoundRoles-20 at
  `018875f92` (`compose_roles`, `compose_workflows`, the `role-row-schema.toml` and `workflow-schema.toml` kinds,
  `check_core_fields`, `check_actor_patch`, `check_role_acts`, a repository role listed with no agent file) and
  TOOL-dBoundRoles-19 at `bfccd9126` (the house text files moved into the overlay as level-5 units by the
  `roles/house-overlays-to-instructions` step, `render_role` reading them into the marked part) and
  TOOL-dBoundRoles-25 at `00a96bb43` (`tools/hooks/agent-cap.js` and its suite moved into the roles kit as
  `tools/roles/spawn-guard.js` and `tools/roles/spawn-guard.test.sh`, harness admission held to the landed blob,
  the `agent-cap/spawn-guard-to-roles-pack` upgrade step, red-fixed through `69a052808`) and
  TOOL-dBoundRoles-42 at `9cf3482fa` (the retired hook's `memory/` readers classed, the step's spellings waived as
  `widened:` dead-path rows, widen record 8): the `role` and
  `field` tag namespaces, every role
  file's `never:`, `return:`, `layer:` and `acts-as:`, the merged `gov-reviewer`, the four new roles and the roster by
  layer. Build on those as they stand.
- Every roster spec was re-grounded on HEAD before this dispatch, so its citations hold at HEAD or name the earlier
  unit that changes them. Still verify each claim the spec makes about current code against source before your first
  write, and hand a claim that no longer holds back as a divergence rather than building around it.
- The roles, hooks, govkit, playbook and loop kits are shipped kit code: name every new helper with a verb the naming lexicon declares
  (`lexicon.py --suggest <name> --as py.function`), and give every new verb, key or reader its usage anchor on the
  `help/` page the spec names (stamps from `python tools/govkit/docs_leg.py --fingerprints`); a row an anchor drains
  from `memory/project/docs-undocumented.txt` leaves that list in the same commit. If a change moves the charter's
  render, run the playbook kit's `adopt-playbook.sh --target .` and commit `AGENTS.md` and
  `.governance/instructions.lock`. The self-test arm of section 7 runs only as the probe of your own rows, never the
  suite.
- In every record, name a bare line citation in words, never as `path:line`, and never set a number before a counted
  noun (write "the deviation record of this unit"): the positional and pinned-facts checks read both as findings.
  Spell every fixture key from parts. Every scratch tree and staged break runs under `%TEMP%`, never in the tree.
- Generated outputs are admitted undeclared and belong in the pass commit: every file `gen_build_index.py --write`
  rewrites, the dClosedLoop as-built view, the map generator's output and the charter render. If a spec claim no
  longer holds at HEAD and the fix is mechanical, make the change inside the write set and record it in the deviation
  record. Hand back as a divergence only a design choice the spec leaves open; any other path outside the set: name it
  in your return and do not write it.
- Every new Python text read or write, subprocess call included, names `encoding="utf-8"`. No shipped file spells a
  kit path literally: build a path from a variable or from the file's own location. Every code citation in a record
  names its full path. The pass legs red on each of these.
- The main loop decided, in `build/2026-11-23-build-TOOL-dBoundRoles-43-1-main-loop-decision.md`, how this spec's
  retired leg name is read: read it whole before you write; it binds over the spec as the owner's ruling does.
  `agent-cap self-test` reads `spawn-guard self-test` (TOOL-dBoundRoles-25 renamed it in `tools/gate-legs.json`), the
  suite is `tools/roles/spawn-guard.test.sh`, and the spec's two hits for it are waived rows of
  `memory/project/spec-token-waivers.txt` (widen record 9 of this build). Write no spec text but your own spec's
  status cell: a spec's text is `gov-spec-writer`'s. S2's rev bump of TOOL-dBoundRoles-25's spec is owed to a spec
  writer at the close, so answer AC2 AMENDED in your ledger, naming that decision record.
- The main loop red-fixed unit 25's pass legs ahead of you, and three of those fixes sit on your items. Build on
  them and do not undo them:
  - S27: `0b026d5c7` moved the testsuite-count waiver row from `tools/hooks/agent-cap.test.sh` to
    `tools/roles/spawn-guard.test.sh`, because the suite at its new path printed no count. S27's end state removes
    that row once the suite prints `PASS (<n> assertions)` against a pinned `FLOOR_ASSERTIONS`. You may not run
    the suite. Pin the floor only if you can count the executed assertions without running it, and say how in
    the ledger. Otherwise keep the row and give AC27 as owed to the close, which measures the floor at VERIFYING,
    naming TOOL-dBoundRoles-64, the unit the spec's edge hands the pinned floor to.
  - S28: `69a052808` wrote `memory/project/spec-token-waivers.txt` path rows for `tools/hooks/agent-cap.js`
    (count 1) and `tools/hooks/agent-cap.test.sh` (count 2) by hand, disposed `carried:TOOL-dBoundRoles-25`,
    in place of the two retired line-token rows. Re-dispose each through S28's door,
    `python tools/memory-tree/ratchet.py widen spec-token-waivers`, so each row ends `widened:<record stem>`.
    Remove the hand-written row first, because the door adds to the count of a key that already exists. Add the
    `tools/roles/house/gov-diff-reviewer.md` row the same way.
  - `b9a6d5204` and TOOL-dBoundRoles-42 at `9cf3482fa` waive the lines of `tools/govkit/steps/spawn_guard_pack.py`
    and `tools/hooks/kit.toml` that name the retired hook. Those rows sit in `memory/project/dead-path-waivers.txt`,
    keyed by each line's exact text and disposed `widened:2026-11-23-build-TOOL-dBoundRoles-42-widen-8`. If S41
    edits one of those lines, re-key its row to the new text under the same disposition. If S41 adds a line naming
    `agent-cap.js`, give it a row through `ratchet.py widen dead-path-waivers`.
    `bash tools/check-dead-paths.sh --list` must mark every such line waived, with no stale row.
- The spawn-guard suite already reads its kit directory names from where each kit sits: `RKN`, `HKN`, `WKN` and
  `LBW`, since `0bc0ae291`. Its pack-building helper is `build_pack`. Every arm you add follows
  that form, because the install-prefix ban has no waiver.
- Record every change the spec does not state in ONE deviation record,
  `build/2026-11-23-build-TOOL-dBoundRoles-43-deviation-435.md` (values `report` and `author-recorded`); the
  build already holds this unit's deviation records 431 to 434, so check the number is unused first. This unit's
  decision record holds sequence number one, so your acceptance ledger is
  `build/2026-11-22-build-TOOL-dBoundRoles-43-2-acceptance-ledger.md`. The widen door names its own records: it
  wrote widen record 9 for the decision, so yours start at 10; name every stem it mints in your return.
- The policy guard admits a commit touching a guarded path (`tools/policy/guarded-paths.txt`, among them
  `.claude/roles.json`, the rendered agent files and `.governance/` files) only on the live run's branch. If the
  pre-commit hook refuses your pass commit for that reason alone, never route around it: save the whole staged pass
  as a binary patch (`git diff --cached --binary`) and its full commit message under the scratch directory, check the
  patch applies with `git apply --check --index` at your base, and return `committed: false` naming both files and
  the guarded paths. The main loop applies and commits it on the run's branch.
- A new `[[upgrade]]` step id enters `memory/project/landed-steps.txt` in the pass commit if the ratchet asks for it,
  and a plant you add to a kit's self-test moves its row in `tools/run-gates/selftest-budgets.txt`: re-price that
  row's `plants=` token and scale its ceiling by the plant count, as the rows re-priced in this run did.
- `.claude/agents/` and `.claude/roles.json` are renders: rewrite them only with `tools/roles/render_agents.py`; every
  other generated copy the spec names (the charter, the review protocol, the workflow renders, the leg manifest) is
  re-rendered by its own renderer, never edited by hand.
## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-43`, its final trailer block carrying `Pass: TOOL-dBoundRoles-43` beside
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage explicit
  paths only, never `git add -A`.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-43-2-acceptance-ledger.md` in the
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
