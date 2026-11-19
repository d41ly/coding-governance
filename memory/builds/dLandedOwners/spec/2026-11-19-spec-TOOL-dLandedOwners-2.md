# TOOL-dLandedOwners-2 — the reader scan reads a key passed to a reader through a module constant

**Status:** SPECCED · rev-1 · 2026-11-19 · node d · Tier-2 · base 51971579 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-prompt-TOOL-dLandedOwners-1-brief.md](../prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-brief.md) | research | TOOL-dLandedOwners-1 TOOL-dLandedOwners-3 |

<!-- /gen:spec-records -->

## 1. Goal

The policy kit's reader scan counts a Python call that passes a policy key by the name of a
module-level string constant, the shape the loop kit uses for seven dDeclaredLoop keys. Once
TOOL-dLandedOwners-1 counts dDeclaredLoop as landed, reader coverage then reports none of those
seven as unread.

## 2. Scope (IN)

- **S1** — A new `READER_SHAPES` row for `.py` files reads the argument run of every call that opens
  on a line. Each argument that is a bare name, or `<keyword>=<name>`, reads as the text of that
  name's module constant in the same file. A module constant is a column-0 line binding one name to
  one quoted string, `KEY = "flow.adapt"`, read by the new `MODULE_CONSTANT` pattern. The row's own
  match never adds its raw text to the spelled set. Observed by AC1 and AC4.
- **S2** — A call nested inside another call's argument list is read on its own, so
  `derive_activated_rows(placed, rows, read_scenario_policy(root, CONFLICT_KEY, rev))` reads
  `CONFLICT_KEY`. Observed by AC1 and AC4.
- **S3** — `read_budget_value` in `tools/loop/budget.py` passes `BUDGET_KEY` and `ROUTE_KEY` by name
  to a call, one call per key, in place of the loop over a tuple of the two. The values it returns,
  the order it reads them in and its refusal text do not change. Observed by AC1 and AC2.
- **S4** — Reader coverage over the real tree, with dDeclaredLoop named as landed, reports none of
  the seven keys §4 "Inventory" lists. Observed by AC3.
- **S5** — Two `RC_CASES` cases: `reader-constant`, which must grade green, and `constant-unread`,
  which must red the planted key. Observed by AC4.
- **S6** — The user page and the kit README state the new reader shape and what it does not see.
  Observed by AC5.

## 3. Non-goals (OUT)

- `derive_landed_owners` and what counts as landed. That is TOOL-dLandedOwners-1, and this unit's
  criteria name the landed set through `check_reader_coverage`'s `landed` argument instead.
- `deviation.approval`, whose only reader sits outside the scanned code. That is
  TOOL-dLandedOwners-3, and this unit leaves that key's finding standing.
- A constant in JavaScript or shell, a constant imported from another module, a function-local
  variable, and a call whose argument list spans lines. No landed owner's key is read in any of
  those shapes at base `51971579`, and the literal row has the same multi-line blind spot.
- The shell-wrapper shape ask TOOL-dPlacedRequest-73 names (`read_card_policy`).
- Any loop kit edit beyond `read_budget_value`, and any other policy key.
- Minting kit versions, which the landing does.

### Edges

none

## 4. Design

### Inventory

The seven keys and the read each makes today, read at base `51971579`:

| Key | Constant | Read |
|---|---|---|
| `flow.adapt` | `tools/loop/adapt.py#KEY` | `policy.resolve(KEY, str(root), "HEAD")`, `tools/loop/adapt.py@b496531b5267:137` |
| `deps.on-parent-withdrawn` | `tools/loop/loop_parents.py#KEY` | `policy.resolve(KEY, str(root))`, `tools/loop/loop_parents.py@13072a1e65c5:165` |
| `transitions.record` | `tools/loop/loop_transition.py#KEY` | `policy.resolve(KEY, str(root), rev)`, `tools/loop/loop_transition.py@8b78cbc05345:234` |
| `flow.on-exhausted` | `tools/loop/budget.py#ENDING_KEY` | `policy.resolve(ENDING_KEY, str(root), "HEAD")`, `tools/loop/budget.py@bfef8c85146d:432` |
| `flow.scenario-default` | `tools/loop/scenario.py#DEFAULT_KEY` | `read_scenario_policy(root, DEFAULT_KEY, "HEAD")`, nested, `tools/loop/scenario.py@842a953a534a:245` |
| `flow.scenario-conflict` | `tools/loop/scenario.py#CONFLICT_KEY` | `read_scenario_policy(root, CONFLICT_KEY, rev)`, nested, `tools/loop/scenario.py@842a953a534a:233` |
| `flow.rework-budget` | `tools/loop/budget.py#BUDGET_KEY` | `for key in (BUDGET_KEY, ROUTE_KEY):` then `policy.resolve(key, ...)`, `tools/loop/budget.py@bfef8c85146d:239` |

The identifiers this unit mints are the pattern `MODULE_CONSTANT` and the two case names
`reader-constant` and `constant-unread`. This repo declares no naming cell for a module pattern or a
fixture case.

### The shape

Today `READER_SHAPES` holds three rows, and group 2 of each is the key text
(`tools/policy/check_policy.py#READER_SHAPES`). Row 1 reads a call whose first argument is a string
literal. Row 2 reads a key joined around a name, which the scan detects by `m.re.groups == 4`
(`tools/policy/check_policy.py#scan_reader_keys`). A name passed to a call matches neither row.

- **`MODULE_CONSTANT`**, beside `READER_SHAPES`: a whole line that opens at column 0 with a name,
  then `=`, then one string literal in either quote, then an optional `#` comment. Group 1 is the
  name and group 3 the literal's text. A starting point, which the builder may tighten:
  `^([A-Za-z_]\w*)[ \t]*=[ \t]*(['"])((?:(?!\2)[^\n\\])*)\2[ \t]*(?:#.*)?$`.
- **The row**, appended to `READER_SHAPES` for `(".py",)`: a zero-width match at every call opening,
  meaning an identifier or dotted name that is not preceded by a word character, `.` or `$` and is
  followed by `(`. Its named group `args` captures the text after `(` up to the first `(`, `)` or end
  of line. The match must be zero-width, so an outer call's match never consumes an inner call's
  name. A starting point: `(?<![\w.$])(?=[A-Za-z_][\w.]*\((?P<args>[^()\n]*))`.

### The scan

`scan_reader_keys` keeps its file population, its skips and its comment rule unchanged. For a `.py`
file it first builds the file's constant map, name to every text `MODULE_CONSTANT` binds it to, over
all of the file's lines. Then, per line that is not a comment:

- a match of a row whose pattern names an `args` group splits that group on `,`. Each piece is
  stripped, and the piece's name is either the whole piece, or the part after `=` in a
  `<keyword>=<name>` piece. Where that name is in the constant map, every text bound to it joins the
  spelled set. The match's own text never joins it.
- every other row keeps today's reading: `m[2]`, with the joined-name splice for row 2.

The row is told apart by `"args" in m.re.groupindex`, never by a group count, because a fourth row
that happened to carry four groups would be read as row 2.

### `read_budget_value`

`tools/loop/budget.py#read_budget_value` resolves `BUDGET_KEY` and then `ROUTE_KEY`, each through a
call whose argument list names the constant on one line, for example a local `read_one(key)` called
as `read_one(BUDGET_KEY)` and then `read_one(ROUTE_KEY)`. The `ValueError` text stays
`"%s does not resolve at HEAD: %s" % (key, e)`, and the return tuple and its errors stay as they
are. This is the loop kit edit the brief's non-goals admit, "beyond what a reader shape needs to
see".

### Measured on the tree

PINNED, measured 2026-11-19 at `9b58eeea`, whose code paths equal base `51971579`'s (`git diff
--stat 51971579 9b58eeea` touches records only):

- `check_reader_coverage` grades 32 dDeclaredLoop keys and finds 8 unread: the seven above and
  `deviation.approval`. dSafePassage's 5 keys are all read, and dFairHearing and dTrueNorth own no
  key.
- Over the 177 tracked `.py` files the scan reads, a probe of S1 and S2 newly credits exactly six
  catalogue keys, every row of the inventory except `flow.rework-budget`, and no other key. All six
  belong to dDeclaredLoop. The probe was a scratch script, not part of this unit.
- `read_budget_value('.')` returns `(4, 2, 3)`.

### Files touched (estimate)

- `tools/policy/check_policy.py`: `MODULE_CONSTANT`, the new `READER_SHAPES` row,
  `scan_reader_keys`, two `RC_CASES` rows, and the module docstring's `reader-coverage` paragraph
  if it names the shapes.
- `tools/loop/budget.py`: `read_budget_value` only.
- `help/policy.md`: the "A reader" and "What it does not see" bullets.
- `tools/policy/README.md`: the call-shapes paragraph and the `arm_reader_coverage` paragraph.

### Alternatives rejected

- **An `ast` walk over each `.py` file**, crediting a `Name` argument of any `Call` bound by a
  module-level `Assign`. Tested by the same probe over the same 177 files: it credits the same six
  keys and no other, and all 177 files parse, so the real tree does not tell the two apart. It loses
  on the seam. `READER_SHAPES` states that "a new shape is one row", and an `ast` pass would be a
  second scan beside the rows, with its own comment rule and skip population. Its one gain, a call
  whose argument list spans lines, is a blind spot the literal row already has.
- **A non-lookahead row**, `[A-Za-z_][\w.]*\(([^()\n]*)` with `finditer`. Tested: it credits four of
  the seven and misses both `scenario.py` keys. The outer `derive_activated_rows(` match consumes the
  inner `read_scenario_policy` name. S2 exists because of this result.
- **A shape for a constant inside a tuple that a `for` loop iterates**, which would read
  `flow.rework-budget` with no edit to the loop kit. Rejected for three reasons. It is a second
  shape for one instance: the probe found no other read of that form. Admitting a bare name inside
  any parentheses would also credit a `"%s" % (KEY, value)` message tuple, and `help/policy.md`
  already lists "a call that only mentions the key" as a false pass. And the recorded precedent
  takes the other route: TOOL-dScopedBuild-25 §10 "moves the read to the shape rather than adding a
  row". The brief's non-goal admits a loop kit edit of exactly this size.

## 5. Production-readiness checklist

- security: N/A. The scan reads tracked files it already reads and writes nothing, and no new input
  reaches it.
- perf / scale: one extra pass of `MODULE_CONSTANT` over each `.py` file's lines, already in memory,
  plus one zero-width match per call opening. The file count is unchanged.
- error / empty / loading states: a file with no module constant credits nothing from the row. A
  file that does not decode is read with `errors="replace"`, as it is today.
- observability: unchanged. The summary line and one finding per unread key stay as
  `check_reader_coverage` prints them.
- risks: a false pass where a module constant holding a key is passed to a call that is not a reader,
  `print(KEY)` say. That is the same class row 1 accepts for a literal, and it is stated on the user
  page. A column-0 `NAME = "text"` line inside a triple-quoted string binds too, which can credit a
  key only where a call also passes that name.
- testing: AC4's two fixture cases, and AC1 to AC3's probes over the real tree.
- migration: N/A. No stored data or config changes shape.
- user docs: `help/policy.md`'s reader-coverage section, S6 and AC5.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; s = c.scan_reader_keys('.'); print(sorted(k for k in s if k.split('.')[0] in ('flow', 'deps', 'transitions')))"`
  runs at this unit's tip, the list it prints holds all seven keys of §4 "Inventory".
  Red when: the row is absent, the scan dispatches it as a literal row, its match consumes an outer
  call so `flow.scenario-default` and `flow.scenario-conflict` drop out, or `read_budget_value`
  still reads through the tuple loop so `flow.rework-budget` drops out.
- **AC2** — When `python -c "import sys; sys.path.insert(0, 'tools/loop'); import budget; print(budget.read_budget_value('.'))"`
  runs at this unit's tip, it prints the tuple that the base's `read_budget_value` printed in the
  same tree, `(4, 2, 3)`.
  Red when: the respelled reads swap their order, drop a key or change the parse of either value.
  figure: PINNED, measured 2026-11-19 at `9b58eeea`. If `.governance/policy.toml` has moved
  `flow.rework-budget` or `flow.route-backs` since, the figure re-derives from
  `python tools/policy/policy.py get` of the two keys.
- **AC3** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; n, f = c.check_reader_coverage('.', landed={'dDeclaredLoop'}); print(n); print(*f, sep='\n')"`
  runs at this unit's tip, no finding line names any of the seven keys of §4 "Inventory". The only
  finding line left names `deviation.approval`, or there is none once TOOL-dLandedOwners-3 has
  landed.
  Red when: a key of the inventory is still reported as having no reader.
  figure: the graded count printed first is DERIVED, the catalogue's dDeclaredLoop rows by
  `policy.load_catalogue`, and was 32 at `9b58eeea`.
- **AC4** — When `python tools/policy/check_policy.py --fixture reader-coverage` runs, it prints a
  `case reader-constant: green` line and a `case constant-unread: red` line, and no line of the case
  carries `WRONG:`. `reader-constant` plants `consumer.py` holding `KEY = "fixture.planted"` at
  column 0 and a nested call passing it, `value = read(root, resolve(root, KEY))`, and grades 1 key
  with no finding. `constant-unread` plants three files and must red `fixture.planted`: a
  `consumer.py` binding `KEY` at column 0 and naming it only in a message tuple,
  `print("%s" % (KEY,))`; an `other.py` holding `resolve(KEY)` and no binding; and a `local.py`
  binding `key = "fixture.planted"` inside a function and passing it.
  Red when: the row is deleted from `READER_SHAPES`, which makes `reader-constant` print `WRONG:`,
  or the constant map reads a binding at any indent or from another file, which makes
  `constant-unread` print `WRONG:`.
- **AC5** — When `grep -n "resolve(KEY)" help/policy.md tools/policy/README.md` runs, each file prints
  a line stating the module-constant shape. When
  `grep -c "a key passed through a variable reads as unread" tools/policy/README.md` runs, it prints
  `0`.
  Red when: either page still describes only the literal and CLI shapes, or the README still says
  every key passed through a variable is unread.

## 7. Gates

`policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `loop budget fixtures`

The close runs these with the merge bar. This build's brief waives the policy kit's flagged bar,
and the main loop decides at the close what that waiver reaches.

New arm: tools/policy/check_policy.py RC_CASES reader-constant and constant-unread · covers AC4 · the new READER_SHAPES row deleted reds reader-constant, and MODULE_CONSTANT unanchored from column 0 reds constant-unread · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-19 · initial draft.

## 10. Reuse audit

The seam this unit extends is the reader scan, `tools/policy/check_policy.py#READER_SHAPES` and
`tools/policy/check_policy.py#scan_reader_keys`, one row added under the rule its comment states, "a
new shape is one row". `tools/codebase-map/reuse_lookup.py` returned no seam for the behaviour.
Its candidates were name-stem matches on `read`, `key` and `scan`, such as `read_text`,
`read_policy_value` and `read_policy_kit`, and none of them reads a key out of source text. The seam
came from recall instead: TOOL-dGroundRules-8, the arm's own spec, and TOOL-dScopedBuild-25, the
precedent of moving a read to the shape rather than adding a row. The second precedent decided the
`read_budget_value` respell. The candidates tested and rejected, with the test that rejected each,
are under §4 "Alternatives rejected". Recall also returned TOOL-dPlacedRequest-73, an open ask for a
different shape, which §3 leaves out.

Recall terms used: `python tools/codebase-map/reuse_lookup.py "scan code for a policy key passed to a reader call through a module-level string constant"`
and `python tools/memory-recall/query.py "how does reader coverage find a key read through a constant rather than a literal" --terms "reader coverage READER_SHAPES scan_reader_keys module constant key literal catalogue landed owner shape"`.
