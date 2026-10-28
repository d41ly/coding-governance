**Serves:** journal TOOL-dSafePassage-63

# TOOL-dSafePassage-63 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/govkit.py`: `check_render_edited` grades a row with
no `oid` and an `output_sha256` as edited when that hash names none of the file's raw bytes, those
bytes with CRLF folded to LF, or the folded bytes written as CRLF; a row with an `oid` is graded by
it as before, and a row with neither field, or no file, is False. `tools/govkit/fixtures/retired_edits.py`
gains the plants `render-edited-no-oid` and `render-eol-no-oid` and the stub `oid-only`.
`tools/govkit/selftest.py`: the `_rte_cases` rows gain the two plants and `render-edited-no-oid
--stub oid-only`. `help/update-edits.md`'s "A rendered file you edited since its last render"
paragraph says how a row with only its install's bytes is compared.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 were observed by
the unit's own fixture, `python tools/govkit/fixtures/retired_edits.py --plant <case>`, over its
scratch repositories under `%TEMP%` on node d (Windows, Git Bash), and AC2's red by a `python -c`
probe of `check_render_edited` over a scratch file; AC3's first half by `git grep`. They stand in for
the `govkit selftest` leg's `[dSafePassage-63]` rows for this unit only.

Owed at the close: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `recall floor arms`, `policy fixtures`, `encoding posture`, `lexicon naming
predicates`, `docs` (AC3's `python tools/govkit/docs_leg.py` exits 0, which the role hook refused
in this pass), `memory hygiene`, `spec tokens`; and the new arm's RED-first observation (§7): the
`_rte_cases` rows, `render-edited-no-oid --stub oid-only` staging the red.

**Evidences:** TOOL-dSafePassage-63
- AC1 — `--plant render-edited-no-oid` exited 0 printing `the render's recorded oid: 'absent'`, `verdict docs/out.md: 'render-edited'`, `the HELD BACK line: 'True'`, `render-edited orders: '1'`, `the edited bytes: 'kept'`, `6 of 6 observation(s) matched`. Red: `--plant render-edited-no-oid --stub oid-only` exited 1 printing `verdict docs/out.md: 're-rendered' · expects 'render-edited' · MISS` and `the edited bytes: 'overwritten'`.
- AC2 — `--plant render-eol-no-oid` exited 0 printing `the render's recorded oid: 'absent'`, `verdict docs/out.md: 're-rendered'`, `render-edited orders: '0'`, `4 of 4 observation(s) matched`. Red: a `python -c` probe over a scratch file of `a\r\nb\r\n` against a row recording the hash of `a\nb\n` printed `crlf of lf-record False raw-only would say True`: the raw hash alone reads the line-ending rewrite edited.
- AC3 — `git grep -n -e "recorded only the bytes" -- help/update-edits.md` printed `help/update-edits.md:42`. `python tools/govkit/docs_leg.py` is a gate leg the role hook refuses here: owed at the close.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (the `_rte_cases` rows for dSP-63 and the `oid-only` stub), the break was `check_render_edited` returning False on a row with no `oid`, which is what the stub stages: `FAIL [dSafePassage-63] plant render-edited-no-oid matches its case — exit 1`, where the fixture prints `the edited bytes: 'overwritten' · expects 'kept' · MISS` (1 of 3). Restored, GREEN: 3 of 3 `ok`.
