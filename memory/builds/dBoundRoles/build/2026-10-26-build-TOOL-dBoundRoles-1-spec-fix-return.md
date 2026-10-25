**Serves:** research TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26

# Spec fix pass — dBoundRoles, its return

The return of the agent dispatched from `memory/builds/dBoundRoles/prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-1-spec-writer.md`, run direct/aedfe0f13e4e7108b, extracted from its transcript by script.

I made every fix in the brief, but the spec-tokens check has not been re-run. The scratch-guard hook stopped me running `check-spec-tokens.py`, because that gate is outside my role's allowance. So F3 to F6, the spec-tokens findings, still need that check run in the main session.

What I did check: in a throwaway clone with every dBoundRoles spec and record committed, I ran `gen_build_index.py --write` and then `check-memory-hygiene.sh --only 2,12,25,30`. It exited 0. The edge joins are switched on there (`SPEC_EDGES_CUTOFF` is set), and check 30 reported "as-built clean · 663 deviation records". I deleted the clone afterwards. Nothing is committed and every spec stays `rev-1`.

**Files changed** (all under `C:\projects\coding-governance\.claude\worktrees\unattended-dboundroles-a396a1\memory\builds\dBoundRoles\`)
- `spec\2026-10-25-spec-TOOL-dBoundRoles-3.md` — F1: added hands-off TOOL-dBoundRoles-23 naming `### item`, `### inputs`, `### allowance`, `### return`, `### witness`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-4.md` — F3: re-pinned to `cl-dClosedLoop-0169@60524f05`; added §8 F4, naming deviation-41 and the `PLAY-dClosedLoop-30` disagreement.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-6.md` — F1: the role index's keys now read `layer`, `acts-as` and `shapes`, citing unit 1 §8 F4. F4: added `check-wiring self-test` and `lexicon naming predicates`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-7.md` — F3: re-pinned to `cl-dClosedLoop-0172@d88edbe8`; added §8 F5, naming deviation-71 and `PLAY-dClosedLoop-30`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-10.md` — F3: re-pinned to `cl-dClosedLoop-0175@0d300fb9`; added §8 F4, naming deviations 101 and 102 and `PLAY-dClosedLoop-30`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-11.md` — F4: added `check-wiring self-test` and `recall floor arms`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-13.md` — F4: added `check-wiring self-test` and `lexicon naming predicates`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-14.md` — F1: added hands-off TOOL-dBoundRoles-19 naming `role.<slot>`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-15.md` — F4: added `check-wiring self-test` and `lexicon naming predicates`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-17.md` — F4: added `recall floor` and `recall floor arms`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-18.md`:
  - F5: AC6 now spells `tools/roles/house/gov-diff-reviewer.md` and cites the new file only by its basename `gov-reviewer.md`.
  - F6: AC7's expected grep output now describes the self-test module as "govkit's self-test module, whose `reviewer-merge-` cases (§7's New arm) spell the old stems". Its suite is already on §7's `New arm:` line.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-19.md` — F1: added consumes-from TOOL-dBoundRoles-14 naming `role.<slot>`. F4: added `check-wiring self-test`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-20.md` — F1: added consumes-from TOOL-dBoundRoles-15 naming `budget`, and hands-off TOOL-dBoundRoles-25 naming `harnesses`.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-21.md` — F5: AC5 now describes the plant as a role file named `default` in a scratch copy's role-file directory, with no path shape.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-24.md` — F6: AC2's fixture line no longer names `adopt-roles.test.sh`; it points to §7's existing New arm.
- `spec\2026-10-25-spec-TOOL-dBoundRoles-25.md`:
  - F1: added consumes-from TOOL-dBoundRoles-20 naming `harnesses`.
  - F6: AC8 now pipes each payload in the ledger into `node spawn-guard.js` and checks its exit, instead of comparing labels between the two suites.
  - F6: AC14 now describes the self-test module in words. `spawn-guard.test.sh` was already on §7's New arm.
  - F6: the retired `tools/hooks/agent-cap.test.sh` is now listed in S8's `**Readers:**` clause. It does name `agent-cap.js` (10 hits).
- `spec\2026-10-25-spec-TOOL-dBoundRoles-26.md` — F4: added `check-wiring self-test`.
- `build\2026-10-25-build-TOOL-dBoundRoles-10-deviation-102.md` — F2: added `- **Supersedes:** 2026-10-25-build-TOOL-dBoundRoles-10-deviation-101`. Its **After:** is now the whole clause with both the `driver.reads` and `roles.no-spawn` changes, on one line with no `|`. I left deviation-101 as it was.

**F1's last bullet:** I added an edge between units 20 and 25, both ways, naming `harnesses`. Unit 25's moved `checkHarnessCall` matches against the role index's held-harness list, and unit 20's composition renders that list (unit 20 §4 "Harness paths in the install", and its table row for the spawn guard).

**Unit 10's pin:** re-pinned to `0d300fb9`. That is the hash the clone's regenerated view gives `cl-dClosedLoop-0175` once deviation-102 heads the set, and it matches the sha256 of 102's new **After:** text.

**Two follow-ups for the main loop:**
- **Spec tokens:** run `python tools/check-spec-tokens.py` to confirm F3 to F6 are clean.
- **As-built view:** this worktree's copy of `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` still shows clause 0175 at its baseline text, so unit 10's new pin looks stale until it is regenerated. As the brief said, I ran the generator only in the clone.
