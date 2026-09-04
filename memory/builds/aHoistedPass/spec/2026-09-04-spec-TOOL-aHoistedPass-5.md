# TOOL-aHoistedPass-5 — the child that builds one unit and holds nothing else

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-aHoistedPass-1-design-pass.md](../build/2026-09-04-build-aHoistedPass-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

<!-- /gen:spec-records -->

## 1. Goal

Land `tools/workflows/unattended-unit.js`, a workflow script that builds exactly ONE unit of an
unattended build, oriented in that unit's spec and that unit's brief and never in the roster. Under
the hoist the parent program ends after DISPOSAL and returns the ordered roster, and the run makes
one main-loop `Workflow` call per unit against this file; without the file there is nothing to
dispatch and the hoist has no callee.

## 2. Scope (IN)

- **S1** — the file at `tools/workflows/unattended-unit.js`, taken from the candidate at
  `scratchpad/unattended-unit.candidate.js` (measured at this base: 110 lines, 6933 bytes), with the
  corrections S6 and S8 below.
- **S2** — the args contract. `repo`, `slug`, `unitId`, `specPath`, `briefPath`, `driver`, `ground`
  and `checklist` are each refused by name with a reason, after a `JSON.parse` guard for the case
  where the caller hands the tool a string.
- **S3** — exactly one `agent()` call, under `UNIT_SCHEMA`, whose required keys are `committed`,
  `sha`, `why` and `summary`. `why` is required on both outcomes, so an empty result carries a
  reason rather than being indistinguishable from a clean pass over nothing.
- **S4** — the prompt. Read the brief and the spec whole before touching code; change the spec first
  where the build must diverge; declare the write set with `--dispatch … --writes`; record the brief
  with `--brief`; commit; run the checklist command and act on what it names.
- **S5** — the status flip, in the prompt: set this unit's spec status header to `CLOSED`, or to
  `WONTDO` with a reason, IN THE SAME COMMIT as the code. §4 states why this is load-bearing.
- **S6** — exactly ONE top-level definition, so the `kit-js` symbol layer has a symbol to index. This
  is a correction to the design of record and it is measured in §4; the fork it opens is F1.
- **S7** — the map claim. `"unattended-unit.js"` joins `workflow-scripts` in
  `memory/map/features/unattended.md`, and `python tools/codebase-map/gen_map.py --write` re-runs in
  the same commit so the generated artifacts land with the claim.
- **S8** — the file header rewritten so that every property it declares names what actually holds it,
  in the words §4's inventory settles on. The candidate's header is already close; two of its claims
  are corrected by measurement here.

## 3. Non-goals (OUT)

- The parent. Deleting the BUILD `agent()`, the roster return, `resolvePathsWith`, `--plan --paths`
  and the order-gate arm belong to the parent-and-driver unit (design U5). This unit adds a callee and
  changes nothing that calls it.
- Any Skill, protocol or BUILD-METHOD edit. The dispatch loop, the `scriptPath` pin, the per-dispatch
  re-read step and the four `next:` branches are `TOOL-aHoistedPass-2`'s; this file is named by them,
  never the other way round.
- Widening the fan-out predicate. The two loop spellings that walk past it are
  `TOOL-aHoistedPass-4`; this unit takes `agent-cap.js` exactly as it stands at `c4fcf5ad`.
- Teaching the codebase-map JS liveness floor about the export scan. That is F1 option (b) and it is
  not taken here; it is a backlog row if the fork is ever reopened.
- Concurrent dispatch of an `order` group. M6 will name the permission; nothing in this file or in
  this build implements it.
- A new govkit kit id for this file. It ships inside the `review-harness` kit's home
  (`tools/workflows/kit.toml` declares `include = "**"`, role `engine`) and needs no entry of its own.

## 4. Design

### Data model

`args` arrives as an object or as a JSON string. Eight keys, all required, none defaulted:

| key | what it carries | why it is not defaulted |
|---|---|---|
| `repo` | the build root | defaulting it to the process cwd is how a sibling harness reviewed the wrong repository |
| `slug` | the build slug | every driver verb in the prompt is slug-addressed |
| `unitId` | the one unit | this script builds one unit and cannot pick it |
| `specPath` | that unit's spec | a unit built without its spec is the defect the harness exists to close |
| `briefPath` | that unit's brief | the brief is the only carrier the driver hashes |
| `driver` | the driver invocation, spelled by the caller | so this file spells no install path |
| `ground` | the grounding preamble the parent built | the child does not re-derive grounding |
| `checklist` | the per-pass bug-class command | owed after every commit, and a sidechain agent does not inherit the unattended Skill |

The return is `{committed, sha, why, summary}`, coerced from the agent's result so a missing field
becomes an empty string rather than `undefined`.

**No `roster` field, and no `reportPath`.** The child never receives the roster: the parent holds it
and holds the order. Anything a unit must know beyond its spec goes into its BRIEF file, because that
is the only carrier `--brief` hashes — it refuses an untracked path and hashes with `git hash-object`.
Nothing hashes a prompt string.

### Inventory — every declared property, and what actually holds it

Measured at `c4fcf5ad` in this worktree. Every fixture is the candidate plus one appended construct,
dispatched by `scriptPath` in Windows form to `node tools/hooks/agent-cap.js`, exit codes captured by
redirecting to a file rather than through a pipe.

| declared property | what holds it | measured |
|---|---|---|
| a BARE top-level script, never `export default` | **`workflow script syntax`**, on every bar | the candidate → exit 0, `1 workflow script(s) parsed clean`; the same file rewritten as `export default async function run()` → **exit 1**, `SyntaxError: Unexpected token 'export'` |
| no spawn once per item — as a loop, or as an array-method receiver | **`agent-cap.js:1521`, per dispatch** | `for (const u of cfg.units) { await agent(…) }` → **exit 2**; `await Promise.all(cfg.units.map((u) => agent(…)))` → **exit 2**; `cfg.units.map((u) => agent(…))` alone → **exit 2** |
| no raw `parallel(` / `pipeline(` | **`agent-cap.js:1562`, per dispatch** | `await parallel([agent(…), agent(…)])` → **exit 2** |
| it spells no `tools/` literal | **`install-prefix (shipped surface)`**, on every bar, once the file is TRACKED | clean child staged → exit 0, `181 shipped files` (180 without it); the same file plus one `bash tools/unattended/unattended.sh` literal → **exit 1**, `UNRECORDED  tools/workflows/unattended-unit.js	1` |
| at least one top-level definition | **`codebase-map coverage + freshness`**, on every bar | see the next sub-head — the candidate as written REDS this leg |
| a plain loop, a `function`, a `=>`, a non-receiver `.map()`, a bare `Promise.all` | **NOTHING. A file-style rule with no gate.** | all five fixtures → **exit 0** |
| exactly ONE `agent()` | **NOTHING.** The run holds it. | a second `agent()` with an unrelated prompt → **exit 0** |
| it never NESTS | **NOTHING.** The run holds it. | `await workflow({scriptPath: …}, {})` appended → **exit 0**; and `grep -c "workflow(" tools/hooks/agent-cap.js` = **0**, so the hook contains no occurrence of the nesting call form at all. A nested call fired from inside this sidechain reaches no hook either (`agent-cap.js:9`) |
| `export const meta` is present | **NOTHING. It SELECTS.** | deleting the declaration line drops the file out of BOTH marker-keyed legs at exit 0: `workflow script syntax` and `verifier fan-out` each report **4** scripts instead of 5. `check-review-join.sh:102-103` selects on path alone with no marker filter, so `review-join ban` keeps the file either way |
| the prompt's content, between dispatches | **NOTHING.** The run holds it. | the second-`agent()` and rewritten-prompt fixtures both admit |

Two of the nine rows are the whole of what the per-dispatch re-read buys, and they are ONE rule plus
one: `fanoutFindings` at `:1521` catches a spawn once per item however it is spelled — a loop or an
array-method receiver — and `offendingLines` at `:1562` catches the raw primitive. A loop with no
spawn inside admits (**exit 0**, measured), so "no loop" is not the rule; "no spawn per item" is.
Rules 2 and 5 (`:1541` an unresolvable bound, `:1593` the ref-keyed verdict join) are in the same
scan and this file trips neither.

### The correction the design of record missed: the `kit-js` liveness floor

The design names `workflow script syntax` and `verifier fan-out` as this unit's boundaries. A third
unguarded leg runs on every bar and REDS on the candidate as written.

`map_extractors.py:213` walks `tools/` with `map_lib.scan_js_definitions`, whose three rules
(`map_lib.py:405-415`) recognise `function <id>`, `class <id>`, and `const|let|var <id> =` bound to a
function or an arrow. The candidate has none of the three: every occurrence of `function`, `=>` and
`Promise` in it sits inside a `//` comment, which the scanner strips. A file yielding zero symbols
raises rather than indexing less — `map_lib.py:474`:

> `kit-js: tools/workflows/unattended-unit.js yielded NO definition. A JS file with no top-level
> function or class is either not what this layer is for, or a form these rules forgot — raising
> rather than indexing less, which is how this layer went 30-to-3 unseen`

Observed: with the candidate copied to its real path, `python3 tools/codebase-map/test_codebase_map.py`
exits 1 on that `MapError` traceback. The floor is deliberate and fail-closed, and it is a LIVENESS
assertion of exactly the kind §7 of the charter demands, so it is not a bug to route around.

**S6 is the resolution: one top-level definition.** The candidate spends eight near-identical lines on
`if (!cfg.<key>) throw new Error(…)`; one `function need(key, why)` replaces the seven that share a
shape, satisfies rule 1 of `JS_DEFINITION_RULES`, and makes the file shorter. Observed with that one
function added: the `MapError` is gone and the leg reports only its two ordinary obligations — the
unclaimed key and the stale generated artifacts. With `"unattended-unit.js"` added to
`workflow-scripts` in `memory/map/features/unattended.md` (which already claims `unattended-build.js`)
and `gen_map.py --write` re-run, the leg exits **0**, all five of its tests `ok`.

The cost is one clause of a style rule that nothing enforces: the file may no longer claim it holds no
`function`. `function` ADMITS at the hook (measured, exit 0), so nothing about fan-out changes. F1
records the alternative and why it was not taken.

### The status flip, and why it is load-bearing

`unattended.sh:2144` is the only thing that removes a unit from `next` candidacy:

```sh
case "$st" in CLOSED|WONTDO) [ "$state" = "READY" ] && state="DONE" || state="DONE ($state)" ;; esac
```

`$st` is the spec's status header. The candidacy branch immediately below (`:2147-2150`) sets `next`
only for a state of exactly `THIN`, `FORKED` or `READY`, and the flip above rewrites all three to
`DONE …`, which matches none of them. Under the hoist the run reads `--plan <slug> --paths` between
dispatches, so a child that commits code without flipping the header leaves `--plan` naming the same
unit `READY - build it` forever, and the run's own loop counter never advances. `--plan` reads the
INDEX (`unattended.sh:2043`, `git ls-files "$dir/spec/*.md"`), so the flip must be STAGED in the same
commit, not merely written.

The same flip is load-bearing a second time downstream: `build-complete`'s non-terminal term at
`--close` (`unattended.sh:3353`) refuses a build any of whose units is neither `CLOSED` nor `WONTDO`,
and that term is the ONE thing catching an incomplete loop. Its only exit is a recorded
`--override build-complete`.

**No other carrier instructs the act.** The prompt is where it is instructed, and nothing enforces it:
`--dispatch` does not require it, `--brief` does not, and `pass-order history` grades only units that
already reached `CLOSED`. The run holds it until `--close`, where the refusal is overridable.

### What the prompt may and may not say about `--dispatch`

The prompt tells the agent to declare its write set and that a refusal is binding, and then states the
verb's reach honestly, because the parent's own BUILD prompt shipped the opposite claim:

- `unattended.sh:4604` refuses a unit no tracked spec under this build defines.
- `:4609` refuses a unit whose spec grades `THIN`, and that is the only arm in its `case`.
- The order gate runs only `if [ -n "$_d_ord" ]` (`:4630`) and skips any sibling with no verb
  (`:4639`), so it is available only where BOTH units carry an `order` verb.
- A sibling carrying a dispatch row stops blocking whether or not it was ever built (`:4647`), and
  `--dispatch` writes that row itself.

So the prompt says its silence is not a clearance, and that order is the parent roster this child was
dispatched from rather than something the verb proves. `grep -c "THAT DISPATCH IS THE ORDER GATE"` over
this file must stay **0**.

### The version marker, stated for what it is

`meta.version` carries `// gov:kit unattended-unit@1.0`, matching the sibling
`unattended-build.js:3`. No branch of `check-kit-versions.sh` reads that id — its kit ids are a
hard-coded list (`tier2-review`, `review-harness`, `agent-cap`, `run-gates`, `settings-merge`,
`memory-tree`, `unattended`) — so the marker is documentation and not a graded contract. Matching the
sibling beats inventing a third convention; the comment beside it says so rather than implying a
versioning contract the file does not have.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/workflows/unattended-unit.js` | NEW, ~110 lines |
| `memory/map/features/unattended.md` | one key added to `workflow-scripts` |
| `memory/map/generated/inventories.json` · `symbols.json` · `MAP.md` | regenerated, never hand-edited |

### Alternatives rejected

- **Put the loop back in the child.** A workflow script has no filesystem, cannot re-read `--plan` and
  cannot verify a commit, and a `workflow()` call fired from inside a sidechain runs no hook at all
  (`agent-cap.js:9`). The loop belongs to the run.
- **Hand the child the roster so it can check its own order.** The order it would check is the order it
  was handed; the parent holds both.
- **Dispatch by `name:` instead of `scriptPath`.** Measured: `{tool_name:'Workflow',
  tool_input:{name:'somewf'}}` → exit 0 with nothing read (`agent-cap.js:1519`). Every rule in the
  inventory above evaporates. The pin is `TOOL-aHoistedPass-2`'s to write.
- **Teach the codebase-map floor about the export scan.** F1 option (b); see §8.

## 5. Production-readiness checklist

- **security** — the child spawns one agent with a prompt built from `args`. It writes no file itself,
  holds no credential, and spells no path; §9 of the charter's write-boundary rules do not apply. The
  agent it spawns has the run's own authority, which nothing here bounds and §10 of the design says so.
- **perf / scale** — one `agent()` per dispatch. N units cost N main-loop returns; the keepalive is
  time-keyed so the returns cost it nothing. Whether N returns raise the stall rate is UNVERIFIED in
  either direction and this unit asserts nothing about it.
- **a11y** — N/A: no user interface.
- **i18n** — N/A: agent-facing English, same as every sibling harness.
- **error / empty / loading states** — eight named arg refusals plus the parse guard; `why` required on
  both outcomes so `committed:false` always carries a reason.
- **observability** — one `log()` line naming the unit, the commit flag and the sha. The run's own
  `dispatch` and `brief` rows are the durable witness and they are written by the driver, not here.
- **risks** — the loop-advance risk is the status flip (§4): a child that commits without it stalls the
  run's counter. It is instructed and not enforced, and `build-complete` is the only downstream catch.
  No concurrency risk: one dispatch at a time, and this unit builds no parallel path.
- **testing + left-shift gates** — three standing legs already cover the file the day it lands
  (`workflow script syntax`, `verifier fan-out`, `review-join ban`), plus
  `codebase-map coverage + freshness` and `install-prefix (shipped surface)`. This unit adds NO new
  gate; §6 names the breaks to stage against the ones it joins.
- **migration / rollback** — additive. Deleting the file restores the tree, minus the map claim and the
  regenerated artifacts, which come out in the same commit.
- **user docs** — none. The file is agent-facing and reached only by a `Workflow` dispatch; the route
  a reader follows to it is `TOOL-aHoistedPass-2`'s M6 sentence.

## 6. Acceptance criteria

- **AC1** — When `node tools/workflows/check-workflow-syntax.js` runs in discovery mode with the file
  landed, it exits 0 and reports `5 workflow script(s) parsed clean`, one more than the `4` measured at
  this base. The count is the membership assertion; the exit code alone is not, because the marker
  SELECTS the population.
- **AC2** — When the same file is rewritten to `export default async function run()` and handed to
  `node tools/workflows/check-workflow-syntax.js` explicitly, it exits **1** with
  `SyntaxError: Unexpected token 'export'`. Staged, observed, unstaged — this is the shape the bare
  top-level rule exists to exclude, and it has been observed RED at this base.
- **AC3** — When `bash tools/workflows/check-verifier-fanout.sh` runs in discovery mode, it exits 0 and
  reports `5 workflow script(s)`, and the same population re-derived by hand —
  `git ls-files --cached --others --exclude-standard -- '*.js'` filtered by
  `grep -qE '^[[:space:]]*export[[:space:]]+const[[:space:]]+meta[[:space:]]*='` — CONTAINS
  `tools/workflows/unattended-unit.js`.
- **AC4** — When the candidate plus `for (const u of cfg.units) { await agent(…) }` is fed to
  `node tools/hooks/agent-cap.js` by `scriptPath`, it exits **2** naming
  `a verify/fan-out stage spawns one agent per item`; when the pristine file is fed the same way it
  exits **0**. Both observed at this base, exit codes captured without a pipe.
- **AC5** — When `python3 tools/codebase-map/test_codebase_map.py` runs with the file landed, its
  claim in `memory/map/features/unattended.md` present and `gen_map.py --write` re-run in the same
  commit, it exits 0 with all five tests `ok`.
- **AC6** — When the file is staged WITHOUT its top-level definition, the same leg exits **1** on
  `map_lib.MapError: kit-js: tools/workflows/unattended-unit.js yielded NO definition`. Staged,
  observed, unstaged — already observed once at this base, and it is the reason S6 exists.
- **AC7** — When the file is staged and `bash tools/check-install-prefix.sh` runs, it exits 0 and
  reports `181 shipped files`, up from the `180` measured at this base; when one
  `bash tools/unattended/unattended.sh` literal is appended to the staged file, the same command exits
  **1** with `UNRECORDED  tools/workflows/unattended-unit.js`. Both observed; the break is unstaged
  before landing.
- **AC8** — When `grep -c 'tools/' tools/workflows/unattended-unit.js` runs, it prints `0`, and
  `memory/project/method-carriers.txt` gains no row, because the file names neither an install path nor
  `BUILD-METHOD.md`.
- **AC9** — When the landed file is scanned with its `//` comment lines removed, it holds exactly one
  `agent(` and zero `workflow(`, and
  `grep -cE '^[[:space:]]*export[[:space:]]+const[[:space:]]+meta[[:space:]]*=' tools/workflows/unattended-unit.js`
  prints `1`. A bare `grep -c 'export const meta'` prints `3` on this file and means nothing, because
  two of the three occurrences are the header comments about the marker.
- **AC10** — When the landed file's prompt string is read, it names the `CLOSED` / `WONTDO` flip AND
  the same-commit requirement AND `--plan` as the reader that acts on it, and
  `grep -c 'THAT DISPATCH IS THE ORDER GATE' tools/workflows/unattended-unit.js` prints `0`.
- **AC11** — When the landed file's args are read, there is no `roster` key and no `reportPath` key,
  and `UNIT_SCHEMA.required` is exactly `committed`, `sha`, `why`, `summary`.
- **AC12** — When `bash tools/workflows/check-review-join.sh` runs with the file landed, it exits 0.
  This leg selects by PATH (`check-review-join.sh:102-103`, no marker filter), so unlike AC1 and AC3
  its coverage of this file does not depend on `export const meta` surviving.
- **AC13** — When the file's own header is read after S8, no sentence claims an enforcer the inventory
  in §4 does not name, and the `function` clause is gone. The header's `export const meta` paragraph
  states that the marker SELECTS and does not require.

## 7. Gates

Legs this unit must keep green, all read from `tools/gate-legs.json` at this base:

- `workflow script syntax` — chunk `wiring`, subject `repo`, no guard. Every bar.
- `verifier fan-out` — chunk `declarations`, subject `repo`, no guard. Every bar.
- `review-join ban (no ref-keyed join)` — declared in `tools/workflows/kit.toml`, `guard = []`. Every bar.
- `codebase-map coverage + freshness` — chunk `declarations`, subject `repo`, no guard. Every bar, and
  the one this unit's shape actually collides with.
- `install-prefix (shipped surface)` — every bar, once the file is tracked.
- `govkit selfcheck` — every bar. Observed exit 0 at this base with the file staged; the new file needs
  no descriptor because `tools/workflows/kit.toml` declares `include = "**"`.
- `memory hygiene` — every bar, for this spec and the acceptance ledger it later answers.

**This unit adds no gate.** Five legs already cover the file the day it lands, and three of the file's
declared properties are covered by none of them, which §4 states and §8 does not pretend away.

## 8. Open questions

**F1 — who yields to the `kit-js` liveness floor: the child, or the floor?** The candidate declares no
top-level `function` and no `=>`; `map_lib.py:474` raises on any `.js` under `tools/` yielding no
definition, and `codebase-map coverage + freshness` runs unguarded on every bar. Both constraints are
real and they are incompatible as written.

- **(a) The child yields.** One top-level `function need(key, why)` replaces seven near-identical
  argument refusals. Cost: one clause of a five-clause style rule that nothing enforces, and the file
  header stops claiming it. Benefit: no edit to another kit, no widening of a fail-closed floor, and
  the file gets shorter. Measured green end to end at this base.
- **(b) The floor yields.** `_build_js_layer` (`map_extractors.py:198-218`) already unions
  `enumerate_exports` with `scan_js_definitions`, and the child IS covered by the export scan through
  `export const meta`. Moving the per-file liveness assertion up to the union — the shape `_live_py`
  already uses for the Python layer — would stop calling a definition-free workflow script a hole. Cost:
  an edit to a fail-closed floor in the codebase-map kit, its self-test arms, its version bump, and a
  weakened floor for every future JS file that genuinely IS a hole.

**Recommendation: (a).** The floor is a liveness assertion doing exactly its job, and the thing it
collides with is the one clause of the child's style rule with neither an enforcer nor a consumer.
Widening a fail-closed check so a style preference can survive is the trade this build exists to stop
making. If the owner prefers (b), it is a separate unit against the codebase-map kit and this unit
lands unchanged behind it.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, written against `origin/main` = `c4fcf5ad` with every line number
  re-opened locally and every exit code re-measured in this worktree. Five corrections to the design of
  record, `build/2026-09-04-build-aHoistedPass-1-design-pass.md`:
  1. **The design names two boundaries for this unit and there are five.** It lists `workflow script
     syntax` and `verifier fan-out`; measured, the file also lands on `review-join ban (no ref-keyed
     join)` (by PATH, not by marker), `install-prefix (shipped surface)` (once tracked), and
     `codebase-map coverage + freshness`.
  2. **The candidate REDS `codebase-map coverage + freshness` as written.** `map_lib.py:474` raises
     `MapError` on a `.js` under `tools/` yielding no top-level definition, and the candidate has none.
     Not mentioned anywhere in the design. S6 and F1 are the response.
  3. **"No loop" is not the rule the hook enforces.** The design and the candidate header both read as
     if a loop is denied. Measured: a loop with NO spawn inside admits at exit 0, and a `.map()` whose
     callback spawns is denied — so the rule at `:1521` is "no spawn once per item", spelled as a loop
     or as an array-method receiver, and the two are one rule rather than two.
  4. **The "spells no paths" property HAS an enforcer.** The design records only that it owes no
     install-prefix row and no `method-carriers.txt` row. Measured with the file tracked: an appended
     `bash tools/unattended/unattended.sh` literal reds `check-install-prefix.sh` at exit 1 naming the
     file. That moves the property out of the un-held column.
  5. **`gov:kit unattended-unit@1.0` names an id no gate reads.** `check-kit-versions.sh` grades a
     hard-coded list of kit ids and `unattended-unit` is not on it. The marker stays, matching
     `unattended-build.js:3`, and §4 says plainly that it is documentation rather than a graded
     contract instead of leaving a reader to infer one.

  Design citations re-opened and CONFIRMED unchanged: `agent-cap.js:403`, `:1494`, `:1509`, `:1519`,
  `:1521`, `:1541`, `:1562`, `:1593`, `:9`; `unattended.sh:2043`, `:2144`, `:3353`, `:4604`, `:4609`,
  `:4630`, `:4639`, `:4647`; `check-workflow-syntax.js:30` and `:72`; `check-verifier-fanout.sh:86`;
  `grep -c "workflow(" tools/hooks/agent-cap.js` = 0; the candidate at 110 lines / 6933 bytes with the
  `export const meta` declaration at `:30`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a workflow script that spawns one agent to build a single
build unit from its spec and brief"` — exit 0 over a corpus of 645 symbols, 188 inventory keys, 19
affordance seams and 20 dossiers. The seam this unit extends is the **`workflow-scripts` inventory
under `memory/map/features/unattended.md`**, which the shortlist surfaced as
`check-workflow-syntax.js [workflow-scripts]` and which already claims `unattended-build.js`; the
sibling this file is modelled on is `tools/workflows/unattended-build.js` (the args-parse guard, the
schema shape and the `meta` block are ported from it rather than re-invented). No new abstraction is
introduced: the file is one more member of an existing declared population, selected by the marker two
gates already read, and its dispatch contract is the same `scriptPath` shape `tier2-review.js` uses.
The probe surfaced no helper this unit should route through instead — `guardAgentSpawn`
(`tools/hooks/agent-cap.js`, fan-in 0) is the hook's own entrypoint and is not callable from a workflow
script, and the `build_*` cluster it ranked highest is name-stem noise from `build` rather than a seam.

Recall terms used: unattended-unit, workflow script, scriptPath dispatch, agent-cap, fan-out receiver,
export const meta selector, sidechain, unit spec brief, status flip CLOSED WONTDO, --plan next
candidacy, --dispatch write set, kit-js liveness floor, workflow-scripts inventory, roster hand-off.
