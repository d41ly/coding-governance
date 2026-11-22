**Serves:** journal TOOL-dBoundRoles-21

# Build brief — TOOL-dBoundRoles-21

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run, building every DEFERRED spec in the build-order table's order. This is build order
  4. Built and CLOSED so far: TOOL-dBoundRoles-14 at `7a58950fb`, TOOL-dBoundRoles-2 at `8795c820a` and
  TOOL-dBoundRoles-1 at `3b479f2fe` (red-fixed at `7016640bb`): the `role` and `field` tag namespaces, every role
  file's `never:`, `return:`, `layer:` and `acts-as:`, the merged `gov-reviewer`, the four new roles and the roster by
  layer. Build on those as they stand.
- Every roster spec was re-grounded on HEAD before this dispatch, so its citations hold at HEAD or name the earlier
  unit that changes them. Still verify each claim the spec makes about current code against source before your first
  write, and hand a claim that no longer holds back as a divergence rather than building around it.
- The spec is rev-6, revised over the first builder's divergence
  (`build/2026-11-22-build-TOOL-dBoundRoles-21-1-builder-return.md`): an unset key's derived-default refusal reads as
  unset (§8 F8), the render selftest swaps in a reader answering `None` (§8 F9), `load_policy` returns the merged gate
  grant (§8 F10), and `.governance/policy.json` is rewritten as its render after the pass commit, as §2 S8 states.
  This pass runs in the run's own tree; TOOL-dBoundRoles-37 is already built and CLOSED at `5f7f208fd`.

- Rev-7 then folded the second builder's divergence
  (`build/2026-11-22-build-TOOL-dBoundRoles-21-2-builder-return.md`): the role factory writes `ROLE_EFFORT = "medium"`
  (§8 F11, observed by AC8), and the mirror is committed alone after the pass commit, AC7 observed there, never an
  amend. That builder's unverified partial implementation is the patch
  `C:/Users/d41ly/AppData/Local/Temp/claude/bf1faa02b154e3ee/b48c5b81-0c25-4457-90e8-da811a25e0e9/scratchpad/TOOL-dBoundRoles-21-partial.patch`;
  reuse what still fits rev-7 and verify every hunk against the spec.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-21`, its final trailer block carrying `Pass: TOOL-dBoundRoles-21` beside
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and nothing after it. Stage explicit
  paths only, never `git add -A`.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-21-1-acceptance-ledger.md` in the
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
