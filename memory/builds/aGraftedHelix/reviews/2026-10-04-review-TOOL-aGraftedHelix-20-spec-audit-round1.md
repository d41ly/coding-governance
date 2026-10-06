**Serves:** spec-audit TOOL-aGraftedHelix-20 TOOL-aGraftedHelix-21 TOOL-aGraftedHelix-22

# aGraftedHelix — Tier-2 spec audit of units 20 to 22, ROUND 1

*Node `a`, 2026-10-04, ROUND 1 for these three subjects. Units 20 to 22 are the promotions of the
HIGHs from the round-1 audit of units 16 to 19. Unit 20 closes that round's H1 (finding 9), unit 21
its H2 and H3 (findings 22 and 17), and unit 22 its H4 (finding 6). Four lenses ran:
underspecification, contradiction, unstated assumption and prior art. Every finding in the body
survived a skeptic prompted to REFUTE it. The seven findings the skeptics refuted appear only in the
appendix. The author of this report confirmed that each pinned blob below is the blob at HEAD
(`f708a1343`), by `git rev-parse HEAD:<path>` against `git hash-object <path>`. Unit 20's blob is
its rev-2. Four rows were spot-checked in the tree. For H3, `tools/unattended/unattended.sh:5563`
writes `set_fact "$rel" session "${sid:-absent}"`. For M3, line 5569 stamps `lease-utc` with
`date -u +%Y-%m-%dT%H:%M:%SZ`. For M6, the holder row's only `stage_or_fail` sits inside the
`write_lease`-due branch (lines 6596 to 6600), under a comment saying the row writes NOTHING
otherwise. For H1, unit 20 S2 (spec lines 35 to 39) writes the fact "only while it reads `absent` or
is missing", and its §3 non-goal (lines 71 to 74) lets `--beat`, `--dispatch`, `--close` and the
status writes publish `s2` while leaving the fact alone. The other rows carry the skeptics' verified
text and were not re-derived here.*

**Reviewed at ROUND 1, each subject pinned at its blob:** `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md`@`7475790766868d8dfc36b694b53a455d6f3ee4a8`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-22.md`@`6de816342fafc970383a8b5bacda7121665bd855`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-21.md`@`dad50bb701975d4adb358e4c0d5a68e5850a44e2`.

## Verdict: CLEAN WITH FIXES

No confirmed finding is graded BLOCKER, so every spec is buildable as written. The verdict is not
CLEAN, because fifteen confirmed findings stand and five of them are HIGH. All five HIGHs sit on
unit 20, and every one of them ends in the outcome unit 20 exists to prevent: a live run reading its
own claim as foreign, answering check 90, and being forced to `--abort --code claim-lost`.

- H1 (ids 6 and 12): S2 keeps `prior-session` sticky on the premise that a present value still names
  the published claim's session. Unit 20's own §3 lets `--beat`, `--dispatch`, `--close` and the
  status writes land a claim under the new session without touching the fact, so a second
  incomplete holder push keeps a value the claim no longer carries.
- H2 (id 2): no criterion drives two incomplete holder calls in a row, so a build that writes the
  fact unconditionally passes, and an offline pid restart then locks the run out.
- H3 (id 7): S2 can copy the literal session `absent` into the fact, and S3 reads `absent` as no
  fact, so a run leased with no session id and resumed under one locks itself out.
- H4 (id 1): S3 widens `mine` on the holder and status-write columns, but AC2 drives only
  `--resume`, so a build that widens only that row passes and `--dispatch` then answers check 90.

Nine findings are MEDIUM and one is LOW. Adjudicated, the fifteen confirmed findings form thirteen
items. Two merges were made, each within one binding grade: ids 6 and 12 (both high, one defect in
S2 reached by the contradiction and unstated-assumption lenses), and ids 10 and 15 (both medium, unit
21's late guard leaves rendered views that the re-run refuses). No binding grade was changed. Three
items carry an adjudication note because their fixes interact, all on the `prior-session` fact: H2's
criterion must be read under H1's set encoding, H3's line removal changes M6's clearing condition,
and H1's set encoding changes M7's take-over widening.

Disposition, per `memory/guides/BUILD-METHOD.md`: every CONFIRMED finding is disposed by severity.
Each HIGH is promoted to a unit whose mechanism closes it, audited as a SPEC. Each MEDIUM and LOW is
folded into its spec as a rev bump with a §9 line. Units 20 to 22 are themselves promotions, so
promoting H1 to H4 extends the chain by one more link. The method ends a chain at a promoting round
whose precision falls below the review protocol's floor of 0.5. This round's precision, stated for
that rule to read, is 0.68, so the chain does not end here.

## Review shape

Intensity full. Raw 22, confirmed 15, refuted 7 (ids 16 to 22), unverified 0 (0 uncertain),
precision 0.68.

The adjudicated tally, counted both ways:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 4 | 5 |
| MEDIUM | 8 | 9 |
| LOW | 1 | 1 |
| **total** | **13** | **15** |

By lens, raw then confirmed: underspecification 5 and 5, contradiction 6 and 6, unstated
assumption 5 and 4, prior art 6 and 0.

The prior-art lens carried the whole drop in precision. Its six findings were all refuted, against
fifteen of sixteen confirmed across the other three lenses. Per the review protocol, tighten that
lens's priming before adding agents to the next round.

By unit, counting confirmed findings by the spec each one is anchored on: unit 20 holds 9, unit 21
holds 4 and unit 22 holds 2.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and 0
  duplicates were found.
- Fixes on confirmed findings: 9 judged sound, 6 judged UNSOUND (ids 5, 6, 10, 12, 14 and 15), 0
  with no fix proposed, and 0 NOT JUDGED. An unjudged fix would be the finder's proposal and nothing
  more; none occurs here. For each UNSOUND fix this report writes the skeptic's corrected fix and
  never the rejected one.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, so none is bound at the finder's grade
  by default. 2 were RE-GRADED by the skeptic: ids 3 and 4, each from high to medium.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

This report does not call the run complete. Every lens and every skeptic batch returned, but no
checklist was swept, no intent was supplied, and every lens ran on the generic brief.

**Intent:** NEITHER `specs` nor `context` was supplied to this review. The lenses graded the three
specs against themselves, against each other, against the units they consume from and against the
tree, not against a stated intent for the build.

**Checklist:** NONE swept — absent. The count of recurring-bug-class findings in this report is
therefore not evidence that the project's recurring classes are absent from these specs. This is the
third consecutive round of this build with no checklist. A caller of the next round should pass the
output of `python tools/memory-tree/gotchas.py --for-paths` over the specs' Files-touched paths.

## How the findings cluster

A fold that repairs a class repairs every row in it, so the classes are named here before the rows.

| class | ids | where the gate belongs |
|---|---|---|
| The `prior-session` fact's lifecycle is under-modelled: who writes it, who clears it, what it may hold, whether it is staged | 6, 12, 2, 7, 13, 14 | one sequence fixture in `tools/unattended/unattended.test.sh` that interleaves incomplete holder pushes with every other claim writer |
| An `Observed by` label that no criterion reads | 1, 2, 3, 4, 5 | a spec lint: every S-line's named AC drives the S-line's own stimulus and reads its outcome |
| A staged break that cannot red the arm it is staged against | 5, 8, 10, 15 | the staged break observed RED at VERIFYING, plus a §10 checklist entry |
| A guard placed after the side effects it should precede | 10, 15 | a §10 checklist entry |
| A sibling unit's assertion or spelling the spec relies on but does not amend | 9, 11 | a §10 checklist entry |

The `Observed by` class has now recurred for three rounds: two LOW rows in the audit of units 10 to
15, four rows in the audit of units 16 to 19, and five rows here, two of them HIGH. The previous
report said two rounds is the point at which a lint earns its cost. It has not been built, and this
round's two HIGHs in the class are the cost of that.

Ids appear in more than one class where the defect has two faces. Each id still sits in exactly one
graded item below.

# HIGH

## H1 · id=6, id=12 — S2 keeps `prior-session` sticky, but other writers land the claim under the new session, so a second incomplete push keeps a value the claim no longer carries

- **Address:** TOOL-aGraftedHelix-20 §2 S2 (the "written only while it reads `absent` or is
  missing" clause), against §3 "Clearing the fact from other writers".
- **Defect:** S2 writes `prior-session` only while it reads absent, justified as keeping "the
  session the published claim still carries". That holds only if every claim write that lands also
  clears the fact. §3 says the opposite: `--beat`, `--dispatch`, `--close` and the status writes copy
  their identity from the record, publish the new session, and leave the fact alone. §3's defence,
  "a stale value widens `mine` only", misses that the stale value also blocks S2's next write.
- **Impact:** an s1 to s2 holder push does not complete, so the record names s2, the claim s1 and
  `prior-session` s1. A tick's `--beat` (id 12) or a `--dispatch` (id 6) then matches `mine`
  through the fact, finds the session field differs, and lands the claim as s2. Unit 1's Renewal
  makes that write due. The fact stays s1, and holder `--resume` calls that follow find the claim
  `mine` with a fresh beat, so no holder renewal clears it. A later s2 to s3 holder push also does
  not complete: S2 keeps s1, and the record moves to s3. On the next s3 call the claim's s2 is
  neither `mine` (record s3, prior s1) nor same session (environment s3). It reads as foreign live,
  the holder column answers check 90, and the live run is forced to `--abort --code claim-lost`.
  That is finding 9's consequence, which this unit exists to close, on a narrow path: two incomplete
  pushes with a landed non-holder write between them. AC2 has no such sequence.
- **Fix — the skeptics judged both finders' fixes UNSOUND; their corrected fixes, merged:** keep
  §3's non-goal, so no writer outside the holder row ever touches the fact. Make `prior-session` a
  SET of sessions, written as one space-separated fact. On every holder-row outcome other than
  landed or lost, add the record's pre-call session to it, plus the session field of the claim this
  call read when the read succeeded, and never remove a member. In the holder and status-write
  columns, `mine` accepts a claim whose keepalive equals the record's and whose session is any
  member. The next holder-row claim write that lands clears the fact. Add AC2 steps and arms for
  four sequences, each followed by an s3 call that must print no check 90: (a) an incomplete s1 to
  s2 push, a `--beat` that lands, then an incomplete s2 to s3 push; (b) the same with a `--dispatch`
  as the writer that lands; (c) the sequence of (a) with the remote unreachable on the s2 to s3
  call; and (d) two unreachable pushes, s1 to s2 and s2 to s3, with nothing landing between them.
- **Why the rejected fixes were rejected, so the promotion spec does not reach for them:** clearing
  the fact on every landed claim write, whatever its writer, would make the out-of-process tick's
  `--beat` write the session's run-state file, which unit 1 S10 defines as writing nothing local,
  and would race the session's own `set_fact` writes in `write_lease`. It would also clear the fact
  after `--hold`, `--landed` and `--abort` have already staged or pushed the record. Overwriting the
  fact with the read claim's session alone loses the unreadable-claim case that sequence (d) drives.
- **Left-shift gate:** the four sequences, kept as arms in `tools/unattended/unattended.test.sh`,
  each observed RED under S2's absent-only rule as unit 20 now states it. Add a §10 checklist entry:
  "a fact that one writer keeps sticky names every other writer of the thing it tracks, and an AC
  interleaves them."

## H2 · id=2 — no criterion drives two incomplete holder calls in a row, so a build that writes the fact unconditionally passes

- **Address:** TOOL-aGraftedHelix-20 §2 S2 (the "written only while it reads `absent` or is
  missing" clause); §6 AC2.
- **Defect:** S2 makes that clause the thing that keeps `prior-session` equal to the session the
  published claim still carries, and says "Observed by AC2". AC2 runs one failing call and then one
  that lands, and its renamed-bare variant has the same shape. No criterion drives two incomplete
  calls in a row.
- **Impact:** a build that always writes the record's pre-call session passes AC2. The holder row's
  `write_lease` is due on a changed pid as well as a changed session (`unattended.sh:6597`). So an
  s1 to s2 call goes offline, then the process restarts under s2 while still offline, and that build
  writes `prior-session` s2 while the claim still names s1. The next call reads the claim as
  foreign, check 90 fires, and the run is forced to claim-lost. The path is narrow but more common
  than a second session change.
- **Fix — the skeptic judged it SOUND:** add an AC2 leg. After the first exit-124 s2 call, a call
  with `CLAUDE_CODE_SESSION_ID=s3` under the same shim exits 0 and leaves `session: s3` and
  `prior-session: s1`. A following s3 call with no shim prints no `UNATTENDED check 90 FAILED` and
  leaves a claim naming `session: s3` with the fact cleared. Red when: the second incomplete call
  rewrites the fact to s2.
- **Adjudication note:** under H1's corrected fix the fact is a set, and the second incomplete call
  ADDS s2 rather than keeping s1 alone. Read the leg's `prior-session: s1` there as "s1 is a
  member", and its red as "s1 is no longer a member". The pid-restart variant in the impact above
  is the stronger stimulus, because it keeps the session constant, so the promotion spec should
  carry it as a second leg.
- **Left-shift gate:** the leg and its pid-restart variant as arms in
  `tools/unattended/unattended.test.sh`, observed RED with the fact written unconditionally.

## H3 · id=7 — S2 can store the literal session `absent`, and S3 reads `absent` as no fact

- **Address:** TOOL-aGraftedHelix-20 §2 S2, against §2 S3.
- **Defect:** `write_lease` writes the literal `absent` when `CLAUDE_CODE_SESSION_ID` is unset
  (`tools/unattended/unattended.sh:5563`), and unit 1 §4 compares `absent` literally. S2 copies the
  record's pre-call session into `prior-session`, so it can store `absent`. S3 treats a fact reading
  `absent` as the cleared state and turns the widening off. The stored value cannot be told apart
  from no fact.
- **Impact:** a run leased under a harness that exposes no session id is resumed by its holder under
  s2, and the claim push does not complete. The record names s2, the claim `absent`, and the fact
  `absent`. On the next s2 call the widening is off, and same session fails because the claim's
  `absent` does not equal s2. The claim reads as foreign live, the call answers check 90, and the
  live run is declared claim-lost.
- **Fix — the skeptic judged it SOUND:** clear the fact by removing its line, so a missing line
  means no fact, or by a sentinel outside the session value space. S3 then accepts any present
  member, compared literally, as unit 1 already compares two `absent` sessions. `fact`
  (`unattended.sh:1117`) prints nothing for a missing line, so the two states are distinguishable.
  Add the absent-to-s2 variant to AC2, and reword AC2's `prior-session: absent`, AC3 and the
  migration line to match.
- **Adjudication note:** under this fix "the fact reads a value other than absent" becomes "the
  fact's line is present". M6's corrected fix should be read that way.
- **Left-shift gate:** the absent-to-s2 arm in `tools/unattended/unattended.test.sh`, observed RED
  with S3 ignoring a fact that reads `absent`. Add a §10 checklist entry: "a cleared state is not
  spelled as a value the field can legitimately hold."

## H4 · id=1 — S3 widens `mine` on two columns, but AC2 drives only `--resume`

- **Address:** TOOL-aGraftedHelix-20 §2 S3; §6 AC2.
- **Defect:** S3 widens `mine` on the holder AND status-write columns and says "Observed by AC2".
  AC2 drives two `--resume` calls, and every S5 arm is a `--resume` s2 call. Unit 1's call-site
  table puts `--dispatch`, `--close` and `--beat` on the holder column, and the LANDING re-bind,
  `--hold`, `--landed` and `--abort` on the status-write column. No spec pins whether
  `check_claim_writable` reads the record itself or is handed the facts by its caller.
- **Impact:** a build that supplies the fact only from the `--resume` row passes AC1 to AC5. After
  an incomplete s2 push, the next `--dispatch`, the run's most common next call, reads claim s1
  against record s2 as foreign, answers check 90, and forces `--abort --code claim-lost`. On the
  same build, `--hold` and `--abort` announce instead of writing, so the published claim keeps a
  stale status.
- **Fix — the skeptic judged it SOUND:** extend AC2. After the incomplete first s2 call, a
  `--dispatch` with no shim prints no `UNATTENDED check 90 FAILED` and leaves a claim naming
  `session: s2`. In a second fixture copy, after the same incomplete call, `--hold` with no shim
  prints no announce line and leaves a claim whose status reads held. Red when: the widening is
  confined to the `--resume` row.
- **Left-shift gate:** both legs as arms in `tools/unattended/unattended.test.sh`, observed RED with
  the widening confined to the `--resume` row, plus the `Observed by` lint named in the class table.

# MEDIUM

## M1 · id=3 — no criterion separates S1's path-field comparison from a whole-line one

- **Address:** TOOL-aGraftedHelix-21 §2 S1 ("a recorded path whose status letters moved during the
  render is still recognised"); §6 AC1 and AC2.
- **Defect:** AC1 checks only that the two listing commands match. In AC2 every foreign path, unit
  16's ` M` and `??` files and `foreign/sub/brief.md`, prints the same line at step 1 and step 5,
  so a whole-line membership test excludes them too and passes. The S4 arms use the same fixture.
- **Impact:** a whole-line build ships. When a foreign path's status letters move between step 1
  and step 5, for example another writer deletes a recorded ` M` file so it becomes ` D`, the loop
  does not recognise it and runs `git add -- <file>`. The spec commit then carries the deletion of
  foreign work.
- **Grade:** the finder graded this high and the skeptic medium, which binds. The harmful case
  needs a concurrent writer during a render that takes seconds, and the commit lands on a branch.
  This report agrees with medium.
- **Fix — the skeptic judged it SOUND:** add an AC2 leg. In the extracted block, insert a line
  between step 4 and step 5 that deletes unit 16's foreign tracked modified file, so its status
  moves from ` M` to ` D`. Assert that the block exits 0 and `git ls-tree -r --name-only HEAD` still
  names that file. Staged break: a membership test comparing whole lines, which puts the deletion in
  HEAD.
- **Left-shift gate:** the leg as an arm in `tools/workflows/unattended-build.test.sh`, observed RED
  under the whole-line test.

## M2 · id=4 — S2 says AC1 observes the standing arm, but AC1 never reads the suite and a pin satisfies the gate

- **Address:** TOOL-aGraftedHelix-22 §2 S2; §6 AC1.
- **Defect:** S2 says the standing arm is "Observed by AC1". AC1 runs a scratch driver copy and
  never reads `tools/unattended/unattended.test.sh`. `tools/memory-tree/check-arms.py` accepts a pin
  row in `unarmed-branches.txt` for any unarmed branch, and enforces shrink-only only as "an armed
  branch must not stay pinned". No tool parses §7's `New arm:` line.
- **Impact:** a build that implements S1 and pins its new fail branch instead of writing the arm
  passes AC1, AC2 and every listed gate. The read-axis refusal then has no keeper, and a later
  change that breaks the membership test while leaving the `fail <n>` call site stays green.
- **Grade:** the finder graded this high and the skeptic medium, which binds. A pinned row reports
  as PINNED in `--report` rather than hiding, and the prior round confirmed the same shape on unit 17
  at medium. This report agrees with medium.
- **Fix — the skeptic judged it SOUND:** either label S2 NOT OBSERVED, as unit 20 S5 and unit 21 S4
  do, or add a criterion: `python tools/memory-tree/check-arms.py --report` names S1's branch as
  armed by `tools/unattended/unattended.test.sh`, and no tracked `unarmed-branches.txt` row pins it.
  Red when: the branch is pinned rather than armed. This report prefers the criterion, because the
  standing arm is what unit 22's title promises.
- **Left-shift gate:** the criterion itself, plus the `Observed by` lint named in the class table.

## M3 · id=5 — AC3's red cannot reliably be observed, because the stamp has one-second resolution

- **Address:** TOOL-aGraftedHelix-20 §6 AC3, observing §2 S1's "computes the lease stamp ONCE".
- **Defect:** `write_lease` stamps `lease-utc` at one-second resolution (`unattended.sh:5569`), so
  two clock reads in one call usually produce byte-equal stamps. AC3's red, "stamps read from two
  clocks", depends on timing rather than on a staged break that must show. No S5 arm stages a
  two-clock break.
- **Impact:** a build whose claim CAS reads its own clock right after the shared stamp passes AC3
  almost always, because the two reads sit milliseconds apart. A build whose `write_lease` ignores
  the third argument reds often but not deterministically; the skeptic measured a claim-style push
  at 287 ms on node `a`. The escaped effect is a claim and record `lease-utc` skew on some calls,
  which costs one immediate renewal push and a published stamp the record never held.
- **Fix — the skeptic judged the finder's fix UNSOUND; the skeptic's corrected fix:** run AC3 with a
  `date` shim on PATH that forwards every invocation to the real `date` unchanged, except a request
  for the `+%Y-%m-%dT%H:%M:%SZ` stamp. It answers that request with the real time advanced by one
  more second per such request, counted in a file under the fixture. Assert that the claim's
  `lease-utc` equals the record's byte for byte. Red when: they differ, which every two-read build
  then produces deterministically.
- **Why the rejected fix was rejected:** a shim that returns a distinct stamp on every invocation
  also answers `read_claims`' epoch conversion and the current-time read, so the seeded claim's age
  reads unknown and the AC3 call itself refuses with check 90. Counting invocations miscounts,
  because a correct call legitimately runs `date` several times.
- **Left-shift gate:** the shimmed AC3 as an arm, observed RED with the claim CAS reading its own
  clock. Add a §10 checklist entry: "an equality between two timestamps is observed under a clock
  that makes the inequality deterministic."

## M4 · id=8 — the 124 arm's staged break cannot red it

- **Address:** TOOL-aGraftedHelix-20 §7 New arm 1 (claim push exits 124) and §5 testing, against §4
  "What each outcome leaves".
- **Defect:** §7's first arm and §5 stage the incomplete-push break as "the CAS moved back after
  `write_lease`". S2 takes the fact from the record's session as it stood before the call, so §4's
  third row is the same in either order: record s2, claim s1, fact s1. The second call passes
  through S3 either way. §7's second arm stages "prior-session left unwritten" for the same outcome
  class, which contradicts §5's claim that both incomplete-push arms use the order break.
- **Impact:** the 124 arm has no staged break that reds it, so its failing case cannot be observed
  as §7 and the charter require. The builder finds the dead break loudly at VERIFYING, so the effect
  is contained.
- **Fix — the skeptic judged it SOUND:** stage the 124 arm with the fact left unwritten, or with S3's
  widening removed, since that is what its second call depends on. Make §5 say that the
  CAS-moved-back break belongs to the lost-race arm only.
- **Left-shift gate:** the staged break observed RED at VERIFYING, which the charter already
  requires. Add a §10 checklist entry: "a staged break changes the state the arm's assertion reads;
  a break whose outcome row is unchanged cannot red."

## M5 · id=9 — unit 21 plants a third foreign path but leaves unit 16's exactly-two assertion standing

- **Address:** TOOL-aGraftedHelix-21 §2 S4 and §4 "The arm's foreign paths", against unit 16 §4
  "The arm".
- **Defect:** unit 16's table asserts that `git status --porcelain` lists exactly the two foreign
  paths, unchanged. Unit 21 plants `foreign/sub/brief.md` and keeps unit 16's assertions for the
  other two paths, but never amends that row. Plain porcelain collapses the untracked directory to
  `?? foreign/`, a third line.
- **Impact:** a correct build reds the extended arm on unit 16's exactly-two assertion. The builder
  must then rewrite another unit's assertion with no spec to say how.
- **Fix — the skeptic judged it SOUND:** have S4 and the §4 table supersede unit 16's row by name:
  `git status --porcelain --untracked-files=all` lists exactly the three foreign paths, unchanged.
- **Left-shift gate:** a §10 checklist entry: "a unit that changes a fixture another unit asserts
  over supersedes that assertion by name."

## M6 · id=13 — neither S2 nor "The order" says the fact write is staged

- **Address:** TOOL-aGraftedHelix-20 §2 S2; §4 "The order" (the `prior-session` row).
- **Defect:** the holder row's only `stage_or_fail` sits inside the `write_lease`-due branch
  (`unattended.sh:6596-6600`), and that branch does not run on the call that clears the fact. The
  spec does not say the fact write or its clearing is staged, and does not limit clearing to a fact
  that is present. The row's existing contract is that a call with nothing to record writes
  nothing, which suite arms pin at `tools/unattended/unattended.test.sh:7811-7813` and near line 8412.
- **Impact:** a builder who appends the fact write after the existing pair leaves it unstaged, and
  the clearing write on AC2's second call is unstaged too. `check_clean` (`unattended.sh:1975`)
  counts the unstaged record, so `--hold` and `--preflight` refuse the run with check 2. If instead
  the fact is cleared on every landed holder-row write, a record that never carried it gains a line
  on a plain renewal and breaks the writes-nothing contract. AC2 and AC3 never look at the index.
- **Fix — the skeptic judged it SOUND:** in S2 and "The order", state that the fact write runs
  before the row's `stage_or_fail`. State that the clearing write runs only when the fact reads a
  value other than absent, and then runs `stage_or_fail` itself. In AC2, assert that
  `git diff --name-only` names no run-state file after each call. In AC3, assert that a renewal call
  on a record without the fact leaves `git status --porcelain` empty.
- **Adjudication note:** if H3's fix is taken, "reads a value other than absent" becomes "the
  fact's line is present".
- **Left-shift gate:** the two index assertions, kept as arms. Add a §10 checklist entry: "a new
  write on a row that has a writes-nothing contract states its staging and the condition it runs
  under."

## M7 · id=14 — the run's own same-session restart reads the claim an incomplete push left as foreign

- **Address:** TOOL-aGraftedHelix-20 §2 S3; §3 "The take sites".
- **Defect:** S3 leaves the take-over comparison unchanged, which assumes no take-over site meets the
  claim an incomplete holder write leaves. The restart branch in `tools/unattended/unattended.sh`,
  after the `--replaces` block, sends the recorded session's own relaunch under a new keepalive
  through `run_takeover`. There `mine` compares with the values the call is about to record.
- **Impact:** after §4's third row (record s2, claim k1 and s1), a crash and a relaunch of s2 under
  k2 read the claim as not `mine` and not same session. Its beat is fresh, so it is foreign live,
  and the take-over column answers check 89. The tick beats only on a LIVE verdict, so nothing
  repairs the claim. The refusal holds until the beat ages past `RESUME_STALE_BOUND`, and the take is
  then logged as a foreign stale take-over, unit 8's `claim-taken-over`, which misreports the event.
- **Fix — the skeptic judged the finder's fix UNSOUND; the skeptic's corrected fix:** widen the
  take-over column's same-session test only when `CLAUDE_CODE_SESSION_ID` equals the record's
  pre-call session, which is the restart row. In that case only, a claim whose keepalive equals the
  record's pre-call keepalive and whose session equals the record's `prior-session`, when that is
  present, reads as same session. Add an arm: an incomplete s1 to s2 holder push, then `CLAUDE_PID`
  changed and a new `--keepalive-id` under s2, which must take over with no check 89. Add a second
  arm: a session other than s2 reaching `run_takeover` over the same record and claim must still
  read the claim as foreign.
- **Adjudication note:** under H1's set encoding, "equals the record's `prior-session`" reads "is a
  member of it", and under H3's line removal "when that is present" means the line exists.
- **Left-shift gate:** the two arms in `tools/unattended/unattended.test.sh`, the first observed RED
  with the widening removed and the second with the session condition removed.

## M8 · id=10, id=15 — unit 21's guard runs after the specs are staged and the views rendered, so the re-run its refusal invites is refused too

- **Address:** TOOL-aGraftedHelix-21 §2 S3 and §4 "The loop", against §3 "The record as a file
  under the git directory" and unit 16 S6.
- **Defect:** S3 places the `${rec+x}` guard only before step 5's loop. In the split shape the arm
  models, with step 1's assignment gone, step 3 has staged the specs and step 4 has rendered
  `memory/LIVE.md`, the ledger shard, the build README and the siblings' records regions before the
  guard refuses. Unit 16 S6's step-2 input check refuses any unstaged path under the memory root
  other than the spec paths. §3 rejects a file-carried record because a later call could read a
  stale copy, yet this refusal leaves stale rendered views behind.
- **Impact:** after one split refusal, the agent follows the refusal text and re-runs the block as
  one invocation. Step 2 refuses it, naming the rendered views as dirty generator inputs, which reads
  as foreign work. The refusal text names only the record, and no spec names the cleanup. An
  unattended build stalls at the spec commit until someone restores the views and unstages the
  specs by hand. No wrong commit is possible.
- **Fix — the skeptics judged both finders' fixes UNSOUND; their corrected fixes, merged:** test
  `${rec+x}` twice, right after step 1 (before step 2, so before step 3's first `git add`) and before
  step 5's loop, and give each guard its own stimulus and staged break.
  (1) Step 1's assignment deleted: the block exits non-zero naming the record, with
  `git diff --cached --name-only` empty and `git status --porcelain --untracked-files=all` equal to
  its value before the run. Staged break: delete the early guard, so the late guard refuses only
  after staging and rendering, and those assertions red.
  (2) The block with `unset rec` inserted after step 4: it exits non-zero naming the record and the
  cleanup, with HEAD unmoved. The cleanup is to restore every unstaged path under the memory root
  other than the spec paths, then unstage the spec paths. Staged break: delete the late guard, which
  commits the foreign paths and moves HEAD. Assert that after the named cleanup the block, re-run as
  one invocation, exits 0.
  Amend AC2 and §7's staged break to match. Put the assertions in S4's second arm as well as AC2.
- **Why the rejected fixes were rejected:** adding the early guard alone, with AC2 and §7 left as
  they are, makes AC2's "the run with the guard deleted and step 1's line deleted moves HEAD" and §7's
  "stage the `${rec+x}` guard deleted" untrue for either guard alone, because the surviving guard
  still refuses. A builder who deletes one guard would observe no red on HEAD.
- **Left-shift gate:** the two stimuli as arms in `tools/workflows/unattended-build.test.sh`, each
  observed RED under its own staged break. Add a §10 checklist entry: "a guard on a state the block
  needs runs before the block's first side effect, and a refusal names the cleanup it leaves owed."

# LOW

## L1 · id=11 — unit 22 pins the literal `foreign-stale`, where unit 19 lets the constant take unit 1's build spelling

- **Address:** TOOL-aGraftedHelix-22 §2 S2 and §6 AC1, against unit 19 §4 "The constants".
- **Defect:** S2 and AC1 pin the removed member and the refusal's text as `foreign-stale`. Unit 19
  says that where unit 1's build already spelled a class as one word, `CLAIM_READS` takes that
  spelling. Unit 1 writes the class with a space and pins no code spelling, and unit 1 is not built
  at base `5266d22e`.
- **Impact:** if unit 1's build spells the class `foreign_stale` or `foreignstale`, AC1 reds a
  correct refusal, or pushes the builder to rename the member and break unit 19's rule that the
  function and the constant agree. The refusal behaves the same under any spelling.
- **Fix — the skeptic judged it SOUND:** phrase S2 and AC1 as "the `CLAIM_READS` member for a
  foreign stale claim, as unit 19 spells it", and assert the refusal names that member.
- **Left-shift gate:** a §10 checklist entry, the same one as M5's: "a spec that names another
  unit's spelling cites that unit's rule rather than restating its value."

## What a fold should do first

1. Unit 20, the holder row's `prior-session` fact. It carries nine of the fifteen confirmed findings
   and all four HIGHs. Fold M3, M4, M6 and M7 in one rev. Then promote H1 to H4 together: one
   promotion unit can close all four, because each redefines the same fact. It makes the fact a set
   with a missing line meaning no fact (H1, H3), drives two incomplete calls in a row including a
   pid restart (H2), and observes the widening at `--dispatch` and `--hold` (H4). Its sequence
   fixture should be the one M6's index assertions and M7's restart arms run over, rather than a
   second one.
2. Unit 21, the spec commit block's loop. Fold M1, M5 and M8 in one rev. All three extend the same
   extracted-block fixture: the ` M` to ` D` move, the three-path listing, and the two guards with
   their own stimuli.
3. Unit 22, the read-axis refusal. Fold M2 and L1 together, both in S2 and AC1.

H1 to H4 are promoted under the method rather than folded. A review of their promotion spec should
run with a checklist swept, an intent supplied, and the prior-art lens's priming tightened. None of
the last three rounds of this build had a checklist or an intent.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 2 S3 / section 6 AC2 | high | high | confirmed | Unit 20 S3 widens `mine` on the holder AND status-write columns and says 'Observed by AC2'. AC2 (lines 195-201) drives only two `--resume` calls, and the S5 arms are all `--resume` s2 calls. Unit 1's call-site table puts `--dispatch`, `--close` and `--beat` on the holder column and the LANDING re-bind, `--hold`, `--landed` and `--abort` on the status-write column. Unit 20's own non-goal 'Clearing the fact from other writers' confirms those sites write claims. Unit 1 S4 has check_claim_writable decide from 'the run's lease identity', and none of these specs pins whether it reads the record itself or is handed the facts by its caller. So a build that supplies prior-session only from the `--resume` row is possible, and it passes AC1 to AC5. The path then works as the finding says: claim s1 and record s2 after an incomplete push, then `--dispatch` under s2 is neither mine nor same session, so it reads as foreign live (or stale), which is check 90 on the holder column and a forced claim-lost abort. That is finding 9's consequence on a narrow path, so high. | sound |
| 2 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 2 S2 (the 'written only while it reads absent or is missing' clause) / section 6 AC2 | high | high | confirmed | S2 (lines 35-39) makes the 'written only while it reads absent or is missing' clause the thing that keeps prior-session equal to the session the published claim still carries, and it says 'Observed by AC2'. AC2 runs one failing call and then one that lands, and its renamed-bare variant has the same shape, so no criterion ever drives two incomplete calls in a row. A build that always writes the record's pre-call session passes. That build fails on a path that is more common than the finder's s3 example. Holder row write_lease is due on a changed pid as well as a changed session (unit 18 evidence, unattended.sh:6591-6600). So s1 to s2 offline, followed by a process restart under s2 while still offline, has that build write prior-session s2 while the claim still says s1. The next call then reads the claim as foreign, check 90 fires, and the run is forced to claim-lost. Same consequence on a narrow path, so high. | sound |
| 3 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-21.md:section 2 S1 (path-field comparison, 'a recorded path whose status letters moved during the render is still recognised') / section 6 AC1, AC2 | high | medium | confirmed | S1 (lines 28-33) promises a path-field comparison under which 'a recorded path whose status letters moved during the render is still recognised', and says 'Observed by AC1 and AC2'. AC1 only compares the two listing commands. In AC2 every foreign path (unit 16's ` M` and `??` files and foreign/sub/brief.md) prints the same line at step 1 and step 5, so a whole-line membership test excludes them too and passes. The S4 arms use the same fixture. Within the block's own steps, a path-field versus whole-line difference only touches paths the block stages anyway: the spec paths, and views that step 2's input check holds clean. The harmful case therefore needs a foreign path's letters to change during a render that takes seconds, which means a concurrent writer, and the commit lands on a branch. That is a real but contained defect, so medium rather than high. This matches the prior round's grading of the unobserved inverted filter. | sound |
| 4 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-22.md:section 2 S2 / section 6 AC1 | high | medium | confirmed | S2 (lines 30-38) says the standing arm is 'Observed by AC1'. AC1 (lines 109-116) runs a scratch driver copy and never reads tools/unattended/unattended.test.sh. check-arms.py cmd_check accepts a pin for any unarmed branch, and no mechanism refuses a new sidecar row: 'shrink-only' is enforced only as 'an armed branch must not stay pinned'. No tool parses section 7's 'New arm:' line either. So a build that pins S1's branch passes AC1, AC2 and every listed gate. The sibling convention labels suite arms NOT OBSERVED (unit 18 S3, unit 20 S5, unit 21 S4). The prior round confirmed the identical shape, unit 17 S1 'Observed by AC1' with AC1 never running the arm, at medium, and unit 17 rev-2 relabelled it. The effect is contained: a pinned row reports as PINNED in --report rather than misleading. So medium. | sound |
| 5 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 6 AC3 (observing section 2 S1's 'computes the lease stamp ONCE') | medium | medium | confirmed | AC3's red depends on timing, not on a staged break that must show. write_lease stamps at one-second resolution (unattended.sh:5569). The finder's 'almost always byte-equal' overstates one case. When write_lease ignores the third argument, its own clock read comes after the claim push and after five set_fact calls plus read_host_name and read_pid_image. Measured on node a, a local claim-style push alone took 287 ms, so that break reds often but not deterministically. When the claim CAS reads its own clock right after the shared stamp, the two reads sit milliseconds apart and AC3 stays green almost always. No S5 arm stages a two-clock break. So the single-stamp property can ship unverified. The escaped effect is a claim/record lease-utc skew on some calls, which costs one immediate renewal push and a published stamp the record never held. That is contained, so medium. The proposed fix is unsound as written, for two reasons. First, a shim that returns a distinct stamp on EVERY invocation also answers read_claims' single `date -u -f - +%s` epoch conversion (unit 1 section 4 'Reading') and the current-time read. The seeded s1 claim's age then reads unknown, so the holder column refuses the AC3 call itself with check 90. Second, the alternative of asserting 'exactly one per call' miscounts, because a correct call legitimately invokes date several times: for the age conversion, for the claim's beat-utc and for the stamp. | unsound |
| 6 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 2 S2 against section 3 "Clearing the fact from other writers" | high | high | confirmed | I traced the scenario against unit 20 S2, S3 and section 3, and against unit 1's holder column and Renewal. After an incomplete s1->s2 holder push, the record names s2, the claim s1 and prior-session s1. --dispatch, --close and --beat are holder-column writers, and S3 widens mine for them, so their claim matches mine through prior-session s1. The session field differs, so unit 1's Renewal makes a write due, and the write lands s2. Section 3 then leaves prior-session at s1. On an s2->s3 holder call, mine passes on the direct match (claim s2, record s2). If that CAS does not complete, S2 may write only while the fact reads absent, so it keeps s1, and write_lease records s3. The next s3 call finds claim s2 against record s3, prior-session s1 and environment s3. That claim is neither mine nor same session, so it is foreign live, and the holder column answers check 90. Section 3's 'a stale value widens mine only' misses that the stale value also blocks the S2 write. The path is narrow: it needs two incomplete pushes with a landing between them. The consequence is still finding 9's: a live run forced to --abort --code claim-lost. The proposed fix is unsound. 'Every claim write that lands, whatever its writer' includes --beat, which the out-of-process resume tick runs in the run's worktree. Unit 1 S10 defines --beat as printing one beat line and writing nothing local. Under the fix, the tick would write the session's run-state file, racing the session's own set_fact read-modify-writes in write_lease. The fix also includes the --hold, --landed and --abort status writes, whose claim write comes after their stage_or_fail. Clearing the fact there would leave the record's working copy different from what was just staged, or from what was pushed for --landed. | unsound |
| 7 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 2 S2 against section 2 S3 | high | high | confirmed | write_lease at base writes the literal `absent` when CLAUDE_CODE_SESSION_ID is unset (tools/unattended/unattended.sh:5563, set_fact ... session "${sid:-absent}"). Unit 1 section 4 compares `absent` literally, so a record and a claim that both name session absent read as mine. On a holder call under s2, write_lease is due. If its CAS does not complete, S2 copies the pre-call session `absent` into prior-session; the absent-only rule allows that write. S3 ignores a prior-session that reads absent. The next s2 call then reads claim absent against record s2. The widened test is off, and same session fails because the claim's `absent` does not equal s2. The claim is foreign live, so the call answers check 90, and the live run is declared claim-lost. This happens only on a narrow path: a run leased under a harness exposing no session id, resumed under one that does, with the push incomplete. The fix is sound. `fact` (unattended.sh:1117) prints nothing for a missing line, so a missing line is distinguishable from the literal `absent`. Accepting a literal `absent` member is the same widening unit 1 already grants two absent sessions. Applying the fix also means rewording AC2's 'prior-session: absent', AC3 and the migration line. | sound |
| 8 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 7 New arm 1 (claim push exits 124) and section 5 testing, against section 4 "What each outcome leaves" | medium | medium | confirmed | S2 takes prior-session from the record's session as it stood before the call, so moving the CAS after write_lease does not change the third row of section 4. The CAS still pushes the values write_lease records, under the same stamp, and it still does not complete. The record names s2, the claim s1 and prior-session s1 in either order, and the second call passes through S3. The 124 arm's staged break in section 7 therefore cannot red it. Section 7's second arm stages 'prior-session left unwritten', which contradicts section 5's 'the incomplete-push arms with the CAS moved back after write_lease'. The arm still checks something real, since it reds if prior-session is not written. The builder finds the dead break loudly at VERIFYING, so the effect is contained. The fix is sound: the CAS-moved-back break is equivalent to section 7's third arm ('write_lease run before the CAS'), whose AC1 does red. | sound |
| 9 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-21.md:section 2 S4 and section 4 "The arm's foreign paths", against unit 16 section 4 "The arm" | medium | medium | confirmed | Unit 16 section 4 'The arm' asserts that `git status --porcelain` lists exactly the two foreign paths, unchanged. Unit 21's S4 and its section 4 table plant foreign/sub/brief.md and keep 'unit 16's' assertions for the first two paths. They never amend that row. Plain porcelain collapses a wholly untracked directory to `?? foreign/`, which is unit 21's own evidence, so the listing has three lines. A correct build reds unit 16's exactly-two assertion. Nothing ships wrong, because the arm reds loudly. The builder still has to rewrite another unit's assertion with no spec to say how. The fix is sound. With --untracked-files=all, the listing is the modified tracked file, the root untracked file and foreign/sub/brief.md. The spec and the README are committed clean, and -B with no .gitignore leaves no cache. | sound |
| 10 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-21.md:section 2 S3 against section 3 "The record as a file under the git directory" and unit 16 S6 | medium | medium | confirmed | Unit 21 S3 and its section 4 put the ${rec+x} guard before step 5's loop. In the split shape the arm models, with step 1's assignment gone, steps 2 to 4 run first. Step 3 stages the specs, step 4 rewrites memory/LIVE.md and the build README regions, and step 5's first half re-adds the specs before the guard refuses. Every later run of the block then fails unit 16 S6's step-2 check: `git diff --name-only` over the memory root names those rendered views outside the spec paths. That check refuses a correct single invocation too, and its message names the views, not the lost record. The tree is left in the stale state section 3 cites against a file-carried record. No commit goes wrong, so the effect is a contained stall. The proposed fix cures the arm's split shape, but it introduces a stale staged break. With two guards, AC2's 'the run with the guard deleted and step 1's line deleted moves HEAD' and section 7's 'stage the ${rec+x} guard deleted' are no longer true for either guard alone: the surviving guard still refuses, so a builder who deletes one guard observes no red on HEAD. | unsound |
| 11 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-22.md:section 2 S2 and section 6 AC1, against unit 19 section 4 "The constants" | low | low | confirmed | Unit 19 section 4 'The constants' says that where unit 1's build already spelled a class as one word, CLAIM_READS takes that spelling. Unit 1 section 4 writes the class as foreign `stale` with a space and pins no code spelling, and unit 1 is not built at base 5266d22e (no check_claim_writable in tools/). So foreign_stale or foreignstale is a legal outcome. Unit 22 S2 and AC1 nonetheless pin the literal `foreign-stale`, so AC1's text could fail a correct refusal or push the builder to rename the member. The effect is limited to the wording of the criterion and the arm. The refusal behaves the same under any spelling, so this is low. | sound |
| 12 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 2 S2, with section 3 'Clearing the fact from other writers' | high | high | confirmed | Unit 20 S2 makes prior-session sticky ('written only while it reads absent or is missing'). It is cleared only by a landed holder-row write. Section 3 says --beat, --dispatch, --close and the status writes copy their identity from the record, publish s2, and leave the fact alone. S3 widens mine for every holder-mode comparison, and that includes --beat, which unit 1 has write through the mine row. Unit 1 'Renewal' makes a write due when a field differs. So after an incomplete s1->s2 push, a tick's --beat lands the claim as s2 and prior-session stays s1. Holder --resume calls that follow find the claim mine with a fresh beat, so no holder renewal is due and the fact can stay s1 indefinitely. A later incomplete s2->s3 push keeps s1 and leaves the claim at s2. On the next s3 call the claim is neither mine (record s3, prior s1) nor same session (s2 vs s3). It is a fresh foreign live claim, and the holder column answers check 90, which forces claim-lost on a live run. That is the outcome unit 1's hands-off says this unit exists to prevent. The path needs two incomplete pushes with a landed non-holder write between them, so it is narrow, which makes this high. | unsound |
| 13 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 2 S2, and section 4 'The order' (prior-session row) | medium | medium | confirmed | At base, the holder row's only stage_or_fail sits inside the write_lease-due branch (unattended.sh:6596-6599). The comment on that row says it 'writes NOTHING' otherwise, and test arms pin this at unattended.test.sh:7811-7813 (a porcelain-empty check after a matching-id resume) and at the AC11 block near 8410. Unit 20's 'The order' puts the prior-session step after the write_lease row, and neither S2 nor the table mentions staging. On AC2's second call (session s2, pid unchanged) write_lease is not due, yet S2 clears the fact there, so the record is written on a path with no stage_or_fail. check_clean (unattended.sh:1975) counts unstaged and staged paths, and --hold and --preflight call it with no exemption, so an unstaged record refuses with check 2. AC2 and AC3 never look at the index, so a build missing the stage passes every criterion. The effect is a refused later verb rather than a wrong record, so this is medium. | sound |
| 14 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 2 S3, and section 3 'The take sites' | medium | medium | confirmed | The restart branch at base (unattended.sh, after the --replaces block) sends the recorded session's relaunch under a new keepalive through run_takeover. Unit 20 S3 leaves the take-over comparison unchanged: there, mine compares with the values the call is about to record, (k2, s2). Section 3 'The take sites' covers only the CAS order. After the third outcome row (record s2, claim k1/s1), a crash and relaunch of s2 under k2 reads the claim as not mine and not same session (s1 vs s2). Its beat is fresh, so it is foreign live, which unit 1's take-over column answers with check 89. The tick beats only on a LIVE verdict, so nothing repairs the claim after the crash. The refusal holds until the beat ages past RESUME_STALE_BOUND, and the take is then logged as a foreign stale take-over (unit 8's claim-taken-over). The effect is a delay of up to the bound plus a misleading event, so this is medium. | unsound |
| 15 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-21.md:section 2 S3, and section 4 'The loop' | medium | medium | confirmed | Unit 21 S3 places the ${rec+x} guard only before step 5's loop, so a split invocation reaches it after unit 16's step 3 has staged the specs and step 4 has rendered memory/LIVE.md, the ledger shard, the build README and the siblings' records regions. Unit 16 S6's step-2 input check refuses any unstaged path under the memory root other than the spec paths. A block re-run as one invocation, which is what unit 21's own refusal text ('must run as one invocation') invites, is therefore refused and names the generated views as dirty inputs. Neither unit 21 nor unit 16 names the cleanup. Unit 15's step 5 ('do not retry around it') and its remedy limit the damage: no wrong commit is possible, and the result is a stuck, misdirected stage. That is a contained defect, so medium. | unsound |
| 16 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-22.md:section 2 S2, and section 6 AC1 | low | - | refuted | The facts hold, but they do not make the spec wrong. The driver refuses at unattended.sh:78-82 unless the library sits beside it. ROOT comes from the cwd at :463. check_clean (:1975) counts untracked files through scan_dirty_paths. The suite's $TMP is the fixture repo (unattended.test.sh:129, :195). Unit 22 never says to put the copy inside the fixture tree. Where a test helper file goes is a builder's setup choice, and the spec's design (S1's check, its place before any claim write, the removed-member stimulus) does not change with it. The suite already has the outside-the-tree pattern this needs: the L2 arm at unattended.test.sh:6194 copies the driver into its own mktemp -d. A copy put in the tree is refused by fail 2, whose own text says the tree is dirty and gives a path count, so the builder sees the cause on the first run. Nothing wrong ships. Low, and it asks only for a setup detail. | sound |
| 17 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 3 'Supersessions this unit records', against section 2 S4 and S7 | medium | - | refuted | dDerivedDocket-61 does not own the lease-fact count, so no supersession of it is owed. Its own section 3 (spec lines 160-162) makes 'The lease-fact SET and write_lease's contract' a non-goal: 'this unit changes who reads them'. Its 'Those facts are six' (line 261) is scoped to 'in this spec'. The owner ruling at DECISIONS.md:123 rules on one lease record, the retired lease file, the single bound and the HELD carve-out, not on the count. The contract that ruling names, STOPS section 7, is the very file unit 20 S7 rewrites in the same commit. The cited comments (lib-unattended.sh:1167-1171, unattended.sh:1227, :1970, :4425) are also edited by S7 to name prior-session, so the next reader sees seven names at the code. S4 also has a real reason. verb_resume sends a recorded LANDING that does not yet derive LANDED to the holder row (unattended.sh:6506-6560 at base), and S2 writes prior-session in the same call as write_lease's six. So a working-copy difference the six-line tolerance already admits can carry that line too. A supersession bullet would be a tidier record, but its absence leaves nothing in the spec wrong. | sound |
| 18 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 2 S2 and S7; section 4 Evidence (the S7 predicate) and Files touched; section 5 migration; section 6 AC3 | medium | - | refuted | Several of the finding's facts are true: S7's carrier list and its predicate miss PROTOCOL.template.md section 2 and SESSION-KICKOFF.md:90. Its claimed consequences do not follow, though. (1) Protocol fact 14 defines the LEASE as 'what an out-of-session actor binds to' (template:226-227 at base), and SESSION-KICKOFF:90 lists what the stop-guard, the stall-recorder and the tick read. No out-of-session actor reads prior-session. Only the driver's claim mine test and check_lease_only_diff read it. So both carriers stay accurate without it, and the protocol's lease is unchanged. (2) The 'always WRITTEN' rule (template:236) names facts 14 to 16 by number. The protocol also keeps facts that are absent until their condition is reached (facts 10 to 12, and 13 under a branch), so a conditionally written fact is an established shape. (3) The authored-facts list says outright that it is incomplete: 'the list below omits mode and the two keys --attest writes. The set is the driver's set_fact keys plus those; count it there' (template:167-169). A new set_fact key is therefore inside the protocol's stated set by construction. No sibling unit in this build amends the protocol either; unit 1 adds claims through the stops guide alone. What remains is a naming preference about the word 'lease'. The fix is unsound for two reasons. Numbering prior-session beside facts 14 to 16, and adding it to SESSION-KICKOFF:90, would say that out-of-session actors bind to it, which is false. And option (a) writes it only on holder-row calls, so records written by --preflight or a take-over would still lack the line, and the always-written property the fix promises would not hold. | unsound |
| 19 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-20.md:section 4 Evidence, the `check_lease_only_diff` bullet; section 5 security | low | - | refuted | Section 4 Evidence says read_landing_commit 'relies on' the predicate. It does not claim to be the only caller, so the statement is true. The design is the same for both callers: S4 widens the one shared predicate, and a predicate keyed on lease-fact lines should admit whatever line the holder row writes in the same call as write_lease. The --landed primary clean check (unattended.sh:1975 and :4425 at base) also gets the widening, and it needs it, because a primary landing on the default branch can carry a holder-row write. The exemption's real risk is dDerivedDocket-61's: a hand-edited witness or phase reaching the terminal write. That risk is untouched, because the predicate still refuses every non-lease line. A prior-session line only widens the mine test, and only for a claim under this run's own keepalive, which a terminal record never uses again. Built as written, nothing behaves differently from what the fuller Evidence would have produced. The finding asks for more prose, and the finder graded it low. | sound |
| 20 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-21.md:section 3 'A NUL-delimited listing'; section 4 Evidence (the TOOL-dMendedRecall-2 bullet) | low | - | refuted | The precedent is as the finder describes it: dMendedRecall-2's build (9cba3c3f8) NUL-reads two plumbing listings into an array with --no-renames. Unit 21's reason is still true for the design it chose, a scalar record assigned through command substitution, which does drop NUL bytes. Section 3 states the cost of that choice accurately. Both listings C-quote identically, so foreign paths still match and are never staged. A quoted path the loop must stage makes git add refuse under set -e, which gives a loud committed: false and never a wrong commit. The generator's outputs carry no such byte. The precedent's 'name nothing to add' concern was a silent miss inside a driver function. Here the block stops on the error, which is a different failure mode. Choosing porcelain over the NUL array is a design alternative that the non-goal explicitly sets aside, and as written it ships no wrong result. The fix is unsound because it offers option (a), adopting the NUL array, without carrying that change through the spec. S3's ${rec+x} guard, applied to an associative array, tests element 0. A recorded array, empty or full, would then read as unset and refuse every run, including the clean tree S3 must let through. S1, AC1 and AC2 also assert two identical porcelain listings, which would no longer exist. | unsound |
| 21 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-22.md:section 10 Reuse audit; section 2 S1 (the refusal message) | low | - | refuted | The prior art is real: AUTH_MODES, is_auth_mode and fail 44 sit at unattended.sh:835/882/2407-2408 with the derive-the-legal-values rationale at :2404-2406, and the aScouredKit-7 deletion note is at :872-881. But the impact the finding claims does not follow from the spec. S1 already pins the message to name the class AND `CLAIM_READS`, and AC1 asserts that the refusal line names `foreign-stale` and `CLAIM_READS`. A builder who writes only an expanded `$CLAIM_READS` is departing from S1's explicit text, and AC1 reds them, so there is no ambiguity between S1 and AC1 to resolve. The 'sibling refusal' that actually shares this function is unit 19's mode refusal, whose S2 pins the same form (the mode and `CLAIM_MODES`), so unit 22 matches its true sibling. A message that names the constant cannot drift the way fail 44's old enumerated text did, which was the precedent's rationale. Section 10's 'no record of a refusal outside a declared constant' is scoped to what the recall probe returned. I re-ran that probe, and the index has since been rebuilt with unit 22 itself in it, so what it returned at authoring time cannot be established. What remains is a missing citation in a reuse-audit record, with no effect on what gets built. That is a documentation preference, and the finder graded it low. | sound |
| 22 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-22.md:section 2 S2 (the scratch-copy edits); section 7 New arm | low | - | refuted | `mutate` exists at unattended.test.sh:184-190 and prints `FAIL fixture no-op`. The finder concedes that a stale anchor cannot produce a false green: the arm still reds, because the claim is taken and the ref moves. The staged break is a one-time build-time observation that AC1 makes directly, and it is not standing suite code. A no-op there fails AC1's 'that sha moves' half rather than passing anything. So the spec as written certifies nothing it does not check. The claimed consequence is only how clearly a future red is diagnosed. How a fixture edit is mechanised is a build-level convention, not a design defect. The suite's existing scratch-driver-copy arms (S6's red fixture at :3033-3049, and :2485) use `sed ... "$SCRIPT" > copy` with their own non-vacuity check rather than `mutate`. Unit 19's sibling arm specifies no mutate either. The spec is neither unbuildable nor wrong without this, and the finding is an implementation preference graded low. | sound |
