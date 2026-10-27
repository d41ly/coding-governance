# TOOL-dWellOiledMachine-124 — spec 121's AC4 is observed both ways: its walk count reads red over spec 115 before the cross-read and green after, and §4 records both readings

**Status:** DEFERRED · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 75 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-124-deviation-1241.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-124-deviation-1241.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-7 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-116-spec-audit.md`),
finding 13, item H1, at HIGH. Item H1 merges findings 1, 9 and 13, and each takes its own unit:
finding 1 is TOOL-dWellOiledMachine-122 and finding 9 is TOOL-dWellOiledMachine-123.

Finding 13 is the failure envelope of 121 AC4: a criterion no correct build can pass, written with no
reading that showed it could pass. The report's fix asks for that reading: apply S5's texts to a
copy of spec 115 and run AC4 over it. This unit makes the reading part of AC4 and of 121's §4. AC4
counts `not in ok` inside the walk of spec 115 as committed at 454dbf8d7, which still carries the
exemption, and requires 1, so the clause is seen to fail on the old walk. 121 §4 Evidence records
that reading beside the one over a copy with 121's walk applied, so the count is shown to separate
the two walks.

## 2. Scope (IN)

- **S1** — 121 AC4 gains the reading over the old walk. Spec 121 takes a rev bump, its §9 line naming
  this unit and finding 13, whose AC4 gains, before its `fixture:` line, "; and
  `git show 454dbf8d7:<spec 115> | awk '/^## 4\./{p=1;next} /^## [0-9]+\./{p=0} p' | tr -s '\n ' ' ' | grep -o 'python -c "[^"]*"' | grep -c "not in ok"`
  prints 1". Its red case gains ", or the count inside spec 115's walk reads 0 over the walk that
  still carries the exemption" before its full stop. The code span stays on one line. Observed by
  AC1, AC2.
- **S2** — 121 §4 Evidence gains the line "At 454dbf8d7 spec 115 counts `not in ok` 5 times over the
  whole file and once inside its §4 walk. A scratch copy with this spec's walk in place of 115's
  counts it 0 times inside the walk, and S5's texts add it at least 3 times outside the walk, so only
  the count inside the walk separates the old walk from the new (round-7 promotions audit, finding
  13)." Observed by AC1.
- **S3** — The route. The rev bump is made at BUILD-METHOD M2's cross-read, before the first code
  pass, in a spec pass whose commit touches spec 121 and whose subject names this unit and none of
  TOOL-dWellOiledMachine-90 to -94. It lands before the amendments spec 121 makes are applied. At
  this unit's own pass, at order 75, nothing is written: the pass runs AC1 to AC3 and records them.
  Observed by AC3.

## 3. Non-goals (OUT)

- AC4's count over the live spec 115: finding 1, TOOL-dWellOiledMachine-122.
- AC4's presence counts of S5's absence checks: finding 9, TOOL-dWellOiledMachine-123.
- No new fixture file: the old walk is read from history, and the applied copy is S2's recorded
  reading.
- No checklist entry that runs every spec-text criterion over its base. That is the report's
  left-shift line, a separate mechanism (M2).

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-121` — AC4's reading over the old walk, its red case and §4 Evidence, which this unit adds before spec 121's amendments land
- **consumes-from** `TOOL-dWellOiledMachine-98` — the ordering predicate AC3 loads from spec 95 and calls

## 4. Design

### Evidence

- Re-run 2026-10-27 at HEAD 454dbf8d7: `grep -c "not in ok"` over spec 115 prints 5. Its §4,
  sliced and flattened, holds one `python -c "` span; cut with `grep -o 'python -c "[^"]*"'`, it
  counts `not in ok` once.
- A scratch copy of spec 115 whose walk line (line 192) was replaced by 121 §4's walk counted
  `not in ok` 0 times inside the cut and `subprocess calls` once.
- 454dbf8d7 is this build's commit of the round-7 promotions, on the run branch; spec 115 at that
  commit is the text the cross-read amends.

### Why history and not a scratch copy

The red half needs a spec 115 that still carries the exempting walk. After the cross-read the live
spec does not, and 454dbf8d7 does, so `git show` reads it with no file written and nothing to clean
up. The green half is the live spec, which TOOL-dWellOiledMachine-122's clause reads.

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-121.md` (the rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 121's rev cell moves)

### Alternatives rejected

- **A scratch copy of spec 115 with the old walk pasted back.** It needs the old walk spelled a
  second time in 121, and history already holds it.
- **Record the reading in §4 only.** A recorded reading is not re-run, so AC4 could drift from it;
  the clause re-observes the red case at every run of AC4.

## 5. Production-readiness checklist

- security — N/A — spec text changes.
- perf / scale — N/A — one `git show` and three greps.
- error / empty / loading states — a missing commit makes `git show` fail, the pipe counts 0 and the
  clause reads red.
- observability — the count prints its number.
- risks — the clause depends on 454dbf8d7 staying reachable, which holds while the run branch or
  its landing keeps it in history.
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

- **AC1** — When `<AC4 of spec 121>` is piped to `grep -c "git show 454dbf8d7"` and to
  `grep -c "still carries the exemption"`, each prints 1, and `<§4 of spec 121>` piped to
  `grep -c "only the count inside the walk separates"` prints 1.
  Red when: AC4 carries no reading that can fail, or 121's §4 does not record the two readings.
- **AC2** — When
  `git show 454dbf8d7:<spec 115> | awk '/^## 4\./{p=1;next} /^## [0-9]+\./{p=0} p' | tr -s '\n ' ' ' | grep -o 'python -c "[^"]*"' | grep -c "not in ok"`
  runs at this unit's pass, it prints 1, and the same pipe over `<spec 115>` as it stands after the
  cross-read prints 0.
  Red when: the old walk reads no exemption, or the live walk still carries one.
- **AC3** — When `check_amended_before_built 121 124 90` runs at this unit's pass, it exits 0.
  Red when: this unit's rev bump of spec 121 lands after unit 90's build commit, the earliest build
  that spec 121's corrections reach through spec 115, as 121 AC14's first pair names.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added or moved: each criterion is a grep, a history read or a history probe at this
unit's pass.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-7 promotions, finding
  13 (H1).

## 10. Reuse audit

The seams reused are 121's own `<§K of spec N>` slice, the `grep -o 'python -c "[^"]*"'` cut its §6
preamble applies as `<walk>`, `git show` at a pinned commit as TOOL-dWellOiledMachine-120 AC1 already
reads spec 115, and TOOL-dWellOiledMachine-98's predicate over `build_commit`
(`tools/unattended/lib-unattended.sh:1186`). No fixture or probe is minted.

Probe: `python tools/codebase-map/reuse_lookup.py "count a token only inside one code span of a spec section"`
ranked name-stem neighbours only (`counts`, `resolve_prefix_token`, `read_spec_revisions`), so no
existing seam fits beyond the idioms named above. The recall query below ranked this finding's report,
whose fix names the scratch-copy reading, and an earlier audit's entry asking every spec-text
criterion to print its red value at base.

Recall terms used: `python tools/memory-recall/query.py "how does an absence criterion over a whole
spec stay passable when the amendment writes the same token" --terms "absence count whole spec
amendment text token code span walk exemption not in ok criterion unsatisfiable"`
