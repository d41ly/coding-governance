# TOOL-dDeclaredLoop-5 deviation 54 — the unattended leg's refusal ceiling raised for check 53, and what the pass adds beside it

**Serves:** deviation TOOL-dDeclaredLoop-5

- **Departs from:** `TOOL-dDeclaredLoop-5@rev-5` [§4 "### The leg's refusal ceiling"]
- **Hand-off:** spec-to-code
- **Before:** `.memory-tree.conf`'s `REFUSAL_CEILINGS` budgets the unattended leg at 264 (PINNED) under decision `TOOL-aSparedSpawn-14`; the census of `fail <n> "` call sites in the leg is 264 (PINNED); `--grade-site` is specified to print a line per entry; the positional row is to be the one `gov_tag.py --list-positional` prints.
- **After:** check 53 adds its two `fail 53` sites, the census reads 266 (PINNED), and the leg's token is `tools/unattended/check-unattended.sh:266:2026-11-14:TOOL-dDeclaredLoop-5` with the RAISED comment line above it; `ARMS_FLOORS` keeps `264:256`. The retirement review the spec tabulates in §4 was re-read against the built leg and found no candidate: check 53's exit-1 site fails R3 and R4, its unreachable-kit site and the fail 1, fail 3 and fail 16 Definition-of-Done sites fail R3, so `memory/project/refusal-retirements.txt` gains no row. Beside the raise: `--grade-site` prints an unlisted actor entry's line without `· until`, as well as its refusal, so every entry whose word resolves is printed; and `gov_tag.py --list-positional` prints only the `§n`, `Mn` and `check n` rows, so the `.memory-tree.conf` row for the new token was written in the list's own `<citing path>\t<path>:<n>` shape beside the `:264` row.
- **Cause:** builder discovery
- **Reason:** the first dispatch found check 53's two sites past the leg's ceiling, and the spec's resolution, §8 F7 (a), keeps every refusal and the clause whole with the least governance change; the decision row `TOOL-dDeclaredLoop-5` (ER:388) landed in the main loop's records commit before this pass. The two additions are what the code needed: an unlisted actor entry still has a class to print, and the spec's named source for the positional row does not list file:line rows.
- **Surface:** REFUSAL_CEILINGS, the leg's token 264 -> 266
- **Evidence:** `REFUSAL_CEILINGS` in `.memory-tree.conf` and `tools/unattended/check-unattended.sh`'s check 53 block at the pass commit of `TOOL-dDeclaredLoop-5`; `tools/loop/loop_lib.py#check_site_witnesses`; the acceptance ledger `2026-11-14-build-TOOL-dDeclaredLoop-5-1-acceptance-ledger.md`, its AC6 and AC9 lines.
- **Risk:** loosening
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the raise rests on decision `TOOL-dDeclaredLoop-5` under ER:388
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-build-TOOL-dDeclaredLoop-5-1-builder-return
