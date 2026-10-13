# TOOL-aOrientedCast-24 — format-guard reads a notification's header alone and opens no turn mid-turn, gate-guard asks the driver whether a leased run is finished, and the arms and docs that pin both

**Status:** INPROGRESS · rev-1 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams tooling · order 26 · ratified 2026-10-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-24-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-24-1-spec-brief.md) | journal | TOOL-aOrientedCast-25 |
| [2026-10-13-prompt-TOOL-aOrientedCast-24-2-build-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-24-2-build-brief.md) | journal | TOOL-aOrientedCast-25 |

<!-- /gen:spec-records -->

## 1. Goal

The second closing review of this build
(`memory/builds/aOrientedCast/reviews/2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md`)
confirmed fourteen findings. This unit closes the seven that land on the hooks kit's
`format-guard.js` and the unattended kit's `gate-guard.js`: M1, M2, M3, M7, L1, L2 and L3. Two are
wrong refusals and one is a silent allow, all in guards this build shipped. The rest are missing
arms that would let those paths regress green, and two docs that state behaviour the code does not
have. Each fix closes its finding's class, and an arm pins it.

## 2. Scope (IN)

- **S1** — M1. `extractTurnAgents` reads a delivered notification's tool-use id from its header
  alone: the first `<tool-use-id>` before the record's first `<result>`, and none when the header
  carries none, under §4 "S1 — the notification header". Observed by AC1.
- **S2** — M2. `scanTurnRecords` opens no turn at a compaction summary, or at a harness meta record
  that sits in a run of meta records directly after a tool result, under §4 "S2 — the turn opener".
  Observed by AC2 and AC3.
- **S3** — M3. `checkAsk` reads the driver's `--liveness` verdict through stop-guard.js's own reader
  for every lease outside PHASES_TERMINAL. TERMINAL allows. An unreadable liveness leaves the
  recorded phase standing. At FINISHED-UNSTAMPED the deny names `--landed` rather than `--park`.
  All under §4 "S3 — the question arm's liveness". Observed by AC6, AC7 and AC8.
- **S4** — M7 and L1. `tools/hooks/format-guard.test.sh` gains the arms of §4 "The format-guard
  arms", and its `FLOOR_ASSERTIONS` rises by their count. Observed by AC1 to AC5.
- **S5** — M3 and L3. `tools/unattended/gate-guard.test.sh` runs its question arms on a stub-driver
  kit copy and gains the arms of §4 "The gate-guard arms", and its `FLOOR_ASSERTIONS` rises by their
  count. Observed by AC6, AC7 and AC9.
- **S6** — L1, with S1 and S2's prose. The format-guard header and the hooks README's format-guard
  section state the parse-failure rule the code has, the header-only id read and the two opener
  exceptions. Observed by AC10.
- **S7** — L2, with S3's prose. The unattended README's question-arm paragraph says the widened
  matcher reaches a running session from its next tool call, and states S3. The gate-guard header
  and the unattended dossier's question-arm sentence state S3. Observed by AC10.
- **S8** — L2's left-shift. The settings gotcha records this second instance of its class. Observed
  by AC10.
- **S9** — The hooks kit moves from 1.36 to 1.37 and the unattended kit from 1.105 to 1.106, each
  with every carrier. Observed by AC11.

## 3. Non-goals (OUT)

- M4, M5, M6, L4, L5, L6 and L7, which TOOL-aOrientedCast-25 closes. M4 needs no edit to
  `tools/hooks/agent-cap.js`: the review's sound fix moves `handoff.py`'s matcher onto agent-cap's
  existing normalisation, so no half of M4 is this unit's. This unit writes `agent-cap.js` for its
  version constant only, and owns `format-guard.js` and its suite, so L4's fix and any parity arm
  it adds belong in the roles kit's own files.
- The run-log prose reader's turn rule (`tools/runlog/prose.py:121-149`). It keeps opening a turn at
  every typed record. It is a report-only measure in another kit, and format-guard's header says
  where the two now differ.
- `handoff.py`'s notification reader and the run-log kit's `_derive_notifications`, which also read
  every `<tool-use-id>` of a block. The first is the roles kit's and its consequence was refuted (the
  review's id 2); the second is a report-only measure.
- Spec 22's §4 "Rollout" and §5 "risks" sentences on a restart, and AC7's "and a restart". A CLOSED
  record is not edited, AC7 stays observable as written (a restart is sufficient, merely not
  needed), and that unit's acceptance ledger is TOOL-aOrientedCast-25's write set for its AC6.
- The kickoff manifest's line calling gate-guard a `Bash|PowerShell` hook
  (`memory/guides/SESSION-KICKOFF.md:180`), stale since TOOL-aOrientedCast-22 widened the matcher.
  TOOL-aOrientedCast-23 re-stamps that file, and a second writer of it would race the stamp. Noted
  here for the main loop.
- The agent-cap dossier, `memory/map/features/agent-cap.md`, which read 20474 bytes against a
  `DOSSIER_CAP_BYTES` of 20480 on 2026-10-13. Its prose stays true after this unit, so it is not
  touched and needs no split. The unattended dossier's `decisions` list is not touched either, so
  nothing under `memory/map/generated/` moves (§4 "Inventory").
- A status-header `closes` verb (§4 "The findings and where each lands").

### Edges

- **consumes-from** external — the driver's `--liveness` verb and stop-guard.js's exported
  `runLiveness` and `parseLiveness`, all landed. Without them S3 has no verdict to read, and the
  recorded phase stands as it does today.
- **hands-off** external — aligning the run-log prose reader's turn rule with S2, should that kit's
  measure want it: a follow-up in the runlog kit.

## 4. Design

Line numbers were read at `debc4bad6` on 2026-10-13.

### The findings and where each lands

| Item | Review id | Severity | Closed by |
|---|---|---|---|
| M1 | 1 | medium | S1, S4 · AC1 |
| M2 | 3 | medium | S2, S4 · AC2, AC3 |
| M3 | 5 | medium | S3, S5 · AC6, AC7, AC8 |
| M7 | 10 | medium | S4 · AC4 |
| L1 | 4 | low | S4, S6 · AC5, AC10 |
| L2 | 7 | low | S7, S8 · AC10 |
| L3 | 11 | low | S5 · AC9 |

The brief asks for a `closes` header verb naming these items. The status header carries none,
because `closes` takes backlog ask ids only: `backlog.py`'s reader refuses a value the id expander
does not parse (`tools/memory-tree/backlog.py:744-747`, `tools/memory-tree/gen_build_index.py:603-615`),
so `closes M1` would stop the index generator for every caller. This table is the join instead.

### Evidence — what the transcripts hold

Measured on 2026-10-13 over the 311 main-session transcripts read from the 400 newest under node
a's Claude projects directory, by read-only scripts in the session scratchpad. Every figure is
PINNED to that date, because a CLI update moves them.

| Fact | Count |
|---|---|
| typed `user` records marked `isMeta` whose nearest earlier user or assistant record holds a `tool_result` | 241: 124 carry `sourceToolUseID` (a Skill's expansion), 117 do not (an image's size note after a Read, a retry prompt, "Continue from where you left off.") |
| other typed `isMeta` records: idle-wake ticks, keepalives, stop-hook feedback, command caveats | 987, plus 1 carrying `sourceToolUseID` that follows no tool result |
| compaction summaries, `isCompactSummary: true` | 71, of which 44 follow a tool call or its result |
| delivered notifications, as `user` records or `queued_command` attachments | 6126; each holds at most one `<task-notification>` block and at most one `<tool-use-id>`; in all 1697 that carry both a header id and a `<result>`, the id comes first; 25 carry a `<result>` and no header id |
| `stop_hook_summary` records, the harness's mark of a Stop | 5133 Stop-to-Stop windows; absent from 32 of the 290 sessions holding an owner prompt; never written with `hookCount` 0 |

The three findings reproduce at `debc4bad6`. A transcript with an `Agent` call, a Skill call, its
result and a meta record carrying `sourceToolUseID` gives `scanTurnRecords` and `extractTurnAgents`
no requirement; without the Skill records it requires `agent:a1`. A notification for `t1` whose
`<result>` quotes `<tool-use-id>t9</tool-use-id>` requires `returned:a1` and `returned:a9`. Fed
an `AskUserQuestion` payload for the lease of `memory/builds/aBatchedMinors/RUN.md`, `gate-guard.js`
exits 2 naming `at LANDING`, while `unattended.sh --liveness aBatchedMinors` prints
`verdict: TERMINAL`.

### S1 — the notification header

Today `note` is a notification record's whole content, and every `<tool-use-id>` in it is pushed,
the `<result>` body included (`tools/hooks/format-guard.js:349-355`). The change cuts `note` at its
first `<result>`, takes the first `<tool-use-id>` in what precedes it, and pushes at most that one
id per record. Both delivery routes, the `user` record of origin `task-notification` and the
`queued_command` attachment, go through it.

Measured above, a real delivery carries its id in the header and carries one, so the cut moves
nothing on a real delivery, and an id the agent quotes in its result names nothing. A record holding
two blocks would lose its second id, which is an allow; no such record was found, and the header
says so.

### S2 — the turn opener

`scanTurnRecords` (`tools/hooks/format-guard.js:263-292`) opens a turn at any typed `user` record
(`checkTyped`, `:266-271`). After the change a typed record opens a turn unless:

1. it carries `isCompactSummary: true`; or
2. it carries `isMeta: true`, and the nearest earlier main-file `user` or `assistant` record that is
   not itself a typed meta record holds a `tool_result` block. A run of meta records directly after
   a tool result therefore opens nothing.

Records of other types, `system`, `attachment` and `queue-operation` among them, are passed over
when looking for that nearest record. The walk runs from the end, so rule 2 is settled one record
late: a meta record waits as pending until the next older user or assistant record that is not a
meta record is parsed, and a pending record with none before it opens the turn. Everything else
holds: back-to-back openers are one turn, an assistant record carrying text or a tool call ends the
run of openers, and a line that does not parse is counted.

Rule 2 keys on position and not on `sourceToolUseID`, because 117 of the 241 mid-turn meta records
carry no such field (§8 F3). An idle-wake tick and a stop hook's feedback follow assistant text, so
each still opens its turn. A typed record that is not a meta record still opens a turn wherever it
sits, so an owner's interjection or an interrupt after a tool result splits the turn there; the
header says so.

### S3 — the question arm's liveness

`checkAsk` (`tools/unattended/gate-guard.js:695-705`) keeps its lease scan and its filter: a lease
whose phase is empty, `absent` or in PHASES_TERMINAL is not live, and costs no spawn. For each lease
left, it requires `stop-guard.js` by `__dirname`, as it already requires `run-lease.js`, and calls
that module's exported `runLiveness(__dirname, root, slug)` and `parseLiveness`
(`tools/unattended/stop-guard.js:107-127`). That is the spawn, bound and parse stop-guard pays on
every stop, so the two hooks read one answer.

| The liveness read | The lease |
|---|---|
| `verdict: TERMINAL` | not live |
| any other verdict | live; the verdict goes into the deny |
| no `verdict:` line, a non-zero exit, the bound, or `stop-guard.js` failing to load | live on its recorded phase; the deny says the liveness could not be read |

The driver reads TERMINAL for a recorded terminal phase, for a LANDING record whose landed log
names its landing commit, and for a HELD hand-off whose landing commit is on the default branch
(`tools/unattended/unattended.sh:8725-8735`). This hook restates none of the three. Only TERMINAL
overrides the recorded phase; ELSEWHERE does not. PHASES_TERMINAL stays as the filter, so a LANDED
or ABORTED record spawns nothing, and its parity arm stays.

The require and the read sit in their own `try`, so a throw there is an unreadable liveness. The
`catch` around `checkAsk` in `main` still fails open for every other input.

`renderAskDeny`'s first line gains `, liveness <verdict>` after the phase, or `; its liveness could
not be read, so the recorded phase stands` when there was none. At FINISHED-UNSTAMPED the park
paragraph gives way to the landing one, mirroring stop-guard's `landing-unstamped` reason
(`renderBlock`):

```text
BLOCKED by gate-guard: this session holds the lease of the unattended run <slug>, at LANDING, liveness FINISHED-UNSTAMPED (<record>).
Its witness is already on the default branch, so the run is finished and unstamped. The one act
left is the landing stamp, not a question:

  unattended.sh --landed <slug>

The question this call asked:
  - <question> — options: <label>, <label>
```

### The format-guard arms

In `tools/hooks/format-guard.test.sh`, after the TOOL-aOrientedCast-21 block. `write_transcript`
(`:307-336`) gains the scenarios below, and its `notice` helper an optional `<result>` body. A meta
record, a compaction summary, a `queued_command` attachment and a torn line are built the same way,
from JSON objects or one raw string, so no byte crosses a shell quote. "Pair-only" is the suite's
`good.md`; A1, R1, A2, A3, R2 and R3 are its existing lines.

1. `quoted` — `Agent` calls t1 and t9 return a1 and a9, async, in an earlier turn; the last turn
   opens with t1's notification, whose result quotes `<tool-use-id>t9</tool-use-id>`. The R1 message
   allows; pair-only blocks naming a1 and not a9.
2. `quoted-headless` — a notification with no header id, its result quoting t9: pair-only allows.
3. `skill` — one turn: a1's async dispatch, a Skill call and its result, a meta record carrying
   `sourceToolUseID`, final text. Pair-only blocks naming a1.
4. `image` — the same with a Read's result and a meta image note carrying no `sourceToolUseID`.
   Pair-only blocks naming a1.
5. `compact` — a1's result followed by a `compact_boundary` system record and a compaction summary.
   Pair-only blocks naming a1.
6. `tick` — a1 dispatched in an earlier turn that ended with text, the last turn opened by an
   idle-wake meta record. Pair-only allows, and stderr is empty.
7. `queued` — a1's async dispatch, then its notification in a `queued_command` attachment later in
   the same turn. A1 alone blocks naming `no returned line for agent a1`; A1 with R1 allows.
8. `foreground` — an `Agent` result `{status: "completed", agentId: "a1"}`. A1 alone blocks naming
   the `returned` line; A1 with R1 allows.
9. `run-foreground` — a `Workflow` result with `runId` `wf_t-1` and status `completed`, its journal
   holding `started` for a2 and a3, a `result` for a2 and a `failed` for a3. A2 with A3 blocks naming
   `no returned line for agent a3`; all four lines allow.
10. `torn` — the `agent` scenario with one unparsable line inside the turn. Pair-only blocks naming
    a1, and stderr carries `1 line(s)`.

`FLOOR_ASSERTIONS` (`:436`) rises by the assertions these arms add, counted at build time, with a
comment naming this unit beside the earlier ones.

### The gate-guard arms

In `tools/unattended/gate-guard.test.sh`. The question arms run a COPY of `gate-guard.js`,
`stop-guard.js` and `run-lease.js` in a scratch kit dir beside a stub `unattended.sh`, the pattern
of `tools/unattended/stop-guard.test.sh:143-162`: on `--liveness` the stub prints a file the arm
writes, and it exits with a code the arm sets. `run_ask` (`:554`) runs that copy. The stub's default
prints `verdict: LIVE`, so Q1 to Q5 keep their expected exits. Both parity arms keep reading the hook
in place. The new arms:

- Q7 — a LANDING record, the stub at TERMINAL: exit 0 with an empty stderr.
- Q8 — a LANDING record at FINISHED-UNSTAMPED: exit 2, stderr naming `unattended.sh --landed fx`
  and not `--park`.
- Q9 — a HELD record at TERMINAL exits 0; at HELD, 2.
- Q10 — a BUILDING record with the stub exiting 1, then printing no `verdict:` line, then absent:
  exit 2 each time, stderr saying the liveness could not be read. A LANDED record with the stub
  absent exits 0.
- Q11 (L3) — a BUILDING record with its `phase:` line deleted: exit 0 with an empty stderr.
- Q12 (L3) — a payload whose `cwd` is the number 42, which makes `resolveRepo` throw: exit 0.

`FLOOR_ASSERTIONS` (`:604`) rises by the assertions these arms add, counted at build time, with a
comment naming this unit.

### Documentation

- `tools/hooks/format-guard.js`, HOW THE TURN'S AGENTS ARE READ (`:40-49`): the turn rule gains S2's
  two exceptions, the notification id is read from the header alone, and the degraded-input
  sentence becomes: no `transcript_path`, an unreadable transcript or journal, or a run id off its
  shape allows the arm with one witness line each; lines in the turn that do not parse are counted
  into one witness line, and the arm still grades the records that parsed. WHAT THIS DOES NOT CHECK
  (`:59-71`) gains S2's residual and a record carrying two notification blocks.
- `tools/hooks/README.md`, "How the turn's agents are read" (`:446-457`) and "The ceiling"
  (`:462-469`): the same three statements and the same two limits, the parse-failure sentence again
  carrying the words "still grades".
- `tools/unattended/gate-guard.js`: THE QUESTION ARM (`:48-59`) states S3; NO PATH OUTSIDE THIS FILE
  IS SPELLED (`:84-92`) adds `stop-guard.js` to the sibling basenames; FAILS OPEN (`:98-101`) names
  an unreadable liveness as the one input that does not allow, and why.
- `tools/unattended/README.md`, the question-arm paragraph (`:103-111`): S3's rule, in a sentence
  saying a lease is finished when the driver's `--liveness` reads TERMINAL, and the
  FINISHED-UNSTAMPED remedy; and, for L2, the widened matcher reaches every session from its next
  tool call, one already running included, because the harness re-reads the hooks settings on each
  call (measured 2026-08-10, recorded as a bug class in the memory tree). A kit file names nothing
  outside itself by literal, so the gotcha is described, not linked.
- `memory/map/features/unattended.md:210-211`: the question-arm sentence says a lease is finished
  when the driver's `--liveness` reads TERMINAL, in those words. Prose only, outside the toml fence.
- `memory/gotchas/settings-edit-takes-effect-mid-session.md`, "Where it bit": one sentence naming
  the second instance, TOOL-aOrientedCast-22's README and spec, in prose with no new backticked path,
  so the catalogue's derived anchors do not move.

### Kit versions

- Hooks, 1.36 to 1.37: `KIT_AGENT_CAP_VERSION` and its same-line marker at
  `tools/hooks/agent-cap.js:101`, and the `gov:kit agent-cap@` markers at
  `tools/hooks/format-guard.js:7` and `tools/hooks/scratch-guard.js:144`, which
  `tools/check-kit-versions.sh:192-220` compares.
- Unattended, 1.105 to 1.106: `KIT_UNATTENDED_VERSION` at `tools/unattended/unattended.sh:66`, the
  same-line constant and marker of the three other `.sh` carriers
  (`tools/check-kit-versions.sh:298-307`), and every file under `tools/unattended/` that carries the
  old marker. The rendered guides and the
  Skill follow through the kit's re-render.

### Inventory

No identifier is minted. S1 and S2 change the bodies of `extractTurnAgents` and `scanTurnRecords`,
and S3 those of `checkAsk` and `renderAskDeny`. A helper the builder finds it needs asks
`python3 tools/lexicon/lexicon.py --suggest <name> --as js.function` first, and a new named
function moves `memory/map/generated/symbols.json`, so that commit then runs
`python tools/codebase-map/gen_map.py --write`.

### Files touched (estimate)

`tools/hooks/format-guard.js`
`tools/hooks/format-guard.test.sh`
`tools/hooks/agent-cap.js`
`tools/hooks/scratch-guard.js`
`tools/hooks/README.md`
`tools/unattended/`
`memory/guides/UNATTENDED-PROTOCOL.md`
`memory/guides/UNATTENDED-ASKS.md`
`memory/guides/UNATTENDED-STOPS.md`
`memory/guides/UNATTENDED-VERBS.md`
`memory/guides/PLAYBOOK-TEMPLATE.md`
`.claude/skills/unattended/SKILL.md`
`memory/map/features/unattended.md`
`memory/gotchas/settings-edit-takes-effect-mid-session.md`

`tools/unattended/` declares the hook, its suite, the README and every carrier of the kit's version
marker; the guide copies and the Skill listed above carry that marker as rendered output.

### Rollout

1. Edit the two hooks, the two suites and the docs as above.
2. Move the hooks kit's three carriers to 1.37.
3. Move the unattended kit's constant and markers to 1.106, editing every file
   `git grep -l "gov:kit unattended@1.105" -- tools/unattended` lists, then re-render with
   `bash tools/unattended/adopt-unattended.sh`, which the kit's `[[regenerate]]` names
   (`tools/unattended/kit.toml:193`).
4. No settings merge: no matcher moves. No `watch:` path of the kickoff manifest moves. Adopters
   receive both hooks at `govkit update`. Rollback is a revert of the unit's commit.

### Alternatives rejected

- Moving `runLiveness` and `parseLiveness` into `run-lease.js`, the binder its header names: it
  edits `stop-guard.js` and the check-36 exemption row in `tools/unattended/check-unattended.sh`
  that names `stop-guard.js` as `parseLiveness`'s home, for no behaviour. Requiring the exported pair
  reuses it with no file moved.
- A third copy of the liveness parse in `gate-guard.js`: the class M3 names.
- The turn-rule candidates, and the restated landed-log test: §8 F1 and F3, with the tests that
  rejected each in §10.

## 5. Production-readiness checklist

- security — S1 narrows trust: an agent's free text in its result can no longer make the Stop hook
  require lines for another agent. S3 spawns the kit's own driver by `__dirname`, with the slug as
  an argv element and no shell, exactly as stop-guard does; the driver's `check_slug` validates it.
  Neither hook writes anything new.
- perf / scale — format-guard parses at most the turn's lines plus one older record per pending
  meta record. gate-guard spawns one `--liveness` per lease outside the terminal pair, on an
  `AskUserQuestion` from a leased session only: 3.9 s for aBatchedMinors on node a, measured
  2026-10-13 and PINNED, bounded by stop-guard's `LIVENESS_BOUND_MS` of 60 s.
- error / empty / loading states — format-guard's degraded inputs are unchanged, and now documented
  as they behave. gate-guard: an unreadable liveness keeps the recorded phase (§8 F2); every other
  unreadable input still allows.
- observability — the deny names the verdict, or says it could not be read; format-guard's reasons
  and witnesses are unchanged.
- risks — S2 reads `isMeta`, `isCompactSummary` and record order, which are readings of a format
  that is no contract; a renamed field reads as today's rule, a silent allow and never a new
  refusal. S3 binds gate-guard to two exports of `stop-guard.js`; the suite copies all three files,
  so a renamed export reds Q7.
- testing — the arms of §4, observed RED first at the close; AC8 on the live tree.
- migration — none, and no settings merge.
- user docs — the format-guard bullet of `help/roles.md` (`:89-90`) stays true; no help page covers
  the unattended kit.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. The format-guard criteria feed
`node tools/hooks/format-guard.js` a hand-built Stop payload in the fixture spec 21's §6 describes: a
repository under a short `%TEMP%` root with a copy of gov's `AGENTS.md`, a `LIVE.md` naming build
`tBuild`, an orientation card routing it, and a transcript T beside its session dir. "Blocks" means
stdout holds `{"decision":"block"…}`, and "allows" means stdout is empty. "Pair-only", A1, R1, A2,
A3, R2 and R3 are the messages and lines of §4 "The format-guard arms". The gate-guard criteria
feed an `AskUserQuestion` payload to a scratch kit dir holding copies of
`tools/unattended/gate-guard.js`, `tools/unattended/stop-guard.js` and
`tools/unattended/run-lease.js` beside a stub driver that prints a chosen liveness, in spec 22's
fixture checkout, with `session_id` `tSess-1` holding the record's lease. Each staged break is
restored before the next.

- **AC1** — When T's earlier turn holds `Agent` calls t1 and t9 returning a1 and a9, and its last
  turn opens with t1's notification whose `<result>` quotes `<tool-use-id>t9</tool-use-id>`,
  `node tools/hooks/format-guard.js` allows the R1 message, and blocks pair-only naming
  `no returned line for agent a1` and not `a9`. A notification whose header carries no id and whose
  result quotes t9 requires nothing: pair-only allows.
  Red when: an id inside a `<result>` body is required.
- **AC2** — When T's last turn holds a1's async dispatch followed by a Skill call, its result and a
  meta record carrying `sourceToolUseID`; or by a Read's result and an `isMeta` image note carrying
  no such field; or by a `compact_boundary` record and an `isCompactSummary` record,
  `node tools/hooks/format-guard.js` blocks pair-only each time, naming `agent a1` and
  `which this turn dispatched`.
  Red when: any of the three records opens the turn and the dispatch goes unrequired.
- **AC3** — When a1's dispatch sits in an earlier turn that ended with assistant text and the last
  turn opens with an `isMeta` idle-wake record, `node tools/hooks/format-guard.js` allows pair-only
  and writes nothing to stderr.
  Red when: a meta record after assistant text opens nothing, so a finished turn's agent is required
  again.
- **AC4** — When T's turn holds a1's async dispatch and its notification arrives in a
  `queued_command` attachment later in the turn, or holds a foreground `Agent` result with status
  `completed`, `node tools/hooks/format-guard.js` blocks A1 alone naming
  `no returned line for agent a1`, and allows A1 with R1. When the turn holds a `Workflow` result
  with `runId` `wf_t-1` and status `completed`, whose journal holds `started` for a2 and a3, a
  `result` for a2 and a `failed` for a3, it blocks A2 with A3 naming
  `no returned line for agent a3`, and allows all four lines.
  Red when: a delivery by attachment, a foreground completion or a foreground run's endings goes
  unrequired.
- **AC5** — When T's turn holds a1's dispatch and one line that does not parse,
  `node tools/hooks/format-guard.js` blocks pair-only naming `agent a1`, and stderr carries
  `1 line(s)`.
  Red when: a torn line allows the arm, or is skipped without its witness.
- **AC6** — When the record is at LANDING and the stub prints `verdict: TERMINAL`, the copied
  `gate-guard.js` exits 0 with an empty stderr; at `FINISHED-UNSTAMPED` it exits 2, and stderr
  names `unattended.sh --landed fx` and not `--park`. A HELD record exits 0 at TERMINAL and 2 at
  HELD. A BUILDING record at LIVE exits 2, and stderr names `liveness LIVE` and
  `unattended.sh --park fx`.
  Red when: a TERMINAL verdict still refuses, a non-terminal verdict allows, or a finished run is
  told to park.
- **AC7** — When the stub exits 1, prints no `verdict:` line, or is absent, the copied
  `gate-guard.js` still exits 2 for a BUILDING record, and stderr says the liveness could not be
  read. A LANDED record exits 0 with the stub absent.
  Red when: an unreadable liveness allows a pass-phase lease, which switches the arm off on a node
  whose driver cannot run.
- **AC8** — When `node tools/unattended/gate-guard.js` is fed an `AskUserQuestion` payload whose
  `session_id` is the lease of `memory/builds/aBatchedMinors/RUN.md` and whose `cwd` is this
  checkout, it exits 0 with an empty stderr. At `debc4bad6` it exits 2 naming `at LANDING`.
  Red when: a run the driver reads TERMINAL still refuses its session's question.
  fixture: the live tree holds that record at LANDING today, and node a's landed log for the slug
  under the git common dir names its landing commit. Another node lacks the log, and there AC6
  observes the same branch.
  cost: one `--liveness`, 3.9 s on node a, measured 2026-10-13.
- **AC9** — When the fixture record's `phase:` line is deleted, the copied `gate-guard.js` exits 0
  with an empty stderr. When the payload's `cwd` is the number `42`, it exits 0.
  Red when: the absent-phase filter, or the fail-open `catch` around `checkAsk`, is gone.
- **AC10** — When `grep -n "restarts" tools/unattended/README.md` runs, it prints nothing, and
  `grep -n "next tool call" tools/unattended/README.md` shows the question-arm paragraph.
  `grep -n "still grades" tools/hooks/format-guard.js tools/hooks/README.md` shows the
  parse-failure sentence in each file.
  `grep -n "reads TERMINAL" memory/map/features/unattended.md tools/unattended/README.md` shows the
  question-arm sentence in each, and
  `grep -n "TOOL-aOrientedCast-22" memory/gotchas/settings-edit-takes-effect-mid-session.md` shows
  the second instance.
  Red when: a doc still says a running session keeps the narrower matcher, or that an unparsable
  line allows the arm.
- **AC11** — When `grep -c "KIT_AGENT_CAP_VERSION = '1.37'" tools/hooks/agent-cap.js` prints 1,
  `git grep -l "gov:kit agent-cap@1.36" -- '*.js'` prints nothing,
  `grep -c "^KIT_UNATTENDED_VERSION=1.106" tools/unattended/unattended.sh` prints 1, and
  `git grep -l "gov:kit unattended@1.105" -- tools memory/guides .claude/skills` prints nothing,
  every carrier moved. The pathspecs leave out `memory/builds`, whose records quote the old values.
  Red when: a constant or one carrier keeps its old value.
  figure: PINNED at `debc4bad6`, where the kits read 1.36 and 1.105; a mint another build lands
  first moves each expected value by the same one step.

## 7. Gates

`format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `hook destinations (every declared hook path ships)` · `unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `unattended skill size` · `check-wiring self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/format-guard.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the arms of §4 "The format-guard arms", each against its own staged break: the notification read put back to every tag in the record (AC1), both opener exceptions taken out (AC2), the meta exception widened to every meta record (AC3), the `queued_command` branch, the `completed` requirement and `addRun`'s non-async `withReturned` each taken out (AC4), and a torn line made to return before the agent arm (AC5) · `FLOOR_ASSERTIONS` raised by the arms' count

New arm: tools/unattended/gate-guard.test.sh · covers AC6 AC7 AC9 · the question arms of §4 "The gate-guard arms" on the stub kit copy, against a `checkAsk` staged to skip the liveness read (AC6), to allow when the liveness is unreadable (AC7), without its absent-phase filter, and without the `try` around it in `main` (AC9) · `FLOOR_ASSERTIONS` raised by the arms' count

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above. AC8 is observed on the live tree, by direct probe.

## 8. Open questions

- **F1 — Which answer decides that a leased run is finished?**
  (a) The driver's `--liveness` verdict, read through stop-guard.js's exported reader, for every
  lease outside PHASES_TERMINAL. (b) The review's alternative: a JavaScript restatement of the
  landed-log test for a LANDING record. (c) The driver, consulted only at LANDING and HELD, the two
  recorded phases its derivation can read as terminal.
  (b) is a second copy of `read_landing_commit` and `read_landed_observation`, which need git
  (`tools/unattended/lib-unattended.sh:1594-1607`), and it misses the landed hand-off: two guards
  asking one question and getting two answers, the class M3 names. (c) restates a phase set the
  driver spells nowhere as data, so no parity arm can pin it. (a) reads the one reader both hooks
  share, at one spawn per question from a leased session.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a). It leaves the fewest open questions and reuses
  stop-guard's reader, the seam M5 found.
- **F2 — What does the question arm do when the liveness cannot be read?**
  (a) Allow, as the review's fix words it and as stop-guard allows a stop. (b) The recorded phase
  stands, so a pass phase still denies, and the deny says the liveness could not be read.
  Under (a), a node whose driver cannot run lets every leased session ask: no bash on the hook's
  PATH, a dead probe. That is the silent switch-off spec 22 restated PHASES_TERMINAL to avoid
  (`tools/unattended/gate-guard.js:84-92`), and on such a node it fails spec 22's AC1. Under (b) the
  M3 false refusal survives only where the driver is broken, and the deny says why.
  Recommendation: (b).
  RESOLVED (agent, 2026-10-13, delegated): (b), the more feature-rich survivor: on a node with a
  broken driver it still satisfies spec 22's criteria and this spec's.
- **FACT-QUESTION · F3 — Which typed records stop opening a turn?**
  (a) A meta record carrying `sourceToolUseID`, and a compaction summary: the review's fix. (b) A
  meta record in a run of meta records directly after a tool result, and a compaction summary.
  (c) Every meta record, and a compaction summary. (d) None, with the turn redefined as everything
  after the last `stop_hook_summary` record.
  The probe: the read-only measurement of §4 "Evidence", which takes each Stop the harness recorded
  and scans back by each rule, comparing the opener with the window since the previous Stop.
  The deciding observation: a rule loses if its opener crosses the previous Stop, which requires a
  finished turn's agents again, or if it cuts more windows than another rule that crosses none; (d)
  loses if its record is missing from sessions holding owner prompts.
  Liveness: the probe produces negatives. Today's rule cuts 416 windows, 29 of them after an `Agent`
  or `Workflow` call; (c) crosses 289 Stops; (d)'s record is absent from 32 sessions.
  Observed: crossings 0, 0, 289 for (a), (b), (c); cuts 347, 313, 275; cuts after a dispatch 20,
  19, 15.
  RESOLVED (agent, 2026-10-13, delegated): (b), the one that falls out of the observation: it
  crosses no Stop and cuts fewer windows than (a).

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "decide whether a run-state lease is still live by asking
the driver liveness verdict"` ranked name-stem neighbours, among them `extract_run_facts`,
`check_lease_only_diff` and `resolveLease`; none reads a verdict. `runLiveness` and `parseLiveness`
in `tools/unattended/stop-guard.js:107-127` did not rank, and they are the seam S3 extends, found by
reading stop-guard.js against the review's fix. `python tools/codebase-map/reuse_lookup.py "find
where a conversation turn opens in a session transcript, skipping harness meta records"` ranked the
run-log kit's `read_records`, `extract_session` and `resolve_session_tree`. The seam S2 extends is
format-guard's own `scanTurnRecords` (`tools/hooks/format-guard.js:263-292`), which spells the
run-log rule in JavaScript because a hook may not import a sibling kit's Python, and S1 extends
`extractTurnAgents`'s note read (`:349-355`). The suites extend `write_transcript`
(`tools/hooks/format-guard.test.sh:307-336`) and `run_ask` (`tools/unattended/gate-guard.test.sh:554`),
the latter with stop-guard's stub-kit pattern (`tools/unattended/stop-guard.test.sh:143-162`).

The recall probe surfaced this build's brief and review, TOOL-aHeardState-2's turn rule, and
TOOL-aWokenSentinel-3's stop-guard spec. Read against source, the run-log reader still admits an
idle tick marked `isMeta` as an opener (`tools/runlog/prose.py:121-149`), which S2 keeps, and
stop-guard's liveness reader is as cited. Nothing stale was found.

Candidates tested and rejected (M12), each with the test that rejected it:

- F3 (a), the `sourceToolUseID` rule: lost on the 117 meta records after a tool result that carry
  no such field, an image's size note after a Read among them; 347 cut windows against (b)'s 313.
- F3 (c), every meta record: crossed 289 Stops, each requiring a finished turn's agents again.
- F3 (d), the turn since the last `stop_hook_summary`: absent from 32 of 290 sessions holding an
  owner prompt and never written with zero hooks, so its presence follows the wiring, not the Stop.
- F1 (b), the restated landed-log test: rejected by reading `read_landing_commit`, which needs
  `git show`, `git log` and `check_lease_only_diff`, and misses the landed hand-off.
- S1's alternative, reading every tag after the `<result>` cut too: no delivery among 6126 carries a
  second header id, so the narrower read loses nothing measured.

Recall terms used: `format-guard gate-guard liveness TERMINAL landed log isMeta turn opener notification tool-use-id stop-guard`
