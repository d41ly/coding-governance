**Serves:** journal TOOL-dBoundRoles-14

# Build brief — TOOL-dBoundRoles-14

You build ONE unit from its spec; the spec is the contract and this brief only adds what the spec cannot know.

## Where the build stands

- This is dBoundRoles's build run. Its spec run landed every spec DEFERRED, and this run builds them in the build-order
  table's order. This is build order 1, the first unit: nothing of this build is built yet.
- The spec's base is `4ed9e567`; the run's is `8b8b1374`. Since then dOrderedCharter, dDeclaredLoop, dPlacedRequest and
  dWitnessedBar landed, and the last touched `tools/playbook/` and `tools/roles/` (TOOL-dWitnessedBar-12 added the leg,
  pack and check namespaces to `tools/playbook/namespaces.toml`; TOOL-dWitnessedBar-23 added the `gov-tester` role, an
  eleventh agent file with its own `reads:` line). Re-derive the agents list and every `namespaces.toml` row at HEAD.
- §8 F4 is yours to discharge: PLAY-dOrderedCharter-19 S2, S4, S13 and PLAY-dOrderedCharter-10 S3, S4, S7 were unbuilt at
  the spec's base. dOrderedCharter has landed since; confirm each section's code exists at HEAD before building on it,
  and hand back a divergence naming the section if one is still absent.
- The spec is rev-6, revised at the main loop over the first builder's divergence
  (`build/2026-11-22-build-TOOL-dBoundRoles-14-1-builder-return.md`): 25 read keys with `brief:prompt` and the
  `upstream` family, eleven role files with `gov-tester`, the extractor contract `fn(ctx, path, text=None)` returning
  kind `tag`, a path-only `purpose-source` (§8 F6), and three readers rev-5 missed (`handoff.py` render's input check,
  `adopt-roles.test.sh` arm 22, `help/tags.md`). Its citations are re-pointed at HEAD `760bfa18`; still verify each claim
  about current code against source before building on it, and hand a claim that no longer holds back as a divergence.
- Rev-7 then folded the second builder's divergence
  (`build/2026-11-22-build-TOOL-dBoundRoles-14-2-builder-return.md`): the binding join re-parses each unit manifest
  through `instruction_units.parse_unit_rows` (§8 F7), reading its text through a `read_served_text(ctx, path)` helper
  lifted out of `check_namespace_purpose` in `tag_index.py`.
- §5 discloses one gap left open on purpose: the index's extractor version does not hash `check_roles.py` or
  `roles_lib.py`, so an edit to either leaves cached rows stale until `gov_tag.py --rebuild`. Do not close it here.

## What the main loop needs from your commit

- One pass commit, its subject naming `TOOL-dBoundRoles-14`, its final trailer block carrying
  `Pass: TOOL-dBoundRoles-14` beside `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's trailer and
  nothing after it. Stage explicit paths only, never `git add -A`.
- Commit `memory/builds/dBoundRoles/RUN.md` with the pass, since `--dispatch` stages rows in it.
- The spec's status is already `INPROGRESS`; move it to `CLOSED` only in the pass commit, after every edit has landed.
  Run `python tools/memory-tree/gen_build_index.py --write` after staging and commit every file it rewrites.
- Write the acceptance ledger
  `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-14-1-acceptance-ledger.md` in the pass commit: one
  line per section 6 criterion, each leading with a backticked token that criterion itself spells.
- The main loop declared the spec's Files touched in `--dispatch` before your spawn. A path beyond that list (the
  ledger, a deviation record, a generated file, a rendered agent under `.claude/`) needs its own `--dispatch` with
  `--writes` for it before you stage it. A file on the kickoff manifest's `watch:` list needs the manifest re-stamped
  in the same commit, and a stale codebase map needs the map generator's output; declare both.
- Run no gate leg, no suite, no bar. Verify with a fixture or a probe of the code you changed.
- A change the spec did not state is a deviation record in `build/`, as the build README's rules say; its values are
  `report` and `author-recorded`.
