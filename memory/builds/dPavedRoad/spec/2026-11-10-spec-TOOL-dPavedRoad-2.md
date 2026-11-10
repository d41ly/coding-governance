# TOOL-dPavedRoad-2 — format-guard's block message carries the lines it asks for

**Status:** SPECCED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md](../prompts/2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md) | research | TOOL-dPavedRoad-1 TOOL-dPavedRoad-3 TOOL-dPavedRoad-4 |

<!-- /gen:spec-records -->

## 1. Goal

When `tools/hooks/format-guard.js` refuses a turn end for a missing `agent`, `returned` or
`committed` line, its reason prints that exact line, ready to paste. About 33 of dSafePassage's turn
ends were refused for those lines, and each cost a re-send that had to run `handoff.py agents` first.

## 2. Scope (IN)

Line numbers are read at `ae6735c1`. The worktree's tip differs from it in records only.

- **S1** — For each `agent` or `returned` defect, the reason prints the line `handoff.py agents`
  derives for that agent, unchanged. The hook runs the verb with the selector the turn already
  names: `--run <run-id>` for a harness agent, and `--handoff <path>` for a direct agent, the path
  read from the `gov:handoff` marker of that agent's prompt. It never passes `--write`. Observed by
  AC2, AC4, AC5, AC10 and AC12.
- **S2** — For each `committed` defect, the reason prints a `committed` line rendered through the
  charter's own `committed` shape, from the commit's sha, the worktree's branch and the commit's
  subject. Observed by AC1, AC6 and AC11.
- **S3** — Every derived line passes the hook's own shape check before it is printed, so pasting a
  printed line clears its defect. A line that fails is withheld, with a witness. Observed by AC5,
  AC10 and AC11.
- **S4** — The derivation runs only on a stop that already blocks, inside one time bound. Any failure
  keeps today's reason for that agent, with today's `handoff.py agents` sentence and one witness line.
  A failure never turns a block into an allow, and never turns an allow into a block. Observed by
  AC3, AC6 and AC12.
- **S5** — `tools/hooks/agent-cap.js` exports `resolveKitDir` and `extractHandoffMarker`, so the hook
  finds the roles kit and reads the marker through the hooks kit's one copy of each. Observed by AC7.
- **S6** — The `format-guard self-test` leg's guard in `tools/gate-legs.json` gains
  `{prefix}/hooks/agent-cap.js`, the module the hook now requires. Observed by AC8.
- **S7** — `tools/hooks/README.md` and `help/roles.md` say the refusal prints the lines. Observed by
  AC9.

## 3. Non-goals (OUT)

- No change to what blocks. The defect set, the arming, the turn reading and the
  once-per-turn-end bound stay as they are. The brief's Non-goals hold this: no check grades
  differently.
- No edit to `tools/roles/handoff.py`. The hook spawns its existing `agents` verb, so unit 3's write
  set and this one stay apart.
- No derived `merged` line. A merge commit gets a `committed` line, which the commit arm already
  accepts (`tools/hooks/format-guard.js:260-261`).
- No line for an agent whose prompt carries no marker, such as a built-in agent type. That agent
  keeps today's reason, since `handoff.py agents` has no selector for it.
- No JavaScript port of the agent line's derivation. See "Alternatives rejected".
- No version marker edit. The lander mints kit versions (build README, Build-level rules).

### Edges

- **consumes-from** external — `handoff.py agents` (`TOOL-aOrientedCast-20`, `TOOL-aOrientedCast-25`)
  derives the `agent` and `returned` lines. Without it, every agent defect keeps today's reason.
- **hands-off** external — the `dBoundRoles` build retires `tools/hooks/agent-cap.js`
  (`tools/hooks/agent-cap.js:915`). The two exports S5 adds must move with the rest, or the hook's
  derivation fails into its witness.

## 4. Design

### Today

`checkStop` (`tools/hooks/format-guard.js:469-540`) gathers the pair, agent and commit defects and
hands them to `renderBlockReason` (:454-466). The reason quotes the charter definitions. For an
agent defect it says to paste what `handoff.py agents --handoff <path>` or `--run <run-id>` prints
(:463). The hook knows each run id (:365-370, :412-413, :420) and each `Agent` result (:406-411,
:416-421). It knows each new commit's sha (:526-528), but no subject and no branch.

Measured on a real transcript (a dFairHearing session, `db957487-b5c0-4a88-ab27-88dd90bc468f`): an
`async_launched` `Agent` result carries `prompt`, and the prompt opens with the `gov:handoff` marker.
For a foreground call the call's own `tool_use` input carries the prompt in the same turn.

### The selector (S1)

`extractTurnAgents` (:356-424) gains a `via` field on each required entry. `addRequired` takes it
as a fourth argument, and a repeated key keeps the first `via`.

| Route | `via` |
|---|---|
| `Workflow` result or notification | `{ run: runId }`, already shape-checked by `readJournalAgents` (:332) |
| `Agent` result or notification | `{ handoff: path }`, from the prompt below |
| no usable marker | `null` |

The prompt is the call's `tool_use` input `prompt` when the call sits in this turn, else the result's
`prompt`. The `calls` map (:371, :377) keeps that input beside the name. `extractHandoffMarker` from
`tools/hooks/agent-cap.js:626-634` reads it, and exactly one marker line yields its `path`. A path
that is absolute, or that holds a `..` segment split on either slash, yields `null`. That check
denies by default: the path reaches a child process as an argument.

### Running the verb (S1, S4)

`readHandoffLines({ script, top, sid, transcriptPath, selector, deadline })` spawns, with no shell,
`<launcher> -B <script> agents --run <id> --session <transcriptPath>`, or `--handoff <path>` in place
of `--run <id>`. The cwd is the toplevel, because `handoff.py` takes its root from
`git rev-parse --show-toplevel` (`tools/roles/handoff.py:994`). The env adds
`CLAUDE_CODE_SESSION_ID` set to the payload's session id, which the run route's card fallback reads
(`tools/roles/handoff.py:884-887`). `-B` writes no bytecode, so the spawn writes nothing.

- **The launcher.** `GOV_PYTHON` when set, then each of `PYTHON_LAUNCHERS`, `python3`, `python` and
  `py`, in `resolve_python`'s order. A candidate whose spawn fails with `ENOENT`, or which exits
  9009, the Microsoft Store stub's exit, is passed over. Any other exit ends the search.
- **The bound.** `HANDOFF_BOUND_MS`, 20000, PINNED here, is one budget shared by every spawn of one
  stop. Each spawn's `timeout` is what remains, and a selector reached after it is spent is not run.
  The fragment declares no Stop timeout (`tools/hooks/format-guard.fragment.json`), and the harness
  default of 60 s is UNVERIFIED. A hook killed at its timeout loses its block, so the bound keeps
  well under it, beside `GIT_BOUND_MS` (:99).
- **The output.** It returns `{ lines }`, every stdout line starting `- `, read as UTF-8, which is
  what `handoff.py` writes (`tools/roles/handoff.py:933`). On a spawn error, a timeout or a non-zero
  exit it returns `{ error }`, naming the exit and the first stderr line.
- **The script.** `resolveKitDir('roles', 'handoff.py', __dirname)` from
  `tools/hooks/agent-cap.js:1000-1033`, the receipt rung first, then the two probes. Its throw is a
  witness. Messages name the script by its bare file name, as the spawn guard does
  (`tools/hooks/agent-cap.js:618-620`), so no shipped string spells a kit segment.

`agent-cap.js` is required lazily, inside the derivation, so an allowing stop parses nothing new.
Requiring it runs no rule: its `main` runs only as the entry point (`tools/hooks/agent-cap.js:920`).

### Choosing the lines (S1, S3)

`checkAgentLines` (:431-452) and `checkCommitLines` (:256-269) each return `{ defects, unmet }`.
`unmet` holds the required entries, or the commits, that produced a defect. Their defect text does
not change. `checkCarries` leaves its closure (:432-436) for module scope, because the filter below
reads it too.

`deriveOwedLines(...)` groups the unmet agent entries by selector and runs `readHandoffLines` once per
selector. For each entry it takes the first returned line that starts `- <head> — `, satisfies
`checkCarries` for that agent id, and matches `shapes[head].re`. An entry with no such line keeps no
derived line and adds a witness naming the agent and the reason: no marker, no script, no launcher,
the verb's error, no line for the agent, the line off its shape, or the bound spent.

### The committed line (S2)

`extractNewCommits` (:246-253) spawns
`git log --first-parent --ancestry-path --format=%H%x1f%s <prev>..<head>` in place of its `rev-list`
call. It is the same walk, plus the subject, in the same single spawn. It returns
`[{ sha, subject }]`, or null as today. Its one caller is `checkStop` (:527).

`readHeadBranch(gitDir)` reads the worktree's `HEAD` file: `ref: refs/heads/<b>` gives `<b>`, and
anything else gives `HEAD`, git's own name for a detached checkout. No spawn.

`renderShapeLine(def, fields)` returns `- ` plus the definition with each `<name>` placeholder set to
`fields[name]`. In each value, ` · ` becomes `, ` and a line break a space, and an empty value
becomes `unknown`. That is `render_shape_line`'s rule (`tools/roles/handoff.py:708-719`), so neither
renderer lets a value add a field. A placeholder `fields` lacks returns null, and the line is not
printed. The `committed` line takes `sha` as the first nine hex digits, which the commit arm reads as
a 7+ prefix (:267).

### The reason (S1, S2, S4)

`renderBlockReason` gains an `owed` argument, the derived lines in order: committed lines first,
then agent lines in the order `required` lists them. When `owed` is not empty, the reason adds, after
the definitions:

```text
The lines this message owes, derived for it — paste each unchanged as a bare `- ` list item at column 0:
- committed — 0123abcde · main · the subject
- agent — gov-builder · effort high · … · run wf_x/a3
```

The `handoff.py agents` sentence (:463) stays only when some agent defect has no derived line. The
rest of the text does not move.

### Where it runs (S4)

`checkStop` calls `deriveOwedLines` only when `defects.length` is non-zero, after the commit arm,
before the return at :539. The witnesses join the existing list. `stop_hook_active` still returns
before any of it (:471), so a chained stop spawns nothing.

### The suite

`tools/hooks/format-guard.test.sh` runs every arm against a copy of the hook. It copies
`format-guard.js`, `scratch-guard.js` and `agent-cap.js` into `$TMP/kit/<hooks home>/`, and writes a
stub `handoff.py` into `$TMP/kit/<roles home>/`. Both homes come from the suite's `resolve_kit_dir`
(:234's idiom), so no literal kit segment is spelled. `HOOK` names the copy, and `GOV_PYTHON` is the
suite's `TESTPY`. So no arm reads the real roles kit, and the guard of S6 is the whole sibling set.

The stub appends its argv and its `CLAUDE_CODE_SESSION_ID` to a log file. It prints the suite's own
`A2`, `A3`, `R2` and `R3` constants for `--run wf_t-1`, and `A1` and `R1` for
`--handoff memory/builds/tBuild/prompts/x.md`. Any other selector exits 1 with one stderr line. A
new `write_transcript` scenario, `agent-marked`, carries that marker in a1's result `prompt`.
Existing arms keep their needles: each still finds its `agent a<n>` text, and a derived line spells
`run …/a<n>`, never `agent a<n>`.

New arms, labelled `PR2`:

- `agent-marked` with the pair alone blocks, and the reason holds `- $A1` verbatim. The message plus
  that line allows.
- `run` with `A2` alone blocks, and the reason holds `- $A3` and not `- $A2`.
- The stub's log holds `agents`, `--session` and the transcript path, holds `tSession-1`, and never
  holds `--write`.
- A stub staged to exit 1 keeps the `handoff.py agents --run` sentence, and the witness names the
  exit.
- An unreported commit whose subject holds ` · ` blocks, and the reason holds
  `- committed — <sha9> · <branch> · <subject with , >`. The message plus that line allows.
- A good message leaves the stub's log empty.

`FLOOR_ASSERTIONS` (129 at `ae6735c1`) rises by the new arms' executed count, which the close
confirms from a real run.

### Inventory

- Functions in `tools/hooks/format-guard.js`: `readHandoffLines`, `deriveOwedLines`,
  `renderShapeLine`, `readHeadBranch`, and `checkCarries` at module scope. Each is `OK` by
  `lexicon.py --suggest <name> --as js.function`, run at writing time.
- Constants: `HANDOFF_BOUND_MS` and `PYTHON_LAUNCHERS`. No cell declares a JS constant, so neither
  is graded.
- Exports: `format-guard.js` adds the four new functions and `extractNewCommits`. `agent-cap.js` adds
  `resolveKitDir` and `extractHandoffMarker`, beside its exports at :916-919.
- The suite scenario `agent-marked`, the arm label prefix `PR2`, and the stub's log file.

### Files touched (estimate)

- `tools/hooks/format-guard.js`
- `tools/hooks/agent-cap.js`
- `tools/hooks/format-guard.test.sh`
- `tools/hooks/README.md`
- `tools/gate-legs.json`
- `help/roles.md`
- `memory/map/generated/symbols.json`

### Rollout

One pass. The header comment's WHAT BLOCKS paragraph (:28-39) gains one sentence on the derived
lines. WHAT THIS DOES NOT CHECK (:66-84) gains: the derived line's field values, which are the
verb's; an agent with no marker; and a derivation cut by the bound.

`tools/hooks/README.md` gains a paragraph after "What blocks" (:489-500). `help/roles.md:111-114`
says the refusal prints the lines when it can derive them, and names the verb otherwise.

`python tools/codebase-map/gen_map.py --write` renders `memory/map/generated/symbols.json` for the
new functions. `tools/gate-legs.json` is a path the kickoff manifest watches
(`memory/guides/SESSION-KICKOFF.md:6`), so its re-audit falls to the main loop at the close. This pass
does not do it.

`help/roles.md` may also be in a sibling unit's write set. If so, `order` sequences the two.

### Alternatives rejected

- **Print the filled command, not the line.** The reason would say
  `handoff.py agents --run wf_x --session <path>`. That still costs a tool call and a re-send per
  refusal, and the brief asks for the lines verbatim.
- **Port the derivation to JavaScript.** The `agent` line needs the agent's transcript and meta, the
  role index and the agent type's front matter (`tools/roles/handoff.py:900-917`). A port is a
  second answer to one question, and it would drift from the verb whose lines it claims to print.
- **A third inline copy of `resolveKitDir`.** The hooks kit already carries one, held to the Python
  original by `tools/lib/resolve-python.test.sh:694-750`. The hook ships beside it in the same
  `[[files]]` home, so it requires that copy.

## 5. Production-readiness checklist

- security — The hook spawns one script, resolved through the install receipt or the kit probes,
  with no shell. Its arguments are a run id already shape-checked, a marker path refused when
  absolute or holding `..`, and the payload's transcript path. It never passes `--write`, and `-B`
  writes no bytecode.
- perf / scale — An allowing stop spawns nothing new and parses nothing new. A blocking stop spends
  one python spawn per distinct selector, all inside `HANDOFF_BOUND_MS`, plus no new git spawn.
- error / empty / loading states — No script, no launcher, a non-zero exit, a timeout, no line, or a
  line off its shape each keep today's reason for that agent, with one witness line.
- observability — Each failure writes one stderr witness, as the hook's existing degraded outcomes
  do (:493-537).
- risks — A slow `handoff.py` on a very large session can spend the bound. The reason then falls back,
  as before this unit. If `agent-cap.js` retires without its exports, every derivation fails into a
  witness.
- testing — The suite arms of §4 "The suite", run at the close. Each pass verifies with the probes
  of §6.
- migration — N/A — no data or config changes. The hook reads the same payload, transcript and
  charter.
- user docs — `help/roles.md` and `tools/hooks/README.md`, S7.

## 6. Acceptance criteria

The probes run from the repository root. Each node probe is saved under the run's scratch directory
before it runs.

- **AC1** — When `node -e "const g=require('./tools/hooks/format-guard.js'); const {shapes}=g.readCharterShapes('.'); const l=g.renderShapeLine(shapes.committed.def,{sha:'0123abcde',branch:'main',subject:'a · b'}); console.log(l, shapes.committed.re.test(l))"`
  runs, it prints `- committed — 0123abcde · main · a, b true`.
  Red when: the ` · ` in the subject is kept, so the line holds four fields and prints `false`.
- **AC2** — When a probe writes a stub script that logs its argv and environment and prints two
  lines, then calls `readHandoffLines` with the selector `{ run: 'wf_x' }`, the result's `lines` are
  the stub's two lines. The logged argv is `-B <stub> agents --run wf_x --session <path>`, with no
  `--write`, and the logged `CLAUDE_CODE_SESSION_ID` is the session id the probe passed.
  Red when: the selector or `--session` is not passed, or `--write` reaches the stub.
- **AC3** — When the same probe's stub exits 1, `readHandoffLines` returns an `error` naming exit 1
  and no `lines`. With `GOV_PYTHON` naming a launcher that does not exist, the next candidate runs
  the stub.
  Red when: a non-zero exit yields lines, or a missing `GOV_PYTHON` ends the search.
- **AC4** — When a probe calls `extractTurnAgents` on a turn holding an `Agent` result whose
  `prompt` opens with a `gov:handoff` marker naming a repo-relative prompt path, and on a
  `Workflow` result with `runId` `wf_x`, the entries carry `via.handoff` that path and `via.run`
  `wf_x`. A marker path that climbs with a `..` segment gives `via` null.
  Red when: the marker path is not read, or a climbing path reaches `via`.
- **AC5** — When a probe calls `deriveOwedLines` with one unmet `agent` entry for `a1` and a stub
  that prints valid `agent` lines for `a1` and `a2` plus one line for `a1` that is off its shape,
  the result holds exactly the valid `a1` line, and the witnesses are empty. With the stub printing
  only the off-shape line, the result is empty and one witness names `a1`.
  Red when: `a2`'s line is printed, or an off-shape line is printed.
- **AC6** — When a probe calls `renderBlockReason` with an agent defect and an `owed` list of one
  line, the reason holds that line on its own line and no `handoff.py agents --run` sentence. With an
  empty `owed` list it holds that sentence.
  Red when: the sentence is dropped while an agent has no derived line, or the line is wrapped or
  quoted.
- **AC7** — When `node -e "const a=require('./tools/hooks/agent-cap.js'); console.log(a.resolveKitDir('roles','handoff.py',require('path').resolve('tools/hooks')), typeof a.extractHandoffMarker)"`
  runs, it prints a path ending `tools/roles` and `function`.
  Red when: either export is missing and the probe throws or prints `undefined`.
- **AC8** — When `python -c "import json; l=[x for x in json.load(open('tools/gate-legs.json',encoding='utf-8')) if x['name']=='format-guard self-test'][0]; print('{prefix}/hooks/agent-cap.js' in l['guard'])"`
  runs, it prints `True`.
  Red when: the guard omits the module, so an edit to it alone skips the leg.
- **AC9** — When `grep -n "derived for it\|prints the lines" tools/hooks/README.md help/roles.md`
  runs, each file shows a line saying the refusal prints the lines.
  Red when: either page still says only that the verb prints them.
- **AC10** — When the suite's fixture, built by its `seed_repo` and `write_transcript` with the
  hook copy beside the stub, takes the `agent-marked` payload, `format-guard.js` blocks and the
  reason holds the stub's `A1` line verbatim. The same message with that line appended allows.
  fixture: the suite builds it; a pass probe extracts the two functions with `sed`, as
  dFairHearing's probes did.
  Red when: the derived line is absent, or pasting it does not clear the defect.
- **AC11** — When that fixture gains an unreported commit whose subject holds ` · `,
  `format-guard.js` blocks and the reason holds `- committed — <sha9> · <branch> · <subject>` with
  the separator folded to `, `. The message with that line appended allows.
  Red when: no committed line is printed, or the printed one does not clear its defect.
- **AC12** — When that fixture takes a message that passes every check, the stub's log stays empty,
  and `format-guard.js` allows.
  Red when: an allowing stop spawns `handoff.py`.

## 7. Gates

`format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/format-guard.test.sh · covers AC10 AC11 AC12 · the `PR2` arms of §4 "The suite", against a hook whose `deriveOwedLines` is staged to return no line, then whose stop is staged to call it on an allow · `FLOOR_ASSERTIONS` raised by the new arms' count

The main loop observes the arm RED on each staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "stop hook block message prints the derived agent and
committed lines"` ranked no seam for this behaviour: its candidates were name-stem matches such as
`render_line` and `check_line` in `tools/runlog/runlog_lib.py`, which render run-log rows. The seams
this unit extends were found by reading source. They are `format-guard.js`'s defect list,
`renderBlockReason` and `extractTurnAgents` (`tools/hooks/format-guard.js:356-466`), and
`agent-cap.js`'s `resolveKitDir` and `extractHandoffMarker` (`tools/hooks/agent-cap.js:626-634`,
:1000-1033), which this unit exports instead of copying. It spawns the existing
`handoff.py agents` verb (`tools/roles/handoff.py:808-935`) rather than restating its derivation.
Stop hooks that spawn a sibling script already exist: `tools/unattended/stop-guard.js:111` and
`tools/process-monitor/procmon-hook.js:116-118`.

The recall probe returned `TOOL-aOrientedCast-21`, whose design (§4, "The reason") named the verb
by bare file name and printed no line. Read against source, the hook still does that (:463). Its
§10 says a hook may not IMPORT a sibling kit's Python, and this unit spawns the script without
importing it. `TOOL-dCalibratedLens-25` moved the `returned` line's fields. The fence at
`AGENTS.md:65-66` ends both lines with the run and agent id, which `checkCarries` reads. No record
rules against printing the lines.

Recall terms used: `format-guard Stop hook block reason agent returned committed line handoff agents derived microformat`
