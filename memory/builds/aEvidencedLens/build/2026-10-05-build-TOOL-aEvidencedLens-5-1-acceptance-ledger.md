# TOOL-aEvidencedLens-5 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-5

The build harness hands the audit its context, sibling specs, checklist and prior findings. The pass
commits `3c1e70373` and `32645a03d` record no direct-check figures beyond the second's statement that
its new token arm read RED against the unrendered template. Every criterion below is therefore read
from the main loop's VERIFYING run of the unattended-build self-test in a frozen clone at `0c8dd1761`,
whose `tools/` matches `5a1643c8d` except the tier2-review rubric extractor: rc 0, `PASS (610
assertions)`, and every `EL5-AC<n>` arm named below printed `ok`. The arm labels are the observation;
where a criterion names text the label does not show, that is said. AC8's greps were re-run on the
tree at `5a1643c8d`.

**Evidences:** TOOL-aEvidencedLens-5
- AC1 — `context` — `EL5-AC1 the callee is handed scratch`, `...a context naming the build README`, `...and the run mandate's directory` and `...and specs: the format, then the siblings not under audit` each printed `ok`.
- AC2 — `gotchas.py --for-paths` — `EL5-AC2 the resolver's checklist reaches the callee verbatim`, `EL5-AC2 the resolver is told to run gotchas.py --for-paths` and `...over the subjects' Files touched (estimate) paths` each printed `ok`.
- AC3 — `checklistError` — `EL5-AC3 a checklistError is announced by its reason`, `...and no checklist key reaches the callee`, `EL5-AC3 a header-only checklist is announced as no bug class selected`, `...and never reaches the callee, whose parseChecklist refuses it`, `EL5-AC3 a caller-pinned subject set passes no checklist key` and `...and announces that no resolver ran` each printed `ok`.
- AC4 — `prevSubjects` — `EL5-AC4 a fold re-invoke hands the previous pin to its subject`, `...and none to a subject the previous round did not pin` and `...and passes priorFindings through` each printed `ok`.
- AC5 — `priorFindings` — `EL5-AC5 a fold re-invoke with neither fold arg does not throw`, `...and announces a degraded fold review`, `...passing no prevBlob`, `...and no priorFindings`, `EL5-AC5 prevSubjects alone announces the missing priorFindings`, `EL5-AC5 priorFindings alone announces prevSubjects and a whole-file review`, and both `...and not as a degraded fold review` lines each printed `ok`.
- AC6 — `prevSubjects` — twelve `EL5-AC6` lines printed `ok`: refused by name, before the sub-workflow and before any agent, each for `prevSubjects must be an array of {path, blob} with a 7 to 40 hex blob`, `priorFindings must be an array of finding objects`, and each field present at callee round 1, a fresh generation.
- AC7 — `confirmedFindings` — `EL5-AC7 the CONVERGING return hands back the pinned {path, blob} set`, `...and the callee's confirmedFindings as priorFindings`, `...and nextAction names both as the args to copy back`, `EL5-AC7 a callee return with no confirmedFindings is announced` and `...and priorFindings is omitted, never handed back as []` each printed `ok`.
- AC8 — `gotchas.py --for-paths` — the eight `EL5-AC8` lines printed `ok`: the args header documents `prevSubjects` and `priorFindings`, the meta Audit phase detail names `context`, `specs`, `checklist` and `scratch`, and the render spells the --for-paths command with no render token left on its line. At `5a1643c8d`, `grep -c` over `tools/workflows/unattended-build.js` printed 2 with no `{{` on either line, and `node tools/workflows/check-workflow-syntax.js` printed `6 workflow script(s) parsed clean`.
- AC9 — `specPath` — `EL5-AC9 an empty or absent specPath never reaches specs` and `...and the audit proceeds` each printed `ok`.
- AC10 — `scratch` — nine `EL5-AC10` lines printed `ok`, three per refused value, `/tmp/s\nX`, `/tmp/r/sub` beside `/tmp/r`, and `C:\\R\\x` beside `c:/r`: the prelude refuses a scratch the callee would, before the sub-workflow and before any spec-stage agent. `EL5-AC10 a sibling of repo sharing its prefix proceeds` printed `ok`. The labels do not show the message's `unattended-build:` opening.
