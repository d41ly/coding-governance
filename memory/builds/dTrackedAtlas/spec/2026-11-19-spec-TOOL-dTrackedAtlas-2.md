# TOOL-dTrackedAtlas-2 — the Atlas renders the actual state of each chain build and each area

**Status:** CLOSED · rev-2 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · records-only · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-brief.md) | research | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-1-pin-fold.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-1-pin-fold.md) | research | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-2-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-2-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-2-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-2-spec-brief.md) | research | — |
| [2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-1-2-3-4-diff-review-round1.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 |
| [2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 TOOL-dTrackedAtlas-11 |

<!-- /gen:spec-records -->

## 1. Goal

The Closed Loop Atlas renders the chain's actual state from `TOOL-dTrackedAtlas-1`'s derivation: a
view per chain build, and per comparison area the landed builds that moved it since the measured
baseline. Each build's clauses are shown as built rather than as v2 planned them. The 2026-10-14
measurements stay on the page, labelled as the baseline and never as today.

## 2. Scope (IN)

- **S1** — A new function `derive_actual(data, ref, claims, plant)` in the generator
  `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`. It adds
  `TOOL-dTrackedAtlas-1`'s state document to the page data whole, as `state`. It refuses a document
  whose builds differ from the generator's own `[chain]` parse. Observed by AC1, AC6 and AC8.
- **S2** — Each comparison area gains `landed`, the landed builds owning one of its gaps, and
  `measured`, the dates of the records its baseline sections come from. The page data gains
  `baseline`. Observed by AC2.
- **S3** — The as-built view is read through `tools/memory-tree/design_lib.py#read_design_view` into
  `asBuilt`, one clause list per chain build. A build the view lacks, or a build the chain lacks, is a
  refusal. Observed by AC3 and AC6.
- **S4** — `main` takes `--ref <rev>` (default `HEAD`) and `--claims cache|none` (default `cache`),
  and the module docstring states both. Observed by AC1 and AC10.
- **S5** — Two new plant cases, `state-dropped` and `asbuilt-dropped`, each stopping the run with its
  refusal. The seven existing cases and every existing refusal stay as they are. Observed by AC6 and
  AC7.
- **S6** — `derive()` keeps its signature and its result, so the design map, the fold-state probe
  and stage 0 read what they read today. Observed by AC9.
- **S7** — The template's Chain view states where each build stands, its diagram marks each node's
  state, and the build inspector shows the runs, units, forks, revisions, deviation records, claim
  and the clauses as built. Observed by AC11 and AC12.
- **S8** — The template's comparison view labels every measured section as the baseline, with its
  dates, and shows the landed builds that moved each area since. Observed by AC4 and AC12.
- **S9** — The template carries its own doctype, charset, viewport and a zero body margin. Observed
  by AC5.

## 3. Non-goals (OUT)

- Deriving any build's state. The state document is `TOOL-dTrackedAtlas-1`'s, read through its
  interface and never re-derived here.
- The page's generation commit, its input digest, the header line `#derived`, the `footer` function
  and a `--check` given a page. Those are `TOOL-dTrackedAtlas-3`'s. In the generator this unit
  changes only the module docstring, `plant_memory`'s unknown-case refusal, and in `main` the one
  line that calls `derive`, plus the reads of `--ref` and `--claims` ahead of it. It adds
  `STATE_PATH`, `ACTUAL_PLANTS` and `derive_actual`. It leaves `corpus`, `derive`, `split_sections`,
  the `--check` summary line and the `--out` splice as they are. In the template it changes only the
  places §4 "The template" lists.
- Regenerating the page after a landing, and any wall bound on the run that does it.
- A per-clause landed status. The derivation answers per build, and research-final-atlas's
  484-unit join waits on the index's node table, which does not exist.
- The resolved forks' picks as text. The page shows each unit's revision and its open forks.
- The Memory view's `Today` columns, which quote the memory plan's own column name, and the tab
  label "Today vs target", which names a view that now shows the baseline and the landings beside
  each other.
- Editing the atlas instruments record, v2, the as-built view, its renderers, or any other
  dClosedLoop instrument. This unit's reds are recorded in its own ledger.
- Committing or publishing the page. It is written to a scratch path outside every git tree.

### Edges

- **consumes-from** `TOOL-dTrackedAtlas-1` — the state document of its `derive`, and its two
  exceptions. Without it the page has no `state` and `derive_actual` cannot load.
- **hands-off** `TOOL-dTrackedAtlas-3` — the page's stamp and the page check. That unit reads this
  unit's `--ref` value, and the state document's `commit` is the commit the chain state was read at.
- **hands-off** `TOOL-dTrackedAtlas-4` — running the generator after a landing, with its defaults,
  and bounding that run.

## 4. Design

### Where the actual state enters

Today `derive` reads only dClosedLoop's records from the working tree and returns the page data
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#derive`). Two other
instruments call it with no argument and read its result, and a third reaches it: the design map
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py#derive`), the fold-state
probe (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-fold-state.py@a98cfe0163195eeb70b296c167ec82de8672294d:20`)
and, through the map, stage 0. So `derive` is left alone, and `main` calls a new function on its
result:

```python
data = derive_actual(derive(plant), ref, claims == "cache", plant)
```

`derive_actual(data, ref="HEAD", claims=True, plant=None)` returns `data` with the keys below added.
It loads its two readers inside the function, so importing the generator loads neither:

- `TOOL-dTrackedAtlas-1`'s module by path, as its §4 "Interface" states, from
  `REPO / "memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py"`,
  held in a new constant `STATE_PATH`. It calls `derive(ref, root=str(REPO), claims=claims,
  detail=True)`.
- `design_lib` from `REPO / "tools/memory-tree"`. Its `read_design_conf` and `read_design_keys` give
  `DESIGN_VIEW` and `DESIGN_BASELINE` from `.memory-tree.conf`, and `read_design_view` reads the view.

The reads differ in where they look, and the spec says so rather than hiding it. dClosedLoop's
records and the as-built view are read from the working tree, as the generator reads everything
today. The chain state is read at `--ref` through git. `TOOL-dTrackedAtlas-3` owns any check that
the two agree.

### Data added

| Key | Value |
|---|---|
| `state` | the state document, whole, as `TOOL-dTrackedAtlas-1`'s §4 "Data model" defines it |
| `baseline` | `{"measured": [first date, last date], "design": DESIGN_BASELINE, "view": DESIGN_VIEW}` |
| `asBuilt` | `{build: [{"clause", "text", "since"}]}`, every row of the view in view order, `since` as `read_design_view` returns it |
| `areas[i].landed` | the slugs of `state.landed` owning at least one gap of `areas[i].gaps`, in `[chain]` row order |
| `areas[i].measured` | the sorted distinct record dates of `areas[i].today`'s sections |

A gap's owner is the `owner` field `derive` already gives each gap. A record's date is the `date`
field `corpus` already gives it, the first ten characters of its file name. `baseline.measured` is
the first and last date over every area's `measured`. Measured at `9e21ac760` on 2026-11-19 with a
scratch probe of `derive` (PINNED), it is 2026-10-14 to 2026-10-16. The `flow` and `gap-register`
sections are dated 2026-10-14, and the layer records' `current` sections 2026-10-15 and 2026-10-16.

A landing follows the measurement for every chain build, because the chain was planned from it, so
"landed" and "landed since the baseline" are one set. That holds by history and is not checked.

### Refusals

Each refusal exits through `sys.exit` with one `atlas:` line, as every refusal of the generator does.

- `TOOL-dTrackedAtlas-1`'s `ChainError` or `StateError` exits `atlas: chain state: <message>`.
- The state document's build slugs, in order, must equal `[c["build"] for c in data["chain"]]`.
  Otherwise it exits `atlas: the chain state lacks <slugs> and holds <slugs> the chain does not`,
  naming `none` for an empty side. The two lists come from two parsers of v2's `[chain]`, the
  generator's and `read_chain`, read from the working tree and at the ref.
- `design_lib.DesignRefusal` exits `atlas: as-built view: <message>`. Blank design keys exit
  `atlas: the design keys are blank, so there is no as-built view to read`.
- The set of builds in the view's rows must equal the chain's builds. Otherwise it exits
  `atlas: the as-built view lacks <slugs> and holds <slugs> the chain does not`.

### Plants

A new tuple `ACTUAL_PLANTS = ("state-dropped", "asbuilt-dropped")`. `plant_memory`'s unknown-case
refusal admits it and lists it beside `MEMORY_PLANTS` and `CORPUS_PLANTS`. Both damage data in memory
inside `derive_actual`, before the refusals run. The anchor of each is the last slug of
`state.landed`, `dDeclaredLoop` at `9e21ac760`. With `state.landed` empty, each exits
`atlas: plant <case>: its anchor is gone`, as `plant_memory`'s anchors do.

- `state-dropped` removes the anchor's entry from `state.builds` and its slug from `state.landed`.
- `asbuilt-dropped` removes the anchor's rows from the rows `read_design_view` returned.

### The template

`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html` changes in these
places. Every string from `state` or `asBuilt` is rendered through the template's `esc` or `md`, as
every record string is today.

| Where | Change |
|---|---|
| the head | `<!doctype html>`, `<meta charset="utf-8">` and `<meta name="viewport" content="width=device-width, initial-scale=1">` as the first three lines, ahead of `<title>`; the `body` rule gains `margin: 0` |
| the style block | rules for the run-state classes below; the existing `.state-pill` classes `done`, `open` and `todo` are reused for the pills |
| `views.chain` | ahead of the diagram, chips counting landed, startable and running-or-held builds, a lede naming `state.commit`'s first nine characters and `state.subject`, and a table of one row per build |
| `chainDiagram` | each node carries `run-<build_run.state>` and `next-<next.state>` classes, and its stage line reads `<stage> · <state label>` |
| `showBuild` | the blocks listed below, the clause list taking the place of "Planned units" |
| `views.compare` | the lede and labels below, and a "Landed since" column of build chips |
| `renderArea` | the measured side's label below, and a "Since the baseline" panel |
| `showArea` | the "Baseline, measured in" block and a "Landed since" block |

The Chain view's table columns are Build, Spec run, Build run, Landing, Units, Open forks,
Deviations, Claim and Next. Each cell reads its own field of the build entry. Landing shows the
sha's first nine characters and the subject. Units shows the count and the counts by status. Next
shows `next.state` with `next.waiting_on` beside it.

The state labels are `landed`, `landed, carrying <n>`, `not landed`, and for `next.state` `can
start`, `running`, `held`, `stale claim`, `waiting` and, for `done`, nothing beyond the build run's
label.

The build inspector, `showBuild`, keeps Parents, Children and the gaps owned, and adds:

- "Where it stands": spec run, build run, landing, next state, waiting on, and the claim's status,
  node, beat and staleness;
- "Runs": each run record with its kind, its phase and its landings;
- "Units": the count and the counts by status, then "Carried forward" with each carried unit, its
  verb and its ask;
- "Open forks": the unit ids in `forked`, or `none`;
- "Revisions": a table of unit id and header revision;
- "Deviation records": a table of id, hand, risk and cause;
- "Clauses as built": `<n> clauses · <m> changed since the design baseline <DESIGN_BASELINE's first
  nine characters>`, then each row of `asBuilt[build]` with its clause id, and on a changed row the
  record id that changed it.

The comparison view's measured side is relabelled. The four labels that present a measurement as
today, `Today: an implicit loop`, `Today, measured in` (twice) and `Today, as measured`, become `The
baseline: an implicit loop`, `Baseline, measured in` and `Baseline, measured <dates>`. The lede
states that the measured sections are the baseline of `baseline.measured`, and that the "Landed
since" column names the chain builds that have landed against each area since. "Since the baseline"
lists each build of `areas[i].landed` with its landing and the gaps of this area it owns. With none,
it says that no build owning this area's gaps has landed.

### What it does not check

That a landed build closed every gap it owns; that the working tree and `--ref` describe one commit;
that the as-built view is current with its deviation records, which is `asbuilt.py --check` and
`gen_build_index.py --check`; and any wall bound, because a library caller of the derivation arms
no timer. With `--claims cache`, a claim's `stale` field can flip between two renders at one ref as
time passes, so byte-identical output is a property of `--claims none` only. Stage 0's re-run of
the generator's `--check` now reads the chain state at `HEAD` too.

### Files touched (estimate)

`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md`

The page itself is written under the run's scratch directory and is never in the repository. AC12's
temporary launch configuration, in the worktree's `.claude` folder, is deleted after it and never
staged.

### Alternatives rejected

Reading the chain state inside `derive`: the design map, the fold-state probe and stage 0 would each
inherit a git read at `HEAD`, the claim cache and the fork grading, none of which they render.

Carrying only the changed clauses and substituting them into v2's "Planned units" cell in the
browser: that needs a second parser of the cell beside
`tools/memory-tree/design_lib.py#parse_chain_cell`. The whole view costs 248,110 B (PINNED, measured on 2026-11-19), about 1.5 % of the 16,856,190 B page.

Adding the as-built view to `corpus`: the page would carry it as a record, and the Records view
would show it beside v2 with no join to the builds. Its skip by name in `corpus` stays.

## 5. Acceptance criteria

The commands run from a worktree root, with these names set. `SCRATCH` is the run's scratch
directory, outside the repository.

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
ATLAS=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py
OUT="$SCRATCH/atlas-ta2.html"
```

The probe `page_data` reads a page's data:

```python
import json
def page_data(path):
    page = open(path, encoding="utf-8").read()
    mark = '<script id="atlas-data" type="application/json">'
    return json.loads(page.split(mark, 1)[1].split("</script>", 1)[0])
```

- **AC1** — When `"$PY" "$ATLAS" --ref 9e21ac760 --claims none --out "$OUT"` runs, it exits 0, and
  `page_data` reads `state.commit` as `9e21ac760`'s full sha. `state.landed` reads dTrueNorth,
  dGroundRules, dSafePassage, dOrderedCharter, dFairHearing, dDeclaredLoop. Their `landing.sha` values
  begin `2511c1181`, `3c0318d95`, `3ada42ab1`, `9760fb746`, `0a760477e` and `9e21ac760`, and
  `state.startable` reads dPlacedRequest, dWitnessedBar.
  Red when: the generator before this unit, whose page data has no `state` key.
  figure: PINNED at `9e21ac760`, from `TOOL-dTrackedAtlas-1`'s AC2.
- **AC2** — When `page_data` reads the same page, the `landed` of area `build` is dTrueNorth, of
  `instruction` dSafePassage and dOrderedCharter, of `spine` dGroundRules, dOrderedCharter and
  dDeclaredLoop, and of `plan` empty. `baseline.measured` is `2026-10-14` and `2026-10-16`, and
  area `review`'s `measured` is `2026-10-14` and `2026-10-15`.
  Red when: `landed` is taken from every owner of the area's gaps, which puts dRankedPlan under
  `plan`.
  figure: PINNED at `9e21ac760`, measured on 2026-11-19 with a scratch probe of `derive`.
- **AC3** — When `page_data` reads the same page, `asBuilt` holds 22 builds in `[chain]` row order
  and 509 rows (PINNED), 51 of them not `baseline`. dTrueNorth's `cl-dClosedLoop-0002` row reads
  `since` `deviation 2026-10-21-build-TOOL-dTrueNorth-2-deviation-3`.
  Red when: the rows come from v2's `[chain]` rather than the view, so no row cites a record.
  figure: PINNED, the view at `9e21ac760` as `read_design_view` read it on 2026-11-19.
- **AC4** — When `grep -c` runs over the edited template for each of `Today: an implicit loop`,
  `Today, measured in` and `Today, as measured`, each counts 0, and `Baseline, measured in` counts 2.
  Red when: any of the three labels remains, as each does at `9e21ac760`.
- **AC5** — When `head -n 4 "$OUT"` runs, its first three lines are `<!doctype html>`,
  `<meta charset="utf-8">` and the viewport line of §4, and the fourth opens `<title>`. A `grep`
  for the `body {` rule shows `margin: 0`.
  Red when: the template as at `9e21ac760`, whose first line is `<title>Closed Loop Atlas</title>`.
- **AC6** — When `"$PY" "$ATLAS" --check --ref 9e21ac760 --claims none --plant state-dropped` runs,
  it exits 1 and its `atlas: the chain state lacks` line names dDeclaredLoop. With `--plant
  asbuilt-dropped` it exits 1 and its `atlas: the as-built view lacks` line names dDeclaredLoop.
  Without `--plant` the same command exits 0.
  Red when: the join under either plant is removed, so the planted run exits 0; or the case is
  unknown, so it exits 1 with `atlas: no plant`, which the line check tells apart.
- **AC7** — When the same command runs with each of `kind-unplaced`, `kind-ghost-tag`,
  `edge-status`, `hop-edge`, `edges-split`, `instruments-decision` and `view-unread`, each exits 1
  and its `atlas:` line is the one that case printed before this unit, recorded in the ledger first.
  Red when: a case exits 0, or prints `atlas: no plant`.
- **AC8** — When `"$PY" "$ATLAS" --check --ref 0000000000 --claims none` runs, it exits 1, the last
  line of its stderr opens `atlas: chain state:`, and the stderr holds no `Traceback`.
  Red when: `derive_actual` lets `StateError` escape as a traceback.
- **AC9** — When a probe loads `"$ATLAS"` by path and prints the SHA-256 of
  `json.dumps(derive(), sort_keys=True)` with the sorted keys of `derive()`, it prints what it
  printed before this unit, recorded in the ledger first. The keys hold no `state`, `baseline` or
  `asBuilt`.
  Red when: `derive` itself reads the chain state, which adds `state` to its keys.
- **AC10** — When AC1's command runs twice to two scratch paths, `cmp` finds the pages equal.
  Red when: the data carries a value read from the clock or from the claim cache under
  `--claims none`.
- **AC11** — When the template's inline script, the one `<script>` element with no attribute, is
  written to a scratch `.js` file and `node --check` runs on it, it exits 0.
  Red when: an edit leaves a syntax error, which a staged stray `)` shows.
- **AC12** — When the browser pane opens `$OUT` served by `python -m http.server` from `$SCRATCH`
  through a temporary launch configuration, the Chain view's table holds 22 rows (DERIVED, one per
  `[chain]` row). Six rows read landed, with the merges of AC1, and dPlacedRequest and dWitnessedBar
  read `can start`. In "Today vs target", the area Build's "Since the baseline" panel names dTrueNorth and `2511c1181`, and no
  measured side is labelled Today.
  Red when: the page at `9e21ac760`, whose Chain view has no table and whose Build area names no
  landing.
  cost: a browser pane, and minutes to load a page of about 17 MB (DERIVED from the 16,856,190 B
  page of §4).
  fixture: a launch configuration written to the worktree's `.claude` folder and deleted after; the
  pane refuses a `file://` open of a page this size.

## 6. Gates

The close runs the plain bar once. It holds the guarded legs of the `selftests` chunk below as
on-demand legs, so they do not run there. This unit adds no gate and no suite arm: the generator's
refusals and plants are observed by the criteria above.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `chain-packet self-test` · `policy fixtures`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft.
- rev-2 · 2026-11-19 · §4 · §5 · §9 · the pass legs' reds after `390c2bc05`, folded from
  2026-11-19-prompt-TOOL-dTrackedAtlas-1-3-spec-writer: the row and size figures of AC3 and AC12
  are pinned on their lines, and each `design_lib` symbol cited by a bare basename now gives its
  repository-relative path. No design change.

## 9. Reuse audit

The seams extended: the generator's own `derive` result, through a new `derive_actual` beside it, and
its `plant_memory` refusal; the template's `views.chain`, `chainDiagram`, `showBuild`,
`views.compare`, `renderArea` and `showArea`, with its `.state-pill` classes. The state document is
`TOOL-dTrackedAtlas-1`'s `derive`. The as-built view is read by
`tools/memory-tree/design_lib.py#read_design_view`, whose host's docstring
(`tools/memory-tree/asbuilt_view.py`) names the atlas render as one of its readers, with the design
keys read by `tools/memory-tree/design_lib.py#read_design_conf` and
`tools/memory-tree/design_lib.py#read_design_keys`. The brief named the bootstrap renderer `asbuilt.py`, and its product successor is the reader taken.
`python tools/codebase-map/reuse_lookup.py "render chain build landed state and as-built clauses into the atlas page"`
ranked only name-stem helpers (`build`, `render`, `build_records`), none a renderer of chain state.
The recall probe returned TOOL-dTrueNorth-6 (the as-built view and its reader), PLAY-dClosedLoop-24
(chain packets pin the as-built view's blob, which this unit never writes), and the 2026-10-20 skip
of the view in `corpus`.

`build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-atlas.md`, its points taken and left:

- Taken: "design against built", each chain build joined to its landed status and its deviation
  records, the atlas rendering the join and owning none of it. The join is per build, from
  `TOOL-dTrackedAtlas-1`.
- Taken: the as-built view read in place of v2's `[chain]`, per build.
- Left: the per-unit join over 484 planned units, and reading the one index's node table, which waits
  on dTotalRecall.
- Left: committed Markdown and Mermaid pages under `help/atlas/`, the three `docs.atlas` policy keys,
  the size budget and the two-way `help/` links. The owner's prompt keeps the page uncommitted.
- Left: the staleness witness of `gap-deploy-23`, which is `TOOL-dTrackedAtlas-3`'s.
- Left: the design map's circular parity arm, which this unit does not touch.

Recall terms used: `python tools/memory-recall/query.py "how should the atlas show which landed chain builds moved an area past the measured baseline and the as-built view" --terms "atlas as-built baseline current-state-measured AREAS landed chain deviation today compare view regenerate"`
