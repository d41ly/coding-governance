# TOOL-aTwinnedPass-11 — the Workflow runtime's worktree spelling, admitted beside the Agent tool's at both ends of the handoff

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-2 · base 900f656d0 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aTwinnedPass-11-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aTwinnedPass-11-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-11-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-11-2-builder.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-2-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-11-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-brief.md) | research | — |
| [2026-11-15-prompt-TOOL-aTwinnedPass-11-pass-brief.md](../prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-pass-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

A parallel pass the unit harness spawns inside a Workflow cannot merge back. `TOOL-aTwinnedPass-4`
held the pass identity to the one spelling the Agent tool cuts, `worktree-agent-<id>` at
`<primary tree>/.claude/worktrees/agent-<id>`, and inside a Workflow the runtime cuts
`worktree-wf_<run id>-<n>` at `<primary tree>/.claude/worktrees/wf_<run id>-<n>`. The harness then
blanks the pass's `branch` and `worktree`, and `pass-tree.sh` refuses the branch. This unit admits
both spellings wherever unit 4 admits one, states the admitted name once per file, and keeps every
refusal unit 4's arms observe.

## 2. Scope (IN)

- **S1** — `tools/workflows/unattended-unit.js`: a new const `PASS_NAME` holds the admitted last
  segment as a regex source, `agent-[A-Za-z0-9]+|wf_[0-9a-f]+-[0-9a-f]+-[0-9]+`. `TREE_SHAPE` and
  `BRANCH_SHAPE` are built from it (§4, "The harness shapes"); their two call sites and every other
  line of the harness stay as they are. Observed by AC1, AC2, AC3.
- **S2** — `tools/workflows/unattended-unit.js`: the comment above the shapes says the runtime cuts
  two spellings, and that `pass-tree.sh` spells the same alternation with no gate holding the two
  copies together (§4, "How the two copies are held"). Observed by AC6.
- **S3** — `tools/unattended/pass-tree.sh` `check_pass_branch`: its shape test admits
  `^worktree-(agent-[A-Za-z0-9]+|wf_[0-9a-f]+-[0-9a-f]+-[0-9]+)$`, and its refusal names both
  spellings. `check_pass_holder`'s code is unchanged: its wanted path is already
  `<primary>/.claude/worktrees/${PT_BRANCH#worktree-}`, which holds a `wf_` pass to its own place.
  Observed by AC3, AC4, AC5.
- **S4** — `tools/unattended/pass-tree.sh`: the header's section 4 sentence and the comment above
  `check_pass_holder` name both spellings and the holder rule as the branch less its `worktree-`
  prefix. Observed by AC6.
- **S5** — `tools/workflows/unattended-build.test.sh`: a `TP11` group after `TP4` feeds the harness
  a `wf_` return it must carry, one hostile `wf_` return, and two names outside both spellings;
  `FLOOR_ASSERTIONS` is raised 1028 to 1039 with its RAISED line. Observed by AC2.
- **S6** — `tools/unattended/pass-tree.test.sh`: `write_fixture_pass` takes an optional third
  argument, the worktree's last segment, defaulting to `agent-p<n>`. A `TP11` block after `T7` merges
  a pass cut as `worktree-wf_0d688c69-edb-1`, refuses one held at another `wf_` name, and refuses a
  `wf_` name off the runtime's structure. Observed by AC4, AC5.

## 3. Non-goals (OUT)

- Editing `TOOL-aTwinnedPass-4`'s spec. It is CLOSED and stays frozen; its correction is this unit
  (`memory/guides/BUILD-METHOD.md@28d18878:146`). This spec supersedes these of its lines, each only
  where it names `agent-<id>` as the one spelling: §1's "the one spelling the runtime cuts"; S1's
  `^worktree-agent-[A-Za-z0-9]+$`; S2's last segment `agent-<id>`; S4's pattern; S5's holder
  "exactly `<primary tree>/.claude/worktrees/agent-<id>`", whose rule this unit keeps and spells as
  the branch less `worktree-`; §4's code block under "The two harness shapes"; §4's
  `check_pass_branch` refusal line; §4's "The header" sentence; AC5's "Red when" clause naming
  `worktree-agent-<id>`; and AC8's header needle `.claude/worktrees/agent-<id>`. Its §3 bullet
  refusing a conf key still holds: one runtime cuts both spellings.
- A gate holding the harness's `PASS_NAME` and the tool's alternation to one another (§4, "How the
  two copies are held"; Edges).
- `check_pass_holder`'s code, `remove_pass_tree`, `--from` and the `TP4` arms of either suite: none
  moves. The round-2 items of ask `TOOL-aTwinnedPass-6`, among them the unreadable worktree list that
  `[ -d "$where" ] || return 0` admits, stay with that ask.
- A cross-check in the harness that the returned worktree's name equals the returned branch's less
  `worktree-`: unit 4's §3 left it to `check_pass_holder`, and this unit does not move it.
- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`;
  `memory/builds/dDeclaredLoop/`; the build harness `unattended-build.js`; the unattended Skill's
  loop; how a main loop picks which units go together; a cap on concurrent passes.
- The raw `branch` and `worktree` on the harness's log line, kept raw on purpose
  (`tools/workflows/unattended-unit.js@08be490b:436`).
- The kit version, which the lander's `mint` moves; a page under `help/`, since none describes
  unattended passes (unit 4's §3).
- A suite run inside the pass. The pass runs `bash -n`, the workflow syntax check, the probes of
  §6 and `gen_map.py --write`; the main loop observes each new arm red and then green at the close.

### Edges

- **consumes-from** external — this build's fourth unit, CLOSED and frozen, so it declares no edge back: the shapes, `check_pass_branch`, `check_pass_holder`,
  the `TP4` arms and the fixture's `.claude/worktrees/` placement this unit widens; without them
  there is no shape to admit a second spelling into.
- **consumes-from** external — the measurement record
  `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-2-measurement.md`, whose
  bench observed the `wf_` spelling and found the defect this unit fixes.
- **hands-off** external — the parity arm that reads the admitted pass name from both ends of the
  harness-to-tool handoff, owed under ask `TOOL-aTwinnedPass-7`. That ask's row names the sha-shape
  parity arm, and unit 4's Edges handed off the branch shape beside it; the main loop amends the
  row to name the pass-name alternation too, since this unit writes no record outside its spec.

## 4. Design

### Evidence

Read at base `900f656d0`.

| Citation | What sits there |
|---|---|
| `tools/workflows/unattended-unit.js@08be490b:441` | the unit 4 comment naming `worktree-agent-<id>` at `.claude/worktrees/agent-<id>` as the runtime's own spelling |
| `tools/workflows/unattended-unit.js@08be490b:446` | `TREE_SHAPE`, a regex literal ending `\.claude[\\/]worktrees[\\/]agent-[A-Za-z0-9]+$`; `BRANCH_SHAPE` at `:447`, `^worktree-agent-[A-Za-z0-9]+$` |
| `tools/workflows/unattended-unit.js@08be490b:448` | the two call sites, `ownBranch` and `ownTree`, each `''` on a failed test |
| `tools/workflows/check-verifier-fanout.js` `LOOP_HEADER` | a sibling workflow file building `new RegExp` from a shared source string, the house form S1 follows |
| `tools/unattended/pass-tree.sh@8e75d203:31` | the header's section 4 sentence naming `worktree-agent-<id>` and `.claude/worktrees/agent-<id>` |
| `tools/unattended/pass-tree.sh@8e75d203:121` | `check_pass_branch`'s shape test, the tool's one copy of the pattern, and its refusal at `:122` |
| `tools/unattended/pass-tree.sh@8e75d203:138` | `check_pass_holder`'s wanted path, `$primary/.claude/worktrees/${PT_BRANCH#worktree-}` |
| `tools/workflows/unattended-build.test.sh@f7472357:1460` | `TP4_ARGS`, `render_pass_returns` at `:1461` and the six hostile cases at `:1464` |
| `tools/workflows/unattended-build.test.sh@f7472357:4004` | `FLOOR_ASSERTIONS=1028` |
| `tools/unattended/pass-tree.test.sh@96d03d18:63` | `write_fixture_pass`, which `cd`s into `$R/.claude/worktrees/agent-p$1` |
| `tools/unattended/pass-tree.test.sh@96d03d18:319` | the `TP4` block cutting its holders by hand with `git worktree add` at `$C` |
| `tools/unattended/pass-tree.test.sh@96d03d18:386` | `T7`, the last block before the PASS line at `:397` |
| `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-2-measurement.md@9f807a3b:50` | the bench's two `wf_` passes, `wf_0d688c69-edb-1` and `wf_b6dff716-2a3-1`, on `worktree-wf_<run id>-<n>` |
| `memory/builds/dDerivedDocket/spec/2026-09-22-spec-TOOL-dDerivedDocket-62.md@caf8970d:374` | a third observation, 2026-09-22: worktree `wf_f6394001-255-1` with `refs/heads/worktree-wf_f6394001-255-1` checked out |

The records hold five `wf_` pass names, all `wf_<8 hex>-<3 hex>-1`, and 555 of 598 distinct
`wf_` tokens are run ids of the form `wf_<8 hex>-<3 hex>` (PINNED 2026-11-15, `git grep -ohE` over
`memory` and `tools` at base). On node a, 2026-11-15, `git worktree list --porcelain` lists 50 trees
under `.claude/worktrees/`: 14 on `worktree-agent-<id>`, none on any other `worktree-` branch, the
rest session trees on `branch/<name>` or `build/<slug>` and one detached, among them
`agent-effort-levels-role-task-507d91` on `branch/aGuardedEffort` (PINNED 2026-11-15).

### The harness shapes

```js
const PASS_NAME = 'agent-[A-Za-z0-9]+|wf_[0-9a-f]+-[0-9a-f]+-[0-9]+'
const TREE_SHAPE = new RegExp(/^(?!.*(^|[\\/])\.\.([\\/]|$))(\/|[A-Za-z]:[\\/])([A-Za-z0-9._ -]+[\\/])*\.claude[\\/]worktrees[\\/]/.source + '(?:' + PASS_NAME + ')$')
const BRANCH_SHAPE = new RegExp('^worktree-(?:' + PASS_NAME + ')$')
```

The prefix stays a regex literal, so it carries no doubled escapes, and `.source` hands it to the
constructor as written; the source of the old `TREE_SHAPE` equals the new one with
`(?:<PASS_NAME>)$` put back to `agent-[A-Za-z0-9]+$`. The `wf_` alternative pins the runtime's
structure, three groups, two hex and one decimal, and not the group lengths (F2). Both names are
built from `PASS_NAME`, so the harness states the admitted name once. No function is minted.

A `node` probe of these three lines on node a, 2026-11-15, printed the expected answer for every
value AC1 lists, and with the old literal for comparison printed `true` for the source equality.

### `check_pass_branch`

Line 121's test becomes:

```bash
if ! [[ $1 =~ ^worktree-(agent-[A-Za-z0-9]+|wf_[0-9a-f]+-[0-9a-f]+-[0-9]+)$ ]]; then
```

and its refusal:

`pass-tree: REFUSING - '<name>' is not a branch the runtime cuts for a pass (worktree-agent-<id> or worktree-wf_<run id>-<n>), so it is not a pass's branch; nothing was written`

The test keeps its place after the leading-dash, `check-ref-format` and own-branch refusals. The
needle `is not a branch the runtime cuts for a pass` that unit 4's `TP4` arms read is unchanged. A
bash probe on node a, 2026-11-15, admitted `worktree-agent-x1` and `worktree-wf_0d688c69-edb-1` and
refused `worktree-wf_x`, `worktree-foo`, `worktree-wf_0d688c69-edb`, a `;id` tail and a newline tail.

`check_pass_holder` needs no edit: for `worktree-wf_0d688c69-edb-1` it wants
`<primary>/.claude/worktrees/wf_0d688c69-edb-1`, exactly where the runtime cut it.

### How the two copies are held

The alternation lives twice, once per file: `PASS_NAME` in the harness and line 121 in the tool. A
workflow script is evaluated alone and the tool is bash, so neither can import the other, which is
why unit 4 copied the template's `..` test the same way. No gate holds the two together today. That
parity arm is a gate, a separate unit by M2 (`memory/guides/BUILD-METHOD.md@28d18878:34`), and it is
owed under ask `TOOL-aTwinnedPass-7` (Edges). Until it lands, a spelling admitted at one end and not
the other fails safe: the harness blanks a name the tool would take, or the tool refuses a branch
the harness carried, each loud and with the tree intact.

### The comments and the header

- The harness comment above the shapes: unit 4's two lines become one sentence for each runtime
  spelling, the Agent tool's `agent-<id>` and a Workflow's `wf_<run id>-<n>`, each cut at
  `<primary tree>/.claude/worktrees/<name>` on `worktree-<name>`; then `PASS_NAME` states the name
  once for both shapes, and `pass-tree.sh`'s `check_pass_branch` spells the same alternation, held to
  this one by no gate, owed under ask `TOOL-aTwinnedPass-7`.
- `pass-tree.sh` section 4: both verbs refuse a branch outside the runtime's two spellings,
  `worktree-agent-<id>` and `worktree-wf_<run id>-<n>`, and a worktree holding it anywhere but
  `<primary tree>/.claude/worktrees/<name>` for that branch's own `<name>`, the branch less
  `worktree-`. The comment above `check_pass_holder` says the same. Section 5's bullet on a runtime
  that cuts passes under another name or place stays as written.

### The arms

`tools/workflows/unattended-build.test.sh`, a `TP11` group right after `TP4`, each call through
`run_wf "$TP4_ARGS" "$(render_pass_returns <branch> <worktree>)" "$C"`:

| Case | `branch` returned | `worktree` returned | Asserts | n |
|---|---|---|---|---|
| the runtime's `wf_` spelling | `worktree-wf_0d688c69-edb-1` | `/w/.claude/worktrees/wf_0d688c69-edb-1` | the `RESULT` line carries both values unchanged; `nextAction` carries ``with its working directory at `/w/.claude/worktrees/wf_0d688c69-edb-1`, before that worktree is merged back`` | 3 |
| a hostile `wf_` tail | `worktree-wf_0d688c69-edb-1$(id)` | `/w/.claude/worktrees/wf_0d688c69-edb-1;id` | `"branch":""`; `"worktree":""`; the `RESULT` line lacks `wf_0d688c69-edb-1`; `nextAction` carries `whose path the builder returned unusable` | 4 |
| a `wf_` name off the structure | `worktree-wf_x` | `/w/.claude/worktrees/wf_x` | `"branch":""`; `"worktree":""` | 2 |
| a name under neither prefix | `worktree-foo` | `/w/.claude/worktrees/foo` | `"branch":""`; `"worktree":""` | 2 |

The values carry no backslash and no double quote, so `render_pass_returns`'s `printf %s` passes
them as written. The hostile payload sits after the name, where only the `wf_` alternative's own
class and anchor refuse it; unit 4's `TP4` cases keep their payloads in earlier segments and stay
as they are, so every hostile value they feed is still refused, observed by their own arms.

`FLOOR_ASSERTIONS` 1028 to 1039, with the line
`# RAISED 1028 -> 1039 by TOOL-aTwinnedPass-11: the 11 its TP11 group executes — the wf_ return's three, the hostile wf_ tail's four, and two each for the wf_ name off the structure and the name under neither prefix. Counted by reading, not measured by a run: the pass that wrote it runs no suite.`

`tools/unattended/pass-tree.test.sh`: `write_fixture_pass` reads its worktree as
`$R/.claude/worktrees/${3:-agent-p$1}`, and its comment names the optional third argument. Every
existing call passes two arguments and is unchanged. A `TP11` block after `T7`, before the PASS
line, cutting each tree by hand at `$C` as `TP4` does:

| Arm | Set-up | Call | Asserts | n |
|---|---|---|---|---|
| a `wf_` pass merges back | `worktree-wf_0d688c69-edb-1` at `$R/.claude/worktrees/wf_0d688c69-edb-1`, then `write_fixture_pass 12 p12.txt wf_0d688c69-edb-1` | `--merge tRun --pass TOOL-tRun-12 --branch worktree-wf_0d688c69-edb-1 --from $C` | exit 0; stdout is `HEAD`; the merge's second parent is the pass commit; `git worktree list --porcelain` lacks `/.claude/worktrees/wf_0d688c69-edb-1`; `git rev-parse --verify -q refs/heads/worktree-wf_0d688c69-edb-1` fails | 5 |
| a `wf_` holder at another `wf_` name | `worktree-wf_0d688c69-edb-2` at `$R/.claude/worktrees/wf_0d688c69-edb-3` | `--remove tRun --branch worktree-wf_0d688c69-edb-2` | exit 1; stderr carries `where the runtime cuts that pass's worktree`; the directory remains; the branch remains | 4 |
| a `wf_` name off the structure | `worktree-wf_x` at `$R/.claude/worktrees/wf_x` | `--remove tRun --branch worktree-wf_x` | exit 1; stderr carries `is not a branch the runtime cuts for a pass`; the directory remains | 3 |

The merge conflicts on `fx-out.txt` and the README region as `T1`'s second merge does, and the tool
resolves both and re-renders. Unit 12 has no dispatch row, as unit 11 in `T7` has none; `--merge`
reads no row. The two refused trees are cut at `$C`, which `run` holds, so neither branch holds a
commit no other ref holds, and only the new refusals stand between `--remove` and a forced removal.
The suite carries no floor.

Ceilings: the harness group adds four `node` launches to a suite whose budget row declares 500 s,
and the pass-tree block three tool calls and one fixture commit to a row declaring 300 s. Neither
row moves, an ESTIMATE PINNED 2026-11-15 that the close's run confirms.

### Inventory

| Identifier | Kind | Lexicon |
|---|---|---|
| `PASS_NAME` | JS const in `unattended-unit.js`, a regex source | no `js` constant cell is declared: `--suggest PASS_NAME --as js.constant` answered UNDECLARED |
| `TP11` | the arm groups' label prefix in both suites | not a code name |

No function is minted, so `memory/map/generated/symbols.json`, which records functions, does not
move. `git grep -nw PASS_NAME` finds nothing in the tree at base.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/unattended/pass-tree.sh`
- `tools/unattended/pass-tree.test.sh`
- `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-11-1-acceptance-ledger.md`

### Rollout

Live, with no switch. A pass the Agent tool cuts meets the same answer as before; a pass the
Workflow runtime cuts is now carried and merged where before it was blanked and refused. Every other
branch and holder is refused as today.

### Alternatives rejected

- **Any `worktree-<name>` whose holder is `.claude/worktrees/<name>`** (F1 (b)).
- **Pinned group lengths, `wf_[0-9a-f]{8}-[0-9a-f]{3}-[0-9]+`** (F2 (b)).
- **A third shape const for the `wf_` spelling, tested beside the first.** Two consts per field and
  two call-site tests where one alternation answers; the comment would then name three shapes.
- **Building the parity arm here.** A gate is its own unit (M2), and ask `TOOL-aTwinnedPass-7` holds
  it.

### What the design does not check

- That `PASS_NAME` and line 121's alternation agree: two copies, no gate, owed under ask
  `TOOL-aTwinnedPass-7`.
- A runtime spelling beyond the two observed, or a `wf_` name whose groups change class: refused at
  both ends until the alternation learns it, which is the safe direction.
- That a returned `wf_` worktree's name matches the returned branch's: graded alone in the harness,
  held together by `check_pass_holder` at the destructive end, as for `agent-`.
- That the run id inside a `wf_` name is the run that spawned the pass: the name is matched by shape.

## 5. Production-readiness checklist

- security — the admitted set grows by one structure of hex and decimal groups, which carries no
  shell, path or quote character; the holder rule, deny by default and textual, is unchanged; no
  new input, write path or `eval`.
- perf / scale — none: one alternation per test; the suites' ceilings are in §4, "The arms".
- error / empty / loading states — a name outside both spellings keeps today's `''` in the harness
  and today's one-line refusal in the tool, whose text now names both spellings.
- observability — the refusal names both spellings, so an operator sees which names the tool takes.
- risks — the two copies of the alternation can drift until the parity arm lands; drift fails safe
  (§4, "How the two copies are held").
- testing — AC1 to AC6 and the `New arm:` lines of §7.
- migration — N/A: no record shape or conf key moves.
- user docs — the tool's header and the harness comment; no `help/` page describes unattended
  passes (§3).

## 6. Acceptance criteria

- **AC1** — When a `node -e` probe reads the `PASS_NAME`, `TREE_SHAPE` and `BRANCH_SHAPE` lines out
  of `tools/workflows/unattended-unit.js`, evaluates them, and tests them, these pass:
  `/w/.claude/worktrees/wf_0d688c69-edb-1`, `C:\w\.claude\worktrees\wf_0d688c69-edb-1`,
  `C:/projects/coding-governance/.claude/worktrees/wf_b6dff716-2a3-1`,
  `/w/.claude/worktrees/agent-x1`, `C:\w\.claude\worktrees\agent-x1`,
  `worktree-wf_0d688c69-edb-1`, `worktree-wf_f6394001-255-1` and
  `worktree-agent-a062c1d85fb878113`; and these fail: the six hostile worktrees and six hostile
  branches of unit 4's `TP4` table, `/w/agent-x1`, `agent-x1`, `/w/.claude/worktrees/agent-x1/sub`,
  `/w/.claude/worktrees/wf_0d688c69-edb-1;id`, `worktree-wf_0d688c69-edb-1$(id)`,
  `/w/.claude/worktrees/wf_x`, `worktree-wf_x`, `/w/.claude/worktrees/foo`, `worktree-foo`,
  `worktree-wf_0d688c69-edb` and `/w/.claude/worktrees/agent-effort-levels-role-task-507d91`.
  Red when: `PASS_NAME` lacks the `wf_` alternative, admits any name, or a shape drops the prefix's
  `..` lookahead, its backslash alternative or its trailing anchor.
- **AC2** — When `run_wf` evaluates the harness with `passBase` and `passLegs` set and the `wf_`
  return of §4's `TP11` table, the `RESULT` line carries `"branch":"worktree-wf_0d688c69-edb-1"` and
  `"worktree":"/w/.claude/worktrees/wf_0d688c69-edb-1"`, and `nextAction` names that worktree; with
  the table's three refused returns, both fields are `""`; and the `TP4` group's hostile returns
  are still refused.
  Red when: `BRANCH_SHAPE` or `TREE_SHAPE` refuses the `wf_` spelling, or admits a hostile tail, a
  `wf_` name off the structure or a name under neither prefix.
  fixture: the `TP4_ARGS` and `render_pass_returns` of the build harness's suite; the pass observes
  the same with a `node -e` stub of `agent`.
  permission: the suite's run is the main loop's, at the close.
- **AC3** — When `grep -c` counts `wf_\[0-9a-f\]` and `agent-\[A-Za-z0-9\]` in
  `tools/workflows/unattended-unit.js` and in `tools/unattended/pass-tree.sh`, each of the four
  counts prints 1.
  Red when: either file spells the admitted name in a second place, or keeps the old single
  spelling beside the new alternation.
- **AC4** — When `bash tools/unattended/pass-tree.sh --merge tRun --pass TOOL-tRun-12 --branch
  worktree-wf_0d688c69-edb-1 --from <C>` runs in a fixture where that branch is checked out at
  `<primary>/.claude/worktrees/wf_0d688c69-edb-1` with one pass commit, it exits 0, prints the merge
  sha, the merge's second parent is the pass commit, and the worktree and branch are gone.
  Red when: `check_pass_branch` refuses the `wf_` spelling, or `check_pass_holder` wants another
  place for it.
  fixture: a hand-built repository in the pass-tree suite's shape, a primary tree on `run` with
  `.unattended.conf` and the run-state file of build `tRun`; the tree holds none.
- **AC5** — When `--remove tRun --branch worktree-wf_0d688c69-edb-2` runs with that branch held at
  `<primary>/.claude/worktrees/wf_0d688c69-edb-3`, it exits 1, its stderr carries `where the runtime
  cuts that pass's worktree`, and the directory and branch remain; and when `--remove` names
  `worktree-wf_x`, held at `<primary>/.claude/worktrees/wf_x`, it exits 1 with `is not a branch the
  runtime cuts for a pass` and the directory remains.
  Red when: the holder test becomes a prefix test, or `check_pass_branch` admits any `wf_` name.
  fixture: as AC4.
- **AC6** — When `grep` runs over `tools/unattended/pass-tree.sh` and
  `tools/workflows/unattended-unit.js`, each names `wf_<run id>-<n>` in a comment above its shape
  test, and `grep -c 'tools/unattended'` over `pass-tree.sh` prints 0; and when
  `python tools/codebase-map/gen_map.py --write` runs, `git diff --quiet --
  memory/map/generated/symbols.json` exits 0.
  Red when: a comment still names `agent-<id>` as the one spelling, the header spells the kit's
  prefix, or a function was minted without the index moving.

## 7. Gates

`workflow script syntax` · `unattended-build self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `install-prefix self-test` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/workflows/unattended-build.test.sh · covers AC2 · the wf_ return's three red with `PASS_NAME` put back to `agent-[A-Za-z0-9]+`; the hostile wf_ tail's four red with the wf_ alternative written `wf_.+`; the off-structure pair red with it written `wf_[A-Za-z0-9_-]+`; the neither-prefix pair red with `PASS_NAME` written `[A-Za-z0-9_-]+` · FLOOR_ASSERTIONS 1028 -> 1039
New arm: tools/unattended/pass-tree.test.sh · covers AC4 AC5 · the merge arm red with line 121's test put back to `^worktree-agent-[A-Za-z0-9]+$`; the other-wf_-name arm red with `check_pass_holder`'s comparison widened to a `$primary/.claude/worktrees/` prefix; the off-structure arm red with the tool's wf_ alternative written `wf_[A-Za-z0-9_-]+` · none

`check-arms` grades nothing here: `pass-tree.sh` defines no `fail` helper and the harness is
JavaScript, so neither is in its discovered population; `python tools/memory-tree/check-arms.py
--check` runs at the close to show the population did not move. No function is minted, so the
lexicon has no new name to grade.

## 8. Open questions

- **F1 — Are the two observed prefixes admitted, or any `worktree-<name>` held at `.claude/worktrees/<name>`?**
  (a) The two observed, `agent-[A-Za-z0-9]+` and `wf_[0-9a-f]+-[0-9a-f]+-[0-9]+`: deny by default,
  and a third runtime spelling is refused at both ends with the tree intact until the alternation
  learns it, one edit in each file. (b) Any `worktree-<name>`, `<name>` from `[A-Za-z0-9_-]+`, its
  holder bound by `check_pass_holder` to `.claude/worktrees/<name>`: no edit when the runtime adds a
  spelling, and today no live tree on node a would be newly admitted (§4, "Evidence"); but this
  repository cuts worktrees by hand under `.claude/worktrees/`, so a hand-cut tree on a branch named
  `worktree-<its name>` becomes one `--remove` force-removes with its scratch, and the harness would
  carry any such name into `nextAction`. Recommendation: (a), on which §4 and the arms are written;
  (b) drops the `TP11` neither-prefix pair and AC1's `foo` values.
  RESOLVED (agent, 2026-11-15, delegated): (a), the recommendation.
- **F2 — Does the `wf_` alternative pin its group lengths?** (a) Structure only,
  `wf_[0-9a-f]+-[0-9a-f]+-[0-9]+`: every observed name fits, the classes carry no hostile character,
  and a runtime that lengthens its run id stays admitted. (b) Pinned,
  `wf_[0-9a-f]{8}-[0-9a-f]{3}-[0-9]+`: matches all five observed names and 555 of 598 run ids in the
  records (§4, "Evidence"), and refuses a length change, which is loud and safe but buys no safety
  the class does not already give. Recommendation: (a), on which §4 is written.
  RESOLVED (agent, 2026-11-15, delegated): (a), the recommendation.

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft, from the brief
  `2026-11-15-prompt-TOOL-aTwinnedPass-11-brief` and the measurement record
  `2026-11-15-build-TOOL-aTwinnedPass-2-measurement`.

## 10. Reuse audit

The seams this unit extends: the harness's `TREE_SHAPE` and `BRANCH_SHAPE`, whose call sites do not
move, now built from one `PASS_NAME` source in the `new RegExp` form `check-verifier-fanout.js`'s
`LOOP_HEADER` already uses; `check_pass_branch`'s one shape test; `check_pass_holder`, reused
unchanged, since its wanted path already derives from the branch; and the suites' `TP4_ARGS`,
`render_pass_returns` and `write_fixture_pass`, the last widened by one defaulted argument rather
than copied. `python tools/codebase-map/reuse_lookup.py "admit a second runtime worktree spelling
for a parallel pass branch and its holder path"` ranked `branches`, `add_scratch_worktree`,
`pass_commit` and path resolvers first; `branches` is check-arms' fail-branch census,
`add_scratch_worktree` cuts a scratch tree rather than checking a name, and `pass_commit` is a
non-goal, so no other seam answers "the names the runtime cuts". The task's reuse list,
`resolve_generated_indexes`, `check_gen_region_only`, `covers`, the commit-message exemption,
`run_regen`, `regen.py --write`, `prebuild`, the `passLegs` key shape and `add_scratch_worktree`,
serves the merge-back that unit 2 and unit 3 built; this unit reaches it unchanged through
`--merge`. `python tools/memory-tree/gotchas.py --for-paths` over the four subject files selected
fifteen classes; `two-answers-to-one-question` is answered in §4, "How the two copies are held",
`heredoc-escape-reaches-the-regex` by the regex-literal prefix and the escape-free `TP11` values,
`staged-break-substitutes-a-synthetic-value` by arms that use observed runtime names,
`node-check-is-not-a-syntax-gate` by the workflow syntax check in place of `node --check`, and
`agent-output-interpolated-into-an-instruction` by the hostile `wf_` tail.

Recall terms used: `python tools/memory-recall/query.py "which worktree and branch names does the
runtime cut for an isolated agent inside a workflow" --terms "worktree-agent wf_ isolation worktree
BRANCH_SHAPE TREE_SHAPE check_pass_branch check_pass_holder pass-tree runtime spelling
claude/worktrees"`
