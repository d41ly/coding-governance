# TOOL-dTotalRecall-77 — manifest-check is read at one commit by its exit status and its own failure line, never through a grep pipe, and the read is seen red on a staged C9 stall

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 |
| [2026-10-26-build-TOOL-dTotalRecall-77-round7-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-77-round7-fix-return.md) | research | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-77-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-77-1-spec-writer.md) | journal | TOOL-dTotalRecall-1 |
| [2026-10-26-prompt-TOOL-dTotalRecall-77-round7-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-77-round7-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 23 at BLOCKER**. It shares item **B1** with ids 1, 16 and 34, which are
`TOOL-dTotalRecall-79`, `TOOL-dTotalRecall-80` and `TOOL-dTotalRecall-78`.

`TOOL-dTotalRecall-76` (order 35) sweeps `manifest-check.sh` over every pass commit, its S19, and
pipes the checker through `grep -E 'fail (5|9)'`. The checker prints a failure through
`fail() { echo "MANIFEST check $1 FAILED — $2"; status=1; }`
(`skills/session-kickoff/manifest-check.sh:1279`) and exits with that status
(`manifest-check.sh:1626`). The text `fail 5` or `fail 9` therefore never reaches output, and the
pipe discards the exit status. The sweep reads nothing else, so it prints nothing at a red commit
and at a green one. Unit 76's S19 red spans, its S20 verdict at unit 69's pass and its AC13 all rest
on a reading that cannot see a failure.

This unit is the reading of one commit: the checker run in a worktree of that commit, its exit
status recorded as its own line, and each failure line matched by the checker's own format. It is
seen red once, on a staged C9 stall, before any sweep relies on it. It repairs
`TOOL-dTotalRecall-76`, at step 36, one above that unit's order.

## 2. Scope (IN)

- **S1** — The read. §4's `read_checker` runs `manifest-check.sh` in a given worktree and prints one
  line `<label> rc=<status>` for every run, then each output line matching
  `^MANIFEST check [0-9]+ FAILED`, prefixed by the label. The status is captured before any filter
  runs, so no pipe can discard it. Observed by AC1 and AC2.
- **S2** — The staged red. In a scratch worktree of this pass's base, placed under
  `$(git rev-parse --git-common-dir)` by `add_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh:59`), `last-body-change` is set to the eleventh newest
  non-merge commit touching a path of the manifest's `watch:` line. `read_checker` there prints
  `live rc=1` and a `live MANIFEST check 9 FAILED` line. The worktree is then removed by
  `remove_scratch_worktree` (`:63`), and a failed removal prints the orphan's path as a red line.
  Observed by AC1.
  **Readers:** by name: no name retires, the item removing only its own scratch worktree, whose path
  is spelled by `add_scratch_worktree` and `remove_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh:59`, `:63`) and their callers `tools/run-gates/post-merge.sh`,
  `tools/run-gates/run-gates.sh` and `tools/run-gates/run-selftests.sh` · by value: NO VALUE READERS —
  the worktree is made and removed inside this item, and no reader outside it compares, counts or
  derives from its path.
- **S3** — The green read. `read_checker` at this pass's base worktree prints `base rc=<status>` and
  every failure line it finds, so S2's red is set beside a read of the same tree unstaged. Observed
  by AC2.

## 3. Non-goals (OUT)

- Visiting every pass commit: `TOOL-dTotalRecall-78`, which runs this read at each.
- The red spans and unit 76's AC13: `TOOL-dTotalRecall-79`.
- Unit 69's AC1 pair and unit 76's S20: `TOOL-dTotalRecall-80`.
- Fixing a red the read finds at the base: unit 79 owns the tip's verdict.
- Editing unit 76's spec, frozen once its unit builds.
- The output-format lint the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S19 sweep and its AC12 and AC13 lines, whose grep this read replaces
- **hands-off** `TOOL-dTotalRecall-78` — `read_checker`, which that unit's sweep runs at each pass commit
- **hands-off** `TOOL-dTotalRecall-79` — `read_checker` and S2's `live` lines, the known red that unit's span derivation must find
- **hands-off** `TOOL-dTotalRecall-80` — `read_checker`, which that unit runs at unit 69's pass commit and its parent

## 4. Design

### The read

```bash
# run from the repository root
source tools/run-gates/lib-attribute.sh
read_checker() {  # worktree path · label -> "<label> rc=<n>", then each failure line of the checker, labelled
  local out rc
  out=$(cd "$1" && bash skills/session-kickoff/manifest-check.sh 2>&1); rc=$?
  printf '%s rc=%s\n' "$2" "$rc"
  printf '%s\n' "$out" | grep -E '^MANIFEST check [0-9]+ FAILED' | sed "s|^|$2 |"
  return 0
}
```

`rc` is the status of the substitution, taken on the next statement, so the filter below it cannot
change it. A `cd` that fails gives a non-zero `rc` too, never a silent green. The match is the
checker's own line format at `manifest-check.sh:1279`, every check number, so a red from a check
other than 5 or 9 is still printed.

### The staged red

```bash
W="$(git rev-parse --git-common-dir)/mc77"
add_scratch_worktree "$W" HEAD || echo "live red worktree-add-failed"
WATCH=$(sed -n 's/^watch: //p' memory/guides/SESSION-KICKOFF.md | tr ';' ' ')
OLD=$(git rev-list --no-merges HEAD -- $WATCH | sed -n 11p)
sed -i "s/^last-body-change: .*/last-body-change: $OLD/" "$W/memory/guides/SESSION-KICKOFF.md"
read_checker "$W" live
remove_scratch_worktree "$W" || echo "live red orphan $W"
read_checker . base
```

C9 counts non-merge watched commits since `last-body-change` and fails at 10
(`manifest-check.sh:1574-1581`). With `last-body-change` at the eleventh newest watched commit,
the ten newer ones are in the range, so C9 must fail. The edit is to the scratch worktree's file
only and is never committed.

PINNED, measured 2026-10-26 at `af814dba8`: the eleventh newest non-merge watched commit is
`427e1e0385c9d3f1e7b730b16a768d40461ad5cb`, an ancestor of HEAD, and
`git rev-list --count --no-merges 427e1e03..HEAD -- <watch paths>` prints 10. The checker run itself
is the pass's; this spec's writer may not run that leg.

### Why order 36

The read replaces unit 76's grep, so it lands after unit 76's pass at step 35. Units 78, 79 and 80
share step 36 and read through it, so the §3 edges run this pass first.

### Inventory

Minted: the probe function `read_checker`, spec text only. Naming cell: none, no product symbol.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger)

### Alternatives rejected

- **`grep -E 'MANIFEST check (5|9) FAILED'` alone.** It mends the literal and still reads nothing on
  a run that fails another check or crashes before printing. The exit status is the leg's verdict.
- **`grep` with `set -o pipefail`.** It returns grep's status where no line matched, which is 1 on a
  green commit, so a green and a red still look alike to the caller.
- **A staged red by editing a watched file.** It moves C5 as well, so the line expected would depend
  on two checks; editing `last-body-change` alone reaches C9 only.

## 5. Production-readiness checklist

- security — no surface. The scratch worktree is removed, and an orphan is named.
- perf / scale — two checker runs and one worktree.
- error / empty / loading states — a failed worktree add or removal is a red line. A run that prints
  nothing still prints its `rc=` line, so an empty read cannot occur.
- observability — every run prints its status and every failure line.
- risks — on a shallow clone C9 warns and skips (`manifest-check.sh:1568`), and S2 would read
  green. The run's checkout is a full clone, and a `live rc=0` is a red of AC1 that names it.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's staged red runs at this pass's base, it prints `live rc=1` and a line starting
  `live MANIFEST check 9 FAILED`, and no `live red` line.
  Red when: the read prints no `rc=` line, prints `live rc=0`, or prints no check-9 line on a C9
  stall.
  figure: the eleventh-commit sha and the count of 10 are PINNED in §4, measured 2026-10-26; the run
  re-derives both at its base.
  permission: `bash skills/session-kickoff/manifest-check.sh` is the argv of the `kickoff-manifest ratchet`
  leg, which no role agent may run (`.claude/roles.json`). The main loop runs §4's staged red and its base read when
  this unit is dispatched and records the output in this unit's acceptance ledger under a
  `Pass: none` commit, before the builder's pass reads it.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-77" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC1 line quotes the two `live` lines and its AC2 line quotes the
  `base rc=` line with every failure line beneath it.
  Red when: the ledger records a verdict with no `rc=` value.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is this pass's staged red, which proves the read prints a failure.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 23
  (BLOCKER, item B1, shared with ids 1, 16 and 34).

## 10. Reuse audit

The seams are the checker itself, run rather than re-implemented, its own line format at
`skills/session-kickoff/manifest-check.sh:1279`, and the scratch-worktree pair
`add_scratch_worktree` and `remove_scratch_worktree` (`tools/run-gates/lib-attribute.sh:59` and
`:63`), whose header places a worktree under the git common directory. `python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`
ranked `add_scratch_worktree` among its SEAM candidates, with `run` and `check` name-stem
neighbours. The recall query below found the audit's B1 item, `TOOL-dTotalRecall-75` and an
inherited-red ask of `aLevelledCopy` naming this leg, and none of them reads the checker's status at
a past commit. The class a filter on a word belongs to is
`memory/gotchas/a-grep-for-a-word-is-a-presence-probe.md`. No existing seam reads the checker's
verdict; the read is three lines over the two seams.

Recall terms used: `python tools/memory-recall/query.py "how is the kickoff manifest checker read at a past commit without losing its exit status" --terms "manifest-check exit status fail line MANIFEST check FAILED sweep worktree pipe grep ratchet C9"`
