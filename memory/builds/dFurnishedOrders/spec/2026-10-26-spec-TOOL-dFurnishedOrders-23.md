# TOOL-dFurnishedOrders-23 — the answered-call hook's verifier exemption keyed on `subject-reads`, and certified on every verifier the shipped role index holds, never on a planted block name

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5ff43572 · streams tooling · order 12 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 20 unit specs
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`)
confirmed finding **id 48 at BLOCKER**, report item **B1**. Id 1 shares that item and takes
`TOOL-dFurnishedOrders-22`.

Under the default `refuse`, `TOOL-dFurnishedOrders-6` refuses a reviewer's read of the spec or diff it
reviews and a skeptic's or tester's read of what it checks, because its S4 compares an input block's
name with class words no block carries. Its AC2 passes only by planting an `### input:claim` block,
which no shipped role's `reads:` line names (`tools/roles/agents/*.agent.md`, read at base `5ff43572`),
so the criterion certifies an exemption on a population the hook never sees: the class
`staged-break-substitutes-a-synthetic-value` (`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`).

This unit keys the exemption on the slots `TOOL-dFurnishedOrders-22` declares, and replaces the
planted case with one drawn from the shipped role index: every verifier, every subject slot, and every
non-subject slot of the same role. It repairs `TOOL-dFurnishedOrders-6` and builds one step after it
(order 12), after unit 22 by the dispatch's id sort.

## 2. Scope (IN)

- **S1** — The decision re-keyed. In `checkAnsweredCall` (`tools/roles/answered-calls.js`,
  `TOOL-dFurnishedOrders-6` S1 and S4), a read the read class matched under a block headed
  `### <slot>` runs, unrecorded, when the role's index entry lists `<slot>` in `subject-reads`. The
  comparison is equality of the whole heading key, and the hook compares the heading with no other
  field. Observed by AC1 and AC2.
- **S2** — An index without the field. An entry with no `subject-reads` key, or one that is not a list
  of strings, reads as `[]`: no read is exempt, and the call proceeds to the policy as any answered
  call does. It is not a hook failure, so no `hook-failed` record is written for it. Observed by AC3.
- **S3** — The verifier arms drawn from the shipped population. The suite
  `tools/roles/answered-calls.test.sh` copies the repository's rendered `.claude/roles.json` into its
  fixture and plants, for each role whose `verifies` is not empty, one work order per `input:` slot of
  that role's `reads` line: a slot `subject-reads` lists must exit 0 with no record, and any other
  slot must exit 2 with a `refused` record; and for `gov-builder`, every slot of its `reads` is
  refused. No block heading in these arms is a literal of the suite. The arm fails when it plants no
  verifier, or when a role whose `verifies` is not empty yields no exit-0 case. Observed by AC4.
- **S4** — Unit 6's planted case retired. The `### input:claim` plant of `TOOL-dFurnishedOrders-6`
  AC2 leaves the suite; that unit's ledger answers AC2 in the AMENDED form, naming this unit's AC1 and
  AC2. **Readers:** by name: READER NOT IN TREE — the one file that plants it is
  `answered-calls.test.sh`, which `TOOL-dFurnishedOrders-6` S9 creates and which is absent at base ·
  by value: NO VALUE READERS — a planted block name feeds no other check. Observed by AC4.

## 3. Non-goals (OUT)

- The field, its check and its index entry: `TOOL-dFurnishedOrders-22`'s.
- The read, method and state classes, the policy values and the failure path: `TOOL-dFurnishedOrders-6`
  S3, S5 and S7, unchanged.
- A spec-lint over the block names a criterion plants (the report's left-shift gate): no clause of
  this build names it, and S3 removes the population the lint would have caught.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-6` — `checkAnsweredCall`'s exemption step and the suite whose `### input:claim` plant S3 and S4 replace (id 48)
- **consumes-from** `TOOL-dFurnishedOrders-22` — `subject-reads`, the index key the exemption compares a block heading with (ids 1 and 48)
- **hands-off** `TOOL-dFurnishedOrders-32` — `checkAnsweredCall`'s subject comparison and the index-drawn arm, which unit 32 extends to a group entry, and AC1 and AC2's reviewer rows, which unit 32 re-reads from the roster (id 2 of the second audit)
- **hands-off** `TOOL-dFurnishedOrders-37` — S2's reading of a malformed `subject-reads`, which unit 37 S35 moves into `loadRoleIndex` as a broken index (id 24 of the second audit)

## 4. Design

### The decision after this unit

```
checkAnsweredCall(data, env)
  ... read class matched under ### <slot>
  role = index.roles[agent_type]; subject = Array.isArray(role['subject-reads']) ? role['subject-reads'] : []
  subject includes <slot>  -> run, unrecorded                                  (S1)
  else                     -> readPolicy('roles.answered-calls') as before     (unit 6 S5)
```

The method and state classes carry no input block, so the exemption never reaches them, as before.

### Why the arm reads the index

A typed block name is the author's population; the index is the population the hook reads at a call.
Drawing every plant from `.claude/roles.json` means a role renamed, a slot added to a `reads` line or a
subject moved re-plants the arm with no edit, and a field that names a slot no role reads cannot pass,
because `TOOL-dFurnishedOrders-22` S2 refuses it before the index is written. The floor is derived, the
count of roles whose `verifies` is not empty, so the arm never passes on an empty selection
(`memory/gotchas/vacuous-selector-empty-population.md`).

### Inventory

Minted: none. S1 changes one comparison of `checkAnsweredCall`; S3's arms are loops of the existing
suite.

### Migration

None: an index without the field reads `[]` (S2), and `TOOL-dFurnishedOrders-22` writes the field in
the same build.

### Rollout

Live at landing. The `KIT_ROLES_VERSION` move `TOOL-dFurnishedOrders-22` makes covers this unit's
shipped bytes in the same landing; the pass moves it again only where the kit epoch leg asks.

### Files touched (estimate)

- `tools/roles/answered-calls.js`
- `tools/roles/answered-calls.test.sh`

### Alternatives rejected

- **Keep the class words and map them to slots in the hook.** The hook would hold a second copy of a
  role's subject beside the role file; unit 22 F1 put it in one field.
- **Rewrite AC2 with a different typed slot.** A typed slot passes as long as the author types the
  right one, which is the defect; S3 reads the slot from the index instead.

## 5. Production-readiness checklist

- security — the exemption narrows to declared, checked slots; an index entry the hook cannot read
  exempts nothing, so a malformed index never widens what a role may re-read.
- perf / scale — one array lookup per matched read; the arm adds one planted call per verifier slot.
- error / empty / loading states — an absent or malformed `subject-reads` reads `[]` (S2); a broken
  index stays unit 6's path.
- observability — an exempt read writes no record, as unit 6 S4 states; a refused one names its block.
- risks — a verifier whose subject arrives in a slot unit 22 did not list is refused; the arm's
  non-subject cases make that visible at the close rather than in a run.
- testing — AC1 to AC4 by probes a pass runs in a fixture repository; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: `TOOL-dFurnishedOrders-22` S4 documents the field the exemption
  reads.

## 6. Acceptance criteria

- **AC1** — When a `PreToolUse` payload with `agent_type` `gov-spec-reviewer`, tool `Read` and a
  transcript whose work order hands the read range under `### input:spec` is piped to
  `node answered-calls.js` in a fixture repository holding a copy of the rendered
  `.claude/roles.json`, it exits 0 and the session's record file gains no line; the same payload with
  `agent_type` `gov-builder` exits 2 and records `refused`.
  Red when: a reviewer is refused the spec it reviews.
  fixture: a scratch repository under `%TEMP%`, built by the pass, as unit 6 AC1's.
- **AC2** — When the AC1 payload carries `agent_type` `gov-diff-reviewer` and the range is handed under
  `### input:spec`, it exits 2 and records `refused`; handed under `### input:diff`, it exits 0 with no
  record.
  Red when: a verifier's re-read of its handed criterion is exempt as if it were its subject.
- **AC3** — When the fixture's index entry for `gov-skeptic` carries no `subject-reads` key and the
  range is handed under `### input:diff`, the hook exits 2 recording `refused`, and the record file
  holds no `hook-failed` line.
  Red when: a missing field throws into the failure path, or exempts every read.
- **AC4** — When a `bash` loop pipes to `node answered-calls.js` one payload per role and `input:` slot
  that the rendered `.claude/roles.json` and the role files' `reads:` lines yield, each subject pair
  exits 0 and each other pair exits 2, the subject pairs number at least the roles whose `verifies` is
  not empty, and `grep -c "input:claim" answered-calls.test.sh` in `tools/roles/` prints 0.
  Red when: the exemption is certified on a block name no shipped role reads.
  figure: the pair counts are DERIVED from the index at observation time.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles adopter self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The leg `answered-calls self-test` is `TOOL-dFurnishedOrders-6`'s, not in the manifest at base, so it is
named here in prose; this unit's arm runs under it.

New arm: tools/roles/answered-calls.test.sh · covers AC1 AC2 AC3 AC4 · the verifier arms planted from the copied index, staged by keying the exemption on `verifies` again, which refuses every reviewer's subject read · none

## 8. Open questions

- **F1 — What does the hook do with an entry that has no `subject-reads`?** Options: (a) read `[]`,
  exempting nothing; (b) fall back to `verifies`; (c) treat it as a hook failure. (b) restores the
  defect this unit closes; (c) makes every role read on a stale index a recorded failure, and at CLI
  2.1.295 or later an exit 1. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, deny by default,
  the charter's `[security]` rule. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, as `TOOL-dFurnishedOrders-22` §8 F3
  records. widens: none · relaxes: none
- **F3 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-6` and `-22` precede this
  unit and are specced, unbuilt at `5ff43572`. RESOLVED (agent, 2026-10-26, delegated): the build run
  re-grounds on each at the pass and stops this unit if a named section is still absent then, rung 1,
  the brief's rule for unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 20 unit specs, id 48
  (BLOCKER, item B1, shared with id 1).
- rev-2 · 2026-10-26 · §3 · hands-off edges to units 32 and 37 (ids 2 and 24 of the second audit).

## 10. Reuse audit

The seams extended: `checkAnsweredCall`'s exemption step (`TOOL-dFurnishedOrders-6` S4), and
`loadRoleIndex` (`tools/hooks/scratch-guard.js:952`), which already hands the hook each role's index
entry, so the field costs no second read. `python tools/codebase-map/reuse_lookup.py "exempt a
verifier's read of the input slot that is its subject from an answered-call refusal"` ranked name
stems (`read`, `read_text`, `refusal`, `Refusal`), none an exemption or a slot key, so no existing seam
fits beyond the two named. The recall probe returned `TOOL-dFurnishedOrders-6`, the audit's B1 text and
the spec brief's row, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which input slot does a verifier role read as
its subject" --terms "verifies subject claim verdict input:spec input:diff reads exemption
answered-calls verifier role index"`
