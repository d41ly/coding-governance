# TOOL-dDeclaredLoop-117 — the conf-opener derivation reads a conf path passed straight to its open, and every refusal of the `conf-readers-declared` plant is a standing case

**Status:** CLOSED · rev-1 · 2026-11-17 · node a · Tier-2 · base 017b0299 · streams tooling · order 54

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 |
| [2026-11-17-build-TOOL-dDeclaredLoop-1-deviation-1173.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-1-deviation-1173.md) | deviation | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 |
| [2026-11-17-build-TOOL-dDeclaredLoop-100-deviation-1171.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-100-deviation-1171.md) | deviation | TOOL-dDeclaredLoop-100 |
| [2026-11-17-build-TOOL-dDeclaredLoop-100-deviation-1172.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-100-deviation-1172.md) | deviation | TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-99 |
| [2026-11-17-build-TOOL-dDeclaredLoop-117-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-117-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-117-deviation-1174.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-117-deviation-1174.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-117-deviation-1175.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-117-deviation-1175.md) | deviation | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-117-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-117-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-117-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-117-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-117-spec-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-117-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The build's closing diff review converged at round 2. Under the owner's 2026-10-04 rule, quoted in
`tools/unattended/unattended.sh#verb_review`, every finding it confirmed is promoted: round 1's two
HIGH items are `TOOL-dDeclaredLoop-115` and `TOOL-dDeclaredLoop-116`, and this unit is the minors,
batched.

| Record | Item | Grade | Finding | Scope items |
|---|---|---|---|---|
| round 1 | 3 | MEDIUM | 5 | S1, S2 |
| round 1 | 4 | MEDIUM | 6 | S2 |
| round 1 | 5 | LOW | 7 | S4 |
| round 1 | 6 | LOW | 8 | S5 |
| round 2 | 1 | LOW | 1 | S6 |
| round 2 | 2 | LOW | 2 | S6 |

The records are `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md`
and `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md`,
read whole at the branch tip.

The one mechanism is the `conf-readers-declared` plant held to every answer it can give.
`derive_conf_openers` today counts a conf path only as an operand of `/` or an argument of `join`,
`Path` or `PurePath`, so `open(".memory-tree.conf")` and `open(<a conf constant>)` are never derived and
an undeclared reader of either shape passes the plant (item 3). And nothing ever feeds the plant a
module that should be refused, so each of its four refusal arms could go silent with the leg green
(item 4). S1 widens the derivation to the conf path an open call is handed; S2 makes each refusal arm,
and each shape S1 adds, a plant of its own that `--selftest` holds to its owed line.

The four records items are defects in CLOSED specs and in a persisted review record, which are frozen,
so S4 to S6 settle them by deviation records and change no code.

## 2. Scope (IN)

- **S1** — `derive_conf_openers` (`tools/loop/loop_lib.py#derive_conf_openers`) counts a conf path
  wherever an open call is handed one, beside the two places it reads today. A conf path is an
  expression `check_conf_name` answers, a name or attribute naming a member of `derive_conf_constants`'
  answer, or a name the function's own body binds to a conf path. A body binding is the `Name` target of an `Assign`, an `AnnAssign` with a value
  or a walrus whose value is a conf path, read to a fixpoint so a re-bound name carries. The places are:
  an operand of `/`; a positional or keyword argument of a `join`, `Path`, `PurePath`, `open` or
  `parse_conf` call; and the receiver of an `open`, `read_bytes` or `read_text` attribute call. The open
  test, the fixture boundary and the nested-definition rule do not change. The docstring's NOT SEEN list
  names what stays unseen (§4 "The predicate"). Observed by AC1, AC2.
- **S2** — Six plants join `PLANTS` and `PLANT_OWED` in `tools/loop/loop_lib.py`, each named in a new
  module tuple `CONF_PLANTS` beside `SCOPE_PLANTS` together with `conf-readers-declared`. `main` runs
  each the way it runs that plant, over a copy of this file that `write_conf_plant(plant, scratch)`
  writes as `loop_lib.py` into a `tempfile.TemporaryDirectory()` whose life ends with the plant run. The copies and the owed
  lines are §4 "The plants". `conf-readers-declared` keeps reading this file. Observed by AC1, AC3,
  AC4.
- **S3** — The docs follow S1 and S2: the `derive_conf_openers` row of `tools/loop/README.md`'s
  function table, which names S1's places in its words, "a positional or keyword argument of" among
  them, and its plants paragraph, the "See a refusal" bullet of help/loop.md, and
  `memory/map/generated/symbols.json` regenerated for `write_conf_plant`. Each plant description names
  a conf in words and never by its file name. Observed by AC4, AC5.
- **S4** — Round 1 item 5: a deviation record corrects unit 100's settled-items row S3, which calls
  `parse_conf` a `TREE_LIB_SYMBOLS` member. Its text is §4 "The records", record 1171. Observed by AC6.
- **S5** — Round 1 item 6: one deviation record answers the ten hands-off edges into unit 100, eight
  of which name a restatement or a re-run unit 100 rev-2 never made, 99's AC6 edge among them (§8 F4).
  Its text is §4 "The records", record 1172. Observed by AC6.
- **S6** — Round 2 items 1 and 2: one deviation record states the promote disposition the round-1
  record contradicts, and pins every bare `path:line` cite of that record to its blob at the reviewed
  head bada76713. Its text is §4 "The records", record 1173. Observed by AC6.

## 3. Non-goals (OUT)

- No edit to a CLOSED spec, to either review record or to `memory/DECISIONS.md`. Units 95, 99 and 100
  are CLOSED and frozen, and a review record is persisted as written; S4 to S6 are records beside them.
- No change to `CONF_READERS`, `CONF_ROUTES`, `check_conf_readers_plant`'s refusals or their order,
  or `derive_conf_reads`. The live answer stays `read_driver_conf` and `resolve_memory_root_source`
  (§4 Evidence, E1).
- The builds-root readers that skip `resolve_memory_root`, `read_builds_dir` in this file among them:
  round 1 item 2, `TOOL-dDeclaredLoop-116`, which builds at order 53, before this unit.
- The left-shift gates the two rounds propose beside their fixes, each a gate of its own and so a unit
  of its own (`doc.build-method#m2-the-spec-set-decompose-detect-classify-act`): the `harness arms (fail branches armed or pinned)` leg counting python
  refusal arms (round 1 item 4); a spec-tokens arm resolving a settled row's claimed membership (item
  5); a check refusing an edge that cites a criterion its target no longer holds (item 6); the exit rule
  in the synthesizer's task with a tier2-review fixture (round 2 item 1); and a hygiene check refusing an
  unpinned code cite in a review record (round 2 item 2).
- What S1 leaves unseen, listed in its docstring: a path built in one function and opened in another, a
  name composed at run time, `subprocess` under another name, and a path carried through an attribute,
  a subscript or a container.

### Edges

- **consumes-from** external — `derive_conf_openers`, `check_conf_readers_plant` and the `conf-readers-declared` plant, landed by TOOL-dDeclaredLoop-99 (CLOSED); without them there is no derivation to widen and no plant to hold to its refusals
- **hands-off** external — the five left-shift gates §3 lists, each a separate mechanism, filed as asks by the dispatcher

## 4. Design

### Evidence

Every reading below ran on `git archive 017b0299` of `branch/unattended-declared-loop-d56bf0`, the
branch tip, extracted under the writer's scratch directory, with Python 3.15.2. This worktree is cut
from main, which lacks the loop kit, so no code claim here was read on main.

| Id | What was measured | Reading | Status |
|---|---|---|---|
| E1 | `python loop_lib.py --fixture --plant conf-readers-declared` in `tools/loop/` | exit 0, `2 opener(s) · read_driver_conf resolve_memory_root_source · outside this module read_design_conf parse_conf`, 0.44 s real | PINNED 2026-11-17 |
| E2 | S1's predicate, prototyped, over `loop_lib.py` | `read_driver_conf`, `resolve_memory_root_source`, the same as E1 | PINNED 2026-11-17 |
| E3 | the review's class fix, any node of the body a conf path, over `loop_lib.py` | also `derive_conf_reads`, whose `confs` tuple names both confs and whose `read_text` reads a module | PINNED 2026-11-17 |
| E4 | S1's predicate over the AC2 module | the six shapes, and neither negative | PINNED 2026-11-17 |
| E5 | the tip's predicate over the AC2 module | an empty list | PINNED 2026-11-17 |
| E6 | the six copies of §4 "The plants", the plant's comparison run over each with S1's predicate | each owed line, one refusal per copy but `conf-openers-none`, which also names both declared members | PINNED 2026-11-17 |
| E7 | `ast.unparse` of the whole file, the predicate run over it | E1's answer | PINNED 2026-11-17 |
| E8 | the three record texts of §4 "The records" read by `tools/memory-tree/deviation_join.py#read_record` | no malformed field in any | PINNED 2026-11-17 |

E3 is why S1 does not take the review's widest form: the live plant would refuse `derive_conf_reads`,
which opens no conf. E5 is the finding's consequence, every new shape passing undeclared.

### The predicate

`derive_conf_openers` walks each module-level `def` and `async def` outside `derive_fixture_boundary`,
its own body only, as today. Per function:

```
conf(o)   = check_conf_name(o)
          or o is a Name whose id is in consts or in locals
          or o is an Attribute whose attr is in consts
locals    = the Name targets of each Assign, AnnAssign with a value, or NamedExpr in the body
            whose value satisfies conf(), repeated until the set stops growing
places    = operands of `/`
          + positional and keyword values of calls whose callee is join, Path, PurePath, open or parse_conf
          + receivers of attribute calls named open, read_bytes or read_text
builds    = any(conf(o) for o in places)
opens     = unchanged: a call of parse_conf, open, read_bytes or read_text, or of an attribute of `subprocess`
```

A callee is a name by its id and an attribute by its attr, as today. The four shapes
TOOL-dDeclaredLoop-99 AC2 derives stay derived, since each sits in a place the old rule read. The NOT SEEN sentence of the
docstring becomes: a path built in one function and opened in another; a conf name composed at run
time; `subprocess` reached under another name; and a path carried through an attribute, a subscript,
a container, or a conf-path name wrapped in a call that is none of the five callees above, such as
`open(str(p))`.

### The plants

Each copy is the text of this file with one change. Three append a function that opens a conf and is
declared nowhere; three break the module so a refusal arm must fire.

| Plant | The copy | Owed exit, opening, needle |
|---|---|---|
| `conf-opener-literal` | appends `def read_literal_conf(): return open(".memory-tree.conf").read()` | 1 · `loop: refused · ` · `read_literal_conf opens a conf and is in neither CONF_READERS nor CONF_ROUTES` |
| `conf-opener-constant` | appends `SEED_CONF = ".unattended.conf"` and `def read_constant_conf(): return open(SEED_CONF).read()` | 1 · `loop: refused · ` · `read_constant_conf opens a conf and is in neither CONF_READERS nor CONF_ROUTES` |
| `conf-opener-local` | appends `def read_local_conf():` binding `name = ".memory-tree.conf"` and returning `open(name).read()` | 1 · `loop: refused · ` · `read_local_conf opens a conf and is in neither CONF_READERS nor CONF_ROUTES` |
| `conf-route-opens-none` | `resolve_memory_root_source`'s body reduced to `return None`, through `ast` and `ast.unparse` | 1 · `loop: refused · ` · `resolve_memory_root_source is in CONF_ROUTES and opens no conf` |
| `conf-openers-none` | the bodies of `read_driver_conf` and `resolve_memory_root_source` reduced the same way | 1 · `loop: refused · ` · `no conf opener found in loop_lib.py` |
| `conf-module-unparsable` | appends `def read_broken_conf(:` | 1 · `loop: refused · ` · `cannot be read as the conf constants' module` |

`write_conf_plant` holds the appended texts in its own body, never at module scope. Its name carries
the token `plant`, so `derive_fixture_boundary` takes it and neither `derive_conf_reads` nor S1 reads
its conf names; it declares no `global`, so `derive_conf_rebinds` answers nothing for it; and a module
constant holding a conf file name would join `derive_conf_constants`' answer, which stays empty
(AC4). It reads this file and writes the copy with `encoding="utf-8"`. The `conf-route-opens-none`
copy keeps `read_driver_conf`, so exactly the third arm fires; the third arm reads the live module's
`globals()`, as TOOL-dDeclaredLoop-99 S3 built it, which is why both body cases change a body and never
a tuple.

`main`'s branch becomes `if plant in CONF_PLANTS:`, printing the fixture line, running
`check_conf_readers_plant` over this file for `conf-readers-declared` and over the copy otherwise,
printing each refusal and exiting 1 on any, else 0. `--selftest` takes the six through its existing
`PLANTS` loop and `run_selftest_cases`, each held to its owed line by name.

### The records

Each is a `deviation` record in `memory/builds/dDeclaredLoop/build/`, named
`<pass date>-build-<unit>-deviation-<n>.md` and written by hand, the kind having no door in
`tools/memory-tree/build_records.py#write_record`'s callers. The n values 1171 to 1173 sit above the
build's highest, 1002, PINNED at the tip. Each serves its departing unit, the units whose readers need
it, and this one. E8 read all three texts.

Record 1171, under unit 100:

```
# TOOL-dDeclaredLoop-100 deviation 1171 — the settled-items row S3 names `parse_conf` a `TREE_LIB_SYMBOLS` member, which it is not

**Serves:** deviation TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-117

- **Departs from:** `TOOL-dDeclaredLoop-100@rev-2` [§3 S3]
- **Hand-off:** code-to-record
- **Before:** row S3 of the settled-items table says `TREE_LIB_SYMBOLS` holds two names and 95 rev-3 §3 settles `parse_conf` as a member (its S1).
- **After:** `TREE_LIB_SYMBOLS` holds two names, `derive_docstring_ids` and `derive_constant_charges`, and 95 rev-3 §3 settles `parse_conf` as no member of it (its S1); `parse_conf` is a member of `CONF_READERS`, as row S21 of the same table says.
- **Cause:** review finding
- **Reason:** the closing diff review's round 1 confirmed row S3 contradicting row S21, unit 95's §3 row S1 and the tuple in `tools/loop/loop_lib.py` (its item 5, finding 7); the spec is CLOSED and frozen, so this record carries the correction and the spec's text stays as landed.
- **Evidence:** `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md`, item 5; `tools/loop/loop_lib.py#TREE_LIB_SYMBOLS` and `tools/loop/loop_lib.py#CONF_READERS`; row S1 of the §3 table of `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-95.md`.
- **Risk:** editorial
- **Approver:** author, the builder pass of TOOL-dDeclaredLoop-117, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1
```

Record 1172, under unit 100:

```
# TOOL-dDeclaredLoop-100 deviation 1172 — the hands-off edges into this unit name restatements and re-runs it never made

**Serves:** deviation TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-117

- **Departs from:** `TOOL-dDeclaredLoop-100@rev-2` [the ten hands-off edges into it]
- **Hand-off:** code-to-record
- **Before:** the hands-off edges into `TOOL-dDeclaredLoop-100` from units 41, 60, 64, 72, 90, 92, 94, 95, 96 and 99 say that unit restates their text, onto `read_tree_conf` for 60 and 64, re-runs 72's `confs-disagree` plant, re-runs 90's AC4 and AC5, reads 95's and 96's settled items at its re-ground, and re-runs 99's `conf-readers-declared` plant by an AC6.
- **After:** `TOOL-dDeclaredLoop-100` rev-2 wrote nothing under `tools/`, restated no sibling spec and re-ran no plant: it read 95's and 96's settled items, settled the ids each edge names in the rows of its §3 table and closed on AC22 alone, the collection 90 AC4 states; the plants stand where they run, `conf-readers-declared` under the `loop definition fixtures` leg and `confs-disagree` under the `loop budget fixtures` and `loop breakpoint fixtures` legs.
- **Cause:** review finding
- **Reason:** the closing diff review's round 1 confirmed 99's edge claiming a re-run that never happened, an empty population read as coverage (its item 6, finding 8), and named the other edges into the same unit as the same defect; each spec is CLOSED and frozen, so one record answers every edge and their texts stay as landed.
- **Evidence:** `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md`, item 6; §1 to §3 of `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-100.md`, which hold S22 and AC22 alone and write nothing under `tools/`; the pass commit e8307cd60.
- **Risk:** editorial
- **Approver:** author, the builder pass of TOOL-dDeclaredLoop-117, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1
```

Record 1173, under unit 1, the id the review records are named by:

```
# TOOL-dDeclaredLoop-1 deviation 1173 — the closing review's round-1 record states a fix-first exit and leaves its code cites unpinned

**Serves:** deviation TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117

- **Departs from:** dDeclaredLoop [the closing diff review's round-1 record]
- **Hand-off:** code-to-record
- **Before:** the round-1 record says every item is owed a fix, or a close deviation for the records items, before the close's merge bar and RED-first observations run, and it cites code by bare `path:line` beside its pinned sites.
- **After:** every item the round confirmed is promoted at the closing review's exit under the owner's 2026-10-04 rule `verb_review` quotes, item 1 to `TOOL-dDeclaredLoop-115`, item 2 to `TOOL-dDeclaredLoop-116` and items 3 to 6 batched to `TOOL-dDeclaredLoop-117`; each bare cite reads at the reviewed head bada76713, where the blobs are `help/policy.md@1482cecf`, `tools/loop/upstream.py@43147593`, `tools/loop/loop_lib.py@637ea901`, `tools/loop/adapt.py@1c930e56`, `tools/loop/guard.py@13a73d3e`, `tools/loop/breakpoints.py@790d996d`, `tools/loop/budget.py@ae3163cf`, `tools/memory-tree/build_records.py@e689f3e9`, `tools/loop/loop_parents.py@d078c52c`, `tools/loop/position.py@87072a03`, the unit 100 spec `@96299153` and the unit 99 spec `@c4913160`, so item 2's fourth site is `tools/loop/upstream.py@43147593:297`.
- **Cause:** review finding
- **Reason:** the closing diff review's round 2 confirmed both defects in the round-1 record (its items 1 and 2); a review record is persisted as written and never edited by hand, so this record carries the correction.
- **Evidence:** `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md`, items 1 and 2; the rescope add rows for `TOOL-dDeclaredLoop-115`, `TOOL-dDeclaredLoop-116` and `TOOL-dDeclaredLoop-117` in `memory/builds/dDeclaredLoop/RUN.md`; `tools/unattended/unattended.sh#verb_review`.
- **Risk:** editorial
- **Approver:** author, the builder pass of TOOL-dDeclaredLoop-117, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2
```

The blobs in record 1173 were read with `git ls-tree -r bada76713` over the twelve paths, and each
cited line was read at its blob: `tools/loop/upstream.py@43147593:297` is the `memory_root =
(read_design_conf(root)...` line, and `tools/memory-tree/build_records.py@e689f3e9:249` is the
`memory_root = (conf.get("MEMORY_ROOT")...` line, the one round 1 cites bare under that file's
name. The review cites the two specs as written at bada76713, rows the tip has since moved: 100's S3
row is line 80 at `@96299153`, and 99's edge line 126 at `@c4913160`.

### Inventory

| Identifier | Kind | Where | Naming |
|---|---|---|---|
| `write_conf_plant` | function | `tools/loop/loop_lib.py` | cell `py.function`: `lexicon.py --suggest write_conf_plant --as py.function` answered OK, leading verb `write` |
| `CONF_PLANTS` | module tuple | `tools/loop/loop_lib.py` | none: `.lexicon.conf` declares no `py.constant` cell at the tip or on main |
| six plant names, §4 "The plants" | `PLANTS` keys | `tools/loop/loop_lib.py` | none |
| records 1171, 1172 and 1173 | deviation records | `memory/builds/dDeclaredLoop/build/` | the typed name `<date>-build-<unit id>-deviation-<n>.md` |

The appended functions and `SEED_CONF` live only in the scratch copies' text and are not minted names
of the tree.

### Files touched (estimate)

- `tools/loop/loop_lib.py`: `derive_conf_openers`, `write_conf_plant`, `CONF_PLANTS`, `PLANTS`,
  `PLANT_OWED`, `main`
- `tools/loop/README.md`: the `derive_conf_openers` row and the plants paragraph
- help/loop.md, the loop help page, which main does not track: the "See a refusal" bullet
- `memory/map/generated/symbols.json`: regenerated (§5 "The sweep")
- `memory/builds/dDeclaredLoop/build/`: the three records

### Alternatives rejected

- **Any expression node in the body is a conf path, the review's class fix (§8 F2 (a)).** E3: it derives
  `derive_conf_reads`, which reads module text and holds both conf names in a tuple, so the live plant
  would refuse a function that opens no conf.
- **Only the open call's own argument, the finder's fix (§8 F2 (c)).** It misses the local binding and
  the `read_text` receiver of a joined path, two of AC2's six shapes.
- **One plant iterating every copy, one owed row (§8 F3 (b)).** `PLANT_OWED` holds one needle a plant,
  so the arms after the first could fall silent behind it.
- **The copies held in a module dict.** A module-level string naming a conf file joins
  `derive_conf_constants`' answer, which `derive_conf_reads` grades in `budget.py` and
  `breakpoints.py`.
- **The copy written through `tools/loop/loop_witness.py#write_fixture_files`.** One file and one call;
  importing that module inside the plant adds an edge for a single `write_text`.

## 5. Production-readiness checklist

- security — the plant guards the no-own-conf-read rule's reader set: S1 closes the shape an undeclared
  reader would most plainly take. Each copy is written under the host temp directory, removed after,
  and never imported or run; only `ast` reads it. Nothing reads or writes a conf.
- perf / scale — six plant runs join `--selftest`, each one `derive_conf_constants`, one `ast.parse`
  and one file write, near E1's 0.44 s, PINNED 2026-11-17: some 3 s (PINNED estimate) against the
  `tools/run-gates/selftest-budgets.txt` row's 33 s and the leg's 120 s ceiling, both PINNED at the tip.
  S1 adds one fixpoint per function over its own body.
- error / empty / loading states — the empty answer, the missing or unparsable module and a memory-tree
  kit that does not load are each one refusal, exit 1, as today; two of them now have standing plants.
  A body binding no conf path leaves the locals empty.
- observability — each new plant prints the fixture line and its refusal; `--selftest` prints one PASS
  or FAIL line per plant naming it.
- risks — S1 over-matches on the closed side, as TOOL-dDeclaredLoop-99 recorded: a body binding a conf
  name and opening any other file through that name is derived, and the owner declares or restructures
  it. E2 shows no such function at the tip. `TOOL-dDeclaredLoop-116` writes `tools/loop/loop_lib.py` at
  order 53; if it adds a function that opens a conf it declares it there, and this pass re-reads E1's
  answer over the bytes it leaves (AC2). The records are editorial and move no verdict.
- testing — AC1 to AC6: plant runs, a predicate probe over a written module, staged breaks in scratch
  copies, greps and a record read.
- migration — none: no stored data or row shape moves, and the records are additive.
- user docs — help/loop.md's "See a refusal" bullet names the six cases (S3); no verb or flag is
  added, so no usage row or help anchor moves.

### The sweep

Each count is DERIVED by the command beside it, run on the tip's archived copy unless the row says
otherwise; the figure beside it is that reading, PINNED 2026-11-17.

| What moves | Readers, pins and populations | What keeps each green |
|---|---|---|
| `derive_conf_openers`' answer | `check_conf_readers_plant`, its one caller, and the README row, `grep -rn derive_conf_openers tools help --include=*.py --include=*.md` printing the definition, `check_conf_readers_plant`'s docstring and call, and two README lines, no other | E2: the live answer does not move, so `conf-readers-declared` keeps exit 0 and its pass line (AC2) |
| `PLANTS` and `PLANT_OWED` gain six keys each | `main`'s `--selftest` and the `loop definition fixtures` leg; `python -I -c "import sys; sys.path.insert(0, '.'); import loop_lib as l; print(len(l.PLANTS), len(l.PLANT_OWED))"` in `tools/loop/` prints `35 35` at the tip | both gain the same keys, so every plant keeps its owed row; unit 116's plants, if any, sit beside them |
| `main`'s usage line, which joins the `PLANTS` keys | the `script:{prefix}/loop/loop_lib.py` row of `tools/govkit/usage.toml` and its anchor in help/loop.md, fingerprint `a3a33b34` at the tip | the row lists flags alone and no flag is added |
| `main`'s plant branch | `tools/loop/adopt-loop.sh --check`, check 53's `--grade-site` and `tools/loop/loop_witness.py`'s `READER_PLANTS` take other argv; `grep -rn "PLANTS\|PLANT_OWED" tools --include=*.py --include=*.sh` finds no reader outside `tools/loop/loop_lib.py` | the new branch is taken only under the six plant names |
| a module copied alone | `tools/unattended/cross-component.test.sh` and `tools/roles/adopt-roles.test.sh` copy `loop_lib.py` without the memory-tree kit and run `--check` | no import moves to module scope; `ast` and `tempfile` are imported inside the functions or already at the top |
| the module's conf constants | `derive_conf_reads`' `conf constant` kind in `budget.py` and `breakpoints.py`, over `derive_conf_constants('loop_lib.py')`, an empty set at the tip | `CONF_PLANTS`, the six descriptions and owed rows hold no conf file name, and the appended texts sit inside `write_conf_plant` (AC4) |
| the symbol tier | `memory/map/generated/symbols.json`, `grep -c '"id": "write_conf_plant"' memory/map/generated/symbols.json` printing 0 at the tip; module tuples carry no row, `grep -c '"id": "SCOPE_PLANTS"'` printing 0 | the regeneration, `python tools/codebase-map/gen_map.py --write`, adds one row; the `codebase-map coverage + freshness` leg reads it |
| the lexicon offender pin | `VERB_OFFENDER_PIN` in `.lexicon.conf`, 1215 at the tip | `write_conf_plant` leads with a declared verb (§4 Inventory); the planted names are string text |
| text IO | the `encoding posture (text IO names its encoding)` leg; `memory/project/encoding-posture-sites.txt` holds no `tools/loop/loop_lib.py` row | `write_conf_plant`'s read and write each name `encoding="utf-8"` |
| the README | `tools/loop/README.md`, `grep -c "derive_conf_openers(loop_lib_path)" README.md` printing 1 and `grep -c "conf-opener-literal" README.md` printing 0 at the tip; its function table carries no plant helper, `grep -c "write_loop_plant\|check_scope_plant" README.md` printing 0 | S3 edits the one row and the paragraph and adds no row |
| the help page | help/loop.md, `grep -rl conf-readers-declared help/` printing that one path at the tip; the `docs` and `help page commands` legs read it | S3 adds a sentence naming the cases and no command span |
| the refusal census and families | `tools/memory-tree/check-arms.py#discover` reads tracked `*.sh` only; `REFUSAL_CEILINGS` in `.memory-tree.conf` names two `tools/unattended/` scripts; `find tools/loop -name "*.families.txt"` prints nothing | the pass writes no shell script |
| shared records | `SHARED_RECORDS` in `.unattended.conf`: `memory/DECISIONS.md` and `memory/project/readme-contract.txt` | the pass writes neither |
| the deviation population | `tools/memory-tree/deviation_join.py#read_records` over `memory/builds/*/build/*-deviation-*.md`; `ls memory/builds/dDeclaredLoop/build \| grep -o "deviation-[0-9]*" \| sort -t- -k2 -n \| tail -1` printing `deviation-1002` | n 1171 to 1173 are unused; each record parses (E8); none departs from a clause id, so the as-built view's clause rows do not move; a record joining no departure is no finding |
| the records regions | the `<!-- gen:spec-records -->` regions of units 1, 41, 60, 64, 72, 90, 92, 94, 95, 96, 99, 100, 115, 116 and 117 | the dispatcher's index regeneration renders the new rows; no text outside a region moves |
| the record bindings | check 21 and `RECORD_UNBOUND_PIN`; every Serves id resolves to a spec H1 | each record carries a bound Serves line, so the unbound count does not move; 115 and 116 are specced at orders 52 and 53 |
| the kickoff manifest | the `watch:` line of `memory/guides/SESSION-KICKOFF.md` | it names none of §4's paths |
| the kit version | `tools/loop/kit.toml`'s `version_from` | `tools/push-main.sh` mints kit versions at landing; the builder writes none |

Order: `TOOL-dDeclaredLoop-115` builds at order 52 and writes `tools/loop/guard.py`;
`TOOL-dDeclaredLoop-116` builds at order 53 and writes `tools/loop/loop_lib.py` among others. This
unit builds at order 54 over the bytes both leave, re-deriving every count above at its pass.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --fixture --plant <case>` runs in `tools/loop/` for each of
  `conf-opener-literal`, `conf-opener-constant`, `conf-opener-local`, `conf-route-opens-none`,
  `conf-openers-none` and `conf-module-unparsable`, it exits 1 and prints the owed line of §4 "The
  plants"; and `--plant conf-readers-declared` still exits 0 with its pass line.
  Red when: a case is absent, as at the tip, where each exits 2 on the usage line; or, with
  `derive_conf_openers` restored to the tip's bytes, the three opener cases exit 0 printing the pass
  line, the review's consequence for item 3.
- **AC2** — When
  `python -I -c "import sys; sys.path.insert(0, '.'); import loop_lib as ll; print(ll.derive_conf_openers('loop_lib.py'))"`
  runs in `tools/loop/`, it prints `['read_driver_conf', 'resolve_memory_root_source']`, or that list
  with any opener unit 116 declared; and the same call over a module written under the run's scratch
  directory holding §4's shapes prints
  `['read_constant', 'read_keyword', 'read_literal', 'read_local', 'read_rebound', 'read_receiver']`.
  That module binds `SEED = ".unattended.conf"` and defines `read_literal`, `open(".memory-tree.conf")`;
  `read_keyword`, `open(file=".unattended.conf")`; `read_constant`, `open(SEED)`; `read_local`, a local
  bound to the name and opened; `read_rebound`, a local re-bound to a second and opened;
  `read_receiver(root)`, `root.joinpath(".unattended.conf")` bound and `read_text` called on it;
  `list_conf_names(path)`, both names in a tuple and `open(path)`; `seed_fixture_conf`, the literal
  open; and `name_conf`, a local bound to the name and never opened.
  Red when: the predicate takes `list_conf_names`, `seed_fixture_conf` or `name_conf`, or misses one of
  the six; at the tip the second call prints `[]` (E5).
  fixture: the module is written at observation time.
- **AC3** — Take scratch copies of `tools/loop/`, `tools/lib/` and `tools/memory-tree/` under the run's
  scratch directory, stage one break in `check_conf_readers_plant` in each, and run
  `python loop_lib.py --fixture --plant <case>` in the copy's `loop/`:
  - with the `in neither CONF_READERS nor CONF_ROUTES` refusals left out, `conf-opener-literal` exits 0
    printing the pass line;
  - with the `no conf opener found` refusal left out, `conf-openers-none` prints no line naming it;
  - with the `opens no conf` refusals left out, `conf-route-opens-none` exits 0 printing the pass line;
  - with the `except LoopError` clause left out, `conf-module-unparsable` ends in a traceback and prints
    no `loop: refused · ` line.
  Red when: a break leaves its case's owed line printed, so the case cannot see its arm go silent.
  fixture: the copies are made at observation time.
- **AC4** — When
  `python -I -c "import sys; sys.path.insert(0, '.'); import loop_lib as ll; c = ll.CONF_PLANTS; print(len(c), all(p in ll.PLANTS and p in ll.PLANT_OWED for p in c), any(n in ll.PLANTS[p] for p in c for n in ('.memory-tree.conf', '.unattended.conf')), sorted(ll.derive_conf_constants('loop_lib.py')))"`
  runs in `tools/loop/`, it prints `7 True False []`.
  Red when: a plant has no owed row, so `--selftest` would not hold it, or a description or a module
  binding spells a conf file name, which moves the `conf constant` kind.
  figure: 7 is PINNED, `conf-readers-declared` and the six.
- **AC5** — In `tools/loop/`, `grep -c "conf-opener-literal" README.md` prints at least 1 and
  `grep -c "positional or keyword argument of" README.md` prints 1; `grep -rl "conf-module-unparsable" help/`
  in the repository root prints one path, the loop page's; `grep -c '"id": "write_conf_plant"' memory/map/generated/symbols.json`
  prints 1; and `python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import loop_lib as ll; print('a subscript' in ll.derive_conf_openers.__doc__)"`
  prints `True`.
  Red when: the README, the help page, the symbol tier or the NOT SEEN list does not follow S1 and S2.
  figure: at the tip each grep finds nothing and the probe prints `False`, PINNED 2026-11-17.
- **AC6** — When
  `python -I -c "import sys, pathlib; sys.path.insert(0, 'tools/memory-tree'); import deviation_join as d; [print(p.name, d.read_record(p.as_posix(), p.read_text(encoding='utf-8'))['malformed']) for p in sorted(pathlib.Path('memory/builds/dDeclaredLoop/build').glob('*-deviation-117[123].md'))]"`
  runs in the repository root, it prints three rows, each ending `[]`; and
  `grep -l "CONF_READERS" memory/builds/dDeclaredLoop/build/*-deviation-1171.md`,
  `grep -c "TOOL-dDeclaredLoop-99 " memory/builds/dDeclaredLoop/build/*-deviation-1172.md` and
  `grep -c "upstream.py@43147593:297" memory/builds/dDeclaredLoop/build/*-deviation-1173.md` each find
  the record.
  Red when: a record is absent or malformed, an `After:` holding a `|` among the cases, or one names
  neither the correction nor the pin its item asks.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `docs` · `help page commands` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's leg this pass keeps green, a leg in `tools/gate-legs.json` on the branch and absent from
main's: `loop definition fixtures`, whose `--selftest` runs the six new plants against their
`PLANT_OWED` rows. The `loop budget fixtures` and `loop breakpoint fixtures` legs keep their conf-read
plants, whose answers do not move. The deviation join, hosted in `tools/memory-tree/routed_commits.py`
under its `report` policy, reads the three records and lists them, never refusing.

New arm: tools/loop/loop_lib.py · covers AC1 AC3 · the six conf plants run by --selftest against their PLANT_OWED rows, red with derive_conf_openers at the tip's bytes, where the three opener cases exit 0, and with each refusal arm of check_conf_readers_plant left out in turn · none, unless the leg's first reading passes the 33 PINNED s budget row, which is then re-priced in the same commit

What the arm does not check, stated so a green is not read as more. It grades shapes S1 names and no
other: the §3 blind spots pass it undeclared. Each opener case appends one function, so it shows the
derivation sees that shape in a body by itself, not inside every other construct. The body cases
grade the arms against the declared members this module binds; a member defined in another kit stays
named on the pass line and unchecked. And the arm runs over copies of this file only: no other loop
module's conf reads are its concern.

## 8. Open questions

- **F1 — Which binding line does a unit the closing diff review promoted carry?** (a)
  `**Derived:** PLAY-dClosedLoop-2`, the line the build's promoted units carry, 99 and 100 among them,
  and the closing-review promotions of `dGroundRules`; (b) `**Derived:** TOOL-dDeclaredLoop-99`, the
  unit whose plant this repairs, as 112 carries the unit it repairs. 112 was an owner rescope repairing
  one unit, not a promotion. Recommendation (a).
  RESOLVED (agent, 2026-11-17, delegated): (a), rung 3: a promoted finding derives from the chain row the build serves, as every promoted unit of this build records
  widens: none · relaxes: none
- **F2 — How far does the derivation widen (item 3)?** (a) any expression node of the body that is a
  conf path, the review's class fix; (b) the conf path an open call is handed, as an argument, a keyword
  or a receiver, with body bindings followed; (c) only the open call's own positional argument, the
  finder's fix. (a) over-matches at the tip (E3) and reds the live plant. (c) misses two of AC2's
  shapes. Recommendation (b), S1.
  RESOLVED (agent, 2026-11-17, delegated): (b), rung 3: it sees every shape the review planted and the live answer does not move
  widens: none · relaxes: none
- **F3 — Where do the standing cases live (item 4)?** (a) six plants in `PLANTS` and `PLANT_OWED`, run
  by the existing `--selftest` loop; (b) one plant iterating every copy, held to one owed row; (c) a
  case list of its own outside `PLANTS`. (b) holds one needle, so the arms after the first can fall
  silent behind it. (c) is a second selftest loop beside the one 67 S30 built. Recommendation (a), S2.
  RESOLVED (agent, 2026-11-17, delegated): (a), rung 2: the plants and their owed rows are the seam the leg already runs, each case failing by its own name
  widens: none · relaxes: none
- **F4 — Do the records items settle the cited instance or the class?** (a) the instance: item 6's
  record answers 99's edge alone and round 2 item 2's pins line 65 alone; (b) the class the skeptic
  named: item 6's record answers the ten edges into unit 100, and round 2 item 2's pins every bare cite
  of the round-1 record. Both reviews judged the instance fixes INSTANCE-ONLY, and the class costs one
  record each, not more. Recommendation (b), S5 and S6.
  RESOLVED (agent, 2026-11-17, delegated): (b), rung 3: one record per defect class reaches every reader of the stale text at the cost of the instance
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-17 · initial draft, from the writer's handoff
  2026-11-17-prompt-TOOL-dDeclaredLoop-117-1-spec-writer, the closing diff review's rounds 1 and 2 read
  whole at `branch/unattended-declared-loop-d56bf0` 017b0299.

## 10. Reuse audit

The seams are `tools/loop/loop_lib.py#derive_conf_openers`, extended in place by S1 and still reading
`tools/loop/loop_lib.py#check_conf_name` and `tools/loop/loop_lib.py#derive_conf_constants` as its
operands' tests, and the definition plants `main` runs through `PLANTS`, `PLANT_OWED` and
`tools/loop/loop_lib.py#run_selftest_cases`, extended by six rows and one helper in the shape of
`tools/loop/loop_lib.py#write_loop_plant`, with a plant tuple beside `SCOPE_PLANTS`. The records reuse
the deviation grammar `tools/memory-tree/deviation_join.py#read_record` grades, in the shape of the
build's records 991, 1001 and 1002.
`python tools/codebase-map/reuse_lookup.py "write a scratch copy of a module with one function planted or emptied and run a plant's refusals over it"`,
run on the tip's archived copy 2026-11-17, ranked `run`, `write`, `write_text`, `Refusal`, `scratch`,
`run_selftest_cases`, `write_fixture_files` and `build_scratch_tree` first. `run_selftest_cases` is the
seam above; `write_fixture_files` writes a tree of files and is rejected in §4 for one file; none
writes a mutated copy of a module, so no existing seam fits `write_conf_plant` itself.

Recall terms used: derive_conf_openers check_conf_readers_plant conf-readers-declared PLANT_OWED write_loop_plant run_selftest_cases scratch copy refusal arm conf constant deviation record code-to-record
