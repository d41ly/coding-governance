# TOOL-dLinkedLibrary-43 — the region census stated exactly, its exclusions written as rules, and the two parsers it missed re-pointed

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 3 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 |
| [2026-10-26-build-TOOL-dLinkedLibrary-43-deviation-431.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-43-deviation-431.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 20 at HIGH**, report item **R7**. No other id shares the item; id 30 (item R9, govkit's
`find_block`) is `TOOL-dLinkedLibrary-45`'s.

`TOOL-dLinkedLibrary-18` §4 "The population" pins two queries and an 18-row table. Run at HEAD, the
queries return sites outside the table and miss `tools/hooks/format-guard.js`, whose `const FENCE_OPEN =`
the leading `^[A-Z_]*` cannot match. Two of the extra hits are region parsers: `tools/check-microformats.sh`
slices its block with awk `$0 == o`, and the run-gates suite slices the `mempause_sh` block. So that
unit's AC8, `0 site(s) outside the factory`, cannot be reached, and the standing census arm either stays
red or is narrowed by ad hoc exclusions while real parsers stay outside the factory.

This unit states the census predicate exactly, widens it to indented JavaScript constants, writes each
exclusion as a rule the census prints rather than hides, and re-points the two parsers it missed. It
repairs `TOOL-dLinkedLibrary-18` and builds one step after it (order 3).

## 2. Scope (IN)

- **S1** — The predicate. `region.py --census` (`TOOL-dLinkedLibrary-18` S7) reads three arms over tracked
  files under `tools/` and `skills/`: a marker CONSTANT, a line matching
  `^\s*((const|let|var)\s+)?[A-Z_]*(OPEN|CLOSE|BEGIN|END|MARK)[A-Z_]*(, [A-Z_]+)?\s*=\s*['"](<!--|#)`; an
  awk or shell MARKER TEST, `index(ln, o) == 1`, `$0 == <var>` inside an awk range or flag program, or a
  `/^# >>> <stem>/,/^# <<< <stem>/` range; and a `GEN_REGION_AWK=` assignment or a `>>> ` opener read
  by a regex. A hit inside `tools/lib/region.*` or inside a `region_py`, `region_sh`, `gen_region_awk` or
  `region_js` block is the factory. Observed by AC1, AC2 and AC3.
- **S2** — The exclusions, each a rule the census applies to a hit and prints as `excluded <rule> —
  <path>:<line>`, counted beside the site count and never in it: X1, a constant its module writes and
  never locates in a text; X2, a `## ` heading constant; X3, a comment line; X4, a copy discovery, a `git
  grep -l` or `grep -c` over a block opener that lists or counts files and slices nothing; X5, a
  single-line find, one line located by equality with no second marker in its program, so no region
  is read; X6, a suite scan that
  skips the lines of a `PARITY_ROWS` block to grade the rest, the block's bytes graded by its parity row.
  Observed by AC1 and AC4.
- **S3** — The parsers re-pointed. `tools/check-microformats.sh` sources `tools/lib/region.sh` (it is a
  gov-internal tool at the tool root) and reads its block with `region`, its exactly-one-pair check
  kept; the `mempause_sh` slice of `tools/run-gates/run-gates.test.sh` (:3600) reads the block with
  `region_nth` from `tools/lib/region.sh`. Observed by AC5.
- **S4** — The table at the pass. The census's own output at this pass's tip is the population: §4's
  reading at HEAD `823440497` names every hit and its disposition, and `TOOL-dLinkedLibrary-18`'s
  acceptance ledger answers its AC8 citing this unit. Observed by AC1.

## 3. Non-goals (OUT)

- govkit's `find_block` and `write_block`, which take synthesized markers no constant names:
  `TOOL-dLinkedLibrary-45`'s behavioural arm and re-point (id 30).
- The factory's contract, its twins and the parity rows: `TOOL-dLinkedLibrary-18`'s.
- Re-pointing an excluded site: a rule's population is printed so the next reader can contest it.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-18` — `region.py --census`, the factory and `region_nth`, whose predicate S1 states and whose population S3 completes (id 20)
- **hands-off** `TOOL-dLinkedLibrary-54` — S3's re-point of `tools/check-microformats.sh`, which unit 54 makes carry the `region_sh` block inline (id 3 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-56` — S3's re-point of the `mempause_sh` slice, which unit 56 makes read through an inline `region_nth` block (id 17 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-64` — `region.py --census` and the §4 table, whose arm names and ledger reconciliation unit 64 completes (ids 10, 13 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

Read at HEAD `823440497` with the two queries of `TOOL-dLinkedLibrary-18` §4 and S1's awk arm, 7 hits of
`git grep -nE '\$0 ?== ?[a-zA-Z_]+[ ;{)]'`, every hit opened at its line. PINNED at that commit; the
census of S1 re-derives it.

| Hit | Disposition |
|---|---|
| `tools/check-microformats.sh:28-29` and its awk at :49 | a site: S3 |
| `tools/run-gates/run-gates.test.sh:3600` | a site: S3 |
| `tools/hooks/format-guard.js:95-96`, missed by `^[A-Z_]*` | the table's `format-guard.js` row, now found |
| `tools/memory-tree/gen_build_index.py:91-174`, `tools/playbook/render_playbook.py:121-128`, `tools/roles/check_roles.py:114`, `tools/roles/roles_lib.py:60`, :88, `tools/runlog/prose.py:25-26`, `tools/unattended/unattended.sh:1279-1299` | constants of table rows |
| `tools/memory-tree/gotchas.py:61` | X1: written at :463 and :481, never located |
| `tools/workflows/review_replay.py:64` | X2 |
| `tools/lib/pyrun.sh:15` | X3 |
| `tools/lib/resolve-python.test.sh:226`, :232, :550; `tools/memory-tree/merge-rows.test.sh:396`; `tools/unattended/unattended.test.sh:3220` | X4 |
| `tools/unattended/check-unattended.test.sh:3705` and its uses at :567, :578, :3754, :3784, :3815; `tools/unattended/unattended.sh:9108` | X5 |
| `tools/lib/resolve-python.test.sh:600`, :678; `tools/unattended/unattended.test.sh:3221` | X6 |

### Why rules and not a path list

A path list exempts a line and keeps exempting whatever moves onto it; a rule exempts a SHAPE, so a new
hit is graded by what it does. Every excluded hit is printed, so an exemption is never read as coverage.

### Files touched (estimate)

- `tools/lib/region.py`: S1, S2
- `tools/lib/resolve-python.test.sh`: the census arm's plants
- `tools/check-microformats.sh`: S3
- `tools/run-gates/run-gates.test.sh`: S3

### Alternatives rejected

- **Re-pointing every X4 and X6 hit.** A discovery grep slices no text, and a parity-block skip reads the
  complement of a block whose bytes are already graded identical; re-pointing them adds sources of
  `tools/lib/region.sh` to suites the unattended waiver leaves unobserved for this landing.
- **Exempting by path.** §4 "Why rules and not a path list".

## 5. Production-readiness checklist

- security — read-only census; the two re-points read as before and refuse a malformed pair.
- perf / scale — one pass over the tracked tree, as `TOOL-dLinkedLibrary-18` S7.
- error / empty / loading states — a census over no hit prints `0 site(s)` and its exclusion counts.
- observability — each site, each exclusion and its rule printed.
- risks — a rule too wide hides a parser; AC4 plants one shaped like each rule that does slice.
- testing — the census plants in the parity suite.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python region.py --census` runs from `tools/lib` at this pass's tip, it prints
  `region census — 0 site(s) outside the factory` and one `excluded X<n>` line per excluded hit of §4,
  with a count per rule, and exits 0.
  Red when: a site of §4 is left outside, or an exclusion is applied without its line.
  figure: DERIVED at the pass by the census; §4's reading gives 18 excluded hits at `823440497`.
- **AC2** — When a scratch copy of the tree gains a tool module holding an indented
  `const FOO_OPEN = '<!-- foo -->'` and `lines.indexOf(FOO_OPEN)`, `python region.py --census` exits 1 naming that line.
  Red when: an indented JavaScript constant is missed.
- **AC3** — When a scratch tool script gains `awk -v o="$OPEN" '$0 == o {f=1; next} f' "$F"` or an awk
  range `/^# >>> foo/,/^# <<< foo/`, the census exits 1 naming each.
  Red when: an awk region read outside the factory passes.
- **AC4** — When the planted script of AC3 carries its range inside a `git grep -l` line's neighbour, a
  comment above it, and a heading constant beside it, the census still names the range and excludes
  only the three neighbours.
  Red when: a rule excludes a line that slices a region.
- **AC5** — When `grep -n "region.sh" tools/check-microformats.sh` and
  `grep -n "region_nth" tools/run-gates/run-gates.test.sh` run, each prints the re-pointed read, and the
  microformats check exits as it did at base over the charter.
  Red when: either parser keeps its own slice.

## 7. Gates

`micro-format definitions` · `micro-format gate selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates canary` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/resolve-python.test.sh · covers AC2 AC3 AC4 · the census plants, the failing case staged by the rev-1 constant query and by an X4 rule matching any line near a grep · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 18 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 20
  (HIGH, item R7).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-54, TOOL-dLinkedLibrary-56, TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-18`'s census in `tools/lib/region.py` and its arm in the
parity suite; the two re-points call the factory's shell twin. `python tools/codebase-map/reuse_lookup.py
"census of region parsers outside a factory"` ranked `parse`, `parse_args`, `census` (`merge-rows.py`,
a row census) and `parse_conf`, none a region census, so no existing seam fits beyond the one being
repaired.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
