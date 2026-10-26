# TOOL-dBoundRoles-22 — workflow entries as data: ordered stages, each naming its role, fan, cap, effort and rows, every cap under the agent limit

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 5 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0187@5afc67cc whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-c.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-16 TOOL-dBoundRoles-21 TOOL-dBoundRoles-25 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

Declare each workflow entry's stages as ordered rows, every stage naming its role, its fan, its cap,
its effort and the rows it receives and returns, so one agent, a parallel set, several steps, mixed
roles and variable caps are all data, and every cap sits at or under the repository's agent limit
(night pass two, point 1, the owner's NT-8). Today a stage is an unordered `key → slot` pair
(`tools/roles/workflows.toml:37`, `:47`, `:57`, `:67`) and its fan and cap are literals inside each
harness.

## 2. Scope (IN)

- **S1** — The stage rows: every `workflow`-driver entry of `tools/roles/workflows.toml` carries ordered
  `[[workflow.stages]]` tables in place of its inline `stages` map, each with `key`, `role`, `fan`,
  `cap`, `effort`, `receives` and `returns`, per §4 "### The row". The table keeps the name `stages`, so
  it never trips TOOL-dDeclaredLoop-1's `stage` grep. Observed by AC1.
- **S2** — One reader of the rows, `load_workflows` (`tools/roles/roles_lib.py:339`), returning each
  entry's stages as a list of row dicts in file order, and one derivation, `derive_stage_map(entry)`,
  the ordered `{key: role}` map every former reader of the inline table now reads: `print_harness_args`
  (`tools/roles/handoff.py:453`), so the map `harness-args` prints is derived from the rows; R9
  (`tools/roles/check_roles.py:297-310`); R12's stage-key check (`tools/roles/roles_lib.py:430-451`);
  the catalogue region's `stages` cell (`tools/roles/check_roles.py:121-141`); and `extract_field`'s stage
  half (TOOL-dBoundRoles-14 S3), which reads each row's `key`. Observed by AC1 and AC2.
- **S3** — The stage's declared effort placed in the order TOOL-dBoundRoles-21 sets:
  `resolve_stage_efforts` reads a row's `effort` after the three keys and the house file, before the
  role's declared `effort`, per §4 "### The effort". Observed by AC3.
- **S4** — R9 widened over the rows: a `key` outside `STAGE_KEY_RE` or repeated in its entry; a `role`
  the entry's `roles` does not list or that is `agent: false`; a `fan` or `cap` that is not an integer
  of at least 1; an `effort` outside `EFFORT_LEVELS`; a `receives` or `returns` entry outside the row
  kinds of TOOL-dDeclaredLoop-29 S3; and a `cap` above the repository's agent limit, each one R9 line
  naming the entry and the stage. Observed by AC4 and AC5.
- **S5** — The agent limit read once per run, `read_agent_limit(root)` in `roles_lib.py`: the resolved
  value of `runtime.agents-in-flight` (TOOL-dGroundRules-10, catalogue default 6) through the same
  `resolve` import TOOL-dBoundRoles-21 S1 makes, whatever its source. With no policy kit found the cap
  arm prints `unarmed` once and grades nothing, never green. Observed by AC5.
- **S6** — Gov's four workflow-driver entries rewritten as rows, per §4 "### Gov's rows", each value
  the harness literal or resolved level it states at base, so no harness call changes in this unit.
  Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- The five kinds as named defaults over the rows, the checklist, the orientation template, the merge,
  the twin rule and the experiment kind: TOOL-dBoundRoles-16's, over these rows (§8 F1).
- A scenario's workflow entries and role rows composed per build: TOOL-dBoundRoles-20 composes the
  `workflow` and `role` rows a repository's overlay or a scenario activates, through
  PLAY-dOrderedCharter-35's `compose_rows`, and `load_workflows` returns that composition (§8 F2).
- Harnesses reading `fan` and `cap` from the rows: the harness literals (`MAX_VERIFIERS` at
  `tools/workflows/tier2-review.js:1352`, `SPEC_WRITERS` at `tools/workflows/unattended-build.js:942`)
  stay until TOOL-dBoundRoles-16 binds the shapes to the calls.
- Teaching TOOL-dDeclaredLoop-6 S8's `new workflow` factory the row keys: an ask this writer names for
  the main loop to file in dDeclaredLoop's backlog.
- The integer `stage` key's move out of `workflows.toml`: TOOL-dDeclaredLoop-1 S4's.

### Edges

- **consumes-from** `TOOL-dBoundRoles-14` — `field.<family>.<name>`, whose `field.stage.<seg>` half the extractor now reads from each row's `key`
- **consumes-from** `TOOL-dBoundRoles-21` — `resolve_stage_efforts`, the order a row's declared effort takes its place in
- **consumes-from** external — TOOL-dGroundRules-10's `runtime.agents-in-flight` and TOOL-dDeclaredLoop-29 S3's closed set of row kinds
- **hands-off** `TOOL-dBoundRoles-16` — `workflow.stages`, the rows the five kinds are named defaults over
- **hands-off** `TOOL-dBoundRoles-20` — `workflow.stages`, the rows a repository's and a scenario's workflow entries compose with gov's
- **hands-off** `TOOL-dBoundRoles-43` — the stage rows and the effort order, whose every reader unit 43 re-points and whose steps it floors (ids 18 and 50 of the round-1 spec audit)

## 4. Design

### The row

```toml
[[workflow]]
name = "spec-review"
driver = "workflow"
harness = "{prefix}/workflows/tier2-review.js"
roles = ["gov-reviewer", "gov-skeptic", "gov-synthesizer"]
enforced-by = ["agent-cap.js spawn guard, on the build harness's Workflow call whose roles carry the audit's review keys"]
trigger = "after the spec set is written, where the build or its project declares a spec audit"

[[workflow.stages]]
key = "specFinder"
role = "gov-reviewer"
fan = 5
cap = 5
effort = "medium"
receives = []
returns = ["finding"]
```

| Field | Holds |
|---|---|
| `key` | the harness's stage key, `STAGE_KEY_RE` (`tools/roles/check_roles.py:110`), unique in its entry |
| `role` | the slot the stage spawns as, listed by the entry's `roles` |
| `fan` | the most agents the stage spawns in one call |
| `cap` | the most of them in flight at once, at or under `runtime.agents-in-flight` |
| `effort` | the stage's declared level, one of `EFFORT_LEVELS` |
| `receives`, `returns` | the row kinds the stage takes and hands on, from `seam`, `criterion`, `interface`, `fork`, `finding`, `repair` (TOOL-dDeclaredLoop-29 S3), empty where none |

The row kinds are read from the loop kit through `resolve_kit_dir("loop", "upstream.py", here)` where it
resolves, so the set has one home; where it does not, the two lists are graded by the `seg` shape alone
and one note says so.

### Gov's rows

| Entry | Stage rows, in order: `key` `role` fan/cap effort, receives → returns |
|---|---|
| `spec-write` | `specWriter` `gov-spec-writer` 5/5 high, seam → criterion interface fork; `disposal` `gov-spec-writer` 1/1 high, finding → repair; `builder` `gov-builder` 1/1 xhigh, criterion interface → repair; `specFinder` `gov-reviewer` 5/5 medium, none → finding; `skeptic` `gov-skeptic` 5/5 medium, finding → finding; `synthesis` `gov-synthesizer` 1/1 medium, finding → finding |
| `spec-review` | `specFinder` `gov-reviewer` 5/5 medium, none → finding; `skeptic` `gov-skeptic` 5/5 medium, finding → finding; `synthesis` `gov-synthesizer` 1/1 medium, finding → finding |
| `build` | `builder` `gov-builder` 1/1 xhigh, criterion interface → repair |
| `closing-review` | `diffFinder` `gov-reviewer` 5/5 high, none → finding; `skeptic` `gov-skeptic` 5/5 high, finding → finding; `synthesis` `gov-synthesizer` 1/1 high, finding → finding |

The fans and caps are PINNED, measured 2026-10-25 at `4ed9e567`: five finder lenses and at most five
verifier batches (`tools/workflows/tier2-review.template.js:10-11`, `MAX_VERIFIERS = 5` rendered),
five spec writers (`SPEC_WRITERS = 5` rendered) and one builder per unit. The efforts are each stage's
resolved level after TOOL-dBoundRoles-1's merge, so `stage-efforts` prints the same map before and after
this unit. The receive and return kinds state what each stage hands on as the night pass two's point 3
names the rows, so a later gate on an edge reads data rather than prose.

### The effort

TOOL-dBoundRoles-21's order with this unit's step:

1. `roles.effort.<workflow>.<stage>`; 2. `roles.effort.<role>`; 3. `roles.effort.default`;
4. the house file's chain, where present; 5. the stage row's `effort`; 6. the role's declared `effort`.

Step 5 is the stage's own declaration, read before its role's as the stage key is read before the role
key. Since `effort` is required on every row, step 6 remains for a role's own agent type, which has no
stage.

### The cap

```
limit = read_agent_limit(root)          # resolve("runtime.agents-in-flight", root, rev).value
for each entry, for each row:  red when row.cap > limit
    "entry <n> (<name>) stage <key> caps <cap> agents, above runtime.agents-in-flight <limit>"
```

`FANOUT_CAP` names no new surface: the limit is the policy key the night pass two's point 7 put in its
place.

### Inventory

Minted: the `[[workflow.stages]]` row and its seven fields; `derive_stage_map` and `read_agent_limit`
in `roles_lib.py`. Naming cells: each function is asked of `python tools/lexicon/lexicon.py --suggest
<name> --as py.function` at the pass.

### Migration

An adopter's `workflows.toml` is engine (`tools/roles/kit.toml`, `include = "**"`), overwritten on
update, so gov's rows reach every install with the reader that reads them; no adopter file holds the
inline form afterwards.

### Rollout

Live at landing on the `roles catalogue` leg; `harness-args` prints the same map for each harness, so
no Workflow call changes.

### Files touched (estimate)

- `tools/roles/workflows.toml`
- `tools/roles/roles_lib.py`
- `tools/roles/check_roles.py` (R9, R12's message, the catalogue cell, the docstring)
- `tools/roles/handoff.py`
- `tools/roles/README.md` (the `stages` paragraph and the rendered catalogue region)
- `tools/roles/adopt-roles.test.sh` (the arms of §7)
- `tools/playbook/tag_index.py` (`extract_field`'s stage half)

### Alternatives rejected

- **A second file of shapes beside `workflows.toml`.** systems.md `[design-role-shapes]` rejected it
  as two registries over one fact.
- **`[[workflow.stage]]`, singular.** It trips TOOL-dDeclaredLoop-1's AC2 grep for a line opening
  `stage` and its `stage-in-roles` plant.
- **An inline array of tables on the entry line.** It cannot carry seven fields per stage legibly, and
  TOML's array-of-tables is the form `tomllib` and a reader both read.

## 5. Production-readiness checklist

- security — no new write path; the cap arm bounds what an entry may declare, under the one limit.
- perf / scale — one `resolve` per run for the limit; the rows are a handful per entry.
- error / empty / loading states — no policy kit prints `unarmed` for the cap arm; an entry with no
  rows on a `workflow` driver is an R9 line, never an empty map passed to a harness.
- observability — `check_roles.py`'s summary counts the stage rows graded and prints the limit it
  graded against.
- risks — a harness literal and a row value can disagree until TOOL-dBoundRoles-16 binds them; §4
  pins both to the same measurement.
- testing — each criterion is a probe of the library or a scratch copy of the kit; the arm in §7 is
  observed RED then GREEN by the main loop at the close.
- migration — none owed by an adopter, as §4 Migration says.
- user docs — none owed: no page under `help/` documents `workflows.toml`; `tools/roles/README.md`
  does.

## 6. Acceptance criteria

- **AC1** — When `python handoff.py harness-args tier2-review` runs in `tools/roles/` over the rewritten
  table, it prints `{"diffFinder":"gov-reviewer","skeptic":"gov-skeptic","specFinder":"gov-reviewer","synthesis":"gov-synthesizer"}`,
  the map derived from the rows, and `grep -c 'stages = {' workflows.toml` there prints 0.
  Red when: `print_harness_args` still reads an inline table, so the rows change nothing it prints.
- **AC2** — When `python check_roles.py --root <repo>` runs from a scratch copy of `tools/roles/` whose
  `workflows.toml` adds an entry of two stages, `scout` as `gov-reuse-scout` fan 1 cap 1 and `judge` as
  `gov-skeptic` fan 1 cap 1, it prints no R9 line for that entry, and that copy's
  `handoff.py harness-args` for its harness prints both keys mapped to their two roles.
  Red when: a stage map typed per entry admits one role only, so the mixed entry reds.
- **AC3** — When `python handoff.py stage-efforts closing-review` runs in `tools/roles/`, it prints
  `diffFinder`, `skeptic` and `synthesis` at `high`, as at base; in a fixture with the house file
  deleted and no key set, it prints the rows' declared levels.
  Red when: the row's `effort` is read before the keys, so a set key loses to a row.
- **AC4** — When the scratch copy's row carries `fan = 0`, `effort = "huge"` and
  `returns = ["bug"]`, `python check_roles.py --root <repo>` exits 1 with three R9 lines naming the stage.
  Red when: the row fields are read without validation, so a harness receives a zero fan.
- **AC5** — When the scratch copy's `judge` row carries `cap = 7` and the fixture's limit resolves to 6,
  `python check_roles.py --root <fixture>` exits 1 with one R9 line naming `judge`, 7 and 6; at `cap = 6`
  it exits 0; with no policy kit it prints the cap arm `unarmed`.
  Red when: the cap is compared with a literal, so a lowered `runtime.agents-in-flight` changes nothing.
  fixture: a git repository under `%TEMP%`, short-named, holding the roles and policy kits; the policy
  kit is TOOL-dGroundRules-1's and absent at `4ed9e567`.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `playbook render selftest` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC2 AC4 AC5 · a fixture kit whose table plants a two-stage mixed-role entry, a zero fan, an unknown row kind and a cap above a committed limit · none

## 8. Open questions

- **F1 — The clause keeps the five kinds "as named defaults over" the rows, and the brief's I10 gives
  the `kind` key to TOOL-dBoundRoles-16; which unit names the defaults?** Options: (a) this unit adds
  the rows, every field required, and hands the kinds to TOOL-dBoundRoles-16, which names each kind as
  the defaults a row may omit; (b) this unit adds `kind` and its defaults too. (b) splits the shapes
  registry across two units and respells I10. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3,
  tie-broken by reuse of I10's assignment; the hand-off is the `workflow.stages` edge, and this spec
  carries the clause whole with that one phrase built by the unit after it.
  widens: none · relaxes: none
- **F2 — "A scenario's workflow entries and role rows composed per build": which unit composes them?**
  Options: (a) TOOL-dBoundRoles-20, which registers the role and workflow kinds a scenario's `activates`
  table names (TOOL-dDeclaredLoop-27 S3) and composes rows through `compose_rows`; (b) this unit,
  minting those kind rows ahead of the unit that owns them. (b) runs against the build order, the
  kinds at order 23 and this unit at 5. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the order
  constraint; this unit's rows are what the composition composes, handed off on `workflow.stages`.
  widens: none · relaxes: none
- **F3 — Is a row's `effort` required?** Options: (a) required, the clause's "every stage naming its
  ... effort"; (b) optional, the order falling to the role's declaration. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 1, the clause text; TOOL-dBoundRoles-16 may let a kind supply it.
  widens: none · relaxes: none
- **F4 — TOOL-dGroundRules-10 and TOOL-dDeclaredLoop-29 are specced and not built at `4ed9e567`.**
  RESOLVED (agent, 2026-10-25, delegated): the build run re-grounds on each at its base and stops this
  unit if `runtime.agents-in-flight` has no catalogue row then; the row kinds fall back to the `seg` shape
  with a note where the loop kit is absent, rung 1, the brief's rule for unbuilt parents.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 22, the brief's I10, scout C's row for
  cl-0187, the night pass two's point 1, and the roles kit at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring the edges of TOOL-dBoundRoles-43, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.

## 10. Reuse audit

The seam extended is the workflow registry: `workflows.toml` read only by `load_workflows`
(`tools/roles/roles_lib.py:339`), graded by R6 to R9 (`tools/roles/check_roles.py:246-313`), with its
stage readers `print_harness_args` (`tools/roles/handoff.py:453-471`), `resolve_stage_efforts`
(`roles_lib.py:571`) and R12's stage check (`:430-451`), each verified at `4ed9e567`. `python
tools/codebase-map/reuse_lookup.py "workflow entry ordered stages with fan and cap under the agent
limit"` ranked `load_workflows` first as a SEAM, then `resolve_stage_efforts` and
`extract_workflow_harnesses`, the three this unit extends. The recall probe returned scout C's row, the
brief's I10, research-role-shapes-a's inventory of the table at `:17` and TOOL-aOrientedCast-10's brief;
scout C cites R9 at `:298-310`, which source puts at `:297-310`, and `checkHarnessCall`'s `args.roles`
check at `agent-cap.js:2178-2186`, which agrees.

Recall terms used: `python tools/memory-recall/query.py "how are workflow stages declared with fan cap and effort" --terms "workflows.toml stages table fan cap agents-in-flight harness-args stage key workflow entry R9"`
