# TOOL-dSafePassage-34 — the `ac-order` join ships under a dated cutoff, over a population measured at HEAD with every current hit disposed

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 7 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-34-deviation-80.md](../build/2026-10-23-build-TOOL-dSafePassage-34-deviation-80.md) | deviation | — |
| [2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-32 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-33 TOOL-dSafePassage-31 TOOL-dSafePassage-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
confirmed finding **id 29** at HIGH, its item **D-7**. TOOL-dSafePassage-26 S45 adds an `ac-order` join
to `tools/check-spec-tokens.py` over every live spec in the repo, with no cutoff key, and its AC43
says that over this build's live specs it names none. This unit's probe ported `LIVE`, `AC_HEAD` and
`AC_LABEL` (`tools/check-spec-tokens.py:299`, `:334`, `:338`) over `git ls-files 'memory/**/*spec*.md'`
at `c9675455` and printed `live 61 out-of-order 2`, as the report's skeptic did:
`memory/builds/aPacedTurnstile/spec/2026-08-20-spec-TOOL-aPacedTurnstile-14.md` lists AC11 before
AC10, and TOOL-dSafePassage-8 lists AC9 before AC8. S45 says TOOL-dSafePassage-8's order "does not
change", and the other spec is another build's, which this build's writes rule does not let it edit.
Built as written, the unguarded `spec tokens (a spec's own names resolve)` leg goes red over the
whole bar. This unit is id 29's promotion: the join is armed by a dated key in the established
`SPEC_*_CUTOFF` form, its population is stated as measured, and each current hit is disposed by name.

## 2. Scope (IN)

- **S1** — The key. `.memory-tree.conf` gains `SPEC_AC_ORDER_CUTOFF="2026-10-23"` with a comment block
  in the form its sibling cutoffs carry, and `tools/check-spec-tokens.py` reads it through
  `read_cutoff_key` and `check_cutoff_value` (`tools/check-spec-tokens.py:736-760`) as
  `AC_ORDER_KEY`. The join grades a LIVE spec whose filename date is on or after the key; blank turns
  it off; a value that is not an ISO date is refused like every other cutoff. Observed by AC1 and AC2.
- **S2** — The population, stated. At `c9675455` the live specs dated on or after 2026-10-23 are this
  build's 25 (PINNED, the probe of §1), and the join reports the graded count on its line of every run,
  so an empty population is visible. Observed by AC3.
- **S3** — TOOL-dSafePassage-8, disposed. It is dated 2026-10-23, so it is graded. When this unit's
  pass runs and TOOL-dSafePassage-8's status is still live, its AC8 bullet moves above its AC9 bullet,
  labels and text unchanged, as a rev bump of that spec with its §9 line; every citation of the two
  labels holds because no label changes. When its status is terminal, it is outside `LIVE` and needs
  nothing. TOOL-dSafePassage-26 S45's sentence that its order "does not change" is superseded by this
  item. Observed by AC3.
- **S4** — TOOL-aPacedTurnstile-14, disposed. It is dated 2026-08-20, before the key, so it is held
  ungraded and its build is not written to. Observed by AC4.
- **S5** — TOOL-dSafePassage-26's AC43, read. Its second clause, "over this build's live specs it
  names none", is read as AC3 of this unit, over the population S2 states. Observed by AC3.

## 3. Non-goals (OUT)

- The join's predicate, which TOOL-dSafePassage-26 S45 defines and this unit keeps.
- Renumbering any spec's criteria. Moving a bullet keeps every citation; renumbering would not.
- Filing an ask in another build for TOOL-aPacedTurnstile-14's order. Held below the key, it reds
  nothing.

### Edges

- **consumes-from** `TOOL-dSafePassage-26` — the `ac-order` join of `tools/check-spec-tokens.py` and its scratch arm; without them there is no join to arm by a key
- **hands-off** `TOOL-dSafePassage-41` — the `ac-order` join itself, with AC1, AC3 and the arm covering AC1, built at that unit's pass reading this unit's key: this unit's pass declares, reads and validates `AC_ORDER_KEY` with nothing yet graded by it, the repair of finding 22 of the spec audit of units 27 to 35
- **hands-off** `TOOL-dSafePassage-42` — finding 21 of the spec audit of units 27 to 35, the `cutoff_keys_armed` raise this unit's key costs; finding 7, TOOL-dSafePassage-8's spec in this unit's `--dispatch --writes` when S3 edits it; and finding 20, `SPEC_DATE` as the date the join reads

## 4. Design

### Data model

```
# .memory-tree.conf
SPEC_AC_ORDER_CUTOFF="2026-10-23"   # date; a LIVE spec dated >= this has its §6 labels ascend; blank = off
```

The join's run line names the key's value and the graded count, the shape the other dated joins of
`tools/check-spec-tokens.py` print.

### Why 2026-10-23

It is the earliest date that grades this build's own specs, where the join is born, and it holds every
older live spec out, among them the one another build owns. A later date would grade nothing at HEAD,
and a join seen grading nothing is not a gate.

### Inventory

Minted: the conf key `SPEC_AC_ORDER_CUTOFF`; the constant `AC_ORDER_KEY` in
`tools/check-spec-tokens.py`. No function, gate leg or policy key.

### Migration

None: the key arms a join that does not exist before TOOL-dSafePassage-26 lands.

### Rollout

Live at landing. It builds at order 7, after TOOL-dSafePassage-26 (order 6), whose join it arms.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `.memory-tree.conf`
- `memory/map/features/spec-tokens.md`

### Alternatives rejected

- **No key, renumbering both specs.** It writes into another build's spec, which this build's writes
  rule forbids, and renumbering breaks every citation of the moved labels.
- **A waiver row per hit.** A join born with a waiver on its first day grades the waiver, and the
  dated key is the corpus's established form for a new demand.
- **A cutoff after 2026-10-23.** It grades an empty population at HEAD.

## 5. Production-readiness checklist

- security: N/A — a spec-text join.
- perf / scale: one date compare per live spec.
- error / empty / loading states: a malformed key is refused before grading; the graded count rides
  every run line.
- observability: the run line names the key and the count.
- risks: a spec dated before the key keeps an out-of-order list; it is graded by nobody, which the
  conf comment states.
- testing: the scratch arm of §7.
- migration: none.
- user docs: N/A — `memory/map/features/spec-tokens.md` names the key beside its siblings; no `help/`
  page covers the checker.

## 6. Acceptance criteria

- **AC1** — When `tools/check-spec-tokens.py` runs over a scratch repo whose conf sets
  `SPEC_AC_ORDER_CUTOFF` to a date and whose live spec at that date lists `AC2` before `AC1`, it names
  the spec and `AC2`; with the key blank it names nothing; with the spec dated a day before the key it
  names nothing.
  Red when: the join grades a spec the key holds out, or stays armed when the key is blank.
- **AC2** — When the same scratch conf sets `SPEC_AC_ORDER_CUTOFF="2026-9-8"`, the run refuses naming
  the key as not an ISO date.
  Red when: a malformed key reads as off or as armed.
- **AC3** — When `python tools/check-spec-tokens.py` runs over the tree after the pass, its
  `ac-order` line names no spec and states a graded count of at least this build's live specs.
  Red when: TOOL-dSafePassage-8 is live and still lists AC9 before AC8, or the count is zero.
  figure: the count is DERIVED by the run; 25 was measured at `c9675455`.
- **AC4** — When `git grep -n -e "SPEC_AC_ORDER_CUTOFF" -- .memory-tree.conf memory/map/features/spec-tokens.md`
  runs, the conf prints the dated key and its comment, and the features page names it.
  Red when: the join is armed by no declared key.

## 7. Gates

`spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 · scratch repos whose conf sets the key, blanks it and malforms it, beside a spec dated before it, its failing case staged by a checker copy that ignores the key · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit of units 15 to 26's
  id 29 (HIGH, item D-7).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-41`, `TOOL-dSafePassage-42`; no other section moved.

## 10. Reuse audit

The seam extended is `tools/check-spec-tokens.py`'s dated-key reader, `read_cutoff_key` with
`check_cutoff_value` (`:736-760`), which every one of its dated joins already uses, and the
`SPEC_*_CUTOFF` declarations of `.memory-tree.conf`, `SPEC_HANDOFF_CUTOFF` (`:973`) among them.
`python tools/codebase-map/reuse_lookup.py "cutoff key for a spec join"` ranked `read_conf_key`
(`tools/check-spec-tokens.py`), `read_spec_revisions` and `read_design_keys`, and the first is the
conf reader this seam sits on, so the hits and the source agree.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
