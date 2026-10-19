# TOOL-dRenderedAnchor-2 — acceptance ledger

**Serves:** journal TOOL-dRenderedAnchor-2

This is the build pass of the unit, built from spec rev-1. `<p1>` is the pass commit this ledger
lands in. It narrows `scan_misplaced_harnesses` to a file beside a mark of its kit through the new
`read_kit_home`, re-plants selftest arm 17 with each mark, adds arm 18 and arm 16's two decoy rows,
adds sections 2e and 2f to `tools/lib/resolve-python.test.sh`, gives `tools/roles/roles_lib.py`
`resolve_cited_paths` and the adopter's `render_skill` its citation pass, adds adopter arm 14 with
its floor, rewords check-wiring's roles note, the render's line and docstring, the roles README, the
roles help page and the roles feature map, adds the two gotcha entries and the repro record's
correction, and moves the spec's status to CLOSED.

No merge bar, gate leg or self-test suite was run by this pass: not `render_agents.py --selftest`,
not `adopt-roles.test.sh` and not `resolve-python.test.sh`. The section 7 legs and the RED-first
observation of the six `New arm:` lines are owed to the close. Every criterion below was observed by
a direct probe on this Windows host under Python 3.14.5, each probe program saved under the session
scratchpad: an in-process program for AC1, AC2 and AC4 that builds each row as the arms do, a bash
program for AC3 and AC5 that builds the section 2e and 2f fixtures, and a bash program for AC14 that
builds the fixture as the adopter suite's `build_fixture` does and runs the arm's body.

govkit lands from a commit, so AC6, AC8 and AC12 ran from `28a7f9f91`, a scratch clone of this
branch at `aa49edc1a` holding the pass's eight product files committed as they stand in `<p1>`. Its
trees are `tools` `cf80fbde`, `help` `4ddcd941`, `skills` `18fefd1f` and `.githooks` `ca920885`, and
`<p1>` carries the same four tree ids.

**Evidences:** TOOL-dRenderedAnchor-2
- AC1 — `build_fixture` — the probe imported the render, built rows 18a and 18b in one scratch
  directory and 18c in another, wrote each, then called `run_mode` with `check`: each returned 0,
  printed the note for the listed harness, `toolroot/workflows/a.js` and at the root install
  `workflows/a.js`, and printed no `misplaced` line. Red half: with unit 1's
  `scan_misplaced_harnesses` read from `2f7a67b0` swapped in, 18a and 18b each returned 1 on a
  `misplaced` line naming `toolroot/ci/a.js`, and 18c on one naming `ci/a.js`.
- AC2 — `MISPLACED_LINE` — row 17a wrote with 0 and exactly one `misplaced` line, and its check
  returned 1 with that line, equal to the constant formatted with `toolroot/workflows/a.js` and
  `toolroot/renamed/a.js`, and no note. Row 17b returned 1 with the same line and no note; row 17c
  returned 0 with the note and no `misplaced` line. Red halves: with the scan's template test cut,
  17a wrote and checked with 0 and the note; with its `read_kit_home` test cut, 17b returned 0 with
  the note.
- AC3 — `tools/lib/resolve_kit_dir.py` — loaded from the worktree over section 4's six-row fixture
  with `here` at `p`, it printed `p/k`, `p/k`, then `LookupError` for rows 3 to 6. Red halves: a
  copy with the role term cut printed `c` for row 3, and a copy with the home term cut printed `p/k`
  for row 4, every other row unchanged.
- AC4 — `harnesses` — arm 16's fixture with the `merged` and the other-home `rendered` decoy rows
  ahead of the real row, each backed by `.claude/a.js`, wrote `harnesses` as
  `['toolroot/renamed/a.js']`. Red halves: with the role term, and separately the home term, cut
  from the library's inline `resolve_kit_dir` in-process, `harnesses` read `['.claude/a.js']`.
- AC5 — `derive_kit_paths` — sourced from `tools/lib/render-doc.sh` over the section 2f fixture, it
  printed exactly one line, `{{TOOL_ROOT}}h/t.js`, a tab and `p/k/t.js`. Red half: with
  `git show a60b0c7d:tools/lib/render-doc.sh` sourced instead, it printed nothing.
- AC6 — `tools/review-harness/` — `$T` is `%TEMP%/rh3`, made from `28a7f9f91` by the repro
  record's instruments: intake rc 0 with 26 kits; apply rc 1 with 255 files, 365 receipt rows and
  35 problems, each a leg, pin or adopter line of a fresh install, as unit 1's ledger measured at
  both of its commits; the hand render rc 0 writing the four harnesses; then gov's `AGENTS.md`
  copied in and the roles adopter's `--scaffold` rc 0. Instrument 5, the spawn guard, was not run:
  no criterion here reads it. Over `$T`, `derive_kit_paths` sourced from `tools/lib/render-doc.sh`
  printed `tools/review-harness/tier2-review.js`, `tools/review-harness/unattended-build.js` and
  `tools/review-harness/unattended-unit.js` for the three harness citations, each a file in `$T`.
  Red half: sourced from `a60b0c7d`, only the `unattended-unit.js` citation printed.
- AC7 — `derive_kit_paths` — over the repro record, `grep -c 'TOOL-dRenderedAnchor-2'` printed 2,
  `grep -c 'derive_kit_paths'` printed 1 and `grep -c '^## '` printed 3; at `2f7a67b0` they read 0,
  0 and 3.
- AC8 — `python tools/govkit/govkit.py update --target $U --to <p1>` — `$U` is `%TEMP%/rh1u`, a copy
  of `%TEMP%/rh1` with its two roles files restored from its index to the `a60b0c7d` install bytes,
  which unit 1's close had overwritten. Its own memory-tree adopter's `--render` exited 3, nothing to
  refresh, and its `--scaffold` refused while `memory/` held the two guides apply landed, so
  `memory/` was moved aside, `--scaffold` exited 0 and the two guides were put back. The rendered
  `memory/guides/BUILD-METHOD.md` named `tools/workflows/` at lines 134, 223 and 262 and
  `tools/review-harness/unattended-unit.js` at 225. All of it was committed, then
  `python tools/govkit/govkit.py update --target $U --to 28a7f9f91911165eb52b7c3135413793f5b5aa9a`
  ran from the scratch clone, read-only, rc 0, 348 lines. Its lines naming the three files, verbatim:
  `  re-rendered        [rendered     ] memory/guides/BUILD-METHOD.md`,
  `  re-rendered        [rendered     ] .claude/skills/build/SKILL.md` and
  `  re-rendered        [rendered     ] memory/guides/REVIEW-PROTOCOL.md`. The other `SKILL.md`
  rows read `re-rendered` too, for the cleanup, lexicon, runlog, drift-audit and memory-recall
  Skills, and `missing` for the unattended Skill; 16 lines carry `re-rendered`. No line names any of
  them as drift. The carry-map lines that list `memory/guides/BUILD-METHOD.md`,
  `.claude/skills/build/SKILL.md` and `memory/guides/REVIEW-PROTOCOL.md` among the rows under a
  dropped directory name them too.
- AC9 — `tools/check-wiring.sh` — `grep -c 'adopt-roles.sh --check'` over it printed 2 and
  `grep -c 'until the review harness is installed'` printed 0, and `grep -c 'check-wiring'` over
  `help/roles.md` printed 2; at `2f7a67b0` they read 0, 1 and 0.
- AC10 — `memory/map/features/roles.md` — `grep -c 'TOOL-dRenderedAnchor-1'` printed 3,
  `grep -c 'kit.toml'` printed 1 and `grep -c 'note, not a defect'` printed 0; at `2f7a67b0` they
  read 0, 0 and 1.
- AC11 — `kit.toml` — counted 1 over `help/roles.md`, 1 over `tools/roles/README.md` and 11 over
  `tools/roles/render_agents.py`, and `grep -c 'is installed; the kit resolver'` over the render
  printed 0; at `2f7a67b0` they read 0, 0, 0 and 1.
- AC12 — `$T/.claude/skills/build/SKILL.md` — after apply, whose roles adopter ran before the
  harnesses were rendered, its lines 45 and 76 named `tools/workflows/`. After the hand render and
  the `--scaffold`, `grep -n` printed line 45 naming `tools/review-harness/unattended-build.js` and
  line 76 naming `tools/review-harness/tier2-review.js`, and no line naming `tools/workflows/`.
  `harnesses` read the three `tools/review-harness/` paths.
- AC13 — `git diff --quiet -- .claude/skills/build/SKILL.md` — after
  `bash tools/roles/adopt-roles.sh --scaffold` in this worktree, which printed the render's
  unchanged line and exited 0, it exited 0. In-process, `resolve_cited_paths` over gov's template
  returned the four citations at `tools/unattended/unattended.sh`, `tools/workflows/unattended-build.js`,
  `tools/workflows/tier2-review.js` and `tools/run-gates/run-gates.sh`, each what the plain
  substitution writes. The red half, an absolute path, was not staged.
- AC14 — `adopt-roles.sh --scaffold` — the probe built the fixture at a short `%TEMP%` path, read
  the two cited harnesses, `unattended-build.js` and `tier2-review.js`, from the template and the
  workflow table, moved them behind rendered rows into `tools/renamed/`, and re-ran the scaffold: rc
  0, the Skill named both under `tools/renamed/` and neither under `tools/workflows/`, and the
  adopter's `--check` inside the probe exited 0. Red half: with the citation pass's loop taken out
  of a copy of the adopter, the Skill named both under `tools/workflows/` and the arm's assertion
  failed. The hook refuses `adopt-roles.sh --check` spelled in a role agent's command, as the
  `roles render wiring` leg, so the close re-observes that half through arm 14.
- AC15 — `memory/gotchas/two-answers-to-one-question.md` — `grep -c 'TOOL-dRenderedAnchor-1'`
  printed 1 over it and 1 over `memory/gotchas/invariant-held-on-one-admission-path.md`, which
  gained a "Where it bit" section to hold its entry; at `2f7a67b0` both read 0.
