---
slug: dGaugedVintage
node: d
opened: 2026-09-01
streams: deployer
roster: DEPL
ids: DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11
---

# dGaugedVintage — the second inCMS dossier, triaged against this tree

## The problem this build exists to solve

The owner asked whether an inbound adoption audit from `d41ly/incms` yields fixes that would
simplify updating or adopting this repo's kits. Answering it needed the document's claims measured
against THIS tree, because most are about the adopter's own fork. Eleven real defects came out; nine
were unrecorded. The evidence is
[the triage](build/2026-09-01-build-dGaugedVintage-1-incms-dossier-triage.md), which cites this tree
rather than the document's. Each defect carries a spec, and they are being built in order.

## Expected improvements

- Eleven cited defects arrive specced, so the next session builds rather than re-deriving.
- `DEPL-dGaugedVintage-8` names why the mechanical update path did not answer: it leaves half the
  adopter's receipt ungraded and moves the anchor anyway.
- Seven wrong claims about this tree stop propagating into a third dossier.

## Detriments if this is not built

- The next adopter audit repeats a five-lens manual comparison a verb should answer.
- The receipt keeps re-stamping forward over rows it never graded, so they get harder to attribute.
- "inCMS is a hand fork with no receipt" survives a third time, having already survived two.

## Build-level rules

**Every unit observes its own failing case FIRST.** A gate seen only to pass asserts nothing, so no
unit closes until its RED has been reproduced on the pre-fix binary and recorded in its ledger. Two
of the first three REDs did not fire on the first attempt and both misfires are in the ledgers.

**A spec may narrow at build time, and three have.** Reading the code before writing it has found a
premise wrong in `-8`, `-3` and `-9`. When that happens the spec is revised and the reason logged in
its §9 before any code is written, rather than building to a plan already known to be false.

**Build order is the `order` verb** on each spec, rendered below; `-4`/`-5`, `-1`/`-9` and
`-10`/`-11` are parallel pairs.

**The inbound document is not carried in.** It cites 43 rooted-looking paths and 34 name files
absent here. `DEAD_PATH_PIN` is `0` and hygiene check 15 demands set equality against an empty
registry, so carrying it in would red the bar or cost 34 waiver rows for citations that are correct
in the repo that wrote them.

**Findings are two readings, not refuted ones.** Five lenses measured; all five returned; the
orchestrator re-read every cited line. The skeptic pass did not run, and the triage says so rather
than letting a reader assume adversarial confidence.

**A premise this build itself got wrong.** Its first commit repeated the document's claim that inCMS
is a hand fork with no receipt. It carries a schema-3 govkit receipt. Both earlier commits are left
in history with their reasoning intact.

## Parked decisions

**For the owner.** `DEPL-dGaugedVintage-2` asks for a status sweep this build declined to make:
`DEPL-dCarriedReceipt-1` through `-15` read SPECCED while their specs read CLOSED. Fifteen status
flips across a build this session did not build carry their own judgement calls.

**Unmeasured**, and named rather than left implicit: whether `-3`'s rule precedence behaves as its
descriptor comment says when driven through `resolve_entry`; whether a genuinely receipt-less tree
can be brought under the probe end-to-end; how many of the adopter's 59 `not-installed` rows are
renames rather than non-adoption; and the behavioural content of the ~1,900 upstream lines the
document scopes as a pull.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `DEPL-dGaugedVintage-8` | CLOSED | a way out of `unattributed`, and a stamp that cannot outrun it |
| 2 | `DEPL-dGaugedVintage-3` | CLOSED | a default kit stops reporting adopted while landing no program |
| 3 | `DEPL-dGaugedVintage-4` | OPEN | derive each kit's marker population, assert every site |
| 4 | `DEPL-dGaugedVintage-5` | OPEN | the five entries carrying no readable marker gain one |
| 5 | `DEPL-dGaugedVintage-1` | OPEN | `selfcheck` asserts the version constant actually ships |
| 6 | `DEPL-dGaugedVintage-9` | OPEN | report the per-kit version delta the receipt already stores |
| 7 | `DEPL-dGaugedVintage-10` | OPEN | refuse to measure from a gov checkout stale against its remote |
| 8 | `DEPL-dGaugedVintage-11` | OPEN | the relocate rung survives a kit that fans out |
| 9 | `DEPL-dGaugedVintage-7` | OPEN | the prefix ratchet counts literals, not lines |
| 10 | `DEPL-dGaugedVintage-6` | CLOSED | drift-audit's install block stops contradicting itself |
| 11 | `DEPL-dGaugedVintage-2` | OPEN | fifteen backlog rows reconciled against their CLOSED specs |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 11 unit(s) · node d · opened 2026-09-01 · streams deployer
ids DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-dGaugedVintage-8 — the stamp must not outrun the rows it never graded](spec/2026-09-01-spec-DEPL-dGaugedVintage-8.md) | 1 | 2 | CLOSED | rev-4 | 2026-09-01 |
| [DEPL-dGaugedVintage-3 — a default kit must not report adopted while landing no program](spec/2026-09-01-spec-DEPL-dGaugedVintage-3.md) | 2 | 2 | CLOSED | rev-3 | 2026-09-01 |
| [DEPL-dGaugedVintage-4 — derive each kit's marker population, and assert every site in it](spec/2026-09-01-spec-DEPL-dGaugedVintage-4.md) | 3 | 2 | OPEN | rev-2 | 2026-09-01 |
| [DEPL-dGaugedVintage-5 — five entries an adopter cannot read a version out of](spec/2026-09-01-spec-DEPL-dGaugedVintage-5.md) | 3 | 2 | OPEN | rev-2 | 2026-09-01 |
| [DEPL-dGaugedVintage-1 — a version constant an adopter never receives](spec/2026-09-01-spec-DEPL-dGaugedVintage-1.md) | 4 | 2 | OPEN | rev-2 | 2026-09-01 |
| [DEPL-dGaugedVintage-9 — report the per-kit version delta, once the stored half stops lying](spec/2026-09-01-spec-DEPL-dGaugedVintage-9.md) | 4 | 2 | OPEN | rev-2 | 2026-09-01 |
| [DEPL-dGaugedVintage-10 — a stale measurer reports every row current](spec/2026-09-01-spec-DEPL-dGaugedVintage-10.md) | 5 | 2 | OPEN | rev-2 | 2026-09-01 |
| [DEPL-dGaugedVintage-11 — the relocate rung goes quiet exactly where a kit fans out](spec/2026-09-01-spec-DEPL-dGaugedVintage-11.md) | 5 | 2 | OPEN | rev-2 | 2026-09-01 |
| [DEPL-dGaugedVintage-7 — a ratchet that counts lines cannot see a swapped literal](spec/2026-09-01-spec-DEPL-dGaugedVintage-7.md) | 6 | 2 | OPEN | rev-2 | 2026-09-01 |
| [DEPL-dGaugedVintage-2 — fifteen rows that outlived their specs](spec/2026-09-01-spec-DEPL-dGaugedVintage-2.md) | 7 | 1 | OPEN | rev-1 | 2026-09-01 |
| [DEPL-dGaugedVintage-6 — an install block whose second line cannot run](spec/2026-09-01-spec-DEPL-dGaugedVintage-6.md) | 7 | 1 | CLOSED | rev-3 | 2026-09-01 |
<!-- /gen:build-units -->

Records: 5 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
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
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
