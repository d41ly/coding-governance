# Re-review — aMendedLedger repair, `bde0de8..HEAD`

**Serves:** diff-review TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8  <!-- inferred: re-review of the repair, over a commit range -->

- **subject** — one commit (`f0335c9`), 8 files: `rows()` splits lead-in from anchor, `%B`-only keys
  splice instead of append, a `no_new_duplicates()` postcondition arms every clean verdict,
  `check-wiring.sh` runs a smoke three-way before printing `ok`, the drift selftest gains its second
  direction, and the previous closing review lands as a report.
- **review shape** — raw 24 · confirmed 20 · refuted 4 · unverified 0 · **precision 0.83**.
- **counts** — 7 blocking · 4 non-blocking.

---

## 1. Verdict

# DO NOT SHIP

**What decided it:** the repair moved the corruption, it did not close it — and on two inputs it
made the driver *worse than the driver it replaced*.

The previous review returned DO NOT SHIP on a single decisive standard: **the driver converts a loud
conflict into a silently wrong append-only file**. That standard is met again, by the repair itself,
on inputs the repair introduced. Splitting lead-in from anchor — the root-cause fix — narrowed the
delete comparison to the anchor line alone, so both honoured-delete branches now `continue` past
`lead(k)` and discard whatever the other node filed above the deleted row. I ran the identical three
inputs through three drivers:

```
driver @ HEAD (this repair) : rc 0  "1 dropped (delete honoured), clean"   incoming row: GONE   markers 0
driver @ bde0de8 (pre-repair): rc 1  CONFLICT                              incoming row: present, markers 1
no driver (git merge-file)   : rc 1  CONFLICT                              incoming row: present, markers 1
```

The commit that exists to stop silent record loss introduces a new silent record loss, at exit 0,
on a file whose backlog shards are declared mutable and whose 38-of-73 unkeyable `…-1b` rows travel
as exactly the content being dropped.

Second: the misfiling defect the repair was built to close (**B5**, "an incoming row is filed under
whatever heading happens to be last") is still live in mirror. I reproduced it end to end through a
real `git merge` on the real `memory/DECISIONS.md`, with this repo's own `.gitattributes` and
`merge.rows.driver` — a `PLAY` decision was **auto-committed under `## KICK — kickoff`**, rc 0,
audit line `clean`, zero markers, working tree clean. Git's built-in merge on the same two commits
files both rows correctly at rc 0. The old failure was fixed in one direction and reintroduced in
the other.

Third: **the bar is RED at HEAD.** `bash tools/run-gates.sh` in a clean clone returns
`gates RED — 1/39 legs failed (1 skipped)`. The commit message's closing line reads
`Full bar green, 38/38.` It is false against the tree it describes, and the leg count is wrong. In a
repair whose entire premise is *"the full bar returned 38/38 while the record was being corrupted"*,
shipping a green claim over a red bar is the same error one level up.

The wiring half of the repair is real and I would keep it: B2 (the published command), B4 (the drift
muzzle), B6/B7 (wiring that means the command runs) are genuinely closed, and I sabotaged each to
watch its arm red. The driver half is not shippable in this shape.

**Cheapest honest path to green:** B1 and B2 are contained edits in `merge()`/the splice with a
fixture each; B3–B5 are the postcondition's three widenings; B6 is two string edits in a committed
report; B7 is three fixtures. Nothing here needs a redesign — but nothing here should land on the
current claim that it is already done.

---

## 2. Blocking findings

### B1 — an honoured delete discards the deleted row's lead-in, so incoming content above it vanishes at rc 0

`tools/memory-tree/merge-rows.py:381-382` (theirs-deleted) · `:417-418` (ours-deleted)

**Failing scenario.** `rows()` now returns the anchor line separately from its lead-in. Both delete
branches compare the **anchor alone** (`o_txt == a_txt`, `O[k] == B[k]`), read "the other side left
this row untouched" even when that side added lines immediately above it, and then `continue`
without emitting `lead(k)`. Everything attached to that row — the `## FAMILY` heading that opens its
section, and any unkeyable `…-9b` correction row the other node filed above it — is discarded.
Before the split the lead was glued to the anchor, so a changed lead-in made the comparison unequal
and the driver conflicted.

Ran, base 3 rows / ours deletes row 2 / theirs inserts `- TOOL-zFixture-<n>b · OPEN · correction row
from node b` immediately above row 2:

```
merge-rows: 2 row(s) from ours, 0 new from theirs, 1 dropped (delete honoured), clean   rc=0
result: rows 1 and 3 only                             7b count: 0     markers: 0
```

Controls on the identical triple: `git merge-file` → rc 1, row preserved. **Pre-repair driver at
`bde0de8` → rc 1 `CONFLICT`, row preserved, 1 marker.** This is a regression introduced by the
repair, not an inherited gap. The mirror direction (ours adds, theirs deletes) behaves identically.
`no_new_duplicates()` is structurally blind: it is a duplicate detector and this is a drop. The
audit line cannot report it either — the lost content is unkeyed, so it lands in neither `kept` nor
`took_b`, and the line reads `0 new from theirs`.

**Exact fix.** Restore the pre-split semantics of the delete test: compare `o_lead[k] + [O[k]]`
against `b_lead.get(k, o_lead[k]) + [B[k]]` (and the mirror), so a side that added content adjacent
to the deleted row lands in the existing delete/modify CONFLICT branch. Emitting `lead(k)` before
both `continue`s is the smaller edit but silently relocates the other side's furniture, which is a
choice that should be conflicted rather than guessed. Add the fixture the 20 groups lack: ours
deletes row 2, theirs inserts an unkeyable row above it, assert rc 1 and one surviving copy. Watch
it red against the shipped code first.

### B2 — the splice files rows under the wrong `## FAMILY` heading, in both directions, at rc 0

`tools/memory-tree/merge-rows.py:316-324` · docstring `:47-53` · specs `spec/2026-08-09-spec-aMendedLedger-1.md:82`, `spec/units/2026-08-09-spec-aMendedLedger-5-u5-merge-driver.md:114`

**Failing scenario.** The splice seats its cursor with `at = order.index(k)` on keys shared with
`%A` only, and always inserts at `at + 1`. Two consequences, both silent:

*Direction one — ours' row pushed under theirs' new heading.* When both sides append after the same
predecessor and theirs' row is the **first** of the next section, theirs' row carries the `## FAMILY`
heading as its lead-in, so ours' row lands beneath it. Reproduced end to end through a real
`git merge` on the real `memory/DECISIONS.md`:

```
merge-rows: 36 row(s) from ours, 1 new from theirs, 0 dropped (delete honoured), clean
Merge made by the 'ort' strategy.                          MERGE rc=0    markers 0    status clean

10:## KICK — kickoff
12:- KICK-bNewTheirs-<n> · OPEN · theirs opened the KICK section
13:- PLAY-aNewOurs-<n> · OPEN · ours appended inside the PLAY section   ← a PLAY row under ## KICK
```

Control, same two commits, `merge.rows.driver` unset: the PLAY row at line 9 under `## PLAY`, rc 0,
0 markers, **correct**. Git's own merge gets this right and the driver does not.

*Direction two — theirs' row spliced behind a neighbour ours moved or deleted.* Because the cursor
sits at **ours'** position for the shared key, a row ours relocated across a `## ` boundary (or
honoured a delete on) drags theirs' new row into the wrong section. Also reproduced through a real
`git merge`: rc 0, `clean`, 0 markers, `- TOOL-bNine-<n>` committed under `## closed`.

Nothing can see either: `no_new_duplicates()` counts lines, the test's `dups()` oracle counts
repeats, and a misfiled row is neither. Case 11 (`merge-rows.test.sh:461-475`) is the arm for this
class and it is live — reverting the splice to a plain append reds it with `FAIL b-only placement` —
but its fixture is a pure insert in the final section, so it covers neither direction above.

**Exact fix.** Anchor the splice on both sides' surviving neighbours, not on `%B`'s predecessor
alone: when a `%B`-only key's insertion point collides with `%A`-only keys already following the
shared predecessor, emit the `%A`-only keys first; and refuse (CONFLICT) when the predecessor a
`%B`-only row arrived behind is not emitted in the section it occupied in `%B`. Widen case 11 with
both fixtures, asserting each row's line number against the next `^## `.

**And amend the specs in the same commit.** Both ratified tables still read `| id in %B only |
append |`, and U5 introduces its copy at `:110` with "implemented exactly as the master ratified it".
The code splices; `git diff --name-status bde0de8..HEAD` touches no `spec/` file and no
`memory/DECISIONS.md` entry, so the rule change is recorded nowhere but the commit message. Whatever
splice rule survives this fix is the one that must appear in both tables, with a rev bump. In a repo
whose product is record-vs-reality gating, a ratified decision table that no longer describes the
code is the failure class it exists to prevent — and nothing on the bar compares the two.

### B3 — `no_new_duplicates()` compares exact lines, so the same suffixed id from two nodes lands twice at rc 0

`tools/memory-tree/merge-rows.py:239-265`

**Failing scenario.** The census keys on stripped **line text**. Two nodes that each mint the same
unkeyable correction id (`…-9b` — the ratified form this very build added three of) with different
prose produce two different lines, so each is seen once, the cap holds, and both are written. The id
appears twice in an append-only record at rc 0.

```
merge-rows: 2 row(s) from ours, 0 new from theirs, 0 dropped (delete honoured), clean   rc=0
4  - TOOL-zFix-<n>b · CORRECTS TOOL-zFix-<n>: the ours-side wording
6  - TOOL-zFix-<n>b · CORRECTS TOOL-zFix-<n>: the theirs-side wording      <n>b occurrences: 2, markers: 0

the suite's own dups() oracle on that output:  TOOL-zFix-<n>b     ← it sees it; no fixture runs the shape
```

This is precisely the population the docstring at `:55-78` claims the postcondition exists for
("unkeyed content is precisely the population the postcondition below exists for") and the commit
message calls closed ("The corrupting half is closed"). It is **not** the stated residual — that
carve-out covers different suffixed rows *over-conflicting*, not the same id silently duplicating.
Case 12 only ever uses byte-identical text, which is the one shape the census catches.

**Exact fix.** Add an id-level postcondition beside the line-level one: key every `^\s*[-*] ` line
with a grammar at least as wide as the test's own oracle (`\b[A-Z]+-[A-Za-z0-9]+-[0-9]+[a-z]*\b`)
and refuse any id written more often than the most any single input carried it — the same rule
already implemented, lifted from *line* to *record*. Add a case 12b with divergent text asserting
rc 1. If the widening is genuinely deferred, narrow the docstring and the commit claim to
"byte-identical unkeyed lines only" rather than leaving both overstated.

### B4 — the lead-in dedup is keyed file-wide, so a legitimately repeated lead-in is dropped the second time

`tools/memory-tree/merge-rows.py:364-369`

**Failing scenario.** `seen_leads` is one set consulted for every new id anywhere in the file, and
`lead()` returns `[]` on the second identical signature. Correct for the case it was written for
(two nodes opening the *same* empty section, one piece of furniture). Wrong whenever the same
lead-in text legitimately belongs to two rows in two places — each occurrence is that row's own
structure, not a second copy of one heading.

Ran — ours adds `### 2026-08` + a new row in `## PLAY`, theirs adds `### 2026-08` + a new row in
`## TOOL`:

```
DRIVER   rc=0  "3 row(s) from ours, 1 new from theirs, 0 dropped (delete honoured), clean"
  13  - <the base row>   · OPEN · base
  14  - <theirs' new row> · OPEN · theirs      ← theirs' `### 2026-08` sub-heading DELETED

CONTROL  git merge-file rc=0 and CORRECT: `### 2026-08` at 15, theirs' row at 17
```

This is the second input in this diff where the control produces the fully correct file at rc 0 and
the driver produces a wrong one at rc 0 — strictly worse than no driver.

**Exact fix.** Scope the dedup to the case it was measured on: suppress a repeated lead-in only when
the two new ids are **adjacent in the emit order**, or only when the repeated signature is a prefix
of the base furniture the two ids share. Add the negative arm — two new ids in non-adjacent
positions carrying an identical lead-in — asserting both copies survive, against the `merge-file`
control, which is right here.

### B5 — any unrelated conflict disables the duplicate detector for the whole file

`tools/memory-tree/merge-rows.py:451-452`

**Failing scenario.** The postcondition runs only `if verdict == "clean"`. The justification at
`:449-450` (a conflict hunk repeats context lines by construction) argues for excising the marker
*regions*, not for skipping the census. One unrelated both-sides row edit anywhere in the file turns
the detector off entirely, and the duplicate is emitted **outside** the markers, in text the author
reads as already settled. An author who resolves the one marked hunk and commits ships a duplicated
row into an append-only record.

```
merge-rows: 3 row(s) from ours, 0 new from theirs, 0 dropped (delete honoured), CONFLICT   rc=1
 4  - TOOL-zFix-<n>b · an unkeyable correction row minted on BOTH nodes
 6  - TOOL-zFix-<n>b · an unkeyable correction row minted on BOTH nodes    ← duplicate, OUTSIDE the markers
 7  <<<<<<< ours     ... (the unrelated zFix-3 edit)
no DuplicatedContent on stderr — the postcondition never ran

same duplicate, no unrelated conflict:
merge-rows: FAILED (DuplicatedContent: 1 line(s) would be written more often than any single input
  carries them, e.g. '- TOOL-zFix-<n>b · …' x2 against x1) — writing a conflict rather than a silent take-ours
```

**Exact fix.** Run `no_new_duplicates` unconditionally over the merged lines with the marker regions
excised (drop everything between `<<<<<<<` and `>>>>>>>` before the census). A duplicate in the
settled region is exactly as invisible at rc 1 as at rc 0, because the author only inspects the
hunks. Add case 12's fixture again with one extra both-sides row edit, asserting the refusal still
fires.

### B6 — the merge bar is RED at HEAD; the commit message asserts it is green

`memory/builds/aMendedLedger/reviews/2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md:200-201`

**Failing scenario.** `f0335c9` adds the previous closing review, whose B5 transcript quotes two
invented fixture ids — `TOOL-aNewOurs-<n>` and `PLAY-bNewTheirs-<n>`, with the trailing numeral
elided **here** so this report does not commit the same defect it is reporting; the literals are at
`:200-201` of that file. `corpus_ids.py` check 14 harvests citations without exempting fenced
transcripts, so both are cited-and-never-defined. The first leg of `tools/run-gates.sh` exits 1.

```
worktree at HEAD, git status clean:
  HYGIENE check 14: id PLAY-bNewTheirs-<n> is cited but never defined, and is not in memory/project/id-orphan-waiver.txt
  HYGIENE check 14: id TOOL-aNewOurs-<n>  is cited but never defined, and is not in memory/project/id-orphan-waiver.txt
  rc=1

clean clone, branch present so every leg resolves:
  GATE FAIL  memory hygiene (19 checks) (exit 1)
  gates RED — 1/39 legs failed (1 skipped)

same command at the parent bde0de8: rc=0        ← this diff caused it
git log --diff-filter=A on that report:  f0335c9
```

`.githooks/pre-push` runs the full bar and blocks a red push to the default branch, so this cannot
land as committed. The commit message ends `Full bar green, 38/38.` — wrong on the verdict and on
the count (`tools/gate-legs.json` declares 39).

**Exact fix.** Respell the two id-shaped literals in the committed report so they do not key
(`TOOL-<oursSlug>-1`, `PLAY-<theirsSlug>-1`, or elide as that report's own B1 transcript already
does). **Do not use the waiver:** `.memory-tree.conf:39` pins `ORPHAN_ID_PIN="5"` and
`memory/project/id-orphan-waiver.txt` holds exactly 5 entries under a shrink-only rule, so adding
two would red the ratchet instead. Re-run `bash tools/run-gates.sh` to 39/39 and correct the commit
message before landing.

### B7 — three of the repair's own new mechanisms have no arm; each sabotage passes 20/20

The repair's stated discipline is "Every arm was watched failing before its fix and passing after."
Three of its mechanisms fail that test. I sabotaged each in a throwaway clone, one at a time.

**(a) `lead()`'s `k in O` three-way — `merge-rows.py:355-358`.** This is what `rows()`'s own
docstring leads with: "an edit to the heading on one side and to the row on the other could not both
survive". Replacing it with `return list(a_lead.get(k, o_lead[k]))` silently discards the other
side's heading rename at rc 0 — and `bash tools/memory-tree/merge-rows.test.sh` prints
`PASS — merge-rows: 20 fixture groups held`, with `check-arms.py` rc 0 and the whole bar showing the
identical failures as unsabotaged HEAD.

```
HEAD       rc=0 → ## RENAMED HEADING  +  - TOOL-zFix-<n> · OPEN · OURS-EDIT
SABOTAGED  rc=0 → ## OLD HEADING      +  - TOOL-zFix-<n> · OPEN · OURS-EDIT     (theirs' rename gone)
```

*Fix:* one fixture — a `## ` heading inside the row block, renamed on `%B`, its row edited on `%A`,
asserting both survive at rc 0.

**(b) `census()`'s `strip()` — `merge-rows.py:227`.** Deliberate and documented, and nothing tests
it. Changing the key to the raw line leaves the leg at `PASS — 20 fixture groups held` while a
reachable input corrupts: theirs' copy of the row as the final line **with no trailing newline**.

```
SHIPPED    rc=1  DuplicatedContent … x2 against x1 — writing a conflict rather than a silent take-ours
SABOTAGED  rc=0  "2 row(s) from ours, 0 new from theirs, 0 dropped (delete honoured), clean"   9b × 2
```

*Fix:* duplicate case 12 with one side's copy differing only in line form (missing final newline),
asserting the same rc 1. Note the docstring's stated channel — a CRLF side against an LF side — is
**not** the live one: git hands the driver uniformly-terminated `%O`/`%A`/`%B` under either
`core.autocrlf`, and the governed blobs are all-LF on check-in. Build the fixture on line form, and
correct the comment.

**(c) `check-wiring.sh`'s smoke three-way — `tools/check-wiring.sh:313-315`.** The fixture is
`x` / `a\nx` / `x\nb`. `split_regions()` finds no anchor, so the whole file is preamble and the run
is a plain `git merge-file`: `rows()`, `merge()`, `lead()`, the splice and `no_new_duplicates()` are
never entered. The arm's own comment claims "'Wired' is 'the command git will exec actually
merges'". A one-token drift in `.memory-tree.conf` FAMILIES (`tooling:TOOL` → `tooling:TOOLS`) makes
the driver key **zero** rows — every governed append-collision conflicts forever, the driver is
completely inert — and the arm still prints:

```
ok       merge     — merge.rows.driver wired
merge-rows: 0 row(s) from ours, 0 new from theirs, 0 dropped (delete honoured), CONFLICT   markers=1
```

*Fix:* put one anchored row in each of the three smoke inputs (`%A` appends a second, `%B` a third)
and require rc 0 with all three ids present exactly once. Same single python start; turns the arm
into what its comment claims.

---

## 3. Non-blocking

- **N1 — a row theirs re-filed into another section is silently reverted to ours' section**
  (`merge-rows.py:316-324`). `order` is seeded from `a_order` and shared keys are never
  repositioned, so a `%B` cross-section move is discarded at rc 0 (`4 row(s) from ours … clean`,
  theirs' move gone; control refuses at rc 1). LOW today — the backlog shards carry no `## `
  sections and `DECISIONS.md` is append-only in practice — but it contradicts the docstring's
  `:53` claim that splicing keeps section membership, which it does only for `%B`-only rows. Fix
  with B2, or narrow the docstring.
- **N2 — two *different* empty sections inside the row block scramble instead of merging.** Each
  side opening a different one yields overlapping-but-unequal lead-in signatures, so `seen_leads`
  does not suppress the second, the heading is emitted twice, and the whole file returns as one
  `DuplicatedContent` conflict with both rows misfiled. `git merge-file` resolves the same three
  inputs at rc 0, correctly. Fails **closed**, so LOW — but it is a regression against the merge
  being replaced on a variant of the class the unit auto-resolves. Unreachable today only because
  `## DEPL` sits in the trailer; reachable the moment a family is added ahead of the last one.
- **N3 — LF-only conflict markers stamped into a CRLF file on the fail-closed path**
  (`merge-rows.py:492`). `DuplicatedContent` now raises from ordinary content, so `main()`'s
  whole-file writer went from exotic to routine — and on a CRLF worktree file the result is mixed:
  `lines: 13 | without CR: 3` (`<<<<<<< ours`, `=======`, `>>>>>>> theirs (merge-rows failed…)`).
  Case 7b's CR:LF assertion covers clean merges only. Derive the terminator from `%A`'s dominant
  ending and extend 7b to an rc-1 arm. Secondary: raising with the offending ids would let the
  handler write a scoped hunk instead of a ~180-line whole-file conflict in an append-only record.
- **N4 — the README's new wiring doctrine is false in the layout `WIRE-INTO-PROJECT.md` produces**
  (`tools/memory-tree/README.md`). It claims `check-wiring.sh` "sets exactly one of the two commands
  below" and that a mixed-prefix command "names a driver that exists in neither layout". The runbook
  copies the kit to `<project>/memory-tree/` (`:103`) and `check-wiring.sh` to `<project>/tools/`
  (`:354`) and never installs `pyrun.sh`; following `check-wiring.sh:271`'s own remedy lands it at
  `<project>/tools/lib/`, and `--fix` then sets exactly the mixed spelling — which works. Not
  corrupting, but the published doctrine is wrong for the only layout the runbook creates, and
  AC12's fixtures are both single-prefix. Restate the claim, or fix the remedy's prefix.

---

## 4. Precision

**0.83** — 24 findings raised, 20 confirmed, 4 refuted, 0 unverified.

Refuted, with the measurement that killed each:

- *"The splice cursor advances over honoured-delete keys, misplacing the next `%B` row."* The
  symptom reproduces, but the named mechanism is **inert**: applying the finding's own fix
  (`continue` before the `at`/`order.insert` pair) produced byte-identical output, and a 600-trial
  randomized differential reported **0** differing outputs. The real cause is B1 — the deleted row's
  `## TOOL` lead-in is discarded and reappears as the next survivor's lead. B1's fix turns the same
  input into a loud `DuplicatedContent` refusal. Same root, subsumed.
- *"The test oracle's id grammar is narrower than the driver's `key()`, so arms pass vacuously."*
  The grammar gap is real; the consequence is not. All 14 `run` call sites declare non-empty id sets
  over fixtures the test writes, and the one corpus touch (`:104`) is a liveness guard that **fires**
  on the hypothesized corpus rather than passing silently.
- *"`dups()` over the real corpus reports pre-existing duplicates."* It does — but `dups()` is never
  pointed at the corpus; its only call sites are `$TMP/a` and two-line fixtures. A future false red,
  not an arm that cannot fail.
- *"The drift-audit selftest is flaky / the DECLARED_EMPTY muzzle greens `--check`."* 25 consecutive
  selftest runs green, 3 full bar runs green on that leg, and the claimed signature is structurally
  impossible — `--check`'s over-pin filter and the human ladder evaluate the identical predicate,
  and DECLARED_EMPTY is consulted only by the `dead` filter.

---

## 5. Verified by execution

Everything above was run in this session, in `git clone --shared` copies of `f0335c9` (the primary
worktree was touched read-only; `git status --porcelain` empty before and after).

**Real `git merge` runs** — repo's own `.gitattributes` (`git check-attr merge -- memory/DECISIONS.md`
→ `merge: rows`) with `merge.rows.driver` configured:

| merge | driver | result |
|---|---|---|
| ours appends in `## PLAY`, theirs opens `## KICK`, real `DECISIONS.md` | HEAD | rc 0, `clean`, 0 markers, **PLAY row committed under `## KICK`** |
| same two commits | driver unset | rc 0, 0 markers, **correctly filed** |
| ours moves a row across a `## ` boundary, theirs adds after it | HEAD | rc 0, `clean`, 0 markers, **theirs' row under `## closed`** |
| ours deletes a row, theirs adds to that section | HEAD | rc 0, `1 dropped … clean`, **theirs' row under `## open`** |
| node a retires a backlog row, node b files a `…-9b` row above it | HEAD | rc 0, `clean`, **node b's row gone**, tree clean |

**Direct three-way runs, each against a control:** honoured-delete + adjacent lead-in (HEAD rc 0 row
gone · `bde0de8` rc 1 row kept · `git merge-file` rc 1 row kept); divergent-text `…-9b` duplicate
(rc 0, id ×2, the suite's own `dups()` oracle sees it); repeated `### 2026-08` lead-in (HEAD rc 0
sub-heading dropped · control rc 0 **correct**); duplicate + unrelated conflict (rc 1, duplicate
outside the markers, no `DuplicatedContent`) versus the same duplicate alone (refuses, rc 1);
cross-section move (rc 0, theirs' move discarded); CRLF fail-closed path (3 LF-only marker lines in
an otherwise all-CRLF 13-line file).

**Arms sabotaged, one at a time, and observed:**

| sabotage | expected to red | observed |
|---|---|---|
| `lead()` `k in O` three-way → take-ours | replay leg | `PASS — 20 fixture groups held`, `check-arms` rc 0, full bar unchanged — **NOT ARMED** |
| `census()` strip → raw line | replay leg | `PASS — 20 fixture groups held`; duplicate written at rc 0 `clean` — **NOT ARMED** |
| `.memory-tree.conf` FAMILIES `TOOL`→`TOOLS` (driver keys 0 rows) | `check-wiring --check` | `ok merge — merge.rows.driver wired` — **NOT ARMED** |
| splice → plain append | replay leg | `FAIL b-only placement …` — armed (but only the one direction) |

**Gates run:** `bash tools/memory-tree/check-memory-hygiene.sh` in the primary worktree → rc 1, the
two check-14 orphans; the same command at `bde0de8` → rc 0; `bash tools/run-gates.sh` in a clean
clone with the branch present → `gates RED — 1/39 legs failed (1 skipped)`;
`bash tools/memory-tree/merge-rows.test.sh` at HEAD → `PASS — merge-rows: 20 fixture groups held`,
**green throughout every defect in §2**.

**Confirmed closed by the repair** (sabotaged, arm red, restored): the drift-audit muzzle
(`and s["signal"] not in declared` on `drift_report.py` → selftest rc 1, naming the signal); the
`check-wiring` smoke block (deleting it reds 4 assertions, ignoring its verdict reds 3); the
`.gitattributes` `merge=rows` lines (commenting one out reds AC11); the README's third-spelling ban
(a mixed literal reds AC12).
