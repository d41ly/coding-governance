---
slug: cFinalBerth
node: c
opened: 2026-08-13
streams: tooling
roster: TOOL
ids: TOOL-cFinalBerth-1 TOOL-cFinalBerth-2 TOOL-cFinalBerth-3 TOOL-cFinalBerth-4 TOOL-cFinalBerth-5
---

# cFinalBerth — the run that can finish

Node `c` · opened 2026-08-13 · streams tooling.

The unattended kit had ten phases and no way to reach the last two. `--phase` refused a terminal
phase, saying it was `--close`'s to write; `--close` wrote `LANDING`. Nothing in the driver wrote
`LANDED` or `ABORTED`. A run therefore could not finish, and a record that cannot finish is counted
as live forever by the driver's own single-live precondition and by leg check 7.

This README is the master overview and the owner decision menu, per `memory/TEMPLATE-SPEC.md`.

## Start here

**How the hole opened, verified rather than inferred.** Two builds landed half a fix each, days
apart, and neither saw the other.

The review record `reviews/2026-08-11-review-TOOL-aStandingWrit-1-2.md` finding F2 established that
`--phase` could reach `LANDED` from any phase, skipping the entire Definition of Done — including
the two items enforced nowhere else, the keepalive reap and the parked-decision surfacing. Its
recommended fix opens with the words *a precondition, not a blanket rejection*, and then supplies a
code snippet that is a blanket rejection whose message names `--close` as the producer. **The
snippet shipped; the precondition did not.** The message it carries is false today.

The review record `reviews/2026-08-11-review-TOOL-aMooredAnchor-1-1.md` finding D5, a BLOCKER, reached the
same lifecycle from the gate side: a landed record red the bar forever because check 9 compared the
recorded base for equality. That spec's S3 changed check 9's question to ancestry, and its AC4 reads
*when a run-state record is LANDED and the merge-base has moved past the recorded base, the gate is
green*. It made a `LANDED` record harmless without ever asking how one comes to exist.

So one build made the terminal state safe and the other removed its only producer. Each is correct
in isolation. The seam between them is the defect, and it is precisely the class the open row
`TOOL-aStandingWrit-8` names: the kit has driver arms, leg arms and parity arms, and no arm that
runs the driver and then the leg over one tree.

**What was observable in this repo when the build opened.** The record at
`memory/builds/aSealedCaravan/RUN.md` sat at phase `BUILDING`. That run landed — `main` carried its
work at `7a4f904` with the full bar green — and it could not be closed. It was the only run-state
file in the tree, so leg check 7 counted one live run and stayed green by exactly one: the next
unattended run would have made it two and red the bar. It now reads `LANDED`, repaired by unit 2's
S7, and the tree carries no non-terminal run.

**Why the second unit is here and not in a follow-up.** Not because it is the only way to unwedge
`aSealedCaravan` — the spec audit refuted that reason, and unit 2's own S7 repairs that record
directly and independently of everything else in the build. The surviving reason is narrower and
better: the kit cannot close ANY run whose HEAD is already published, which is the state every
successful landing ends in, and the sentence it refuses with sits on the authorization path and is
false about that state. Shipping a terminal producer on top of a close that cannot run after a
landing would have left the lifecycle broken one step from the end.

The record repair and the driver change are therefore separate obligations inside unit 2, and the
spec keeps them separable.

## The units

| Unit | Subject | Obligation |
|---|---|---|
| **Unit 1** | `TOOL-cFinalBerth-1` — the terminal transition | a run reaches `LANDED` by an observation of the remote and `ABORTED` by a recorded refusal, and the gate arms both |
| **Unit 2** | `TOOL-cFinalBerth-2` — `--close` after the landing it precedes | the degenerate-base refusal stays at `--close` and changes its question to the recorded base, so a landed run can be closed and a run that built nothing still cannot |

## Owner decision menu

**F1 — how a run reaches `LANDED` · RESOLVED (owner, 2026-08-13): a verified `--landed` verb.** The
alternative was to relax `--phase` to accept `LANDED` from `LANDING`, which is roughly eight lines
and closes F2's hole just as well, but leaves the terminal claim an agent assertion. The owner chose
the observation: `--landed` re-observes the remote and refuses unless HEAD is an ancestor of the tip
the remote advertises for its own HEAD. The cost accepted with it is a network round-trip on the
verb and a records commit afterwards that has to be pushed.

**F2 — scope · RESOLVED (owner, 2026-08-13): fold in the post-landing close.** Two mechanisms, so
two specs under one build, per the build method's one-mechanism-per-spec rule. This answer is about
SCOPE and nothing else — rev-1 of unit 2 cited it as if it also resolved F3 below, which the spec
audit correctly called a blocker.

**F3 — may the merge-base-equals-HEAD refusal at `--close` be deleted? · RESOLVED (owner,
2026-08-13): narrow it rather than delete it.** The guard was scoped by verb as the `aStandingWrit`
spec's S3, ratified as that spec's fork F2 (owner, 2026-08-11, "keep equality"), and pinned by a
paired arm. The builder's recommendation was to delete it, on the grounds that the anchor has since
become an observation of the remote and that the hazard is now reproduced with a control. The owner
chose to keep a refusal at `--close` and change its question to the recorded base, which is the
discriminator that can separate a run that built nothing from a run whose work is landed. The cost
was named before the answer: it makes a run-written value an input on the authorization path, a class
this kit has a recorded scar in. Unit 2's section 4 accounts for what bounds it.

## Review record

`reviews/2026-08-13-review-TOOL-cFinalBerth-1-1.md` — M4 spec audit over both rev-1 specs and this README.
Four lenses, 34 raw, 23 confirmed, 11 refuted, precision 0.68, no dead lens; 16 distinct confirmed
findings — 2 blockers, 8 highs, 4 mediums, 2 lows. Verdict: **BLOCKED**, and rev-2 of both specs is
the fold.

Both blockers were re-verified against source before being acted on rather than taken on the
reviewers' word, and both held. Unit 1's blocker was fatal to its central mechanism: rev-1 rested
`--landed`'s integrity on the claim that `--close` is the only writer of `LANDING`, and `LANDING` is
an ordinary non-terminal member of the vocabulary, so one `--phase` call reopened the hole the unit
exists to close. Unit 2's blocker was a decision signed in the owner's name that the owner had never
been asked; it is F3 above, now asked and answered.

*(The synthesis pass's own summary says "three lenses". It was four — the per-agent journal records
12, 10, 7 and 5 findings. Corrected here rather than in the record, which is left as written.)*

The table below is GENERATED from the status header of
every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node c · opened 2026-08-13 · streams tooling
ids TOOL-cFinalBerth-1 TOOL-cFinalBerth-2 TOOL-cFinalBerth-3 TOOL-cFinalBerth-4 TOOL-cFinalBerth-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-cFinalBerth-1 — the terminal transition: LANDED as an observation, ABORTED as a record](spec/2026-08-13-spec-cFinalBerth-1.md) | — | 2 | CLOSED | rev-4 | 2026-08-14 |
| [TOOL-cFinalBerth-2 — the close that survives the landing it precedes](spec/2026-08-13-spec-cFinalBerth-2.md) | — | 2 | CLOSED | rev-4 | 2026-08-14 |
<!-- /gen:build-units -->

Records live under `spec/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-13-review-TOOL-cFinalBerth-1-1.md](reviews/2026-08-13-review-TOOL-cFinalBerth-1-1.md) | spec-audit | TOOL-cFinalBerth-1 TOOL-cFinalBerth-2 |
| [2026-08-13-review-TOOL-cFinalBerth-1-2.md](reviews/2026-08-13-review-TOOL-cFinalBerth-1-2.md) | diff-review | TOOL-cFinalBerth-1 TOOL-cFinalBerth-2 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-13-spec-cFinalBerth-1.md](spec/2026-08-13-spec-cFinalBerth-1.md)
  - [2026-08-13-spec-cFinalBerth-2.md](spec/2026-08-13-spec-cFinalBerth-2.md)
- **`reviews/`**
  - [2026-08-13-review-TOOL-cFinalBerth-1-1.md](reviews/2026-08-13-review-TOOL-cFinalBerth-1-1.md)
  - [2026-08-13-review-TOOL-cFinalBerth-1-2.md](reviews/2026-08-13-review-TOOL-cFinalBerth-1-2.md)
<!-- /gen:build-docs -->
