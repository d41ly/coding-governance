---
slug: dNarrowedAnchor
node: d
opened: 2026-08-24
streams: tooling
roster: TOOL
ids: TOOL-dNarrowedAnchor-1 TOOL-dNarrowedAnchor-2
---

# dNarrowedAnchor — the second anchor becomes PER-MODE, so a `slug` run cannot reach it

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node d · opened 2026-08-24 · streams tooling
ids TOOL-dNarrowedAnchor-1 TOOL-dNarrowedAnchor-2

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-dNarrowedAnchor-1 — the second anchor is admissible per MODE, and `slug` is not one of them](spec/2026-08-24-spec-TOOL-dNarrowedAnchor-1.md) | INPROGRESS | rev-1 | 2026-08-25 |
<!-- /gen:build-units -->

Records live under `spec/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-24-spec-TOOL-dNarrowedAnchor-1.md](spec/2026-08-24-spec-TOOL-dNarrowedAnchor-1.md)
<!-- /gen:build-docs -->

Node `d` · opened 2026-08-24 · streams tooling.

`ANCHOR_SCOPE="published"` is a whole-project switch. It widens `resolve_base` for EVERY run, and the
mode a run declares in `authorized-by:` has no bearing on which anchor it may use. So an adopter who
turns it on to enable the prompt path also, silently and without saying so anywhere, lets a
`slug`-mode run author its own build folder, push its own branch, and be authorized by it.

This is the upstream half of an adopter's finding. inCMS turned the key on at `ARCH-dPublishedAnchor-1`
(2026-08-24) and recorded the cost in its own charter because the kit gave it no way to scope the
concession. `ABL-dPublishedAnchor-1` is that repo's row asking for this.

## The asymmetry, which is the whole argument

| Mode | Authors its own build folder? | Needs the second anchor? |
|---|---|---|
| `slug` | never — the folder exists before the run | **no** |
| `prompt` | always — the prose IS the input | yes |
| `recipe` | sometimes — the owner may have landed it first | sometimes |

`slug` is the one mode whose own definition says the folder predates the run. A `slug` run reaching
the second anchor has therefore contradicted its own declaration, and there is no case where that is
what the owner meant. `prompt` and `recipe` keep the widening because their disciplines are what the
widening exists for.

**Absent is `slug`**, which matters more than it looks: every build README written before the
`authorized-by:` key existed declares nothing, defaults to `slug`, and is thereby refused from the
second anchor by this change. That is the correct answer for all of them — they were all landed on
the default branch.
