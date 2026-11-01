**Serves:** research TOOL-dRankedPlan-38 TOOL-dRankedPlan-41 TOOL-dRankedPlan-45

# The promoted-fix pass's return — dRankedPlan round 3

The gov-spec-writer return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-38-1-spec-writer.md`, over `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-38-promoted-fix-brief.md`, extracted from its transcript by script, never retyped.

I fixed all three hits in place in specs 41 and 45. Unit 38 had no hit, so its spec is unchanged. Every `**Carries:**` line, §3 edge and §8 mark is unchanged, as are the status headers, and nothing is committed.

**Hit 1: check 25 on `-41.md` and `-45.md`.** Neither item retires anything, so I reworded both rather than adding a `**Readers:**` clause.
- **41 S3:** "Quote characters are removed from a word before it is compared with `ratify.py`…" now reads "A word is compared with `ratify.py`, an interpreter name or a mode flag with its quote characters stripped." It describes stripping quotes, not retiring a name.
- **45 S20:** Two retirement words were present. "deleted" became "taken out of the tree". The other is "replaced", inside the plant name `replaced-in-one-commit`. I kept that name because the audit's fix names it. What fired the check was the backticked function name next to those words, so I now cite the gate by unit instead: "The held line of Plan's exit gate (`TOOL-dRankedPlan-10` S4) names the stale record…". I also rewrapped one long line there.

**Hit 2: check-spec-tokens `[bar]` on `-45.md` AC8.** The dispatch probe on `.githooks/pre_push_bar_selftest.py` is now a fixture. A second run of `caller-heredoc-argv` plants only a `.py` hook whose one mention of `read_plan_ratification` is in its docstring, and the check exits 0. This tells the two readers apart: the Python reader only counts real references to the name (unit 32 S1), while the shell reader's textual rule (unit 38 S1) would refuse that line. A plain call in a `.py` hook would not tell them apart, because both readers refuse it.
- S32 now names that second run.
- I updated the `tools/loop/ratify.py` arm's staged-break wording in §7 to "skips bound names and heredoc bodies and reads a `.py` hook as shell". That arm already covered AC8.
- I added no `New arm:` for `pre_push_bar_selftest.py`, because this unit adds no arm to that suite.

**Hit 3: check-spec-tokens `[guards]` on `-45.md`.** The unit really does edit `tools/gate-legs.json` (S6 adds the ceiling, S18 widens the guards), so I added `run-gates canary`, spelled as `tools/gate-legs.json` names it, to the §7 leg line before `run-gates gov canary`.

**Checks:**
- **Hygiene:** `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exits 0. The only lines naming dRankedPlan files are "did not grade … READER NOT IN TREE" notes on the earlier committed specs 2, 3, 10, 16 and 29, none of which I touched.
- **Check 25 trigger, run directly:** I copied its trigger functions into a scratch script and ran them over specs 38 to 45. Before the edits it fired on 41 S3 and 45 S20, and after them on nothing.
- **First hygiene run:** my first run also exited 0, but that was piped through `tail`, so it doesn't count as a clean result from before the edits.
- **check-spec-tokens:** not run by me. You said you would re-run it.

**Possible extra guards hit:** specs 41 and 45 both touch `tools/lib/extract_code.py`. The `run-gates canary` guard includes `{prefix}/lib/`, and spec 41's §7 does not name that leg. Your hit list didn't flag it, so the guard check may not match that path. If your re-run reports it, spec 41 needs the same addition.

Files changed:
- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-41.md
- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-45.md
