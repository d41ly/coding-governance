# The `subject` descriptor census, re-derived — and a number my rev-3 spec got wrong

**Serves:** research TOOL-aGatheredDeclaration-6

Written while the round-3 spec audit was running, so the specs it corrects could not be edited
without changing the blobs that audit is reading. **The correction is owed to
`TOOL-aGatheredDeclaration-6` §2 S1(e) and is applied at the round-3 fold**, not here.

## What rev-3 asserts, and what is true

`TOOL-aGatheredDeclaration-6` S1(e) currently reads *"68 `subject = ` rows across 23 descriptor
TOMLs, 21 under `tools/govkit/entries/` and the rest in other kits' `kit.toml`"*. The first two
figures are right and the third is wrong. Re-derived at base `44734f15` with
`grep -rn '^subject = ' --include='*.toml'` excluding `memory/`:

| population | rows | files |
|---|---|---|
| `tools/govkit/entries/` | 18 | 11 |
| every other kit's `kit.toml` | 50 | 12 |
| **total** | **68** | **23** |

So the split is **18 rows in 11 files** under `entries/`, not 21. The per-kit rows outside
`entries/`: `memory-tree` 16, `workflows` 7, `run-gates` 6, `codebase-map` 3, `drift-audit` 3,
`lexicon` 3, `unattended` 3, `agent-instructions` 2, `hooks` 2, `memory-recall` 2, `playbook` 2,
`pytest-parallel-guardrails` 1.

**Where the wrong number came from, because that matters more than the number.** The round-2 audit's
R6 reported "21 of them under `tools/govkit/entries/`", and the fold copied it into the spec without
re-deriving. That is the exact defect class this build exists to remove — a figure written beside the
thing it counts, correct when somebody typed it and unowned afterwards — committed by the fold that
was fixing an instance of it. The audit's total and its file count were both right, which is what
made the third figure look safe to carry.

The load-bearing claim survives unchanged: S1(e)'s point is that the key is read by considerably more
of govkit and its descriptor population than rev-2's "three changes" priced, and 68 rows across 23
files says that whether 18 or 21 of them sit in one directory.

## A second, smaller correction to the same audit finding

R7 named `.codebase-map.conf:13` as "a second carrier of the same string", alongside
`.governance/deploy.toml:44`'s `gate_commands`. Re-read at source, those are two different things.
`.governance/deploy.toml:44` genuinely OWNS the entry-point sentence and is rendered into
`AGENTS.md:250` through `{{GATE_COMMANDS}}`. `.codebase-map.conf:13` is a PROSE COMMENT that happens
to mention `tools/gate-legs.json`; it carries no placeholder and nothing renders from it.

Both still belong in `TOOL-aGatheredDeclaration-6`'s files-touched, but for different reasons and at
different times: `deploy.toml` because S11 must edit the source rather than the render, and
`.codebase-map.conf` only because S10's dead-path waiver set has to account for one more carrier of
the deleted basename. The rev-3 text treats them as one class; the fold separates them.

## What this record does NOT claim

- No count here was taken from the audit. Every figure was re-derived by the greps named above, on
  this tree, at this base.
- The nine `govkit.py` line references in S1(e) were NOT re-verified here. They came from the round-2
  audit, which states it re-derived every citation at base `44734f15`, and the two I spot-checked
  independently (`:6620`'s closed key tuple and `:2947`'s grammar refusal) were exact. The remaining
  seven are carried on that record's word, and this sentence is what makes that visible.
