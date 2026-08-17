# aTetheredConvoy — build record

What ran, what landed, and what did not. Derived from the branch, the review records under
`reviews/`, and the spec set's own `RESOLVED` marks. Every row here has a source on disk.

## What landed

| Unit | State | Commit |
|---|---|---|
| 1 — the truthful core | BUILT | `0dfc56f` |
| 2 — `update` | BUILT, blockers folded | `e4d14c4`, `7f8b172` |
| 3 — the convergence ratchet | BUILT | `a21e2ce` |
| 4 — the gate-runner declaration | BUILT | `66d6f18` |
| 5 — check carries evidence | BUILT | `0de03f7`, `9ea510b` |
| 6 — the merged region | **PART** — the region writer; the LF-pin block and its renormalize are not built | `9a939f8` |
| 7 — the harness | **PART** — the refusal join; the acceptance matrix and runbook parity gate are not built | `180bc8b` |

Five units whole, two in part. The selftest went 61 -> 170 arms, all holding, and the refusal join
enumerates 135 refusal branches with both of its pins derived rather than guessed.

**What is NOT built, named rather than implied.** Unit 6's line-ending pin block and the
`git add --renormalize` that follows it — the half whose spec carries four reproduced constraints,
including deriving the renormalize population from git rather than from a pattern string. Unit 7's
acceptance matrix over repo SHAPES, and the runbook parity gate with the runbook demotion it grades.
Each has a folded, audited spec; none is blocked by anything but session budget.

## Parked — the landing question

**This run does not merge and does not push, and could not have.** The unattended protocol requires a
committed standing mandate the run ASSERTS and cannot have written, reachable from the run's pinned
BASE. This run AUTHORED `memory/builds/aTetheredConvoy/`, so no such mandate exists at BASE
`0f0a121d` and the kit's own preflight would refuse. That refusal is correct and was not worked
around.

*Options seen:* start a formal unattended run and let its preflight decide; commit a mandate first
and then assert it; or build and commit on the unit branch and leave landing to the owner. *Chosen:*
the third. *Reason:* the second is precisely the bypass the protocol names — a run writing the
authorization it then reads — and the first would have refused for the same reason, more slowly.

## Parked — what is left, and why it is these two halves

**Unbuilt: unit 6's line-ending pin block with its renormalize, and unit 7's acceptance matrix with
the runbook parity gate.** Session budget, not design — both halves have folded, audited specs.

*Options seen at the point the budget bound:* spread the remaining budget thinly across both halves;
or take the piece of each that the rest of the build actually depends on and leave the piece that
stands alone. *Chosen:* the second. *Reason:* unit 6's REGION WRITER is what four other things
needed — it is what makes the `merged` role honourable, what unit 2's verdict table needed a real row
for, and what `check`'s drift arm had no precondition without; the pin block needs none of them and
is reachable on its own. Unit 7's REFUSAL JOIN grades the refusal population units 1–6 actually
produced, and that population only stopped moving when unit 6 landed; the acceptance matrix grades
repo SHAPES and does not depend on it.

*What that leaves, stated so it is not discovered:* an adopter gets no line-ending pins, so the
`gate-green-by-accident-on-generated-bytes` class stays open for a target on a foreign platform —
which is precisely the class this repo already records against itself, and which bit this very
session in three `.claude/skills/*/SKILL.md` renders. And the four repo SHAPES the contract names
(empty, non-Python, blocking hook, pre-existing red leg) are exercised by no fixture; the shapes the
selftest does exercise are the ones each unit needed.

*Deviation from the ordering contract, recorded:* unit 5 was built before unit 4. What unit 5 assumed
of unit 4 — `check --observe` and the emitted-leg presence loop — was not built at that point, so the
dependency was unused rather than violated; unit 4 landed afterwards and both are whole now.

## Parked — the full bar is unconfirmed, and what a failed run of it DID surface

A background `GATE_FULL=1 bash tools/run-gates.sh` exited 255 and its `gate-last-failure.txt` named
six red legs. **That verdict is unusable and was discarded**: the run started while this session was
still editing the tree, so it read files mid-write, and its leg names are the pre-rename spellings —
it was grading a tree that no longer exists. Recorded rather than deleted, because a discarded gate
result is exactly the kind of thing a later reader finds and believes.

Each of the six was then re-run individually against the COMMITTED tree, and two were real:

- **`drift-audit records` was genuinely RED, and the cause was this build.** The signal
  `non_terminal_specs_cited_by_product_source` is pinned at 2 and read 5: three comments in
  `tools/govkit/govkit.py` cited OPEN specs of this very build by id. That is the drift this signal
  exists to catch — product source pointing at a spec that has not closed — and the repair is to
  state the RULE in the comment and let the build folder hold the reasoning. Back to 2, green.
- **Three skill-wiring legs were red from a PRE-EXISTING condition, not from this diff.** The
  SessionStart hook reported CRLF on three `eol=lf`-pinned `.claude/skills/*/SKILL.md` renders before
  this session touched anything, and `git log` over this branch shows it never touched that tree. It
  is the worktree-checkout half of this repo's own `gate-green-by-accident-on-generated-bytes` class.
  Fixed with the documented remedy, `bash tools/check-wiring.sh --fix`; the index was already
  normalised, so the repair is worktree-only and there is nothing to commit for it.

The other three (`memory hygiene`, `codebase-map coverage + freshness`, and `check-wiring self-test`)
re-ran green or were progressing green when the node's time budget ran out.

**The full bar is still NOT confirmed green for this branch.** This node is far slower than the
charter's measured node — a single heavy shell leg exceeds several minutes and the suite exceeds the
session's budget — so the gap is an environment limit rather than a known failure. What IS confirmed,
per pass and re-confirmed against the committed tree: `govkit selfcheck`, `govkit selftest` (all
arms), `check-kit-versions`, `check-install-prefix`, `codebase-map coverage + freshness`, memory-tree
hygiene, the build-index render, `drift-audit records`, the three skill-wiring `--check` legs, the
kickoff-manifest ratchet (including its `--staged` leg, which blocked a commit until the audit block
was re-stamped), and `git diff --cached --check`.

This is a DoD gap, not a claim of green. It leads the wrap-up for that reason.

## Two owner-review items, flagged during the fork sweep and not settled by silence

- **Unit 4 F1** — the baseline EXECUTES target-authored code, twice per apply plus the target's own
  pre-commit hook, and the command comes from a file committed in the target repo. The resolution
  taken makes the committed descriptor the approval and re-prompts when the argv or its commit
  changes. That is a security posture resolved under delegation, and a posture deserves an owner's
  eye. **Unit 4 is now BUILT, so this is live**: an `apply` against a target declaring
  `kind = "manifest"` runs that target's own command twice and its pre-commit hook once. The argv and
  its source are printed before the first run.
- **Unit 6 F3** — appending gov's line-ending pins at the end of a target's attributes file makes
  gov's rules WIN, so a target that deliberately set the opposite is overridden and told, rather than
  refused. It is the one place this build knowingly overrides a target's own declared rule and answers
  with a message rather than a stop. **Still not live**: the pin block is the half of unit 6 that was
  not built, so nothing writes to a target's attributes file yet. The decision stands for whoever
  builds it.

## What the reviews cost, and what they bought

Three adversarial passes ran, all returning BLOCKED, and each one changed the work rather than
decorating it:

- the design pass over the finish-the-deployer scope: 10 blockers, and its structural finding — that
  the combined work re-decided four shared facts when specced as one body — is why this build has
  seven ordered units instead of one spec.
- the M4 spec audit: 19 blockers over 60 candidates. It re-resolved a fork by measurement (a landable
  `project-owned` would have won zero destinations) and falsified a reuse claim (this repo already
  ships AST enumeration joined to an execution trace, which unit 7 said did not exist).
- the fold re-audit: 8 blockers. Its headline finding was about CODE and was verified independently
  before folding — the carve-out changes no byte on this tree, because destination last-wins already
  elects the seed template, so the criterion written to grade it had no red state.

The pattern across all three is the one this repo already names: the defects were not the findings a
pass missed, they were disagreements between two paragraphs written in the same pass.

## Parked — the landing is blocked on a third convergence, and it is a real one

The merge to `main` completed and every gate was green at `49e06d9`. The PUSH is not done: local is
25 ahead / 10 behind, and `tools/push-main.sh` reconciles before the gate, so it re-enters a merge
with `origin/main`.

That merge resolves structurally — both files parse, `govkit selfcheck` exits 0, and 177 of 186 arms
hold. It is filed as `DEPL-aTetheredConvoy-8` rather than landed, because the 9 red arms are not
merge damage; they are a **semantic disagreement between upstream's landed classifier and this
branch's receipt schema 2**, and upstream's arms predate the schema.

`TOOL-dClosedLexicon-13` made `plan` and `apply` share one predicate — `ROLE_KINDS` plus
`derive_rule_kind` — and deleted the role filter from the arm that compares plan's write set to
apply's receipt, correctly: under schema 1 every receipt row was `engine` or `seed`, so the whole
receipt *was* the write set. Schema 2 records a row for every file gov is responsible for, including
`rendered`, `attributes` and `project-owned`. The comparison has to filter to `LANDABLE_ROLES` on the
receipt side — which is exactly what the conflicted arm's filter was for, and what its own comment
said.

Four separable questions, stated so the next pass measures rather than guesses:

- **the expected per-role mark counts move**, because unit 6 adds 9 `ORDER|attributes` pin rows that
  did not exist when the arm was written. Measured on this tree: `write|engine` 54 · `write|seed` 4 ·
  `SIDE|rendered` 4 · `ORDER|attributes` 9 · `ORDER|engine` 1 · `ORDER|hole` 5 ·
  `COVER|project-owned` 1 — and `ORDER|project-owned` 0, which is the arm that reds.
- **the receipt-side role filter**, above.
- **`cmd_apply` prints the skip fact twice** — upstream's `SKIPPED [role] dest <- kit: why` and this
  branch's `not landed [role] dest — why`. Two answers to one question, in the output of the verb
  built to end silent partial installs. Drop the second and re-key this branch's two `why` arms onto
  upstream's line, which already carries role, destination, kit and reason.
- **the `settings-merge` refusal arm reuses a target earlier applies left kits in**, so apply refuses
  for the pre-existing-kits reason instead of the merged-role one. The arm passes for `push-main` and
  reds for `settings-merge` on fixture order alone.

*Why this was not pushed through.* The tempting move is to read the four failing counts off the
measured output and write them into the arms. That is `fixture-passes-by-finding-nothing` performed
deliberately: the arm would then assert whatever the code does, and the receipt-schema question — the
one that actually matters — would be buried under a green bar. The resolution is preserved as a patch
so no reconcile work is lost, and the tree stands at a green `49e06d9`.

*Also unresolved, and not caused by this:* the renormalize refused with `the pinned population is not
clean relative to HEAD` naming two gov paths. That was measured against a mid-merge working tree, so
it is unusable as a verdict — the same discarded-gate-result trap this record already names once.
Re-measure against a clean tree before believing it either way.
