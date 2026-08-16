# Regression check — aMendedLedger round 3, `1a22f1d..HEAD`

**Serves:** diff-review TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8  <!-- inferred: regression check over a commit range -->

- **subject** — one commit (`68b90fe`, "round 3 — the driver stops being worse than the merge it
  replaces"), 10 files, +658/-94. The engine change is `tools/memory-tree/merge-rows.py`: `lead()`'s
  lead-in dedup narrows from file-wide to adjacency-scoped, `census()` narrows from every non-blank
  line to row-shaped lines only, a `no_misfiled_rows` postcondition arrives, the delete tests widen
  back to the whole row, and `%B`-only keys splice past trailing `%A`-only keys. Eight new fixture
  groups (28 total) and one new `check-wiring.sh` state.
- **question** — one only: **did round 3 introduce a NEW defect where the driver loses or corrupts
  content that `git merge-file` does not?**
- **review shape** — survivors verified 17 · upheld 2 · refuted 15 · **precision 0.12**.
- **counts** — 1 blocking · 4 non-blocking.

---

## 1. Verdict

# DO NOT SHIP

**What decided it: yes — and it is the same class of defect round 1 returned DO NOT SHIP for.** On a
reachable shape, round 3 writes a section heading **twice** into an append-only index, at **rc 0**,
with **zero conflict markers**, and `git merge` **auto-commits it**. The round-2 driver produces the
correct single-heading file on the identical three blobs, and `git merge-file` refuses the input
outright. So on this input the driver is worse than the driver it replaces *and* worse than no driver
at all — which is exactly the standard the commit message claims to have met, and the standard
`lead()`'s own docstring sets ("emitting both is how `## DEPL — deployer` appeared twice in an
append-only file at exit 0").

The mechanism is that round 3 narrowed **both** guards that stood between this input and the file,
in the same commit:

| guard | round 2 | round 3 | effect |
|---|---|---|---|
| `lead()` dedup | file-wide (`sig in seen_leads`) | adjacency-only (`sig == prev_new_sig`) | the suppression can be dodged |
| `census()` population | every non-blank line | `_ROW_RE`-shaped lines only | a doubled heading is no longer counted |

A heading is not row-shaped, so once the dedup is dodged nothing observes the duplicate. It is dodged
by **any new row landing between the two rows that carry the same furniture**: `lead()` resets
`prev_new_sig` to `None` only on the `k in O` branch, so a *new* middle row with a different
non-blank lead-in overwrites the signature and the second copy of the heading is emitted again.

I verified both narrowings are individually load-bearing by patching each one back (§5). Neither
change is wrong on its own — each closes a real round-2 defect — but their intersection is a hole,
and nothing on the bar can see it: `merge-rows.test.sh` reports `PASS — 28 fixture groups held` and
`tools/run-gates.sh` reports `gates GREEN — 38/38 legs passed (1 skipped)` on the tree that does this.

This is **not** a re-report of round 1's B1. B1's trigger (each side opens the same empty section
with one row, no intervening row) is genuinely **fixed** at HEAD — I ran it and got one heading at
rc 0. The doubling only returns through the middle-row path, which did not exist before this diff.

---

## 2. Blocking regression

### B1 — a section heading is written twice and auto-committed at rc 0

`tools/memory-tree/merge-rows.py` — `lead()` (adjacency dedup) x `census()` (row-shaped population).

**Shape.** This repo's live `memory/DECISIONS.md`: `## KICK — kickoff` / blank / `*(none yet)*`. Node
a opens the section with two rows separated by an unkeyable note row; node b opens the same section
with one row. Both `## KICK` and `## DEPL` are empty in this corpus today, so the trigger is the next
session in which two nodes each land a first decision in the same family — the same reachability the
suite's own case 10 comment asserts.

**Reproduction — real `git merge`, real file, driver wired.**

```
$ git clone --shared <worktree> r3 && cd r3          # HEAD = 68b90fe
$ git config merge.rows.driver "bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P"
$ git check-attr merge -- memory/DECISIONS.md
  memory/DECISIONS.md: merge: rows

  # branch `theirs`:  *(none yet)*  ->  - KICK-zTheirsKick-<n> · theirs kickoff decision
  # branch `ours`  :  *(none yet)*  ->  - KICK-zOursKick-<n>   · ours first kickoff decision
  #                                     - an unkeyable ours-side note row
  #                                     - KICK-zOursKick-<m>   · ours second kickoff decision

$ git merge theirs
  merge-rows: 37 row(s) from ours, 1 new from theirs, 0 dropped (delete honoured), clean
  Auto-merging memory/DECISIONS.md
  Merge made by the "ort" strategy.
  rc=0        -> AUTO-COMMITTED as 2915d26, working tree clean
```

The committed file:

```
## KICK — kickoff

- KICK-zOursKick-<n> · ours first kickoff decision
- an unkeyable ours-side note row
- KICK-zOursKick-<m> · ours second kickoff decision

## KICK — kickoff                     <-- SECOND COPY
- KICK-zTheirsKick-<n> · theirs kickoff decision

  "## KICK — kickoff" x 2 | conflict markers x 0
```

**Controls, identical three blobs:**

```
git merge-file -p -L ours -L base -L theirs   rc=1  heading x1  (refuses the input)
round-2 driver @1a22f1d (run in-tree)         rc=0  heading x1   94 lines   CORRECT
round-3 driver @HEAD                          rc=0  heading x2   97 lines   CORRUPT
```

**Attribution, one variable at a time (each patch applied to HEAD's bytes, then reverted):**

```
A. census() row-shape filter removed (round-2 breadth), lead() untouched:
   merge-rows: FAILED (DuplicatedContent: 1 row line(s) ... "## KICK — kickoff" x2 against x1)  rc=1

B. lead() dedup widened back to file-wide (round-2 semantics), census() untouched:
   merge-rows: 37 row(s) from ours, 1 new from theirs, clean   rc=0   heading x1
```

So either narrowing alone would have prevented this. The defect is the pair.

**Why the suite does not catch it.** Case 10 ("both nodes open the same empty section") uses exactly
one row per side, so `prev_new_sig` is never overwritten. Case 17 ("a lead-in that legitimately
repeats") separates its two copies with a **shared base row** (`TOOL-zFixture-<n>`), which resets
`prev_new_sig` through the `k in O` branch. Neither shape reaches the middle-row path.

**Fix direction (not prescriptive).** The cheapest correct move is to restore `census()`'s breadth
over headings while keeping `_ROW_RE` for the *id* census — the duplicate-furniture population and
the duplicate-record population are different questions, and round 3 collapsed them onto one
predicate. Whatever the fix, it needs an arm on the middle-row shape, since the current 28 groups
pass either way.

---

## 3. Non-blocking observations

- **A repeated lead-in is deleted at rc 0 where git preserves it — real, live, undisclosed, but
  INHERITED, not a round-3 regression.** Ours appends three rows, the first and third each led by
  `> a note that legitimately repeats`, the second by a blank line only; theirs edits only preamble
  prose. Driver rc 0 `clean`, second note **gone**; `git merge-file` rc 0 with both copies. Round 2
  loses it identically, so round 3 did not introduce it — but it does falsify the commit's headline
  claim, and it is not among the four disclosed Gaps. Confirmed end to end: real `git merge`
  committed `bb64ca8` with diffstat `1 insertion(+), 2 deletions(-)` from a preamble-only incoming
  change. Cause is the blank-lead-in exemption at `merge-rows.py:551` — `if not sig: return
  list(got)` skips the `prev_new_sig` reset, so a furniture-less row does not break the adjacency
  chain and the suppression reaches across it.
- **The blank-lead-in exemption has no arm.** Mutating it so a blank lead-in *breaks* the chain
  leaves the suite at `PASS — 28 fixture groups held`, and the mutant is demonstrably
  non-equivalent: on the fixture above it writes 2 note copies where HEAD writes 1. An untested
  branch that changes real output. (Note the mutant actually *removes* the loss above.)
- **The other 15 survivors are all fail-closed and do not clear the bar.** Every one is driver rc 1 /
  `git merge-file` rc 0, with both inputs written verbatim between one marker pair and git refusing
  the commit. Spot-checked the misfiled class end to end (ours fills the KICK placeholder, theirs
  appends `PLAY-zTheirsRule-<n>`): driver rc 1 `FAILED (Misfiled: ... under "## KICK — kickoff"
  against ["## PLAY — playbook"])`, 186 lines, one marker pair, each row present exactly once;
  `git merge-file` rc 0, 92 lines. Noisy and heavier than it needs to be on a ~90-line index, but
  nothing is lost or corrupted — the dossier already books this as ergonomics under "A postcondition
  refusal is a WHOLE-FILE conflict, not a scoped hunk".
- **`_ID_RE`'s docstring overclaims.** It says "deliberately WIDER" than the anchor grammar;
  measured, it is wider for the session era only and *narrower* for the two flat eras (flat-numeric
  ids key but do not match `_ID_RE`). Zero reachability on this corpus (0 of 91 governed rows carry
  a flat id), so it is a comment defect, not a behaviour defect.

---

## 4. Precision

**0.12** — 17 survivors reached verification, 2 upheld, 15 refuted.

Blocking precision is **0.06**: exactly one survivor is a new content-corrupting regression against
`git merge-file`. The dominant refutation class (13 of 15) is the same mistake repeated — reading a
fail-closed conflict as damage. A conflict where git resolves cleanly is noise; only rc 0 with wrong
bytes is damage, and the review question named that distinction explicitly.

---

## 5. Verified by execution

Every claim above was run, not read. Work happened in throwaway `git clone --shared` copies; the
worktree under review was never modified.

**Merges run.**
- Real `git merge` with `merge.rows.driver` configured and the tracked `.gitattributes` `merge=rows`
  attribute live (`git check-attr` confirmed), on the real `memory/DECISIONS.md`, twice: the B1
  shape (rc 0, auto-committed `2915d26`, heading x2, markers 0) and the repeated-lead-in shape
  (rc 0, auto-committed `bb64ca8`, one note copy where ours had two).
- Standalone driver invocations through `tools/lib/pyrun.sh` on five fixture families: the B1 doubled
  heading, the one-row-per-side simple shape, the repeated lead-in, the misfiled-row shape, and the
  rebuilt fixtures that replaced my own two bad ones.
- Two false starts recorded honestly: the first fixture was written to a Windows temp path while the
  copy step read the MSYS one, and a later one was rebuilt from the already-merged worktree. Both
  produced wrong results (`0 row(s) from ours`, and a spurious heading x2 on the simple shape) and
  both were discarded and rebuilt from a pristine base before any conclusion was drawn.

**Controls compared.** On every fixture, three engines on byte-identical inputs: round-3 driver at
`68b90fe`, round-2 driver at `1a22f1d` (copied *into* `tools/memory-tree/` — run from outside the
tree it dies on `no .memory-tree.conf above ...`, which would have been a fake control), and
`git merge-file -p -L ours -L base -L theirs`. The round-2 control is what makes B1 decisive: it is
not merely that git conflicts, it is that the immediately preceding driver got this right.

**Arms sabotaged.**
- `census()` row-shape filter deleted -> the B1 fixture flips to
  `FAILED (DuplicatedContent ... "## KICK — kickoff" x2 against x1)` rc 1.
- `lead()` dedup widened to file-wide -> the B1 fixture flips to heading x1 rc 0.
- Blank-lead-in exemption mutated to break the chain -> suite still
  `PASS — 28 fixture groups held`, output demonstrably different (2 note copies vs 1), proving the
  mutant non-equivalent and the branch unarmed.
- All three patches reverted to HEAD's exact bytes, confirmed by `git diff --stat` returning empty.

**Bar state on the tree that does this.**
```
bash tools/memory-tree/merge-rows.test.sh        -> PASS — merge-rows: 28 fixture groups held
GOV_DEFAULT_BRANCH=main bash tools/run-gates.sh  -> gates GREEN — 38/38 legs passed (1 skipped)
```
A green bar is not evidence here. (Clone note: a `--shared` clone of the worktree has no local
`main`, so the drift-audit records leg fails closed until `git branch main origin/main` is run —
`GOV_DEFAULT_BRANCH` alone is insufficient. Clone artifact, not a repo defect.)
