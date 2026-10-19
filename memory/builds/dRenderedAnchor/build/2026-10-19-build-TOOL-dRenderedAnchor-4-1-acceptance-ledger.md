# TOOL-dRenderedAnchor-4 — acceptance ledger

**Serves:** journal TOOL-dRenderedAnchor-4

This is the build pass of the unit, built from spec rev-1. `<p1>` is the pass commit this ledger
lands in. It adds adopter arm 17 and raises the floor to 50, names arm 17 in the suite header's arm
list and in its WHAT THIS DOES NOT CHECK block, writes "at a prefixed install" and "a
`workflow`-driver harness of the workflow table" into the help page, the roles README, the adopter
header, arm 15's comment and, for the second phrase, the `resolve_cited_paths` docstring, adds the
three gotcha entries, regenerates the gotchas index, and moves the spec's status to CLOSED.

No merge bar, gate leg or self-test suite was run by this pass: not `adopt-roles.test.sh`, in whole
or as a slice, and not `render_agents.py --selftest`. The section 6 legs and the RED-first
observation of the `New arm:` line, arm 17 against line 626 staged as `here = kit`, are owed to the
close. Every criterion below was observed by a direct probe on this Windows host under Python 3.14.5,
each probe program saved under the session scratchpad: `probe_ac1.sh` for AC1, `probe_arm17.sh`,
which grades arm 17's own assertion lines copied out of the block over AC1's two fixtures,
`carriers.py`, section 4's program, for AC5 and AC6, and `ac8.py` for AC8. The adopter fixtures were
built as the suite's `build_fixture` builds one, at short `%TEMP%` paths.

**Evidences:** TOOL-dRenderedAnchor-4
- AC1 — `workflows/tier2-review.js` — in a fixture holding `.git`, the roles kit at `tools/roles/`,
  the conf and the charter, scaffolded once, with `workflows/tier2-review.js` and
  `workflows/unattended-build.js` written at its root, no `tools/workflows/` and no
  `.governance/install.json`, `bash tools/roles/adopt-roles.sh --scaffold` exited 0. The Skill held
  `` `workflows/tier2-review.js` `` and `` `workflows/unattended-build.js` `` once each and neither
  `tools/workflows/` spelling, and the `harnesses` list of `.claude/roles.json` read
  `tools/workflows/unattended-unit.js`, `workflows/tier2-review.js`, `workflows/unattended-build.js`.
  Red half: with the fixture's copy of line 626 staged as `here = kit`, `--scaffold` exited 0, the
  Skill held `` `tools/workflows/tier2-review.js` `` and `` `tools/workflows/unattended-build.js` ``
  and neither root spelling, and `roles.json` was unchanged. Arm 17's assertion lines, graded over
  the two fixtures, printed verdict 1 on the shipped line and 0 on the staged one.
- AC2 — `TOOL-dRenderedAnchor-4` — `grep -n '^FLOOR_ASSERTIONS='` printed one line, `81:FLOOR_ASSERTIONS=50`,
  and line 80 above it names `TOOL-dRenderedAnchor-4`. At `340be90b` it printed
  `78:FLOOR_ASSERTIONS=49`.
- AC3 — `HARNESS_PAIRS_READ` — the arm 17 block with comment lines dropped printed 0 for
  `roles_lib\|TOOL_ROOT_CITE_RE`, and the block piped to `grep -c 'HARNESS_PAIRS_READ'` printed 2.
- AC4 — `arm 17` — the header through `set -u` piped to `grep -c 'arm 17'` printed 2; at `340be90b`
  it printed 0.
- AC5 — `help/roles.md` — `carriers.py` printed `1 0` for the L1 pair over it, `tools/roles/README.md`,
  `tools/roles/adopt-roles.sh` and `tools/roles/adopt-roles.test.sh`. Red half: over the four files
  as at `340be90b` it printed `1 1` for each.
- AC6 — `tools/roles/roles_lib.py` — `carriers.py` printed `1 0` for the L2 pair over it and over the
  four AC5 files. The grep printed `help/roles.md:131`, `tools/roles/README.md:316`,
  `tools/roles/adopt-roles.sh:34` and `tools/roles/roles_lib.py:611`, each holding
  "`workflow`-driver". Red half: at `340be90b` each L2 pair read `1 1`, and the grep printed only the
  README's line 316 and the library's line 611.
- AC7 — `memory/gotchas/observed-by-claim-no-arm-discharges.md` — `grep -c 'TOOL-dRenderedAnchor-4'`
  printed 1 over it and 2 over `memory/gotchas/two-answers-to-one-question.md`; at `340be90b` each
  printed 0.
- AC8 — `tools/roles/roles_lib.py` — `ac8.py` compared the library at `340be90b` with the bytes this
  commit holds, every leading docstring dropped, and printed `equal`; line 626 is unmoved. The
  adopter diff from `340be90b` piped to `grep -c '^[-+][^-+#]'` printed 0. Red half: the same
  program over the fixture's copy with line 626 staged as `here = kit` printed `DIFFER`.

## The close's observations

Run by the main loop at `6d560aed2`, before the closing review.

- `New arm:` arm 17 — RED with `tools/roles/roles_lib.py:626` written as `here = kit`, the C2
  break: `adopt-roles.test.sh` exited 1, `FAIL (1 of 62)`, on arm 17 alone. GREEN with the file
  restored by `git checkout`: exit 0, `PASS (62 assertions)`.
