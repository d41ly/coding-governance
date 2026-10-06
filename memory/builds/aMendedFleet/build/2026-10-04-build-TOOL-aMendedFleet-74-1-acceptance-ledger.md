# TOOL-aMendedFleet-74 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-74

**Evidences:** TOOL-aMendedFleet-74
- AC1 — `tools/workflows/check-workflow-syntax.js` — its evaluation shape, run from a scratchpad stub with a recording `agent`, put the paragraph naming the command after `--dispatch` and `--brief` and before `NO GATE, SUITE OR BAR RUNS` in unattended mode, put it in attended mode with no `--dispatch` order, and logged a line naming the unit and the command; the base file run the same way failed all of these
- AC2 — `git show` — the stub run with no `prebuild`, both modes, recorded prompts, options and logs byte-identical between the tip and `7af5f564`; a staged break that logged unconditionally made both comparisons fail
- AC3 — `prebuild` — set to `7`, an empty string, a string with a newline and one with a backtick, each threw an error opening `unattended-unit:` and naming the key with no spawn recorded; the base file reached the spawn on all four
- AC4 — `node tools/workflows/check-workflow-syntax.js` — 7 scripts parsed clean, `bash tools/workflows/check-verifier-fanout.sh` clean over 7, and `grep -c "^function "` printed 1
- AC5 — `grep -n "prebuild" tools/workflows/unattended-unit.js` — the header hits name the off default, the `--for-paths` command spelled with `<prefix>`, and the measurement against builds without it that the default waits on; the file spells no `tools/` path
