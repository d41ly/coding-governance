# TOOL-aQuotedBrief-3 — build brief

**Serves:** journal TOOL-aQuotedBrief-3

node a · 2026-10-09 · handed to one unit agent by the orchestrator. The spec is the scope; this brief
adds only what the spec does not carry. Units 1 and 2 are built on this branch (tip `170bb25d2`).

- **Read first, whole:** the spec `spec/2026-10-09-spec-TOOL-aQuotedBrief-3.md`, unit 1's
  `check_prompt_brief` (it already parses `### Items` and enforces numbered lines), the
  `build-complete` arm of `dod_met` in `tools/unattended/unattended.sh` with its six terms, and the
  `park()` and `--rescope` writers for the run-state line shapes.
- **Write set.** Declare with `--dispatch` before writing: `tools/unattended/unattended.sh`,
  `tools/unattended/unattended.test.sh`, `tools/unattended/VERBS.template.md`,
  `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-VERBS.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md`, `memory/map/generated/symbols.json`, the spec, the build
  README, and the ledger at `memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-3-6-acceptance-ledger.md`.
- **The preflight join** sits beside `check_prompt_brief` and is gated exactly as it is: prompt mode,
  a BASE, and the README `opened:` at or after `PROMPT_BRIEF_CUTOFF`. Reuse its record read rather than
  a second `git show`; extending `check_prompt_brief` itself is acceptable if that is the smaller diff,
  provided each join rule fails with its own message naming the rule and the item number LAST.
- **Term 7** goes after term 6 and returns early with its own `DOD_OUT`, like every other term. It
  reads the mode from the run-state fact `mode`, the record from the pinned BASE, statuses from the
  generated units region at HEAD, and supersede and park lines from the run-state file. A slug-mode
  run or a pre-cutoff README meets it silently.
- **The protocol is at 65688 of its 65692-byte cap.** The §4 `build-complete` sentence you add must be
  paid for by a trim of equal size elsewhere in the template, and `check-template-size` must pass.
- **Unit 2's fixture shim.** First preflights in the suite go through `run_main_at_head`; your arms use
  the ordinary helpers. Arms for term 7 drive `--close` over a fixture; find how existing
  `build-complete` arms stage one and copy that shape.
- **Renders** come from `bash tools/unattended/adopt-unattended.sh`; finish with its `--check` in sync.
- **Verification, fast and direct only.** Arms beside units 1 and 2, floors raised by what you add,
  observed by SLICING (prologue plus your block, temp script under `tools/unattended/`, deleted before
  commit), each seen RED against the pre-pass driver first. Also `python tools/memory-tree/check-arms.py`,
  `python tools/lexicon/lexicon.py`, `python tools/codebase-map/gen_map.py --write`,
  `python tools/check-spec-tokens.py` and `bash tools/check-template-size.sh`. No bar, no whole suite.
- **Commit** once, subject `build(aQuotedBrief): TOOL-aQuotedBrief-3 — <what>`, trailers
  `Pass: TOOL-aQuotedBrief-3` and the co-author line. Set the spec CLOSED in the same commit only when
  every AC was observed, and write the acceptance ledger: one `**Evidences:** TOOL-aQuotedBrief-3`
  line directly above the `- AC1 — …` lines, each with a backticked observation. Report the sha.
