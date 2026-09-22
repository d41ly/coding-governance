**Serves:** diff-review TOOL-aGroundedOrientation-1 TOOL-aGroundedOrientation-2 TOOL-aGroundedOrientation-3

# Closing diff review — aGroundedOrientation, round 1

Tier-2 closing diff review over the build's three units, node `a`, 2026-08-27. ROUND 1. Shape: raw 13, confirmed 6, refuted 7, unverified 0, precision 0.46.

Reviewed range: `f5dff6aee0b0a0177fac8ec842532b461eeca71f...HEAD` (HEAD = `0858295c0ed5a29b68ee14df092336e3f08fe5c5`).

## Verdict: BLOCKED

One blocker and one high, both this build's, plus one blocker-severity red the build INHERITED and did not cause. Every confirmed finding is in the same place: the merge bar is RED at the landing tip, on two unguarded legs, and the tip is already `origin/main`. Nothing is wrong with the three units' code — the guard, the locator and the arms all hold, and template/rendered parity is byte-exact. What failed is the LANDING: the reconcile merge `ded17252` was allowed to complete without the post-merge audit the charter's kickoff-manifest merge exception assigns to the merging run, which is the "a conflict-free merge is not a passing merge" class in its purest form.

Six confirmed ids collapse to three distinct defects. Ids 3, 7 and 10 are one defect (`last-body-change` stranded, check 9 red) and are adjudicated ONCE as F1. Ids 6 and 11 are one defect (`last-audit` not re-stamped, check 5 red) and are adjudicated ONCE as F2. Id 9 is F3. The table's counts and the integers this review reports therefore agree with each other, not with the raw id list.

## Findings

| # | Sev | Address | One line | Billed to |
|---|-----|---------|----------|-----------|
| F1 | blocker | `memory/guides/SESSION-KICKOFF.md:8` | The merge tipped check 9's watched-commit count to exactly 10; neither parent was red. | this build |
| F2 | high | `memory/guides/SESSION-KICKOFF.md:5` | `last-audit` re-stamped mid-run, then re-broken by the run's own watched-file edit. | this build |
| F3 | blocker | `memory/project/unarmed-branches.txt:42` | A shrink-only pin row survived the arm that armed its branch; `check-arms` reds. | INHERITED — `aWarmedTether` |

Scope note on F3: it is listed because a closing review cannot certify a landing whose bar is red, and it is labelled INHERITED because it was reproduced red at `f1be0b49` — the origin/main side of the reconcile — and green at BASE. The arm that armed the pinned branch is `9ea8f94c`, which is not reachable from this build's `08040d24`. This review does not otherwise report the merged-in work of `aWarmedTether`, `aBoundedCeiling` or `dTieredTribunal`.

---

### F1 — blocker — `memory/guides/SESSION-KICKOFF.md:8`, `last-body-change`

**The defect.** `last-body-change` is pinned at `2196414866a0e2db52759ebd015aae4a79dd0e8d`. Check 9 of the kickoff-manifest ratchet counts non-merge commits touching the manifest's own `watch:` pathspecs since that sha and refuses at 10 or more. The reconcile merge combined two sub-threshold sides into a red one.

**Reproduced.** `bash skills/session-kickoff/manifest-check.sh` at HEAD exits 1:

```
MANIFEST check 9 FAILED — the manifest body has not changed across ten or more watched
commits ... 10 non-merge commits since 2196414866a0e2db52759ebd015aae4a79dd0e8d
```

**The arithmetic, computed directly** with `git rev-list --count --no-merges 2196414866..<tip> -- <the ten watch pathspecs>`:

| tip | count | check 9 |
|-----|-------|---------|
| `f5dff6ae` (BASE) | 1 | green |
| `f1be0b49` (origin/main side of the merge) | 8 | green |
| `08040d24` (build side of the merge) | 6 | green |
| `ded17252` / HEAD | 10 | RED |

Neither parent was red. The merge is. This build supplied exactly two of the ten — `08040d24` (`.memory-tree.conf`, the ARMS_FLOORS bump) and `e62f6f32` (`tools/memory-tree/check-memory-hygiene.sh`, unit 3) — and without them the count is 8 and the leg is green, so this build's own commits are the marginal cause, not bystanders.

**Why it is a blocker and not a nuisance.** The carrying leg is declared in `tools/gate-legs.json` as `{"name": "kickoff-manifest ratchet", "argv": ["bash", "skills/session-kickoff/manifest-check.sh"], "chunk": "records", "subject": "repo", "ceiling": 60}` with **no `guard` key**. `tools/run-gates/run-gates.sh:794` skips only guarded legs, so this one runs on every bar — including the scoped push-boundary run, and including a records-only commit. `origin/main` resolves to `ded17252`, and the only commit between it and HEAD touches `memory/LIVE.md`, the build folder and the ledger, so the red is live on the default branch right now. Every node that pushes next inherits a refusal this run created.

**The mechanism, which matters for the fix.** `e62f6f32` DID add a §B body entry — the pre-commit leg's cost, the guard, and the orphaned-hook-tree trap — and a body change is exactly what advances this stamp. The reconcile merge `ded17252` then dropped that entry to fit check 7's 25600-byte cap while taking main's own body growth (the `GATE_BOUND` bullet, the ceiling line, a rewritten dated correction). So the body change that would have reset the counter was removed and the counter was left over. Worse, `e62f6f32`'s commit message reasons explicitly from "1 watched commit against a 10-commit threshold" to justify not advancing the sha. That premise was true when written and false eight commits later in the same run, and nobody re-checked it. This is the amendment-leaves-its-other-half-standing shape: the half that reset the counter was deleted, the half that declined to advance the sha was not.

**The cap is parked and will fight the fix.** `wc -c memory/guides/SESSION-KICKOFF.md` is 25598 against `MAX_MANIFEST_BYTES=25600` at `skills/session-kickoff/manifest-check.sh:169`. There are two bytes of headroom. A body change large enough to be honest does not fit without making room first.

**Fix.** In one follow-up records commit: re-read §B against the merged tree; make room (the surviving half of the dropped trap — a timed-out commit orphans its hook tree, so a raised timeout is the wrong remedy — is the entry worth restoring, and one of the two dated corrections is the obvious place to prune from); land the body change; advance `last-body-change` to the same sha F2's re-stamp uses. Confirm with `bash skills/session-kickoff/manifest-check.sh` exiting 0.

**Left-shift gate.** The leg already catches the state; what it does not catch is the moment of creation. Add a merge-time predicate to the pre-push decision — cheapest as a new arm in `skills/session-kickoff/manifest-check.test.sh`, and cheapest of all as a bug-class entry under `memory/gotchas/` selected for `memory/guides/SESSION-KICKOFF.md` plus `.githooks/*`: *a ratchet whose counter is a count over a commit range is sub-threshold on both parents and over it on the merge, so both sides individually pass and the merge does not*. The machine-checkable form, if it earns its keep: `manifest-check.sh` reds a merge commit whose check-9 count exceeds the max of its parents' counts, with a message naming both parents — that is the case a per-branch run structurally cannot reach.

---

### F2 — high — `memory/guides/SESSION-KICKOFF.md:5`, `last-audit`

**The defect.** `last-audit` names `b4e1d5be879bc8868529fb57c15657e271c39113`, and five watched files changed after it with no re-stamp at or after the change. Two of the five are this build's own edits.

**Reproduced.** The same gate run exits 1 on a second, independent check:

```
MANIFEST check 5 FAILED — watched files changed since last-audit with no re-stamp at/after
the change:
  .memory-tree.conf
  .unattended.conf
  tools/gate-legs.json
  tools/memory-tree/check-memory-hygiene.sh
  tools/run-gates/run-gates.sh
```

**Honest framing — this is NOT a fresh red.** Reproduced in detached worktrees: check 5 was already failing at BASE `f5dff6ae`, naming one file (`tools/run-gates/run-gates.sh`), and already failing at `f1be0b49`, naming three. So the build inherited a broken check 5 and grew it from three files to five.

**What is nevertheless this build's.** Two things, and they are why this is a HIGH rather than a footnote:

- The run **paid for this repair and then undid it.** Commit `f16cb918` re-stamped `last-audit` from `f5dff6ae` to `b4e1d5be` with the message "re-stamp last-audit to the merged tree, superseding both sides". Two commits later `08040d24` changed `.memory-tree.conf` — a watched file — with no re-stamp. `git log b4e1d5be..HEAD -- .memory-tree.conf` returns exactly that one commit. The repair the run made is gone, undone by the run itself.
- `e62f6f32` (unit 3, `tools/memory-tree/check-memory-hygiene.sh`) is not reachable from `b4e1d5be` either, so even the mid-run stamp never covered this build's own unit-3 edit.
- The charter's kickoff-manifest merge exception assigns the post-merge fresh audit and re-stamp to the **merging** run, and `ded17252` is this build's merge. The merge landed; the audit that closes it did not. §1's manifest Definition-of-Done item is unmet for this build's own change.

**Fix.** Fold into the same commit as F1: re-verify the §B claims derived from `.memory-tree.conf` and `tools/memory-tree/check-memory-hygiene.sh` (the two this build owns) and from the three it inherited, update any claim they made stale, then re-stamp `last-audit` with a fresh timestamp and `ded172527621226aed8f4b9f3dcf78234ac084e2` — the merge-base against `origin/main`; on the default branch the rule takes post-merge HEAD instead. F1 and F2 then clear in one commit, which is the whole reason to fold them.

**Left-shift gate.** The gap is not detection — check 5 detects fine — it is that the refusal is invisible until someone runs the bar, and this run demonstrably re-broke it two commits after fixing it. Wire the manifest ratchet into the tracked `.githooks/pre-commit` fast leg, scoped: if the commit stages any path in the manifest's own `watch:` list and does not also touch `memory/guides/SESSION-KICKOFF.md`, refuse with the file that needs the stamp. That is a `git diff --cached --name-only` intersection against a list the manifest already declares, it costs nothing, and it fires at the exact moment `08040d24` undid `f16cb918` instead of an hour later at the push boundary.

---

### F3 — blocker — `memory/project/unarmed-branches.txt:42` — INHERITED, not billed to this build

**The defect.** The shrink-only pin row exempting `tools/unattended/check-unattended.sh` check 30 branch 2 is still present, but that branch is now armed, so the arms ratchet refuses.

**Reproduced at HEAD.** `python tools/memory-tree/check-arms.py --check` exits 1:

```
HYGIENE check-arms: memory/project/unarmed-branches.txt:42 pins
tools/unattended/check-unattended.sh check 30 branch 2, which IS armed now
— delete the row (the pin is shrink-only)
```

**Attribution, established rather than assumed.** Green at BASE `f5dff6ae` (rc=0, verified in a detached worktree). RED at `f1be0b49`, the origin/main side of the reconcile, in its own detached worktree — so the red predates the merge and exists independently of this build. `git log -S` on the arming assertion string returns `9ea8f94c` ("fix(unattended): three arms in check-unattended.test.sh graded nothing", `aWarmedTether`), and `git merge-base --is-ancestor 9ea8f94c 08040d24` is false — that commit is not on this build's side. `git diff f5dff6ae..HEAD -- memory/project/unarmed-branches.txt` is empty: this build never touched the file. None of the three units' arms armed a pinned branch.

**Why it is still in this report.** The leg `harness arms (fail branches armed or pinned)` in `tools/gate-legs.json` carries `subject: repo` and no `guard`, so it runs on every bar. The tree being landed fails it, and a closing review that says CLEAN over a red bar is worthless. The billing changes who fixes it, not whether it must be fixed before this landing is complete.

**Fix.** One deleted line, plus its now-false justification. Delete row 42, and delete the comment block at lines 35–41 that justifies it — "No fixture can arrange that", "not 'an arm nobody wrote' but 'an arm that cannot be written from here'". The new arm demonstrably writes it, so leaving the prose while deleting the row is the same amendment-leaves-its-other-half-standing shape as F1, one level up. Re-run `python tools/memory-tree/check-arms.py --check` and confirm rc=0.

**Left-shift gate.** `check-arms.py` already catches the row; what it does not catch is the orphaned justification. Extend it: when a pin row is deleted, or when a row's contiguous preceding comment block survives it, red naming the comment's line range. Cheaper still and probably enough — require every pin row to carry its justification as a trailing field on the row itself rather than as a free comment above it, so deleting the row deletes the reason by construction and the two halves cannot separate.

---

## What was checked and found sound

Recorded so a later round does not re-spend the tokens.

- **Template/rendered parity holds.** `tools/unattended/SKILL.template.md:205` and `.claude/skills/unattended/SKILL.md:205` carry the literal `RUN the orientation probes` at the same line, byte-identical. The two-answers-to-one-question class does not apply here — the rendered file is a faithful render and shows no hand-edit.
- **Check 20's fourth locator is section-scoped, not whole-file.** `tools/unattended/check-unattended.sh:1774` slices `$psec` and takes the first index hit; the vacuity refusal at `:1777` names both literals it looked for. That is the design its spec mandates, and it is not the rejected whole-file grep.
- **The `--staged` guard on check 23 matches its four siblings.** The guard sits at `tools/memory-tree/check-memory-hygiene.sh:1121`, structurally identical to `:667`, `:1051`, `:1066` and `:1076`.
- **`.memory-tree.conf` ARMS_FLOORS 99:98 -> 101:100** is consistent with three new arms landing; the floors ratchet up, which is the direction the check requires.
- No finding in the fixture-passes-by-finding-nothing, assertion-between-two-derived-values or absence-assertion-over-whole-file-text classes survived verification over this build's files.

## The state this leaves

The three units' code is sound and none of these findings asks for a code change, a new unit, or a design revision. All three are records-and-stamps defects at the landing boundary, and F1 plus F2 close in a single follow-up commit. F3 closes in one deleted row and one deleted comment, and belongs to whoever picks up the inherited red first — it is red on `origin/main` for every node, not just this one.

The landing is BLOCKED until `bash skills/session-kickoff/manifest-check.sh` and `python tools/memory-tree/check-arms.py --check` both exit 0 at the tip.
