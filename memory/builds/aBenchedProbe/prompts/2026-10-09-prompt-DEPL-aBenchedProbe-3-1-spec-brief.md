**Serves:** journal DEPL-aBenchedProbe-3 DEPL-aBenchedProbe-4

# Spec brief — aBenchedProbe, the closing review's two promotions

You author the spec for each unit you are handed, and you write no code. Read first: the closing
review record `memory/builds/aBenchedProbe/reviews/2026-10-09-review-TOOL-aBenchedProbe-1-closing-diff-round1.md`
WHOLE (it carries each finding's location, impact and the skeptic-corrected fix), the specs of
`DEPL-aBenchedProbe-1` and `DEPL-aBenchedProbe-2` the findings land on, and the earlier spec brief
`2026-10-09-prompt-TOOL-aBenchedProbe-1-1-spec-brief.md`, whose invariants all still bind. Filename
`memory/builds/aBenchedProbe/spec/2026-10-09-spec-DEPL-aBenchedProbe-<n>.md`, status `OPEN`, `rev-1`,
`node a`, `base 2b26f187`, `streams deployer`. Both are **Tier-2** with the full ten sections. Header
`order`: DEPL-3 is `order 4`, DEPL-4 is `order 5` (both write `tools/govkit/govkit.py` and
`tools/govkit/selftest.py`, and DEPL-4's arms run against DEPL-3's predicate). Each spec's §1 names the
review finding ids it closes. Name the specs in `authored` by unit id.

**One invariant this pair adds.** The review's HIGH is the `hand-named-gate-list-green-while-the-bar-reds`
class: DEPL-aBenchedProbe-1 changed `selfcheck` and named only `govkit selfcheck` over the real tree, so
nobody ran the `govkit selftest` fixtures that call `selfcheck`. Both specs' §6 must observe the
affected `tools/govkit/selftest.py` FUNCTIONS directly, sliced one function at a time (memory note
"govkit slices and the guards that bite them"; the suite pins the common dir's HEAD in a linked
worktree, so never run the whole suite in a pass). Enumerate in §4 every selftest function that runs
`selfcheck` (grep for it), and say which ones each unit's change can move.

## DEPL-aBenchedProbe-3 — 7j4's liveness reds bind only where a self-test population exists (H1, id 2)

The 7j4 arm in `selfcheck` (`tools/govkit/govkit.py` ~3260-3295) reds on an absent manifest, zero
legs graded and zero self-test-shaped legs. `tools/govkit/selftest.py` builds minimal scratch-gov
trees (~3101 with one `engine.sh` leg and no chunk, ~5019 with one `true` leg and no chunk,
`build_scratch_gov_kit` ~5079 with no gate-legs.json) and expects `selfcheck` green on them, and its
AC5 fixture (~5426-5446) sets chunk `selftests` with subject `repo`, 7j4's exact red predicate.

Take the skeptic's corrected fix as the starting design and test it against the alternatives:
1. The zero-graded and zero-shaped reds bind only when gov's manifest has at least one
   `chunk == "selftests"` row; otherwise `r.note`. Say why this keeps the liveness the arm exists for
   on gov's real tree (where 52+9 legs carry that chunk) and what a scratch tree loses.
2. An absent gate-legs.json is a note, not a red, unless some descriptor declares a `[[gate_leg]]`.
   Check how 7h itself treats an absent manifest and agree with it rather than inventing a third rule.
3. The AC5 fixture keeps subject `repo` and its pin-row assertion, and expects exit 1 with a line
   naming `7j4: entry 'demo' gate leg 'demo'` (confirm the exact spelling the arm prints). First
   confirm `selfcheck --write` still writes the pin on a red run; if it does not, say what AC5 must
   change instead.
Acceptance: each affected selftest function observed RED at the current HEAD (before the fix) and
GREEN after, sliced; the real tree's `python tools/govkit/govkit.py selfcheck` still green with the 7j4
note naming 59 graded / 22 shaped / 3 exempt (DERIVED, not pinned); and a staged break that removes
every `selftests` chunk from a COPY of the manifest shows the liveness red is now a note, while one
that keeps them and empties the descriptor legs still reds. Fixture copies go under `%TEMP%/<short>`.

## DEPL-aBenchedProbe-4 — regression arms for the keep rule, 7j4 and the 7h ceiling clause (minors)

The review's two MEDIUM items and two LOW items, batched (M4: one unit for the minors):
- **H-M1 (ids 1, 4, 6).** In `check_ceiling_emission` (`tools/govkit/selftest.py` ~2328-2422), after
  CE4: assert the receipt's emitted ceiling for the leg is still gov's 1780, `settle`, run a SECOND
  apply with no edit, and assert it exits 0, the row still reads 3600 and the keep line prints again.
  CE5 stays as it is. Observe it RED with `govkit.py`'s receipt write changed to `row.get("ceiling")`.
- **H-M2 (ids 7, 8).** Persistent staged-break arms in the selftest's gov-copy block, following the
  `check_halved_install_arms` precedent named in the review: (a) 7j4 — the copy's `pre-push self-test`
  set to subject `repo` in descriptor AND manifest reds with a `7j4:` line naming the leg; the `chunk`
  key deleted from one filename-shaped `declarations` row reds naming the argv element; restored, green.
  Observe the arm RED with 7j4's exempt test mutated to exempt everything. (b) 7h ceiling — the copy's
  push-main `pre-push self-test` ceiling set to 1781, then `true`, each reds naming push-main and the
  leg; restored, green. Observe it RED with the clause deleted. Measure the cost of a gov-copy selfcheck
  and say whether the arms can share one copy.
- **H-L1 (id 3).** Delete the dead `manifest_chunk: dict = {}` pre-initialisation at
  `tools/govkit/govkit.py` ~2673 and its false comment, or keep the binding and reword the comment so it
  says 7j4 reads the map only under its own `is_file` guard. DEPL-3 may move that guard; read its spec.
- **H-L2 (id 9).** CE4's "names the leg" assertion matches the leg inside the keep line itself, never
  as two substrings over the whole output.
- **Left-shift.** Each class the review named is already a `memory/gotchas/` file except, possibly,
  H-L2's (an assertion that a line names X matched over the whole output). Grep `memory/gotchas/`; if
  no class covers it, the spec adds one gotcha file in the format the others use, and says which.
