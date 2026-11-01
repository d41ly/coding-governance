# TOOL-dWellOiledMachine-122 — spec 121's AC4 counts `not in ok` inside spec 115's walk alone, so the absence checks S5 writes elsewhere in 115 no longer read red

**Status:** DEFERRED · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 75 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-122-deviation-1221.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-122-deviation-1221.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-7 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md`),
finding 1, item H1, at HIGH. Item H1 merges findings 1, 9 and 13, and each takes its own unit:
finding 9 is TOOL-dWellOiledMachine-123 and finding 13 is TOOL-dWellOiledMachine-124.

121 AC4 requires `grep -c "not in ok"` to print 0 over the whole of spec 115. But 121 S5 writes that
string into spec 115 three times as absence checks: 115 S12's last sentence, the 115 AC6 clause and
115 §4's AC10 text. On a correct build AC4 counts 3 or more and reads red. This unit scopes AC4's
spec-115 half to the one place the old exemption lived, the walk's code span in 115 §4, and pairs it
with a count that shows the cut found the walk.

## 2. Scope (IN)

- **S1** — 121 AC4's spec-115 clause rewritten. Spec 121 takes a rev bump, its §9 line naming this
  unit and finding 1, whose AC4 clause "`grep -c "not in ok"` prints 0 over `<spec 90>` and over
  `<spec 115>`" reads "`grep -c "not in ok"` prints 0 over `<spec 90>`; `<§4 of spec 115>` piped to
  `grep -o 'python -c "[^"]*"'`, which cuts it to its walk, then to `grep -c "not in ok"` prints 0
  and to `grep -c "subprocess calls"` prints 1". AC4's red case gains ", or spec 115's walk keeps
  the `ok` exemption" before its full stop. Observed by AC1, AC2.
- **S2** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 121 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 121 makes are applied. At
  this unit's own pass, at order 75, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- AC4's positive counts of S5's absence checks: finding 9, TOOL-dWellOiledMachine-123.
- AC4's reading over spec 115 as it stood before the cross-read, and 121 §4's record of it:
  finding 13, TOOL-dWellOiledMachine-124.
- AC4's `<spec 90>` half, which the report keeps as it is.
- No spec-lint check that flags an absence count over a whole spec whose own amendment writes the
  token. That is the report's left-shift line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-121` — AC4's spec-115 clause and red case, which this unit rewrites before spec 121's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- Re-run 2026-10-27 at HEAD 454dbf8d7: `grep -c "not in ok"` over spec 115 prints 5; spec 121 writes
  the string at its lines 152, 158 and 193, each a text it sets into spec 115.
- 115 §4, sliced and flattened as 121's §6 preamble defines `<§4 of spec N>`, holds one
  `python -c "` code span, its walk. Cut with `grep -o 'python -c "[^"]*"'`, it counts `not in ok`
  once and `subprocess calls` once today. A scratch copy of spec 115 whose walk line is 121 §4's
  walk counts them 0 and 1.
- The walk's code holds no double quote: its Python strings are single-quoted, so the cut ends at
  the walk's closing quote.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-121.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 121's rev cell moves)

### Alternatives rejected

- **Count a token only the old walk carries, such as `ok={id(x)`.** It passes over a walk that
  spells the exemption another way; the cut reads the walk whatever it is spelled.
- **Drop the spec-115 half.** 121 S5 removes the exemption from 115's walk, and nothing else would
  observe that it is gone from 115.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — one slice and three greps.
- error / empty / loading states — a cut that finds no walk counts `subprocess calls` 0 and reads red,
  so an empty cut never passes as an absence.
- observability — each count prints its number.
- risks — a second `python -c "` span added to 115 §4 is cut too and counted with the walk, which
  can only make the absence stricter.
- testing — AC1 to AC3.
- migration — none.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

`<spec N>` is `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-N.md`,
`<X of spec N>` is the bullet labelled X of that spec, from its label to the next column-0 `- **`
label or heading, flattened with `tr -s '\n ' ' '`, and `<§K of spec N>` is
`awk '/^## K\./{p=1;next} /^## [0-9]+\./{p=0} p' <spec N> | tr -s '\n ' ' '` for section number K.
Each command runs from the repository root; the predicate is loaded as TOOL-dWellOiledMachine-98 §6
states.

- **AC1** — When `<AC4 of spec 121>` is piped to `grep -cF "grep -o 'python -c"` and to
  `grep -c "keeps the .ok. exemption"`, each prints 1, and piped to
  `grep -c "over .<spec 90>. and over .<spec 115>."` it prints 0.
  Red when: AC4 still counts `not in ok` over the whole of spec 115.
- **AC2** — When `<§4 of spec 115>` is piped to `grep -o 'python -c "[^"]*"'` at this unit's pass,
  after the cross-read, and then to `grep -c "not in ok"`, it prints 0, and to
  `grep -c "subprocess calls"` it prints 1; and `grep -c "not in ok" <spec 115>` prints 3 or more.
  Red when: 115's walk keeps the exemption, the cut finds no walk, or the whole file no longer
  carries the absence checks a whole-file count would trip on.
- **AC3** — When `check_amended_before_built 121 122 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 121 lands after unit 90's build commit, the earliest build
  that spec 121's corrections reach through spec 115, as 121 AC14's first pair names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep or a history probe at this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-7 promotions, finding
  1 (H1).

## 10. Reuse audit

The seams reused are 121's own `<§K of spec N>` slice, the `grep -o 'python -c "[^"]*"'` cut 121's
§6 preamble already applies to 90 AC20 as `<walk>`, and TOOL-dWellOiledMachine-98's predicate over
`build_commit` (`tools/unattended/lib-unattended.sh:1186`). No new probe is minted.

Probe: `python tools/codebase-map/reuse_lookup.py "count a token only inside one code span of a spec section"`
ranked name-stem neighbours only (`counts`, `resolve_prefix_token`, `read_spec_revisions`); none cuts
a code span out of a spec section, so no existing seam fits beyond the cut named above. The recall
query below ranked this finding's own report and an earlier audit's "green before the amendment"
finding among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how does an absence criterion over a whole
spec stay passable when the amendment writes the same token" --terms "absence count whole spec
amendment text token code span walk exemption not in ok criterion unsatisfiable"`
