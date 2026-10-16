# Brief — dRedressedBar: agent-cap's install command names another kit's file at its own prefix

**Serves:** research TOOL-dRedressedBar-15

## The prompt

> add the apply prefix defect as unit 12

## The brief

### Goal
`TOOL-dRedressedBar-14`'s writer split the apply-prefix reproduction into two causes. Unit 14 fixes
settings-merge's exit 2, the receipt being absent during CONFIGURE. agent-cap's exit 2 is this
unit's. agent-cap's adopter argv is `python {prefix}/settings-merge.py` (`tools/hooks/kit.toml:108`).
`{prefix}` fills from agent-cap's OWN per-kit prefix, so with `[kit.agent-cap] prefix = "scripts"` it
runs `scripts/settings-merge.py`, a file the settings-merge kit never installed there. It fails with
python's "can't open file", even with a receipt on disk. The writer measured it as the only adopter
argv in the registry that names another kit's file. Fix it, so the reproduction exits 0.

### Items
1. **TOOL-dRedressedBar-15 — agent-cap's adopter resolves settings-merge at settings-merge's own
   home.** The owner chose this as its own unit (§8 F1 of unit 14, option (a), 2026-10-14). Find the
   candidates and the test each could lose (BUILD-METHOD M12), and choose by M3's rule. Candidates
   include:
   - a token that resolves another kit's prefix in an argv, such as `{prefix:settings-merge}`, if
     the descriptor grammar has or can take one;
   - agent-cap carrying no adopter of its own and relying on settings-merge's;
   - resolving the script through the receipt at run time.

   Gate the class, not the instance: a check that no adopter argv names another kit's file through
   its own `{prefix}`, run over the real registry first. State what an adopter sees change. This
   unit moves agent-cap's (the hooks kit's) shipped bytes, and it is ordered after
   `TOOL-dRedressedBar-7`, which measures kit versions. So this unit bumps the hooks kit version
   itself, and says so.
   - Edges: `consumes-from TOOL-dRedressedBar-14`, after whose receipt fix the reproduction's only
     remaining exit 2 is this one.
   - Order: after `TOOL-dRedressedBar-14` (order 10).

### Acceptance
`apply --kits agent-cap,settings-merge,kickoff-manifest` with `[kit.agent-cap] prefix = "scripts"`,
on a scratch target under `%TEMP%/<short-name>`, exits 0 over units 14 and 15. The receipt rows the
hook at `scripts/hooks/agent-cap.js`, and `.claude/settings.json` wires it. Over unit 14 alone it
exits 1 with agent-cap's adopter at exit 2 and "can't open file". The default-prefix apply is
unchanged.

### Gates
`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `hook destinations self-test` · `agent-cap self-test`

### Non-goals
- No change to which kits the registry's default set holds.
- No edit to unit 14's receipt write.

### Limitations
- Children run no bar and no whole suite. The govkit selftest costs 30+ minutes here, so verify with a
  hermetic probe and leave the suite verdict to the main loop.

### Reuse
The descriptor grammar's token resolution in `tools/govkit/govkit.py`, `resolve_kit_dir`, and unit
14's scratch targets `%TEMP%/drb14` (per-kit prefix) and `%TEMP%/drb14d` (default prefix).

## Drawn from the session

> (a) Its own unit (Recommended)
— owner, 2026-10-14, answering unit 14's F1

## Owner confirmation

Asked: Unit 14 (apply at a per-kit prefix), fork F1 … Where should that second bug go?
Answer: (a) Its own unit (Recommended)
