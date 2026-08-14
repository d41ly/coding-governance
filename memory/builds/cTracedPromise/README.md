---
slug: cTracedPromise
node: c
opened: 2026-08-14
streams: tooling
roster: TOOL
ids: TOOL-cTracedPromise-1
---

# cTracedPromise — a closed spec has to point at a commit that changed the product

Node `c` · opened 2026-08-14 · streams tooling.

The owner asked two questions: how do we know a specced build was actually built from its spec, and
what are the chances a spec is written while the build runs off on its own and is invented. This
build answers the second with a measurement and closes the gap the measurement exposed.

This README is the master overview and the owner decision menu, per `memory/TEMPLATE-SPEC.md`.

## Start here — the measurement, before the change

The tree holds 49 CLOSED specs. **Every one of them has a real commit trail.** No invented build was
found. But the trail is not machine-readable for most of them, and nothing on the bar was asking.

| Oracle over the 49 CLOSED specs | Apparent misses | Real misses |
|---|---|---|
| the spec's own id appears in a commit SUBJECT | 35 | 0 |
| the spec's own id appears anywhere in a commit MESSAGE | 18 | 0 |
| id or slug names a commit that TOUCHED product source | 12 | 0 |

Every apparent miss is a naming convention that predates the rule it is being judged against. The
"unit id in the commit subject" rule arrived with `memory/guides/BUILD-METHOD.md` at `a383375` on
2026-08-11. Before that the subjects were `feat(memory-tree)!: U1 — retire the discipline directory
axis` and `fix(aStandingWrit): fold the closing Tier-2` — the unit number or the slug, never the id.
Three were verified by reading the commits that landed them, not by inference.

Applied only to specs dated on or after the day the rule landed, the third oracle reads **0 misses
over 13 CLOSED specs**. That is a ratchet with a live population, not a decoration.

## What this build changes

One unit. A sixth drift-audit signal, `closed_specs_with_no_product_commit`, gateable, pinned at 0,
date-gated by a project-layer `TRACE_CUTOFF` so no landed spec is retroactively red. It rides the two
drift-audit legs already on the bar and adds none.

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node c · opened 2026-08-14 · streams tooling · ids TOOL-cTracedPromise-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-cTracedPromise-1 — a closed spec has to point at a commit that changed the product](spec/2026-08-14-spec-cTracedPromise-1.md) | OPEN | rev-1 | 2026-08-14 |
<!-- /gen:build-index -->

## The owner decision menu

**D1 — the §6 acceptance-witness rule, dropped from the approved scope.** The kickoff card scoped a
second unit: require each `AC<n>` in a spec's §6 to name a machine-checkable witness. The measurement
above is the argument against building it now. Not one of the 49 CLOSED specs was untraceable because
an acceptance criterion lacked a witness; every apparent gap was commit-subject convention. That unit
would ratchet the spec format in a second kit, needing its own cutoff, a `KIT_MEMORY_TREE_VERSION`
bump, the verdict-epoch gate, the hygiene parity floor and the arms floors — a large surface against a
problem with no measured instance. Filed as a backlog row instead. **Say so if you want it built
anyway; the evidence is a recommendation, not a refusal.**

**D2 — what this signal cannot do, stated so it is not assumed.** It measures LINKAGE, not fidelity.
A build that cites its unit correctly and then implements something else entirely passes it. Nothing
mechanical in this repo measures how closely a build followed its spec; that judgement is the M4 spec
audit and the M8 closing adversarial review, and it stays there. The signal narrows the blind spot
from "no measurement at all" to "the link is measured, the content is reviewed".
