**Serves:** diff-review DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1

# Closing diff review — dSealedTally

Tier-2 · node `d` · 2026-09-04 · the cumulative diff landing on `main`, reviewed once at the
integration boundary rather than per unit.

**ROUND 1** over the cumulative range `4fd318320cd4d17dcc543d38eb6dceb7b2d5cbf8...HEAD`
(HEAD = `3a1c0d6d`), 12 commits, 24 files, +3792/-409. The product surface is
`tools/govkit/govkit.py`, `tools/govkit/selftest.py` and `tools/unattended/unattended.sh`;
everything else in the range is records.

## Verdict: BLOCKED

One blocker and two highs. The blocker is mechanical and costs one command: the merge bar is RED on
this diff because three new module-level symbols never reached the generated codebase-map inventory.
The two highs are both in the new landed-source rollback path, and both end in the same place — an
adopter's repository, which gov does not own, holding either a destroyed index entry or a
gov-written file no receipt names. Four mediums and two lows follow.

## Review shape

Raw 16 · confirmed 13 · refuted 3 · unverified 0 · precision 0.81. The 13 confirmed findings fold
into the 9 distinct defects below: two pairs of finders converged on the same site independently
(the unconditional receipt-row drop, and the rollback order's self-contradiction), and those are
reported once each with both derivations kept. Nothing was dropped in the fold, and no finding is
carried forward unverified.

## Findings

| # | Severity | Site | Defect |
|---|----------|------|--------|
| F1 | **blocker** | `tools/govkit/govkit.py:3487` (+ `selftest.py:85`, `:113`) | Three new symbols missing from `memory/map/generated/symbols.json` — the map freshness leg is RED |
| F2 | **high** | `tools/govkit/govkit.py:7193` | Landed-source snapshot hardcodes `index: {dest: None}` from a disk-only probe; rollback destroys an adopter's staged blob |
| F3 | **high** | `tools/govkit/govkit.py:7327` | The landed-rollback branch drops the receipt row even when the path's own removal was refused or failed |
| F4 | medium | `tools/govkit/govkit.py:4598`, `:4831` | `index_read` now raises; two mid-write callers in `_cmd_apply` have no handler, re-opening the no-receipt half-install |
| F5 | medium | `tools/govkit/govkit.py:3805` | The out-of-tree filter uses `.resolve()`, so a tracked symlink pointing outside the tree is reported ABSENT from the index |
| F6 | medium | `tools/govkit/govkit.py:7136` | The landed receipt row is minted before `git add`, and the stage-failure branch unlinks the file without removing the row |
| F7 | medium | `tools/govkit/govkit.py:7366`, `:7372`, `:7382` | The rollback order and its stdout line contradict themselves when the only rolled-back write was a landing |
| F8 | low | `tools/govkit/govkit.py:6374` | `derive_unclaimed_candidates` returns a third tuple element nothing reads, under a comment claiming it saves a second resolve |
| F9 | low | `tools/govkit/selftest.py:132` | A prose count of "Eleven" call sites contradicts the guard added in the same diff, which pins the population at 4 |

---

### F1 — blocker — the generated codebase-map inventory no longer describes the tree

`tools/govkit/govkit.py:3487` (`paths_never_lost`), `tools/govkit/selftest.py:85`
(`resolve_gov_pin`), `tools/govkit/selftest.py:113` (`repin_receipt`).

Three module-level symbols land in this diff and none of them is in
`memory/map/generated/symbols.json` — `grep -c` returns 0 for all three. The merge-bar leg
`codebase-map coverage + freshness` is therefore RED. Measured on this worktree:

```
ok   test_every_inventory_key_is_claimed_or_baselined
ok   test_dossier_prose_headings_pinned
ok   test_dossier_affordance_present_or_graced
ok   test_path_derived_keys_are_posix
FAIL test_generated_artifacts_are_fresh
STALE symbols.json — regen: python tools/codebase-map/gen_map.py --write
```

The leg carries no `guard` key in `tools/gate-legs.json`, so it runs on every bar and reds every
push of this range. Until it is regenerated the map's own ratchet cannot see the new keys at all,
which is the coverage half of the same leg silently not doing its job.

**Fix.** Run `python tools/codebase-map/gen_map.py --write` and commit the regenerated
`memory/map/generated/symbols.json` in the same commit. Verified: after the regen all five map arms
go green, and no dossier or baseline edit is required.

**Left-shift.** The leg already exists and already reds; what failed is that it was never run before
the closing review. Add the freshness check to the tracked pre-commit fast leg, guarded to commits
touching `tools/**/*.py`, so a stale generated artifact is refused at the commit that causes it
rather than at the push boundary several commits later.

---

### F2 — high — the landed-source snapshot asserts an index state it never asked about

`tools/govkit/govkit.py:7193`, with the disk probe it rests on at `:7106`.

The landing block's only occupancy guard is `os.path.lexists(_abs0)`. That proves the WORKTREE file
is absent and nothing else. A path that is tracked in the adopter's index but whose worktree copy the
operator deleted with a plain `rm` passes the gate, so gov writes its own bytes there and `git add`s
over the existing index entry — already a violation of the block's own stated rule that a
destination the target holds is a refusal.

The snapshot minted immediately after then hardcodes `"index": {_dest: None}` under a comment
asserting that `absent` "is not an assumption, it is the condition that made the landing legal".
When that kit's check reds, the restore loop reads the `None`, takes the `entry is None` arm, and
runs `git rm --cached` followed by `unlink`. The adopter's index entry is removed rather than
restored. If the entry was staged-only — added, never committed — the blob is unreachable and
permanently lost; if it was HEAD's, the adopter is left holding a staged deletion it did not make.

The strongest evidence is internal to the same file. The rename branch at `:6591` asks both the index
(`index_read`) and the disk (`ndp.exists()`), and its comment states the exact reason: a tracked file
whose worktree copy the operator removed is invisible to `exists()`. The single `git ls-files` in the
landing block runs at `:7175`, after the write and after the `git add`, purely to fill `oid`.
Reproduced on a scratch repo: `git ls-files -s` reports both a tracked `keep.txt` and a staged-only
`staged.txt` while `os.path.lexists` answers False for both after a plain `rm`.

**Fix.** Ask the index as well as the disk at the landing gate, exactly as the rename branch does.
Put `_, _at_land = index_read(target, [_dest])` beside the `lexists` check at `:7106` and refuse the
landing when `_dest in _at_land`. Only then is `index: {_dest: None}` a proved fact. If refusing is
too strict, record the real entry (`_at_land.get(_dest)`) in the snapshot so the restore loop takes
the `update-index`/`checkout-index` arm and puts the adopter's blob back.

**Left-shift.** Two arms, one instance and one class. The instance: extend the landkit fixture so the
destination is `git add`ed and then `rm`ed from the worktree before the update run, and assert the
landing refuses rather than writing. The class: a source-scan leg over `tools/govkit/govkit.py`
refusing any snapshot literal that mints `"index"` with a `None` value unless an `index_read` call
appears in the same block — a disk probe may never author an index claim.

---

### F3 — high — a receipt row is dropped even when its file could not be removed

`tools/govkit/govkit.py:7327`, reached from the failure arms at `:7279` and `:7296`.

Two finders arrived here independently. Both `continue`s in the path loop — the
`demand_contained_dest` refusal and the `git rm --cached` failure — exit the inner `for p in
s["paths"]` loop, leaving the landed file on disk AND staged in the adopter's index. The
`if s.get("origin") == "landed":` block sits OUTSIDE that loop, so it removes the row from
`receipt["files"]` and strips the path from `_landed_new` regardless of whether anything was undone.

The consequences compound. The receipt written at `:7426` names no row for a gov-written file that is
still tracked in the adopter's repository. `install.sums` is rebuilt from `receipt["files"]` and
omits it. The closing `unclaimed sources:` tally no longer reports it. Because the path never entered
`restored` it is never moved into `removed_landed` either, and landed paths are in `written_paths`
(`:7198`) so they never reach `untouched` — the path is named in NO line of
`update-rollback-<eid>.md`, directly contradicting the failure arms' own instruction to "say so
rather than reporting a rollback that did not happen". No later `update` can withdraw it, because
withdrawal walks receipt rows.

The containment arm is reachable without any git failure at all. The landing gate at `:7095` tests
containment with `resolve()`; the rollback tests it with `demand_contained_dest`'s string rule.
`resolve_entry` never calls `demand_contained_dest`, so these are genuinely two different rules and a
destination can satisfy one and be refused by the other. The finder's example (`a:b/x.txt`) is
refused by both on Windows, where pathlib swaps the drive and `relative_to` raises, but diverges on
POSIX; a `prefix` like `a:/x` passes `demand_safe_token`'s drive-prefix carve-out. That cross-OS
shape matters in a repo whose whole premise is one tree across Windows and non-Windows nodes.

One correction to the finders, kept for accuracy: `Report.fail` accumulates and `emit` prints every
problem, so the path IS named in the run's failure output. It is absent from the order file and from
every tally, not from the run entirely.

**Fix.** Track per-path removal success inside the path loop and only `receipt["files"].remove(...)`
and strip `_landed_new` for paths that actually reached `restored`. For the rest, keep the row and
emit an explicit `NOT removed` line in the order beside the existing `r.fail`, so a landing that
could not be undone stays visible to the next run instead of becoming an orphaned staged file.

**Left-shift.** A partition assertion, which gates the class rather than the instance: for every
rolled-back kit, assert that each path in that kit's `snap_rows` appears in exactly one line of
`update-rollback-<eid>.md` — `restored`, `removed`, `left alone`, or a new `NOT removed`. That single
arm catches this defect, F7's contradiction, and every future variant where a path falls between the
lists. Add a forced-failure arm that makes the unstage red (a read-only index, or a fixture path the
rollback containment rule refuses) and assert the receipt row survives.

---

### F4 — medium — `index_read`'s new refusal reaches two mid-write callers in `_cmd_apply`

`tools/govkit/govkit.py:4598` and `:4831`.

The new liveness assertion makes `index_read` raise `Refusal` on a non-zero `git ls-files`. The diff
added a `try/except Refusal` at exactly one call site, `:6602` in `_cmd_update`, justified by the
comment at `:6598`: "Every other `index_read` runs before this verb has written anything, so letting
the refusal reach the verb boundary costs nothing there."

That is true of `_cmd_update`, whose other calls at `:5918` and `:6470` are both preamble. It is
false of `_cmd_apply`. Both of its calls sit after `git_pathspec(target, ["add"], staged)` at `:4590`
and before `receipt_path.write_text` at `:5131`. A non-zero `git ls-files` there — an unreadable
index, a destination git parses as pathspec magic, a contended index state — propagates to the
top-level handler at `:8581` and exits 2, leaving the adopter's tree with gov files written and
staged, `.governance/outbox/` created, and no receipt. `cmd_apply`'s only wrapper is a
`finally: release_write_lock()`; there is no receipt salvage.

The resulting state is unrecoverable, which is what raises this above cosmetic. `--resume` refuses at
`:4274` for want of a receipt, and a plain re-`apply` refuses at `:4280` because `foreign_kit_present`
sees a kit resolving in the target that an absent receipt cannot claim. The same file records this
state twice as a ratified defect: the hoisted-containment comment at `:4334` and `git_pathspec`'s
docstring at `:3728` ("a verb whose failure mode is a half-applied install cannot fail that way").
The trigger is narrow — a corrupt or contended index right after a successful `git add` — but that is
precisely the condition the new liveness assertion exists to detect.

**Fix.** Wrap both `:4598` and `:4831` in the same `try/except Refusal` the diff added at `:6602`,
degrading to "no `oid` recorded for these rows" plus an `r.fail`, so `_cmd_apply` still reaches its
receipt write. Correct the comment at `:6598`, which currently states as fact that no other caller is
mid-write.

**Left-shift.** An arm that corrupts the target's index between the stage and the `oid` read (point
`GIT_INDEX_FILE` at a garbage file, or chmod it) and asserts `install.json` exists and `--resume`
works afterward. The class gate is cheaper and broader: a source-scan leg asserting that every
`index_read(` call site lexically after a `git_pathspec(..., ["add"], ...)` within the same function
is enclosed in a `try` that catches `Refusal`.

---

### F5 — medium — a tracked symlink pointing outside the tree is reported absent from the index

`tools/govkit/govkit.py:3805`.

The new out-of-tree filter drops any path whose `(target / _p).resolve()` escapes the repository.
`.resolve()` follows the final component's symlink, so a path that IS tracked but resolves outside
the tree is silently removed from both return values.

Reproduced on a scratch repo with a native symlink: `git ls-files -s` reports
`120000 9e422c30… link.txt`, while `index_read(repo, ["link.txt", "keep.txt"])` returns
`({'keep.txt': ('100644', '2fa992c0…')}, {'keep.txt'})`. The tracked symlink is gone from both.

The filter is strictly broader than its own justification. Its comment at `:3793` describes git
exiting 128 on a pathspec that is LEXICALLY outside the repository — and git never follows symlink
targets when matching pathspecs against index entries, so no symlink case was ever in scope.

The downstream consequence is at `:5919`. A receipt row of a `table` role whose destination is a
tracked symlink to a file outside the target now satisfies both `w["path"] not in index_present` and
`(target / w["path"]).is_file()`, so the S4 preamble raises the whole-run Refusal about a path that
is present in the WORKTREE and absent from its INDEX — about a path that IS in the index. Its stated
remedy, `git add`, cannot clear it, because the path is filtered before git is ever asked. The target
is wedged for every later `update`. Before this hunk the same path was read correctly.

Reachability is narrow — an adopter replacing a gov-landed file with an out-of-tree symlink, or a
junction on Windows with tracked files beneath it — but the misreport is demonstrated rather than
argued, and the failure mode is a wedged target with an unclearable message.

**Fix.** Filter lexically rather than by resolving symlinks: normalise the joined path
(`os.path.normpath((target / _p).as_posix())`, or `PurePosixPath` with `..` collapsed) and drop it
only when the normalised form escapes `target` or is absolute. That still excludes the
`../escape/out.txt` and `C:/…` cases the AC6 arm grades, without re-classifying a tracked symlink as
absent.

**Left-shift.** Add a positive arm to the AC6 fixture: a tracked symlink whose target is outside the
repository must be RETURNED by `index_read`, not filtered. The existing arms only grade the negative
direction, which is why a filter that is too wide passed them. Skip the arm explicitly with a named
reason where symlink creation is unavailable, rather than letting it vanish.

---

### F6 — medium — the landed receipt row is minted before the stage that can refuse it

`tools/govkit/govkit.py:7136`, with the stage-failure branch at `:7162`.

The receipt row is appended at `:7136`; `git add` runs at `:7162`. When the stage fails — the
ordinary `.gitignore` case the comment at `:7157` names, reproduced here as
`git add --pathspec-from-file=- --pathspec-file-nul` exiting 1 over an ignored path — the branch
unlinks the file, appends to `_refused_new`, and `continue`s. Nothing removes
`receipt["files"][-1]`, and the `snap_rows.append` at `:7192` is never reached, so the rollback
coverage this unit adds cannot see the row either.

`_refused_new` never calls `r.fail` — grepped every use: declared at `:7009`, appended at seven
sites, consumed only by the print at `:7411`. So `r.problems` can stay empty, the run falls through
to the re-stamp at `:7461` and the `install.sums` write at `:7463`, and the sidecar gains a
`sha256  <path>` line for a file that exists neither in the worktree nor in the index. `govkit check`
then reds at `:2890` and again on the sidecar cross-assertion at `:2964`.

The refusal message's claim that the path "was removed rather than left as a receipt row for an
untracked file" is therefore false — only the bytes were removed. One caveat on the finder's wording,
kept: the drift is not provably permanent, since a later `--write` update reclassifies the row as
`missing` and rewrites it through `checkout-index`/`update-index --cacheinfo`, which bypasses
gitignore. Until then, `check` reds on a row nothing explains.

**Fix.** Bind the row (`_new_row = {...}`), append it, and in the `if _add0.returncode != 0:` branch
do `receipt["files"].remove(_new_row)` — or build the row and only append it after the stage
succeeds, filling `oid` from `_idx0` at the same point.

**Left-shift.** An arm that lands into a destination the target's own `.gitignore` covers, asserting
three things after the run: the run exits with the refusal reported, `install.sums` gains no line for
that path, and a following `govkit check` is GREEN. The third assertion is the one that generalises —
"any `update --write` that reports refusals leaves `check` green" catches this whole class.

---

### F7 — medium — the rollback order and its console line misdescribe a removed landing

`tools/govkit/govkit.py:7366`, `:7372` and `:7382`. Three sites, one contiguous expression, two
independent finders.

For a kit whose only rolled-back write was a landing, `restored` is empty BY CONSTRUCTION: the
`origin == "landed"` block at `:7327` moves every successfully removed path out of `restored` into
`removed_landed`. The suite's own `[-ST1]` landkit fixture is exactly that shape — gov commit B adds
only `tools/landkit/arrival.txt`, and no table-origin rows exist for that kit. Three statements are
then wrong at once:

- `:7372` gates the "(nothing to restore: every path this kit owns was refused before it was
  written)" sentence on `not restored` alone, ignoring `removed_landed`. The order therefore prints
  `removed   tools/landkit/arrival.txt` and, on the very next line, a sentence denying that anything
  was written.
- `:7366` states "Every path below was restored to the index entry it had before the first byte
  moved, and this kit's receipt rows were restored with them" above BOTH lists. Both halves are false
  of a removed landing: it had no prior index entry (the snapshot is minted with
  `index: {_dest: None}`), and its receipt row is deleted at `:7329`, not restored. The code's own S7
  comment at `:7259` concedes exactly this, and the fix applied was only the per-path verb.
- `:7382` interpolates `restored` alone, so the console prints `ROLLED BACK · (no path restored)` for
  a run that wrote, staged and then unlinked a file. Combined with `:7332` stripping the path from
  `_landed_new`, the path reaches no stdout line at all — an unattended or CI capture records a
  rollback that appears to have touched nothing. That is the skip-that-looks-like-a-pass shape the
  surrounding code is explicitly written against ("EVERY COUNT PRINTS, including the zeros", `:7403`).

The `[-ST1]` arms at `selftest.py:5598` assert only that the `removed` line is present and the
`restored` line absent, so the contradiction ships green. Operator-facing text only, no state
corruption — but this is the durable record of a rollback in a repository gov does not own, and its
closing paragraph asks the operator to resolve by hand from it.

**Fix.** Gate the fallback sentence on `not restored and not removed_landed`; split the header
sentence by disposition (restored paths went back to their pre-run index entry with their rows;
removed paths were minted by this run, had no prior entry, and their rows were deleted); and build
the console summary from `restored + removed_landed`, falling back to `(no path restored)` only when
both are empty.

**Left-shift.** The partition assertion proposed under F3 covers the body lines. Add one negative arm
beside it: when `removed_landed` is non-empty, the order must NOT carry the "nothing to restore"
sentence, and stdout must not carry `(no path restored)`. A gate that only asserts a line is PRESENT
cannot see a contradicting line beside it, which is why the existing arms passed.

---

### F8 — low — a returned tuple element nothing reads, under a comment claiming it saves work

`tools/govkit/govkit.py:6374` (the return-site comment), with the appends at `:6367`.

`derive_unclaimed_candidates` appends `(_dest, _eid, _row0)` triples. The only two unpack sites are
`:6394` (`for _p0, _e0, _r0 in _pv_land`, a preview print) and `:6412`
(`_landed_kits_pre = {_e for _d0, _e, _r0 in _land_pre}`). A grep for `_r0` across the whole file
returns those two lines and nothing else, so the third element is never read — only the kit id is
consumed. Meanwhile the landing block at `:7014` makes its own `resolve_entry` call per kit and
re-derives `_row0` from `_res0["writes"]`, so the comment's "nothing has to resolve it twice" asserts
a benefit the code does not deliver.

Zero runtime impact, correctly filed low. Worth recording because it is precisely the
prose-asserts-what-code-does-not-do class this repo gates against, and because a later reader wiring
the landing through this function will assume the row is already threaded. Partial mitigation: the
function's own body at `:6316` does admit that "the landing loop below is not yet routed through this
function", fifty lines above the comment that overclaims.

**Fix.** Either consume the row in the write path — the landing loop at `:7031` can take its row from
the triple instead of re-resolving — or return pairs and delete the sentence about resolving twice.

**Left-shift.** An unused-local / unused-binding lint leg (pyflakes-class) scoped to
`tools/govkit/`, which would have flagged both `_r0` bindings at the site. That is a real gate rather
than a checklist entry, and this file is large enough to earn one.

---

### F9 — low — a prose count contradicting the guard added in the same diff

`tools/govkit/selftest.py:132`.

The comment on `run()` states "Eleven call sites carry a deliberate per-fixture vintage". The `[-ST5]`
AC5 guard added at `:5155` in the same diff counts anchored `run(` lines carrying their own `"--to"`
and asserts the population is 4.

An AST walk of the file gives: bare `run(...)` with a literal `--to` = 4 (lines 3765, 3796, 3808,
3827), `gov_run` = 5, `run_in_gov` = 4, plus one raw `subprocess.Popen`. No subset sums to eleven —
the combinations give 9, 10, 13 or 14. The two numbers describe the same set, the invocations a
blanket pin must not clobber, and they disagree. The guard is the derived authority; the comment is
the stale prose count AGENTS.md §7 bans outright, and the guard's own comment already records that an
earlier revision shipped a different miscount as a fact.

**Fix.** Delete the number from the comment and point at the guard instead — "the arms that carry
their own `--to` are counted and pinned by `[-ST5]` AC5" — so the count lives in exactly one place
that reds when it changes.

**Left-shift.** Extend the AC5 guard itself: assert that the comment block above `def run(` matches
no `(one|two|…|eleven|[0-9]+) call sites` pattern. The guard already owns the number, so making it
also refuse a second copy of that number is one predicate and closes the class for this file.

---

## What was refuted

Three of the sixteen raw findings did not survive the skeptic pass and are not carried here. No
finding came back without a usable verdict, so nothing in this round is outstanding-but-unclassified.

## What this round did not cover

The review scoped to the diff at the pinned base plus the immediate callers and callees of what it
touches. It did not re-derive the six unit specs — three prior spec-audit rounds in this folder did
that — it did not run the full merge bar, only the codebase-map leg, which is how F1 was measured,
and it did not exercise the govkit self-test suite. Two of the confirmed defects, F3's containment
divergence and F5's symlink filter, have POSIX-only or Windows-only arms; the reproductions recorded
above were done on node `d`, which is Windows, and the POSIX halves are argued from the code rather
than measured.
