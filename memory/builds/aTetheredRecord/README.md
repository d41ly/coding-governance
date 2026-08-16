---
slug: aTetheredRecord
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aTetheredRecord-1 TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-3 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-5 TOOL-aTetheredRecord-6
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

The binding is **authored once, in the record's own head**, as a `**Serves:**` line naming spec ids.
Three carriers were designed independently and adversarially judged; two were dropped on blockers.

**The filename does not carry it.** A set-scoped review serves seven ids and a filename cannot spell
seven. Widening the ordinal slot to admit an id list makes the closed family alternation vacuous for
the whole non-spec population, and the rename touches 103 cross-referring lines in 62 files.

**The generated index does not carry it.** A generator cannot invent a binding it is not told, so
that angle needs the authored line anyway; the render is worth building on top of it, not instead.

Ids resolve against **the set defined by a spec H1** — measured 113 today — and never against a
build README's `ids:` roster, which is a reservation range: 66 of its 179 ids have no spec at all.

Every count on this page is a BASE-time snapshot, and the design-pass record is the dated source for
all of them. A unit re-measures from the tree rather than carrying a number out of this paragraph —
the corpus moves, and a figure quoted forward is how the two-answers class gets in.

Enforcement is check 21 in `tools/memory-tree/check-memory-hygiene.sh`, three armed `fail` branches.
Resolution costs no new machinery: any id written into a record is already a citation, and check 14
already reds a citation that resolves to nothing.

**No cutoff, by owner decision.** Every other ratchet in this kit phases in by filename date. This
one does not, so the retrofit is a scope item rather than a grandfather clause. That choice is
strictly better for arming: `STREAMS_CUTOFF` was set ahead of the corpus and its required arm is
therefore fixture-only, whereas check 21 is exercised by 76 live records from its first run.

The design pass is committed at
[`build/2026-08-16-build-aTetheredRecord-1-design-pass.md`](build/2026-08-16-build-aTetheredRecord-1-design-pass.md),
with every candidate, every blocker and every refuted finding enumerated.

The table below is GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 6 unit(s) · node a · opened 2026-08-16 · streams tooling · ids TOOL-aTetheredRecord-1 TOOL-aTetheredRecord-2 TOOL-aTetheredRecord-3 TOOL-aTetheredRecord-4 TOOL-aTetheredRecord-5 TOOL-aTetheredRecord-6

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aTetheredRecord-1 — mint the five missing spec ids, and drain the orphan waiver](spec/2026-08-16-spec-TOOL-aTetheredRecord-1.md) | SPECCED | rev-1 | 2026-08-16 |
| [TOOL-aTetheredRecord-2 — the binding grammar and its read-only parser](spec/2026-08-16-spec-TOOL-aTetheredRecord-2.md) | SPECCED | rev-1 | 2026-08-16 |
| [TOOL-aTetheredRecord-3 — the retrofit: all 76 records gain a binding line](spec/2026-08-16-spec-TOOL-aTetheredRecord-3.md) | SPECCED | rev-1 | 2026-08-16 |
| [TOOL-aTetheredRecord-4 — check 21: the binding becomes the merge bar](spec/2026-08-16-spec-TOOL-aTetheredRecord-4.md) | SPECCED | rev-1 | 2026-08-16 |
| [TOOL-aTetheredRecord-5 — the rendered Records table and the coverage join](spec/2026-08-16-spec-TOOL-aTetheredRecord-5.md) | SPECCED | rev-1 | 2026-08-16 |
| [TOOL-aTetheredRecord-6 — the adopter path: the obligation ships with the step that arms it](spec/2026-08-16-spec-TOOL-aTetheredRecord-6.md) | SPECCED | rev-1 | 2026-08-16 |

Records live under `spec/` and `build/`.
<!-- /gen:build-index -->

## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

Each cell is a label. The unit's §1 Goal owns the full statement.

| Unit | Mechanism | Tier | Classification |
|---|---|---|---|
| `TOOL-aTetheredRecord-1` | Mint the five missing spec H1 ids; drain the orphan waiver to empty | 1 | MISSING → authored this run |
| `TOOL-aTetheredRecord-2` | The binding parser and its read-only `--print-bindings` mode | 2 | MISSING → authored this run |
| `TOOL-aTetheredRecord-3` | The retrofit — all 76 records gain a conformant head line | 1 | MISSING → authored this run |
| `TOOL-aTetheredRecord-4` | Check 21 — three armed fail branches over an extension-agnostic population | 2 | MISSING → authored this run |
| `TOOL-aTetheredRecord-5` | The rendered Records table and the two-sided coverage join | 2 | FORKED — see Fork B |
| `TOOL-aTetheredRecord-6` | The adopter path — the obligation ships with the step that arms it | 2 | MISSING → authored this run |

Ordering is a dependency chain for 1 → 2 → 3 → 4. Unit 5 is separable and unit 6 rides unit 4.

## Open forks for the owner

Every fork below is stated in the unit that owns it; this is the index, not the resolution.

- **Fork A — do filenames carry anything?** Recommended: no, and one sentence in `HYGIENE.md` says
  so. The literal ask included filenames; the cost is 76 renames against 103 cross-referring lines,
  and the ordinal keeps disagreeing with the binding until a reader opens the file. A narrower
  follow-up renaming only the ordinals that collide with a real different id in the same build is
  the better shape. Owned by `TOOL-aTetheredRecord-4`.
- **Fork B — does the render land?** Recommended: yes, after check 21. It buys the one thing no
  grep can compute — which spec ids no record names. Owned by `TOOL-aTetheredRecord-5`.
- **Fork C — is the reviewed rev mandatory?** Recommended: optional. M4 is rev-keyed, but the rev at
  review time is unrecoverable for most of the corpus and requiring it would force a fabricated
  number. Owned by `TOOL-aTetheredRecord-2`.
- **Fork D — bound the unbound escape by a count or a registry?** Recommended: a count. A seventh
  registry costs a documented six-file sweep that a prior unit measured and rejected. Owned by
  `TOOL-aTetheredRecord-4`.
- **Fork E — does a record declare a relation KIND?** Recommended: defer, and do not claim M4
  coverage meanwhile. A cumulative-diff review is not a spec audit, and this build binds ids without
  claiming which relation holds. Owned by `TOOL-aTetheredRecord-5`.

## Status

The spec set was authored this run and is **unreviewed by definition** (`BUILD-METHOD.md` M4). The
adversarial pass recorded under `build/` judged the three candidate DESIGNS, not these documents.
The M4 spec audit is the next pass.
