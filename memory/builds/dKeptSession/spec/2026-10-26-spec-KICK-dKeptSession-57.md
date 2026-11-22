# KICK-dKeptSession-57 — the batch's pass-bound items observed at a pass that runs after them, never at an earlier unit's commit

**Status:** DEFERRED · rev-3 · 2026-11-21 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 32 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-57-deviation-571.md](../build/2026-10-26-build-KICK-dKeptSession-57-deviation-571.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-57-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-57-promoted-fix-return.md) | research | KICK-dKeptSession-62 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-57-1-spec-writer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-57-1-spec-writer.md) | journal | KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-57-promoted-fix-brief.md) | research | KICK-dKeptSession-62 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief.md) | research | KICK-dKeptSession-30 KICK-dKeptSession-32 KICK-dKeptSession-35 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-56 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-57-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-57-precheck-brief.md) | research | KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-22-prompt-KICK-dKeptSession-57-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-57-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed finding **id 1 at HIGH**, report item **H1**, which no other id shares.

`KICK-dKeptSession-56` takes order 31, past every unit it amends, yet four of its items bind passes
that run long before it. S13 lands unit 39's tuple member "in unit 5's pass" (order 16) and names a
gate unit 5's §7 does not carry. S25 to S27 and S44 bind each named unit's legs to "at its pass".
S29 makes `.governance/policy.json` a write of unit 40's pass (order 4) and unit 41's pass
(order 29), while unit 41 §3 says that file does not move. Its AC11 runs `git show <unit 5's pass
commit>` and AC24 runs `mirror --check` at units 40's and 41's pass commits. A builder of 56 cannot
change those commits, so the criteria stay red for good. This unit re-binds each item to a pass that
runs after the work it observes: this unit's own. It repairs `KICK-dKeptSession-56` and builds one
step after it (order 32).

## 2. Scope (IN)

- **S1** — id 1. The factory row and the tuple member. `KICK-dKeptSession-56` S13's "land in one
  write set, in unit 5's pass, whose gates name `build-index selftest`" and its AC11 are superseded
  by name. Unit 5 S12's factory row and unit 39 S1's tuple member stay each their own unit's pass, as
  those specs state. This unit's pass observes both together at its own commit: the row in
  `tools/memory-tree/build_records.py`, the member in `tools/memory-tree/tree_lib.py`, and
  `import build_records` exiting 0. This spec's §7 names `build-index selftest`, which the close
  runs. Observed by AC1.
- **S2** — id 1. The committed mirror. `KICK-dKeptSession-56` S29's "a write of units 40 and 41" and
  its AC24 are superseded by name. This unit's pass runs `python tools/policy/policy.py mirror
  --write` once and commits `.governance/policy.json` when its bytes moved, so the mirror is fresh
  over every input units 40 and 41 changed. Unit 41 §3's "`.governance/policy.json` does not move"
  reads as this item. Observed by AC2.
- **S3** — id 1. The owed legs. `KICK-dKeptSession-56` S25 to S27 and S44's "each unit's pass names
  the legs" and the "at its pass" of AC22 are superseded by name. This unit's pass runs `python
  tools/check-spec-tokens.py --legs-for` over each named unit's `### Files touched (estimate)` and
  records the printed legs in this unit's own acceptance ledger,
  `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-57-1-acceptance-ledger.md`,
  as one OBSERVED line per unit, each naming its unit. The lines for units 35, 36 and 42 name `loop
  selftest` as the leg that runs `tools/loop/selftest.py` at the close. Every named unit builds before
  this unit and is CLOSED when it builds, so no named unit's ledger is written (F1). Observed by AC3.
- **S4** — id 1. The sibling texts answered. This unit's own acceptance ledger answers
  `KICK-dKeptSession-56` AC11, AC22 and AC24 by this unit's AC1 to AC3, each by name, quoting AC11's
  "the factory row lands without the tuple member", AC22's "a guarded leg is missing from a pass's
  record" and AC24's "at each of unit 40's and unit 41's pass commits". Unit 56 builds at order 31
  and is CLOSED when this unit builds, so neither its spec nor its ledger is written (F1). Observed by
  AC4.

## 3. Non-goals (OUT)

- Renumbering any order. Unit 39 keeps its step 17; nothing in S1 needs units 5 and 39 to share a
  pass once both are built before this one.
- The commits between units 5's and 39's passes. No bar runs there (BUILD-METHOD M6), and unit 39's
  pass is the next step, so the import refusal it could meet is never observed by a gate.
- The six units the batch's S25 and S27 omit: id 2, `KICK-dKeptSession-62`.
- The report's left-shift hygiene arm, that a criterion naming an earlier unit's pass commit reds. It
  is a separate gate, so a separate unit by M2, and no clause of this build names it.

### Edges

- **consumes-from** `KICK-dKeptSession-56` — S13, S25 to S27, S29 and S44 with AC11, AC22 and AC24, which this unit re-binds to its own pass (id 1)
- **hands-off** `KICK-dKeptSession-62` — S3's ledger rule, which the batch's S1 runs for units 49, 50, 52 to 55 (id 2)
- **hands-off** `KICK-dKeptSession-63` — S3's ledger rule, whose population the batch's S9 derives and whose non-success outputs its S17 records (ids 13, 27)

## 4. Design

### Evidence

- spec-56 §1: "takes the order past every unit of the build (order 31)"; S13: "in unit 5's pass,
  whose gates name `build-index selftest`"; S29: "a write of units 40 and 41"; AC11: "`git show
  <unit 5's pass commit>`"; AC24: "at each of unit 40's and unit 41's pass commits".
- spec-5 §7's leg line names `unattended kit gate`, `manifest-check self-test`, `scratch-guard
  self-test` and four more, and no `build-index selftest`.
- spec-41 §3 says `.governance/policy.json` does not move; spec-40:62 and spec-41:69 hand the write
  to unit 56.
- The README's generated build order puts unit 5 at step 16, unit 39 at 17, unit 40 at 4, unit 41 at
  29 and unit 56 at 31.

### The re-binding

| 56's text | Bound to | Re-bound to |
|---|---|---|
| S13, AC11 | unit 5's pass commit | this unit's pass commit, AC1 |
| S29, AC24 | units 40 and 41's pass commits | this unit's `mirror --write`, AC2 |
| S25 to S27, S44, AC22 | each named unit's pass | one ledger line per unit at this pass, AC3 |

### Inventory

No identifier is minted.

### Migration

None: the mirror is re-rendered by the kit's own verb, and this unit's ledger carries the lines.

### Files touched (estimate)

- `.governance/policy.json`: S2, when its render moved
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-57-1-acceptance-ledger.md`:
  S3's lines and S4's answers beside the criteria observed

### Alternatives rejected

- **Moving S13, S29 and the ledger duties into units 5, 39, 40 and 41's specs.** It folds the
  finding into specs this disposal may not fold, and S29's write would still land at order 4, before
  unit 41's catalogue edit at order 29 moves the mirror again.
- **Dropping AC11, AC22 and AC24.** The duties they observe stay owed, and nothing would observe them.

## 5. Production-readiness checklist

- security — none: one render by the kit's own verb and ledger lines.
- perf / scale — one `mirror --write` and one `--legs-for` per named unit, once.
- error / empty / loading states — before dGroundRules lands `tools/policy/`, S2 has no verb to run;
  this unit is built after every unit that needs it, and the close's bar runs after it.
- observability — each ledger line names the legs it read.
- risks — the committed mirror is stale between units 40's and this unit's passes; `policy-mirror.js`
  reads it STALE and its reads fall through to the reader shim (`KICK-dKeptSession-49` §5).
- testing — the criteria of §6; no arm is added.
- migration — none.
- user docs — none: no owner-facing behaviour changes.

## 6. Acceptance criteria

Each criterion reads this unit's own pass commit, `<this pass>`.

- **AC1** — When `git grep -n "mailbox-message" <this pass> -- tools/memory-tree/tree_lib.py
  tools/memory-tree/build_records.py` runs, it prints the tuple member and the factory row, and
  `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import build_records"` exits 0 at
  that commit.
  Red when: either half is absent, or the import refuses.
- **AC2** — When `python policy.py mirror --check` runs in the policy kit at `<this pass>`, it exits 0
  and prints `policy: mirror fresh`.
  Red when: the committed mirror is stale against the inputs units 40 and 41 changed.
- **AC3** — When this unit's ledger is read at `<this pass>`, it carries one OBSERVED line for each
  of units 30 and 32 to 44, naming the legs `check-spec-tokens.py --legs-for` prints over that unit's
  Files touched at `<this pass>`, and the lines for units 35, 36 and 42 name `loop selftest`.
  Red when: a named unit has no line, or a printed leg is missing from its line.
- **AC4** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c` prints `1`
  for each of "the factory row lands without the tuple member", "a guarded leg is missing from a
  pass's record" and "at each of unit 40's and unit 41's pass commits"; and `git diff --name-only
  <pass base> HEAD -- memory/builds/dKeptSession/build/` lists no acceptance ledger but this unit's
  own.
  Red when: an answer or a line lands in unit 56's ledger or a named unit's, or this unit's ledger
  leaves one of unit 56's criteria unquoted.

## 7. Gates

`build-index selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's `policy fixtures` leg checks the mirror once dGroundRules has landed it.

## 8. Open questions

- **F1 — Where are S3's lines and S4's answers recorded?** Units 30 and 32 to 44 and unit 56 build
  before this unit, so each is CLOSED when it builds, and their ledgers are in neither this unit's
  Files touched nor its write set. (a) Each named unit's acceptance ledger, a record of a closed unit
  written by a later one; (b) this unit's own acceptance ledger, one line per named unit and unit
  56's criteria quoted. Recommendation (b). RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a
  CLOSED unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled.
  Rejected: (a), writing the other unit's ledger. The main loop's ruling, in
  `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-2 promotions' audit, H1 (id 1).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S3 · S4 · §4 · AC3 · AC4 · §8 · S3's lines and S4's answers move from
  the named units' and unit 56's ledgers to this unit's own acceptance ledger, which joins Files
  touched, F1 resolved (b) and AC4 observing the quoted criteria, under the brief
  `2026-11-21-prompt-KICK-dKeptSession-30-ledger-class-brief`; the class KICK-dKeptSession-49 rev-6
  first resolved. §1 re-reads unit 56 at rev-4, whose S25 to S27 and S44 record in its own ledger.
  The ledger's path trips the two `recall floor` legs, already on §7's leg line.

## 10. Reuse audit

The seams reused are `policy.py mirror --write` and `--check`, dGroundRules' one mirror renderer, and
`check-spec-tokens.py --legs-for` (`tools/check-spec-tokens.py`), the derivation 56's S25 already
names; nothing is minted. `python tools/codebase-map/reuse_lookup.py "re-bind a pass commit
criterion to a later pass"` returned name-stem candidates only, so no existing seam in the tree fits
beyond those two verbs.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
