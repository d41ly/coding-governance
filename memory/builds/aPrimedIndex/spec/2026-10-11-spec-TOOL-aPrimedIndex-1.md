# TOOL-aPrimedIndex-1 — every generated output a bar leg grades declares its write and check commands in its kit's descriptor

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPrimedIndex-1-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPrimedIndex-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1-2-build-brief.md) | journal | TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4 |
| [2026-10-11-prompt-TOOL-aPrimedIndex-1.md](../prompts/2026-10-11-prompt-TOOL-aPrimedIndex-1.md) | research | TOOL-aPrimedIndex-2 TOOL-aPrimedIndex-3 TOOL-aPrimedIndex-4 |

<!-- /gen:spec-records -->

## 1. Goal

Declare, once and in the kit that generates it, how every output a merge-bar leg grades for
freshness is rewritten and how its freshness is proved, so one reader can regenerate or check the
whole set without a hand-kept list.

## 2. Scope (IN)

- **S1** — The `[[generated]]` descriptor table gains three optional keys: `write` and `check`, each
  an argv array, and `stage`, a positive integer. A row carries all three or none. Observed by AC1.
- **S2** — The `[[regenerate]]` descriptor table gains two optional keys: `stage`, a positive
  integer, and `check`, an argv array. A row carrying `stage` joins the regeneration set; its
  freshness is proved by its own `check`, else by its kit's `[check]` argv. Observed by AC1.
- **S3** — The rows of §4's inventory carry those keys: three record and code indexes on
  `[[generated]]` rows, eight kit renders on `[[regenerate]]` rows. Observed by AC1 and AC2.
- **S4** — Every key added is invisible to the two existing readers of these tables: the unattended
  kit's `resolve_generated_indexes` and govkit's `[[generated]]` grading and `[[regenerate]]` argv
  derivation. Observed by AC3 and AC4.
- **S5** — The stage meaning is written once, in the run-gates kit README beside the reader that
  honours it: 1 renders from kit templates, 2 indexes over the records, 3 the codebase map, which
  reads the output of both. Observed by AC5.

## 3. Non-goals (OUT)

- No reader. The verb that resolves and runs these rows is TOOL-aPrimedIndex-2.
- No row for an output that is not derived from the tree alone. Excluded, with the reason each is
  out:
  - `CLAUDE.md`: its render takes an alias set the project chooses, which a shipped descriptor
    cannot know, and its kit declares no `[[regenerate]]` row.
  - `tools/govkit/subject-pins.tsv`: a change ratchet, and regenerating it is the decision it
    records.
  - Kit version carriers: the lander mints them.
  - `tools/run-gates/ceiling-evidence.txt` and the pooled self-test evidence: node-local run history.
  - Runlog records: node-local journals.
  - The template-size and README-slot high-water files: ratchets.
  - The kickoff manifest's `last-audit` stamp: a manual re-verification.
  - memory-tree's `--arm-routing` regenerate row: an adopter migration that writes
    `.memory-tree.conf`, never a render.
- No govkit grading of the new keys. The reader refuses a malformed row at the moment it would be
  used, which is every bar.
- No version bump by hand; the lander mints.

### Edges

- **hands-off** `TOOL-aPrimedIndex-2` — the reader that resolves these rows, runs them and refuses a
  malformed one.

## 4. Design

### Data model

```toml
[[generated]]
path = "{memory_root}/LIVE.md"
generator = "gen_build_index.py"
why = "..."
write = ["python", "{kit}/gen_build_index.py", "--write"]
check = ["python", "{kit}/gen_build_index.py", "--check"]
stage = 2

[[regenerate]]
argv = ["bash", "{kit}/adopt-lexicon.sh", "--render"]
stage = 1          # proved fresh by this kit's [check] argv
```

The argv tokens are the four the descriptors already spell: `{kit}`, `{prefix}`, `{memory_root}`
and `{map_root}`. An argv beginning `python` or `python3` names the interpreter the reader resolves,
never a launcher on `PATH`. Rows sharing one `write` and one `check` are one regeneration item with
several paths: the build index's three rows are one item.

The keys are written at column 0 as TOML arrays and integers. The two shell readers of these tables
match only `path`, `generator` and `when` lines, so a new key is a line neither reads.

### Inventory

PINNED, measured 2026-10-11 on node `a` against base b726385f by reading every `[[gate_leg]]` and
manifest leg that byte-compares a file with a fresh render.

| Stage | Kit | Outputs | Write | Check | Leg that grades it |
|---|---|---|---|---|---|
| 1 | memory-tree | `HYGIENE.md`, `TEMPLATE-SPEC.md`, two guides | `adopt-memory-tree.sh --render` | `kit-dogfood-parity.test.sh` | `kit/dogfood doc parity` |
| 1 | workflows | `REVIEW-PROTOCOL.md`, five rendered scripts | `check-protocol-parity.test.sh --render --tracked-only` | the same script, no flag | `review-protocol parity (kit vs dogfood)` |
| 1 | unattended | its Skill, five guides, the playbook fixture | `adopt-unattended.sh` | its `[check]` | `unattended skill wiring` |
| 1 | lexicon | its Skill | `adopt-lexicon.sh --render` | its `[check]` | `lexicon wiring` |
| 1 | memory-recall | its Skill | `adopt-memory-recall.sh --scaffold` | its `[check]` | `memory-recall skill wiring` |
| 1 | drift-audit | its Skill | `adopt-drift-audit.sh` | its `[check]` | `drift-audit wiring` |
| 1 | runlog | its Skill | `adopt-runlog.sh --scaffold` | its `[check]` | `runlog skill wiring` |
| 1 | playbook | the `gov:playbook` region of the charter | `adopt-playbook.sh --target .` | its `[check]` | `playbook render wiring` |
| 2 | memory-tree | `LIVE.md`, the ledger and backlog views, README and spec regions | `gen_build_index.py --write` | `gen_build_index.py --check` | `memory hygiene` |
| 2 | memory-tree | `gotchas/INDEX.md` | `gotchas.py --write` | `gotchas.py --check` | `memory hygiene` |
| 3 | codebase-map | `{map_root}/generated/` | `gen_map.py --write` | `gen_map.py --check` | `codebase-map coverage + freshness` |

memory-tree declares two identical `--render` rows; `stage` and `check` go on the first, and the
reader joins the two by their argv. Its `[check]` declares `none`, and so does workflows', so both of
their rows carry a row-level `check`.

### Files touched (estimate)

- `tools/memory-tree/kit.toml`
- `tools/codebase-map/kit.toml`
- `tools/workflows/kit.toml`
- `tools/unattended/kit.toml`
- `tools/lexicon/kit.toml`
- `tools/memory-recall/kit.toml`
- `tools/drift-audit/kit.toml`
- `tools/runlog/kit.toml`
- `tools/playbook/kit.toml`
- `tools/run-gates/README.md`

### Alternatives rejected

- **One new descriptor table for the whole set.** It would restate the eight render argvs the
  `[[regenerate]]` rows already carry and the five `[check]` argvs beside them, two answers to one
  question per kit.
- **Index generators as `[[regenerate]]` rows.** govkit's `update` and `mint` run every such row, so
  this would start rewriting an adopter's indexes on every kit update and roll a kit back when a
  generator refused. That is a deployer change this build was not asked for.
- **Renders as `[[generated]]` rows.** The unattended kit reads that table as "outputs a pass never
  chooses to write": `--dispatch` would refuse a pass declaring a render beside its adopter, which
  is ordinary kit work, and check 23 would stop counting a hand edit of the charter.
- **A project-level list in the run-gates kit.** Authored beside the kits it describes, it goes stale
  the day a kit adds an output, and an adopter's kit set differs from gov's.

## 5. Production-readiness checklist

- security: N/A — the new keys name commands from files the repo already executes on every bar.
- perf / scale: the declaration costs nothing; the reader's cost is TOOL-aPrimedIndex-3's.
- error / empty / loading states: a row carrying some of `write`, `check` and `stage` is refused by
  the reader, never half-read.
- observability: TOOL-aPrimedIndex-2's listing prints the resolved set.
- risks: a new key mistyped at a non-zero column reaches tomllib and not the shell readers; AC3 and
  AC4 observe both reader families unchanged.
- testing: the direct probes in §6; the reader's arms belong to TOOL-aPrimedIndex-2.
- migration: none. Absent keys keep every existing row's meaning, and an adopter receives the rows
  with its next kit update.
- user docs: the run-gates kit README states the keys and the stage meaning (S5).

## 6. Acceptance criteria

- **AC1** — When `python -c` reads every tracked kit descriptor with `tomllib` and prints each row
  carrying `stage`, it prints the eleven rows of §4's inventory, and every `[[generated]]` row
  carrying one of `write`, `check` and `stage` carries all three. Red when: a row of the inventory is
  missing, or a `[[generated]]` row carries a partial set.
  figure: PINNED at eleven by §4's inventory.
- **AC2** — When each staged row's `check` argv, or its kit's `[check]` argv, is run from the repo
  root, every one exits 0 on this tree. Red when: an argv names a file the kit does not ship, or a
  check that cannot pass on a fresh tree.
  cost: about two minutes concurrently on the loaded node `a`, measured 2026-10-11.
- **AC3** — When `resolve_generated_indexes` from `tools/unattended/lib-unattended.sh` is called on
  this tree before and after the edit, its two outputs are byte-identical. Red when: a new key line
  is read as a path, generator or `when` value.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` runs, check 6c reports no `[[generated]]`
  row on which the shell reader and tomllib disagree. Red when: a key written off column 0 or
  single-quoted makes the two readers disagree.
  cost: over 90 s on node `a`.
- **AC5** — When `grep -n "stage" tools/run-gates/README.md` runs, it shows the three stage meanings
  and the two keys of each table. Red when: a stage value is used in a descriptor and named nowhere.

## 7. Gates

`codebase-map coverage + freshness` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `drift-audit selftest` · `lexicon selftest` · `pre-push run-log line` · `runlog selftest` · `run-gates run-log line` · `govkit acceptance matrix` · `playbook render selftest` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test`

The legs after `memory hygiene` are the narrow guards the descriptors trip, every one a held
self-test; the bar at the close runs them only under the owner's on-demand switch.

The epoch leg is owed because every descriptor named above is shipped bytes; the lander mints the
versions it owes.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

The seam is the `[[generated]]` table read by `resolve_generated_indexes` in
`tools/unattended/lib-unattended.sh`, which `tools/codebase-map/reuse_lookup.py` ranked as a seam
for "regenerate every generated index before the merge bar runs", and the `[[regenerate]]` table
with each kit's `[check]` argv. Both are extended with keys; no new table is added.

Recall terms used: `python tools/memory-recall/query.py "is regenerating generated indexes enforced before the merge bar runs, so a stale index does not red the bar" --terms "generated index stale regen render --write freshness leg bar pre-push lander prepare gotchas symbols LIVE.md"`.
