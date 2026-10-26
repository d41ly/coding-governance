# TOOL-dTotalRecall-80 — unit 69's AC1 pair is answered by manifest-check's own C5 verdict at unit 69's pass commit and at its parent, replacing unit 76's S20 answer

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 16 at BLOCKER**. It shares item **B1** with ids 1, 23 and 34, which are
`TOOL-dTotalRecall-79`, `TOOL-dTotalRecall-77` and `TOOL-dTotalRecall-78`.

`TOOL-dTotalRecall-69` (order 32) re-stamps `last-audit`, and its AC1 copies C5's predicate: W, the
newest watched commit, is an ancestor of S, the newest commit changing the stamp. Round 6 (item L5)
ruled that a copy of a predicate is not an answer, and `TOOL-dTotalRecall-76`'s S20 answers it by
"the S19 sweep's line for pass(69)", C5's verdict there. That sweep greps for `fail 5`, a string
the checker never prints (`skills/session-kickoff/manifest-check.sh:1279`), so the line for pass(69)
can never appear and S20 reads green whatever C5 did. Minors M15 and L5 of round 6 then close on an
empty observation.

This unit answers unit 69's AC1 by the checker itself, read by `TOOL-dTotalRecall-77`'s
`read_checker`, at unit 69's pass commit and at its parent. The parent shows the C5 red the re-stamp
was made to clear, and the pass commit shows whether it cleared it. It repairs
`TOOL-dTotalRecall-76`, at step 36, one above that unit's order.

## 2. Scope (IN)

- **S1** — The two reads. Unit 69's pass commit is `pass_of 69` (`TOOL-dTotalRecall-81`). Each of it
  and its parent is checked out by `add_scratch_worktree` under the git common directory and read by
  `read_checker` with the labels `p69` and `p69^`. Observed by AC1.
- **S2** — The answer. Unit 69's AC1 is answered green where `p69` prints no
  `MANIFEST check 5 FAILED` line, and red where it prints one. The ledger states whether `p69^`
  printed a check-5 line: a C5 red the re-stamp cleared, or none, meaning the re-stamp followed no
  red. Observed by AC1 and AC2.
- **S3** — The records. Where `p69` prints a check-5 line, unit 69 departed from its AC1 and AC2,
  and a deviation record of `TOOL-dTotalRecall-69` names the line. Unit 76's S20 answer, read from a
  line that could not appear, is named in a deviation record of `TOOL-dTotalRecall-76`. Each record
  is written only where `git grep -l` over the build folder lists none naming that departure.
  Observed by AC2.

## 3. Non-goals (OUT)

- The sweep over every pass commit and its spans: `TOOL-dTotalRecall-78` and `TOOL-dTotalRecall-79`.
- Remedying a C5 red at unit 69's pass: a landed pass is history. A red at this build's tip is unit
  79's to remedy.
- Unit 69's AC2 exit status, which is the same run's status line and which S2 quotes.
- Editing unit 69's or unit 76's spec, each frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S20 answer, which this unit replaces with the checker's verdict
- **consumes-from** `TOOL-dTotalRecall-77` — `read_checker`, the read both commits get
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of`, which resolves unit 69's pass commit by the driver's rule
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S3's records are written through

## 4. Design

### The reads

```bash
# run from the repository root, with unit 77 §4's read_checker and unit 81 §4's pass_of sourced
P=$(pass_of 69) || { echo "p69 red no pass commit"; exit 1; }
W="$(git rev-parse --git-common-dir)/mc80"
for R in "$P" "$P^"; do
  L=p69; [ "$R" = "$P" ] || L='p69^'
  add_scratch_worktree "$W" "$R" || { echo "$L red worktree-add-failed $R"; continue; }
  read_checker "$W" "$L"
  remove_scratch_worktree "$W" || echo "$L red orphan $W"
done
```

`add_scratch_worktree` resolves `$P^` through git's own revision grammar, and a `$P` that resolved
cannot leave a bare `^`, since the first line stops on an empty pass.

### The answer

| `p69` | `p69^` | Unit 69's AC1 | Records |
|---|---|---|---|
| no check-5 line | a check-5 line | green, the re-stamp cleared C5 | unit 76's S20 only |
| no check-5 line | no check-5 line | green, no red preceded the re-stamp | unit 76's S20 only |
| a check-5 line | any | red | unit 69's and unit 76's S20 |

Unit 76's S20 answer departs in every row, because it was read from a line the sweep could not
print; the record names that the departure is in how it was read, and states whether this unit's
answer agrees with it.

### The deviation records

Each is written by `python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id>`
with one `--field` per REQUIRED name of `tools/memory-tree/deviation_join.py:146`, `Hand-off`
`spec-to-code`, `Cause` `review finding`, the approver under the chain's `author-recorded` value
(`PLAY-dClosedLoop-4`) and `Caused-by` `TOOL-dTotalRecall-80`. Its Evidence names both labelled
reads and item B1.

### Why order 36

The reads rest on unit 77's `read_checker` at step 36 and unit 81's `pass_of` at step 22, and the
record replaces an answer unit 76 made at step 35.

### Inventory

Minted: nothing in code; at most one deviation record each of `TOOL-dTotalRecall-69` and
`TOOL-dTotalRecall-76`.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S3)

### Alternatives rejected

- **Take pass(69)'s line from unit 78's sweep.** The sweep reads pass commits only, and `p69^` is
  not one unless another unit's pass happens to sit there. Two reads of its own cost one checkout.
- **Re-run unit 69's AC1 pair.** That is the copy of C5's predicate round 6's item L5 refused.

## 5. Production-readiness checklist

- security — no surface. One scratch worktree, removed after each read.
- perf / scale — two checkouts and two checker runs.
- error / empty / loading states — an unresolved pass, a failed add and a failed removal each print a
  named red line; each read prints its status.
- observability — the ledger quotes both labelled reads.
- risks — none beyond the read's, which unit 77 states.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's reads run at this pass's base, they print a `p69 rc=` line and a `p69^ rc=`
  line, and no line starting `p69 red` or `p69^ red`.
  Red when: either commit is not read, or a read prints no status.
  permission: `bash skills/session-kickoff/manifest-check.sh` is the argv of the `kickoff-manifest ratchet`
  leg, which no role agent may run (`.claude/roles.json`). The main loop runs §4's two reads when
  this unit is dispatched and records the output in this unit's acceptance ledger under a
  `Pass: none` commit, before the builder's pass reads it.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-80" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC2 line answers unit 69's AC1 from the `p69` read and quotes both reads.
  `git grep -l "deviation TOOL-dTotalRecall-76" -- memory/builds/dTotalRecall/build` prints one
  record naming S20, and where `p69` printed a check-5 line the same for `TOOL-dTotalRecall-69`
  prints one record naming it.
  Red when: unit 69's AC1 is answered from anything but the `p69` read, or an owed record is absent.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is two runs of the checker through unit 77's read, whose staged red that
unit observes.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 16
  (BLOCKER, item B1, shared with ids 1, 23 and 34).

## 10. Reuse audit

The seams are the checker, run through `TOOL-dTotalRecall-77`'s `read_checker`, the driver's pass
rule through `TOOL-dTotalRecall-81`'s `pass_of`, and the scratch-worktree pair of
`tools/run-gates/lib-attribute.sh:59` and `:63`. `python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`
ranked `add_scratch_worktree` among its SEAM candidates. The recall query below found the audit's B1
item and `TOOL-dTotalRecall-75`, neither of which reads C5 at a past commit. No existing seam fits
beyond them.

Recall terms used: `python tools/memory-recall/query.py "how is the kickoff manifest checker read at a past commit without losing its exit status" --terms "manifest-check exit status fail line MANIFEST check FAILED sweep worktree pipe grep ratchet C9"`
