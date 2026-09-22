# TOOL-dDerivedDocket-65 — a session waiting on its own sub-agents, a move the liveness clock sees

**Status:** SPECCED · rev-1 · 2026-09-22 · node d · Tier-2 · base 67d2ccfc · streams tooling · order 35

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

While an orchestrating session waits on a background Workflow, no signal `--liveness` reads moves in
its run worktree. Its own transcript sits still, and its sub-agents append to transcripts under
`<sid>/subagents/`, which the transcript term never reads. Once unit 61's Rollout records this
build's session, a wave that outlasts `RESUME_STALE_BOUND`, 5400 s in gov, with no orchestrator
commit reads STALE in the one worktree `TOOL-dDerivedDocket-62` lets act, and the resume tick would
kill the orchestrator with its Workflow. That is H1 of
`memory/builds/dDerivedDocket/reviews/2026-09-22-review-TOOL-dDerivedDocket-62-spec-audit-g9-round1.md`.
Here `derive_last_move` gains one term, the newest sub-agent transcript of the recorded session, so
a session waiting on its own sub-agents is a move.

## 2. Scope (IN)

- **S1** `derive_last_move`, as unit 61 S3 extracts it and unit 64 S3 extends it, gains a last term
  after the transcript term. When the transcript derived, `LM_TRANSCRIPT` with `.jsonl` stripped
  names the session's directory, and the term reads every `agent-*.jsonl` at any depth under its
  `subagents/`. ONE `stat -c %Y` spawn dates them all, and a reading newer than the newest move so
  far takes it with source label `subagent`, compared with `-gt` as every term is. No transcript, no
  `subagents/` directory and no matching file each contribute nothing. Fewer numeric readings than
  matched paths is a dead probe named `stat -c %Y over <dir>`, which reaches the existing `fail 52`.
  `--liveness` prints no new key. Observed by AC1, AC2, AC3 and AC4.
- **S2** The driver's `--liveness` header and the signals comment inside `derive_last_move` name the
  term, its population and the bound it honours (§4), naming the run-log kit's reader of the same
  layout by role and not by path. No capped carrier is edited: after unit 64 S4 no carrier
  enumerates the signals, and this unit adds no conf key, so no protocol key-table row is owed.
  Observed by AC6.
- **S3** The suite arms follow the code, each staged RED. The driver suite gains the term in its
  `--liveness` signals block and over unit 61's AC20 fixture, and the resume-tick suite gains a
  record whose only fresh signal is a sub-agent transcript. Each suite's `FLOOR_ASSERTIONS`, and the
  driver suite's `FLOOR_SHARD_2` beside it, rises by exactly the assertions its new arms carry,
  counted off their blocks and never read off a run; the driver arms are written in region two, so
  `FLOOR_SHARD_1` does not move. Observed by AC5.
- **S4** The unit's hygiene: no kit version moves, no added line in a shipped kit file spells a
  `tools/<kit>/` literal, no function is minted and no `fail` branch is added. Observed by AC6.

## 3. Non-goals (OUT)

- A session silent past the bound for another reason: one tool call longer than it, or a wait on a
  background shell task that is not the bar. Neither writes a sub-agent transcript. Where that task
  writes its output was not measured. This is the class of unit 61's §5 risk (2), and unit 64 hands
  its running-bar half off external.
- The wave worktrees' own clocks. Unit 62's route (a) discards them by design, and this term reaches
  the unit agents that write there through their transcripts, which live under the orchestrator's
  session whatever worktree they run in (§4).
- Correcting unit 61 §4's refresh sentence and its §5 risks (1) and (6), which G9 H1 asks for under
  either route. That is the orchestrator's fold of H1 into that spec, and this unit writes no text
  there.
- `--audit`'s unit stall probe, which stays on `read_tree_clocks`. Grading a dispatched unit by its
  own transcript is a different question.
- A `--liveness` key saying whether the term is live (§8 F4), and a gate joining the layout this
  driver spells with the run-log kit's (§5 risk 2).
- Any kit version constant. The unattended kit stands unreleased at 1.29 on this branch.
- No edge to `TOOL-dDerivedDocket-63` is declared. AC2 reads the matrix's fresh-clock refusal of a
  new id from another session and its stale take-over. That unit moves the `--replaces` row and
  narrows the same-session row, and a caller under session `T` reaches neither.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-61` — `derive_last_move` with its `LM_TRANSCRIPT` global,
  the one clock `print_liveness`, `check_lease_fresh` and `--status` share, which S1 extends by one
  term; the re-keyed resume matrix, whose check-58 refusal on a fresh clock and stale take-over AC2
  reads; and its AC20 fixture, which AC2 reuses with a sub-agent transcript in place of the gate
  log. Without it the term reaches `--liveness` alone, and the matrix keeps grading the retired
  lease file's clock.
- **consumes-from** `TOOL-dDerivedDocket-62` — the tick's `skip · NO RUN BRANCH` row and the
  `holder-ref` key, which is why AC1's fixture names a `run-branch` and AC3's arm runs over the tick
  suite's `build_fixture`, which that unit makes write one; and its route (a), under which only the
  run-branch worktree acts, the worktree whose root encodes the orchestrator's transcript directory.
- **consumes-from** `TOOL-dDerivedDocket-64` — the gate-queue term, which this term follows in
  `derive_last_move`, and its S4 rewording, which leaves the driver's `--liveness` header the one
  place the signals are listed, so this unit edits no capped carrier.
- **hands-off** external — G9 H1's left-shift, a documented check at spec audit that enumerates
  every writer of a retired refresh, heartbeat or lease write and names the replacement signal each
  reader sees from where it runs. No unit in this build carries it.

## 4. Design

### What the merged tree does, measured

Measured on node `d` 2026-09-22 at `67d2ccfc` (PINNED), over a scratch repository holding a conf in
the shape of the driver suite's `mkconf`, which declares `RESUME_STALE_BOUND="5400"`, and one
committed BUILDING run-state file carrying the six lease facts, session `S65`, `host: absent` and
`run-branch: refs/heads/main`, its commit dated 2000-01-01. `CLAUDE_CONFIG_DIR` names a scratch
directory whose `S65.jsonl`, at the fixture's encoded root, is dated 2000-01-01 too:

| Fixture | Observation |
|---|---|
| nothing else | `--liveness` prints `last-move-source: commit`, `stale: yes`, `verdict: STALE` |
| `agent-a1.jsonl` touched now under `S65/subagents/workflows/wf_x/` | unchanged, because the driver reads nothing under `S65/` |
| `resume-tick.sh --dry-run` over the second | `resumed · attempt 1`: the tick would kill and relaunch |
| `--resume tRun --keepalive-id C` under session `T`, over the second | announces `presumed-stopped` and enters the take-over, which the scratch clone stops at check 24 for want of a remote |

### What a session writes while it waits, measured

Measured on node `d` 2026-09-22 at 08:12:58Z (PINNED), over this build's orchestrating session
`2588f719…` while two Workflows ran, one of them this spec's own authoring:

| Path under `<config>/projects/<enc>/<sid>/` | Written | The signal |
|---|---|---|
| `subagents/agent-<id>.jsonl` | by a direct `Agent` spawn, one append per turn | yes |
| `subagents/workflows/wf_<id>/agent-<id>.jsonl` | by each Workflow agent, one append per turn | yes |
| `subagents/…/agent-<id>.meta.json` | once, at the spawn | no |
| `subagents/workflows/wf_<id>/journal.jsonl` | at the launch and at each agent's start and result | no |
| `workflows/wf_<id>.json` | at the Workflow's end: absent for both running ones | no |
| `tool-results/*.txt` | when one tool output is too large to inline | no |

- The orchestrator's `2588f719….jsonl` was 530 s old, and the three live agent transcripts were 0 s,
  16 s and 19 s old. G9's skeptic stage measured the same transcript still for 19 minutes while a
  review Workflow wrote.
- A worktree-isolated agent writes there too. The agent of `wf_164f0154-0d1` carries a
  `worktreePath` naming `.claude/worktrees/wf_164f0154-0d1-1` in its `meta.json`, and its transcript
  sits under the orchestrator's directory. So the term reaches the `--dispatch` and `--brief` writes
  that G9 H1's first premise names, through the agent that makes them.
- The session holds 431 agent transcripts after two days: 2 directly under `subagents/` and 429
  under 46 `workflows/wf_*/` directories. Every metadata file reads `spawnDepth: 1`, because a
  sidechain agent holds neither spawning tool (charter §8).
- A Workflow agent runs inside its session's process. This author's own shell reads
  `CLAUDE_CODE_SESSION_ID` equal to the orchestrator's id and `CLAUDE_PID=22572`, the orchestrator's
  `claude.exe`. While three agents ran, no `claude.exe` on the node had a Claude Code `claude.exe`
  as its parent.

### The term

After the transcript term, inside `derive_last_move`, with `sd`, `fs`, `g`, `ms`, `k`, `m` and `f`
declared local:

```sh
  if [ -z "$LM_DEAD" ] && [ -n "$LM_TRANSCRIPT" ]; then
    sd="${LM_TRANSCRIPT%.jsonl}/subagents"; fs=(); g=""
    shopt -q globstar && g=1; shopt -s globstar
    for f in "$sd"/**/agent-*.jsonl; do [ -f "$f" ] && fs+=("$f"); done
    [ -n "$g" ] || shopt -u globstar
    if [ "${#fs[@]}" -gt 0 ]; then
      ms=$(stat -c %Y -- "${fs[@]}" 2>/dev/null) || true; k=0
      while IFS= read -r m; do
        case "$m" in ""|*[!0-9]*) continue ;; esac
        k=$((k+1)); if [ "$m" -gt "$LM_NEWEST" ]; then LM_NEWEST=$m; LM_SOURCE=subagent; fi
      done <<<"$ms"
      [ "$k" -eq "${#fs[@]}" ] || LM_DEAD="stat -c %Y over $sd"
    fi
  fi
```

The glob, the `-f` tests, `shopt` and the loop are builtins, so the term costs one spawn whatever
the count. A path list of 431 entries, about 92 KB, reached one `stat` on node `d` and returned 431
readings. The loop takes the shape `read_tree_clocks` already uses, a variable fed through a
here-string. `globstar` is restored to the state it was found in, and nothing else in the driver
spells `**`. A `stat` that dates some paths and not others still prints the rest, so the count test
is what makes a partial reading a dead probe rather than a silently smaller population.

### Why the term is this run's, and what can move it

- It reads only the directory of the recorded `session` fact. A Workflow agent runs under its
  spawning session's id, as measured above, so another session's sub-agents write under that other
  id and move nothing here. AC1 plants one to pin it.
- The tick relaunches with `claude -p --resume <session>`, unit 61 §4 "The relaunched session",
  which keeps the id, so the relaunch's sub-agents write into the same directory. That session is
  the holder under unit 61's same-session row.
- The directory is found through the transcript path, which `resolve_transcript_path` derives from
  `$ROOT`. A sibling worktree's `--liveness` derives no transcript for the orchestrator's session,
  so it reads no sub-agent either, and the term keeps the per-worktree reach unit 62's route (a)
  relies on.
- Any process that can write the config directory can move it by hand, the reach it already has over
  `<sid>.jsonl` (§5 security).

### The bound it honours

- `RESUME_STALE_BOUND`, as every term. The unit adds no conf key and no second bound.
- A dead holder is kept fresh for at most one bound after its last sub-agent turn. A Workflow cannot
  outlive its session's process, because its agents run inside it, as measured above, so once the
  holder dies no transcript of its session moves. That is the window the transcript term already
  gives after the holder's last turn. It is UNVERIFIED for a harness that runs agents out of
  process, and the process listing above is the measurement to repeat.
- An agent inside one tool call writes nothing until the call returns. This harness states a 600 s
  ceiling on one Bash call, under gov's 5400 s. A tool with no ceiling is §5 risk (3).

### Inventory

| Identifier | Kind | Cell, and the lexicon answer at writing |
|---|---|---|
| `subagent` | a `last-move-source` value | a value, beside `transcript` |

The unit mints no function and no global, so no name is owed to `python tools/lexicon/lexicon.py
--suggest`. It adds no `fail` branch and moves no `fail` line, so no row of
`memory/project/unarmed-branches.txt` is re-keyed.

### Migration

None. The unit adds no record fact, conf key or persisted state. A session that has spawned no
sub-agent reads exactly as it does on unit 64's driver.

### Rollout

The unit lands after unit 64 in this build's own run, in the serial order of the promoted units, and
ships live: its only effect is to withhold a kill and a take-over from a session whose sub-agents
are writing. From unit 61's Rollout, which records this build's session, until this unit's build
commit is in the run worktree, a wave that outlasts the bound with no orchestrator commit reads
STALE there. Measured on node `d` 2026-09-22 (PINNED), `schtasks /query` lists 416 tasks and none
matches `resume`, `unattended` or `tick`, so the kill is latent. The resume tick stays unregistered
on node `d` until this unit has landed. The take-over half of that window needs another session's
`--resume --keepalive-id` in the run worktree, which nothing in this build issues.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/resume-tick.test.sh`

### Alternatives rejected

- Stating the residual and keeping the tick unregistered while a Workflow runs, G9 H1's route (b),
  and the other options §8 F1 weighs.
- A per-file `stat` loop, as the gate-log term dates its files. Over this session's 431 transcripts
  that is 431 spawns on a node whose process creation is the dominant cost.
- The Workflow journals alone. A journal moves at an agent's start and result, so a long agent is
  silent between them.
- Calling the run-log kit's reader. It is Python in another kit, so each `--liveness` call would pay
  an interpreter spawn, and a kit file may not name another kit's path.

## 5. Production-readiness checklist

- security — The term reads mtimes only and never parses a transcript. Any process that can write
  the config directory can keep a run LIVE by touching a file under the recorded session, which is
  the reach it already has over `<sid>.jsonl`. The lease stops an accidental second driver and not a
  malicious one, as unit 61's §5 states.
- perf / scale — One `stat` spawn per `--liveness` call once the session has a sub-agent. PINNED,
  node `d` 2026-09-22: a prototype of the term over this session's 431 transcripts took 0.27 s to
  0.41 s warm with its shell's own start, against 0.05 s over a session with none. One first read of
  the same tree through `find` took 8.6 s, which a warm cache did not reproduce. The count grows
  with the session's own agents and resets with a new session.
- error / empty / loading states — No transcript, no `subagents/` directory and no match each
  contribute nothing. A partial reading is the dead probe `fail 52` refuses on, which the tick
  reads as a skip and `check_lease_fresh` as unknown, declining a take-over rather than inviting
  one, so a file the CLI prunes mid-read errs toward the live verdict.
- observability — `last-move-source: subagent` while a session waits on its agents; the `transcript`
  key still names the session's own file, whose directory holds them.
- risks — (1) Between unit 61's Rollout and this unit's landing the kill is armed for any wave past
  the bound (§4 Rollout). (2) The layout is spelled in two kits, this term's glob and
  `build_session_tree` in `tools/runlog/extract.py`, and no gate joins them; a CLI that moves
  sub-agent transcripts silences the term in the kill direction, and the driver suite's literal
  paths pin the layout measured in §4. (3) An agent inside one tool call longer than the bound, on a
  tool with no ceiling, still reads stale. (4) A harness that ran agents out of process would let
  the term keep a dead holder fresh past one bound (§4).
- testing — The arms §7 names, each staged RED and executed once at VERIFYING; the direct
  observations in §6 are fixture runs of the driver and the tick, and greps over tracked files.
- migration — none, per §4 Migration.
- user docs — The driver's `--liveness` header and the signals comment in `derive_last_move`. No
  user-facing carrier lists the signals once unit 64 lands.

## 6. Acceptance criteria

- **AC1** — When `--liveness` runs over §4's measured fixture, its commit and `S65.jsonl` aged past
  `RESUME_STALE_BOUND`, with one `agent-a1.jsonl` dated inside the bound under
  `S65/subagents/workflows/wf_x/`, it prints `last-move-source: subagent`, `stale: no` and
  `verdict: LIVE`, with the same keys in the same order as without the file. The same holds with the
  file directly under `S65/subagents/`, and one directory deeper than `wf_x/`. With the file dated
  past the bound by `touch -d` it prints `stale: yes` and `verdict: STALE`, and so it does with the
  fresh file under another session's `T/subagents/workflows/wf_x/` instead. With a `stat` stub first
  on `PATH` that prints no reading for one matched path, it refuses at check 52 naming
  `stat -c %Y over` that directory and prints no `verdict:` line.
  Red when: a fresh sub-agent transcript reads `stale: yes` with `last-move-source: commit`, as
  measured at `67d2ccfc`, so the tick kills an orchestrator waiting on its Workflow; or another
  session's agent keeps this run LIVE; or an aged one keeps a dead run LIVE; or a nesting the CLI
  does not write today, or an undatable file, reads as absent. The fresh reading is staged RED by a
  copy of `derive_last_move` with the sub-agent term removed.
  fixture: the scratch repository of §4's measurement, with every file planted by hand, so no
  Workflow runs.
- **AC2** — Take `TOOL-dDerivedDocket-61` AC20's fixture with its commit and transcript aged past
  `RESUME_STALE_BOUND`, and plant one `agent-a1.jsonl` dated inside the bound under the recorded
  session's `subagents/workflows/wf_x/`, in place of that criterion's gate log. `--status` prints no
  `presumed-stopped`, and `--resume --keepalive-id C` from session `T` refuses at check 58 and
  leaves the run-state file byte-unchanged. With the file dated past the bound, `--status` prints
  `presumed-stopped` and the same call takes the run over.
  Red when: a second session takes the slug over from an orchestrator whose Workflow is still
  writing, the take-over G9 H1 names beside the kill; or the matrix and `--liveness` disagree about
  one waiting session because one of them reads a clock without the term.
  fixture: unit 61 AC3's authorized record at a pinned BASE over a local bare remote, the shape the
  driver suite's prologue builds, on the branch its record names, so unit 62's guard lets the call
  through to the rows read here; the tree holds none outside that suite.
  permission: the arm lives in the driver suite, a held kit suite on no bar leg, so it runs in the
  orchestrator's attributed VERIFYING run and never in this pass.
- **AC3** — When `bash tools/unattended/resume-tick.sh --repo <fixture> --dry-run` runs over AC1's
  fixture with the sub-agent transcript dated inside the bound, it prints `skip · verdict LIVE` and
  no `resumed ·` decision; with it dated past the bound it prints `resumed · attempt 1`. The
  fixture's `run-branch` names the ref its HEAD has checked out, so unit 62's `skip · NO RUN BRANCH`
  is not what the aged half meets.
  Red when: the tick decides `resumed · attempt 1` for a record whose only fresh signal is a
  sub-agent transcript, as measured at `67d2ccfc`, which on a node with a registered tick kills the
  orchestrator's tree and its Workflow and relaunches it.
  permission: the fixture run is this pass's direct check. The arm that keeps it runs over the tick
  suite's `build_fixture` with `CONF_EXTRA='RESUME_STALE_BOUND="1800"'`, because that fixture's
  declared 1 s bound is shorter than one tick call; it is a held kit suite, executed at VERIFYING
  beside AC2's.
- **AC4** — When `grep -cE '^[^#]*subagents' tools/unattended/unattended.sh` runs at the build
  commit it prints 1, and `grep -cF '/**/agent-*.jsonl'` over the same file prints 1. The count of
  `grep -cF "'----'"` over it, the root encoding's one spelling, is what it was at the first parent,
  1 at `67d2ccfc`.
  Red when: the term derives the session directory a second way, so it can disagree with the
  transcript term about a root whose `_` encoding is UNVERIFIED; or the layout is spelled on a
  second code line, so a CLI change is fixed in one and not the other.
- **AC5** — When the attributed run at VERIFYING reports `verdict clean` on the driver and
  resume-tick suites, this unit's arms are among the executed ones, and each suite's
  `FLOOR_ASSERTIONS`, with the driver suite's `FLOOR_SHARD_2`, reads at the build commit its figure
  at the first parent plus exactly the assertions those arms' blocks carry, read with `git show` at
  both, while the driver suite's `FLOOR_SHARD_1` is unchanged.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it, above all
  the key-order arm at `tools/unattended/unattended.test.sh:5897` and the transcript arm at `:6036`;
  or a floor moves by a number no arm accounts for.
  permission: both are held kit suites on no plain bar leg, so they run at VERIFYING and never in
  this pass.
- **AC6** — When `grep -c 'KIT_UNATTENDED_VERSION=1.29' tools/unattended/unattended.sh` runs at the
  build commit it prints 1. The lines this unit adds to the driver, read by `git diff -U0` of the
  build commit, carry no `tools/<kit>/` literal. `grep -cE '^[a-z_]+\(\) *\{'` and
  `grep -cE '^[^#]*\bfail [0-9]+'` over the driver print what they printed at the parent.
  `grep -cE '^ *#.*sub-agent transcript'` over the driver prints at least 2, and `git diff
  --name-only` of the build commit names none of the protocol, stop contract or verb carrier, as
  template or render.
  Red when: the unit moves a version the unreleased kit does not owe; or an added line spells a path
  the install-prefix ban forbids; or a function or a `fail` branch arrives unpriced; or the comment
  that lists the signals omits the term, so a reader sizing the bound is told a waiting session is
  silent; or a capped carrier is edited to say so instead.
  permission: the ban's verdict is the `install-prefix (shipped surface)` leg, and the
  armed-or-pinned verdict is the `harness arms (fail branches armed or pinned)` leg, both observed
  at VERIFYING.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a driver copy whose `derive_last_move` lacks the sub-agent term, under which the signals block's fresh sub-agent transcript reads `stale: yes` and unit 61's AC20 fixture with one is taken over · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`, each raised by exactly the new arms' assertions, counted off their blocks
New arm: `tools/unattended/resume-tick.test.sh` · the same driver copy, under which a BUILDING record with a fresh sub-agent transcript decides `resumed · attempt 1` · `FLOOR_ASSERTIONS`, raised by exactly the new arm's assertions, counted off its block

Every floor follows this build's practice, set by the CLOSED units 25, 30, 49 and 54: a unit raises
its suite's executed-assertion floor by exactly the arms it adds, derived from the blocks rather
than read off a run, which this pass does not make. The driver's new arms are written in region
two, so `FLOOR_SHARD_1` does not move. No path under §4's estimate trips a guard narrower than the
broad `tools/` one, so the legs above are named by choice.

## 8. Open questions

- **F1 — how a session waiting on its sub-agents stays fresh.** Options: (a) a term over the
  recorded session's sub-agent transcripts; (b) G9 H1's route (b), stating the residual in unit 61
  §5 and unit 62 §8 F1 and keeping the tick unregistered while a Workflow runs; (c) the orchestrator
  commits within every bound while it waits; (d) the clock joined across the slug's worktrees.
  RESOLVED (agent, 2026-09-22, delegated): (a), settled by this spec's author under the build's
  delegated rule on the first route of G9 H1's fix. (b) needs no mechanism, but every wave of this
  build is a Workflow, so the tick could never be registered for its run, and the matrix's stale
  take-over stays open to any session in the run worktree. (c) needs a turn, and G9 measured no
  keepalive wake across 88 minutes of Workflow waits. (d) is unit 62's rejected F1 option (b), a
  sibling's commit keeping a dead holder fresh, and it still misses an agent that has not yet
  committed.
- **F2 — which files are the signal.** Options: (a) `agent-*.jsonl` at any depth under
  `<sid>/subagents/`; (b) the two depths the CLI writes today; (c) every file under `<sid>/`;
  (d) the Workflow journals alone. RESOLVED (agent, 2026-09-22, delegated): (a), by the same author.
  It is the population `build_session_tree` in `tools/runlog/extract.py` reads, so one layout has
  two readers that agree. (b) is the same set today and goes silent in the kill direction when the
  layout nests deeper; (c) adds files written once or at a Workflow's end, none of them a turn;
  (d) moves only at an agent's start and result.
- **F3 — how the term finds the directory.** Options: (a) the derived transcript path with `.jsonl`
  stripped; (b) a second derivation from `$ROOT` and the `session` fact. RESOLVED (agent,
  2026-09-22, delegated): (a), by the same author. It keeps one derivation of an encoding whose `_`
  rule is UNVERIFIED, and each of the four session directories under this worktree's encoding has
  its transcript beside it, so none is missed.
- **F4 — how the term says it cannot move.** Options: (a) the dead probe alone, with the layout risk
  stated; (b) a dead probe when `subagents/` exists and no file matches; (c) a `--liveness` key.
  RESOLVED (agent, 2026-09-22, delegated): (a), by the same author. A Workflow's directory is made
  at its launch, with its journal, before its first agent appends, so under (b) a script that ends
  before it spawns an agent would leave a directory refusing every later verdict for the session.
  That is argued, not observed: none of this session's 46 directories is in that state. (c) is the
  key unit 64 declined for its own term.
- **F5 — a `memory/DECISIONS.md` row.** RESOLVED (agent, 2026-09-22, delegated): none, by the same
  author. The decision is F1 above and the driver comment, and unit 61's row already records the
  lease reconciliation this unit completes.

## 9. Revision log

- rev-1 · 2026-09-22 · initial draft, promoted from H1 of the G9 spec audit, round 1, grounded on
  `67d2ccfc` and on `TOOL-dDerivedDocket-61` at rev-6 and `TOOL-dDerivedDocket-64` at rev-2 as
  specified, with the current behaviour measured over a scratch fixture and the session layout
  measured over this build's own orchestrating session.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the newest modification time over a session's sub-agent
transcripts, read as one more term of an out-of-process liveness clock"` names
`resolve_session_tree` in `tools/runlog/extract.py` as a seam. It hands the session's transcript to
`build_session_tree` beside it, the run-log kit's reader of the same layout. Neither is called: it is Python in another kit, the driver pays a spawn per call, and a
kit file may not name another kit's path. So the term copies that reader's POPULATION,
`<sid>/subagents/**/agent-*.jsonl`, and none of its code. The probe's header prints `unscanned
layers: .sh`, the layer this unit is written in, so the seams it extends were found by reading
source: `resolve_transcript_path`, whose derived path the term strips, and the transcript term of
`print_liveness`, which unit 61 moves into `derive_last_move`.

Recall terms used: `python tools/memory-recall/query.py "how does the liveness clock see a session
that is waiting on its own sub-agents or a background Workflow, so its run is not read stale and
killed" --terms "liveness transcript subagent workflow stale bound resume-tick kill orchestrator
derive_last_move session clock"`. It returned G9's H1 itself; unit 64's §10; the risks row of
`TOOL-aWokenSentinel-5`, which already named a killed Workflow as the harm of a false STALE, bounded
by `RESUME_STALE_BOUND`; `TOOL-aBoundedCeiling-12`'s dead-ticket row; and
`TOOL-aBatchedTribunal-1b`, which put the fan-out cap at the Workflow tool call.
