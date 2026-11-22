**Serves:** journal TOOL-dBoundRoles-13

# Build brief — TOOL-dBoundRoles-13

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  10. Built and CLOSED so far: TOOL-dBoundRoles-14 at `7a58950fb`, TOOL-dBoundRoles-2 at `8795c820a` and
  TOOL-dBoundRoles-1 at `3b479f2fe`, TOOL-dBoundRoles-37 at `5f7f208fd`, TOOL-dBoundRoles-21 at `4c2cf2a3d`,
  TOOL-dBoundRoles-22 at `8463d5212` (ordered `[[workflow.stages]]` rows, `derive_stage_map`, `read_agent_limit`) and
  TOOL-dBoundRoles-49 at `fa3e705e1` (`derive_seed_expected` and the S3 overlay check in `tools/govkit/selftest.py`) and
  TOOL-dBoundRoles-54 at `ff44a3ec1` (`load_kit_roster`, `derive_overlay_expected`, `derive_overlay_drift`, the two-way
  overlay checks), TOOL-dBoundRoles-55 at `5e3109bd2` (the empty-roster refusal) and TOOL-dBoundRoles-16 at `901778344`
  (the five `[[kind]]` rows, each entry's `kind`, `checklist` and `orientation`, every role's `shapes`, the factories)
  TOOL-dBoundRoles-15 at `3a53454b3` (each role's `budget`, `render_static_block`, R5 over the whole block) and
  TOOL-dBoundRoles-17 at `af9af7ba5` (`MARKER_RE` with named groups and `item=`, R16, `--item`, the work-order legacy home)
  and TOOL-dBoundRoles-6 at `9e14a5ca4` (`render_role_section` and the work-order helpers in `roles_lib`, `role-sha` in the
  index and compared at spawn, rendered paths guarded): the `role` and `field` tag namespaces, every role
  file's `never:`, `return:`, `layer:` and `acts-as:`, the merged `gov-reviewer`, the four new roles and the roster by
  layer. Build on those as they stand.
- Every roster spec was re-grounded on HEAD before this dispatch, so its citations hold at HEAD or name the earlier
  unit that changes them. Still verify each claim the spec makes about current code against source before your first
  write, and hand a claim that no longer holds back as a divergence rather than building around it.
- This is the third dispatch. The second builder (run `wf_e5e7a4cb-5ca`) found two more items, decided in
  `build/2026-11-22-build-TOOL-dBoundRoles-13-2-main-loop-decision.md`: `facts` is required only where `roles.builder`
  travels, and `memory/guides/UNATTENDED-VERBS.md` changes with its template in your commit. Build both decision
  records' items and record all of them in the one deviation record.
- Earlier: this was the second dispatch. The first builder (run `wf_44b97275-54b`) stopped on rev-6; the main loop decided its six
  items in `build/2026-11-22-build-TOOL-dBoundRoles-13-1-main-loop-decision.md`. Build them as stated there and record
  items 1 to 5 in the one deviation record below. The spec stays at rev-6.
- Generated outputs are admitted undeclared and belong in the pass commit: `.claude/roles.json`, `.claude/agents/` and
  the rendered `.claude/skills/*/SKILL.md` as their renderers write them, every file `gen_build_index.py --write`
  rewrites, the dClosedLoop as-built view and the map generator's output. `memory/DECISIONS.md` is a shared record a
  pass commit may not write: put the decision row's text in your return and the main loop commits it after the merge.
- The write set also names `help/roles.md`, `help/agent-limit.md` and the deviation record
  `build/2026-11-22-build-TOOL-dBoundRoles-13-deviation-132.md`. If the docs rule owes a page or README the spec does
  not name, or a spec claim no longer holds at HEAD and the fix is mechanical, make the change and record it in that
  ONE deviation record (values `report` and `author-recorded`). Hand back as a divergence only a design choice the
  spec leaves open; any other path outside the set: name it in your return and do not write it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-13`, its final trailer block carrying `Pass: TOOL-dBoundRoles-13` beside
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage explicit
  paths only, never `git add -A`.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-13-1-acceptance-ledger.md` in the
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
