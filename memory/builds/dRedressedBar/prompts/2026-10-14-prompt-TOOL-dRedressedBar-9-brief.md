# Brief — dRedressedBar: govkit update's gained settings-merge refuses without agent-cap

**Serves:** research TOOL-dRedressedBar-9

## The prompt

> let the canary run, confirm 12-15 then fix all the traced reds

## The brief

### Goal
`TOOL-dRedressedBar-3`'s §4 S5 traced a product defect in `govkit update`. Since TOOL-aRoutedQuill-5
S4, a writing update installs every entry the registry's default set gained since the receipt's
`gov_commit` (`tools/govkit/govkit.py:8863-8879`, `derive_default_gained` at `:970`). The requirement
filter drops `agent-cap`, which requires `kickoff-manifest` (`tools/hooks/kit.toml:9`), whenever the
receipt does not claim `kickoff-manifest`. It keeps `settings-merge`. `settings-merge`
(`tools/govkit/entries/settings-merge.kit.toml`) and `agent-cap` (`tools/hooks/kit.toml:102-108`)
share one adopter argv, `python {prefix}/settings-merge.py`. That adopter wires the built-in
`agent-cap.js` entry and refuses when the file is absent (`tools/settings-merge.py:1040-1052`). So the
update exits 2 at `default-gained settings-merge: adopter exit 2`, fails, and never re-stamps. Every
writing update against any receipt that does not claim `kickoff-manifest` fails this way. Fix it.

### Items
1. **TOOL-dRedressedBar-9 — a gained `settings-merge` no longer fails an update that left `agent-cap`
   out.** The owner chose to fix this in this build (§7 F1 of unit 3, option (c), 2026-10-14). Candidate
   mechanisms the unit-3 writer named:
   - leave `settings-merge` out of the gained set whenever `agent-cap` is left out for an unmet
     requirement, a requirement-closure rule in the gaining;
   - give `settings-merge` no adopter of its own, or one that does not presume `agent-cap.js`.

   Find the candidates and the test each could lose (BUILD-METHOD M12), and choose by M3's rule. A
   change to a kit's contract or to the deployer's gaining rule is in scope by the owner's ruling.
   State what an adopter sees change. Its witness is the three govkit selftest arms unit 3 leaves
   unscoped (`and re-stamps the receipt at the new commit`, `[-12] AC4 NEGATIVE`,
   `[-12] AC9 NEGATIVE`), which must read green over the fix, plus a new arm reproducing the
   narrow-receipt update that fails at the base.

### Acceptance
A writing `govkit update` over a receipt that claims `check-wiring` alone and predates the default
set's widening exits 0 and re-stamps the receipt. At `ebce889c` the same call exits non-zero with
`default-gained settings-merge: adopter exit 2`. The three unscoped arms read green.

### Gates
`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `receipt sync (installed files match the receipt)`

### Non-goals
- No edit to `tools/govkit/selftest.py` beyond the new witnessing arm: unit 3 owns that file's
  re-arming and lands after this unit.
- No change to which kits the registry's default set holds.

### Limitations
- Children run no bar and no whole suite. The govkit selftest costs 30+ minutes here, so verify with a
  hermetic probe of the update path, and leave the suite verdict to the main loop.

### Reuse
`derive_default_gained` and the requirement filter beside it; `apply`'s requirement-complete
selection, which never meets this defect; the unit-3 spec's §4 S4 and S5 analysis.

## Drawn from the session

> (c) Scope + fix the bug here
— owner, 2026-10-14, answering unit 3's F1

## Owner confirmation

Asked: govkit selftest, fork F1 … What should this build do?
Answer: (c) Scope + fix the bug here
