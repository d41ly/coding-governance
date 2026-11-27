**Serves:** journal TOOL-dTotalRecall-22

# TOOL-dTotalRecall-22 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `1ca91e849` from [2026-11-22-prompt-TOOL-dTotalRecall-22-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-22-build-brief.md), recorded whole; the pass tip is `491dfe31c`.

## Why

TOOL-dTotalRecall-22 is built from spec rev-5 with no divergence. The spec's claims about the code checked out against the tree before any write: the 26 declared rows and 1 derived row (DERIVED by `edge_grammar.py --list`), the 10 kind rows that mirror a bounded type (DERIVED by the §4 rule), `resolve_clause_rows`' head rule, `LATER_COLUMNS`, the flags of `leg_factory.py new`, the `practice.one-fact` row and the `--print-relations` line format. Everything is in one pass commit, `Pass: TOOL-dTotalRecall-22`, and the spec header is CLOSED.

## Summary

Built and committed TOOL-dTotalRecall-22 as 491dfe31c on base 1ca91e849. No gate, suite or bar ran. Every acceptance criterion was checked with a probe or the unit's own command-line plants; the gates of §7 and the three `New arm:` red-first observations are owed to the close.

**What was built**
- `tools/playbook/edges.toml`: every declared row now carries a `cardinality` key. `supersedes` allows one per target, `caused-by` one per source, every other type `many` on both ends, and the derived `cites` row has none.
- `tools/playbook/edge_grammar.py`:
  - `read_edge_types` now refuses a declared row without the key, a bad value, or the key on the derived row.
  - New functions `derive_edge_bounds`, `derive_cardinality_cell`, `check_cardinality_mirror`, `read_relation_edges` and `check_edge_cardinality`.
  - New flags `--cardinality` and `--registry`.
  - Four new plants (test fixtures run with `--fixture --plant`): `cardinality-missing`, `cardinality-mirror`, `cardinality-branch` and `cardinality-merge`.
- `tools/memory-tree/design_lib.py`: the shared counter `check_edge_bounds` and its `Violation`. `tools/memory-tree/asbuilt_view.py#resolve_clause_rows` now produces its two-heads finding through that counter.
- `tools/memory-tree/record-kinds.toml`: the 10 mirror cells. `tools/memory-tree/record_kinds.py`: `LATER_COLUMNS` now admits `cardinality`.
- The new leg is an `[[exempt_leg]]` row in `tools/govkit/registry.toml` (`pack = "tags"`, enforcing `practice.one-fact`), rendered into `tools/gate-legs.json`. Its subject-pins row was written by `selfcheck --write`.
- Docs and claims: 6 plant rows in `tools/playbook/adopt-playbook.sh`, the usage row in `tools/govkit/usage.toml`, a new bullet and stamp in `help/tags.md`, the leg claimed in `memory/map/features/playbook.md`, and the kickoff manifest's `last-audit` re-stamped.
- Records: deviation 224 and the acceptance ledger, both under `memory/builds/dTotalRecall/build/`.

**Checks run, and the gate each stands in for**
- **AC1** (`edges` / `playbook render selftest`): a `tomllib` probe found the key on every declared row. `--plant cardinality-missing` exited 2 naming `edge 'part-of' (row 1)`.
- **AC2** (`record-kinds` / the new leg): `--cardinality --registry` exited 0 and reported 10 mirroring kinds, 0 differing. `--plant cardinality-mirror` exited 1 naming deviation, caused-by, "many" and "1".
- **AC3**: a `python -c` probe of `check_edge_bounds` returned one target violation at D with bound ("many", 1) and none with ("many", "many").
- **AC4**: the `unordered-amends` plant printed the same finding before and after the change. With the counter stubbed out it printed `findings 0`.
- **AC5**: the merge plant printed that the merge was clean with 2 parents, then exited 1 naming PLAY-xDec-1 and both records. The branch plant exited 0.
- **AC6**: `--cardinality --registry` at the working tree exited 0 having read 26382 edges of 6 types. This was run before the leg was declared; after that the role hook refused the command as the leg itself.
- **AC7**: a probe of `gate-legs.json` found the row, and `leg_factory --list` named `tools/govkit/registry.toml` as its declaring file.
- **AC8** (`docs`): `docs_leg.py --fingerprints` printed bbbb4ab6, which matches the stamp, and a grep of `help/tags.md` finds `--cardinality --registry`.
- The naming lexicon printed OK for each new name, and `--measure` left `VERB_OFFENDER_PIN` at 1446.

**Owed at the close**
- The §7 gates.
- `New arm: adopt-playbook.sh`: the merge plant staged red by dropping the per-target group.
- `New arm: asbuilt_view.py`: the stubbed counter.
- `New arm: gate-legs.json`: the leg seen red in a scratch worktree holding two `supersedes=` edges to one target, then green at the tip.

**For the main loop to act on**
- The pre-commit `codebase-map coverage` check first failed because the new leg was unclaimed. Fixed by claiming it in `memory/map/features/playbook.md`; the commit then passed its hooks.
- `adopt-playbook.sh --selftest` (ceiling 300) gained about 60 s of plant runs (5 plant runs; DERIVED as the builder's untimed estimate), so its ceiling and budget rows need re-measuring.
- The guard on that leg names only the playbook kit, but the new plants also read memory-tree's `record-kinds.toml` and `gen_build_index.py`. A memory-tree-only edit can leave the leg skipped.
- The `kit epoch` leg may ask for a version bump for the playbook and memory-tree kits, since shipped files in both changed.
- Ask TOOL-dTotalRecall-32 now reads OPEN and its acceptance holds at this commit. The spec names no closes, so it is left for you.
- `derive-ceilings --write` also added 27 runner rows for node d alongside the new leg's 14.3 s observed row (recorded in deviation 224 and a `Decided:` line).
- The first `--dispatch` for the map files timed out at its 120 s bound (DERIVED from the builder's tool timeout) and was skipped, not re-run. Those generated files are committed undeclared.

**Bug-class checklist**
`gotchas.py --for-diff HEAD~1..HEAD` ran and was acted on:
- The fixture cannot pass by finding nothing: the branch plant also asserts that 1 edge was read.
- Each insert keyed on a field that occurs once per row (26 and 10 inserts, matching the row counts).
- The mirror plant mutates the shipped deviation row, not a synthetic value.
- The meta-gates a new leg trips, the stale suite budget, the sibling-kit guard and the adopter migration (an older memory-tree registry would make the mirror plant exit 2) are left to the bar at the close.
