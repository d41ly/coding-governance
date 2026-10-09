# TOOL-aFrugalTurnstile-5 — the gate turnstile is host-wide, names its holder, lets nested bars through, and `--hold` admits a foreign bar

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 2 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

Implements design D6. On 2026-10-09 gov's, inCMS's and NicoCares's bars ran at once on one host
because the turnstile is keyed on each repository's git common dir, and they starved each other into
timeouts and load flakes. One bar per machine: the beacon and the queue move to a host directory, a
queued bar names who holds the host, a bar started inside a holder's own process tree does not queue
behind its parent, and a bar that is not this runner can enter the queue through `--hold`.

## 2. Scope (IN)

- **S1 — the host directory.** In `tools/run-gates/run-gates.sh`'s turnstile block (~1088-1512),
  with the turnstile on, `TS_HOST` resolves `${GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile}`,
  creates it with `mkdir -p`, and makes it absolute with `cd … && pwd`. `TS_DIR_C` becomes
  `$TS_HOST/gate-bar-beacon` and `TS_Q` becomes `$TS_HOST/gate-bar-queue`. `TS_COMMON` is still
  resolved exactly as at base and still feeds `RG_HEALTH_LOG` and `WORK_COMMON`, so the health log,
  the scratch-dir owner record and the dead-bar sweep stay per common dir. When `TS_HOST` cannot be
  created or resolved, the runner prints one NOTE line and uses `TS_COMMON` for both paths, which is
  base behaviour. `QUEUED_FROM` reads `unresolved` when neither resolves. Observed by AC1, AC12.
- **S2 — the beacon names its holder.** The claiming branch also writes `repo` (`$ROOT`), `run`
  and `ttl` (`$TS_TTL`) into the beacon dir beside `heartbeat`, `pid` and `nonce`. `run` is the run
  id, so its derivation, `${GATE_RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)-$$}`, moves from ~1914 to just
  above the turnstile block into `TS_RUN`, and ~1914 assigns `RUNID="$TS_RUN"`. Observed by AC2.
- **S3 — staleness is judged against the holder's TTL.** `ts_try_reap` reads `ttl` from the
  beacon; a positive integer is the bound, anything else, as from a beacon an older runner wrote,
  falls back to the waiter's own `TS_TTL`. The reap line and its health-event detail print the bound
  used. Observed by AC5.
- **S4 — the queue line names the holder.** At ~1439 the leading clause only changes, to the two
  queue lines of §4's Messages table, each absent beacon field printed as `-`. The tail, the
  `gate queue: waited` line and the `gate queue: acquired` line stay byte-identical. Observed by AC1,
  AC5.
- **S5 — a holder exports its nonce, and a bar inside it nests.** A run that holds the beacon
  (`TS_HELD=1`) exports `GATE_TURNSTILE_HOLDER="$TS_NONCE"` before its first leg. Before taking a
  ticket, a runner whose inherited `GATE_TURNSTILE_HOLDER` is non-empty and equal to the live
  beacon's `nonce` is NESTED: it takes no ticket, never claims, prints
  `gate queue: nested under <run> — <repo> pid <pid>` from the beacon's fields, keeps the inherited
  value for its own legs, and records `queued` `0` and `queued_from` `nested`. The `waited 0s` and
  `acquired … from nested` lines are printed as for any run. Observed by AC3.
- **S6 — `--hold -- <command…>`.** Parsed right after the `cd "$ROOT"` at ~99, before anything reads
  `$1`: the command words are saved and the positional arguments cleared, and `--hold` with no `--`
  or no command word exits 2 with §4's usage line. The run then passes through the same prelude a bar does, takes the turnstile (or
  nests, or runs unqueued under `GATE_TURNSTILE=0` or a WAIT EXPIRED, each announced as for a bar),
  and immediately after the `gate queue: acquired` line runs the saved command from the repository
  top level with `GATE_TURNSTILE_HOLDER` exported when it holds. It then runs `ts_tick_stop`,
  `ts_release` and `ts_drop_ticket`, and exits with the command's status. It writes no run record,
  no ledger row and no stamp. Observed by AC6, AC7.
- **S7 — every other reader of the two paths follows them.**
  - `tools/unattended/unattended.sh` `print_interrupted_acts` (~5884) reads the queue at
    `${GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile}/gate-bar-queue`, the runner's spelling. A blind
    probe there reports "no interrupted act" over a queue it never read. Observed by AC9.
  - `tools/run-gates/run-selftests.sh` exports a per-row `GATE_TURNSTILE_DIR` under each row's
    private `TMPDIR`, so pooled suites isolate their fixture bars as separate common dirs did, and
    its comment at ~1200 stops claiming the beacon sits under the common dir. Observed by AC11.
  - The suites that assert a fixture bar's turnstile state isolate it: the turnstile suite and the
    evidence suite export `GATE_TURNSTILE_DIR` to their own scratch in the prologue, the turnstile
    suite's `beacon()` and `queue()` helpers return paths under it, and `run-gates.test.sh`'s AC3 and
    AC5 arms plant and its OM arm reads the beacon there. NOT OBSERVED in the pass: suite edits run
    at VERIFYING.
- **S8 — the knob classes.** `GATE_TURNSTILE_DIR` and `GATE_TURNSTILE_HOLDER` join
  `BAR_INERT_KNOBS` in `.githooks/pre-push.test.sh`'s H49 arm, beside `GATE_TURNSTILE`, with one
  comment line each (F1). Observed by AC8.
- **S9 — the text.** The turnstile block's header comment and `tools/run-gates/README.md`'s section
  "The turnstile — one bar per repository" are rewritten, not appended to: one bar per host, the
  beacon's fields, the holder's TTL, nesting, `--hold`, the fallback, and the `queued_from` values
  named without a count. Observed by AC10, AC13.

## 3. Non-goals (OUT)

- Changing the TTL, `TS_MAXWAIT` or the ticker cadence derivations.
- The health log, which stays per common dir.
- The two-waiters reap race of `TOOL-aReapedTicket-4`, which a host-wide queue makes likelier and
  which this unit does not absorb.
- `run-gates.sh`'s held-count summary line, which belongs to the concurrent `aBenchedProbe` run.
- Starting a post-merge bar (TOOL-aFrugalTurnstile-6 and -8).

### Edges

- **hands-off** `TOOL-aFrugalTurnstile-6` — the `--hold` verb its post-merge script runs the
  declared bar through, so that bar takes the next idle slot on the host.

## 4. Design

A nested run is the reason the host key cannot deadlock. Before this unit a fixture bar inside a
suite resolved its scratch repo's common dir and never met its parent; under a host key it would
queue behind the very bar whose leg started it. The holder's nonce, exported to its legs and compared
with the LIVE beacon, says "I am inside the bar that holds this host". It is compared, not merely
present, so a value left in some shell by a dead bar nests nothing once a successor holds.

Outside any bar, a fixture bar uses the host directory and serializes against real bars, which is
D6's intent. Pooled suites under `run-selftests.sh` are isolated per row instead (S7), so a pool
does not serialize its own rows.

`--hold` exits before the scratch-dir block, so the held command runs with the turnstile's own traps
armed (`ts_tick_stop; ts_release; ts_drop_ticket` on EXIT, INT, TERM and HUP) and nothing else.

### Messages

| Event | Line |
|---|---|
| queued, holder present | `run-gates: another bar holds this host — <repo> run <run> pid <pid> — queued at position N (waited Ns)` |
| queued, no holder | `run-gates: no bar holds this host, but a ticket sorts ahead of this one — queued at position N (waited Ns)` |
| nested | `gate queue: nested under <run> — <repo> pid <pid>` |
| host dir unusable | `run-gates: NOTE - the host turnstile directory '<dir>' could not be created, so this bar queues per repository under <common dir>` |
| `--hold` usage | `run-gates: --hold needs a command: run-gates.sh --hold -- <command…>` |

### Inventory

No function is minted; the nested test and `--hold` are inline. New names: `TS_HOST`, `TS_RUN`,
`TS_NESTED` (shell variables); `GATE_TURNSTILE_DIR`, `GATE_TURNSTILE_HOLDER` (environment knobs,
classified by S8); `repo`, `run`, `ttl` (beacon files); `nested` (a `queued_from` value); `--hold`
(a runner verb).

### Rollout

Serialization is complete only when every repository on the host runs a runner carrying this
change. An older runner keys on its common dir and does not see the host beacon, so it runs beside a
new one exactly as two repositories do today. This unit writes `tools/unattended/unattended.sh`
beside TOOL-aFrugalTurnstile-3 and `.githooks/pre-push.test.sh` beside TOOL-aFrugalTurnstile-2, all
three in order group 2, so the passes are not write-disjoint and sequence. The README's build-level
rule lists `unattended.sh` writers as 3 and 9; this unit is a third.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/README.md`
- `tools/run-gates/run-selftests.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/unattended/unattended.sh`
- `.githooks/pre-push.test.sh`

### Alternatives rejected

- **Reusing `GATE_TURNSTILE_HELD`**, the existing lineage marker, as the holder nonce: it is a
  comma-joined list, it is exported after the wait loop on the expired and unticketed paths too,
  where no beacon is the run's, and the H49 arm already classes it INERT as a marker. D6 names one
  nonce exported only on a hold.
- **A flock-style lock**: `flock` does not exist on this platform; the directory create is already
  the atomic claim.

## 5. Production-readiness checklist

- security — nesting trusts an inherited nonce that any process on the host can read from the
  beacon. Nesting decides contention and never a verdict, and so do `GATE_TURNSTILE=0` and
  `GATE_TURNSTILE_DIR`, which is why S8 classes both new knobs INERT beside the first.
- perf / scale — a host-wide queue lengthens waits, inside the same `TS_MAXWAIT` bound the
  unattended backstop already charges; the saving is bars that no longer fail on load.
- error / empty / loading states — an unusable host dir falls back to base behaviour, announced; an
  older beacon's absent fields print `-` and its TTL falls back to the waiter's.
- observability — the holder line, the nested line, the `nested` header value, the fallback NOTE.
- risks — a push made from inside a held bar nests, because S8 does not scrub the holder (F1); a
  suite run directly while a real bar runs now waits behind it, which is the intent. The race of
  `TOOL-aReapedTicket-4` is likelier with more waiters.
- testing — the arms in §7; the pass observes AC1 to AC13 in scratch fixtures.
- migration — none; the first bar after the change creates the host dir.
- user docs — the README section (S9).

## 6. Acceptance criteria

The fixtures are scratch repos under the session scratch built the way the turnstile suite's
`mk_repo` builds one: the runner, `gate-profiles.txt`, `gate-fingerprint.sh` and the python resolver
copied in, an occupancy leg and a long leg, committed. Every case runs the base runner
(`git show bef97330:tools/run-gates/run-gates.sh`) first, then the changed one.

- **AC1** — When repo 1 runs a long bar and repo 2 starts a bar while it holds, both under one
  `GATE_TURNSTILE_DIR`, repo 2's output carries `another bar holds this host —` naming repo 1's top
  level, its run id and its pid, and the occupancy peak is 1. Red when: the peak is 2 with no queue
  line, which is the base runner's behaviour.
- **AC2** — When repo 1 holds, the beacon under `GATE_TURNSTILE_DIR` holds `repo`, `run` and `ttl`
  files equal to repo 1's top level, its header's run id and its TTL. Red when: any is absent.
- **AC3** — When a leg of the holder starts a runner in another scratch repo with
  `GATE_TURNSTILE_HOLDER` inherited, that runner prints `gate queue: nested under`, takes no ticket,
  and its header reads `queued_from` `nested`; when the same leg unsets the knob, the inner runner
  prints `queued at position` instead. Red when: the inherited case queues.
  cost: the unset case waits out a `TS_MAXWAIT` of 20 s under a TTL of 5.
- **AC4** — When the host beacon names a dead pid, the next bar prints
  `reaping the beacon of a dead holder` and runs. Red when: it queues.
- **AC5** — When the host beacon carries `ttl` 600, a heartbeat 400 s old and a live pid, a waiter
  whose `GATE_TURNSTILE_TTL` is 60 prints `another bar holds this host` within 8 s and no `reaping`
  line, and the beacon still exists when the waiter is killed; when the beacon carries no `ttl`, the
  waiter reaps it as `stalled` with `ttl 60s`. Red when: the first case reaps, which the base runner
  does over a beacon planted in its common dir.
- **AC6** — When the changed runner runs with `--hold -- false`, it exits 1 and the host dir holds no
  `gate-bar-beacon`; when the held command prints `GATE_TURNSTILE_HOLDER` and the beacon's `nonce`,
  the two are equal, and the runner with `--hold -- true` exits 0. Red when: the base runner, which ignores `--hold`,
  runs the scratch repo's legs and prints `gates GREEN`.
- **AC7** — When the changed runner runs with `--hold` and no command, it exits 2 and prints
  `--hold needs a command`. Red when: it exits 0.
- **AC8** — When `check_knob_classes` is evaluated out of the hook suite with its
  `BAR_INERT_KNOBS` line and run over the changed runner, it prints nothing; over a copy of the
  runner reading a planted `GATE_TURNSTILE_PLANTED`, it names that knob. Red when: either new knob
  reads `unclassified-or-twice`.
- **AC9** — When `print_interrupted_acts` is evaluated out of `tools/unattended/unattended.sh` in a
  scratch repo with a dead-pid ticket planted in `GATE_TURNSTILE_DIR`'s queue, it prints
  `INTERRUPTED — a turnstile ticket names a pid that is not running`. Red when: it prints
  `no interrupted act`, which the base driver does.
- **AC10** — When `grep -c 'GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile'` runs over the runner
  and over `tools/unattended/unattended.sh`, each prints at least `1`.
  Red when: either prints `0`.
- **AC11** — When `grep -n 'GATE_TURNSTILE_DIR' tools/run-gates/run-selftests.sh` runs, it shows
  the per-row export beside the row's private `TMPDIR`. Red when: it shows none.
- **AC12** — When `GATE_TURNSTILE_DIR` names an existing regular file, the bar prints
  `could not be created, so this bar queues per repository` and its beacon appears under the scratch
  repo's common dir. Red when: the bar runs with no beacon anywhere.
- **AC13** — When `grep -c '## The turnstile — one bar per host' tools/run-gates/README.md` and
  `grep -c 'NESTING TRUSTS AN INHERITED NONCE'` over the runner run, each prints `1`.
  Red when: either prints `0`.

## 7. Gates

`run-gates turnstile` · `run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `run-selftests self-test` · `pre-push self-test` · `unattended kit gate` · `install-prefix (shipped surface)` · `remote literals (kit code names no remote)` · `foreign-prefix parity (every self-test at three prefixes)` · `testsuite counts (every bar self-test prints one)`

New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC12 · two scratch repos under one host dir, a planted beacon per case, each run against the base runner first · `FLOOR_ASSERTIONS` raised by the assertions it adds
New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC10 · the default host directory spelled identically in the runner and in the unattended driver, located with the suite's `resolve_kit_dir` and skipped with an announcement where that kit is absent · `FLOOR_ASSERTIONS` raised likewise
New arm: tools/unattended/unattended.test.sh · covers AC9 · a dead-pid ticket planted in the host queue · none
New arm: .githooks/pre-push.test.sh · covers AC8 · the H49 class arm over the changed runner · none

The sentence S9 adds to the turnstile block's header, quoted: "WHAT THIS DOES NOT CHECK: NESTING
TRUSTS AN INHERITED NONCE, which any process on this host can read from the beacon, so nesting
decides contention and never a verdict; and a runner older than this change keys on its common dir
and does not see the host beacon."

## 8. Open questions

- **FACT-QUESTION · F1 — Does scrubbing `GATE_TURNSTILE_DIR` and `GATE_TURNSTILE_HOLDER` from the
  boundary's bar, as the brief and design D6 ask, narrow anything the environment cannot already
  do?** Probe: the H49 classification at base, `GATE_TURNSTILE` in `BAR_INERT_KNOBS`
  (`.githooks/pre-push.test.sh` ~1244) and absent from the hook's `BAR_SCRUBBED_KNOBS` (~1421); and
  a fixture in which a leg of a holding bar pushes through a real hook to a scratch remote. Observed
  at writing time by the read: `GATE_TURNSTILE=0`, which disables the queue outright, already
  reaches the boundary's bar, so scrubbing a narrower knob closes nothing. The fixture observation
  that decides the holder half: a scrubbed holder makes that inner bar queue behind its own parent
  until `TS_MAXWAIT`. Liveness: had `GATE_TURNSTILE` been in `BAR_SCRUBBED_KNOBS` the read would
  favour scrubbing, and an unscrubbed holder in the fixture prints `nested under`, so both halves
  can read the other way.
  RESOLVED (agent, 2026-10-09, delegated): classify both INERT (S8) and scrub neither; the
  main loop owes design D6 a rev line for this departure.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft from design D6, the turnstile block read at base bef97330.

## 10. Reuse audit

`reuse_lookup.py "serialize concurrent gate bars with a lock that names its holder"` returned no
seam outside the runner itself; the seams extended are the turnstile block's own `ts_try_reap`,
`ts_release`, ticket queue and traps, the `--print-profile` early-verb pattern for `--hold`'s
placement, `run-selftests.sh`'s per-row private `TMPDIR` for the per-row host dir, and the H49
class arm for the knobs. The recall probe names `TOOL-aReapedTicket-4` (the two-waiter race, left
out in §3) and `TOOL-aBoundedCeiling-12` (dead tickets), and the nesting deadlock a round-2 review
of `aBoundedCeiling` found, which S5 removes by construction.

Recall terms used: turnstile beacon queue ticket nonce heartbeat ttl reap stalled holder common dir nested deadlock
