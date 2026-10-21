# Phase 0 builder brief: the packet's file name claims the id its Serves line lists

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 244 renders from this brief record through `handoff.py render --role gov-builder`, with this
file as its `input:spec`. The opening, committed at `b50573ef4`, reds memory hygiene's check 21 on all 22 packets:
"record filenames whose family, slug and ordinal name an id their own Serves line does not list", for example
`memory/builds/dGroundRules/prompts/2026-10-21-prompt-TOOL-dGroundRules-1-packet.md — the name claims
TOOL-dGroundRules-1` (`tools/memory-tree/check-memory-hygiene.sh:1446-1478`). The packet serves
`PLAY-dClosedLoop-1`. Listing the first unit's id on the Serves line instead was tried in a scratch clone and reds
check 21's other arm: "TOOL-dGroundRules-1 is named but no spec H1 in this tree defines it", since no chain unit is
specced at the opening. So the name changes, and the plan's P0.3 name is raised with the owner at the opening read.

## The prompt

Write each packet as `memory/builds/<slug>/prompts/<date>-prompt-PLAY-dClosedLoop-1-packet.md`, so its name claims the
id its Serves line lists, and re-render the opening on the new name.

## The brief

### Goal

`build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py` writes and reads each packet under the new name, its docstring
and `build/2026-10-20-build-PLAY-dClosedLoop-1-open.py`'s docstring name it, and the opening is re-rendered: the 22
old packet files removed, the 22 new ones written, every view re-rendered, and memory hygiene's check 21 green on
the result.

### Items

1. The name in `packet.py` (its write path, `packet.py:542`, and whatever finds a build's packet, `packet.py:506`,
   which must find exactly the one packet per build) and both docstrings.
2. The re-rendered opening: `git rm` the 22 `*-prompt-<unit>-packet.md` files, `open.py --write`, `python
   tools/memory-tree/gen_build_index.py --write`, then stage every file it renders. `open.py --check` and `packet.py
   --check <slug>` for all 22 exit 0.
3. The packet plants (`--fixture` and every `--plant`) keep their verdicts, and `open.py`'s red tests still red.

### Acceptance

- `bash tools/memory-tree/check-memory-hygiene.sh` (the whole tree, no `--staged`) in your clone after the commit
  shows no check 21 finding naming a packet. Run it once, at the end, as the acceptance observation; it is the one
  gate this unit may run, because the finding is a gate's.
- `open.py --check` exit 0; `packet.py --check` exit 0 for all 22; `gen_build_index.py --check` exit 0.
- Append a `## The packet's file name` section to `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-packet-instruments.md`
  listing every command, in order, with its exit and the line that proves it.

### Gates

Only the whole-tree hygiene run named above, once. No other leg, suite or kit self-test. The naming lexicon before
naming a new function. The pre-commit hook fires on your commits; give each commit a 600000 ms timeout.

### Non-goals

- Your tree: a `git clone --shared` of `C:/projects/coding-governance/.claude/worktrees/unruffled-aryabhata-d89ede` at
  its branch `branch/unruffled-aryabhata-d89ede`, made under your scratch folder, with a linked worktree on a branch
  `p0-packet-name` for your commits and `core.hooksPath=.githooks` set in the clone. The main loop fetches that branch
  when you return; name its tip in your return.
- No file but `packet.py`, `open.py`'s docstring, the record above, and the opening's own files and renders as
  `open.py --write` and `gen_build_index.py --write` make them. No change to the execution plan (the main loop
  routes its P0.3 line), v2, the decision rows or any other record.
- No product code, no unit spec, no merge, no push, no rebase.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d244/` only; never delete anything outside it.
