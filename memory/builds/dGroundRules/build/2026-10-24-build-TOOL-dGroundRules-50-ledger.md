# TOOL-dGroundRules-50 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-50

No merge bar, gate leg or self-test suite ran in this pass. AC1 ran verbatim from this worktree's root
over `a65cd823e` with this pass's `tools/policy/check_policy.py` in the working tree. AC2 ran in a
clone made as `SCRATCH` makes it, under `%TEMP%/gr50` and checked out at `a65cd823e`, with this
pass's `tools/policy/check_policy.py` copied over the clone's, byte-identical to the committed file,
and `HELP_MOVED` staged there by moving the deferral line from under `## Install` to under
`## Example`; the clone was removed after. Owed at the close: the `memory hygiene` and
`policy fixtures` legs over the built tree, and the RED-first observation of the `New arm:` line of
§6, which covers AC2.

**Evidences:** TOOL-dGroundRules-50
- AC1 — `WITNESS_LINE` printed one page line, `` `adopt-policy: mirror deferred · <file> has uncommitted changes · commit, then re-run --scaffold` ``, line 103 of `help/policy.md`, under `## Install` at line 93; the fixture printed `policy-fixture: adopter-fresh-target · help/policy.md:103 carries the deferral line` and `211 assertion(s) executed · 0 wrong`, exit 0.
- AC2 — after `HELP_MOVED` in `SCRATCH`, `python tools/policy/check_policy.py --fixture adopter-fresh-target` printed a `WRONG` naming `help/policy.md`, `` policy-fixture: adopter-fresh-target · WRONG: help/policy.md has no line under `## Install` holding the deferral line the install-day --scaffold printed ``, no line carrying `carries the deferral line`, and `211 assertion(s) executed · 1 wrong`, exit 1.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: HELP_MOVED -> adopter-fresh-target `WRONG: help/policy.md has no line under `## Install` ...` and no witness line. GREEN `help/policy.md:103 carries the deferral line`, 0 wrong.
