# Amendments and owner rulings — dRedressedBar, moved out of the README's rules slot

**Serves:** research TOOL-dRedressedBar-28

The build README's `## Build-level rules` slot grew to 7675 B against its 1800 B ceiling, one amendment per added unit, and the landing bar's `build README slot contract` leg refused it on 2026-10-16. The entries below are moved here unchanged and in their original order; the README keeps the rules that still bind and a pointer to this record. Every path below is relative to the build folder. The last entry is new.

- **Amendment (M2 ADD), 2026-10-14**: unit 8 added before the audit. Both canary attempts hung
  in arm 11g AC14, past the 13200 s ceiling: the arm's FIFO server exited on one failed open while
  its nested bar ran with no wall. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-8-brief.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 9 added before the audit, by the owner's resolution of
  unit 3's F1 as (c). A writing `govkit update` that gains `settings-merge` but leaves `agent-cap`
  out fails on settings-merge's adopter; the owner chose to fix it here rather than record it. Its
  brief is `prompts/2026-10-14-prompt-TOOL-dRedressedBar-9-brief.md`, and unit 3's revision record
  is `prompts/2026-10-14-prompt-TOOL-dRedressedBar-3-2-revision.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 11 added after the round-1 spec audit, by the owner's
  resolution of unit 10's F1 as (c). Unit 10 narrows settings-merge's accepted stop to two probed
  paths, and unit 11 adds a receipt-reading probe term to the declared-outcome contract, so a hook at
  a receipt-recorded home also refuses the false accept. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-11-brief.md`, and unit 10's revision record is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 14 added by the owner ("add the apply prefix defect"), the
  defect unit 11's writer measured. A first `apply` at a per-kit agent-cap prefix exits 1, because
  CONFIGURE runs before the receipt exists. It was drafted as unit 12 and re-id'd to 14 when the
  round-2 disposal claimed 12 and 13 in the same minute. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-14-brief.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 15 added by the owner's resolution of unit 14's F1 as
  (a). agent-cap's adopter argv runs `{prefix}/settings-merge.py` at agent-cap's own prefix, a file
  that kit never installed there. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-15-brief.md`, and the edge revisions are
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-14-2-revision.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 18 added by the owner: a gate profiler that runs every
  leg in `tools/gate-legs.json`, serially or concurrently under 80% CPU and 90% memory load. Each leg
  runs with no knob, no ceiling and every log kept, and is profiled down to each process it spawns,
  with stall detection that reports and never kills. It is ordered after every other unit. Its brief
  is `prompts/2026-10-14-prompt-TOOL-dRedressedBar-18-brief.md`.
- Write sets overlap on `tools/roles/adopt-roles.test.sh`, so order sequences them: units 1 and 8
  are disjoint from everything at step 1; units 2 and 9 both commit a regenerated
  `memory/map/generated/symbols.json` (the pre-commit codebase-map gate refuses a stale one), so
  they are built one after the other, never together; 3 follows 9, whose fix its three unscoped arms witness; 4 follows 1; 5 follows
  4; 6 follows 5; 7, the records and kit versions, is measured over the code units 1 to 6, 8 and 9
  leave. Units 10, 11, 12, 13 and 14 follow 7 in that order. Each touches only govkit-exempt files
  and adds no function, so none moves a kit version or the symbol index unit 7 regenerates. Unit 15
  follows 14, and because it moves the hooks kit's shipped bytes after 7, it bumps that version itself.
- **Owner ruling, 2026-10-14, the audit chain's end**: run spec-audit round 4 over units 16, 17
  and 18, then build. Every unit round 4 promotes is built from its spec as written, under a
  recorded override of `specs-audited` for those units only. No round 5 runs. Each round so far
  confirmed a new high plus about 22 minors at precision 1.00, 1.00 and 0.92, so the chain would not
  end on M4's precision floor. The closing diff review covers the promoted units' code.
- **Amendment (M2 ADD), 2026-10-14**: unit 20 added by the owner ("Fix the class") after unit 7's
  builder diverged. `govkit mint` let the `playbook` entry's version pattern rewrite a selftest
  fixture in `tools/playbook/render_playbook.py`, playbook-render's file, moving that kit's bytes
  without a bump. Unit 20 tightens the carrier writer so a pattern counts only inside its own entry's
  file group, at order 4, before unit 7. It is built from its spec under the same recorded override
  as round 4's promotions; no further audit round runs. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-20-brief.md`, and unit 7's revision record is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-7-2-revision.md`.
- **Owner ruling, 2026-10-15, the closing review's findings**: the round-1 closing diff review
  (`reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md`, CLEAN WITH FIXES, no
  blocker) confirmed 1 high, 7 mediums and 5 lows; the owner promoted all 13 into this build. Units
  21 (H1, the profiler's dead-run sweep), 22 (the profiler's M1, M2, M5, M7, L1, L2, L3 and L5) and
  23 (govkit's M3, M4, M6 and L4) follow unit 19 in that order, built from their specs under the same
  recorded override as round 4's promotions. Closing review round 2 reviews their fold. Their brief
  is `prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-brief.md`.
- **Owner rulings, 2026-10-15, H1's class**: unit 21 also takes the capture path's open, read and
  delete, and every Python fixed-name temp-then-replace writer under `tools/run-gates/`. Unit 21's
  F1 resolved as its own unit: unit 24 gives the 19 bash `mv` sites and the heredoc writer in
  `run-gates.sh`, `post-merge.sh` and `run-selftests.sh` unpredictable temps under a bash-side static
  check, after unit 23 and before the bar. Its brief is
  `prompts/2026-10-15-prompt-TOOL-dRedressedBar-24-brief.md`.
- **Owner ruling, 2026-10-15, the round-2 closing review**: the fold review
  (`reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md`, CLEAN WITH FIXES, no
  blocker) confirmed 2 highs, 6 mediums and 6 lows; the owner promoted all 14, "then stop". Unit 25
  takes the profiler's arms and guards (H1, M1, L1, L6), unit 26 the temp-name lint and the runner's
  temps (H2, M2, M3, M4, L2, L3, L4, L5), after unit 24 in that order. A round-3 review covers their
  fold; it fixes blockers only, and its other findings go to a follow-up build. Their brief is
  `prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-brief.md`.
- **Owner ruling, 2026-10-15, check 23**: the base bar's `memory hygiene` leg was red on check 23 as
  well as check 17, on ledger lines in builds aSparedSpawn and aOrientedCast that this branch never
  touched (`prompts/2026-10-15-prompt-TOOL-dRedressedBar-1-4-researcher.md`). The owner chose to fix
  them here. Unit 27, a records-only unit after unit 26, rewrites those ledger lines in a legal form
  and writes the acceptance ledgers units 2, 4, 5, 7, 9, 11, 18 and 20 never wrote. Its brief is
  `prompts/2026-10-15-prompt-TOOL-dRedressedBar-27-brief.md`.
- **Owner ask, 2026-10-16, the landing**: "land it without self tests". `push-main.sh --land` over
  the prepared merge `30466e129` refused: 3 of 71 legs red, all attributed OWN. The README slot
  contract and the kickoff manifest ratchet are fixed in records commits: this record, and a
  `last-audit` re-stamp after `tools/run-gates/run-gates.sh` moved. Unit 28, after unit 27, fixes
  the install-prefix leg's two kit-path spellings from units 10, 11 and 14. Its brief is
  `prompts/2026-10-16-prompt-TOOL-dRedressedBar-28-brief.md`.
