# TOOL-aWokenSentinel-5 — `resume-tick.sh`, the OS-scheduled out-of-process resumer

**Status:** CLOSED · rev-5 · 2026-09-21 · node a · Tier-2 · base 5f9648d6 · streams tooling · order 11 · ratified 2026-09-16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md](../build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md) | research | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-6 |
| [2026-09-16-build-TOOL-aWokenSentinel-5-1-acceptance-ledger.md](../build/2026-09-16-build-TOOL-aWokenSentinel-5-1-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 |
| [2026-09-16-prompt-TOOL-aWokenSentinel-5-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-5-1-build-brief.md) | journal | — |
| [2026-09-21-prompt-TOOL-aWokenSentinel-5-2-fold-brief.md](../prompts/2026-09-21-prompt-TOOL-aWokenSentinel-5-2-fold-brief.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-12 |
| [2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-1-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |
| [2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md](../reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round2.md) | diff-review | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14 TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-19 TOOL-aWokenSentinel-20 TOOL-aWokenSentinel-21 TOOL-aWokenSentinel-22 TOOL-aWokenSentinel-23 TOOL-aWokenSentinel-24 TOOL-aWokenSentinel-25 TOOL-aWokenSentinel-26 TOOL-aWokenSentinel-27 TOOL-aWokenSentinel-28 |

<!-- /gen:spec-records -->

## 1. Goal

Every recorded resume of a stalled unattended run was a human starting a session. This unit ships
the one mechanism that acts when the session is idle-on-error, hung, locked out or dead, because it
does not share the session's process: `resume-tick.sh`, registered by the owner as an OS-scheduled
task, which walks every worktree, asks `--liveness` about every run whose lease names a session,
and on `STALE` kills the recorded pid's tree, appends an attempt line and launches
`claude -p --resume <session>` detached, with a payload that forbids re-parking.

## 2. Scope (IN)

- **S1** — A new kit file `resume-tick.sh` with `[--repo <root>] [--dry-run]`. It derives its kit
  dir from `$0`, the repo root from `--repo` or `git rev-parse --show-toplevel`, and walks
  `git worktree list --porcelain`. It sources `lib-unattended.sh` beside itself and calls the
  driver beside itself, and it spells no path outside its own directory. Observed by AC1, AC2 and
  AC8.
- **S2** — Per worktree, for each `<MEMORY_ROOT>/builds/*/RUN.md` IN THE INDEX whose `session:`
  fact, read off the index blob, is present and not `absent`, the tick runs `unattended.sh
  --liveness <slug>` with that worktree as cwd and decides from its `verdict`, `stale`, `pid`,
  `pid-alive` and `last-move` lines; a run-state file on disk and not in the index is announced
  and skipped, and a lease whose `host:` names another node is skipped before the probe. The
  decision table is section 4. Observed by AC1, AC2, AC3, AC4, AC14, AC15 and AC16.
- **S3** — `RESUME_ATTEMPTS` (kit default 6) and `RESUME_TURNS` (kit default 40) are read through
  `read_bound_key`, which this unit HOISTS verbatim from `tools/unattended/unattended.sh` into
  `tools/unattended/lib-unattended.sh` so the tick and the driver read a bound the same way — and
  satisfies the function's calling-shell contract the way the driver does: the tick sources
  `$ROOT/.unattended.conf` into its own shell with `CONF` set before the two calls, which is
  `TOOL-aWokenSentinel-13`'s design, root-scoped, and that unit's arms observe it under a declared
  key. The driver's four calls stay where they are. Both keys are added to `.unattended.conf` and
  `tools/unattended/.unattended.conf.example` with a one-line rationale each, to
  `tools/unattended/kit.toml` `optional_keys`, and to the protocol's section 8 key table with its
  render, because check 22 of the kit gate joins the example to that table in both directions.
  Observed by AC5 and AC6.
- **S4** — Attempts are counted from `<git-dir>/unattended/resume.<slug>.log`, one line per
  launch, and only the lines newer than the run's last move count against the cap. Observed by
  AC3.
- **S5** — On `pid-alive: yes` the tick kills the recorded pid's TREE before launching — and
  only AFTER the login row has answered logged-in, so a kill happens only where a launch will
  follow, which is `TOOL-aWokenSentinel-12`'s order and that unit's arm observes it: `taskkill
  //PID <pid> //T //F` under MSYS, `kill -- -<pgid>` elsewhere. `pid-alive` is `--liveness`'s and
  from rev-5 matches the lease's recorded image too, so a recycled pid reads `no` and is not
  killed. A launched pid (S13) still alive after the tree moved is killed beside it. Observed by
  AC4 and AC13.
- **S6** — `claude auth status` is consulted before every launch; a CLI that is not logged in is an
  ANNOUNCED skip line and exit 0, never a pass and never a launch. Observed by AC2.
- **S7** — The launch is DETACHED through a launcher file the tick writes under the sidecar dir:
  the tick returns while the resumed session runs. The CONTINUE payload is one string in the tick,
  section 4. Observed by AC1 and AC7.
- **S8** — `verb_status` gains one FIELD on its existing line, ` · resume-tick <n> attempt(s), last
  <utc>`, printed only when the sidecar holds at least one line, so no existing arm that reads the
  status line whole sees a byte it did not see at base; the sidecar is found through unit 2's
  `resolve_sidecar_dir`, never an inline `rev-parse`, which `TOOL-aWokenSentinel-11`'s kit-gate
  check binds. Observed by AC9.
- **S9** — `adopt-unattended.sh --check` prints one INFO line saying whether a scheduled task named
  `gov-resume-tick` exists on this node, before its `in sync` line, and reds on neither answer.
  `tools/unattended/README.md` carries the registration line per OS. Observed by AC10.
- **S12** — The walk's two announced skips — a non-zero `--liveness` exit prints
  `liveness probe failed: <line>` and skips the run; a worktree without `.unattended.conf` prints
  one line and is skipped while the other trees are still walked. Observed by AC12.
- **S10** — The tick's own suite, one arm per decision, with a STUB `claude` first on `PATH`; a
  budget row for it in `tools/run-gates/selftest-budgets.txt`; the suite named in `kit.toml`'s
  `project-owned` list; every function in the tick and its suite leads with a verb `.lexicon.conf`
  declares, so `VERB_OFFENDER_PIN` does not move. Observed by AC8 and AC11.
- **S11** — `.unattended.conf` is on the kickoff manifest's `watch:` line, so the same commit
  re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md` with a delta line in the subject.
  Observed by AC6.
- **S13** — The pid the tick launched is written onto the attempt line as a trailing
  `launched <pid>` field and read back by the next tick through the library's `check_pid_alive`:
  alive with the tree unmoved since the line, the run is IN-FLIGHT and skipped; alive with the
  tree moved since, the resumed session hung and its tree is killed beside the recorded pid's.
  Observed by AC13.

## 3. Non-goals (OUT)

- **No registration by the kit.** `schtasks /create` and `crontab` are the OWNER's acts, once per
  node, and the mandate names the CLI token as minted out of band (build-level rule five). The
  tick ships INERT: unregistered it does nothing, and `--check` reports that as INFO because an
  adopter who has not registered it has a working kit, not a broken one.
- **No owner notification.** `ATTEMPTS EXHAUSTED` is the line a notification would key on; the
  notification itself is the research record's fallback 10 and is a backlog row the close mints,
  not this unit.
- **No liveness of its own.** The tick decides from `--liveness`'s lines and never re-derives
  `stale`, `pid-alive` or the terminal predicate; a second spelling of any of them is the
  two-answers class unit 2 exists to remove. What `--liveness` cannot see, the tick cannot either.
  The one probe the tick runs itself, on the pid IT launched (S13), is the library's
  `check_pid_alive` — the same function `--liveness` calls, not a second spelling.
- **No mandate check beyond the index.** The tick launches only on a lease the INDEX holds
  (S2), which closes the FILE-WRITE attacker — an `acceptEdits` session, a sub-agent or an
  injected edit dropping a `RUN.md` under a worktree. An actor who can STAGE is the shell-access
  case protocol section 9 concedes, and the remote-BASE check stays `--preflight`'s.
- **No driver verb.** A verb the agent never runs would still owe a header line, a VERBS entry and
  a Skill invocation under check 26, and the driver's preamble refuses a cwd outside a repo, which
  is exactly where a scheduler starts a task. The tick is a sibling script that takes `--repo`.
- **No `run_bounded` hoist.** Its two globals, `GATE_BOUND_LIVE` and `GATE_BOUND`, are the driver's
  conf-derived state; the tick's one network-shaped call is bounded inline instead (section 4,
  "Login"). `ponytail:` one inline `timeout`; hoist `run_bounded` with its globals if the tick
  grows a second bounded call.
- **No kit version bump.** The closing pass bumps unattended 1.24 to 1.25 once across every carrier
  `bash tools/check-kit-versions.sh` names.
- **No hook, no protocol prose, no Skill prose.** The stop-guard and the stall-recorder are units 3
  and 4; the contract that names the tick as one of three keepalive actors, the Skill section that
  points at the README's registration line and the sidecar-layout paragraph are unit 6's.
- **The suite is not run whole inside the pass.** Build-level rule three: each arm is observed by
  running the tick over its fixture directly, and the suite runs at the close through
  `bash tools/unattended/run-unattended-gates.sh` on a frozen clone.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-1` — the `session:` and `pid:` facts, and
  `--resume <slug> --keepalive-id <id>`, which the CONTINUE payload tells the resumed session to run
  first. Without unit 1 every record reads `session: absent` and the tick has nothing to resume.
- **consumes-from** `TOOL-aWokenSentinel-2` — `--liveness <slug>` and its `verdict`, `pid`,
  `pid-alive` and `last-move` lines, `RESUME_STALE_BOUND` as the number behind `stale` (read
  there, never here), the `fail 52` refusal shape the tick treats as a dead probe, and
  `resolve_sidecar_dir`, through which S8 finds the resume log in the driver. Unit 2's spec hands
  this unit "keying the tick on `verdict: STALE` and on `pid-alive`" and the resume log's
  derivation, and that is the whole of what this unit reads.
- **consumes-from** `TOOL-aWokenSentinel-11` — the kit-gate check that the driver, the lib and
  the tick together hold one code-line `rev-parse --git-dir`, in the lib; S8's read through the
  function is what keeps it green in the driver, and S4's read through the same function is what
  keeps it green in the tick, which is inside that check's population at its rev-2.
- **consumes-from** `TOOL-aWokenSentinel-20` — `resolve_sidecar_dir` in `lib-unattended.sh`,
  which the tick sources; S4's resume-log root is that function's answer, never an inline
  `rev-parse` of the tick's own. Without the move the tick would hold the second bash spelling of
  the root the kit's own record (the lib header's pointer, dUnstalledConvoy seq 22) says must not exist.
- **hands-off** `TOOL-aWokenSentinel-6` — the protocol's section 5 naming the tick as a keepalive
  actor, the Skill's short section naming the two hooks and the tick, the README's sidecar-layout
  paragraph beside this unit's registration lines, and the rationale prose for `RESUME_ATTEMPTS`
  and `RESUME_TURNS` where unit 6 finds this unit's one-liners wanting. This unit writes the
  registration lines and the section 8 rows; unit 6 does not rewrite them.
- **hands-off** `TOOL-aWokenSentinel-9` — the field rule at `verb_status` (appended to
  `parked`, omitted at nothing) and the `resume-tick` field that precedes unit 9's keepalive field
  on the same line — the shape F1 chose, and the one-line promise unit 17 arms and unit 9 reads.
  Unit 7 prints no `--status` line at its rev-2 and takes nothing from this unit.
- **hands-off** `TOOL-aWokenSentinel-18` — the guard inside the hoisted `read_bound_key` that
  refuses a caller with no `CONF` naming a file; this unit moves the function verbatim, unit 18
  adds the guard one order after unit 13 sets `CONF` in the tick.
- **hands-off** `TOOL-aWokenSentinel-12` — the arm that observes a live recorded pid surviving
  under a logged-out CLI, and the gotcha class for a destructive step ordered before its
  precondition; this unit builds the order, unit 12 proves it.
- **hands-off** `TOOL-aWokenSentinel-13` — the arms that observe the root conf's declared
  `RESUME_ATTEMPTS` and `RESUME_TURNS` honoured and the NOTE naming a non-empty path; this unit
  builds the read, unit 13 proves it.
- **hands-off** external — registering `gov-resume-tick` on each node, the owner's act; the
  owner-notification fallback, a backlog row the close mints.

## 4. Design

### The walk

```
resume-tick.sh [--repo <root>] [--dry-run]
```

`KIT_DIR=$(cd "$(dirname "$0")" && pwd)`; `DRIVER="$KIT_DIR/unattended.sh"`; `.
"$KIT_DIR/lib-unattended.sh"` — the same three lines `gate-guard.test.sh` and the driver use to
find their siblings, and an empty derivation refuses with exit 2 naming what it looked for. The
root is `--repo` when given, else `git rev-parse --show-toplevel`; a root that is not a git
repository is `resume-tick: REFUSED — <root> is not a git repository, so there is no worktree list
to walk`, exit 2. The tick defines no `fail()` helper and has no numbered checks, so it joins no
population `tools/memory-tree/check-arms.py` discovers; its refusal lines are its own suite's to
assert.

Before the walk, the tick's own conf read, as `TOOL-aWokenSentinel-13` §4 states it:
`CONF="$ROOT/.unattended.conf"`, refused with exit 2 naming the root when absent, then `. "$CONF"`
into the tick's shell, then the two `read_bound_key` calls — the driver's own idiom at
`unattended.sh:341`, so `RESUME_ATTEMPTS` and `RESUME_TURNS` resolve from the ROOT's declaration
and the NOTE names that file. The two knobs are root-scoped: one repo, one pair of bounds.

`git -C "$ROOT" worktree list --porcelain` gives one `worktree <path>` line per tree. Per tree: skip
with one line when `<path>/.unattended.conf` is absent (a checkout predating the kit); otherwise
`MEMORY_ROOT` is read by sourcing that conf in a subshell, default `memory`, and every
`<MEMORY_ROOT>/builds/*/RUN.md` IN THE INDEX whose `session:` fact, read off the index blob by one
`git -C <tree> grep --cached -H -E '^(session|host): '`, is present and not `absent` is a
candidate, with its `host:` fact taken from the same read (rev-5). A record `git ls-files --others`
lists — on disk, not in the index — prints `skip · RUN.md is not tracked, and the tick launches
only on a lease the index holds` and is never probed: the index is what `stage_or_fail` writes at
`--preflight` and at `--resume --keepalive-id`, and the working copy is what anything with a file
handle writes. That read is the only read the tick makes of a record directly; everything else is
`--liveness`'s. Zero candidates across every tree prints `resume-tick: no bound run in <n>
worktree(s)` and exits 0 — an announced nothing, never a silent one.

Per candidate, first the node: a `host:` fact naming a node other than `read_host_name`'s answer
prints `skip · leased on <host>, not this node <me>` and nothing is probed, killed or launched —
its pid is a number in another process table; `absent` or no fact at all is judged as before.
Then, with cwd set to the worktree so the driver reads that tree's conf:
`bash "$DRIVER" --liveness <slug>`. A non-zero exit — unit 2's `fail 52` dead-probe refusal
included — prints `resume-tick: <slug> · liveness probe failed: <line>` and skips, where `<line>`
is the driver's `UNATTENDED check` sentence when one printed, else the first line that is not a
`unattended: NOTE`, else the first line (rev-5: the driver NOTEs every undeclared bound on stderr
at source time, so an adopter on a kit default logged the NOTE instead of the check): a run whose
liveness cannot be measured is never resumed, because the alternative reads a dead probe as a
verdict. The five values are read off the `key: value` lines by `sed -n 's/^verdict: //p'` and its
siblings.

### The decision, per run

| `verdict` | attempts | `pid-alive` | login | act |
|---|---|---|---|---|
| — (RUN.md not in the index) | — | — | — | `skip · RUN.md is not tracked, and the tick launches only on a lease the index holds` |
| — (`host:` names another node) | — | — | — | `skip · leased on <host>, not this node <me>` |
| not `STALE`, and not `FINISHED-UNSTAMPED` with `stale: yes` | — | — | — | `skip · verdict <V>` |
| `STALE` | `RESUME_ATTEMPTS` or more since the last move | — | — | `skip · ATTEMPTS EXHAUSTED · last <utc> · out <path>` |
| `STALE` | newest line's `launched <pid>` alive AND the line newer than the last move | — | — | `skip · IN-FLIGHT · launched <pid> alive since <utc>` |
| `STALE` | under the cap | any | not logged in | `SKIP — the CLI is not logged in on this node; nothing can resume <slug>` — nothing killed, nothing written |
| `STALE` | under the cap | `yes` | logged in | kill the tree — the recorded pid's, and a launched pid still alive after the tree moved — then the row below |
| `STALE` | under the cap | any | logged in | append the attempt line, launch detached, `resumed · attempt <n> · out <path>` |

`STALE` in the rows below the first three reads as "`STALE`, or `FINISHED-UNSTAMPED` with
`stale: yes`" (rev-5): a session that dies between the lander's push and `--landed` outranks
`STALE` in `--liveness`'s verdict order and nothing else stamps it — the B1 wedge for a dead
session, which unit 8 covered for the live one — and the payload's "continue from the phase the
run-state file names" is `--landed` there.

The login row precedes the kill row, and the order is the point: a kill is useful only where a
launch will follow, so the probe that decides whether one can happen runs first, and a logged-out
node kills nothing. `TOOL-aWokenSentinel-12` owns that ordering's proof — the arm with a live
recorded pid under a logged-out stub — and the gotcha class it left-shifts.

Every act prints exactly one line, `resume-tick: <slug> · <worktree> · <act>`, and `--dry-run`
prints the line it WOULD act on with ` (dry-run)` appended and does nothing else — no kill, no
attempt line, no launch, no login probe.

The in-flight guard is the LAUNCHED PID (S13, rev-5; rev-4 had none and reasoned only about a
launch that produced no turn). `run_detached` writes the pid it started to a file — `Start-Process
-PassThru`'s `.Id` under MSYS, `$!` elsewhere — never through `$( )`, and the tick appends
` launched <pid>` to the attempt line it wrote before the launch. `derive_attempts` reads it back
from the newest line: alive with that line NEWER than the run's last move, the resumer has not
produced its first turn — throttled, or still starting — and a second launch would put two
skip-permissions agents on one tree, so the tick prints the IN-FLIGHT skip; alive with the line
OLDER than the last move, the resumed session ran, moved the tree and hung, which is the case the
tree kill exists for, so it joins the kill and the run is relaunched. A resumed session that ran
`--resume --keepalive-id` is the recorded pid and takes the ordinary row. `ponytail:` the launched
pid is the launcher shell and the CLI is its child, so the tree kill reaches it; record the child
if a launcher ever exits while its child lives. The tick reads no `RESUME_STALE_BOUND`: that is
`--liveness`'s number, and a second reader of it in the tick would be a second copy of its default.

### Attempts (S4)

`$(resolve_sidecar_dir)/resume.<slug>.log`, the function `TOOL-aWokenSentinel-20` puts in
`lib-unattended.sh` and the tick sources, called with cwd in the worktree so it answers that
tree's git dir — the kit's one spelling, the same dir the `stop` and `stall` kinds use, and the
tick spells no `rev-parse` of its own, which is what unit 11's check reads.
One space-separated line per launch, appended before the launch so a tick that dies mid-launch
still counts:

```
<utc> attempt <n> session <sid> pid <pid> pid-alive <yes|no|unknown> out <out-path>[ launched <pid>]
```

The `launched` field is appended AFTER the launch by `sed -i` on the last line, because the pid
exists only then; a tick that dies between the two leaves a line without it, which the next tick
reads as it read every line before rev-5. `out` is cut at ` launched ` wherever the line is parsed.

The count against the cap is the number of lines whose `<utc>` is newer than the run's last move,
where the last-move instant is `now - last-move` from the `--liveness` line, so a resume that
produced a commit, a write or a transcript entry resets the count and the cap bounds CONSECUTIVE
fruitless attempts rather than a run's lifetime. `<n>` in the line is the lifetime ordinal, so an
owner reading the sidecar sees both. `ponytail:` a transcript-only move resets the count too, which
`RESUME_TURNS` and unit 3's block cap bound; count commits alone if that proves too generous.

### The tree kill (S5)

The kill is aimed at the recorded PROCESS, not the number (rev-5): `write_lease` records `host`,
`pid-image` and `lease-utc` beside `pid` (unit 1), the library's `check_pid_alive <pid> [image]`
reads `no` when something holds the pid and the recorded image does not match it (unit 2), and
`--liveness` passes the record's `pid-image` to it — so a pid a reboot recycled to the owner's next
process is `pid-alive: no` here and never killed. An image of `absent`, or none, is the pid-only
reading a pre-rev-5 lease always had. `read_host_name`, `read_pid_image` and `check_pid_alive` live
in `lib-unattended.sh`, moved there from the driver, because the driver writes the facts, `--liveness`
probes the recorded pid and the tick probes the launched one, and a spelling in each is two answers.

Under `uname -s` matching `MINGW*|MSYS*|CYGWIN*`: `taskkill //PID "$pid" //T //F`. Measured on node
`a` 2026-09-16: a bash-started `ping` child, killed by its Windows pid this way, is gone from
`tasklist` and from `ps` afterwards, and the `//` doubling is the MSYS shell's path-mangling guard,
which `tools/process-monitor/reap.py`'s header records as wrong from a non-shell exec and right
from bash. Elsewhere: `kill -- -"$(ps -o pgid= -p "$pid" | tr -d ' ')"` then `kill "$pid"`,
UNVERIFIED — no registered node is POSIX. The recorded pid is `claude.exe`'s Windows pid, a
native parent, so `/T` walks the tree from a Windows edge; the measured hole in that reaper's
header — MSYS-forked grandchildren whose parent edge is not a Windows one — is a known ceiling
here: `ponytail:` one `taskkill`; route through the process-monitor kit's per-row reaper if a
resumed turn ever re-stalls on a survivor, at the cost of a Python launch in the tick.

### Login (S6)

Consulted BEFORE any kill, per the table above. `claude auth status` printed, on node `a`
2026-09-16 with the CLI logged in, a JSON object whose
second line is `"loggedIn": true`, exit 0. The tick greps `"loggedIn":[[:space:]]*true` over the
output and treats anything else — `false`, an error, an empty answer — as not logged in, because
the exit code of the logged-out case was not measured and a grep over the measured shape is right
in both. The call is bounded by `timeout 60` where `timeout 1 true` runs, unbounded otherwise: a
bound may never turn the check into a skip. A not-logged-in answer is the announced line above,
exit 0, and no attempt line: an attempt that could not have launched is not an attempt.

### The launch (S7)

The tick writes `<git-dir>/unattended/resume.<slug>.<utc>.sh`, the LAUNCHER, and runs it detached.
The `<utc>` in a FILE name is the basic-format stamp, `20260920T202456Z`, never the extended one
with colons: NTFS has no `:` in a file name, MSYS smuggles one through as a private-use
character that `cygpath -m` and `Start-Process` then disagree about, and the launcher's path
crosses that boundary (rev-4). The attempt LINE keeps the extended stamp, which is what the
count compares.
The launcher is three statements: `export PATH='<the tick's own PATH>'`, `cd '<worktree>'`, and

```
claude -p --resume '<session>' --dangerously-skip-permissions --max-turns <RESUME_TURNS> '<payload>' </dev/null >'<out>' 2>&1
```

where `<out>` is `<git-dir>/unattended/resume.<slug>.<utc>.out`. The PATH export is what lets the
suite's stub `claude` win: a login shell re-reads its profile and would put the real CLI back.
`--max-turns` is absent from `claude --help` on CLI 2.1.178 and is ACCEPTED by it — measured
2026-09-16 on node `a`: `claude -p --max-turns 1 </dev/null` answers the no-input error while
`claude -p --bogus-flag 1` answers `unknown option`, and neither reaches the API. `-p` warns after
3 s with no stdin, so stdin is `/dev/null` (research section 6).

Detachment is `run_detached <launcher>`: under MSYS, `powershell.exe -NoProfile -NonInteractive
-Command "Start-Process -WindowStyle Hidden -FilePath '<bash.exe>' -ArgumentList '<launcher>'"`
with both paths through `cygpath -m`; elsewhere `setsid nohup bash <launcher> >/dev/null 2>&1 &`.
Measured on node `a` 2026-09-16: the PowerShell form returned in 0 s with the launched child still
alive two seconds later and its output file written. A `nohup … &` inside the tick's own console
was not relied on, because whether a scheduler's console keeps a background child alive after
`bash -lc` exits was not measured and the design does not need the answer: `Start-Process` gives
the child a console of its own. The launcher file doubles as the record of what was launched,
argv included, beside the `.out` it wrote to.

The CONTINUE payload is ONE string in the tick, with `<kit-rel>` derived as `${KIT_DIR#"$ROOT"/}`
and never spelled:

> You are the resumed session of unattended run `<slug>`. First run
> `bash <kit-rel>/unattended.sh --resume <slug> --keepalive-id <the idle-wake id you schedule now,
> per the unattended Skill>` so this session's lease replaces the dead one. Then continue from the
> phase the run-state file names. The owner is absent: never park a question the protocol lets you
> decide — take the option that makes no measured observable worse and record why. If the run is
> terminal, reap the idle-wake and stop.

### `--status` (S8)

In `verb_status`, beside the `parked`, `noted` and `STALE briefs` fields and following their rule:
when `$(resolve_sidecar_dir)/resume.<slug>.log` — unit 2's one derivation, never an inline
`rev-parse`, which unit 11's check reds at the close — exists and has at least one line,
`parked="$parked · resume-tick <n> attempt(s), last <utc>"` with `<n>` the line count and `<utc>`
the last line's first token. Absent or empty, nothing is printed — the ordinary line does not grow.
`--resume` inherits it through `verb_status`, so the status-and-resume agreement arm still holds.

### The adopter's INFO line and the README (S9)

In `adopt-unattended.sh`'s `--check` branch, before the `in sync` line: under MSYS
`schtasks //query //tn gov-resume-tick` — the `//` because `schtasks /query` from bash is mangled to
`C:/Program Files/Git/query`, measured 2026-09-16 — exit 0 prints `unattended: INFO — the resume
tick is registered as gov-resume-tick`, anything else `unattended: INFO — no scheduled task named
gov-resume-tick on this node; the resume tick is unregistered (the kit README has the line)`;
elsewhere the same two lines keyed on `crontab -l 2>/dev/null | grep -qF resume-tick`. Neither
answer changes the exit code.

The README gains a section, "The resume tick — registration is the owner's", with the two lines,
placeholders and no kit path: Windows, from cmd or PowerShell, `schtasks /create /sc minute /mo
10 /tn gov-resume-tick /tr "\"<bash.exe>\" -lc \"<kit-dir>/resume-tick.sh --repo <root>\""` with a
note that Git-Bash needs every `/` option doubled; POSIX, `*/10 * * * * <kit-dir>/resume-tick.sh
--repo <root>`; and `--dry-run` as the way to read what a tick would do. Unit 6 adds the sidecar
layout beside it.

### Data model

Two conf keys, OPTIONAL and announced: `RESUME_ATTEMPTS` — the cap on consecutive fruitless
launches per run, kit default 6, one line each in `.unattended.conf` and the example (`# resumes
this many times with no movement between them, then stops and says ATTEMPTS EXHAUSTED`);
`RESUME_TURNS` — the `--max-turns` a resumed session gets, kit default 40 (`# one resumed turn
budget; a run that needs more is resumed again by the next tick`). Both read by `read_bound_key`
with `attempts` and `turns` as the unit word, defaults named `RESUME_ATTEMPTS_DEFAULT` and
`RESUME_TURNS_DEFAULT` in the tick, never a literal digit in the call, from the ROOT conf sourced
into the tick's shell (unit 13); each comment line says the tick reads the root's copy. Two rows
in the protocol's section 8 table on `UNIT_STALL_BOUND`'s terms.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `resume-tick.sh` | kit file | no cell |
| `run_tick`, `scan_worktrees`, `read_liveness`, `check_login`, `run_kill_tree`, `run_detached`, `print_decision`, `derive_attempts` | function | `sh.function`, each leading with a declared verb; `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` answers OK for each |
| `read_host_name`, `read_pid_image`, `check_pid_alive` | function, in `lib-unattended.sh` (rev-5; the last MOVED from the driver) | `sh.function`, `--suggest` answers OK for each |
| `resume.<slug>.log`, `resume.<slug>.<utc>.sh`, `resume.<slug>.<utc>.out` | sidecar files | no cell |
| `RESUME_ATTEMPTS`, `RESUME_TURNS` | conf keys | no cell, conf is dark |
| `gov-resume-tick` | task name | no cell |
| ` · resume-tick <n> attempt(s), last <utc>` | status field | no cell |
| `read_bound_key` | function, MOVED to `lib-unattended.sh` | already graded |

### Files touched (estimate)

| path | change |
|---|---|
| `tools/unattended/resume-tick.sh` | new |
| `tools/unattended/resume-tick.test.sh` | new |
| `tools/unattended/lib-unattended.sh` | `read_bound_key` moved in, verbatim with its header comment; rev-5: `read_host_name`, `read_pid_image`, `check_pid_alive` |
| `tools/unattended/unattended.sh` | `read_bound_key` definition removed; the `--status` field |
| `tools/unattended/unattended.test.sh` | the `--status` field arm, region two |
| `tools/unattended/adopt-unattended.sh` | the INFO line |
| `tools/unattended/README.md` | the registration section |
| `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md` | two section 8 rows, re-rendered |
| `.unattended.conf`, `tools/unattended/.unattended.conf.example` | two keys |
| `tools/unattended/kit.toml` | `optional_keys` +2, `project-owned` +1 |
| `tools/run-gates/selftest-budgets.txt` | one row |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp |

### Alternatives rejected

- A driver verb — section 3.
- A second conf reader in the tick — the defaulted-validated-announced read would be spelled twice;
  the hoist is twelve lines moved and zero copied.
- `nohup … &` as the detach — section "The launch".
- A lifetime attempt cap — a run resumed six times over a long build would be dead on its seventh
  stall with nothing wrong; consecutive-fruitless is one `awk` comparison more and is right on that
  case.

## 5. Production-readiness checklist

- security — the tick launches `claude` with `--dangerously-skip-permissions` under the owner's
  own login, on a session id read from the INDEX blob of a tracked record (rev-5; rev-4 read the
  working copy of any file the glob found, so one file write bought a skip-permissions session
  ninety minutes later — closing review id 1, the blocker); a forged `session:` fact staged by an
  actor with shell access can only resume a session the owner's CLI can already open, and that
  actor is protocol section 9's concession. The payload is a fixed string plus the slug and a
  derived path; no record text is interpolated into it.
- perf / scale — one `git worktree list`, one grep per record, one driver run per bound record,
  every ten minutes; seconds. The launch is detached, so the task's own wall is the tick's.
- error / empty / loading states — no bound run, an unreadable tree, a dead liveness probe, a
  logged-out CLI and an exhausted cap each print their own line; nothing is silent and nothing
  resumes on a probe that answered nothing.
- observability — every decision is one line on the tick's stdout, every launch leaves its
  launcher and its `.out` beside the attempt line, and `--status` shows the count.
- risks — a false `STALE` from unit 2's clock, on a LOGGED-IN node, kills a healthy session's
  tree and resumes into it; the harm is duplicated work and a killed `Workflow`, bounded by
  `RESUME_STALE_BOUND`. A logged-out node kills nothing: the login row precedes the kill row, so
  the false-`STALE` harm there is one announced SKIP line. The
  parent transcript's movement during a long sidechain is UNVERIFIED. A hidden CLI flag can be
  withdrawn: a launch failing on `--max-turns` leaves `unknown option` in the `.out`, the attempt
  still counts, and `ATTEMPTS EXHAUSTED` names that file. `schtasks` runs the task only while the
  owner is logged on (research section 3.3).
- testing — section 6; every arm observes the tick over a scratch repo with a stub `claude`; no
  arm runs the real CLI.
- migration — N/A. Records without a `session:` fact are skipped by the grep; nothing rewrites
  them.
- user docs — the README's registration section here; the protocol, Skill and dossier prose are
  unit 6's.

## 6. Acceptance criteria

The tick's suite carries the arms and is on no bar leg; each criterion is observed by running the
tick over the suite's fixture directly. The fixture is a scratch `git init` repo under a short
`%TEMP%` path — never the scratchpad, whose length breaks a clone — with the driver suite's
`mkconf` shape plus `RESUME_STALE_BOUND="1"`, a `tRun` build README, a `RUN.md` at phase
`BUILDING` carrying `session: 11111111-2222-3333-4444-555555555555` and `pid: <n>`, one commit,
and a stub `claude` first on `PATH` that writes its argv and its own pid to `stub.log`, answers
`auth status` with `{"loggedIn": true}` or `false` from `STUB_LOGGED_IN`, and on `-p` sleeps 15 s.

- **AC1** — When the fixture's record has `pid: 999999999`, the tree is clean and its one commit is
  two seconds old, `bash resume-tick.sh --repo <fixture>` prints one line ending
  `resumed · attempt 1 · out <path>`, exits within 5 s while `stub.log` shows the stub still
  running, and `stub.log` carries `--resume 11111111-2222-3333-4444-555555555555`,
  `--dangerously-skip-permissions`, `--max-turns 40` and a payload token
  `--keepalive-id`; the sidecar's one line starts with a UTC stamp and carries `attempt 1`,
  `pid-alive no`; the launcher file exists beside it.
  Red when: the tick blocks until the stub exits, which means the launch was not detached; or the
  stub was never invoked, which means the decision table skipped `STALE`; or `stub.log` lacks the
  payload token, which means the payload lost its first instruction.
  fixture: the suite's scratch repo; `RESUME_STALE_BOUND="1"` and a two-second-old commit make it
  `STALE`; nothing in this tree is a live fixture.
- **AC2** — When the same fixture runs with `STUB_LOGGED_IN=false`, the tick prints
  `SKIP — the CLI is not logged in on this node; nothing can resume tRun`, exits 0, the stub's log
  shows `auth status` and no `-p`, and no sidecar line is written; when a file is touched under
  `<git-dir>/gate-logs/` first, the tick prints `skip · verdict LIVE` and consults neither login
  nor the stub.
  Red when: the logged-out answer launches anyway, which means the grep read the exit code; or the
  skip is silent; or a LIVE record probes login, which means the table's order is wrong. The
  logged-out arm with a LIVE recorded pid — the sleep survives — is unit 12's AC1.
- **AC3** — When the sidecar is pre-seeded with six lines dated after the fixture commit and the
  record is `STALE`, the tick prints `ATTEMPTS EXHAUSTED · last <utc>` and invokes nothing; when
  the six lines predate the commit, attempt 7 launches, because a move resets the count; and with
  five lines dated after the commit, attempt 6 launches.
  Red when: the seventh launch is refused, which means the cap is lifetime; or six lines dated
  before the last move skip; or five lines exhaust, which means the comparison is off by one.
- **AC4** — When the fixture starts `sleep 300` in the background, waits until `ps -p $!` names
  `sleep`, records that row's WINPID column as `pid:` and runs the tick, the tick prints
  `resumed`, the stub is invoked, and `tasklist //FI "PID eq <pid>"` afterwards prints its
  `No tasks are running` line; on a POSIX node the arm records `$!` and `kill -0` fails
  afterwards. Measured 2026-09-16: `ps -p` shows the forked child as `bash` under one WINPID
  before `exec` and as `sleep` under another after, which is why the arm waits.
  Red when: the sleep survives, which means the wrong pid namespace was killed or the kill arm was
  skipped on `pid-alive: yes`; or the tick resumed without killing.
  fixture: the arm's own background sleep; the Windows pid is read from `ps`, the MSYS pid is not
  the one `tasklist` knows.
- **AC5** — When `grep -c '^read_bound_key() ' tools/unattended/lib-unattended.sh` and the same over
  `tools/unattended/unattended.sh` are read at the tip, they print 1 and 0, and the driver's
  `read_bound_key ` call count is unchanged from this unit's base; and with the fixture conf
  declaring `GATE_BOUND="abc"`, `bash tools/unattended/unattended.sh --status tRun` still prints
  `which is not a positive integer of seconds` and exits 2, while a conf declaring no
  `RESUME_ATTEMPTS` makes the tick print `declares no RESUME_ATTEMPTS` on stderr once, naming the
  root conf's path after `Declare one in `, and act on the default of 6; the declared-key arms are
  unit 13's.
  Red when: the driver keeps a definition, which means the function was copied and the tick has a
  second reader; or the driver's refusal sentence changed bytes, which reds the existing bound arms;
  or the NOTE is absent, which means the tick read the key with a bare default.
  figure: the call count is DERIVED by grep at base and tip; 1 and 0 are the definition counts and
  are PINNED.
- **AC6** — When `git show --stat HEAD` of the pass commit is read, it lists `.unattended.conf`
  together with `memory/guides/SESSION-KICKOFF.md`; `grep -c 'RESUME_ATTEMPTS\|RESUME_TURNS'` over
  `tools/unattended/.unattended.conf.example` prints 2 and over `tools/unattended/kit.toml` prints
  1 — the `optional_keys` line — and the section 8 region of `memory/guides/UNATTENDED-PROTOCOL.md`,
  cut by `awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f'`, carries both keys; every count is 0 at
  base.
  Red when: the conf moved without the stamp, which `kickoff-manifest ratchet` reds at the close;
  or a key is declared in the example and absent from the table, which check 22 of the kit gate
  reds at the close and this grep sees now.
- **AC7** — When `bash resume-tick.sh --repo <fixture> --dry-run` runs over the AC1 fixture, it
  prints the `resumed` decision line with ` (dry-run)` appended, invokes nothing, kills nothing and
  writes no sidecar line and no launcher; and over a fixture with no bound record it prints
  `resume-tick: no bound run in 1 worktree(s)` and exits 0.
  Red when: dry-run launches or writes; or an empty walk exits silently.
- **AC8** — When `bash tools/check-install-prefix.sh --list` runs at the tip, it lists no row for
  `resume-tick.sh`, and `grep -c 'dirname "$0"'` over the tick file prints at least 1; and
  `bash resume-tick.sh --repo <a non-repo dir>` prints `REFUSED` naming the dir and exits 2.
  Red when: the tick spells a kit path, which the `install-prefix (shipped surface)` leg reds at the
  close; or a non-repo root walks nothing and exits 0.
- **AC9** — When the driver suite's `tRun` fixture gains a sidecar `resume.tRun.log` of two lines
  whose first tokens are UTC stamps, `bash tools/unattended/unattended.sh --status tRun` prints its
  one line carrying ` · resume-tick 2 attempt(s), last <the second stamp>`; with the sidecar
  removed the line is byte-identical to what it printed before this unit; `--resume tRun`'s first
  line carries the same field; and `grep -c 'rev-parse --git-dir' tools/unattended/unattended.sh`
  is unchanged from this unit's base, which is the read going through `resolve_sidecar_dir`.
  Red when: the field prints at zero, which grows every existing status line; it prints as a
  second line, which reds the arms that `sed` the whole `--status` output; or the count moved,
  which is a second spelling of the sidecar root and reds unit 11's check at the close.
- **AC10** — When `bash tools/unattended/adopt-unattended.sh --check` runs on node `a`, it prints
  one line beginning `unattended: INFO —` naming `gov-resume-tick` before its `in sync` line and
  exits 0 whether or not the task is registered; `schtasks //query //tn gov-resume-tick` on this
  node today answers `ERROR: The system cannot find the file specified.` and the INFO line reads
  `unregistered`; and `grep -c 'gov-resume-tick' tools/unattended/README.md` prints at least 2 —
  the Windows and the POSIX lines.
  Red when: an unregistered task reds `--check`, which reds `unattended skill wiring` at the close
  for every adopter; or the README names the task nowhere.
- **AC11** — When `python tools/lexicon/lexicon.py --check` runs at the tip, its `P1 verb` line
  reports `offenders=983`, the `VERB_OFFENDER_PIN` value in `.lexicon.conf`, and its
  `sh.function.conv` line reports 6 of the grown population; `grep -c 'resume-tick' tools/run-gates/selftest-budgets.txt`
  prints 1 and `grep -c 'resume-tick.test.sh' tools/unattended/kit.toml` prints 1, both 0 at base.
  Red when: a function in the tick or its suite leads with an undeclared verb, which moves the
  equality pin and reds `lexicon naming predicates`; or the suite arrives with no budget row, which
  the kit's gate runner reports as `OVER BUDGET … declares no ceiling`; or the suite ships to
  adopters because `project-owned` does not name it.
  figure: 983 and 6 are DERIVED from `.lexicon.conf` at observation and PINNED here as read on
  2026-09-16.
- **AC12** — When the fixture's driver is shadowed by a stub that prints a `unattended: NOTE`
  line on stderr and then exits 1 on `--liveness` with an `UNATTENDED check 52 FAILED` line, the
  tick prints `liveness probe failed:` with the CHECK line and not the NOTE, launches nothing and
  writes no attempt line; and when the fixture gains a second worktree by `git worktree add` with
  no `.unattended.conf` in it, the tick prints one skip line naming that tree and still prints its
  decision line for the first tree's run.
  Red when: a dead probe is read as a verdict and launches, which is the alternative §4 refuses;
  the diagnostic is the NOTE, which is rev-4's first-merged-line read; or a conf-less tree ends the
  walk early, which is a skip that skips everything after it.
- **AC13** — When AC1's launch has returned, the sidecar line ends `launched <pid>` with `<pid>`
  alive by `check_pid_alive`, and a second tick over the unmoved fixture prints one line ending
  `skip · IN-FLIGHT · launched <pid> alive since <utc>`, invokes nothing and writes no second
  line; and when the sidecar is seeded with one line stamped two hours ago carrying
  `launched <the WINPID of the arm's own sleep 300>`, the tick prints `resumed · attempt 2`, and
  `tasklist //FI "PID eq <pid>"` afterwards prints its `No tasks are running` line.
  Red when: the line carries no launched pid, which means the launch reported none; a second tick
  launches attempt 2 while the first is alive, which is rev-4's duplicate; or the sleep survives,
  which means a hung resumed session is never killed.
- **AC14** — When the fixture's tracked record reads `session: absent` and an UNTRACKED
  `memory/builds/tDrop/RUN.md` carrying a live session id and an hour-old mtime is dropped beside
  it, the tick prints exactly one line, `tDrop · <fixture> · skip · RUN.md is not tracked, and the
  tick launches only on a lease the index holds`, invokes nothing and writes no attempt line and no
  launcher; after `git add` of that record the same tick prints `tDrop · … · resumed · attempt 1`;
  and when the tracked `tRun` record's `session:` is rewritten ON DISK to a second id (mtime an
  hour old) the launcher carries the index's id and not the disk's.
  Red when: the untracked drop launches, which is rev-4's filesystem glob and the closing review's
  blocker; the staged record is skipped, which means the index read fails; or the launcher carries
  the working copy's id, which means the fact was read off the disk after all.
- **AC15** — When the fixture's record carries `pid: <the WINPID of the arm's own sleep>` and
  `host: some-other-node`, committed an hour old, the tick prints `skip · leased on
  some-other-node, not this node <read_host_name>`, exits 0, the sleep is still listed by
  `tasklist` afterwards, the stub saw nothing and no attempt line exists; with `host:` rewritten to
  this node's own name the same fixture prints `resumed · attempt 1` under `--dry-run`.
  Red when: the foreign lease is probed, killed or launched, which is a pid aimed at another node's
  process table; or this node's own name is refused, which means the writer and the reader spell
  the host differently.
- **AC16** — When the fixture's record is at `LANDING` with `witness: <the first commit's sha>`,
  committed an hour old with `GOV_DEFAULT_BRANCH=main` in the tick's environment, the driver reads
  `verdict: FINISHED-UNSTAMPED` and the tick prints `resumed · attempt 1`, writes the attempt line
  and the launcher; with a gate log touched five minutes ahead the same record prints `skip ·
  verdict FINISHED-UNSTAMPED`.
  Red when: the dead LANDING run is skipped by verdict, which is rev-4 and leaves the record
  unstamped forever; or a live one is resumed, which is `stale` ignored.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kickoff-manifest ratchet` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness`

These run once at `--close`. The pass runs none of them: it verifies with the tick and the driver
invocations section 6 names over a scratch repo, `python tools/lexicon/lexicon.py --check` and
`bash tools/check-install-prefix.sh --list`, each seconds. Under `unattended kit gate`, check 22 is
the join this unit moves.

New arm: `tools/unattended/resume-tick.test.sh` · every decision of section 4's table staged by
fixture — AC1 to AC4, AC7, AC8, the two announced skips of AC12, and from rev-5 AC13 to AC16 —
each observed red against the tick with the graded line commented out before the arm is trusted ·
a `FLOOR_ASSERTIONS` pin authored from the executed count of the first green run, the shape
`gate-guard.test.sh` carries.

New arm: `tools/unattended/unattended.test.sh` · the `--status` field with and without the sidecar,
AC9, region two beside the `--status` arms · the suite's executed-assertion floors rise by this
arm's assertions, read off the floor-breach line with the floor over-pinned.

## 8. Open questions

- **F1 — `--status`: a second line or a field.** The brief spells `resume-tick: <n> attempt(s), last
  <utc>|none` as a line. (a) A second stdout line after the status line. (b) A field on the
  existing line, omitted at zero, the shape `parked` and `noted` already take. The driver suite
  reads `--status` whole in two arms — `sed 's/.*· next //'` over every line, and a `grep -c`
  keyed on the first line — so (a) reds both on every fixture, and the verb's own header promises
  one line. Recommendation: (b).
  RESOLVED (agent, 2026-09-16, delegated): (b). (a) fails an existing arm, which is veto 1 applied
  to a gate already written; (b) satisfies every stated criterion and the `none` form the brief
  spelled is the omitted field.
- **F2 — the attempt cap: lifetime or consecutive.** (a) Every line in the sidecar counts. (b)
  Only lines newer than the run's last move count. (a) is the brief's literal reading and makes a
  run dead on its seventh stall over a long build; (b) is one comparison more and bounds what the
  cap is for, fruitless launches. Recommendation: (b).
  RESOLVED (agent, 2026-09-16, delegated): (b), the more feature-rich survivor with no new surface
  and no criterion failed; the transcript-only reset it admits is named as a ceiling in section 4.
- **F3 — the detach primitive under MSYS.** (a) `nohup … &` inside the tick's console. (b)
  `Start-Process -WindowStyle Hidden` through `powershell.exe`, a console of the child's own. (a)
  rests on an unmeasured property of the scheduler's console; (b) was measured to return in 0 s
  with the child alive. Recommendation: (b).
  RESOLVED (agent, 2026-09-16, delegated): (b). It needs nothing outside a stock Windows install,
  the fixture arm AC1 observes it directly, and (a) would leave AC1 resting on a fact nobody
  measured.

## 9. Revision log

- rev-5 · 2026-09-21 · S2 · S5 · S13 · §3 · §4 · §5 · AC12 · AC13 · AC14 · AC15 · AC16 · §7 ·
  folded the closing diff review round 1
  (`reviews/2026-09-21-review-TOOL-aWokenSentinel-1-diff-review-round1.md`), ids 1, 2, 3, 5 and
  16: id 1 (BLOCKER) — the tick globbed `RUN.md` off the worktree and honoured an untracked lease,
  so the walk reads `session:` and `host:` off the INDEX blob, announces an untracked record and
  launches nothing (S2, AC14; §3 names the file-write attacker closed and the staging attacker as
  section 9's concession); id 2 (HIGH) — the kill was aimed at a pid, so `--liveness` passes the
  lease's `pid-image` to the library's `check_pid_alive` and the tick stands off a foreign
  `host:` (S5, AC15; the facts are unit 1's rev-5, the match unit 2's rev-5, the reboot case unit
  12's record); id 3 — the launched pid rides on the attempt line and the next tick reads it back
  as in-flight or hung (S13, AC13; class `guard-fed-the-value-it-supersedes`); id 5 —
  `FINISHED-UNSTAMPED` with `stale: yes` acts (§4 table, AC16; spec 8 §3 points here for the dead
  half); id 16 — the dead-probe line is the driver's check sentence, never a NOTE (§4, AC12).
  Status unchanged, CLOSED.
- rev-4 · 2026-09-20 · §4 · the build pass: the launcher and `.out` file names carry the
  basic-format UTC stamp (no colons), because NTFS refuses `:` in a name and the launcher's path
  crosses into PowerShell; the attempt line's stamp is unchanged. Status CLOSED. Two readings
  recorded in the ledger rather than folded: AC5's driver call count is compared against the
  pass's parent (4), not the pinned base (3), because unit 2 landed the fourth call after the
  base; and the suite's stub dir is POSIX-spelled because a `C:/` element in PATH splits at the
  drive colon and lets the real CLI win — measured on node `a` the first time an arm ran. The
  pass's bug-class checklist named `bounded-through-a-pipe-is-unbounded` on the login probe, so
  its answer goes to a file under the sidecar and never through `$( )`, its liveness probe is the
  driver's measured `timeout -k 1s 10 true`, and the suite measures the tick's wall against a
  stub that leaves a sleeper on stdout.
- rev-3 · 2026-09-20 · §3 · §4 · folded spec-audit round 2: sibling agreement for the promoted
  `TOOL-aWokenSentinel-20` (H6, raw 36) and the rev-2 of spec 11 (M9, raw 50) — S4's resume-log
  root reads through the lib's `resolve_sidecar_dir` and the tick joins the one-derivation
  check's population; M6 (raw 26) — spec 9's `consumes-from` on this unit had no reciprocal, so
  the unit-9 `hands-off` is declared and the unit-7 absence bullet is dropped, the check-12 join
  reading a declared absence as an edge; a `hands-off` on the promoted `TOOL-aWokenSentinel-18`
  (H4, raw 4); and the two check-12 lines the round-2 record's M2 paragraph reports as seen on
  this spec — the `consumes-from` on unit 1 gains its reciprocal in spec 1's rev-3, and spec 4's
  `hands-off` on this unit is dropped there, because the tick acts on `--liveness`'s verdict alone
  and never opens the stall sidecar. Order 9 → 11 for the insertions of units 20 and 16.
- rev-2 · 2026-09-20 · S12 · S3 · S5 · S8 · §3 · §4 · §5 · AC2 · AC5 · AC9 · AC12 · §7 · folded
  spec-audit round 1: L1 (raw 10) — the walk's two announced skips had no criterion, so S12 and
  AC12 observe them. Sibling agreement for the promoted units: the `--status` hands-off names unit
  9's field, not a second line from unit 7 (H1); S8 and AC9 read the resume log through
  `resolve_sidecar_dir` and consume unit 11's check (H3); the decision table's login row precedes
  the kill row and §5's risk row says a logged-out node kills nothing, proof handed to unit 12
  (H4); the walk sources the root conf into the tick's shell with `CONF` set before the bound
  reads, root-scoped, proof handed to unit 13 (H5). Order 5 → 9.
- rev-1 · 2026-09-16 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resume a stalled unattended run from an OS-scheduled
tick outside the session process"` returned no shell seam — its header prints `unscanned layers:
.sh` — and one relevant Python hit: `run_kill` in `tools/process-monitor/reap.py`, the per-row
tree reaper. It was read and NOT taken: a kit file names nothing outside itself by literal, that
kit is a sibling, and routing through it would put a Python launch inside a ten-minute tick; its
header's measurement of `taskkill /T` is cited in section 4 as this unit's known ceiling instead.
The seams this unit extends were found by reading the driver and are cited by line: `read_bound_key`
at `tools/unattended/unattended.sh:358`, hoisted into `tools/unattended/lib-unattended.sh` beside
`pass_commit` at `:164`; the `parked`/`noted` field rule in `verb_status` at `:2890`; the adopter's
`--check` tail at `tools/unattended/adopt-unattended.sh:432`; and the sibling-derivation preamble of
`tools/unattended/gate-guard.test.sh:24`. One disagreement with the brief, settled by source: it
names `run_bounded` at `:183` as a seam, and that function reads two driver globals the tick does
not have, so the tick bounds its one call inline (section 3). The memory-recall hits
`TOOL-aPromptedMandate-11` and `TOOL-aReapedSpinner-10` are the measured facts behind the tree
kill and the attestation this unit's payload no longer trusts.

Recall terms used: `resume process death cross-node takeover claude -p transcript session id schtasks tick attempts kill tree detached login`
