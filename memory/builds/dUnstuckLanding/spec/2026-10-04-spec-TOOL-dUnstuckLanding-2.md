# TOOL-dUnstuckLanding-2 — the design: unattended closes through inherited reds and closing decisions, plus attended-landing verbs

**Status:** CLOSED · rev-1 · 2026-10-04 · node d · Tier-1 · base a587e82d · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-1-census.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-1-census.md) | research | TOOL-dUnstuckLanding-1 |
| [2026-10-04-build-TOOL-dUnstuckLanding-2-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-build-TOOL-dUnstuckLanding-2-design.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-2-design.md) | research | — |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-1-0-run-mandate.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-1-0-run-mandate.md) | journal | TOOL-dUnstuckLanding-1 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-2-build-brief.md) | journal | — |
| [2026-10-04-review-TOOL-dUnstuckLanding-1-2-closing-diff-round1.md](../reviews/2026-10-04-review-TOOL-dUnstuckLanding-1-2-closing-diff-round1.md) | diff-review | TOOL-dUnstuckLanding-1 |

<!-- /gen:spec-records -->

## 1. Goal

Design the kit changes that let an unattended run carry its own build to a landed terminal: through
a red it inherited, and through a closing decision it would otherwise defer. Also design a separate
record shape, other than `ABORTED`, for a run that is interrupted and later landed with the owner
present. Then file each chosen mechanism as an ask that a later run can build.

## 2. Scope (IN)

- **S1** — For each failure class in the census, give at least two candidate mechanisms that differ
  in mechanism, and record a test that discriminates between them, together with the loser's
  reason, as M12 asks. Observed by AC1.
- **S2** — An inherited-red design that ends in a landing or an honest pause, with no owner turn in
  either case. Observed by AC2.
- **S3** — A closing-decision design: which decisions the mandate delegates at close, the rule the
  run applies, and what the record keeps. Observed by AC2.
- **S4** — The attended-landing verbs: their names, the phase or fact each writes, their
  preconditions, and how existing `ABORTED` records whose work landed are reconciled. Observed by
  AC3.
- **S5** — One ask per chosen mechanism, filed in this build's `BACKLOG.md` with `seen`, `accept`,
  `SEV` and `KEEP`. Observed by AC4.

## 3. Non-goals (OUT)

- Building any mechanism. The prompt asks for design; the asks carry the building to a later run.
- Changing a governance carrier. The design names the carrier edits each ask owes, and makes none.

### Edges

- **consumes-from** `TOOL-dUnstuckLanding-1` — the classes and the inherited-red answer.

## 4. Design

There is ONE design record, under `build/`, written against the census. Each mechanism section
gives the class it answers, the candidates, the discriminating test with its result, the pick, the
carrier edits it owes, its acceptance shape, and the ask id it was filed under.

### Files touched (estimate)

- `memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-2-design.md`
- `memory/builds/dUnstuckLanding/BACKLOG.md`

## 6. Acceptance criteria

- **AC1** — When the design record `2026-10-04-build-TOOL-dUnstuckLanding-2-design.md` is read, every
  mechanism section names two or more candidates and states the test that rejected each loser.
  Red when: a section names one candidate with no "only one mechanism" claim and its evidence.
- **AC2** — When the census's `## Failure classes` list is joined to the design's sections, every class the census
  counts more than once is answered by a section or is declined with a reason.
  Red when: a class is silently dropped.
- **AC3** — When the verbs section is read, each new verb names its phase or fact, its refusals, and
  the migration route for an existing `ABORTED`-but-landed record, mapped onto `--abort`, `--hold`
  and `--landed` without contradicting `UNATTENDED-STOPS.md`. Red when: a verb writes a terminal
  without a verb that evaluates it.
- **AC4** — When `python tools/memory-tree/gen_build_index.py --asks --build dUnstuckLanding --all`
  runs, it reads every filed ask back as live with a `SEV` row and a `KEEP` disposition.
  Red when: an ask lacks either row.

## 7. Gates

`memory hygiene` · `build README slot contract` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

The seams it extends are the HELD stop contract (`memory/guides/UNATTENDED-STOPS.md` §1-§13), the
inherited-red policy (§13), and the derived terminal (§12). The design builds on all three and
replaces none of them.
Recall terms used: ABORTED landed attended inherited red gates-green absorb hold close override terminal phase abort code
