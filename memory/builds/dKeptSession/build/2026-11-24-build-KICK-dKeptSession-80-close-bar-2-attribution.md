**Serves:** research KICK-dKeptSession-80

# dKeptSession — the close's second full bar, over the merged tree, and its reds attributed against origin/main

The full merge bar, `GATE_FULL=1 bash tools/run-gates/run-gates.sh` with `GATE_SELFTESTS` unset, ran at `3b7cfc355`
on node a, 2026-11-24, and read RED on 15 of 120 legs, 106 held (DERIVED, that run's last line).

Each red leg's manifest argv, its `{prefix}` written as `tools`, was run through Git-Bash in this tree and in a
worktree at `origin/main` `525f3ab97`. Node d's probe passed `{prefix}` literally, which may be why five of its legs
read exit 2 on both sides.

| Leg | This tree | origin/main | Whose, and its disposition |
|---|---|---|---|
| policy check | 1 | 1 | MIXED. Main's: `tests.history-verdicts` and `tests.fixture-templates` have no reader. The run's, presets and unnamed keys: `8e0a3ba6b` and widen 5 |
| remote literals (kit code names no remote) | 1 | 0 | the run's: `0915f1016` |
| govkit selfcheck | 1 | 0 | the run's: `bfe2c300d` |
| layer dependencies (the core never depends on an expansion) | 1 | 0 | the run's: `3c0175552` |
| python reads (a name never bound, an import outside its guard) | 1 | 0 | the run's: widen 6 |
| shell hygiene (a location probe asked from a moved directory) | 1 | 0 | the run's: `ec9226a9b` |
| shell hygiene (a fork spent on builtin work) | 1 | 0 | the run's: `ec9226a9b` |
| shell hygiene (a fixed-name temp renamed into place) | 1 | 0 | the run's: `ec9226a9b` |
| shell hygiene (a stage committed with no staged-diff test) | 1 | 0 | the run's: `ec9226a9b` |
| encoding posture (JavaScript text IO names its encoding) | 1 | 0 | the run's: `dd7e4082f` |
| shell hygiene (a quoting hazard) | 1 | 0 | the run's: widen 7 |
| portability (shell lines only shrink) | 1 | 0 | the run's: widen 8 |
| kickoff-manifest ratchet | 1 | 0 | the run's, red by construction at the merge: `ab5149256` |
| memory hygiene | 1 | 0 | the run's: check 15's backlog citation and widen 9, and check 27's gotcha named |
| tags (the resolver's checks) | timed out | 0 | the bar timed it out and its serial retry; run by hand it is green in both trees |

The `tags` leg by hand, DERIVED from each run's own clock: both trees run together took about twelve minutes; this
tree alone took 483 s and `origin/main` alone 404 s, against a 420 s ceiling (PINNED 2026-11-24, `tools/gate-legs.json`).
Light commit work ran beside both, so neither is a clean reading. The check reports no finding in either tree.
