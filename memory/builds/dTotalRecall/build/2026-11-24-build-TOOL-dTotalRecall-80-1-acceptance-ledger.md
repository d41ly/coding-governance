# TOOL-dTotalRecall-80 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-80
**Caused-by:** TOOL-dTotalRecall-80

No merge bar, no self-test suite, no gate leg and no run of the checker in this pass. The builder built spec rev-4 over
base `b59da9a7daae9c87fed806814eba4d5f56c32520` on node a, 2026-11-24. The pass edits no code and no stamp. §7's legs
are the close's.

The lift is §4's `read_sweep_line` fence, extracted from the spec to a file under the scratch directory and run from the
repository root with the `pass_of` fence of `TOOL-dTotalRecall-81` §4 sourced. `pass_of 69` printed
`f7011dd6fc390d088e0d790c5e6c6901fd20edd6`. The parent read is the main loop's, copied from "The parent read, as run"
of `2026-11-24-prompt-TOOL-dTotalRecall-80-build-brief.md`. The block is the lift's whole output, then the parent
read's whole output (DERIVED 2026-11-24, those two runs):

```text
p69 rc=0
parent ff3c1b93aa888d71bbeb81b6af92f0b1ebd4ea0e
p69^ rc=0
```

Four records hold the sweep line the lift found, and they agree, since the lift printed one line: the acceptance
ledgers and the build briefs of `TOOL-dTotalRecall-76` and `TOOL-dTotalRecall-78` (DERIVED 2026-11-24, `grep -rlE` for
that line's lead over both folders). Two controls were run. Keyed on a sha no sweep read, which is the pass sha with
one digit appended, the lift printed nothing. Run for unit 22 and its own pass commit, the same function printed that
pass's red status and its check-9 failure line, so the lift can carry a failure (DERIVED 2026-11-24, those two runs).

**Evidences:** TOOL-dTotalRecall-80
- AC1 — `read_sweep_line` — the lift printed exactly one line, a status line of label `p69`, in the block above, so no second read is in the brief and none is owed. `grep -rlE "(^|[^a-z0-9])live rc=1" memory/builds/dTotalRecall/build` lists unit 76's acceptance ledger, beside unit 77's ledger and builder return, so the sweep's staged read was red. The parent read's `parent` line holds `ff3c1b93aa888d71bbeb81b6af92f0b1ebd4ea0e`, the sha `git rev-parse f7011dd6fc390d088e0d790c5e6c6901fd20edd6^` prints, and its one other line is a status line of label `p69^`. Neither read prints a `red` line. `git worktree list --porcelain` names no path ending `/gate-mc80` (DERIVED 2026-11-24, these commands).
- AC2 — `git grep -l --all-match` — unit 69's AC1 is answered GREEN from the `p69` read: it prints no check-5 line and no failure line. The parent read prints no check-5 line either, so the row of §4's table is its first, no check-5 line at either commit: no red preceded the pass, which stamped nothing, and there is no contradiction to name. `git show --name-only` of the pass commit lists neither a watched path nor the manifest, and W and S are both `f1e11ac4933ff21ea5ee851f488dad17a313beef` at the parent and at the pass, which is what the two reads agree with and not what decides them. Unit 76's S20 answer, on its ledger's AC13 line, holds the sweep line for pass(69) and states the same C5 verdict there, no failure, answering unit 69's AC1; this answer replaces it and agrees with it. Both outputs stand in the one fenced block above. No S3 condition owes a record, and the predicate lists nothing and exits 1 for `TOOL-dTotalRecall-69` and for `TOOL-dTotalRecall-76`; with `PLAY-dClosedLoop-2` for the cause it lists `2026-10-26-build-TOOL-dTotalRecall-69-deviation-691` for unit 69, so it was seen both ways. No record is written (DERIVED 2026-11-24, these commands).
