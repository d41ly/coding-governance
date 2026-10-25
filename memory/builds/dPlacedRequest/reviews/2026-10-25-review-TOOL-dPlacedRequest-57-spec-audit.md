**Serves:** spec-audit TOOL-dPlacedRequest-57@rev-1 TOOL-dPlacedRequest-58@rev-2 TOOL-dPlacedRequest-59@rev-1

# Tier-2 spec audit — build dPlacedRequest, the round-6 promotion specs TOOL-dPlacedRequest-57 to -59, ROUND 1

*This is an adversarial pre-code pass over the three specs that the round-6 spec audit promoted, dated 2026-10-25. Five lenses found defects, and five skeptic batches tried to refute each finding. This report is synthesised only from the findings that survived. Finders were gov-spec-reviewer, skeptic batches gov-skeptic, and synthesis gov-synthesizer.*

Reviewed: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md@bb2da67d3c16c00d811c6095616f7bbdf0c0f7c6, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-58.md@18c06ca54c6695d66f8652125cb2541cad4d9a9c, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md@0e2db40b1c886a21347152a645b8f92e145390aa

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker was confirmed. One HIGH was confirmed, so under the owner's ruling ("audit until a round confirms no HIGH, then stop") this round does not end the audit loop.

By item the tally is 0 blocker, 1 high, 7 medium and 9 low, 17 items in all. By raw confirmed finding it is 0 blocker, 1 high, 11 medium and 9 low, 21 findings in all.

No finding was confirmed against TOOL-dPlacedRequest-58.

## Review shape

The review ran at intensity full: raw 22, confirmed 21, refuted 1, unverified 0 (0 uncertain), precision 0.95.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 5 | 4 | 1 | 0 | 0 | 0.80 |

The one refutation, id 19, is a duplicate of id 16.

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified.
- Discards: 0 spurious verdicts were discarded, and 0 duplicates.
- Fixes on confirmed findings: 16 judged sound, 5 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 56 spec documents were supplied as `specs`, as sibling context.
- Checklist: 40 items, each assigned to exactly one of 5 lenses (8 each).
- By design: 1 invariant from the checklist's by-design block.
- Move check: no checked subject moved.

Every count above is zero where it must be, so the run is complete.

## HIGH

### H1. 57 AC2's extraction of 34 AC59 runs to the end of 34's spec (id 16)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-57.md`, §6 AC2, the clause that says 34's AC59 bullet is "extracted the same way" as 44's AC1.
- **What is wrong:** The 44 form stops at the next criterion bullet. AC59 is the last criterion in 34 (line 547), and there is no AC60. The range therefore never closes, and it takes in 34's §7 to §10 (60 lines).
- **Consequence:** AC2's two clauses on AC59 are graded over the whole tail of 34's spec, not over AC59. The clause "names `TOOL-dPlacedRequest-44`" can pass on a §9 revision line, which this build's own passes write into 34, while AC59 carries no pointer. AC2 then certifies a restatement that never happened. In the other direction, any later §9 or §10 text holding an 8-hex sha turns AC2 red on a correct AC59.
- **Fix (judged SOUND by the skeptic):** Bound the extraction at the next criterion or the next section, e.g. `awk '/^- \*\*AC59\*\*/{f=1;print;next} f&&/^(- \*\*AC|## )/{exit} f'`. Spell that command out in AC2 for 34 instead of writing "the same way". Add a red case: a scratch copy of 34 whose AC59 lacks the name but whose §9 names `TOOL-dPlacedRequest-44` must fail AC2.
- **Left-shift gate:** A spec lint that rejects any criterion extraction range with no terminator for the last bullet of a section. Failing that, a checklist entry: "a bullet extraction must stop at the next bullet OR the next heading".

## MEDIUM

### M1. 59 AC3's class sweep and S3's inventory describe different populations (ids 1, 9, 17, 18)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §2 S3 (the inventory of oracle-running criteria) against §6 AC3 (the sweep `grep -E 'oracle[^.]*(runs|run )'` over the joined bullets).
- **What is wrong, first direction (false red):** The sweep hits 59's own AC2, AC4, AC5 and AC21, which run the oracle on a fixture, and S3 lists none of them. It also hits 56 AC19, a false positive: that bullet ends "for a form no oracle runs." and runs no oracle.
- **What is wrong, second direction (blind spot):** The sweep misses criteria S3 does list. 44 AC2 and 56 AC10 are worded "the oracle prints", 43 AC24 does not name the oracle, and 52 AC29 does not match either.
- **What is wrong, row format:** S3 writes rows as ranges ("52 AC11 to AC14", "44 AC1 to AC3"). A literal label check either misses AC12, AC13 and AC2, or finds "AC1" inside "AC11".
- **Consequence:** Built exactly as S3 lists it, AC3 is red on a correct build, and the builder must pad the table or loosen the criterion. AC3 also cannot go red when an oracle criterion worded "prints" drops out of the inventory, which is the omission it exists to catch. It certifies coverage in one direction only.
- **Fix (judged SOUND on ids 1, 17 and 18, UNSOUND on id 9, whose skeptic correction is used here):**
  - Make S3's inventory one label per row, with no ranges.
  - Add 59 AC2, AC4, AC5 and AC21 to it, each with the base it passes (the fixture's base).
  - Have AC3 match each label anchored as `AC<n>\b` against an explicit expected list, and name text-only hits such as 56 AC19 as exclusions. Matching an oracle invocation (a run-shape with an argument) instead of the bare word "runs" also drops 56 AC19.
  - Add the reverse direction: every inventory row's criterion, extracted, names the oracle and a base.
  - Do not derive the inventory from the predicate, because the predicate misses 43 AC24, 44 AC2, 56 AC10 and 52 AC29.
  - Run the final pattern over the real spec tree first, and record its hit set in 54 §4 Evidence.
- **Left-shift gate:** A class-sweep criterion must state its expected hit set and be checked in both directions (hits ⊆ inventory, inventory ⊆ class). Add a checklist entry "a sweep regex is run over the real tree before it is written into a criterion".

### M2. 59 AC7's count of the key split counts the wrong spelling (ids 2, 15)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §6 AC7 against §4 "The shared key reader (S7)".
- **What is wrong:** AC7 requires `grep -c 'index($0, ": ")' tools/unattended/unattended.sh` to print 1, "inside `CLAIM_KV_AWK`". The sketch's function is `kv(line, ...)` and splits with `index(line, ": ")`. Today the grep already prints 1, from read_claims at unattended.sh:2170.
- **Consequence:** A build that follows the sketch prints 0, so AC7 fails a correct build. A build that keeps read_claims' `$0` split prints 1 and passes, which admits the very duplicate S7 removes. A second split spelled with any other variable is invisible to the count.
- **Fix (id 2 judged SOUND; id 15 judged UNSOUND, whose skeptic correction is used here):**
  - Require `grep -cE 'index\([^,)]*, *": "\)' tools/unattended/unattended.sh` to print 1, with its one hit on a line between `CLAIM_KV_AWK='` and its closing quote. This pattern catches a split under any variable name. It prints 1 on today's tree, so the line-position clause is what makes it red before the build.
  - State the red case as a probe the build must run: a scratch copy of the driver that adds a second split, under any variable name, to the age walk makes the count print 2.
- **Left-shift gate:** A checklist entry: "a count criterion over code must match the spelling the design's sketch produces, and must be shown to be red on today's tree".

### M3. 56 and 57 share order 29, so the build index renders them as parallel (id 3)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-57.md`, the header (`order 29`), §3 Edges (hands-off 56) and §4 Files touched. 56 also carries `order 29`.
- **What is wrong:** gen_build_index.py:1717 treats units sharing an order as the parallel group. README.md:227 renders `| 29 | TOOL-dPlacedRequest-56, TOOL-dPlacedRequest-57 | yes |`. The two units share a write set: 57 edits 44 AC1 and 34 AC59, and 56 edits 44 and measures 34 after 57's cut. The sequencing exists only in 57's prose (57:66, 57:99-100).
- **Consequence:** The index tells a dispatcher it may run 56 and 57 at the same time. That breaks M6's disjoint-write-set condition: one pass can overwrite the other's edits to 44, or 56 S11 measures 34 before 57 cuts it. The effect is contained because M6 asks for recorded write sets at `--dispatch`.
- **Fix (judged UNSOUND by the skeptic; the skeptic's correction):**
  - Give 57 order 29, and move 56 to 30, 58 to 31 and 59 to 32.
  - In the same pass, update the prose that cites the old numbers: 56:28 "at order 29", 58:30 "repairs 56, at order 29, so it sits at order 30", 59:27 "at order 31", and the "shared order" wording at 57:66 and 57:99-100.
  - Re-render the index so the step table shows no parallel group for the pair.
- **Left-shift gate:** Make gen_build_index.py, or a hygiene check, refuse two same-order units whose Files touched overlap.

### M4. 57 AC1 cannot observe S1, and §1 misstates why 54 AC1 is green today (id 7)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-57.md`, §1 Goal, §4 "The read, at the close", §6 AC1.
- **What is wrong:** §1 says 54 AC1 is green today "only because the merge found is the base". In fact the nearest first-parent merge, c63aabbb, is dOrderedCharter's landing. 54's subject test sets own=0 and short-circuits before the ancestor test runs. AC1 checks only exit 2, the refusal line, and a header naming the merge found.
- **Consequence:** In the build run, the nearest first-parent merge may be another build's landing (concurrent runs are by design) or a reconcile merge with a non-lander subject. Either way own=0 refuses with exit 2 whatever base is passed. AC1 is then green with the stale c63aabbb base, so its "Red when" cannot fire. §1 also misleads the next reader about which test protects the tree.
- **Fix (judged SOUND by the skeptic):**
  - Restate §1: today's refusal comes from the subject test, because c63aabbb is a foreign landing.
  - Make AC1 first assert that `git log -1 --format=%s` of the merge it finds matches `merge: dPlacedRequest — land onto `. If it does not, AC1 must report itself unexercised instead of passing.
  - Better, add a contrast leg: run the same oracle with the spec run's archived base (from its RUN.LANDED.*.md `base:` fact) and expect a walk with exit 0, while the run's own base exits 2. That shows the base matters.
- **Left-shift gate:** A checklist entry: "a refusal criterion must show which test refused, or carry a contrast leg that passes".

### M5. 59 S19's joined-read regex matches none of the house-style sequence sentences (id 10)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §4 "The sweep (S14) and the joined read (S19)", §2 S19, §6 AC19.
- **What is wrong:** The regex `TOOL-dPlacedRequest-[0-9]* writes [^.]*unattended\.test\.sh[^.]*in sequence` needs a bare id followed by " writes". The house form wraps the id in backticks ("`TOOL-dPlacedRequest-44` writes this file", at 48:99, 57:99 and 54:120). Looped over every spec's Files touched section, the regex prints nothing.
- **Consequence:** When 56 S5's sentence is written in house style, 56 AC5 (as S19 restates it) and 59 AC19 over 48 print nothing. A correct build goes red, or the builder bends the prose to fit the regex. This is the same class of false red the item set out to remove.
- **Fix (judged UNSOUND by the skeptic; the skeptic's correction):**
  - Have S19 fix 56 S5's sentence word for word in both 48 and 50, e.g. "`TOOL-dPlacedRequest-50` writes `tools/unattended/unattended.test.sh` at order 25, so the two passes run in sequence."
  - Have the joined read allow the backtick: ``grep -o 'TOOL-dPlacedRequest-[0-9]*`\? writes [^.]*unattended\.test\.sh[^.]*in sequence'``.
  - Check it against that exact sentence, and against a copy wrapped between "run in" and "sequence".
- **Left-shift gate:** Same class as M1: a prose-matching regex is run over the real tree and over the sentence it is meant to find before it is written into a criterion.

### M6. 57 S1 writes a new `base:` reader beside the shared `extract_run_facts` (id 14)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-57.md`, §2 S1, §4 "The read, at the close" (lines 39 and 74), §10 Reuse audit (lines 165-169).
- **What is wrong:** S1 spells a fresh awk, `awk '/^## /{s=/^## Run facts/} s&&/^base: /{print $2; exit}'`. tools/unattended/lib-unattended.sh:2057 already defines `extract_run_facts`, and its header says every pipe reader of a run fact routes through it. check-brief-recorded.sh:381 and check-pass-order.sh:356 already read `base` through it. §10 claims "no existing seam fits", which is false.
- **Consequence:** This adds a third spelling of the Run-facts grammar, and it already differs: it requires exactly one space after `base:` and strips no CR. A later change to the facts grammar moves the library readers and not this criterion. §10 also tells the next unit that no seam exists.
- **Fix (judged SOUND by the skeptic):**
  - Restate S1, §4 and 44 AC1 (the copy S2 gives it) to the library spelling, as check-pass-order.sh:356 has it: `b=$(bash -c '. tools/unattended/lib-unattended.sh; extract_run_facts' < memory/builds/dPlacedRequest/RUN.md | sed -n 's/^base:[[:space:]]*//p' | head -1 | tr -d '\r')`.
  - Correct §10 to name `extract_run_facts` as the seam extended.
  - AC2's check that 44 AC1 names `RUN.md` and `## Run facts` should also accept, or require, `extract_run_facts`.
- **Left-shift gate:** A gate leg that flags a `/^## Run facts/` awk anywhere outside lib-unattended.sh, in specs as well as in code.

### M7. 59's shared `CLAIM_KV_AWK` sketch drops read_claims' CR strip (id 20)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §2 S7 and §4 "The shared key reader (S7)" (59.md:159-167).
- **What is wrong:** read_claims today runs `{ sub(/\r$/, ""); p = index($0, ": ") ...` (unattended.sh:2170). The sketch shows the callers as bare `{ kv($0, want, v, 0) }`, and kv has no CR strip. 59 says nothing about CR anywhere. The sketch also declares no function-local p, k or value; this part is minor, because p and k are already global in read_claims.
- **Consequence:** A builder who follows the sketch drops the strip from the strict reader. A claim body line `status: live\r` then fails the status test, and that claim reads incomplete or unknown. The walk's bare `renews:\r` no longer matches `/^[a-z-]+:[ ]*$/`. §5 prices only "admits nothing it refused before", not the reader refusing more.
- **Fix (judged SOUND by the skeptic):** Put `sub(/\r$/, "", line)` inside kv, before the index split, so both readers get it. Declare p, k and value as function locals. Add a CRLF body row to the S7 arm, staged against a copy without the strip.
- **Left-shift gate:** A checklist entry: "a refactor that extracts a shared reader carries every normalisation step of the caller it replaces, with a row for each".

## LOW

### L1. 59 AC4 and AC5 have clauses that cannot fail (id 4)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §6 AC4 and AC5.
- **What is wrong:** AC4 checks that 56 AC10 "names `base`", and 56 AC10 already contains `merge-base`. AC5 checks that 43 AC24 "names a base". That is a substring check, so it cannot tell the run's base, which S5 requires, from the fixture's base or any "merge-base" text.
- **Consequence:** An unbuilt 56 AC10 passes AC4. A 43 AC24 given the wrong base passes AC5.
- **Fix (judged SOUND by the skeptic):** Match the argument form instead of the substring. AC4 requires "the fixture's base" in each bullet. AC5 requires 43 AC24 to name `RUN.md` or "the run's base" (57 S1's read), as 57 AC2 does for 44 AC1.
- **Left-shift gate:** Same class as M2: show each criterion clause red on today's tree.

### L2. 59 S21 writes the oracle's head into two specs, against S13's "stated once" (id 5)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §2 S21 (59:117-119) against S13 (59:98-100).
- **What is wrong:** S13 makes 52's oracle a pointer "so the oracle is stated once". S21 then writes the ancestor-status case into both 44 §4 and 54 §4's sketch. 54:77-90 holds a full head. AC13 checks only 52.
- **Consequence:** Two spec copies of the oracle's head can drift, and a later fold that edits one goes unnoticed. This is a documentation defect only.
- **Fix (judged SOUND by the skeptic):** Write S21 into 44 §4 only. Make 54 §4's head section a pointer to 44 §4, as S13 does for 52. Extend AC13 so that `grep -c 'git rev-list'` over 54's head section also prints 0.
- **Left-shift gate:** A checklist entry: "a 'stated once' claim carries a count criterion over every spec that once held a copy".

### L3. 57 AC2's extraction of 34 AC59 runs to the end of the file (id 6)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-57.md`, §6 AC2.
- **What is wrong:** This is the same defect as H1. It is kept as its own item only because its binding grade is low and items merge within one grade. Its angle: the `[0-9a-f]{8}` clause reads 34's §7 to §10, including the §9 line this unit requires.
- **Consequence:** A §9 line naming 57 that quotes the dropped sha (e.g. "drops c63aabbb") would fail AC2 on a correct build, or push the author to word the log around the check.
- **Grade note:** I judge this high alongside id 16, because it is the same defect with the same consequence. The binding grade is kept.
- **Fix (judged SOUND by the skeptic):** End the extraction at the next bullet, heading or blank line, e.g. `awk '/^- \*\*AC59\*\*/{f=1;print;next} f&&/^(- |#|$)/{exit} f'`, and state that form explicitly. H1's fix covers this too.
- **Left-shift gate:** As H1.

### L4. 59 S1 writes the wrong cause into 54's evidence (id 8)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §2 S1 (59:54-57), §6 AC1 (59:230-231).
- **What is wrong:** S1 has 54 §4 Evidence say the ancestor test went unexercised because "the merge found there was the base itself". The real cause is that the merge found was dOrderedCharter's landing, and the subject test refused it first.
- **Consequence:** A later reader thinks that a base equal to the found merge is what disables the protection. That reader misses that every foreign-subject merge bypasses the ancestor test.
- **Fix (judged UNSOUND by the skeptic; the skeptic's correction):** Restate S1 so the Evidence bullet says the merge found was a foreign landing that the subject test refused before the ancestor test ran. AC1 should check for the phrase `subject test` in that bullet, not `dOrderedCharter`.
- **Left-shift gate:** As M4. A causal claim in Evidence names the test that fired, observed rather than inferred.

### L5. 59's shared key reader neither strips CR nor trims the value (id 11)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §2 S7 and §4 "The shared key reader (S7)" (lines 160-164).
- **What is wrong:** The kv sketch sets the value from the text after `p + 1`. It has no trim, and 52 S26 says the walk's `renews:` value is "trimmed". The CR side overlaps M7, which is graded separately.
- **Consequence:** `renews:` followed by two spaces parses to the value " ", not to the empty value. By 52 S25/S26 that reads on the same way, so the outcome barely changes. MSYS gawk drops the CR on pipe input, so no local probe on node a can show the CR case.
- **Fix (judged SOUND by the skeptic):** Put the CR strip and a trim of the value inside the function, or state that each caller strips the CR first. Add a `renews:` row with two trailing spaces to AC7. Add a CR row that runs on a POSIX node or a CI leg.
- **Left-shift gate:** As M7.

### L6. 59 §1 miscounts the multi-id review items (id 12)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §1 Goal (line 23).
- **What is wrong:** It says "Five review items hold more than one id" and lists four (M1, M2, L2, L5). The 53 audit has exactly those four.
- **Consequence:** A reader checking coverage trips on it. Nothing depends on it.
- **Fix (judged SOUND by the skeptic):** Change "Five" to "Four".
- **Left-shift gate:** None fits. Add it to the bug-class checklist as "a stated count matches the list it introduces".

### L7. 57 §5 understates RUN.md's size (id 13)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-57.md`, §5 perf / scale (line 116).
- **What is wrong:** It says "a file of under a hundred lines", but RUN.md has 133.
- **Consequence:** None. The cost is still trivial.
- **Fix (judged SOUND by the skeptic):** Say "a run-state file of a few hundred lines at most", or drop the count.
- **Left-shift gate:** As L6.

### L8. 57 S1's awk does not copy `fact`'s grammar (id 21)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-57.md`, §2 S1 and §4 "The read, at the close" (57.md:39 and :74).
- **What is wrong:** `fact` (unattended.sh:1363-1371) strips a trailing CR and accepts `base:` followed by any run of spaces, including none. The awk keeps a CR inside `$2` on POSIX gawk and needs exactly one space.
- **Consequence:** A run-state file with CRLF endings, or a `base:<sha>` line, gives `b` as empty or CR-bearing. The oracle then refuses with `base does not resolve` where AC1 expects `no prepared merge on HEAD`. The failure is loud and needs a hand-edited file, because RUN.md is pinned eol=lf and set_fact writes `key: value`.
- **Fix (judged SOUND by the skeptic):** Have the read strip CR and tolerate the space run that `fact` tolerates, e.g. `awk '{sub(/\r$/,"")} /^## /{s=/^## Run facts/} s&&/^base:/{sub(/^base: */,""); print; exit}'`, and cite `fact`'s semantics (unattended.sh:1350-1353) as its contract. M6's fix, routing through `extract_run_facts`, also removes this defect.
- **Left-shift gate:** As M6.

### L9. 59 S21's sketch hides the tests that must run before the ancestor case (id 22)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-59.md`, §2 S21 (:117-119) and §4 "The ancestor test's status (S21)" (:169-177).
- **What is wrong:** The sketch shows `git merge-base --is-ancestor "$t" "$base"; a=$?` and its case on their own. It never says that 54.md:86's `[ -z "$t" ] || [ "$own" = 0 ]` short-circuits still run first.
- **Consequence:** A builder who swaps 54's whole `if` for the case block refuses a no-merge HEAD with the wrong line (merge-base exits 128) and walks foreign landings. 54 AC2's fixture rows would catch this, so the effect is contained.
- **Fix (judged SOUND by the skeptic):** Have S21 state the order explicitly. `[ -z "$t" ] || [ "$own" = 0 ]` exits 2 with `no prepared merge on HEAD` first, and only then does the captured is-ancestor case run. Show the full head in the sketch.
- **Left-shift gate:** A checklist entry: "a partial sketch that replaces part of a guarded block shows the whole block".

review-shape kind=spec-audit round=1 intensity=full at=synth raw=22 confirmed=21 refuted=1 unverified=0 blocker=0 high=1 medium=11 low=9 agents=11 out-tokens=145692

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 6 AC3 against section 2 S3 | medium | medium | confirmed | I re-ran 59 S14's join with `grep -E 'oracle[^.]*(runs\|run )'` over every spec/*.md. It hit 44 AC1, AC3; 52 AC11-14, AC17; 54 AC1, AC2; 55 AC1, AC2; 56 AC6, AC19; 57 AC1; 59 AC2, AC4, AC5, AC21. S3's inventory (59:61-64) has no 56 AC19 and no 59 rows, so AC3 fails on a build that follows S3. 56 AC19's joined bullet ends 'for a form no oracle runs.' and runs no oracle, so it is a false positive. 44 AC2 ('the oracle prints') and 56 AC10 (oracle 'prints') do not match the regex, so the sweep cannot catch a missing row of that kind. The check works in one direction only, and as written it contradicts its own inventory. | sound | fixture-passes-by-finding-nothing |
| 2 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 6 AC7 against section 4 'The shared key reader (S7)' | medium | medium | confirmed | `grep -n 'index($0, ": ")' tools/unattended/unattended.sh` prints one line today, 2170, inside read_claims. 59 §4's S7 sketch writes `CLAIM_KV_AWK = function kv(line, ...)` with `p = index(line, ": ")`. A build that follows the sketch drops the `$0` count to 0 and fails AC7. A build that keeps read_claims' own `$0` split keeps the count at 1 and passes. So the count clause rejects the correct build and admits the duplicate S7 removes. | sound | a-spelling-change-strands-its-readers |
| 3 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md:header order 29; section 3 Edges hands-off 56; section 4 Files touched | medium | medium | confirmed | Both 56:3 and 57:3 carry `order 29`. README.md:227 renders `\| 29 \| TOOL-dPlacedRequest-56, TOOL-dPlacedRequest-57 \| yes \|` under the `Parallel` column, and gen_build_index.py:1717 says units sharing an order are the parallel group. 57's Files touched (44 AC1, 34 AC59) overlaps 56's write and read set (56:151 measures 34 after 57's cut). M6's parallel-when-disjoint condition therefore fails. The sequencing exists only in prose (57:66, 57:99-100), and no non-goal of 57 withholds a renumbering (the no-renumbering non-goal is 59's). The generated index misleads a dispatcher; the effect is contained because M6 asks for recorded write sets at --dispatch. | unsound | - |
| 4 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 6 AC4 and AC5 | low | low | confirmed | 56 AC10's bullet reads 'merge-base (form\|origin)' (seen in the joined bullet), so 'names `base`' already passes before 56 is built. 43 AC24 today reads only S24's `git log` grep and names no base. AC5's 'names a base' is a substring check, so it accepts the fixture's base or any 'merge-base' text, when S5 requires the run's base. Part of each criterion is green, or wrongly green, regardless of the build. | sound | - |
| 5 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 2 S21 against S13 | low | low | confirmed | 59:98-100 (S13) makes 52's oracle a pointer 'so the oracle is stated once'. But S21 (59:117-119) writes the ancestor-status case into both 44 §4 and 54 §4's sketch. 54:77-90 holds a full head with `git rev-list --first-parent ...` and the is-ancestor test, and AC13 checks only 52's section. The result is two spec copies of the head that can drift, which is a documentation defect only. | sound | two-answers-to-one-question |
| 6 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md:section 6 AC2 | low | low | confirmed | 57 AC2 (57:136-140) says 34's AC59 bullet is 'extracted the same way' as 44's AC1, i.e. ending at the next AC bullet. `grep -c '^- \*\*AC60\*\*' 34.md` printed 0. 34's headings show AC59 at line 547, followed by §7 at 551 through §10 at 595, so the awk range runs to the end of the file and takes in the §9 line that S3 requires. Today the only 8-hex hit in that range is AC59's own c63aabbb. A §9 entry naming 57 that quotes the dropped sha would turn AC2 red on a correct build. Only the wording of a criterion is affected, so low. | sound | - |
| 7 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md:section 1 Goal, section 4 'The read, at the close', section 6 AC1 | medium | medium | confirmed | `git log -1 --format='%s%n%P' c63aabbb` printed 'merge: dOrderedCharter — land onto origin/main at cdfbd1cf'. `git rev-list --first-parent --min-parents=2 --max-count=1 HEAD` printed c63aabbb. 54 §4 sketch lines 85-86 set own=0 for any subject other than 'merge: dPlacedRequest — land onto' and test `[ "$own" = 0 ] \|\|` before `git merge-base --is-ancestor`. So today's refusal comes from the subject test short-circuiting, and 57 §1's claim 'green today only because the merge found is the base' is false. 57 AC1 checks only exit 2, the refusal line and a header naming the merge that was found. If the nearest first-parent merge in the build run is another build's landing or a reconcile merge, AC1 is green whatever base is passed, and its Red-when cannot fire. That is a real but contained weakness in a criterion. | sound | observed-by-claim-no-arm-discharges |
| 8 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 2 S1, section 6 AC1 | low | low | confirmed | 59 S1 (59:54-57) has 54 §4 Evidence say 'the merge found there was the base itself, so that measurement did not exercise the ancestor test'. 59 AC1 (59:230-231) checks for `the base itself`. Re-probe: c63aabbb's subject is dOrderedCharter's landing (54:102 records the same subject), and 54's sketch sets own=0 for that subject and short-circuits before is-ancestor. Even with own=1, is-ancestor c63aabbb c63aabbb would also refuse. The recorded cause is therefore wrong. It only misleads readers of the evidence prose, so low. | unsound | - |
| 9 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 2 S3, section 6 AC3 | medium | medium | confirmed | I ran 59 §4's join awk plus `grep -E 'oracle[^.]*(runs\|run )'` over spec/*.md. Hits: 44 AC1, AC3; 52 AC11-AC14, AC17; 54 AC1, AC2; 55 AC1, AC2; 56 AC6, AC19; 57 AC1; 59 AC2, AC4, AC5, AC21, exactly as the finding states. The inventory in 59 S3 (59:61-64) lists neither 56 AC19 nor any of 59's own criteria, so AC3 is red on a correct build. The sweep also does not hit 43 AC24, 44 AC2, 56 AC10 or 52 AC29, all of which S3 lists, so it cannot detect those omissions. S3's rows are written as ranges ('52 AC11 to AC14', '44 AC1 to AC3'), which a label lookup cannot match reliably. | unsound | id-matched-as-a-substring |
| 10 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 4 'The sweep (S14) and the joined read (S19)', section 2 S19, section 6 AC19 | medium | medium | confirmed | I looped the S19 joined read (59 §4) over every spec's Files touched section and it printed nothing for any of them. `grep -rnoE 'TOOL-dPlacedRequest-[0-9]+`? writes'` shows the house form wraps the id in backticks ('`TOOL-dPlacedRequest-44` writes this file ...', 48:99, 57:99, 54:120). A house-style line ('`TOOL-dPlacedRequest-50` writes this file ... in sequence') piped through the regex gave rc=1. Only a non-backticked id with the path after 'writes' matched (rc=0). 59 S19 does not fix the sentence form, so a correctly written 56 S5 sentence makes 56 AC5 and 59 AC19 print nothing. | unsound | - |
| 11 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 2 S7, section 4 'The shared key reader (S7)' | low | low | confirmed | The 59 section 4 sketch (lines 160-164) has `p = index(line, ": ")` and `value = after p + 1`. It has no CR strip and no trim. The live split at unattended.sh:2170 strips the CR in read_claims' own program, before the split. 52 S26 (line 151) says the walk's `renews:` value is 'trimmed'. So `renews:` plus two spaces gives " " under the sketch, and that disagrees with 52. The consequence is small. By 52 S25/S26, any value outside the four, " " included, reads on the same way the empty value does, so the outcome barely changes. A CR on a claim body line is also unlikely. Low. | sound | - |
| 12 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 1 Goal | low | low | confirmed | 59 line 23 says 'Five review items hold more than one id' and then lists four (M1, M2, L2, L5). The grep of the 53 audit's headings shows exactly those four multi-id items. Prose only. | sound | - |
| 13 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md:section 5 perf / scale | low | low | confirmed | 57 line 116 says 'a file of under a hundred lines'. `wc -l memory/builds/dPlacedRequest/RUN.md` printed 133. The size claim is wrong, but nothing depends on it. | sound | - |
| 14 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md:section 2 S1, section 4 "The read, at the close", section 10 Reuse audit | medium | medium | confirmed | 57 S1 and section 4 (lines 39 and 74) spell a new awk reader that needs exactly `base: ` and takes `$2`. lib-unattended.sh:2057 defines `extract_run_facts`. Its header says every pipe reader of a run fact routes through it. check-brief-recorded.sh:381 and check-pass-order.sh:356 already read `base` that way. 57 section 10 (lines 165-169) says no seam fits beyond the run-state file. That is false and misleads the next unit. The duplicate reader also has its own grammar: one space only and no CR strip. RUN.md:39 holds `base: c63aabbb…`, so the library answers the same question today. | sound | - |
| 15 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 6 AC7 against section 4 "The shared key reader (S7)" | medium | medium | confirmed | 59 AC7 (line 251) counts `index($0, ": ")` and expects 1 'inside CLAIM_KV_AWK'. The 59 sketch (lines 160-161) spells the split as `index(line, ": ")`, so a faithful build prints 0 and AC7 fails. Today the grep prints 1, from unattended.sh:2170 in read_claims, so the count conjunct is already green before the unit is built. It also cannot see a second split spelled with another variable. The proposed fix's first option lists only `$0\|line\|l`, so a duplicate spelled `index(s, ": ")` still escapes, and the fix does not cure the defect it names. The general pattern `grep -cE 'index\([^,)]*, *": "\)'` prints 1 on today's tree, at :2170. | unsound | - |
| 16 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md:section 6 AC2 (34's AC59 bullet, 'extracted the same way') | high | high | confirmed | 57.md:136-140 says 34's AC59 bullet is 'extracted the same way' as 44's AC1, i.e. `awk '/^- \*\*AC1\*\*/{f=1} f&&/^- \*\*AC2\*\*/{exit} f'`. I ran `grep -n '^- \*\*AC' 34.md \| tail -2`: AC59 at :547 is the last criterion. `awk '/^- \*\*AC59\*\*/{f=1} f' 34.md \| wc -l` printed 60, and the headings for §7 (:551), §8 (:561), §9 (:580) and §10 (:595) all fall inside that range. Right now the tail after :550 holds neither TOOL-dPlacedRequest-44 nor an 8-hex run. But this build's own passes add §9 lines to 34 (AC2 itself requires one naming 57), and a line that records AC59's restatement would plausibly name 44. That lets AC2 certify a pointer AC59 does not carry, and any sha in a later line would turn it red on a correct AC59. | sound | amendment-leaves-its-other-half-standing |
| 17 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 2 S3 (inventory list) against section 6 AC3 | medium | medium | confirmed | I re-ran the joined-bullet sweep with AC3's `grep -E 'oracle[^.]*(runs\|run )'` over spec/*.md. It printed 44 AC1, 44 AC3, 52 AC11-14, 52 AC17, 54 AC1, 54 AC2, 55 AC1, 55 AC2, 56 AC6, 56 AC19, 57 AC1, 59 AC2, 59 AC4, 59 AC5 and 59 AC21. S3 (59.md:61-64) lists none of 56 AC19, 59 AC2, 59 AC4, 59 AC5 or 59 AC21. AC3 (59.md:237-240) requires every hit to appear in 54's inventory, so a build that follows S3 exactly goes red. 56 AC19 (56.md:285-287) only says 'a form no oracle runs', which is a false hit. | sound | - |
| 18 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 6 AC3 (with section 2 S3) | medium | medium | confirmed | The same re-run sweep reproduces the extra hits (56 AC19 and 59's AC2, AC4, AC5, AC21), which S3 does not list. It also misses real oracle-running criteria. 44 AC2 (44.md:132-135) reads 'the oracle prints `+KIT_UNATTENDED_VERSION=1.111`', and 56 AC10 (56.md:262) reads 'the oracle prints `walked no commit of the build` and exits 2'. Neither matches `(runs\|run )`, and 43 AC24 does not name the oracle at all. So AC3 cannot go red when one of those drops out of the inventory, even though S3 lists them. This is a distinct defect from id=17 (under-matching rather than the false red). | sound | - |
| 19 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md:section 6 AC2 | medium | - | refuted | duplicate of id=16. Same defect: AC59 is 34's last criterion (:547), the 'same way' extraction runs to EOF, and the 60-line output takes in §7 to §10. I reproduced it identically. | sound | - |
| 20 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 2 S7 and section 4 'The shared key reader (S7)' | medium | medium | confirmed | tools/unattended/unattended.sh:2170 reads `{ sub(/\r$/, ""); p = index($0, ": ")`, so read_claims strips a trailing CR before it splits. The S7 sketch at 59.md:159-167 has the callers as bare `{ kv($0, want, v, 0) }`, and kv contains no CR strip. I grepped 59.md for CR, \r and CRLF and found nothing. S7 says only that `want` and `ok` are unchanged. A builder following the sketch would drop the strip, and then a CRLF value like `live\r` fails the status test, and a bare `renews:\r` fails the `^[a-z-]+:[ ]*$` match. The locals point is minor because p and k are already global in read_claims, but the CR omission is a real, contained defect. | sound | - |
| 21 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-57.md:section 2 S1 and section 4 'The read, at the close' | low | low | confirmed | 57.md:39 and :74 read `b` with `awk '/^## /{s=/^## Run facts/} s&&/^base: /{print $2; exit}'`. `fact` at unattended.sh:1363-1371 strips a trailing CR, matches the bare prefix `base:` and then strips any run of spaces, so it accepts `base:<sha>` and the awk does not. On this node, MSYS gawk 5.4.0 dropped the CR from a CRLF scratch file, but on a POSIX gawk the default FS leaves CR inside $2. `git ls-files --eol` gives RUN.md `i/lf w/lf attr/text eol=lf`, and set_fact writes `key: value`, so neither spelling turns up today. The two readers really do differ, but the effect is a loud refusal on a hand-edited file only, which makes this low. | sound | two-readers-of-one-config-one-re-derived |
| 22 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-59.md:section 2 S21 and section 4 'The ancestor test's status (S21)' | low | low | confirmed | 59.md:169-177 (§4 'The ancestor test's status (S21)') shows only `git merge-base --is-ancestor "$t" "$base"; a=$?` and its case. S21 at :117-119 says it is 'written into 44 §4 and 54 §4's sketch' but never says that 54.md:86's `[ -z "$t" ] \|\| [ "$own" = 0 ]` short-circuits still run before it. A builder who swaps the whole `if` for the case block would lose those tests. AC21 (:295-298) only exercises the errored-merge-base path. 54 AC2's fixture rows would catch the regression, so the effect stays contained and this is low. | sound | - |
