# TOOL-dSafePassage-41 — the `ac-order` join lands in the pass that arms it, so no commit carries the join without its cutoff key

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 8 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-41-deviation-87.md](../build/2026-10-23-build-TOOL-dSafePassage-41-deviation-87.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 27 to 35
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md`)
confirmed finding **id 22** at HIGH, its item **D-6**. TOOL-dSafePassage-26 S45 adds the `ac-order`
join to `tools/check-spec-tokens.py` over every live spec, with no key, at order 6, and
TOOL-dSafePassage-34 arms its cutoff key at order 7. `memory/builds/aPacedTurnstile/spec/2026-08-20-spec-TOOL-aPacedTurnstile-14.md`
reads `SPECCED · rev-3`, which `LIVE` (`tools/check-spec-tokens.py:299`) matches, and lists AC11
(`:264`) before AC10 (`:268`); this unit read both on 2026-10-23. The `spec tokens (a spec's own names
resolve)` leg (`tools/gate-legs.json:1692`) has no guard. So the commit of TOOL-dSafePassage-26's pass
carries a join that names that spec, and the leg is red until the next order lands. Neither spec
sequences the key with the join. This unit is id 22's promotion: the join is built in this unit's one
pass, after TOOL-dSafePassage-34 has declared and read the key, so the commit that first carries the
join also carries the key it reads.

## 2. Scope (IN)

- **S1** — The join. `tools/check-spec-tokens.py` gains the `ac-order` join with TOOL-dSafePassage-26
  S45's predicate: a live spec whose §6 criterion labels, read with `AC_LABEL` (`:338`) inside the
  section `AC_HEAD` (`:334`) finds, do not ascend is a finding naming the spec and the first label out
  of order. It grades only a spec whose filename date, matched as `SPEC_DATE.search("/" + f)` the way
  the dated joins at `:1466` and `:1508` match it, is on or after `AC_ORDER_KEY` as TOOL-dSafePassage-34
  S1 reads it. A blank key turns the join off, and a refused key is the run's refusal. Its run line
  names the key's value and the graded count, as TOOL-dSafePassage-34 S2 states. Observed by AC1 and
  AC2.
- **S2** — One pass. The join and its read of `AC_ORDER_KEY` land in this unit's one pass commit.
  TOOL-dSafePassage-26's pass adds no join, as its §3 hands-off bullet to this unit says, and
  TOOL-dSafePassage-34's pass declares, reads and validates the key with nothing yet graded by it, as
  its §3 hands-off bullet says. So no commit of this build carries the join without its key.
  Observed by AC3.
- **S3** — The criteria carried. TOOL-dSafePassage-26's AC43 and TOOL-dSafePassage-34's AC1 and AC3,
  which observe the join, are observed at this unit's pass as AC1 and AC2 of this unit, and the two
  `tools/check-spec-tokens.test.sh` arms those units declare for them are this unit's one arm.
  Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The key, its conf comment and its refusal of a malformed value: `TOOL-dSafePassage-34`.
- TOOL-dSafePassage-8's criterion order, which TOOL-dSafePassage-34 S3 moves at order 7, before this
  pass grades it.
- Writing to another build's spec. TOOL-aPacedTurnstile-14 is dated before the key and is held
  ungraded, as TOOL-dSafePassage-34 S4 says.

### Edges

- **consumes-from** `TOOL-dSafePassage-34` — `AC_ORDER_KEY`, its declaration and read, and S3's move of TOOL-dSafePassage-8's AC8; without them the join would grade every live spec on its first commit
- **consumes-from** `TOOL-dSafePassage-26` — S45's predicate and AC43, which this unit builds in place of that unit's pass; without them the join has no stated predicate
- **hands-off** `TOOL-dSafePassage-42` — the reading of TOOL-dSafePassage-34's S1 and §10 with `SPEC_DATE`, finding 20, which that batch observes over this unit's join

## 4. Design

### The order of the three passes

| Order | Unit | Commit carries | `spec tokens` over the tree |
|---|---|---|---|
| 6 | TOOL-dSafePassage-26 | no `ac-order` join | unchanged by the join |
| 7 | TOOL-dSafePassage-34 | the key declared, read and validated; TOOL-dSafePassage-8's AC8 above AC9 | unchanged by the join |
| 8 | this unit | the join, reading the key | the join grades specs dated 2026-10-23 or later and names none |

### Inventory

Minted: the join name `ac-order` in `tools/check-spec-tokens.py`, moved here from
TOOL-dSafePassage-26's Inventory. No function beyond the join's own, no conf key, gate leg or policy
key.

### Migration

None.

### Rollout

Live at landing. It builds at order 8, after TOOL-dSafePassage-34 (order 7), whose key it reads. It
shares no file with `TOOL-dSafePassage-35`, the other unit at order 8.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `memory/map/features/spec-tokens.md`

### Alternatives rejected

- **TOOL-dSafePassage-26's pass reads the key.** The key is declared at order 7, after that pass, and
  this disposal renumbers no unit, so the join would read an undeclared key; to land green it would
  need TOOL-dSafePassage-34 moved before it.
- **Building TOOL-dSafePassage-26 and TOOL-dSafePassage-34 as one pass.** BUILD-METHOD M6's pass is one
  unit built, so two units committed together are not a pass kind.
- **A waiver row for TOOL-aPacedTurnstile-14.** A join born with a waiver grades the waiver, as
  TOOL-dSafePassage-34 §4 records.

## 5. Production-readiness checklist

- security: N/A — a spec-text join.
- perf / scale: one label scan per graded live spec.
- error / empty / loading states: the graded count rides every run line, so an empty population is
  visible; a refused key refuses the run.
- observability: the run line names the key, the count and each finding.
- risks: a spec dated before the key keeps an out-of-order list, graded by nobody, which
  TOOL-dSafePassage-34's conf comment states.
- testing: the scratch arm of §7 and the history probe of AC3.
- migration: none.
- user docs: N/A — `memory/map/features/spec-tokens.md` names the join beside its siblings; no `help/`
  page covers the checker.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py` runs over a scratch repo whose conf sets
  `SPEC_AC_ORDER_CUTOFF` to a date and whose live spec dated at it lists `AC2` before `AC1`, it names
  the spec and `AC2`; with the key blank it names nothing; with the spec dated a day before the key it
  names nothing.
  Red when: an out-of-order criterion passes the join, or the join grades a spec the key holds out.
- **AC2** — When `python tools/check-spec-tokens.py` runs over the tree after the pass, its `ac-order`
  line names no spec and states a graded count of at least this build's live specs.
  Red when: TOOL-dSafePassage-8 is live and still lists AC9 before AC8, or the count is zero.
  figure: the count is DERIVED by the run; 25 was measured at `c9675455` (TOOL-dSafePassage-34 §1).
- **AC3** — When `git log --reverse --format=%H -S "ac-order" -- tools/check-spec-tokens.py` runs after
  the pass, its first commit is TOOL-dSafePassage-34's or this unit's pass commit, and
  `git show <that commit>:tools/check-spec-tokens.py` carries `AC_ORDER_KEY`; at this unit's pass commit
  the join's grading condition reads it.
  Red when: TOOL-dSafePassage-26's pass, or any commit without the key, is the first to carry the join.

## 7. Gates

`spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-spec-tokens.test.sh · covers AC1 · scratch repos whose conf sets, blanks and holds out the key beside a spec whose criteria run out of order, its failing case staged by a checker copy whose join ignores the key · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 27 to 35's id 22
  (HIGH, item D-6).

## 10. Reuse audit

The seams extended are `tools/check-spec-tokens.py`'s dated joins, each reading `SPEC_DATE` (`:896`,
bound from `design_lib.SPEC_FILE_DATE`) and a key through `read_cutoff_key` (`:736`), and the specced
predicate of TOOL-dSafePassage-26 S45 and key of TOOL-dSafePassage-34. `python tools/codebase-map/reuse_lookup.py
"first commit that carries a new spec join also carries its cutoff key"` ranked `key`, `keys`,
`build_commit` and `read_conf_key` (`tools/check-spec-tokens.py`); the last is the conf reader under
`read_cutoff_key`, so the hits and the source agree on the seam.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's promoted repairs are placed and sequenced after the unit they repair" --terms "spec audit promoted repair unit order edges hands-off consumes-from minors batch disposal rescope"`
