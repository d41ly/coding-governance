# TOOL-aTwinnedPass-1 — the unit harness builds one pass in a worktree of its own, on a write set the main loop declared

**Status:** CLOSED · rev-2 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 1 · closes TOOL-dDerivedDocket-55

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aTwinnedPass-1-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aTwinnedPass-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aTwinnedPass-2-measurement.md](../build/2026-11-15-build-TOOL-aTwinnedPass-2-measurement.md) | research | TOOL-aTwinnedPass-2 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-2-builder.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-2-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-4-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-4-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-5-builder.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-5-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md) | research | TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-pass-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-pass-brief.md) | research | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-1-revision.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-revision.md) | research | TOOL-aTwinnedPass-2 |
| [2026-11-15-review-TOOL-aTwinnedPass-1-2-3-closing-diff-round1.md](../reviews/2026-11-15-review-TOOL-aTwinnedPass-1-2-3-closing-diff-round1.md) | diff-review | TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 |
| [2026-11-15-review-TOOL-aTwinnedPass-11-closing-diff-round3.md](../reviews/2026-11-15-review-TOOL-aTwinnedPass-11-closing-diff-round3.md) | diff-review | TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 TOOL-aTwinnedPass-4 TOOL-aTwinnedPass-5 TOOL-aTwinnedPass-11 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/unattended-unit.js` builds every pass in the caller's own tree and, in unattended
mode, orders its builder to run `--dispatch` and `--brief`, which both write the run-state file. So
two passes of one build cannot run at once: they would share one git index and both touch the file
M6 condition 3 keeps from a concurrent pass. A path handed to a builder in prose is no remedy: the
harness refuses a subagent's write to a worktree its session is not bound to (the revision record,
R1). This unit adds an optional `passBase` key, the commit the pass starts from, and with it a
`writes` key. With them the one `agent()` call runs in a worktree the runtime cuts for that agent,
the builder first resets it to `passBase`, builds and commits there on the write set the main loop
already declared, and returns the worktree's branch and path. Every call without `passBase` stays
exactly as it is.

## 2. Scope (IN)

- **S1** — `passBase` is optional. Present, it is refused before any spawn unless it is a string
  matching the harness's own commit shape, `COMMIT_SHAPE`, seven to sixty-four lower-case hex
  digits. Observed by AC6.
- **S2** — `writes` is optional, graded as `prebuild` is, and required exactly when `passBase` is
  given in unattended mode: given without that pairing, or absent with it, it is refused before any
  spawn. Observed by AC7.
- **S3** — With `passBase`, in either mode, the one `agent()` call's options carry
  `isolation: 'worktree'`, and its schema declares and requires `branch` and `worktree` beside the
  four keys it requires today. Observed by AC3, AC4.
- **S4** — With `passBase`, in either mode, the prompt carries one paragraph, ahead of every other
  order: before any other command, run `git reset --hard <passBase>` in the agent's own worktree
  and confirm `git rev-parse HEAD` prints a sha beginning with it, else return `committed:false`;
  then run, resolve, write and commit only in that worktree, on its branch; and return the branch as
  `branch` and the top-level path as `worktree`. The `base` sentence is unchanged, and after the
  reset it reads `passBase`. Observed by AC3, AC4.
- **S5** — With `passBase` in unattended mode, the driver steps say the main loop already declared
  the write set and recorded the brief on the run's branch at `passBase`, order neither verb, name
  the declared write set from `writes`, and tell the builder to return a path it needs beyond that
  set instead of writing it. In attended mode the driver steps are unchanged. Observed by AC3, AC4.
- **S6** — With `passBase`, the return carries `branch` and `worktree`, each the builder's value
  when it passes its shape check and the empty string otherwise; one log line before the spawn
  names `passBase` and, where given, the declared write set, and one after it names the raw branch
  and worktree the builder returned. Observed by AC3, AC8.
- **S7** — With `passBase` and `passLegs`, the `nextAction` takes its `--base` from `passBase`,
  names the returned worktree as the command's working directory and the merge back as its
  deadline, and says the pass commit is `HEAD` there; with a worktree that fails its shape it names
  that failure in place of a path. Observed by AC5, AC8.
- **S8** — Without `passBase`, the prompt, the spawn options, the log and the return are byte for
  byte those of the file at base. Observed by AC2.
- **S9** — `meta.version` and its marker move to 1.2, and the header comment states `passBase` and
  `writes` beside `prebuild`, `roles`, `efforts` and `passLegs`. Observed by AC9.
- **S10** — `help/pass-legs.md` says that a pass built in its own worktree has its `nextAction` name
  that worktree. Observed by AC10.
- **S11** — The arms of §4 "The arms" in `tools/workflows/unattended-build.test.sh`, its runner
  tracing an `isolation` option the way it traces `effort`, and `FLOOR_ASSERTIONS` raised by the
  count the arms execute. Observed by AC11.
- **S12** — The changed harness parses in the dialect its runtime evaluates. Observed by AC1.
- **S13** — The codebase map is re-rendered and its symbol index is unchanged, because no
  definition is added. Observed by AC12.
- **S14** — The pass commit carries this unit's acceptance ledger. Observed by AC13.

## 3. Non-goals (OUT)

- Merging a pass's branch back, cleaning up its worktree, and the order the main loop runs the
  steps in: `TOOL-aTwinnedPass-2`'s tool.
- `--dispatch` and its sibling comparison: `TOOL-aTwinnedPass-3`.
- The build harness `tools/workflows/unattended-build.template.js` and its render, which hand out
  `dispatch.args` and never a `passBase`. A main loop composes a `passBase` call itself.
- Any check that the reset happened, that `passBase` exists, or that the returned `base` equals it.
  The child has no filesystem and reads no git; `TOOL-aTwinnedPass-2`'s `--merge` refuses a branch
  whose merge base with the run's `HEAD` is not the commit the pass was dispatched from.
- Comparing `writes` with the run-state file's dispatch row, or parsing it into paths.
- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`, and anything
  under `memory/builds/dDeclaredLoop/`.
- Any self-test suite or bar inside the pass. The arms are written and checked with `bash -n`; the
  main loop observes each red and then green at the close.
- The serial-against-parallel measurement the build's acceptance names. It needs `TOOL-aTwinnedPass-2`
  and is the main loop's, at the build's close.
- The workflows kit version, which `tools/workflows/kit.toml` reads from
  `tools/workflows/tier2-review.template.js` and the lander mints (`tools/push-main.sh`, its "KIT
  VERSIONS ARE MINTED HERE" comment). The harness's own `meta.version` moves (S9).
- The verbs guide and the method's "passes-harnessed" paragraph, which describe the parallel route
  as a whole: `TOOL-aTwinnedPass-2` writes that route.

### Edges

- **hands-off** `TOOL-aTwinnedPass-2` — `--merge` of the `branch` this unit returns, `--remove` of
  the `branch` a `committed: false` return carries, and the order that tool's header states.
  The commit a pass resets to must be the records commit carrying the dispatch rows, the brief rows and the brief
  files themselves: the builder reads its brief under its worktree after the reset, and the write
  gate's dispatch fallback reads the run-state file at the write target's own toplevel, which in a
  pass is that worktree (§4, "Evidence"). A `committed: false` return still carries `branch` and
  `worktree`, so the main loop knows which pass `--remove` takes away; the runtime may already have
  removed a worktree it judged unchanged (§4, "What the design does not check").

## 4. Design

### Evidence

Read at base `aebbb4a72`. The harness blob `tools/workflows/unattended-unit.js@71852dc0` is the same
at this branch's tip, as are the other blobs named below.

| Line | What sits there |
|---|---|
| `tools/workflows/unattended-unit.js@71852dc0:66` | the `passLegs` header paragraph, the last of the optional-key paragraphs |
| `tools/workflows/unattended-unit.js@71852dc0:72` | `version: '1.1', // gov:kit unattended-unit@1.1` |
| `tools/workflows/unattended-unit.js@71852dc0:142` | the `prebuild` test: undefined, or a non-empty string with no CR, LF or backtick |
| `tools/workflows/unattended-unit.js@71852dc0:155` | the `passLegs` test, the same three parts |
| `tools/workflows/unattended-unit.js@71852dc0:224` | `UNIT_SCHEMA`, requiring `committed`, `sha`, `why` and `summary` |
| `tools/workflows/unattended-unit.js@71852dc0:258` | `DRIVER_STEPS`, a ternary on `mode`; the unattended branch orders `--dispatch` and `--brief` |
| `tools/workflows/unattended-unit.js@71852dc0:276` | `PROMPT`; `'\n\nBuild exactly ONE unit: '` at `:281` |
| `tools/workflows/unattended-unit.js@71852dc0:295` | the `base` sentence, `git rev-parse HEAD` |
| `tools/workflows/unattended-unit.js@71852dc0:351` | the `passLegs` log line |
| `tools/workflows/unattended-unit.js@71852dc0:362` | `COMMIT_SHAPE`, `/^[0-9a-f]{7,64}$/`, declared after `PROMPT` |
| `tools/workflows/unattended-unit.js@71852dc0:364` | the one `agent()` call; its options are an `Object.assign` of optional spreads |
| `tools/workflows/unattended-unit.js@71852dc0:373` | the return; `nextAction` at `:386` to `:401` |
| `tools/workflows/unattended-build.template.js@cc868b60:298` | `scratch` refused unless it matches `/^(\/\|[A-Za-z]:[\\/])/` |
| `tools/workflows/unattended-build.template.js@cc868b60:3031` | `dispatch.args`, which carries no `base` and no commit key |
| `tools/unattended/unattended.sh@eb567029:13382` | `--brief` parks its row in the run-state file and stages it |
| `tools/unattended/unattended.sh@eb567029:14944` | `--dispatch` parks its row in the run-state file and stages it |
| `tools/unattended/unattended.sh@eb567029:14269` | `check_commit_message` finds its run by a run-state file naming this branch's ref |
| `tools/hooks/scratch-guard.js@7c31933f:784` | `checkOriented` returns null on an `agent_id`: a subagent's commit is not orientation-gated |
| `tools/hooks/scratch-guard.js#readDispatchedUnits` | reads the run-state file under the write target's toplevel; the write gate binds a subagent |
| `tools/workflows/unattended-build.test.sh@6fd35a28:286` | `run_wf`; the `effort:` trace line at `:307`, written only when the options carry the key |
| `tools/workflows/unattended-build.test.sh@6fd35a28:1245` | `CHILD_ARGS`, `childU` and `childA`, the default child fixtures |
| `tools/workflows/unattended-build.test.sh@6fd35a28:1333` | the `passLegs` group; `FLOOR_ASSERTIONS=950` at `:3888` |

Observed, not read from code. The revision record's R1: a builder told in prose to write in a
hand-cut worktree had its first Edit refused, "belongs to a different worktree". Its R2: an Agent
call with worktree isolation runs in `<primary tree>/.claude/worktrees/agent-<agentId>` on branch
`worktree-agent-<agentId>`, cut at the default branch's tip, and its writes there are admitted.
`git worktree list` on node a, 2026-11-15, shows `agent-a17154d749d2a5d26` at `8397ac8ca`, the
dispatch commit `TOOL-aTwinnedPass-3`'s pass brief ordered it reset to, with that pass's product
edits staged: the reset runs and the write gate admits the writes after it. The workflow runtime's
`isolation: 'worktree'` option for `agent()` is the revision record's citation of the runtime's
reference; no file in this repository documents it, and AC3 observes only that the option is
passed.

The harness carries one top-level definition, `check`, and no loop, array method or arrow
(`:20` to `:26`); the codebase-map JS floor needs the one definition. Every addition below is an
`if` block, a ternary, a regex constant or a string, so that stays true.

### The two keys

`COMMIT_SHAPE` moves, with its comment, from `:362` to just after the `passLegs` block, because the
`passBase` test reads it and a `const` read before its line throws. Its comment gains one sentence:
it also grades `passBase`, which is spelled into a shell order in the prompt. Then, before the
`roles` block, so `mode` is already graded:

```js
// `passBase` IS OPTIONAL (TOOL-aTwinnedPass-1): the commit this pass starts from. It is spelled into
// a shell order in the prompt, so it is graded by the commit shape and nothing else passes.
if (cfg.passBase !== undefined && (typeof cfg.passBase !== 'string' || !COMMIT_SHAPE.test(cfg.passBase))) {
  throw new Error(
    'unattended-unit: args `passBase` must be a commit sha of 7 to 64 lower-case hex digits, got ' +
      JSON.stringify(cfg.passBase) + '. Omit the key and the pass builds in the caller\'s own tree.',
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
if ((cfg.passBase !== undefined && cfg.mode === 'unattended') !== (cfg.writes !== undefined)) {
  throw new Error(
    'unattended-unit: args `writes` travels with `passBase` in unattended mode and nowhere else: it is the ' +
      'write set the main loop declared for a pass building in its own worktree, which that builder ' +
      'then does not declare. Got `passBase` ' + JSON.stringify(cfg.passBase) + ', `mode` ' +
      JSON.stringify(cfg.mode) + ' and `writes` ' + JSON.stringify(cfg.writes) + '.',
  )
}
```

The third test refuses a `writes` the builder would never be told about, and a `passBase` call in
unattended mode with nothing to name as its write set (F1).

### The spawn

`UNIT_SCHEMA` keeps its bytes without the key, so its two lists branch on it:

```js
required: cfg.passBase === undefined
  ? ['committed', 'sha', 'why', 'summary']
  : ['committed', 'sha', 'why', 'summary', 'branch', 'worktree'],
```

and its `properties` becomes an `Object.assign` of today's five-key object and, with `passBase`,
`{ branch: { type: 'string' }, worktree: { type: 'string' } }`, else `{}`. Two literal lists and
not a `concat`, because the file carries no array method (F5).

The `agent()` options gain a fourth spread, after `effort`:
`cfg.passBase === undefined ? {} : { isolation: 'worktree' }`.

### The prompt

**The worktree paragraph**, in both modes, inserted in `PROMPT` immediately before
`'\n\nBuild exactly ONE unit: '`, so it follows only the parent's ground text and the role stamp and
comes ahead of every order:

```js
(cfg.passBase === undefined
  ? ''
  : '\n\nTHIS PASS BUILDS IN A WORKTREE OF ITS OWN, which the runtime cut for this agent and which may ' +
    'sit on another commit. BEFORE ANY OTHER COMMAND, run `git reset --hard ' + cfg.passBase + '` there, ' +
    'then confirm `git rev-parse HEAD` prints a sha beginning with `' + cfg.passBase + '`, the commit ' +
    'this pass was dispatched from; if it does not, commit nothing and return committed:false with a ' +
    'why naming what it printed. Run every shell command with its working directory there, resolve ' +
    'every relative path in this message under it, the brief and the spec included, and write and ' +
    'commit only there, on the branch it has checked out, never in any other tree. Return that branch ' +
    'as `branch`, as `git branch --show-current` prints it, and the worktree\'s path as `worktree`, as ' +
    '`git rev-parse --show-toplevel` prints it.') +
```

The `base` sentence is not touched: it is read before the first write, which the paragraph places
after the reset, so the `base` returned is `passBase` in full. In attended mode this paragraph is
the whole change to the prompt.

**The driver steps.** `DRIVER_STEPS` keeps both of its branches and gains a third, taken only when
`passBase` is given and the mode is unattended:

```js
'The main loop declared this pass\'s write set with --dispatch and recorded this brief with ' +
'--brief, on the run\'s branch at `' + cfg.passBase + '`, the commit you reset to, so you call ' +
'neither: both write the run-state file, which a pass running beside another must not touch. The ' +
'declared write set is `' + cfg.writes + '`. Write no path outside it. Where you need one, stop, ' +
'restore every path you changed, commit nothing, and return committed:false with a why naming each ' +
'such path: a declaration widens only before its pass commits, and only the main loop may widen ' +
'this one.\n'
```

The text spells neither `cfg.driver` nor `cfg.slug`, so the prompt carries no runnable recording
verb. The `prebuild` paragraph that follows reads "Once your write set is declared", which stays
true. The return-instead-of-write rule follows from `check_commit_message`'s comment that a pass may
widen its declaration with `--dispatch` until it commits and never after (F2).

### The log and the return

After the `passLegs` log line:

```js
if (cfg.passBase !== undefined) log('unit ' + cfg.unitId + ': own worktree from `' + cfg.passBase + '`' +
  (cfg.writes === undefined ? '' : ', declared writes `' + cfg.writes + '`'))
```

After the `committed=` log line, with the raw values, as that line logs the raw `sha`:
`if (cfg.passBase !== undefined) log('unit ' + cfg.unitId + ': branch=' + ((r && r.branch) || '-') + ' worktree=' + ((r && r.worktree) || '-'))`.

Then, before the return, the two shape checks, each a constant beside `COMMIT_SHAPE`'s use:

```js
// owner of the absolute prefix: unattended-build.template.js `scratch`
const TREE_SHAPE = /^(\/|[A-Za-z]:[\\/])[^\r\n`]*$/
const BRANCH_SHAPE = /^[A-Za-z0-9][A-Za-z0-9._\/-]{0,254}$/
const ownBranch = r && typeof r.branch === 'string' && BRANCH_SHAPE.test(r.branch) ? r.branch : ''
const ownTree = r && typeof r.worktree === 'string' && TREE_SHAPE.test(r.worktree) ? r.worktree : ''
```

In the return, after `diverged` and before the `nextAction` spread:
`...(cfg.passBase === undefined ? {} : { branch: ownBranch, worktree: ownTree }),`. Both are present
on every return of a `passBase` call, `committed:false` included, because the worktree outlives the
pass either way. An empty string is the shape check's refusal, as `sha` is empty for a missing sha.

### The nextAction

Four spans of the `nextAction` expression branch on `cfg.passBase`, and each
`cfg.passBase === undefined` arm is today's bytes:

| Span | Without `passBase` (today) | With `passBase` |
|---|---|---|
| base | `r.base` when usable, else the `<rev>` fallback sentence | `passBase`, always |
| deadline | `at the main loop before the next dispatch and before any later commit,` | ``at the main loop with its working directory at `<worktree>`, before that worktree is merged back,`` |
| no usable worktree | — | `at the main loop with its working directory at the worktree this pass built in, whose path the builder returned unusable, before that worktree is merged back,` |
| pass commit | `The pass commit is <sha>, which is HEAD when the command runs.` | `The pass commit is <sha>, which is HEAD there when the command runs.` |

With an ill-shaped `sha` the last span reads `The pass commit is HEAD there when the command runs.`
With `passBase`, a filled `nextAction` begins
``Run `<passLegs> --base <passBase>` at the main loop with its working directory at `<worktree>`, before that worktree is merged back, where that file exists.``
`passBase` and not the builder's `base`, because the main loop chose it and checked its shape, and a
builder that skipped the reset would hand back the default branch's tip (F4). The pass legs write
their record and the gate ledger into the git dir of the tree they run in, which is where the
red-fix lane reads them for a write in that tree.

### The header comment

A paragraph after the `passLegs` one, opening `` // `passBase` IS OPTIONAL (TOOL-aTwinnedPass-1) ``,
stating: the commit the pass starts from; with it the agent runs in a worktree the runtime cuts for
it, which may sit on the default branch's tip, so the prompt's first order is the reset; `writes`,
the write set the main loop declared, travels with it in unattended mode and nowhere else, and the
builder then orders neither recording verb, because both write the run-state file; the return
carries `branch` and `worktree` after a shape check, and `nextAction` takes its base from `passBase`
and names the worktree; absent, the prompt, options, log and return are unchanged. `meta.version`
becomes `'1.2'` and its marker `gov:kit unattended-unit@1.2`.

### The help page

`help/pass-legs.md`, after the paragraph at its line 9 that says the unit harness's return carries
a `nextAction`, gains one sentence: "When the pass was built in its own worktree, the harness's
`passBase` argument, the `nextAction` names that worktree as the command's working directory and the
merge back as its deadline." No other page under `help/` names the unit harness's arguments.

### The arms

`run_wf` gains one trace line after the `effort:` one, written only when the options carry the key,
so every trace written before it stays byte for byte what it was:
`if (opts && Object.prototype.hasOwnProperty.call(opts, "isolation")) trace.push("isolation:" + label + ":" + opts.isolation)`.

One group in `tools/workflows/unattended-build.test.sh`, after the `passLegs` group, through
`run_wf` with `$C`. The fixture is `CHILD_ARGS` with `"passBase":"fedcba9"` and, in unattended
mode, `"writes":"P1 P2"`. The return double is `PL_OK`'s with
`"branch":"worktree-agent-x1","worktree":"/w/agent-x1"` added.

- **T1, the unattended prompt.** The `prompt:build:` line carries
  `THIS PASS BUILDS IN A WORKTREE OF ITS OWN`, `` `git reset --hard fedcba9` `` and
  ``The declared write set is `P1 P2` ``, and carries neither `--dispatch tB` nor `--brief tB`.
  The trace carries `isolation:build:worktree`. The result carries `"branch":"worktree-agent-x1"`
  and `"worktree":"/w/agent-x1"`. The log carries
  ``unit A-tB-1: own worktree from `fedcba9`, declared writes `P1 P2` ``.
- **T2, the attended prompt.** With `"mode":"attended"` and `passBase` alone, the `prompt:build:`
  line with the worktree paragraph cut out by a fixed-string `sed` equals `childA`'s `prompt:build:`
  line, and the paragraph itself is present. The `type:` line equals `childA`'s, and the
  `isolation:` line is present.
- **T3, the default.** `childU` and `childA` carry neither `isolation:` nor `OWN WORKTREE` nor
  `"branch"`. T1 is the positive control on the same fixture.
- **T4, the nextAction.** With `"passLegs":"PL"` beside the T1 args, the `nextAction` read by
  `read_next_action` carries
  ``Run `PL --base fedcba9` at the main loop with its working directory at `/w/agent-x1`, before that worktree is merged back``
  and `which is HEAD there when the command runs`, and not `def5678`.
- **T5, the shape checks.** With the double's `branch` as `a b` and `worktree` as `rel/w`, the result
  carries `"branch":""` and `"worktree":""`, and the `nextAction` carries
  `whose path the builder returned unusable`.
- **T6, the refusals.** `passBase` as `7`, `""`, `"abc"`, `"ABC1234"` and `` "fedcba9`" `` each print
  ``THROW unattended-unit: args `passBase` `` and no `agent:build`. A forty-digit hex `passBase`
  spawns, a positive control. `writes` as `7`, `""`, `"a\nb"` and `` "a`b" `` beside a valid
  unattended `passBase` each print ``THROW unattended-unit: args `writes` ``; so do an unattended
  `passBase` with no `writes`, a `writes` with no `passBase` in unattended mode, and a `writes`
  beside `passBase` in attended mode. None prints `agent:build`.

`FLOOR_ASSERTIONS` rises by the count the group executes, counted by reading, with a `RAISED`
comment line in the register above it naming this unit, as `TOOL-aNimbleMend-15`'s line does.

Ceiling, a declared bound rather than a measurement: the group adds about thirty-five `run_wf` node
processes, at most 60 s on node a (PINNED 2026-11-15). The close's suite run measures it.

### Inventory

| Minted | Where | Lexicon |
|---|---|---|
| arg `passBase` | `unattended-unit.js` | no cell grades an args key: `.lexicon.conf` grades `js` function names. `--suggest startCommit --as js.function` steers `start` to `main`, so no `start` stem; `--suggest base --as js.function` answers a scoping question, not a verb. The `pass` stem follows `passLegs`, and `base` is the return's own word for the commit a pass started from |
| arg `writes` | `unattended-unit.js` | as `passBase`; unchanged from rev-1 |
| return keys `branch`, `worktree` | `unattended-unit.js` | `--suggest branch` and `--suggest worktree`, each `--as js.function`, answer a scoping question, not a verb |
| options key `isolation` | the `agent()` call | the runtime's own option name, not minted here |
| constants `TREE_SHAPE`, `BRANCH_SHAPE`; locals `ownBranch`, `ownTree` | `unattended-unit.js` | constants and locals, which the floor and the lexicon's function pattern do not count |

No function, file or conf key is minted, so no lexicon verb cell is involved and the symbol index
does not move. None of the key names occurs as an args key in the harness at base.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`
- `help/pass-legs.md`
- `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-1-1-acceptance-ledger.md`

### Rollout

Dark by construction: nothing passes `passBase` until a main loop composes a call with it, and every
call without it is today's call (S8). No switch is added, because the absent key is the switch.

### Alternatives rejected

- **A path key naming a worktree the main loop cut** (rev-1's `tree`). A subagent's write to a
  worktree its session is not bound to is refused, and routing the write through the shell breaks
  the charter's `[tools]` rule (the revision record, R1).
- **Naming the key `base`.** The build harness's `base` is the run's pinned review anchor
  (`tools/workflows/unattended-build.template.js@cc868b60:168`), and a main loop copying it into a
  child call would reset every pass to the run's start.
- **A second definition or an arrow for the shape tests.** The header states the file keeps one
  definition and no arrow, and the floor it answers needs only one.
- **Taking `nextAction`'s base from the builder's `base`** when usable, as without the key. See F4.
- **Letting the builder widen its declaration from its worktree.** That writes the run-state file
  this unit keeps the pass away from.

### What the design does not check

- That the reset ran, that `passBase` names a commit, or that the returned `base` equals it. The
  prompt orders the confirmation and a `committed:false` when it fails; `--merge` refuses a branch
  that does not start there (§3).
- That the runtime cuts the worktree, where, or from which commit; and whether it removes one after
  a `committed:false` pass: its reference says a worktree is auto-removed if unchanged, and whether
  a reset with no commit counts as unchanged is not known here.
- That the builder obeys the paragraph. A shell write outside its worktree is unseen by this file;
  the write gate refuses an Edit outside the session's own worktree (R1), which is the boundary
  this design leans on.
- That `branch` names the worktree's branch or that `worktree` names an existing directory: both
  are shape-checked only. A detached worktree's empty `git branch --show-current` returns an empty
  `branch`, which the main loop cannot merge by name.
- The pass commit's declaration. `check_commit_message` finds its run by a run-state file naming
  the branch `HEAD` holds, and no run-state file names a pass branch, so `--check-commit` is silent
  on a commit in a pass worktree. The prompt's sentence that the commit-msg hook refuses a commit
  with no `Pass:` trailer is then not true there; the trailer order still stands and check 23
  grades the commit at the close (F3).
- `writes` as paths: it is not split, normalized or compared with the dispatch row, and a value of
  spaces alone is admitted, as `prebuild` admits one.
- AC2 holds byte-identity against base once, at the build. The arms hold it structurally after
  that: T2 for the attended prompt, T3's absences, and the existing `passLegs` arms for today's
  `nextAction` bytes. A later change to the default prompt that also lands in the paragraph's
  absence is seen by neither.

## 5. Production-readiness checklist

- security — two new caller inputs refused before any spawn: `passBase` unless a hex commit, since it
  is spelled into a shell order; `writes` unless one line with no backtick. Two agent-returned values,
  `branch` and `worktree`, reach the return and `nextAction` only through a shape check. The agent's
  grants are unchanged; isolation narrows where it writes.
- perf / scale — none per call; the runtime's worktree cut is per pass. The build's
  serial-against-parallel figure is the main loop's.
- error / empty / loading states — every malformed or unpaired key is a named refusal; an unusable
  `branch` or `worktree` is an empty string and a `nextAction` sentence naming it unusable.
- observability — one log line names `passBase` and the declared write set, one the returned branch
  and worktree.
- risks — a builder that skips the reset, writes outside its worktree or misses a path is caught at
  the merge or by check 23, not here (§4, "What the design does not check").
- testing — AC1 to AC13, and the arms on the `New arm:` lines in §7.
- migration — N/A: no data or record shape moves.
- user docs — `help/pass-legs.md` (S10). The parallel route as a whole is `TOOL-aTwinnedPass-2`'s.

## 6. Acceptance criteria

The probe below evaluates the harness the way its runtime does and prints its log, each prompt and
options object, and its result or refusal. AC2 to AC8 run it from the scratch directory `$S`, with
`$J` a committed return, `$K` one with no `base`, `$W` one carrying a branch and worktree, and `$X`
one carrying ill-shaped ones:

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
W='{"committed":true,"sha":"abc1234","base":"def5678","why":"","summary":"s","branch":"worktree-agent-x1","worktree":"/w/agent-x1"}'
X='{"committed":true,"sha":"abc1234","base":"def5678","why":"","summary":"s","branch":"a b","worktree":"rel/w"}'
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
  Red when: any byte of a prompt, an options object, a log line or the result moves without `passBase`.
  figure: the base output is DERIVED from the base blob at observation time.
- **AC3** — When the probe runs `"$U,\"passBase\":\"fedcba9\",\"writes\":\"P1 P2\"}"` with `$W`,
  the prompt carries `THIS PASS BUILDS IN A WORKTREE OF ITS OWN`, `` `git reset --hard fedcba9` ``,
  ``The declared write set is `P1 P2` `` and `return what it prints as \`base\``, and carries
  neither `--dispatch tB` nor `--brief tB`; the `opts:` line carries `"isolation":"worktree"` and a
  `required` list ending `"branch","worktree"`; the log carries
  ``unit A-tB-1: own worktree from `fedcba9`, declared writes`` and
  `branch=worktree-agent-x1 worktree=/w/agent-x1`; and the result carries
  `"branch":"worktree-agent-x1"` and `"worktree":"/w/agent-x1"`.
  Red when: the spawn is not isolated, the unattended driver steps still order a recording verb, or
  the return or the log does not name the branch and worktree.
- **AC4** — When the probe runs `"$A,\"passBase\":\"fedcba9\"}"` with `$W`, its JSON-encoded prompt
  line with the substring from `\n\nTHIS PASS BUILDS` to `` `git rev-parse --show-toplevel` prints it. ``
  cut out equals the prompt line the `"$A}"` call of AC2 printed, that substring is present, and the
  `opts:` line carries `"isolation":"worktree"`.
  Red when: `passBase` moves anything in an attended prompt beyond its one paragraph, or the attended
  spawn is not isolated.
- **AC5** — When the probe runs the AC3 call with `"passLegs":"PL"` added, with `$W`, the
  `nextAction` carries ``Run `PL --base fedcba9` at the main loop with its working directory at
  `/w/agent-x1`, before that worktree is merged back`` and `which is HEAD there when the command
  runs`, and does not carry `def5678`; with `$K` it still carries `--base fedcba9`.
  Red when: the `nextAction` of a worktree pass takes the builder's base, or still names the run
  tree's `HEAD` or the next dispatch.
- **AC6** — When the probe runs `"$U,\"writes\":\"w\",\"passBase\":<v>}"` for each `<v>` of `7`,
  `""`, `"abc"`, `"ABC1234"` and `` "fedcba9`" ``, each prints ``THROW unattended-unit: args `passBase` ``
  and no `prompt:` line, and for a forty-digit lower-case hex `<v>` it prints a `prompt:` line.
  Red when: a malformed `passBase` reaches the prompt, or a full sha is refused.
  figure: each criterion from AC2 to AC8 is DERIVED at the build from the probe; rev-1's figures
  were taken against the `tree` design and do not carry over.
- **AC7** — When the probe runs `"$U,\"passBase\":\"fedcba9\",\"writes\":<v>}"` for each `<v>` of
  `7`, `""`, `"a\nb"` and `` "a`b" ``, and then `"$U,\"passBase\":\"fedcba9\"}"`,
  `"$U,\"writes\":\"w\"}"` and `"$A,\"passBase\":\"fedcba9\",\"writes\":\"w\"}"`, each prints
  ``THROW unattended-unit: args `writes` `` and no `prompt:` line.
  Red when: a malformed `writes` reaches the prompt, or an unpaired `passBase` or `writes` spawns.
- **AC8** — When the probe runs the AC5 call with `$X`, the result carries `"branch":""` and
  `"worktree":""`, the `nextAction` carries `whose path the builder returned unusable` and neither
  `rel/w` nor `a b`, and the log carries `branch=a b worktree=rel/w`.
  Red when: an ill-shaped agent value reaches the return or the `nextAction`.
- **AC9** — When `grep -c "version: '1.2', // gov:kit unattended-unit@1.2"` and
  ``grep -c '^// `passBase` IS OPTIONAL (TOOL-aTwinnedPass-1)'`` run over
  `tools/workflows/unattended-unit.js`, each prints 1, and `grep -c "unattended-unit@1.1"` prints 0.
  Red when: the version or the header paragraph does not move.
- **AC10** — When `grep -cF "names that worktree as the command's working directory"` runs over
  `help/pass-legs.md`, it prints 1.
  Red when: the page still describes only a pass built in the caller's tree.
- **AC11** — When `bash -n tools/workflows/unattended-build.test.sh` runs, it exits 0;
  `grep -c 'RAISED 950 -> .* by TOOL-aTwinnedPass-1'` over that file prints 1; and
  `grep -c 'trace.push("isolation:"'` over it prints 1.
  Red when: the group does not parse, the floor does not count it, or the runner cannot see the
  option.
  permission: the arms' red-then-green run is the main loop's, at the close.
- **AC12** — When `python tools/codebase-map/gen_map.py --write` has run,
  `python tools/codebase-map/gen_map.py --check` exits 0 and `git diff --exit-code -- memory/map/generated/symbols.json`
  prints nothing.
  Red when: a definition is added to the harness, or the map is left stale.
- **AC13** — When `git show --stat HEAD` runs on the pass commit, it lists the acceptance ledger
  §4 "Files touched" names under this build's build folder, which carries one `**Evidences:** TOOL-aTwinnedPass-1` block answering AC1 to AC13 and names the
  arms' red-then-green as owed to the main loop.
  Red when: the pass commit lands without its ledger.

## 7. Gates

`workflow script syntax` · `unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `routed commits name a specced unit` · `pass-order history` · `brief-recorded`

New arm: tools/workflows/unattended-build.test.sh · covers AC3 AC4 · the harness at base aebbb4a72, which reads no passBase key, so its spawn has no isolation option, its prompt has no worktree paragraph and still orders `--dispatch tB`, and its result has no branch field · FLOOR_ASSERTIONS raised by the group's count
New arm: tools/workflows/unattended-build.test.sh · covers AC5 AC8 · base, whose nextAction takes the builder's base and names the next dispatch and the run tree's HEAD · none
New arm: tools/workflows/unattended-build.test.sh · covers AC6 AC7 · base, which grades neither key, so every malformed or unpaired value spawns the builder · none

`check-arms` owes nothing here: its population is the `*.sh` gates defining `fail`, and the harness
is neither. The arms run once, at the close, by the main loop.

## 8. Open questions

- **F1 — A `writes` outside an unattended `passBase` call: refuse it, or ignore it?** (a) Refuse, as
  §4 spells: the key means "the main loop declared this", which is true only there, and the
  harness refuses a misspelt `roles` stage rather than ignoring it for the same reason. (b) Ignore
  it: a caller that always passes both keys keeps working in attended mode. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a). Rev-2 renames the pairing's other key and keeps the answer.
- **F2 — A builder in its own worktree that needs a path outside its declared set: return, or write
  and report?** (a) Return `committed:false` naming the path, as §4 spells: the declaration may widen
  only before the pass commits, and only the main loop may write the run-state file. (b) Write it
  and name it in `summary`: the pass keeps its work, and check 23 reds the close unless the main
  loop widens first, which it cannot after the commit. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F3 — The commit sentence says the commit-msg hook refuses a commit with no `Pass:` trailer, and
  inside a pass worktree that hook is silent. Change the sentence for a `passBase` call?** (a) Leave
  it: the order to write the trailer is right in both trees, the default stays byte-identical, and
  check 23 grades the commit at the close. (b) Give the worktree branch a sentence saying the hook
  does not grade this commit and the trailer is the builder's alone: true, at the cost of another
  span in the prompt and one more arm. Recommendation: (a), and file the hook's silence in a pass
  worktree as an ask beside `TOOL-aTwinnedPass-2`'s merge.
  RESOLVED (agent, 2026-11-15, delegated): (a), the ask filed at the close.
- **F4 — With `passBase`, does `nextAction`'s `--base` come from `passBase` or from the builder's
  `base`?** (a) `passBase`, always, as §4 spells: the main loop chose and shape-checked it, a correct
  pass returns it as `base` anyway, and a builder that skipped the reset returns the default
  branch's tip, which would widen the pass legs over commits the pass never made. (b) The builder's
  `base` when usable, `passBase` as the fallback: today's precedence kept, at the cost of trusting
  an agent value the main loop already holds. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).
- **F5 — Does the schema require `branch` and `worktree` with `passBase`, or only declare them?**
  (a) Require, as §4 spells: the main loop cannot merge or remove a pass whose branch it was not
  told, so a missing key is a schema failure the runtime surfaces, and a `committed:false` return
  still has a worktree to name. (b) Declare only: a builder that cannot name them still returns,
  and the return carries empty strings. Recommendation: (a).
  RESOLVED (agent, 2026-11-15, delegated): (a).

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.
- rev-2 · 2026-11-15 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · repair of TOOL-aTwinnedPass-1 under the
  revision record 2026-11-15-prompt-TOOL-aTwinnedPass-1-revision. R1 and R3: the `tree` path key
  gives way to `passBase`, the agent call carries `isolation: 'worktree'`, the prompt's first order
  is the reset to `passBase` and its confirmation, the schema and return carry `branch` and
  `worktree` after a shape check, and `nextAction` takes its base from `passBase` and names the
  returned worktree; the test runner traces the option. R2 is in §4 "Evidence". R6: F1 to F3 stand
  as RESOLVED, F4 and F5 are new, and `writes` and the unattended driver steps keep rev-1's design
  with the dispatch commit named by `passBase`. R4 and R5 bind `TOOL-aTwinnedPass-2`.

## 10. Reuse audit

The seam this unit extends is the harness's own optional-key shape: the `prebuild` and `passLegs`
tests at `tools/workflows/unattended-unit.js@71852dc0:142` and `:155`, which `writes` copies; its
`COMMIT_SHAPE` at `:362`, which grades `passBase` and moves up so the test can read it; the optional
spreads of the `agent()` options at `:364`, which `isolation` joins; and the build harness's
absolute-path test for `scratch` at `tools/workflows/unattended-build.template.js@cc868b60:298`,
whose prefix `TREE_SHAPE` uses. The return's spread of an optional key follows `nextAction`'s. The
runner's `isolation:` trace copies its `effort:` line at
`tools/workflows/unattended-build.test.sh@6fd35a28:307`. `add_scratch_worktree` in
`tools/run-gates/lib-attribute.sh` cuts a detached worktree from a main loop's shell and has no
place here: the runtime cuts this one. The probe `python tools/codebase-map/reuse_lookup.py "run a
builder agent in a runtime-isolated worktree reset to a given commit and return its branch and
path"` ranked `run`, `build`, `run_git`, `write_commit`, `build_records`, `build_commit` and
`branches` by name stem; none spawns an agent or grades a workflow argument, so the source read is
the evidence for the seam. `gotchas.py --for-paths` over the three product files selected
`agent-output-interpolated-into-an-instruction`, answered by `BRANCH_SHAPE` and `TREE_SHAPE` before
either agent value reaches the return or `nextAction`, and by `passBase` in place of the builder's
`base`; `fixed-base-assumes-one-commit-per-pass`, answered because `passBase` precedes every commit
the pass makes; `forwarded-arg-opens-an-unhandled-return-shape`, answered because the parent reads
no child return field it does not already read; `test-oracle-read-from-a-historical-sha`, answered
by keeping the base comparison in AC2 and out of the arms; `node-check-is-not-a-syntax-gate`,
answered by AC1; `degradation-known-but-unreported`, answered by the empty-string fields and the
`nextAction`'s unusable-path sentence; and `fixture-passes-by-finding-nothing`, answered by T1
beside T3's absences.

Recall terms used: `python tools/memory-recall/query.py "unit harness worktree isolation for
parallel passes, dispatch and brief recorded by the caller" --terms "unattended-unit worktree tree
parallel-when-disjoint dispatch brief run-state passLegs prebuild nextAction isolation"`, and at
rev-2 `python tools/memory-recall/query.py "builder agent worktree isolation reset hard to dispatch
commit, runtime cuts worktree from default branch" --terms "isolation worktree reset passBase
agent-worktree unattended-unit"`, whose first hit is `TOOL-dDerivedDocket-55` and its prototype's
hard reset to the group commit.
