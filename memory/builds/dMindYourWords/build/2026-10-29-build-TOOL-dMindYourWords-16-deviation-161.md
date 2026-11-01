# TOOL-dMindYourWords-16 deviation 161 — the marginal offense rate moves with the two lexicon drift signals

**Serves:** deviation TOOL-dMindYourWords-16

- **Departs from:** `cl-dClosedLoop-0277@11ec04ed`
- **Hand-off:** design-to-spec
- **Before:** the two lexicon drift signals as the lexicon's own leg pack, registered at Test's leg-pack point
- **After:** the two lexicon drift signals as the lexicon's own leg pack, registered at Test's leg-pack point, and the report-only marginal offense rate moved into the lexicon kit with them, so drift-audit's engine imports nothing of the lexicon
- **Cause:** design defect
- **Reason:** The clause names two signals, and gap-lex-08, which it closes, complains that they reach the bar "through drift-audit's engine, which imports the optional lexicon kit". Source shows three signals importing the kit, not two: `build_lexicon_marginal_offense_rate` resolves and imports the lexicon the same way the two gateable signals do. Moving only the two leaves drift-audit importing the optional kit, so the gap's complaint stays true. TOOL-dMindYourWords-16 §8 F1 settled it by the plan's rung 3, the most feature-rich survivor: all three move, the rate staying report-only. The clause's text is unchanged and still carried whole, because the two signals it names do move; the third is scope added beside it.
- **Evidence:** the three imports, `tools/drift-audit/drift_report.py:1205`, `:1272` and `:1474`, at `ba8b3c8c`; the engine's own docstring calling the signals "the ONLY place this shipped engine names an optional kit", `drift_report.py:1186-1188`; scout C's disagreement 4, `memory/builds/dMindYourWords/build/2026-10-29-build-TOOL-dMindYourWords-11-reuse-scout-c.md:23`; the gap, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:263`; the fork, `memory/builds/dMindYourWords/spec/2026-10-29-spec-TOOL-dMindYourWords-16.md` §8 F1; rung 3, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:910`
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of dMindYourWords' spec run, under the chain's `author-recorded` value (README rule 5); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0277@11ec04ed
- **Caused-by:** TOOL-dMindYourWords-16
