# TOOL-aWrittenMethod-2 — the mandate BASE the run cannot steer

**Status:** CLOSED · rev-5 · 2026-08-11 · node a · Tier-2 · base 7f614a17 · streams tooling · review wf_eb978bb2-f98

## 1. Goal

> **SUPERSEDED at the merge, and this spec is kept as the reasoning rather than the design.** Another
> node landed a remote-OBSERVED anchor while this unit was in flight — the run-state file records
> `anchor-ref`, `anchor-sha` and `anchor-url`, and `resolve_base` merge-bases against a sha the remote
> answered for. That is unit 2's own F2, which this spec filed as out of scope, and it is strictly
> stronger: it does not depend on `refs/remotes/origin/HEAD`, a ref the run rewrites locally. The
> mechanism described below — `RESOLVED_REF`, `canonical_ref`, the `base-ref` fact — no longer exists
> in `tools/unattended/unattended.sh`; `grep` returns zero.
>
> What SURVIVES is the principle, and it survived because the other node reached it independently:
> **the gate must not read the input the driver read**, or it confirms a steer instead of
> contradicting it. What did NOT survive is this unit's terminal-phase exemption, and the reason is
> worth keeping: the run writes `phase:`, so keying an exemption on it is a one-line escape from the
> check. The other implementation's comment says exactly that, and says it as a rejected option. This
> spec shipped it, and its own closing review reproduced the bypass one commit later.


The mandate comparison is the only thing standing between an unattended run and an unreviewed push,
and its BASE is currently chosen by the run. **NARROW** the hole from two mechanisms to one, and make
the gate leg an independent second opinion rather than a second computation of the same steered value.

This unit does NOT close the bypass, and saying so is part of the deliverable.
`refs/remotes/origin/HEAD` is an ordinary symref the run rewrites or deletes locally. Reproduced:
`git symbolic-ref -d refs/remotes/origin/HEAD` exits 0 with no push and no network. What this unit
removes is the ability to steer the BASE with an environment variable while every gate stays green.

## 2. Scope (IN)


**Landing order.** This unit is step one of five. The set lands `2 → 6 → 3 → 4 → 5`, fixed by the
audit `wf_eb978bb2-f98`: unit 6 rewrites the renderer unit 3 measures against, unit 3 creates a new
method carrier unit 4 must then enumerate, and unit 5 puts the method under a manifest ratchet that
would otherwise tax every earlier unit's commit. These are NOT parallel-safe under M6.

- **S1** — the driver records the ref it resolved. `verb_preflight` writes a new `base-ref:` fact
  holding the full ref name `resolve_base` used (`refs/remotes/origin/<default>`), beside the existing
  `base:` sha. `resolve_base` returns the name as well as the sha.
- **S2** — the gate leg stops reading the subject's input. `check-unattended.sh` derives the default
  branch from `refs/remotes/origin/HEAD` ONLY and ignores `GOV_DEFAULT_BRANCH` entirely, so a run that
  steered the driver with that variable is contradicted rather than confirmed.
- **S3** — the gate leg re-resolves the RECORDED ref, deriving exactly ONE ref name,
  `refs/remotes/origin/<default>`. **Five** named refusals: `base-ref:` absent; it disagrees with the
  ref the leg derived; it does not resolve; the merge-base of that ref with the run's tip is not the
  recorded `base:`; and — the one rev-1 missed — **the leg cannot itself derive a default branch**.
  That last is a RED naming `refs/remotes/origin/HEAD` as the thing to set, never a skip. Reproduced:
  after `git symbolic-ref -d refs/remotes/origin/HEAD`, the leg sets its default-branch variable empty
  and its `if` guard skips the entire merge-base body with no else, so a forged mandate at a
  run-authored BASE passes at exit 0. This is the absence-is-the-exemption shape the leg's own comment
  already condemns for `base:`, reintroduced one level up, and it is what D3 fix 4 named.
- **S4** — the refusal lives in `trusted_base`, NOT in `verb_preflight`, so every verb touching the
  BASE inherits it and the driver refuses when the resolved ref is not the one
  `refs/remotes/origin/HEAD` names. `trusted_base` also validates the recorded `base-ref:` the way it
  already validates `base:` — recorded value as EVIDENCE, re-derived independently, refuse on
  mismatch. Scoping this to preflight would have missed `--close`, which is on the attack path.
- **S5** — left-shift arms, both directions, in `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/unattended.test.sh`. **Both fixtures must first gain a `refs/remotes/origin/HEAD`**
  (`git remote set-head origin main`, local, no network) and `check-unattended.test.sh` must DROP its
  `export GOV_DEFAULT_BRANCH=main`. Measured: neither fixture has that symref today — they build the
  anchor by pushing to a bare remote, which creates `refs/remotes/origin/main` and no HEAD — so after
  S2 the leg's derivation would be EMPTY inside the very tests meant to arm it, and AC6's positive
  control would pass because the check was OFF. Arms: a run-created branch named by
  `GOV_DEFAULT_BRANCH` at HEAD still reds; a `refs/remotes/origin/<name>` written by `git update-ref`
  still reds; a DELETED `origin/HEAD` reds; an unsteered repo passes.
- **S6** — the protocol pair, THREE edits each, not one. §2 says the authored region carries
  "exactly five facts and nothing else" and that "nothing in the tree derives any of them" is the test
  for belonging: `base-ref:` is the sixth, so the count becomes six, it is added as item 6, and the
  membership sentence is rewritten to admit a fact recorded SO THAT a second party can contradict it.
  §1 gains the sentence naming the mechanism. Both `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md` change in lockstep — the leg byte-compares them.

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
There are ZERO run-state files at BASE (`git ls-files 'memory/builds/*/RUN.md'` returns nothing), so
the migration set is empty and the refusal costs nothing. The corollary is uncomfortable and belongs
here: the dogfood bar exercises none of this on real data, so the S5 fixtures are the ONLY place S3
ever runs, which is why their repair is a scope item rather than a test detail.

### The asymmetry that makes this work

The driver may be steered; the leg may not. The driver runs inside the session the kit distrusts and
needs an operator escape. The leg runs on the merge bar and answers to nobody in the session. Giving
them the SAME input was the defect: `check-unattended.sh` recomputing the identical wrong value is
what turned a single point of failure into a confirmed one. `TOOL-aUnmannedHelm-6` already recorded
the general form — a gate that verifies the paperwork of a claim without verifying the claim is a
second signature, not defence in depth.

### Files touched (estimate)

Eight. `tools/unattended/unattended.sh`, `tools/unattended/check-unattended.sh`, both self-tests,
`tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, `.memory-tree.conf`
(the `ARMS_FLOORS` raise) and `.claude/SESSION-KICKOFF.md` (the re-stamp both watched paths oblige).

### Alternatives rejected

Dropping `GOV_DEFAULT_BRANCH` from the driver too: it breaks the operator escape and the testing pin,
and the leg ignoring it is sufficient — a steered driver now fails on the bar.

Recording the ref's SHA instead of its name: the sha is what the run controls. The name is what the
leg can independently derive, which is the only reason to record anything.

## 5. Production-readiness checklist

- security — this IS the security item. It NARROWS an authorization bypass reproduced end to end,
  from two mechanisms to one. The residual is `refs/remotes/origin/HEAD` itself, which the run can
  rewrite or delete locally; F2 files the only thing that closes it.
- perf / scale — N/A. Two extra `git rev-parse` calls per gate run.
- a11y · i18n — N/A.
- error / empty / loading states — five named refusals in S3, each armed in both directions.
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
- **AC9** — When the leg runs against a tree whose `refs/remotes/origin/HEAD` has been DELETED, it
  REDS naming that ref, rather than skipping the merge-base body.
- **AC10** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs on this unit's own
  commit, it passes: `.memory-tree.conf` and `.claude/SESSION-KICKOFF.md` are both watched paths, so
  the `ARMS_FLOORS` raise obliges a `last-audit` re-stamp bundled into the same commit.

## 7. Gates

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/adopt-unattended.test.sh` ·
`python tools/memory-tree/check-arms.py` · `tools/memory-tree/check-memory-hygiene.sh` ·
`bash skills/session-kickoff/manifest-check.sh --staged` · `bash tools/run-gates.sh` at the push
boundary. No new leg.

## 8. Open questions

none — every fork below is RESOLVED.

### F1 — the escape when the default branch is legitimately not what `origin/HEAD` names

S4 refuses a steered driver. A repo whose `origin/HEAD` is stale or unset has a legitimate need for
`GOV_DEFAULT_BRANCH`. Options: refuse always and require the operator to fix `origin/HEAD`; or accept
the variable when it is set AND `origin/HEAD` is unresolvable, refusing only when the two disagree.
**RESOLVED (agent, 2026-08-11, delegated): the FIRST — refuse, and require the operator to repair
`origin/HEAD`.** The audit reproduced that the second option is granted by a state the subject
manufactures: deleting `origin/HEAD` costs the run one local command and hands the environment
variable back, which is the exact defect class this unit exists to close. The pre-push hook already
tells an operator to run `git remote set-head origin -a` in this state, so the repair is documented
and one command. An escape the attacker can open is not an escape.

### F2 — verifying against the actual remote

`git ls-remote origin <branch>` returns the real remote sha without mutating anything, and would close
the remaining hole where a run overwrites `refs/remotes/origin/main` directly. It needs network in a
gate leg. Options: add it as a hard check; add it as a soft check that skips loudly offline; leave it
out. **RESOLVED (agent, 2026-08-11, delegated): leave it out of this unit and file it.** A gate leg that needs network is a
gate leg that reds on a plane, and the DEAD PROBE discipline says a probe that cannot run must say so
rather than pass — which turns every offline run red. It deserves its own unit with that decided.

### F3 — the `refs/remotes/$d` fallback

`resolve_base` walks `refs/remotes/origin/$d` then `refs/remotes/$d`. The second is for a repo whose
remote is not named `origin`, and it widens what the run can write. **RESOLVED (agent, 2026-08-11, delegated): REMOVE it**, from both driver and leg. F3 as written
contradicted S3: S3 derives exactly one ref name, so a fallback the leg does not walk is a shape the
comparison cannot express. D3 fix 1 asked for the removal and it is the only reading under which S3
is implementable. A repo whose remote is not `origin` sets `origin/HEAD` or does not use the kit.

## 9. Revision log

- rev-5 · 2026-08-11 · SUPERSEDED at the merge and marked so in section 1. The remote-observed anchor
  another node landed is this unit's own F2, filed here as out of scope; it does not depend on
  refs/remotes/origin/HEAD and is strictly stronger. The mechanism this spec describes is gone from
  the driver. The principle survives; the terminal-phase exemption does not, and why is recorded.
- rev-4 · 2026-08-11 · folded closing review wf_384dfc48-5a9. B1 CONFIRMED and reproduced with a
  control: refs/remotes/origin/<default> is an ordinary local ref, so `git update-ref` steers the
  BASE with no push and both check 9 and check 13 certify a self-authored mandate. The CODE limit
  was already F2; what was wrong was the PROTOCOL, which this unit shipped claiming the BASE is
  "anchored outside the run". Both copies now say NARROWED, name the command that moves the value,
  and name what closing it needs. H2: check 9 reproduced a merge-base for TERMINAL records, so the
  first successful landing would have redded main permanently — terminal records now assert
  reachability instead, armed both directions. An earlier spelling used `continue` and silently took
  the mandate assertion with it; the leg's own self-test caught that. M2: fail 22 computed a third
  argument that fail() discards, so the operator never saw the values.
- rev-3 · 2026-08-11 · BUILT on branch, unmerged. Driver 59 assertions, leg 64, arms clean,
  ARMS_FLOORS raised 31->34 and 33->38. Two defects the arms caught during the build: resolve_base
  ran under $( ) so the global it set never reached the caller, and a default_branch refusal inside
  trusted_base was unreachable because resolve_base already returns on that failure. Both fixed;
  the unreachable branch was deleted rather than left as decoration.
- rev-2 · 2026-08-11 · folded audit `wf_eb978bb2-f98`. Two blockers, both reproduced independently:
  the leg's sole input is NULLABLE (`git symbolic-ref -d refs/remotes/origin/HEAD` exits 0, after
  which the leg skips its whole body), and neither self-test fixture HAS that symref, so the arms
  would have proven nothing. F1 reversed — its escape was manufacturable by the attacker. F3 resolved
  by removal, because it contradicted S3. The refusal moved from `verb_preflight` to `trusted_base`,
  §1 and §5 restated to claim narrowing rather than closure, and S6 grew from one edit to three
  because the protocol's "exactly five facts" bars the sixth.
- rev-1 · 2026-08-11 · initial draft. Implements fixes 3 and 4 of `D3` from
  `../../aUnmannedHelm/reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-2.md`, which specified four and landed
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
`D3` at `../../aUnmannedHelm/reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-2.md:173` with its four numbered
fixes, and two decision rows — `TOOL-aUnmannedHelm-5` ("every input to the mandate comparison must lie
OUTSIDE the run's reach") and `TOOL-aUnmannedHelm-6` ("a gate that verifies the PAPERWORK of a claim
without verifying the claim is a second signature, not defence in depth"). This unit is the second of
those two decisions applied to the first. The seam extended is `resolve_base` and `trusted_base` in
`tools/unattended/unattended.sh`, which already implement the evidence pattern — record the value,
re-derive it, refuse on mismatch — for `base:`; S1 through S3 extend that same pattern one level out
to the ref the base came from.
