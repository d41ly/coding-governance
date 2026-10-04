# TOOL-aWindowedPass-5 — each run is graded against zero; the repo-global ceiling is retired

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-2 · base 886b089d · streams tooling · order 4 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aWindowedPass-5-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aWindowedPass-5-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aWindowedPass-5-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aWindowedPass-5-2-build-brief.md) | journal | — |
| [2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md](../reviews/2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md) | diff-review | TOOL-aWindowedPass-1 TOOL-aWindowedPass-2 TOOL-aWindowedPass-3 TOOL-aWindowedPass-4 |

<!-- /gen:spec-records -->

## 1. Goal

`UNDECLARED_WRITE_CEILING` is one shrink-only number over every live run in the repository. A run's
violations, once committed, cannot be repaired, and raising the number is the owner's call, so one
run's history holds or aborts another run's landing, and every adopter measures its own starting
value. With solo passes no longer counted (`TOOL-aWindowedPass-1`), the honest target for an
overlapping pass is zero, owned by the run that made it. This unit grades each run against zero on
its own and retires the key.

## 2. Scope (IN)

- **S1** — Check 23 FAILS when the run this tree drives — the record whose `run-branch` fact equals
  the current branch's ref — has a counted undeclared write. A counted write in any other live run is
  printed as `check 23 OTHER RUN <run>: <n> counted, graded at its own close - this tree drives <ref>`
  and does not fail.
  Observed by AC1 and AC2.
- **S2** — With no run bound to the current branch, every counted write is reported and none fails,
  and the check says which branch it looked for. Observed by AC2.
- **S3** — `UNDECLARED_WRITE_CEILING` is RETIRED: a `RETIRED_CONF_KEYS` constant in
  `tools/unattended/check-unattended.sh` names it, check 22's join tolerates a retired key a project
  still sets and prints, on the report channel, that it is ignored and may be deleted, and the protocol's key table marks the
  row retired. This repo's conf and the shipped example drop the key. Observed by AC3.
  **Readers:**
  by name: `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/cross-component.test.sh`, `tools/unattended/.unattended.conf.example`,
  `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md`,
  `tools/unattended/README.md` and `.unattended.conf` spell `UNDECLARED_WRITE_CEILING`.
  by value: check 23's ratchet in `tools/unattended/check-unattended.sh` is the only comparison, and
  S1 replaces it with zero for the bound run.
- **S4** — `--emit-ceiling` is retired with the key: it exits 2 naming this unit. Observed by AC4.
  **Readers:**
  by name: `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`,
  `tools/unattended/README.md`, `tools/unattended/PROTOCOL.template.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md` and `.unattended.conf`'s comments spell `--emit-ceiling`.
  by value: NO VALUE READERS — its one output line was pasted into the conf by hand, and nothing in
  the tree parses it.

## 3. Non-goals (OUT)

- A counted write is still not repairable after the commit; preventing it is the commit-time step's
  job (`TOOL-aWindowedPass-3`).

### Edges

- **consumes-from** `TOOL-aWindowedPass-1` — the counted set this unit grades against zero.

## 4. Design

The current branch's ref comes from `git symbolic-ref -q HEAD`; a detached HEAD binds no run. The
existing accumulators become per-run: `ds_over_n` is kept per record, compared to zero for the bound
run, and summed for the report line. The ceiling's validation block and its `--emit-ceiling` output
are removed, and the retired-key list is the one place check 22 learns a key may be set and
undocumented.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/README.md`
- `tools/unattended/cross-component.test.sh`
- `.unattended.conf`

### Alternatives rejected

- **A per-run ceiling key.** A number per run is still a number nobody can lower in time; zero for
  overlapping passes is what the declaration promises.
- **Deleting the key outright.** Check 22 would red every adopter whose conf still sets it.

## 5. Production-readiness checklist

- security — N/A: a gate's scope.
- perf / scale — unchanged.
- error / empty / loading states — no bound run reports and passes, saying so.
- observability — OTHER RUN lines, and the bound run's verdict naming the branch it bound.
- risks — the bar on a default branch no longer fails check 23; the run's close is where it binds,
  and a run cannot land in place without one.
- testing — fixtures with a bound run, another run, and a detached HEAD.
- migration — adopters' confs keep working; the retired key is reported until deleted.
- user docs — the protocol key table and the kit README.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs on a fixture branch whose own run
  has one counted write, it fails check 23 naming that run.
  Red when: the bound run's count is compared against the retired ceiling instead of zero.
- **AC2** — When the counted write belongs to another live run, or HEAD is detached, the output
  carries `check 23 OTHER RUN` and check 23 does not fail.
  Red when: every live run is still summed into one verdict.
- **AC3** — When the fixture conf sets `UNDECLARED_WRITE_CEILING="5"`, check 22 passes and prints the
  key as retired.
  Red when: the retired key is dropped from the join without the tolerance, so check 22 reds.
- **AC4** — When `bash tools/unattended/check-unattended.sh --emit-ceiling` runs, it exits 2 naming
  `TOOL-aWindowedPass-5`.
  Red when: the flag still prints a ceiling.

## 7. Gates

`unattended kit gate`

New arm: tools/unattended/check-unattended.test.sh · bound, other-run and detached fixtures · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the owner's part (5) and check 23's ratchet at base.
- rev-2 · 2026-10-04 · build pass · S1 · S3 · the OTHER RUN line names the ref this tree drives, which
  is S2's "says which branch it looked for" in the same line rather than a second one; the retired
  key's notice is on the report channel, since it changes no verdict; the retired key is filtered from
  check 22's protocol half too, because the table row stays and the example no longer ships it.
- rev-3 · 2026-10-04 · closing review r1 · S1 · M6 · a record naming no run branch prints `check 23 UNBOUND` instead of
  claiming a close that would grade it; no checkout binds it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade only the run this branch drives"` ranked name-stem
neighbours only and printed `unscanned layers: .sh`. Extended: check 23's accumulators, check 22's
key join, and the `run-branch` fact preflight already writes. The recall probe returned
TOOL-cMendedVintage-14, which made the count a ratchet, and TOOL-aSightedSkeptic-13, which lowered it
to 0 by excluding derived-LANDED records.

Recall terms used: check 23 undeclared write ceiling dispatch declaration disjointness concurrent pass generated index shrink-only ratchet

The question passed with them: "why does check 23 count undeclared writes against a shrink-only ceiling and how was the dispatch declaration meant to prove disjointness".
