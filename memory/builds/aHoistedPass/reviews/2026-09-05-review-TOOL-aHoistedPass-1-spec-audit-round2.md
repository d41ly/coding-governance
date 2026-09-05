**Serves:** spec-audit TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1

# Tier-2 spec audit — the aHoistedPass spec set

*Adversarial pre-code pass over all ten unit specs, run against the rev-3/rev-4/rev-5 folds that
answered round 1. Node `a`, 2026-09-05, ROUND 2. Every finding below survived a skeptic prompted to
refute it; each carries its address, its fix, and the gate that would have caught it before a human
had to read for it.*

**Reviewed subjects, pinned at blob:**

- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-1.md`@`d897146b58132b8e50f7c6abd82b2ef89ee920d4`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-2.md`@`fd70fc79eb147e169625aa976dd5bbaebcdb341f`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-3.md`@`7fb55cffc82ba5eb92748e1b133597f50571939a`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-4.md`@`37c044cd61946d65bb538b0c329c7e60ac279fc0`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-5.md`@`de4c6476bd3e3f191e40cca1d91021ee5b399dc3`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-6.md`@`8e8bd81ea97bc74c32b83ff4dc11fd70a9443775`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-7.md`@`06638638fde8ea66dd46a19e084c07c9d130f452`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-8.md`@`f6202970a7adeca66db666311d14c85d455c4f99`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-9.md`@`5531b37fd3fd4477709cf96e6e587a71011c4f70`
- `memory/builds/aHoistedPass/spec/2026-09-04-spec-DEPL-aHoistedPass-1.md`@`aa409e546aae377cc2b102bcd09d68bc3f4052af`

All ten pins were re-hashed against the working tree with `git hash-object` at report time and match
byte for byte, so every address below is an address in the text as pinned.

## Verdict: BLOCKED

One finding at BLOCKER severity, eleven at HIGH, seven at MEDIUM, one at LOW — twenty adjudicated
rows drawn from twenty-three confirmed findings, after I merged three pairs that two lenses each
reported as one defect. The blocker is `TOOL-aHoistedPass-7`, which reproduces round 1's only blocker
one file over: every `tools/unattended/check-pass-order.sh` span the spec builds on is a `c4fcf5ad`
address naming unrelated code at the run's BASE, and its S1/S2 tell the builder to lift those spans
whole. That one is not a fix-while-building item — the spec has to be re-derived at BASE first.

The high band is dominated by one structural fault and one arithmetic accident. The fault is that
`DEPL-aHoistedPass-1` took the whole `unattended` 1.17-to-1.18 bump in its fork resolution, and the
handover was incomplete in four separate ways: the destination spec does not book the carriers, does
not list the leg the bump pulls in, does not record the owner turn it inherited, and does not carry
the ninth-carrier gap the source spec paid to discover — while two source specs still book carrier
edits in their Files-touched tables. The accident is that the repo's lexicon verb pin sits exactly at
its ceiling right now, so `TOOL-aHoistedPass-5`'s fold-confirmed `function need(key, why)` reds the
bar on landing, with no scope item, no criterion and no gate row anywhere in that spec.

`TOOL-aHoistedPass-8` drew zero findings this round. No lens died, so that zero is evidence within
this review's scope rather than a gap in it.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates
  recorded by the orchestrator's own dedup pass.
- Unverified findings carried into this report: 0. There is no OUTSTANDING band below.

Every integrity counter is zero, so this run is complete and the finding set is not truncated by a
dead arm.

## Review shape

- Raw findings: 39
- Confirmed: 23
- Refuted: 16
- Unverified: 0
- Precision: 0.59

Precision sits just above the 0.5 floor §8 names as the retune threshold, so the lens priming stays
as it is for a round 3. Three of the twenty-three confirmed findings were the same defect reported by
two lenses each; I merged those pairs at adjudication rather than counting them twice, and each
merged row names both source ids. The orchestrator's dedup pass reported none, which is worth a note:
its duplicate test did not catch a pair whose two reports address the same defect through different
sections of one file.

## Findings

Severity is the one I adjudicated here, not the lens's. Where I moved a lens's rating, the row says
so.

### BLOCKER

**B1 — `TOOL-aHoistedPass-7` is written against a tree that no longer exists, and its S1/S2 tell the
builder to copy from it.** *(source id 23)*

`memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-7.md`, section 2 S1/S2, section 4
"The anchor, measured", section 10.

Every `tools/unattended/check-pass-order.sh:<span>` this spec builds on is a `c4fcf5ad` address that
names unrelated code at BASE `e828f778`. Verified at BASE: `:172-215` is the WAIVER REGISTRY prose
plus the `PREANCHOR_CAP` range validation, not the build-commit selection — that is `_find_build_commit`
at `:337`, exactly as this spec's own section 8 says. `:59-102` ("the subshell conf import") is
PREVIEW arg parsing. `:132-145` ("the dated cutoff") is the `plan_state` slice; the cutoff is at
`:153-166`. `:217-221` ("anchors on the build commit's FIRST PARENT") is counter initialisation.
`:245-263` ("the four-count liveness line") is THE RANGE comment block; the liveness line is at `:440`.
`:106-108` (the header sentence forbidding a second copy) is the conf-import `eval` allow-list.

S1 tells the builder to copy named spans as the new leg's skeleton and S2 tells it to lift `:172-215`
"whole" — which is now an exemption registry. A builder following the spec literally ships a waiver
registry inside a pass-order leg. The document contradicts itself on this point: section 8 was
re-derived at BASE and names `_find_build_commit` at `:337` and `_report` at `:325` correctly, so
rev-4 had the file open at BASE and left S1, S2, section 4 and section 10 in the old frame.

*Fix:* re-open the file at BASE and re-cite by NAME — the selection is `_find_build_commit`, the
report helper is `_report`, and each reused block goes by its own heading comment. Keep the BASE line
number as a convenience only, exactly as `TOOL-aHoistedPass-5` rev-4 and `TOOL-aHoistedPass-6` rev-4
did after the identical finding in round 1.

*Left-shift gate:* **G-SPAN**. A spec lint that, for every `path:NNN` or `path:NNN-MMM` citation in a
spec carrying an adjacent quoted phrase, asserts the phrase occurs within a small window of that line
at the spec's declared `base`. This is the third appearance of this class in two rounds across three
files; it is the single highest-value gate in this report.

### HIGH

**H1 — `TOOL-aHoistedPass-2` grades two different scope items under one criterion id.** *(source ids 1
and 12, merged; lens ratings high and medium, adjudicated high)*

`…-spec-TOOL-aHoistedPass-2.md`, section 6, `- **AC18**` at `:418` and again at `:453`.

Confirmed by grep at the pinned blob: two criteria carry the label AC18. The first is rev-3's
insertion grading S5's rewritten `:635-637` sentences for DISPOSAL and the roster hand-out; the
second is the pre-existing criterion grading S7's three residual clauses. The spec keys its own
acceptance ledger on these ids — rev-3's log walks "AC1 to AC17" by number — so one verdict row can
be reported as satisfying both obligations. Whichever is checked, the other ships unobserved, and one
of them is the rewrite rev-3 added precisely because that false text could otherwise survive a green
landing.

*Fix:* renumber the S5 criterion to AC19, leave AC18 with S7's residual clauses, and open each with
the S item it grades. Update rev-3's revision-log line, which says "AC18 added", to the new label.

*Left-shift gate:* **G-DUPAC**. Assert that `AC<n>` labels within a spec's section 6 are unique and
form a contiguous 1-up run. Two lines of shell, and it would have caught this at authoring time.

**H2 — `TOOL-aHoistedPass-4` closes a backlog row that no criterion reads.**

`…-spec-TOOL-aHoistedPass-4.md`, section 2 S6, against section 6 AC1–AC13.

S6 closes `TOOL-dFoldedVerdict-8` in `memory/backlog/TOOL.md`. The rev-3 rewrite gave S4 criteria
(AC10, AC12) and S5 criteria (AC8, AC9) and left S6 with none. AC13 runs
`check-memory-hygiene.sh`, which grades row shape and ids rather than the status token, so it passes
on `OPEN` and `CLOSED` alike. The unit whose narrowed purpose is S4/S5/S6 can therefore land with the
row it exists to answer still `OPEN` at `memory/backlog/TOOL.md:11`, with every leg green. The
sibling convention is unanimous against this: DEPL-1 AC14, TOOL-1 AC3/AC8 and TOOL-6 AC24 each grade
their own backlog scope item.

*Fix:* add an AC asserting `grep -n "TOOL-dFoldedVerdict-8" memory/backlog/TOOL.md` returns exactly
one row whose status field is `CLOSED` and whose text names the widening that answers it.

*Left-shift gate:* **G-SCOPE-AC**. For every `S<n>` in section 2 that is not struck, assert at least
one section-6 criterion names it. Three findings in this report are this one class.

**H3 — `DEPL-aHoistedPass-1` performs a kit bump it books four files for.**

`…-spec-DEPL-aHoistedPass-1.md`, section 4 "Files touched (estimate)" and section 7 Gates, against
section 2 S8, section 8 F1 RESOLVED, and AC10.

Section 8's fork resolution makes this unit the performer of the whole `unattended` 1.17-to-1.18 move
at order 2 — and `TOOL-aHoistedPass-2` S11, `TOOL-aHoistedPass-7` S8 and `TOOL-aHoistedPass-9` S7 were
each struck to a bare assertion on the strength of that. Section 4 then books only four files:
`kit.toml`, `govkit.py`, `selftest.py`, `backlog/DEPL.md`. Missing are the three engine constants
(`unattended.sh:42`, `check-unattended.sh:40`, `check-pass-order.sh:38`) and the five tracked
`tools/unattended/*.template.md` markers — which together are exactly the eight
`tools/check-kit-versions.sh:164-192` grades, and exactly where AC10's "eight carriers" comes from.

Worse, measured on this tree, `gov:kit unattended@1.17` also sits in five RENDERED carriers:
`.claude/skills/unattended/SKILL.md:5`, `memory/guides/UNATTENDED-PROTOCOL.md`,
`memory/guides/PLAYBOOK-TEMPLATE.md`, `memory/guides/UNATTENDED-VERBS.md` and
`tools/unattended/playbook.fixture.md`. `tools/unattended/adopt-unattended.sh:182-202` renders those
five and `--check` diffs them, which is the leg `unattended skill wiring` — guard `None`, chunk
`wiring`, so it runs on every bar. Section 7 names neither that leg nor `kit/dogfood doc parity`.
Bump the eight and skip the re-render and the bar reds at a boundary this spec never mentions.

*Fix:* add the eight carriers and the five renders as Files-touched rows, deriving the carrier set
with `bash tools/check-kit-versions.sh` rather than typing a count. Add `unattended skill wiring`
(`bash tools/unattended/adopt-unattended.sh --check`) to section 7, with a criterion that the renders
were regenerated by the adopter rather than hand-edited.

*Left-shift gate:* **G-GATELEG**. Derive the gate list in section 7 from `tools/gate-legs.json` by
matching each leg's guard against the spec's Files-touched paths, and red on a leg that matches but
is unlisted. Pairs with **G-CARRIER** below.

**H4 — the owner turn migrated to `DEPL-aHoistedPass-1` and is recorded in no section of it.**

`…-spec-DEPL-aHoistedPass-1.md`, section 8, the RESOLVED addendum against F1's own body.

F1's body at `:328-329` states plainly that because the bump edits `SKILL.template.md`'s marker,
whichever unit takes it becomes an owner turn under ruling D1. The RESOLVED addendum at `:341-347`
awards the bump to this unit and simultaneously asserts the picks were taken "under the standing
mandate's delegated resolver authority" and add no carrier beyond ratified scope. Tree check:
`tools/unattended/SKILL.template.md:5` carries `gov:kit unattended@1.17` and AC10 requires all eight
carriers at 1.18, so this unit does edit that carrier. `memory/guides/BUILD-METHOD.md:76` says the
delegation does not reach veto 2's governance-carrier clause, which is `:84`. No section of this spec
classifies the unit either way.

`TOOL-aHoistedPass-6`, `-7` and `-9` each re-derive themselves as NOT owner turns by pointing at this
unit, and TOOL-7 `:217` and TOOL-9 `:198-206` use the same sentence about a classification derived
from an edit the unit does not make. The classification decides whether an unattended run may land
the unit at all, and it now sits nowhere.

*Fix:* state in the RESOLVED addendum, and beside the carrier list in section 4, that taking the bump
puts `SKILL.template.md`'s marker in this unit's diff and therefore makes it an owner turn under D1 —
or, if the run cannot make an owner turn, hand the bump to a unit that can and re-open the three
siblings' stand-downs.

*Left-shift gate:* **G-XREF**. Assert that when spec A strikes a scope item to "unit B takes it", spec
B contains a live scope item claiming it, and that any unit whose Files-touched set intersects the
veto-2 carrier list carries an explicit owner-turn classification.

**H5 — `TOOL-aHoistedPass-2`'s Files-touched table still moves three carriers its S11 was struck to
disclaim.**

`…-spec-TOOL-aHoistedPass-2.md`, section 4 "Files touched (estimate)", against S11 and AC15.

S11 at `:53-61` is struck to "this unit moves neither", and AC15 requires `check-kit-versions.sh`
exit 0 at whatever values order-2 sets. Three surviving table rows disagree:
`tools/unattended/check-unattended.sh` at `:335` reads "…header, constant and marker",
`tools/unattended/PROTOCOL.template.md` at `:337` reads "…§9's clauses, marker", and
`tools/unattended/SKILL.template.md` at `:339` reads "…prompt-path read step, marker". A builder
following the table at order 3 moves a constant and two markers that DEPL-1 already set at order 2,
breaking marker-to-constant agreement and redding the very leg AC15 requires green. rev-4 at `:568-575`
records that it was fixing this exact half-standing in the Migration prose, and left the table the
prose belongs to.

*Fix:* strike "constant and marker" from the `check-unattended.sh` row and "marker" from the two
template rows, matching the `BUILD-METHOD.template.md` row, which already reads "**not the marker**".

*Left-shift gate:* **G-FILESTOUCH**. Cross-check section 4's Files-touched cells against section 2:
red on a cell describing an edit whose only scope item is struck.

**H6 — `TOOL-aHoistedPass-4`'s section 4 still builds the work section 2 struck as landed.**

`…-spec-TOOL-aHoistedPass-4.md`, section 4 (the Data model block, "The count is the acceptance", the
Files-touched table) and section 5, against section 2's LANDED strike and AC1/AC4/AC7/AC8.

Section 2 struck S1–S3 as landed under `TOOL-aWeldedTribunal-1` and section 6 was rewritten to
verification, but section 4 still specifies them as this unit's build. Its Data model at `:101-121`
declares `LOOP_HEAD`/`LOOP_TAIL` while AC1 names the four constants that actually shipped —
`LOOP_KEYWORDS`, `LOOP_HEADER`, `LOOP_HEADER_G`, `LOOP_KEYWORD_TAIL` at `agent-cap.js:476-479`.
"The count is the acceptance" at `:129-132` asserts the raw literal `(for|while)` does not appear in
the file at all, which AC4 overturns as an observed count of 1 and names as the
`absence-assertion-over-whole-file-text` class. And the Files-touched table books
`tools/hooks/agent-cap.test.sh` for "four DENY arms, three control arms" plus six predicate sites —
four `tools/` files against AC8's "exactly three", and against AC7's requirement that the commit
touch neither the predicate block nor the test arms. Section 5's "staged RED before the widening
lands" bullet is the same leftover, contradicted by section 6's own recorded LOSS that the failing
case is no longer observable. Section 2's "kept as written" licence covers the struck scope items
only; section 4 carries no such annotation, so a builder working from it rewrites shipped constants
under names that no longer exist.

*Fix:* restate section 4's Data model as the landed shape at `agent-cap.js:476-479` (or strike it with
the same annotation S1 carries), correct the count paragraph to the observed 1 with its reason, drop
the `agent-cap.test.sh` row and the six-site clause, and rewrite section 5's testing bullet to the
LOSS section 6 already records.

*Left-shift gate:* **G-STRUCK**. When a scope item is struck, red on any surviving non-annotated prose
elsewhere in the same file that still specifies its operands. Four findings in this report are this
class.

**H7 — `TOOL-aHoistedPass-4` AC7's witness cannot show what AC7 claims, and this unit's own commit
makes it false.**

`…-spec-TOOL-aHoistedPass-4.md`, section 6 AC7.

Measured: `git log --oneline -1 -- tools/hooks/agent-cap.js` returns `4b13ecac records+kit(aWeldedTribunal):
the DoD bookkeeping the full bar demanded`, not `TOOL-aWeldedTribunal-1`. The commit that actually
landed the constants is `cc8776b8`, eight commits back — a fact sibling `TOOL-aHoistedPass-5` rev-4
already recorded. Worse, S4 and S5 both edit `tools/hooks/agent-cap.js`, so after this unit commits
the same `-1` read returns THIS unit and the criterion reads as a refutation of its own claim.

*Fix:* witness the attribution with a command that survives the unit's own commit —
`git log -S 'LOOP_KEYWORDS' --oneline -- tools/hooks/agent-cap.js` naming `cc8776b8
TOOL-aWeldedTribunal-1` — and keep the "not this unit" half as the diff assertion AC8 already makes.

*Left-shift gate:* **G-WITNESS**. Run every AC whose witness is a shell command at the spec's declared
base and assert it produces the output the criterion claims. A criterion nobody has ever run is an
assertion about nothing, which is §7's own rule applied to specs.

**H8 — `TOOL-aHoistedPass-6`'s KEEP row and its normative return block describe different arrays.**

`…-spec-TOOL-aHoistedPass-6.md`, section 4, "What S2 does NOT delete" against "The return — four
exits, one predicate".

The KEEP row at `:132` says `buildUnits` "becomes the roster filter". The return block at `:253`
spells `roster: ordered.map(...)`, and the exit table's fourth row says "the ordered array". Verified
at HEAD, `tools/workflows/unattended-build.js:765` is
`const buildUnits = ordered.filter(function (u) { return skippedDone.indexOf(u.id) === -1 })`, sitting
under a comment naming the exact prior defect ("the BUILD agent was handed the UNFILTERED roster").
`ordered` at `:216` is the unfiltered sort. The two statements cannot both be implemented whenever
attended mode has some-but-not-all terminal units, and written as the code block spells it, the
attended `planState` refusal S2 deliberately KEEPS filters nothing: every already-terminal unit is
handed out for dispatch, which is the precise outcome the KEEP row exists to prevent. AC7 grades
three objects in order sequence and AC8 grades only `dispatch.args` keys, so neither distinguishes
the arrays.

*Fix:* make the return block map `buildUnits`, and say whether `units:` still counts `ordered`. If the
roster is deliberately unfiltered with `skippedTerminal` as the caller's filter, say that and drop
the "becomes the roster filter" clause. Either way, add an AC asserting a `skippedDone` unit is
absent from `roster` in the attended fixture.

*Left-shift gate:* no cheap lint reaches this one — it is a semantic contradiction between two prose
blocks. The compensating check is the AC above, and the documented manual check is that a spec whose
section 4 contains a normative code block re-reads that block against every KEEP/DELETE row in the
same section during the fold. Left-shift it into §10's checklist as
`normative-block-contradicts-its-own-narrative`.

**H9 — `TOOL-aHoistedPass-7`'s Files-touched table asserts the edit the paragraph beneath it denies.**

`…-spec-TOOL-aHoistedPass-7.md`, section 4 Files-touched at `:204-205`, against the rev-4 owner-gating
paragraph at `:215-221`.

The table still books `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh` and
"the five tracked `tools/unattended/*.template.md` markers" — booked by rev-1 for the 1.17-to-1.18
bump that rev-4 struck to an assertion. `git ls-files` returns exactly five such templates and
`SKILL.template.md`, a veto-2 carrier, is among them. The unit edits none of them: the new script
joins `KIT_SH` by glob, since `check-unattended.sh` builds that list from `$HERE/*.sh`. So two lines
above the paragraph that re-derives "not an owner turn", the table asserts precisely the edit that
would make it one. The spec's own words are that this classification decides whether an unattended
run may land the unit at all, and it asks that any reclassification name the carrier.

*Fix:* strike the two engine rows and the five-template-marker row, the way `TOOL-aHoistedPass-9`
rev-3 struck its two, keeping `tools/check-kit-versions.sh` for S8's genuine script-list entry.

*Left-shift gate:* **G-FILESTOUCH** and **G-XREF**, as above. This is H5's class in a second file and
H4's class in a third, which is why both gates are worth building rather than fixing three rows.

**H10 — `TOOL-aHoistedPass-6` still says a sibling owns a correction that sibling explicitly
disclaims.** *(source ids 28 and 33, merged; lens ratings medium and high, adjudicated high)*

`…-spec-TOOL-aHoistedPass-6.md`, section 3, the third non-goal bullet (`unattended-build.js:63-67`).

The bullet says `TOOL-aHoistedPass-1` "owns that correction by name".
`TOOL-aHoistedPass-1` section 3 says the opposite in bold: "S4's row carries all four, and NO unit of
this build takes any of them — including the `unattended-build.js` one", and names this bullet as the
false half. Spec 1's rev-3 fixed its side; spec 6's rev-4 only re-pointed the ADDRESS (`:34-37` to
`:63-67`, its own rev log says so) and left the ownership claim standing. The disclaim loop still
runs in one direction, so a builder reading spec 6 believes the superseded `parallelism route: none`
citation is being corrected elsewhere and it stays live. Nothing on the bar grades whether a decision
quotation is still true — spec 1 section 4 says so explicitly — so the build closes green with the
carrier uncorrected.

*Fix:* rewrite the bullet to the BASE fact: `TOOL-aHoistedPass-1` S4 FILES the residual and no unit of
this build takes it. Better, take the correction here — this unit already edits
`tools/workflows/unattended-build.js` across S1–S7 and its test file at S9, and already owns the
`review-harness` 1.6-to-1.7 move, so the carrier sites at `:63-67` and `:330-335` cost it no extra
bump.

*Left-shift gate:* **G-XREF**, in its symmetric form: for every spec sentence of the shape
"`<unit-id>` owns/takes `<thing>`", assert the named spec contains a live scope item claiming it.

**H11 — `TOOL-aHoistedPass-5` lands a new function whose verb reds the bar, with no scope item, no
criterion and no gate row.**

`…-spec-TOOL-aHoistedPass-5.md`, section 2 S6, section 8 F1 RESOLVED, section 7 Gates.

Measured live in this worktree at report time: `python tools/lexicon/lexicon.py --check` reports
`P1 verb graded=1059 offenders=467` against `VERB_OFFENDER_PIN="467"` in `.lexicon.conf:186`, and
`lexicon.py:697` reds on `len(unwaived) > pin`. The pin is exactly at its ceiling, with zero headroom.
`--suggest need` answers that `need` is not in the declared table (the twenty-three declared verbs are
`add arm build check cmd derive extract init load main measure parse print read remove render resolve
run scan seed set test write`). `.lexicon.conf:23` declares `js:js-regex:probe`, whose functions
pattern matches `function need(key, why)` wherever it sits, and the leg `lexicon naming predicates`
carries guard `["tools/", …]`, so the very commit landing `tools/workflows/unattended-unit.js` runs it
and reaches 468 over 467.

The spec fold-confirms `function need(key, why)` by name at `:168`, `:368` and `:385`, and section 7's
gate list — which claims to be "all read from `tools/gate-legs.json` at this base" — omits the leg
entirely. The words "lexicon", "verb table" and "naming predicates" appear nowhere in the file. This
is a guaranteed merge-bar RED on the very option F1 chose in order to avoid editing another kit.

*Fix:* name the definition with a table verb — `check`, "assert a predicate and return a verdict",
fits the eight arg refusals exactly — and say so in S6. Otherwise add a scope item raising
`VERB_OFFENDER_PIN` 467 to 468 with the offender NAMED and attributed under `.lexicon.conf`'s own
raise-comment discipline. Either way, add `lexicon naming predicates` to section 7 and an AC asserting
`python tools/lexicon/lexicon.py --check` exits 0 on the landing tree.

*Left-shift gate:* **G-LEXICON-SPEC**. For every new `function <name>(` a spec names in a scope item,
run `lexicon.py --suggest <name>` during the fold and red on "not in the declared table". Cheap
companion: have `--check` print the remaining headroom (`pin − offenders`) on its verb line, so a pin
sitting at zero is visible to anyone reading a green run rather than only to whoever next adds a
definition.

### MEDIUM

**M1 — `TOOL-aHoistedPass-5`'s five prompt acts are observable nowhere.**

`…-spec-TOOL-aHoistedPass-5.md`, section 2 S4, against section 6 AC1–AC15.

S4 specifies five acts the prompt must perform: read brief and spec whole, change the spec first on
divergence, declare the write set with `--dispatch … --writes`, record the brief with `--brief`, and
run the checklist command. AC10 is the only criterion that reads the prompt string, and it reads S5's
`CLOSED`/`WONTDO` clause plus `--plan`. Nothing observes any of the five. Section 7 states that no
standing leg calls this file at all, so a prompt shipped without the `--brief` instruction is
observable nowhere — while `TOOL-aHoistedPass-7`'s entire leg grades that a brief row exists at the
build commit, and the only thing that writes one is this prompt. No non-goal withholds this: section
3 excludes the parent, the Skill and protocol edits, and the fan-out predicate, none of which is the
prompt.

*Fix:* extend AC10 (or add AC16) to grep the landed prompt for each of the five acts by name —
`--writes`, `--brief`, the checklist command token, the spec-first divergence rule and the read-whole
step — the way AC10 already greps the status flip.

*Left-shift gate:* **G-SCOPE-AC**.

**M2 — `TOOL-aHoistedPass-3`'s gate keeps under-reporting its own exit codes.**

`…-spec-TOOL-aHoistedPass-3.md`, section 2 S6, against section 6 AC1–AC15.

S6 adds exit 6 and the already-omitted exit 4 to the exit-code list in
`tools/check-template-size.sh:17-19`, which today documents 0, 1, 2, 3 and 5. No criterion reads that
header block: AC3/AC4 exercise the new branch's behaviour and message, AC7 grades `check-arms.py`'s
armed/branch counts at 7:7, AC6 the test-suite arms. `check-arms.py`'s population is `fail() {`
definitions and `fail <n> "` call sites plus sibling-test assertions; it never reads a comment, so no
gate substitutes. A gate whose own header misreports its exit codes is the
checker-whose-record-does-not-describe-it class this whole build exists to remove, and rev-3 folded
three findings of exactly this shape into this file while leaving this one.

*Fix:* add an AC asserting that on the landing tree the header names 4 and 6 alongside 1, 2, 3 and 5,
and that the set it names equals the distinct `FAIL_CODE` values the file assigns.

*Left-shift gate:* **G-SCOPE-AC**, plus a small runtime check inside `check-template-size.sh` itself:
derive the documented set from the header and compare it to the assigned `FAIL_CODE` values, so the
pair cannot drift again after this build closes.

**M3 — the ninth `unattended` carrier was dropped on the handover between two specs.**

`…-spec-DEPL-aHoistedPass-1.md`, section 2 S8, against `TOOL-aHoistedPass-2` section 4 "Migration".

`tools/unattended/README.md:1` carries `gov:kit unattended@1.17` and is in neither population
`check-kit-versions.sh` reads — grep confirms the graded eight are three engine constants plus five
`*.template.md` markers. TOOL-2 at `:291-294` measured this and instructed "Move it in the same
commit, and file the gap", with its Files-touched row for that file reading "the ungraded marker, as
a NOTE — not an edit". That instruction was written while TOOL-2 owned the bump. DEPL-1 now owns it
and names neither the marker nor the gap: its S9 backlog rows are the mis-spelled `require` key and
the stale pins, unrelated. A build-wide grep for `unattended/README` and `ninth` finds the finding
stated only in TOOL-2's kept-for-reference prose, assigned to nobody. After the landing the shipped
kit README advertises 1.17 while all eight graded carriers read 1.18, and nothing reds.

*Fix:* extend S8 to move `tools/unattended/README.md:1` with the other carriers, and add a backlog row
(or fold it into S9's) recording that the marker sits outside both populations
`check-kit-versions.sh` reads.

*Left-shift gate:* **G-CARRIER**. Derive the version-carrier set with
`git grep -l "gov:kit <kit>@" -- tools/<kit>/` and assert every hit is either graded by
`check-kit-versions.sh` or named in a registered waiver. That closes the underlying gap as well as the
handover: the README marker only survived because a hand-kept population was one file short.

**M4 — `TOOL-aHoistedPass-2` ships a Skill bullet ordering a flag that will not exist for two orders.**

`…-spec-TOOL-aHoistedPass-2.md`, section 2 S9 and section 4 "The Skill loop bullet", against
`TOOL-aHoistedPass-6` S8.

The bullet this unit ships at order 3 orders a re-read of `--plan <slug> --paths` between dispatches.
`--paths` is built by `TOOL-aHoistedPass-6` at order 5. Verified: `--paths` exists nowhere in the tree
today, and `unattended.sh:4892` is `--plan) shift; … verb_plan "${1:-}"; exit $?`, so a trailing
`--paths` is silently discarded — the run gets the padded table, no spec paths, exit 0, and no
refusal. Between order 3 and order 5 the rendered Skill instructs a run to call a flag the driver
ignores. Section 3's non-goals, fork F2 at `:486-491`, its RESOLVED at `:504-506` and the section 5
risks bullet at `:380-382` each disclose only the dangling `unattended-unit.js` PATH; the dangling
verb mode is disclosed nowhere.

*Fix:* extend F2's disclosure and section 3 to name `--plan <slug> --paths` alongside the script path
as a forward reference held by the run, and state the order dependency on `TOOL-aHoistedPass-6` the
way section 3 already states the one on `TOOL-aHoistedPass-3`.

*Left-shift gate:* **G-FORWARD**. For every CLI flag a spec instructs a shipped artifact to call,
assert the flag either exists at BASE or is named in a disclosed forward reference with the building
unit's id. The cheaper permanent fix lives in the driver: make `verb_plan` refuse an unrecognised
trailing argument instead of discarding it, so a dangling mode is loud rather than silent.

**M5 — `TOOL-aHoistedPass-9` justifies a gate leg by a bump it no longer performs.** *(source ids 20
and 30, merged; lens ratings medium and low, adjudicated medium)*

`…-spec-TOOL-aHoistedPass-9.md`, section 7, second paragraph.

"The version-marker bump is what pulls in `unattended skill wiring`" survives rev-3's strike of S7.
S7 at `:38-44` is struck SPENT ("`DEPL-aHoistedPass-1`'s section 8 F1 takes that single move at
`order 2`"), the Rollout at `:202` states "this unit no longer touches a template marker at all", and
the Files-touched table at `:216-219` records that the two constant rows and the five-template-marker
row left the table. Section 9's rev-4 entry enumerates the strike's consequences and misses this one,
so this sentence is the single surviving statement in the document asserting a marker move the unit
does not make — sitting in the section whose job is to justify the leg list, one section from the
paragraph rev-3 rewrote to kill exactly that derivation. The leg itself is correctly listed: its
guard is empty, so it runs on every bar regardless.

*Fix:* drop the sentence, or keep the leg and give its real footing — unguarded, runs on every bar.

*Left-shift gate:* **G-STRUCK**.

**M6 — three of `TOOL-aHoistedPass-1`'s four carrier addresses are stale at BASE.**

`…-spec-TOOL-aHoistedPass-1.md`, section 3, first non-goal bullet.

Measured at BASE `e828f778` with `git grep -n "parallelism route: none" -- tools/`: the quotes sit at
`agent-cap.js:444`, `agent-cap.test.sh:328`, `unattended-build.js:64` and `README.md:63`. The spec
cites `:412`, `:177`, `:34-37` and `:63`. The first three were exact only at `c4fcf5ad` and resolve at
BASE to RULE 2 prose, blanked-view prose and attended-mode prose respectively. The correction already
existed inside this fold round — `TOOL-aHoistedPass-6` rev-4 recorded `:34-37 → :63-67` for the same
carrier as part of round 1's blocker — and spec 1's rev-3 restated the superseded span anyway.

*Fix:* re-derive the four addresses at BASE with that grep and cite each by its quoted sentence rather
than a span, per the "cite by NAME, not by span" rule `TOOL-aHoistedPass-6` rev-4 adopted. Carry the
corrected addresses into S4's row so AC7's enumeration names live text.

*Left-shift gate:* **G-SPAN** (B1's gate). This is the same class as the blocker at lower blast radius,
which is the argument for building the gate once rather than fixing seven citations.

**M7 — `TOOL-aHoistedPass-1` certifies coverage of a carrier population that is one file short.**

`…-spec-TOOL-aHoistedPass-1.md`, section 2 S4 and section 6 AC7.

`git grep -ln "parallelism route: none" -- tools/` returns FIVE files at BASE and the same five at
`c4fcf5ad`, so this is a measurement error rather than staleness.
`tools/workflows/unattended-build.test.sh` is the fifth: its `:187` and `:194` assert
`TOOL-cBriefedPilot-21`'s ratified `parallelism route: none` in the present tense, `:194` adding "it
failed on E4" — the exact claim `TOOL-dUnstalledConvoy-7` overturned by RUNNING E3 and E4 — and
`:421`/`:424` carry it again. `unattended-build.js` also holds a second site at `:330-335`. S4 says
"the four tracked non-memory carriers" and AC7 grades the row by four basenames, so the criterion goes
green over a population derived at the wrong base, and nothing on the bar grades prose truth.

*Fix:* derive the set in the row rather than typing it — `git grep -ln "parallelism route: none" --
tools/` returns five at BASE. Name all five in S4 and restate AC7 as "the row names every file that
grep returns", so a later carrier cannot be silently outside the population.

*Left-shift gate:* **G-DERIVED-POP**. Any spec sentence of the form "the N tracked …" must carry the
command that derives N, and the criterion must assert the row equals that command's output. This is
§7's "NO count of a derived population is written in prose" applied to specs, where it is currently
unenforced.

### LOW

**L1 — `TOOL-aHoistedPass-1`'s inventory contradicts its own revision log about the row S2 edits.**

`…-spec-TOOL-aHoistedPass-1.md`, section 4 Inventory, the `stale backlog row` row.

Verified at BASE: `memory/backlog/TOOL.md:137` is `TOOL-cBriefedPilot-27` and `:138` is
`TOOL-cBriefedPilot-28`, the row S2 rewrites. The inventory still cites `:137`, while this spec's own
rev-2 log recorded the correction to `:138`, and its own section 4 rejected alternative rejects
line-citing that row at all ("Rows move; ids do not"). The document contradicts itself about the
operand of its own scope item, one section from where the correction was already written.

*Fix:* replace the `:137` cell with the id alone, or with `:138` plus the derivation command, so the
inventory agrees with both the revision log and the spec's own citation rule.

*Left-shift gate:* **G-SPAN**, again — a memory-tree row cited by line is exactly the case its rule
covers.

## Left-shift summary

Twenty findings collapse into eight gates and one checklist entry. Ranked by findings closed:

| Gate | Closes | What it asserts |
|---|---|---|
| **G-SPAN** | B1, M6, L1 | Every `path:NNN` citation with an adjacent quoted phrase resolves to that phrase at the spec's declared base. |
| **G-STRUCK** | H5, H6, H9, M5 | A struck scope item leaves no live prose elsewhere in the file still specifying its operands. |
| **G-SCOPE-AC** | H2, M1, M2 | Every unstruck `S<n>` is named by at least one section-6 criterion. |
| **G-XREF** | H4, H9, H10 | "Unit B takes it" is matched by a live claiming scope item in spec B; a veto-2 carrier in Files-touched forces an explicit owner-turn classification. |
| **G-FILESTOUCH** | H5, H9 | No Files-touched cell describes an edit whose only scope item is struck. |
| **G-CARRIER** / **G-DERIVED-POP** | H3, M3, M7 | Version-carrier and "the N tracked …" populations are derived by command, never typed. |
| **G-GATELEG** | H3, H11 | Section 7's leg list is derived by matching `tools/gate-legs.json` guards against Files-touched paths. |
| **G-DUPAC**, **G-WITNESS**, **G-LEXICON-SPEC**, **G-FORWARD** | H1, H7, H11, M4 | AC labels unique and 1-up; every command-witness AC actually runs at base; every new function name passes `--suggest`; every instructed CLI flag exists or is disclosed. |
| §10 checklist entry | H8 | `normative-block-contradicts-its-own-narrative` — a section-4 code block is re-read against every KEEP/DELETE row in the same section during the fold. |

The first four gates alone close thirteen of twenty findings, and all four are greppable spec lints
rather than semantic judgments. If only one is built, build **G-SPAN**: it is the class that produced
the only blocker in each of the two rounds so far.

## What round 2 says about round 1's fold

The folds worked where they were applied and stopped one section short of where they were needed.
Eleven of these twenty findings are the `amendment-leaves-its-other-half-standing` class the folds
were raised to remove — a strike landed in section 2 and section 6 while section 4, section 7 or a
sibling spec kept the superseded claim. That is not a criticism of any individual fold; it is the
signature of a fold pass that reads the sections a finding named rather than every section the
struck item touches. **G-STRUCK** is the mechanical form of that discipline, and it is the reason to
build it before a round 3 rather than after.

## Disposition of the standing blocker — the M4 exit

Round 1 confirmed one blocker and round 2 confirmed one, so the count did not shrink and the loop is
NON-CONVERGENT. M4 admits exactly two dispositions at that exit and no third.

- **B1 — FOLDED.** It is a defect in a document this review read, so it takes the fold, not the
  promotion: `memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-7.md` is bumped to
  `rev-5` with its section 9 line. Every `check-pass-order.sh` address in S1, S2, S3, section 4 and
  section 10 is re-derived at BASE `e828f778` and re-cited BY NAME, which is the rule
  `TOOL-aHoistedPass-5` rev-4 and `TOOL-aHoistedPass-6` rev-4 adopted after the identical round-1
  finding. Nothing was promoted, because the fix needs no mechanism this build lacks — it needs the
  file opened at the right sha, which the fold did.
- **Not re-reviewed.** M4 forbids it, and the fold is what a round 3 would have measured.

The eleven HIGH, seven MEDIUM and one LOW rows are not blockers and are not disposed here. They stay
as this record wrote them, and each is the property of the unit it names when that unit is built: a
divergence found while building changes the spec first, as a rev bump with its section 9 line. The
eight left-shift gates this report proposes are recommendations to a later build, not scope of this
one.
