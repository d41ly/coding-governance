# Fold brief: writer 6, the requests and the reconciliation rows

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the five fold writers' requests and to resolve the reconciliation probe's nine new findings,
as one fold script that runs after theirs.** This brief is your instructions, not a spec to review.

## What you fold, and against what

- **The subject is dClosedLoop's design records as the five writers' scripts leave them.** The scripts are
  `<scratch>/fold/w<n>/fold-<n>.py` for n from 1 to 5, where `<scratch>` is
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad`.
  They apply to the working tree at commit `e7b58e2ee`. Read them, but never edit them.
- **The folded copies of the seven records they change** are in `<scratch>/fold/composite/`: architecture-v2,
  flow, flow-steps, layer-memory, layer-runtime, layer-expansions and fates. Every other record is unchanged, so read
  it in the working tree. Your script runs after the five, so every `sub` and `insert_before` must match the
  composite's text exactly once, or the working tree's for a record the composite does not hold.
- **The main loop amended the five scripts twice.**
  - fold-2's place 68 no longer ranks a fork "under `design.forks`' default", because dBoundRoles does not descend
    from dIndexedDesign.
  - The states are named `incomplete` (the terminal) and `parked` (the hold) in both fold-1 and fold-4.
- **Your records:**
  - every design record a request names;
  - the recut record's `[reconciled-order]` class table (`build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md`);
  - v2's revision log and its `[clause-ids]`.
- **Read freely** in the working tree, the composite and the five scripts. Write only in `<scratch>/fold/w6/`. Nothing
  goes into the repository, and nothing is read from the sealed copy.

## The requests

Each of the five saved returns lists its requests under `## 4. Requests`. They are in
`memory/builds/dClosedLoop/build/`:

- `2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w1.md`, R1 to R5.
- `2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w2.md`, 1 to 3.
- `2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w3.md`, R-1 to R-10.
- `2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w4.md`, its seven record-level bullets and their sub-items.
- `2026-10-20-build-PLAY-dClosedLoop-1-fold-return-w5.md`, its three bullets.

Number your items `w<n>-<its label>` in the returns' order. The main loop has seen these overlaps between requests and
other writers' folds. Verify each one against the composite, and look for any others.

- **w1 R1** asks for `[transitions]` rows for the incomplete terminal and the owner park. It meets w4's place 15,
  which added the `parked` state and the terminal. Fold only what w4's rows leave out.
- **w1 R5** is the round record's own `[stage0-classes]`. Its disposition is `main loop's`, taken at the next Stage 0.
- **w3 R-8** asks for flow-steps `[adopt]` rows. It meets w4's place 114, which added `adopt.instructions` and
  `adopt.declarations`.
- **w4's requests on cl-0383, cl-0384, cl-0422 and cl-0423** meet w3's folds of the same clauses (places 95, 100 and
  101). Merge each pair into one text per clause. For cl-0422, fold the per-value arms. Leave the cross-node landing
  turn to the owner's fork FK-4-7, which the owner is answering now.
- **w4's `maintain.patch` request** meets w5's place 32 fold of the same row.
- **w5's flow-steps request** on `entry.claim`, `plan.dedupe` and the `[transitions]` patch row meets w4's place 23
  fold of `entry.claim`.
- **w4's layer-roles counts** say "81 items … 20 items with a role" becomes "88 … 24". Derive both numbers from the
  composite's flow-steps item tables, write what you count, and say how you counted.
- **Minting.** fold-3 mints 0497 to 0499 and sets `[clause-ids]`' next id to `cl-dClosedLoop-0500`.
  - Mint from 0500 in your items' order: w3's R-4, w4's dPlacedRequest clause, w5's dConvergedCharter clause, and any
    other request that adds a clause.
  - Set the next id past your last.
- **The revision log.** w1 and w3 each add a "Revised 2026-10-20" paragraph above the 2026-10-17 line.
  - Add w2's paragraph (its request 1) between theirs.
  - Add one paragraph for your own pass, in the same register.
- **A request that rests on an owner fork** is `fork`, naming the fork. The forks are FK-1-1 to FK-1-7, FK-2-1 to
  FK-2-4, FK-3-1 to FK-3-3, FK-4-1 to FK-4-13 and FK-5-1 to FK-5-6 in the five returns. Fold the part that does not
  rest on it.

## The reconciliation probe's findings

After fold-1 to fold-5, the probe reports nine dependencies on a node owned by a build that is not an ancestor, each
with no class row:

```text
dFairHearing cites `review.dispose` (dDeclaredLoop's, not an ancestor): UNCLASSED
dKeptSession cites `memory.map-purpose` (dTotalRecall's, not an ancestor): UNCLASSED
dTrueNorth cites `deviation.approval` (dDeclaredLoop's, not an ancestor): UNCLASSED
dFairHearing reads `leases.offline` (dPlacedRequest's, not an ancestor): UNCLASSED
dPlacedRequest reads `build.unit-holders` (dWellOiledMachine's, not an ancestor): UNCLASSED
dPlacedRequest reads `kickoff.runs` (dRankedPlan's, not an ancestor): UNCLASSED
dPlacedRequest reads `patch.ratify` (dTendedCadence's, not an ancestor): UNCLASSED
dPlacedRequest reads `run.on-owner-question` (dBoundRoles's, not an ancestor): UNCLASSED
dShippedRelease reads `patch.ratify` (dTendedCadence's, not an ancestor): UNCLASSED
```

Number them `probe-1` to `probe-9` in this order. Resolve each one in one of three ways:

- **Class it** in recut's `[reconciled-order]` table, in the shape of the table's existing rows (`| Row | Node | Owner |
  Class | Why |`). The class is one of tolerance, homonym, not a use and moved. A tolerance's reason names the stand-in
  the citing build runs until the owner lands, as the folded text or the item's interim bullet says.
- **Reword** the folded text, where it names a key it never needs.
- **Raise a fork,** where the design settles no stand-in.

The owner's fork FK-4-9 asks where the stand-ins for routes into later builds are declared. Its recommendation keeps
tolerance rows in this table. Class these nine dependencies by the table's existing practice either way.

## Checking your script

You may dry-run all six scripts on your own folder:

```sh
DRY_DIR=<scratch>/fold/w6/dry FOLD_ORDER="1 2 3 4 5 6" bash <scratch>/stall/dry_run.sh <scratch>/fold/all.py
```

It copies the worktree into that folder, runs the six scripts there, then runs the build's ten final checks. It ends
`ALL rc 0` when all of them pass. The output shows only the last six lines of each check. To list every probe line,
run `python -X utf8 memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-reconcile.py
memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-recut.md` from the dry folder's root.

## What you return

Your final message, nothing else:

1. **Dispositions,** one row per item: `| item | record · place | disposition | evidence or the fold's one-line gist |`.
   A `duplicate` names the fold that already carries it.
2. **Fold script:** `<scratch>/fold/w6/fold-6.py`, and how many edits it makes in which records.
3. **Forks,** each `### FK-6-<k> — <question>`, then its options, your recommendation and the item it rests on.
4. **The dry run:** its last line and any red check, or `not run`.
5. **Read outside the list above:** `none`, or what and why.
