# TOOL-aBriskPreflight-4 — preflight starts its bounded probes together and collects each at its own check

**Status:** CLOSED · rev-3 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 2 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md](../build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.md](../build/2026-10-11-build-TOOL-aBriskPreflight-4-probes-ab.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-4-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-4-build-brief.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-4-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-4-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

In the peer's 1561 s old-code preflight, `run_bounded` waited 754 s on four children it started and
awaited one after another inside `verb_preflight`'s precondition block: the wiring check (544 s),
the lander's `--carry` (57 s) and `--prepared` (43 s), and the profile command (55 s) (PINNED, the
baseline record, node `a`, 2026-10-11). None reads another's output. This unit starts the four
together and reads each where it is read today, so the block's wall is about its longest child
rather than their sum, while every printed line, its order, every refusal number and every
refusal's text stay as they are.

## 2. Scope (IN)

Line numbers are at b726385f and move once TOOL-aBriskPreflight-5 lands first in the same file.

- **S1** — THE RUNNER IN TWO HALVES. `run_bounded` (`tools/unattended/unattended.sh:234`) becomes a
  call of two new functions, and its callers see no difference. `init_bounded <argv…>` creates the
  capture directory, launches today's wrapper line, waits for its exec marker, records the child
  with `write_proc_record` and sets `RB_HANDLE`. `read_bounded <handle>` waits for that child and
  sets `RB_OUT`, `RB_STDOUT`, `RB_ERR` and `RB_TOOK`, and returns the child's status, exactly as
  `run_bounded` sets and returns them today. Kept unchanged: the capture through two files and never
  a substitution; the wrapper carrying the repository root as its `$0`, ended by `; exit $?`; the
  exec-marker wait before the record; `</dev/null`; `RB_BOUND` read per call, at the start;
  `GATE_BOUND_LIVE`'s unbounded path; and the capture-failure branch, its sentence in `RB_OUT` and
  `RB_TOOK` zeroed. `RB_TOOK` is measured from that child's own start. Observed by AC9.
- **S2** — ONE GUARD, TWO READERS. A new `check_wiring_runnable` answers whether the declared
  `WIRING_CHECK` may run: declared, and every dash-led token one of `--check`, `--dry-run`,
  `--verify` and `-n`. It prints nothing and leaves the first refused token in `WR_TOKEN`, empty when
  nothing is declared. `check_wiring` asks it and prints its two check 4 refusals byte for byte, in
  today's order, and the probe starter asks it before starting the wiring child. Observed by AC7.
- **S3** — THE PROBES START TOGETHER. A new `init_preflight_probes <slug>` runs in `verb_preflight`
  between `check_branch` and `check_wiring`. It starts, through `init_bounded` and in this order: the
  wiring check, when `check_wiring_runnable` passes; the lander's `--carry` and then its
  `--prepared`, when `LANDER_MODE` is `in-place`; and the profile command, when `GATE_PROFILE_CMD` is
  declared. Each handle goes to its own `PF_PROBE_*` variable, and the function prints nothing. A
  start that cannot create its capture leaves its variable empty, so its reader runs the synchronous
  form at its own position and prints today's sentence there. Observed by AC3, AC4 and AC8.
- **S4** — EACH PROBE IS READ WHERE IT IS READ TODAY. `check_wiring`, `run_lander` and
  `derive_gate_backstop` each take their pending handle when one is set, clear its variable and call
  `read_bounded`, and otherwise run `run_bounded` as today. Nothing after the read moves. Their
  callers at `--close` (`tools/unattended/unattended.sh:9964`, `:10173` and `:10603`) find no handle
  and keep the synchronous form. Observed by AC1, AC2 and AC6.
- **S5** — NO PROBE OUTLIVES THE VERB UNREAD. A new `read_preflight_probes` runs after the
  `GB_CMP` case that follows `derive_gate_backstop`. It reads every handle still pending and discards
  what it read, and it prints nothing. It leaves `RB_OUT`, `RB_STDOUT`, `RB_ERR` and `RB_TOOK` as it
  found them. The one handle it can meet is `--prepared`'s, after `check_lander_mode` refused on
  `--carry` and returned before reading it. Observed by AC5.
- **S6** — THE SUITE FOLLOWS THE SPLIT. `tools/unattended/unattended.test.sh` extracts `run_bounded`
  by its definition line at `:8451` and `:8588`, and through `slice_fn` at `:12096`; each site also
  extracts the two halves, and `:8588`'s count of closing braces rises from three to five. Arms
  stage AC1 to AC8 on stub children, and `FLOOR_ASSERTIONS` and the floor of the region holding
  them rise by their count. NOT OBSERVED by a criterion of its own: the suite runs once, at the
  close, and AC1 to AC9 are the observations its arms repeat.
- **S7** — THE RECORDS. The Reuse affordance line of `memory/map/features/unattended-stops.md` says
  that a verb overlapping several bounded commands calls the two halves, and
  `memory/map/generated/symbols.json` is re-rendered by `gen_map.py --write`. NOT OBSERVED by a
  criterion: the `codebase-map coverage + freshness` leg grades both.

## 3. Non-goals (OUT)

- The driver's readers `fact`, `runmd_of` and `readme_of`. `TOOL-aSparedSpawn-8` S1 plans them.
- The children's own cost. TOOL-aBriskPreflight-1, TOOL-aBriskPreflight-2 and
  TOOL-aBriskPreflight-3 own the wiring check's; `tools/push-main.sh` and
  `tools/run-gates/run-gates.sh` are not edited.
- Overlap anywhere but `--preflight`. `--close`, `--dispatch`, the ask generator and the lander keep
  the synchronous form.
- How `check_lander_mode` maps a lander's exit to a refusal. `TOOL-dDerivedDocket-68` is the open
  ask about that mapping, and this unit reads the same statuses the same way.
- A wall-clock ceiling on any child. TOOL-aBriskPreflight-7 owns that.
- A kill of a probe left unread. A kill is the least reversible act the driver takes, and its own
  comment at `tools/unattended/unattended.sh:7144` keeps it for the lease holder's reap.
- A new `.unattended.conf` key, a switch for the overlap, or any change to the protocol. A key owes
  a protocol key-table row, and the protocol is a governance carrier.
- Any change to where `check_clean` and `check_branch` sit, or to what they read.
- The unattended kit's version bump. The build makes one bump per kit, after its last move.

### Edges

- **hands-off** `TOOL-aBriskPreflight-7` — the wiring child's bound is read when that child STARTS,
  so the per-call `RB_BOUND` that unit sets for the ceiling is set around the start of the wiring
  child in the probe starter, not around the read in `check_wiring`; check 4's kill is still read in
  `check_wiring`, where this unit leaves it.
- **hands-off** external — the protocol's key table does not say that a lander's `--carry` and
  `--prepared` write nothing. This unit overlaps both with the block's checks on the driver's own
  naming of them as read-only calls, and stating that in the protocol is the owner's change to a
  governance carrier.

## 4. Design

### Evidence

Read at 748ca395 on 2026-10-11. Its `tools/` bytes equal b726385f's, because a `git diff --stat`
from b726385f2 to HEAD over `tools/` prints nothing.

- `run_bounded` is `tools/unattended/unattended.sh:234` to `:273`. It takes `_d` from `mktemp -d`
  and `_s` from `date +%s`, launches the wrapper at `:258` or `:260` with `&`, polls `$_d/up` up to
  100 times, calls `write_proc_record "$_p" "$@"`, then `wait "$_p"` and reads both capture files.
- Those two `&` lines are the only background jobs in the driver and its library, and that `wait`
  is the only `wait`. No function the block runs calls a bare `wait`, which would have collected the
  probes' statuses before their readers asked for them.
- `check_wiring` (`:2711` to `:2752`) refuses an undeclared `WIRING_CHECK` and a dash-led token
  outside its allow-list with two `fail 4` lines, then runs `run_bounded $WIRING_CHECK`.
- `run_lander` (`:2765`) is `run_bounded $LANDER "$1" --slug "$2"`. `check_lander_mode` (`:2778`)
  runs `--carry` then `--prepared`, and returns 1 after `fail 60` or `fail 61` on `--carry` without
  running `--prepared`.
- `derive_gate_backstop` (`:9168`) returns before running anything when `GATE_PROFILE_CMD` is blank,
  and otherwise runs `run_bounded $GATE_PROFILE_CMD`.
- The block is `:6994` to `:7013`: `check_clean`, `check_branch`, `check_wiring`, `check_method`,
  `check_waivers`, `check_single_live`, `check_cross_run_overlap`, `check_lander_mode`, then
  `derive_gate_backstop` and its `GB_CMP` case, each joined by `|| true`. Every early `return` of
  `verb_preflight` sits above `check_clean` or below that case, and `fail` (`:685`) never exits, so
  every read point is reached on every path through the block.
- `tools/push-main.sh:186` and the `case` under it install no trap for `--carry` or `--prepared`.
  `cmd_carry` (`:828`) and `cmd_prepared` (`:843`) write no file in the work tree or the git dir;
  `--carry`'s two `mktemp` files sit in the system temp directory and are deleted before it
  returns. The one git write is `read_tip_object`'s `git fetch` of the default branch (`:368`),
  reached from `--carry` alone and only when the advertised tip object is not already local.
- `tools/run-gates/run-gates.sh:1006` states that `--print-profile` exits before the turnstile and
  runs no leg, writes no run record and touches no ledger.
- The suite's exec-marker arm (`tools/unattended/unattended.test.sh:8502`) reads `$_d/up` through
  bash's dynamic scope from inside a `write_proc_record` stub, so the half that calls the recorder
  keeps the capture directory in a local named `_d`.
- The suite sources these functions alone under `set -u` (`tools/unattended/unattended.sh:256`). An
  associative array declared only at file scope would be an indexed one there
  (`tools/unattended/unattended.sh:4345`), so the handle is a plain string.

### The two halves

`init_bounded` sets `RB_HANDLE` to one string holding the child's pid, its start second and its
capture directory, the directory last because a path may carry a space. On a capture failure it sets
today's sentence in `RB_OUT`, empties `RB_STDOUT`, `RB_ERR` and `RB_HANDLE`, zeroes `RB_TOOK` and
returns 1. `read_bounded` splits the handle with parameter expansion and starts no process to do
so. It then runs today's tail of `run_bounded` from the `wait` on, cleaning the directory up.
`run_bounded` is `init_bounded "$@" || return 1` followed by `read_bounded "$RB_HANDLE"`, so one
wrapper line exists, as `TOOL-aBoundedCeiling-6` requires of the one bounded runner.

`RB_TOOK` runs from the child's own start to the moment its read returns. For a synchronous call
that is today's figure. For a probe it can exceed the child's own wall only when the child finished
before its reader asked. The one probe whose `RB_TOOK` preflight prints is the wiring check's, in the
check 4 kill message, where the child ran to its bound, so the printed figure is the bound's.

### The order of the block

```
check_clean || true
check_branch || true
init_preflight_probes "$slug"      # wiring, --carry, --prepared, profile: started, nothing printed
check_wiring || true               # reads the wiring child
check_method || true
check_waivers "$rel" || true
check_single_live || true
check_cross_run_overlap "$slug" || true
check_lander_mode "$slug" || true  # reads --carry, then --prepared
derive_gate_backstop || true       # reads the profile
case "$GB_CMP" in ... esac
read_preflight_probes              # reads and discards whatever is still pending
```

The wiring check starts first because it is the longest child and the first read. The three others
start while it runs, so their exec waits and ledger writes delay the block only if the wiring child
finishes before they do.

Each reader takes its handle by copying the variable and emptying it before the read, so a handle
is read at most once, and `read_preflight_probes` meets only what no reader took.

### The lander's two probes, side by side

`--carry` and `--prepared` run at the same time as each other, as the wiring check, as the profile,
and as `check_method` through `check_cross_run_overlap`. Neither takes a lock or a marker, and
`--prepared` writes nothing. `--carry` may fetch the default branch into its remote-tracking ref.
Two readers in the window read remote-tracking refs:

- `check_cross_run_overlap` lists `refs/remotes/<remote>/` with `--no-merged` against the anchor
  and HEAD. A fetch that brings the ref up to the anchor leaves it merged, so it is out of the list
  either side of the fetch. Only when the remote moved again between the anchor observation and
  `--carry`'s own can the fetched ref sit past the anchor and enter the list. That changes a count
  on the probe's report line and never a verdict, because the probe always returns 0.
- The wiring check's skill arm reads `refs/remotes/<remote>/HEAD` for a merge base only in a linked
  worktree whose branch edits the kickoff engine. That merge base moves only when HEAD already holds
  a default-branch commit newer than the local ref.

Both are residuals of one race, a remote moving inside the block, and §5 names them.

`check_clean` reads the working tree before any probe exists, so no project-declared command can
change its verdict. That is why the probes start after it rather than at the very top (§8 F1).

### Leaving the block early

On every ordinary path each started probe is read: by its reader, or by `read_preflight_probes`. A
driver ended by a signal or by a `set -u` abort leaves up to four probes running instead of today's
one. Each has its ledger row from the moment it started, naming this driver's pid, so `--status`
counts it and the next `--preflight`'s `run_orphan_reap` reaps it, exactly as it reaps today's one.
None holds the caller's stdout, because each child writes only to its capture files.

### Rollout

Not landed dark. The template's dark landing is for behaviour whose proof needs the landed tree,
and every criterion here is observed in the pass, on fixtures and on node `a`'s real children. The
change reverts as one commit. A switch was considered and rejected: a conf switch needs a protocol
row, and a file constant nobody turns off is dead code. If AC10 is red, the unit does not ship: it
is retired by M2's AMEND with the A/B as its reason, and the halves go with it.

### Inventory

| Identifier | What it is | Cell |
|---|---|---|
| `init_bounded` | starts a bounded child and records it | `sh.function` |
| `read_bounded` | waits for one child and reads its capture | `sh.function` |
| `check_wiring_runnable` | the wiring check's guard, asked by two readers | `sh.function` |
| `init_preflight_probes` | starts preflight's four probes | `sh.function` |
| `read_preflight_probes` | reads and discards any probe left pending | `sh.function` |
| `RB_HANDLE` | the last started child's handle | none: no cell grades a shell variable |
| `WR_TOKEN` | the first token the guard refused | none |
| `PF_PROBE_WIRING`, `PF_PROBE_CARRY`, `PF_PROBE_PREPARED`, `PF_PROBE_PROFILE` | the pending handles, empty at file scope | none |

Each function name was asked of `tools/lexicon/lexicon.py` with `--suggest` and `--as sh.function`
at writing, and each answered OK.

### Files touched (estimate)

`tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh`
`memory/map/features/unattended-stops.md`
`memory/map/generated/symbols.json`

### Alternatives rejected

- Start the four before `check_clean`, the brief's "top of the block". A declared lander or profile
  command is a project's, and a write it made could change `check_clean`'s verdict; the overlap given
  up by starting after `check_branch` is a few git reads (§8 F1).
- Start three probes and run the wiring check synchronously in `check_wiring`. The longest child
  would then wait behind three exec waits and three ledger writes, each several spawns at node `a`'s
  measured cost (§8 F2).
- A wrapper stamp of each child's own end, read for `RB_TOOK`. It changes the wrapper's text for
  every caller to sharpen a figure no preflight probe prints except at a kill.
- A second launch line beside `run_bounded`'s for the overlapped form. Two copies of the wrapper are
  the drift `TOOL-aBoundedCeiling-6` removed.
- A pool collected with `wait -n`, as the gate runner collects its legs. It returns children in
  finishing order, so a refusal would print where its child finished rather than at its check.
- An associative array of handles. The suite sources the halves alone under `set -u`, where an
  undeclared one silently becomes an indexed array.

## 5. Production-readiness checklist

- security — No new write path and no new surface. `check_wiring_runnable` is asked before the
  wiring child starts, so a repairing flag such as `--session` is refused before anything runs
  (AC7), the class `memory/gotchas/destructive-step-before-its-precondition.md` names. Every child
  keeps `</dev/null` and file capture.
- perf / scale — The block's children cost about their longest rather than their sum (AC3), and on
  node `a` the A/B decides whether that survives four children at once on a loaded host (AC10). The
  three extra exec waits and ledger writes run while the wiring check runs.
- error / empty / loading states — An undeclared or refused wiring check starts nothing; `primary`
  mode starts no lander probe; a blank profile command starts no profile; a capture failure runs the
  synchronous form at the read point; a probe left unread is read and discarded.
- observability — Every child keeps its ledger row, and a child killed at its bound is named by the
  same refusal as today. Nothing new is printed.
- risks — A declared lander or profile command that writes something a check in the window reads
  now races that check; gov's own write nothing in the window, as §4 records, and the protocol does
  not yet say an adopter's must not (§3 Edges). When the remote moves inside the block, `--carry`'s
  fetch can change a count on the overlap probe's report line, or the skill arm's merge base in the
  one worktree state §4 names; neither is a refusal today's order would not also meet on the next
  preflight. More load during the wiring
  check can flip its straggler `note` to `exited 124`, which is a `note` and is printed only when the
  check fails. A signal now leaves up to four recorded orphans instead of one.
- testing — AC1 to AC9 in the pass, on stub children; AC10 on node `a`'s real children; the suite's
  arms at the close (§7).
- migration — None. The ledger gains rows in its existing format, and no record or conf changes.
- user docs — N/A for `help/`: the change is internal to `--preflight` and prints nothing new. The
  map dossier's affordance line is the record S7 refreshes.

## 6. Acceptance criteria

The fixtures live under `%TEMP%/bp4`, a short path, because a clone under the scratchpad fails with
`Filename too long`. Each is a repository with a bare origin, built the way the suite's `mkconf`
and `fixture` helpers build one, with `LANDER_MODE="in-place"`, `LANDER="bash lander.sh"`,
`GATE_PROFILE_CMD="bash profile.sh"` and `WIRING_CHECK="bash wire.sh --check"`, committed.
`lander.sh` dispatches on its first argument. Every run starts from a fresh copy of one
pristine fixture at one path, so two drivers see identical bytes. "Old" is the driver at the commit
the pass started from, run from a clone at that commit under `%TEMP%/bp4o`; "new" is the pass's
driver. Each run is `bash <driver> --preflight tRun --keepalive-id k1` from the fixture.

- **AC1** — When fixture F1 runs `--preflight` under old and under new, where every stub answers at
  once with 0, or 1 from the lander, `cmp` finds their stdout and their stderr byte-identical and
  the two exit statuses are equal.
  Red when: any line moves, appears or is missing.
- **AC2** — When fixture F2 runs, old and new print byte-identical output. In F2, `wire.sh`
  prints `WIRE-OUT` and exits 1, `--carry` prints `CARRY-OUT` and exits 2, `--prepared` prints
  `PREP-OUT` and exits 1, and `profile.sh` exits 3. In new's output `UNATTENDED check 4 FAILED`
  precedes `WIRE-OUT`, which precedes `UNATTENDED check 60 FAILED`, which precedes `CARRY-OUT`,
  which precedes `the wall is not compared with the largest leg ceiling`. `PREP-OUT` appears
  nowhere.
  Red when: a refusal or a probe's captured output prints at another position, or `PREP-OUT` prints.
- **AC3** — When fixture F3 runs new, `OVERLAP` exists afterwards, and new's wall is at least 20 s
  below old's on the same fixture. In F3, `--carry`, `--prepared` and `profile.sh` each create
  a start marker and sleep 10 s, and `wire.sh` polls up to 60 s for all three markers, creates
  `OVERLAP` when it sees them, and exits 0.
  Red when: `OVERLAP` is absent because the children ran one after another, or the walls differ by
  less than 20 s.
  figure: the 10 s and 60 s are PINNED stub values; both walls are DERIVED per run.
- **AC4** — When new has run fixture F2, which refuses and so prunes nothing, the slug's ledger
  holds four rows. That ledger is `tRun.procs` in the `unattended` directory of the git common dir.
  Its rows' argv fields read `bash wire.sh --check`, `bash lander.sh --carry`,
  `bash lander.sh --prepared` and `bash profile.sh`, and each names a pid and this driver's pid.
  Red when: a started child has no row.
- **AC5** — When fixture F4 runs new, `PREP-DONE` exists when the verb returns, `PREP-OUT` is absent
  from its output, and `kill -0` on the pid of the `--prepared` row fails. In F4, `--carry` records
  the second it answered and exits 2 at once, and `--prepared` sleeps 30 s, creates `PREP-DONE`,
  prints `PREP-OUT` and exits 1. When the verb returns more than 40 s after `--carry` answered, the
  arm prints a NOTE that this run could not tell a probe read before the return from one left to
  finish alone.
  Red when: `PREP-DONE` is absent because the verb returned while the probe ran, or `PREP-OUT`
  prints.
  figure: the 30 s sleeper and the 40 s note threshold are PINNED; the verb's wall is DERIVED.
- **AC6** — When fixture F5 runs new with `GATE_BOUND` at 2 and a `--prepared` that runs
  `exec sleep 600`, its output holds `UNATTENDED check 61 FAILED` naming `bash lander.sh --prepared`,
  the verb returns within 300 s, and `kill -0` on that row's pid fails afterwards.
  Red when: the probe outlives its bound, or outlives the verb.
  figure: the 600 s sleeper and the 300 s hang backstop are PINNED; the verb's wall is DERIVED per run,
  and the gap between them is the margin a loaded host's whole preflight spends.
- **AC7** — When fixture F6 runs new with `WIRING_CHECK="bash wire.sh --session"`, where
  `wire.sh` creates `WIRE-RAN`, its output holds `WIRING_CHECK carries a flag this kit does not recognise as READ-ONLY`
  on an `UNATTENDED check 4 FAILED` line, `WIRE-RAN` does not exist, and the ledger has no
  `wire.sh` row. With `WIRING_CHECK` blank the output holds `WIRING_CHECK is not declared in .unattended.conf`
  and the same two absences hold.
  Red when: `WIRE-RAN` exists, because a repairing command started before its guard refused it.
- **AC8** — When fixture F7 runs, with `LANDER_MODE="primary"`, no `GATE_PROFILE_CMD` and a
  `wire.sh` that exits 1, old and new print byte-identical output, and new's ledger holds one row,
  `bash wire.sh --check`.
  Red when: a lander or profile row exists, or the outputs differ.
- **AC9** — When a scratch probe extracts `run_bounded`, `init_bounded` and `read_bounded` from new
  by their definition lines and sources them with `GATE_BOUND=2`, `GATE_BOUND_LIVE=1`, `ROOT` set
  and `write_proc_record` stubbed, these hold. `run_bounded bash -c 'sleep 30'` returns 124 or 137
  within 20 s, and `run_bounded bash -c 'sleep 30 & exit 0'` returns within 20 s.
  `run_bounded bash -c 'echo alive'` leaves `alive` in `RB_OUT`. A recorder stub testing `$_d/up`
  records `up`. With `GATE_BOUND_LIVE=0`, `run_bounded bash -c 'exit 3'` returns 3. Two
  `init_bounded` calls read back in the reverse order each return their own child's status and
  output.
  Red when: the split loses the bound, the file capture, the exec-marker wait or a handle's identity.
- **AC10** — When a scratch harness runs this worktree's four declared probe commands from
  `.unattended.conf` through new's halves, interleaving arm A and arm B three times each with
  `2026-10-11-build-TOOL-aBriskPreflight-1-host-state.sh` before each arm, the median wall of arm B
  is below the median wall of arm A. Arm A runs the four through `run_bounded` one after another in
  the block's read order. Arm B starts them through `init_bounded` in `init_preflight_probes`'s
  order and reads them through `read_bounded` in the block's read order. Each arm proves it ran: the
  wiring check's status is 0, the lander's two statuses are 0 or 1, and the profile's stdout carries
  a `wall` row.
  Red when: arm B's median is at or above arm A's, so four children at once on this host cost more
  than the overlap saves; the unit is then retired (§4 Rollout).
  cost: arm A pays the four children's sum, 699 s at BASE before the wiring check's own units land
  (PINNED, the baseline record's peer trace, 2026-10-11), so six arms take tens of minutes on node
  `a`; the walls are DERIVED per arm.
  permission: the lander runs only its two read-only flags, as preflight runs them today, under the
  same `GATE_BOUND`; no bar and no suite runs.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `pass-order history` · `brief-recorded`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · in-place fixtures whose stub children's exits, sleeps and markers stage each case, red against the sequential driver for AC3 and AC5 · FLOOR_ASSERTIONS and the floor of the region holding them, by the arms' count

New arm: tools/unattended/unattended.test.sh · covers AC9 · the run_bounded extraction widened to its two halves, red while any half is left out of a site · the closing-brace count at the capture-helper extraction, three to five

The pass verifies with AC1 to AC10 only. The listed legs run once, at the close, after the last
unit is terminal.

## 8. Open questions

- **F1 — Where do the probes start?** (a) Before `check_clean`, the brief's "top of the block".
  (b) Between `check_branch` and `check_wiring`. Under (a) a project-declared lander or profile
  command runs while `check_clean` reads the tree, so a write it makes could change a verdict that
  today cannot depend on it. Under (b) the overlap given up is `check_clean`'s and `check_branch`'s
  few git reads. Recommendation: (b).
  RESOLVED (agent, 2026-10-11, delegated): (b). It satisfies every criterion, and (a) leaves AC1's
  byte equality hostage to what an adopter's command writes.
- **F2 — Does the wiring check start with the others, or run synchronously after they start?**
  (a) It starts first in `init_preflight_probes` and is read in `check_wiring`, which costs one
  guard predicate shared by both. (b) Three start, then `check_wiring` runs it synchronously, with
  no guard to share. Recommendation: (a), because the wiring check is the critical path.
  RESOLVED (agent, 2026-10-11, delegated): (a). It is the faster of the two by the three starts it
  does not wait behind, and it trips no veto.
- **FACT-QUESTION · F3 — May the lander's two probes overlap each other, the wiring check and the
  block's checks?** Probe: read `tools/push-main.sh` along the `--carry` and `--prepared` paths for a
  trap, a lock, a marker, a verdict file or a git write. Deciding observation: no trap is installed
  for either flag, neither writes a file, and the one write is `--carry`'s conditional fetch of the
  default branch. Liveness: the same read along `--land` finds its EXIT trap and its
  `claim-push.lock`, so the probe reports a write where one exists.
  RESOLVED (agent, 2026-10-11, delegated): they may overlap. The fetch's two readers in the window
  are named in §4 with what each reads, and the residual is in §5.
- **F4 — What happens to a probe the block leaves unread?** (a) It is read and discarded after the
  block's last read. (b) It is killed. (c) It is left running as a recorded orphan for the next
  reap. Under (c) every preflight refused on `--carry` leaves a live process behind; under (b) the
  driver kills outside the lease holder's reap. Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a). No child outlives the verb on an ordinary path, and
  nothing is killed.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the spec brief
  `2026-10-11-prompt-TOOL-aBriskPreflight-4-spec-brief.md`.
- rev-2 · 2026-10-11 · AC6's sleeper 60 s -> 600 s and its wall 40 s -> 300 s. Observed in the pass on
  node `a`: under a concurrent bar a whole fixture `--preflight` took 149 s to 516 s under both drivers,
  so a 40 s wall reds for the host and not the bound. A 600 s sleeper keeps the arm red when the bound
  does not fire, and 300 s is the hang backstop the sibling wiring-bound arm already uses.
- rev-3 · 2026-10-11 · AC5's sleeper 5 s -> 30 s, and a NOTE when the run cannot discriminate. A
  staged break, the driver with its `read_preflight_probes` call deleted, passed AC5 at 5 s on node
  `a`: the verb's own remainder after `--carry` outlasted the sleeper, so the unread probe finished
  alone before the verb returned. The arm now says when that happened rather than reading as cover.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py`, asked the phrase in the first fenced line below, ranked
`boundedParallel`, `scan_processes`, `run_bounded` and `read_bound_key`. `boundedParallel` caps a
Workflow script's agent fan-out in JavaScript and runs no process. `scan_processes` is process-monitor's
census. `run_bounded` is the seam this unit extends, the one the map dossier
`memory/map/features/unattended-stops.md` names as the reuse affordance for a declared command a
verb must bound and record. No existing seam overlaps several bounded commands, so this unit splits
`run_bounded` rather than adding a second runner. The gate runner's own leg pool in
`tools/run-gates/run-gates.sh` was read and rejected in §4 Alternatives, because it collects in
finishing order.

The recall probe returned `TOOL-dDerivedDocket-28`, the process ledger S1 keeps writing per child;
`TOOL-dDerivedDocket-3`, the two lander probes and their exit codes; `TOOL-dDerivedDocket-68`, the
open ask on that exit mapping, left untouched (§3); and `TOOL-aPromptedMandate-9`, the wiring seam
first measured slow. Their claims were verified against source at 748ca395.

Recall terms used: run_bounded preflight process ledger write_proc_record orphan reap lander carry
prepared GATE_PROFILE_CMD WIRING_CHECK concurrent. The two probes, verbatim:

```bash
python tools/codebase-map/reuse_lookup.py "start several bounded child processes together and collect each result later"
python tools/memory-recall/query.py "how does preflight bound and record the commands it waits on, and may the lander probes run concurrently" --terms "run_bounded preflight process ledger write_proc_record orphan reap lander carry prepared GATE_PROFILE_CMD WIRING_CHECK concurrent"
```
