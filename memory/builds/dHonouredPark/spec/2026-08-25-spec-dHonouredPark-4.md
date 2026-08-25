# TOOL-dHonouredPark-4 — `--plan` reads the rendered units region, so both verbs answer from one source

**Status:** SPECCED · rev-1 · 2026-08-25 · node d · Tier-2 · base 60ba1d60 · order 4 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md](../reviews/2026-08-25-review-TOOL-dHonouredPark-1-spec-audit-round1.md) | spec-audit | TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 |

<!-- /gen:spec-records -->

## 1. Goal

Since the roster sorts by build order, `--status` and `--plan` volunteer different units as next:
`--status` reads the generated units region and names the first in build order, `--plan` re-derives
from tracked specs and sorts by id. Neither is wrong about STATUS, and that is what makes the
disagreement expensive — two verbs answering one question differently, with nothing to say which is
authoritative. The owner ruled `--plan` reads the rendered region.

## 2. Scope (IN)

- **S1** — `--plan`'s unit enumeration reads the `gen:build-units` region rather than re-deriving from
  tracked specs. That region is already the shape `check_authorization` and `--status` read, so this
  makes three verbs agree instead of two disagreeing with a third.
- **S2** — `--plan` reports units in the region's own order, which is build order, so its "next" and
  `--status`'s "next" are the same unit by construction rather than by coincidence.
- **S3** — the MISSING join is UNCHANGED and still reads the authored `roster:units` pair. That
  question — which units are planned but unspecced — cannot be answered from a region rendered out of
  the specs that exist, and pointing it there was tried and reverted at `TOOL-aBoundedVerdict-11`.
  This unit moves where the SPECCED set comes from and does not touch where the PLANNED set does.
- **S4** — a REFUSAL when the region is absent or malformed, naming the file and the marker, rather
  than a silent fallback to the old derivation. A fallback would restore the divergence exactly when
  the tree is in the state most likely to hide it.
- **S5** — arms: both verbs name the same next unit on a build with order values; both name the same
  on a build with none; a malformed region refuses; and the MISSING join still fires from the
  authored pair with the region present.

## 3. Non-goals (OUT)

- No change to what `--status` reads. It is already the region and is the verb the other is being
  brought into line with.
- No change to the MISSING join or to `roster_ids`. S3 states the boundary; `TOOL-dHonouredPark-1`
  is the unit that changes anything about the authored pair.
- No sorting of `--plan` by the order verb directly. That was the other option and it couples the
  unattended driver to a grammar the memory-tree kit owns, which is the cross-kit dependency this
  repo's stream rules exist to avoid. Reading the region gets the same order without the coupling.
- No new region and no new marker. The units region already has an address.

## 4. Design

### Data model

Unchanged. `--plan` stops parsing spec files for this list and parses the region instead; both carry
id, status and title.

### Inventory

Three readers of the units region after this unit: `check_authorization`, `--status` and `--plan`.
One reader of the authored pair: `roster_ids`, feeding the MISSING join. The split stays exactly where
`TOOL-aBoundedVerdict-11` put it, and this unit moves one verb from the wrong side of it to the right.

### Migration

One commit. `--plan`'s output changes ORDER for any build carrying order values and is otherwise
identical; nothing downstream parses it, verified by grep for the verb across the tree.

### Alternatives rejected

**Sort `--plan` by the order verb.** Smallest diff. Rejected by the owner and on the coupling: the
driver would have to read a status-header grammar the memory-tree kit defines and can change, and the
two kits are separate streams.

**Document the divergence.** Zero code, and it leaves two verbs volunteering different next units —
the two-answers-to-one-question class this build's parent spent itself removing.

### Files touched (estimate)

`tools/unattended/unattended.sh` · its arms · the kit version sites · `memory/guides/UNATTENDED-PROTOCOL.md`
only if it states what `--plan` reads, which is checked rather than assumed.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — strictly cheaper: one region parse instead of one parse per tracked spec.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an absent or malformed region REFUSES by S4. A build with no units
  renders the region's own empty-case sentence and `--plan` reports no next unit, which is the
  existing behaviour and stays.
- observability — the refusal names the file and the marker, so a stale render is distinguishable
  from an empty build.
- risks — the fallback is the risk, and S4 removes it. A silent fall-back to the old derivation would
  reintroduce the divergence precisely when the region is stale, which is the case where the two
  answers differ most.
- testing + left-shift gates — five arms, including the both-verbs-agree pair, which is the assertion
  that would have caught this divergence when it was introduced.
- migration / rollback — one commit, invertible.
- user docs — the protocol only if it makes a claim about `--plan`'s source.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --plan <slug>` and `--status <slug>` run over a
  build whose units carry order values, both name the SAME unit as next.
- **AC2** — `--plan` and `--status` over a build carrying NO order values still name the same unit.
- **AC3** — When the `gen:build-units` region is absent or its markers are malformed, `--plan` exits
  non-zero naming the file and the marker, and does NOT fall back to the spec derivation.
- **AC4** — When a build's authored `roster:units` pair names an id no spec defines, `--plan` still
  reports it MISSING with the region present, proving S3's boundary held.
- **AC5** — When `--plan` runs over a build carrying order values, its rows appear in build order.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs, the kit gate is green, and the
  both-verbs-agree arm is observed RED first against a staged re-derivation.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `check-kit-versions.sh` · `check-verdict-epoch.sh` ·
`check-arms.py` floors if the driver gains `fail` branches.

## 8. Open questions

- **F1 — does `--plan` keep re-deriving anything from the spec files?** It still needs each spec's
  own classification, which the region does not carry. Recommendation: read the region for the SET
  and its order, and the spec files for per-unit classification — one source per question, which is
  the rule rather than a compromise between two.
- **F2 — should `--status` and `--plan` share one enumerator function?** It would make divergence
  structurally impossible rather than merely tested. Against: it widens this unit into a refactor of
  two verbs with different output contracts. Recommendation: shared enumerator, IF it falls out of
  S1's implementation without changing either verb's output; otherwise the arm in S5 is the guard and
  the refactor is its own row.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, from the owner's ruling on `dFramedEntrypoint`'s third park —
  the one park that was still unruled when the build landed.

## 10. Reuse audit

Memory-recall terms for the regrounding read: `plan status next unit units region rendered derived
divergence build order id order driver verbs`. The seam is the `gen:build-units` region and the
existing readers of it — `check_authorization` at the authorization path and `nonterminal_units`
behind `--status` — both of which select rows out of that region already, so `--plan` is joining an
established pattern rather than inventing one. The negative finding: there is no shared enumerator
today, which is why two verbs could drift at all, and F2 asks whether creating one falls out of this
change or needs its own unit.
