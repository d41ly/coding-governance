**Serves:** journal TOOL-dBoundRoles-2

# Build brief — TOOL-dBoundRoles-2

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  2. TOOL-dBoundRoles-14 is built and CLOSED at `7a58950fb`: `tools/roles/roles_lib.py` now carries `READ_FAMILIES`
  (`READ_KEYS` derived from it), `parse_read_key`, `derive_field_tag` and `derive_stage_field_tag`; every role file's
  `reads:` line is in the tag spelling (`field.input.spec`); `check_roles.py` has `--print-tag-rows`; and
  `adopt-roles.test.sh` gained arm 26 with its floor at 79. Build on those as they stand, not as the spec's base had it.
- The spec's base is `4ed9e567`; the run's is `8b8b1374`. Since then TOOL-dWitnessedBar-23 added
  `tools/roles/agents/gov-tester.agent.md`, so there are eleven role files; §8 F4 is yours to discharge against it at
  HEAD.
- Two earlier builders of this run diverged on stale claims the spec checker cannot see. Before your first write,
  verify every claim the spec makes about current code against HEAD: each path, line, function, count and behaviour.
  Hand any claim that no longer holds back as a divergence rather than building around it.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-2`, its final trailer block carrying `Pass: TOOL-dBoundRoles-2`
  beside `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage
  explicit paths only, never `git add -A`.
- Commit `memory/builds/dBoundRoles/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-2-1-acceptance-ledger.md` in the pass commit: one
  line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- In every record you write, cite code as `path#symbol` or a blob-pinned `path@<blob8>:<line>`, never a bare
  `path:line`, and put a pin (a sha, a `path:line` or `DERIVED`) on any line quoting a count of lines, files or units:
  the positional and writing-practice legs red on both.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (a
  deviation record, a generated file) needs its own `--dispatch` with `--writes` naming the FULL set before you stage
  it, since `--check-commit` grades the latest row's anchor only. A file on the kickoff manifest's `watch:` list needs
  the manifest re-stamped in the same commit, and a stale codebase map needs the map generator's output.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
