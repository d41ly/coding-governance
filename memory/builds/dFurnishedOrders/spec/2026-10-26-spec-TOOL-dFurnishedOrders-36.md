# TOOL-dFurnishedOrders-36 — the kits' own suites out of the call-site scan on every target: a `project-owned` file or a `*.test.sh` under a kit home spells the retired keys on purpose and is never an adopter's call site

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 8c395e3c · streams tooling · order 6 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-37 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md`)
confirmed finding **id 25 at HIGH**, report item **H4**. Id 10 shares that item and takes
`TOOL-dFurnishedOrders-35`.

Id 25 is the item's blast radius. `tools/workflows/unattended-build.test.sh` names
`unattended-unit.js` and spells `"checklist":` and `"prebuild":` as object keys (`:1053`, `:1100`,
`:1120`, read at `8c395e3c`), and the refusal arms `TOOL-dFurnishedOrders-4` and `-30` keep in it pass each retired key on
purpose. The suite is `role = "project-owned"` (`tools/workflows/kit.toml:35-37`), so `govkit apply`
never writes it and no receipt row names it: the receipt subtraction of `TOOL-dFurnishedOrders-25` S1
leaves it in the population wherever it sits. It sits on gov, under a source-mode receipt once
TOOL-dSafePassage-8 lands, and on an adopter that copy-installed a kit and later took a receipt, since
`cp -r` carries the suites (the comment at `tools/workflows/kit.toml:31-33`).

This unit drops a kit's own suites from the population on every target, receipt or not. It repairs
`TOOL-dFurnishedOrders-25` and builds one step after it (order 6), after unit 35 by the dispatch's id
sort.

## 2. Scope (IN)

- **S1** — The suite subtraction. `derive_call_sites` (`tools/govkit/steps/retired_dispatch_args.py`)
  subtracts, before unit 35's kit-file subtraction, every tracked file under a kit home that is a
  `*.test.sh`, or that a kit's descriptor in gov (`<gov tool root>/<home>/kit.toml`) lists in an
  `include` of a `[[files]]` row whose `role` is `project-owned`. A kit home is a directory holding a
  `kit.toml` (`TOOL-dFurnishedOrders-35` S2), or on a receipt target the directory of each receipt row
  whose `source` sits under that kit's home. Observed by AC1.
- **S2** — The scan line counts it. Unit 25 S5's line gains `, <s> kit suite(s)` before unit 35's kit
  files, each file counted once, by the first subtraction that takes it in the order memory root,
  markdown, kit suites, kit files. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The kit files themselves on each target kind: `TOOL-dFurnishedOrders-35`, for id 10.
- An adopter's own suite outside every kit home: it is the adopter's code, and the walk scans it.
- Removing the suites from a copy-install target: the runbook's step (`WIRE-INTO-PROJECT.md`), not
  this program's, since the step writes nothing.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-25` — `derive_call_sites` and its scan line, to which S1 and S2 add the suite subtraction (id 25)
- **consumes-from** `TOOL-dFurnishedOrders-35` — the kit homes its `kit.toml` rule reads, and the kit-file subtraction S1 runs before (ids 10 and 25)
- **hands-off** `TOOL-dFurnishedOrders-40` — S1's kit home on a receipt target, which unit 40 S1 to S3 define from the kit's declaration (id 28 of the third audit)
- **hands-off** `TOOL-dFurnishedOrders-41` — S1's suite subtraction, its descriptor read and AC2, which unit 41 S3 and S7 to S11 settle (ids 10, 15, 17, 24, 33, 8 of the third audit)

## 4. Design

### The subtraction order

```
git ls-files -z
  - <memory_root>/**                                   unit 25
  - *.md                                               unit 25
  - kit suites: *.test.sh, project-owned includes      this unit
  - kit files: kit source, receipt or kit.toml homes   unit 35
  = the population
```

### Why the descriptor read is gov's

A receipt target holds no `kit.toml` for an applied kit, and the step runs from gov's tool root, so
gov's descriptor of each kit is the one source of which names are `project-owned`. The suite rule
`*.test.sh` stands beside it because a `project-owned` row names the suites a kit withholds today,
and a suite added later is caught by its name before its row is written.

### What it does not check

- A kit suite that an adopter renamed away from `*.test.sh` and that no `project-owned` row names.

### Inventory

Minted: the count word `kit suite(s)` of S2. No function: S1 is a branch of `derive_call_sites`.

### Migration

None: the steps have never run.

### Rollout

Live at landing, beside units 25 and 35.

### Files touched (estimate)

- `tools/govkit/steps/retired_dispatch_args.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Rely on unit 35's kit-source rule.** It covers gov's own tree only; a receipt-holding adopter
  carrying a copied suite still stops.
- **Drop every file under a receipt kit's home.** An adopter's own script placed beside an applied
  kit would go unscanned, which is the call site the walk exists to name.

## 5. Production-readiness checklist

- security — the step reads gov's descriptors and the target and writes nothing.
- perf / scale — one descriptor read per kit home.
- error / empty / loading states — a descriptor that does not parse refuses the step at exit 1 naming
  it, before any scan.
- observability — the suite count on every scan line.
- risks — a suite renamed away from `*.test.sh` is scanned (§4); its hits name it, so it is visible.
- testing — AC1 and AC2 by a fixture and a probe; the arm of §7 at the close.
- migration — none.
- user docs — none: the step's printed line is what the walk shows.

## 6. Acceptance criteria

- **AC1** — When `python retired_dispatch_args.py witness <target> checklist` and
  `witness <target> prebuild` run over a scratch target whose install receipt, `install.json` under `.governance`,
  holds an `engine` row for the workflows kit's `unattended-unit.js` under `tools/workflows`, and which also
  holds under `tools/workflows/` a copy of the workflows kit's build-harness suite naming
  `unattended-unit.js` and spelling `"checklist": "CK"` and `"prebuild": true`, each exits 0 and its scan line counts `1 kit suite(s)`;
  once a `run-mine.js` under `tools/workflows`, with no receipt row, passes `checklist: 'x'` to `unattended-unit.js`,
  `witness <target> checklist` exits 1 naming that file alone.
  Red when: a kit's own suite stops an adopter's walk, or the subtraction takes an adopter's own file
  beside it.
  fixture: a scratch target repository under `%TEMP%`, built by the pass.
- **AC2** — When `python retired_dispatch_args.py witness . checklist`, run from `tools/govkit/steps`, runs on this
  repository, its scan line's kit-suite count is at least 1.
  Red when: the suite subtraction is dropped, and gov's suites fall to the kit-source rule alone.
  figure: the count is DERIVED at observation time.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · a receipt target carrying a kit suite and an adopter script beside it, staged by dropping S1 so the suite hits · none

## 8. Open questions

- **F1 — Which files are a kit's own suites?** Options: (a) `*.test.sh` under a kit home and every
  `project-owned` include of gov's descriptor; (b) `project-owned` rows only; (c) every file under a
  receipt kit's home. (b) misses a suite added before its row; (c) hides an adopter's script beside an
  applied kit. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the skeptic-judged fix in the
  report. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-25` and `-35` are specced and
  unbuilt at `8c395e3c`. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on each at
  the pass and stops this unit if a named section is still absent then, rung 1, the brief's rule for
  unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the spec audit of the round-1 promotions, id 25
  (HIGH, item H4, shared with id 10).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet(s) mirroring TOOL-dFurnishedOrders-40, TOOL-dFurnishedOrders-41, promoted from the spec audit of the round-2 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `derive_call_sites` (`TOOL-dFurnishedOrders-25` S1) and the `[[files]]` grammar
every kit descriptor carries (`tools/workflows/kit.toml:35-37`), whose `project-owned` role is what
`govkit apply` already withholds. `python tools/codebase-map/reuse_lookup.py "files a kit homes on a
target with no install receipt"` ranked `resolve_kit_dir`, `kit_rel` and `kit_dir`, none a reader of a
descriptor's `project-owned` rows, so no existing seam fits beyond the ones named. The recall probe
returned TOOL-dSafePassage-8's source-mode receipt and unit 25, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which kit files does an upgrade step skip on
gov's own checkout and on an adopter without an install receipt" --terms "install receipt kit.toml
project-owned suite call site retired key upgrade step witness tool root"`
