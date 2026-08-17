---
slug: cTracedPromise
node: c
opened: 2026-08-14
streams: tooling
roster: TOOL
ids: TOOL-cTracedPromise-1 TOOL-cTracedPromise-2 TOOL-cTracedPromise-3 TOOL-cTracedPromise-4 TOOL-cTracedPromise-5 TOOL-cTracedPromise-6 TOOL-cTracedPromise-7
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

Applied only to specs CLOSED on or after the day the rule landed, and corrected by the M4 audit to
drop merge commits and to stop accepting `.claude/` and the kickoff manifest as product, the third
oracle reads **1 miss over 13 CLOSED specs**. That miss is `TOOL-aMooredAnchor-1`, whose build
commits predate by hours the convention it is judged by. It is the signal's seeded pin, not rot.

The 0 an earlier revision of this spec claimed was an artifact: reconcile merges name the branch
being merged INTO, so `TOOL-aMooredAnchor-1` was certified by two merge subjects belonging to
another build. That is the difference between a measurement and a number.

## What this build changes

Two units.

**U1** — a sixth drift-audit signal, `closed_specs_with_no_product_commit`, gateable, pinned at its
measured 1, date-gated by a project-layer `TRACE_CUTOFF` on each spec's status-header date so no
landed spec is retroactively red and no in-flight one is exempted forever. It rides the two
drift-audit legs already on the bar and adds none.

**U2** — an acceptance-witness branch in check 12 of the memory-tree hygiene gate: once a spec's
filename date reaches `SPEC_WITNESS_CUTOFF`, every acceptance bullet must name something in
backticks. Both tiers, a forward ratchet, four fixtures. Added on the owner's instruction after D1
below was put to them.


## The owner decision menu

**D1 — RESOLVED (owner, 2026-08-15): build it. Shipped as `TOOL-cTracedPromise-2`.** The record of
what was put to them, and the correction the first draft needed, is kept below because the reasoning
is what a later reader needs, not the outcome alone.

**The deferral as it was argued. This was a cost decision, not an evidence-backed one, and the first
draft of this section overstated it.** The kickoff card scoped
a second unit: require each `AC<n>` in a spec's §6 to name a machine-checkable witness. The
measurement above is **silent** on whether that rule is needed — all three oracles key on commit
subjects and none of them reads a spec's §6 at all, so "no measured instance" was a claim the
measurement could not support.

What can be said, measured on this tree: **123 of 359 acceptance bullets across 33 of the 49 CLOSED
specs carry no backticked token** — no test name, no gate leg, no command. That is a candidate count,
not a defect count, since an AC can name its witness in prose. It is the population such a rule would
act on.

The argument for deferring is cost. That unit ratchets the spec format in a second kit, needing its
own cutoff, a `KIT_MEMORY_TREE_VERSION` bump, the verdict-epoch gate, the hygiene parity floor and the
arms floors — and it would grade 359 bullets on a shape rather than on whether the witness is real.
Filed as a `TOOL` backlog row, and then built when the owner asked for it in the same session.

**D2 — what this signal cannot do, stated so it is not assumed.** It measures LINKAGE, not fidelity.
A build that cites its unit correctly and then implements something else entirely passes it. Nothing
mechanical in this repo measures how closely a build followed its spec; that judgement is the M4 spec
audit and the M8 closing adversarial review, and it stays there. The signal narrows the blind spot
from "no measurement at all" to "the link is measured, the content is reviewed".


<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node c · opened 2026-08-14 · streams tooling
ids TOOL-cTracedPromise-1 TOOL-cTracedPromise-2 TOOL-cTracedPromise-3 TOOL-cTracedPromise-4 TOOL-cTracedPromise-5 TOOL-cTracedPromise-6 TOOL-cTracedPromise-7

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-cTracedPromise-1 — a closed spec has to point at a commit that changed the product](spec/2026-08-14-spec-cTracedPromise-1.md) | CLOSED | rev-3 | 2026-08-15 |
| [TOOL-cTracedPromise-2 — an acceptance criterion has to name something a machine can find](spec/2026-08-15-spec-cTracedPromise-2.md) | CLOSED | rev-4 | 2026-08-15 |

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
  - [2026-08-14-spec-cTracedPromise-1.md](spec/2026-08-14-spec-cTracedPromise-1.md)
  - [2026-08-15-spec-cTracedPromise-2.md](spec/2026-08-15-spec-cTracedPromise-2.md)
<!-- /gen:build-docs -->
