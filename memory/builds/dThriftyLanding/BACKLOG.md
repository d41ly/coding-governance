# dThriftyLanding — asks

## Asks
- TOOL-dThriftyLanding-7 · filed 2026-10-05 · `unattended kit gate` costs 222 s standalone on node d and reads every build record, so a doc-only push that touches any file under memory/builds/ still pays it in full, and it is then the whole wall of that push's bar · seen `tools/unattended/check-unattended.sh` matching `FILES=$(git ls-files "$M/")` · accept per-build checks scoped to the builds whose folders moved since a base the caller names, observed by the scoped and unscoped runs agreeing on an unchanged tree

## Dispositions
- SEV · TOOL-dThriftyLanding-7 · MED · costs about four minutes of bar on every records push; no wrong verdict
- KEEP · TOOL-dThriftyLanding-7 · filed by this run; scoping a 6000-line checker's checks is a change to what it grades, outside this build's goal
