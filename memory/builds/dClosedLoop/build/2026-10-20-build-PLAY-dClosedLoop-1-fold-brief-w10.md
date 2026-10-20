# Fold brief: writer 10, the closing pair's fold

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the closing pair's confirmed defects into dClosedLoop's design records, as one fold script.**
This brief is your instructions, not a spec to review.

## What you fold, and against what

- **Paths.** `<scratch>` is
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad`.
- **What to fold.** The comparison record is `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-audit-closing-reviews-compared.md`.
  - Its `[map]` places every finding of both runs on a defect.
  - Its `[fold]` table says where each defect folds and what changes. Each row there is your instruction.
  - The two reports hold each finding's evidence and its skeptic's corrected fix:
    `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-audit-closing-a.md` and `-b.md`.
- **The subject** is the design records in the working tree at `ef94fefba`, with two changes made since:
  - The recut record (`build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md`), as the main loop's Rule-column step
    leaves it, is in `<scratch>/closing/composite10/`. That step (`<scratch>/fold/rule_column.py`) did three things.
    It gave `[reconciled-order]` its Rule column, derived from the probe's own dependency lines. It split five rows that
    two rules need into one row per rule, each keeping its old class and reason. It dropped the two rows whose edges
    were prose stage words: dIndexedDesign `build.base` and dWitnessedBar `deploy.current`.
  - The main loop has already changed two build scripts in the working tree, so do not edit them:
    - **reconcile.py** keys class rows by (rule, build, node) and reads a key spelled `policy.<key>`. It counts a stage
      word as a route only after its branch's arrow. It reds a tolerance row whose reason says "today's tool" and
      names no backticked path that exists. Its docstring now says what rule 3 reads.
    - **stage0.py's K1** reads an Actor cell that opens "the role that owns" as one actor.
  - Every other record is unchanged, so read it in the working tree.
- **Read freely** in the working tree, the composite, the two reports, the comparison record and the scratch fold
  tools. Write only in `<scratch>/fold/w10/`. Nothing goes into the repository, and nothing is read from the sealed
  copy.

## The defects

Fold each of the comparison record's 21 `fold` rows as its `[fold]` row says, except the parts below that are the main
loop's. The main loop's parts take the disposition `main loop's`.

- **policy-prefix-unread, rule3-doc-overstates:** done in reconcile.py.
- **reconcile-key-no-rule:** the probe's code is done, and the Rule column is derived. Two parts are yours:
  - Word each split row's reason for its own rule, as the `[fold]` row says. The cites rows for dFairHearing
    `review.trigger` and `review.dispose` name cl-0070's stand-in. The cites rows for dDeclaredLoop `plan.exit`,
    `build.ratify` and `decisions.major` name cl-0104's owner-gate stand-in, as the owner's FK-9-1 has it.
  - Say in recut's prose that each row names its rule.
- **prose-stage-words-as-routes:** the probe's arrow rule is done, and the two rows are dropped. Reword the flow-steps
  prose cells the `[fold]` row names.
- **tolerance-rows-unnamed-tool:** the probe's check is done. Give every row it reds its real stand-in, as the
  `[fold]` row says, and make flow-steps' stand-in bullet say a command with no tool today is unarmed.
- **mailbox-answer-actor:** K1's reading is done. Make flow-steps `[rules]`' one-actor rule name the owning role.
- **stage0-red-unreported:** the round record's `[fold-applied]`, `[stage0]` and `[stage0-classes]`, and the
  instruments, are the main loop's.
  - Fix in the design records the reds the row names: `leases.overlap` and `kits.cadence` read by a clause or item,
    `runtime.attended-allowance`, and the unreached `adopt.declarations`, `adopt.instructions`, `kits.install-attended`
    and `kits.update-attended`.
  - Where a red cannot be fixed by a design edit, list it under *Requests* with its arm, its node and a class from that
    arm's closed set (stage0.py's `CLASSES`), and leave the classing to the main loop.

**The fork, answered.** For `flakes-measured-no-writer` the owner chose verbatim "dWitnessedBar derives it
(Recommended)", which is option (a):
- dWitnessedBar's gate-health clause cl-0339 derives the measured threshold by a rule the clause states, and writes it
  to the gate-health record;
- `test.flakes` reads it;
- a planted leg whose measured threshold differs from 2/10 is seen;
- v2:1253, layer-memory:584-585 and cl-0346 follow.

The owner's earlier answers stand, in the round record's `[fold]` and `[fold-applied]`. Fold none of them back.

## Writing the fold

- **New clauses** end with `` `cl-dClosedLoop-W10-<k>` ``. The main loop's mint step numbers them after your
  script.
- **Revision notes.**
  - In v2, add one paragraph, "Revised 2026-10-20 by the audit's closing pair's fold", with the defect slugs it closes,
    inserted before the line that opens "Revised: 2026-10-17, after the folds' closing review".
  - Add a short note to every other record you edit that keeps a revision log.
- **Register.** Write short declarative sentences in the records' own register. Name a stand-in wherever a clause relies
  on a later build.

## Checking your script

Run both checks:

```sh
DRY_DIR=<scratch>/fold/w10/dry FOLD_ORDER="rule_column 10 mint" bash <scratch>/stall/dry_run.sh <scratch>/fold/all.py
```

```sh
python -X utf8 memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-stage0.py
```

- The dry run must end `ALL rc 0`.
- Run Stage 0 from the dry folder's root after the dry run. Report its per-arm counts. The K1 cycle and the
  `mailbox.answer` reds should be gone.
- To list every probe line, run reconcile.py with the recut record from the dry folder's root, as the dry run's
  check does.
- See a planted row red: `--plant-why <build>:<node>=today's tool` on a route row you fixed.

## What you return

Your final message, nothing else:
1. **Dispositions,** one row per defect: `| defect | records · places | disposition | the fold's one-line gist |`.
2. **Fold script:** `<scratch>/fold/w10/fold-10.py`, how many edits it makes in which records, and any placeholder
   ids.
3. **Forks,** each `### FK-10-<k> — <question>`, with its options, your recommendation and the defect it rests on, or
   `none`.
4. **Requests:** the Stage 0 reds to class, each as arm, node, class and reason, or `none`.
5. **The dry run and Stage 0:** the dry run's last line and any red, Stage 0's per-arm counts, and the planted row's
   red.
6. **Read outside the list above:** `none`, or what and why.
