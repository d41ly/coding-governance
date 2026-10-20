# Fold brief: writer 7, the owner's answers on v2's policies, leases and the layer records

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the owner's answers to the eighteen forks below into dClosedLoop's design records, as one fold
script that runs after the six fold scripts.** This brief is your instructions, not a spec to review. Writer 8 folds
the other fifteen answers in parallel, and its forks are listed at the end so you can stay clear of its lines.

## What you fold, and against what

- **Paths.** `<scratch>` stands for
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad`.
- **The subject is the design records as the six fold scripts leave them.**
  - The scripts are `<scratch>/fold/w<n>/fold-<n>.py` for n from 1 to 6. They apply to the working tree at commit
    `e7b58e2ee`. Read them, never edit them.
  - The folded copies of the twelve records they change are in `<scratch>/fold/composite6/`. Every other record is
    unchanged, so read it in the working tree.
  - Your script runs after the six. So each `sub` and `insert_before` must match the composite's text exactly once,
    or the working tree's text for a record the composite does not hold.
- **Where each fork is written out.** Each fork's question, options and reasoning are in the saved return of the
  writer that raised it, under `## 3. Forks`. The returns are in `memory/builds/dClosedLoop/build/`, named
  `2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w<n>.md`. The findings each fork rests on are in the three walk
  reports, `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-whole-walk-{a,b,c}.md`.
- **Your records** are every design record your forks need. Writer 8 edits flow-steps heavily, so apply the
  shared-lines rule below.
- **Read freely** in the working tree, the composite and the six scripts. Write only in `<scratch>/fold/w7/`. Nothing
  goes into the repository, and nothing is read from the sealed copy.

## Your forks and the owner's answers

The answers below are the owner's, verbatim, given on 2026-10-20 through the question tool. Fold each one as chosen.
Five of the owner's 33 answers chose an option the question did not recommend. Two of them are yours, FK-1-3 and
FK-1-5, so fold the option the owner picked.

| Fork | Raised by | The owner's answer | What the answer means |
|---|---|---|---|
| FK-1-1 | w1 | "In the build folder (Recommended)" | Option (b). The override record and the exception register are records in the building build's `build/` folder, as deviation records are. They are written in the recording session's commit, and they join memory-plan `[doors]`' stand-in list until dTotalRecall's `record` adopts them. |
| FK-1-2 | w1 | "New id class + edge (Recommended)" | Option (a). In cl-0058, `cl-<slug>-NNNN` becomes a native-id class owned by dTrueNorth, with an `@hash8` pin. A new edge type, `carries-clause` (spec → clause), may carry a pin. memory-plan `[frame]` and `[edges]` change, and P33's count grows by one. |
| FK-1-3 | w1 | "budgets.* now" | Option (a), not the recommendation. `budgets.*` becomes the one declaration of each cap's value now, and an upgrade step migrates `template-size-limits.txt` into it. The key's owner and cl-0015 must then agree, and so must every reader of the caps. |
| FK-1-4 + FK-3-1 | w1, w3 | "Drop delete and refuse (Recommended)" | Drop `install.retired-edits: delete` and `install.on-shim-call: refuse`. `keep` stays, armed with a planted case in cl-0026. Edit the `[policies]` Allowed cells and every place that names the dropped values. |
| FK-1-5 | w1 | "Reopen root record" | Option (c), not the recommendation. Each draw a patch build makes on its closed root's rework budget re-opens the root's transition record under the root's lease. The fold must say how the closed record is re-opened and how concurrent draws serialize, and plant two concurrent draws (cl-0115, cl-0440). |
| FK-1-6 | w1 | "Fixture wins (Recommended)" | Option (a). While the card-import fixture is red, `always-resume` reads as `fresh-when-idle`, and the override is reported (cl-0150). |
| FK-1-7 | w1 | "Drop the session (Recommended)" | Option (a). Until acts are minted, a message's id is derived without the session: build, item instance key, pass, kind, subject and answered id. The check reads every one of the build's per-session refs, and a retry from a new session is planted. |
| FK-2-1 | w2 | "Live until unlease (Recommended)" | Option A. The landing push carries the lease beat and the `landed` notice in one atomic push, and the release stays at `deploy.unlease`. Edit cl-0337 and cl-0333's atomic-landing probe, and reword cloud-and-scale's design item 2. |
| FK-2-2 | w2 | "Supervisor, 'or' (Recommended)" | Option A. The supervisor measures its node's offset at each beat against the remote host's time and records it in the node registry. Either expiry rule expires a lease. Edit cl-0293, the `leases.expiry-hours` row and layer-runtime:837. |
| FK-2-3 | w2 | "Generic sweep, arms move (Recommended)" | Option B. The sweep is generic over each wait's declared deadline and planted with an owner-request wait. The `build.release-ceiling` arm, the release arm of the atomic landing and the key's ownership (v2:1184) move to dShippedRelease. |
| FK-2-4 | w2 | "Beats mark renewal (Recommended)" | Option A. Each beat marks whether it renews, and the observer judges expiry from the last renewing beat. Edit cl-0135, the `leases.expiry-hours` row and cl-0324, with a red arm on a holder repeating one red verdict. |
| FK-3-2 | w3 | "Per-harness key (Recommended)" | Option (a). `roles.model.<role>.<harness>` defaults to each adapter's equivalent of the role's model. The preset check reds a harness set that lacks a model. Edit the `[policies]` row, dBoundRoles' reader and cl-0332. |
| FK-3-3 | w3 | "Rename to design.streams-when (Recommended)" | Option (a). Rename the key in v2 `[policies]`, `[presets]` and cl-0397, and at each of its uses in flow-steps: flow-steps:187-189 and the `policy.design.streams` conditions that fold-4 wrote at its place 175. The planner's item keeps its name. |
| FK-5-1 | w5 | "Command + attended items (Recommended)" | Option A. `kits.install` and `kits.update` become commands, `kits.install-attended` and `kits.update-attended` become owner items, and the outcome set closes from dSafePassage's clauses. |
| FK-5-3 | w5 | "Refuse at record's door (Recommended)" | Option A. `record`'s door refuses a coordination write whose ref path or sender names another session, act or fleet tag. A terminal tombstone is admitted only from the holder or the take-over verb. Plant a cross-session mail and a forged tombstone, and state the limit openly. |
| FK-5-5 | w5 | "Declared edges (Recommended)" | Option A, as FK-5-5 lists it in w5's return. |
| FK-5-6 | w5 | "Cadence lease + CAS (Recommended)" | Option A, as FK-5-6 lists it in w5's return. |
| FK-6-2 | w6 | "Move to dPlacedRequest (Recommended)" | Option (a). Move `patch.ratify` to dPlacedRequest: v2 `[policies]`' owner cell, and the ownership record's rows (ownership:94 and :379). The probe's three `patch.ratify` lines must then clear. |

## Writing the fold

- **New clauses** end with a placeholder id, `` `cl-dClosedLoop-W7-<k>` `` for k = 1, 2, …, never a real number, and
  never an edit to `[clause-ids]`' next id. The main loop's mint step (`<scratch>/fold/mint.py`) numbers the
  placeholders after both writers' scripts. It updates every place that cites them, an `[enforcement]` row included.
- **Lines writer 8 also edits.** Writer 8 folds FK-4-1 to FK-4-13 (FK-4-12 merged with FK-5-2), FK-5-4 and FK-6-1. Its
  edits are mostly in flow-steps, in the recut table and in the v2 clauses those forks name: cl-0207, cl-0100,
  cl-0117, cl-0422, the `verdict.flakes` and `deps.on-parent-withdrawn` rows, and dKeptSession's and dFairHearing's
  rows.
  - Add a new row or bullet with `insert_before`, before a line neither of you rewrites. Two inserts before one anchor
    both apply.
  - Rewrite a line only when your own fork names it.
  - A line that both your fork and writer 8's need goes under *Requests*, with the exact change, and stays out of
    your script.
- **The revision log.** Add one "Revised 2026-10-20 by the whole-design audit's fork answers" paragraph to v2 for your
  forks, inserted before the line that opens "Revised: 2026-10-17, after the folds' closing review". Add a short note
  to any other record that keeps a revision log.
- **Register.** Write short declarative sentences in the records' own register. Use no new term where a defined one
  exists. Name a stand-in wherever a clause relies on a later build.

## Checking your script

You may dry-run the scripts on your own folder:

```sh
DRY_DIR=<scratch>/fold/w7/dry FOLD_ORDER="1 2 3 4 5 6 7 mint" bash <scratch>/stall/dry_run.sh <scratch>/fold/all.py
```

It ends `ALL rc 0` when the build's ten final checks pass. Without writer 8's script, the reconciliation probe still
shows `dFairHearing reads leases.offline`, which FK-6-1 resolves. Name any other red, and the fork that clears it. To
list every probe line, run this from the dry folder's root:

```sh
python -X utf8 memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md
```

## What you return

Your final message, nothing else:

1. **Dispositions,** one row per fork: `| fork | records · places | disposition | the fold's one-line gist, or what
   stops it |`. The disposition is `fold`, or `fork` when the answer needs a choice the owner did not make.
2. **Fold script:** `<scratch>/fold/w7/fold-7.py`, how many edits it makes in which records, and its placeholder
   ids.
3. **Forks,** each as `### FK-7-<k> — <question>`, then the options, your recommendation and the fork it rests on;
   or `none`.
4. **Requests** for lines writer 8 also edits, or `none`.
5. **The dry run:** its last line and any red check, or `not run`.
6. **Read outside the list above:** `none`, or what and why.
