**Serves:** spec-audit TOOL-dPlacedRequest-60@rev-1 TOOL-dPlacedRequest-61@rev-1

# Tier-2 spec audit — build dPlacedRequest, the round-7 promotion specs TOOL-dPlacedRequest-60 and -61, ROUND 1

*This is an adversarial pre-code pass over the two specs that the round-7 spec audit promoted, dated 2026-10-25. Five lenses found defects, and five skeptic batches tried to refute each finding. This report is synthesised only from the findings that survived. Finders were gov-spec-reviewer, skeptic batches gov-skeptic, and synthesis gov-synthesizer.*

Reviewed: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-60.md@3a687d93096ed2d80c0d26995464e69ddb1e35f1, memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md@c60e84e368dc20fc82309287baf2de94894aab70

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker was confirmed. One HIGH was confirmed, so under the owner's ruling ("audit until a round confirms no HIGH, then stop") this round does not end the audit loop.

By item the tally is 0 blocker, 1 high, 8 medium and 8 low, 17 items in all. By raw confirmed finding it is 0 blocker, 1 high, 12 medium and 9 low, 22 findings in all.

Two findings against TOOL-dPlacedRequest-60 were confirmed, both low (L5, L6).

## Review shape

The review ran at intensity full: raw 24, confirmed 22, refuted 2, unverified 0 (0 uncertain), precision 0.92.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 6 | 4 | 2 | 0 | 0 | 0.67 |

The two refutations, ids 19 and 20, appear in the appendix only.

The skeptics re-graded 8 findings. Each item below carries the binding grade.

Ids 7 and 11 describe one defect, but their binding grades differ (low and medium). They stay as two items, M5 and L4, and neither id is counted twice.

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified.
- Discards: 0 spurious verdicts were discarded, and 0 duplicates.
- Fixes on confirmed findings: 20 judged sound, 2 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 8 RE-GRADED.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 59 spec documents were supplied as `specs`, as sibling context.
- Checklist: 40 items, each assigned to exactly one of 5 lenses (8 each).
- By design: 1 invariant from the checklist's by-design block.
- Move check: no checked subject moved.

Every count above is zero where it must be, so the run is complete.

## HIGH

### H1. 61's "extracted" reads a `###` section as its heading line alone (id 13)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, the §2 preamble's definition of "Extracted" (61.md:54-55), as used by S13, AC13 and AC20.
- **What is wrong:** 61 makes unit 60 S1's bullet reader the meaning of "extracted" for every criterion. That reader stops at the next bullet, heading or blank line. On a `###` section it returns only the heading line, because the line after the heading is blank. This applies to 54's `### The oracle's head` in AC13 and to 44's `### The oracle` (44.md:71) in AC20.
- **Consequence:** AC13's `grep -c 'git rev-list'` prints 0 whatever the section holds, so that clause cannot fail. AC13's "names TOOL-dPlacedRequest-44" clause passes only if the pointer sits on the heading line itself. AC20 can never find `[ "$own" = 0 ]` before `merge-base --is-ancestor`. The builder gets criteria that are vacuous or impossible.
- **Fix (judged UNSOUND by the skeptic; this is the skeptic's corrected fix):** Narrow 61 §2's "Extracted" to S and AC bullets. Define a `###` section's extraction as running from its heading to the next `##` or `###` heading, e.g. `awk "/^### The oracle's head/{f=1;next} /^##+ /{f=0} f"`, so that a `# comment` line inside a code block does not end it. Restate AC13 and AC20 against that form. The build must probe that over 54 as it stands this prints a `git rev-list` count of 1, so AC13 is red before S13.
- **Left-shift gate:** A checklist entry: "each extraction form is probed over its real target, and a form that returns only a heading line is rejected". A spec lint could flag any criterion that applies a bullet reader to a `###` label.

## MEDIUM

### M1. S4's reverse direction and S12 require base wording that no unit writes (id 1)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S4 (with S12), §4 Files touched (61.md:221), §6 AC4.
- **What is wrong:** S4's reverse direction requires every inventory row's criterion, once extracted, to name `RUN.md` or `fixture's base`. 52 AC11, AC12 and AC17, 54 AC1 (it pins `c63aabbb`), 57 AC1, 59 AC21 and 43 AC24 name neither. 59 AC2 says `fixture's later base`, which a `fixture's base` grep misses. 59 S4 and S5 rewrite only some rows, and give 43 AC24 only "the run's base". S12 requires 43 AC24 to name `RUN.md`. Files touched leaves out 52 and 43.
- **Consequence:** Once 61 is built, the amended 59 AC3 and AC5 are red on a correct build. The builder must widen scope or weaken the check. No wrong behaviour ships, which is why the skeptic graded it medium, down from the finder's high.
- **Fix (judged SOUND by the skeptic):** Either add one item per row that writes the base wording into each criterion, and add 52 and 43 to Files touched and Edges, or limit the reverse direction to the rows 59 S4 and S5 rewrite. Spell the match as `fixture's( later)? base`, or name the exact phrase per row. Add a criterion that runs the reverse direction over the built folder and must print no red row.
- **Left-shift gate:** A checklist entry: "a new rule over an inventory is run over every row before it is written, and each red row gets an item that edits it".

### M2. The sweep hits 61's own criteria, and S1 places none of them (ids 2, 9, 23)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S1, S3 and S4, §4 Evidence (the sweep bullet, 61.md:198-201), §6 AC1 and AC20.
- **What is wrong:** §4's sweep runs over `spec/*.md`, which includes 60 and 61. Run over the folder as it stands, it also hits 61 AC4, AC13 and AC20. The pinned Evidence hit set predates 61, and it also leaves out 56 AC19. S1's inventory and Excluded lists name none of 61's hits. 61 AC20 runs the oracle on 54's no-merge fixture (61.md:319-322) and names no base.
- **Consequence:** AC1 ("every hit is a row of 54's inventory or of its Excluded sub-table") and 59 AC3's explicit-list comparison are red on a correct build. AC20 has no correct placement. As an inventory row it fails S4's reverse direction, and as a text-only exclusion it hides an oracle run.
- **Fix (judged SOUND by the skeptic):** Add 61 AC20 to S1's inventory rows, and reword AC20 to name `fixture's base` (on 54's no-merge fixture). Add 61 AC4 and AC13 to the `Excluded, text only` list, each with the phrase that matched. Re-measure the Evidence hit set with 60 and 61 present. Alternatively, state that the sweep excludes the batch's own spec, and why.
- **Left-shift gate:** A checklist entry: "a sweep's population includes the spec that defines it, and the pinned hit set is measured after that spec is written".

### M3. S10 leaves 57 AC2's `## Run facts` clause standing (ids 6, 16)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S10 (61.md:96-100) and §6 AC10 (61.md:288-289), against 57 AC2 (57.md:140-141).
- **What is wrong:** S10 replaces 44 AC1's Run-facts reader with `bash -c '. tools/unattended/lib-unattended.sh; extract_run_facts' < memory/builds/dPlacedRequest/RUN.md | sed ...`, which holds no `## Run facts` text. 57 AC2 still requires 44 AC1 to name `RUN.md` and `## Run facts`. S10 only adds that 57 AC2 must also name `extract_run_facts`, and never retires the old clause. AC10 greps the awk-regex spelling `/^## Run facts/`, so it misses 57 AC2's plain `## Run facts`.
- **Consequence:** On a correct build 57 AC2 goes red, or the builder pads 44 AC1 with the retired heading. AC10 catches neither outcome. The damage stays inside one criterion.
- **Fix (judged SOUND by the skeptic):** In S10, restate 57 AC2's clause "names `RUN.md` and `## Run facts`" as "names `RUN.md` and `extract_run_facts`". Add to AC10 that the extracted 57 AC2 bullet has `grep -c 'Run facts'` = 0, and that the extracted 44 AC1 still passes 57 AC2's name clause.
- **Left-shift gate:** Class amendment-leaves-its-other-half-standing. A checklist entry: "a replacement names every clause it retires, and its criterion greps for the retired text in every spelling it appears in".

### M4. The CRLF arm's `BINMODE=3` does not reach the driver's awk (ids 8, 22)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S11, §4 Evidence (the GNU Awk / BINMODE bullet), §6 AC11, §7 New arm.
- **What is wrong:** The spec says the CRLF row runs "under `BINMODE=3`" so the CR reaches the reader. On node a's GNU Awk 5.4.0, BINMODE keeps the CR only as an awk program variable (`-v BINMODE=3` or set in BEGIN). Set as an environment prefix, the natural reading of "run under", it leaves the CR dropped (reproduced: length 12 against 13). The driver's `read_claims` awk call (unattended.sh:2160-2172) passes no BINMODE, and the spec does not say how the arm gets it there.
- **Consequence:** An arm built as `BINMODE=3 <driver>` never feeds the CR to `CLAIM_KV_AWK` on node a. The CRLF row passes with or without the strip, so the staged break cannot go red and AC11's second clause fails on a correct build. Behaviour depends on the machine's awk. The effect stays inside the test arm, which is why the skeptic graded id 22 medium, down from the finder's high.
- **Fix (judged SOUND by the skeptic):** State the mechanism: awk sees `-v BINMODE=3`, or `BINMODE=3` in a BEGIN block, not an environment prefix. Say how it reaches the shared function. Either the driver's call that uses `CLAIM_KV_AWK` takes `-v BINMODE="${CLAIM_BINMODE:-0}"`, or the arm calls the function's awk directly with `awk -v BINMODE=3`. Correct the Evidence bullet to name the form that kept the CR. Make AC11 record that on node a the staged copy without the strip reads incomplete under that exact invocation. The build must run that staged break.
- **Left-shift gate:** Class fixture-inherits-ambient-machine-state. A checklist entry: "a platform knob in a test arm is spelled as the exact invocation, and its staged break is observed red on the machine the evidence came from".

### M5. AC4's first clause never observes S4's change to 59 AC3's pattern (id 11)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §6 AC4, first clause (61.md:267), which observes S4.
- **What is wrong:** The clause runs 61's own §4 sweep, whose pattern (61.md:164) already holds `oracle[^.]*(runs|run |prints|exits)`. 59 AC3 (59.md:240) still states `oracle[^.]*(runs|run )`. No 61 criterion reads 59 AC3's pattern.
- **Consequence:** The clause is green today. If S4's widening of 59 AC3 is never made, no criterion notices, and 59 AC3 keeps missing criteria worded "the oracle prints".
- **Fix (judged SOUND by the skeptic):** Have the clause extract 59 AC3 and require it to hold `oracle[^.]*(runs|run |prints|exits)`. Or run the pattern 59 AC3 states, not §4's, and require hits on 44 AC2 and 56 AC10.
- **Left-shift gate:** A checklist entry: "a criterion that observes an edit reads the edited text, and is shown red on today's tree".

### M6. F1 rests on a false account of the driver's shared-order behaviour (id 14)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §8 F1 (61.md:337-339), §5 risks (S7), and §4 Alternatives rejected, the last bullet.
- **What is wrong:** F1 rejects option (c), "a gate refusing a shared order over intersecting write sets", as "a new leg". It also says "under every option unit 56's pass there precedes 57's. That is harmless". 56 and 57 are both order 29, and 56 declares `consumes-from TOOL-dPlacedRequest-57`. The workflow sorts by order then id (unattended-build.js:608-613), so it reaches 56 first. `--dispatch` then refuses 56 with fail 49 while 57 is OPEN (unattended.sh:13746-13758, asserted at unattended.test.sh:6399-6411). The same verb already runs M6 condition 1's write-set intersection test (unattended.sh:13421).
- **Consequence:** The fork is resolved on a false account of the driver. The next change will read as harmless a precedence the code forbids. The chosen option (a) stands on its own, so the effect is contained.
- **Fix (judged SOUND by the skeptic):** Restate F1 and §5 risks from the driver's real behaviour. At the shared order, `--dispatch`'s edge refusal already forces 57 before 56, or refuses 56. Name that check as the existing seam for option (c), and drop "It is a new leg". S7's renumbering can stay as the fix that makes the index read true, with its reason corrected. The build must probe `--dispatch dPlacedRequest --pass TOOL-dPlacedRequest-56` with 57 OPEN at the current orders and see the fail-49 edge refusal.
- **Left-shift gate:** A checklist entry: "a claim about what the driver does at a fork cites the code line and a probe".

### M7. 44 §4's "whole head" sketch drops the base-resolve refusal (id 21)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S20, §4 "The oracle's head, stated once in 44 §4", §6 AC20.
- **What is wrong:** S20 calls its sketch "the whole head", and S13 makes 44 §4 its only statement. The sketch starts at `t=$(git rev-list ...)`. It leaves out `base=$1` and the `git rev-parse -q --verify "$base^{commit}" || ... base does not resolve` refusal. 54 S1 names that refusal as its first case, and 57 S1 and §5 rely on it for an empty base. 44 holds no rev-parse today.
- **Consequence:** A builder who writes 44 §4 to this sketch drops the empty or unresolvable base case. An empty `b` reaches `git merge-base --is-ancestor "$t" ""`, which exits 128 and prints "the ancestor test failed" instead of "base does not resolve". It still exits 2, so 57 AC1's exit-2 legs cannot tell a failed base read from a real refusal, and AC20 stays green. The path is narrow and the effect contained, which is why the skeptic graded it medium, down from the finder's high.
- **Fix (judged SOUND by the skeptic):** Put `base=$1` and the rev-parse base-resolve refusal at the top of the §4 sketch, ahead of `t=`. Add to AC20 that the extracted 44 §4 holds `base does not resolve` on a line before `rev-list`, and that the oracle run with an empty base prints it.
- **Left-shift gate:** A checklist entry: "a sketch that moves code into a single home is diffed, case by case, against the copy it retires".

### M8. The shared key reader misses a tab-only empty value (id 24)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S16, §4 "The shared key reader" sketch.
- **What is wrong:** The bare branch matches `/^[a-z-]+:[ ]*$/`, spaces only, while the trim removes blanks, tabs included. `renews:` followed by a tab holds no `: ` and fails the bare branch, so the key is never read and counts as absent.
- **Consequence:** A tab-only empty `renews` value takes the renewing-beat branch (52.md:222) instead of the empty-value branch, for which 52 S26 (52.md:149-152) prints `stale`. Only hand-edited claim bodies reach it. The skeptic graded it medium, up from the finder's low, because the decision changes.
- **Fix (judged SOUND by the skeptic):** Make the bare branch `/^[a-z-]+:[[:blank:]]*$/`, the same class the trim uses. Add a `renews:` plus tab row beside the two-space row in AC16.
- **Left-shift gate:** A checklist entry: "a key reader's match and trim use one whitespace class", with a tab row in every reader's fixture.

## LOW

### L1. S14 and AC14 restate an edit unit 60 already makes, and AC14 cannot fail (id 3)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S14, §6 AC14 (61.md:301-304).
- **What is wrong:** 60 S1 already makes both of 57 AC2's AC59 clauses, the no-sha test included, read the bounded output, and S14 restates that. AC14 runs only 60's fixed awk over a scratch copy of 34 and never reads 57 AC2's bullet.
- **Consequence:** AC14 is green before 61 is built, whatever 57 AC2 says. Two units claim the same edit to 57 AC2 (60 at order 30, 61 at order 33), which risks a second rev bump or a conflicting rewrite. 60 AC1 already observes the real edit, so nothing goes uncertified in practice.
- **Fix (judged SOUND by the skeptic):** Drop S14 and AC14 and cite 60 AC1 and AC2 as closing finding 6. Or make AC14 read 57's AC2 bullet and require its no-sha clause to run over the bounded read's output, with a Red when naming a 57 AC2 whose no-sha clause reads the unbounded range.
- **Left-shift gate:** A checklist entry: "an item that another unit already makes is cited, not restated".

### L2. S20 writes the oracle's head into 59 S21 as well as 44 §4 (id 4)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S13 (61.md:107-110) against S20 (61.md:129-131), §6 AC13 and AC20.
- **What is wrong:** S13 restates 59 S21 to point at 44 §4 alone. S20 says "59 S21 and the sketch in 44 §4 show the whole head". The head then lands in two specs, the drift S13 exists to remove. AC13 checks only 54's section and AC20 only 44 §4, so nothing observes S20's edit to 59 S21.
- **Consequence:** Drift only: scope-item prose duplicates a design sketch.
- **Fix (judged SOUND by the skeptic):** S20 should write the whole head into 44 §4 only and leave 59 S21 as a pointer, matching S13. Extend AC13 to require `grep -c 'merge-base --is-ancestor'` over 59's S21 extraction to print 0, with a pointer to 44 §4.
- **Left-shift gate:** Class two-answers-to-one-question. A checklist entry: "a 'stated once' item is checked by a criterion over every spec that held a copy".

### L3. AC19's fixture has no `## Run facts` heading, so S10's read prints nothing (ids 5, 12)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S10 and S19, §4 Evidence (the S10 read bullet, 61.md:207-208), §6 AC19 (61.md:316).
- **What is wrong:** AC19 and the Evidence describe a scratch file "holding `base:<sha>`" with CRLF endings. S10's read goes through `extract_run_facts` (lib-unattended.sh:2057), which prints only lines under a `## Run facts` heading. With no heading the pipeline printed nothing, and with a CRLF `## Run facts` line first it printed the sha. S19 cites `fact`'s semantics, not `extract_run_facts`'s. Both are section-scoped, but `[[:space:]]*` also strips tabs, which `fact` does not.
- **Consequence:** A fixture built from the text reads red on a correct build until the builder adds the heading. The Evidence as worded is not reproducible.
- **Fix (judged SOUND by the skeptic):** Have AC19 and the Evidence say the scratch file holds a `## Run facts` heading followed by `base:<sha>`, both with CRLF endings. Have S19 cite `extract_run_facts` (lib-unattended.sh:2057, section-scoped, CRs kept) plus the trailing `tr -d '\r'`, alongside `fact`'s space semantics.
- **Left-shift gate:** A checklist entry: "an Evidence fixture is written as the exact bytes the probe used".

### L4. AC4's first clause is green today and never reads 59 AC3 (id 7)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §6 AC4, first clause.
- **What is wrong:** This is the defect in M5, reported by another lens with a binding grade of low. The new pattern already lists 44 AC2 and 56 AC10, and the old pattern at 59.md:240 lists neither. AC4 runs §4's sweep, not 59 AC3's.
- **Consequence:** 59 AC3 could keep its old pattern, which misses "prints" criteria, and AC4 would still pass.
- **Fix (judged SOUND by the skeptic):** Extract 59's AC3 bullet and require that it holds `oracle[^.]*(runs|run |prints|exits)`. Then run that pattern and require that 44 AC2 and 56 AC10 are hits.
- **Left-shift gate:** As for M5.

### L5. 60 AC3 is green before unit 60 is built (id 10)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-60.md`, §6 AC3 (60.md:108), which observes S3.
- **What is wrong:** AC3 needs `grep -c 'TOOL-dPlacedRequest-60'` over 57's §9 to be at least 1. 57's §9 rev-2 line (the hands-off fold) already names it, so the count is 1 today.
- **Consequence:** S3, the rev bump with a §9 line naming this unit and AC2, is never observed. The defect is only in a record check.
- **Fix (judged SOUND by the skeptic):** Have AC3 require a §9 line that names both `TOOL-dPlacedRequest-60` and `AC2`, e.g. `grep -E 'TOOL-dPlacedRequest-60\b.*AC2'` over 57's §9. Or require 57's rev to move past rev-2. Confirm that it prints 0 today.
- **Left-shift gate:** A checklist entry: "every criterion is run on today's tree and must be red before its unit is built".

### L6. 60 S1 adds a second bullet reader beside 59 §4's join (id 15)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-60.md`, §2 S1 (60.md:30-32) and §10 (60.md:132).
- **What is wrong:** S1 writes `awk '/^- \*\*AC59\*\*/{f=1;print;next} f&&/^(- |#|$)/{exit} f'`. It copies the closers of 59 §4's join but not its line joining or `tr -s ' '`. 61 then reads with both: the join for the sweep, and 60's form for every "extracted" clause.
- **Consequence:** One criterion bullet has two readers that can disagree. A phrase that wraps across a continuation line is found by the join and missed by S1's form. No phrase differs today, so the effect is at most a false red on a later wrap.
- **Fix (judged UNSOUND by the skeptic; this is the skeptic's corrected fix):** Keep 60 S1's span (label to the next bullet, heading or blank line) as the one reader for every label, and join its output with `| tr '\n' ' ' | tr -s ' '`. Have 61 §2's "extracted" name that joined form.
- **Left-shift gate:** A checklist entry: "one reader per record shape, and a second reader states why the first does not serve".

### L7. 57 AC1 still points at S1's retired `awk` (id 17)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S10 and S8, §6 AC10, against 57 AC1 (57.md:131).
- **What is wrong:** S10 retires 57 S1's private awk reader, but its list (61.md:96-100) names only 57 S1, 57 §4 and 44 AC1. 57 AC1 reads "`b` is read by S1's `awk`", and S8 rewrites AC1 without retiring that phrase. AC10 reads three extractions instead of sweeping the tree.
- **Consequence:** A stale cross-reference survives in criterion prose, with no behavioural effect. Any copy of the old reader that a 57 or 59 pass writes elsewhere is also missed.
- **Fix (judged SOUND by the skeptic):** Add 57 AC1's "read by S1's `awk`" to S10's list, reworded to "read by S10's form". Make AC10 a tree sweep: `grep -rln '/\^## Run facts/\|S1.s .awk.' memory/builds/dPlacedRequest/spec/` should print no live spec except unit 61 itself.
- **Left-shift gate:** Class retirement-inventory-misses-readers-by-value. A checklist entry: "a retirement's list of readers comes from a tree grep recorded in Evidence".

### L8. S7's renumbering leaves stale order prose that AC7 does not check (id 18)

- **Where:** `2026-10-25-spec-TOOL-dPlacedRequest-61.md`, §2 S7 (61.md:78-83), §6 AC7 (61.md:276-279).
- **What is wrong:** S7 renumbers 56, 58 and 59. Its update list includes 59 §3's "No renumbering" bullet but not 56 §3's identical bullet (56.md:132). AC7 checks the headers, step 29 of the index, 56 §1 and 58 §1. It never checks 59 §1 ("at order 31, after unit", 59.md:28) or the shared-order edges at 56.md:151 and 57.md:67.
- **Consequence:** After the pass, 56 says "No renumbering of any order" while its own header has moved from 29 to 30. Other order prose can stay stale while AC7 passes. Only the order record, which the next plan reads, is affected.
- **Fix (judged SOUND by the skeptic):** Add 56 §3's no-renumbering bullet to S7's list. Extend AC7: 59 §1 names `order 32` and `order 31`, and `grep -c 'shared order\|at this order'` over the extracted edges of 56 and 57 prints 0.
- **Left-shift gate:** A checklist entry: "a renumbering greps every spec for the old order numbers and order phrases before it is written".

review-shape kind=spec-audit round=1 intensity=full at=synth raw=24 confirmed=22 refuted=2 unverified=0 blocker=0 high=1 medium=12 low=9 agents=11 out-tokens=149865

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S4 (with S12), section 4 Files touched, section 6 AC4 | high | medium | confirmed | Confirmed by re-probe. I extracted each row with the finder's awk. 52 AC11, AC12 and AC17, 54 AC1, 57 AC1, 59 AC21 and 43 AC24 contain neither `fixture's base` nor `RUN.md`. 59 AC2 says `fixture's later base`, so a plain `fixture's base` grep misses it. 52 AC11 reads 'When the oracle runs on S14's fixture ... exits 1' and 54 AC1 pins `c63aabbb`. The rewrites in 59 S4 and S5 (spec-59.md:66-70) cover only 55 AC1 and AC2, 52 AC29, 56 AC6 and AC10, 44 AC2 and AC3, and 43 AC24. For 43 AC24 they give only 'the run's base'. 61's Files touched (spec-61.md:221) leaves out 52 and 43, so no unit adds the base wording that the reverse direction (S4) and S12's `RUN.md` clause require. The amended 59 AC3 and AC5 are red on a correct build. Graded medium rather than high: the effect is a criterion that cannot go green and forces scope widening, and no wrong behaviour ships. | sound | - |
| 2 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S1/S3, section 4 Evidence, section 6 AC1 and AC20 | medium | medium | confirmed | I re-ran §4's sweep over the spec folder. It printed the same 24 hits the finder lists, ending 59 AC13, 59 AC21, 61 AC4, 61 AC13 and 61 AC20. The Evidence hit set (spec-61.md:198-201) leaves out 56 AC19 and all of 61's own hits. S1's general 'every sweep hit that runs no oracle' could cover 61 AC4 and AC13 as excluded rows. 61 AC20, though, runs the oracle on 54's no-merge fixture (spec-61.md:319-321) and names no base. S1 adds inventory rows only for 59 AC2, AC4, AC5 and AC21. So AC20 is either missing from the inventory, which fails AC1, or a row that fails S4's reverse direction. | sound | - |
| 3 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S14, section 6 AC14 | medium | low | confirmed | 60 S1 (spec-60.md, §2) already says 'Both of AC2's clauses on AC59, the name and the no-sha test, read that output', so 61 S14 restates an edit unit 60 makes. 61 AC14 (spec-61.md:301-304) runs only 60's fixed awk over a scratch copy of 34 and never reads 57's AC2 bullet. Its result does not depend on the tree, so it is green before 61 is built and cannot fail. Graded low because 60 AC1 already observes the real edit, so nothing goes uncertified in practice. | sound | - |
| 4 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S13 against S20; section 6 AC13 and AC20 | medium | low | confirmed | S13 (spec-61.md:107-110) restates 59 S21 to name 44 §4 alone. S20 (spec-61.md:129-131) says '59 S21 and the sketch in 44 §4 show the whole head', so the head text lands in both 59 S21 and 44 §4. AC13 extracts only 54's head section, and AC20 only 44 §4 and the fixture. Nothing observes S20's edit to 59 S21. 59 S21 today reads 'Written into 44 §4 and 54 §4's sketch' (spec-59.md:118-120). The duplication is scope-item prose against a design sketch, so its effect is cosmetic or drift-only. Hence low. | sound | two-answers-to-one-question |
| 5 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S10/S19, section 6 AC19 | medium | low | confirmed | Reproduced. Feeding `base:<sha>` CRLF with no heading to `extract_run_facts` (lib-unattended.sh:2057, section-scoped) through the S10 pipeline printed nothing (od: 0000000). With a `## Run facts` CRLF line first, it printed c63aabbb4a73d44315dd5dd1219ff1dac5055cf8. So AC19's fixture, read literally, is red on a correct build. The finder's side claim is wrong, though: `fact` (unattended.sh:1359-1375) is section-scoped too, not 'whole file, first match'. S19 cites it only for the CR and space semantics. The one real difference is that `[[:space:]]*` also strips tabs, which `fact` does not. Graded low: the builder only has to add the heading. | sound | - |
| 6 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S10, section 6 AC10 | medium | medium | confirmed | 57 AC2 (spec-57.md:140-141) requires 44's AC1 bullet to name `RUN.md` and `## Run facts`. 61 S10 (61.md:96-100) swaps 44 AC1's reader for the `extract_run_facts` form, which holds no `## Run facts` text, and only says 57 AC2 'requires 44 AC1 to name `extract_run_facts`'. It never retires the old clause. AC10's `grep -c "/\^## Run facts/"` only matches the literal awk regex `/^## Run facts/`, so it would not catch 57 AC2 still asking for the backticked `## Run facts`. If 57 AC2 keeps that clause, it goes red on a correctly rewritten 44 AC1 unless prose is padded in. | sound | - |
| 7 | coherence | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 6 AC4 first clause | low | low | confirmed | I re-ran §4's sweep. With the new pattern `oracle[^.]*(runs\|run \|prints\|exits)` it already lists 44 AC2 and 56 AC10. With the old pattern `oracle[^.]*(runs\|run )` it lists neither. spec-59.md:240 still holds the old pattern. AC4's first clause runs §4's own sweep, not 59 AC3's, so it is green today and nothing checks that S4 changed 59 AC3's pattern. | sound | - |
| 8 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S11, section 4 Evidence (GNU Awk bullet), section 6 AC11, section 7 New arm | medium | medium | confirmed | Reproduced with GNU Awk 5.4.0 on a file holding `status: live` + CRLF. Plain awk gave length 12. `BINMODE=3 awk` given as an env prefix also gave 12 (piped too). `awk -v BINMODE=3` gave 13, and so did `BEGIN{BINMODE=3}`, both from a file and through a pipe. So the spec's 'run under `BINMODE=3`' (S11, AC11, §4 Evidence) only keeps the CR when BINMODE is an awk variable. The spec never says how the arm gets that variable into the driver's awk. Built as an env prefix, the CRLF row passes with or without the strip, so the staged break cannot go red. | sound | - |
| 9 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S1 and S3, section 4 Evidence (sweep bullet), section 6 AC1 and AC20 | medium | medium | confirmed | I re-ran §4's sweep over spec/*.md. It printed the pinned set plus `61 AC4;61 AC13;61 AC20`. 61 AC20 (61.md:319-322) runs the oracle on 54's no-merge fixture, so it belongs in the inventory. S1 adds inventory rows only for 59 AC2/AC4/AC5/AC21. AC20 also names neither `fixture's base` nor `RUN.md`, so as an inventory row it would be red under S4's reverse rule. S1's excluded list is only partly worded as 'among them', so 61 AC4 and AC13 are not named. The Evidence hit set is pinned without unit 61's own criteria. | sound | - |
| 10 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-60.md:section 6 AC3 (observes S3) | medium | low | confirmed | 60 AC3 (60.md:108) needs at least 1 for `grep -c 'TOOL-dPlacedRequest-60'` over 57's §9. 57's §9 rev-2 line already names `TOOL-dPlacedRequest-60` (the hands-off fold), so the count is 1 today and AC3 passes before the unit is built. S3's rev bump naming this unit and AC2 is never observed. The defect is only in a record check. | sound | - |
| 11 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 6 AC4 (first clause, observes S4) | medium | medium | confirmed | 61.md:267 AC4's first clause runs '§4's sweep', and §4 (61.md:164) already greps `oracle[^.]*(runs\|run \|prints\|exits)`. 59.md:240 AC3 still states `grep -E 'oracle[^.]*(runs\|run )'`. No 61 criterion reads 59 AC3's pattern: grep for '59 AC3' in 61 finds only S2/S3/S4 and AC2/AC3, and those test the label anchor and the comparison, not the pattern. So the clause is green today and never observes S4's edit to 59 AC3. | sound | - |
| 12 | grounding | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 4 Evidence (S10 read bullet), section 6 AC19 | low | low | confirmed | S10's read (61.md:98) pipes through extract_run_facts. lib-unattended.sh:2057 is `awk '/^## /{ sec = (index($0, "## Run facts") == 1); next } sec'`, so it prints nothing until a `## Run facts` heading appears. A file that holds only `base:<sha>`, as AC19 (61.md:316) and the Evidence bullet (61.md:207-208) word it, prints an empty base. The CR on the heading line does not break index()==1, so the proposed heading-plus-CRLF fixture works. | sound | - |
| 13 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 preamble (the "Extracted" definition), as used by S13, AC13 and AC20 | high | high | confirmed | 61.md:54-55 defines 'Extracted' as 60 S1's form, which stops at the next bullet, heading or blank line. I ran that form with the label `### The oracle's head` over 54. It printed only the heading line, because line 79 is blank. AC13's `grep -c 'git rev-list'` = 0 therefore passes whatever the section holds, and its 'names TOOL-dPlacedRequest-44' clause can only pass if the pointer sits on the heading line. AC20 has the same problem with 44's `### The oracle` (44.md:71): it can never find `[ "$own" = 0 ]`. The section form to the next `### ` heading printed a rev-list count of 1. Built as written, the builder gets a vacuous clause and impossible ones, so the grade is high rather than blocker, since the impossible clauses would surface. | unsound | - |
| 14 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 8 F1 and section 5 risks (S7); section 4 Alternatives rejected, the last bullet | medium | medium | confirmed | 56.md:3 and 57.md:3 are both order 29. 56.md:151 declares consumes-from 57. unattended-build.js:608-613 sorts by order and then by id, so 56 comes before 57. unattended.sh:13746-13758 refuses `--dispatch` (fail 49) for a consumer whose own-build producer is not CLOSED or WONTDO, and unattended.test.sh:6399-6411 asserts that refusal at the same order. 61.md:337-339 F1 claims that 56's pass 'precedes 57's. That is harmless', but the driver refuses that order. The account F1 rests on is false. The chosen option (a) stands on its own, so the effect is contained. | sound | - |
| 15 | reuse | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-60.md:section 2 S1 and section 10 | low | low | confirmed | 60.md:30-32 S1 writes its own line-preserving awk, and 60.md:132 §10 says it copies the closers of 59 §4's join without reusing that join, which also joins continuation lines and squeezes spaces. A phrase that wraps across a continuation line is found by the join and missed by S1's form, so one criterion bullet has two readers that can disagree. I re-probed the phrases 61 currently extracts (59 AC4 'fixture's base' and others): none differs today, so the effect is at most a false red on a later wrap. Low. | unsound | - |
| 16 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S10, section 6 AC10 | medium | medium | confirmed | 57.md:140-141 still requires 44's AC1 bullet to name `RUN.md` and `## Run facts`. 61 S10 (61.md:96-100) gives 44 AC1 the form `bash -c '. tools/unattended/lib-unattended.sh; extract_run_facts' < .../RUN.md \| sed ...`, which does not contain `## Run facts`. It only says 57 AC2 'requires 44 AC1 to name `extract_run_facts`', without saying the old clause is replaced rather than added to. AC10 (61.md:288-289) greps `/\^## Run facts/`, the awk-regex spelling. A grep for 'Run facts/' found it only at 57.md:40 and :77 and 61.md:289, so 57 AC2's plain `## Run facts` text would not trip it. Built as written, a correct build either fails 57 AC2 or pads 44 AC1 with the retired heading. The damage stays inside one criterion. | sound | amendment-leaves-its-other-half-standing |
| 17 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S10/S8, section 6 AC10 | low | low | confirmed | 57.md:131 (AC1) reads '`b` is read by S1's `awk`'. S10 replaces S1's awk read with the extract_run_facts form, and S8 rewrites AC1, but neither retires that phrase. S10's list (61.md:96-100) names only 57 S1, 57 §4 and 44 AC1. AC10 reads only 57 S1, 57 AC2 and 44 AC1, so the stale reference survives without a red. Grep found the phrase only at 57.md:131, plus the awk at 57.md:40 and :77. The result is a stale cross-reference in criterion prose with no behavioural effect. | sound | retirement-inventory-misses-readers-by-value |
| 18 | blast-radius | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S7, section 6 AC7 | low | low | confirmed | 56.md:132 reads '- No renumbering of any order: ...', and S7 (61.md:78-83) does not list it, although it does list 59 §3's matching bullet (59.md:128). AC7 (61.md:276-279) checks the headers, step 29 of the index, 56 §1 and 58 §1. It never checks 59 §1 ('at order 31, after unit' at 59.md:28) or the shared-order edges at 56.md:151 and 57.md:67. Those can stay stale while AC7 passes. Only the order record is affected. | sound | - |
| 19 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-60.md:section 2 S1, section 3 Non-goals | high | - | refuted | The premise is false on re-probe. H1's defect is a spelled-out unbounded range: 57 AC2 extracts 34 AC59 'the same way' as 44 AC1, an awk that closes only at the next AC bullet (57.md:140-142). 49 AC3 (49.md:291-292, 'AC59 there names `TOOL-dPlacedRequest-44`') and 54 AC3 (54.md:156-158, 'When the AC59 bullet ... is read') state no extraction range at all. They read 'the AC59 bullet', which by its plain meaning ends where the bullet ends, so no stated read in either runs on into §7 to §10. The defect unit 60 closes is absent from both. | unsound | - |
| 20 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S8, section 5 error/empty states, AC8 | high | - | refuted | The premise is false on re-probe. The finder measured the current spec run, which does not build unit 57. The README's build-level rule says the spec run specs and defers every unit and closes by carry-forward. 57 §1 (57.md:26-29) says unit 57 is built in the build run that forks after this spec run lands. push-main.sh:880 gives that landing the subject `merge: $SLUG — land onto ...`. unattended.sh:5206-5219 says the build tracks the landed spec run's record as a rotated `RUN.LANDED.<blob8>.md`. So in the run that builds 57, both inputs exist: the dPlacedRequest landing merge and its archive. `git log --all` shows no earlier dPlacedRequest landing (0 'merge: dPlacedRequest' subjects), so exactly one archive will match the glob. The dOrderedCharter merge and the missing archive the finder saw are facts about this spec run only. The zero-match and several-match cases are speculative edges, not paths the build run takes. | unsound | - |
| 21 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S20, section 4 'The oracle's head, stated once in 44 §4', AC20 | high | medium | confirmed | 61.md S20 says the sketch in 44 §4 shows 'the whole head', and the §4 sketch titled 'The oracle's head, stated once in 44 §4' starts at `t=$(git rev-list ...)`. It has no `base=$1` and no `git rev-parse -q --verify "$base^{commit}" \|\| ... base does not resolve`. 54.md §4's sketch has both, and 54 S1 names that refusal as its first case. S13 turns 54's head section into a pointer to 44 §4, and grep finds no rev-parse in 44 today, so 44 §4 would be the only copy and it would lack the guard. 57 S1 and §5 rely on that guard for an empty b. On a narrow path (an empty or unresolvable base) the oracle would still exit 2 but print the wrong reason. 57 AC1 checks `no prepared merge` and exit 2, so it does not catch this. The effect is contained, so I grade it medium. | sound | - |
| 22 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S11, section 4 Evidence (BINMODE bullet), AC11, section 7 New arm | high | medium | confirmed | I re-probed with GNU Awk 5.4.0 on a CRLF file. Default awk printed 12, env `BINMODE=3 awk` printed 12, `awk -v BINMODE=3` printed 13, and a pipe with -v printed 13. So BINMODE only takes effect as a program variable. 61 S11, AC11 and §7 say only 'under `BINMODE=3`' and never say how it reaches the awk. The read_claims awk call at unattended.sh:2160-2172 passes no BINMODE. An arm written with the env form leaves the CR dropped on node a, and the staged copy without the strip cannot go red. That arm's clean reading is waived for this landing. The effect stays inside the test arm, so I grade it medium. | sound | fixture-inherits-ambient-machine-state |
| 23 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S1/S4, section 4 Evidence (sweep bullet), AC1, AC20 | medium | medium | confirmed | I ran 61 §4's join and sweep loop over the spec folder. It printed the finder's set exactly, ending 59 AC21; 61 AC4; 61 AC13; 61 AC20. 61 AC20's joined text says 'on 54's no-merge fixture row the oracle prints `no prepared merge on HEAD`' and names neither RUN.md nor `fixture's base`. Made an inventory row, it fails the reverse rule S4 adds. Excluded as text only, it hides an oracle run. S1's 'among them' would let a builder place 61 AC4 and AC13 as text only, but AC20 has no correct placement as written, so AC1 or the S4 reverse leg goes red. | sound | - |
| 24 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-61.md:section 2 S16, section 4 'The shared key reader' sketch | low | medium | confirmed | In 61 §4's sketch, `renews:` followed by a tab holds no ': ', so p is 0. It also fails the bare regex `/^[a-z-]+:[ ]*$/`, which allows spaces only, so k is never set and the key reads as absent. 52 S26 (52.md:149-152) says the walk reads the key on any line beginning `renews:` with its value trimmed, so the empty value reads on as `no`. 52.md:222 sends an absent key to the renewing-beat branch. So such a line takes the renewing-beat branch, a different decision from the one 52 S26 specifies. Only hand-edited bodies reach it, but behaviour changes, so I grade it medium rather than low. | sound | - |
