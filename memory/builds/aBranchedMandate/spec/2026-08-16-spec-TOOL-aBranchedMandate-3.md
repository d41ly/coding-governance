# TOOL-aBranchedMandate-3 — a build published on the run's own branch may authorize the run

**Status:** SPECCED · rev-4 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling · ratified 2026-08-17

## 1. Goal

The unattended authorization requires the build README to be reachable from the merge-base with the
tip the remote advertises for its own HEAD, so a build specced and committed on a unit branch cannot
start a run until it is landed. Admit a second anchor — the tip the remote advertises for the run's
own branch — as a declared, recorded, strictly weaker alternative, and state what it costs in the
document that already states what the first one costs.

## 2. Scope (IN)

- **S1** — `resolve_base` in `tools/unattended/unattended.sh` gains a fallback: when the build README
  does not resolve at the default-branch merge-base, and the project declares the wider scope, the
  BASE is pinned to the tip the remote advertises for the run's current branch. The observation uses
  the same `ls-remote --symref --exit-code` discipline, the same `GIT()` dereference pin and the same
  `GIT_TERMINAL_PROMPT=0` as the existing one.

  **The trigger's mechanism is stated, because the first revision left it unimplementable.**
  `resolve_base` takes no arguments, knows no slug and never reads a README, and its only caller
  reads its value through `fresh=$(resolve_base)`. So: `resolve_base` and `trusted_base` both gain
  the resolved README path as a parameter, and the trigger is a SILENT existence probe —
  `GIT show "$base:$rel" >/dev/null 2>&1` — evaluated inside `resolve_base`. It must NOT be evaluated
  by calling `check_authorization`: that function answers by calling `fail 6`, which prints a numbered
  refusal an operator reads as a failure and sets the global `status`, which has no reset in the file.
  Every successful branch-anchored preflight would emit `UNATTENDED check 6 FAILED` on its way to
  succeeding.
- **S2** — the fallback tip must be an ancestor of HEAD. A tip that is not is a branch the run is not
  building on, and pinning to it would measure the authorization against history this run does not
  contain.
- **S3** — `check_authorization`'s BODY is unchanged; only its signature moves with S1's plumbing. It
  already takes the base as an argument and asserts shape at it, so the fallback changes which commit
  it is handed, not what it asks. The silent probe in S1 is deliberately NOT a second spelling of it:
  it answers existence only, and the shape assertions stay in one place.
- **S11** — `resolve_base`'s RETURN CONTRACT is preserved across both anchors. `rc=2` means "the
  derived base equals HEAD" and is the sole gate on both `fail 16` branches — "the record pins no
  BASE" and "the recorded BASE equals HEAD, so this run built nothing and has nothing to land" —
  whose cost is a recorded owner-accepted fork. On the fallback path the base is reached through
  `rc=0` after the merge-base test has already returned a non-HEAD value, so without this item both
  refusals stop firing for every branch-anchored run, and `check-arms.py` stays green because the
  branches remain reachable on the default-branch path. The fallback tip is re-tested against HEAD and
  returns `rc=2` when equal.
- **S12** — the anchor KIND is pinned at preflight and does not change for the life of the run.
  `trusted_base` re-derives the anchor at every later verb and refuses unless the recorded BASE is an
  ancestor of the freshly derived one. With two anchors that derivation is no longer monotone: if the
  build folder reaches the default branch mid-run — another node lands it, or the run merges origin —
  the FIRST anchor starts firing, the freshly derived base moves to the default branch, and the
  recorded branch tip is not an ancestor of it, so `fail 18` refuses at `--close`. That verb is the
  one the mandate requires, `authorization-reachable` is explicitly not overridable, and `LANDING` is
  close-only, so the run wedges in a non-terminal phase with `--abort` as its only exit.

  **The mechanism is a MONOTONE derivation, not a discriminator** (F5, resolved). `trusted_base`
  accepts a recorded BASE that is an ancestor of EITHER derivation — the default-branch merge-base or
  the advertised branch tip — so nothing has to select, nothing has to remember which anchor fired,
  and `anchor-kind` never reaches the decision path. That is the property this kit keeps paying to
  preserve: the run writes `anchor-kind`, and a verb that branched on it would be the
  inputs-inside-the-subject's-reach defect wearing a new key. The cost is that `fail 18` widens — it
  now fires only for a BASE on NEITHER history — so S9 carries an arm proving it still has a failing
  case. A guard whose widening is untested is a guard nobody notices going vacuous.
- **S4** — the run-state file records `anchor-kind`, plus the branch ref and tip that were observed.
  Protocol section 2 enumerates its authored facts individually, counting one anchor observation as
  three, so at that granularity the count moves from **seven to ten** — not the eight an earlier
  revision wrote. S4 maps each new key to a numbered item and states how the two conditional ones are
  admitted when absent, since section 2's "nothing else" clause is unconditional today. The count
  lives in one place and moves in both copies of the protocol together.
- **S5** — a new declaration `ANCHOR_SCOPE` in `.unattended.conf`, over the closed value set
  `default-branch` and `published`, selects the scope. Absent, blank, or any value outside the set is
  a REFUSAL to widen: an adopter who declares nothing keeps the strict anchor, and a misspelling
  cannot silently select either behaviour.
- **S6** — check 9 of `tools/unattended/check-unattended.sh` stops asking "is the recorded BASE an
  ancestor of the anchor" and asks "is the recorded BASE **published on the remote**": an ancestor of
  the advertised HEAD tip, **or an ancestor of a tip the remote advertises for any ref**. The leg does
  **not** read `anchor-kind` and does **not** read a branch name.

  **REACHABILITY, NOT EQUALITY.** The first revision wrote clause 2 as "equal to a tip the remote
  advertises", justified as "equality is exactly published on the remote". It is not — equality is a
  strict subset. Under S1 the BASE is pinned to the advertised branch tip; the run then commits and
  pushes that same branch again, which is precisely what S7's Skill precondition trains an operator to
  do, and the advertised tip moves past BASE. The recorded BASE is then neither an ancestor of the
  advertised HEAD tip nor equal to any advertised tip, and check 9 reds — permanently, and worse after
  a branch delete or a squash-merge landing, on a leg that iterates every tracked run-state file. This
  is the exact wedge `tools/unattended/check-unattended.sh:271-277` records the kit having already
  been moved off once ("Equality wedged the bar permanently … Reproduced on an honest fixture with no
  attacker"), and `trusted_base` carries the same lesson. Reachability is the form that survives the
  run doing the thing the design tells it to do.
- **S6b** — S6 states, item by item, the disposition of everything else inside the loop it rewrites.
  `tools/unattended/check-unattended.sh:269-316` is ONE `for b in refs/remotes/...` loop carrying
  five things: the not-a-commit refusal, the ancestor-of-anchor test S6 replaces, the
  ancestor-of-HEAD test, the phase-keyed `rb != HEAD` refusal, and — nested inside the same loop —
  check 15's SECOND HALF, which compares the LANDED witness against that loop's `$b` and whose own
  comment says it is inside the loop because it needs the anchor. S6's replacement predicate needs no
  `$b`, so the loop cannot survive as written. Deletion would be loud, because the sibling self-test
  arms both check 15's second half and the phase-keyed clause. RE-ANCHORING would be silent:
  `ARMS_FLOORS` counts branches and textual arms, so a `fail 15` left comparing against the wrong
  anchor stays green. Each of the five is named with the anchor it uses once the loop is gone, and if
  ancestor-of-HEAD is dropped, §4's price list says so — clause 2 has no relation to this run's
  history, so a BASE published on a wholly unrelated ref would otherwise satisfy the check.
- **S6c** — S6 states the leg's OFFLINE behaviour. `check-unattended.sh` makes zero network calls
  today; both of S6's clauses are stated against the remote's advertisement, and AC8 forbids the leg
  from reading `anchor-kind`, so it cannot know which records need the observation and must observe
  for every one. It is an UNGUARDED merge-bar leg that runs under the pre-push hook. Fail-closed reds
  the bar on every offline or credential-less run, including over records that are already terminal;
  fail-open disarms the only BASE check on the bar and matches the silent-skip shape the same check's
  own comment refuses by name. One advertisement is fetched per leg run, not per record, and
  `GIT_TERMINAL_PROMPT=0` is carried into the leg as a stated requirement rather than left to the
  driver.
- **S7** — the rendered Skill states the new precondition, so an operator starting a run on an
  unlanded build is told to publish the branch first rather than meeting a refusal.
- **S8** — protocol sections 1, 2, 8 and 9 gain the second anchor, its declaration, and **all three**
  costs from §4's price list, in `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md` in lockstep. Section 1's four mechanical properties become
  qualified per anchor — the roster one does not hold on the branch anchor — rather than left standing
  unconditionally. A cost the owner accepted that appears only in this spec is a cost the next reader
  of the binding document never sees.
- **S9** — the two sibling self-tests gain arms for the fallback: it fires only when declared, it
  refuses an unadvertised branch, it refuses a tip that is not an ancestor of HEAD, and the leg
  accepts a branch-anchored record while still refusing a BASE that is on no advertised history. One
  further arm covers S5's refusal set: a blank and a misspelled `ANCHOR_SCOPE` both keep the strict
  anchor, because a value-set guard whose failing case is untested is the guard that silently admits.
  A second further arm covers S12's widened `fail 18`: a recorded BASE on NEITHER derivation still
  refuses. Both arms exist for the same reason — this unit widens two guards, and a widened guard with
  no failing-case arm is indistinguishable from a deleted one.
- **S10** — `TOOL-aStandingWrit-6`'s backlog row is rewritten to name what S6 leaves unrepaired,
  rather than closed. S6 makes the leg observe along this predicate's path only; every other
  consumer of the leg's `GOV_DEFAULT_BRANCH` derivation in that file is untouched, and a row closed
  on a partial repair is how a known gap stops being tracked.

## 3. Non-goals (OUT)

- Any anchor that is not an observation of the remote. A local ref, a reflog entry, a commit date, a
  committer identity and the environment are all inside the run's reach, and
  `memory/gotchas/inputs-inside-the-subjects-reach.md` records what that cost the last time.
- Closing the self-authorization class. Protocol section 9 already says this kit does not prevent an
  unauthorized landing, only makes it a visibly deliberate act and records which act was taken. This
  unit lowers the price of that act and is honest about it; it does not claim to raise it.
- Repairing the gate leg's anchor generally. `TOOL-aStandingWrit-6` is the tracked OPEN row for the
  leg computing BASE from `GOV_DEFAULT_BRANCH` and a remote-tracking ref rather than an observation.
  S6 makes the leg observe **for its own predicate**; it does not repair every other consumer of that
  derivation in the same file, and S10 keeps the row open naming the remainder.
- Changing `--landed`, the lander, or the pre-push hook. Landing still happens on the default branch
  and is still gated exactly as today.
- Changing the phase vocabulary or the Definition-of-Done set. `CORE_FLOOR` does not move.
- Bumping `KIT_UNATTENDED_VERSION`. Resolved in §8 F3: the version moves once, in node `c`'s build,
  and this one lands without waiting on it.

## 4. Design

### What fails today, and why it is not a bug

Reproduced by `build/repro-c3.sh` under this build, against a bare origin that advertises a HEAD
symref so the anchor observation succeeds and only the authorization comparison fails:

```
UNATTENDED check 6 FAILED — no build README at the pinned BASE, so nothing committed before this
run branched authorizes it, and a build folder the run created on its own branch authorizes
nothing: <merge-base>:memory/builds/aTestBuild/README.md
```

Protocol section 1 states this as ratified design, and the four costs of the current model were
enumerated and accepted by the owner. So this unit is a **rule change**, priced as one.

Two facts about the current predicate that shape the fix. It reads only `README.md` — specs are
never consulted, so landing the specs would change nothing. And it is not worktree-specific; any
branch reproduces it. The worktree is where this repo keeps branches, which is why the symptom is
seen there.

### The second anchor

```
observe HEAD symref  ->  advertised default ref + tip        (today, unchanged)
BASE := merge-base(advertised tip, HEAD)
    build README resolves at BASE?  -> authorized, anchor-kind: default-branch
    otherwise, and only when declared:
observe refs/heads/<current branch>  ->  advertised branch tip
    tip is an ancestor of HEAD?      (S2)
    build README resolves at tip?    -> authorized, anchor-kind: run-branch
                                        BASE := that tip
```

Both anchors are observations of the same endpoint the landing push goes to. The existing
same-endpoint, single-remote, no-substitution-lever and no-injected-config guards run before either
and are not duplicated.

### What is preserved, and what is spent

**Preserved.** The anchor is never a local ref and never a name from the environment, so the two
reproduced offline forgeries stay inert by construction. The recorded observation still lets a party
off this machine re-derive the pin without trusting a byte the run wrote.

**Spent — THREE things, not one.** The first revision priced only the first and called it "the whole
price of the unit". The spec audit found the other two.

**1. Self-authorization gets cheaper.** Under the default-branch anchor the authorizing commit had
passed the pre-push hook, which runs the full bar. `.githooks/pre-push` classifies on the remote ref
and runs the bar only for a default-branch push, so **a branch push is an ungated publish**:

> Today a run can authorize its SUCCESSOR — protocol section 1, cost 4, already accepted. Under the
> second anchor a run can authorize ITSELF, in two ordinary commands: commit a build folder on its
> branch, push the branch, preflight.

**2. The BAR weakens for adopters who never opt in.** `ANCHOR_SCOPE` gates the DRIVER. It cannot gate
the leg: the conf is a working-tree file the run can commit, so it sits inside the subject's reach
exactly as `anchor-kind` does, and a leg branching on it would be the same defect wearing a different
key. So S6's predicate is unconditional, and after it a run-state record whose BASE is a tip the run
itself published passes check 9 **in every repo**, including one that declares `default-branch` and
one that declares nothing. Check 13 then resolves the README at that same BASE and passes too. That
is a widening of the half protocol section 9 identifies as the thing that actually binds — the leg
re-run in a clone by a party the run cannot execute code as — and it is paid by adopters who get none
of the benefit. **§5's "defaulted off in S5" applied only to the driver, and this states the rest.**

**3. Roster integrity becomes satisfiable by construction on one anchor.** Protocol section 1 lists
four mechanical properties, the fourth being that a Units table inside a roster marker pair may not
move under the run. `check_authorization` takes the roster region at BASE and compares it against the
WORKING COPY's README. Under the default-branch anchor BASE is a commit the run cannot advance
without a gated landing, so the comparison really does catch a roster rewritten mid-flight. Under the
branch anchor BASE is a tip the run committed and pushed, and `trusted_base` requires only that the
recorded base be an ANCESTOR of the derived one — so the run re-satisfies the comparison against its
own new bytes in two commands. The property is not lost on the default-branch anchor and is not
enforceable on the branch anchor, so S8 qualifies protocol section 1's claim per anchor rather than
leaving it standing unconditionally. **This one matters beyond the spec: the owner accepted cost 1 on
a price list that did not include costs 2 or 3.**

Nothing in this design closes any of the three, and no wording in the protocol may imply otherwise.
What the design does instead is make the first visible: `anchor-kind: run-branch` is on the record,
the branch ref and tip are on the record, and an off-machine verifier sees which anchor a run leaned
on. That is section 9's stated posture applied rather than abandoned. Costs 2 and 3 are not made
visible by anything, which is why they are stated here and put back to the owner as F6.

Two guards were considered for the gap and both rejected as theatre: requiring the advertised branch
tip to differ from HEAD (defeated by one empty commit) and requiring a minimum commit distance
(defeated by the same). A guard the subject satisfies trivially is worse than no guard, because it
reads as protection in a document whose value is that its claims are exact.

### Why the leg must not read `anchor-kind`

`anchor-kind` is written by the run. A leg branching on it would be a security check whose
discriminator is supplied by its subject, which is the class
`memory/gotchas/inputs-inside-the-subjects-reach.md` records and the class three of this kit's
authorization defects belonged to. So S6 gives the leg a single predicate that covers both anchors
and needs no discriminator:

> the recorded BASE is an ancestor of the advertised HEAD tip, **or** an ancestor of a tip the remote
> advertises for some ref.

Ancestry of an advertised tip is "this commit is published on the remote". The first revision wrote
EQUALITY here and justified it with that same sentence, which was wrong: equality is a strict subset
of published, and it wedges the moment the run pushes its branch a second time. S6 carries the
reproduction path. It also keeps the leg free of any branch NAME: route 2
of the reproduced bypass was a branch name supplied through the environment, and a leg that never
reads one cannot be walked through that way. `anchor-kind` stays in the record as EVIDENCE for a
human and for an off-machine verifier, exactly as the anchor ref, tip and URL already do.

The driver does read its own branch name, and that is sound: a forged local name merely selects a
different remote ref to observe, and the authorization still requires the remote to advertise it and
a conforming build README to resolve there.

### Data model

| Run fact | Today | After |
|---|---|---|
| `base` | the pinned merge-base | the pinned base, from whichever anchor |
| `anchor-ref` · `anchor-sha` · `anchor-url` | the observed default-branch advertisement | unchanged |
| `anchor-kind` | absent | `default-branch` or `run-branch` |
| `branch-ref` · `branch-sha` | absent | the second observation, when it was used |

Protocol section 2 states the authored region carries "exactly seven facts and nothing else", and
enumerates them 1..7 — counting one anchor observation as THREE separately numbered facts. At that
same granularity this table's three new keys make the count **ten**, not the eight an earlier
revision of S4 claimed. S4 now states the real count and maps each new key to a numbered item,
including how the two conditional ones are admitted when absent, because section 2's "nothing else"
clause is unconditional today. The count appears in one place only, and both protocol copies move
together — check 10 byte-compares them against each other, so a wrong count is identical in both and
passes. **`memory/builds/cBriefedPilot/README.md` states "No eighth authored fact" as the premise for
routing its own waiver through fact 3**, so this is a live fleet collision and belongs beside the kit
version literal on the build README's stop-and-reconsider list.

### Inventory — every consumer of the authorization

| Site | Change |
|---|---|
| `unattended.sh` `resolve_base` | S1, S2, S11 — gains the README path as a parameter, the silent existence probe, and the preserved `rc=2` contract |
| `unattended.sh` `trusted_base` | gains the same parameter and passes it through; the equality cross-check needs NO change, since a commit is its own ancestor. What it does need is S12 — its ancestry test becomes "ancestor of EITHER derivation", which is what makes the anchor selection irrelevant instead of merely stable |
| `unattended.sh` `check_authorization` | body unchanged (S3); signature moves with S1's plumbing |
| `unattended.sh` `verb_preflight` | records the new facts |
| `unattended.sh` `dod_met` → `authorization-reachable` | re-derives through `trusted_base`, so it inherits S12. Not "none" |
| `unattended.sh` `verb_landed` | landing is still measured against the default-branch tip; AC13 observes it on a branch-anchored run rather than asserting it |
| `check-unattended.sh` check 9 | S6, S6b, S6c |
| `check-unattended.sh` check 15, second half | S6b — it is nested INSIDE the loop S6 rewrites and compares the LANDED witness against that loop's anchor |
| `check-unattended.sh` the phase-keyed `rb != HEAD` clause | S6b — same loop |
| `check-unattended.sh` check 13 | reads the README at the recorded BASE, which S6 has already validated |

The four rows this table previously marked "none" were assertions about code whose behaviour changes
under S1, and no acceptance criterion observed any of them. That is what let S12's wedge sit inside a
spec with twelve green criteria.

### Migration

**Existing records.** A run-state file with no `anchor-kind` is a default-branch run, and S6's
predicate accepts its BASE by the first clause exactly as check 9 does today, so no committed record
is retroactively red.

**Durability of a branch-anchored record**, which the first revision did not consider at all. The
recorded BASE must keep passing check 9 after: the run pushes its branch again (S6's reachability
form covers it; equality did not), the branch is deleted after landing, and the work is
squash-merged rather than fast-forwarded. The last two both leave a BASE that is an ancestor of no
advertised tip. AC6's red case — "a BASE on no advertised history" — is indistinguishable from the
state a legitimate branch-anchored record decays into, which is why S6c's offline behaviour and this
paragraph's cases need their own criteria rather than being read off that one.

### Rollout

Total order, and the reason is the leg. S6 must land in the same commit as S1: a driver that can pin
a branch anchor while the leg still demands ancestry of the default tip writes a record that reds the
bar on the next push, on the one path the run is required to take.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | S1, S2, S4, S11, S12 |
| `tools/unattended/check-unattended.sh` | S6, S6b, S6c |
| `tools/unattended/SKILL.template.md` + the rendered Skill | S7 |
| `tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` | S8 |
| `.unattended.conf` + `tools/unattended/.unattended.conf.example` | S5 |
| `tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.test.sh` | S9 |
| `.memory-tree.conf` | the `ARMS_FLOORS` pairs for both files, re-measured |
| `memory/backlog/TOOL.md` | S10, the `TOOL-aStandingWrit-6` row rewritten to name what remains |
| `AGENTS.md` | **conditional and unbacked.** S6 changes ordinals rather than adding one, so the "fifteen checks" claim at `AGENTS.md:136` is expected to stand — verified: the leg carries exactly `fail 1` through `fail 15` today. If S6b's dispositions add an ordinal, this row becomes mandatory. No gate enforces it either way; see the §7 correction |

### Alternatives rejected

- **Anchor on the commit that introduced the build folder, read locally.** One ordinary commit
  authorizes the run, with no push and nothing published. It deletes the property rather than
  weakening it, and leaves no record that anything was weakened.
- **Keep the strict anchor and require the owner to land the build first.** This is today's
  behaviour and it is what the commissioning report rejects. Recorded because it remains a legitimate
  answer if the owner decides the price in the section above is too high — in which case the
  deliverable is `TOOL-aBranchedMandate-1` and `TOOL-aBranchedMandate-2` alone, which between them
  fix every worktree failure that is not the authorization rule.
- **A signed tag or a secret the owner holds.** It is the one construction that would genuinely close
  the class, and this kit can neither issue nor manage a secret. Protocol section 9 already names the
  remote-side required check as the thing that actually binds.
- **Widen the first anchor's merge-base to any ancestor of the advertised tip that carries the
  README.** It sounds weaker-but-simpler and is neither: a build landed and later deleted would keep
  authorizing runs forever, and it does nothing for a build that was never landed, which is the case
  the report is about.

## 5. Production-readiness checklist

- security — this is the unit's entire subject, and §4 now prices THREE spent properties where the
  first revision priced one. **Only the DRIVER half is defaulted off by S5.** The leg-side widening in
  S6 is unconditional and cannot be gated on `ANCHOR_SCOPE`, because the conf is a working-tree file
  the run can commit and would therefore be the same inside-the-subject's-reach defect as reading
  `anchor-kind`. So adopters who never opt in still get the weaker bar. The one hard rule this unit
  must not break: no input to the authorization may come from inside the run's reach.
- perf / scale — one additional `ls-remote` per preflight on the fallback path. **The leg is
  different and the first revision was wrong about it**: the leg has one predicate, not a fallback
  path, and AC8 forbids it from reading `anchor-kind`, so it cannot know which records need the
  observation and observes once per leg RUN regardless. The leg makes zero network calls today.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a remote that answers but advertises nothing for the branch is a
  refusal naming the branch, distinct from a remote that does not answer at all, which the existing
  `--exit-code` discipline already distinguishes. An empty declaration must select the strict anchor,
  never the wide one: protocol section 8's rule is that an empty declaration is a refusal rather than
  a pass, and the safe reading of a blank scope key is today's behaviour. **The leg's offline
  behaviour belongs here and not in perf**: S6c decides it, it is an unguarded merge-bar leg running
  under the pre-push hook, and neither fail-closed nor fail-open is free.
- observability — the run-state file gains the three facts that make the weaker anchor legible, and
  the wrap-up surfaces `anchor-kind` because an owner reading a landed run should not have to
  reconstruct which anchor it used.
- risks — three named. Self-authorization and the two further spent properties, all in §4. The leg
  and the driver drifting into two different predicates, which is what wedged this kit twice before;
  S6 answers it by giving both one property (published on the remote) rather than two spellings of one
  procedure. And the ANCHOR SELECTION FLIPPING mid-run, which S12 exists for — it is a wedge with no
  attacker, reachable by another node simply landing the build folder, and it ends with the run stuck
  in a non-terminal phase because the verb that would move it is the one that refuses.
- testing + left-shift gates — S9, and the fixture must build a real bare origin that advertises a
  HEAD symref. `build/repro-c3.sh` under this build is the working fixture shape and the arms reuse
  it. An arm keyed on the exit code alone would pass on any refusal, which is the
  `fixture-passes-by-finding-nothing` class this repo tracks by name.
- migration / rollback — no record migrates. Reverting restores the strict anchor and makes any
  branch-anchored run's record unverifiable, so a rollback must be paired with closing or aborting
  any live run — worth stating in the commit, not worth mechanising.
- user docs — S7 and S8. The Skill gains the precondition; the protocol gains the cost.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs on a build committed and pushed on the run's own branch, with the
  wide scope declared, it succeeds and the run-state file records `anchor-kind: run-branch` together
  with the observed branch ref and tip.
- **AC2** — When the same command runs with the scope undeclared or blank, it refuses with the check
  6 message, exactly as `build/repro-c3.sh` reproduces today.
- **AC3** — When the build folder is committed on the branch but the branch has **not** been pushed,
  `--preflight` refuses and its message names the branch that the remote does not advertise.
- **AC4** — When the remote advertises the branch but its tip is not an ancestor of HEAD,
  `--preflight` refuses, and the arm proving it uses a fixture where the tip is a real advertised
  commit rather than a missing one.
- **AC5** — When a build README is present at the branch tip but declares a different `slug:`,
  `--preflight` refuses through the existing shape check, proving `check_authorization` was reached
  rather than bypassed.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs over a branch-anchored record, it
  passes; when it runs over a record whose BASE is on no advertised history, it reds naming that
  BASE.
- **AC7** — When the leg runs over an existing default-branch record that carries no `anchor-kind`,
  it passes unchanged, proving no committed record is retroactively red.
- **AC8** — When `grep` is run over `tools/unattended/check-unattended.sh` for `anchor-kind`, there is
  no hit, proving the leg gains **no new** run-written discriminator. The earlier wording concluded
  "the leg branches on nothing the run wrote", which is false — it reads `phase`, `witness` and `base`
  from the run-state file on every iteration, and the leg's own comment concedes it. An overstated
  boundary claim is exactly what this unit's S8 exists to stop the protocol from making.
- **AC9** — When `bash tools/unattended/adopt-unattended.sh --check` runs, the rendered Skill matches
  the template plus the conf and carries no surviving placeholder, with S7's precondition present.
- **AC10** — When the leg's shipped-equals-installed check runs, `PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md` agree after S8, **and both contain an `ANCHOR_SCOPE` row in
  section 8's key table and a fifth cost in section 1**. The byte-comparison alone is green today,
  green if S8 is skipped entirely, and green if both copies are edited to omit exactly those two
  things — so it observed nothing about the unit's headline deliverable. The content half follows the
  shape AC9 already uses.
- **AC11** — When `python tools/memory-tree/check-arms.py` runs, both unattended files are fully
  armed and the `ARMS_FLOORS` pairs in `.memory-tree.conf` match a fresh measurement.
- **AC12** — When `bash tools/unattended/adopt-unattended.test.sh` runs, the adopter e2e is green,
  including its junction arm, proving S5's new key did not break the render for an adopter.
- **AC13** — When a branch-anchored run is carried through `--close`, the `authorization-reachable`
  DoD item is met without an override, and `--landed` then reaches the terminal phase. Every
  driver-side criterion above stops at `--preflight`, so F4's ratified resolution — that such a run
  does reach the terminal phase — had no observation at all, and §4's Inventory rows asserting
  downstream consumers are unaffected were untested claims.
- **AC14** — When a branch-anchored run's build folder reaches the default branch mid-run and the run
  then calls `--close`, it does NOT refuse. This is S12's observation and the wedge has no attacker in
  it.
- **AC18** — When a run-state file records a BASE that lies on NEITHER derivation, `--close` still
  refuses with `fail 18`. This is the failing case S12's widening owes: the guard now fires on a
  strictly smaller set, and without this criterion "monotone" and "deleted" look identical from
  outside.
- **AC15** — When the run pushes its branch a SECOND time after preflight, `bash
  tools/unattended/check-unattended.sh` still passes over that record. This is S6's reachability
  form; under the equality form it reds, permanently.
- **AC16** — When `bash tools/unattended/check-unattended.sh` runs with the remote unreachable, it
  behaves as S6c specifies, and the arm names which behaviour that is rather than accepting either.
- **AC17** — When the leg runs in a repo declaring `ANCHOR_SCOPE=default-branch` over a
  branch-anchored record, the verdict is the one §4's price list states. This is the observation the
  unconditional leg-side widening owes; without it nothing in the spec set notices that the bar moved
  for adopters who never opted in.

## 7. Gates

- `bash tools/run-gates.sh`, and `GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.
- `bash tools/unattended/check-unattended.sh` — the kit gate, which S6 edits.
- `bash tools/unattended/check-unattended.test.sh` and `bash tools/unattended/unattended.test.sh` —
  the two sibling legs, which S9 edits.
- `bash tools/unattended/adopt-unattended.sh --check` and `bash tools/unattended/adopt-unattended.test.sh`.
- `python tools/memory-tree/check-arms.py` with the `ARMS_FLOORS` pins in `.memory-tree.conf`.
- `python tools/codebase-map/test_codebase_map.py` — the unattended dossier under `memory/map/features/`
  must be re-derived for the new anchor, and the generated artifacts re-rendered.
- `bash tools/check-playbook-parity.sh` — must stay green. **It is NOT a backstop for the leg's check
  count**, which an earlier revision of this line claimed. That gate opens only the three
  `parallel-coding-governance.*` files and carries two declared pairs, neither about a leg check
  count; it never reads `AGENTS.md`, where the count lives. So the `AGENTS.md` row in §4's
  Files-touched has no gate behind it and is a manual obligation — stated plainly rather than left
  looking mechanised, with node `c` concurrently moving the same number.

## 8. Open questions

none — all six forks below are RESOLVED, and the build-level decision that precedes them is recorded
in this build's README. F5 and F6 were opened by the spec audit AFTER the first four were answered,
and neither was a re-litigation: F5 was a mechanism the first revision did not know it needed, and F6
was a cost the owner was not shown when they priced the unit.

- **F1 — the declaration's name and value set.** Options: a boolean-ish key naming the behaviour
  (`ALLOW_BRANCH_ANCHOR=1`), or a scope key with a closed value set
  (`ANCHOR_SCOPE=default-branch|published`). **RESOLVED (owner, 2026-08-16): the scope key.** It
  names the property rather than the mechanism, it leaves room for a third scope without a second
  boolean, and a closed value set means a typo is a refusal instead of a falsy string that silently
  selects the strict path. A boolean whose absence and whose misspelling produce the same behaviour
  is the shape that hides a misconfiguration. S5 carries the refusal set and S9 carries its arm.
- **F2 — does S6 need `TOOL-aStandingWrit-6` first?** That row records that the leg's anchor is not
  observed. S6 makes the leg observe for its own predicate, which repairs that gap along the path
  this unit uses and leaves it open elsewhere in the file. Options: land S6 as specified and narrow
  the row, or block on the row and land the leg's anchor wholesale. **RESOLVED (owner, 2026-08-16):
  land S6 as specified, and rewrite the row to name what remains.** Blocking couples this unit to an
  unspecced one, and a partially observed leg is strictly better than a wholly unobserved one. S10
  carries the row rewrite, and it is a rewrite rather than a close on purpose.
- **F3 — the kit version.** Node `c`'s in-flight `cBriefedPilot` takes this kit to 1.5 across the
  driver literal, the leg literal and the shipped doc marker, and it holds twenty-two open rows on
  the same files this unit edits. Options: bump here, ride theirs, or sequence behind them.
  **RESOLVED (owner, 2026-08-16): do not bump, and land without waiting on node `c`.** The version
  moves once, in the build that owns the move. The owner took the merge cost on the shared files
  rather than sequencing this build behind an unrelated one; whichever lands second reconciles, and
  the value that must stay unambiguous is moved by exactly one build either way.
- **F4 — should a branch-anchored run be allowed to reach `LANDED` at all?** A defensible stricter
  position is that the weaker anchor authorizes building and merging but not the final landing
  observation. Against it: `--landed` already requires HEAD to be an ancestor of the advertised
  default tip, so the work IS on the default branch by the time it is claimed, and refusing there
  would strand a run that has already landed its work in a non-terminal phase no verb can close.
  **RESOLVED (owner, 2026-08-16): no additional restriction.**
- **F5 — OPEN. How is the anchor SELECTION kept stable for the life of a run?** S12 states the
  requirement; it does not state the mechanism, because both candidates have a real cost. **(a) Read
  `anchor-kind` back from the record** and let it select which derivation `trusted_base` performs.
  Simple, and it works — but the value is run-written, and AC8 plus §4's whole "why the leg must not
  read `anchor-kind`" argument exist to keep run-written values off this path. The mitigation is that
  the DRIVER already trusts the record for `base` as evidence and re-derives the commit itself, so
  reading a KIND is arguably the same class of trust; the objection is that this kit has been burned
  three times by exactly that reasoning. **(b) Make the derivation monotone across both anchors**, so
  no discriminator is needed — for instance by having `trusted_base` accept a recorded BASE that is an
  ancestor of EITHER derivation, which keeps `fail 18` reachable only for a base on neither history.
  Cheaper to reason about, but it widens `fail 18` and needs its own arm to show the guard still has a
  failing case. **RESOLVED (owner, 2026-08-17): (b).** It keeps the run-written value off the decision
  path, which is the property this kit keeps paying to preserve, and the widening it costs is one this
  spec can measure. Folded into S12 as the stated mechanism, into §4's `trusted_base` Inventory row,
  into S9 as an arm and into AC18 as the failing case the widening owes.
- **F6 — OPEN. Costs 2 and 3 in §4 were not on the price list the owner accepted.** The owner
  ratified the rule change against "a run can authorize itself". The audit found two more spent
  properties: the leg-side widening applies to adopters who never opt in and cannot be gated on the
  conf, and the roster-integrity comparison becomes satisfiable by construction on the branch anchor.
  Options: **(a) accept all three and land** — the unit does what was asked and the protocol states
  all three costs; **(b) accept 1 and 3, and narrow S6's clause 2** to something a non-opted-in repo
  still refuses, which needs a discriminator outside the run's reach and may not exist; **(c) stop
  here** and take units 1 and 2 only, which was the alternative on the table when the owner chose to
  build all three and which fixes every worktree failure that is not the authorization rule.
  **RESOLVED (owner, 2026-08-17): (a), re-confirmed against the complete price list.** The unit cannot
  deliver what was asked without cost 2, and cost 3 is a property the branch anchor structurally
  cannot carry.

  **What this resolution obliges, beyond saying yes.** S8 writes all THREE costs into the protocol,
  not the one the first revision knew about — §1's cost list grows by the leg-side widening and by the
  roster-integrity qualification, and §1's fourth mechanical property is qualified per anchor rather
  than left standing unconditionally. AC10's content half checks for them. An accepted cost that only
  this spec records is an accepted cost the next reader of the binding document never sees.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the reproduction recorded under this build's `build/`.
- rev-2 · 2026-08-16 · all four forks resolved by the owner. F1's pick folded into S5 as a closed
  value set with its refusals, and into S9 as an arm; F2's into the new S10 and §3's non-goal; F3's
  into §3. F4 changed no scope item, which is what "no additional restriction" means.
- rev-3 · 2026-08-16 · folded the spec audit recorded under this build's `reviews/`, which returned
  BLOCKED with three blockers, two of them here. S6's clause 2 moved from EQUALITY to REACHABILITY —
  equality wedges the moment the run pushes its branch a second time, which is the shape this kit's
  own source records being moved off after a reproduced wedge. §4's price list went from one spent
  property to three: the leg-side widening is unconditional and hits adopters who never opt in, and
  roster integrity becomes satisfiable by construction on the branch anchor. S1 gained the trigger's
  actual mechanism, since `resolve_base` takes no slug and never reads a README and the obvious
  implementation would print a numbered refusal on every successful preflight. New S6b (the four other
  assertions inside the loop S6 rewrites, plus check 15's second half nested in it), S6c (the leg's
  offline behaviour, and it is an unguarded merge-bar leg), S11 (the `rc=2` return contract that gates
  both `fail 16` branches) and S12 (the anchor selection can flip mid-run and wedge `--close`). AC8
  and AC10 were green regardless of the work; AC13-AC17 added, including the first observation of a
  branch-anchored run past `--preflight`. The authored-fact count corrected from eight to ten, with
  the `cBriefedPilot` collision named. §7's claimed backstop for the AGENTS.md count does not read
  AGENTS.md. F5 and F6 opened.
- rev-4 · 2026-08-17 · F5 and F6 resolved by the owner. F5 picks the MONOTONE derivation over reading
  `anchor-kind` back, so S12 states the mechanism, `trusted_base`'s Inventory row becomes
  "ancestor of EITHER derivation", S9 gains the widened-guard arm and AC18 carries its failing case.
  F6 re-confirms the rule change against the complete three-cost price list, which obliges S8 to write
  all three into the protocol and qualify §1's roster property per anchor rather than only recording
  them here. The spec is no longer FORKED; every fork in it is resolved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "unattended run authorization anchor observed from the
remote"` returned no symbol-level seam, which is the correct answer and not an absence of diligence:
the anchor machinery is a set of file-local functions in one copy-installed kit, so it has a fan-in of
one and never reaches the map's seam threshold. The seams this unit wires through are named directly.

`observe_anchor` in `tools/unattended/unattended.sh` already carries every precondition the second
observation needs — one remote, the same fetch and push endpoint, no injected git config, no
object-substitution lever, and the `GIT()` dereference pin — so S1 extends that function's result
rather than opening a second, differently-guarded path to the remote. Reusing it is what keeps the
new observation from becoming the weaker of two spellings.

`check_authorization`'s BODY is reused (S3): it already takes the base as a parameter and asserts
shape at it, which is why a second anchor needs no second authorization predicate. Its signature moves
only to carry S1's plumbing.

**An earlier revision of this section said the region and roster comparisons "apply to the branch
anchor unchanged". They do not, and the correction is in §4's price list as cost 3.** The comparisons
still RUN, but the roster one stops being an integrity check: it compares the region at BASE against
the working copy, and on the branch anchor BASE is a tip the run itself pushed, so the run can
re-satisfy it against its own new bytes. Protocol section 1 lists that as a mechanical property, which
is why S8 qualifies it per anchor instead of leaving it standing.

The fixture shape is reused from `build/repro-c3.sh` under this build, which itself follows the bare
origin with an advertised HEAD symref that `tools/unattended/unattended.test.sh` established. No new
test harness is introduced.
