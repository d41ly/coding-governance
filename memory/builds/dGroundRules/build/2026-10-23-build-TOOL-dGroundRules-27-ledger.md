# TOOL-dGroundRules-27 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-27

No merge bar, no gate leg and no self-test suite ran in this pass. Every criterion ran in the kit's
directory of a scratch clone of this branch at `96f914df1` under `%TEMP%`, with this pass's
`check_policy.py` and `README.md` copied over its working tree, which each case's snapshot commits;
the clone was removed after. AC1 and AC2's staged halves inserted
`raise RuntimeError("run_govkit staged")` as the first statement of the clone's `run_govkit` and copied
the unstaged file back after. The `New arm:` line's red-first observation, and the §7 legs, are the
close's.

**Evidences:** TOOL-dGroundRules-27
- AC1 — `run_govkit staged` — staged, `python check_policy.py --fixture legacy-homes-withheld-install` printed `policy-fixture: legacy-homes-withheld-install · legacy-homes-withheld-install · the target · WRONG: RuntimeError: run_govkit staged` and `1 assertion(s) executed · 1 wrong`; undone, it printed the plan's `ORDER [project-owned] tools/policy/legacy-homes.txt` row, the apply row `receipt holds policy · none held`, and `2 assertion(s) executed · 0 wrong`.
- AC2 — `run_govkit staged` — staged, `census-default-adopter` printed `WRONG: RuntimeError: run_govkit staged` and `1 wrong`, and `adopter-fresh-target` printed `policy-fixture: adopter-fresh-target · WRONG: run_govkit staged` and `28 assertion(s) executed · 1 wrong`, the raise recorded rather than escaping. Undone, `census-default-adopter` printed `2 assertion(s) executed · 0 wrong`; `adopter-fresh-target` printed `1 wrong`, its one WRONG the deployer's `apply` refusing on the policy adopter's install-day `uncommitted changes; the mirror renders a revision, commit first`, the known red `TOOL-dGroundRules-31` owns, so its `0 wrong` half is owed at the close after that unit.
- AC3 — `build_source_snapshot` — the `python -c` probe calling `run_govkit(top, top, '--help')` with the clone's toplevel printed `RAISED: run_govkit: C:/Users/daily-agent/AppData/Local/Temp/g27 is the tree under test; take build_source_snapshot first` and no exit status; `python check_policy.py --fixture govkit-source-root-refused` printed that message under `a RuntimeError naming C:/Users/daily-agent/AppData/Local/Temp/g27 and build_source_snapshot` and `1 assertion(s) executed · 0 wrong`.
- AC4 — `run_ships_join` — `grep -n govkit.py check_policy.py` printed four lines, 1082 and 1091 inside `run_govkit` and 3541 and 3551 inside `run_ships_join`, each enclosing function read off Python's `ast` spans; `grep -n run_install_verb check_policy.py` printed nothing and exited 1.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the `policy check` and `policy fixtures` legs, observed by a researcher in scratch clones of `4f76c4b39`: --fixture govkit-source-root-refused. run_govkit staged to admit equal roots -> `WRONG: the deployer ran: exit 0`. GREEN: the RuntimeError naming build_source_snapshot (exit 1 only on the guard-trace trailer).
