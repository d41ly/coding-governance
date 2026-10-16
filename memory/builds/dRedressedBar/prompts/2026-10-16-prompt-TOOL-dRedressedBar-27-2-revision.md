# Revision — dRedressedBar: TOOL-dRedressedBar-27, the builder's divergence (a spec write no builder may make)

**Serves:** research TOOL-dRedressedBar-27 TOOL-dRedressedBar-18

## The brief

### Goal
DIVERGENCE: spec 27 §4 "The six revision entries" gives the build pass five spec writes, as do S4, §3's second non-goal, §4 Files touched, AC4 and AC5. Each is one appended revision entry plus the status header's rev and date, in TOOL-aSparedSpawn-11 (rev-4), TOOL-aSparedSpawn-13 (rev-6), TOOL-aSparedSpawn-32 (rev-5), TOOL-aOrientedCast-22 (rev-2) and TOOL-dRedressedBar-18 (rev-9). The scratch-guard hook refused all five edits. .claude/roles.json lets only gov-spec-writer write a spec, and a gov-builder may move only the status and date cells of its own routed spec. The repo's precedent agrees: a records-fix revision to another spec is written by the unit's spec-writer pass (spec 18 rev-5 to rev-8, spec 9 rev-5 to rev-7).

What §4 would have to say: TOOL-dRedressedBar-27's spec-writer pass writes the five entries and header moves, and re-renders the three build READMEs' generated rows with gen_build_index.py --write, before the build pass. The build pass then writes only the eight ledgers, the re-collected returns record, the 37 foreign lines and this unit's own ledger. AC4's spec half and AC5's entry lookup would then grade the spec-writer commit.

Without those entries, the five U lines would cite revisions that do not exist, so I committed nothing. Every path this pass changed is restored, and the work is saved for the redispatch.

### Items
1. **TOOL-dRedressedBar-27 — revise to rev-2, and run `<w27>` in this same pass.** Restructure as the builder states above: the five revision entries and header moves (TOOL-aSparedSpawn-11 rev-4, -13 rev-6, -32 rev-5, TOOL-aOrientedCast-22 rev-2, TOOL-dRedressedBar-18 rev-9) are this unit's spec-writer pass `<w27>`, and you write them now, in this pass, with the exact text the builder saved under `HANDOFF.txt` in `memory/builds/dRedressedBar/build/2026-10-16-build-TOOL-dRedressedBar-27-1-set-aside-work.md`. Date each entry and header 2026-10-16. The main loop commits your spec-27 revision and the five entries together as `<w27>` and re-renders the three build READMEs' generated rows with `gen_build_index.py --write`. The build pass then writes only the eight ledgers, the re-collected returns record, the 37 foreign ledger lines and its own ledger, restoring them from that set-aside record and changing them only where this revision requires; AC4's spec half and AC5's entry lookup grade the `<w27>` commit.
2. **The builder's seven spec facts, each corrected:** (1) aSparedSpawn-8/AC11's template token is `skipped — <id> · <why>` as spec 8 spells it; (2) aSparedSpawn-4/AC12's literal is the wrapper at `989e9234b:tools/hooks/agent-cap.test.sh:72`; (3) aSparedSpawn-3/AC7's before-runner is `286b839a`; (4) aSparedSpawn-16/AC12's instrument base is `f53211e6c`, with the file spelled `age.${heldkeys[$i]}`; (5) AC5's `git grep -F` lookup is satisfied by the owning spec for the tokens the builder lists; (6) Files touched adds the generated records rows the eight new ledgers add to specs 2, 4, 5, 7, 9, 11, 18 and 20; (7) AC4's pinned date is 2026-10-16.

### Acceptance
`git diff` shows spec 27 at rev-2 and the five owning specs each with one appended revision entry and their header rev and date moved, nothing else. `bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 27 READY.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit beyond spec 27 and the five revision entries with their header moves. No status change; no index regeneration; no commit.
