---
slug: aBranchedMandate
node: a
opened: 2026-08-16
streams: tooling
roster: TOOL
ids: TOOL-aBranchedMandate-1 TOOL-aBranchedMandate-2 TOOL-aBranchedMandate-3
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
| C1 | driver check 4, via the wiring check's eol arm | any fresh worktree | no | unit 2 |
| C2 | the merge bar, via one adopter's byte-compare | any fresh worktree | no | unit 1 |
| C3 | driver check 6, the authorization | the build README is not on the default branch | yes | unit 3 |

C1 refuses `--preflight` before C3 is ever evaluated — confirmed against a build that IS on the
default branch. C2 does not block the start; it blocks `--close`, because the `gates-green`
Definition-of-Done item runs the declared merge bar, and that bar is red in a fresh worktree before
any work is done.

**C3 is not a defect.** `memory/guides/UNATTENDED-PROTOCOL.md` section 1 states it as ratified
design, with four costs the owner enumerated and accepted. Unit 3 is therefore a **rule change**
priced as one, and its §4 states plainly what the change spends: today a run can authorize its
successor, and afterwards it can authorize itself. Units 1 and 2 carry no such trade — they are a
missing normalisation and a report severity.

The table below is GENERATED from the status header of every spec in this folder — do not hand-edit
it.

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node a · opened 2026-08-16 · streams tooling · ids TOOL-aBranchedMandate-1 TOOL-aBranchedMandate-2 TOOL-aBranchedMandate-3

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aBranchedMandate-1 — the memory-recall adopter stops reding the bar on a checkout artifact](spec/2026-08-16-spec-TOOL-aBranchedMandate-1.md) | SPECCED | rev-2 | 2026-08-16 |
| [TOOL-aBranchedMandate-2 — a checkout artifact stops refusing every unattended run in a worktree](spec/2026-08-16-spec-TOOL-aBranchedMandate-2.md) | SPECCED | rev-2 | 2026-08-16 |
| [TOOL-aBranchedMandate-3 — a build published on the run's own branch may authorize the run](spec/2026-08-16-spec-TOOL-aBranchedMandate-3.md) | SPECCED | rev-2 | 2026-08-16 |

Records live under `spec/` and `build/`.
<!-- /gen:build-index -->

## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

Each cell is a label, not a description. The unit's §1 Goal owns the full statement.

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBranchedMandate-1` | 1 | one adopter's missing CR normalisation |
| 2 | `TOOL-aBranchedMandate-2` | 2 | the eol arm's report severity, and the driver's remedy line |
| 3 | `TOOL-aBranchedMandate-3` | 2 | the second authorization anchor |

**The order is TOTAL and units 1 and 2 are the reason.** Unit 2's whole argument is that the eol
arm's exit status is unfunded — that no gate reds on CR any more. That becomes true only when unit 1
lands. Landing unit 2 first would silence a signal that is still correctly predicting a red leg,
which is the opposite of what unit 2 claims to be doing.

Unit 3 is independent of both and is sequenced last because it is the one that changes a ratified
rule. That decision has now been made — see the resolutions below — so the ordering is a build
ordering rather than a gate on approval.

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
  The drift signal for that sits at a pin with zero tolerance, and `tools/` — which all three units
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
