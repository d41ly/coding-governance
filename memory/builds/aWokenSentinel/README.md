---
slug: aWokenSentinel
node: a
opened: 2026-09-16
streams: tooling
roster: TOOL
parents: aPrimedKeepalive aProbedUnit
authorized-by: prompt
ids: TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 TOOL-aWokenSentinel-29 TOOL-aWokenSentinel-30
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

- **Every unit ships to adopters through its kit.** A rendered or copy-installed file lands in the template AND its render in one commit.
- **Failure-domain rule.** A mechanism covers a stall class only when it shares none of the stalled session's process, event loop or account for that class; the research record's ranking rule, and why the cron job is demoted rather than fixed.
- **No self-test suite runs inside a pass.** A pass observes the single arm or the staged break; `run-unattended-gates.sh` runs once at the close on a frozen clone, with `run-selftests.sh --kit tools/workflows` beside it from unit 21 on.
- **Vocabulary changes land in every carrier in one commit**: driver, leg, VERBS, SKILL, protocol, conf and its example.
- **The CLI token is the owner's**, minted out of band; unit 5 ships inert until registered and reports an absent login as an announced skip.
- **Classification at open**: all MISSING; specced from the briefs under `prompts/`. Unit 7 ADDED after preflight by `--rescope` on the measured `session_crons` field.
- **Four spec-audit rounds disposed by severity (M4), 2026-09-20**: every BLOCKER and HIGH PROMOTED into units 8-14, 15-20, 21-24, 25-28, one per defect; every MEDIUM and LOW FOLDED. Round 3 swapped orders 7 and 17.
- **The cascade stopped at generation four as M4's CEILING (TOOL-aWokenSentinel-29).** Generations promoted 7, 6, 4, 4; the fourth did not shrink. Units 25-28 build from their disposal-authored specs with no fifth audit; the method defect is TOOL-aWokenSentinel-30.

## Parked decisions

(none yet)

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aWokenSentinel-1` | CLOSED | the run-state file records the lease: `session:` and `pid:` at preflight and resume, and resume re-records the keepalive id |
| 2 | `TOOL-aWokenSentinel-2` | CLOSED | `--liveness <slug>`: the one machine-readable predicate every out-of-session reader shares |
| 3 | `TOOL-aWokenSentinel-3` | CLOSED | `stop-guard`: a `Stop` hook that refuses the turn end of a session bound to a non-terminal run, bounded |
| 4 | `TOOL-aWokenSentinel-4` | CLOSED | `stall-recorder`: a `StopFailure` hook that writes the stall to a sidecar under the git dir |
| 5 | `TOOL-aWokenSentinel-5` | PLANNED | `resume-tick.sh`: the OS-scheduled out-of-process resumer, acting on a stale lease only |
| 6 | `TOOL-aWokenSentinel-6` | PLANNED | the contract: protocol §5, the Skill, the conf knobs and the kit version, with the cron job demoted to the idle-wake |
| 7 | `TOOL-aWokenSentinel-7` | PLANNED | `keepalive-reaped` becomes CHECKED at `--landed` against the cron listing the stop-guard recorded, no longer attested |
| 8 | `TOOL-aWokenSentinel-8` | CLOSED | the stop-guard's `landing-unstamped` row: a bound session at `FINISHED-UNSTAMPED` is BLOCKED and told to run `--landed`, so the `--landed` refusal's end-the-turn remedy is continued rather than allowed (audit B1) |
| 9 | `TOOL-aWokenSentinel-9` | PLANNED | the stop-guard listing as a FIELD on `--status`'s one line, omitted when unrecorded, and the header's one-line promise made an arm (audit H1) |
| 10 | `TOOL-aWokenSentinel-10` | CLOSED | `STOP_GUARD_BLOCKS` declared in every carrier check 22 and spec 6 AC6 read: the example, `optional_keys`, the protocol's section 8 row with its render, the root conf with its rationale and the manifest re-stamp (audit H2) |
| 11 | `TOOL-aWokenSentinel-11` | CLOSED | a kit-gate check that the driver holds ONE derivation of the sidecar root, `resolve_sidecar_dir`, so a second `rev-parse --git-dir` spelling reds the bar for every unit (audit H3) |
| 12 | `TOOL-aWokenSentinel-12` | PLANNED | the tick consults login BEFORE it kills: a logged-out node kills nothing, observed by an arm whose live process survives, and the class left-shifted to `memory/gotchas/` (audit H4) |
| 13 | `TOOL-aWokenSentinel-13` | PLANNED | the tick sources the root `.unattended.conf` into its own shell before its `read_bound_key` calls, so a declared bound is honoured and the NOTE names the file; arms under a declared key (audit H5) |
| 14 | `TOOL-aWokenSentinel-14` | CLOSED | `seed()` in `adopt-unattended.test.sh` commits once, so every fixture that borrows it has a born HEAD and `--liveness`'s `git log` probe is live; the class left-shifted to `memory/gotchas/` (audit H6) |
| 15 | `TOOL-aWokenSentinel-15` | PLANNED | the spec-audit commission's blob-pin pre-flight: the harness's resolver returns each subject's committed blob and working-tree hash, and refuses to dispatch a lens while any differ (audit round 2 B1, B2) |
| 16 | `TOOL-aWokenSentinel-16` | CLOSED | `--landed`'s check 34 accepts the `--no-ff` landing the charter mandates: the marker's commit contains the witness and sits on the remote default branch, with the no-ff fixture arm that is RED today (audit round 2 H1; `TOOL-dUnstalledConvoy-38`) |
| 17 | `TOOL-aWokenSentinel-17` | PLANNED | the driver suite reads `--status` by FIELD: `extract_next` armed on a suffixed line and `check_status_one_line` armed against a two-line driver copy (audit round 2 H2, H3) |
| 18 | `TOOL-aWokenSentinel-18` | PLANNED | `read_bound_key` refuses with exit 2 a caller that named no conf, so a bound read from a shell with `CONF` unset is a refusal rather than a default with an empty NOTE (audit round 2 H4) |
| 19 | `TOOL-aWokenSentinel-19` | PLANNED | `adopt-unattended.test.sh` declares a shrink-only `FLOOR_ASSERTIONS`, and the close's `run-unattended-gates.sh` run is the named observer of every arm the committed `seed()` feeds (audit round 2 H5) |
| 20 | `TOOL-aWokenSentinel-20` | CLOSED | `resolve_sidecar_dir` lives in `lib-unattended.sh`: one derivation of the sidecar root for the driver and the tick, and unit 11's check counts code lines across the three files (audit round 2 H6) |
| 21 | `TOOL-aWokenSentinel-21` | PLANNED | the build harness's suite `unattended-build.test.sh` joins the declared self-test population: a held leg, a budget row, a registry exemption and a shrink-only `FLOOR_ASSERTIONS`, so its supplied-subject fixtures are an executed arm for unit 15's compare (audit round 3 H1) |
| 22 | `TOOL-aWokenSentinel-22` | PLANNED | check 34's two refusal branches unit 16 leaves unarmed get their arms over the suite's marker fixture — the marker with no sha, the marker the remote default branch does not reach — each read RED first against the pre-predicate driver (audit round 3 H2) |
| 23 | `TOOL-aWokenSentinel-23` | PLANNED | a kit-gate check that no shell file in the kit counts a captured variable's lines through `printf '%s
'`, `echo` or a here-string into `wc -l`, the shape that reads an empty capture as one line, with the class in `memory/gotchas/` (audit round 3 H3) |
| 24 | `TOOL-aWokenSentinel-24` | PLANNED | the tick's conf-block staged break is ONE artifact: `build_tick_without_conf_block` in the tick's suite makes the copy from two anchor lines and asserts its shape, so spec 13's and spec 18's arms name a helper and no count (audit round 3 H4) |
| 25 | `TOOL-aWokenSentinel-25` | PLANNED | `check-arms.py` names a STRANDED prefix beside its UNARMED row, in `--report` and in `--check`'s refusal, and prints the whole signature instead of 72 characters of it, so an arm that stops short of a long message is diagnosed with its line rather than read as absent (audit round 4 H1) |
| 26 | `TOOL-aWokenSentinel-26` | PLANNED | the marker region's accepting arm asserts its own entry state before it runs — a committed `LANDING` record, a clean tree, HEAD advertised on `origin main` — so an arm inserted above it that lands the record reds there naming the property that moved (audit round 4 H2) |
| 27 | `TOOL-aWokenSentinel-27` | PLANNED | unit 21's leg enrolled in the three meta-gates that grade a manifest leg: the `PASS ($n assertions)` line, the `gate-legs` dossier claim with the map re-rendered, and the GENERATED `subject-pins.tsv` row (audit round 4 H3, H4, H5) |
| 28 | `TOOL-aWokenSentinel-28` | PLANNED | the `echo` and here-string spellings unit 23's fixture does not stage get their own staged lines and RED readings in the kit gate's suite, over the same suite copy, so every top-level branch of the added-newline predicate has been seen to fail (audit round 4 H6) |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 28 unit(s) · node a · opened 2026-09-16 · streams tooling
ids TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13
ids TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25
ids TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 TOOL-aWokenSentinel-29 TOOL-aWokenSentinel-30

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aWokenSentinel-1 — the run-state file records the LEASE: `session:` and `pid:` at preflight, and `--resume --keepalive-id` replaces it](spec/2026-09-16-spec-TOOL-aWokenSentinel-1.md) | 1 | 2 | CLOSED | rev-4 | 2026-09-20 |
| [TOOL-aWokenSentinel-2 — `--liveness <slug>`, the one machine-readable predicate every out-of-session reader shares](spec/2026-09-16-spec-TOOL-aWokenSentinel-2.md) | 2 | 2 | CLOSED | rev-4 | 2026-09-20 |
| [TOOL-aWokenSentinel-20 — `resolve_sidecar_dir` lives in `lib-unattended.sh`: one derivation of the sidecar root for the driver and the tick, counted in code lines across the three files](spec/2026-09-20-spec-TOOL-aWokenSentinel-20.md) | 3 | 2 | CLOSED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-11 — a kit-gate check that the driver holds ONE derivation of the sidecar root](spec/2026-09-20-spec-TOOL-aWokenSentinel-11.md) | 4 | 2 | CLOSED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-14 — `seed()` commits once, so every fixture that borrows it has a born HEAD](spec/2026-09-20-spec-TOOL-aWokenSentinel-14.md) | 5 | 2 | CLOSED | rev-4 | 2026-09-20 |
| [TOOL-aWokenSentinel-3 — `stop-guard`, the `Stop` hook that refuses a bound session's turn end](spec/2026-09-16-spec-TOOL-aWokenSentinel-3.md) | 6 | 2 | CLOSED | rev-4 | 2026-09-20 |
| [TOOL-aWokenSentinel-16 — `--landed`'s check 34 accepts the `--no-ff` landing the charter mandates: the marker's commit contains the witness and sits on the remote default branch](spec/2026-09-20-spec-TOOL-aWokenSentinel-16.md) | 7 | 2 | CLOSED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-8 — the stop-guard's `landing-unstamped` row: a bound session at `FINISHED-UNSTAMPED` is blocked and told to run `--landed`](spec/2026-09-20-spec-TOOL-aWokenSentinel-8.md) | 8 | 2 | CLOSED | rev-3 | 2026-09-20 |
| [TOOL-aWokenSentinel-10 — `STOP_GUARD_BLOCKS` declared in every carrier check 22 and spec 6 AC6 read](spec/2026-09-20-spec-TOOL-aWokenSentinel-10.md) | 9 | 2 | CLOSED | rev-4 | 2026-09-20 |
| [TOOL-aWokenSentinel-4 — `stall-recorder`, the `StopFailure` hook that writes an API-error stall to disk](spec/2026-09-16-spec-TOOL-aWokenSentinel-4.md) | 10 | 2 | CLOSED | rev-4 | 2026-09-20 |
| [TOOL-aWokenSentinel-5 — `resume-tick.sh`, the OS-scheduled out-of-process resumer](spec/2026-09-16-spec-TOOL-aWokenSentinel-5.md) | 11 | 2 | SPECCED | rev-3 | 2026-09-20 |
| [TOOL-aWokenSentinel-12 — the resume tick consults login BEFORE it kills: a logged-out node kills nothing](spec/2026-09-20-spec-TOOL-aWokenSentinel-12.md) | 12 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-13 — the resume tick sources the root conf before its bound reads, so a declared bound is honoured and the NOTE names the file](spec/2026-09-20-spec-TOOL-aWokenSentinel-13.md) | 13 | 2 | SPECCED | rev-3 | 2026-09-20 |
| [TOOL-aWokenSentinel-18 — `read_bound_key` refuses a caller that named no conf: a bound read from a shell with `CONF` unset exits 2 instead of taking a default with an empty NOTE](spec/2026-09-20-spec-TOOL-aWokenSentinel-18.md) | 14 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-6 — the contract: protocol section 5, the Skill, the README, the conf prose and the dossier, with the cron job demoted to the idle-wake](spec/2026-09-16-spec-TOOL-aWokenSentinel-6.md) | 15 | 2 | SPECCED | rev-3 | 2026-09-20 |
| [TOOL-aWokenSentinel-17 — the driver suite reads `--status` by FIELD: one extraction helper armed on a suffixed line, and a one-line assertion armed against a two-line driver](spec/2026-09-20-spec-TOOL-aWokenSentinel-17.md) | 16 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-7 — `keepalive-reaped` becomes CHECKED: `--landed` reads the harness's own cron listing](spec/2026-09-16-spec-TOOL-aWokenSentinel-7.md) | 17 | 2 | SPECCED | rev-4 | 2026-09-20 |
| [TOOL-aWokenSentinel-9 — the stop-guard listing as a FIELD on `--status`'s one line, and the one-line promise made an arm](spec/2026-09-20-spec-TOOL-aWokenSentinel-9.md) | 18 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-19 — the adopter suite declares a shrink-only `FLOOR_ASSERTIONS`, and the close's kit-gate run is the named observer of every arm the committed `seed()` feeds](spec/2026-09-20-spec-TOOL-aWokenSentinel-19.md) | 19 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-15 — the spec-audit commission pins each subject at its committed blob and refuses a dirty subject before a lens is dispatched](spec/2026-09-20-spec-TOOL-aWokenSentinel-15.md) | 20 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-21 — the build harness's suite joins the declared self-test population: a held leg, a budget row, a registry exemption and a shrink-only `FLOOR_ASSERTIONS`, so its supplied-subject fixtures are an executed arm](spec/2026-09-20-spec-TOOL-aWokenSentinel-21.md) | 21 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-22 — check 34's two refusal branches unit 16 leaves unarmed get their arms: the marker with no sha and the marker the remote default branch does not reach, each read RED first](spec/2026-09-20-spec-TOOL-aWokenSentinel-22.md) | 22 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-23 — a kit-gate check banning the line count that reads an empty capture as one line: `printf '%s\n'`, `echo` or a here-string into `wc -l` over a captured variable, with the class in `memory/gotchas/`](spec/2026-09-20-spec-TOOL-aWokenSentinel-23.md) | 23 | 2 | SPECCED | rev-2 | 2026-09-20 |
| [TOOL-aWokenSentinel-24 — the tick's conf-block staged break is ONE artifact: `build_tick_without_conf_block` in the tick's suite makes the copy from two anchor lines and asserts its shape, so both arms that stage it name a helper and no count](spec/2026-09-20-spec-TOOL-aWokenSentinel-24.md) | 24 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-25 — `check-arms.py` names a STRANDED prefix beside its UNARMED row and prints the whole signature, so an arm that stops short of a long message is diagnosed rather than read as absent](spec/2026-09-20-spec-TOOL-aWokenSentinel-25.md) | 25 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-26 — the marker region's accepting arm asserts its entry state before it runs: a committed `LANDING` record, a clean tree and HEAD advertised on `origin main`](spec/2026-09-20-spec-TOOL-aWokenSentinel-26.md) | 26 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-27 — unit 21's leg satisfies the three meta-gates that grade a manifest leg: the `PASS` count line, the `gate-legs` dossier claim with the map re-rendered, and the `subject-pins.tsv` row](spec/2026-09-20-spec-TOOL-aWokenSentinel-27.md) | 27 | 2 | SPECCED | rev-1 | 2026-09-20 |
| [TOOL-aWokenSentinel-28 — the `echo` and here-string spellings unit 23 does not stage get their own staged lines and RED readings, so every branch of the added-newline predicate has been seen to fail](spec/2026-09-20-spec-TOOL-aWokenSentinel-28.md) | 28 | 2 | SPECCED | rev-1 | 2026-09-20 |
<!-- /gen:build-units -->

Records: 45 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aWokenSentinel-1` | no |
| 2 | `TOOL-aWokenSentinel-2` | no |
| 3 | `TOOL-aWokenSentinel-20` | no |
| 4 | `TOOL-aWokenSentinel-11` | no |
| 5 | `TOOL-aWokenSentinel-14` | no |
| 6 | `TOOL-aWokenSentinel-3` | no |
| 7 | `TOOL-aWokenSentinel-16` | no |
| 8 | `TOOL-aWokenSentinel-8` | no |
| 9 | `TOOL-aWokenSentinel-10` | no |
| 10 | `TOOL-aWokenSentinel-4` | no |
| 11 | `TOOL-aWokenSentinel-5` | no |
| 12 | `TOOL-aWokenSentinel-12` | no |
| 13 | `TOOL-aWokenSentinel-13` | no |
| 14 | `TOOL-aWokenSentinel-18` | no |
| 15 | `TOOL-aWokenSentinel-6` | no |
| 16 | `TOOL-aWokenSentinel-17` | no |
| 17 | `TOOL-aWokenSentinel-7` | no |
| 18 | `TOOL-aWokenSentinel-9` | no |
| 19 | `TOOL-aWokenSentinel-19` | no |
| 20 | `TOOL-aWokenSentinel-15` | no |
| 21 | `TOOL-aWokenSentinel-21` | no |
| 22 | `TOOL-aWokenSentinel-22` | no |
| 23 | `TOOL-aWokenSentinel-23` | no |
| 24 | `TOOL-aWokenSentinel-24` | no |
| 25 | `TOOL-aWokenSentinel-25` | no |
| 26 | `TOOL-aWokenSentinel-26` | no |
| 27 | `TOOL-aWokenSentinel-27` | no |
| 28 | `TOOL-aWokenSentinel-28` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [aPrimedKeepalive](../aPrimedKeepalive/README.md), [aProbedUnit](../aProbedUnit/README.md)
<!-- /gen:build-edges -->
