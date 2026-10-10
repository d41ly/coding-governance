# TOOL-aQuotedBrief-6 — build brief

**Serves:** journal TOOL-aQuotedBrief-6

node a · 2026-10-09 · handed to one unit agent by the orchestrator. The spec is the scope; this brief
adds only what the spec does not carry. Units 1 to 5 and the round 1 fold are built on this branch.

- **Read first, whole:** the spec `spec/2026-10-09-spec-TOOL-aQuotedBrief-6.md`, then the round 1
  review record's M2 to M6 and L1 to L4 sections and the round 2 record's one finding under
  `reviews/`; each names its file, line, sound fix and left-shift arm. Then the current
  `check_prompt_brief`, `read_brief_items`, `check_brief_items`, the call site in `verb_preflight`,
  and `park()`.
- **Write set.** Declare with `--dispatch` before writing: `tools/unattended/unattended.sh`,
  `tools/unattended/unattended.test.sh`, `tools/unattended/PROTOCOL.template.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md`, `.unattended.conf`, `memory/guides/SESSION-KICKOFF.md`
  (a `.unattended.conf` edit owes the kickoff manifest a `last-audit` re-stamp, as unit 1 found),
  `memory/map/generated/symbols.json`, the spec, the build README, `memory/LIVE.md`, and the ledger at
  `memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-6-12-acceptance-ledger.md`.
- **S2's date** is `PROMPT_BRIEF_CUTOFF="2026-10-10"`. Rewrite its conf comment to say a date must
  clear the `opened:` of every prompt-mode run in flight as well as of landed builds.
- **S7, the protocol row.** The protocol render is within a few bytes of its cap. Pay for the reworded
  `build-complete` clause with an equal trim elsewhere in the template; `bash tools/check-template-size.sh`
  must pass. Render with `bash tools/unattended/adopt-unattended.sh` and finish with its `--check` in sync.
- **S8's arms** are listed in the spec; the round records give each one's fixture. Unit 5 removed the
  `skip` sentinel, so the round 2 arm is a trailing build brief in the unit 3 join loop asserting the
  rule-3 refusal still fires. Unit 4 put the fixture cutoff on the default branch through
  `write_default_conf`; use it.
- **Verification, fast and direct only.** Floors raised by what you add. Observe by SLICING (temp
  scripts under `tools/unattended/` NOT named `*.test.sh`, each kept under 600 s by splitting, deleted
  before commit), each new arm seen RED against the pre-unit driver or, where that driver already
  passes, against a staged break. Then `python tools/memory-tree/check-arms.py --check`,
  `python tools/lexicon/lexicon.py`, `python tools/codebase-map/gen_map.py --write` after the slices
  are deleted, and `python tools/check-spec-tokens.py`. No bar, no whole suite.
- **Commit** once, subject `build(aQuotedBrief): TOOL-aQuotedBrief-6 — <what>`, trailers
  `Pass: TOOL-aQuotedBrief-6` and the co-author line. Set the spec CLOSED in the same commit only when
  every AC was observed, and write the acceptance ledger: one `**Evidences:** TOOL-aQuotedBrief-6`
  line directly above the `- AC1 — …` lines, each answer carrying a backticked token that also appears
  in its criterion. Report the sha.
