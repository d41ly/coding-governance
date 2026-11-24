# TOOL-dBoundRoles-57 deviation 572 — the builder's departures from the description-invariant spec

**Serves:** deviation TOOL-dBoundRoles-57

- **Departs from:** `TOOL-dBoundRoles-57@rev-3` [S1, AC1]
- **Hand-off:** spec-to-code
- **Before:** S1 at rev-3 lists the tokens the description holds and then the search-tool words it does not, with no order between the assertions; AC1 imports the kit's self-test module as a library and runs no suite.
- **After:** S1: the no-search-tool assertion stands before the token loop of `tools/memory-recall/selftest.py#test_skill_description_invariants`, so the wording AC1 restores, which drops `git grep` as well, fails naming `Grep`. AC1: the module's `check` decorator runs each arm at definition, so a plain import runs the suite; the pass's probe compiled the module with that decorator replaced by one that returns the function unrun, then called the check, and swapped `copy_extra` for a copy from the scratch kit to stage the break. The comment over check 4 is re-wrapped to its new words.
- **Cause:** builder discovery
- **Reason:** with the token loop first, the restored wording fails on `git grep` and the staged arm of section 7 never reaches the assertion it names; and a role agent runs no suite, which a plain import of this module is. `TOOL-dBoundRoles-60` lifts the invariant into an undecorated function, so the probe's neutralised decorator leaves no shipped code behind.
- **Evidence:** the build brief `memory/builds/dBoundRoles/prompts/2026-11-24-prompt-TOOL-dBoundRoles-57-build-brief.md` and the acceptance ledger `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-57-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value; reported by the `report` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-57
