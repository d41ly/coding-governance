# TOOL-aMendedFleet-13 — LIVE.md counts each build's landed-unclosed units from drift-audit's own join

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-13-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-13-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

A unit can ship while its spec still reads OPEN, SPECCED, BLOCKED or INPROGRESS, and `memory/LIVE.md`,
the file a session reads for work state, cannot say so. drift-audit already answers it: its signal
`non_terminal_specs_cited_by_product_source` joins every non-terminal spec's own id to the tracked
product source that cites it, and read 2 of 42 on 2026-10-04, PINNED. This unit renders that join's
answer into `LIVE.md` as a per-build `Landed-unclosed` count, by calling the drift kit's signal
rather than re-implementing it, so the work-state file and the drift report cannot disagree.

## 2. Scope (IN)

- **S1** — With `LIVE_LANDED_UNCLOSED` set to `1`, the generator resolves the drift-audit kit through
  the `resolve_kit_dir` copy `tools/memory-tree/backlog.py` already carries, imports
  `drift_report`, builds its `Ctx` from the kit's own `load_conf` and `load_project_layer` with the
  base ref `HEAD`, and calls `signal_spec_status` once. Nothing of the join is restated in the
  memory-tree kit. Observed by AC1.
- **S2** — A pure function maps the signal's `detail` rows to a count per live build: a row counts
  for a build when its `file` sits under that build's `spec/` folder AND its `id` is one of that
  build's units in the generator's own tracked reading. A row for a terminal build, or for a spec the
  generator does not track, counts nowhere. Observed by AC1 and AC2.
- **S3** — `LIVE.md` gains one trailing column, `Landed-unclosed`, an integer on every row, zero
  included, placed after any column `TOOL-aMendedFleet-12` adds; and one opening sentence saying the
  count is drift-audit's join and a candidate to close, not a verdict, placed after the dormancy
  sentence that unit renders when both keys are set. Observed by AC1.
- **S4** — Liveness: when the signal reports zero evidence files, the population its join reads is
  empty and every zero would be a reassuring one, so the generator refuses with a named error before
  writing any artifact. A tree with no non-terminal keyed spec renders zeros, which are a reading.
  Observed by AC3.
- **S5** — Refusals, each a named error and no artifact written: a value other than blank or `1`;
  the key set while the drift kit does not resolve, naming the kit and the places looked; and a
  drift-kit error, such as a missing project layer, carried through with its own text. Observed by
  AC4 and AC5.
- **S6** — Blank or undeclared, the key renders `LIVE.md` byte-identical to the render without this
  unit, and the drift kit is never imported. Observed by AC6.
- **S7** — Declarations: this repo's `.memory-tree.conf` sets the key to `1`; the kit's
  `.memory-tree.conf.example` declares it blank with a comment; `tools/memory-tree/kit.toml` gains a
  `requires_if` row naming `drift-audit` on the key, the shape its sibling rows use; the module
  docstring's source list names the join as a fifth source read only under the key; and the kit
  README's generator row names the column and the key. Observed by AC7.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- A second join. A non-terminal spec whose id appears in a product COMMIT subject is the predicate of
  node d's dLandedVerdict unit 1, live on that node and not on main; when it lands, a follow-up may
  add its rows to the same count.
- Making the drift signal faster. It spawns one `git grep` per non-terminal spec, 1.48 s for 42 on
  node a on 2026-10-04, PINNED; batching it into one spawn is a drift-audit change and is not needed
  for this render.
- Listing the cited ids in `LIVE.md`. The row is in the index entry-budget population, and the ids
  are one `drift_report.py --json` call away.
- Closing, flagging or filing anything about a counted unit. The count reports.
- The memory-tree kit version bump, owed once at this build's close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-12` — the column order and the sentence order: this unit's
  column follows the two that unit adds, and its opening sentence follows that unit's, when both keys
  are set.
- **consumes-from** external — the drift-audit kit and its filled project layer, which this repo
  carries; without them the key is refused, never silently skipped.
- **hands-off** external — the commit-subject predicate of node d's dLandedVerdict unit 1, and the
  memory-tree kit version bump owed by this build's close.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 at `6a88fbf7`, whose `tools/` bytes equal base.

- `signal_spec_status` in `tools/drift-audit/drift_report.py` globs `builds/*/spec/**/*.md`, keeps a
  spec whose status is in `NON_TERMINAL`, which is OPEN, SPECCED, BLOCKED and INPROGRESS, takes the
  spec's own id from its H1, and runs `git grep -l -w -F <id>` over `EVIDENCE_GLOBS` from the project
  layer. Its record carries `value`, `of`, `evidence_files`, `live` and `detail`, each detail row
  naming `file`, `id`, `status` and up to three `cited_in` paths. Called through the module on the
  live tree it returned 2 of 42 in 1.48 s, `TOOL-aBatchedLintel-1` and `TOOL-dNarrowedAnchor-1`, the
  same two the drift report prints.
- The signal globs the filesystem, so an untracked spec reaches it; the generator reads tracked
  files only. S2's intersection with the generator's own units keeps the render a function of the
  tracked tree.
- `Ctx` needs a base ref and the signal does not read it, so S1 passes `HEAD` rather than resolving
  the remote, which keeps the render offline.
- `tools/memory-tree/backlog.py` carries the gated `resolve_kit_dir` canonical copy, which resolves a
  sibling kit by install receipt, then by probe, and raises `LookupError` naming the places looked.
- Importing `drift_report` sets `sys.dont_write_bytecode` for the process and puts the drift kit
  directory on `sys.path`; no module name there collides with one the memory-tree kit imports.

### Data model

```
| Build | Status | Node | Opened | Streams | Ids (n) | [Last record | Activity |] Landed-unclosed |
```

The bracketed pair is `TOOL-aMendedFleet-12`'s and renders only under its key. The opening sentence,
rendered only under this key: `Landed-unclosed: the build's non-terminal units whose id tracked
product source cites, by drift-audit's non_terminal_specs_cited_by_product_source join. A candidate to
close, not a verdict.`

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_landed_unclosed` | function: root and conf in, the signal record out | `py.function`, verb `read` |
| `derive_landed_counts` | function: the record and the builds in, a count per slug out | `py.function`, verb `derive` |
| `LIVE_LANDED_UNCLOSED` | conf key, `.memory-tree.conf` | conf key; blank means off |

A name the lexicon leg refuses is replaced with its `--suggest` answer at build time, and this table
is amended with a rev bump.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/README.md`
- `tools/memory-tree/.memory-tree.conf.example`
- `.memory-tree.conf`
- `memory/LIVE.md`
- `memory/map/generated/symbols.json`

### Rollout

Dark by key. An adopter's `LIVE.md` is unchanged until it sets `LIVE_LANDED_UNCLOSED`, which also
declares that it carries the drift kit; this repo sets it in the commit that re-renders its file.

### Alternatives rejected

- **Spawning `drift_report.py --json`.** Measured 31.7 s on the live tree, every signal computed to
  read one, on every `--check`. Lost on cost.
- **Re-implementing the join in the generator with its own glob list.** A second declaration of what
  product source is, beside `EVIDENCE_GLOBS`, and a second predicate to drift from the first; the
  brief asks for reuse.
- **A new CLI mode on the drift report for this one signal.** A new public surface on another kit,
  where an import of an existing function needs none.
- **Rendering the cited ids.** The row is in check 7's entry-width population; a count holds.

## 5. Production-readiness checklist

- security — N/A — a read-only render; the join greps tracked files with a fixed argv the drift kit
  builds from its tracked project layer.
- perf / scale — one in-process call, 1.48 s at 42 non-terminal specs on node a, PINNED 2026-10-04,
  growing with the non-terminal spec count; paid only under the key.
- error / empty / loading states — S4's empty-evidence refusal and S5's three refusals; zero
  non-terminal specs renders zeros.
- observability — the opening sentence names the signal, so a reader can run the drift report for
  the ids behind a count.
- risks — a product commit that newly cites a live non-terminal id makes `LIVE.md` stale, and the
  freshness check names `--write` as the remedy; the drift records leg already reds the same event
  against the signal's pin. A partial commit of product source can leave the committed render stale,
  as for any generated artifact.
- testing — two `--selftest` arms and direct calls on the live tree, AC2 and AC6 among them.
- migration — N/A — a rendered file.
- user docs — the kit README's generator row and the example conf comment, S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` runs on the live tree, the
  `memory/LIVE.md` header row ends `| Landed-unclosed |`, and each row's count equals the number of
  `detail` rows under that build in the `non_terminal_specs_cited_by_product_source` record of
  `python tools/drift-audit/drift_report.py --json`, read in the same minute.
  Red when: a count disagrees with the drift report, or a row lacks the cell.
  figure: DERIVED at observation time; at writing, one each for `aBatchedLintel` and
  `dNarrowedAnchor`, zero elsewhere.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, an arm hands the pure
  mapping a canned record of three rows, one for a live build's tracked unit, one for a terminal
  build's unit and one for a spec the fixture does not track, and asserts a count of 1 on the live
  build and 0 everywhere else.
  Red when: a terminal or untracked row is counted, or the live one is missed.
- **AC3** — When `EVIDENCE_GLOBS` in `tools/drift-audit/drift_signals.py` is staged as a single glob
  matching no tracked file and `python tools/memory-tree/gen_build_index.py --check` runs, it exits
  non-zero with a line naming the empty evidence population and renders no column of zeros;
  restoring the file restores the clean run. That edit is the staged break for S4.
  Red when: the run exits 0 or prints a render.
- **AC4** — When `LIVE_LANDED_UNCLOSED` in `.memory-tree.conf` is staged as `yes` and
  `python tools/memory-tree/gen_build_index.py --check` runs, it exits non-zero naming the key and its
  two legal values. That edit is the staged break for S5's value refusal.
  Red when: the value renders or exits 0.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, an arm with the key
  set and a resolver that raises `LookupError` asserts a named error carrying `drift-audit` and the
  key, and no artifact.
  Red when: an unresolved kit renders the file or a traceback.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, an arm with the key
  blank and a resolver that raises if called asserts the `LIVE.md` render equals the render without
  this unit, byte for byte.
  Red when: a blank key imports the drift kit or moves a byte.
- **AC7** — When `grep -n "LIVE_LANDED_UNCLOSED" .memory-tree.conf tools/memory-tree/.memory-tree.conf.example tools/memory-tree/kit.toml tools/memory-tree/README.md tools/memory-tree/gen_build_index.py`
  runs, every file reports a hit, this repo's value is `1`, the example's is blank, and the
  `kit.toml` hit sits in a `requires_if` row naming `drift-audit`.
  Red when: a carrier omits the key, or the requires row is missing.

## 7. Gates

`build-index selftest` · `build README slot contract` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `govkit selfcheck` · `drift-audit records` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py --selftest · a canned three-row record, a raising resolver under the key, and one under a blank key · none

## 8. Open questions

- **F1** — How does the generator reach the join?
  Options: spawn the whole drift report; re-implement the predicate; add a drift CLI mode; import
  the drift module and call the signal. §4 records why each of the first three lost.
  RESOLVED (agent, 2026-10-04, delegated): import and call `signal_spec_status`.
- **F2** — Does LANDED-UNCLOSED also read product commit subjects?
  Options: the source-citation join alone, which the report names; add the commit-subject predicate,
  which is node d's live dLandedVerdict unit 1 and exists on no ref of main.
  RESOLVED (agent, 2026-10-04, delegated): the source-citation join alone; §3 hands the other off.
- **F3** — Is the column on by default where the drift kit resolves?
  Options: on whenever the kit resolves; behind a key. On by default changes every adopter's
  `LIVE.md` at its next kit update and couples two kits silently.
  RESOLVED (agent, 2026-10-04, delegated): behind `LIVE_LANDED_UNCLOSED`, blank meaning off.
- **F4** — What does the render do when the join's evidence population is empty?
  Options: render zeros; refuse. A zero from an empty population is the reassuring zero §7 of the
  charter forbids.
  RESOLVED (agent, 2026-10-04, delegated): refuse, per S4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `signal_spec_status`, its `Ctx`, `render_live` and a timed
  call of the signal on the live tree.
- rev-2 · 2026-10-04 · §2 S8 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
  §2 S3 and the §3 edge also say where its opening sentence sits beside
  `TOOL-aMendedFleet-12`'s, which neither spec stated.

## 10. Reuse audit

The seam reused is `signal_spec_status` in `tools/drift-audit/drift_report.py`, called whole through
the kit's own `Ctx`, `load_conf` and `load_project_layer`, and reached by the `resolve_kit_dir` copy in
`tools/memory-tree/backlog.py`; the render seam extended is `render_live` in
`tools/memory-tree/gen_build_index.py`. `python tools/codebase-map/reuse_lookup.py "non-terminal spec
whose id is cited by product source shipped but not closed"` returned name-stem neighbours only and
not the drift signal, which `git grep -n non_terminal_specs_cited tools/` found. Recall returned
`TOOL-aBoundedVerdict-30`, which added the `-w` that keeps `-1` from matching inside `-11`, and
`TOOL-dCarriedReceipt-4`, a spec deliberately held open while cited, the false-positive shape S3's
"candidate, not a verdict" sentence answers. Where the report and the tree disagree: the report
calls this a join of spec ids to product COMMITS and quotes 2 of 29; the tree joins spec ids to
product SOURCE files and read 2 of 42 at writing, so the reuse is of the source join, and the commit
join is node d's unlanded work.

Recall terms used: `python tools/memory-recall/query.py "how is a spec that shipped but is still open
detected, landed but unclosed" --terms "non_terminal_specs_cited_by_product_source EVIDENCE_GLOBS
landed unclosed spec status cited product source drift-audit signal LIVE.md"`
