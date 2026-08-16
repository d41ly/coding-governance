---
slug: aMooredAnchor
node: a
opened: 2026-08-11
streams: tooling
roster: TOOL
ids: TOOL-aMooredAnchor-1 TOOL-aMooredAnchor-2 TOOL-aMooredAnchor-4
---

# aMooredAnchor — the anchor the run cannot move

Node `a` · opened 2026-08-11 · streams tooling.

`TOOL-aUnmannedHelm-5` established the rule this build finishes: *every input to the mandate
comparison must lie outside the run's reach*. Commit `b94818b` applied it to the driver and to the
shape of the gate's loop. It did not finish the job, and the residue is not a tidy remainder — one of
the four holes reproduced here is a **blocker of the same class as the three that build already
fixed**, reachable with one git command, no environment variable and no network.

This README is the master overview and the owner decision menu, per `memory/TEMPLATE-SPEC.md`.

## Start here

**State.** BUILT and landed as one unit, after being REBASED twice onto work that landed from other
sessions mid-build. The reproduction harness ran before a line of the spec was written, and its
transcript is in `build/`.

**What survived the rebases, and what did not.** `aStandingWrit` S0 solved the anchor half
independently and better — it made the rewritten tracking ref and the env-supplied branch name INERT
rather than detected, and it measured something this build had wrong: `GIT_NO_REPLACE_OBJECTS=1`
does NOT suppress a graft file, only `GIT_GRAFT_FILE` pointing outside the repo does. So this build's
anchor material and its §1a bound paragraph were both WITHDRAWN rather than merged, and what shipped
is the four defects no fork answer reached, each verified still-live on `main` immediately before
re-applying: the marker grammar, the terminal-record lifecycle, the word-split population loop, and
the replace-ref/graft PRESENCE refusal.

**What was reproduced, with controls.** The harness builds the same fixture
`check-unattended.test.sh` builds, then runs two controls and four defeats. Both controls behave:
an honest tree is green, and a forged mandate with an **untouched** anchor reds on check 9. That
second control is what makes the four defeats mean something.

| # | Defeat | Needs | Result |
|---|---|---|---|
| R1 | `git update-ref refs/remotes/origin/main <run's own commit>` | one command | gate **green**, driver `preflight OK` |
| R2 | `GOV_DEFAULT_BRANCH` naming a remote-tracking ref the run created | one command + one env var | gate **green** |
| R3 | `GOV_DEFAULT_BRANCH=nosuchref` with a 40-zero recorded base | one env var | check 9 **silent**, exit 0 |
| R4 | a clone with no `origin/HEAD`, 40-zero recorded base | **no attacker at all** | check 9 **silent**, exit 0 |

**The finding this build was opened against under-states the problem.** Its fix list treats
`GOV_DEFAULT_BRANCH` as the tainted input and `refs/remotes/origin/<default>` as the trustworthy
anchor. R1 shows the second half is false. `refs/remotes/*` is an ordinary local ref namespace and
`git update-ref` writes it without a push, without a network and without touching `origin/HEAD` —
which still answers `origin/main` throughout the attack. The kit's own comment at
`tools/unattended/unattended.sh:113` asserts the opposite in as many words: *moving it requires a
push, which is the act being authorized, so using it is not circular.* That sentence is the defect.
Applying only the four listed fixes would close R2, R3 and R4 and leave R1 open, with every gate
green and a comment in the source explaining why the remaining hole cannot exist.

**Consequence for scope.** This build cannot be a patch to a loop. It has to answer a question the
kit has not yet asked: *what is the trust root?* That is unit 1's central fork, and it is the one
thing here the owner should decide rather than the builder.

## The unit

| Unit | Subject | Obligation |
|---|---|---|
| **Unit 1** | `TOOL-aMooredAnchor-1` — marker grammar, the landing lifecycle, and two silent skips | close the four reproduced defeats that no trust-root answer reaches, on whatever base main is at when it lands. **Met**, after two rebases |

## Owner decision menu — RESOLVED

**F1 — the trust root · resolved to D, and the menu it was picked from was wrong.** The owner picked
"the builder's recommendation" while that recommendation was **A** (fetch the anchor from the
remote). A is withdrawn: `git config remote.origin.url <the run's own bare repo>` — or
`url.<evil>.insteadOf`, which leaves `remote.origin.url` *reading* honest — makes the "server-blessed"
anchor the run's own forged commit. `.git/config` is untracked and appears in no commit, so there is
no value at BASE to compare it against. Reproduced here twice and by the review three times, once
driving the real pre-push hook with no `--no-verify`. **C** was also mispriced: it was described as
the only purely-local unforgeable root, and three repo-local `git config` lines make
`git verify-commit` exit 0 on a run-signed commit.

So the recommendation changed to **D — concede the bound and write it as a checkable sentence** —
and the review's structural finding is what makes that cost nothing: *none of the work that closes a
reproduced defeat depends on which trust root is chosen.* The bound now lives in
the driver's own source, replacing the sentence that asserted the opposite. The protocol statement
was withdrawn in favour of `aStandingWrit`'s §9, which says it better — a rule in two carriers is a
defect in the second. Closing the anchor at all is `aStandingWrit`'s ground now, not this build's.

**F2 — one resolver or two · resolved to neither.** With A withdrawn there is no fetch to share, so
no `anchor.sh` is added. The rev-1 cost note was wrong in both directions: `check-arms.py` discovers
a file only when it *defines* `fail() {`, so a `fail()`-free resolver needs no floor at all, while a
`fail()`-defining one plus its charter-required sibling would have moved `gate-legs.json`, the
dossier's gate-legs row, a fresh map render and a charter bullet — all of which §7 denied.

**F3 — `base-ref:` · deferred with F1.** Under every fork answer the local ref name carries no
information `base:` does not, so its disagreement branch would compare a constant with itself.

## Review record

`reviews/2026-08-11-review-aMooredAnchor-1.md` — Tier-2 over the rev-1 spec. Five lenses, 38 raw, 32
confirmed, 6 refuted, precision 0.84, no dead lens. 17 distinct defects: 4 blockers, 6 highs, 4
mediums, 3 lows. Verdict: **fold and rebuild the spec**, which rev-2 is.

The three claims that changed a decision were re-reproduced independently before being acted on,
rather than taken on the reviewers' word. All three held. A fourth — `refs/replace/*` — needed a
second attempt: the first replacement commit had different parents, so ancestry moved and the gate
red for an unrelated reason. Rebuilt with `git commit-tree` preserving parents, it reproduced exactly
as reported, and that same parent-preservation is now a comment in the arm so the next person does
not repeat it.

The table below is GENERATED from the status
header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node a · opened 2026-08-11 · streams tooling · ids TOOL-aMooredAnchor-1 TOOL-aMooredAnchor-2 TOOL-aMooredAnchor-4

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aMooredAnchor-1 — marker grammar, the lifecycle the kit never had, and two silent skips](spec/2026-08-11-spec-aMooredAnchor-1.md) | CLOSED | rev-5 | 2026-08-11 |

Records live under `spec/`, `build/` and `reviews/`.
<!-- /gen:build-index -->
