**Serves:** diff-review DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1

# Closing diff review — dSealedTally

Tier-2 · node `d` · 2026-09-04 · the cumulative diff landing on `main`, reviewed once at the
integration boundary rather than per unit.

**ROUND 2** over the cumulative range `3a1c0d6d1c28157ab480c8952ec7c46275dae1b4...HEAD`
(HEAD = `178dc739`), 1 commit, 12 files, +477/-21. That commit is the fold of round 1: the product
surface is `tools/govkit/govkit.py` (8 hunks) and `tools/govkit/selftest.py` (1 hunk); the rest is
`memory/map/generated/symbols.json` and this build's own records.

## Verdict: BLOCKED

One blocker, two highs, two mediums, one low. The blocker is not a new defect at all — it is round
1's F7, prescribed a fix, asserted folded in the fold commit's own message, and byte-unchanged in
the tree. The two highs are both the fold's own new code: an `index_read` added mid-write with no
`except Refusal`, at the third site this build has now closed that class at, and the landing
occupancy gate that F2 taught the rollback about but did not teach to refuse.

## Review shape

Raw 15 · confirmed 12 · refuted 3 · unverified 0 · precision 0.80. The 12 confirmed findings fold
into 5 distinct defects below: four finders converged independently on the unguarded `index_read`,
three on the rollback's landed reclassification, and two each on the disk-only landing gate and the
unnamed left-behind landing. Every one is reported once with the converging derivations kept.

The blocker (F1) is NOT one of those 12. It came out of the synthesis pass, from diffing the fold
commit against the round-1 report it claims to fold, and it was verified directly against the tree
rather than by a skeptic. It is marked as such where it stands.

## Findings

| # | Severity | Site | Defect |
|---|----------|------|--------|
| F1 | **blocker** | `tools/govkit/govkit.py:7418`, `:7424`, `:7434` | Round 1's F7 is unfolded — the three contradicting order-file statements are byte-unchanged, while the fold commit's message says otherwise |
| F2 | **high** | `tools/govkit/govkit.py:7146` | The new `index_read` is a third mid-write caller with no `except Refusal`; a raise aborts a part-written adopter tree with no receipt |
| F3 | **high** | `tools/govkit/govkit.py:7126` | The landing occupancy gate probes DISK only, so gov overwrites an adopter's staged blob on every run that is not rolled back |
| F4 | medium | `tools/govkit/govkit.py:7377` | The landed branch reclassifies a genuine restore as `removed`, because F2 falsified the premise it rests on |
| F5 | medium | `tools/govkit/govkit.py:7373` | `_left_landed` reaches `r.fail` only; the rollback order names that path in no line |
| F6 | low | `tools/govkit/govkit.py:3802` | The F5 comment rewrite left its other half standing, and the surviving half is false of the code beneath it |

Round 1's F1 (the stale generated map) is confirmed CLOSED: `python tools/codebase-map/gen_map.py
--check` exits 0 on this tree, and `symbols.json` gained the 15 lines the three new symbols owed.
Round 1's F9 is confirmed closed too — the anchored `[-ST5] AC5` arm at `selftest.py:5158` pins the
population at 4, and an anchored count over the suite returns exactly 4.

---

### F1 — blocker — round 1's F7 was declared folded and was not folded

`tools/govkit/govkit.py:7418` (the header sentence), `:7424` (the empty-case sentence), `:7434` (the
stdout summary).

The fold commit `178dc739` says, in its own body:

> F7 — three contradictions in the rollback order when the only rolled-back write was a landing:
> prose claiming everything was restored, an empty-case line announcing "nothing to restore", and
> stdout printing "(no path restored)".

`git diff 3a1c0d6d..HEAD -- tools/govkit/govkit.py` contains eight hunks, at lines 3802, 4595, 4828,
6370, 7119, 7161, 7189 and 7325. None of them reaches 7418-7434. The three statements round 1 asked
to be changed are byte-identical to the ones it reviewed.

The mechanism is unchanged and still fires on the ordinary path, not an exotic one. For a kit whose
only rolled-back write is a landing — which is exactly the shipping `[-ST1]` landkit fixture — the
`origin == "landed"` block at `:7366` moves every successfully removed path out of `restored` and
into `removed_landed`. `restored` is then empty by construction, so:

- `:7424` gates its fallback sentence on `not restored` alone. The order prints
  `removed   tools/landkit/arrival.txt` and, on the next line, *"(nothing to restore: every path
  this kit owns was refused before it was written)"* — a flat denial that the file above it was ever
  written.
- `:7418` asserts *"Every path below was restored to the index entry it had before the first byte
  moved, and this kit's receipt rows were restored with them"* above both lists, and it is false of
  a removed landing on both halves.
- `:7434` interpolates `restored` alone, so the console prints `ROLLED BACK · (no path restored)`
  for a run that wrote, staged and then unlinked a file in somebody else's repository.

This is the durable operator artifact for a rollback in a repository gov does not own, and its
closing paragraph asks the operator to resolve by hand from it. Round 1 rated it medium. It is a
blocker in round 2 for a different reason: the build's Definition of Done is that every confirmed
finding is left-shifted, the commit message states this one was, and the tree says it was not. A
record that claims a fold it did not perform is worse than the defect it describes, because the next
round has no reason to look.

**Fix.** Apply round 1's prescription verbatim; it is still correct. Gate `:7424` on
`not restored and not removed_landed` (and on F5's new list once it exists); split the `:7418`
sentence by disposition — restored paths went back to the index entry they had, removed paths were
minted by this run, had no prior entry, and their rows were deleted; and build the `:7434` summary
from `restored + removed_landed`, falling back to `(no path restored)` only when both are empty.

**Left-shift.** Two gates, and the second is the one that catches the class rather than the
instance.

1. A negative arm beside the `[-ST1]` assertions at `selftest.py:5599`: when `removed_landed` is
   non-empty, the order must NOT contain the substring `nothing to restore`, and stdout must NOT
   contain `(no path restored)`. The existing arms assert a line is PRESENT, which cannot see a
   contradicting line beside it — which is why this shipped green twice.
2. A fold-completeness check for the build method: a review record whose findings table names
   `file:line` sites must, at the fold commit, either have a diff hunk touching each named site or
   carry an explicit FILED row saying it does not. Round 1's F7 named three lines and the fold
   touched none of them. That is mechanically detectable, and nobody should have to read a commit
   message to see it.

---

### F2 — high — a third mid-write `index_read` with no handler, in the verb that writes into a foreign repo

`tools/govkit/govkit.py:7146`.

Four finders reached this independently and none of them was refuted.

```python
_idx_pre, _ = index_read(target, [_dest])
```

`index_read` raises `Refusal` whenever `git ls-files` exits non-zero over an in-tree path
(`:3839-3850`). Out-of-tree paths are filtered rather than raised on, so that filter does not
neutralise this: `_dest` is contained by the checks at `:7100-7116`, which puts it squarely in the
population that raises.

The call is unambiguously mid-write. It sits inside the landing loop, gated by
`if not write: continue` at `:7128`, and by the time control reaches it the row walk above has
already run `land_through_index`, `git mv` (`:6685`) and `git rm` (`:6847`), and earlier iterations
of this same loop have already `write_bytes`'d (`:7150`) and `git add`ed (`:7186`) their own
landings. The receipt is not written until `:7478`, `:7506` and `:7513`. `cmd_update`'s wrapper only
releases the lock, so an escape unwinds to `main`'s handler at `:8633`, which prints
`govkit: <msg>` and returns 2.

The result is gov-written bytes staged in the adopter's index that no receipt row names, so gov can
never withdraw them, and the run never reaches its own verify-and-rollback pass at `:7288`. That is
the half-install-with-no-receipt state this whole build is closing.

Two things make this worse than a missing `try`. First, the same commit closed this exact class at
two other sites — `:4605` and `:4843` in `_cmd_apply`, both carrying the comment *"MID-WRITE, so it
disposes rather than raises"*. Second, the sibling reader at `:6622` carries a comment that is now
false of the file it sits in:

> DEPL-dSealedTally-4. THE ONE MID-WRITE CALLER, and the only one that catches. Every other
> `index_read` runs before this verb has written anything.

**Fix.** Wrap it in the shape `:6622` already uses, and skip the row rather than defaulting
`_idx_pre` to `{}` — an empty map is the `absent` answer that later authorises the rollback to
`git rm --cached` the adopter's own blob.

```python
try:
    _idx_pre, _ = index_read(target, [_dest])
except Refusal as _land_idx_err:
    r.fail(f"could not read the index for the landing destination {_dest!r}, so its pre-write "
           f"state is UNKNOWN — not landing it rather than writing a path whose rollback could "
           f"not be recorded: {_land_idx_err}")
    continue
```

Nothing has been written for this row at that point, so refusing the row is both the stricter
disposal and the correct one. Then amend `:6620`, which now names a population of two.

**Left-shift.** Gate the class, not the call. Add an arm that walks `govkit.py`'s AST, finds every
`index_read` call inside the body of a function that also contains a `write_bytes`,
`git_pathspec(..., ["add"], ...)`, `git mv` or `git rm` call, and asserts each is lexically enclosed
by a `try` with an `except Refusal` handler. That is a short check and it pins all four sites at
once. A fixture-based arm would need a broken target index, which the suite manufactures for nothing
else and which the surrounding comments already admit it cannot stage.

---

### F3 — high — the landing gate asks the disk, so a staged blob in a foreign repo is silently replaced

`tools/govkit/govkit.py:7126`.

```python
if os.path.lexists(_abs0):
    _refused_new.append((_dest, "the target already holds this path and the receipt "
                                "does not name it, so gov did not put it there"))
    continue
```

Two finders, both high, neither refuted. The block's own heading two lines above is AC5: *"A
DESTINATION THE TARGET ALREADY HOLDS IS A REFUSAL, NEVER AN OVERWRITE."* `lexists` is a disk probe
and cannot see an index entry. A path the operator staged and then removed from the worktree — plain
`git add x; rm x`, or a skip-worktree or sparse path — is held by the adopter's index and invisible
here. The gate passes, `write_bytes` at `:7150` re-creates the file, `git add` at `:7186` replaces
the adopter's index entry with gov's blob, and a receipt row is minted claiming it. The adopter's
staged, uncommitted bytes become an unreachable object. Exit 0. The refusal text never prints.

Nothing upstream covers it. `demand_claimed_paths_clean` (`:4087`) is scoped to
`dirty_claimed_paths` over RECEIPT paths, and its own message says a dirty path outside the receipt
does not block. A landing destination is excluded from that population by construction, by the
`if _dest in _claimed_paths or _dest in _decided: continue` skip at `:7052`. `demand_index_resolved`
covers unmerged stages only.

The engine's own standard is both probes. The sibling rename gate at `:6628` reads the index AND the
disk — `if new_dest in _at_dest or ndp.exists()` — under a comment naming this exact state: *"a
tracked file there whose worktree copy the operator removed is invisible to `exists()`"*. The
read-only preview twin at `:6378` shares the single-probe form, so plan and write also disagree
about what "occupied" means.

What the fold did here is the finding. F2 read the index at `:7146` and taught the rollback to
restore that pre-state — conceding the state is real — instead of refusing the write that destroys
it. Rollback runs only on the `adopted -> landed-but-inert` transition, so on the ordinary green
path the loss is silent and permanent.

**Fix.** Hoist the `index_read` above the gate and make the gate index-aware, matching `:6628`. Take
the SECOND return value, not the stage-0 map, so an unmerged destination counts as held — its stages
1-3 are invisible to `_idx_pre.get(_dest)` and would otherwise be recorded `absent` and destroyed by
the rollback's `git rm --cached`.

```python
_idx_pre, _pre_present = index_read(target, [_dest])   # wrapped per F2
if _dest in _pre_present or os.path.lexists(_abs0):
    _refused_new.append((_dest, "the target already holds this path — in its index, its worktree "
                                "or both — and the receipt does not name it, so gov did not put "
                                "it there"))
    continue
```

Apply the same predicate at `:6378` so the read-only preview refuses what the write path refuses.

**Left-shift.** A `[-ST1]` arm that stages a file at a landing destination and then deletes it from
the worktree (`git add`, then `rm`), runs `update --write`, and asserts three things: the run refuses
that row, the refusal text names the path, and `git ls-files -s -- <dest>` still reports the
adopter's original oid. Add its twin on the read-only path asserting the preview refuses it too, so
the plan/write divergence is gated rather than remembered.

---

### F4 — medium — a genuine restore is reported as a removal

`tools/govkit/govkit.py:7377`.

Three finders. The `origin == "landed"` block reclassifies unconditionally.

```python
for _lp in [p for p in s["paths"] if p in restored]:
    while _lp in _landed_new:
        _landed_new.remove(_lp)
    restored.remove(_lp)
    removed_landed.append(_lp)
```

That was sound while `snap_rows` hardcoded `index: {_dest: None}`, and the declaration comment at
`:7300` still states the premise it rested on: *"A landed path had no index entry to restore."* F2
falsified it. With a real `(mode, oid)` in the snapshot, the per-path loop takes the
`entry is not None` arm at `:7340`, runs `update-index --cacheinfo` and `checkout-index -f`, and
appends to `restored` — the adopter's own blob is back in the index and back on disk. This block
then moves it into `removed_landed`, so the order at `:7423` prints `removed   <path>` for a file
that exists holding the adopter's bytes, and `:7434` omits it from the restored list.

The operator's only durable record of the rollback says gov deleted a file it restored, and they may
act on that by re-creating or re-staging over it. It compounds F1: if that landing is the kit's only
rolled-back path, `restored` is empty and the *"nothing to restore"* sentence fires on top of it.

The `[-ST1]` arms cannot catch this. Their fixture lands into a genuinely absent destination, and the
arm at `selftest.py:5601` asserts only that the path is NOT reported as `restored`.

**Fix.** Branch on the recorded pre-state rather than on `origin`. Keep the `_landed_new` removal and
the receipt-row drop unconditional — that row was minted by this run either way — and split only the
report bucket.

```python
if s["index"].get(_lp) is None:
    restored.remove(_lp)
    removed_landed.append(_lp)
# else: it WAS restored, to the adopter's own entry — leave it in `restored`
```

**Left-shift.** Extend the F3 fixture. Once F3 refuses that pre-state at the gate, the only way a
landed path carries a non-None snapshot entry is a bug, so assert it directly:
`s["index"][dest] is None` for every `origin == "landed"` snapshot row, checked through a debug dump
or an equivalent seam. If F3 is fixed and F4 is not, that arm reds. If F3 is deferred, the same arm
becomes F4's regression test by landing into a staged-no-worktree destination and asserting the order
says `restored`, never `removed`.

---

### F5 — medium — the left-behind landing is named in the failure and in no line of the order

`tools/govkit/govkit.py:7373`.

Two finders. `_left_landed` is computed, passed to `r.fail` at `:7379-7384`, and never reaches the
artifact.

```python
_left_landed = [p for p in s["paths"] if p not in restored]
```

The order body at `:7422-7429` renders `restored`, `removed_landed` and `untouched`. A landed path
that survives — refused by `demand_contained_dest` at `:7315`, or whose `git rm --cached`,
`update-index` or `checkout-index` failed — is in none of the three. It is in `written_paths`, so it
never reaches `untouched`; it never reached `restored`; and `removed_landed` is filled only from
paths that ARE in `restored`. So `.governance/outbox/update-rollback-<kit>.md` mentions it nowhere.

That is precisely the defect the branch's own comment at `:7370` names — *"named in no line of the
rollback order and withdrawable by nothing"*. The fold fixed withdrawability by keeping the receipt
row. It did not fix the naming, which is the half the operator reads.

`r.fail` accumulates into `Result.problems` and prints. It never reaches the outbox file the operator
opens later, and that file's closing paragraph is what asks them to resolve by hand.

**Fix.** Carry `_left_landed` out of the branch into a per-kit list beside the other three, render it,
and widen the empty-case guard F1 already has to fix.

```python
+ "".join(f"still staged {p} — gov wrote it, removal was REFUSED, and its receipt row is KEPT "
          f"so a later `update` can still see it\n" for p in still_staged)
```

Gate `:7424` on `not restored and not removed_landed and not still_staged`, and add the same term to
the stdout line at `:7434`.

**Left-shift.** The three plumbing failures under this branch are the ones the suite manufactures
none of, and the code says so where it stands. Rather than staging a broken index, gate the
reachable arm: plant a `../`-spelled dest in a snapshot row so `demand_contained_dest` refuses that
landed path, then assert the resulting order file contains that path in some line. One arm, one
refusal, and it covers the naming rule for all three branches — the class, not the instance.

---

### F6 — low — the amended comment left its other half standing

`tools/govkit/govkit.py:3802`.

The F5 rewrite replaced `.resolve()` / `relative_to` with a lexical test at `:3810-3816`, and added
the paragraph at `:3805-3809` explaining why. It did not touch the sentence above it, which still
reads:

> Filtered HERE so all callers inherit it, using the same resolve/relative_to idiom the
> rename-destination containment check already uses.

The code beneath calls neither `resolve()` nor `relative_to()`. It is `os.path.normpath` plus
`isabs` and `..` / `../` prefix tests. One doc block now returns two verdicts on how the filter
works, and the false half is the one attached to the load-bearing *"Filtered HERE so all callers
inherit it"* rationale — the sentence a reader extending the filter would take as licence to resolve,
which is the belief F5 exists to kill. This is the `amendment-leaves-its-other-half-standing` class,
one of the four anchored for this diff.

**Fix.** Collapse it to the surviving rule and drop the idiom clause. The F5 paragraph below already
carries the why.

```
# Filtered HERE so all callers inherit it. A filtered path is simply left out of both return
# values, which is what "absent" means to every caller.
```

**Left-shift.** Not gateable as prose, so it joins the recurring-class checklist the Tier-2 protocol
already runs, in this concrete form: when a fix rewrites a mechanism, grep the enclosing comment
block for the OLD mechanism's vocabulary — here `resolve` and `relative_to` — before calling the hunk
done. `python tools/memory-tree/gotchas.py --for-diff <base>..<head>` is where that check is written
down for the next diff.

---

## What is not a finding

Three refuted, dropped, and named so the next round does not re-derive them.

- The F6 receipt-row pop at `:7192` was read as able to remove another row. It is guarded on
  `receipt["files"][-1].get("path") == _dest`, so it can only ever remove the row it just minted.
- The F4 `_idx = {}` fallback in `_cmd_apply` was read as re-opening the false-absent. It only skips
  the `oid` stamp for that pass, and `r.fail` has already made the run report a problem.
- The `_dest` containment checks at `:7100-7116` were read as insufficient against pathspec magic.
  They are not the containment story for `index_read`'s raise; that path is F2's, and it is filed as
  such.

## Round shape

Round 1 confirmed 13 of 16 raw at precision 0.81. Round 2 confirmed 12 of 15 at 0.80 over a diff one
tenth the size, and its single most valuable finding came from the synthesis pass rather than from
the fan — diffing the fold against the report it claimed to fold. That is worth carrying: after a
fold commit, the cheapest high-yield check is not another lens over the code, it is a hunk-by-hunk
reconciliation of the fold against the previous round's site list.
