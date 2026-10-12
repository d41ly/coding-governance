# TOOL-aTrimmedHook-1 — build brief

**Serves:** journal TOOL-aTrimmedHook-1

node a · 2026-10-11 · the orchestrator builds this unit inline; the spec is the scope and this brief
adds only what the spec does not carry. Inline, so the four units are sequenced by this session.

- **Read first, whole:** the spec `spec/2026-10-11-spec-TOOL-aTrimmedHook-1.md`, `rosters()`,
  `collect()`, `cmd_check()` and `main()` in `tools/memory-tree/gen_build_index.py`, and check 9 in
  `tools/memory-tree/check-memory-hygiene.sh`.
- **Write set.** Declared with `--dispatch` before writing: `tools/memory-tree/gen_build_index.py`,
  `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/README.md`,
  `memory/map/generated/symbols.json`, the memory-tree dossier, the spec, the build README, the
  acceptance ledger, `memory/LIVE.md` and `memory/ledger/2026-10.md`.
- **Fixtures.** Arms use `_fixture` in a temp dir and stage edits there; `main` is exercised through a
  subprocess with the fixture as cwd.
- **Verification, fast and direct only.** `python tools/memory-tree/gen_build_index.py --selftest`,
  each new arm seen RED first against a classifier that ignores ids and a structural set without
  `ledger/`; the staged hygiene leg for AC7; `check-arms.py --check`, `lexicon.py`,
  `gen_map.py --write`, `check-spec-tokens.py`. No bar, no whole suite.
- **Commit** once, subject `build(aTrimmedHook): TOOL-aTrimmedHook-1 — <what>`, trailers
  `Pass: TOOL-aTrimmedHook-1` and the co-author line, with `RUN.md`, the spec set CLOSED only when
  every AC was observed, and the acceptance ledger.
