# Brief — aTrimmedWait: six reworks that cut the time builds spend waiting, with no verdict moved

**Serves:** research TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7

The prompt arrived as prose from the session that started this one, on the owner's instruction, and is quoted whole.

## The prompt

> Background (from the session that started this one):
> The owner asked on 2026-11-14 for a new build covering all six recommendations from a timing analysis of session db957487. That session ran builds dFairHearing and aSmoothedDispatch: 334 agents and 72h of agent wall time. Its biggest reworkable costs were re-dispatched units caused by spec defects, checks that grade the whole tree when the caller needs one file (hygiene check 12, whole-tree spec tokens, full index renders), the pre-commit hook's cost and refusals, 51-second idle-wake ticks, builders polling their own background suites, and re-parsing the session transcript for format lines. aSmoothedDispatch, landed at origin/main 47ed57fab, already scoped and cached the spec-token check at `--dispatch` (its unit 4) and gave spec writers `--spec`. The lander's mint-fixpoint bug is filed separately as TOOL-aSmoothedDispatch-23 and is not part of this build.
>
> Task:
> Open and run a new ATTENDED build in the coding-governance repository for six reworks that cut the time builds spend waiting, without changing any check's verdict.
>
> 1. Read the full handoff brief first. It holds the measured evidence, the code anchors and the constraints for each item, and the analysis scripts beside it re-derive every figure.
> 2. Run `/session-kickoff` for a new build on local main (it was `846d51d39` at handoff). Mint the slug, derive the closed scope from the brief, and ask the owner the spec-audit question once.
> 3. Before any spec, re-verify each of the six items against current main, since builds have landed since the measurements. Shrink or drop an item main already fixed, and record that you did.
> 4. The six items, in evidence order:
>    - **R1:** validate a spec against what `--dispatch` checks, before the spec commit. About 30h of re-dispatch rework, from 44 extra agents.
>    - **R2:** scope memory-hygiene check 12 to one spec or one build. About 8h; each run takes 4–6 min.
>    - **R3:** render the build index before the pre-commit grade, and render only what changed. About 3–5h, plus 71 check-9 refusals.
>    - **R4:** short-circuit the idle-wake `--resume` and `--release-task` when nothing moved. About 6h at 51 s per tick.
>    - **R5:** no suites inside a pass (scratch-guard G3, every launch form), and no `tail -f` polling. About 12h of builder waiting.
>    - **R6:** make `handoff.py agents` incremental. About 1.5h.
>
>    Each item is at least one Tier-2 unit, and each unit's spec comes from `gov-spec-writer`.
> 5. Build through `/build`, with `gov-builder` per unit, the closing review, RED-first observations of the new arms, and one bar.
>
> **Done looks like:** every unit is CLOSED; its acceptance ledger records the same command timed before and after on node a; a fixture shows the verdict unchanged: the same refusals, reds and greens; the bar is green.
>
> Land through `bash tools/push-main.sh` only when the owner asks, never with `--no-verify`. Ask each fork on its own.

## The brief

### Goal
Cut the time a build spends waiting on checks, renders and polls that do more than their caller
needs, while every check returns the verdict it returns today.

### Items
1. R1: a spec is validated against `--dispatch`'s cheap refusals before the spec commit, through the driver's own predicates [planned TOOL-aTrimmedWait-1]
2. R2: hygiene check 12 grades one named spec or build on request; the full run and the bar still grade all [planned TOOL-aTrimmedWait-2]
3. R3: the pre-commit hook renders the staged builds' index before check 9 and stages it [planned TOOL-aTrimmedWait-3]
4. R3: `gen_build_index.py --write` re-renders only what its changed inputs reach [planned TOOL-aTrimmedWait-4]
5. R4: `--resume` returns its previous verdict when HEAD, the run-state file and the task registry have not moved [planned TOOL-aTrimmedWait-5]
6. R5: a role agent's polling wait is refused, and G3 reads past `-o pipefail` [planned TOOL-aTrimmedWait-6]
7. R6: `handoff.py agents` parses only a transcript's appended bytes, printing byte-identical lines [planned TOOL-aTrimmedWait-7]

### Acceptance
- Each unit's acceptance ledger records the same command timed before and after on node a.
- Each unit has a fixture on which the refusals, reds and greens before and after are identical.
- Each new arm is observed red before green.
- R1: a spec carrying each refusal class `--dispatch` reports cheaply is refused before its commit, with `--dispatch`'s own message.
- R6: `handoff.py agents` prints byte-identical output with the cache cold, warm and after an append.

### Gates
The merge bar, `bash tools/run-gates/run-gates.sh`, once at the close, with no self-test suite in it; each kit's own arms for the units that touch it.

### Non-goals
- No verdict change, and no narrowing of the full hygiene run, the bar, or `--dispatch`'s own refusals.
- R4: no `--release-task` change unless a timed release on a live registry exceeds the driver's 4.7 s startup.
- R5: no G3 change beyond the option gap; the header's ceiling on evasion stays as written.
- The lander's mint fixpoint, TOOL-aSmoothedDispatch-23, is not in this build.
- The other findings of the analysis (agent edits aimed at the primary tree, agent-cap marker refusals, environment reboots) are not in this build.

### Limitations
- Every speed-up is keyed on what it read, so a cached or scoped answer that cannot prove its inputs falls back to the full run.
- Measurements run on node a, one at a time, with no suite running beside them.
- Long suites run on a frozen clone, one at a time.

### Reuse
- R1: `verb_dispatch`, `plan_state`, `order_verb_of`, `scan_consumes_cycles` and `run_spec_token_check` in `tools/unattended/unattended.sh`; `check-spec-tokens.py --spec`.
- R2: check 12's loop and the `--only` parse in `tools/memory-tree/check-memory-hygiene.sh`.
- R3: `--check --staged`'s render decision in `tools/memory-tree/gen_build_index.py` (TOOL-aTrimmedHook-1) and `.githooks/pre-commit`.
- R4: `derive_spec_token_key`'s key-then-record pattern in `tools/unattended/unattended.sh`, beside `verb_resume`.
- R5: `scanCommandHeads`, `checkRoleGate` and `GATE_OPTION_RULES` in `tools/hooks/scratch-guard.js`.
- R6: `load_session_calls` in `tools/roles/handoff.py`.
- Recall returned no record that already scopes these checks.
- Recall terms used: dispatch check-49 spec-tokens hygiene check-12 gen_build_index staged render resume audit tick handoff agents cache

## Drawn from the session

> HYGIENE --only 12 ran checks 12 25 / wall 376.705 s
— agent, kickoff re-verification at `846d51d39`

> UNATTENDED check 88 FAILED — the task has no open registration … / wall 4.748 s
— agent, kickoff re-verification of `--release-task` at `846d51d39`

> DENY timeout 900 bash tools/workflows/tier2-review.test.sh · DENY cd tools/workflows && bash tier2-review.test.sh · DENY nohup bash … & · ADMIT bash -eo pipefail tools/workflows/tier2-review.test.sh · ADMIT tail -f /c/x.log
— agent, kickoff probe of `checkRoleGate` for `gov-builder` at `846d51d39`

## Owner confirmation

Asked: Should build aTrimmedWait (six speed-up reworks, about 6–8 Tier-2 units) declare `spec-audit:`, so an adversarial spec audit runs before any code is built?
Answer: No audit

Asked: Ready — say go and I'll start, or adjust any field.
Answer: Go
