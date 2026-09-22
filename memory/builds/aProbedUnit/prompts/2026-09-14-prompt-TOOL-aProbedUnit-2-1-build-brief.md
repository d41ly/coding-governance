# Build brief — TOOL-aProbedUnit-2

**Serves:** journal TOOL-aProbedUnit-2

The pass this brief was handed to builds unit 2 of `aProbedUnit`: every command a unit runs is bounded. The two spec-audit
rounds converged at 0 blockers on 2026-09-14; every confirmed finding is folded, so the spec is
the design and the section 9 log says what moved.

## What the pass builds

The spec is `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-2.md` at rev-2 and it
is authoritative. Tier 1: the second paragraph in the child prompt of
`tools/workflows/unattended-unit.js` (unit 1 landed the first — read it at HEAD and place yours
after it), the Skill clause, and the harness suite arm. The child keeps exactly ONE top-level
definition (`check`); the oracle is `grep -cE '^(async )?function ' tools/workflows/unattended-unit.js`
stays 1.

## What binds every pass of this build (read before the spec)

- **NO merge bar, NO gate leg, NO `*.test.sh` suite, NO spec section-7 gate list runs inside this
  pass.** Those are `--close`'s, once. Every acceptance criterion in the spec has a pass half — a
  grep or ONE arm run alone by the form the spec gives — and a leg half marked `observed at
  --close`. You observe the pass half. Your ledger row for a leg half reads `observed at --close`,
  never OBSERVED by a pass that did not run it. (Build README, rule five; the round-1 audit's
  blocker.) A whole suite run inside a pass is the stall this build exists to end.
- **Every shell call carries the Bash tool's `timeout` parameter**: 120000 ms by default, at most
  600000 ms for the git commit (its pre-commit hook runs a staged hygiene pass of two to four
  minutes) or a build command the change itself needs. A check, cleanup, probe or any command
  unrelated to writing code that exceeds its bound is SKIPPED, named in your `summary`, and never
  re-run or waited on. PRIMARY OBJECTIVE: code written and committed.
- **Every temporary file goes under the session scratchpad, spelled absolute:**
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-build-stalls-6d0f2b/2dc0612b-7e56-48f3-a007-0d205b40b230/scratchpad`. Never `$TMPDIR` (EMPTY on this node — it resolves to the filesystem root),
  never `/tmp`, never `$TEMP`, never a bare `mktemp`, never any other path outside the repository.
  A frozen copy of a kit for a single-arm run goes there too.
- **Regrounding (M7):** at the start read `git log --oneline -5`, the run-state file
  `memory/builds/aProbedUnit/RUN.md`, `memory/guides/BUILD-METHOD.md` whole, and the spec whole.
- **Declare, then build.** `bash tools/unattended/unattended.sh --dispatch aProbedUnit --pass <id>
  --writes <path>` once per path BEFORE writing — the spec's Files touched is the list. Do NOT
  declare `memory/DECISIONS.md`, `memory/backlog/*`, `memory/project/readme-contract.txt`, or
  `memory/builds/aProbedUnit/RUN.md` (the verb refuses shared records). Declare `memory/LIVE.md`
  and `memory/ledger` (generated indexes, without their generator). Then record this brief:
  `bash tools/unattended/unattended.sh --brief aProbedUnit --unit <id> --path <this file>`.
- **Templates and renders land in ONE commit.** An edit to `tools/unattended/*.template.md` is
  re-rendered with `bash tools/unattended/adopt-unattended.sh` (then `--check`); an edit to
  `tools/workflows/unattended-build.template.js` with the review-harness parity gate's render mode
  (read `tools/workflows/kit.toml` `[[regenerate]]` for the argv); an edit to
  `tools/memory-tree/BUILD-METHOD.template.md` with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The renders are byte-compared.
- **Watched files owe a stamp.** If the commit touches `.unattended.conf` or
  `memory/guides/BUILD-METHOD.md`, re-stamp `last-audit:` in `memory/guides/SESSION-KICKOFF.md`
  (ISO datetime with offset ` @ ` the sha of `git merge-base origin/main HEAD`) in the same commit,
  and put `manifest-audit: delta none · watch-commits-since-stamp: <n>` in the commit message.
  The pre-commit ratchet refuses the commit otherwise.
- **No kit version bump.** The closing pass bumps unattended, memory-tree and agent-cap once.
- **New `fail <n>` branches in `tools/unattended/unattended.sh` need an ARM** in
  `tools/unattended/unattended.test.sh` asserting the literal text; observe it RED by running that
  arm alone with the suite's preamble sourced (the spec says how), never the suite whole.
- **The acceptance ledger** is a tracked record at
  `memory/builds/aProbedUnit/build/2026-09-14-build-TOOL-aProbedUnit-<n>-1-acceptance-ledger.md`
  opening with `# <id> — acceptance ledger`, then `**Serves:** journal <id>`, then an
  `**Evidences:** <id>` block with one `- AC<k> — <command> — <what it printed>` line per
  criterion, OBSERVED or `observed at --close` or AMENDED (spec rev bump with its section 9 line).
- **Commit** with the unit id in the subject; in that same commit set the spec's status header to
  CLOSED (date moves, rev does not), run `python tools/memory-tree/gen_build_index.py --write`
  after staging, `git add -A memory`, and let the hook run. Then run
  `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names. Return
  `committed:false` with a `why` rather than a commit you cannot stand behind.
