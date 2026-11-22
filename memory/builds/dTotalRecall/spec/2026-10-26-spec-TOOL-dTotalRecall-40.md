# TOOL-dTotalRecall-40 — the routing region reads every record kind through `resolve_kind`, so log records written after the rename route under logs

**Status:** INPROGRESS · rev-4 · 2026-11-22 · node d · Tier-2 · base 94e17798 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-build-TOOL-dTotalRecall-40-deviation-401.md](../build/2026-10-26-build-TOOL-dTotalRecall-40-deviation-401.md) | deviation | — |
| [2026-11-22-build-TOOL-dTotalRecall-40-reground-2-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-40-reground-2-return.md) | research | — |
| [2026-11-22-build-TOOL-dTotalRecall-40-reground-return.md](../build/2026-11-22-build-TOOL-dTotalRecall-40-reground-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-53 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-11-22-prompt-TOOL-dTotalRecall-40-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-40-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-40-reground-2-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-40-reground-2-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-40-reground-2-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-40-reground-2-spec-writer.md) | log | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-40-reground-brief.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-40-reground-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dTotalRecall-40-reground-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-40-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 36 at HIGH**, its item **H5**, alone in that item; its finding id 9 reports the
same defect at MEDIUM in item M8 and is disposed in `TOOL-dTotalRecall-43`. The audit read
`TOOL-dTotalRecall-4` §4 "The routing region" routing "each build/ record whose kind is `journal`",
read raw from the bindings `plan()` reads once. `TOOL-dTotalRecall-18`, CLOSED at `305b6e9d1`, renamed
the kind `log`: every writer writes `log`, `read_bindings` keeps the written token, and a comparison by
value reads it through `resolve_kind` (`tools/memory-tree/tree_lib.py#resolve_kind` over
`#KIND_ALIASES`; unit 18 S7, S8). Unit 4's rev-6 spec names `resolve_kind` for its `logs` row, but
its AC5 plants one record per typed kind and none under the alias, so no criterion sees a `journal`
and a `log` binding route together, and nothing reds a raw comparison of the retired token elsewhere.
This unit holds every kind comparison of `render_routes` to `resolve_kind`, re-pointing any its pass
finds raw, witnesses the pair under `logs`, and adds a census that reds a raw comparison of a retired
kind token anywhere in the tool root. It repairs `TOOL-dTotalRecall-4`.

## 2. Scope (IN)

- **S1** — `render_routes` in `tools/memory-tree/gen_build_index.py`, as `TOOL-dTotalRecall-4` S5 lands
  it at order 8, reads each record's kind once as `resolve_kind(<the written token>)` and compares that
  value on every row: each member of `TYPED_RECORD_KINDS`, `research`, and the `logs` row against
  `log`. A record bound `**Serves:** journal` and one bound `**Serves:** log` both route under `logs`.
  A comparison the pass finds on the written token is re-pointed and every build README's
  `build-routes` region re-rendered by `gen_build_index.py --write`; where unit 4 landed each comparison
  through `resolve_kind`, no region changes (§8 F3). Observed by AC1 and AC2.
- **S2** — The alias census, `check_alias_compares(root, tool_rel)` in `tools/memory-tree/record_kinds.py`,
  an arm of `check_record_kinds` (`#check_record_kinds`) returning `(lines, reds)` as the pocket arm
  `#check_pockets` does, so `--check` runs it. It reads every tracked `*.py`, `*.sh` and `*.js` file under the tool
  root through `read_tracked` (`#read_tracked`, `#derive_tool_rel`) and lists each line spelling a key of
  `tree_lib.KIND_ALIASES` as a quoted literal that is an operand of `==`, `!=`, `===` or `!==`, a member
  of the bracket after ` in (` or ` in [`, or, in a `*.sh` file, a `case` pattern. A listed line is red
  unless the constant `ALIAS_COMPARE_KEPT`, `{<path under the tool root>: <reason>}`, keys its file, and
  is then printed `kept <reason>`. A reason names one of two causes: a fixture planting a legacy record
  on purpose, or a homonym, the token naming no record kind (§8 F4). The alias table's own line, a dict
  literal, is no comparison form. The plant's text is spelled in parts, as `#build_fixture` spells a kit
  path, so the census's own source holds no hit. The predicate was run over the real tree before the
  constant is written (§4 "The census at base"). Observed by AC3 and AC4.
- **S3** — Unit 2's half of the finding, its S9 row list naming the `journal` row, is handed to
  `TOOL-dTotalRecall-43` (its S8), because the door `gov_record.py` is built at order 12, after this unit.
  S2's census reds that half at the close if the door compares the alias token raw. NOT OBSERVED by a
  criterion of this unit: `TOOL-dTotalRecall-43`'s item for id 9 observes it.

## 3. Non-goals (OUT)

- The routing region's purposes, its bound of two records per purpose and its `card ref` row:
  `TOOL-dTotalRecall-4`'s, unchanged.
- The rename, `KIND_ALIASES` and `resolve_kind`: `TOOL-dTotalRecall-18`'s.
- Rewriting any record's Serves token: the alias is read, never normalised on disk.
- Renaming the govkit shim's `journal` mode, a policy value adopters set (§8 F4).
- A regex or unquoted form and a population outside the tool root, which `TOOL-dTotalRecall-53`
  widens, and a kept file whose lines no longer hit, which `TOOL-dTotalRecall-66` S3 drains.

### Edges

- **consumes-from** `TOOL-dTotalRecall-4` — `render_routes` and the `build-routes` region, whose kind
  comparisons this unit holds to `resolve_kind`
- **consumes-from** `TOOL-dTotalRecall-18` — `resolve_kind` and `KIND_ALIASES` in `tree_lib.py`, landed at
  `305b6e9d1`, the one alias reader S1 calls and the alias set S2's census reads
- **consumes-from** `TOOL-dTotalRecall-1` — `record_kinds.py` and its `--check`, as unit 18 completed it,
  which the alias census joins
- **hands-off** `TOOL-dTotalRecall-43` — the door's S9 row list naming the retired `journal` row,
  `TOOL-dTotalRecall-2`'s half of this finding and of id 9, built at order 12 after this unit
- **hands-off** `TOOL-dTotalRecall-53` — `check_alias_compares` and `ALIAS_COMPARE_KEPT`, whose forms, population and keep grammar that unit widens (the round-1 audit of units 36 to 43, ids 19, 29, 36 and 46)

## 4. Design

### The region, after this unit

| Purpose | Read |
|---|---|
| `<kind>`, one row per member of `TYPED_RECORD_KINDS` | each `build/` record whose `resolve_kind` is that member |
| research | each `build/` record whose `resolve_kind` is `research` |
| logs | each `build/` record whose `resolve_kind` is `log`, a `journal` binding read as its alias |

The other rows of `TOOL-dTotalRecall-4` §4 are unchanged. The kinds still come from `binds_all`, read
once in `plan()` (`tools/memory-tree/gen_build_index.py#plan`) and attached as `build["records"]`; only
the comparison is held. Unit 4 registers the region in `#GEN_REGIONS` and its renderer in
`#REGION_RENDERERS`, neither of which holds it at `94e17798f`.

### The census at base

Re-derived at `94e17798f`, after units 5, 16, 25, 38 and 54 landed: S2's predicate, run as a probe over the 381 tracked code files under
`tools/` (DERIVED, `git ls-files tools | grep -cE "\.(py|sh|js)$"`), lists 7 lines in 2 files (DERIVED,
the probe), none a kind comparison: unit 18 re-pointed every reader its sites table names. Each is the
govkit shim's `install.on-shim-call` mode `journal`, a homonym: `tools/govkit/shims.py#JS_TEMPLATE`
(two lines), `#PY_PRELUDE` (two), `#run_forward_plant` (two), and `tools/govkit/selftest.py@94e17798f:20615`,
a mode list in `main`. `ALIAS_COMPARE_KEPT` therefore opens keying those two files by their paths
under the tool root, each reason `homonym: the shim's install.on-shim-call mode`. The pass re-runs the
probe at its base, after unit 4, and a hit outside these is a comparison to
re-point in this pass, by the same rule as S1, or a fixture to key with its reason.

### Inventory

Minted: `check_alias_compares` and `ALIAS_COMPARE_KEPT` in `tools/memory-tree/record_kinds.py`; the
plants `raw-alias-compare` and `alias-compare-kept` in its `#PLANTS`. Naming cell:
`python tools/lexicon/lexicon.py --suggest check_alias_compares --as py.function` answered OK at
`94e17798f`, `check` a VERBS entry of `.lexicon.conf`.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py` (`render_routes`, where the pass re-points; the `--selftest` arm)
- `tools/memory-tree/record_kinds.py` (the census, its constant, its plants, its docstring's gate and
  WHAT IT DOES NOT CHECK paragraphs)
- `memory/builds/` (each README's `build-routes` region, re-rendered by `gen_build_index.py --write`
  where S1 re-points a comparison)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Route on the written token and list both `journal` and `log` in the row.** Two spellings of one
  kind in one renderer, which is the comparison class `resolve_kind` exists to end.
- **Normalise the token on read in `read_bindings`.** `TOOL-dTotalRecall-18` §8 rejected it: every
  records region would change bytes.

## 5. Production-readiness checklist

- security — no new surface; the census reads tracked files and writes nothing.
- perf / scale — one dict lookup per record kind; the census reads 381 files (DERIVED, §4) once per
  `--check`, under the `record-kinds` leg's ceiling, 122 s (DERIVED, its row in `tools/gate-legs.json`),
  whose evidenced run is 1.6 s (`tools/run-gates/ceiling-evidence.txt:121`).
- error / empty / loading states — a build with no log record renders no `logs` row, as before; a
  tree with no tracked code file under its tool root lists nothing and prints the count line.
- observability — the census prints each hit's path and line, red or `kept <reason>`, and a count line.
- risks — a file-keyed keep hides a real kind comparison added to a kept file (§7).
- testing — AC1 to AC4 by the pass; the arms of §7 at the close.
- migration — the re-render of S1, only where it re-points.
- user docs — none under `help/`: no page describes the routing region or `--check`'s arms.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` runs in a scratch clone of the pass
  tip under `%TEMP%`, holding one added build folder with a `build/` record bound
  `**Serves:** log TOOL-bRoutes-1` and another bound `**Serves:** journal TOOL-bRoutes-1`, its README's
  `build-routes` region names both under `logs`.
  Red when: the region compares the written token, so one of the two is absent.
  fixture: the scratch clone; the pass makes it, its ids in the `TOOL` family the clone's `FAMILIES`
  holds, since an id of no family binds `malformed` and routes nowhere, as `read_bindings` reads it; its
  README types no front-matter key unit 4 derives, which unit 4's AC4 refuses on a new README.
- **AC2** — When a probe prints `render_routes`' source through `ast.get_source_segment` at the pass tip,
  no line of it spells `journal` and it calls `resolve_kind`.
  Red when: the renderer keeps a raw comparison beside the `resolve_kind` call.
- **AC3** — When `python tools/memory-tree/record_kinds.py --fixture --plant raw-alias-compare` runs at the
  pass tip, where a planted file under the fixture's tool root spells `if kind == "journal":`, it exits 1
  with a RED line naming that file and line under the alias census; at the pass tip
  `python tools/memory-tree/record_kinds.py --check` prints no alias-compare RED line.
  Red when: the census reads only `gen_build_index.py`, so a comparison in another module escapes.
- **AC4** — When `python tools/memory-tree/record_kinds.py --check` runs at the pass tip, it prints
  the hits of the two govkit files §4 names as `kept homonym`, and
  `record_kinds.py --fixture --plant alias-compare-kept` exits 0 printing its planted line `kept`.
  Red when: a kept file's line reds, or a kept line is dropped from the output instead of printed.

## 7. Gates

`build-index selftest` · `build README slot contract` · `tier2-review self-test` · `memory hygiene` · `memory-hygiene self-test` · `record-kinds` · `chain-packet self-test` · `policy fixtures` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 · `--selftest` gains the routes plant, a `log` and a `journal` record in one build, both under `logs`, staged by comparing the written token · none
New arm: tools/memory-tree/record_kinds.py · covers AC3 AC4 · `--selftest` gains the plants `raw-alias-compare`, red, and `alias-compare-kept`, shown kept, staged by cutting `check_alias_compares` from `check_record_kinds` · none

What these do not check: a comparison through a variable holding the alias, a regex form such as the
`awk` `(log|journal)` readers, an unquoted shell test such as `[ "$x" = journal ]`, and any file outside
the tool root (unit 53 widens the forms and the population); a real kind comparison added to a kept
file, which the file-keyed keep hides; and a kept file that no longer hits (unit 66 S3's drain).

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-4`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Is the row's purpose label `journals` or `logs`?** Options: (a) `logs`, the canonical kind's
  name; (b) `journals`, keeping the region's bytes for legacy-only builds. (b) labels the canonical
  kind by its alias, the reading `TOOL-dTotalRecall-18` S9 re-spells in every prose carrier.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the report's fix text and unit 18's S9.
  widens: none · relaxes: none
- **F3 — What does S1 do now unit 4's re-ground names `resolve_kind` for its `logs` row?** Options: (a)
  keep S1 as the hold, re-pointing any raw comparison the landed renderer keeps, with AC1's pair and
  AC2's source probe; (b) drop S1 and leave H5 to unit 4. (b) fails AC1 and AC2, and unit 4's AC5 plants
  no alias, so veto 1 discards it. RESOLVED (agent, 2026-11-22, delegated): (a), the one survivor.
  widens: none · relaxes: none
- **F4 — How does the census treat the shim's `journal` mode, 7 hits at base (DERIVED, §4)?** Options:
  (a) `ALIAS_COMPARE_KEPT` admits a homonym reason beside the fixture reason, keying the two govkit
  files; (b) narrow the predicate to lines naming a kind context (`kind`, `Serves`, `binds`); (c) rename
  the shim mode. (c) changes a policy value adopters set, a public surface: veto 2. (b) lets a raw
  comparison on any other variable name pass, so it reds fewer cases than (a). RESOLVED (agent,
  2026-11-22, delegated): (a), the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 36 (HIGH, item H5).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.
- rev-3 · 2026-11-22 · title · §1 · S1 · S2 · §3 · §4 · §5 · AC1 to AC4 · §7 · §8 F3, F4 · §10 · re-grounded
  at `8fbc5a337` per `2026-11-22-prompt-TOOL-dTotalRecall-40-reground-brief`: `canonical_kind` is
  `resolve_kind` as unit 18 landed it; S1 holds unit 4's renderer, whose rev-4 already names the call
  (F3), over its typed rows; the census is an arm of `check_record_kinds` over the tool root, keyed by
  tool-root path, its base population 7 homonym lines in govkit (F4) and AC4 its keep; AC1's ids move
  to a real family; the legs `record-kinds`, `memory-hygiene self-test`, `chain-packet self-test`,
  `policy fixtures` and `spec tokens` join §7.
- rev-4 · 2026-11-22 · header · §1 · S2 · §4 · AC1 · re-grounded at `94e17798f` per
  `2026-11-22-prompt-TOOL-dTotalRecall-40-reground-2-brief`: the census probe re-run over the landed units 5,
  16, 25, 38 and 54 still lists 7 homonym lines in 2 govkit files over 381 files (DERIVED, §4); S2's return
  shape is `#check_pockets`', `#check_serves_aliases` returning one line; unit 4 is cited at its rev-6;
  AC1's fixture README types no key unit 4 derives; every other claim held.

## 10. Reuse audit

The seams extended are `TOOL-dTotalRecall-4`'s `render_routes` in `tools/memory-tree/gen_build_index.py`
and `TOOL-dTotalRecall-18`'s `resolve_kind` (`tools/memory-tree/tree_lib.py#resolve_kind`), the one alias
reader, which this unit calls rather than re-spelling the alias; the census is an arm of
`tools/memory-tree/record_kinds.py#check_record_kinds` in the shape of `#check_pockets` and
`#check_serves_aliases`, reads through `#read_tracked`, and its plants join `#PLANTS`, `#build_fixture`
and `#run_selftest`. No existing census compares code against an alias table:
`python tools/codebase-map/reuse_lookup.py "census code lines comparing a retired alias token"` ranked
name-stem neighbours (`resolve_prefix_token`, `merge-rows.py`'s `census`, `practice_census.py`'s
`CensusRefused`), none of which reads code for a token's comparison; `TOOL-dTotalRecall-36`'s
`check_cause_writers` builds at order 17, after this unit.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
