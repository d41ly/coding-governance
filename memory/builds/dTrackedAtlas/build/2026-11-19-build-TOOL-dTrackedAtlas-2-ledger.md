# TOOL-dTrackedAtlas-2 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-2

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command from the worktree root, the page written to the run's scratch directory and never into the
repository. Each red case was observed on the shape the criterion names: the generator and template as
they stood at the unit's start (`a47c438bb`), or a staged break in a scratch probe that compiles the
generator's source with one substitution, under the generator's own path, and runs it in memory, so the
tracked file was never edited to stage a red.

Recorded before the first edit, at `a47c438bb`:

- AC9's probe printed `8bbf287e2f1ac362607683b2165ec614f40a2bb37de5c7e336f918b81226bc8c` and the keys
  `areas build chain consult contract contracts cycle decisions digest events gaps kitFates kits latest`
  `layers libraryItems libraryPaths libraryRound loops memory oneLine owed policies presets principles`
  `programs progress records reviews roster sources steps terminal timeline tools transitions v2map v2open`.
- AC7's cases under `--check --plant <case>`, each exiting `1`:
  - `kind-unplaced`: `atlas: layer-memory [contract] kind 'ghost kind' names no writer item and carries no marker`
  - `kind-ghost-tag`: `atlas: layer-memory [contract] kind 'ghost kind' names ['plan.ghost-writer'], resolving to no item, key or file`
  - `edge-status`: ``atlas: memory-plan [edges] row '`made-by`': status 'nwe' unread``
  - `hop-edge`: `atlas: memory-plan [cycle] hop 'work order → act': a family, its state or an edge is unread ['answered-by-typo']`
  - `edges-split`: `atlas: memory-plan [edges] holds 25 row lines but its table parsed 1: a split table drops rows`
  - `instruments-decision`: `atlas: night-pass-instruments is an instruments record, yet its section 'The owner's answers, folded' reads as a decision; an instruments record holds scripts and runs, so retitle the section`
  - `view-unread`: `atlas: v2's sections ['planned'] map to a view that reads none of them; map them to records or render them`
- `state-dropped` and `asbuilt-dropped` each printed `atlas: no plant <case>; the cases are kind-unplaced, ...`.

**Evidences:** TOOL-dTrackedAtlas-2
- AC1 — `"$PY" "$ATLAS" --ref 9e21ac760 --claims none --out "$OUT"` exited `0`. `page_data` read
  `state.commit` `9e21ac760dc0a43d6ed007396922722ccee98d57`, `state.landed` dTrueNorth, dGroundRules,
  dSafePassage, dOrderedCharter, dFairHearing, dDeclaredLoop with `landing.sha` beginning `2511c1181`,
  `3c0318d95`, `3ada42ab1`, `9760fb746`, `0a760477e`, `9e21ac760`, and `state.startable` dPlacedRequest,
  dWitnessedBar. Red: the page of the generator at `a47c438bb` has no `state`, `asBuilt` or `baseline` key.
- AC2 — the same page: `landed` of `build` dTrueNorth, of `instruction` dSafePassage and dOrderedCharter,
  of `spine` dGroundRules, dOrderedCharter and dDeclaredLoop, of `plan` empty; `baseline.measured`
  `2026-10-14` and `2026-10-16`; `review`'s `measured` `2026-10-14` and `2026-10-15`. Red: a staged
  `landed` taken from every owner of the area's gaps read `plan` as dRankedPlan.
- AC3 — the same page: `asBuilt` holds `22` builds in `[chain]` row order and `509` rows, `51` not
  `baseline` (PINNED at 9e21ac760); dTrueNorth's `cl-dClosedLoop-0002` reads `since`
  `deviation 2026-10-21-build-TOOL-dTrueNorth-2-deviation-3`. Red: a staged read of the rows from v2's
  `[chain]` through `tools/memory-tree/design_lib.py#read_chain_clauses` gave `22` builds, `509` rows and
  `0` citing a record.
- AC4 — `grep -c` over the edited template: `Today: an implicit loop` `0`, `Today, measured in` `0`,
  `Today, as measured` `0`, `Baseline, measured in` `2`. Red: the template at `a47c438bb` counted
  `1`, `2`, `1` and `0`.
- AC5 — `head -n 4 "$OUT"` printed `<!doctype html>`, `<meta charset="utf-8">`, the viewport line and
  `<title>Closed Loop Atlas</title>`; the `body {` rule reads `margin: 0`. Red: the template at
  `a47c438bb` opens with `<title>Closed Loop Atlas</title>`.
- AC6 — `--check --ref 9e21ac760 --claims none --plant state-dropped` exited `1` with
  `atlas: the chain state lacks dDeclaredLoop and holds none the chain does not`;
  `--plant asbuilt-dropped` exited `1` with
  `atlas: the as-built view lacks dDeclaredLoop and holds none the chain does not`; without
  `--plant` it exited `0`. Red: each join staged away, the planted run exited `0`; before this unit
  each case exited `1` with `atlas: no plant`, which the line check tells apart.
- AC7 — the same command with each of the seven cases exited `1` and printed the line recorded above,
  byte-equal under `diff`. Red: a staged admission without `CORPUS_PLANTS` printed
  `atlas: no plant instruments-decision`.
- AC8 — `--check --ref 0000000000 --claims none` exited `1`; the last stderr line is
  `atlas: chain state: 0000000000 resolves to no commit in <worktree>`, with no `Traceback`. Red: a staged handler
  catching `ChainError` alone let `StateError` escape as a traceback.
- AC9 — the probe printed the hash and the keys recorded above, equal under `diff`; no `state`,
  `baseline` or `asBuilt`. Red: a staged `derive` returning a `state` key, an empty one rather than a
  document read through git, which the key check reads alike and the hash tells apart either way, printed
  `cb94e61ff4ca74cac4f77a61becc205450e641ed90ebf6c2551a2c1ce321ac9e` with `state` among its keys.
- AC10 — AC1's command to two scratch paths: `cmp` exited `0`. Red: a staged clock value in the data
  made `cmp` exit `1`.
- AC11 — the template's one attribute-free `<script>` written to a scratch `.js` file: `node --check`
  exited `0`. Red: a staged stray `)` exited `1`.
- AC12 — not observed in the browser pane, which this pass cannot open: owed to the close. A headless
  Edge `--dump-dom` of `$OUT` served by `python -m http.server` from the scratch directory stood in for
  the render: the Chain view's table held `22` rows (DERIVED, one per `[chain]` row), six reading
  `landed` or `landed, carrying 1` with AC1's merges, dPlacedRequest and dWitnessedBar reading
  `can start`; the Comparison view's side labels read `The baseline: an implicit loop` and
  `Baseline, measured 2026-10-15`, none `Today`; and the default area, Instruction, showed its "Since the
  baseline" panel naming dSafePassage `3ada42ab1` and dOrderedCharter `9760fb746`. The Build area's
  panel, which needs a click, was not observed.

Owed to the close: the plain bar; AC12 in the browser pane, with its red on the page at `9e21ac760`.

Owed to the close, and since observed by the main loop in the browser pane: AC12. Green at the close tip
`2d8acb04e93b`, on its page served from scratch (`--out --claims none`, `git hash-object`
`11f11aeed5cb`): the Chain view's table holds one row per chain build; six read landed with AC1's merges
`2511c1181`, `3c0318d95`, `3ada42ab1`, `9760fb746`, `0a760477e` and `9e21ac760`; dPlacedRequest and dWitnessedBar
read `can start`; the Build area's "Since the baseline" panel reads
`dTrueNorth landed · 2511c1181 merge: dTrueNorth — land onto origin/main at 271aa59d`; no leaf of the view reads
`Today`. Red on the page the generator at `9e21ac760` wrote with `--out` alone (`git hash-object`
`0d66ebbbed8c`): no build-state table in the Chain view, and no "Since the baseline" panel for the Build area.
