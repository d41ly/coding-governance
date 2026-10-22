# TOOL-dTrueNorth-15 — check 29 counts what it graded on every run, and says so when nothing was

**Status:** CLOSED · rev-2 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 2

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-15-deviation-14.md](../build/2026-10-21-build-TOOL-dTrueNorth-15-deviation-14.md) | deviation | — |
| [2026-10-21-build-TOOL-dTrueNorth-15-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-15-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md](../build/2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md) | journal | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 TOOL-dTrueNorth-31 TOOL-dTrueNorth-32 TOOL-dTrueNorth-33 |
| [2026-10-21-prompt-TOOL-dTrueNorth-15-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-15-build-brief.md) | journal | — |
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-16 |
| [2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md) | diff-review | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 41 at HIGH**, its item **H8**: check 29 grades an empty population on the
harness path and says nothing. `TOOL-dTrueNorth-3` S5 grades only chain-build specs at `INPROGRESS`,
and the unattended driver never writes that status: each spec goes `OPEN` to `CLOSED` in its build
commit. On every chain run the check passes having graded nothing, and its green reads as a coverage
refusal it never applied. This unit makes `--check-coverage` print the graded count on every armed
run, naming an empty population as such and why, and files the trigger question the finding puts to
the owner as an ask. It repairs `TOOL-dTrueNorth-3`.

## 2. Scope (IN)

- **S1** — `cmd_check_coverage` (`TOOL-dTrueNorth-3` S5) prints one line on every armed run, refused or
  green: `build-index: coverage — check 29 graded <k> INPROGRESS chain spec(s) in <j> of <b> chain
  build(s)`. At `k` = 0 the line continues `— nothing graded: no chain spec is INPROGRESS, and under
  the unattended harness a spec goes OPEN to CLOSED in its build commit, so this check grades attended
  builds only`. The off line `TOOL-dTrueNorth-3` S5 prints stays as it is. Observed by AC1 and AC2.
- **S2** — Check 29 prints the verb's output on a green run as well as a red one, the way checks 24
  and 26 print their delegate's capture (`tools/memory-tree/check-memory-hygiene.sh:1581-1634`), so the
  count reaches every full hygiene run. Observed by AC3.
- **S3** — The owner's question, filed: one ask row and its `SEV` row in
  `memory/builds/dClosedLoop/BACKLOG.md`, in that file's grammar, asking whether check 29's trigger
  extends to the status a harness-run chain spec holds past its build's Design exit. Its id is the next
  `PLAY-dClosedLoop-<n>` above every one the tree spells at the pass's base. Observed by AC4.

## 3. Non-goals (OUT)

- Extending the trigger (§8 F2). The clause names `INPROGRESS`, and the extension is the owner's.
- A gate that fails any hygiene check able to pass with zero graded, the finding's suggested
  left-shift. It is a separate gate over every check, so a separate unit by M2; S1 is the instance.
- The staged trigger of check 29: `TOOL-dTrueNorth-16`'s item for id 45.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-3` — `cmd_check_coverage`, its `--check-coverage` verb and hygiene check 29's delegation; without them there is no check to count for
- **hands-off** `TOOL-dTrueNorth-20` — the coverage off line's spelling, §4 Evidence's corrected command, and the ask commit's renders and id reconcile (the round-2 spec audit's ids 4, 14, 31 and 43)

## 4. Design

### Evidence

- `grep -n INPROGRESS tools/unattended/unattended.sh` finds one comment line, and the driver closes
  each unit spec in its own build commit (`tools/unattended/unattended.sh:13482-13483`).
- Attended builds do use `INPROGRESS`: `git grep -l 'Status:\*\* INPROGRESS' -- 'memory/builds/*/spec/'`
  prints specs of non-chain builds, so the population is empty on the harness path, not everywhere.
- The hygiene engine already prints a graded-nothing notice for its §3 edge arms, its §8 F-item arms
  and check 25 (`tools/memory-tree/check-memory-hygiene.sh:2724-2750`), the house shape S1 follows.
- dClosedLoop's asks read `- <id> · filed <date> · <text> · accept <criterion>`, each with a
  `- SEV · <id> · <grade> · <consequence>` row (`memory/builds/dClosedLoop/BACKLOG.md:5`, `:17`).

### The ask

```markdown
- PLAY-dClosedLoop-<n> · filed <the pass's date> · CHECK 29 GRADES ATTENDED BUILDS ONLY. dTrueNorth's hygiene check 29 refuses a chain build's spec at INPROGRESS while its build's coverage is red, as cl-dClosedLoop-0003 states, and the unattended harness closes each spec OPEN to CLOSED in its build commit, so on every harness-run chain build the check grades nothing; TOOL-dTrueNorth-15 announces the empty population on every run. · accept the owner rules whether check 29's trigger extends to the status a harness-run chain spec holds past its build's Design exit, and a ruling to extend it is specced as a departure from cl-dClosedLoop-0003
- SEV · PLAY-dClosedLoop-<n> · LOW · a harness-run chain build's red coverage is caught at the next spec landing rather than refused at its build pass
```

The `<n>` and the date are the pass's to fill, by the rule in S3.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/builds/dClosedLoop/BACKLOG.md`

### Alternatives rejected

- **The count on stderr only.** Check 29's capture is stdout, and a count the hygiene run discards
  is the silent skip this unit exists to end.

## 5. Production-readiness checklist

- security — no new surface; the ask row is the one write outside this build's folder README
  build-level rule 7 admits.
- perf / scale — none; the count is read from the value the verb already holds.
- error / empty / loading states — the empty population is now a line, never a silence.
- observability — the count line, on every armed run.
- risks — none beyond one more line in the hygiene output.
- testing — AC1, AC2 and AC4 as probes; AC3 through the hygiene suite's arm.
- migration — none.
- user docs — `memory/HYGIENE.md` item 29 is `TOOL-dTrueNorth-3`'s; the count line is self-describing.

## 6. Acceptance criteria

- **AC1** — When `python3 tools/memory-tree/gen_build_index.py --check-coverage` runs in a scratch clone
  under `%TEMP%` at the pass's commit, where no chain spec is `INPROGRESS`, it exits 0 and prints
  `check 29 graded 0 INPROGRESS chain spec(s)` followed by `nothing graded`.
  Red when: a green run prints no count, so an empty population reads as coverage.
  fixture: a scratch clone under a short `%TEMP%` path.
- **AC2** — When the clone sets one dTrueNorth spec's header to `INPROGRESS` with coverage otherwise
  clean, the same command exits 0 and prints `check 29 graded 1 INPROGRESS chain spec(s) in 1 of`.
  Red when: the count line is absent, or counts 0 over a population of one.
- **AC3** — When the hygiene engine runs check 29 over AC1's clone, its output carries the count line.
  Red when: check 29 drops the delegate's stdout on a green run.
  permission: the hygiene engine is a gate leg no role agent may run; the main loop observes it
  through the hygiene suite's `New arm:` line in §7.
- **AC4** — When `grep -n 'CHECK 29 GRADES ATTENDED BUILDS ONLY' memory/builds/dClosedLoop/BACKLOG.md`
  runs after the pass, it prints one ask row, and `grep -c 'SEV · PLAY-dClosedLoop-'` over the same file
  counts one more than at the pass's base.
  Red when: the question the finding puts to the owner is handed off with no row.

## 7. Gates

`build-index selftest` · `memory-hygiene self-test` · `memory hygiene` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC3 · check 29 over a fixture chain build with no INPROGRESS spec, red against the base verb that prints nothing on a green run · that suite's assertion floor, raised by the arms added

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — Keep the `INPROGRESS` trigger and announce the gap, or extend it?** (a) Keep it, with S1's
  count line. (b) Extend it to an `OPEN` chain spec of a build whose run has passed its Design exit.
  (b) changes what `cl-dClosedLoop-0003` refuses, a departure from the clause no ruling of the owner's
  covers, and reads the unattended kit's run-state file from the memory-tree kit, a dependency on
  another kit's record; veto 2 discards it outside the grant, and (a) survives, so rung 5 is not
  reached. Recommendation (a), with (b) filed as the owner's ask (S3). Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F3 — Does the build's grant lift veto 2 for the generator and engine edits?** Both are governance
  carriers by `PLAY-dClosedLoop-10`'s list, and `cl-dClosedLoop-0003` names memory hygiene's refusal,
  whose count this is. RESOLVED (agent, 2026-10-21, delegated): lifted by `PLAY-dClosedLoop-3`,
  rung 3. grants: PLAY-dClosedLoop-3 check 29's graded-count line for the refusal cl-dClosedLoop-0003
  names · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 41 (HIGH, item H8).
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-20, promoted by the
  round-2 spec audit, the mirror of its consumes-from; no other section moves.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "count the graded population and announce an empty
one"` ranked name stems and no counter, so the seam was found by reading the engine: the graded-nothing
notices for the §3 edge arms and check 25 (`tools/memory-tree/check-memory-hygiene.sh:2724-2750`),
whose shape S1 takes, and checks 24 and 26's delegation, which S2 follows. The ask row follows the
grammar `memory/builds/dClosedLoop/BACKLOG.md` already holds. No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
