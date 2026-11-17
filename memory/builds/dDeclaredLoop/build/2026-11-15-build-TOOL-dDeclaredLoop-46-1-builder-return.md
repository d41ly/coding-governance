**Serves:** journal TOOL-dDeclaredLoop-46

# Builder return — TOOL-dDeclaredLoop-46, dispatch 1: the run-gates version the spec mints is already shipped on origin/main

## Why

DIVERGENCE: §2 S1, §4 Evidence (second bullet) and §6 AC1 (its figure line and Red-when). The spec says the runner reads KIT_RUN_GATES_VERSION=1.47 "and origin/main reads the same, PINNED 2026-11-15", and S1 takes "the value this pass finds" plus one as both the new version and STAGE_FLOOR_RUN_GATES. That premise is no longer true. The branch still reads 1.47 (tools/run-gates/run-gates.sh line 36 at base 9c320b83f). But origin/main at 179486e8f reads `KIT_RUN_GATES_VERSION=1.48   # gov:kit run-gates@1.48`, which the aMeasuredDrag landing 30bb17eb4 minted on 2026-11-15. Both of origin/main's canary KNOWN copies (tools/run-gates/run-gates.test.sh, the two `KNOWN = {` lines) list 14 keys and no `stage`. Built as written, S1 gives 1.48 and STAGE_FLOOR_RUN_GATES = (1, 48). That floor names a runner the default branch has already shipped, and its canary refuses `stage`. An adopter that installed from origin/main would then receive `stage` rows from this emitter and its canary would fail. AC1's Red-when names this exact case ("the floor names a version whose canary lacks `stage`"). It also gives two branches the same number with different bytes, the 1.30 + 1.30 collision the runner's own history comment records. To be buildable, the spec needs four changes. (1) S1: the new version is one above the higher of the branch's value and the default branch's (origin/main) value. Today that is 1.49, and STAGE_FLOOR_RUN_GATES is that tuple. (2) §4 Evidence: re-pin the origin/main reading (1.48 at 179486e8f, canary without `stage`). (3) AC1: derive its starting figure from the higher of the two values. (4) §5 risks or AC1: say how the floor stays above every shipped version that lacks the admission if origin/main mints again before this lands. For example, a close-time probe could compare the floor with origin/main's runner version and canary. I checked the spec's other claims against the tree and they hold. No product path was edited, so there is nothing to restore and no patch file.

## Summary

I stopped before any write. Nothing was dispatched, recorded or committed, and no path changed. The pass started at 9c320b83f851be61243169b765ca3b4bf05e4d4d.

**What blocks the build:** the run-gates version the spec picks is already taken. origin/main (179486e8f) shipped run-gates 1.48 on 2026-11-15, and its canary does not admit `stage`. S1 as written also yields 1.48, so the new stage floor would point at a runner that rejects the key. The full divergence and the four spec changes it needs are in `why`.

**What I checked, as read-only probes (no gate, suite or bar ran):**
- **Canary admission (part of AC1):** both `KNOWN` lines in tools/run-gates/run-gates.test.sh already carry `stage`, as unit 4 left them.
- **Population (stands in for AC2's tomllib probe):** every `[[gate_leg]]` table, joined to tools/gate-legs.json by name, gives 70 tables in 27 PINNED files, 11 of them under tools/govkit/entries/. Every manifest row carries `stage` and no table does yet. This matches S2.
- **govkit.py code:** `check_target_reads_subject`, the three existing floors and the `write_gate_legs` row order match §4. One build note: the ceiling keep rule can append `ceiling` after any key set earlier. To keep `stage` last, it has to be set after the keep rule, on the row already placed in `existing`.
- **7h:** `manifest_ceiling` and the `impure` presence-included compare are where §4 places them.
- **Self-test edits:** the staged edits in `check_benched_probe_arms` (`name`/`subject` and `ceiling = 1780` in tools/govkit/entries/push-main.kit.toml) would still match once if `stage` is the table's last key.
- **Kickoff manifest:** the watch line names run-gates.sh, so the re-stamp is owed.
- **Budgets:** no `[[gate_leg]]` key-set validator exists. The refusal ceilings cover only the unattended scripts, and memory/DECISIONS.md is not needed. memory/map/generated/symbols.json carries no line numbers. No new function, verb or flag is planned, so the lexicon and help-anchor budgets are not reached.

**Owed at the close once a revised spec is built:** observing AC2 and AC4 through `govkit selfcheck`, and the RED-first observation of the spec's one `New arm:` line (tools/govkit/selftest.py: `check_ceiling_emission` and `check_benched_probe_arms`). Nothing timed out or was skipped.
