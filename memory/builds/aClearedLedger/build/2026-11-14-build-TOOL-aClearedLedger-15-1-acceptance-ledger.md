# Acceptance ledger — TOOL-aClearedLedger-15

**Serves:** journal TOOL-aClearedLedger-15

Built against spec rev-1 in this record's own commit, from base b25dad34c.
Each line is a probe the builder made in the pass: the probe of the spec's section 4, "The probe", cut out of the spec, saved in the session scratchpad and run from the worktree's toplevel, and the criteria's own greps. No suite, gate leg or bar ran in the pass.
The rows files are the JSON blocks of this spec and of the specs of TOOL-aClearedLedger-12, TOOL-aClearedLedger-13 and TOOL-aClearedLedger-14, each saved as its own file.
Red side, on a scratch copy of the hook outside the repository: the hook at 998b627aa, whose blob is 07723a18, named rows W1 to W4 and W6 over this spec's rows file and read each older rows file whole, the red figure AC1 states (PINNED, 2026-11-14).
The floor the builder found in the hook's suite was the one TOOL-aClearedLedger-14 left at 998b627aa, so the raise is the spec's own derivation and nothing was added to another value.
Owed to the close: the hook's suite on a frozen clone, the legs of the spec's Gates section, and the RED-first observation of each `New arm:` line, staged as that line says.
Not a criterion, and probed all the same: `bash -n` read the hook's suite without a syntax error, and `node` loaded the hook. The spec's Inventory mints no identifier, so the naming lexicon had nothing to name. No file this commit moves is on the kickoff manifest's watch list, so no stamp is owed.

**Evidences:** TOOL-aClearedLedger-15
- AC1 — `rows wrong: 0` — the probe, run through `node` against `tools/unattended/gate-guard.js`, printed that as its last line over this spec's rows file and over each older rows file (PINNED, 2026-11-14).
- AC2 — `grep -cE '^run_planted "D6 a quoted > opening a glued target after 2?> -> deny" +2 "\$B" "\$M_FLAG 2?>.>x\.log."$' tools/unattended/gate-guard.test.sh` — printed 2 (PINNED, 2026-11-14).
- AC3 — `grep -c '^FLOOR_ASSERTIONS=221$' tools/unattended/gate-guard.test.sh` — printed 1, and `grep -c 'RAISED 219 -> 221 at TOOL-aClearedLedger-15' tools/unattended/gate-guard.test.sh` printed 1 (PINNED, 2026-11-14).
