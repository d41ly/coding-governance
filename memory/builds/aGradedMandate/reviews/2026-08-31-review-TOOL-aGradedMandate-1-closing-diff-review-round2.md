**Serves:** diff-review TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-5

# aGradedMandate — the CLOSING diff review, ROUND 2

*Adversarial Tier-2 pass over the FOLD, node `a`, 2026-08-31. The base is round 1's own reviewed tip,
so this diff is the fold commit, the records that carry it, the dossier edit, and the merge that
brought `aProvenReuse` in. Six primed finder lenses over the gate leg, the driver, the shared library,
the two suites, both conf carriers and every records artifact; a skeptic prompted to REFUTE each
finding; one synthesis pass. ROUND 1's findings are NOT re-raised — this report judges the FIX. Every
surviving finding was re-derived against the tree at the line numbers it cites, and the severities in
the table are this report's adjudication, not the finders' self-grading. Binding contract:
`memory/guides/UNATTENDED-PROTOCOL.md`. Method: `memory/guides/BUILD-METHOD.md`.*

**Range:** `2aee73b884c020f12c51f4fd9211719ee4d32d01...HEAD` — round 1's reviewed tip to `34f8c5bb`,
across the fold `ed281374`, the records commit `68688431`, the dossier commit `997cea89` and the
`origin/main` merge `34f8c5bb`.

## Verdict: CLEAN WITH FIXES

Three HIGHs, four MEDIUMs, seven LOWs — fourteen distinct defects, no blocker. Round 1's blocker is
genuinely closed: the strictness regression in check 24's RETIRE arm is repaired, the exemption now
falls back to the live-phase baseline instead of waving an absent unit through, and the leg is GREEN
end to end on this tree (observed, see *What the fold got right*).

**The question this round was commissioned to answer is: did the fix do it again? Yes, twice — both
smaller than round 1's, and neither reaches the product.** The fold replaced check 24's whole-check
skip with two per-arm skips, and the two announcements now certify each other unconditionally: when
both baselines refuse, each line tells the operator the other arm ran (M1). And the fold repaired the
merge-base `base:` pin in `seed_ros` while leaving the identical pin in the one arm 20 lines below
whose entire subject is the exemption the fold REWROTE, so the rewritten predicate has no arm that can
fail (H1). Round 1's blocker was a regression introduced by a fix for a spec-audit finding; this
round's H1 is a fix applied to the instance and not the class, which is the same failure one level up.

The third HIGH is not the fold's doing but is the fold's subject: the empty-roster vacuity closed in
`pinned_units` this diff is still open in the driver's own `check_authorization`, which is the reader
that actually refuses a run (H2). H3 is the acceptance ledger, which was graded claim by claim as
commissioned: most of it reproduces exactly, and every one of the measurements it cites *once* in its
own preamble no longer does, because the merge that closes this range moved the populations underneath
them.

## Review shape

Raw 30 · confirmed 30 · refuted 0 · unverified 0 · precision 1.00. The thirty confirmed findings
deduplicate to **fourteen distinct defects** — four lenses independently found the vacuous test arm and
four found the shadowed floor constant, which is the strongest convergence signal in the set. Four
findings were corrected or downgraded during adjudication; see *Adjudications* at the bottom.

| # | Sev | Where | One line |
|---|-----|-------|----------|
| H1 | HIGH | `tools/unattended/check-unattended.test.sh:2316` | The rewritten RETIRE-arm exemption's only arm passes by SKIP; `seed_ros`'s repair was not applied here |
| H2 | HIGH | `tools/unattended/unattended.sh:1451` | The empty-roster vacuity closed in `pinned_units` is left open in `check_authorization` |
| H3 | HIGH | `…-1-acceptance-ledger.md:7` | Every measurement the ledger cites once is pre-merge: 895 assertions, 28 records, `12:11` |
| M1 | MEDIUM | `tools/unattended/check-unattended.sh:1709` | The two new skip announcements each certify the other arm ran; their guards are independent |
| M2 | MEDIUM | `tools/unattended/check-unattended.sh:1735` | The RETIRE arm harvests and exempts on any row MENTIONING an id — the class `row_ids_of` closed elsewhere in this same fold |
| M3 | MEDIUM | `tools/unattended/unattended.test.sh:4963` | `FLOOR_ASSERTIONS` bumped on an assignment shadowed 31 lines later; the shard floors moved the wrong way |
| M4 | MEDIUM | `…spec-TOOL-aGradedMandate-6.md:3` | Header says rev-2 over a log whose latest entry is rev-4, with no rev-3; the hygiene check is one-directional |
| L1 | LOW | `…spec-TOOL-aGradedMandate-2.md:122` | The two `AMENDED at rev-N` stamps are swapped; one names a rev that does not exist |
| L2 | LOW | `…-1-acceptance-ledger.md:14` | "since four criteria rest on it" — five table rows, seven criteria cite one |
| L3 | LOW | `…-1-acceptance-ledger.md:136` | AC3's `grep -c` reproduces 2, not the 1 recorded |
| L4 | LOW | `…-1-acceptance-ledger.md:135` | Unit 11's AC2 line is in neither of the two forms the ledger's header declares |
| L5 | LOW | `memory/map/features/unattended.md:151` | "Four Definition-of-Done terms" then enumerates three |
| L6 | LOW | `.unattended.conf:142` | Round 1's spliced-sentence finding is half-fixed: a blank line still severs it, in both carriers |
| L7 | LOW | `tools/unattended/check-unattended.test.sh:2329` | `miss "check 24 skipped"` names a string this fixture can no longer produce |

## BLOCKERS

None.

## HIGH

### H1 — the rewritten exemption's only arm is green by SKIP

`tools/unattended/check-unattended.test.sh:2316`

The fold repaired `seed_ros` (2254-2258): commit the fixture, then re-pin `base:` to
`git rev-parse HEAD` and commit again, with a comment stating why — "the merge-base predates this
fixture build folder entirely, so the RETIRE arm would refuse rather than grade, and every arm below
would be green because the arm found nothing." That is exactly right, and it was applied to one of the
two call sites. The arm at 2311-2322 does not call `seed_ros` and still pins
`base: $(git merge-base origin/main HEAD)`.

`reset_tree` (215-221) repoints `refs/remotes/origin/main` at `$ANCHOR0`, captured at line 164 —
before any `build tRos`, whose first occurrence is line 2249. So the merge-base is a commit with no
`memory/builds/tRos/README.md`, `pinned_units` refuses with "no build README at the pinned commit",
`rs_pwhy` is set, and check 24's ENTIRE RETIRE arm is skipped for this fixture
(`check-unattended.sh:1721`). `miss "$(run)" "check 24 FAILED"` at 2318 then passes because nothing
graded. Its liveness half at 2321 counts `| WONTDO |` rows in the fixture README, which is true whether
the arm ran or not — the could-not-fail shape round 1 already flagged elsewhere.

What makes this a HIGH rather than a LOW is what the arm covers. This is the ONLY arm exercising the
was-already-`WONTDO` exemption, the arm's own comment says it exists because
`TOOL-dUnstalledConvoy-33` silently killed that exemption once, and the fold REWROTE that exemption
this diff (`check-unattended.sh:1736-1740`, the new `if id_in … elif [ -z "$rs_why" ] …` block). A
rewritten predicate whose only test cannot fail is an assertion about nothing. The build's decision
record claims the suite's fixture defects are repaired; this one is not.

**Fix:** mirror the `seed_ros` repair — commit the fixture, then
`sed -i "s/^base: .*$/base: $(git rev-parse HEAD)/" memory/builds/tRos/RUN.md` and commit again.
Better, hoist the two-commit pin into a helper both call, so the two cannot diverge a second time.

**Left-shift gate:** add the liveness assertion the arm lacks —
`miss "$(GOV_UNATTENDED_REPORT=1 bash "$SCRIPT" 2>&1)" "check 24's RETIRE arm skipped"` — and, for the
class rather than the instance, a suite-level arm asserting that no fixture `RUN.md` written by this
file pins `base:` to a merge-base (`grep -c 'base: .*merge-base' check-unattended.test.sh` = 0 outside
the `tRun` prologue). A skip must announce itself, and here nothing can hear it.

### H2 — the empty-roster vacuity is closed in two readers and open in the third

`tools/unattended/unattended.sh:1451`

`pinned_units` gained the empty-roster refusal in this fold, `baseline_units` already carried it, and
the fold's own comment argues the case at length: `region` exits 0 with empty stdout for a well-formed
pair enclosing nothing, so an id-less units region returns SUCCESS with an empty roster and every
membership test against it answers "absent".

`check_authorization` — the reader that actually fails a run, at check 20 — has no such refusal. Line
1451 gates the comparison on the presence of the open MARKER; a well-formed but id-less region passes
that gate, `_ids_of` yields nothing, and `comm -23` over an empty left side yields nothing, so `miss`
is empty at 1461 and the check returns 0. The `elif [ -n "$UNITS_REGION_CUTOFF" ]` refusal below is
unreachable in that state, because the marker IS present, so the cutoff cannot rescue it at any date.
That branch's own message names the defect: "an empty set would satisfy the subset test vacuously."
Two shapes produce the same empty set and only one is refused.

Reachable, measured on this tree: seven tracked build READMEs carry an id-less units region today
(`aDeployScout`, `aFerriedDossier`, `aKitHardener`, `aLeanRework`, `aPortableWarden`, `aRatchetForge`,
`bThriftyBellows`), and it is the ordinary shape of a build whose folder is opened and whose BASE is
pinned before its specs are authored — the prompt-authorized mode. Check 24's RETIRE arm does not
compensate, because `pinned_units` refuses there and the arm skips.

One correction to how the finders framed it: with an id-less BASE region the authorized roster is
empty, so nothing can be *narrowed* out of it. What is lost is that the scope is not frozen at all,
while the branch one `elif` below refuses precisely that state. The inconsistency is the finding.

**Fix:** after `ub=$(… region …)`, refuse when `printf '%s\n' "$ub" | _ids_of` is empty, with the
message shape `pinned_units` now uses. Better: route this read through `pinned_units` so one predicate
owns the refusal and the checker and driver cannot disagree about what an id-less region means.

**Left-shift gate:** a driver-suite arm with a BASE README carrying a marker pair around only the
`*No spec…*` line, asserting check 20 REFUSES; plus a leg arm asserting that every function reading a
units region out of a blob carries an empty-roster refusal (grep the three readers for the refusal
string, count 3). The fold's comment already warns that counting refusal BRANCHES will not catch this
— the sets differ, not the sizes — so the gate must key on the id-emptiness test itself.

### H3 — every measurement the ledger cites once is pre-merge

`memory/builds/aGradedMandate/build/2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md:7`

The ledger states its measurements once, in the preamble, so no line repeats them. All three have
moved under it, and eight AC lines lean on the first:

- **"GREEN at 895 assertions"** (line 7). The fold `ed281374` added two counted arms to
  `unattended.test.sh` (the `DONE` / `DONE (` pair) after that measurement was taken, and the merge
  `34f8c5bb` added thirteen more static assertion sites to REGION ONE with the `RECALL_CLI` block. The
  suite has not been re-run since — RUN.md records no re-run after 12:08:32Z — so at the tip this
  ledger grades, both the count and GREEN are inferences rather than observations.
- **"all 28 tracked `RUN.md`"** (lines 34, 55, 100). 28 at the ledger's own commit `68688431`; 29 at
  HEAD, `aProvenReuse` having arrived with the merge. The census's population is one record short of
  the tree the record is committed on.
- **`CORE_FLOOR="12:11"` and "an eleven-member `DOD_CORE`"** (unit 2, AC4 and AC4b, line 62). Both
  carriers read `CORE_FLOOR="12:12"` at HEAD, `DOD_CORE` has twelve members, and both protocol copies
  say "Twelve kit-owned core items" — the merge landed `reuse-probed` as a twelfth. The cited values
  were true when written and reproduce at `git show 68688431:`; they do not reproduce at HEAD.

The ledger's own preamble is the standard it is being held to: "a number typed beside a set it does
not derive is this repo's own named defect."

**Fix:** re-run `bash tools/unattended/unattended.test.sh` on the merged tip and restate the observed
count, or say plainly that the figure was taken at `2aee73b8` and that the suite has not been re-run
since arms were added to it. Re-derive the census population and the two conf figures at HEAD, or
stamp each with the sha it was measured at.

**Left-shift gate:** the ledger's cited measurements should carry the sha they were taken at
(`measured at <sha>`), and a hygiene check should red when a records artifact cites a bare present-tense
count for a population the tree can derive without naming a commit. Cheaper interim: make the ledger's
preamble state the sha once, which turns three unfalsifiable claims into three checkable ones.

## MEDIUM

### M1 — the two new skip announcements certify each other

`tools/unattended/check-unattended.sh:1709` and `:1722`

`rs_why` (a `baseline_units` refusal) and `rs_pwhy` (a `pinned_units` refusal) are set independently,
and neither message reads the other's flag. Line 1709 always appends "(the RETIRE and supersession
arms still ran)"; line 1722 always appends "(the ADD arm still ran)". The inputs genuinely overlap:
line 1681 hands `$rb` to `baseline_units` as its FALLBACK commit and 1698 hands the same `$rb` to
`pinned_units`, so a build with no live-phase commit reads the same blob through both functions, and
a README with no well-formed non-empty units region at that commit refuses in both. Both lines then
print for one file and each is false; only the "supersession arms" half survives, that loop sitting
outside both guards.

This is a regression introduced by the fix for round 1's whole-check skip: before the fold, that state
produced one honest skip line. It is an announced skip that overstates its coverage, which is the class
this build exists to close, and it is why this round exists. Bounded: `report()` prints only under
`GOV_UNATTENDED_REPORT=1`, and it is NOT live on this tree — a full reporting run at HEAD emitted
exactly two report lines and both were check 23's.

**Fix:** decide the message from both flags at once. When both are set, emit one line naming both
refusals and stating that only the supersession arm ran; keep the two single-arm messages for the
cases where one baseline failed.

**Left-shift gate:** a leg-suite arm over a fixture whose README carries an empty units pair at both
commits, asserting under `GOV_UNATTENDED_REPORT=1` that the output does NOT contain "(the ADD arm still
ran)" together with "ADD arm skipped". No arm anywhere asserts either message today — `grep -n 'arm
skipped'` hits only the two source lines — which is why the rename in L7 also went unnoticed.

### M2 — the RETIRE arm still joins ids by mention, not by ownership

`tools/unattended/check-unattended.sh:1735`

The same fold added `row_ids_of` to the driver (`unattended.sh:1856`) with an explicit argument: "a
generated unit row leads with its link label and may mention another id in the title text… a foreign
id there would put a unit into a population it is not in." It wired it into `build-complete` and
`specs-audited`. Check 24's RETIRE arm — the one predicate that refuses a silently dropped unit, and
the one this fold rewrote — still harvests with a bare `grep -oE` over `| WONTDO |` rows (1735) and
still exempts via `id_rows` (1737, 1739), which matches the id as a whole token ANYWHERE on the line
(`lib-unattended.sh:34-36`).

Both directions are wrong. A `WONTDO` row whose title names another unit's id exempts that other unit
from ever owing a retire or supersede row; the same foreign id demands a row for a unit that was never
retired. Verified in isolation against the shipped library: with rows
`| ARCH-x-1 — the first unit `spec/one.md` | OPEN |` and
`| ARCH-x-2 — folded into ARCH-x-1 `spec/two.md` | WONTDO |`, `id_rows "$rows" ARCH-x-1` returns both
rows and the exemption fires for `ARCH-x-1`.

The fold's own census measured zero foreign ids across 80 generated regions, so this is a latent shape
rather than a live instance — but it is the shape the fold declared worth closing, left open in the
refusal path, and reachable through an ordinary free-text unit title. Note the structural obstacle:
`row_ids_of` lives in `unattended.sh`, which the checker does not source, so the checker cannot reach
it.

**Fix:** move `row_ids_of` into `lib-unattended.sh` beside `id_rows`, select the `WONTDO` population
with it, and replace the two `id_rows … | grep -q '| WONTDO |'` lookups with a match on the row whose
FIRST id is `$rsid`.

**Left-shift gate:** a leg-suite arm with a unit row whose TITLE names a sibling id, asserting the
sibling is neither exempted nor accused. Same fixture serves both directions.

### M3 — the floor bump landed on a dead constant, and the shard floors moved the wrong way

`tools/unattended/unattended.test.sh:4963`

`FLOOR_ASSERTIONS` is assigned twice: 550 at 4963 (the fold's bump, from 547) and 675 at 4994, with
nothing but comments between them. The second wins unconditionally, and only it reaches
`*) FLOOR=$FLOOR_ASSERTIONS` at 5022. The fold's +3 to the unsharded floor therefore decides nothing,
and the comment block at 4959-4962 — "Lower it in a reviewed diff or not at all" — guards a constant
no run reads. It is the same dead-plumbing class round 1 found in check 16d, one file over.

The shard pins are worse than inert. The two arms the fold added sit inside `if in_shard 2` (REGION TWO
opens at 1591), so shard 1 does not run them — yet `FLOOR_SHARD_1` was raised 205 -> 208 and
`FLOOR_SHARD_2` was left at 510. Measured statically at the fold commit, REGION ONE held 192 assertion
sites against 192 at the base: shard 1 gained nothing and its floor rose by three, cutting its margin
to about two arms against a block that argues for ~3%. It does not red today only because the later
merge added thirteen REGION ONE sites for unrelated reasons (205 at HEAD, plus 18 prologue). Nobody
re-measured: the block's own rule is that the next session to touch this suite owes it three numbers,
and this diff gives it none.

**Fix:** delete the shadowed assignment at 4963 (keeping its rationale comment above the surviving
constant), re-measure all three counts on the merged tip, and re-derive the floors at the block's
stated discount, recording the triple in the comment as that block requires.

**Left-shift gate:** an arm asserting the file declares each `FLOOR_*` constant exactly once
(`grep -c '^FLOOR_ASSERTIONS='` = 1). That is three lines and it makes a shadowed pin impossible, which
is the general form of "a guard that can be raised without raising anything."

### M4 — unit 6's status header is BEHIND its revision log, and the gate only looks the other way

`memory/builds/aGradedMandate/spec/2026-08-31-spec-TOOL-aGradedMandate-6.md:3`

The header reads `CLOSED · rev-2`; section 9 carries rev-1, rev-2 and a rev-4 entry added by this fold,
with no rev-3 at all. `tools/memory-tree/check-memory-hygiene.sh:919` fires only on `!seen || hrev + 0
> mx` — a header AHEAD of its log — so header-behind-log is green by construction. All eleven specs
were checked; this is the only one.

The consequence is not cosmetic. `memory/builds/aGradedMandate/README.md:92` renders `rev-2` for unit 6
from that header, while the ledger's unit-6 block cites "amended rev-4" for AC3 and AC3b — the two
criteria this build deliberately records as UNEXERCISED and UNOBSERVED, where the amendment trail is
doing all the work. Spec 9's own rev-3 entry records the identical drift being found and fixed in an
earlier round, so the class has now recurred with no gate closing it.

**Fix:** renumber the added entry to rev-3 and stamp the header rev-3 (or author the missing rev-3 and
stamp rev-4), then re-render with `tools/memory-tree/gen_build_index.py --write`.

**Left-shift gate:** make the hygiene rev check SYMMETRIC — red when the header rev is BELOW the logged
maximum as well as above it. One `||` clause in an awk predicate that already computes both values.

## LOW

### L1 — the two `AMENDED at rev-N` stamps are swapped

`memory/builds/aGradedMandate/spec/2026-08-31-spec-TOOL-aGradedMandate-2.md:122` and
`…-spec-TOOL-aGradedMandate-9.md:102`

Spec 2's AC4a reads "AMENDED at rev-4" on a spec whose header is rev-3 and whose amending log entry is
rev-3; rev-4 does not exist in that file at all. Spec 9's AC5 reads "AMENDED at rev-3" on a spec whose
header is rev-4 and whose amending entry is rev-4 — its actual rev-3 entry is an unrelated header/log
fold. The ledger has both right (`amended rev-3` for unit 2, `amended rev-4` for unit 9), so the
ledger and the criteria disagree, and the "see the section 9 line" pointer resolves to the wrong entry
in one file and to nothing in the other. The amendment paragraph is the same copied text in four specs
with the rev not adjusted per file.

**Fix:** spec 2 line 122 to rev-3, spec 9 line 102 to rev-4.

**Left-shift gate:** extend the hygiene rev walk to assert every in-body `AMENDED at rev-N` names a
revision the same file's section 9 logs. It reads both halves already for M4's check.

### L2 — "since four criteria rest on it" derives nothing

`…-1-acceptance-ledger.md:14`

The table beneath the heading has five rows, and the criteria whose evidence is a staged break are
seven: unit 2 AC4, unit 5 AC4 and AC8, unit 6 AC1, unit 7 AC1, unit 9 AC1 and AC2. Four IS derivable as
the number of distinct CHECKS the breaks fired (16, 2, 3, 24), but the heading's noun is "criteria",
and the preamble twelve lines above forbids exactly this — "the lines below are the population, and a
number typed beside a set it does not derive is this repo's own named defect."

**Fix:** drop the count — "What a staged break bought".

**Left-shift gate:** none proposed; a prose-count gate over records would red on legitimate historical
counts. This one belongs in the §10 checklist the build already keeps, where the same class was
recorded for the dossier (L5).

### L3 — AC3's cited count reproduces as 2, not 1

`…-1-acceptance-ledger.md:136`

`grep -c 'closing-loop-census' …spec-TOOL-aGradedMandate-1.md` returns 2 at HEAD, and returned 2 at
the ledger's own commit: the second hit is the generated spec-records row at spec-1 line 11, committed
by the same records commit that carries the ledger. The AC's substance holds (the spec names the census
record) and a re-runner gets 2 >= 1, which strengthens rather than weakens it. The finders' "measured 0
before the edit" half is TRUE — the token entered spec-1 at `788908bc`.

**Fix:** restate as 2, or scope the probe to the acceptance section so the number is stable against the
records-table render.

**Left-shift gate:** prefer a `grep -c` scoped to a section over one scoped to a file whenever the file
carries a GENERATED region — a §10 checklist entry, since no predicate can tell which was intended.

### L4 — unit 11's AC2 line is in neither declared form

`…-1-acceptance-ledger.md:135`

The line carries no backticked observation token and no `amended rev-N`, so check 23's flattening awk
grades it `bad` — the state that check fails on with "an acceptance-ledger line is in neither legal
form". It escapes only because that check's selector drops any spec whose header is not Tier-2, and
unit 11 is Tier-1. The ledger's opening claim — "in one of the ledger's two forms and no third" — is
therefore false for one line, and the gate cited as the guarantee cannot reach it.

**Fix:** give the line a backticked token, e.g. the census record's path.

**Left-shift gate:** widen check 23's selector to grade Tier-1 units' ledger lines too, or state in the
check's own header that Tier-1 lines are ungraded. Right now the check reads as covering the ledger
and covers part of it.

### L5 — "Four Definition-of-Done terms" enumerates three

`memory/map/features/unattended.md:151`

The paragraph names `closing-review-recorded`'s second term, `specs-audited`, and `build-complete`'s
sixth term. The fourth was `TOOL-aGradedMandate-3`'s gates-green escalation, retired WONTDO before any
code, so the sentence credits the kit with a term it does not have. `DOD_CORE` was checked directly:
unit 7's promotion clause is graded by the leg, not by a DoD term, so there is no unnamed fourth. It
lands in the commit whose subject is "the dossier stops carrying three claims this build falsified",
and which deliberately removed two other prose counts on this exact argument.

**Fix:** drop the numeral. The three sentences that follow are the population.

**Left-shift gate:** same §10 entry as L2.

### L6 — round 1's spliced sentence is half-fixed, in both carriers

`.unattended.conf:142` and `tools/unattended/.unattended.conf.example:158`

The declaration was moved out from under `SPEC_THIN_CUTOFF`, which was the half the round-1 finding was
for, but the sentence is still cut — now by a blank line, which reads as a comment-block boundary.
`.unattended.conf` line 141 ends "…re-opens the vacuity for every BASE in", 142 is empty, 143 resumes
"# between; moving it earlier refuses runs…". The example has the identical break at a different split
point (157/158/159). Parser-harmless — check 22 joins on `^[A-Z_]+=` — but the example is the file
every adopter copies.

**Fix:** delete the blank line inside the comment block in both files, leaving the separator above the
block rather than inside it.

**Left-shift gate:** the example-conf parity arm already compares the two carriers; extend it to assert
no blank line falls between a key's comment block and the key, which is a two-line awk over a file the
suite already reads.

### L7 — the renamed skip message left its assertion behind

`tools/unattended/check-unattended.test.sh:2329`

`miss "$out" "check 24 skipped"` is paired with a `hit` at 2327 asserting the empty-baseline reason IS
visible under `GOV_UNATTENDED_REPORT=1`; the `miss` is meant to assert the same message stays OFF the
default channel. The fold renamed that message to "check 24's ADD arm skipped", so the string this arm
names cannot appear in this scenario — `build()` always writes a well-formed units pair, so the only
surviving "check 24 skipped" emitter (the malformed-region branch at 1685) is unreachable here. The
arm is inert: if a future change printed skips unconditionally, it would still pass.

**Fix:** assert both new spellings, or `miss "$out" "check 24's"`.

**Left-shift gate:** this is the general case of "the rename left its assertion behind" — a suite arm
asserting that every literal the suite `miss`es on the report channel appears at least once in
`check-unattended.sh`. A `miss` over a string the leg cannot print is a test that cannot fail, and this
suite now has at least one.

## What the fold got right

Credited, because a review that only lists defects misrepresents the diff.

- **Round 1's blocker is closed, and closed on the mechanism rather than the symptom.** The RETIRE arm
  no longer exempts a unit merely for being absent from the pinned roster; it falls back to the
  live-phase baseline, and the comment states the population and the reasoning. The staged break the
  ledger describes — units 10 and 11 flipped `WONTDO`, unit 3's retire row deleted — is the scenario
  round 1 used to describe the regression, and it now produces three refusals.
- **The leg is GREEN at HEAD, observed here.** `GOV_UNATTENDED_REPORT=1 bash
  tools/unattended/check-unattended.sh` exits 0, and the only report lines are check 23's two, which
  reproduces the ledger's claim about the report channel exactly and independently confirms that check
  24's skip branches are unreached on this tree.
- **Round 1's dead plumbing is properly deleted, not worked around.** The `grep -c . >/dev/null` in
  check 16d is gone and the duplicate `_no_tmpl` collapsed onto the existing `$tmpl` (verified: line
  1327 defines it as the SKILL template, so the collapse is behaviour-preserving).
- **`pinned_units`' new refusal carries the argument for why counting branches would not have caught
  it** — "both have seven, and the sets differ rather than the sizes" — which is the kind of comment
  that stops a future gate being written to the wrong shape.
- **The ledger's checkable claims mostly reproduce.** Verified at HEAD: `park_kinds_unowed` = 2,
  `grep -c '46 records'` = 0, `pieces-complete` = 2, the protocol pair is byte-identical, seven id-less
  build READMEs, the two non-terminal records are `aGradedMandate` and `aThawedCorpus`, and the census's
  refusal split holds for the population it was taken over. The AMENDED form is used honestly: four
  criteria say what was observed instead of claiming what was not.

## Adjudications — where this report departs from the finders

- **`FLOOR_SHARD_1` "may red the shard-1 leg" — not supported, and downgraded into M3.** Measured
  statically: REGION ONE plus prologue is 223 assertion sites at HEAD against a floor of 208. At the
  fold commit it was 210 against 208, which is the real complaint (headroom, not a red), and the margin
  was restored by unrelated merged arms rather than by anything the fold did.
- **`check_authorization` "can narrow or rename its entire authorized roster" — overstated, corrected
  in H2.** With an id-less BASE region there is no roster to narrow; the defect is that the scope is
  not frozen at all while the neighbouring branch refuses that same state.
- **"The checker no longer emits `check 24 skipped`" — corrected in L7.** The string survives on the
  malformed-region branch; it is unreachable in the arm's own scenario, which is enough for the arm to
  be inert but not enough for the string to be dead.
- **"AC3 measured 0 before the edit is false" — refuted.** The token entered spec-1 at `788908bc`; only
  the current value is wrong.
- **Six near-duplicate records findings collapsed.** Three lenses each reported the conf splice, the
  swapped AMENDED stamps and the shadowed floor; they are one defect apiece.

## What was NOT verified

- **Neither suite was run.** `tools/unattended/unattended.test.sh` and
  `tools/unattended/check-unattended.test.sh` were not executed for this review; H1, M1, M2 and L7 are
  read from the source and from the checker's behaviour, not from a suite run. H1's mechanism was
  traced through `reset_tree`, `$ANCHOR0` and `pinned_units` rather than reproduced end to end. The
  suite skip is the build's own recorded owner instruction, and this review inherits its blind spot
  rather than closing it.
- **The worktree mutated mid-review.** A concurrent session rewrote
  `memory/guides/UNATTENDED-PROTOCOL.md` and `.claude/skills/unattended/SKILL.md` under this pass —
  transient states showing kit 1.14 and a rewritten concurrency section were observed and then vanished.
  Every measurement in this report was re-taken against `git show <sha>:` or re-confirmed after that
  window. If a future reader cannot reproduce a figure here, check for a concurrent run before assuming
  drift.
- **The bar as a whole was not run** — only `check-unattended.sh`. `bash tools/run-gates/run-gates.sh`
  is the push boundary's job and this review does not stand in for it.
