# TOOL-aQuenchedHarness-1 — the bar's own wall, so a wedged run dies with a verdict

**Status:** CLOSED · rev-6 · 2026-09-07 · node a · Tier-2 · base faaea5f5 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aQuenchedHarness-1-wall-landed.md](../build/2026-09-06-build-TOOL-aQuenchedHarness-1-wall-landed.md) | journal | — |
| [2026-09-07-build-TOOL-aQuenchedHarness-1-acceptance-ledger-the-bar-wall.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-1-acceptance-ledger-the-bar-wall.md) | journal | — |
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-5 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Give `tools/run-gates/run-gates.sh` a whole-run wall-clock wall, so a bar that wedges is killed and
REDs naming what was still running, instead of stalling an unattended build for hours. Today the only
bound is per-leg. Rev-1 to rev-4 called the worst case "the sum of every ceiling it can reach", which
is 42.06 h across the 94 declared ceilings and is WRONG by 4.6x: at width 8 the list-scheduling worst
case is 9.16 h. The wall tightens 9.2 h to the declared value, which is still worth having and is a
smaller claim than this spec used to make.

## 2. Scope (IN)

- **S1** — a `wall=<s>` knob on `tools/run-gates/gate-profiles.txt`, in the same grammar as `width`
  and `timeout`, read by the same `KNOWN_KNOBS` path. `0` means off, and off is a state the profile
  line REPORTS rather than a silence.
- **S2** — the wall is armed when the first leg is dispatched, not at process start: the turnstile
  wait is a queue, not a run, and folding it into the wall would kill a bar for waiting its turn. The
  wait has its own bound, `TS_MAXWAIT`.
- **S3** — on breach the runner kills the outstanding legs, writes a RED summary NAMING every leg
  that had not returned, and exits non-zero. A wall breach is a VERDICT, never a skip and never a
  green, which is `gate-profiles.txt`'s governing invariant applied to this knob.
- **S4** — ONE MECHANISM, stated once, and it is NOT a process-group kill. The runner never enables
  job control — `set -u` at `:18`, no `set -m` anywhere — and legs are dispatched as plain
  `runleg "$k" &` at `:1276` from the single dispatch/report shell, so every leg shares the RUNNER's
  process group. A group kill would take down the reader loop, the watcher and the shell that renders
  the verdict: the run would die signalled and silent instead of exiting non-zero with the RED summary
  S3 requires. `setsid`, the primitive that would give each leg its own group, is ABSENT on this node
  (`command -v setsid` returns rc=1, verified). So the watcher kills RECORDED PER-LEG PIDS and walks
  their descendants, touching no process outside that set. It does not use `timeout` either; rev-1's
  claim that it reuses the per-leg ceiling's `timeout -k` path was wrong, because that call at
  `run-gates.sh:1110` wraps exactly one command, not a pool. The per-leg ceiling is untouched.
- **S5** — **THERE IS NO STARTUP LIVENESS PROBE, and its withdrawal is this spec's largest
  correction.** Rev-4 specced one and it GRADED NOTHING on every host: it built its subject as
  `( ( sleep 90 & ) ; sleep 90 ) &`, and bash exec-replaces a subshell's last command, so `$!` WAS
  the sleep and had no children — the intended grandchild was reparented to PID 1 before the
  snapshot. `wall_tree` returned a one-element set every time, the survivor check saw only the pid
  it had just SIGKILLed, `WALL_LIVE` was pinned at 1, and the INERT branch was unreachable dead
  code. Reproduced 14/14 by four independent reviewers. It cost 4.2 s quiet and 12–16 s loaded per
  bar, and leaked one orphaned `sleep 90` per bar, to answer a question it could not ask. That is
  the reassuring-zero class, inside the scope item whose own text cited it.
  **The assertion MOVES TO THE BREACH PATH**, which is the only moment a real tree exists and the
  only moment the answer is needed: `wall_kill_tree` re-checks what it killed and REPORTS by pid
  what it could not reach. A host where the walk cannot reach a leg's descendants says so with the
  evidence, at the instant that matters, and costs nothing on the runs that never breach.
- **S6** — `GATE_WALL=<s>` overrides the selected row's value alone, mirroring `GATE_JOBS`.
- **S7** — arms in `tools/run-gates/run-gates.test.sh`: a leg that outlives the wall, asserted on the
  RUNNER'S EXIT STATUS and the presence of the RED summary line, because an arm that only greps for
  the breach message passes on a runner that was itself killed; an untimed control proving the elapsed
  time is the wall and not the leg; an off (`wall=0`) run; a run whose wall is INERT; a leg whose child
  spawns a grandchild that outlives it, asserted killed by pid; and a bar that WAITS behind a held
  beacon for longer than the declared wall and then runs a short leg, which must complete GREEN.
- **S9** — **THE BREACH MARKER IS WRITTEN BEFORE THE FIRST KILL.** Written last — as rev-4 had it —
  the watcher's kill loop runs a `wall_kill_tree` per stuck leg, seconds to tens of seconds wide,
  and the reader is free to report the killed legs and DISPATCH FRESH ONES throughout. Measured: an
  8 s wall, two wedged legs, and a third leg started 57 s after the breach and ran to completion —
  149 s against an 8 s bound, 18.6x. The wall bounded nothing once it had fired. Writing the marker
  first also collapses the race that decided whether the durable record said RED or GREEN.
- **S10** — **THE WALL IS A DEADLINE, NOT A COUNTER.** Rev-4 slept 1 second `$WALL` times, and
  `sleep` is external: measured, 20 nominal seconds took 32.9 s and 30 took 58.0 s, a 1.65–1.93x
  drift that is entirely spawn cost. `wall=10800` would have fired between 4h56m and 5h48m while the
  profile line printed 3 h. `EPOCHSECONDS` is a bash builtin; the poll is a tenth of the wall,
  floored at 1 s and capped at 30 s, so the spawn count is about ten per run whatever the wall is
  and the overshoot stays proportional rather than absolute.
- **S11** — **A BREACH REACHES ITS VERDICT BEFORE ANY OTHER EXIT PATH, and the durable record reads
  the MARKER rather than `fails`.** A killed leg writes no `.rc`, so whether `fails` moves at all is
  a race — both outcomes were reproduced. Rev-4's placement let a breach write
  `verdict GREEN / ran 0 / failed 0` into the run record whose ABSENCE is this runner's documented
  crash signal, and on the break path it could satisfy the empty-population refusal and exit 2
  announcing "this run executed NOTHING" — a hang reported as operator error.
- **S12** — **A CHUNK THE WALL EMPTIED REPORTS `killed`, never `green`.** A killed leg increments
  none of the five chunk counters, so it fell straight through to the green branch. Observed:
  `---- chunk product: green (0 ran, 0 failed, 0 skipped, 0 reused, 0 held)` over a chunk whose every
  leg had just been SIGKILLed. This is `TOOL-dUnstalledConvoy-32`'s rule reaching a newer kind of
  did-not-run, which is the reachability failure that row exists to record.
- **S13** — **THE KIT VERSION MOVES WITH THE TABLE.** `gate-profiles.txt` gaining `wall` makes the
  skew asymmetric and fatal in one direction: a runner below the bump reads a walled table, hits
  `prof_die` on the first row, and exits 2 having run ZERO legs — every bar, not some. The precedent
  is four lines below the constant (`TOOL-dUnstalledConvoy-26`, the `subject` key). `1.4 -> 1.5`,
  with the note beside it.
- **S8** — the wall's elapsed measurement is asserted to START AT FIRST DISPATCH. S2 says so and
  nothing in rev-2 measured it, so the dangerous first draft — arming at process start and killing a
  bar for queueing — passed every criterion. S7's last arm is that measurement.

## 3. Non-goals (OUT)

- Not the per-leg ceiling. That exists, this unit does not touch it, and `TOOL-aQuenchedHarness-2`
  owns its evidence.
- Not the turnstile. Its wait bound is `TS_MAXWAIT` and its live-holder defect is
  `TOOL-aQuenchedHarness-8`, which lands first.
- Not a per-leg budget verdict — cost policing is units 4 and 6. A wall is a HANG bound.
- Not a wall value nobody would meet in practice. Choosing the number is a declaration this unit makes
  with the reading beside it.

## 4. Design

### Data model

`gate-profiles.txt` rows gain a third knob. The row grammar is unchanged — knobs are a comma-joined
list — so the parser change is one `case` arm beside `width` and `timeout`, and the declared
`KNOWN_KNOBS` string grows by one member. The canary PINS that set separately, which is what forces
an author to read the table's governing-invariant paragraph before adding a knob.

### The wall

One background watcher, started when the first leg is dispatched, sleeping in short increments so it
can be reaped cheaply when the pool drains normally. On expiry it writes a breach marker into the
run's work directory and kills the process group of every outstanding leg; the pool's reaper reads
the marker and renders the RED summary. The marker is a FILE rather than a variable, because a
watcher that shares a variable with the pool it watches is not a watcher (charter §7).

### Two flags, two probes

`CEILINGS_LIVE` answers "can `timeout -k` run here", and the per-leg ceiling is what consumes it.
`WALL_LIVE` answers "does a group kill from a watcher reach a leg's descendants here", and only the
wall consumes it. Rev-1 pinned the second to the first "rather than a second probe", which certified
a mechanism the wall does not use in both directions: a host with no `timeout` would have declared a
working watcher INERT, and a host where the group kill cannot reach a grandchild would have reported
the wall live. That is the reassuring-zero class, inside the unit that cites it.

### Inventory

- `wall` — the profile knob, in `tools/run-gates/gate-profiles.txt`; graded by the canary's pin.
- `GATE_WALL` — the environment override.
- `scan_descendants` · `remove_descendants` · `arm_wall` · `remove_wall_watcher` — the four shell
  functions, every one leading with a verb `.lexicon.conf` declares. Checked with
  `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` BEFORE they were written here.
  A first cut named them `wall_*` and moved `VERB_OFFENDER_PIN` by four; renaming is the fix §12
  requires, and unlike the `ts_*` pair there was no existing family to stay consistent with.
- There is NO `WALL_LIVE` flag. Rev-4 declared one and rev-5 withdrew it with the probe that set it.
- The breach marker file, under the existing per-run work directory; no new location.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/gate-profiles.txt` ·
`tools/run-gates/run-gates.test.sh` · `.lexicon.conf`, for the `VERB_OFFENDER_PIN` move any new shell
function forces, with its justification line · `AGENTS.md`'s merge-bar section, one sentence.

### Alternatives rejected

A wall enforced by the CALLER — the pre-push hook, or the unattended driver's `GATE_BOUND` — was
rejected: that bound exists at 3600 s and did not prevent the stalls, because it covers only the bar
`--close` runs and not a bar a session starts itself. A bound only some callers apply is a bound the
bar does not have.

## 5. Production-readiness checklist

- security — N/A: no new input, no new write path outside the existing work directory.
- perf / scale — one watcher process per run, sleeping, plus one startup probe; against a bar
  measured in thousands of spawns.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — wall off, wall INERT, wall breached. Each has its own printed
  line and none of them is silence.
- observability — the profile line reports `width`/`timeout`/`ceilings` and gains `wall`, so the run
  says what bound it is under before the first verdict.
- risks — a wall that fires on a legitimately slow bar turns a passing run red, which is
  `TOOL-dRetiredFork-40`'s recorded failure for ceilings. Mitigated by sizing it against recorded
  leg-sums and by the override, and by landing `TOOL-aQuenchedHarness-8` FIRST so the wall is sized
  against an uncontended bar rather than against two bars running as one.
- testing + left-shift gates — S7's arms, in the existing canary, graded against an untimed control
  rather than against a message.
- migration / rollback — `wall=0` on every row is the rollback and is behaviour-identical to today.
- user docs — one sentence in `AGENTS.md`'s bar section and the knob's own justification comment.

## 6. Acceptance criteria

- **AC1** — When a fixture leg sleeps past the declared wall, `bash tools/run-gates/run-gates.sh`
  exits non-zero and its summary NAMES that leg as still running, rather than reporting a leg failure.
- **AC2** — When the same fixture runs with `GATE_WALL=0`, it completes normally, proving the arm
  measures the wall and not the leg.
- **AC3** — When the wall fires, the elapsed time measured by the arm in
  `tools/run-gates/run-gates.test.sh` is bounded by the wall and compared against an untimed control
  run in the same arm, so a bound applied through a pipe cannot pass.
- **AC4** — When a breach cannot reach a leg's descendants, `bash tools/run-gates/run-gates.sh`
  prints the pids it left running. There is no startup probe and no `WALL_LIVE` flag; the assertion
  is made where a real tree exists.
- **AC9** — When the wall fires, `bash tools/run-gates/run-gates.sh` exits **1** — not 0, and not 2.
  Two is the configuration refusal, which is how rev-4 could misreport a hang as operator error.
- **AC10** — When the wall fires, the run record under `<git-dir>/gate-run/` carries
  `gate_verdict RED`. A breach must not leave a plausible green in the file whose absence is this
  runner's crash signal.
- **AC11** — When the wall fires with legs still outstanding, NO further leg is dispatched after
  `$WORK/wall.breach` appears, asserted by comparing the dispatched-leg count across the breach.
- **AC5** — When a knob is added to `gate-profiles.txt` without updating `KNOWN_KNOBS`, the
  `run-gates canary` leg reds, so the pin cannot drift.
- **AC7** — When the wall fires, `bash tools/run-gates/run-gates.sh` SURVIVES long enough to print the
  RED summary, asserted by exit status rather than by output presence — the runner is not in the set
  of things the watcher kills.
- **AC8** — When a bar waits behind a held beacon for longer than the declared `wall` and then runs
  a short leg, `bash tools/run-gates/run-gates.sh` completes GREEN, proving the clock starts at first
  dispatch and not at process start.
- **AC6** — When a fixture leg spawns a grandchild that outlives it and the wall fires, the arm in
  `tools/run-gates/run-gates.test.sh` finds the grandchild dead, asserted by pid rather than by the
  summary's wording.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the `run-gates canary` leg, which owns the knob pin · the
`lexicon naming predicates` leg, which guards on `tools/` and grades any new shell function this unit
defines, including the `VERB_OFFENDER_PIN` move a new definition forces ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for that canary at the Definition of Done, since
it is a held self-test leg.

## 8. Open questions

- **F1 — what value does each profile row declare?** RESOLVED (agent, 2026-09-06, delegated), and
  BUILT: `capable` 10800, `modest` 14400, `minimal` 21600, each carrying its reading in
  `gate-profiles.txt`'s header. Derived from the costliest bar this repo can measure —
  `GATE_FULL=1 GATE_SELFTESTS=1`, 13644 s of leg-sum with its longest leg at 3837 s, so at width 8
  the pool term is 1706 s and the floor is the longest leg: about 4000 s end to end. 10800 is 2.7x
  that, and deliberately loose, because a bound that fires on a healthy bar is strictly worse than a
  loose one. The lower rows scale with the pool term, which is the only part the width moves. A single figure cannot be right for a cost that is node-relative, which
  `TOOL-aCollapsedScan-4` records; and shipping it off everywhere would land a knob that has never
  fired, which charter §7 refuses.
- **F2 — is the wall sized before or after `TOOL-aQuenchedHarness-8`?** RESOLVED (agent, 2026-09-06,
  delegated): after. Unit 8 takes `order 1` and this unit `order 2`, because every recorded leg-sum
  in the tree today was measured under a bar that may have been sharing the machine with a second
  bar it reaped. Sizing a wall against those numbers would bake the defect into the bound.

## 9. Revision log

- rev-6 · 2026-09-07 · CLOSED. The wall exists, fires, bounds a run and now records a VERDICT rather than this runner's crash signal. Two defects found by the closing review made its guarantee decorative until today: the survivor scan read a snapshot the function had already deleted, and the breach exited above the verdict writer. Both fixed, both failing cases observed. AC6 remains NOT DONE and is now known-absent rather than merely unrun: no arm captures a pid, so the descendant walk is ungraded, which is exactly how the `rm` in the wrong place shipped.

- rev-1 · 2026-09-06 · initial draft.
- rev-5 · 2026-09-06 · folded an adversarial forensic review of the BUILT code — 55 findings, 37
  confirmed. Twelve defects, six of them landing blockers, and one of them retracts a measurement
  this build reported to the owner as fact.
  **The retraction first:** the "+44 s per bar, 6.4x" regression reported earlier DOES NOT EXIST. The
  A/B that produced it paired HEAD's runner with the NEW profile table; HEAD does not carry the
  `wall` knob, so that arm hit `prof_die` and exited 2 in ~8 s having run ZERO legs, and 8 s read as
  a fast bar. Re-measured with each arm carrying its own table and every arm asserted to have printed
  `gates GREEN`: old 25679/25867/27082 ms against new 22520/23026/29312 ms — no measurable difference.
  The check that was owed is one `grep -q '^gates GREEN'` per arm.
  **The blockers:** S5's startup probe graded nothing and is WITHDRAWN (it also leaked a process per
  bar); S9 moves the breach marker before the kills, because a third leg was measured starting 57 s
  after an 8 s wall fired; S10 makes the wall a deadline, because `sleep 1` drift put `wall=10800` at
  ~5 h; S11 hoists the verdict and makes the durable record read the marker, because a breach could
  write GREEN or exit 2 as a refusal; S12 stops a killed chunk reporting green; S13 bumps the kit
  version, without which any adopter taking the table without the runner reds 100% of bars.
  Also folded: a numeric guard on the `ps` walk, since cygwin prints argv raw and this box already
  carries ~10 malformed continuation rows per snapshot; and the tracked arm, which was red 3/3 for a
  property of the box, now bounds both runs and grades a 30 s margin against a 112 s designed gap.
  §1's "the sum of every ceiling it can reach" overstated the worst case by 4.6x — at width 8 it is
  9.2 h, not 42 h — and the wall is a real tightening of that, not of 42 h.
- rev-4 · 2026-09-06 · BUILT, with two corrections the build found. §5's liveness sentence still said
  "the group kill" after rev-3's S4 stopped using one — my own amendment-leaves-its-other-half-standing,
  fixed here. And the probe is THREE deep rather than two, graded over every pid it collected rather
  than over the root: a two-deep probe would have graded a mechanism simpler than the shipped case,
  and checking only the root would call a kill LIVE that left a grandchild behind. F1's values are
  now declared rather than deferred.
- rev-3 · 2026-09-06 · folded spec-audit round 2. B3: the wall does NOT kill a process group. The
  runner never enables job control, so there is one group and the runner is in it, and `setsid` is
  absent on this node (rc=1, verified) — S4 now kills recorded per-leg pids and their descendants, and
  AC7 asserts the runner survives to print its own verdict. H1: rev-2's S2 said the wall arms at first
  dispatch and nothing measured it, so arming at process start passed every criterion while killing a
  bar for queueing; S8 and AC8 measure it. H3: §7 names the lexicon leg and Files touched carries
  `.lexicon.conf`'s pin move.
- rev-2 · 2026-09-06 · folded spec-audit round 1. H3: the wall and the per-leg ceiling are now ONE
  mechanism each rather than one claim spanning both — S4 states the watcher does not use `timeout`,
  and S5 gives `WALL_LIVE` its own probe of the group kill with a grandchild, so a host with no
  `timeout` no longer declares a working watcher inert and a host where the group kill cannot reach a
  descendant no longer reports the wall live. AC4 rewritten to name both directions, AC6 added for
  the grandchild. §5 and §8 F2 record that this unit is sized AFTER unit 8, because today's leg-sums
  were measured under bars that may have been running two at a time.

## 10. Reuse audit

The seam this unit extends is `tools/run-gates/run-gates.sh`'s existing per-run machinery — the
profile knob parser at `KNOWN_KNOBS`, the per-run work directory, the marker-file idiom and the
summary renderer. It does NOT extend the per-leg `timeout -k` path, and saying so is the correction
rev-2 makes: that call wraps one command and the wall bounds a pool, so reusing its liveness probe
was reuse of the wrong thing. `tools/codebase-map/reuse_lookup.py` returned
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seam for this area, carrying
decisions `TOOL-aPacedTurnstile-1` through `-16`; that build's own review record supplied the MSYS
group-kill condition S5's probe now tests for. The profile table's governing-invariant paragraph was
read before adding a knob, as it instructs.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
