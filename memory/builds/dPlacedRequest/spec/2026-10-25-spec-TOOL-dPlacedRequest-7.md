# TOOL-dPlacedRequest-7 — the probe program: eight items, the `probe` and `probe-trigger` records, and the four `probe.*` keys

**Status:** CLOSED · rev-9 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 15 · advances TOOL-dPlacedRequest-22 · closes TOOL-dPlacedRequest-69

**Carries:** cl-dClosedLoop-0125@4e0727e5 whole
**Carries:** node:item.probe.trigger
**Carries:** node:item.probe.pin
**Carries:** node:item.probe.design
**Carries:** node:item.probe.experiment
**Carries:** node:item.probe.run
**Carries:** node:item.probe.judge
**Carries:** node:item.probe.judge-claimed
**Carries:** node:item.probe.return
**Carries:** node:record-kind.probe
**Carries:** node:record-kind.probe-trigger
**Carries:** node:policy-key.probe.points
**Carries:** node:policy-key.probe.raise
**Carries:** node:policy-key.probe.observations
**Carries:** node:policy-key.probe.experiment.authority

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-26-build-TOOL-dPlacedRequest-7-deviation-71.md](../build/2026-10-26-build-TOOL-dPlacedRequest-7-deviation-71.md) | deviation | — |
| [2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-7-1-acceptance-ledger.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-34 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-26-prompt-TOOL-dPlacedRequest-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dPlacedRequest-1-parents-reground.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-34 |
| [2026-10-26-prompt-TOOL-dPlacedRequest-7-1-spec-reviewer.md](../prompts/2026-10-26-prompt-TOOL-dPlacedRequest-7-1-spec-reviewer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dPlacedRequest-7-2-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dPlacedRequest-7-2-spec-writer.md) | journal | — |
| [2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-crosscheck.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-1-asks-adopt-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-1-asks-adopt-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-20 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-7-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-7-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-7-2-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-7-2-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-7-divergence-2-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-7-divergence-2-brief.md) | research | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-7-divergence-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-7-divergence-brief.md) | research | — |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

No testing happens outside Test: an owner's observation cannot be verified before placement, a
reported bug cannot be made red before its fix, no experiment can set a measured reference, and 61 of
81 items have no role that could ask for a test (gap-flow-18). The unattended driver's `TESTING`
position exists only as a phase word (`tools/unattended/unattended.sh:852`). P31 makes testing a
program with two ways in (v2:1024-1028): placed at an item boundary by `probe.points` or the owner, or
raised by a role's `probe` outcome under `probe.raise`. This unit lands flow-steps' `[probe]`
program (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:605-675`):
its eight items, the `probe` and `probe-trigger` record kinds, the commands behind `probe.trigger`,
`probe.pin`, `probe.run`, `probe.judge` and `probe.return`, the role steps `probe.design` and
`probe.experiment`, its record handed to the asking item, an
entry-time probe keyed by content as triage is, the four keys, and a stand-in for each later part.

## 2. Scope (IN)

- **S1** — The items: eight `[[item]]` rows of `tools/loop/loop.toml` in TOOL-dDeclaredLoop-12 S1's
  shape, tags `item.probe.trigger`, `.pin`, `.design`, `.experiment`, `.run`, `.judge`,
  `.judge-claimed` and `.return` (I17), each with the actor, needs, witness, outcomes and routes of
  flow-steps.md:632-639, as §4's table states, and `step = "none"`. `check_program`'s admission of
  `step = "none"`, which TOOL-dDeclaredLoop-50 S3 grants rows whose tag's middle segment is `review`,
  reads the tuple `PROGRAM_SEGMENTS = ("review", "probe")` in `tools/loop/loop_lib.py`. The tester's
  two items spell their actor `role:gov-tester`, the slot the Test rows already spell
  (`tools/loop/loop.toml@b6651f21:1725`) and TOOL-dWitnessedBar-23 S7 writes. Observed by AC1 and
  AC13.
- **S2** — The stand-ins, flow-steps.md:666-675, ride the item rows and add no `[[stand-in]]` row
  (F10). That table names the owner of a row item, one a `[[transition]]` row names, and
  `tools/loop/loop_table.py#check_transition_tables` refuses a stand-in row naming no row item as
  stale; no transition row names a probe item. Each unbuilt part rides its item's own `owner` field,
  the build that lands it, and a `stand-in:{prefix}/<home>/<file>` route where its work leaves the
  program today:

  | Item | `owner` | Today's stand-in |
  |---|---|---|
  | `item.probe.design` | `dWitnessedBar` | the tester role is pending, and the owner writes the method through `probe.py design` |
  | `item.probe.judge-claimed` | `dWitnessedBar` | the same pending role; the claimed judgment reaches the owner item by `item.probe.return`'s `claimed` route |
  | `item.probe.experiment` | `dBoundRoles` | its `beyond-authority` route to the owner item, which `probe.py` prints naming `dBoundRoles` while the `experiment` shape is unbuilt |
  | `item.probe.run` | `dWellOiledMachine` | `probe.py run`, calling TOOL-dDeclaredLoop-17 S4's re-run |
  | `item.probe.return` | `dTotalRecall` | S5's write through the record factory, `Writer: stand-in`, and its `returned` route to `stand-in:{prefix}/loop/probe.py` |

  The other three items' `owner` is `dPlacedRequest`. A method entry marked `visual`, which needs
  dWellOiledMachine's capture adapter, is `unrunnable` (F7). Observed by AC1 and AC6.
- **S3** — `probe.trigger`, the verb `python tools/loop/probe.py trigger --cause <c> --asker <item tag>
  --subject <text> (--build <slug> --unit <id> | --request <content key>) [--at <item tag>]`, in
  `review.trigger`'s flag shape (TOOL-dDeclaredLoop-20 S2). `--unit` stands beside `--build`, since
  `tools/memory-tree/build_records.py#write_record` names a build-folder record by its unit id (F14);
  `--build` without `--unit` exits 2. `<c>` is one of the closed set I17 names,
  `point`, `owner`, `observation`, `raised` and `reproduction`, held as data: `[[trigger-cause]]` rows
  of `tools/loop/loop.toml`, each `program = "probe"` and `cause`, read by `read_trigger_causes(program)`.
  It opens the probe and writes a `probe-trigger` record, or, when a key below refuses the cause,
  writes nothing and prints `probe — not opened · <key>: <why> · to <asker>`, its route
  `stand-in:{prefix}/loop/probe.py` (F13). Observed by AC2 and AC3.
- **S4** — `probe.pin`, `python tools/loop/probe.py pin --trigger <record> --sha <sha> --kind
  verification|reproduction|experiment --question <text> --losing <text>`, writes the `probe` record's
  head (`Sha`, `Kind`, `Question`, `Losing`, `Asker`, `Trigger`) and records it, committed where the
  record lives in the tree, before any command runs (F8). A build-folder record is committed alone,
  subject `probe pin(<asker>): <kind>`. An entry-time trigger's head is written as
  `<content key>.probe.md` in the git-common-dir `requests/` store and committed nowhere, since that
  store is outside the tree. A SHA that does not resolve exits 2. An experiment routes to
  `item.probe.experiment`, the others to `item.probe.design`. Observed by AC4.
- **S5** — The method, `probe.run`, `probe.judge` and `probe.return`. `python tools/loop/probe.py
  design --probe <record> --cmd <command> --expect <exit>:<hash> [--mark "judge claimed"] [--mark
  visual]` is the method's one writer (F5): each call appends one entry to the record's `Method`
  section. It refuses an `--expect` outside `tools/loop/loop_witness.py#EXPECT`, a `--mark` outside
  the two, a command holding the field separator, and a frozen record, one already holding a `run`
  line (F9), each with exit 2 and the record's bytes unchanged. `python tools/loop/probe.py run
  --probe <record>` reads the `Method` entries. An entry marked `visual` makes it run nothing and
  write `Verdict: unrunnable` and `Judged: computed`, routing to `item.probe.return`. Otherwise it
  calls `tools/loop/loop_witness.py#run_rerun` once, as `loop_witness.py rerun --sha <pinned>` with
  one `--cmd` and `--expect` pair per entry, never a second runner, and writes each `run · <exit> ·
  <hash> · <command>` line. `judge` reads the re-run's per-command answers: every one `confirmed` is
  `confirmed`, any `refuted` is `refuted`, otherwise `inconclusive`, written as `Verdict` with
  `Judged: computed`. A method holding a `judge claimed` entry is written `Judged: claimed` with no
  `Verdict` and routes to `item.probe.judge-claimed` (F6). `return` writes `Writer` (`stand-in` until
  the executor lands) and prints `probe — <verdict> · <record> · to <asker>`, the line the asking
  item's re-entry reads as its input (flow-steps.md:35-36); a record `Judged: claimed` or `Verdict:
  unrunnable` routes to an owner item, named in the asker's place. Observed by AC5, AC6 and AC14.
- **S6** — The record kinds, rows of the record factory `tools/memory-tree/build_records.py`
  (PLAY-dOrderedCharter-7 S7), in the shape TOOL-dDeclaredLoop-17 S1 gives its `acceptance` kind:
  `record-kind.probe-trigger`, `<date>-build-<unit id>-probe-trigger-<n>.md`, served as
  `**Serves:** probe-trigger <unit id>`, fields `Cause`, `Asker`, `Subject`, `At` and `Key`; and
  `record-kind.probe`, `<date>-build-<unit id>-probe-<n>.md`, served as `**Serves:** probe <unit id>`,
  fields `Sha`, `Kind`, `Question`, `Losing`, `Asker`, `Trigger`, `Verdict`, `Judged` and `Writer`,
  then a `Method` section of entries, then the `run` lines. A method entry is one line, `- method ·
  <exit>:<hash> · <command>`, with the optional trailing fields `judge claimed` and `visual`, each
  after a ` · ` separator (F5). `Verdict` is closed per `Kind`: `confirmed`, `refuted`,
  `inconclusive`, `unrunnable` for a verification or a reproduction, `measured`, `within-noise`,
  `aborted`, `unrunnable` for an experiment (flow-steps.md:622-624). `Judged` is closed at `computed`
  and `claimed`, a second fact beside `Verdict` (F6). The kinds join the reader in the same pass:
  both are added to `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`, which the factory's
  kind table must equal at import (PLAY-dOrderedCharter-42 S1, S2), and to the closed `<kind>` list of
  `tools/memory-tree/HYGIENE.template.md` (its S5); under its S3 a `-probe-<n>.md` or
  `-probe-trigger-<n>.md` file served as any other kind is malformed. `probe.py` writes each
  build-folder record through `tools/memory-tree/build_records.py#write_record`, passing the
  `--build` slug, the `--unit` id, a title and the fields, in the shape §4's records show. The
  factory's `DOORS` lists the kinds `new <kind>` writes, every other kind being `write_record`'s
  alone, so this unit claims no `new probe` or `new probe-trigger` door. Observed by AC7.
- **S7** — The entry-time probe. Before `entry.claim` no build folder exists, so a trigger given
  `--request <content key>`, the key `tools/loop/request.py#derive_request_content_key` derives (I11),
  writes its records beside that request's local text (I12):
  `<git-common-dir>/requests/<content key>.probe-trigger.md` and `<content key>.probe.md`, in the
  record kinds' field grammar, minting no id (flow-steps.md:632). A request holds one entry-time
  probe: a trigger for a key whose probe is open with a new subject joins it, adding its `Subject`
  line and printing `probe — joined · <record>`, so placement may trigger once per observation; the
  same subject again exits 1 as already opened. The design then declares a command per subject, and
  the judge's aggregate verdict covers them all. Observed by AC8.
- **S8** — The `probe` outcome on every role item: each `[[item]]` row whose actor is a role and whose
  `outcomes` is a list gains `probe`, routed to `stand-in:{prefix}/loop/probe.py` (flow-steps.md:35-36),
  never to `item.probe.trigger` (F11). A role item sits in a gov step and the probe program in none,
  so a route to a probe item would cross a step, and the route join of
  `tools/loop/loop_table.py#check_transition_tables` refuses a cross-step route that no build row and
  no `[[owed-row]]` covers. The probe program's own role items, `item.probe.design`,
  `item.probe.experiment` and `item.probe.judge-claimed`, take no `probe` outcome (F12). A check
  `check_probe_outcomes(items)` in `tools/loop/loop_lib.py` refuses a role item outside the probe
  program that lacks the outcome or routes it to another target, and an `item.probe.*` row that
  carries it. Until dBoundRoles puts the outcome on the role templates, no role returns it, so probes
  are placed, never raised (flow-steps.md:672). Observed by AC9.
- **S9** — The keys, each read through dGroundRules' `policy.py get` (I24), with v2's catalogue
  default until that reader lands. Their four rows already exist in `tools/policy/catalogue.toml`,
  owner `dPlacedRequest`, landed by TOOL-dGroundRules-1 at `c9bd97720`; this unit adds no row through
  the policy-key factory and edits a row in place only where a value differs from v2 (v2:1248-1251):
  `probe.points`, a set of item tags in `review.breakpoints`' grammar, its row's `allowed` a
  `{ type = "set", item = … }` table (TOOL-dGroundRules-1 §4) with `empty = "allowed"` and default
  `[]`, v2's `none`, so PLAY-dOrderedCharter-36 S4 reads it as tag-valued and TOOL-dDeclaredLoop-26
  S6's `read_tag_policy` reads it (TOOL-dDeclaredLoop-6 S4 names no `empty` flag, so the build run
  passes it as the landed factory admits), listed by `probe.py points --build <slug>`, a tag the
  loop definition does not declare refused naming the key; `probe.raise` (`roles-and-owner`,
  `owner-only`, `off`), refusing `raised` under `owner-only` and `off`, and `owner` under `off`;
  `probe.observations` (`verify-before-place`, `verify-at-plan`, `on-request`), admitting the cause
  `observation` at `--at item.entry.place` under `verify-before-place` and at `item.plan.input` under
  `verify-at-plan`, and refusing it at every position under `on-request`, where the owner opens a
  probe with `--cause owner`, which `probe.raise` governs, and no request flag is minted (F15); and
  `probe.experiment.authority` (`within-cap`, `owner-opts-in`, `free`), named with its value on the
  owner item an experiment routes to, the cap under `within-cap` being the agent cap
  `tools/hooks/agent-cap.js` enforces (:61-71). Observed by AC3 and AC10.
- **S10** — The fixture, `python tools/loop/probe.py --fixture --plant <case>`, a throwaway repository
  in the system temp directory with a stub policy kit and a pinned commit, each case printing its
  observation. `python tools/loop/probe.py --selftest` runs every case through
  `tools/loop/loop_lib.py#run_selftest_cases`, printing the count line the `testsuite counts (every
  bar self-test prints one)` leg reads, as `tools/loop/request.py --selftest` does. The leg `loop
  probe fixtures`, argv `python {prefix}/loop/probe.py --selftest`, runs it. It holds the rows
  `loop request fixtures` holds, each read at writing:

  | Where | The row |
  |---|---|
  | `tools/gate-legs.json` | its leg row, `chunk = "selftests"`, `subject = "kit"`, `stage = ["step.test"]`, a `ceiling` the builder pins from the leg's first reading, and `enforces = ["principle.p31"]` (`tools/gate-legs.json@9934afd2:2232`) |
  | `tools/govkit/registry.toml` | an `[[exempt_leg]]` row with its `why`: the leg is gov's own and no `[[gate_leg]]` of the loop kit's descriptor (`tools/govkit/registry.toml@3c7b9224:898`) |
  | `tools/govkit/subject-pins.tsv` | its `<name>`, `kit`, `selftests` row, written by `govkit.py selfcheck --write` (`tools/govkit/subject-pins.tsv@33c34be4:102`) |
  | `tools/run-gates/selftest-budgets.txt` | its budget row, the seconds PINNED from a reading the row names (`tools/run-gates/selftest-budgets.txt@9b31304a:82`) |
  | `memory/map/features/loop.md` | its name in the dossier's `gate-legs` list (`memory/map/features/loop.md@801045ca:13`) |

  `tools/run-gates/ceiling-evidence.txt` gains no row: `derive-ceilings.py --write` generates it from
  run records, and it holds none for `loop request fixtures`. The page `help/loop.md` gains the
  probe's section. P31 is the
  principle whose v2 `[enforcement]` row names this unit's clause `cl-dClosedLoop-0125` (v2:1853).
  The pending list holds the row `principle.p31`, armed by `dPlacedRequest`
  (`tools/playbook/core-pending.txt@6e02f812:22`), and this pass deletes it, since
  `tools/playbook/core.py#run_meta_check` reds a pending row stale once a leg enforces its tag.
  Observed by AC1 to AC12 and AC14.
  **Readers:** by name: `tools/playbook/core.py`, whose meta-check cited above reads the row and
  reds it stale once a leg's `enforces` holds `principle.p31` · by value: NO VALUE READERS — the
  row's arming build is only printed, in that stale red, never compared or counted.

## 3. Non-goals (OUT)

- Test's landing verdict: only `test.verdict`'s runner-written record gates a landing; no probe
  verdict feeds `deploy.current`, and seen-red stays Test's record kind (night-pass.md:180-182).
- The tester, the `experiment` shape, the scorer factory's experiment judging, the executor, the
  visual capture adapter and the `record` command: dWitnessedBar's, dBoundRoles', dFairHearing's,
  dWellOiledMachine's and dTotalRecall's; S2 names each stand-in.
- The `probe` outcome on the role templates: dFurnishedOrders' `cl-dClosedLoop-0206`.
- Where placement routes an observation: TOOL-dPlacedRequest-4's `entry.place`, which calls S3 with
  `--cause observation --at item.entry.place`.
- `review.trigger`'s own cause set: the `[[trigger-cause]]` table admits a `program = "review"` row,
  and moving the driver's literal set onto it re-points its readers, the driver's verb and the review
  harness, which is not this clause's.
- Firing a probe point at its boundary: the executor's; `probe.py points` lists them and S3 opens one.
- Publishing an entry-time record: it stays on the typing node with the request until
  dWellOiledMachine publishes the request redacted.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-19` — `tools/loop/request.py#derive_request_content_key`, the key an entry-time trigger and its records are filed under beside the request's local text
- **hands-off** `TOOL-dPlacedRequest-4` — `item.probe.trigger`, which `entry.place` routes an owner's observation to under `probe.observations`, receiving the probe's record back
- **hands-off** `TOOL-dPlacedRequest-3` — `stand-in:{prefix}/loop/probe.py`, the route target of the entry items' `probe` outcome, which the entry rows declare
- **consumes-from** external — dDeclaredLoop, built before this build run: the item rows and `check_program` (TOOL-dDeclaredLoop-12, -50 S3), the route join of `check_transition_tables` (TOOL-dDeclaredLoop-13), the `[[record-version]]` join (TOOL-dDeclaredLoop-24), `loop_witness.py rerun` (TOOL-dDeclaredLoop-17 S4), `review.trigger`'s flag shape (TOOL-dDeclaredLoop-20 S2), `read_tag_policy` (TOOL-dDeclaredLoop-26 S6), the policy-key factory (TOOL-dDeclaredLoop-6 S4)
- **consumes-from** external — the record factory (PLAY-dOrderedCharter-7 S7), its kind list `TYPED_RECORD_KINDS` (PLAY-dOrderedCharter-42 S2), the meta-check that reds a leg with no `enforces` (PLAY-dOrderedCharter-7 S3) and dGroundRules' `policy.py get`
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The items

| Item | Actor | `owner` | Needs | Witness | Routes |
|---|---|---|---|---|---|
| `item.probe.trigger` | `command:probe.trigger` | `dPlacedRequest` | none | the `probe-trigger` record | opened → `item.probe.pin`; not-opened → `stand-in:{prefix}/loop/probe.py` |
| `item.probe.pin` | `command:probe.pin` | `dPlacedRequest` | `item.probe.trigger` | the head, recorded before any run | verification, reproduction → `item.probe.design`; experiment → `item.probe.experiment` |
| `item.probe.design` | `role:gov-tester` | `dWitnessedBar` | `item.probe.pin` | the method's schema check | done → `item.probe.run` |
| `item.probe.experiment` | `role:gov-researcher` | `dBoundRoles` | `item.probe.pin` | the method's schema check | done → `item.probe.run`; beyond-authority → owner item |
| `item.probe.run` | `executor` | `dWellOiledMachine` | `item.probe.design` or `item.probe.experiment` | the `run` lines by hash | done → `item.probe.judge`; unrunnable → `item.probe.return` |
| `item.probe.judge` | `command:probe.judge` | `dPlacedRequest` | `item.probe.run` | the computed verdict | judged → `item.probe.return`; claimed → `item.probe.judge-claimed` |
| `item.probe.judge-claimed` | `role:gov-tester` | `dWitnessedBar` | `item.probe.judge` | the judgment's schema check, held as claimed | done → `item.probe.return` |
| `item.probe.return` | `command:probe.return` | `dTotalRecall` | `item.probe.judge` | the `probe` record | returned → `stand-in:{prefix}/loop/probe.py`; claimed, unrunnable → owner item |

Each command actor is `command:probe.<verb>`, the shape `tools/loop/loop_lib.py#ACTOR_FORM` admits,
as the review program's `command:review.trigger` and `command:review.pin` rows of
`tools/loop/loop.toml` spell theirs (F4). Every target is a declared item or a stand-in path, the two
forms `tools/loop/loop_lib.py#ROUTE_STAND_IN` and `check_program` admit beside `transition`, and
none crosses a step, since every probe item sits at `step = "none"` (F13). "Owner item" is the route
`stand-in:{prefix}/unattended/unattended.sh`, as the review program's `item.review.trigger` row
routes `refused` (`tools/loop/loop.toml@d70457cc:2013`): its `--park` under a mandate and the
owner's own turn when attended, until the owner gate of dDeclaredLoop's breakpoints arms it. A
route to `stand-in:{prefix}/loop/probe.py` is the line `probe.py` prints ending `· to <asker>`: the
asker's next item is the asker itself, re-entered with that line as its input (flow-steps.md:35-36),
since the probe left the asker's own work unfinished.

### The record versions

`item.probe.trigger` declares `returns = "record-kind.probe-trigger"`, and `item.probe.pin`,
`item.probe.run`, `item.probe.judge` and `item.probe.return` declare `returns = "record-kind.probe"`.
`tools/loop/loop_items.py#check_record_versions` refuses an item whose `returns` or input names a
typed kind no `[[record-version]]` row pins, so `tools/loop/loop.toml` gains two rows after the four
it holds (`tools/loop/loop.toml@d70457cc:1121`):

| `kind` | `version` | `fields` |
|---|---|---|
| `record-kind.probe-trigger` | `1` | DERIVED: `tools/loop/loop_items.py#derive_record_hash` over the kind's `required` and `closed` in `build_records.py`'s `KINDS` |
| `record-kind.probe` | `1` | DERIVED, the same way |

The builder copies each `fields` value from the `loop: record-version` line `loop_items.py check`
prints once the kind rows land.

The `[[computed-witness]]` row `probe-rerun` of `tools/loop/loop.toml` switches its `serves` from
`none` to `item.probe.run`, whose witness class is `history`, a class
`tools/loop/loop_lib.py#check_computed_witnesses` admits for a served item.

### The trigger's refusals

| Cause | Refused when |
|---|---|
| `point` | `--at` is not in `probe.points` |
| `owner` | `probe.raise` is `off` |
| `observation` | `--at` is not the position `probe.observations` admits, and at every position under `on-request` |
| `raised` | `probe.raise` is `owner-only` or `off` |
| `reproduction` | never; a patch build's red-first reproduction (`cl-dClosedLoop-0408`) |

### The records

Each record is written as `tools/memory-tree/build_records.py#write_record` writes one: a
`# <unit> <kind> <n> — <title>` head, the `**Serves:**` line, then each field as a `- **Key:** value`
bullet, the shape `build_records.py#FIELD` reads, then the lines after one blank line. The title is
`<cause> from <asker>` for a trigger and `<kind> for <asker>` for a probe. A run line is written bare,
`run · <exit> · <hash> · <command>`, the shape `build_records.py#RUN_LINE` reads.

```
# TOOL-dExample-2 probe-trigger 1 — observation from item.entry.place

**Serves:** probe-trigger TOOL-dExample-2

- **Cause:** observation
- **Asker:** item.entry.place
- **Subject:** the owner reports the card drops its route after a compaction
- **At:** item.entry.place
- **Key:** 3f9c2a71d0e4
```

```
# TOOL-dExample-2 probe 1 — reproduction for item.entry.place

**Serves:** probe TOOL-dExample-2

- **Sha:** 3f9c2a71
- **Kind:** reproduction
- **Question:** does a compaction drop the card's route?
- **Losing:** the replayed card keeps its route section
- **Asker:** item.entry.place
- **Trigger:** 2026-10-25-build-TOOL-dExample-2-probe-trigger-1
- **Verdict:** confirmed
- **Judged:** computed
- **Writer:** stand-in

## Method

- method · 1:9c0e5a1b2f33 · bash replay-case.sh

run · 1 · 9c0e5a1b2f33 · bash replay-case.sh
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/probe.py` | module | none declared for files |
| `trigger`, `pin`, `design`, `run`, `judge`, `return`, `points` | verbs of `probe.py` | none |
| `--probe`, `--cmd`, `--expect`, `--mark` | flags of `design`, as `run`, `loop_witness.py rerun` and `build_records.py` spell them | none declared for flags |
| `--cause`, `--asker`, `--subject`, `--build`, `--unit`, `--request`, `--at` | flags of `trigger`, `--build` and `--unit` as `build_records.py` spells them | none declared for flags |
| `--selftest` | flag of `probe.py`, as `request.py` spells it | none declared for flags |
| `read_trigger_causes`, `check_probe_outcomes` | functions | `py.function`, OK |
| `PROGRAM_SEGMENTS` | constant | none declared |
| `[[trigger-cause]]` | table of `loop.toml` | none |
| the eight `item.probe.*` tags | item tags | graded by `gov_tag.py check` |
| `probe`, `probe-trigger` | record kinds | none |
| `loop probe fixtures` | leg, with `enforces` | none |

### Migration

None: no probe exists before this unit, and the `probe` outcome on existing rows is additive.

### Rollout

Live at landing, placed only: probes open from the owner, `probe.points` and placement's
observations; no role raises one until dBoundRoles lands the outcome on the templates.

The pass regenerates `.governance/policy.json` in its own commit wherever the catalogue moves, the
subject pins through `govkit.py selfcheck --write`, `memory/HYGIENE.md` from its template, and
`memory/map/generated/` through the codebase-map kit's `gen_map.py --write` wherever its diff mints,
renames or deletes a function the symbol extractor reads, so `gen_map.py --check` exits 0 after the
pass; `TOOL-dPlacedRequest-34` S38 is the final re-check only.

### Files touched (estimate)

- `tools/loop/probe.py`
- `tools/loop/loop.toml`
- `tools/loop/loop_lib.py`
- `tools/loop/kit.toml`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `tools/playbook/core-pending.txt`
- `tools/policy/catalogue.toml`
- `.governance/policy.json`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/features/loop.md`
- `help/loop.md`
- `memory/map/generated/`

### Alternatives rejected

- **A second runner in `probe.py`.** TOOL-dDeclaredLoop-17 S4's `rerun` already answers the
  verification vocabulary at a pinned SHA; its §3 hands `probe.run` and `probe.judge` here by name.
- **A probe step.** Testing is not a step (flow-steps.md:607); the rows ride `step = "none"` as the
  breakpoint program's do.
- **A second record kind for an experiment's reference.** The experiment's probe record is the
  measured reference (night-pass.md:180-182).

## 5. Production-readiness checklist

- security — the re-run executes the method's commands in a detached worktree at the pinned SHA
  under a timeout (TOOL-dDeclaredLoop-17 S2); the method is declared by a role or the owner, never by
  the asker's reasoning; an entry-time record stays on its node with the request text.
- perf / scale — one re-run per probe; an experiment never runs before its shape lands.
- error / empty / loading states — a refused cause writes nothing and names the key; an unresolved
  SHA exits 2; a `visual` method entry is `unrunnable`, routed to the owner; `design` on a frozen
  record exits 2 and writes nothing.
- observability — each verb prints one `probe —` line naming the record and the route taken.
- risks — a claimed verdict is held as claimed and goes to the owner, never fed to a gate.
- testing — S10's plants, red and green.
- migration — none.
- user docs — `help/loop.md` gains the probe's section.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --check` runs over the tree, it passes with the eight
  `item.probe.*` rows at `step = "none"`, each carrying the `owner` of §4's table, and the plant
  `probe-step` with an `item.plan.x` row at `step = "none"` exits 1 naming it; and
  `python loop_table.py check`, run in the loop kit's directory, exits 0 and prints no
  `stand-in item.probe.` line.
  Red when: a probe row is refused for its step, the admission widens past the two segments, or a
  `[[stand-in]]` row names a probe item, which the stand-in arm refuses as stale.
- **AC2** — When `python probe.py --fixture --plant trigger-causes` runs `trigger --cause hunch`, it
  exits 2 naming the five causes `read_trigger_causes("probe")` returns, `trigger --cause owner
  --build <slug> --unit TOOL-dExample-2` writes one `probe-trigger` record named
  `<date>-build-TOOL-dExample-2-probe-trigger-1.md`, and the same call without `--unit` exits 2.
  Red when: a cause outside the rows opens a probe, the set is typed in `probe.py`, or a build-folder
  record is written with no unit id.
- **AC3** — When the plants `raise-owner-only`, `raise-off`, `points-unlisted`,
  `observation-at-plan` and `observation-on-request` run their refused cause, each prints
  `probe — not opened` naming its key and ending `· to <asker>`, and `git status --porcelain` prints
  nothing; each value's admitted case opens, and under `on-request` the `--cause owner` case opens.
  Red when: a key's value does not move what opens, or `on-request` admits an observation.
- **AC4** — When the plant `pin` pins a verification, `git log -1 --format=%s` in the fixture reads
  `probe pin(item.entry.place): verification` and that commit holds the record's `Losing` field while
  no `run` line exists yet; an unresolvable `--sha` exits 2. Pinned from the `entry-time` plant's
  trigger, the head lands as `3f9c2a71d0e4.probe.md` in the `requests` store of the fixture's git
  common dir, holding `Losing`, and `git rev-parse HEAD` in the fixture prints the commit it printed before.
  Red when: a command runs before the losing outcome is recorded.
- **AC5** — When the plant `run-judge` pins a reproduction whose method predicts the planted failing
  command's exit and hash, `run` then `judge` then `return` write `Verdict: confirmed`, and the plant
  `run-refuted`, whose prediction differs, writes `refuted`; `return` prints `probe — <verdict> ·
  <record> · to item.entry.place`.
  Red when: the verdict is typed rather than computed from the re-run, or the record does not name its asker.
- **AC6** — When the plant `visual` pins a verification whose method carries a `visual` entry,
  `run` runs no command, writes `Verdict: unrunnable` and `Judged: computed`, and `return` prints the
  owner-item route; the plant `judge-claimed`, whose method carries a `judge claimed` entry, writes
  `Judged: claimed` with no `Verdict` and routes to `item.probe.judge-claimed`; the plant
  `experiment` routes `pin` to `item.probe.experiment`, whose stand-in prints the owner item naming
  dBoundRoles.
  Red when: an unbuilt part runs as if it were built, or a claimed judgment is written as computed.
- **AC7** — When `python build_records.py read` runs over the AC5 fixture's records, both grade
  clean, and a plant `verdict-cross` writing `measured` on a reproduction is refused naming `Verdict`;
  and `python tools/memory-tree/gen_build_index.py --print-bindings` over that fixture repository
  prints an `S` row of kind `probe-trigger` for `<date>-build-TOOL-dExample-2-probe-trigger-1.md`
  and one of kind `probe` for `-probe-1.md`, and no `A` row for either.
  Red when: a verdict outside its kind's set is admitted, or a record serves as `journal` or its kind
  is missing from `TYPED_RECORD_KINDS`, so it reads malformed.
- **AC8** — When the plant `entry-time` runs `trigger --cause observation --request 3f9c2a71d0e4 --at
  item.entry.place`, the record lands at `requests/3f9c2a71d0e4.probe-trigger.md` under the
  fixture's git common dir, no build folder gains a file, a second observation's trigger prints
  `probe — joined` and adds its `Subject` line to that record, and the first trigger again exits 1 as
  already opened.
  Red when: an entry-time probe mints an id or writes into a build folder.
- **AC9** — When `python loop_lib.py --fixture --plant role-no-probe` removes `probe` from one role
  item's outcomes, it exits 1 naming the item, and the plant `probe-self`, giving
  `item.probe.design` the outcome, exits 1 naming that item. Over the tree, every role item with a
  listed outcome set, `item.probe.design`, `item.probe.experiment` and `item.probe.judge-claimed`
  excepted, routes `probe` to the probe tool's stand-in target S8 names; `python loop_table.py check` exits 0
  with no cross-step route refused, and `python termination.py check`, both run in the loop kit's
  directory, exits 0 naming no counted cycle through a probe item.
  Red when: a role item cannot ask for a test, a probe item asks for a probe of itself, or the
  `probe` route crosses a step.
- **AC10** — When `python -c "import tomllib, sys; print(sorted(r['name'] for r in tomllib.load(open(sys.argv[1], 'rb'))['key'] if r['name'].startswith('probe.')))" catalogue.toml`
  runs in the policy kit's directory, it prints `probe.experiment.authority`, `probe.observations`,
  `probe.points` and `probe.raise`, and the same read of the `probe.points` row prints its `allowed`
  `type` as `set` and its `default` as `[]`, both a guard on rows the base already holds. The half the
  unit moves: `python -c "import sys; sys.path.insert(0, sys.argv[1]); import check_policy; k = check_policy.scan_reader_keys(sys.argv[2]); print(sorted(x for x in k if x.startswith(sys.argv[3])))" tools/policy . probe.`, run at the repository root over the built tree, prints a list holding the four keys, where at the
  base it prints `[]`, and `git grep -n "probe.raise" -- probe.py`, run in the loop kit's directory,
  finds a literal-key read.
  Red when: a key is read in a shape the reader-coverage arm does not count, or `probe.points` is not a
  set row, so `read_tag_policy` does not read it as tag-valued.
  fixture: none; the rows are tracked since `c9bd97720`.
- **AC11** — When `grep -n "probe.observations" loop.md` runs in `help/`, it finds the probe section
  naming the two ways in and the four keys.
  Red when: the program lands and the page does not say how a probe opens.
- **AC12** — When `grep -n '"loop probe fixtures"' tools/gate-legs.json` runs, it finds the leg row and
  its argv naming `probe.py` and `--selftest`, and `python -m json.tool tools/gate-legs.json` read for that row shows
  `enforces` holding `principle.p31`.
  Red when: the leg row is absent, names another command, or carries no `enforces`, so the bar never
  runs the cases or the core meta-check reds it.
- **AC13** — When `python loop_lib.py --check` runs in the loop kit's directory after the rows land,
  the lines for `item.probe.design` and `item.probe.judge-claimed` read `role:gov-tester · pending ·
  the roles kit holds no gov-tester role`, the line `item.test.attribute` prints at `6e9c6062`, the
  line for `item.probe.experiment` reads `role:gov-researcher` with no `pending`, since
  `tools/roles/agents/gov-researcher.agent.md` ships the role, and
  `grep -c 'actor = "role:tester"' loop.toml` and `grep -c 'actor = "role:researcher"' loop.toml` each
  print `0`.
  Red when: a probe row spells `role:tester` or `role:researcher`, a slot no build ships, so it stays
  pending once dWitnessedBar's `gov-tester` role lands or for ever.
- **AC14** — When the plant `design` runs `design --probe <record> --cmd "bash replay-case.sh"
  --expect 1:9c0e5a1b2f33` over a pinned record, its `Method` section gains one `- method` line, a
  second call with `--mark visual` appends a second line ending `· visual`, and once `run` has
  written a `run` line a third call exits 2 naming the record, whose bytes stay unchanged.
  Red when: `design` rewrites an entry rather than appending one, or appends to a record a run has
  read.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `kit/dogfood doc parity` · `routed-commits selftest` · `playbook render selftest` · `policy fixtures` · `scratch-guard self-test` · `codebase-map coverage + freshness`

New arm: tools/loop/probe.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC14 · the `loop probe fixtures` leg running `probe.py --selftest` over every case, its failing case staged by `run-refuted` against a predicted `confirmed` · none

New arm: tools/loop/loop_lib.py · covers AC1 AC9 · the `probe-step`, `role-no-probe` and `probe-self` cases under the `loop definition` leg, the failing case staged by `role-no-probe` · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that
  legal?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-25:
  the tuple does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it.
  RESOLVED (agent, 2026-10-25, delegated): `OPEN`.
- **F2 — Where does an entry-time probe's record live, when no build folder exists and the trigger
  "mints no id"?** Options: (a) beside the request's local text, keyed by its content key; (b) on the
  request ref's commit; (c) in a scratch build folder. (b) pushes a subject the request's text is
  withheld from the remote to protect (`cl-dClosedLoop-0137`); (c) mints a build before placement.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the survivor, the home I12 gives the request's
  own text.
- **F3 — The cause set "as data": does `review.trigger`'s literal set move onto the table here?**
  Options: (a) the table with a `program` column, probe's rows only; (b) both programs' rows, the
  driver's verb and the review harness re-pointed. (b) re-points a parent's two readers outside this
  clause. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3; the `program` column is what lets
  review's rows join without a second table.
- **F4 — F-actor: how are the four command items' actors spelled?** Options: (a)
  `command:probe.<verb>`, as the review program's rows spell `command:review.trigger` and
  `command:review.pin`; (b) `command:probe.py <verb>`, which `tools/loop/loop_lib.py#ACTOR_FORM`
  refuses, its name admitting no space. RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the
  loop's one actor grammar stands, and the sibling program is the precedent. widens: none · relaxes:
  none
- **F5 — F-method: where does the method live, in what grammar, and who writes it?** Options: (a) a
  `Method` section of the `probe` record, one entry per line, its marks trailing fields, written by
  `probe.py design` one entry per call; (b) a record of its own, splitting one probe's facts across
  two records. RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the method is part of the record
  the probe pins, so it is written into that record and frozen there. widens: none · relaxes: none
- **F6 — F-judged: where does a claimed judgment go, when `Verdict` is closed?** Options: (a) a
  field `Judged`, `computed` or `claimed`, beside `Verdict`, whose set is unchanged; (b) `claimed`
  as a `Verdict` member. RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the verdict and the
  way it was reached are two facts. widens: none · relaxes: none
- **F7 — F-visual: is visual a `--kind`?** Options: (a) a method entry's `visual` mark, `--kind`
  closed at its three; (b) a fourth `--kind`. RESOLVED (agent, 2026-11-20, delegated): (a), rung 3;
  the capture adapter is a need of one command, so the mark sits on the entry that needs it. widens:
  none · relaxes: none
- **F8 — F-entry: what does `pin` commit for an entry-time trigger, whose record lives outside the
  worktree?** Options: (a) write `<content key>.probe.md` into the git-common-dir `requests/` store
  and commit nothing; (b) copy it into the tree and commit it, publishing what F2 keeps on the node.
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the store is outside the tree, so the head is
  recorded where it lives. widens: none · relaxes: none
- **F9 — When does the method freeze?** The F5 ruling has `design` refuse once the record is
  pinned, yet `item.probe.design` needs `item.probe.pin` and predicts at the pinned SHA, so a
  refusal at the pin leaves `design` nothing to write. Options: (a) keep the item order; `design`
  refuses once the record holds a `run` line, the first point an output could shape a prediction;
  (b) `design` before `pin`, which commits head and method together, departing from the carried
  order and leaving no pinned SHA to predict at; (c) a sealing commit before `run`, a verb no carried
  item declares. Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the
  carried item order stands (design after pin, predicting at the pinned SHA), and refusing once the
  record holds a run line still puts every prediction before any output exists. widens: none ·
  relaxes: none
- **F10 — F-stand-in: where do the unbuilt parts' stand-ins live, when the stand-in table holds row
  items alone?** Options: (a) no `[[stand-in]]` row; each unbuilt part rides its item's own `owner`
  field and a `stand-in:{prefix}/<home>/<file>` route where its work leaves the program, an item
  whose unbuilt part is its actor keeping declared-item routes with its stand-in the `probe.py` verb
  that does the work; (b) the five rows kept, each with a `[[transition]]` row minted so the stand-in
  arm reads it as a row item, a move no level of the tables makes. Recommendation: (a). RESOLVED
  (agent, 2026-11-20, delegated): (a), rung 3; the stand-in table is one row per row item by its own
  grammar, and the probe items are no row items. widens: none · relaxes: none
- **F11 — F-route: where does a role item's `probe` outcome route?** Options: (a) to
  `stand-in:{prefix}/loop/probe.py`, so no route crosses a step and the route join owes no build row;
  (b) to `item.probe.trigger` with an `[[owed-row]]` per role item, a row no unit or build writes.
  Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; a gov-step item routing
  into a program at no step is a cross-step route, and the stand-in target is the form the loop's
  grammar gives a route into a tool. The entry rows of TOOL-dPlacedRequest-3 spell the same target
  `item.probe.trigger` in that unit's own spec, which this pass does not edit. widens: none · relaxes:
  none
- **F12 — F-cycle: do the probe program's own role items carry `probe`?** Options: (a) no; S8 and
  AC9 exclude them by name and `check_probe_outcomes` refuses the outcome on an `item.probe.*` row;
  (b) yes, each route set aside from the counted check by a pending `cycle` row. Recommendation: (a).
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; a probe never asks for a probe of itself, so
  no counted cycle is formed. widens: none · relaxes: none
- **F13 — F-targets: how are the routes to the asker spelled?** Options: (a) `not-opened` and
  `returned` route to `stand-in:{prefix}/loop/probe.py`, the line `probe.py` prints naming the asker,
  re-entered as its own next item; the owner item is spelled `stand-in:{prefix}/unattended/unattended.sh`,
  as the review program's rows spell it, rev-8's spelling lacking the install prefix
  `ROUTE_STAND_IN` requires; (b) a new route word for the asker, which `check_program` would have to
  admit. Recommendation: (a). RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the asker is a
  runtime value no static target can name, and the tool that knows it prints it. widens: none ·
  relaxes: none
- **F14 — F-unit: where does a build-folder record's unit id come from?** Options: (a) `trigger`
  takes `--unit <id>` beside `--build`; (b) `trigger` derives the unit from the build's live spec,
  a guess when more than one is INPROGRESS. Recommendation: (a). RESOLVED (agent, 2026-11-20,
  delegated): (a), rung 3; `write_record` names the record's file by its unit id, and the caller
  that knows the unit says it. widens: none · relaxes: none
- **F15 — F-observation: what admits an observation under `probe.observations=on-request`?**
  Options: (a) nothing; the cause is refused at every position, and the owner opens a probe with
  `--cause owner`; (b) a new request flag on `trigger`. Recommendation: (a). RESOLVED (agent,
  2026-11-20, delegated): (a), rung 3; the owner's own cause already carries the owner's request,
  so no flag is minted. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 7, flow-steps' `[probe]`, P31 and
  v2:1248-1251.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: AC10's grep names the module by its basename,
  run in the loop kit's directory.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.
- rev-4 · 2026-10-26 · §2 S6, S9, S10 · §3 Edges · §4 The records, Inventory, Files touched · §6 AC7,
  AC10, AC12 · §10 · re-grounded on dDeclaredLoop at `783f1ad3a` and dOrderedCharter at `462d20f35`
  by the cross-check record `build/2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md`,
  rows 45, 46 and 48: `probe.points` is a set row defaulting to `[]`; both kinds serve as themselves,
  joined to `TYPED_RECORD_KINDS` and the HYGIENE kind list, with no factory door claimed; the leg
  carries `enforces`.
- rev-5 · 2026-11-19 · §2 S1 · §4 The items · §6 AC13 · §7 · adopts ask TOOL-dPlacedRequest-69 per
  the brief `2026-11-19-prompt-TOOL-dPlacedRequest-1-1-spec-writer`: the item table spells the
  tester's actor `role:gov-tester`, as `tools/loop/loop.toml` and TOOL-dWitnessedBar-23 S7 do; and,
  a discovery adopted by this build run, `item.probe.experiment`'s actor is respelled
  `role:gov-researcher`, the role the tree ships; §7 gains the five legs the spec-token guard join
  names.
- rev-6 · 2026-11-19 · §2 S9 · §4 Files touched · §6 AC10, AC13 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`: finding 5 (M4), AC13 reads the
  `item.probe.experiment` line as `role:gov-researcher` with no `pending` and refuses a row left at
  `role:researcher`; finding 26 (M8), the four `probe.*` rows already exist at `c9bd97720`, so S9
  drops the factory step and edits a row in place only where it differs from v2, and AC10's
  catalogue conjunct reads `scan_reader_keys` over the built tree, which the unit moves.
- rev-7 · 2026-11-19 · §4 Files touched · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.
- rev-8 · 2026-11-20 · §2 S2, S4, S5, S6, S7, S10 · §3 Edges · §4 · §5 · §6 AC4, AC6, AC12, AC14 ·
  §7 · §8 F4 to F9 · folds the brief `2026-11-20-prompt-TOOL-dPlacedRequest-7-divergence-brief`, the
  main loop's rulings on the builder's DIVERGENCE in run `wf_060498d5-d58`, as F4 to F8; citations
  re-grounded; the leg runs `probe.py --selftest`, with registry and budget rows. F9, the freeze
  point on which the F5 ruling and the carried item order disagreed, is resolved by the main loop's
  ruling as (a).
- rev-9 · 2026-11-20 · §2 S2, S3, S6, S8, S9, S10 · §3 Edges · §4 · §6 AC1, AC2, AC3, AC9 · §7 · §8
  F10 to F15 · §10 · folds the brief `2026-11-20-prompt-TOOL-dPlacedRequest-7-divergence-2-brief`,
  the main loop's rulings on the builder's second DIVERGENCE in run `wf_1b6a10b9-c12`, as F10 to F15:
  no stand-in rows, the `probe` route and the asker routes to the probe tool, no `probe` on the
  program's own items, `--unit` on `trigger`, no observation under `on-request`. The records take
  `write_record`'s head and bullet shape, the leg's rows are those `loop request fixtures` holds with
  the generated ceiling file dropped, and the two `[[record-version]]` rows are named.

## 10. Reuse audit

The seams extended are the item rows and their program check (TOOL-dDeclaredLoop-12, -50 S3),
their `owner` field and stand-in routes, the `[[record-version]]` table by two rows
(TOOL-dDeclaredLoop-24), the record writer `build_records.py#write_record`, the re-run primitive `loop_witness.py rerun`
(TOOL-dDeclaredLoop-17 S4), whose §3 names `probe.run` and `probe.judge` as this build's, the
trigger verb's shape (TOOL-dDeclaredLoop-20 S2), `read_tag_policy` (TOOL-dDeclaredLoop-26 S6) for
`probe.points` in `review.breakpoints`' grammar, and the record factory (PLAY-dOrderedCharter-7 S7)
by two kind rows and their `TYPED_RECORD_KINDS` members (PLAY-dOrderedCharter-42).
Scout C's row holds against source: `TESTING` is a phase word with no reader
(`tools/unattended/unattended.sh:852`), and `read_preflight_probes` reads background handles, not
probes. `python tools/codebase-map/reuse_lookup.py "pin a subject by sha, run commands and judge the
verdict against a losing outcome"` ranked name stems (`run`, `run_arms`, `run_git`,
`classify_outcome`), none a pinned re-run, so the parents' specs hold every seam.

Recall terms used: `python tools/memory-recall/query.py "how is a probe triggered pinned run and judged" --terms "probe.trigger probe.pin probe.run probe.judge loop_witness rerun confirmed refuted inconclusive probe.raise probe.points"`
