# Acceptance ledger — TOOL-aClearedLedger-12

**Serves:** journal TOOL-aClearedLedger-12

Built against spec rev-1 in this record's own commit, from base 4a6394c5b.
Each line is a probe the builder made in the pass: the spec's probe over its rows file, saved in the session scratchpad and run from the worktree's toplevel, and the criteria's own greps. No suite, gate leg or bar ran in the pass.
Before the edit the same probe printed `a,>,>,b,2>,>,c,<,<,<,d`, then `D4 D4 D4`, named rows Q1 to Q6 and ended `rows wrong: 6`, the red figure the spec states for AC1 (PINNED, 2026-11-14).
The floor the builder found in the suite was the one the spec names, so the raise is the spec's own and nothing was added to another value.
Owed to the close: the hook's suite on a frozen clone, the legs of the spec's Gates section, and the RED-first observation of each `New arm:` line, staged as that line says: the guard's last clause put back to the all-digits test with the arms in place.
Not a criterion, and probed all the same: `bash -n` over the suite read it without a syntax error, and the tail of the fourth arm, printed through `printf`, carried the variable and its quotes as typed.

**Evidences:** TOOL-aClearedLedger-12
- AC1 — `rows wrong: 0` — the probe, run through `node` against `tools/unattended/gate-guard.js` and the rows file, printed that as its last line and no row above it (PINNED, 2026-11-14).
- AC2 — `a,>>,b,2>>,c,<<<,d` — the same probe printed that as its first line and `D4 D4 D4` as its second (PINNED, 2026-11-14).
- AC3 — `grep -c 'run_planted "D6 the leg appended ' tools/unattended/gate-guard.test.sh` — printed 4, the row count of the spec's arm table (PINNED, 2026-11-14).
- AC4 — `grep -c '^FLOOR_ASSERTIONS=214$' tools/unattended/gate-guard.test.sh` — printed 1, and `grep -c 'RAISED 210 -> 214 at TOOL-aClearedLedger-12' tools/unattended/gate-guard.test.sh` printed 1 (PINNED, 2026-11-14).
