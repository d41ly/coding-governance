# TOOL-dDerivedDocket-51 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-51

An admitted example family for the kit's scratch fixtures: one `EXAMPLE_ROW` carrier, a default-OFF
keyword on `_fixture`, nine arms in the build-index selftest, and the staged RED that turns unit 15's
AC13 from an assertion about nothing into one about the generator.

The direct check for every line below is the FLAG form
`python3 tools/memory-tree/gen_build_index.py --selftest`, which AC4's and AC6's `permission:` lines
name as the check this pass may make; what those lines defer to the VERIFYING bar is the identical
argv's run as a HELD `chunk = selftests` LEG, not the criterion. No merge bar, no gate leg and no
`*.test.sh` suite ran in this pass.

Every one of the nine new arms has an observed RED, staged and unstaged by hand.
The §4 break — the `- EXMP-aFoo-3 — the ask` bullet in the fixture's README — redded the negative
anchor arm naming that id. Five further breaks covered the rest: defaulting `_fixture`'s keyword ON
(four arms red), writing the family half of the pair without the discipline half (two red), declaring
both halves in the halfway fixture (one red), emptying the break line of its id (the control, one
red), and emptying the line list the anchor scan walks (the liveness half of the negative arm).

**Evidences:** TOOL-dDerivedDocket-51
- AC1 — `EXAMPLE_ROW` — the arm splits the constant and looks for each half in the field the fixture
  wrote it into, reading the text back out of the written `.memory-tree.conf` with `parse_conf`
  rather than respelling the pair in the assertion. Observed RED under the break that writes the
  family half alone, where the discipline half is missing from `DISCIPLINES` and the arm names it.
- AC2 — `.memory-tree.conf` — two arms, both reading the file a real `_fixture` call wrote and not
  the renderer they share. The keyword-omitted fixture's conf is
  `MEMORY_ROOT=memory` / `DISCIPLINES="arch"` / `FAMILIES="arch:ARCH"`, byte-identical to the parent
  commit's, confirmed with `git show HEAD:tools/memory-tree/gen_build_index.py`; the opted-in one
  carries both halves. Both observed RED under the break that defaults the keyword ON.
- AC3 — amended rev-2 — `--check` — the criterion asserted `--check` exits 0 over the opted-in
  fixture, which is false for a README whose generated region has never been rendered: `--check`
  exits 1 on staleness, a verdict about the markers rather than about the declaration. It now names
  `--write` then `--check` and asserts both, and it no longer calls the writer "the scaffold arm",
  which is `TOOL-dDerivedDocket-15`'s at order 15 and does not exist at this commit. §9's rev-2 entry
  logs both, with the moved line citations. Observed as amended: the three arms are green — write=0
  check=0 over the opted-in fixture, `streams value 'example' is outside the DISCIPLINES enum` with
  the keyword omitted, `roster value 'EXMP' is outside the FAMILIES set` over the discipline half
  alone — each red under its own break.
- AC4 — amended rev-2 — `EXMP-aFoo-3` — the criterion said "every line the scaffold wrote" for the
  same reason AC3 did, and it gained the `new arm:` clause this build writes everywhere else, since
  S4 demanded that clause of unit 15's AC13 and this unit's own negative arm is the same
  could-not-fail shape. §9's rev-2 entry logs it. Observed as amended: the predicate resolved through
  `corpus_ids.resolve_anchor(root)` at the opted-in fixture's root returns `[]` over every line of
  the rendered README. Two REDs, because the arm asserts two things in one value: with the §4 break
  in that README it reds `anchored=['- EXMP-aFoo-3 — the ask'] carries-the-id=True`, and with the
  line list emptied it reds `anchored=[] carries-the-id=False` — the liveness half, without which an
  unrendered or unread README reports the same `[]` a clean one does, which is the
  `vacuous-selector-empty-population` class the diff checklist named. The control arm, which asserts
  the same predicate DOES answer the break line, stays armed, and a third arm asserts a fixture that
  never declared the family answers `None` for it.
- AC5 — `new arm:` — unit 15's spec at this commit carries the clause on AC13, naming the staged
  break and requiring the arm to have been seen RED over it, and its §9 carries a rev-7 entry whose
  scope names AC13. Its header moved rev-6 → rev-7 and stays SPECCED, because that unit is not built.
- AC6 — `arm(` — the whole suite reaches `PASS — gen_build_index: all arms held`, and the `arm(` call
  sites in the file count 216 at this commit against 207 at its parent, both derived at observation
  time with `git show HEAD:tools/memory-tree/gen_build_index.py | grep -o` over the same pattern. No
  count is pinned in the spec and none is pinned here beyond this reading.
- AC7 — `FAMILIES` — read out of this repository's `.memory-tree.conf` at this commit and at its
  parent with `parse_conf`, the value is the same four families and carries no example family. The
  anchor predicate resolved against this repository's own root answers `None` for the example-family
  bullet, heading and table-row spellings of an `EXMP`-family id, while the control bullet spelling the
  same slug and sequence in the `TOOL` family is
  answered — so the id corpus this repository grades did not grow.
- AC8 — `memory/map/generated/symbols.json` — `python tools/codebase-map/gen_map.py --write` re-derived
  all three artifacts and `git status --porcelain` reports none of them modified, so they are
  byte-identical to the parent's. That artifact carries no row for `EXAMPLE_ROW` and none for
  `_render_fixture_conf`: the extractor captures public module-level defs and classes plus statically
  listed `__all__` names only, this unit's carriers are a module constant and a private function, and
  no memory-tree module declares an `__all__`.
