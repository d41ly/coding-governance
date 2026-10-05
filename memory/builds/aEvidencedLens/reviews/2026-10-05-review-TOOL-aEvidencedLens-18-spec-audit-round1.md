**Serves:** spec-audit TOOL-aEvidencedLens-18

# aEvidencedLens — spec audit of TOOL-aEvidencedLens-18, round 1

*Node `a`, 2026-10-05. This is a Tier-2 adversarial pass over the spec for unit 18, which the build
promoted to close the gaps the unit-15 audit found. Five finder lenses ran, then a skeptic stage
prompted to refute each finding, then one synthesis. Findings are graded by consequence under the
run's severity rubric, and each confirmed finding keeps the grade the run bound it to.*

**Round: 1.** Range reviewed: the subject below, pinned at the blob it was read at, plus the tree it cites.

- `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md@b6e31e95151f022df57c02e7387aef5b5093a53f`

## Verdict: BLOCKED

One high finding survived. The byte tie that S1 adds to close the id-5 gap uses plain
`git hash-object`, and on this node that command runs the CRLF clean filter. A CRLF-rewritten copy
of the harness therefore hashes equal to its LF blob, so the new check certifies a tie it does not
check. The spec should not be dispatched until S1, the section 4 pseudo-code and AC1 are fixed.
Three medium findings and eleven low findings are also confirmed. All of them are defects in the
spec's acceptance text, its premise or its declared records. None of them changes what the driver
observes.

## Review shape

Intensity full, raw 16, confirmed 15, refuted 1, unverified 0 (0 uncertain), precision 0.94.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| failure-envelope | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

By item, the adjudicated tally is 0 blocker, 1 high, 2 medium and 6 low, which makes 9 items.

By raw confirmed finding, it is 0 blocker and 1 high (id 14). There are 3 medium (ids 7, 12 and 15)
and 11 low (ids 1, 2, 3, 4, 5, 6, 8, 9, 10, 11 and 16).

The one refuted finding, id 13, was refuted as a duplicate of id 16 rather than as false.

Ids 7 and 14 describe the same defect. They are kept as two items because their binding grades
differ: medium for 7 and high for 14. The high grade is the one to act on. The rubric's high band
names "a check that certifies what it does not check" on a narrow path, and that is what S1 is.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate
  refutations demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 13 judged sound, 2 judged UNSOUND, 0 with no fix proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic (ids 1 and 2,
  medium to low).
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 16 spec documents were supplied as `specs`, as sibling context.
- Checklist: 13 items, each assigned to exactly one of 5 lenses (coherence 3, grounding 3, reuse 3,
  blast-radius 2, failure-envelope 2).
- Move check: no checked subject moved.

Every counter above that could mark the run incomplete is zero, so this run is complete.

## Findings

### HIGH — id 14: S1's byte tie reads equal for CRLF-mangled bytes, and has no staged break

**Where:** `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md`, section 2
S1, section 6 AC1 and section 5 testing.

S1 ties each saved file to its blob with plain `git hash-object`, which applies the path's clean
filters. On this node `core.autocrlf=true` comes from the system gitconfig, and
`tools/workflows/tier2-review.js` is `text eol=lf`. The skeptic reproduced this in scratch. A
`sed 's/$/\r/'` copy of head.js hashed to `3faf86625e60…` with plain `hash-object` and with
`--path=`, which equals the blob that `rev-parse` names. `--no-filters` printed `7732dff5caaf…`
instead.

A PowerShell redirect or a text-mode write produces exactly that input, and PowerShell is this
node's primary shell. So the ledger would record a byte-identity proof for bytes the driver did not
run on, which is the id-5 class this unit exists to close. Section 5 testing names only S2 and S3 as
liveness arms. S1's new refusal is never observed RED, against the build README's rule that every new
refusal is observed RED on a staged break.

**Fix (judged SOUND by the skeptic):** spell the assertion as
`git hash-object --no-filters <file>` == `git rev-parse <rev>:<path>`, or compare bytes with `cmp`
against `git cat-file blob <rev>:<path>`. Save each file with `git cat-file blob <rev>:<path> >
<scratch>/x.js` from bash, never through a PowerShell redirect. Add an AC1 liveness arm that the
build runs in scratch. A CRLF copy of head.js (`sed 's/$/\r/'`) and, separately, a one-byte append
must each red the S1 assertion and name the file. Record both outcomes in the S6 ledger.

**Left-shift gate:** a check over spec and brief text that refuses a bare `git hash-object` used as
an identity assertion without `--no-filters`. Pair it with a `checklist` entry for spec audits: "an
equality between a file and a blob runs with filters off".

### MEDIUM — id 7: the same filter defect, seen from grounding

**Where:** same spec, section 2 S1, section 4 "The completed observation", section 6 AC1.

This is the same reproduction as id 14, from the grounding lens. The skeptic graded it medium
because JS template literals normalise CRLF, so the prompts the driver observes are unaffected and
the damage is confined to the record. The run binds that grade, so this item stays medium. Id 14's
high grade governs the action, and the two share one fix.

**Fix (judged SOUND by the skeptic):** use `git hash-object --no-filters <file>` in S1, in the
section 4 pseudo-code and in AC1, or `cmp` each saved file against
`git cat-file blob <rev>:tools/workflows/tier2-review.js`. The ledger records which form ran. The
build also runs the probe: write a CRLF copy of head.js into scratch, confirm the AC1 equality reds
on it, then discard the copy.

**Left-shift gate:** as id 14.

### MEDIUM — ids 12 and 15: S5 hard-codes "the build's last open unit", the instance and not the class

**Where:** same spec, section 2 S5, section 4 "Files touched" (last bullet), section 6 AC5.

S5 states that unit 18 "is then the build's last open unit". AC5 then requires this pass to write
`memory/LIVE.md` and `memory/ledger/2026-10.md`. This audit is unit 18's first spec audit; README
line 104 lists TOOL-aEvidencedLens-18 as never yet named by one. Under BUILD-METHOD every confirmed
finding is promoted into a batched unit ordered after its subject, and this audit confirms fifteen.
`gen_build_index.py:745-748` returns the first PRECEDENCE token any unit holds, so a promoted unit at
SPECCED keeps the build at SPECCED. Unit 18's close then writes neither index. AC5 reds on a correct
build, and the dispatch row declaring both indexes is never closed by a pass write. That is the id-3
defect from unit 15's audit, moved one unit along.

**Fix:** the two findings proposed overlapping fixes. id 12's fix was judged SOUND by the skeptic.
id 15's was judged UNSOUND, and the skeptic's corrected fix is written below in its place. The
corrected fix subsumes id 12's, so apply it:

> Declare memory/LIVE.md and the month's ledger shard at dispatch if and only if gen_build_index's
> derived build status with this unit flipped to CLOSED differs from the status currently rendered.
> Otherwise declare neither. AC5 reds when any commit of the pass writes an undeclared index, or when
> the dispatch declares an index that no commit of the pass writes. It reads every commit of the
> unit's pass, not a single "pass commit".

The ledger records which branch held, as id 12's fix asks. If the build would rather not derive this,
id 12's sound alternative is a section 8 line: a promotion from this audit moves the closing write set
to the promoted unit, with S5 and AC5 amended to match.

**Left-shift gate:** a spec-token check that refuses the phrase "last open unit" (and its kin) in a
spec section 2 unless the same spec states the conditional derivation. Better still, `--dispatch`
computes the closing write set itself from the derived-status delta, so no spec can assert it.

### LOW — ids 1, 4 and 11: clauses that are green before the build and cannot red

**Where:** same spec, section 2 S1 and section 6 AC1 (ids 1 and 11); section 6 AC5, first clause
(ids 4 and 11).

AC1's hash-object red-when holds by construction for a file saved with `git show <rev>:<path>`. The
skeptic printed `54cf03a3…` twice at `028b5cac` and `3faf8662…` twice at HEAD, and no criterion
stages a break that observes it red. AC5's first clause reads unit 15's pass commits, which are
fixed history: `git show --name-only d239695c6 ad25d88c3` lists neither index. It also says "pass
commit" in the singular, although unit 15's pass was two commits. Id 14's fix supplies the missing
staged break, and with filters off the AC1 clause becomes live.

**Fix (all three judged SOUND by the skeptic):**
- id 1: add to AC1 a scratch `head-x.js`, which is head.js with one byte appended. The assertion over
  it against `rev-parse HEAD:tools/workflows/tier2-review.js` reds and names the file, and the ledger
  records that red beside the two equalities.
- id 11: for AC1, either drop the hash-object red-when or make it observable. For example, stage a
  dirty working copy of `tools/workflows/tier2-review.js`, described in the brief and not done by a
  reviewer. Then show head.js from `git show` still hashes to the rev-parse blob while the working
  copy does not. For AC5, record the first clause as a historical observation naming both unit-15
  pass shas, `d239695c6` and `ad25d88c3`, rather than as a criterion that can fail.
- id 4: record the unit-15 clause as a precondition read once into the ledger, and keep AC5's
  observation to this unit's dispatch row and commit.

**Left-shift gate:** a `checklist` entry for spec audits: "every red-when names the staged break
that turns it red, or is labelled a precondition". A spec-token check could then refuse a `Red when:`
line in section 6 with no break or precondition label near it.

### LOW — ids 5 and 9: section 1's "four missing pieces" premise is stale; S3 re-closes a defect the seam lacks

**Where:** same spec, section 1, section 2 S3, section 6 AC3 (and the section 10 reuse paragraph).

Spec 18 was committed at `e4dd6c85b`, before unit 15 built. Unit 15's ledger
(`build/2026-10-05-build-TOOL-aEvidencedLens-15-1-acceptance-ledger.md`, written by `d239695c6`,
amended by `ad25d88c3`) already records the following:
- all four prints: r1 `aada6477` against `6380ce0a`, r2 `30f26c60` against `62ba7747`, pairwise
  distinct;
- an object-database head.js run;
- the `--mask-key` red in both arg sets, with each HEAD print.

`u15-check.js:73-91` loops over both ARGSETS and counts reds without exiting. It exits only after
the loop. So AC3's "the driver stops after one red" cannot fire against the driver S3 reuses. What
the ledger still lacks is the S1 byte tie and the S2 step-3 break.

**Fix (both judged SOUND by the skeptic):** amend section 1 to say unit 15's ledger already carries
the four prints and the per-arg-set reds. Rescope S3 and AC3 to cite that ledger and the two pass
commits. Keep only what the ledger lacks, which is the pairwise-distinct cross-check, and require
the re-run prints to equal unit 15's recorded `aada6477`, `6380ce0a`, `30f26c60` and `62ba7747`.
Drop the stops-after-one-red clause, or turn it into a staged break of the driver that the build
observes red, such as an early `process.exit` after the first red. Amend the section 10 reuse
paragraph to match.

**Left-shift gate:** none mechanical. Add a `checklist` entry: "a spec written before a sibling unit
built re-reads that sibling's ledger at dispatch and strikes premises it already discharged".

### LOW — ids 6, 10 and 16: unit 15's step-1 break is called `broken1.js`, and its rebuild is undefined

**Where:** same spec, section 2 S2, section 4 sketch, section 6 AC2 and its preamble, section 5
risks.

Unit 15's AC3 (spec-15 line 154), its ledger and the scratch folder all name the step-1 break
`broken.js`. Spec 18 calls it `broken1.js` at lines 46, 115 and 179, and no `broken1.js` exists. The
rebuild-when-absent rule in section 5 and the section 6 preamble covers only `u15-check.js`, although
section 3 Edges also consumes the step-1 break. The exact edit is recorded only in unit 15's ledger.
A fresh session could therefore stage a different step-1 edit and compare against a break unit 15
never observed.

**Fix (all three judged SOUND by the skeptic):** name it `broken.js` (scratch `u15/broken.js`), as
unit 15's AC3 and ledger do, or state that `broken1.js` is that file renamed. Extend the rebuild
sentence, and its ledger note, to the break by its recorded edit. That edit is head.js with step 1's
`forward slashes (a relative answer` changed to `backward slashes (a relative answer`, with one
occurrence asserted.

**Left-shift gate:** a spec-token check that resolves every scratch artefact a spec says it consumes
from a sibling unit against the names in that sibling's ledger, refusing a name the sibling never
recorded.

### LOW — id 2: AC6 records AC5's outcome for the very commit that writes the ledger

**Where:** same spec, section 6 AC5 and AC6, section 2 S6.

AC5's second half observes that "this unit's pass commit writes both" indexes. AC6 requires the
ledger to carry that outcome, and the ledger is written in the same pass commit, so it cannot
observe its own commit. `.githooks/pre-commit` adds nothing to the staged set, so a pre-commit
observation is accurate. The same applies to AC4's "after this pass" hygiene run.

**Fix (judged SOUND by the skeptic):** restate AC5's second half as observed pre-commit:
`git diff --cached --name-only` at the pass commit lists `memory/LIVE.md` and
`memory/ledger/2026-10.md` and nothing outside the dispatch row. Alternatively, name a follow-up
ledger commit inside the dispatch set that records `git show --name-only <pass sha>`. Id 12/15's
conditional fix changes which indexes appear, not this timing.

**Left-shift gate:** a `checklist` entry: "a ledger criterion never observes the commit that
contains the ledger".

### LOW — id 3: AC4's rev-bump clause is already green for all three specs

**Where:** same spec, section 6 AC4, section 2 S4.

At HEAD, spec-1 is `CLOSED · rev-3`, spec-12 is `CLOSED · rev-4` and spec-15 is `CLOSED · rev-2`.
Each already has a section 9 line naming section 3. So "each of the three carries a bumped rev with a
§9 line naming §3" cannot observe S4's bump. The edge clauses can still fail.

**Fix:** the finder's proposal was judged UNSOUND, because it had unit 15's own section 9 line name
TOOL-aEvidencedLens-15. The skeptic's corrected fix: name the revs AC4 expects, which are unit 1 at
rev-4, unit 12 at rev-5 and unit 15 at rev-3. In units 1 and 12, the new section 9 line names
TOOL-aEvidencedLens-15. In unit 15, the new section 9 line names TOOL-aEvidencedLens-12 and
TOOL-aEvidencedLens-1.

**Left-shift gate:** a `checklist` entry: "a rev-bump criterion names the target rev number, never
'a bumped rev'".

### LOW — id 8: section 4 says `round` feeds inputPrint; it feeds only the key

**Where:** same spec, section 4 Evidence, second bullet.

`tools/workflows/tier2-review.js:696-697` builds inputPrint from shape, context, byDesign,
priorFindings, lensNotes, specs, checklist and intensity, and conditionally from probeRules and
prevBlobs. `round` enters only `deriveReviewKey` at line 702. The conclusion still holds, because
the two arg sets differ in checklist, specs and priorFindings.

**Fix (judged SOUND by the skeptic):** reword the bullet. The inputs include checklist, specs and
priorFindings, the two arg sets differ in those, and so their prints are distinct. `round` is part
of the key, not of the print.

**Left-shift gate:** none worth building for one sentence. Prose that names a function's inputs
should cite the line it read.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S1, section 6 AC1 | medium | low | confirmed | Re-probed: git show 028b5cac:tools/workflows/tier2-review.js > scratch/base.js, then git hash-object vs git rev-parse printed 54cf03a30ce84f777247baeca5ce54a3a6410540 twice, so the two values are equal by construction. Spec-18 lines 168-175 (AC1) give a 'Red when' for a hash mismatch but stage no break that observes it. The build README's rule 'Every new refusal or gate clause is observed RED on a staged break before it lands' is therefore unmet for S1's new clause. Graded low rather than medium: because the bytes come from the object database, the recorded tie holds whether or not the assertion code is right. The defect is an assertion with unproven liveness and an unmet build rule, not a wrong result. | sound |
| 2 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 6 AC5 and AC6, section 2 S6 | medium | low | confirmed | Spec-18 AC5 (lines 194-198) asks that 'this unit's pass commit writes both' indexes. AC6 (lines 199-203) requires the acceptance ledger to carry AC5's outcome. S6 and the files-touched list put that ledger in this same pass's write set. So the ledger cannot record a git show --name-only of the commit that contains it, and the spec names no follow-up commit. Unit 15 did land a ledger-only follow-up, ad25d88c3 (git show --name-only lists only the ledger), but for a format reason, not to record its own commit. The gap is real but small. A grep of .githooks/pre-commit for gen_build_index, LIVE.md and git add matched nothing, so the staged set equals what the commit writes and a pre-commit observation is accurate. The effect is wording only, so low. | sound |
| 3 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 6 AC4, section 2 S4 | low | low | confirmed | At HEAD, spec-1 is 'CLOSED · rev-3' with §9 rev-3 '§3 · gains the hands-off to TOOL-aEvidencedLens-18'. Spec-12 is 'CLOSED · rev-4' with a matching rev-4 §3 line. Spec-15 is 'CLOSED · rev-2' with a matching rev-2 §3 line. So AC4's clause 'each of the three carries a bumped rev with a §9 line naming §3' is already green for all three, and unit 15 too, not just units 1 and 12. The edge clauses can still fail: spec-1 and spec-12 hold no hands-off to 15 today, and spec-15 holds no consumes-from to 12 or 1. Only the rev-bump half is vacuous, so low. The fix is unsound as written because it asks unit 15's own §9 line to name TOOL-aEvidencedLens-15, its own id, when the edge it records points at units 12 and 1. | unsound |
| 4 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 6 AC5 | low | low | confirmed | Spec-15 is CLOSED at HEAD. git show --name-only d239695c6 (unit 15's pass) listed only README.md, RUN.md, the unit-15 ledger and spec-15. Its follow-up ad25d88c3 listed only the ledger. git log -- memory/LIVE.md last touched it at e4dd6c85b. So AC5's first clause is green before unit 18 is built and nothing this unit does can turn it red. The clause records S5's ordering effect correctly, so the consequence is a criterion that cannot fail, with no wrong result: low. | sound |
| 5 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 1, section 2 S3, section 6 AC3 | low | low | confirmed | Re-read build/2026-10-05-build-TOOL-aEvidencedLens-15-1-acceptance-ledger.md at HEAD. Lines 26-27 record all four prints: r1 aada6477 against 6380ce0a, r2 30f26c60 against 62ba7747, all distinct. Line 30 (AC1) records 'The same run against head.js from the object database: GREEN'. Line 31 (AC2) records the key mask RED 'in both arg sets' with HEAD prints 6380ce0a and 62ba7747. git log shows spec 18 was committed at e4dd6c85b (06:25) and the ledger at d239695c6/ad25d88c3 (06:37-06:38). The pinned blob b6e31e95 equals HEAD's, so spec 18 section 1's 'four missing pieces' premise and S3's 'every print, per arg set' framing are stale against the tree. The hash-object tie (S1) and the step-3 break (S2) are still absent from the ledger, so only part of the premise is stale. The effect is limited to misdirection, so low. | sound |
| 6 | coherence | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S2, section 6 AC2 | low | low | confirmed | spec-15 line 154 (AC3) and the unit-15 ledger line 32 name the step-1 break broken.js. Spec 18 S2 and AC2 call it broken1.js. The section 6 preamble rebuild rule covers only u15-check.js ('When it is absent it is rebuilt from unit 15's section 6 and S1'). Spec 15 AC3 defines the break only as 'one word of the probe's step 1 instruction changed', and the exact edit ('forward slashes' to 'backward slashes', one occurrence asserted) is recorded only in unit 15's ledger. The claim is true. Any one-word step-1 edit still yields the red AC2 asks for, so the effect is a non-identical re-run rather than a wrong verdict, so low. | sound |
| 7 | grounding | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S1, section 4 The completed observation, section 6 AC1 | medium | medium | confirmed | Reproduced in scratch. git show HEAD:tools/workflows/tier2-review.js > head.js, then sed 's/$/\r/' > headcrlf.js. rev-parse HEAD:<harness> printed 3faf86625e60..., and both `git -C <repo> hash-object headcrlf.js` and `git hash-object headcrlf.js` run from scratch printed 3faf86625e60... (equal). `git hash-object --no-filters headcrlf.js` printed 7732dff5caaf... (differs), and cmp printed 'differ: char 22, line 1'. `git config --show-origin --get core.autocrlf` printed 'file:C:/Program Files/Git/etc/gitconfig true', and check-attr shows text set and eol lf on the harness. So the S1/AC1 equality as specified does not tie bytes to the blob for line-ending differences, and the ledger would record a byte-identity proof it does not have. The divergence is limited to EOL bytes that git's own clean filter treats as the same file, and JS normalises CRLF inside template literals, so the observed prompts are unaffected. That is a contained defect, so medium rather than high. | sound |
| 8 | grounding | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 4 Evidence, second bullet | low | low | confirmed | git show HEAD:tools/workflows/tier2-review.js, lines 694-702, re-read. Lines 696-697 build inputPrint from shape, context, byDesign, priorFindings, lensNotes, specs, checklist, intensity, and conditionally probeRules and prevBlobs. There is no round field. round appears only in deriveReviewKey at line 702 ('${kind}-r${round}-...-${inputPrint}'). Spec 18 section 4 Evidence bullet 2 ('inputs to inputPrint include priorFindings and round') is therefore wrong about round. The conclusion of distinct prints still holds via checklist, specs and priorFindings, as the ledger's four distinct values show, so low. | sound |
| 9 | reuse | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S3, section 6 AC3, section 1 | low | low | confirmed | Re-read scratch u15/u15-check.js:73-91: the loop over ARGSETS prints 'prints left X · right Y' per arg set, increments red with no exit inside the loop, and exits only after the loop with process.exit(red ? 1 : 0). The unit 15 ledger (written by d239695c6, amended by ad25d88c3 per git show --name-only) already records all four prints (aada6477/6380ce0a, 30f26c60/62ba7747, pairwise distinct) and the --mask-key red in BOTH arg sets with each HEAD print. So AC3's 'driver stops after one red' clause cannot fire against the driver S3 reuses, and S3's 'the defect this closes' names a defect the seam does not have. Spec 18 was committed at e4dd6c85b before unit 15 built, which explains it but does not cure it. Consequence is a redundant re-observation and a misleading sentence, no wrong behaviour: low. | sound |
| 10 | reuse | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S2, section 6 AC2 and its preamble | low | low | confirmed | find over the scratch dir prints u13/broken.js, u15/broken.js and broken-u12.js; no broken1.js exists. Unit 15 spec line 154 (AC3) and its ledger AC3 line both name it broken.js and give the exact edit ('forward slashes (a relative answer' to 'backward slashes (a relative answer', one occurrence). Spec 18 S2, the section 4 sketch and AC2 call it broken1.js, and the section 6 preamble's rebuild rule covers only u15-check.js. Contained naming/rebuild gap: low. | sound |
| 11 | reuse | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 6 AC1 (hash-object clause) and AC5 (first clause) | low | low | confirmed | Re-ran: git show 028b5cac:/HEAD:tools/workflows/tier2-review.js into scratch, then hash-object vs rev-parse printed 54cf03a3... = 54cf03a3... and 3faf8662... = 3faf8662... (equal). The clause can only red if the save step itself transforms bytes, so it is green before the build and does not observe what id 5 asks (independence from the working copy). 'git show --name-only d239695c6 ad25d88c3 \| grep -c LIVE.md\|ledger/2026-10' printed 0: AC5's first clause reads fixed history and cannot red, and it says 'pass commit' singular where unit 15 has two pass commits. No shipped behaviour differs: low. | sound |
| 12 | blast-radius | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S5, section 4 Files touched (last bullet), section 6 AC5 | medium | medium | confirmed | README line 104 prints 'Ids no spec-audit record has ever named: TOOL-aEvidencedLens-18', so this audit is unit 18's spec audit; BUILD-METHOD.md:142 says every confirmed MEDIUM/LOW at exit is PROMOTED into a batched unit, and even a precision-ended chain still builds its promotions. gen_build_index.py:745-748 returns the first PRECEDENCE token present, so one SPECCED promoted unit keeps the build SPECCED. LIVE.md:12 and ledger/2026-10.md:9 rows carry status SPECCED and would not change in 18's pass in that case, so AC5's 'this unit's pass commit writes both' reds on a correct build and the dispatch declares two indexes never written. S5 states 'this unit is then the build's last open unit' unconditionally, the same shape that unit 15 had before 18 was promoted (e4dd6c85b). Contained to records and one criterion: medium. | sound |
| 13 | blast-radius | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S2, section 6 AC2 | low | - | refuted | duplicate of id=16. The premise does reproduce. Spec 18 lines 46 and 115 and AC2 at line 179 name `broken1.js`. Unit 15's spec AC3 at line 154 and its ledger AC3 at line 32 name `broken.js`, and `grep -rln broken1 memory/` hits only spec 18. Id 16 makes this same naming claim and adds the rebuild-rule gap, and I confirm id 16 here. | sound |
| 14 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S1, section 6 AC1, section 5 testing | high | high | confirmed | Re-probed in scratch. `git show HEAD:tools/workflows/tier2-review.js > head.js`, then `sed 's/$/\r/'` into crlf.js. `git rev-parse HEAD:tools/workflows/tier2-review.js` printed 3faf86625e60...; plain `git hash-object crlf.js` printed the same 3faf86625e60..., and so did the `--path=` form. `git hash-object --no-filters crlf.js` printed 7732dff5caaf.... `git config --show-origin --get-all core.autocrlf` printed the system gitconfig with `true`, and check-attr printed `text: set`, `eol: lf`. So S1 and AC1 (spec lines 39-41 and 170) use plain `git hash-object`, and that assertion reads equal for CRLF-mangled bytes the driver would run on. A PowerShell redirect is a plausible way to get them, since PowerShell is this node's primary shell. §5 testing (line 158) names only S2 and S3 as liveness. S1's new refusal has no staged break, against the README build-level rule that every new refusal is observed RED on a staged break. It is a check that certifies a tie it does not check, on a narrow path. | sound |
| 15 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S5, section 4 Files touched, section 6 AC5 | medium | medium | confirmed | S5 at lines 58-61 and Files touched at lines 131-133 assert that this is the build's last open unit, and AC5 at lines 194-198 requires this pass to write both indexes. README:27 says every confirmed spec-audit finding becomes a unit. README:104 lists TOOL-aEvidencedLens-18 as never yet named by a spec-audit record, so this audit is pending, and this same batch confirms findings against it. A unit 19 ordered after 18 is therefore likely. gen_build_index.py:160 sets PRECEDENCE = INPROGRESS, BLOCKED, OPEN, SPECCED, DEFERRED, and lines 745-748 return the first token any unit holds. With unit 19 at SPECCED, unit 18's close leaves the build at SPECCED. memory/LIVE.md:12 and ledger/2026-10.md:9 show the row at SPECCED now. So that pass writes neither index, and AC5 reds a correct build. `git show --name-only` confirms unit 15's pass was two commits, d239695c6 and ad25d88c3, and neither lists an index. The spec covers only the instance, not the class. The effect is contained to records. | unsound |
| 16 | failure-envelope | memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-18.md:section 2 S2, section 6 AC2, section 5 risks | low | low | confirmed | `ls` of the scratch u15 folder printed base.js, broken.js, head.js and u15-check.js, with no broken1.js. Unit 15's ledger AC3 at line 32 defines `broken.js` as head.js with `forward slashes (a relative answer` changed to `backward slashes (a relative answer`, one occurrence asserted. Spec 18 names it `broken1.js` at lines 46, 115 and 179 and never defines its edit. The §5 risks rule at lines 156-157 and the §6 preamble at lines 164-165 rebuild only `u15-check.js` when absent, although §3 Edges (line 83) also consumes unit 15's step-1 break. A lost scratch therefore leaves the AC2 step-1 re-run undefined. The effect is contained to the ledger's evidence. | sound |
