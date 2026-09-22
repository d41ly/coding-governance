# dLandedVerdict — design pass

**Serves:** research TOOL-dLandedVerdict-1 TOOL-dLandedVerdict-2
**Commissions:** TOOL-dLandedVerdict-1 TOOL-dLandedVerdict-2

Node `d` · 2026-08-19 · BASE `098bebd`. Every figure here is a BASE-time snapshot; a unit re-measures
from the tree rather than carrying a number out of this page.

## 1. What was measured, and how

A ground-truth pass over all seventeen builds in `memory/LIVE.md`. Five investigators, one group of
builds each, told to verify at ARTIFACT level at `main` — not to trust a commit-message grep, because
one known case (`aTimedTurnstile`) landed under commits whose subjects name only `feat(run-gates)`.
Every LANDED verdict then went to a skeptic instructed to REFUTE it, attacking on four axes:
reachability (`git merge-base --is-ancestor`), per-unit completeness, provenance (which commit
actually introduced the artifact), and deliberate non-terminality.

Ten agents, 365 tool calls, zero errors.

## 2. The result

**Fourteen of seventeen builds have their product work on `main`.** Only `aBoundedVerdict`,
`aPortableWarden` and `aFerriedDossier` are honestly not-landed.

The refutation stage is what makes this usable, because it split the fourteen in two.

**Nine survived refutation — landed, and closeable.** `aTetheredRecord` (7 specs),
`cKeyedLaunchpad` (7), `aDrainedSluice` (4), `aTimedTurnstile` (2), `aBatchedLintel`,
`aGuardedTally`, `aWireWarden`, plus `aWalkedCorpus` and `aDeployScout`, which are excluded from the
close-out for their own reasons (a `DEFERRED` spec is a chosen state; a research record carries no
status header).

**Five were refuted — landed, and NOT closeable:**

| build | what the skeptic found |
|---|---|
| `aSealedCaravan` | `DEPL-aSealedCaravan-2`'s DoD names three legs; not all are among the 70 in `tools/gate-legs.json` |
| `aTetheredConvoy` | units 1-6 hold at `main`; `DEPL-aTetheredConvoy-7` did not land |
| `bConvergentLodestar` | `TOOL-bConvergentLodestar-1` did not land — and provenance for the rest is stronger than claimed, the commit bodies name the unit directly |
| `aMendedLedger` | every artifact is on `main`; the build carries owner-reserved decisions never ratified |
| `aQuarriedLantern` | the work landed and the record explicitly forbids closure, with a gate enforcing it |

## 3. The design consequence

`landed` and `closeable` are different predicates. Five of fourteen are the first and not the second,
and the difference lives in a DoD, an unlanded sibling unit, or an unratified owner decision — none
of which a predicate over git history or record bindings can read.

This is the whole argument for `gateable: False`. A gating version would refuse merges on five
honest states, and the only escape would be a waiver registry the build would have to invent.

## 4. The predicate: three candidates, all measured

Against the 46 non-terminal specs at BASE.

| predicate | flags | verdict |
|---|---|---|
| unit id in a product commit subject | 20 of 46 | **CHOSEN** |
| slug in a product commit subject | 37 of 46 | rejected |
| `**Serves:** diff-review <id>` | 15 of 46 | rejected |

**Why not the slug.** It reproduces a failure this repo already recorded. `drift_report.py:298-303`
says slug-keying was tried upstream and over-flagged 107 of 126, because every id of a build shares
its slug, so one shipped unit makes all its siblings look stale. The measurement here reproduced it
exactly: `aSealedCaravan`'s genuinely-open unit is flagged through its CLOSED sibling.

**Why not the record binding.** It misses `aTetheredRecord`, `cKeyedLaunchpad` and `aTimedTurnstile`.
Their closing reviews exist but were filed under kind `spec-audit`, not `diff-review`. A predicate
that depends on a kind token being chosen correctly inherits every past miscategorisation.

**What the id key costs, stated rather than hidden.** It cannot see a records-only unit, because such
a unit has no product commit by construction — two of `aTetheredRecord`'s seven are invisible to it.
That miss is honest: the signal says "this unit's work appears on the trunk", and for a records-only
unit there is nothing on the trunk under `PRODUCT_GLOBS` to appear.

## 5. What the two existing signals actually cover

`signal_closed_specs_untraceable`'s docstring claims it and `signal_spec_status` "cover both ways a
status can lie about git". That claim is false and the gap is measurable: 20 specs have their id in a
landing commit subject, while `non_terminal_specs_cited_by_product_source` sees 2 — because it reads
product SOURCE FILES, not commit history. The two questions are not the same question.

The docstring is not edited by this build. Correcting a sibling's prose while adding the member it was
wrong about is a change a reviewer cannot separate from the addition; it is filed instead.

## 6. Parked

- The five refuted builds each need their own disposition — land the missing unit, or park it
  formally. Two require owner ratification. Not this build's scope; raised as backlog rows.
- `signal_closed_specs_untraceable`'s completeness claim in its own docstring is now known false and
  is left for a follow-up that touches only that prose.
