**Serves:** research TOOL-dSafePassage-1 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-13

# Brief — dSafePassage: the six deviation records' After fields, and the parent's clause left to its own build

## The prompt

> The spec commit 5fd9f90c2 re-rendered the as-built view from the six deviation records the writers wrote. Two
> rows lost most of their clause, one of them a dGroundRules clause, and four departures do not show at all.

— the run's main loop, reading `git show 5fd9f90c2 -- memory/builds/dClosedLoop/build/*as-built.md` and the
re-rendered packet

## The brief

### Goal

Make each of the six records under `memory/builds/dSafePassage/build/` render into the as-built view as the clause
the spec actually carries. Leave dGroundRules' clause `cl-dClosedLoop-0012` to dGroundRules' own spec run, through an
ask.

### Items

1. **The rule the view applies.** `asbuilt.py` (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py`)
   renders an `amends` record's `**After:**` as the clause's WHOLE new text. The ` [<section>]` tail on
   `**Departs from:**` scopes nothing in the view. Read that instrument's header and confirm this before you edit.
   Read-only: never edit it.
2. **deviation-11** (`cl-dClosedLoop-0018`). Its After holds only the row's fields, so the view's row dropped the
   legacy homes, `.agent-cap.conf` and `template-size-limits.txt`, with their steps and plants, and the dWitnessedBar
   join. Rewrite After as the clause's full baseline text, quoted from the packet's Items 1, with only the derived
   introducing commit changed. Keep its Reason, Risk and every other field unless that change makes one false.
3. **deviation-12** (`cl-dClosedLoop-0012`, dGroundRules' clause). Withdraw it. Delete the file: it never landed, and
   README rule 7 lets this run reach another build only through an ask row in that build's `BACKLOG.md`. Instead:
   - file one ask in `memory/builds/dGroundRules/BACKLOG.md` under `## Asks`, id `TOOL-dGroundRules-13` (12 is that
     build's carry-forward ask), in that file's row grammar (`tools/memory-tree/row_grammar.py`), filed 2026-10-23.
     It asks dGroundRules' minimal guard to admit the write a declared upgrade step makes on gov's own tree, as
     deviation-12's After and Reason describe: only when every `budgets.*` value reads the same through the policy
     reader after the write as before it. Its accept clause names that guard admitting the step's write and still
     refusing every other shape `cl-dClosedLoop-0012` refuses;
   - add its `SEV` row under `## Dispositions` in the same shape as the existing row;
   - revise `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-1.md` to rev-2, with a §9 line, so it
     cites `TOOL-dGroundRules-13` where it cited deviation-12, and says in §8 that the build run re-grounds against
     the guard dGroundRules lands. Change nothing else in that spec.
4. **deviation-21, -31, -51 and -52** (`cl-dClosedLoop-0024`, `-0028`, `-0030`). Each After restates its clause's
   baseline text byte for byte, so the view shows no change while the record claims a departure, two of them
   `loosening`. For each, decide which holds and act on it:
   - **The clause's text changes.** Rewrite After as the full clause text with the departure applied, so the view's
     row and its hash move.
   - **The clause stands and only the spec departs.** Then the record is not a clause amendment. Re-address
     `**Departs from:**` and `**Follow-through:**` to what the grammar in `memory/HYGIENE.md` "Deviation records"
     allows for that case, so the view does not read it as amending the clause. If no address fits, rewrite After as
     in the first case.
   -51 and -52 both amend `cl-dClosedLoop-0030`. If both still amend it, the newer one names the older in
   `**Supersedes:**`, and its After carries both departures.

### Acceptance

- `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py --write`, run into a
  scratch copy or followed by `git diff`, shows the `cl-dClosedLoop-0012` row back at `baseline`, and the
  `cl-dClosedLoop-0018` row's text still naming `.agent-cap.conf`, `template-size-limits.txt`, `FANOUT_CAP=2` and
  dWitnessedBar.
- Each of the four records in item 4 either moves its clause's row or no longer amends it.
- `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py --build dSafePassage --exit`
  exits 0.
- `python memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py --report dSafePassage`
  lists no record as unjoined that it did not list before your edit.

### Gates

None. A role agent runs no gate. The main loop re-renders and commits.

### Non-goals

No instrument, no v2, no packet and no other spec is edited. The only path outside `memory/builds/dSafePassage/`
you write is `memory/builds/dGroundRules/BACKLOG.md`. No commit, no stage.

### Limitations

This is an unattended run, so nobody will answer a question. Settle any fork by README rule 6's rungs, and put the
reason in the record you change.

### Reuse

The records' own grammar in `memory/HYGIENE.md` "Deviation records"; the ask row grammar in
`tools/memory-tree/row_grammar.py`.
