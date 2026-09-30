# dAlignedCarrier — asks

## Asks

- TOOL-dAlignedCarrier-7 · filed 2026-09-30 · THE VERB CONTRACT'S `--status` ENTRY NAMES FIELDS THE VERB HAS OUTGROWN. `tools/unattended/VERBS.template.md` enumerates what `--status` prints, and TOOL-dAlignedCarrier-4 added two fields, the pinned-asks verdict and the holder-worktree verdict, which the entry does not name. No mandated accept clause names that carrier, so the build method's veto 2 kept this run from editing it. Declined under the unattended protocol's section 11. · seen `tools/unattended/VERBS.template.md` matching `one line: the phase, the first non-terminal unit` · accept the `--status` entry in `tools/unattended/VERBS.template.md` and its render name the pinned-asks and holder-worktree fields, and the unattended kit gate is green
- TOOL-dAlignedCarrier-8 · filed 2026-09-30 · inherited red: leg memory-recall kit selftest red at 87c245b3, introduced by 78c4bf7d · seen `tools/memory-recall/selftest.py`@87c245b3 run `python3 tools/memory-recall/selftest.py` · accept the leg is green at the default branch's tip → 78c4bf7d
- TOOL-dAlignedCarrier-9 · filed 2026-10-01 · AN IN-PLACE CLOSE THAT AUTO-FILES AN INHERITED-RED ASK CANNOT COMMIT ITS OWN RECORD. The gates-green arm stages the ask row in the build's BACKLOG.md and re-renders nothing, so `write_close_commit` meets the pre-commit's hygiene check 9 on the stale generated views and fails check 69 after the whole flagged bar was paid. Met at this build's close on 2026-09-30, and recovered by rendering the views and making the same commit by hand. Declined under the unattended protocol's section 11. · seen `tools/unattended/unattended.sh` matching `could not commit its own record` · accept an in-place close that auto-files an inherited-red ask commits `records(<slug>): close — LANDING` with the generated views re-rendered in that commit, observed on a fixture whose bar leaves one inherited red

## Dispositions

- SEV · TOOL-dAlignedCarrier-7 · LOW · a reader of the verb contract does not learn two fields `--status` now prints
- KEEP · TOOL-dAlignedCarrier-7 · declined under the unattended protocol's section 11; wanted after this build closes, an owner call under veto 2
- SEV · TOOL-dAlignedCarrier-8 · HIGH · a merge-bar leg is red on the default branch
- KEEP · TOOL-dAlignedCarrier-8 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dAlignedCarrier-9 · MED · an evaluated close fails to travel and costs a hand recovery or a second bar
- KEEP · TOOL-dAlignedCarrier-9 · declined under the unattended protocol's section 11; wanted after this build closes, outside its goal
