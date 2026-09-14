# TOOL-dLoggedFlight-7 — the `Decided:` commit trailer, so a choice with no commit of its own has a home

**Status:** CLOSED · rev-2 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-build-TOOL-dLoggedFlight-7-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-dLoggedFlight-7-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The build method already says that anything a run would have said goes to a file, and names homes for
a park, a decision about a spec and a finding. It names none for a choice made in passing: a leg
subset run instead of the bar, an arm verified by inspection, a pass stopped at 18 of 65. A sample of
21 such choices from one run found 8 recorded nowhere. Give them one home, a `Decided:` trailer on
the commit that carries the work, and make the wrap-up derive from it.

## 2. Scope (IN)

- **S1** `tools/memory-tree/BUILD-METHOD.template.md` M10's first bullet adds the home: a choice with
  no spec, record or park of its own goes to a `Decided: <the choice> — <why>` line, one per choice, in
  the commit message's FINAL trailer block beside `Co-Authored-By:`. M10 carries one example line.
  Observed by AC1 and AC3.
- **S2** M9's "decisions taken" row adds the source: every `Decided:` trailer on the build's own
  commits. Observed by AC1.
- **S3** The dogfood copy `memory/guides/BUILD-METHOD.md` is re-rendered byte-identical, and the
  method stays under its own 27648-byte cap. Observed by AC2.
- **S4** The grammar is git's own trailer format, so `git log --format='%(trailers:key=Decided,valueonly)'`
  reads it with no new parser. Git parses trailers only in the message's last paragraph, which is why
  S1 places the lines there. `TOOL-dLoggedFlight-8` harvests them. Observed by AC3.
- **S5** The memory-tree kit version moves from 2.69 to 2.70 across its carriers, because the unit
  changes shipped memory-tree bytes. TOOL-dMuffledSentinel-3 records an adopter refusing a pull whose
  shipped bytes moved at an unchanged version. Observed by AC4.

## 3. Non-goals (OUT)

- A new verb or row kind in the run-state file. The research record rejects that: the file is already
  over its stated budget on 12 of 56 records.
- A gate that demands trailers. Whether a choice was made is not observable, so there is nothing to
  gate. The harvest reports how many trailers a run left, and nothing refuses a run that left none.

### Edges

- **hands-off** `TOOL-dLoggedFlight-8` — the run model harvests the trailers into its decision ledger.

## 4. Design

M10 is a pointer section, and M1 forbids restating a rule a carrier owns, so the addition is one
clause and one example line, not a paragraph. The trailer rides the commit the work is in. It is
timestamped and public by the same standard commit bodies already are. It costs no protocol-carrier
bytes.

The verdict-epoch rule dates the engine's verdicts, and this unit moves no engine line. The version
still moves, for the adopter-vintage reason in S5, which is a separate rule from the verdict epoch.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `Decided:` | commit trailer key | none |

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md`, and the memory-tree
version carriers `tools/check-kit-versions.sh` names.

### Alternatives rejected

- A `--decide` driver verb: rejected, because its text would either stay machine-local, and so be
  invisible to other nodes, or grow an over-budget run-state file.

## 5. Production-readiness checklist

- security — N/A. A trailer is commit-message text, public by the same rule as the subject.
- perf / scale — N/A. A doc change.
- error / empty / loading states — a run that leaves no trailer harvests to an empty list, reported as
  zero, not as an absence. A `Decided:` line written above the trailer block is invisible to git, and
  the harvest counts those as near-misses (`TOOL-dLoggedFlight-8`).
- observability — the harvest count in the run record.
- risks — the method's byte budget. The addition stays under 300 bytes against 1,209 of headroom.
- testing — the dogfood parity leg, the size leg, the version leg, and a scratch-repo arm for the
  grammar.
- migration — adopters take the M10 line on their next memory-tree update, at 2.70.
- user docs — M10 is the documentation.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'Decided:' memory/guides/BUILD-METHOD.md` runs after this unit, it finds the
  M10 home, its example line and the M9 source row.
  Red when: any of the three is missing from the rendered copy.
- **AC2** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` and
  `bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` run, both are green.
  Red when: the dogfood copy differs from the template, or the method passes 27648 bytes.
- **AC3** — When a scratch repo's commit message is built from M10's own example line placed in the
  final trailer block, `git log --format='%(trailers:key=Decided,valueonly)'` prints that value. A
  second commit with the same line written mid-body, above a paragraph break, prints nothing.
  Red when: M10's placement rule is not the one git parses, or the example cannot be parsed.
- **AC4** — When `bash tools/check-kit-versions.sh` runs, memory-tree is green at 2.70 in every carrier.
  Red when: a carrier still reads 2.69.

## 7. Gates

`kit/dogfood doc parity` · `build-method size` · `kit version markers` · `method carriers (every pointer declared)` · `unattended kit gate` · `memory hygiene`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S4 S5 · §4 · AC1 AC3 AC4 · folded round-1 spec audit M11 (the lines go in
  the final trailer block, since git parses trailers only there; AC3 builds its commit from M10's own
  example and adds a mid-body negative) and M21 (the memory-tree version moves to 2.70 on the
  adopter-vintage precedent of TOOL-dMuffledSentinel-3).

## 10. Reuse audit

The seam is M10's existing bullet in `tools/memory-tree/BUILD-METHOD.template.md`, which already routes
parks, spec decisions and findings. `tools/codebase-map/reuse_lookup.py "record a decision the run
took"` surfaced the build-method dossier and no trailer convention. `git log` already parses trailers,
so the harvest needs no new grammar.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
