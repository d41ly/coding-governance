---
slug: dGaugedVintage
node: d
opened: 2026-09-01
status: OPEN
streams: deployer
roster: DEPL
ids: DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2
---

# dGaugedVintage — the second inCMS dossier, triaged against this tree

Node `d` · opened 2026-09-01 · streams deployer.

This build authors no product change. It answers one question the owner asked of an inbound
document: **are there fixes in it that would simplify updating or adopting this repo's kits?**

The answer is mostly no, and the reason is worth recording: nearly every gov-side implication the
document raises is already built, already recorded, or wrong about this tree. One row is stale, one
assertion is genuinely missing, and the largest single fact is that the adopter ran a five-lens
manual audit to derive what a shipped verb prints.

## The inbound document

inCMS — a hand-forked adopter carrying gov kits at a `scripts/` prefix with no `.governance/`
receipt — audited its own adoption on 2026-09-01, against this repo at `d65da7ab`. `aFerriedDossier`
carried its first dossier in on 2026-08-16; this is its second.

**The document itself is deliberately NOT carried into this tree.** It cites 43 rooted-looking
paths, and 34 of them name files that do not exist here — the adopter's own `scripts/` layout, plus
`.claude/` and `memory/` paths from its tree. `DEAD_PATH_PIN` is `0` and check 15 demands set
equality against an empty registry, so carrying the file in would red the bar or cost 34 waiver rows
for citations that are correct in the repo that wrote them. What is durable about it is the triage
below, which cites this tree instead. Its own location is recorded in the landing commit.

## What the document got wrong about this tree

Each row was checked by reading the named file here, not by reasoning about the claim.

| The document says | Measured here |
|---|---|
| `adopt-memory-recall.sh` / `adopt-drift-audit.sh` are dead pointers | Both are tracked. The adopter did not carry them |
| `push-main.sh` hardcodes `origin/HEAD` and would brick a non-`origin` lander | `tools/push-main.sh:20` reads `GOV_DEFAULT_BRANCH` first, then falls back, then fails CLOSED naming both escapes |
| Fresh `tools/` refs arrive in adopters silently | `tools/check-install-prefix.sh` is a shrink-only ratchet over exactly that class |
| The gov-commit column is a stale batch anchor | It grades `.governance/install.index` — a file gov never writes. Gov's receipt is `install.json`; `install.index` is the fork's own, and gov carries a fixture modelling it |
| So per-file update distance is underivable | Each row carries its own `commit` and `gov_oid` (`tools/govkit/govkit.py:4095`), advanced only on rows actually written (`:5741`, `:5859`, `:5975`) |
| Nothing answers "am I on the latest gov?" | `govkit adopt` measures a receiptless tree against gov history; `update` takes a target rev. Both read-only by default |
| `SKILL.template.md` is carried for two kits and not the other two | All four ship it AND declare it here. The split is the fork's |

The document marked its own `push-main` and prefix claims unverified, and both are among these. Its
"what nothing here measured" section is honest and worth trusting on that point.

## What is actually actionable

**One stale row, and a block behind it**, filed as `DEPL-dGaugedVintage-2`.
`DEPL-aFerriedDossier-1` says a hand-forked adopter gets no update path. Its declared closer,
`DEPL-dCarriedReceipt-13` — "`govkit adopt`, the receipt bootstrap" — has a spec reading CLOSED at
rev-8, 2026-08-26, and the code is in the tree. The runbook carries a section titled for the case.
But the closer's own backlog row still reads SPECCED, as do `DEPL-dCarriedReceipt-1` through `-15`,
so the staleness is a block and not one row. Flipping fifteen statuses across a build this session
did not build is a sweep with its own judgement calls, so it is filed rather than done here.

**One missing assertion**, filed as `DEPL-dGaugedVintage-1`. `selfcheck` check 5 asserts that an
entry's `version_from` file EXISTS in gov and that its pattern matches exactly one line. No arm
asserts that file is inside the entry's own installed population, so a kit could ship without the
constant an adopter pins against. It is latent rather than live: every kit with a `version_from`
file today has an `include` rule covering it, checked one by one. Check 5b compares the registry to
`check-kit-versions.sh` in both directions, but only as `note` — reported, not repaired.

## The fact worth more than either row

The adopter ran a five-investigator manual audit, on 2026-09-01, to hand-derive per-file distance
from gov. `govkit adopt` had shipped on 2026-08-26 and does that by measuring the tree against gov's
own history; `WIRE-INTO-PROJECT.md` §5b is a top-level section titled for precisely this situation —
a tree that already carries kits, bootstrapping its receipt.

Gov is not even unaware of this adopter's shape: `tools/govkit/fixtures/make_incms_receipt.py`
builds a fixture from inCMS's own `install.index` so `selftest.py` can exercise it. The verb, the
runbook section and a fixture for this exact tree all exist.

So this is not a capability gap and not a documentation gap in the ordinary sense. Something about
the path from "I have hand-forked kits and want to update them" to "§5b" did not carry. This build
does not guess at the fix, because the adopter is the only one who can say what they looked at
first. It is recorded here so the next person does not re-derive the whole comparison by hand.

## Non-goals

No change to `govkit.py`, to any `kit.toml`, to the runbook, or to a gate leg. No fix for
`DEPL-dGaugedVintage-1` — that is a follow-up unit, and it owes a failing case observed before it
lands, like any new assertion.

<!-- roster:units -->

*No unit is planned under this build; its output is two backlog rows and the triage above.*

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-09-01 · streams deployer
ids DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 0 bound to this build, across 0 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
