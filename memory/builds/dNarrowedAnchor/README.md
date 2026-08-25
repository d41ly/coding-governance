---
slug: dNarrowedAnchor
node: d
opened: 2026-08-24
streams: tooling
roster: TOOL
ids: TOOL-dNarrowedAnchor-1 TOOL-dNarrowedAnchor-2 TOOL-dNarrowedAnchor-3
---

# dNarrowedAnchor — the second anchor becomes PER-MODE, so a `slug` run cannot reach it

## The problem this build exists to solve
`ANCHOR_SCOPE="published"` is a whole-project switch. It widens `resolve_base` for EVERY run, and the
mode a run declares in `authorized-by:` has no bearing on which anchor it may use. So an adopter who
turns it on to enable the prompt path also, silently, lets a `slug`-mode run author its own build
folder, push its own branch, and be authorized by it. `slug` is the one mode whose definition says
the folder predates the run, so such a run has contradicted its own declaration — and an absent
`authorized-by:` key reads as `slug`, which is every build README written before that key existed.

## Expected improvements
- Turning the key on stops widening every run: only `prompt` and `recipe`, the disciplines that
  author their own build folder, reach the branch anchor.
- Self-authorization can no longer happen by DEFAULT — it requires a mode declared in the file the
  merge bar reads, which the bar records.
- An adopter stops having to write the concession into its own charter, which is what inCMS did at
  `ARCH-dPublishedAnchor-1` because the kit offered no way to scope one.

## Detriments if this is not built
- Every adopter that wants the prompt path buys a `slug` self-authorization path it did not ask for
  and is not told about.
- The cost lands in each adopter's charter separately, so the same concession is re-argued per repo
  and drifts between them.
- A defect an adopter can only document, never scope, is a kit defect wearing an adopter's clothes.

## Build-level rules
- **The admissible set is KIT-OWNED**, with no `.unattended.conf` channel. An adopter-declarable set
  is an adopter-reopenable hole, and there is no project in which a `slug` run legitimately
  authorizes itself off a branch it pushed.
- **`recipe` is IN the set.** `SKILL.template.md` tells a playbook author that writing the build
  folder yourself needs `published`; excluding `recipe` would make this kit refuse a path its own
  carrier instructs.
- **The leg derives, never reads back.** `anchor-kind` is written by the file under inspection, so
  the merge bar answers the anchor question from the advertised default-branch tip instead.
- **This does not make `authorized-by:` true.** Section 9 of the protocol still applies; a run that
  means to self-authorize can declare `prompt`. What is removed is the DEFAULT.

## Parked decisions
- **The inCMS re-pull is not in this build.** `.governance/install.index` there pins a gov commit
  this build had not made, so closing `ABL-dPublishedAnchor-1` is a second act on the adopter side.
- **`unattended.test.sh` is red on a pristine main** — three arms assert a wording this repo's driver
  does not contain. Found by running a baseline rather than assuming one, and filed as
  `TOOL-dNarrowedAnchor-2` rather than fixed here, because a suite repair inside a feature build is
  how an unrelated red gets attributed to the feature.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dNarrowedAnchor-1` | 2 | the second anchor is admissible per MODE, and `slug` is not one of them |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node d · opened 2026-08-24 · streams tooling
ids TOOL-dNarrowedAnchor-1 TOOL-dNarrowedAnchor-2 TOOL-dNarrowedAnchor-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dNarrowedAnchor-1 — the second anchor is admissible per MODE, and `slug` is not one of them](spec/2026-08-24-spec-TOOL-dNarrowedAnchor-1.md) | — | 2 | INPROGRESS | rev-1 | 2026-08-25 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-dNarrowedAnchor-1.

Ids no `spec-audit` record has ever named: TOOL-dNarrowedAnchor-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
