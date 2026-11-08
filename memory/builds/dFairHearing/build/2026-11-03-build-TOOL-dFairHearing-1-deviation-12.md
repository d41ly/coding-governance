# TOOL-dFairHearing-1 deviation 12 — replays 3 and 4 render each finding's text from the committed reports, the finders' returns being gone

**Serves:** deviation TOOL-dFairHearing-1

- **Departs from:** TOOL-dFairHearing-1@rev-5 [§4 The other three replays]
- **Hand-off:** spec-revised
- **Before:** at rev-5, replay 3's synthesis runs under `addressTwins: 'shown'` "over each run's verified findings and refuted claims", read as the finders returned them, and replay 4's skeptic is handed round 1's finding #23 and the control's as the find stage returned them; the spec names no source for a finding's claim, impact, fix or evidence.
- **After:** at rev-6 (`20fe70ba2`), §4 Twins and Fix verdict name a committed source for every field the harness renders: a confirmed finding's claim, impact and fix from the report item whose heading holds its id, a refuted finding's claim from its appendix `reason` with an empty impact and fix, #23's and the control's from their round-1 report items by the labels those reports use, every other field from the appendix row, and evidence the empty string; the harness renders the prompt itself under stub agents, and the probe stops on an id whose lens and ref differ from its appendix row.
- **Cause:** builder discovery
- **Reason:** the runtime-a and runtime-b appendices carry `id`, `lens`, `ref`, `severity`, `skepticSeverity`, `verdict`, `reason`, `fixVerdict` and `classes`, never a claim, impact, fix or evidence; refuted A14, A45, A46, A59 and B61 appear nowhere else in either report; the runs' find and verify files are on no node; and aRoutedQuill round 1's row 23 has only its item B1's prose. Re-running the find stage would mint new ids, so the ids AC7 names would not exist, and judging from the SAME-ADDRESS PAIRS block alone fails AC7's negative pair, so §8 F7 (a) is the one option meeting AC7 and AC8. The carried clause names only "the synthesis with twins shown" and "#23's fix re-judged by class", which the stand-in still runs. It relaxes what replays 3 and 4 test: a synthesizer and a skeptic reading report prose and the skeptic's refutation reasons in place of the finders' returns.
- **Evidence:** the second builder return, `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-2-builder-return.md`; TOOL-dFairHearing-1 §8 F7 and §4 Twins at rev-6; the appendix header of `memory/builds/dClosedLoop/reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md`; the staged inputs this pass rendered under rev-6, `2026-11-03-build-TOOL-dFairHearing-1-replay-3-synthesis-a`, `-b`, `2026-11-03-build-TOOL-dFairHearing-1-replay-4-skeptic-23` and `-control`.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of dFairHearing's build run, resolving §8 F7 by BUILD-METHOD M3 under the run's standing mandate, recorded in TOOL-dFairHearing-1 §8 F7 at rev-6
- **Follow-through:** usage builder-divergence
- **Caused-by:** TOOL-dFairHearing-1
- **Bound:** rev-5's §4 Twins text, "over each run's verified findings and refuted claims", read as the finders returned them
- **Tier:** weakest, a reach the spec read into the clause beyond its text
