# TOOL-dRenderedAnchor-6 — acceptance ledger

**Serves:** journal TOOL-dRenderedAnchor-6

This is the build pass of the unit, built from spec rev-1. `<p1>` is the pass commit this ledger
lands in. It adds `render_kit_cites` to `tools/lib/render-doc.sh` as a third gated canonical, carries
it and `derive_kit_paths` inline in the review-harness kit's parity script and in the unattended
adopter, calls it in each `render` between the `{{KIT_DIR}}` and the `{{TOOL_ROOT}}` substitutions,
derives `KIT_PATHS` once in each, gives the parity script's render mode its second pass under
`PROTOCOL_PARITY_REPASS`, adds the `render_kit_cites` parity row and section 2g to the python
resolver's suite, adds arms RA6-1 and RA6-2 to the build harness's suite with its floor raised 658 to
667, says so in both kit READMEs, regenerates the codebase map's `symbols.json` and the build index,
and moves the spec's status to CLOSED.

No merge bar, gate leg or self-test suite was run by this pass: not `resolve-python.test.sh`, not
`unattended-build.test.sh`, and not the parity script in check mode, which the role hook refuses as a
suite-shaped name. The section 7 legs and the RED-first observation of the four `New arm:` lines are
owed to the close. Every criterion below was observed by a direct probe on this Windows host under
bash 5.3 and Python 3.14, each probe saved under the session scratchpad: `probe_ra6.sh` builds `$L`
with the arm's own steps at `%TEMP%/ra6`, and each red half ran the same probe over a scratch copy of
the three kit directories with one break staged by `stage_break.py`, which removes the shipped call
or guard rather than substituting a value.

**Evidences:** TOOL-dRenderedAnchor-6
- AC1 — `scripts/rh/tier2-review.js` — the fixture's parity script in render mode in `$L` printed its
  five `rendered` lines, the re-run line, the five again, and `rc=0`. Over the protocol, the counts
  of `scripts/rh/tier2-review.js`, `scripts/rh/check-verifier-fanout.sh` and `scripts/workflows/`,
  each a `grep -c`, printed 2, 1 and 0. Red half: with the `render_kit_cites` call taken out of the
  parity script's `render`, the three counts read 0, 0 and 3.
- AC2 — `protocol-parity: in parity` — NOT observed here: the check mode of a suite-shaped script is
  the hook's to refuse and the close's to run, through RA6-1. Its render-side red half was observed:
  with the second pass's guard taken out, no re-run line printed, and the protocol's counts read 0, 1
  and 2, so the first render names `scripts/workflows/tier2-review.js` on both lines.
- AC3 — `scripts/rh/unattended-build.js` — after AC1, `bash scripts/unattended/adopt-unattended.sh`
  in `$L` exited 0; over the Skill the three counts printed 1, 1 and 0, and line 125 read
  `` `scripts/rh/unattended-build.js` `` then `` `scripts/rh/unattended-unit.js` ``. The fixture's
  `adopt-unattended.sh --check`, run in `$L` with `GOV_SETTINGS_JSON` empty, printed its hooks line
  for three wired fragments and `in sync`, and exited 0. Red half: with the call taken out of the
  adopter's `render`, the counts read 0, 0 and 1, line 125 naming `scripts/workflows/` twice.
- AC4 — `a p/k/t.js b {{TOOL_ROOT}}c {{GATE_RUNNER}}` — the canonical, sourced in a `bash -c` with
  section 2g's three CRLF lines and `out` exported, printed exactly that, read through `od -c`. Red
  halves: with the case filter taken out it printed `a p/k/t.js b q/c x`, and with the CR drop taken
  out a `\r` followed `t.js`.
- AC5 — the four block diffs — `render_kit_cites` and `derive_kit_paths` out of each renderer, CRs
  dropped, against `tools/lib/render-doc.sh`: each printed nothing and exited 0. Each copy carries two
  `resolve_kit_dir` blocks, its own and the one nested in `derive_kit_paths`. The red half, one byte
  changed in a copy, was not staged; the parity row that grades it is owed to the close.
- AC6 — `git status --porcelain` — in this worktree, holding the bytes `<p1>` commits,
  `bash tools/workflows/check-protocol-parity.test.sh --render` printed its five `rendered` lines and
  no re-run line, and `bash tools/unattended/adopt-unattended.sh` rendered the Skill; both exited 0,
  and the status named only this pass's own edited files. Re-run at `b31803aab` itself, both exited
  0 and the status printed nothing. The red half was not staged.
- AC7 — `tools/review-harness/` — `<p1>` is `b31803aab`, and govkit lands a commit rather than the
  working tree, so this answer was added by the records commit after it. A fresh `%TEMP%/rh6` made
  by Instruments 1 to 3 from `b31803aab`: `apply` printed `[3/LAND] from b31803aa` and landed the kit
  at `tools/review-harness/`, and the hand render printed its five `rendered` lines, the re-run line
  and the five again, at rc 0. With PV-AC12's seven-key conf added and staged,
  `bash tools/unattended/adopt-unattended.sh` exited 0. `grep -n 'tools/review-harness/'` printed
  lines 34, 92 and 202 of `$T/memory/guides/REVIEW-PROTOCOL.md` and line 125 of
  `$T/.claude/skills/unattended/SKILL.md`, which reads `` `tools/review-harness/unattended-build.js` ``
  then `` `tools/review-harness/unattended-unit.js` ``, and `grep -c 'tools/workflows/'` printed 0
  over each. Red half: the same instruments from `2c5b6287`, this unit's base bytes, read
  `tools/workflows/` on lines 34, 92 and 202 of the protocol and twice on line 125 of the Skill. In
  both runs `apply` exited 1, naming 35 legs that did not exist before the install and are red after
  it; nothing here depends on those legs.
- AC8 — `derive_kit_paths` — `grep -c` printed 1 over each README; at `05357638` both read 0.
