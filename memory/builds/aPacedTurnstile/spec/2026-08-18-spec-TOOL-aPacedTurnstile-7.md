# TOOL-aPacedTurnstile-7 — the push boundary scopes to the diff, and "every leg" becomes a bounded obligation

**Status:** CLOSED · rev-10 · 2026-08-20 · node a · Tier-2 · base 6517579f · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round2.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round3.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-round4.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1-run-cumulative.md) | diff-review | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 |
| [2026-08-18-review-TOOL-aPacedTurnstile-1.md](../reviews/2026-08-18-review-TOOL-aPacedTurnstile-1.md) | spec-audit | TOOL-aPacedTurnstile-1 TOOL-aPacedTurnstile-2 TOOL-aPacedTurnstile-3 TOOL-aPacedTurnstile-4 TOOL-aPacedTurnstile-5 TOOL-aPacedTurnstile-6 |

<!-- /gen:spec-records -->

## 1. Goal

`.githooks/pre-push:83` exports `GATE_FULL=1` unconditionally, so every landing runs the WHOLE leg
manifest whatever its diff contains. The manifest's size is derived and not pinned:
`python -c "import json;print(len(json.load(open('tools/gate-legs.json'))))"`. That read 86 at
`43a6c13` on 2026-08-20 and 70 at `6517579f` on 2026-08-18, which is itself the argument for
deriving it — the figure moved by sixteen in two days.

The cost is measured by `python tools/run-gates/profile_bar.py`, the instrument the sibling build
`aMeteredTurnstile` shipped for exactly this. Run with `GATE_FULL=1` on a QUIET node `a` at
`43a6c13` on 2026-08-20 it reported 1033.2 s of wall clock, of which the single leg
`unattended driver selftest` held 836.5 s. These figures are never to be taken from
`<git-dir>/gate-timings.tsv`, which is last-write-wins across runs and whose copy on this node was
written under four concurrent bars, where it held that same leg at 1252 s.

The floor leg carries a guard. `tools/gate-legs.json` declares it as `["tools/lib/",
"tools/unattended/"]`, so a landing touching neither does not run it at all. That is why scoping the
boundary is one of only two things in this build that can move wall clock. `profile_bar.py` reports
the bar as FLOOR-bound and states in its own output that only making the binding leg cheaper,
sharding it, or removing it from the critical path buys anything; scoping the boundary removes it
from the critical path of every landing that does not touch it.

The saving itself is DERIVED at build time and is deliberately not pinned here: run the bar over the
landing's own diff without `GATE_FULL` and read the wall from the same instrument. The 62 s figure
this spec carried through rev-8 was measured at `6517579f` on a 70-leg bar and describes nothing
that exists now.

Scope the push boundary to the diff, and replace the property that forcing bought with a bounded,
recorded obligation instead of deleting it.

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
  defect it is. The helper does not exist yet: `ls tools/run-gates/` at `43a6c13` shows no
  `gate-fingerprint.sh`, and `-5` is the unit that ships it, which is the first half of §4's
  ordering line.

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
  TOML a bash hook cannot parse, and the profile table forbids a coverage knob by rule.
  **That last clause was a forecast when rev-2 wrote it and is now a landed rule**, so the
  source-constant decision no longer rests on a prediction: `tools/run-gates/gate-profiles.txt:12-15`
  declares "no knob here may ever turn a leg into a PASS or a SKIP", which `TOOL-aPacedTurnstile-2`
  landed. It
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
- **S7 — CUT by the 2026-08-20 re-scope, and recorded here rather than deleted.** It exported the
  no-halt flag `TOOL-aPacedTurnstile-3` was to define, so that a landing got a complete verdict list
  instead of stopping at the first red chunk. The re-scope cut `-3`'s dispatch half, the boundary
  HALT included, on the measurement that scheduling cannot move a floor-bound bar. With no halt
  there is no flag, and an export of a flag nothing reads is a line that looks like a safeguard.
  The property the item wanted is unaffected by this unit: the runner reports every leg it runs and
  this unit changes only WHICH legs run. The number is kept vacant rather than reused, so a review
  citing S7 against an earlier revision still resolves.
- **S8** — `.githooks/pre-push.test.sh` gains one arm per forcing predicate, one arm proving the
  scoped path actually scopes, and one asserting the lag constant in
  the hook is a decimal integer at edit time (S6). The no-halt arm goes with S7. **One arm of this
  unit lands in a SIBLING's
  suite**: AC6d's header assertion goes in `tools/run-gates/run-gates.evidence.test.sh`, because
  that is the harness which really drives the runner and because `TOOL-aPacedTurnstile-5` owns the
  header — the hook's own suite stubs the gate by design. Named here rather than only in the
  criterion, because §4 Files touched is what a builder derives the commit's edits from and a
  cross-unit arm recorded in neither unit is an arm nobody writes (round 4's V4). **That arm must be
  CORPUS-NEUTRAL**, which rev-8 did not require and `-1` made mandatory: `tools/run-gates/kit.toml:18-20`
  ships this whole directory under `[[files]] include = "**"`, so an arm naming a gov leg, a gov
  reason literal or the real manifest reds on arrival in an adopter tree. It drives the runner
  through a fixture `GATE_LEGS` manifest and supplies the reason string from its own environment. If
  it cannot be written that way it moves to `tools/run-gates/run-gates.gov.test.sh`, which
  `tools/run-gates/kit.toml:33-35` withholds with `role = "project-owned"`, beside AC9's arm. It also gains an EXECUTED ASSERTION COUNTER in the
  agreed shape, and this unit DELETES that suite's row from
  `memory/project/testsuite-count-waivers.txt:6` in the same commit. Both halves or neither: the
  registry reds on a waiver naming a suite that now complies, so a counter without the deletion and a
  deletion without the counter are each a red, and AC10 was unsatisfiable while the row stood
  (round 2's R18).
- **S9** — the safety property is rewritten wherever it is stated, and the population is MEASURED
  rather than enumerated: a whitespace-insensitive search for the claim across the tracked
  non-archive tree selects the carriers, and the search itself is what §6 grades. The enumeration
  frozen into an earlier AC7 is what rotted, twice: rev-2 found three where the tree held seven, and
  the 2026-08-20 reground found two of those seven gone. The classes below are what a builder needs
  and they do not rot the way a file list does. **The paths and line anchors in them are a SNAPSHOT
  taken at `43a6c13` on 2026-08-20, kept for orientation and explicitly NON-BINDING.** What binds is
  AC7, which grades the probe's return at build time; a builder who finds this snapshot disagreeing
  with the probe follows the probe and does not repair the snapshot.
  - **The charter, which has THREE sources and needs all three edited.** `AGENTS.md` is the
    committed text. `coding-governance-agents.template.md:58` is the source of its template-fixed
    sentences, this repo dogfooding its own product. `.governance/deploy.toml:36` is the renderer's
    INPUT for the answer-fed ones, and it outranks an `AGENTS.md` edit alone, because
    `tools/playbook/adopt-playbook.sh` fills the placeholder from that answer and the next deploy
    writes the retired claim straight back in. `ci_file` there reads "the bar runs at the push
    boundary via `.githooks/pre-push`", which stays literally true and stops being the whole truth.
  - **The runner, which SHIPS.** `tools/run-gates/run-gates.sh:3` states the claim in its own
    header, and `TOOL-aPacedTurnstile-1` made this directory a kit, so an adopter receives it.
  - **The shipped canary**, `tools/run-gates/run-gates.test.sh:458-461`, whose arm 3i comment
    carries the retired claim verbatim — that `.githooks/pre-push` sets `GATE_FULL`, so a guard can
    only ever scope a NON-authoritative run and a too-narrow guard costs an early signal rather than
    a wrong merge verdict. `-1` split the canary and left this half shipping.
  - **`memory/guides/BUILD-METHOD.md:147` TOGETHER WITH its shipped source
    `tools/memory-tree/BUILD-METHOD.template.md:147`** — edited as a pair and re-rendered, because
    `kit-dogfood-parity.test.sh` compares exactly those two and reds on a one-sided edit.
  - **`memory/guides/SESSION-KICKOFF.md:79`**, whose gate-command block glosses `GATE_FULL=1` as
    "what `.githooks/pre-push` runs", which is the exact sentence this unit falsifies.
  - `parallel-coding-governance.domain-rules.md` and `parallel-coding-governance.template.md` are
    STRUCK from this item. Neither is tracked: `PLAY-aFusedCharter-1` collapsed the family into the
    single `coding-governance-agents.template.md` at v3.0, and the only files still bearing the old
    name are the frozen snapshots under `memory/archive/`, which must not be edited.
- **S10** — close the one guard hole that is verified still open, named in
  `memory/builds/cKeyedLaunchpad/README.md` park 2 and in `cBriefedPilot-15`: the kit/dogfood parity
  leg's guard omits `memory/guides/`, which is a file pair it actually validates. Re-verified at
  `43a6c13`: the leg's row in `tools/gate-legs.json` guards on `memory/HYGIENE.md`,
  `memory/TEMPLATE-SPEC.md`, `tools/lib/` and `tools/memory-tree/`, while
  `tools/memory-tree/kit-dogfood-parity.test.sh:53` really does validate the
  `memory/guides/BUILD-METHOD.md` pair. **The hole has TWO carriers and both are closed here.** gov's
  own row in `tools/gate-legs.json` is the one an earlier
  draft fixed; `tools/memory-tree/kit.toml:112` declares the SAME leg for DEPLOYMENT with an even
  narrower guard, and `govkit.py:2371` copies a descriptor's declared guard verbatim into the
  target's manifest. Fixing only gov's row leaves the half that SHIPS open, so an adopter taking
  memory-tree plus the promoted run-gates kit receives a parity leg that skips when their own
  build-method guide moves — the wrong-merge-verdict inversion this unit exists to bound, exported
  rather than fixed. Nothing catches the divergence today: govkit's selfcheck joins descriptor gate
  legs to the manifest by NAME only and never compares the two guards. **So this unit also writes
  the arm**, in `tools/govkit/selftest.py`, which already parses every descriptor: an assertion that
  this leg's declared guard names `memory/guides/`, with a narrow-spelling fixture as its control.
  Stated as a scope obligation and not only in AC9b, because the criterion alone is the R11-R13
  shape one level down — it can fail, but nothing tells the builder to write it (round 4's V5). The
  GENERAL descriptor-to-manifest guard join stays out and is `TOOL-aPacedTurnstile-12`, which
  `memory/map/features/run-gates.md` already files in its Gaps section; this is one
  assertion about one leg.

## 3. Non-goals (OUT)

- Changing what any leg asserts. Widening guards in general stays out: S10 closes the ONE hole that
  is verified open and recorded twice, and does not open a survey of the rest. The count of guarded
  legs that stood here through rev-8 is struck. It read 41, `tools/gate-legs.json` holds 50 at
  `43a6c13`, and a derived population written into prose is the class §7 of the charter bans. Derive
  it if a reader needs it:
  `python -c "import json;print(sum(1 for l in json.load(open('tools/gate-legs.json')) if l.get('guard')))"`.
- The run record's format, location and writer. That is `TOOL-aPacedTurnstile-5`; this unit is a
  consumer and states only what it reads.
- Removing `GATE_FULL`. It stays as the manual escape and as the mechanism this unit sets.
- Making the bar faster. Scoping changes which legs run, never how fast a leg is. The measurement
  behind this build says a leg is where the remaining wall clock lives, and sharding it is its own
  build.
- Exporting a no-halt flag. **This is the S7 cut**, carried here so the refusal is on the record and
  not merely absent. The 2026-08-20 re-scope cut the boundary HALT out of
  `TOOL-aPacedTurnstile-3` because scheduling cannot move a floor-bound bar, and with no halt there
  is no flag to export. AC8 graded that export and is struck with it; its number is left vacant so
  older reviews still resolve.
- Proving guard completeness. Named as the follow-up that would retire this unit's residual risk.

## 4. Design

### The property, before and after

Today the hook's own comment states it. `GATE_FULL` marks "THE run that must be total: the self-test
legs are diff-scoped on earlier runs, and if that scoping reached here no run would ever execute
every leg against the tree that actually lands." That is accurate, and three records lean on it.
`memory/builds/cBriefedPilot/spec/2026-08-14-spec-cBriefedPilot-15.md` names a leg whose guard
omits `memory/guides/BUILD-METHOD.md` and is caught only at the push boundary.
`memory/builds/cKeyedLaunchpad/README.md` refused to widen a guard because `GATE_FULL=1` covers it.
`tools/run-gates/run-gates.gov.test.sh:143-150` arms it, grepping `.githooks/pre-push` for the
literal line this unit deletes, so the arm reds at this unit's own landing — §8 carries the fork
over what replaces it.

The replacement property, as it will be written into every carrier S9 names: every leg runs against a
tree that lands at least once every `GATE_FULL_MAX_LAG` commits, and always when the leg set or its
guards move. That is strictly weaker. It is also, unlike today's property, MEASURABLE — the record
makes "when did every leg last run, and on what sha" answerable, which nothing answers today.

**This unit supersedes `TOOL-aTimedTurnstile-2`'s S3, "the push boundary stays full."** That is the
correct shape and it is stated here so the supersession is a record rather than a silent
contradiction: `-aTimedTurnstile-2` measured the case for guards and then declined to spend the
boundary, and the owner reopened exactly that call on 2026-08-18. The earlier record is not
rewritten.

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

**Ordering, which does not follow from the one-commit shape and so is stated.** The re-scoped build
order is `-5 → -4 → -6 → -7 → -3`, and this unit lands FOURTH of the five. Two edges bind it.
`TOOL-aPacedTurnstile-5` must land first, because it ships `tools/run-gates/gate-fingerprint.sh`,
absent from `tools/run-gates/` at `43a6c13`, and the record header key predicate 0 and AC6d read.
`TOOL-aPacedTurnstile-6` must land first, because this unit consumes `changed()` against the base
that unit sets, and settling base semantics before the boundary keeps the two failure surfaces
apart. The edge to `TOOL-aPacedTurnstile-3` is GONE: it existed only because S7 exported a no-halt
flag that unit was to define, and the re-scope cut both the halt and S7. `-3` now runs last because
it is reporting-only and has no dependents, not because this unit waits on it.

### Files touched (estimate)

| file | change |
|---|---|
| `.githooks/pre-push` | the decision block, the lag default with its comment |
| `.githooks/pre-push.test.sh` | one arm per predicate, the scoped-path arm, the lag-constant arm |
| `AGENTS.md` | the committed charter's safety-property sentences (S9) |
| `coding-governance-agents.template.md` | its diff-scope and full-bar line, the template-fixed source of those sentences (S9) |
| `.governance/deploy.toml` | the `ci_file` answer, the RENDERER's input — without it the next deploy rewrites the retired claim into `AGENTS.md` (S9) |
| `tools/run-gates/run-gates.sh` | the header comment stating the same retired claim, which ships to adopters (S9) |
| `tools/run-gates/run-gates.test.sh` | arm 3i's comment, which states the retired claim verbatim in the SHIPPED half (S9) |
| `memory/guides/BUILD-METHOD.md` + `tools/memory-tree/BUILD-METHOD.template.md` | the same claim, edited as a PAIR and re-rendered or kit/dogfood parity reds (S9) |
| `memory/guides/SESSION-KICKOFF.md` | the gate-command gloss on `GATE_FULL=1` (S9) |
| `tools/run-gates/run-gates.gov.test.sh` | G3, which greps for the exact line this unit deletes and reds on landing — §8's fork decides what replaces it |
| `tools/gate-legs.json` | S10's guard row — gov's carrier |
| `tools/memory-tree/kit.toml` | S10's OTHER carrier: the same leg's declared guard, which govkit emits verbatim into a target (R7) |
| `tools/run-gates/run-gates.evidence.test.sh` | AC6d's header arm — a CROSS-UNIT edit into `TOOL-aPacedTurnstile-5`'s suite, written corpus-neutral because this file now SHIPS (V4) |
| `tools/govkit/selftest.py` | S10's guard assertion over `tools/memory-tree/kit.toml` and its narrow-spelling control (V5) |
| `memory/project/testsuite-count-waivers.txt` | the pre-push suite's row, deleted beside S8's counter |

### Alternatives rejected

- **Scope with no backstop at all.** Rejected: three live records depend on the backstop, one of
  them an executable arm, and the residual risk is a wrong merge verdict rather than a late signal.
- **Keep forcing full on every push.** Rejected by owner decision on 2026-08-18. The measurement in
  hand at the time was 873 s against 62 s at `6517579f`; the decision was re-affirmed on 2026-08-20
  against 1033.2 s of wall clock at `43a6c13`, with the binding leg at 836.5 s and guarded.
- **Prove each guard complete, then scope freely.** The sound answer, and far larger than this
  build. Recorded as the follow-up that retires the residual risk.
- **Reuse a previous green keyed on the tree sha instead of scoping.** Sound where legs are pure,
  and `git rev-parse HEAD^{tree}` makes it a one-command key. But `tools/unattended/check-unattended.sh`
  calls `git ls-remote`, so its verdict is a function of the remote as well as of the tree. Reuse
  therefore belongs to `TOOL-aPacedTurnstile-6` behind a per-leg purity declaration, not here.

## 5. Production-readiness checklist

- security — the record is read from the git dir, already trusted by every other hook path; a
  hostile record can only force MORE work, because every parse failure forces full.
- perf / scale — one git command per row of §4's decision table, plus `gate-fingerprint.sh`'s own
  calls. Each is O(1) or O(commits in range), all well under a second on this repo. The count that
  stood here through rev-8 said five and the table has seven rows; the shape is what matters and the
  arithmetic is now derivable from the table beside it.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English strings in a shell hook, as everywhere else here.
- error / empty / loading states — the absent-record and unparseable-record paths ARE the empty
  states, both force full, and both carry arms.
- observability — S5 is the observability: the reason string is printed and recorded.
- risks (concurrency, data-loss, rollback hazards) — the residual risk is a too-narrow guard landing
  a wrong verdict inside the lag window. Rollback is one line.
- testing + left-shift gates — S8's arms: one per forcing predicate, the scoped-path arm, the
  edit-time lag-constant arm, and AC6d's corpus-neutral header arm in the sibling evidence suite.
  The class left-shifts as the forcing table itself.
- migration / rollback — no migration. Cold start forces full, which is correct.
- user docs — S9, across every carrier the measured search selects. Deliberately NOT a count
  restated here, and now not a list either: this line read "all three carriers" for one revision
  after S9 stopped enumerating three, and the enumeration that replaced it named two files the tree
  no longer has (round 3's T13/T16/T23, then the 2026-08-20 reground). Three of the carriers are
  product an adopter receives, and one is the build-method guide edited as a pair with its shipped
  template.

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
  green — of which the `tools/push-main.sh` reconcile retry is ONE INSTANCE, not the population —
  `bash .githooks/pre-push.test.sh` observes `GATE_FULL=1` AND the reason
  `a merge tip the record does not cover`. Graded in the HOOK's suite, not the lander's,
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
  `GATE_LEGS` and where `-5` owns the header. **The arm names no gov leg, no gov reason literal and
  not the real manifest**, because `tools/run-gates/kit.toml:18` ships this file: it drives the
  runner over a fixture `GATE_LEGS` manifest and supplies the reason from its own environment, and
  the criterion is satisfied only by an arm that would pass in an empty adopter tree. An arm that
  cannot be written that way moves to `tools/run-gates/run-gates.gov.test.sh` beside AC9's.
  **Not in `.githooks/pre-push.test.sh`:** that suite
  stubs the gate through `GOV_GATE_CMD` so the bar never runs, which §10 leans on by name, so no
  runner-written header exists there and the cheap implementation would be a stub echoing its own
  environment into a file the arm then reads — certifying test code and leaving R21's gap open
  (round 3's T6). The hook's own suite keeps the half it CAN observe: that the reason is exported to
  the gate command's environment. S5's durable half is otherwise satisfied by a stdout-only
  implementation, and §4 rests the whole inversion on the record making "when did every leg last
  run, and on what sha" answerable.
- **AC7** — When the retired claim is searched for after this lands, the WHITESPACE-INSENSITIVE
  probe run over the tracked non-archive tree returns ZERO hits for the retired sentence, AND for
  every path that same probe selected BEFORE the edit it returns exactly one hit for the replacement
  sentence naming `GATE_FULL_MAX_LAG`. **The criterion grades the probe's RETURN and never a list**,
  and both halves read one enumeration the build computes from `git ls-files` at the time it runs, so
  a carrier that appears between this revision and the build is graded without anybody editing this
  file. The negative alone is satisfied by any rewording, including one still false, and by a grep
  that never could have matched — the carriers hard-wrap the sentence across lines, so a
  line-anchored `grep` matches nothing today and would pass unchanged. The positive alone is
  satisfied by editing some carriers and leaving others, which is what round 2's R8 found. An
  ENUMERATION is what rotted twice: rev-2 replaced a three-file list that missed four, and the
  2026-08-20 reground found two of the seven that replaced it no longer tracked. S9 carries a dated,
  explicitly NON-BINDING snapshot of the current selection for orientation only.
- **AC9** — When `bash tools/run-gates/run-gates.gov.test.sh` runs — the GOV-ONLY harness
  `TOOL-aPacedTurnstile-1` S1 splits out, because this arm names a gov leg and would red on arrival in
  an adopter tree — the kit/dogfood parity leg's guard names `memory/guides/`, and a fixture touching
  only `memory/guides/BUILD-METHOD.md` causes that leg to RUN rather than skip.
- **AC9b** — When `python tools/govkit/selftest.py` runs, it asserts that
  `tools/memory-tree/kit.toml`'s declared gate-leg guard for this leg names `memory/guides/`, and a
  fixture reverting it to the narrow spelling reds. The arm lives THERE and not in
  `kit-dogfood-parity.test.sh`, which round 4's V5 established is a bash document-differ whose whole
  declared contract is two rendered documents and which reads no `kit.toml` at all — putting a TOML
  read inside it would be a new capability in the wrong host. `tools/govkit/selftest.py` already
  parses every descriptor. The arm is an obligation of S10, not only of this criterion, and **`govkit.py` performs no
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
- **AC11** — When the bar is profiled before and after this lands with
  `python tools/run-gates/profile_bar.py`, both readings taken on a QUIET node, the scoped landing's
  wall clock is recorded together with the sha it was taken at. This criterion exists because the
  saving is the unit's whole justification and no current measurement of it exists: the figures this
  spec carried were taken at `6517579f` on a 70-leg bar. It grades a measurement being TAKEN and
  written down, not a threshold, because a threshold pinned here is the defect D1 of the re-scope
  brief exists to remove.

## 7. Gates

`bash .githooks/pre-push.test.sh` · `bash tools/push-main.test.sh` ·
`bash tools/run-gates/run-gates.test.sh` (the shipped canary, which this unit edits) ·
`bash tools/run-gates/run-gates.gov.test.sh` (whose G3 this unit necessarily breaks — see §8) ·
`bash tools/check-testsuite-counts.sh` ·
`bash tools/check-playbook-parity.sh` · `bash tools/memory-tree/check-memory-hygiene.sh` ·
`python tools/memory-tree/check-arms.py --check` · `python tools/govkit/govkit.py selfcheck` ·
`python tools/govkit/selftest.py` · `bash tools/memory-tree/kit-dogfood-parity.test.sh` ·
and the full bar, `GATE_FULL=1 bash tools/run-gates/run-gates.sh`, which is what this unit runs at
its own landing.

## 8. Open questions

none open — the fork raised by the 2026-08-20 regrounding was RESOLVED at build time, and the two
below it were already resolved; each pick is the
M3 ratification of the fork's own recommendation, with the reason it survived the veto order.

- **What replaces `run-gates.gov.test.sh`'s G3.** That arm greps `.githooks/pre-push` for the exact
  literal `^export GATE_FULL=1$`, so S1 reds it at this unit's own landing. Deleting it is the one
  answer this unit must not take alone: G3 is the only executable statement anywhere that the
  authoritative run covers the whole bar, and removing the arm that guards a property while weakening
  the property is the shape §7 of the charter calls gating the instance rather than the class.
  Option A, REWRITE it in place to assert that the hook still contains a forcing path at all — cheap,
  and weak enough to pass a hook that forces on nothing. Option B, MOVE the behavioural half to
  `.githooks/pre-push.test.sh`, where the hook is really driven and where AC2 through AC6c already
  live, and leave G3 asserting only the gov-specific fact that the hook exists and is wired.
  Option C, replace G3 with an arm over the RECORD instead of over the hook — that the lag between
  the recorded full green and the default-branch tip is within `GATE_FULL_MAX_LAG` — which grades the
  replacement property rather than the mechanism, and reds when the obligation is actually missed.
  Recommendation: C with B beneath it, because C is the only one of the three that can fail for the
  reason the property exists. It is left OPEN because C makes a gov canary depend on the record's
  presence in a fresh clone, and whether that is a red or a skip is a decision about the canary's
  contract rather than about this unit.

  RESOLVED (2026-08-20, at build time): **C with B beneath it, exactly as recommended, and the
  question the fork could not answer resolves to a SKIP.** G3 went red the moment S1 landed, which
  is the fork proving itself rather than a surprise. What replaced it: the behavioural half moved
  to `.githooks/pre-push.test.sh`, which now carries one arm per forcing predicate PLUS the control
  that a scoped run is ever chosen at all — without that control every forcing arm is satisfied by
  a hook that forces unconditionally, which is the hook this unit replaced, passing its own tests.
  What stayed in the gov canary is the half that is about this repository: that a forcing path
  exists at all, and that the staleness bound is a SOURCE constant rather than an environment knob.

  **The fresh-clone question is a skip, and a loud one.** A clone with no record is a legitimate
  state, not a defect — the hook forces a total run there, which is the safe direction — so a red
  would fail every clone on its first push while proving nothing. The arm announces the skip and
  counts it, because a skip that looks like a pass is indistinguishable from coverage.
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

- rev-10 · 2026-08-20 · BUILT and CLOSED. The push boundary DECIDES, and the property it retires
  is replaced rather than deleted.

  **Seven predicates, and every one of them FORCES.** There is no predicate that makes a run
  smaller: the question is "is a scoped run good enough this time", and every way of not knowing
  the answer is a force. That asymmetry is the whole safety argument — the block can be wrong in
  one direction only. Predicate 4 joins the recorded fingerprint AT THE RECORDED SHA and calls the
  shipped helper rather than reimplementing the digest; both were named blockers in earlier rounds
  and both are now structural rather than remembered.

  **S9 was executed as a SEARCH, and it found carriers the spec did not name.** Two of the seven
  files it listed no longer exist. The live set was `AGENTS.md` twice, the product template, the
  runner, the shipped canary, the kickoff manifest's gate-command block, and `.governance/
  deploy.toml` — the last of which the spec never named and which OUTRANKS `AGENTS.md`, because it
  is the renderer's input and the next deploy would have written the retired claim back. The
  sweep is now clean over the whole tracked tree outside `archive/` and `builds/`, and this unit's
  own hook comment was reworded so that a historical mention does not read as a live claim to the
  probe.

  **S10 closed the guard hole in BOTH carriers, which is the half that was nearly missed.**
  `kit/dogfood doc parity` validates three pairs and guarded on two of them, so a change to only
  `memory/guides/BUILD-METHOD.md` skipped the leg that checks it. While the boundary forced a total
  run that cost a late signal; after this unit it would cost a wrong merge verdict. The same narrow
  guard is declared in `tools/memory-tree/kit.toml`, and govkit copies a descriptor's guard verbatim
  into a target — so fixing gov's manifest alone would have EXPORTED the hole rather than fixing it.

  **The arm that mattered most was the one proving the cheap path is ever taken.** Its first
  spelling read the hook's decision from stderr, as the refusal arms above it do; the decision line
  is ordinary progress output on STDOUT, so `1>/dev/null` threw it away and seven arms reported
  "the hook made no decision". A push with nothing to send also never invokes the hook at all, so
  the helper now commits first — a hook that did not run is indistinguishable from one that decided
  nothing.
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
- rev-8 · 2026-08-18 · folded round 4, which returned CLEAN WITH FIXES — the T1 blocker closed
  WHOLE across all seven carriers, and nothing here of that grade. V1: AC6c still asserted the
  RETIRED reason literal and the narrow push-main gloss that S2b and §4's table were rewritten in
  the same commit to reject, so no implementation satisfied both binding carriers and the cheapest
  field repair would have restored T12. V4: AC6d's move to the sibling evidence suite landed in the
  criterion alone — S8, §5 and §4 Files touched now carry the cross-unit arm, since a cross-unit arm
  recorded in neither unit is an arm nobody writes. V5: AC9b named a bash document-differ that reads
  no `kit.toml`; it points at `tools/govkit/selftest.py`, which already parses every descriptor, and
  S10 states the arm as an obligation rather than leaving it in the criterion alone.
- rev-9 · 2026-08-20 · folded the owner's re-scope and the regrounding behind it. The mechanism is
  untouched; what changed is that every figure it rested on had moved and two of its carriers had
  stopped existing. **The numbers.** `profile_bar.py` on a quiet node at `43a6c13` reports 1033.2 s
  of wall clock over 86 legs where §1 claimed 873 s over 70, and the bar is FLOOR-bound with one leg
  at 836.5 s, so §1 now derives the leg count, dates every measurement to its sha, and refuses to
  restate the 62 s scoped figure at all — it was taken on a bar sixteen legs smaller and the ratio
  built on it was arithmetic about a tree that no longer exists. AC11 is added because the saving is
  this unit's whole justification and nothing currently measures it; it grades a measurement being
  taken, never a threshold, since a pinned threshold is the defect being removed. §3's "the other
  41" guarded legs is struck for the same reason — the tree holds 50 and a derived population in
  prose is what §7 of the charter bans. **The carriers.** S9 named
  `parallel-coding-governance.domain-rules.md`, which `PLAY-aFusedCharter-1` dissolved into the
  charter at v3.0, and `parallel-coding-governance.template.md`, whose only surviving instances are
  frozen archive snapshots; a builder following §4 literally would have edited nothing or edited an
  archive, and AC7 graded per-carrier so it was unsatisfiable as written. Both are struck with the
  reason on the record. Three carriers are added, each verified in the tree: `.governance/deploy.toml`,
  which is the renderer's INPUT and therefore outranks an `AGENTS.md` edit that the next deploy would
  revert; `tools/run-gates/run-gates.test.sh`, whose arm 3i comment carries the retired claim
  verbatim in the half `-1` left SHIPPING; and `tools/run-gates/run-gates.gov.test.sh`, whose G3
  greps for the literal line S1 deletes and therefore reds at this unit's own landing. AC7 is
  restated as the SEARCH's output rather than a list, because the enumeration is the half that rotted
  twice and a criterion grading a probe's return cannot rot at all. **The cut.** S7 and AC8 exported
  and graded a no-halt flag `TOOL-aPacedTurnstile-3` was to define; the re-scope cut that unit's
  dispatch half and the boundary halt with it, on `profile_bar.py`'s own finding that scheduling
  cannot move a floor-bound bar. Both numbers are left vacant rather than reused, the refusal is
  recorded in §3, and the ordering edge to `-3` dissolves with them — §4's Rollout now states this
  unit as fourth of five in `-5 → -4 → -6 → -7 → -3`, bound only by `-5`'s fingerprint helper, absent
  from the tree today, and by `-6`'s base rule. **The corpus-neutrality obligation**, which is new
  since rev-8 and not a re-scope item: `-1` made `tools/run-gates/` a deployable kit, so AC6d's arm
  now travels to adopters and must name no gov leg and no gov reason literal, or move to the withheld
  gov harness. §10 is repointed past `-1`'s move and records `profile_bar.py`'s partial run record
  and why it is not the one this unit reads. §8 gains its first OPEN fork since rev-5, over what
  replaces G3, because deleting the only executable statement of the property while weakening the
  property is a decision this unit should not take silently.

## 10. Reuse audit

The seam this extends is `.githooks/pre-push`'s existing `GOV_GATE_CMD` indirection together with its
`export GATE_FULL=1` line, both already exercised by `.githooks/pre-push.test.sh` — the hook's test
already stubs the gate, so the forcing arms need no new harness.
`tools/run-gates/run-gates.sh:117`'s `changed()` and its `GATE_FULL` bypass are consumed unchanged;
this unit adds no scoping mechanism of its own. The path is the post-move one: `-1` moved the runner
from `tools/run-gates.sh`, which §10 went on naming for two revisions after §4 and §7 were
repointed.

`tools/run-gates/profile_bar.py:368-385` writes a run record of its own, appending a row carrying the
sha, the width, whether `GATE_FULL` was set, the exit code and the failed leg names to
`<git-dir>/gate-profile.jsonl`. Structurally that is three of the four fields §4's data model wants,
and it is NOT the record this unit reads. It is written only when an operator invokes the profiling
verb rather than by the bar itself, it carries no manifest fingerprint, no tree fingerprint and no
schema version, and `profile_bar.py:350-364` REFUSES to write at all on a stale timing cache or an
impossible packing ratio. It is therefore absent exactly when a landing needs it. The record this
unit reads stays `TOOL-aPacedTurnstile-5`'s, cited there rather than duplicated here.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL. The probe returned `TOOL-aTimedTurnstile-2` (the owner call this
unit executes, and whose S3 it supersedes), `cBriefedPilot-15` and the `cKeyedLaunchpad` park (both
dependents on the property this unit weakens), and `TOOL-aStandingWrit-4` (the fail-OPEN class the
decision table's fail-toward-FULL direction is written against).
