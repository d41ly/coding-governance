# DEPL-dGaugedVintage-10 — a stale measurer reports every row current

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing asserts that the gov checkout doing the measuring is current with its own remote. The only
vintage guards are ancestry and reachability, so `update --to HEAD` run from a gov clone that is
fifty commits behind reports `current` for every row gov has since moved — a green that means the
measurer was behind, not that the target was level.

## 2. Scope (IN)

- **S1** — A currency probe on the gov checkout: is `to_commit` reachable from the remote's own
  advertised default-branch head, and how far behind is it. It reads the REMOTE's advertisement, not
  a local tracking ref, because a local ref is exactly as stale as the clone.
- **S2** — A declared staleness bound. Beyond it the run REFUSES; within it the run proceeds and says
  how far behind the measurer is. The bound is declared in one place and named in the message.
- **S3** — An offline path that ANNOUNCES itself: when the remote cannot be reached, the run says the
  currency of the measurer is unverified rather than treating unreachable as current.

## 3. Non-goals (OUT)

- Fetching on the adopter's behalf. A verb that mutates the operator's gov checkout to make its own
  answer valid is a side effect nobody asked for.
- Any assertion about the TARGET's currency with its own remote. This unit is about the measurer.
- Replacing `demand_published_vintage` or `demand_forward_vintage`. They answer reachability and
  direction, which are different questions, and both stay.
- Making the probe a hard network dependency. S3 is the reason.

## 4. Design

### Inventory

| Guard | Question it answers | Sees the remote |
|---|---|---|
| `demand_published_vintage` (`govkit.py:3769`) | is `to_commit` on some ref | no |
| `demand_forward_vintage` | is `to_commit` a descendant of the receipt's base | no |
| S1 (new) | is `to_commit` current with the remote's head | yes |

The gap is precise: both existing guards are satisfied by any commit the local clone can see, and a
stale clone can see all of its own commits.

### Rollout

S2's refusal is the behaviour change. It ships with the bound declared and the offline announcement
in the same commit, so an adopter without network access is never blocked by a check that cannot run.

### Alternatives rejected

Comparing against `origin/main` in the local clone was rejected outright: that ref is updated by
fetch, so a clone that has not fetched compares its stale head against its equally stale tracking ref
and reports level. That is a probe that cannot move, which this repo names as worse than none.

## 5. Production-readiness checklist

- security — the probe reads a remote advertisement. It performs no write and follows no redirect.
- perf / scale — one `git ls-remote`-shaped call per run, cached for the run's duration.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S3 is this line: unreachable is ANNOUNCED, never silently green.
- observability — every run prints how far behind the measurer is, including zero.
- risks — a network call in a verb that had none. Bounded by S3 and by a timeout, so an unreachable
  remote costs a message rather than a hang.
- testing + left-shift gates — AC3 and AC4 are the failing cases; both are fixture-driven.
- migration / rollback — none.
- user docs — `WIRE-INTO-PROJECT.md` §5b gains a line saying the measurer's own currency is checked.

## 6. Acceptance criteria

- **AC1** — When the gov checkout is level with its remote, `python tools/govkit/govkit.py update`
  reports the measurer zero commits behind and proceeds.
- **AC2** — When the gov checkout is behind but within the declared bound,
  `python tools/govkit/govkit.py update` proceeds and its output names the distance.
- **AC3** — When the gov checkout is behind by more than the bound,
  `python tools/govkit/govkit.py update` REFUSES and names the bound, observed on a fixture clone
  rewound past it.
- **AC4** — When the remote is unreachable, `python tools/govkit/govkit.py update` announces the
  measurer's currency as unverified and does not report it current, observed by pointing the fixture
  at a dead remote.
- **AC5** — The probe reads the remote rather than a tracking ref: rewind `origin/main` locally
  without fetching and confirm `python tools/govkit/govkit.py update` still reports the true
  distance.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `govkit acceptance matrix`. Any fixture
using a remote must not require network access on the bar; AC4's dead-remote fixture is local.

## 8. Open questions

- **F1 — where the staleness bound is declared.** `.githooks/pre-push` already declares a
  commits-behind bound for the recorded-green rule, so a second spelling would be a second thing to
  drift. Recommendation: reuse that declaration's home if the value can honestly be shared, and
  otherwise declare this one beside it with a comment naming why they differ. Unresolved.
- **F2 — whether the probe runs on `adopt` too.** `adopt` walks gov history to attribute, so a stale
  measurer mis-attributes there as well. Recommendation: yes, same probe, same bound — but it widens
  the unit, so it is the reviewer's call. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.

## 10. Reuse audit

- No existing seam fits, and the evidence is that `python tools/codebase-map/reuse_lookup.py "check
  that a repo checkout is current with its remote before measuring"` returns only generic `check`
  and `repo_root` symbols plus `check_target_reads_subject`, none of which contacts a remote. The
  closest existing behaviour is `memory/guides/UNATTENDED-PROTOCOL.md`'s rule that a BASE is OBSERVED
  from the remote's own HEAD advertisement rather than read from a local ref — the same principle,
  already ratified here, and S1 applies it to the deployer.
- Recall terms used: `base observed remote advertisement local ref stale anchor vintage published
  forward reachability bypass`
