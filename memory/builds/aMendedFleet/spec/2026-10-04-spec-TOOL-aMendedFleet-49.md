# TOOL-aMendedFleet-49 — the unattended close prints the BASE..HEAD drift delta

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 49

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A run closes without anyone seeing what it did to the repo's record of itself: whether it drained a
drift signal, raised one, or swapped its members at an equal count. `TOOL-aMendedFleet-48` makes every
bar append its drift readings to `drift-history.tsv` in the clone's common git dir, and the close
runs the bar, so the reading at the close's HEAD exists by the time the Definition of Done has been
evaluated. This unit adds the one reader the close needs, `drift_report.py --delta <base> <head>`,
and has `--close` print its output as a report-only block, so the wrap-up carries the delta from a
file instead of from a recollection.

## 2. Scope (IN)

- **S1** — `drift_report.py --delta <base> <head>` reads the history file `TOOL-aMendedFleet-48`
  writes, through the same path resolver, and locates its columns by the header. It takes ONE
  `git rev-list --parents <head> <base>` and derives both ancestor sets from that graph. It refuses
  with exit 2 only when either argument does not resolve to a commit. Observed by AC1 and AC2.
- **S2** — The two readings. A GROUP is the rows of one write, keyed by `utc` and `sha`. The BASE
  reading is the last-appended group whose `sha` is BASE or an ancestor of it. The HEAD reading is
  the last-appended group whose `sha` is HEAD or an ancestor of it and is not an ancestor of BASE, so
  the two never name one reading. Each is printed with its own sha and whether it equals its end or
  is an ancestor of it. Observed by AC1.
- **S3** — The delta, one line per signal that moved, in the HEAD group's order: its value at BASE
  and at HEAD; `members changed` when the values are equal and `key_hash` differs; the state when a
  side is not `live`; `absent` for a signal one group lacks. When nothing moved it prints one line
  saying so. Observed by AC1.
- **S4** — Every case that cannot produce a delta prints one `skipped` line naming the reason and
  exits 0: no history file in this clone, a header this engine does not write, no reading at or
  before BASE, and no reading inside BASE..HEAD. None of them prints a zero delta. Observed by AC2.
- **S5** — In `tools/unattended/unattended.sh`, a function `print_drift_delta` takes the run-state
  file, reads its `base` fact, resolves python with the inline `resolve_python`, resolves the
  drift-audit kit with the library's `resolve_kit_dir` from the driver's own `KIT_DIR`, runs
  `--delta <base> HEAD` and prints its stdout under one heading line saying the block is report
  only. A python or kit that does not resolve prints one skip line naming which. It never writes,
  never calls `fail`, and always returns 0. Observed by AC3 and AC4.
- **S6** — `verb_close` calls `print_drift_delta` once, after the Definition-of-Done loop and before
  the `[ "$unmet" = 0 ] || return 1` line, so a refused close shows the delta too. Observed by AC4.
- **S7** — The kit README of drift-audit gains `--delta` in its layout row for `drift_report.py`
  and two sentences on what it reads. Observed by AC5.
- **S8** — The unattended driver suite gains one arm that closes a fixture run with a hand-written
  history file and asserts the block's heading and one moved signal. NOT OBSERVED by a criterion
  here: the suite runs once at the close, and the arm is declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- Writing any history. Rows are `TOOL-aMendedFleet-48`'s, and only the bar writes them.
- Running drift at BASE to manufacture a reading. It costs a worktree at BASE and a full report;
  a missing BASE reading is announced instead, and it becomes rarer as bars accumulate on the node.
- Any refusal. The block is report-only: a close never fails on what drift did.
- A new `.unattended.conf` key naming the drift CLI. It would owe a row in the protocol's binding
  key table, a governance carrier, and the library's `resolve_kit_dir` already reaches a sibling
  kit without one.
- The close's other report-only blocks, the touched-file open asks and the unrefreshed dossiers,
  which are units 66 and 83 of this build. Each is its own call beside this one.
- The kickoff card's drift line, which is a later unit of this build.
- Bumping the drift-audit or unattended kit version here; each is owed once at the build's close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-48` — the history file, its header contract and its path
  resolver. Without it every close prints the no-history skip line.
- **hands-off** external — the kit version bumps owed at the build's close.

## 4. Design

### Output

```
unattended: drift delta, report only — from the bar readings in this clone's drift history
drift-delta: BASE 7af5f564 read at 35438ba0 (an ancestor) · HEAD 1a2b3c4d read at 1a2b3c4d (equal)
drift-delta:   run_records_nonterminal_but_merged 13 -> 2
drift-delta:   readme_mechanism_drift 31 -> 31 (members changed)
drift-delta:   dangling_pointers_in_own_ledger dead -> live 0
```

The shas above are illustrative.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `--delta` | CLI flag of `drift_report.py` | CLI subcommand flag |
| `read_history_groups` | function | Python function, verb `read` |
| `derive_drift_delta` | function | Python function, verb `derive` |
| `render_drift_delta` | function | Python function, verb `render` |
| `print_drift_delta` | shell function in the driver | shell function, verb `print` |

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/README.md`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- An `awk` reader of the TSV inside the driver. No conf key, but a second parser of a file another
  kit writes, which is two answers to one question; the Python reader sits beside the writer and
  shares its constants.
- The nearest reading by commit distance rather than by append order. It needs a distance per
  candidate group, and the last-appended group already is the close's own bar on the HEAD side,
  which is the case that matters.

## 5. Production-readiness checklist

- security — N/A — reads local git data and a node-local file; the only argument passed in is the
  `base` fact, which `--delta` resolves as a commit or refuses.
- perf / scale — one `rev-list --parents` over HEAD's history and one read of the history file, in
  a verb that has just run a full bar.
- error / empty / loading states — S4's four skip lines and S5's two.
- observability — the block itself, and its heading names it report only.
- risks — a BASE reading taken at an older ancestor overstates what the run moved; S2 prints which
  sha each side was read at, so the reader can see it.
- testing — AC1 to AC3 observe the mode and the function directly; the suite arm is S8's.
- migration — N/A — a new mode and a new printed block.
- user docs — S7's README sentences; the close prints its own heading.

## 6. Acceptance criteria

- **AC1** — When a `git clone --local` of the tree into a short directory under `%TEMP%` holds a
  hand-written `drift-history.tsv` in its common git dir, with the S2 header, one group at that
  clone's `HEAD~3` and one at `HEAD`, and `python tools/drift-audit/drift_report.py --delta HEAD~3 HEAD`
  runs there, it prints both readings with `equal`, one line for a signal whose value moved, one
  `members changed` line for a signal whose hash alone moved, and no line for an unchanged signal.
  Red when: an unchanged signal is printed, or a hash-only move is missed.
- **AC2** — When the same clone's history is deleted, or holds only a group at `HEAD`, or opens
  with a different header, `--delta HEAD~3 HEAD` prints exactly one `skipped` line naming that
  reason and exits 0; and `--delta 0000000 HEAD` exits 2.
  Red when: any of the three prints a delta or a bare zero.
- **AC3** — When `awk '/^print_drift_delta\(\)/,/^}/' tools/unattended/unattended.sh` is written to a
  scratch script beside a sourcing of `tools/unattended/lib-unattended.sh` and the driver's
  `resolve_python`, and called in the AC1 clone on a run-state file whose `base` fact is that
  clone's `HEAD~3`, it prints the report-only heading followed by AC1's lines and returns 0; with
  `KIT_DIR` pointed at an empty directory it prints one skip line naming the unresolved kit and
  returns 0.
  Red when: a missing kit returns non-zero or prints nothing.
  cost: about a minute to assemble the slice by hand.
- **AC4** — When `grep -n "print_drift_delta" tools/unattended/unattended.sh` runs, it prints the
  definition and exactly one call, and that call's line number is below the Definition-of-Done loop
  and above the `[ "$unmet" = 0 ] || return 1` line in `verb_close`.
  Red when: the call sits after that return, so a refused close never prints the delta.
- **AC5** — When `grep -c -- "--delta" tools/drift-audit/README.md` runs, it reports at least 1.
  Red when: the mode ships undocumented.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `drift-audit wiring` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture close with a hand-written history file in the fixture's common git dir · none
New arm: `tools/drift-audit/selftest.py` · the four skip cases and one moved, one hash-only and one unchanged signal · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — How does the driver reach the drift reader without spelling the sibling kit's path?
  RESOLVED (agent, 2026-10-04, delegated): through the library's `resolve_kit_dir`, as
  `resolve_index_generator` reaches the memory-tree generator. A conf key was rejected in §3: it
  owes a row in the protocol's key table, a governance-carrier change outside this mandate.
- **F2** — Which reading stands for BASE when no bar ran at BASE itself?
  RESOLVED (agent, 2026-10-04, delegated): the last-appended group at BASE or an ancestor of it,
  printed with the sha it was read at, per S2. Refusing whenever BASE has no exact reading would
  leave the block silent on most runs, since `base` is the run branch's tip at preflight.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

The seams extended are `drift_report.py`'s `main` argument parser and `TOOL-aMendedFleet-48`'s
history path resolver and column constants; on the driver side, `resolve_kit_dir` and
`resolve_index_generator` in `tools/unattended/lib-unattended.sh`, which are the sanctioned route from
an engine to a sibling kit, and `print_reap_targets` in `tools/unattended/unattended.sh`, the existing
report-only print the close makes before evaluating its Definition of Done. `python
tools/codebase-map/reuse_lookup.py "print the drift delta between base and head at the unattended
close"` returned `delta` and `print_report` in `tools/memory-tree/transition_audit.py`, which compare
two audit runs of a different file and share no data, and named `.sh` as unscanned; `git grep -n
"drift" -- tools/unattended/unattended.sh` covers that layer and finds no drift reader. Node d's
unlanded rewrite of the unattended kit carries no drift delta either, read on its branch with
`git grep`. Where the report and the tree disagree: none; the close prints no drift today.

Recall terms used: `python tools/memory-recall/query.py "does the unattended close print drift or
any report-only block" --terms "unattended --close report-only block drift delta BASE HEAD wrap-up
kickoff card drift-history"`
