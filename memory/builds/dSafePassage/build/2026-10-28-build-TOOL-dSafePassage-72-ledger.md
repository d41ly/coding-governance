**Serves:** journal TOOL-dSafePassage-72

# TOOL-dSafePassage-72 — acceptance ledger

The unit as built, at spec rev-4. Product writes: `tools/govkit/upgrade_steps.py` (S1's
`derive_contained_rel`; S3 and S4's `check_contained`, the lexical half through the predicate and the
link walk through `test_path_linked`, its unreadable-name refusal its own; S5's `derive_image_path`
through `check_contained`; S6's held-branch test), `tools/govkit/govkit.py` (S2's
`demand_contained_dest` deciding through the predicate, its docstring rewritten, the unused `ntpath`
import dropped), `tools/govkit/selftest.py` (the `[dSP-72]` arm in `check_upgrade_steps`) and
`help/upgrade-steps.md` (S7's bullet). `memory/map/generated/symbols.json` regenerated.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11) over this worktree by the probe the spec names, run directly from the repository root;
AC4 and AC5 by the `[dSP-72]` arm's block, lifted out of `tools/govkit/selftest.py` and executed alone
by a scratch probe with a stub `check`, which printed 15 of 15 PASS and no stray file.

Owed at the close: the `New arm:` line's RED-first observation of the `[dSP-72]` checks in
`tools/govkit/selftest.py` (AC1 to AC5), and the §7 legs at the bar.

**Evidences:** TOOL-dSafePassage-72
- AC1 — `derive_contained_rel` — the spec's `python -c` probe printed `[] ['a/b', 'a/b', 'b']`.
- AC2 — `demand_contained_dest` — the spec's probe printed `True a/b`.
- AC3 — `check_contained` — the spec's probe printed `True True`: the climb, rooted and UNC forms refused `is not a path inside the target`, the NUL, `a?b` and `a|b` names `does not read as a path on this node`, by `check_contained`, `read_image_paths` and, for the climb, `write_from_before_image`; no file outside the targets.
- AC4 — the `[dSP-72]` arm's block — a `mklink /J` junction `lnk` to a sibling `outside/`: the down over `lnk/planted.txt` and the up naming `lnk/secret.txt` each refused naming `lnk` and `reparse point`, no image written; a dangling junction `gone` refused; `derive_image_path` on a target whose `.governance` is a junction refused naming `.governance`; the plain-directory control restored `plain/f.txt`; `outside/` held only its planted `secret.txt`.
- AC5 — the `[dSP-72]` arm's block — a held image listing `lnk/secret.txt` refused naming `lnk`, and the list `derive_after` appends to stayed empty.
- AC6 — `awk '/^## /{s=$0} /A before-image path outside the repository/{print s}' help/upgrade-steps.md` — printed `## Rolling back`.
- AC7 — `git grep -n -e "ntpath.isabs" -e "PurePosixPath(rel)" -- "tools/govkit/*.py"` — printed one line, `tools/govkit/upgrade_steps.py:1049`, inside `derive_contained_rel`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `b634d60e5` (batch d, `2026-10-29-prompt-TOOL-dSafePassage-72-close-arms-d-researcher.md`), each break staged alone and restored. The `New arm:` line of this unit was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `b634d60e5`. tools/govkit/selftest.py `check_upgrade_steps`, with `check_contained`'s body replaced by the base `83817478` form (`PurePosixPath`, no segment walk): `FAIL [dSP-72] AC3 '..\\ESCAPED.txt' is refused by check_contained and read_image_paths, 'is not a path inside the target'` and `FAIL [dSP-72] AC4 a down through a linked segment is refused naming it, writing nothing outside`, 12 `[dSP-72]` arms in all (AC3 x6, AC4 x5, AC5 x1). AC1 and AC2 hold, since they grade `derive_contained_rel` and `demand_contained_dest`, which the break leaves alone. GREEN restored: `FAILURES 0`, 81 `ok`.
