**Serves:** research KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-5 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-14 KICK-dKeptSession-28

# Fix brief — dKeptSession, the eleven findings the main loop's checks raised over the 28 authored specs

The five writers of `unattended-build.js` run `wf_a0e6e1c9-cf1` authored the 28 specs under
`memory/builds/dKeptSession/spec/`, staged and not committed. The main loop then ran `tools/check-spec-tokens.py`
(10 unwaived hits) and `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` (check 25 on one spec).
`carries.py --report dKeptSession` reads all 28 clauses carried whole and all 16 owned nodes named: keep it so.

Fix exactly these findings, in place, in the spec named, keeping every clause token, `**Carries:**` line, §3 edge and
§8 mark as it stands. The specs are uncommitted, so they stay `rev-1`: change no status header. Write nothing else,
commit nothing, and return each finding with what you changed. The spec brief,
`memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md`, still binds every rule.

## The findings

1. `2026-10-26-spec-KICK-dKeptSession-1.md` · `[path]` · `tools/loop/loop.toml` is cited where the checker grades paths
   (§6), and no such file is tracked. Cite it by basename (`loop.toml`) in §6, keeping the full path in §2, §4 and
   Files touched.
2. `2026-10-26-spec-KICK-dKeptSession-11.md` · `[guards]` · §4 Files touched names `tools/playbook/`, which trips the
   guards of the legs `govkit acceptance matrix` and `playbook render selftest`, absent from the §7 leg line. Name
   the exact file the unit edits in place of the directory, and add each leg whose guard that file still trips to
   the §7 leg line, spelled as `tools/gate-legs.json` names it.
3. `2026-10-26-spec-KICK-dKeptSession-12.md` · `[path]` · `@.claude/orientation-card.md` reads as an untracked path.
   It is an import line, not a file this unit cites: describe it without a path-shaped token in backticks (for
   example, the `CLAUDE.md` import line naming the card file), or cite the card file by basename.
4. `2026-10-26-spec-KICK-dKeptSession-28.md` · `[guards]` · Files touched names `tools/playbook/render_playbook.py`,
   which trips `govkit acceptance matrix` and `playbook render selftest`: add both to the §7 leg line.
5. `2026-10-26-spec-KICK-dKeptSession-5.md` · `[guards]` · Files touched names `tools/govkit/subject-pins.tsv`, which
   trips `govkit selftest`, `govkit refusal join` and `govkit acceptance matrix`. If the unit truly edits that file,
   add all three to the §7 leg line; if it does not, drop the path from Files touched and say why in §9.
6. `2026-10-26-spec-KICK-dKeptSession-14.md` · `[handoff]` · its §3 hands `derive_context_tokens` to
   KICK-dKeptSession-9, and KICK-dKeptSession-9's spec never names it. KICK-9 reads `derive_context_fill` (the writer's
   return): either name `derive_context_tokens` where KICK-9 reads it, if it does, or correct KICK-14's bullet to the
   token KICK-9 reads, keeping the pair reciprocal (KICK-9's `consumes-from` names the same token).
7. `2026-10-26-spec-KICK-dKeptSession-2.md` · hygiene check 25 · §2 item S2's `**Readers:**` clause lists, by name,
   `tools/policy/policy.py`, `read_default_value`, `tools/policy/check_policy.py`, `run_resolution_order`,
   `preset-named`, `help/policy.md`, `tools/policy/README.md`, `branch/unattended-dgroundrules-e47ae1` and
   `3c8c4718a`, none of which a tracked reader spells: they are dGroundRules' unlanded bytes. Write
   `READER NOT IN TREE` and the reason on that half (the readers live on dGroundRules' unlanded branch at
   `3c8c4718a`, and the build run re-grounds on its landed bytes), in the shape
   `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md` S6 already uses and check 25 accepts.

When done, run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm it prints no finding on
a dKeptSession spec. The main loop re-runs `check-spec-tokens.py`.
