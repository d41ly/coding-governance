**Serves:** research DEPL-dShippedRelease-1 DEPL-dShippedRelease-4

# dShippedRelease — the re-ground writer's return, verbatim

The `gov-spec-writer` return for the re-ground brief [`2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground`](../prompts/2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground.md), extracted by script from the agent's transcript and not retyped. The cross-check record it folds is [`2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck`](2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md).

## Spec 4

I've fixed the stale citation in DEPL-dShippedRelease-4, and there were no other moved citations to fix.

Spec: `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dShippedRelease\spec\2026-10-30-spec-DEPL-dShippedRelease-4.md`

**Row 10 (edited):** first I checked it against wm58 at `66c5b8dbf`. The last commit to touch that file is `66f7b8d32`, and the worktree copy matches. wm58:288 is now AC3's `not-holder` line. The `not-closing-verb` assertion for `deploy.unlease` is in AC4, at wm58:290-295 (the clause is at :292-293). In §8 F5, sr4:398 changed from "its acceptance at `:288` asserts" to "its acceptance's AC4 asserts". Nothing else in F5 changed: it stays RESOLVED (a) and its ask is untouched.

**Status line:** now `DEFERRED · rev-5 · 2026-11-03`, with every other field as it was.

**§9 line added:** `- rev-5 · 2026-11-03 · §8 F5 · the citation of TOOL-dWellOiledMachine-58's `not-closing-verb` assertion for `deploy.unlease` moves from a line number, which that spec's rev-5 renumbered onto AC3's `not-holder` line, to its section AC4, by the brief prompts/2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground.md`. I left the old `:288` out of this line on purpose, so the "no `:288` citing wm58" check holds.

**No other moved citations:** I searched the spec for every `:<line>` citation. None of the others points at wm58 or wm6. They cite `unattended.sh`, `lib-unattended.sh`, `layer-memory.md` and `flow-steps.md`, which are outside this brief. The spec cites wm58 and wm6 everywhere else by section (S5, S6, S9, wm6 S8).

**Refused rows:** none.

**Acceptance results:**
- `wc -c` is 39593, under 49152.
- `grep -n ':288'` prints nothing.
- The hygiene gate, run with `--staged` on a throwaway index copy (since deleted), exited 1 on one finding only, which names nothing in the spec itself. Check 9 reports the build index needs re-rendering because the spec is an input to it: `memory/LIVE.md` and `memory/builds/dShippedRelease/README.md` are stale. Only `gen_build_index.py --write` fixes that, so I left it for the main loop.

I made no commit and staged nothing into the real index.
