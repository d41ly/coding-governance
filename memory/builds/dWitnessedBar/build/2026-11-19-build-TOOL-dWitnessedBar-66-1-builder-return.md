**Serves:** journal TOOL-dWitnessedBar-66

# TOOL-dWitnessedBar-66 — builder return 1 (run `wf_525fb61c-14b`), committed e3cdc2201

## Why

Unit 66 is built as its spec (rev-3) says. The AC12 arm in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh now plants a CR on the second `sha` line, which is a key that `read_green_file` reads. The hook half grades `rec_sha`. The `read_tag_lines` half prints `repr` of both values. The spec's status header is CLOSED in the same pass commit.

## Summary

Built TOOL-dWitnessedBar-66 and committed it as one pass commit, e3cdc2201, on base 248058974. The commit carries the `Pass: TOOL-dWitnessedBar-66` trailer.

What the commit changes:
- **The arm (S1 to S4):** I edited the arm in place in `tools/run-gates/run-gates.gov.test.sh`.
  - The record's third line now ends in CR-LF, so it is `verdict GREEN CR` / `sha a×40` / `sha b×40 CR`.
  - The hook-half failure line names `rec_sha` and prints its value with each newline shown as `|` and each CR as `\r`. The CR is put in through a variable (`rgf_cr='\r'`), which renders the same on both bash versions I probed.
  - The `read_tag_lines` call prints `repr(r.get("verdict")), repr(r.get("sha"))`, and the check is now `'GREEN' '<b×40>'`.
  - The comment above the arm names `rec_sha`, the two staged breaks, and the WHAT THIS DOES NOT CHECK clause for Git for Windows gawk and bash `$(...)`.
  - No `a=$((a+1))` was added or removed. The file's code-line count, measured by `sh_hygiene.measure_code_lines`, stays 611, which matches its row in `memory/project/shell-role.txt`, so no widen was needed.
- **Records in the same commit:**
  - The spec status header moves from INPROGRESS to CLOSED; its date was already 2026-11-21.
  - New acceptance ledger: `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-66-1-acceptance-ledger.md`.
  - `RUN.md`, plus what `gen_build_index.py --write` rewrote: `memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README, and the generated records table in the spec. Every one of these paths was in the declared dispatch set.
  - No function was added, so the codebase map was not regenerated.

Checks that ran. These are probes of this unit's own code; no gate, suite or bar ran.
- `bash -n` on the suite passed.
- A scratch probe (`scratchpad/u66-probe.sh`) wrote S1's record with the arm's own `printf`. It cut `read_green_file` from the hook by the arm's awk range, sourced it, and ran the arm's compare and failure line against three hooks. It stands in for the `run-gates gov canary` leg's run of this arm.
  - **HEAD's `.githooks/pre-push`:** green, and `rec_sha` was 40 bytes (AC1). (DERIVED from the builder's probe)
  - **A copy whose `sha` read prints every match** (diff shows one `>` line): red at 81 bytes. The failure line named `rec_sha` and printed `a…a|b…b` (AC2, first break). (DERIVED from the builder's probe)
  - **A copy with the CR strip removed** (diff shows one `>` line): stayed green at 40 bytes on this Git for Windows node, as the spec's §4 Evidence and §8 F3 predict. (DERIVED from the builder's probe)
- The `read_tag_lines` call, run as written, printed `'GREEN' '<b×40>'` and the check held (AC3).
- The CR rendering was probed on a value ending in CR; it printed `\r`.
- The AC1 and AC3 greps name the failure line and the Python line.
- The bug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`) ran and I acted on it; nothing needed a fix.

Owed to the main loop at the close:
- **The arm's RED-first observation** for its `New arm:` line, staged by switching the `sha` read to print every match.
- **The legs §7 names:** `run-gates gov canary`, `pre-push self-test` and `memory hygiene`.
- **AC2's CR-strip half:** it can only go red on a node whose awk and bash `$(...)` keep the CR. Otherwise it waits for TOOL-dWitnessedBar-70 S3, after unit 69 S1 (§8 F3).

AC1's grep figure does not hold as written on this node. GNU grep 3.0 here reads in text mode, so plain `grep -c $'\r$'` over the record printed 0 at a prompt and 3 inside `$(...)`. `grep -c -U` printed 2, and a Python byte read confirmed two CR-LF pairs. The ledger and a `Decided:` trailer record this. The spec's command is unreliable on Windows, and its author may want to know.

No command timed out or was skipped. The working tree has two modified files that were already modified before this pass, `help/reference/drive.md` and `help/reference/units.md`. I left them out of the commit.
