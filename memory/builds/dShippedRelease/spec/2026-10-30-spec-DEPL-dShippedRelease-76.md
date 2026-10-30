# DEPL-dShippedRelease-76 — the offer spells two environments: the grant for clone and push, and none for `update`

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 21 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 86 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H20. Unit 16 S1 refuses unless `credential.helper` is empty, S4 and §4 spawn `update`
with the environment that carries the grant's helper, and S8 and §5 say the update process never
holds the grant. Unit 7 §4 sets the helper through `GIT_CONFIG_COUNT`, so it reaches the child.
Built with S4's environment `check_offer_env` exits 2 on every offer; built by relaxing S1, the
process reading a hostile adopter's tree can obtain the secret.

## 2. Scope (IN)

- **S1** — `derive_offer_git_env(scratch, key)` in `tools/govkit/offer.py` is
  `build_step_env(scratch)` plus the grant's helper, and only `git clone` and `write_offer_branch`'s
  push run under it. Observed by AC1.
- **S2** — `derive_update_env(scratch)` is `build_step_env(scratch)` alone, with
  `GOVKIT_NO_REMOTE_PROBE=1`, and `update --offer` runs under it. So S1 of unit 16 holds as written,
  and unit 16 S4's "with the same environment" and the §4 pseudo-code's single `env` are superseded.
  Observed by AC1, AC2.
- **S3** — The canary. `--plant canary-fill` runs `git credential fill` under `derive_update_env`'s
  result inside the fixture, and asserts no password comes back. Observed by AC2.

## 3. Non-goals (OUT)

- The disposition table and the symlink class: review ids 87 and 89, in the minors batch.
- How the helper is spelled on a Windows node: review id 36, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-16` — `run_offer`, `check_offer_env` and `write_offer_branch`, the three call sites this unit separates

## 4. Design

### Evidence

- Unit 16 S1 lists `credential.helper` empty among `build_step_env`'s isolation, and S8 says the update process never holds the grant (scout D fork 10).
- Unit 7 §4 spells the helper by `GIT_CONFIG_COUNT`, an environment a child inherits (report id 86).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_offer_git_env`, `derive_update_env` | functions, `tools/govkit/offer.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/govkit/offer.py`: S1, S2, S3

## 5. Production-readiness checklist

- security — the grant reaches two git commands and no process that reads the adopter's tree, seen
  by the canary.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a later step added to `run_offer` picks one of two named environments, so the choice is on
  the line that spawns it.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python offer.py --fixture --plant two-envs` runs an offer against a credentialed
  stub remote, the clone and the push succeed, `update` exits 0, and `check_offer_env` passes.
  Red when: `check_offer_env` exits 2 on every offer, so nothing is offered.
- **AC2** — When `--plant canary-fill` runs, `git credential fill` under `derive_update_env` returns
  no `password=` line, and with the grant's helper added to it the same call does.
  Red when: the process reading a hostile tree can obtain the secret, or the canary cannot see one.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/offer.py · covers AC1 AC2 · `canary-fill`, its failing case one shared environment · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 86 (HIGH, item H20) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-7's `build_step_env`, called twice.
`python tools/codebase-map/reuse_lookup.py "build an isolated environment for a child process with no credential helper"`
ranked `build`, `build_commit` and `build_fixture`, name-stem hits, because the parent is specced
and unbuilt, so no existing seam fits beside it. The recall probe surfaced unit 16 and report item
H20, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the offer keep the grant out of the process that reads an adopter tree" --terms "build_step_env credential.helper GIT_CONFIG_COUNT grant isolation offer update hostile tree"`
