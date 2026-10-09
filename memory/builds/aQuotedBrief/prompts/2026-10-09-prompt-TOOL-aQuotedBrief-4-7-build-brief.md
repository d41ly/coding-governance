# TOOL-aQuotedBrief-4 — build brief

**Serves:** journal TOOL-aQuotedBrief-4

node a · 2026-10-09 · handed to one unit agent by the orchestrator. The spec is the scope; this brief
adds only what the spec does not carry. Units 1 to 3 and the round 1 fold are built on this branch.

- **Read first, whole:** the spec `spec/2026-10-09-spec-TOOL-aQuotedBrief-4.md`, the round 1 review
  record's H1 and M1 sections under `reviews/`, `check_prompt_brief` and `check_brief_items` in
  `tools/unattended/unattended.sh`, and the `SPEC_AUDIT_DEFAULT` read inside `check_authorization`
  (the `_cb` merge-base and the blank-first, sentinel-evaluated subshell) — copy that idiom exactly,
  including its two newlines of glue and its comment's reasons, rather than re-deriving it.
- **Write set.** Declare with `--dispatch` before writing: `tools/unattended/unattended.sh`,
  `tools/unattended/unattended.test.sh`, `memory/map/generated/symbols.json`, the spec, the build
  README, `memory/LIVE.md`, and the ledger at
  `memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-4-8-acceptance-ledger.md`.
- **At close**, term 7 needs the anchor kind and the observed anchor tip to compute the default-branch
  side. Find what `--close` already has in scope (the `anchor-kind` and `base` run-state facts, and
  whatever `authorization-reachable` observes); do not add a second remote observation if one exists.
- **The fixtures.** Every prompt-record and term-7 arm that appends `PROMPT_BRIEF_CUTOFF` to the
  fixture conf on the run branch now has to put it where the reader looks. Find the smallest change
  that keeps each arm grading what it graded: for a run-branch fixture, the default branch of the
  fixture's origin. Re-observe every such arm in the slice afterwards.
- **Verification, fast and direct only.** New arms for AC1 to AC4 beside the existing ones, floors
  raised by what you add, observed by SLICING (prologue plus the blocks, in a temp script under
  `tools/unattended/` NOT named `*.test.sh`, which the gate guard blocks before VERIFYING; delete it
  before commit), each new arm seen RED against the pre-unit driver first. Also
  `python tools/memory-tree/check-arms.py --check`, `python tools/lexicon/lexicon.py`,
  `python tools/codebase-map/gen_map.py --write`, `python tools/check-spec-tokens.py`. No bar, no
  whole suite.
- **Commit** once, subject `build(aQuotedBrief): TOOL-aQuotedBrief-4 — <what>`, trailers
  `Pass: TOOL-aQuotedBrief-4` and the co-author line. Set the spec CLOSED in the same commit only when
  every AC was observed, and write the acceptance ledger: one `**Evidences:** TOOL-aQuotedBrief-4`
  line directly above the `- AC1 — …` lines, each answer carrying a backticked token that also appears
  in its criterion (hygiene check 23 joins on that). Report the sha.
