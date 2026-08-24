---
slug: aTetheredRecord
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aTetheredRecord-1 TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-3 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-5 TOOL-aTetheredRecord-6 TOOL-aTetheredRecord-7
---

# aTetheredRecord — every record names the spec it is evidence about

Node `a` · opened 2026-08-16 · streams tooling.

The build slug is this repo's bookkeeping centrepiece, and everything under a build folder that is
not a spec currently floats free of it. A build holds one spec per unit, each carrying an id in its
status header and its H1. It also holds adversarial reviews, build records, design-pass journals,
research reports and transcripts — and those name nothing. Measured at BASE `96141aed`: **54 of 76
records name no id in their first six lines**, and the recording-name grammar that governs all of
them constrains only the SHAPE of a trailing integer, never that the integer resolves to anything.

The integer is the trap rather than the gap. `memory/builds/aSiftedPlaybook/` holds seven specs
(`PLAY-aSiftedPlaybook-1` through `-4`, `TOOL-aSiftedPlaybook-1` through `-3`) and six reviews named
`review-aSiftedPlaybook-1` through `-6`. That review ordinal is a round counter on its own sequence.
`review-aSiftedPlaybook-3` reads as a match for two different specs and is neither, and the reviews
drop the family qualifier the specs carry, so the collision is structural rather than accidental.

`memory/guides/BUILD-METHOD.md:85` already presumes the binding exists — M4 selects "every spec with
no review record naming it" — so the method's own coverage question cannot be answered from the tree
it is asked about.

## What this build decided

The binding is **authored once, in the record's own head**, as a `**Serves:**` line carrying a kind
token and the spec ids. Three carriers were designed independently and adversarially judged, and the
owner then ratified a fourth arrangement in which two of them carry it together.

**The header is the authored source.** It is the only carrier that can express a set-scoped review
over seven ids, a record that precedes every spec in its build, and one that reaches into a second
build — all of which the corpus actually contains.

**The filename carries a PROJECTION of it** (Fork A, owner). The record's ordinal stops being a
per-kind round counter and becomes the sequence number of a spec it serves. The grammar does not
change SHAPE, which is what avoids the blocker that killed the filename carrier in the design pass:
widening the ordinal slot to hold an id list would have made the closed family alternation vacuous,
and redefining what the existing slot MEANS widens nothing. Check 21's fourth branch asserts the
filename's id is a member of the header's set, so the two carriers cannot drift.

**The generated index renders both** (Fork B, owner). A generator cannot invent a binding it is not
told, so the index derives from the header rather than competing with it.

Ids resolve against **the set defined by a spec H1** — measured 113 today — and never against a
build README's `ids:` roster, which is a reservation range: 66 of its 179 ids have no spec at all.

Every count on this page is a BASE-time snapshot, and the design-pass record is the dated source for
all of them. A unit re-measures from the tree rather than carrying a number out of this paragraph —
the corpus moves, and a figure quoted forward is how the two-answers class gets in.

Enforcement is check 21 in `tools/memory-tree/check-memory-hygiene.sh`, four armed `fail` branches —
the fourth added by Fork A to bind the filename to the header. Resolution costs no new machinery: any
id written into a record is already a citation, and check 14 already reds a citation that resolves to
nothing.

**No cutoff, by owner decision.** Every other ratchet in this kit phases in by filename date. This
one does not, so the retrofit is a scope item rather than a grandfather clause. That choice is
strictly better for arming: `STREAMS_CUTOFF` was set ahead of the corpus and its required arm is
therefore fixture-only, whereas check 21 is exercised by 76 live records from its first run.

The design pass is committed at
[`build/2026-08-16-build-aTetheredRecord-1-design-pass.md`](build/2026-08-16-build-aTetheredRecord-1-design-pass.md),
with every candidate, every blocker and every refuted finding enumerated.

The table below is GENERATED from the status header of every spec in this folder — do not hand-edit it.


## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

Each cell is a label. The unit's §1 Goal owns the full statement.

| Unit | Mechanism | Tier | Classification |
|---|---|---|---|
| `TOOL-aTetheredRecord-1` | Mint the five missing spec H1 ids; drain the orphan waiver to empty | 1 | MISSING → authored this run |
| `TOOL-aTetheredRecord-2` | The binding parser and its read-only `--print-bindings` mode | 2 | MISSING → authored this run |
| `TOOL-aTetheredRecord-3` | The retrofit — all 76 records gain a conformant head line | 1 | MISSING → authored this run |
| `TOOL-aTetheredRecord-4` | Check 21 — four armed fail branches over an extension-agnostic population | 2 | MISSING → authored this run |
| `TOOL-aTetheredRecord-5` | The rendered Records table, the kind column and the two coverage joins | 2 | READY — Forks B and E resolved |
| `TOOL-aTetheredRecord-6` | The adopter path — the obligation ships with the step that arms it | 2 | MISSING → authored this run |
| `TOOL-aTetheredRecord-7` | The rename — every record filename names a spec, and 107 references move with it | 1 | Created by the owner's Fork A resolution |

Ordering is a dependency chain: 1 → 2 → 3 → 7 → 4, then 5 and 6. Unit 7 sits between the retrofit and
the gate because it DERIVES each target name from the binding line unit 3 authors, and because check
21's fourth branch should land on a corpus that already satisfies it.

## Forks — all five RESOLVED by the owner, 2026-08-17

Each resolution is marked in place in the §8 of the unit that owns it, with the option set and the
reasoning; this is the index. Two went AGAINST the spec set's recommendation and are marked as such,
because a resolution that overrode advice and one that confirmed it must stay distinguishable.

| Fork | Resolution | Owner vs recommendation |
|---|---|---|
| A — do filenames carry the binding? | Rename every record; the filename projects the header | **Overrode** — the set recommended leaving ordinals alone |
| B — does the render land? | Build it, after check 21 | Confirmed |
| C — is the reviewed rev mandatory? | Optional, by elimination once cutoffs were ruled out | Confirmed |
| D — bound the escape by count or registry? | A shrink-only count pin | Confirmed |
| E — does a record declare a relation kind? | Add the kind vocabulary now | **Overrode** — the set recommended deferring |

Two of them interact, and the interaction is recorded rather than left to be discovered: E sharpens
the coverage line from "no record names this id" to "no spec audit names this id", and C leaves it
unable to reach M4's rev-keyed question at all. The build therefore does not claim to make M4
computable, and the rendered label says what it actually reports.

## Status

The spec set was authored this run and is **unreviewed by definition** (`BUILD-METHOD.md` M4). The
adversarial pass recorded under `build/` judged the three candidate DESIGNS, not these documents, and
it did not see units 5 through 7 in their present form at all. The M4 spec audit is the next pass,
and unit 7 is the one that most needs it: it exists because a recommendation was overridden, so no
adversarial pass has yet tried to break it.


<!-- gen:build-index -->
**Build status:** CLOSED · 7 unit(s) · node a · opened 2026-08-16 · streams tooling
ids TOOL-aTetheredRecord-1 TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-3 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-5 TOOL-aTetheredRecord-6 TOOL-aTetheredRecord-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTetheredRecord-1 — mint the five missing spec ids, and drain the orphan waiver](spec/2026-08-16-spec-TOOL-aTetheredRecord-1.md) | — | 1 | CLOSED | rev-2 | 2026-08-20 |
| [TOOL-aTetheredRecord-2 — the binding grammar and its read-only parser](spec/2026-08-16-spec-TOOL-aTetheredRecord-2.md) | — | 2 | CLOSED | rev-3 | 2026-08-20 |
| [TOOL-aTetheredRecord-3 — the retrofit: all 76 records gain a binding line](spec/2026-08-16-spec-TOOL-aTetheredRecord-3.md) | — | 1 | CLOSED | rev-4 | 2026-08-20 |
| [TOOL-aTetheredRecord-4 — check 21: the binding becomes the merge bar](spec/2026-08-16-spec-TOOL-aTetheredRecord-4.md) | — | 2 | CLOSED | rev-4 | 2026-08-20 |
| [TOOL-aTetheredRecord-5 — the rendered Records table and the coverage join](spec/2026-08-16-spec-TOOL-aTetheredRecord-5.md) | — | 2 | CLOSED | rev-4 | 2026-08-20 |
| [TOOL-aTetheredRecord-6 — the adopter path: the obligation ships with the step that arms it](spec/2026-08-16-spec-TOOL-aTetheredRecord-6.md) | — | 2 | CLOSED | rev-3 | 2026-08-20 |
| [TOOL-aTetheredRecord-7 — the rename: every record filename names a spec](spec/2026-08-17-spec-TOOL-aTetheredRecord-7.md) | — | 1 | CLOSED | rev-2 | 2026-08-20 |
<!-- /gen:build-units -->

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-16-build-aTetheredRecord-1-design-pass.md](build/2026-08-16-build-aTetheredRecord-1-design-pass.md) | — | *none — this record PRECEDES the spec set and commissioned it; it is the class-4 case the* |
| [2026-08-17-review-TOOL-aTetheredRecord-1-1.md](reviews/2026-08-17-review-TOOL-aTetheredRecord-1-1.md) | spec-audit | TOOL-aTetheredRecord-1 TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-3 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-5 TOOL-aTetheredRecord-6 TOOL-aTetheredRecord-7 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-16-spec-TOOL-aTetheredRecord-1.md](spec/2026-08-16-spec-TOOL-aTetheredRecord-1.md)
  - [2026-08-16-spec-TOOL-aTetheredRecord-2.md](spec/2026-08-16-spec-TOOL-aTetheredRecord-2.md)
  - [2026-08-16-spec-TOOL-aTetheredRecord-3.md](spec/2026-08-16-spec-TOOL-aTetheredRecord-3.md)
  - [2026-08-16-spec-TOOL-aTetheredRecord-4.md](spec/2026-08-16-spec-TOOL-aTetheredRecord-4.md)
  - [2026-08-16-spec-TOOL-aTetheredRecord-5.md](spec/2026-08-16-spec-TOOL-aTetheredRecord-5.md)
  - [2026-08-16-spec-TOOL-aTetheredRecord-6.md](spec/2026-08-16-spec-TOOL-aTetheredRecord-6.md)
  - [2026-08-17-spec-TOOL-aTetheredRecord-7.md](spec/2026-08-17-spec-TOOL-aTetheredRecord-7.md)
- **`build/`**
  - [2026-08-16-build-aTetheredRecord-1-design-pass.md](build/2026-08-16-build-aTetheredRecord-1-design-pass.md)
- **`reviews/`**
  - [2026-08-17-review-TOOL-aTetheredRecord-1-1.md](reviews/2026-08-17-review-TOOL-aTetheredRecord-1-1.md)
<!-- /gen:build-docs -->
