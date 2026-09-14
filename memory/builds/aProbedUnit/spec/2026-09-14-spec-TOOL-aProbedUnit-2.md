# TOOL-aProbedUnit-2 — every command a unit runs is bounded; a stalled non-code command is skipped and named

**Status:** SPECCED · rev-2 · 2026-09-14 · node a · Tier-1 · base 1b000d1a · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md](../prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md) | journal | TOOL-aProbedUnit-1 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |
| [2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aProbedUnit-1-spec-audit-round1.md) | spec-audit | TOOL-aProbedUnit-1 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7 |

<!-- /gen:spec-records -->

## 1. Goal

A unit on node `d` did thirteen minutes of work and then sat six hours and fourteen minutes on one
`rm`, and the whole workflow waited on it (`memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-0-run-mandate.md`,
the HIGH item). Nothing in the child prompt of `tools/workflows/unattended-unit.js` bounds a
command or says what to do when one does not return. This unit adds the second binding paragraph
to that prompt: the primary objective is code written and committed; every shell call carries the
tool's `timeout`; a check, cleanup or probe that does not return within it is skipped and named,
never re-run or waited on; a backgrounded command is awaited through the harness's notification and
never polled. The Skill's harness bullet gains one clause pointing at it.

Tier-1, as the brief assigns: prompt text in one kit file plus a pointer clause in the Skill that
`TOOL-aProbedUnit-1` already edits; no write path, contract, schema key, conf key or gate moves.
The ten sections are kept anyway, so the audit has the same surface as its sibling.

## 2. Scope (IN)

- **S1** — The child `PROMPT` in `tools/workflows/unattended-unit.js` gains one paragraph directly
  after the paragraph `TOOL-aProbedUnit-1` adds, with the text section 4 pins. Observed by AC1 and
  AC2.
- **S2** — The sentence `TOOL-aProbedUnit-1` adds to the "Drive the build as ONE program" bullet of
  `tools/unattended/SKILL.template.md` gains one trailing clause naming the bound and the skip; the
  render `.claude/skills/unattended/SKILL.md` is re-made by `bash tools/unattended/adopt-unattended.sh`
  in the same commit. Observed by AC3.
- **S3** — One `has` arm in `tools/workflows/unattended-build.test.sh`, beside the arm unit 1 adds,
  asserting the traced unattended child prompt carries this paragraph's opening phrase. Observed by
  AC2.
- **S4** — The same-commit obligations: this spec's status header goes to CLOSED in the pass commit.
  No watched file moves and no ledger is owed at this tier. Observed by AC4.

## 3. Non-goals (OUT)

- **No change to the child's return schema.** The skipped commands are prose in `summary`, which
  `UNIT_SCHEMA` already requires; a `skipped` key is the alternative rejected in section 4.
- **No conf key, no driver verb, no probe.** The outside-in stall probe is `TOOL-aProbedUnit-3`;
  this unit is the inside-out half, the rule the agent itself follows.
- **The scratch root is `TOOL-aProbedUnit-4` and `TOOL-aProbedUnit-5`.** The `rm` that stalled was
  a delete OUTSIDE the workspace, and the owner's inference is that it sat on an approval prompt. A
  prompt precedes execution, and this spec does not verify whether the tool's timeout clock covers
  a pending approval — marked UNVERIFIED. The bound here closes the class where a command RUNS and
  does not return: a hung suite, a slow probe, a cleanup over a wedged handle. The class where a
  command never starts because a write left the sanctioned roots is closed by keeping writes inside
  them, which those two units do.
- **No numbers of this repo's own harness are moved.** `GATE_BOUND` in `.unattended.conf` bounds the
  bar the close runs; the ceilings in `tools/gate-legs.json` bound legs. This unit bounds what an
  AGENT launches from inside a pass, which `memory/map/features/process-monitor.md` records as the
  one class nothing bounded.
- **No kit version moves.** The closing pass's, once per kit.
- **No dossier edit.** Same reason as unit 1: `memory/map/features/unattended.md` sits at
  20470 of 20480 bytes and describes mechanisms and gates, not prompt paragraphs.
- **No `New arm:` beyond the one `has`.** The paragraph is text; the arm is the class reader for
  "the child lost the rule", and there is nothing else to stage.

### Edges

- **consumes-from** `TOOL-aProbedUnit-1` — the position of both edits: the child paragraph goes
  after that unit's paragraph, and the Skill clause extends that unit's sentence. Without it there is
  no sentence to extend and this unit's grep anchors name text that does not exist.
- **consumes-from** external — the `Bash` tool's `timeout` parameter as the CLI publishes it to an
  agent, in milliseconds with a 120000 default and a 600000 maximum; the figures in the paragraph
  are that contract's, PINNED from the tool's own description on node `a` on 2026-09-14, and an
  adopter whose harness publishes another bound reads the paragraph's numbers as this CLI's.
- **hands-off** `TOOL-aProbedUnit-3` — observing the stall from OUTSIDE the unit, with a bound the
  project declares, and the remedy that re-dispatches with a brief naming what was skipped.
- **hands-off** external — the kit version bump at the closing pass.

## 4. Design

### The paragraph (S1)

Inserted in `tools/workflows/unattended-unit.js` directly after the `NO GATE, SUITE OR BAR RUNS
INSIDE THIS PASS` paragraph unit 1 places between `DRIVER_STEPS +` and the `'Commit with the unit
id` line. Prose, split into `'…' +` lines in the file's style:

```
YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED, and every command you run is bounded. Every
shell call carries the tool's `timeout` parameter: 120000 ms by default, at most 600000 ms for a
build or test command the change itself needs. A check, cleanup, probe or any other command
unrelated to writing code that does not return within its bound is SKIPPED: name it in `summary`
with what it was for, and never re-run it or wait on it. Never wait on a command with no bound. A
backgrounded command is awaited through the harness's completion notification, never by a polling
loop.
```

The opening phrase `YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED` is the arm signature and
sits on ONE source line. It spells no path, so `tools/check-install-prefix.sh` has nothing to read,
and it adds no definition, so the child keeps exactly one top-level definition and the codebase-map
JS liveness floor is unmoved.

Why the numbers are the tool's and not a conf key. The bound is applied by the agent at the tool
call, where no script and no hook of this kit runs; a conf key would need a reader in the child,
which has no filesystem, or in the parent, which would have to render it into `GROUND` for an agent
that may still ignore it. The tool's own default is already 120000 ms; what the paragraph changes is
the ceiling the agent may raise it to and what it does when the ceiling is reached, which no number
in a file changes.

Why the skip is named in `summary` and not a key. `memory/gotchas/degradation-known-but-unreported.md`
is the class where a run computes its own degradation and does not say so where a reader looks.
The reader of a child is the main-loop caller, which reads the four keys the child returns; `summary`
is one of them and is required, so the name lands in front of the reader with no schema change. The
sentence "with what it was for" is what lets the re-dispatch brief of `TOOL-aProbedUnit-3` say what
to skip.

Why "never by a polling loop". A `Bash` call with `run_in_background` re-invokes the agent when the
job exits, and an agent that instead waits in a foreground loop has turned a bounded call into an
unbounded one, and one that spawns a `sleep`-and-check loop per poll multiplies the processes the
stall holds open. The harness notification is the bound; the loop defeats it.

### The Skill clause (S2)

Unit 1's sentence in the "Drive the build as ONE program" bullet of
`tools/unattended/SKILL.template.md` ends "…and to verify with the one check that exercises its
change." This unit replaces that final full stop with a clause, so the bullet reads:

```
… and to verify with the one check that exercises its change, and to bound every command it runs:
a non-code command that does not return within its bound is skipped and named in its return.
```

No token; the render `.claude/skills/unattended/SKILL.md` carries the same bytes after
`bash tools/unattended/adopt-unattended.sh`. The clause is a POINTER at what the child is ordered
to do, in the Skill's voice, and does not restate the numbers: the numbers are the tool's, and a
second copy of them in a rendered Skill is the two-answers class.

### The arm (S3)

One line in `tools/workflows/unattended-build.test.sh`, directly after unit 1's arm:

```
has "aProbedUnit-2 the child prompt bounds every command and names a skipped one" "$childU" "YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED"
```

Positive by construction; the suite carries no floor. The failing case is the base child, whose
traced prompt holds the phrase zero times — the section 10 probe.

### Inventory

No identifier is minted.

### Rollout

The pass declares, through `--dispatch --writes`: `tools/workflows/unattended-unit.js`,
`tools/unattended/SKILL.template.md`, `.claude/skills/unattended/SKILL.md`,
`tools/workflows/unattended-build.test.sh`, this spec, the build README, and the generated
`memory/LIVE.md` and `memory/ledger/2026-09.md`. Three of those are unit 1's too, which is why the
roster sequences this unit second; the pass does not begin until unit 1's commit is in `HEAD`.

The one check the pass verifies with is AC2's double. Nothing else runs inside it.

Landing owes no data step.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/workflows/unattended-unit.js` | one paragraph added to `PROMPT` after unit 1's |
| `tools/unattended/SKILL.template.md` | one clause appended to unit 1's sentence |
| `.claude/skills/unattended/SKILL.md` | re-rendered from the template |
| `tools/workflows/unattended-build.test.sh` | one `has` arm after unit 1's |

### Alternatives rejected

- **A `skipped` array in the child's return.** `UNIT_SCHEMA` accepts stray keys, so the agent could
  return one today; but the child's own `return` statement copies four keys and drops the rest, so
  surfacing it means editing that statement and the caller that reads it — a contract change for a
  key with no reader yet. Add it when `--audit` or a caller reads the key.
- **A `COMMAND_BOUND` conf key rendered into `GROUND`.** A number nobody enforces at the tool call,
  read from a file the agent is asked to honour; the tool already publishes its own default and
  ceiling, and the rule is about behaviour at the ceiling, not its value.
- **Order the agent to wrap every command in `timeout N`.** The shell's `timeout` inside a command
  substitution bounds the verdict and not the clock, which is
  `memory/gotchas/bounded-through-a-pipe-is-unbounded.md`; the tool parameter bounds the call from
  outside the shell.
- **Put the bound in the method's M6.** M6 is about what a pass is, and the bound is a per-call
  discipline of one agent under one harness; the method has 95 bytes of headroom under its
  high-water after unit 1 and units 6 and 7 still owe M4 edits.

## 5. Production-readiness checklist

- security — N/A. Prompt text.
- perf / scale — the prompt grows by one paragraph per child spawn. The cost this unit removes is
  wall-clock: a six-hour wait becomes a 120- or 600-second one plus a named skip.
- error / empty / loading states — a skipped command is the state this unit defines, and it is
  reported in `summary` with its purpose; a unit that skipped a check it needed says so and the
  caller decides, which is `TOOL-aProbedUnit-3`'s remedy.
- observability — the skip is prose in a required field, not a key; the alternative and its trigger
  are in section 4. Nothing in the run-state file records a skip; the re-dispatch brief is where it
  lands.
- risks — an agent may read "at most 600000 ms for a build or test command the change itself
  needs" as licence to raise every call; the paragraph binds the ceiling to the change's own need
  and says a check that exceeds it is skipped, not raised. The approval-prompt class is stated as
  UNVERIFIED in section 3 and is not what this unit claims to close.
- testing — one `has` arm on the traced child prompt, failing case the base file, observed by the
  section 10 probe at `0`. No suite runs whole inside the pass.
- migration — N/A.
- user docs — the Skill clause is the document, rendered.

## 6. Acceptance criteria

- **AC1** — When `grep -cF "YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED" tools/workflows/unattended-unit.js`
  runs at the landed tip, it prints `1`. Leg half, observed at `--close` per the build README's
  rule: `node tools/workflows/check-workflow-syntax.js` prints `workflow script(s) parsed clean` and
  exits 0; the pass sees the same break through AC2's double, which fails to evaluate a child whose
  concatenation is broken.
  Red when: the count is `0`; or the syntax gate names `unattended-unit.js`, which is a quote or
  concatenation broken by the paragraph's own `'`.
- **AC2** — When the child is run through the `run_wf` double of
  `tools/workflows/unattended-build.test.sh` with its `CHILD_ARGS` fixture in `unattended` mode and
  the output is piped through `grep -c "YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED"`, it
  prints `1` at the landed tip and `0` against the base child, and the traced prompt carries this
  phrase AFTER `NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS` and before `Commit with the unit id`.
  This is the ONE check the pass verifies with. And when
  `grep -cF 'YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED' tools/workflows/unattended-build.test.sh`
  runs, it prints `1` at the landed tip and `0` at base, which is the S3 arm existing at all.
  Red when: the landed count is `0`, meaning the text is in the file and not in the prompt; the base
  count is not `0`, meaning the arm cannot fail; the order is wrong, meaning the paragraph was
  placed outside the two anchors and the commit sentence no longer follows the verification rules;
  or the suite grep prints `0` at the tip, meaning the paragraph landed and the reader for "the
  child lost the rule" did not, or `2`, meaning the phrase was duplicated into a second arm or a
  comment.
  cost: seconds — one `node -e` evaluation with stub hooks, no agent spawned.
  fixture: the double inside the suite, run alone as unit 1's AC6 describes; never the suite whole.
- **AC3** — When `grep -cF "bound every command it runs" tools/unattended/SKILL.template.md` and
  the same grep over `.claude/skills/unattended/SKILL.md` run at the landed tip, each prints `1`.
  Leg half, observed at `--close`: `bash tools/unattended/adopt-unattended.sh --check` prints
  `unattended: in sync` and exits 0.
  Red when: either count is `0`; or the wiring leg reports drift, which is a template edit without
  the re-render, or the reverse.
- **AC4** — When `git show --name-only --format= HEAD` runs on the pass commit, it lists none of
  the ten paths on the `watch` line of `memory/guides/SESSION-KICKOFF.md`, and
  `git grep -lE '^\*\*Status:\*\* CLOSED' -- memory/builds/aProbedUnit/spec/` lists this spec. Leg
  half, observed at `--close`: `bash skills/session-kickoff/manifest-check.sh` check 5 reports no
  watched file changed since `last-audit`.
  Red when: the commit lists a watched path, which means this pass touched something outside its
  declared set; or the header still reads `SPECCED`.
  figure: ten is what the `watch` line held on 2026-09-14; the observation reads the line, not
  this number.

## 7. Gates

`workflow script syntax` · `unattended skill wiring` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

These are `--close`'s. The pass runs none of them; it verifies with AC2's double alone, and the leg
halves of AC1, AC3 and AC4 are the close's observations of those criteria. Chunks read
from `tools/gate-legs.json` on 2026-09-14: `workflow script syntax` and `unattended skill wiring`
are `chunk: wiring`, `install-prefix` is `chunk: product`, the other three `chunk: declarations` or
`chunk: records`; none is `chunk: selftests`.

New arm: `tools/workflows/unattended-build.test.sh` · the base child traced through `run_wf`, whose
prompt holds the phrase zero times · no floor moves.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft, from the brief in
  `memory/builds/aProbedUnit/prompts/2026-09-14-prompt-TOOL-aProbedUnit-1-1-spec-briefs.md` and
  the mandate's HIGH item.
- rev-2 · 2026-09-14 · §6 · §7 · AC1 · AC2 · AC3 · AC4 · folded round-1 cluster M id 3 (AC2 gains
  the grep over the suite file for the S3 arm, `1` at the tip and `0` at base); and, under the build
  README's rule from cluster A, the leg half of AC1, AC3 and AC4 marked observed at `--close`, with
  AC4 given the pass-cheap half it lacked.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "every shell command a unit agent runs carries a timeout
and a stalled non-code command is skipped and named"`, run on 2026-09-14 at base `1b000d1a`,
reported `scan coverage: 71 files scanned | 0 parse skips | unscanned layers: .sh` and ranked `run`,
`resolve_shell_argv` and `run_bounded` in `tools/process-monitor/census.py`. `run_bounded` is the
right shape and the wrong layer: it wraps a command a CHECKER launches, and
`memory/map/features/process-monitor.md` says in its own words that nothing bounded a process an
AGENT launched. No existing seam bounds an agent's own tool call from inside the kit, and none can —
the bound is a tool parameter the agent sets — so the seam this unit extends is the child `PROMPT`
in `tools/workflows/unattended-unit.js`, which exists, and the pointer bullet in
`tools/unattended/SKILL.template.md`, which unit 1 extends first. The test seam is the `run_wf`
double in `tools/workflows/unattended-build.test.sh`; it was run against the base child on
2026-09-14 and the phrase count read `0`.

The recall probe's live hits were the mandate's HIGH item, the process-monitor dossier line above,
and `memory/builds/aQuenchedHarness/README.md`, which bounded the LEGS after two builds stalled 9 h
and 6 h on the bar — the checker-launched half of the same problem, already closed. Where a hit was
STALE against source: the round-1 review record under `memory/builds/aBoundedCeiling/reviews/`
cites `unattended.sh:988` for an unbounded `$WIRING_CHECK` substitution; at base that line is a
`rec0` comparison and the driver's own header at `unattended.sh:217-219` says the call is bounded
now, so nothing here rests on that finding.

Recall terms used: `python tools/memory-recall/query.py "what bounds a command a harnessed unit agent
runs, and what happened when one stalled on an rm for hours" --terms "bounded command timeout stalled
unit skip cleanup probe rm approval prompt session blocked hours"`.
