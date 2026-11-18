# TOOL-dDeclaredLoop-99 — every `loop_lib.py` function that opens a conf is declared in `CONF_READERS` or `CONF_ROUTES`, checked both ways by a definition plant

**Status:** CLOSED · rev-2 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 50 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-10-24-build-TOOL-dDeclaredLoop-99-deviation-991.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-99-deviation-991.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-100-deviation-1172.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-100-deviation-1172.md) | deviation | TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-117 |
| [2026-11-17-build-TOOL-dDeclaredLoop-99-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-99-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-99-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-99-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-99-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-99-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-99-reground-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-99-reground-brief.md) | research | — |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-12 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-95-spec-audit.md`)
confirmed finding **id 19 at HIGH**, in its item **H1**. Ids 1 and 11 share that item, and each is its
own unit: `TOOL-dDeclaredLoop-97` (id 1) and `TOOL-dDeclaredLoop-98` (id 11).

Id 19 is the failure envelope of H1. The `no-own-conf-read` rule, `derive_conf_reads`, answers a
`reader call` only for a callee it was told about, so a reader `loop_lib.py` gains later escapes the
rule until someone declares its name. When rev-1 was written that reader was 95's `read_tree_conf`.
95 rev-3 builds none, and the class stays: 97 gives the rule one declared tuple, `CONF_READERS`, and
nothing checks that the tuple keeps up with `loop_lib.py`.

This unit derives, from the syntax of `loop_lib.py`, the functions that build a conf path and open it,
and compares that set both ways with what the module declares, in a plant the `loop definition
fixtures` leg runs on every bar. At HEAD the derivation finds two functions: `read_driver_conf`, a
declared reader, and `resolve_memory_root_source`, which opens the driver's conf to key its cache and
is the sanctioned route the rule never grades (97 §3). The second is declared in a tuple of its own,
`CONF_ROUTES`, so each function that opens a conf sits in exactly one declaration. The next function
that opens a conf then reds the leg until it is declared, and a declaration that outlives its opener
reds it too. It builds at order 50, after 97, and repairs `TOOL-dDeclaredLoop-95`.

## 2. Scope (IN)

- **S1** — `derive_conf_openers(loop_lib_path)` in `tools/loop/loop_lib.py`, directly below
  `derive_conf_reads`, answers the sorted names of the module-level `def` and `async def` nodes of the
  file at `loop_lib_path` that `derive_fixture_boundary` does not answer and whose own body meets both
  tests below. The body is the nodes reached from the definition's statements, a nested `def`,
  `async def` or `class` and everything under it excluded. It calls
  `derive_conf_constants(loop_lib_path)` first, so that function's refusals, a missing or unparseable
  file and `load_tree_lib`'s, are this one's, then parses the file with `ast` and never imports it.
  - **Builds a conf path**: an operand of a `/` `BinOp`, or a positional argument of a call whose
    callee, a `Name` by its id or an `Attribute` by its attr, is `join`, `Path` or `PurePath`, is a
    subtree `check_conf_name` answers, or is a `Name` or an `Attribute` naming a member of the
    `derive_conf_constants` answer.
  - **Opens content**: a call whose callee, named the same way, is `parse_conf`, `open`, `read_bytes`
    or `read_text`, or a call of an attribute of the name `subprocess`, which is how
    `read_driver_conf` sources the driver's conf.
  The function holds no conf file name of its own: `check_conf_name` is the one conf-name predicate,
  as it is for `derive_conf_constants` and `derive_conf_rebinds`. Observed by AC2.
- **S2** — `CONF_ROUTES = ("resolve_memory_root_source",)` is a module-level tuple in
  `tools/loop/loop_lib.py`, directly above `derive_conf_openers`, under a `#` comment naming it the
  functions of this module that open a conf and answer a resolved root, never a conf's values: the
  sanctioned route the rule never grades, declared beside `CONF_READERS` for the plant in S3. Observed
  by AC1, AC3.
- **S3** — The plant `conf-readers-declared` joins `PLANTS` and `PLANT_OWED` in `tools/loop/loop_lib.py`.
  - Its `PLANTS` description names the check in words and spells no conf file name, as every
    description there does, so `derive_conf_constants` over `loop_lib.py` keeps its answer.
  - Its `PLANT_OWED` row is `(0, "loop: conf readers declared · ", " opener(s) · ")`, so `--selftest`,
    which the `loop definition fixtures` leg runs, holds it on every bar.
  - `main`, once the argv names this plant, prints the `loop: fixture · plant <name> · <description>`
    line every plant prints, reads no definition, and calls `check_conf_readers_plant(loop_lib_path)`
    with its own file, `pathlib.Path(__file__)`. It prints each refusal as `loop: refused · <why>` and
    exits 1 where there is one, else 0.
  - `check_conf_readers_plant` compares the `derive_conf_openers` answer over that file with
    `CONF_READERS` and `CONF_ROUTES`, read from its own module's globals, and answers one refusal per
    mismatch, in this order:
    - an empty answer: `no conf opener found in loop_lib.py`, so a predicate that matches nothing
      cannot pass;
    - a derived opener in neither tuple: `<name> opens a conf and is in neither CONF_READERS nor CONF_ROUTES`;
    - a member of either tuple that this module binds as a function, `callable(globals().get(name))`,
      and that the answer lacks: `<name> is in <tuple> and opens no conf`.
    A member this module does not bind, `read_design_conf` of the memory-tree kit's `design_lib.py` and
    `parse_conf` of its `tree_lib.py` at HEAD, is outside the comparison and named on the pass line.
    A `LoopError` from `derive_conf_openers` is answered as one refusal, its text. With no refusal it
    prints `loop: conf readers declared · <n> opener(s) · <names> · outside this module <names or none>`.
  Observed by AC1, AC3, AC4.
- **S4** — The docs name the plant and the function. `tools/loop/README.md` gains a
  `derive_conf_openers(loop_lib_path)` row in its table of `loop_lib.py` functions and a sentence on
  `conf-readers-declared` in its paragraph on that module's plants. `help/loop.md` gains a sentence on
  the case in its "See a refusal" bullet for `loop_lib.py`. The regenerated
  `memory/map/generated/symbols.json` gains the rows `derive_conf_openers` and
  `check_conf_readers_plant`. Observed by AC5.

## 3. Non-goals (OUT)

- **Rev-1 items settled at HEAD.** Each was read on the branch tip §4 Evidence names.

| Item | Rev-1 ordered | Settled because |
|---|---|---|
| AC1's and AC2's answer | `read_driver_conf read_tree_conf` | no `read_tree_conf` exists and 95 rev-3 builds none; `resolve_memory_root_source` opens the driver's conf with `read_bytes` to key `DRIVER_ROOTS`, so S1's predicate answers it, which rev-1 §4 had not read; S2 declares it (§8 F3) |
| S2's second case over every member of `CONF_READERS` | a member S1 does not derive reds | 97 S1's tuple holds `read_design_conf` and `parse_conf`, defined outside `loop_lib.py`, which S1 never derives; S3 compares the members this module binds (§8 F4), as 97 §3 hands off |
| S3 and AC4 | rev bumps of 87 §3 and 89 S5 naming the `reader call` kind over `CONF_READERS` | 87 and 89 are CLOSED and frozen, and their hands-off bullets stand as record; `tools/loop/loop_lib.py#derive_conf_rebinds` names a `def` or `class` name read through a call as a `reader call` in its docstring, and 97 S2 points `derive_conf_reads`' docstring at the tuple |
| S2's leg wiring | the plant joins `loop_lib.py --fixture` | 67 S30 built the leg as `loop_lib.py --selftest`, which runs every `PLANTS` member against its `PLANT_OWED` row, so S3 adds a row to each, as 67 §5 asks this unit's re-ground |

- The tuple of reader callees and the rule reading it: id 1's mechanism, `TOOL-dDeclaredLoop-97`.
- The plant row proving that the rule answers each member: id 11's mechanism, `TOOL-dDeclaredLoop-98`.
- A conf read in `budget.py` or `breakpoints.py` themselves: the `no-own-conf-read` plants' (76 S3).
- Whether a member defined outside `loop_lib.py` exists: 97 AC1 observes it once. The plant names those
  members on its pass line and checks none of them (§8 F4).
- A reader whose conf path is built in one function and opened in another, a conf name composed at run
  time, such as `"." + "unattended.conf"`, and `subprocess` reached under another name. S1 reads one
  body at a time, constant text only and the bare name `subprocess`. A declared member split this way
  still reds the third case of S3, and an undeclared one is missed. 76 §5 records the run-time
  composition gap for the rule itself.
- A function that calls a declared reader, such as `read_builds_dir`, which calls `read_design_conf` and
  builds the memory-tree conf's path only for its message. Following calls is §4's rejected alternative.
- A name in both tuples. The rule would grade it as a reader, so the readers' own plants red where a
  loop module calls it; this plant does not check the overlap.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-97` — `CONF_READERS`, whose members this module binds S3 compares both ways with S1's derived openers, two members being defined outside `loop_lib.py` (the round-12 spec audit's ids 1, 19)
- **consumes-from** `TOOL-dDeclaredLoop-80` — S1's fixture boundary, `derive_fixture_boundary`, outside which S1 derives the openers (the round-12 spec audit's id 19)
- **consumes-from** `TOOL-dDeclaredLoop-87` — `derive_conf_constants` as S1 states its class, whose members count as a conf path in S1; §3's bullet on a conf read through a call stands frozen (the round-12 spec audit's id 19)
- **consumes-from** `TOOL-dDeclaredLoop-89` — S5's sub-bullet on a `def` or `class` name read through a call, which stands frozen and which `derive_conf_rebinds`' docstring carries (the round-12 spec audit's id 19)
- **consumes-from** `TOOL-dDeclaredLoop-67` — S30's `loop definition fixtures` leg, argv `loop_lib.py --selftest`, which runs S3's plant against its `PLANT_OWED` row (the round-12 spec audit's id 19)
- **hands-off** `TOOL-dDeclaredLoop-100` — the `conf-readers-declared` plant, which that unit's AC6 re-runs over the conf read it rewrites (the round-12 spec audit's ids 10, 19, 20)

## 4. Design

### Evidence

Read or probed 2026-11-17 on node `d`: PINNED, that date. Every code read is of
`branch/unattended-declared-loop-d56bf0` at `5197eb157`, its tree written by `git archive` into the
run's scratch directory, since this worktree is cut from main, which lacks the loop kit. The
prototype of S1 ran in that copy's `tools/loop/`, importing its `loop_lib`. 97 rev-2 was read from the
branch, not yet built. The lexicon's `--suggest` ran in this worktree, whose `.lexicon.conf` differs
from the branch's in the offender pin's comments and value alone.

- `tools/loop/loop_lib.py#resolve_memory_root_source` builds `pathlib.Path(tree).resolve() / ".unattended.conf"`
  and keys `DRIVER_ROOTS` by `conf.read_bytes()`; it also builds the memory-tree conf's path for an
  existence test, and reads both confs' values through `read_design_conf` and `read_driver_conf`.
  `budget.py` and `breakpoints.py` import and call it, so it cannot join `CONF_READERS` without the
  rule grading their sanctioned route.
- `tools/loop/loop_lib.py#read_driver_conf` builds `top / ".unattended.conf"` and runs bash through
  `subprocess.run`. `tools/loop/loop_lib.py#read_builds_dir` builds the memory-tree conf's path only
  inside its message and opens nothing itself.
- The prototype of S1 over `loop_lib.py` answered `['read_driver_conf', 'resolve_memory_root_source']`
  in 0.3 s wall time for one python process, PINNED. Beside them it saw a builder alone in
  `read_builds_dir` and an opener alone in `resolve_kit_dir`, `derive_conf_constants`,
  `derive_conf_reads`, `read_actor_rows`, `read_definition`, `read_layer_tags` and `derive_item_scope`.
  Over the fixture module below it answered `['read_by_constant', 'read_by_shell', 'read_path_call',
  'read_slash']`, and `derive_conf_constants` answered `DRIVER` there and nothing over `loop_lib.py`.
- `grep -rn read_tree_conf tools/` prints nothing; `CONF_READERS` is 97 S1's, unbuilt at the tip.
- `tools/loop/loop_lib.py#main` runs `--selftest` as every `PLANTS` member through
  `run_selftest_cases` against `PLANT_OWED`, and its usage line joins the `PLANTS` keys. `PLANTS` and
  `PLANT_OWED` hold 34 rows each, PINNED at the tip. No `PLANTS` description spells a conf file name.
- `tools/gate-legs.json`'s `loop definition fixtures` leg runs `{prefix}/loop/loop_lib.py --selftest`
  with ceiling 120 s, PINNED, subject `kit`, stage `step.test` and no guard.
- `tools/govkit/usage.toml`'s `script:{prefix}/loop/loop_lib.py` row lists flags alone, `--plant=`
  among them, and `help/loop.md` anchors it; `help/loop.md` and `tools/loop/README.md` each list every
  definition plant by name.
- `tools/loop/loop_lib.py#derive_fixture_boundary` answers every `def` whose name split on `_` holds
  `fixture` or `plant`, so `check_conf_readers_plant` sits inside the boundary and S1 passes over it.
- `tools/loop/loop_lib.py#check_conf_name` walks a node's subtree for a str constant holding a conf
  file name, an f-string's literal part included.

### The check, after this unit

```
# The functions of this module that open a conf and answer a resolved root, never its values: the
# sanctioned route the no-own-conf-read rule never grades (TOOL-dDeclaredLoop-99 S2).
CONF_ROUTES = ("resolve_memory_root_source",)

derive_conf_openers(loop_lib_path):
    consts = derive_conf_constants(loop_lib_path)               # its refusals are this one's
    tree   = ast.parse(read(loop_lib_path))                     # parsed, never imported
    for each def | async def in tree.body not in derive_fixture_boundary(tree):
        body   = nodes under its statements, nested def | async def | class subtrees excluded
        path   = check_conf_name(operand) or a Name | Attribute in consts
        builds = a path as an operand of "/", or as a positional argument of join | Path | PurePath
        opens  = a call of parse_conf | open | read_bytes | read_text, or of subprocess.<any>
        builds and opens -> answer its name
    return sorted names

check_conf_readers_plant(loop_lib_path):
    try derived = derive_conf_openers(loop_lib_path) except LoopError as e -> [str(e)]
    declared = CONF_READERS + CONF_ROUTES ; here = [m for m in declared if callable(globals().get(m))]
    refusals = ["no conf opener found in loop_lib.py"] if not derived else []
    refusals += [d + " opens a conf and is in neither CONF_READERS nor CONF_ROUTES" for d not in declared]
    refusals += [m + " is in <its tuple> and opens no conf" for m in here not in derived]
    no refusals -> print "loop: conf readers declared · <n> opener(s) · <derived> · outside this module <declared - here>"
    return refusals
```

### The fixture module AC2 writes

```
import os, pathlib
DRIVER = ".unattended.conf"
def read_slash(t): return open(t / ".unattended.conf").read()
def build_only(t): return os.path.join(t, ".memory-tree.conf")
def read_path_call(t): return pathlib.Path(t, ".memory-tree.conf").read_text()
def read_by_constant(t): return parse_conf(t / DRIVER)
def read_by_shell(t):
    import subprocess
    return subprocess.run(["cat", str(t / ".unattended.conf")])
def read_nested(t):
    def inner(): return open(t / ".unattended.conf").read()
    return inner
def seed_fixture_conf(t): return (t / ".unattended.conf").read_bytes()
def read_other(t): return open(t / "notes.txt").read() if ".unattended.conf" else None
```

### Write set

This pass writes `tools/loop/loop_lib.py` (S1 to S3), `tools/loop/README.md` and `help/loop.md` (S4),
and regenerates `memory/map/generated/symbols.json` with `python tools/codebase-map/gen_map.py --write`,
which gains two function rows (S4). It writes no sibling spec. The build README's regions are the
generator's render, and the loop kit's version is the lander's mint.

### Inventory

- `derive_conf_openers` — a public function in `tools/loop/loop_lib.py`, one row in
  `memory/map/generated/symbols.json`.
- `check_conf_readers_plant` — a function in `tools/loop/loop_lib.py`, inside the fixture boundary, one
  row in `memory/map/generated/symbols.json`.
- `CONF_ROUTES` — a module-level tuple in `tools/loop/loop_lib.py`, not a symbol row, as 97's
  `CONF_READERS` is not.
- `conf-readers-declared` — a `PLANTS` and `PLANT_OWED` key of `tools/loop/loop_lib.py`.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/README.md`
- `help/loop.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Leave the tuple hand-kept, with no check (97 alone).** The tuple then drifts as the two-name pair
  did, and the next reader repeats H1.
- **Derive the rule's reader set from S1 and keep no tuple.** The rule would rest on a heuristic with no
  declared answer to compare against, and a predicate miss would shrink the rule silently.
- **Class a function as a reader when its body names a conf at all.** `derive_conf_reads`,
  `check_conf_name` and `read_builds_dir` name a conf with no path opened, so the rule and its
  predicate would be readers. S1 requires a conf path and an open call in one body.
- **Follow calls, so a function calling a reader is a reader.** `resolve_memory_root_source` and
  `read_builds_dir` call readers and return a resolved root or folder; following calls would class
  every caller of a reader as one.
- **Hold `resolve_memory_root_source` as a literal inside the plant (§8 F3 option b).** A second,
  unnamed list beside the two tuples, and one never checked both ways.

## 5. Production-readiness checklist

- security — the rule's reader set cannot fall behind `loop_lib.py` silently: a new function that
  opens a conf reds the leg until it is declared a reader, which the rule grades, or a route, which is
  reviewed as one. The `confs-disagree` refusal (72 AC3) keeps its reach.
- perf / scale — one `derive_conf_constants` call and one `ast.parse` of `loop_lib.py` per plant run,
  0.3 s for the prototype's whole process, PINNED 2026-11-17, against the leg's ceiling of 120 s, PINNED.
- error / empty / loading states — an empty derived set refuses by name; a missing or unparseable
  file and a memory-tree kit that does not load are `derive_conf_constants`' refusals (86 S13, 88 S33,
  94 S21), each answered as one refusal and exit 1.
- observability — the pass line names every derived opener and every declared member outside this
  module, and each refusal names the function, the tuple and the direction.
- risks — S1 is syntactic and over-matches on the closed side: a body building a conf path and opening
  any other file is derived, and the owner declares or restructures it. §3 names the blind spots. The
  members outside `loop_lib.py` are named on the pass line and never checked.
- testing — AC1 to AC5 as plant runs, probes, staged breaks in scratch copies and greps.
- migration — none: no stored data, and the rule's answers do not move.
- user docs — `help/loop.md`'s "See a refusal" bullet and `tools/loop/README.md` (S4). No verb or flag
  is added, so no usage row or anchor moves.

### The sweep

Each count is DERIVED by the command beside it, run on the branch tip's archived copy unless the row
says otherwise.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| `PLANTS` and `PLANT_OWED` gain one key each | `main`'s `--selftest` and the `loop definition fixtures` leg, `python -I -c "import sys; sys.path.insert(0, '.'); import loop_lib as l; print(len(l.PLANTS), len(l.PLANT_OWED))"` in `tools/loop/` printing `34 34` at the tip | both gain the same key, so every plant keeps its owed row; the new arm is observed red then green at the close (§7) |
| `main`'s usage line, which joins the `PLANTS` keys | `tools/govkit/usage.toml`'s `script:{prefix}/loop/loop_lib.py` row and its anchor in `help/loop.md` | the row lists flags alone and no flag is added, so its fingerprint does not move |
| `main`'s argv branches | `tools/loop/adopt-loop.sh` and the kit's shipped `loop definition` leg run `--check`; check 53 of `tools/unattended/check-unattended.sh` runs `--grade-site`; `tools/loop/loop_witness.py`'s `READER_PLANTS` runs two computed-witness plants | the new branch is taken only under its own plant's argv, before any definition read |
| a module copied alone | `tools/unattended/cross-component.test.sh` and `tools/roles/adopt-roles.test.sh` copy `loop_lib.py` without the memory-tree kit and run `--check` | no import is added at module scope; the memory-tree kit loads only inside `derive_conf_constants` |
| the module's conf constants | `derive_conf_reads`' `conf constant` kind in `budget.py` and `breakpoints.py`, over `derive_conf_constants('loop_lib.py')`, an empty set at the tip | the tuple, the `PLANTS` description, the `PLANT_OWED` row and both new functions hold no conf file name at module scope (AC4) |
| `derive_conf_rebinds`' global loaders | the same answer | neither new function declares a `global` |
| the symbol tier | `memory/map/generated/symbols.json`, `grep -c '"derive_conf_openers"\|"check_conf_readers_plant"' memory/map/generated/symbols.json` printing 0 at the tip | the regeneration adds both rows; the `codebase-map coverage + freshness` leg reads the result |
| the lexicon offender pin | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 PINNED at the tip | `python tools/lexicon/lexicon.py --suggest <name> --as py.function`, run in this worktree, printed `OK` for both function names, each leading with a declared verb; `.lexicon.conf` declares no `py.constant` cell, so `CONF_ROUTES` is not graded |
| the README function table and plants paragraph | `tools/loop/README.md`, `grep -c "conf-readers-declared\|derive_conf_openers" tools/loop/README.md` printing 0 at the tip; 97 S2 edits the `derive_conf_reads` row above at order 50 | S4 adds a row and a sentence and edits no row 97 writes |
| the help page | `help/loop.md`'s "See a refusal" bullet, `grep -c conf-readers-declared help/loop.md` printing 0 at the tip | S4 adds a sentence naming the case and no command, so the docs leg's command test sees no new span |
| this spec's item and criterion ids | 97 rev-2 cites "99's second case" and "99's check", 100 rev-1 cites the plant in its §3 and AC6, 67's §5 names this unit's argv, and 80's §5 records this unit citing 80 S1, `grep -no "99 [SA]C\?[0-9]*\|99's [a-z]*\|(99)" memory/builds/dDeclaredLoop/spec/*.md` | 97's second case is S3's third, over the members this module binds; the plant keeps its name; the argv is `--selftest`; 80 S1 is read by symbol |
| the edges naming this unit | six bullets, hands-off from 67, 80, 87, 89 and 97 and consumes-from in 100, `grep -n "^- \*\*[a-z-]*\*\* .TOOL-dDeclaredLoop-99. " memory/builds/dDeclaredLoop/spec/*.md` | rev-2 keeps its six mirrored bullets, verbs and targets unchanged |
| the H1 title | the units row of `memory/builds/dDeclaredLoop/README.md`, a generated region; the `After:` line of `memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-99-deviation-991.md` | the dispatcher's index regeneration renders rev-2; the deviation record is history and keeps rev-1's title |
| this spec's positional rows | `memory/project/positional-refs.txt`, `grep -c "dDeclaredLoop-99.md" memory/project/positional-refs.txt` printing 0 | rev-2 cites code by symbol only |
| the siblings at order 50 and 51 | 97 rev-2 builds `CONF_READERS` before this unit; 98 rev-1 writes `budget.py`; 100 rev-1, at order 51, is re-grounded before its builder | this unit writes no file 98 writes, and reads `CONF_READERS` as 97 S1 states it |
| refusal ceilings and families | `tools/memory-tree/check-arms.py#discover` reads tracked `*.sh` files | the pass writes no shell script; `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts, and `tools/loop/` holds no `.families.txt` |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither, and the run lands no decision row ahead of it |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md` | `grep "^watch:" memory/guides/SESSION-KICKOFF.md \| grep -c "tools/loop"` prints 0 |
| the kit version | `KIT_LOOP_VERSION` in `loop_lib.py`, read by `tools/loop/kit.toml`'s `version_from` | `tools/push-main.sh` mints kit versions at landing; the builder writes none |
| the install-prefix ban, the verdict-epoch delegates, subject pins, upgrade steps and help anchors | `tools/check-install-prefix.sh`, `tools/memory-tree/check-verdict-epoch.sh`, every leg's `subject`, `tools/govkit/upgrade_steps.py`, `help/` | the pass writes no install line, leg, step, verb or flag; `check-verdict-epoch.sh` names no loop module |

Order: this unit reads the code units 67, 70, 72, 80, 82, 86 to 90, 92 and 94 built, each CLOSED at the
tip, and `CONF_READERS` as 97 rev-2 S1 builds it at order 50, before this unit. 95 rev-3, at order 49,
and 96 rev-3, at order 50, write no code. 98 builds beside it at order 50, and 100 at order 51.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --fixture --plant conf-readers-declared` runs in `tools/loop/`, it
  exits 0 and prints
  `loop: conf readers declared · 2 opener(s) · read_driver_conf resolve_memory_root_source · outside this module read_design_conf parse_conf`, its count DERIVED.
  Red when: the plant is absent, as at the tip, where the command exits 2 on the usage line.
  figure: 2 and the names are DERIVED from `loop_lib.py` and 97's `CONF_READERS` at observation time.
- **AC2** — When
  `python -I -c "import sys; sys.path.insert(0, '.'); import loop_lib as ll; print(ll.derive_conf_openers('loop_lib.py'))"`
  runs in `tools/loop/`, it prints `['read_driver_conf', 'resolve_memory_root_source']`. The same
  call over the fixture module §4 states, written under the run's scratch directory, prints
  `['read_by_constant', 'read_by_shell', 'read_path_call', 'read_slash']`.
  Red when: the predicate takes a nested `def`, a boundary function, a path built with no open call or
  a conf name outside a path operand, or misses a `/` operand, a `Path` argument, a conf constant or a
  `subprocess` call; at the tip the call ends in an `AttributeError` naming `derive_conf_openers`.
  fixture: the module is written at observation time.
- **AC3** — Take scratch copies of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, and run `python loop_lib.py --fixture --plant conf-readers-declared` in each
  copy's `loop/`. Each staged function is inserted directly above `def main`.
  - gaining `def read_other_conf(tree): return (tree / ".unattended.conf").read_bytes()`, it exits 1
    printing `loop: refused · read_other_conf opens a conf and is in neither CONF_READERS nor CONF_ROUTES`;
  - with `CONF_ROUTES = ()`, it exits 1 printing
    `loop: refused · resolve_memory_root_source opens a conf and is in neither CONF_READERS nor CONF_ROUTES`;
  - with `"resolve_memory_root"` appended to `CONF_ROUTES`, it exits 1 printing
    `loop: refused · resolve_memory_root is in CONF_ROUTES and opens no conf`;
  - with `"read_memory_tree"` appended to `CONF_READERS`, it exits 1 printing
    `loop: refused · read_memory_tree is in CONF_READERS and opens no conf`;
  - with `return []` as the first statement of `derive_conf_openers`, it exits 1 printing
    `loop: refused · no conf opener found in loop_lib.py`;
  - gaining the same reader named `seed_fixture_conf`, it exits 0, because the fixture boundary passes
    over it.
  Red when: a new conf opener in `loop_lib.py` passes undeclared, the report's consequence for id 19,
  or a stale declaration passes.
  fixture: the copies are made at observation time.
- **AC4** — When
  `python -I -c "import sys; sys.path.insert(0, '.'); import loop_lib as ll; print(ll.PLANT_OWED['conf-readers-declared'], any(c in ll.PLANTS['conf-readers-declared'] for c in ('.memory-tree.conf', '.unattended.conf')), ll.CONF_ROUTES, sorted(ll.derive_conf_constants('loop_lib.py')))"`
  runs in `tools/loop/`, it prints
  `(0, 'loop: conf readers declared · ', ' opener(s) · ') False ('resolve_memory_root_source',) []`.
  Red when: the plant has no owed row, so `--selftest` would not run it, or its description or a new
  module constant spells a conf file name, which moves the `conf constant` kind; at the tip the probe
  ends in a `KeyError`.
- **AC5** — In `tools/loop/`, `grep -c conf-readers-declared README.md` prints at least 1 and
  `grep -c "derive_conf_openers(loop_lib_path)" README.md` prints 1. In the repository root,
  `grep -rl conf-readers-declared help/` prints one path, the loop page's, and
  `grep -c '"derive_conf_openers"\|"check_conf_readers_plant"' memory/map/generated/symbols.json`
  prints 2.
  Red when: the docs or the symbol tier do not name the plant and the function.
  figure: each prints 0 at the tip, PINNED 2026-11-17.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's leg this pass keeps green, a leg in `tools/gate-legs.json` on the branch and absent from
main's: `loop definition fixtures`, whose `--selftest` runs the new plant against its `PLANT_OWED` row.
The `loop budget fixtures` and `loop breakpoint fixtures` legs keep their conf-read plants, whose
answers do not move (§5). The `docs` leg reads `help/loop.md`.

New arm: tools/loop/loop_lib.py · covers AC1 AC3 · the conf-readers-declared plant run by --selftest against its PLANT_OWED row, staged with an undeclared opener, an empty CONF_ROUTES and a declared member that opens no conf · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** `**Derived:** PLAY-dClosedLoop-2`,
  rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  RESOLVED (agent, 2026-11-17, delegated): (rung 3). widens: none · relaxes: none
- **F2 — Keep the tuple complete by a derived check, or derive the rule's set directly (id 19)?** (a) a
  plant comparing a syntactic derivation with the declarations both ways; (b) the rule reads the
  derivation and no tuple exists. (b) loses the declared answer, so a predicate miss shrinks the rule
  with no signal. (a) turns a miss in either direction into a named red. Recommendation: (a), S1 and S3.
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none
- **F3 — How does the check hold `resolve_memory_root_source`, which opens the driver's conf to key its
  cache and is the sanctioned route?** (a) a second module tuple, `CONF_ROUTES`, compared both ways
  beside `CONF_READERS`; (b) the plant holds its name as a literal exemption; (c) it joins
  `CONF_READERS`; (d) the open test omits `read_bytes`; (e) the cache keys by file metadata, so the function
  opens nothing. (c) makes the rule grade every call of it in `budget.py` and `breakpoints.py`, the
  route 97 §3 keeps out. (d) misses every reader that uses `read_bytes`. (e) edits a function other
  units own and lets a same-size rewrite within the clock's resolution reuse a stale root. (b) is an
  unnamed second list never checked both ways. (a) names the route once and reds where it goes stale.
  Recommendation: (a), S2.
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none
- **F4 — Which declared members does the third case compare, with two of `CONF_READERS` defined
  outside `loop_lib.py`?** (a) the members this module binds as functions, the rest named on the pass
  line; (b) also a lasting check that each outside member is a function of `design_lib.py` or
  `tree_lib.py`; (c) also derive the openers of those two modules. (c) cannot hold: `parse_conf` parses
  text it is handed and opens nothing, so it would red. (b) checks existence, a different property 97
  AC1 observes once, and loads a second module of another kit per run. Recommendation: (a), S3.
  RESOLVED (agent, 2026-11-17, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-12 spec audit's id 19 (HIGH, item H1,
  shared with ids 1 and 11).
- rev-2 · 2026-11-17 · §1 §2 §3 §4 §5 §6 §7 §8 §10 · S1 S2 S3 S4 AC1 AC2 AC3 AC4 AC5 · re-grounded on the
  code at `branch/unattended-declared-loop-d56bf0` by 2026-11-17-prompt-TOOL-dDeclaredLoop-99-1-spec-writer:
  no `read_tree_conf` under 95 rev-3, and `resolve_memory_root_source` opens a conf, so S2 declares it in
  `CONF_ROUTES` (F3); the stale-declaration case compares only the members this module binds (F4); the
  plant joins `PLANTS` and `PLANT_OWED` for 67 S30's `--selftest`; rev-1's S3 and AC4 settled in §3, 87
  and 89 being CLOSED; S4 and AC5 add the docs and symbol rows; §5's sweep added; the H1 names both
  tuples; the six Edges bullets kept with their payloads re-worded; F1 and F2 re-marked, F3 and F4 added.

## 10. Reuse audit

The seams are `tools/loop/loop_lib.py#derive_conf_constants`, read for the conf-constant operand,
`tools/loop/loop_lib.py#check_conf_name`, the one conf-name predicate, read for every other operand,
`tools/loop/loop_lib.py#derive_fixture_boundary`, read as 80 S1 states it, and the definition plants
`main` runs through `PLANTS` and `PLANT_OWED`, extended by one plant whose helper follows
`tools/loop/loop_lib.py#check_scope_plant`'s shape, a list of refusals that `main` prints. S1's walk is
the `ast` walk shape of `derive_conf_reads`, read one body at a time where that rule reads a module.
`python tools/codebase-map/reuse_lookup.py "derive the functions of a module that build a conf path and open it, compared both ways with a declared tuple"`,
run on the branch tip's archived copy 2026-11-17, ranked `build`, `load_conf`, `build_records`,
`opened`, `parse_conf`, `read_design_conf`, `derive_kit_prefix` and `read_conf` among its seams. Each
reads, parses or builds one thing; none classifies the functions of a module by what they open, so no
existing seam fits S1's predicate itself. The memory-recall query at rev-1 returned the round-12
report's H1, 76's spec, 80's fixture boundary and 82's sketch.

Recall terms used: derive_conf_reads derive_conf_constants check_conf_name derive_fixture_boundary reader call read_driver_conf resolve_memory_root_source parse_conf no-own-conf-read plant PLANT_OWED conf readers tuple CONF_READERS
