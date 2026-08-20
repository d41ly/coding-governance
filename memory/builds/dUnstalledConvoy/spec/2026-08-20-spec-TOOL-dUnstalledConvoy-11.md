# TOOL-dUnstalledConvoy-11 — a journal record gains an acceptance ledger, so a built unit says which criterion each observation satisfied

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling

## 1. Goal

Specs number their acceptance criteria and nothing joins a built unit back to those numbers. This
unit defines the ledger that carries the join — one line per criterion, naming either the observation
that satisfied it or the revision that amended it — inside the `journal` record kind that already
exists for evidence of what was built.

## 2. Scope (IN)

- **S1** — `memory/HYGIENE.md` and its template gain an `Acceptance ledger` sub-section beside the
  existing `Record bindings` grammar, because a ledger is a second binding a record carries and
  belongs where the first one is documented.
- **S2** — the grammar is one line per criterion, inside a record whose `**Serves:**` line carries
  kind `journal` and names the unit:

  ```
  **Evidences:** <unit-id>
  - AC1 — `<observation token>` — <what was observed>
  - AC2 — amended rev-<n> — <the change, and the section 9 line that logs it>
  ```

- **S3** — two forms per criterion and no third. A criterion is either OBSERVED, and then the line
  carries a backticked token naming the command, file, flag or test that made the observation; or
  AMENDED, and then the line names the revision that changed it. There is no "satisfied" without one
  of those two.
- **S4** — the AMENDED form is what makes divergence legal and visible. M2 already permits divergence
  by changing the spec first, and this is the record of having done so.
- **S5** — the ledger is REQUIRED for a unit whose spec status is `CLOSED` and whose spec filename
  date is at or after a new `ACCEPTANCE_LEDGER_CUTOFF` in `.memory-tree.conf`. `WONTDO` units owe no
  ledger, because a retired unit built nothing.
- **S6** — `memory/TEMPLATE-SPEC.md` §6 gains one sentence pointing at the ledger, so an author
  numbering criteria knows what will later cite them. It points and does not restate.
- **S7** — the kit templates and this repo's rendered copies move together, and the kit version
  marker is bumped across every carrier that holds one, derived from the markers rather than from a
  remediation message an open row records as naming too few.

## 3. Non-goals (OUT)

- The check that enforces it. That is `TOOL-dUnstalledConvoy-12`.
- A new record KIND. `journal` is defined as evidence of what was built, which is exactly this. A new
  kind would make the closed kind set stop being groupable.
- A Definition-of-Done item. The owner chose a hygiene check over a blocking item, because a ninth
  blocking item is one more way for a finished build to wedge.
- Requiring a ledger for an attended build's units. S5 keys on the spec status and date, not on
  whether a run existed, so attended builds are in scope by the same rule — this is deliberate and
  is flagged in §8.
- Validating that an observation token names something that exists. The gate reads shape, exactly as
  the existing acceptance-witness rule does.

## 4. Design

### Where it lives, and why not in the spec

The ledger could live in the spec's §6, beside each criterion. It must not. A spec is the design and
is written before the code; a ledger is evidence and is written after it. Putting evidence in the
spec would make every build rewrite its own acceptance criteria, and the revision log would fill with
rev bumps that changed no design.

The `journal` kind already exists for exactly this and already carries a `**Serves:**` line naming
the unit. The ledger is a second block in a record that is already bound to the right spec.

### Why two forms and no third

A criterion that was neither observed nor amended is a criterion nobody met. Allowing a third form —
"satisfied", "N/A", "covered elsewhere" — is how a ledger becomes a checkbox exercise, and the
resulting green is worth nothing. Two forms force the author to say which of the two true things
happened.

The AMENDED form is the more important of the two. Without it a run that legitimately discovered a
criterion was wrong has no legal way to record that, and would either lie in the observed form or
skip the ledger. With it, divergence has a home and becomes visible rather than trusted, which is
the whole of the owner's third observation.

### Grandfathering

This corpus holds roughly 149 closed specs, none of which carries a ledger. Without a cutoff, the
check in `TOOL-dUnstalledConvoy-12` reds on every one of them and the unit is unlandable by any run —
the same shape `UNITS_REGION_CUTOFF` exists to prevent, and the same idiom is used.

`ACCEPTANCE_LEDGER_CUTOFF` is set to the day this pair lands. The conf comment states what moving it
in either direction costs, matching the three cutoffs the file already carries.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/HYGIENE.template.md` | the `Acceptance ledger` sub-section |
| `memory/HYGIENE.md` | the render of the same |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | S6's pointer in §6 |
| `memory/TEMPLATE-SPEC.md` | the render of the same |
| `.memory-tree.conf` | `ACCEPTANCE_LEDGER_CUTOFF` with its comment |
| every carrier holding the kit version marker | the bump, derived from the markers |

### Alternatives rejected

- **A per-criterion field inside the spec.** Rejected in §4, with the reason.
- **A new record kind `acceptance`.** Rejected: `journal` is already defined as evidence of what was
  built, and the kind set is closed precisely so two authors cannot spell one relation two ways.
- **Making the ledger a Definition-of-Done item.** Offered to the owner and declined.

## 5. Production-readiness checklist

- security — N/A — a record grammar.
- perf / scale — N/A — a record grammar. The check's cost is `TOOL-dUnstalledConvoy-12`'s line.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A for the grammar; the malformed-ledger refusals belong to the
  check.
- observability — this unit IS the observability the owner's third observation asked for.
- risks (concurrency, data-loss, rollback hazards) — the live risk is the ledger becoming ceremony.
  S3's two-form rule is the control, and it is the design decision most worth reviewing.
- testing + left-shift gates — the check is unit 12. This unit's own gates are the hygiene gate's
  existing checks over `HYGIENE.md` and the template parity legs.
- migration / rollback — the cutoff. No existing record is rewritten.
- user docs — `HYGIENE.md` and `TEMPLATE-SPEC.md` are the user docs for this, and both are in scope.

## 6. Acceptance criteria

- **AC1** — `memory/HYGIENE.md` carries an `Acceptance ledger` sub-section stating the two forms and
  the `**Evidences:**` line, and its template is byte-identical modulo the install prefix.
- **AC2** — `memory/TEMPLATE-SPEC.md` §6 points at the ledger in one sentence and does not restate
  the grammar.
- **AC3** — `ACCEPTANCE_LEDGER_CUTOFF` is present in `.memory-tree.conf` with a comment stating what
  moving it either way costs.
- **AC4** — `bash tools/memory-tree/check-memory-hygiene.sh` stays green over the corpus after the
  documentation lands and before unit 12's check is armed.
- **AC5** — `bash tools/check-kit-versions.sh` is green, with the marker bumped in every carrier that
  holds one, derived by grepping for the marker rather than from a remediation message.
- **AC6** — A hand-written example ledger in the new sub-section parses under the grammar the section
  states, checked by reading it back against unit 12's parser once that lands, observed in `tools/memory-tree/check-memory-hygiene.sh`.

## 7. Gates

`memory-tree hygiene` · `kit version markers` · `verdict epoch` · `method carriers` · the full bar at
the push boundary.

## 8. Open questions

- **F1 — does the ledger bind ATTENDED builds too?** S5 keys on spec status and date, so it does.
  That is a wider blast radius than the owner's report, which was about unattended runs. Options:
  keep it universal; or scope the requirement to units belonging to a build that has a run-state
  file. **Recommendation: keep it universal.** An attended build's spec conformance is exactly as
  unobserved as an unattended one's, the ledger is cheap, and a rule that applies by run mode is two
  rules. Raised because it is a scope question the owner may want, and it pairs with
  `TOOL-dUnstalledConvoy-8` F1, which asks the same question about M6.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a record names the spec it serves and the evidence it
carries"` returns the `build-readme-surface` dossier and `apply_region` as its affordance seam, plus
the memory-tree hygiene dossier. The seam extended is the `Record bindings` grammar in
`memory/HYGIENE.md` and the `journal` kind it already defines — read at source before writing, where
the kind is glossed exactly as "evidence of what was built".

`python tools/memory-recall/query.py "how does this repo record that a built unit satisfied the
acceptance criteria its spec wrote" --terms "acceptance criteria witness token journal record serves
binding evidence conformance spec divergence revision amended cutoff"` returns the record-binding
records, the acceptance-witness cutoff record and the spec-format ownership record. The
acceptance-witness rule is the closest prior art and is deliberately mirrored: it too reads shape
only, and says so.

Recall terms used: acceptance criteria witness token journal record serves binding evidence
conformance spec divergence revision amended cutoff.
