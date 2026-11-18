# TOOL-dDeclaredLoop-112 — the ask plan reads each spec's ask verbs once, so `--status` stops scaling with asks times specs

**Status:** CLOSED · rev-1 · 2026-11-15 · node a · Tier-2 · base 6d91c49a · streams tooling · order 18

**Derived:** TOOL-dDeclaredLoop-7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-11-15-build-TOOL-dDeclaredLoop-112-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-112-1-acceptance-ledger.md) | journal | — |
| [2026-11-18-build-TOOL-dDeclaredLoop-112-red-fix-76.md](../build/2026-11-18-build-TOOL-dDeclaredLoop-112-red-fix-76.md) | red-fix | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-112-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-112-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-112-build-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-112-build-brief.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-112-spec-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-112-spec-brief.md) | research | — |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dDeclaredLoop-7 S9 made `--status` run the position engine standalone, and the engine standalone
asks the driver's `--plan` for its hand-over. `--plan`'s ask plan tests every ask against every spec
with a fresh spawn chain, so the hand-over costs one chain per (ask, spec) pair, and `--status` and
`--resume`, which prints it, went from seconds to beyond ten minutes on this build (§4 Evidence, M1 to
M4). This unit reads each spec's ask verbs once per call and each ask's rank facts once per ask, so
the hand-over is linear in units and asks again, and declares a fork-ceiling row over a populated
fixture so a hand-over that scales with the roster reds the spawn budget.

## 2. Scope (IN)

- **S1** — `expand_id_runs` in `tools/unattended/lib-unattended.sh` gains a keyed mode, `--keyed`:
  each input line `<a>` TAB `<b>` TAB `<words>` prints `<a>` TAB `<b>` TAB `<id>` once per id the
  words name, ranges expanded and an `@rev-N` suffix cut by the same awk program the unkeyed mode
  runs. Input read without the flag reads exactly as today. Observed by AC1.
- **S2** — `read_spec_asks <spec>...` in `tools/unattended/unattended.sh`, beside `spec_ask_verbs`:
  one awk over every readable spec, reading the first line of each that opens `**Status:**`,
  splitting it on `·` and trimming each field as `spec_ask_verbs` does, and printing
  `<path>` TAB `<verb>` TAB `<rest of the field>` for each field opening `closes ` or `advances `,
  piped once through `expand_id_runs --keyed`. A path that is not readable is filtered out before the
  awk, which is fatal on a file it cannot open (the round-4 note on `spec_facts`), and prints nothing,
  as the failed `grep` in `spec_ask_verbs` prints nothing today. `spec_ask_verbs <spec> <verb>` keeps its
  signature and its three other callers, and prints the third field of `read_spec_asks "$1"` rows
  whose second field is its verb, so the header's verb grammar is read by one program. Observed by
  AC1, AC2.
- **S3** — The cover in `build_ask_plan`: before its per-ask loop, one `read_spec_asks "$@"` call,
  read through a process substitution as `load_spec_facts` reads `spec_facts`, fills a local map from
  each ask id to the space-joined spec paths naming it, in argument order, each path once. The
  per-ask loop walks that map's paths for its ask instead of every spec, and every line after the
  per-spec match test is unchanged, so `_cover`, `_live`, the duplicate-closer refusal and the ask
  rows keep their bytes. Observed by AC2, AC3, AC4.
- **S4** — The rank in `ask_rank_order`: before its selection rounds, each id's `holds` value and its
  `ask_sort_key` are read once into local maps, and the rounds read the maps. Both values are pure in
  the id while the function runs, since `AW_ROWS` and `ASK_POSITIONS` do not move inside it, so the
  ids it returns and their order are unchanged. Observed by AC2, AC3, AC4.
- **S5** — The row `unattended-plan-handover` in `memory/project/fork-ceilings.txt` for bash 5.3, its
  setup building the build `tFork` with twenty-four specs that grade READY, a units region listing them,
  a `BACKLOG.md` filing three asks of which one is closed by a spec's header, and a run-state file,
  with the two conf files copied from `ROOT` as the `unattended-status` row copies them; its command
  `GOV_POSITION_STATES= bash "$ROOT/tools/unattended/unattended.sh" --plan tFork`, the call the engine
  makes for `--status`. Its ceiling is the count measured at this pass and its base the count
  measured over the base driver's bytes, so the saving reads off the row. The `unattended-status`
  row's reason gains one clause saying its fixture holds no unit and that the engine's own `--plan`
  run is a python child the counter cannot see, naming the new row; its ceiling and count do not
  move. Observed by AC4.

## 3. Non-goals (OUT)

- No edit to `tools/loop/position.py`, to `verb_status` or `verb_resume`, to the hand-over grammar,
  to `--plan`'s printed rows or its `next:` shapes. TOOL-dDeclaredLoop-7 is CLOSED and its spec stays
  frozen; none of its AC1 to AC12 changes what it observes (§4 "Unit 7's criteria").
- `plan_state` keeps its one awk per unit row. `tools/unattended/check-pass-order.sh` and
  `tools/memory-tree/marker-contract.test.sh` slice it out of the driver and call it per file, and its
  per-row cost is the small term of M4.
- The three other callers of `spec_ask_verbs`, in `check_carry_forward`, `dod_met` and
  `verb_dispatch`, keep their per-spec calls. They are other verbs and no `--status` path reaches them.
- The per-ask residual of `build_ask_plan`, its closers pipelines and its `ask_field_or_dash` reads,
  stays linear in asks.
- The engine's own per-unit spawns: `derive_unit_step` asks `check_is_ancestor`, one `git merge-base`
  per held pass and tip. They run in python, the counter cannot see them, and with no unit of this
  build reading `built` today they cost nothing yet (M5).
- No cached hand-over and no new verb (§8 F1).

### Edges

- **consumes-from** external — the position engine and `--status`'s standalone call into it, landed by TOOL-dDeclaredLoop-7 at 1e11500da; the cost this unit repairs is paid through them, and it changes neither
- **hands-off** external — the engine's per-built-unit ancestry spawns, which grow with built units and are invisible to the fork counter; a follow-up ask, filed by the dispatcher if a reading shows them

## 4. Design

### Evidence

Every reading below was taken on node a, the row's id named where the text cites it.

| Id | What was measured | Reading | Status |
|---|---|---|---|
| M1 | `GOV_POSITION_STATES= bash tools/unattended/unattended.sh --plan dDeclaredLoop` at 1e11500da, 111 roster ids | 11m25s real, 3m24s user, 6m22s sys | PINNED, the run's reading carried by the brief |
| M2 | `--status dDeclaredLoop` with the driver extracted at 89baa328c, the commit before unit 7, over this tree at 6d91c49a | 12.5 s real | PINNED 2026-11-15 |
| M3 | `--status dDeclaredLoop` and `--resume dDeclaredLoop` at 1e11500da | nothing printed within 400 s and 600 s | PINNED, the run's reading carried by the brief |
| M4 | the M1 command traced as `fork-count.sh` traces, distinct `BASHPID` per function, stopped at 240 s | 168 forks before `build_ask_plan`, 1,090 before its first ask, then 1,195, 1,211 and 1,211 forks for asks one to three; of 5,136 traced: `spec_ask_verbs` 2,661, `build_ask_plan` 1,367, `ask_field` 326, `ask_sort_key` 312, `ask_rank_order` 234, `verb_plan` 107 | PINNED 2026-11-15 |
| M5 | `python tools/loop/position.py dDeclaredLoop` with a 112-row hand-over supplied | 3.8 s real, every unit `designed` | PINNED 2026-11-15 |
| M6 | the ask generator, `gen_build_index.py --asks --tsv --ready` over this build's twelve asks | 5.9 s real | PINNED 2026-11-15 |
| M7 | `GOV_POSITION_STATES= bash tools/unattended/unattended.sh --plan --asks dConvergedCharter` at 6d91c49a, 24 roster ids, 27 specs, 14 asks, one a duplicate-closer refusal | 4m15s real, 1m17s user, 2m25s sys | PINNED 2026-11-15 |

Twelve asks at about 1,200 forks each are some 14,500 of the hand-over's forks (PINNED 2026-11-15,
DERIVED from M4): the cover loop is more than nine tenths of M1. M1 over that count is near
44 ms a fork (PINNED 2026-11-15, DERIVED from M1 and M4), under the 89 to 315 ms range, PINNED, that
the header of `tools/gate-lint/fork-count.sh` records for MSYS.

### Where the time goes

- `verb_plan` (`tools/unattended/unattended.sh#verb_plan`) calls `build_ask_plan`
  (`tools/unattended/unattended.sh#build_ask_plan`) with every tracked spec. For each ask, in rank
  order, it runs `spec_ask_verbs "$_sp" closes | grep -qxF` over every spec, and `advances` where that
  misses: a command substitution, a `grep`, a `printf | awk` pipe, the `expand_id_runs` awk and the
  caller's `grep`, twice per pair (`tools/unattended/unattended.sh#spec_ask_verbs`,
  `tools/unattended/lib-unattended.sh#expand_id_runs`). That is the per-pair chain M4 counts.
- `ask_rank_order` (`tools/unattended/unattended.sh#ask_rank_order`) is a selection sort whose every
  round re-reads each remaining id's `holds` through `ask_field` and its key through `ask_sort_key`
  (`tools/unattended/unattended.sh#ask_sort_key`), so its reads grow with the square of the asks.
- `plan_state` (`tools/unattended/unattended.sh#plan_state`) is one awk per unit row; it and the rest
  of `verb_plan`'s prelude are the 168 forks of M4 before the ask plan, PINNED 2026-11-15.
- The engine alone is cheap (M5); its cost under `--status` is the `--plan` it runs through
  `read_handover` (`tools/loop/position.py#read_handover`) when the hand-over variable is empty.

### Which callers need the engine's full answer

| Caller | What it reads from the engine | Needs the ask plan |
|---|---|---|
| `--plan` | the `next:` line, rendered from the answer; it hands over its own rows, so the engine never re-runs it | yes, its own |
| `--status` (`tools/unattended/unattended.sh#verb_status`) | the `position —`, `unit —`, `next —` and `interrupt —` lines and the least-advanced unit for `· next` | yes: the undecided ask is an `interrupt —` line and moves the answer between `awaiting` and `terminal` (`tools/loop/position.py#derive_interrupts`, `tools/loop/position.py#derive_answer`) |
| `--resume` (`tools/unattended/unattended.sh#verb_resume`) | `verb_status`'s lines, at its exits | yes, through `--status` |
| `position.py <slug>` standalone | the whole `Position` | yes |

No caller can skip the ask plan without printing different lines, so the repair makes the plan cheap
for all of them rather than giving one caller a thinner hand-over (§8 F1).

### The mechanism

The cover reads each spec once:

```
read_spec_asks "$@"            ->  <path> TAB closes|advances TAB <ask id>   one row per id, ranges expanded
local -A _covers               ->  _covers[<ask id>]="<path> <path> ..."     argument order, each path once
for _sp in ${_covers[$_id]:-}  ->  the existing body after the per-spec match test, unchanged
```

`read_spec_asks` is one awk and one `expand_id_runs --keyed` per `build_ask_plan` call, whatever the
number of specs and asks. Its rows never carry an empty field, so the `IFS` read that fills the map
cannot collapse one (`memory/gotchas/empty-field-collapses-unless-it-is-last.md`). Paths are the
`git ls-files` output `verb_plan` already word-splits into `build_ask_plan`, so splitting the map's
value adds no assumption the caller does not already make.

The rank reads each ask once: a first pass over the ids sets `_key[<id>]` from `ask_sort_key` and
`_holds[<id>]` from `ask_field <id> holds`, and the selection rounds, the blocked test and the
fall-back round read the two maps. The output is the same id string.

Expected cost on this build after the repair: the cover loop's thousands of chains become one call,
and the rank's quadratic reads become two per ask; the prelude, the generator (M6), the per-ask
residual and the engine (M5) remain. `--status dDeclaredLoop` is expected within one minute, an
estimate from M2, M4, M5 and M6, PINNED 2026-11-15, and AC3 reads it.

### Unit 7's criteria

The repair changes no byte any of TOOL-dDeclaredLoop-7's criteria reads. AC1 to AC9 and AC12 run the
engine over plants with the hand-over supplied and never reach the driver. AC10's `plan-line` plant
and AC11's `status-line` plant run the driver's `--plan` and `--status`; their observations stand as
written, and AC5 below re-runs both at this pass. `--plan`'s `next:` shapes are rendered by the engine
from the same hand-over bytes, so they keep their bytes, which AC2 and AC3 compare.

### Inventory

| Identifier | Kind | Where | Naming |
|---|---|---|---|
| `read_spec_asks` | function | `tools/unattended/unattended.sh` | cell `sh.function`: `lexicon.py --suggest read_spec_asks --as sh.function` answers OK, leading verb `read` |
| `--keyed` | mode argument of `expand_id_runs` | `tools/unattended/lib-unattended.sh` | none |
| `unattended-plan-handover` | fork-ceiling row id | `memory/project/fork-ceilings.txt` | none |

The two maps of S3 and S4 are `local` to their functions and are not minted names.

### The fixture

The row's setup is one shell line, as every row's is: `git init`, the two conf files copied from
`ROOT`, a README whose front matter names `slug: tFork` and whose `<!-- gen:build-units -->` region
lists the twenty-four ids (PINNED, the declared size), the twenty-four specs in the READY shape
`position.py`'s `render_spec` writes (`tools/loop/position.py#render_spec`), the first of them
carrying `closes TOOL-tFork-91` in its header, a `BACKLOG.md` whose `## Asks` section files
`TOOL-tFork-91` to `TOOL-tFork-93`, a `RUN.md` carrying `phase: RUNNING`, and one commit. The asks
generator the copied conf declares resolves no path in the scratch directory, so `run_ask_witness`
answers with `AW_WHY` and the plan goes on with no projection rows, as it does in every tree that has
not adopted the generator; the cover loop and the rank still run over the three asks. Twenty-four
specs make a per-unit spawn add a visible multiple of twenty-four to the count, and three asks make a
per-pair chain cost some 860 forks (DERIVED from M4's per-pair figure, PINNED 2026-11-15) against a
ceiling expected near two hundred.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `read_spec_asks`, `spec_ask_verbs`, `build_ask_plan`,
  `ask_rank_order`
- `tools/unattended/lib-unattended.sh`: `expand_id_runs --keyed`
- `memory/project/fork-ceilings.txt`: the new row and the `unattended-status` reason clause
- `memory/map/generated/symbols.json`: regenerated for the new function

### Alternatives rejected

- **A hand-over built without the M2 classification, a cheaper witness per row (§8 F1 (a)).** M4 puts
  `plan_state` near one percent of the cost, and the cheaper witness on offer is the typed status word
  unit 7 retired as a step source.
- **`--status` and `--resume` stop running the engine, a separate verb printing its lines (§8 F1
  (c)).** It moves TOOL-dDeclaredLoop-7 S9's observation, AC11, hands `· next` back to the typed
  status, and leaves `--plan` and check 30's walk as slow as M1.
- **One awk that classifies and covers every spec.** `plan_state` is sliced by two other legs per
  file, and the cover is the cost; one change, not two.
- **A cached hand-over keyed by HEAD.** A new write path and a staleness question for a cost the
  hoist removes.

## 5. Production-readiness checklist

- security — read-only: every changed function reads tracked spec headers and the projection already
  in memory, and writes nothing. No new command, path or remote.
- perf / scale — the unit's subject. The cover becomes one awk per call and the rank two reads per ask;
  `plan_state`'s one awk per row and the per-ask residual stay. Check 30 of
  `tools/unattended/check-unattended.sh` walks `--plan` over every build, so the `unattended kit
  gate` leg gains too; its `tools/run-gates/selftest-budgets.txt` row grades only an overrun and
  does not move.
- error / empty / loading states — a build with no ask returns from `build_ask_plan` before the map is
  read, as today. A spec whose header names no verb adds no row. An unreadable spec adds no row and
  reaches no awk, so one missing file cannot blank the map.
- observability — none added. `--plan`, `--plan --asks` and `--status` print what they printed.
- risks — the cover's ORDER: `_cover` is the first spec in argument order naming the ask, and the
  map keeps argument order because the awk reads its files in that order and each path enters once.
  A reader of `spec_ask_verbs`'s output: its three other callers read the same lines from the new
  body, which AC1 compares over two builds' specs. The rank's equality rests on `AW_ROWS` and
  `ASK_POSITIONS` not moving inside `ask_rank_order`, which no line of it assigns.
- dependency — order 18, before units 14, 45 and 69. TOOL-dDeclaredLoop-14 edits `verb_plan` and
  `tools/loop/position.py` for its frontier, away from `build_ask_plan`, `ask_rank_order` and
  `spec_ask_verbs`, so it starts from this unit's landed bytes.
- registry, budgets, ceilings and maps, each row the change could newly red and what keeps it green:
  - `memory/project/fork-ceilings.txt`, row `unattended-plan-handover`: new, its ceiling the count
    `fork-count.sh --only unattended-plan-handover` measures at this pass, three readings, the
    largest written, as the file's other rows record theirs.
  - the same file's `unattended-status` row: its fixture README carries no units region, so `--plan`
    refuses before `build_ask_plan` and the engine's child is invisible; the count stays at its
    ceiling, and only the reason column gains a clause.
  - the same file's `check-unattended` row: its fixture holds no build, so check 30 walks nothing;
    unchanged.
  - `memory/project/spawn-idiom-sites.txt`, the `tools/unattended/unattended.sh` and
    `tools/unattended/lib-unattended.sh` rows: `ask_sort_key` and `ask_field` spawn, so a
    substitution of either is not `pure-fn-subst`, and the design adds no `printf-subst`,
    `var-pipe` or `path-subst` site; if the scan's count moves, the row moves in the same commit.
  - `memory/project/substitution-fed-loops.txt`: the map is read through a process substitution, a
    shape the leg does not count; no here-string or heredoc is added.
  - `tools/gate-legs.json`, `tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv` and
    `tools/govkit/usage.toml`: no leg, flag or script is added, so no row moves; the spawn budget leg
    runs one more row inside its 2400 s ceiling, PINNED in `tools/gate-legs.json` at 6d91c49a.
  - `memory/map/generated/symbols.json`: regenerated for `read_spec_asks`. The symbol tier feeds that
    file only and never the map's ratchet, and `memory/map/features/unattended.md` names none of the
    four functions this unit edits, so the dossier does not move.
  - `tools/unattended/check-pass-order.sh` and `tools/memory-tree/marker-contract.test.sh` slice
    `plan_state` out of the driver; it is not edited.
  - `tools/unattended/unattended.test.sh`: its ask arms read the `ASK` rows' `cover=` and `rank=`
    fields, which keep their bytes. The suite is waived for this build's landing (the build README,
    owner 2026-10-20).
- testing — AC1 to AC5; the parity criteria compare this pass's bytes with the base driver's.
- migration — none; no record or row shape changes, and the fork-ceiling row is additive.
- user docs — none: no verb, flag or printed line changes, so no page under `help/` moves.

## 6. Acceptance criteria

- **AC1** — When `expand_id_runs --keyed` reads `p` TAB `closes` TAB `TOOL-x-1..3 TOOL-y-7@rev-2`
  with `tools/unattended/lib-unattended.sh` sourced, it prints four rows keyed `p` TAB `closes`, ids
  `TOOL-x-1`, `TOOL-x-2`, `TOOL-x-3` and `TOOL-y-7`; and when `spec_ask_verbs` is sliced out of this
  pass's driver and out of the base driver (`git archive 6d91c49a tools`), both print the same ids
  for `closes` and for `advances` over every tracked spec of `memory/builds/dDeclaredLoop/spec/` and
  `memory/builds/dConvergedCharter/spec/`.
  Red when: a range is not expanded, a keyed row loses its key, or one spec's ids differ.
  fixture: the tree holds no status header in the range form, so the planted line is the only range
  case.
- **AC2** — When `GOV_POSITION_STATES= bash tools/unattended/unattended.sh --plan --asks
  dConvergedCharter` runs at this pass and with the base driver extracted by `git archive`, the two
  outputs are byte-identical, each carrying an `ASK` row per filed ask, the `refused=duplicate-closer`
  row among them; and `--plan dConvergedCharter`, the engine called, prints the same `next:` line from both.
  Red when: a cover, a rank, a duplicate-closer refusal or the `next:` line differs.
  cost: the base driver's run is M7; run it in the background with a bound.
- **AC3** — When `bash tools/unattended/unattended.sh --status dDeclaredLoop` runs at this pass, it
  prints the engine's `position —` line and returns within 60 s (PINNED, the ceiling this unit
  declares, against M2's 12.5 s and M3's over 400 s, PINNED); and
  `GOV_POSITION_STATES= bash tools/unattended/unattended.sh --plan dDeclaredLoop` prints the same
  bytes as the base driver's.
  Red when: `--status` takes longer than the ceiling, prints no position line, or the hand-over differs.
  cost: the base driver's `--plan dDeclaredLoop` is M1's eleven minutes; run it in the background with
  a bound of 900 s (PINNED, the bound this criterion declares).
  permission: `--resume` writes the run's lease and run-state file, so it is observed through
  `--status`, which each of its exits prints.
  figure: the 60 s ceiling is PINNED; the reading is taken at observation.
- **AC4** — When `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only
  unattended-plan-handover` runs at this pass, it exits 0 with the count at the row's ceiling; and
  with the base driver's bytes of `build_ask_plan` and `ask_rank_order` restored in the worktree, it
  exits 1 naming a delta above the ceiling and sites on `spec_ask_verbs`'s lines. The row's setup and
  command run by hand, with `--asks` added, print three `ASK` rows, one naming the closing spec as its
  cover.
  Red when: the restored per-pair loop stays within the ceiling, or the fixture prints no `ASK` row and
  the count grades a plan that never ran.
  figure: the ceiling and the base are counts measured at this pass, then PINNED in the row.
- **AC5** — When `python tools/loop/position.py --fixture --plant plan-line` and `--plant status-line`
  run at this pass, each prints `position: fixture · <case> · held`.
  Red when: the driver's `next:` line or `--status`'s position line moves.

## 7. Gates

`spawn budget (forks per hot entrypoint)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `unattended kit gate` · `loop position fixtures` · `pass-order history` · `marker contracts` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `scratch-guard self-test` · `routed-commits selftest` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: memory/project/fork-ceilings.txt · covers AC4 · the row `unattended-plan-handover`, red with the base driver's `build_ask_plan` and `ask_rank_order` bytes restored, the per-pair chains lifting the count far above the ceiling · none

What the row does not check, stated so a green is not read as more. It counts bash forks only: the
engine and every process a python child starts are invisible to it (the counter's own header says so),
so the engine's per-unit spawns and the `--plan` that `--status` runs through python are not graded
under `--status`; the row grades that `--plan` directly instead. It reads no clock, so a cost that
spends no fork, an awk that grows quadratic inside one process or a slower generator, is unseen. It
grades bash 5.3 alone, printing the `skipped` shape on any other. It grades `--plan` and not
`verb_status`'s own body, whose fixture in the `unattended-status` row holds no unit. And it grades a
count, not a slope: any fork above the ceiling reds, a fixed one as surely as a per-unit one, and only
the size of the delta, a multiple of the fixture's twenty-four specs or three asks, tells a reader
which class came back.

## 8. Open questions

- **F1 — Which mechanism restores the cost?** (a) `--status` and `--resume` take their lines from a
  hand-over the driver builds without the per-row M2 classification, a cheaper witness deciding each
  row; (b) the per-pair reads `--plan`'s ask plan runs are hoisted to one read per spec and per ask,
  so every engine caller gains; (c) `--status` and `--resume` stop running the engine and a separate
  verb prints its lines. M4 refutes (a)'s premise: the classification is about one percent of the
  cost and the ask plan the rest, and its cheaper witness is the typed status unit 7 retired. (c)
  moves unit 7's S9 and AC11 and leaves `--plan` and check 30 at M1. Recommendation (b), the body's.
  RESOLVED (agent, 2026-11-15, delegated): (b), rung 3: the measurement puts nine tenths of the cost in build_ask_plan's per-ask spec reads, which one read per spec removes for every engine caller
  widens: none · relaxes: none
- **F2 — What does "no more than before unit 7" mean on this build?** (a) The hand-over is linear in
  units and asks again and `--status dDeclaredLoop` returns within a one-minute ceiling: M2 plus the
  engine and the hand-over's floor, which unit 7's S9 accepted when it added the call; (b) `--status`
  matches M2 itself, which no design running the engine can, so it needs F1 (c) or a cached hand-over.
  Recommendation (a): the regression is the scaling, and the engine's fixed cost is the price S9
  chose.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: the hand-over stops growing with asks times specs and --status returns within its bound, while the engine still runs
  widens: none · relaxes: none
- **F3 — Does the rank's quadratic read belong in this unit?** (a) Yes, S4: the same hoist in the same
  hand-over path, about a tenth of the hand-over's forks before the first ask (M4); (b) no, filed as
  an ask. (b) leaves a term that grows with the square of a build's asks on the path this unit exists
  to bound. Recommendation (a).
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: the rank's repeated fact reads are the same hoist in the same reader
  widens: none · relaxes: none
- **F4 — What form does the gate take?** (a) A fork-ceiling row over `--plan` with the hand-over
  variable empty, the call `--status` makes, over a populated fixture; (b) a wall-clock bound on
  `--status` over a fixture, which sees python too but flakes on a loaded host, the reason the counter
  reads no clock; (c) both. Recommendation (a), with §7's statement of what it does not see.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: a fork count over the exact --plan call the engine makes is deterministic on every node
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft, from the brief 2026-11-15-prompt-TOOL-dDeclaredLoop-112-spec-brief
  and the writer's handoff 2026-11-15-prompt-TOOL-dDeclaredLoop-112-1-spec-writer.

## 10. Reuse audit

The seam is TOOL-aCollapsedScan-1's: `spec_facts` and `load_spec_facts`
(`tools/unattended/unattended.sh#spec_facts`, `tools/unattended/unattended.sh#load_spec_facts`)
collapsed `verb_plan`'s per-spec awks into one pass and a map lookup, and S2 and S3 extend that seam
to the header's ask verbs, read through the existing `expand_id_runs`, whose awk program gains a mode
rather than a copy. The gate extends TOOL-aSparedSpawn-8's fork-ceiling file with one row beside
`unattended-status`. The map dossier probe,
`python tools/codebase-map/reuse_lookup.py "batch per-spec header reads into one pass instead of one spawn per spec in the plan verb"`,
ranked name-stem neighbours (`read_text`, `read_design_conf`, `read_spec_revisions`) and no seam in
the driver; the recall probe found TOOL-aCollapsedScan-1 and TOOL-aSparedSpawn-8, which name the two
seams above.

Recall terms used: `spawn fork per-spec awk collapsed scan spec_facts build_ask_plan cover rank fork-count ceiling`, against the question "why does the plan verb spawn a process per spec and how was it collapsed before".
