---
slug: aWokenSentinel
node: a
opened: 2026-09-16
streams: tooling
roster: TOOL
status: OPEN
parents: aPrimedKeepalive aProbedUnit
authorized-by: prompt
ids: TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7
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
| 7 | `TOOL-aWokenSentinel-7` | PLANNED | `keepalive-reaped` becomes CHECKED at `--close` against the cron listing the stop-guard recorded, no longer attested |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-09-16 · streams tooling
ids TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 3 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aPrimedKeepalive](../aPrimedKeepalive/README.md), [aProbedUnit](../aProbedUnit/README.md)
<!-- /gen:build-edges -->
