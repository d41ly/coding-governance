**Serves:** diff-review TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 TOOL-aGraftedHelix-16 TOOL-aGraftedHelix-17 TOOL-aGraftedHelix-18 TOOL-aGraftedHelix-19 TOOL-aGraftedHelix-20 TOOL-aGraftedHelix-21 TOOL-aGraftedHelix-22 TOOL-aGraftedHelix-23 TOOL-aGraftedHelix-24 TOOL-aGraftedHelix-25 TOOL-aGraftedHelix-26 TOOL-aGraftedHelix-27 TOOL-aGraftedHelix-28

# Tier-2 closing diff review — aGraftedHelix, ROUND 1

*Node `a`, 2026-10-05, Tier-2, on `branch/helixir-review-gov-adoption-ce32e1`. This is the closing
review of build aGraftedHelix over its cumulative diff at the integration boundary. It ran through
`tier2-review.js`: five finder lenses, five skeptic batches, then this synthesis. The range runs from
the merge-base with `origin/main` to the run's tip, so it holds only this build's net change. That is
28 units across seven kits, plus two reconciling merges with `origin/main` (the first brought
aWardedAudit, aBatchedMinors and dUnstuckLanding, the second aEvidencedLens). It touches 185 files,
+24423/−398. The branch HEAD (`90a6f6fae`) is two records-only commits past the range tip. The
owner's prompt and the helixir review the build adopts are
`prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-0-run-mandate.md`. Every unit was verified by its
builder with sliced suites and staged breaks only. No whole self-test suite and no merge bar had run
when this review ran. The synthesis spot-checked findings 2, 3, 12, 13, 20 and 21 against the blobs
at `a49d53d5`; the other rows carry the skeptics' verified text.*

**Reviewed range:** `c3ef67429fef8327a8854a17a77d14e19b39b7fd...a49d53d5700dc9e4229784334528e7475313acc9`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is graded BLOCKER. The verdict is not CLEAN, because 24 findings stand and
three of them are HIGH, forming three HIGH items.

**Decision needed before `--close`:** H2 (id 20). This build's README declares `spec-audit:` under
`authorized-by: prompt`. Since the first reconciling merge, the merged driver's check 89 refuses
that state, and the run-mandate prompt record at BASE does not quote the owner asking for the
audit. `--close aGraftedHelix` therefore fails `authorization-reachable`, which takes no override.
The run cannot close through its protocol until the orchestrator or the owner picks one of the
two exits under H2.

The other two HIGHs are defects in shipped mechanisms. H1 (id 1): the by-design block handed to every
lens and skeptic is rendered from the tree under review, so a diff can write its own review
exemption, and this round's own three by-design entries were written by this range. H3 (id 21): the
`--settle` verb the first reconciling merge brought in never writes the run claim, so a settled
hand-off stays `held` on the remote for good.

Under TOOL-aBatchedMinors-5, every finding a closing review confirms is promoted to a unit. That is
three units for the HIGHs and one batched unit for the 21 minors (`highs 3 · minors 21`). The
minors split cleanly into two write sets at most: the recall kit's self-test plus `row_grammar.py`
(ids 4, 10, 11, 19, 28), and everything else. The `row_grammar.py` half shares the memory-tree kit's
version carriers with H1's unit, so one batched unit is the simpler choice.

## Review shape

Intensity full. Raw 28, confirmed 24, refuted 4, unverified 0 (0 uncertain). Precision 0.86.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 7 | 5 | 2 | 0 | 0 | 0.71 |
| seams | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |
| intent | yes | 9 | 8 | 1 | 0 | 0 | 0.89 |

- Adjudicated tally by raw confirmed finding: BLOCKER 0, HIGH 3 (ids 1, 20, 21), MEDIUM 13 (ids 2,
  3, 6, 7, 12, 14, 15, 16, 17, 19, 22, 23, 25), LOW 8 (ids 4, 9, 10, 11, 13, 26, 27, 28). That is
  24 findings.
- Adjudicated tally by item: BLOCKER 0, HIGH 3 (H1 to H3), MEDIUM 9 (M1 to M9), LOW 4 (L1 to L4).
  That is 16 items.
- Merges are mine, made at write time, and each joins findings of one binding grade only. Ids 3, 15
  and 22 are one defect (M1). Ids 6, 12 and 23 are one defect (M2). Ids 9 and 27 (LOW) are the same
  defect as id 17 (MEDIUM), so they stand apart as L1 beside M8. Ids 4, 10 and 28 (LOW) are the same
  defect as id 19 (MEDIUM), so they stand apart as L2 beside M9. Ids 13 and 26 are one defect (L4).
  Each split pair needs one fix.
- Every binding grade is kept. Ids 13 (medium to low) and 16 (low to medium) carry the skeptic's
  re-grade, which is their binding grade.
- Four refutals: two duplicates (ids 5 and 18) and two by-design calls on the card's remote read
  (ids 8 and 24). Precision 0.86 is well above the 0.5 floor, so a second round needs no tighter
  priming. It does need the by-design input fixed; see Run integrity.
- Intent: 14 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 86 items, each assigned to exactly one of 5 lenses: security 18, correctness 17, seams
  17, verification 17, intent 17.
- By design: 3 invariants from the checklist's by-design block.

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 22 judged sound, 2 judged UNSOUND (ids 7 and 22), 0 none proposed, 0
  NOT JUDGED. Where a fix was judged unsound, only the skeptic's corrected fix appears below.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic (ids 13 and
  16).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Every count above that should be zero is zero, so the run is complete for those briefs.
- One caveat on the inputs. The three by-design invariants this round was handed are
  `canary-waits-on-a-rendezvous-not-a-clock`, `concurrent-runs-are-announced-not-refused` and
  `sweep-issues-no-cost-verdict`. All three are records this range adds, which is H1's live
  instance. No refutal in this round cites any of them, and the one that anchors `unattended.sh`
  explicitly excludes the same-slug claim refusal. But a finding a lens withheld because of them
  leaves no trace, so their effect on this round is unmeasured. A second round should render the
  by-design block at the base, where the invariant kind does not exist, so that block is empty.

## The builder-reported gaps, answered

1. **Unit 26, AC3's "no claim pushed when the claim could not be read" never observed red alone.**
   Confirmed, and explained: it cannot go red in its fixture (M8, L1). The once-only mktemp shim is
   always absorbed before any push can run.
2. **Unit 21, the spec-commit stage's `git commit` takes the whole index.** Confirmed (M1). The
   ordinary rider is the run's own staged RUN.md, not only foreign work.
3. **Unit 4, no standing arm for recall's evidence banner or `extract.py`'s `superseded` line.**
   Confirmed (M9, L2).
4. **Unit 9, the row-key regex spelled five times in `row_grammar.py`.** Confirmed as a drift risk
   only (L3). All five copies are byte-identical today.
5. **Unit 2, the card's remote read adds about 4 s to SessionStart, bounded at 15 s.** The cost
   itself was refuted as a defect twice (ids 8 and 24), because spec 2 accepts and measures it. One
   narrower finding was confirmed (M5, id 14): the read runs even where `RUN_CLAIMS` is off, the
   shipped default, where no node writes a claim and the read buys nothing.
6. **Unit 27, `derive_self_rel` costs about 120 ms per driver load.** No lens raised a finding. The
   cost stands as the builder reported it and was not measured by this review.

## The reconciling merges, judged

- `tools/unattended/unattended.sh`: two semantic conflicts that no textual conflict showed. The
  merged check 89 now refuses this build's own README (H2). The merged `--settle` verb was never
  given the claim write that this build added to every other terminal writer (H3). The renumber of
  the claim checks from 89-93 to 107-111 missed one dossier (L4).
- `tools/workflows/unattended-build.template.js`: no finding against the merge resolution. M1 and M2
  sit on this file, but both are defects in this build's own units 15, 21 and 28.
- The VERBS template: no finding.
- These zeros come from five lenses on generic briefs. No lens died, so the set is complete for
  those briefs, but a zero here is not positive evidence that the resolutions are right.

## BLOCKER

None.

## HIGH

### H1 — the by-design block is rendered from the tree under review, so a diff writes its own review exemption (id 1)

- **Where:** `tools/memory-tree/gotchas.py:549` (`cmd_for_paths` renders every selected invariant
  through `render_by_design`), with `cmd_for_diff` at `:566`. The consumer is
  `tools/workflows/tier2-review.template.js:372-392`, which cuts the block into `byDesign`, and
  `:930`, which tells every skeptic to refute any finding a by-design entry covers.
- **Defect:** `cmd_for_diff` holds the range's changed paths but passes only those paths to
  `cmd_for_paths`. That function selects invariants from `records(root, m)` at the subject's tip. A
  diff that adds or edits a `kind: invariant` gotcha therefore adds itself to the by-design list.
  Check 18 only asks that the cited decision id exist somewhere, and the same diff's spec can define
  it.
- **Impact:** A checklist item can only widen a review; this block narrows one. Spec 3's "same trust
  as the checklist" argument therefore does not hold. The live instance is this round: all three
  by-design entries are files the range adds, and one anchors `unattended.sh`, whose
  `check_single_live` the range rewrites. The same channel is open in `unattended-build`: a caller's
  `checklist` argument and agent-returned checker stdout reach the spec audit through
  `renderChecklistUnion` unchecked.
- **Fix (judged SOUND by the skeptic):** Pass `changed` and the range base from `cmd_for_diff` into
  `cmd_for_paths`. Render each by-design line from the invariant's text at the base (`git show
  <base>:<path>`). An invariant whose record path is in `changed` prints as a checklist item, for
  example `- [ ] NEW/CHANGED invariant <name> - verify the ruling before treating it as by design`,
  and never inside the by-design block. Add a `gotchas.py --selftest` arm that adds an invariant
  inside the range and asserts the by-design count excludes it.
- **Still open after that fix:** the skeptic notes that it cures only the `--for-diff` path that
  `tier2-review` uses. The `--for-paths` spec-audit channel has no range to compare against, and its
  fix is still to be designed. One candidate is to render it at the run's pinned BASE.
- **Left-shift:** the selftest arm above, observed RED against today's code before the fix lands.
  Add a `tier2-review` harness arm that feeds a diff adding an invariant and asserts `byDesign`
  excludes it, so the class is pinned at the consumer as well as the producer.

### H2 — this build's README declares a spec audit the merged check 89 refuses, so `--close` cannot pass (id 20)

- **Where:** `memory/builds/aGraftedHelix/README.md:8` (`spec-audit: 2026-10-04` under
  `authorized-by: prompt`, at the pinned BASE `5266d22e`). The refusal is
  `tools/unattended/unattended.sh:2985-2991` (`check_authorization`, check 89). `--close` reaches it
  through `authorization-reachable` (`:9252`), which is in `DOD_NO_OVERRIDE` (`:740`). A take-over
  reaches it at `:7579`.
- **Defect:** TOOL-aWardedAudit-4, in the merge-base, made the spec audit an owner-only opt-in.
  TOOL-aEvidencedLens-22 narrowed it: a prompt-mode README is admitted only when the prompt record at
  BASE quotes the owner asking for the audit. No prompt record here matches `SPEC_AUDIT_ASK_RE`;
  the run mandate never asks for the audit. Neither reconciling merge squared the README with that
  ruling. The README's own build rule ("Spec audit: declared by the run, not the owner") is the
  self-opt-in the ruling forbids.
- **Impact:** `--close aGraftedHelix` fails check 89, `authorization-reachable` reads unmet, and
  `specs-audited` reads "not gradable". The suite arm at `unattended.test.sh:3812-3826` asserts this
  exact outcome. The BASE blob cannot be edited. The planned `specs-audited` override also cites a
  ruling that names unit 26 only, while units 27 and 28 are unaudited too. The refusal is loud, so
  this is HIGH, not BLOCKER: nothing wrong lands, but the build cannot close through its protocol.
- **Fix (judged SOUND by the skeptic):** Decide this before `--close`. Either re-preflight the slug
  onto a BASE whose README carries no `spec-audit:`, or land it as an owner hand-off. Record in the
  README and RUN.md that TOOL-aWardedAudit-4 supersedes the run-declared audit. Widen the override
  reason to cover units 27 and 28.
- **Left-shift:** a reconciling merge that brings in a new authorization or DoD check should re-run
  the DoD's `authorization-reachable` item against the merged driver, so a merged-in refusal reds
  at the merge rather than at the close. Until a verb or arm runs that item outside `--close`, it
  joins the project's bug-class checklist as a documented post-merge check.

### H3 — `--settle` never writes the run claim, so a settled hand-off stays `held` on the remote for good (id 21)

- **Where:** `tools/unattended/unattended.sh:6010`, the handed branch of `run_settle`
  (`:5917-6045`).
- **Defect:** The handed branch sets phase LANDED, runs `stage_or_fail` and returns, with no claim
  write on any branch. `--settle` came from dUnstuckLanding with the first reconciling merge, so this
  build's claim feature never covered it. A hand-off's claim was last written `held` by `run_hold`
  (`:5786-5789`), and `read_claims` maps `held` to verdict `held` at any age.
- **Impact:** With `RUN_CLAIMS` on, this repo's setting, a landed hand-off is reported as held
  forever, on every card and at every other slug's `--preflight`. The supported re-run of the same
  slug from another session reads foreign `held` and is refused at check 107. Nothing clears it
  short of a manual ref delete. Spec 1 rev-7 fixed exactly this for the in-place `--landed`
  (`:5091-5098`). The lease-dead branch likewise leaves a `live` claim to age to stale and be
  announced.
- **Fix (judged SOUND by the skeptic):** After `run_settle`'s `stage_or_fail`, add the status-write
  block `--landed` uses: `read_claims soft`, then `check_claim_writable status` with the record's
  keepalive and session plus the record, then `write_claim landed`. The record's lease facts make the
  hand-off's held claim read `mine`. Use `aborted` on the lease-dead branch. Add `--settle` to STOPS
  §7's status-write list, and add an arm: handoff, then settle, then `--claims` reads terminal.
- **Left-shift:** the arm above, plus a class gate in the unattended suite: enumerate every function
  that writes a terminal phase (`set_fact ... phase LANDED|ABORTED|...`) and assert each one also
  calls `write_claim`, or is on a named exemption list. A new terminal writer then reds until it
  writes the claim or says why not.

## MEDIUM

### M1 — the spec commit stage commits the whole index, so already-staged paths ride a `Pass: none` commit (ids 3, 15, 22)

- **Where:** `tools/workflows/unattended-build.template.js:920`, the bare `git commit -q -m
  'spec(<slug>): ...' ... --trailer 'Pass: none'` at the end of `commitBlock` (`:899-920`). The input
  check at `:244` uses `git diff --name-only`, which sees unstaged changes only.
- **Defect:** `rec` and the delta loop only decide what the block itself stages. Anything already in
  the index is committed by the pathless commit. `check_commit_message` returns 0 on any `Pass: none`
  trailer (`unattended.sh:11537`), so no commit-time check grades that content.
- **Impact:** The ordinary rider is the run's own RUN.md. `stage_or_fail` in `--resume`'s holder
  row, `--preflight`, `--dispatch`, `--hold` and others leaves it staged and uncommitted. Foreign
  staged work in the same worktree rides the same way. The commit is misattributed under
  `spec(<slug>)`, and only check 23 at the close grades the paths. This contradicts spec 15 §5's
  "keeps a foreign change out of the commit, tracked or untracked". Nothing is lost, and the commit
  is local and revertable, so the effect is contained. The GH16 and GH21 fixture plants only an
  unstaged edit and untracked files, which is why no arm saw this.
- **Fix, id 3 (judged SOUND by the skeptic):** Commit by explicit pathspec. Collect the paths the
  post-render loop stages into a variable, using process substitution rather than a pipeline
  subshell, then run `git commit -- <spec paths> $rendered`. Every other staged entry stays staged
  and out of the commit. Do not refuse on a non-empty index, because the driver's staged RUN.md would
  make that refuse every run. Add a real-git arm that pre-stages a foreign file and asserts it is
  absent from the spec commit.
- **Fix, id 15 (judged SOUND by the skeptic):** Before the commit, refuse when `git diff --cached
  --name-only` lists a path outside the spec paths and the paths the render changed. Or commit with
  an explicit pathspec built from those same two sets.
- **Fix, id 22 (REJECTED by the skeptic; the skeptic's corrected fix):** Commit only the stage's own
  paths. Collect the generator-output paths the loop stages into a variable, using process
  substitution rather than a pipe so the variable survives the loop. Then run `git commit --only -q
  -m ... -- <spec paths> $staged_delta`, which leaves any pre-staged path, RUN.md included, staged
  and out of the commit. Add a real-git arm that pre-stages a foreign tracked file and a RUN.md edit,
  then asserts neither is in HEAD's tree diff and both are still staged.
- **Synthesis:** take the pathspec route that ids 3 and 22 agree on. Id 15's refusal option would
  refuse every run in which the driver left RUN.md staged, which is the reason the refuted duplicate
  id 5 gave against the same option. The arm should pre-stage both a foreign file and a RUN.md edit.
- **Left-shift:** the real-git arm above. For the class, add a grep gate over the workflow templates
  that reds any `git commit` inside an agent-run block that carries no ` -- <pathspec>`.

### M2 — the by-design head is spelled four times, and the parity checker built to hold it sees two (ids 6, 12, 23)

- **Where:** `tools/workflows/unattended-build.template.js:497` re-declares `BY_DESIGN_HEAD`, and
  `:516` emits the merged head from its own string literal (`'# by design — ' + n + ' invariant(s)
  this selection touches'`). `tools/workflows/check_by_design_parity.py:7` and
  `tools/workflows/README.md:202` both say the head is "spelled twice, in two kits".
- **Defect:** Unit 15 added the third and fourth spellings before unit 28 was specced. Unit 28's
  checker evaluates only `gotchas.py` against `tier2-review.template.js`. The only pin on the build
  harness's copy is the GH15 arm (`unattended-build.test.sh:1532-1533`). It byte-compares the regex
  declaration lines and never the `:516` literal, and its leg is a kit self-test the bar holds unless
  `GATE_SELFTESTS=1`.
- **Impact:** Suppose the head is reworded in `gotchas.py` and `tier2-review` together. The bar's
  parity leg goes green. `renderChecklistUnion` then stops recognising the resolver's block, files
  its `- <invariant>` entries as checklist items, and appends a stale head. On the spec-audit route
  that is the silent by-design loss unit 28 exists to stop, or, as id 6's skeptic notes, more often
  a loud count refusal in `extractByDesign`. Either way the checker's stated population is wrong, so
  it misleads the next change. The effect is review noise or a refusal, not a wrong landing.
- **Fix, id 6 (judged SOUND by the skeptic):** Extend `check_by_design_parity.py` to evaluate the
  `BY_DESIGN_HEAD` literal in `unattended-build.template.js` too, and render the union's head through
  the same sample counts. Alternatively, derive the emitted head in `renderChecklistUnion` from the
  first head it parsed rather than a literal, and add the third file to the checker's evaluated set.
  Correct the docstring's "spelled twice".
- **Fix, id 12 (judged SOUND by the skeptic):** Emit the head from one place and check it against
  the pattern when the script loads, for example `const head = '# by design — ' + n + ' invariant(s)
  this selection touches'; if (!BY_DESIGN_HEAD.test(head)) throw new Error(...)`. Or add an arm that
  feeds `renderChecklistUnion` output through `tier2-review`'s `extractByDesign`. Then correct the
  "spelled twice" claim in `check_by_design_parity.py` and in `tools/workflows/README.md`.
- **Fix, id 23 (judged SOUND by the skeptic):** Extend `check_by_design_parity.py` to evaluate
  `unattended-build.template.js`'s `BY_DESIGN_HEAD` too, and to run its `renderChecklistUnion` head
  through the tier2 pattern; it already evaluates a template literal in node. Alternatively, derive
  the `:516` literal from the regex. Then correct the header's "spelled twice" and its "does not
  check" list.
- **Left-shift:** make the checker derive its own population. Have it grep every tracked file for
  the head's fixed text (`invariant(s) this selection touches`) and red on any file it does not
  evaluate. A fifth spelling then joins the check or reds the bar, which gates the class rather than
  the instance.

### M3 — a claim push during a landing deletes push-main's verdict files (id 2)

- **Where:** `tools/unattended/unattended.sh:2059` (`write_claim` removes the refusal file and
  pushes), against `.githooks/pre-push:334`, which runs `rm -f "$PUSH_REFUSAL" "$PUSH_BAR"` before
  its skip-nondefault exit.
- **Defect:** Both pushes' hooks share the run worktree's git dir. `resume-tick.sh:296` runs
  `--beat` in that worktree on every tick, and a live claim's beat falls due every 1350 s here
  (`RESUME_STALE_BOUND=5400`). That is inside a 16-to-65-minute landing bar, so under
  `RUN_CLAIMS=on` the overlap is the expected case. `write_claim`'s own comment assumes the opposite:
  "a token read after it came from THIS push's hook".
- **Impact:** A beat that lands mid-bar clears `pre-push-bar`, so push-main writes no lander marker
  and `--landed` refuses the green, pushed landing at check 34. The skeptic corrects one detail:
  push-main prints "NOT writing the lander marker" and exits 0, not 1. A cleared `gate-red` token
  makes push-main classify a red bar as a race and re-run it. It fails closed and never lands red,
  so the effect is contained.
- **Fix (judged SOUND by the skeptic):** In `write_claim`, and so in `--beat`, skip with rc 2 and an
  announced reason while `<git-dir>/push-main-active` exists. push-main already holds that marker in
  the same git dir for the whole of its push (`tools/push-main.sh:120`). Add an `unattended.test.sh`
  arm that plants the marker and asserts no claim push runs and both verdict files survive.
- **Left-shift:** the arm above. The class is a verdict channel with a second writer; add it to the
  project's bug-class checklist as "every file the lander trusts has exactly one writer per push".

### M4 — `--preflight` pushes its live claim before refusals that need nothing from it (id 7)

- **Where:** `tools/unattended/unattended.sh:6253` (the claim CAS), after the write gate at `:6245`.
  Four refusals follow it: `write_landed_record` and the rotation `GIT mv` (fail 29, about
  `:6278-6280`), the SRC-marker region check (fail 9, `:6299`), `scaffold_runmd` (fail 9, `:6307`),
  and the GEN-marker check (fail 9, `:6309`).
- **Defect:** Each of those ends in a bare `return 1`, and nothing rolls the claim back. The block's
  own rule is that "NOTHING is written until every precondition above has passed", and a remote claim
  is a write.
- **Impact:** A preflight refused for malformed README markers prints "the run-state file is
  unchanged" and exits 1, while the remote holds `refs/gov/runs/<slug>` at `live` for a run that
  never started. Another session's `--preflight` or take-over is refused at check 107 until the beat
  ages past `RESUME_STALE_BOUND`, and `--claims` announces the phantom run. The same session's retry
  reads `mine` and renews, and the refusing paths are narrow, so the effect is contained.
- **Fix (REJECTED by the skeptic; the skeptic's corrected fix):** Move the SRC-marker region check
  above the write gate; it is a pure read. Move the GEN-marker check above the gate only for a
  run-state file that exists and is not being rotated (`rotate != 1`). After a rotation the check has
  to grade the freshly scaffolded file, not the archived one. For the failures that cannot move
  (`write_landed_record`, the `GIT mv`, `scaffold_runmd`), undo only what this call did, and only
  when `CW_ACT` was `create`: delete `refs/gov/runs/<slug>`, leasing on the commit this call just
  pushed. `write_claim` never refreshes `CW_SHA`, so capture that sha from the push. On renew,
  rewrite, take or take-announced, leave the claim in place and print one line saying it was left.
  Writing `aborted` over a renewed `mine` claim would end a live run's claim, and the claim a take
  replaced cannot be restored.
- **Left-shift:** one arm per post-gate refusal (malformed SRC markers first, since it is the
  easiest to stage) asserting `git ls-remote` shows no claim ref after a refused first preflight.
  The class is "a remote write counts as a write"; add it to the bug-class checklist beside the
  write-gate rule.

### M5 — the card's remote read ignores `RUN_CLAIMS`, so the shipped dark default still pays a fetch per SessionStart (id 14)

- **Where:** `skills/session-kickoff/manifest-check.sh:390` (`derive_claims_line`), which gates only
  on `.unattended.conf` existing and a driver resolving, then runs `--claims`. `print_claims` calls
  `read_claims strict`, which fetches whatever `RUN_CLAIMS` says (`unattended.sh:1798`, `:1910`).
- **Defect:** The shipped value in `.unattended.conf.example:164` is `RUN_CLAIMS="off"`. With the
  switch off no node writes a claim, so the cell can only say none, skipped, or name leftover
  terminal claims. Unit 2's spec predates the switch and never mentions it.
- **Impact:** Every adopter of the unattended kit pays a remote fetch at each SessionStart, up to the
  15 s bound on an unreachable remote, for a cell that carries no information. The skeptic corrects
  the finder on one point: with an empty namespace the fetch writes no refs, so the ref-pollution
  half of the impact is mostly moot. The latency stands and is contained.
- **Note on the refuted siblings:** ids 8 and 24 raised the read's cost and were refuted as by
  design, because spec 2 accepts and measures it. This finding survives on the narrower ground
  that the read buys nothing when the switch is off, which the spec never weighed.
- **Fix (judged SOUND by the skeptic):** Gate the read on the switch through the driver rather than a
  second reader of the conf. For example, have `--claims` print one `claims: off` line with no fetch
  when `RUN_CLAIMS` is off, or add a mode for that, and have the card render it as `claims —
  skipped: RUN_CLAIMS is off`.
- **Left-shift:** a `manifest-check` arm with `RUN_CLAIMS=off` in the fixture conf, asserting the
  card line reads `skipped: RUN_CLAIMS is off` and the git shim logs no fetch.

### M6 — `read_claims soft` lets check 24 fail the verb after its record writes (id 16)

- **Where:** `tools/unattended/unattended.sh:1843`. `read_claims` (`:1834-1845`) restores `status`
  and `RUNLOG_CHECKS` only on the `quiet` branch.
- **Defect:** Under `soft`, `resolve_claim_remote`'s `fail 24` sets `status=1`, and that becomes the
  process exit (`:12391`). The soft callers that never run `observe_anchor` first are `verb_abort`
  (`:5486`), `run_hold` (`:5786`), `verb_resume`'s re-bind and holder row (`:7810`, `:7897`, `:7988`)
  and `verb_dispatch` (`:11919`). Their own comment promises a claim step "announced and never
  failing the verb". `--landed` is not affected, because its `observe_anchor` refuses at check 24
  first.
- **Impact:** If a second remote is added mid-run, those verbs finish their record writes and
  staging, then exit 1 with `UNATTENDED check 24 FAILED`. An agent reading the exit as a failed
  `--dispatch` may dispatch again and write a second row. The path is narrow, but the consequence is
  a wrong exit after side effects. The skeptic re-graded this from low to medium, which binds.
- **Fix (judged SOUND by the skeptic):** Under `soft`, restore `status` and `RUNLOG_CHECKS` after
  `resolve_claim_remote` the way the quiet branch does, so check 24 only feeds `CL_WHY` and the one
  announced line.
- **Left-shift:** an arm that adds a second remote after preflight and asserts `--dispatch` exits 0,
  prints one announced claim line, and writes exactly one row.

### M7 — unit 27's handed-off discovery was neither adopted nor parked (id 25)

- **Where:** `memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-27.md:81`, which
  hands off "a class gate over the location probes ... 20 of them after this unit" with "this run's
  orchestrator adopts it as a unit or parks it".
- **Defect:** RUN.md's Parked section holds no row for it, and the README's Parked decisions list
  only the check-arms gate. HEAD `90a6f6fae` adds nothing either. The new class record
  `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md` says the gate was "handed off
  rather than implied here", to a recipient that never took it.
- **Impact:** The mandate says not to backlog anything, and BUILD-METHOD names adopt or park as the
  only dispositions. The discovery was dropped silently, and the class record misleads the next
  reader into thinking someone owns the gate. The class record already names a documented manual
  check meanwhile, so no behaviour changes.
- **Fix (judged SOUND by the skeptic):** Before the close, either add a unit for the location-probe
  class gate or park a decision row with the M2/M3 veto that blocks it, and point the class record's
  "Its gate" section at that row.
- **Left-shift:** a close-time documented check: every spec line that hands a discovery to the
  orchestrator resolves to a unit or a parked row in RUN.md. If the hand-off wording is fixed, this
  can become a grep arm in the close.

### M8 — GH26 AC3's "no claim pushed" assertion cannot fail in its own fixture (id 17)

- **Where:** `tools/unattended/unattended.test.sh:14132`, in the GH26 AC3 arm (`:14097-14135`).
- **Defect:** The once-only mktemp shim fails the first `mktemp` after the fetch marker. On any path
  that pushes after the failed claim read, that first `mktemp` is `write_claim`'s own `d=$(mktemp)`
  (`unattended.sh:2054`), which runs before `observe_remote ... push`. So the push never reaches the
  shim's log, and the assertion is always green.
- **Impact:** AC3's red-when, "the row pushes a claim it could not read", is certified by an
  assertion that cannot go red. The regression is still caught, but by accident: the absorbed
  failure lets the `prior-session` add succeed, so the exit, check-17 and session assertions red
  instead. GH24 AC1's away leg does not catch it at all. A later change that re-keys the shim loses
  even that accidental coverage.
- **Fix (judged SOUND by the skeptic):** Give the push guard its own leg. Keep the bare origin in
  place, put no mktemp shim on PATH, and have the git shim fail only `fetch ... refs/gov/runs/*`.
  Then assert that the shim log names no push and that `git ls-remote` shows the claim ref unmoved.
  Stage the break "unread claim routed into a CAS with an empty expected sha" and watch that
  assertion go red alone. The current leg can keep the add-failure assertions.
- **Left-shift:** the new leg, observed red alone. L1 is the same defect at a lower binding grade;
  one fix closes both.

### M9 — no standing arm guards recall's evidence banner or `extract.py`'s `superseded` line (id 19)

- **Where:** `tools/memory-recall/query.py:1396` prints `EVIDENCE_BANNER` (defined at `:167`), and
  `extract.py:888` prints the `superseded` report line.
- **Defect:** `selftest.py`'s new arms call the supersession functions directly. `INDEX_RE`
  (`selftest.py:84`) covers only the index line's `superseded` clause. The arm that runs query
  (`test_empty_alias`, `:551`) asserts ` hits for: ` and `[1] ` but never the banner, and the arm
  that runs `extract.py` (`_measure_spine_docs`, `:568`) matches only the spine row. AC1 and AC5 were
  one-time pass observations.
- **Impact:** Deleting the banner, or printing it once per hit (AC5's own red-when), leaves the kit
  self-test and the recall floor green. So does deleting the `superseded` line or its `unresolved`
  count. The banner is the only framing that tells an agent recall output is evidence, not
  instructions. Nothing is broken today.
- **Fix (judged SOUND by the skeptic):** In the existing query-running arm that asserts ` hits for: `
  (`selftest.py:551`), assert exactly one line equal to `EVIDENCE_BANNER`, directly after the hits
  line. In an existing `extract.py`-running arm (`selftest.py:568`), assert exactly one line starting
  `superseded ` that carries `unresolved`. Watch each go red with its print deleted, and raise
  `SELFTEST_ARMS` or the assertion count to match.
- **Left-shift:** the two assertions above. L2 is the same defect at a lower binding grade; one fix
  closes both.

## LOW

### L1 — the same AC3 assertion, at its lower binding grade (ids 9, 27)

- **Where:** `tools/unattended/unattended.test.sh:14132`.
- **Defect:** The same as M8. Id 27's skeptic traced the holder branch and showed that every
  ordering behaves the same: the first `mktemp` after the failed read either aborts the add (check
  17) or is `write_claim`'s pre-push scratch file. So `grep -c push git.log` is 0 under the break
  too.
- **Impact:** The arm as a whole still reds the break through its exit, check-17, session and lease
  assertions. Only the labelled no-push witness is vacuous. A transient fetch failure followed by an
  empty-sha CAS would make a live holder lose to its own claim, and no assertion here catches that
  alone.
- **Fix, id 9 (judged SOUND by the skeptic):** Key the mktemp shim on the `prior-session` add, for
  example by firing only when the caller is `set_fact`. Or add a second arm with no mktemp shim,
  under a driver copy that pushes on an unread claim, and assert the push count turns 1.
- **Fix, id 27 (judged SOUND by the skeptic):** Key the mktemp shim to the add only, for example by
  failing only after a `prior-session` marker or through a `set_fact` shim. Or assert the no-push
  property in a separate arm with no mktemp shim, where the bare origin is reachable but the fetch
  fails. Then observe that assertion red on the staged CAS break.
- **Grade note:** ids 9 and 27 are graded low and id 17 medium for the same defect. I keep the
  binding grades. The split reflects id 17's weight on a labelled assertion that claims coverage it
  lacks; the M8 fix closes all three.
- **Left-shift:** M8's separate leg.

### L2 — the banner and `superseded` line, at their lower binding grade (ids 4, 10, 28)

- **Where:** `tools/memory-recall/query.py:1396` and `extract.py:888`.
- **Defect:** The same as M9. A search of every `*.py`, `*.sh`, `*.js` and `*.json` under `tools/`
  and `.githooks` finds no arm asserting the banner or its text. The mandate's item 3 asks for the
  banner by name.
- **Impact:** A later edit that drops or duplicates either print passes every arm. The banner text is
  correct today.
- **Fix, id 4 (judged SOUND by the skeptic):** Add a `selftest.py` arm that runs `main()` over the
  existing fixture corpus and asserts exactly one line equal to `EVIDENCE_BANNER`, directly after
  the `<n> hits for:` line. Observe it red once with the print removed.
- **Fix, id 10 (judged SOUND by the skeptic):** Add a selftest arm that runs `query.main` over the
  fixture corpus, captures stdout, and asserts `count(EVIDENCE_BANNER) == 1` on the line after `<n>
  hits for:`. Add a second arm that runs `extract.main` and asserts one `superseded` line carrying
  the map counts.
- **Fix, id 28 (judged SOUND by the skeptic):** Add a `selftest.py` arm that runs `main()` over the
  fixture corpus and asserts that `EVIDENCE_BANNER` occurs exactly once, on the line after `<n> hits
  for:`. Add one that runs `extract.py` and asserts a `superseded` line carrying per-pattern counts.
  Observe both red with the print removed.
- **Grade note:** id 19 carries the same defect at medium. The binding grades are kept, and the M9
  fix closes all four.
- **Left-shift:** M9's two assertions.

### L3 — the row-key regex is built five times in `row_grammar.py` (id 11)

- **Where:** `tools/memory-tree/row_grammar.py:1062`, and the same pattern at `:322`, `:811`,
  `:1142` and `:1291`. The base had two copies; this diff added three, for checks 27 and 28.
- **Defect:** All five are byte-identical today and all derive the id from `id_pattern(conf)`, so
  there is no wrong result now.
- **Impact:** A grammar fix applied to check 20's `scan` alone would let checks 27 and 28 enumerate
  a different row population from check 20, with no gate noticing.
- **Fix (judged SOUND by the skeptic):** Hoist one `derive_row_re(conf)` beside `id_pattern` and call
  it at all five sites.
- **Left-shift:** a `row_grammar` selftest assertion that the pattern's literal text occurs exactly
  once in the module, so a sixth copy reds.

### L4 — the claim-check renumber missed the codebase-map dossier (ids 13, 26)

- **Where:** `memory/map/features/unattended-stops.md:56-57`, a paragraph this diff added. It still
  names the claim refusals as check 89 (`--preflight` and take-over) and check 90 (the holder's
  verbs).
- **Defect:** Commit `5db6e3894` moved the claim checks from 89-93 to 107-111 before merging main. It
  built its inventory from the driver, the suites, the confs and the templates, and its exemption
  covers only `memory/builds/`. In the merged driver, check 89 is aWardedAudit's spec-audit opt-in
  refusal (`unattended.sh:2990`) and the `--hold` hand-off-code refusal (`:5600`), and check 90 is
  the `--handoff` code refusal (`:5867`).
- **Impact:** A session using the codebase map to find the claim refusals lands on two unrelated live
  checks. The guides, the VERBS and STOPS templates and the SKILL all say 107 and 108, so the record
  disagrees with itself. Prose only; no behaviour changes. Id 13's skeptic re-graded it from medium
  to low, which binds.
- **Fix, id 13 (judged SOUND by the skeptic):** In `memory/map/features/unattended-stops.md`, change
  "check 89" to "check 107" and "check 90" to "check 108", and name check 109 for a read that does
  not complete.
- **Fix, id 26 (judged SOUND by the skeptic):** Change "check 89" to "check 107" and "check 90" to
  "check 108" on lines 56-57. Then grep `memory/map`, `memory/guides` and `memory/gotchas` for the
  other old numbers in a claim context.
- **Left-shift:** a renumber is an inventory problem. Add to the bug-class checklist that a check
  renumber greps the whole tracked tree, excluding only `memory/builds/`, and lists every hit in the
  commit message.

## Refuted

- **id 5:** a duplicate of id 3, at the same line with the same consequence. Its fix's refusal
  option was judged unsound, because the driver's staged RUN.md would make it refuse every
  unattended spec commit. That reasoning is carried into M1's synthesis.
- **id 8:** by design. Spec 2 records the card's remote read as an accepted, bounded and measured
  cost. The driver documents that `--claims` reads whatever `RUN_CLAIMS` says. M5 survives on a
  narrower ground.
- **id 18:** a duplicate of id 15. Its fixture gap (no staged foreign path in
  `build_spec_commit_repo`) is carried into M1's regression arm.
- **id 24:** by design, on the same ground as id 8. Spec 1 S16 keeps `--claims` as the remote
  reader either way, and spec 1 §4's "never exposed by a kit update" concerns claim writes and
  refusals, not a read-only card fetch.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | security | tools/memory-tree/gotchas.py:549 | high | high | confirmed | The block is new in this range: the base gotchas.py has no invariant kind and no render_by_design. cmd_for_paths (gotchas.py:533-551) selects invariants from records(root, m) at the tree it runs in, and cmd_for_diff (566-576) passes only the changed paths, never which records the range itself added. tier2-review.template.js:372-392 cuts the block into byDesign, and line 930 tells every skeptic 'BY DESIGN (refute any finding one of these covers)'. So a diff that adds a kind: invariant record narrows its own review. A checklist item can only widen one, which is why spec 3 section 5's 'same trust as the checklist' argument fails. The live instance is real: all three by-design entries in this round's prompt are files the range adds (git diff --name-status shows A). concurrent-runs-are-announced-not-refused anchors unattended.sh, whose check_single_live the range edits (diff hunk at 2746). The path needs a diff whose new invariant covers a defect in that same diff, which is narrow, so the grade is high rather than blocker. Fix verdict: the fix cures the --for-diff path that tier2-review uses. The tier2 parser does not count-check class items, so an extra '- [ ]' item cannot refuse, and the existing invariant arms call cmd_for_paths with no changed set, so they are unaffected. It leaves open the --for-paths spec-audit channel that the finding also names, which has no range to compare against. | sound |
| 2 | security | tools/unattended/unattended.sh:2059 | medium | medium | confirmed | Claim pushes are new in this range. The hook's unconditional rm -f of pre-push-refusal and pre-push-bar (.githooks/pre-push:334) runs before the skip-nondefault exit (909), so any claim push clears both files. write_claim (unattended.sh:2059) also removes the refusal file itself, and RUNLOG_GITDIR is the worktree's own git dir. The landing push runs in the run worktree ('in the run worktree: ... --land', unattended.sh:5851), and push-main --land writes its files to that same git dir. The hook writes pre-push-bar before the bar and does not write it again after. resume-tick.sh:296 runs --beat in that worktree on a LIVE verdict. This repo sets RUN_CLAIMS=on and RESUME_STALE_BOUND=5400, so a beat falls due every 1350 s, which is inside a 16-65 minute bar. One detail is wrong: write_lander_marker's '*)' branch sets lm='' and returns 0, so push-main prints 'NOT writing the lander marker' and exits 0, not 1. The consequence is the same: a green, pushed landing has no marker, and --landed refuses it with check 34. It fails closed, so the effect is contained. Fix verdict: the fix is sound. push-main-active lives in the same git dir for the whole push. A marker leaked by SIGKILL would also hold back claim writes in that worktree, but the next push-main run's EXIT trap clears it. | sound |
| 3 | security | tools/workflows/unattended-build.template.js:920 | medium | medium | confirmed | The spec commit stage is new in this range (the base template has no such stage). commitBlock (unattended-build.template.js:899-920) ends with a bare 'git commit -q -m ...' and no pathspec, so it commits the whole index. rec and the delta loop only decide what the block itself stages, and the input check uses 'git diff --name-only', which sees unstaged changes only. Driver verbs routinely leave RUN.md staged: stage_or_fail runs in verb_phase, verb_preflight, run_takeover and others. check_commit_message returns 0 on a 'Pass: none' trailer (unattended.sh:11537), so already-staged content is committed under 'spec(<slug>)'. That contradicts spec 15 section 5, 'keeps a foreign change out of the commit, tracked or untracked'. The effect is contained: check 23 grades the paths at the close, and the usual rider is the run's own RUN.md. Fix verdict: committing by explicit pathspec gives git's --only semantics. Only the named paths' working-tree content is committed, and every other staged entry stays staged. The specs and the loop's adds are in the index, so the pathspec resolves. Collecting the paths through process substitution is required, because the current pipeline runs the loop in a subshell. | sound |
| 4 | security | tools/memory-recall/query.py:1396 | low | low | confirmed | EVIDENCE_BANNER is defined at query.py:167 and printed only at query.py:1396. A search of tools/memory-recall (selftest.py included), every *.py, *.sh, *.js and *.json under tools/, and .githooks finds no arm that asserts the banner or its text; the only other hits are unrelated run-selftests prose. So dropping or rewording the banner keeps every gate green. The banner is correct today, so this is a missing guard with no current effect on behaviour. Fix verdict: the fix is sound. The banner is one line with no embedded newline, so asserting exactly one equal line directly after the hits line pins it. | sound |
| 5 | correctness | tools/workflows/unattended-build.template.js:920 | medium | - | refuted | Duplicate of id 3: same defect, same line (the spec commit stage's bare git commit takes the whole index), same consequence. The claim itself is accurate. Judged separately, the fix's option (a) is unsound. verb_phase, verb_preflight and the holder verbs leave the run-state file staged through stage_or_fail, so refusing on any staged path other than the specs would refuse every unattended spec commit. Option (b), commit only the paths the block stages, is the sound one. | unsound |
| 6 | correctness | tools/workflows/unattended-build.template.js:497 | medium | medium | confirmed | This range adds both renderChecklistUnion (unit 15) and check_by_design_parity.py (unit 28). The union re-declares BY_DESIGN_HEAD at unattended-build.template.js:497 and writes the emitted head as a string literal at line 516. Its own comment admits that both are copies of tier2-review's head. check_by_design_parity.py evaluates only tier2-review.template.js, and its docstring says the head is 'spelled twice'. A reword of the head in gotchas.py and tier2-review together therefore passes parity while the union files the reworded head and its entries as checklist items and appends a stale head. That is the value-beside-its-source rule broken by the very checker built to enforce it, and it misleads the next change. The impact is narrower than claimed: tier2's extractByDesign then usually finds the reworded head in the union output, and its count check mostly refuses loudly rather than passing a silently misfiled checklist. So medium. Fix verdict: the fix is sound. The template has exactly one one-line BY_DESIGN_HEAD declaration, which the checker's evaluator requires, and deriving or rendering the union's head closes the third spelling. | sound |
| 7 | correctness | tools/unattended/unattended.sh:6253 | medium | medium | confirmed | The write gate is at tools/unattended/unattended.sh:6245. The claim CAS is at 6253 and is new in this diff; base c3ef6742 has no write_claim. Four failures come after the CAS: write_landed_record and the rotation `GIT mv` (fail 29, around 6278-6280), the SRC-marker region check (fail 9, 6299), scaffold_runmd (fail 9, 6307), and the GEN-marker check (fail 9, 6309). Each one ends in a bare `return 1`. PF_CLAIM is never read after 6253, and nothing in the verb or the 12367 dispatch rolls the claim back. SRC (`gen:build-index`) and UNITS (`gen:build-units`) are separate marker pairs (lines 1100 and 1120), so the UNITS check above the gate does not cover the SRC one. The spec placed the write before rotation and scaffold so that a lost race leaves the tree untouched, but it says nothing about the opposite case, a published claim followed by a local refusal. On these paths a `live` claim stays on the remote for a run that never started. A different session or keepalive reads it as foreign-live, and check 107 refuses it until the beat passes RESUME_STALE_BOUND. The effect is contained: the same session's retry reads `mine` and renews it, and the refusing paths are narrow (malformed README markers, or a failed scaffold or mv). | unsound |
| 8 | correctness | skills/session-kickoff/manifest-check.sh:390 | medium | - | refuted | By design, per the unit-2 spec and the driver. Spec S2 says adoption is read from the tree, so `.unattended.conf` present means the card reads. Section 5 'risks' records the accepted cost: 'Every card write in a tree adopting the unattended kit now starts the driver once'. The perf/scale line accepts one bounded remote read at 15 s, and AC10 records the measured cost. The driver states the read is deliberately not gated: unattended.sh:1798 says 'nothing below runs while RUN_CLAIMS is `off`, except `--claims`, which only reads', and the print_claims header says it 'reads whatever RUN_CLAIMS says, because a read changes nothing'. The 'lands DARK' comment at 576 is about claim writes and refusals, the behaviour that changes what a run may do. The read writes nothing to the remote and moves only the driver's private cache namespace, which S7 records. The effect is a documented, bounded latency, not a defect. | unsound |
| 9 | correctness | tools/unattended/unattended.test.sh:14132 | low | low | confirmed | The AC3 arm at unattended.test.sh:14108-14141 uses a once-only mktemp shim that fires on the first `mktemp` after the failed claim fetch. write_claim (unattended.sh:2041) calls a bare `d=$(mktemp)` before it builds the commit or pushes, and set_fact (6555) calls a bare `tmp=$(mktemp)` too. Whichever runs first after the failed read takes the one shimmed failure. Take the mutant that routes the unread claim into a CAS (cw=0 with CW_SHA empty): write_claim's mktemp fails, it returns 2 before any `git push`, and the add then succeeds. The push count stays 0, and the arm goes red only through its rc-1 and check-17 assertions. Take the other order: the add fails first and returns 1 before any write. Either way the line 'the git shim's log names no push' cannot go red on its own while this shim is armed. It is a test-coverage gap with no effect on behaviour. | sound |
| 10 | correctness | tools/memory-recall/query.py:1396 | low | low | confirmed | query.py:1396 prints EVIDENCE_BANNER once, after `<n> hits for:`, and extract.py:888 prints the `superseded` report line. A repo-wide grep finds no test that asserts either one. selftest.py's CLI arm, test_empty_alias around line 551, checks only that ' hits for: ' and '[1] ' are present. INDEX_RE at selftest.py:84 matches query.py's index line at 1381, not extract.py's `superseded` line. Spec 4's AC5 is a one-time grep observation, not a standing arm. Dropping the banner, or printing it once per hit, would pass the self-test. This is a coverage gap; behaviour is correct today. | sound |
| 11 | correctness | tools/memory-tree/row_grammar.py:1062 | low | low | confirmed | The pattern `^\s*[-*]\s+[`*]*(` + id + `)\b` appears at row_grammar.py lines 322, 811, 1062, 1142 and 1291. At base c3ef6742 there were two copies, at 285 and 774, so this diff added three. All five are byte-identical today and all derive the id from id_pattern(conf), so there is no wrong result now. The finding is the drift risk only, which makes it low. | sound |
| 12 | seams | tools/workflows/unattended-build.template.js:516 | medium | medium | confirmed | unattended-build.template.js:516 emits the merged head from its own literal, '# by design — ' + n + ' invariant(s) this selection touches'. That literal is not tied to BY_DESIGN_HEAD at line 497 or to anything else. check_by_design_parity.py runs only gotchas.py's render against the tier2-review template's regex, and its docstring (lines 7-8) and README.md:202 say 'spelled twice, in two kits', which this diff makes false. The GH15 arm byte-compares only the two `BY_DESIGN_HEAD = ...` declarations. Its merged-output assertion hard-codes the expected head, a fourth spelling. Suppose someone rewords the head, updates gotchas.py, both regexes and the GH15 fixtures, and leaves line 516 and the expected string alone. GH15 stays green, line 516 prints the old head, tier2-review's extractByDesign finds no block, byDesign logs 'none supplied', and the `- <invariant> — …` lines become checklist items. Base has none of this (unit 15/28 code). The result is review noise on the spec-audit route, not a wrong landing, so medium. | sound |
| 13 | seams | memory/map/features/unattended-stops.md:56 | medium | low | confirmed | At a49d53d5, memory/map/features/unattended-stops.md:56-57 (a paragraph this diff added) still says check 89 and check 90. In the merged driver, check 89 is the spec-audit opt-in refusal (unattended.sh:2990) and the --hold hand-off-code refusal (5600), and check 90 is the --handoff code refusal (5867). The claim refusals are fail 107 (2007, preflight and take-over), fail 108 (2010 and 2092, holder) and fail 109 (1860 and 2093, a read or write that does not complete). Commit 5db6e3894 renumbered everything else and missed this dossier. The error is in prose only and changes no behaviour, and the guides, templates and SKILL give the right numbers, so it is graded low. | sound |
| 14 | seams | skills/session-kickoff/manifest-check.sh:390 | medium | medium | confirmed | derive_claims_line (manifest-check.sh, at a49d53d5) gates only on the .unattended.conf file existing and a driver resolving. It then runs `bash $drv --claims`, and print_claims calls read_claims strict, which fetches from the remote whatever RUN_CLAIMS says (unattended.sh:1798 and 1910). So every adopter of the unattended kit pays a remote fetch at each SessionStart, including the shipped default RUN_CLAIMS="off" in .unattended.conf.example:164. Unit 2's spec never mentions RUN_CLAIMS. It was written before S16 added the switch, and the decision row TOOL-aGraftedHelix-2 priced the read (1.6 s to 5.4-6.5 s) on node a, where the switch is on. With the switch off, no node writes a claim, so the cell can only say none, skipped or leftover terminal claims, and an unreachable remote costs up to the 15 s bound. One correction to the finder: with an empty namespace the fetch writes no refs, so the ref-pollution half of the impact is mostly moot. The latency cost stands and is contained. | sound |
| 15 | seams | tools/workflows/unattended-build.template.js:920 | medium | medium | confirmed | The commitBlock (unattended-build.template.js, around line 920 at a49d53d5) ends in `git commit -q -m 'spec(...)' ... --trailer 'Pass: none'` with no pathspec, so the commit takes the whole index. The input check is `git diff --name-only -- "$root" ...`, which compares the worktree with the index, so a path already staged with no further edit is never listed. The delta loop skips every path in rec, but that does not unstage it. The driver's verbs routinely leave the run-state file staged and uncommitted: stage_or_fail is called in --resume, --dispatch, --hold and the others. When a caller launches the harness in that state, RUN.md rides a `spec(<slug>)` commit marked Pass: none. That breaks the prompt's promise that foreign paths are never taken by this stage. The GH16/GH21 fixture (build_spec_commit_repo) plants only an unstaged edit and untracked files, so no arm sees this. Nothing is lost and the effect stays in this worktree's history, but the commit is misattributed and no pass check grades it. | sound |
| 16 | seams | tools/unattended/unattended.sh:1843 | low | medium | confirmed | read_claims (unattended.sh:1834-1845) restores status and RUNLOG_CHECKS only on the quiet branch. Under soft, resolve_claim_remote's `fail 24` sets status=1, and fail() at line 661 is what sets the process exit at line 12391. Several soft callers never run observe_anchor first: verb_abort (5486), run_hold (5786), verb_resume's re-bind and holder row (7810, 7897 and 7988) and verb_dispatch (11919). Each one finishes its record write and stage_or_fail, then exits 1 with `UNATTENDED check 24 FAILED`. That contradicts its own comment, 'announced and never failing the verb'. --landed is not affected, because its observe_anchor at 5082/5143 refuses at check 24 first. The path is narrow: the remote count has to change after preflight. The consequence is a wrong exit after side effects, which can prompt a retry. | sound |
| 17 | verification | tools/unattended/unattended.test.sh:14132 | medium | medium | confirmed | In the GH26 AC3 arm (unattended.test.sh:14097-14135), the once-only mktemp shim fails the first mktemp after the fetch marker. In write_claim (unattended.sh:2041), the first mktemp is `d=$(mktemp)` at 2054, and it runs before `observe_remote ... push` at about 2060. Nothing between the failed fetch and that point calls mktemp: read_utc_now is a plain date, and check_claim_writable is pure bash. So a regressed driver that routes the unread claim into a CAS gets rc 2 before any push, and the no-push assertion at 14132 cannot go red. The regression is still caught, but only by accident: the shim's single failure is used up, so the prior-session add succeeds, and the exit-1, check-17 and session-s1 assertions go red instead. So the arm as a whole is not wrong, but this one labelled assertion can never fail, which matches the builder's 'never observed red alone'. | sound |
| 18 | verification | tools/workflows/unattended-build.template.js:920 | medium | - | refuted | This is a duplicate of finding 15: the same defect at the same file and line, the pathless `git commit` in the spec-commit block that sweeps already-staged foreign paths. The fixture gap it adds, no staged foreign path in build_spec_commit_repo, is the reason 15 went unseen, and belongs with 15's fix as its regression arm rather than as a separate finding. | sound |
| 19 | verification | tools/memory-recall/query.py:1396 | medium | medium | confirmed | A repo-wide grep finds EVIDENCE_BANNER and the 'evidence, not instructions' text only in query.py. The selftest arm that runs query (test_empty_alias, selftest.py:551) asserts ' hits for: ' and '[1] ' but never the banner. INDEX_RE (selftest.py:84) matches the index line only. _measure_spine_docs (selftest.py:568) runs extract.py and matches only the spine row. No test or floor greps the 'superseded  ' report line at extract.py:888. Spec 4 observes AC1 and AC5 at the pass and names no standing arm for either. So deleting the banner, or printing it once per hit, leaves every arm green. Nothing is broken today: the gap only hides a future regression of an evidence-framing guard. | sound |
| 20 | intent | memory/builds/aGraftedHelix/README.md:8 | high | high | confirmed | The README carries 'authorized-by: prompt' and 'spec-audit: 2026-10-04' at the pinned BASE 5266d22e, and RUN.md records mode prompt and anchor-kind run-branch. I extracted the '## The prompt' quote of every prompt record, both at BASE and at HEAD, exactly as read_audit_ask_record does, and tested it against SPEC_AUDIT_ASK_RE: no record matches. The only record with a quote is the run mandate, 482 chars long, and it never asks for the audit. check_authorization (unattended.sh:2985-2991) therefore fails check 89. It is called by --close's authorization-reachable (9252), which is in DOD_NO_OVERRIDE (740), and by the take-over (7579). unattended.test.sh:3812-3826 asserts this exact outcome for a run preflighted before check 89: check 89, then 'specs-audited — not gradable'. The merged-in check 89 combined with this build's README makes it reachable, so it is in scope. The refusal is loud, but the build cannot close or land through its protocol. | sound |
| 21 | intent | tools/unattended/unattended.sh:6010 | high | high | confirmed | run_settle (unattended.sh:5917-6045) has no claim write on any branch. The handed branch sets phase LANDED, stage_or_fail runs, and it returns. --settle is absent from the pinned BASE and arrived with the reconciling merge, so this diff's claim feature never covered it. A hand-off's claim was last written 'held' by run_hold (5786-5789). read_claims maps 'held' to verdict held at any age. check_claim_writable sends preflight:foreign-held to the preflight:* branch, check 107. The rotation path of --preflight after a derived LANDED reads claims with the new keepalive (6166-6170). A different session therefore reads foreign-held and is refused. Only the same harness session reads 'same'. RUN_CLAIMS is "on" in this repo's conf. STOPS §7's list of status writes omits --settle, and the in-place --landed got exactly this fix (5091-5098). | sound |
| 22 | intent | tools/workflows/unattended-build.template.js:920 | medium | medium | confirmed | The commit line in commitBlock (unattended-build.template.js:920) has no pathspec and no --only, so it commits the whole index. The input check reads only 'git diff --name-only', unstaged changes. A path already staged when rec is taken is skipped by the delta loop, because rec lists it, and then rides the spec commit anyway. That contradicts spec 15 §5's security bullet, which says step 2's record keeps a foreign change out of the commit, tracked or untracked. Spec 21 (lines 135-139) measured the same corollary. It calls the run-state case benign and defers foreign staged work to 'unit 16's whole-index commit', and that is never fixed. The harmful trigger is narrow, foreign staged work in the run's worktree, and the result is a local, revertable commit, so the effect is contained. | unsound |
| 23 | intent | tools/workflows/check_by_design_parity.py:7 | medium | medium | confirmed | unattended-build.template.js declares its own 'const BY_DESIGN_HEAD' at :497 and emits a literal head at :516. The bar's parity leg (check-protocol-parity.test.sh:405-417) runs check_by_design_parity.py over gotchas.py and tier2-review.template.js only. That checker's header says the head is 'spelled twice, in two kits'. The only pin on the build harness's copy is GH15 (unattended-build.test.sh:1533). That arm byte-compares the regex line with tier2-review.js and never compares the :516 literal. Its leg is chunk 'selftests' / subject 'kit', which the bar holds unless GATE_SELFTESTS=1. A reword in gotchas.py and tier2 alone therefore passes the bar, and renderChecklistUnion stops cutting the resolver's block, which is the silent class unit 28 exists to catch. | sound |
| 24 | intent | skills/session-kickoff/manifest-check.sh:397 | medium | - | refuted | This is the specified design, not a defect. Spec 1 S16 says '`--claims` stays the remote reader either way', and the driver's I2 header (unattended.sh:1908-1911) says it 'reads whatever RUN_CLAIMS says, because a read changes nothing'. Spec 2 gates the cell only on the conf and the driver (S2, S3). Its risks bullet says 'Every card write in a tree adopting the unattended kit now starts the driver once'. Its perf bullet budgets one driver start and one remote read bounded at 15 s, measured by AC10. A DECISIONS row supersedes KICK-aReplayedCard-1's card budget. Spec 1 §4's 'never exposed by a kit update' is about the dark-landed claim behaviour: no verb reads, writes or refuses on a claim. A read-only card fetch is not that. | unsound |
| 25 | intent | memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-27.md:81 | medium | medium | confirmed | Spec 27 line 81 (new in this range) hands off 'a class gate over the location probes ... this run's orchestrator adopts it as a unit or parks it'. At a49d53d RUN.md's Parked section holds rescope rows adding units 27 and 28 and a single decision row (the check-arms dispatch-block gate). No row mentions location probes. The README's 'Parked decisions' lists only the check-arms gate. HEAD 90a6f6fae adds nothing either. The new class record memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md (absent at base) says the gate is 'handed off rather than implied here'. The mandate (prompt record line 14/70) says 'do not backlog anything', and BUILD-METHOD line 307 names adopt/park as the dispositions. So the discovery was dropped with no disposition. The effect is contained: the class record already names a documented manual check meanwhile, and no behaviour changes. That makes it medium rather than high. | sound |
| 26 | intent | memory/map/features/unattended-stops.md:56 | low | low | confirmed | At base, memory/map/features/unattended-stops.md has no 'check 89/90' text, so this range introduced lines 56-57. They still say claim refusals are check 89 (preflight/take-over) and check 90 (holder). Renumber commit 5db6e3894 did not touch memory/map (its stat lists SKILL.md, the confs, guides and the suite only). Its exemption covers only memory/builds/. In the merged driver, 'fail 107' and 'fail 108' are the claim refusals (unattended.sh:2007, 2010, 2092). 'fail 89' is aWardedAudit's spec-audit opt-in (2990), and 'fail 90' is the --handoff code refusal (5867). The dossier therefore points at the wrong checks. The effect is documentary only. | sound |
| 27 | intent | tools/unattended/unattended.test.sh:14132 | low | low | confirmed | Traced the holder branch (unattended.sh ~7890-7915). A failed read_claims removes its scratch dir with no further mktemp, then leaves cw empty, so no CAS runs. The add's set_fact is then the first mktemp, and the once-only shim fails it. Under the staged break the header names (the unread claim routed into write_claim with an empty CW_SHA), the first mktemp after the failed fetch is write_claim's own 'd=$(mktemp)' at line 2054. That precedes observe_remote's push, so the write ends rc=2 'not completed' and never invokes push. The git shim logs nothing for push, and 'grep -c push git.log' = 0 holds under the break too. Any ordering behaves the same way: the first mktemp either aborts the call (the add, check 17) or is write_claim's pre-push scratch file. So the assertion at test.sh:14132 cannot go red in this fixture. The break is still caught by the exit, check-17, session and lease assertions, so coverage of the arm holds and only the named no-push witness is vacuous. Hence low. | sound |
| 28 | intent | tools/memory-recall/query.py:1396 | low | low | confirmed | EVIDENCE_BANNER (query.py:167, printed at 1396) and extract.py's 'superseded' summary line (888) are both absent at base, so both are new. In the recall kit's tests: selftest.py's INDEX_RE guards query.py's index-line 'superseded' clause, not extract.py's CLI line. The extract.py runs at selftest 568/657/734 assert only SPINE_RE, EMPTY SPINE and ZERO RECORDS. check-recall.py runs extract.py but reads no 'superseded' line. Nothing outside query/README/SKILL references the banner. Spec 4's AC5 and AC1 are pass-time acceptance probes, not standing arms. Dropping or duplicating either print passes every arm. The effect is contained to user-visible output, hence low. | sound |
