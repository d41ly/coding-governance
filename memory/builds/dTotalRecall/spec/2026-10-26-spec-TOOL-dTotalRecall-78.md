# TOOL-dTotalRecall-78 — the S19 sweep visits every unit's pass commit by the driver's rule in a placed scratch worktree, and a commit it cannot resolve or check out is a printed red

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 34 at BLOCKER**. It shares item **B1** with ids 1, 16 and 23, which are
`TOOL-dTotalRecall-79`, `TOOL-dTotalRecall-80` and `TOOL-dTotalRecall-77`.

`TOOL-dTotalRecall-76` (order 35) sweeps the checker over "every unit id with a pass commit". Its
loop resolves each pass by a `git log --grep` first line and runs
`git worktree add --detach "$D/w" "$P" >/dev/null && (…)`. An empty `$P` or a failed add
short-circuits the `&&`, so that commit prints no line, and the grep after the checker prints no line
either. A sweep that checked nothing therefore reads exactly as a sweep that found every commit
green. The failure envelope has no red in it.

This unit is the sweep. Its population is derived from the build README's generated build order,
every unit at a step below 36. Each unit's pass commit is resolved by the driver's rule through
`TOOL-dTotalRecall-81`'s `pass_of`, checked out by the kit's scratch-worktree helpers under the git
common directory, and read by `TOOL-dTotalRecall-77`'s `read_checker`. Every unit of the population
prints exactly one verdict line, a status or a named red, so the sweep's line count is its own
liveness. It repairs `TOOL-dTotalRecall-76`, at step 36, one above that unit's order.

## 2. Scope (IN)

- **S1** — The population. The units at a step below 36 in the README's `gen:build-order` region,
  in step order, derived by §4's `awk` and never typed. Observed by AC1.
- **S2** — The resolution. Each unit's pass commit is `pass_of <n>`. A unit with none prints
  `<n> red no pass commit`, never a skip. Observed by AC1.
- **S3** — The checkout. Each resolved commit is checked out by `add_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh:59`) at one path under `$(git rev-parse --git-common-dir)`,
  where a long scratch path cannot push it past MAX_PATH. A failed add prints
  `<n> red worktree-add-failed <sha>`. After the read, `remove_scratch_worktree` (`:63`) removes it,
  and a failed removal prints `<n> red orphan <path>`. Observed by AC1 and AC2.
  **Readers:** by name: no name retires, the item removing only the scratch worktree it added for
  each unit, whose path is spelled by `add_scratch_worktree` and `remove_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh:59`, `:63`) and their callers `tools/run-gates/post-merge.sh`,
  `tools/run-gates/run-gates.sh` and `tools/run-gates/run-selftests.sh` · by value: NO VALUE READERS —
  each worktree is made and removed inside this item, and no reader outside it compares, counts or
  derives from its path.
- **S4** — The read. Each checked-out commit is read by `read_checker` with the label `<n> <sha>`.
  Observed by AC1.
- **S5** — The record. The sweep's whole output goes into this unit's acceptance ledger as a fenced
  block under its AC1 answer, the input units 79 and 88 read. Observed by AC2.

## 3. Non-goals (OUT)

- Reading one commit: `TOOL-dTotalRecall-77`.
- Deriving red spans and judging unit 76's AC13: `TOOL-dTotalRecall-79`.
- Unit 69's AC1 pair: `TOOL-dTotalRecall-80`.
- Removing unit 76's own leftover scratch directory and worktree (item L6, id 22): the batch
  `TOOL-dTotalRecall-88`.
- Editing unit 76's spec, frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S19 population and loop, which this sweep replaces
- **consumes-from** `TOOL-dTotalRecall-77` — `read_checker`, the read each commit gets; without it the sweep repeats the grep that reads nothing
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of`, the driver's pass rule each unit's commit is resolved by
- **hands-off** `TOOL-dTotalRecall-79` — the sweep's lines in this unit's ledger, from which that unit derives the red spans
- **hands-off** `TOOL-dTotalRecall-88` — the sweep's lines for the pass commits of units 75 and 76, which that batch reads for its items of ids 6 and 35
- **hands-off** `TOOL-dTotalRecall-92` — the sweep's block, its `population` line and the `mc78` worktree path, which that batch counts, completes and clears (the round-1 audit of units 77 to 88, ids 3, 13, 19, 27)

## 4. Design

### The sweep

```bash
# run from the repository root, with unit 77 §4's read_checker and unit 81 §4's pass_of sourced
README=memory/builds/dTotalRecall/README.md
UNITS=$(awk -F'|' '/\/gen:build-order/{f=0;next} /gen:build-order/{f=1;next} f && $2+0>=1 && $2+0<36 {print $3}' "$README" \
        | grep -oE 'TOOL-dTotalRecall-[0-9]+' | sed 's/.*-//')
W="$(git rev-parse --git-common-dir)/mc78"
for N in $UNITS; do
  P=$(pass_of "$N") || { echo "$N red no pass commit"; continue; }
  if ! add_scratch_worktree "$W" "$P"; then echo "$N red worktree-add-failed $P"; continue; fi
  read_checker "$W" "$N $P"
  remove_scratch_worktree "$W" || { echo "$N red orphan $W"; break; }
done
echo "population $(printf '%s\n' $UNITS | grep -c .)"
```

An orphan stops the loop, because every later add would fail at the same path. The last line states
the population's size, so AC1 can count the verdict lines against it.

PINNED, measured 2026-10-26 at `af814dba8`: the `awk` derivation prints 67 units, the build order of
units 1 to 76 at steps 1 to 35. Once this build's audit adds units 81 to 87 at steps 22, 34 and 35,
the derivation includes them, which is correct: their passes precede this one.

### Why order 36

Every pass commit the sweep reads exists by step 35's end. Unit 77's read and unit 81's resolution
come first, by the §3 edges; unit 79 reads this unit's output, so the edge to it runs this pass
before unit 79's.

### Inventory

Minted: nothing in code; the sweep's output in this unit's acceptance ledger.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger)

### Alternatives rejected

- **The population as "every unit with a pass commit".** A unit whose pass does not resolve leaves
  that population silently, which is the vacuous selector of
  `memory/gotchas/vacuous-selector-empty-population.md`. The roster's build order is the population,
  and an unresolved member is a red.
- **`tempfile.mkdtemp` for the worktree, as unit 76 wrote it.** The directory is never removed, and a
  long TMP path can pass MAX_PATH; `lib-attribute.sh`'s header names the git common directory for
  that reason.
- **One worktree per commit, kept until the end.** About seventy checkouts held at once, for no
  reading the reuse of one path lacks.

## 5. Production-readiness checklist

- security — no surface. One scratch worktree, removed after each read.
- perf / scale — one checkout and one checker run per unit, about seventy-five in all, each seconds.
- error / empty / loading states — an unresolved pass, a failed add and a failed removal are each a
  named red line. No unit can print nothing.
- observability — each verdict line names the unit and the sha read.
- risks — a unit whose first pass is a records-only commit is read there, the driver's own answer.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's sweep runs at this pass's base, the number of its lines matching
  `^[0-9]+ ([0-9a-f]{40} rc=[0-9]+|red )` equals the value on its `population` line, and each unit of
  the population leads exactly one of them.
  Red when: a unit of the population prints no verdict line, or the population is empty.
  cost: one checker run per unit, minutes in all.
  permission: `bash skills/session-kickoff/manifest-check.sh` is the argv of the `kickoff-manifest ratchet`
  leg, which no role agent may run (`.claude/roles.json`). The main loop runs §4's sweep when
  this unit is dispatched and records the output in this unit's acceptance ledger under a
  `Pass: none` commit, before the builder's pass reads it.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-78" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC1 answer holds the sweep's output in a fenced block, and
  `git worktree list --porcelain` names no path ending `/mc78`.
  Red when: the output is summarised rather than recorded, or the sweep left its worktree behind.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the sweep's liveness is its own line count against its derived population, and unit
77's staged red proves the read inside it.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 34
  (BLOCKER, item B1, shared with ids 1, 16 and 23).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.

## 10. Reuse audit

The seams are the README's generated build-order region as the population, the driver's pass rule
through `TOOL-dTotalRecall-81`'s `pass_of`, the scratch-worktree pair of
`tools/run-gates/lib-attribute.sh:59` and `:63`, and `TOOL-dTotalRecall-77`'s `read_checker`.
`python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`
ranked `add_scratch_worktree` among its SEAM candidates and no sweep over commits. The recall query
below found the audit's B1 item and `TOOL-dTotalRecall-75`, neither a sweep. No existing seam visits
commits; the loop is eight lines over the seams.

Recall terms used: `python tools/memory-recall/query.py "how is the kickoff manifest checker read at a past commit without losing its exit status" --terms "manifest-check exit status fail line MANIFEST check FAILED sweep worktree pipe grep ratchet C9"`
