# Brief — dSettledStage: the closing review's findings promoted, a failed stage refuses and the scan's gaps close

**Serves:** research TOOL-dSettledStage-3 TOOL-dSettledStage-4

## The prompt

> One defect is HIGH: `write_staged_change` ignores a failed `git add -A` and answers "nothing staged", so the lander silently skips its mint, gov-first and regen commits and its merge fold.

## The brief

### Goal
Dispose every confirmed finding of the round-1 closing review
(`reviews/2026-11-19-review-TOOL-dSettledStage-1-2-closing-diff-round1.md`) by the build method's severity rule:
the HIGH item becomes `TOOL-dSettledStage-3`, and the MEDIUM and LOW items are batched into `TOOL-dSettledStage-4`.

### Items
1. `TOOL-dSettledStage-3`, the review's item 1 (findings 1, 3 and 5). `write_staged_change` in `tools/push-main.sh`
   gains a third answer for a failed `git add -A`, and every caller refuses on it with its own stage's line: the
   mint, gov-first and regen sites abort with no push, and `write_merge_fold` returns 1. Do not rely on the
   caller's later commit failing. A `tools/push-main.test.sh` arm holds `.git/index.lock` over a real change and
   asserts both refusals. The new class `failed-stage-reads-as-nothing-staged` lands as a `memory/gotchas/` entry
   claimed under the push-main dossier's `gotcha-classes`, rendered with `gen_map.py --write` in the same commit.
2. `TOOL-dSettledStage-4`, the review's items 2 to 6 (findings 2, 4, 6, 8, 9 and 10), in
   `tools/gate-lint/sh_hygiene.py` and arm 43. The quoted-substitution `)` no longer ends a verb's arguments
   (item 2). Every git global-option spelling before the verb is read, or a `STAGE_BOUNDARY` row names the ones
   still unread (item 3). The stager set closes transitively (item 4). Arm 43 gains arm 42's liveness markers
   (item 5). Spec 2's §7 Gates line omission is a CLOSED spec, which stays frozen; unit 4's own §7 names the leg
   and its revision log records the correction (item 6). Re-measure `memory/project/stage-commit-sites.txt` after
   widening, and raise `FLOOR_ASSERTIONS` to the count the selftest prints.

### Acceptance
Each unit's criteria observe its fix on a fixture or probe, with a RED observable on the tree at
`41e57fca5` (the build's head when the review ran). Unit 3: with `.git/index.lock` held over a real change, the
landing exits 1 with a stage refusal and pushes nothing, and the fold returns 1. Unit 4: the review's probe
inputs for items 2 to 4 read the classes its fixes state, and arm 43 reds when its fixture produces no dirty,
empty-stage shape.

### Gates
`push-main self-test` · `shell-hygiene selftest` · `shell hygiene (a stage committed with no staged-diff test)` ·
`harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` ·
`writing practice (records and units)` · `positional (the citation check alone)` · `codebase-map coverage + freshness`

### Non-goals
No change to `run_regen`, the generators, `.gitattributes`, `.githooks/pre-push` or the bar. No edit to the
CLOSED specs of units 1 and 2. The `tools/unattended/` registry row stays a follow-up for the owner.

### Limitations
Units run no gates. Unit 3 is ordered before unit 4, because both write `tools/push-main.test.sh`. Refusals
earlier passes of this build hit, to avoid in the specs and records: a count in prose with no pin on its line
(an id, a blob-pinned `path@blob:line`, PINNED or DERIVED); a bare `path:line` citation outside a code span; a
`Pass: none` trailer anywhere but the final trailer block; a new symbol without `gen_map.py --write`; a new
gotcha class without its dossier claim. Run `python tools/check-spec-tokens.py --spec <path>` before returning.

### Reuse
Unit 3 extends `write_staged_change` and arms 42 and 43's fixtures. Unit 4 extends `read_stage_events`,
`read_stage_helpers`, `STAGE_EVENT`, `STAGE_BOUNDARY` and `read_substitution` in `sh_hygiene.py`.

## Drawn from the session

> Fix every blocker, and ONLY blockers: highs, mediums and lows carry to the exit, where M4 promotes them.
— agent, the build method's close section

## Owner confirmation

Asked: Please reply "go" plus "audit yes" or "audit no".
Answer: go, no audit
