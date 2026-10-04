# TOOL-aMendedFleet-92 — check 23 prints a fleet line, and drift-audit reads it from the newest bar run

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 92

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Unit 62 split this unit off node d's dUnstuckLanding unit 17: check 23's range mode, a per-build
budget key in place of the shared ceiling key, the retired measuring flag, a fleet line and a drift
signal reading it. Re-verified against base, most of that half is already on main by another route.
The aWindowedPass build's units 1 and 5 made check 23 count only an undeclared write whose pass
overlapped a sibling, fail only the run the checked-out branch drives, print every other run's
counted writes as a `check 23 OTHER RUN` line, list the old ceiling key in `RETIRED_CONF_KEYS`, and
make `--emit-ceiling` exit 2. A run's landed history no longer reds another run's close, which was
the report's point `[B#14]`. What main lacks is the fleet half: no single line totals the counted
writes, so nothing outside a checkout on a run's own branch ever sees a run whose writes no leg
fails. This unit prints that line under main's rules and applies node d's drift signal, which reads
it from the newest bar run, as node d's bytes wherever they still describe main.

## 2. Scope (IN)

- **S1** — THE FLEET LINE. Check 23 in `tools/unattended/check-unattended.sh` accumulates, across the
  records it grades, the counted undeclared writes, the graded passes, the graded records and one
  `<slug>=<n>` pair per record holding a counted write. After its record loop, whenever at least one
  record reached grading, it prints on the default channel:
  `unattended: check 23 fleet — <n> undeclared write(s) over <g> graded pass(es) in <r> record(s) · budget 0 per run · over <slug>=<n>…|none · at <head8>`.
  The head and the first field are node d's words, so node d's parser reads the line unchanged.
  The line never fails the leg and never changes an existing verdict. A record check 23 skips or
  excludes before grading contributes nothing. Observed by AC2 and AC3.
- **S2** — THE HEADER CONTRACT. Exception TWO in the header of `tools/unattended/check-unattended.sh`
  names the fleet line beside `check 23 SOLO` and `check 23 OTHER RUN`, so the "exit 0 and no output"
  contract still describes the code. Observed by AC4.
- **S3** — THE DRIFT SIGNAL. `_FLEET_HEAD`, `_parse_fleet_line` and `measure_fleet_over_budget` in
  `tools/drift-audit/drift_report.py`, applied from node d's commit `d99cd0328` byte for byte except
  the comment lines that spell the fleet line's fields, which spell main's line; the function is
  appended to `SIGNALS` after `measure_legs_retried_after_timeout`. It is REPORT-ONLY, reads NOT
  ASKED without `.unattended.conf`, and reads DEAD PROBE where no run record under the git dir's
  `gate-run` directory carries a fleet line. Observed by AC5 and AC6.
- **S4** — THE README ROW. One row for `fleet_over_budget` in the signal table of
  `tools/drift-audit/README.md`, in node d's position and shape, its question reworded for main:
  which live runs hold undeclared writes counted against check 23's per-run zero, read from the
  fleet line of the newest bar run. Observed by AC7.
- **S5** — THE DRIFT SELF-TEST ARM. Node d's `test_fleet_over_budget` and `_write_fleet_out` in
  `tools/drift-audit/selftest.py`, byte for byte, with `CHECK_FLOOR` raised by the arm's nine checks
  and a comment line saying the rise was counted off the arm, not measured. NOT OBSERVED by a
  criterion here: the suite runs once at the close, and the arm is declared under `New arm:` in §7.
- **S6** — THE KIT-GATE ARMS. One arm in `tools/unattended/check-unattended.test.sh` asserting the
  fleet line for a fixture with a counted write and for one with none; every existing arm that
  asserts check 23's default-channel output byte for byte is updated for the new line in the same
  pass. NOT OBSERVED by a criterion here: the suite runs once at the close, and AC2 and AC3 observe
  the behaviour through a slice.

## 3. Non-goals (OUT)

- A budget key. Main grades the run a checkout drives against zero by design (aWindowedPass unit 5),
  and a declared budget would reopen that ruling. The fleet line spells the zero as data.
- Range mode for check 23. A derived-LANDED record is already excluded through
  `check_derived_landed`, and the run a checkout drives lands once at its close, so no pushed pass of
  a graded run remains for a range to skip. Re-verify before building: if node d's later units land
  first, a hand-off can leave pushed passes in a live record, and that is their mechanism.
- Changing how `--emit-ceiling` or a conf still setting the ceiling key behave. Both are main's
  already, and AC1 observes them.
- Making the fleet total bind anywhere. It is printed and read, never a refusal.
- The `range` field of node d's line. Main has no range mode to name, and node d's parser ignores
  the field.
- The drift-audit and unattended kit version moves, owed once at the close after the build's last
  move of each kit.

### Edges

- **consumes-from** external — main's per-run check 23 from the aWindowedPass build, which this unit
  totals and does not change.
- **hands-off** external — the reconcile with node d's dUnstuckLanding unit 17, which meets one
  `SIGNALS` line, the `CHECK_FLOOR` line and the comment lines S3 names as differing hunks.

## 4. Design

### Evidence

Read at the worktree HEAD `8312d315`, whose bytes under `tools/` equal base `7af5f564`'s. Node d's
branch `origin/branch/unattended-build-closing-f90fd9` was read at `a96ae2dfa`.

- Main's check 23 already holds the per-run verdict: `DS_HEAD_REF` binds the run the checkout drives,
  `fail 23` fires only for it, and `check 23 OTHER RUN` and `check 23 UNBOUND` print for the rest.
  `RETIRED_CONF_KEYS` names the old ceiling key, and the `--emit-ceiling` argv branch exits 2. Both
  arrived with aWindowedPass commits `c5582706e` and `7ab7ae535`, which node d's branch lacks.
- Three-way merges with `git merge-file`, base `d99cd0328^`, ours HEAD, theirs `d99cd0328`, written
  to the scratchpad: `tools/unattended/check-unattended.sh` 7 conflicts, its suite 11,
  `.unattended.conf`, the example conf, both protocol copies and the cross-component suite 1 each;
  `tools/drift-audit/drift_report.py` 1, the `SIGNALS` list only; `tools/drift-audit/selftest.py` 1,
  the `CHECK_FLOOR` block only; `tools/drift-audit/README.md` 0. So node d's drift half applies as
  its bytes, and its check 23 half is a rewrite of code main has also rewritten.
- Node d's `_parse_fleet_line` anchors on the head, requires the first field's exact words, and reads
  only the `over` and `at` fields by their leading word. A line with no `budget` or `range` field
  parses, which is why S1 may drop the range field and keep the reader byte for byte.
- `gate-run/<id>/<i>.out` holds each leg's stdout, redacted, under the header line
  `# run-gates | leg <name> | exit <rc>`, written by `tools/run-gates/run-gates.sh`; node d's reader
  scans every `.out` of the newest record holding a fleet line, so it needs no leg name.
- Live run records with dispatch rows exist on this tree: `aClosedDocket` at BUILDING with one row,
  and several LANDING records. So the line has a population to print over here.
- Node d's README row names `UNDECLARED_WRITE_BUDGET`, which main does not declare; S4 rewords it.

### Data model

The one contract between the two kits, illustrative values:

```
unattended: check 23 fleet — 2 undeclared write(s) over 11 graded pass(es) in 3 record(s) · budget 0 per run · over aClosedDocket=2 · at 8312d315
```

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `measure_fleet_over_budget` | python function | `py.function`; `python tools/lexicon/lexicon.py --suggest measure_fleet_over_budget --as py.function` answered OK |
| `_parse_fleet_line` | python function | `py.function`; the lexicon answered OK |
| `_FLEET_HEAD` | python constant | not graded |
| `fleet_over_budget` | drift signal name | none |
| `check 23 fleet` | default-channel message head | none |

The shell accumulators beside `ds_over_n` take the `ds_fleet_` prefix node d used; shell globals are
not graded.

### Rollout

1. Write S1 and S2, then S6's arm, and observe AC2 to AC4 through the slice.
2. Apply S3 to S5 from node d's commit with `git show d99cd0328 -- <file>` hunks, resolving the
   `SIGNALS` and `CHECK_FLOOR` conflicts to main's lists plus this unit's entries, then rewrite the
   comment lines S3 names. Observe AC5 to AC7.
3. Commit once with the unit id in the subject and a `Decided:` trailer naming the reuse and the
   comment lines that differ.

### Files touched (estimate)

- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`

### Alternatives rejected

- **Apply node d's check 23 half as its bytes.** Seven conflicts against code main rewrote; resolving
  them either restores the ceiling's successor as a budget key, reversing aWindowedPass unit 5, or is
  a hand rewrite that matches node d nowhere.
- **A drift signal parsing the `OTHER RUN` and `UNBOUND` lines.** On a clean tree check 23 prints
  neither, so the signal could not tell a fleet with no counted write from a leg that never graded
  one. The fleet line prints whenever a record was graded, which is the liveness the signal needs.
- **The drift signal re-runs check 23.** Node d measured the kit gate at 623.656 s against a report
  measured in seconds.

## 5. Production-readiness checklist

- security — N/A — one printed line from counts check 23 already holds, and a reader of a file the
  gate runner already writes under the git dir.
- perf / scale — a few integer additions in check 23's loop; the signal reads the run records under
  one git dir, newest first, and stops at the first fleet line.
- error / empty / loading states — no graded record prints no line, and the signal then reads DEAD
  PROBE rather than 0; a line that does not parse is detail, never a count.
- observability — the line itself, plus the signal's detail naming the record it read and whether
  HEAD moved past it.
- risks — existing kit-gate arms asserting exact output on a fixture with dispatch rows change; S6
  updates them in the same pass. The signal reports a past bar, and says so.
- testing — AC1 to AC7 directly; the arms in S5 and S6.
- migration — none: no conf key, no stored record.
- user docs — S4; the kit README names no check 23 output line today.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh --emit-ceiling` runs, it exits 2 within a
  second naming the retirement, and `grep -n '^RETIRED_CONF_KEYS=' tools/unattended/check-unattended.sh`
  prints the line naming the old ceiling key. These observe the half main already carries.
  Red when: a rebuild here reintroduces the ceiling key's check or the measuring flag's output.
- **AC2** — When a scratch slice of the kit-gate suite, its prologue plus the check 23 per-run arms
  and the new fleet arm, runs a fixture whose live record has one counted undeclared write, the
  output carries exactly one line opening `unattended: check 23 fleet — 1 undeclared write(s)` whose
  `over` field names that record's slug with `=1`, and the arms that passed before still pass.
  Red when: the fleet line's `printf` is staged out, and the new arm reds.
  cost: minutes for the slice; the suite whole is never run.
  fixture: the suite's own check 23 fixture builder, which the tree holds today.
- **AC3** — When the same slice runs a fixture whose live record has dispatch rows and no counted
  write, the fleet line reads `0 undeclared write(s)` and `over none`; when the only record is
  derived LANDED, no fleet line prints.
  Red when: an excluded record is counted, or a graded clean record prints no line.
- **AC4** — When `sed -n 1,40p tools/unattended/check-unattended.sh` is grepped for `check 23 fleet`,
  it hits exception TWO.
  Red when: the header contract still omits a default-channel line the code prints.
- **AC5** — When `python tools/drift-audit/drift_report.py --json` runs in a `git clone --local` of
  the unit's tip under a short `%TEMP%` root whose git dir holds no run record, `fleet_over_budget`
  reads `live` false; after a file `0.out` under a `gate-run` subdirectory of that clone's git dir
  is written carrying S1's line shape, with no `range` field and `over aFixture=2`, it reads value 1,
  `gateable` false and a detail naming `aFixture`; deleting the file returns it to `live` false.
  Red when: the reader needs a field main's line lacks, so a well-formed main line reads DEAD, or a
  deleted record reads a live 0.
  cost: about 30 s per report run.
  fixture: under `%TEMP%`, never the scratchpad, whose long path fails a clone.
- **AC6** — When the text of `measure_fleet_over_budget`, `_parse_fleet_line` and the `_FLEET_HEAD`
  line is cut from the drift engine's blob at node d's `d99cd0328`, read with `git show`, and from
  the unit commit's blob, and the two are compared with `diff`, they differ only on the comment lines
  that spell the
  fleet line's fields, and `grep -c "check 23 fleet — "` over `tools/unattended/check-unattended.sh`
  and over `tools/drift-audit/drift_report.py` prints at least 1 for each.
  Red when: a reader line was retyped, or the two kits spell the head differently.
- **AC7** — When `grep -n fleet_over_budget tools/drift-audit/README.md` runs it prints one table row,
  and `grep -c UNDECLARED_WRITE_BUDGET tools/drift-audit/README.md` prints 0.
  Red when: the signal ships undocumented, or its row names a key main does not declare.

## 7. Gates

`unattended kit gate` · `drift-audit records` · `drift-audit wiring` · `drift-audit selftest` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/check-unattended.test.sh` · a live record with one counted write prints the fleet line naming it; a clean graded record prints `over none`; a derived-LANDED-only population prints none · none
New arm: `tools/drift-audit/selftest.py` · node d's `test_fleet_over_budget`: no conf, a conf with no record, one build over, `over none`, the record deleted · `CHECK_FLOOR` rises by 9

## 8. Open questions

- **F1** — Which of node d's check 23 parts does this unit still build?
  Options: all of them, rewritten against main; the fleet line and the drift signal only; nothing,
  observing main's half and retiring the unit. The budget key and the ceiling refusal reverse
  aWindowedPass unit 5's landed ruling; range mode has no pushed pass to skip; retiring leaves a
  graded run's writes visible only from a checkout on its own branch.
  RESOLVED (agent, 2026-10-04, delegated): the fleet line and the drift signal, with AC1 observing
  the half main already carries.
- **F2** — Do the drift reader's comment lines keep node d's bytes?
  Options: keep them, naming a `budget` field main spells differently and a `range` field main does
  not print; rewrite only those lines. The code lines stay byte-identical either way, and a comment
  describing a line the leg never prints is the stale-record class this build exists to remove.
  RESOLVED (agent, 2026-10-04, delegated): rewrite only those comment lines, per S3 and AC6.
- **F3** — What does the fleet line's budget field say?
  Options: omit it; `budget 0 per build`, node d's words; `budget 0 per run`. Main grades each run
  record against zero, the parser ignores the field, and a reader of a green bar learns the rule
  from it.
  RESOLVED (agent, 2026-10-04, delegated): `budget 0 per run`, per S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from unit 62's split, node d's spec and commit `d99cd0328`, a
  three-way merge probe of its files against this tree, and main's check 23 as aWindowedPass left
  it.

## 10. Reuse audit

The seams are node d's drift reader at `d99cd0328`, applied as bytes, and main's check 23 counters
in `tools/unattended/check-unattended.sh`, which S1 totals; the reader sits beside
`measure_legs_retried_after_timeout` in `tools/drift-audit/drift_report.py` and shares its
`_RUN_RECORD_DIR` constant. `python tools/codebase-map/reuse_lookup.py "report live runs whose
undeclared writes no leg failed, read from the newest bar run record"` returned only name-stem
neighbours, `read_text`, `run` and `report` among them, and printed `unscanned layers: .sh`, so check
23's counters were read from source instead. Recall returned the aWindowedPass unit 5 spec and its
acceptance ledger, which landed the per-run zero and the `OTHER RUN` line, the protocol row marking
the ceiling key retired, and `TOOL-cMendedVintage-14`, the earlier ratchet. Where the brief and the
tree disagree: the brief lists the budget key, the ceiling key and the measuring flag as this unit's
work; main settled all three by another route after node d branched.

Recall terms used: `python tools/memory-recall/query.py "where does a live run's counted undeclared
write get reported when no checkout on its branch runs check 23" --terms "check 23 undeclared write
OTHER RUN UNBOUND ceiling retired fleet budget drift signal run record gate-run"`
