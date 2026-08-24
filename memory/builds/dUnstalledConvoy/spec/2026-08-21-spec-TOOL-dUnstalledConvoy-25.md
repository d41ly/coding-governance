# TOOL-dUnstalledConvoy-25 — RETIRED: a spec-base identifier gate that measurement could not justify

**Status:** WONTDO · rev-2 · 2026-08-21 · node d · Tier-2 · base d9728f89 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-21-review-TOOL-dUnstalledConvoy-23-24-25-specs-rev3.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-23-24-25-specs-rev3.md) | diff-review | TOOL-dUnstalledConvoy-23 TOOL-dUnstalledConvoy-24 |
| [2026-08-21-review-TOOL-dUnstalledConvoy-23-24-25-specs.md](../reviews/2026-08-21-review-TOOL-dUnstalledConvoy-23-24-25-specs.md) | diff-review | TOOL-dUnstalledConvoy-23 TOOL-dUnstalledConvoy-24 |

<!-- /gen:spec-records -->

## 1. Goal

The goal was a hygiene check that every path and identifier a spec's Scope or Design section names
resolves at that spec's declared BASE. `TOOL-dUnstalledConvoy-23` rev-1 named four pieces of machinery
that a commit ANCESTRAL to its own base had deleted, passed every gate in this repo, and was caught
only by a human-scale review. That is the definition of a missing gate, and this unit was opened to
supply it.

It is retired because the measurement does not support any version of it.

## 2. Scope (IN)

Nothing. The unit is retired before any code.

## 3. Non-goals (OUT)

Everything previously in scope: the path predicate, the identifier predicate, the cutoff, the
grandfather list, and the announce-what-it-skips header.

## 4. Design

The retirement rests on three measurements, all taken on this tree rather than reasoned about.

**The broad predicate is unshippable.** Every backticked slash-bearing token in sections 2–4 across the
tracked spec corpus: **3853 tokens across 236 specs**. A reviewer ran the resolve step and measured
151 of 225 based specs redding, including `TOOL-dUnstalledConvoy-23` rev-2 in the same commit that
proposed the check. A gate that reds two-thirds of the corpus on its first run is a tax, and the
cutoff cannot rescue it because a spec whose Scope adds NEW files reds on its own scope.

**The narrow predicate is vacuous.** Restricted to path-shaped tokens, in the Scope section only, for
specs dated on or after today, the population is **4 tokens across 7 specs**, and three of those specs
contribute none. A check over four tokens is not a gate.

**The narrow predicate is also blind to the failure it was written for.** rev-1's four dead items were
`cur`, `curgrp`, a narrowing test and a re-declaration lookup — SHELL IDENTIFIERS, not paths. Two of
the four were prose that carries no backtick at all. So the version that is cheap enough to ship would
not have caught the incident, and the version that might have is the one that reds the corpus.

The class is real. It is not cheaply gateable, and this is the second time in this build that a
candidate predicate has been written, run over the real tree, and rejected on its false-positive rate
— the first being the `fail`-in-a-subshell scan. The repo's sanctioned answer for an ungateable class
is a gotcha record and a documented check, which is what replaces this unit.

## 5. Production-readiness checklist

N/A — retired before implementation. The measurements above stand in for it.

## 6. Acceptance criteria

- **AC1** — the class is recorded as a gotcha with its measurements and its review-time check, observed
  in `memory/gotchas/spec-names-code-its-base-lacks.md`.
- **AC2** — the build method's spec step names the check, so a spec author is told to verify identifiers
  against the declared base, observed in `memory/guides/BUILD-METHOD.md`.

## 7. Gates

None. The replacement is a documented check, and the gotcha record is what the hygiene gate's own
check 18 requires of a class with no machine gate.

## 8. Open questions

- **F1 — retire, or ship the narrow version anyway?** RESOLVED (agent, 2026-08-21, delegated): retire. The narrow version examines four
tokens and is blind to the identifier class that caused the incident; shipping it would put a green row
on the bar that means almost nothing, which is the failure mode this whole build has spent five review
rounds removing.

## 9. Revision log

- rev-2 · 2026-08-21 · RETIRED. The owner selected the narrow variant on my framing that narrowing
  would work; the dry-run I then ran — the one rev-1 promised and did not do — falsified that framing.
  Recorded here rather than quietly dropped, because the owner's decision was made on a premise I had
  not yet tested.
- rev-1 · 2026-08-21 · initial draft, proposing the gate a spec review recommended as its own
  left-shift.

## 10. Reuse audit

Nothing is built, so nothing is reused. The replacement reuses `memory/gotchas/` and its existing
`gotchas.py --for-diff` delivery, which already hands a reviewer the classes their diff can hit.
