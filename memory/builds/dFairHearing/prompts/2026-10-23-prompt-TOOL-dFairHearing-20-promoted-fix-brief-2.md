**Serves:** research TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23

# Promoted-units fix brief, part two — one writer per unit, each its own files only

Read `memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md` first: its sections 1 (token hits) and 3 (one departure record per added unit, its fields and its file name) bind you. Do only YOUR unit's row below, the unit your handoff names, and touch no other unit's files. The specs are uncommitted at rev-1 and unaudited: edit in place, no rev bump. Do not commit, stage, or run the build-index generator or any gate.

- **TOOL-dFairHearing-20** — write its departure record, `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-20-deviation-201.md`. Its spec has no token hit; leave it alone.
- **TOOL-dFairHearing-21** — fix its one §6 hit: `tools/workflows/replay_scorer.py`, not tracked by git ls-files (cite it by basename in §6). Write `…-TOOL-dFairHearing-21-deviation-211.md`.
- **TOOL-dFairHearing-22** — fix its one §6 hit: `tools/workflows/spec-audit-optin.js`, not tracked by git ls-files (cite it by basename in §6). Write `…-TOOL-dFairHearing-22-deviation-221.md`.
- **TOOL-dFairHearing-23** — its departure record exists; do not touch it. Two fixes:
  - **The `[bar]` hit.** §6 names `agent-cap.test.sh` as an acceptance observation. A bar or suite is never one: observe the checker on a staged break, a `--selftest` flag or a fixture instead, and name the suite on a `New arm:` line in §7.
  - **The size.** The file is 48995 bytes on disk, CRs included, against the 49152 ceiling the size join measures. Its generated `gen:spec-records` region grows by a row of about 500 to 600 bytes for each record that will name it: the round-2 audit record, the departures report and the closing records. Bring the file to at most 46000 bytes on disk. Tighten prose and drop repetition, keeping every finding id, criterion, red case, fork and `New arm:` line. If that cannot reach 46000, split it under build method M4: the second batch unit a second batch unit under the next free id, admissible ONLY when the minors fall into two disjoint write sets. Report which finding ids and product paths each half holds. Report the final byte size from `wc -c`.
