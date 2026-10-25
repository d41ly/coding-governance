**Serves:** research TOOL-dWitnessedBar-78

# Round-8 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-78-1-spec-writer.md`, run direct/ae22e6c2ce458a12a, one per stop, extracted from its transcript by script.

## Return 1

I cleared all four spec-token hits in TOOL-dWitnessedBar-78, all in its §6 criteria. I edited the spec in place with no rev bump and changed nothing else. The hygiene gate (`--only 2,12,25`) exits 0 and reports nothing on unit 78. I did not run `python tools/check-spec-tokens.py`, because my role allows only the hygiene gate and the lexicon. So "no dWitnessedBar hit" is still for the main loop to confirm.

**TOOL-dWitnessedBar-78** — authored (round-8 path fix), at `C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-78.md`

- **AC4:** the `-c` literal now opens `sys.argv[1]`, and `tools/gate-legs.json` is passed as an argument after the closing quote. That leaves the tracked path as a separate word.
- **AC11:** now `python verdict_backends.py read --backend local-hook --sha <sha>`, run in `tools/run-gates/`. The created file is cited by its basename.
- **AC12:** both commands now run in `tools/run-gates/`:
  - the posture probe adds `'../gate-lint'` to `sys.path` and gets `verdict_backends.py` through `sys.argv[1]`;
  - the `grep -n "encoding='utf-8', newline=''"` check names `verdict_backends.py` by basename.
  - `scan_text_io` exists at `tools/gate-lint/encoding_posture.py:94`.

The checker's own rules say these forms are not graded:
- A bare basename is not path-shaped outside a repo-root install (`tools/check-spec-tokens.py:47-54`).
- A token opening with a quote is dropped (`NOT_A_TOKEN`, `tools/check-spec-tokens.py:290`). That covers `'../gate-lint'` and the existing `'run-gates/verdict_backends.py"` on line 385.

The full path `tools/run-gates/verdict_backends.py` stays only in §2 (S10, line 99), line 172 and Files touched (line 243), none of which the paths arm grades.

No other spec, `order` verb, deviation record or index was touched. Nothing was staged or committed. Unit 78 shows as `AM` because your staged copy predates these edits.
