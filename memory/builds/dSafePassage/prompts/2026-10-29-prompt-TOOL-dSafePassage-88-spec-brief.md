**Serves:** research TOOL-dSafePassage-88 TOOL-dSafePassage-89

# Brief: the two moved-prefix stops past the plants, and 86/87's untracked path tokens

## The prompt

> TOOL-dSafePassage-86 and -87's writer measured, with both units staged in a clone moved to `scripts/`, that the walk still stops twice past the plants (87 §4 "Past the plants, measured", and its §3 hands-off external edge). H1 of the round-2 closing review (id 13) is the `upgrade-walk` row of the foreign-prefix parity leg red at every moved prefix, so it stays open until both stops are closed. BUILD-METHOD M10 adopts them now, as one unit each. The spec-token check over 86 and 87 also names nine untracked path tokens.

## The brief

### Goal
Author TOOL-dSafePassage-88 and TOOL-dSafePassage-89, each closing one of the two stops, and clear the spec-token findings in 86 and 87. Each new spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, carries `**Derived:** TOOL-dSafePassage-1` with 87's measurement named in its §9, declares `consumes-from` on 87 (and 86 where it needs it), has one mechanism, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse, and its §8 reads `none` or only RESOLVED forks. Add each row to the README `roster:units` table. Verify every cited line at `b634d60e5` before citing it.

### Items
- **TOOL-dSafePassage-88: the moved kit descriptor checks out CRLF.** `.gitattributes:2` sets `* text=auto` and `:222` pins `tools/*/kit.toml text eol=lf` only; the walk's clone sets `core.autocrlf=false` and no `core.eol` (`tools/govkit/upgrade_walk.py:197`). So on Windows the moved `kit.toml` checks out CRLF and the `withdraw-one` gov plant's replace text no longer matches. Decide from the code and records whether the defect is the walk's clone setup or the shipped `.gitattributes` pin, and whether adopters at a moved prefix meet it too; say which and why.
- **TOOL-dSafePassage-89: `read_steps` refuses at a moved tip.** With an eol pin staged for measurement only, the walk stops at `upgrade_steps.Refusal: tools/govkit/registry.toml: no registry at <tip>` from `read_steps` over the clone tip (`tools/govkit/upgrade_walk.py:1095`, `tools/govkit/upgrade_steps.py:756-760`), exit 1. The cause was not diagnosed: diagnose it by reading the code and reproducing it in a scratch clone moved to `scripts/` with 86, 87 and 88's fixes staged, then spec the fix. If the cause turns out to be the same mechanism as 88's, say so and author one unit, refusing the other with its reason.
- **86 and 87's path tokens.** `python tools/check-spec-tokens.py` (with 86 and 87 read as live) names: in 86, `scripts/govkit/upgrade_walk.py` and `f"{rel}/govkit.py"'`; in 87, `tools/govkit/engine.py`, `tools/lib/x.sh`, `scripts/govkit/upgrade_walk.py` (twice), `scripts/hooks/kit.toml`, `scripts/memory-tree/README.md` (twice). Each is a backticked path not tracked by git. Reword each so the check no longer reads it as a path, keeping the meaning; bump each spec's rev and add a §9 line naming this brief. Point 87's §3 hands-off external edge at 88 and 89.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside this brief's items.

### Acceptance
Each stop is closed by exactly one unit's §2 scope, or refused with its reason. Every spec authored is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
