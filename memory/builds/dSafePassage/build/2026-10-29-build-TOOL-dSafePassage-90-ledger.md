**Serves:** journal TOOL-dSafePassage-90

# TOOL-dSafePassage-90 — acceptance ledger

The unit as built, at spec rev-2. Product writes: `tools/govkit/govkit.py` (S1: the local `own_file`
and its `samefile` arm leave `_cmd_update`'s `renamed` occupancy test, which now reads
`not in_place`; the one `r.fail` call picks a case-only, an other-name or the occupied message by
`_alias`, a `samefile` identity, and `_case`, a `casefold` compare under it) and
`tools/govkit/selftest.py` (S2: the case-only `[dSP-88]` check in the `DEPL-dCarriedReceipt-11`
block becomes the `[dSP-90]` check, reading the target's index and bytes). No function added, so
`memory/map/generated/symbols.json` is not regenerated; no `Refusal` site is added or removed.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion was observed
on node a (Windows 11, case-folding filesystem) from this worktree's root. The §4 probe ran verbatim
from the run's scratch; its `tempfile.mkdtemp(prefix="p90-")` fixture repos went under `%TEMP%`, the
short-path exception for fixture repositories.

Owed at the close: the RED-first observation of §7's `New arm:` line, the `[dSP-90]` check staged red
by the `samefile` arm kept in the occupancy test; and the §7 legs at the bar. The red probe below ran
against a scratch copy of HEAD's engine and does not discharge the arm's staged-break observation
inside the selftest.

**Evidences:** TOOL-dSafePassage-90
- AC1 — `python <scratch>/p90_probe.py` printed `case-insensitive: True`, then `case-only alone: update exit 1 | second spelling named: True | index: ['keep.txt'] | bytes kept: True`, then `case-only sibling: update exit 1 | second spelling named: True | index: ['keep.txt'] | bytes kept: True | occupied refused: True`, then `hard link: update exit 1 | case-only named: False | other name named: True | bytes kept: True`. Against a scratch engine extracted from HEAD (`a21607b16`) it printed `case-only alone: update exit 0 | second spelling named: False | index: ['Keep.txt'] | bytes kept: True`, `case-only sibling: update exit 1 | second spelling named: False | index: ['keep.txt'] | bytes kept: False | occupied refused: True` and `hard link: update exit 1 | case-only named: False | other name named: False | bytes kept: True`, the red side.
- AC2 — `git grep -n -e "own_file" -e "samefile" -- tools/govkit/govkit.py` printed one line, `govkit.py:11110`, the `_alias` test; the `case-only rename is on a case-insensitive filesystem`, `casefold()` and `under another name (a link` greps each printed one line (`:11114`, `:11111`, `:11119`).
- AC3 — `git grep -n -F "[dSP-90]" -- tools/govkit/selftest.py` printed one line, `selftest.py:13125`, in the `DEPL-dCarriedReceipt-11` block; `git grep -n -F "[dSP-88]" -- tools/govkit/selftest.py` printed one line, `selftest.py:13106`, the in-place check.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in a scratch clone of `390033278` (batch f, `2026-11-01-prompt-TOOL-dSafePassage-86-1-researcher.md`), each break staged alone and restored. On node a's case-folding NTFS (`fold True`), the same slice: the samefile arm kept in the occupancy test: `FAIL [dSP-90] a case-only rename is refused by name where the filesystem folds case, and moves where it does not — fold True update 0 ['pinned/demo/Keep.txt']`, `[dSP-88]` staying ok. GREEN restored: both ok, `FAILURES []`.
