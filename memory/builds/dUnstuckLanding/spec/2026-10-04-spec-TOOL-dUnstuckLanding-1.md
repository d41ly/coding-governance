# TOOL-dUnstuckLanding-1 — the closing-time failure census across gov, inCMS and NicoCares

**Status:** CLOSED · rev-1 · 2026-10-04 · node d · Tier-1 · base a587e82d · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-1-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-build-TOOL-dUnstuckLanding-1-census.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-1-census.md) | research | TOOL-dUnstuckLanding-2 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-1-0-run-mandate.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-1-0-run-mandate.md) | journal | TOOL-dUnstuckLanding-2 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-1-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Establish, with citations, what actually goes wrong when unattended runs reach their close in the
three repositories that run this kit. The design unit builds on this evidence and on nothing
recalled. The census also answers the owner's direct question: why a run does not resolve a red
it inherited.

## 2. Scope (IN)

- **S1** — Enumerate every run record that ended `ABORTED` or `HELD`, or that recorded a close
  override, in gov, inCMS and NicoCares. For each record, state the code, the reason, and the stage
  it died at. Observed by AC1.
- **S2** — For every `ABORTED` record, say whether the build's work landed anyway, and whether the
  record still reads `ABORTED`. Observed by AC2.
- **S3** — Classify the failures by root cause, giving a count and cited instances for each class.
  Observed by AC3.
- **S4** — Answer "why is an inherited red not resolved in-run" from the driver and the contract,
  citing lines. Observed by AC4.
- **S5** — Catalogue the closing decisions that runs deferred to an absent owner, with the reason
  each run gave. Observed by AC3.

## 3. Non-goals (OUT)

- Any edit to the kit, or to either of the other two repositories. Those repositories are read-only
  sources.
- Choosing a remedy. That belongs to `TOOL-dUnstuckLanding-2`.

### Edges

- **hands-off** `TOOL-dUnstuckLanding-2` — the classes and the inherited-red answer it designs against.

## 4. Design

The census is ONE research record, under `build/`. It is assembled from three read-only historian
passes, one per repository. Each historian writes its findings to the session scratchpad, and the
orchestrator verifies a sample of each historian's citations before folding them in. Every claim in
the record carries a path, a sha or a `file:line`.

### Files touched (estimate)

- `memory/builds/dUnstuckLanding/build/2026-10-04-build-TOOL-dUnstuckLanding-1-census.md`

## 6. Acceptance criteria

- **AC1** — When the record `2026-10-04-build-TOOL-dUnstuckLanding-1-census.md` is read, its run table
  names every repository and gives code, stage and evidence on each row.
  Red when: a repository is missing, or a row has no evidence cell.
- **AC2** — When a sampled `ABORTED` row's slug is grepped in `git log origin/main`, the landed-later
  cell agrees with what git shows. Red when: the cell and `git log` disagree.
- **AC3** — When the census record's `## Failure classes` section is read, each class states a count, cites at least
  two instances (or says that only one exists), and names a root cause.
  Red when: a class carries no instance.
- **AC4** — When the inherited-red answer's `unattended.sh` line citations are opened at BASE, they
  show the mechanism the answer names. Red when: a cited line shows something else.

## 7. Gates

`memory hygiene` · `build README slot contract` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

No existing seam fits: this unit is a record, not code. The prior records it builds on are
`TOOL-dDerivedDocket-24` (the inherited-red policy, `UNATTENDED-STOPS.md` §13) and the HELD stop
contract. Both were found by the recall probe.
Recall terms used: ABORTED landed attended inherited red gates-green absorb hold close override terminal phase abort code
