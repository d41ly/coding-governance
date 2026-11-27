**Serves:** research TOOL-dTotalRecall-41

# TOOL-dTotalRecall-41 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-41-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-41-reground-spec-writer.md), in substance.

- Folded to rev-3; `check-spec-tokens.py --spec`, `--check-specs`, hygiene check 12 and pinned-facts read green; no fork new or parked.
- Every bare line citation moved to `path#symbol`.
- Unit 7's `--sev <LEVEL> <why>` (its F5): S1 refuses a line break in the `--sev` reason too, since `render_sev_row` writes it verbatim; S3 counts one added ask and one added `SEV` row; every criterion passes `--sev LOW w`, so unit 7's parser cannot exit 2 for the wrong reason.
- S2 states the grade as `derive_clauses(build_corpus([parse]))` over the one would-be parse; the Goal's injection repro still produces two rows at `e1ae60af8`.
- The test arm moves from `gov_record.py`, which no leg runs, to unit 7's `build_records.py --fixture --plant ask-door` case in `check-memory-hygiene.test.sh`; Files touched and the leg line grow to match.
- Unit 19's `New arm:` on `gov_record.py` has the same no-leg gap, passed to unit 19's writer mid-run.
