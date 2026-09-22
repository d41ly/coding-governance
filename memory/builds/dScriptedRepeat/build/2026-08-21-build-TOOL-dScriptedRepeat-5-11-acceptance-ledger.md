# dScriptedRepeat units 5, 6, 7, 9, 10, 11 — the acceptance ledger

**Serves:** journal TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11

Node `d`, 2026-08-21, after the round-1 diff review's fold. One line per numbered criterion, naming
the observation that answered it.

**Written LAST, and that is the finding.** Units 6 and 7 shipped their `dod_met` branches with no test
arm at all, so writing this ledger meant writing fourteen arms first — and those arms found three
things a green bar had certified: the per-piece join that did not exist, the set join that accepted a
verdict for an undeclared leg, and `pieces-complete` being overridable when the spec that introduced
it had ratified the opposite. A ledger compiled from the specs rather than from observations would
have recorded all three as met.

**Round 2 re-judged every one of these repairs and blocked on two of them**, both in code written to
close a round-1 finding: the new `piece_checks` parse had no trailing-comment strip while its sibling
did, and `--counts` was pinned per-field so one field stayed on the working tree. The criteria below
still hold — they name observations, and every observation still reproduces — but the mechanism under
AC1 of unit 5 and AC4 of unit 6 is the round-2 one, not the round-1 one.

**Round 3 re-judged the round-2 fold and blocked again**, and its most useful finding was about this
ledger's own evidence rather than about the code: three of its six top findings were GATES THAT COULD
NOT FAIL, written in the round-2 fold to hold the round-2 repairs. Check 28's answer arm asserted only
that the parse was empty, so a parser returning nothing for every input scored correct; check 28's
template loop reached two of the block's ten keys; and the `--counts` behavioural arm produced
byte-identical output pinned and unpinned. Every criterion below still names an observation and every
observation still reproduces — but three of them were being answered by an arm that had never been seen
to fail, which is the same green-by-absence the ledger was written to end. The round-3 fold staged a RED
for each before re-arming it. The mechanism under unit 5's AC1 and unit 6's AC4 is now the round-3 one.

**Round 4 found three blockers in that fold, and one of them is about this ledger rather than the
code.** Round-3's `GITSHOW` repair NEVER LANDED: the function was byte-identical at both ends of the
range while the commit message, spec 5 rev-9 and the paragraph above all recorded the pin as shipped.
Three records, one fix, no fix — and 92 gate legs could not see the difference, because nothing
compared a claim against a file. The round-4 fold lands the pin and adds check 28c, which enumerates
every sha dereference in the kit and reds an unpinned one, so that particular divergence now costs a
red bar rather than a review round. The two structural gates beside it (28a, the refusal must be read
at every call site; 28b, every template key bound to the parser its real reader calls) were each
observed RED against the live tree before the fixes went in, which is the discipline this ledger's own
preamble was written about.

**Round 5 blocked on the fold again, and its finding was about the three gates round 4 added.** All
three were instance gates: 28a whitelisted any line carrying `||`, so the discard it existed to catch
came back spelled `|| true`; 28b was a fixed-string search that matched nothing over all ten template
keys; 28c matched only lowercase `git`, so its whole live population was the one already-pinned line it
exempts while thirty wrapper-routed reads stayed invisible. Each had been observed RED against the live
tree before the round-4 fixes went in, which is exactly what made them look armed — redding on the
instance in front of you is not the same claim as covering the class, and this ledger now records the
difference. The round-5 fold rewrites all three over a DERIVED kit-source population and arms each with
eight staged breaks and two controls, the controls being the half that proves a tightened rule has not
simply traded a false green for a false red.

Suite counts at the time of writing: driver 680, leg 405, playbook 90, cross-component 19.

## TOOL-dScriptedRepeat-5 — the per-piece record

**Evidences:** TOOL-dScriptedRepeat-5
- AC1 — `check-playbook.test.sh` — the census control returns `verified 2` over two hash-joined records each carrying a PASS for the declared leg. Post-fold this requires the `piece_checks` join; pre-fold it required only the absence of a FAIL.
- AC2 — `check-playbook.test.sh` — appending to a piece after its record moves it to `stale 1`, asserted as a whole census line so a second column cannot move unnoticed.
- AC3 — `check-playbook.test.sh` — hiding a record moves its piece to `unrecorded 1`.
- AC4 — `check-playbook.test.sh` — hiding a piece whose record survives reports `orphan record`, the reverse direction.
- AC5 — `check-playbook.test.sh` — flipping a verdict to FAIL moves the piece out of verified into `failed 1`.
- AC6 — `DEAD PROBE` — the zero-piece grain reports a dead probe rather than a clean census, armed in the leg self-test.
- AC7 — `check-playbook.test.sh` — the whole census runs in a scratch tree asserted to contain no run-state file, which is the attended path's only gated surface.
- AC8 — `unattended.test.sh` — `--record-piece` stages its record and no-ops on re-issue, both directions armed.
- AC9 — `check-playbook.sh` — a stale piece is reported and does not red the leg; only `--close` blocks on it.
- AC10 — `unattended.test.sh` — a piece at `content/pieces/pièce-é/index.md` records, joins, and the record names the path back byte for byte. No arm existed before this ledger; the claim rested on reading the `tr '/' '~'` transform rather than running it.

## TOOL-dScriptedRepeat-6 — `pieces-complete`

**Evidences:** TOOL-dScriptedRepeat-6
- AC0 — `skipped — pieces-complete is scoped to recipe-mode runs` — a `prompt`-mode close announces the skip. The announcement existed and reached nobody until unit 11's fold: `verb_close` printed `DOD_OUT` under the unmet arm only.
- AC1 — `unattended.test.sh` — a recipe close over zero pieces blocks on the vacuity guard.
- AC2 — `unattended.test.sh` — a piece edited after its record blocks with the staleness message.
- AC3 — `unattended.test.sh` — a tree holding pieces recorded against another run blocks on vacuity, and stops blocking once this run's pieces exist. Run membership is derived from each record's own `run:` line.
- AC4 — `unattended.test.sh` — two pieces, each hash-joined and each recording a PASS for the declared leg, do not block. The passing direction, without which every red arm is satisfied by an item that blocks on anything.
- AC5 — `unattended.test.sh` — a hash-fresh piece recording FAIL blocks with a message asserted DISTINCT from AC2's.
- AC6 — `unattended.test.sh` — the same run-scope arm as AC3; a second run is not answerable for the first run's pieces.
- AC7 — `--override pieces-complete` — refused, naming `--abort` as the honest exit. **Ratified by this spec and never implemented**; only the authorization item was non-overridable. The driver now holds a declared `DOD_NO_OVERRIDE` set.
- AC8 — `check-unattended.test.sh` — a `CORE_FLOOR` declared below the kit's own core count reds, and the slack arm covers both halves of the pin.

## TOOL-dScriptedRepeat-7 — `set-checks-recorded`

**Evidences:** TOOL-dScriptedRepeat-7
- AC0 — `skipped — set-checks-recorded is scoped to recipe-mode runs` — the sibling term zero, armed with AC0 above and asserted to print exactly twice.
- AC1 — `unattended.test.sh` — a set record carrying a PASS for every declared check does not block.
- AC2 — `unattended.test.sh` — a declared set check with no verdict blocks. Pre-fold this passed: the item required only that a record EXIST and carry no FAIL, so one `NA` on an undeclared leg satisfied it.
- AC3 — `unattended.test.sh` — a declared set check recording FAIL blocks with its own message, distinct from AC2's.
- AC4 — `check-playbook.sh` — a `CHECK`-tagged entry is reported and never redded; the leg header states the split and check 25 gates that it keeps stating it.
- AC5 — `unattended.test.sh` — re-recording a piece after the set verdict blocks with the SUPERSEDED message. The `set:` member list had no reader at all until this fold.
- AC6 — `unattended.sh` — `set_checks` declaring a null is a declared null and passes, matched against a TRIMMED value; the kit's own template line `set_checks   = []    # …` did not match before the fold.
- AC7 — `unattended.test.sh` — with N of one, set checks still run: a FAIL on the single-piece run blocks.

## TOOL-dScriptedRepeat-9 — the `proposal` kind

**Evidences:** TOOL-dScriptedRepeat-9
- AC1 — `proposal recorded against step F4` — the row lands in the parked region and is staged.
- AC2 — `proposal already recorded, unchanged` — an exact-line compare, and the same amendment at a different step is a second row.
- AC3 — `unattended.test.sh` — a proposal changes nothing the close blocks on, asserted as a DIFFERENCE across a close that is unmet for unrelated reasons.
- AC4 — `--propose requires --step` — refused, and the refusal writes nothing.
- AC5 — `· noted 1` — `--status` counts proposals apart from parked decisions. The field was `proposals` until the merge added two more unowed kinds; a label naming one of three is wrong about the other two.
- AC6 — `unattended.test.sh` — every verb carrier is joined to the ONE declaration, iterating the driver's own `VERBS_SLUG` rather than a list typed in the test.

## TOOL-dScriptedRepeat-10 — the start paths

**Evidences:** TOOL-dScriptedRepeat-10
- AC1 — `adopt-unattended.test.sh` — the render carries no surviving `{{…}}` and no uppercase angle-bracket placeholder, both checked by SHAPE rather than by a list of names.
- AC2 — `check-unattended.test.sh` — the directive registry and the Skill table are joined in both directions, each with a vacuity guard ahead of the comparison.
- AC3 — `check 24` — `AUTH_MODES` and the routing table are joined both ways, with two vacuity arms. This closes unit 1's F2.
- AC4 — `unattended.test.sh` — the example conf's `DIRECTIVES_FLOOR` is asserted equal to the driver's own count, and the leg's slack arm covers the installed conf. Growing the registry by two forced both to 15 or red; no new arm was needed and that is recorded so nobody adds a third.
- AC5 — `--waive playbook-followed` — refused on a run of another mode and ACCEPTED on a `recipe`-authorized one. Both directions, because an arm naming one scoped member twice is what left the second unenforced.
- AC6 — `check-playbook.test.sh` — the attended path's records are read with no run-state file anywhere in the tree, asserted rather than assumed.
- AC7 — `check 25` — the content-scope rule is labelled a CHECK and denies its own machine half, greped as literals because a heading survives a gutted body. Unit 8's withdrawal is what made the denial true.

## TOOL-dScriptedRepeat-11 — the creation path

**Evidences:** TOOL-dScriptedRepeat-11
- AC1 — `check-playbook.test.sh` — a tracked playbook is graded with no build README naming it, asserted over a scratch tree whose `memory/builds` is empty.
- AC2 — amended rev-6 — the criterion named unit 8's scope refusal, which was withdrawn unbuilt. Nothing to observe, and nothing was faked.
- AC3 — `check-playbook.test.sh` — eleven staged breaks each red with their own check number and message, so a playbook failing the canon cannot land.
- AC4 — `preflight OK` — a `recipe` run whose build README names a playbook committed earlier resolves it at BASE.
- AC5 — `does not resolve at the pinned BASE` — a create-and-follow run is refused, and the arm runs under BOTH scope values over one tree. The spec predicted `published` would not refuse; the arm was written and the prediction was wrong.
- AC5b — `anchor-kind: run-branch` — a run authoring BOTH its build folder and its playbook under `published` is refused by nothing. That is the state that is genuinely unprotected, and it is narrower than the spec claimed.
- AC6 — `unattended.test.sh` — both piece-scoped items are MET and ANNOUNCE the skip on a `prompt`-mode close, asserted to print exactly twice so one item cannot inherit the other's text.
