---
slug: aWokenSentinel
node: a
opened: 2026-09-16
streams: tooling
roster: TOOL
parents: aPrimedKeepalive aProbedUnit
authorized-by: prompt
ids: TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14
---

# aWokenSentinel — a keepalive that lives outside the failure domain of the run it keeps alive

## The problem this build exists to solve

An unattended run that stalls never resumes. The kit's keepalive is a `CronCreate` job: same
process, same event loop, same account as the run it guards, and it fires only while the session is
idle. Over this repo's records zero stalls were ever cleared by it; every resume was a human. The
prompt is the mandate and its bytes are the record under `prompts/`; the design it names is the
research record under `build/`.

## Expected improvements

- The run-state file names the session and pid holding the run, so a resumer can find it.
- One read-only predicate answers "is this run alive" for every reader.
- A session bound to a non-terminal run cannot end its turn: the `Stop` hook refuses, bounded.
- An API-error or limit stall is an on-disk fact at zero API cost.
- An OS-scheduled tick resumes a dead or hung session from a different process.
- The contract names the actors and stops calling the cron job a keepalive.

## Detriments if this is not built

- Every class-E stall (parked on an absent owner) keeps costing a human resume; four of six did.
- A limit lockout or 5xx run ends silently and is found the next morning.
- App death takes every run on the node with it and nothing on disk says which.
- Adopters copy a keepalive the records show has never resumed anything.

## Build-level rules

- **Every unit ships to adopters through its kit.** A change to a rendered or copy-installed file lands in the template AND its render in one commit.
- **Failure-domain rule.** A mechanism is only counted as covering a stall class when it does not share the stalled session's process, event loop or account for that class. This is the research record's ranking rule and the reason the cron job is demoted rather than fixed.
- **No self-test suite runs inside a pass.** A pass observes the single arm or the staged break; `run-unattended-gates.sh` runs once, at the close, on a frozen clone.
- **Vocabulary changes land in every carrier in one commit**: driver, leg, VERBS, SKILL, protocol, conf and its example.
- **The CLI token is the owner's**, minted out of band; unit 5 ships inert until registered and reports an absent login as an announced skip, never a pass.
- **Classification at open**: all MISSING; specced by the harness's SPEC stage from the briefs under `prompts/`. Unit 7 was ADDED after preflight by `--rescope`, on the measured `session_crons` field.
- **Spec-audit round 1 disposed by severity (M4), 2026-09-20.** BOUNDED at `REVIEW_ROUNDS` 1, 43 confirmed: the 16 at BLOCKER and HIGH PROMOTED by `--rescope --act add` into units 8 to 14, one per defect, audited as specs before build; the 27 at MEDIUM and LOW FOLDED as rev-2 of units 1 to 7. Nothing parked, waived, retired or re-reviewed.

## Parked decisions

(none yet)

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aWokenSentinel-1` | PLANNED | the run-state file records the lease: `session:` and `pid:` at preflight and resume, and resume re-records the keepalive id |
| 2 | `TOOL-aWokenSentinel-2` | PLANNED | `--liveness <slug>`: the one machine-readable predicate every out-of-session reader shares |
| 3 | `TOOL-aWokenSentinel-3` | PLANNED | `stop-guard`: a `Stop` hook that refuses the turn end of a session bound to a non-terminal run, bounded |
| 4 | `TOOL-aWokenSentinel-4` | PLANNED | `stall-recorder`: a `StopFailure` hook that writes the stall to a sidecar under the git dir |
| 5 | `TOOL-aWokenSentinel-5` | PLANNED | `resume-tick.sh`: the OS-scheduled out-of-process resumer, acting on a stale lease only |
| 6 | `TOOL-aWokenSentinel-6` | PLANNED | the contract: protocol §5, the Skill, the conf knobs and the kit version, with the cron job demoted to the idle-wake |
| 7 | `TOOL-aWokenSentinel-7` | PLANNED | `keepalive-reaped` becomes CHECKED at `--landed` against the cron listing the stop-guard recorded, no longer attested |
| 8 | `TOOL-aWokenSentinel-8` | PLANNED | the stop-guard's `landing-unstamped` row: a bound session at `FINISHED-UNSTAMPED` is BLOCKED and told to run `--landed`, so the `--landed` refusal's end-the-turn remedy is continued rather than allowed (audit B1) |
| 9 | `TOOL-aWokenSentinel-9` | PLANNED | the stop-guard listing as a FIELD on `--status`'s one line, omitted when unrecorded, and the header's one-line promise made an arm (audit H1) |
| 10 | `TOOL-aWokenSentinel-10` | PLANNED | `STOP_GUARD_BLOCKS` declared in every carrier check 22 and spec 6 AC6 read: the example, `optional_keys`, the protocol's section 8 row with its render, the root conf with its rationale and the manifest re-stamp (audit H2) |
| 11 | `TOOL-aWokenSentinel-11` | PLANNED | a kit-gate check that the driver holds ONE derivation of the sidecar root, `resolve_sidecar_dir`, so a second `rev-parse --git-dir` spelling reds the bar for every unit (audit H3) |
| 12 | `TOOL-aWokenSentinel-12` | PLANNED | the tick consults login BEFORE it kills: a logged-out node kills nothing, observed by an arm whose live process survives, and the class left-shifted to `memory/gotchas/` (audit H4) |
| 13 | `TOOL-aWokenSentinel-13` | PLANNED | the tick sources the root `.unattended.conf` into its own shell before its `read_bound_key` calls, so a declared bound is honoured and the NOTE names the file; arms under a declared key (audit H5) |
| 14 | `TOOL-aWokenSentinel-14` | PLANNED | `seed()` in `adopt-unattended.test.sh` commits once, so every fixture that borrows it has a born HEAD and `--liveness`'s `git log` probe is live; the class left-shifted to `memory/gotchas/` (audit H6) |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 14 unit(s) · node a · opened 2026-09-16 · streams tooling
ids TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13
ids TOOL-aWokenSentinel-14

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aWokenSentinel-1 — the run-state file records the LEASE: `session:` and `pid:` at preflight, and `--resume --keepalive-id` replaces it](spec/2026-09-16-spec-TOOL-aWokenSentinel-1.md) | 1 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-2 — `--liveness <slug>`, the one machine-readable predicate every out-of-session reader shares](spec/2026-09-16-spec-TOOL-aWokenSentinel-2.md) | 2 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-11 — a kit-gate check that the driver holds ONE derivation of the sidecar root](spec/2026-09-20-spec-TOOL-aWokenSentinel-11.md) | 3 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-14 — `seed()` commits once, so every fixture that borrows it has a born HEAD](spec/2026-09-20-spec-TOOL-aWokenSentinel-14.md) | 4 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-3 — `stop-guard`, the `Stop` hook that refuses a bound session's turn end](spec/2026-09-16-spec-TOOL-aWokenSentinel-3.md) | 5 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-8 — the stop-guard's `landing-unstamped` row: a bound session at `FINISHED-UNSTAMPED` is blocked and told to run `--landed`](spec/2026-09-20-spec-TOOL-aWokenSentinel-8.md) | 6 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-10 — `STOP_GUARD_BLOCKS` declared in every carrier check 22 and spec 6 AC6 read](spec/2026-09-20-spec-TOOL-aWokenSentinel-10.md) | 7 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-4 — `stall-recorder`, the `StopFailure` hook that writes an API-error stall to disk](spec/2026-09-16-spec-TOOL-aWokenSentinel-4.md) | 8 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-5 — `resume-tick.sh`, the OS-scheduled out-of-process resumer](spec/2026-09-16-spec-TOOL-aWokenSentinel-5.md) | 9 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-12 — the resume tick consults login BEFORE it kills: a logged-out node kills nothing](spec/2026-09-20-spec-TOOL-aWokenSentinel-12.md) | 10 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-13 — the resume tick sources the root conf before its bound reads, so a declared bound is honoured and the NOTE names the file](spec/2026-09-20-spec-TOOL-aWokenSentinel-13.md) | 11 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-6 — the contract: protocol section 5, the Skill, the README, the conf prose and the dossier, with the cron job demoted to the idle-wake](spec/2026-09-16-spec-TOOL-aWokenSentinel-6.md) | 12 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-7 — `keepalive-reaped` becomes CHECKED: `--landed` reads the harness's own cron listing](spec/2026-09-16-spec-TOOL-aWokenSentinel-7.md) | 13 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-9 — the stop-guard listing as a FIELD on `--status`'s one line, and the one-line promise made an arm](spec/2026-09-20-spec-TOOL-aWokenSentinel-9.md) | 14 | 2 | SPECCED | rev-1 | 2026-09-20 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 4 record folder(s).

Ids no record names: TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9.

Ids no `spec-audit` record has ever named: TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aWokenSentinel-1` | no |
| 2 | `TOOL-aWokenSentinel-2` | no |
| 3 | `TOOL-aWokenSentinel-11` | no |
| 4 | `TOOL-aWokenSentinel-14` | no |
| 5 | `TOOL-aWokenSentinel-3` | no |
| 6 | `TOOL-aWokenSentinel-8` | no |
| 7 | `TOOL-aWokenSentinel-10` | no |
| 8 | `TOOL-aWokenSentinel-4` | no |
| 9 | `TOOL-aWokenSentinel-5` | no |
| 10 | `TOOL-aWokenSentinel-12` | no |
| 11 | `TOOL-aWokenSentinel-13` | no |
| 12 | `TOOL-aWokenSentinel-6` | no |
| 13 | `TOOL-aWokenSentinel-7` | no |
| 14 | `TOOL-aWokenSentinel-9` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aPrimedKeepalive](../aPrimedKeepalive/README.md), [aProbedUnit](../aProbedUnit/README.md)
<!-- /gen:build-edges -->
