# DEPL-dGaugedVintage-10 — a stale measurer reports every row current

**Status:** CLOSED · rev-3 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 5 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-10-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-10-acceptance-ledger.md) | journal | — |
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing asserts that the gov checkout doing the measuring is itself current. The only vintage guards
are ancestry and reachability, so `update --to HEAD` from a gov clone that has not fetched reports
`current` for every row gov has since moved — a green meaning the measurer was behind, not that the
target was level.

## 2. Scope (IN)

- **S1** — An IDENTITY probe on the gov checkout: is `to_commit` the same sha as the remote's own
  advertised default-branch head, yes or no. It reads the REMOTE's advertisement, never a local
  tracking ref, because a local ref is exactly as stale as the clone.
- **S2** — On not-equal, the run says so and names both shas. REVISED at build time: not-equal is
  reported as one of THREE states, not one — `ahead`, `behind` or `diverged` — because a measurer
  ahead of the advertised head is missing nothing and telling that operator to fetch is wrong advice.
  The distinction needs no fetch: see §4.
- **S3** — An offline path that ANNOUNCES itself: when the remote cannot be reached, the run says the
  measurer's currency is unverified rather than treating unreachable as current.

## 3. Non-goals (OUT)

- **A commits-behind DISTANCE.** It is not computable here and rev-1 wrongly required it. An
  advertisement returns a sha, not objects; on the stale clone this unit exists for,
  `git rev-list --count <to_commit>..<remote_head>` dies with a bad-object error and
  `git merge-base --is-ancestor` has no remote history to walk. Equal-or-not is the whole answerable
  question without a fetch, and a fetch is the next bullet.
- Fetching on the adopter's behalf. A verb that mutates the operator's gov checkout to make its own
  answer valid is a side effect nobody asked for. F2 asks whether a scoped object fetch should
  reopen this.
- Any assertion about the TARGET's currency with its own remote. This unit is about the measurer.
- Replacing `demand_published_vintage` or `demand_forward_vintage`. They answer reachability and
  direction, which are different questions, and both stay.

## 4. Design

### Inventory

| Guard | Question it answers | Sees the remote |
|---|---|---|
| `demand_published_vintage` (`govkit.py:3769`) | is `to_commit` on some ref | no |
| `demand_forward_vintage` | is `to_commit` a descendant of the receipt's base | no |
| S1 (new) | is `to_commit` the remote's advertised head | yes |

Both existing guards are satisfied by any commit the local clone can see, and a stale clone can see
all of its own commits. That is the gap, and it is a gap in identity rather than in distance.

### Rollout

S1 and S3 land together, so an adopter without network access is never blocked by a check that
cannot run.

### Alternatives rejected

Comparing against `origin/main` in the local clone: that ref is updated by fetch, so an unfetched
clone compares its stale head against its equally stale tracking ref and reports level. A probe that
cannot move.

A commits-behind bound, which rev-1 specified. Rejected because §3's first bullet shows the quantity
is unobtainable under this unit's own constraints, and its fixtures would have kept the objects
locally and gone green on exactly the case the unit exists for.

## 5. Production-readiness checklist

- security — the probe reads a remote advertisement. No write, no redirect-following.
- perf / scale — one `ls-remote`-shaped call per run, cached for the run's duration. That call
  returns a sha, which is precisely what S1 needs and all it needs.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S3 is this line: unreachable is ANNOUNCED, never silently green.
- observability — every run says equal or not-equal, and prints both shas when not.
- risks — a network call in a verb that had none. Bounded by S3 and a timeout.
- testing + left-shift gates — AC2 and AC3 are the failing cases; both are local fixtures.
- migration / rollback — none.
- user docs — `WIRE-INTO-PROJECT.md` §5b gains a line saying the measurer's own currency is checked.

## 6. Acceptance criteria

- **AC1** — When the gov checkout's `to_commit` equals the remote's advertised head,
  `python tools/govkit/govkit.py update` says so and proceeds.
- **AC2** — When it does not, `python tools/govkit/govkit.py update` reports not-equal and prints both
  shas, observed on a fixture whose remote advertises a sha the local clone does not have as its head.
- **AC3** — When the remote is unreachable, `python tools/govkit/govkit.py update` announces the
  measurer's currency as unverified and does not report it current, observed by pointing the fixture
  at a dead remote.
- **AC4** — The probe reads the advertisement, not a tracking ref: move `origin/main` locally without
  fetching, and confirm `python tools/govkit/govkit.py update` still reports against the remote's
  advertised sha.
- **AC5** — AMENDED at build time. The probe DOES call `merge-base --is-ancestor`, but only after
  `git cat-file -e` has proved the advertised object is present in this clone; when it is absent that
  absence is itself the verdict (`behind`), and no object-walking command runs. `rev-list` is never
  called — `grep -c rev-list` over the probe returns 0. The property AC5 was protecting is that no
  command runs against objects the clone may lack, and that property holds; the criterion as written
  banned a command rather than the hazard.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `govkit acceptance matrix`. No fixture
may require network access on the bar; AC3's dead-remote fixture is local.

## 8. Open questions

- **F1 — refuse or warn on not-equal.** A refusal makes the guard binding; a warning keeps a
  disconnected operator working. Recommendation: warn by default and refuse under an opt-in, because
  the unit's own S3 concedes the probe cannot always run. RESOLVED (agent, 2026-09-01, delegated):
  WARN, with no opt-in refusal shipped — a guard that blocks a disconnected operator is one they
  route around, and the observation is what was missing. `prior:` `memory/guides/UNATTENDED-PROTOCOL.md`
  section 1 requires the BASE be observed from the remote's advertisement, but rules on authorization
  rather than on this refusal.
- **F2 — whether a scoped object fetch should reopen the distance question.**
  `git fetch --no-write-fetch-head <remote> <head-sha>` would make a distance computable at the cost
  of reversing §3's second bullet and writing objects into the operator's clone. RESOLVED (agent,
  2026-09-01, delegated): no. The three-state answer built here — ahead, behind, diverged — turns out
  to carry the decision an operator actually makes, so the number was never the requirement.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit B3. The unit no longer asks for a commits-behind
  distance: it is not computable from an advertisement without a fetch, which §3 forbids, and rev-1's
  AC2/AC3/AC5 fixtures would have kept the objects locally and passed on exactly the stale clone the
  unit exists for. Reduced to an identity probe, deleted the staleness bound, and corrected §10 —
  the precedent it cites computes no distance either.

- rev-3 · 2026-09-01 · BUILT and CLOSED as `resolve_measurer_currency`, called once per `update`.
  S2 REVISED at build time from a binary to three states: run against a feature branch, the binary
  form told an operator who was AHEAD to fetch, which is wrong advice. AC5 amended — it banned a
  command where it meant to ban a hazard. F1 resolved to warn-only, F2 to no fetch.
  Acceptance ledger at `build/2026-09-01-build-DEPL-dGaugedVintage-10-acceptance-ledger.md`.
## 10. Reuse audit

- The seam is the advertisement read this repo already ships: `tools/unattended/check-unattended.sh`
  around `:655` and `tools/unattended/unattended.sh:747` run `ls-remote --symref --exit-code HEAD`
  and take the sha and the symref name. That is an IDENTITY observation computing no distance, which
  is why S1 is the binary question and not rev-1's. `python tools/codebase-map/reuse_lookup.py "check
  that a repo checkout is current with its remote before measuring"` returns only generic `check` and
  `repo_root` symbols, none of which contacts a remote — the query asked about checkouts rather than
  about advertisements, which is why it missed the seam that exists.
- Recall terms used: `base observed remote advertisement local ref stale anchor vintage published
  forward reachability bypass`
