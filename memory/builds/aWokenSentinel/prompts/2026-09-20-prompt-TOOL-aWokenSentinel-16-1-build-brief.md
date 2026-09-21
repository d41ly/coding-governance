# Build brief — TOOL-aWokenSentinel-16

**Serves:** journal TOOL-aWokenSentinel-16

The pass this brief was handed to builds unit 16 of `aWokenSentinel`: `--landed`'s check 34 accepts the `--no-ff` landing the charter mandates: the marker's commit contains the witness and sits on the remote default branch. The spec-audit round
disposed by severity on 2026-09-20; every fold is in the spec's revision log, and the spec is the
design. Read it whole; where it and this brief disagree, the spec wins and this brief is wrong.

## What the pass builds

The spec is `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-16.md` and it is authoritative. This unit was PROMOTED by a spec-audit disposal to close confirmed findings; the review record its spec cites is the defect statement. You build exactly what section 4 designs and section 2 scopes; the files it names in section 2 are: `check-arms.py`. A template edit re-renders in the same commit; a new `fail` or `check` number is re-derived from the tree, never copied from the spec; a new gate leg also needs its `tools/gate-legs.json` row, its `PASS` line, its dossier claim and its subject pin where the spec says so.

## What binds every pass of this build (read before the spec)

- **NO merge bar, NO gate leg, NO `*.test.sh` suite, NO spec section-7 gate list runs inside this
  pass.** Those are `--close`'s, once. Every acceptance criterion in the spec has a pass half — a
  grep or ONE arm run alone by the form the spec gives — and a leg half marked `observed at
  --close`. You observe the pass half. Your ledger row for a leg half reads `observed at --close`,
  never OBSERVED by a pass that did not run it. A whole suite run inside a pass is the stall this
  kit's previous build existed to end.
- **Every shell call carries the Bash tool's `timeout` parameter**: 120000 ms by default, at most
  600000 ms for the git commit (its pre-commit hook runs a staged hygiene pass of two to four
  minutes) or a build command the change itself needs. A check, cleanup, probe or any command
  unrelated to writing code that exceeds its bound is SKIPPED, named in your `summary`, and never
  re-run or waited on. PRIMARY OBJECTIVE: code written and committed.
- **Every temporary file goes under the session scratchpad, spelled absolute:**
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-eloquent-pasteur-e7ecb5/2db85696-ae7f-456a-9d88-fffc3fe3482a/scratchpad`. Never `$TMPDIR` (EMPTY on this node — it resolves to the filesystem root),
  never `/tmp`, never `$TEMP`, never a bare `mktemp`, never any other path outside the repository.
  A frozen copy of a kit for a single-arm run goes there too; a fixture git repo goes under
  `%TEMP%/<short-name>` because the scratchpad path is long enough to break a clone on Windows.
- **Regrounding (M7):** at the start read `git log --oneline -5`, the run-state file
  `memory/builds/aWokenSentinel/RUN.md`, `memory/guides/BUILD-METHOD.md` whole, and the spec whole.
- **Declare, then build.** `bash tools/unattended/unattended.sh --dispatch aWokenSentinel --pass <id>
  --writes <path>` once per path BEFORE writing — the spec's section 2 and 4 name the list. Do NOT
  declare `memory/DECISIONS.md`, `memory/backlog/*`, `memory/project/readme-contract.txt`, or
  `memory/builds/aWokenSentinel/RUN.md` (the verb refuses shared records; a backlog row edit is still
  made, just not declared). Declare `memory/LIVE.md` and `memory/ledger` (generated indexes,
  without their generator). Give a many-path dispatch a 600000 ms timeout. Then record this brief:
  `bash tools/unattended/unattended.sh --brief aWokenSentinel --unit <id> --path <this file>`.
- **Templates and renders land in ONE commit.** An edit to `tools/unattended/*.template.md` is
  re-rendered with `bash tools/unattended/adopt-unattended.sh` (then `--check`); the renders are
  byte-compared by the kit gate.
- **Watched files owe a stamp.** If the commit touches `.unattended.conf` or
  `memory/guides/BUILD-METHOD.md`, re-stamp `last-audit:` in `memory/guides/SESSION-KICKOFF.md`
  (ISO datetime with offset ` @ ` the sha of `git merge-base origin/main HEAD`) in the same commit,
  and put `manifest-audit: delta none · watch-commits-since-stamp: <n>` in the commit message.
  The pre-commit ratchet refuses the commit otherwise.
- **No kit version bump.** The closing pass bumps unattended once, across every carrier
  `bash tools/check-kit-versions.sh` names.
- **A kit file names nothing outside itself by literal.** A hook derives its kit dir from
  `__dirname`; a script from `$0`; the install prefix of this repo is never spelled in a shipped
  file. The install-prefix gate grades every file under `tools/`.
- **New `fail <n>` branches in `tools/unattended/unattended.sh` need an ARM** in
  `tools/unattended/unattended.test.sh` asserting the literal text; observe it RED by running that
  arm alone with the suite's preamble sourced, never the suite whole. The driver's `fail`
  high-water was 51 and the kit gate's `check` high-water 48 at base; re-derive before numbering.
- **Every new verb or option gets its VERBS entry** in `tools/unattended/VERBS.template.md` with its
  render in the same commit; check 26 joins the declared set to that file both ways.
- **The acceptance ledger** is a tracked record at
  `memory/builds/aWokenSentinel/build/2026-09-20-build-<id>-1-acceptance-ledger.md`
  opening with `# <id> — acceptance ledger`, then `**Serves:** journal <id>`, then an
  `**Evidences:** <id>` block with one `- AC<k> — <command> — <what it printed>` line per
  criterion, OBSERVED or `observed at --close` or AMENDED (spec rev bump with its section 9 line).
- **Commit** with the unit id in the subject; in that same commit set the spec's status header to
  CLOSED (date moves, rev does not), run `python tools/memory-tree/gen_build_index.py --write`
  after staging, `git add -A memory`, and let the hook run. Then run
  `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names. Return
  `committed:false` with a `why` rather than a commit you cannot stand behind.
