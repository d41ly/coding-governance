**Serves:** research TOOL-dSafePassage-104

# Brief: the three reds this build's own diff leaves on the landing merge 9f8812d80

## The prompt

> The close's bar on the prepared landing merge `9f8812d80` with its packet commit `ae1be0507` (log at `C:/Users/daily-agent/AppData/Local/Temp/dsp86-logs/close-ae1be0507.log`, 2810 s) reds four legs. Three trace to this build's own diff, and the fourth is the manifest ratchet's re-stamp. (1) Memory hygiene check 12: `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-103.md (§3 declares **consumes-from** `TOOL-dSafePassage-8` and that unit declares no matching **hands-off** `TOOL-dSafePassage-103` back)`, the class TOOL-dSafePassage-101 S1 answered for 99. (2) The lexicon naming predicates and lexicon wiring legs: `lexicon: verb offenders 1212 over pin 1211`. Main `2a6f39756` reads 0 and pins 1212; the branch pins 1211 after TOOL-dSafePassage-81's renames, and the merge keeps 1211. The one offender the merge adds that is not a moved name is `tools/policy/check_policy.py · verb · ask#2`: TOOL-dSafePassage-103's `run_census_source_receipt` defines a second nested `ask()` at `check_policy.py:4238`, a copy of `run_census_window_edge`'s at `:4206`, and `ask` is not in the declared VERBS table (`python tools/lexicon/lexicon.py --suggest ask --as py.function` calls it a scoping question). (3) The kickoff-manifest ratchet, which needs a post-merge re-stamp; that is the main loop's records commit, not this unit's.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-104, clearing (1) and (2) by their legs' own remedies, never by a raised pin. (1): TOOL-dSafePassage-103's §3 Edges reads `none` with a prose paragraph naming TOOL-dSafePassage-8 as read-and-closed, as TOOL-dSafePassage-101 S1 did for 99; 103 moves to rev-3 with a §9 line; the spec-writer pass that makes 104's spec makes that edit too, since it is the spec class. (2): the second `ask` stops being an offender, by reuse first (one wrapper both cases call, the charter's reuse rule at a kind's second instance) or else a name the lexicon declares, chosen by `lexicon.py --suggest`; the verb offender count returns to 1211 on the branch, so the merge reads the pin the branch carries. Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, `**Derived:** TOOL-dSafePassage-103` with this brief's finding in §9, §6 criteria each with a Red-when (the leg's own line above), §7 gates naming memory hygiene, the two lexicon legs and `policy fixtures` (the `census-source-receipt` and `census-window-edge` cases must still read 0 wrong), §10 reuse, §8 `none`, and §3 Edges with NO `consumes-from` onto a CLOSED sibling. Add its row to the README `roster:units` table. Verify every cited line at the current HEAD before citing it.

### Items
- **Id 1:** 103's §3 edge as prose, 103 at rev-3; AC: `bash tools/memory-tree/check-memory-hygiene.sh` prints no check 12 line for 103.
- **Id 2:** the second `ask` reused or renamed; AC: `python tools/lexicon/lexicon.py` exits 0 at the build commit, and `--offenders` lists no `ask#2`; `python tools/policy/check_policy.py --fixture census-source-receipt` and `--fixture census-window-edge` each read 0 wrong.

### Non-goals
No change to `.lexicon.conf` or any pin; no manifest stamp (the main loop's); no other spec than 103; no commit, no stage into the real index, no RUN.md row.

### Acceptance
Both items are carried in 104's text, and 103's rev-3 edit is made. Each spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path, a code fragment that embeds a repository path, or a regex-escaped path.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
