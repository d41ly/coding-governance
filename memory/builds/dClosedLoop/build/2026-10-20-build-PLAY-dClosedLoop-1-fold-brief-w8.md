# Fold brief: writer 8, the owner's answers on flow-steps

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the owner's answers to the fifteen forks below into dClosedLoop's design records, as one fold
script that runs after the six fold scripts.** This brief is your instructions, not a spec to review. Writer 7 folds
the other eighteen answers in parallel; its forks are listed at the end so you can stay clear of its lines.

## What you fold, and against what

- **The subject is the design records as the six fold scripts leave them.**
  - `<scratch>` stands for
    `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad`.
  - The scripts are `<scratch>/fold/w<n>/fold-<n>.py` for n from 1 to 6. They apply to the working tree at commit
    `e7b58e2ee`. Read them, never edit them.
  - The folded copies of the twelve records they change are in `<scratch>/fold/composite6/`. Every other record is
    unchanged, so read it in the working tree.
  - Your script runs after the six. Each `sub` and `insert_before` must match the composite's text exactly once, or
    the working tree's for a record the composite does not hold.
- **Each fork's question, options and reasoning** are in the saved return of the writer that raised it, under
  `## 3. Forks`. The returns are `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w<n>.md`.
  The findings each fork rests on are in the three walk reports,
  `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-whole-walk-{a,b,c}.md`.
- **Your records** are every design record your forks need. Most of the work is in flow-steps, the recut record's
  `[reconciled-order]` table, and the v2 clauses your forks name. Writer 7 edits v2's policies and several layer
  records, so apply the shared-lines rule below.
- **Read freely** in the working tree, the composite and the six scripts. Write only in `<scratch>/fold/w8/`. Nothing
  goes into the repository, and nothing is read from the sealed copy.

## Your forks and the owner's answers

The answers below are the owner's, verbatim, given on 2026-10-20 through the question tool. Fold each one as chosen.
Five of the owner's 33 answers chose an option the question did not recommend. Three of them are yours: FK-4-2,
FK-4-12 with FK-5-2, and FK-4-13. Fold the option the owner picked.

| Fork | Raised by | The owner's answer | What the answer means |
|---|---|---|---|
| FK-4-1 | w4 | "Hold, then amend (Recommended)" | Options (A) with (i). While the owner attends, a confirm gate or a live question is held until `run.owner-deadline`, then `run.on-owner-silence` applies, and `run.on-owner-question` decides only unattended items (cl-0207). A late answer is placed by `entry.place` as an amendment that re-enters the item it answers, drawing on `flow.rework-budget`. The amendment row gains `planning`. |
| FK-4-2 | w4 | "Yes, as LR-3 reads" | Option (A), not the recommendation. `best-effort-recorded` may fill the landing gate and the design gate under `three-gates` and `every-stage`. Only ratifications are excluded, as LR-3 reads today. Fold the smallest text that makes this explicit where B3-F4 found it unclear. Where the records already say it, record that no edit is needed. |
| FK-4-3 | w4 | "Inventory + owner item (Recommended)" | Option (A). `adopt-parent-work`: the child's plan revision takes in the parent's kept units through the child's `design.inventory`, at the parent's kept branch tip. `withdraw-too`: an owner item proposing the child's withdrawal. |
| FK-4-4 | w4 | "Placement disposition (Recommended)" | Option (A). A `breakpoint` disposition in `entry.place`'s closed set names the live build. Its witness is the intake record plus the placement disposition. `review.trigger`'s "owner's request record" becomes "the placement disposition naming the breakpoint". |
| FK-4-5 | w4 | "Units, then exhaustion (Recommended)" | Option (B), plus the ordering. While budget remains, a blocking item's open work becomes a new unit, then goes to `flow.on-exhausted`. A non-blocking item's open work goes to asks. Whichever bound a review loop reaches first, `flow.route-backs` or `review.max-rounds`, ends it, and both promote the same way. |
| FK-4-6 | w4 | "Stays reconstructed (Recommended)" | Option (A). A candidate the raters split on stays `reconstructed` and not major. It goes to `adopt.decisions-ratify` only under `docs-owner-ratifies` or `docs-and-trailers`. |
| FK-4-7 | w4 | "Yes, landing-turn ref (Recommended)" | Option (A). A compare-and-swap landing-turn ref on the remote, built with `gap-flow-08`'s queue, orders landings across nodes. cl-0422 gets the cross-node turn, which writer 6 left to this fork. |
| FK-4-8 | w4 | "Unarmed (Recommended)" | Option (C). Before dScopedBuild's `build.distill` writes rows, `deploy.distill` records "measured nothing", is never green, and routes on. The landing record says so, as `test.seed`'s unarmed seed does. |
| FK-4-9 | w4 | "Rules bullet + rows (Recommended)" | Option (A). See "FK-4-9's rows" below. |
| FK-4-10 | w4 | "Wait, then owner item (Recommended)" | Option (A). A paused build's pause is a declared wait within `flow.wait-ceiling`, then an owner item to resume, withdraw or stay paused. If that item goes unanswered at `run.owner-deadline`, the build is parked and its lease released. |
| FK-4-11 | w4 | "Split the key (Recommended)" | Option (A). `verdict.flakes` splits into an entry threshold and the release streak of 3 greens. The entry threshold counts flakes in a window. Its default is "measured", and 2 in the leg's last 10 verdicts until measured. Each key gets its `[policies]` and `[presets]` rows, because the preset check reds a presettable key with no preset row. |
| FK-4-12 + FK-5-2 | w4, w5 | "build.acceptance" | w5's option (A), not the recommendation. The executor writes the seen-red record at `build.acceptance`, re-running each new gate's planted red, one record per gate, keyed by leg and red SHA. `test.seen-red` stays its reader, and a planted gate with no recorded red reds it. `build.acceptance` is dScopedBuild's, which lands after the reader's build, so declare its stand-in as FK-4-9's answer does. Edit the layer-memory kind row's writer and the flow-steps witnesses. |
| FK-4-13 | w4 | "Revert row, no draw" | Option (A), not the recommendation. A testing → building transition row covers a best-effort descope's revert of a failing unit already in Test's tree. It draws nothing on the budget, being an ending and not a lap. |
| FK-5-4 | w5 | "A flow item (Recommended)" | Option A. A dKeptSession flow item answers a mailbox `question`. `next` dispatches it when a question arrives, and it is run by the role that owns the asked interface or item. The recipient's refused transition becomes a declared wait inside `flow.wait-ceiling`, so `leases.renewal: progress` renews the lease. |
| FK-6-1 | w6 | "Refuse (Recommended)" | Option (a). Before dPlacedRequest lands `leases.offline`, `review.report` refuses a `new:` slug's claim on an unreachable remote. No slug is claimed and no local id is minted. The finding stays in the report with its slug marked unclaimed, and is disposed of by hand. A tolerance row in recut's table names this. |

## FK-4-9's rows

The owner chose one `[rules]` bullet in flow-steps plus one tolerance row per forward route in recut's
`[reconciled-order]` table. The bullet says that until an item's owning build lands, a route into it reaches today's
stand-in:

- the attended session's agent, for a role item;
- today's tool, for a command;
- `push-main.sh`, for the lander.

The forward routes are those the reconciliation probe lists with `--all-routes`, run on a folded copy. The probe's
default run reads fewer route edges. It reports a class row with no dependency it reads as a finding, so check both
runs before you add rows:

- Rows that only `--all-routes` needs may red the default run.
- If they do, add rows only for the routes the default run reads, and report the remainder with their counts.
- Probe changes are the main loop's to make. Do not edit the probe.

## Writing the fold

- **New clauses.** Each ends with a placeholder id, `` `cl-dClosedLoop-W8-<k>` `` for k = 1, 2, …, never a real
  number, and never an edit to `[clause-ids]`' next id. The main loop's mint step (`<scratch>/fold/mint.py`) numbers the
  placeholders after both writers' scripts, and updates every place that cites them.
- **Lines writer 7 also edits.** Writer 7 folds FK-1-1 to FK-1-7, FK-1-4 with FK-3-1, FK-2-1 to FK-2-4, FK-3-2, FK-3-3,
  FK-5-1, FK-5-3, FK-5-5, FK-5-6 and FK-6-2. Its edits fall in v2's `[policies]` and `[presets]` rows for `budgets.*`,
  `install.*`, `leases.expiry-hours`, `roles.model`, `design.streams`, `patch.ratify` and `maintain.*`. They also fall in
  the lease and landing clauses (cl-0133, cl-0135, cl-0293, cl-0324, cl-0333, cl-0337), cl-0015, cl-0026, cl-0058,
  cl-0115, cl-0143, cl-0150, cl-0332 and cl-0397, and in layer-expansions' kits, maintain and release items.
  FK-3-3's rename of `design.streams` (the key) to `design.streams-when` reaches flow-steps:187-189 and the
  `policy.design.streams` conditions too.
  - Add a new row or bullet with `insert_before`, before a line neither of you rewrites. Two inserts before one anchor
    both apply.
  - Rewrite a line only when your own fork names it.
  - A line that both your fork and writer 7's need goes under *Requests*, with the exact change, and stays out of your
    script.
- **The revision log.**
  - v2: if you edit v2, add one "Revised 2026-10-20 by the whole-design audit's fork answers" paragraph for your forks,
    inserted before the line that opens "Revised: 2026-10-17, after the folds' closing review".
  - flow-steps: add its own revision note in its `[revised]` section.
  - Any other record that keeps a revision log gets a short note.
- **Register.** Short declarative sentences in the records' own register, and no new term where a defined one exists.
  Name a stand-in wherever a clause or an item relies on a later build.

## Checking your script

You may dry-run the scripts on your own folder:

```sh
DRY_DIR=<scratch>/fold/w8/dry FOLD_ORDER="1 2 3 4 5 6 8 mint" bash <scratch>/stall/dry_run.sh <scratch>/fold/all.py
```

It ends `ALL rc 0` when the build's ten final checks pass. Without writer 7's script, three reconciliation probe lines
stay: `patch.ratify`, read by dPlacedRequest and dShippedRelease and cited by dPlacedRequest. FK-6-2 resolves them.
Name any other red, and the fork that clears it.

To list every probe line, run this from the dry folder's root:

```sh
python -X utf8 memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py \
  memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md [--all-routes]
```

## What you return

Your final message, nothing else:

1. **Dispositions,** one row per fork: `| fork | records · places | disposition | the fold's one-line gist, or what
   stops it |`. The disposition is `fold`, or `fork` when the answer needs a choice the owner did not make.
2. **Fold script:** `<scratch>/fold/w8/fold-8.py`, how many edits it makes in which records, and its placeholder
   ids.
3. **Forks,** each `### FK-8-<k> — <question>`, then the options, your recommendation and the fork it rests on; or
   `none`.
4. **Requests** for lines writer 7 also edits, or `none`.
5. **The dry run:** its last line and any red check, or `not run`.
6. **Read outside the list above:** `none`, or what and why.
