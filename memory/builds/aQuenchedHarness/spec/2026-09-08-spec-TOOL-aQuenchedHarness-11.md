# TOOL-aQuenchedHarness-11 — the strays a stopped run leaves behind, named on demand

**Status:** SPECCED · rev-1 · 2026-09-08 · node a · Tier-2 · base ab58d1cc · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aQuenchedHarness-11-probe-design.md](../build/2026-09-08-build-TOOL-aQuenchedHarness-11-probe-design.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

A stopped run does not stop. Measured on this node 2026-09-08: a runner killed with TaskStop 7.5 h
earlier was still executing with its whole child tree, nine copies of one suite were live where one
was intentional, and two busy-wait loops had burned 12.8 core-hours waiting on a file that could
never arrive. None of it was visible in the output files being watched, and every timing measured
beside it was reported as clean. Give a session one command that answers which of its long-running
gate jobs are still alive, which are orphans, and what that is costing — and let it reap the ones it
can prove nobody owns.

## 2. Scope (IN)

- **S1** — `tools/run-gates/gate-strays.sh`, four verbs: default report, `--count-foreign` (one
  integer on stdout), `--json`, and `--reap`. Report goes to stderr; the two machine shapes own
  stdout. AC1, AC2.
- **S2** — A chain tag. Three wrappers each export `GOV_GATE_CHAIN`, appending their own run id, so
  a process's ancestry is readable from its own environment rather than reconstructed from a parent
  chain that TaskStop has already broken. Deliberately NOT `GATE_RUN_ID`, which the runner reads as
  an override and which a bar leg already pins. AC3.
- **S3** — Fixture roots carry the chain root in their name (`tools/lib/lib-selftest.sh`, one line),
  so litter left by a dead run is attributable rather than merely old. An unset chain falls through
  to a plain `mktemp -d` and is reported untagged rather than guessed at. AC4.
- **S4** — The probe's own liveness, graded on the JOIN and not on "did it run": four checks, each
  with a reachable red, that distinguish a clean board from a blind one. AC5, AC6.
- **S5** — A reap that refuses more than it kills. Only a process whose chain ROOT is dead by two
  independent readers, never a live root, an unreadable environ, an untagged process, or anything at
  all when a liveness check failed. AC7, AC8.
- **S6** — Two rows in `run-gates.sh`'s existing header block recording foreign gate load at the
  time of the run, so a bar measured beside other gate work says so in its own record. `?` and `0`
  are distinguishable. AC9.
- **S7** — `tools/run-gates/gate-strays.test.sh`, held off the bar per the 2026-08-23 ruling, with a
  `selftest-budgets.txt` row and a `kit.toml` claim. AC10.

## 3. Non-goals (OUT)

- **The two worst things in the incident are OUT OF REACH and the tool says so rather than implying
  coverage.** A busy-wait loop and a Monitor `grep` are spawned by harness tool calls, carry no chain
  and can never carry one. They are reported `UNTAGGED` with an age and a CPU price and no judgement,
  and are never reaped. Pattern-matching command lines would reach them and is exactly what makes the
  stopgap unsafe to let kill on a shared machine.
- **It is not a stall detector.** CPU is priced against age and is never an input to any verdict in
  either direction, because a healthy bar prints nothing for an hour and a 61-hour stale monitor
  burns 0.03% of a core. The per-leg ceiling and the whole-run wall stay the only killers.
- **It does not replace or repair the turnstile.** §10 records that the turnstile already keeps
  beacons, holder pids and heartbeats, and that two open backlog rows say its reap predicate has no
  liveness test on the tickets themselves. That is a different unit against a different mechanism;
  this one covers jobs no turnstile beacon ever describes.
- **No bar leg, no hook, no watcher process.** `--reap` is human-typed. A reaper on a hook is a
  reaper that eventually kills something it should not, at the moment nobody is watching.
- **No native Windows process is killed by this tool.** It prints the `taskkill` line and stops.

### Edges

- **consumes-from** `TOOL-aQuenchedHarness-10` — the guarded A/B harness that unit built proves a box
  quiet before trusting a timing. This unit answers WHY a box was not quiet.
- **hands-off** `none`

## 4. Design

### The pid-space trap, which decides the whole shape

MSYS and Windows keep different pid spaces, verified on this box: one live process is msys `2543011`
and Windows `31208`; `kill -0` succeeds on the first and fails on the second. Every one of three
independent designs put a Windows pid in the kill path. **The forest and the kill therefore stay in
msys space** (`ps -ef`), and CIM is used only as a CPU lookup joined on `/proc/<pid>/winpid`, with a
failed join printing `cpu unavailable` rather than a number belonging to someone else.

### Attribution

A process is judged only if it carries `GOV_GATE_CHAIN` in its own environment and that chain's ROOT
is a run id this tree minted. The chain root is a chain, not a scalar, so a nested runner is
attributable to the outermost run rather than to its immediate parent — which is the relationship
TaskStop destroys.

`/proc` is INSTANCE-SCOPED on Windows: measured 12 directories against 41 `ps -ef` rows. So most
processes' environments are unreadable from here, and the tool prints that ratio every run and
REFUSES those rows by name. It is blind to another session's orphans by construction and says so.

### Liveness, graded on the join

Four checks before any row prints: the probe reads its own chain back through `/proc/self/environ`;
foreign-read coverage is an assertion, so zero readable with candidates present is `DEAD PROBE`; the
snapshot parse ratio must exceed one half, because six of eight sampled `ps -ef` rows were argv
continuations; and the probe's own CPU must resolve, whose failure disarms the CPU column WITHOUT
disarming attribution. `NOT ASKED` is a third state, keyed per program: a tree where no wrapper is
wired is never `CLEAN`.

### Alternatives rejected

- **A detached watchdog started by the runner.** It is one more process to orphan, and the incident
  was orphans.
- **`rows > 0` as the liveness assertion.** All three candidate designs used it. It passes on an arm
  that sees 4% of the box, which is the state actually measured.
- **"Did anything advance globally?"** returns movers even at a zero gap, because enumeration itself
  burns CPU. Near-unfailable, and it would have reported a healthy probe throughout the incident.

### Files touched (estimate)

`tools/run-gates/gate-strays.sh` (new) · `tools/run-gates/gate-strays.test.sh` (new) ·
`tools/run-gates/run-gates.sh` · `tools/run-gates/run-selftests.sh` ·
`tools/unattended/run-unattended-gates.sh` · `tools/lib/lib-selftest.sh` ·
`tools/run-gates/kit.toml` · `tools/run-gates/selftest-budgets.txt`

## 5. Production-readiness checklist

- security — a kill path. Every refusal in S5 is a security control, not a nicety: the failure mode
  is killing another session's work on a shared machine.
- perf / scale — ~1.9 s and 3 processes on Windows, ~0.1 s and 2 on POSIX; `--count-foreign` ~0.6 s
  once per bar. It must stay cheap enough to run constantly or it will not be run at all.
- error / empty / loading states — `NOT ASKED`, `REFUSED`, `DEAD PROBE` and `UNTAGGED` are all
  first-class outputs; the tool has no silent path.
- observability — two additive rows in `run-gates.sh`'s existing header, `?` distinct from `0`.
- risks — the msys/Windows pid join is the one that bites; a mis-resolved join in the kill path is
  unrecoverable, so the last step across that boundary stays with a human.
- testing — AC10's suite, held, with every red in §6 staged.
- migration — none. An unset `GOV_GATE_CHAIN` degrades to untagged everywhere.
- user docs — the tool's own header, per this repo's convention that a gate states what it does NOT
  check.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/gate-strays.sh` runs on a tree with a live gate run, it prints
  a `LIVE` row naming that run's chain root. Red when: the row is absent, so a wired tree reads as
  unwired.
- **AC2** — When `--count-foreign` runs, stdout is exactly one integer and nothing else. Red when:
  a report line leaks to stdout and the header row records a string where a count belongs.
- **AC3** — When a run started through a wired wrapper is killed and its children survive, each
  survivor prints `STRAY` naming the dead root. Observed by starting `run-selftests.sh`, killing only
  its wrapper, and running the probe. Red when: the children print `UNTAGGED`, which is what the
  chain exists to prevent.
- **AC4** — When a fixture root outlives a dead chain root, it prints `LITTER` with its age.
  `tools/lib/lib-selftest.sh`. Red when: it prints `UNTAGGED FIXTURES`, meaning the mktemp tag did
  not take.
- **AC5** — When `/proc/self/environ` cannot be read, the tool prints `DEAD PROBE` and exits 3
  without printing a single row. Red when: it prints rows, because a partial board reads as a board.
- **AC6** — When candidates exist but zero foreign environments are readable, the tool prints
  `DEAD PROBE` rather than `CLEAN`. Red when: it reports `CLEAN · 0 stray`, which is the exact
  reassuring-zero this repo's doctrine exists against.
  fixture: reachable by pointing the probe at a snapshot whose rows have no readable `/proc` entry.
- **AC7** — When `--reap` meets a process whose chain root is still live, it prints `REFUSED` and the
  process survives. Red when: it is killed, which is the unsafe-kill class.
- **AC8** — When any liveness check has failed, `--reap` kills nothing at all. Red when: it reaps on
  a blind board.
- **AC9** — When a bar runs beside foreign gate work, `run-gates.sh`'s header carries a non-zero
  `foreign_gate_procs`, and `?` when the probe could not answer. Red when: `?` and `0` collapse to
  one value, so a broken probe reads as a quiet box.
- **AC10** — When `bash tools/run-gates/gate-strays.test.sh` runs, every red above is staged and
  observed. Red when: an arm asserts a message the tool cannot emit.
  cost: held off the bar per the 2026-08-23 owner ruling; on demand only.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/run-gates/gate-strays.test.sh` · stages every red in §6 including the two DEAD PROBE
branches · no floor to move, it is a new suite.

## 8. Open questions

None blocking. One parked: the turnstile's own reap predicate has two open defects (§10). Whether
this tool should eventually subsume it, or whether the turnstile should be fixed in place, is a
decision for whoever picks up `TOOL-aBoundedCeiling-12`.

## 9. Revision log

- rev-1 · 2026-09-08 · specced from a four-lens survey and three adversarially-judged designs, all
  three of which scored 3/10 from their own reviewers. Two design-killing facts were verified
  directly on this box rather than taken from the survey: the msys/Windows pid split, and `/proc`
  covering 12 of 41 processes. The synthesis is in the build folder's research record.

## 10. Reuse audit

The turnstile in `tools/run-gates/run-gates.sh` ALREADY keeps the machinery this unit's problem
suggests: a beacon directory, holder pids, heartbeats with a TTL, and a reap path that prints
`reaping the beacon of a dead holder`. It is not reusable here and the reason is recorded rather than
assumed: it describes holders of the gate bar, and every process in the incident — suite children,
sweep runners, busy-wait loops, Monitor greps — holds no beacon and never will. Two open rows say the
mechanism is itself unsound: `TOOL-aBoundedCeiling-12` (the acquire predicate has no liveness test on
the tickets, so a dead ticket sorts first forever, twice-reproduced) and `TOOL-aSurfacedLexicon-25`
(two reap paths, two behaviours, only one runs a bar). This build's own round-2 review recorded the
same class a third time in H2 against unit 8. So the seam exists, is adjacent, is known-broken, and
covers a disjoint population; this unit extends nothing and says why. No existing seam fits.

Recall terms used: orphan process liveness reap turnstile beacon attribution pid session worktree
stray watchdog CPU sample.
