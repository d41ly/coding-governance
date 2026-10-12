**Serves:** journal TOOL-aOrientedCast-12 TOOL-aOrientedCast-14

# Fold handoff — two spec defects that stopped TOOL-aOrientedCast-12's dispatch

## Role

You are a software architect maintaining two unit specifications. You write no product code. You
change each spec only where this handoff names it, as a `rev-N` bump with its `§9` line. Leave every
other sentence alone. You may run only memory hygiene and the lexicon, and nothing else. You do not
stage, commit or regenerate any index. Return only what the return contract asks for.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

1. **`memory/builds/aOrientedCast/spec/2026-10-12-spec-TOOL-aOrientedCast-14.md`, line 201.**
   `--dispatch` check 49 refuses every pass while the spec-token checker reds over the live tree, and
   this spec's backticked `node -r ./p.js <script> --selftest` reads to that checker as a path git does
   not track: "`./p.js` — not tracked by git ls-files". Respell the token so it names no untracked
   path. Read `tools/check-spec-tokens.py` to learn what it treats as a path, without running it: it
   is a gate. Keep the sentence's meaning.
2. **`memory/builds/aOrientedCast/spec/2026-10-12-spec-TOOL-aOrientedCast-12.md`.** Its change moves
   `tools/run-gates/run-selftests.sh`, which the run-gates kit ships as an engine file, so the kit's
   version (1.35, in `tools/run-gates/run-gates.sh` near line 32 and `tools/run-gates/README.md`
   line 3) is owed one bump. This is the last unit of the build editing `tools/run-gates/`. Its §3
   forbids a bump. Amend §3, and add the two carriers to its files touched and an acceptance line
   naming the bump. The main loop observes `bash tools/check-kit-versions.sh` and the kit epoch
   check at the close.

**Return:**
- `folded`: each spec's new rev and what moved;
- the memory hygiene exit status, if you ran it.

**Addendum, after the first fold.**

3. **The same spec, `2026-10-12-spec-TOOL-aOrientedCast-12.md`, its new AC4.** The spec-token
   checker refuses it: "`run-gates.sh` — a bar or suite is not an acceptance observation". AC4 names
   that file as a version CARRIER, but a backticked `run-gates.sh` in `§6` reads as running the bar.
   Respell the criterion so it names the carrier without that token: by the version constant it
   holds, `KIT_RUN_GATES_VERSION`, or as a path the checker's bar pattern does not match. Read
   `tools/check-spec-tokens.py` to learn the pattern, without running it. Bump the spec's rev with
   its revision-log line.
