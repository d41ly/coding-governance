**Serves:** journal TOOL-dBoundRoles-42

# TOOL-dBoundRoles-42 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit on its worktree at base `8f8abe4d0`, with `git grep`,
`git diff`, `python tools/codebase-map/gen_map.py --write` and the dead-path checker's authoring aid
`bash tools/check-dead-paths.sh --list`. No gate, suite or bar ran in the pass; the legs section 7 lists are owed to the
main loop at the close. The departures from the spec's class table are the deviation record of this unit,
`memory/builds/dBoundRoles/build/2026-11-23-build-TOOL-dBoundRoles-42-deviation-423.md`.

## S1 — the classes at the pass's base

The population `git grep -l -F 'agent-cap.js' -- memory ':!memory/builds' ':!memory/ledger'` printed at `8f8abe4d0`
(DERIVED), each file with its class and its disposition at that base:

| File | Class | Disposition |
|---|---|---|
| `memory/DECISIONS.md` | append-only record | historical, unchanged (S2) |
| `memory/archive/DECISIONS.2026-08-10.md` | append-only record | historical, unchanged (S2) |
| `memory/archive/parallel-coding-governance.template-v-2-1.md` | append-only record | historical, unchanged (S2) |
| `memory/archive/parallel-coding-governance.template-v-2-2.md` | append-only record | historical, unchanged (S2) |
| `memory/archive/parallel-coding-governance.template-v-2-3.md` | append-only record | historical, unchanged (S2) |
| `memory/archive/parallel-coding-governance.template-v-2-4.md` | append-only record | historical, unchanged (S2) |
| `memory/archive/parallel-coding-governance.template-v-2-5.md` | append-only record | historical, unchanged (S2) |
| `memory/archive/parallel-coding-governance.template-v-2-6.md` | append-only record | historical, unchanged (S2) |
| `memory/archive/parallel-coding-governance.template-v-2-7.md` | append-only record | historical, unchanged (S2) |
| `memory/backlog/TOOL.md` | append-only record | historical: its rows naming the hook unchanged; the shard is generated, its rows rewritten only by the index generator (S2, AC2 AMENDED) |
| `memory/gotchas/amendment-leaves-its-other-half-standing.md` | gotcha page | `TOOL-dBoundRoles-44`, id 43; its narrative line carried in the dead-path waivers by red-fix `b9a6d5204`, which repointed every other gotcha page at `tools/roles/spawn-guard.js` |
| `memory/project/spec-token-waivers.txt` | registry | unchanged here: the seeded `.claude/hooks/agent-cap.js` row stands, and red-fix `69a052808` replaced the base-line token rows with path rows for `tools/hooks/agent-cap.js` and `tools/hooks/agent-cap.test.sh`, `carried:TOOL-dBoundRoles-25`, which `TOOL-dBoundRoles-43` disposes (id 45) |
| `memory/project/positional-refs.txt` | registry | unchanged: each row is keyed by its citing file, and no citing file changes here; red-fix `69a052808` shrank the rows the re-keyed spec-token rows left |
| `memory/project/dead-path-waivers.txt` | registry | the waiver ledger S5 writes, added to the population by red-fix `b9a6d5204`: the step's and the hooks kit's lines re-disposed `widened:2026-11-23-build-TOOL-dBoundRoles-42-widen-8` here; the gotcha and frozen-fixture rows stay `carried:TOOL-dBoundRoles-25` for `TOOL-dBoundRoles-44` |

No rendered guide, map dossier or generated map file prints at this base: unit 25's S8 disposed the guides and dossiers,
and the generated map no longer names the hook. No file is left without a class, so the S1 stop does not hold.

## Criteria

**Evidences:** TOOL-dBoundRoles-42

- AC1 — `git grep -l -F 'agent-cap.js' -- memory ':!memory/builds' ':!memory/ledger'` — run at base `8f8abe4d0` printed the files of the table above (DERIVED), and each has a class line there. The spec's table population, pinned at `462d20f3`, is not this one: the departures are the deviation record of this unit.
- AC2 — `git diff --quiet <unit 25's parent sha> HEAD -- memory/DECISIONS.md memory/archive memory/backlog` — answered AMENDED, naming `TOOL-dBoundRoles-51` S4, as the spec's hands-off edge states: the literal `git diff --quiet 43808717e HEAD -- memory/DECISIONS.md memory/archive memory/backlog` exits 1, because the generated shard `memory/backlog/TOOL.md` had its `TOOL-dBoundRoles-27` row's caused-by cell rewritten by the index generator. Observed per class: `git diff --quiet 43808717e HEAD -- memory/archive` exited 0; `git diff --numstat 43808717e HEAD -- memory/DECISIONS.md` printed nothing; no line of that diff over those paths names the hook. This pass writes none of them by hand; whatever `gen_build_index.py --write` rewrites in the shard is the generator's.
- AC3 — `git status --porcelain memory/map/generated` — `python tools/codebase-map/gen_map.py --write` ran on the pass's tree before and after its edits, and `git status --porcelain memory/map/generated` printed nothing each time.
- AC4 — `git grep -l -F 'agent-cap.js' -- ':!memory' ':!.governance/steps'` on the built tree printed `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`, `tools/govkit/steps/spawn_guard_pack.py` and `tools/hooks/kit.toml`, each in the admitted set; it holds as written, the registry under the `':!memory'` exclusion as `TOOL-dBoundRoles-50` S14 records.
- AC5 — `bash tools/check-dead-paths.sh --list` on the built tree marked `waived` every line it printed for the retired hook's basenames in `tools/hooks/kit.toml` and `tools/govkit/steps/spawn_guard_pack.py`, each by a row `widened:2026-11-23-build-TOOL-dBoundRoles-42-widen-8`; it printed no such line in `tools/govkit/selftest.py` or under `.governance/steps`, and no row stale or unresolved. The widen door wrote the `surfaces` and `OLD_MARKER` rows with their record; the backticked docstring rows were written by hand under the same stem, as section 8 F3 says. OWED: the dead-path leg's verdict at the close.

## Amended by TOOL-dBoundRoles-51

- The class of `memory/guides/MERGE-BAR.md`, amended by `TOOL-dBoundRoles-51` S5: a live guide edited in place by unit 25 S8 (`00a96bb43`), not a rendered guide, since the tree tracks no template or renderer for it. Only `memory/guides/REVIEW-PROTOCOL.md` is re-rendered, from `tools/workflows/REVIEW-PROTOCOL.template.md`.
