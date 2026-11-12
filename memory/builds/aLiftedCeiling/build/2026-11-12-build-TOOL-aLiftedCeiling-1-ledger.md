# TOOL-aLiftedCeiling-1 — acceptance ledger

**Serves:** journal TOOL-aLiftedCeiling-1

Each line is a probe the builder ran over the pass's working tree at rev-1 of the spec. No leg, suite or bar ran in the pass.
Where a line says "owed", the main loop observes it after every unit is terminal.

**The race and the evidence row are the main loop's.** The spec's Design has the builder race the two tag-index checks in a
scratch clone and write the leg's evidence row there with `derive-ceilings.py --write --observed`. The role hook refused the
race in this pass, naming `gov_tag.py check` as the tags leg, which a role agent may not run (PINNED, the hook's refusal in this
pass). The row's seconds are the race's wall, so the row cannot be written before the race. The pass therefore leaves
`tools/run-gates/ceiling-evidence.txt` unchanged, and the main loop runs both steps of the Design's evidence-row section as
written, copying the generated file back under a `Pass: none` commit. Until then the leg has no row and the ceiling check reports
it unbacked, so no check grades the new ceiling.

**Evidences:** TOOL-aLiftedCeiling-1
- AC1 — `[420]` — the spec's `python -c` probe over `tools/gate-legs.json` printed `[420]`, one value for the leg's name (PINNED, the pass's diff).
- AC2 — `ie rc=0` — owed: the race of `gov_tag.py check` against `instructions_edit.py check` on a fresh index in a scratch clone is the main loop's, because the role hook refuses a leg in this pass.
- AC3 — `ceiling-evidence.txt` — owed: the row is written by `--write --observed` from AC2's wall, in the scratch clone, after the race.
- AC4 — `git diff --numstat` — owed: it reads the copied-back evidence file, which the pass leaves unchanged.
- AC5 — `derive-ceilings.py --check` — owed: it grades the leg only once AC3's row is in place.
- AC6 — `stamped` — the spec's `git merge-base --is-ancestor` probe over the pass commit, which changes both the leg's ceiling and the manifest's `last-audit` value, is run once the commit exists and its output is in the builder's return.

**Owed to the close.** Every leg of the spec's Gates section, AC2's race, AC3's row and its copy into this worktree, then AC4
and AC5 over that row. The spec declares no `New arm:` line.
