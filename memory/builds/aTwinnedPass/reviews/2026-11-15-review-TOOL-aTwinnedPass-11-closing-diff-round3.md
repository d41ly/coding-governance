**Serves:** diff-review TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 TOOL-aTwinnedPass-4 TOOL-aTwinnedPass-5 TOOL-aTwinnedPass-11

# Closing diff review, round 3: aTwinnedPass unit 11, the wf_ pass name, and the records since round 2

Tier-2 · 2026-11-15 · on `branch/dazzling-jackson-b895c0` · adversarial fan through `tier2-review.js`: 3 finder lenses (`gov-diff-reviewer`), 1 skeptic batch (`gov-skeptic`), then this synthesis (`gov-synthesizer`). The diff spans 24 files, +1229/−22, from round 2's tip `39a71c080` to `1bf0e9f78`. Unit 11 was merged as `12dfe39d2` and CLOSED at `1bf0e9f78`. The rest of the range is records only: close observations, the round-2 asks, the measurement record and unit 11's spec. Unit 11 admits the Workflow runtime's `wf_<run id>-<n>` pass name beside the Agent tool's `agent-<id>`. It does this through `PASS_NAME` in `unattended-unit.js`, from which `BRANCH_SHAPE` and `TREE_SHAPE` are built, and through `check_pass_branch` in `pass-tree.sh`. `check_pass_holder`'s rule is unchanged. Intent came from the 2 spec documents supplied and the range's commit messages. Every line ref below is pinned to the blob at the reviewed sha `1bf0e9f7`.

**Reviewed range:** `39a71c080570cc41b18898467931aed9acdeedb0...1bf0e9f787baabef67d94fe6d7550838fe8bd0ba`. **ROUND 3.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high. One item is MEDIUM. The suites do not pin the interior of the new `wf_` alternative, so a later loosening of it that admits a shell payload would leave every gate green. The shipped regex is correct today.

## Review shape

Intensity **light** · raw **1** · confirmed **1** · refuted **0** · merged **0** · unverified **0** (0 uncertain) · precision **1.00**.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated, by item: **0 BLOCKER · 0 HIGH · 1 MEDIUM · 0 LOW** (1 item).
Adjudicated, by raw confirmed finding: **0 BLOCKER · 0 HIGH · 1 MEDIUM · 0 LOW** (1 finding).

Id 1 keeps its binding medium grade. No refuted finding was shown, so no twin flag is raised.

## Run integrity

- Lenses **3/3** returned, **0 DIED**.
- Skeptic batches **1/1** returned, **0 DIED**.
- **0** contradictory verdicts were demoted to unverified, and **0** orphaned duplicate refutations were demoted.
- **0** duplicate refutations were counted as merged confirmations.
- **0** spurious verdicts were discarded, and **0** duplicates were removed.
- Fixes on confirmed findings: **0** judged sound, **0** judged UNSOUND, **1** judged INSTANCE-ONLY (id 1), **0** none proposed, **0** NOT JUDGED. An INSTANCE-ONLY fix cures the cited instance and leaves its class standing.
- Severity on confirmed findings: **0** UNGRADED by the skeptic, **0** RE-GRADED by the skeptic.
- Unverified findings: **0** answered UNCERTAIN, **0** with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`, synthesis `gov-synthesizer`.
- Intensity is **light**. The security and intent lenses were NOT run, so their classes were swept only through the checklist shares. This is not a full review.
- Intent: 2 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 33 items, acquired by the harness from `--for-diff 39a71c080570cc41b18898467931aed9acdeedb0..HEAD`. Each was assigned to one of 3 lenses: correctness 11, seams 11, verification 11.
- By design: the caller's byDesign.
- Refuted findings shown: 0. Same-address pairs shown: 0.
- Dispositions: unclassed values are refused. 33 class slugs were handed, and 175 leg names were read from `tools/gate-legs.json`.

Every count above is zero where it must be, so the finding set is complete for the lenses that ran. The zero yield of the correctness and seams lenses is evidence of absence only within a light review.

## MEDIUM

### M1 — no suite arm pins the interior of the new `wf_` alternative (id 1)

- **Where:** `tools/workflows/unattended-build.test.sh@5d68ca38:1499` (TP11, lines 1497-1508), `tools/unattended/pass-tree.test.sh@41b0ee18:420` (TP11, lines 420-424), and the shape under test at `tools/workflows/unattended-unit.js@6a84c2e9:449`.
- **What is wrong:** `PASS_NAME` is `agent-[A-Za-z0-9]+|wf_[0-9a-f]+-[0-9a-f]+-[0-9]+`, and `BRANCH_SHAPE` and `TREE_SHAPE` anchor it at the end. In `unattended-build.test.sh`, TP11 refuses only three values. The first is a payload after the trailing digits (`worktree-wf_0d688c69-edb-1$(id)`). The other two are the dash-less `worktree-wf_x` and `worktree-foo`. `pass-tree.test.sh` TP11 refuses only `worktree-wf_x`. So the run-id class, the middle-group class and the required third `-<n>` group are exercised only by AC1's one-shot `node -e` probe (spec line 295), which no suite re-runs. AC2's wording "Red when … admits a hostile tail" reads as covering the whole alternative, but the arms cover only the last group.
- **Consequence:** The finder staged two widenings against every TP11 and TP4 suite value. Under `wf_[^-]+-[^-]+-[0-9]+`, the suites stay green while `worktree-wf_$(id)-a-1` is admitted. Under `wf_[0-9a-f]+-[0-9a-f]+(-[0-9]+)?`, they stay green while `worktree-wf_0d688c69-edb` is admitted. A later edit that loosens either class would let builder-returned free text reach `nextAction`, and on the other end reach a git argument in `pass-tree.sh`, with every gate green. That breaks the unit's stated security boundary. The effect is contained because the shipped regex is correct today, so the binding grade is medium.
- **Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** Pin each group of the `wf_` alternative with its own refused value, in both suites.
  1. A payload inside the run id: `worktree-wf_0d$(id)-edb-1` with `/w/.claude/worktrees/wf_0d;id-edb-1`.
  2. A payload inside the middle group: `worktree-wf_0d688c69-e$(id)-1` with `/w/.claude/worktrees/wf_0d688c69-e;id-1`.
  3. A name missing `-<n>`: `worktree-wf_0d688c69-edb`.

  Add these to TP11 of `unattended-build.test.sh`, each asserting `"branch":""` and `"worktree":""`. Add the matching branch-shape `--remove` refusals (run-id interior, middle interior, missing `-<n>`) to `pass-tree.test.sh`. Each expects exit 1, the text `is not a branch the runtime cuts for a pass`, and the tree left in place. Raise `FLOOR_ASSERTIONS` by the count. Stage the breaks `wf_[^-]+-[0-9a-f]+-[0-9]+`, `wf_[0-9a-f]+-[^-]+-[0-9]+` and `(-[0-9]+)?` in each file, and watch each new arm go red.

  The finder's proposal cures the cited instance alone. It adds the run-id payload and the missing-`-<n>` returns to TP11, plus one `--remove` arm for `worktree-wf_0d688c69-edb`. It leaves the middle group unpinned and the `pass-tree.test.sh` interior refusals incomplete.
- **Left-shift gate:** This is the second round in a row where a confinement rule built from several parts had a part with no refused fixture (round 2's M3 was the primary-tree anchor). Add a line to this project's bug-class checklist: every group of a shape regex that guards a trust boundary gets one refused fixture that passes every other group, in every suite that checks the shape. Each group's staged break goes in spec §7. Mechanically, the `harness arms (fail branches armed or pinned)` leg could run the staged breaks a spec §7 names and require the named suite to go red.

review-shape kind=diff-review round=3 intensity=light at=synth raw=1 confirmed=1 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=1 low=0 agents=5 out-tokens=24424
review-round round=3 limit=- prior=3,0 count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | verification | tools/workflows/unattended-build.test.sh:1499 | medium | medium | confirmed | Confirmed against the code. In tools/workflows/unattended-unit.js:449, PASS_NAME is 'agent-[A-Za-z0-9]+\|wf_[0-9a-f]+-[0-9a-f]+-[0-9]+'. BRANCH_SHAPE and TREE_SHAPE (450-451) anchor it at the end. The TP11 arms in unattended-build.test.sh:1497-1508 feed only three refused values: a payload after the trailing digits ('worktree-wf_0d688c69-edb-1$(id)'), 'worktree-wf_x' and 'worktree-foo'. pass-tree.test.sh TP11 (420-424) refuses only 'worktree-wf_x'. Under the widening 'wf_[^-]+-[^-]+-[0-9]+', the $(id) tail still fails the anchored [0-9]+$, wf_x has no dashes and foo has no wf_, so every arm stays green while 'worktree-wf_$(id)-a-1' is admitted. Under '(-[0-9]+)?', 'worktree-wf_0d688c69-edb' is admitted, and that value appears only in AC1's one-shot node -e probe (spec line 295). No suite pins it. The gap came in with this diff's new wf_ alternative, so it is not pre-existing. The by-design notes do not cover it: ask 7 is about parity between the two files, not the interior of the pattern. AC2's general 'Red when … admits a hostile tail' wording also overstates what the arms check. Severity is medium: the shipped regex is correct today, and the effect is contained to a future loosening going unnoticed. | instance | - | new:shape-group-without-a-refused-fixture |
