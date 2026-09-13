**Serves:** spec-audit TOOL-aBatchedArm-3

# Tier-2 spec audit — TOOL-aBatchedArm-3, ROUND 5

*The fourth fold audit, SCOPED like round 4. Round 4 (BLOCKED, four blocker rows over seven
defects, precision 0.40) graded rev-5; rev-6 is the fold of round 4's two blockers, two highs and
five mediums, and this round grades THAT fold only. Because round 4's precision sat below the ~0.5
line `AGENTS.md` §8 sets, the lenses were primed on three clauses and nothing else: §2 S5, §6 AC8
and AC12, and AC4's completion-witness clause. Everything else has been read four times and was
either found stable or drew zero findings last round; a zero against any section outside that scope
is not a measured zero. Node `a`, 2026-09-13, ROUND 5. Every finding below survived a skeptic
prompted to REFUTE it, and every suite line cited was re-read at the spec's declared base
`0422ea2e` by the author of this report rather than transcribed from a lens — the file is
byte-identical at HEAD, so one reading covers both: the three helpers at `:57-59`, `cd "$TMP"` at
`:61`, the prologue's three commits at `:173`, `:191` and `:233` and the absence of any date pin
but `:856`, `reset_tree`'s body at `:240-246` and its ~297 call lines, the `ahead` block at
`:1238-1245`, the `land the run` merge and push at `:1252-1257`, the region-two seam and its `SH_I
= 2` replay at `:1277-1294`, the restore at `:1646`, the `trunk` arm at `:3045-3053`, the floor
grade at `:3168`, the C21 epilogue at `:3216-3224`, the sharded trailer at `:3227`, the PASS line at
`:3228`, every `--git-dir="$ORIGIN"` write in the file, the zero `ls-remote` lines in it, the
`ADV_TIPS` read at `check-unattended.sh:912-913`, and the cited rulings in `TOOL-aShardedFloor-3`
(AC2 at `:90-99`, the rev-4 CLOSE at `:210-236`), its build folder's file list, and
`memory/guides/BUILD-METHOD.md:140`.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-3.md`@`1bc33ff85dd029e0d2f788f97ad735ba3c9dbd37` — rev-6, the fold of round 4. ROUND 5. Scoped to §2 S5, §6 AC8, §6 AC12, and §6 AC4's completion-witness clause.

Facts this round rests on, each checked in the tree rather than in the spec or in the commissioning
note. `reset_tree` (`:240-246`) runs with cwd `$TMP` — the work-tree clone, `:61` — and its one
`update-ref --stdin --no-deref` carries no `--git-dir` and no `-C`, so it enumerates and deletes the
CLONE's `refs/remotes/` and `refs/replace/` and touches nothing on the bare origin; every origin-side
write in the file is spelled `git --git-dir="$ORIGIN" …` (`:186`, `:936-942`, `:1528`, `:3048`,
`:3052`). **The commissioning note's verified-facts line "reset_tree runs update-ref --stdin on the
bare origin already" is therefore wrong at source**, and H1 below carries the consequence. Every
fixture commit but one is minted at run time from the clock — `GIT_COMMITTER_DATE` appears at `:856`
only, inside `mkdisp` — so `ANCHOR0`, `BASE0`, `PRISTINE` and every later sha are per-process. The
test file contains zero `ls-remote` and zero `for-each-ref refs/heads` lines: the capture S5 says it
reuses exists nowhere in the tree. `PASS ($n assertions)` prints only under `[ "$st" = 0 ]`
(`:3228`); `FAIL executed …` prints only when `$n` misses the floor (`:3168`); the trailer at
`:3227` prints for every sharded run whatever the verdict. The only heads ever pushed to the origin
besides `main` are `ahead` (`:1243`) and `trunk` (`:3047`), and `:3046` also creates a LOCAL
`refs/heads/trunk` nothing deletes. `TOOL-aShardedFloor-3`'s rev-4 CLOSE records an ancestry-property
replay and a verdict measurement (`merge rc 0` against three arms failing) and no capture equality
and no planted negative; its build folder holds one design brief, one repricing record and one
spec-audit, none of which observes AC2.

## Verdict: BLOCKED

Twelve rows at BLOCKER, five at HIGH, one at MEDIUM. Those eighteen rows collapse to **five distinct
defects**; the table below names which rows share one, so a fold that repairs a defect repairs every
row under it. Severity is adjudicated by this report, not carried from the pipeline, under round 4's
definition: BLOCKER means that built or graded exactly as written the spec yields a wrong verdict, or
a Definition of Done that cannot be met without breaking one of its own binding non-goals; HIGH means
a measurement, observation or mechanism statement the spec relies on cannot distinguish the case it
exists to catch, or is false at source so a literal build lands a no-op; MEDIUM is placement,
anchors, records and cost. Five rows the pipeline confirmed at HIGH (id=4, id=9, id=14, id=15,
id=20) are BLOCKER under that definition and the rows say why; one the pipeline confirmed at HIGH
stays there (id=8) because it carries the could-not-fail half of B2 alone.

Three defects are blockers, and all three are inside the clauses the fold rewrote. **The reused
state-equality oracle compares sha-bearing listings across two processes** (B1): S5 and AC8 require
shard k's `ls-remote --heads` plus `for-each-ref refs/heads refs/remotes` capture to EQUAL the
unsharded run's at the boundary line, and every ref in both listings carries a sha minted per
process from the clock, so the two captures differ at all seven boundaries on a correct cut, the
"replay is owed" clause fires everywhere and "correct when they match" never fires. The oracle it
says it reuses "verbatim in shape" was specified in `aShardedFloor-3` AC2 and never discharged there
— rev-6 imported a criterion nobody has seen pass and §10 calls it reuse. **The named negative has no
passing shape for a correct cut** (B2): where a leak exists to plant, "two DIFFERENT captures" holds
by construction because the capture IS the listing the plant changes, so the clause cannot fail and
the arm-naming is decoration; and the derived leaked set is EMPTY at every boundary before `:1243`
and — once S5's own delete lands — at every `reset_tree`-led boundary, so AC8's red-when ("no
difference, or no recorded pair") reds a correct build at all seven boundaries with no skip-by-name
rule. The half of the prior-art oracle that made its negative a check, the per-arm output
comparison, is the half rev-6 dropped — after round 4's B1 asked for exactly that artifact.
**AC4's completion witnesses do not print on a red-but-complete run** (B3): the clause names `PASS
(…)`, gated on `st = 0`, and `FAIL executed …`, gated on a missed floor; §3 and AC8 both say the suite
is RED at BASE and that no shard is required green, so every red-above-floor arm — at least one of
the two BASE invocations and at least one of the eight HEAD shards, on the record's own account of
where the reds live — prints neither and is recorded as NO READING by the clause's own rule. AC4
then has no longest wall on at least one side and F2's ratio cannot be taken. That is round 4's H1
fixed into a clause that voids the reading instead of witnessing it.

One defect is HIGH. **S5's delete is "batched into the `update-ref --stdin` it already runs on the
bare repo", and no such batch exists** (H1): the one batch runs on the clone, a `delete
refs/heads/ahead` fed to it exits 0 silently against a ref the clone never has, the origin's heads
survive every reset, and AC12's first clause reds on a literal build. Reaching the origin is a second
`--git-dir="$ORIGIN"` process per reset — two if the set is derived live — which is round 4's M1
cost returning on the unit whose deliverable is wall, on a claim round 4's M1 already stated and
rev-6 inverted.

The medium row: the derivation reads only the origin, but the capture it must satisfy also lists
local `refs/heads`, and the `trunk` arm leaks a LOCAL head (`:3046`) the delete never reaches, so
every boundary past `:3047` differs on a ref no S5 mechanism removes (M1).

AC12's second clause — the unsharded `FAIL` set with the delete in place byte-identical to its set at
BASE — drew no confirmed finding and is the one clause in scope that stands: it is the §3 observation
round 4's H2 asked for, and it is correctly placed where AC6 cannot see. AC4 outside the witness
clause was not in scope and carries no zero of any kind from this round.

**Convergence.** Under `memory/guides/BUILD-METHOD.md` (`:140`) the loop re-arms only on a STRICTLY
SMALLER confirmed-blocker count than the round before. Rounds 2, 3 and 4 stood at 9, 8 and 4
blocker rows; this round stands at 12. By the rule's letter the loop does NOT re-arm on this round.
Read by defect it is 2 blocker defects in round 4 against 3 here, which is not smaller either; total
defects fell from 7 to 5, and every one of the 5 sits inside the three clauses the fold rewrote.
The row count is partly an artefact of the scoping — four lenses primed on three clauses hit the
same three defects and rows multiply — but the defect count is not, and it says the fold replaced
one unbuildable oracle (rev-5's verdict sets, blind by construction) with another (rev-6's raw
captures, unequal by construction) that was never built anywhere. **Disposition of all three
standing blockers: FOLD.** Each fix lies inside S5, AC8 or AC4, each is a rule the build already has
the artifacts to apply once the per-invocation output log exists, and none needs a mechanism this
build lacks. Nothing here needs a PROMOTE. What the rule does with a round that did not re-arm is
the orchestrator's call under `:140`; this report states the count and the disposition and nothing
else about the loop.

## Review shape

- raw 24 · confirmed 18 · refuted 6 · unverified 0 · precision 0.75

Precision rose from 0.40 to 0.75, so scoping to three clauses did what scoping to five sections did
not. The refuted six were not handed to the author of this report and are not characterised here.
Read the confirmed count with the table in hand: the pipeline reports zero duplicates because each
row addresses a different clause or a different half of one, but four rows hit the sha-bearing
capture, six hit the negative, three hit AC4's witness, four hit the delete's target repository, and
one hits the local `trunk` head. Eighteen rows is five defects.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete FOR THE SCOPE THE LENSES WERE PRIMED ON, and a fold may treat the UNVERIFIED
bucket as genuinely empty. Sections outside the scope were not graded this round and carry no zero
of any kind from it.

## The five defects, and which rows carry each

| Defect | Rows (severity as adjudicated here) | Section |
|---|---|---|
| D-1 · the reused capture pair is sha-bearing and per-process, so "EQUALS" cannot hold at any boundary on a correct cut; the oracle was specified in `aShardedFloor-3` AC2 and never discharged there | id=2 blocker · id=6 blocker · id=12 blocker · id=18 blocker | B1 |
| D-2 · the named negative cannot fail where a plant exists and reds by "no recorded pair" where the derived set is empty, which after the delete lands is every boundary; the per-arm output comparison that made the prior art's negative a check was dropped | id=19 blocker · id=14 blocker · id=4 blocker · id=9 blocker · id=20 blocker · id=8 high | B2 |
| D-3 · AC4's completion witnesses are `PASS (…)` and `FAIL executed …`, neither of which prints on a red-but-complete run, so every red arm of the ten is NO READING and the ratio has no figure | id=1 blocker · id=7 blocker · id=15 blocker | B3 |
| D-4 · `reset_tree`'s batch runs on the clone, not the bare origin; a literal build lands a no-op delete, AC12 reds, and the "one spawn" cost claim is wrong by one or two per reset | id=3 high · id=10 high · id=13 high · id=21 high | H1 |
| D-5 · the derivation is origin-only but the capture lists local `refs/heads`, and `:3046` leaks a local `trunk` head nothing deletes | id=17 medium (id=3 carries it too) | M1 |

## Round 4 against the fold, item by item (scoped)

- **B1 (S5's KEPT/DROPPED oracle compares `FAIL` sets printed only on failure)** — rev-6 dropped the
  verdict comparison and adopted `aShardedFloor-3` AC2's state capture. RIGHT that the verdict sets
  cannot decide. WRONG on what replaced them: the raw captures are unequal by construction (B1 here),
  and the prior art's own closing sentence — the per-arm byte comparison "belongs here too" — is the
  part not carried. Round 4's B1 fix asked for the per-invocation output log as the artifact and for
  §10 to dispose AC2 as SUPERSEDED-in-part with the verdict comparison ADDED to state; rev-6 carries
  neither the log nor that disposition and §10 says AC2 is reused "verbatim in shape". The fix was
  inverted, not folded.
- **B2 (AC8's "runs green at each index" is unsatisfiable under §3)** — folded: AC8 now says "No
  shard is required to run GREEN; the suite is red at BASE and §3 forbids changing that" (`:233-234`).
  RIGHT. Not re-graded; no confirmed finding on that clause.
- **H1 (AC4's ten timed arms carry no completion witness)** — folded into a witness clause
  (`:198-201`) naming two lines that do not print on the run the spec itself says every arm is (B3
  here). RIGHT to add a witness; WRONG witnesses. The fix round 4 wrote named the `:3227` trailer;
  the fold named the two lines round 4 said were conditional.
- **H2 (the delete lands unobserved; §3 has no observation for it)** — folded as AC12's second
  clause. RIGHT, and it stands.
- **M1 (the delete inside `reset_tree` is one spawn per call on ~300 call lines)** — rev-6 answers
  it with "batched into the `update-ref --stdin` it already runs on the bare repo", which is false
  at source (H1 here). Round 4's M1 said in so many words that "an origin-side delete cannot ride that
  batch"; the fold asserts that it can. Inverted.
- **M2 (`trunk` is a second leak; AC8's clause is instance-shaped)** — folded: the leaks are derived
  and `trunk` is named. HALF RIGHT: the derivation reads the origin only, and the same arm leaks a
  local head the capture lists and the delete cannot reach (M1 here).
- **M3 (five "same commit" sites)** — the rev-6 log says corrected. Outside this round's scope; not
  graded here.

---

# BLOCKERS

## B1 · id=2, id=6, id=12, id=18 — the reused capture pair is sha-bearing and per-process, so "EQUALS" cannot hold on a correct cut; the oracle was specified in `aShardedFloor-3` AC2 and never discharged there

**Address:** section 2 S5 (`:57-62`, "captures `git ls-remote --heads "$ORIGIN"` and `git
for-each-ref refs/heads refs/remotes` … a replay is owed at every boundary where the two differ, and
is correct when they match after it"; `:57-58`, "which sharded this file once"); section 6 AC8
(`:224-226`, "EQUALS the unsharded run's capture at that boundary's line"; `:232`, "Red when: any
boundary's captures differ after the replay"); section 5 testing (`:172-173`, "AC8's replay observed
failing when removed"); section 4 (`:130-131`); section 10 (`:336-338`, "`-3`'s AC2 state-equality
oracle with its named negative, which S5 and AC8 now carry verbatim in shape").

Both capture commands print `<sha>\t<refname>`. Every process runs `TMP=$(mktemp -d)`, `git init`,
and commits `base` (`:173`), `unit work` (`:191`) and `facts` (`:233`) with no date pin — the only
`GIT_COMMITTER_DATE` in the file is `:856`, inside `mkdisp` — so `ANCHOR0`, `BASE0`, `PRISTINE` and
every later sha are minted per process. The unsharded run's listing at any boundary line and a
separate `--shard k/8` process's listing at its start therefore differ on every ref's sha unless the
two processes happened to start within the same second with identical trees, which nothing arranges;
AC8's predicate is byte EQUALITY with no normalisation clause, and its red-when "captures differ
after the replay" reds a correct cut at every boundary. §5's "AC8's replay observed failing when
removed" cannot discriminate, because it fails with the replay present too.

The one existing seam is a second witness against equality even after any sha mapping. At `:1252`
the unsharded run makes a `--no-ff` merge with `-m "land the run"` and force-pushes it (`:1257`);
`reset_tree` never touches local `main` or origin `main`, so both sit at that merge commit until the
restore at `:1646`. Shard 2's replay (`:1289-1293`) instead fast-forwards `main` onto `unit`
(`PRISTINE`) with `git merge --no-edit`. Different message, different topology, different
`refs/heads/main` — the replay the spec says it "generalises into a rule" produces a state that
fails the rule. And a names-only rescue, which is what AC12's "same head set" (`:236`) already says,
is blind to exactly that: `main` is a head a fresh start HAS, at a sha it does not, and the ancestry
property the SH_I=2 replay exists to restore ("one property rather than a pile of state", `:1278`)
is invisible to a name set. AC8 and AC12 also disagree on the unit of comparison — listings against a
head set — for what S5 says is one capture.

And the prior art was never discharged. `aShardedFloor-3` AC2 (`:90-99`) is the round-1 F7 wording
(`reviews/2026-08-21-review-TOOL-aShardedFloor-1.md:60`) written into the spec; its rev-4 CLOSE
(`:210-236`) records instrumentation, an ancestry-property replay, three arms repaired, counts and
walls — a VERDICT observation — and no capture equality and no planted negative. The build folder
holds one design brief, one repricing record and one spec-audit, none of which observes AC2, and the
test file contains zero `ls-remote` and zero `for-each-ref refs/heads` lines. "Which sharded this
file once" (`:57-58`) and "carry verbatim in shape" (`:338`) import wording, not a mechanism; rev-6
reuses a criterion nobody has seen pass and the DoD cannot be met as written. Four rows carry this;
all four are BLOCKER because AC8 reds on the correct build at every boundary.

**Fix.** Define the capture ONCE in S5, cite it from AC8 and AC12, and make it sha-free:

- The origin head-NAME set (`ls-remote --heads` after `cut -f2`), the local head-name set
  (`for-each-ref refs/heads`, where `trunk` shows — M1), the origin `HEAD` symref target (the `trunk`
  arm moves it at `:3048` and restores it at `:3052`), `refs/replace` empty, and the clone's
  checked-out branch (`git symbolic-ref HEAD`; region one ends on `checkout unit` at `:1261`).
- Each listed ref's objectname CLASSIFIED to a run-local label rather than compared — `ANCHOR0`,
  `BASE0`, `PRISTINE`, `landed` (a descendant of `BASE0` merged into `main`, the `:1257-1646`
  window), else `minted` — so a moved `main` is a difference the tuple SEES.
- The two predicates the seam's consumer reads: `git merge-base --is-ancestor unit main` rc, and
  `refs/remotes/origin/main == ANCHOR0`.
- State in S5 that raw sha equality cannot hold past a process boundary, that the existing SH_I=2
  replay matches the unsharded state only under the classification (it fast-forwards where the
  unsharded run merged), and that the classification is boundary-specific: after the `:1646` restore
  `main` is `ANCHOR0` again, so the SH_I=2 replay must NOT be copied to later boundaries.
- In §10, dispose `-3` AC2 as REUSED-NORMALISED: specified there, never discharged there, exercised
  for the first time here. Strike "which sharded this file once".

One caution on the confirmed fix text of id=6 and id=10, which propose adding `update refs/heads/main
$ANCHOR0` to an origin-side batch at every reset: do not. Between `:1257` and `:1646` origin `main`
sits at the landed merge on purpose — the restore comment at `:1645` says every later arm would
otherwise inherit tWaive — and the checker reads the advertisement on every `run()`
(`check-unattended.sh:912-913`), so resetting origin `main` per reset in that window moves what
arms see and is a §3 hazard. The moved `main` is a state the tuple CLASSIFIES and a boundary's
replay REPRODUCES, not a leak to delete.

**Left-shift gate.** The normaliser is a script in the build (or a guarded function in the suite),
and its first arm is its own liveness probe: run it from two fresh processes at the prologue's end
and require the RAW listings to differ (proves the shas are per-process and the normaliser is doing
work) while the normalised tuples match. Then stage the break the §7 rule demands: force-move origin
`main` to a `commit-tree` child of `ANCHOR0` and observe RED naming the tuple field that moved. A
tuple that has never been seen to red is the same assertion about nothing this round is grading.

## B2 · id=19, id=14, id=4, id=9, id=20 (blocker), id=8 (high) — the named negative cannot fail where a plant exists and reds where the derived set is empty, which after the delete lands is everywhere; the per-arm output comparison that made the prior art's negative a check was dropped

**Address:** section 2 S5 (`:65-67`, "run the shard with the boundary's leaked refs planted and
again with them absent and require a DIFFERENCE in the capture, naming the arm each boundary
breaks"; `:67-70`, "The leaks are DERIVED … every head `ls-remote` shows on the fixture origin that
a fresh start does not"); section 6 AC8 (`:227-229`, "the same shard with that boundary's derived
leaked refs planted and with them absent yields two DIFFERENT captures, with the arm each boundary
breaks named"; `:232-233`, "Red when: … any negative shows no difference, or a boundary has no
recorded pair"); section 6 AC12 first clause (`:235-236`).

Two halves, each fatal on its own.

**The could-not-fail half** (id=8, id=14(a), id=19). The capture IS `git ls-remote --heads
"$ORIGIN"` plus the local listing, and planting a leak IS pushing a head to the origin, so "two
DIFFERENT captures" holds by construction before any arm runs. The clause cannot fail once the plant
succeeds; "naming the arm each boundary breaks" is decoration, because AC8's red-when grades only the
capture. The prior art's negative (`aShardedFloor-3` AC2, `:93-95`) ties the difference to an ARM —
"naming the specific arm to break … otherwise the arm does not read the leak and AC2 protects
nothing" — and closes with "The sibling's per-arm BYTE comparison belongs here too" (`:99`). rev-6
moved the difference into the capture and kept only the arm's NAME. Round 4's B1 fix asked for
exactly that per-invocation output log as the DROP condition and the left-shift gate; rev-6 carries
neither. Nothing at this base would move on a plant anyway: `$ahead` is unused past `:1244`,
`trunk` is unused past `:3049`, `ahead` is a `commit-tree` child of `ANCHOR0` and `trunk` equals
`main`, so neither publishes an ancestry a later base could newly fall under, and the checker's
`ADV_TIPS` (`check-unattended.sh:913`) gains a sha no later arm's base carries. "The arm each
boundary breaks" has no referent, and `:67`'s "so the check reads the leak rather than passing over
it" is asserted by a check that reads only the plant. This is the §7 "a gate you have only ever seen
pass" class, reintroduced by the fold that claims to have removed the blind oracle.

**The empty-set half** (id=4, id=9, id=14(b), id=20). S5 derives the leaked set as heads the origin
shows that a fresh start does not. Before `:1243` the origin holds only `main`, so the set is EMPTY
at every region-one boundary — a hundred of the ~297 `reset_tree` call lines precede `:1243`, and
region one was roughly 40 % of the two-shard wall, so a time-balanced eight-way cut places boundaries
there. And once S5's own delete lands, the set is empty at EVERY `reset_tree`-led boundary by
AC12's own first clause. At an empty boundary "planted" equals "absent", the captures are identical,
and AC8's red-when fires on "no difference" — or the builder records nothing and it fires on "no
recorded pair". There is no skip-by-name rule in S5 or AC8 and §7 forbids a vacuous pass. Nor does
the spec say at which commit the set is derived (BASE, pre-delete, or HEAD), nor whether "at its
start" means before or after the shard's leading `reset_tree` — before, the planted ref differs
trivially; after, the delete has erased it. Under every reading a correct cut with a working delete is
red on AC8 at all seven boundaries, or passes its negative without any arm having been shown to read
anything. The check AC8 exists for — does the shard READ the state the replay restores — is not
performed by anything the spec specifies.

Severity. id=19 and id=14 state the whole defect and the consequence that AC8 has no passing shape;
id=4, id=9 and id=20 state the empty-set half, which alone makes the DoD unmeetable on a correct
build, so all five are BLOCKER by this report's definition — the same promotion round 4 made for
its B2 (a criterion with no satisfiable outcome). id=8 states the could-not-fail half alone, a check
that cannot distinguish the case it exists to catch, and stays at HIGH; the split follows round 4's
H2 precedent. The exact figures in id=4 (40 of 151) were not reproduced — this report counts 100
`reset_tree` call lines before `:1243` of ~297 — and the mechanism holds at either count.

**Fix.** Rewrite the negative as the negative OF THE REPLAY, on the artifact round 4 already named:

- For each boundary whose normalised tuple (B1) differs, run shard k with its replay and without,
  and require the shard's per-invocation OUTPUT log — every `$(run)` capture, appended by a `run()`
  that writes to a file under an env var, the `aShardedFloor-2` AC9 artifact — to differ, naming the
  arm whose line moves. At the existing seam that arm is the tWaive fixture and the difference is
  the three arms `:1287` already records.
- A boundary whose normalised tuple already matches owes no replay and records `negative: not owed ·
  boundary k` as an announced skip. AC8's red-when is scoped to boundaries that owe one, plus "a
  boundary that owes a replay and records neither a pair nor a skip".
- Drop "planted leaked refs" and the capture-difference criterion entirely. The delete makes a
  planted leak a state the unsharded run never has at any boundary, and the AC12 first clause is
  where the delete's effect is observed, not AC8.
- State the commit the leaked set is derived at (BASE, the pre-delete tree) and record the set beside
  the derivation, so "catches a third the day one lands" has a baseline to compare against.
- In §10, dispose `-3` AC2's negative as SUPERSEDED: the difference is read on the arm's output, not
  on the listing, which is what its own closing sentence asked for.

**Left-shift gate.** The per-boundary output-log diff, recorded in the build log as a table —
boundary · replay owed · output delta with the arm named · or the skip by name — and a script that
reds when an owed boundary has an empty delta or a boundary has neither row. It cannot be satisfied
by the plant, because the plant is gone, and it cannot pass vacuously, because a skip is a named row
and not an absence.

## B3 · id=1, id=7, id=15 — AC4's completion witnesses are `PASS (…)` and `FAIL executed …`, neither of which prints on a red-but-complete run, so every red arm of the ten is NO READING and the ratio has no figure

**Address:** section 6 AC4, the completion-witness clause (`:198-201`, "Every timed invocation, all
ten, is a reading only if its own summary line (`PASS (…)` or `FAIL executed …`) is present in its
captured output … it is recorded as NO READING rather than as a number"); against section 3
(`:92-93`) and section 6 AC8 (`:233-234`, "No shard is required to run GREEN; the suite is red at
BASE").

Verified at source, identical at BASE and HEAD: `PASS ($n assertions)` is guarded by `[ "$st" = 0 ]`
(`:3228`), and `FAIL executed …` prints only when `[ "$n" -ge "$FLOOR" ]` fails (`:3168`). A run that
is red on any arm and reaches its floor — which is what "red at BASE" means for a suite whose floor
is met — ends on the two C21 lines (`:3217`/`:3219` and `:3223`/`:3224`, in either shape), the
trailer at `:3227`, and `exit "$st"`, printing neither of the two lines AC4 names. The spec asserts
the red itself: §3 forbids repairing it, AC8 restates it, `TOOL-aHoistedPass-38` records the suite
"RED IN BOTH SHARDS" with causes 1 to 3 open (`memory/backlog/TOOL.md:415`), and the build README
says so at `:35`. So under the clause's own rule at least one of the two BASE `--shard i/2`
invocations and at least one of the eight HEAD shards is NO READING, and the longest wall on that
side — possibly the longest arm of all — is absent from the set the ratio is taken over. AC4
cannot produce its figure and F2's arity decision cannot be taken. That is the opposite of the class
the clause was added for: round 4's H1 said a truncated arm reads as a short wall, and the fold turns
a COMPLETE arm into a missing one. Three rows carry this; id=15 is promoted from HIGH because its own
impact line is the DoD-unmeetable one — no longest wall, no ratio, no F2 decision.

**Fix.** Name a witness every completed run prints in both verdicts, and that exists at BASE, since
the BASE reading cannot add a line to the file. All ten timed invocations are sharded runs, and the
trailer at `:3227` — `(this leg ran $MODE only; the other region was NOT exercised here)` — prints
for every `SH_I != 0` whatever `$st` is, and carries the index and arity in `$MODE`, so a mistyped
`--shard 1/8` at BASE refuses before it and is correctly NO READING. Pin it by text; if the build
rewords it for eight regions, the spec pins the new text. For any unsharded run the C21 non-vacuity
line in either shape (`:3223-3224`) is the last assertion in the file and serves the same purpose.
State that `PASS (…)` is a witness only for a green arm and `FAIL executed …` is a floor verdict,
not a completion witness. Author's note, not a lens finding and carrying no severity: `:200` cites
"this repo's `ab-arm-must-prove-it-ran` note", and the tracked gotcha is
`memory/gotchas/ab-arm-never-did-the-work.md`; correct the name in the same edit.

**Left-shift gate.** In the build's own measurement script, `grep -F 'the other region was NOT
exercised here'` over each arm's captured output, red on absence, before any wall is written into
the record. It is the gotcha's documented check made mechanical, and it reds on the truncated arm
round 4 named while passing the red-but-complete arm this round found it voiding.

---

# HIGH

## H1 · id=3, id=10, id=13, id=21 — `reset_tree`'s batch runs on the clone, not the bare origin; a literal build lands a no-op delete, AC12 reds, and the "one spawn" cost claim is wrong by one or two per reset

**Address:** section 2 S5 (`:70-73`, "`reset_tree` gains one origin-side delete of that derived set,
batched into the `update-ref --stdin` it already runs on the bare repo rather than one push per ref,
so the unsharded run pays one spawn and not one per leaked head per reset"); section 6 AC12 first
clause (`:235-236`, "When `reset_tree` runs after the leak-producing arms, `git ls-remote --heads` on
the fixture origin shows the same head set a fresh start shows"); the rev-6 log (`:286-287`, "the
delete is batched into the existing `update-ref --stdin`"); and the commissioning note's
verified-facts line for this round.

`reset_tree` (`:240-246`) runs with cwd `$TMP`, the work-tree clone (`:61`). Its `git for-each-ref …
| git update-ref --stdin --no-deref` carries no `--git-dir` and no `-C`, enumerates the CLONE's
`refs/remotes/` and `refs/replace/`, and repoints the clone's `refs/remotes/origin/main`. The bare
origin at `$ORIGIN` is addressed in this file only through `git --git-dir="$ORIGIN" …` (`:186`,
`:936-942`, `:1528`, `:3048`, `:3052`). `update-ref --stdin` cannot address a second repository, so
the batch S5 says the delete rides "on the bare repo" does not exist. Reproduced by the lenses and
re-read here: `printf 'delete refs/heads/ahead\n' | git update-ref --stdin --no-deref` in the clone
exits 0 silently against a ref the clone never has (`ahead` is pushed by sha at `:1243` and exists
locally only as the tracking ref the batch already deletes), and `ls-remote --heads` on the origin
still lists `refs/heads/ahead`. For `trunk` the same line deletes the clone's LOCAL branch from
`:3046` and leaves the origin's. A builder following S5 literally lands a no-op, the origin's heads
survive every reset, and AC12's first clause reds — the mechanism the spec says is in place is not.

The cost claim fails with it. Reaching the origin is a separate `git --git-dir="$ORIGIN" update-ref
--stdin` per `reset_tree` — one extra spawn with a fixed set, two if the set is derived live as
"catches a third the day one lands" implies — on ~297 call lines, two of them inside `anchor_break`
and `anchor_restore`, which are themselves called many times more. That is round 4's M1 cost
returning, possibly doubled, on the unit whose deliverable is wall; round 4's M1 said "an
origin-side delete cannot ride that batch and is one more process per call" (`round4.md:355-358`),
and rev-6 wrote the opposite. The commissioning note's "reset_tree runs update-ref --stdin on the
bare origin already" is wrong by the same six lines. HIGH rather than BLOCKER: a builder who reads
`:240-246` lands the right batch, and the wrong verdict a literal build produces is a correct red on
a real leak; the spec's statement about its own source is false and its cost accounting rests on it.

**Fix.** Rewrite the sentence with the mechanism, and choose the cheaper placement:

- Delete each leak at the arm that makes it, not per reset: `git push -q origin :refs/heads/ahead`
  after `:1245`, and `git push -q origin :refs/heads/trunk; git branch -qD trunk` after `:3052` —
  three spawns per unsharded run, and the second clears the local head too (M1). An intra-region
  leak is the unsharded run's own state today; the delete's scope is cross-boundary, and per-arm
  placement pays for exactly that.
- Keep the derivation as ONE end-of-suite assertion, not a per-reset scan: `ls-remote --heads` on
  the origin names only `main` and `for-each-ref refs/heads` names only `main unit`, red naming any
  third ref. That is "catches a third the day one lands" at one spawn per run instead of one per
  reset.
- If the per-reset placement is kept anyway, state it as a SECOND batch — `git --git-dir="$ORIGIN"
  for-each-ref --format='delete %(refname)' refs/heads | grep -v ' refs/heads/main$' | git
  --git-dir="$ORIGIN" update-ref --stdin` — and restate the cost as two origin-side spawns per reset.
  Do NOT add `update refs/heads/main $ANCHOR0` to it; see B1's caution.
- Correct "it already runs on the bare repo" to "runs on the clone" in S5 and in the rev-6 log
  line, and reword AC12's trigger from "when `reset_tree` runs" to wherever the delete actually
  sits. Correct the verified-facts line in this round's record.

**Left-shift gate.** The end-of-suite head-set assertion above, staged RED first by commenting out
one delete and observing the third ref named, then unstaged. It covers the class (any leaked head,
origin or local) at one spawn, and it is the assertion S5's "derived, not named" sentence describes
without a mechanism.

---

# MEDIUM

## M1 · id=17 (and the second half of id=3) — the derivation is origin-only but the capture lists local `refs/heads`, and `:3046` leaks a local `trunk` head nothing deletes

**Address:** section 2 S5 (`:67-70`, "every head `ls-remote` shows on the fixture origin that a fresh
start does not"; `:70-71`, "one origin-side delete of that derived set"); against section 6 AC8's
capture (`:225`, "plus `git for-each-ref refs/heads refs/remotes`").

`git branch -f trunk main` at `:3046` creates the clone's `refs/heads/trunk`. `reset_tree` deletes
`refs/remotes/` and `refs/replace/` only; the file has no `branch -d` or `-D`; eight `reset_tree`
lines follow `:3047`. S5's derivation is explicitly origin-side and so is its delete, but AC8's
capture reads local heads too, so the rule is blind to a carrier its own capture lists, with a live
instance in the file. At any boundary past `:3047` the unsharded capture carries local `trunk`, a
fresh shard does not, AC8's first clause says a replay is owed, and the only replay that equalises
recreates the leak in the shard rather than removing it from the run. Conditional on cut placement —
the tail past `:3047` is ~10 invocations, so a time-balanced last boundary may sit before it — which
is why this is MEDIUM and not HIGH; the derivation rule is wrong against its own capture regardless,
and S5 claims generality for it.

**Fix.** Derive from BOTH capture sources — any ref in `for-each-ref refs/heads` absent at a fresh
start (`main unit`) as well as any origin head — and delete local `trunk` at its producer with the
`git branch -qD trunk` H1's fix already places after `:3052`. Record local `trunk` as the instance at
this base beside origin `ahead` and origin `trunk`.

**Left-shift gate.** H1's end-of-suite assertion already covers it: `for-each-ref refs/heads` names
only `main unit`. One gate for both carriers, red on either.

---

## What a fold should do first

B1 and B2 are one tuple and one artifact. The tuple is the normalised capture: head-name sets on
both sides, the origin `HEAD` target, the clone's checked-out branch, each sha classified to
`ANCHOR0` / `BASE0` / `PRISTINE` / `landed` / `minted`, and the two ancestry predicates — written
once in S5 and cited from AC8 and AC12, with its own liveness probe (raw listings differ, tuples
match) and its own staged RED. The artifact is the per-invocation output log round 4's B1 already
asked for: with it, a boundary's negative is "shard k with and without its replay, output differs,
arm named", a boundary that owes nothing records a skip by name, and the plant goes away entirely.
Do the §10 disposition of `aShardedFloor-3` AC2 in the same edit — REUSED-NORMALISED for the capture,
SUPERSEDED for the negative — and strike "which sharded this file once", because the next round
will look for both.

B3 is one sentence: the witness is the `:3227` trailer, pinned by text, and `PASS`/`FAIL executed`
are named as what they are.

H1 and M1 land together: the delete moved to the two producing arms with a `git branch -qD trunk`
beside the second, one end-of-suite head-set assertion on both carriers staged RED once, and the
S5 sentence about the bare repo corrected in the spec, in the rev log, and in the round record's
verified-facts line. Precision this round was 0.75 against 0.40, so priming on clauses rather than
sections is what lifted it; the next fan should be primed with rev-7's S5/AC8/AC12/AC4 as the only
open surface, with AC12's second clause and the base bump as CLOSED and by-design, and with the
three-process fact (unsharded, shard k, and the normaliser's own probe) in the brief, so it hunts the
fold and not the history.
