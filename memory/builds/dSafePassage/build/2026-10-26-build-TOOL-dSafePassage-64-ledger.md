**Serves:** journal TOOL-dSafePassage-64

# TOOL-dSafePassage-64 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/govkit.py`: in `_cmd_update`'s role re-resolution, a
row recorded `retired-edited` whose path the `--to` resolution names a role for, whose `UPDATE_ROLE`
disposition is not in `KIT_WRITING_DISPOSITIONS`, takes that role and is dispatched under it in the
same run, with no `--accept-role-moves`; its `path`, `source`, `commit`, `gov_oid` and `kit` stay.
`tools/govkit/fixtures/retired_edits.py` gains the plant `edited-reshipped`. `tools/govkit/selftest.py`:
the `_rte_cases` rows gain `edited-reshipped`. `help/update-edits.md`'s "A file you edited that gov
stopped shipping" says the row keeps the role until gov ships the file again.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 was observed by the
unit's own fixture, `python tools/govkit/fixtures/retired_edits.py --plant <case>`, over its scratch
repositories under `%TEMP%` on node d (Windows, Git Bash), and its red by the same plant over a
working copy whose return was disabled (`False and` prefixed to its condition), restored after; AC2's
first half by `git grep`. They stand in for the `govkit selftest` leg's `[dSafePassage-64]` row for
this unit only. `--plant edited-row` still exited 0, 9 of 9 matched.

Owed at the close: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `recall floor arms`, `policy fixtures`, `encoding posture`, `lexicon naming
predicates`, `docs` (AC2's `python tools/govkit/docs_leg.py` exits 0, a gate leg the role hook
refuses in this pass), `memory hygiene`, `spec tokens`; and the new arm's RED-first observation (§7):
the `_rte_cases` row `edited-reshipped`, its red staged by the return taken out of a working copy.

**Evidences:** TOOL-dSafePassage-64
- AC1 — `--plant edited-reshipped` exited 0 printing `first run's verdict: 'retired-edited'`, `role before the second run: 'retired-edited'`, `verdict tools/demo/gone.txt: 'patched'`, `receipt role: 'engine'`, `retired-edited orders: '0'`, `the edited bytes: 'kept'`, `7 of 7 observation(s) matched`. Red: with the return disabled in the working copy it exited 1 printing `verdict tools/demo/gone.txt: '(no row)' · expects 'patched' · MISS` and `receipt role: 'retired-edited' · expects 'engine' · MISS`, `5 of 7 observation(s) matched`.
- AC2 — `git grep -n -e "ships the file again" -- help/update-edits.md` printed `help/update-edits.md:11`. `python tools/govkit/docs_leg.py` is a gate leg the role hook refuses here: owed at the close.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (the `_rte_cases` row `edited-reshipped`), the break was the `retired-edited` take-back made `False and …`: `FAIL [dSafePassage-64] plant edited-reshipped matches its case — exit 1`, where the fixture prints `receipt role: 'retired-edited' · expects 'engine' · MISS`. Restored, GREEN: 1 of 1 `ok`.
