# TOOL-aNimbleMend-7 — the run point: each unit harness return tells the main loop to run the pass legs

**Status:** CLOSED · rev-2 · 2026-11-12 · node a · Tier-2 · base 1265772c · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aNimbleMend-7-1-acceptance-ledger.md](../build/2026-11-12-build-TOOL-aNimbleMend-7-1-acceptance-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-7-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-7-build-brief.md) | research | — |
| [2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md](../reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md) | diff-review | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 TOOL-aNimbleMend-13 |

<!-- /gen:spec-records -->

## 1. Goal

A pass leg can only catch a red if something runs the list after every pass, and the one actor that
may run a gate leg during a build is the main loop. This unit makes the unit harness's return carry
that instruction, so the unattended flow and the attended build get it from one carrier, after the
builder's commit and never inside the builder's pass.

## 2. Scope (IN)

- **S1** — `tools/workflows/unattended-unit.js` reads an optional arg, `passLegs`, a one-line command.
  When the key is present and the builder returned `committed: true`, the harness return carries a
  `nextAction` string that names the command and the pass commit's sha, and one log line names the
  command. Observed by AC1.
- **S2** — With `passLegs` absent, the return, the log lines, the builder prompt and the spawn options
  are byte-identical to the file before this unit. With it present and `committed: false`, the return
  carries no `nextAction`. Observed by AC2 and AC3.
- **S3** — A `passLegs` that is not a non-empty single-line string with no backtick is refused before
  any spawn, by the test `prebuild` already meets. Observed by AC4.
- **S4** — The builder prompt never names the command, with the key present or absent, so a role
  agent's pass stays gate-free. Observed by AC5.
- **S5** — `tools/workflows/unattended-build.template.js` gains one constant, `PASS_LEGS`, holding the
  pass-leg runner's invocation over the pass commit, and its hand-out carries it as
  `dispatch.args.passLegs` in both modes. `tools/workflows/unattended-build.js` is re-rendered from the
  template. Observed by AC6.
- **S6** — The two routers that tell a main loop how to read a unit harness return each gain one
  sentence: act on the return's `nextAction` before the next dispatch. They are
  `tools/unattended/VERBS.template.md`, in the "Between dispatches" sub-bullet, and
  `tools/roles/SKILL.template.md`, as a step of stage 5. `memory/guides/UNATTENDED-VERBS.md` and
  `.claude/skills/build/SKILL.md` are re-rendered from them. Observed by AC7.
- **S7** — `tools/workflows/unattended-build.test.sh` gains the arms §7 declares. NOT OBSERVED: a pass
  runs no suite, so the main loop observes these arms RED and then GREEN at the close.

## 3. Non-goals (OUT)

- The runner. What runs, over which diff, with which guards, its run record and its overrun finding
  are TOOL-aNimbleMend-5's. This unit spells the runner's invocation once and runs nothing.
- Reading a policy key. A workflow script has no filesystem, so it cannot ask the reader. The
  adapter asks `pass.fast-legs` before it acts and runs nothing when the key is `off`; F1 states the
  one choice this leaves.
- The hooks. TOOL-aNimbleMend-6 keeps the adapter refused to a role agent and admitted at the main
  loop, and this unit changes neither hook.
- What the main loop does with a red leg. Fixing it without a spec is the lane of TOOL-aNimbleMend-8.
- Refusing the next dispatch when the legs did not run. M6 says the harness buys order and not
  enforcement, and this unit adds an instruction to that order, not a refusal.
- A run after a spec pass, an audit pass or the closing review. The owner's prompt asks for the legs
  after every unit pass, and those passes change no product path.
- The build method's and the protocol's sentences that no gate runs in a pass, the unattended Skill,
  and the help pages. They are TOOL-aNimbleMend-11's.
- The `gov:kit` version markers, which the lander's `mint` moves once, after the last unit.

### Edges

- **consumes-from** `TOOL-aNimbleMend-5` — the adapter's file and its `--base` invocation, which
  runs the declared list over one pass's diff. Without it `PASS_LEGS` names nothing and AC6 has no
  file to resolve.
- **consumes-from** `TOOL-aNimbleMend-1` — the key `pass.fast-legs`, which the instruction names
  as the switch the adapter asks. Without it the instruction names a switch that does not exist.
- **hands-off** `TOOL-aNimbleMend-11` — the build method and the protocol say where the pass legs
  run, pointing at the unit harness return this unit adds.
- **hands-off** `TOOL-aNimbleMend-12` — one unit pass observed end to end in a scratch adopter and in
  gov, with the pass-leg key on and off.

## 4. Design

### Evidence

Read at 91ca33f2, which adds only records to the base.

- **Who dispatches.** `tools/workflows/unattended-build.template.js` ends by returning a hand-out
  whose `dispatch` object carries `scriptPath`, the invariant `args` and `perUnit`. The main loop
  makes one `Workflow` call per unit from it, in both flows: the verbs guide's "Drive the build as
  ONE program" bullet for a mandated run, and stage 5 of `tools/roles/SKILL.template.md` for an
  attended one. Both routers already tell the main loop to branch on the return's `diverged` and
  `committed` fields.
- **What the unit harness returns.** `tools/workflows/unattended-unit.js` returns `identity`,
  `committed`, `sha`, `why`, `summary` and `diverged`, and nothing that names a next step. The build
  harness's hand-out already uses a `nextAction` string for that purpose.
- **The dark-arg precedent.** `prebuild` in the same file is optional, is refused unless it is a
  non-empty single-line string with no backtick, and leaves the prompt, options and log
  byte-identical when absent. `checklist` is the other precedent: the parent spells the command as
  the constant `CHECKLIST` and hands it out in `dispatch.args`, because the child "spells no paths".
- **The child has one definition.** Its header says the codebase-map liveness floor counts exactly
  one top-level definition and the file keeps no loop, arrow or array method. S1 to S3 are a guard,
  a conditional string and a spread, and add no definition.
- **No gate in the builder's pass.** The child's prompt carries the paragraph opening "NO GATE, SUITE
  OR BAR RUNS INSIDE THIS PASS", and the scratch guard's role-gate arm refuses a role agent's gate.
  The build README rules that pass legs run at the main loop, after the builder's commit.
- **The template is the source.** `tools/workflows/README.md` says "Edit the template, never the
  render", and names `check-protocol-parity.test.sh --render` as the one renderer. The gate guard
  lists `--render` in `READ_ONLY_VERBS` and the scratch guard in `GATE_SUITE_ADMITS`.

### The child

`passLegs` is read beside `prebuild` and graded by the same three-part test, with its own refusal
text naming the key. When present, one log line follows the `prebuild` log line's shape:
`unit <id>: pass legs` followed by the command in backticks.

The return gains one conditional key, after `diverged`:

| `passLegs` | builder returned | `nextAction` |
|---|---|---|
| absent | anything | key absent |
| present | `committed: true` | present |
| present | `committed: false`, a divergence included | key absent |

The `nextAction` string says, in this order: run the command at the main loop before the next
dispatch and before any later commit, where that file exists; the pass commit is the returned
`sha`, which is HEAD when it runs; act on its exit status and on every finding line it prints; the
command runs nothing where `pass.fast-legs` is `off`. It names the command verbatim inside
backticks and the sha verbatim. It says nothing about how a red is fixed, which is another unit's
text.

### The parent

`PASS_LEGS` sits beside `CHECKLIST` and is spelled through `{{TOOL_ROOT}}` as `DRIVER` is, so the
install-prefix gate reads a rendered path and no literal. Its value is the adapter
TOOL-aNimbleMend-5 ships, `pass-legs.sh` in the run-gates kit, run under `bash` with `--base HEAD~1`:
the pass is one commit, so its base is that commit's parent, the same range `CHECKLIST` spells as
`HEAD~1..HEAD`. The builder confirms the flag against the built adapter and its README section, and
where they differ the built file wins. `dispatch.args` gains `passLegs: PASS_LEGS` beside
`checklist: CHECKLIST`, unconditionally and in both modes, under F1's recommended option.

### The routers

One sentence each, and each names the return field and no command, so the command keeps one
spelling:

- `tools/unattended/VERBS.template.md`, "Between dispatches re-read `--plan <slug> --paths`": a
  return carrying `nextAction` is acted on first, before that re-read.
- `tools/roles/SKILL.template.md`, stage 5: a step after the dispatch step saying the same.

Each rendered copy is regenerated by its kit's own renderer and never edited in place.

### The probe

The criteria run the child under stub hooks, as the suite's `run_wf` does. The builder writes this
file into the run's scratch directory as `unit-probe.js`:

```js
// usage: node unit-probe.js <script> <args-json> <agent-return-json>
const fs = require('fs')
const src = fs.readFileSync(process.argv[2], 'utf8').replace(/^\s*export\s+const\s+meta\s*=/m, 'const meta =')
const AF = Object.getPrototypeOf(async function () {}).constructor
const out = []
new AF('args', 'agent', 'log', 'phase', src)(
  JSON.parse(process.argv[3]),
  async (p, o) => { out.push('prompt:' + JSON.stringify(String(p))); out.push('opts:' + JSON.stringify(o)); return JSON.parse(process.argv[4]) },
  (m) => out.push('log:' + m), () => {},
).then((r) => console.log(out.join('\n') + '\nRESULT ' + JSON.stringify(r)), (e) => console.log(out.join('\n') + '\nTHROW ' + e.message))
```

`ARGS` is the suite's child fixture:
`{"repo":"/tmp/r","slug":"tB","scratch":"/tmp/s","unitId":"A-tB-1","specPath":"s1","briefPath":"b1","driver":"bash drv.sh","ground":"G. goes under /tmp/s. ","checklist":"CK","mode":"unattended"}`.
`ARGS+PL` is the same object with `"passLegs":"PL --base HEAD~1"` added. `OK` is
`{"committed":true,"sha":"abc1234","why":"","summary":"s"}` and `NO` is the same with
`"committed":false` and `"why":"w"`. `PRE` is the child's blob at the tip the build pass started
from, written to scratch with `git show`.

### Inventory

| Minted | Where | Graded by |
|---|---|---|
| arg `passLegs` | `unattended-unit.js`, `dispatch.args` of the build harness | AC1, AC4, AC6 |
| return key `nextAction` | `unattended-unit.js` | AC1, AC3 |
| constant `PASS_LEGS` | `unattended-build.template.js` | AC6 |

No function is minted, so no lexicon verb cell is involved.

### Rollout

The key is absent from every caller's args until the parent hands it out, and the parent's hand-out
and the child land in this one unit. A run whose hand-out predates this unit passes no `passLegs`
and meets the old child behaviour.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/unattended/VERBS.template.md`
- `tools/roles/SKILL.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `.claude/skills/build/SKILL.md`

### Alternatives rejected

- **The builder runs the legs after its commit.** The owner's prompt left this choice open. The
  scratch guard refuses a gate to a role agent, and that refusal is what keeps a pass cheap; the
  build README rules for the main loop.
- **The unit harness spawns a second agent to run the legs.** That agent is a sidechain role agent
  too, so it meets the same refusal, and the leg output would reach the main loop second-hand.
- **Router prose alone, with no return field.** The main loop reads a router once and reads every
  unit return, and a context that compacts mid-build keeps the return in front of it. The hand-out's
  `nextAction` is the same carrier one level up.
- **A new driver verb that refuses the next `--dispatch` until the legs ran.** It would be a second
  mechanism, it has no attended form because an attended run has no run-state file, and it adds a
  refusal to a driver whose refusal count `.memory-tree.conf` holds under `REFUSAL_CEILINGS`.

## 5. Production-readiness checklist

- security — `passLegs` is spelled into a string an agent reads inside backticks, so it is refused
  unless it is one line with no backtick, as `prebuild` is. No write path and no surface is added.
- perf / scale — one string per unit return. The legs' own cost is TOOL-aNimbleMend-3's budget.
- error / empty / loading states — an absent key, a refused value, `committed: false` and a
  divergence each have a row in §4, "The child". An adopter without the runner's file reads "where
  that file exists" in the instruction and runs nothing.
- observability — the child logs the command when it was handed one, and logs nothing new otherwise.
- risks — the instruction is not enforced: a main loop that ignores `nextAction` runs no pass leg
  and nothing refuses it. The close's bar still runs every leg. A run started on a rendered build
  harness older than this unit hands out no `passLegs`.
- testing — AC1 to AC7 are probes; the suite arms of §7 re-observe AC1 to AC6 at the close.
- migration — none. The arg is additive and absent means today's behaviour; an adopter takes the
  re-rendered harness and routers at its next update.
- user docs — the two routers are S6. The help page and the build method are TOOL-aNimbleMend-11's.

## 6. Acceptance criteria

- **AC1** — When `node unit-probe.js tools/workflows/unattended-unit.js` runs with `ARGS+PL` and
  `OK`, the `RESULT` line's `nextAction` is a string containing `PL --base HEAD~1` inside backticks and
  `abc1234`, and one `log:` line contains `pass legs` and the command.
  Red when: the child ignores the key, omits the sha, or logs nothing for it.
- **AC2** — When the same probe runs with `ARGS` and `OK` over `tools/workflows/unattended-unit.js`
  and over `PRE`, the two outputs are identical under `diff`.
  Red when: the absent-key path gained a key, a log line, a prompt byte or a spawn option.
- **AC3** — When the probe runs over `tools/workflows/unattended-unit.js` with `ARGS+PL` and `NO`,
  the `RESULT` line carries no `nextAction` key, and with `"why":"DIVERGENCE: x"` it carries
  `"diverged":true` and still no `nextAction`.
  Red when: a pass that committed nothing orders a leg run over a commit that does not exist.
- **AC4** — When the probe runs over `tools/workflows/unattended-unit.js` with `passLegs` set in turn
  to `7`, `""`, a string holding a line break and a string holding a backtick, each output ends in a
  `THROW` line naming `passLegs` and holds no `prompt:` line.
  Red when: a malformed value reaches the return, or the refusal comes after the spawn.
- **AC5** — When the `prompt:` and `opts:` lines of the AC1 run and of the AC2 run over
  `tools/workflows/unattended-unit.js` are compared, they are identical.
  Red when: the builder is told to run the legs, which would put a gate inside a role agent's pass.
- **AC6** — When `grep -c "passLegs: PASS_LEGS"` and `grep -c "^const PASS_LEGS = "` run over
  `tools/workflows/unattended-build.template.js` and over `tools/workflows/unattended-build.js`, each
  prints 1; the rendered constant's line holds no `{{`; and the first path-shaped word of its value
  is a file `git ls-files --error-unmatch` accepts.
  Red when: the hand-out drops the key, the render was not regenerated, or the constant names a
  runner file that does not ship.
  fixture: the runner's file exists only once TOOL-aNimbleMend-5 is built, which the build order
  puts before this unit.
- **AC7** — When `grep -c nextAction` runs over `tools/unattended/VERBS.template.md` and
  `memory/guides/UNATTENDED-VERBS.md`, the two counts are equal and one higher than at `PRE`'s tip;
  and over `tools/roles/SKILL.template.md` and `.claude/skills/build/SKILL.md` the two counts are
  equal and one higher than at that tip.
  Red when: a router was not told, or a rendered copy was edited in place or left stale.
  figure: DERIVED at observation time from the tip the pass started from.

## 7. Gates

`unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `policy fixtures` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `install-prefix (shipped surface)` · `roles render wiring` · `unattended skill wiring` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The first five and `check-wiring self-test` are held or guarded on a default bar, and the close runs
them as its flags decide. The kit epoch and version legs expect the lander's `mint`.

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the child ignoring `passLegs`, or adding a key, a log line or a prompt sentence on the absent-key path · none
New arm: tools/workflows/unattended-build.test.sh · covers AC6 · the hand-out's `dispatch.args` dropping `passLegs`, in either mode · none

## 8. Open questions

- **F1 — Does the build harness hand out `passLegs` on every hand-out, or only when its caller asks?**
  The harness has no filesystem and cannot read the pass-leg key itself.
  - **A, always.** `dispatch.args.passLegs` is unconditional. The runner asks the key before it acts
    and does nothing when the key is off, so the switch lives in one place and a forgetful caller
    cannot turn a default-on mechanism off. With the key off, the unit return still carries a
    `nextAction` naming a command that then runs no leg and writes no record. The build's "byte for
    byte" acceptance then holds for the tree, the hooks and the runner, and not for this one return
    field.
  - **B, on request.** The build harness takes an optional `passLegs` arg and forwards it, and the
    two routers tell the main loop to read the key through the policy reader and pass the arg when
    it is on. With the key off the hand-out and every unit return are byte-identical to today. A
    main loop that forgets the arg runs no pass leg under a key that says on, and nothing reports
    it; and the routers gain a second place that knows the key's name.
  - **Recommendation: A.** The build README gives each mechanism one reader it asks before it acts,
    and the acting mechanism here is the adapter, whose ask TOOL-aNimbleMend-5 already specs.
    TOOL-aNimbleMend-1 words its edge to this unit as the run point asking the key; under A that
    ask is the adapter's and this unit's instruction names the key, and under B it is the main
    loop's. B satisfies the byte-for-byte sentence more
    literally and costs a silent off state, which is the failure this build exists to remove. Under
    B, S5 changes to an optional forwarded arg and S6's sentences gain the policy read; the child,
    S1 to S4, is the same under both.
  RESOLVED (agent, 2026-11-12, delegated): A, always. The adapter is the one asker of the key, so a caller that forgets an argument cannot turn a default-on mechanism off.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

The seam is the unit harness's optional-arg pattern and the build harness's hand-out:
`tools/workflows/unattended-unit.js` already reads `prebuild` as a dark, refused-when-malformed
arg, the build harness already spells `CHECKLIST` once and hands it out in `dispatch.args`, and its
hand-out already carries a `nextAction` string the routers tell the main loop to act on. This unit
extends all three and adds no file. `python tools/codebase-map/reuse_lookup.py "main loop runs fast
gate legs after each unit pass commit"` returned name-stem neighbours only (`run`, `legs`, `main`,
`units`), none of which is a run point; for a post-pass instruction to the main loop, no existing
seam fits beyond the three named above, which reading the two harness files found.

Recall returned TOOL-aMendedFleet-74, the unit that added `prebuild` and says a declared switch in
the parent belongs to whichever unit flips its default, and TOOL-aOrientedCast-4, the precedent for
forwarding one key through `dispatch.args`. It also returned TOOL-dFurnishedOrders-4 and
TOOL-dFurnishedOrders-30, which plan to retire the `checklist` and `prebuild` args. That is where
recall and source disagree: at 91ca33f2 the child still reads both, so this unit builds on the
source, and a build that later retires them moves `passLegs` by the same step.

Recall terms used: `python tools/memory-recall/query.py "where does the main loop learn what to run
after a unit harness returns" --terms "passes-harnessed unit harness dispatch args prebuild
checklist nextAction hand-out main loop pass commit gate-free"`
