# dSweptBranches — asks

## Asks
- TOOL-dSweptBranches-6 · filed 2026-10-13 · audit gov's memory-tree checks that read files a range ADDS, for the blind spot inCMS's memory-local check 21 has: it reads a merge of the default branch into a feature branch as adding every `memory/` file the default branch gained, while its sibling check 29 already skips merge commits. Gov's checks of the same shape, those listing `--diff-filter=A` over a commit range, should skip a merge's first-parent side or be shown not to need to · accept each gov check that lists additions over a range is named, with a fixture that merges the default branch into a feature branch, and is observed either to ignore the merged-in additions or red before its fix
- TOOL-dSweptBranches-18 · filed 2026-10-13 · held red: suite process-monitor census selftest red at 37200355 on the daily held job, run 38247412830 · seen `{prefix}/process-monitor/selftest.py`@37200355 run `python {prefix}/process-monitor/selftest.py` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dSweptBranches-22 · filed 2026-10-13 · two staged-set readers read a merge of the default branch as additions (the TOOL-dSweptBranches-20 audit): `tools/hooks/scratch-guard.js` exempts a commit that adds a prompt-authorized build README from the kickoff gate, so a merge bringing one in is exempted too; `read_pinned_base` in `tools/unattended/unattended.sh` reads a staged run-state archive as a rotation in doubt, so a merge staging this build's archive refuses a landing. Both should skip what the merge's other side already holds (MERGE_HEAD present: read only paths whose staged blob differs from MERGE_HEAD's) · accept each site's suite carries an arm that stages a merge of the default branch bringing the file in, observed red before its fix: the guard still gates that merge, and the pinned base reads no doubt

## Dispositions
- SEV · TOOL-dSweptBranches-6 · MED · a false refusal on every feature branch that merges the default branch in, which is the reconcile this build's skill recommends
- KEEP · TOOL-dSweptBranches-6 · the owner's prompt of 2026-10-13 files it as a separate ask rather than this run's unit
- SEV · TOOL-dSweptBranches-18 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dSweptBranches-18 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dSweptBranches-22 · LOW · a merge commit escapes the kickoff gate, or a rare landing refuses as a doubt; neither loses work
- KEEP · TOOL-dSweptBranches-22 · found by the TOOL-dSweptBranches-20 audit; its fix edits two kits that unit put OUT
