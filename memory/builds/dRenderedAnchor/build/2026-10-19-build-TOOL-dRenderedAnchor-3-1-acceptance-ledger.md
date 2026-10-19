# TOOL-dRenderedAnchor-3 — acceptance ledger

**Serves:** journal TOOL-dRenderedAnchor-3

This is the build pass of the unit, built from spec rev-2 under F1's resolution, C4. `<p1>` is the
pass commit this ledger lands in. It adds `extract_workflow_harnesses` to `tools/roles/roles_lib.py`
and reads `derive_harness_paths` through it, gives `resolve_cited_paths` the workflow table and the
kit directory so only a table harness resolves from the tool root, has the adopter's citation pass
print the template substituted whole through `TOOL_ROOT_CITE_RE.sub`, rewrites adopter arm 14 over
the suite's own `tomllib` read with the L3 row, adds arms 15 and 16 and the floor of 49, adds
section 2e's row 7 and check-wiring's remedy-tail assertion, rewords the help page, the README, the
render's docstring and the feature map, adds the two gotcha entries, regenerates the gotchas index
and the codebase map's `symbols.json`, and moves the spec's status to CLOSED.

No merge bar, gate leg or self-test suite was run by this pass: not `adopt-roles.test.sh`, not
`resolve-python.test.sh`, not `check-wiring.test.sh` and not `render_agents.py --selftest`. The
section 7 legs and the RED-first observation of the seven `New arm:` lines are owed to the close.
Every criterion below was observed by a direct probe on this Windows host under Python 3.14.5 and
bash 5.3.9, each probe program saved under the session scratchpad: `ac1.py` in-process for AC1,
`probe_adopter.sh` for AC2, AC3 and AC5, `probe_ac7.sh` for AC7 and `probe_ac8.sh` for AC8, which
reads section 2e's python program out of the suite. Each adopter fixture was built as the suite's
`build_fixture` builds one, at a short `%TEMP%` path.

**Evidences:** TOOL-dRenderedAnchor-3
- AC1 — `resolve_cited_paths` — over the shipped template with the kit's table, in a fixture holding
  `.git`, `tools/roles/`, both cited harnesses under `tools/workflows/` and the two root files, it
  returned exactly `{{TOOL_ROOT}}workflows/unattended-build.js` and
  `{{TOOL_ROOT}}workflows/tier2-review.js`, each under `tools/workflows/`. Red half: the library
  of `8a0e0b59`, called with the tool root as it was, also returned `unattended/unattended.sh` and
  `run-gates/run-gates.sh`, the two root files.
- AC2 — `adopt-roles.sh --scaffold` — with the two root files written, rc 0, and the Skill held
  `` `bash tools/run-gates/run-gates.sh` `` at line 84 and `` `bash tools/unattended/unattended.sh` ``
  at line 12. Red half: with the adopter, library and render of `8a0e0b59` in the fixture's kit,
  rc 0 and the Skill held `` `bash run-gates/run-gates.sh` `` and
  `` `bash unattended/unattended.sh` ``.
- AC3 — `ci/run-gates.sh` — the same fixture with a receipt row whose `source` is
  `tools/run-gates/run-gates.sh` and whose `path` is `ci/run-gates.sh`, the file written: rc 0, the
  Skill held `` `bash ci/run-gates.sh` ``, and `derive_kit_paths` sourced from
  `tools/lib/render-doc.sh` over the same tree printed `{{TOOL_ROOT}}run-gates/run-gates.sh`, a tab
  and `ci/run-gates.sh`. Red half: with a copy of the library that lists no citation but a table
  harness, C1, the Skill held `` `bash tools/run-gates/run-gates.sh` ``.
- AC4 — arm 14's block — `grep -c 'TOOL_ROOT_CITE_RE\|import roles_lib\|roles_lib\.'` over the
  lines from its heading to arm 15's printed 0, and 4 over the block at `8a0e0b59`. The population
  program the block runs is the prologue's `HARNESS_PAIRS_READ`, shared by arms 14 to 16 and
  holding none of those terms either; over the kit's own `workflows.toml` and `SKILL.template.md` it
  printed `workflows/unattended-build.js` and `workflows/tier2-review.js`.
- AC5 — `tier2-review.jsx` — arm 14's fixture with both harnesses behind rendered rows under
  `tools/renamed/` and the line appended: rc 0, and the Skill held
  `` `tools/workflows/tier2-review.jsx` `` at line 102 and `` `tools/renamed/tier2-review.js` `` at
  line 76. Red half: the adopter of `8a0e0b59` wrote `` `tools/renamed/tier2-review.jsx` ``.
- AC6 — arm 14's positive check — `` grep -qF -- "\`${_a14[$_i]}\`" `` with the value
  `tools/renamed/tier2-review.js` failed on the file reading
  `` `C:/x/tools/renamed/tier2-review.js` `` and passed on the one reading
  `` `tools/renamed/tier2-review.js` ``. Red half: the bare `grep -qF` of `8a0e0b59` passed both.
- AC7 — the root install — `repo/.git`, the kit at `repo/roles` and a sibling `workflows/` holding
  both cited harnesses: `resolve_cited_paths` returned `[]`, and `bash roles/adopt-roles.sh
  --scaffold` in `repo` exited 0 with the Skill naming `` `workflows/unattended-build.js` `` at
  line 45 and `` `workflows/tier2-review.js` `` at line 76. Red half: with the library's `except`
  narrowed to `LookupError`, the call raised `ValueError` naming the sibling's
  `workflows\unattended-build.js`, and the adopter exited 2 on
  `roles: the citation pass over roles/SKILL.template.md failed`.
- AC8 — `tools/lib/resolve_kit_dir.py` — section 2e's fixture with row 7 written by the suite's own
  program, its `path` the posix `C:/.../out/y.js`: the seven queries printed `p/k`, `p/k` and five
  `LookupError`. Red half: with `root in hit.parents` cut from a copy, the `y.js` query returned the
  `out` directory, whose `relative_to` raised out of the program.
- AC9 — `tools/check-wiring.test.sh` — the count printed 1; at `8a0e0b59` it reads 0.
- AC10 — `help/roles.md` — `grep -c 'check_roles.py'` printed 1; at `8a0e0b59` it reads 0.
- AC11 — the four files — the first count printed 0 over each and `grep -c 'not counted as its
  kit'` printed 1 over each; at `8a0e0b59` they read 1 and 0 over each.
- AC12 — the three counts printed 0, 0 and 2. At `8a0e0b59` they read 1, 0 and 1, not the 1, 1 and
  1 the red half states: the README wraps the phrase as `citation the kit` and `resolver holds` on
  two lines, so its `grep -c` cannot read the old text either way. That term of AC12 has no red
  half on this file.
- AC13 — `git diff --quiet -- .claude/skills/build/SKILL.md .claude/roles.json` — after
  `bash tools/roles/adopt-roles.sh --scaffold` in this worktree, holding the bytes `<p1>` commits,
  which printed the render's unchanged line and exited 0, it exited 0. The red half, an absolute
  path, was not staged.
- AC14 — `memory/gotchas/two-answers-to-one-question.md` — `grep -c 'TOOL-dRenderedAnchor-3'`
  printed 2; at `8a0e0b59` it reads 0.
- AC15 — `tools/roles/adopt-roles.test.sh` — `grep -c '^FLOOR_ASSERTIONS='` printed 1, on
  `FLOOR_ASSERTIONS=49`: arm 14 gained one floored `check_arm`, arm 15 has three and arm 16 two.
