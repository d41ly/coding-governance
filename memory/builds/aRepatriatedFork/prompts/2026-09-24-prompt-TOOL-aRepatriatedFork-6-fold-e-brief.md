# Fold brief E — closing review round 2, M1 and L1

**Serves:** journal TOOL-aRepatriatedFork-6

A FOLD pass under the aRepatriatedFork mandate: the converged closing review's MEDIUM and LOW items.

Items **M1** and **L1** of round 2 — the run-state readers and writer the round-1 L2 fold left
unscoped. Code: `tools/unattended/gate-guard.js`, `tools/unattended/check-brief-recorded.sh`,
`tools/unattended/lib-unattended.sh`, `tools/unattended/unattended.sh`,
`tools/unattended/check-unattended.sh` and their suites.

- M1: every remaining reader of a run fact is scoped to `## Run facts` exactly as `fact` is:
  gate-guard.js `readFact` (take run-lease.js's heading slice), `CLAIM_AWK`, `baseline_units`, and
  `dod_met`, which calls `fact` instead of grepping. The LF+CR refusal moves INTO `park()`, so every
  reason-carrying verb inherits it. Left-shift: a gate-guard arm on the `1a phase: LANDED` fixture that
  asserts the hook still DENIES, a `\r run-branch:` park row that asserts the binding does not move,
  and a check in `check-unattended.sh` that reds any `^<key>:`-shaped run-state read in the kit that
  does not route through `fact`, `fact_of` or the heading slice, observed RED on a staged unscoped
  read before it lands.
- L1: `set_fact` matches and replaces only inside `## Run facts`, and inserts under the heading when
  the section lacks the key even if the same key sits elsewhere. Left-shift: a suite arm with `base:`
  only above the heading, `--preflight`, then `fact base` non-empty.

## How to fold

The review converged at round 2, so these items are FOLDED and never re-reviewed: this pass is the
last word on them, which is why each fix owes an arm observed failing first. The record
`memory/builds/aRepatriatedFork/reviews/2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round2.md` states each item's location, defect, fix and left-shift; read the items named above
there, whole.

- Reproduce each item at HEAD first. A finding you cannot reproduce is reported back as such, with
  the command, and not "fixed".
- The left-shift arm is observed FAILING against HEAD's bytes, then passing. Suites are not run
  whole: run the new block as a slice (prologue plus the block, in a temp script you delete) or by
  importing the module and calling the one arm.
- Fold into the owning spec as a rev-N bump whose §9 line names "closing review round 2 <item>" and
  the section, scope id or acceptance id it moved; the status header stays CLOSED.
- Governance carriers (`AGENTS.md`, the charter template, `memory/guides/UNATTENDED-PROTOCOL.md`,
  `memory/guides/REVIEW-PROTOCOL.md`, `memory/HYGIENE.md`) are not edited.
- Before committing, all exit 0: `python tools/lexicon/lexicon.py`, `bash tools/check-install-prefix.sh`,
  `python3 tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills`.
  After committing, all exit 0: `python tools/govkit/govkit.py epoch --base f8fdd873`,
  `bash tools/check-kit-versions.sh`, `python tools/govkit/govkit.py selfcheck`,
  `python3 tools/memory-tree/check-arms.py --check`. A kit whose shipped bytes moved owes its version
  bump in every carrier.
- A staged watched file owes a `last-audit` re-stamp to HEAD and a `Manifest delta:` line.
- Commit subject: `<owning unit id>: closing review round 2 <items> — <what changed>`.

## What to return

Per item: reproduced or not, the fix, the arm and its observed red, the spec rev. Name every suite the
close must now run.
