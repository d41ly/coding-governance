# PLAY-dConvergedCharter-14 — every part at its fate: the fates table as rows with path globs, and its join run as convergence's exit check

**Status:** DEFERRED · rev-2 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 22 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0488@7cf98c51 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md](../build/2026-11-03-build-PLAY-dConvergedCharter-5-reuse-scout-d.md) | research | PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-23 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

Today's parts have a fate in a design record, function by function, and nothing derives the shipped-part population
from the tree or checks that a part reached its fate (gap-tool-09; the fates record's `[check]`, "whether each part
reaches its fate is dConvergedCharter's exit check"). This unit materializes the fates table as rows with path
globs, joins it both ways against a population derived from `git ls-files`, reads a declined retirement through its
ratification record, and runs the join as convergence's exit check and as a standing leg, so a new file with no
part and a part off its fate red from here on.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `0d1c1dda`, re-grounded by the build run, which stops this
unit when one is absent: TOOL-dCalibratedLens-5 S8 (`read_keep_records` and the `keep` record in
`tools/loop/loop_review.py`); TOOL-dCalibratedLens-3 (`METRICS`); TOOL-dTotalRecall-10 S1 (`derive_anchor`, the one
heading fold). The rest is live at base: `tracked` (`tools/govkit/govkit.py:344`), `surface_paths` (`:361`),
`resolve_prefix_token` (`:218`), `load_registry` (`:311`), selfcheck arm 8 (`:3415-3453`) and `resolve_landing_base`
(`tools/govkit/upgrade_steps.py:2572`).

- **S1** — The table, `tools/govkit/fates.toml`, gov-internal under the registry's `{prefix}/govkit` exemption
  (`tools/govkit/registry.toml:307-309`), as `tools/govkit/adopters.toml` is. One `[[part]]` row per row of the fates
  record's `[table]` (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-fates.md`), its keys
  `id`, `kit`, `function`, `fate`, `where`, `decided` and `paths`:
  `id = "<kit slug>/<function slug>"`, each slug `derive_anchor` of its cell, so a part of a registry entry is
  spelled as the `[[retired]]` part form `<entry>/<slug>` spells it; `kit`, `function` and `where` the record's
  cells verbatim; `fate` one of `FATES` (§8 F1); `decided` a list, the record's "Decided by" cell split on `;`, to
  which an amendment adds `keep:<key hash>` (S5); `paths` a list of globs read as `surface_paths` reads them
  (`<dir>/*`, `<dir>/**`, a plain path with `*`), `{prefix}` resolved by `resolve_prefix_token` as `load_registry`
  does. A part that lives inside a file other parts share carries `paths = []` (§8 F2). The table also takes the
  four `[[part]]` rows PLAY-dConvergedCharter-15 S1 hands it in `fates.toml`'s grammar (`help/` pages, kit READMEs,
  root `README.md` and the agent runbook, each `kit = "top-level"` and `fate = "RESHAPED"`): the `help/` pages row
  is the record's own `[table]` row with those paths, and the other three are added beside the record's rows.
  Observed by AC1.
  **Readers:** by name: none, since this item mints the table and withdraws no name · by value: NO VALUE READERS,
  nothing this item names is taken out of the tree.
- **S2** — The reader, `read_fate_rows(root)` in `tools/govkit/fates_join.py`: validated rows, refusing (exit 2,
  naming the row) a missing key, a key outside the seven, a fate outside `FATES`, an `id` twice, a glob carrying
  `..` or a leading `/`, and one tracked path matched both by a row whose fate is `RETIRED` or `MERGED` and by a
  row whose fate is `STAYS`, `RESHAPED` or `KEPT`, since no tree satisfies both. Observed by AC1 and AC7.
  **Readers:** by name: none, since this item reads the table and withdraws no name · by value: NO VALUE READERS,
  nothing this item names is taken out of the tree.
- **S3** — The population, `derive_convergence_population(root, rows, at=None)`: `tracked(root, at)`, the paths
  `git ls-files` lists or the tree at `at` holds, under `POPULATION_ROOTS` (`tools`, `skills`, `.githooks`,
  `.claude`, `.github`, `help`, `WIRE-INTO-PROJECT.md` and `coding-governance-agents.template.md`), plus every
  tracked path a row's glob matches outside them, `memory/guides/` and the root's kit confs among them; and
  `read_part_population(root, at=None)`, the parts reading
  `{<id>: {"fate", "where", "paths": [<tracked path>, ...]}}`, the tip's rows over the tree at `at`. Observed by
  AC6.
- **S4** — The join, `check_fates_join(root, base)`, arm 8's shape over this population and table
  (`tools/govkit/govkit.py:3428-3453`):
  1. every population path a row's glob matches, else `fates — <path> · no part's glob matches it`;
  2. every part at its fate: a `RETIRED` or `MERGED` row with a tracked path reds
     `fates — <id> · <fate> · <n> path(s) still tracked · <first>`, and a `STAYS`, `RESHAPED` or `KEPT` row whose
     globs match nothing reds
     `fates — <id> · <fate> · no path tracked`;
  3. the declined arm of S5;
  4. the ratified arm: PLAY-dConvergedCharter-4's `check_ratified_retirements(root, base, "HEAD", parts_at)`, its
     `parts_at` this unit's `read_part_population`, `base` from `resolve_landing_base`;
  and a count line,
  `fates — <n> part(s) · population <p> · <u> unlisted · <f> off fate · <d> declined · <z> carry no path · <r> retired in range`,
  so a part with no path is counted aloud and never read as at its fate unseen.
  It exits 1 on any finding, 2 on a refusal, else 0. Observed by AC2, AC3 and AC5.
  **Readers:** by name: none, since this item grades parts and withdraws no name · by value: NO VALUE READERS,
  nothing this item names is taken out of the tree.
- **S5** — A declined retirement, read through the ratification record. A part whose `(part, id)` a `keep` record
  governs, read through `read_keep_records` (TOOL-dCalibratedLens-5 S8), is declined. Its row must be amended: its
  `fate` no longer `RETIRED` or `MERGED` (to `KEPT`, the clause's `kept`, or a new fate) and its `decided` holding
  `keep:<derive_key_hash("part", <id>)>`, the key the keep's own file name carries; an unamended row reds
  `fates — <id> · declined by <keep path> · row unamended`. A `KEPT` row whose `decided` holds no `keep:` key of its
  own id reds `fates — <id> · KEPT with no ratification record`. A keep that has lapsed for the Loop Review still
  ratifies the amendment it caused. The amendment is an edit of the row, graded here (§8 F4). Observed by AC4.
  **Readers:** by name: none, since this item grades a declined part and withdraws no name · by value: NO VALUE READERS,
  nothing this item names is taken out of the tree.
- **S6** — The parts reading for the Loop Review: one `METRICS` entry `parts` in `tools/loop/loop_review.py`
  (TOOL-dCalibratedLens-3) whose reader runs `python <prefix>/govkit/fates_join.py parts --at <base>` as a bounded
  subprocess (60 s), govkit found through the inline `resolve_kit_dir` block, and hands its JSON to `readings["parts"]`
  for PLAY-dConvergedCharter-4's proposer, its metrics line `parts: <n> parts · <s> superseded · fates_join.py`.
  Where govkit is absent, an adopter's tree, the entry adds no reading and the proposer announces itself unarmed.
  Observed by AC8.
- **S7** — The exit check and the leg. `python fates_join.py check` runs S4; `python fates_join.py check --exit
  [--release <tag>]` runs it and, in the same run and verdict, PLAY-dConvergedCharter-20's adopter exit arm
  `check_adopters_converged(root, release)` (`tools/govkit/adopter_reading.py`, unit 20 S5), which grades every
  row of the adopter register, registered or not, through `derive_migration_state` (unit 5 S1) at `release`, so
  the two read beside each other and never as two populations. `release` is the converged release unit 5 S5
  names, the first `gov/v*` tag whose commit contains this build's landing merge, taken from `--release` when
  given and otherwise derived by that same rule. Where no such tag exists, or the register is empty, the arm
  exits 2 and `check --exit` prints `fates — exit check not graded: <the arm's reason>` and exits 2: a
  not-graded adopter half is never read as green, whatever the join's own verdict. Observed by AC11.
  The leg `fates join`, argv `python {prefix}/govkit/fates_join.py check`, is gov's own as `step-gate` is at base: a
  row in `tools/gate-legs.json`, `chunk` `declarations`, `subject` `repo`, with its `reads`, and an `[[exempt_leg]]`
  row in `tools/govkit/registry.toml` saying why no adopter carries it; where TOOL-dWitnessedBar-28 has moved gov's
  own legs elsewhere by the build run, it is declared there. Observed by AC9.
- **S8** — The plants, `python fates_join.py --fixture --plant <name>`, each a scratch git repository under
  `%TEMP%` with a short name holding a three-row table: `unlisted`, `surviving-guide`, `stays-vanished`,
  `declined-unamended`, `declined-amended`, `kept-unratified`, `retired-unratified`, `overlap` and
  `exit-ungraded`; each is red as
  planted and green with its fix, and `--fixture` with no plant runs them all. Observed by AC2 to AC7.
  **Readers:** by name: none, since this item mints plants and withdraws no name · by value: NO VALUE READERS,
  nothing this item names is taken out of the tree.
- **S9** — The docs: `help/fates.md`, a new page: the table, its row grammar, what the join reds, how a decline
  amends a row, and the leg; its row in `help/README.md`. Observed by AC10.

## 3. Non-goals (OUT)

- Moving any part to its fate: each part's own unit or a ratified proposal does it (PLAY-dConvergedCharter-4).
- Judging whether a row's fate is right, or a `RETIRED` part's replacement: the record's own `[check]` says neither
  check does, and none is added.
- The fates record's own consistency checks, which the design map's instrument runs over the record.
- The adopter exit arm's reading of adopters: PLAY-dConvergedCharter-20's, which this unit runs beside its join.
- A write verb for an amendment: §8 F4.
- Shipping the table or the leg to an adopter: both are gov's (§8 F3).

### Edges

- **consumes-from** `PLAY-dConvergedCharter-4` — the `keep` record of a declined part keyed `(part, id)`, which S5 reads; `check_ratified_retirements`, which S4 runs as its fourth arm; and the parts reading `readings["parts"]` that unit's proposer reads, which S6 supplies
- **consumes-from** `PLAY-dConvergedCharter-23` — `derive_key_hash`, the factory S5 keys a declined part's `keep` record through
- **consumes-from** `PLAY-dConvergedCharter-20` — `check_adopters_converged(root, release)`, that unit's adopter exit arm, which `check --exit` runs beside the join at unit 5 S5's converged release, each register row graded through `derive_migration_state`, its exit 2 read as not graded
- **consumes-from** `PLAY-dConvergedCharter-15` — `fates.toml`, the four `[[part]]` rows of that unit's S1 (`help/` pages, kit READMEs, root `README.md`, the agent runbook), which S1 materializes with the record's `[table]`
- **consumes-from** external — TOOL-dCalibratedLens-3 and -5 (`METRICS`, `read_keep_records`) and TOOL-dTotalRecall-10 (`derive_anchor`), each DEFERRED at base and of a parent or ancestor build

## 4. Design

### Evidence

Selfcheck arm 8 already joins tracked paths against declarations in both directions and reds a stale exemption
(`tools/govkit/govkit.py:3415-3453`), over the registry's surface globs and with entries and exemptions as the
table; this join is that shape over a wider population and the fates rows. The fates record's `[table]` has no path
column (scout D disagreement 3) and its fate set is `STAYS`, `RESHAPED`, `MERGED`, `RETIRED`, while the clause
amends to `kept` (disagreement 4). It holds 138 rows: `STAYS` 22, `RESHAPED` 73, `MERGED` 25, `RETIRED` 18 (PINNED,
parsed at `0d1c1dda`); the record's own text states 139 and `RESHAPED` 74, so the materialization takes the 138
rows the table holds, plus the three `RESHAPED` rows PLAY-dConvergedCharter-15 S1 hands it, and the build pass
says so. The population at base is 490 tracked paths: `tools` 437,
`skills` 7, `.githooks` 11, `.claude` 19, `.github` 1, `help` 13, and the two root files (PINNED, `git ls-files`
at `0d1c1dda`); `memory/guides/` holds 10 and the root holds five `.*.conf` files, each in the population only once
a row names it.

### Data model

```toml
[[part]]
id = "guides/hand-written-guides"
kit = "guides"
function = "hand-written guides"
fate = "RETIRED"
where = "rendered views; rationale moves to `help` fields (dConvergedCharter)"
decided = ["v2 `[chain]` dConvergedCharter"]
paths = ["memory/guides/*.md"]

[[part]]
id = "codebase-map/reuse-lookup-py"
kit = "codebase-map"
function = "`reuse_lookup.py`"
fate = "KEPT"
where = "…"
decided = ["…", "keep:3f2a9c01b4de5a67"]
paths = ["{prefix}/codebase-map/reuse_lookup.py"]
```

`FATES` is `STAYS`, `RESHAPED`, `MERGED`, `RETIRED` and `KEPT`. A glob reads as `surface_paths` reads it, so `<dir>/*`
is the depth-1 entries and `<dir>/**` everything below.

### The join's lines

```
fates — tools/newkit/tool.py · no part's glob matches it
fates — guides/hand-written-guides · RETIRED · 1 path(s) still tracked · memory/guides/BUILD-METHOD.md
fates — skills/deploy-governance · declined by memory/loop-review/2026-12-01-keep-9a8b….md · row unamended
fates — 141 part(s) · population 512 · 0 unlisted · 0 off fate · 1 declined · 41 carry no path · 6 retired in range
```

### Inventory

Names this unit mints, each asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at this
base and answered OK: `read_fate_rows`, `derive_convergence_population`, `read_part_population`,
`check_fates_join`. `FATES` and `POPULATION_ROOTS` are module constants; the `py.constant` cell is undeclared at
this base. File: `tools/govkit/fates_join.py`, verbs `rows`, `population`, `parts`, `check`, `check --exit` and
`--fixture`. Table: `tools/govkit/fates.toml`, row kind `[[part]]`. Leg: `fates join`. Metrics name: `parts`.

### Migration

None for an adopter: the table, its reader and the leg are gov's. For gov, the materialization is one build pass:
each `[table]` row becomes a `[[part]]` row, and each row's `paths` is written by reading what the part is in the
tree at the build commit; the join's first run is the check that the globs cover the population.

### Rollout

Lands at order 22, after every retirement and migration unit of this build, so its first run at the build commit is
the exit reading: a part still off its fate at that commit is a finding the build run disposes, by its own unit, by
a proposal PLAY-dConvergedCharter-4 files, or by a decline that amends its row.

### Files touched (estimate)

- `tools/govkit/fates.toml` (S1)
- `tools/govkit/fates_join.py` (S2 to S5, S7, S8)
- `tools/loop/loop_review.py` (S6)
- `tools/gate-legs.json` (S7, the leg row)
- `tools/govkit/registry.toml` (S7, the `[[exempt_leg]]` row)
- `help/fates.md` (S9)
- `help/README.md` (S9)

### Alternatives rejected

- **A new selfcheck arm in `govkit.py`.** The test: selfcheck grades the registry's declared surface, `tools/*` at
  depth 1, and its population excludes `memory/guides/` and the root confs the clause names; widening arm 8 would
  change what `govkit selfcheck` reds for every kit, while a separate program over its own population changes
  nothing that passes today.
- **The table inline in the fates record, read from its markdown.** The test: the record is frozen design under
  `memory/builds/dClosedLoop/build/`, and an amendment to `KEPT` would have to edit it, which the packet's
  non-goals forbid.
- **A one-time exit check with no leg.** Rejected by §8 F3's test: a file added after convergence would go unlisted
  with nothing to red it.
- **`step_gate.derive_vanished_members` as the at-fate arm.** The test: it diffs two populations
  (`tools/govkit/step_gate.py:219`), which answers "what left in this range", not "is every part where its fate
  says"; a `RETIRED` part that never left would pass it. The range question is the ratified arm's, which reads
  the parts at both ends.

## 5. Production-readiness checklist

- security — the reader refuses a glob with `..` or a leading `/` before any path is built; every git and
  subprocess call is an argv list; the table is gov-internal and never ships.
- perf / scale — one `git ls-files` per side, one compiled matcher per glob over about 500 paths (PINNED at base),
  and one `git log --diff-filter=D` per part retired in the range.
- error / empty / loading states — a missing table is a refusal naming it, never an empty pass; no `keep` record
  tracked reads as no declined part and says `0 declined`; a part with no path is counted on the count line.
- observability — one line per finding and the count line on every run.
- risks — the first run at the build commit may red on parts still off their fate; §4 Rollout names their
  disposal.
- testing — the plants of S8; the `New arm:` line in §7.
- migration — §4.
- user docs — `help/fates.md` (S9).

## 6. Acceptance criteria

Each plant builds a scratch git repository under `%TEMP%` with a short name, runs `fates_join.py` from this tree
against it, and prints its observations; it exits 0 when each matches and 1 otherwise. What the join does not
check: whether a fate is right, whether a part with no path reached its fate, and one part named under two kits.

- **AC1** — When `python fates_join.py rows` runs at the unit's build commit, it prints one line per part and the
  count line `141 part(s) · STAYS 22 · RESHAPED 76 · MERGED 25 · RETIRED 18 · KEPT 0`, the record's 138 rows and
  the three rows PLAY-dConvergedCharter-15 S1 adds, and every (Kit, Function) pair of the record's `[table]` appears
  once.
  Red when: a record row has no part, or a part names a fate outside `FATES`.
  figure: PINNED, the record's table parsed at `0d1c1dda`; a fate an earlier unit of this build amended moves
  it, and the build pass states the delta.
- **AC2** — When `python fates_join.py --fixture --plant unlisted` adds a tracked file under `tools/` that no glob
  matches, `check` prints `fates — <path> · no part's glob matches it` and exits 1; with a row naming it, exit 0.
  Red when: the unlisted file passes.
- **AC3** — When `--plant surviving-guide` keeps a tracked file under `memory/guides/` while its row reads `RETIRED`,
  `check` prints `RETIRED · 1 path(s) still tracked` naming it and exits 1, and exits 0 once the file is removed
  by a commit whose unit's spec carries a clause; `--plant stays-vanished` removes a `STAYS` part's only file and
  `check` prints `no path tracked`.
  Red when: a surviving `memory/guides/` file passes, or a vanished `STAYS` part passes.
- **AC4** — When `--plant declined-unamended` commits a `keep` record for `(part, <id>)` beside a row still reading
  `RETIRED`, `check` prints `declined by <keep path> · row unamended` and exits 1; `--plant declined-amended`
  amends the row to `KEPT` with `decided` holding `keep:<derive_key_hash("part", <id>)>` and exits 0, and to
  `RESHAPED` with the same key exits 0; `--plant kept-unratified` writes `KEPT` with no `keep:` key and prints
  `KEPT with no ratification record`.
  Red when: a declined part passes on an unamended row, or `KEPT` passes with no ratification record.
- **AC5** — When `--plant retired-unratified` deletes a `RETIRED` part's file in a commit whose `Pass:` unit carries
  no clause and no ratified proposal exists, `check` prints PLAY-dConvergedCharter-4's
  `with no ratified proposal` line and the count line reads `1 retired in range`.
  Red when: the fourth arm is not run, or its finding does not set the exit.
- **AC6** — When `python fates_join.py population` runs in the fixture, it lists the tracked paths under each of
  `POPULATION_ROOTS` and a tracked `.memory-tree.conf` a row names, and leaves out an untracked file and a tracked
  path outside the roots no row names.
  Red when: a root is missing, or a row-named path outside the roots is left out.
- **AC7** — When `--plant overlap` writes one path matched by a `RETIRED` row and a `STAYS` row, `check` exits 2
  naming both rows and the path.
  Red when: the contradiction is read as one finding or passes.
- **AC8** — When `python loop_review.py --fixture --plant supersede` runs with a planted govkit holding the
  three-row table, `gather --dry-run` prints `parts: 3 parts · 1 superseded · fates_join.py`, and with the govkit
  directory absent no `parts` line prints and `propose --dry-run` prints `supersede — unarmed · no parts reading`.
  Red when: the entry reads an absent govkit as an empty table.
- **AC9** — When `grep -n '"name": "fates join"' tools/gate-legs.json` and
  `grep -n 'name = "fates join"' tools/govkit/registry.toml` run, each prints one row.
  Red when: the leg lacks its manifest row or its exemption row.
- **AC10** — When `grep -n "keep:" fates.md` and `grep -n "fates.md" README.md` run in `help/`, each prints a line.
  Red when: the page or its index row is missing.
- **AC11** — When `python fates_join.py --fixture --plant exit-ungraded` runs `check --exit` over a fixture whose
  join is green, whose register holds one row and which carries no `gov/v*` tag, it prints `fates — exit check not
  graded` with the adopter arm's reason and exits 2; with `--release <tag>` naming a planted tag and the row
  `migrated`, it exits 0.
  Red when: the exit check reads green while its adopter half was not graded.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `docs` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `step-gate`

The close runs `python tools/govkit/fates_join.py check --exit` once, after the last unit is terminal, as
convergence's exit check; its verdict is the build's, not a criterion of this unit.

New arm: tools/govkit/fates_join.py · covers AC2 AC3 AC4 AC5 AC6 AC7 AC11 · the `--fixture` plants `unlisted`, `surviving-guide`, `stays-vanished`, `declined-unamended`, `declined-amended`, `kept-unratified`, `retired-unratified`, `overlap` and `exit-ungraded`, staged red by a join with each arm removed in turn and by `check --exit` folding the adopter arm's exit 2 into a green, and the new leg `fates join` itself run red over a scratch clone of this tree holding one unlisted file · none

## 8. Open questions

- **F1 — What is the fate vocabulary, given the record's four and the clause's `kept`?** Options: (a) the four
  upper-case fates plus `KEPT`, the clause's `kept` read as it; (b) every fate lower-cased; (c) `kept` beside the
  four as written. (b) rewrites 138 materialized cells for spelling; (c) leaves one set in two cases. Rung 3.
  RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F2 — When is a part at its fate, and what does a part inside a shared file name?** Options: (a) a `RETIRED` or
  `MERGED` row's globs match nothing tracked, a `STAYS`, `RESHAPED` or `KEPT` row's match something, a part living
  inside a file other parts share names no path and is counted aloud, and one path under a must-go and a
  must-stay row is refused; (b) every part names its host file, so a merged function's file reds while its host
  stays; (c) a part at its fate by declaration only. (b) reds parts that did reach their fate; (c) checks nothing.
  Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F3 — A standing leg, or a check run once at the close?** Options: (a) both: the leg `fates join` on gov's bar,
  gov-only as `step-gate` is, and `check --exit` at the close, which adds the adopter arm; (b) only the close's
  run. (b) lets a file added after convergence go unlisted, a gate seen once and never again (`[gate]`). Rung 3.
  RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F4 — How does a decline amend its row?** Options: (a) the row is edited, `fate` and a `keep:<key hash>` entry
  in `decided`, and the join grades the pair against `read_keep_records`; (b) a verb `fates_join.py amend` that
  writes both. (b) adds a write path for an edit the join already grades on every run, and the table is gov's
  own file under review like any other. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the packet's Items 14 (`cl-dClosedLoop-0488@7cf98c51`), the spec
  brief's unit 14 row and I9, I22, I23 and I24, scout D's row for unit 14 and its disagreements 3 and 4, the fates
  record's `[kits]`, `[table]` and `[check]`, the night pass's `[p8-fates]` and the shape audit's
  `declined-retirement` finding.
- rev-2 · 2026-11-04 · S7 S8 §3 AC11 §7 · folded `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1`
  finding 11: the adopter arm is described as unit 20 S5 defines it, `check_adopters_converged(root, release)`
  over every register row through `derive_migration_state`, `check --exit` takes the release from
  `--release` or unit 5 S5's rule, and the arm's exit 2 makes the exit check not graded, the
  `exit-ungraded` plant observing it; the consumes-from edge to PLAY-dConvergedCharter-20 says so.

## 10. Reuse audit

The seam extended: selfcheck arm 8's both-ways join (`tools/govkit/govkit.py:3415-3453`), with `tracked` (`:344`)
for the population, `surface_paths`' glob reading (`:361-384`) and `resolve_prefix_token` (`:218`) as
`load_registry` (`:311`) applies it, reused rather than copied; the declined arm reads TOOL-dCalibratedLens-5's
`read_keep_records` and PLAY-dConvergedCharter-23's `derive_key_hash`; the ratified arm is
PLAY-dConvergedCharter-4's `check_ratified_retirements`. The probe `python tools/codebase-map/reuse_lookup.py
"join every tracked file against declared path globs both directions and red an unlisted file"` ranked `tracked`
(fan-in 40, SEAM) first and nothing that joins against a fate, so no existing seam fits the fates join itself, and
it sits on arm 8's pieces. Where scout D's row and source disagree: it cites `step_gate.read_surface_population`
at `:155` and `derive_vanished_members` at `:219`, both holding at this base, and proposes the vanished-member
diff for the at-fate arm, which §4's alternatives reject. The brief's I22 names `KEPT`; the clause names `kept`;
§8 F1 joins them.

Recall terms used: `python tools/memory-recall/query.py "how does convergence's exit check join the fates table to
the tracked files and read a declined retirement" --terms "fates table join exit check git ls-files path glob
declined retirement kept ratification record convergence"`
