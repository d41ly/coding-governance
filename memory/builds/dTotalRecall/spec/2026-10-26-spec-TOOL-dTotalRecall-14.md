# TOOL-dTotalRecall-14 — the level-0 project map: its renderer and gov map, derived from the one index, held to its budget without losing a node

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 23 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0225@db15491d whole
**Carries:** node:system.project-map
**Carries:** node:policy-key.memory.map-budget
**Carries:** node:policy-key.memory.map-overflow

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-c.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-11 TOOL-dTotalRecall-15 TOOL-dTotalRecall-17 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-13 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-22 TOOL-dTotalRecall-3 TOOL-dTotalRecall-2 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-9 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

Give an agent the whole project at once. The level-0 map is one line per node of every bounded
namespace and one counted line per unbounded one, derived from the one index and cached beside it.
It is held to `memory.map-budget`, and over that budget it degrades in a fixed order or is refused,
as `memory.map-overflow` says, never losing a node (PM-1, PM-2). Today no whole-project view
reaches an agent: 37 of 52 items of one audit, and 30 of 39 in two more, needed a piece not in view
(gap-mem-26). The map is an inventory with no node above one unit (gap-design-01), and it stood at
31,203 of its 32,768 B before the `code` line it must budget (gap-mem-30).

## 2. Scope (IN)

The index, its namespace registry, its resolver and the policy reader are PLAY-dOrderedCharter-19 S2,
S4, S6 and S8 (`<git-common-dir>/gov/index.db`, `tools/playbook/namespaces.toml` read by
`read_namespaces`, `tools/playbook/gov_tag.py`, `read_policy_value`). The edge types are
PLAY-dOrderedCharter-28's `tools/playbook/edges.toml`, and each namespace's `purpose-source` is
PLAY-dOrderedCharter-22 S1's. The catalogue rows are TOOL-dGroundRules-1 S3's. All are DEFERRED at
base `462d20f3`.

- **S1** — Built only on a won replay. The pass opens by reading unit 17's verdict record; on
  `**Verdict:** lose` this unit is not built, as unit 17 §8 F5 routes. Observed by AC1.
- **S2** — The renderer and its CLI, `tools/memory-tree/gov_map.py`, standing in for `gov map` as
  `gov_tag.py` stands in for `gov tag`. `python gov_map.py` prints level 0, and
  `python gov_map.py <ns>[.<seg>]` prints one namespace whole in the same grammar (level 1). It ports
  the design instrument's `line`, `render` and `fit` and its `LINE` and `NSLINE` grammar
  (`2026-10-17-build-PLAY-dClosedLoop-1-map.py:436`, `:448`, `:476`, `:495-496`), reading the index
  instead of design records. Observed by AC2, AC3 and AC5.
- **S3** — The nodes, DERIVED from the index (shared interface I11). A node is a tag `<ns>.<id>`
  that the served tree's rows carry, `<ns>` a namespace `read_namespaces` returns. Its key is the
  native id where the namespace declares one, its tag otherwise. Its purpose is unit 16's `purpose`
  for a record kind, else the namespace row's `purpose-source`, at most 60 characters. A node with
  none renders `—` and is counted `pending`. Its counts are the inbound edges the index holds per
  edge type. Its relations, `layer`, `owner`, `after` and `implements`, come from declared edges
  only, each at most three keys. A required field that is missing renders `?`, and a missing owner
  is counted `unowned`. Observed by AC2 and AC4.
- **S4** — The tiers. Bounded namespaces render one line per node in the registry's row order.
  Unbounded ones render one `nsline` each. The namespace row's new field `map = "line" | "fold"`
  says which, and a row with neither folds past 40 nodes. `read_namespaces` admits the field and
  refuses any other value. The rows this build's chain registers are set from project-map.md:586-591.
  Observed by AC3 and AC8.
- **S5** — The header,
  `map <tree-id> · nodes <n> · lines <n> · folded <ns>,… [· pending <n>] [· unowned <n>] [· unarmed <ns>,…] [· degraded <step>,…]`,
  where a `degraded` step is `purpose-40` or `fold:<ns>`. Observed by AC2.
- **S6** — The budget, `memory.map-budget` (`16k`, `24k` or `32k`, default `32k`, a k being 1,024
  bytes as the instrument's `BUDGET` reads), and `memory.map-overflow` (`degrade` or `refuse`,
  default `degrade`), each read through `read_policy_value` with the key literal first. Under
  `degrade`, purposes are cut to 40 characters, then the lowest-ordered bounded namespaces fold to
  their counted lines one at a time until the map fits, and the header names each step. Under
  `refuse`, a map over the budget exits 1 naming its bytes and the budget, and nothing is cached.
  Either way every node stays on a line or inside a count. Observed by AC2 and AC3.
- **S7** — The cache, `<git-common-dir>/gov/map/<tree>.map` (D6), beside the index and resolved by
  `common_git_dir`. Its first line stamps the two keys' values and `gov_map.py`'s version, and a
  stamp that differs re-renders. A worktree with uncommitted edits is rendered and never cached.
  Observed by AC6.
- **S8** — The `code` line. Unit 8's `code` namespace renders as one counted line at level 0, never a
  line per file, and gov's own map holds it within the default budget. Observed by AC7.
- **S9** — The two keys' catalogue rows gain their `summary` and a `usage` line in
  `tools/policy/catalogue.toml` (`memory.map-budget = "24k"`, `memory.map-overflow = "refuse"`).
  Their names leave `tools/policy/unsummarised-keys.txt` through `policy.py lists --write` in the same
  commit, and the mirror `policy.py mirror --write` regenerates lands in a second commit, as
  PLAY-dOrderedCharter-19 S8 does for its keys. Observed by AC9.
- **S10** — The fixture, `gov_map.py --fixture --plant <case>`, and `--selftest`, which runs every
  plant: a scratch repository with a registered namespace set and a built index. Observed by AC2 to
  AC6 and AC8.
- **S11** — The help page `help/project-map.md`: what the map shows, `gov_map.py`'s two forms and
  the two keys, linked from `help/README.md`. NOT OBSERVED by a criterion: prose, graded by the
  memory hygiene leg's link checks at the close.

## 3. Non-goals (OUT)

- The three-way completeness check and the `map` leg pack: unit 15's.
- The atlas and the map's render-parity arm against it: unit 26's.
- Delivery: the work order's `map` slot, its unfolds and `memory.project-map`, dBoundRoles'; the
  owner session's default load (`memory.default-load`) and the read count, dWellOiledMachine's.
- Purposes for namespaces whose owning builds land later. They render `—` until those builds land,
  and no chain edge is added for them (project-map.md:669-670).
- The codebase map's own `render_map_md` (`tools/codebase-map/map_lib.py`), which stays the
  optional kit's code-depth view.

### Edges

- **consumes-from** `TOOL-dTotalRecall-17` — `map-replay`, whose verdict record must read `win` before this unit is built
- **consumes-from** `TOOL-dTotalRecall-16` — `purpose`, the kind registry's column a record-kind node's purpose is read from
- **hands-off** `TOOL-dTotalRecall-15` — `gov_map.py`, its rendered lines, its header and its `--fixture` plants, which the completeness checks and the `map` leg pack read
- **hands-off** `TOOL-dTotalRecall-26` — `gov_map.py`, its node-table derivation `derive_nodes`, which every atlas page renders from, and the namespace row's `map` field
- **hands-off** `TOOL-dTotalRecall-43` — `gov_map.py`, its policy reads and its cache, which that unit changes and observes for the round-1 audit's ids 11, 15, 33 and 58

## 4. Design

### The line

```text
line   := "- " <key> [" — " <purpose>] [" · " <count> {", " <count>}] [" · " <rel> {" " <rel>}]
nsline := "- " <ns> ".* — " <int> " nodes · gov map " <ns>
```

The grammar is project-map.md:551-562's, verbatim. A line never holds section content, dates,
typed status words, line numbers or provenance. A status the index derives, such as a live build's,
is the only status a line may carry.

### Fitting

```
fit(nodes, budget, overflow):
  out = render(nodes)                       # purposes at 60
  if bytes(out) <= budget: return out
  if overflow == "refuse": exit 1
  out = render(nodes, purpose=40); steps = ["purpose-40"]
  for ns in bounded namespaces, lowest order first:
      if bytes(out) <= budget: break
      out = render(nodes, purpose=40, folded += ns); steps += ["fold:" + ns]
  if bytes(out) > budget: exit 1 naming every step taken
```

A folded namespace's nodes are inside its `nsline` count, so the sum of lines and counts equals the
node count at every step.

### Inventory

Minted: `tools/memory-tree/gov_map.py` with `derive_nodes`, `render_line`, `render_map`, `fit_map`,
`read_map_cache`, `write_map_cache`, `build_map_fixture`; the namespace row field `map`; the cache
directory `<git-common-dir>/gov/map/`; the header fields `pending`, `unowned`, `unarmed`,
`degraded`; `help/project-map.md`. Naming cells: each function asked of the lexicon's `--suggest`
under `--as py.function` at the pass.

### Migration

None. The cache is node-local and starts empty.

### Rollout

Live on landing for a reader that calls `gov_map.py`. Nothing loads the map until dBoundRoles' slot
and dWellOiledMachine's default load land.

### Files touched (estimate)

- `tools/memory-tree/gov_map.py` (new)
- `tools/memory-tree/kit.toml`: a `[[files]]` rule shipping it
- `tools/playbook/tag_index.py`: `read_namespaces` admits `map`
- `tools/playbook/namespaces.toml`: the `map` value on each registered row
- `tools/policy/catalogue.toml`: the two rows' `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: drained by `lists --write`
- `.governance/policy.json`: regenerated, in its own commit
- `memory/map/features/project-map.md` (new dossier for the map's modules)
- `help/project-map.md` (new)
- `help/README.md`

### Alternatives rejected

- **A map in the codebase-map kit.** The owner put it in core memory (PM-2), so it exists where the
  optional kit is absent.
- **Drop the lowest-ranked nodes past the budget.** The clause forbids losing a node; folding keeps
  each inside a count.
- **Cache keyed by the tree alone.** A changed budget would then serve a render made under the old
  one.

## 5. Production-readiness checklist

- security — no new write path but the node-local cache under the git common dir.
- perf / scale — one index read per render; a cached render is one file read.
- error / empty / loading states — an absent index exits 2 naming it; an empty namespace reads
  `unarmed` in the header, never as a green zero.
- observability — the header carries every count and every degrade step.
- risks — a budget too small even fully folded exits 1 naming each step, rather than losing a
  node.
- testing — AC1 to AC9 by a pass; the arms of §7 at the close.
- migration — none.
- user docs — `help/project-map.md` (S11).

## 6. Acceptance criteria

- **AC1** — When the pass begins, `grep -n "^\*\*Verdict:\*\* win" <unit 17's verdict record>`
  prints one line, before any of this unit's code is written.
  Red when: the record reads `lose` or is absent, and the unit is held unbuilt.
- **AC2** — When `python gov_map.py --fixture --plant over-budget` renders a planted namespace set
  over a `16k` budget under `degrade`, the header names `degraded purpose-40` and each `fold:<ns>`
  step, the output is at most 16,384 bytes, and its line count plus its counted nodes equals the
  index's node count.
  Red when: a degrade step is taken and not named, or a node is on no line and in no count.
- **AC3** — When the same plant runs under `memory.map-overflow` `refuse`, it exits 1 naming the
  bytes and the budget, and no cache file is written.
  Red when: an over-budget map is printed under `refuse`.
- **AC4** — When `--plant purposeless` and `--plant ownerless` run, the planted node renders `—`
  and the header counts `pending 1`; the planted ownerless item renders `owner=?` and the header
  counts `unowned 1`.
  Red when: a missing purpose or owner is filled from a default, or not counted.
- **AC5** — When `python gov_map.py <ns>` runs on the fixture for a folded namespace, it prints every
  node of that namespace, one line each, under no budget fold.
  Red when: level 1 is cut or folded.
- **AC6** — When `gov_map.py` runs twice on a clean fixture, the second run reads the cache; when the
  budget key changes between runs, it re-renders; when the worktree has an uncommitted edit, no
  cache file is written.
  Red when: a stale stamp is served, or a dirty render is cached.
- **AC7** — When `python gov_map.py` runs on gov's tree at the pass tip, the header's byte count is
  at most 32,768 and one `- code.*` line is present.
  Red when: the `code` line is a line per file, or gov's map exceeds the default budget unfolded and
  names no step.
  figure: DERIVED at the run; gap-mem-30 pinned 31,203 B at `15cec9200` before the `code` line.
- **AC8** — When `read_namespaces` reads a fixture registry row carrying `map = "table"`, it
  refuses naming the row and the field.
  Red when: an unknown `map` value is read as `auto`.
- **AC9** — When `python policy.py get memory.map-budget --explain` runs at the pass tip, it prints a
  non-empty summary, and `grep -c "memory.map-" unsummarised-keys.txt` run in the policy kit prints 0.
  Red when: either key keeps an empty summary or stays on the shrink-only list.

## 7. Gates

`memory hygiene` · `govkit acceptance matrix` · `playbook render selftest` · `govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

dGroundRules' policy legs, `policy check` and `policy fixtures`, grade the two filled rows; they are
named here rather than on the leg line, because neither exists at this spec's base.

New arm: tools/memory-tree/gov_map.py · covers AC2 AC3 AC4 AC5 AC6 AC8 · `--selftest` runs every plant, staged by `fit_map` skipping the header step for `purpose-40`; unit 15 wires it as a leg of the `map` pack · none

## 8. Open questions

- **F1 — Where does the map cache sit, given the design's path collides with the index file?**
  project-map.md:544 spells `<git-common-dir>/gov/index/<tree>.map`, beside `gov/index.db`.
  Options: (a) `<git-common-dir>/gov/map/<tree>.map`; (b) the design's path. (b) puts a directory
  named `index` next to a file named `index.db`, and the clause says only "cached beside it".
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's words (brief D6). widens: none ·
  relaxes: none
- **F2 — What order do bounded namespaces render and fold in?** Options: (a) the registry's row
  order; (b) a constant in `gov_map.py`. (b) types an order beside the registry it describes.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — What does the header add for the degrade steps?** The design says the header names each step
  and its grammar has no field for one. RESOLVED (agent, 2026-10-26, delegated): a `degraded` field,
  S5, rung 3, the reading under which unit 15's budget check can red a render that omits a step.
  widens: none · relaxes: none
- **F4 — The index, the registry, the edge types, the policy reader and unit 17's verdict are
  unbuilt at base `462d20f3`.** RESOLVED (agent, 2026-10-26, delegated): this spec calls them as
  their specs name them, and the build run re-grounds on the landed code, rung 1. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 14, the brief's I11, I12 and I19, D6,
  scout C's row for cl-0225, and the project map's `[placement]`, `[line]`, `[tiers]` and `[fit]`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are the design instrument's `line`, `render` and `fit`
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py:436`, `:448`, `:476`,
its constants `BUDGET` `:37` and `FOLD_PAST` `:39`), ported rather than imported, since a product
module reads no design record. The node source is PLAY-dOrderedCharter-19's index and
`read_namespaces`, and the CLI's stand-in shape is `gov_tag.py`'s (its §8 F1). `python
tools/codebase-map/reuse_lookup.py "render a byte-budgeted map of nodes degrading in a fixed order"`
ranked `render_map_md` (`tools/codebase-map/map_lib.py`, the code-depth view this unit leaves alone)
and `derive_budget_cut` (`tools/codebase-map/reuse_lookup.py:484`), whose budget cuts a ranked list
and has no fold, so it does not fit a map that must keep every node. Scout C's instrument line numbers
held at `462d20f3`.

Recall terms used: `python tools/memory-recall/query.py "how is the level-0 project map rendered under its byte budget" --terms "project map gov map map-budget map-overflow degrade fold nsline header fit level-0 PM-1 PM-2"`
