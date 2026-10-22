# TOOL-dTrueNorth-32 — the round-3 closing diff review's minors: one attribute read, a whole bullet, every constant charged, each pathspec probed, and an environment hold the parity scan reads as none

**Status:** CLOSED · rev-1 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 15

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-32-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-32-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md](../build/2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md) | journal | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 TOOL-dTrueNorth-31 TOOL-dTrueNorth-33 |
| [2026-10-22-build-TOOL-dTrueNorth-32-deviation-35.md](../build/2026-10-22-build-TOOL-dTrueNorth-32-deviation-35.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-32-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-32-build-brief.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-32-1-spec-writer.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-32-1-spec-writer.md) | journal | — |
| [2026-10-22-prompt-TOOL-dTrueNorth-32-spec-brief.md](../prompts/2026-10-22-prompt-TOOL-dTrueNorth-32-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 closing diff review of dTrueNorth
(`memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-31-closing-diff-review-round3.md`)
exited CLEAN WITH FIXES with 16 confirmed findings in 14 items and no blocker or high. Beside it, at
`3c4271e8f` the memory-hygiene self-test reds one arm unit 31 caused: the conf-example parity scan reads
the merge-guard arm's `GIT_CONFIG_GLOBAL` read as a conf key the example does not declare. This unit is
the one batch BUILD-METHOD M4 makes of them, one scope item per review item and one for the red. Each
takes the fix the review's skeptic judged sound, and for findings 6, 11, 13 and 16 the skeptic's
corrected fix, except where the item says why its variant is better. Where a round-2 fix proved
incomplete (M1, M2, M4, M5), the item closes the class the review names, not the one instance. By the
owner's instruction of 2026-10-22
(`memory/builds/dTrueNorth/prompts/2026-10-22-prompt-TOOL-dTrueNorth-1-owner-no-more-rounds.md`), no
closing review round follows this unit: it is built because it also clears the hygiene red, and its
suites run once, standalone, at the close. Every line cited below was read at `2057f2272`, and every
reading marked as measured was observed there.

| Review item | Severity | Finding ids | Scope item | Criterion |
|---|---|---|---|---|
| M1 | MEDIUM | 2 | S1 | AC1 |
| M2 | MEDIUM | 4 | S2 | AC2 |
| M3 | MEDIUM | 11 | S3 | AC3 |
| M4 | MEDIUM | 14 | S4 | AC4 |
| M5 | MEDIUM | 10 | S5 | AC5 |
| M6 | MEDIUM | 15, 19 | S6 | AC6 |
| L1 | LOW | 3 | S7 | AC7 |
| L2 | LOW | 6 | S8 | AC8 |
| L3 | LOW | 7, 20 | S9 | AC9 |
| L4 | LOW | 9 | S10 | AC10 |
| L5 | LOW | 13 | S11 | AC11 |
| L6 | LOW | 16 | S12 | AC12 |
| L7 | LOW | 17 | S13 | AC13 |
| L8 | LOW | 18 | S14 | AC14 |
| hygiene red | — | — | S15 | AC15 |

## 2. Scope (IN)

- **S1** — M1, finding 2, `tools/memory-tree/asbuilt_view.py:239` (the record's `:222`) and the runner
  `tools/memory-tree/design_lib.py:152-163`. The class is every attribute source git consults beside the
  work tree's `.gitattributes` files, §4's table. Every `check-attr` call of `asbuilt_view.py` carries
  `ATTR_ARGS`, a new module constant `("-c", "core.attributesFile=/dev/null", "-c", "attr.tree=")`, and
  runs under `ATTR_ENV` (`:131`), which gains the entry `"GIT_ATTR_SOURCE": None`. `design_lib.run_git`'s
  `extra_env` reads a None value as "absent from this call's env", so a caller's `GIT_ATTR_SOURCE` never
  reaches the call; its docstring says so. No call passes `--attr-source`. The `check_view_merge`
  docstring (`:228-238`) names each source of the table and what keeps it out. This is the record's fix,
  held in one constant pair, so a later attribute read cannot carry a different subset of it. Observed by
  AC1.
- **S2** — M2, finding 4, `tools/memory-tree/asbuilt_view.py:217`, `read_info_merge` (`:199-224`).
  Where `info/attributes` is a file, the view is evaluated as tracked state alone answers it:
  `git check-attr` with `--git-dir` naming an empty scratch git directory initialised
  `--bare --template=`, `--work-tree` naming the root's absolute path, `ATTR_ARGS` and `ATTR_ENV`. That read sees the work
  tree's `.gitattributes` files with their macros and no `info/attributes` at all. When it answers
  anything but `ours`, the view's `ours` comes only through that file: `read_info_merge` returns the
  file and that answer, and `check_view_merge` reports the finding §4 words. This is better than the
  record's fix, which evaluates the tracked `[attr]` lines followed by the `info/attributes` lines: that
  misses the reverse direction, an `info/attributes` macro used by a tracked line. Measured: a tracked
  `v.md keep` with `[attr]keep merge=ours` in `info/attributes` answered `ours` plainly, `unspecified`
  under the record's evaluation, and `unspecified` under this one. The cost is unit 31's: one `git init`
  per check-30 run, on a node holding `info/attributes` alone. Observed by AC2.
- **S3** — M3, finding 11, the skeptic's corrected fix. The code-49 remedy at
  `tools/unattended/unattended.sh:13736` ends with the clause
  `or the word external, or the word none with no backticked token after it in the bullet:$_c_bad`,
  in place of `or the word external or none:$_c_bad`. In the same commit, the literals at
  `tools/unattended/unattended.test.sh:6430`, `:6431` and `:6453`, and S4's plant, carry that ending.
  Hygiene check 12 (`tools/memory-tree/check-memory-hygiene.sh:2479-2492`, `:2701-2709`) is unchanged,
  and the two readers' divergence is declared in §3's Edges as owed work. Observed by AC3.
- **S4** — M4, finding 14, `tools/unattended/lib-unattended.sh:357`. The class is a bullet read as its
  first physical line. A consumes-from line whose payload begins with `none`, bare or backticked, holds
  its verdict until the bullet ends, appending each following line. The bullet ends at a blank line, a
  line opening another bullet (`-` or `*`, then whitespace, at column 0), a heading, a new file, or the
  input's end, so an indented and a lazy continuation both join. A backtick after the word anywhere in
  the joined text makes the line unreadable, the `<spec> TAB` row of `--scan`. Every other payload is read
  as today: `external` admitted, an id read from the first line's backticked token. It is the narrowest
  change that closes the class, since only a `none` payload is admitted on what follows it. A suite plant
  wraps the S1 arm's bullet (`tools/unattended/unattended.test.sh:6445-6453`) so the backticked
  `ARCH-tRun-2` sits on an indented continuation line, and expects the unreadable refusal naming that
  spec. Observed by AC4.
- **S5** — M5, finding 10, `tools/memory-tree/gen_build_index.py:5155`, `scan_glob_readers`
  (`:5118-5173`). The class is a constant the walk cannot place. Each string constant carrying `:(glob)`
  outside a docstring is charged to exactly one name, by §4's charge rule. This is better than the
  record's `in_function=False`: a class built inside a function is local to it, so the function is its
  one reader, and a name such as `outer.Inner.P` is a table row no probe can reach. The rule is total, so
  every shape has an owner. The planted module of the AC5 plant arm (`:6442-6449`) gains §4's
  `outer_class`. Observed by AC5.
- **S6** — M6, findings 15 and 19, `tools/memory-tree/gen_build_index.py:6343-6346` and the comment at
  `:6329-6334`. The class is a probe answering for two pathspecs, which must be empty unless each one
  read. The `deviation_join.read_population` probe answers its sorted list only when the kinds it holds
  include both `audit` and `handback`, else an empty list. The `row_grammar._build_backlog_pathspecs`
  row is the class's second member: its reader joins two pathspecs (`tools/memory-tree/row_grammar.py:1656`),
  and the fixture `t23` holds one shard, `memory/backlog/ARCH.md` (`:6326`), so the second reads nothing.
  `t23` gains `memory/builds/tOne/BACKLOG.md` holding the row `ARCH-tOne-8`, written beside that shard
  before its commit, and the probe answers `derive_first_seen` only when it dates both `ARCH-tOne-8` and
  `ARCH-tOne-9`, else an empty dict. The comment says each probe is empty unless each of its pathspecs
  read. The arm's expected `probed=4 empty=[] moved=[]` is unchanged. Observed by AC6.
- **S7** — L1, finding 3, `tools/memory-tree/deviation_join.py:1586`. The class is every fixture
  `git init` of the memory-tree kit's Python, which passes `--template=`: `deviation_join.py:1224`
  (`build_fixture`), `:1453` (the AC20 arm), `:1586` (the AC4 arm's lone repository) and
  `tools/memory-tree/routed_commits.py:394`. A `run_plant_arms` arm exports `GIT_TEMPLATE_DIR`, through
  S15's keyword form, naming a scratch template whose `config` declares an `origin` remote, and asserts
  that a repository `build_fixture` writes and the lone repository each list no remote. Observed by AC7.
- **S8** — L2, finding 6, the skeptic's corrected fix. The class is every comment and message of the
  unattended kit that teaches the `none` grammar. The summary at `tools/unattended/lib-unattended.sh:331`
  says the unreadable payload is neither a backticked id, `external` nor a `none` that no backtick
  follows in its bullet, its wrapped lines included. The paragraph at `:333-341` and the comment at
  `tools/unattended/unattended.sh:13722-13724` say the same, each carrying the phrase
  `its wrapped lines included`. S3 owns the remedy. Observed by AC8.
- **S9** — L3, findings 7 and 20, the `scan_glob_readers` docstring at
  `tools/memory-tree/gen_build_index.py:5119-5130`. It states §4's charge rule, saying each `:(glob)`
  constant outside a docstring is charged to exactly one name, and its NOT SEEN list keeps run-time
  composition and shell scripts, now its only gaps. The planted module gains a module-level
  `SPECS.append` of a `:(glob)` constant, named `planted23`, and a class-level `PATHS.append` in
  `Planted`, named `planted23.Planted`. Observed by AC9.
- **S10** — L4, finding 9, `tools/memory-tree/asbuilt_view.py:206-209`. When
  `git rev-parse --git-path info/attributes` exits non-zero or prints nothing, `read_info_merge`
  returns `("info/attributes", "nothing, exit <n>")`, so check 30 refuses, as its scratch branch
  does. It answers None only when the resolved path is no file, or when S2's read answers `ours`. An arm swaps the module's `run_git` name,
  through a `global` statement, for a stand-in answering exit 128 with no stdout to `rev-parse` and
  calling the real runner otherwise, restored in a `finally`. Observed by AC10.
- **S11** — L5, finding 13, the skeptic's corrected fix. THE FINDINGS paragraph of the `asbuilt_view.py`
  docstring (`tools/memory-tree/asbuilt_view.py:69-77`) and check 30's entry in
  `tools/memory-tree/HYGIENE.template.md:591-609` and `memory/HYGIENE.md:591-609` each gain, in the same
  words, the S2 finding and the sources check 30 does not read. The two HYGIENE copies stay equal under
  the parity leg. Each carries the phrases `untracked info/attributes` and `attribute source tree`, each
  on one line. Observed by AC11.
- **S12** — L6, finding 16, the skeptic's corrected fix, in `test_coverage_stub`
  (`tools/memory-tree/gen_build_index.py:4749-4785`). An arm writes a scratch checker whose
  `load_design_lib` returns one module-level object holding its own `DesignRefusal` class, and whose
  `derive_carries_coverage` raises that class. The arm sets `CARRIES_CHECKER` to the checker's absolute
  path through the function's existing `global` statement, and puts a namesake `design_lib` with another
  `DesignRefusal` in `sys.modules`. It calls `read_carries_coverage(t, conf)` with no `resolve` and
  expects the Problem holding `carries join refused`. The `finally` restores both. Observed by AC12.
- **S13** — L7, finding 17. The planted module gains `def outer():`, whose nested `def inner():` alone
  returns a `:(glob)` constant, and the arm expects `planted23.outer.inner` and no `planted23.outer`.
  Observed by AC13.
- **S14** — L8, finding 18. An `asbuilt_view.py` arm exports `GIT_TEMPLATE_DIR`, through S15's keyword
  form, naming a scratch template whose `info/attributes` sets the view `merge=binary`, builds a second
  fixture with `build_view_fixture`, and asserts `check_merge_arm` holds over it. It then runs
  `check_node_merge_arm` under a template whose `info/attributes` sets the view `merge=ours`, which reds
  if S2's scratch initialisation takes a template. The `check_view_merge` docstring says no arm plants the
  system attributes file, whose path is git's install prefix. Observed by AC14.
- **S15** — the hygiene red, `tools/memory-tree/asbuilt_view.py:602-612`. `deviation_join.set_env_aside`
  (`tools/memory-tree/deviation_join.py:177-187`) takes the form `set_env_aside(names=(), **put)`: it
  holds each name of `names` and each key of `put` present in `os.environ`, sets `put`'s values for the
  block, and in its `finally` takes each `put` key out before restoring the held values. Every env name
  this unit's arms set, `GIT_CONFIG_GLOBAL`, `GIT_ATTR_SOURCE` and `GIT_TEMPLATE_DIR`, is passed as a
  keyword, so no line of the kit spells a quoted subscript or `.get` of one. The scan's pattern
  (`tools/memory-tree/check-memory-hygiene.test.sh:2821-2826`) and its exemptions (`:2863`) are
  unchanged, and S12 writes `CARRIES_CHECKER` through `global`, never a quoted `globals()` subscript.
  Observed by AC15.

## 3. Non-goals (OUT)

- The four refuted findings (1, 5, 8 and 12), earlier rounds' items whose fixes hold, and the flagged
  bar's inherited reds.
- The left-shift gates the record proposes as gates of their own: a grep gate over every kit's suites for
  a template-less `init` (L1) and the checklist classes. Each is its own unit by BUILD-METHOD M2.
- Hygiene check 12: its first-line read of an Edges bullet, its silent pass of a `none` followed by a
  backticked token, and its empty-payload message, which names `external` alone. TEMPLATE-SPEC's Edges
  payload rule is out too. They are declared below as owed.
- The fixture inits of other kits' suites, outside the memory-tree kit S7 grades.
- `tree_lib.GIT_ENV_LEAKS`, which the attribute read does not extend.
- Running any suite or the bar, and editing the frozen specs of units 1 to 31.

### Edges

- **consumes-from** external — the code CLOSED units of this build landed, which these fixes amend: the
  merge guard and its arms (units 26 and 31), the none admission and its remedy (units 20, 26 and 31),
  the glob walk and its mode arm (units 23 and 31), the coverage catch (unit 31), the fixture inits and
  the env hold (units 27 and 31); a frozen spec cannot write the mirroring hands-off line, so they are
  named here in prose
- **hands-off** external — hygiene check 12 reads an Edges bullet's first line alone and passes a none
  payload whatever follows it, where the dispatch reads the whole bullet and refuses a none a backticked
  token follows; aligning check 12, its message and the template's payload rule is a carrier change no
  clause of this build names, owed to a unit of its own

## 4. Design

### One unit

M4 batches every minor into one unit. S3, S4 and S8 write only the unattended kit, a set disjoint from
the rest, but order 15 holds this unit alone and the rescope row names one, so a split buys no
concurrency.

### The attribute read (S1, S2, S10, S14)

| Source git consults | Selected by | Kept out by |
|---|---|---|
| the system attributes file | git's install prefix | `GIT_ATTR_NOSYSTEM=1` in `ATTR_ENV`; no arm can plant it (S14) |
| the global attributes file | `core.attributesFile` at any scope, by default under `XDG_CONFIG_HOME` or `HOME` | `-c core.attributesFile=/dev/null` in `ATTR_ARGS` |
| an attribute source tree | `--attr-source`, `GIT_ATTR_SOURCE`, `attr.tree` | no call passes the option; `ATTR_ENV` unsets the variable; `-c attr.tree=` in `ATTR_ARGS` |
| `info/attributes` | the git directory, the common one in a linked worktree | the tracked-alone read (S2) |
| the work tree's `.gitattributes` files, the index where one is missing | the repository | read, as unit 31 S3 chose |

Measured on git 2.54.0.windows.1 in a scratch repository whose HEAD has no `.gitattributes` and whose
parent sets `v.md merge=ours`: under `-c attr.tree=`, a local `attr.tree`, a `GIT_CONFIG_COUNT` entry
and a `GIT_CONFIG_PARAMETERS` entry naming the parent each answered `unspecified`, and
`GIT_ATTR_SOURCE` naming it still answered `ours`. A `GIT_CONFIG_COUNT` entry naming a global attributes
file answered `ours` plainly and `unspecified` under the `-c`. The command-line `-c` wins over both
config variables, so the argv closes the config channel and only the env variable needs the unset.

`read_info_merge(root, view)`, after S2 and S10:

1. `rev-parse --git-path info/attributes` failing or printing nothing returns the pair of
   `info/attributes` and `nothing, exit <n>`.
2. A resolved path that is no file returns None.
3. Otherwise a scratch git directory is initialised `--bare --template=` under `ATTR_ENV`, and the
   view is read with `--git-dir` naming it and `--work-tree` naming the root. An answer of `ours`
   returns None, any other answer returns the resolved path and that answer in backticks, and a failed
   read returns the path and `nothing, exit <n>`. The scratch directory is taken out in a `finally`.

`check_view_merge` reports, for a returned pair `(file, said)`:

```text
DESIGN_VIEW <view>: answers `ours` for its merge attribute only through <file>, untracked node state
that outranks every tracked `.gitattributes` line, and tracked state alone answers <said>, so this node
merges the view as no other node does; take the view's line, or the macro it uses, out of that file and
keep the tracked `<view> merge=ours` line
```

The text keeps `info/attributes` in the finding, which unit 31's arm (`asbuilt_view.py:626`) asserts.

### The charge rule (S5, S9, S13)

Each `:(glob)` string constant outside a docstring is charged to exactly one name:

1. the innermost enclosing function, its decorators and signature included, as
   `<module>.<qualified name>` joining every enclosing class and function name;
2. else, outside every function, each `Name` in the targets of the innermost enclosing `Assign`,
   `AnnAssign` or `AugAssign`, qualified by the enclosing classes;
3. else the innermost enclosing class, qualified;
4. else the module, as `<module>`.

The rule over `tools/memory-tree/` at `2057f2272` names the five readers the table holds,
`design_lib.read_spec_revisions`, `deviation_join.read_population`, `gen_build_index.cmd_selftest`,
`gen_build_index.derive_audit_writers` and `row_grammar._build_backlog_pathspecs`, as the current walk
does. The planted module after S5, S9 and S13 appends to today's text:

```python
class Planted:          # today's class, gaining two lines before read_method
    PATHS = []
    PATHS.append(":(glob)memory/builds/*/prompts/**")


def outer_class():
    class Inner:
        P = ":(glob)memory/builds/**"
    return Inner.P


def outer():
    def inner():
        return ":(glob)memory/**"
    return inner


SPECS = []
SPECS.append(":(glob)memory/backlog/*.md")
```

Measured by an `ast` probe of the rule over that module, the arm's new expected `unlisted` list:

```text
['planted23', 'planted23.GUARDED', 'planted23.PLANTED', 'planted23.Planted', 'planted23.Planted.read_method',
 'planted23.outer.inner', 'planted23.outer_class', 'planted23.read_planted']
```

The current walk printed the same list less `planted23`, `planted23.Planted` and
`planted23.outer_class`.

### Contract changes a shipped verb takes (brief item 3)

| Item | Verb | What changes | What does not |
|---|---|---|---|
| S1 | `--check-asbuilt`, check 30, and `asbuilt_view.py --check` | `attr.tree` and `GIT_ATTR_SOURCE` no longer answer: a view guarded only through them is the unguarded-view finding | that finding's text, every exit |
| S2 | the same | the `info/attributes` finding fires when tracked state alone does not answer `ours`, macros of either side included; an `info/attributes` line agreeing with tracked state is not a finding; the finding's text is §4's | every exit, the unguarded-view finding |
| S10 | the same | a failed `info/attributes` path read is the finding, not clean | every other answer |
| S3 | `--dispatch`'s code-49 remedy | its text | the exit and when it fires |
| S4 | `--dispatch`, through `read_consumes_from` | a `none` bullet with a backtick on a later line of the bullet is unreadable, refused with code 49 | `external`; an id's read; a `none` bullet holding no backtick; every exit |
| S1 | `design_lib.run_git`, one caller | a None `extra_env` value leaves its key out of the call's env | every other key and call |
| S15 | `deviation_join.set_env_aside`, a kit-internal helper | it takes `put` keywords | the positional form its four call sites use |

Each is the narrowest change that closes its class. S1 adds one `-c` and one unset to the read the
guard makes. S2 reads one more time only where `info/attributes` exists and the first answer is `ours`.
S4 joins later lines only for the one payload admitted on what follows it.

### What each item does not check

- S1: the work tree's `.gitattributes`, an untracked one included, still answers, and the index answers
  for a file missing from the work tree, as unit 31 S3 chose.
- S2: a tracked `.gitattributes` missing from the work tree reads from the index in the real read and
  not in the scratch one, so on a node that also holds `info/attributes` it is the S2 finding, the
  refusing direction, naming the wrong file.
- S4: a sibling named in a `none` bullet's prose without backticks still reads as no edge, as unit 31 S1
  stated.
- S5: a pathspec composed at run time stays unseen, and a module-level name is a table row only when a
  probe can reach it.
- S6: the backlog reader passes both pathspecs to one git call, so a mode moves them together, and the
  probe proves each read a row at the unset baseline.
- S7: other kits' suites are not graded, §3.
- S12: the arm proves the catch reads the checker's own class, not that every checker refusal is a
  `DesignRefusal`.
- S14: the system attributes file is not planted: no variable relocates it, and the arm writes no file
  outside its scratch directories.
- S15: a later arm spelling an env read as a quoted subscript reds the parity arm by name, the loud
  direction.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `ATTR_ARGS` | module constant, `asbuilt_view.py` | `py.constant`, OK |
| `put` | keyword-collecting parameter of `set_env_aside` | none |

The names `outer_class`, `outer`, `inner`, `PATHS` and `SPECS` sit in the planted module's text, which
the selftest writes to a scratch directory, and are no identifiers of the tree.

### Files touched (estimate)

- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by
  `--write`, never edited: `asbuilt_view.py`, `design_lib.py` and `deviation_join.py` are view inputs)

### Alternatives rejected

- **S2: the record's evaluation of tracked `[attr]` lines followed by the `info/attributes` lines.** It
  answers `unspecified` for an `info/attributes` macro a tracked line uses, measured above.
- **S2: a finding for any `info/attributes` line whose pattern matches the view.** The record's
  alternative misses a macro defined there, and reds a line that agrees with tracked state.
- **S1: `GIT_ATTR_SOURCE` in `tree_lib.GIT_ENV_LEAKS`.** Every kit git reader would lose a variable only
  this read must not see, and the leak list's arm asserts its twelve names
  (`tools/memory-tree/gen_build_index.py:6413`).
- **S5: `in_function=False` for a class nested in a function.** It names a constant no probe can reach.
- **S6: one probe row per pathspec.** The table's keys are the walk's names, and AC5's both-ways equality
  would report a key no walk derives as stale.
- **S15: `GIT_CONFIG_GLOBAL` in `_pyexempt`.** It loosens the scan. A name constant read through
  `os.environ.get(NAME)` passes too, but leaves three arms with three hold-and-restore copies where one
  helper serves.

## 5. Production-readiness checklist

- security — S1 and S2 keep every node-local attribute source out of the guard's answer, S10 refuses a
  read that cannot be made, and S4 refuses rather than admits.
- perf / scale — S2 adds no git call to a node without `info/attributes`; S14 adds one view fixture and
  S6 one file to the selftests.
- error / empty / loading states — S6's probes are empty unless each pathspec read; S10 turns a failed
  path read into the finding.
- observability — S2's finding names the file and what tracked state alone answers; S3's remedy names
  the rule.
- risks — S2 reports a missing tracked `.gitattributes` as the `info/attributes` finding on a node
  holding both, the loud direction; S4 refuses a wrapped `none` naming a non-sibling token too.
- testing — AC1 to AC15 as probes and greps; the arms under §7.
- migration — none: the two corpus `none` payloads hold no backtick in their bullets
  (`memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md:106`,
  `memory/builds/aQuenchedHarness/spec/2026-09-08-spec-TOOL-aQuenchedHarness-13.md:44`).
- user docs — no page under `help/` covers these engines; S11's HYGIENE entries and the comments S8
  names are their documentation.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch repository sits under the session's temp root
with no hook installed.

- **AC1** — When a probe makes a scratch repository whose HEAD has no `.gitattributes` and whose parent
  commit's sets `v.md merge=ours`, and calls `asbuilt_view.check_view_merge(root, "v.md")` once with
  `GIT_ATTR_SOURCE` exported naming the parent and once with a local `git config attr.tree` naming it,
  each call returns the finding naming `DESIGN_VIEW` and `merge=ours`.
  Red when: either call returns None, as the review measured at `2057f2272`.
- **AC2** — When a probe makes a scratch repository and calls
  `asbuilt_view.check_view_merge(root, "v.md")` three times, the answers are: with the committed
  `.gitattributes` holding `[attr]keep merge=ours` and `info/attributes` holding `v.md keep`, a finding
  naming `info/attributes`; with `v.md keep` committed and `[attr]keep merge=ours` in `info/attributes`,
  the same; and with `v.md merge=ours` in both, None.
  Red when: the first or second returns None, the first as the review measured at `2057f2272`.
- **AC3** — When `grep -c 'or the word none with no backticked token after it in the bullet:\$_c_bad' tools/unattended/unattended.sh`
  runs it prints 1; `grep -c 'or the word none with no backticked token after it in the bullet' tools/unattended/unattended.test.sh`
  prints at least 4; and `grep -c 'or the word external or none' tools/unattended/unattended.sh tools/unattended/unattended.test.sh`
  prints 0 for each file.
  Red when: the last prints 1 and 3, as at `2057f2272`.
- **AC4** — When a probe sources `tools/unattended/lib-unattended.sh` and runs
  `read_consumes_from --scan` over three scratch specs, it prints the first spec's path and a tab, the
  same for the second, and for the third only its path, a tab and `ARCH-tRun-3`. The first spec's bullet
  is `none until the producer` with `ARCH-tRun-2` backticked on an indented next line; the second has
  that next line at column 0; the third's `none until the producer` continues on a line holding no
  backtick, followed by a bullet consuming from a backticked `ARCH-tRun-3`. In ids mode the third prints
  `ARCH-tRun-3` alone.
  Red when: the first spec prints nothing, as the review measured at `2057f2272`.
- **AC5** — When a probe copies the Python modules of `tools/memory-tree/` to a scratch directory beside
  the planted module §4 writes, `gen_build_index.scan_glob_readers` over it names
  `planted23.outer_class`, and over `tools/memory-tree/` it names the five readers §4 lists.
  Red when: `planted23.outer_class` is unnamed, as the review's probe of that shape printed `[]`.
- **AC6** — When an `ast` probe reads the `probes23` dict of `tools/memory-tree/gen_build_index.py`, the
  lambda under `deviation_join.read_population` compares the kinds it read with a set display holding
  `audit` and `handback`, and the lambda under `row_grammar._build_backlog_pathspecs` names
  `ARCH-tOne-8` and `ARCH-tOne-9`; and `grep -c 'ARCH-tOne-8' tools/memory-tree/gen_build_index.py`
  prints at least 2.
  Red when: either lambda returns its answer whatever kinds or ids it holds, as both do at `2057f2272`.
- **AC7** — When `grep -nE '"init", "-q"' tools/memory-tree/*.py | grep -vc -- '--template='` runs it
  prints 0, and a probe exporting `GIT_TEMPLATE_DIR` naming a scratch template whose `config` declares
  `[remote "origin"]` calls `deviation_join.build_fixture(root, [])`, after which `git -C <root> remote`
  prints nothing.
  Red when: the grep prints 4 and the remote lists `origin`, as at `2057f2272`.
- **AC8** — When `grep -cE 'external. nor .none. ' tools/unattended/lib-unattended.sh` runs it prints
  0, and `grep -c 'its wrapped lines included' tools/unattended/lib-unattended.sh tools/unattended/unattended.sh`
  prints at least 1 for each file.
  Red when: the summary still lists `none` unqualified, the second grep printing 1 as at `2057f2272`.
- **AC9** — When the AC5 probe runs, `scan_glob_readers` names `planted23` and `planted23.Planted`; and
  `grep -c 'The walk reaches every depth' tools/memory-tree/gen_build_index.py` prints 0, and
  `grep -c 'charged to exactly one name' tools/memory-tree/gen_build_index.py` prints at least 1.
  Red when: `planted23` is unnamed, as the review's probe of a module-level `append` printed only the
  top-level reader.
- **AC10** — When a probe loads `tools/memory-tree/asbuilt_view.py`, swaps the module's `run_git` for a
  stand-in answering exit 128 with no stdout to `rev-parse`, and calls
  `asbuilt_view.read_info_merge(root, "v.md")` over a scratch repository, it returns a pair whose first
  item is `info/attributes` and whose second holds `exit 128`; with the real runner restored and no
  `info/attributes` file, it returns None.
  Red when: the failed read returns None, as `tools/memory-tree/asbuilt_view.py:206-209` reads at `2057f2272`.
- **AC11** — When `grep -c 'untracked info/attributes' tools/memory-tree/asbuilt_view.py tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md`
  and the same with `attribute source tree` run, each prints at least 1 for each file.
  Red when: any file prints 0, as all three do at `2057f2272`.
- **AC12** — When a probe writes a scratch checker as S12 states, sets
  `gen_build_index.CARRIES_CHECKER` to its absolute path, puts a namesake `design_lib` in `sys.modules`,
  and calls `gen_build_index.read_carries_coverage(t, conf)` with `CARRIES_KEY` set in `conf`, it raises
  the module's `Problem` holding `carries join refused`; and
  `grep -c 'carries join refused' tools/memory-tree/gen_build_index.py` prints 3.
  Red when: the catch reads the refusal class from `sys.modules` alone, so the checker's refusal escapes
  as itself, and the grep prints 2, as at `2057f2272`.
- **AC13** — When the AC5 probe runs, `scan_glob_readers` names `planted23.outer.inner` and not
  `planted23.outer`, and `grep -c 'planted23.outer.inner' tools/memory-tree/gen_build_index.py` prints at
  least 1.
  Red when: a walk descending into nested functions names `planted23.outer`, as the review's
  full-descent probe named its `outer`.
- **AC14** — When a probe exports `GIT_TEMPLATE_DIR` naming a scratch template whose `info/attributes`
  holds `*.md merge=binary` and calls `asbuilt_view.build_view_fixture(root)`, then
  `asbuilt_view.read_view_inputs(root, conf)` answers no finding; and
  `grep -c 'system attributes file' tools/memory-tree/asbuilt_view.py` prints at least 1.
  Red when: the fixture's init takes the template and the view answers `binary`.
- **AC15** — When `cat tools/memory-tree/*.py | grep -oE "[]A-Za-z0-9_)](\.get\(|\[)[\"'][A-Z][A-Z0-9_]{2,}[\"']" | grep -cE 'GIT_(CONFIG_GLOBAL|ATTR_SOURCE|TEMPLATE_DIR)'`
  runs it prints 0, and `grep -c 'GIT_CONFIG_GLOBAL' tools/memory-tree/check-memory-hygiene.test.sh`
  prints 0.
  Red when: the first prints 3, the arm's spellings at `tools/memory-tree/asbuilt_view.py:602-612`, as
  at `2057f2272`.

## 7. Gates

`build-index selftest` · `routed-commits selftest` · `tier2-review self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `memory-hygiene self-test` · `memory hygiene` · `unattended kit gate` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/asbuilt_view.py (its selftest, run by the build-index selftest) · covers AC1 AC2 AC10 AC14 · the fixture view under a local attr.tree and an exported GIT_ATTR_SOURCE naming HEAD with the work-tree line emptied, a tracked macro used from info/attributes and the reverse, an agreeing info/attributes line, a failed path read, and two templates · none
New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC5 AC6 AC9 AC12 AC13 · the planted module's class in a function, module-level and class-level appends and nested def; the deviation fixture without the audit-pin plant and t23 without its builds BACKLOG row; a scratch checker raising its own DesignRefusal under a namesake · none
New arm: tools/memory-tree/deviation_join.py (its selftest, run by the routed-commits selftest) · covers AC7 · GIT_TEMPLATE_DIR naming a template whose config declares an origin remote · none
New arm: tools/unattended/unattended.test.sh · covers AC3 AC4 · the S1 bullet wrapped, its backticked sibling on an indented line, and the remedy's literals · none

The first six legs are the ones the estimate's guards trip; the rest carry the arms and the gates the
touched files feed. S8's comments and S11's documentation have no arm: no arm reads a comment, and the
parity leg already holds the two HYGIENE copies equal. S15 adds no arm: the parity arm at
`tools/memory-tree/check-memory-hygiene.test.sh:2874` is its guard, observed red at `3c4271e8f`. S7's
`routed_commits.py` site has no arm of its own: deviation_join's template arm is the class's plant, and
AC7's grep observes the site. README rule 8 waives the unattended suites' verdict at this landing, so the
fourth arm's red-then-green readings at the close are AC3's and AC4's probes.

## 8. Open questions

- **F1 — Does the build's grant lift veto 2 for each carrier edit here?** S1, S2, S10 and S14 change
  check 30's attribute read, the as-built guard of `cl-dClosedLoop-0006`, with S1's runner change in
  `cl-dClosedLoop-0001`'s `design_lib`, and S11 the check's two HYGIENE entries. S7's `deviation_join`
  sites and S15 change `cl-dClosedLoop-0004`'s fixture and its env hold. S4 changes the dispatch's edge
  reader, a carrier no clause names. It builds the rest of the change TOOL-dTrueNorth-31 §8 F1 took at
  rung 5 and deviation-34 records, whose After admits a none only when no backtick follows it, which a
  wrapped bullet's later line does; so S4 is that resolution's and owes no record of its own. S3 and S8
  change a message and comments; S5, S6, S9, S12 and S13 a walk and arms only the generator's selftest
  calls; S7's `routed_commits` site a selftest fixture. RESOLVED (agent, 2026-10-22, delegated): lifted
  by `PLAY-dClosedLoop-3`, rung 3, for S1, S2, S7's deviation_join sites, S10, S11, S14 and S15; S4 rests
  on TOOL-dTrueNorth-31 §8 F1 and deviation-34; the rest change no carrier's behaviour, as
  TOOL-dTrueNorth-27 §8 F6 read its message edit. grants: PLAY-dClosedLoop-3 the memory-tree kit edits
  S1, S2, S7, S10, S11, S14 and S15 make for cl-dClosedLoop-0001, cl-dClosedLoop-0004 and
  cl-dClosedLoop-0006 · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-22 · initial draft, batching the round-3 closing diff review's 6 MEDIUM and 8 LOW
  items, findings 6, 11, 13 and 16 from the skeptic's corrected fix, M1, M2, M4 and M5 closed by class,
  and the memory-hygiene conf-example parity red, with deviation-35's record of the unit.

## 10. Reuse audit

Every item extends a seam the build already has, read at `2057f2272`: `ATTR_ENV` and the attribute read
of `check_view_merge` and `read_info_merge` (`tools/memory-tree/asbuilt_view.py:131`, `:199-252`);
`design_lib.run_git`'s `extra_env` (`tools/memory-tree/design_lib.py:152-163`);
`deviation_join.set_env_aside` (`tools/memory-tree/deviation_join.py:177-187`); the `read_consumes_from`
awk (`tools/unattended/lib-unattended.sh:342-366`); `scan_glob_readers` and its planted-module arm; the
`probes23` table and its `audit-pin` fixture; `test_coverage_stub` and its `global CARRIES_CHECKER` swap;
and the `--template=` init the kit's other fixtures already use (`tools/memory-tree/check-arms.py:1169`).

The two `reuse_lookup.py` probes, verbatim:

```bash
python tools/codebase-map/reuse_lookup.py "evaluate git attributes from tracked state alone, without node-local attribute sources"
python tools/codebase-map/reuse_lookup.py "hold an environment variable set to a value for a block and restore the caller's value after"
```

The first ranked `run_git` as a SEAM, beside `read_git_output` and `build_git_env`, and S1 and S2
extend `design_lib.run_git`. The second did not rank `set_env_aside`: its stems ranked `holder`,
`set_gen_strip` and `set_fact`, none an environment hold, so that seam was found by reading
`tools/memory-tree/deviation_join.py:177-187`. No existing seam fits the tracked-alone attribute read
itself, and S2 builds it on `design_lib.run_git`.

Recall terms used: `python tools/memory-recall/query.py "how does the round-three closing diff review's batch close the attribute source, wrapped none bullet and glob walk classes" --terms "closing diff review round three attr.tree GIT_ATTR_SOURCE info/attributes macro wrapped none bullet glob walk pathspec probe template"`
