# KICK-dKeptSession-89 — acceptance ledger

**Serves:** journal KICK-dKeptSession-89

One builder pass, in the run worktree over the working tree at `d1328d4d7`, staged and not committed: the
commit, with its `Pass:` trailer, is the main loop's. No merge bar, no self-test suite and no gate leg ran
in it. `check_policy.py` is refused to the builder role, so AC5 is the main loop's, and AC7 reads the pass
commit, so it is too. Neither was observed when this ledger was written.

The spec's claims about the tree were read before the first edit and held: the two definitions, their
calls, the base compare standing twice, and no spelling of either old name outside `memory/builds/` and the
paths its S1 names. `--suggest` answered OK for each of the new names. `origin/main` read `525f3ab97`
before and after the edit.

Beside the criteria, two probes ran. One, with a stub factory, read `write_shrink_file` keep the named rows
in key order with their values and return None, and `read_shrink_base` return the factory's pair unchanged.
One, over the live factory and `memory/project/unnamed-keys.txt` with `write_rows` captured, read
`write_shrink_list` drain the one name left out of the derivation, and `check_shrink_list` report that name
stale and a planted name unlisted.

**Evidences:** KICK-dKeptSession-89
- AC1 — observed: `git grep -n name_ledger -- tools/ help/` printed no line, and the `grep -cE` of the definitions over `tools/policy/policy.py` printed `4`.
- AC2 — observed: the docstring probe printed `[]`; `grep -c 'the shrink-list factory made'` printed `0`, `grep -c 'compare_to_base(repo, reg)'` printed `1`, `grep -c '= read_shrink_base('` printed `2` and `grep -c '^ *write_shrink_file('` printed `1`.
- AC3 — observed: `python tools/policy/policy.py lists --check` exited 0 before and after the edit, and `cmp` of the two files was silent.
- AC4 — observed: the `read_shrink_base` probe exited 1, its last stderr line opening `policy.Refusal: ` and carrying `the base compare did not run`.
- AC5 — observed by the main loop over the staged tree: `python tools/policy/check_policy.py` exited 0, and its `reader-join`, `purposes-drain`, `purposes-new` and `legacy-homes` fixtures each exited 0 and printed `0 wrong`.
- AC6 — observed: `python tools/codebase-map/gen_map.py --check` exited 0 after the write, which moved `memory/map/generated/symbols.json` alone; over it `grep -c name_ledger` printed `0` and the ids' `grep -cE` printed `4`.
- AC7 — not observed in this pass, the main loop's, at the pass commit: `python tools/lexicon/lexicon.py --merge-losses "origin/main..HEAD"`, whose summary is to carry `losses=0` and `restored=4`.

## Owed to the close

AC5, AC7 and every leg the spec's section 6 names. The unit mints no arm, so no RED-first observation is
owed. The `policy.py` anchors `help/policy.md` and `help/agent-limit.md` carry equal the fingerprints the
code derives (`python tools/govkit/docs_leg.py --fingerprints`), so no help page moves.

The bug-class checklist was run over the three product paths by `gotchas.py --for-paths`, since nothing is
committed yet. One class bears: `two-answers-to-one-question`, which S2 narrows by folding the second copy of
the base compare into `read_shrink_base`. The run over the pass commit is the main loop's.
