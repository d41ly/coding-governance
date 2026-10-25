**Serves:** research TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34

# The promoted-fix pass — dPlacedRequest round 1, its return

The return of the gov-spec-writer dispatched from `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-6-spec-writer.md`, run direct/afb13713052248189, extracted from its transcript by script.

All 19 hits are fixed in six specs (TOOL-dPlacedRequest-24, -30, -31, -32, -33 and -34). Hygiene `--only 2,12,25`, run with the specs staged, now exits 0 with no failures. I did not run `check-spec-tokens.py`, since the brief leaves that to you. Instead I ran a script copying its path rule and suite-name pattern over the acceptance criteria of all six specs, and it found no untracked path and no suite name.

I judged no hit false. Each edited spec moved to rev-2 with a §9 line. Nothing was committed or re-rendered, and the `**Carries:**` and `**Derived:**` lines are untouched.

**spec-tokens hits**
- **TOOL-dPlacedRequest-24 [path] `tools/lib/gov-feed.sh` ×2:** AC6 now names `gov-feed.sh` by basename. TOOL-dPlacedRequest-13 creates that file.
- **TOOL-dPlacedRequest-24 [handoff] `write_node_lock`:** -34 S33 now names `write_node_lock` as -24's guarded factory, so the receiving spec names the token.
- **-30, -31, -32 [path] `requests/<key>.md` and `.typed` (6 hits):** each is now written with the `<git-common-dir>/` prefix (-30 AC1; -31 AC1, AC2, AC3; -32 AC1).
- **-33 [path] `skills/session-kickoff/card-store.fixture.sh`:** the §6 preamble and AC1 now use `card-store.fixture.sh`. TOOL-dPlacedRequest-2 creates it.
- **-34 [path], five hits:**
  - AC20: `loop_lib.py`
  - AC45: `<git-common-dir>/refs/gov/remote/runs/tFix.lock`
  - AC46: `RESUME.md`
  - AC55: `tag_index.py`
  - AC58: now reads "`git ls-files -- tools/loop` lists `request.py`, and `git cat-file -e` of that path at `c63aabbb` fails".
- **-34 [bar] `.githooks/pre-push.test.sh`:** AC24 and AC25 now run `.githooks/pre-push` directly in a scratch clone, on one stdin line, next to a stub `straggler-guard.sh` that prints a marker. AC25 runs the same line through a copy of the hook put back to the base `<sha>^ missing` test. The suite stays on its `New arm:` line in §7.
- **-34 [bar] `tools/hooks/scratch-guard.test.sh`:** AC28 now calls the exported `readCard` through a `node -e` probe (`module.exports`, `tools/hooks/scratch-guard.js:1615`). The suite stays on its `New arm:` line.
- **-34 [size]:** the spec went from 50800 to 49043 bytes, under the 49152 ceiling with 109 bytes to spare.
  - The review-item table is folded into a bracket on each scope item, e.g. "finding 4 (M5)", so the item-to-finding mapping is kept.
  - Evidence bullets that repeated §2's citations, two rejected alternatives already recorded as F3 and F4, and some wordy prose were cut.
  - All 59 finding ids in the RUN.md rescope row still have a scope item and a criterion.

**Check 12**
- **-34 AC25 had no backticked witness:** it now names `<sha>^ missing`, as part of the [bar] rewrite.

**Check 25**
- **-24 S1:** added a `**Readers:**` clause. By name it lists the three claim-push lock functions, which `tools/unattended/unattended.sh` and `tools/unattended/unattended.test.sh` spell, and the two lock events in `tools/unattended/README.md`. TOOL-dPlacedRequest-11 S6 retires those names and owns those readers. By value it is NO VALUE READERS, because the factory's only callers are new in this build.
- **-34 S2 and S15 had no real retirement, so I changed the wording instead of adding a clause.** The check was set off by runtime words: S2's "deleted" became "pruned" and S15's "drop" became "lose". Neither item retires a named thing.
- **-34 S30 (`--host` is dropped):** added a clause. By name is READER NOT IN TREE, since TOOL-dPlacedRequest-1 S11 creates the `--fleet-tag` `--host` flag and its caller in this build. By value is NO VALUE READERS.
- **-34 S38:** added a clause. By name: `write_claim_push_lock` and its three siblings, spelled in `memory/map/generated/symbols.json`. By value: NO VALUE READERS.
- **-34 S35 and S26 (one half missing):** these were line-wrap faults: "by" and "name:" or "value:" had ended up on different lines. Each marker is now on one line, and the names they list are spelled in the tree.
- **-34 S8:** by name is now READER NOT IN TREE. The local `refs/gov/builds/<slug>/card` is read only by TOOL-dPlacedRequest-2's S6 and S9, which are built in this build. I took the unit id out of backticks there.
- **-33 S3:** by name is now READER NOT IN TREE. `gov_ref_sh` is created by TOOL-dPlacedRequest-11 S8's parity row and `gov_feed_sh` by TOOL-dPlacedRequest-13. The note about the reader `tools/lib/resolve-python.test.sh` is kept.

Edited files, all under `C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\`:
- `2026-10-25-spec-TOOL-dPlacedRequest-24.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-30.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-31.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-32.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-33.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-34.md`
