# TOOL-dRankedPlan-32 — the caller predicate reads invocations by their structure, so an argv list counts and a resolver line does not

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 7 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-30-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-30-promoted-fix-return.md) | research | TOOL-dRankedPlan-30 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 |
| [2026-10-27-build-TOOL-dRankedPlan-32-deviation-321.md](../build/2026-10-27-build-TOOL-dRankedPlan-32-deviation-321.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md) | research | TOOL-dRankedPlan-30 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 19 to 29
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`) confirmed
**finding 30 at HIGH**, item **H7**. The skeptic judged the finder's fix unsound and wrote the corrected
one this unit takes. `TOOL-dRankedPlan-22` S2 counts a caller only as a code line matching
`\bread_plan_ratification\s*\(` or "a shell line invoking `ratify.py`" with no `--` argument. That
misses the repository's usual cross-kit call form, a Python argv list such as `[sys.executable,
str(kit / "map_diff.py"), "--stale-dossiers", "--json"]` (`tools/drift-audit/drift_report.py:3433`).
It also misses an import alias and a bare reference. On the other side, a plain reading of "invoking"
flags the resolver line `resolve_kit_dir "$py" drift-audit drift_report.py "$KIT_DIR"`
(`tools/unattended/unattended.sh:1268`), whose `ratify.py` twin `TOOL-dRankedPlan-10` S6 adds to the
driver. This unit reads each statement by its structure. Python is read through `ast`, a shell
command by the position of the script word, and an argv list or a continued shell line is judged whole,
so flags on a later line are seen. It repairs `TOOL-dRankedPlan-22`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — Python, read by `read_python_callers(path, text)` in `tools/loop/ratify.py`. Observed by
  AC1, AC2 and AC3. Only a file whose text names `ratify.py` or `read_plan_ratification` is parsed,
  with `ast.parse`. A file that does not parse exits 2 naming it. Three forms are callers:
  - a **reference**: a `Name` or an `Attribute` spelled `read_plan_ratification`, or an `import` or
    `from … import` binding it under any alias, whether called or not;
  - an **argv list**: a `List` or `Tuple` literal with an element naming `ratify.py`, which is a
    `str` constant ending in `ratify.py` anywhere inside that element, such as `str(kit /
    "ratify.py")`. The element sits at index 1 or later after `sys.executable`, any other `Name` or
    `Attribute`, or a `str` constant whose last path segment is `python`, `python3` or `py`. Or it
    sits at index 0 beside an element that is not a `str` constant ending in `.py`. The list is a
    caller unless one of its `str` constants is in `RATIFY_MODE_FLAGS`;
  - an **in-process call**: a `Call` of `.main` on a name bound by importing the module `ratify`. It
    is a caller unless the `str` constants of its arguments carry a mode flag.
- **S2** — Shell, read by `read_shell_callers(path, text)` over `*.sh` and every file under
  `.githooks/`. Backslash-continued lines are joined, and each line is split into commands at `;`,
  `&&`, `||`, `|`, `$(`, a backtick and `(`. Words are read by `shlex.split` with comments ignored, and
  leading `NAME=value` words are skipped. A command invokes `ratify.py` in one of two ways. Its first
  word ends in `ratify.py` and no other word ends in `.py`. Or its first word is an interpreter, meaning
  `python`, `python3`, `py` or a `$` variable such as `"$py"`, and its first later word not beginning
  `-` ends in `ratify.py`. An invocation is a caller unless one of its words is in
  `RATIFY_MODE_FLAGS`. A resolver call, a file test and an `echo` that name the file put it at the
  third word or later, so none is an invocation. Observed by AC3 and AC4.
- **S3** — JavaScript, read by `read_js_callers(path, text)` over `*.js`. An array literal is read
  from its `[` to the matching `]`, joined across lines with string literals respected. It is an
  invocation when one of its string elements ends in `ratify.py`, and it is a caller unless one of
  its string elements is a mode flag. NOT OBSERVED by a criterion: no tracked `*.js` file invokes a
  kit's Python script at base (§4 "The probe over the tree"), so no plant has a real shape to copy.
  The reader exists so the population that unit 22 S2 declares is read whole.
- **S4** — The mode flags. `RATIFY_MODE_FLAGS = ("--exit", "--exited", "--fixture", "--check-callers")`
  in `ratify.py` names the flags that choose a mode other than the predicate: the exit act's answer
  (`TOOL-dRankedPlan-10` S3), the crossing reader (`TOOL-dRankedPlan-21` S1), the fixture
  (`TOOL-dRankedPlan-9` S7) and this check (`TOOL-dRankedPlan-22` S2). Observed by AC3 and AC4.
- **S5** — The check re-pointed. `check_predicate_callers(root)` (`TOOL-dRankedPlan-22` S2) asks the
  reader for each tracked file's kind and reports each caller at its statement's first line. This
  supersedes unit 22 S2's sentence that defines a caller. Unit 22's refusal line, pass line, exit codes
  and population stand. Observed by AC1 to AC4.
- **S6** — The plants. Observed by AC1, AC2 and AC3. Four plants join `ratify.py --fixture --plant
  <case>`, each in its own scratch repository:
  - `caller-argv` plants a module whose argv list spans three lines and passes a slug and no flag. It
    is refused.
  - `caller-alias` plants `from ratify import read_plan_ratification as rpr`. It is refused.
  - `caller-resolver` plants a `.githooks/pre-commit` holding the resolver line `d=$(resolve_kit_dir
    "$py" loop ratify.py "$KIT_DIR")` and a file test `[ -f "$d/ratify.py" ]`. It is admitted.
  - `caller-argv-exit` plants the `caller-argv` list with `"--exit"` on its last line. It is
    admitted.

## 3. Non-goals (OUT)

- Which files may call the predicate: `TOOL-dRankedPlan-30` derives that set.
- The leg that runs the check over the tree: `TOOL-dRankedPlan-31`'s.
- Plants for the shell form unit 22 S2 already names, meaning a bare `ratify.py "$slug"` hook and an
  `--exit` one (finding 31): `TOOL-dRankedPlan-37`'s.
- A call assembled at run time, by `getattr`, `importlib` or a command string built from pieces. It
  stays invisible, as unit 22 §5 states.

### Edges

- **consumes-from** `TOOL-dRankedPlan-22` — `check_predicate_callers`, its population and its lines, whose caller definition S5 re-points; without them there is no check to widen
- **consumes-from** `TOOL-dRankedPlan-10` — S6's driver arm in `tools/unattended/unattended.sh`, the resolver line and `--exit` invocation AC4 reads in the real tree; without it AC4 sees no resolver line
- **hands-off** `TOOL-dRankedPlan-37` — S2's shell reading, over which that unit's item for finding 31 plants the bare `ratify.py "$slug"` hook and its `--exit` twin

## 4. Design

### Evidence

- `tools/drift-audit/drift_report.py:3433` calls `[sys.executable, str(kit / "map_diff.py"),
  "--stale-dossiers", "--json"]`, and `tools/drift-audit/selftest.py:2061` calls `[sys.executable,
  str(r / KIT_NAME / "drift_report.py"), "--check"]`. These are the repository's cross-kit form.
- `tools/codebase-map/selftest.py:246` and :255 set `_sys.argv = ["map_diff.py", ...]` and call
  `md.main()` in process.
- `tools/unattended/unattended.sh:1268` resolves with `resolve_kit_dir "$py" drift-audit
  drift_report.py "$KIT_DIR"`, and :1272 invokes `"$py" "$d/drift_report.py" --delta "$base" HEAD`.
- `tools/govkit/selftest.py:115` holds `("drift-audit", "drift_report.py")` as a data tuple, the shape
  of `TOOL-dRankedPlan-30`'s anchors.

### The probe over the tree

The H7 left-shift asks that a textual predicate be run over the real tree, with its hits and misses
recorded, before it is pinned. `ratify.py` does not exist at base 0689e7fa, so S1 and S2 were run over
analogue kit scripts that do. Both were measured 2026-10-27 with a scratch probe, so the counts are
PINNED.

| Rule | Analogue | Statements naming it | Flagged | Every flag an invocation | Every miss a non-invocation |
|---|---|---|---|---|---|
| S1 argv list | `drift_report.py`, `map_diff.py` | 6 list literals | 4: drift_report.py:3433, drift-audit selftest :2061, codebase-map selftest :246 and :255 | yes | yes: drift-audit selftest :359, a pair of file names, and govkit selftest :115, an anchor pair |
| S2 shell | `drift_report.py` | 10 | 1: unattended.sh:1272 | yes | yes: the resolver at :1268, the `echo` at :1269, and `check-kit-versions.sh` :129, :342 and :346 |
| S2 shell | `gen_build_index.py` | 69 | 26, every one through an interpreter word | yes | yes: assignments such as `PARITY_EXEMPT=…`, `echo` text, `resolve_kit_dir` lines and a quoted expected string |

The first S2 draft flagged `PARITY_EXEMPT="… gen_build_index.py"` (`tools/check-spec-tokens.test.sh:869`)
and a word list split across lines. Skipping assignment words and requiring a lone `.py` word at
position 0 removed both, so the table reflects the rule as written. One miss class stays, which is a
heredoc line that reads as a command. It is deny by default, so it fails as a refusal and never as a
pass. No tracked `*.js` invokes a kit's Python script. `drift-audit-code.js:7` names `drift_report.py`
inside prose only, which S3 does not read as an element ending in the name.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_python_callers`, `read_shell_callers`, `read_js_callers` | functions, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for each |
| `RATIFY_MODE_FLAGS` | constant, `ratify.py` | none declared |
| `caller-argv`, `caller-alias`, `caller-resolver`, `caller-argv-exit` | `ratify.py` fixture plants | none |

### Rollout

Live at landing. At this unit's tip the real tree holds `TOOL-dRankedPlan-10` S6's resolver line and
`--exit` call in the driver, and `TOOL-dRankedPlan-9`'s `--fixture` call in the loop selftest, so AC4
reads the admitted shapes in place.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S6

### Alternatives rejected

- **The skeptic's textual rule with named exemptions for `resolve_kit_dir` lines and file tests.** An
  exemption list grows with every new resolver spelling, such as `resolve_carrier_kit` at
  `tools/check-kit-versions.sh:129`. The position rule exempts them all by structure.
- **A regex over Python source.** It cannot tell a docstring from code, or a three-line argv list from
  three unrelated lines. `ast` sees both, and the textual prefilter keeps it to the few files that
  name the script.

## 5. Production-readiness checklist

- security — deny by default widens to the argv-list, alias and in-process forms; every unread form is
  named in §3.
- perf / scale — the textual prefilter means only files naming the script are parsed: 14 of 157 tracked
  `*.py` files for the analogue, measured 2026-10-27.
- error / empty / loading states — an unparsable Python file exits 2 naming it, never skipped.
- observability — each refusal names the file and the statement's first line.
- risks — a heredoc line shaped like a command is refused, which fails closed.
- testing — four plants, red and green, and AC4's run over the real tree.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-argv` runs, the check exits 1 and names the
  planted module at the first line of its three-line argv list.
  Red when: an argv-list invocation of the predicate's CLI passes the check.
- **AC2** — When the plant `caller-alias` runs, the check exits 1 and names the import line.
  Red when: an aliased import of `read_plan_ratification` passes.
- **AC3** — When the plants `caller-resolver` and `caller-argv-exit` run, each check exits 0 and
  prints `ratify — callers:`.
  Red when: a resolver line, a file test or an `--exit` list on a later line is refused.
- **AC4** — When `python ratify.py --check-callers` runs over this repository at the pass tip, it
  exits 0, while `grep -c "ratify.py" tools/unattended/unattended.sh` prints at least 1 for
  `TOOL-dRankedPlan-10` S6's resolver line and `--exit` call.
  Red when: the driver's resolver line or its `--exit` arm is refused in the real tree.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the four `caller-*` plants under `--fixture`, staged by a predicate that matches only `read_plan_ratification(` on one line · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 19 to 29, finding 30 (HIGH,
  item H7), repairing `TOOL-dRankedPlan-22`.

## 10. Reuse audit

No existing seam fits the reader. `python tools/codebase-map/reuse_lookup.py "find every place a
script is invoked by a subprocess argv list or a shell command"` ranked `read_id_list`,
`parse_shell_defs` (`tools/lexicon/lexicon.py:747`, which reads shell function definitions) and
`resolve_shell_argv` (`tools/govkit/govkit.py:1200`, which rewrites a leading `bash`). Neither of the
last two reads an invocation, as their docstrings state. The rule reused is the code-line
rule of `tools/workflows/check-review-join.sh`, which unit 22 already cites. The recall query returned
TOOL-dTotalRecall-13's scout row and this audit's H7 item, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how is a caller of a script found across shell and python files" --terms "caller predicate argv list subprocess sys.executable resolve_kit_dir invocation import alias ast shell continuation"`
