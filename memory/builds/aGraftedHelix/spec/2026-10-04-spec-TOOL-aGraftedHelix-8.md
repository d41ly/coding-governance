# TOOL-aGraftedHelix-8 — every automatic self-heal appends one line to a health log the orientation card counts

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-1 · base 5266d22e · streams tooling+kickoff · order 9 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-9 |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-9 |

<!-- /gen:spec-records -->

## 1. Goal

Gov repairs its own state in several places, and each repair is reported only on the stdout of the
process that made it: a SessionStart hook nobody reads, a scheduled tick, a bar's stderr. This unit
gives every automatic self-heal one append-only line in `<git-common-dir>/health.log` (interface I3
of the spec brief), and gives the orientation card a `health —` line counting what happened in the
last 24 hours, so a session learns at start that its repository repaired itself.

## 2. Scope (IN)

- **S1** — One shared block per writer language, each with three functions and one constant:
  `derive_health_log <common-dir>` prints `<common-dir>/health.log` and spawns nothing;
  `resolve_health_log <repo-dir>` asks `git -C <repo-dir> rev-parse --path-format=absolute
  --git-common-dir` once and prints the same path, or fails with nothing printed;
  `add_health_event <log> <source> <event> <detail>` appends one I3 line and is the only writer of
  the file. The constant is `HEALTH_LOG_CAP_LINES=500`. The canonical copies are a bash file and a
  Python file under `tools/lib/`, marker stems `health_log_sh` and `health_log_py`, and every writer
  and the card carry the block inline, byte-identical. §4 "The shared block" pins the behaviour.
  Observed by AC1 and AC2.
- **S2** — `tools/lib/resolve-python.test.sh` gains two `PARITY_ROWS` rows, one per stem, and one
  behaviour arm in which both canonicals append to one scratch log and every line matches I3.
  Observed by AC3; the arm's own red on a staged break is observed at the close (§7).
- **S3** — `tools/check-wiring.sh` writes `hookspath-set` where its hooks arm sets an unset
  `core.hooksPath`, and `merge-driver-set` where its merge arm sets an unset `merge.rows.driver`, in
  whichever mode reached the branch, the mode named in the detail. Observed by AC4, both arms, and
  AC5.
- **S4** — `tools/process-monitor/reap.py` writes `tree-killed` once per kill target, after
  `check_survivors` has read the census back, on both non-dry-run paths: the `--kill`/`--kill-msys`
  path in `main` and the loop in `run_sweep`. A dry run reaches neither call. The log is resolved
  once per process from the same `root_dir` the conf is read from. Observed by AC2 and AC5.
- **S5** — The unattended kit carries the shell block once, in `tools/unattended/lib-unattended.sh`,
  which both the driver and `tools/unattended/resume-tick.sh` source. The tick writes `run-resumed`
  after a launch that reported a pid and `resume-failed` on the `launch failed` branch; the driver
  writes `claim-taken-over` where unit 1's claim write takes over a claim whose I2 verdict is
  `stale`. Observed by AC5 and AC6.
- **S6** — `tools/run-gates/run-gates.sh` carries the shell block and writes, through
  `derive_health_log` over the common dir the runner already holds (`TS_COMMON` at the turnstile
  sites, `WORK_COMMON` after them, which falls back to its own resolution with the turnstile off),
  so no site spawns `git`: `beacon-reaped` in
  `ts_try_reap`, `ticket-swept` in `ts_sweep_queue`, `scratch-swept` where a dead bar's scratch is
  swept, `turnstile-expired` where the wait fails open, `retry-passed` for each deferred leg whose
  serial retry passes, and `dispatch-paused` ONCE per bar that paused, beside unit 7's summary line.
  Observed by AC5 and AC6.
- **S7** — `render_card` in `skills/session-kickoff/manifest-check.sh` renders one `health —` line,
  through a new `render_health_cell`, immediately above `recent —`, over a declared
  `HEALTH_WINDOW_S=86400` beside `CARD_CAP_BYTES`. Its forms are §4 "The card line". Observed by
  AC7 and AC8.
- **S8** — Every writer kit whose shipped bytes move has its version bumped once, after its last
  move, in every carrier `tools/check-kit-versions.sh` pairs, and the kickoff manifest's audit stamp
  is renewed because `tools/run-gates/run-gates.sh` and `skills/session-kickoff/manifest-check.sh`
  are on its watch list. Observed by AC9 and AC10.
- **S9** — One sentence in each writer kit's README naming the events it writes and pointing at the
  canonical block's header for I3. NOT OBSERVED: prose, graded by the closing review.

## 3. Non-goals (OUT)

- No alert, notification, stop or refusal. The card line is the only reader, and it counts.
- No change to any self-heal's behaviour or to the stdout or stderr line it already prints; a
  writer gains one call beside that line and nothing else.
- No JavaScript appender: no JavaScript site is IN (§4 Inventory says why each was left out).
- No cross-node view. The log is per clone, under the common dir, never tracked and never pushed;
  which node holds which run is unit 1's remote claim, not this file.
- No backfill of heals that happened before the writers exist.
- No reader in `--status`, `--liveness` or the runlog CLI.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-1` — the driver's take-over of a claim whose verdict is
  `stale`; without it the `claim-taken-over` call has no branch to sit in.
- **consumes-from** `TOOL-aGraftedHelix-7` — the gate runner's per-bar pause summary; without it
  the `dispatch-paused` call has no count to carry.
- **consumes-from** `TOOL-aGraftedHelix-2` — the `claims —` line it adds to the same card in the
  same file; this unit's line goes immediately above `recent —`, so it lands below whatever unit 2
  placed, and the two edits are sequenced by build order.

## 4. Design

### Data model

I3, as the brief pins it, with the choices it left open made here. One line per event, four fields
joined by TAB, LF-terminated, UTF-8:

```
<utc>\t<source>\t<event>\t<detail>
utc     YYYY-MM-DDTHH:MM:SS+00:00, always UTC, always this offset spelling, so lines sort as text
source  ^[a-z][a-z0-9-]*$, the writer: check-wiring, reap, resume-tick, unattended, run-gates
event   ^[a-z][a-z0-9-]*$, one token from the table under Inventory
detail  free text, TAB CR and LF each folded to one space, at most 240 characters
```

The bash stamp is `date -u +%Y-%m-%dT%H:%M:%S+00:00`; the Python stamp is `strftime` with the same
format string over `datetime.now(timezone.utc)`, never `isoformat()`, so the two spellings are one
literal and the behaviour arm can compare them.

**The cap.** When the log holds `HEALTH_LOG_CAP_LINES` (500) lines or more, the appender first
rewrites it to its newest 250 through a temp file and a rename, then appends. The file is therefore
never longer than 500 lines, about 175 KB at the detail cap. 500 is PINNED by this spec, not
measured: it holds several weeks of the event rates the Inventory sites produce on node `a`, and the
card reads 24 hours of it.

### The shared block

Both languages, one contract:

- `add_health_event` never fails its caller. An empty log path, a refused source or event token, or a
  write that fails prints ONE line on stderr starting `health: NOTE -` naming the path and the
  reason, writes nothing, and returns 0 (Python: returns `None`, never raises). A degraded write is
  announced, never silent (`memory/gotchas/degradation-known-but-unreported.md`).
- `resolve_health_log` is the only spawn. A bash writer calls it at most once per run and keeps the
  path it printed in its own variable, because a cache held inside the block would die with the
  command substitution that reads it; the Python copy caches per process. Either way a writer pays
  at most one `git` per run.
- The canonical header states what the block does NOT do: it does not serialize concurrent writers
  (an append of one short line is not torn in practice, and a trim racing an append can lose the
  appended line — `ponytail:` one rename, a lock file if a lost line is ever observed); it does not
  validate a detail's meaning; and it cannot tell a repository where no writer kit is installed from
  one where nothing healed.

The bash block runs under `set -u` without `set -e` and feeds no loop from a command substitution,
which is what every consumer it is inlined into already requires of its own code.

### The card line

`render_health_cell` reads the log through `derive_health_log` over the common dir `--card` already
resolved for `CARD_DIR`, so the card spawns no extra `git`. It computes the window's start as a UTC
stamp of I3's spelling — `date -u -d @<epoch>`, falling back to BSD `date -u -r <epoch>` — compares
stamps as text, and renders exactly one of:

```
health — <n> in the last 24h of <m> logged[ · <source> <event> ×<k>]...[ · +<j> more kinds][ · <u> unreadable]
health — none recorded: no health.log in the git common dir
health — skipped: <why>
```

`<m>` counts every well-formed line in the file and `<n>` those stamped inside the window.
At most four `<source> <event>` pairs, from the window only, by count descending then by name. A line
that is not four fields or whose stamp does not match the I3 pattern is counted `unreadable` and
never as an event. `skipped:` covers a log that exists and cannot be read, and a host whose `date`
computes neither form. The hours figure is `HEALTH_WINDOW_S / 3600`. The line carries no path, id or
sha, so `--card --check` finds no token in it. No time bound is needed: the read is one local file
capped at 500 lines, two `date` calls and one `awk`, with no network and no lock.

It sits ABOVE `recent —` because `CARD_PARTS_AWK` splits a stored card into STARTUP, ending with the
`recent —` block, and TAIL; a line below that block would be filed into the tail an append replaces.

### Inventory

Found by `git grep -nIiE 'self-heal|auto-?(set|fix|heal|repair)|reclaim|relaunch|\bFIXED\b'` over
tracked code outside the suites, then `grep -nE 'reaping|sweeping|retried after timeout|WAIT
EXPIRED|resumed · attempt|launch failed'` over the runners those hits led to, at base `5266d22e`.

| Site | Kit, language | Disposition |
|---|---|---|
| `check_hooks`, unset branch, `FIXED hooks` | check-wiring, sh | IN — `hookspath-set`, detail `core.hooksPath -> .githooks · mode <m>` |
| merge arm, unset branch, `FIXED merge` | check-wiring, sh | IN — `merge-driver-set`, detail `merge.rows.driver · mode <m>` |
| eol arm, `fixed eol` | check-wiring, sh | OUT — runs under `--fix` only, never `--session`, by owner ruling (the aDrainedSluice build's eighth unit, Fork A), so a person asked for it and read its line |
| `check_survivors` callers, both non-dry-run paths | process-monitor, py | IN — `tree-killed`, detail `target <winpid> killed <n> survivors <s> unsignalable <u>` |
| driver `run_orphan_reap` | unattended, sh | OUT as a writer — its kills go through `PROCMON_CMD`, which is `reap.py` here and is logged there; an adopter's own reaper is outside this unit |
| gate runner `run_leg_reap` | run-gates, sh | OUT as a writer — it kills through `reap.py`, logged there |
| tick, launch reported a pid | unattended, sh | IN — `run-resumed`, detail `<slug> attempt <n> session <sid> killed <pid or none>` |
| tick, `launch failed` | unattended, sh | IN — `resume-failed`, detail `<slug> attempt <n> <the launcher's first line>` |
| tick, `ATTEMPTS EXHAUSTED` skip | unattended, sh | OUT — printed on every tick while true, six an hour, and `--liveness` already carries it |
| unit 1, take-over of a `stale` claim | unattended, sh | IN — `claim-taken-over`, detail `<slug> from node <n> session <s> beat-age <a>s` |
| `ts_try_reap`, dead and stalled holder | run-gates, sh | IN — `beacon-reaped`, detail `dead holder pid <p>` or `stalled holder heartbeat <a>s ttl <t>s` |
| `ts_sweep_queue` | run-gates, sh | IN — `ticket-swept`, detail `dead waiter pid <p>` or `stamp <s> past <cutoff>` |
| dead-bar scratch sweep | run-gates, sh | IN — `scratch-swept`, detail `dead bar pid <p>` |
| turnstile `WAIT EXPIRED`, running unqueued | run-gates, sh | IN — `turnstile-expired`, detail `waited <w>s bound <b>s` |
| serial retry, `GATE ok … (retried after timeout)` | run-gates, sh | IN — `retry-passed`, detail `<leg> after a <s>s timeout` (`TOOL-dDerivedDocket-26`) |
| unit 7, per-bar pause summary | run-gates, sh | IN — `dispatch-paused`, ONE per bar, detail = unit 7's summary counts |
| timing-cache fallback | run-gates, sh | OUT — a degradation the runner already announces; nothing is repaired |
| agent-cap slot TTL reclaim | hooks, js | OUT — the budget expiring as designed, on every new prompt turn; nothing was broken |
| `procmon-hook.js` session sweep | process-monitor, js | OUT — `--dry-run`; it reports and kills nothing |
| stall-recorder, stop-guard | unattended, js | OUT — recorders and a blocker writing their own sidecars; nothing is repaired |
| `push-main.sh` re-prepare attempts | push-main, sh | OUT — an in-call retry of a command its caller invoked and reads; the lander marker records the outcome |
| pass commits re-rendering generated indexes | unattended, sh | OUT — generation by design, not repair |

Identifiers this unit mints, each beside the naming cell that grades it (all answered `OK` by
`python tools/lexicon/lexicon.py --suggest <name> --as <cell>` at base):

| Identifier | Cell |
|---|---|
| `add_health_event` | `sh.function`, `py.function` |
| `resolve_health_log` | `sh.function`, `py.function` |
| `derive_health_log` | `sh.function`, `py.function` |
| `render_health_cell` | `sh.function` |
| `HEALTH_LOG_CAP_LINES`, `HEALTH_WINDOW_S` | constants, no cell |
| marker stems `health_log_sh`, `health_log_py` | parity-table keys, no cell |
| the twelve event tokens in the table above | I3 values, no cell |

No gate leg, kit, hook, guide, workflow script or lexicon verb is added, so no inventory key is minted
and the codebase map owes nothing; `<prefix>/lib/` is the registry's standing gov-internal exemption.

### Files touched (estimate)

- `tools/lib/health-log.sh` (new)
- `tools/lib/health_log.py` (new)
- `tools/lib/resolve-python.test.sh`
- `tools/check-wiring.sh`
- `tools/check-wiring.test.sh`
- `tools/process-monitor/reap.py`
- `tools/process-monitor/selftest.py`
- `tools/process-monitor/census.py`
- `tools/process-monitor/classify.py`
- `tools/process-monitor/scope.py`
- `tools/process-monitor/adopt-process-monitor.sh`
- `tools/process-monitor/README.md`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/resume-tick.sh`
- `tools/unattended/resume-tick.test.sh`
- `tools/unattended/README.md`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/README.md`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/guides/SESSION-KICKOFF.md`

The process-monitor `.py` and `adopt-process-monitor.sh` rows are version carriers only. The
unattended kit's other carriers move with its version and trip no guarded leg.

### Alternatives rejected

- **One sourced library under `tools/lib/`.** `<prefix>/lib/` ships nothing, so a copy-installed
  kit cannot source it: measured at base, 65 tracked files carry the `resolve_python` block inline
  and 66 the `resolve_kit_dir` block for exactly that reason.
- **One writer program in one kit that the others invoke.** A kit would name a sibling's path
  (invariant 2), and run-gates installed without process-monitor could not log at all.
- **A hand-written appender per kit.** Two spellings of one format drift; measured at base, the card
  header stamps local time with `%z` while 22 shell lines under `tools/` stamp UTC.
- **Logging `tree-killed` at the two callers rather than in `reap.py`** — see F3.

## 5. Production-readiness checklist

- security — The file lives under the common dir, is never tracked and never pushed. Details carry
  pids, slugs, session ids and leg names, all already on disk in `RUN.md`, the ledgers or the bar's
  logs; no credential reaches a writer. The appender writes only the path its caller resolved.
- perf / scale — One append per heal, at most one `git` per writer process, and a trim once per 250
  events. The card adds two `date` calls and one `awk` over at most 500 lines; AC7 records its cost.
- error / empty / loading states — An unwritable log or a refused token is one `health: NOTE -`
  line and a caller that continues. The card's `none recorded` and `skipped:` forms are §4.
- observability — This unit is the observability: the card line, and the file itself for `grep`.
- risks — A trim racing an append can lose that append (§4). Suites that assert a card's exact
  lines must learn the new one. `reap.py` run from a root outside any repository prints the NOTE on
  stderr, which a self-test arm asserting an empty stderr will see. Check S of `tools/check-wiring.sh`
  reports the installed engine as differing in this worktree once the engine moves, which is that
  arm working; it clears at landing.
- testing — AC1 to AC10 by direct observation in a pass; the suite arms in §7, observed red on a
  staged break at the close.
- migration — None. An absent log is the starting state and renders `none recorded`.
- user docs — S9's README sentences; I3 itself lives in the canonical block's header.

## 6. Acceptance criteria

`$S` below is a scratch repository under `%TEMP%` with a short name, and `$GCD` its absolute git
common dir.

- **AC1** — When the block between `# >>> health_log_sh` and `# <<< health_log_sh` in
  `tools/check-wiring.sh` is sourced and `add_health_event "$GCD/health.log" check-wiring
  hookspath-set "a<TAB>b<LF>c"` runs, the log holds one line of four TAB-separated fields whose
  first matches `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+00:00$` and whose detail
  is `a b c`; an event of `Hooks` writes nothing and prints one `health: NOTE -` line; a log path
  inside a missing directory prints one and the call returns 0.
  Red when: the folded detail still splits the line into five fields, or a refused token is written.
- **AC2** — When `$GCD/health.log` holds 500 numbered lines and `python -c "import sys;
  sys.path.insert(0, 'tools/process-monitor'); import reap; reap.add_health_event(sys.argv[1],
  'reap', 'tree-killed', 'x')" "$GCD/health.log"` runs, the file holds 251 lines, the old lines 251
  to 500 in order and then the new one; the same fixture through AC1's bash call gives the same
  shape, and `awk -F'\t' 'NF != 4'` over a log both languages appended to prints nothing.
  A second fixture of 499 lines holds 500 after one append, with no trim. The Python copy's three
  failure paths each return `None`, print one `health: NOTE -` line on stderr and raise nothing:
  `reap.add_health_event('', 'reap', 'tree-killed', 'x')`, the same call with the event `Bad`, and
  a log path inside a missing directory.
  Red when: the trim keeps the oldest half, or fires at 499 or 501 lines, or the Python stamp is
  spelled `Z` and AC1's pattern refuses it, or a Python failure path raises, which turns a
  completed kill into a traceback.
  figure: 499, 500, 250 and 251 are PINNED by `HEALTH_LOG_CAP_LINES`.
- **AC3** — When `awk '/^# >>> health_log_sh/,/^# <<< health_log_sh/' <file> | tr -d '\r' | cksum`
  runs over every file `git grep -l '^# >>> health_log_sh'` lists, one checksum prints; the same
  holds for `health_log_py`; and the two lists name the canonical, every IN writer's file and the
  card engine.
  Red when: one inline copy differs from the canonical by a byte.
- **AC4** — When `bash tools/check-wiring.sh --session` runs in `$S`, which tracks a
  `.githooks/pre-commit` and a copy of the checker at its own relative path and has no
  `core.hooksPath`, it prints its `FIXED    hooks` line and `$GCD/health.log` gains one line whose
  second and third fields are `check-wiring` and `hookspath-set`; a second run prints `ok       hooks`
  and adds no line. The same holds for the merge arm: with `merge.rows.driver` unset, the first
  `--session` appends one `merge-driver-set` line and a second run appends none.
  Red when: either call sits outside the branch that ran `git config`, so the second run writes
  too and the card counts a self-heal on every SessionStart.
  fixture: built per run; the tree holds none today.
- **AC5** — When `git grep -nE 'add_health_event' -- tools/check-wiring.sh tools/process-monitor/
  tools/unattended/ tools/run-gates/` runs, the call lines name `hookspath-set` and
  `merge-driver-set` in the checker, `tree-killed` twice in `reap.py`, each after a `check_survivors`
  call in its function, `run-resumed` and `resume-failed` in `resume-tick.sh`, and `beacon-reaped`,
  `ticket-swept`, `scratch-swept`, `turnstile-expired` and `retry-passed` in the gate runner. This
  criterion proves PRESENCE only. Placement is proved by a behaviour arm per site in §7: AC4 for
  the two checker sites, the process-monitor arm for `tree-killed`, the resume-tick arm for the two
  tick events, and the turnstile and canary arms for the five gate-runner events.
  Red when: a site §4 marks IN carries no call, or a `tree-killed` call precedes the read-back.
- **AC6** — When the same `git grep -nE 'add_health_event'` runs after units 1 and 7 are built on
  the run branch, it also names `claim-taken-over` in the driver's stale-claim take-over and
  `dispatch-paused` exactly once in the gate runner, outside the per-pause path.
  Red when: `dispatch-paused` is written once per pause, so one pressured bar writes dozens of lines.
  fixture: both sites exist only after `TOOL-aGraftedHelix-1` and `TOOL-aGraftedHelix-7` are built;
  a parked sibling takes its row out of this criterion with a §9 line.
- **AC7** — When `bash skills/session-kickoff/manifest-check.sh --card --write --session t8` runs in
  `$S` holding a copy of the engine and a `$GCD/health.log` seeded with a `check-wiring
  hookspath-set` line and a `run-gates retry-passed` line stamped an hour ago, one line stamped 30
  hours ago and one line of three fields, the card carries, on the line directly above `recent —`,
  `health — 2 in the last 24h of 3 logged · check-wiring hookspath-set ×1 · run-gates retry-passed ×1 · 1 unreadable`.
  Red when: the 30-hour line is counted inside the window, the three-field line counts as an event,
  or the line lands below the `recent —` block.
  cost: the card's wall time with and without the line, read on node `a` in the pass and recorded
  in the acceptance ledger as a PINNED figure.
- **AC8** — When the same command runs in `$S` with no `$GCD/health.log`, the line reads
  `health — none recorded: no health.log in the git common dir`, on the same line position as AC7's.
  Red when: an absent log renders `0 in the last 24h`, a probe reporting a zero it never measured.
- **AC9** — When `python tools/govkit/govkit.py epoch --base <the pass's base>` runs at the pass's
  commit, it names none of `kickoff-manifest`, `check-wiring`, `process-monitor`, `unattended` and
  `run-gates`.
  Red when: a writer kit's shipped bytes moved and its version did not.
- **AC10** — When `bash skills/session-kickoff/manifest-check.sh` runs at the pass's commit, it
  prints no `MANIFEST check 5 FAILED` line.
  Red when: a watched file moved and the audit stamp was not renewed.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `transition-audit arms` · `straggler-guard arms` · `process-monitor census selftest` · `process-monitor adopter selftest` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `check-wiring self-test` · `run-gates turnstile` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kickoff-manifest ratchet` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

The close runs these once; no pass runs a suite. The unattended kit's suites are off the bar and run
on demand through its own runner, so the resume-tick arm below is owed to that run at VERIFYING.

New arm: tools/lib/resolve-python.test.sh · PARITY_ROWS rows health_log_sh and health_log_py; stage one copy's trim count edited · none
New arm: tools/lib/resolve-python.test.sh · both canonicals append to one scratch log; stage the Python stamp spelled Z · none
New arm: tools/check-wiring.test.sh · --session over an unset core.hooksPath appends one hookspath-set line; stage the call moved to the ok branch · none
New arm: tools/check-wiring.test.sh · --session over an unset merge.rows.driver appends one merge-driver-set line and a second run none; stage the call moved to the ok branch · none
New arm: tools/run-gates/run-gates.turnstile.test.sh · the dead-waiter queue fixture appends one ticket-swept line, the expired wait one turnstile-expired line, and the dead bar's scratch one scratch-swept line; stage each call moved off its branch · none
New arm: tools/process-monitor/selftest.py · the Python appender's empty path, refused event and missing directory each return None with one NOTE line; stage the guard removed so the call raises · none
New arm: tools/lib/resolve-python.test.sh · the 499-line fixture holds 500 after one append; stage the trim threshold lowered by one · none
New arm: tools/process-monitor/selftest.py · its real-kill fixture appends one tree-killed line, its dry-run sweep none; stage the call moved into the dry-run branch · none
New arm: tools/unattended/resume-tick.test.sh · the STALE relaunch fixture appends one run-resumed line, the no-pid launch one resume-failed; stage the call moved above the pid check · none
New arm: tools/run-gates/run-gates.turnstile.test.sh · the dead-holder fixture appends one beacon-reaped line; stage the call commented out · none
New arm: tools/run-gates/run-gates.test.sh · the deferred-retry fixture appends one retry-passed line; stage the call moved to the FAIL branch · none
New arm: skills/session-kickoff/manifest-check.test.sh · AC7's seeded log and AC8's absent one; stage the window compare reversed · none

## 8. Open questions

- **F1 — Does the card count since the previous card, or over a declared window?** Since-previous
  shows each event once across all cards; the window shows every session the same 24 hours.
  RESOLVED (agent, 2026-10-04, delegated): a declared window, `HEALTH_WINDOW_S=86400`. Cards are
  per session and sessions overlap, so "previous" is whichever card some other session wrote,
  possibly seconds earlier and never read; an event would then reach only that card. The window is
  the option that satisfies the goal for every card, and it needs no read of another session's file.
- **F2 — Is the log bounded by rotating to a second file, or by trimming in place?** RESOLVED
  (agent, 2026-10-04, delegated): trim in place to the newest half. One file means the reader reads
  one path and the name is spelled once, inside the shared block; rotation would put the second
  file's suffix in the card outside the block. Both lose a line to a racing writer; neither needs a
  lock at this rate.
- **F3 — Does `reap.py` log its own kills, or do its automatic callers?** RESOLVED (agent,
  2026-10-04, delegated): `reap.py`, after the read-back. Every kill in this repository routes
  through it, so one site covers the gate runner's teardown and the driver's orphan reap, and the
  logged count is the read-back's, not the signal's. The cost: a person's explicit `--kill` is logged
  too, and the detail does not say who asked.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 8 section and the writers at base
  `5266d22e`.
- rev-2 · 2026-10-04 · §6 §7 · S1 S3 · AC2 AC4 AC5 · folded the round-1 spec audit's findings on
  this unit: 24 (AC2 observes the Python copy's three failure paths); 25 (AC4 extends to the merge
  arm, AC5 says it proves presence only and names each site's placement arm, and §7 gains the
  merge, ticket, wait and scratch arms); and 26 (AC2's 499-line fixture, the side of the
  threshold a 500-line fixture cannot see).
- rev-3 · 2026-10-05 · §4 · the shared block · the bash copy keeps no cache: every bash writer reads
  `resolve_health_log` through a command substitution, a subshell whose variables die with it, so a
  cache inside the block could never hit; each bash writer holds the path in its own variable
  instead, which keeps the one-`git`-per-run bound. Read at the run branch's tip, after units 1, 2
  and 7 were built.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "append an event line to a shared log under the git
common dir that a session start card reads"` ranked name-stem neighbours and printed `unscanned
layers: .sh`, so the shell half was read from source. Two seams are extended. The inline-copy parity
table `PARITY_ROWS` in `tools/lib/resolve-python.test.sh` is how this repository gives copy-installed
kits shared code, and it already grades a stem whose copies are both shell and Python. The card's
cell sequence in `render_card` is where the line goes, after the `live —` cell's precedent of reading
an optional file and saying `skipped:` without it. The probe's neighbour `log_path` in
`tools/memory-recall/query.py` led to `common_git_dir` beside it, which resolves the common dir the
way `resolve_health_log` will and is a sibling kit's, so its shape is copied and not called. Its JavaScript neighbour `writeSidecarLine` in
`tools/unattended/run-lease.js` is the append-only sidecar precedent; no JavaScript writer is in
scope. Where the probe and source disagreed: nothing it ranked is a writer of any repair line, so
the Inventory came from the greps in §4, not from it. The recall probe returned `TOOL-aWireWarden-1`
and its spec's owner ruling that `--session` auto-fixes an unset `core.hooksPath`, and the
aDrainedSluice ruling that the eol rewrite stays under `--fix`, which is why §4 marks that site OUT.

Recall terms used: self-heal auto-set hooksPath check-wiring session reap orphan resume-tick relaunch orientation card degradation unreported

The question passed with them: "where should an automatic self-heal such as core.hooksPath auto-set or a reaped process be recorded so a later session sees it".
