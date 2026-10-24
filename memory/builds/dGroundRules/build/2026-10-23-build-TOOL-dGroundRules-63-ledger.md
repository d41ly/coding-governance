# TOOL-dGroundRules-63 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-63

No merge bar, no gate leg and no self-test suite ran in this pass. Every premise of the spec's §4
held at `d56a864be`: `TERMINAL`, `scan_live_run`, `read_landed_derivation` and `cmd_check` sit in
the packet instrument as cited, `main` returns 2 on `Unmeasured`, 22 chain builds hold a packet and
four a `RUN.md` (dGroundRules `BUILDING`; dFairHearing, dSafePassage and dTrueNorth `LANDING`), and
`packet.py --check dGroundRules` printed `byte compare green` both before and after this unit's
status flip. The join derives the instrument from the one tracked `*-build-<id>-packet.py` under
dClosedLoop's `build/` folder rather than spelling its path, since that path carries the id of a
live spec and a `tools/` file spelling it is cited as product source by drift-audit's held signal.
`SCRATCH` was a `git clone` of this branch under `%TEMP%/gr63` with this unit's working tree
committed on top as `2d56d6349`, the staged tree of this commit less this ledger; each staging was
committed in the clone and reset after. Observations marked "worktree" were taken on the staged
tree of this commit before it was written. Owed at the close: the `New arm:` line's two arms in
`tools/check-spec-tokens.test.sh`, observed RED on a staged break and GREEN restored, and the §7
legs.

**Evidences:** TOOL-dGroundRules-63
- AC1 — `LIST` on the worktree printed `spec-tokens: source join · 0 sourced file(s) examined in 0 live spec(s) · 0 by bare name` and no `[source]` hit; in `SCRATCH` with `PLANT_BARE` staged it printed `HIT    [source] memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-63.md :: helper.sh` and the count line `1 sourced file(s) examined in 1 live spec(s) · 1 by bare name`, the red case.
- AC3 — `BARE_STATUS` in `SCRATCH` at `2d56d6349` printed one line, `TOOL-dGroundRules-34 CLOSED lib-unattended.sh`; with `PLANT_BARE` staged it printed a second, `TOOL-dGroundRules-63 INPROGRESS helper.sh`, the red case.
- AC4 — with `RUN_LIVE` and `STALE` committed, `LIST` in `SCRATCH` printed `HIT    [packet] memory/builds/dGroundRules/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md :: dGroundRules — packet.py --check exited 1: packet: dGroundRules · … · byte compare red · completeness 0 findings …`.
- AC5 — with `RUN_LIVE` alone, `LIST` in `SCRATCH` printed `spec-tokens: packet join · 1 live chain run(s) · 1 packet(s) checked` and no `[packet]` hit.
- AC6 — with `RUN_DONE` and `STALE` committed, `LIST` in `SCRATCH` printed `spec-tokens: packet join · 0 live chain run(s) · 0 packet(s) checked` and no `[packet]` hit.
- AC7 — `LIST` on the worktree printed `spec-tokens: packet join · 1 live chain run(s) · 1 packet(s) checked` and no `[packet]` hit, exit 0.
- AC8 — `grep -c "forty-one" memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md` printed `0`, and `grep -c "TOOL-dGroundRules-65 and TOOL-dGroundRules-14 to TOOL-dGroundRules-52"` over `RECORD` printed `1`.
- AC9 — `ROSTER_JOIN` printed `51 51` and nothing else.
- AC10 — `DEFER_WORDS` printed `0`.
- AC11 — `grep -c "TOOL-dGroundRules-1 to TOOL-dGroundRules-11"` over `RECORD` printed `1`.
- AC12 — `grep -c "TOOL-dGroundRules-46" memory/gotchas/observation-before-the-last-fold-of-the-same-commit.md` printed `1`, and `python tools/memory-tree/gotchas.py --check` exited 0.
- AC13 — `grep -c "id range" memory/gotchas/two-answers-to-one-question.md` printed `1`.
- AC14 — `grep -c "scan_live_packets" memory/map/generated/symbols.json` printed `1` on the regenerated map, committed in this pass commit, and `python tools/codebase-map/gen_map.py --check` exited 0.
