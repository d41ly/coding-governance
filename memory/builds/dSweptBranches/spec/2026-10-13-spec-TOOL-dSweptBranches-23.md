# TOOL-dSweptBranches-23 — the adopter withdraws the old `/branch-reconcile` render, and `--check` reds while it stays

**Status:** OPEN · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 20

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Unit 19 moved the rendered skill from `.claude/skills/branch-reconcile/SKILL.md` to
`.claude/skills/cleanup/SKILL.md`. Its spec said `govkit update` moves an adopter's copy, and that is
false. govkit's rename path keys on the descriptor row's SOURCE, and `SKILL.template.md` did not
move, so an updating adopter keeps the old render beside the new one (closing review round 1, H1 and
M1, ids 1, 6 and 10). Two skills then answer the same asks, and no check reads the old one. This
unit makes the kit's own adopter withdraw it.

## 2. Scope (IN)

- **S1** — `adopt-branch-reconcile.sh --scaffold` removes the skills directory's
  branch-reconcile/SKILL.md when its front matter reads `name: branch-reconcile` and it names the CLI
  `branch_reconcile.py`, then removes that directory if it is left empty. A file at that path that
  fails either test is not removed: it is named as a leftover the operator must remove, and the
  scaffold exits 1.
  **Readers:**
  by name: `tools/branch-reconcile/README.md` and `WIRE-INTO-PROJECT.md`, which describe the adopter.
  by value: NO VALUE READERS — the harness lists whatever skills exist, and nothing in this tree
  counts them.
  Observed by AC1 and AC2.
- **S2** — `adopt-branch-reconcile.sh --check` exits 1 while the old render exists, naming it and the
  `--scaffold` that withdraws it.
  **Readers:**
  by name: the `cleanup skill wiring` leg, which runs `--check`.
  by value: NO VALUE READERS — the leg reads only the exit status.
  Observed by AC3.
- **S3** — `WIRE-INTO-PROJECT.md` section 3g states the vintage step for an adopter that installed
  the kit before the rename: run `--scaffold`, commit the removal, and delete the manifest's
  `branch-reconcile skill wiring` leg row, which `cleanup skill wiring` replaces.
  **Readers:**
  by name: an adopter's run-gates manifest, which carries the old leg row by name.
  by value: NO VALUE READERS — both rows run the same `--check` argv, and nothing counts them.
  Observed by AC4.

## 3. Non-goals (OUT)

- No change to govkit's rename path. Whether a rendered row whose destination moved while its source
  stayed put should be withdrawn by govkit is a deployer question for its own build; this unit fixes
  the one kit that did it.
- No `git rm`: the scaffold removes the file, and the adopter's commit records the removal, as it
  records the new render.
- Spec 19 is CLOSED and keeps its text; its false claim is recorded as an erratum in its revision log
  and corrected here.

### Edges

- **consumes-from** `TOOL-dSweptBranches-19` — the rename this unit completes.

## 4. Design

Both modes run one function, `check_old_render`, after the fresh render is checked. It reads the old
path's front matter with `sed`, never sourcing it. `--scaffold` removes a recognised old render and
then `rmdir`s its directory, ignoring a non-empty one; `--check` only reports. A recognised render
is the kit's own output: the front matter carries the name, and the body names the CLI by its
rendered path. An unrecognised file is someone's work, so it is reported and kept.

The new arm builds a fixture repository holding the kit's three shipped files under a non-default
prefix, renders, plants an old render, and runs both modes.

### Files touched (estimate)

- `tools/branch-reconcile/adopt-branch-reconcile.sh`
- `tools/branch-reconcile/selftest.py`
- `tools/branch-reconcile/README.md`
- `WIRE-INTO-PROJECT.md`
- `memory/builds/dSweptBranches/spec/2026-10-13-spec-TOOL-dSweptBranches-19.md`, the erratum

### Alternatives rejected

- A WIRE-INTO-PROJECT step alone, with no removal by the kit: an adopter who misses it keeps two
  skills forever, and no gate says so.
- Removing whatever sits at the old path: an adopter's own file there would be deleted unread.
- A govkit change that withdraws a moved rendered destination: it changes every kit's update
  contract to fix one kit, and it is a deployer build of its own.

## 5. Production-readiness checklist

- security — the removal is confined to one fixed repo-relative path under the repository the script
  derived, and only after both content tests pass.
- perf / scale — N/A.
- error / empty / loading states — an unrecognised file is named and kept, and the scaffold exits 1.
- observability — each mode prints the old path and what it did with it.
- risks — an adopter who hand-edited the old render keeps it, by S1's second clause.
- testing — AC1 to AC3 in the kit self-test.
- migration — the removal reaches adopters through `govkit update`, whose `[[regenerate]]` runs
  `--scaffold`.
- user docs — the kit README and the runbook.

## 6. Acceptance criteria

- **AC1** — When `test_scaffold_withdraws_the_old_render` runs `--scaffold` over a fixture holding a
  planted old render, the old file and its directory are gone and the cleanup render exists.
  Red when: `--scaffold` leaves the old render in place.
- **AC2** — When `test_scaffold_keeps_an_unrecognised_old_file` plants a file at the old path that
  does not carry `name: branch-reconcile`, `--scaffold` exits 1 naming it, and the file is unchanged.
  Red when: the removal skips the content test.
- **AC3** — When `test_check_reds_while_the_old_render_stays` runs `--check` over a fresh cleanup
  render with an old render beside it, it exits 1 naming the old path; with the old render removed,
  it exits 0.
  Red when: `--check` reads only the new path.
- **AC4** — When `grep -n "branch-reconcile skill wiring" WIRE-INTO-PROJECT.md` runs, it finds the
  vintage step in section 3g.
  Red when: the runbook does not name the old leg row.

## 7. Gates

`branch-reconcile selftest` · `cleanup skill wiring` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 · an old render planted beside a fresh one · none
New arm: `tools/branch-reconcile/selftest.py` · covers AC2 · a foreign file planted at the old path · none
New arm: `tools/branch-reconcile/selftest.py` · covers AC3 · an old render planted beside a fresh one · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · promoted at the follow-up's closing diff review, round 1 (H1, M1).

## 10. Reuse audit

`reuse_lookup.py "withdraw an old rendered file at a moved destination"` ranked only name-token
neighbours (`corpus_files`, `parse_file`, `hash_file`); no existing seam fits a withdrawal. The seam is the kit's own adopter, `tools/branch-reconcile/adopt-branch-reconcile.sh`, whose
`[[regenerate]]` row already makes `govkit update` run `--scaffold`. govkit's rename path,
`resolve_renamed` in `tools/govkit/govkit.py`, keys on the source and was read to confirm it cannot
serve.

Recall terms used: "how does govkit update move a rendered file whose destination changed" --terms
"govkit update rename rendered destination withdrawn receipt regenerate scaffold adopter stale render"
