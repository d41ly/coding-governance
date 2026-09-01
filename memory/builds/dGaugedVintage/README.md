---
slug: dGaugedVintage
node: d
opened: 2026-09-01
streams: deployer
roster: DEPL
ids: DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 DEPL-dGaugedVintage-12 DEPL-dGaugedVintage-13
---

# dGaugedVintage — the second inCMS dossier, triaged against this tree

## The problem this build exists to solve

The owner asked whether an inbound adoption audit from `d41ly/incms` yields fixes that would
simplify updating or adopting this repo's kits. Answering it needed the document's claims measured
against THIS tree, because most are about the adopter's own fork. Eleven real defects came out; nine
were unrecorded. All eleven are specced, reviewed, built and closed. The evidence trail is
[the triage](build/2026-09-01-build-dGaugedVintage-1-incms-dossier-triage.md), the
[round-1 audit](reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md), and one
acceptance ledger per unit under `build/`.

## Expected improvements

- `govkit update` now answers "which of my kits are behind" in one command, and reproduces by
  machine the two releases the inbound audit found by hand.
- A stale measurer, an ungraded stamp, a kit that lands no program and a marker nobody could read
  are each reported where they were silent.
- Seven wrong claims about this tree stop propagating into a third dossier.

## Detriments if this is not built

- The next adopter audit repeats a five-lens manual comparison a verb should answer.
- The receipt keeps re-stamping forward over rows it never graded.
- A default kit keeps reporting adopted while landing no executable file.

## Build-level rules

**Every unit observed its own failing case FIRST**, on the pre-fix binary, and each ledger records
it. Two REDs did not fire on the first attempt — one ran the old engine from a temp dir where its
root resolver could not work, one used a malformed fixture — and both misfires are written down,
because a red that proves nothing is worse than no red.

**A spec may narrow at build time, and five did.** Reading the code before writing it found a premise
wrong in `-8`, `-9`, `-10`, `-11` and `-7`. `-8` shrank the most: two revisions had scoped a
re-attribution pass that already ships as `adopt --re-adopt`.

**An unmet criterion is AMENDED in place, never quietly dropped.** Seven were: `-3` AC6, `-4` AC6,
`-5` AC5, `-9` AC5, `-10` AC5, `-11` AC1, and `-7` AC2 and AC4. `-7` is HALF BUILT and says so.

## Parked decisions

**For the owner.** `-3` §8 F1 asks whether to reverse `DEPL-dCarriedReceipt-10` and seed a `forked`
file at first install. The REFUSAL branch was built, which needs no ratification; the seed branch
stays superseded and needs an owner id. "build it" was read as scope approval, not as that
ratification.

**Filed, not built.** `DEPL-dGaugedVintage-12` is `-7`'s unbuilt identity arm, so a kit path swapped
for another's at equal count still passes. `DEPL-dGaugedVintage-13` gates the class `-2` swept by
hand.

**Unmeasured**, named rather than implied: the fan-out kit count in `-11` is the review lens's and
was not re-derived; `-9`'s absent-`version`-key state is implemented but no receipt in reach
exercises it; and the ~1,900 upstream lines the document scopes as a pull were never read.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `DEPL-dGaugedVintage-8` | CLOSED | a way out of `unattributed`, and a stamp that cannot outrun it |
| 2 | `DEPL-dGaugedVintage-3` | CLOSED | a default kit stops reporting adopted while landing no program |
| 3 | `DEPL-dGaugedVintage-4` | CLOSED | derive each kit's marker population, assert every site |
| 4 | `DEPL-dGaugedVintage-5` | CLOSED | the five entries carrying no readable marker gain one |
| 5 | `DEPL-dGaugedVintage-1` | CLOSED | `selfcheck` asserts the version constant actually ships |
| 6 | `DEPL-dGaugedVintage-9` | CLOSED | report the per-kit version delta the receipt already stores |
| 7 | `DEPL-dGaugedVintage-10` | CLOSED | refuse to measure from a gov checkout stale against its remote |
| 8 | `DEPL-dGaugedVintage-11` | CLOSED | the relocate rung survives a kit that fans out |
| 9 | `DEPL-dGaugedVintage-7` | CLOSED | the prefix ratchet counts literals, not lines |
| 10 | `DEPL-dGaugedVintage-6` | CLOSED | drift-audit's install block stops contradicting itself |
| 11 | `DEPL-dGaugedVintage-2` | CLOSED | fifteen backlog rows reconciled against their CLOSED specs |
| 12 | `DEPL-dGaugedVintage-12` | CLOSED | the prefix ratchet records identity, not only a count |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 12 unit(s) · node d · opened 2026-09-01 · streams deployer
ids DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 DEPL-dGaugedVintage-12 DEPL-dGaugedVintage-13

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-dGaugedVintage-8 — the stamp must not outrun the rows it never graded](spec/2026-09-01-spec-DEPL-dGaugedVintage-8.md) | 1 | 2 | CLOSED | rev-4 | 2026-09-01 |
| [DEPL-dGaugedVintage-3 — a default kit must not report adopted while landing no program](spec/2026-09-01-spec-DEPL-dGaugedVintage-3.md) | 2 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-4 — derive each kit's marker population, and assert every site in it](spec/2026-09-01-spec-DEPL-dGaugedVintage-4.md) | 3 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-5 — five entries an adopter cannot read a version out of](spec/2026-09-01-spec-DEPL-dGaugedVintage-5.md) | 3 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-1 — a version constant an adopter never receives](spec/2026-09-01-spec-DEPL-dGaugedVintage-1.md) | 4 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-9 — report the per-kit version delta, once the stored half stops lying](spec/2026-09-01-spec-DEPL-dGaugedVintage-9.md) | 4 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-10 — a stale measurer reports every row current](spec/2026-09-01-spec-DEPL-dGaugedVintage-10.md) | 5 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-11 — the relocate rung goes quiet exactly where a kit fans out](spec/2026-09-01-spec-DEPL-dGaugedVintage-11.md) | 5 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-7 — a ratchet that counts lines cannot see a swapped literal](spec/2026-09-01-spec-DEPL-dGaugedVintage-7.md) | 6 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-2 — fifteen rows that outlived their specs](spec/2026-09-01-spec-DEPL-dGaugedVintage-2.md) | 7 | 1 | CLOSED | rev-2 | 2026-09-01 |
| [DEPL-dGaugedVintage-6 — an install block whose second line cannot run](spec/2026-09-01-spec-DEPL-dGaugedVintage-6.md) | 7 | 1 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-12 — the prefix ratchet records identity, not only a count](spec/2026-09-01-spec-DEPL-dGaugedVintage-12.md) | 8 | 2 | CLOSED | rev-2 | 2026-09-01 |
<!-- /gen:build-units -->

Records: 14 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-dGaugedVintage-12.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-dGaugedVintage-8` | no |
| 2 | `DEPL-dGaugedVintage-3` | no |
| 3 | `DEPL-dGaugedVintage-4`, `DEPL-dGaugedVintage-5` | yes |
| 4 | `DEPL-dGaugedVintage-1`, `DEPL-dGaugedVintage-9` | yes |
| 5 | `DEPL-dGaugedVintage-10`, `DEPL-dGaugedVintage-11` | yes |
| 6 | `DEPL-dGaugedVintage-7` | no |
| 7 | `DEPL-dGaugedVintage-2`, `DEPL-dGaugedVintage-6` | yes |
| 8 | `DEPL-dGaugedVintage-12` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
