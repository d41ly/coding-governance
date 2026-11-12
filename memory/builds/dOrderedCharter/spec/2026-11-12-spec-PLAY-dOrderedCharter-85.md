# PLAY-dOrderedCharter-85 — the prepare folds gov first's walk into the merge before it regenerates

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-2 · base 5177028b6 · streams tooling · order 46 · advances PLAY-dOrderedCharter-38 · ratified 2026-11-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 PLAY-dOrderedCharter-84 PLAY-dOrderedCharter-86 |
| [2026-11-12-build-PLAY-dOrderedCharter-85-1-builder-return.md](../build/2026-11-12-build-PLAY-dOrderedCharter-85-1-builder-return.md) | journal | — |
| [2026-11-12-build-PLAY-dOrderedCharter-85-ledger.md](../build/2026-11-12-build-PLAY-dOrderedCharter-85-ledger.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-85-build-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-85-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The lander's `--prepare` runs the upgrade steps and then regenerates over their uncommitted output.
The policy mirror renders only a committed revision, so any pending step that writes the
instruction overlay stops every lander, attended or not. This run held on exactly that. This unit
makes `--prepare` fold what gov first's walk wrote into the prepared merge before it regenerates,
the order the attended landing already keeps.

## 2. Scope (IN)

- **S1** — `tools/push-main.sh` gains `write_merge_fold`. It rewrites the detached prepared merge
  over the working tree, with the same parents and message, when the tree differs from HEAD.
  `cmd_prepare` calls it once after `run_gov_first` and before `run_regen`, and once after
  `run_regen` where its inline fold block stands today. A failed fold after the walk refuses the
  prepare by the walk's own exit shape (section 4, "The fold"). Observed by AC1 and AC2.
- **S2** — `tools/push-main.test.sh` gains arm 41. Its branch commits a planted upgrade step that
  passes and a `regen.py` that exits 1 on any uncommitted change. The arm asserts that `--prepare`
  exits 0 with one merge onto the advertised tip, a clean tree, and a receipt that records the
  planted step (section 4, "The arm"). NOT OBSERVED by a criterion: an acceptance command may not
  run a suite. It is declared on section 7's `New arm:` line, where the main loop observes it red
  at the base and green at the close.

## 3. Non-goals (OUT)

- The policy guard's run admission. That is the sibling unit PLAY-dOrderedCharter-84, at the same
  order. Neither unit reads or writes the other's files, and they can land in either order. This
  run's landing needs both.
- The attended landing. It already commits gov first's walk before it regenerates
  (`tools/push-main.sh@efee7864:1333-1341`), so it is left as it is.
- Any change to the mint, the walk, the regeneration, the snapshot and its cleaning, the merge-loss
  check or the compare-and-swap.
- A refusal at `--prepare` for a step that writes a guarded file. The owner's ruling makes no file
  owner-only to a run (section 4, "Alternatives rejected").
- A bump of the lander's kit version. Kit versions are minted at the landing
  (`tools/push-main.sh@efee7864:26-29`).
- A count floor or a ceiling move for `push-main self-test`.

### Edges

- **consumes-from** external — PLAY-dOrderedCharter-31's upgrade step
  `playbook/adopter-rules-to-overlay`, CLOSED. AC2 observes this run's prepare fold that step's
  output. Arm 41 plants its own step and needs none.

## 4. Design

### Evidence

Read at `5177028b6`.

- The hold: `--prepare` applied `playbook/adopter-rules-to-overlay`, and then `regen.py --write`
  stopped at the policy mirror
  (`memory/builds/dOrderedCharter/build/2026-11-12-build-PLAY-dOrderedCharter-1-owner-landing.md`).
  `policy.py mirror --write` refuses while any input it records differs in the working tree from
  its blob at HEAD (`tools/policy/policy.py@aef77389:1459-1463`). The overlay
  `.governance/instructions.toml` is one of those inputs (`tools/policy/policy.py@aef77389:67`,
  `tools/policy/policy.py@aef77389:859`).
- `cmd_prepare` runs the mint, then `run_gov_first`, then `run_regen` over one uncommitted tree. It
  folds all three into the merge only at the end (`tools/push-main.sh@efee7864:1104-1148`). The
  attended landing commits gov first's walk before it regenerates
  (`tools/push-main.sh@efee7864:1333-1341`). That is the order the prepare lacks.
- The prepare's fold is `git commit-tree` over the detached merge, chosen so that no pre-commit hook
  fires (`tools/push-main.sh@efee7864:1098-1103`). An extra fold therefore meets no policy guard.
- The fold block is one inline instance today (`tools/push-main.sh@efee7864:1140-1148`). This unit
  adds the second.
- Arms 34 and 36 already build a clone of the repository with `build_regen_fixture`, plant a step
  row in the deployer's `steps.toml`, and commit a `regen.py` that exits 1 on the branch
  (`tools/push-main.test.sh@ad8503b9:1248-1320`).
- This run's receipt `.governance/install.json` records the step id
  `playbook/adopter-rules-to-overlay` 0 times at `5177028b6` (PINNED, `grep -c`).

### The fold (S1)

```bash
write_merge_fold() {  # first parent · second parent · message -> 0 HEAD is the merge over the tree, or the tree was HEAD's · 1 the commit or the ref move failed
```

When `git status --porcelain --ignore-submodules=untracked` prints nothing, the function returns 0.
Otherwise it runs `git add -A`, sets the global `t` to `git commit-tree "$(git write-tree)" -p <first> -p <second> -m <message>`,
and runs `git update-ref --no-deref HEAD "$t"`. This is the current inline block lifted as it
stands. Its second instance is the reason to extract it.

In `cmd_prepare`, after `run_gov_first` passes and before `run_regen`:

```bash
  if ! write_merge_fold "$R" "$oldb" "$msg"; then
    git reset -q --hard HEAD >/dev/null 2>&1 || true
    remove_new_untracked "$gfsnap"; rm -f "$gfsnap"
    git checkout "$branch" >/dev/null 2>&1 || true
    echo "push-main: could not fold the upgrade steps' output into the merge before the regeneration. Nothing was changed: '$branch' is still ${oldb:0:8} and is checked out." >&2
    return 1
  fi
```

The final block becomes the same call with its existing message and reset. After the first fold,
`t` is the folded merge. The regeneration's refusal then resets to it, and `git checkout "$branch"`
returns the tree to `oldb`. A file the walk created is tracked in `t` and absent in `oldb`, so the
checkout takes it away. `remove_new_untracked` cleans the rest against the snapshot taken before the
walk, as today. The idempotency check, the merge-loss check and the compare-and-swap read only the
final `t`, whose parents are still `R` and `oldb`. The header paragraph at
`tools/push-main.sh@efee7864:36-39` gains the sentence "gov first's walk is folded before the
regeneration, so a generator reading HEAD sees it committed".

### The arm (S2)

Arm 41 runs where arm 36 runs: `_mt_gk`, `_rg_k` and `_py_arms` all resolve, with the same skip line
otherwise. Over `build_regen_fixture`, the branch `feat` commits two things. The first is a
`[[upgrade]]` row appended to the deployer's `steps.toml`, id `govkit/planted-fold`, whose up, down
and witness are each `python -c pass`. The second is a `regen.py` that prints
`git status --porcelain` to stderr and exits 1 when it is not empty, else exits 0. That stub models
the mirror's refusal of an uncommitted input. The arm runs `--prepare` and asserts:

- the exit is 0;
- `HEAD^1` is the advertised tip and `HEAD^2` is `feat`'s tip, so there is one merge;
- `git status --porcelain` is empty;
- `git show HEAD:.governance/install.json` records `govkit/planted-fold`.

At the base the walk writes the receipt row, the stub sees it uncommitted, and the prepare exits 1
naming `could NOT be regenerated`. That is the failing case.

### What it does not check

- A generator that reads the working tree, not HEAD, regenerated correctly before this unit and
  still does. The fold changes only what HEAD holds when the regeneration starts.
- The fold also carries the mint's output, which precedes the walk. It is folded one stage earlier
  than before, and the final tree is the same.
- Arm 41's stub models the mirror's refusal. It does not run `policy.py`. AC2 is the observation
  over the real mirror.
- No hook judges either fold, as before.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| `write_merge_fold` | `tools/push-main.sh` | `sh.function`, `OK` by `--suggest` at design |
| arm 41, `govkit/planted-fold` | `tools/push-main.test.sh` | no cell grades an arm number or a step id |

### Files touched (estimate)

- `tools/push-main.sh` (S1)
- `tools/push-main.test.sh` (S2)

### Alternatives rejected

- **Refusing at `--prepare` any step that writes a guarded file, naming the owner's remedy.** This was
  the hold record's other option. The ruling makes no file owner-only to a run, so the refusal would
  name a remedy that no longer applies.
- **Folding only the paths the walk names.** It needs a list of what the walk wrote, which the
  deployer does not hand back. The existing fold already takes the whole tree.
- **Regenerating before the walk.** The regeneration must render the steps' outputs, which is why
  the walk comes first today.

## 5. Production-readiness checklist

- security — No guard, grant or hook changes. The fold is the existing `commit-tree` rewrite, run
  once more.
- perf / scale — The prepare gains at most one `commit-tree` and one `update-ref`.
- error / empty / loading states — A failed fold refuses the prepare with the branch unmoved and no
  file of the walk left behind. A walk that wrote nothing folds nothing.
- observability — The new refusal names its stage.
- risks — A generator that reads HEAD now sees the mint's and the walk's output one stage earlier,
  which is the intent. Arm 41 and AC2 observe the order.
- testing — AC1 is a direct probe, and AC2 is the run's own prepare. Arm 41 is declared in section 7,
  and the main loop observes it red at the base and green at the close.
- migration — N/A: no schema, record shape or conf key moves.
- user docs — N/A: no help page describes the prepare's internal order, and the flags do not change.

## 6. Acceptance criteria

- **AC1** — When `grep -n -e "run_gov_first" -e "write_merge_fold" -e "run_regen" tools/push-main.sh`
  runs after the build, the lines inside `cmd_prepare` read in this order: `run_gov_first`, then
  `write_merge_fold`, then `run_regen`, then `write_merge_fold`.
  Red when: the prepare regenerates before it folds the walk, so a generator that reads HEAD meets
  the walk's output uncommitted.
- **AC2** — When the main loop runs `bash tools/push-main.sh --prepare --slug dOrderedCharter` on this
  run's branch after the build, it exits 0 and prints `push-main: prepared`. Then
  `git grep -c "playbook/adopter-rules-to-overlay" HEAD -- .governance/install.json` prints a count
  of at least 1, and `git ls-tree --name-only HEAD .governance/` lists the instruction overlay.
  Red when: the regeneration refuses at the policy mirror because the step's output is still
  uncommitted.
  figure: PINNED, the receipt's count of 0 for that step id at `5177028b6`.
  permission: the main loop runs the lander. It moves the run branch.

## 7. Gates

`push-main self-test` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

Every leg the estimate's two paths trip has a broad guard (DERIVED by the spec-token checker's
`--legs-for` at `5177028b6`), so no leg is owed by the guard join. `push-main self-test` holds arm
41. `lexicon naming predicates` grades `write_merge_fold`. The suite's ceiling of 580 stands
(`tools/gate-legs.json@83fb3a5f`). Arm 41 adds one prepare over one clone, as arm 36 does, and is
not re-measured by this spec.

New arm: tools/push-main.test.sh · covers AC1 · arm 41: the base lander regenerates before it folds, so the branch's `regen.py` meets the walk's receipt uncommitted and the prepare exits 1 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-12 · split out of PLAY-dOrderedCharter-84 by its F1, resolved under the owner's
  standing fork picks and ratified 2026-11-12. S1 and S2 were that spec's rev-1 S4 and S5. AC1 was
  its AC5, and AC2 its AC7, which no longer waits on that unit's commit. The arm and its failing
  case are unchanged. Grounded at `5177028b6`.

## 10. Reuse audit

Seams extended: `cmd_prepare`'s own inline fold, extracted at its second instance
(`tools/push-main.sh@efee7864:1140-1148`); the attended landing's order, which commits the walk
before the regeneration (`tools/push-main.sh@efee7864:1333-1341`); and arms 34 and 36's
`build_regen_fixture` and planted step row (`tools/push-main.test.sh@ad8503b9:1248-1320`).
`tools/codebase-map/reuse_lookup.py` ranked the generic stems `commit`, `merge` and `tree`, and
`write_commit` in other kits, none of which rewrites a prepared merge. No other seam fits.

Recall terms used: `reuse_lookup.py "fold the working tree into the prepared merge commit-tree before the regeneration"`
