---
slug: dGaugedVintage
node: d
opened: 2026-09-01
status: OPEN
streams: deployer
roster: DEPL
ids: DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11
---

# dGaugedVintage — the second inCMS dossier, triaged against this tree

## The problem this build exists to solve

The owner asked whether an inbound adoption audit from `d41ly/incms` yields fixes that would
simplify updating or adopting this repo's kits. Answering it needs the document's claims measured
against THIS tree, because most of them are about the adopter's own fork. Eleven real defects came
out; nine were unrecorded. The evidence is
[the triage](build/2026-09-01-build-dGaugedVintage-1-incms-dossier-triage.md), which cites this tree
rather than the document's. This build authors no product change and no spec.

## Expected improvements

- The next session reads eleven cited defects instead of re-deriving a cross-repo comparison by hand.
- `DEPL-dGaugedVintage-8` names why the mechanical update path did not answer: it leaves half the
  adopter's receipt ungraded and moves the anchor anyway.
- Six wrong claims about this tree stop propagating into a third dossier.

## Detriments if this is not built

- The next adopter audit repeats a five-lens manual comparison a verb should answer.
- The receipt keeps re-stamping forward over rows it never graded, so they get harder to attribute.
- "inCMS is a hand fork with no receipt" survives a third time, having already survived two.

## Build-level rules

**No product change.** No edit to `govkit.py`, to any `kit.toml`, to the runbook, or to a gate leg.
Each of the eleven is a follow-up unit, and the two wanting new assertions owe a failing case
observed before they land.

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

*No unit is planned under this build; its output is eleven backlog rows and the triage record.*

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-09-01 · streams deployer
ids DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
