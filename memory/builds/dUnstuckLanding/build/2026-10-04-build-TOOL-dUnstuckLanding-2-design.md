# dUnstuckLanding — the design: runs that close themselves, and a hand-off that is not an abort (research record)

**Serves:** research TOOL-dUnstuckLanding-2

## What this record is

This record designs against the census, `2026-10-04-build-TOOL-dUnstuckLanding-1-census.md`, and
against nothing recalled. Every mechanism section follows the same order:

1. the class it answers;
2. the candidates;
3. the test that decided between them, and why each loser lost;
4. the pick;
5. what it owes;
6. the ask it is filed under, in `BACKLOG.md`.

**A PICK HERE IS A RECOMMENDATION, NOT A RULING.** Every mechanism below changes a governance
carrier — the protocol, the stop contract, the verbs, the build method, or a kit leg — and M3's veto 2
makes that the owner's call. The owner rules on each pick when they scaffold the build that takes its
ask. Two picks reverse earlier owner rulings, and each says so where it does.

## The shape of the answer

The census says one thing four ways: **the close has no honest exit for "done, but someone else has
to land it."** So the run reaches for `ABORTED`. The owner lands the work by hand, and the record
contradicts git from then on.

The design gives the close exactly three exits, and makes each of them truthful:

| Exit | Means | Record | Who lands |
|---|---|---|---|
| **LAND** | the work passes the bar; landed whole, or partly with every remaining unit carried forward | `LANDING` → `LANDED` | the run |
| **HAND OFF** | the work is sound, and a step only the owner may take stands between it and the landing | `HELD` · `owner-landing` or `owner-decision` | the owner, or a resumed run |
| **ABORT** | the work must NOT land as it stands | `ABORTED` | nobody |

The rest of the design is how a run reaches the right exit without asking anyone:

- Inherited reds stop blocking LAND: §3 and §4.
- Closing decisions get a standing disposition: §5.
- HAND OFF gets a verb, and its attended landing gets a terminal: §1 and §2.
- The 28 existing records get settled: §2.

## 1. The hand-off verb — `--handoff`

**Answers** K2, K3 and K6. Of the 37 aborts, 36 handed work to the owner to land, and the abort
codes said so (census, "The headline").

**Candidates.**

- **(a) A new phase, `HANDED`**, between `HELD` and `VERIFYING`, with its own producer verb.
- **(b) The HELD family**: a verb that writes `HELD` under two new hold codes, reusing every guarantee
  the hold already carries.
- **(c) No new verb**: redefine two halt codes, `external-prerequisite` and `gate-red-out-of-scope`,
  to mean hand-off, and keep `ABORTED`.

**Test.** What each one costs in readers, and whether each one keeps the record true. Counted at
BASE `0c16a66b`:

- **(a) touches far more readers.** It needs a twin wherever the driver special-cases `HELD`: 84
  occurrences across 9 files. These are `unattended.sh` (58), `run-gates.sh` (10), `resume-tick.sh`
  (5), `stop-guard.js` (4), `run-unattended-gates.sh` (3), `check-unattended.sh` (2), and one each
  in `backlog.py`, `transition_audit.py` and `runlog/record.py`. It also needs an entry wherever the
  phase SETS are read: 6 files, plus `CORE_FLOOR`.
- **(b) touches two readers.** It needs `HOLD_CODES_CORE` in the driver and the `HOLD_FLOOR` pin in
  `check-unattended.sh`.
- **(b) already has the hand-off's hygiene.** `--hold` already refuses a dirty tree and an
  unpublished tip, and requires the keepalive reaped (`UNATTENDED-STOPS.md` §4). A hold released by
  `owner` is never scheduled (§3).
- **(c) keeps the record false.** It leaves a terminal that says the run finished. That is the
  falsehood the owner is complaining about.

**(a) loses on cost.** Each of the 84 sites is a place for the amendment-leaves-its-other-half-
standing class to land. **(c) loses on truth.**

**Pick — (b).** A new verb, `--handoff <slug> --code owner-landing|owner-decision --reason "<text>"
--reaped <id>`. It routes through `run_hold` with `--until owner` and adds two things:

- **The landing recipe.** It writes the commands a person runs to land this branch to the
  run-state file's parked region, as a `handoff` row in the `surfaced` class. So the owner's one read
  is a recipe, not a paragraph. Under `in-place` the recipe is `--prepare` then `--land`. Under
  `primary` it is the lander from the primary tree.
- **The settle hint.** It prints the `--settle` line from §2, which the owner runs after landing.

The two codes say what the owner owes:

- `owner-landing` — nothing to decide; only the landing remains. This is the node-b runs, and the
  cross-repo order.
- `owner-decision` — one parked decision stands first. A decision row is required, and the verb
  refuses without one.

Both join `HOLD_CODES_CORE`, and `HOLD_FLOOR` moves from 5 to 7.

**What changes for `--abort`.**

- **The meaning.** `ABORTED` comes to mean DISCARD: the run's work must not land as it stands. The
  protocol §3 gains that sentence.
- **A notice, never a refusal.** From a dated `HANDOFF_CUTOFF`, an `--abort` whose code is one of
  the four hand-off-shaped codes prints a notice naming `--handoff`. Those codes are
  `external-prerequisite`, `gate-red-out-of-scope`, `scope-approval-needed` and
  `repo-state-out-of-mandate`. The verb cannot know that the work is sound; the run does.
- **The backstop is §2's signal.** It flags any `ABORTED` record whose work reached the remote
  anyway.

**What it owes.**

- `unattended.sh`: the verb, the two codes, and the notice.
- `VERBS.template.md`: an entry for `--handoff`.
- `STOPS.template.md`: §2 and §11. The durable restart a hand-off owes is `none`.
- `PROTOCOL.template.md`: §3's ABORTED sentence.
- `SKILL.template.md`: a "If it is done but you may not land it — hand it off" section, before the
  abort section.
- The gate leg's hold-floor pin.

**Filed as** `TOOL-dUnstuckLanding-3`.

## 2. The attended terminal — derived, then settled

**Answers** K3. 28 ABORTED records and 10 LANDING records disagree with git. Under `primary`, the
`--landed` stamp is a commit made after the push, and five nc merges exist only to carry it.

**Candidates.**

- **(a) A new terminal phase, `LANDED-ATTENDED`**, written over the record by a verb, ABORTED
  records included.
- **(b) Derivation only.** A handed `HELD` record whose own commit is on the advertised tip READS
  `LANDED (attended)` everywhere that derives. An ABORTED record whose witness is there reads
  `ABORTED (work landed at <tip8>)`. Nothing is written.
- **(c) Derivation plus one writer.** Do (b), and add a verb, `--settle`, that WRITES what the
  derivation computes:
  - a handed record becomes `phase: LANDED`, with `landed-by: attended` and `landed-derived:
    <commit> <tip>`;
  - an ABORTED record keeps its phase and gains one fact, `work-landed-at: <witness> <tip>`, decided
    by the CONTENT predicate below, never by ancestry alone.

**Test.**

- **Is witness ancestry a sound predicate? No, for an ABORTED record. (rev-2, H1)** The probe
  `git merge-base --is-ancestor <witness> <remote tip>` read ON for all 30 ABORTED records in the
  three repositories. For a record read FROM the tip, that is structural.
  - **Why it is structural.** `verb_abort` writes `witness` = HEAD of the tree that runs it
    (`unattended.sh:4746-4749`), and the record's own commit sits on top of that HEAD. So any ABORTED
    record that reached the tip has its witness on the tip.
  - **Why the negative proved nothing.** The two OFF readings rev-1 cited, nc `a7e0eb03` and inCMS
    `eafbff4f4`, are LANDING stamps. They are not members of the population the probe acts on.
  - **Worse shapes.** A witness equal to BASE (an abort before the first commit) is on every later
    tip. A witness from another tree is foreign work: gov `dTieredTribunal`'s `ee0e7547` is
    `aBoundedCeiling`'s commit.

  So ancestry measures "the RECORD reached the default branch". The census's evidence that the WORK
  landed is the per-run merge after each abort, and not this probe.
- **The predicate that replaces it: the CONTENT predicate.** An ABORTED record's work landed when
  all three of these hold:
  - **(i) The witness is a real tip of the run's own work.** The witness is not an ancestor of the
    record's `base`, and `base..witness` contains at least one commit attributable to the run: one
    naming its slug in the subject, or touching `memory/builds/<slug>/`.
  - **(ii) Every attributable commit is an ancestor of the tip.**
  - **(iii) No commit on the tip's first-parent line since the landing reverts one of them.** That is
    a `This reverts commit <sha>` trailer naming one.

  When (i) cannot be decided — `base` is missing, or the history is unreadable — the predicate refuses
  with a number and does not guess. Its negative arms come from the population it acts on: a fixture
  record whose witness equals its base, one whose witness is a foreign tree's commit, and one whose
  work was merged and then reverted. Each must read OFF.
- **(a) fails twice.**
  - **Immutability.** A terminal written over a terminal is what `refuse_if_terminal` (fail 26)
    exists to stop. nc's `23be1536` refused exactly that, because LANDED over ABORTED "would
    manufacture a state no sequence of verbs produced".
  - **Cost.** It is a third terminal, which means 6 phase-set readers and a floor.
- **(b) fails on the most-read file.** `UNATTENDED-STOPS.md` §12 says the committed live index does
  NOT derive, because it is freshness-gated. The record bytes, and every reader that does not derive,
  would keep saying `HELD` or `ABORTED` forever. The contradiction stays in the file the owner reads.
- **(c) passes both tests.** The phase still answers "how did the run end", and the fact answers
  "where did its work go". The writer is a derivation made durable, which is what `--preflight`'s
  rotation already does for a derived-`LANDED` record (§12).

**Pick — (c).** Three parts:

- **(c1) `read_derived_phase` extends to `HELD` under a hand-off code.** The extension is the same
  landing-commit-by-content rule §12 uses. That rule's reader, `read_landing_commit`
  (`lib-unattended.sh:1066-1072`), returns nothing unless HEAD's copy reads LANDING, so it must
  admit a HELD record under a hand-off code as well. For a handed record, ancestry IS the right
  test, unlike an ABORTED one: the hand-off commit is the run's last act on its own branch, and a
  landing that carries it carries the work it hands off. It does not extend to any other hold code: a paused run
  whose branch somebody merged has not been handed off, and deriving a terminal under a live lease
  would kill the run with fail 26. `--status` and `--liveness` print the derived reading. The gate
  leg's check-7 exclusion and its fact-set arm accept it, with `landed-by: attended` added to the
  fact set.
- **(c2) `--settle <slug>` writes what (c1) derives.** It also writes `work-landed-at` onto an
  ABORTED record. Any session may run it, attended or not, because the act is an observation: it
  writes only what the advertised tip proves.
  - **What it refuses.** It refuses, numbered, on a record that neither derivation covers. It
    refuses on a live lease that is not the caller's. And it refuses when the remote does not answer.
  - **A narrow exception to fail 26.** For an ABORTED record, the one fact is the only write fail 26
    admits. The exception is stated in protocol §3 beside "A run that is already terminal cannot be
    moved at all", because a rule with an unstated exception is two answers to one question.
- **(c3) A drift-audit signal, `aborted_work_landed`.** It lists every ABORTED record that the
  content predicate reads ON and that carries no `work-landed-at`. Its liveness comes from the same
  three fixture records (c2)'s arms use, each of which must read OFF. It is never fed a free-standing
  sha. Its count today is not claimed here, because rev-1's 28 counted records that reached main, not
  work that landed.

**What it owes.**

- `unattended.sh`: `read_derived_phase`, the `--settle` verb, and the fact-set arm. Also
  `--preflight`'s order: it derives and rotates a terminal (`:5080-5081`) BEFORE its HELD refusal
  (`:5141-5142`), so a handed record that derives LANDED must rotate with every fact the rotation's
  fail 81 requires (`:5127`).
- `lib-unattended.sh`: `read_landing_commit`, so that it admits a HELD record under a hand-off code.
- `STOPS.template.md`:
  - §1, whose "Only `--landed` and `--abort` still write a terminal" and whose
    `--preflight`-over-HELD refusal both change;
  - §8, a resume-matrix row for a handed record that derives LANDED;
  - §12.
- `PROTOCOL.template.md`: §3, both the exception and the "write the two ends" sentence.
- `VERBS.template.md`: an entry for `--settle`.
- `tools/drift-audit/drift_report.py`: the signal.
- `check-unattended.sh`: check 7, check 15 and the fact-set arm.

**Filed as** `TOOL-dUnstuckLanding-4` for (c1) and (c2), and `TOOL-dUnstuckLanding-5` for (c3).
They are separate because one is a writer and the other is a reader with its own liveness assertion.

## 3. Inherited reds stop blocking LAND

**Answers** K1a. This is the owner's "why are inherited reds not resolved automatically", and the
census answers it in eight mechanisms. Two findings narrow the design.

**INHERITED already means non-worsening.**

- **The test.** The classifier's rule 5 (`run-gates.sh:2403-2405`) reads a leg INHERITED only when
  the run's offender set is a SUBSET of the offender set at R, or, for a leg without a `signature`,
  when the output is byte-identical.
- **What it rules out.** A run that adds an offender to a leg that is already red reads OWN or
  MIXED, never INHERITED. aStagedLane's wrongly claimed "pre-existing" lexicon red would read OWN
  today.
- **What it means.** Landing an INHERITED red makes nothing worse by construction, which is protocol
  §11's adoption test. The only thing that stops a run landing one is the AGE BOUND, together with
  the kit default.

**The age bound turns a permanent red into a fleet-wide stop.**

- **Some reds never age out.** They are permanent by construction: a history-anchored leg, a
  shrink-only pin only the owner moves, or a red in another repository. The census counts 13 of them
  in nc (6 tenure and 7 history-leg instances), 9 in inCMS (6 shared-ceiling and 3 history-leg
  instances), and the lexicon and drift pins in gov.
- **The bound then parks every later run.** Once one of those reds passes `INHERITED_RED_MAX_AGE`
  landings, every later run holds `inherited-red` until the owner moves.
- **The hold does not fix main.** Its release, `probe gate`, re-runs a bar that stays red. No
  `inherited-red` hold has ever been taken in gov.

**Candidates.**

- **(a) Keep the policy, and raise or remove the bound per repository.** This is the status quo
  dial.
- **(b) Land every INHERITED red, aged or not, and make the age an ESCALATION.** At the bound, the
  ask auto-filed for the leg (`UNATTENDED-STOPS.md` §13) is raised to `BLOCKER`. It stays in the
  CLOSING build's BACKLOG, where §13 files it today, and it is reused by the next closing run that
  meets the same leg at the same R. `memory/LIVE.md` lists "main red on <leg> since R~<n>". The kit
  default becomes `land`. (rev-2, H2 and H5) Rev-1 filed the ask in the INTRODUCING build's backlog.
  An aged leg never has an introducer: `derive_age` returns `aged` before any bisection
  (`run-gates.sh:2876-2879`), and the driver then files it as "introduced by an unknown landing".
  Filing into another build would also be a write into another run's folder.
- **(c) Widen ABSORB.** Let a run raise a shrink-only pin, or move a cutoff, when its own diff did
  not move the counter.

**Test.** The census instances, read against each candidate:

- **(a) changes nothing.** A permanent red outlives any finite bound, and an infinite bound is (b)
  without the escalation. So (a) loses on the K1b and K1c instances.
- **(c) contradicts the owner's own record.** The owner's pin moves do not follow a rule a grant
  could encode: inCMS check 23 went 18 → 20 → 72 → 20 → 21 → 19 in ten days, and nc build tenure
  went 0 → 2, 0 → 1, 1 → 2, 2 → 4. Each was a judgement about which build to blame. A grant that
  automated it would be the run authorizing itself, which runs refuse on the record (inCMS
  `aRisingCultivar`, nc `aBoxedCipher`).
- **(b) lands every K1a instance whose attribution is INHERITED.** Gov `dAlignedCarrier` already
  landed that way. It lands none whose attribution is OWN, MIXED or CONTENDED: gov `aReapedSpinner`
  (8 of 13 legs own) and `aSightedSkeptic` (comparator rule) still stop, correctly. And the pressure
  the bound meant to put on the owner arrives as a BLOCKER ask and a LIVE line, instead of as a held
  run that did not break main.
- **An age-unproven leg lands too.** Under (b) the age decides only the escalation, never the
  landing. A leg whose age probe cannot answer lands, and is not escalated, since nothing proves it
  aged.

**Pick — (b).** This REVERSES part of owner ruling D12-i4 (`TOOL-dDerivedDocket-24`): the kit
default `park` and the bound as a stop. It keeps D12-i5, ABSORB, unchanged. That stays true in fact,
because the per-leg ask stays in the closing build, where ABSORB's fourth condition already looks for
it. The ask states the reversal. Under the reversed policy, `park` remains a declarable value for a repository that wants
it.

**What it owes.**

- `unattended.sh`: `read_gate_policy`'s default, the decision table, and the ask-filing site.
- `tools/run-gates/run-gates.sh`: the `ATTR_LANDABLE` predicate, which today counts only legs with a
  numeric age into `land_n` (`:3026-3036`, `:3051`), so an aged or age-unproven leg never sets it. The
  inherited-green stamp is written only under it (`:3375`). The comment at `:2785-2788` says aged is
  something "no policy lands". Without this edit, `gates-green` would meet, `--close` would write
  LANDING, and the pre-push hook would refuse the push: a new stranded-LANDING path made by the fix.
- `.githooks/pre-push`: the policy read at R, and its admission of a red push only from the
  inherited-green stamp.
- `STOPS.template.md`: §13.
- `memory/DECISIONS.md`: a superseding row for `TOOL-dDerivedDocket-24`.
- `gen_build_index.py`: the LIVE line.

**Filed as** `TOOL-dUnstuckLanding-6`.

**Declined: early detection at `--preflight`.** The candidate read the anchor's known-red legs
from the node's local bar records, or from remote CI, so that a run could plan an absorb unit at the
start instead of at the close.

- **Tested on this very run.** The node keeps five bar records, keyed by run id. None of them
  covers this run's anchor, `a587e82d`, which another node landed. And the newest full-green stamp
  names `1f915870`. `gh` is not installed on this node, and neither adopter has a remote CI bar. So
  the fact would have read `unknown` here, and wherever the anchor was landed from elsewhere.
- **Its strongest form is ruled out by K4.** A background bar at BASE would double bar contention,
  which K4 measures as a failure class of its own.
- **What decides instead.** Close-time attribution, plus §4, decides the K1a cases this candidate
  was for.

## 4. History-anchored and fleet-counter legs grade only the run's own share

**Answers** K1b and K1c. These are the reds that are never the closing run's to fix, and in the
adopters they are the largest single class. inCMS check 23 was behind 6 aborts and 2 owner landing
exceptions. nc's build tenure was behind 6 pin raises, and its history legs behind 7 runs.

**Candidates.**

- **(a) Grade each such leg over the run's own range and the run's own budget.**
  - **The history legs**, `brief-recorded`, check 23 and `pass-order`, grade only commits in
    `<advertised tip>..HEAD`. A violation already on the default branch was graded when it landed,
    and it is never graded again.
  - **The fleet counters** grade only the closing build's own contribution against a per-build
    budget. Those counters are the undeclared-write count, build tenure, and any count summed over
    other builds' records. The fleet total is REPORTED, with a `fleet` line, and never fails a
    closing run.
- **(b) Leave the legs as they are, and let §3's policy land them as INHERITED.**
- **(c) Leave them, and auto-exclude any record whose build has a derived terminal.** This
  generalises what gov did for check 23, where `TOOL-aSightedSkeptic-13` took the ceiling from 45 to
  0.

**Test.** The census instances:

- **(b) cannot catch the shared-counter case.** A shared counter crossed by the run's OWN
  increment, together with others' rows, reads MIXED, not INHERITED. inCMS `dTuckedKebab` was 29
  against 20: 11 rows its own, 18 another build's. So (b) still stops on it, although the run's own
  11 were the only part it could act on.
- **(c) fixes only part.** It closes the stale-record half: inCMS `dSnideCartographer`'s 18 rows
  were a record that never reached a terminal. It leaves build tenure, which counts OTHER live
  builds' age, and the history legs, whose subject is landed history.
- **(a) answers every instance, and loses no signal.** A violation is still graded once, in the
  build that made it, and the fleet line keeps the total visible. Gov's own check 23 already moved
  most of the way to (a), with generated renders skipped and terminal records excluded. (a)
  finishes the job and names the principle: a closing run's bar grades the closing run.

**Pick — (a).** Where a project wants the fleet ceiling to BIND somewhere, it binds in a scheduled
or owner-run audit — drift-audit or the remote CI's daily `held` job. It does not bind in a closing
run's bar.

**What it owes.** `check-unattended.sh` check 23, `check-brief-recorded.sh`, `check-pass-order.sh`,
and the nc and inCMS tenure legs in their own repositories. **Filed as** `TOOL-dUnstuckLanding-7`
for the kit's three legs. The adopter tenure legs belong to §8's carriage.

## 5. Closing decisions get a standing disposition

**Answers** K2. 46 closing decisions were deferred across the three repositories, and every one of
them landed on the absent owner as an abort or an override.

**Candidates.**

- **(a) A CLOSED close-decision table, ratified once by the owner.** It names each decision KIND the
  census found, and maps it to one of the three exits plus the record it writes. The run applies the
  table and never parks a decision of a listed kind.
- **(b) Standing grants.** A project key, `CLOSE_GRANTS`, lifts veto 2 for named carrier classes, so
  that a run may move a pin or edit a carrier at the close.
- **(c) A pre-asked close.** The prompt path's one owner turn also asks the foreseeable close
  questions, for example "if the build ends partial, land the closed units?".

**Test.** The census's seven decision kinds (census, K2), resolved without an owner turn at close:

| Kind | (a) the table | (b) grants | (c) pre-ask |
|---|---|---|---|
| land a partial build | LAND, carrying the rest forward (below) | no | only on the prompt path |
| move a shrink-only pin | dissolved by §4; any rest is HAND OFF `owner-decision` | yes, but see §3's test | no |
| act on another run's record | no act needed: concurrency is permitted, and §2's derivation excludes the record | no | no |
| publish another session's commits | never occurs under `in-place`, which §8 carries to the adopters | no | no |
| land in a dependency order across repos | HAND OFF `owner-landing`, with the recipe naming both repositories | no | no |
| choose a fix where every option touches a carrier | HAND OFF `owner-decision` | partly | no |
| a question main already answered | §6's refresh, before any park | no | no |

How each candidate fares on that table:

- **(a) resolves all seven** into a truthful exit.
- **(b) resolves one and a part**, and that one is the pin move §3's test showed the owner does not
  make by rule.
- **(c) resolves one**, and only on the prompt path. The slug and scaffold paths have no owner turn
  at all.

**Pick — (a).** Two of the table's rows need mechanics, and those are what the ask carries.

**The carry-forward partial landing.**

- **What changes.** `build-complete` meets, with no override, when every unit that is not CLOSED is
  `DEFERRED` with a filed ask that this build's `BACKLOG.md` holds open, and when no CLOSED unit
  declares a `consumes-from` edge (TEMPLATE-SPEC §3) onto a unit that is not closed.
- **The edge clause is the safety half.** A partial build whose closed half needs the open half is
  not landable, and that case is a HAND OFF.
- **Why it is safe to land.** The charter's dark-landing rule (template §1) already makes landing
  half a feature safe when it ships behind a default-OFF flag.
- **What the owner sees.** The deferral is a `rescope` row that the wrap-up surfaces, so dropping
  declared scope still reaches the owner's one read (M3: a build may resolve its scope, never
  abandon it unrecorded).
- **What it would have done.** gov `cBriefedPilot` (16 of 22 units, bar 54/54 green) lands its 16.
  `dScriptedRepeat` lands its closed units, and both of its forks become asks. The 11 gov, 4 nc and
  3 inCMS `build-complete` overrides are the population this rule addresses. Which of them meet the
  edge clause is that unit's own measurement to make, and is not claimed here.

**The rule beside M3's park rule.** BUILD-METHOD M3 says "No survivors → park". At the CLOSE, a park
is never an abort: the park is recorded, and the run takes the table's exit. That is one sentence in
M3. It points at the protocol section that holds the table, so the table exists once.

**What it owes.**

- `unattended.sh`: `build-complete`'s terms.
- `PROTOCOL.template.md`: a new subsection holding the table.
- `BUILD-METHOD` M3: one sentence. The memory-tree kit renders it, and its budget is ≤30720 bytes,
  so the sentence must fit or displace.
- `SKILL.template.md`: the Close section.

**Filed as** `TOOL-dUnstuckLanding-8`.

## 6. Refresh before a verdict

**Answers** K2's last row and K1's stale-BASE variant:

- nc `dGuardedThreshold` parked a question that main had answered four hours earlier.
- gov `aBranchedMandate` overrode a red that came only from a stale LOCAL main.
- gov `aStagedLane` claimed "pre-existing" against a base main had moved past, and the claim was
  later withdrawn.

**Candidates.**

- **(a) A refusal.** `--park`, `--handoff` and `--abort` refuse until the run has merged the
  advertised tip into its branch.
- **(b) A notice.** The same three verbs, and `--close` under `primary`, OBSERVE the advertised tip
  and print the commits on it since BASE that touch the build's declared write set or its README.
  They write the observed tip as a `refreshed-at` fact, so the record shows the verdict was taken
  against a known tip.
- **(c) Nothing.** Rely on `in-place`'s `--prepare`, which already merges the tip before the bar.

**Test.**

- **(c) covers only the bar, and only in gov.** It is the bar under `in-place`. It does not cover
  the parks and aborts that come before the close, and it does not cover the `primary` adopters. All
  three instances above are outside it.
- **(a) adds a write mid-run.** A merge can conflict. And it makes a park, the cheapest honest act a
  run has, the most expensive one.
- **(b) costs one `ls-remote` and one `log`.** `observe_anchor` already does the first, and it
  changes no write. The fact makes a stale verdict visible to the wrap-up rather than to the next
  person who trips on it.

**Pick — (b).** **Filed as** `TOOL-dUnstuckLanding-9`.

## 7. Landing capability is declared, and checked at `--preflight`

**Answers** K6: nc's node-`b` runs (5) and inCMS's shared primary tree (10).

**Candidates.**

- **(a) Refuse** a `--preflight` on a node the project does not declare as able to land.
- **(b) Pre-declare the hand-off.** A project key, `LANDING_NODES`, lets a run on any other node
  start normally, record `landing: handoff` as a fact, and end at `--handoff --code owner-landing`
  by design. `landed-via-lander` and `gates-green` are not overridden.
- **(c) Leave it to the project's prose**, which is what nc's `CLAUDE.md:59` does today.

**Test.**

- **(c) is today's outcome**: 5 runs that each overrode an item they "knew before it started", then
  aborted (nc `bGildedVestibule/RUN.md:46`).
- **(a) throws away work the owner wanted.** Node `b` built real units that landed attended, so
  refusing loses them.
- **(b) keeps the work and makes the ending honest from the first commit.**

**Pick — (b).** The inCMS half is not a node capability. It is the `primary` lander publishing other
sessions' commits from a shared local `main`, and gov's `in-place` mode removed it here
(the `LANDER_MODE` declaration in `.unattended.conf` and its comment). That half is §8's.

**Filed as** `TOOL-dUnstuckLanding-10`.

## 8. Carriage — the adopters run the kit this design changes

**Answers** the fact that 22 of the 37 aborts were in repositories running kit 1.40 or older:

- **No stop contract.** There is no `HELD`, so every hand-off and every pause is an ABORTED.
- **No attribution.** There is no inherited-red classifier, so an override at `--close` buys nothing
  at a lander that re-runs the bar.
- **No `in-place` lander.** So a landing publishes other sessions' commits from a shared local
  `main`.

**Candidates.**

- **(a)** Carry the kit forward through the deployer once §1 to §7 land, with `LANDER_MODE="in-place"`
  and `INHERITED_RED=land` declared in each adopter.
- **(b)** Back-port only §1 and §2 to 1.40.

**Test.**

- **(b) needs features 1.40 does not have.** §1 rides `HELD`, and §2's derivation rides §12's
  landing-commit rule. Neither exists in 1.40, so a back-port is the forward-carry under another
  name.
- **(a) is the only candidate whose pieces exist.**

**Pick — (a).** It writes into foreign repositories, so it is a deployer act under that kit's
containment rules, and the owner of each adopter scaffolds it. **Filed as** `TOOL-dUnstuckLanding-11`.

## What this does not answer, said out loud

- **K4.** The bar that does not return, and load flakes such as inCMS's `0xC000070A`. Gov's backstop
  and `host-degraded` holds cover the "did not return" half. The flake class has never been
  left-shifted in inCMS: no gotcha, ask or build names it. That is inCMS's own finding to file, and
  §8's carriage is where it would ride.
- **K5.** Marker-ordering defects. Gov's in-place mode and derived terminal closed most of them. The
  ones still open already have asks: `TOOL-aUnblockedFleet-7`, `TOOL-dUnstalledConvoy-24` and
  `TOOL-dUnstalledConvoy-38`.
- **Conservative attribution** (the comparator rule and KF3). It is deliberate. The runner's header
  records two wrong "not mine" claims among five stops, and loosening it would buy back the class it
  closed.
- **The two abandoned BUILDING records**, gov `aClosedDocket` and `aUnblockedFleet`. Once §1 and §2
  land, `--settle` reports them as covered by neither derivation, which is the honest state, and
  their owner decides.

## Order

§1 → §2 (the derivation reads §1's codes). §2 → §5 (carry-forward needs the hand-off exit). §3, §4
and §6 are independent of each other and of §1. §7 rides §1. §8 rides all of them.
