# TOOL-aPacedTurnstile-7 — the push boundary scopes to the diff, and "every leg" becomes a bounded obligation

**Status:** OPEN · rev-7 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

`.githooks/pre-push` exports `GATE_FULL=1`, so every landing runs all 70 legs and pays a measured
873 s — a records-only landing included, at 14x the 62 s its own guards would have cost. Scope the
push boundary to the diff, and replace the property that forcing bought with a bounded, recorded
obligation instead of deleting it.

## 2. Scope (IN)

- **S1** — `.githooks/pre-push` stops exporting `GATE_FULL=1` unconditionally; it decides.
- **S2** — the hook forces a full run when the run record's last full green is absent, is not an
  ancestor of the pushed tip, or is more than `GATE_FULL_MAX_LAG` commits behind it.
- **S2b** — the hook forces a full run when the record's TREE fingerprint does not equal a fresh
  fingerprint computed AT THE RECORDED SHA (predicate 0), and when the pushed tip is a merge whose
  second parent is not an ancestor of the recorded green (predicate 6). **That population is WIDER
  than the reconcile retry that motivated it, and round 3's T12 is why this now says so.** Every
  build landing on the default branch here is a merge commit, so the row fires on any first-attempt
  landing whose recorded green was not earned on that exact second parent — not only on a retry. The
  row is kept at that width, because a merge tip the record does not cover is exactly the case the
  record cannot speak for; what changes is that the reason string names the real condition and AC6c
  gains the negative half, so a row this broad cannot fire unconditionally without an arm noticing. It computes that fingerprint by CALLING `TOOL-aPacedTurnstile-5`'s shipped
  `tools/run-gates/gate-fingerprint.sh` **in its AT-A-REV form, `gate-fingerprint.sh <recorded-sha>`**
  — the form that unit's S5 declares, whose working-tree components are supplied empty and which is
  therefore EQUAL to the no-argument form on a clean tree, which is the only tree S7 lets a record
  be written from. The argument is the point: the no-argument form digests the live worktree, so
  calling it from a pre-push hook takes the fingerprint at the pushed tip, which is round 2's
  blocker verbatim. It is never reimplemented — two implementations of
  one digest disagree silently and then force full forever, which reads as caution rather than as the
  defect it is.

  **Predicate 0 joins at the RECORDED sha, not at the tip, and round 2's blocker R1 is why.**
  `TOOL-aPacedTurnstile-5` defines the digest over the committed tree object, so it moves on every
  commit; joined against the TIP it fires on every push whose tree is not identical to the commit the
  green was earned on, which is exactly the population predicates 3 and 4 exist to admit. That
  spelling made the scoped path unreachable, predicates 3-6 dead code, and AC1 and AC6b mutually
  unsatisfiable on a real push — while both arms, being fixture-built, stayed green. What predicate 0
  buys in its corrected form is stated rather than implied: it detects a record whose stored digest no
  longer describes the tree at the sha it names — a hand-edited record, or an object store rewritten
  under that sha. It does NOT detect a dirty working tree — true of the AT-A-REV form, whose
  working-tree components are empty by construction, and NOT of the no-argument form, which is one
  more reason the argument is named rather than left to a builder. The dirty-tree hole is closed
  elsewhere: `TOOL-aPacedTurnstile-5` S7 refuses to write the record at all unless the tree was
  clean at start. Predicate 0 is not the clean-tree assertion and this spec no longer
  claims it is.

  **Predicate 6 is derived from the tip's SHAPE and not from the lander.** The first spelling forced
  full "on any `push-main` retry after the first", and the lander keeps its attempt counter as a plain
  shell local that it exports nowhere; the hook is a separate process git invokes and cannot see it,
  so alone among the rows that predicate would have failed toward SCOPED when its signal was absent —
  against §4's "every predicate fails toward FULL". The retry reconciles with origin, which produces a
  merge commit, so the hook derives the same fact from the commit it is already given.
- **S3** — the hook forces a full run when the pushed diff touches `tools/gate-legs.json`, the file
  in which a guard can be narrowed.
- **S4** — the hook forces a full run when the recorded leg-manifest fingerprint differs from
  `git hash-object tools/gate-legs.json` at the pushed tip.
- **S5** — the decision and its reason are printed on one line, and passed to the runner in the
  environment so it lands in the record's header as a declared key. The first draft said "written to
  the run record" with no mechanism, which contradicted this unit's own non-goal of not owning the
  record format. The reason that survives is that one: the record's format and writer belong to
  `TOOL-aPacedTurnstile-5`, so the hook declares the value and that unit's S2 key list carries it.
  An earlier revision also cited the record's start-of-run reset, a mechanism `-5` no longer has —
  its §8 now ratifies per-run directories with nothing cleared at start (round 3's T18).
- **S6** — `GATE_FULL_MAX_LAG` is a SOURCE CONSTANT in `.githooks/pre-push` with its justification in
  a comment beside it. No sibling creates a runtime conf the hook could read: the kit descriptor is
  TOML a bash hook cannot parse, and the profile table's header forbids a coverage knob by rule. It
  is deliberately NOT the `GOV_DEFAULT_BRANCH` shape, which the spec audit showed does not exist as
  described and would be fail-OPEN here — an environment value that widens the lag leaves no diff
  behind, which is the defeatable class `TOOL-aStandingWrit-4` recorded in this very hook.
  **The environment supplies it NOWHERE, and round 2's R20 is why the hedge came out.** The first
  spelling made it a source constant and then hedged that an environment value, "if honoured at all",
  would be clamped and validated — which left the reachability of the forcing row guarding it
  undecidable from the text: a builder reading the constant as final writes no such row and every
  criterion stays green, and a builder honouring the environment writes the very env-settable bound
  this item argues against, also with no arm. The row is therefore deleted from §4's table rather than
  left unobserved, and the constant is validated by `.githooks/pre-push.test.sh` at EDIT time — an arm
  asserting the literal in the hook is a decimal integer, which reds on the edit that breaks it
  instead of at a push nobody is watching.
- **S7** — the hook exports the no-halt flag `TOOL-aPacedTurnstile-3` defines, unconditionally and
  independently of its own scoped-or-full decision, so a landing always gets a complete verdict list
  instead of stopping at the first red chunk.
- **S8** — `.githooks/pre-push.test.sh` gains one arm per forcing predicate, one arm proving the
  scoped path actually scopes, one proving the no-halt export, and one asserting the lag constant in
  the hook is a decimal integer at edit time (S6). It also gains an EXECUTED ASSERTION COUNTER in the
  agreed shape, and this unit DELETES that suite's row from
  `memory/project/testsuite-count-waivers.txt` in the same commit. Both halves or neither: the
  registry reds on a waiver naming a suite that now complies, so a counter without the deletion and a
  deletion without the counter are each a red, and AC10 was unsatisfiable while the row stood
  (round 2's R18).
- **S9** — the safety property is rewritten wherever it is stated, and the population is MEASURED
  rather than enumerated: a whitespace-insensitive search for the claim across tracked product files
  and the guides selects the carriers, and the search itself is what §6 grades. At this base it
  selects seven, of which the first draft named three — the missed four are why this item stopped
  enumerating. `AGENTS.md`. The playbook template's diff-scope line.
  `tools/run-gates/run-gates.sh`'s own header comment, which `TOOL-aPacedTurnstile-1` ships into the
  kit and therefore to adopters. **Two bullets of `parallel-coding-governance.domain-rules.md`**,
  which state the once-at-the-push-boundary guarantee and name the pre-push hook as the sole mandated
  full run — PRODUCT, received by every adopter, and the file the charter says is run in every Tier-2
  review, so leaving it would have gov's own reviewers grading against a guarantee this unit deletes.
  **`memory/guides/BUILD-METHOD.md` TOGETHER WITH its shipped source
  `tools/memory-tree/BUILD-METHOD.template.md`** — edited as a pair and re-rendered, because
  `kit-dogfood-parity.test.sh` compares exactly those two and reds on a one-sided edit. And
  **`memory/guides/SESSION-KICKOFF.md`**, which states it a fourth time.
- **S10** — close the one guard hole that is verified still open, named in
  `memory/builds/cKeyedLaunchpad/README.md` park 2 and in `cBriefedPilot-15`: the kit/dogfood parity
  leg's guard omits `memory/guides/`, which is a file pair it actually validates. **The hole has TWO
  carriers and both are closed here.** gov's own row in `tools/gate-legs.json` is the one an earlier
  draft fixed; `tools/memory-tree/kit.toml` declares the SAME leg for DEPLOYMENT with an even
  narrower guard, and `govkit.py`'s emit verb copies a descriptor's declared guard verbatim into the
  target's manifest. Fixing only gov's row leaves the half that SHIPS open, so an adopter taking
  memory-tree plus the promoted run-gates kit receives a parity leg that skips when their own
  build-method guide moves — the wrong-merge-verdict inversion this unit exists to bound, exported
  rather than fixed. Nothing catches the divergence today: govkit's selfcheck joins descriptor gate
  legs to the manifest by NAME only and never compares the two guards.

## 3. Non-goals (OUT)

- Changing what any leg asserts. Widening guards in general stays out: S10 closes the ONE hole that
  is verified open and recorded twice, and does not open a survey of the other 41.
- The run record's format, location and writer. That is `TOOL-aPacedTurnstile-5`; this unit is a
  consumer and states only what it reads.
- Removing `GATE_FULL`. It stays as the manual escape and as the mechanism this unit sets.
- Making the bar faster. Scoping changes which legs run, never how fast a leg is.
- Proving guard completeness. Named as the follow-up that would retire this unit's residual risk.

## 4. Design

### The property, before and after

Today the hook's own comment states it. `GATE_FULL` marks "THE run that must be total: the self-test
legs are diff-scoped on earlier runs, and if that scoping reached here no run would ever execute
every leg against the tree that actually lands." That is accurate, and two records already lean on
it. `memory/builds/cBriefedPilot/spec/2026-08-14-spec-cBriefedPilot-15.md` names a leg whose guard
omits `memory/guides/BUILD-METHOD.md` and is caught only at the push boundary.
`memory/builds/cKeyedLaunchpad/README.md` refused to widen a guard because `GATE_FULL=1` covers it.

The replacement property, as it will be written into `AGENTS.md`: every leg runs against a tree that
lands at least once every `GATE_FULL_MAX_LAG` commits, and always when the leg set or its guards
move. That is strictly weaker. It is also, unlike today's property, MEASURABLE — the record makes
"when did every leg last run, and on what sha" answerable, which nothing answers today.

### Data model

The hook reads four fields from the run record and nothing else: the sha of the most recent run in
which every leg ran and passed, that run's leg-manifest fingerprint, its TREE fingerprint, and a
schema version it can refuse. The tree fingerprint is what predicate 0 joins against a fresh
fingerprint computed at the RECORDED sha. The dirty-tree hole an earlier draft gave as this join's
justification is closed elsewhere and is not claimed here: `TOOL-aPacedTurnstile-5` S7 refuses to
write the record at all unless the tree was clean at start, so a green earned on a dirty tree never
becomes a record. What survives for predicate 0 is narrower and is worth stating exactly — a stored
digest that no longer describes the tree at the sha it names, which is a hand-edited record or an
object store rewritten under that sha. Field names are owned by `TOOL-aPacedTurnstile-5`, and the
digest is computed by that unit's `tools/run-gates/gate-fingerprint.sh` and by nothing else — in its
AT-A-REV form, `gate-fingerprint.sh <recorded-sha>`, which that unit's S5 declares and which is
EQUAL to the runner's no-argument form on the clean tree S7 requires before a record exists at all.
The no-argument form here would digest the live worktree, which is the pushed tip, which is round
2's blocker.

### The decision

Evaluated in order; the first hit forces and stops.

| # | predicate | reason string |
|---|---|---|
| 0 | the record's tree fingerprint does not equal a fresh fingerprint computed AT THE RECORDED SHA | `the record describes a different tree` |
| 1 | no run record, or it does not parse, or its schema version is unknown | `no usable run record` |
| 2 | recorded manifest fingerprint differs from `git hash-object tools/gate-legs.json` | `the leg manifest changed` |
| 3 | `git merge-base --is-ancestor` of recorded sha against the tip is non-zero | `the last full green is not an ancestor` |
| 4 | `git rev-list --count` over recorded sha to tip exceeds `GATE_FULL_MAX_LAG` | `N commits since the last full bar` |
| 5 | the pushed diff touches `tools/gate-legs.json` | `the leg manifest is in this diff` |
| 6 | the pushed tip is a merge whose second parent is not an ancestor of the recorded green | `a merge tip the record does not cover` |

Seven rows, not eight. The row that forced full on a non-integer lag is gone, because S6 settles that
no environment supplies the lag: a forcing row whose input cannot vary at run time is not a predicate,
it is an edit-time invariant, and S8 arms it as one. Round 2's R20 found it as the single row of the
table with no criterion while S8 promised one arm per row.

**Every predicate fails toward FULL.** An absent, unreadable, unparseable or ambiguous record yields
a full run, never a scoped one. This is the entire safety argument, and it is why each read is
written as a failure that sets the reason rather than as an assignment that might leave a variable
empty. `TOOL-aStandingWrit-4` recorded that exact class in this same hook, where an unmatched
`GOV_DEFAULT_BRANCH` sent it down its own "nothing to gate" exit 0 and skipped every leg on the bar.

Predicates 2 and 5 overlap without being the same check. Predicate 5 catches a manifest edit inside
the pushed range even where the fingerprint round-trips. Predicate 2 catches a manifest that differs
from the recorded one for any other reason, including a record written on another node.

### Rollout

One commit. The rollback is restoring the unconditional `export GATE_FULL=1`, one line, no revert of
anything else. The first push after this lands finds no record and forces full, which is the correct
cold start rather than a special case.

### Files touched (estimate)

| file | change |
|---|---|
| `.githooks/pre-push` | the decision block, the lag default with its comment, the no-halt export |
| `.githooks/pre-push.test.sh` | one arm per predicate, the scoped-path arm, the no-halt arm |
| `AGENTS.md` | the gate-suite paragraph's safety-property sentence |
| `parallel-coding-governance.template.md` | its diff-scope and full-bar sentence |
| `tools/run-gates/run-gates.sh` | the header comment stating the same retired claim |
| `parallel-coding-governance.domain-rules.md` | the two bullets stating the retired guarantee (S9) |
| `memory/guides/BUILD-METHOD.md` + `tools/memory-tree/BUILD-METHOD.template.md` | the same claim, edited as a PAIR and re-rendered or kit/dogfood parity reds (S9) |
| `memory/guides/SESSION-KICKOFF.md` | the fourth statement of the claim (S9) |
| `tools/gate-legs.json` | S10's guard row — gov's carrier |
| `tools/memory-tree/kit.toml` | S10's OTHER carrier: the same leg's declared guard, which govkit emits verbatim into a target (R7) |
| `memory/project/testsuite-count-waivers.txt` | the pre-push suite's row, deleted beside S8's counter |

### Alternatives rejected

- **Scope with no backstop at all.** Rejected: two live records depend on the backstop, and the
  residual risk is a wrong merge verdict rather than a late signal.
- **Keep forcing full on every push.** Rejected by owner decision on 2026-08-18, with the 873 s
  against 62 s measurement in hand.
- **Prove each guard complete, then scope freely.** The sound answer, and far larger than this
  build. Recorded as the follow-up that retires the residual risk.
- **Reuse a previous green keyed on the tree sha instead of scoping.** Sound where legs are pure,
  and `git rev-parse HEAD^{tree}` makes it a one-command key. But `tools/unattended/check-unattended.sh`
  calls `git ls-remote`, so its verdict is a function of the remote as well as of the tree. Reuse
  therefore belongs to `TOOL-aPacedTurnstile-5` behind a per-leg purity declaration, not here.

## 5. Production-readiness checklist

- security — the record is read from the git dir, already trusted by every other hook path; a
  hostile record can only force MORE work, because every parse failure forces full.
- perf / scale — five git commands, each O(1) or O(commits in range), all measured well under a
  second on this repo.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English strings in a shell hook, as everywhere else here.
- error / empty / loading states — the absent-record and unparseable-record paths ARE the empty
  states, both force full, and both carry arms.
- observability — S5 is the observability: the reason string is printed and recorded.
- risks (concurrency, data-loss, rollback hazards) — the residual risk is a too-narrow guard landing
  a wrong verdict inside the lag window. Rollback is one line.
- testing + left-shift gates — S8's arms, one per forcing predicate. The class left-shifts as the
  forcing table itself.
- migration / rollback — no migration. Cold start forces full, which is correct.
- user docs — S9, across every carrier the measured search selects, seven at this base, two of them
  product files an adopter receives and one of them the build-method guide edited as a pair with its
  shipped template. Deliberately NOT a count restated here: this line read "all three carriers" for
  one revision after S9 stopped enumerating three, which is the §5-contradicts-the-scope-item class
  round 2 raised against `-5` (round 3's T13/T16/T23).

## 6. Acceptance criteria

- **AC1** — When a records-only commit is pushed to the default branch with a fresh full-green
  record present, `.githooks/pre-push` runs its gate without `GATE_FULL` set.
- **AC2** — When no run record exists, `bash .githooks/pre-push.test.sh` observes the hook invoking
  its gate with `GATE_FULL=1` and printing `no usable run record`.
- **AC3** — When the pushed diff touches `tools/gate-legs.json`, `bash .githooks/pre-push.test.sh`
  observes `GATE_FULL=1` and the reason `the leg manifest is in this diff`.
- **AC4** — When the recorded full-green sha is not an ancestor of the pushed tip,
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` AND the reason
  `the last full green is not an ancestor`. The reason string is part of the criterion because
  predicate 1 also yields `GATE_FULL=1`, so the flag alone cannot tell the arms apart, and each
  fixture's record is asserted to PARSE before the predicate under test is triggered.
- **AC5** — When more commits than `GATE_FULL_MAX_LAG` separate the recorded green from the tip,
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` AND the reason naming the commit count.
- **AC6** — When the record's manifest fingerprint disagrees with `git hash-object tools/gate-legs.json`,
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` AND the reason `the leg manifest changed`.
- **AC6b** — When the record's stored tree fingerprint does not match a fresh fingerprint computed
  AT THE RECORDED SHA, `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` and the reason
  `the record describes a different tree`. **Its control is the other half and they are graded
  together:** a record whose stored fingerprint DOES match at the recorded sha, on a tip whose tree
  differs from that sha's, observes the gate running WITHOUT `GATE_FULL` — which is the criterion the
  tip-joined spelling could not satisfy at the same time as AC1, and the reason round 2 called that
  spelling a blocker. Without the second half this criterion is satisfied by a predicate 0 that fires
  unconditionally.
- **AC6c** — When the pushed tip is a merge whose second parent is not an ancestor of the recorded
  green — the shape `tools/push-main.sh` produces when it reconciles and retries —
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` AND the reason
  `a reconcile merge is not covered by the record`. Graded in the HOOK's suite, not the lander's,
  because the hook derives the fact from the commit it is handed and needs no channel from the
  lander; `bash tools/push-main.test.sh` keeps only the end-to-end observation that a reconciled
  retry lands green. **Its control is the negative half, and it is required:** a merge tip whose
  second parent IS an ancestor of the recorded green observes the gate running WITHOUT `GATE_FULL`.
  Every landing on the default branch here is a merge, so without the control this row is satisfied
  by a predicate that fires on all of them — the identical hole AC6b gained a control for in the
  same fold (round 3's T12).
- **AC6d** — When the hook forces a full run for a known reason, that run's record header carries the
  SAME reason string under the declared key `TOOL-aPacedTurnstile-5` S2 defines — asserted in
  `tools/run-gates/run-gates.evidence.test.sh`, where the runner is really driven through
  `GATE_LEGS` and where `-5` owns the header. **Not in `.githooks/pre-push.test.sh`:** that suite
  stubs the gate through `GOV_GATE_CMD` so the bar never runs, which §10 leans on by name, so no
  runner-written header exists there and the cheap implementation would be a stub echoing its own
  environment into a file the arm then reads — certifying test code and leaving R21's gap open
  (round 3's T6). The hook's own suite keeps the half it CAN observe: that the reason is exported to
  the gate command's environment. S5's durable half is otherwise satisfied by a stdout-only
  implementation, and §4 rests the whole inversion on the record making "when did every leg last
  run, and on what sha" answerable.
- **AC7** — When the retired claim is searched for after this lands, a WHITESPACE-INSENSITIVE search
  (the carriers hard-wrap the sentence across lines, so a line-anchored `grep` matches nothing today
  and would pass unchanged) finds it in NONE of the carriers S9 measures, AND a positive search finds
  the replacement sentence naming `GATE_FULL_MAX_LAG` in each. Both halves are per-carrier, over the
  MEASURED population and not a literal list: `AGENTS.md`, `tools/run-gates/run-gates.sh`,
  `parallel-coding-governance.template.md`, `parallel-coding-governance.domain-rules.md`,
  `memory/guides/BUILD-METHOD.md`, `tools/memory-tree/BUILD-METHOD.template.md` and
  `memory/guides/SESSION-KICKOFF.md` at this base. The negative alone is satisfied by any rewording,
  including one still false, and by a grep that never could have matched; an enumeration alone is
  satisfied by editing three files and leaving four, which is what round 2's R8 found.
- **AC8** — When the hook runs, it exports the no-halt flag regardless of which branch its forcing
  table took, asserted in `.githooks/pre-push.test.sh` on both the scoped and the forced path — so a
  landing never stops reporting at the first red chunk.
- **AC9** — When `bash tools/run-gates/run-gates.gov.test.sh` runs — the GOV-ONLY harness
  `TOOL-aPacedTurnstile-1` S1 splits out, because this arm names a gov leg and would red on arrival in
  an adopter tree — the kit/dogfood parity leg's guard names `memory/guides/`, and a fixture touching
  only `memory/guides/BUILD-METHOD.md` causes that leg to RUN rather than skip.
- **AC9b** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, it asserts that
  `tools/memory-tree/kit.toml`'s declared gate-leg guard for this leg names `memory/guides/`, and a
  fixture reverting it to the narrow spelling reds. The arm lives in the memory-tree kit's own suite
  because that is the kit whose descriptor carries the guard, and because **`govkit.py` performs no
  such comparison** — its descriptor/manifest join reads the leg NAME only, exactly as S10's own
  closing sentence says. An earlier spelling of this criterion demanded selfcheck red on that
  fixture, which no scope item built and no existing arm could satisfy: an obligation named in prose
  with no criterion that can fail, which is the R11-R13 shape reintroduced by the fix for a different
  finding (round 3's T10). The descriptor-to-manifest guard JOIN — the thing that would catch this
  class in general — is filed as `TOOL-aPacedTurnstile-12`, because building it here changes govkit's
  contract inside a unit that only reads it, which is the same veto that sent `-1`'s selfcheck arm to
  a follow-up.
- **AC10** — When `bash tools/check-testsuite-counts.sh` runs, `.githooks/pre-push.test.sh` reports
  an executed assertion count no lower than its recorded floor AND the registry carries no row naming
  that suite. The second clause is the half round 2's R18 found missing: the registry reds on a waiver
  naming a suite that now complies, so the criterion was unsatisfiable while S8 added only arms, and
  an implementation that added a counter without deleting the row traded one red for another.

## 7. Gates

`bash .githooks/pre-push.test.sh` · `bash tools/push-main.test.sh` ·
`bash tools/run-gates/run-gates.test.sh` (the post-move path — this unit lands seventh) ·
`bash tools/run-gates/run-gates.gov.test.sh` · `bash tools/check-testsuite-counts.sh` ·
`bash tools/check-playbook-parity.sh` · `bash tools/memory-tree/check-memory-hygiene.sh` ·
`python tools/memory-tree/check-arms.py --check` · `python tools/govkit/govkit.py selfcheck` ·
`bash tools/memory-tree/kit-dogfood-parity.test.sh` ·
and the full bar, `GATE_FULL=1 bash tools/run-gates/run-gates.sh` — the POST-move path, which is
what this unit runs at its own landing and which the last entry still spelled pre-move.

## 8. Open questions

none — the forks below are RESOLVED. Every pick is the M3 ratification of the fork's own
recommendation; the reason each survived the veto order is recorded with it.

- **The shipped default for `GATE_FULL_MAX_LAG`.** Options are `1` (full on nearly every push, so
  almost no saving), `10`, `25`, or a time bound rather than a commit bound. Recommendation: `10`.
  This repo took 13 commits between `origin/main` and the current tip inside a single build, so `10`
  forces roughly one full bar per build rather than one per push, which is the granularity at which
  both parked records would still have been caught.
  RESOLVED (agent, 2026-08-18, delegated): `10`. This is the disposition the build README already
  records, together with the design pass's refused recommendation of `1` and the reason for
  refusing it: the owner's stated goal is to stop paying the full bar per landing, and `1` defers
  essentially all of that saving. The knob is one line and lowering it later needs no code.
- **Where the reconcile-retry case is decided, and by which component.** RESOLVED (agent,
  2026-08-18, delegated), and RESTATED after round 3's T5/T15/T20 in the numbering and the terms the
  fold left the rest of this file in. The case is real and the first draft was wrong to scope it:
  the lander retries by reconciling with origin, which produces a MERGE commit whose content no
  recorded green describes, since the recorded green was earned on the pre-merge tip — so the commit
  that actually reaches the remote would have been the one commit never fully graded. **But
  `tools/push-main.sh` forces nothing and exports nothing.** It keeps its attempt counter as a plain
  shell local, and the hook is a separate process git invokes and cannot see it, so a predicate
  reading that counter would fail toward SCOPED when its signal was absent — against §4's "every
  predicate fails toward FULL". The hook derives the same fact from the commit it is already handed:
  **predicate 6**, a merge tip whose second parent is not an ancestor of the recorded green. There
  is no predicate 7; the table runs 0-6. `tools/push-main.test.sh` keeps only the end-to-end
  observation that a reconciled retry lands green, and AC6c grades the predicate in the HOOK's
  suite.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-4 · 2026-08-18 · folded the blocker re-review: §2 described none of predicates 0, 6 or 7, so
  the scope under-described its own decision table; and predicate 0 is now stated as CALLING
  `TOOL-aPacedTurnstile-5`'s shipped fingerprint helper rather than computing its own digest, which
  would have failed toward FULL permanently and looked like caution.
- rev-3 · 2026-08-18 · folded the spec audit. Predicate 0 joins the record's tree fingerprint to the
  pushed tip, without which a full green earned on a dirty tree reset the lag counter (BLOCKER F5,
  F30). Predicate 7 forces full on a push-main retry, whose reconcile merge commit no recorded green
  describes — the first draft's §8 answer was wrong and is rewritten (F29). The lag becomes a source
  constant rather than the cited `GOV_DEFAULT_BRANCH` shape, which does not exist as described and
  would be fail-OPEN (F26). AC4 through AC6 gain their reason strings, because the flag alone cannot
  tell the predicates apart (F28). AC7 becomes whitespace-insensitive and covers all three carriers,
  having been a line-anchored grep that could never have matched a hard-wrapped sentence (F27, F42).
  S5's durable half gains a mechanism (F25); the gate list is repointed past `-1`'s move (F43).
- rev-2 · 2026-08-18 · folded the design-set reconciliation. The lag default moves into the hook
  because no sibling creates a conf a bash hook can read; the no-halt export is added, because
  `TOOL-aPacedTurnstile-3`'s halt fires when the full-run flag is unset and this unit makes the
  landing run frequently unset, which would have made a landing fail-fast; the retired safety claim
  is chased into the runner's own header comment, which ships to adopters; the one verified-open
  guard hole is closed here rather than left as a recorded residual; and AC7 gains its positive
  half, having been satisfiable by any rewording.
- rev-5 · 2026-08-18 · swept section 8 under the standing mandate: every fork RESOLVED in
  place per M3, and the section's first non-blank line made machine-legal so the classifier
  reads this unit as READY instead of FORKED.
- rev-6 · 2026-08-18 · folded the round-2 spec audit. BLOCKER R1: predicate 0 joined the recorded
  digest against a fresh fingerprint of the PUSHED TIP, and the digest moves on every commit, so it
  fired on exactly the population predicates 3 and 4 admit — the scoped path was unreachable,
  predicates 3-6 dead code, AC1 and AC6b mutually unsatisfiable, and both arms fixture-built so the
  bar saw nothing. The join moves to the RECORDED sha and both S2b and §4 now state what it does and
  does not buy. R15/R20: the reconcile-retry row is derived from the tip's SHAPE rather than from a
  lander local the hook cannot see, and MOVES from 7 to 6 as the non-integer-lag row is deleted,
  because S6 now settles that no environment supplies the lag — an edit-time invariant with an arm, not a forcing row with none.
  R7: S10 closes BOTH carriers of the guard hole, gov's manifest row and the kit descriptor govkit
  emits verbatim, with AC9b arming the shipping half. R8: S9's carrier population is MEASURED, not
  enumerated — it named three where the tree holds seven, two of them product. R10: AC9 moves to the
  gov-only harness. R18: S8 gains the counter and the waiver-row deletion together. R21: AC6d reads
  the forced-full reason back out of the record header. R26: §7's full-bar entry repointed past the
  move.
- rev-7 · 2026-08-18 · folded the round-3 blocker re-review. T1/T2/T3: S2b now names the AT-A-REV
  FORM with its argument, which is the half of the R1 fix that never landed — `-5` owned the helper
  and was never given a signature, so this unit's corrected predicate named a computation the
  interface could not perform, and the two paths of least resistance were the tip join and a second
  implementation. The flat "does NOT detect a dirty working tree" is qualified to the form the hook
  actually calls. T12: predicate 6's population is WIDER than the reconcile retry that motivated it
  — every landing here is a merge — so the reason string names the real condition and AC6c gains the
  negative half, the same control AC6b gained. T5/T15/T20: §8's second fork is restated in the hook's
  terms and the current numbering; it still asked a lander question, answered YES for the lander, and
  closed on a predicate 7 the renumbered table no longer has. T6: AC6d moves to the evidence suite,
  which really drives the runner, because the hook's suite stubs the gate by design and §10 leans on
  that. T10: AC9b is restated as what the memory-tree kit's own suite can observe, and the
  descriptor-to-manifest guard join is filed as `TOOL-aPacedTurnstile-12`. T13/T16/T23: §5's
  user-docs line stops restating a count S9 no longer carries. T18: the cross-reference to `-5`'s
  deleted start-of-run reset is gone.

## 10. Reuse audit

The seam this extends is `.githooks/pre-push`'s existing `GOV_GATE_CMD` indirection together with its
`export GATE_FULL=1` line, both already exercised by `.githooks/pre-push.test.sh` — the hook's test
already stubs the gate, so the forcing arms need no new harness. `tools/run-gates.sh`'s `changed()`
and its `GATE_FULL` bypass are consumed unchanged; this unit adds no scoping mechanism of its own.
The record it reads is `TOOL-aPacedTurnstile-5`'s, cited there rather than duplicated here.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL. The probe returned `TOOL-aTimedTurnstile-2` (the owner call this
unit executes), `cBriefedPilot-15` and the `cKeyedLaunchpad` park (both dependents on the property
this unit weakens), and `TOOL-aStandingWrit-4` (the fail-OPEN class the decision table's
fail-toward-FULL direction is written against).
