**Serves:** journal TOOL-dSafePassage-74

# TOOL-dSafePassage-74 — acceptance ledger

The unit as built, at spec rev-3. Product writes: `tools/govkit/upgrade_steps.py` (S1's raw-text
test removed from `derive_introduced`, its loop `for i in want & held:`, and `TypeError` joining the
`except` that skips an unparsable vintage, since a misshapen one the test used to skip is now parsed;
S3's docstring) and `tools/govkit/selftest.py` (the `[dSP-74]` checks in `check_upgrade_steps`).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11) over this worktree, run directly from the repository root.

Owed at the close: the `New arm:` line's RED-first observation (the `[dSP-74]` checks in
`tools/govkit/selftest.py`), and the §7 legs at the bar.

**Evidences:** TOOL-dSafePassage-74
- AC1 — the spec's probe, saved to the scratchpad — printed `['lib/dq-1'] True` before the change and `['lib/dq-1', 'lib/esc-1', 'lib/ml-1', 'lib/sq-1'] True` after it.
- AC2 — a scratchpad probe importing `selftest` as a library and replaying the `[dSP-74]` arm's fixture (`build_steps_gov`, a single-quoted `demo/single` row and a single-quoted `[[retired]]` row `gone` committed after the double-quoted `demo/first`) — printed `True` for `read_steps(g, "HEAD", "main")` giving `demo/first` the base commit and `demo/single` the second, in that order, and `True` for `read_retired(g, "HEAD", "main")` giving `gone` the second commit.
- AC3 — `git grep -n -F "f'\"{i}\"' in text" -- tools/govkit/upgrade_steps.py` and `git grep -n "parsed only where" -- tools/govkit/upgrade_steps.py` — each printed nothing.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `b634d60e5` (batch d, `2026-10-29-prompt-TOOL-dSafePassage-72-close-arms-d-researcher.md`), each break staged alone and restored. The `New arm:` line of this unit was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `b634d60e5`. tools/govkit/selftest.py `check_upgrade_steps`, with `derive_introduced` given back the base prefilter (`f'"{i}"' in text`): `FAIL [dSP-74] AC2 a single-quoted step row reads its committing sha, ordered after the earlier row` and `FAIL [dSP-74] AC2 a single-quoted [[retired]] row reads its committing sha` (2 of 2, nothing else red). GREEN restored: `FAILURES 0`, 81 `ok`.
