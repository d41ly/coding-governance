# TOOL-dLinkedLibrary-2 — the reuse scout's house index, delivered through the task card's `**Reuse:**` field and accepted on aScoutedSeam's benchmark

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 23 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0239@36d4c1c8 whole
**Carries:** node:policy-key.reuse.delivery

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-a.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

No reuse instruction reaches an agent: the task card's `**Reuse:**` field has no producer, and
`reuse_lookup.py` solved 0 of 24 benchmark cases while a scout that first read a generated house
index solved 16 in each of two runs (gap-mem-03,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:186`; the M1c
trial, `memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-7-m1c-trial.md:56-62`).
This unit ships that index in M1c's shape, makes the reuse scout read it and fill the `**Reuse:**`
field of every work order as `reuse.delivery` says, and accepts the result only by re-running
aScoutedSeam's benchmark and its twelve held-out cases at M1c's bar or better (layer-memory `[reuse]`,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:716-744`).

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: the reuse entries
`memory/map/features/<feature>.reuse.toml` and `memory/map/conventions/<name>.reuse.toml`
(TOOL-dLinkedLibrary-1, I1); `origin_rank` and `record_origin.py --of` (TOOL-dLinkedLibrary-9 S6);
the code reader `gov_code.py callers` (TOOL-dLinkedLibrary-14, I17) over the core `code` record
(TOOL-dTotalRecall-8 S7); the scorer factory's `scouted-seam` instance and its `--experiment`
manifest (TOOL-dFairHearing-12 S4, -14 S1); and `read_policy_value` (PLAY-dOrderedCharter-7 §4),
the contract over dGroundRules' `resolve` (`tools/policy/policy.py:752`).

- **S1** — The corpus readers move first. `load_corpus` and `seed_affordances`
  (`tools/codebase-map/reuse_lookup.py:193`, :375), with the private helpers they call, move into
  `tools/codebase-map/map_lib.py`; `gen_map.py` (:36, :194, :199) and `reuse_lookup.py` import them
  from there. `gen_map.py --seed-affordances` prints the same bytes before and after. Observed by AC1.
- **S2** — The house index, `tools/codebase-map/house_index.py`, `render_house_index(root, label)`
  ported from M1c's `render_house_index`
  (`memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-4-bench.py:493-552`), a build
  record never imported. Deterministic, no agent, one markdown document per tree, its sections in §4
  "The index": the steps, shared libraries, canonical copies, symbols with their callers, gate legs,
  bug classes, dossier seams, reuse entries, and the conf-declared listings. A section whose source is
  absent prints `### <section>: absent — <why>`, so an empty index never reads as a house with no
  conventions. The CLI `python house_index.py [--host <tree>]… [--out <path>]`. Observed by AC2 and
  AC3.
- **S3** — The sketch and census steps travel in the index, under `## Steps` at its head: M1c's
  implementation sketch (6 to 15 components a builder would write, each then searched for an existing
  implementation) and its convention census (five or more siblings opened and their shared choices
  tabulated, the majority bound), from the M1c arm's checklist steps 2, 3b and 4
  (`memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m1c-sketch-scout.js:49-54`).
  Observed by AC2.
- **S4** — The ranking and the cap. Symbols rank by `map_lib.fan_in` (:960) at or above
  `seam_fanin_threshold` (:984), as M1c ranked them; dossier seams and reuse entries rank by
  `origin_rank` (one `record_origin.py --of` call), `reconstructed` last, then by fan-in. The whole
  document stays under `HOUSE_INDEX_MAX_BYTES = 34816`, the M1c trial's largest index (33 KB) rounded
  to 34 KiB; past it, each section cuts its lowest-ranked lines first and prints `… <n> more`.
  Observed by AC3.
- **S5** — The reuse scout reads it. `tools/roles/agents/gov-reuse-scout.agent.md`'s body, under its
  1536-byte ceiling (`tools/roles/check_roles.py:88`), says to run `house_index.py` and read its output
  whole before any search, to follow its `## Steps`, and to return a `## Matches` section, one
  `- <seam path or entry tag> — <need> — <how>` line per match or the single word `none`, with the
  index's `**Index:** <sha8>` line; its `returns:` line says so, and the pointer to
  `reuse-lookup.agent.md` leaves the body. `.claude/agents/gov-reuse-scout.md` and the roles index in
  `tools/roles/README.md` re-render from it. Observed by AC4.
- **S6** — The scout's record, I24: `<date>-build-<unit id>-reuse-scout[-<x>].md` under the build's
  `build/` folder, bound `**Serves:** research <ids>`, holding the scout's return. One reader,
  `read_reuse_scouts(root, slug)` in `tools/memory-tree/tree_lib.py`, over `read_bindings` (:471),
  and its CLI `python gen_build_index.py --reuse-scouts <slug>`, printing `<path> TAB <ids> TAB
  <index sha8|->` per record, newest first. Observed by AC5.
- **S7** — The slot, `python house_index.py --slot <slug> <unit> --role <role>`, per §4 "The slot":
  the `task:reuse` block from the newest record S6 finds naming `<unit>`, in one of three states,
  `matched`, `searched` or `not searched`, each rendered distinctly. Under `reuse.delivery` =
  `rendered` it prints the block for every role but `gov-reuse-scout`; under `on-demand` only for a
  role whose `reads` names `task:reuse`, and nothing otherwise. Observed by AC6 and AC7.
- **S8** — The delivery. `render_handoff` (`tools/roles/handoff.py:312`), when it renders a work
  order for a named unit, runs S7 as a subprocess found by `resolve_kit_dir("codebase-map",
  "house_index.py", here)` under `CHECKER_BOUND_S` (:102), and a non-empty answer is the work
  order's `### task:reuse` block; a card `**Reuse:**` value that is not a placeholder follows it as
  `authored: <value>`. No resolver, or a run past the bound, renders `not searched — <why>` under
  `rendered` and nothing under `on-demand`. Observed by AC7.
- **S9** — The key. `reuse.delivery` (`rendered`, the default, or `on-demand`) is read once per slot
  through `read_policy_value("reuse.delivery", root)`; its catalogue row (`tools/policy/catalogue.toml:333-337`,
  owner dLinkedLibrary) gains its `summary` and a `usage` line (`reuse.delivery = "on-demand"`), the
  name leaves `tools/policy/unsummarised-keys.txt` through `python policy.py lists --write`, and
  `.governance/policy.json` is regenerated by `policy.py mirror --write` in a second commit. Observed
  by AC6 and AC8.
- **S10** — The benchmark trees. `python house_index.py --bench <cases> --src-root <dir> --out <dir>
  [--only <ids>]` checks that every repository a case names has a clone at `<src-root>/<repo>` before
  building any tree, and exits 2 naming each missing clone; then builds each case's tree at its `sha`
  by the transient-ref clone `bench.py`'s `build_tree` uses (:109-123), ported, and writes
  `<out>/<short>/house-index.md`. Observed by AC9.
- **S11** — The re-run. `tools/workflows/reuse-bench.js`, gov-only and withheld from installs by a
  `project-owned` row in `tools/workflows/kit.toml`, dispatches one `gov-reuse-scout` agent per case
  over its tree and index, bounded at the agent limit, and writes `results.json` in the
  `scouted-seam` shape (TOOL-dFairHearing-12 S4: a `seams` list per case). The run's manifest and
  results are committed as `<date>-build-TOOL-dLinkedLibrary-2-reuse-bench.json` and
  `-reuse-bench-results.json` and scored by `python replay_scorer.py --experiment <manifest>`
  (TOOL-dFairHearing-14 S1), naming the 30 benchmark cases and the 12 held-out cases. Observed by
  AC10.
- **S12** — The docs: a new page `help/reuse.md` (the index, the scout, the three slot states, the key
  and the benchmark bar) with its line in `help/README.md`, and `tools/codebase-map/README.md` naming
  `house_index.py`. Observed by AC11.

## 3. Non-goals (OUT)

- Retiring `reuse_lookup.py`, its agent file and their readers: TOOL-dLinkedLibrary-3, which reads
  this unit's record as the new reuse evidence.
- The reuse entries and their proposal: TOOL-dLinkedLibrary-1.
- The code record and its callers: dTotalRecall and TOOL-dLinkedLibrary-14; the index reads them.
- The benchmark's cases, held-out set and scorer: aScoutedSeam's records and dFairHearing's factory;
  no case is edited and no new case is written.
- The bench as dBoundRoles' `experiment` entry (TOOL-dBoundRoles-16 S4): a later build declares it.
- TOOL-aScoutedSeam-1 S10 specs the same index as a `gen_map.py --house-index` mode, SPECCED and
  unbuilt; this unit does not build that mode (§8 F1, and the ask there).

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-1` — `reuse.toml`, the reuse entries the index lists under its reuse-entries section; without them the section prints `absent`
- **consumes-from** `TOOL-dLinkedLibrary-9` — `reconstructed`, ranked last by `origin_rank` through `record_origin.py --of`, the order S4 sorts dossier seams and entries by
- **consumes-from** `TOOL-dLinkedLibrary-14` — `gov_code.py`, whose `callers` verb gives each listed symbol's caller files (I17); a tree without it prints the callers section `absent`
- **hands-off** `TOOL-dLinkedLibrary-3` — `house_index.py`, and the scout's record with its one reader `gen_build_index.py --reuse-scouts`, which check 12's §10 arm, `reuse-probed` and M5 read in place of the lookup
- **consumes-from** external — dFairHearing, built before this build run: `replay_scorer.py`'s `scouted-seam` instance and `--experiment` (TOOL-dFairHearing-12 S4, -14 S1)
- **consumes-from** external — dOrderedCharter: `read_policy_value` (PLAY-dOrderedCharter-7 §4)
- **hands-off** external — dBoundRoles: the bench declared as an `experiment` workflow entry once that kind lands
- **hands-off** `TOOL-dLinkedLibrary-42` — `house_index.py`, the codebase-map CLI `MAP_CLI` names from unit 42 on (id 8)
- **hands-off** `TOOL-dLinkedLibrary-52` — `house_index.py`, whose manifest read, conf keys and slot unit 52 re-points and caps (ids 29, 41, 54, 81)

## 4. Design

### Evidence

- `TASK_FIELDS` already holds `reuse` (`tools/roles/handoff.py:97`), and the card label is
  `**Reuse:**` (`skills/session-kickoff/MANIFEST-TEMPLATE.md:59`); no tool writes it (scout A row 2).
- `render_handoff` (`tools/roles/handoff.py:312-424`) renders only the keys a role's `reads` names;
  `gov-spec-writer` reads `task:reuse?` and `gov-builder` does not
  (`tools/roles/agents/*.agent.md:7`).
- `gov-reuse-scout.agent.md:18` points at `reuse-lookup.agent.md`, and its body is 1057 bytes
  against a 1536-byte ceiling (`tools/roles/check_roles.py:88`). M1c's checklist is several KB, so
  its steps cannot sit in the role body (§8 F2).
- `gen_map.py` imports `reuse_lookup` as `rl` (:36) and calls `rl.load_corpus` (:194) and
  `rl.seed_affordances` (:199).
- The held-out file holds 12 cases: five `gov`, four `incms`, three `nicocares`; the benchmark holds
  30, 24 positives and 6 controls (read from both files at base). `bench.py`'s `cmd_trees` builds a
  case tree from `<src_root>/<repo>` (:125-146).
- TOOL-aScoutedSeam-1 S10 specs a `gen_map.py --house-index` mode with `HOUSE_INDEX_DIRS` and
  `HOUSE_INDEX_KINDS` in `.codebase-map.conf`; `git grep -n house_index -- tools/` finds nothing.

### The index

```
# House index — <tree> at <sha8>
**Index:** <sha8>
## Steps                      the sketch, the census, then search every sketched piece (S3)
### Shared libraries          tools/lib, scripts/lib or lib: one line per file, its head comment
### Canonical copies          `# >>> <name>` markers and their install-site counts
### Symbols and callers       fan-in ≥ the seam threshold; up to 3 caller files each (gov_code.py)
### Gate legs                 the names in the manifest `.memory-tree.conf` declares as LEG_MANIFEST
### Bug classes               the stems under <memory root>/gotchas/, with the gotchas CLI's call
### Dossier seams             each dossier's `## Reuse affordance` seams, via map_lib.parse_affordance
### Reuse entries             each entry's tag, needs and anchors, origin-ranked
### <conf listing>            HOUSE_INDEX_DIRS files and HOUSE_INDEX_KINDS captures, as aScoutedSeam S10 names them
```

`--host <tree>` adds a second document for a host tree, as M1c's package cases did.

### The slot

| State | Rendered when | Block |
|---|---|---|
| matched | the newest record naming the unit has a `## Matches` section with lines | `matched — <n> seam(s) · <record path>`, then the lines verbatim |
| searched | the section reads `none` | `searched — no match · <record path>` |
| not searched | no record names the unit; the record has no `## Matches` (the scout failed); or the index is stale: files under the dossier and entry homes or the map's symbols changed since the record's `**Index:**` sha | `not searched — <the reason>` |

### The benchmark bar

M1c's own reading is the bar: 16 of the 24 positives solved by the path matcher on the benchmark,
and 8 of the 12 held-out cases, each read from the `--experiment` output's figure lines. The bench
trees for `incms` and `nicocares` cases need those repositories' clones under `--src-root`; the
clones sit under `%TEMP%`, outside the worktree, as the fixture rule requires.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `house_index.py`, `render_house_index`, `HOUSE_INDEX_MAX_BYTES` | file, function, constant | `py.function`, asked at the pass |
| `--host`, `--out`, `--slot`, `--role`, `--bench`, `--src-root`, `--only` | flags of `house_index.py` | `cli.flag`, asked at the pass |
| `read_reuse_scouts`, `--reuse-scouts` | function in `tree_lib.py`, flag of `gen_build_index.py` | asked at the pass |
| `## Matches`, `**Index:**` | scout return sections | none |
| `reuse-bench.js` | workflow, `tools/workflows/` | none |
| `help/reuse.md` | help page | none |

### Migration

None for records: the scout records already in the tree (scout A to D here) carry no `## Matches`
section, so a slot over them reads `not searched — the record has no Matches section`, which is
true.

### Rollout

The index, slot and delivery land live. The unit closes only on S11's figures at the bar; below
it, the run's departure rule applies (README rule 4) and the unit stays open.

### Files touched (estimate)

- `tools/codebase-map/map_lib.py`, `tools/codebase-map/gen_map.py`, `tools/codebase-map/reuse_lookup.py`: S1
- `tools/codebase-map/house_index.py` (new): S2, S3, S4, S7, S10
- `tools/codebase-map/selftest.py`: the arm the §7 line declares
- `tools/codebase-map/README.md`: S12
- `tools/roles/agents/gov-reuse-scout.agent.md`, its render `.claude/agents/gov-reuse-scout.md`, and the render `tools/roles/README.md`: S5
- `tools/roles/handoff.py`: S8
- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/gen_build_index.py`: S6
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`, `.governance/policy.json`: S9
- `tools/workflows/reuse-bench.js` (new), `tools/workflows/kit.toml`: S11
- `help/reuse.md` (new), `help/README.md`: S12

### Alternatives rejected

- **The steps in the role body.** Over the 1536-byte ceiling several times; raising a ceiling the
  roles kit prices per role moves a guarded constant for one role (§8 F2).
- **The scout writing the card.** The card is per session and the work order per unit; a record is
  durable and one reader derives the slot from it.
- **A ranking list in the work order.** layer-memory:722-723 hands the scout an index, never a
  ranking, and the lookup's ranking solved 0 of 24.

## 5. Production-readiness checklist

- security — the index reads tracked files only and runs `git` with argv lists; the bench clones
  with `--no-local` from local paths into `%TEMP%` and deletes its transient ref; the slot quotes a
  record's lines into a work order as data under its heading, never as instructions to the renderer.
- perf / scale — one corpus load, one `record_origin.py --of` call and at most 45 `gov_code.py
  callers` calls per index; the slot is one `--reuse-scouts` call per work order, bounded.
- error / empty / loading states — `absent — <why>` per section; three slot states; exit 2 naming a
  missing clone.
- observability — the slot names its record; the bench prints parsed counts before figures.
- risks — the bench costs one agent per case (42); the run's agent limit bounds it.
- testing — S1's byte compare, the index plants, the slot states and the delivery, red and green.
- migration — none.
- user docs — `help/reuse.md`, S12.

## 6. Acceptance criteria

- **AC1** — When `python gen_map.py --seed-affordances` runs before and after S1 over this tree, the
  two outputs are byte-identical, and `python -c "import map_lib; map_lib.load_corpus"` resolves in
  `tools/codebase-map`.
  Red when: the move changes the worklist or leaves a copy in `reuse_lookup.py`.
- **AC2** — When `python house_index.py --out <scratch>/hi.md` runs over this tree, the file opens
  with `# House index`, an `**Index:**` line and `## Steps`, and holds each section of §4 or its
  `absent — <why>` line.
  Red when: a section is silently missing.
- **AC3** — When `python house_index.py --fixture --plant ranked` runs over a scratch tree whose two
  dossier seams carry `written` and `reconstructed@<sha8>` origins and whose symbols outgrow
  `HOUSE_INDEX_MAX_BYTES`, the `written` seam lists first, the document stays under the cap, and the
  cut sections end `… <n> more`.
  Red when: a `reconstructed` seam ranks first or the cap is exceeded.
- **AC4** — When `grep -n "house_index.py" gov-reuse-scout.agent.md` and `grep -c
  "reuse-lookup.agent.md" gov-reuse-scout.agent.md` run over the role source, they print a hit and
  `0`, and a `python -c` byte count of its body after the front matter, CR stripped, reads at most
  1536.
  Red when: the body still points at the lookup or exceeds 1536 bytes.
- **AC5** — When `python gen_build_index.py --reuse-scouts dLinkedLibrary` runs, it prints the four
  scout records of this build, each with its served ids and `-` for the index sha.
  Red when: a record is missed or a non-scout record is listed.
- **AC6** — When `python house_index.py --fixture --plant slot` runs its three records (matched,
  `none`, and no `## Matches`) and a stale `**Index:**`, the slot prints `matched — 2 seam(s)`,
  `searched — no match`, `not searched — the record has no Matches section` and `not searched — the
  index was rendered at`; with a planted `.governance/policy.toml` setting `reuse.delivery =
  "on-demand"`, `--role gov-builder` prints nothing and `--role gov-spec-writer` prints the block.
  Red when: two states render alike, or `on-demand` delivers to a role that did not ask.
- **AC7** — When `python handoff.py render --role gov-builder --build tFix --unit TOOL-tFix-1 --stdout`
  runs in the `slot` fixture under `rendered`, the work order holds a `### task:reuse` block with the
  matched lines and the card's authored value as `authored:`.
  Red when: the builder's work order carries no reuse block under `rendered`.
- **AC8** — When `python policy.py get reuse.delivery` runs with no policy file, it prints
  `rendered`, and after `python policy.py lists --write` the unsummarised list no longer names
  `reuse.delivery`.
  Red when: the row is missing or still unsummarised.
- **AC9** — When `python house_index.py --bench <held-out cases> --src-root <dir> --out <dir>` runs
  with no `incms` clone under `<dir>`, it exits 2 naming `<dir>/incms` and builds no tree.
  Red when: the re-run starts, or names no clone.
- **AC10** — When the main loop runs `reuse-bench.js` over the 30 benchmark and 12 held-out cases
  and `python replay_scorer.py --experiment <manifest>` scores the committed results, the figure
  lines read at least 16 of 24 positives solved on the benchmark and at least 8 of 12 on the held-out
  cases.
  Red when: either figure falls below M1c's bar.
  cost: one agent per case, 42, and the trees' clones.
  permission: a Workflow run, the main loop's, at the close.
  fixture: clones of `incms` and `nicocares` under `%TEMP%`; machine-local, not in the tree.
  figure: 16 and 8 are PINNED by the clause; the solved counts are DERIVED by the scorer.
- **AC11** — When `grep -n "on-demand" reuse.md` runs over the help page, it finds the section
  naming both values and the three slot states.
  Red when: the page is absent or omits a state.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `check-wiring self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `policy check` · `policy fixtures` · `memory hygiene` · `memory-hygiene self-test` · `workflow script syntax` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/codebase-map/selftest.py · covers AC1 AC2 AC3 AC6 AC9 · the corpus move, the index sections, the ranking and cap, the slot states and the missing-clone refusal over scratch trees, the failing case a `reconstructed` seam ranked first, staged by dropping the `--of` sort · none

## 8. Open questions

- **F1 — Where does the house index live?** Options: (a) a module `tools/codebase-map/house_index.py`
  with its own CLI (I24); (b) the `gen_map.py --house-index` mode TOOL-aScoutedSeam-1 S10 specs; (c)
  both. (b) puts a second job into the map's generator and its byte gate; (c) is two doors to one
  document. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor; it
  adopts S10's conf keys `HOUSE_INDEX_DIRS` and `HOUSE_INDEX_KINDS` so no adopter setting differs.
  Ask for aScoutedSeam, target build aScoutedSeam: "TOOL-aScoutedSeam-1 S10's house index is
  carried by TOOL-dLinkedLibrary-2's `house_index.py`" · accept S10 re-pointed to call
  `house_index.py`, or retired, before aScoutedSeam builds. widens: none · relaxes: none
- **F2 — Where do M1c's sketch and census steps live?** Options: (a) in the index under `## Steps`;
  (b) in the role body, raising `gov-reuse-scout`'s 1536-byte ceiling; (c) an instruction unit the
  role names (TOOL-dBoundRoles-16 S6's `checklist`), not built before this unit. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3: the clause's "with the sketch and census steps" describes the
  digest, and it moves no guarded ceiling. widens: none · relaxes: none
- **F3 — How does a work order receive the slot?** Options: (a) `render_handoff` runs the slot verb
  and renders its answer as `task:reuse` (S8); (b) the scout writes the session card's `**Reuse:**`
  line; (c) the spec writer copies it. (b) is session-scoped and lost to a fresh session; (c) is a
  typed copy. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, by the tie-break: reuse of
  `render_handoff`'s field render and one derived source. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 2, layer-memory `[reuse]` :716-744, the
  M1c trial and arm, TOOL-dFairHearing-12 and -14, TOOL-aScoutedSeam-1 S10, I24 and scout A's row
  for this unit.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-42, TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended are M1c's `render_house_index` (ported, `…-1-4-bench.py:493`), `map_lib.fan_in`,
`seam_fanin_threshold` and `parse_affordance` (`tools/codebase-map/map_lib.py:960`, :984, :1290),
the corpus readers moved from `reuse_lookup.py:193` and :375, `TASK_FIELDS` and `render_handoff`
(`tools/roles/handoff.py:97`, :312), `read_bindings` (`tools/memory-tree/tree_lib.py:471`), and the
`scouted-seam` scorer (TOOL-dFairHearing-12 S4), each line verified at base. `python
tools/codebase-map/reuse_lookup.py "generate a digest of symbols callers dossiers and reuse entries
for a scout to read first"` ranked name stems (`read`, `read_text`, `digest`, `read_conf`); none
generates a digest, which is gap-mem-03's 0-of-24 failure, so no existing seam fits the index
outside the M1c record and S2 ports it. Scout A cited `gotchas.load_leg_names` for the legs and
`gotchas.records` for the classes; both are memory-tree functions a codebase-map module may not
import, so the index reads `LEG_MANIFEST` and lists the class stems, as M1c did. Scout A cited
`reuse_lookup.py:193` and :375 correctly at base.

Recall terms used: `python tools/memory-recall/query.py "how does the reuse scout get a house index and fill the task card's reuse field" --terms "house index reuse scout M1c sketch census digest Reuse field reuse.delivery benchmark held-out"`
