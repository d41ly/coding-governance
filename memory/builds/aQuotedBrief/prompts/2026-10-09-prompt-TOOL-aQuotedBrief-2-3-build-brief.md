# TOOL-aQuotedBrief-2 — build brief

**Serves:** journal TOOL-aQuotedBrief-2

node a · 2026-10-09 · handed to one unit agent by the orchestrator. The spec is the scope; this brief
adds only what the spec does not carry. Unit 1 landed on this branch at `c3d7761af`; build on it.

- **Read first, whole:** the spec `spec/2026-10-09-spec-TOOL-aQuotedBrief-2.md` (rev-2, ratified),
  then `verb_preflight` in `tools/unattended/unattended.sh` from the rotation test to the write gate,
  `observe_anchor`, `default_branch`, `covers`, and unit 1's `check_prompt_brief` for the house style.
- **Write set.** Declare these with `--dispatch` before writing: `tools/unattended/unattended.sh`,
  `tools/unattended/unattended.test.sh`, `tools/unattended/VERBS.template.md`,
  `tools/unattended/SKILL.template.md`, `memory/guides/UNATTENDED-VERBS.md`,
  `.claude/skills/unattended/SKILL.md`, `memory/map/generated/symbols.json`, the spec, the build
  README, and the ledger at `memory/builds/aQuotedBrief/build/2026-10-09-build-TOOL-aQuotedBrief-2-4-acceptance-ledger.md`.
  Unit 1's pass was refused by check 49 until those last three were declared, so declare them now.
- **First preflight.** The check runs only when the run-state file `$rel` does not exist when
  preflight starts. Capture that BEFORE the rotation logic can create or move anything, and call
  `check_branch_carried` beside `check_prompt_brief`, before the write gate.
- **The predicate** is one `git log --format=%h --name-only HEAD --not <ASHA> [refs/heads/<default>]`.
  A path passes when it is under `$M/builds/<slug>/` or `covers` says an index in `GENERATED_INDEXES`
  covers it. Name the first offending commit and path LAST in the message, then print the recovery
  of spec §4. The header comment states what the check does not catch, per the charter's §7 rule.
- **The skill render is 7 bytes under its 10240-byte cap** after unit 1. Any line you add to
  `SKILL.template.md` must be paid for by a trim of equal size, and `check-template-size` must pass.
- **Renders** come from `bash tools/unattended/adopt-unattended.sh`, as unit 1 did; finish with its
  `--check` in sync.
- **Verification, fast and direct only.** Arms in `unattended.test.sh` beside unit 1's, the floors
  raised by what you add, observed by SLICING (prologue plus your block, temp script under
  `tools/unattended/`, deleted before commit), each seen RED against the pre-pass driver first.
  Also `python tools/memory-tree/check-arms.py`, `python tools/lexicon/lexicon.py`,
  `python tools/codebase-map/gen_map.py --write`, and `bash tools/check-template-size.sh`. Run no merge
  bar and no whole suite.
- **Commit** once, subject `build(aQuotedBrief): TOOL-aQuotedBrief-2 — <what>`, trailers
  `Pass: TOOL-aQuotedBrief-2` and the co-author line. In the same commit set the spec CLOSED only when
  every AC was observed, and write the acceptance ledger: one `**Evidences:** TOOL-aQuotedBrief-2`
  line directly above the `- AC1 — …` lines, each with a backticked observation. Report the sha.
