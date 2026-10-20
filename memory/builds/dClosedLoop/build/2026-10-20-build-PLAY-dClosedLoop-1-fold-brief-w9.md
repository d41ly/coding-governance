# Fold brief: writer 9, the fold's integration

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the items below, as one fold script that runs after the eight fold scripts and before the mint
step, so the build's ten final checks pass.** This brief is your instructions, not a spec to review.

## What you fold, and against what

- **Paths.** `<scratch>` is
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad`.
- **The subject** is the design records as `<scratch>/fold/w<n>/fold-<n>.py`, for n from 1 to 8, leave them. Those
  scripts are applied to the working tree at commit `10c0c4fb4`.
  - The records they change are in `<scratch>/fold/composite8/`. They are taken before the mint step, so writers 7
    and 8's new clauses still end with their placeholder ids, `cl-dClosedLoop-W7-<k>` and `-W8-<k>`.
  - Every other record is unchanged, so read it in the working tree.
  - Each `sub` and `insert_before` of yours must match that text exactly once.
- **The returns.** The eight writers' saved returns are
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w<n>.md`. The owner's answers are
  verbatim in the round record's `[fold]` section, `build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.
- **The probe is widened.** The reconciliation probe (`build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py`, in
  the working tree) now reads every route target in every run. Its docstring had kept the default run to the
  breakpoint program "until the audit's fold classes what it finds", and the owner's FK-4-9 asks for those rows.
  - Before the change, the default run found no forward routes. After it, it finds 21 on the unfolded tree, the same
    lines the old `--all-routes` run printed, and 28 on the folded copy. Both readings are recorded.
  - Don't edit the probe.
- **Your records** are every design record your items need. Write only in `<scratch>/fold/w9/`. Nothing goes into the
  repository, and nothing is read from the sealed copy.

## The items

Number them as below.

1. **probe-1 to probe-28.** These are the widened probe's unclassed lines on the folded copy, one per line in
   `<scratch>/fold/probe-28.txt`: 27 routes into a later build's item, and dTendedCadence's citation of `currency`.
   - Class each route in recut's `[reconciled-order]` table, in its rows' shape (`| Row | Node | Owner | Class |
     Why |`). The source build goes in Row, the target item in Node, its owner in Owner, and the class is
     `tolerance`.
   - The reason names the stand-in the route reaches until the owner lands, under flow-steps' `[rules]` bullet "A route
     into a later build reaches today's stand-in": the attended session's agent for a role item, today's tool for a
     command, and `push-main.sh` for the lander. Read each target's kind from its Actor cell.
   - Where a clause declares its own stand-in for that route, the row names the clause's stand-in instead (item 2).
   - Where the design settles no stand-in for a target, such as an owner item, raise a fork.
   - Generate the rows from the probe's lines inside your script rather than typing 27 rows by hand.
   - For `currency`, choose the class that fits what writer 7's W7-3 clause does with it, or reword the clause if it
     names the leg only as a pattern.
2. **The owner's FK-8-1.** The owner answered: "The clause's own wins (Recommended)". A stand-in a clause declares for
   its own route wins, and the `[rules]` bullet gains "where no clause declares another" (cl-0123's owner item is
   the case writer 8 found, C2-F7). Fold the bullet's words, and let item 1's rows follow them.
3. **The owner's FK-7-1.** The owner answered: "Run may raise, per the file's rules (Recommended)".
   - Once a cap's row moves under `budgets.*` (FK-1-3), the guarded policy command admits a run's raise of a
     measured-file cap under `template-size-limits.txt`'s four conditions (the owner's 2026-10-13 ruling,
     TOOL-aOrientedCast-23), argued in the write's change record.
   - Class rows, lowerings, new rows and removals stay the owner's, and every other agent write to the policy file
     stays refused (cl-0012).
   - Writer 7's return names the places it left open for this: cl-0012, cl-0015, cl-0036 and layer-instruction's rule
     on who may raise a row.
4. **The recut sentence that fold-6 wrote.** Writer 7's request R1 and writer 8's second request both rewrite the
   sentence that says the probe still reds on `leases.offline` and `patch.ratify`. Fold writer 8's merged text, and
   bring the sentence up to date with the widened probe and item 1's rows.
5. **Writer 7's R2.** Add flow-steps' revision note for FK-1-5 and FK-3-3, beside the note fold-8 appends.
6. **Writer 8's first request.** cl-0115's route-back phrase. Writer 7's FK-1-5 already edits cl-0115, so merge the
   two into one text.
7. **The roles matrix.** layer-roles' `role_matrix.py` is the instrument in its `[instrument]` section. Since fold-8
   added `mailbox.answer`, whose Actor cell reads "the role that owns the asked interface or item, one per
   question", the instrument reds under arm 1 on that item.
   - Make the record and its instrument agree. Revise the instrument in the record to read that actor form, as
     writer 6 revised it for the `[probe]` group, with its red and green runs recorded. Or name the actor in a form
     the instrument already reads, whichever keeps one fact in one place.
   - The instrument is not one of the ten final checks. Run it on your dry copy anyway, red and green.
8. **Revision notes.** Add one for every record you edit that keeps a revision log. In v2, add one "Revised 2026-10-20
   by the whole-design audit's fold integration" paragraph, inserted before the line that opens "Revised: 2026-10-17,
   after the folds' closing review".

New clauses, if you need any, end with `` `cl-dClosedLoop-W9-<k>` ``. The mint step numbers them after your script.

## Checking your script

```sh
DRY_DIR=<scratch>/fold/w9/dry FOLD_ORDER="1 2 3 4 5 6 7 8 9 mint" bash <scratch>/stall/dry_run.sh <scratch>/fold/all.py
```

- The run must end `ALL rc 0`. The output shows the last six lines of each check.
- To list every probe line, run this from the dry folder's root:
  `python -X utf8 memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md`
- See one of your rows seen red: the probe's `--plant-drop <build>:<node>` removes a class row in memory.

## What you return

Your final message, nothing else:

1. **Dispositions,** one row per item, with probe-1 to probe-28 as one row giving their class counts:
   `| item | records · places | disposition | the fold's one-line gist |`.
2. **Fold script:** `<scratch>/fold/w9/fold-9.py`, how many edits it makes in which records, and any placeholder
   ids.
3. **Forks,** each as `### FK-9-<k> — <question>`, with its options, your recommendation and the item it rests on.
   Write `none` if there are none.
4. **The dry run:** its last line, any red check, and the planted row's red.
5. **Read outside the list above:** `none`, or what and why.
