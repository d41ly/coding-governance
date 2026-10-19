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
  `` `bash tools/run-gates/run-gates.sh` `` at line 84 and
  `` `bash tools/unattended/unattended.sh` `` at line 12. Red half: with the adopter, library and render of `8a0e0b59` in the fixture's kit,
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
- AC6 — `tools/renamed/tier2-review.js` — arm 14's positive check, the backticked `grep -qF` with
  that value, failed on the file reading `` `C:/x/tools/renamed/tier2-review.js` `` and passed on
  the one reading `` `tools/renamed/tier2-review.js` ``. Red half: the bare `grep -qF` of
  `8a0e0b59` passed both.
- AC7 — `resolve_cited_paths` at the root install, `repo/.git`, the kit at `repo/roles` and a
  sibling `workflows/` holding both cited harnesses: it returned `[]`, and
  `bash roles/adopt-roles.sh --scaffold` in `repo` exited 0 with the Skill naming
  `` `workflows/unattended-build.js` `` at line 45 and `` `workflows/tier2-review.js` `` at line 76.
  Red half: with the library's `except`
  narrowed to `LookupError`, the call raised `ValueError` naming the sibling's
  `workflows\unattended-build.js`, and the adopter exited 2 on
  `roles: the citation pass over roles/SKILL.template.md failed`.
- AC8 — `tools/lib/resolve_kit_dir.py` — section 2e's fixture with row 7 written by the suite's own
  program, its `path` the posix `C:/.../out/y.js`: the seven queries printed `p/k`, `p/k` and five
  `LookupError`. Red half: with `root in hit.parents` cut from a copy, the `y.js` query returned the
  `out` directory, whose `relative_to` raised out of the program.
- AC9 — `tools/check-wiring.test.sh` — the count printed 1; at `8a0e0b59` it reads 0.
- AC10 — `help/roles.md` — `grep -c 'check_roles.py'` printed 1; at `8a0e0b59` it reads 0.
- AC11 — `help/roles.md` and the other three files — the first count printed 0 over each, and
  `grep -c 'not counted as its kit'` printed 1 over each; at `8a0e0b59` they read 1 and 0 over each.
- AC12 — `help/roles.md` and `tools/roles/README.md` — the three counts printed 0, 0 and 2. At
  `8a0e0b59` they read 1, 0 and 1, not the 1, 1 and 1 the red half states: the README wraps the
  phrase as `citation the kit` and `resolver holds` on two lines, so its `grep -c` cannot read the
  old text either way. That term of AC12 has no red half on this file.
- AC13 — `git diff --quiet -- .claude/skills/build/SKILL.md .claude/roles.json` — after
  `bash tools/roles/adopt-roles.sh --scaffold` in this worktree, holding the bytes `<p1>` commits,
  which printed the render's unchanged line and exited 0, it exited 0. The red half, an absolute
  path, was not staged.
- AC14 — `memory/gotchas/two-answers-to-one-question.md` — `grep -c 'TOOL-dRenderedAnchor-3'`
  printed 2; at `8a0e0b59` it reads 0.
- AC15 — `tools/roles/adopt-roles.test.sh` — `grep -c '^FLOOR_ASSERTIONS='` printed 1, on
  `FLOOR_ASSERTIONS=49`: arm 14 gained one floored `check_arm`, arm 15 has three and arm 16 two.

## The close's observations

Run by the main loop at `052b43a24`, before the closing review. Each staged break was written by a
script into the one file it names, or into a scratch copy of the adopter passed as
`ROLES_ADOPTER`, the suite run, and the file restored by `git checkout`; the tree read clean after
the last one.

- `New arm:` arm 14, AC4 — RED with `TOOL_ROOT_CITE_RE` narrowed to `[A-Za-z.-]+`:
  `adopt-roles.test.sh` exited 1, `FAIL (1 of 61)`, on arm 14's first check alone.
- `New arm:` arm 14, AC6 — RED with `.relative_to(root)` dropped in `resolve_cited_paths`: exit 1
  on arm 14's first check, with arms 15 and 16 redding beside it on the same absolute paths.
- `New arm:` arm 14, AC5 — RED with a copy of the adopter applying the held lines through the
  unanchored bash loop of `8a0e0b59` and calling the four-argument `resolve_cited_paths`: exit 1,
  arm 14's extended-citation check failing beside its first check and arm 15's receipt row.
- `New arm:` arm 15 — RED with every citation resolved with `here` at the tool root:
  `FAIL (1 of 61)`, arm 15's decoy check.
- `New arm:` arm 16 — RED with `except LookupError` alone in `resolve_cited_paths`:
  `FAIL (2 of 61)`, both arm 16 checks.
- `New arm:` section 2e row 7 — RED with `root in hit.parents` cut from
  `tools/lib/resolve_kit_dir.py`: both section 2e checks failed, beside 70 inline-parity rows. The
  red reads as a traceback, not a mismatched row: row 7's answer is outside the fixture, so the
  section's program raises on `.relative_to` before it prints.
- `New arm:` the check-wiring remedy check — RED with the remedy tail dropped from the echo in
  `tools/check-wiring.sh`: `FAIL OC8 AC6 ...and the note ends with the remedy naming the adopter's --check`.
- GREEN, all restored: `adopt-roles.test.sh` `PASS (61 assertions)`, `resolve-python.test.sh`
  `PASS — resolve-python: 343 assertions held`, `check-wiring.test.sh` `253 passed, 0 failed`, each
  exit 0.

## The fix pass for the closing bar's own red

The bar at `b4b79004d` read `shell hygiene (a fork spent on builtin work)` red on this unit's suite
lines. `tools/lib/resolve-python.test.sh` measured 11 `var-pipe` sites against the registry's 8,
and `tools/roles/adopt-roles.test.sh` measured 8 that no row declares. The fix record is
`2026-10-19-prompt-TOOL-dRenderedAnchor-3-3-fix.md`. This pass converts those eleven sites to the
no-fork form and changes no other line of either suite. It does not touch
`memory/project/spawn-idiom-sites.txt`.

- Section 2e's row-count check now reads the rows with `mapfile -t rk_rows <<<"$rk_got"` and counts
  the non-empty ones in a `for` loop, which is what `grep -c .` counted. Its two messages join the
  rows with `${rk_got//$'\n'/ }` in place of `tr '\n' ' '`. A `while read` count over
  `<<<"$rk_got"` was tried first. The loop classifier of the leg
  `shell hygiene (a loop fed by a command substitution)` graded it a `loop-var-sub` site. That
  raised the suite's `<<<` count to 2 against its row of 1 in
  `memory/project/substitution-fed-loops.txt`. The `mapfile` line is the idiom that
  section 3a of the same suite already uses, and neither line is a loop fed by a here-string.
- Section 2f's `| tr -d '\r'` capture pipes a command's output, not a variable's, so the lint counts
  no site there. It is unchanged.
- The eight diagnostic lines of adopter arms 14 to 17 now print
  `printf '    %s\n' "${out//$'\n'/$'\n'    }"` in place of `printf '%s\n' "$out" | sed 's/^/    /'`.
  That is the indent form section 3a of `resolve-python.test.sh` already uses. Each line keeps its
  own guard, so no `check_arm` value moves.

Observed by probes. No leg or suite was run.

- The lint's own `scan_spawn_file`, imported from `tools/gate-lint/sh_hygiene.py`, ran over each
  file. `resolve-python.test.sh` read `path-subst` 4 and `var-pipe` 8, and `adopt-roles.test.sh`
  read no site. Both equal the registry's rows for each file. Before this pass they read 11 and 8
  `var-pipe`. Its `scan_file` over the same files read one `<<<` `loop-var-sub` site for
  `resolve-python.test.sh`, which equals its row, and none for `adopt-roles.test.sh`.
  `git diff a60b0c7dc` over both registries was empty.
- `probe_fix3.sh` in the session scratchpad ran each old form and its replacement over seven values.
  They were: empty, one row, section 2e's seven rows, a blank row between two, leading and trailing
  whitespace with a tab, a backslash and `%s`, a trailing newline, and a three-line traceback. It
  read 0 differences for the count, the join and the indent. The guarded indent printed nothing on
  `rc` 0, and printed both lines indented on `rc` 1. A copy that counted blank rows read 3
  differences, and a copy that indented by three spaces read 7, so the probe can read red.
- `bash -n` parsed both suites.

Owed to the close and not run here: `shell hygiene (a fork spent on builtin work)` green with the
registry unchanged, `shell hygiene (a loop fed by a command substitution)` green,
`adopt-roles.test.sh` `PASS (62 assertions)`, `resolve-python.test.sh` green, arms 14 to 17 and
sections 2e and 2f RED on their staged breaks, and then the full bar.

## The close's observations after the fix pass

Run by the main loop at `a73090d7c`. `shell hygiene (a fork spent on builtin work)` and
`shell hygiene (a loop fed by a command substitution)` each exited 0, and
`git diff --quiet a60b0c7dc HEAD -- memory/project/spawn-idiom-sites.txt memory/project/substitution-fed-loops.txt`
exited 0. Every arm whose lines the pass rewrote was observed RED again on its staged break:
arm 14 (narrowed regex, dropped `.relative_to`, the unanchored adopter copy), arm 15, arm 16,
arm 17 (`here = kit`), section 2e (role term, home term, and row 7's `root in hit.parents`) and the
check-wiring remedy check. GREEN restored: `adopt-roles.test.sh` `PASS (62 assertions)`,
`resolve-python.test.sh` `PASS — resolve-python: 343 assertions held`, `check-wiring.test.sh`
`253 passed, 0 failed`.
