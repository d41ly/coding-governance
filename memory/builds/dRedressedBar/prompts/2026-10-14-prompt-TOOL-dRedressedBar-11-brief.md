# Brief — dRedressedBar: a receipt-reading probe term for govkit's declared outcomes

**Serves:** research TOOL-dRedressedBar-11

## The prompt

> let the canary run, confirm 12-15 then fix all the traced reds

## The brief

### Goal
`TOOL-dRedressedBar-9` declares settings-merge's adopter exit 2 an accepted stop when agent-cap's
hook is absent. The round-1 spec audit found that the absence probe reads fixed paths, and
`TOOL-dRedressedBar-10` S22 narrows it to two. One route stays open after that. agent-cap can be
installed at a home only the target's receipt records. If settings.json is then malformed or cannot
be written, the run exits 2, both probes read absent, and the verb prints a false accepted stop and
swallows the real error. This reaches `update` gaining settings-merge (`govkit.py:11104-11126`) and
`apply --kits settings-merge` over a target that already holds agent-cap (`govkit.py:7740-7764`).
`resolve_kit_dir` reads the receipt first (`settings-merge.py:78-108`). The owner chose to close
every route (§8 F1 of unit 10, option (c), 2026-10-14). Do it with a probe term in
`classify_outcome` (`govkit.py:6313-6324`) that resolves a kit's installed home from the target's
receipt, and use that term in settings-merge's code-2 outcome.

### Items
1. **TOOL-dRedressedBar-11 — a receipt-reading probe term in the declared-outcome contract.** This is
   a new vocabulary in a contract that three verbs read (apply, update, and the matrix). Name the
   term, its grammar, how it resolves when no receipt exists (a fresh apply), and what each verb does
   with it. Find which readers of `[[outcome]]` probes exist and update every one, so no reader
   silently ignores the new term. State what an adopter sees change, and whether a kit version or
   the descriptor schema version moves.
   - Order: after `TOOL-dRedressedBar-9`, whose code-2 block this edits, and after
     `TOOL-dRedressedBar-10`, whose S22 narrowing it builds on. `TOOL-dRedressedBar-7` measures kit
     versions over the fixed tree, so say whether unit 7 must now follow this unit, and name the
     README ordering change that implies.

### Acceptance
A target holds agent-cap at a receipt-recorded renamed home and a malformed `.claude/settings.json`.
`apply --kits settings-merge`, and an update that gains settings-merge, both exit non-zero and name
the adopter's real failure, never the accepted stop. With agent-cap truly absent, the accepted stop
still holds. At `ebce889c`, or over unit 10 alone, the first case prints the false accepted stop.

### Gates
`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)`

### Non-goals
- No change to which kits the registry's default set holds.
- No edit to the units 9 and 10 own beyond the code-2 block's probe and the readers this term needs.

### Limitations
- Children run no bar and no whole suite. The govkit selftest costs 30+ minutes here, so verify with a
  hermetic probe and leave the suite verdict to the main loop.

### Reuse
`classify_outcome` and its existing `must_exist` / `must_not_exist` terms, `resolve_kit_dir`'s
receipt read, `resolve_entry`, and unit 9's `check_outcome_states` helper in `tools/govkit/matrix.py`.

## Drawn from the session

> (c) Narrow + receipt probe
— owner, 2026-10-14, answering unit 10's F1

## Owner confirmation

Asked: Unit 10 (the audit's 23 minor fixes, batched), fork F1 … How should it close?
Answer: (c) Narrow + receipt probe
