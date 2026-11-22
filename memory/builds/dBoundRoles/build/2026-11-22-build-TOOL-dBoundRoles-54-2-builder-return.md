**Serves:** journal TOOL-dBoundRoles-54

# TOOL-dBoundRoles-54 — the second builder's return, a commit refused on the spec's mark

Run `wf_9f781b86-8b6`, started at `8a5cf9347` on rev-6. It built the pass and the pre-commit hook refused it, so it
committed nothing and kept the staged pass as `TOOL-dBoundRoles-54-pass.patch` in the session scratchpad; `diverged:
true`.

## The divergence, as returned

1. §8 F3's mark reads `RESOLVED (agent, 2026-11-22, delegated, M3)`. Memory hygiene check 12
   (`tools/memory-tree/check-memory-hygiene.sh#check_mark`) admits only `(owner|agent), <date>` with an optional
   `, delegated` inside the parentheses, so once the status reads `CLOSED` the hook refuses the pass commit on F3. The
   fix is `RESOLVED (agent, 2026-11-22, delegated): (a), ...` with `M3` after the parenthesis, as F1 and F2 spell it.
2. S3 spells the record's Departs from as one code span holding the bracket. `build_records.py read` reports that
   malformed: `tools/memory-tree/deviation_join.py#DEPARTS` admits the bracket only outside the backticks, as
   `` `TOOL-dBoundRoles-49@rev-5` [AC2] ``.
3. The built pass mints two helpers the Inventory does not name: `load_kit_roster`, the one roster loader S1 asks
   both derivations to call, and `derive_overlay_drift`, the two-way compare a probe observes. The lexicon accepted
   both.

The main loop found two positional reds in the spec at `8a5cf9347`: an unlisted `BUILD-METHOD M4` reference whose
tag cite is `doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`, and a stale
`BUILD-METHOD M2` row the register's shrink drops.

Every other claim held. The probe stood for AC1, AC2 and AC3 over fixtures and passed each.
