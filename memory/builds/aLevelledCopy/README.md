---
slug: aLevelledCopy
node: a
opened: 2026-10-09
streams: tooling+deployer
roster: TOOL+DEPL
ids: DEPL-aLevelledCopy-1 DEPL-aLevelledCopy-2 TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 TOOL-aLevelledCopy-4 TOOL-aLevelledCopy-5 TOOL-aLevelledCopy-6 TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-8 TOOL-aLevelledCopy-9
authorized-by: prompt
---

# aLevelledCopy — gov covers what adopters' pre-gov hook installer still does

## The problem this build exists to solve

inCMS and NicoCares still run a pre-gov installer, `scripts/install-guards.ps1`, for duties gov does
not perform. A CRLF working copy under an `eol=lf` pin reds the receipt-sync leg although the
committed blob is gov's. An ordinary branch push gets no SSH keepalive, so a long pre-push gate
loses its socket. And gov tracks its git hooks 100644, so a POSIX node runs none of them. The owner's
prose is the mandate, recorded under [prompts/](prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1.md).

## Expected improvements

- Both adopters delete `install-guards.ps1` and take this with a normal govkit update, with no
  per-node step.
- A CRLF-only working copy stops reading as receipt drift, and a real edit still reds.
- Every push from a wired tree carries SSH keepalives.
- A POSIX node runs gov's hooks.

## Detriments if this is not built

- The adopters keep a second, unversioned installer beside gov, and it drifts.
- Receipt-sync stays red on every Windows node that took an eol pin after checkout.
- Long gated pushes keep dying after a green bar.
- On Linux, the branch guard and the pre-push bar do not run, and nothing says so.

## Build-level rules

- **Classification (M2)**: four units, MISSING at open, authored this run, one mechanism each.
- Units 2 and 3 both write `check-wiring.sh`, so they are sequenced; 1 and 4 are disjoint from both.
- Unit 4 is Tier-2: it changes what the deployer writes into an adopter's index.
- One kit-version bump per touched kit, after the last unit (no per-unit bumps).
- Units 5 to 7 are the closing review's promotions (M4): 5 and 6 both write `check-wiring.sh`.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aLevelledCopy-1` | receipt-sync grades a mismatched row through the target's clean filter |
| 2 | `TOOL-aLevelledCopy-2` | check-wiring sets core.sshCommand from push-main's keepalive string when unset |
| 3 | `TOOL-aLevelledCopy-3` | gov's executed hooks are 100755, and check-wiring grades a hook's index mode |
| 4 | `DEPL-aLevelledCopy-1` | govkit update carries gov's exec bit onto an existing engine row |
| 5 | `TOOL-aLevelledCopy-7` | the ssh arm stands back when the operator chose an SSH program by `GIT_SSH` or `ssh.variant` |
| 6 | `TOOL-aLevelledCopy-8` | the ssh arm's failure states each get a verdict and an arm (review minors) |
| 7 | `TOOL-aLevelledCopy-9` | receipt fixtures are hermetic, a renamed row keeps its bit, and the records agree (review minors) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 7 unit(s) · node a · opened 2026-10-09 · streams tooling+deployer
ids DEPL-aLevelledCopy-1 DEPL-aLevelledCopy-2 TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 TOOL-aLevelledCopy-4 TOOL-aLevelledCopy-5 TOOL-aLevelledCopy-6 TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-8 TOOL-aLevelledCopy-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-aLevelledCopy-1 — govkit update carries gov's exec bit onto an existing engine row](spec/2026-10-09-spec-DEPL-aLevelledCopy-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-09 |
| [TOOL-aLevelledCopy-1 — receipt-sync grades a mismatched row through the target's clean filter](spec/2026-10-09-spec-TOOL-aLevelledCopy-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-09 |
| [TOOL-aLevelledCopy-2 — check-wiring sets core.sshCommand from push-main's keepalive string](spec/2026-10-09-spec-TOOL-aLevelledCopy-2.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-09 |
| [TOOL-aLevelledCopy-3 — gov's executed hooks are 100755, and check-wiring grades a hook's index mode](spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md) | 2 | 2 | CLOSED | rev-3 | 2026-10-09 |
| [TOOL-aLevelledCopy-7 — the ssh arm stands back when the operator chose an SSH program](spec/2026-10-09-spec-TOOL-aLevelledCopy-7.md) | 3 | 2 | CLOSED | rev-2 | 2026-10-09 |
| [TOOL-aLevelledCopy-9 — receipt fixtures are hermetic, a renamed row keeps its bit, the records agree](spec/2026-10-09-spec-TOOL-aLevelledCopy-9.md) | 3 | 2 | CLOSED | rev-3 | 2026-10-09 |
| [TOOL-aLevelledCopy-8 — the ssh arm's failure states each get a verdict and an arm](spec/2026-10-09-spec-TOOL-aLevelledCopy-8.md) | 4 | 2 | CLOSED | rev-1 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-aLevelledCopy-1 TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 TOOL-aLevelledCopy-7 TOOL-aLevelledCopy-8 TOOL-aLevelledCopy-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-aLevelledCopy-1`, `TOOL-aLevelledCopy-1`, `TOOL-aLevelledCopy-2` | yes |
| 2 | `TOOL-aLevelledCopy-3` | no |
| 3 | `TOOL-aLevelledCopy-7`, `TOOL-aLevelledCopy-9` | yes |
| 4 | `TOOL-aLevelledCopy-8` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
