---
slug: aFerriedDossier
node: a
opened: 2026-08-16
status: OPEN
streams: deployer
roster: DEPL
ids: DEPL-aFerriedDossier-1 DEPL-aFerriedDossier-2 DEPL-aFerriedDossier-3
---

# aFerriedDossier — an adopter's dossier, carried in from inCMS

Node `a` · opened 2026-08-16 · streams deployer.

This build authors no product change. It carries ONE inbound document: what the `d41ly/incms` repo
measured about this repo while deciding whether to migrate its hand-forked kits onto `govkit`. The
three backlog rows it mints are the asks; the report under `build/` is the evidence behind them.

**Why it is a build folder and not a loose file.** The layout rule is that reports live under a
build's own folder, and a document nobody owns is a document nobody services. The slug owns the
three `DEPL` ids so a later unit can close them by citation.

## What inCMS is

A hand-forked adopter. It carries nine kits from this repo at the `scripts/` prefix rather than
`tools/`, copied by hand over months, with no `.governance/` receipt and no record of the commit any
of them came from. Five of its nine forks carry no version constant at all. That makes it an
unusually harsh test target for `govkit`, which is the only reason this dossier is worth the time:
it exercises states the reference installs cannot reach.

Its measurements were taken against gov `96141ae` and against the `aTetheredConvoy` worktree at
`d594bf1`, and re-verified by an adversarial pass before landing here.

## The one finding that is not a defect report

`aTetheredConvoy` gives every govkit-INSTALLED repo an update path and gives a hand-forked repo
nothing. A grep for `adopt-existing|adopt_existing|hand-fork|from-commit|bootstrap` across all seven
of its specs returns zero, and the README's OUT clause "adding kits to an existing install" is
operationalised by unit 2 into a predicate that presupposes a receipt — which is widening an install
that exists, not creating a first one.

That is a scope observation about a build whose own README opens by naming the upgrade-orphan class
it exists to end. It is filed as `DEPL-aFerriedDossier-1` rather than as a review comment, because
every unit is OPEN and the cheapest possible fix — one fixture variant — stops being cheap once
unit 3 is built.

## Open

All three rows. Nothing here has been actioned.

## Work state

Rendered by `gen_build_index.py` from this file's front matter — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-08-16 · streams deployer
ids DEPL-aFerriedDossier-1 DEPL-aFerriedDossier-2 DEPL-aFerriedDossier-3

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records live under `build/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-16-build-aFerriedDossier-1-incms-adopter-handoff.md](build/2026-08-16-build-aFerriedDossier-1-incms-adopter-handoff.md) | — | *none — an adopter handoff carried in from another repo; this build holds no spec for it to serve* |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`build/`**
  - [2026-08-16-build-aFerriedDossier-1-incms-adopter-handoff.md](build/2026-08-16-build-aFerriedDossier-1-incms-adopter-handoff.md)
<!-- /gen:build-docs -->
