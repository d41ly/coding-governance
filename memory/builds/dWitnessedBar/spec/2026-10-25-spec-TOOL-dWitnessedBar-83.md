# TOOL-dWitnessedBar-83 — the gov canary's floor is owned by the last unit that adds an arm, derived from the specs, and its equality with the executed count is held at the close

**Status:** DEFERRED · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 43 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-83-round9-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-83-round9-fix-return.md) | research | TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-83-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-83-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-83-round9-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-83-round9-fix-brief.md) | research | TOOL-dWitnessedBar-84 |
| [2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-79-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-84 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 74 to 78
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-74-spec-audit-round1.md`)
confirmed finding **id 14 at HIGH**, report item **H2**. Id 2 shares that item and takes
`TOOL-dWitnessedBar-82`.

`TOOL-dWitnessedBar-73` S15 states the floor at unit 73's pass, and its AC15 requires the close's
`PASS (<n> assertions)` count to equal that floor. Units 74 to 78 build after unit 73 and add executed
assertions, so the equality fails once unit 78 lands, and no unit is assigned to restate the floor or
to answer AC15 against the final one. The report's left-shift names the rule that was missing: the
last unit in the build that adds assertions owns the restatement.

This unit makes that owner a derived fact rather than a sentence each spec repeats. The owner is the
unit, among those whose §7 declares a gov-canary New arm, that the dispatcher builds last. At the close
the floor's comment must name it, and the executed count must equal the floor. Unit 73 AC15's close
clause is answered by that observation. It repairs `TOOL-dWitnessedBar-78` and builds one step after
it (order 43), after `TOOL-dWitnessedBar-82` within that order.

## 2. Scope (IN)

- **S1** — The owner, derived. The floor's owner is the spec under `memory/builds/dWitnessedBar/spec/`
  that carries a line opening `New arm: tools/run-gates/run-gates.gov.test.sh` and sorts last by its
  status header's `order`, then by id string, the order `tools/workflows/unattended-build.js:608-613`
  dispatches in. At the close the comment beside `FLOOR_ASSERTIONS=` in
  `tools/run-gates/run-gates.gov.test.sh` names that unit's id. Observed by AC1.
- **S2** — The close's equality. At the close the arm's `PASS (<n> assertions)` count over the built
  tree equals `FLOOR_ASSERTIONS`. This unit's acceptance ledger records both numbers and the owner S1
  derived. Observed by AC2.
- **S3** — Unit 73 AC15 answered. Unit 73's acceptance ledger beside AC15 records the equality at
  unit 73's own pass commit, observed in a scratch clone checked out there, and names this unit's AC2
  as the close's equality, since units 74 to 84 add arms after unit 73 builds. Observed by AC3.

## 3. Non-goals (OUT)

- The restatement after unit 78, which is `TOOL-dWitnessedBar-82`'s for id 2, and the restatement for
  the arms `TOOL-dWitnessedBar-84` adds, which is that unit's.
- A gate that reads the owner on every bar. The derivation reads spec files, which the suite does not
  read; it is a close-time observation, and the floor check at `:459` is the per-run gate.
- Rewording unit 73 AC15. It is answered in unit 73's ledger by name, as `TOOL-dWitnessedBar-78` §3
  answers units 68 to 73.
- The report's left-shift text as a spec lint over New-arm lines. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-73` — S15's floor and AC15's equality, which S3 answers at unit 73's pass and S2 holds at the close (id 14)
- **consumes-from** `TOOL-dWitnessedBar-82` — the restated floor and its comment, which S1 checks against the derived owner (ids 14 and 2)
- **hands-off** `TOOL-dWitnessedBar-84` — the last restatement, whose comment S1 requires to name the last unit that adds a gov-canary arm (ids 14 and 21)
- **hands-off** `TOOL-dWitnessedBar-88` — S1's owner, AC1's pipeline and comment read, and S3's pass-commit record, which unit 88 derives through the shipped readers, reads with `grep -B1` and locates by `build_commit` (ids 6, 9, 10 and 22 of the round-1 spec audit of units 79 to 84)

## 4. Design

### Evidence

- `spec/2026-10-25-spec-TOOL-dWitnessedBar-73.md` S15 states the floor at its own pass, and AC15
  requires the close's `PASS` count to equal it, with a comment naming units 65 to 73.
- `tools/run-gates/run-gates.gov.test.sh:459` fails only when `a` is below the floor, so assertions
  added after a restatement pass silently.
- The derivation of S1, run on 2026-10-25 over this build's specs, listed 20 specs from unit 12 at
  order 5 to unit 78 at order 42, and named unit 78 as the owner. After this round it names
  `TOOL-dWitnessedBar-84` at order 44.
- `tools/workflows/unattended-build.js:608-613` sorts by `order`, then by `String(id)`. A sort of
  spec paths by string after the order keeps the same tie order, because each path ends in the id
  followed by `.md`.

### Inventory

Minted: nothing in code. The ledger records of S2 and S3. No function, constant, plant, flag or file.
Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

At the close, after every unit is terminal. The unit takes order 43, after unit 78 and beside
`TOOL-dWitnessedBar-82`, whose restatement it reads; `TOOL-dWitnessedBar-84` builds at order 44 and is
the owner S1 expects.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/`

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
  `grep -B3 '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh` prints a comment naming that
  owner's id.
  Red when: the floor's comment names a unit that builds before another unit adding a gov-canary arm,
  or the list is empty and no owner is named.
  figure: the owner and the list's length are DERIVED at observation time; the list held 20 specs on
  2026-10-25.
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

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 74 to 78, id 14
  (HIGH, item H2, shared with id 2).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-88, promoted by the round-1 spec audit of units 79 to 84; nothing else
  moved.

## 10. Reuse audit

The seam is the dispatcher's own order, `tools/workflows/unattended-build.js:608-613`, read from the
`order` verb every spec carries, and the acceptance ledger of `memory/HYGIENE.md` "Acceptance ledger".
`python tools/codebase-map/reuse_lookup.py "assert a pinned count of executed assertions against a floor"`
ranked `counts`, `measure_typed_counts`, `build_counted_values` and `check_count_sources`, none an
owner of a pinned floor, so no existing seam fits beyond the two named above.

Recall terms used: `python tools/memory-recall/query.py "how is each condition of a canary byte check seen red, and who restates the assertion floor" --terms "canary liveness variant length tail CR byte check FLOOR_ASSERTIONS restated floor owner seen red"`
