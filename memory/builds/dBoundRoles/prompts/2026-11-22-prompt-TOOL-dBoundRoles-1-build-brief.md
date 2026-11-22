**Serves:** journal TOOL-dBoundRoles-1

# Build brief — TOOL-dBoundRoles-1

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  3. Built and CLOSED so far: TOOL-dBoundRoles-14 at `7a58950fb` (the `role` and `field` tag namespaces,
  `READ_FAMILIES`, the tag spelling of every `reads:` line) and TOOL-dBoundRoles-2 at `8795c820a`, red-fixed at
  `be10c4680` (`tools/roles/role-schema.toml`, every role file's `never:` and `return:`, the `## Never`, `## Ceiling`
  and `## Return` sections after `## Charter`, the factory's `--never` and `--return`). Build on those as they stand.
- The spec is rev-6, re-grounded on HEAD `a01362eb0` before this dispatch
  (`prompts/2026-11-22-prompt-TOOL-dBoundRoles-1-reground-e-brief.md`): both reviewers sit at `medium`, R6 joins
  `workflows.toml` to `tools/loop/loop.toml`, so a scratch copy of the roles kit needs the loop kit beside it, and
  §8 F7 to F10 are resolved. Unit 2 landed after that re-ground, so verify every claim the spec makes about the role
  file grammar and `render_role` against HEAD before your first write, and hand a claim that no longer holds back as
  a divergence rather than building around it.
- Rendering the new and merged agent types changes `.claude/agents/`; the running session cannot spawn a changed
  type until a new session starts, which is expected and not yours to fix.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-1`, its final trailer block carrying `Pass: TOOL-dBoundRoles-1`
  beside `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage
  explicit paths only, never `git add -A`.
- Commit `memory/builds/dBoundRoles/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-1-1-acceptance-ledger.md` in the pass commit: one
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
