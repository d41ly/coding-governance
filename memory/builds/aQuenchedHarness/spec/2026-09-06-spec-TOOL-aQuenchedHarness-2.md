# TOOL-aQuenchedHarness-2 — leg ceilings derived from the ledger, not guessed at ten times

**Status:** OPEN · rev-1 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md](../build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md) | research | TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Stop authoring per-leg ceilings by hand at roughly ten times a measurement, which is why a wedged leg
today burns between 1.2 and 4.5 hours before the runner kills it. Derive each ceiling from
`<git-dir>/gate-ledger.tsv`, and REFUSE a ceiling that no recorded reading supports — in either
direction, because a ceiling far above the reading is a bound that cannot fire and one below it is a
bound that fires on a healthy leg.

## 2. Scope (IN)

- **S1** — `tools/run-gates/derive-ceilings.py`, a verb that reads `tools/gate-legs.json` and the
  ledger and reports, per leg: the recorded seconds, the declared ceiling, and their ratio.
- **S2** — a `--check` mode that REDS when a ratio falls outside a DECLARED band, and a `--write`
  mode that rewrites the `ceiling` values from the ledger. The band is declared in a data file with
  its reading beside it, in the `gate-profiles.txt` idiom, never as a literal in the script.
- **S3** — a leg with NO ledger row keeps a declared ceiling and is REPORTED as unbacked on every
  run. Unbacked and absent are different states; the reporter distinguishes them, and neither is
  silence.
- **S4** — the band is derived from the ledger's own spread, not chosen: the ledger records the same
  leg under load and idle, so the multiple that does not fire on a healthy concurrent bar is a
  measurement this repo already holds. Record the derivation beside the declaration.
- **S5** — a gate leg wiring `--check` into `tools/gate-legs.json`, so a hand-edited ceiling reds
  rather than drifting. It is a `subject = repo` leg: it grades the manifest, not the kit.
- **S6** — arms staging each refusal: a ceiling above the band, one below it, a leg with no ledger
  row, and an absent ledger entirely.

## 3. Non-goals (OUT)

- Not the whole-run wall, which is `TOOL-aQuenchedHarness-1`.
- Not a per-suite BUDGET verdict — that is a cost check and belongs to `TOOL-aQuenchedHarness-4`. A
  ceiling is a hang bound; conflating the two is what `tools/unattended/run-unattended-gates.sh`
  already warns about in its own comments.
- Not making the ledger authoritative for anything else. It stays a timing cache whose corruption
  costs wall clock only, and this unit must not turn it into a file whose absence reds a bar.
- Not re-deriving ceilings automatically at run time. A ceiling is a DECLARATION; deriving it
  silently on every run would remove the diff that makes a raise visible.

## 4. Design

### Data model

`tools/run-gates/ceiling-band.txt` — a declared band in the two-file idiom this tree already uses for
`tools/template-size-limits.txt` and `tools/memory-tree/build-readme-slot-limits.txt`: the numbers,
and the reading each was set against, argued in place. One row for the band, plus per-leg override
rows for legs whose shape genuinely differs, each carrying its reason.

The ledger is `<git-dir>/gate-ledger.tsv`, one row per leg: name, seconds, verdict, sha, timestamp.
It is READ ONLY here.

### The refusal

`--check` compares `ceiling / recorded` against the band. Above the band is a bound that cannot fire
— the state at HEAD for every one of the nine legs `TOOL-dRetiredFork-40` names. Below the band is a
bound that fires on a healthy leg under the pool, which that same row records as the worse of the two
failures: it turns a passing leg red and teaches everyone to ignore the verdict.

### Migration

`--write` re-derives every ceiling once, in one commit, with the before/after table in the commit
message. The nine legs the backlog names are the ones that move most; the rest move little, and the
report says which.

### Inventory

- `tools/run-gates/derive-ceilings.py` — the verb.
- `tools/run-gates/ceiling-band.txt` — the declaration.
- `leg ceilings backed by measurement` — the new gate leg's name in `tools/gate-legs.json`.

### Files touched (estimate)

`tools/run-gates/derive-ceilings.py` (new) · `tools/run-gates/ceiling-band.txt` (new) ·
`tools/gate-legs.json` · `tools/run-gates/kit.toml` · a self-test beside the verb.

### Alternatives rejected

Deleting ceilings entirely in favour of unit 1's wall was rejected: the wall bounds a RUN, so one
wedged leg would kill the whole bar rather than reporting itself, and the per-leg verdict is what
tells an operator WHICH leg wedged.

## 5. Production-readiness checklist

- security — N/A: reads two tracked-or-local files, writes one tracked file under an explicit verb.
- perf / scale — one Python process over a 94-row manifest and a small TSV; sub-second.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — absent ledger, empty ledger, leg with no row, and ratio out of
  band are four distinct reports, none of them a bare pass.
- observability — the report is the artifact: the ratio table is what makes a raise arguable.
- risks — the ledger is per-worktree and can be absent on a fresh clone, so `--check` must treat an
  absent ledger as UNMEASURED and say so, never as a clean run. That is the vacuous-selector class
  and it is the main hazard here.
- testing + left-shift gates — S6's arms, each a staged break observed RED before landing.
- migration / rollback — reverting the re-derived `tools/gate-legs.json` restores today's values; the
  verb is additive.
- user docs — the band file's own header, and one line in `AGENTS.md`'s bar section.

## 6. Acceptance criteria

- **AC1** — When `python tools/run-gates/derive-ceilings.py --check` runs at HEAD before the
  migration, it REDS naming the legs whose ratio is above the band, and the named set includes the
  ones `TOOL-dRetiredFork-40` records.
- **AC2** — When a ceiling in `tools/gate-legs.json` is edited by hand to a value outside the band,
  the `leg ceilings backed by measurement` leg reds.
- **AC3** — When the ledger is absent, `--check` reports `UNMEASURED` and exits non-zero, rather than
  reporting a clean run over an empty population.
- **AC4** — When `--write` runs, every declared ceiling is inside the band and the report table is
  reproducible from `<git-dir>/gate-ledger.tsv` alone.
- **AC5** — When a leg has no ledger row, `--check` names it as unbacked and does not silently accept
  its declared `ceiling`.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `leg ceilings backed by measurement` leg · the
`run-gates canary`, which asserts the manifest's pinned key set and therefore grades any change to
`tools/gate-legs.json`.

## 8. Open questions

- **F1 — FACT-QUESTION · what band does the ledger support?** The probe is the ledger itself: for
  every leg with more than one recorded reading, the ratio between its slowest and fastest recorded
  seconds is the load spread this bar actually shows, and the band's lower edge must clear it. The
  observation that decides it is that spread; the liveness assertion is that a ledger with fewer than
  two readings for every leg produces NO band and the probe says so rather than returning a default.
  Resolved by measurement during the build, not here.
- **F2 — does the band apply to `subject = kit` legs?** RESOLVED (agent, 2026-09-06, delegated): yes,
  and that is the point — a held leg's ceiling is exactly the one nobody re-measures, which is what
  `TOOL-aBoundedCeiling-10` records about held legs generally.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.

## 10. Reuse audit

The seam is `tools/run-gates/run-gates.sh`'s existing ceiling field and the ledger it already writes
— `<git-dir>/gate-ledger.tsv`, one row per leg with its own seconds — plus the declared-value file
idiom of `tools/template-size-limits.txt`, which `tools/run-gates/gate-profiles.txt` already cites as
the settled answer to this exact problem. `tools/codebase-map/reuse_lookup.py` returned
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seam. Nothing here re-implements
the timing capture: the ledger is read, never re-derived, which is `memory/gotchas/
second-implementation-is-not-a-second-opinion.md` applied at the read path.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
