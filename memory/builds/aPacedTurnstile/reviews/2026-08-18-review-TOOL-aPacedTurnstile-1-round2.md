# Spec audit round 2 — TOOL-aPacedTurnstile (units 1-7)

**Serves:** spec-audit TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 TOOL-aPacedTurnstile-7

**Date:** 2026-08-18 · **Tier:** 2 · **Streams:** tooling · **Base:** `f00cf2ee` · **Round:** 2
**Targets:** the seven specs under `memory/builds/aPacedTurnstile/spec/` as they stand after the
round-1 fold-in and the design-pass fork sweep, read against each other, against the build README,
and against the tree at this base. **Question asked:** did folding round 1 and ratifying the section-8
forks leave a set that still describes a bar refusing a bad merge — and did any fold-in land half,
inverted, or in the wrong unit? **Out of scope:** the five owner decisions settled at kickoff, the
findings round 1 already closed cleanly, and anything requiring code that does not exist yet.

## Verdict: BLOCKED

One blocker survived, and it is a design defect in the newest text rather than a leftover. In
`TOOL-aPacedTurnstile-7`, predicate 0 forces a full run whenever the recorded green's tree
fingerprint differs from a fresh fingerprint of the PUSHED TIP. `TOOL-aPacedTurnstile-5` defines that
digest over the committed tree object, so it moves on every commit, and `-5` S7 already refuses to
write the green record unless the tree was clean at start. Predicate 0 therefore fires on every push
whose tip is not tree-identical to the commit the green was earned on — which is exactly the
population predicates 3 and 4 exist to admit. The lag window is dead code, AC1 and AC6b cannot both
hold on a real push, and every landing keeps paying the measured full-bar cost the build's headline
claim is about. Both arms are fixture-built, so nothing on the bar notices; the failure reads as
caution, which is the same shape `-5` S5 warns about for the digest itself.

The dominant theme below the blocker is fold-in completeness. Nine of the twenty-nine findings are
round-1 findings that landed partially: F38's cleanup split was written into `-4` instead of `-5`
and with the ownership inverted, so the widened trap now deletes the durable record `-5` exists to
create (R2, R3); F21's testsuite-count conflict was never folded at all and now has no reachable
green state, since satisfying the criteria reds the staleness arm on the waiver rows `-1` S11 keeps
(R4, R5); F43 repointed one of two stale paths (R26); F15, F25 and F31 each landed one of their two
halves (R29, R21, R16); F39 fixed the scope item and left the security checklist asserting the
opposite (R24); F10's defect was relocated from the figure half of the claim to the formula half by
the fix for it (R23); and F33 is untouched (R22). None of these is a re-raise of something already
closed — each was checked against the revision logs, and where a log claims the fold the residue is
named.

The second theme is new: the ratified section-8 answers are themselves a defect surface. Three units
now carry a RESOLVED line that no scope item implements or that contradicts the fold-in the rest of
the same file carries. `-1`'s pick ships a default-selection edit that S8, the files-touched table
and every criterion omit, so the hazard it closes ships unbuilt and silently (R11-R13). `-5`'s pick
ratifies "clear it each run" and credits blocker F2's closure to clearing, when the rest of that file
now closes F2 with the run id and preserves the per-run directory deliberately — a builder following
§8 restores the branch F2 named (R6). `-3`'s pick names contiguity as the protection against an
unclaimed leg, the reasoning round 1 refuted by construction, and does not cite the unconditional
assertion that replaced it (R29). The sweep appears to have ratified an option set written before the
fold-in, which is a process signal as much as a text one.

The third theme is the deployment boundary this build opens. `-1` promotes the runner to a deployable
kit, and the set has not finished thinking about what that means. Three siblings key the SHIPPED
canary on gov's own corpus — six chunk names, gov's network-calling leg names, a gov leg's guard — so
the kit is red on arrival in an adopter tree, which is the pin-copied-from-another-corpus class `-1`
itself cites when it refuses to seed gov's leg names (R10). The guard hole the README stakes the
build's largest risk on has two carriers, and `-7` S10 fixes the one that does not ship (R7). And
enumerated populations keep standing in for measured ones: `-7` S9 names three carriers of the
safety property where the tree holds at least seven, two of them product files an adopter receives
(R8); `-1` S10 names six spellings of the pre-move path and misses two under `memory/guides/` that
red an UNGUARDED leg on the single commit the rollout insists on (R9); `-3` freezes 70 legs for a
commit that lands after three more are added (R17).

Counting: 1 BLOCKER, 9 HIGH, 15 MEDIUM, 4 LOW, against round 1's 5 / 25 / 13 / 1. Three of the
twenty-nine are the same defect reached by two lenses and three by three lenses; they are kept
separate, as round 1 kept F9-F11, because the lenses carry different evidence. Eight raw findings
were refuted and are listed at the end so the next round does not spend a lens on them. Nothing in
this round challenges the build's architecture: the emitter design, the turnstile, the chunking and
the read-side inversion all survive. What is not yet true is that the seven documents agree with each
other and with the tree.

## Findings

### R1 - BLOCKER - TOOL-aPacedTurnstile-7 §2 S2b · §4 The decision, predicate 0 · §6 AC6b

- **Claim:** predicate 0 is evaluated first and forces full when "the record's tree fingerprint does
  not equal a fresh fingerprint of the pushed tip". `-5` §4 defines that digest over the committed
  tree object plus the porcelain lines plus dirty-file blob hashes, so it changes on every commit,
  and `-5` S7 already refuses to write `gate-full-green` unless the tree was clean at start — so the
  recorded value is always the fingerprint of the recorded sha's own tree. Predicate 0 therefore
  fires on every push whose tip is not tree-identical to the commit the green was earned on, which
  is exactly the set predicates 3 (ancestor) and 4 (lag ≤ `GATE_FULL_MAX_LAG`) exist to let through.
- **Impact:** the scoped path is unreachable in practice, predicates 3-6 become dead code, and AC1
  (records-only commit plus a fresh record ⇒ the gate runs without the full-run flag) and AC6b cannot
  both hold on a real push. Both are fixture-built, so an AC1 fixture whose synthetic record is
  stamped at the fixture's own tip passes while the shipped hook forces full forever. The single
  build-level claim the README and this unit's §1 rest on is not implied by the union of §6.
- **Fix:** the defect is in `-7`, not `-5`. Either drop predicate 0 and treat the record's existence
  as the clean-tree assertion `-5` S7 already makes it, or restate it as a join at the RECORDED sha —
  the record's `tree_fingerprint` against a fresh fingerprint computed at that sha — and restate AC6b
  in those terms. The reason string is fine; the tip half is what is wrong.
- **Confirmed because:** read against current text. S2b and §4's decision table both spell predicate
  0 against "a fresh fingerprint of the pushed tip", evaluated first; `-5` S5/§4 define the digest
  over the committed tree object; `-5` S7's clean-at-start precondition already closes the dirty-tree
  hole §4 gives as predicate 0's justification, leaving the tip-side join with no purpose and a fatal
  side effect.

### R2 - HIGH - TOOL-aPacedTurnstile-4 §4 Signals, the sibling-premise paragraph

- **Claim:** `-5`'s ratified fork A is "clear it each run", a sweep at the START of a run, which
  presupposes the per-run directory survives the previous run's exit. `-4` §4 says the opposite about
  the same directory: the widened trap "releases the beacon and sweeps the run directory, and the two
  units must agree on which of them owns the cleanup line — this one does". Under `-5`'s vocabulary
  the run directory is `<git-dir>/gate-run/<run-id>/`, the durable record. `-4`'s premise is also
  factually wrong about the current `-5` text: `-5` S1 retargets only the per-leg completion files,
  so the `mktemp -d` scratch still exists and still holds the timings temporaries.
- **Impact:** `-4` lands sixth, after `-5` and `-3`. Its builder writes a trap that deletes the run
  directory on every clean exit and on INT, TERM and HUP — destroying the record on the one path that
  is not a crash. `-5` AC3 and `-3` AC7/AC8 red on the bar, and the builder must adjudicate between
  two specs mid-build with no stated owner of the lifetime. Meanwhile the leak round 1's F38 actually
  named, the scratch dir on TERM and HUP, is still unaddressed in `-5`, which still says "drop the
  trap" in §4 and "restoring the trap" in Rollout.
- **Fix:** split the two directories explicitly in both files. `-4` §4: the widened trap releases the
  beacon and sweeps the `mktemp -d` scratch, and never touches `<git-dir>/gate-run/`. `-5` S1 and §4:
  the trap stops covering `<git-dir>/gate-run/` and keeps covering the scratch dir, and the
  start-of-run clear is the only deleter of the per-run record. Rev-bump both with §9 lines.
- **Confirmed because:** F38's prescribed fix was to `-5` S1 and was applied to `-4` instead, with the
  ownership reversed; `tools/run-gates.sh` line 219 confirms the scratch dir still holds
  `timings.new` and `timings.merged`, so the premise "retargets the scratch directory" is false at
  the text it cites.

### R3 - HIGH - TOOL-aPacedTurnstile-4 §4 Signals, against `-5` §2 S1 / §4 / §6 AC3

- **Claim:** the same sentence read from the sibling-agreement side. `-5` S1 uses "the run directory"
  for exactly `<git-dir>/gate-run/<run-id>/` ("Creating the run directory fails the run the way the
  `mktemp -d` it replaces already does"), and assigns its retention to a start-of-run sweep; `-4`
  claims the cleanup line for its own trap. Two specs claim ownership of one cleanup with opposite
  semantics, and the later-landing one wins by default.
- **Impact:** every ordinary exit and every caught signal erases the record `-5` exists to produce,
  including the "header present, verdict absent" crash signal — on exactly the signals `-4` teaches
  the trap to catch. `-5` AC2/AC3 and `-3` AC7/AC8 go red the moment `-4` lands.
- **Fix:** as R2. While correcting it, narrow `-5` §4's bare "drop the trap" and its Rollout line to
  the same split, so the ownership is stated once in each file rather than implied twice.
- **Confirmed because:** verbatim quotation on both sides, and the two vocabularies genuinely
  collide — this is the same defect as R2 seen from the M2 sub-spec-agreement lens, kept separate
  because it supplies the `-3` AC7/AC8 join that R2 does not.

### R4 - HIGH - TOOL-aPacedTurnstile-5 §6 AC12 (and `-3` §6 AC11) against `-1` §2 S11

- **Claim:** `-1` S11 keeps "the two repointed rows in `memory/project/testsuite-count-waivers.txt`".
  Both `tools/run-gates.test.sh` and `tools/run-gates.evidence.test.sh` are rows in that shrink-only
  registry today, meaning they print no count and pin no floor. `-5` AC12 asserts both moved
  harnesses report counts at or above their floors, and `-3` AC11 asserts the same for the canary,
  while no scope item in `-1`, `-3` or `-5` adds a counter to either file.
- **Impact:** both criteria are false as written. Making them true without deleting the rows reds
  `tools/check-testsuite-counts.sh` the other way — a waiver naming a suite that now complies — so
  the set as it stands has no reachable green state for these two criteria, and that gate sits in
  both units' §7.
- **Fix:** pick one side and write it once. Either drop AC12 and AC11 to "exits 0 with the repointed
  waiver rows intact", or add the counters as a scope item in `-1` (which owns the move and the rows)
  with both waiver-row deletions in the same commit, and keep the criteria as written.
- **Confirmed because:** verified against the live registry, and this is round 1's F21 with no
  revision log in `-1`, `-3` or `-5` claiming it — the text is unchanged, so the "already fixed"
  refutation does not apply.

### R5 - HIGH - TOOL-aPacedTurnstile-5 §6 AC12 · `-3` §6 AC11 · `-1` §2 S11 (acceptance lens)

- **Claim:** same conflict, reached by asking which criteria cannot fail and which scope items carry
  none. The registry's own header states that a row naming a compliant suite reds as stale, so the
  two directions are mutually exclusive by design, not by accident.
- **Impact:** whichever way the builder goes, one graded artefact is wrong at DoD — either two
  acceptance criteria are unsatisfiable, or a bar leg reds on a stale waiver row that no spec deletes.
- **Fix:** as R4; the deletion and the counter must land in the same commit, which is why the work
  belongs to one unit rather than being split across `-3` and `-5`.
- **Confirmed because:** the registry, `check-testsuite-counts.sh`'s staleness branch and `-1` S11's
  day-one obligation were each read directly; kept separate from R4 because it is the lens that
  establishes there is no ordering of the two edits that is green at every commit.

### R6 - HIGH - TOOL-aPacedTurnstile-5 §8 first fork, the RESOLVED line

- **Claim:** the resolution ratifies "clear it each run" and states that a leftover file in this
  directory is the F2 blocker's false-GREEN class "which clearing is what closes". Both halves
  contradict the F2 fold-in the rest of the file now carries. S1 says the per-run uniqueness is
  "preserved deliberately, not incidentally" and that retention of older run dirs is bounded by a
  sweep — precisely the retention policy the resolution dismisses as unasked-for. §4 says the flat
  spelling is deliberately absent "and that is the whole of blocker F2". F2 is closed by the run id.
- **Impact:** a builder following the ratified answer restores the branch F2 named — a start-of-run
  clear with no failure branch, which on this platform can partially fail on an open handle or an AV
  lock and inherit the previous run's verdicts. AC14 cannot catch it: with the run id pinned and the
  directory cleared at start, the planted completion file is deleted, the leg executes, and the arm
  is green under both designs. It also erases the crashed-run evidence §1 says the unit exists to
  make readable, and leaves S1's sweep with no owner.
- **Fix:** rewrite the resolution to ratify what S1 says — per-run directories, nothing cleared at
  start, older run dirs bounded by a sweep after the verdict is written — and strike "which clearing
  is what closes", since the run-id uniqueness is the mechanism. If the sweep's bound is a real
  decision, state it and give it a criterion.
- **Confirmed because:** the rev-4 sweep ratified a pre-fold option set (round 1's own text quotes the
  old S1 as clearing the directory at start), so §8 now credits F2's closure to the wrong mechanism
  and re-licenses the branch the fold-in removed, with no arm able to tell the two designs apart.

### R7 - HIGH - TOOL-aPacedTurnstile-7 §2 S10 · §4 Files touched · §6 AC9

- **Claim:** the guard hole S10 closes has two carriers and S10 fixes one. `tools/gate-legs.json`
  holds gov's row for the kit/dogfood parity leg, but `tools/memory-tree/kit.toml` declares the SAME
  leg for deployment with an even narrower guard, while `kit-dogfood-parity.test.sh` validates a file
  under `memory/guides/`. `tools/govkit/govkit.py`'s emit verb copies a descriptor's declared guard
  verbatim into the target's manifest. S10 names only the leg's guard, §4 Files touched lists only
  `tools/gate-legs.json`, and AC9 observes only the canary over gov's manifest.
- **Impact:** the one hole the README says is closed inside this build stays open in the half that
  SHIPS. Nothing catches the divergence: govkit selfcheck joins descriptor gate legs to the manifest
  by name only, its guard classification never compares the two, and the run-gates canary only checks
  that a guard resolves to a tracked path. Since `-1` promotes run-gates to a deployable kit
  precisely so adopters run this bar, an adopter taking memory-tree plus run-gates receives a parity
  leg that skips when their own build-method guide moves — the wrong-merge-verdict inversion this
  unit exists to bound, exported rather than fixed.
- **Fix:** S10 names both carriers — gov's manifest row and the kit descriptor's gate-leg guard, which
  gains the guides directory — with the descriptor added to §4 Files touched and AC9 extended to
  assert it. Better, and the only thing that would have caught this: a govkit selfcheck arm joining a
  descriptor's declared guard to gov's manifest row for the same leg name.
- **Confirmed because:** both halves verified in the tree, including the emit verb copying the
  descriptor guard and the selfcheck joining by name only. Not covered by the deferred follow-up,
  which defers proving guards complete IN GENERAL, not this specific verified hole. HIGH rather than
  BLOCKER: gov's own bar stays sound, and the repair is one descriptor line plus an AC extension.

### R8 - HIGH - TOOL-aPacedTurnstile-7 §2 S9 · §4 Files touched · §6 AC7

- **Claim:** S9 says the safety property is rewritten "wherever it is stated" and then enumerates
  three carriers. The population is measurably larger and two of the missing carriers are PRODUCT:
  two bullets of `parallel-coding-governance.domain-rules.md` state the once-at-the-push-boundary
  guarantee and name the pre-push hook as the sole mandated full run; `memory/guides/BUILD-METHOD.md`
  states it together with its shipped source `tools/memory-tree/BUILD-METHOD.template.md`; and
  `memory/guides/SESSION-KICKOFF.md` states it a fourth time.
- **Impact:** the domain-rules checklist is what the charter says is run in every Tier-2 review, so
  gov's own reviewers keep grading against the guarantee this unit deletes, and every adopter
  receives it in the shipped rule set. No later pass catches it: AC7 greps exactly the three named
  files, the playbook-parity gate is structural and says so, the placeholder gate grades only the
  catalogue, and kit/dogfood parity compares live against template — leaving both build-method copies
  unedited keeps it green.
- **Fix:** derive the carrier population by measurement rather than enumeration — grep the claim
  across tracked product files and the guides — and name in S9 and §4 the two domain-rules bullets,
  the build-method guide WITH its template (edited as a pair and re-rendered, or kit/dogfood parity
  reds), and the kickoff guide. Give AC7 its negative-plus-positive pair per carrier.
- **Confirmed because:** every carrier was located and quoted at this base, and none is round 1's F42
  (that was the playbook template, now covered by AC7). The externalized half of a landed decision
  lives in the domain-rules file, so the enumeration silently retires half of a ratified record.

### R9 - HIGH - TOOL-aPacedTurnstile-1 §2 S10 · §4 Rollout · §7 Gates

- **Claim:** S10 claims to repoint "every live spelling of the old path" and lists six carriers; two
  live spellings under `memory/` are missing. `memory/guides/BUILD-METHOD.md` writes the merge bar's
  pre-move path in backticks, inside the hygiene check's present-tense population, so after the move
  it is an unresolved repo-path citation; its authored source is the memory-tree kit's build-method
  template, so the repoint must edit the TEMPLATE and re-render or kit/dogfood parity reds.
  `memory/guides/SESSION-KICKOFF.md` spells the pre-move path four more times, one of them in the
  manifest-audit watch line.
- **Impact:** the hygiene leg is UNGUARDED, so it runs on every bar: the single commit §4 Rollout
  insists on — "a half-moved runner has no green state" — lands RED at `-1`'s own landing, and the
  kickoff manifest check fails a second way on a watch pathspec matching no tracked file. §7's gate
  list omits the hygiene check, the parity test and the manifest check, so the unit's stated DoD
  cannot see any of it. The build-method repoint also turns out to be a shipped-kit-template edit
  rather than a records edit, which §4 Files touched does not carry.
- **Fix:** add both guides to S10 and to §4 Files touched, routing the build-method edit through its
  template with a re-render, add the three missing gates to §7, and state the enumeration as measured
  (a grep for the old path excluding the build and archive areas) rather than authored.
- **Confirmed because:** the citations were located by line, the present-tense population regex was
  read to confirm the guides are inside it, and the manifest-check branch that fails on an unmatched
  watch pathspec was read directly. The finding understated its own impact by one red.

### R10 - HIGH - TOOL-aPacedTurnstile-3 §6 AC6 · `-6` §2 S8 / §6 AC12 · `-7` §6 AC9, against `-1` §2 S1/S6

- **Claim:** `-1` moves the canary into the kit and declares it a gate-leg row, so an adopter's
  emitted manifest runs it in THEIR tree. Three siblings then key that same harness on gov's corpus,
  unconditionally: `-3` AC6 asserts every leg in the manifest carries a chunk from gov's declared SIX;
  `-6` requires the scan to resolve the known network-calling legs BY NAME and to print a dead-probe
  failure when its match set is empty; `-7` AC9 pins a gov leg name's guard. In an adopter tree the
  manifest is seeded empty and emitted from descriptors with no chunk key, and gov's legs do not
  exist, so all three red. `-3` §8 contradicts its own AC6 in the same file by keeping a catch-all
  chunk "in the kit for adopters", i.e. expecting adopter legs to carry no chunk.
- **Impact:** the kit `-1` exists to make deployable is red-on-arrival in a target — the
  pin-copied-from-another-corpus class `-1` §3 cites by name when it refuses to seed gov's leg names.
  `-1` AC1's claim that every shipped test runs to completion in the target tree cannot hold
  alongside these three, and the likely field repair — making the arms conditional — silently undoes
  the fix that made AC6 unconditional.
- **Fix:** split the harness the way the recall kit already splits. Gov-corpus-keyed arms — the six
  chunk names, the network-leg name set, the named guard pin — move to a gov-only file that is its own
  leg and is withheld from the kit payload; the shipped canary keeps only assertions true in any
  tree. Name the split in `-1` S1/S6 so the three siblings land their arms in the right file, and
  reconcile `-3` §8's adopter catch-all with AC6's scope.
- **Confirmed because:** the descriptor gate-leg emission path was read in `govkit.py`, today's
  canary was read and asserts only tree-agnostic properties, and the charter already records the
  recall kit's gov-only split with the reason that arms keyed on this repo's record ids are
  meaningless in an adopter's tree — settled precedent for exactly this.

### R11 - MEDIUM - TOOL-aPacedTurnstile-1 §8 fork B (RESOLVED) against §2 S8 · §4 Files touched · §6

- **Claim:** the resolution is "the default-selection line in this unit, with the selfcheck arm filed
  as its own govkit unit rather than built here". That line is real and concrete —
  `tools/govkit/registry.toml` declares a default selection of five kits, none of them this one — but
  no scope item asks for it. S8 enumerates the registry surgery exhaustively (add the entry, delete
  five rows, correct one clause) and §4 Files touched repeats the same closed list. No criterion
  observes it: AC3 runs selfcheck, AC9 checks what intake writes when it selects this kit.
- **Impact:** the pick exists to close the hazard the fork names — a target can receive the merge-bar
  hook without the merge bar, because a requires edge only orders a selection and pulls no missing
  kit in. A builder working from §2 and §6 does not add the line, no gate reds, and the hazard stays
  open with its detection arm deferred to a unit that was only filed because the line was supposed to
  ship here.
- **Fix:** add the default-selection edit to S8, add it to the registry row in §4 Files touched, and
  add a criterion — a plan with no explicit selection includes this kit, or a read-only assertion
  that the entry id appears in the default array. Rev-bump with the §9 line.
- **Confirmed because:** the registry file, S8, §4 and the whole of §6 were read; the obligation lives
  only inside §8, and the backlog row for the deferred selfcheck arm states in its own text that this
  unit "ships the default-selection line instead", so the deferral does not cover it.

### R12 - MEDIUM - TOOL-aPacedTurnstile-1 §8 fork 2 resolution (sub-spec-agreement lens)

- **Claim:** same defect reached by asking whether every unit's interface obligations are carried by
  a scope item. The fork's own text records why nothing else catches it: a requires edge only orders
  a selection and does not pull a missing kit in.
- **Impact:** the resolution commits the unit to work no scope item carries and no criterion grades,
  so it ships unbuilt and SILENTLY — the selfcheck exits 0 either way.
- **Fix:** as R11.
- **Confirmed because:** the backlog row for the deferred unit repeats the same assignment, so two
  records now say this unit ships the line and the unit's own scope says otherwise.

### R13 - MEDIUM - TOOL-aPacedTurnstile-1 §8 second fork, the RESOLVED line (acceptance lens)

- **Claim:** the third reading adds the mechanical proof that no existing arm can catch it. In
  `tools/govkit/govkit.py`, the selfcheck's unreachable-entry test compares against the set of all
  non-conditional entries, so a new entry named in no default set is never unreachable and the check
  exits 0 whatever the default array holds.
- **Impact:** this is round 1's F25 shape — a decision with a mechanism named in prose, no scope item
  and no observation — reintroduced by the resolution itself. The push-main descriptor declares no
  requires edge and claims the pre-push hook and its test, so a target can still receive the merge-bar
  hook with no merge bar.
- **Fix:** as R11. If the default set is the wrong home, say so and record which selection does reach
  it.
- **Confirmed because:** the selfcheck branch was read line by line and the descriptor's empty
  requires list verified; kept separate from R11 and R12 because it is the only one of the three that
  proves the gate cannot fail rather than that the scope is silent.

### R14 - MEDIUM - TOOL-aPacedTurnstile-3 §6 AC6 against §4 Rollout and §2 S8

- **Claim:** AC6 asserts unconditionally that every leg in the manifest carries a chunk from the
  declared six and that the chunks are contiguous, and S8 puts those arms in the runner commit. §4
  Rollout says that commit lands against the existing manifest order, "where every leg falls into the
  default chunk" — a manifest with no chunk keys, on which the arm cannot pass. The keys arrive only
  in the manifest commit, which the README sequences last.
- **Impact:** the canary is red from the runner commit until the build's final commit, spanning `-4`
  and `-7`, both of which run the canary in their own §7, and the pre-push hook blocks a red push —
  so the middle of the sequenced build cannot land. The cheapest field fix is to re-weaken AC6 to the
  conditional form the round-1 fix removed, silently undoing a folded finding.
- **Fix:** state in §4 Rollout that the arms grading the REAL manifest land in the same commit as the
  chunk keys and that the runner commit carries only fixture-driven arms; or move the key assignment
  into the runner commit and leave only the row reorder last — but then say so, since the key edit
  rewrites every row for the same merge-driver reason the reorder does.
- **Confirmed because:** AC6, S8 and §4 Rollout were read together and disagree on their face; loud
  rather than silent, which is why it is MEDIUM.

### R15 - MEDIUM - TOOL-aPacedTurnstile-7 §2 S2b predicate 7 · §4 Files touched, against §6 AC6c

- **Claim:** predicate 7 forces full "on any push-main retry after the first", but `tools/push-main.sh`
  keeps its attempt counter as a plain shell local and exports nothing; the hook is a separate process
  invoked by git push and cannot see it. §2 and §4 Files touched name only the hook and its test,
  while AC6c grades the behaviour through the lander's own suite. No spec in the set puts the export
  anywhere.
- **Impact:** predicate 7 has no input source, so alone among the eight rows it fails toward SCOPED
  when its signal is absent, contradicting §4's "Every predicate fails toward FULL".
- **Fix:** add the exported attempt marker in the lander's retry loop as a scope item and a
  files-touched row, and say plainly that an absent marker reads as "not a retry"; or derive the
  predicate inside the hook from the tip's shape — a merge whose second parent is not an ancestor of
  the recorded green — which needs no second file and cannot be lost.
- **Confirmed because:** the lander was read (the counter is local, the only channel to the hook is a
  contentless marker file) and no unit in the set touches it. Severity lowered from the raised HIGH
  because predicate 0 already forces full on the post-reconcile tree, so the claimed "the reconcile
  merge goes on being scoped" consequence is weaker than stated.

### R16 - MEDIUM - TOOL-aPacedTurnstile-4 §2 S10 · §4 Files touched, against `-1` §2 S12 and `-4` §3

- **Claim:** `-1` S12 explicitly declines this unit's leg key — "that unit adds its own key to this
  dossier when it lands" — which is the accepted half of round 1's F31 fix. `-4` never takes it: S10
  registers the new suite only in the manifest and the kit descriptor, §4 Files touched lists no
  dossier row, and §3's non-goal says the key "is claimed there" in the passive with no owner.
- **Impact:** `-4` adds a gate leg the codebase-map gate-leg inventory grades, so the map test —
  listed in `-4`'s own §7 — reds on the unclaimed key at `-4`'s landing, and the set does not say who
  repairs it. The obligation was assigned by one unit and accepted by none.
- **Fix:** extend `-4` S10 to add this leg's claim line to the run-gates dossier, add that file to §4
  Files touched, and reword §3's non-goal to name a separate dossier while accepting the claim line.
- **Confirmed because:** `-4`'s rev-2 log folds four round-1 findings and F31 is not among them, while
  §7 nevertheless runs the map test that reds on an unclaimed gate-leg key.

### R17 - MEDIUM - TOOL-aPacedTurnstile-3 §2 S2 and §4 Inventory, the default chunk assignment

- **Claim:** S2 says all 70 legs get an explicit chunk and the inventory claims six chunks over 70
  legs with every index claimed exactly once. The manifest carries 70 legs at base, but `-3`'s
  manifest commit lands LAST: by then `-1` has added two legs and `-4` has added one, so the file has
  73 rows at that commit.
- **Impact:** a builder assigning from the table leaves the three build-added legs with no chunk,
  which is precisely what AC6's unconditional arm reds on, and the per-chunk counts are wrong on the
  day they land. All three under-counted legs are added by units sequenced BEFORE this commit, so no
  later pass adds them.
- **Fix:** state the assignment over the manifest as it stands at the reorder commit, name the chunk
  each of the three build-added legs takes, and drop the frozen 70 in favour of "every leg in the
  manifest at this commit".
- **Confirmed because:** the manifest was counted at this base and the two siblings' files-touched
  tables read; this is the frozen-count rot class the charter already names in the govkit leg, where
  a spec twice stated a figure the tree then moved underneath.

### R18 - MEDIUM - TOOL-aPacedTurnstile-7 §6 AC10 against §2 S8 and §4 Files touched

- **Claim:** AC10 asserts the pre-push suite reports an executed assertion count no lower than its
  recorded floor. That suite is a row in the testsuite-count waiver registry today, so it has no floor
  and prints no count. S8 adds arms only; §4 Files touched carries no registry row.
- **Impact:** the criterion is unsatisfiable as written, and an implementation that satisfies it by
  adding a counter reds the count gate on the now-stale waiver row, which no scope item deletes.
- **Fix:** restate AC10 as "the count gate exits 0 with the suite's waiver row intact", or add the
  counter plus that row's deletion to S8 and to §4 Files touched.
- **Confirmed because:** verified in the live registry. Same class as R4/R5 on a third suite round 1
  did not check, so it is a new finding rather than a restatement.

### R19 - MEDIUM - TOOL-aPacedTurnstile-5 §2 S5 and §4 Files touched, against `-7` §2 S2b

- **Claim:** S5 makes the fingerprint "its OWN executable inside the kit, not as a function private to
  the runner", because `-7`'s predicate 0 has to compute the same digest from a git hook, and `-7`
  S2b says it computes it by CALLING that shipped helper. Neither spec spells the file's name or
  path. `-5` §4 Files touched lists no new file at all, and `-1`'s kit-dir layout — which does carry a
  row for `-2`'s profile table — has no row for it.
- **Impact:** the one interface in this build that both specs insist must have exactly one
  implementation is the only one with no identifier, against the spec template's rule to name things
  by repo identifier. `-7`'s builder has no path to call, which makes reimplementing the digest — the
  failure both specs warn about, and which fails toward FULL forever — the path of least resistance.
- **Fix:** name the executable in `-5`, add it as a row in §4 Files touched, and spell the same path
  in `-7` S2b and in `-1`'s kit-dir layout block.
- **Confirmed because:** both specs were grepped for a path and neither carries one; the template
  rule was read directly. Softened from the raised severity by S2b's explicit ban on a second
  implementation, which at least states the intent the missing name undermines.

### R20 - MEDIUM - TOOL-aPacedTurnstile-7 §4 The decision, predicate 6, against §2 S6 and S8

- **Claim:** predicate 6 — the lag constant set to anything that is not a decimal integer — is the
  only row of the eight-row forcing table with no acceptance criterion, while S8 declares "one arm per
  forcing predicate". Its reachability is also undecidable from the text: S6 makes the lag a SOURCE
  CONSTANT that no conf can supply, then hedges that if an environment value is honoured at all it is
  clamped and validated.
- **Impact:** predicate 6 is the fix for the left-shift class round 1 named — a numeric comparison on
  environment input. As it stands, a builder reading S6 as source-constant-only writes no predicate 6
  and every criterion stays green; a builder honouring the environment writes the env-settable lag S6
  argues against, also with no arm. Either way one row of the table carrying the unit's safety
  argument ships unobserved.
- **Fix:** decide in S6 whether the environment can supply the lag. If yes, add a criterion beside
  AC5 — a non-integer value makes the hook's own suite observe the full-run flag and the unusable-lag
  reason, plus the clamp. If no, delete predicate 6 from the table and state that the constant is
  validated by the hook's test at edit time.
- **Confirmed because:** the predicate-to-criterion mapping was built row by row and predicate 6 is
  the only orphan. Downgraded from HIGH because S8's blanket "one arm per forcing predicate" already
  obligates the arm even though §6 does not enumerate it.

### R21 - MEDIUM - TOOL-aPacedTurnstile-7 §2 S5, still uncovered

- **Claim:** S5's durable half gained a mechanism in the last revision — the reason is passed to the
  runner in the environment so it lands in the record's header as a declared key — and the join now
  resolves, since `-5` S2's key list carries the full-run flag and the reason it was forced. No
  criterion in either spec reads it back: the hook's criteria observe the PRINTED reason only, and
  `-5` AC1 reads the header for the run id alone.
- **Impact:** a stdout-only implementation satisfies every criterion in §6, so the half that makes the
  replacement property measurable ships unbuilt — and §4 rests the whole inversion on measurability,
  that the record makes "when did every leg last run, and on what sha" answerable.
- **Fix:** extend one of the hook criteria, or add one: when the hook forces full for a known reason,
  that run's header carries the same reason string, asserted in the hook's suite or as a header arm in
  `-5`'s set.
- **Confirmed because:** round 1's F25 fix asked for both the mechanism and a criterion reading it
  back from the record; only the mechanism landed, and `-5`'s canary pins the MANIFEST key set, not
  the header's, so nothing else observes it either.

### R22 - MEDIUM - TOOL-aPacedTurnstile-3 §2 S9 and §4 Files touched, still uncovered

- **Claim:** S9's kickoff-guide edit has no acceptance criterion and no gate in §7 reads that file's
  content. The charter chunk-contract sentence in §4 Files touched is in the same state: §7 carries no
  drift-report check, and the charter signal that does exist joins leg SCRIPT PATHS, not prose.
- **Impact:** every sibling arms its doc edit — `-1` through the drift signal, `-2` by grep, `-7` by a
  whitespace-insensitive search across three carriers — and this unit arms neither of its two. The
  kickoff guide is the file the kickoff skill loads at hand-back, so an operator reads a truncated
  per-chunk verdict list as a complete one and does not learn that a red chunk halts the run.
- **Fix:** add a criterion in the sibling's shape: a grep for the halt sentence and for the
  chunk-contract sentence in the kickoff guide returns non-zero counts, and the same positive grep for
  the chunk-contract sentence in the charter.
- **Confirmed because:** §6 was read end to end with no observation of either file, §7's seven gates
  read neither, and this is round 1's F33 verbatim while the revision log folds six other findings and
  not this one.

### R23 - MEDIUM - TOOL-aPacedTurnstile-2 §6 AC11 against §2 S8

- **Claim:** the rewrite that fixed three round-1 findings dropped the width-formula half of S8. S8
  names two claims to repair — the stated width formula and the older serial-to-concurrent figure —
  and AC11 now observes only the figure, negatively, plus the measured pair positively. The charter
  still states the width formula this unit falsifies, and nothing in §6 or §7 observes it: the
  playbook-parity gate grades the playbook files, not the charter, and the drift-audit charter signal
  joins leg script paths.
- **Impact:** S8 can land half-done with AC11 green — the exact defect round 1 raised, relocated from
  the figure half to the formula half by the fix for it. The charter then states a width formula the
  runner no longer uses, which is the claim this unit exists to falsify.
- **Fix:** add to AC11 the negative that is actually in the file — a count of the backticked formula
  returning zero — paired with a positive grep for the replacement sentence naming the profile table
  as the width's source.
- **Confirmed because:** both charter lines were located at this base; round 1's stated fix was to grep
  the formula string that is in the file, and that half did not land.

### R24 - MEDIUM - TOOL-aPacedTurnstile-5 §2 S3 against §5 security, and §6

- **Claim:** S3 now requires the retargeted per-leg output copy to take "the same redaction and the
  same restrictive mode the existing per-leg log already has". §5 still reads that the existing
  redaction is untouched and "the new files carry no command output" — the opposite claim, and false
  the moment S3 lands. No criterion observes the redaction, the mode of the durable output file, or
  the mode of the record directory.
- **Impact:** §5 is the checklist a builder grades the security line against, so the file that now says
  no masking is needed is the one they read, and nothing reds if the masking is skipped. That is the
  credential leak round 1 named, with the scope item fixed and both the checklist and the criteria
  still pointing the other way.
- **Fix:** correct the §5 security line to match S3, and add a criterion: a fixture leg emitting a
  token the runner's redaction masks leaves only the masked form in the durable per-leg output, with
  that file's mode and the directory's mode asserted in the evidence suite.
- **Confirmed because:** the contradiction is between two sections of one file, and the revision log
  claims the round-1 finding folded — so it is half-closed, in the half a builder reads.

### R25 - MEDIUM - TOOL-aPacedTurnstile-2 §2 S6 and S7 against §6

- **Claim:** S6 declares four refusals and S7 says the canary's arms cover "every refusal". §6 arms
  two — a profile name resolving to no row, and an unknown knob key. The malformed-row refusal, which
  §4's table promises exits 2 naming file and line number, and the no-row-matches refusal have no
  criterion. The second is also unreachable against any table keeping §4's mandatory catch-all last
  row, so an arm for it needs a fixture table without one, which no criterion says to build.
- **Impact:** §4 states why these are refusals rather than fallbacks — a silently ignored knob is a
  knob the operator believes they set — and the table is the declared home for every future knob, so a
  malformed row skipped instead of refused is the failure that matters and nothing observes it.
- **Fix:** add a criterion for a malformed row (exit 2 naming the file and the line number, in the
  canary) and one for a fixture table with no catch-all row (exit 2 rather than falling through).
- **Confirmed because:** the four declared refusals were matched against the thirteen criteria one by
  one; two have no arm and one of those is unreachable without a fixture no criterion asks for.

### R26 - LOW - TOOL-aPacedTurnstile-7 §7 Gates, the last entry

- **Claim:** §7 still ends with the full-bar command spelled at the pre-move path, while §4 Files
  touched, AC9 and §7's own third entry all use the post-move path. The revision log records the
  round-1 finding as folded — "the gate list is repointed past the move" — but only one of the two
  entries moved, and the one left behind is the full-bar command this unit exists to change.
- **Impact:** `-7` lands seventh; the path in its own DoD gate list has not existed since the first
  commit of the build, and §4 and §7 of one document disagree on the same file. It is the only
  remaining live mis-spelling in the set, so a reader trusting the revision log believes the class is
  closed.
- **Fix:** repoint the full-bar entry, logged as a revision line. §10's citation of the pre-move
  runner reads as a citation of the seam at base and can stay.
- **Confirmed because:** the line was read at its position; a half-folded finding, not a fixed one,
  though the residue is a single stale token in a command that fails loudly.

### R27 - LOW - TOOL-aPacedTurnstile-1 §2 S5

- **Claim:** S5 calls the two-space tail "the output contract" that `-2`, `-3` and `-5` all extend.
  `-5` adds no stdout verb — its scope writes header, per-leg rows, verdict and ledger files, and its
  §3 states it changes no verdict. The fourth report verb is `-6`, which cites this contract by name,
  as `-2` and `-3`'s chunk verb do.
- **Impact:** the contract's own owner mis-lists its dependents by one, so a reader checking that every
  extender conforms checks a unit that extends nothing and misses the one that does. The README's
  matching sentence says only "the other three" and cannot correct it.
- **Fix:** `-1` S5 should read `-2`, `-3` and `-6`.
- **Confirmed because:** all four units' scope sections were read for a report verb; cosmetic, but
  factually wrong in the section that defines the contract.

### R28 - LOW - TOOL-aPacedTurnstile-6 §6 AC6

- **Claim:** AC6 states no precondition, unlike its neighbour AC1, which specifies a green run
  repeated on an unchanged tree. On a cold ledger both of AC6's clauses pass by finding nothing — the
  fixture-passes-by-finding-nothing class this build names elsewhere.
- **Impact:** AC6 is the only criterion guarding the opt-in default, and the default is §4's boundary
  rule that an advisory input may cause less work only on an opt-in, non-authoritative run.
- **Fix:** state the precondition AC1 already states — an immediately preceding green run whose rows
  would match this run's keys — and make the control that same tree run with the ledger removed, so a
  leaked default shows up as reuse verbs on the subject run's stdout.
- **Confirmed because:** downgraded from the raised severity: the finding overstated the control as
  identical to the subject, since the manifest does carry reuse-relevant state, and a leaked default
  over a WARM ledger would in fact red the comparison. The real gap is only the unstated precondition.

### R29 - LOW - TOOL-aPacedTurnstile-3 §8 second fork, the RESOLVED line

- **Claim:** the resolution gives as its reason that the contiguity arm is what makes an unclaimed leg
  visible — the reasoning round 1 refuted by construction, since a leg with no key falls into a
  default chunk and one or two unclaimed legs form a default chunk that is trivially contiguous. AC6
  was rewritten to carry the real assertion, and the resolution does not cite it.
- **Impact:** the ratified record names a mechanism that cannot fail as the protection, so a later
  editor trimming AC6 back toward its contiguity clause would believe they were keeping the guard §8
  describes.
- **Fix:** restate the reason as AC6's unconditional every-leg-carries-a-chunk assertion, and keep
  contiguity for what it actually buys — report order equalling manifest order.
- **Confirmed because:** the round-1 fix had two halves and only the criterion half appears in the
  revision log; documentational only, hence LOW.

## Refuted

- `-2` §8 fork B, the OFF half of the timeout knob unarmed — killed: the shipped rows' values are
  data, not behaviour, and the full bar is their observation (AC11 records the measured wall-clock
  pair under the shipped table, which a firing timeout would move); pinning shipped values would
  freeze the table §4 declares as the home for every future knob.
- `-7` §8 fork A, the lag default `10` stated only in §8 and the README — killed: a ratified §8 answer
  is binding text by the build method, which is the premise this whole audit rests on, and a
  parameterised criterion is the right shape for a tunable constant; an arm hardcoding the value would
  red the first time it is tuned.
- `-4` §8 fork B, "every run takes the ticket" observed by no criterion — killed: AC8 and AC9 are
  single-runner arms asserting the beacon is RELEASED on a signal and at a fail-fast halt, and a run
  that skipped the claim loop has no beacon to release, so the unconditional ticket is observed.
- `-5` §2 S5, the fingerprint executable named nowhere — killed as a duplicate; recorded once as R19,
  which carries the same claim with the sibling join `-7` S2b spelled out.
- `-5` §4 Data model, "Every path below sits under the PER-RUN directory" false for two of five paths —
  killed: both exceptions are spelled with their own full `<git-dir>/` prefix in the same section, so
  no reader can be misled about where they live and no decision hangs on the sentence.
- `-5` §2 S1 exclusive create versus AC14's planted file — killed: S1's sentence is about failure
  PROPAGATION, that a failed create aborts the run as the scratch-dir create already does, not about
  exclusivity semantics; the run id is unique per run, and AC14's pre-existing directory is
  manufactured by the test seam it names.
- `-7` §6 AC9's second clause not observable in the named harness — killed: guard matching is a pure
  decision over a changed-path list, so the canary can drive it with a synthetic changed set inside
  its own scratch repo without re-entering the real bar or executing the real leg.
- No `guard` stated for the three manifest rows this build adds — killed: an unstated guard means an
  UNGUARDED leg, which runs on every bar, and the charter already states a guard can only ever scope a
  non-authoritative run. The omission defaults toward more work, not less, so it is a preference, not
  a defect.
