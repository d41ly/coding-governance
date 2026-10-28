**Serves:** research TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38

# Promoted fix returns — dIndexedDesign, round 1

The three unit-scoped spec writers' final returns, extracted from their transcripts by script, never retyped.

## agent a94dfea29ea24fa41

I fixed unit `TOOL-dIndexedDesign-31`, which is the only unit this handoff gave me. The hygiene run still exits 1, but its one failure is in unit 38, which is not mine. This unit's file is a rev-1 draft, so I edited it in place with no rev bump and no §9 line. I committed nothing and ran no index generator.

**Fixed: finding 1, unit 31.** In `/C:/projects/coding-governance/.claude/worktrees/unattended-dindexeddesign-516d37/memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-31.md`, I added four legs to the start of the §7 leg line: `verifier fan-out self-test`, `tier2-review self-test`, `unattended-build self-test` and `review-join self-test`. Each matches a leg name in `tools/gate-legs.json` exactly, and they come first in the same order as unit 5's §7 line. The line now reads:

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

**Left alone: findings 2 and 3**, which are in unit 37 (line 141's `tools/x.sh` example) and unit 38 (AC18 has no backticked witness). I didn't touch either file.

**Check run:** I ran `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` against a private copy of the git index with the edited unit-31 spec staged into it. The copy is at `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dindexeddesign-516d37/75965d52-bd39-4234-bbfb-fb440f651df7/scratchpad/index31`.
- Unit 31 is clean under checks 2, 12 and 25.
- The run exits 1 on one failure: check 12 on unit 38 AC18, which is finding 3 and still open until someone fixes that file.
- Check 25 printed only "did not grade … READER NOT IN TREE" notices, all from other specs, none from unit 31.

I didn't run `tools/check-spec-tokens.py`, because I'm only allowed the hygiene gate and the naming lexicon. The dispatcher should re-run it to confirm the guarded-legs finding is gone for unit 31.

## agent a78505590c5f3241d

I fixed both findings the brief raised against `TOOL-dIndexedDesign-37`, changing only `C:/projects/coding-governance/.claude/worktrees/unattended-dindexeddesign-516d37/memory/builds/dIndexedDesign/spec/2026-10-28-spec-TOOL-dIndexedDesign-37.md`. It is still an uncommitted rev-1 draft with no rev bump and no §9 line. Finding 3 is for `TOOL-dIndexedDesign-38`, which wasn't handed to me, so I didn't touch it.

**Finding 1 (missing leg in the §7 line):** fixed. I added `tier2-review self-test` to the §7 leg line, right after `build-index selftest`. The spelling matches `tools/gate-legs.json:737`, and that leg's guard lists `{prefix}/memory-tree/gen_build_index.py` (`:742-745`), which is the §4 file that triggers it.

**Finding 2 (an example path read as a citation):** fixed, but not with the brief's suggested spelling.
- **Why not `<dir>/<file>.sh`:** a token starting with `<` matches `NOT_A_TOKEN` (`tools/memory-tree/design_lib.py:525`). This unit's own S1 says such a token returns False, so AC1's "True for the first five" would no longer hold.
- **What I used instead:** a tracked nested file, `tools/memory-tree/design_lib.py`. AC1 now reads `.memory-tree.conf`, `README.md`, `.gitattributes`, `tools/memory-tree/design_lib.py`, `tools/x/`, `tools/`, `src/*.py` and `../x`, and still expects True for the first five and False for the last three.
- **Why the checker accepts it:** `check_path_shaped` (`tools/check-spec-tokens.py:1104-1121`) resolves it against `git ls-files`. Under S1 it is still a nested path with no empty, `.` or `..` segment, so it reads True as before.
- **The other examples need no change:** the checker never grades `tools/x/` (it ends in `/`), `src/*.py` (it's a glob) or `../x` (no dot in its last segment).

**Check:** `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`, run with `GIT_INDEX_FILE` pointing at a private copy of the index with the spec folder re-added, exited 0 and reported nothing for `TOOL-dIndexedDesign-37`. I didn't rerun `tools/check-spec-tokens.py`, since my role allows only the hygiene gate and the naming lexicon. Both fixes rest on reading the checker's code.

The index copy is at `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dindexeddesign-516d37/75965d52-bd39-4234-bbfb-fb440f651df7/scratchpad/index37` and the hygiene output at `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dindexeddesign-516d37/75965d52-bd39-4234-bbfb-fb440f651df7/scratchpad/hyg37.txt`.

## agent aab8a4e96e5eab9a9

I fixed finding 3 in unit 38's spec. Findings 1 and 2 are in the specs for units 31 and 37, which this handoff does not cover, so I left those files alone.

**TOOL-dIndexedDesign-38: authored (an in-place fix to the uncommitted rev-1 draft; no rev bump and no §9 line)**

- **Finding 3 (hygiene check 12, AC18 had no backticked witness):** fixed in `C:\projects\coding-governance\.claude\worktrees\unattended-dindexeddesign-516d37\memory\builds\dIndexedDesign\spec\2026-10-28-spec-TOOL-dIndexedDesign-38.md`, AC18 (now lines 392-396). The criterion now says how a pass runs each of the five readers S24 lists over the scratch spec:
  - `extract_open_questions`, `S10_RE` and `_SEC10` by `python -c`.
  - `plan_state` by the `sed -n` slice of `unattended.sh`, from `^plan_state()` to its closing brace.
  - `read_consumes_from` by sourcing `lib-unattended.sh`.

  The observation is the same as before: none reads the fenced heading, each reads the CR one, and "Red when: a twin differs." The `New arm:` line for `marker-contract.test.sh` is unchanged, so the suite stays there and the witness only probes the unit's own code.

  I checked each reader the probe names against current code: `plan_state()` at `tools/unattended/unattended.sh:4458`, `read_consumes_from()` at `tools/unattended/lib-unattended.sh:348`, `extract_open_questions` at `tools/runlog/model.py:1444`, `S10_RE` at `tools/memory-recall/check-recall.py:447` and `_SEC10` at `tools/codebase-map/replay-phrases.py:139`. The slice runs from the start line to the first closing brace, the way `tools/memory-tree/marker-contract.test.sh:281-284` cuts it. The probe forms match unit 9's AC11.

**Hygiene check:** I copied the git index to a private file in the scratch folder, staged the edited spec there, and ran `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` against it. It exited 0 with no finding on any dIndexedDesign spec. The only other output was check 25's "did not grade — READER NOT IN TREE" notices about other builds' specs. The real index is untouched. I did not commit or run the build-index generator.
