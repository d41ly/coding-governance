# TOOL-dRedressedBar-26 — the round-2 temp-name findings, batched: every command-word `mv` is read, no positional or two-hop source reds, no bare `SRANDOM` is admitted, and the cache writer and leftover check hold on every runtime

**Status:** CLOSED · rev-1 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-15-build-TOOL-dRedressedBar-26-1-acceptance-ledger.md](../build/2026-10-15-build-TOOL-dRedressedBar-26-1-acceptance-ledger.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-25-brief.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-brief.md) | research | TOOL-dRedressedBar-25 |
| [2026-10-15-prompt-TOOL-dRedressedBar-26-1-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-26-1-spec-writer.md) | journal | — |
| [2026-10-15-prompt-TOOL-dRedressedBar-26-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-26-2-revision.md) | research | TOOL-dRedressedBar-24 |
| [2026-10-15-prompt-TOOL-dRedressedBar-26-3-spec-writer.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-26-3-spec-writer.md) | journal | — |
| [2026-10-15-review-TOOL-dRedressedBar-25-26-diff-review-round3.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-25-26-diff-review-round3.md) | diff-review | TOOL-dRedressedBar-18 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-24 TOOL-dRedressedBar-25 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 closing diff review over `e114f1356..5b30e4b47`
(`reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md`) read CLEAN WITH FIXES,
and the owner promoted all 14 of its confirmed findings on 2026-10-15, "then stop" (the README's
Build-level rules). BUILD-METHOD M4 batches them by disjoint write set. This is the batch over
`tools/gate-lint/sh_hygiene.py --temp-names`, its README section, and the run-gates writer and arm
unit 24 left. Unit 25 is the profiler's batch. The brief is
`prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-brief.md`.

It closes these findings, by report id, each with the report item it sits in:

| id | grade | item | sits in, at `5b30e4b47` | what is wrong | closed by |
|---|---|---|---|---|---|
| 22 | HIGH | H2 | `tools/gate-lint/sh_hygiene.py:962` | no `mv` is read after `if`, `elif`, `while`, `until`, `command`, `exec` or a leading assignment | S22 |
| 6 | MEDIUM | M2 | `sh_hygiene.py:962` against `:972` | TEMP_MV's keyword leads are three of TEMP_LEAD's seven, one rule kept twice | S6 |
| 7 | MEDIUM | M3 | `sh_hygiene.py:966` | a positional rename source is gated, against the documented contract | S7 |
| 10 | MEDIUM | M4 | `sh_hygiene.py:968`, `:999-1005`, `:989-991` | a bare `$SRANDOM` temp is admitted, and it is a fixed name on bash before 5.1 | S10 |
| 21 | LOW | L2 | `sh_hygiene.py:1068-1075`, `:1112-1117` | a two-hop binding is a false red, `command mv` an unlisted miss, and the docs say "never a false red" | S21 |
| 8 | LOW | L3 | `tools/run-gates/run-gates.sh:5481-5482` | the reuse-cache writer imports `tempfile` under a bare `-c` run from `$ROOT` | S8 |
| 19 | LOW | L4 | `tools/run-gates/run-gates.runlog.test.sh:1085` | the TWO arm's leftover check counts only the SRANDOM spelling of a staging name | S19 |
| 13 | LOW | L5 | `sh_hygiene.py:1146-1148`, with `check_registry` at `:479-482` | a drifted registry key is counted as two findings | S13 |

Id 7 was re-graded low to medium by its skeptic, and that grade binds. Id 6 is the `if`, `elif`,
`while` and `until` half of id 22, and the record asks for both in one change. Every fix here is the
record's own, each judged SOUND by its skeptic.

Spec 24 is CLOSED and describes the predicate, the selftest rows, the cache writer and the TWO arm
this unit changes. Its correction is this unit's spec-writer pass, `<w26>` (§4 "What this unit
corrects in spec 24").

## 2. Scope (IN)

Item S<n> closes report id n, and S24 is the record. Every line cited is at `5b30e4b47`, whose
`tools/` equals `bc6a4c9f0`'s. Unit 25 edits no file of this unit's product write set, so the
citations hold at this unit's turn.

- **S22** — id 22, H2. `sh_hygiene.py` gains `TEMP_KEYWORDS`, the tuple `("if", "then", "else",
  "elif", "do", "while", "until")`, and `TEMP_PREFIXES`, the tuple `("command", "builtin", "exec")`.
  TEMP_MV is built from both: an `mv` is a command word at a segment's start, or after `;`, `&`,
  `|`, `{`, `(` or `!`, once a run of lead words is skipped. A lead word is an opener or `!`, a word
  of `TEMP_KEYWORDS`, a word of `TEMP_PREFIXES`, or an assignment word `NAME=value`. The selftest
  gains the lead-word arm and the rows `LC_ALL=C mv`, `command mv` and two prefix assignments
  (§4 "The selftest"). Observed by AC22.
- **S6** — id 6, M2. TEMP_LEAD is built from `TEMP_KEYWORDS` too, so the binding side and the `mv`
  side read one list. `TEMP_PREFIXES` is TEMP_MV's alone, because `command f`, `builtin f` and
  `exec f` do not run a shell function `f`, so a binder call after one binds nothing. The selftest
  gains the `if mv` row. Built in one change with S22. Observed by AC6.
- **S7** — id 7, M3. `sh_hygiene.py` gains `TEMP_POSITIONAL`, a source that is exactly one
  positional parameter: `$<digit>`, `${<digits>}`, `$@` or `$*`, quoted or not. Such a source is
  `unfollowed`. So is a source whose one-hop binding has such a value, as in `local src=$1`. The
  selftest gains the two rows the record names, each expecting `([], 0, 1)`. Observed by AC7.
- **S10** — id 10, M4. `TEMP_UNPREDICTABLE` matches `$(mktemp` alone, so a bare `SRANDOM` source or
  bound value is graded `fixed`. `read_temp_binders` admits a binder when its body holds `mktemp`
  and, wherever it expands `SRANDOM`, also holds the test `${SRANDOM:-`, which is the shape of
  `derive_temp_path` (`run-gates.sh:779`). TEMP_REMEDY names two forms, `t=$(mktemp -u
  "$dest.XXXXXXXX")` and a binder of that shape, spelling its `${SRANDOM:-}` test and its `mktemp`
  fallback. The `admitted` label in TEMP_CLASSES, the module
  docstring's fourth-class paragraph (`:13-20`) and the README section say the same. The selftest's
  `SRANDOM` row expects a site on line 2, and a row for a binder that expands `SRANDOM` with no
  guard expects one too. Observed by AC10.
- **S21** — id 21, L2. A one-hop binding whose value is itself one expansion, `TEMP_FOLLOW`'s shape,
  is `unfollowed`, so `t=$u` no longer reds. `command mv` is read by S22. The documented boundary
  becomes one table, `TEMP_BOUNDARY`, of 13 rows: a label, a shell example and the class the
  example lands in (§4 "The boundary"). `run_temp_scan`'s docstring names every label and says
  which row is a false red, where today it says each gap is "a MISS and never a false red". The
  README section names every label. TEMP_CLASSES' `unfollowed` label states S7's and S21's sources.
  The selftest gains the two-hop row and the boundary arm. Observed by AC21.
- **S8** — id 8, L3. The reuse-cache writer runs as `"$PYBIN" -I -c '` (`run-gates.sh:5481`), with
  a comment line above it saying the program runs from `$ROOT`, where a top-level `tempfile.py`
  would shadow the standard module. Nothing else in the program moves. Observed by AC8.
- **S19** — id 19, L4. `check_two_writers` in `tools/run-gates/run-gates.runlog.test.sh` counts
  leftovers with one pattern, `stg='^gate-full-green\.shared\.'`, which matches both spellings the
  helper writes and not the destination. A planted pair, one name of each spelling, must count 2.
  The stamp half then runs a second time on the helper's `mktemp` branch, with `unset SRANDOM`
  ahead of the helper in each process. `FLOOR_ASSERTIONS` (`:56`) rises from 226 to 230.
  Observed by AC19.
- **S13** — id 13, L5. `check_registry` (`sh_hygiene.py:457`) gains an optional fourth argument,
  `listing`, a key's site lines, appended to that key's count-mismatch line. `run_temp_scan`
  passes its listing there and appends no second line of its own (`:1146-1148`). The other three
  modes pass none and print as now. The selftest gains a unit row and a run over a scratch
  repository whose one key drifted, asserting the printed total reads `1 finding(s)`.
  Observed by AC13.
- **S24** — The record, in two passes. Spec 24 takes ONE rev bump in `<w26>`, which runs once unit
  25 is CLOSED and before this unit's build pass. Its revision line names `TOOL-dRedressedBar-26`
  and every report id §4's correction table assigns it, and its §3 Edges gains `hands-off`
  `TOOL-dRedressedBar-26`. The product commit `<p26>` carries the kickoff-manifest re-stamp at its
  parent that the ratchet's staged check requires, as `73b80ed31` did. A second commit, `<p26m>`,
  re-stamps `last-audit:` in `memory/guides/SESSION-KICKOFF.md` at `<p26>` after a section B
  re-read, with a `manifest-audit:` line in its body, as `be022852d` did. The build pass writes no
  spec file but this one's status and date cells. Every reading goes to an acceptance ledger under
  `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal TOOL-dRedressedBar-26`.
  Observed by AC24.

Every selftest addition is unconditional. `FLOOR_ASSERTIONS` (`sh_hygiene.py:226`) rises from 92 to
the count `--selftest` prints, with a comment line in the form of `:222-225`. This design's count is
32 new assertions, so 124, an ESTIMATE counted off §4's table.

## 3. Non-goals (OUT)

- No finding outside the round-2 record. Ids 4, 11, 15, 18, 20 and 23 are unit 25's. Ids 1, 2, 3,
  5, 9, 12, 14, 16 and 17 were refuted and stay refuted.
- The other four `"$PYBIN" -c` programs in the runner (`run-gates.sh:1363`, `:2708`, `:2986`,
  `:4956`). They import `json`, `hashlib`, `statistics` and `subprocess`, none preloaded, so a
  top-level module of one of those names shadows them too. Measured on node d on 2026-10-15 under
  Python 3.12.10: a cwd `json.py` stops a bare `-c` import. They predate the reviewed fold, no
  confirmed finding names them, and the record's static arm for the class would red on all four.
  They are handed off (Edges).
- The record's two checklist lines, M2's "two regexes that each list a grammar's keywords are one
  rule kept twice" and M4's "an unpredictability predicate admits a source only when the source is
  unpredictable on every runtime the kit supports". Each is a record under `memory/gotchas/`, a
  separate document by M2, as unit 22 left its record's checklist lines.
- No `mv` read in a case arm, through a wrapper command, by a path or a backslash, or with an
  option after `command`. Each is a documented row of `TEMP_BOUNDARY`, which is what the record's
  fix asks of a form left out.
- No change to how a prefix assignment binds. A segment `LC_ALL=C mv ...` still records `LC_ALL` in
  the scope's table, as at `5b30e4b47`, and no source reads that name.
- No change to `memory/project/temp-name-sites.txt`. The designed rules measure the same 20 sites
  in 14 files on today's tree (§4 Evidence).
- No kit version moved. Run-gates' shipped bytes move, and the lander's `govkit.py mint` dates the
  move (`tools/govkit/govkit.py:13381`). Gate-lint declares no version (`tools/gate-lint/kit.toml:6`).
- No `tools/unattended/` self-test suite runs, by the owner's standing instruction of 2026-08-23.

### Edges

- **consumes-from** `TOOL-dRedressedBar-24` — the `--temp-names` mode, its selftest rows, the
  registry, `derive_temp_path`, the TWO arm's re-arm and the reuse-cache writer's `mkstemp`
  program, all of which this unit changes, and spec 24, whose text `<w26>` corrects. Without them
  there is nothing to fix.
- **hands-off** external — the shadowing class over the runner's four other `"$PYBIN" -c` programs,
  and the record's static arm for it, for the follow-up build the README's round-2 ruling names.
- **hands-off** external — the record's checklist lines for M2 and M4, as records under
  `memory/gotchas/`.

## 4. Design

### Evidence, read at `bc6a4c9f0` on 2026-10-15

`git diff --stat 5b30e4b47 bc6a4c9f0 -- tools help skills .githooks .memory-tree.conf` prints
nothing, so the reviewed tip's code is the tree read here. Every line the record cites was re-read
and agrees, except two offsets: the cache writer's `"$PYBIN" -c '` is `run-gates.sh:5481` and its
`import` line `:5482`, and the docstring's not-checked list is `sh_hygiene.py:1112-1117`.

A python program imported `sh_hygiene` and ran `scan_temp_file` over each spelling. It printed
fixed lines, the admitted count and the unfollowed count:

| Text | Reading at `5b30e4b47` |
|---|---|
| `mv -f "$f.tmp" "$f"` | `([1], 0, 0)` |
| `if mv -f "$f.tmp" "$f"; then :; fi`, and `elif`, `while`, `until` | `([], 0, 0)` each |
| `command mv`, `builtin mv`, `exec mv`, `LC_ALL=C mv`, `A=1 B=2 mv` | `([], 0, 0)` each |
| `if ! mv ...`, `while ! mv ...` | `([1], 0, 0)` |
| `rename_into() { mv -f "$1" "$2"; }` | `([1], 0, 0)` |
| `g() { local src=$1; mv -f "$src" "$2"; }`, over three lines | `([3], 0, 0)` |
| `t="$f.$SRANDOM$SRANDOM.tmp"` then `mv "$t" "$f"` | `([], 1, 0)` |
| a binder whose body expands `SRANDOM` and holds no `mktemp` | `([], 1, 0)` |
| `u=$(mktemp -u "$x.XXXX")`, `t=$u`, `mv "$t" x` | `([3], 0, 0)` |
| `check_registry` plus `run_temp_scan`'s extend, one key declared 1 and measured 2 | two problems |

With `SRANDOM` unset, `t="$f.$SRANDOM$SRANDOM.tmp"` expands to `<f>..tmp`, so the admitted name is
fixed on a bash that has no `SRANDOM`. In a directory holding `tempfile.py` that raises,
`python -c 'import os, sys, tempfile, time'` exits 1 with the raised message, and the same with
`-I` prints `ok`. Only `os`, `sys` and `time` are in `sys.modules` at a bare `-c` start. Both
`py -I -c` and `python3 -I -c` report `sys.flags.isolated` 1, and `tools/lib/resolve-python.sh:30`
resolves `PYBIN` to one of `python3`, `python` or `py` when no override names another. Under the
TWO arm's old pattern, a directory holding `gate-full-green.shared`, `gate-full-green.shared.1234567890.tmp`
and `gate-full-green.shared.AbCd1234` counts 1, and under S19's pattern 2.

**The tree, under the designed rules.** A probe copied `scan_temp_file` with S22's TEMP_MV, S7's and
S21's follow step and S10's admitted rule, and ran it and the shipped scanner over the leg's
population (`. :!*.test.sh :!memory/`). Both read 68 sources, 20 fixed sites in 14 files, 28
admitted and 1 unfollowed, and no file's lists differ. All PINNED at `bc6a4c9f0` on 2026-10-15. The
registry is unchanged for that reason. The record says the same of H2.

### The lint, item by item

Each row is a change to `tools/gate-lint/sh_hygiene.py` unless it names another file.

| Id | Change |
|---|---|
| 22, 6 | `TEMP_KEYWORDS`, `TEMP_PREFIXES`; TEMP_MV and TEMP_LEAD built from them; the lead-word arm; four `temp_cases` rows |
| 7 | `TEMP_POSITIONAL`; the follow step; two `temp_cases` rows |
| 10 | `TEMP_UNPREDICTABLE`; `read_temp_binders`; TEMP_REMEDY; the `admitted` label; the module docstring; the `SRANDOM` row's expectation and one new row; the README section; `memory/map/features/gate-lint.md:207` |
| 21 | the follow step; `TEMP_BOUNDARY`; `run_temp_scan`'s docstring; the `unfollowed` label; the README section; the two-hop row; the boundary arm |
| 13 | `check_registry`'s `listing`; `run_temp_scan`'s call; a unit row; a scratch-repository run |
| 8 | `tools/run-gates/run-gates.sh`, the cache writer's interpreter flags and a comment |
| 19 | `tools/run-gates/run-gates.runlog.test.sh`, `check_two_writers` and its floor |

### The command-word rule, S22 and S6

```python
# The keywords a command word may follow at a segment's start: ONE list, read by both predicates.
TEMP_KEYWORDS = ("if", "then", "else", "elif", "do", "while", "until")
# Words that run the word after them as a command. Read before `mv` only: none of them runs a shell
# function, so a binder call after one binds nothing.
TEMP_PREFIXES = ("command", "builtin", "exec")
TEMP_LEAD = re.compile(r"\A(?:[ \t]*(?:[{(!]|(?:" + "|".join(TEMP_KEYWORDS) + r")(?=[ \t])))*[ \t]*")
TEMP_MV = re.compile(r"(?:\A|[;&|{(!])(?:[ \t]*(?:[{(!]|(?:" + "|".join(TEMP_KEYWORDS + TEMP_PREFIXES)
                     + r")(?=[ \t])|[A-Za-z_][A-Za-z0-9_]*\+?=[^ \t]*(?=[ \t])))*[ \t]*mv(?=[ \t])")
```

TEMP_MV runs over the segment with its quoted text blanked (`:1034-1048`), so a quoted value inside
an assignment word holds no space, and `B="x y" mv` reads as one assignment word and `mv`. The
segment cuts at `;`, `&&` and `||` (`:1049`) already put every keyword at a segment's start, so the
old mid-segment alternative `(?<![\w-])(?:then|do|else)[ \t]+` is not kept. Its one effect the probe
found is a false site on `echo then mv x.tmp x`, where `mv` is an argument.

### The follow step, S7 and S21

```python
TEMP_POSITIONAL = re.compile(r"\A(\"?)\$(?:[0-9@*]|\{(?:[0-9]+|[@*])\})\1\Z")

follow = TEMP_FOLLOW.match(source)
bound = table.get(follow.group(2) or follow.group(3)) if follow else None
value = bound[1].strip() if bound and bound[0] == "value" else ""
if (not source or TEMP_POSITIONAL.match(source) or (follow and bound is None)
        or TEMP_FOLLOW.match(value) or TEMP_POSITIONAL.match(value)):
    kind = "unfollowed"
elif bound and bound[0] == "binder":
    kind = "admitted" if binders[bound[1]] else "fixed"
else:
    kind = "admitted" if check_temp_source(value or source) else "fixed"
```

A value that is one expansion is unfollowed whether its name's own binding is unpredictable or
fixed. So `u="$x.tmp"; t=$u; mv "$t" x` is a miss, where today it reds. The record's fix chooses
that side, and `TEMP_BOUNDARY` says so. A fixed name built from an argument, `mv "$1.tmp" "$1"`,
is not one expansion, and still reds.

### The admitted rule, S10

```python
TEMP_UNPREDICTABLE = re.compile(r"\$\([ \t]*mktemp(?![\w-])")

def read_temp_binders(code_lines):
    return {name: bool(re.search(r"(?<![\w-])mktemp(?![\w-])", body))
                  and ("${SRANDOM:-" in body or not re.search(r"\$\{?SRANDOM(?![A-Za-z0-9_])", body))
            for name, body in read_function_bodies(code_lines).items() if TEMP_BINDER.search(body)}
```

The test is textual. A body that holds the guard and the `mktemp` fallback in an order that does
not protect the write is admitted, and that is stated in the docstring beside the rule.

### The boundary, S21

`TEMP_BOUNDARY` is a list of `(label, example, class)`. The class is one of `unfollowed`, `unread`
(no `mv` counted), `admitted` and `fixed`. Each row below was run through the designed rules
(§4 Evidence's probe) and lands as shown:

| Label | Example | Class |
|---|---|---|
| a positional source | `f() { mv -f "$1" "$2"; }` | unfollowed |
| a binding that is itself one expansion | `u=$(mktemp -u "$x.XXXXXXXX")`, `t=$u`, `mv "$t" "$x"` | unfollowed |
| a temp bound in another scope | `t="$x.tmp"` in `a()`, `mv "$t" "$x"` in `b()` | unfollowed |
| a loop variable | `for f in a.*; do mv -f "$f" "$f.bak"; done` | unfollowed |
| a binder in a sourced library | `. ./lib.sh`, `name_temp t "$f"`, `mv "$t" "$f"` | unfollowed |
| an mv split across a line continuation | `mv -f \`, then `"$f.tmp" "$f"` on the next line | unfollowed |
| an mv in a case arm | `case $x in a) mv "$f.tmp" "$f" ;; esac` | unread |
| an mv run through a wrapper command | `env mv "$f.tmp" "$f"` | unread |
| an mv named by a path or escaped | `\mv "$f.tmp" "$f"` | unread |
| an mv inside a quoted string or under eval | `eval "mv $f.tmp $f"` | unread |
| a fixed name written with no mv | `printf x > "$f.tmp"` | unread |
| a mktemp temp in another directory | `t=$(mktemp)`, `mv "$t" "$f"` | admitted |
| a name a function prints | `t=$(name_temp "$f")`, `mv "$t" "$f"` | fixed |

The last row is the mode's one known false red: a function that prints an unpredictable name is not
followed into, and its remedy is a binder. `run_temp_scan`'s docstring groups the labels by class,
says which class is gated, and adds Python inside a shell string, which has no shell example. The
README's `--temp-names` section carries the same labels. The wrapper row's prose names `time`,
`nohup`, `xargs` and `command -p` beside `env`.

The boundary arm runs each row through `scan_temp_file` and takes the class whose list is the one
non-empty list, or `unread` when all three are empty. It asserts that class, and that the label sits
in `run_temp_scan.__doc__` and in the README section, each with its whitespace squeezed. The section
is read from `pathlib.Path(__file__).with_name("README.md")`, with `encoding="utf-8"`, cut from the
line opening ``### `--temp-names` `` to the next line opening `## `. The kit ships `include = "**"`
(`tools/gate-lint/kit.toml:10-12`), and the three-prefix leg moves the tree whole, so the README
sits beside the scanner at every prefix. The arm grades that each label is named and that its
example lands in its class. It does not grade that the prose around a label states that class.

### The registry's one line per key, S13

`check_registry(measured, declared, explained=None, listing=None)`. In the `have != want` branch
(`:479-482`) the line gains `listing.get(key, "")` when `listing` is given, so the mismatch line
carries the site lines below it. `run_temp_scan` builds `listing` as at `:1141-1143` and passes it.
The scratch-repository run sits inside the selftest's existing block (`:1366-1422`), which already
holds `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE` out of the environment. The block's tree gains
`t.sh` holding `mv -f "$f.tmp" "$f"`, which carries no probe, so the block's probe-set assertions are
unchanged. Before the block renames `.git` (`:1415`), it writes `t.sh\tfixed-temp\t2\tdrifted` to
a second registry and runs `run_temp_scan` over the tree with `:!*.test.sh`. Exit 1, a stdout
carrying `1 finding(s)`, and `t.sh:1` on the finding is the assertion.

### The cache writer, S8

```bash
    # -I: this program runs from $ROOT, where a top-level tempfile.py would shadow the stdlib module (TOOL-dRedressedBar-26)
    "$PYBIN" -I -c '
```

`-I` drops the script directory and the cwd from `sys.path`, and ignores `PYTHON*` variables and the
user site. The program reads tab-separated ASCII fields from stdin and writes through an explicit
`encoding="utf-8"`, so neither ignored input changes what it writes. The comment line sits inside the
`if` block above the call and adds no compound command.

### The leftover check, S19

```bash
  # A staging name of either spelling the helper writes: <dest>.<digits>.tmp from SRANDOM, and
  # <dest>.XXXXXXXX from its mktemp fallback (TOOL-dRedressedBar-26).
  stg='^gate-full-green\.shared\.'
```

`check_two_writers` plants `gate-full-green.shared`, `gate-full-green.shared.123.tmp` and
`gate-full-green.shared.AbCd1234` in `$t/plant` and checks that `ls "$t/plant" | grep -c "$stg"`
reads 2. The first pass is as today, with its leftover count reading `$stg`. The second pass clears
the shared files, then runs the distinct-names check and the two stampers again, each `bash -c`
handed `unset SRANDOM` on the line above the helper. It checks distinct names, one whole stamp and
no staging file left. That is four checks, so `FLOOR_ASSERTIONS` reads 230, with a comment line in
the form of `:52-55`. On a bash before 5.1 both passes take the `mktemp` branch, which is the host
the finding names.

### The selftest

| Arm | Rows | Assertions |
|---|---|---|
| `temp_cases` | `if mv "$f.tmp" "$f"; then :; fi`, `LC_ALL=C mv "$f.tmp" "$f"` and `command mv "$x.tmp" x`, each a site on line 1; `rename_into() { mv -f "$1" "$2"; }` and the three-line `local src=$1` function, each `([], 0, 1)`; `u=$(mktemp -u "$x.XXXX")`, `t=$u`, `mv "$t" x` as `([], 0, 1)`; `dt() { printf -v "$1" '%s.%s.tmp' "$2" "$SRANDOM"; }`, `dt t "$f" && mv "$t" "$f"` as `([2], 0, 0)` | 7 |
| the `SRANDOM` row | its expectation becomes `([2], 0, 0)` | 0 new |
| lead words | for each word of `TEMP_KEYWORDS + TEMP_PREFIXES`, `<word> mv "$f.tmp" "$f"` is one site on line 1, and TEMP_LEAD skips the word when it is a keyword and not when it is a prefix | 10 |
| boundary | each row of `TEMP_BOUNDARY` | 13 |
| registry, one line per key | `check_registry` with one key declared 1, measured 2 and a listing gives one problem carrying the listing; the scratch-repository run | 2 |

That is 32, the figure §2's floor sentence uses.

### What this unit corrects in spec 24

A corrected paragraph carries `TOOL-dRedressedBar-26` and one sentence naming the change, and this
spec's §2 and §4 hold the design. Under `.claude/roles.json` only `gov-spec-writer` writes spec files,
and scratch-guard admits a builder's spec edit only where it moves the status and date cells of a
spec its card routes (`tools/hooks/scratch-guard.js:91-99`). So the rows below are `<w26>`, M6's "a
review's fixes folded in". It is dispatched once unit 25 is CLOSED, and before this unit's build
pass. If unit 25's own spec-writer pass bumps spec 24, `<w26>` takes the next rev after it. Spec 24
keeps its status. A build pass that finds no `<w26>` returns that to the main loop before any write.

| Spec | Ids | What moves |
|---|---|---|
| 24 | 22, 6, 7, 10, 21, 8, 19 | S3: the program runs under `-I`. S8: TWO counts every `gate-full-green.shared.` staging name, plants one of each spelling, and runs a second pass on the helper's `mktemp` branch. §4 "The class gate" step table: the `an mv` row reads S22's lead run; the `a binder` row admits on `mktemp` with `SRANDOM` only behind `${SRANDOM:-`; the `follow` row makes a positional source and a one-expansion value unfollowed; the `verdict` row admits `$(mktemp` alone. The not-checked paragraph points at `TEMP_BOUNDARY`. The selftest table's `SRANDOM` row reads a site. AC6's anchor line ends `-I -c '`. §3 Edges gains the hands-off. A revision line naming S3, S5, S8 and AC6 |

Id 13 moves no sentence of spec 24, whose §4 says only that a failing key lists its sites. Specs 21
and 22 describe none of this unit's changes: spec 21's `tempfile` lines are the Python writers and
its F1 options, and spec 22 is the profiler. Until `<w26>` lands, an unstaged `memory hygiene` run
reds check 12's reciprocity join on §3's `consumes-from` edge. The staged run holds the joins
(`memory/TEMPLATE-SPEC.md`, "§3 Edges").

### Order, the manifest, and the runner hazards

**Order 20**, one above unit 25's. Unit 25's spec is authored beside this one, so its order 19 is
UNVERIFIED here, and the brief's `--plan` read is what observes the sequence. Both units commit a
kickoff-manifest re-stamp, so M6 sequences them, and that is sequence, not an edge.
`tools/run-gates/run-gates.sh` is on the manifest's `watch:` line (`memory/guides/SESSION-KICKOFF.md:6`),
and `sh_hygiene.py` and the runlog suite are not. No function is minted, so the symbol index does
not move.

Bash reads a script by byte offset as it runs it, so editing `run-gates.sh` under a live run
corrupts that run (`memory/gotchas/suite-edited-while-bash-executes-it.md`). Before the first edit
the build pass reads `$HOME/.gov/gate-turnstile` and the git dir's `gate-run/current` and runs no
bar, as unit 24's did. A diff that edits `run-gates.sh` also makes the close's bar attribute every
red to this run (KF3, `memory/builds/aPairedSlots/RUN.md:18`), and the main loop reads it so.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `TEMP_KEYWORDS`, `TEMP_PREFIXES`, `TEMP_POSITIONAL`, `TEMP_BOUNDARY` | module constants in `sh_hygiene.py` | none |
| `listing` | an optional argument of `check_registry` | none |
| `stg` | a local variable of `check_two_writers` | none |

`python tools/lexicon/lexicon.py --suggest TEMP_KEYWORDS --as py.constant` exits 2 on 2026-10-15,
because `.lexicon.conf` declares no `py.constant` cell, so no convention grades these names. They
follow the file's `TEMP_*` constants. A grep of the tree found none of the four constant names.

### Files touched (estimate)

- `tools/gate-lint/sh_hygiene.py`
- `tools/gate-lint/README.md`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `memory/map/features/gate-lint.md`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/dRedressedBar/build/`

The dossier's line 207 says the remedy names the admitted forms, not three. Spec 24 is `<w26>`'s
write set, not the build pass's.

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| H2 by stripping the segment through TEMP_LEAD and an assignment prefix, then testing for `mv` at its start | TEMP_MV's scan also reads an `mv` after `\|`, `&`, `{`, `(` or `!` inside a segment, which a start-only test loses | Rejected; S22 widens TEMP_MV's lead run |
| `command`, `builtin` and `exec` in TEMP_LEAD as well | none of them runs a shell function, so a binder call after one binds nothing in bash | Rejected; `TEMP_PREFIXES` is TEMP_MV's alone |
| Following a binding two or more hops | the table holds each name's binding as of the `mv`, so `u=a; t=$u; u=b` would read `b`; bind-time resolution is new state the record's fix does not need | Rejected; S21's unfollowed |
| L3 by `os.open` with `O_CREAT\|O_EXCL` on an `os.urandom` name | it spells `mkstemp` inline beside the shape units 21 and 24 standardised, and leaves the next import the program gains loading from the cwd | Rejected; S8's `-I` |
| L3 by `-P` | it needs Python 3.11, and the resolver admits any working `python3`, `python` or `py` | Rejected |
| L3's class here, `-I` on all five programs and the record's static arm | the four others predate the fold and no confirmed finding names them | Handed off (§3) |
| L4 by running the arm on the `mktemp` branch alone | a 5.1 host then never grades the `SRANDOM` branch it ships | Rejected; two passes |
| L5 by dropping `check_registry`'s mismatch line for this mode | that line is the one the other three modes print, and the listing is what a reader needs to fix the key | Rejected; S13 appends the listing |
| The boundary read out of the docstring's prose | a prose parser grades whatever a sentence happens to say | Rejected; one table both docs name |
| M4 by refusing `SRANDOM` in any binder | the runner's hot sites fork nothing on 5.1 and later through `derive_temp_path`'s `SRANDOM` branch (spec 24 §4) | Rejected; the guarded binder stays admitted |

## 5. Production-readiness checklist

- security — The lint now reds a fixed-name temp renamed through `if ! mv`, `command mv` or a prefix
  assignment, and a bare `SRANDOM` name, which a planter can know on bash before 5.1. The cache
  writer no longer imports a module from the repository top. What stays open: §3's four programs,
  the 13 boundary rows, and the static binder test (§4).
- perf / scale — The lint reads the same population in the same pass. The selftest adds 32
  assertions and one `run_temp_scan` over a repository it already builds. TWO's second pass adds
  about 50 `bash -c` runs and 50 `mktemp` forks, an ESTIMATE of 10 to 20 s under MSYS, not measured.
  `-I` costs nothing.
- error / empty / loading states — A drifted key prints one finding with its sites. A positional or
  one-expansion source prints as unfollowed.
- observability — The count-mismatch line carries the site listing.
- risks — An adopter whose registry counted a positional or two-hop source sees its count fall, and
  the shrink-only rule reds the row until it is lowered. The home tree measured no such site. An
  adopter with a bare `SRANDOM` site reds, which is the finding.
- testing — Every criterion is a direct run of the scanner over text, a scratch repository or the
  tree, a `-c` program run beside a planted module, and bash and `grep` probes over the runlog
  suite and specs. The arms are §7's.
- migration — None. The registry's grammar is unchanged, and `listing` defaults to `None`.
- user docs — `tools/gate-lint/README.md`'s `--temp-names` section and the gate-lint dossier's
  line. No `help/` page covers gate-lint.

## 6. Acceptance criteria

The numbering follows report ids, and AC24 is the record. `<p26>` is the product commit, `<p26m>`
the manifest re-stamp and `<w26>` the spec-writer commit, each named in the ledger. `<pre>` is
`<p26>~1`. `<sh>` is `python tools/gate-lint/sh_hygiene.py`. `<scan> <text>` is a python program
that puts `tools/gate-lint` on `sys.path`, imports `sh_hygiene`, runs `scan_temp_file(<text>)` and
prints the fixed lines, the admitted count and the unfollowed count. "Over `<pre>`" runs the same
program over `git show <pre>:tools/gate-lint/sh_hygiene.py` written into a scratch dir. `<rg>` and
`<rl>` are run-gates.sh and run-gates.runlog.test.sh under tools/run-gates/, spelled through
placeholders because the spec-token checker reads a backticked runner path as an invocation. `<t>`
is a fresh dir under `%TEMP%`, and `<s24>` is spec 24's file. "Joined" means whitespace squeezed to
single spaces. Commands run from the worktree root on node d.

- **AC22** — `<scan>` over `command mv -f "$f.tmp" "$f"`, `builtin mv "$f.tmp" "$f"`,
  `exec mv "$f.tmp" "$f"`, `LC_ALL=C mv -f "$f.tmp" "$f"` and `A=1 B="x y" mv -f "$f.tmp" "$f"`
  reads `([1], 0, 0)` for each. `<scan>` over `echo then mv x.tmp x` reads `([], 0, 0)`.
  `<sh> --temp-names` with the registry `memory/project/temp-name-sites.txt`, root `.`, and the
  pathspecs `:!*.test.sh` and `:!memory/` exits 0, and its OK line counts 20 registered sites in 14
  rows.
  Red when: over `<pre>` each of the five reads `([], 0, 0)`, the `mv` not even counted.
  figure: 20 in 14 PINNED at `bc6a4c9f0` on 2026-10-15 (§4 Evidence); DERIVED at observation.
- **AC6** — `<scan>` over `if mv "$f.tmp" "$f"; then :; fi`, `if a; then :; elif mv "$f.tmp"
  "$f"; then :; fi`, `while mv "$f.tmp" "$f"; do :; done` and `until mv "$f.tmp" "$f"; do :; done`
  reads `([1], 0, 0)` for each. An `ast` walk of `sh_hygiene.py` finds the module-level assignments
  to `TEMP_MV` and `TEMP_LEAD` each holding the name `TEMP_KEYWORDS`, and no string constant inside
  either spelling `elif`. For every word of `TEMP_KEYWORDS`, `TEMP_LEAD.match(word + " t=x").end()`
  equals `len(word) + 1`.
  Red when: over `<pre>` the four read `([], 0, 0)`, and TEMP_MV's literal spells `then|do|else`
  while TEMP_LEAD's spells seven words.
- **AC7** — `<scan>` over `rename_into() { mv -f "$1" "$2"; }`, over `g() {`, `  local src=$1`,
  `  mv -f "$src" "$2"`, `}` on four lines, over `h() { mv -f "${1}" "$2"; }` and over
  `h() { mv -f "$@"; }` reads `([], 0, 1)` for each. `<scan>` over `mv "$1.tmp" "$1"` reads
  `([1], 0, 0)`, so a fixed name built from an argument still reds.
  Red when: over `<pre>` the first two read `([1], 0, 0)` and `([3], 0, 0)`.
- **AC10** — `bash -c 'unset SRANDOM; f=/x/d; t="$f.$SRANDOM$SRANDOM.tmp"; printf %s "$t"'` prints
  `/x/d..tmp`. `<scan>` over `t="$f.$SRANDOM$SRANDOM.tmp"` then `mv -f "$t" "$f"` reads
  `([2], 0, 0)`, and over `dt() { printf -v "$1" '%s.%s.tmp' "$2" "$SRANDOM"; }` then
  `dt t "$f" && mv "$t" "$f"` reads `([2], 0, 0)`. `<scan>` over the line
  `sed -n '/^derive_temp_path()/p'` prints from `<rg>`, then `derive_temp_path t "$f" && mv -f
  "$t" "$f"`, reads `([], 1, 0)`. `sh_hygiene.TEMP_REMEDY` carries `mktemp -u` and `${SRANDOM:-`
  and no `$SRANDOM$SRANDOM`. The README's `--temp-names` section, joined, carries no
  `$SRANDOM$SRANDOM`, and `grep -c 'three admitted forms' memory/map/features/gate-lint.md`
  prints 0.
  Red when: over `<pre>` the bare form and the unguarded binder each read `([], 1, 0)`, and
  TEMP_REMEDY carries `$SRANDOM$SRANDOM`.
- **AC21** — `<scan>` over `u=$(mktemp -u "$x.XXXX")`, `t=$u`, `mv "$t" x` on three lines reads
  `([], 0, 1)`, and over `command mv "$x.tmp" x` reads `([1], 0, 0)`. A python program reads
  `sh_hygiene.TEMP_BOUNDARY`: it holds at least 13 rows, and each row's example lands in its
  class alone by §4's rule. Each label sits in `run_temp_scan.__doc__`, joined, and in the README's
  `--temp-names` section, joined. The docstring carries no `never a false red` and carries
  `false red`.
  Red when: over `<pre>` the two-hop text reads `([3], 0, 0)`, `command mv` reads `([], 0, 0)`,
  and the docstring carries `each a MISS and never a false red` while naming neither form.
  figure: 13 rows PINNED by §4's table on 2026-10-15; the count is DERIVED from the constant at
  observation.
- **AC8** — A python program reads `<rg>`, finds the line opening `' "$REUSE_CACHE"` and the nearest
  line above it ending `-c '`, and takes the program between them. The flags on that line between
  `"$PYBIN"` and `-c` read `-I`. It writes `<t>/top/tempfile.py` holding
  `raise SystemExit("SHADOWED")` and runs `sys.executable` with those flags, `-c`, the program and
  `<t>/cache`, in cwd `<t>/top`, with the stdin row `abcdef`, `3`, `r1`, `sha`, `1700000000`, `0`,
  tab-separated. It exits 0, and `<t>/cache/ab/` lists exactly `abcdef`.
  Red when: the same run with no flags, as at `<pre>`, into `<t>/cache2`, exits 1 printing
  `SHADOWED`, and `<t>/cache2/ab/` does not exist.
- **AC19** — `sed -n "s/^  stg='\(.*\)'$/\1/p" <rl>` prints the pattern `^gate-full-green\.shared\.`.
  With `<t>` holding `gate-full-green.shared`, `gate-full-green.shared.1234567890.tmp` and
  `gate-full-green.shared.AbCd1234`, `ls <t> | grep -c` over that pattern prints 2. A bash probe
  runs the line `sed -n '/^derive_temp_path()/p'` prints from `<rg>` under `unset SRANDOM`, then
  `derive_temp_path _tp <t>/x/gate-full-green.shared`, and the name it prints matches the pattern.
  `sed -n '/^check_two_writers()/,/^}/p' <rl> | grep -c 'unset SRANDOM'` prints at least 2, and
  `grep -c '^FLOOR_ASSERTIONS=230$' <rl>` prints 1.
  Red when: the pattern as at `<pre>`, `^gate-full-green\.shared\..*\.tmp$`, counts 1 of the
  planted two, and does not match the name the `mktemp` branch prints.
- **AC13** — A python program, with `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE` held out of its
  environment, makes `<t>/r` a git repository whose one tracked file `t.sh` holds
  `mv -f "$f.tmp" "$f"`. It writes `<t>/reg.txt` holding `t.sh`, `fixed-temp`, `2`, `drifted`,
  tab-separated. `<sh> --temp-names <t>/reg.txt <t>/r` exits 1, its stdout carries
  `1 finding(s)`, and that one finding carries `the scan measures 1` and `t.sh:1`.
  `inspect.signature(sh_hygiene.check_registry)` names `listing`.
  Red when: over `<pre>` the same run prints `2 finding(s)`.
- **AC24** — `git diff <w26>~1 <w26> -- memory/builds/dRedressedBar/spec/` shows `<s24>` with one
  header rev change and one new revision line, which names `TOOL-dRedressedBar-26` and ids 22, 6,
  7, 10, 21, 8 and 19. `<s24>` carries a CLOSED header at `<w26>~1`, and a §3 bullet `hands-off`
  `TOOL-dRedressedBar-26` at `<w26>`. `git diff --name-only <p26>~1 <p26> --
  memory/builds/dRedressedBar/spec/` names no file but this spec. `git log -1 --format=%B <p26m>`
  carries `manifest-audit:`, and the `last-audit:` line of `memory/guides/SESSION-KICKOFF.md`
  names a commit at which `<rg>` carries `"$PYBIN" -I -c`. The ledger S24 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-26`.
  Red when: spec 24 takes no bump or two, its revision line misses one of its ids, the stamp names
  a commit before `<p26>`, or a build-pass commit writes another spec.

## 7. Gates

`shell-hygiene selftest` · `shell hygiene (a fixed-name temp renamed into place)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `measure-legs selftest` · `run-gates run-log line` · `run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `foreign-prefix parity (every self-test at three prefixes)` · `spawn budget (forks per hot entrypoint)` · `python resolver (behaviour + inline parity + idiom ban)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `install-prefix (shipped surface)` · `govkit selfcheck` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `testsuite counts (every bar self-test prints one)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The line is a floor. Joined against the guards in `tools/gate-legs.json` with `BROAD_LEG_FLOOR`
(`tools/check-spec-tokens.py:262`, 5) applied, §4 Files touched owes `shell-hygiene selftest`,
`measure-legs selftest`, `recall floor` and `recall floor arms`. The rest are legs the change moves:
the four modes `sh_hygiene.py` serves, the runner and the suites that run it, its inline
interpreter, the kits' shipped bytes, the selftest's new text IO, the manifest, the suite counts,
and this spec.

New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC22 AC6 · the lead-word arm and the `if`, `LC_ALL=C` and `command` rows over a copy whose TEMP_MV is the one at `<pre>` · raise `FLOOR_ASSERTIONS` from 92 to the count printed
New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC7 AC21 · the two positional rows, the two-hop row and the boundary arm over a copy whose follow step is the one at `<pre>`, and the boundary arm again with one label taken out of `run_temp_scan`'s docstring · none
New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC10 · the `SRANDOM` row and the unguarded-binder row over a copy whose TEMP_UNPREDICTABLE and binder test are the ones at `<pre>` · none
New arm: tools/gate-lint/sh_hygiene.py --selftest · covers AC13 · the one-line-per-key unit row and the scratch-repository run over a copy whose `run_temp_scan` appends its second mismatch line, as at `<pre>` · none
New arm: tools/run-gates/run-gates.runlog.test.sh · covers AC19 · TWO with its leftover pattern as at `<pre>`, where the planted pair counts 1 and the `mktemp`-branch pass would leave a staging name uncounted · raise `FLOOR_ASSERTIONS` from 226 to 230

The main loop observes each new or moved arm red on its staged break, then green, at the close, and
runs the bar once after the last unit is terminal. AC8 has no arm: the record's arm for its class is
handed off (§3).

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-15 · initial draft, promoted from the round-2 closing diff review's temp-name lint
  and runner temp findings by the owner's ruling of 2026-10-15. Report ids 22, 6, 7, 10, 21, 8, 19
  and 13 are batched by M4. Every finding was reproduced at `bc6a4c9f0`, whose `tools/` equals the
  reviewed tip's, and the designed rules were measured over the leg's population: 68 sources, 20
  sites in 14 files, unchanged. The shadowing class over the runner's other four `-c` programs and
  the record's two checklist lines are handed off.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "one keyword list shared by two shell command-word
predicates so an mv after if or a prefix assignment is read"` ranked name-stem matches only (`read`,
`read_text`, `read_conf`) and no shell-grammar seam. `python tools/codebase-map/reuse_lookup.py
"registry count mismatch line carrying the scanned site listing so one drifted key is one finding"`
ranked `key`, `counts` and `load_registry` by stem, and none reports a registry drift. Both are
recorded as misses, and no existing seam outside the file fits. The seams extended are the scanner's
own: `scan_temp_file` (`tools/gate-lint/sh_hygiene.py:1008`), whose follow step S7 and S21 widen;
TEMP_LEAD (`:972`), which S6 derives from the list TEMP_MV now reads; `read_temp_binders` (`:999`),
which S10 narrows; and `check_registry` (`:457`), whose optional `explained` argument is the shape
S13's `listing` follows. The selftest reuses `test`, the `temp_cases` loop (`:1527-1531`) and the
scratch-repository block with its `GIT_DIR` hold (`:1366-1422`). The README read follows unit 22's
`test_signal_docs`, a selftest that grades a kit README's section against the code. The admitted
binder shape is `derive_temp_path` (`tools/run-gates/run-gates.sh:779`). S19 reuses the TWO arm's own
`hp` and `sg` extraction (`tools/run-gates/run-gates.runlog.test.sh:1068-1072`).

The recall probe returned spec 24 and its ledger, the round-2 record, spec 21, the brief, and
`TOOL-cMendedVintage-2`, which made the registry argument optional, the three states S13 keeps. It
also returned `TOOL-dRemeasuredRender-2`, an open ask on the `--location-probes` mode's reading of a
redirect before `&&`. That ask is the location-probe mode's and not this unit's. The record and the
code agree on every citation re-read, with the two offsets §4 Evidence names.

The gotchas checklist for this unit's paths selected these classes, each answered here:
- `fixture-passes-by-finding-nothing`: every boundary row asserts the class it lands in, the
  lead-word arm asserts one site per word, AC7 keeps a fixed argument-built name red, and S19 plants
  a pair before it trusts a zero.
- `two-answers-to-one-question`: the class of id 6, which `TEMP_KEYWORDS` closes, and of id 21's
  docs, which `TEMP_BOUNDARY` and the boundary arm close.
- `guard-above-a-fold-makes-its-fallback-dead`: S10 admits `SRANDOM` only beside its `${SRANDOM:-`
  guard and the `mktemp` fallback, and S19's second pass runs that fallback.
- `staged-break-substitutes-a-synthetic-value`: S19 forces the fallback by `unset SRANDOM` on the
  shipped helper, not by a substitute helper.
- `inherited-git-dir-pins-the-work-tree-to-the-cwd`: S13's scratch run sits inside the block that
  already holds `GIT_DIR` out.
- `heredoc-escape-reaches-the-regex`: §4's regexes are raw strings in the file, written with the
  edit tool and never through a shell heredoc.
- `amendment-leaves-its-other-half-standing`: S10's rule moves in five texts at once, the remedy,
  the label, the module docstring, the README and the dossier, and `<w26>` moves spec 24's copy.

Recall terms used: `python tools/memory-recall/query.py "where can a shell command word start for
the temp-name lint, and when is a SRANDOM temp name unpredictable on older bash" --terms "TEMP_MV
TEMP_LEAD sh_hygiene temp-names SRANDOM mktemp positional unfollowed binder check_registry isolated
shadow"`
