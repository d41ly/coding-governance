# TOOL-aMendedFleet-74 — a unit can be handed the bug-class checklist for its write set before it writes code

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 74

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A unit agent meets the bug-class checklist only after it commits: `tools/workflows/unattended-unit.js`
orders it to run `gotchas.py --for-diff HEAD~1..HEAD` and act on what that names. A class the unit
walked into therefore costs a fix commit. The report found the list a unit would get BEFORE building,
from the paths it is about to touch, is 76 to 94% of the list it gets after `[B#6]`. It also found
that 7 of the 9 checklist-fix commits came from one build, so whether handing it over early helps is
unmeasured. This unit gives the unit harness an optional `prebuild` argument. When a caller passes
it, the agent runs that checklist over its declared write set before writing code. It is off by
default, so the build that measures it is the one that turns it on. The report's other half of this
point, path-scoped rules, is a second mechanism and is split off (§8 F1).

## 2. Scope (IN)

- **S1** — `tools/workflows/unattended-unit.js` reads an optional `prebuild` key from its args. With
  the key absent, the spawn's prompt and options are byte-identical to today's. With it present, it
  must be a non-empty single-line string carrying no backtick, or the script throws an error opening
  `unattended-unit:` and naming `prebuild` before the agent is spawned. Observed by AC1, AC2 and AC3.
- **S2** — With `prebuild` present, the prompt carries one paragraph after the driver steps and before
  the paragraph forbidding gates. It tells the agent that once its write set is declared, or written
  down in attended mode, and before any code, it runs the `prebuild` command followed by every path
  in that write set. An item the checklist prints in full is a class to design against now. A
  one-line item is a pointer, to be read when its class matches what the agent is about to write.
  Observed by AC1.
- **S3** — With `prebuild` present, the script logs one line naming the unit and the command before
  the spawn. With it absent, nothing new is logged. Observed by AC1 and AC2.
- **S4** — The file's header comment documents the key: the command a caller passes, spelled with
  `<prefix>` because the install-prefix gate grades this file; that it is off by default; and that it
  stays off until a build has measured whether it cuts checklist-fix commits. The budget is the
  checklist's own tiered cut, and the header says so. Observed by AC5.
- **S5** — New arms in `tools/workflows/unattended-build.test.sh` run the child with and without
  `prebuild`. NOT OBSERVED by a criterion here: the suite runs once at the close, and the arms are
  declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- Path-scoped rules for editing areas. They are a context-diet mechanism in a different file, and the
  report orders them after the diet units are measured; §8 F1 splits them to a unit the run adds.
- The parent harness handing `prebuild` out. The main loop composes each unit's Workflow call from
  `dispatch.args`, so a measuring build adds the key there; a declared switch in the parent belongs to
  whichever unit flips the default.
- The measurement: one build run with the key against builds without it, counting checklist-fix
  commits. It needs builds that have not happened.
- Ranking the checklist and cutting it in tiers. That is unit 16 of this build, which this unit's
  criteria do not rest on: they observe the prompt, not the checklist's length.
- Removing the post-commit checklist. It stays, and it is what a fix commit is counted against.

### Edges

- **hands-off** external — the path-scoped rules, split to a unit the run adds after the diet units.
- **hands-off** external — the measured build that decides whether a unit gets the checklist by
  default.

## 4. Design

### Evidence

Read at base `7af5f564` on 2026-10-04.

- `tools/workflows/unattended-unit.js` is 205 lines with one agent spawn. Its args are refused by one
  `check(key, why)` predicate, its only top-level definition. Its prompt is `cfg.ground`, the read
  order, the mode-branched `DRIVER_STEPS`, the paragraph forbidding gates and bars, and the commit and
  post-commit checklist text, which spells `cfg.checklist`.
- `tools/workflows/unattended-build.js` sets that `checklist` to
  `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and hands it out in `dispatch.args`.
  The child spells no install path; the template renders the prefix.
- `python tools/memory-tree/gotchas.py --for-paths` over unit 67's seven declared files printed 15
  items, 9 anchored and 6 universal, in 3,889 bytes. Over `tools/run-gates/run-gates.sh` alone it
  printed 10 items. PINNED at base on 2026-10-04, before unit 16's tiered cut lands.
- `TOOL-aWeighedCompass-14` measured `--for-paths tools/` selecting 30 classes plus 4 universal, which
  is the catalogue and not a checklist. The paragraph therefore hands the declared FILE paths, never a
  directory.
- The report's 76 to 94% overlap and its 7 of 9 fix commits were not re-derived; they are UNVERIFIED
  here and motivate only the dark default.
- Facts for the split unit, read from the PATH CLI 2.1.178 binary with a read-only `grep -a -o`:
  `.claude/rules/` files "can be scoped to specific file paths using `paths` frontmatter", and an
  instructions-loaded hook event reports a `path_glob_match` load reason. This repository has no
  `.claude/rules/` directory.

### Inventory

No new function. The key is read inline beside the `mode` refusal, which is also not a `check()`
call, because `check()` asserts truthiness and `prebuild` is optional. The file keeps its one
top-level definition: the codebase-map JS liveness floor and the lexicon's probe layer both grade it.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`

### Rollout

Dark: no caller passes `prebuild`, so every unit's prompt is unchanged until a build measures it. The
child's `meta.version` and its `gov:kit` marker move once, minted at the lander by unit 65 or owed at
the close.

### Alternatives rejected

- **Turning it on for every unit now.** The report's own uncertainty list names this exact effect as
  unknown, and seven of the nine fix commits it counted came from one build.
- **A top-N cap chosen here.** The checklist already cuts itself in tiers once unit 16 lands; a second
  budget in the prompt would be two answers to one question.
- **Running the checklist inside the harness and pasting its output into the prompt.** The harness
  runs before the agent declares its write set, so it does not know the paths.

## 5. Production-readiness checklist

- security — the key is a command string the caller already controls, as `checklist` is; refusing a
  newline or a backtick keeps one value from rewriting the prompt around it.
- perf / scale — one checklist run per unit, about a second, and only when the key is passed.
- error / empty / loading states — a malformed value is refused before the spawn; a checklist that
  selects nothing prints its universals, which is still a list.
- observability — the S3 log line says which units ran with it, which is what a measuring build
  counts.
- risks — a longer prompt for every unit that gets it; the dark default means no unit gets it unasked.
- testing — AC1 to AC5 directly; the arms in S5.
- migration — none.
- user docs — the header comment in S4; the workflows README does not describe this child today.

## 6. Acceptance criteria

- **AC1** — When `tools/workflows/unattended-unit.js` is evaluated as an async function body with a
  recording stub `agent`, unattended-mode args and
  `prebuild: 'python tools/memory-tree/gotchas.py --for-paths'`, the recorded prompt carries one
  paragraph naming that command, after the `--dispatch` sentence and before the text
  `NO GATE, SUITE OR BAR RUNS`, and the log carries a line naming the unit and the command. The same
  run in attended mode carries the paragraph and no order to call `--dispatch`.
  Red when: the paragraph is missing, out of place, or tells an attended unit to call a verb that
  refuses there.
  fixture: the stub runner is the evaluation shape `tools/workflows/check-workflow-syntax.js` already
  uses, written to the scratchpad for this check.
- **AC2** — When the same stub run is made with no `prebuild`, in both modes, against the unit's tip
  and against the file at `7af5f564` read with `git show`, the recorded prompts, options and log lines
  are identical between the two.
  Red when: a default run changes.
- **AC3** — When the stub run is made with `prebuild` set to `7`, to an empty string, to a string
  carrying a newline and to one carrying a backtick, each throws an error naming `prebuild` before the
  stub records a spawn. These are the staged breaks for S1's refusal.
  Red when: any of the four reaches the spawn.
- **AC4** — When `node tools/workflows/check-workflow-syntax.js` and
  `bash tools/workflows/check-verifier-fanout.sh` run at the unit's tip, both exit 0, and
  `grep -c "^function " tools/workflows/unattended-unit.js` prints 1.
  Red when: the script no longer parses, or a second top-level definition appears.
- **AC5** — When `grep -n "prebuild" tools/workflows/unattended-unit.js` runs, its header-comment hits
  name the off default, the `--for-paths` command spelled with `<prefix>`, and the measurement the
  default waits on.
  Red when: the key is undocumented, or the header spells an install path.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `tier2-review self-test` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/workflows/unattended-build.test.sh` · the child run with and without `prebuild`, against the base child, which reads no such key · none

## 8. Open questions

- **F1 — Is this point one mechanism?**
  The report's item joins path-scoped rules for editing areas with a budgeted pre-build checklist in
  unit prompts. The first is a set of rule files the CLI loads by path, cut from the charter, and the
  report orders it after the diet units 67, 68 and 79 are measured. The second is a prompt paragraph
  in the unit harness, whose precondition is the checklist's ranking.
  RESOLVED (agent, 2026-10-04, delegated): split — the path-scoped rules move to a new unit the run
  adds, ordered after units 67, 68, 79 and the A/B run unit 93; this unit keeps the pre-build
  checklist.
- **F2 — Where does the switch live?**
  Options: an optional key on the child only; a key the parent harness also hands out. The main loop
  already composes each unit's call from `dispatch.args`, and the parent's own arms live in a suite
  this pass may not run.
  RESOLVED (agent, 2026-10-04, delegated): the child only, per S1.
- **F3 — Does the brief's precondition bind this half?**
  The brief orders the point after units 67, 68 and 79 are measured; the report orders it after its
  items 14, 15 and 20, the last being the checklist's ranking, unit 16 here. The diet measurements
  bear on the context an agent loads, which is the split half. This half lands dark, so no unit's
  prompt changes before a build measures it.
  RESOLVED (agent, 2026-10-04, delegated): build at order 74, dark; the diet precondition travels with
  the split unit.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft; the point split in §8 F1, the child harness's prompt and args
  read at base, and the checklist sized over two real write sets.

## 10. Reuse audit

The seam extended is the child harness's existing pattern for the post-commit checklist: a command
string the caller hands in args and the prompt spells, as `cfg.checklist` is in
`tools/workflows/unattended-unit.js`, with the inline refusal shape of its `mode` key. The command it
names is the existing `--for-paths` mode of `tools/memory-tree/gotchas.py`. `python
tools/codebase-map/reuse_lookup.py "hand a unit agent a budgeted pre-build bug-class checklist for
the paths it declared"` returned only name-stem neighbours such as `build_reference_index` and
`build_unit_id_re`, none of which builds a prompt; `grep -n checklist` over the two unattended
workflow scripts was the probe and found the seam. Recall returned `TOOL-aWeighedCompass-14`, which
measured why a directory argument floods the checklist; unit 16's spec, whose hands-off names this
driver-side step; and the original bug-class corpus decision `TOOL-aFoldedQuarry-6`. Where the report
and the tree disagree: the report speaks of a "budgeted top-N", and no top-N exists; the budget is
unit 16's tiered cut. And the brief's precondition names units 67, 68 and 79 where the report names
its items 14, 15 and 20, which §8 F3 reconciles.

Recall terms used: `python tools/memory-recall/query.py "should a unit get the bug-class checklist
before it writes code rather than only after the commit" --terms "pre-build checklist gotchas
for-paths dispatch write set budgeted top-N unit prompt checklist-fix commits path-scoped rules"`
