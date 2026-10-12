# TOOL-aOrientedCast-12 — a budget row is four fields, and an argv column that reads as prose is refused

**Status:** INPROGRESS · rev-1 · 2026-10-12 · node a · Tier-1 · base 646d4a73 · streams tooling · order 12 · ratified 2026-10-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-aOrientedCast-12-1-spec-brief.md](../prompts/2026-10-12-prompt-TOOL-aOrientedCast-12-1-spec-brief.md) | journal | TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes review items H1 and M1 of
[the closing review, round 1](../reviews/2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md).
Row 94 of `tools/run-gates/selftest-budgets.txt` lacks its empty argv column, so its reading prose
runs as the `roles render selftest` command; this unit restores the column and makes the
declaration's one reader refuse that class of row, so the next missing tab reds `--check`.

## 2. Scope (IN)

- **S1** — Row 94 of `tools/run-gates/selftest-budgets.txt`, `roles render selftest`, gains its empty
  argv column: `roles render selftest<TAB>60<TAB><TAB>measured 1.3s …`, matching row 93 and every
  sibling. Observed by AC1.
- **S2** — `read_population` in `tools/run-gates/run-selftests.sh` (its embedded Python program,
  lines 528-584) emits the state `BADROW` for a data row whose tab-split field count is not four,
  ahead of the budget test. The header comment at `selftest-budgets.txt:49` names those four
  columns. A one-field row, which the reader skips without a word today, reads `BADROW` too.
  Observed by AC2.
- **S3** — `read_population` emits the state `BADARGV` for a row whose own argv column is non-empty
  and whose first word neither begins the argv of any leg in the manifest the reader already loads
  nor carries a slash. The launcher set is DERIVED from the manifest's `argv[0]` values, so no
  launcher list is typed. A row whose argv comes from the manifest is not graded by it. Observed by
  AC2.
- **S4** — `--check` refuses each new state by name, beside its existing `UNRESOLVED` and
  `BADBUDGET` branches (`run-selftests.sh:788-795`). The run loops already refuse any non-`ok` state,
  at `:1362`, `:1835` and `:1967`, so they need no edit. Observed by AC3.

## 3. Non-goals (OUT)

- No second parser of the declaration. `--rank` (`run-selftests.sh:417`) reads the reading column on
  its own and reports a three-field row as unbacked, which is loud; it is left as it is.
- No change to the budget figures, to any other row, or to `tools/gate-legs.json`.
- No kit-version bump for run-gates; each touched kit moves once at the close.

## 4. Design

The seam is the one reader every mode shares. `read_population` is called for the run, pooled and
`--list` modes at `:757` and for `--attribute` at a second commit at `:1821`, so a state emitted
there reaches every consumer. That is how `BADBUDGET` was added by `TOOL-aQuenchedHarness-7`, and
this unit follows its shape exactly.

In the Python loop, after the comment and blank-line skips:

1. Split the line on tabs. If the count is not 4, print `BADROW`, the name, the budget field as
   written (or empty), and an empty argv, then continue. This replaces the `len(f) < 2` skip.
2. The existing `BADBUDGET` test follows unchanged.
3. If the row's own argv is non-empty, take its first word. If that word is not in
   `{leg["argv"][0] for leg in legs if leg.get("argv")}` and carries no `/` or `\`, print
   `BADARGV`, the name, the budget and the argv, then continue.
4. The manifest fallback and the `{prefix}` resolution follow unchanged.

In `--check`'s reverse loop, two branches beside the existing two:

- `BADROW`: `run-selftests: row '<name>' does not carry the four tab-separated fields the
  declaration's header names (name, budget, argv, reading), so its reading can run as its argv`.
- `BADARGV`: `run-selftests: row '<name>' declares the argv '<argv>', whose first word is no
  launcher a manifest leg uses and names no path, so it reads as prose rather than a command`.

Each sets `fails=1` and continues, as the two existing branches do.

The predicate was run over the real tree before it was specced. The field count hits one row, row 94,
and no other: 93 rows carry four fields. The launcher test, run over every row with a non-empty argv
from either source, hits one row, row 94, and its near-misses are the 27 row-declared argvs, all of
which begin `bash` and name a `{prefix}` path. Both counts are PINNED, measured on node a
2026-10-12. The manifest's launchers measured then are `bash`, `python3`, `python` and `node`, a set
the predicate re-derives on every run.

The probe a pass runs, since the role gate refuses a builder the self-test runner itself. Run
against the base reader on 2026-10-12 it printed `ok` for a three-field prose row, which is the RED
this unit turns:

```bash
PYBIN=python TROOT=tools bash -c 'eval "$(sed -n "/^read_population() {/,/^}/p" tools/run-gates/run-selftests.sh)"; read_population "$1" tools/gate-legs.json ""' _ <scratch budgets file>
```

### Files touched (estimate)

`tools/run-gates/selftest-budgets.txt`
`tools/run-gates/run-selftests.sh`
`tools/run-gates/run-selftests.test.sh`
`memory/guides/SESSION-KICKOFF.md`

`run-selftests.sh` is in the kickoff manifest's `watch:` list, so this unit re-stamps the
manifest's `last-audit` with a delta line in its commit message. It mints no function.

## 5. Acceptance criteria

- **AC1** — When `awk -F'\t' '!/^[[:space:]]*#/ && NF && NF != 4' tools/run-gates/selftest-budgets.txt`
  runs, it prints nothing, and `grep -c '^roles render selftest' tools/run-gates/selftest-budgets.txt`
  prints 1.
  Red when: row 94 keeps three fields, or the fix drops the row.
- **AC2** — When the §4 probe runs `read_population` over a scratch budgets file holding a three-field
  row, a four-field row whose argv column is `measured 1s`, and the row `agent-cap self-test<TAB>590<TAB><TAB>r`,
  it prints `BADROW` for the first, `BADARGV` for the second and `ok` with the manifest's argv for
  the third; over the real `tools/run-gates/selftest-budgets.txt` it prints `ok` on every line.
  Red when: a three-field row or a prose argv reads `ok`, or a real row reads anything else.
  fixture: the scratch file is written by the pass and deleted after it.
- **AC3** — When the `run-selftests self-test` leg's new arms run, a declaration with a three-field
  row and one with a prose argv each red `--check` naming the row, and the serial run refuses the
  three-field row as `BADROW`.
  Red when: `--check` passes either row, or the run loop runs the prose.
  permission: this run's builder may not execute the self-test runner or its suite; the main loop
  observes the arms at the close.

## 6. Gates

`every held leg is budgeted, every budget row resolves` · `run-selftests self-test` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-selftests.test.sh · covers AC3 · a row appended with one tab short, and a four-field row whose argv is `measured 1s`, each against a reader with the field-count or launcher test staged out · none
New arm: tools/run-gates/run-selftests.test.sh · covers AC3 · the serial run over a three-field row, against a reader whose field-count test is staged out, which runs the prose and exits 127 · none

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 7. Open questions

- **F1 — Does the status header carry `closes H1 M1`, as the spec brief asks?**
  `backlog.read_header_verbs` expands a `closes` value through the generator's id grammar, and
  `H1` is no id: a probe of `_read_backlog_verbs` on such a header raised "H1 M1 is not an id or an
  id range", which refuses every render of the build index. The build keeps no `BACKLOG.md`, so no
  ask id exists to name instead, and filing one is outside a spec pass.
  Options: (a) write the verb and red the index; (b) name the review items in §1 and leave the verb
  out.
  RESOLVED (agent, 2026-10-12, delegated): (b). Option (a) fails the build-index leg, M3 veto 1.

## 8. Revision log

- rev-1 · 2026-10-12 · initial draft.

## 9. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a malformed self-test budget row"` ranked
name-token neighbours, `rows`, `row` and `extract_row`, none of which reads this declaration. The
seam extended is `read_population` in `tools/run-gates/run-selftests.sh`, found by reading it, and
its `--check` branches; the precedent is `TOOL-aQuenchedHarness-7`'s `BADBUDGET`, which the recall
probe surfaced from that build's closing review.

Recall terms used: `selftest budgets row argv column read_population BADBUDGET UNRESOLVED check reverse declared population`
