# TOOL-aWrittenMethod-2 — the mandate BASE the run cannot steer

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-2 · base 7f614a17 · streams tooling

## 1. Goal

The mandate comparison is the only thing standing between an unattended run and an unreviewed push,
and its BASE is currently chosen by the run. Make every input to that comparison lie outside the
subject's reach, and make the gate leg an independent second opinion rather than a second computation
of the same steered value.

## 2. Scope (IN)

- **S1** — the driver records the ref it resolved. `verb_preflight` writes a new `base-ref:` fact
  holding the full ref name `resolve_base` used (`refs/remotes/origin/<default>`), beside the existing
  `base:` sha. `resolve_base` returns the name as well as the sha.
- **S2** — the gate leg stops reading the subject's input. `check-unattended.sh` derives the default
  branch from `refs/remotes/origin/HEAD` ONLY and ignores `GOV_DEFAULT_BRANCH` entirely, so a run that
  steered the driver with that variable is contradicted rather than confirmed.
- **S3** — the gate leg re-resolves the RECORDED ref. It refuses when `base-ref:` is absent, when it
  is not the ref the leg independently derived, when it does not resolve, and when the merge-base of
  that ref with the run's tip is not the recorded `base:`. Each is its own named refusal.
- **S4** — a `--preflight` refusal when the resolved ref is not the one `refs/remotes/origin/HEAD`
  names, unless the operator sets the escape declared in F1. The driver keeps `GOV_DEFAULT_BRANCH` for
  the legitimate testing use; what it loses is the ability to use it silently.
- **S5** — left-shift arms, both directions, in `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/unattended.test.sh`: a run-created branch named by `GOV_DEFAULT_BRANCH` at HEAD
  still reds the leg; a `refs/remotes/origin/<name>` written by `git update-ref` with no push still
  reds; an unsteered repo still passes. The positive control is mandatory — an arm that reds on
  everything proves nothing.
- **S6** — `memory/guides/UNATTENDED-PROTOCOL.md` §1 gains one sentence stating that the BASE's ref
  is recorded and independently re-derived, and `PROTOCOL.template.md` in lockstep. The protocol
  already promises the two provenance properties; this names the mechanism that makes the second one
  true.

## 3. Non-goals (OUT)

No verification against the actual remote. A run that overwrites `refs/remotes/origin/main` itself
still steers both driver and leg, and only `git ls-remote` closes that. It needs network in a gate
leg, which is a different risk. See F2 — this unit narrows the hole from two mechanisms to one and
says so rather than claiming closure.

No change to `check_mandate`'s byte comparison, which is correct once its BASE is trustworthy.

No removal of `GOV_DEFAULT_BRANCH` from the driver. Other gates read it as a legitimate pin and an
operator on a non-`main` default needs it; the defect is that the GATE read it too.

Not the terminal-phase gap, not `--close --landed`, not the override arity. Those are real and
separately filed.

## 4. Design

### Data model

The run-state file's authored region gains a sixth fact, `base-ref:`. It is a runtime observation
with no re-derivable source at read time — which is the protocol's own test for belonging in the
authored half — because the whole point is that the leg re-derives it INDEPENDENTLY and compares.
Recording a fact so that a second party can contradict it is not the restatement the protocol bans;
it is the evidence pattern `trusted_base` already uses for `base:` itself.

### Migration

A run-state file written before this unit carries no `base-ref:`. The leg refuses rather than skips.
There is exactly one run-state file in the tree today (none), so the migration set is empty and the
refusal is free.

### The asymmetry that makes this work

The driver may be steered; the leg may not. The driver runs inside the session the kit distrusts and
needs an operator escape. The leg runs on the merge bar and answers to nobody in the session. Giving
them the SAME input was the defect: `check-unattended.sh` recomputing the identical wrong value is
what turned a single point of failure into a confirmed one. `TOOL-aUnmannedHelm-6` already recorded
the general form — a gate that verifies the paperwork of a claim without verifying the claim is a
second signature, not defence in depth.

### Files touched (estimate)

Six. `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`, both self-tests,
`tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`.

### Alternatives rejected

Dropping `GOV_DEFAULT_BRANCH` from the driver too: it breaks the operator escape and the testing pin,
and the leg ignoring it is sufficient — a steered driver now fails on the bar.

Recording the ref's SHA instead of its name: the sha is what the run controls. The name is what the
leg can independently derive, which is the only reason to record anything.

## 5. Production-readiness checklist

- security — this IS the security item. It closes an authorization bypass reproduced end to end.
- perf / scale — N/A. Two extra `git rev-parse` calls per gate run.
- a11y · i18n — N/A.
- error / empty / loading states — four named refusals in S3, each armed in both directions.
- observability — the leg names the ref it derived and the ref that was recorded when they differ.
- risks — a false deny on a legitimately non-`origin` default branch. F1 is the declared escape.
- testing + left-shift gates — S5. Both self-tests are already on the bar, so the arms ride existing
  legs and no new leg is added.
- migration / rollback — the empty migration set above; rollback is reverting six files.
- user docs — S6, one sentence in the protocol.

## 6. Acceptance criteria

- **AC1** — When a run sets `GOV_DEFAULT_BRANCH` to a branch it created at HEAD and runs
  `--preflight`, the driver refuses, naming the ref it was steered toward and the ref
  `refs/remotes/origin/HEAD` actually names.
- **AC2** — When a run writes `refs/remotes/origin/<name>` with `git update-ref` (no push, no
  network), points `GOV_DEFAULT_BRANCH` at it, and gets a run-state file past preflight by any means,
  `bash tools/unattended/check-unattended.sh` REDS naming the disagreement.
- **AC3** — When the run-state file carries no `base-ref:`, the leg reds with its own named refusal
  rather than skipping the check.
- **AC4** — When `base-ref:` names a ref that no longer resolves, the leg reds naming it.
- **AC5** — When the recorded `base:` is not the merge-base of the recorded `base-ref:` and the run's
  tip, the leg reds.
- **AC6** — When an UNSTEERED repo with a normal `origin/HEAD` runs the full sequence, preflight and
  the leg both pass. This is the positive control and it is not optional.
- **AC7** — When `bash tools/unattended/check-unattended.test.sh` and
  `bash tools/unattended/unattended.test.sh` run, both pass and their assertion counts have grown.
- **AC8** — When `python tools/memory-tree/check-arms.py` runs, the new fail branches are armed and
  `ARMS_FLOORS` for both files has been raised to match.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.test.sh` ·
`python tools/memory-tree/check-arms.py` · `tools/memory-tree/check-memory-hygiene.sh` ·
`bash tools/run-gates.sh` at the push boundary. No new leg.

## 8. Open questions

### F1 — the escape when the default branch is legitimately not what `origin/HEAD` names

S4 refuses a steered driver. A repo whose `origin/HEAD` is stale or unset has a legitimate need for
`GOV_DEFAULT_BRANCH`. Options: refuse always and require the operator to fix `origin/HEAD`; or accept
the variable when it is set AND `origin/HEAD` is unresolvable, refusing only when the two disagree.
**Recommendation: the second.** It is the most feature-rich option that satisfies every stated
constraint — it keeps the operator escape, and a disagreement is the only shape the attack takes,
since a run that could set `origin/HEAD` could equally set the ref it points to.

### F2 — verifying against the actual remote

`git ls-remote origin <branch>` returns the real remote sha without mutating anything, and would close
the remaining hole where a run overwrites `refs/remotes/origin/main` directly. It needs network in a
gate leg. Options: add it as a hard check; add it as a soft check that skips loudly offline; leave it
out. **Recommendation: leave it out of this unit and file it.** A gate leg that needs network is a
gate leg that reds on a plane, and the DEAD PROBE discipline says a probe that cannot run must say so
rather than pass — which turns every offline run red. It deserves its own unit with that decided.

### F3 — the `refs/remotes/$d` fallback

`resolve_base` walks `refs/remotes/origin/$d` then `refs/remotes/$d`. The second is for a repo whose
remote is not named `origin`, and it widens what the run can write. **Recommendation: keep it, and
record it** — S1 records whichever ref was used and S3 compares it against the leg's independent
derivation, so the fallback is covered by the same mechanism rather than needing removal.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. Implements fixes 3 and 4 of `D3` from
  `../../aUnmannedHelm/reviews/2026-08-10-review-aUnmannedHelm-2.md`, which specified four and landed
  two. The hole the unapplied two leave was reproduced end to end during unit 1 and recorded in this
  build's README.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve a trustworthy base commit the run cannot move, and
escape values before substitution"` returned `resolve` (`tools/memory-recall/recall_conf.py`, fan-in
15) and `resolve_root` (`tools/codebase-map/map_lib.py`) as the repo's resolver seams, plus the
gotcha class `assertion-between-two-derived-values.md`. Neither resolver seam fits: both resolve a
PATH from configuration, while this unit resolves a REF under an adversarial assumption about who
supplies the input. The gotcha class does fit and is the reason S2 exists — an assertion between two
values derived from the same steered input is not an assertion.

`python tools/memory-recall/query.py "what did the review decide about anchoring the mandate base on a
ref the run cannot move" --terms "mandate base anchor remote-tracking ref update-ref default branch
env var provenance merge-base forge authorization gate leg"` returned the binding prior art directly:
`D3` at `../../aUnmannedHelm/reviews/2026-08-10-review-aUnmannedHelm-2.md:173` with its four numbered
fixes, and two decision rows — `TOOL-aUnmannedHelm-5` ("every input to the mandate comparison must lie
OUTSIDE the run's reach") and `TOOL-aUnmannedHelm-6` ("a gate that verifies the PAPERWORK of a claim
without verifying the claim is a second signature, not defence in depth"). This unit is the second of
those two decisions applied to the first. The seam extended is `resolve_base` and `trusted_base` in
`tools/unattended/unattended.sh`, which already implement the evidence pattern — record the value,
re-derive it, refuse on mismatch — for `base:`; S1 through S3 extend that same pattern one level out
to the ref the base came from.
