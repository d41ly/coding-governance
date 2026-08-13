# TOOL-cFinalBerth-2 — the close that survives the landing it precedes

**Status:** SPECCED · rev-2 · 2026-08-13 · node c · Tier-2 · base f006691f · streams tooling · ratified 2026-08-13

## 1. Goal

Stop `--close` refusing every run whose HEAD is already published. The refusal fires on the state
that follows a successful landing, and it cannot tell that state from a run that built nothing. It
becomes conditional on the discriminator that can.

## 2. Scope (IN)

- **S1** — **The degenerate refusal at `--close` becomes conditional.** A merge-base equal to HEAD is
  accepted when the record shows work was built on the pin, and refused when it does not. The by-verb
  split survives: `--preflight` keeps its early acceptance, `--close` keeps a refusal, and only the
  refusal's QUESTION changes.
- **S2** — **The recorded base decides only WHETHER to refuse, never WHAT is compared.** The value
  handed to the authorization comparison stays the derived, published commit. The recorded value is
  read as a discriminator and never becomes the base the comparison reads.
- **S3** — **Three named refusals on the new path**, because an absent or unreadable discriminator
  must fail closed: the record carries no base line, the recorded base does not resolve to a commit,
  and the recorded base equals HEAD. The third is the run that built nothing, which is the case the
  original refusal existed for.
- **S4** — **The degenerate path stops skipping the recorded-base cross-check.** Today it returns
  early on every caller that is allowed it, so the comparison between the recorded base and the
  derived one never runs there. On the `--close` path it now runs.
- **S5** — **The false premise is corrected where it is written.** The refusal text and the comment
  above it assert that a merge-base equal to HEAD means the run authored every byte the authorization
  comparison reads. Under an observed anchor it means the opposite, and the driver already says so in
  the preflight comment that blesses the same state.
- **S6** — **The paired by-verb arm is rewritten, not deleted.** It runs `--preflight` and `--close`
  against the same fixture one command apart, which is what shows the VERB differs and not the tree.
  It gains a third branch: `--close` on the same fixture with work committed on top of the pin is
  ACCEPTED. All three run against one fixture.
- **S7** — **The stuck record is repaired.** The run at `aSealedCaravan` landed and its record still
  reads `BUILDING`. It is moved to `LANDED` with the landing sha as its witness, as a records repair
  rather than a close. This is independent of S1 through S6 and of unit 1.
- **S8** — **The arms floor for the driver moves** to cover the branches this unit adds, net of
  unit 1's.

## 3. Non-goals (OUT)

- **Deleting the refusal.** Put to the owner on 2026-08-13 and refused; see section 8. The guard
  stays at `--close`, and only its question changes.
- **Removing the caller keyword.** The by-verb split is the owner-ratified shape and it survives, so
  the keyword that expresses it survives with it.
- **Running `--close` against the stuck record.** The run is over and its process is gone; closing it
  from an unrelated branch would evaluate the Definition of Done against this tree rather than the
  one it ran on. S7 is a repair of a record and says so rather than dressing it as a close.
- **Any change to what the authorization item ASSERTS.** It still re-derives its own base and still
  reads the build README at it. Its VERDICT on the degenerate path changes from an unconditional
  refusal to a conditional pass; the assertion does not.
- **Leg check 9's phase list**, including the removal of the aborted phase from it. Unit 1 owns that.
- **The leg's anchor independence**, owned by the open row `TOOL-aStandingWrit-6`.

## 4. Design

### What was reproduced, with a control

Run on this build's own tree at base `f006691f`, before any commit existed on the unit branch, which
is what made HEAD an ancestor of the advertised tip:

| Step | Observation |
|---|---|
| control, before | the record hashes `89e85861` |
| `--close` on a published HEAD | check 16 fires — *the merge-base equals HEAD, so the run authored every byte the authorization comparison would read* — and the authorization item is reported unmet as its consequence |
| control, after | the record hashes `89e85861`, unchanged, and its phase still reads `BUILDING` |

The control is the half that matters: a failing close writes nothing, so the refusal is a wedge
rather than a corruption. HEAD at the time was `f006691f`, the tip the remote advertises for its own
default branch — published, and authored by other nodes. The refusal's sentence is false about the
state it fired on.

### What the guard is, and who ratified it

This is not an incidental branch. The `aStandingWrit` spec scoped it BY VERB as its S3 — legal at
`--preflight`, a refusal at `--close` and in the gate leg — and its section 8 fork F2 records
**RESOLVED (owner, 2026-08-11): keep equality**, reasoning that relaxing a guard for a hazard nobody
has reproduced is how the anchor bypass survived two reviews. The driver's own comment cites that
ratification as the reason the branch survives, and a dedicated paired arm in the driver's self-test
runs `--preflight` and `--close` against one fixture a command apart to prove the verb is what
differs. All three are cited here because a unit that changes a ratified guard without naming its
ratification is asking the owner to re-decide blind.

### Why the question changes, and what stays

Two things moved since the ratification. The anchor became an OBSERVATION of the remote rather than
a local ref the run could rewrite offline, so a merge-base equal to HEAD now means HEAD is an
ancestor of the tip the remote advertises — published — where it once meant *the anchor is my own
commit*. And the hazard is no longer unreproduced: the wedge is reproduced above, with a control, on
an honest tree with no attacker.

What the guard bought was the refusal of a run that built nothing. The merge-base cannot express
that, because it is equal to HEAD in both the built-nothing state and the fully-landed state. The
recorded base can, because it is pinned once at preflight and does not move:

| State | merge-base vs HEAD | recorded base vs HEAD |
|---|---|---|
| a run that has built nothing | equal | equal — refused by S3 |
| a run whose work is fully landed | equal | differs — accepted |

So the guard stays at the verb the owner put it at, and its question becomes the one that can
distinguish the two states.

### The residual, stated because it is the cost the owner accepted

The recorded base is written by the run. Reading it as a discriminator therefore lets a run edit one
line to pass this specific refusal. Three things bound that, and none of them makes it disappear:

1. The discriminator decides only whether to refuse. The commit the authorization comparison reads
   is the derived, published one, so a forged discriminator does not forge the comparison.
2. An ABSENT or unresolvable value is a refusal, not a pass. The kit's recorded scar here is a
   deleted base line degenerating a comparison to the git index, and failing closed is what keeps
   this path out of that class.
3. Leg check 9 asserts the same facts independently on the bar — the recorded base resolves, is an
   ancestor of the anchor, is an ancestor of HEAD, and is not HEAD at a work-claiming phase.

The honest summary is that this narrows a refusal that could not be forged into one that can be, and
buys a kit that can close a landed run. That trade was put to the owner with the cost named and
chosen.

### Inventory

| Change | Site |
|---|---|
| the degenerate case at `--close` is decided by the recorded base | the driver's base resolver |
| three named refusals on that path: absent, unresolvable, equal to HEAD | the same resolver |
| the derived commit stays the value returned | the same resolver |
| the degenerate path on that caller runs the recorded-base cross-check | the same resolver |
| the false comment and refusal text are corrected | the same resolver |
| the paired by-verb arm gains an accepted third branch | the driver self-test |
| the record moves to a terminal phase with the landing sha as witness | the stuck run-state file |

### Rollout

Two commits. The resolver change and its arms land together, because changing a refusal and moving
its floor in separate commits leaves the meta-gate red in between. The record repair is the second,
so the diff that changes behaviour and the diff that changes a record are separable.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `.memory-tree.conf` ·
`memory/builds/aSealedCaravan/RUN.md` · `memory/backlog/TOOL.md` · `memory/DECISIONS.md`

### Alternatives rejected

**Deleting the refusal outright**, which rev-1 specced. Put to the owner and refused; the guard stays
at the verb it was scoped to.

**Keeping it unchanged and closing before landing.** That is the intended order and it works, but it
leaves the kit unable to close any run that already landed, including the one in this tree, and
leaves a false sentence on the authorization path.

**A phase-keyed carve-out** — skipping the check when the phase is terminal. Rejected for the reason
the `aMooredAnchor` spec recorded: the phase is run-written, so it is a one-line escape. The recorded
base is also run-written, which is why S2 confines it to the discriminator role and S3 fails it
closed.

## 5. Production-readiness checklist

- security — the change narrows a refusal on the authorization path, so the reasoning, the
  ratification it revisits and the residual it accepts are all written out above rather than implied.
- perf / scale — no new process, no new remote call.
- a11y — N/A — a shell driver with no user interface.
- i18n — N/A — this repo's tooling is English-only by charter.
- error / empty / loading states — three named refusals on the new path, all failing closed.
- observability — the close path already prints which item is unmet; the new refusals print which of
  the three conditions fired.
- risks — the accepted residual is a run-written discriminator, bounded three ways in section 4 and
  named in section 8; a run that built nothing is still refused.
- testing + left-shift gates — the paired by-verb arm gains a third branch, and each of the three new
  refusals gets a positive arm.
- migration / rollback — no record changes shape; rollback is a revert, after which the wedge
  returns.
- user docs — none: the protocol does not describe the degenerate case, and the by-verb split it does
  not describe is unchanged.

## 6. Acceptance criteria

- **AC1** — When `--close` runs in a fixture whose HEAD is an ancestor of the advertised tip, on a
  record whose recorded base is an ancestor of HEAD and not equal to it, it no longer refuses on the
  merge-base and the record moves to `LANDING`.
- **AC2** — When `--close` runs in that same fixture on a record whose recorded base EQUALS HEAD, it
  refuses naming the built-nothing condition. This is the control for AC1 and the survival of the
  property the original guard bought.
- **AC3** — When `--close` runs on that fixture with the base line deleted, it refuses naming the
  absent pin; when the recorded base names a commit this history does not carry, it refuses naming
  that.
- **AC4** — When `--preflight` runs on the same fixture one command earlier, it is accepted and its
  output does not name the merge-base condition; the three `--close` branches above run against that
  same fixture, so the verb is what differs and not the tree.
- **AC5** — When the degenerate path runs at `--close` with a recorded base that is not an ancestor
  of the derived base, it refuses, proving the cross-check the early return used to skip now runs.
- **AC6** — The record at `aSealedCaravan` reads phase `LANDED` with the landing sha as its witness,
  the leg is silent over it, and the leg counts no non-terminal run in the tree.
- **AC7** — `bash tools/run-gates.sh` is green, including the arms meta-gate at the adjusted floor.

## 7. Gates

The five unattended legs, the harness meta-gate at the adjusted floor, the memory-tree hygiene gate
over the repaired record, and the full bar. No new gate leg, so the codebase-map inventories do not
move.

## 8. Open questions

none — the fork below is RESOLVED and the resolution is the owner's own, taken on the question as
asked rather than inherited from the scope decision that folded this unit into the build.

**F1 — may the merge-base-equals-HEAD refusal at `--close` be deleted?** It was scoped by verb as the
`aStandingWrit` spec's S3, ratified as that spec's section 8 fork F2 (owner, 2026-08-11, "keep
equality"), and the driver cites that ratification as the reason it survives. This unit argued the
premise expired because the anchor moved from a local ref to an observation, and that the property it
bought survives at leg check 9. The builder's recommendation was to delete.
**RESOLVED (owner, 2026-08-13): narrow it rather than delete it.** The guard stays at `--close` and
fires on the recorded base instead of the merge-base. The owner was told, before answering, that this
makes a run-written value an input on the authorization path and that the kit has a recorded scar in
that class; section 4's residual paragraph is the accounting of what was accepted.

## 9. Revision log

- rev-1 · 2026-08-13 · initial draft, written after the wedge was reproduced live on this tree with a
  before-and-after control rather than argued from the source.
- rev-2 · 2026-08-13 · folded the M4 spec audit, verdict BLOCKED. The blocker was rev-1's section 8,
  which signed `(owner, 2026-08-13)` for a fork the owner had never been asked — the decision it
  cited was the SCOPE answer that folded this unit in — while the unit deleted a guard the owner had
  ratified by name and a paired arm pinned. The fork was put to the owner properly and answered
  NARROW rather than DELETE, so S1 through S4 are rewritten from a deletion to a conditional refusal,
  S6 rewrites the arm instead of removing it, and rev-1's acceptance criterion asserting the keyword
  was gone is withdrawn because the keyword stays. Also corrected rev-1's S2, which claimed the
  change was "strictly stricter, not looser" — true for `--preflight`, the only caller that took the
  early return, and false for `--close`, which is the caller the sentence named. Status moves OPEN to
  SPECCED.

## 10. Reuse audit

No new seam is introduced; this unit changes one branch's question and routes one path through
machinery that already exists. The seams it reuses, each verified against source at this spec's base:

- the driver's base resolver and its recorded-base cross-check — the degenerate path at `--close` is
  routed into the cross-check that already exists rather than gaining one of its own.
- the driver's fact reader — the discriminator is read with the accessor every other verb uses, so
  there is no second parser for the authored region.
- leg check 9's recorded-base assertions — cited as the independent bound on the residual rather than
  duplicated in the driver, because a rule in two carriers is a defect in the second.
- the paired by-verb arm in the driver self-test — extended with a third branch on the same fixture,
  which is the shape that made the original split provable.
- the reproduction shape from the `aMooredAnchor` build — a control before and after every defeat,
  which is what turned this unit's claim from a reading of the source into an observation.

Recall terms used: unattended, close, degenerate, merge-base, anchor, observed, authorization,
reachable, base, recorded, landing, wedge. The probe returned the parked entry in the stuck run's own
record as its top hit, which is where the defect was first written down by the run that hit it.
