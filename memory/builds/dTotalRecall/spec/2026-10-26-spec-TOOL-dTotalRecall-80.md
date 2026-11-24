# TOOL-dTotalRecall-80 — unit 69's AC1 pair is answered by manifest-check's own C5 verdict at unit 69's pass commit and at its parent, replacing unit 76's S20 answer

**Status:** INPROGRESS · rev-4 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 36 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-80-deviation-801.md](../build/2026-10-26-build-TOOL-dTotalRecall-80-deviation-801.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-80-deviation-802.md](../build/2026-10-26-build-TOOL-dTotalRecall-80-deviation-802.md) | deviation | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-80-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-80-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-80-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-80-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-80-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-80-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-77-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-87 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-88 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 71 to 76
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-71-spec-audit-round1.md`)
confirmed finding **id 16 at BLOCKER**. It shares item **B1** with ids 1, 23 and 34, which are
`TOOL-dTotalRecall-79`, `TOOL-dTotalRecall-77` and `TOOL-dTotalRecall-78`.

`TOOL-dTotalRecall-69` (order 32) reads `last-audit`, and its AC1 copies C5's predicate: W, the newest
watched commit, is an ancestor of S, the newest commit changing the stamp. Round 6 (item L5) ruled
that a copy of a predicate is not an answer. `TOOL-dTotalRecall-76`'s S20 answers it by the S19 sweep's
line for pass(69). As audited, that sweep grepped for `fail 5`, a string the checker never prints, so
the line could not appear and S20 read green whatever C5 did.

Two premises of the finding have moved. Unit 76 rev-4 reads the checker's own text
(`skills/session-kickoff/manifest-check.sh@f7011dd6f:2396`) and its exit status, so its line for
pass(69) is C5's verdict there. Unit 69 rev-3 stamped nothing: unit 65's commit `f1e11ac49` bundled the
stamp, and pass(69), `f7011dd6f`, touches no watched path and not the manifest (DERIVED 2026-11-24, `git show --name-only`).

This unit answers unit 69's AC1 by the checker itself, at unit 69's pass commit and at its parent. The
first read is the one unit 76's sweep made, lifted from its record by the driver's pass sha. The second
is one run, which no sweep makes. The parent shows whether a C5 red stood before unit 69's pass. It
repairs `TOOL-dTotalRecall-76`, at step 36, one above that unit's order.

## 2. Scope (IN)

- **S1** — The two reads. Unit 69's pass commit is `pass_of 69` (`TOOL-dTotalRecall-81` §4). The read
  labelled `p69` is the sweep's, lifted by §4's `read_sweep_line` out of unit 76's build brief and
  acceptance ledger, keyed on that sha and relabelled, where that sweep's own `live` read is red. The
  read labelled `p69^` is §4's parent read through `TOOL-dTotalRecall-77`'s `read_checker`, which the
  main loop runs before this unit's dispatch and hands over in the build brief (§8 F2). The ledger holds both outputs verbatim in one fenced block and spells a read line nowhere else, since
  `TOOL-dTotalRecall-97` counts every other line that names one. Observed by AC1.
- **S2** — The answer. Unit 69's AC1 is answered green where `p69` prints no
  `MANIFEST check 5 FAILED` line, and red where it prints one. The ledger states whether `p69^`
  printed a check-5 line. No stamp of unit 69 stands between the two commits, so a red at the parent
  and none at the pass is a contradiction, and the ledger names it as one. Observed by AC1 and AC2.
- **S3** — The records. Where `p69` prints a check-5 line, unit 69 departed from its AC1, and a
  deviation record of `TOOL-dTotalRecall-69` names the line. Unit 76's S20 answer owes a deviation
  record of `TOOL-dTotalRecall-76` only where its ledger holds no sweep line for pass(69), or states
  another C5 verdict there than S2's; its rev-4 reads the printed text, so none is owed for how it was
  read. Each record is written only where §4's predicate lists none. Observed by AC2.

## 3. Non-goals (OUT)

- The sweep over every pass commit and its spans: `TOOL-dTotalRecall-78` and `TOOL-dTotalRecall-79`.
- Remedying a C5 red at unit 69's pass: a landed pass is history. A red at this build's tip is unit
  79's to remedy.
- Unit 69's AC2, at its rev-3 a git probe of the stamp's shape, which no checker run answers.
- Keying the answer on whether C5 ran at all: `TOOL-dTotalRecall-91` and `TOOL-dTotalRecall-96`.
- Editing unit 69's or unit 76's spec, each frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-76` — its S20 answer, which this unit replaces with the checker's verdict, and its S19 sweep's lines for pass(69) and for `live`
- **consumes-from** `TOOL-dTotalRecall-77` — `read_checker`, the read the parent gets, and the two line shapes it prints, which both reads keep
- **consumes-from** `TOOL-dTotalRecall-81` — `pass_of`, which resolves unit 69's pass commit by the driver's rule
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S3's records are written through
- **hands-off** `TOOL-dTotalRecall-91` — its `p69` and `p69^` reads and its answer to unit 69's AC1, which that unit classifies and answers again (the round-1 audit of units 77 to 88, id 23)
- **hands-off** `TOOL-dTotalRecall-92` — the `gate-mc80` worktree path, no longer `mc80`, which that batch finds clear, and the readers of that path §4 names (the round-1 audit of units 77 to 88, id 19)
- **hands-off** `TOOL-dTotalRecall-96` — its `p69` and `p69^` reads, which that unit classifies again by a status that must agree with the failure lines (the round-1 audit of units 89 to 92, id 12)
- **hands-off** `TOOL-dTotalRecall-97` — its acceptance ledger, from which that unit extracts the `p69` and `p69^` read lines (the round-1 audit of units 89 to 92, id 30)

## 4. Design

### The pass read, lifted

```bash
# run from the repository root, with unit 81 §4's pass_of sourced
read_sweep_line() {  # unit number · pass sha · label · path... -> that pass's sweep lines, relabelled, each once
  local n=$1 p=$2 l=$3; shift 3
  grep -rhoE "(^|[^0-9])$n $p (rc=[0-9]+|MANIFEST check [0-9]+ FAILED.*)" "$@" \
    | sed -E "s/^.*$n $p /$l /; s/[\`[:space:]]+\$//" | awk '!seen[$0]++'
}
P=$(pass_of 69) || { echo "p69 red no pass commit"; exit 1; }
read_sweep_line 69 "$P" p69 memory/builds/dTotalRecall/build memory/builds/dTotalRecall/prompts
```

The sha is the key, so a sweep that read another commit for unit 69 yields no line. Both of unit 76's
records, and any later record of the same sweep, are read: a read recorded twice prints once, and two
records that disagree print two status lines, which is AC1's red.

PINNED, measured 2026-11-24 at `aec378661` with this function over scratch files: `69 <sha> rc=0` beside
lines of units 70 and 169 printed `p69 rc=0` alone; an indented `rc=1` line and a backticked check-5
bullet printed `p69 rc=1` and the labelled failure line; two different statuses printed both; another sha
printed nothing. Over the tree it printed nothing, since unit 76 has not built, and `pass_of 69` printed
`f7011dd6fc390d088e0d790c5e6c6901fd20edd6`.

### The parent read

```bash
# the main loop's, from the repository root, in the background, its output kept for the brief, with
# unit 77 §4's read_checker, unit 81 §4's pass_of and tools/run-gates/lib-attribute.sh sourced
P=$(pass_of 69) || { echo "p69^ red ${P#red 69 }"; exit 1; }
W="$(git rev-parse --git-common-dir)/gate-mc80"
if add_scratch_worktree "$W" "$P^"; then
  echo "parent $(git -C "$W" rev-parse HEAD)"
  read_checker "$W" 'p69^'
  remove_scratch_worktree "$W" || echo "gate-mc80 red orphan $W"
else
  echo "p69^ red worktree-add-failed $P^"
fi
```

The path is the one shape the common directory admits for a scratch worktree: `check_pockets`
(`tools/memory-tree/record_kinds.py#check_pockets`) reds a bare `mc80`, which no witness row's home
matches, and the `gate-*` home matches this one.

PINNED 2026-11-24, with a stub body in the checker's place, in a scratch clone: it printed
`parent ff3c1b93aa888d71bbeb81b6af92f0b1ebd4ea0e`, a status line and the stub's failure line, and left no
worktree. A sha naming no commit and an empty one, which leaves a bare `^`, each printed the add's red, and
an unresolved pass its cause. Where the lift prints no status line, the sweep having printed a red for
that commit, the main loop runs the same block at `$P` with the label `p69` before the dispatch.

### The answer

| `p69` | `p69^` | Unit 69's AC1 | What the ledger states |
|---|---|---|---|
| no check-5 line | no check-5 line | green | no red preceded the pass, which stamped nothing |
| no check-5 line | a check-5 line | green | the contradiction S2 names |
| a check-5 line | any | red | the line, and unit 69's record |

The inputs C5 reads agree at both commits: W and S are `f1e11ac49` at `ff3c1b93a` and at `f7011dd6f`
(DERIVED 2026-11-24, unit 69 AC1's commands at each). The first row is what they lead a reader to
expect, and the checker's lines alone decide it.

### The deviation records

Each is written by
`python tools/memory-tree/gov_record.py new deviation --build dTotalRecall --unit <id> --title <text>`
with one `--field` per required name of the deviation entry of `tools/memory-tree/build_records.py#KINDS`,
each value inside that entry's closed sets: `Departs from` `<id>@rev-<n> [<section> <label>]` at the rev
the unit built from, `Hand-off` `spec-to-code`, `Cause` `review finding`, `Risk` `loosening`, `Approver` opening with
the role `author` under the chain's `author-recorded` value
(`tools/memory-tree/deviation_join.py#HOST_APPROVAL`, `PLAY-dClosedLoop-4`), `Follow-through`
`ask TOOL-dTotalRecall-27` and `Caused-by` `TOOL-dTotalRecall-80`. Its Evidence names both labelled reads and item B1.

It is written only where
`git grep -l --all-match -e 'Serves:\*\* deviation <id>$' -e 'Caused-by:\*\* TOOL-dTotalRecall-80$' -- memory/builds/dTotalRecall/build`
lists nothing. For unit 69 it lists nothing and exits 1 at `aec378661`, and with `PLAY-dClosedLoop-2` for
the cause it lists `2026-10-26-build-TOOL-dTotalRecall-69-deviation-691`, the roster promotion (DERIVED
2026-11-24), so the predicate is seen both ways and that record never counts.

### Why order 36

The lift reads what unit 76 recorded at step 35, by unit 81's `pass_of` of step 22, and the line shapes
are unit 77's, at step 36, which the §3 edge runs first.

### Inventory

Minted: the probe function `read_sweep_line`, spec text only; at most one deviation record each of
`TOOL-dTotalRecall-69` and `TOOL-dTotalRecall-76`. Naming cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger and the records of S3)

### Alternatives rejected

- **Take `p69^` from a sweep too.** Unit 76's and unit 78's sweeps read pass commits only, and `p69^` is
  a records commit, no unit's pass.
- **Re-run unit 69's AC1 pair.** That is the copy of C5's predicate round 6's item L5 refused.
- **The bare name `mc80`, as rev-3 wrote it.** Every session's `check_pockets` reds while it stands,
  the audit's id 19.
- **A lift that reads unit 76's ledger alone.** The sweep is recorded twice, in that unit's brief and
  its ledger, and reading both is what can find them disagreeing.

## 5. Production-readiness checklist

- security — no surface. One scratch worktree, removed after the read.
- perf / scale — one worktree and one checker run, off the pass.
- error / empty / loading states — an unresolved pass, a failed add, a failed removal and a pass with no
  sweep line are each a red, never a green read.
- observability — the ledger quotes both labelled reads and the parent's sha.
- risks — the lift reads recorded text. A sweep line mis-copied into unit 76's records is answered as
  copied, unless a second record disagrees.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's `read_sweep_line` runs at this pass's base over `memory/builds/dTotalRecall/build`
  and `memory/builds/dTotalRecall/prompts`, it prints exactly one line starting `p69 rc=`, or nothing
  where the build brief carries the main loop's `p69` run instead, and
  `grep -rlE "(^|[^a-z0-9])live rc=1" memory/builds/dTotalRecall/build` lists unit 76's acceptance ledger. The
  brief's parent read prints `parent` with the sha `git rev-parse <pass_of 69>^` prints and exactly one
  line starting `p69^ rc=`. No line of either read starts `p69 red` or `p69^ red`, and
  `git worktree list --porcelain` names no path ending `/gate-mc80`.
  Red when: either commit is not read, a read prints no status, two records of one read disagree, or
  the sweep's staged read was green.
  permission: `bash skills/session-kickoff/manifest-check.sh` is the argv of the `kickoff-manifest ratchet`
  leg, which no role agent may run (`.claude/roles.json`). The main loop runs the parent read in the
  background before this unit is dispatched and hands its output in the build brief.
- **AC2** — When `git grep -n "Evidences:\*\* TOOL-dTotalRecall-80" -- memory/builds/dTotalRecall/build`
  runs after the pass, its ledger's AC2 line answers unit 69's AC1 from the `p69` read, names the row of
  §4's table and sets it beside unit 76's S20 answer, and one fenced block of that ledger holds AC1's two
  outputs verbatim. §4's `git grep -l --all-match` predicate prints one record for
  `TOOL-dTotalRecall-69` where `p69` printed a check-5 line, one for `TOOL-dTotalRecall-76` where S3 owes
  it, and none otherwise.
  Red when: unit 69's AC1 is answered from anything but the `p69` read, an owed record is absent, or a
  record no S3 condition owes is written.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the parent read is one run of the checker through the read unit 77 sees red, the sweep's own
staged red is AC1's, and the lift's outcomes are pinned in §4.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which of the two checker runs is made here, now that unit 76's sweep reads pass(69)?** Options:
  (a) both, as rev-3 wrote it; (b) `p69` lifted from the sweep's record and `p69^` run once by the main
  loop; (c) neither, the parent read cut because unit 69 stamped nothing. (c) fails AC1 and leaves units
  91, 96 and 97 no `p69^` line to read; veto 1 discards it. (a) and (b) satisfy the same criteria, and
  (b) reuses a read already on record. RESOLVED (agent, 2026-11-24, delegated): (b), the tie-break's
  reuse, per `2026-11-24-prompt-TOOL-dTotalRecall-80-reground-brief`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 71 to 76, id 16
  (BLOCKER, item B1, shared with ids 1, 23 and 34).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-91, TOOL-dTotalRecall-92, each the other end of an edge a
  unit the round-1 spec audit of units 77 to 88 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-96, TOOL-dTotalRecall-97, each the other end of an edge a
  unit the round-1 spec audit of units 89 to 92 promoted wrote; nothing else moved.
- rev-4 · 2026-11-24 · §1 · S1 · S2 · S3 · §3 · §4 · §5 · AC1 · AC2 · §7 · §8 F2 · §10 · re-grounded at
  `aec378661` per `2026-11-24-prompt-TOOL-dTotalRecall-80-reground-brief`, over unit 69 rev-3 as built
  and unit 76 rev-4: `p69` is lifted from unit 76's sweep, `p69^` is one main-loop run in `gate-mc80`,
  which `check_pockets` admits and `mc80` it reds, unit 76's record is owed only on a missing or disagreeing answer, unit 69's AC2 is a git probe,
  the deviation fields and the existence predicate are spelled, and citations are pinned.

## 10. Reuse audit

The seams are the recorded lines of `TOOL-dTotalRecall-76`'s sweep, the checker run through
`TOOL-dTotalRecall-77`'s `read_checker`, the driver's pass rule through `TOOL-dTotalRecall-81`'s
`pass_of`, and the scratch-worktree pair `add_scratch_worktree` and `remove_scratch_worktree` of
`tools/run-gates/lib-attribute.sh`, each re-read at `aec378661`.
`python tools/codebase-map/reuse_lookup.py "run a checker at each historical commit in a scratch worktree"`,
re-run 2026-11-24, ranked `add_scratch_worktree` among its SEAM candidates. The recall query below was made
when the spec was written. It found the audit's B1 item and `TOOL-dTotalRecall-75`, neither of which
reads C5 at a past commit. `TOOL-dTotalRecall-97`'s `c5_input` lifts read lines out of a ledger, and is
unbuilt and keyed on one label with no sha. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how is the kickoff manifest checker read at a past commit without losing its exit status" --terms "manifest-check exit status fail line MANIFEST check FAILED sweep worktree pipe grep ratchet C9"`
