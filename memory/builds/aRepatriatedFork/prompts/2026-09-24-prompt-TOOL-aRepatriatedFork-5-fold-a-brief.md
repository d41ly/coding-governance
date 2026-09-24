# Fold brief A — closing review round 1, B1, H1 and M1

**Serves:** journal TOOL-aRepatriatedFork-5

A FOLD pass under the aRepatriatedFork mandate: the closing diff review's fixes folded in.

Items **B1**, **H1** and **M1** — the pre-push bar vetting and the hook-to-lander stub decision,
both inside the security model's first invariant. Code: `.githooks/pre-push`, `tools/push-main.sh`,
`.githooks/pre_push_bar_selftest.py`, `.githooks/pre-push.test.sh`, `.githooks/gate-env.sh`'s
reading. Specs: `TOOL-aRepatriatedFork-5` (B1, M1) and `TOOL-aRepatriatedFork-8` (H1, whose lander
this is).

- B1: the executed program is a tracked, clean path at word 1, or at word 2 after `bash`/`sh`, and
  nothing else sits between; run the vetted command with globbing off, as it was vetted.
- H1: ONE channel. The hook clears, then writes, a git-dir file beside `pre-push-refusal` holding
  the bar class it vetted plus the script path and blob; push-main writes the marker only when that
  file reads `default` or `tracked`. Vet `.githooks/gate-env.sh` as the bar is vetted: tracked at the
  pushed sha and clean, an ignored or excluded copy refused. Add the gotcha record the review asks
  for, under `memory/gotchas/`, for the class "a decision re-derived by a second process from a
  different input", in the shape the existing records there use.
- M1: `GOV_GATE_CMD` is accepted only when it equals the default runner or a value DECLARED in a
  tracked file read at the pushed sha; the vetted path and blob id ride the run-log END line and the
  lander marker.

## How to fold

The review record `memory/builds/aRepatriatedFork/reviews/2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md` states each item's location, defect, fix and left-shift. Read the
items named above there, whole, before touching code. For each item:

- Reproduce it at HEAD FIRST, then fix it. A finding you cannot reproduce is reported back as such in
  `summary`, with the command you ran, and not "fixed".
- Left-shift it as the record says: the new arm or row must be OBSERVED FAILING against HEAD's bytes
  before your fix, then passing after. An arm you only ever saw pass is an assertion about nothing.
- Fold into the owning spec as a rev-N bump whose §9 line names the review item (for example
  "closing review round 1 B1") and the section, scope id or acceptance id it moved.
- Suites and the merge bar are NOT run in this pass. A new arm inside a `*.test.sh` or selftest is
  run as a SLICE (the suite's prologue plus only the new block, in a temp script you delete), or by
  importing the module and calling the one arm function.
- Governance carriers (`AGENTS.md`, the charter template, `memory/guides/UNATTENDED-PROTOCOL.md`,
  `memory/guides/REVIEW-PROTOCOL.md`, `memory/HYGIENE.md`) are NOT edited by this pass: where a
  fix offers "vet it, or document it in the protocol", take the vetting.
- Before committing: `python tools/lexicon/lexicon.py` and `bash tools/check-install-prefix.sh`
  both exit 0. After committing: `python tools/govkit/govkit.py epoch --base f8fdd873`,
  `bash tools/check-kit-versions.sh` and `python tools/govkit/govkit.py selfcheck` all exit 0; a kit
  whose shipped bytes moved owes its version bump in every carrier, as a follow-up commit if needed.
- The pre-commit hook re-stamps nothing for you: a staged watched file (see `watch:` in
  `memory/guides/SESSION-KICKOFF.md`) owes a `last-audit` re-stamp to HEAD in the same commit and a
  `Manifest delta:` line in the message. `memory/map/generated/symbols.json` is regenerated with
  `python tools/codebase-map/gen_map.py --write` when a Python definition moves.
- Commit subject: `<owning unit id>: closing review round 1 <items> — <what changed>`.

## What to return

`summary` lists, per item: reproduced or not, the fix, the arm and its observed red, and the spec
rev. Name every suite the close must now run because an arm inside it changed.
