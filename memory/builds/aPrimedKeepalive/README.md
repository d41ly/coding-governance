---
slug: aPrimedKeepalive
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
ids: TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6
authorized-by: prompt
---

# aPrimedKeepalive — an unattended run keeps itself alive from its first act, and adopts a beneficial discovery instead of waiting for the owner who left

Node `a` · opened 2026-08-27 · streams tooling.

The owner reports two defects in the unattended-run kit, and both are the same failure wearing two
faces: **a run that stops, with nobody there to notice.** Each was verified against source before a
line of this file was written. Orientation then found two more instances of the same family already
tracked and already reddening this repo's own bar, and the owner ruled them into this build.

The prompt is recorded verbatim at
[the prompt record](prompts/2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md); this file states the
build in its own words.

## The problem this build exists to solve

A run that cannot be woken and a run that will not decide are the same outage from the owner's side:
the terminal goes quiet and stays quiet. The kit already knows this — it is why the keepalive exists
and why `--park` demands a reason — but three of its four start paths never schedule the keepalive
before their longest unattended stretch, and nothing in the method tells a run what to do with
something good it was not looking for. So the two named defects are not a coincidence; they are the
two halves of one hole.

## Defect A — three of four start paths orient with no keepalive

`SKILL.template.md` schedules the keepalive at **step 3 of the slug path** and nowhere else. The
PROMPT path (its steps 1–6) and the PLAYBOOK path (its steps 0–6) both orient, research and decide
BEFORE they preflight, and both reach preflight through "exactly as the slug path does" — which
carries the preflight call and silently drops the step before it.

The protocol says the same thing in the same shape. Section 5: *"The **agent** schedules the
keepalive before the run leaves `PREFLIGHT`"*. A run has not entered `PREFLIGHT` until `--preflight`
writes it, so that sentence is satisfied by scheduling at preflight time — and the two prompt-bearing
paths do their longest unattended work before that instant. M12's research-then-test loop happens
there. A run stalled in it has no keepalive, so nothing wakes it and nothing records why.

`aGroundedOrientation` is the reported instance: it stalled in orientation, and there was no
keepalive to bring it back.

## Defect B — nothing tells a run to adopt what it finds

M2 already names ADD as an amendment act, M3 already delegates a build's own scope to a standing
mandate, and `--rescope --act add` already writes the row. Every mechanism this needs exists. What
does not exist is the sentence that says **use them** — so a run that finds something good outside
its scope falls back to the nearest rule it can see, which is M3's *"a fork the goal cannot survive
is still not yours — park it"*, and parks.

`aGroundedOrientation` again, and this is the sharper half: it found a scoped hygiene-check fix
worth **1000 s → 60 s on a git commit**, parked it, and waited. Told to proceed, it parked the fix a
second time. A run that has measured a sixteen-fold improvement and files it as a question for an
absent reader has not been careful; it has thrown the finding away and called it diligence.

## Defect C — this repo's own bar is already red, for the same reason

Measured at BASE, before this build wrote anything:

| Record | Phase | What reds | Tracked as |
|---|---|---|---|
| `memory/builds/dCarriedReceipt/RUN.md` | `LANDED` | check 15 — no `landed-anchor`, first commit 2026-08-25, after the declared cutoff | `TOOL-dScaffoldedMirror-22` |
| `memory/builds/dTieredTribunal/RUN.md` | `LANDING` | check 7, the moment a second run goes live | `TOOL-aBoundedVerdict-24`, `TOOL-aFusedCharter-4` |

Both are runs that could not reach a truthful terminal state. `dTieredTribunal` merged and pushed —
`b4e1d5be` is the tip the remote advertises — and then could not stamp its own record, because
`--landed`'s check 34 wants a lander marker naming the witness and node `a`'s marker names an older
commit. `TOOL-dUnstalledConvoy-38` records the predicate that check should have used.

`dCarriedReceipt` has a recorded remedy used twice already: hand-complete `landed-anchor: remote`
after confirming the witness independently. Its witness `04c7da24` is an ancestor of `origin/main`,
verified with `git merge-base --is-ancestor` before this line was written.

## Defect D — the owner's own example is still unapplied, and it taxed this build's first commit

The prompt cites a "scoped hygiene check fix that takes git commits from 1000s to 60s" that
`aGroundedOrientation` parked twice. It is still parked. Verified at BASE: the block at
`tools/memory-tree/check-memory-hygiene.sh:1113` holding checks 22 and 23 opens on
`if [ -n "$alcut" ]` alone, while all three of its siblings at `:1051`, `:1066` and `:1076` open on
`if [ "$STAGED" = 0 ]`. So the pre-commit fast leg walks every tracked build record and every closed
Tier-2 spec on every commit, and this build's own first commit timed out at 120 s because of it.

The file's own header states the split it is supposed to have — *"set-checks tree-wide, file-checks
on staged paths"* at `:9` — and `:732` names CI's full run as the tree-wide truth. This is a one-line
omission, not a design.

**It is adopted rather than parked, which is the rule this build is here to write.** Sequenced FIRST,
because every later commit of this build pays the tax until it lands.

## Owner decisions — RESOLVED 2026-08-27

One question was put, at the prompt path's single sanctioned owner turn, before anything was written.

**Q — the bar is already red for two tracked reasons and one worsens the moment this run goes live;
how should the run proceed?** RESOLVED (owner, 2026-08-27): clear both and widen the build. Units 4
and 5 are that ruling.

**And the ASKING was itself corrected**, in the owner's words: *"This is an unattended build, you know
that perfectly. Why did you stop for an askuserquestion? Bring this issue into the build."* The run
reproduced the exact reflex it was sent to remove — a blocker with a derivable, measured resolution,
filed as a question for a reader who had left. Unit 2's rule is written to cover a BLOCKER the run can
resolve and not only a discovery it would be nice to have, and that widening comes from this
correction. No further owner turn is taken by this build.

## Expected improvements

A run wakes from any stall on any start path, including the long pre-preflight stretch the two
prompt-bearing paths spend orienting. A discovery worth having is built by the run that found it
rather than surfaced to a reader who is not there. A record whose work is provably on the remote's
default branch stops holding the whole fleet's bar hostage.

## Detriments if this is not built

The keepalive gap costs a run per stall, silently, on the paths the owner uses most. The adoption gap
costs every finding an unattended run makes outside its own scope, and those are the findings nobody
else is positioned to make. The red bar costs every later run on every node until somebody clears it
by hand.

## Build-level rules

**Classification (M2), first match wins.** Every unit is MISSING at open — no spec carries any of
these ids — so every one is authored first and re-classified.

**M3 veto 2 is not tripped by this build's own subject.** Units 1 through 3 change governance
carriers, and veto 2 makes a carrier change an owner turn. That veto is about a FORK whose resolution
needs a carrier edit as a side effect. Here the carrier edit is the mandate: the owner's prompt asks
for a binding rule, and a binding rule of this kit lives in `UNATTENDED-PROTOCOL.md` and
`BUILD-METHOD.md`. Recorded so a later reader does not mistake the build for a bypass.

**`BUILD-METHOD.md` has 30 bytes of headroom against M1's stated 24 576 B budget, and that is the
binding constraint of unit 2.** M1's budget is a governance carrier's own stated constraint, which
M3's delegation explicitly does not reach — so the budget is not raiseable by this run. A unit that
does not fit trims prose elsewhere in that file under charter §5's derive-over-author rule, or it
raises a fork. Re-measure from `wc -c`, never from this line.

**THE WORK PRECEDED THE PREFLIGHT, and the closing review's base is the MERGE-BASE, not the pinned
BASE.** The prompt path writes the build folder, pushes, then preflights — but this repo's own
pre-commit hook took ten minutes per commit until unit 6 landed, and the build-folder commit could
not be made until that was fixed. So units 6, 1, 2, 3, 4 and 5 are all ancestors of the commit
`--preflight` pinned as BASE, and a review scoped `BASE..HEAD` would read an empty diff. The closing
review runs `b4e1d5be..HEAD`, which is the diff that actually lands. Recorded here rather than parked
because it is a fact about this run, not a question for the owner.

**Every unit re-renders its carrier's pair in the same commit.** The protocol, the Skill and the
build method are each a template plus an installed copy that a leg byte-compares.

## Units — the authored roster (M2)

One mechanism per unit. Each cell is a label; the unit's `§1` Goal owns the statement.

<!-- roster:units -->
| Unit | Tier | Mechanism |
|---|---|---|
| `TOOL-aPrimedKeepalive-1` | 2 | the keepalive is scheduled as the run's first act, on every start path |
| `TOOL-aPrimedKeepalive-2` | 2 | the adoption rule — a strictly beneficial discovery joins the running build |
| `TOOL-aPrimedKeepalive-3` | 2 | the `discoveries-adopted` directive, so the rule is in the set a run reads at step 0 |
| `TOOL-aPrimedKeepalive-4` | 2 | leg check 7 stops counting a LANDING record whose work is already on the remote |
| `TOOL-aPrimedKeepalive-5` | 1 | `dCarriedReceipt`'s record gains the `landed-anchor` its own verb failed to write |
| `TOOL-aPrimedKeepalive-6` | 1 | hygiene checks 22 and 23 take the `--staged` guard all three of their siblings carry |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 6 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPrimedKeepalive-6 — hygiene checks 22 and 23 take the `--staged` guard all three of their siblings carry](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-6.md) | 1 | 1 | OPEN | rev-1 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-1 — the keepalive is scheduled as the run's FIRST act, on every start path](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-1.md) | 2 | 2 | INPROGRESS | rev-2 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-2 — the adoption rule: a strictly beneficial discovery joins the running build, decided at once](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-2.md) | 3 | 2 | OPEN | rev-1 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-3 — the `discoveries-adopted` directive, so the rule is in the set a run reads at step 0](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-3.md) | 4 | 2 | OPEN | rev-1 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-4 — leg check 7 stops counting a LANDING record whose work is already on the remote](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-4.md) | 5 | 2 | OPEN | rev-1 | 2026-08-27 |
| [TOOL-aPrimedKeepalive-5 — `dCarriedReceipt`'s record gains the `landed-anchor` its own verb failed to write](spec/2026-08-27-spec-TOOL-aPrimedKeepalive-5.md) | 6 | 1 | OPEN | rev-1 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: TOOL-aPrimedKeepalive-6.

Ids no `spec-audit` record has ever named: TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-2 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPrimedKeepalive-6` | no |
| 2 | `TOOL-aPrimedKeepalive-1` | no |
| 3 | `TOOL-aPrimedKeepalive-2` | no |
| 4 | `TOOL-aPrimedKeepalive-3` | no |
| 5 | `TOOL-aPrimedKeepalive-4` | no |
| 6 | `TOOL-aPrimedKeepalive-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
