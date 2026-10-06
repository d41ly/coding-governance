# TOOL-aMendedFleet-65 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-65

**Evidences:** TOOL-aMendedFleet-65
- AC1 — `bash tools/push-main.sh --prepare --slug tMint` — in a `git clone --bare` of the worktree under `%TEMP%`/m65 and a working clone of it, `main` at the branch head plus this unit's `govkit.py`, `push-main.sh` and `check-verdict-epoch.sh`: a branch adding a comment line to `tools/runlog/extract.py` was prepared, exit 0, first parent the advertised tip, stdout one `mint: runlog` line, and the merge's diff against its first parent moved `KIT_RUNLOG_VERSION` from 1.6 to 1.7 with every runlog marker beside it, eight files and a clean tree. Staged break: the same script with the base lander, govkit and gate printed no mint line and the merge carried 1.6
- AC2 — `python tools/govkit/govkit.py epoch --base <tip>` — at the AC1 merge it printed `epoch: runlog · clean` and `bash tools/check-kit-versions.sh` exited 0. Staged break: at the base lander's merge it printed a runlog FAILED line
- AC3 — `git rev-parse HEAD` — a second `--prepare` on the AC1 branch exited 0 with HEAD unchanged and no `mint:` line naming a new value
- AC4 — `mint: kit versions onto` — in the same fixture `main` took the comment commit and `bash tools/push-main.sh` pushed a `mint: kit versions onto origin/main at <sha8>` commit to the bare repository whose diff moved `KIT_RUNLOG_VERSION` to 1.7; no `core.hooksPath`, so no bar ran. Staged break: the base lander pushed the move with no mint commit
- AC5 — `tools/govkit/govkit.py` — a branch committing its removal was prepared: exit 0, the merge exists on the tip, and stdout carried one `NOT minted — no govkit deployer` line. Staged break: the base lander prepared silently
- AC6 — `tools/govkit/registry.toml` — a branch committing `[[entry` into it was prepared: exit 1, `the version minter REFUSED` with govkit's parse refusal, `git rev-parse HEAD` equal to the branch tip and the branch checked out. Staged break: the base lander kept the merge and exited 0
- AC7 — `python tools/govkit/govkit.py epoch` — on the AC1 branch tip before any prepare, `GATE_PUSH_BASE` unset: `epoch: runlog · owed at the lander`, exit 0. Staged break: the base govkit printed a runlog FAILED line and exited 1
- AC8 — `GATE_PUSH_BASE` — the same call with it set to the tip's sha printed a runlog FAILED line and exited 1, on the unit and on the base alike
- AC9 — `bash tools/memory-tree/check-verdict-epoch.sh` — a branch adding a behaviour line to `tools/memory-tree/check-memory-hygiene.sh`: exit 0 with one `owed at the lander` line unset, exit 1 with `GATE_PUSH_BASE` set to the tip. Then that branch prepared minted `memory-tree · 2.119 -> 2.120` into the merge, after which the gate read `clean` and govkit `epoch` exit 0 at the push boundary, the version gate exit 0. Staged break: the base gate exited 1 unset
- AC10 — `grep -n "mint" tools/push-main.sh tools/memory-tree/check-verdict-epoch.sh` — the usage header names the minting `--prepare` and the `mint: kit versions onto` commit, and the gate's header says the obligation binds at the push boundary

## The suite arms

S9's arms are written and not run as suites. `check_mint_verb` in `tools/govkit/selftest.py` ran
as a one-function slice under `%TEMP%`/m65s: 7 of 7 ok, and 6 FAIL with the base `govkit.py` copied
in. The new arms of `tools/push-main.test.sh` (case 24) and `tools/memory-tree/check-verdict-epoch.test.sh`
(section 5b, and the live arm now accepting `owed at the lander`) did not run. `cmd_epoch`'s output
over the live tree with `--base` at the merge-base was byte-equal (`cmp`) before and after the
extraction, exit 1 both. The govkit selftest, the two shell suites, the refusal join,
`gen_map.py --check`, and the lexicon, line-length, install-prefix, kit-version and both epoch legs
are owed at the close.
