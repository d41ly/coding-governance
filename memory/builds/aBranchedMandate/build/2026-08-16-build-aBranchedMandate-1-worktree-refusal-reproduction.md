# aBranchedMandate — why an unattended run refuses in a worktree

**Serves:** none — a reproduction of the commissioning complaint; it PRECEDES the spec set and is what warranted it
**Commissions:** TOOL-aBranchedMandate-1..4

Node `a` · 2026-08-16 · reproduced against BASE `96141aed`.

The commissioning report was one sentence: an unattended build cannot be started from a worktree
unless the build and its specs are landed on the default branch. This record is the reproduction. It
exists because the report names one cause and there are **three**, they fire in a fixed order, and
fixing only the named one leaves every worktree run still refused.

Everything below was executed. No claim here is inferred from reading source alone.

## The three causes, in the order they fire

| # | Where | Fires when | Named by the report? |
|---|---|---|---|
| C1 | `tools/check-wiring.sh` eol arm → driver check 4 | a worktree carries CRLF on the pinned `.claude/` renders | no |
| C2 | `tools/memory-recall/adopt-memory-recall.sh --check`, a merge-bar leg | the same condition | no |
| C3 | `check_authorization` in `tools/unattended/unattended.sh` → driver check 6 | the build README is not on the default branch | yes |

**The "fires when" column for C1 and C2 was wrong in the first revision of this record and is
corrected here.** It read "any fresh worktree on this fleet", attributing the CRLF to `git worktree
add`. That is false, and the correction is in the measured section below. The refusals themselves were
observed exactly as written; only their cause was misattributed.

C1 refuses `--preflight` before C3 is ever evaluated. C2 does not block the start; it blocks
`--close`, because the `gates-green` Definition-of-Done item runs the declared `GATE_CMD`. So a run
that got past C1 and C3 would still be unable to finish.

## The CRLF writer — measured, and NOT what the first revision claimed

The first revision of this record said `git worktree add` lands CRLF on `eol=lf`-pinned paths, citing
`tools/check-wiring.sh:194`. That source line says a worktree checkout **can** land CRLF; this record
upgraded "can" to "always" and did not test it. The spec audit challenged the claim and it does not
hold. Re-measured on node `a` at BASE `96141aed`:

| Tree | How it was created | CR bytes in `.claude/skills/memory-recall/SKILL.md` |
|---|---|---|
| primary checkout | ordinary clone | 0 |
| a scratch worktree | `git worktree add --detach <tmp> 96141aed` | 0 |
| all five live worktrees | the agent harness's worktree creation | 89 each |

In the scratch worktree `bash tools/check-wiring.sh --check` printed
`ok       eol       — every eol=lf-pinned .claude/ file is LF in the worktree` and exited 0, and
`bash tools/memory-recall/adopt-memory-recall.sh --check` exited 0 **despite still carrying no CR
normalisation**. So `git worktree add` is not the writer.

The writer is scoped, which is the useful part. In a live worktree the CRLF is confined to `.claude/`
— the three pinned Skill renders and `.claude/settings.json`. Every other `eol=lf`-pinned path
measured LF in the same tree: `tools/run-gates.sh`, `tools/gate-legs.json`, `.memory-tree.conf`,
`.unattended.conf`, `skills/session-kickoff/SKILL.md`, `memory/HYGIENE.md`. Two candidate writers were
tested and both cleared: the adopters' own `--scaffold` render wrote LF, and the pins all predate
every live worktree by days, so a pre-pin checkout is not the explanation either.

**The writer is therefore the agent harness's worktree creation, and it is UNVERIFIED beyond that
scope.** No process was caught in the act. What is established is the population it touches
(`.claude/`), that it is systematic across all five live worktrees, and that it is not git. The
consequence for the fix stands and is if anything sharper: `tools/check-wiring.sh`'s eol population is
derived from tracked `.claude/` paths carrying the pin, which is exactly the writer's scope.

What this does NOT change: the committed bytes are correct on every node, so a CRLF working copy is
still a working-copy condition rather than a repository defect. What it DOES change: the reason. The
first revision derived that from "the index normalises on commit, so CRLF can only come from the
checkout filter", and the checkout filter is not where this came from.

## C1 — the wiring check reds on that CRLF, and the driver may not repair it

With the pinned `.claude/` renders carrying CRLF, the eol arm reports UNWIRED and `--check` exits
non-zero.

Observed in this worktree, unmodified:

```
$ bash tools/check-wiring.sh --check ; echo $?
UNWIRED  eol       — .claude/skills/drift-audit/SKILL.md holds CRLF despite its eol=lf pin; ...
UNWIRED  eol       — .claude/skills/memory-recall/SKILL.md holds CRLF despite its eol=lf pin; ...
UNWIRED  eol       — .claude/skills/unattended/SKILL.md holds CRLF despite its eol=lf pin; ...
1
```

`.unattended.conf` declares `WIRING_CHECK="bash tools/check-wiring.sh --check"`, and
`memory/guides/UNATTENDED-PROTOCOL.md` section 7 forbids the driver from delegating to the repairing
mode. So the driver refuses and cannot self-heal, on a build that is fully landed:

```
$ bash tools/unattended/unattended.sh --preflight aBatchedLintel --keepalive-id probe
UNATTENDED check 4 FAILED — the declared wiring check failed, and a dormant hook makes every
later green meaningless: bash tools/check-wiring.sh --check
unattended: --preflight refused; the run-state file is unchanged
```

`aBatchedLintel` is on the default branch and predates this branch, so C3 is not in play here. This
is the refusal the report attributes to the authorization rule, and it is not the authorization rule.

## C2 — one of three adopters byte-compares without normalising CR

`memory/gotchas/gate-green-by-accident-on-generated-bytes.md` states the rule: a generated file needs
**both** an `eol=lf` pin and a normalising comparison, and either alone leaves the failure mode. Two
of the three pinned Skill renders have both halves. One has only the pin:

```
$ for k in unattended memory-recall drift-audit; do
    printf '%-14s ' "$k"; bash tools/$k/adopt-$k.sh --check >/dev/null 2>&1 \
      && echo "exit=0" || echo "exit=$?"; done
unattended     exit=0
memory-recall  exit=1
drift-audit    exit=0
```

The failure is the whole-file diff the gotcha describes — every line reported as changed on a file
nobody edited:

```
$ bash tools/memory-recall/adopt-memory-recall.sh --check
memory-recall: .claude/skills/memory-recall/SKILL.md has DRIFTED from .memory-tree.conf.
@@ -1,89 +1,89 @@
----
-name: memory-recall
...
```

`memory-recall skill wiring` is a leg in `tools/gate-legs.json` and carries **no `guard`**, so it
runs on every invocation of the bar including a records-only diff. In a worktree carrying the CRLF the
merge bar is therefore red before any work is done, which makes `gates-green` unmeetable and `--close`
blocked. Measured: `bash tools/run-gates.sh` here reported `gates RED — 1/58 legs failed`, and that
one leg is this one; the same bar in the primary checkout is green.

The defect in the adopter is REAL and independent of what writes the CRLF. It is the only one of the
three pinned Skill adopters lacking the normalising half its own gotcha record requires, so it reds
whenever the condition appears — as it does in all five live worktrees today — while its two siblings
tolerate it. What the corrected measurement changes is that the scratch worktree does not exercise it,
so a fixture has to CONSTRUCT the CRLF rather than expect a checkout to supply it.

This is a defect in one adopter, not in the unattended kit. It reaches the unattended kit because the
kit declares that adopter's bar as its Definition of Done.

## C3 — the authorization anchor, which is the cause the report names

`check_authorization` resolves the build README at the pinned BASE, and BASE is the merge-base
against the tip the remote advertises for its own HEAD. A build committed on the run's own branch is
not at that merge-base.

Reproduced in a scratch clone with a real bare origin advertising a HEAD symref, so the anchor
observation succeeds and only the authorization comparison fails. The script is
`build/2026-08-16-build-TOOL-aBranchedMandate-3-repro-c3.sh` beside this record. Its flow: seed and push a default branch, branch to `unit`,
write and commit a conforming build folder there, then preflight.

```
--- HEAD=c7fab8a  BASE(merge-base)=0761b21 ---
UNATTENDED check 6 FAILED — no build README at the pinned BASE, so nothing committed before this
run branched authorizes it, and a build folder the run created on its own branch authorizes
nothing: 0761b21...:memory/builds/aTestBuild/README.md
unattended: --preflight refused; the run-state file is unchanged
```

**C3 is not a bug.** `memory/guides/UNATTENDED-PROTOCOL.md` section 1 states it as ratified design:
"A build folder introduced by a commit on the run's own branch grants nothing." The four costs of the
current design were enumerated and accepted by the owner. Changing it changes a property the owner
ratified, which is why the unit that changes it is Tier 2 and carries the trade as a stated fork
rather than as an implementation detail.

Two further facts about C3 worth having before designing a fix:

- The predicate reads **only** `README.md`. Specs are not consulted. The report's phrase "and its
  specs" describes the situation but not the mechanism — landing the specs would change nothing.
- It is **not worktree-specific**. Any branch reproduces it. The worktree is where this repo puts
  branches, so it is where the symptom is seen.

## What C3's residual looks like after any fix

`memory/guides/UNATTENDED-PROTOCOL.md` section 9 already concludes that nothing running under the
run's own uid constitutes authorization, and that what actually binds lives on the remote. Any fix
here therefore moves the anchor rather than closing the class, and the honest measure of a fix is
which deliberate act it makes necessary and whether that act is recorded.

`TOOL-aStandingWrit-6` is a tracked OPEN row stating that the gate leg still recomputes BASE from
`GOV_DEFAULT_BRANCH` and a remote-tracking ref rather than from an observation. Any anchor change
lands on top of that gap and does not repair it.
