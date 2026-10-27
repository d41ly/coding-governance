**Serves:** research TOOL-dSafePassage-35

# Brief: a rollback killed after the schema step's down resumes — TOOL-dSafePassage-70 takes S19, and 35 folds three file-list findings

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-35 back a second time (`wf_bcf396f4-b58`, HEAD `717bf240a`). The run revises the spec under M2.

## The brief

### Goal

A rollback killed between the schema step's down and the stamp can be re-run, and the re-run finishes what the killed run started. That behaviour, and S19/AC17 which observe it, live in one new unit, TOOL-dSafePassage-70. TOOL-dSafePassage-35 keeps every other item, buildable as specced, with its Files touched complete.

**What the builder measured.**

- **The plant.** The builder built the plant `schema-step-kill-shipped-rows` exactly as S19 describes, and ran `python tools/govkit/upgrade_steps.py fixture rollback-update --plant schema-step-kill-shipped-rows`. The log is `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dsafepassage-567339/c5f50d22-89c6-41d7-84e5-2382dcd49faa/scratchpad/s19.log`.
- **The uninterrupted twin rolled back cleanly.** s2, s1 and the schema step all reached `rolled-back`, with exit 0 and schema 3.
- **The killed target's re-run exited 2.** Its error was `govkit: a receipt at schema 3 has no steps to record 'fx/s2' in`. Move 3 of `run_reverse_walk` (`tools/govkit/upgrade_steps.py`, the `write_step_record` of `down interrupted` before the spawn) calls `set_step_state`, which refuses on the schema-3 receipt the killed schema down left behind.
- **Past that refusal, the walk would still stop early.** `if not recordable and n < len(rows): return stop(row, LOWERED_STOP)` would stop at s2, the first of three rows.
- **The re-run's record can never byte-equal the twin's.** On the re-run the schema step's witness no longer holds, so its line reads `skipped (nothing applied)` where the twin's reads `rolled-back`.

**Further findings for 35 itself (none diverges on its own):**
- (a) **S3:** once `read_file_members` always reads the plan, `write_file_plant` (the `file` class's plant in `tools/govkit/step_gate.py`) no longer moves a member, because it removes a receipt row. It has to change too, for example to `git rm` a shipped README. The `file` summary in `tools/govkit/surface-classes.toml` and `help/step-gate.md:15` also describe the receipt source. Neither file is in §4.
- (b) **S22:** `help/python-floor.md:74` spells out `down 3.12 <target> <to>`, so the docs rule puts that page in the write set.
- (c) **S24:** once `resolve_bash` moves, govkit has no reader of `_BASH` left, so binding it back would leave a stale alias. `_BASH` should belong to the step module alone. Check this against the selftest's write at `selftest.py:17330` and `:17338`, which rev-6 already names.

### Items

1. **Author `memory/builds/dSafePassage/spec/2026-10-28-spec-TOOL-dSafePassage-70.md`**:
   - Header: Tier-2, `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 8`, `**Derived:** TOOL-dSafePassage-35`; `consumes-from` TOOL-dSafePassage-2, -4 and -62 (the walk, the rollback and the pre-walk receipt), plus any other unit the reverse walk's code shows it depends on.
   - Its one mechanism: `run_reverse_walk`'s rule on a receipt already below schema 4 when the walk starts. Derive the rule from the code: for example, skip move 3's persist and the `LOWERED_STOP` check and finish to the stamp, or a named alternative. Say why.
   - Carry S19 and AC17 over from 35, restated so the record compare says exactly what equals the twin's. For example: the twin's lines except the schema step's `skipped (nothing applied)`, or only the two shipped rows' down lines plus the `files` and `gov_commit` lines.
   - It needs its red case, §4 Files touched, a `New arm:` line, and a README `roster:units` row.
2. **Revise TOOL-dSafePassage-35** as rev-7, dated 2026-10-28, still `DEFERRED`:
   - Remove S19 and AC17, pointing at TOOL-dSafePassage-70 where a reader needs it.
   - Fold (a), (b) and (c) into §4 Files touched and the items they touch.
   - Add one §9 line naming this brief.
3. **Cross-read** every DEFERRED sibling that cites 35's S19 or AC17, and TOOL-dSafePassage-42. CLOSED specs are read-only.
4. **Commit nothing.** Return the files you wrote.

### Acceptance

- TOOL-dSafePassage-70's spec is conforming: status header, `**Derived:**`, §6 criteria each with a Red-when, §7 with a `New arm:` line, and §10 reuse.
- `grep -n 'S19\|AC17' memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-35.md` prints only pointers to TOOL-dSafePassage-70.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, and no edit to a CLOSED spec.
- No commit and no stage into the real index.
