# TOOL-dUnstalledConvoy-25 — a spec that names code its own BASE does not carry is refused before it is committed

**Status:** SPECCED · rev-1 · 2026-08-21 · node d · Tier-2 · base d9728f89 · streams tooling

## 1. Goal

A spec pins a BASE sha in its status header and then names identifiers and paths in its Scope and
Design sections. Nothing checks that those exist at that base. `TOOL-dUnstalledConvoy-23` rev-1 named a
re-declaration lookup, a `cur` selection, a narrowing test and a `curgrp` gate; the commit deleting all
four was an ANCESTOR of the base the spec pinned, and the spec passed every gate in the repo and was
committed. A review found it. This unit makes that a gate instead.

## 2. Scope (IN)

- **S1 — a hygiene check over specs at or after a declared cutoff:** every backticked PATH a spec names
  in its Scope or Design sections must exist at the spec's own BASE, tested with
  `git cat-file -e <base>:<path>`.
- **S2 — every backticked IDENTIFIER those sections name that looks like a shell function or variable
  must appear in at least one file the spec also names, at that base.** The population is deliberately
  narrow — see the design — because a wide one is a spelling test.
- **S3 — a declared cutoff and a by-id grandfather list**, in `.memory-tree.conf`, the same idiom the
  acceptance-ledger and spec-witness rules already use. Specs written before this rule cannot satisfy it.
- **S4 — the check announces what it did NOT look at**, in its own header: prose outside those two
  sections, identifiers in other languages, and whether the named thing means what the spec says.

## 3. Non-goals (OUT)

- Checking prose, section 4's narrative beyond its backticked tokens, or any section other than 2 and 3
  and 4. A spec's Goal legitimately describes a world that does not exist yet.
- Checking that a named identifier BEHAVES as the spec claims. That is a review's job and this check's
  header will say so.
- Any language beyond shell and file paths. A Python or JS identifier population needs a parser, and an
  undeclared language must be a named refusal rather than a silent skip.
- Changing the spec format, the section set, or any existing hygiene check.

## 4. Design

The check runs over the same spec population the format gate already walks, so it inherits a selector
that is known to be non-empty rather than inventing one.

S1 is the half that would have caught rev-1 on its own and is nearly free: a spec's Scope section names
few paths, and `git cat-file -e` answers per path. S2 is narrower than it sounds and deliberately so.
The population is identifiers matching a shell-name shape that the spec ALSO co-names with a file — so
`` `curgrp` `` beside `tools/unattended/unattended.sh` is checked against that file at the base, while a
bare `` `union` `` in a sentence is not a candidate at all. A wider population would flag prose nouns
and become the tax that gets waived.

The cutoff in S3 exists because roughly every spec in this corpus predates the rule and a check that
redded them would be unlandable — the same argument `SPEC10_CUTOFF`, `SPEC_WITNESS_CUTOFF` and
`ACCEPTANCE_LEDGER_CUTOFF` each already make, with the same shape of answer.

S4 is the part that keeps a green row honest. This check reads NAMES at a SHA. It cannot tell whether a
spec's design is right, whether the named function does what the spec assumes, or whether the base
itself is the right one to have pinned — and a structural check reads as a semantic one to everybody who
did not write it.

## 5. Production-readiness checklist

- **security** — none; a read-only check over tracked files at a named sha.
- **perf/scale** — one `git cat-file -e` per named path per in-population spec. The hygiene leg already
  walks every spec, so this is a constant-factor addition on a walk that exists.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — a base sha the clone does not carry is an announced SKIP, not a
  refusal: a shallow or fresh clone legitimately lacks it, and redding there would punish the clone
  rather than the spec.
- **observability** — failures name the spec, the token, and the base, because a message naming only the
  spec sends the reader to re-derive which of a dozen tokens was wrong.
- **testing/gates** — fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`, both arms, observed
  RED before landing. The negative arm matters most: a spec naming only things that DO exist must pass.
- **migration/rollback** — the cutoff. Set it forward and the check measures nothing; that is the
  rollback and it needs no code change.
- **help/ docs** — `HYGIENE.md` gains the rule beside the other spec-format rules, in both the template
  and the rendered copy.

## 6. Acceptance criteria

- **AC1** — a spec naming a path absent at its BASE reds, naming the spec, the path and the base,
  observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC2** — a spec naming a shell identifier absent from its co-named file at that BASE reds, observed
  in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC3** — a spec naming only present paths and identifiers PASSES, so the check is not vacuously
  strict, observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC4** — a spec dated before the cutoff is excluded, and one named in the grandfather list is
  excluded, observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC5** — a BASE the clone does not carry produces an announced SKIP naming the spec, not a refusal
  and not silence, observed in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC6** — run over the real corpus at its own base the check is green, and `TOOL-dUnstalledConvoy-23`
  rev-1 restored into a fixture REDS on all four of its dead identifiers, observed in
  `2026-08-21-build-TOOL-dUnstalledConvoy-25-1-red-first.md`.
- **AC7** — the check's header states what it does not check, observed by `grep`.
- **AC8** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`bash tools/run-gates/run-gates.sh`; the memory-hygiene leg and its self-test are what exercise this.

## 8. Open questions

**F1 — is S2 worth its false-positive risk, or is S1 enough?** RESOLVED: both, with S2's population
narrowed to identifiers co-named with a file. S1 alone would have caught none of rev-1's four dead
items, because all four named identifiers inside a file that does exist. The candidate predicate is run
over the real corpus and its hits AND near-misses printed before it is wired, per the charter's rule for
exactly this risk.

## 9. Revision log

- rev-1 · 2026-08-21 · initial draft. Written as the left-shift for the blocker in
  `../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-23-24-specs.md`, which recommended this gate in
  its own fix section.

## 10. Reuse audit

`check-memory-hygiene.sh` already walks every spec, already parses the status header for the base sha,
and already implements the cutoff-plus-grandfather idiom three times. This adds a check to that walk
rather than a script beside it, and reuses `pop_guard` for its population so an empty selector reds.
