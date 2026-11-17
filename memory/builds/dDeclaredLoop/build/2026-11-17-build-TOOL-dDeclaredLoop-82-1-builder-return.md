**Serves:** journal TOOL-dDeclaredLoop-82

# Builder return — TOOL-dDeclaredLoop-82, dispatch 1: the widened conf-name rule finds eight plant descriptions outside the fixture boundary

## Why

DIVERGENCE: if S10 is built as written, the `no-own-conf-read` plants of both loop modules go red. Spec §4 "Evidence", §5 "The sweep" (its first two derive_conf_reads rows) and AC1's base probe each say this cannot happen, and at HEAD 8efa0fb0f it does.

What the spec claims:
- §4 "Evidence": "A probe of S1 and S10's rule, with 80 S1's boundary, over the two modules finds no reader call, no conf name mid-string and no conf constant".
- §5 "The sweep": "the tip's live hits all sit inside 80's boundary".

What the base probe found: I ran the widened rule (S1's conf constant, S10's conf name anywhere in a string, alias-resolved reader calls, 80's boundary, 82 S8's docstring set) over tools/loop/budget.py and tools/loop/breakpoints.py at the base, before any edit. It finds 8 `conf name` hits, all at module level and all outside the boundary. Each one is a description string in the module's own `PLANTS` dict that spells `.unattended.conf` or `.memory-tree.conf` mid-string:
- budget.py: the `unattended-root`, `confs-disagree`, `root-source`, `unset-driver-root`, `trailing-slash-agree` and `no-confs` descriptions (6 hits). Units 72, 75, 76 and 79 added them.
- breakpoints.py: the `unattended-root` and `confs-disagree` descriptions (2 hits).
- No reader call and no conf constant: loop_lib.py binds no conf-named constant.

Both `no-own-conf-read` plants end in `check(not hits)`, so the widened rule newly reds `loop budget fixtures` and `loop breakpoint fixtures`. breakpoints.py is also missing from §4 "Files touched", so this pass cannot fix its two strings.

What the spec has to say: pick one of these, and state it in Scope and Files touched.
- (a) Reword the 8 descriptions so each names its conf without the dotted file name, adding tools/loop/breakpoints.py to Files touched. The new `conf-read-forms` description owes the same.
- (b) Narrow S10's anywhere-in-a-string rule so plant-description prose is passed over, and say how.
- (c) Some other exclusion the spec writer prefers.
Then restate the Evidence line and the two sweep rows.

Stale figures for the same revision (figures only, no design claim):
- tools/run-gates/selftest-budgets.txt now reads `loop budget fixtures` 498, `loop guard fixtures` 95 and `loop position fixtures` 432, where the sweep pins 476, 90 and 411.
- memory/project/positional-refs.txt holds 1 row for this spec, not 9.
- The sweep's guard.py grep for `unparseable-parent|conflict-elsewhere` counts 5, not 0, because unit 75's `push-merge-conflict-elsewhere` plant matches it.
- §4 "Evidence" still spells the old name `write_pre_placement_tree`; unit 80 renamed it to `write_pre_placement_plant`.

Every other claim I checked held at HEAD:
- 75 S27's exit-1 `absent` reading in `read_remerge_policy`.
- `check_push_range`'s `does not parse at parent <sha8>` refusal in its parents' grade.
- `scan_glob_readers`' inline docstring set and its eight owed names.
- 74's `no line for main of origin` skip.
- Both live modules import from loop_lib.
- The README `derive_conf_reads` row and the kit.toml reach comment that S24 edits.
- The budgets: lexicon pin 1215, SHARED_RECORDS and the driver's ceiling 343.

Nothing was written under the repository: no product edit, no dispatch and no commit, so no restore patch was needed. I did not run `--brief`, because RUN.md already holds its row (2026-11-17T03:29:05Z) for this brief path, and a second run would leave RUN.md changed with no commit to carry it.

## Summary

I stopped before the first write and committed nothing. The base is 8efa0fb0fb41f2545764ad974213b21f9f68f3a5.

**Check that ran:** AC1's own first step, the base probe. It is a python reimplementation of the widened derive_conf_reads rule, using HEAD's `derive_fixture_boundary`, run over tools/loop/budget.py and tools/loop/breakpoints.py. It stands in for the `no-own-conf-read` plants that the `loop budget fixtures` and `loop breakpoint fixtures` legs run. Script and output are in the scratchpad:
- C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/u82/probe_widened.py
- C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/u82/base-probe.txt

**Result:** 8 `conf name` hits outside the boundary, all in module-level `PLANTS` description strings (6 in budget.py, 2 in breakpoints.py). Both plants end in `check(not hits)`, so S10 as written newly reds both legs. That contradicts the spec's §4 "Evidence" and §5 "The sweep", and breakpoints.py is not in §4 "Files touched". The `why` field names three ways the spec could resolve it.

**Also reported for the same revision:** the stale figures (three budget rows, the positional-refs count, the guard.py grep count) and the old `write_pre_placement_tree` name.

**Not done:** no gate, suite, `--selftest` or `--dispatch` ran, so there are no RED-first observations and no gotchas run over a commit. Once the spec is revised and rebuilt, the close still owes:
- AC21's `loop definition fixtures` runs at the pass commits of units 67, 79 and 80.
- The four `New arm:` lines of §7 (budget.py, guard.py, position.py, gen_build_index.py).
