**Serves:** research TOOL-aSweptBar-7

# Brief — aSweptBar: the closing review's mediums and lows, batched

## The prompt

> Run a full bar over the repo, including self-tests, and fix all discovered reds gracefully.

## The brief

### Goal
The closing diff review, round 1
(`memory/builds/aSweptBar/reviews/2026-10-13-review-TOOL-aSweptBar-1-6-closing-diff-round1.md`),
read CLEAN WITH FIXES: 0 blockers, 0 highs, 3 mediums and 4 lows. BUILD-METHOD M4 promotes them all
into ONE batched unit, never parked or folded. This unit closes every one, with the fix the
report's skeptic confirmed (the report carries the skeptic's corrected fix where it rejected the
finder's). Read the report WHOLE first; each item carries file:line, the failing state and the fix.

### Items
1. **M1** — `tools/workflows/unattended-build.test.sh:1037`: the F2 no-run-state refusal set is
   derived from `verb_*` bodies only, and misses the eight verbs dispatched to other handlers
   (`--hold`, `--handoff`, `--settle`, `--beat`, `--audit`, `--register-task`, `--liveness`,
   `--authorization`); derive it from the driver's `case "$VERB"` dispatch joined to the handlers
   that call `check_run_state`, and make the comment true.
2. **M2** — the seven build-folder instruments that source `resolve-python.sh` through
   `${BASH_SOURCE[0]%/*}` fail when run by bare filename from their own folder; use a form that
   survives a slashless `BASH_SOURCE`.
3. **M3** — `.githooks/pre-push.test.sh`: no arm asserts the hook's non-runner FULL refusal reason
   any more ("is not this kit's runner"); restore an arm that reaches it with no bar record to adopt.
4. **L1** — `tools/run-gates/run-gates.evidence.test.sh:1469-1471`: the header still describes the
   retired `GATE_REUSE=1` control.
5. **L2** — gov's rendered `memory/TEMPLATE-SPEC.md` no longer names its review protocol file.
6. **L3** — no arm fails without the `getval` empty-first guard in
   `skills/session-kickoff/manifest-check.sh`.
7. **L4** — the CLOSED `TOOL-aSweptBar-3` spec's §4 S5 says the plain earning bar stamps nothing;
   the runner stamps it. The spec writer for this unit revises that spec (rev-3, one §8 line naming
   §4 S5) in the same spec pass; the builder does not touch specs.

### Acceptance
Each item's own observation from the report holds at the unit's tip; an arm added for M3 or L3 is
observed red on its staged break by the main loop at the close.

### Gates
`unattended-build self-test` · `pre-push self-test` · `run-gates evidence` · `manifest-check self-test` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene`

### Non-goals
Nothing beyond the seven items. Nothing under `tools/roles/`, `.claude/agents/`, `.claude/skills/build/`
or `tools/playbook/`.

### Limitations
No suite or bar runs in a pass; each verifies with a fixture or probe of its own change.

### Reuse
The report's skeptic-confirmed fixes; the driver's own dispatch table for M1; the canonical render
path `adopt-memory-tree.sh` takes for `{{REVIEW_PROTOCOL}}` for L2.

## Owner confirmation

Asked: The bar is still running, and three root causes are confirmed so far: the foreign-prefix declarations, the driver fixture's harness files, and the roles kit citing v3 charter §n sections that v4 no longer has. Shall I go and build aSweptBar, adding later reds to the roster as they land?
Answer: Go (Recommended)
