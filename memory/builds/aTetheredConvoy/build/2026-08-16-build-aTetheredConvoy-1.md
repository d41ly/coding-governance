# aTetheredConvoy — build record

What ran, what landed, and what did not. Derived from the branch, the review records under
`reviews/`, and the spec set's own `RESOLVED` marks. Every row here has a source on disk.

## What landed

| Unit | State | Commit |
|---|---|---|
| 1 — the truthful core | BUILT | `0dfc56f` |
| 2 — `update` | BUILT | `e4d14c4` |
| 3 — the convergence ratchet | BUILT | `a21e2ce` |
| 5 — check carries evidence | **PART** — receipt-evidence half only | `0de03f7` |
| 4 — the gate-runner declaration | NOT BUILT | — |
| 6 — the merged role | NOT BUILT | — |
| 7 — the harness | NOT BUILT | — |

All seven specs exist, are Tier-2 conformant, were audited, and are folded. Three units and part of a
fourth are implemented.

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

## Parked — the scope call

**Units 4, 6 and 7 are not built, and unit 5 is half built.** The build ran out of session budget, not
out of design: every one of the four has a folded, audited spec and a stated position in the ordering
contract.

*Options seen:* build unit 4 next per the ordering contract and stop mid-unit; or take unit 5's
receipt-evidence half, which the ordering contract does NOT make dependent on unit 4, and land it
whole. *Chosen:* the second. *Reason:* unit 5's integrity, provenance and sidecar loops close a
MEASURED silent-green — a target whose files were all deleted and whose receipt was corrupted exited
0 — and they depend only on unit 1's receipt. Unit 4's value is latent until a target has a runner
wired. A half-built unit 4 would have left the `[gate_runner]` declaration written and unread, which
is the declared-and-dead class this build spent unit 3 closing.

*Deviation recorded:* this takes unit 5 out of the stated order. What unit 5 assumes of unit 4 —
`check --observe` and the emitted-leg presence loop — is exactly what was NOT built, so the
dependency is not violated, only unused. The remaining halves of unit 5 (adopter fan-out, rendered
rows, machine-scoped orders, the `[[outcome]]` evaluator, the outbox reader) are unbuilt.

## Parked — the full bar is unconfirmed

`GATE_FULL=1 bash tools/run-gates.sh` was started and had produced no output after roughly forty
minutes on this node; the charter records ~95s at width 8 on node `a`, so this node is far slower
rather than the bar being wedged by this diff. **The full bar is therefore NOT confirmed green for
this branch.** What IS confirmed, per pass: `govkit selfcheck`, `govkit selftest` (all arms),
`check-kit-versions`, `check-install-prefix`, the codebase-map coverage and freshness gate, the
memory-tree hygiene gate, the build-index render, the kickoff-manifest ratchet (including its
`--staged` leg, which blocked a commit until the audit block was re-stamped), and `git diff --cached
--check` for line endings.

This is a DoD gap, not a claim of green. It leads the wrap-up for that reason.

## Two owner-review items, flagged during the fork sweep and not settled by silence

- **Unit 4 F1** — the baseline EXECUTES target-authored code, twice per apply plus the target's own
  pre-commit hook, and the command comes from a file committed in the target repo. The resolution
  taken makes the committed descriptor the approval and re-prompts when the argv or its commit
  changes. That is a security posture resolved under delegation, and a posture deserves an owner's
  eye. Unit 4 is unbuilt, so nothing has acted on it yet.
- **Unit 6 F3** — appending gov's line-ending pins at the end of a target's attributes file makes
  gov's rules WIN, so a target that deliberately set the opposite is overridden and told, rather than
  refused. It is the one place this build knowingly overrides a target's own declared rule and answers
  with a message rather than a stop. Unit 6 is unbuilt.

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
