**Serves:** research PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55

# Brief: the spec-token hits the build's DEFERRED specs carry, folded before their units dispatch

## The prompt

> dOrderedCharter

— owner, 2026-11-02, invoking `/unattended` for the build run. Unit 19's fourth `--dispatch` (run wf_4f067f67-62a)
was refused by the spec-token check once its spec turned INPROGRESS: `[bar] python tools/codebase-map/selftest.py — a
bar or suite is not an acceptance observation`. The check grades only live specs, so every DEFERRED spec of this
build can carry a hit that surfaces only at its own dispatch. The main loop ran `tools/check-spec-tokens.py` with
DEFERRED read as live over the tree at `20cb62fa3`; this brief folds the hits that reading names in this build.

## The brief

### Goal

Fold every spec-token hit of a DEFERRED spec of this build that the unit's own build would not cure, so no unit's
dispatch is refused on a spec defect.

### Items

1. **Spec 19.** AC17 observes `derive_baseline_additions` by a probe of the moved function (for example, called in a
   scratch repository with a seeded baseline, checking the clean, added-key, no-baseline and bad-TOML answers), never
   by `python tools/codebase-map/selftest.py`, which stays on §7's `New arm:` line. AC10's run of
   `test_codebase_map.py` in a scratch copy is a suite run too: observe it by a probe or move it to §7. §4 Files touched
   adds `.lexicon.conf` (the verb pin moves, because the canonical and its copy each count), `tools/govkit/usage.toml`
   and `memory/project/docs-undocumented.txt` (the docs leg's rows for `help/tags.md`).
2. **The `policy fixtures` leg (35 specs).** Each spec below names in §4 Files touched a path the `policy fixtures`
   leg's guard covers, and its §7 leg line does not name the leg. Add `policy fixtures` to that leg line: specs 1, 2,
   3, 5, 7, 10, 11, 12, 13, 15, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39, 41, 43, 46, 49,
   50 and 55, plus 37 and 42 below.
3. **Spec 37** adds `recall floor` too (its Files touched names `memory/project/docs-undocumented.txt`); **spec 42**
   adds `playbook render selftest` (it names `tools/memory-tree/tree_lib.py`).
4. **Stale citations.** Spec 48 cites `tools/hooks/agent-cap.js:2414` twice, and the file has 2008 lines; spec 55 cites
   `tools/memory-tree/merge-rows.py:1538`, and the file has 1524 lines. Re-point each to the line that now carries what
   the spec means, found by reading the file at HEAD.

The `[path]` hits on files a unit creates (specs 11, 15, 19, 26, 31, 32) and on `HEAD:.governance/policy.toml` (specs
2, 3) are out of this brief.

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-03, the status kept `DEFERRED`, and add one §9 line naming this brief
  and the hit it folds. Change nothing else.
- The §7 leg line's spelling is the one the spec-token checker's guards join reads; match the leg names in
  `tools/gate-legs.json` byte for byte.
- Stay under the 47000-byte authored budget.

For the run:

- Writes stay in the specs named above and the files `gen_build_index.py --write` rewrites; a script under the
  scratchpad may make the mechanical item 2 edit, read back per file.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return the list of specs revised with each new rev, spec 19's AC17 and AC10 as they now read, and the two re-pointed
  citations.

### Acceptance

- `grep -c 'policy fixtures'` over each of the 35 specs' §7 prints at least 1.
- Spec 19's §6 names no `.test.sh`, `selftest.py` or `run-gates` runner.
- Each revised Status line is one rev higher, and §9 holds the new line.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no other edit of any spec; the `[path]` hits named above.

### Limitations

The items above, "For the run".

### Reuse

`tools/check-spec-tokens.py`'s guards join and its `BAR` pattern define what each item must satisfy.
