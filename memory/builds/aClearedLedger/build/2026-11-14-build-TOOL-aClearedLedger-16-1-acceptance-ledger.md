# Acceptance ledger — TOOL-aClearedLedger-16

**Serves:** journal TOOL-aClearedLedger-16

Built against spec rev-1 in this record's own commit, from base edc6286af.
Each line is a probe the builder made in the pass: the probe of the spec's section 4, "The probe", the floor probe, the docstring probe and the code probe of its section 6, each cut out of the spec, saved in the session scratchpad and run from the worktree's toplevel, and the criteria's own greps. No suite, gate leg or bar ran in the pass.
The rows files are the JSON blocks of this spec and of the specs of TOOL-aClearedLedger-12, TOOL-aClearedLedger-13 and TOOL-aClearedLedger-14, each saved as its own file.
Red side, on scratch copies of the hook outside the repository: the hook at edc6286af printed the red lines AC1 and AC2 state, and the hook of this commit with its keep-as-word test weakened to `!redir || q >= 0` named rows V1 and V2 over this spec's rows file and rows U8 to U10 over that of TOOL-aClearedLedger-14, the red figure AC3 states (PINNED, 2026-11-14).
The floor the builder found in the hook's suite was the one TOOL-aClearedLedger-15 left at 599c3dfb5, so the raise is the spec's own derivation and nothing was added to another value.
Owed to the close: the hook's suite on a frozen clone, the legs of the spec's Gates section, and the RED-first observation of each `New arm:` line, staged as that line says.
Not a criterion, and probed all the same: `bash -n` read the hook's suite without a syntax error, and `node` loaded the hook. The spec's Inventory mints no identifier, so the naming lexicon had nothing to name. No file this commit moves is on the kickoff manifest's watch list, so no stamp is owed.

**Evidences:** TOOL-aClearedLedger-16
- AC1 — `a,,>x,b,,<y,c,,>z,d,2,>w` — the probe, run through `node`, printed that as its first line and `-1,0,-1,-1,0,-1,-1,0,-1,-1,0,-1` as its second (PINNED, 2026-11-14).
- AC2 — `- - D4` — the same probe printed that as its third line (PINNED, 2026-11-14).
- AC3 — `rows wrong: 0` — the probe, run through `node` against `tools/unattended/gate-guard.js`, printed that as its last line over this spec's rows file and over each older rows file (PINNED, 2026-11-14).
- AC4 — `grep -cE '^run_planted "D6 the leg with a quoted target glued to 2?> -> deny" +2 "\$B" "\$M_FLAG 2?>\\"x\.log\\""$' tools/unattended/gate-guard.test.sh` — printed 2 (PINNED, 2026-11-14).
- AC5 — `rise: 2` — the floor probe, run through `bash`, printed that and then 1, the `RAISED 221 -> 223 at TOOL-aClearedLedger-16` line (PINNED, 2026-11-14).
- AC6 — `grep -cF "'>' x.log" tools/unattended/gate-guard.js tools/unattended/README.md` — printed 0 for each file, and `grep -c "'&'>x.log., .'>'>x.log"` over the same files printed 1 for each (PINNED, 2026-11-14).
- AC7 — `code unchanged: True` — the code probe printed that; the docstring probe printed `'&'>x.log commands: 2 hit: True` and `'>'>x.log commands: 1 hit: True`; `grep -c "splits the command here because the split pattern has no" tools/check-spec-tokens.py` printed 1 and `grep -c "which this reader reads with its quotes out" tools/check-spec-tokens.py` printed 0 (PINNED, 2026-11-14).
