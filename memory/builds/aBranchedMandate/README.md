---
slug: aBranchedMandate
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aBranchedMandate-1 TOOL-aBranchedMandate-2 TOOL-aBranchedMandate-3 TOOL-aBranchedMandate-4 TOOL-aBranchedMandate-5 TOOL-aBranchedMandate-6
---

# aBranchedMandate — an unattended run stops needing its build landed first

Node `a` · opened 2026-08-16 · streams tooling.

The commissioning report was one sentence: unattended build tooling will not execute unless the build
and its specs are landed on the default branch, and starting a run from a worktree fails. A build
specced and ready in a worktree should be runnable there.

The reproduction found **three** causes, not one. They fire in a fixed order, and the cause the
report names fires last — so fixing only it leaves every worktree run still refused. All three are
enumerated with their observed output in
[`build/2026-08-16-build-aBranchedMandate-1-worktree-refusal-reproduction.md`](build/2026-08-16-build-aBranchedMandate-1-worktree-refusal-reproduction.md),
and the third has a committed fixture at [`build/repro-c3.sh`](build/repro-c3.sh) that exits 0 only
when it reproduces the specific refusal it is about.

| | What refuses | Fires when | In the report? | Unit |
|---|---|---|---|---|
| C1 | driver check 4, via the wiring check's eol arm | a worktree carries CRLF on the pinned `.claude/` renders | no | unit 2 |
| C2 | the merge bar, via one adopter's byte-compare | the same condition | no | unit 1 |
| C3 | driver check 6, the authorization | the build README is not on the default branch | yes | unit 3 |

C1 refuses `--preflight` before C3 is ever evaluated — confirmed against a build that IS on the
default branch. C2 does not block the start; it blocks `--close`, because the `gates-green`
Definition-of-Done item runs the declared merge bar, and that bar is red in such a worktree before any
work is done.

**The "fires when" column for C1 and C2 said "any fresh worktree" and that was wrong.** The spec audit
challenged it and re-measurement refuted it: `git worktree add` produces CR=0 and both checks green.
The CRLF is written by the agent harness's worktree creation, is confined to `.claude/`, and is
present in all five live worktrees and in none of the trees git makes. The refusals were observed
exactly as recorded; only their cause was misattributed, and four acceptance criteria keyed to the
false cause have been re-keyed to constructed fixtures.

**C3 is not a defect.** `memory/guides/UNATTENDED-PROTOCOL.md` section 1 states it as ratified
design, with four costs the owner enumerated and accepted. Unit 3 is therefore a **rule change**,
and its §4 prices **three** spent properties: a run gains the ability to authorize ITSELF rather than
only its successor; the leg-side widening is unconditional, so the bar weakens for adopters who never
opt in; and roster integrity becomes satisfiable by construction on the branch anchor. The first
revision priced only the first and called it the whole price — the spec audit found the other two, and
the owner re-confirmed the change against the complete list on 2026-08-17. Units 1 and 2 carry no such
trade: they are a missing normalisation and a report severity.

The table below is GENERATED from the status header of every spec in this folder — do not hand-edit
it.

<!-- gen:build-index -->
**Build status:** DEFERRED · 4 unit(s) · node a · opened 2026-08-16 · streams tooling · ids TOOL-aBranchedMandate-1 TOOL-aBranchedMandate-2 TOOL-aBranchedMandate-3 TOOL-aBranchedMandate-4 TOOL-aBranchedMandate-5 TOOL-aBranchedMandate-6

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aBranchedMandate-1 — the memory-recall adopter stops reding the bar on a checkout artifact](spec/2026-08-16-spec-TOOL-aBranchedMandate-1.md) | CLOSED | rev-4 | 2026-08-17 |
| [TOOL-aBranchedMandate-2 — a checkout artifact stops refusing every unattended run in a worktree](spec/2026-08-16-spec-TOOL-aBranchedMandate-2.md) | CLOSED | rev-5 | 2026-08-17 |
| [TOOL-aBranchedMandate-3 — a build published on the run's own branch may authorize the run](spec/2026-08-16-spec-TOOL-aBranchedMandate-3.md) | DEFERRED | rev-5 | 2026-08-17 |
| [TOOL-aBranchedMandate-4 — the unattended adopter decides repo membership without comparing path strings](spec/2026-08-17-spec-TOOL-aBranchedMandate-4.md) | CLOSED | rev-4 | 2026-08-17 |

Records live under `spec/`, `build/` and `reviews/`.
<!-- /gen:build-index -->

## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

Each cell is a label, not a description. The unit's §1 Goal owns the full statement.

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBranchedMandate-4` | 2 | the adopter's repo-membership derivation |
| 2 | `TOOL-aBranchedMandate-1` | 1 | one adopter's missing CR normalisation |
| 3 | `TOOL-aBranchedMandate-2` | 2 | the eol arm's report severity, and the driver's remedy line |
| 4 | `TOOL-aBranchedMandate-3` | 2 | the second authorization anchor |

**The order is TOTAL, and it changed when unit 4 arrived.** Two constraints fix it.

`TOOL-aBranchedMandate-4` goes FIRST. The `unattended adopter e2e` leg is guarded in
`tools/gate-legs.json` on `tools/lib/` and `tools/unattended/`, and both `TOOL-aBranchedMandate-2` and
`TOOL-aBranchedMandate-3` edit files under `tools/unattended/`. So their own diff-scoped gate runs
execute the leg unit 4 exists to repair, and M6's pass loop does not continue past a red gate. Every
later unit inherits that red until unit 4 lands.

`TOOL-aBranchedMandate-1` still precedes `TOOL-aBranchedMandate-2`. Unit 2's whole argument is that
the eol arm's exit status is unfunded — that no gate reds on CR any more — and that becomes true only
when unit 1 lands. Landing unit 2 first would silence a signal still correctly predicting a red leg.

`TOOL-aBranchedMandate-3` is last because it is the one that changes a ratified rule. That decision
has been made, so its position is a build ordering rather than a gate on approval.

## What each unit is worth on its own

Stated when a subset was still on the table. The owner took all three, so this is now the record of
what was weighed rather than a menu.

- **Units 1 and 2 alone** fix every worktree failure that is not the authorization rule. After them,
  a run started from a worktree on a build that IS on the default branch works, and the merge bar is
  green in a fresh worktree. Neither unit changes a security property.
- **Unit 3 alone** is not deliverable: a run it authorizes still meets C1 at preflight and C2 at
  close.
- **Unit 3 on top of 1 and 2** is what answers the report as written, and it is the only one of the
  three that spends something.

## Build-level rules

- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal for that sits at a pin with zero tolerance, and `tools/` — which all four units
  edit — is inside its globs. Provenance goes in the commit message, not in a source comment.
- **Every unit that edits a `fail` branch re-measures `ARMS_FLOORS`** in `.memory-tree.conf` rather
  than assuming its pair is unchanged. Both unattended files carry a pinned pair, and a message edit
  that leaves an arm no longer matching its branch's full literal signature is the trap this repo
  carries in writing and has still paid for twice.
- **The two protocol copies move together or not at all.** The kit's `PROTOCOL.template.md` and the
  installed `memory/guides/UNATTENDED-PROTOCOL.md` are byte-compared by the kit gate.
- **Node `c` has a live build on these exact files.** `cBriefedPilot` holds twenty-two open rows on
  the unattended kit and takes it to version 1.5 across three literals. **No unit here bumps that
  version**, and this build does not sequence behind theirs — unit 2 §8 F2 and unit 3 §8 F3. Whoever
  lands second reconciles. A unit that finds itself needing to move the version literal has hit a
  changed premise and stops rather than moving it.
- **Two values are STOP-AND-RECONSIDER, not just merge-carefully.** The kit version literal above,
  and **the authored-fact count in protocol section 2**. `memory/builds/cBriefedPilot/README.md`
  states "No eighth authored fact" as the premise for routing its own waiver through fact 3, while
  unit 3's S4 moves that count to ten. Whichever build lands second is changing a number the other
  build reasoned from, and the correct response is to stop and re-read, not to reconcile the number.

## PARKED — unit 4 (`TOOL-aBranchedMandate-3`), by the unattended run of 2026-08-17

Units 1 and 2 of the order (`TOOL-aBranchedMandate-4`, then `-1`, then `-2`) are CLOSED and landing.
`TOOL-aBranchedMandate-3` is DEFERRED and NOT built. The stop-and-reconsider rule above fired, on
both of the two values it names.

**The question, unanswered on purpose.** Does the owner's ratification of unit 3 — given against a
three-cost price list on 2026-08-17 — still stand now that the document carrying that price list has
changed underneath it? `origin/main` gained `dClosedLexicon`'s unattended work mid-run: the kit
version is 1.6 rather than the 1.5 F3 reasoned about, protocol section 2 gained a subsection, the
leg gained a sixteenth check, and the `for b in refs/remotes/…` loop that S6b enumerates item by item
no longer exists. The authored-fact count S4 moves from "seven" was already eight before this run
started, so both this README's collision note and S4's arithmetic are off by one.

**The options seen.** (a) Re-derive S6b and S4 against the merged leg and build it — rejected: S6b's
obligation is to state the disposition of five assertions inside a loop that is gone, which is
re-specifying a security predicate, not re-pointing a citation. (b) Build the mechanical parts and
leave S6b — rejected: S6's rollout section requires the leg and the driver to land in one commit,
so a half-built unit writes records that red the bar on the next push. (c) Park, land units 1 and 2,
and hand the re-pricing back. **Taken.**

**Why refused rather than decided.** M3 delegates fork resolution, not scope, and this is not a fork
in any spec — it is whether a ratified price is still the price. Units 1 and 2 were always a
deliverable subset: this README's own "What each unit is worth on its own" records that they fix
every worktree failure that is not the authorization rule and spend no security property. Unit 3's
full drift table is in its own §9 rev-5.

## Owner decisions — RESOLVED 2026-08-16

The decision prior to every fork, because it is not a fork in any spec: **is the price in unit 3's
§4 worth paying** — the price being that a run stops being able to authorize only its successor and
becomes able to authorize itself. **Answered: build all three.** The alternative on the table was
units 1 and 2 alone, which fixes every worktree failure except the authorization rule and spends no
security property. It was declined in favour of answering the report as written.

All eight forks are resolved and marked in place in each spec's §8. **Eight, not seven** — an earlier
version of this table listed seven and omitted unit 2's F3, which is exactly the completeness defect
this repo has paid for before. F3 turned out not to be a fork at all: it carried no options and no
trade, its answer was entailed by F1, and it has been reclassified into unit 2's §4 with the
reclassification recorded rather than the row silently vanishing.

| Fork | Question | Resolution |
|---|---|---|
| unit 1 F1 | where the CR regression arm lives | fold into `tools/memory-recall/selftest.py`; no new leg |
| unit 2 F1 | the label for the non-gating eol line | `note` |
| unit 2 F2 | bump the kit version here | no, and land without waiting on node `c` |
| unit 2 F3 | — | not a fork; reclassified into §4 |
| unit 3 F1 | the declaration's name and value set | `ANCHOR_SCOPE`, closed value set, absent or misspelled refuses to widen |
| unit 3 F2 | block on the tracked row for the leg's anchor | land S6 as specified; rewrite the row to name what remains |
| unit 3 F3 | the kit version, against node `c`'s in-flight bump | do not bump; land regardless of order |
| unit 3 F4 | may a branch-anchored run reach the terminal landing phase | no extra restriction |

Two resolutions created work that was not in the specs when the forks were put, and both are carried
as scope items rather than left implicit. Unit 3 gains **S10**, the rewrite of the tracked row for
the leg's anchor — a rewrite and not a close, because S6 repairs that gap only along its own
predicate's path. Unit 3's S9 gains an arm for the new declaration's refusal set, because a
value-set guard whose failing case is untested is the guard that silently admits.

**F2 and F3 both chose to land without sequencing behind node `c`.** The merge cost on the shared
files is accepted; whichever build lands second reconciles. The version literal is still moved by
exactly one build.

## The spec audit — BLOCKED, folded at rev-3

`reviews/2026-08-16-review-aBranchedMandate-1.md` records an M4 audit run as a five-lens workflow with
batched default-refute skeptics under the review protocol's caps: 45 raw findings, 36 confirmed,
9 refuted, none unverified, deduplicated to 18. **Verdict BLOCKED, three blockers.** All 18 are folded;
every spec is at rev-3 with its §9 line.

The most important one refuted this build's own causal premise. C1 measured that `git worktree add`
does NOT land CRLF — so unit 1's AC3 was already green with the fix reverted, unit 1's AC5 was
unsatisfiable, and unit 2's AC1 named a fixture that cannot be created. That is the
`fixture-passes-by-finding-nothing` class, in the build that lists it on its own checklist. It was
re-verified here before folding, not taken on the reviewer's word.

The other two blockers were both in unit 3: S6 respecified a gate predicate as EQUALITY, the exact
shape `check-unattended.sh` records the kit being moved off after a reproduced permanent wedge; and
§5 priced the change as "defaulted off" when the leg-side half is unconditional and cannot be gated on
the conf. A fourth finding, C9, established that the price list the owner accepted was **incomplete** —
roster integrity is a second ratified property this unit spends, and §10 had asserted the opposite.

The audit opened three further forks, all after the owner's earlier resolutions and none of them a
re-litigation. **All three were put to the owner and answered on 2026-08-17**, so no spec in this
build is FORKED any more:

| Fork | Question | Resolution |
|---|---|---|
| unit 2 F4 | the CRLF writer is unidentified; may a severity downgrade rest on that | land as specified — the report survives, only the gating goes; the residual stays written down |
| unit 3 F5 | how the anchor selection is kept stable without reading a run-written value | a MONOTONE derivation: accept a BASE that is an ancestor of EITHER anchor, so nothing selects |
| unit 3 F6 | costs 2 and 3 were not on the price list the owner accepted | re-confirmed against the complete list; S8 must now write all three into the protocol |

Two of the three created obligations rather than merely ratifying, and both are scope items now, not
implications. F5's monotone derivation WIDENS `fail 18`, so unit 3 gains an arm and AC18 — a widened
guard with no failing-case arm is indistinguishable from a deleted one, and this build widens two
guards. F6's re-confirmation binds S8 to put all three costs and the per-anchor roster qualification
into the binding document, because a cost recorded only in a spec is one the next reader of the
protocol never sees.

**The fold itself is unreviewed**, by M4's stop rule: fixes are folded once and reviewing resumes only
if the design moves again. A second audit is a decision, not an obligation.
