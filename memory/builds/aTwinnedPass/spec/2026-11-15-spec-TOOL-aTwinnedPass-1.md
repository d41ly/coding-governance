# TOOL-aTwinnedPass-1 — the unit harness builds one pass in a worktree of its own, on a write set the main loop declared

**Status:** INPROGRESS · rev-1 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 1 · closes TOOL-dDerivedDocket-55

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-2-builder.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-2-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-4-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-4-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md) | research | TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-pass-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-pass-brief.md) | research | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-revision.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-revision.md) | research | TOOL-aTwinnedPass-2 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/unattended-unit.js` builds every pass in the caller's own tree and, in unattended
mode, orders its builder to run `--dispatch` and `--brief`, which both write the run-state file. So
two passes of one build cannot run at once: they would share one git index and both touch the file
M6 condition 3 keeps from a concurrent pass. This unit adds an optional `tree` key, and with it a
`writes` key, so one call builds and commits in the worktree the main loop cut for it, on the write
set the main loop already declared, and leaves every call without `tree` exactly as it is.

## 2. Scope (IN)

- **S1** — `tree` is optional. Present, it is refused before any spawn unless it is a non-empty
  single-line string with no backtick and an absolute path by the shape the build harness grades
  `scratch` by. Observed by AC6.
- **S2** — `writes` is optional, graded as `prebuild` is, and required exactly when `tree` is given
  in unattended mode: given without that pairing, or absent with it, it is refused before any spawn.
  Observed by AC7.
- **S3** — With `tree`, in either mode, the prompt carries one paragraph ordering every shell
  command, read, write and the commit into that worktree, and every relative path in the message,
  the brief's and the spec's included, to resolve under it. The `base` sentence then reads that
  worktree's `HEAD`, because its shell call runs there. Observed by AC3, AC4.
- **S4** — With `tree` in unattended mode, the driver steps say the main loop already declared the
  write set and recorded the brief at the commit the worktree was cut from, order neither verb,
  name the declared write set from `writes`, and tell the builder to return a path it needs beyond
  that set instead of writing it. In attended mode the driver steps are unchanged. Observed by AC3,
  AC4.
- **S5** — With `tree`, the return carries `tree` and one log line names the tree and, where given,
  the declared write set. Observed by AC3.
- **S6** — With `tree` and `passLegs`, the `nextAction` names the worktree as the command's working
  directory and the merge back as its deadline, and its no-base fallback names the commit the
  worktree was cut from. Observed by AC5.
- **S7** — Without `tree`, the prompt, the spawn options, the log and the return are byte for byte
  those of the file at base. Observed by AC2.
- **S8** — `meta.version` and its marker move to 1.2, and the header comment states `tree` and
  `writes` beside `prebuild`, `roles`, `efforts` and `passLegs`. Observed by AC8.
- **S9** — `help/pass-legs.md` says that a pass built in its own worktree has its `nextAction` name
  that worktree. Observed by AC9.
- **S10** — The arms of §4 "The arms" in `tools/workflows/unattended-build.test.sh`, with
  `FLOOR_ASSERTIONS` raised by the count they execute. Observed by AC10.
- **S11** — The changed harness parses in the dialect its runtime evaluates. Observed by AC1.
- **S12** — The codebase map is re-rendered and its symbol index is unchanged, because no
  definition is added. Observed by AC11.
- **S13** — The pass commit carries this unit's acceptance ledger. Observed by AC12.

## 3. Non-goals (OUT)

- Cutting, merging or cleaning up a worktree, and the order the main loop runs those steps in:
  `TOOL-aTwinnedPass-2`'s tool.
- `--dispatch` and its sibling comparison: `TOOL-aTwinnedPass-3`.
- The build harness `tools/workflows/unattended-build.template.js` and its render, which hand out
  `dispatch.args` and never a `tree`. A main loop composes a `tree` call itself.
- An `agent()` option that sets a working directory. The runtime's own worktree isolation was what
  the ask's prototype used, and it cut the worktree from the default branch and needed a hard reset.
  The worktree here is the main loop's, ordered in prose.
- Any check that `tree` exists, is a worktree of `repo`, holds its own branch or is clean. The child
  has no filesystem; the cut verb owns those refusals.
- Comparing `writes` with the run-state file's dispatch row, or parsing it into paths.
- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`, and anything
  under `memory/builds/dDeclaredLoop/`.
- Any self-test suite or bar inside the pass. The arms are written and checked with `bash -n`; the
  main loop observes each red and then green at the close.
- The serial-against-parallel measurement the build's acceptance names. It needs `TOOL-aTwinnedPass-2`
  and is the main loop's, at the build's close.
- The workflows kit version, which `tools/workflows/kit.toml` reads from
  `tools/workflows/tier2-review.template.js` and the lander mints (`tools/push-main.sh`, its "KIT
  VERSIONS ARE MINTED HERE" comment). The harness's own `meta.version` moves (S8).
- The verbs guide and the method's "passes-harnessed" paragraph, which describe the parallel route
  as a whole: `TOOL-aTwinnedPass-2` writes that route.

### Edges

- **hands-off** `TOOL-aTwinnedPass-2` — `--cut`, `--merge` and `--remove` of a pass's worktree, and
  the order that tool's header states. The worktree must be cut after the records commit that
  carries the dispatch rows, the brief rows and the brief files themselves: the builder reads its
  brief under the tree, and the write gate's dispatch fallback reads the run-state file at the
  target's own toplevel, which in a pass is the tree (§4, "Evidence"). A `committed: false` return
  carries `tree`, so the main loop knows which worktree `--remove` takes away.

## 4. Design

### Evidence

Read at base `aebbb4a72`. Line numbers are `tools/workflows/unattended-unit.js@71852dc0` unless named.

| Line | What sits there |
|---|---|
| `tools/workflows/unattended-unit.js@71852dc0:66` | the `passLegs` header paragraph, the last of the optional-key paragraphs |
| `tools/workflows/unattended-unit.js@71852dc0:72` | `version: '1.1', // gov:kit unattended-unit@1.1` |
| `tools/workflows/unattended-unit.js@71852dc0:131` | the closed `mode` refusal |
| `tools/workflows/unattended-unit.js@71852dc0:142` | the `prebuild` test: undefined, or a non-empty string with no CR, LF or backtick |
| `tools/workflows/unattended-unit.js@71852dc0:155` | the `passLegs` test, the same three parts |
| `tools/workflows/unattended-unit.js@71852dc0:258` | `DRIVER_STEPS`, a ternary on `mode`; the unattended branch orders `--dispatch` and `--brief` |
| `tools/workflows/unattended-unit.js@71852dc0:276` | `PROMPT`; `'\n\nBuild exactly ONE unit: '` at `:281` |
| `tools/workflows/unattended-unit.js@71852dc0:295` | the `base` sentence, `git rev-parse HEAD` |
| `tools/workflows/unattended-unit.js@71852dc0:351` | the `passLegs` log line |
| `tools/workflows/unattended-unit.js@71852dc0:373` | the return; `nextAction` at `:386` to `:401` |
| `tools/workflows/unattended-build.template.js@cc868b60:298` | `scratch` refused unless it matches `/^(\/\|[A-Za-z]:[\\/])/` |
| `tools/unattended/unattended.sh@eb567029:13382` | `--brief` parks its row in the run-state file and stages it |
| `tools/unattended/unattended.sh@eb567029:14944` | `--dispatch` parks its row in the run-state file and stages it |
| `tools/unattended/unattended.sh@eb567029:14269` | `check_commit_message` finds its run by a run-state file naming this branch's ref |
| `tools/hooks/scratch-guard.js@7c31933f:784` | `checkOriented` returns null on an `agent_id`: a subagent's commit is not orientation-gated |
| `tools/hooks/scratch-guard.js@7c31933f:918` | `readDispatchedUnits` reads the run-state file under the write target's toplevel; the write gate binds a subagent |
| `tools/workflows/unattended-build.test.sh@6fd35a28:1245` | `CHILD_ARGS`, `childU` and `childA`, the default child fixtures |
| `tools/workflows/unattended-build.test.sh@6fd35a28:1333` | the `passLegs` group; `FLOOR_ASSERTIONS=950` at `:3888` |

The harness carries one top-level definition, `check`, and no loop, array method or arrow
(`:20` to `:26`); the codebase-map JS floor needs the one definition. Every addition below is an
`if` block, a ternary or a string, so that stays true.

### The two keys

After the `passLegs` block and before the `roles` block, so `mode` is already graded:

```js
// `tree` IS OPTIONAL (TOOL-aTwinnedPass-1), graded as `prebuild` is because it is spelled into the
// prompt inside backticks, and absolute by the shape the build harness grades `scratch` by.
if (
  cfg.tree !== undefined &&
  (typeof cfg.tree !== 'string' || cfg.tree === '' || /[\r\n`]/.test(cfg.tree) ||
    !/^(\/|[A-Za-z]:[\\/])/.test(cfg.tree))
) {
  throw new Error(
    'unattended-unit: args `tree` must be an absolute single-line path with no backtick, got ' +
      JSON.stringify(cfg.tree) + '. Omit the key and the pass builds in the caller\'s own tree.',
  )
}
if (
  cfg.writes !== undefined &&
  (typeof cfg.writes !== 'string' || cfg.writes === '' || /[\r\n`]/.test(cfg.writes))
) {
  throw new Error(
    'unattended-unit: args `writes` must be a non-empty single-line string with no backtick, got ' +
      JSON.stringify(cfg.writes) + '. It is the write set the main loop declared with --dispatch for this pass.',
  )
}
if ((cfg.tree !== undefined && cfg.mode === 'unattended') !== (cfg.writes !== undefined)) {
  throw new Error(
    'unattended-unit: args `writes` travels with `tree` in unattended mode and nowhere else: it is the ' +
      'write set the main loop declared for a pass building in its own worktree, which that builder ' +
      'then does not declare. Got `tree` ' + JSON.stringify(cfg.tree) + ', `mode` ' +
      JSON.stringify(cfg.mode) + ' and `writes` ' + JSON.stringify(cfg.writes) + '.',
  )
}
```

The third test refuses a `writes` the builder would never be told about, and a `tree` call in
unattended mode with nothing to name as its write set (F1).

### The prompt

**The worktree paragraph**, in both modes, inserted in `PROMPT` immediately before
`'\n\nBuild exactly ONE unit: '`:

```js
(cfg.tree === undefined
  ? ''
  : '\n\nTHIS PASS BUILDS IN ITS OWN WORKTREE, `' + cfg.tree + '`, on the branch that worktree has ' +
    'checked out. Run every shell command with its working directory there, resolve every relative ' +
    'path in this message under it, the brief and the spec included, and write and commit only ' +
    'there, never in any other tree.') +
```

The `base` sentence is not touched: its `git rev-parse HEAD` is a shell command, which this
paragraph places in the worktree, so the `base` returned is that worktree's `HEAD` before the first
write. In attended mode this paragraph is the whole change to the prompt.

**The driver steps.** `DRIVER_STEPS` keeps both of its branches and gains a third, taken only when
`tree` is given and the mode is unattended:

```js
'The main loop declared this pass\'s write set with --dispatch and recorded this brief with ' +
'--brief, on the run\'s branch at the commit this worktree was cut from, so you call neither: both ' +
'write the run-state file, which a pass running beside another must not touch. The declared write ' +
'set is `' + cfg.writes + '`. Write no path outside it. Where you need one, stop, restore every ' +
'path you changed, commit nothing, and return committed:false with a why naming each such path: ' +
'a declaration widens only before its pass commits, and only the main loop may widen this one.\n'
```

The text spells neither `cfg.driver` nor `cfg.slug`, so the prompt carries no runnable recording
verb. The `prebuild` paragraph that follows reads "Once your write set is declared", which stays
true. The return-instead-of-write rule follows from `check_commit_message`'s comment that a pass may
widen its declaration with `--dispatch` until it commits and never after (F2).

### The log and the return

After the `passLegs` log line:

```js
if (cfg.tree !== undefined) log('unit ' + cfg.unitId + ': tree `' + cfg.tree + '`' +
  (cfg.writes === undefined ? '' : ', declared writes `' + cfg.writes + '`'))
```

In the return, after `diverged` and before the `nextAction` spread:
`...(cfg.tree === undefined ? {} : { tree: cfg.tree }),`. It is present on every return of a
`tree` call, `committed:false` included, because the tree outlives the pass either way.

### The nextAction

Three spans of the `nextAction` expression branch on `cfg.tree`, and each `cfg.tree === undefined`
arm is today's bytes:

| Span | Without `tree` (today) | With `tree` |
|---|---|---|
| fallback base | `` `<rev>` is the commit HEAD named before the dispatch, `` | `` `<rev>` is the commit that worktree was cut from, `` |
| deadline | `at the main loop before the next dispatch and before any later commit,` | ``at the main loop with its working directory at `<tree>`, before that worktree is merged back,`` |
| pass commit | `The pass commit is <sha>, which is HEAD when the command runs.` | `The pass commit is <sha>, which is HEAD there when the command runs.` |

With an ill-shaped `sha` the last span reads `The pass commit is HEAD there when the command runs.`
With `tree`, a filled `nextAction` begins
``Run `<passLegs> --base <base>` at the main loop with its working directory at `<tree>`, before that worktree is merged back, where that file exists.``
The pass legs write their record and the gate ledger into the git dir of the tree they run in, which
is where the red-fix lane reads them for a write in that tree.

### The header comment

A paragraph after the `passLegs` one, opening `` // `tree` IS OPTIONAL (TOOL-aTwinnedPass-1) ``,
stating: the absolute path of the worktree the main loop cut for this pass; `writes`, the write set
the main loop declared for it, which travels with it in unattended mode and nowhere else; the prompt
orders the work into the tree, and in unattended mode orders neither recording verb, because both
write the run-state file; the return carries `tree` and `nextAction` names it; absent, the prompt,
options, log and return are unchanged. `meta.version` becomes `'1.2'` and its marker
`gov:kit unattended-unit@1.2`.

### The help page

`help/pass-legs.md`, after the paragraph at its line 9 that says the unit harness's return carries
a `nextAction`, gains one sentence: "When the pass was built in its own worktree, the harness's
`tree` argument, the `nextAction` names that worktree as the command's working directory and the
merge back as its deadline." No other page under `help/` names the unit harness's arguments.

### The arms

One group in `tools/workflows/unattended-build.test.sh`, after the `passLegs` group, through
`run_wf` with `$C`. The fixture is `CHILD_ARGS` with `"tree":"/tmp/w"` and, in unattended mode,
`"writes":"P1 P2"`. A return double of `PL_OK`'s shape stands in for a commit.

- **T1, the unattended tree prompt.** The `prompt:build:` line carries
  `THIS PASS BUILDS IN ITS OWN WORKTREE, \`/tmp/w\`` and
  `The declared write set is \`P1 P2\``, and carries neither `--dispatch tB` nor
  `--brief tB`. The result carries `"tree":"/tmp/w"`. The log carries
  ``unit A-tB-1: tree `/tmp/w`, declared writes `P1 P2` ``.
- **T2, the attended tree prompt.** With `"mode":"attended"` and `tree` alone, the `prompt:build:`
  line with the worktree paragraph cut out by a fixed-string `sed` equals `childA`'s `prompt:build:`
  line, and the paragraph itself is present. The `type:` and `effort:` lines equal `childA`'s.
- **T3, the default.** `childU` and `childA` carry neither `OWN WORKTREE` nor `"tree"`. T1 is the
  positive control on the same fixture.
- **T4, the nextAction.** With `"passLegs":"PL"` beside the T1 args, the `nextAction` read by
  `read_next_action` carries
  ``Run `PL --base def5678` at the main loop with its working directory at `/tmp/w`, before that worktree is merged back``
  and `which is HEAD there when the command runs`. With no `base` in the double it carries
  `is the commit that worktree was cut from`.
- **T5, the refusals.** `tree` as `7`, `""`, `"a\nb"`, `` "a`b" `` and `"rel/w"` each print
  ``THROW unattended-unit: args `tree` `` and no `agent:build`. `"C:\\w"`, `"C:/w"` and `"/c/w"`
  each spawn, a positive control. `writes` as `7`, `""`, `"a\nb"` and `` "a`b" `` beside a valid
  unattended `tree` each print ``THROW unattended-unit: args `writes` ``; so do an unattended `tree`
  with no `writes`, a `writes` with no `tree` in unattended mode, and a `writes` beside `tree` in
  attended mode. None prints `agent:build`.

`FLOOR_ASSERTIONS` rises by the count the group executes, counted by reading, with a `RAISED`
comment line in the register above it naming this unit, as `TOOL-aNimbleMend-15`'s line does.

Ceiling, a declared bound rather than a measurement: the group adds about thirty `run_wf` node
processes, at most 60 s on node a (PINNED 2026-11-15). The close's suite run measures it.

### Inventory

| Minted | Where | Lexicon |
|---|---|---|
| arg `tree` | `unattended-unit.js` | no cell grades an args key: `.lexicon.conf` grades `js` function names, and `--suggest tree --as js.function` answers that `tree` is a scoping question, not a verb |
| arg `writes` | `unattended-unit.js` | as `tree`; the same answer |
| return key `tree` | `unattended-unit.js` | as above |

No function, file or conf key is minted, so no lexicon verb cell is involved and the symbol index
does not move. None of the two key names occurs as an args key in the harness at base.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`
- `help/pass-legs.md`
- `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-1-1-acceptance-ledger.md`

### Rollout

Dark by construction: nothing passes `tree` until a main loop composes a call with it, and every
call without it is today's call (S7). No switch is added, because the absent key is the switch.

### Alternatives rejected

- **A second definition or an arrow for the three-part string test**, which `prebuild`, `passLegs`,
  `tree` and `writes` now all spell. The header states the file keeps one definition and no arrow so
  its one spawn reads in one screen, and the floor it answers needs only one. The test is one line.
- **Changing the `base` sentence to `git -C <tree> rev-parse HEAD`.** The paragraph already places
  every shell command in the tree, and the sentence stays byte-identical in both cases.
- **Spelling the tree inside a quoted shell command.** A path holding a quote would rewrite the
  command; the prose order leaves the quoting to the agent.
- **Letting the builder widen its declaration from the tree.** That writes the run-state file this
  unit keeps the pass away from.

### What the design does not check

- That `tree` exists, is a worktree of `repo`, has its own branch checked out, is clean, or differs
  from `repo`. The child has no filesystem; a `tree` equal to `repo` builds in the run's tree.
- That the builder obeys the paragraph. A shell write outside the tree is unseen, and the scratch
  guard's write gate places an Edit by the target's own toplevel, so an Edit in the run's tree is
  graded as a write there and not refused for leaving the pass's tree.
- The pass commit's declaration. `check_commit_message` finds its run by a run-state file naming
  the branch `HEAD` holds, and no run-state file names a pass branch, so `--check-commit` is silent
  on a commit in a pass tree. The prompt's sentence that the commit-msg hook refuses a commit with
  no `Pass:` trailer is then not true there; the trailer order still stands and check 23 grades the
  commit at the close (F3).
- `writes` as paths: it is not split, normalized or compared with the dispatch row, and a value of
  spaces alone is admitted, as `prebuild` admits one.
- A `tree` holding spaces or shell metacharacters is spelled as given.
- AC2 holds byte-identity against base once, at the build. The arms hold it structurally after
  that: T2 for the attended prompt and T3's absences, and the existing `passLegs` arms for today's
  `nextAction` bytes. A later change to the default prompt that also lands in the tree paragraph's
  absence is seen by neither.

## 5. Production-readiness checklist

- security — two new caller inputs, each refused before any spawn unless one line with no backtick,
  since both are spelled into the prompt and `tree` into the `nextAction`; no new write path, and
  the builder's grants are unchanged.
- perf / scale — none per call; the build's serial-against-parallel figure is the main loop's.
- error / empty / loading states — every malformed or unpaired key is a named refusal; a
  `committed:false` return still carries `tree`.
- observability — one log line names the tree and the declared write set.
- risks — a builder that writes outside its tree, or misses a path, is caught at the merge or by
  check 23, not here (§4, "What the design does not check").
- testing — AC1 to AC12, and the arms on the `New arm:` lines in §7.
- migration — N/A: no data or record shape moves.
- user docs — `help/pass-legs.md` (S9). The parallel route as a whole is `TOOL-aTwinnedPass-2`'s.

## 6. Acceptance criteria

The probe below evaluates the harness the way its runtime does and prints its log, each prompt and
options object, and its result or refusal. AC2 to AC7 run it from the scratch directory `$S`, with
`$J` a committed return and `$K` one with no `base`:

```
// $S/unit-probe.js — node unit-probe.js <script> <args-json> <agent-return-json>
const fs = require('fs')
const src = fs.readFileSync(process.argv[2], 'utf8').replace(/^\s*export\s+const\s+meta\s*=/m, 'const meta =')
const AF = Object.getPrototypeOf(async function () {}).constructor
const ret = JSON.parse(process.argv[4])
const out = []
const agent = async (p, o) => { out.push('prompt:' + JSON.stringify(p)); out.push('opts:' + JSON.stringify(o)); return ret }
new AF('args', 'agent', 'phase', 'log', src)(process.argv[3], agent, () => {}, (m) => out.push('log:' + m))
  .then((r) => { out.push('RESULT ' + JSON.stringify(r)); console.log(out.join('\n')) },
        (e) => { out.push('THROW ' + e.message); console.log(out.join('\n')) })
```

```
J='{"committed":true,"sha":"abc1234","base":"def5678","why":"","summary":"s"}'
K='{"committed":true,"sha":"abc1234","why":"","summary":"s"}'
U='{"repo":"/r","slug":"tB","scratch":"/s","unitId":"A-tB-1","specPath":"s1","briefPath":"b1","driver":"bash drv.sh","ground":"G /s. ","checklist":"CK","mode":"unattended"'
A=${U/unattended/attended}
git show aebbb4a72:tools/workflows/unattended-unit.js > "$S/base.js"
```

- **AC1** — When `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-unit.js`
  runs, it exits 0.
  Red when: the change leaves a parse error, which `node --check` would not show.
- **AC2** — When the base blob is in `$S/base.js`, as the block above writes it, `diff` over the probe's output for `$S/base.js` and for `tools/workflows/unattended-unit.js`
  prints nothing for each of these four calls: `"$U}"` with `$J`; `"$U,\"passLegs\":\"PL\",\"prebuild\":\"PB\",\"roles\":{\"builder\":\"gov-builder\"},\"efforts\":{\"builder\":\"high\"}}"`
  with `$J`; the same with `$K`; and `"$A}"` with `$J`.
  Red when: any byte of a prompt, an options object, a log line or the result moves without `tree`.
  figure: the base output is DERIVED from the base blob at observation time.
- **AC3** — When the probe runs `"$U,\"tree\":\"/tmp/w\",\"writes\":\"P1 P2\"}"`
  with `$J`, the prompt carries `THIS PASS BUILDS IN ITS OWN WORKTREE, \`/tmp/w\``, ``The declared
  write set is `P1 P2` `` and `return what it prints as \`base\``, carries neither
  `--dispatch tB` nor `--brief tB`, the log carries ``unit A-tB-1: tree `/tmp/w`, declared writes``,
  and the result carries `"tree":"/tmp/w"`.
  Red when: the unattended driver steps still order a recording verb with `tree`, or the return or
  the log does not name the tree.
- **AC4** — When the probe runs `"$A,\"tree\":\"/tmp/w\"}"` with `$J`, its JSON-encoded prompt line
  with the substring from `\n\nTHIS PASS BUILDS` to `never in any other tree.` cut out equals the
  prompt line the `"$A}"` call of AC2 printed, that substring is present, and the `opts:` lines are
  equal.
  Red when: `tree` moves anything in an attended prompt beyond its one paragraph.
- **AC5** — When the probe runs the AC3 call with `"passLegs":"PL"` added, with `$J`, the
  `nextAction` carries ``Run `PL --base def5678` at the main loop with its working directory at
  `/tmp/w`, before that worktree is merged back`` and `which is HEAD there when the command runs`;
  with `$K` it carries `is the commit that worktree was cut from`.
  Red when: the `nextAction` of a tree pass still names the run's tree's `HEAD` or the next dispatch.
- **AC6** — When the probe runs `"$U,\"writes\":\"w\",\"tree\":<v>}"` for each `<v>` of `7`, `""`,
  `"a\nb"`, `` "a`b" `` and `"rel/w"`, each prints ``THROW unattended-unit: args `tree` `` and no
  `prompt:` line, and for each of `"C:\\w"`, `"C:/w"` and `"/c/w"` it prints a `prompt:` line. Each
  `<v>` is spelled as JSON, so the first of the three is the path `C:` then one backslash then `w`.
  Red when: a malformed `tree` reaches the prompt, or a Windows or MSYS absolute path is refused.
  figure: each criterion from AC2 to AC7 was run once against a scratch prototype of §4 on node a,
  2026-11-15, and held; PINNED there, DERIVED again at the build.
- **AC7** — When the probe runs `"$U,\"tree\":\"/tmp/w\",\"writes\":<v>}"` for each `<v>` of `7`,
  `""`, `"a\nb"` and `` "a`b" ``, and then `"$U,\"tree\":\"/tmp/w\"}"`, `"$U,\"writes\":\"w\"}"` and
  `"$A,\"tree\":\"/tmp/w\",\"writes\":\"w\"}"`, each prints ``THROW unattended-unit: args `writes` `` and no
  `prompt:` line.
  Red when: a malformed `writes` reaches the prompt, or an unpaired `tree` or `writes` spawns.
- **AC8** — When `grep -c "version: '1.2', // gov:kit unattended-unit@1.2"` and
  ``grep -c '^// `tree` IS OPTIONAL (TOOL-aTwinnedPass-1)'`` run over
  `tools/workflows/unattended-unit.js`, each prints 1, and `grep -c "unattended-unit@1.1"` prints 0.
  Red when: the version or the header paragraph does not move.
- **AC9** — When `grep -cF "names that worktree as the command's working directory"` runs over
  `help/pass-legs.md`, it prints 1.
  Red when: the page still describes only a pass built in the caller's tree.
- **AC10** — When `bash -n tools/workflows/unattended-build.test.sh` runs, it exits 0, and
  `grep -c 'RAISED 950 -> .* by TOOL-aTwinnedPass-1'` over that file prints 1.
  Red when: the group does not parse, or the floor does not count it.
  permission: the arms' red-then-green run is the main loop's, at the close.
- **AC11** — When `python tools/codebase-map/gen_map.py --write` has run,
  `python tools/codebase-map/gen_map.py --check` exits 0 and `git diff --exit-code -- memory/map/generated/symbols.json`
  prints nothing.
  Red when: a definition is added to the harness, or the map is left stale.
- **AC12** — When `git show --stat HEAD` runs on the pass commit, it lists the acceptance ledger
  §4 "Files touched" names under this build's build folder, which carries one `**Evidences:** TOOL-aTwinnedPass-1` block answering AC1 to AC12 and names the
  arms' red-then-green as owed to the main loop.
  Red when: the pass commit lands without its ledger.

## 7. Gates

`workflow script syntax` · `unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `routed commits name a specced unit` · `pass-order history` · `brief-recorded`

New arm: tools/workflows/unattended-build.test.sh · covers AC3 AC4 · the harness at base aebbb4a72, which reads no tree key, so its prompt has no worktree paragraph, still orders `--dispatch tB`, and its result has no tree field · FLOOR_ASSERTIONS raised by the group's count
New arm: tools/workflows/unattended-build.test.sh · covers AC5 · base, whose nextAction names the next dispatch and the run tree's HEAD · none
New arm: tools/workflows/unattended-build.test.sh · covers AC6 AC7 · base, which grades neither key, so every malformed or unpaired value spawns the builder · none

`check-arms` owes nothing here: its population is the `*.sh` gates defining `fail`, and the harness
is neither. The arms run once, at the close, by the main loop.

## 8. Open questions

- **F1 — A `writes` outside an unattended `tree` call: refuse it, or ignore it?** (a) Refuse, as
  §4 spells: the key means "the main loop declared this", which is true only there, and the
  harness refuses a misspelt `roles` stage rather than ignoring it for the same reason. (b) Ignore
  it: a caller that always passes both keys keeps working in attended mode. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F2 — A builder in a tree that needs a path outside its declared set: return, or write and
  report?** (a) Return `committed:false` naming the path, as §4 spells: the declaration may widen
  only before the pass commits, and only the main loop may write the run-state file. (b) Write it
  and name it in `summary`: the pass keeps its work, and check 23 reds the close unless the main
  loop widens first, which it cannot after the commit. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F3 — The commit sentence says the commit-msg hook refuses a commit with no `Pass:` trailer, and
  inside a pass tree that hook is silent. Change the sentence for a tree call?** (a) Leave it: the
  order to write the trailer is right in both trees, the default stays byte-identical, and check
  23 grades the commit at the close. (b) Give the tree branch a sentence saying the hook does not
  grade this commit and the trailer is the builder's alone: true, at the cost of a fourth `tree`
  span in the prompt and one more arm. Recommendation: (a), and file the hook's silence in a pass
  tree as an ask beside `TOOL-aTwinnedPass-2`'s merge.
  RESOLVED (agent, 2026-11-15, delegated): (a), the ask filed at the close.

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

The seam this unit extends is the harness's own optional-key shape: the `prebuild` and `passLegs`
tests at `tools/workflows/unattended-unit.js@71852dc0:142` and `:155`, which `tree` and `writes`
copy, and the build harness's absolute-path test for `scratch` at
`tools/workflows/unattended-build.template.js@cc868b60:298`, whose regex `tree` uses. The return's
spread of an optional key follows `nextAction`'s. `add_scratch_worktree` in
`tools/run-gates/lib-attribute.sh` cuts a detached worktree and belongs to the cut verb, not here.
The probe `python tools/codebase-map/reuse_lookup.py "validate an optional single-line workflow
argument and spell an absolute worktree path into a builder prompt"` ranked `build`, `build_commit`,
`check_line`, `add_scratch_worktree` and `resolve_tool_path` by name stem; none grades a workflow
argument, so the source read is the evidence for the seam. `gotchas.py --for-paths` over the three
product files selected `agent-output-interpolated-into-an-instruction`, answered because `tree` is
the caller's and the agent's `sha` and `base` still pass `COMMIT_SHAPE`;
`forwarded-arg-opens-an-unhandled-return-shape`, answered because the parent reads no child return
field it does not already read; `test-oracle-read-from-a-historical-sha`, answered by keeping the
base comparison in AC2 and out of the arms; `node-check-is-not-a-syntax-gate`, answered by AC1; and
`fixture-passes-by-finding-nothing`, answered by T1 beside T3's absences.

Recall terms used: `python tools/memory-recall/query.py "unit harness worktree isolation for
parallel passes, dispatch and brief recorded by the caller" --terms "unattended-unit worktree tree
parallel-when-disjoint dispatch brief run-state passLegs prebuild nextAction isolation"`
