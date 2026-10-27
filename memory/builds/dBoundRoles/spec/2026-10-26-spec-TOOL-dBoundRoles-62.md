# TOOL-dBoundRoles-62 — the spawn guard's suite carries the floor unit 60's AC15 checks, and AC15 refuses a suite with no floor and names its units suite by suite

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 34 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-61-round5-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-61-round5-fix-return.md) | research | TOOL-dBoundRoles-61 TOOL-dBoundRoles-63 |
| [2026-10-26-build-TOOL-dBoundRoles-62-deviation-621.md](../build/2026-10-26-build-TOOL-dBoundRoles-62-deviation-621.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-62-deviation-622.md](../build/2026-10-26-build-TOOL-dBoundRoles-62-deviation-622.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-61-round5-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-61-round5-fix-brief.md) | research | TOOL-dBoundRoles-61 TOOL-dBoundRoles-63 |
| [2026-10-26-review-TOOL-dBoundRoles-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-61-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-61 TOOL-dBoundRoles-63 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the promoted specs 59 and 60
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-59-spec-audit-round1.md`) confirmed
finding **id 21 at HIGH**, report item **H2**. No other id shares the item. Ids 2 and 10 raise the same
missing floor beside the base-term defect at MEDIUM, item M1, and are `TOOL-dBoundRoles-63`'s.

`TOOL-dBoundRoles-60` S24 and AC15 check "each suite's floor" over two suites. The spawn guard's suite
has none at base: `grep -c FLOOR_ASSERTIONS tools/hooks/agent-cap.test.sh` prints 0, and unit 25 moves
that file to `tools/roles/spawn-guard.test.sh`. Unit 58's arm line on it ends in `none`. Over a suite with
no `FLOOR_ASSERTIONS` line AC15 has nothing to sum, so it passes vacuously or errors, and it reports the
suite as covered. AC15 also never says which units must appear in which suite's terms.

This unit gives the spawn guard's suite a floor with a history, and restates unit 60's S24 and AC15 so
AC15 is red on a suite with no floor and names its units per suite. It repairs `TOOL-dBoundRoles-60` and
builds one step after it (order 34).

## 2. Scope (IN)

- **S1** — The floor. At this pass `tools/roles/spawn-guard.test.sh` holds four things: a count of the
  assertions it executes, one `FLOOR_ASSERTIONS=<n>` line, a comparison that fails naming the executed
  count and the floor when the count is below it, and the `PASS ($n assertions)` line that
  `tools/check-testsuite-counts.sh` reads. Where unit 43's pass left all four (43 S27, 43 AC27), this
  pass records that and keeps the value. Where any is missing, this pass adds it. Observed by AC1.
- **S2** — The floor's history. The comment above the line opens with a bare base term, then carries a
  `+<n> for <case> (TOOL-dBoundRoles-58)` term for the floored assertions unit 58's arms add, and
  `FLOOR_ASSERTIONS` equals the base plus the terms. The base is the value unit 43 pinned, or, where no
  floor was pinned, the count of the suite's other assertions. Both figures are DERIVED at this pass by
  reading each assertion call site from source, and the comment says so; the close's run of the suite is
  the executed observation (§7). Observed by AC2.
- **S3** — Unit 60's spec follows. The pass bumps `TOOL-dBoundRoles-60`'s spec before it edits the suite
  (BUILD-METHOD M2, READY). S24 names, per suite, the units whose `+<n>` terms its floor carries:
  units 52, 53, 58, 59 and 61 for `tools/roles/adopt-roles.test.sh`, and unit 58 for
  `tools/roles/spawn-guard.test.sh`, whose base term carries every earlier unit. AC15 checks each suite
  apart. It is red when a named suite holds no `^FLOOR_ASSERTIONS=[0-9]+$` line, naming the suite, and red
  when a unit that suite's list names appears in no `+<n>` term. Its §9 line names this unit, S24 and
  AC15, and unit 60's ledger answers AC15 `amended rev-<n>`, naming that revision. AC15's sum clause is
  unit 63's (ids 2, 10, 15 and 22), and this bump leaves its text as it stands. Observed by AC3.
- **S4** — Unit 58's arm line names its floor move. Spec 58's `New arm:` line on
  `tools/roles/spawn-guard.test.sh` names `FLOOR_ASSERTIONS` in its floor field, as 60 S24 requires. Where
  unit 60's pass left it ending in `none`, this pass makes that bump of spec 58, with a §9 line naming
  this unit and §7. Observed by AC4.

## 3. Non-goals (OUT)

- Ids 2, 10, 15 and 22: the base term in AC15's sum and §4 Evidence's figure, which `TOOL-dBoundRoles-63`
  restates.
- The report's left-shift gate, a check refusing a criterion that names a suite's `FLOOR_ASSERTIONS` where
  the suite carries none at the pinned base. No clause of this build names it; AC3 is the regression.
- Floors in any other suite, and the leg rename unit 25 owns.

### Edges

- **consumes-from** `TOOL-dBoundRoles-60` — S24, AC15 and its restatement of unit 58's arm line, which S3 restates per suite and S4 completes (id 21)
- **consumes-from** `TOOL-dBoundRoles-61` — the `+<n>` term naming unit 61 on the adopter suite's floor, which restated AC15 requires (ids 19 and 21)
- **hands-off** `TOOL-dBoundRoles-63` — the spawn guard's floor line and its base term, which unit 63's restated sum clause reads (ids 2, 10 and 21)
- **hands-off** `TOOL-dBoundRoles-64` — S1 to S3, §3, §4 Evidence, §5, §7, AC1 to AC3 and the spawn guard's floor, which unit 64 restates: the executed count, units 50, 60 and 61 named, the base kept as a term, the testsuite-counts leg, the edge to unit 58 and the comment shape (ids 1, 6, 7, 11, 12, 13, 16, 19, 20, 21, 27, 28, 31 and 32 of the round-1 audit of units 61 to 63)
- **hands-off** `TOOL-dBoundRoles-66` — the §5 risks line and the §7 spawn-guard `New arm:` line, which unit 66 restates: the overcount priced and the arm line naming unit 50's term and the executed count (ids 5 and 17 of the round-1 audit of unit 64)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `grep -c FLOOR_ASSERTIONS tools/hooks/agent-cap.test.sh` prints 0, while `tools/hooks/scratch-guard.test.sh`
  prints 3. The agent-cap suite counts `pass` and `fail` and ends `echo "---- $pass passed, $fail failed ----"`.
- `tools/hooks/scratch-guard.test.sh:1303-1321` is the house shape: a comment whose first line names the
  pin, a `<total> = <prior> + <added>` history whose later raises were counted by hand because a pass runs
  no suite (`:1314-1318`), `FLOOR_ASSERTIONS=309`, and `[ "$n" -ge "$FLOOR_ASSERTIONS" ]` failing with the
  executed count.
- `tools/check-testsuite-counts.sh:93-98` reads a pinned floor as `^FLOOR_ASSERTIONS=[0-9]+$`, refuses
  `0`, and requires the file to reference the variable; `:123-126` fails a floored suite that prints no
  `PASS ($n assertions)` line.
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-43.md` S27 has the pack's suite print
  `PASS (<n> assertions)` against a pinned `FLOOR_ASSERTIONS`, and its AC27 observes that line. Its
  spawn-guard arm line says only `FLOOR_ASSERTIONS` raised.
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-58.md`'s spawn-guard `New arm:` line ends
  in `none`.
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-60.md` S24 names the floor comment per
  unit for both suites; AC15 sums "the `+<n>` terms above each suite's `FLOOR_ASSERTIONS`" and names units
  52, 53 and 58 with no suite.

### Inventory

Minted: none. `FLOOR_ASSERTIONS` is the suites' existing convention; the executed counter takes whatever
name the suite's count line already uses.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 34, after unit 60 at order 33. No other unit holds order 34.

### Files touched (estimate)

- `tools/roles/spawn-guard.test.sh`
- the specs of TOOL-dBoundRoles-58 and TOOL-dBoundRoles-60, rev bumps (S3, S4), named here for the dispatch
  write set
- unit 60's acceptance ledger, the AMENDED answer of S3, named here for the dispatch write set

### Alternatives rejected

- **Drop the spawn guard's suite from S24 and say why.** It records the gap rather than closing it, and
  unit 58's arms would keep landing in a suite whose executed count nothing pins (§8 F2).
- **One unit list for both suites.** Units 52 and 53 add no arm to the spawn guard's suite, so a shared
  list is red on a correct tree.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one comparison at the suite's end.
- error / empty / loading states — a suite with no floor line reds restated AC15, naming the suite.
- observability — the comparison names the executed count and the floor; the comment names each unit's
  share.
- risks — a base read from source can overcount a skipped arm, which reds the suite at the close; the
  comparison's message names both figures, so the fix is one edit.
- testing — AC1 to AC4 by a scratch shell over the comparison line, a comment probe and spec extraction;
  the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `grep -cE '^FLOOR_ASSERTIONS=[0-9]+$'` runs over the spawn-guard suite unit 25 adds (its
  path in S1 and Files touched), it prints 1. A scratch shell then evaluates only the suite's floor line
  and comparison line, both copied out by `grep`, with the executed count set one below the floor: it
  prints the failure line naming both figures. With the count equal to the floor it prints nothing. No
  suite runs.
  Red when: the suite holds no floor, or the comparison cannot fail.
- **AC2** — When a `python -c` probe reads the comment block above `FLOOR_ASSERTIONS` in the spawn
  guard's suite, its first bare number plus every `+<n>` term equals the floor, and a
  `+<n>` term names `TOOL-dBoundRoles-58`.
  Red when: the floor carries no history, or unit 58's arms land and the floor stays put.
  figure: DERIVED from the file at observation time; no number is typed here.
- **AC3** — When a `python -c` probe extracts spec 60's S24 and AC15 bullets, each names both the roles
  adopter suite and the spawn guard's suite by path. AC15 names units 52, 53, 58, 59 and 61 for the first
  and unit 58 for the second, and states a red for a suite holding no
  `FLOOR_ASSERTIONS` line. Spec 60's §9 holds a line naming `TOOL-dBoundRoles-62`.
  Red when: AC15 can pass over a suite with no floor.
- **AC4** — When `grep -n '^New arm: .*spawn-guard'` runs over spec 58, it prints the arm line on the
  spawn-guard suite, and that line names `FLOOR_ASSERTIONS` after its last `·`.
  Red when: unit 58's arms land with a floor field of `none`.

## 7. Gates

`agent-cap self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`agent-cap self-test` stands for the spawn guard's suite; unit 25's pass renames it on every live §7
line when it renames the leg.

New arm: tools/roles/spawn-guard.test.sh · covers AC1 · the floor comparison, staged by a floor one above the executed count · `FLOOR_ASSERTIONS` kept or minted, its comment carrying the base and unit 58's term

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 60 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — A floor in the spawn guard's suite, or that suite dropped from S24 (id 21)?** Options: (a) S1's
  floor, kept from unit 43 or minted here; (b) S24 names one suite and says why. Both pass M3's vetoes:
  neither adds a dependency, a surface or a write path. (a) closes the gap and (b) records it. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 59 and 60, id 21
  (HIGH, item H2), on the report's fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-66, the minors batch of the round-1 audit of unit 64; nothing else moved.

## 10. Reuse audit

The seam is the suites' shrink-only `FLOOR_ASSERTIONS` convention, in the shape
`tools/hooks/scratch-guard.test.sh:1303-1321` carries and `tools/check-testsuite-counts.sh:93-126` reads,
extended to one more suite rather than re-invented.
`python tools/codebase-map/reuse_lookup.py "a suite pins a shrink-only floor on its executed assertion count"`
ranked `counts`, `measure_typed_counts`, `check_shrink_row` and `count_never_falls`, none a suite floor,
so no existing seam fits beyond that convention. The recall query's hits are `TOOL-aWokenSentinel-19`
and `TOOL-aWokenSentinel-21`, each declaring a shrink-only `FLOOR_ASSERTIONS` in a suite that had none,
the precedent S1 follows.

Recall terms used: `python tools/memory-recall/query.py "how does a suite floor its executed assertion count and comment each raise" --terms "FLOOR_ASSERTIONS floor shrink-only executed count assertions raise comment suite spawn-guard arm"`
