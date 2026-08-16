<!-- The merge driver's reproduction corpus: every defect the three adversarial rounds
     actually REPRODUCED, deduped. It is the acceptance suite for the U9 redesign, and it is
     in the tree rather than a scratchpad because a session that did not run those rounds
     cannot rebuild it. Assembled 2026-08-10 from the three reports under ../reviews/. -->

**Serves:** journal TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8  <!-- inferred: the merge driver's reproduction corpus, evidence across the build -->

# Reproduction corpus — row-keyed merge driver (`tools/memory-tree/merge-rows.py`)

Acceptance suite for the redesign. Every case below was reproduced by execution in one of three
adversarial review rounds, or re-run in this session. A redesign must produce, for every case, an
outcome that is **not worse than `git merge-file` on the identical three blobs**.

## Provenance

| round | report | subject commit | driver state |
|---|---|---|---|
| R1 | `memory/builds/aMendedLedger/reviews/2026-08-09-review-aMendedLedger-1-closing-diff.md` | `a08c2f3` (U5, reviewed at `bde0de8`) | first cut |
| R2 | `.../2026-08-09-review-aMendedLedger-2-repair.md` | `f0335c9` | repair 1 |
| R3 | `.../2026-08-09-review-aMendedLedger-3-regression.md` | `68b90fe` | repair 2 = **current HEAD** |

Current worktree HEAD is `68b90fe`. `merge-rows.test.sh` reports `PASS — 28 fixture groups held` and
`tools/run-gates.sh` reports `gates GREEN — 38/38` on the tree that still fails cases **C2**, **C4**,
**C8**, **C15**, **C16**, **C21**. A green bar is not evidence in this area.

## Conventions

- **CORRUPTION** = rc 0 (or rc 1 outside the markers) with wrong bytes: content lost, duplicated, or
  filed under a heading no input filed it under. Only this class is a defect.
- **CONSERVATIVE** = the driver conflicts where git resolves. Noise, not damage. Recorded so the
  redesign does not "fix" a conflict into a silent guess.
- Ids are spelled with `<n>` / `<m>` in place of the trailing numeral throughout (a committed report
  that spells a fixture id verbatim reds hygiene check 14 as cited-but-never-defined — that is R2-B6,
  and it turned the whole bar red once already).
- **Live furniture** (real `memory/DECISIONS.md`, 91 lines, 73 `- ` rows, **35 anchored / 38
  unkeyed**, re-measured this session): a title, two `>` routing lines, then
  `## PLAY — playbook` (rows), `## KICK — kickoff` + `*(none yet)*`, `## TOOL — tooling` (rows),
  `## DEPL — deployer` + `*(none yet)*`. First anchor at line 8, last at line 87, so `## PLAY` is
  **preamble** and `## KICK` / `## TOOL` / `## DEPL` are **inside the row block**. Both `KICK` and
  `DEPL` are empty today: the trigger for the whole doubled-heading family is two nodes landing a
  first decision in the same family.
- Correction-id form `<FAMILY>-<slug>-<n>b` is ratified and in use; it does **not** key (the shared
  session era in `tools/memory-recall/extract.py:73` is `[a-z][A-Za-z]{2,}-\d+` inside `\b…\b`).
  This was never widened — verified at HEAD.

---

# A. Merge-algorithm cases

### C1 · DOUBLED-HEADING-SIMPLE — R1-B1
- **base**: `## KICK — kickoff` / blank / `*(none yet)*` (or the same shape at `## DEPL`).
- **ours**: replaces the placeholder with one row, `KICK-zOursKick-<n>`.
- **theirs**: replaces the placeholder with one row, `KICK-zTheirsKick-<n>`.
- **driver (R1)**: rc 0, `36 row(s) from ours, 1 new from theirs, 0 dropped … clean`, **0 markers**,
  `## DEPL` x2 (base 1), `*(none yet)*` x3 (base 2). Reproduced end-to-end through a real
  `git merge --no-edit` with the tracked `.gitattributes` + config (`Merge made by the 'ort'
  strategy`, rc 0). Hygiene + `corpus_ids.py` both rc 0 on the corrupted file.
- **control**: `git merge-file -p` → **rc 1**, one hunk, heading x1.
- **verdict**: CORRUPTION.
- **covered**: yes — group 10 ("both nodes open the same empty section"). Fixed at HEAD (R3 re-ran it:
  one heading, rc 0).
- **mechanism**: `rows()` attached every unkeyed line since the previous anchor to the *following*
  anchor, so the heading rode in as part of the first row of its section and was emitted once per side.

### C2 · DOUBLED-HEADING-MIDDLE-ROW — R3-B1 · **LIVE AT HEAD** · re-run this session
- **base**: real `memory/DECISIONS.md`; `## KICK — kickoff` / blank / `*(none yet)*`.
- **ours**: placeholder replaced by **three** lines — `KICK-zOursKick-<n>`, then an *unkeyable*
  note row (`- an unkeyable ours-side note row`), then `KICK-zOursKick-<m>`.
- **theirs**: placeholder replaced by one row, `KICK-zTheirsKick-<n>`.
- **driver @ HEAD**: rc 0, `37 row(s) from ours, 1 new from theirs, 0 dropped … clean`, **0 markers**,
  97 lines, `## KICK — kickoff` **x2**. R3 ran this through a real `git merge` and it
  **auto-committed** (`2915d26`, working tree clean). Re-run standalone this session on the real file:
  identical (rc 0, heading x2, markers 0).
- **control**: `git merge-file -p` → **rc 1**, heading x1 (refuses). Round-2 driver at `1a22f1d` →
  rc 0, heading x1, 94 lines, **correct**.
- **verdict**: CORRUPTION — worse than git *and* worse than the driver it replaced.
- **covered**: **no**. Group 10 uses exactly one row per side; group 17 separates its two copies with
  a shared base row, which resets the chain via the `k in O` branch.
- **mechanism**: intersection of two round-3 narrowings, each individually load-bearing (R3 patched
  each back: restoring either prevents it). `lead()`'s dedup went file-wide → adjacency-only
  (`sig == prev_new_sig`), so a *new* middle row with a different non-blank lead-in overwrites the
  signature and the second copy of the heading is emitted again; `census()` went from every non-blank
  line → `_ROW_RE`-shaped lines only, so a doubled heading is no longer counted by the postcondition.

### C3 · LEADIN-DROPPED-TWO-SECTIONS — R2-B4
- **base**: row block with `## PLAY` and `## TOOL` sections.
- **ours**: adds `### 2026-08` + a new row inside `## PLAY`.
- **theirs**: adds `### 2026-08` + a new row inside `## TOOL`.
- **driver (R2)**: rc 0, `3 row(s) from ours, 1 new from theirs, 0 dropped … clean`, **theirs'
  `### 2026-08` sub-heading DELETED**.
- **control**: `git merge-file` → **rc 0 and fully correct** (sub-heading present, both rows filed).
- **verdict**: CORRUPTION (silent loss where git is right at rc 0).
- **covered**: yes — group 17, which runs a live `git merge-file` control and byte-compares.
- **mechanism**: `seen_leads` was one file-wide set; the second identical lead-in signature returned
  `[]`. Fixed in round 3 by adjacency scoping — which is what opened **C2**.

### C4 · LEADIN-DROPPED-BLANK-CHAIN — R3-N1 (inherited from R2) · **LIVE AT HEAD** · re-run this session
- **base**: real `memory/DECISIONS.md`.
- **ours**: appends, at the end of the `## TOOL` block, five lines —
  `> a note that legitimately repeats` / `TOOL-zOne-<n>` / `TOOL-zTwo-<n>` /
  `> a note that legitimately repeats` / `TOOL-zThree-<n>`. (Row 1 and row 3 each carry the note as
  lead-in; row 2's lead-in is blank.)
- **theirs**: edits **preamble prose only** (e.g. one `>` routing line).
- **driver @ HEAD**: rc 0, `38 row(s) from ours, 0 new from theirs, 0 dropped … clean`, 0 markers,
  **1 copy of the note where ours had 2**. R3 confirmed end-to-end: real `git merge` committed
  `bb64ca8` with diffstat `1 insertion(+), 2 deletions(-)` from a preamble-only incoming change.
  Re-run standalone this session: identical.
- **control**: `git merge-file` → rc 0 with **both** copies.
- **verdict**: CORRUPTION. Content loss at rc 0 from an incoming change that touched nothing near it.
- **covered**: **no**.
- **mechanism**: the blank-lead-in exemption, `merge-rows.py:551` — `if not sig: return list(got)`
  returns before `prev_new_sig` is reset, so a furniture-less row does not break the adjacency chain
  and the suppression reaches across it. R3 mutated the exemption so a blank lead-in *breaks* the
  chain: suite still `PASS — 28 fixture groups held`, output demonstrably different (2 notes vs 1) —
  the branch is unarmed and non-equivalent.

### C5 · MISFILE-APPEND-PAST-BLOCK — R1-B5
- **base**: real `memory/DECISIONS.md`.
- **ours**: inserts a TOOL row inside `## TOOL`.
- **theirs**: inserts a PLAY row inside `## PLAY`.
- **driver (R1)**: rc 0, `clean`, 0 markers, the PLAY row emitted at line 90 — under `## TOOL`
  (heading at 13, next heading at 91).
- **control**: same two inserts through `git merge-file` → **rc 0, PLAY row at line 10, correctly
  under `## PLAY`**. U5 *introduced* the misfiling.
- **verdict**: CORRUPTION.
- **covered**: yes — group 11 ("a `%B`-only row in a non-final section stays inside its section").
- **mechanism**: `for k in b_order: out.extend(B[k])` appended every theirs-only row after **all** of
  ours' rows; position survived only when the incoming row was the first of its section. Replaced by
  the splice.

### C6 · MISFILE-OURS-UNDER-THEIRS-NEW-HEADING — R2-B2 direction one
- **base**: real `memory/DECISIONS.md`, `## KICK` empty.
- **ours**: appends `PLAY-aNewOurs-<n>` inside `## PLAY`.
- **theirs**: opens `## KICK` with `KICK-bNewTheirs-<n>` (so theirs' row carries the `## KICK`
  heading as its lead-in).
- **driver (R2)**: real `git merge`, rc 0, `36 row(s) from ours, 1 new from theirs … clean`,
  0 markers, tree clean — **the PLAY row committed under `## KICK — kickoff`**.
- **control**: same two commits with `merge.rows.driver` unset → rc 0, 0 markers, PLAY row under
  `## PLAY`, **correct**.
- **verdict**: CORRUPTION.
- **covered**: yes — group 14 ("a `%B`-only row that opens the next section must not swallow ours'
  own new row"), which runs the live `git merge-file` control and byte-compares.
- **mechanism**: the splice seated its cursor with `at = order.index(k)` on keys shared with `%A`
  only and always inserted at `at + 1`. Fixed by splicing past the `%A`-only keys that already follow
  the shared predecessor.

### C7 · MISFILE-BEHIND-A-MOVED-NEIGHBOUR — R2-B2 direction two
- **base**: row block with two `## ` sections.
- **ours**: relocates a shared row across a `## ` boundary (or honours a delete on it).
- **theirs**: adds a new row immediately after that shared row.
- **driver (R2)**: real `git merge`, rc 0, `clean`, 0 markers, `- TOOL-bNine-<n>` committed under
  `## closed`.
- **control**: `git merge-file` **refuses** the same input (rc 1).
- **verdict**: was CORRUPTION; now CONSERVATIVE at HEAD — the `no_misfiled_rows` postcondition
  catches it and the run fails closed.
- **covered**: yes — group 15 ("placement the splice cannot decide is a conflict, never a guess").
- **mechanism**: the cursor sits at **ours'** position for the shared key, so ours' move drags theirs'
  new row with it. The splice cannot decide this shape; the postcondition is the answer.

### C8 · CROSS-SECTION-MOVE-DISCARDED — R2-N1 · **LIVE AT HEAD** (dossier §Gaps)
- **base**: a shared row in section X.
- **ours**: leaves it alone.
- **theirs**: moves it to section Y.
- **driver**: rc 0, `4 row(s) from ours … clean` — **theirs' move silently discarded**.
- **control**: `git merge-file` **refuses**, rc 1.
- **verdict**: CORRUPTION (silent revert of a deliberate change), rated LOW today because the backlog
  shards carry no `## ` sections and `DECISIONS.md` is append-only in practice.
- **covered**: **no**.
- **mechanism**: `order` is seeded from `a_order` and shared keys are never repositioned.
  `no_misfiled_rows` cannot see it — it asks whether the merged section matches *an* input that
  carries the row, and ours' does.

### C9 · DELETE-EATS-ADJACENT-CONTENT — R2-B1 (both directions)
- **base**: 3 rows.
- **ours**: deletes row 2.
- **theirs**: inserts `- TOOL-zFixture-<n>b · OPEN · correction row from node b` immediately **above**
  row 2 (an unkeyable line, so it is row 2's lead-in).
- **driver (R2)**: rc 0, `2 row(s) from ours, 0 new from theirs, 1 dropped (delete honoured), clean`,
  0 markers — **the incoming row is GONE**; result holds rows 1 and 3 only.
- **control**: `git merge-file` → rc 1, row preserved. **Pre-repair driver at `bde0de8`** → rc 1,
  row preserved, 1 marker. A regression introduced by the round-2 repair.
- **verdict**: CORRUPTION.
- **covered**: yes — group 13, both directions ("ours deleted, theirs filed above it" and the mirror),
  each asserting rc 1.
- **mechanism**: splitting lead-in from anchor narrowed both delete comparisons to the anchor line, so
  a side that left the row untouched but filed something above it read as "untouched" and the
  `continue` skipped `lead(k)`. Fixed by comparing the whole row (`a_lead[k] == o_lead[k]` alongside
  `o_txt == a_txt`, and the mirror). Note the audit line **cannot report this class**: the lost
  content is unkeyed, so it lands in neither `kept` nor `took_b`.

### C10 · DUP-UNKEYABLE-ROW-SAME-TEXT — R1-B3(b) · control re-measured this session
- **base**: real `memory/DECISIONS.md`.
- **ours**: files `- TOOL-zFix-<n>b · CORRECTS TOOL-zFix-<m>: …` high in the `## TOOL` block.
- **theirs**: files the **byte-identical** line low in the same block (different region).
- **driver (R1)**: rc 0, `35 row(s) from ours, 0 new from theirs, 0 dropped … clean`, the id present
  **twice** (lines 88 and 93).
- **control (re-run this session on the real file)**: `git merge-file` → **rc 0, 0 markers, the row
  written TWICE**. This is the one shape where git itself corrupts, and it is the justification for
  the driver existing at all.
- **driver @ HEAD (re-run this session)**: `FAILED (DuplicatedContent: 1 row line(s) would be written
  more often than any single input carries them … x2 against x1)`, rc 1 — fails closed.
- **verdict**: CORRUPTION at R1; **git is equally wrong here**, so R1's driver was not worse than git,
  it merely failed to deliver the property it claimed. At HEAD: correct (refusal).
- **covered**: yes — group 12 ("an unkeyable row minted on both nodes, in different regions", rc 1),
  plus its one-side-only companion at rc 0.
- **mechanism**: the anchor grammar keys 35 of 73 rows; the other 38 travel as lead-in/trailer, i.e.
  as content a line merge can copy. Closed by the **line half** of `no_new_duplicates` (no
  `^\s*[-*]\s` line written more often than the most any one input carried it).

### C11 · DUP-SAME-ID-DIFFERENT-WORDING — R2-B3
- **base**: 2 rows.
- **ours**: appends `- TOOL-zFix-<n>b · CORRECTS TOOL-zFix-<m>: the ours-side wording`.
- **theirs**: appends `- TOOL-zFix-<n>b · CORRECTS TOOL-zFix-<m>: the theirs-side wording`
  (**same id, different prose** — two different *lines*).
- **driver (R2)**: rc 0, `2 row(s) from ours, 0 new from theirs, 0 dropped … clean`, 0 markers,
  the id present twice. The suite's own `dups()` oracle sees it; no fixture ran the shape.
- **control**: **not recorded in any round.** Presumed to duplicate as in C10; treat as unmeasured.
- **verdict**: CORRUPTION.
- **covered**: yes — group 16 ("the same suffixed id minted on both nodes, with different wording").
- **mechanism**: the census keyed on stripped **line text**. Closed by the **id half** — each
  row-shaped line is also keyed on the **first** id it carries under `_ID_RE`
  (`\b[A-Z]+-[A-Za-z0-9]+-[0-9]+[a-z]*\b`), first id only because rows cite other records constantly.

### C12 · DUP-HIDDEN-BY-AN-UNRELATED-CONFLICT — R2-B5
- **base / ours / theirs**: the C11 duplicate **plus** one unrelated both-sides edit of a different
  row anywhere in the file.
- **driver (R2)**: rc 1 `CONFLICT`, and the duplicated row written **outside** the markers —
  `no DuplicatedContent on stderr, the postcondition never ran`. The same duplicate without the
  unrelated conflict correctly refused.
- **control**: not recorded.
- **verdict**: CORRUPTION. An author resolves the marked hunk and reads the rest as settled, so a
  duplicate outside the markers is exactly as invisible at rc 1 as at rc 0.
- **covered**: yes — group 18 ("an unrelated conflict must not switch the duplicate detector off").
- **mechanism**: the postcondition ran only `if verdict == "clean"`. Fixed by running all three
  postconditions on **every** verdict over `settled()` — the merged lines with conflict regions
  excised (excision is what handles a hunk's by-construction repetition).

### C13 · DUP-SMUGGLED-BY-LINE-FORM — R2-B7(b) (coverage hole, not a live break)
- **base / ours / theirs**: two nodes minting the same unkeyable row, where theirs' copy is the
  **final line with no trailing newline**.
- **driver**: shipped code correct (rc 1, `DuplicatedContent`). With `census()`'s `strip()` replaced
  by the raw line: rc 0 `clean`, the row x2 — and `merge-rows.test.sh` still printed
  `PASS — 20 fixture groups held`.
- **verdict**: not corruption at HEAD; an **unarmed branch that changes real output**.
- **covered**: yes — group 20 ("the census keys on the stripped line, so line form cannot smuggle a
  duplicate in").
- **note**: the docstring's original claimed channel (a CRLF side against an LF side) is **not** the
  live one — git hands the driver uniformly-terminated `%O`/`%A`/`%B` under either `core.autocrlf`.
  Build on **line form**, not on CR.

### C14 · HEADING-RENAME-vs-ROW-EDIT — R2-B7(a) (coverage hole)
- **base**: a `## ` heading inside the row block, above a row.
- **ours**: edits the row.
- **theirs**: renames the heading.
- **driver**: shipped code correct (rc 0, both survive). Replacing `lead()`'s `k in O` three-way with
  `return list(a_lead.get(k, o_lead[k]))` silently discards theirs' rename at rc 0 and the suite
  still printed `PASS — 20 fixture groups held`.
- **verdict**: unarmed branch; the property is real and must survive any redesign.
- **covered**: yes — group 19 ("a heading renamed on theirs survives a row edited on ours").

### C15 · INERT-ON-SUFFIXED-IDS — R1-B3(a) · **LIVE AT HEAD** · re-verified this session
- **base / ours / theirs**: two nodes each appending a **different** `…-<n>b` correction row.
- **driver**: **CONFLICT (rc 1)**, where the identical appends with plain numeric ids auto-resolve
  clean (rc 0). Over half the index (38 of 73 rows) never enters the keyed path at all.
- **control**: git conflicts on the same-insertion-point append too (measured this session: rc 1,
  1 marker), so git is no better here.
- **verdict**: CONSERVATIVE — but it means the auto-resolve the unit exists for is unavailable for
  the majority of the file's rows.
- **covered**: **no** — and it cannot be seen by the current oracle for a second reason: the test's
  "independent" id oracle was originally `\b[A-Z]+-[A-Za-z0-9]+-[0-9]+\b`, which fails the same
  boundary. Group 0d now proves the widened oracle strictly wider than the driver's grammar and
  proves `dups()` fires.
- **mechanism**: `extract.py:73`'s session era `[a-z][A-Za-z]{2,}-\d+` is bounded by `\b`, so a
  trailing letter kills the match. R1's prescribed widening (`…-\d+[a-z]*`) was **not applied** —
  re-measured at HEAD: 91 lines, 73 rows, **35 anchored, 38 unkeyed**.

### C16 · TWO-DIFFERENT-EMPTY-SECTIONS — R2-N2 · **LIVE AT HEAD** (dossier §Gaps)
- **base**: two different empty sections inside the row block, each `## FAMILY` + `*(none yet)*`.
- **ours**: opens section X with its first row.
- **theirs**: opens section Y with its first row.
- **driver**: rc 1, one heading emitted twice inside a whole-file `DuplicatedContent` conflict, both
  rows correctly filed.
- **control**: `git merge-file` → **rc 0, correct**.
- **verdict**: CONSERVATIVE (fails closed, nothing lost) — but still worse than the merge it replaces.
- **covered**: **no**. Unreachable on today's corpus only because `## DEPL` sits in the trailer;
  reachable the moment a family is added ahead of the last one.
- **mechanism**: each side's lead-in for its new row is a different, overlapping slice of the same
  base furniture, so the adjacency dedup suppresses neither. Closing it means merging lead-ins as
  text against the base rather than picking one.

### C17 · WHOLE-FILE-REFUSAL — R3-N3 (dossier §Gaps, ergonomics)
- **input**: any postcondition violation, e.g. ours fills the `## KICK` placeholder while theirs
  appends `PLAY-zTheirsRule-<n>`.
- **driver**: rc 1, `FAILED (Misfiled: … under "## KICK — kickoff" against ["## PLAY — playbook"])`,
  **186 lines** for a ~90-line index, one marker pair, each row present exactly once.
- **control**: `git merge-file` rc 0, 92 lines.
- **verdict**: CONSERVATIVE. Nothing lost or corrupted; heavy. R3 spot-checked this class end to end
  and refuted 13 of 15 survivors on exactly this distinction.
- **covered**: partially (groups 15, 12, 16, 18 all assert rc 1); the *ergonomics* are not gated.

---

# B. Wiring / observability cases (outside `merge()`, still in the acceptance suite)

### C18 · DRIVER-CANNOT-START → SILENT TAKE-OURS — R1-B2 + R1-B6 State A
- **input**: any conflicting merge, with `merge.rows.driver` set to a command that cannot start.
  Two reproduced causes: (i) the kit README published a mixed-prefix command naming a driver that
  exists in neither install layout; (ii) `tools/lib/resolve-python.sh` moved aside
  (`resolve_python: command not found`).
- **observed**: git prints `CONFLICT (content)`, the driver never writes `%A`, so the path holds
  **ours-only content, `grep -c '<<<<<<<' = 0`, status `UU`**. An author who sees "conflict", opens
  a marker-free file and `git add`s it has silently dropped every incoming row.
- **control**: n/a — this is the failure the driver's own docstring names "silent, unrecoverable loss".
- **verdict**: CORRUPTION, and the worst class in the corpus (unrecoverable, no signal).
- **covered**: partially — group 0b (the shim's contract), group 0c (every deferred-resolution failure
  becomes a conflict, never a take-ours), group 0a (the driver parses under the interpreter the shim
  resolves). `check-wiring.sh` now runs a smoke three-way before printing `ok` (R2 confirmed deleting
  it reds 4 assertions). The published README literal is now gated (AC12).
- **redesign requirement**: the wiring arm must **execute** what it validates; every start failure
  must become markers, never a take-ours.

### C19 · WIRING-SMOKE-VACUOUS / FAMILIES-DRIFT-INERT — R2-B7(c) · closure **UNVERIFIED**
- **input**: `.memory-tree.conf` FAMILIES drift by one token (`tooling:TOOL` → `tooling:TOOLS`), so
  the driver keys **zero** rows and every governed append-collision conflicts forever.
- **observed (R2)**: `check-wiring.sh` still printed `ok merge — merge.rows.driver wired`, because its
  smoke fixture was `x` / `a\nx` / `x\nb` — no anchor, so `split_regions()` made the whole file
  preamble and the run was a plain `git merge-file`; `rows()`, `merge()`, `lead()`, the splice and the
  postconditions were never entered.
- **verdict**: CONSERVATIVE at merge time (inert, loud), but the wiring arm **lies**.
- **covered**: R3's subject commit adds "one new `check-wiring.sh` state"; R3's question was scoped to
  new content-corrupting regressions and it did **not** re-verify this. Treat as open until re-run.
- **redesign requirement**: the smoke inputs must carry one anchored row each (`%A` appends a second,
  `%B` a third) and require rc 0 with all three ids present exactly once.

### C20 · ATTRIBUTE-UNGATED — R1-B7 (closed)
- **input**: delete the two `.gitattributes` `merge=rows` lines.
- **observed (R1)**: `git check-attr merge` → `merge: unspecified`, bar still green (38 of 39 legs;
  the one red was a clone artifact reproducing with the lines restored). Group 9 wrote its **own**
  `.gitattributes` in a scratch repo, so it proved the driver works against an attribute it invented.
- **verdict**: observability. Un-wiring the driver silently reverts every node to git's line merge —
  i.e. to **C10's** duplication, at rc 0.
- **covered**: closed by the repair — R2 confirmed commenting one line out reds AC11.

### C21 · AUDIT-LINE-DOES-NOT-RECONCILE — R1-N2 (+ R2-B1's corollary) · **LIVE AT HEAD**
- **input (a)**: any both-sides conflict on one row. The branch writes **both** rows but increments
  `kept` once → printed `1 row(s) from ours, 0 new from theirs … CONFLICT`, rc 1, while
  `grep -c '^- TOOL-'` on the written file = 2.
- **input (b)**: any loss of **unkeyed** content (C4, C9). Re-measured this session on C4: the audit
  line read `38 row(s) from ours, 0 new from theirs, 0 dropped … clean` while a line was deleted.
- **observed**: the module's only output is unreconcilable in exactly the regimes that matter.
- **verdict**: observability defect. The comment at `merge-rows.py:651` still asserts
  `kept + took_b` is the anchored-row count of the file just written.
- **covered**: **no at rc 1** — group 8's `audit()` helper does assert
  `kept + took == grep -c '^- TOOL-'`, but all three call sites pass `want_rc 0`, so the only regime
  that can break the equality is never exercised. Unkeyed loss is unrepresentable in the line at all.

### C22 · LF-MARKERS-INTO-A-CRLF-FILE — R2-N3 (dossier §Gaps)
- **input**: any fail-closed path on a CRLF worktree file.
- **observed**: `lines: 13 | without CR: 3` — `<<<<<<< ours`, `=======`, `>>>>>>> theirs (…)` written
  with LF into an otherwise all-CRLF file. Group 7b's CR:LF assertion covers **clean** merges only.
- **verdict**: cosmetic (marker lines are deleted during resolution), but it is a real asymmetry
  against the four newline sites the driver is otherwise strict about.
- **covered**: **no** (no rc-1 arm on 7b).

---

# WHAT THE CONTROLS SHOW

`git merge-file -p -L ours -L base -L theirs` on the identical three blobs, every case where a
control was recorded or measured:

| case | content class | git rc | git result | correct? |
|---|---|---|---|---|
| C1 doubled heading, simple | furniture + first row | 1 | one hunk, heading x1 | yes (refused) |
| C2 doubled heading, middle row | furniture + rows | 1 | heading x1, refuses | yes (refused) |
| C3 repeated `### ` in two sections | furniture | 0 | both sub-headings, both rows | **yes (resolved)** |
| C4 repeated note lead-in | furniture | 0 | both note copies | **yes (resolved)** |
| C5 misfile, append past block | rows in two sections | 0 | both rows in their own sections | **yes (resolved)** |
| C6 ours under theirs' new heading | furniture + rows | 0 | both rows correctly filed | **yes (resolved)** |
| C7 behind a moved neighbour | rows | 1 | refuses | yes (refused) |
| C8 cross-section move | rows | 1 | refuses | yes (refused) |
| C9 delete vs adjacent insert | rows + lead-in | 1 | row preserved | yes (refused) |
| C10 same unkeyable row, two regions | **rows** | **0** | **the row written TWICE, 0 markers** | **NO — silent duplication** |
| C15 append collision, same point | rows | 1 | one marker | yes (refused) |
| C16 two different empty sections | furniture | 0 | correct | **yes (resolved)** |
| C17 postcondition-refusal shapes (13 of 15 R3 survivors) | mixed | 0 | 92 lines, correct | **yes (resolved)** |

Plus two non-`merge-file` data points on git's own line merge:
- R1-N3: with `merge=rows` declared and `merge.rows.driver` unset, git 2.54 emits **0 bytes** of
  warning and, in the auto-resolving regime of that same run, **silently duplicated a row at rc 0**.
- Upstream replay quoted in the docstring: `merge=union` never LOSES an id (0 of 441) but INTRODUCES
  a duplicate in **147 of 151** `DECISIONS.md` conflicts and 118 of 121 backlog conflicts. Note this
  measures **union**, not the built-in three-way — weaker evidence than it reads as.

## Verdict on the working hypothesis

**CONFIRMED, with three carve-outs.**

Across 13 recorded/measured controls, git was **never observed to corrupt non-row content**. On
furniture it either resolved correctly (C3, C4, C6, C16, and the C5/C17 mixed cases) or refused
loudly with the structure intact (C1, C2, C7, C8, C9, C15). Its single observed corruption — measured
twice, once by R1 and once directly in this session on the real file — is a **row line duplicated at
rc 0** (C10), which is precisely the keyed-row population the driver is supposed to own. Git also
never LOST content in any recorded case; every driver case in class CORRUPTION that involves *loss*
(C4, C9) is one git got right.

So "delegate non-row content to `git merge-file`, key-merge only the row set" is supported by the
evidence. **What it does not cover:**

1. **The partition must be the row SHAPE, not the anchor grammar.** 38 of 73 `- ` lines in the live
   file do not key (C15, re-verified at HEAD). If "row set" means "anchored rows", the redesign hands
   git exactly the lines git duplicates (C10, C11). The split has to be `^\s*[-*]\s` — which is what
   `_ROW_RE` already is — with the id postcondition on top.
2. **Furniture that RIDES WITH a row is neither side of the partition.** C1/C2 (the `## FAMILY`
   heading + `*(none yet)*` placeholder consumed by the first row of an empty section), C3/C4 (a
   lead-in that legitimately repeats) and C16 all live exactly on that boundary, and they are 4 of the
   corpus's 13 corruption cases. Delegating them to git costs the driver's **headline** auto-resolve:
   git refuses C1 and C2 (rc 1). Any delegating design must say what happens to lines that sit between
   two rows inside the row block, and must be measured against C1/C2/C3/C4/C16 as a set — fixing one
   by narrowing a guard is what produced C2 out of C3.
3. **Deletes and moves are row-class but git refuses them** (C7, C8, C9). Pure delegation loses the
   honour-a-delete auto-resolve (group 4) and re-introduces nothing; that is a conservative trade, but
   it must be a stated one.

Not established by any evidence here: that a strip-non-rows → `git merge-file` → re-key pipeline
preserves blank-line structure. A probe of that shape was attempted this session and was **invalid**
(it read a `%A` the driver had already overwritten); nothing was learned and nothing should be
inferred. Removing rows changes the context lines git's diff aligns on, so the residue merge is not
obviously the same merge — measure it before designing on it.

---

# STILL OPEN

## Recorded in `memory/map/features/memory-tree-merge-driver.md` §Gaps
1. **Not packaged for adopters.** `adopt-memory-tree.sh` untouched; a copy-installed kit lands at
   `<root>/memory-tree/` and cannot reach `tools/lib/pyrun.sh`. The driver resolves both layouts, so
   this is packaging, not a rewrite. (Related and separate: R1-N4 — `merge-rows.test.sh:20` resolves
   `ROOT` as `$HERE/../..`, which is the parent of the repo root at the adopter prefix, producing
   `FAIL no usable python on this host` for a path bug. Second-hand; not re-run.)
2. **The grammar is read from the PRE-merge worktree.** A merge that itself changes `FAMILIES` keys
   its index merge on the old grammar.
3. **Conflict markers are LF into a CRLF file** — C22.
4. **A postcondition refusal is a WHOLE-FILE conflict, not a scoped hunk** — C17.
5. **Two DIFFERENT empty sections still conflict where git resolves** — C16.
6. **A `%B` cross-section MOVE of a shared row is discarded at rc 0** — C8.
7. **No `regenerate` driver, and there will not be one** — `ort` checks the result out only after the
   per-path merges run, so a generator inside a driver renders from the pre-merge tree.

## Live defects at HEAD not in §Gaps
- **C2** doubled heading via the middle-row path (R3-B1, blocking, reproduced this session).
- **C4** a legitimately repeated lead-in deleted at rc 0 (R3-N1; inherited from round 2, **not**
  among the disclosed Gaps, and it falsifies the round-3 commit's headline claim).
- **C15** the driver is inert for 38 of 73 rows; `extract.py`'s session era was never widened.
- **C21** the audit line does not reconcile at rc 1 and cannot represent unkeyed loss.

## Unarmed branches (mutation survives the 28-group suite)
- The **blank-lead-in exemption** at `merge-rows.py:551`. R3 mutated it so a blank lead-in breaks the
  adjacency chain: suite `PASS — 28 fixture groups held`, output demonstrably different (2 note copies
  vs 1). The mutant actually *removes* C4's loss.
- **rc-1 audit reconciliation** (group 8 has no `want_rc 1` call site).
- **rc-1 line-ending discipline** (group 7b asserts CR:LF on clean merges only).

## Left UNVERIFIED by the reports
- **"845 in-process replays over every historical triple → 0 dropped ids."** R1 §4 flags this
  explicitly: nobody re-ran it. **"The driver never DROPS a row" is UNPROVEN** — and C4 and C9 are
  measured drops, so treat it as falsified for those shapes.
- **C19** — whether round 3's new `check-wiring.sh` state actually closes the vacuous smoke. R3's
  question was scoped to content-corrupting regressions and did not re-check it.
- **C11's control** — `git merge-file` behaviour on the same-id/different-wording triple was never
  measured in any round.
- **C12's control** — never measured.
- `_ID_RE`'s docstring claims it is "deliberately WIDER" than the anchor grammar; measured (R3-N4) it
  is wider for the session era only and **narrower** for the two flat eras (flat-numeric ids key but
  do not match `_ID_RE`). Zero reachability on this corpus (0 of 91 governed rows carry a flat id) —
  a comment defect today, a hole for any adopter using flat ids.
- Second-hand in R1 and never re-run by its author: the adopter-fixture false red behind N1
  (`check-memory-hygiene.sh:234`, pop_guard 3's bare `.txt` precondition), the State A/B
  `check-wiring` reproductions, the `.gitattributes`-deletion clone run, the git-2.54 zero-stderr
  measurement, the `similarity index` measurements behind N5, and the adopter-prefix `ROOT` failure
  behind N4.
- **R2-N4** — the kit README's wiring doctrine ("`check-wiring.sh` sets exactly one of the two
  commands"; a mixed-prefix command "names a driver that exists in neither layout") is false for the
  only layout `WIRE-INTO-PROJECT.md` actually produces, where the mixed spelling works. Not corrupting;
  never re-checked.

## Out of scope for this corpus (found in the same rounds, not driver defects)
R1-B4 (drift-audit `DECLARED_EMPTY` muzzle arm — closed by the repair, R2 sabotaged it and watched it
red), R1-N1 (hygiene pop_guard 3 precondition), R1-N5 (master AC2 unsatisfiable), R2-B6 (the bar was
red because a committed report spelled two fixture ids verbatim — the reason this file elides every
trailing numeral), R2-B2's spec half (both ratified decision tables still read
`| id in %B only | append |` while the code splices; nothing on the bar compares the two).

---

# Fixture-group coverage map (`merge-rows.test.sh`, 28 groups at HEAD)

| group | what it holds | corpus case |
|---|---|---|
| 0 / 0a / 0b / 0c / 0d | oracle liveness · driver parses · shim contract · fail-closed on every deferred-resolution failure · oracle strictly wider than the grammar + `dups()` fires | C18 (partial), C15 (partial) |
| 1 | disjoint appends — the case the unit is FOR | — |
| 2 | same id, different text, both sides | — |
| 3 | one side edits, the other does not | — |
| 4 / 4b / 4c | delete honoured · delete/modify both directions · marker labels | C9 (partial) |
| 5 | an unkeyable line inside the row block keeps its position | C1 (insufficient — position preserved, never copied) |
| 6 | empty `%O` | — |
| 7 / 7b | identity on the real index · preamble three-way in both line-ending flavours | C22 (clean only) |
| 8 | the audit line reconciles with the written file | C21 (rc 0 only) |
| 9 | end-to-end two-branch `git merge` through the real wiring | C20 |
| 10 | both nodes open the same empty section | **C1** |
| 11 | a `%B`-only row in a non-final section | **C5** |
| 12 | an unkeyable row minted on both nodes, in different regions | **C10** |
| 13 | an honoured delete must not swallow adjacent content, both directions | **C9** |
| 14 | a `%B`-only row opening the next section must not swallow ours' new row (live `merge-file` control) | **C6** |
| 15 | placement the splice cannot decide is a conflict | **C7** |
| 16 | the same suffixed id on both nodes, different wording | **C11** |
| 17 | a lead-in that legitimately repeats in two sections (live `merge-file` control) | **C3** |
| 18 | an unrelated conflict must not switch the duplicate detector off | **C12** |
| 19 | a heading renamed on theirs survives a row edited on ours | **C14** |
| 20 | the census keys on the stripped line | **C13** |
| — | **no group** | **C2, C4, C8, C15, C16, C19, C21, C22** |

Only groups 14 and 17 run a live `git merge-file` control. Every case in this corpus should.
