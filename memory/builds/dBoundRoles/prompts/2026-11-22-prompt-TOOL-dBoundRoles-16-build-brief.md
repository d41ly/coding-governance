**Serves:** journal TOOL-dBoundRoles-16

# Build brief — TOOL-dBoundRoles-16

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  6. Built and CLOSED so far: TOOL-dBoundRoles-14 at `7a58950fb`, TOOL-dBoundRoles-2 at `8795c820a` and
  TOOL-dBoundRoles-1 at `3b479f2fe`, TOOL-dBoundRoles-37 at `5f7f208fd`, TOOL-dBoundRoles-21 at `4c2cf2a3d`,
  TOOL-dBoundRoles-22 at `8463d5212` (ordered `[[workflow.stages]]` rows, `derive_stage_map`, `read_agent_limit`) and
  TOOL-dBoundRoles-49 at `fa3e705e1` (`derive_seed_expected` and the S3 overlay check in `tools/govkit/selftest.py`): the `role` and `field` tag namespaces, every role
  file's `never:`, `return:`, `layer:` and `acts-as:`, the merged `gov-reviewer`, the four new roles and the roster by
  layer. Build on those as they stand.
- Every roster spec was re-grounded on HEAD before this dispatch, so its citations hold at HEAD or name the earlier
  unit that changes them. Still verify each claim the spec makes about current code against source before your first
  write, and hand a claim that no longer holds back as a divergence rather than building around it.
- This is the fourth dispatch. The third builder (run `wf_e3c2d4a9-882`) found the loop kit's factories writing none
  of the fields S2 and S5 make required; rev-7 resolves it in §8 F8 (the role factory writes `shapes` from its
  workflow entry's `kind`, the workflow factory writes the three fields for a non-empty `--roles`), adds
  `tools/loop/factories.py` to Files touched and the write set, and adds AC8.
- Earlier dispatches, still in force: this is the second dispatch's text. The first builder (run `wf_2669408c-2f0`) stopped before its first write because the
  write set lacked the four `add` change records §8 F7 (a) asks for; it found no spec divergence. The write set now
  names them, `build/2026-11-22-build-TOOL-dBoundRoles-16-change-1.md` to `-change-4.md`, one per new unit row
  (`unit.orient.producer`, `unit.orient.verifier-cold`, `unit.checklist.for-paths`, `unit.checklist.for-diff`), written
  by `tools/memory-tree/build_records.py new change`. A second builder (run `wf_f845c411-bc5`) then stopped on the
  generated outputs. Those are admitted undeclared, and you write and commit them in the pass commit:
  `.claude/roles.json` and `.claude/agents/` as `render_agents.py --write` renders them, every file
  `gen_build_index.py --write` rewrites (this spec's `gen:spec-records` region, the build README, `memory/LIVE.md`,
  `memory/backlog/TOOL.md`, the dClosedLoop as-built view) and the map generator's output. The deviation record
  `build/2026-11-22-build-TOOL-dBoundRoles-16-deviation-163.md` is declared for choice 2 below. Any other path
  outside the declared set: name it in your return and do not write it. Rev-6 keeps `gov-orienter` at `high` (§8 F5, the owner's ruling TOOL-dEasedEffort-1), its deviation in `build/`.
- The main loop decided the first builder's four open choices, as M3 delegated resolutions, `widens: none` and
  `relaxes: none` each; record any of them that the spec does not state as a deviation:
  1. The `experiment` kind row omits `fan` and `cap`, and `derive_stage_rows` takes them from the table's `fan`.
  2. R9 prints one line per role and missing kind, naming every stage the role runs in, so AC4's one line holds.
  3. AC3's exit-0 fixture reuses an existing workflow name (the scratch `reuse` entry as `kind = "experiment"`).
  4. The four unit rows carry no `usage`, so no rendered reference page outside the write set moves.
- Rendering `.claude/agents/` changes agent types the running session cannot spawn until a new session starts, which
  is expected and not yours to fix.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-16`, its final trailer block carrying `Pass: TOOL-dBoundRoles-16` beside
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage explicit
  paths only, never `git add -A`.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-1-acceptance-ledger.md` in the
  pass commit: one line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- In every record you write, cite code as `path#symbol` or a blob-pinned `path@<blob8>:<line>`, never a bare
  `path:line`, and put a pin (a sha, a `path:line` or `DERIVED`) on any line quoting a count of lines, files or units.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list needs its
  own `--dispatch` with `--writes` naming the FULL set before you stage it, unless the call carries `passBase`, in
  which case you record nothing in the run-state file and name the extra path in your return. A file on the kickoff
  manifest's `watch:` list needs the manifest re-stamped in the same commit, and a stale codebase map needs the map
  generator's output.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`; its values are `report` and `author-recorded`.
