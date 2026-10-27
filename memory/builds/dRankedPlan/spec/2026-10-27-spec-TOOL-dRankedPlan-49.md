# TOOL-dRankedPlan-49 — a shell word naming a variable bound to a `ratify.py` path names `ratify.py`

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 21 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-49-deviation-491.md](../build/2026-10-27-build-TOOL-dRankedPlan-49-deviation-491.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 38 to 45
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md`) confirmed
**finding 33 at HIGH**, item **H3**. `TOOL-dRankedPlan-45` S3 resolves a script path bound to a name and
invoked through the name, for Python only. In shell, `r="$d/ratify.py"; "$py" "$r" "$slug"` has no
later word ending `ratify.py`, so under `TOOL-dRankedPlan-32` S2 it is not an invocation, and
`TOOL-dRankedPlan-38`'s textual rule matches only the predicate's name. `TOOL-dRankedPlan-39`'s table
"The forms read" names only a call assembled at run time as unread, and a variable bound to a literal
path is not that. The repository writes this shape, `.githooks/commit-msg:76` and :104, so a hook
following it passes the always-run ban. This unit is S3's shell twin: a `$name` word is resolved
through the file's assignments to that name. It repairs `TOOL-dRankedPlan-45`, whose S3 has no shell
twin, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The bindings. `read_shell_callers` (`TOOL-dRankedPlan-32` S2, over `TOOL-dRankedPlan-41`
  S3's commands) collects every assignment word `NAME=value` in the file: the leading assignment words
  of a command, and the assignment words after `local`, `export`, `readonly`, `declare` or `typeset`.
  A value is compared with its quote characters stripped. Observed by AC1 and AC3.
- **S2** — The resolution. Wherever unit 32 S2 compares a word with `ratify.py`, a word that is
  `$name` or `${name}`, quotes stripped, names `ratify.py` when any assignment to `name` anywhere in the
  file has a value ending in `ratify.py`. One such assignment is enough, so assignments that disagree
  fail closed, and an assignment after the use counts, because a function may be called after the
  line that binds its variable. Both invocation forms of unit 32 S2 read the resolved word, and its
  mode-flag rule applies unchanged. Observed by AC1, AC2 and AC3.
- **S3** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors. Observed by AC1, AC2 and AC3.
  - `caller-shell-bound` plants a `.githooks/pre-commit` holding `r="$d/ratify.py"` and then `"$py"
    "$r" "$slug"`. It is refused.
  - `caller-shell-bound-exit` plants the same two lines with `--exit` after `"$slug"`. It is admitted.
  - `caller-shell-bound-local` plants a function whose body holds `local r="$d/ratify.py"` and then
    `"$py" "${r}" "$slug"`. It is refused.
- **S4** — The forms table. This unit's §4 "The reading after this unit" adds the bound-variable form
  to the forms `TOOL-dRankedPlan-39` §4 "The forms read" lists, and the two tables are read together.
  Unit 39's spec text is not edited, because it builds at order 8. NOT OBSERVED by a criterion: it is
  a record correction, which the plants observe in behaviour.

## 3. Non-goals (OUT)

- A variable bound in another file that the hook sources, or bound to the output of a command
  substitution whose text does not end in `ratify.py`. Both are run-time assembly, unread as
  `TOOL-dRankedPlan-32` §3 states.
- The Python twin: `TOOL-dRankedPlan-45` S3, unchanged.
- Scoping a binding to its function. A file-wide reading fails closed, and the tree's bindings are
  file-scoped.

### Edges

- **consumes-from** `TOOL-dRankedPlan-45` — S3's bound-name rule for Python, whose shell twin this unit adds; without it the two readers would disagree on the same shape
- **consumes-from** `TOOL-dRankedPlan-41` — S3's commands and words from the shared tokenizer, over which S1 collects the assignments; without them there is no word to resolve

## 4. Design

### Evidence

- `.githooks/commit-msg:76` reads `if [ -f "$base/transition_audit.py" ]; then
  module="$base/transition_audit.py"; break; fi`, and :104 reads `"$py" "$module" --staged`.
- `TOOL-dRankedPlan-32` S2 reads the "first later word not beginning `-`", which is `"$r"` there, and
  `TOOL-dRankedPlan-39` §4 "The forms read" lists no bound-variable row.
- `TOOL-dRankedPlan-45` S3 resolves a Python `Name` through module-level and function-local
  assignments, the rule S2 mirrors.

### The reading after this unit

| Hook lines | Script word | Answer |
|---|---|---|
| `r="$d/ratify.py"`, then `"$py" "$r" "$slug"` | `"$r"`, resolved to `$d/ratify.py` | caller |
| the same, with `--exit` | resolved | not a caller |
| `r="$d/other.py"` and `r="$d/ratify.py"`, then `"$py" "$r"` | one value ends `ratify.py` | caller |
| `r=$(pick_script)`, then `"$py" "$r"` | unresolved | unread, run-time assembly |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `caller-shell-bound`, `caller-shell-bound-exit`, `caller-shell-bound-local` | `ratify.py` fixture plants | none |

### Rollout

Live at landing, at order 21. Units 46 to 49 share order 21 and all write `tools/loop/ratify.py`, so
by BUILD-METHOD M6 clause 1 they are sequenced inside that step.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Bind only the nearest earlier assignment.** It needs a flow reading of `if`, `case` and function
  calls to be right, and a wrong answer fails open. The file-wide rule fails closed on the same input.
- **Name the bound-variable form as unread.** It is the repository's own hook pattern, so the ban would
  certify an absence over the shape the next hook will copy.

## 5. Production-readiness checklist

- security — narrows: the repository's bound-path hook pattern is read by the deny-by-default ban.
- perf / scale — one pass over each tokenized shell file's assignment words.
- error / empty / loading states — a `$name` with no assignment in the file resolves to nothing, and is
  read as unit 32 S2 reads it today.
- observability — the refusal names the file and the invoking command's line.
- risks — a name reused for an unrelated path in the same file fails closed.
- testing — the three plants, red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-bound` runs, the check exits 1
  naming `.githooks/pre-commit` and the line of `"$py" "$r" "$slug"`.
  Red when: a script path bound to a variable passes the ban.
- **AC2** — When the plant `caller-shell-bound-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a bound `--exit` call is refused.
- **AC3** — When the plant `caller-shell-bound-local` runs, the check exits 1 naming the
  `"${r}"` line.
  Red when: a `local` binding or the `${name}` spelling is not resolved.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest` is owed once dDeclaredLoop's loop legs are in the manifest, and this unit's pass names it
on the line above then, by `TOOL-dRankedPlan-45` S17's rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 · the three `caller-shell-bound*` plants, staged by a reader that compares a `$name` word with `ratify.py` unresolved · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 38 to 45, finding 33 (HIGH,
  item H3), repairing `TOOL-dRankedPlan-45`.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-32`'s `read_shell_callers` over `TOOL-dRankedPlan-41`'s token
stream, and the rule mirrored is `TOOL-dRankedPlan-45` S3's Python bound-name resolution. `python
tools/codebase-map/reuse_lookup.py "find which command a shell heredoc or wrapper function runs and
read its script argument"` ranked name stems only (`read`, `run`, `run_git`), and none reads a shell
assignment, so no seam fits beyond the reader. The recall query returned units 38, 40 and 41 and this
audit's items, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does a shell reader resolve heredoc bodies wrappers and bound variables to a script invocation" --terms "heredoc interpreter wrapper timeout function variable assignment tokenizer brace subshell string literal caller"`
