# TOOL-aGraftedHelix-7 — the gate runner stops dispatching legs above a declared memory fraction and records the pause

**Status:** CLOSED · rev-4 · 2026-10-05 · node a · Tier-2 · base 5266d22e · streams tooling · order 8 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/run-gates/run-gates.sh` picks its pool width from total RAM once, at start (`det_ram`), and
nothing watches memory while the legs run; "never run the bar, the pooled suites and agents at
once" is a memory note, not a mechanism. This unit makes both dispatchers in the run-gates kit hold
their next dispatch while used memory is above a declared fraction and something is still running,
bounded so a hold always ends, records each pause and prints one summary line, and keeps a reading
taken during a pause out of ceiling evidence.

## 2. Scope (IN)

- **S1** — A profile knob `mempause=<pct>` in `tools/run-gates/gate-profiles.txt`: 0 is off and is
  what a row that omits it gets, 1 to 100 is the used-memory threshold, and every shipped row
  declares `mempause=90`. `KNOWN_KNOBS` gains it, and a table value above 100 is refused like any
  malformed knob. `GATE_MEMPAUSE=<pct>` overrides the row's value alone; any other non-empty
  override value prints one `run-gates: NOTE` line and leaves the pause off, and an empty one reads
  as unset, as an empty `GATE_WALL` does. The profile line gains
  `mempause <n>%`, `mempause off` or `mempause INERT`; `--print-profile` gains the key `mempause`,
  the effective threshold with 0 for off, INERT being a fact about the host that the line carries;
  the run header gains `mempause` outside the four-key envelope block. Observed by AC1 and AC2.
- **S2** — One shell block between `# >>> mempause_sh` and `# <<< mempause_sh`, canonical in the
  runner and carried byte-identical in `tools/run-gates/run-selftests.sh`, graded by a new
  `PARITY_ROWS` row in `tools/lib/resolve-python.test.sh`. It holds `read_mem_used`,
  `check_dispatch_pause`, `write_pause_row`, `render_pause_summary` and the hold bound
  `MEMPAUSE_HOLD`, 300 s, which `GATE_MEMPAUSE_HOLD` overrides. Observed by AC3.
- **S3** — `read_mem_used` prints used memory as a whole percent, read with builtins only:
  `MemTotal` against `MemAvailable`, or `MemFree` where the file carries no `MemAvailable`, from
  `GATE_MEMINFO` or `/proc/meminfo`; and, when a limit and a usage both read under
  `GATE_CGROUP_ROOT`, the cgroup's usage over its limit. The HIGHER of the two wins. With no reading
  it prints nothing and fails. It also leaves the figure in `MEMPAUSE_READ`, so the decision calls
  it with its output discarded rather than through a command substitution, which would fork. A
  knob that is on over a host giving no reading prints one
  `run-gates: NOTE` line at start and reads INERT. Observed by AC4 and AC7.
- **S4** — Before every dispatch, the runner calls `check_dispatch_pause` with the count of legs
  running, at BOTH of its dispatch sites: the inner pass, and the forced-progress branch, which
  passes a count of 0. It HOLDS when the reading is above the threshold and at least one leg runs,
  and a hold ends, so the waiting leg dispatches, when the reading falls to or under the threshold
  (`fell`), when a decision finds the episode has held `MEMPAUSE_HOLD` seconds or more (`bound`),
  when no leg is left running (`drained`), when the reading becomes unavailable (`unread`) or when
  the wall fires (`wall`). A decision happens when a leg completes; nothing polls. So the bound is
  tested at the first leg completion after it expires, and a hold lasts at most until then.
  Observed by AC5, AC6, AC12 and AC14.
- **S5** — Each closed episode is one row in the run record's `pauses` file; the verdict file
  gains `paused` and `paused_s` in all three of its writers; and one `memory:` summary line prints
  after the pool drains, on every run. The two whole-output comparisons in the run-gates suites
  filter that line and check it was printed once. Observed by AC5, AC6, AC8 and AC13.
- **S6** — The self-test runner's pooled sweep makes the same check before each suite it
  dispatches, with its own count of suites running, reads the threshold from the one
  `--print-profile` call it already makes, decides INERT with one `read_mem_used` of its own
  before its loop, and prints the same summary line. With no runner beside it the call answers
  nothing and the pause reads off. It keeps no run record, so it writes no `pauses` row.
  Observed by AC9.
- **S7** — `read_runs` in `tools/run-gates/derive-ceilings.py` gains the set-aside reason `paused`,
  between `contended` and `uncensused` in first-match order: an admitted reading whose leg ran
  while one of its own run's `pauses` episodes was open, by strict overlap. The `# set aside:` line
  and the `aside` column count it. Observed by AC10.
- **S8** — The table's KNOBS block, the canary's `PINNED_KNOBS`, the README, the run-gates dossier
  and the kickoff manifest's command catalog name the knob; the kit version moves once, after the
  last move; the manifest's audit stamp is renewed. Observed by AC2 and AC11.
- **S9** — The canary, the evidence suite and the self-test runner's suite carry this unit's arms,
  and each suite's `FLOOR_ASSERTIONS` rises by the arms it gains. NOT OBSERVED: a suite is the
  close's to run, and each arm's red on a staged break is observed there (§7).

## 3. Non-goals (OUT)

- No health-log line. `TOOL-aGraftedHelix-8` writes its one per-bar event beside this unit's
  summary line.
- No change to how the width is chosen: the rows' core and RAM thresholds, `det_ram` and the cgroup
  cap stay as they are. The pause narrows a pool in effect; it never re-sizes it.
- No reading on a host without `/proc/meminfo` or a cgroup pair, macOS among them. The knob is
  announced INERT there rather than read through a spawn.
- No pause in the serial retry, which runs one leg alone after the pool drains, nor in the
  self-test runner's `--serial` mode, which runs one suite at a time; neither has a second job to
  hold.
- No verdict. The knob never turns a leg into a pass, a skip or a red: the table's governing
  invariant, which it may satisfy only by making the bar slower.
- No drift-audit signal. The card line `TOOL-aGraftedHelix-8` adds is the cross-run surface.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-5` — the set-aside path in `derive-ceilings.py`, its
  `aside` column and its `# set aside:` line; S7 adds the `paused` reason to it, read from this
  unit's `pauses` rows. Without it there is no reason list to extend.
- **hands-off** `TOOL-aGraftedHelix-8` — the per-run pause count and held seconds, beside the
  summary line, where that unit writes its single `dispatch-paused` health event.

## 4. Design

### Data model

```
knob        mempause=<0..100>                  gate-profiles.txt, per row; absent = 0 = off
overrides   GATE_MEMPAUSE=<0..100>  GATE_MEMPAUSE_HOLD=<s>  GATE_MEMINFO=<path>
pauses      <started-s> TAB <ended-s> TAB <held-s> TAB <peak-pct> TAB <threshold> TAB <ended-by>
ended-by    fell | bound | drained | unread | wall
verdict     paused TAB <episodes>     paused_s TAB <held seconds, summed>
header      mempause TAB <pct|off|inert>
profile     ... wall <w>, mempause <pct>%|off|INERT; <tag>
```

Epochs are `EPOCHSECONDS`, a builtin, so stamping an episode spawns nothing. `pauses` lives in the
run record beside the `.leg` rows and `census`.

The summary line, one of:

```
memory: pause off
memory: no reading on this host, so the <n>% pause was INERT
memory: no pause  (peak <p>% used, threshold <n>%)
memory: <k> pause(s), <s>s held  (peak <p>% used, threshold <n>%; fell <a>, bound <b>, drained <c>, unread <d>, wall <e>)
```

The peak is the highest reading any dispatch decision took this run, so the close's own bar prints
the figure that tells whether 90 suits node `a`; a run whose decisions took no reading prints it
as `?`, the profile line's spelling of an unknown figure.

### The reading

On MSYS `MemFree` is Windows' own available figure, and the file carries no `MemAvailable`.
Measured on node `a` 2026-10-04: `/proc/meminfo` read `MemFree` 16408792 kB against `\Memory\
Available KBytes` 16390936 and `FreePhysicalMemory` 16427416 a moment apart, and `MemTotal`
33477600 kB on both sides. On Linux `MemAvailable` is the right field and `MemFree` understates
it, so the fallback can only over-read pressure, which costs speed and never coverage.

The cgroup half reads `memory.current` over `memory.max`, or the v1 pair `memory.usage_in_bytes`
over `memory.limit_in_bytes`, rejecting `max` and the v1 sentinel exactly as `cgroup_ram_mb`
rejects them. The higher fraction wins, for the reason `det_ram_capped` takes the lower RAM: a
wrong source can only make the bar slower.

Cost, PINNED on node `a` 2026-10-04: one builtin read of `/proc/meminfo` took 0.69 ms, 100 in
0.069 s, against 25 ms for the same read through an `awk` spawn. The count of running legs is the
one the dispatch loop's own condition already takes, captured rather than asked again, so a
decision adds no spawn.

### The decision

`check_dispatch_pause <running>` returns 0 to HOLD and 1 to dispatch, first match:

1. The pause is off or INERT: dispatch.
2. No reading: close an open episode as `unread`; dispatch.
3. The reading is at or under the threshold: close an open episode as `fell`; dispatch.
4. Nothing runs: close an open episode as `drained`; dispatch. A hold can never outlive the last
   running job, so a pause cannot deadlock a pool.
5. An open episode has held `MEMPAUSE_HOLD` seconds or more: close it as `bound`; dispatch. This
   is tested only when a decision runs, so an episode is released at the first leg completion
   after `MEMPAUSE_HOLD` seconds, never at the instant the bound expires.
6. Otherwise open an episode if none is open, and hold.

`write_pause_row <ended-by>` closes the open episode: it adds one `pauses` row when the caller set
a record path, and updates the counters `render_pause_summary` prints. After the dispatch loop
ends, an episode still open, which only the wall's break can leave, closes as `wall`.

In the bar's inner dispatch loop the call sits after the sentinel skip and before `arm_wall`. A
hold steps the dispatch index back and leaves the inner loop, and the reader then blocks on
`wait -n` exactly as it does with a full pool; at least one leg runs by rule 4, so that wait
returns. The next completion re-runs the decision for the same leg. Under a pressure that never
falls, each episode releases one leg at the first completion after `MEMPAUSE_HOLD` seconds, so a
hold lasts until the first running leg to finish after the bound does, and the pool drains toward
width 1; the bar slows and keeps moving.

The runner has a SECOND dispatch site. When nothing is live, legs remain and the inner pass
dispatched nothing, the forced-progress branch (`run-gates.sh`'s `if [ "$di" -eq "$di_before" ]`) runs one
leg so the loop can never spin. A hold steps the index back, so a held leg can reach that branch
when the running legs finish between the inner pass's count and the outer liveness test, a window
the runner's own comment measures as common. The branch therefore calls `check_dispatch_pause 0`
before its `runleg`: rule 4 closes the open episode `drained` and the leg dispatches. Without that
call the episode would survive the loop and close as `wall` with no wall fired.

The sweep in `tools/run-gates/run-selftests.sh` dispatches through a simpler loop: it starts a
suite, counts it in `live`, and waits on `wait -n` once `live` reaches the outer width. The call
goes immediately before a suite starts, as a loop that waits for one suite to finish and counts it
out for as long as the call says hold, then re-tests the wall's breach marker the loop already
reads. Its `--serial` mode has its own loop, one suite at a time, and gains nothing.

### Recording

The bar sets the record path to the run record's `pauses` file and prints the summary line after
the pool drains, before the serial retry, so a run the wall stopped prints it too. The verdict
file's three writers each gain `paused` and `paused_s`. The block keeps its counters in two shell
variables, `MEMPAUSE_N` for episodes and `MEMPAUSE_HELD_S` for held seconds, and
`TOOL-aGraftedHelix-8` reads those two beside the summary line for its one health event.

### The evidence join

`read_pauses` in `tools/run-gates/derive-ceilings.py` reads one run directory's `pauses` rows,
skipping any row that is not six fields with numeric stamps. A reading is `paused` when its own
start and end, the `.leg` stamps divided down from nanoseconds, strictly overlap a row's
`[started, ended]`. A reading that only touches an episode's edge is not paused, because the
episode's own end is the instant its waiting leg dispatched. A legacy row stamped `0 0` overlaps
nothing. Text IO names `utf-8`, as the module's other reads do.

This stays inside one unit by M2's test: it adds no document, gate, adopter or generated artifact,
only a reason to the filter `TOOL-aGraftedHelix-5` builds, defined by the record this unit writes.

### Inventory

| Identifier | Cell |
|---|---|
| `read_mem_used`, `check_dispatch_pause`, `write_pause_row`, `render_pause_summary` | `sh.function` |
| `read_pauses` | `py.function` |
| `mempause`, `MEMPAUSE_HOLD`, `GATE_MEMPAUSE`, `GATE_MEMPAUSE_HOLD`, `GATE_MEMINFO` | knob, constant, overrides; no cell |
| `MEMPAUSE_N`, `MEMPAUSE_HELD_S` | the block's two counters; no cell |
| `MEMPAUSE`, `MEMPAUSE_INERT`, `MEMPAUSE_ROWS`, `MEMPAUSE_READ` | what each caller sets for the block (threshold, host state, record path) and the last reading; no cell |
| marker stem `mempause_sh` | parity-table key, no cell |
| `pauses`, `paused`, `paused_s`, the reason `paused` | record file, verdict keys, set-aside reason; no cell |

Each function name was answered `OK` by `python tools/lexicon/lexicon.py --suggest <name> --as
<cell>`. No gate leg, kit, hook, guide, workflow script or lexicon verb is added, so the codebase
map owes no claim. `read_pauses` enters the symbol index, so the map's generated artifacts are
re-rendered with `python tools/codebase-map/gen_map.py --write` in the same commit.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-selftests.sh`
- `tools/run-gates/gate-profiles.txt`
- `tools/run-gates/derive-ceilings.py`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `tools/run-gates/run-selftests.test.sh`
- `tools/lib/resolve-python.test.sh`
- `memory/map/features/run-gates.md`
- `memory/map/generated/symbols.json`
- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Polling while held**, a `sleep` job raced against `wait -n`. The sleep is a job `jobs -rp`
  counts, so it takes a pool slot, and the runner's own record of an earlier polling loop is 317 s
  of a 617 s run spent spawning sleeps.
- **Re-sizing the width mid-run.** A second scheduler beside the declared row, and a width
  decision the profile line could no longer report.
- **Reading through `free`, `vm_stat` or PowerShell.** A spawn per decision at 25 ms or more, and
  seconds for PowerShell, against 0.69 ms for a builtin read.
- **A kit-local sourced library**, the `lib-attribute.sh` shape. Every suite fixture that copies
  the runner and the shipped table without such a file would read the pause INERT and print a NOTE
  no arm expects; an inline block travels inside the file that runs it.
- **A per-run hold budget** — F1.

## 5. Production-readiness checklist

- security — Reads one kernel file and two cgroup files and writes integers into a mode-700 run
  record. No path in it comes from a leg.
- perf / scale — One builtin read per dispatch decision, 0.69 ms on node `a`, and no added spawn.
  Under real pressure a hold slows the bar by design. It is released at the first leg completion
  after `MEMPAUSE_HOLD` seconds, so one hold lasts at most until then, which is bounded by the
  running legs' own ceilings and by the wall.
- error / empty / loading states — No reading is INERT and announced at start, `unread` mid-run,
  and never a 0 % reading. A malformed table value refuses; a malformed override is announced and
  leaves the pause off.
- observability — The profile line, the header key, the `pauses` rows, the verdict's two keys and
  the summary line with its peak.
- risks — A pause narrows the self-test sweep's pool against a wall derived from its declared
  width, so a long hold can leave a suite UNRUN; that reads red and says why, never green. A wedged
  reading on a host that always reads above the threshold slows every bar, and the summary line's
  `bound` count is what shows it. The decision runs only at dispatch, so the bar's last legs run
  unwatched once nothing waits.
- testing — AC1 to AC11 by direct observation in the pass; the suite arms in §7 at the close.
- migration — None. A table without the knob runs with the pause off, and a runner without it
  refuses a table that has it, the documented one-way skew of `KNOWN_KNOBS`, so table and runner
  move in one commit.
- user docs — The table's KNOBS block, the README section and one line in the manifest's command
  catalog.

## 6. Acceptance criteria

`$S` below is a scratch repository under `%TEMP%` with a short name, holding a copy of the runner,
`gate-fingerprint.sh`, a fixture profile table and a manifest of one-script fixture legs, with
`GATE_CGROUP_ROOT` pointed at an empty directory so the host's cgroup files cannot vote.

- **AC1** — When the runner runs `--print-profile` in `$S` over one row reading
  `width=2,timeout=0,wall=0,mempause=80`, it prints the key `mempause` with 80 and a profile line
  carrying `mempause 80%`; with `GATE_MEMPAUSE=0` the line carries `mempause off`; a row carrying
  `mempause=101` exits 2 naming the knob; and `GATE_MEMPAUSE=x` prints one `run-gates: NOTE` line
  and a line carrying `mempause off`.
  Red when: a table value above 100 is accepted, or the override does not reach the line.
- **AC2** — When `grep -c 'mempause=90' tools/run-gates/gate-profiles.txt` runs it prints the
  number of rows the table declares, and `grep -n '^PINNED_KNOBS=' tools/run-gates/run-gates.test.sh`
  names `mempause`.
  Red when: a shipped row omits the knob, or the canary's pinned set lacks it.
  figure: DERIVED; the row count is read from the table when observed.
- **AC3** — When `git grep -l '^# >>> mempause_sh'` runs it lists the runner and the self-test
  runner, `awk '/^# >>> mempause_sh/,/^# <<< mempause_sh/' <file> | tr -d '\r' | cksum` over each
  prints one checksum, and `grep -n 'mempause_sh' tools/lib/resolve-python.test.sh` names a
  `PARITY_ROWS` row.
  Red when: one copy differs by a byte, or no row grades the stem.
- **AC4** — When the block, extracted from the runner by the AC3 `awk`, is sourced with
  `GATE_MEMINFO` at a fixture of `MemTotal` 1000 kB, `read_mem_used` prints 85 for `MemAvailable`
  150 kB; 85 for `MemFree` 150 kB with no `MemAvailable`; 85 for `MemAvailable` 150 kB beside
  `MemFree` 900 kB; nothing, failing, with no `MemTotal`; 95 beside a `GATE_CGROUP_ROOT` holding
  `memory.max` 1000 and `memory.current` 950; and 85 when that `memory.max` reads `max`.
  Red when: an unreadable file prints a number, or the lower of host and cgroup wins.
  cost: one builtin read, PINNED at 0.69 ms on node `a` 2026-10-04; the pass re-times 1000 calls
  and records its figure in the acceptance ledger.
- **AC5** — When `$S` runs at width 3 with `GATE_MEMPAUSE=90` and `GATE_MEMINFO` at a fixture
  reading 95 % used, over leg A that sleeps 3 s and then rewrites the fixture to 10 % used and
  instant legs B and C, the run's `pauses` file holds one row ending `fell` with a held time of 2 s
  or more, B's and C's `.leg` start stamps are no earlier than A's end stamp, the verdict file reads
  `paused` 1, and stdout carries exactly one line opening `memory: 1 pause(s)`.
  Red when: B or C dispatches while the reading is above 90 and A runs.
- **AC6** — When `$S` runs at width 3 with `GATE_MEMPAUSE_HOLD=2` and the fixture at 10 % used,
  over leg A sleeping 8 s, leg B sleeping 1 s that rewrites the fixture to 95 % as it ends, leg C
  sleeping 4 s and instant legs D and E, the `pauses` file holds a row ending `bound` and a row
  ending `drained`, every leg reports, and the exit code equals the same fixture's run with
  `GATE_MEMPAUSE=0`. Traced: B ends at 1 s and D is held; C ends at 4 s, past D's 2 s bound, and
  D is released `bound`; E is held from then until A ends at 8 s and closes `drained`.
  Red when: a held dispatch survives a leg completion that occurs after its bound while legs still
  run, or the run fails to finish inside an outer bound of 60 s.
- **AC7** — When `$S` runs with `GATE_MEMPAUSE=90` and `GATE_MEMINFO` naming a file that does not
  exist, stderr carries one `run-gates: NOTE` line naming the pause INERT, the profile line carries
  `mempause INERT`, no `pauses` row is written, and the summary line opens `memory: no reading`.
  Red when: an absent reading is taken as 0 % used and the line reads `no pause`.
- **AC8** — When `git grep -n "memory: " -- tools/run-gates/run-gates.test.sh tools/run-gates/run-gates.runlog.test.sh`
  runs, it names a filter in the canary's two-width comparison and in the run-log suite's
  comparison, each beside a check that exactly one such line was printed.
  Red when: either comparison reads the line, whose peak varies with the host, or a filter hides
  the line's absence.
- **AC9** — When the self-test runner's sweep runs `--pooled --calibrate` in `$S` over a two-suite
  declaration at outer width 2, with `GATE_MEMPAUSE=90` and `GATE_MEMINFO` at 95 %, the second
  suite starts no earlier than the first ends and the sweep prints one line opening
  `memory: 1 pause(s)`; at 10 % both start together and the line opens `memory: no pause`.
  Red when: the pooled sweep starts its second suite under pressure while the first runs.
  cost: the fixture declaration and two trivial suites; seconds.
- **AC10** — When `python tools/run-gates/derive-ceilings.py --report` runs in a fixture git dir
  whose one run holds a `pauses` row spanning epoch 1000 to 1010 and three `ok` readings of leg L
  with `foreign` 0 — 10 s from 995 to 1005, 20 s from 1020 to 1040, 30 s from 970 to 1000 — L's row
  reads a max of `30.0` from 2 readings with an `aside` of 1, and the `# set aside:` line names
  `1 paused`.
  Red when: the overlapping reading is admitted, or the reading that only touches the episode's
  start is set aside.
  figure: every count is PINNED by the fixture.
- **AC11** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0,
  `python tools/govkit/govkit.py epoch --base <the pass's base>` names no run-gates entry,
  `bash skills/session-kickoff/manifest-check.sh` prints no `MANIFEST check 5 FAILED` line, and
  `grep -n 'mempause' memory/guides/SESSION-KICKOFF.md` names the command catalog's line.
  Red when: the runner moved and its version, the audit stamp or the catalog line did not.
- **AC12** — When `$S` runs AC5's fixture with leg A deleting the `GATE_MEMINFO` file instead of
  rewriting it, the `pauses` file holds one row ending `unread`, and B and C dispatch at A's end.
  Red when: an unreadable meminfo mid-hold holds until the bound instead of releasing.
- **AC13** — When `$S` runs at width 2 with `GATE_MEMPAUSE=90`, `GATE_MEMINFO` at 95 % and a
  `GATE_WALL` of 3 s, over leg A sleeping 10 s and an instant leg B that the pressure holds, the
  `pauses` file holds a row ending `wall`, the verdict file carries `paused` and `paused_s`, and
  stdout carries exactly one line opening `memory:`.
  Red when: a wall-stopped run omits its open episode, its verdict keys or its summary line.
- **AC14** — When the block, extracted by the AC3 `awk`, is sourced with an episode open and the
  reading above the threshold, `check_dispatch_pause 0` returns 1 and adds one `pauses` row ending
  `drained`. When `$S` runs at width 2 over legs C (instant), A (3 s) and Y (0.5 s), in that
  manifest order, after a seed bar with the pause off has written the ledger that dispatches them
  A, Y, C, with `GATE_MEMPAUSE=90` and `GATE_MEMINFO` naming a FIFO whose writer answers the first
  three reads 10 % and the fourth 95 % only once A's `.leg` row exists and a second more has
  passed, the `pauses` file holds exactly one row, ending `drained`, and the bar exits 0. Traced:
  Y's completion starts a pass whose first candidate is C; its decision blocks until A's worker is
  gone and then holds C with nothing running, so the next dispatch is the forced branch's.
  Red when: the forced-progress branch dispatches a held leg with no decision, so its episode
  closes `wall` with no wall fired.
  cost: two fixture bars of about 4 s each; a host with no `mkfifo` announces the half skipped.

## 7. Gates

`run-gates canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates gov canary` · `run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `run-selftests self-test` · `every held leg is budgeted, every budget row resolves` · `foreign-prefix parity (every self-test at three prefixes)` · `leg ceilings clear their evidenced maximum` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `install-prefix (shipped surface)` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

The close runs these once; no pass runs a suite. `run-gates evidence`, `run-gates turnstile`,
`run-gates run-log line`, `run-gates adopter e2e`, `profile-bar selftest` and `run-selftests
self-test` are held kit self-tests, so the close owes each a run of its own, bounded, rather than
inside the bar.

New arm: tools/run-gates/run-gates.test.sh · AC1 and AC2 beside arm 4e's pinned set, and AC5 to AC7 as fixture bars; stage rule 4 deleted, the bound compare reversed, and the INERT branch reading 0 · FLOOR_ASSERTIONS rises by the arms added
New arm: tools/run-gates/run-gates.test.sh and tools/run-gates/run-gates.runlog.test.sh · AC8's presence checks; stage the summary line deleted · FLOOR_ASSERTIONS rises in each
New arm: tools/lib/resolve-python.test.sh · the mempause_sh parity row; stage one byte edited in the self-test runner's copy · none
New arm: tools/run-gates/run-selftests.test.sh · AC9's pooled fixture; stage the call deleted from the sweep's loop · FLOOR_ASSERTIONS rises by the arms added
New arm: tools/run-gates/run-gates.evidence.test.sh · AC10 over fixture rows; stage the overlap test made non-strict · FLOOR_ASSERTIONS rises by the arms added
New arm: tools/run-gates/run-gates.test.sh · AC12's deleted meminfo, AC13's wall during a hold and AC14's forced-progress decision; stage rule 2 deleted, the wall close deleted, and the forced branch's call deleted · FLOOR_ASSERTIONS rises by the arms added

## 8. Open questions

- **F1 — Is a hold bounded per episode, or by a budget for the whole run?** (a) Per episode: each
  episode is released at the first leg completion after `MEMPAUSE_HOLD` seconds and lasts at most
  until then, and a further held decision opens a new episode, so under lasting pressure the pool
  runs narrow and keeps moving; at least one leg always runs while a hold is open. (b) Per run: once
  the run's summed hold reaches a budget, the pause disarms for the rest of the run. Both meet the
  brief's criteria, and neither trips a veto. (b) re-opens full-width dispatch exactly while the
  pressure lasts, which is the thrash this unit exists to stop, so it leaves the unit's own goal
  open; (a) costs only speed, which the table's governing invariant permits, and its worst case, a
  fully serialized bar, is bounded by the wall: the costliest bar the table's own comment records
  is 13644 s of leg-sum, against the 21600 s wall every shipped row declares.
  RESOLVED (agent, 2026-10-04, delegated): (a), per episode.
- **F2 — Does the self-test runner's pooled sweep pause too, or only the bar?** (a) Both, through
  one parity-graded block; (b) the bar alone, as the spec brief's heading reads. The owner's prompt
  record names the shape as "the runners stop dispatching new legs", plural, and
  `tools/unattended/run-unattended-gates.sh` sends its pooled half through the self-test runner, so
  (a) also covers the pooled unattended suites the memory note warns about. Vetoes: the block adds
  no public surface, since it is inline and its parity row is a test-table row, and touches no
  governance carrier. RESOLVED (agent, 2026-10-04, delegated): (a), both runners.
- **F3 — Does a reading taken during a pause argue a ceiling?** (a) No: `derive-ceilings.py` sets
  it aside as `paused`; (b) yes, the pause being a dispatch control only. The build's expected
  improvement is that a contended timing cannot raise a ceiling, and a leg that ran while used
  memory sat above the threshold ran contended. Vetoes: none; it extends a filter this build
  already adds. RESOLVED (agent, 2026-10-04, delegated): (a), set aside as `paused`.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 7 section, the prompt record's
  sixth item, `run-gates.sh`, `run-selftests.sh` and `gate-profiles.txt` at base `5266d22e`, and
  the readings recorded in §4.
- rev-2 · 2026-10-04 · §4 §5 §6 §7 §8 · S4 S5 · AC6 AC12 AC13 AC14 · folded the round-1 spec
  audit's findings on this unit: 33 and 41, one defect (the hold bound is tested at the next leg
  completion, restated in S4, rule 5, the dispatch paragraph, §5 perf and §8 F1, and AC6's Red-when
  rewritten to that semantics with its trace); 40 (the forced-progress branch named as a second
  dispatch site and routed through `check_dispatch_pause 0`, S4, AC14); and 23 (AC12's `unread`
  and AC13's `wall` end reasons and the wall-stopped summary).
- rev-3 · 2026-10-05 · S1 S3 S6 §4 · read against the runner as unit 5 left it (run-gates 1.25,
  `arm_census` beside `arm_wall`, the census merged at `909c5e0b9`): the forced-progress branch is
  named by its condition, since its line numbers moved; `--print-profile`'s `mempause` is the
  numeric threshold and an empty override reads as unset; `read_mem_used` also sets
  `MEMPAUSE_READ` so a decision forks nothing; the sweep decides INERT with one read of its own and
  reads off with no runner beside it; an unread peak prints `?`; the inventory names the four
  variables a caller sets for the block.
- rev-4 · 2026-10-05 · AC6 AC14 · observed while building the arms. AC14's twenty runs could not
  red: an instant A dispatched first puts the hold on the pass's SECOND candidate, so the
  forced-progress branch, which needs the hold on a pass's FIRST, was never reached, and twenty
  runs with the branch's call deleted stayed green. Its second half is now a fixture that reaches
  the branch by construction, a FIFO holding the decision until the last runner is gone, observed
  red with the call deleted. AC6's B wrote its pressure at its START, which races C's own dispatch
  decision; held there, every later episode read `drained` (two runs in five). It writes as it
  ends, the trace unchanged.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "pause dispatching work while available memory is low"`
ranked only name-stem neighbours (`resolve_memory_root`, `readMemoryRoot`) and printed `unscanned
layers: .sh`, so the shell seams were read from source, per
`memory/gotchas/reuse-lookup-cannot-see-shell-seams.md`. Extended: the profile table and its row
validator with `KNOWN_KNOBS`; `cgroup_ram_mb` and `det_ram_capped`, whose sources and fail-safe
direction the reading reuses; the bar's dispatch loop and its `live()` count; the `--print-profile`
seam the self-test runner already reads its width through (`TOOL-aQuenchedHarness-4`); the
verdict file's three writers; the inline-copy parity table `PARITY_ROWS`, whose `kickoff_region`
row already names a kit file rather than a `tools/lib/` file as its canonical; and the set-aside
path `TOOL-aGraftedHelix-5` adds to `read_runs`. Where probe and source disagreed: nothing the map
ranked reads memory or dispatches work. The recall probe returned the profile table's own build
(`TOOL-aPacedTurnstile-2`, the thrash it was written for) and its cgroup review finding, which is
why the cgroup half is in S3. Rejected candidates and why are §4 and §8.

Recall terms used: gate-profiles width RAM det_ram thrash cgroup pool dispatch knob wall scratch repos memory pressure

The question passed with them: "why does the gate runner size its pool from RAM once and what
happens when memory runs short during a bar".
