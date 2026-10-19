# TOOL-dRenderedAnchor-1 — acceptance ledger

**Serves:** journal TOOL-dRenderedAnchor-1

This is the build pass of the unit, built from spec rev-1. `<p1>` is `40d657e2e`, the pass commit
this ledger first landed in, and `<p1>~1` is `0f787ab62`, whose product files equal the spec's base
`a60b0c7d`. The commit after `<p1>` edits this ledger alone: it unwraps two backticked tokens,
which the bug-class checklist's wrapped-token class named over the pass, and records the probes
re-run at `<p1>`. The pass commit widens the receipt step of the canonical resolver and copies the
block's bytes into the 70 inline copies, adds `scan_misplaced_harnesses`, `MISPLACED_LINE` and
selftest arms 16 and 17 to the role render, names the new red in the render's docstring, the roles
README and the roles help page, corrects the awk reader's comment in `tools/check-wiring.sh`, and
moves the spec's status to CLOSED.

No merge bar, gate leg or self-test suite was run by this pass, and `render_agents.py --selftest`
was not run. The section 7 legs and the RED-first observation of arms 16 and 17 are owed to the
close. Every criterion below was observed by a direct probe on this Windows host under Python
3.14.5, each probe program saved under the session scratchpad and each scratch target a fresh
directory under `%TEMP%`, deleted after. The in-process probes of AC2 and AC6 to AC8, first run
before the pass's last whitespace and docstring edit to the render, were run again at `<p1>` with
the same output.

govkit lands from a commit and not from the working copy, so AC4 and AC5 ran from `b34006c1`, a
scratch clone of this branch at `0f787ab62` holding the pass's 74 product files committed as they
stand in `<p1>`. Its trees are `tools` `92d5531a`, `skills` `18fefd1f`, `.githooks` `ca920885` and
`help` `9b82f3d9`, and `<p1>` carries the same four tree ids.

**Evidences:** TOOL-dRenderedAnchor-1
- AC1 — `not a declared harness` — over the repro record, which this pass does not touch,
  `grep -cE '^## (Instruments|Results|Root cause)$'` printed 3 and `grep -c 'not a declared harness'`
  printed 2.
- AC2 — `resolve_kit_dir` — a probe loaded the canonical file with `runpy`, built `%TEMP%/rka` with
  a `.git` directory, `.governance/install.json` holding the six rows of spec section 4 and a sibling
  `%TEMP%/rka-out/w.js`, and called the resolver per row with `here` at the fixture's `tools`. Rows 1
  and 2 printed `tools/review-harness`, rows 3 to 6 `LookupError`. Red halves: over the `a60b0c7d`
  canonical, row 1 printed `LookupError`; over the canonical with the role term taken out, row 3
  printed `.claude`. Both fixtures were deleted after each run. A shell copy, the function block
  of `tools/check-install-prefix.sh` sourced into bash over a rendered-row fixture, printed
  `tools/review-harness` and exited 0, and exited 1 with the named refusal for an absent anchor.
- AC3 — `71 71 1` — a probe listing the population grep's files at `<p1>` and extracting every
  block with carriage returns stripped printed `71 71 1`, and the one block carries
  `row.get("role") == "rendered"`. Red half: with only the canonical edited it printed `71 71 2`; at
  `a60b0c7d` it printed `71 71 1` with no role term.
- AC4 — `node tools/hooks/agent-cap.js` — instruments 1 to 5 ran from `b34006c1` into a fresh
  `%TEMP%/rh2`: intake rc 0, apply 255 files and 365 receipt rows, the hand render rc 0 writing the
  four harnesses, and `adopt-roles.sh --scaffold` rc 0 with no `render_agents: note` and no
  `render_agents: misplaced` line. `harnesses` printed the three paths
  `tools/review-harness/tier2-review.js`, `tools/review-harness/unattended-build.js` and
  `tools/review-harness/unattended-unit.js`, in that order, each a file. agent-cap with
  `CLAUDE_PROJECT_DIR` set to the target exited 0 on the `tier2-review.js`, the
  `unattended-build.js` and the `unattended-unit.js` payloads, each carrying the `args.roles` that
  `handoff.py harness-args` printed there. Red half: the same instruments from `0f787ab62` listed
  the two `tools/workflows/` paths, absent from disk, printed two `note` lines, and agent-cap exited
  2 with `not a declared harness` for both review-harness payloads. Apply exited 1 with the same 35
  problems at both commits, each a pin, adopter, rendered-file or leg line of a fresh install with
  no governing doc; none names the resolver or the roles render.
- AC5 — `python tools/roles/render_agents.py --check` — in the AC4 target, with
  `tools/roles/roles_lib.py` overwritten by `git show a60b0c7d:tools/roles/roles_lib.py`, it exited
  1 and printed `render_agents: misplaced tools/workflows/tier2-review.js` naming
  `tools/review-harness/tier2-review.js`, the same for `unattended-build.js`, then the graded line
  and `drift .claude/roles.json`, and no `note` line. With the file restored from `b34006c1`, equal
  to the installed bytes, it exited 0 and printed the graded line alone.
- AC6 — `build_fixture` — a probe imported the render, called `build_fixture` with one role whose
  `workflow` is `w1`, moved `toolroot/workflows` to `toolroot/renamed`, made `.git`, wrote the
  one-row rendered receipt and ran `run_mode` write then check: both returned 0, `harnesses` read
  `['toolroot/renamed/a.js']`, and neither output carried a `note` line naming `a.js` or any
  `misplaced` line. Red half: over a copy of the kit holding the `a60b0c7d` `roles_lib.py`,
  `harnesses` read `['toolroot/workflows/a.js']` and check returned 1 on a `misplaced` line.
- AC7 — `scan_misplaced_harnesses` — the same probe with no receipt: write returned 0 and printed
  exactly one `misplaced` line, equal to `MISPLACED_LINE` formatted with
  `toolroot/workflows/a.js` and `toolroot/renamed/a.js`, and no note for it; check returned 1
  printing that line. With `toolroot/renamed/a.js` unlinked, check returned 0, printed the note
  and no `misplaced` line. Red half: with `scan_misplaced_harnesses` stubbed to return `{}`, the
  first check returned 0 with the note.
- AC8 — `git diff --quiet` — at `<p1>`,
  `git diff --quiet a60b0c7dc 40d657e2e -- .claude/roles.json .claude/agents/` exited 0.
  In-process in this repository, `derive_harness_paths` over gov's catalogue returned the three
  `tools/workflows/` harnesses held and an empty absent list, and the scan over it returned `{}`.
  Liveness: the scan fed the held list instead named each harness against itself, which is the red
  the absent-only input prevents. `python tools/roles/render_agents.py --check` over this
  repository was not run by this pass: it is the inner command of the `roles render wiring` leg and
  is owed to the close.
- AC9 — `grep -c 'misplaced'` — printed 1 over `help/roles.md`, 1 over `tools/roles/README.md` and
  17 over `tools/roles/render_agents.py`, each 0 at `a60b0c7d`. `grep -c 'rendered'` over
  `tools/lib/resolve_kit_dir.py` printed 3, one in the module docstring and two in the block, and 0
  at `a60b0c7d`.
- AC10 — `tools/check-wiring.sh` — the comment range from `THE RECEIPT RUNG` to the reader carries
  `rendered` and `TOOL-dRenderedAnchor-1`, and read no `rendered` at `a60b0c7d`. The reader's
  function body extracted at `a60b0c7d` and at `<p1>` compared equal under `diff`.
