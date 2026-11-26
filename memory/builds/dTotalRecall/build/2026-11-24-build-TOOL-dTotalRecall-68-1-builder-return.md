**Serves:** journal TOOL-dTotalRecall-68
**Caused-by:** TOOL-dTotalRecall-68

# TOOL-dTotalRecall-68 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `c0a707782` from [2026-11-24-prompt-TOOL-dTotalRecall-68-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-68-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `7252440fd`.

## Why

Spec rev-3 is built as written, with no divergence. Re-derived at the pass base, unit 65's nine rows, its `#` notes and the reader list matched the spec's claims. The one reader or plant the spec does not name is `record_kinds.py`'s plant `marker-in-kept-script`, which S6's grep clause covers. Unit 66 rev-5 already holds the amendment, so S5 wrote nothing there. (DERIVED 2026-11-24, the pass)

## Summary

`census-kept-paths` is registered as a shrink-only `[[ledger]]` population in tools/govkit/registry.toml, with unit 65's notes moved into its comment. The nine rows of memory/project/census-kept-paths.txt were rewritten through `write_rows` at the base sha, seeded (DERIVED 2026-11-24). `tree_lib.py` gains `KEPT_FIELDS`. `read_kept_rows` reads through `legacy_ledger.read_rows` and answers `{path: row}`; `read_kept_path` answers one row or None. Both censuses read `row["reason"]`. All four plants that write a keep row use the new `record_kinds.py#write_kept_fixture` (DERIVED 2026-11-24). The spec is CLOSED, and the acceptance ledger and RUN.md are in the commit.

OBSERVED by probe, DERIVED 2026-11-24:
- AC1: the registration probe prints `tools/govkit/registry.toml shrink-only`, the home, then `True True True`. The read-back prints nine rows, each ending in TAB 1. The tools/lib read exits 0. Stands in for ratchet (unarmed), (populated) and (key shape).
- AC2: the gain probe prints `[]`, the `gained` tuple for the third row, the never-gains line, and 1 last. Stands in for ratchet (never gains). (DERIVED 2026-11-24, the pass)
- AC3: prints `True False`; a three-field row raises ValueError naming `census-kept-paths.txt` and `line 2`.
- AC4: the build-folder lines equal the base's (8 kept, 1 pinned, 0 red), and the alias row at line 380 is kept. Stands in for `record causes` and `record-kinds`. AC3 and AC4 are partial stand-ins only. (DERIVED 2026-11-24, the pass)
- AC5: each stale phrase prints 0, and the records-field phrase prints 5. (DERIVED 2026-11-24, the pass)
- AC6: `kept-row-drained` and `kept-row-editable` each exit 1 with one RED; `reason-on-other-file` exits 1 with two. `adopter-no-registry`, `marker-in-kept-script` and `pinned-writer-drained` print PASS. Stands in for those `memory-hygiene self-test` arms. (DERIVED 2026-11-24, the pass)
- `gen_map.py --write` added one symbol. `leg_factory.py --write` left gate-legs.json as it was. The lexicon still measures 1435 verb offenders, the pin, and `--suggest` accepts the new name. No watched file was touched, so there is no re-stamp. No `--dispatch` beyond the declared set was needed. (DERIVED 2026-11-24, the pass)

OWED TO THE CLOSE: every leg of section 7, and AC5's `merge-base --is-ancestor` half once unit 66 builds. There is no new arm. The moved plants keep their arms' bytes but changed how they write, so the close re-observes them. (DERIVED 2026-11-24, the pass)

OTHER POINTS:
- The factory admits an empty key field, so a row with a blank reason no longer reads as malformed, as it did under unit 65's split. Both censuses read it as keeping nothing (a `Decided:` trailer). Nothing reds the blank field by name, and unit 70's items do not cover it.
- The first three commit attempts were refused by hygiene check 9, because other spec writers were editing the specs of units 70, 73 and 75 in this worktree (DERIVED 2026-11-24). The fourth passed after a re-render. The committed README carries only this unit's rows; the working README holds the full render, unstaged beside those specs and prompts, which I left alone.
- With unit 68 CLOSED, LIVE.md and the TOOL backlog derive the build as DEFERRED until another unit is INPROGRESS.
- `gotchas.py --for-diff HEAD~1..HEAD` ran over the commit. I checked its reader, row-shape-doc and parser classes against the diff; none needed a change.
- Skipped: three compound shell calls the worktree guard refused, each re-run split. Nothing timed out.
