**Serves:** research TOOL-dPavedRoad-2

# Brief: TOOL-dPavedRoad-2's four spec-token hits

## The prompt

> `python tools/check-spec-tokens.py`, run by the main loop over TOOL-dPavedRoad-2's spec with its status flipped to INPROGRESS for the run, prints 4 unwaived [path] hits on `memory/builds/dPavedRoad/spec/2026-11-10-spec-TOOL-dPavedRoad-2.md`, one per backticked fragment: `g=require('./tools/hooks/format-guard.js');`, `a=require('./tools/hooks/agent-cap.js');`, `json.load(open('tools/gate-legs.json',encoding='utf-8'))` and `print('{prefix}/hooks/agent-cap.js'`, each "not tracked by git ls-files". The checker reads a backticked token that embeds a repository path as a path.

## The brief

### Goal
Respell the four tokens in TOOL-dPavedRoad-2's spec so no backticked token embeds a repository path, keeping every criterion's meaning: move each command into a fenced block, or name the tracked file as its own backticked token beside an unbackticked description of the call. The spec stays at rev-1, since this corrects an unreviewed spec before any build.

### Items
- Each of the four backticked fragments the spec-token check reads as an untracked path, respelled: `g=require('./tools/hooks/format-guard.js');`, `a=require('./tools/hooks/agent-cap.js');`, `json.load(open('tools/gate-legs.json',encoding='utf-8'))` and `print('{prefix}/hooks/agent-cap.js'`.

### Acceptance
No backticked token in the spec embeds a repository path, and `bash tools/memory-tree/check-memory-hygiene.sh --staged`, over a copy of the index with only the spec staged through `GIT_INDEX_FILE`, names no finding in it other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals
No other change to the spec; no edit to any other spec; no commit, no stage into the real index.
