# Brief — dRedressedBar: a first apply at a per-kit prefix configures before the receipt exists

**Serves:** research TOOL-dRedressedBar-14

*Re-id: drafted as unit 12. The round-2 spec audit's disposal claimed ids 12 and 13 in the same
minute, so the writer was redirected to 14 before it wrote anything. Its handoff record keeps the id
it was rendered with, `prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-1-spec-writer.md`.*

## The prompt

> add the apply prefix defect as unit 12

## The brief

### Goal
`TOOL-dRedressedBar-11`'s writer measured a defect at spec time and recorded it as an external
hand-off in that spec's §3 Edges. A first `govkit apply` that selects agent-cap with
`[kit.agent-cap] prefix = "scripts"` in its deploy exits 1, and both adopters, agent-cap's and
settings-merge's, exit 2. apply's CONFIGURE step runs the adopters before the receipt is written.
settings-merge.py finds the hook through `resolve_kit_dir("hooks", "agent-cap.js", <its own dir>)`
(`tools/settings-merge.py:192`), which reads `.governance/install.json` first. With no receipt yet,
it looks only at the static homes, so a hook installed at the per-kit prefix
(`scripts/hooks/agent-cap.js`) is not found. The install is real but the apply fails. Fix it, so a
first apply at a per-kit prefix exits 0 with both adopters wired.

### Items
1. **TOOL-dRedressedBar-14 — a first apply at a per-kit prefix configures against the homes it just
   wrote.** Reproduce it first on a scratch target under `%TEMP%/<short-name>`:
   `apply --kits agent-cap,settings-merge,kickoff-manifest` with `[kit.agent-cap] prefix = "scripts"`.
   Then find the candidates and the test each could lose (BUILD-METHOD M12), and choose by M3's rule.
   Among the candidates:
   - write the receipt, or a provisional one, before CONFIGURE runs;
   - hand the adopters the planned homes, through the environment or an argument;
   - run CONFIGURE after the receipt write.

   State what the order change does to a CONFIGURE that fails: what the receipt then claims, and
   whether a re-run recovers. State what an adopter sees change. Name every reader that assumes the
   receipt is absent during CONFIGURE.
   - Edges: `consumes-from TOOL-dRedressedBar-11`, whose `must_not_resolve` term reads the same
     receipt, so its acceptance must still hold over this fix. Spec 11's external hand-off line for
     this defect becomes a `hands-off TOOL-dRedressedBar-14` line; the main loop makes that edit.
   - Order: after `TOOL-dRedressedBar-11`. Say whether `TOOL-dRedressedBar-7`'s version measurement
     covers the files this unit moves, and name the README ordering change if it does not.

### Acceptance
At the base, the reproduction exits 1 with both adopters at exit 2. Over the fix, it exits 0, the
receipt rows the hook at `scripts/hooks/agent-cap.js`, and `.claude/settings.json` wires it. The
default-prefix apply is unchanged. Unit 11's AC that reads a receipt-recorded renamed home still
holds.

### Gates
`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)`

### Non-goals
- No change to which kits the registry's default set holds.
- The stderr-tail helper consolidation, the other external hand-off in spec 11, is not this unit.

### Limitations
- Children run no bar and no whole suite. The govkit selftest costs 30+ minutes here, so verify with a
  hermetic probe and leave the suite verdict to the main loop.

### Reuse
apply's CONFIGURE and receipt-write steps in `tools/govkit/govkit.py`, `resolve_kit_dir` and its
inlined copies, and the `stale_target` and `make_target` fixtures in `tools/govkit/selftest.py`.

## Drawn from the session

> add the apply prefix defect as unit 12
— owner, 2026-10-14

## Owner confirmation

Asked: (the owner's own instruction)
Answer: add the apply prefix defect as unit 12
