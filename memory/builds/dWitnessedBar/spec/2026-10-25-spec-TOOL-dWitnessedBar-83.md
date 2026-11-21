# TOOL-dWitnessedBar-83 — the gov canary's floor is owned by the last unit that adds an arm, derived from the specs, and its equality with the executed count is held at the close

**Status:** INPROGRESS · rev-3 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 43 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-83-deviation-831.md](../build/2026-10-25-build-TOOL-dWitnessedBar-83-deviation-831.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-83-round9-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-83-round9-fix-return.md) | research | TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-83-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-83-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-83-round9-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-83-round9-fix-brief.md) | research | TOOL-dWitnessedBar-84 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-83-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-83-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-83-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-83-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-83-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-83-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-84 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 74 to 78
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md`)
confirmed finding **id 14 at HIGH**, report item **H2**. Id 2 shares that item and takes
`TOOL-dWitnessedBar-82`.

`TOOL-dWitnessedBar-73` S15 stated `FLOOR_ASSERTIONS=72` at unit 73's pass, `71f212ad1`, and its
rev-5 AC15 holds the `PASS (<n> assertions)` equality in a scratch clone at that pass commit, naming
this unit for the close's. Units built after `TOOL-dWitnessedBar-73` add executed assertions:
`TOOL-dWitnessedBar-78` (`253e21771`) added two, and `TOOL-dWitnessedBar-82` (`47ab62ebf`) restated
the floor at 74 (`2026-11-19-build-TOOL-dWitnessedBar-82-1-builder-return`). Units 84, 85, 88, 89 and
90 declare gov-canary arms after that, and each restates the floor for its own (`TOOL-dWitnessedBar-84`
S14, `TOOL-dWitnessedBar-85` S2, `TOOL-dWitnessedBar-88` S7, `TOOL-dWitnessedBar-89` S10,
`TOOL-dWitnessedBar-90` S11). The finding was that no unit was assigned to answer AC15 against the
final floor. The report's left-shift names the rule that was missing: the last unit in the build that
adds assertions owns the restatement.

This unit makes that owner a derived fact rather than a sentence each spec repeats. The owner is the
unit, among those whose §7 declares a gov-canary New arm, that the dispatcher builds last. At the close
the floor's comment must name it, and the executed count must equal the floor. Unit 73 AC15's close
clause is answered by that observation. It repairs `TOOL-dWitnessedBar-78`, builds one step after it,
after `TOOL-dWitnessedBar-82` within order 43, and closes that order alone.

## 2. Scope (IN)

- **S1** — The owner, derived. The floor's owner is the spec under `memory/builds/dWitnessedBar/spec/`
  that carries a line opening `New arm: tools/run-gates/run-gates.gov.test.sh` and sorts last by its
  status header's `order`, then by id string, the order
  `tools/workflows/unattended-build.js@8519d2244:692-697` sorts its roster in. At the close the one
  comment line directly above `FLOOR_ASSERTIONS=` in `tools/run-gates/run-gates.gov.test.sh` names
  that unit's id (§8 F3). Observed by AC1.
- **S2** — The close's equality. At the close the arm's `PASS (<n> assertions)` count over the built
  tree equals `FLOOR_ASSERTIONS`. This unit's acceptance ledger records both numbers and the owner S1
  derived, on the one line of that ledger carrying the string `AC2`. Observed by AC2.
- **S3** — Unit 73 AC15 answered. This unit's builder appends to the existing AC15 line of
  `2026-11-19-build-TOOL-dWitnessedBar-73-1-acceptance-ledger` a clause naming `TOOL-dWitnessedBar-83`
  AC2 as the close's equality, since the units after unit 73 in S1's list add arms after its pass.
  At the close the main loop writes, on that same line, the `PASS` count unit 73 AC15 owes from a
  scratch clone at `71f212ad1`, beside the floor that line already records, so the line holds both
  numbers and the name. Observed by AC3.

## 3. Non-goals (OUT)

- The restatement after unit 78, which is `TOOL-dWitnessedBar-82`'s for id 2, and each restatement
  for the arms a later unit adds, which is that unit's: `TOOL-dWitnessedBar-84`, `-85`, `-88`, `-89`
  and `-90`.
- Unit 28's arm. `TOOL-dWitnessedBar-28` declares a gov-canary New arm at order 30 and is not built:
  it waits on three dOrderedCharter changes (asks `TOOL-dWitnessedBar-101` to `-103`), and this run
  defers it. S1's list carries its spec, which does not sort last, and its floor restatement waits
  with `TOOL-dWitnessedBar-28`.
- A gate that reads the owner on every bar. The derivation reads spec files, which the suite does not
  read; it is a close-time observation, and the floor check
  (`tools/run-gates/run-gates.gov.test.sh@8519d2244:1269`) is the per-run gate.
- Rewording unit 73 AC15. It is answered in unit 73's ledger by name, as `TOOL-dWitnessedBar-78` §3
  answers units 68 to 73.
- The report's left-shift text as a spec lint over New-arm lines. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-73` — S15's floor and AC15's equality, which S3 answers at unit 73's pass and S2 holds at the close (id 14)
- **consumes-from** `TOOL-dWitnessedBar-82` — the restated floor and its comment, which S1 checks against the derived owner (ids 14 and 2)
- **hands-off** `TOOL-dWitnessedBar-84` — a later restatement, whose comment S1 holds against the derived owner at the close, which names the last unit that adds a gov-canary arm (ids 14 and 21)
- **hands-off** `TOOL-dWitnessedBar-88` — S1's owner, AC1's pipeline and comment read, and S3's pass-commit record, which unit 88 derives through the shipped readers, reads with `grep -B1` and locates by `build_commit` (ids 6, 9, 10 and 22 of the round-1 spec audit of units 79 to 84)

## 4. Design

### Evidence

- `spec/2026-10-25-spec-TOOL-dWitnessedBar-73.md` S15 states the floor at its own pass, and rev-5
  AC15 requires the `PASS` count in a scratch clone at that pass commit to equal it. Its ledger's
  AC15 line records `FLOOR_ASSERTIONS=72`, names `TOOL-dWitnessedBar-73`, and leaves the `PASS`
  equality OWED to the main loop at the close (`2026-11-19-build-TOOL-dWitnessedBar-73-1-acceptance-ledger`).
  That ledger has one line carrying the string `AC15` (PINNED 2026-11-21 by `grep -c 'AC15'`).
- `tools/run-gates/run-gates.gov.test.sh@8519d2244:1269` fails only when `a` is below the floor, so
  assertions added after a restatement pass silently.
- `TOOL-dWitnessedBar-82` S1 put its `RAISED 72 -> 74` comment on the line directly below the bare
  `FLOOR_ASSERTIONS=74` (`tools/run-gates/run-gates.gov.test.sh@8519d2244:246-247`). The line above
  it is the `TOOL-aShardedFloor-2` comment (`@8519d2244:245`), so at HEAD `grep -B1` reads no owner.
  The later units name the side: `TOOL-dWitnessedBar-88` S7 and `TOOL-dWitnessedBar-90` S11 put the
  owner line directly above the constant, and 85, 88, 89 and 90 read it with `grep -B1 | head -1`.
- The derivation of S1 over this build's specs lists 28 specs (PINNED 2026-11-21 by AC1's pipeline),
  from `TOOL-dWitnessedBar-12` at order 5 to `TOOL-dWitnessedBar-90` at order 47, and names
  `TOOL-dWitnessedBar-90` as the owner (PINNED 2026-11-21 by AC1's pipeline). It listed 20 specs ending at unit 78 on 2026-10-25 (PINNED then). Of the 28,
  22 are CLOSED and 6 DEFERRED: units 28, 84, 85, 88, 89 and 90 (PINNED 2026-11-21 by each status
  header). Specs 83 and 92 mention the New-arm line in prose only, at no line start, and sit outside
  the population (PINNED 2026-11-21: `TOOL-dWitnessedBar-83` S1, `TOOL-dWitnessedBar-92` §4).
- `tools/workflows/unattended-build.js@8519d2244:692-697` sorts by `order`, then by `String(id)`. A
  sort of spec paths by string after the order keeps the same tie order, because each path ends in the
  id followed by `.md`.

### Inventory

Minted: nothing in code. The ledger records of S2 and S3. No function, constant, plant, flag or file.
Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

The pass takes order 43 after `TOOL-dWitnessedBar-82` (`47ab62ebf`) and builds alone. It writes S3's
clause and this unit's ledger, with the AC1 to AC3 observations OWED to the main loop. Those are made
at the close, after every unit this run builds is terminal, which is after `TOOL-dWitnessedBar-90` at
order 47, the owner S1 names today. `TOOL-dWitnessedBar-28` is deferred by the run and is not waited on.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-73-1-acceptance-ledger.md`:
  S3's clause, appended to its AC15 line.
- This unit's own acceptance ledger, a new record in the same build directory, named as every
  builder's ledger is: one line each for AC1, AC2 and AC3, each OWED to the close.

No code file and no other record.

### Alternatives rejected

- **Name the owner by hand in each spec's New-arm line.** That is the defect: units 76 to 78 named
  unit 73, which built before them. A hand-typed owner is a second copy of the build order.
- **Have the suite read the specs to find its owner.** The suite reads the gate manifest, the
  hook, the charter and the merge-bar guide, never a build record; an arm over one build's spec folder would make every bar depend on a
  record this build owns.

## 5. Production-readiness checklist

- security — no new write path.
- perf / scale — one pass over this build's specs and one arm run, once, at the close.
- error / empty / loading states — an empty derivation is a red, never an owner of nothing: AC1
  requires a non-empty list.
- observability — the floor's comment names the owner, so a later unit knows whose number it moves.
- risks — a spec whose New-arm line names the suite under another spelling drops out of the list;
  AC1's figure line records the count so a drop reads as a change.
- testing — AC1 by probe, AC2 by scratch clone, AC3 by ledger, all at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When
  `set -- tools/run-gates/run-gates.gov.test.sh ; for f in memory/builds/dWitnessedBar/spec/*.md; do grep -q "^New arm: $1" "$f" && printf '%s %s\n' "$(sed -n 's/^\*\*Status:\*\*.* order \([0-9]*\).*/\1/p' "$f")" "$f"; done | sort -k1,1n -k2,2`
  runs at the close, it prints a non-empty list whose last line names the owner, and
  `grep -B1 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh | head -1` prints a comment
  naming that owner's id.
  Red when: the floor's comment names a unit that builds before another unit adding a gov-canary arm,
  the owner's comment sits where `grep -B1` cannot see it, or the list is empty and no owner is named.
  figure: the owner and the list's length are DERIVED at observation time; the list held 20 specs on
  2026-10-25 and 28 ending at `TOOL-dWitnessedBar-90` on 2026-11-21 (PINNED by this pipeline).
- **AC2** — When the arm runs over the built tree at the close, its `PASS (<n> assertions)` count
  equals the value `grep '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh` prints. When
  `grep -n 'AC2' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-83*acceptance-ledger*` runs,
  it prints one line holding both numbers and the owner's id.
  Red when: the executed count exceeds the floor, so the last arms added can be deleted with the
  canary green.
  figure: both numbers are DERIVED at observation time.
  permission: the arm's run is the main loop's, at the close.
- **AC3** — When `grep -n 'AC15' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-73*acceptance-ledger*`
  runs at the close, it prints one line holding the floor and `PASS` count at unit 73's pass commit
  and naming `TOOL-dWitnessedBar-83` AC2, on the line grep prints.
  Red when: unit 73 AC15 is recorded against the final floor, which unit 73 did not state, or with no
  number.
  permission: the arm's run is the main loop's, at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. AC2 runs the
`run-gates gov canary` arm at the close; this unit adds no arm and moves none, so it declares no
`New arm:` line.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 78 is itself derived
  and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — How is the floor's owner fixed (id 14)?** Options: (a) derived from the specs' New-arm lines
  and the dispatch order, checked at the close; (b) assigned by name to `TOOL-dWitnessedBar-82`, the
  report's fix; (c) a spec lint over every New-arm line. (b) is wrong as soon as
  `TOOL-dWitnessedBar-84` adds arms after it, which fails AC2. (c) adds a gate, a public surface no
  clause of this build names; veto 2 discards it. RESOLVED (agent, 2026-10-25, delegated): (a),
  rung 3, the most feature-rich survivor.
  widens: none · relaxes: none
- **F3 — Which side of the constant does AC1 read the owner on?** Forced by the re-ground:
  `TOOL-dWitnessedBar-82` landed its comment below the constant, and rev-2's `grep -B3` reads above it.
  Options: (a) the one line directly above, `grep -B1 ... | head -1`, the side `TOOL-dWitnessedBar-88`
  S7 and `TOOL-dWitnessedBar-90` S11 state and the read 85, 88, 89 and 90 make; (b) keep `grep -B3`,
  which passes on an owner up to three lines above with other comment lines between; (c) read both
  sides, which passes on the below-line shape that `TOOL-dWitnessedBar-88` AC7 reds, so two specs'
  criteria disagree. RESOLVED (agent, 2026-11-21, delegated): (a), the most feature-rich survivor,
  joining the reading the later units' criteria already make; (b) satisfies fewer of them.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 74 to 78, id 14
  (HIGH, item H2, shared with id 2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of units 79 to 84; nothing else
  moved.
- rev-3 · 2026-11-21 · §1 · S1 · S2 · S3 · §3 · §4 · AC1 · §8 · §10 · re-grounded at `8519d2244`
  under `2026-11-19-prompt-TOOL-dWitnessedBar-83-reground-brief`: units 73, 78 and 82 as landed, the
  owner now `TOOL-dWitnessedBar-90` over 28 specs (PINNED 2026-11-21), unit 28's arm out of scope, S3's writer and line,
  AC1's comment read on the side the later units state (F3), Rollout and Files touched listed
  exactly, and blob-pinned citations; intent unchanged.

## 10. Reuse audit

The seam is the dispatcher's own order, `tools/workflows/unattended-build.js@8519d2244:692-697`, read
from the `order` verb every spec carries, and the acceptance ledger of `memory/HYGIENE.md`
"Acceptance ledger".
`python tools/codebase-map/reuse_lookup.py "assert a pinned count of executed assertions against a floor"`
ranked `counts`, `compare_counts`, `measure_typed_counts`, `read_count` and `read_floor` first
(PINNED 2026-11-21). None owns a pinned assertion floor: `read_floor` reads a Python version floor
and a loop policy, and `compare_counts` compares declared and measured key counts. So no existing
seam fits beyond the two named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
