**Serves:** diff-review TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-17 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-21

# Review round 4 — the fix range for round 3's fifteen defects

**Range:** `ebe5012577271a86bed653739e267c4049560995...4f850cb` (one commit: `4f850cb`, "round 3's fifteen — nine were one carrier of a pair").
**Round:** 4.
**Kind:** FIX REVIEW OF A FIX REVIEW. The underlying build was not re-reviewed and neither were the round-1/2/3 fixes. The only question asked of every hunk is whether *this* commit's fix is correct, complete across its paired carriers, and free of a new instance of the class it closes.

## Verdict: BLOCKED

**Shape:** raw 30 · confirmed 25 · refuted 5 · unverified 0 · precision 0.83. The 25 confirmed fold to **15 distinct defects** after collapsing cross-lens duplicates; the fold is recorded in the `dup` column of each finding.

**Why BLOCKED:** two merge-bar legs are measured RED at `4f850cb` in this worktree, right now.

- `bash tools/memory-tree/check-verdict-epoch.sh` exits 1 — the commit moved 8 behaviour-bearing lines of the hygiene engine without bumping `KIT_MEMORY_TREE_VERSION` (B1). The leg has no guard in `tools/gate-legs.json`, so it runs on every bar invocation.
- `bash tools/memory-tree/check-memory-hygiene.sh` prints `HYGIENE check 9 FAILED — generated build index differs from a fresh render` — the commit added its own round-3 review record without regenerating the build index (B2).

Both are one command each to fix. Neither is subtle. Both are the same shape: a DoD step the commit skipped while fixing other people's skipped DoD steps.

**The pattern held, and it is still the dominant one.** Round 3 named it: nine of fifteen defects were a fix applied to one of two or three paired carriers. This round, **six of fifteen** are the same shape — BUILD-METHOD's two copies (H2), `.memory-tree.conf`'s stale comment beside the value the commit edited (M1), `recall-opened.test.sh` as the second `mktemp` carrier (L3), the `ls-remote` rc classification the driver already has one file over (M3), the derived-count arm the memory-tree sibling already carries (M2), and `push-main.sh` vs `unattended.sh` on `LANDER_MARKER` (L4). The commit message says it was hunting this class. It found nine of them and left six.

**The build's own theme reappears twice.** `is_published`'s new third answer (H1) is gated on a condition that makes it unreachable in the normal case, and its fixture structurally cannot reach the gap. The `marker-contract` case table (M4) gained no row for the divergence the commit just fixed, so reverting the fix leaves the harness green. A check that cannot fail, landed in the fold whose subject is checks that cannot fail — for the second consecutive round.

---

## Blockers

### B1 — the hygiene engine changed without a version bump, so the `verdict epoch` leg is RED
`tools/memory-tree/check-memory-hygiene.sh:909` · dup: id 13

`git show 4f850cb -- tools/memory-tree/check-memory-hygiene.sh` moves 8 behaviour-bearing lines: the `q8` trim/`tolower` and three `N/A` comparisons. `KIT_MEMORY_TREE_VERSION` was not bumped in the same commit.

Measured: `bash tools/memory-tree/check-verdict-epoch.sh` exits 1 with *"the bump is OLDER than the change it claims to date — last behaviour-bearing engine change: 4f850cb (8 lines) … last KIT_MEMORY_TREE_VERSION change: 19d33e9"*. The leg is `tools/gate-legs.json:102` ("verdict epoch (kit version dates the engine)") with no guard clause, so the push-boundary bar fails. `hygiene-parity.test.sh`'s derived baseline floor now points at a commit from before this verdict change.

**Fix.** Bump the constant in the three places the gate names, in a commit at or after `4f850cb`: `check-memory-hygiene.sh:13` (the value AND the `gov:kit memory-tree@…` marker on that same line), `tools/memory-tree/HYGIENE.template.md` line 1, `memory/HYGIENE.md` line 1. Then `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.

**Left-shift.** The gate already exists and already caught this. What is missing is that it caught it *after* the commit. Add the verdict-epoch leg to the pre-commit fast leg's set when the staged diff touches `tools/memory-tree/check-memory-hygiene.sh`, so the refusal lands before the commit object exists rather than at the push boundary.

### B2 — a review record was added without regenerating the build index, so hygiene check 9 is RED
`memory/builds/aBoundedVerdict/reviews/2026-08-21-review-TOOL-aBoundedVerdict-1-round3.md:1` · dup: ids 9, 14

The commit tracks the round-3 review record and does not regenerate `memory/builds/aBoundedVerdict/README.md`.

Measured two ways. In this worktree: `bash tools/memory-tree/check-memory-hygiene.sh` prints `HYGIENE check 9 FAILED — generated build index differs from a fresh render: memory/builds/aBoundedVerdict/README.md (stale)`. On a clean extraction (`git archive 4f850cb` into scratch, `git init`, then `gen_build_index.py --check`): `build-index DRIFT … (stale — differs from a fresh render)`, rc=1. `--write` on that clean tree adds exactly two rows the committed README lacks — the `gen:build-index` row and the `gen:build-docs` link for the round-3 review file. `git show 4f850cb:memory/builds/aBoundedVerdict/README.md | grep -c round3` returns 0.

AGENTS.md §1's DoD requires claim edits to regen generated artifacts in the same commit. This is the second generated-artifact drift in three commits in this range.

**Fix.** `python tools/memory-tree/gen_build_index.py --write`, and include `memory/builds/aBoundedVerdict/README.md` in the commit.

**Left-shift.** A pre-commit arm: if the staged set adds or removes any file under `memory/builds/*/reviews/`, `*/spec/` or `*/build/` and does NOT stage the sibling `README.md`, refuse. That is the whole class, and it is cheaper than discovering it at the bar for the third time.

---

## High

### H1 — `is_published`'s new CANNOT-TELL answer is half-applied and unreachable in the normal case
`tools/unattended/check-unattended.sh:505` · dup: ids 1, 8, 16

The fix adds a third answer (rc=2, "cannot be observed") so an unfetched clone stops accusing honest records of forgery. But `have` is a single OR across `ADV_HEAD` plus every tip in `ADV_TIPS`, so rc=2 requires that **no** advertised tip is local. One stale locally-present branch — the normal state of any clone that has ever fetched a sibling branch — restores the definitive negative answer, which routes at `:661-668` to *"it names a commit that exists only where this run could have authored it"*.

Reproduced against this clone's live advertisement, today. `git ls-remote --heads origin` advertises three tips: `c2b3576` PRESENT locally, `4bd2a45` ABSENT, `refs/heads/main` `381345d` ABSENT — and `ADV_HEAD` resolves to the missing `381345d`. Slicing the shipped function body (`:494-506`) and feeding it those values, an unpublished commit returns **rc=1, not rc=2**. Deleting the one present tip from `ADV_TIPS` returns rc=2. Also reproduced in a scratch repo (origin with `main`+`sidebr`, `main` advanced only in the bare repo, clone holding `sidebr` but not the new `main` tip): rc=1.

The bar is green today by coincidence: the recorded BASEs (`43a6c13`, `ee9a590`) happen to be ancestors of the one present tip. The verdict on any recorded BASE currently depends on which branch that BASE sits under — which is precisely the network-timing red the fix's own comment ("sixteen records, every one of them honest, all sixteen red") was written to kill.

The check-9 fixture at `check-unattended.test.sh:513-520` builds ONE ghost tip inside the bare origin and asserts it is absent, so ALL advertised tips are absent in the fixture. It structurally cannot reach the mixed case.

**Fix.** Track absence, not just presence:

```sh
local c="$1" t miss=0 have=0
# ... on the ADV_HEAD guard and inside the ADV_TIPS loop:
GIT cat-file -e "$t^{commit}" 2>/dev/null || { miss=1; continue; }
# ... before the final:
[ "$miss" = 0 ] || return 2
return 1
```

The sound invariant is "no present tip contains it AND every advertised tip was readable" → not published; anything less → cannot tell. The driver already uses that shape at `unattended.sh:516`, where it refuses outright on the one tip it needs rather than falling back on another.

**Left-shift.** A fixture arm advertising **two** tips — one built inside the bare origin (absent locally) and one the clone has — with a BASE on neither, asserting the CANNOT-BE-OBSERVED message. The single-branch scratch origin is what let this through; the arm that pins the fix must be the mixed one.

### H2 — BUILD-METHOD still teaches the per-ITEM §8 rule this commit withdrew, in both carriers
`memory/guides/BUILD-METHOD.md:100` and `tools/memory-tree/BUILD-METHOD.template.md:100` · dup: ids 2, 17, 24

Both files, byte-identical at lines 100-102, read:

> **Every ITEM is graded, not the section's first line** … A `none` first line ends the section only when it has NO items; below one, an unresolved item still reds.

Both readers now do the opposite. `check-memory-hygiene.sh:965-977` builds one whitespace-squeezed `bblob` over the whole section and sets `bmark` from a single regex over it — no per-item walk — and `q8 ~ /^none/` short-circuits before `bmark` is consulted. `unattended.sh:1265-1268` is `if (lf ~ /^none/ || lf ~ /^n\/a/ || any_mark) print "READY"`.

`memory/TEMPLATE-SPEC.md:180-190`, rewritten by **this same commit**, says the opposite in as many words — "They do not grade PER ITEM" — and names the below-`none` case as a pinned gap. `marker-contract.test.sh:279` pins it as `mark_case "none line, later open" silent READY`. The commit edited `BUILD-METHOD.template.md` at line 106-108 (the M4 "Not the harness" line), six lines below the stale paragraph, and left it.

This is live guidance, not documentation trivia: AGENTS.md routes `/session-kickoff`'s hand-back and the unattended kit's M3 at BUILD-METHOD. An agent resolving one fork of several is told the rest are graded. They are not.

No gate sees it. `check-method-carriers.sh` is structural (does a file point rather than copy) and excludes both `memory/` and the template; `kit-dogfood-parity` compares template to render, and the two are wrong identically — the both-copies-wrong shape round 3 called out by name.

**Fix.** Rewrite lines 100-102 in `tools/memory-tree/BUILD-METHOD.template.md` to the corrected TEMPLATE-SPEC wording — the readers grade the whole section as one whitespace-squeezed string, a section with items and no conforming mark anywhere is unresolved, a `none`/`N/A` opening line resolves it whatever follows, and an unresolved fork below an honest `none` line is a known parked gap. Then re-render so `memory/guides/BUILD-METHOD.md` matches. Do NOT run `--render` in the direction that overwrites the live copy's other live-only edits.

**Left-shift.** A claim-join arm: grep both BUILD-METHOD carriers and `memory/TEMPLATE-SPEC.md` for the phrase `PER ITEM` / `Every ITEM is graded`, and refuse when the two documents disagree on whether §8 grades per item. Parity between two wrong copies is not coverage; the join that matters is doc-against-doc, not carrier-against-carrier.

### H3 — the case fix widened the none-form escape: `None of the forks below are resolved.` now passes both readers
`tools/memory-tree/check-memory-hygiene.sh:974` · dup: ids 4, 15

`q8` became `tolower(trim(first non-blank line))` while the tests stayed bare unanchored prefixes `/^none/` and `/^n\/a/`. Before this commit the raw-case test made `None of the forks below are resolved.` fail `/^none/`, so hygiene red the spec — `plan_state` already had the hole. After it, both readers see `none of the forks…`, match the prefix, and a CLOSED spec at or after `FORK_MARK_CUTOFF` with genuinely unmarked items passes the gate while `--plan` reports READY.

Reproduced twice. On a purpose-built scratch fixture (terminal CLOSED spec, cutoff 2026-08-01, §8 = `NONE of the forks below are resolved.` above an unmarked `- **F1 …**` bullet): the `ebe5012` engine printed *"terminal Status, §8 carries items and no conforming resolution mark anywhere"*; the current engine prints nothing. And by adding the row to `marker-contract.test.sh` directly — the current tree printed `FAIL hygiene said silent` AND `FAIL plan_state said READY`; reverting only `tolower(q8)` left just the plan_state FAIL.

The case agreement is real and was worth having. It was bought by loosening the stricter reader into the shape an author most naturally writes — a sentence-initial capital on a denial. That is the exact failure mode both readers' own comments name as the live defect they fixed: "a section whose opening sentence announced that a fork was NOT resolved classified as RESOLVED".

The guarding row `mark_case "first line denies it"` opens with `F1 below is NOT RESOLVED`, which does not begin with the word, so the case table cannot see the regression.

**Fix.** Anchor the none-form to a delimiter rather than accepting a bare prefix, in both readers: `/^none([[:space:]]*[-—.:]|$)/` and `/^n\/a([[:space:]]*[-—.:]|$)/` at `check-memory-hygiene.sh:974, :976, :979` and `unattended.sh:1266, :1268`. Corpus-safe: every tracked §8 none-opener is `none.`, `none - …` or `none — …`, all of which still match, and no tracked spec opens with an uppercase form at all.

**Left-shift.** See M4 — the anchor and the case rows are one piece of work. The row that pins this is a `None of the forks below are resolved.` body with an unmarked item, expecting `red` from hygiene and `FORKED` from plan_state.

---

## Medium

### M1 — the `FORK_MARK_CUTOFF` comment, in the file this commit edited, still declares check 12 "graded PER ITEM"
`.memory-tree.conf:41` · dup: id 3

Lines 41-49 read "check 12, the §8 RESOLUTION MARK, graded PER ITEM once a spec filename reaches this date", list "any unresolved item BELOW a `none` first line was invisible" as a failure mode now addressed, and close with "an ITEM is its opening line plus its continuation lines". All three are false of `check-memory-hygiene.sh:950-979`: there is no per-item walk, and the below-`none` case is explicitly parked in the code's own comment and pinned as silent/READY in `marker-contract.test.sh:279`.

The commit touched this file — the `ARMS_FLOORS` line at `:218`, bumping `check-unattended.sh` 93:93 to 96:96 — without touching the stale comment nine screens above it. It is the conf the gate reads and the first place an operator looks to understand what the cutoff turns on.

**Fix.** Rewrite the 41-49 block to the shipped behaviour: the mark is the documented attributed shape, matched over the whole whitespace-squeezed section so a wrapped mark counts; a section with items and no conforming mark anywhere is unresolved; a `none`/`n/a` opening line resolves the section whatever follows, and an unresolved fork below one is a known parked gap. Keep the measured corpus figures. Drop "PER ITEM" and drop the claim that the below-`none` mode was fixed.

**Left-shift.** Fold into H2's claim-join arm — `.memory-tree.conf` is the third carrier of the same sentence.

### M2 — the header's replacement derivation prints `fail 1`, and the derived arm was not ported
`tools/unattended/check-unattended.sh:3` · dup: ids 6, 10, 19, 25

Line 3 tells the reader to derive the count with `grep -oE 'fail [0-9]+' tools/unattended/check-unattended.sh | sort -un`. Ran it verbatim against the shipped file: it prints exactly one line, `fail 1`. `sort -n` keys on the leading numeric prefix; every line begins with the letters `fail`, so all 96 matches compare equal at 0 and `-u` collapses them. A reader following the header's own instruction concludes the leg has one check. The correct set is the contiguous 1..22.

The header exists precisely because the figure "has now been wrong twice". Its remedy is wrong by a factor of 22 — the same fix-message-that-does-not-work class as round 3's F3. Line 2 also still spells "Its check ids run 1..22" in prose, in the same sentence that asserts the count is not retyped in prose anywhere.

Round 3's F10 additionally asked for a derived arm. The memory-tree sibling already carries the correct form and the gate at `check-memory-hygiene.test.sh:1424-1433`; grep over `check-unattended.test.sh` finds no equivalent. So the figure is the fifth retyping and is still ungated.

**Fix.** `grep -oE 'fail [0-9]+' tools/unattended/check-unattended.sh | awk '{print $2}' | sort -un` (verified: prints 1..22), or the `| grep -oE '[0-9]+' | sort -nu` spelling F10 already suggested. Drop the "1..22" clause from the sentence claiming the count is never retyped.

**Left-shift.** Port the sibling arm into `check-unattended.test.sh`: derive the distinct id set, assert it is contiguous from 1, assert its max equals the figure parsed out of the header, and refuse when the header figure cannot be read. The arm is written already, one file over.

### M3 — a transport failure still reports as "the remote advertised no tips"
`tools/unattended/check-unattended.sh:473` · dup: id 11

Round 3's F9 named five causes of an empty advertisement and asked for the non-124 `ls-remote` rc to be captured as the fifth. Only the two remote-count sentinels (96/97 at `:401-402`) were added. `_rc1` (`:468`) and `_rc2` (`:470`) are captured and compared only against 124 at `:473`.

Any other non-success rc — git returns 128 for auth failure, DNS failure, unknown host, connection refused, a URL that no longer exists — leaves `ADV_HEAD`/`ADV_TIPS` empty with `ADV_RC=0`, so the chain at `:622` falls past the 96/97/98/124 arms to the else at `:640` and prints *"the remote advertised no tips, so the recorded BASE cannot be shown to be published"*: a sentence about the remote for a fault in the transport. That is the exact misattribution the two new arms were added to remove.

The driver already carries the distinction one file over — `unattended.sh:497`, `if [ "$rc" != 0 ] && [ "$rc" != 2 ]` → "the remote did not answer". Paired-carrier shape again.

Fail-closed, so this is a wrong diagnosis rather than a wrong verdict. Medium is the right severity.

**Fix.** After `:473`:

```sh
{ { [ "$_rc1" != 0 ] && [ "$_rc1" != 2 ]; } || [ "$_rc2" != 0 ]; } && [ "$ADV_RC" = 0 ] && ADV_RC=99
```

(rc 2 is legal only on the `--exit-code` call.) Give 99 its own arm in the `:632` chain naming the transport rather than the remote's answer.

**Left-shift.** A red fixture stubbing `git` in `TMPBIN` to exit 128, the way the 124 arm already does — the harness for it exists, it needs one more rc.

### M4 — the cross-kit contract table gained no case or whitespace row, so the fix it pins regresses silently
`tools/memory-tree/marker-contract.test.sh:266` · dup: ids 5, 20

The harness whose stated purpose is pinning the two §8 readers against each other has exactly two none-form rows, both lowercase and unindented: `'none - no forks here.'` and `'none - every fork below is RESOLVED in place.'`. No `None`, no `NONE`, no `N/A`, no `n/a`, no leading-whitespace row anywhere in the file.

Measured: reverting `q8 = tolower(q8)` to `q8 = q8` in `check-memory-hygiene.sh` and running the suite printed `PASS (38 cases across 3 contracts, marker-region, section-8 mark and review verdicts, held)`. The commit's stated purpose is that the hygiene reader now matches `plan_state` byte for byte on `None`, `NONE`, lowercase `n/a` and an indented `none` — every one of those was a live divergence, and the table has a row for none of them. The driver test's `fkspec` fixtures (`unattended.test.sh:2509+`) carry no case-divergence case either.

This is round 3's F6 left-shift, unimplemented. Without it the fix is one edit away from silently regressing, and it is the same shape as the build's own theme one level up: a check that cannot fail on the class it owns.

**Fix.** Add rows **with items present**, so the `items>0` arm is the one graded: `None - all resolved.`, `NONE — …`, `n/a - …`, and an indented `  none - …`, each expecting the same verdict from hygiene and plan_state. Add one denial row opening `None of the forks below are resolved.` above an unmarked bullet, expecting `red`/`FORKED` — that row is also H3's arm.

**Left-shift.** This finding *is* the gate. Land it with H3.

### M5 — the rewritten cross-subject promotion clause has no test arm at all
`tools/unattended/check-unattended.sh:167` · dup: id 18

`grep -n "subject(s) EXITED\|neither fixed nor promoted" tools/unattended/check-unattended.test.sh` returns nothing. Neither of clause 3's messages is asserted anywhere. `python tools/memory-tree/check-arms.py` exits 0 because the enclosing `fail 2` is armed by clause 2's message at test line 278 — so the whole rewrite (the `nneed` count and the `newids + 0 < nneed` comparison, which is the actual per-FILE-vs-per-SUBJECT defect being fixed) has never been observed failing.

Worse: the arm's supposed green control at test line 284 does reach clause 3. Rebuilt the test's `tRev` fixture #2 verbatim in a scratch repo (`RUN.md` with the NON-CONVERGENT exit token, no build README so `rv_readable=0`) and ran the real leg — it prints *"UNATTENDED check 2 FAILED … 1 subject(s) EXITED without converging and the roster at this run BASE cannot be read"*. The suite's `miss` at that arm only greps clause 2's "blocker counts did not shrink", so the control is red and the suite cannot tell.

**Fix.** Add a fixture with TWO subjects both carrying NON-CONVERGENT, a build README whose `gen:build-units` region gained exactly ONE id since the run BASE, and a `hit` on "2 subject(s) EXITED without converging and the generated units region gained only 1 unit id(s)". Add a `hit` for the `readable != 1` message on the existing README-less fixture.

**Left-shift.** `check-arms.py` is satisfied by one armed message per `fail` branch. That is the hole: a multi-clause `fail` is armed by whichever clause happens to be tested. Extend the arms rule to require a positive assertion per distinct literal message under a `fail`, not per `fail` id — the count is derivable from the source, so the floor can be derived too.

### M6 — `TOOL-aBoundedVerdict-4` ratified per-item §8 grading and no superseding record was appended
`memory/DECISIONS.md:70` · dup: id 21

Line 70 still ratifies §8 grading "per ITEM BLOCK rather than on the first line, in both readers". Neither reader does that: `check-memory-hygiene.sh:977` grades `!bmark` over a whitespace-squeezed section blob and escapes on `q8 ~ /^none/` with `bitems>0`; `unattended.sh` plan_state prints READY on the same bytes, pinned as the parked gap at `unattended.test.sh:2549`. Grepped every `aBoundedVerdict` row: no superseding id records the withdrawal. The spec itself (`2026-08-16-spec-TOOL-aBoundedVerdict-4.md`, CLOSED rev-8) still asserts the per-item design and its AC7.

AGENTS.md §6 requires a ratified record to be superseded by a new id plus a note, never left standing wrong. The repo's own convention proves it — line 78's `aBoundedVerdict-11` reads "Reverses aBoundedVerdict-1's cap knowingly (owner)". A session grepping the log for why §8 is graded the way it is currently gets the reversed answer.

Attribution nuance: the code withdrawal landed in `570f810` and this commit rewrote TEMPLATE-SPEC to match it. The missing decision record is real either way and is in the reviewed range.

**Fix.** Append a new `TOOL-<slug>-<n>` superseding `TOOL-aBoundedVerdict-4`: per-item grading withdrawn on measurement (287 §8 bullets, 69 labelled, both resolved and open forks among them), what the readers grade instead, and the parked gap.

**Left-shift.** Hard to gate in general, but this instance is gateable: the decision log's `aBoundedVerdict-4` row names a behaviour that `marker-contract.test.sh` pins the opposite of. A check that greps ratified decision rows for `PER ITEM`-shaped claims and requires either a superseding row or a matching fixture is narrow enough to be worth it once.

---

## Low

### L1 — the verb-documentation arm still guards only non-emptiness, and its new denylist is unasserted
`tools/unattended/check-unattended.test.sh:241` · dup: id 7

Round 3's F11 prescribed a count floor as the left-shift: "this arm's existing liveness check only refuses an EMPTY population, which is why a nine-of-twelve population passed". Line 241 is unchanged — `[ -n "$verbs" ]`. The population is now correct at eleven, but any change that shrinks it again (a reindent, a renamed dispatch site) passes exactly as the nine-verb version did.

The new hand-maintained denylist compounds it. It is applied unconditionally with no assertion that each name it strips is actually a flag, and two of its entries are already dead: the derivation regex at `:233` is `^ +--[a-z]+\)`, which cannot match a hyphenated token, so `--keepalive-id` is invisible to it; and `--witness` has no `--witness)` case arm anywhere in the driver (it is handled by a positional test inside `--phase`, at `unattended.sh:2579`). A stale exemption silently exempts a real verb of that name the day one is added — widening the surface it was written to narrow.

**Fix.** Add the floor: `[ "$(printf '%s\n' "$verbs" | grep -c .)" -ge 11 ]` or the arm refuses. Then either derive the denylist (a name is a flag when it does NOT appear as an arm of the terminal `case "$VERB" in` block and does not dispatch-and-exit), or minimally assert that every denylisted name still matches a `--name)` arm in the driver.

**Left-shift.** The assertion on the denylist *is* the gate: a stale exemption reds instead of widening.

### L2 — the flag denylist exempts `--version`, a dispatched entry point documented on no surface
`tools/unattended/check-unattended.test.sh:237` · dup: id 28

The comment above the list broadens the population precisely because "an arm that grades nine of eleven verbs reports full coverage of a set it never saw", then waives `--version` on the stated grounds that flags are "arguments rather than verbs and are documented by the verb they belong to". `--version` (`unattended.sh:2582`) is not an argument to any verb: it prints the kit version and exits 0. `grep -rn -- "--version"` across `tools/unattended/` and `memory/guides/UNATTENDED-PROTOCOL.md` returns only the dispatch arm and the exemption line itself — it is absent from `SKILL.template.md`, from the usage string at `:2591`, and from the unknown-argument refusal at `:2583`.

Reproduced the population: the derivation yields 21 case arms, the exclusion list leaves exactly 11 verbs, and `--version` is the 12th dispatched entry point no surface names. The widening found a real documentation hole and the same commit waived it.

**Fix.** Remove `--version` from the exclusion list and add it to the usage string, the unknown-argument refusal and the Skill (one line: it prints the kit version). Or keep the exclusion and say in the comment that it is a version probe deliberately outside the documented verb set. Drop `--keepalive-id` and `--witness`, which the extraction can never produce.

**Left-shift.** Same arm as L1 — an exemption that must still match a live `--name)` arm cannot be a hiding place.

### L3 — the `mktemp -d` leak fix has an unfixed second carrier, and this one has no EXIT trap at all
`tools/memory-recall/recall-opened.test.sh:99` · dup: id 22

`WT=$(mktemp -d)/wt`, and `cleanup()` at `:44` removes `$WT` and `$D` but never the mktemp parent of `$WT` — the identical shape the commit fixed in `check-unattended.test.sh` by introducing `TMPBIN_PARENT` and adding it to the EXIT trap. So one scratch directory leaks per completed suite run. Grepped the whole file for `trap`: there is none, so an interrupted run also leaks the `$D` repos from all five `newrepo` calls.

Small in isolation (the leaked parent is empty after cleanup), but the gotcha this commit strengthened — `memory/gotchas/bounded-through-a-pipe-is-unbounded.md:50` — says the accumulation now happens during ordinary completed bar runs, and its recorded consequence is the next suite aborting at startup with `Device or resource busy`. It is the unfixed second carrier of the pair the commit message names.

**Fix.** `WT_PARENT=$(mktemp -d); WT="$WT_PARENT/wt"`, remove `$WT_PARENT` in `cleanup()`, add `trap 'cleanup' EXIT` near the top.

**Left-shift.** A repo-wide grep arm: refuse any `$(mktemp -d)/` construction whose parent is not captured into a variable that the file's cleanup path removes. Zero-false-positive and it covers every future carrier of this pair.

### L4 — the `LANDER_MARKER` refusal was not added, so a `/`-bearing value still aborts push-main after a successful push
`tools/push-main.sh:100` · dup: id 23

The prose carrier was fixed — `.unattended.conf.example:113-119` now says "A BARE NAME, resolved … against `git rev-parse --git-common-dir`", joining `.unattended.conf`, `UNATTENDED-PROTOCOL.md:412` and `PROTOCOL.template.md:412`. Round 3's remediation was explicitly two-part; part two did not land. No refusal exists: `push-main.sh:100` writes `> "$_gcd/$lm"` with the `mkdir -p` gone and the former `|| true` now a hard `exit 1`, and `unattended.sh:1534` concatenates `"$_lm_gcd/$LANDER_MARKER"`. Neither tests for `/`. Check 22 joins key NAMES only.

A stale `LANDER_MARKER=".git/unattended-landed"` — the exact value three carriers documented until this range — resolves to `<git-common-dir>/.git/unattended-landed`, whose parent does not exist. The redirect fails and push-main exits 1 printing "The push SUCCEEDED and is not recorded", wedging the run at `--landed` after an irreversible push.

Requires adopter misconfiguration and the error message is honest, hence low. Four documents now say "bare name" and nothing enforces it.

**Fix.** Refuse a value containing `/` at both ends — one branch in `verb_landed` and one in `push-main.sh` before the write — so a path-shaped marker is a named refusal *before* the push rather than a failed write after it.

**Left-shift.** The refusal is the gate. Add one conf-validation arm to `check-unattended.sh` asserting `LANDER_MARKER` has no `/`, so a bad value reds on the bar rather than at the worst possible moment.

---

## What this round says about the loop

Three rounds in, the fixes are consistently correct in substance and short in reach. Round 3 measured nine of fifteen as paired-carrier misses; this round measures six of fifteen, plus two DoD steps skipped by the commit that was fixing skipped DoD steps. The per-defect gates being added are working — the `verdict epoch` leg and `check-arms.py` both fired here — but they fire at the bar, after the commit exists.

The cheapest remaining left-shift is still the one round 3 named: **a pairing arm per pair**, not fifteen individual gates. The pairs in this tree are enumerable — `memory/guides/X.md` ↔ `tools/<kit>/X.template.md`, `.unattended.conf` ↔ `.unattended.conf.example`, the two §8 readers, the driver ↔ its leg, a fixture ↔ its sibling suite. A single declared registry of those pairs, with an arm that refuses a commit touching one side of a pair without the other, would have caught H2, M1, M3, L3 and L4 in this commit alone — five of fifteen, before the commit object existed.

The second cheapest is a pre-commit widening: run `check-verdict-epoch.sh` when the engine is staged, and refuse a staged build-record add without its regenerated `README.md`. That is both blockers, for two grep conditions.
