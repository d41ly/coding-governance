# TOOL-dWitnessedBar-53 — every population an uncommitted scaffold seeds equals its seed after the first commit, held by a suite arm

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 11 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-52-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 to 51
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md`)
confirmed finding **id 13 at HIGH**, in its item **H1**, which it shares with id 1
(`TOOL-dWitnessedBar-52`). Id 13 grounds the defect in both readers: `TOOL-dWitnessedBar-46` S2 for the
seed, and `TOOL-dWitnessedBar-14` S11 with its table row ("live, over the tracked root confs") for the
leg. Built as written, every fresh adopter gets a false red on the shipped leg, and no criterion of
either unit can see it: unit 46's AC2 runs over a scaffold, and the hygiene suite's own scaffold arm
commits before it looks (`tools/memory-tree/check-memory-hygiene.test.sh:2425-2426`). Unit 52 changes
the read; this unit adds the artifact that proves it and keeps the class closed, the report's fix AC
and left-shift arm: a scaffold left uncommitted, seeded, committed and seeded again, for every
population it arms. It repairs `TOOL-dWitnessedBar-46`.

## 2. Scope (IN)

- **S1** — The seed-across-commit arm. `tools/memory-tree/check-memory-hygiene.test.sh` gains a scaffold
  made from `tools/memory-tree/.memory-tree.conf.example`, the conf copied and left untracked, on which
  `adopt-memory-tree.sh --scaffold` runs and nothing is committed. The arm lists the populations
  `python legacy_ledger.py seed --all` reports `present`, copies each home aside, runs
  `git add -A && git commit`, clears each home from the work tree, runs `seed --all` again, and asserts
  each home's key and count columns equal the copy's. Observed by AC1.
- **S2** — Never green over nothing. The arm fails when the listed population set is empty, since the
  example conf carries `ROW_DUPLICATE_PIN` and `conf-scalar-pins` must arm. Observed by AC1.
- **S3** — The leg across the commit. In the same scaffold, `python ratchet.py keys-not-scalar` exits 0
  before the commit and after it, naming the `ROW_DUPLICATE_PIN` row both times. Observed by AC2.
- **S4** — The floor follows the arm. The suite's `FLOOR_ASSERTIONS`, 668 at the base
  (`check-memory-hygiene.test.sh:4370`), rises by the assertions this arm adds, with a dated
  `RAISED <old> -> <new> by TOOL-dWitnessedBar-53` comment beside it, as the rows above it carry.
  Observed by AC3.

## 3. Non-goals (OUT)

- The conf read itself: `TOOL-dWitnessedBar-52`'s.
- The `--home` seeds of `adopt-codebase-map.sh` and `adopt-drift-audit.sh`: `TOOL-dWitnessedBar-47` S3
  runs each adopter on a fresh uncommitted target.
- A bug-class checklist entry under `memory/gotchas/`: the class is gated here, so BUILD-METHOD M8's
  fallback to a gotcha does not apply.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-52` — `root_confs`, the read whose behaviour across the first commit this arm observes; without it the arm reds
- **consumes-from** `TOOL-dWitnessedBar-46` — the memory-tree adopter's seed of `conf-scalar-pins`, the population the arm must find armed
- **consumes-from** `TOOL-dWitnessedBar-15` — `legacy_ledger.py seed --all` and its `present` line, which list the armed populations and re-seed them
- **consumes-from** `TOOL-dWitnessedBar-61` — the null SHA on an unborn HEAD, without which the arm's first `seed --all` before the commit cannot arm a population
- **hands-off** `TOOL-dWitnessedBar-62` — the seed-across-commit arm, which the minors batch builds into unit 46's scaffold arm, widens to every population the listing run arms and asserts the null SHA on (ids 2, 3, 18, 25, 36)

## 4. Design

### Evidence

- The suite's existing scaffold writes a stand-in conf and commits in the same subshell, before any
  assertion (`tools/memory-tree/check-memory-hygiene.test.sh:2421-2426`).
- `FLOOR_ASSERTIONS=668` and its `-ge` check (`check-memory-hygiene.test.sh:4370-4371`), with the dated
  `RAISED` comments above it.
- Unit 15 §4: `seed` over a present armed home prints `present <population>` and writes nothing; over an
  absent home it seeds.

### The arm

```
S = scratch git init; copy the kit; cp .memory-tree.conf.example S/.memory-tree.conf   (untracked)
adopt-memory-tree.sh --scaffold                     # seeds conf-scalar-pins (unit 46 S2)
P = populations `seed --all` prints `present` for   # S2: P empty -> FAIL
keys-not-scalar exits 0 naming ROW_DUPLICATE_PIN    # S3, before
save each home of P; git add -A && git commit
keys-not-scalar exits 0 naming ROW_DUPLICATE_PIN    # S3, after
remove each home of P; seed --all
for p in P: key and count columns of the new home == the saved home's     # S1
```

The SHA and disposition columns are dropped from the compare, because the re-seed stamps the new
commit.

### Inventory

Minted: nothing by name; one suite arm and its floor raise.

### Migration

None.

### Rollout

Live at landing. This unit shares order 11 with `TOOL-dWitnessedBar-52`, and its arm reads that unit's
output, so the main loop sequences it after unit 52 within the step (BUILD-METHOD M6, clause 2).

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`

### Alternatives rejected

- **Assert only `conf-scalar-pins`.** The next registration whose seed reads tracked files fails the
  same way and passes an instance arm; the arm derives its population.
- **Commit the scaffold before seeding.** It is the order a real adopter never runs
  (`tools/memory-tree/adopt-memory-tree.sh:694`).

## 5. Production-readiness checklist

- security — no new surface; a scratch target only.
- perf / scale — one scaffold, two seed runs and one commit, seconds.
- error / empty / loading states — an empty armed set fails the arm, never passes it.
- observability — the arm prints each population compared and its row count.
- risks — a registration whose seed is not deterministic across a commit reds the arm; that is the
  class it exists to name.
- testing — AC1 to AC3 by fixture; the arm of §7 at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When the arm's scaffold runs in a scratch target with nothing committed, `legacy_ledger.py
  seed --all` names `conf-scalar-pins` present, and after the commit and a re-seed each listed home's key
  and count columns equal the saved copy's.
  Red when: a seed reads tracked files only, so the home before the commit is empty and the re-seed is
  not; or the listed set is empty and the arm passes over nothing.
  fixture: a scratch `git init` target under `%TEMP%/<short-name>`, built by the suite.
- **AC2** — When `python ratchet.py keys-not-scalar` runs in that scaffold before the commit and after
  it, each run exits 0 and names the `ROW_DUPLICATE_PIN` row.
  Red when: the leg reds once the conf is committed.
- **AC3** — When `grep -n '^FLOOR_ASSERTIONS=' check-memory-hygiene.test.sh` runs in `tools/memory-tree/`,
  the value exceeds the pass's parent's by the arm's assertion count, and a `RAISED` comment names
  `TOOL-dWitnessedBar-53`.
  Red when: the arm can be deleted and the suite stays green.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC2 · the uncommitted example-conf scaffold seeded, committed and re-seeded, staged red by dropping `--others` from unit 52's `root_confs` · FLOOR_ASSERTIONS raised by the arm's assertions

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-46`'s clause. Unit 46 carries
  none, being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which artifact closes id 13, given unit 52 changes the read for both readers?** Options: (a) a
  suite arm over every population an uncommitted scaffold seeds, the report's fix AC and left-shift;
  (b) a second change to the leg's read alone; (c) a gotcha entry. (b) duplicates unit 52's one function
  and fails [one-fact]; (c) is M8's fallback for a class that cannot be gated, and this one can.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the option meeting the report's AC and gating
  the class. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 40 to 51, id 13
  (HIGH, item H1, shared with id 1).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the consumes-from bullet mirroring
  TOOL-dWitnessedBar-61's hands-off edge and the hands-off bullet mirroring TOOL-dWitnessedBar-62's
  consumes-from edge, promoted by the round-1 spec audit of units 52 to 57; nothing else moved.

## 10. Reuse audit

The seam is the suite's existing scaffold block (`tools/memory-tree/check-memory-hygiene.test.sh:2415-2426`)
and unit 15's `seed --all`, which already lists and re-seeds every registered population; the arm
composes the two with one commit between them. `python tools/codebase-map/reuse_lookup.py "an adopter
seed equal before and after the first commit"` ranked `before`, `seed`, `adopt` and `build_commit`,
each a test helper or a commit builder and none a compare across a first commit, so no existing seam
fits beyond the two named.

Recall terms used: `python tools/memory-recall/query.py "why does an adopter seed read the working tree at scaffold time" --terms "method-carriers seed git ls-files empty scaffold untracked conf vacuous-selector-empty-population adopter first commit"`
