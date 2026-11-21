# KICK-dKeptSession-52 — the per-exit pass observed on a repeated interface, so dropping `--pass` prints a duplicate

**Status:** DEFERRED · rev-3 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-52-deviation-521.md](../build/2026-10-26-build-KICK-dKeptSession-52-deviation-521.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md) | research | KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-53 KICK-dKeptSession-55 |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 3 at HIGH**, report item **H5**, which no other id shares.

`KICK-dKeptSession-35` S1 gives every `confirmed` and `changed` notice `--pass <n>`, the Design-exit
ordinal, and its rev-2 AC1 said a copy dropping `--pass` reds "on the A to B to A case". It cannot.
`KICK-dKeptSession-31` S1 derives the id from eight fields, `kind` and `content-key` among them, and
over interface texts A, B, A the posts to one dependent are (`confirmed`, A), (`changed`, B) and
(`changed`, A): exits 1 and 3 differ in kind, and exits 2 and 3 in key, so without `--pass` no two
share an id and the arm stays green with S1 removed. This unit pins the case that only the pass
separates and names the red it prints. It repairs `KICK-dKeptSession-35` and builds one step after
it (order 26).

## 2. Scope (IN)

- **S1** — id 3. The discriminating case. A plant `notices-repeat-key` in
  `tools/loop/loop_transition.py`'s fixture, a `PLANTS` member read by a `run_selftest` case
  (`tools/loop/loop_transition.py#run_selftest`), moves the parent out of Design three times with the
  interface texts A, B and B, through the B5 and B21 rows `KICK-dKeptSession-35`'s
  `notices-two-dependents` plant walks, and two dependent READMEs, so exits 2 and 3 publish two
  `changed` notices with one content key to each dependent. Observed by AC1.
- **S2** — id 3. The staged red named. The case's staged break is a scratch copy of
  `loop_transition.py` whose `write_dependency_notices` passes no `--pass`; on it, exit 3 prints
  `mail — duplicate` for each dependent, and the build records that line in unit 35's acceptance
  ledger before the fix lands. Observed by AC2.
- **S3** — id 3. The sibling text, already carried. `KICK-dKeptSession-35` rev-3's AC1 "Red when"
  clause and its §4 Alternatives line read: the pass separates a `changed` from a later `changed`
  with the same key, while kind and key already separate the A, B, A posts. NOT OBSERVED: unit 35's
  rev-3 text carries it, and no behaviour moves with it.

## 3. Non-goals (OUT)

- The pass itself and the refusal line: `KICK-dKeptSession-35`, unchanged.
- The id's fields: `KICK-dKeptSession-31`.
- The report's left-shift entry, that every staged break in a spec names the red line it prints.
  No clause of this build names that checklist; S2 is the instance here.

### Edges

- **consumes-from** `KICK-dKeptSession-35` — `write_dependency_notices`' `--pass <n>` and AC1's three-exit plant, which this unit pins to a key the pass alone separates (id 3)
- **hands-off** `KICK-dKeptSession-62` — the `notices-repeat-key` arm, whose leg the batch's S1 records (id 2)

## 4. Design

### Evidence

- `KICK-dKeptSession-31` S1: `derive_message_id <build> <item> <pass> <kind> <subject> <answers> <to>
  <content-key>`, each absent field `none`; `KICK-dKeptSession-51` keeps the act as a later ninth.
- `KICK-dKeptSession-7` S4: the first post to a dependent is `confirmed`, every later one `changed`,
  each carrying its `--interface` key, so a key repeated at a later exit is the only collision the
  kind leaves.
- The fixture's plants are `PLANTS` members of `tools/loop/loop_transition.py`, run by
  `run_transition_fixture` and read by `run_selftest`'s cases through `run_selftest_cases`
  (`tools/loop/loop_transition.py#run_transition_fixture`), the `loop transition record` leg's
  `check --selftest`.

### The posts to one dependent, interface texts A, B, B

```
exit 1  confirmed · key(A) · pass 1
exit 2  changed   · key(B) · pass 2
exit 3  changed   · key(B) · pass 3      without --pass: id equals exit 2's -> mail — duplicate
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `notices-repeat-key` | `--plant` case and its `run_selftest` case | `tools/loop/loop_transition.py` |

### Migration

None.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: S1's plant and case

### Alternatives rejected

- **Four exits A, B, A, B.** It also collides at exit 4, but needs a fourth exit and reads no more
  than A, B, B does.
- **Keeping A, B, A and asserting six posts.** Six posts land with or without the pass, so the case
  cannot fail on the scope item it claims.

## 5. Production-readiness checklist

- security — none: a fixture plant.
- perf / scale — one more three-exit plant in the transition suite.
- error / empty / loading states — none new.
- observability — S2's recorded red.
- risks — none.
- testing — the criteria of §6 and the arm in §7.
- migration — none.
- user docs — none: no behaviour a user sees moves.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-35`'s: a scratch repository with two builds' READMEs naming one
parent, a bare origin under `%TEMP%` and `RUN_CLAIMS=on`.

- **AC1** — When `python tools/loop/loop_transition.py --fixture --plant notices-repeat-key` records
  three Design exits with the interface texts A, B and B, `--mail read dA` and `--mail read dB` each
  list one `confirmed` and two `changed`, every post printing `mail — posted`.
  Red when: a post prints `mail — duplicate`.
- **AC2** — When the same plant runs against the scratch copy whose `write_dependency_notices`
  passes no `--pass`, exit 3 prints `mail — duplicate` for each dependent, and unit 35's acceptance
  ledger holds that line.
  Red when: the copy stays green, so the case does not decide S1 of unit 35.

## 7. Gates

`loop transition record` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_transition.py · covers AC1 AC2 · three Design exits with interface texts A, B, B to two dependents, staged red by a scratch copy dropping `--pass` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H5 (id 3).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S1 · S2 · S3 · §4 · §5 · AC1 · AC2 · §7 · §10 · re-grounded on base
  c2a407b0 by `2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief`: the case moves
  from the absent `tools/loop/selftest.py` to a `PLANTS` member of `loop_transition.py`'s fixture,
  walking the B5 and B21 rows unit 35's rev-3 plant walks; the leg line gains
  `loop transition record`. Narrowed: S3 is carried by `KICK-dKeptSession-35` rev-3's own AC1 and
  Alternatives text, so no ledger answer is owed for it.

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-35`'s three-exit plant and its staged copy, now pinned to
interface texts, in the landed fixture `tools/loop/loop_transition.py#run_transition_fixture` and its
`PLANTS`; no case runner is minted. `python tools/codebase-map/reuse_lookup.py "post each dependent a
notice per Design exit ordinal"` ranked `DesignRefusal` and `read_design_conf` by the name stem
`design` only, so no other seam fits and unit 35's plant is the seam.

Recall terms used: `python tools/memory-recall/query.py "which staged break makes the per-exit
pass decide a notice id" --terms "pass Design exit ordinal changed confirmed content-key duplicate
staged break fixture write_dependency_notices"`
