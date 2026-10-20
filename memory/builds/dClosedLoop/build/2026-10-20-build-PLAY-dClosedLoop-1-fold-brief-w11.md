# Fold brief: writer 11, Stage 0 again

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fix or class every lead Stage 0 reports on the folded tree, as one fold script and one classes
file.** This brief is your instructions, not a spec to review.

## What you work on

- **Paths.** `<scratch>` is
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad`.
- **The subject** is dClosedLoop's design records in the working tree at commit `15988ccd5`. The audit's fold and its
  closing pair's fold are both applied there.
- **The leads.** Run Stage 0 from the worktree root:
  `python -X utf8 memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-stage0.py`. At `15988ccd5` it
  reports 98 findings, with 7 classed:
  - **K2 (routes):** 21 findings. They are targets written in no declared form, `kits.*` items no entry reaches, and
    one item that ends nowhere.
  - **K3 (record kinds):** 76 findings. 37 have no writer item named, and many of those carry the marker "writer item
    not named". 39 have no reader: no item waits on the kind's writer or names it, and no other build's clause names
    it.
  - **K4 (keys):** 1 finding, `roles.shape-enforce`, read by no chain clause and no item.
- **How Stage 0 reads.** Its docstring and each arm's code say what a finding means and what each class admits. The
  closed sets are in its `CLASSES`:

  | Arm | Classes |
  |---|---|
  | K1 | prose need |
  | K2 | prose target, external entry |
  | K3 | program writer, hook writer, external writer, program reader, external reader |
  | K4 | planned, read through a system |

  The round record's `[stage0-classes]` (`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`) holds the seven
  rows classed so far. Read their form. You may not edit that record.

## How you dispose of each lead

- **fold:** the records already settle the answer. Examples: a kind's text names the item that writes it, a Then cell
  can be written in a declared target form, or a clause plainly reads the key. Write the smallest edit.
- **class:** the design keeps the lead by intent. Examples: a record a program or hook writes outside any flow item, a
  reader outside the loop, or an entry the owner starts. Pick the class from the arm's set. Give a reason the records
  state, with the place you read it.
- **fork:** closing it needs a choice the owner has not made. Name the question, the options and your recommendation.

Prefer a fold where the records settle it, and never class a lead only to silence it. Group leads of one kind by their
shared reason where that is honest. Each class row still names its own node.

## What you write

- **The fold script**, `<scratch>/fold/w11/fold-11.py`, using the build's fold library like every earlier fold:
  `sys.path.insert(0, "<scratch>/expansions")`, `from fold_lib import Record`. Each `sub` and `insert_before` matches
  exactly once.
  - New clauses end with `` `cl-dClosedLoop-W11-<k>` ``.
  - Add a revision note to every record you edit that keeps a revision log. v2's note goes before the line opening
    "Revised: 2026-10-17, after the folds' closing review".
- **The classes file**, `<scratch>/fold/w11/classes.md`: one row per class, `| K<n> | `<node>` | <class> | <reason> |`.
  The main loop's step `<scratch>/fold/stage0_classes.py` adds the rows to the round record. It refuses a class outside
  its arm's set and a repeated arm and node.

## Checking your work

Run the dry run, then Stage 0 from the dry folder's root:

```sh
DRY_DIR=<scratch>/fold/w11/dry FOLD_ORDER="11 stage0_classes mint" bash <scratch>/stall/dry_run.sh <scratch>/fold/all.py
```

```sh
python -X utf8 memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-stage0.py
```

- The dry run must end `ALL rc 0`.
- Stage 0 should report findings 0. Its two git-reading reruns red in a dry folder, which is not a repository; say so
  and leave them.
- A class row that no finding needs reds Stage 0 as well. That proves the row is not idle.

## What you return

Your final message, nothing else:
1. **Dispositions:** one row per finding, or per group sharing one disposition and one reason,
   `| arm | nodes | disposition | the fold's gist or the class and its reason |`.
2. **Fold script and classes file:** their paths, the edits by record, the class rows by arm and class, and any
   placeholder ids.
3. **Forks,** each `### FK-11-<k> — <question>`, with its options, your recommendation and the findings it rests on,
   or `none`.
4. **The dry run and Stage 0:** the dry run's last line, and Stage 0's per-arm counts and classed count.
5. **Read outside the list above:** `none`, or what and why.
