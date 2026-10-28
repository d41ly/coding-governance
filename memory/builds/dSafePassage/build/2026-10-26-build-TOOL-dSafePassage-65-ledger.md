**Serves:** journal TOOL-dSafePassage-65

# TOOL-dSafePassage-65 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/govkit.py`: `read_descriptor_at(root, commit, dpath)`
reads the descriptor blob at `commit` through `blob_at`, parses it with `tomllib`, refuses by path and
commit where it does not parse, and joins it with `resolve_descriptor_paths` over `derive_tool_root`;
`None` where the blob is absent. `tracked`, `resolve_rule_pool`, `expand_rules` and `resolve_entry`
take `at=None`; with `at`, `tracked` lists `git ls-tree -r --name-only -z <at>`. `_cmd_update`'s role
re-resolution, where `to_commit` differs from the checkout's `HEAD`, resolves each kit through
`resolve_entry(root, read_descriptor_at(root, to_commit, dpath), ctx, at=to_commit)`, and keeps the
working tree's resolution for a kit whose descriptor is absent at `to_commit`.
`tools/govkit/fixtures/retired_edits.py` gains the plant `edited-rolled-back`; `tools/govkit/selftest.py`'s
`_rte_cases` rows gain it; `help/upgrade-steps.md`'s "Rolling back" gains a **Roles.** bullet.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 was observed by the
unit's own fixture, `python tools/govkit/fixtures/retired_edits.py --plant <case>`, over its scratch
repositories under `%TEMP%` on node d (Windows, Git Bash), its red by the same plant run before the
govkit change; AC2's first half by `git grep`. They stand in for the `govkit selftest` leg's
`[dSafePassage-65]` row for this unit only. `--plant edited-reshipped` (7 of 7), `edited-row` (9 of 9)
and `fragment-rollback` (6 of 6) still exited 0. A `python -c` probe of `read_descriptor_at` printed
`None` for an absent path, `tools/hooks` as the joined home of `tools/hooks/kit.toml` at `HEAD`, and a
`Refusal` naming `tools/govkit/govkit.py at HEAD is not valid TOML` for a blob that does not parse;
`tracked(root)` and `tracked(root, "HEAD")` both listed 7878 paths.

The spec's AC1 red names two misses, the role and an order; the red observed shows one. Before the
change the rollback printed `patched [retired-edited]` and wrote no order, because gov holds a blob at
`A` and the row is graded from it under its recorded role; only the receipt role missed. The criterion
still discriminates by that observation.

Owed at the close: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `recall floor arms`, `policy fixtures`, `encoding posture`, `lexicon naming
predicates`, `docs` (AC2's `python tools/govkit/docs_leg.py` exits 0, a gate leg the role hook
refuses in this pass), `memory hygiene`, `spec tokens`; and the new arm's RED-first observation (§7):
the `_rte_cases` row `edited-rolled-back`, its red staged by the re-resolution reading the working
tree in a working copy.

**Evidences:** TOOL-dSafePassage-65
- AC1 — `--plant edited-rolled-back` exited 0 printing `first run's verdict: 'retired-edited'`, `role before the second run: 'retired-edited'`, `verdict tools/demo/gone.txt: 'patched'`, `receipt role: 'engine'`, `retired-edited orders: '0'`, `the edited bytes: 'kept'`, `7 of 7 observation(s) matched`. Red: before the govkit change it exited 1 printing `receipt role: 'retired-edited' · expects 'engine' · MISS`, `6 of 7 observation(s) matched`.
- AC2 — `git grep -n -e "descriptor gives it" -- help/upgrade-steps.md` printed `help/upgrade-steps.md:237`. `python tools/govkit/docs_leg.py` is a gate leg the role hook refuses here: owed at the close.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (the `_rte_cases` row `edited-rolled-back`), the break was the role re-resolved from the working tree, with `read_descriptor_at` never taken: `FAIL [dSafePassage-65] plant edited-rolled-back matches its case — exit 1`, where the fixture prints `receipt role: 'retired-edited' · expects 'engine' · MISS`. Restored, GREEN: 1 of 1 `ok`.
