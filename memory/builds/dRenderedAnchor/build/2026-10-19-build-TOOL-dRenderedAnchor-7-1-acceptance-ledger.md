# TOOL-dRenderedAnchor-7 — acceptance ledger

**Serves:** journal TOOL-dRenderedAnchor-7

This is the build pass of the unit, built from spec rev-1 with §8 F1 resolved (b) by the owner.
`<p1>` is the pass commit this ledger lands in. It closes unit 6's closing-review items H1, M1, L1,
L2, L3 and L4. The canonical `derive_kit_paths` in `tools/lib/render-doc.sh` takes its kit
directory with `.absolute()`, and its four inline copies are re-synced. A fourth gated canonical,
`check_kit_cites`, is carried inline by the review-harness kit's parity script and by the unattended
adopter, each calling it right after its `KIT_PATHS` derivation. The parity script's re-run guard
reads the value 1 alone, and a suppressed re-run is a named exit 1. Its `FANOUT_CAP` block moves to
just after the citation check. The python resolver's suite gains the `check_kit_cites` parity row
and sections 2h and 2i. The build harness's suite gains `build_renamed`, `seed_unattended_kit` and
`write_python_stubs`, two RA6-1 sites and arms RA7-1 to RA7-4, with its floor raised 667 to 686.
Both kit READMEs state the refusal, and the workflows README states the re-run's exit, the
suppression line and what `--tracked-only` does. The codebase map's `symbols.json` and the build
index are regenerated, and the spec's status moves to CLOSED.

No merge bar, gate leg or self-test suite was run by this pass: not `resolve-python.test.sh`, not
`unattended-build.test.sh`, and not the parity script in check mode over gov's tree. The section 7
legs and the RED-first observation of the seven `New arm:` lines are owed to the close. Every
criterion below was observed on this Windows host under bash 5.3 by a direct probe saved under the
session scratchpad. `probe_ac1_ac3.sh` copies sections 2h and 2i into a fixture at `%TEMP%/ra7j`.
`probe_ra7.sh` copies the build harness's helpers, RA6-1, RA6-2 and RA7-1 to RA7-4 into fixtures at
`%TEMP%/ra7`. Each red half ran the same probe over a scratch copy of the kit directories, with the
shipped call, guard or line removed or reverted, never a value substituted. The build harness's
breaks sat in two copies. Copy A held the resolver lines made `|| :`, `exit $?` made `exit 0`, both
`check_kit_cites` calls taken out and the suppression branch taken out. Copy B held the guard
reverted to the `+set` test and the announcement taken out. Each arm's layout reaches only the break
named against it below.

## The correction unit 6's spec carries no longer

Unit 6's spec is CLOSED and frozen, so this ledger and spec 7's §4 carry the correction to its §4
paragraph on the second pass. That paragraph said `--tracked-only` creates nothing, so its two
derivations agree and it never re-runs. That is false. The `--tracked-only` skip fires only for a
live copy that is absent AND untracked, so a tracked harness deleted from the worktree is rendered
and written again. The first derivation could not see that harness, because the resolver keeps a
receipt row or a probe only when it is a file. The second derivation sees it, and the run re-runs
once, like a fresh render. The workflows README and the parity script's comment now say so.

**Evidences:** TOOL-dRenderedAnchor-7
- AC1 — `.gov/wf/t.js` — `ln -s` left no link on this host, so the probe made a directory junction
  with `cmd //c mklink //J`, and `[ -L ]` read true. The canonical, sourced, printed
  `{{TOOL_ROOT}}wf/t.js<TAB>.gov/wf/t.js`. Red half: over a copy with `.absolute()` reverted to
  `.resolve()`, it printed `{{TOOL_ROOT}}wf/t.js<TAB>tools/wf/t.js`.
- AC2 — the four `derive_kit_paths` diffs — each copy's block, CRs dropped, compared equal to the
  canonical's: `adopt-memory-tree.sh`, `kit-dogfood-parity.test.sh`, `adopt-unattended.sh` and the
  parity script. The red half is the parity row's, owed to the close.
- AC3 — `check_kit_cites` — the canonical, sourced, returned 0, 2 and 2. It printed nothing over the
  first input. It returned 2 over the second, with one line naming `{{TOOL_ROOT}}h/u.js` and `p/u';x;'/u.js`, and 2
  over the third, with one line naming `{{TOOL_ROOT}}h/v.js` and `p/q r/v.js`. Red halves: with the
  value case made to match nothing, all three returned 0. With the cite filter taken out, all three
  returned 2 on the bare line's `q r/`.
- AC4 — the two `check_kit_cites` diffs — the parity script's copy and the adopter's, CRs dropped,
  compared equal to the canonical's. The one-byte red half is the parity row's, owed to the close.
- AC5 — `q r/check-verifier-fanout.sh` — in RA7-3's layout, the parity script's render mode printed
  `protocol-parity: the citation {{TOOL_ROOT}}workflows/check-verifier-fanout.sh resolves to 'q r/check-verifier-fanout.sh'`
  and the rest of its refusal, at `rc=2`, and no protocol existed afterwards. The adopter then printed the line naming
  `{{TOOL_ROOT}}workflows/unattended-unit.js` and `'q r/unattended-unit.js'` and `rc=2`, and no
  Skill existed. Red half: with both calls taken out (copy A), the parity script exited 0 and wrote
  the protocol, and the adopter exited 0 and wrote the Skill.
- AC6 — `PROTOCOL_PARITY_REPASS` — with `PROTOCOL_PARITY_REPASS=1` exported, the render printed the
  suppression line and no `rendering once more` line, at `rc=1`. With `PROTOCOL_PARITY_REPASS=`
  exported over a second layout, it printed `rendering once more` exactly once, at `rc=0`. Red halves:
  with the suppression branch taken out (copy A), the first run printed no line at `rc=0`. With the
  guard reverted to the `+set` test (copy B), the second run took the suppression branch at `rc=1`,
  and no re-run ran.
- AC7 — `rendering once more` — over a fresh `build_renamed` layout, `grep -c` read 1 at `rc=0`.
  With the `repass` stubs first on PATH and `GOV_PYTHON` unset, the render printed the re-run line at
  `rc=2`. Red halves: with `exit $?` changed to `exit 0` (copy A), the second run read `rc=0`. With
  the announcement taken out (copy B), the count read 0, and RA7-1's line was missing.
- AC8 — `resolve_python: tried: python3 python py` — RA6's layout after RA6-2, with the `always` stubs
  first on PATH and `GOV_PYTHON` unset. `adopt-unattended.sh --check` and the parity script's check
  mode each printed that line last, at `rc=2`. Red half: with `|| exit 2` made `|| :` on each
  resolver line (copy A), both still exited 2, which is why the arm reads the last line. The adopter's last
  line was then `scripts/unattended/adopt-unattended.sh: line 384: : command not found`, and the
  parity script's was `protocol-parity: could not resolve the citations the templates make`.
- AC9 — the five counts — over `tools/workflows/README.md`, `never re-runs` read 0 and
  `PROTOCOL_PARITY_REPASS` read 3. `A-Za-z0-9._/+@-` read 1 over it and 1 over
  `tools/unattended/README.md`. Over the parity script, the old comment's phrase read 0. At
  `a99b3f23` the same five read 1, 1, 0, 0 and 1.
- AC10 — `git status --porcelain` — in this worktree, holding the bytes `<p1>` commits,
  `bash tools/workflows/check-protocol-parity.test.sh --render` printed its five `rendered` lines and
  no re-run line at rc 0. `bash tools/unattended/adopt-unattended.sh` exited 0. The status then named
  only this pass's own edited files, the same set as before the two runs. `derive_kit_paths` from
  this tree's `render-doc.sh` and from `a99b3f23`'s, run over the memory-tree templates, the five
  review-harness templates and the Skill's template from each of the three kit directories, printed
  identical 18-line outputs.

## Owed to the close

- The section 7 legs and then the bar, once.
- RED then GREEN for each `New arm:` line, the arm itself run on its staged break: sections 2h and
  2i, the `check_kit_cites` parity row, and RA6-1's two new sites with RA7-1 to RA7-4.
- `FLOOR_ASSERTIONS` at 686 is counted by hand off the blocks and not measured by a run.
- `kit epoch` and `kit version markers`: three kits' shipped bytes moved, and the lander's `mint`
  writes their versions.
