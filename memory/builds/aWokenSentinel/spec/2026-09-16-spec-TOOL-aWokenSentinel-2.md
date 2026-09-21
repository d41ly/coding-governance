# TOOL-aWokenSentinel-2 — `--liveness <slug>`, the one machine-readable predicate every out-of-session reader shares

**Status:** CLOSED · rev-5 · 2026-09-21 · node a · Tier-2 · base 5f9648d6 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md](../build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md) | research | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 |
| [2026-09-16-build-TOOL-aWokenSentinel-2-1-acceptance-ledger.md](../build/2026-09-16-build-TOOL-aWokenSentinel-2-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 |
| [2026-09-16-prompt-TOOL-aWokenSentinel-2-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-2-1-build-brief.md) | journal | — |
| [2026-09-21-prompt-TOOL-aWokenSentinel-5-2-fold-brief.md](../prompts/2026-09-21-prompt-TOOL-aWokenSentinel-5-2-fold-brief.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-12 |
| [2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |

<!-- /gen:spec-records -->

## 1. Goal

"Is this run alive" has no single answer today: `--status` prints prose for a human, `--audit`
grades dispatched UNITS and says nothing about the session holding the run, and only `--preflight`
knows that a `LANDING` record whose witness is already on the default branch is a finished run
missing a stamp. Six non-terminal records with CLOSED READMEs exist at base, so a reader keyed on
`phase:` alone fires on all six forever. `tools/unattended/unattended.sh` gains a read-only verb,
`--liveness <slug>`, that prints `key: value` lines and one of five verdicts, and the stop-guard,
the stall-recorder's reader and the resume tick all call it rather than each deciding for
themselves. Tier 2: a new verb is a change to the kit's contract.

## 2. Scope (IN)

- **S1** — `--liveness` joins `VERBS_SLUG`, the driver's header lines and the dispatch `case`,
  with a bullet in `tools/unattended/VERBS.template.md`, one invocation in
  `tools/unattended/SKILL.template.md`, and both renders re-made in the same commit — the three
  carriers check 26 of the kit gate joins. Observed by AC1 and AC9.
- **S2** — The verb prints, in this order and nothing else on stdout: `phase`, `state`,
  `default-branch`, `session`, `pid`, `keepalive`, `pid-alive`, `last-move`, `last-move-source`,
  `transcript`, `last-stall`, `stale`, `verdict` — section 4's step order, which AC2 cites. Each
  value's vocabulary is section 4's. It exits 0 on any run-state file whose probes answer; a dead
  probe is the check-52 refusal of S8, exit 1 with no verdict line. Observed by AC2 to AC7.
- **S3** — `state` is one of `terminal`, `finished-unstamped` and `live`, where
  `finished-unstamped` is the OFFLINE half of `check_single_live`'s predicate: phase `LANDING` and
  a sha-shaped witness that is an ancestor of the local default branch's ref, no network.
  Observed by AC2 and AC3.
- **S4** — `last-move` is the seconds since the NEWEST of four signals: the last commit, the
  newest dirty or untracked path's mtime, the newest file under `<git-dir>/gate-logs/`, and the
  session transcript when its path derives. The first two are `print_audit`'s clocks at
  `tools/unattended/unattended.sh:3013` to `:3025`, EXTRACTED into `read_tree_clocks`, which both
  verbs call; neither keeps a copy. Observed by AC5 and AC8.
- **S5** — `RESUME_STALE_BOUND` is read through `read_bound_key` beside its three siblings
  `GATE_BOUND`, `UNIT_STALL_BOUND` and `REVIEW_ROUNDS`, the fourth caller, with its default
  DERIVED in the driver from the two DECLARED bounds already resolved — `GATE_BOUND +
  UNIT_STALL_BOUND` — never from the kit defaults; declared in `.unattended.conf` and
  `tools/unattended/.unattended.conf.example` with its reason, listed in `optional_keys` of
  `tools/unattended/kit.toml`, and rowed in section 8's key table of
  `tools/unattended/PROTOCOL.template.md`; each of the four carriers read by a criterion. A
  declared value below that sum is announced on stderr, because under it the driver's own bar
  reads dead. Observed by AC6.
- **S6** — `pid-alive` is `yes`, `no` or `unknown`, probed by `tasklist` under MSYS and `kill -0`
  elsewhere, `unknown` when the fact is `absent`, non-numeric, or the probe tool is missing; from
  rev-5 `no` also when something holds the pid and the record's `pid-image` (unit 1) does not
  match it, `absent` or no image matching anything. Observed by AC4 and AC11.
- **S7** — `last-stall` is the last line of `<git-dir>/unattended/stall.<slug>.log` when that
  file exists, else `none`; this unit only READS it. Observed by AC7.
- **S8** — Two refusals under one new `fail` number, each with an arm: no run-state file; a clock
  or mtime probe that answers nothing. The driver's own header states what the verb does NOT
  check. Observed by AC1 and AC8.
- **S9** — The `.unattended.conf` edit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`
  in the same commit with a delta line in the subject. Observed by AC10.
- **S10** — The record obligations: this spec to CLOSED in the pass commit; the acceptance ledger
  at `memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-2-1-acceptance-ledger.md`
  with one row per criterion; `--dispatch` declares the write set section 4 lists. Observed by
  AC10.

## 3. Non-goals (OUT)

- **What the verb does not know, stated in its own header.** It cannot see what the session is
  doing, whether a process is hung on a tool call, or which command it is sitting on. `pid-alive`
  says a process EXISTS; a hung `claude.exe` is alive by this probe. The process-side question is
  the process-monitor kit's, named by kit name and never by path, because a kit file names nothing
  outside itself by literal.
- **No action.** It reads and prints. Refusing a stop, recording a stall, killing a tree and
  resuming are units 3, 4 and 5, each of which reads this verb's `verdict` line.
- **No network.** `finished-unstamped` uses the local ref for the default branch; the preflight
  predicate's online half stays where it is at `:1372` to `:1392`. A run whose landing was pushed
  from another tree and not yet fetched here reads `live` — a false `live` from a stale fetch
  costs one unneeded resume attempt, whereas an `ls-remote` per tick per run is a network call from
  a scheduler.
- **No writer of `stall.<slug>.log`.** Unit 4's hook writes it; this verb prints its last line
  verbatim and interprets nothing.
- **No `--status` change.** `--status` gains lines in units 5 and 7.
- **No kit version bump, no `ARMS_FLOORS` raise.** The closing pass bumps unattended 1.24 to 1.25
  once. `python3 tools/memory-tree/check-arms.py --report` at base reads the driver as
  `branches 201 (floor 104)   armed 194 (floor 101)`; two more branches, both armed, leave both
  floors slack.
- **No dossier edit.** `memory/map/features/unattended.md` sits at 20387 of 20480 bytes, PINNED
  2026-09-16; unit 6 refreshes its prose for the whole build. This unit mints no key the map
  enumerates — a verb and a conf key are not key classes of `map_extractors.py`.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-1` — the `session:` and `pid:` facts and their `absent`
  literal. Without it every record reads `session: absent` and every verdict is `UNBOUND`, which is
  the correct answer for a record nothing can bind to and the wrong one for every live run.
- **consumes-from** external — `tasklist` on MSYS and `kill -0` elsewhere as the process-existence
  probe; `ps`'s `WINPID` column under MSYS for the fixture only. All three measured on node `a` on
  2026-09-16 (section 4, "pid-alive").
- **hands-off** `TOOL-aWokenSentinel-3` — calling `--liveness` from the hook and acting on
  `TERMINAL`, `FINISHED-UNSTAMPED` and the rest.
- **hands-off** `TOOL-aWokenSentinel-4` — writing `stall.<slug>.log`; this unit's AC7 fixture
  writes one line by hand, and unit 4's own arm observes the reader over a line its hook wrote.
- **hands-off** `TOOL-aWokenSentinel-5` — keying the tick on `verdict: STALE` and on `pid-alive`.
- **hands-off** `TOOL-aWokenSentinel-6` — the Skill prose for who runs the verb and when; this
  unit ships the one invocation line check 26 demands and nothing more.
- **hands-off** `TOOL-aWokenSentinel-7` — the sidecar root's derivation, `<git-dir>/unattended/`,
  which `--landed` reuses to find the stop log; this unit derives it once for the stall log.
- **hands-off** `TOOL-aWokenSentinel-5` — reading `resume.<slug>.log` through the same
  `resolve_sidecar_dir`, never an inline `rev-parse`.
- **hands-off** `TOOL-aWokenSentinel-11` — the kit-gate check that the driver, the lib and the
  tick together hold exactly one code-line `rev-parse --git-dir`, this function's, so the
  one-derivation rule AC7 states for this unit's own pass binds every later unit on the bar.
- **hands-off** `TOOL-aWokenSentinel-20` — moving `resolve_sidecar_dir` verbatim from the driver
  into `lib-unattended.sh` one order later, so the tick calls the same function through the lib it
  sources; this unit defines it in the driver, where AC7 counts it, and unit 20 changes its home
  and nothing it prints.
- **hands-off** external — the kit version bump, the closing pass's, once.

## 4. Design

### The verb, in the driver (S1, S2, S8)

`--liveness` joins `VERBS_SLUG` at `tools/unattended/unattended.sh:88`, gains the header line
`#   unattended.sh --liveness <slug>   # key: value lines and ONE verdict, for an out-of-session reader`
after the `--audit` line at `:9` so `usage` renders it, and an arm
`--liveness) print_liveness "$SLUG" ;;` in the dispatch `case` at `:5321`. The function is named
`print_liveness` for the reason `print_audit` was: `print` is the declared verb for writing to
stdout for a reader, and `python tools/lexicon/lexicon.py --suggest print_liveness --as sh.function`
answers OK on 2026-09-16, so the lexicon offender pin does not move.

The header comment above the function states what it does not check, in the words of section 3's
first bullet. Body, in order:

1. `check_slug`, `rel=$(runmd_of "$slug")`. No file: `fail 52` — the next free number after
   the driver's high-water of 51, DERIVED by `grep -oE 'fail [0-9]+'` at base — with the sentence
   `no run-state file, so there is no run whose liveness can be graded: <rel>`.
2. `phase` — `fact "$rel" phase`, or `absent`.
3. `state` — `terminal` when `is_terminal` at `:613` says so; else `finished-unstamped` when the
   phase is `LANDING`, the witness is sha-shaped by the same seven-hex `case` the preflight
   predicate uses at `:1381`, resolves as a commit, and `GIT merge-base --is-ancestor <witness>
   <ref>` where `<ref>` is `refs/remotes/origin/<d>` when that ref exists and `refs/heads/<d>`
   otherwise, `<d>` from `default_branch` at `:876`; else `live`. When `default_branch` fails the
   test is not run and `state` is `live`.
4. `default-branch` — the ref the test used, or `unresolved` when `default_branch` failed, so a
   skipped test is announced rather than read as `live`.
5. `session`, `pid`, `keepalive` — each `fact` value, or `absent` when the key is missing or empty.
6. `pid-alive` — section "pid-alive" below.
7. `read_tree_clocks` — section "The clocks" below — then the two further signals, and
   `last-move` = now minus the newest; `last-move-source` names it: `commit`, `write`, `gate-log`
   or `transcript`.
8. `transcript` — the path when it derives and exists, else `absent`.
9. `last-stall` — `tail -n 1` of `<sidecar>/stall.<slug>.log` when the file exists and is
   non-empty, else `none`, where `<sidecar>` is what `resolve_sidecar_dir` prints:
   `$(GIT rev-parse --git-dir)/unattended` — the WORKTREE's git dir, where `gate-logs/` already
   lives, never the common dir, because a run lives in one worktree. One function, so unit 7's
   `--landed` reads the stop log from the same root by calling it rather than respelling it; an
   empty `rev-parse` answer is a dead probe under the rule below, never a path composed from an
   empty root.
10. `stale` — `yes` when `last-move` exceeds `RESUME_STALE_BOUND`, else `no`.
11. `verdict` — the first that holds: `TERMINAL` (state terminal), `FINISHED-UNSTAMPED`,
    `UNBOUND` (session `absent`), `STALE` (stale yes), `LIVE`.

A dead probe — `date`, `git log`, `stat` on an existing path, or `read_tree_clocks` reporting
one — is the second `fail 52` branch: `the liveness cannot be measured on this node, because a
probe it needs answered nothing, so no verdict is answerable and a zero from a dead probe would
read as moved-just-now: <probe>`, exit 1, and no `verdict` line prints. The brief said "nothing
else refuses"; that sentence is kept for the RECORD — a terminal phase, an absent session, an
unresolvable default branch are all values, never refusals — and not for the node, because
the charter's section 7 requires a probe that cannot move to say so and `--audit` already refuses
the same way at its check 51.

Every key prints on every run that reaches the verdict, including a terminal record, so a reader
never has to know which keys a state omits. Output is stdout only; the `read_bound_key` NOTE for
an undeclared bound goes to stderr as its siblings' do.

### The clocks (S4)

`print_audit`'s block from `now=$(date -u +%s ...)` at `:3013` through the `done <<<"$dirty"` at
`:3025` moves verbatim into `read_tree_clocks`, which sets four globals: `TC_NOW`, `TC_LASTC`
(HEAD's committer epoch), `TC_LASTW` (newest mtime over `scan_dirty_paths`, empty for a clean
tree) and `TC_DEAD` (the probe that answered nothing, or empty). `print_audit` calls it and reads
the globals where it read its locals; its verdict arithmetic and its dead-probe refusal are
unchanged. `read` is a declared verb and the lexicon answers OK for the name.

`print_liveness` adds two signals after the call. The gate-log clock: when `<git-dir>/gate-logs/`
exists, the newest mtime over its files by `stat -c %Y`, each answered-nothing a `TC_DEAD`
equivalent; an absent directory contributes nothing and is not a dead probe, because a repo that
has never run the bar has none. The transcript clock: the mtime of the file `resolve_transcript_path`
returns, when it returns one. `last-move` is `TC_NOW` minus the maximum of the signals present; a
clean tree with no gate logs and no transcript reads from the commit alone. This is the research's
guard, "liveness from what moves during a healthy silence": during a 26-minute bar neither the
transcript nor the last commit moves, and the per-leg logs do.

### The transcript path

`resolve_transcript_path <session>` derives `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/projects/<enc>/<session>.jsonl`
where `<enc>` is the worktree root from `GIT rev-parse --show-toplevel`, in its native spelling on
Windows, with every `:`, `\`, `/` and `.` replaced by `-`. Measured on node `a` on 2026-09-16:
`C:\projects\coding-governance\.claude\worktrees\eloquent-pasteur-e7ecb5` is stored as
`C--projects-coding-governance--claude-worktrees-eloquent-pasteur-e7ecb5`, so `.` IS replaced —
the brief listed three characters and this corrects it to four. Whether `_` is replaced is
UNVERIFIED: no project on the node has one. When `<session>` is `absent`, the encoded directory
does not exist, or the file does not exist, the function returns nothing and `transcript: absent`
prints; the three tree signals decide. A session that opened at the worktrees' PARENT rather than
the root reads `absent` too, which is a signal lost, not a wrong one. `CLAUDE_CONFIG_DIR` is the
CLI's documented override; that this harness sets it is UNVERIFIED — it is not in this session's
environment on node `a` — and the default is `$HOME/.claude`. Honouring it costs one expansion and
is also the fixture's seam: the arms point it at a scratch directory rather than moving `HOME`.

### pid-alive (S6)

`check_pid_alive <pid> [image]` prints `yes`, `no` or `unknown`; from rev-5 it lives in
`lib-unattended.sh` over `read_pid_image`, which prints the image holding a pid and returns 0 held,
1 nobody, 2 the probe answered nothing — the driver's `write_lease` records the image through it,
`--liveness` passes the record's `pid-image` fact here, and the resume tick probes the pid it
launched through the same function. A recorded image that is not the one holding the pid is `no`:
a reboot recycles the number, and a tree kill aimed at it lands on the owner's next process
(closing review id 2). `absent`, or none, matches anything — the pid-only reading every earlier
lease had. `absent` or a value with a non-digit is `unknown`. Under `uname -s` matching `MINGW*|MSYS*|CYGWIN*`: `tasklist //FI "PID eq <pid>" //NH`,
`unknown` when `tasklist` is not on `PATH` or exits non-zero — a tool that answered nothing is not a
`no` — and otherwise `yes` when its output carries ` <pid> ` as a whole field, `no` when it does not.
Elsewhere: `kill -0 <pid>` exit 0 is `yes`, else `no`. Measured on node `a` on
2026-09-16: `tasklist` prints the process row for the live `claude.exe` that `CLAUDE_PID` names
and an `INFO: No tasks are running` line for a dead pid, exit 0 in BOTH cases, so the exit code
decides nothing and the output must be read; `kill -0` on that same live Windows pid reports
`No such process` under MSYS, so `kill -0` alone would read every live run on this fleet as dead,
which is why the MSYS arm exists. The recorded pid is `claude.exe`'s Windows pid, which is the
one `tasklist` knows.

### The bound (S5)

After BOTH existing reads — `GATE_BOUND` at `:369` and `UNIT_STALL_BOUND` at `:370`, which
resolve the declared or defaulted values into their variables — two lines:
`RESUME_STALE_BOUND_DEFAULT=$((GATE_BOUND + UNIT_STALL_BOUND))` and
`read_bound_key RESUME_STALE_BOUND "$RESUME_STALE_BOUND_DEFAULT" seconds "a run reads STALE after the derived default of ${RESUME_STALE_BOUND_DEFAULT}s (GATE_BOUND + UNIT_STALL_BOUND) with no signal moved"`,
with `RESUME_STALE_BOUND=""` added to the empty-initialisation line at `:339`. No literal at `:256`
and no retyped `1800`: the default derives from the DECLARED bounds, so an adopter who raises
`GATE_BOUND` for a longer bar — the conf's own documented remedy — raises this default with it,
and the two-numbers class the driver's `REVIEW_ROUNDS_DEFAULT` comment records is not re-entered.
5400 at base with the kit defaults, DERIVED: `GATE_BOUND` is the longest a bounded command may run
and a healthy bar is silence on every signal but the gate logs, so the stale bound sits one
`UNIT_STALL_BOUND` above it. After the read, one more line: when the resolved `RESUME_STALE_BOUND`
is below `GATE_BOUND + UNIT_STALL_BOUND`, stderr carries
`unattended: NOTE - RESUME_STALE_BOUND (<n>s) is below GATE_BOUND + UNIT_STALL_BOUND (<sum>s), so a
full bar's silence reads STALE and an out-of-process resumer may kill a healthy bar` — a NOTE and
not a refusal, because a declared bound is the adopter's to lower and the driver's job is to say
what it costs. The conf declaration carries the derivation sentence as its reason, the example
mirrors it, `optional_keys` gains the key, and the protocol's section 8 key table gains a row on
`UNIT_STALL_BOUND`'s terms.

### The carriers (S1)

- `tools/unattended/VERBS.template.md`, after the `--audit` bullet:
  `- \`--liveness\` — key: value lines and one verdict for an OUT-OF-SESSION reader: the phase, the
  lease, whether the recorded pid exists, seconds since anything moved, the last recorded stall,
  and TERMINAL, FINISHED-UNSTAMPED, UNBOUND, STALE or LIVE. Read-only; the stop-guard, the
  stall-recorder's readers and the resume tick call it rather than deciding for themselves. It
  cannot see what the session is doing or whether a process is hung — existence is not progress.`
- `tools/unattended/SKILL.template.md`, in `## While it runs`: one sentence and one fenced
  `bash {{KIT_DIR}}/unattended.sh --liveness <slug>` — the verb every out-of-session reader
  shares; who reads it and when is unit 6's prose. Check 26 needs the substring
  `unattended.sh --liveness ` in the template; this is that and no more.
- Both renders through `bash tools/unattended/adopt-unattended.sh`.

### The fixture

The suite's `mkconf` gains an EIGHTH positional, `RESUME_STALE_BOUND="${8-5400}"`, so every
existing fixture declares the key at the kit default and no existing arm sees a NOTE it did not see
at base — the sixth and seventh positionals' precedent. The unit's arms, in a new block after unit
1's:

1. `build_audit_fixture`; `mutate` phase to `LANDED`; `run --liveness tRun` → `verdict: TERMINAL`.
2. `build_audit_fixture`; `mutate` phase to `LANDING` and witness to `$BASE`, a commit on the
   fixture's `main`; `run --liveness tRun` → `state: finished-unstamped`,
   `default-branch: refs/remotes/origin/main`, `verdict: FINISHED-UNSTAMPED`; then witness to the
   unit branch's HEAD → `state: live`.
3. `build_audit_fixture`; `mutate` session to `absent` → `verdict: UNBOUND`.
4. `build_audit_fixture`; `mutate` pid to `999999999` → `pid-alive: no`; under MSYS start
   `sleep 60 &`, take `ps`'s `WINPID` for `$!`, elsewhere `$!` itself, `mutate` pid to it →
   `pid-alive: yes`; kill the sleep. Measured 2026-09-16: `ps` reports a background sleep's
   `WINPID`, `tasklist` lists it while alive and not after `kill`.
5. `build_audit_fixture`; `mkconf "true" "true" "" "3600" "" "1800" "7" "60"`; commit with
   `GIT_COMMITTER_DATE` an hour old over a clean tree → `stale: yes`, `verdict: STALE`,
   `last-move-source: commit`; then `mkdir -p "$(git rev-parse --git-dir)/gate-logs"` and `touch`
   one file there → `stale: no`, `verdict: LIVE`, `last-move-source: gate-log`.
6. On the STALE fixture, `CLAUDE_CONFIG_DIR=$ORIGIN_DIR/cfg` with the encoded directory under its
   `projects/` and a `fixture-session.jsonl` touched there → `transcript: <that path>`,
   `last-move-source: transcript`, `verdict: LIVE`; `CLAUDE_CONFIG_DIR` pointing at an empty
   directory → `transcript: absent`. The override and not `HOME`, because `HOME` is also where git
   reads its global config and moving it changes what every `GIT` call in the driver sees. OUTSIDE
   the fixture tree, under the suite's `$ORIGIN_DIR` rather than `$TMP`: `$TMP` IS the fixture's
   work tree, so a config directory under it is an untracked WRITE with the transcript's own mtime,
   and `write` wins the source line on the tie — measured on the block's first run, 2026-09-20.
7. `printf '2026-09-16T00:00:00Z fixture-session rate_limit {}\n' > "$(git rev-parse
   --git-dir)/unattended/stall.tRun.log"` → `last-stall:` carries that line; removed → `none`.
8. `run --liveness tNoRun` → the first `fail 52` sentence, exit 1; the `stat` stub of the audit
   arms over a dirty tree → the second, exit 1, and no `verdict:` line.
9. The `NOCONF` heredoc → stderr carries `declares no RESUME_STALE_BOUND`; `"abc"` in the eighth
   positional → `REFUSING - RESUME_STALE_BOUND is declared as`, exit 2.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `--liveness` | slug verb | the driver's `VERBS_SLUG`; check 26 joins it |
| `print_liveness` | shell function | `sh.function`, verb `print` |
| `read_tree_clocks` | shell function | `sh.function`, verb `read` |
| `resolve_transcript_path` | shell function | `sh.function`, verb `resolve` |
| `check_pid_alive` | shell function, in `lib-unattended.sh` from rev-5 (moved from the driver), beside `read_pid_image` | `sh.function`, verb `check` |
| `resolve_sidecar_dir` | shell function | `sh.function`, verb `resolve` |
| `RESUME_STALE_BOUND` | conf key | `read_bound_key`; not a naming cell |
| `TC_NOW`, `TC_LASTC`, `TC_LASTW`, `TC_DEAD` | shell globals | the driver's upper-case convention for shared state |

### Rollout

The pass declares, through `--dispatch --writes`: `tools/unattended/unattended.sh`,
`tools/unattended/unattended.test.sh`, `tools/unattended/VERBS.template.md`,
`memory/guides/UNATTENDED-VERBS.md`, `tools/unattended/SKILL.template.md`,
`.claude/skills/unattended/SKILL.md`, `tools/unattended/PROTOCOL.template.md`,
`memory/guides/UNATTENDED-PROTOCOL.md`, `.unattended.conf`,
`tools/unattended/.unattended.conf.example`, `tools/unattended/kit.toml`,
`memory/guides/SESSION-KICKOFF.md`, this spec, the build README, the acceptance ledger S10
names, and the generated `memory/LIVE.md` and `memory/ledger/2026-09.md`. Five of those are unit
1's too, which is why the roster sequences this unit second; the pass does not begin until unit 1's
commit is in `HEAD`.

Forward-compatible: a record with no `session:` reads `UNBOUND`, a conf with no bound takes the
announced default. No migration.

The one check the pass verifies with is the driver over the fixtures of section 6, once against
the built driver and once with the graded line removed.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | verb, five functions, the clocks extracted, one bound read, one header line, one comment |
| `tools/unattended/unattended.test.sh` | `mkconf` eighth positional; one arm block |
| `tools/unattended/VERBS.template.md` | one bullet |
| `tools/unattended/SKILL.template.md` | one sentence, one fenced invocation |
| `tools/unattended/PROTOCOL.template.md` | one key-table row |
| `.unattended.conf`, `tools/unattended/.unattended.conf.example` | the key with its reason |
| `tools/unattended/kit.toml` | `optional_keys` gains the key |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp |
| `memory/guides/UNATTENDED-VERBS.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, `.claude/skills/unattended/SKILL.md` | re-rendered |

### Alternatives rejected

- **A verdict from `phase:` alone.** Six non-terminal records with CLOSED READMEs at base would
  read LIVE forever, which is the defect in section 1.
- **A JSON line.** The driver's readers are a Node hook and a shell tick; `key: value` is greppable
  by both without a parser and matches `fact`'s own grammar for the run-state file.
- **`stale` from the transcript alone.** Refuted by the research's skeptic: a healthy bar is 26
  minutes of transcript silence, so a threshold under `GATE_BOUND` resumes into a healthy bar.
  The gate-log signal is the one that moves during a bar, and the bound sits above `GATE_BOUND`.
- **A sixth verdict for a dead probe.** A reader keyed on the verdict line would have to know one
  more word; a refusal with no verdict line is what `--audit` does and what every reader already
  handles as "not STALE".
- **`ls-remote` for `finished-unstamped`.** A network call per tick per run from a scheduler;
  the local ref is at worst one fetch behind, and the cost of that is one wasted resume attempt.

## 5. Production-readiness checklist

- security — read-only; the verb writes no row and stages nothing. Every input it reads was
  authored by the run or by a hook of this kit; a forged `session:` yields a wrong `transcript`
  path and a forged `pid:` a wrong `pid-alive`, and the tick's kill is bounded to the recorded pid,
  which is unit 5's risk row.
- perf / scale — one `git log`, one `stat` per dirty path, one per gate-log file, one `tasklist`
  or `kill -0`, one `merge-base`; seconds, called once per stop and once per tick per run.
- error / empty / loading states — an absent key is `absent`; a clean tree, no gate logs and no
  transcript read from the commit; a missing stall file is `none`; a dead probe and a missing
  record are named refusals; an unresolvable default branch announces itself.
- observability — every value the verdict was decided from prints above it, so a reader re-derives
  the verdict from the lines; `last-move-source` says which signal won.
- risks — `stat -c` and `date -u +%s` are GNU spellings, live on every registered node; a BSD node
  hits the refusal rather than a wrong verdict. Moving the clock block out of `print_audit` changes
  no byte it computes; the audit's STALLED, PROGRESSING and dead-probe arms stand. The transcript
  encoding is measured on one node and degrades to `absent`, never to a wrong path that exists.
- testing — section 6; every arm runs the driver over a fixture. The suite is on no bar leg and is
  not run inside the pass.
- migration — N/A. No record shape changes; the key is optional and announced.
- user docs — the verb carrier, the protocol's key table and the Skill's one invocation are the
  docs, rendered and byte-compared by the kit gate; the prose about who calls it is unit 6's.

## 6. Acceptance criteria

The suite that carries the arms is on no bar leg and the build's rule three keeps it out of the
pass. Each criterion is observed by running the driver over the suite's `tRun` fixture in a scratch
clone as its arm does, after `build_audit_fixture` — which runs `--preflight` under the prologue's
pinned `CLAUDE_CODE_SESSION_ID=fixture-session` and `CLAUDE_PID=999999999` from unit 1 — with the
eighth `mkconf` positional carrying the bound. The staged break for each is a driver copy with the
graded line removed.

- **AC1** — When `bash tools/unattended/unattended.sh --liveness tNoRun` runs with no run-state
  file, it prints `UNATTENDED check 52 FAILED` and `no run-state file, so there is no run whose
  liveness can be graded:` and exits 1; and `bash tools/unattended/unattended.sh --liveness`
  with no slug is refused by `check_slug`, not by a verdict.
  Red when: the verb prints a verdict over a missing file; or the sentence differs from the arm's,
  which `python3 tools/memory-tree/check-arms.py --report` shows as a `check 52` branch not `ARMED`.
- **AC2** — When the fixture's phase is `LANDED`, `bash tools/unattended/unattended.sh --liveness tRun`
  prints `state: terminal` and `verdict: TERMINAL`, exits 0, and prints thirteen `key: value` lines
  and nothing else on stdout, the thirteen keys in S2's order, which is section 4's step order
  with `keepalive` before `pid-alive`; and every key prints again on a `BUILDING` fixture, so
  `grep -c ':'` over stdout is `13` in both.
  Red when: a terminal record omits a key, so a reader must know which state prints what; a line
  prints that is not `key: value`; or the exit is non-zero.
  figure: thirteen is DERIVED from S2's list at observation time.
- **AC3** — When the fixture's phase is `LANDING` and its witness is `$BASE`, the fixture commit
  on the fixture's `main`, the verb prints `state: finished-unstamped`,
  `default-branch: refs/remotes/origin/main` and `verdict: FINISHED-UNSTAMPED`; when the witness
  is the unit branch's HEAD it prints `state: live`; and when `GOV_DEFAULT_BRANCH` is unset and
  `origin/HEAD` is not set, it prints `default-branch: unresolved` and `state: live`.
  Red when: a witness on `main` reads `live`, which is the ancestry test not run; a witness off
  `main` reads `finished-unstamped`, which is a name resolved as a branch; or an unresolved
  default branch prints a ref, which is a fallback fabricating the passing value.
  fixture: the suite's `$BASE` and its `origin` remote, both built by the prologue.
- **AC4** — When the fixture's `pid:` is `999999999` the verb prints `pid-alive: no`; when it is
  the Windows pid of a background `sleep` the arm started — `ps`'s `WINPID` column for `$!` under
  MSYS, `$!` elsewhere — it prints `pid-alive: yes`, and after the sleep is killed, `no`; when
  `pid:` is `absent` it prints `pid-alive: unknown`; and under MSYS with `tasklist` shadowed on
  `PATH` by a stub that exits 1 and prints nothing, `unknown`.
  Red when: a live pid reads `no`, which is `kill -0` on a Windows pid; a dead pid reads `yes`,
  which is `tasklist`'s exit code trusted over its output; or `absent` is probed.
  fixture: the arm's own `sleep`, killed by the arm; `ps` with a `WINPID` column, measured present
  in this node's Git Bash on 2026-09-16.
- **AC11** — When, on AC4's live-sleep fixture, `pid-image:` is rewritten to `claude.exe`, the
  verb prints `pid-alive: no`; rewritten to what `read_pid_image` prints for that pid, `yes`; and
  rewritten to `absent`, `yes`.
  Red when: the mismatch reads `yes`, which is the image ignored and the recycled-pid kill left
  open; or `absent` reads `no`, which reds every lease written before the image existed.
- **AC5** — When the fixture conf carries `RESUME_STALE_BOUND=60` through `mkconf`'s eighth
  positional, the fixture commit is an hour old by `GIT_COMMITTER_DATE`, the tree is clean, the
  fixture git dir holds no `gate-logs` directory and `CLAUDE_CONFIG_DIR` points at an empty
  directory, the verb prints `last-move-source: commit`, `stale: yes` and `verdict: STALE`; after
  `touch` of one file under the fixture git dir's `gate-logs`, it prints
  `last-move-source: gate-log`, `stale: no` and `verdict: LIVE`; and after a file at the transcript
  path derived for `fixture-session` under a `CLAUDE_CONFIG_DIR` the arm builds is touched,
  `transcript:` names that path and `last-move-source: transcript`; and on the STALE fixture with
  no gate log and no transcript, after `touch scratch.txt` writes one untracked file over the
  hour-old commit, the verb prints `last-move-source: write` and `stale: no`.
  Red when: a clean, log-less, transcript-less tree reads `LIVE`, which is an empty signal read as
  "now"; a touched gate log leaves `STALE`, which is the third signal not joined; the transcript
  path never resolves, which is the encoding wrong for `.` or for `:`; or the dirty-write signal
  never wins, which is a maximum that dropped `TC_LASTW` and reads every run mid-edit as STALE.
  fixture: the arm sets `CLAUDE_CONFIG_DIR` itself for both halves, so the box's real transcripts
  are never read and git's global config under `HOME` is untouched.
- **AC6** — When the fixture conf declares no `RESUME_STALE_BOUND` — the `NOCONF` heredoc — stderr
  carries `declares no RESUME_STALE_BOUND, so a run reads STALE after the derived default of 5400s`
  once; when the eighth positional is `"abc"` the driver prints `REFUSING - RESUME_STALE_BOUND is
  declared as` and exits 2 before any verb runs; when the eighth positional is `"60"` under the
  fixture's `GATE_BOUND="3600"` and `UNIT_STALL_BOUND="1800"`, stderr carries
  `RESUME_STALE_BOUND (60s) is below GATE_BOUND + UNIT_STALL_BOUND (5400s)` once and the verb still
  prints its verdict; `grep -c '^read_bound_key RESUME_STALE_BOUND ' tools/unattended/unattended.sh`
  prints `1` and `0` at base, and `grep -cE '^read_bound_key [A-Z_]+ ' tools/unattended/unattended.sh`
  prints `4` and `3` at base; and each of the four carriers reads the key once —
  `grep -c '^RESUME_STALE_BOUND=' .unattended.conf` and the same over
  `tools/unattended/.unattended.conf.example` print `1`, `grep -c 'RESUME_STALE_BOUND' tools/unattended/kit.toml`
  prints `1`, and the section 8 region of `memory/guides/UNATTENDED-PROTOCOL.md` cut by
  `awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f'` carries the key once — every one `0` at base.
  Red when: a blank is silent; junk is coerced; a bound below the sum is silent, which is the false
  STALE unit 5 kills on; the call count stays `3`, which is a key with its own `case`; or a carrier
  is missing, which check 22 reds at the close and this grep sees now.
  figure: 5400 is DERIVED in the driver as `GATE_BOUND + UNIT_STALL_BOUND` from the fixture's
  declared values; the arm's needle carries the literal and reds if the derivation or either
  declared addend moves. The counts `1`, `4`, `3` and `0` are DERIVED by the greps at observation.
- **AC7** — When the file `stall.tRun.log` under the `unattended` directory of the fixture's git
  dir — `git rev-parse --git-dir` — holds one line written by `printf`, the verb prints
  `last-stall:` followed by that line verbatim; when the file is absent, `last-stall: none`; and
  `grep -c 'resolve_sidecar_dir' tools/unattended/unattended.sh` prints at least `2`, the
  definition and this verb's call, and `0` at base; and
  `grep -cE '^[^#]*rev-parse --git-dir' tools/unattended/unattended.sh` prints exactly `1` at this
  unit's tip and `0` at base — the literal on one CODE line, the function's, however many comment
  lines name it.
  Red when: the line is parsed or truncated; an absent file is a refusal; or the root is spelled
  inline, which leaves unit 7 a second spelling to drift from; or the code-line count is not 1,
  which is the premise unit 11's check reads after unit 20 moves the one line into the lib.
  figure: every count is DERIVED by the greps at observation.
- **AC8** — When `stat` is shadowed on `PATH` by a stub that exits 1 over a dirty fixture tree,
  the verb prints `UNATTENDED check 52 FAILED` and `the liveness cannot be measured on this node`,
  no `verdict:` line, and exits 1; and `grep -c 'read_tree_clocks' tools/unattended/unattended.sh`
  prints at least `3` — one definition, one call in `print_audit`, one in `print_liveness` — and
  prints `0` at base; and on the audit arms' STALLED fixture `bash tools/unattended/unattended.sh --audit tRun`
  still prints a line carrying `· last-write none ·` and `· STALLED`, which is the extraction
  leaving the audit's arithmetic alone.
  Red when: a dead `stat` yields a verdict; the count is `2`, which is one verb keeping a copy; or
  the audit's line changes bytes.
- **AC9** — When `grep -c 'unattended.sh --liveness' tools/unattended/unattended.sh` runs it
  prints `1` and `0` at base; `grep -cP '^- \x60--liveness\x60' tools/unattended/VERBS.template.md`
  and the same over `memory/guides/UNATTENDED-VERBS.md` each print `1`;
  `grep -c 'unattended.sh --liveness' tools/unattended/SKILL.template.md` and the same over
  `.claude/skills/unattended/SKILL.md` each print `1`; and `grep -c -- '--liveness' tools/unattended/unattended.sh`
  is at least `3`, the declaration, the header and the dispatch arm. Leg half, observed at
  `--close`: `bash tools/unattended/adopt-unattended.sh --check` prints `in sync` and exits 0.
  Red when: any count is `0`, which is a carrier check 26 will name; or the renders differ from
  their templates.
- **AC10** — When `git show --name-only --format= HEAD` runs on the pass commit, it lists
  `.unattended.conf` and `memory/guides/SESSION-KICKOFF.md` together, the `last-audit` line of the
  latter names the sha the manifest's own stamp rule gives — `git merge-base origin/main HEAD` off
  the default branch, an ancestor of HEAD and later than the stamp it replaces — with a datetime
  that advances, the commit message carries the `manifest-audit:` delta line, and
  `git grep -lE '^\*\*Status:\*\* CLOSED' -- memory/builds/aWokenSentinel/spec/` lists this spec.
  Leg half, observed at `--close`: `bash skills/session-kickoff/manifest-check.sh` check 5 reports
  no watched file changed since `last-audit`.
  Red when: the conf moved without the stamp; the stamp names a sha not in this branch; or the
  header still reads `SPECCED`.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kickoff-manifest ratchet` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness`

These are `--close`'s. The pass runs none of them: it verifies with the driver invocations of
AC1 to AC8 over the fixture and the greps of AC6, AC8 and AC9, nothing else. Under
`unattended kit gate`, checks 10 and 26 are the joins this unit moves. Chunks read from
`tools/gate-legs.json` on 2026-09-16: `unattended kit gate`, `harness arms`, `spec tokens`,
`lexicon` and `codebase-map` are `chunk: declarations`; `unattended skill wiring` is
`chunk: wiring`; `install-prefix` is `chunk: product`; `memory hygiene` and
`kickoff-manifest ratchet` are `chunk: records`; none is `chunk: selftests`.

New arm: `tools/unattended/unattended.test.sh` · the two check-52 refusals of AC1 and AC8, each
observed against the driver copy with the branch removed — a missing file, a shadowed `stat` —
plus the TERMINAL, FINISHED-UNSTAMPED, UNBOUND, pid, STALE, LIVE, transcript, stall-line and bound
fixtures of AC2 to AC7 · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the block's executed
assertions; `FLOOR_SHARD_1` does not move.

## 8. Open questions

none

## 9. Revision log

- rev-5 · 2026-09-21 · S6 · §4 · AC11 · inventory · folded the closing diff review round 1
  (`reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md`), id 2 (HIGH): `pid-alive: yes` proved
  that SOME process held the pid, and the tick's tree kill then ran on whatever that was after a
  reboot recycled the number. `check_pid_alive` takes the lease's recorded image (unit 1's rev-5)
  and prints `no` on a mismatch; it moved to the library with `read_pid_image` because the writer,
  this verb and the tick's launched-pid probe are three callers. Status unchanged, CLOSED.
- rev-4 · 2026-09-20 · §4 fixture 6 · AC10 · the build pass, before its code: the arm's transcript
  root moved from `$TMP/cfg` to `$ORIGIN_DIR/cfg`, because `$TMP` is the fixture's work tree and a
  directory under it is an untracked write that ties the transcript's mtime and wins the source
  line (observed RED on the block's first run); and AC10's stamp phrase — "the commit's parent or a
  later sha" — contradicted the manifest's own stamp rule, which off the default branch names
  `git merge-base origin/main HEAD`, so the criterion now states that rule. Status CLOSED in the
  pass commit; no other criterion moved.
- rev-3 · 2026-09-20 · §3 · AC7 · folded spec-audit round 2: sibling agreement for the promoted
  `TOOL-aWokenSentinel-20` (H6, raw 36) — AC7 pins the code-line count of `rev-parse --git-dir`
  at exactly 1 at this unit's tip, the premise spec 11 rested on and nothing asserted, and §3 hands
  the function's move to the lib off; the unit-11 bullet names the widened population. Order
  unchanged.
- rev-2 · 2026-09-20 · S2 · S5 · §3 · §4 · AC2 · AC5 · AC6 · §10 · folded spec-audit round 1:
  M2 (raw 5, 23, 41) — the `read_bound_key` count was 5 at base, not 3, so AC6 now greps the call
  line's own spelling and S5 and §10 say fourth caller; M3 (raw 6) — S5's four carriers had no
  criterion, so AC6 reads each by path; M8 (raw 35) — the default derived from kit defaults and
  retyped 1800, so §4 derives it from the declared `GATE_BOUND + UNIT_STALL_BOUND` after both
  reads and announces a declared value below the sum; L2 (raw 11) — S2's exit contract now names
  the check-52 refusal; L3 (raw 12) — AC5 gains the dirty-write arm; L9 (raw 27) — S2's key order
  is section 4's and AC2 cites S2. Edges gain hands-off rows to units 5 and 11 for the
  one-derivation rule H3 (raw 4, 20, 34) promoted to `TOOL-aWokenSentinel-11`.
- rev-1 · 2026-09-16 · initial draft, from the brief in
  `memory/builds/aWokenSentinel/prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md`
  and the research record under `build/`. Three corrections against the node: the transcript
  directory encoding replaces `.` as well as `:`, `/` and `\`; `kill -0` on a Windows pid fails
  under MSYS even while the process lives, so the MSYS arm is `tasklist` and its OUTPUT decides;
  and a dead probe is a refusal, as at `--audit`, rather than a value.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "is this unattended run alive: one read-only liveness
predicate over the run-state file, the tree's newest write and commit, the recorded pid and a stale
bound"`, run on 2026-09-16 at base `5f9648d6`, reported `scan coverage: 73 files scanned | 0 parse
skips | unscanned layers: .sh` and ranked `read_roots` in `tools/process-monitor/scope.py` and
`boundedParallel` in the workflow scripts — neither is a seam for a shell verb, and the driver is
in the layer the map does not scan, so the seams are cited from source by grep. The seam this unit
extends is `print_audit`'s clock block at `tools/unattended/unattended.sh:3013` to `:3025`, which
becomes `read_tree_clocks` with two callers; `read_bound_key` at `:358`, whose FOURTH caller this
is after `GATE_BOUND`, `UNIT_STALL_BOUND` and `REVIEW_ROUNDS` — a call, never a fourth `case`;
the audit counted the grep at base as 5 (definition, three calls, one comment at `:525`), which is
why AC6 anchors its count on the call line's own spelling;
`is_terminal` at `:613`; and the offline half of `check_single_live`'s finished-unstamped test at
`:1372` to `:1392`, whose sha-shape `case` and `merge-base --is-ancestor` are reused with a local
ref in place of the observed anchor. The verb-carrier seam is check 26 of
`tools/unattended/check-unattended.sh`, which joins three carriers and is why the Skill invocation
ships here and not in unit 6.

The recall probe's live hits were `TOOL-aProbedUnit-11` (the `--audit` decision and its bound),
the protocol's section 8 row for `UNIT_STALL_BOUND` (the terms the new key copies), and
`TOOL-dUnstalledConvoy-38` (`--landed` evaluating its idempotence guard after its own write),
which binds unit 7 and not this one. Where a hit was STALE against source: the brief cites
`verb_audit`; at base the function is `print_audit`, renamed by `TOOL-aProbedUnit-3` for the
lexicon, and this spec cites the name the file carries.

Recall terms used: `python tools/memory-recall/query.py "what decides whether an unattended run is
alive, finished without a stamp, or stalled, and which verb measures the tree's idle time" --terms
"audit stall bound last-write last-commit dispatched unit idle PROGRESSING STALLED liveness
finished-unstamped witness ancestor"`.
