# TOOL-dGroundRules-88 — packet.py's `--repin` guard admits an owner at a console inside a live chain run, refuses every agent and unattended caller, and records the admitted repin in each packet's Pins

**Status:** DEFERRED · rev-1 · 2026-10-25 · node d · Tier-2 · base 87917c2f · streams tooling · order 34

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-88-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-88-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-88-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-88-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`packet.py --repin` refuses inside a chain run by tree state alone, so it refuses the owner exactly
as it refuses an agent. While a chain run is open, any fix to a pinned instrument leaves a stale pin
that nobody may move, and the run cannot close. This unit keys the guard on the caller when a chain
run is live. It admits an owner at a console and refuses every agent and every caller it cannot
classify. The first render stays refused inside a chain run, and the admitted repin is written into
each packet it rewrites, so it is visible on the record.

In this spec, `packet.py` is
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py`.

## 2. Scope (IN)

- **S1** — The caller test. `derive_caller(env, tty, answer)` in `packet.py` returns
  `(kind, why)`, where `kind` is `owner`, `agent` or `unknown`. It reads nothing but its arguments
  and decides in this order, and the first match wins:
  1. Any name in `AGENT_MARKERS = ("AI_AGENT", "CLAUDECODE")` is present in `env`, at any value
     including the empty string. The result is `agent`, and `why` is
     `an agent's call (<names> set in its environment)`, the present names comma-joined.
  2. `tty` is false. The result is `unknown`, and `why` is
     `no terminal on stdin, so no owner typed this (refused by default)`.
  3. `answer()`, stripped, is not `yes`. The result is `unknown`, and `why` is
     `the owner's confirmation was not typed (want yes; refused by default)`.
  4. Otherwise the result is `owner`, and `why` is
     `an owner at a console: no agent marker, a terminal on stdin, and yes typed`.
  `answer` is called at step 3 and nowhere else, so an agent caller and a caller with no terminal
  are never prompted. Observed by AC1.
- **S2** — The guard in `cmd_repin`. When `scan_live_run` returns a non-empty list, `cmd_repin`
  calls `derive_caller(os.environ, sys.stdin.isatty(), <reader>)`, where the reader is
  `read_confirmation(name, live)`. That function prints
  `packet: --repin <name> inside the live chain run <live>; type yes to move the pin in every chain packet: `
  and returns the line typed, or `""` at end of input. For any kind but `owner`, `cmd_repin`
  raises `Refusal` with
  `--repin is the owner's, and inside a chain run only an owner at a console runs it: <why>: <live>`,
  before anything is written. With no live chain run, `cmd_repin` asks nothing and runs as it does
  at base. `render_packet`'s first-render refusal is unchanged. Observed by AC2, AC3.
- **S3** — The record. A repin the guard admits inside a live chain run writes one line into the
  `### Pins` section of every packet `cmd_repin` rewrites. The line sits after the instrument lines
  and before `rendered at`, and reads:
  `` - repinned inside a live chain run: `<instrument>` blob `<blob>` at `<HEAD>` by an owner at a console, over <live> ``
  where `<live>` is `scan_live_run`'s list joined by `; `.
  - `REPIN` is the regex for that line, and `read_repins(text)` returns
    `{instrument: (blob, head, over)}` from a packet's Pins section.
  - `render_text(src, pins, at, repins=None)` renders a record, in `INSTRUMENTS` order, only while
    its blob equals that instrument's pin. A later repin that moves the pin leaves the record out
    of the render, with no code for it in `cmd_repin`.
  - `render_packet` and `cmd_check` pass `read_repins` of the packet they read, so `--write` and the
    byte compare carry the record as they carry the pins.
  - `cmd_repin` passes the packet's records with this instrument's entry set to the new one when the
    guard admitted the repin inside a live chain run.
  - Before its per-packet lines, `cmd_repin` prints once:
    `packet: owner repin inside a live chain run, recorded in each packet's Pins: <live>`.
  Observed by AC4.
- **S4** — The plants. `PLANTS` gains `run-live-owner`, `run-live-agent` and `run-live-detached`.
  Each runs over the `run-live` tree, a chain build's `RUN.md` at `BUILDING`, and calls
  `derive_caller` with a fixed caller:

  | Plant | `env` | `tty` | `answer` |
  |---|---|---|---|
  | `run-live-owner` | `{}` | true | returns `yes` |
  | `run-live-agent` | `{"AI_AGENT": "claude-code_0-0-0_agent"}` | true | raises |
  | `run-live-detached` | `{}` | false | raises |

  - `run-live-agent` and `run-live-detached` print `--repin refused: <why>: <live>` and exit 1.
  - `run-live-owner` prints `--repin admitted: <why>`. It then renders the packet with every
    instrument pinned at HEAD and a record for `SELF`, and runs `check_text` over that render against
    its re-render through `read_repins`. It renders once more with `SELF`'s pin moved by one byte, as
    the `pin` plant moves `carries.py`'s. The line ends
    `· <check_text summary> · record read back: <yes|no> · record once the pin moves: <none|kept>`,
    then one line per finding. It exits 0 only when the check finds nothing, the record reads back,
    and the moved render carries no record.
  - The five existing plants `run-live`, `run-landed`, `run-pushed`, `run-unpushed` and `run-dirty`
    pass `run-live-agent`'s caller through the guard. Each prints the line it prints at base and
    exits as it does at base.
  Observed by AC4, AC5, AC6.
- **S5** — The docstring.
  - The `--repin` usage entry (`packet.py:46-47`) says that inside a chain run it admits only an
    owner at a console.
  - The plant list (`packet.py:53-56`) names the three plants.
  - The guard paragraph (`packet.py:57-60`) becomes two sentences. A first render refuses inside a
    chain run. Inside a chain run `--repin` admits only an owner at a console: no `AI_AGENT` or
    `CLAUDECODE` in its environment, a terminal on stdin, and `yes` typed at the prompt. Any other
    caller is refused, and one it cannot classify is refused by default. The LANDING sentence is
    unchanged.
  - "What it does not check" (`packet.py:64-69`) gains a caller that unsets both markers and types
    through a pseudo-terminal, which the caller test cannot tell from the owner.
  Observed by AC7.

## 3. Non-goals (OUT)

- `carries.py` and its batching, ask TOOL-dGroundRules-112.
- The first-render refusal in `render_packet` (`packet.py:614-616`). A first render pins every
  instrument, and it stays refused inside a chain run for every caller.
- The pin arm's grading, `check_pins` (`packet.py:475-480`), and the byte compare in `check_text`.
  Both are unchanged. Only the text they are handed carries the record.
- Any other instrument under `memory/builds/dClosedLoop/build/`, and `open.py`, whose calls of
  `render_packet`, `cmd_check` and `scan_packets` keep their signatures.
- A hook arm. `tools/hooks/scratch-guard.js` and `tools/unattended/gate-guard.js` are not touched.
  §4 "Alternatives rejected" says why.
- `--repin` with no live chain run. It keeps its base behaviour for every caller, so the execution
  plan's practice of dClosedLoop's session repinning on the owner's ask still runs there.
- dClosedLoop's landed records: the execution plan's `--repin` paragraph
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:356-358`)
  and the Phase 0 decision rows. They are frozen records and outside this build's writes.
- The 22 chain packets. The owner's repin rewrites them after the build commit, not this unit's
  pass (§4 "Rollout").

### Edges

- **consumes-from** external — `scan_live_run`, `read_landed_derivation` and the five `run-*` plants as they stand at base `87917c2f`, PLAY-dClosedLoop-26's guard; this unit adds the caller test after them and changes neither predicate
- **hands-off** external — the owner's `packet.py --repin packet.py`, from a console after this unit's build commit and before the close's bar; until it runs, `packet.py --check dGroundRules` and the spec tokens leg's packet join are red on `packet.py`'s own pin

## 4. Design

### Evidence

Measured 2026-10-25 at `87917c2f`, from this run's worktree.

- **The guard decides by tree state.** `scan_live_run` (`packet.py:541-556`) lists each chain
  build's `RUN.md` whose last `phase:` line is not terminal. `cmd_repin` (`packet.py:660-664`)
  refuses whenever that list is non-empty. No line of `packet.py` reads `os.environ` beyond
  building `UTF8` (`packet.py:109`).
- **The run is live while HELD.** `memory/builds/dGroundRules/RUN.md` carries `hold-code:
  owner-decision`, `held-from: VERIFYING` and a last `phase: VERIFYING`, so the guard reads it as
  live.
- **Today's refusal.**
  `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --repin packet.py`
  exited 1 in 8.6 s with
  `packet: refused: --repin is the owner's, and never runs inside a chain run: memory/builds/dGroundRules/RUN.md (phase VERIFYING)`.
  It wrote nothing.
- **The plants at base**, each `--fixture --plant <case>` over the default build:

  | Plant | Exit | Line after `· plant <case> · ` |
  |---|---|---|
  | `run-live` | 1 | `--repin refused: memory/builds/dTrueNorth/RUN.md (phase BUILDING)` |
  | `run-landed` | 0 | `--repin not refused: no live chain run` |
  | `run-pushed` | 0 | `--repin not refused: no live chain run` |
  | `run-unpushed` | 1 | `--repin refused: memory/builds/dTrueNorth/RUN.md (phase LANDING: its landing commit <sha8> is not on refs/heads/main at <sha8>)` |
  | `run-dirty` | 1 | `--repin refused: memory/builds/dTrueNorth/RUN.md (phase LANDING: the LANDING record is not committed as it stands, so no commit carries it to any remote)` |

  `run-unpushed`'s two shas come from the scratch clone each run makes, so they differ per run.
- **This tool shell's environment.** It carries `AI_AGENT=claude-code_2-1-308_agent`,
  `CLAUDECODE=1`, `CLAUDE_CODE_SESSION_ATTENDED=1`, and a `CLAUDE_CODE_SESSION_ID` equal to the
  `session:` fact in dGroundRules' `RUN.md`. The shell is a subagent's, and its session id is its
  parent's. Its stdin is not a terminal.
- **Windows reads NUL as a terminal.** With this node's Python 3.14.6,
  `python -c "import sys; print(sys.stdin.isatty())" < /dev/null` prints `True`, because NUL is a
  character device. The same call fed by a pipe, and the tool shell's own stdin, print `False`. A
  bare `isatty` test therefore admits an agent that unsets the markers and appends `< /dev/null`,
  which agents do routinely to keep a command from waiting. Step 3 of S1 closes that, since NUL
  answers end of input.
- **The pin goes stale on the build commit, twice over.** dGroundRules' packet pins `packet.py` at
  blob `20a7319cfe49`, its blob at base. `derive_sources` takes the generator's version line from
  `read_head_blob(SELF)` (`packet.py:274`). So once the build commit moves the blob,
  `packet.py --check dGroundRules` reds on the pin arm and on the byte compare. The spec tokens
  leg's packet join runs that check for every live chain run
  (`tools/check-spec-tokens.py:1381-1411`), so the leg reds as well.
- **Every packet is rewritten.** 22 chain packets are tracked, one per chain build, and `cmd_repin`
  rewrites each one (`packet.py:670-683`).

### Where this repository tells an owner from an agent today

| Seam | What it keys on | Why it cannot be the test here |
|---|---|---|
| scratch-guard's role arms (`tools/hooks/scratch-guard.js:1168`) | the hook payload's `agent_type` | The main loop carries none (`tools/hooks/scratch-guard.js:96-97`), and an unattended run is a main loop, so it cannot tell the run from an owner's session. A Python process never sees the payload. |
| gate-guard's question arm and `run-lease.js` (`tools/unattended/gate-guard.js:48-52`, `tools/unattended/run-lease.js:21`) | the payload `session_id` against a record's `session:` fact | It binds the run's own lease session only. Any other agent session is not that run and would be admitted, which fails deny-by-default. |
| `read_cli_version` (`tools/unattended/unattended.sh:8931-8942`) | `AI_AGENT` | It reads the version, not presence. Its comment records the fact S1 rests on: the Claude Code CLI sets `AI_AGENT` from its own version, overwriting an inherited one. |
| the unattended kit's owner-only grants (`tools/unattended/unattended.sh:4159-4167`) | provenance: a slug-mode README the owner committed at the default-branch anchor | That is a commit-time fact about authorship, not about who invokes a command now. |
| `tools/check-template-size.sh:269` | nothing | "Raising the limit is the owner's decision" is message prose. No caller test runs. |
| `tools/run-gates/run-gates.sh:2201-2268` | a process id | "owner" there is the scratch directory's owning bar process, not a person. |

S1 therefore extends the `AI_AGENT` fact that `read_cli_version` already relies on, read for
presence, together with the `CLAUDECODE` marker this shell carries. It adds the console test and
the typed confirmation, because no existing seam gives positive evidence of an owner. It is a new
predicate in Python inside a dClosedLoop instrument, and not a second copy of a shell reader, so
there is no factory to extract.

### The caller test and the guard

```
AGENT_MARKERS = ("AI_AGENT", "CLAUDECODE")   # set in every tool shell Claude Code starts

def derive_caller(env, tty, answer):        # -> (kind, why); answer is called at step 3 only
    found = [k for k in AGENT_MARKERS if k in env]
    if found: return "agent", f"an agent's call ({', '.join(found)} set in its environment)"
    if not tty: return "unknown", "no terminal on stdin, so no owner typed this (refused by default)"
    if answer().strip() != "yes": return "unknown", "the owner's confirmation was not typed (want yes; refused by default)"
    return "owner", "an owner at a console: no agent marker, a terminal on stdin, and yes typed"

cmd_repin(name):
    live = scan_live_run(chain, read_file)
    if live:
        kind, why = derive_caller(os.environ, sys.stdin.isatty(), lambda: read_confirmation(name, live))
        if kind != "owner": raise Refusal(<S2's text>)
    <resolve, blob, packets as at base; when live, each packet's records gain this instrument's>
```

A marker counts by presence, so an empty value is still an agent. That is the deny direction, and
Claude Code never sets either marker empty. The prompt names the instrument and every live run, so
the owner sees what the repin moves and which run it moves it inside. `read_confirmation` returns
`""` on `EOFError`, which is what NUL and a closed stdin give.

### The record

The record goes in the packet because that is the file the act writes, and it already holds the
state an owner moves, the pins, carried across renders. Every session reads the packet in the build
method's reading order (step 4 of the packet's own Reading order). Every landing diff of a repin
shows it beside the pin line it explains, and the owner's landing-diff check is where the
docstring already places the guard against a hand edit of a pin line (`packet.py:67-68`).

| Fact | Value |
|---|---|
| Where | the `### Pins` section of every chain packet the admitted `--repin` rewrites, after the instrument lines |
| Shape | one line per instrument, matched by `REPIN`: instrument, the blob it set, the HEAD it ran at, and the live runs it ran inside |
| Lifetime | rendered while its blob is that instrument's pin, and left out of the render once a later repin moves the pin |
| Read by | every session reading the packet; the Tier-2 review of the landing diff; `--write` and `--check`, which carry it through `read_repins` |

### What stays as it is

- `scan_live_run`, `read_landed_derivation` and the LANDING derivation. The caller test runs after
  them and only when they report a live run.
- The first render. `render_packet` refuses inside a chain run for every caller.
- `check_pins` and the byte compare. A packet whose record matches its pins re-renders to the same
  bytes.
- The five `run-*` plants' lines and exits (S4).

### What it does not see

- **Deliberate evasion.** A caller that unsets both markers and types `yes` through a
  pseudo-terminal is admitted. Like scratch-guard's arms, this guard stops forgetting, not evasion
  (`tools/hooks/scratch-guard.js:63`). The record then puts the repin in the landing diff.
- **The owner inside Claude Code.** Whether the shell behind Claude Code's `!` prompt carries the
  markers is UNVERIFIED. If it does, the owner is refused there with the marker named, and runs the
  command from a console instead.
- **mintty.** That a native Windows Python under Git Bash's mintty, without `winpty`, sees stdin as
  a pipe is UNVERIFIED on this fleet. If it does, the owner is refused with `no terminal on stdin`,
  and the remedy is PowerShell, Windows Terminal or `winpty python`.
- **A hand-written record line** renders like the guard's, exactly as a hand-edited pin line does.
- **Outside a chain run** there is no caller test, as at base.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_caller` | py.function | `packet.py` |
| `read_confirmation` | py.function | `packet.py` |
| `read_repins` | py.function | `packet.py` |
| `AGENT_MARKERS` | module constant | `packet.py` |
| `REPIN` | module constant, a regex | `packet.py` |
| `repins` | keyword parameter of `render_text`, default `None` | `packet.py` |
| `run-live-owner`, `run-live-agent`, `run-live-detached` | fixture plants in `PLANTS` | `packet.py` |
| `- repinned inside a live chain run:` | packet line prefix | `### Pins` |
| `only an owner at a console runs it` | refusal text, S2 | `cmd_repin` |

`lexicon.py --suggest <name> --as py.function` answered OK on 2026-10-25 for `derive_caller`,
`read_confirmation` and `read_repins`. The lexicon declares no `py.constant` cell.

### Files touched (estimate)

- `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py`

### Rollout

1. The build pass declares its write with the driver's dispatch verb, below. A dispatched write is
   the README's admitted exception to "writes stay in this build's folder".

   ```
   bash tools/unattended/unattended.sh --dispatch dGroundRules --pass TOOL-dGroundRules-88 --writes memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py
   ```

2. The build commit moves `packet.py`'s blob. From then until step 3,
   `packet.py --check dGroundRules` is red on its pin arm and byte compare, and so is the spec
   tokens leg.
3. **The owner action this unit leaves.** The owner works from a console: PowerShell or Windows
   Terminal, not Claude Code's `!` prompt and not a mintty window without `winpty`. At the run
   worktree's root, on the build commit, the owner runs the command below and types `yes`:

   ```
   python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --repin packet.py
   ```

   The guard admits it inside dGroundRules' live run. It sets `packet.py`'s pin to its new blob in
   all 22 chain packets, writes the record, and re-renders each packet at HEAD. This unit touches no
   other instrument, so no other repin is owed.
4. A records commit of the 22 packets follows. The main loop may make it, because the repin was the
   owner's act and the commit only carries its output. `packet.py --check dGroundRules` is then
   green, and the close's bar runs after that.
5. A later fold that edits `packet.py` again owes step 3 again.

TOOL-dGroundRules-87 shares order 34 and touches only `tools/gate-legs.json`. The two units are
disjoint, and neither consumes the other.

### Alternatives rejected

- **The tree-state guard with an owner override flag.** Any caller can type a flag, so it is a
  bypass rather than a test.
- **`agent_type` from the scratch-guard payload.** The run's main loop carries none, and the
  instrument never sees the payload.
- **The session match `run-lease.js` makes.** It names only the run's own session. Another agent
  session is admitted, so the test is not deny-by-default.
- **`CLAUDE_CODE_SESSION_ATTENDED`.** It reads `1` in this unattended run's own tool shell, so it
  cannot tell a run from an attended owner.
- **The marker test alone.** A scheduled task, a CI runner or a script carries no marker, and this
  version would admit them. Deny-by-default needs positive evidence of an owner.
- **Markers plus `isatty`, with no confirmation.** On Windows, `< /dev/null` reads as a terminal
  (§4 "Evidence"), so a marker-stripped call that forgot nothing else would pass.
- **A refusal arm in a PreToolUse hook.** It is textual and fails open, and it sees only an agent's
  tool calls. It would put a second mechanism in a shipped kit, with a version bump, for a guard
  that lives in this instrument.
- **The record in the live run's `RUN.md`.** The unattended driver owns that file's grammar, and its
  check parses the parked region line by line.
- **The record as a parked decision through `--park`.** A park is a decision the close surfaces to
  the owner, and this is an act the owner already took.
- **A separate repin log file.** No reader reads it, so it is write-only.
- **Stdout only.** Nothing durable remains, which is the silent repin the brief rules out.

## 5. Production-readiness checklist

- security — the guard narrows who moves a pin inside a chain run from nobody to an owner at a
  console, and refuses every other caller, an unclassifiable one by default. It is a guard against
  forgetting, and §4 "What it does not see" states the evasion it cannot stop. The refusal prints
  marker names and never their values. No new write path: the record rides the packet write
  `cmd_repin` already makes.
- perf / scale — one environment read and one `isatty` call per `--repin` inside a live run, and
  one prompt for a console caller. Rendering adds at most one line per instrument, seven at most.
- error / empty / loading states — end of input, an empty line and any answer but `yes` refuse. A
  packet with no record renders exactly as at base. A record whose blob is not the current pin is
  left out of the render, and is never an error.
- observability — the refusal names the caller class and the live runs. An admitted repin prints
  one line naming the runs and writes the record into every packet it rewrites.
- risks — the owner may be refused from Claude Code's `!` prompt or from mintty (both UNVERIFIED),
  and each refusal names its remedy. A deliberate evader is admitted and recorded.
- testing — AC1 to AC7, and the three plants on the §7 `New arm:` lines.
- migration — none. A packet with no record line is valid, and `render_text`'s new parameter
  defaults to none.
- user docs — the instrument's docstring (S5). No page under `help/` covers the dClosedLoop
  instruments.

## 6. Acceptance criteria

Every criterion runs from the root of the pass's worktree, in the pass's own tool shell, after the
build edit. BEFORE means the same command against `packet.py` at base `87917c2f`.

- **AC1** — When `python -c "import importlib.util as u; s = u.spec_from_file_location('p', 'memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py'); m = u.module_from_spec(s); s.loader.exec_module(m); y = lambda: 'yes'; z = lambda: 1 / 0; print([m.derive_caller(e, t, a)[0] for e, t, a in [({}, True, y), ({}, True, lambda: ''), ({}, False, z), ({'AI_AGENT': 'x'}, True, z), ({'CLAUDECODE': '1'}, True, z), ({'AI_AGENT': ''}, True, z)]])"`
  runs, it prints `['owner', 'unknown', 'unknown', 'agent', 'agent', 'agent']` and raises nothing.
  Red when: the marker test reads `env.get(k)` rather than presence, so the sixth case prints
  `owner`; or the answer is read before the marker and terminal tests, so a `z` case raises
  `ZeroDivisionError`; or an empty answer reads as consent, so the second case prints `owner`.
- **AC2** — When `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --repin packet.py`
  runs, it exits 1 printing `refused: --repin is the owner's` with `an agent's call` and
  `AI_AGENT` on the same line. Then `git status --short -- "memory/builds/*/prompts/*-packet.md"`
  prints nothing. BEFORE, it exits 1 with no `an agent's call`.
  Red when: the guard admits an agent's call inside a live chain run and a packet changes, or
  refuses it without naming the caller class.
  fixture: the tree holds `memory/builds/dGroundRules/RUN.md` at a non-terminal last phase, measured
  `VERIFYING` on 2026-10-25, and the pass's shell carries `AI_AGENT` and `CLAUDECODE`.
- **AC3** — When `env -u AI_AGENT -u CLAUDECODE python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --repin packet.py < /dev/null`
  runs, it exits 1 printing `refused by default`, and AC2's `git status` prints nothing. BEFORE, it
  exits 1 with no `refused by default`.
  Red when: the staged break of a guard that tests `isatty` with no confirmation admits it, because
  Windows reads NUL as a terminal, and the repin writes every packet.
  fixture: AC2's live `RUN.md`. On this fleet NUL takes the confirmation path, and on a POSIX node
  `/dev/null` takes the no-terminal path; both print `refused by default`.
- **AC4** — When `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --fixture --plant run-live-owner`
  runs, it exits 0 printing `--repin admitted: an owner at a console`, `byte compare green`,
  `record read back: yes` and `record once the pin moves: none`, with no finding line. BEFORE, it
  exits 2 with argparse's `invalid choice`.
  Red when: `render_text` leaves the record out while its blob is the pin, so the byte compare reds
  and `record read back: no`; or it keeps the record once the pin moves, printing `kept`; or
  `REPIN` reads a shape the renderer does not write.
- **AC5** — When `python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --fixture --plant run-live-agent`
  runs, it exits 1 printing `--repin refused: an agent's call (AI_AGENT set in its environment)`.
  With `--plant run-live-detached` it exits 1 printing
  `--repin refused: no terminal on stdin, so no owner typed this (refused by default)`.
  Red when: either plant is admitted, or either one prompts, which the raising answer turns into a
  traceback.
- **AC6** — When `for c in run-live run-landed run-pushed run-unpushed run-dirty; do python memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --fixture --plant $c; echo "exit $?"; done`
  runs, each plant prints the line and exit §4 "Evidence" tabulates at base, `run-unpushed`'s two
  shas aside.
  Red when: the agent caller these plants now carry changes a verdict or a line, for example a
  `run-live` that prints the caller's reason or exits 0.
  cost: `run-pushed`, `run-unpushed` and `run-dirty` each make a scratch remote and clone, a few
  seconds each.
- **AC7** — When `grep -c "admits only an owner at a console" memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py`
  runs, it prints at least `2`, for the usage entry and the guard paragraph. Then
  `grep -c "A first render and --repin refuse inside a chain run" memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py`
  prints `0`, and
  `grep -c "cannot tell from the owner" memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py`
  prints `1`.
  Red when: the docstring still says `--repin` refuses inside every chain run, or leaves the
  caller test's evasion ceiling unstated.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy fixtures` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

`policy fixtures`, `recall floor` and `recall floor arms` are the legs `derive_guarded_legs` joins to
the one file under §4 "Files touched", as `check-spec-tokens.py --legs-for` printed on 2026-10-25.
`spec tokens (a spec's own names resolve)` runs the packet join, which this unit reds until the
owner's repin. `lexicon naming predicates` grades the new function names in the dClosedLoop
instruments.

New arm: memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --fixture --plant run-live-owner · covers AC4 · red at base, where the plant is no choice and argparse exits 2; staged, a render_text that leaves the record out reds its byte compare · none
New arm: memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --fixture --plant run-live-agent · covers AC5 · red at base, where the plant is no choice; staged, a guard that skips the marker test reaches the raising answer and tracebacks · none
New arm: memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py --fixture --plant run-live-detached · covers AC5 · red at base, where the plant is no choice; staged, a guard that skips the terminal test reaches the raising answer and tracebacks · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft from the owner-ordered rescope add row for this unit in
  dGroundRules' `RUN.md` and its spec brief, grounded at base `87917c2f`:

  ```
  memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-88-spec-brief.md
  ```

  The brief numbers the sections as the Tier-1 profile does. This spec is Tier-2 as the brief
  directs, so the brief's acceptance rules apply to §6, its gate-leg rule to §7, and its open
  questions rule to §8. A follow-up for whoever next edits TOOL-dGroundRules-112: that ask says the
  owner repins `carries.py` while no chain run is live, "since `--repin` refuses inside one". Once
  this unit lands, an owner at a console may repin inside a live chain run, so the ask's cure no
  longer waits on a run-free window. Its text is the ask's to change, outside this unit.

## 10. Reuse audit

The seam extended is the `AI_AGENT` fact `read_cli_version` already relies on
(`tools/unattended/unattended.sh:8931-8942`, TOOL-aMendedFleet-61): the Claude Code CLI sets it in
every session's shell, overwriting an inherited one. This unit reads it for presence, beside
`CLAUDECODE`, inside the guard PLAY-dClosedLoop-26 left in `scan_live_run` and `cmd_repin`, which it
extends rather than duplicates. The probe
`python tools/codebase-map/reuse_lookup.py "tell the owner's own invocation from an agent or unattended session's caller and refuse the agent"`
ranked name stems only (`refus`, `invoc`, `ses`, `own`, `agent`): `CensusRefused`,
`build_invocations`, `extract_session`, `owners_of`, and the harness hooks `agent-cap.js`,
`gate-guard.js` and `stop-guard.js`. None of the symbols classifies a caller. The two hooks key on a
hook payload a Python process never sees, as §4's seam table records with the other four sites
read. So no existing seam fits the positive owner test, and the console test and the typed
confirmation are new. The recall probe returned PLAY-dClosedLoop-26 and PLAY-dClosedLoop-27, the
guard's last change and its decision row, whose LANDING derivation this unit keeps. It also returned
ask TOOL-dGroundRules-112, which this unit does not close, and TOOL-dGroundRules-63, the packet join
that reds while the pin is stale.

Recall terms used:
`python tools/memory-recall/query.py "packet repin guard admits the owner and refuses an agent inside a live chain run" --terms "repin packet owner agent caller chain run live guard AI_AGENT CLAUDECODE terminal confirmation unattended"`
