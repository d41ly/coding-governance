**Serves:** research TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29

# The promoted-fix pass's return — dRankedPlan round 1

The gov-spec-writer return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-1-spec-writer.md`, over `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md`, extracted from its transcript by script, never retyped.

I fixed all 21 hits in place, in §6 of each spec. All 10 promoted specs are edited:

- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-19.md
- through ...-TOOL-dRankedPlan-26.md
- ...-TOOL-dRankedPlan-28.md
- ...-TOOL-dRankedPlan-29.md

No status header, `**Carries:**` line, §3 edge, §7 `New arm:` line or §8 mark changed, and the full paths are still in §2, §4 and Files touched. I committed nothing.

I couldn't re-run `check-spec-tokens.py`: the scratch guard blocks this role from running that gate. In its place I ran my own probe over each spec's §6, using the checker's path-shape rule (`check_path_shaped`) and the selftest pattern from its `BAR` regex, and it reports nothing. Bare basenames like `ratify.py` aren't graded here, because the checker only grades bare names when its tool root is blank, and here it's `tools` (`check-spec-tokens.py:1500-1503`, `:300-312`).

| Unit | Hit | Change |
|---|---|---|
| TOOL-dRankedPlan-19 | `tools/loop/ratify.py` | AC1 and AC4 now run `python ratify.py …` |
| TOOL-dRankedPlan-19 | `help/plan.md` | AC5: `grep -n "item.plan.record" plan.md` "runs over the help page" (line rewrapped) |
| TOOL-dRankedPlan-20 | `tools/loop/scenario.py` | AC1 now runs `python scenario.py --fixture --plant plan-patch` |
| TOOL-dRankedPlan-20 | `help/loop.md` | AC4: `grep -n "Scenario: none" loop.md` runs over the help page |
| TOOL-dRankedPlan-21 | `tools/loop/ratify.py` | AC1's two commands now run `python ratify.py …` |
| TOOL-dRankedPlan-21 | `help/plan.md` | AC4: the `--exited` grep reads `plan.md`, which runs over the help page (rewrapped) |
| TOOL-dRankedPlan-22 | `tools/loop/ratify.py` | AC1 and AC3 now run `python ratify.py …`. AC2 says it lists "two paths, the loop kit's `ratify.py` and the memory-tree kit's `triage.py`, as S1 spells them" |
| TOOL-dRankedPlan-22 | `tools/memory-tree/triage.py` | AC1: "the planted caller at the memory-tree kit's `triage.py`". AC2 as in the row above |
| TOOL-dRankedPlan-22 | `tools/loop/README.md` | AC4: `grep -n "check-callers" README.md` runs over the loop kit's README |
| TOOL-dRankedPlan-23 | `tools/loop/plan_revision.py` | AC1 now runs `python plan_revision.py --selftest --plant fallback-disposition`. AC4's grep reads `plan_revision.py` over the loop kit's file |
| TOOL-dRankedPlan-23 | `help/loop.md` | AC5: the grep reads `loop.md` over the help page |
| TOOL-dRankedPlan-24 | `tools/loop/ratify.py` | AC1 now runs `python ratify.py --fixture --plant terminal-reentry` |
| TOOL-dRankedPlan-25 | `tools/loop/ratify.py` | AC1 now runs `python ratify.py --fixture --plant fallback-reentry` |
| TOOL-dRankedPlan-25 | `help/plan.md` | AC3: the grep reads `plan.md` over the help page |
| TOOL-dRankedPlan-26 | `tools/loop/ratify.py` | AC1 now runs `python ratify.py --fixture --plant holding-ask` |
| TOOL-dRankedPlan-28 | `tools/memory-tree/record_kinds.py` | AC1 now runs `python record_kinds.py --selftest` |
| TOOL-dRankedPlan-29 | `[bar]` `tools/drift-audit/selftest.py` | AC16 now reads: a probe imports `drift_report` and calls `build_live_builds_without_activity` over a planted `LIVE.md` with one `dormant` and one `paused` row; the result reads `unjudgeable` 0, `disposed` 1, `value` 1 and `of` 1, following S20. The README grep part is unchanged, and the suite stays on its existing §7 `New arm:` line |
| TOOL-dRankedPlan-29 | `tools/loop/loop.toml` | AC7: the grep reads `loop.toml`, which runs over the loop kit's table |
| TOOL-dRankedPlan-29 | `tools/workflows/review_pin.py` | AC14: the grep reads `review_pin.py` over the workflows kit's file |
| TOOL-dRankedPlan-29 | `memory/PLAN.md` | AC19: "the plan view `PLAN.md` under `memory`" |
| TOOL-dRankedPlan-29 | `tools/ok.py` | AC15 and AC28 now say "the planted in-tree file `ok.py` under `tools`". AC28's `Scope:` token is split so `../z` stays as its own token, and the line is rewrapped |

`check-memory-hygiene.sh --only 2,12,25` exits 0 with no finding. The dRankedPlan lines it prints are the informational "check 25 did not grade … READER NOT IN TREE" kind. They fall on specs 2, 3, 10, 16, and on 29's §2 S18, none of it text I edited. The main loop still needs to re-run `check-spec-tokens.py` to confirm the hits are cleared.
