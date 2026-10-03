# TOOL-aWindowedPass-4 — kits declare their generated outputs, and the unattended kit reads them

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-2 · base 886b089d · streams tooling · order 1 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aWindowedPass-4-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aWindowedPass-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aWindowedPass-4-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aWindowedPass-4-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Check 23, `--dispatch`'s condition 3, check 38 and the build-commit pick in two other legs all read
`GENERATED_INDEXES`, a hand-typed `index:generator` list in `.unattended.conf`. This repo's list
names four pairs and misses the codebase map's generated artifacts and the gotcha index, so a
hook-forced regeneration counts as an undeclared write. The example conf adopters copy names two.
This unit moves the declaration to the kits that own the generators, as `[[generated]]` tables in
their `kit.toml`, and gives the unattended kit ONE resolver that every reader calls.

## 2. Scope (IN)

- **S1** — memory-tree's `kit.toml` declares `[[generated]]` rows for `{memory_root}/LIVE.md`,
  `{memory_root}/ledger` and `{memory_root}/backlog` (generator `gen_build_index.py`),
  `{memory_root}/backlog` (generator `backlog.py`) and `{memory_root}/gotchas/INDEX.md` (generator
  `gotchas.py`); codebase-map's declares `{map_root}/generated` (generator `gen_map.py`). Observed by
  AC1.
- **S2** — `resolve_generated_indexes` in `tools/unattended/lib-unattended.sh` reads every
  `<tool root>/*/kit.toml` beside the unattended kit, resolves `{memory_root}`, `{map_root}` and
  `{kit}`, and prints the effective `index:generator` pairs: the declared rows, then the conf's
  `GENERATED_INDEXES` pairs as a project-specific addition. A row whose token does not resolve is
  printed to stderr and skipped. Observed by AC1 and AC2.
- **S3** — check 23, check 38, `--dispatch`'s condition 3 and the conf load in the driver, and the
  `GENERATED_INDEXES` readers in `check-pass-order.sh` and `check-brief-recorded.sh`, read the
  resolver's output instead of the raw conf value. Observed by AC3.
- **S4** — `GENERATED_INDEXES` becomes optional and additive: this repo's `.unattended.conf` and the
  shipped example declare it blank, and the adopter stops stamping it. Observed by AC4.
- **S5** — govkit selfcheck refuses a `[[generated]]` row whose generator is not a file the kit
  ships, or whose path names a token other than `{memory_root}`, `{map_root}` or `{kit}`. Observed by
  AC5.

## 3. Non-goals (OUT)

- No govkit write path changes: the rows are declarations a target reads beside the kit.
- The index-with-its-generator refusal of condition 3 is kept exactly; only its input changes.

### Edges

- **hands-off** `TOOL-aWindowedPass-3` — the commit-time step reads the same resolver.

## 4. Design

### Data model

```toml
[[generated]]
path = "{memory_root}/LIVE.md"
generator = "gen_build_index.py"
why = "rendered from every build's front matter on every spec status move"
```

The resolver parses the three keys with awk, line by line inside a `[[generated]]` table, the same
constrained TOML subset the kit's other readers parse. `{memory_root}` comes from the unattended
conf's `MEMORY_ROOT`, `{map_root}` from `.codebase-map.conf`'s `MAP_ROOT` (default `memory/map`, the
default `map_lib.load_conf` applies), and `{kit}` from the descriptor's directory.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`
- `tools/unattended/adopt-unattended.sh`
- `tools/unattended/.unattended.conf.example`
- `tools/memory-tree/kit.toml`
- `tools/codebase-map/kit.toml`
- `tools/govkit/govkit.py`
- `.unattended.conf`

### Alternatives rejected

- **Stamping a fuller list into the example conf.** Still a hand-typed copy of facts the kits own.
- **A marker inside each generated file.** Partial files (the README's gen regions) already have one;
  a directory of generated JSON has no single place for it, and condition 3 needs the generator path.

## 5. Production-readiness checklist

- security — the resolver reads tracked descriptors; tokens resolve to repo-relative paths only.
- perf / scale — one awk pass over a dozen small files per gate run.
- error / empty / loading states — an unresolvable token is named and the row skipped.
- observability — check 23 prints the effective set it read, with each pair's source.
- risks — a kit not installed contributes nothing, which is correct.
- testing — arms over a fixture tree with declared rows and a conf addition.
- migration — adopters' stamped `GENERATED_INDEXES` stays valid as an addition; duplicates collapse.
- user docs — the protocol's key row and the kit README describe the declaration.

## 6. Acceptance criteria

- **AC1** — When `resolve_generated_indexes` runs in this repo, it prints a pair for
  `memory/map/generated` and one for `memory/gotchas/INDEX.md`.
  Red when: the codebase-map or gotchas row is missing from the descriptors.
- **AC2** — When the fixture conf's `GENERATED_INDEXES` adds a pair, the resolver prints it after the
  declared ones, once.
  Red when: the conf value replaces the declarations instead of adding to them.
- **AC3** — When `bash tools/unattended/check-unattended.sh` grades a fixture pass whose commit wrote
  only a declared generated output, check 23 does not count it.
  Red when: check 23 still reads the raw conf value.
- **AC4** — When `grep -c '^GENERATED_INDEXES=""' .unattended.conf` runs, it prints 1.
  Red when: the hand-typed pairs remain.
- **AC5** — When `python tools/govkit/govkit.py selfcheck` runs with a `[[generated]]` generator
  staged to a missing file, it names the entry.
  Red when: the arm reads no `[[generated]]` table.

## 7. Gates

`unattended kit gate` · `govkit selfcheck` · `govkit selftest` · `brief-recorded` · `pass-order history` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/unattended/check-unattended.test.sh · a pass writing only a declared output · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the owner's part (3) and the readers mapped at base.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "kits declare generated outputs a gate reads"` ranked
name-stem neighbours only and printed `unscanned layers: .sh`; the shell seams were read directly.
Extended: `covers` and `check_generated_render` in the leg, `resolve_generator` in the driver, the
`GENERATED_INDEXES` readers in the two other legs, and govkit selfcheck's descriptor walk. The recall
probe returned TOOL-aRepatriatedFork-55, which added the generated-render skip over the same conf key.

Recall terms used: check 23 undeclared write ceiling dispatch declaration disjointness concurrent pass generated index shrink-only ratchet

The question passed with them: "why does check 23 count undeclared writes against a shrink-only ceiling and how was the dispatch declaration meant to prove disjointness".
