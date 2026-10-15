# TOOL-aOrientedCast-22 — gate-guard refuses AskUserQuestion from the session holding a live unattended run's lease, and names the park

**Status:** CLOSED · rev-2 · 2026-10-16 · node a · Tier-2 · base 646d4a73 · streams tooling · order 24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md](../build/2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 TOOL-aOrientedCast-23 |
| [2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-build-TOOL-aOrientedCast-25-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aOrientedCast-25-1-acceptance-ledger.md) | journal | TOOL-aOrientedCast-25 TOOL-aOrientedCast-21 |
| [2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md) | diff-review | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 |

<!-- /gen:spec-records -->

## 1. Goal

This run called `AskUserQuestion` mid-run and stalled until the owner returned. The build method
says an unattended run never asks (M10), and that a fork no mandate can resolve is parked (M3), but
no hook refuses the question, so the rule held only as long as it was remembered. This unit widens
the unattended kit's PreToolUse hook to `AskUserQuestion` and refuses the call from the session that
holds a non-terminal run's lease, naming `unattended.sh --park` with the question and its options.

## 2. Scope (IN)

- **S1** — `gate-guard.js` handles a payload whose `tool_name` is `AskUserQuestion` through
  `checkAsk`, under §4 "The refusal": it denies when a run-state record leased to the payload's
  `session_id` is in a phase outside `PHASES_TERMINAL`, and allows otherwise. Observed by AC1, AC2
  and AC3.
- **S2** — The deny text, from `renderAskDeny`, names the run, its phase and record, the reason, and
  the `--park` route with each question and its option labels quoted from the payload. Observed by
  AC1.
- **S3** — `PHASES_TERMINAL` restates the driver's terminal pair and a parity arm pins it.
  Observed by AC4.
- **S4** — `gate-guard.fragment.json`'s matcher becomes `Bash|PowerShell|AskUserQuestion`, and gov's
  `.claude/settings.json` is re-merged from it. Observed by AC5.
- **S5** — `tools/unattended/gate-guard.test.sh` gains the arms of §4 "The suite arms", and its
  `FLOOR_ASSERTIONS` rises by their count. Observed by AC1 to AC4, whose breaks they stage.
- **S6** — The hook's header and the kit README's section on it describe the arm and what it does
  not check. NOT OBSERVED by a criterion: prose, read by the closing review against §4.
- **S7** — The unattended kit moves from 1.104 to 1.105 with every carrier. Observed by AC6.

## 3. Non-goals (OUT)

- The size-limits file's header and BUILD-METHOD M3's governance-carrier clause, which the same
  rescope row asks to agree on whether a run may raise a ceiling. That is a separate document, so M2
  makes it its own unit (§3 Edges).
- Any change to the protocol, the build method or the driver. M10 already says never ask, M3 already
  says park, and `--park` already exists (`tools/unattended/unattended.sh:17`); this unit adds the
  refusal, not the rule.
- A hooks kit change. `agent-cap.js`, `scratch-guard.js` and `format-guard.js` are left as they are,
  and the hooks kit's version move stays `TOOL-aOrientedCast-21`'s (§8 F1).
- Refusing a question from a session that holds no lease, or from a run at `LANDED` or `ABORTED`.
  An owner's attended session on the same branch may still ask.
- Moving `gate-guard.js`'s branch-keyed bar arm onto `run-lease.js`, a backlog row that module's
  header names; only the new arm reads the lease.

### Edges

- **hands-off** external — the unit the main loop mints for the other half of the rescope row: one
  stated answer, in `tools/template-size-limits.txt`'s header and in BUILD-METHOD M3's
  governance-carrier clause alike, on which ceiling rows a run may move and on what condition.

## 4. Design

Line numbers were read at `def5209d7` on 2026-10-13, the run branch's HEAD after this unit's
rescope row.

### Evidence

- The rescope row: `memory/builds/aOrientedCast/RUN.md:199`. The run's lease lives in its
  `## Run facts` section as `session: <id>` beside `phase: <phase>` (`:22`, `:32`).
- The protocol's absent-owner default already states the rule this arm enforces: a session bound to
  a non-terminal run never ends its turn by asking, but builds the next READY unit, aborts with a
  code or holds; and a question the protocol lets it decide is decided, not parked
  (`memory/guides/UNATTENDED-PROTOCOL.md:411-415`). BUILD-METHOD M10 says never ask, and M3 parks a
  fork no delegated resolver can take.
- `run-lease.js` is the session-keyed binder every unattended hook shares (its header, `:1-27`):
  `resolveRepo` walks to the checkout (`:58`), `readMemoryRoot` reads `.unattended.conf` (`:106`),
  and `resolveLease(root, memoryRoot, sessionId)` returns every record whose `session:` fact under
  `## Run facts` equals the session id, as `{slug, session, phase, record}`, an empty id or the
  literal `absent` binding nothing (`:132-175`). `stop-guard.js` and `stall-recorder.js` require it by
  `__dirname` (`stop-guard.js:84`, `stall-recorder.js:40`).
- `gate-guard.js` is the kit's one PreToolUse hook: `TOOLS` is `['Bash', 'PowerShell']` (`:94`), `main`
  exits 0 on any other tool (`:655`), it denies by stderr text and exit 2 and fails open on every
  unreadable input (`:81-85`). Its bar arm keys on the branch (`resolveRunPhase`, `:586-616`) and
  restates the driver's phase tail as `PHASES_ALLOW`, pinned by a parity arm
  (`gate-guard.test.sh:540-546`).
- The driver's terminal set is `PHASES_TERMINAL="LANDED ABORTED"` (`unattended.sh:853`); `HELD` and
  every pass phase are non-terminal (`:852`).
- `gate-guard.fragment.json` wires the hook on `PreToolUse` with matcher `Bash|PowerShell`.
  `settings-merge.py` moves an existing entry into the group of its fragment's matcher when the
  two differ (`set_group`, `tools/settings-merge.py:400-420`), so a widened matcher re-wires on the
  next merge. One script carries one fragment per event, which is why the matcher widens here
  instead of a second fragment being added.
- An `AskUserQuestion` call's input, read from this session's own eight calls: `questions`, a list
  of objects carrying `question`, `header`, `multiSelect` and `options`, each option a `label` and
  a `description`.

### The refusal

`main` (`:648`) dispatches `AskUserQuestion` before its `TOOLS` test, to `checkAsk(data)`:

1. `run-lease.js` is required by `__dirname`, as its two siblings require it. `resolveRepo(data.cwd)`,
   then `readMemoryRoot`, then `resolveLease(root, memoryRoot, data.session_id)`. Any of them
   answering nothing allows.
2. A lease whose `phase` is non-empty, not `absent` and not in `PHASES_TERMINAL` is live. No live
   lease allows.
3. Otherwise `renderAskDeny(live, extractAskQuestions(data.tool_input))` goes to stderr and the
   hook exits 2.

`PHASES_TERMINAL = ['LANDED', 'ABORTED']`, restated for the reason `PHASES_ALLOW` is (the header's
"NO PATH OUTSIDE THIS FILE IS SPELLED" paragraph): the hook fails open, so a value read from the
driver at run time would switch the arm off silently the day the driver could not be read.

The deny text, its placeholders filled from the lease and the payload:

```text
BLOCKED by gate-guard: this session holds the lease of the unattended run <slug>, at <phase> (<record>).
An unattended run never asks: nobody is there to answer, so the question stalls the run until
the owner comes back. A question the protocol lets you decide is decided: take the option that
makes no measured observable worse, and record why. One no delegated resolver can take is parked,
and the run goes on to its next READY unit or holds:

  unattended.sh --park <slug> --item "<the question, and its options>" --reason "<why no resolver the mandate delegates exists>"

The question this call asked:
  - <question> — options: <label>, <label>
```

`extractAskQuestions` returns each question's text and its option labels, each value cut to
`ASK_QUOTE_MAX = 300` characters, control characters removed, and an input of another shape
yielding `(no question text)` rather than a throw. The driver is named by its bare file name, as the
bar arm names the runner, because a kit file spells no path outside itself.

### The suite arms

In `tools/unattended/gate-guard.test.sh`, on its `build_fixture` (`:153`), whose record gains a
`session: tSess-1` fact under `## Run facts`, after the bar arms:

1. an `AskUserQuestion` payload with `session_id` `tSess-1` at `BUILDING` exits 2, and stderr names
   the slug, `BUILDING`, `--park`, the fixture question and both option labels;
2. the same payload with `session_id` `tSess-2` exits 0 with nothing on stderr;
3. the record at `LANDED`, then at `ABORTED`, exits 0; at `HELD` it exits 2;
4. the record's `session:` fact reading `absent`, and a tree with no `.unattended.conf`, each exit 0;
5. a `Bash` payload of the plain bar at `BUILDING` still exits 0, so the widened dispatch leaves the
   bar arm's verdicts alone;
6. the parity arm: `PHASES_TERMINAL` equals the driver's `PHASES_TERMINAL`, read from
   `unattended.sh` the way the `PHASES_ALLOW` arm reads its tail.

`FLOOR_ASSERTIONS` (`:566`) rises by the assertions these arms add, counted at build time, with a
comment naming this unit.

### Documentation

- The header gains a paragraph, THE QUESTION ARM, beside WHAT IT DENIES: what it refuses, its key and
  its terminal set. WHAT IT NEVER DENIES gains the attended session with no lease and a run at
  `LANDED` or `ABORTED`.
- `tools/unattended/README.md`'s section "The act is refused at the tool call, not only forbidden"
  (`:87-100`) gains the arm and the widened matcher.
- `memory/map/features/unattended.md`: `TOOL-aOrientedCast-22` joins `decisions`, and its prose
  gains a sentence on the arm. Its `harness-hooks` key carries no matcher, so it does not move.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `checkAsk`, `renderAskDeny`, `extractAskQuestions` | functions in `gate-guard.js`, each added to `module.exports` | `js.function`; `lexicon.py --suggest <name> --as js.function` answered OK for each |
| `ASK_TOOL` = `'AskUserQuestion'`, `PHASES_TERMINAL`, `ASK_QUOTE_MAX` | constants in `gate-guard.js` | none, as the file's existing constants |

### Files touched (estimate)

`tools/unattended/`
`memory/guides/UNATTENDED-PROTOCOL.md`
`memory/guides/UNATTENDED-ASKS.md`
`memory/guides/UNATTENDED-STOPS.md`
`memory/guides/UNATTENDED-VERBS.md`
`memory/guides/PLAYBOOK-TEMPLATE.md`
`.claude/skills/unattended/SKILL.md`
`.claude/settings.json`
`memory/map/features/unattended.md`
`memory/map/generated/`

`tools/unattended/` declares the hook, its fragment, its suite, its README and every carrier of the
kit's version marker; the rendered guide copies listed above and the rendered Skill carry that
marker too.

### Rollout

- **The matcher.** Edit the fragment, then re-merge gov's settings with
  `python tools/settings-merge.py --fragment tools/unattended/gate-guard.fragment.json`, which moves
  the entry into the widened group (`set_group`). A session started before the merge keeps the old
  wiring until it restarts.
- **The kit version.** `KIT_UNATTENDED_VERSION` at `tools/unattended/unattended.sh:66` moves to
  1.105, and so does every `gov:kit unattended@` marker: the same-line markers of the four `.sh`
  carriers and the marker of every shipped document, which `tools/check-kit-versions.sh:282-320`
  pairs with the constant, the courtesy markers its `.js` files carry, and the rendered copies under
  `memory/guides/` and `.claude/skills/unattended/`. `python tools/govkit/govkit.py selfcheck --fix` writes the paired ones from the constant;
  where the role gate refuses that command to the builder, the builder edits every file
  `git grep -l "gov:kit unattended@1.104"` lists. Then the kit's re-render,
  `bash tools/unattended/adopt-unattended.sh`, which the entry's `[[regenerate]]` names
  (`tools/unattended/kit.toml:193-194`).
- **The map.** `python tools/codebase-map/gen_map.py --write`, since three new functions stale it.
- Adopters receive the arm at `govkit update` and the matcher at their next settings merge. No
  `watch:` path of the kickoff manifest moves. Rollback is a revert of the unit's commit and a
  re-merge of the fragment.

### Alternatives rejected

- Keying on the branch, as the bar arm does: an owner's attended session in the same checkout would
  be refused a question it is free to ask, and the lease is the run's own record of who drives it.
- Keying on `LIVE.md` for the non-terminal set: §8 F2.
- Carrying the refusal in a hooks kit script, or in a new script with its own fragment: §8 F1.

## 5. Production-readiness checklist

- security — reads the checkout's conf and run-state records only, through the kit's existing
  lease reader; writes nothing. The deny text quotes the payload's own question back, cut to 300
  characters a value and stripped of control characters. It narrows what an automated session may
  do and widens nothing.
- perf / scale — the arm runs only on an `AskUserQuestion` call, a rare tool: one directory listing
  and one small read per build, as `stop-guard.js` pays on every stop.
- error / empty / loading states — fails open on every unreadable input, as the hook's header
  promises; a lease with no phase allows.
- observability — the deny names the run, phase and record; an allow prints nothing, as the bar
  arm's does.
- risks — a run whose owner wants a mid-run answer must park and hand off rather than ask; that is
  the rule M10 states, now enforced. Whether the harness fires PreToolUse for `AskUserQuestion` is
  observed live by AC7, since the suite feeds the hook its payload directly. A session started
  before the settings merge keeps the narrower matcher until it restarts.
- testing — the arms of §4, observed RED first at the close; AC7 live.
- migration — none beyond the merge; rollback is a revert and a re-merge.
- user docs — the kit README; no help page covers the unattended kit today.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each feeds `node tools/unattended/gate-guard.js`
a hand-built payload in a fixture checkout, as the suite's arms do, or reads a file. The fixture is
a git repository under a short `%TEMP%` root holding a `.unattended.conf` declaring
`MEMORY_ROOT=memory` and `memory/builds/tFix/RUN.md` whose `## Run facts` carry `phase: BUILDING`,
`session: tSess-1` and a `run-branch:` naming the fixture's branch. The payload is
`{"tool_name": "AskUserQuestion", "session_id": "tSess-1", "cwd": <the fixture>, "tool_input": {"questions": [{"question": "Raise the ceiling?", "header": "Ceiling", "multiSelect": false, "options": [{"label": "17408", "description": "d"}, {"label": "20480", "description": "d"}]}]}}`.
Each staged break is restored before the next.

- **AC1** — When the payload is fed to `node tools/unattended/gate-guard.js`, it exits 2, and stderr
  names `tFix`, `BUILDING`, `unattended.sh --park tFix`, `Raise the ceiling?`, `17408` and `20480`.
  Red when: a live run's lease holder asks unrefused, or the refusal omits the park route or the
  question.
- **AC2** — When the payload's `session_id` is `tSess-2`, the record's `session:` reads `absent`, or
  `.unattended.conf` is removed, `node tools/unattended/gate-guard.js` exits 0 with an empty stderr
  each time.
  Red when: a session holding no lease is refused, or an unreadable input denies.
- **AC3** — When the record's phase is `LANDED`, then `ABORTED`, the hook exits 0; at `HELD` it
  exits 2.
  Red when: a finished run still refuses, or a held run lets its session ask.
- **AC4** — When `node -p "require(require('path').resolve('tools/unattended/gate-guard.js')).PHASES_TERMINAL.join(' ')"`
  and `grep "^PHASES_TERMINAL=" tools/unattended/unattended.sh` run, the first prints `LANDED ABORTED`
  and the second carries the same two names in the same order.
  Red when: the restatement drifts from the driver.
- **AC5** — When `grep -c "Bash|PowerShell|AskUserQuestion" tools/unattended/gate-guard.fragment.json .claude/settings.json`
  runs, it prints 1 for each file, and
  `python tools/settings-merge.py --fragment tools/unattended/gate-guard.fragment.json --check` exits 0.
  Red when: the fragment widens without gov's wiring following, or the wiring holds the hook twice.
- **AC6** — When `grep -c "^KIT_UNATTENDED_VERSION=1.105" tools/unattended/unattended.sh` prints 1 and
  `git grep -l "gov:kit unattended@1.104"` prints nothing, every carrier moved.
  Red when: the constant or one carrier keeps 1.104.
  figure: PINNED at `def5209d7`, where the kit reads 1.104; a mint another build lands first moves
  the expected value by the same one step.
- **AC7** — When the main loop, in a session holding this run's lease after the merge and a restart,
  calls `AskUserQuestion` once at a pass phase, the call is refused with the AC1 text and no question
  reaches the owner.
  Red when: the harness fires no PreToolUse for the tool, which the fixture cannot see.
  fixture: the live session at the close; observed by the main loop.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `unattended skill size` · `hook destinations (every declared hook path ships)` · `check-wiring self-test` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/gate-guard.test.sh · covers AC1 AC2 AC3 AC4 · the arms of §4 "The suite arms", against a hook whose `checkAsk` is staged to return null, then whose `PHASES_TERMINAL` is staged to add `HELD` · `FLOOR_ASSERTIONS` raised by the arms' count

The main loop observes the arms RED on each staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — Which hook and matcher carry the refusal?**
  (a) The unattended kit's `gate-guard.js`, its matcher widened to `Bash|PowerShell|AskUserQuestion`,
  keyed through `run-lease.js` beside it; (b) the hooks kit's `agent-cap.js`, widened to
  `Workflow|Agent|AskUserQuestion`; (c) the hooks kit's `scratch-guard.js`, widened likewise; (d) a
  new script with a fragment of its own.
  The rule is the unattended protocol's, the lease and the phases are the unattended kit's record,
  and that kit already ships the lease reader its hooks share. (b) and (c) would put a reader of
  another kit's record into guards whose concerns are fan-out and writes, and move the hooks kit's
  version a second time in this set. (d) adds wiring and a file where a matcher widens. (a) extends
  the seam that already reads the run, and the hooks kit's move stays `TOOL-aOrientedCast-21`'s.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a). It is the reuse of the seam M5 found, with fewer
  follow-ups than every other option.
- **F2 — What makes a run non-terminal for the arm?**
  (a) The leased record's `phase` against the driver's terminal pair; (b) the build's row in
  `LIVE.md`, as `format-guard.js` reads it. `LIVE.md` lists the builds with a non-terminal unit, so a
  run at `VERIFYING` or `LANDING` whose units are all closed leaves it while it still drives its
  close, and (b) would let that session ask where a stall costs the landing. (a) reads the run's own
  phase, which is what M10 binds.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), with `PHASES_TERMINAL` pinned by AC4.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.
- rev-2 · 2026-10-16 · AC7 · records, TOOL-dRedressedBar-27: the live refusal was owed to the main
  loop's session at the close, and no record observes it. The criterion does not move, and the
  status stays CLOSED.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a tool call from the session that holds a live
unattended run's lease"` ranked name-stem neighbours, among them `extract_run_facts` and
`check_lease_only_diff` in the driver's library and `holder` in `agent-cap.js`; none refuses a tool
call by lease, so no ranked function fits as the seam. The unattended kit's dossier claims
`gate-guard.js` among its `harness-hooks`, and `run-lease.js`'s header names itself the binder every
unattended hook shares, which is where the seam is. The seams this unit extends are `gate-guard.js`'s dispatch and deny
protocol (`tools/unattended/gate-guard.js:648-670`), `run-lease.js`'s `resolveLease`
(`tools/unattended/run-lease.js:172-175`), the `PHASES_ALLOW` restatement and its parity arm as the
model for `PHASES_TERMINAL`, and `settings-merge.py`'s `set_group` for the matcher move. No existing
seam reads an `AskUserQuestion` payload. The recall probe surfaced the protocol's absent-owner
default (`memory/guides/UNATTENDED-PROTOCOL.md:411`), this build's rescope row, and the
aWokenSentinel spec's resumed-session wording, each read against source; the deny text follows the
protocol's wording, and nothing stale was found.

Recall terms used: `unattended lease session AskUserQuestion park gate-guard PreToolUse matcher phase terminal never ask`
