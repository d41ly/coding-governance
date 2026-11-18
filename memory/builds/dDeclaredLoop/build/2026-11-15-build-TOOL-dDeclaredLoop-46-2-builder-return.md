**Serves:** journal TOOL-dDeclaredLoop-46

# Builder return — TOOL-dDeclaredLoop-46, dispatch 2: --dispatch refused: unit 6's open dispatch row claims five of its paths

## Why

REFUSAL: --dispatch refused this unit's write set, and that refusal is binding. It printed "UNATTENDED check 49 FAILED — --dispatch declares a path a sibling pass in the same group already declared, and two passes claiming one file are not disjoint: tools/loop/kit.toml also in 2b1d84b0 TOOL-dDeclaredLoop-6" and exited 1.

Unit 6's dispatch row is still open in memory/builds/dDeclaredLoop/RUN.md (line 222, at 2026-11-15T16:57:06Z). That unit is being re-specced and is not building, but its row has not been withdrawn. The check names only the first collision. Comparing that row with my 76-path declaration, five paths overlap:
- tools/loop/kit.toml (spec §4 Files touched: its two [[gate_leg]] tables must gain `stage`, S2)
- memory/guides/SESSION-KICKOFF.md (the kickoff manifest re-stamp, owed because run-gates.sh is on its watch list)
- memory/builds/dDeclaredLoop/README.md, memory/LIVE.md and memory/backlog/TOOL.md (rewritten by gen_build_index.py --write)

To unblock, the caller has to either withdraw or re-declare unit 6's dispatch row without these paths, or run units 46 and 6 one after the other. S2 and AC2 need every [[gate_leg]] table, the loop kit's included, so unit 46 cannot leave tools/loop/kit.toml out of its write set without a spec change.

Nothing was written. The brief was not recorded because --brief writes and comes after the refused dispatch. The tree is clean at base, so there is nothing to restore and no patch file.

## Summary

TOOL-dDeclaredLoop-46 is not built: --dispatch refused its write set (check 49), so there is no commit.

Before dispatching, I checked rev-5 against the tree with read-only probes. No gate, suite or bar ran.

- **Origin/main version (stands in for AC1 and AC5's starting figure):** after `git fetch origin`, origin/main is still 179486e8f. Its runner reads KIT_RUN_GATES_VERSION=1.48 and its canary has no `KNOWN` line with "stage" (count 0). The branch reads 1.47 and both of its `KNOWN` lines carry "stage" (count 2). So S1 would mint 1.49, and STAGE_FLOOR_RUN_GATES would be (1, 49).
- **Population (stands in for AC2's tomllib probe and the selfcheck leg):** there are 70 [[gate_leg]] tables in 27 PINNED files, matching S2. Every manifest row carries `stage` and no descriptor table does yet.
- **Emitter and 7h:** the code matches §4 Evidence (tools/govkit/govkit.py#write_gate_legs, #check_target_reads_subject, #selfcheck). One build note: the ceiling keep rule can add `ceiling` after keys set earlier, so `stage` has to be set after the keep rule for it to stay the row's last key.
- **Selftest staged edits:** inserting `stage` as the table's last key leaves the "ceiling = 1780" edit and the name/subject edit in tools/govkit/entries/push-main.kit.toml each matching exactly once.
- **Version carriers:** under tools/, skills/ and help/, only tools/run-gates/README.md line 3 and run-gates.sh line 36 carry run-gates@1.47.
- **Budgets:** no new function, verb, flag or leg is planned, and memory/DECISIONS.md is not needed. No other code checks the key set of a [[gate_leg]] table. The longest `stage` line would be 35 characters, well under the line-length limit.

The refusal and the five overlapping paths are listed in `why`. The overlap is with unit 6's open dispatch row (2b1d84b0) in memory/builds/dDeclaredLoop/RUN.md.

Owed once a pass can dispatch:
- at the close: the spec's §7 PINNED legs, plus AC2 and AC4 through `govkit selfcheck`;
- the RED-first observation of the one `New arm:` line, which adds arms to check_ceiling_emission and check_benched_probe_arms in tools/govkit/selftest.py;
- AC5, re-observed at the close and again on the landing's reconciled tree.

Nothing timed out or was skipped. Every probe used was read-only and returned within its bound.
