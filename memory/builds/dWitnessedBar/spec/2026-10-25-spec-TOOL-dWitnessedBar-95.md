# TOOL-dWitnessedBar-95 — unit 92 AC5 reads the write grant through the shipped parser and containment test, so a declared ancestor of the spec directory reds

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 49 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 91 and 92
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-91-spec-audit-round1.md`)
confirmed finding **id 8 at HIGH**, report item **H3**. No other id shares the item.

`TOOL-dWitnessedBar-92` AC5 checks that no pass of unit 92 declares the spec directory by grepping
its dispatch rows for the literal ` memory/builds/dWitnessedBar/spec/?( |$)` (spec-92 lines 422-423).
`--check-commit` admits a staged path through `covers` (`tools/unattended/unattended.sh:13555`), and
`covers` admits every path under a declared directory (`tools/unattended/lib-unattended.sh:745-749`).
A declaration of `memory`, `memory/` or `memory/builds/dWitnessedBar/` therefore grants writes under
`spec/` while AC5's count prints 0.

This unit replaces AC5's dispatch half with a check that reads the declarations through
`read_pass_declarations` and asks `covers` of each declared path. It repairs
`TOOL-dWitnessedBar-92` and builds one step after it (order 49).

## 2. Scope (IN)

- **S1** — id 8. The grant check. The two `grep` clauses that open 92 AC5, from
  `grep -E ' dispatch · item [0-9a-f]+ TOOL-dWitnessedBar-92 '` through its piped
  `grep -cE ' memory/builds/dWitnessedBar/spec/?( |$)'` printing 0, give way to §4's grant check.
  It reads every dispatch key of `TOOL-dWitnessedBar-92` that `read_pass_declarations` prints, so
  each pass of the unit is read and not only its last. It names each declared path that `covers` a
  path under `memory/builds/dWitnessedBar/spec/`, or that `is_repo_root` names. It reds when the unit
  has no dispatch row, so an empty read cannot pass. The rest of 92 AC5 stands. Observed by AC1, AC2
  and AC3.
- **S2** — id 8. The red case 92 AC5 lacks. In a scratch copy of `memory/builds/dWitnessedBar/RUN.md`
  carrying a dispatch row of unit 92 that declares `memory/builds/dWitnessedBar/`, the grant check
  prints `GRANTS SPEC memory/builds/dWitnessedBar/` and exits 1, where 92 AC5's literal count prints 0.
  Observed by AC2.
- **S3** — Unit 92 answered. Unit 92's acceptance ledger records the grant check's last line on the
  built tree as a note under its `- AC5` answer. The note is a continuation line, two spaces in,
  opening with the label `TOOL-dWitnessedBar-95 S3` and carrying the backticked `WIDE 0` and the word
  `covers` on that one physical line. Observed by AC4.

## 3. Non-goals (OUT)

- Rewording the spec text of unit 92. Its AC5 dispatch clauses are superseded by name here and
  answered in its ledger, as `TOOL-dWitnessedBar-92` §3 does for unit 90.
- AC5's pass-commit half, which reads the commits of units 89 and 90. `TOOL-dWitnessedBar-97` takes
  ids 9 and 10, which land there.
- The dispatch rows of units 89 and 90. 92 S5 answers them through their pass commits, after the
  fact.
- The report's left-shift text, a spec-lint rule refusing a criterion that greps `--writes` paths. No
  clause of this build names it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-92` — AC5's dispatch half, its literal spec-directory count, which S1 replaces with the grant check, and S5's withdrawn declaration, which the grant check grades (id 8)

## 4. Design

### Evidence

- `tools/unattended/unattended.sh:13538` walks each unit of the `Pass:` trailer, and `:13555` admits a
  staged path when `covers "$q" "$p"` holds for some declared `q`. `:13565` and `:13577` refuse the
  rest with `stages paths outside the set it declared before dispatch`.
- `covers` (`tools/unattended/lib-unattended.sh:745-749`) returns 0 when the second path is the first
  or sits under it, after `normpath`. `is_repo_root` (`:754-758`) names `""`, `.` and `./`, which
  `covers` does not, and `--dispatch` refuses them (`tools/unattended/unattended.sh:13807`).
- `read_pass_declarations` (`tools/unattended/lib-unattended.sh:1116`) prints one line per dispatch
  key in the raw row's shape, `<utc> dispatch · item <anchor> <unit> · reason <paths>`. Without its
  `current` argument it prints every key, so a unit with several passes prints one line per pass.
- Probed on 2026-10-25 with `lib-unattended.sh` sourced: `covers` returned 0 against
  `memory/builds/dWitnessedBar/spec/x` for `memory`, `memory/`, `memory/builds/dWitnessedBar/`,
  `memory/builds/dWitnessedBar/spec` and `memory/builds/dWitnessedBar/spec/`, and 1 for
  `memory/builds/dWitnessedBar/build/`. `is_repo_root` returned 0 for `.`, `./` and `""`.
- §4's grant check was probed on 2026-10-25 over scratch copies of `memory/builds/dWitnessedBar/RUN.md`,
  each with one dispatch row of unit 92 appended. A row declaring
  `memory/builds/dWitnessedBar/build/` printed `ROWS 1 WIDE 0`, exit 0. Rows declaring
  `memory/builds/dWitnessedBar/` and `memory` each printed their `GRANTS SPEC` line and
  `ROWS 1 WIDE 1`, exit 1, where 92 AC5's literal count printed 0. Over the live file, which holds no
  dispatch row, it printed `ROWS 0 WIDE 0`, exit 1.

### The grant check

Run as a script with `bash` from the repository root, `SCRATCH` set to the run's scratch directory.
`RUNSTATE` names the run-state file and defaults to the build's. It prints a `GRANTS SPEC <path>` line
for each declared path that grants a write under `spec/`, then `ROWS <n> WIDE <m>`. It exits 0 only
when unit 92 has at least one dispatch row and no declared path grants that write.

```bash
. tools/unattended/lib-unattended.sh
r=${RUNSTATE:-memory/builds/dWitnessedBar/RUN.md}
read_pass_declarations "$r" > "$SCRATCH/rows"
rows=0; wide=0
while IFS= read -r row; do
  k=${row#* dispatch · item }; k=${k%% · reason *}
  [ "${k#* }" = TOOL-dWitnessedBar-92 ] || continue
  rows=$((rows+1))
  for q in ${row#* · reason }; do
    if is_repo_root "$q" || covers "$q" memory/builds/dWitnessedBar/spec/x; then
      echo "GRANTS SPEC $q"; wide=$((wide+1))
    fi
  done
done < "$SCRATCH/rows"
echo "ROWS $rows WIDE $wide"
[ "$rows" -ge 1 ] && [ "$wide" = 0 ]
```

The declared paths are split unquoted, as `--check-commit` splits them at `:13555`. `--dispatch`
refuses a declared path carrying a glob character, so the split expands nothing.

### Inventory

Minted: the grant check's `GRANTS SPEC <path>` and `ROWS <n> WIDE <m>` lines; the ledger note
labelled `TOOL-dWitnessedBar-95 S3`. No function, constant, plant, flag or file in the product.
Naming cells: none apply.

### Migration

None: no stored data changes.

### Rollout

After unit 92's pass commit, where 92 AC5's dispatch half ran. The unit takes order 49, one above
unit 92's 48, beside units 93, 94 and 96. The scratch-copy red runs at the close, and the note is
written then.

### Files touched (estimate)

- `memory/builds/dWitnessedBar/build/`

### Alternatives rejected

- **Widen the literal to the spec directory and each of its ancestors.** It spells the containment
  rule a second time beside `covers`, so a change to `normpath` moves one and not the other.
- **`read_pass_declarations ... current`, the report's spelling.** It keeps only the unit's last key,
  so a first pass that declared an ancestor and a second that did not would pass.

## 5. Production-readiness checklist

- security — the check reads a write grant through the same containment test that admits the write,
  so it cannot certify a grant `--check-commit` would honour as narrow.
- perf / scale — one awk pass over the run-state file and one `covers` per declared path.
- error / empty / loading states — no dispatch row for unit 92 prints `ROWS 0` and reds.
- observability — each granting path is printed by name.
- risks — a declaration that grants `spec/` and is never used still reds, which is the intended
  reading of 92 S5's withdrawal.
- testing — AC1 after the pass commit; AC2 and AC3 by scratch copy at the close; AC4 by ledger.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — After unit 92's pass commit, §4's grant check, run with `SCRATCH` set, prints a last line
  `ROWS <n> WIDE 0` with `n` at least 1 and exits 0.
  Red when: a pass of unit 92 declares the spec directory or an ancestor of it.
  figure: `n` is DERIVED at observation time from the dispatch rows of unit 92.
- **AC2** — In a scratch copy of `memory/builds/dWitnessedBar/RUN.md` with the row
  `<utc> dispatch · item <sha8> TOOL-dWitnessedBar-92 · reason memory/builds/dWitnessedBar/` appended,
  the grant check run with `RUNSTATE` naming the copy prints `GRANTS SPEC memory/builds/dWitnessedBar/`
  and `ROWS 1 WIDE 1` and exits 1. Over the same copy,
  `grep -E ' dispatch · item [0-9a-f]+ TOOL-dWitnessedBar-92 '` piped to
  `grep -cE ' memory/builds/dWitnessedBar/spec/?( |$)'` prints 0. The same holds with `memory` in
  place of the build directory.
  Red when: a declared ancestor of the spec directory passes the grant check.
  fixture: a scratch copy under the run's scratch directory; the live file holds no row of unit 92
  before its dispatch.
- **AC3** — In a scratch copy of `memory/builds/dWitnessedBar/RUN.md` with no dispatch row of unit 92,
  the grant check prints `ROWS 0 WIDE 0` and exits 1.
  Red when: an empty read of the dispatch rows passes as a narrow grant.
  fixture: a scratch copy under the run's scratch directory.
- **AC4** — When 92 §4's note check is fed `95|S3|92|AC5|WIDE 0` and `95|S3|92|AC5|covers`, it prints
  `NOTES OK 2`.
  Red when: unit 92 AC5 is recorded against the literal spec-directory count.
  permission: the ledger is written at the close.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

`recall floor` and `recall floor arms` are owed for the ledgers under `memory/`. AC2 and AC3 run by
scratch copy at the close. This unit adds no arm and moves none, so it declares no `New arm:` line,
and `TOOL-dWitnessedBar-88` S6's derivation still names unit 90 the floor's owner.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 92 is itself
  derived and carries no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-90` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Which dispatch keys does the grant check read?** Options: (a) the unit's last key, through
  `read_pass_declarations ... current`, as the report spells it; (b) every key of the unit. (a) misses
  an earlier pass's grant. (b) reads every pass and costs nothing more. RESOLVED (agent, 2026-10-25,
  delegated): (b), rung 3, the most feature-rich survivor.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 91 and 92, id 8
  (HIGH, item H3).

## 10. Reuse audit

The seams are `read_pass_declarations` (`tools/unattended/lib-unattended.sh:1116`), the shipped
parser of dispatch rows, and `covers` (`:745`) with `is_repo_root` (`:754`), the containment test
`--check-commit` admits a write through. The grant check calls them and spells neither again.
`python tools/codebase-map/reuse_lookup.py "which declared write paths cover a directory a pass may not write"`
ranked `write`, `note`, `write_text` and `declares`, none a reader of dispatch declarations, so the
two library seams named above are the ones extended.

Recall terms used: `python tools/memory-recall/query.py "how does a check tell a declared write grant that covers a directory through an ancestor" --terms "dispatch writes declaration covers ancestor directory read_pass_declarations grant spec directory check-commit narrow"`
