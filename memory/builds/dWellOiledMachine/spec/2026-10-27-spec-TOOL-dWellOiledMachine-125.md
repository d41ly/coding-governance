# TOOL-dWellOiledMachine-125 — 97 AC1 runs 90 AC20's walk over the two files at their repository paths, as spec 121 has 108 S10 spell it

**Status:** DEFERRED · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 75 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-125-deviation-1251.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-125-deviation-1251.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-7 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md`),
finding 2, item H2, at HIGH. Item H2 carries finding 2 alone.

The bare-names defect is closed for 115 AC6 (TOOL-dWellOiledMachine-119), 115 AC7 and 108 AC10
(121 S4 and S10) and 90 AC20 (TOOL-dWellOiledMachine-120 S1), but not for 97 AC1. 121 S2 rewrites
97 AC1's expected output and leaves its files spelled "the supervisor and the door fixture,
`supervise.py` and `door_fixture.py`". Run from the repository root, the walk opens bare
`supervise.py`, raises `FileNotFoundError` and prints no count line, so 97 AC1 is red on a correct
build of units 92 and 97. This unit has 121's text for 115 S11 spell 97 AC1's files at their
repository paths, and has 121 AC1 read them.

## 2. Scope (IN)

- **S1** — 121 §4's text for 115 S11 extended. Spec 121 takes a rev bump, its §9 line naming this
  unit and finding 2, whose 115 S11 text's clause "and 97 AC1, whose 'it prints nothing' reads 'it
  prints exactly the line `subprocess calls <k>`'" reads "and 97 AC1, whose 'it prints nothing' reads
  'it prints exactly the line `subprocess calls <k>`' and whose files, 'the supervisor and the door
  fixture, `supervise.py` and `door_fixture.py`', read
  `'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'`". The paths are quoted for the
  reason TOOL-dWellOiledMachine-120 S1 gives. Observed by AC1, AC2.
- **S2** — 121 S2 gains, before "Observed by AC1", "With finding 2 of the round-7 promotions audit
  (H2), the same text spells 97 AC1's files at their repository paths, quoted, in place of the bare
  names." Observed by AC1.
- **S3** — 121 AC1 gains, before "Red when:", "; and `<AC1 of spec 97>` piped to
  `grep -c "door fixture, .supervise.py."` prints 0, and piped to
  `grep -o "'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'" | grep -c .` prints 2,
  once for the `git ls-files` liveness half 108 S8 writes and once for the walk's files". Its red
  case gains ", or 97 AC1 runs the walk over a bare name the root does not hold" before its full
  stop. Observed by AC1.
- **S4** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 121 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 121 makes are applied. At
  this unit's own pass, at order 75, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- 97 S1's population for 94 AC8, which 120 S6's text leaves unquoted: findings 4, 7 and 10,
  TOOL-dWellOiledMachine-126.
- 121 AC1's positive count token: finding 3, TOOL-dWellOiledMachine-126.
- No change to 120 S1's text: the walk's files for 97 AC1 belong beside its expected output, which
  121's 115 S11 text already sets.
- No spec-lint check that flags a walk run over a path with no `/`, and no checklist entry naming
  every consumer of a fixed defect. Those are the report's left-shift lines, separate mechanisms (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-121` — S2, §4's text for 115 S11 and AC1, which this unit extends before spec 121's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- 97 AC1 at HEAD 454dbf8d7 (spec 97 lines 243-246) runs its check "over the supervisor and the door
  fixture, `supervise.py` and `door_fixture.py`". Flattened, it counts `door fixture, .supervise.py.`
  once and the quoted pair 0 times.
- 108 S10 (spec 108 lines 76-83) has 97 AC1 run 90 AC20's walk and never spells its files; 108 S8
  (lines 71-73) writes the `git ls-files --error-unmatch` liveness half, which
  TOOL-dWellOiledMachine-120 S1 quotes. So after the cross-read the quoted pair occurs in 97 AC1 once
  through 108 S8 and, with this unit, once through the walk's files.
- TOOL-dWellOiledMachine-119 §4 Evidence records the walk run from the root over bare `supervise.py`
  raising `FileNotFoundError` with no count line.

### Why the count is 2

A count of 1 is met by the liveness half alone, which is how TOOL-dWellOiledMachine-120 AC2's quoted
pair count passes without the walk's files (the report's consequence). Requiring 2 makes the walk's
own files observable, and the bare-phrase count of 0 catches a text that kept the old spelling
beside the new.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-121.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 121's rev cell moves)

### Alternatives rejected

- **Extend 120's S6 text instead, as the report also allows.** 120's S6 text carries the liveness
  halves; 97 AC1's expected output is already set in 121's 115 S11 text, so its files belong in the
  same sentence and one spec spells the whole of 97 AC1's walk clause.
- **Match `walk[^.]*` before the pair, as the report's check does.** A text that puts the word
  `walk` before the liveness half satisfies it with no walk files; the count of 2 does not depend
  on word order.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — two greps.
- error / empty / loading states — a bare file name raises `FileNotFoundError` from the root and
  prints no count line, which reads red in 97 AC1; the pair count of 2 reads red before that.
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

- **AC1** — When `<§4 of spec 121>` is piped to `grep -c "whose files, .the supervisor and the door fixture"`,
  `<S2 of spec 121>` to `grep -c "finding 2 of the round-7 promotions audit"` and `<AC1 of spec 121>`
  to `grep -c "door fixture, .supervise.py."`, each prints 1.
  Red when: 121 leaves 97 AC1's files bare or AC1 does not read them.
- **AC2** — When `<AC1 of spec 97>` is piped to `grep -c "door fixture, .supervise.py."` at this
  unit's pass, after the cross-read, it prints 0, and to
  `grep -o "'tools/runtime/supervise.py' 'tools/memory-tree/door_fixture.py'" | grep -c .` it prints 2;
  and `git show 454dbf8d7:<spec 97>` sliced to AC1 the same way counts the bare phrase 1 and the pair 0.
  Red when: 97 AC1 still names a file by a bare name, or the pair occurs only in its liveness half.
- **AC3** — When `check_amended_before_built 121 125 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 121 lands after unit 90's build commit, the earliest build
  that spec 121's corrections reach through spec 115, as 121 AC14's first pair names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep, a history read or a history probe at this
unit's pass. Each path to the two unbuilt fixtures in this spec's criteria sits inside quotes.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-7 promotions, finding
  2 (H2).

## 10. Reuse audit

The seams reused are 121's own text for 115 S11, which already sets 97 AC1's expected output, the
quoted spelling TOOL-dWellOiledMachine-120 S1 gives the two paths, the `<X of spec N>` slice, and
TOOL-dWellOiledMachine-98's predicate over `build_commit` (`tools/unattended/lib-unattended.sh:1186`).
No new probe is minted.

Probe: `python tools/codebase-map/reuse_lookup.py "count a token only inside one code span of a spec section"`
ranked name-stem neighbours only (`counts`, `resolve_prefix_token`, `read_spec_revisions`), so no
existing seam fits beyond the slices named above. The recall query below ranked TOOL-dWellOiledMachine-120
and this finding's report among its first hits.

Recall terms used: `python tools/memory-recall/query.py "how does a spec criterion name an untracked
path without the spec token join reading it red" --terms "quoted pathspec untracked path spec tokens
criterion code span full path bare name error-unmatch"`
