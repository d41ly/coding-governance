# TOOL-dTotalRecall-62 — unit 52 judges the merged legacy home at the run's real base and builds no `absorbs` read, so its own pass is green

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 28 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 54 to 60
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md`)
confirmed finding **id 2 at HIGH**, its item **H2**, alone in that item. `TOOL-dTotalRecall-52`
(order 28) AC2 requires `compare_to_base` at the pass base to name a planted extra `causes` row
`gained`. The pass base `462d20f3` holds neither legacy home, so the factory reads the merged home as
a first seed (`TOOL-dWitnessedBar-51` S30) and AC2 can never see `gained`, as
`TOOL-dTotalRecall-59` §1 itself records. Unit 52's AC3 requires no carrier of `legacy-records` under
`tools`, yet its own S2 and §4 write `absorbs = [{ population = "legacy-records", ... }]` into
`tools/memory-tree/kit.toml`. Unit 59, which cuts that line, builds at order 29. So both criteria are
red at unit 52's own pass, and no later step can make that pass green.

The defect sits in the hand-off from `TOOL-dTotalRecall-43` S19, which merges the two ledgers on the
premise that the merged home is judged against a base holding the absorbed one, to unit 52, which
builds a read for that premise. This unit amends unit 52 in the step it sits in, ahead of its pass by
a declared edge, so it builds no `absorbs` field and its AC2 observes the first-seed reading the real
base gives. Unit 59 keeps its fixture proof of `shrink-only` and observes the field absent. It repairs
`TOOL-dTotalRecall-43`.

## 2. Scope (IN)

- **S1** — Unit 52 builds no base re-key. `TOOL-dTotalRecall-52`'s S2 takes §4's text, its §4
  registration block carries no `absorbs` line, and its Inventory, Files touched, §5 and §7 New arm
  carry nothing for the field. Observed by AC1 and AC2.
- **S2** — Unit 52's AC2 reads the real base. It is restated as the first-seed reading
  `compare_to_base` gives at the run's merge-base, and its title and §1 say why. Observed by AC1 and
  AC2.
- **S3** — Unit 59 observes the field absent. Its S2 states that unit 52 builds no `absorbs`, its AC2
  stands as the observation of that, and its title, §4, §5 and consumes-from line carry no cut. Its S1
  and S3, the fixture proof, stand. Observed by AC1 and AC3.
- **S4** — The amendments land before unit 52's pass, each a rev bump with its §9 line naming this
  unit, in this unit's pass at order 28, which unit 52 and unit 59 consume by §3 edges. Observed by AC1.

## 3. Non-goals (OUT)

- The triple key and the old name's carriers: unit 52's S1 and S3, unchanged.
- The factory's first-seed rule: `TOOL-dWitnessedBar-51` S30's, observed and not changed.
- The window in which a first seed refuses nothing: the batch `TOOL-dTotalRecall-66` bounds it for
  the round-1 audit's id 37.
- Any code. This unit writes spec text only.

### Edges

- **hands-off** `TOOL-dTotalRecall-52` — S2, AC2 and the registration block amended so that unit
  builds no `absorbs` field and reads the first seed at its pass base
- **hands-off** `TOOL-dTotalRecall-59` — S2 amended to observe `absorbs` absent, its fixture proof of
  `shrink-only` kept
- **hands-off** `TOOL-dTotalRecall-66` — unit 52's restated AC2, which that unit re-observes for the
  round-1 audit's id 32

## 4. Design

### The amendments to unit 52

Each is a rev bump with a §9 line of the form
`rev-<N> · <date> · S2 AC2 §1 §4 §5 §7 · amended by TOOL-dTotalRecall-62 (id 2, item H2) ...`.

- Title: "the one legacy registration is keyed by path, section and check, judged at the run's real
  base, and leaves no carrier of the old name".
- §1 gains, after its account of unit 43 S19: "At this run's compare base `462d20f3` neither home
  exists, so the factory reads the merged home as a first seed and names no `gained` key; no base
  re-key is built (`TOOL-dTotalRecall-62`)."
- S2:

  > **S2** — The judgement at the run's base. `compare_to_base` reads the merged home at the run's
  > merge-base as a first seed, every row `seeded`, and names no `gained` key. The registration
  > carries only the factory's own fields. Observed by AC2.

- §4: the registration block ends at `direction = "shrink-only"`, and the paragraph under it is
  struck. Inventory reads "Minted: nothing in the factory; the `check` values `kind-schema` and
  `causes`." Files touched carries no `tools/lib/legacy_ledger.py`.
- §5: perf / scale reads "none: one home, read once"; error states "a first seed prints its line";
  observability "`compare_to_base` prints `first seed record-kinds-legacy <n> rows`"; risks "none
  beyond the first-seed window, which the batch `TOOL-dTotalRecall-66` bounds".
- AC2:

  > When a `python -c` probe run from `tools/lib/` calls `compare_to_base` from `legacy_ledger.py` for
  > `record-kinds-legacy` at the pass tip, it prints `first seed record-kinds-legacy` with the working
  > row count and names no `gained` key. Red when: it names a `gained` key, or the registration
  > carries a field the factory's grammar lacks.

- §7: the New arm line over `tools/lib/legacy_ledger.py` is struck; `TOOL-dTotalRecall-59`'s arm
  proves `shrink-only` on a fixture base.
- §3: the hands-off to unit 59 reads "the merged registration, whose `shrink-only` judgement that
  unit proves on a fixture base holding the merged home".

### The amendments to unit 59

- Title: "the merged legacy registration is judged at the run's real compare base, a first seed, and
  its `shrink-only` is proved on a fixture base that holds it".
- §1 ends: "Unit 52 builds no `absorbs` field (`TOOL-dTotalRecall-62`), so this unit grounds the
  judgement on the real base and proves `shrink-only` on a fixture base."
- S2:

  > **S2** — `absorbs` is absent. Unit 52 builds no such field, so the registration and the factory
  > carry none. Observed by AC2.

- §4: the Inventory's "Deleted" sentence is struck; Files touched carries no
  `tools/memory-tree/kit.toml`; §5 security reads "no new surface". The New arm's "it replaces unit
  52's absorbed-population arm" clause is struck.
- §3: the consumes-from line to unit 52 reads "the merged registration, judged here at the real base
  and on a fixture base".

### Inventory

Minted: nothing in code. Amended: the two spec files below.

### Files touched (estimate)

- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-52.md`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-59.md`

### Alternatives rejected

- **Leave unit 52 as written and repair after it.** Its AC2 and AC3 are red at its own pass.
- **Move unit 59's fixture into unit 52.** Unit 52's AC2 would then prove `shrink-only` too, but the
  fixture and its arm are unit 59's design, and two units designing one arm is H3's defect.
- **Keep `absorbs` for a later base.** `legacy-records` never reaches `main`, because unit 52 S3
  deletes its home on the run branch, so no base the field could read will exist.

## 5. Production-readiness checklist

- security — no surface: spec text only.
- perf / scale — none.
- error / empty / loading states — none at runtime; a missing amendment is AC1's red.
- observability — each amended spec's §9 line names this unit and the finding.
- risks — the two specs' revs move after their audit; their new text is this spec's §4, which the
  audit of this unit reviews.
- testing — AC1 by the pass; AC2 at unit 52's pass; AC3 at unit 59's pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `grep -n "absorbs = "` runs over
  `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-52.md` at this pass's tip it
  prints nothing, `grep -c "first seed record-kinds-legacy"` over the same file prints at least 1, and
  `grep -c TOOL-dTotalRecall-62` over the §9 of units 52 and 59 prints at least 1 for each.
  Red when: unit 52 still designs the field or still asks for `gained` at its pass base.
- **AC2** — When unit 52's pass tip is reached, the probe of its restated AC2 prints
  `first seed record-kinds-legacy` and names no `gained` key, and
  `git grep -n "legacy-records" -- tools .memory-tree.conf memory/project` prints nothing.
  Red when: unit 52's AC2 or AC3 is red at its own tip.
- **AC3** — When unit 59's pass tip is reached, its AC3 fixture names the planted `causes` key
  `gained` and, with the row removed, names none, and `git grep -n absorbs -- tools/memory-tree/kit.toml`
  prints nothing.
  Red when: `shrink-only` goes unproved, or the field appears at any step.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: this unit writes spec text, and unit 59's arm proves the judgement.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 54 to 60, id 2
  (HIGH, item H2).

## 10. Reuse audit

The seam is the ledger factory's own base read, `compare_to_base` at `resolve_compare_base`
(`tools/codebase-map/map_lib.py:1502`), with its first-seed rule (`TOOL-dWitnessedBar-51` S30): unit
52 reads it as it is and adds no field. `git merge-base HEAD origin/main` printed `462d20f3` here, the
base unit 59 §1 measured. `python tools/codebase-map/reuse_lookup.py "amend a sibling spec before its unit builds"`
ranked name-stem neighbours and no seam for sequencing an amendment, so no existing seam fits beyond
the factory read named here.

Recall terms used: `python tools/memory-recall/query.py "how does a repair land before the unit whose own pass it must make green" --terms "order repair promoted spec-audit step hands-off consumes-from amendment rev-bump pass tip supersede"`
