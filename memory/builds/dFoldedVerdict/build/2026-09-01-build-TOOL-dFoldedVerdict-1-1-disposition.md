# TOOL-dFoldedVerdict-1 — a review exit says which disposition it took

**Serves:** journal TOOL-dFoldedVerdict-1

*Node `d`, 2026-09-01, owner-present build under `memory/guides/BUILD-METHOD.md`.*

## What binds now

`--review` takes `--disposition fold|promote`, validated against a closed `REVIEW_DISPOSITIONS`
constant. It is **REQUIRED** at a terminal exit — when `review_state` computes `NON-CONVERGENT` or
`CEILING` — and **REFUSED** on any round that is not one. The value is appended to the free-text
reason AFTER the state token, so a row now reads
`verdict BLOCKED · blockers 19 · NON-CONVERGENT · disposition fold`.

That placement is the whole reason the field went there: the gate leg already greps a substring
ending `· NON-CONVERGENT`, and appending after the token leaves every existing reader matching.
Verified on the fixture, not assumed.

The trigger is the COMPUTED state and never `--verdict`, whose closed set holds none of those four
tokens. Both refusals are ordered deliberately — the closed-set check sits with the other argument
validations ABOVE the state computation, so `--disposition nonsense` on a `CONVERGING` round produces
the closed-set refusal and not the state one. That is testable and is tested; without it an arm
passes against either refusal and the ordering is proven by nobody.

The two exit sentences no longer hard-code promotion. They did, in the sentence a run reads at the
moment it exits, so before this unit the driver would have refused a fold and then told the run it
had promoted. `review_exit_note` holds both, defined once because two exits share it, and its
promote wording deliberately keeps the word `PROMOTED` that an existing suite arm asserts on.

## The CEILING ruling, made observable

The owner ruled on 2026-09-01 that at `CEILING` the driver accepts EITHER disposition, on the ground
the recommendation gave: a forced value is a constant, and a constant is not evidence for the clause
that reads it. Both were driven on the fixture — a ceiling round recording `fold` and a second
subject recording `promote`, because `unattended.sh:3951` refuses a second terminal round for a
subject that already has one, so one subject cannot serve both arms.

The cost is recorded rather than absorbed. `memory/guides/BUILD-METHOD.md` M4 and the Skill both say
a run reaching the runaway ceiling promotes and lands anyway, and neither describes a fold there. No
unit of this build amends either sentence. The driver now permits an exit two documents do not
describe, and this paragraph is where that is written down.

## Evidence

**Evidences:** TOOL-dFoldedVerdict-1

Every criterion below was witnessed by DIRECT invocation of `bash tools/unattended/unattended.sh` on
a scratch fixture built from this tree — a throwaway git repo holding the driver, `.unattended.conf`
and four seeded run-state files. **Not** by running `tools/unattended/unattended.test.sh`: a standing
owner instruction forbids running this kit's self-tests, and AC7, AC14 and AC15 name this route in
as many words rather than depending on a suite they may not run.

- **AC1** — a direct `--disposition fold` call on a fixture whose prior round recorded 19 blockers
  appends a row ending `· NON-CONVERGENT · disposition fold`. `grep -c` over the fixture's `RUN.md` returns 1, read
  from the record and not from the source.
- **AC2** — with `--disposition nonsense`, the refusal reads `--review names a disposition outside
  the closed set … legal dispositions: fold|promote`, rendering the constant rather than a retyped
  literal.
- **AC3** — `--disposition nonsense` on a round whose computed state is `CONVERGING` produces the
  CLOSED-SET refusal and NOT the state one, observed in that same stdout. This is S3a's ordering,
  pinned.
- **AC4** — a first round for a fresh subject with `--disposition fold` is REFUSED: `a disposition
  recorded mid-loop is a claim about an exit that has not happened yet: state CONVERGING`.
- **AC5** — a `NON-CONVERGENT` round with no disposition is REFUSED and the message names both
  values: `legal dispositions: fold|promote`.
- **AC6** — after all four refusals above, `git diff --stat` over the fixture's `RUN.md` is EMPTY.
  That is what proves the refusals sit above the `park` call rather than after it.
- **AC7** — the two sequences the suite drives at `:4471` and `:4478`, each with a disposition
  added, both succeed, and the stdout of the promote one still contains `PROMOTED` — `grep -c` returns 1. **The first attempt at
  this arm failed for a fixture reason worth recording:** the driver STAGES its own writes through
  `stage_or_fail`, so `git checkout -- <path>` restored the appended row rather than removing it, and
  the second call hit the already-terminal refusal. Given its own subject, as AC15 already required
  for the same reason.
- **AC8** — `python tools/memory-tree/check-arms.py --check` exits 0. Each new `fail 37` branch has a
  positive assertion in `tools/unattended/unattended.test.sh` naming its own failure text. The arm
  text carries the FULL signature, trailing fragments included: the signature is the longest literal
  run between interpolations after `:`, `"` and spaces are trimmed, so one branch's ends `: state`
  and an arm stopping at the last word would read as unarmed with no hint why.
- **AC9** — `python tools/memory-tree/check-arms.py --report` shows
  `tools/unattended/unattended.sh` at **193 branches / 187 armed**, both risen by exactly 3 from the
  190 / 184 the spec measured — the three branches added. The floors `104:101` sit far below and do
  not move, so no floor edit is owed. The ratified `TOOL-aClosedDocket-4` AC9 asserted the opposite
  in both directions and is false against `tools/memory-tree/check-arms.py:283-291`.
- **AC10** — `bash tools/unattended/check-unattended.sh` reports exactly the status it had at BASE:
  ONE failure, check 2, which is `TOOL-dFoldedVerdict-2`'s clause to change and
  `TOOL-dFoldedVerdict-3`'s record to repair. The criterion asserts the driver change MOVED NOTHING
  on the leg, never that the leg turned green, and it did not.
- **AC11** — `bash tools/memory-tree/marker-contract.test.sh` exits 0, which is S2a proven rather
  than argued: contract 3 reads the verdict vocabulary with a `sed` anchored on `^REVIEW_VERDICTS="`,
  and a constant whose name began with that string would have been swept into it and compared against
  the hygiene engine's three verdict tokens.
- **AC12** — `bash tools/unattended/unattended.sh` with no verb renders the usage from the header and
  its `--review` line reads `--review <slug> --subject <id> --verdict <v> --blockers <N>
  [--disposition fold|promote]`.
- **AC13** — the AC1 invocation's STDOUT names the recorded fold and `grep -c PROMOTED` over the
  capture prints **0**. The criterion's sentence "that call's exit status is 1" is about the `grep
  -c`, which exits 1 when it counts zero — the DRIVER exits 0, because recording a fold is a success.
  Read the other way the criterion would demand a failing driver, so the reading is stated here
  rather than left to the next person.
- **AC14** — a round driven to `CEILING` with no disposition is REFUSED: `--review exits CEILING and
  requires --disposition …`. This reaches the absent-at-exit refusal's SECOND state; AC5 reaches only
  `NON-CONVERGENT`.
- **AC15** — that same fixture records `--disposition fold` at `CEILING` and SUCCEEDS, the row ends
  `· CEILING · disposition fold`, and `grep -c 'promotes and lands anyway'` over the stdout returns
  **0**. A second seeded subject records `--disposition promote` at `CEILING` and also succeeds. Both
  arms, because a criterion observing only `fold` passes an implementation that refuses `promote` at
  a ceiling — which is exactly what the owner ruling forbids.
- **AC16** — `grep -n -- '--disposition' tools/unattended/unattended.test.sh` returns a hit on each
  of the two driver-driven exit calls, `:4471` for `F1 (fork)` with `fold` and `:4478` for `S1` with
  `promote`; the `hit "$out" "PROMOTED"` assertion still stands below the second; and the two
  first-round calls at `:4467` and `:4477`, which compute `CONVERGING`, did NOT gain one.
- **AC17** — the `--review` bullet extracted from both halves of the VERBS pair contains neither
  `promoted to a unit rather than parked` nor any other form of the old claim, and both contain
  `fold` and `promote`. `wc -c memory/guides/UNATTENDED-VERBS.md` reports 8950, far under 61440 —
  which is the reorder paying off, since at BASE this edit had to fit a document with zero headroom.

## What this pass did NOT do

The three new suite arms have not been EXECUTED, for the same standing instruction. What has been
executed is the driver itself, on every branch those arms cover, through the scratch fixture — so
the BRANCHES are witnessed and the arms that would keep them witnessed in CI are not.

It did not amend `memory/guides/BUILD-METHOD.md` M4 or the Skill sentence that say a ceiling
promotes and lands anyway. Both are now incomplete rather than wrong, and no unit of this build owns
them. Recorded above rather than discovered later.

It did not touch `memory/project/unarmed-branches.txt`. The three branches were APPENDED within their
checks rather than inserted, and that file pins no row for check 37 of this driver — verified by
reading it, not assumed, because an insertion above a pinned row silently repoints it at a different
branch.
