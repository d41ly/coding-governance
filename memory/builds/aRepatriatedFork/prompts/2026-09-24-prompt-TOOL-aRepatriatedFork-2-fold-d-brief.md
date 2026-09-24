# Fold brief D — closing review round 1, L3, L4 and residual b

**Serves:** journal TOOL-aRepatriatedFork-2

A FOLD pass under the aRepatriatedFork mandate: the closing diff review's fixes folded in.

Items **L3**, **L4** and residual **(b)** — three places a path or a value is resolved twice.
Code: `skills/session-kickoff/manifest-check.sh` and its test, `tools/memory-tree/adopt-memory-tree.sh`,
`tools/memory-tree/kit-dogfood-parity.test.sh`, `tools/hooks/agent-cap.js`,
`tools/workflows/check-verifier-fanout.sh`, `tools/workflows/check-protocol-parity.test.sh`. Specs:
`TOOL-aRepatriatedFork-2` (L3), `TOOL-aRepatriatedFork-10` (L4), `TOOL-aRepatriatedFork-7` (b).

- L3: manifest-check tries `resolve_kit_dir` anchored at the repo root after its own dir, and keeps
  the flat `memory-tree` probe as the last fallback.
- L4: both files resolve the sibling kit through the inline `resolve_kit_dir`; if a copy remains,
  it joins the `tools/lib/resolve-python.test.sh` byte-parity table.
- (b): the hook answers the effective cap itself (a print mode), and both shell readers ask it
  instead of parsing `.agent-cap.conf`.

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
