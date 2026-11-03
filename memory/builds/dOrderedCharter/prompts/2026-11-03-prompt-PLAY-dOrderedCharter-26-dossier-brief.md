**Serves:** research PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-50

# Brief: unit 26's second divergence — its new leg's dossier claim, which the commit hook owes in the same pass

## The prompt

> Try again

— owner, 2026-11-03, the run's last instruction. Unit 26's builder (run wf_8d835a4a-35d) built rev-6 whole and probed
it green, then the pre-commit hook refused the pass commit: the codebase-map gate
(`test_every_inventory_key_is_claimed_or_baselined`) reads `UNCLAIMED ... {'gate-legs': ['tags positional selftest']}`,
and the map's baseline is shrink-only. Spec 26 §2 S7 adds that leg, and §3 Edges hands its dossier claim to
PLAY-dOrderedCharter-50 S5 one order later, so no pass between them can commit. The built pass is saved as a scratch
patch.

## The brief

### Goal

Move the `tags positional selftest` leg's dossier claim into unit 26, so its pass commits, and make spec 50 agree.

### Items

1. **Spec 26.** S7 also writes the leg's claim in `memory/map/features/playbook.md` (§4 Files touched gains that path,
   and `memory/map/generated/*` the map generator rewrites); move the claim half of PLAY-dOrderedCharter-50's S5 and
   its AC4 here as an AC observed by a probe of the dossier (never the codebase-map gate itself); §3 Edges' hands-off
   line to unit 50 keeps the subject-pins and descriptor rows only.
2. **Spec 50.** Drop the dossier-claim half of S5 and of AC4 with a §9 line pointing at spec 26, keeping its id, its
   subject-pins and descriptor rows and every other item (BUILD-METHOD M4: a repair corrects an unbuilt sibling's
   spec). Fix the line near 127 that says builders between order 9 and order 10 "land red".

In every spec you revise:

- Bump the **Status:** rev by one, dated 2026-11-03, the status kept `DEFERRED`, and add one §9 line naming this brief.
- §7's leg line names every leg whose guard a Files-touched path trips.
- Verify every path, count and line you cite against the tree at HEAD; stay under the 47000-byte authored budget.

For the run:

- Writes stay in specs 26 and 50 and the files `gen_build_index.py --write` rewrites.
- Do not commit and run no check: the main loop re-renders the packet, runs the spec-token check, renders the index
  and commits.
- Scratch files go under the session scratchpad
  `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad`.
- Return each spec's new rev and the moved lines as they now read.

### Acceptance

- `grep -n 'memory/map/features/playbook.md'` prints spec 26's Files touched line.
- Spec 50's S5 and AC4 name no dossier claim for `tags positional selftest`.
- Each Status line is one rev higher, and §9 holds the new line.

### Gates

The spec-token check, run by the main loop before the commit.

### Non-goals

No code; no spec but 26 and 50.

### Limitations

The items above, "For the run".

### Reuse

The dossier claim shape other legs already carry in `memory/map/features/playbook.md` (units 16 and 28 wrote theirs).
