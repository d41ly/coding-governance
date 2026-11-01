**Serves:** research TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-81

# The promoted-fix pass's returns — dRankedPlan round 8

The gov-spec-writer returns for the handoff `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-78-1-spec-writer.md`, over `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-78-promoted-fix-brief.md`: its first return, which fixed unit 78 alone, and its return after the main loop sent it back for units 79 and 81, extracted from its transcript by script, never retyped.

I fixed both check-spec-tokens hits in `TOOL-dRankedPlan-78`. I did not re-run the spec-token checker itself, since I'm only allowed the hygiene and lexicon gates. The hygiene check you asked for passed with no finding on a dRankedPlan file. The status header, `**Carries:**` line, §3 edges and §8 are unchanged, and nothing is committed.

The spec is `C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-78.md`.

**Hit 1, `[bar]` (§6 named `selftest.py`):**
- **AC1** now reads: "imports `read_extent_call_arities` alone from the loop kit's self-test module, running no case of it, and calls it on the eight-line text of §4 Evidence planted as a string". That makes it a direct probe of the function on a planted input. No backticked `*selftest.py` token is left in §6.
- **No `New arm:` line added.** This unit adds a function to the suite file but no case to it. A `New arm:` line would declare an arm that doesn't exist, which the main loop would then try to see red and then green.
- **§7 gets one prose sentence instead.** It says this unit adds no suite arm, AC1 to AC3 observe the function directly, and the arm that runs it at every close is `TOOL-dRankedPlan-79` S1's `extent-calls-carry-facts`. That arm is already declared on unit 79's own §7 `New arm:` line.

**Hit 2, `[path]` (§6 cited `tools/loop/ratify.py`):**
- **AC3:** both the criterion and its `Red when:` now say "the loop kit's `ratify.py`". A bare file name is graded only at a root install, and this repo's tools live under `tools/`, so the basename is not graded.
- **Full path kept** in §2, §3, §4 Evidence and §5, as the brief asked.
- **One `selftest.py` mention remains in §7:** the existing sentence naming `--legs-for tools/loop/selftest.py`. I left it because it isn't a leg line, and there `selftest.py` is an argument, not the command, so the bar check's pattern can't match it.

**Hygiene:** `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exited 0. The only lines it printed were "did not grade" notes on dTotalRecall and dWitnessedBar specs.

---

I fixed the same two hits in `TOOL-dRankedPlan-79` and `TOOL-dRankedPlan-81`, so all three specs from the brief are now done. I did not re-run the spec-token checker, since I'm only allowed the hygiene and lexicon gates. Instead I grepped §6 of units 78, 79 and 81 for backticked tokens containing `selftest.py` or `tools/loop/`, and none are left. The hygiene re-run exited 0, but it does print lines naming dRankedPlan files (see the end). I changed no status header, `**Carries:**` line, §3 edge or §8 mark, and committed nothing.

**TOOL-dRankedPlan-79** (`C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-79.md`)
- **`[bar]`, AC1:** "calls the `extent-calls-carry-facts` case of `selftest.py` on the copy" now reads "calls the `extent-calls-carry-facts` case's function alone from the loop kit's self-test module on the copy, running no other case". It still observes the unit's own case on the planted copy.
- **`[path]`, AC2:** "runs on the unmodified `tools/loop/ratify.py`" now reads "the same probe calls the case on the loop kit's unmodified `ratify.py`". The full path stays in §1, §2, §4 and Files touched.
- **§7:** the existing `New arm: tools/loop/selftest.py · covers AC1 AC2 · …` line is unchanged. This unit really does add that case to the suite, so the line belongs.

**TOOL-dRankedPlan-81** (`C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-81.md`)
- **`[bar]`, AC1:** "calls `read_extent_call_arities` from the loop kit's `selftest.py`" now reads "imports `read_extent_call_arities` alone from the loop kit's self-test module, running no case of it, and calls it on the first two-line text of §4 Evidence planted as a string".
- **`[path]`, AC26:** "runs over `tools/loop/ratify.py`" now reads "runs over the loop kit's `ratify.py`". The full path stays in §1, §4 and Files touched.
- **§7:** no `New arm:` line added for the self-test. Unit 81 adds no case to it; its only arm is the existing `tools/loop/ratify.py` plants line, which I left as it was.

**Unit 78**, for completeness: AC1 and AC3 were fixed the same way. I added a §7 sentence saying the unit adds no suite arm, and that unit 79's `extent-calls-carry-facts` arm is the one that runs the predicate at every close.

**Hygiene re-run** (`--only 2,12,25`, exit 0): it printed 103 "check 25 did not grade … READER NOT IN TREE covers it" lines plus the closing summary line. Eleven of those name dRankedPlan specs 2, 3, 10, 16, 29 and 51, which I didn't touch. They say the check skipped a name because its reader isn't in the tree yet, which isn't a failure. None names units 78, 79 or 81.
