# TOOL-aQuotedBrief-5 — build brief

**Serves:** journal TOOL-aQuotedBrief-5

node a · 2026-10-09 · handed to one unit agent by the orchestrator. The spec is the scope; this brief
adds only what the spec does not carry. Units 1 to 4 and the round 1 fold are built on this branch.

- **Read first, whole:** the spec `spec/2026-10-09-spec-TOOL-aQuotedBrief-5.md`, the round 1 review
  record's H2 section under `reviews/`, and `check_prompt_brief`, `check_brief_items` and
  `read_audit_ask_record` in `tools/unattended/unattended.sh`.
- **Write set.** Declare with `--dispatch` before writing: `tools/unattended/unattended.sh`,
  `tools/unattended/unattended.test.sh`, `memory/map/generated/symbols.json`, the spec, the build
  README, `memory/LIVE.md`, and the ledger at
  `memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-5-10-acceptance-ledger.md`.
- **The predicate.** `check_prompt_heading` reads stdin and matches `^## The prompt[[:space:]]*\r?$`,
  the anchor `read_audit_ask_record` already spells. `check_prompt_brief` skips a record the predicate
  rejects before its structural awk runs; the awk's own `seen["The prompt"]` stops deciding it.
  `read_audit_ask_record` is not edited.
- **Fixtures.** Unit 4 moved the cutoff onto the fixture's default branch through
  `write_default_conf`; new arms use it the same way.
- **Verification, fast and direct only.** Arms for AC1 and AC2 beside the existing ones, floors raised
  by what you add, observed by SLICING (temp script under `tools/unattended/` NOT named `*.test.sh`;
  deleted before commit; keep each slice under 600 s by splitting), each new arm seen RED against the
  pre-unit driver first. AC3 is `git diff 6473ae38 -- tools/unattended/unattended.sh` read for
  `read_audit_ask_record`. Also `python tools/memory-tree/check-arms.py --check`,
  `python tools/lexicon/lexicon.py`, `python tools/codebase-map/gen_map.py --write`,
  `python tools/check-spec-tokens.py`. No bar, no whole suite.
- **Commit** once, subject `build(aQuotedBrief): TOOL-aQuotedBrief-5 — <what>`, trailers
  `Pass: TOOL-aQuotedBrief-5` and the co-author line. Set the spec CLOSED in the same commit only when
  every AC was observed, and write the acceptance ledger: one `**Evidences:** TOOL-aQuotedBrief-5`
  line directly above the `- AC1 — …` lines, each answer carrying a backticked token that also appears
  in its criterion. Report the sha.
