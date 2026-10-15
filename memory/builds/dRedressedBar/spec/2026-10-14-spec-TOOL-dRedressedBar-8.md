# TOOL-dRedressedBar-8 — arm 11g AC14 bounded, and its FIFO server kept alive through MSYS's failed opens and broken pipes

**Status:** CLOSED · rev-3 · 2026-10-14 · node d · Tier-1 · base ebce889c · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md](../build/2026-10-14-build-TOOL-dRedressedBar-1-research-bar-profile.md) | research | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-9 |
| [2026-10-14-prompt-TOOL-dRedressedBar-8-1-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-8-1-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-8-brief.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-8-brief.md) | research | — |
| [2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-1-9-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-9 |
| [2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md) | diff-review | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 |

<!-- /gen:spec-records -->

## 1. Goal

Arm 11g AC14 of `tools/run-gates/run-gates.test.sh` hangs the `run-gates canary` leg to its 13200 s
ceiling whenever its FIFO server dies, and on this host the server dies within a few reads. This
unit keeps the server alive through the two failures that kill it, and bounds the arm's nested bar,
so a dead or silent server reds the arm with a line naming it.

## 2. Scope (IN)

- **S1** — `serve.sh`, the server the arm writes at `run-gates.test.sh:3590-3611`, survives a failed
  FIFO open and a write to a reader that has left. It ignores `SIGPIPE`. It retries a failed open
  after 0.1 s while the FIFO still exists, and exits when the FIFO is gone. It waits 0.2 s after each
  answer before it opens again. What it serves is unchanged. Its stderr goes to `$MP/x/serve.err`
  instead of `/dev/null`. Observed by AC1 and AC2.
- **S2** — `run_mp_bar` (`run-gates.test.sh:3410-3416`) runs its nested runner under
  `timeout -k 5s "$MP_BOUND"` when the caller sets `MP_BOUND`, and exactly as today when it does
  not. Only the `ac14` call sets it, to the calibrated `_mpwall` of arm 11c (`:3519`).
  Observed by AC3, AC4 and AC6.
- **S3** — After the `ac14` run, the arm reads the server's own exit status and checks it before the
  verdict. A server that ended before the arm's kill reds the arm with a line naming `serve.sh`, its
  exit status and its stderr. A nested bar killed at its bound, with the server alive, reds with a
  line naming the bound, the seconds taken and `serve.sh` alive. Otherwise the verdict check at
  `:3623-3626` runs unchanged. The half stays one counted assertion. Observed by AC3, AC4 and AC6.
- **S4** — On a host with no runnable `timeout -k`, where `HAVE_TIMEOUT` (`:286`) is not 1, the
  forced-branch half prints an announced SKIP and runs no nested bar. Its count at `:3612` is kept.
  Observed by AC5.

## 3. Non-goals (OUT)

- No edit to `tools/run-gates/run-gates.sh`. The brief excludes it: the memory pause is the subject
  under test. That includes `read_mem_used` blocking in its open of a FIFO with no writer
  (`run-gates.sh:590-593`). Production leaves `GATE_MEMINFO` unset, so the read is `/proc/meminfo`
  (`run-gates.sh:587`), which never blocks.
- No change to what `serve.sh` serves. The 10 % and 95 % answers stay keyed on the trigger rows. The
  go file, the await and the one-second hold stay as they are.
- No `GATE_WALL` on the `ac14` call. Section 4 shows the wall cannot reach this hang.
- No bound on any other `run_mp_bar` call. Every other arm reads a regular file, and only a FIFO read
  can block forever.
- No new counted assertion and no `FLOOR_ASSERTIONS` change. The new red branches sit inside the one
  assertion `:3612` counts.
- `GATE_REGEN_CHECK` reaching nested runners stays a separate finding, as the brief says.

### Edges

- **hands-off** `TOOL-dRedressedBar-10` — what the round-1 spec audit found (report ids 4, 5 and
  12). AC6 diffs from the build base, so a sibling's `tools/` edit on the branch reds it on a correct
  build. §6 says the fork leg reads none of `tools/run-gates/run-gates.test.sh`, yet `scan_spawn_tree`
  grades it for the registry classes. That unit reads this unit's pass commit alone, counts its sites
  with the leg's classifier, corrects §6, and writes the hands-off to `TOOL-dRedressedBar-7` these
  Edges lack.
- **hands-off** `TOOL-dRedressedBar-7` — the tree this unit leaves, which that unit measures. Its one
  `tools/` file, `tools/run-gates/run-gates.test.sh`, is `project-owned`
  (`tools/run-gates/kit.toml:40-41`), outside `EPOCH_ROLES`, so this unit leaves that unit no
  version to bump.

## 4. Design

### What hung, from the retry's records

The retry's fixture was read at spec time under `gate-work.ca8UP9EB/tmp/tmp.QQMdypyuDs/`, and it
has since been removed, so the table is PINNED to that reading (2026-10-14). Its records correct
one reading in the brief. The runner was not in a hold loop. Its main shell was blocked opening the
FIFO for a dispatch decision:

| Record | What it shows |
|---|---|
| `r/.git/gate-run/ac14/header` | `dispatch 1 2 0`, so A14 was dispatched first, then Y14, then C14, and `census_every 60` |
| `r/.git/gate-run/ac14/` | one `1.leg` (A14, 74.028 s, exit 0), no `0.leg`, no `2.leg`, no `pauses`, no `verdict` |
| `x/ac14.go` | absent, so the server never reached its 95 % branch |
| `r/.git/gate-run/ac14/census` | one row every 60 s from the run's start, 20:01:24Z, to the file's last write at 21:39:30Z, 98 minutes later |

A hold needs a reading above 90 %. The server serves 95 % only after it writes the go file
(`run-gates.test.sh:3602-3606`), and that file was never written, so no hold ever opened. The
`sleep 60` was the census watcher's tick (`CENSUS_EVERY=60`, `run-gates.sh:2919`, loop at
`:4270-4279`). Y14 is the second dispatch, decided while A14 ran: `check_dispatch_pause`
(`:5092`) calls `read_mem_used` (`:638`), whose `done < "$f"` (`:590-593`) opens the FIFO for
reading. With no writer, that open blocks forever.

The brief also asks for confirmation that AC6 to AC13 completed in the retry. They did. `ac7`,
`ac12`, `ac13`, `held` and `ac14seed` each hold a `verdict`. `ac12/pauses` closes `unread` and
`ac13/pauses` closes `wall`. The `ac5` and `ac6` records were pruned by retention: the runner keeps
the five newest (`GATE_RUN_KEEP=5`, `run-gates.sh:2559`, pruned at `:5658`). `x/m6` was last written
at 23:00:46, which is the rewrite at `run-gates.test.sh:3530` that runs only after the `ac6` bar
returns. The first attempt's log stops at the AC6 calibration line because `check_mp_value` prints
only on failure (`:3420-3423`). That echo (`:3520`) is the last unconditional line before 11g.

The hang reproduces outside the bar. The probe `probe-11.sh` below, run unstaged over this tree
(`tools/` is unchanged from `ebce889c7`), printed the AC6 calibration and then held in AC14 until its
900 s outer bound. Its `ac14` record held only a `header` reading `dispatch 1 2 0`, no leg had run,
and no `serve.sh` process was alive. So on this run the runner blocked at A14's own first decision
(PINNED, node d, 2026-10-14, one run).

### Why the server dies: a probe of its loop

The server's loop opens the FIFO (`exec 3>"$f" || exit 0`, `:3600`), writes one answer, closes, and
re-opens at once. A scratch copy of that loop shape, answering a reader shaped like `read_mem_used`
as fast as it reads, died in every run (PINNED, node d, 2026-10-14):

| Server variant | Runs | How it ended |
|---|---|---|
| as shipped | 3 | dead after 31, 31 and 4 reads. Twice the open failed with `No such file or directory` on a FIFO that exists, and `\|\| exit 0` ended it with exit 0. Once `printf` met a reader that had left, and `SIGPIPE` killed it with exit 141 |
| ignores `SIGPIPE`, retries a failed open | 2 | alive after 300 reads, through 1 and 5 failed opens and 13 and 1 failed writes. 12 and 1 of the 300 reads came back empty |
| the same, plus 0.2 s after each close | 2 | alive after 300 reads, all 300 carrying a reading, with no failed open and no failed write |

Both death modes are root-caused by the table. The mechanism behind them is UNVERIFIED. The likely
reading is that a writer re-opening at once meets the reader that is still draining the previous
answer, so its open meets a pipe instance mid-teardown, or its write meets a reader that is leaving.
That is consistent with the arm's own note that an MSYS reader can take two writer opens before its
EOF (`:3595-3596`).

An empty read matters here. `read_mem_used` returns 1 on it, and `check_dispatch_pause` then lets
the dispatch go as `unread` (`run-gates.sh:654-656`). At C14's decision that opens no episode, and
the arm reds as `[]`. Survival alone turns a hang into an occasional red, and the settle removes it
in the measured runs. That is why S1 carries all three changes.

### The server (S1)

The server keeps its argument contract and its serving rule. Its loop becomes the following shape.
The two lines a staged break edits, the open at the head of its line and `exec 3>&-` alone on its
line, are spelled exactly as the probes below expect.

```bash
trap '' PIPE
f=$1; await=$2; go=$3; shift 3; held=""
while [ -p "$f" ]; do
  exec 3>"$f" || { sleep 0.1; continue; }
  pct=10
  # … the trigger test, the go file, the await and the one-second hold, unchanged …
  printf 'MemTotal: 1000 kB\nMemAvailable: %s kB\n' "$(( (100 - pct) * 10 ))" >&3
  exec 3>&-
  sleep 0.2
done
```

With `SIGPIPE` ignored, a write to a departed reader prints a broken-pipe line to stderr and the loop
goes on. `[ -p "$f" ]` held through every failed open in the probe, so the loop condition ends the
server only when `rm -rf "$MP"` takes the FIFO away. The header comment gains a paragraph that names
this unit, the two death modes and the measured table above. The launch at `:3618-3619` sends
stdout to `/dev/null` and stderr to `"$MP/x/serve.err"`.

### The bound (S2), and why it is not the wall

The brief offers `GATE_WALL` as an example. The wall cannot end this hang. Its watcher writes
`wall.breach` and reaps each leg with a pid file and no rc (`run-gates.sh:4189-4196`). The reader
loop reads the marker only at its head (`:5078`). A main shell blocked in an open inside a dispatch
decision is neither a leg nor at the loop head. In the retry, A14 had already ended, so there was no
leg to reap either.

The suite already bounds nested bars with `timeout`: the clamp arms at `run-gates.test.sh:937`,
`:956` and `:969`. `run_mp_bar` gains the same bound, behind a variable its other callers never
set:

```bash
( cd "$MP/r" && ${MP_BOUND:+timeout -k 5s "$MP_BOUND"} env GATE_FULL= … bash $KIT_REL/run-gates.sh … ); MP_RC=$?
```

Its header comment gains `MP_BOUND=<s>`, with exit 124 or 137 on expiry. The `ac14` call becomes
`MP_BOUND=$_mpwall run_mp_bar ac14 …`, timed with `date +%s` around the call as arm 11c times its
calibration (`:3517`). `_mpwall` is `4 * (_mphold + _mpcal) + 60` and never under 120 s (`:3518-3519`).
It is DERIVED per host, and was 128 s on node d on 2026-10-14. A healthy `ac14` run takes seconds.
`run_mp_bar` captures to files, which is the form arm 1c (`:304-323`) shows a `timeout` bounds on
the clock, where a captured substitution does not. On expiry `timeout` also ended a background
child of the command it ran, and spared a sibling started outside it (PINNED, node d, 2026-10-14,
one scratch probe). So the expiry reaches the runner's legs and census watcher, and the server,
started by the suite's shell, survives it to be read.

### The liveness check (S3)

The arm already kills the server, releases a blocked writer and waits (`:3622`). The wait's status
becomes the liveness reading: 143 is the arm's own `TERM` reaching a live server, and anything else
is the status the server died with. The `kill -0` alternative is rejected below. The checks run in
this order, all inside the one assertion:

1. Server status not 143:
   `canary: memory pause — AC14 the FIFO server serve.sh died before the run ended (exit <rc>), so a dispatch decision read a FIFO with no writer; the nested bar exited <MP_RC> after <s>s`,
   then `$MP/x/serve.err` indented by four spaces, then `fail=1`.
2. `MP_RC` 124 or 137:
   `canary: memory pause — AC14 the nested bar outlived its <_mpwall>s bound (exit <MP_RC> after <s>s) with the FIFO server serve.sh alive, so the server stopped answering`,
   then `fail=1`.
3. Otherwise, the verdict check at `:3623-3626`, unchanged.

The 11g comment gains what this does not check. The bound proves the arm ends, not that the forced
branch decided, which the verdict check grades. The settle makes a lost answer rare but cannot rule
it out under load, and a lost one reds as `[]` rather than hanging.

### The SKIP (S4)

The branch at `:3613` gains a first arm, before the `mkfifo`. Where `HAVE_TIMEOUT` is not 1 it prints
`canary: SKIP arm 11g's forced-branch half — this host has no runnable 'timeout -k', so the nested bar that reads the FIFO cannot be bounded`
and runs nothing. This is the suite's announced-skip pattern for the arms that need `timeout`
(`:299-302`, TOOL-aSiftedFork-7). The `n=$((n+1))` at `:3612` stays above the branch, so the count
holds on such a host.

### The probes

The builder writes both under a scratch directory `$P` outside the worktree, and runs them from the
worktree root. Neither is committed.

`probe-serve.sh` runs the server out of the suite, against a FIFO, for a set number of reads. Its
triggers never exist, so every answer is 10 %. Once the server is gone, a release subshell hands any
blocked reader a writer and then EOF, so the probe cannot hang.

```bash
#!/usr/bin/env bash
# probe-serve.sh <worktree> <scratch dir> <reads>
set -u
ROOT=$1; S=$2; N=$3
rm -rf "$S"; mkdir -p "$S"
awk '/^cat > "\$MP\/x\/serve.sh" <<.SH.$/ { f = 1; next } f && /^SH$/ { exit } f' \
  "$ROOT/tools/run-gates/run-gates.test.sh" > "$S/serve.sh"
mkfifo "$S/fifo" || { echo "probe: no mkfifo"; exit 2; }
bash "$S/serve.sh" "$S/fifo" "$S/no-await" "$S/go" "$S/no-trigger" >/dev/null 2>"$S/serve.err" & sv=$!
( while kill -0 "$sv" 2>/dev/null; do sleep 0.2; done; : > "$S/dead"
  exec 5<>"$S/fifo"; sleep 0.3; exec 5>&- ) &
ok=0; i=0
while [ "$i" -lt "$N" ] && [ ! -f "$S/dead" ]; do
  i=$((i+1)); av=""
  while read -r k v _; do case "$k" in MemAvailable:) av=$v ;; esac; done < "$S/fifo"
  [ "$av" = 900 ] && ok=$((ok+1))
done
if [ -f "$S/dead" ]; then wait "$sv"; rc=$?
else kill "$sv"; exec 4<>"$S/fifo"; exec 4>&-; wait "$sv"; rc=$?; fi
echo "probe: $ok of $i reads carried 10 %, $N asked · server exit $rc"
```

`probe-11.sh` runs section 11 alone, sliced out of the suite. It uses the sourced-not-run idiom of
`run-gates.turnstile.test.sh:1499-1510`, and `TOOL-aMeteredSweep-1` AC5 ran this section the same
way. A stage edits one line of the server. `dead` exits after the first answer, which is the
observed shape: A14 dispatched, then nothing. `silent` never opens. The `staged lines` count is the
liveness check that the edit landed.

```bash
#!/usr/bin/env bash
# probe-11.sh <worktree> <none|dead|silent> [HAVE_TIMEOUT override]
set -u
ROOT=$1; STAGE=$2
cd "$ROOT" || exit 2
T=tools/run-gates/run-gates.test.sh
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@e GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@e
export GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=false
KIT_REL=tools/run-gates; KITDIR=$ROOT/tools/run-gates; n=0; fail=0
eval "$(sed -n '/^HAVE_TIMEOUT=0; timeout/p' "$T")"
[ -n "${3:-}" ] && HAVE_TIMEOUT=$3
eval "$(sed -n '/^build_hv_repo() {/,/^}/p' "$T")"
case "$STAGE" in
  none)   edit='' ;;
  dead)   edit='s/^  exec 3>&-$/  exec 3>\&-; exit 0/' ;;
  silent) edit='s/^  exec 3>"\$f"/  while :; do sleep 1; done; exec 3>"$f"/' ;;
  *) echo "probe: unknown stage $STAGE"; exit 2 ;;
esac
blk=$(sed -n '/^# 11\. THE MEMORY PAUSE/,/^rm -rf "\$MP"/p' "$T" | sed "$edit")
printf 'probe: staged lines: %s\n' "$(printf '%s\n' "$blk" | grep -c 'exec 3>&-; exit 0\|while :; do sleep 1; done; exec 3')"
t0=$SECONDS
eval "$blk"
echo "probe: stage $STAGE · HAVE_TIMEOUT $HAVE_TIMEOUT · fail=$fail · n=$n · $((SECONDS - t0))s"
```

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `MP_BOUND` | shell variable, read by `run_mp_bar` | none. `lexicon.py --suggest MP_BOUND --as sh.constant` answers that the cell is undeclared, and the declared cells are `js.function`, `py.function`, `py.type` and `sh.function` |
| `$MP/x/serve.err` | fixture file, the server's stderr | none |

No function is minted.

### Files touched (estimate)

- `tools/run-gates/run-gates.test.sh`

The suite is claimed `project-owned` in `tools/run-gates/kit.toml`. The version epoch measures only
`engine`, `seed`, `rendered` and `merged` files (`EPOCH_ROLES`, `tools/govkit/govkit.py:12935`), so
this edit does not move the run-gates version. That is why unit 7's stop on a `run-gates` epoch hit
is not reached from here.

### Alternatives rejected

- `GATE_WALL` on the `ac14` call, the brief's example. The wall cannot reach a main shell blocked in
  an open, as shown above.
- A release watchdog in the arm that opens the FIFO when the server dies. It bounds a dead server
  but not a silent one, and it adds a second writer whose opens are the MSYS behaviour that killed
  the first.
- Respawning a dead server. It hides the death the arm must name.
- Survival without the settle. It leaves 1 to 13 lost answers in 300 reads, and one landing on C14's
  decision reds the arm as `[]`.
- A `kill -0` test before the kill. A child that has exited but not yet been reaped still answers
  `kill -0`, so a just-dead server could read as alive. The status of the arm's own `wait` cannot be
  misread that way.
- Running the half unbounded on a host with no `timeout`. An unbounded read of a FIFO is the defect.

## 5. Acceptance criteria

`$P` is the scratch directory of section 4, and every command runs from the worktree root.

- **AC1** — When `timeout -k 10s 600 bash "$P/probe-serve.sh" "$PWD" "$P/serve1" 300` runs, twice,
  each run prints `probe: 300 of 300 reads carried 10 %, 300 asked · server exit 143`.
  Red when: the server ends on its own before the arm's kill, with exit 0 from a failed open or
  141 from `SIGPIPE`. Over the shipped server this probe printed
  `probe: 1 of 2 reads carried 10 %, 300 asked · server exit 141` on node d on 2026-10-14. Also red
  when a lost answer leaves a read empty.
  cost: about 90 s a run, most of it the 0.2 s settle.
  figure: 300 reads and two runs, PINNED as the probe's own counts.
- **AC2** — When `timeout -k 10s 1800 bash "$P/probe-11.sh" "$PWD" none` runs three times, each
  prints `probe: staged lines: 0`, then a line reading `fail=0`, and no line carrying `AC14`.
  Red when: AC14 holds the probe to its outer bound, as the unstaged slice did over this tree on
  2026-10-14, or the arm reds.
  cost: a few minutes a run on node d, most of it arms 11b to 11f.
- **AC3** — When `timeout -k 10s 1800 bash "$P/probe-11.sh" "$PWD" dead` runs, it prints
  `probe: staged lines: 1` and the line
  `canary: memory pause — AC14 the FIFO server serve.sh died before the run ended (exit 0)` with
  its tail. The seconds in that tail are at most the `inside <N>s` of the AC6 calibration line in the
  same output, plus 15. The summary line reads `fail=1`.
  Red when: the probe runs to its outer `timeout`, so the bound did not reach the blocked open. Also
  red when the red line reports the bar's verdict and not the server.
  figure: N is DERIVED from that run's own calibration line.
- **AC4** — When `timeout -k 10s 1800 bash "$P/probe-11.sh" "$PWD" silent` runs, it prints
  `probe: staged lines: 1` and the line `canary: memory pause — AC14 the nested bar outlived its <N>s bound`
  with exit 124 or 137, and it names `serve.sh` alive. The seconds are at most N plus 15, where N is
  the calibration line's, and the summary reads `fail=1`.
  Red when: the probe runs to its outer bound, or the line calls a live server dead.
- **AC5** — When `timeout -k 10s 1800 bash "$P/probe-11.sh" "$PWD" none 0` runs, it prints the
  SKIP line naming `'timeout -k'`, then a summary reading `fail=0` with the same `n=` as AC2's runs.
  Red when: the half runs a nested bar on a host the probe says has no `timeout`, or the SKIP drops
  the half's count.
- **AC6** — When `git diff --stat ebce889c7 <pass> -- tools/` is read at this unit's pass commit,
  it lists one file, the canary suite. In `git diff ebce889c7 <pass> -- tools/run-gates/`,
  `MP_BOUND` appears only in `run_mp_bar` and on the one `ac14` call. No `n=$((n+1))` line is added,
  and `FLOOR_ASSERTIONS=401` is unchanged.
  Red when: another `run_mp_bar` call is bounded, the `ac14` call is not, the runner itself moves,
  or the floor or count moves.

## 6. Gates

`run-gates canary` · `run-gates gov canary` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `harness arms (fail branches armed or pinned)`

The main loop runs these at the close. `run-gates canary` is the leg this unit unblocks. Its hang was
observed in both canary attempts over `ebce889c7`. The brief's last acceptance, the canary
completing under its 13200 s ceiling in the closing bar, is the main loop's observation and not a
criterion here.

What these legs read of this change. The fork leg's argv excludes `*.test.sh` from its product
population (`tools/gate-legs.json:187-195`), and it still grades this file for the registry classes:
`scan_spawn_tree` adds every tracked `*.test.sh` (`tools/gate-lint/sh_hygiene.py:843-850`), counted
against this file's six rows at `memory/project/spawn-idiom-sites.txt:214-219`. So a counted site
this unit added would red it, and `TOOL-dRedressedBar-10`'s AC5 reads this pass and finds none
added. The loop leg reads the file too, through one registry row
(`memory/project/substitution-fed-loops.txt:45`, one `<<<` reader). No line this unit adds feeds a
`done <<` or `done <<<` reader, so that row does not move. The gov canary reads only the suite's
manifest-derivation lines, which this unit leaves alone. The touched path trips only the broad
`tools/` guard and `tools/run-gates/`, which six legs carry, over `BROAD_LEG_FLOOR` of 5
(`tools/check-spec-tokens.py:262`). So the guard join owes no leg.

New arm: tools/run-gates/run-gates.test.sh · covers AC2 AC3 AC4 AC5 · `probe-11.sh` stages the server's exit after its first answer, or its silence, and arm 11g reds inside its calibrated bound naming `serve.sh` · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-14 · initial draft, from the build's unit-8 brief, the retry's fixture records and
  three scratch probes of the server's loop.
- rev-2 · 2026-10-14 · §3 · Edges, which read `none`, gain the hands-off to TOOL-dRedressedBar-10,
  the batch the round-1 spec audit's minors were promoted into, for report ids 4, 5 and 12. No scope,
  design or criterion moves.
- rev-3 · 2026-10-14 · §3 · §6 · AC6 · a records fix for TOOL-dRedressedBar-10, closing round-1
  report ids 4, 5 and 12, written by that unit's spec-writer pass. The status stays CLOSED, and no
  criterion text moves. Ids 5 and 12: §6 said the fork leg reads none of this suite. It grades the
  suite for the registry classes through `scan_spawn_tree`, against six registry rows, and the
  paragraph now says so. Id 4: AC6 diffs from the build base, so a sibling's `tools/` edit on the
  branch reds it over a correct build. TOOL-dRedressedBar-10's AC4 reads this unit's pass commit
  alone, `<p8>~1..<p8>`. Edges gain the hands-off to `TOOL-dRedressedBar-7`, the mirror of that
  spec's new `consumes-from`.

## 9. Reuse audit

The seam is `run_mp_bar` (`tools/run-gates/run-gates.test.sh:3410-3416`), extended with one
optional bound rather than a second runner call. The bound reuses the suite's `timeout` on nested
bars (`:937`, `:956`, `:969`) and its `HAVE_TIMEOUT` probe and announced SKIP (`:286`, `:299-302`).
Its value is arm 11c's calibrated `_mpwall` (`:3519`). The liveness reading reuses the arm's own
kill-release-wait line (`:3622`). The probes reuse the sourced-not-run slice of
`tools/run-gates/run-gates.turnstile.test.sh:1499-1510` and `TOOL-aMeteredSweep-1` AC5's
section-alone run. `tools/codebase-map/reuse_lookup.py "bound a nested runner that blocks reading a fixture FIFO whose server died"`
ranked generic seams: `read`, `fixture`, `build_fixture`, and `boundedParallel` from the JavaScript
workflows. None of them is nearer than this suite's own helpers. Recall named TOOL-aSiftedFork-7,
which asks for the `HAVE_TIMEOUT` guard on every arm whose subject is bounded execution, and
TOOL-aScannedThrottle-7, a nested bar under `timeout` in the evidence suite. The gotcha
`memory/gotchas/fixture-passes-by-finding-nothing.md` is why both probes print a staged-lines count.
`memory/gotchas/staged-break-substitutes-a-synthetic-value.md` is why the `dead` stage reproduces the
observed shape and not a simpler one.

Recall terms used: `python tools/memory-recall/query.py "how is a nested bar in the canary bounded so a fixture that stops answering reds the arm instead of hanging the leg" --terms "canary nested bar timeout bound FIFO mkfifo serve.sh memory pause forced branch hang MSYS"`
