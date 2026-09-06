# TOOL-aHoistedPass-6 — the harness hands out a roster and stops driving the build

**Status:** CLOSED · rev-7 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md](../build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-05-build-TOOL-aHoistedPass-6-1-acceptance-ledger.md](../build/2026-09-05-build-TOOL-aHoistedPass-6-1-acceptance-ledger.md) | journal | — |
| [2026-09-05-prompt-TOOL-aHoistedPass-6-brief.md](../prompts/2026-09-05-prompt-TOOL-aHoistedPass-6-brief.md) | journal | — |
| [2026-09-05-prompt-TOOL-aHoistedPass-6-fold-round1.md](../prompts/2026-09-05-prompt-TOOL-aHoistedPass-6-fold-round1.md) | journal | — |
| [2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md) | spec-audit | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round2.md) | spec-audit | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-06-review-TOOL-aHoistedPass-1-closing-diff-round1.md](../reviews/2026-09-06-review-TOOL-aHoistedPass-1-closing-diff-round1.md) | diff-review | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |
| [2026-09-06-review-TOOL-aHoistedPass-1-closing-diff-round2.md](../reviews/2026-09-06-review-TOOL-aHoistedPass-1-closing-diff-round2.md) | diff-review | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/unattended-build.js` builds every unit of a roster inside ONE `agent()` call, and
that call's prompt tells the agent `--dispatch` is the order gate, which is conditionally false. End
the program after SPEC, AUDIT and a new whole-set DISPOSAL stage, return the ordered roster, and let
the run make one main-loop `Workflow` call per unit — so a per-unit dispatch becomes a tool call the
fan-out hook sees at all, and the three surviving stages stop claiming an enforcement they never had.

## 2. Scope (IN)

- **S1 — DISPOSAL becomes its own stage**, an `agent()` call over the whole spec set with its own
  schema, run after the audit gate and BEFORE the roster is handed out. Today the disposal
  instruction is the `const disposal` string at `unattended-build.js:686-695`, prepended to the BUILD
  prompt at `:786`, so it is carried by the agent that is being deleted. The header's attended-mode
  clause at `:51-53` says "`disposal` below is composed only for a non-CONVERGED verdict" — it names
  the STRING and must name the STAGE. What it states stays true: attended mode's only terminal token
  is CONVERGED, so the disposal stage never runs there.
- **S2 — DELETE the BUILD agent, BY NAME.** The `agent()` call whose options carry `label: 'build:'`,
  its prompt, the `if (!built)` refusal, `const unbuilt`, `const BUILD_SCHEMA`, `const buildRoster`,
  `const driverSteps` (dead the moment the prompt goes) and the `phase('Build')` call. §4 gives each
  one's address at BASE and says what S2 does NOT take with it: the attended-mode `planState`
  refusal grades which units may be DISPATCHED, so it moves ahead of the hand-out rather than leaving
  with the agent.
- **S3 — Correct every `--dispatch`-is-the-order-gate assertion, including the three that do NOT
  leave with the BUILD agent.** FIVE sites carry it at BASE, one more than rev-3 counted because
  attended mode added one; §4 names each, its address, and which of them S2 removes on its own.
- **S4 — The roster RETURN, and FOUR exits that all carry `roster`.** A terminal verdict with
  disposal done returns the ordered roster plus a `dispatch` block; a failed disposal, a `CONVERGING`
  verdict and attended mode's every-unit-terminal exit each return `roster: []`. The fourth landed
  with attended mode after this spec's base and rev-3 did not know it existed. `built`, `unbuilt` and
  `allIds` (`:236`, `:663-664`, `:771`, `:821-822`) go with them.
- **S5 — `meta` stops describing a program that builds.** `description` (`:5`) and the third
  `phases` entry (`:9`) both say this file drives BUILD. Both addresses are unmoved at BASE.
- **S6 — The nesting comment at `:467-468`** stops reading as a consumed budget.
- **S7 — The empty-`units` refusal text at `:182-188`** names `--plan <slug> --paths` rather than the
  bare `--plan` it spells at `:184`, which cannot supply a spec path today.
- **S8 — `bash tools/unattended/unattended.sh --plan <slug> --paths`**: a TSV emitter over the values
  `verb_plan` already resolves per unit, plus the resume note in its own header comment. The default
  `--plan` output stays byte-identical.
- **S9 — Arms in `tools/workflows/unattended-build.test.sh`** for every property S1 and S4 add, and
  arms in `tools/unattended/unattended.test.sh` for both `--plan` modes.
- **S10 — `tools/install-prefix-carried.txt`**, two rows, each rise hand-justified because the
  ratchet is a BAN (`check-install-prefix.sh:315-319`).
- **S11 — The `--paths` sentence in the verb carrier**, `tools/unattended/VERBS.template.md`, with
  `memory/guides/UNATTENDED-VERBS.md` regenerated by `bash tools/unattended/adopt-unattended.sh`
  rather than hand-edited.
- **S12 — `review-harness` 1.6 to 1.7**, on the one line at `tier2-review.js:3` that carries all
  three of its version tokens. This unit changes `review-harness` payload bytes and the sibling that
  also does declines the bump; §8 F1 is why the item sits here rather than there.
- **S13 — the backlog rows for what this unit deliberately does not fix.** Three rows in
  `memory/backlog/TOOL.md`, their ids minted by the session that files them (§2, slug-scoped):
  (1) the `gov:kit unattended-build@1.0` marker at `:3`, which `check-kit-versions.sh` pairs against
  no constant, so it drifts a whole release unnoticed; (2) `meta.description` and `meta.phases`,
  which no leg joins to this file's `phase()` calls, so S5's correction is graded by nothing;
  (3) the hand-out's empty `specPath` for every freshly-specced unit, which nothing refuses. Each is
  a residual §4, §5 or §7 already names, and without a row it is named only in a spec that goes
  CLOSED. §4's Files-touched booked this file before any scope item authorised the edit.

## 3. Non-goals (OUT)

- **The child, `tools/workflows/unattended-unit.js`.** It is its own unit at the preceding order.
  This unit names its path in `dispatch.scriptPath` and asserts nothing about its contents.
- **The M6 route sentence, `UNATTENDED-PROTOCOL.md` §12, and the Skill's loop bullet.** Those are
  `TOOL-aHoistedPass-2` at `order 3`, and two of the three are owner-gated veto-2 carriers.
- **`unattended-build.js:63-67` and `:330-335`**, the superseded `parallelism route: none`
  citations. **rev-6 corrects what this bullet claimed.** It said `TOOL-aHoistedPass-1` "owns that
  correction by name"; that unit's own section 3 says the opposite in bold — S4's row carries all the
  carriers and NO unit of this build takes any of them, including this file's. The two specs
  disclaimed to each other and the edit fell between them, which nothing on the bar would have
  caught, because no leg grades whether a decision row's quotation is still true. The BASE fact:
  `TOOL-aHoistedPass-1` FILED the residual as a backlog row naming every carrier `git grep -ln
  "parallelism route: none" -- tools/` returns — five files, eight sites, `unattended-build.js` and
  `unattended-build.test.sh` among them — and this unit takes none of them either. **Taking the
  correction here was considered and refused**: this unit already edits both files and already owns
  the `review-harness` bump, so the carriers would cost it no extra move, but the filed row asserts
  that no unit of this build edits one, and a unit that quietly falsified a landed backlog row to
  save itself a follow-up is the record-drift this build exists to end. The row stays true and the
  correction stays filed.
- **Making anything refuse a FORKED unit, a re-dispatch, or the successor of a failed pass.** §4
  enumerates what `--dispatch` does refuse; adding a refusal is a separate unit with its own arm.
- **Any concurrent dispatch path.** The return carries `order` so a future caller can group by it.
  Nothing here dispatches two units at once, and M6's parallel clause states a permission.
- **The `brief-recorded` witness leg**, the budget gate, and the kit-dependency work. Separate units.
- **Extending the slot ledger to `Workflow` calls.** It is the change this shape is incompatible
  with, and the note warning against it belongs to the `tools/hooks/` unit at `order 1`.
- **Verifying anything about the tree from inside the script.** A workflow script has no filesystem
  and the file's own header says so at `:23-28`. The disposal stage reports; it does not confirm.
- **The `unattended` kit version.** `DEPL-aHoistedPass-1` at `order 2` takes 1.17 to 1.18 and this
  unit lands inside that release. See §4 for why no second bump is owed or possible to grade.
  (rev-1 through rev-4 named `TOOL-aHoistedPass-2` as the owner; section 8's fork sweep moved it to
  `DEPL-aHoistedPass-1` and stood that unit down. The conclusion is unchanged — the owner is not.)

## 4. Design

### Inventory — the five sites that assert `--dispatch` enforces order

**Re-derived at the run's BASE `e828f778`**, by opening the file, not by trusting rev-1's reading of
it at `c4fcf5ad`. This file is 835 lines at BASE and was 531 at `c4fcf5ad`, and it is byte-identical
between BASE and this worktree's HEAD (`git diff --stat`, empty).
`grep -n -- "--dispatch" tools/workflows/unattended-build.js` returns ELEVEN lines, not the five
rev-1 measured. Of those eleven, `:756` is the call itself, and `:47`, `:210`, `:698-699`, `:739` and
`:753` name the verb without characterising what it refuses. The rest are the assertion sites:

| site | what it says | does S2 remove it? |
|---|---|---|
| `:26-27` | the file's WHY block: *"`--dispatch` refuses a MISSING, THIN or out-of-order unit, and the `pass-order history` leg refuses a unit whose build commit predates its spec"* | **NO** |
| `:44-46` | attended mode's WHAT IT LOSES item 2: *"`--dispatch`'s ORDER REFUSAL — the tree-reading check that a unit is not MISSING, THIN or out of order"* | **NO** |
| `:85-86` | forced-shapes item 1: *"per-unit order moves onto `--dispatch`'s refusal, which reads the tree and is therefore a STRONGER check than a JS loop"* | **NO** |
| `:675-676` | the STAGE 3 comment: *"what ENFORCES it is `--dispatch`, which reads the tree and refuses a unit that is MISSING, THIN or out of the build's declared order"* | yes |
| `:758-760` | `driverSteps`, the unattended branch, reaching the BUILD prompt at `:792`: *"THAT DISPATCH IS THE ORDER GATE: it refuses a unit that is MISSING, THIN or out of the declared order"* | yes |

The design of record names one of these. THREE of the five survive the deletion, so S3 is a separate
scope item rather than a consequence of S2. `:26-27` becomes a statement of what the driver refuses
at the moment of the act, with the order clause marked conditional and the `pass-order history`
clause narrowed to spec-before-code for CLOSED units. `:85-86` is rewritten around DISPOSAL, which is
the stage the one-agent-per-stage shape still applies to. `:44-46` takes the same conditional marking
as `:26-27` and nothing else: it is a true statement about what attended mode gives up, over-claiming
only the order arm's coverage.

### What S2 does NOT delete, now that the BUILD stage holds more than an agent

Attended mode (`TOOL-aStagedLane-2`) landed inside this stage after `c4fcf5ad`, so "delete the BUILD
agent" no longer describes one contiguous region. The boundary, drawn by name:

| at BASE | S2? | why |
|---|---|---|
| the `label: 'build:'` agent (`:784-797`), its `if (!built)` refusal (`:798-803`), `const unbuilt` (`:804`) | delete | the hoist's whole point |
| `BUILD_SCHEMA` (`:298-307`) | delete | it binds a return that no longer exists |
| `const buildRoster` (`:783`), `const driverSteps` (`:751-760`) | delete | consumed only by the deleted prompt, at `:788` and `:792` |
| `phase('Build')` (`:696`) | delete | S5 makes the third phase `Disposal` |
| the attended `planState` refusal (`:718-750`) and `skippedDone` | **KEEP** | it grades which units may be DISPATCHED, so it belongs to the hand-out; `buildUnits` (`:765`) becomes the roster filter and `skippedTerminal` stays on the return |
| the attended every-unit-terminal return (`:766-782`) | **KEEP** | it is exit four; S4 gives it `roster: []` |

One instruction is LOST rather than moved, and saying so is cheaper than letting a reader find it:
`driverSteps`' ATTENDED branch tells the pass to write down the paths it will touch before touching
them, because the driver's recording verbs are unavailable without a run-state file. That is a
per-pass instruction and the child owns per-pass instructions, and the child is §3's first non-goal.
This unit does not re-home it, so an attended run under the hoist loses it unless the child carries
it.

### What `--dispatch` actually refuses

`verb_dispatch` is `unattended.sh:4579-4812`. It carries twenty `fail 49` sites plus
`refuse_if_terminal` at `:4680`, every one opened here. The design of record says it refuses
"exactly two things about the UNIT'S STATE"; two is the count of arms that grade the unit's SPEC, and
the wider set matters because a run reading only that sentence expects a backstop it does not have.

**Unit-state and run-state refusals.**

| line | refuses |
|---|---|
| `:4584` | no run-state file for this slug |
| `:4587` | a `--pass` value that is not id-shaped by the driver's own spelling |
| `:4604` | a unit no tracked spec under this build defines — M2's MISSING |
| `:4609` | a unit whose spec grades `THIN`; this `case` has exactly one arm |
| `:4627` | this unit's own status header carrying a MALFORMED `order` verb |
| `:4636` | a SIBLING's status header carrying a MALFORMED `order` verb |
| `:4652` | an earlier order step still holding a unit that is neither terminal nor dispatched |
| `:4680` | the RUN being at a terminal phase, through `refuse_if_terminal` |

**Write-set refusals**, over the `--writes` paths and their siblings' declarations.

| line | refuses |
|---|---|
| `:4588` | no `--writes` path at all |
| `:4659` | an empty path |
| `:4660` | an absolute path |
| `:4661` | a path escaping the repository |
| `:4664` | the repository root |
| `:4667` | a glob metacharacter |
| `:4670` | whitespace inside a path |
| `:4677` | a path spelling the declared bypass flag |
| `:4690` | the run-state file, or a path containing it |
| `:4694` | a path overlapping a declared `SHARED_RECORDS` entry |
| `:4703` | an unresolvable `HEAD`, which is the group key |
| `:4767` | a generated index declared together with its generator |
| `:4783` | a path a sibling pass in the same group already declared |

**What it does NOT refuse, and this unit claims no substitute.** A FORKED unit: `plan_state` returns
`READY`, `THIN` or `FORKED` and the `case` at `:4608-4610` has only the `THIN` arm. An already-CLOSED
unit: `plan_state` never returns a terminal token, so a closed unit grades `READY` and passes. A
re-dispatch: the comment at `:4791-4808` records that the re-declaration machinery was removed
deliberately, so every `--dispatch` parks a fresh row and nothing rewrites or refuses an earlier one.
The successor of a failed pass: `:4652` skips any sibling carrying a dispatch row (`:4647`), and
`--dispatch` writes that row itself at `:4813` before the pass runs. **The run holds all four.**

The order gate is also opt-in twice over: `:4630` runs it only when THIS unit carries an `order`
verb, and `:4639` skips any sibling that carries none.

### The disposal stage

DISPOSAL is a whole-set act because it is authority over every unit's spec, not over one unit's.
Carrying it into the first child would spend it on whichever unit happens to be first, and a resumed
run whose first roster element is already built would spend it on a child that does nothing.

It runs only on a non-`CONVERGED` terminal verdict, because the driver emits `CONVERGED` only at a
blocker count of zero. The `CONVERGED` path **announces the skip** rather than passing silently:

```js
log('disposal: skipped — the verdict is CONVERGED, so the driver reported zero standing blockers')
```

The prompt is the current `:686-695` string, unchanged in substance: BUILD-METHOD M4 admits FOLD and
PROMOTE and no third disposition. Its schema follows the file's own rule at `:242-245`, that a
refused list is its own required field and never an absence:

```js
const DISPOSAL_SCHEMA = {
  type: 'object',
  required: ['disposed', 'standing', 'summary'],
  additionalProperties: true,
  properties: {
    disposed: { type: 'boolean' },
    standing: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
}
```

The agent call carries `{ label: 'dispose:' + slug, phase: 'Disposal', schema: DISPOSAL_SCHEMA }`.
The `phase:` key is there because all three surviving agents carry one (`:399`, `:493`, `:604`); the
design of record's block omits it.

**If disposal fails the roster is not handed out.** `d` absent, or `d.disposed !== true`, returns the
empty-roster shape below with a `DEGRADED` note naming what stood. There is no partial hand-out: a
roster minus the units a blocker touches is a judgement the script cannot make, having no filesystem.

### The return — four exits, one predicate

Every non-throwing exit carries `roster`, so `roster.length === 0` is the caller's whole stop
condition. The design of record leaves the `CONVERGING` early return at `:648-670` untouched while
its Skill bullet tells the run that an empty roster is the refusal; that return carries no `roster`
key at all, so a caller reading `roster.length` would read a property of `undefined` and throw. The
attended every-unit-terminal return at `:768-781` has the identical defect and was not in the design
at all — it landed after this spec's base. All four exits are unified here instead.

| exit | `roster` | note |
|---|---|---|
| `CONVERGING` (`:646`) | `[]` | `HELD AT AUDIT` plus the existing fold-and-re-invoke `nextAction` |
| attended, every unit terminal (`:766`) | `[]` | its existing note, which says something no other exit's does: the ATTENDED-mode statement plus the `DEGRADED` prefix it already composes |
| disposal not done | `[]` | `DEGRADED — blockers were not disposed: …` |
| terminal verdict, disposal done | the ordered array | `prologue complete; N unit(s) to dispatch` |

The full shape of the fourth exit:

```js
return {
  slug: slug, mode: mode, base: base, round: roundNo,
  units: ordered.length, specced: speccedCount, specRefused: specRefused,
  verdict: verdict, blockers: au.blockers, lastReport: lastReport,
  skippedTerminal: skippedDone,
  roster: buildUnits.map(function (u) {
    return { id: u.id, order: u.order, specPath: u.specPath || '', briefPath: u.briefPath || '' }
  }),
  dispatch: {
    scriptPath: 'tools/workflows/unattended-unit.js',
    args: { repo: repo, slug: slug, driver: DRIVER, ground: GROUND, checklist: CHECKLIST },
    perUnit: ['unitId', 'specPath', 'briefPath'],
    resolvePathsWith: DRIVER + ' --plan ' + slug + ' --paths',
  },
  note: /* as the table above */,
}
```

**THE ROSTER MAPS `buildUnits`, NOT `ordered`, and rev-6 corrected the block rather than the KEEP
row.** The two said different things: the KEEP row calls `buildUnits` "the roster filter" while the
block spelled `ordered.map(...)`, and they cannot both be implemented whenever attended mode has
some-but-not-all terminal units. Written as the block spelled it, the attended `planState` refusal
S2 deliberately KEEPS would have filtered nothing and every already-terminal unit would have been
handed out for dispatch — which is verbatim the defect `unattended-build.js`'s own comment above
`buildUnits` records: "the BUILD agent was handed the UNFILTERED roster", so the run told its
operator it had skipped the terminal units and told its agent to build them. Handing the same
unfiltered array to a per-unit dispatch loop reproduces it one layer over. `units:` still counts
`ordered`, because that field is the SET SIZE and not the work list. AC25 grades the difference.

`mode` and `skippedTerminal` are in that block because EVERY return at BASE carries them and the
design of record predates both. `mode` is a run-integrity field — its own comment at `:823-826` says
it exists so a caller can tell an attended run from an unattended one — so dropping it here would
silently undo `TOOL-aStagedLane-2`, unremarked, in a diff about something else.

Four further properties of that block are load-bearing.

**`specPath` is EMPTY for every unit the SPEC stage just authored, and the program cannot fix it.**
`units` arrives in `args` and `ordered` is a sorted copy (`:216-221`); `grep -n "specPath" ` over the
file returns `:130`, `:230` and `:489`, and not one of them is a write. The field is carried only so a
caller that already had a path does not lose it, and `resolvePathsWith` names the command that
resolves the rest. A run that dispatches straight off this array hands a child an empty spec path.

**`dispatch.args` carries the invariants and `perUnit` names the three that vary.** The roster is not
among them, which is the whole shape change: a child receives its own unit and never the list.

**`checklist` moves into `dispatch.args`.** The bug-class command is spelled at `:794` today, inside
the prompt S2 deletes, and it is the file's only `gotchas.py` occurrence. A `CHECKLIST` constant
beside `DRIVER` (`:215`) is where it goes, because the child spells zero `tools/` literals and cannot
carry it.

**No `reportPath` reaches any child.** What a unit must know beyond its spec goes in its BRIEF file,
because `--brief` is the only carrier that hashes anything: it refuses an untracked path
(`unattended.sh:4199-4200`), hashes with `git hash-object` (`:4203`), and parks the row
`brief · item <unit> · reason <hash12> <path>` (`:4217`). Nothing hashes a prompt string.

`renderRoster` (`:226`, called `:235`) SURVIVES, and not only because the SPEC fan calls it per group
(`:375`, consumed at `:382`) and the blob resolver consumes it (`:488`). It is this file's only
top-level definition, and
`tools/codebase-map/map_lib.py:474-475` RAISES `MapError` on a JS file yielding none. Deleting it
with the BUILD agent would red `codebase-map coverage + freshness` rather than fail quietly.

### Why one `Workflow` call per unit costs no slot, and why nesting is not a budget

`guardAgentSpawn` (defined `agent-cap.js:1525`) is reached only on `data.tool_name === 'Agent'`
(`:1698-1699`, opened here at BASE — that file grew 215 lines since `c4fcf5ad` and all three
addresses below moved). N main-loop `Workflow` calls therefore spend none of the five-per-prompt
direct-spawn budget, and N is not bounded by it. What each `scriptPath` call does buy is a re-read of
the child at `:1710-1712`, feeding four rule blocks — still four, at `:1725`, `:1745`, `:1766` and
`:1797`, counted here rather than carried. A `name:` call reads nothing and exits 0 at `:1722`.

The comment at `:467-468` reads *"Nesting is one level deep … so the one level is available and is
spent here."* That reads as a budget one caller consumes, and it would tell a later author that the
disposal stage may not call a second sub-workflow. It is a DEPTH limit: a parent may make several
sequential nested calls at the same depth, evidenced by `wf_9b984206-816`'s three sequential
`await workflow()` calls all returning. **That evidence is CARRIED from an earlier pass and was not
re-run here**, and the corrected comment says so rather than asserting it as measured. Under the
hoist the point is close to moot — the per-unit dispatches are main-loop calls at depth zero — which
is exactly why a stale sentence about it would sit unread until it misled somebody.

### `--plan <slug> --paths`

`verb_plan` (`unattended.sh:2010-2178`) prints a padded three-column table and no spec path. It
resolves the path per unit internally at `:2127` (`spec="${SPEC_PATH[$id]:-}"`) and discards it. The
emitter hands that value back.

`--plan` exits INSIDE the argument-parsing loop (`:4892`), so `--paths` cannot be a top-loop flag —
at the moment the arm runs, a later flag has not been consumed. It is read positionally after the
slug, in the shape the `--phase` arm at `:4893-4897` already uses for `--witness`:

```sh
--plan)  shift; refuse_waive_unless_preflight --plan || exit 1
         PL_SLUG=${1:-}; shift 2>/dev/null || true
         PLAN_PATHS=""; [ "${1:-}" = "--paths" ] && PLAN_PATHS=paths
         verb_plan "$PL_SLUG"; exit $? ;;
```

`PLAN_PATHS` is initialised at file scope beside the other globals, because `set -u` is on and the
row emitter reads it without a caller frame.

**ONE emitter, so the two modes cannot disagree about which rows are units.** The three padded
`printf` sites that name a unit id (`:2132`, `:2145`, `:2155-2156`) route through:

```sh
plan_row() { # id · status · state · specPath — PATHS mode swaps the shape and nothing else
  if [ -n "$PLAN_PATHS" ]; then printf '%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4"
  else printf '%-34s %-11s %s\n' "$1" "$2" "$3"; fi
}
```

The two `NOT A UNIT` diagnostics (`:2078`, `:2082`) are keyed on a FILENAME rather than an id and
keep their padded shape in both modes. A caller splits on TAB and skips any line with fewer than four
fields, which is stated in the emitter's header rather than left to be inferred. The `roster:` and
`next:` lines are untouched, so one `--paths` invocation answers both "which unit is next" and "where
is its spec" — which is what makes it the resume path's single source.

**Order comes free.** The unit set and its order come from the generated units region (`:2117-2126`),
which is rendered in build order, so a `--paths` listing IS build order. No sort is added.

**`briefPath` is not obtainable from any verb**, because the run authors that file. It is recoverable
on resume from the run-state file's `brief · item` rows (`:4217`).

**No new refusal branch.** `--paths` changes an output shape. `check-arms.py --check` therefore owes
this unit nothing, and saying that is cheaper than an arm for a branch that does not exist.

### Resume — the re-entry contract

**A resumed run dispatches a child WITHOUT calling the harness.** It re-reads the run-state file,
reaps and re-schedules the keepalive, runs `--plan <slug> --paths` for `next` and the spec paths,
recovers `briefPath` for any already-briefed unit from that file's `brief · item` rows, and makes the
next `Workflow` call. It pays no fresh SPEC pass and records no fresh audit round.

`next` is a TREE FACT and is re-asked between every dispatch rather than read off a held list, which
did not survive the last compaction. It has FOUR shapes and a run branches on all four:
`(READY - build it)` at `:2149`; `(THIN)` or `(FORKED)` at `:2148` and `(MISSING - spec it first)` at
`:2158`, none of which may be dispatched; `next: none - every tracked spec is terminal` at `:2175`,
which is completion; and `next: none - no tracked spec grades as a unit` at `:2173`, which is a
REFUSAL printed at `return 0` (`:2177`) and reads like completion to anyone who does not know.

**What advances the loop counter is a spec status flip and nothing else.** `:2144` is the only line
that removes a unit from `next` candidacy, and it reads the spec's own status header. A child that
commits without setting `CLOSED` or `WONTDO` leaves `--plan` naming the same unit forever. The child
is instructed to do it in the same commit; that instruction is the child unit's scope and **nothing
in this unit enforces it.**

**What this contract is held by: the run.** No branch of `unattended.sh` and no leg observes whether
a resumed run re-invoked the harness. A resume inside the SPEC or AUDIT prologue still records a
second review round; the hoist shrinks that window from the whole build to the prologue and does not
close it.

### Version markers, and why this unit moves none

`check-kit-versions.sh` requires the three `unattended` engine constants and the five tracked
`tools/unattended/*.template.md` markers to agree — eight carriers, all reading 1.17 here.
`DEPL-aHoistedPass-1` at `order 2` takes them to 1.18, and this unit at `order 5` lands inside that
release. No branch of `check-kit-versions.sh` reads a diff, so a second bump within one build's
landing range is neither required nor gradeable. **This unit is therefore NOT owner-gated**, and the
design of record marks it gated on the strength of a bump it does not owe. `VERBS.template.md` is not
on the veto-2 list; only `SKILL.template.md` and the two guide pairs are.

The `review-harness` kit is a different matter, and S12 takes it. Its version is read from
`tier2-review.js` (`tools/workflows/kit.toml`), whose `:3` carries `meta.version`, a
`gov:kit tier2-review@` marker and a `gov:kit review-harness@` marker on ONE line, all three compared
by `check-kit-versions.sh:28-44`. `unattended-build.js` ships under that kit (`include = "**"`), so
editing it is a payload change; the sibling child unit at `order 4` also changes those bytes and its
spec names no bump, so this unit takes the single 1.6 to 1.7 move for the release.

`tools/workflows/unattended-build.js` carries `gov:kit unattended-build@1.0` at `:3`.
`check-kit-versions.sh` pairs `tier2-review` and `review-harness` on `tier2-review.js` and names no
`unattended-build` id anywhere, so that marker is graded by nothing and goes stale in silence. It is
not moved here; **S13 files the backlog row that records it**, which rev-3 promised in Files-touched
and no scope item delivered.

### The install-prefix ratchet, measured rather than predicted

`carried_rows` counts matching LINES for a `tools/<kit>/<file>.<ext>` literal per path — a line
carrying two literals counts once, which its own comment at `check-install-prefix.sh:243` states.
**Re-measured at BASE with `bash tools/check-install-prefix.sh --list`, which reports `5` for
`tools/workflows/unattended-build.js`**, matching its row at `install-prefix-carried.txt:124`. The
five lines are `:71` (`tools/hooks/agent-cap.js`), `:215` (`DRIVER`), `:457` and `:519` (both
`tools/workflows/tier2-review.js`), and `:794` (`gotchas.py`). The glob at `:470` does NOT count: the
checker's `re_ship` filename class is `[A-Za-z0-9_.-]+` and excludes `*`.

The design of record attributes the rise to the `dispatch.scriptPath` literal and implies the
`gotchas.py` line leaves with the prompt. It does not leave — it MOVES into `CHECKLIST`, because the
child spells zero `tools/` literals. So the arithmetic is five minus zero plus one, and the row goes
**5 to 6** with its
reason extended to name the sub-workflow the harness hands out. `resolvePathsWith` adds nothing: it
is built from `DRIVER`, already counted.

`tools/workflows/unattended-build.test.sh` is in the carried population too — shipped tests are
received — so any arm spelling `tools/workflows/unattended-unit.js` raises its row from 2. That rise
is DERIVED at the landing by `bash tools/check-install-prefix.sh --list` and justified in the row,
not predicted here. The precedent for spelling it rather than deriving it is that file's own existing
reason: the literal IS the assertion.

### Files touched (estimate)

| file | what |
|---|---|
| `tools/workflows/unattended-build.js` | S1 through S7 |
| `tools/workflows/unattended-build.test.sh` | the arms of S9 |
| `tools/unattended/unattended.sh` | `PLAN_PATHS`, `plan_row`, three call sites, the `--plan` arm, the usage line at `:6` |
| `tools/unattended/unattended.test.sh` | both `--plan` mode arms |
| `tools/workflows/tier2-review.js` | `:3` alone, all three version tokens, 1.6 to 1.7 |
| `tools/unattended/VERBS.template.md` | the `--paths` sentence at its `--plan` bullet (`:45`) |
| `memory/guides/UNATTENDED-VERBS.md` | REGENERATED by `bash tools/unattended/adopt-unattended.sh` |
| `tools/install-prefix-carried.txt` | two rows |
| `memory/backlog/TOOL.md` | the three rows S13 names |

No map artifact moves. `BUILD_SCHEMA` and `DISPOSAL_SCHEMA` are `const`s whose right-hand side is an
object literal, and `JS_DEFINITION_RULES` (`map_lib.py:405-415`) indexes a `const` only when its
right-hand side is a function, an arrow or a class. `renderRoster` stays, so `symbols.json` is
unchanged. The `workflow-scripts` claim at `memory/map/features/unattended.md:14` gains its second
entry in the CHILD's unit, not here.

### Alternatives rejected

- **Keep BUILD and loop `workflow(child)` inside it.** Every such call fires ZERO hooks —
  `agent-cap.js:9` says *"workflow sidechains don't run hooks"* — so the per-dispatch delta the hoist
  buys is zero to four rules, not one read per build to one per dispatch.
- **Carry disposal into the first child.** It is authority over the whole spec set, and a resumed run
  whose first roster element is already built would spend it on a child that does nothing.
- **Return a partial roster when disposal fails.** Deciding which units a standing blocker touches
  needs the tree, which this runtime does not have. An empty roster is the honest refusal.
- **Add `--plan-paths` as a new verb.** `check-unattended.sh` check 26 joins every declared verb to
  three carriers, so a new verb owes a header line, a `VERBS.template.md` entry and a Skill
  invocation. `--paths` is an output mode on a verb that already exists.
- **Emit the TSV in addition to the padded table.** Two shapes of the same rows in one stream, and a
  caller that greps loosely joins on both. The mode swaps one `printf`.
- **Derive the child path in the test arms instead of spelling it.** It makes the arm agree with
  whatever the harness did, which is the reason the file's existing ratchet row gives for spelling it.

## 5. Production-readiness checklist

- **security** — No new trust boundary. The run gains N main-loop tool calls where it had one, and
  each is a `PreToolUse` the fan-out hook sees; the previous shape's per-unit dispatches fired no
  hook at all. Nothing here reads untrusted input or writes outside the two files named.
- **perf / scale** — N `Workflow` returns replace one long `agent()` call. Whether that raises or
  lowers the stall rate is UNMEASURED in either direction and this spec asserts neither. The
  keepalive is time-keyed (`.unattended.conf:50`), so N returns cost it nothing.
- **a11y** — N/A — a workflow script and a shell verb, neither with an interface.
- **i18n** — N/A — the emitted rows are ids, statuses and repo-relative paths.
- **error / empty / loading states** — Three exits, all carrying `roster`, and the empty one is the
  refusal in both cases that produce it. The `CONVERGED` disposal skip is announced in the log.
- **observability** — `log()` lines for the disposal verdict and for its skip. The `--paths` rows are
  the run's own source for what it dispatches next. The harness still writes nothing to disk, and no
  leg can tell a harnessed run from an unharnessed one; that is the witness unit's problem, not this
  one's, and it is not narrowed here.
- **risks (concurrency, data-loss, rollback hazards)** — A run that ignores the hand-out and
  dispatches straight off the returned `roster` hands a child an empty `specPath` for every
  freshly-specced unit. Nothing refuses that; the child throws, and the run reads a throw. Rollback
  is a revert of two files with no on-disk format change.
- **testing + left-shift gates** — This unit adds no gate leg. Its arms live in two suites that the
  2026-08-23 owner ruling keeps off the bar, so §7 names the boundary as absent rather than implying
  one. The arms are staged RED before the change lands.
- **migration / rollback** — None. No on-disk format moves. A run mid-flight when this lands is
  holding a return shape from the old file; that shape's `built`/`unbuilt` keys are gone, which is
  why the note string names the change and the run reads `roster` before anything else.
- **user docs** — `tools/unattended/VERBS.template.md` gains the `--paths` sentence and its render is
  regenerated. `memory/guides/BUILD-METHOD.md` and the Skill are `TOOL-aHoistedPass-2`'s.

## 6. Acceptance criteria

- **AC1** — When the file is grepped for its agent LABELS after the change,
  `grep -c "label: 'build:" tools/workflows/unattended-build.js` returns `0`, and each of
  `label: 'spec:`, `label: 'audit:subjects:`, `label: 'audit:record:` and `label: 'dispose:` returns
  `1` — four surviving `agent()` call sites, named rather than counted. rev-1 asserted "exactly four
  lines" from `grep -nE "= await agent\("`; that pattern returns TWO at BASE (`:485` and `:784`),
  because the spec fan spells `return agent(` and the round recorder `: await agent(`. It graded a
  spelling, not a population.
- **AC2** — When
  `grep -cE "out of the declared order|out of the build's declared order|out-of-order unit|per-unit order moves onto|THAT DISPATCH IS THE ORDER GATE" tools/workflows/unattended-build.js`
  runs, it returns `0`. Run at BASE it returns `5` (`:26`, `:85`, `:676`, `:758`, `:759`); rev-1's
  pattern, without the second alternative, returns `4` and MISSES `:676`, whose wording is *"out of
  the build's declared order"* — so the STAGE 3 site could have been left standing on a green
  criterion. The `:44-46` site's phrase spans two lines and no line-based grep reaches it; AC2b
  grades it.
- **AC2b — the positive half, because an absence grades a DELETION exactly as well as a rewrite.**
  When the three surviving sites are read after the change: the WHY block names the two spec-state
  refusals (MISSING and THIN), marks the ORDER clause conditional on the unit carrying an `order`
  verb, and carries the `pass-order history` clause narrowed to spec-before-code for CLOSED units;
  the forced-shapes item names DISPOSAL as the stage the one-agent-per-stage shape still applies to;
  and attended mode's WHAT IT LOSES item 2 carries the same conditional marking on its order arm.
  Each is a grep for the SUCCESSOR text. S3 specifies replacement text, and a scope item that
  specifies text may not be graded solely by AC2 — deleting the three survivors would satisfy AC2
  perfectly, which is the green-by-absence class.
- **AC3** — When `grep -c "BUILD_SCHEMA" tools/workflows/unattended-build.js` runs it returns `0`,
  and `grep -nE "^const (allIds|unbuilt|built|buildRoster|driverSteps) " ` names no line. All five
  are `const`s at BASE (`:236`, `:804`, `:784`, `:783`, `:751`) and all five leave with S2 or S4.
- **AC4** — When the suite runs the harness with a `CONVERGED` verdict and no `dispose:` double, the
  trace carries no `agent:dispose:` entry and carries the log line naming `disposal: skipped`. A skip
  that looks like a pass is what this arm exists to distinguish.
- **AC5** — When the suite runs the harness with a `NON-CONVERGENT` verdict and a `dispose:` double
  returning `{"disposed":false,"standing":["b1"],"summary":"x"}`, the `RESULT` carries `"roster":[]`
  and a note beginning `DEGRADED`, and the trace carries no agent call after `agent:dispose:tB`.
- **AC6** — When the suite runs the harness with a `CONVERGING` verdict, the `RESULT` carries
  `"roster":[]`; and when it runs the harness in ATTENDED mode with every unit already terminal, that
  return carries `"roster":[]` too. Neither carried a `roster` key before this change, so both arms
  are staged against the current file first and observed to FAIL there. The second exit is the one
  rev-3 did not know existed, and it is the same `roster.length` on `undefined` throw.
- **AC7** — When the suite runs the harness with a terminal verdict and a successful `dispose:`
  double, the `RESULT`'s `roster` is an array of three objects each carrying exactly `id`, `order`,
  `specPath` and `briefPath`, in `order` then id sequence, and `dispatch.scriptPath` equals the
  repo-relative path of the child script `TOOL-aHoistedPass-5` lands — the literal §4 spells — while
  `dispatch.resolvePathsWith` ends with `--plan tB --paths`.
- **AC8** — When the suite asserts on `dispatch.args`, its keys are exactly `repo`, `slug`, `driver`,
  `ground` and `checklist`, and no key of the return below `dispatch` is named `roster` inside it.
  The child never receives the list.
- **AC9** — When `grep -c "renderRoster" tools/workflows/unattended-build.js` runs it returns at
  least `3` — the definition, its call and its use — and `python3 tools/codebase-map/test_codebase_map.py`
  exits `0` with no regenerated artifact in the diff.
- **AC10** — When `bash tools/unattended/unattended.sh --plan <slug>` runs against a fixture build,
  its output is BYTE-IDENTICAL to the same command run on the PRE-CHANGE tree, captured before the
  change and diffed. The human table is untouched and the arm proves it rather than asserting it.
  rev-3 anchored this on `c4fcf5ad`; that anchor still yields the same bytes, because
  `tools/unattended/unattended.sh` is byte-identical at `c4fcf5ad` and at BASE — but the criterion is
  about this change, so it names the tree the change is made on rather than a sha it will outlive.
- **AC11** — When `bash tools/unattended/unattended.sh --plan <slug> --paths` runs against the same
  fixture, every line naming a unit id carries exactly three TAB characters, the fourth field of a
  unit with a tracked spec is that spec's repo-relative path, the fourth field of a `MISSING` unit is
  empty, and the `roster:` and `next:` lines are present and unchanged.
- **AC12** — When the `--paths` rows are compared to the region order that
  `bash tools/unattended/unattended.sh --status <slug>` reads, the ids appear in the same sequence.
  Order comes from the region and no sort was added.
- **AC13** — When `bash tools/unattended/unattended.sh --plan` runs with the two `NOT A UNIT` fixture
  specs present and `--paths` given, those two diagnostic lines carry ZERO TAB characters and are
  therefore skippable by a four-field split.
- **AC14** — When the empty-`units` refusal is triggered by calling the harness with `"units":[]`,
  the thrown message names `--plan <slug> --paths` and no longer names bare `--plan`.
- **AC15** — When `grep -n -- "Nesting" tools/workflows/unattended-build.js` names the nesting
  comment and that comment is read, it names a DEPTH limit and marks the three-sequential-calls
  evidence as CARRIED from an earlier pass; and `grep -cE "\bspent\b|\bbudget\b"` over the whole file
  returns `0`. Measured at BASE, that count is `1` and its one hit IS the comment (`:468`), so the
  criterion has a failing case that has been observed. rev-1 read the comment with
  `sed -n '276,277p'`, which at BASE prints `const SUBJECTS_SCHEMA = {` — an acceptance criterion
  anchored on a line range rots between authoring and landing, in the one place where rot is graded
  as failure. Cite by NAME, not by span.
- **AC16** — When `node -e` evaluates `meta` out of the file, `meta.phases` has three entries whose
  titles are `Spec`, `Audit` and `Disposal`, and `meta.description` contains neither `BUILD` nor
  `-> BUILD`. Nothing standing grades this pair, which is stated in §7 rather than implied.
- **AC17** — When each new arm is staged into `tools/workflows/unattended-build.test.sh` WITHOUT the
  source change, `bash tools/workflows/unattended-build.test.sh` FAILS naming each of them; with the
  change it exits `0`. An arm whose failing case has not been observed asserts nothing.
- **AC18** — When `bash tools/check-install-prefix.sh` runs after the change it exits `0`, with
  `tools/workflows/unattended-build.js` at `6` in `tools/install-prefix-carried.txt` and its reason
  string naming the dispatched sub-workflow. The test file's row is set from
  `bash tools/check-install-prefix.sh --list` at the landing and carries its own justification.
- **AC19** — When `bash tools/unattended/adopt-unattended.sh --check` runs after
  `bash tools/unattended/adopt-unattended.sh` has regenerated the verb carrier, it exits `0`, and
  `grep -c -- "--paths" memory/guides/UNATTENDED-VERBS.md` returns at least `1`.
- **AC20** — When `bash tools/unattended/check-unattended.sh` runs, it exits `0`; check 26's join
  still finds `#   unattended.sh --plan ` in the driver header, which the amended usage line keeps.
- **AC21** — In a scratch clone, when `bash tools/unattended/unattended.sh --dispatch <slug> --pass <a unit --plan grades FORKED> --writes <a legal path>`
  runs against a live run-state file, it exits `0` and parks a dispatch row. The enumeration in §4 is
  grounded on an observation rather than on a reading, and this is the claim the build's README
  forbids any spec from getting wrong.
- **AC22** — When `bash tools/check-kit-versions.sh` runs after the change, it exits `0` with all
  three tokens on `tier2-review.js:3` reading `1.7`. With `meta.version` moved and the
  `gov:kit review-harness@` marker left at 1.6, it exits non-zero naming that marker — the arm the
  three-token line exists for, and one this repo has already had go quietly green once.
- **AC23** — When `node tools/workflows/check-workflow-syntax.js`,
  `bash tools/workflows/check-verifier-fanout.sh`, `bash tools/workflows/check-review-join.sh`,
  `python3 tools/memory-tree/check-arms.py --check`, `bash tools/check-kit-versions.sh` and
  `bash tools/memory-tree/check-memory-hygiene.sh` run on the landing commit, all six exit `0`.
- **AC24** — When `memory/backlog/TOOL.md` is read after the change, it carries the three rows S13
  files: one naming the ungraded `gov:kit unattended-build@` marker, one naming `meta.description`
  and `meta.phases` as graded by no leg, and one naming the hand-out's empty `specPath` for every
  freshly-specced unit. Each row names its subject in text a grep finds, and each carries an id
  minted by the filing session. Before this rev the unit's Files-touched booked
  `memory/backlog/TOOL.md` while no scope item filed anything into it.

- **AC25** — When the attended fixture has some-but-not-all units terminal, every id in
  `skippedTerminal` is ABSENT from the returned `roster`, and `units` still counts the whole ordered
  set. **The two are different arrays and section 4 spelled them as one until rev-6.** No existing
  criterion distinguished them: AC7 grades three objects in order sequence and AC8 grades only
  `dispatch.args` keys, so a roster built from `ordered` would have passed both while handing every
  already-terminal unit out for dispatch.

## 7. Gates

Green on the landing commit, every one of them chunk `declarations`, `product`, `wiring` or `records`
with subject `repo` and no guard, so every one runs on an ordinary bar:

- `workflow script syntax` — `node tools/workflows/check-workflow-syntax.js`
- `verifier fan-out` — `bash tools/workflows/check-verifier-fanout.sh`
- `review-join ban (no ref-keyed join)` — `bash tools/workflows/check-review-join.sh`, whose
  population is every `*.js` under `tools/`, so the edited parent is in it
- `unattended kit gate` — `bash tools/unattended/check-unattended.sh`, for check 26's verb join
- `unattended skill wiring` — `bash tools/unattended/adopt-unattended.sh --check`, the byte-compare
  that makes the regenerated verb carrier a derivation rather than an authoring act
- `install-prefix (shipped surface)` — `bash tools/check-install-prefix.sh`
- `harness arms (fail branches armed or pinned)` — `python3 tools/memory-tree/check-arms.py --check`
- `kit version markers`, `codebase-map coverage + freshness`, `memory hygiene`

**This unit adds no gate leg, and the arms it adds are on no bar.** That is the honest statement of
its coverage. `tools/workflows/unattended-build.test.sh` and `tools/unattended/unattended.test.sh`
appear in no row of `tools/gate-legs.json` — derived here, and the second is absent because the
2026-08-23 owner ruling took the unattended kit's seven `*.test.sh` legs off the bar. So AC4 through
AC8, AC10 through AC14 and AC17 are observations the RUN makes by executing both suites by hand and
reporting the result, and nothing standing re-checks them afterwards. The compensating check is that
hand-run, named in the landing report with its exit codes.

**Two claims in this unit are graded by nothing at all, said here rather than left to be found.**
`meta.description` and `meta.phases` (AC16): no leg joins `meta.phases` to the file's `phase()` calls,
and `check-workflow-syntax.js:30` reads the `meta` marker only as a population SELECTOR. And the
`gov:kit unattended-build@1.0` marker at `:3`, which `check-kit-versions.sh` pairs against no
constant, so it may drift a whole release unnoticed. **S13 files a backlog row for each**, so the
two survive this spec going CLOSED.

## 8. Open questions

- **F1 — which `tools/workflows/` unit carries the `review-harness` 1.6 to 1.7 bump.** Two units of
  this build change that kit's payload bytes: `TOOL-aHoistedPass-5` at `order 4` adds
  `unattended-unit.js`, and this one edits `unattended-build.js`. A kit version is a RELEASE rather
  than a per-commit stamp, so bumping it twice inside one build records a release that never shipped,
  and bumping it zero times ships two payload changes under a stale version. Nothing machine-checks
  either direction: `check-kit-versions.sh` grades marker and constant AGREEMENT, and no branch of it
  reads a diff to ask whether a body change earned a bump.
  **Recommendation, and S12 acts on it: this unit takes the single 1.6 to 1.7 move.** The earlier
  order would ordinarily own it, but `TOOL-aHoistedPass-5`'s spec was read here and names no bump —
  it discusses only its own ungraded `gov:kit unattended-unit@1.0` marker. If that spec is revised to
  take the bump, S12 and AC22 drop out of this one; they must not both land.

RESOLVED (agent, 2026-09-05, delegated): **F1 — this unit takes the single `review-harness` 1.6 to 1.7 move**, as S12 and AC22
already specify. `TOOL-aHoistedPass-5`'s spec was re-read during this sweep and is NOT revised to
take the bump, so S12 and AC22 stand rather than dropping out. The two must not both land, and this
line is the record of which one does.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against `origin/main` at `c4fcf5ad` in a worktree
  standing at that exact sha, so every line number above was opened locally rather than through a
  blob. Corrections made to the design of record while writing it:
  - **Two of the four `--dispatch`-is-the-order-gate assertions do NOT leave with the BUILD agent.**
    The design names `:495-497` and treats the deletion as removing the over-claim. Measured here:
    `grep -n -- "--dispatch"` returns five lines, of which `:26-27` and `:56-57` make the same
    conditional claim and survive S2 untouched, and `:462-463` is a third site inside the deleted
    region that the design does not name. S3 exists because of this.
  - **The nesting comment is `:276-277`, not `:274-279`.** The design's rev-8 change ledger
    "corrects" its predecessor's citation to a range whose `:278` is a bare `//` and whose `:279`
    opens the unrelated `FIRST CALLER IN THE REPO` paragraph. The predecessor was right.
  - **The `CONVERGING` return would have thrown in the caller.** The design leaves `:441-457`
    untouched while its Skill bullet tells the run that an empty roster is the refusal. That return
    carries no `roster` key, so `roster.length` reads a property of `undefined`. All three exits are
    unified here and AC6 stages the arm against the current file to observe it.
  - **The design's disposal agent carries no `phase:` option.** All three surviving agents do
    (`:240`, `:302`, `:398`). Added, so the trace stays readable.
  - **`meta` is not in the design's edit set.** `description` at `:5` and the third `phases` entry at
    `:9` both say this program drives BUILD, and nothing grades either, so they would have stayed
    false on a green bar — which is the class this whole build exists to remove. Added as S5 and
    disclosed in §7 as ungraded.
  - **The install-prefix rise is 5 to 6 for a different reason than the design gives.** Measured with
    the checker's own `re_ship` predicate at `c4fcf5ad`: the five occurrences are `:42`, `:127`,
    `:279`, `:328` and `:499`. The design implies `:499`'s `gotchas.py` leaves with the prompt; it
    MOVES into `CHECKLIST` in `dispatch.args`, because the child spells zero `tools/` literals. Same
    number, different arithmetic, and the row's reason has to say which.
  - **This unit is NOT owner-gated, and the design marks it gated.** Its stated route is the
    `unattended` 1.17 to 1.18 bump reaching `SKILL.template.md`'s marker. `DEPL-aHoistedPass-1` at
    `order 2` takes that bump; `check-kit-versions.sh` grades presence and agreement with no branch
    reading a diff; and `VERBS.template.md`, the only `*.template.md` this unit touches, is not on
    the veto-2 list.
  - **`--paths` cannot be a top-loop flag.** The `--plan` arm exits inside the parse loop at `:4892`,
    so a later flag is unconsumed when it runs. It is read positionally, in the shape the `--phase`
    arm at `:4893-4897` already uses for `--witness`. The design does not say where it is parsed.
  - **`--dispatch` refuses more than "exactly two things about the unit's STATE".** Enumerated here
    from source: twenty `fail 49` sites plus `refuse_if_terminal`. Two of them grade the unit's spec,
    which is what the design's sentence is about; six more are about the unit, the run or an order
    verb, and thirteen are about the write set. Split into two tables in §4.
  - **`renderRoster` must survive for a reason the design does not give.** It is this file's only
    top-level definition and `map_lib.py:474-475` RAISES on a JS file yielding none, so deleting it
    reds `codebase-map coverage + freshness` rather than merely losing a helper.
  - **The three-sequential-nested-calls evidence is CARRIED, not measured here.** It comes from
    `wf_9b984206-816` in an earlier pass. The corrected comment says so, because a comment asserting
    a measurement this pass did not take is the defect one level down.
  - **The `review-harness` bump had no owner and now has one.** The design's edit set lists
    `tier2-review.js` moving 1.6 to 1.7 without assigning it to a unit. `TOOL-aHoistedPass-5`'s spec
    was read here at `order 4` and names no bump, so S12 takes it and §8 F1 records the coordination
    rather than leaving two units each assuming the other did it.
- rev-2 · 2026-09-05 · AC7's witness re-pointed. It asserted `dispatch.scriptPath` against a path
  literal that does not exist until `TOOL-aHoistedPass-5` lands at the preceding order, so the
  criterion read as a claim about a file rather than about this unit's dispatch. It now names the
  child by the unit that owns it and defers the literal to §4, which already spells it once in the
  dispatch block. This is also the more durable criterion: if the child's path moves, §4 moves with
  it and AC7 does not go stale. Nothing else in AC7 changed.
- rev-3 - 2026-09-05 - M3 fork sweep under the standing mandate: F1 marked RESOLVED at its
  recommendation, and `TOOL-aHoistedPass-5`'s rev-3 confirms it takes no bump. Premise re-derived at
  the run's BASE `e828f778`: `tools/workflows/unattended-build.js:784` is still ONE `agent()` call
  handed the whole roster, and that file's own header still states the shape at `:84`, so the hoist
  is still unbuilt 66 commits on.
- rev-4 - 2026-09-05 - three confirmed findings of the round-1 spec audit, folded. Finding 31 was the
  round's only BLOCKER and it is an address blocker: this spec was written against `c4fcf5ad`, the
  run's BASE is `e828f778`, and `tools/workflows/unattended-build.js` went from 531 lines to 835
  across those 66 commits. Every figure below was opened at BASE rather than carried.
  - **31 - every `unattended-build.js` address in section 4 re-derived.** rev-3's own sweep cited
    `:784` and `:84`, so it knew the file had moved and corrected the premise line only. Section 4
    still addressed `c4fcf5ad`, where S2's deletion span now holds the AUDIT stage: `:485` is
    `const res = await agent(`, the subjects resolver, and `:210-219` is schema prose. A builder
    following it literally would have deleted the audit and left BUILD standing. Old -> new: the
    BUILD agent `:485` -> `:784`, its options `:493` -> `:796`; `BUILD_SCHEMA` `:210-219` ->
    `:298-307`; the `if (!built)` refusal `:503-508` -> `:798-803`; `const unbuilt` `:509` -> `:804`;
    the disposal string `:473-482` -> `:686-695`; the `--dispatch` sites `:26-27` unmoved,
    `:56-57` -> `:85-86`, `:462-463` -> `:675-676`, `:495-497` -> `:758-760`; `renderRoster` `:138`
    -> `:226`, called `:147` -> `:235`, consumed `:232` -> `:375` and `:297` -> `:488`; `allIds`
    `:148` -> `:236`; the `CONVERGING` return `:441-457` -> `:648-670` and its `if` `:439` -> `:646`;
    the empty-`units` refusal `:118-124` -> `:182-188`; `gotchas.py` `:499` -> `:794`; `DRIVER`
    `:127` -> `:215`; the nesting comment `:276-277` -> `:467-468`; the refused-list schema rule
    `:154-157` -> `:242-245`; the three `phase:` options `:240`, `:302`, `:398` -> `:399`, `:493`,
    `:604`; the `ordered` sort `:128-133` -> `:216-221`; the three `specPath` reads `:70`, `:142`,
    `:298` -> `:130`, `:230`, `:489`; and in section 3, the `parallelism route: none` non-goal
    `:34-37` -> `:63-67`. `meta.description` `:5` and the third `phases` entry `:9` are unmoved, as
    is the header citation `:23-28`. Three `agent-cap.js` addresses moved too, that file having grown
    215 lines: `:1494-1499` -> `:1698-1699` (`guardAgentSpawn` now defined at `:1525`), `:1509` ->
    `:1710-1712`, `:1519` -> `:1722`; its rule blocks are still FOUR, counted at `:1725`, `:1745`,
    `:1766` and `:1797`, and `:9` still carries the sidechain sentence. Every other file this spec
    cites is byte-identical between `c4fcf5ad` and BASE, checked with `git diff --stat`:
    `unattended.sh`, `map_lib.py`, `check-kit-versions.sh`, `check-install-prefix.sh`,
    `check-workflow-syntax.js`, `check-unattended.sh`, `.unattended.conf`,
    `memory/map/features/unattended.md` and `VERBS.template.md`. Their citations stand unedited.
  - **31, continued - the corrected addresses changed what S2 deletes, which the finding warned they
    might.** Attended mode (`TOOL-aStagedLane-2`) landed INSIDE the BUILD stage after `c4fcf5ad`, so
    the stage is no longer an agent and a schema. S2 is restated BY NAME and section 4 gains a
    boundary table: the `label: 'build:'` agent, its prompt, the `if (!built)` refusal,
    `const unbuilt`, `BUILD_SCHEMA`, `const buildRoster`, `const driverSteps` and `phase('Build')`
    go; the attended `planState` refusal at `:718-750` and `skippedDone` do NOT, because they grade
    which units may be DISPATCHED and therefore belong to the hand-out. Two consequences rev-3 could
    not have seen. There is a FOURTH non-throwing exit — attended mode's every-unit-terminal return
    at `:766-782` — carrying no `roster` key, which is the identical defect rev-1 caught for
    `CONVERGING`; S4 is now four exits and AC6 grades both. And the section 4 return block was
    missing `mode` and `skippedTerminal`, which every return at BASE carries; dropping `mode` would
    have silently undone that unit's run-integrity field inside a diff about something else. A FIFTH
    `--dispatch` assertion site also exists, at `:44-46`, added with attended mode, so S3 now reads
    five sites and three survivors rather than four and two. One instruction is LOST rather than
    moved and section 4 says so: `driverSteps`' attended branch tells a pass to write down its paths
    before touching them, and that is a per-pass instruction the child owns, the child being a
    non-goal here.
  - **6 - AC2 was absence-only, and its pattern also missed a site it was written to cover.** S3
    specifies replacement TEXT for the surviving sites, and deleting them satisfies a grep returning
    `0` exactly as well as rewriting them does. AC2b is added as the positive half, asserting the
    successor text at all three survivors. Separately, run at BASE, rev-1's AC2 pattern returns four
    lines (`:26`, `:85`, `:758`, `:759`) and MISSES `:676`, whose wording is "out of the build's
    declared order" — so the STAGE 3 site could have been left standing on a green criterion. The
    alternative is added and the pattern re-run at BASE, where it now returns five.
  - **25 - S13 files the backlog rows section 4 already booked.** Files-touched carried
    `memory/backlog/TOOL.md` for "rows for the residuals in §5" while S1 through S12 filed none, so
    the edit set included a file the scope did not authorise and the two residuals the design refuses
    to fix in place had no durable home. S13 names three rows — the ungraded
    `gov:kit unattended-build@` marker, the ungraded `meta` pair, and the empty-`specPath` hand-out
    hazard — and AC24 asserts each exists.
  - **AC1, AC10 and AC15 re-pointed off spans and spellings, by the rule finding 31 states: cite by
    NAME, not by span.** AC15 ran `sed -n '276,277p'`, which at BASE prints
    `const SUBJECTS_SCHEMA = {`; it is now a grep for the comment's own text plus a file-wide
    `spent|budget` count, measured as `1` at BASE and owed `0` after. AC1 asserted four
    `= await agent\(` lines; that pattern returns TWO at BASE, because the spec fan spells
    `return agent(` and the round recorder `: await agent(` — it graded a spelling. It is now four
    `label:` greps naming the four surviving call sites. AC3's absence list gained `built`,
    `buildRoster` and `driverSteps`, all `const`s at BASE. AC10's anchor is restated as the
    pre-change tree, with the `c4fcf5ad` equivalence stated rather than assumed.
  - **What this rev did NOT verify.** Section 4's SUBSTANCE beyond its addresses is still unreviewed:
    the blocker stopped the round-1 audit before it got there, and this rev re-derived addresses
    rather than re-arguing the design. The install-prefix figure was MEASURED, not predicted —
    `bash tools/check-install-prefix.sh --list` reports `5` for this file at BASE, at `:71`, `:215`,
    `:457`, `:519` and `:794` — so the 5-to-6 rise stands on the same arithmetic with re-derived
    sites. Neither suite was run; no arm was staged. `TOOL-aHoistedPass-2`'s narrowing of the
    identical `pass-order history` claim is deliberately untouched here: this spec NARROWS at
    `:26-27` and the sibling is being corrected to match, so the wording is kept quotable rather than
    converted to a strike. Nothing outside this spec file was edited, and nothing was committed.
- rev-5 - 2026-09-05 - the other half of rev-4's fold, caught by the bug-class checklist over that
  commit: `amendment-leaves-its-other-half-standing`. Three passages named `TOOL-aHoistedPass-2` at
  `order 3` as the owner of the `unattended` 1.17-to-1.18 bump this unit lands inside. Section 8's
  fork sweep had already moved that move to `DEPL-aHoistedPass-1` at `order 2` and stood the sibling
  down, and rev-4's fold brief never told the pass so. Owner and order corrected in all three. The
  CONCLUSION each passage draws is untouched and still holds: this unit is NOT owner-gated, because
  it owes no bump and `VERBS.template.md`, the only `*.template.md` it touches, is not on the veto-2
  list.

- rev-6 - 2026-09-05 - folded round-2 spec-audit findings H8 and H10, before any code. **H8** -
  section 4's KEEP row said `buildUnits` "becomes the roster filter" and its normative return block
  spelled `roster: ordered.map(...)`; the two cannot both be implemented whenever attended mode has
  some-but-not-all terminal units, and written as the block spelled it the refusal S2 deliberately
  KEEPS filters nothing. That is the defect the live comment above `buildUnits` already records - the
  BUILD agent handed the UNFILTERED roster - reproduced one layer over in a per-unit dispatch loop.
  The block now maps `buildUnits`, `units:` is stated to count `ordered` on purpose, and AC25 grades
  the difference, which no existing criterion could: AC7 grades order sequence and AC8 grades
  `dispatch.args` keys. **H10** - section 3's third non-goal said `TOOL-aHoistedPass-1` "owns that
  correction by name", and that spec's section 3 says in bold that NO unit of this build takes any of
  the carriers. Two specs disclaiming to each other left the cheapest carrier owned by nobody, with
  nothing on the bar grading a decision quotation's truth. Rewritten to the BASE fact, with the
  option of taking the correction here considered and REFUSED in writing: `TOOL-aHoistedPass-1` has
  now FILED the residual as a row asserting that no unit of this build edits one, and falsifying a
  landed backlog row to save a follow-up is the drift this build exists to end.

- rev-7 - 2026-09-05 - the build pass. Four divergences from rev-6, and the first three were found
  while implementing rather than before it, so this line is folded in the SAME commit as the code
  rather than ahead of it. Saying that plainly is cheaper than implying an ordering the git history
  would contradict.
  - **Exit four's `note` composes a prefix the section 4 table does not carry.** The table gives it
    as `prologue complete; N unit(s) to dispatch` flat. The file's own `degradation-known-but-
    unreported` rule and a LIVE arm in `unattended-build.test.sh` both require a run that refused
    specs, or reached a non-CONVERGED verdict, or ran ATTENDED, to say so on the return — so the
    note is that clause, then ` · `, then the table's sentence. Dropping the clause to match the
    table literally would have deleted a working arm and re-opened the class the file spends four
    comment lines on. AC7's `prologue complete` grep is unaffected either way.
  - **The deleted schema's tombstone comment does not spell its identifier.** AC3 grades
    `grep -c "BUILD_SCHEMA"` at `0`, unanchored, which is the stronger criterion — it also catches a
    stale `schema:` option still pointing at the gone constant — and the file's house style for a
    removed schema is a named tombstone (`AUDIT_SCHEMA` above). The two collide. The criterion won
    and the tombstone says so in its own words, because an anchored grep would have bought a
    prettier comment at the cost of the arm that matters.
  - **Two test arms were retired rather than re-pointed, and section 4's LOST-instruction paragraph
    is why.** `attended prompt: the per-unit build instruction SURVIVES` and the arm reading
    `recording verbs are unavailable` out of the BUILD prompt both graded `driverSteps`, which S2
    deletes. The first is now the child's property and has no witness here at all; the second is
    re-pointed at `GROUND`, where the attended honesty sentence actually lives and which every stage
    still carries. A third arm, `AC5 failed disposal: the standing blocker is NAMED`, was written as
    a bare grep for `b1` and observed GREEN against the unchanged source — the fixture's own
    `"briefPath":"b1"` satisfied it — so it was tightened to assert the note's text before the source
    change landed.
  - **`--dispatch` REFUSED `memory/backlog/TOOL.md`, so S13's own scope item is undeclared.** Check
    49: a path overlapping a declared `SHARED_RECORDS` entry, `memory/backlog/TOOL.md` against
    `memory/backlog`. Observed rather than predicted — the declaration was run WITH the path first
    and refused, then re-run without it. The refusal is about a DISJOINTNESS claim between concurrent
    passes and this pass is sequential and alone, so no declaration can ever carry the path; the
    residual, that a unit whose scope files a backlog row has a write no dispatch row records, is
    parked in `RUN.md`. `TOOL-aHoistedPass-4` took the same route at `4c255e61` earlier in this run.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py "return an ordered unit roster from a workflow harness and emit spec paths from the planning verb"`
against a corpus of 645 symbols, 188 inventory keys, 19 affordance seams and 20 dossiers. It surfaced
`renderRoster` (`tools/workflows/unattended-build.js`, fan-in 0), `rosters` and `parse_spec`
(`tools/memory-tree/gen_build_index.py`), and the declared seam `.unattended.conf` in
`memory/map/features/unattended.md:209`. Verdict, in the sanctioned words: **no existing seam fits.**
`.unattended.conf` is the project DECLARATION surface and carries no output shape; `rosters` renders
the README region this verb READS rather than emitting rows from it; `renderRoster` builds the
human-prose block the SPEC and blob-resolver prompts consume and is kept unchanged for that reason
plus the `map_lib.py:474-475` raise. What this unit extends is not a declared seam but two existing
in-file shapes reused verbatim: `verb_plan`'s three padded `printf` sites collapse into one
`plan_row` helper the way `order_verb_of` already collapsed a duplicated reader, and the `--paths`
flag is parsed in the same positional shape the `--phase` arm at `unattended.sh:4893-4897` uses for
`--witness`. No new primitive is added.

Recall terms used: unattended-build harness, roster hand-out, dispatch order gate, verb_plan,
plan_state, --plan --paths, brief row, run-state park, DISPOSAL stage, BUILD-METHOD M4, agent-cap
slot ledger, workflow nesting depth, install-prefix carried, kit version markers
