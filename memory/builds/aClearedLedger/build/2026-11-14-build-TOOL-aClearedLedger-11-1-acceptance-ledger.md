# Acceptance ledger — TOOL-aClearedLedger-11

**Serves:** journal TOOL-aClearedLedger-11

Built against spec rev-1 in this record's own commit, from base 232161635.
Each line is a probe the builder made in the pass: the spec's probes H and C over its rows file, its word-break and fail-open probes, and the lint's own command line over a scratch repository. No suite, gate leg or bar ran in the pass.
Owed to the close: AC8 to AC11, which the spec gives to the main loop, the legs of the spec's Gates section, and the RED-first observation of each `New arm:` line, staged as that line says. The main loop observed AC8 to AC11 before this commit, on a clone of 232161635 with the unit's staged change applied, and wrote their four lines below.
Not a criterion, and probed all the same: the payloads of the hook suite's new arms were fed to a copy of the hook beside a planted manifest and each exit was the one the spec's arm table names; the lint suite's widened assertion, its new staged assertions and its command-line arms were re-run as probes outside the suite and each read as the spec's tables say.

**Evidences:** TOOL-aClearedLedger-11
- AC1 — `rows wrong: 0` — probe H, run through `node` against `tools/unattended/gate-guard.js` and the rows file, printed that as its last line and no row above it.
- AC2 — `rows wrong: 0 · no set: False` — probe C, run through `python` against `tools/check-spec-tokens.py` and the rows file, printed that as its last line and no row above it.
- AC3 — `D4` — the word-break probe printed that through `node -p`, and the candidate probe of TOOL-aClearedLedger-3 printed `0 0 1` through `node`.
- AC4 — `grep -c 'share a file name' tools/unattended/README.md` — printed a count of one, PINNED 2026-11-14, and the same grep over `tools/unattended/gate-guard.js` printed the same count.
- AC5 — `runner:` — a copy of `gate-guard.js` with no `gate-legs.json` above it exited with the deny status on the fail-open payload and its stderr held that token; it did the same with a `gate-legs.json` above it holding `{`. The same copy allowed the leg alone in both states.
- AC6 — `grep -c 'The policy reader refused:' tools/check-template-size.sh` — printed a count of one, PINNED 2026-11-14; `grep -c 'handed-in default because' tools/check-template-size.sh` printed none and `grep -c 'fail 8 ' tools/check-template-size.sh` printed one, both on this PINNED 2026-11-14 read.
- AC7 — `memory/guides/SESSION-KICKOFF.md` — with the unit's files staged, the criterion's `git diff --cached -U0` pipeline printed a count of one, PINNED 2026-11-14: the staged `last-audit` line ends in 232161635, the commit's parent.
- AC8 — `FLOOR_ASSERTIONS=210` — the main loop's grep over the two suites on the clone printed that line and `FLOOR_ASSERTIONS=252`.
- AC9 — `arm FAIL` — the lint's suite, run whole by the main loop on the clone, printed no line opening that, printed an `arm ok` line for each arm, exited with status zero and ended `PASS (257 assertions)`, PINNED 2026-11-14.
- AC10 — `FAIL` — the hook's suite, run whole by the main loop on the clone, printed no line opening that, exited with status zero and ended `PASS (230 assertions)`, PINNED 2026-11-14.
- AC11 — `[bar]` — the leg `spec tokens (a spec's own names resolve)`, run by its own argv over the clone's tree by the main loop, exited with status zero and printed no row carrying that.
