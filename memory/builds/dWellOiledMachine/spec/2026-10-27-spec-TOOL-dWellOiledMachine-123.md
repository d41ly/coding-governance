# TOOL-dWellOiledMachine-123 — spec 121's AC4 requires the absence checks S5 writes into spec 115, so deleting them can never turn AC4 green

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 75 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-123-deviation-1231.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-123-deviation-1231.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-7 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md`),
finding 9, item H1, at HIGH. Item H1 merges findings 1, 9 and 13, and each takes its own unit:
finding 1 is TOOL-dWellOiledMachine-122 and finding 13 is TOOL-dWellOiledMachine-124.

Finding 9 is the blast radius of 121 AC4. As written, the only way to green it is to delete the
three checks 121 S5 writes into spec 115 that require `not in ok` absent, which removes the guard
that the old exempting walk has not come back. Unit 122 makes AC4 passable. This unit closes the
deletion route: AC4 requires each of those three checks to be present, so deleting one reads red.

## 2. Scope (IN)

- **S1** — 121 AC4 gains the presence counts. Spec 121 takes a rev bump, its §9 line naming this
  unit and finding 9, whose AC4 gains, before its `fixture:` line, "; and `<S12 of spec 115>` piped
  to `grep -c "requires .not in ok. absent"`, and `<AC6 of spec 115>` and `<§4 of spec 115>` each
  piped to `grep -cF 'grep -c "not in ok"'`, each print 1". Observed by AC1, AC2.
- **S2** — 121 AC4's red case gains ", or an absence check S5 writes into spec 115 was deleted"
  before its full stop. Observed by AC1.
- **S3** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 121 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 121 makes are applied. At
  this unit's own pass, at order 75, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- AC4's count inside 115's walk: finding 1, TOOL-dWellOiledMachine-122.
- AC4's reading over spec 115 before the cross-read, and 121 §4's record of it: finding 13,
  TOOL-dWellOiledMachine-124.
- No change to the three absence checks themselves: 121 S5 and §4 spell them.
- No spec-lint check that flags an absence count over a whole spec. That is the report's left-shift
  line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-121` — AC4's presence counts and red case, which this unit adds before spec 121's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- 121 §4 sets three texts into spec 115 that carry `not in ok` as an absence check: 115 S12's last
  sentence ("requires `not in ok` absent", spec 121 line 158), the 115 AC6 clause (line 193) and
  115 §4's AC10 text (line 152). The last two carry the command `grep -c "not in ok"`.
- Re-run 2026-10-27 at HEAD 454dbf8d7: `<S12 of spec 115>` counts `requires .not in ok. absent` 0
  times, and `<AC6 of spec 115>` and `<§4 of spec 115>` count `grep -c "not in ok"` 0 times, so each
  presence count reads red before the cross-read and green only once 121 S5 has landed.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-121.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 121's rev cell moves)

### Alternatives rejected

- **A non-goal forbidding the deletion.** A non-goal binds the unit that states it, and the build
  run reads AC4 when it is red, not 121's non-goals.
- **Count `not in ok` over the whole of spec 115 and require exactly 3.** It reds on any later §9 line
  or note that quotes the string, which is the same unsatisfiable shape again.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — three greps.
- error / empty / loading states — an empty slice counts 0 and reads red, as a deletion does.
- observability — each count prints its number.
- risks — none beyond 121's own.
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

- **AC1** — When `<AC4 of spec 121>` is piped to `grep -cF "<S12 of spec 115>"`, to
  `grep -cF "<AC6 of spec 115>"` and to `grep -c "absence check S5 writes into spec 115 was deleted"`,
  each prints 1.
  Red when: AC4 still greens when an absence check is deleted.
- **AC2** — When `<S12 of spec 115>` is piped to `grep -c "requires .not in ok. absent"` at this
  unit's pass, after the cross-read, it prints 1, and `<AC6 of spec 115>` and `<§4 of spec 115>` each
  piped to `grep -cF 'grep -c "not in ok"'` print 1; and when `<S12 of spec 115>` is first piped
  through `sed 's/requires .not in ok. absent//'`, the same count prints 0.
  Red when: an absence check is missing from spec 115, or the staged deletion still counts it.
- **AC3** — When `check_amended_before_built 121 123 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 121 lands after unit 90's build commit, the earliest build
  that spec 121's corrections reach through spec 115, as 121 AC14's first pair names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep, a piped staged deletion or a history probe at
this unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-7 promotions, finding
  9 (H1).

## 10. Reuse audit

The seams reused are 121's own `<X of spec N>` and `<§K of spec N>` slices and
TOOL-dWellOiledMachine-98's predicate over `build_commit` (`tools/unattended/lib-unattended.sh:1186`).
The staged deletion is a pipe, so it mints no fixture.

Probe: `python tools/codebase-map/reuse_lookup.py "count a token only inside one code span of a spec section"`
ranked name-stem neighbours only (`counts`, `resolve_prefix_token`, `read_spec_revisions`); none reads
a spec's scope bullet for a criterion, so no existing seam fits beyond the slices named above. The
recall query below ranked this finding's own report among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how does an absence criterion over a whole
spec stay passable when the amendment writes the same token" --terms "absence count whole spec
amendment text token code span walk exemption not in ok criterion unsatisfiable"`
