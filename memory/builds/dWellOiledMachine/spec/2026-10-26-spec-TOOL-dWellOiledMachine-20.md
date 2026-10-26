# TOOL-dWellOiledMachine-20 — the `hook` and `point` tag namespaces, and the point registry they read

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 4 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0298@0b701ed6 whole
**Carries:** node:tag-namespace.hook
**Carries:** node:tag-namespace.point

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-b.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-48 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

The systems record gives dWellOiledMachine two of the core's tag namespaces, `hook` and `point`
(systems `[design-tags]`, "dWellOiledMachine `hook` and `point`"), and no point has a registry
anywhere: layer-runtime `[extend]` names eleven extension points and the tree declares none
(scout B row 7). This unit registers both namespaces in the namespace registry the way
PLAY-dOrderedCharter-19 and -10 register theirs, each with its extractor, and lands the point
registry (I4) that the `point` extractor reads and every later point and adapter registers in.

## 2. Scope (IN)

- **S1** — The `hook` row in `tools/playbook/namespaces.toml`, with PLAY-dOrderedCharter-19 S2's
  fields: `ns = "hook"`, `owner = "dWellOiledMachine"`, `layer = "layer.runtime"`,
  `source` every tracked `*.fragment.json`, `extractor = "tag_index:extract_hook"`,
  `role = "describes"`, `purpose-source = "tools/settings-merge.py#purpose"`, the fragment schema's
  reader and the field TOOL-dWellOiledMachine-22 adds, and `join-armed-by = "dWellOiledMachine"`.
  Observed by AC1.
- **S2** — `extract_hook` in `tools/playbook/tag_index.py`: one member per tracked fragment,
  `hook.<name>` from its `name` field, kind `hook`, the line of that field, and the fragment's
  `purpose` as the member's field where it carries one. The twelve fragments at this base each
  carry a name in the tag segment shape (`git ls-files '*.fragment.json'`, read 2026-10-26).
  A fragment that does not parse as JSON yields no member, since `load_fragment` already refuses it
  at wiring (`tools/settings-merge.py:252`). Observed by AC1.
- **S3** — The `point` row: `ns = "point"`, `owner = "dWellOiledMachine"`,
  `layer = "layer.runtime"`, `source = "tools/runtime/points.toml"`,
  `extractor = "tag_index:extract_point"`, `role = "describes"`,
  `purpose-source = "tools/runtime/points.toml#purpose"`, `join-armed-by = "dWellOiledMachine"`;
  and `extract_point`, one member per `[[point]]` row, its `name` the tag, its `purpose` the
  member's field. Observed by AC2.
- **S4** — The point registry (I4), `tools/runtime/points.toml`. `[[point]]` rows carry `name`
  (`point.<seg>` and further segments), `purpose` and `contract`. `[[adapter]]` rows carry `point`,
  naming a `[[point]]` row; `name`, a tag segment, unique within its point; `tenancy`, one of
  `local`, `project` and `shared`; `retention`, `none`, `forever` or `<days>d`; `region`, `local` or
  a lowercase token; `grant`, whose shape and check are TOOL-dWellOiledMachine-17's; and any further
  field the point's own unit declares and grades, as unit 13's `tick` and unit 14's `table` do.
  `read_points(path=None)` in `tools/runtime/points.py` returns the two row lists, and
  `check_points(points, adapters)` returns a finding for a malformed or duplicate point name, an
  empty `contract`, an adapter naming no point row, a duplicate adapter within a point, and a
  `tenancy`, `retention` or `region` outside its shape. `python points.py check` prints each
  finding and exits 1 on any, 0 on none. Observed by AC3, AC4.
- **S5** — The seed rows. `point.spawn-backends` (TOOL-dWellOiledMachine-1 S9) and
  `point.journal-readers` (TOOL-dWellOiledMachine-16 S7), each with its `purpose` from
  layer-runtime `[extend]`'s "What registers there" column and its `contract` from its unit; and
  one row per `point.*` word a `declares` array of `tools/playbook/layers.toml` holds at the build
  run's base (PLAY-dOrderedCharter-16's stand-in words, "a later build registers a `point`
  namespace and the shape check joins it then"), its `contract` naming the layer row that declares
  it and its `purpose` left to TOOL-dWellOiledMachine-22's review. Each `declares` word is then a
  citation PLAY-dOrderedCharter-19's `resolves` check joins against a row. Observed by AC5.
- **S6** — The citations the registration arms. Registering `point` makes every `point.*` token in
  tracked text a citation the `resolves` check reads. The pass runs `gov_tag.py check` once after
  S5 and writes each unresolved `hook` or `point` citation into this unit's acceptance ledger with
  the unit of this build whose `[[point]]` row resolves it (13, 14, 6, 10, 19, 25, 44, 48, 55, 59),
  and the main loop files one ask in this build's `BACKLOG.md` naming any citation no unit of this
  build resolves. NOT OBSERVED by a criterion: its output is a ledger line and an ask, read at the
  close, when every listed unit has landed its row.

## 3. Non-goals (OUT)

- Each later point's `[[point]]` row and its adapters: the unit that owns the point writes them
  (units 6, 10, 13, 14, 19, 25, 44, 48, 55, 59).
- The `grant` field's shape and its check: TOOL-dWellOiledMachine-17.
- `check_value`'s `registry` arm resolving a registered name: the policy kit reading
  `points.toml` would require the runtime kit, which requires the policy kit; no clause of this
  unit states the arm.
- Hook and point purposes: TOOL-dWellOiledMachine-22, which adds `purpose` to the fragments and
  reviews every member's.
- The agent-cap entry, wired by settings-merge's own block and by no fragment
  (`tools/govkit/entries/settings-merge.kit.toml:22`): it joins the `hook` namespace when unit 10
  makes it a pack.
- How the citation extractor bounds a token: PLAY-dOrderedCharter-19's, which the `kit` namespace's
  `kit.toml` meets as `hook.sh` meets this one; AC6 observes the result.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-1` — `point.spawn-backends`, whose contract S5 writes as a `[[point]]` row
- **consumes-from** `TOOL-dWellOiledMachine-16` — `point.journal-readers`, whose contract S5 writes as a `[[point]]` row
- **hands-off** `TOOL-dWellOiledMachine-22` — `points.toml`, whose `purpose` fields and the fragments' the review fills
- **hands-off** `TOOL-dWellOiledMachine-17` — `points.toml`, whose `[[adapter]]` rows gain `grant` and its check
- **hands-off** `TOOL-dWellOiledMachine-14` — `points.toml`, where `point.harness-adapters` and its adapter rows register
- **hands-off** `TOOL-dWellOiledMachine-13` — `points.toml`, where `point.host-adapters` and its adapter rows register
- **hands-off** `TOOL-dWellOiledMachine-10` — `points.toml`, where `point.hook-packs` registers, and the `hook` namespace its packs are tagged in
- **hands-off** `TOOL-dWellOiledMachine-55` — `points.toml`, where the lease-store, doorbell and offer-source points register
- **hands-off** `TOOL-dWellOiledMachine-44` — `points.toml`, where `point.memory-mirrors` and its stand-in adapter register
- **hands-off** `TOOL-dWellOiledMachine-6` — `points.toml`, where `point.command-adapters` and its adapter rows register
- **consumes-from** external — PLAY-dOrderedCharter-19's `namespaces.toml`, `tag_index.py` and `gov_tag.py check`, and PLAY-dOrderedCharter-16's `layers.toml`; specced and unbuilt at this base

## 4. Design

### Data model

```toml
# tools/playbook/namespaces.toml, beside PLAY-dOrderedCharter-19's and -10's rows
[[namespace]]
ns = "point"
owner = "dWellOiledMachine"
layer = "layer.runtime"
source = "tools/runtime/points.toml"
extractor = "tag_index:extract_point"
role = "describes"
purpose-source = "tools/runtime/points.toml#purpose"
join-armed-by = "dWellOiledMachine"
```

```toml
# tools/runtime/points.toml
[[point]]
name = "point.spawn-backends"
purpose = "a way to start a role agent"
contract = "a backend turns one single-agent act's work order into a launch whose process returns the act's return as structured_output (TOOL-dWellOiledMachine-1 S3)"

[[adapter]]
point = "point.host-adapters"
name = "os-scheduler"
tenancy = "local"
retention = "none"
region = "local"
grant = { service = "local", scopes = [], secret = "anonymous" }   # unit 17's field
```

### Why one registry for points

A point needs a contract, a purpose and its adapters (I4); a `layers.toml` `declares` word is a
name alone. Declaring a point once, in `points.toml`, and reading the layer's word as a citation of
it keeps one fact in one place and lets the existing `resolves` check be the join (§8 F1).

### The hazard measured

`git grep -ohE` over tracked `.md`, `.py`, `.sh`, `.js`, `.toml` and `.json`, 2026-10-26, finds 28
distinct `point.<seg>` tokens: 14 are this build's runtime points; 13 name layer points in other
builds' specs and records, which S5's seed covers where `layers.toml` declares them and S6 lists
where it does not; and one, `point.md`, is a file name, the AC6 hazard again. With
a word boundary before the namespace word only, `hook.` precedes file names (`hook.sh`,
`hook.fragment.json`) about 40 times and `hook.js` 139 times inside names like `procmon-hook.js`.
PINNED at that date; the pass re-derives both counts with the same grep before S6.

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `hook`, `point` | namespace rows | `tools/playbook/namespaces.toml` |
| `extract_hook`, `extract_point` | extractors | `tools/playbook/tag_index.py` |
| `read_points`, `check_points` | functions | `tools/runtime/points.py` |
| `check` | CLI verb | `points.py` |
| `local`, `project`, `shared` | `tenancy` values | `tools/runtime/points.py` |
| `hook-member`, `point-member`, `layer-point`, `hook-filename` | fixture plants | `tools/playbook/gov_tag.py` |
| `runtime points registry` | gate leg | `tools/gate-legs.json` |

### Files touched (estimate)

- `tools/playbook/namespaces.toml` — S1, S3
- `tools/playbook/tag_index.py` — S2, S3
- `tools/playbook/gov_tag.py` — the four fixture plants
- `tools/runtime/points.toml` — S4, S5 (new)
- `tools/runtime/points.py` — S4 (new)
- `tools/runtime/selftest.py` — the arm in §7
- `tools/gate-legs.json` — the `runtime points registry` leg
- `tools/runtime/README.md`, `help/tags.md` — the two namespaces and the registry

### Alternatives rejected

- **The extractor reading both `points.toml` and `layers.toml`.** Two declaring sources for one
  namespace, and a `layers.toml` word has no field for the purpose PLAY-dOrderedCharter-22 S2 grades.
- **Runtime points written into `layer.runtime`'s `declares`.** The array holds names only, so the
  contract and adapters would still need a second home.

## 5. Production-readiness checklist

- security — the registry holds names, shapes and `grant` references, never a secret value; unit
  17 grades the reference.
- perf / scale — two extractors over a dozen fragments and one small TOML file.
- error / empty / loading states — an empty namespace prints `unarmed`, as every namespace does
  (PLAY-dOrderedCharter-10 S4); a malformed registry row is a finding naming it.
- observability — `points.py check` lines; the namespaces' counts in `gov_tag.py check`'s summary.
- risks — citations of points whose rows land later read red until their units land (S6); a
  token-boundary rule that reads `hook.sh` as a citation reds AC6.
- testing — the criteria of §6 and the arms in §7.
- migration — none: a new file and two new rows.
- user docs — `help/tags.md` gains the two namespaces and where a point registers.

## 6. Acceptance criteria

- **AC1** — When `python gov_tag.py --fixture --plant hook-member` runs, a fixture fragment named
  `scratch-guard` yields `hook.scratch-guard`, and `show hook.scratch-guard` returns its row at the
  fragment's path.
  Red when: `extract_hook` yields nothing and the empty namespace reads green.
- **AC2** — When `--plant point-member` runs, `show point.spawn-backends` returns the fixture
  registry's row, and a tracked document citing `point.nowhere` makes `check` exit 1 naming it.
  Red when: the unregistered citation passes.
- **AC3** — When `python points.py check` runs over this tree's `points.toml` it exits 0; over a
  copy whose adapter names `point.nowhere`, and over one holding `point.spawn-backends` twice, it
  exits 1 naming the row each time.
  Red when: either copy exits 0.
- **AC4** — When `points.py check` runs over copies whose adapter carries `tenancy = "global"`,
  `retention = "30"` or `region = "EU West"`, each exits 1 naming the field.
  Red when: any of the three exits 0.
- **AC5** — When `--plant layer-point` runs, a fixture `layers.toml` declaring
  `point.memory.record-home` makes `check` exit 1 naming it while the registry lacks its row, and
  exit 0 once the row is added.
  Red when: the declared word with no row passes.
- **AC6** — When `--plant hook-filename` runs, a tracked document naming `procmon-hook.js` and
  `hook.sh` in prose and in backticks adds no unresolved citation in the `hook` namespace.
  Red when: a file name is read as a `hook` citation.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

The broad guard `{prefix}/` leaves the line by the checker's floor; the bar at the close runs it.

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC5 AC6 · the playbook-render selftest runs `gov_tag.py --fixture` under the four new plants · none
New arm: tools/runtime/selftest.py · covers AC3 AC4 · registry copies with a dangling adapter, a duplicate point and each malformed adapter field · none
New arm: tools/runtime/points.py check · covers AC3 · the `runtime points registry` leg over the tree's own registry, staged by a dangling adapter row · none

## 8. Open questions

- **F1 — Where is a point declared?** (a) In `tools/runtime/points.toml` alone, a `layers.toml`
  `declares` word seeded as a row and read as a citation of it; (b) the `point` extractor reading
  both files; (c) runtime points added to `layer.runtime`'s `declares`. (b) gives one namespace two
  declaring sources and leaves layer points with no purpose field, which PLAY-dOrderedCharter-22 S2
  reds; (c) still needs a second home for contracts and adapters. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the most capable option: one declaration per point, its contract,
  purpose and adapters together, and the existing `resolves` check joining the layer words.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended: PLAY-dOrderedCharter-19's registry, extractor table and `check` verb, and its
fixture's plant list as PLAY-dOrderedCharter-10 S8 extends it; the fragment reader's field set
(`tools/settings-merge.py:252`, `load_fragment`); layer-runtime `[extend]`'s table for the seed
rows' purposes. `python tools/codebase-map/reuse_lookup.py "register a tag namespace and extract its
members from fragment files"` ranked `extract` (`tools/lexicon/lexicon.py`), `extract_row`,
`extract_run_facts` and other `extract`-stem names: none reads fragments or tags, and no point
registry exists in source or in any spec (scout B: `grep "points.toml\|[[point]]"` over every spec
returned nothing), so no existing seam fits the registry itself. Where scout and source differ:
scout B's I4 leaves the adapter fields' shapes open; S4 fixes them, and units 13 and 14 already
write `tenancy`, `retention` and `region` "as I4 spells them".

Recall terms used: `python tools/memory-recall/query.py "how is a tag namespace registered with its extractor" --terms "tag namespace registry namespaces.toml extractor hook point fragment name gov_tag citation shape check"`
