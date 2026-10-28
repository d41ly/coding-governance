# TOOL-dSafePassage-1 — the upgrade-step kind: the step row, succession rows, their one reader, and frozen landed rows

**Status:** CLOSED · rev-11 · 2026-10-26 · node d · Tier-2 · base 3708a705 · streams tooling · order 1 · advances TOOL-dSafePassage-14 · ratified 2026-10-24

**Carries:** cl-dClosedLoop-0018@d4cade33 part 1/2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-1-departures-spec.md](../build/2026-10-23-build-TOOL-dSafePassage-1-departures-spec.md) | journal | — |
| [2026-10-23-build-TOOL-dSafePassage-1-deviation-106.md](../build/2026-10-23-build-TOOL-dSafePassage-1-deviation-106.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-1-deviation-107.md](../build/2026-10-23-build-TOOL-dSafePassage-1-deviation-107.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-1-deviation-108.md](../build/2026-10-23-build-TOOL-dSafePassage-1-deviation-108.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-1-deviation-109.md](../build/2026-10-23-build-TOOL-dSafePassage-1-deviation-109.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-1-deviation-11.md](../build/2026-10-23-build-TOOL-dSafePassage-1-deviation-11.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-1-deviation-145.md](../build/2026-10-23-build-TOOL-dSafePassage-1-deviation-145.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-1-deviation-146.md](../build/2026-10-23-build-TOOL-dSafePassage-1-deviation-146.md) | deviation | — |
| [2026-10-24-build-TOOL-dSafePassage-1-deviation-149.md](../build/2026-10-24-build-TOOL-dSafePassage-1-deviation-149.md) | deviation | — |
| [2026-10-24-build-TOOL-dSafePassage-1-deviation-157.md](../build/2026-10-24-build-TOOL-dSafePassage-1-deviation-157.md) | deviation | — |
| [2026-10-24-build-TOOL-dSafePassage-1-deviation-158.md](../build/2026-10-24-build-TOOL-dSafePassage-1-deviation-158.md) | deviation | — |
| [2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md](../build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md) | research | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-25-build-TOOL-dSafePassage-1-deviation-160.md](../build/2026-10-25-build-TOOL-dSafePassage-1-deviation-160.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-parent-fixes-return.md](../build/2026-10-25-build-TOOL-dSafePassage-1-parent-fixes-return.md) | research | TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-13 TOOL-dSafePassage-26 |
| [2026-10-26-build-TOOL-dSafePassage-1-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-1-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-2-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-2-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-3-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-3-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-4-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-4-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-carries-repin.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-carries-repin.md) | research | TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md) | research | TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-owner-audit-cap.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-owner-audit-cap.md) | research | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-widens-marks.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-widens-marks.md) | research | TOOL-dSafePassage-7 |
| [2026-10-24-prompt-TOOL-dSafePassage-1-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dSafePassage-1-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dSafePassage-1-3-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-3-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dSafePassage-1-ac15-pathspec.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-ac15-pathspec.md) | research | — |
| [2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md) | research | TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-24-prompt-TOOL-dSafePassage-1-owner-forks.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-owner-forks.md) | research | TOOL-dSafePassage-6 |
| [2026-10-25-prompt-TOOL-dSafePassage-1-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dSafePassage-1-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md](../prompts/2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md) | research | TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-13 TOOL-dSafePassage-26 |
| [2026-10-26-prompt-TOOL-dSafePassage-1-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-1-build-brief.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-1-owner-builder-effort.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-1-owner-builder-effort.md) | research | — |
| [2026-10-26-prompt-TOOL-dSafePassage-61-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-61-1-spec-writer.md) | research | TOOL-dSafePassage-61 |
| [2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-brief.md) | research | TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-26 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 |
| [2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

Give gov a declared upgrade-step kind: a kit descriptor's `[[upgrade]]` row and the registry's
`[[retired]]` succession row, one reader for both, `update` and `check` that carry a retired kit to
its successor instead of refusing the whole run, the first step (`.agent-cap.conf`'s `FANOUT_CAP`
into `runtime.agents-in-flight`), and a leg that keeps every landed step row frozen. The clause's
second step, the size-limits file's rows into `budgets.*` with gov's own migration, is
TOOL-dSafePassage-61's since §8 F8's stop fired. It closes `gap-deploy-15` (a receipt
naming a retired kit refuses the whole update, and `check` reds on it) and `gap-deploy-16` (no
upgrade-step kind: a moved conf key is only reported).

## 2. Scope (IN)

- **S1** — The step row. Every registry entry's descriptor may carry `[[upgrade]]` rows, and
  `tools/govkit/steps.toml` carries rows of the same grammar for surfaces no descriptor owns
  (§4 Data model). The introducing commit is DERIVED by the reader and never typed in the row (§8 F2).
  Observed by AC1, AC2 and AC3.
- **S2** — The succession row. `tools/govkit/registry.toml` gains `[[retired]]` rows: `id` (an entry
  id or a step id), `successor` (a live id of the same kind, or `none`) and `surfaces`, the commit
  that retires it derived like the introducing commit. Observed by AC2 and AC4.
  **Readers:** by name: `tools/govkit/govkit.py`'s `load_registry` and `read_descriptors`, which load
  the registry whole and read no table they do not name · by value: NO VALUE READERS until S4.
- **S3** — The one reader, `tools/govkit/upgrade_steps.py`. `read_steps` and `read_retired` parse,
  validate and order every row at a revision or in the working tree; `govkit.py` calls them and
  parses no row itself. A CLI, `python tools/govkit/upgrade_steps.py list`, prints the ordered rows.
  Observed by AC1, AC2 and AC3.
- **S4** — `update` and `check` read succession through `resolve_claim`. A claimed kit that is no
  longer a registry entry and carries a `[[retired]]` row is carried to its successor, or released
  with its rows routed to the existing `withdrawn` arm when the successor is `none`, in place of the
  whole-run refusal at `tools/govkit/govkit.py:9235-9239` and the problem `check` appends at
  :5677-5679. A claimed id with no succession row still refuses. Observed by AC6, AC7, AC8 and AC9. The replaced refusal's text, "which is no longer a registry
  entry", is spelled once (`git grep -n -F 'no longer a registry entry' -- tools skills`).
  **Readers:** by name: `tools/govkit/govkit.py:9237`; no test asserts the text · by value:
  NO VALUE READERS — a raise and a report line.
- **S5** — The translation window. Its population is the homes the step rows' `surfaces` declare,
  read from the rows and never retyped, `.agent-cap.conf` among them, and the size-limits file once
  TOOL-dSafePassage-61's row joins. dGroundRules' `legacy-homes.txt` holds neither and is withheld
  from installs (its units 7 and 17), so S5 does not read it. A member's window closes when its step
  lands, and `upgrade_steps.py list --window` prints each member `open` or `closed by <step id>`. Observed by AC16.
- **S6** — The step `agent-cap/fanout-cap-to-agents-in-flight`, an `[[upgrade]]` row in
  `tools/hooks/kit.toml` whose program is `tools/govkit/steps/fanout_cap.py`. Its up moves
  `.agent-cap.conf`'s `FANOUT_CAP` into `runtime.agents-in-flight` and retires the file, so the limit
  reads the same either side; its down restores both files byte-identical.
  Observed by AC10, AC11 and AC12. The file's by-name readers are those
  `git grep -n -F '.agent-cap.conf' -- tools skills` prints, re-derived at the build run's base,
  since dGroundRules' unit 10 retires agent-cap.js's read and `--print-cap` and re-points the rest.
  **Readers:** by name: `tools/hooks/agent-cap.js`, `tools/hooks/README.md`,
  `tools/workflows/README.md`, `tools/workflows/check-verifier-fanout.sh`, `tools/workflows/kit.toml`,
  `tools/hooks/agent-cap.test.sh`, `tools/workflows/check-protocol-parity.test.sh` and
  `tools/workflows/check-verifier-fanout.test.sh`, as at base 3957a8958 · by value: `policy.py get runtime.agents-in-flight`, whose `read_legacy_fanout` reads the file as a
  legacy home while it exists (`cl-dClosedLoop-0016`).
- **S7** — Moved to TOOL-dSafePassage-61, its S1, on 2026-10-26, when §8 F8's stop fired: the
  size-limits step's row and program. NOT OBSERVED here — TOOL-dSafePassage-61's AC1 and AC2
  observe it.
- **S8** — Moved to TOOL-dSafePassage-61, its S4, on 2026-10-26, when §8 F8's stop fired: gov's own
  migration of the size-limits file. NOT OBSERVED here — TOOL-dSafePassage-61's AC3 and AC4
  observe it.
- **S9** — Frozen landed rows. `check_frozen` compares every `[[upgrade]]` and `[[retired]]` row
  present at a base on the default branch with the same id at the head: a removed row reds unless a
  `[[retired]]` row at the head names it; an edited `up`, `down`, `witness`, `resume` or `surfaces`
  reds; an edited byte of any program file a landed argv names reds; a correction shipped as a new
  step is green. It runs as a new leg, `step-rows-frozen`, whose argv is
  `python tools/govkit/upgrade_steps.py frozen`, with an `[[exempt_leg]]` row in
  `tools/govkit/registry.toml`. Observed by AC4, AC5 and AC17.
  **Readers:** by name: READER NOT IN TREE — the one reader is this unit's new module · by value:
  NO VALUE READERS — the runner reads only the exit code.
- **S10** — The help page `help/upgrade-steps.md`, linked from `help/README.md`: what an upgrade step
  is, what `update` does with a kit that has a successor, and where `.agent-cap.conf`'s value lives.
  Observed by AC18.

## 3. Non-goals (OUT)

- The walk, `TOOL-dSafePassage-2`'s, ordering aside (S3): until it lands, S6 runs only by its own
  argv.
- The receipt's `steps` field and the schema-4 step (`TOOL-dSafePassage-3`), down steps in reverse
  and the recorded rollback (`TOOL-dSafePassage-4`), the isolated runner and its `-I` contract
  (`TOOL-dSafePassage-7`), gov's source-mode receipt (`TOOL-dSafePassage-8`), the surface class
  registry and the step gate (`TOOL-dSafePassage-10`), the floor step (`TOOL-dSafePassage-11`) and
  the release-0 fixture (`TOOL-dSafePassage-5`).
- `plan` and `apply` given `--kits` naming a retired id: they still refuse it as unknown.
- `TOOL-dRetiredFork-38`'s scoped re-stamp (`update --write --kits <one>`), which this unit
  neither fixes nor widens.
- Any legacy home other than the one S6 retires. The size-limits file is TOOL-dSafePassage-61's, and
  dConvergedCharter folds the kit conf keys.

### Edges

- **consumes-from** external — dGroundRules, landed first: `.governance/policy.toml` and its schema
  (`cl-dClosedLoop-0007`), `policy.py get` (`cl-dClosedLoop-0008`), `runtime.agents-in-flight` with
  `read_legacy_fanout` (`cl-dClosedLoop-0016`), without which S6 has no key to write
- **hands-off** `TOOL-dSafePassage-2` — walking the ordered rows, running each by its argv, and
  staging every path a step writes, its before-image included
- **hands-off** `TOOL-dSafePassage-3` — the receipt step's row, first in the steps file
- **hands-off** `TOOL-dSafePassage-4` — the reverse walk, each applied row's `down` argv restoring
  from its up's before-image
- **hands-off** `TOOL-dSafePassage-7` — an argv's interpreter and placeholders, under isolation
- **hands-off** `TOOL-dSafePassage-8` — the fan-out step in gov's receipt, its witness holding on gov,
  which tracks no `.agent-cap.conf`
- **hands-off** `TOOL-dSafePassage-10` — the class registry `surfaces` member ids are spelled from
- **hands-off** `TOOL-dSafePassage-11` — the floor step's row, second in the steps file
- **hands-off** `TOOL-dSafePassage-5` — the fan-out step walked up, down and up over the release-0
  fixture
- **hands-off** external — dWitnessedBar's append-only factory, which the frozen rows join
- **hands-off** `TOOL-dSafePassage-17` — the per-row reverted rule and no-image down this unit's grammar and restore helper gain (finding 51)
- **hands-off** `TOOL-dSafePassage-20` — the one spelling of the unlanded value this unit's reader returns, recorded as null at the writer (finding 3)
- **hands-off** `TOOL-dSafePassage-26` — the round-1 spec audit's minors batch, repairing this unit's findings once every unit is built
- **hands-off** `TOOL-dSafePassage-61` — the size-limits step and gov's own migration, moved out at §8 F8's stop; that step reads rows through `read_steps` and writes through `write_before_image` and `render_policy_text`

## 4. Design

### Data model

One grammar for a step row, wherever it is declared.

| Key | Type | Rule |
|---|---|---|
| `id` | string | `<entry>/<slug>`, slug `[a-z0-9][a-z0-9.-]*`. In a descriptor, `<entry>` equals that descriptor's own `id`. In `tools/govkit/steps.toml`, `<entry>` names no registry entry (today `govkit` and `lib`). Unique over every declaring file. |
| `up`, `down`, `witness` | argv list | Non-empty strings. `argv[0]` is `python` or `bash`, which the runner resolves. The only placeholders are `{gov}` (gov's tool root, absolute), `{target}` (the target's checkout root, absolute) and `{prefix}` (the target's install prefix); any other `{...}` is refused. A token beginning `{gov}/` names a program, which must be a tracked file at the revision read. `witness` exits 0 when the step is applied. |
| `resume` | optional | `"atomic"` (the up leaves no partial state) or an argv list under the rules above. Absent means the up is re-runnable over its own partial state. Its use is unit 2's walk's. |
| `surfaces` | list | Required, possibly empty, so an absence is declared. Each item is `<class>:<name>`, class `[a-z][a-z0-9-]*`. Class membership is the step gate's question, not this reader's (§8 F6). |
| `needs-target` | bool | Required. True when the step must run the target's own code. |

Any other key is refused, and so is an `introduced` key, naming the derivation (§8 F2).

A `[[retired]]` row in `tools/govkit/registry.toml` carries `id`, `successor` and `surfaces`; an
entry id retires to an entry id or `none`, a step id to a step id or `none`. Refused: a retired id
still live as an entry or a step, a successor not live at the revision read, an authored `retired`.

A row's introducing commit, and a succession row's retiring commit, is the oldest commit on the
default branch's first-parent line (the remote ladder's `<remote>/<branch>`, else the local branch)
whose tree holds a row with that id, else `unlanded`. The derivation reads the declaring files'
blobs oldest first along `git rev-list --first-parent --reverse <landed ref> -- <declaring files>`
and stops at the first holding blob, so a second-parent branch commit never introduces a row.

The order is total: landed rows by their introducing commit's first-parent position, then unlanded
rows; within one commit `tools/govkit/steps.toml` first, then descriptors in registry entry order
(§8 F7); within one file, row order.

The step this unit ships:

```toml
# tools/hooks/kit.toml
[[upgrade]]
id = "agent-cap/fanout-cap-to-agents-in-flight"
up = ["python", "{gov}/govkit/steps/fanout_cap.py", "up", "{target}"]
down = ["python", "{gov}/govkit/steps/fanout_cap.py", "down", "{target}"]
witness = ["python", "{gov}/govkit/steps/fanout_cap.py", "witness", "{target}"]
surfaces = ["conf-key:.agent-cap.conf#FANOUT_CAP"]
needs-target = false
```

`tools/govkit/steps.toml` lands holding its header comment and no row; TOOL-dSafePassage-3's row is
its first.

**The before-image.** Each up first writes `.governance/steps/<entry>/<slug>.before.json` at the
target: every path it will write or remove, with its bytes (base64, `null` for absent) and the sha256
the up leaves there (`null` for removed). An existing image is never overwritten, so a re-run over a
killed up computes from the first image and converges; the witness file changes last. A down restores
each path only where its bytes are the image's after-hash or before bytes, else exits 1 naming the
path, so a later edit is never discarded silently, and then removes the image. Both helpers live in
`tools/govkit/upgrade_steps.py`, which each step program imports by its own file's path, because the
runner's `-I` drops the script directory from `sys.path`.

**Reading before the commit.** The reader reads committed revisions only (dGroundRules unit 2, S2)
and a kit imports no sibling kit (its unit 1), so a step runs gov's `{gov}/policy/policy.py` or
`budgets.py` as a subprocess in the target before writing, and parses its own output with `tomllib`
for the read-back and the witness. Pre-write reads run only while no before-image exists, so a killed
up's half state, committed or not, never draws the two-homes refusal (its unit 9, S3).

**S6's up.** No `.agent-cap.conf`: exit 0. Otherwise it reads the working-tree file, the bytes its
image keeps, in `read_legacy_fanout`'s grammar (unit 10, S1: `FANOUT_CAP=<n>` or `"<n>"`, a BOM and a
trailing CR tolerated, the last such line winning), and exits 1 writing nothing on an `<n>` that is
not an integer of at least 1, any other assignment, or a conf or policy file differing from its blob
at HEAD. Where `policy.py get runtime.agents-in-flight --rev HEAD --explain` gives the reason
`lowered to <n> by FANOUT_CAP`, it sets `runtime.agents-in-flight` to `<n>`; else the file lowers
nothing and the key is left (§8 F10). It then removes the file. Witness: `.agent-cap.conf` is absent.

**Writing the policy file.** dGroundRules lands no writer, so S6 writes through
`render_policy_text` in `tools/govkit/upgrade_steps.py`, a line editor setting one key in one table
that refuses its own output unless `tomllib` reads the value back (§8 F9).

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `read_steps(root, rev, landed_ref)`, `read_retired(root, rev, landed_ref)`, `derive_introduced`, `resolve_claim(eid, entry_ids, retired)`, `check_frozen(root, base, head)`, `write_before_image`, `write_from_before_image`, `render_policy_text`, `main`, `cmd_list`, `cmd_frozen` | `tools/govkit/upgrade_steps.py` | `py.function` snake, verbs read, derive, resolve, check, write, render, main, cmd |
| `StepRow`, `RetiredRow` | `tools/govkit/upgrade_steps.py` | `py.type` pascal |
| `derive_push_base(root, base)`, extracted from `cmd_epoch` | `tools/govkit/govkit.py` | `py.function` snake |
| `cmd_up`, `cmd_down`, `cmd_witness`, `main` | `tools/govkit/steps/fanout_cap.py` | `py.function` snake |
| the step id `agent-cap/fanout-cap-to-agents-in-flight` | the row above | — |
| the leg `step-rows-frozen` | `tools/gate-legs.json`, chunk `declarations`, subject `repo`, no guard (it reads every descriptor, which live anywhere under the tool root), ceiling measured at build | — |

`Refusal` moves from `tools/govkit/govkit.py:115` into `tools/govkit/upgrade_steps.py` and
`govkit.py` imports it back, so every catcher of `govkit.Refusal` still resolves. Each new
`raise Refusal` and `r.fail` site is a `tools/govkit/refusal_join.py` anchor armed by a
`tools/govkit/selftest.py` arm, its `BRANCH_PIN` floor moving by the count measured at both ends.

`derive_push_base` is `cmd_epoch`'s base ladder (`tools/govkit/govkit.py:13446-13474`): `--base`,
else `GATE_PUSH_BASE`, else the merge-base with the remote ladder's default branch, extracted at its
second instance, `cmd_frozen`, rather than copied (charter `[reuse]`).

### Migration

Additive: a descriptor's new table changes nothing until `update` reads it, and `read_descriptors`
(`tools/govkit/govkit.py:13238-13253`) loads a descriptor whole, so it reaches no other reader. Gov's
tree needs no migration here: it tracks no `.agent-cap.conf`, so S6's up exits 0 on it and writes no
guarded path. Gov's size-limits file is TOOL-dSafePassage-61's (§8 F8).

### Rollout

The leg is live in the landing that adds it. Its first base has no step rows, so its first run prints
`0 landed row(s)`; it grades a row from the landing after the one that introduces it.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/steps.toml`
- `tools/govkit/steps/fanout_cap.py`
- `tools/govkit/govkit.py`
- `tools/govkit/registry.toml`
- `tools/govkit/selftest.py`
- `tools/govkit/refusal_join.py`
- `tools/hooks/kit.toml`
- `tools/hooks/README.md`
- `tools/gate-legs.json`
- `help/upgrade-steps.md`
- `help/README.md`

### Alternatives rejected

- An authored `introduced` commit (§8 F2).
- The frozen check as an arm of `kit epoch (shipped bytes move, the version moves)`, or of the step
  gate (§8 F4).
- Before-images as comments inside `.governance/policy.toml` (§8 F5).

## 5. Production-readiness checklist

- security — the reader is the step rows' write boundary, denying an unknown key, placeholder,
  interpreter or untracked program; steps run no target code, and a down never overwrites later edits.
- perf / scale — the derivation's walk stops at its first hit; measured at build on gov's history.
- error / empty / loading states — an empty `[[retired]]` population and a rowless base are announced
  with their counts; a malformed row exits 2 naming file, row and key.
- observability — `list` prints each row's order, id, introducing commit and file; `update` one line
  per succession.
- risks — the pass stages no guarded path, since the write the guard refuses moved to
  TOOL-dSafePassage-61 (§8 F8); an imported helper is not frozen (§7).
- testing — `tools/govkit/selftest.py` arms over scratch gov trees and targets.
- migration — §4 Migration.
- user docs — `help/upgrade-steps.md` (S10), and `tools/hooks/README.md`'s section on the file.

## 6. Acceptance criteria

The criteria AC13, AC14, AC15 and AC19 moved to TOOL-dSafePassage-61 on 2026-10-26, as its AC1
to AC4, and the size-limits half of AC16 as its AC5; the labels are not reused here.

- **AC1** — When `python tools/govkit/upgrade_steps.py list` runs on gov's tree after the build, it
  prints `agent-cap/fanout-cap-to-agents-in-flight` with its declaring file `tools/hooks/kit.toml` and
  `unlanded` or its introducing commit; over a scratch gov tree whose one commit adds a
  `tools/govkit/steps.toml` row and a descriptor row, it prints the steps-file row first.
  Red when: the reader skips descriptor rows, and the `tools/hooks/kit.toml` row is absent.
- **AC2** — When a scratch gov tree plants, one per run, an unknown key, an authored `introduced`, a
  `{bogus}` placeholder, `argv[0]` of `node`, a `{gov}/` program that is not tracked, a duplicate id,
  a descriptor row whose `<entry>` is another entry's, a `tools/govkit/steps.toml` row whose
  `<entry>` is a registry entry, a `surfaces` item with no `:`, and a `[[retired]]` row whose
  successor is not live, `upgrade_steps.py list` exits 2 naming that file, row and key.
  Red when: any planted case exits 0.
- **AC3** — When a scratch clone carries a row landed on `main` at commit X, and a branch adds a
  second row and merges `main` into itself, `upgrade_steps.py list` prints X for the first row and
  `unlanded` for the second; after `main` merges the branch at M, it prints M for the second.
  Red when: either row reads a commit off `main`'s first-parent line.
- **AC4** — When a branch of a scratch clone edits a landed row's `down` argv, then in a second run
  removes a landed row, then in a third edits one byte of a landed `{gov}/` program,
  `upgrade_steps.py frozen --base <main sha>` exits 1 each time, naming the id and the field or path;
  with the removal plus a `[[retired]]` row naming the removed id and its successor, it exits 0.
  Red when: a planted edit or a planted removal exits 0.
- **AC5** — When the branch instead adds a corrected step under a new id and leaves the landed row as
  it was, `upgrade_steps.py frozen --base <main sha>` exits 0; over a base holding no rows it exits 0
  printing `0 landed row(s)`.
  Red when: the new id reds, or the empty base prints no count.
- **AC6** — When a scratch gov tree's registry carries `[[retired]]` `old` with successor `new`, and
  a target's receipt claims `old`, `govkit.py update --target <t>` prints
  `retired old: claimed by its successor new` and no refusal; with `--write`, the receipt's `kits`
  holds `new` and not `old`.
  Red when: the run refuses with `no longer a registry entry`.
- **AC7** — When the successor is `none`, `govkit.py update --target <t> --write` names each of
  `old`'s rows `withdrawn` with an outbox order and deletes none of their files.
  Red when: the run refuses, or a file of `old` leaves the target.
- **AC8** — When the receipt claims an id that is neither a registry entry nor a `[[retired]]` id,
  `govkit.py update --target <t>` still refuses before writing.
  Red when: the run proceeds.
- **AC9** — When `govkit.py check --target <t>` runs on AC6's receipt, it prints
  `old: retired, successor new` and counts no problem for it; on AC8's receipt it still counts one.
  Red when: AC6's receipt prints probe A's `which is not a registry entry`.
- **AC10** — When a scratch target with a default policy file and a committed `.agent-cap.conf` of
  `FANOUT_CAP=2` runs S6's `up` argv and commits, gov's
  `python policy.py get runtime.agents-in-flight --rev <sha>` prints 2 at the commits before and
  after, `.agent-cap.conf` is gone, the policy file holds `agents-in-flight = 2`, and S6's `witness`
  argv exits 0, where it exited 1 before.
  Red when: the value after the step reads the default of 6.
  fixture: needs dGroundRules' policy kit at the build run's base.
- **AC11** — When S6's `down` argv runs after its up, `.agent-cap.conf` and `.governance/policy.toml`
  are byte-identical to the before state and `.governance/steps/agent-cap/` is gone; after an up
  killed once its before-image was written, it exits 0 and leaves the before state; when
  the policy file was edited after the up, it exits 1 naming the file and changes nothing.
  Red when: a byte differs after a down, or the edited file is overwritten.
- **AC12** — When `.agent-cap.conf` holds `FANOUT_CAP=abc`, or a second assignment `OTHER=1`, S6's up
  exits 1 naming the file and writes no byte, before-image included.
  Red when: the up exits 0, or any file under the target changes.
- **AC16** — When `python tools/govkit/upgrade_steps.py list --window` runs on gov's tree after the
  unit lands on `main`, it prints `.agent-cap.conf` closed by its step id; on a branch adding a step
  whose `surfaces` names a second home, it prints that home `open`.
  Red when: the unlanded step's home prints `closed`.
- **AC17** — When `tools/gate-legs.json` is read, a row named `step-rows-frozen` carries the argv
  `python {prefix}/govkit/upgrade_steps.py frozen`, and `tools/govkit/registry.toml` carries an
  `[[exempt_leg]]` row with that name.
  Red when: either row is missing, so `govkit selfcheck` reads the leg as unclaimed.
- **AC18** — When `help/README.md` is read, it links `help/upgrade-steps.md`, and that page names
  `[[upgrade]]`, `[[retired]]` and `runtime.agents-in-flight`.
  Red when: the page is missing or names none of the three.
## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `recall floor` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `memory-hygiene self-test` · `build-index selftest` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `dead-path carriers (deleted files still named)` · `method carriers (every pointer declared)` · `template size <=48KiB` · `leg ceilings clear their evidenced maximum` · `every held leg is budgeted, every budget row resolves` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The new leg `step-rows-frozen` is off the line above until this unit builds it; AC4 observes it red
and AC5 green.

New arm: tools/govkit/selftest.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 AC11 AC12 AC16 · each case staged by its own scratch gov tree or target, one planted row, receipt or file per arm · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by the measured count

What the frozen leg does not check: what a step program imports. S9 freezes the bytes of each program
a landed argv names, not its imports, so a landed step can still change through an import; the
freeze stays narrow, as dOrderedCharter spec 31 keeps its class reader in an imported module on
purpose. Nor whether a correction step reverses its defect, or any row the default branch has not landed.

## 8. Open questions

- **F1 — One mechanism per spec, or this clause in parts?** M2 asks one mechanism per spec; the
  clause holds a grammar, its reader, two steps and a frozen-row gate. (a) Carry it whole here. (b)
  Carry it in parts across new units, whose ids, minted by five writers at once, can collide, every
  part sharing the reader's one grammar. Recommendation (a), the split left to the spec audit.
  Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F2 — Is the introducing commit typed in the row, or derived?** The clause lists it among the
  row's fields; the brief's S1 keys it `introduced`. (a) Typed. (b) Derived from the default
  branch's first-parent history, `retired` likewise. A row cannot name the commit that lands it,
  whose id hashes the row, and any other typed commit copies a fact git owns (charter `[derive]`),
  so (a) fails the frozen comparison on its first row. The reader still returns `introduced`.
  Recommendation (b), departing from the clause's field list as deviation-11. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b).
- **F3 — What does a landed row freeze?** (a) Its id, introducing commit and argv, the clause's set.
  (b) Those, plus `surfaces`, the bytes of every `{gov}/` program its argv names, and every landed
  `[[retired]]` row. Under (a) an edited `surfaces` covers a later removal with no new step, an
  edited program changes what an unchanged down reverses (the shape audit's M31), and a removed
  succession row brings probe A back. `needs-target` stays mutable. Recommendation (b). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b).
- **F4 — Where does the frozen check run?** (a) Its own leg, `step-rows-frozen`. (b) An arm of
  `kit epoch (shipped bytes move, the version moves)`. (c) An arm of unit 10's step gate. (c) needs
  a later unit, which M2's ordering refuses; (b) makes one leg's red mean two things; (a) reuses
  `cmd_epoch`'s ladder through `derive_push_base`. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F5 — Where does a step keep what its down restores?** (a) A JSON before-image under
  `.governance/steps/`. (b) Comments in `.governance/policy.toml`. (c) No image: the down
  re-synthesises the files. A TOML comment holds no BOM or lone CR, and `.agent-cap.conf` is read
  BOM-led and CRLF (`tools/hooks/agent-cap.test.sh:1991`), so (b) and (c) fail `cl-dClosedLoop-0022`'s
  byte-identical down; (a) adds no install location (`tools/govkit/govkit.py:9170`, `:7039`).
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F6 — How are surface member ids spelled before the class registry exists?** The registry is unit
  10's, sequenced later. (a) This reader checks the `<class>:<name>` shape only, the rows spelling
  `conf-key:.agent-cap.conf#FANOUT_CAP` and `file:{prefix}/template-size-limits.txt`. (b) It checks
  membership too, which needs the later unit. Recommendation (a), the M2 cross-read reconciling the
  spellings with unit 10's registry before the first code pass. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F7 — How are rows ordered across declaring files within one commit?** The brief's S5 leaves files
  unordered. (a) The steps file first, then descriptors in registry entry order. (b) Descriptors
  first, so a descriptor step landing with the receipt step runs before the `steps` field exists.
  Recommendation (a). Rung 1, the brief's S5. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F8 — Who moves gov's own caps, given the minimal guard?** `cl-dClosedLoop-0012`'s guard refuses
  every agent write to the policy file but one cap raise, and S8 writes every `budgets.*` row at once.
  (a) This unit's pass runs S7 on gov, every cap reading unchanged. (b) Unit 8's lander runs it in the
  prepared merge. (c) Gov keeps the file until an attended run moves it. (c) fails unit 8's red on a
  witness that does not hold on gov and leaves an `[[exempt]]` row naming a removed file; (b) leaves
  a registry row and a file disagreeing until the landing; (a) fails only veto 3, if the landed guard
  refuses a value-preserving write. Recommendation (a), rung 5, "Standing ruling takes it
  (Recommended)" (ER:388), that write shape asked of dGroundRules as `TOOL-dGroundRules-13` in
  `memory/builds/dGroundRules/BACKLOG.md`.
  RESOLVED (agent, 2026-10-23, delegated): (a) · widens: none · relaxes: none
  The build run's first pass reads whether the landed guard grants it, and stops S8 if not.
  F8's stop fired, 2026-10-26: the landed guard refuses; S8 and S7 moved to TOOL-dSafePassage-61.
  The guard's `check_raise_shape` refuses S8's seven-key write (`tools/policy/guard.py:150-151`).
  S7's row moved too: declared in a landing without gov's migration, TOOL-dSafePassage-8's gov-first
  walk would run its up on gov in the prepared merge and commit the same refused shape through
  `commit-tree` (`tools/push-main.sh:921`), where no hook fires. S6 stays: gov tracks no
  `.agent-cap.conf`, so its up exits 0 on gov and writes nothing.
- **F9 — What does this unit do while its parent is unbuilt?** dGroundRules is specced and DEFERRED,
  its clauses (§3's first edge) this unit's contract. (a) The build run re-grounds against the landed
  parent first, takes its module paths, table layout, writer and legacy-home parser as spelled, and
  bumps this spec's rev where any differs from §4. (b) Fix the parent's names here, inventing names
  its clauses own, which the brief forbids. Recommendation (a). Rung 1, the brief's parent rule.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F10 — When `FANOUT_CAP` does not lower the key, does the step write the key?** (a) No: the file
  is retired and the policy file left byte-identical. (b) Write the key's current value, restating a
  catalogue default (charter `[one-fact]`). Both meet AC10. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F11 — What happens to a retired kit's rows when its successor is `none`?** (a) They route to the
  existing `withdrawn` arm: a report and an outbox order, deleted only under `--write-withdrawals`.
  (b) The run refuses, as today, keeping `gap-deploy-15` open. (a) reuses the arm at
  `tools/govkit/govkit.py:10741-10778`, whose rename path already degrades an unknown kit's row to
  `withdrawn` (`:9610-9621`). Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F12 — What does S8 leave of the policy kit's limits-file machinery?** `budgets.py`'s `limits:`
  branch retires with the file. (a) The seven census rows take a `policy` `home` form, a value held
  only under `budgets.<cap>`, which this unit adds to `HOME_FORMS` and the census join (S8);
  `arm_limits_readers`' row and the cases planting the file go, and `budgets-two-homes` is
  re-planted on a `conf:` home. (b) The rows keep `limits:` naming an absent file, the arm's reader
  directory moving to `tools/govkit/steps/`: a home and an arm over a file no tree holds.
  Recommendation (a), charter `[yagni]`. Rung 3. RESOLVED (owner, 2026-10-24): (a).
  Moved with S8 to TOOL-dSafePassage-61, its §8 F2, on 2026-10-26.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §8 F8 cites the ask `TOOL-dGroundRules-13` for the withdrawn deviation-12.
- rev-3 · 2026-10-23 · §3 Edges gain `TOOL-dSafePassage-17`, `-20`, `-26`, the round-1 audit's ends.
- rev-4 · 2026-10-23 · §3 Edges gain the hands-off `TOOL-dSafePassage-4`, for check 12's reciprocity.
- rev-5 · 2026-10-23 · §8 F8's mark reads `widens: none · relaxes: none`.
- rev-6 · 2026-10-23 · re-pins `cl-dClosedLoop-0018` from `ed08a364` to `d4cade33`; §1 to §10 unmoved.
- rev-7 · 2026-10-24 · §2 S5 to S8, §3, §4, §6 AC10, AC13, AC15, AC16, §8 F8, F9 and new F12:
  re-grounded by the dGroundRules cross-check.
- rev-8 · 2026-10-24 · §6 AC15's grep excludes the step's own files.
- rev-9 · 2026-10-24 · §2 S8 and §8 F12 read the owner's pick (a), from the owner-forks brief;
  prose trimmed.
- rev-10 · 2026-10-25 · S8 · §4 Files touched · AC19 · §7 · §8 F12 · Items 1 to 3 of
  `2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`: S8 adds the `policy:` home to `HOME_FORMS`,
  `resolve_caps` and `arm_cap_census`, observed by AC19; §7 states the import gap; prose trimmed, and
  trimmed again for the records rows.
- rev-11 · 2026-10-26 · §1 · S5 · S7 · S8 · §3 · §4 · §5 · AC1 · AC13 · AC14 · AC15 · AC16 · AC19 · §7 ·
  §8 F8 · F12 · S7, S8, AC13, AC14, AC15, AC19 and the size-limits halves of S5 and AC16 moved to
  TOOL-dSafePassage-61 at F8's stop, by `2026-10-26-prompt-TOOL-dSafePassage-61-1-spec-writer.md`;
  the clause is carried in two parts.

## 10. Reuse audit

Seams extended, found by `python tools/codebase-map/reuse_lookup.py "declare a versioned
upgrade step in a kit descriptor and read it at a commit"`: `read_descriptors`
(`tools/govkit/govkit.py:13238`), which reaches the new table with no new loader; `load_registry`
(`:247`) for the `[[retired]]` table; `cmd_epoch`'s base ladder (`:13446-13474`), extracted as
`derive_push_base` at its second instance; `resolve_remote` (`:558`) for the default branch; the
`withdrawn` arm (`:10741-10778`) for a successor of `none`; and govkit's `Refusal` with the refusal
join's anchors. The lookup also ranked `read_blobs_at` (`tools/memory-tree/tree_lib.py`), another
kit's, which govkit may not import, so the new module reads blobs with `git cat-file`. A record's
`_cmd_update` cites are an older `govkit.py`'s. Recall added `TOOL-aFlaggedScaffold-3` (no arm for a
source gov starts shipping), not widened here, and `TOOL-dRetiredFork-38` (§3).

Recall terms used: `python tools/memory-recall/query.py "how does govkit update handle a retired
kit, an upgrade step, or a moved conf key" --terms "govkit update receipt registry entry retired
successor descriptor upgrade step withdrawn migration conf"`
