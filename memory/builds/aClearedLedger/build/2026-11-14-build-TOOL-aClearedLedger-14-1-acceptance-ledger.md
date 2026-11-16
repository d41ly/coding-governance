# Acceptance ledger — TOOL-aClearedLedger-14

**Serves:** journal TOOL-aClearedLedger-14

Built against spec rev-2 in this record's own commit, from base 573c67ae1.
Each line is a probe the builder made in the pass: the probe of the spec's section 4, "The probe", the table probe and the code probe, each cut out of the spec, saved in the session scratchpad and run from the worktree's toplevel, and the criteria's own greps. No suite, gate leg or bar ran in the pass.
The rows files are the JSON blocks of this spec and of the specs of TOOL-aClearedLedger-12 and TOOL-aClearedLedger-13, each saved as its own file.
Red side, on scratch copies of the hook outside the repository: the hook at 573c67ae1, whose blob is 77894998, named rows U1 to U7 and printed `no quotedAt`, the red figure AC1 and AC2 state (PINNED, 2026-11-14); a copy holding this commit's hook with the drop test taken out of the candidate loop named rows U2, U6 and U7 (PINNED, 2026-11-14), the first red case AC1 states.
The floor the builder found in the hook's suite was the one TOOL-aClearedLedger-13 left, its blob at the base being f5a82b10, so the raise is the spec's own derivation and nothing was added to another value.
Owed to the close: the hook's suite on a frozen clone, the legs of the spec's Gates section, and the RED-first observation of each `New arm:` line, staged as that line says.
Not a criterion, and probed all the same: `bash -n` read the hook's suite without a syntax error, `node` loaded the hook, and the naming lexicon's `--suggest` named no cell for the new field, which the spec's Inventory says no cell grades. No file this commit moves is on the kickoff manifest's watch list, so no stamp is owed.

**Evidences:** TOOL-aClearedLedger-14
- AC1 — `rows wrong: 0` — the probe, run through `node` against `tools/unattended/gate-guard.js`, printed that as its last line over this spec's rows file and over each older rows file (PINNED, 2026-11-14).
- AC2 — `a,&,>x,b,>,>y,c,2,>z,d,2,>w,e,2>v,f,>>$L` — the probe's first line read that, and its second read `-1,0,-1,-1,0,-1,-1,0,-1,-1,0,-1,-1,2,-1,2` (PINNED, 2026-11-14).
- AC3 — `grep -c 'run_planted "D6 a quoted . glued before a redirection is an argument -> allow"' tools/unattended/gate-guard.test.sh` — printed 2 (PINNED, 2026-11-14).
- AC4 — `grep -c '^FLOOR_ASSERTIONS=219$' tools/unattended/gate-guard.test.sh` — printed 1, and `grep -c 'RAISED 217 -> 219 at TOOL-aClearedLedger-14' tools/unattended/gate-guard.test.sh` printed 1 (PINNED, 2026-11-14).
- AC5 — `restated in check_bar: True` — the table probe, run through `python` over this spec and the spec of TOOL-aClearedLedger-13, printed that, then `frozen row cells: 6 header cells: 3`, then `rows off their header: 0` (PINNED, 2026-11-14).
- AC6 — `code unchanged: True` — the code probe printed that before the commit, and `grep -c 'quoted operator character' tools/unattended/gate-guard.js tools/unattended/README.md tools/check-spec-tokens.py` printed 1 for every file (PINNED, 2026-11-14).
