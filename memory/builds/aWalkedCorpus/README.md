---
slug: aWalkedCorpus
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aWalkedCorpus-1 TOOL-aWalkedCorpus-2 TOOL-aWalkedCorpus-3 TOOL-aWalkedCorpus-4 TOOL-aWalkedCorpus-5 TOOL-aWalkedCorpus-6 TOOL-aWalkedCorpus-7 TOOL-aWalkedCorpus-8 TOOL-aWalkedCorpus-9 TOOL-aWalkedCorpus-10
---

# aWalkedCorpus — one walk over the corpus, and something that grades it

Node `a` · opened 2026-08-16 · streams tooling.

`aDeclaredCeiling` widened the recall corpus to reach declared constraints and left two things it
named as out of scope. One of them it claimed to have recorded and had not.

**The claim is the first unit's subject as much as the cleanup is.**
`memory/builds/aDeclaredCeiling/spec/2026-08-16-spec-TOOL-aDeclaredCeiling-2.md:98` reads
"Unifying the two walks is explicitly NOT this unit's job … **Recorded as the follow-up it is.**"
No row existed. That is a claim that drifted from its source, inside the build whose own
`PLAY-aDeclaredCeiling-1` corrected exactly that shape in a landed record — and it is why this build
exists at all rather than the cleanup simply being scheduled.

## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is an OUTPUT, not this roster.

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aWalkedCorpus-1` | 2 | the two corpus enumerators become one |
| 2 | `TOOL-aWalkedCorpus-2` | 2 | a recall quality floor on the merge bar |
| 3 | `TOOL-aWalkedCorpus-3` | 2 | the same floor, built against the harness that exists |

**Unit 1 first, and the dependency is real rather than tidy.** Unit 2 pins a floor measured against
the corpus, and unit 1 changes how the corpus is enumerated. Measuring a floor against a corpus that
is about to be re-walked would pin a number to a shape the next commit replaces, and re-measuring it
afterwards would make the pin's provenance a guess. Unit 2 measures the corpus unit 1 leaves.

**Unit 3 is unit 2's successor, not its retry.** The round-1 audit answered the question unit 2 was
convened on — is a fixture-plus-floor buildable against `bench.py` as it exists — with a measured no,
and named the two executables the unit needed and never mentioned. Folding that back into unit 2
would have been the fold its own deferral refused; the deferred spec stays DEFERRED as the record of
a design that was wrong, and unit 3 carries the four requirements its §1 wrote down. The build's
title claims something that grades the corpus, so this is the build discharging its own headline
rather than widening.

## Coverage — every follow-up to the unit that discharges it

| Left by `aDeclaredCeiling` | Disposition |
|---|---|
| unify the two corpus enumerators (§4, falsely claimed as recorded) | `TOOL-aWalkedCorpus-1`, which also corrects the claim |
| a recall quality floor (§3 non-goal, §5 risk) | `TOOL-aWalkedCorpus-2`, DEFERRED on measurement, then `TOOL-aWalkedCorpus-3` |
| "one repo-root conf per concern or one for everything" (`TOOL-aDeclaredCeiling-1` §3) | **Not taken.** It is a scoping question with no defect behind it, and neither spec claims it was recorded |

## Build-level rules

- **A landed record is amended in place, never rewritten.** Unit 1 edits a CLOSED spec's §4 to
  correct a false claim; it does not restate what that unit built. `PLAY-aDeclaredCeiling-1` set the
  precedent one build ago and this follows it.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  `non_terminal_specs_cited_by_product_source` sits at its pin with tolerance 0, and `tools/` is a
  product glob. All three units touch `tools/memory-recall/`.
- **A floor is measured, never chosen.** Unit 2 pins whatever the tree actually scores, and the
  number's provenance is the run that produced it. A floor set to a value nobody measured is a
  decoration, and this repo already names that anti-pattern.

The table below is GENERATED from the status header of every spec in this folder — do not
hand-edit it.

<!-- gen:build-index -->
**Build status:** DEFERRED · 3 unit(s) · node a · opened 2026-08-16 · streams tooling
ids TOOL-aWalkedCorpus-1 TOOL-aWalkedCorpus-2 TOOL-aWalkedCorpus-3 TOOL-aWalkedCorpus-4 TOOL-aWalkedCorpus-5 TOOL-aWalkedCorpus-6 TOOL-aWalkedCorpus-7 TOOL-aWalkedCorpus-8 TOOL-aWalkedCorpus-9 TOOL-aWalkedCorpus-10

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aWalkedCorpus-1 — the two corpus enumerators become one](spec/2026-08-16-spec-TOOL-aWalkedCorpus-1.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-aWalkedCorpus-2 — the corpus gets something that grades it](spec/2026-08-16-spec-TOOL-aWalkedCorpus-2.md) | DEFERRED | rev-2 | 2026-08-16 |
| [TOOL-aWalkedCorpus-3 — the recall floor, built against the harness that exists](spec/2026-08-17-spec-TOOL-aWalkedCorpus-3.md) | CLOSED | rev-5 | 2026-08-17 |
<!-- /gen:build-units -->

Records live under `spec/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-16-review-TOOL-aWalkedCorpus-1-1.md](reviews/2026-08-16-review-TOOL-aWalkedCorpus-1-1.md) | spec-audit | TOOL-aWalkedCorpus-1..2 |
| [2026-08-17-review-TOOL-aWalkedCorpus-3-2.md](reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-2.md) | spec-audit | TOOL-aWalkedCorpus-3 |
| [2026-08-17-review-TOOL-aWalkedCorpus-3-3.md](reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-3.md) | spec-audit | TOOL-aWalkedCorpus-3 |
| [2026-08-17-review-TOOL-aWalkedCorpus-3-4.md](reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-4.md) | diff-review | TOOL-aWalkedCorpus-3 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-16-spec-TOOL-aWalkedCorpus-1.md](spec/2026-08-16-spec-TOOL-aWalkedCorpus-1.md)
  - [2026-08-16-spec-TOOL-aWalkedCorpus-2.md](spec/2026-08-16-spec-TOOL-aWalkedCorpus-2.md)
  - [2026-08-17-spec-TOOL-aWalkedCorpus-3.md](spec/2026-08-17-spec-TOOL-aWalkedCorpus-3.md)
- **`reviews/`**
  - [2026-08-16-review-TOOL-aWalkedCorpus-1-1.md](reviews/2026-08-16-review-TOOL-aWalkedCorpus-1-1.md)
  - [2026-08-17-review-TOOL-aWalkedCorpus-3-2.md](reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-2.md)
  - [2026-08-17-review-TOOL-aWalkedCorpus-3-3.md](reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-3.md)
  - [2026-08-17-review-TOOL-aWalkedCorpus-3-4.md](reviews/2026-08-17-review-TOOL-aWalkedCorpus-3-4.md)
<!-- /gen:build-docs -->
