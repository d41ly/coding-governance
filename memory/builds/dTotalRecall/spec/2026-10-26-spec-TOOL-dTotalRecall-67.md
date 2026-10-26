# TOOL-dTotalRecall-67 — unit 61's amendments to units 55, 56 and 57 are read by their own text at step 20, and any it left unwritten is written before those units build

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 20 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 |
| [2026-10-26-build-TOOL-dTotalRecall-67-round5-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-67-round5-fix-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-67-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-67-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-67-round5-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-67-round5-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 61 to 66
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, its item **H1**, alone in that item. `TOOL-dTotalRecall-61`
(order 19) amends the specs of units 53, 55, 56 and 57, and its AC1 is meant to observe that. Its
§9 half counts lines naming `TOOL-dTotalRecall-61` in each amended spec's §9, and the round-4
hands-off fold (`c235c2e05`) already wrote such a line into units 53, 55, 56 and 57: the edge-mirror
line "the Edges block gains the mirror of TOOL-dTotalRecall-61". So that half is green before
unit 61's pass. Its only text probe reads unit 53. A unit-61 pass that amends unit 53 alone meets
AC1, and units 55, 56 and 57 then build at order 30 from unamended text. The first red is unit 61's
AC3, at unit 57's tip, after units 55 and 56 have built.

This unit reads each amendment unit 61 writes into specs 55, 56 and 57 by a string of the
amendment's own text, every one of which prints 0 at this spec's writing. A string that still
prints 0 at this pass's base names an amendment unit 61's pass left unwritten, and this pass writes
it from unit 61's §4, verbatim. It repairs `TOOL-dTotalRecall-61`, at step 20, one above that
unit's order and ten steps ahead of units 55, 56 and 57.

## 2. Scope (IN)

- **S1** — The observation. At this pass's base, the joined-text probe of §4 runs over the specs of
  units 55, 56 and 57 for each string in §4's table, and for the §9 form
  `amended by TOOL-dTotalRecall-61` in each of the three. Each count is recorded before anything is
  written. Observed by AC1 and AC3.
- **S2** — The completion. For a string that prints 0, this pass writes the amendment it belongs to,
  copied from `TOOL-dTotalRecall-61` §4 word for word. Each write is a rev bump on that spec, with a
  §9 line `amended by TOOL-dTotalRecall-67 for TOOL-dTotalRecall-61 (id 1, item H1)`. Unit 57's edge
  to unit 56 is written with its mirror in unit 56's §3. Observed by AC1 and AC2.
- **S3** — The record. This unit's acceptance-ledger line for AC1 names each string's count at the
  pass base. A gap unit 61's pass left therefore shows in the record, and is not repaired silently.
  Observed by AC3.

## 3. Non-goals (OUT)

- Editing unit 61's spec. It lands at order 19, one step before this pass, and a landed spec is
  frozen.
- Unit 61's unit-53 half. That half's text probe, `stays in its constant at this pass`, prints 0 at
  this spec's writing, so it is not pre-green.
- The same defect in units 62, 63 and 64 at MEDIUM (ids 2, 9 and 31, item M1): the batch
  `TOOL-dTotalRecall-70`.
- Any code. This unit reads and writes spec text only.

### Edges

- **consumes-from** `TOOL-dTotalRecall-61` — the amendment text of its §4 and its pass at step 19; without them there is nothing to read or to copy
- **hands-off** `TOOL-dTotalRecall-55` — S2 and AC1 as unit 61 amends them, read here by their own text and written here if absent, before that unit's pass
- **hands-off** `TOOL-dTotalRecall-56` — S2, its new criterion and its hands-off to unit 57, read and written the same way before that unit's pass
- **hands-off** `TOOL-dTotalRecall-57` — its consumes-from edge to unit 56 and its sequencing line, read and written the same way before that unit's pass
- **hands-off** `TOOL-dTotalRecall-70` — the strings of §4's table, which that unit re-reads at the tip against the text each unit built from (id 31)

## 4. Design

### The probe

Every count is taken over joined text, never over lines. A wrapped phrase never matches a line-wise
grep, the defect the same audit graded as id 10:

```bash
python -c "import re,sys; t=re.sub(r'\s+',' ',open(sys.argv[1],encoding='utf-8').read()); print(t.count(sys.argv[2]))" <spec> "<string>"
```

Run from `memory/builds/dTotalRecall/spec/`.

### The strings

| Spec | Amendment, from unit 61 §4 | String |
|---|---|---|
| 55 | S2's added sentence | `whose last rows they are after unit 53` |
| 55 | AC1's added clause | `git grep -n CAUSE_WRITER_KEPT -- tools` |
| 56 | S2's added sentence | `whose last row it is after unit 53` |
| 56 | its added criterion | `git grep -n ALIAS_COMPARE_KEPT -- tools` |
| 57 | §3's edge | ``**consumes-from** `TOOL-dTotalRecall-56` `` |
| 57 | §4's sequencing line | `this one follows units 55 and 56` |

PINNED, measured 2026-10-26 at `653bed738`: each string prints 0 over its spec, and so does
`amended by TOOL-dTotalRecall-61` over each of the three. Over
`2026-10-26-spec-TOOL-dTotalRecall-61.md` the first five strings and the §9 form print 1 each. That
is the probe's liveness: it reads a positive where the text is.
The edge string prints 0 there too, because unit 61 §4 describes that edge rather than spelling it.
So a missing edge is written in the template's bullet shape (`memory/TEMPLATE-SPEC.md`, "§3 Edges").

### Why order 20

The amendments must be present before units 55, 56 and 57 build at order 30. They can only be
checked after unit 61 writes them at order 19. Step 20 is the first step after that, and no pass
between steps 20 and 29 reads these three specs.

### Inventory

Minted: nothing in code. Amended, only where S1 finds a gap: the specs of units 55, 56 and 57.

### Files touched (estimate)

- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-55.md`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-56.md`
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-57.md`
- `memory/builds/dTotalRecall/build/` (this unit's acceptance-ledger line)

### Alternatives rejected

- **Amend unit 61's AC1.** Unit 61 builds at order 19, before this unit. A spec changed after its
  pass is a departure (the same audit's id 5), and the corrected criterion would still run at step
  19 against the gap.
- **Count §9 lines naming unit 61.** The edge-fold lines already match that count, which is the
  defect.
- **Place the check at order 30, with units 55 to 57.** A unit sharing their step cannot precede
  them without a §3 edge each way, and those units would still read unamended text if the check ran
  last.

## 5. Production-readiness checklist

- security — no surface: spec text only.
- perf / scale — eighteen string counts over three files.
- error / empty / loading states — a string that prints 0 is a gap S2 fills. A file the probe cannot
  open is a red, never a 0.
- observability — the ledger line of S3 names every base count.
- risks — S2 copies text that unit 61's own audit reviewed. A copy that differs from unit 61 §4 is
  the risk, and AC1 reads the copied strings.
- testing — AC1 and AC3 by the pass; AC2 at unit 57's pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When the probe of §4 runs at this pass's tip over each spec in §4's table, every string
  prints at least 1. `amended by TOOL-dTotalRecall-61` or `amended by TOOL-dTotalRecall-67` prints
  at least 1 in each of the three specs.
  Red when: an amendment unit 61 §4 names is absent from the spec it amends.
  figure: the base counts are PINNED in §4, measured 2026-10-26; the tip counts are DERIVED by the
  probe at the pass.
- **AC2** — When the pass commits of units 55, 56 and 57 are reached,
  `git merge-base --is-ancestor <this unit's pass commit> <each one>` exits 0 for each, the pass
  commit of a unit being `git log --reverse --format=%H --grep='^Pass: <unit id>$' 462d20f3..HEAD`'s
  first line.
  Red when: a unit of order 30 builds before this pass.
- **AC3** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-67" -- memory/builds/dTotalRecall/build`
  runs after the pass, it prints the ledger block, and that block's AC1 line names a base count for
  each of the six strings and the three §9 forms.
  Red when: the line names only tip counts, so a gap unit 61 left is invisible.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: this unit writes spec text and a ledger line, and the criteria it restores carry their
units' own arms.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 61 to 66, id 1
  (HIGH, item H1).

## 10. Reuse audit

The seam is unit 61's own §4. Its text is the amendment, and this unit reads and copies it, minting
nothing. The probe is the joined-paragraph reading the audit's fix for id 10 names (`tr '\n' ' '`),
written in Python so that it reads one file and prints one count.
`python tools/codebase-map/reuse_lookup.py "count a phrase in a spec file over joined paragraphs"`
ranked neighbours by name stem only (`counts`, `read_spec_revisions`, `parse_spec_h1`). None counts
a phrase in a spec body. The recall query below found no tool that checks a spec amendment by its
text either. Its hits are the precedents `TOOL-dDerivedDocket-37` and `TOOL-cMendedVintage-19`,
which shape a hands-off's payload and a promotion's placement, and neither reads a sibling spec. No
existing seam fits beyond unit 61's §4.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted repair observe a sibling spec amendment that a hands-off fold already named" --terms "pre-green amendment hands-off fold rev-bump section-9 acceptance grep promoted repair order spec-audit"`
