# TOOL-dTotalRecall-78 — the S19 sweep visits every unit's pass commit by the driver's rule in a placed scratch worktree, and a commit it cannot resolve or check out is a printed red

**Status:** CLOSED · rev-3 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-78-deviation-781.md](../build/2026-10-26-build-TOOL-dTotalRecall-78-deviation-781.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-78-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-78-1-acceptance-ledger.md) | log | — |
| [2026-11-24-build-TOOL-dTotalRecall-78-1-builder-return.md](../build/2026-11-24-build-TOOL-dTotalRecall-78-1-builder-return.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-78-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-78-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-78-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-78-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-78-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-78-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |
| [2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md](../reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md) | diff-review | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-36 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 TOOL-dTotalRecall-114 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 34 at BLOCKER**. It shares item **B1** with ids 1, 16 and 23, which are
`TOOL-dTotalRecall-79`, `TOOL-dTotalRecall-80` and `TOOL-dTotalRecall-77`.

`TOOL-dTotalRecall-76` (order 35) swept the checker over "every unit id with a pass commit". The loop the
audit read resolved each pass by a `git log --grep` first line and ran
`git worktree add --detach "$D/w" "$P" >/dev/null && (…)`. An empty `$P` or a failed add
short-circuits the `&&`, so that commit prints no line, and the grep after the checker prints no line
either. A sweep that checked nothing therefore reads exactly as a sweep that found every commit
green. Its rev-4 loop prints a status or a named red for each commit it visits, but it visits only the
units a `Pass:` trailer names at its own base: a unit with no trailer, and the units of step 35
themselves, still print nothing there.

This unit completes the sweep. Its population is derived from the build README's generated build order,
every unit at a step below 36. Each unit's pass commit is resolved by the driver's rule through
`TOOL-dTotalRecall-81`'s `pass_of`. A commit unit 76's sweep read is taken from its lines; every other
is checked out in one scratch worktree under the git common directory and read by
`TOOL-dTotalRecall-77`'s `read_checker`. Every unit of the population
prints exactly one verdict line, a status or a named red, so the sweep's line count is its own
liveness. It repairs `TOOL-dTotalRecall-76`, at step 36, one above that unit's order.

## 2. Scope (IN)

- **S1** — The population. The units at a step below 36 in the README's `gen:build-order` region,
  in step order, derived by §4's `awk` and never typed. Observed by AC1.
- **S2** — The resolution. Each unit's pass commit is `pass_of <n>`. A unit with none prints
  `<n> red no pass commit`, never a skip, and a pass rule with no launcher prints
  `<n> red the pass rule could not answer, rc 2`, the cause `pass_of` names. No red line leads a unit
  whose spec is CLOSED, so a resolution that answered nothing cannot pass as a population of reds.
  Observed by AC1.
- **S3** — The checkout. One worktree is added by `add_scratch_worktree`
  (`tools/run-gates/lib-attribute.sh#add_scratch_worktree`) at `gate-mc78` under
  `$(git rev-parse --git-common-dir)`, where a long scratch path cannot push it past MAX_PATH, and is
  moved to each resolved commit that is read. A failed add prints `<n> red worktree-add-failed <sha>`
  for each such unit, a failed move `<n> red checkout-failed <sha>`. After the loop,
  `remove_scratch_worktree` (`tools/run-gates/lib-attribute.sh#remove_scratch_worktree`) removes it,
  and a failed removal prints `gate-mc78 red orphan <path>`. Observed by AC1 and AC2.
  **Readers:** by name: no name retires, the item removing only the scratch worktree it added,
  whose path is spelled by `add_scratch_worktree` and `remove_scratch_worktree` and their callers
  `tools/run-gates/post-merge.sh`, `tools/run-gates/run-gates.sh` and
  `tools/run-gates/run-selftests.sh` · by value: `tools/memory-tree/record_kinds.py#check_pockets`,
  which reds an entry of the common directory no witness row's home matches; the `gate-ledger` row's
  `gate-*` home (`tools/memory-tree/record-kinds.toml`) matches this one while it stands.
- **S4** — The read. Each checked-out commit is read by `read_checker` with the label `<n> <sha>`.
  A commit unit 76's sweep read under that label is not read twice: its lines are printed as they
  stand, where that sweep's own `live` read is the red it must be (§8 F2). Observed by AC1.
- **S5** — The record. The sweep runs the leg's own checker, which no role agent may run, so the
  main loop runs it in the background before this pass is dispatched and hands its output in the
  brief. The whole output goes into this unit's acceptance ledger as a fenced block under its AC1
  answer, the input units 79, 88 and 92 read. Observed by AC2.

## 3. Non-goals (OUT)

- Reading one commit: `TOOL-dTotalRecall-77`.
- Deriving red spans and judging unit 76's AC13: `TOOL-dTotalRecall-79`.
- Unit 69's AC1 pair: `TOOL-dTotalRecall-80`.
- The leftovers of unit 76's own sweep (item L6, id 22): the batch `TOOL-dTotalRecall-88`.
- Editing unit 76's spec, frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S19 population and loop: the lines its sweep printed and its `live` read, which this sweep takes over where they were read at the driver's commit, and the trailer population this one replaces
- **consumes-from** `TOOL-dTotalRecall-77` — `read_checker`, the read each commit gets; without it the sweep repeats the grep that reads nothing
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of`, the driver's pass rule each unit's commit is resolved by
- **hands-off** `TOOL-dTotalRecall-79` — the sweep's lines in this unit's ledger, from which that unit derives the red spans
- **hands-off** `TOOL-dTotalRecall-88` — the sweep's lines for the pass commits of units 75 and 76, which that batch reads for its items of ids 6 and 35
- **hands-off** `TOOL-dTotalRecall-92` — the sweep's block, its `population` line and the `gate-mc78` worktree path, which that batch counts, completes and clears (the round-1 audit of units 77 to 88, ids 3, 13, 19, 27)

## 4. Design

### The sweep

```bash
# the main loop's, from the repository root, in the background, its output kept for the brief, with
# unit 77 §4's read_checker, unit 81 §4's pass_of and tools/run-gates/lib-attribute.sh sourced;
# HAVE is a file of the lines unit 76's sweep printed, as the main loop kept them for that unit's brief
README=memory/builds/dTotalRecall/README.md
UNITS=$(awk -F'|' '/\/gen:build-order/{f=0;next} /gen:build-order/{f=1;next} f && $2+0>=1 && $2+0<36 {print $3}' "$README" \
        | grep -oE 'TOOL-dTotalRecall-[0-9]+' | sed 's/.*-//')
W="$(git rev-parse --git-common-dir)/gate-mc78"
if ! { grep -qx 'live rc=1' "$HAVE" && grep -q '^live MANIFEST check 9 FAILED' "$HAVE"; }; then
  echo "the lines of unit 76's sweep are not taken over" >&2; HAVE=/dev/null
fi
MADE=; add_scratch_worktree "$W" HEAD && MADE=1
for N in $UNITS; do
  P=$(pass_of "$N") || { echo "$N red ${P#red "$N" }"; continue; }
  if grep -q "^$N $P rc=" "$HAVE"; then grep "^$N $P " "$HAVE"; continue; fi
  [ -n "$MADE" ] || { echo "$N red worktree-add-failed $P"; continue; }
  git -C "$W" checkout -q --detach --force "$P" || { echo "$N red checkout-failed $P"; continue; }
  read_checker "$W" "$N $P"
done
[ -z "$MADE" ] || remove_scratch_worktree "$W" || echo "gate-mc78 red orphan $W"
echo "population $(printf '%s\n' $UNITS | grep -c .)"
```

The two line shapes are unit 76's and `read_checker`'s alike, `<n> <sha> rc=<status>` and
`<n> <sha> MANIFEST check <c> FAILED`, so a line taken over and a line read are one shape to unit 79.
The last line states the population's size, so AC1 can count the verdict lines against it. A worktree a
killed run left at `gate-mc78` fails the next add, which prints a red per unit and never a green; the
main loop removes it and runs the sweep again.

PINNED, measured 2026-11-24 at `aec378661`: the `awk` derivation prints 72 units, the build order of steps
1 to 35 (PINNED 2026-11-24), and `pass_of` over each, run from a script file, printed a sha for 60 (PINNED 2026-11-24).
The trailer rule of unit 76's loop prints the same sha for each of those and names no other unit.
Each other unit prints `red no pass commit`: TOOL-dTotalRecall-8, -37, -14, -15 and -26, held unbuilt, and
TOOL-dTotalRecall-73, -75, -74, -87, -76, -83 and -84, whose passes had not run. So at this pass's
base the second run reads what unit 76's base could not hold, the passes of units 76, 83 and 84, and the
held units print their reds.

### Why order 36

Every pass commit the sweep reads exists by the end of step 35. Unit 77's read and unit 81's resolution
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
- **A temporary clone, as unit 76 rev-4 makes it.** It needs no name in the common directory, and it is
  a second way to place a scratch checkout beside `lib-attribute.sh`'s pair, whose header names the git
  common directory for its short path.
- **One worktree added and removed per commit, as rev-2 wrote it.** A checkout of the whole tree for
  every unit, where a move of one worktree changes only what differs.
- **The bare name `mc78`, as rev-2 wrote it.** `check_pockets`, landed by `TOOL-dTotalRecall-18`, reds
  it: no witness row's home matches, and the `gate-*` home matches `gate-mc78` (§8 F3).

## 5. Production-readiness checklist

- security — no surface. One scratch worktree, removed after the last read.
- perf / scale — one worktree, then one move and one checker run per unit that unit 76's sweep did not
  read, off the pass and in the background.
- error / empty / loading states — an unresolved pass, a failed add, a failed move and a failed removal
  are each a named red line. No unit can print nothing, and a void `HAVE` reads every unit.
- observability — each verdict line names the unit and the sha read.
- risks — a unit whose first pass is a records-only commit is read there, the driver's own answer.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's sweep runs at this pass's base, the number of its lines matching
  `^[0-9]+ ([0-9a-f]{40} rc=[0-9]+|red )` equals the value on its `population` line, and each unit of
  the population leads exactly one of them.
  No unit leading a `red` line has a spec whose status header reads CLOSED.
  Red when: a unit of the population prints no verdict line or two, the population is empty, or a
  CLOSED unit prints a red.
  figure: the population of §4 is PINNED 2026-11-24; the pass re-derives it at its base.
  cost: one checker run per unit the sweep of unit 76 did not read, off the pass.
  permission: `bash skills/session-kickoff/manifest-check.sh` is the argv of the `kickoff-manifest ratchet`
  leg, which no role agent may run (`.claude/roles.json`). The main loop runs §4's sweep in the
  background before this unit is dispatched and hands the output in its brief. The pass lists the units
  with §4's `awk` itself and counts the lines it was handed against the `population` line.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-78" -- memory/builds/dTotalRecall/build`
  runs after the pass, its AC1 answer holds the sweep's output in a fenced block, and
  `git worktree list --porcelain` names no path ending `/gate-mc78`.
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
- **F2 — Is unit 76's sweep run again, now that its rev-4 prints a verdict per commit?** Options: (a) a
  second read of every commit; (b) the lines that sweep printed at the commit `pass_of` names, and a read
  of every other unit; (c) no run, the ledger citing unit 76's. (c) leaves the units with no trailer and
  those of step 35 with no line, which fails AC1, and leaves `TOOL-dTotalRecall-88` S20 with nothing to
  read; veto 1 discards it. (a) and (b) meet the same criteria, and (b) reuses the read already made, its
  lines taken over only where that sweep's `live` read is red, so a blind sweep is never reused.
  RESOLVED (agent, 2026-11-24, delegated): (b), the reuse tie-break, per
  `2026-11-24-prompt-TOOL-dTotalRecall-78-reground-brief`. widens: none · relaxes: none
- **F3 — Where is the scratch worktree placed?** Options: (a) `mc78` in the common directory, added and
  removed per commit; (b) `gate-mc78` there, added once and moved; (c) a temporary clone. (a) reds the
  pocket arm of `record-kinds` for every session while it stands; veto 1 discards it. (c) drops the pair
  the Goal's placed worktree rests on. RESOLVED (agent, 2026-11-24, delegated): (b), rung 3, the name the
  round-1 audit of units 77 to 88 (id 19) asks for and unit 92's `gate-mc92` follows, per
  `2026-11-24-prompt-TOOL-dTotalRecall-78-reground-brief`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 34
  (BLOCKER, item B1, shared with ids 1, 16 and 23).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.
- rev-3 · 2026-11-24 · §1 · S2 to S5 · §3 · §4 · §5 · AC1 AC2 · §8 F2 F3 · §10 · re-grounded at `aec378661` per
  `2026-11-24-prompt-TOOL-dTotalRecall-78-reground-brief`, over unit 76 rev-4: that sweep prints a verdict per
  commit, so its lines are taken over where `pass_of` names the commit it read and only the rest is read
  (F2); the worktree is `gate-mc78`, made once and moved, as `check_pockets` reds `mc78` (F3); a red line
  carries `pass_of`'s cause and a CLOSED unit may not print one; the main loop's run is handed in the
  brief; the population is re-pinned; citations name symbols.

## 10. Reuse audit

The seams are the README's generated build-order region as the population, the driver's pass rule
through `TOOL-dTotalRecall-81`'s `pass_of`, the lines of `TOOL-dTotalRecall-76`'s sweep, the
scratch-worktree pair `add_scratch_worktree` and `remove_scratch_worktree` of
`tools/run-gates/lib-attribute.sh`, and `TOOL-dTotalRecall-77`'s `read_checker`, re-read at `aec378661`.
`python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`
ranked `add_scratch_worktree` among its SEAM candidates and no sweep over commits. The recall query
below found the audit's B1 item and `TOOL-dTotalRecall-75`, neither a sweep. Unit 76 rev-4's loop visits
commits and is spec text; this loop is a few lines over the seams.

Recall terms used: `python tools/memory-recall/query.py "how is the kickoff manifest checker read at a past commit without losing its exit status" --terms "manifest-check exit status fail line MANIFEST check FAILED sweep worktree pipe grep ratchet C9"`
