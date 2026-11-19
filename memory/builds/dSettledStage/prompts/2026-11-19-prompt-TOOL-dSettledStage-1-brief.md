# Brief — dSettledStage: the lander commits only what staging actually changed

**Serves:** research TOOL-dSettledStage-1 TOOL-dSettledStage-2

## The prompt

> Fix a defect in `tools/push-main.sh`, the lander, and gate its class. Route the unit through `/session-kickoff` first. It is a shipped-kit edit, so tier it Tier-2 at kickoff.
>
> **What happened (node d, 2026-11-19, landing 12764ec21):**
> - `run_regen` rewrote `.governance/instructions.lock`. The regen log said "moved", followed by git's "LF will be replaced by CRLF" warning.
> - At `tools/push-main.sh:1393`, `git status --porcelain` was non-empty, so the lander ran `git add -A` and then `git commit -q --no-verify ...`.
> - Staging normalized the file back to the committed bytes, so nothing was staged and the commit failed.
> - The lander printed "push-main: could not commit the regenerated outputs. Aborted (no push)." and exited 1, before the bar.
> - A plain re-run landed cleanly: bar GREEN 100/100, pushed 9e21ac760..12764ec21.
>
> **Done looks like:**
> - When staging leaves no diff, the lander skips the regen commit (`git diff --cached --quiet`) and carries on to the bar instead of aborting.
> - A selftest arm reproduces the dirty-by-EOL-only case. It is observed RED on the current lander and GREEN after the fix, and both observations are recorded beside the result.
> - The bug class gets a gate or a checklist entry, per the charter's [left-shift].
>
> **Constraints:**
> - Never use `--no-verify` outside the lander's own regen commit.
> - Never `git add -A` in your own commits.
> - Units run no gates.
> - Do not run `GATE_SELFTESTS=1` or the unattended `--selftests` without asking the owner.
> - Land only on the owner's explicit ask, through `bash tools/push-main.sh` from the primary tree.

## The brief

### Goal
The lander skips a commit that staging left empty and carries on to the bar, at every site in
`tools/push-main.sh` where a dirty tree gates a stage and a commit; and that class is gated.

### Items
1. `tools/push-main.sh`: the regen (:1393), mint (:1344) and gov-first (:1369) commits and
   `write_merge_fold` (:1063) commit only when `git diff --cached --quiet` reports a staged diff,
   through one helper, not four copies.
2. `tools/push-main.test.sh`: an arm whose regen leaves a tracked file dirty by line endings only.
3. The class gated: a scan in `tools/gate-lint/sh_hygiene.py` if its predicate is precise over the
   real tree, else a `memory/gotchas/` class claimed in a map dossier.

### Acceptance
The new arm fails on the lander at 12764ec21 with `could not commit the regenerated outputs` and
passes after the fix, with the lander reaching the bar. Both observations are recorded in the unit's
acceptance ledger. The class gate reds on a planted dirty-then-stage site and is green on the fixed
tree; a gotcha entry instead is selected by `gotchas.py --for-paths tools/push-main.sh`.

### Gates
`push-main self-test` · `shell-hygiene selftest` and the scan legs · `memory hygiene` ·
`testsuite-counts` · the full bar at landing.

### Non-goals
No change to `run_regen`, `regen.py` or any generator's output · no `.gitattributes` pinning · no
change to `.githooks/pre-push` or the bar · `tools/unattended/` commit sites are a recorded follow-up
if the class predicate finds one there, not a fix here.

### Limitations
`--no-verify` stays only on the lander's own mint, gov-first and regen commits. Units run no gates.
No `GATE_SELFTESTS=1` and no unattended `--selftests` without the owner's ask. Landing only on the
owner's ask, through `bash tools/push-main.sh` from the primary tree.

### Reuse
The regen arms 24 to 33 in `tools/push-main.test.sh` (aPrimedIndex) for the fixture. The class
registry and the shrink-only counted registry in `tools/gate-lint/sh_hygiene.py` for the gate.
`reuse_lookup.py` named no seam that checks a staged diff. Recall returned TOOL-aPrimedIndex-4,
TOOL-aMendedFleet-65, TOOL-dSafePassage-8 and PLAY-dOrderedCharter-85 as the sites' origins.
Recall terms: push-main regen commit run_regen aPrimedIndex generated outputs CRLF eol staging empty
commit lander.

## Drawn from the session

> Staging normalized the file back to the committed bytes, so nothing was staged and the commit failed.
— owner, the opening message, relayed by session local_169a034a

## Owner confirmation

Asked: Please reply "go" plus "audit yes" or "audit no".
Answer: go, no audit
