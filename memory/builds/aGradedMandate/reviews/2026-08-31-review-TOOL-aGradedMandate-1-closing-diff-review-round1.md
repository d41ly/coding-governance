**Serves:** diff-review TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11

# aGradedMandate — the CLOSING diff review, ROUND 1

*Adversarial Tier-2 pass over what SHIPPED, node `a`, 2026-08-31. Five primed finder lenses over the
driver, the gate leg, the shared library, both protocol copies, the Skill pair, both conf carriers and
the driver suite; a skeptic prompted to REFUTE each finding; one synthesis pass. Every surviving
finding below was re-derived against this worktree at the line numbers it cites before it was written
down, and the severities in the table are this report's adjudication rather than the finders'
self-grading. The three prior records under `reviews/` are SPEC audits; their findings are folded and
none is re-raised here. Binding contract: `memory/guides/UNATTENDED-PROTOCOL.md`. Method:
`memory/guides/BUILD-METHOD.md`. Bug-class checklist for this range: the twelve classes
`tools/memory-tree/gotchas.py --for-diff` selected, named in §Lens brief below.*

**Range:** `54309e9c565d30b695ba353adfb8503a3a98dfee...HEAD` — the pinned BASE of this run to the
working tip `2aee73b8`, 30 files, +3198/-158, across three product commits (`ccb5492c`, `67aa9e0a`,
`2aee73b8`).

## Verdict: BLOCKED

One BLOCKER, two HIGHs, three MEDIUMs, nine LOWs — fifteen distinct defects.

The blocker is a STRICTNESS REGRESSION in the one arm this build exists to strengthen. Unit 6 rekeyed
check 24's RETIRE arm to the pinned BASE and, in doing so, added a second exemption that spec 6 S5
forbade in as many words. Before this diff, a unit absent from the baseline roster and WONTDO now
FAILED the arm. After it, that unit is waved through in silence. The population it exempts is not
exotic: it is every unit added between BASE and BUILDING, which on this very build is
`TOOL-aGradedMandate-10` and `-11`. Either could be flipped to WONTDO today, with no rescope row, and
nothing would report it. The build's own stated improvement is "Dropping declared scope reaches the
owner's one turn instead of the history class"; for that population the unit made the opposite true.

The parked entry of 2026-08-31T10:09:23Z is a genuinely good record and this review credits it. It
states, on an explicit owner instruction, that the gate-leg self-test suite was not run, names the two
arms that therefore remain unobserved, and lists what WAS observed directly instead. Two things it does
not say, and both are findings below. The suite is not merely unrun — three of its check-24 arms now
assert a message string this diff deleted, so it is RED and will fail on a message mismatch rather than
on a real defect whenever someone next runs it (H2). And "the driver suite IS green at 895 assertions,
so the driver-side units are covered" is a suite-green claim rather than a coverage one: spec 4's AC4
has no assertion that can fail, and reverting its implementation leaves the suite green (L6).

Nothing here questions the four new refusal items themselves. `closing-review-recorded`'s terminal-token
terms, `specs-audited`, `build-complete`'s TERM 6 and the parked-act split are sound in shape and read
evidence that was previously written and never opened, which is what the build set out to do. Every
finding is in an edge: one strictness regression, one missing refusal, one broken test suite, one
unimplemented acceptance criterion, one term carrying three unannounced skips, one stale contract row,
and a tail of prose, duplication and coverage defects that would not on their own delay a landing.

## Review shape

- Raw findings: **25** · confirmed **18** · refuted **7** · unverified **0** · precision **0.72**.
- Confirmed 18 collapse to **14** distinct defects after merging: four reports of the same conf-comment
  splice (L9) and two of the same RETIRE-arm exemption (B1). One further defect (**H2**) was found while
  verifying B1's coverage claim and is confirmed by direct observation rather than by the skeptic round.
- Precision 0.72 is above the ~0.5 retune floor, so the lens set and priming are left as they are.
- Every census figure quoted below was re-measured against this worktree while writing the report
  rather than carried over from a finder: 116 tracked `**Serves:**` lines mentioning `spec-audit` and
  0 of them unanchored; 80 generated unit regions and 0 carrying a foreign id; 7 build READMEs whose
  well-formed units region names no unit id; 3 undated spec files.

## Lens brief — the bug classes this range selected

`fixture-passes-by-finding-nothing` · `staged-break-substitutes-a-synthetic-value` ·
`two-answers-to-one-question` · `amendment-leaves-its-other-half-standing` ·
`assertion-between-two-derived-values` · `containment-tested-one-way` ·
`fallback-fabricates-the-passing-value` · `id-matched-as-a-substring` ·
`second-implementation-is-not-a-second-opinion` · `status-set-in-a-subshell` ·
`two-guards-one-question-two-answers` · `two-readers-of-one-config-one-re-derived`.

Seven of the fifteen findings are instances of a class on that list, which is the checklist earning its
keep: B1 and H1 are `fixture-passes-by-finding-nothing`, M3 and L4 are
`amendment-leaves-its-other-half-standing`, L2 is `id-matched-as-a-substring` one field to the left, L6
is `containment-tested-one-way`, and L8 is `two-answers-to-one-question`.

## Findings

| # | Severity | Location | Defect |
|---|---|---|---|
| B1 | BLOCKER | `tools/unattended/check-unattended.sh:1720` | The RETIRE arm's new `id_in "$rs_pinned"` exemption silently waves through every unit added after BASE — a strictness regression against spec 6 S5 |
| H1 | HIGH | `tools/unattended/lib-unattended.sh:200` | `pinned_units` omits the empty-roster refusal its sibling carries, so an id-less BASE region makes the RETIRE arm vacuous and silent |
| H2 | HIGH | `tools/unattended/check-unattended.test.sh:2291` | The check-24 arms assert a message this diff deleted, so the suite is RED rather than merely unrun — which the parked entry does not say |
| M1 | MEDIUM | `tools/unattended/check-unattended.sh:1684` | Spec 6 S3 / AC3b unimplemented: an ADD-baseline failure still skips ALL of check 24, on a unit marked CLOSED |
| M2 | MEDIUM | `tools/unattended/unattended.sh:3196` | `build-complete` TERM 6 has three unannounced skips: undated spec filenames, and a swallowed `load_spec_facts` refusal |
| M3 | MEDIUM | `tools/unattended/PROTOCOL.template.md:332` | The `closing-review-recorded` contract row still says it never reads what the review concluded; `--close` now does |
| L1 | LOW | `tools/unattended/unattended.sh:3115` | "FIVE terms, ALL required" is stale in three carriers after TERM 6 landed |
| L2 | LOW | `tools/unattended/unattended.sh:3376` | `specs-audited` matches `spec-audit` anywhere on the binding line rather than in the kind field |
| L3 | LOW | `tools/unattended/unattended.sh:3356` | Two new roster readers use the unscoped `_ids_of` where the same function uses slug-scoped `unit_ids_of` forty lines earlier |
| L4 | LOW | `tools/unattended/unattended.sh:409` | The parked-kind taxonomy comment still says membership is declared "NOWHERE ELSE"; `PARK_ACTS_OWED` falsified that in this diff |
| L5 | LOW | `tools/unattended/unattended.sh:3202` | Spec 4 AC2 requires the THIN grandfather be ANNOUNCED; the implementation is a bare `continue` |
| L6 | LOW | `tools/unattended/unattended.test.sh:1628` | Spec 4 AC4 has no assertion that can fail — reverting the `verb_plan` edit leaves the suite green |
| L7 | LOW | `tools/unattended/check-unattended.sh:1492` | `_no_core`'s first subshell computes a count, discards it to `/dev/null`, and has its status dropped — dead plumbing |
| L8 | LOW | `tools/unattended/check-unattended.sh:1476` | `_no_tmpl` is a second name for the path `tmpl` already holds in the same scope |
| L9 | LOW | `.unattended.conf:135` | The `SPEC_THIN_CUTOFF` block was spliced into the middle of `UNITS_REGION_CUTOFF`'s comment sentence, in both conf carriers |

---

### B1 — BLOCKER · `tools/unattended/check-unattended.sh:1720`

**The defect.** Rekeying the RETIRE arm to the pinned BASE added a SECOND exemption that spec 6 S5
forbade in as many words ("the arm's exemption logic is correct and only its baseline moves"):

```sh
for rsid in $(printf '%s\n' "$rs_now" | grep -E '\| WONTDO \|' | grep -oE '...' | sort -u); do
  id_rows "$rs_pinned" "$rsid" | grep -q '| WONTDO |' && continue
  id_in "$rs_pinned" "$rsid" || continue          # <-- new, undocumented
  printf '%s\n' "$rs_rows" | grep -qE "item (retire|supersede) $rsid( |\$)" && continue
  fail 24 "..."
done
```

Pre-change (`ccb5492c^`) the loop's ONLY exemption was the `| WONTDO |` test against `rs_was`, so a
unit ABSENT from the baseline roster and WONTDO now fell through to the row requirement and FAILED. The
new line exempts it. This is a strictness regression, not a narrowing that was already there.

**Impact.** A unit that enters the roster AFTER the pinned BASE and is later flipped to WONTDO owes no
rescope row anywhere, and no sibling arm covers it:

- the ADD arm (`:1706`) exempts it, because `id_in "$rs_was"` is true — `rs_was` is `baseline_units`,
  the roster at the first BUILDING/RUNNING/VERIFYING/LANDING/LANDED commit, and a unit created during
  SPECCING is present there;
- `check_authorization` (`unattended.sh:1457`) is a `comm -23` SUBSET test that refuses only id
  REMOVALS, and a unit flipped to WONTDO stays in the region, so it is never a removal.

Net: **added after BASE, retired during BUILDING → nothing on the record, nothing reported.** That is
the exact silent-scope-drop harm units 5 and 6 exist to close, and the pre-diff code caught it.

Verified live on this tree: `RUN.md` pins base `54309e9c`, whose README units region names
`TOOL-aGradedMandate-1..9` only. `id_in "$rs_pinned"` is TRUE for `TOOL-aGradedMandate-3` but FALSE for
`-10` and `-11`. Either promotion could be flipped to WONTDO today, with no `--rescope retire` row, and
this arm stays silent. The FOLDING-promotion pattern this kit uses routinely is exactly that shape.

The exemption is also undocumented, against the charter's rule that a gate's header states what it
does NOT check: the arm's new header (`:1688-1698`) justifies only the baseline move and its ADD/RETIRE
asymmetry, and says nothing about absence.

**Fix.** Do not skip on absence. Grade a WONTDO unit against the pinned roster when it is there and
against `rs_was` when it is not — replace the new line with a fallback to the existing `rs_was` WONTDO
test so an added-then-retired unit still owes its row. A run that legitimately performs both acts
writes an `add` and a `retire`, and the arm already accepts the latter. If the exemption is kept
deliberately, it must be stated in the arm header AND in spec 6, naming the residual hole and which arm
covers it — because none does.

**Left-shift gate.** A fixture in `check-unattended.test.sh` for the ADDED-THEN-RETIRED unit: a unit
absent from the pinned BASE region, present and `| WONTDO |` in the executing roster, with NO rescope
row, asserted to `fail 24`. Pair it with the liveness half the existing already-WONTDO arm already
models at `:2315-2318` — assert the fixture's id is genuinely ABSENT from the pinned roster, or the
test is green because the arm found nothing.

---

### H1 — HIGH · `tools/unattended/lib-unattended.sh:200`

**The defect.** `pinned_units` ends at `printf '%s\n' "$_pu_was"` with no empty-roster refusal. Its
sibling `baseline_units` ends (`:250-253`) with one, and states why: "An empty baseline is not a
comparison and is not vacuously true either". Spec 6 S1 required `pinned_units` to carry "the same
cutoff handling and the same refusal shapes".

Measured, because the obvious summary of this is wrong and worth saying so: each function has exactly
**seven** `return 1` branches. The counts MATCH; the sets do not. `pinned_units` adds two refusals its
sibling does not need — the commit must be sha-shaped, and it must resolve, both because this one is
GIVEN its commit while `baseline_units` derives its own — and drops the one that matters here. Any
gate built on comparing the two counts would read 7 against 7 and pass, which is why the left-shift
below is behavioural rather than numeric.

`region()` exits 0 with empty stdout for a well-formed marker pair enclosing nothing — the
`build-complete` header in the driver says so explicitly — so a BASE README whose units region is
well-formed but names no unit returns SUCCESS with an empty roster.

**Impact.** With `rs_pinned=""`, B1's `id_in "$rs_pinned" "$rsid" || continue` skips EVERY WONTDO unit,
and the only skip report is gated on `[ -n "$rs_pwhy" ]`, which an empty SUCCESS never sets. The arm
reports green having graded nothing, with no skip line, because the read succeeded. Textbook
`fixture-passes-by-finding-nothing`, in the one arm this diff rewrote.

Reachable in the kit's SANCTIONED authorization shape, not a contrivance: an owner commits the build
README carrying the `<!-- gen:build-units -->` pair before any spec exists, the run authors the specs,
retires one, and nothing on the record says so. The arm's own header names that window ("that window
is exactly where a prompt-authorized run does its speccing"). Seven tracked build READMEs carry a
well-formed pair enclosing zero unit ids today (`aDeployScout`, `aFerriedDossier`, `aKitHardener`,
`aLeanRework`, `aPortableWarden`, `aRatchetForge`, `bThriftyBellows`). `baseline_units` is unaffected in
that shape — its BUILDING-commit README does carry rows — so M1's whole-check skip does not pre-empt it.

**Fix.** Mirror the sibling. Before the final `printf`, derive
`_pu_ids=$(printf '%s\n' "$_pu_was" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u)` and, when
empty, `echo "the pinned roster names no unit, so every retirement would read as scope that was never
authorized and the comparison would excuse rather than check"; return 1`. The caller already turns a
non-zero return into the reported `check 24's RETIRE arm skipped` line, so no call-site change is
needed.

**Left-shift gate.** One fixture, applied TWICE. Build a README whose `gen:build-units` pair is
well-formed and encloses no unit id, then assert that BOTH `pinned_units` and `baseline_units` refuse
it, and that check 24 prints the corresponding arm-skip line in each case. Driving the two functions
with the identical input is what closes the CLASS — the pair is a
`second-implementation-is-not-a-second-opinion` hazard, and the only assertion that discriminates is a
behavioural one. Explicitly NOT a count parity: as measured above, both functions already have seven
refusal branches, so a numeric assertion between two derived values would report agreement while the
defect stands. That trap is on this range's own bug-class list as
`assertion-between-two-derived-values`, and it caught a draft of this very paragraph.

---

### H2 — HIGH · `tools/unattended/check-unattended.test.sh:2291`

**The defect.** `tools/unattended/check-unattended.test.sh` does not appear in this diff at all —
`git diff --stat 54309e9c...HEAD -- tools/unattended/check-unattended.test.sh` is empty — while
`check-unattended.sh` gained 109 lines including a rewritten check-24 RETIRE arm, a rekeyed baseline
and the new check 16d. Line 2291 still reads:

```
hit "$(run)" "a unit went WONTDO after this run entered BUILDING and no rescope row retires or supersedes it, so a unit was dropped with nothing on the record saying so:"
```

`grep -c` for that sentence in `tools/unattended/check-unattended.sh` returns **0** — the arm now emits
"a unit is WONTDO now and was not at the BASE this run pinned…". `hit()` at line 57 is
`grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }`, so the assertion cannot pass. The
sibling arms at `:2295` and `:2300-2318` are in the same position.

**Impact — and what the parked entry already covers.** The run recorded a parked `decision` at
2026-08-31T10:09:23Z stating that this suite was not run on an explicit owner instruction, naming the
two arms that therefore remain unobserved (check 24's rekeyed RETIRE arm and check 2's non-WONTDO
promotion filter) and listing what was observed directly instead. That is an announced skip on an owner
instruction and it is surfaced-class, so it reaches the owner's turn. None of that is a finding.

The finding is the delta between "was NOT run" and "is now RED". A reader of that entry believes the
coverage is merely unexercised and that running the suite later is a formality that will confirm what
the arms already do. It is not: the next person to run it gets three failures that are message
mismatches, not defects, and the real defect — B1, in the very arm the entry names as unobserved — is
buried under them. An unrun suite and a broken suite are different states and only one of them is on
the record.

Two second-order consequences. `tools/unattended/run-unattended-gates.sh` states in its own header that
"the DoD for any work touching `tools/unattended/` is a GREEN verdict from `--selftests` pasted into
the landing report"; that verdict is now unobtainable without a test edit, so the compensating check
for the whole off-bar self-test exemption is inoperative until someone repairs the suite. And the
entry's closing claim — "the driver suite IS green at 895 assertions, so the driver-side units are
covered" — is a suite-green claim rather than a coverage one, which L6 shows by counter-example.

Two caveats, stated because they bound the severity. This is not a hidden failure: the skip is
recorded, the owner instructed it, and the suite is off the merge bar in this repo and absent from
`kit.toml`, so no adopter receives it. And this reviewer's own attempt to run the suite end to end for
a verdict exceeded a ten-minute budget and is recorded as unfinished in §What this review did NOT check
— the RED conclusion is derived from the source, conclusively but not observed.

**Fix.** Update the three check-24 arms at `check-unattended.test.sh:2287-2318` to the new messages and
re-pin `seed_ros`'s `base:`, which is set to `git merge-base origin/main HEAD` — a commit predating the
fixture build folder, so `pinned_units` REFUSES and the rekeyed arm now skips rather than grades even
once the strings match. Then add the two fixtures B1 and H1 name, and paste a `--selftests` verdict.

**Left-shift gate.** The compensating check for the off-bar self-tests is "a person invokes this
script", and the record shows a person deliberately did not. The gate that closes the class is the one
unit 3 was retired for: `--close` refuses when the run's own diff touches a kit directory and no
`selftests` check row for that kit is recorded in the run-state file. That is DRIVER-side and so is
landable, unlike the leg-side ratchet that retired unit 3. The cheap interim needs no new mechanism at
all — a git check that reds when a checker under `tools/unattended/` moved in a commit range where the
`*.test.sh` naming it did not. That predicate reds this range today, which is the only proof it works.

---

### M1 — MEDIUM · `tools/unattended/check-unattended.sh:1684`

**The defect.** Spec 6 S3 states verbatim: "Today a `baseline_units` failure skips all three loops at
once, including the supersession-successor loop, and removing that whole-check skip is what S3 is for."
AC3b requires the RETIRE arm to still evaluate when the ADD baseline is unreadable and the pinned BASE
resolves. The diff added the MIRROR split (`rs_pwhy`, `:1716`) and left the ADD-side whole-check skip
standing:

```sh
if [ -n "$rs_why" ]; then
  report "check 24 skipped for $f — $rs_why"
elif ! rs_now=$(region ...); then
```

`rs_now` is not even computed on that branch, so the RETIRE arm and the supersession-successor arm both
go down with the ADD arm. Two of the three declared distinguishable skips exist; the unit is CLOSED.

**Impact.** A run whose BUILDING-commit roster is unreadable — a stale index rendering an empty region,
or a baseline README predating the units region — has its retirements ungraded even though the pinned
BASE could answer them, and the message reads "check 24 skipped" rather than naming which question
could not be asked. The record integrity matters more than the runtime harm here: unit 6 is CLOSED
against an acceptance criterion that was never built, in the build that added `specs-audited` and
`build-complete` TERM 6 precisely to make that shape visible. Neither new item can see it, because both
grade the SPEC's completeness and neither grades whether the code met it.

**Fix.** Hoist the `rs_now` read above the `rs_why` branch, replace the whole-check skip with
`report "check 24's ADD arm skipped for $f — $rs_why (the RETIRE and supersession arms still ran)"`,
and guard only the ADD loop on `[ -z "$rs_why" ]`, mirroring the `rs_pwhy` shape already sitting fifteen
lines below.

**Left-shift gate.** A fixture whose `baseline_units` read fails while the pinned BASE resolves,
asserting all three of: the ADD-arm skip line is printed, the RETIRE arm still FAILS on an unrecorded
retirement, and the supersession arm still fires. Assert the three skip messages are DISTINCT strings,
so a future collapse back into one shows up as a failing test rather than as quieter output.

---

### M2 — MEDIUM · `tools/unattended/unattended.sh:3196`

**The defect.** `build-complete` TERM 6 contains three unannounced skips inside a refusal term:

```sh
load_spec_facts $(GIT ls-files -- "$M/builds/$slug/spec/*.md" 2>/dev/null) >/dev/null 2>&1 || true
for _bcid in $(printf '%s\n' "$_bcrows" | grep -E '\| CLOSED \|' | _ids_of); do
  _bcsp="${SPEC_PATH[$_bcid]:-}"
  [ -n "$_bcsp" ] && [ -r "$_bcsp" ] || continue
  _bcdate=$(basename "$_bcsp" | grep -oE '^[0-9]{4}-[0-9]{2}-[0-9]{2}')
  [ -n "$_bcdate" ] || continue
```

1. `|| true` on line 3196 discards `load_spec_facts`'s deliberate producer refusal ("REFUSING to render
   a plan table from a failed producer: it would look complete and name nothing", `:1781-1785`) AND its
   stderr. The `SPEC_PATH` map is filled BEFORE that status test, so a mid-set awk failure leaves the
   map PARTIAL, every unresolved id hits the `continue` on the next line, and the term reports met. The
   sibling call at `:1925` at least lets the refusal print.
2. `[ -n "$_bcdate" ] || continue` turns the term permanently OFF for any spec whose filename lacks a
   date prefix, with no `report` and no `DOD_OUT`.

**Impact.** Nothing in this kit requires a dated spec filename: `spec_ids` globs `"$dir/spec/*.md"`, and
the driver's own suite fixture is `memory/builds/tRun/spec/one.md`. The dating rule lives in the
memory-tree kit's hygiene check 5, which this kit copy-installs WITHOUT — its own comments say so at
`:1848-1852` — so an adopter's undated spec is ungated AND silently ungraded on the one predicate that
asserts what "done" meant. Three undated spec files exist in this repo today.

The suite corroborates the reachability from the other side: the AC1 arm at `unattended.test.sh:4840`
opens by RENAMING the fixture — `mutate ... 's#spec/one.md#spec/2026-08-01-spec-thin.md#'` — because the
undated original could not reach the term. The workaround was written; the gap it works around was not
recorded.

The term's own absent-cutoff case (`:3193-3196`) is deliberately ANNOUNCED, so the announcement
standard here is this term's own, not one imported from the charter.

**Fix.** Make both paths loud. Drop `|| true` and set `DOD_OUT` + `return 1` when `load_spec_facts`
fails. Replace the silent date `continue` with either a named refusal or a git-derived fallback
(`_bcdate=$(GIT log -1 --format=%cs -- "$_bcsp")`), collecting undated specs into a second message so
the operator is told which units the term could not grade.

**Left-shift gate.** A driver self-test arm with an UNDATED spec filename under a build whose
`SPEC_THIN_CUTOFF` is set, asserting the close names it rather than passing silently. Generalise it
into the class with a grep leg over `unattended.sh`: a `continue` or `|| true` inside a `dod_met` case
arm must be preceded by a `DOD_OUT=` or `report` on one of the three lines above it. That predicate
should be run over the real tree before wiring, and its near-misses printed — the charter's rule, and
the reason this term's three instances are worth gating rather than patching.

---

### M3 — MEDIUM · `tools/unattended/PROTOCOL.template.md:332`

**The defect.** Unit 1 added two terms to `closing-review-recorded` in the driver and left the binding
contract's DoD row describing only the original record-existence term. The row still ends "It measures
that a review of what shipped exists and is bound to THIS run, **never what the review concluded**",
while `--close` now additionally requires `review_last_reason` to return a round whose subject is the
build slug, requires that round to carry `CONVERGED`/`NON-CONVERGENT`/`CEILING`, and refuses a
`CONVERGED` round naming non-zero blockers (`unattended.sh:3315-3333`). It reads what the loop
concluded. `memory/guides/UNATTENDED-PROTOCOL.md:332` is byte-identically stale because check 10
compares the two copies.

**Impact.** An unattended run reads the Skill and this contract, not the driver. Neither carrier states
that `--close` BLOCKS without a terminal round: the Skill's "Record each review round" section tells a
run to call `--review <slug> --subject <slug>` but never says the close depends on it. So a run that
files a review record and never calls `--review` is blocked at close by a rule no carrier published,
and the cheapest recorded exit is `--override closing-review-recorded` — the run authorizing itself
past the item.

Nothing on the bar can see this. Check 16's DoD parity arm (`check-unattended.sh:1578-1595`) joins
item NAMES and the count sentence above the table; the checker column is deliberately unjoined, per its
own comment, and no arm reads a cell's PROSE at all. Spec 8 S5 was deleted and no unit claimed the row,
so the edit is UNOWNED rather than deferred; the `specs-audited` row added three lines below at `:335`
shows the standard this row now fails.

This is `amendment-leaves-its-other-half-standing` on a refusal item, which is the more expensive
direction: the contract is weaker than the code, so a compliant run gets refused.

**Fix.** Amend the `closing-review-recorded` row in `tools/unattended/PROTOCOL.template.md` to state
both added terms and what it still does not check, then re-render `memory/guides/UNATTENDED-PROTOCOL.md`
with `adopt-unattended.sh` so check 10 stays green. Add one sentence to the Skill's review section
saying the close refuses without a terminal round.

**Left-shift gate.** A co-change leg: when a commit range touches the `dod_met` case block in
`unattended.sh`, `PROTOCOL.template.md` must move in the same range. Cheap, git-only, no parsing, and it
reds exactly this class. It would also have caught L1 and L4 in this diff.

---

### L1 — LOW · `tools/unattended/unattended.sh:3115`

**The defect.** The `build-complete` header still reads "FIVE terms, ALL required" and its S3 note at
`:3135` still reads "the four surviving terms are evaluated SEQUENTIALLY", after this diff added a
block explicitly labelled TERM 6. Both counts are off by one, and "ALL required" is additionally false
for term 6, which turns itself OFF when `SPEC_THIN_CUTOFF` is unset. A third carrier is stale
identically: `PROTOCOL.template.md:331` and its rendered twin say "Five terms, all required".

**Impact.** A count of a derived population written in prose beside the thing it counts — the class §7
names, in an arm whose header is otherwise scrupulous. A reader auditing the arm sees five and stops,
which is how M2's three silent skips stay unreviewed.

**Fix.** Say six in all four places, add term 6 to the enumeration, and note that term 6 is conditional.

**Left-shift gate.** Derive it rather than typing it: a leg comparing the spelled count in the header
against `grep -c '# ---- TERM\|# TERM' ` within the arm. Or delete the number — a header that says "the
terms are numbered below" cannot go stale.

### L2 — LOW · `tools/unattended/unattended.sh:3376`

**The defect.** `specs-audited` selects the record kind with `/^\*\*Serves:\*\*/ && /spec-audit/` —
the substring anywhere on the line — while the id join on the very next line was deliberately hardened
to `grep -qxF`. `RECORD_KIND_TOKENS` makes the kind the FIRST token
(`tools/memory-tree/gen_build_index.py:511`), which is the anchor this predicate declines to apply, and
`PROTOCOL.template.md:335` promises a record "of kind `spec-audit`" — stronger than the code.

**Impact.** Any tracked record under the build whose `**Serves:**` line merely MENTIONS `spec-audit` in
free text certifies every id on that line. The gap is reachable without tripping any gate:
`gen_build_index.py:490` strips a trailing `<!-- … -->` note before parsing, so
`**Serves:** research TOOL-x-1 <!-- inferred: from the spec-audit round -->` is a conformant `research`
binding under hygiene check 21 and satisfies this join for `TOOL-x-1`. The corpus already carries such
notes (`memory/builds/aBatchedLintel/reviews/2026-08-03-review-TOOL-aBatchedLintel-1-1.md:3`). Measured:
116 tracked `**Serves:**` lines contain `spec-audit` and none is non-anchored today, so this is a latent
widening rather than a live miss — but it is the false-CERTIFICATION direction on a refusal item.

**Fix.** `/^\*\*Serves:\*\* spec-audit([ \t]|$)/ { print }`.

**Left-shift gate.** A driver self-test fixture: a `research`-kind record whose Serves line mentions
`spec-audit` in free text, asserted NOT to satisfy `specs-audited` for the id it names.

### L3 — LOW · `tools/unattended/unattended.sh:3356`

**The defect.** `specs-audited` (`:3356`) and TERM 6 (`:3197`) extract unit ids from generated roster
rows with the unscoped `_ids_of` (`:1847`, `grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+'`), while
`unit_ids_of` (`:1702-1707`) reads the same region with `[A-Z]+-$slug-[0-9]+` and is used 46 lines
earlier at `:3151` in the very same function.

**Impact.** A generated row is `| [<id> — <spec H1 title>](spec/<file>) | … |`, so the title is free
prose. A title citing a sibling build's id — a DEPENDENCY reference, which `verb_plan`'s own header
calls out by name at `:1672` — lands a foreign id in `_sa_ids`. `specs-audited` then demands a
spec-audit binding line naming an id whose records live under a different build folder that
`GIT ls-files -- "$M/builds/$slug/"` never reads: a false RED on a DoD item at close, resolvable only
by an override. Measured: 0 of 80 tracked generated regions carry a foreign id today, so latent.

**Fix.** Scope both selections to the build's own slug, e.g. `| grep -oE "[A-Z]+-$slug-[0-9]+" | sort -u`,
so the CLOSED-row extraction agrees with every other roster reader in the file.

**Left-shift gate.** A grep leg asserting that no `_ids_of` call in `unattended.sh` takes generated
roster rows as input — mechanically, that `_ids_of` appears only where `unit_ids_of` cannot, with the
exceptions named. Cheap, and it stops the pair diverging again.

### L4 — LOW · `tools/unattended/unattended.sh:409`

**The defect.** The parked-kind taxonomy comment still asserts "MEMBERSHIP IS DECLARED HERE AND NOWHERE
ELSE … there is no second set to keep in step. That is the whole reason it is one constant and not
two." `PARK_ACTS_OWED="retire supersede"` at `:369` — added by this same diff — falsifies it: a
`rescope` row is history by KIND yet owed by ACT, which both counters union (`:2658`, `:3410`) and which
`history_exclude_re` states outright at `:3536` ("it has TWO AXES because the owed side does"). The
protocol copies WERE amended to "Membership is declared on TWO AXES" (`:196`, both copies, commit
`788908bc`); this block was not.

**Impact.** The file the gate leg reads the constants OUT OF now contradicts the file that governs it. A
maintainer adding a kind or an act reads this block, concludes no second set exists, and updates one
axis — precisely the divergence the two-axis split was built to prevent.

**Fix.** Rewrite `:409-411` to name both axes: membership is `PARK_KINDS_OWED` (kinds) plus
`PARK_ACTS_OWED` (rescope acts), `history` is the complement on both, and point at the reason the pair
is two constants rather than one `kind:act` grammar, already stated at `:357-368`.

**Left-shift gate.** M3's co-change leg covers it: `PARK_ACTS_OWED` moving without the taxonomy block
moving is the same shape. A narrower version is a grep that reds when `PARK_ACTS_OWED` exists and the
string "NOWHERE ELSE" survives within thirty lines of `PARK_KINDS_OWED`.

### L5 — LOW · `tools/unattended/unattended.sh:3202`

**The defect.** Spec 4 AC2 reads "the item is MET **and the grandfather is announced**". The
implementation is `printf '%s\n%s\n' "$SPEC_THIN_CUTOFF" "$_bcdate" | sort -C || continue` — a bare
`continue` writing nothing to `DOD_OUT`.

**Impact.** A CLOSED unit whose spec grades THIN but predates the cutoff passes with no output at all,
so a reader cannot distinguish a build where the term found nothing from one where it EXEMPTED units it
graded. The mechanism plainly exists and is used one branch above: the blank-cutoff case sets `DOD_OUT`
and returns 0, and the suite asserts it. This is an omission, not an impossibility.

**Fix.** Accumulate grandfathered ids into `_bcold` and, on the passing return, set
`DOD_OUT="note — N CLOSED unit(s) grade THIN and are grandfathered by SPEC_THIN_CUTOFF=…:$_bcold"`.

**Left-shift gate.** Extend the existing AC2 arm at `unattended.test.sh:4849-4851` with a positive
`hit` on that sentence. Today it asserts only `miss "$out" "grades THIN"`, which passes whether or not
the announcement exists — the unmet half of the AC is invisible to the suite, which is the reason it
shipped unmet.

### L6 — LOW · `tools/unattended/unattended.test.sh:1628`

**The defect.** Spec 4 AC4 (`--plan` prints the grade BESIDE `DONE`, not in place of it) has no
assertion that can fail. `grep -rn 'DONE ('` over the whole kit returns exactly ONE hit — the
implementation at `unattended.sh:2018` — and nothing in any test file. The only arm reaching that line
over a terminal thin spec is `:1626-1629`, which asserts `hit "$out" "DONE"`; that substring matches
under both the old `state="DONE"` and the new `state="DONE ($state)"`, and the
`case "$state" in THIN|FORKED)` next-target branch matches neither form, so the `next:` line is
unchanged too.

**Impact.** Reverting the `verb_plan` edit leaves the suite green at its raised assertion floor. A test
that passes on both sides of the change certifies coverage that does not exist — the human-facing half
of unit 4 is covered by nothing.

**Fix.** Change the assertion to `hit "$out" "DONE (THIN)"` (the fixture at `:1626` is CLOSED with empty
scope, AC and gates, so it grades THIN) and add a sibling arm asserting a READY closed spec still prints
bare `DONE`. `containment-tested-one-way`, and the second arm is the other way.

**Left-shift gate.** The assertion above IS the gate. The class-level version is a rule this repo can
enforce cheaply: an assertion whose expected string is a strict PREFIX of the value the change
introduced is a passing-before-and-after assertion, and a diff-scoped grep can flag new test arms whose
`hit` strings existed verbatim in the pre-diff output.

### L7 — LOW · `tools/unattended/check-unattended.sh:1492`

**The defect.** `_no_core=$(printf '%s\n' $DOD_NO_OVERRIDE | grep -c . >/dev/null; printf '%s\n' $DOD_NO_OVERRIDE | sort -u)`
— the first subshell command computes a line count, redirects it to `/dev/null`, and has its exit
status discarded by the `;`. The script sets `set -u` only (no `set -e`), so this contributes nothing:
no output, no status, no side effect.

**Impact.** It READS like an emptiness guard for the `comm` below and is not one — the actual empty-set
guard is the `[ -z "$DOD_NO_OVERRIDE" ]` branch fifteen lines above at `:1477`. A maintainer trusting it
would believe the anti-vacuity arm is doubled when it is single. The count idiom it was copied from
(`_ndc=$(… | grep -c . || true)`) actually consumes its count.

**Fix.** Delete the first clause: `_no_core=$(printf '%s\n' $DOD_NO_OVERRIDE | sort -u)`.

**Left-shift gate.** A shellcheck leg over the kit would flag the discarded substitution class
generically. Absent that, no gate is worth building for a one-line deletion — this one belongs on the
§10 checklist as "a guard whose output goes to /dev/null guards nothing".

### L8 — LOW · `tools/unattended/check-unattended.sh:1476`

**The defect.** `_no_tmpl="$HERE/SKILL.template.md"` is a second variable holding the path `tmpl`
already holds unconditionally at `:1327` — bound there deliberately, per its own comment, so later arms
can read it from outside the branch that used to assign it. Check 26 still reads `tmpl` at `:1986`.

**Impact.** One fact with two names in one script. Relocating the shipped Skill template updates one
spelling and leaves the other resolving to a missing file, at which point 16d takes its
`[ ! -f "$_no_tmpl" ]` branch and reports "the kit ships no SKILL.template.md" while 16a and 26 read it
fine — contradictory verdicts from one run. The leg's own header states the core sets are read from the
driver "never restated here" for exactly this reason. Caveat, stated because the severity depends on it:
both sites spell the literal `SKILL.template.md`, so a grep-driven rename would in practice catch both,
which makes the contradictory-verdict story weaker than the duplication itself.

**Fix.** Drop `_no_tmpl`; use `$tmpl` in 16d's guard and awk invocation.

**Left-shift gate.** None worth building. `two-answers-to-one-question` is already on the §10 checklist
and this is a checklist catch, not a gate catch.

### L9 — LOW · `.unattended.conf:135` and `tools/unattended/.unattended.conf.example:137`

**The defect.** The `SPEC_THIN_CUTOFF` comment block and its assignment were spliced into the MIDDLE of
`UNITS_REGION_CUTOFF`'s comment paragraph, in both carriers. In `.unattended.conf`, line 135 ends
"Moving it later re-opens the vacuity for every BASE in", the new key's eight-line comment and its
assignment follow, and the orphaned remainder — "# between; moving it earlier refuses runs whose BASE
predates the region and can never carry it." — lands at line 145 as `UNITS_REGION_CUTOFF`'s ENTIRE
comment. `.unattended.conf.example` carries the same splice cut one clause later ("…refuses runs" /
"# whose BASE predates the region and can never carry it.").

**Impact.** Worse in the example, which is the file every adopter copies and reads to set both cutoffs.
There the whole "BLANK is the off switch / a BASE with no region is a REFUSAL" rationale now sits
directly above `SPEC_THIN_CUTOFF=`, so a reader attributes it to the wrong key, and the key it actually
describes is left documented by a clause starting mid-sentence — losing exactly the property an operator
needs before moving the date. This kit's whole premise is that agents read these declarations rather
than the code.

**Fix.** Move the `SPEC_THIN_CUTOFF` comment block and assignment BELOW `UNITS_REGION_CUTOFF="…"` in
both files, restoring each comment to one contiguous block above the key it documents.

**Left-shift gate.** A cheap structural leg over both conf carriers: every `KEY=` must be preceded by a
comment block, and no comment block may BEGIN mid-sentence (first word after `# ` lowercase and not a
`TOOL-`/`KICK-`/`PLAY-`/`DEPL-` id). That predicate reds `UNITS_REGION_CUTOFF`'s "# between;" today,
and it is the kind of check whose failing case can be staged in one line.

---

## What this review did NOT check

Stated plainly, per the charter's rule that a skip announces itself.

- **The gate leg and the driver suite were not re-run for a verdict.** The MEASURED state handed to
  this review — the leg GREEN, the driver suite GREEN at 895 assertions, up from 864 — was taken as
  given and not reproduced.
- **`check-unattended.test.sh` was analysed but never observed failing.** Two attempts to run it end to
  end were made. The first exited non-zero after a long run having captured no output; the second
  exceeded a ten-minute budget and was abandoned, which is consistent with a suite whose siblings once
  cost 3339 s of a 4926 s bar. H2's RED conclusion is therefore DERIVED from the source — a `grep -c`
  returning 0 for an asserted string against a `grep -qF` assertion, which is conclusive as reasoning
  — and not witnessed. Said plainly because a skip that looks like a pass is indistinguishable from
  coverage, and this one is on the finding that is itself about an unobserved suite.
- **No unattended run was executed.** Every finding is static: source read at the cited lines, plus
  corpus census by `git ls-files` and `grep`. Nothing here exercises `--close` end to end, so a defect
  reachable only through phase interaction would not appear.
- **The three spec-audit records were read for their folded findings and not re-audited.** By
  instruction; their findings are not re-raised.
- **Records, front matter and ledger rows were not graded.** The lens is the build's own: what lets a
  run do worse work and land it green. Bookkeeping is out of scope by the build-level rule.
- **Unit 3 (`WONTDO`) has no code to review.** Its retirement and the parked fork behind it were read
  as context for H2 and are otherwise untouched. This review takes no position on which of its five
  options the owner should pick.
- **§9 limits are unchanged and unexamined.** Nothing in this diff alters what a check running under
  the run's own uid can buy, and this review makes no claim about run honesty.

## Disposition

Six findings are one-line or one-block fixes with no design question attached: L1, L4, L7, L8, L9, and
the anchor in L2. Two are corrections to the record rather than to code: M3, and the spec-6 header text
B1 asks for once its exemption is settled. H1 is a six-line paste of a refusal its own sibling already
carries. Three need a decision before a fix is written: B1 (drop the exemption, or keep it and document
the hole it leaves and which arm covers it — none does), M1 (implement AC3b as specced, or amend spec 6
and re-close the unit), and H2 (repairing the suite is mechanical; keeping it from happening again is
the parked self-test fork, which is an owner turn).

The landing bar is B1 and H1 — both are shipped behaviour, both make the RETIRE arm quieter than the
code it replaced, and both are one small edit each. H2 is the bar for the NEXT person to touch this
kit rather than for this landing, since the skip that produced it is recorded and instructed.
Everything below that can ride a follow-up without weakening what this build shipped, and the ten
CLOSED units are otherwise sound: the four new refusal items read evidence that was previously
recorded and never opened, which is exactly what the build set out to do.
