**Serves:** research TOOL-aLightenedLoop-7

# Cadence drop — TOOL-aLightenedLoop-7: the tracked idle-wake cadence retired, and the help page's block marked

## The prompt

> Unit 2's new `KEEPALIVE_TRACKED_INTERVAL` conf key reds the policy check: a new key must be a policy-catalogue key, not a new `.unattended.conf` legacy home, and that list is shrink-only. How should the tracked idle-wake cadence be declared?

Answer: "Drop the tracked cadence"

## The brief

### Goal
Retire the longer-cadence half of TOOL-aLightenedLoop-2 and keep its cheap `--wake` tick. The merge bar at `9347f5848` redded two legs on unit 2's changes. Unit 2's fix pass diverged on the first, because moving the key to the policy catalogue is a redesign: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-2-bar-fix.md`. The owner chose to drop the key instead. Unit 2's spec is CLOSED and frozen, so this unit corrects it on top.

### Items
1. Remove `KEEPALIVE_TRACKED_INTERVAL` from everything that carries it: the driver's init block and every reader in `tools/unattended/unattended.sh`, `tools/unattended/.unattended.conf.example`, `tools/unattended/kit.toml`'s optional keys, this repository's `.unattended.conf`, the protocol §8 row, the Skill, verbs and protocol templates and their rendered copies, `help/idle-wake.md`, and the feature dossier. Afterwards `git grep KEEPALIVE_TRACKED_INTERVAL` names only records under `memory/builds/`.
2. `--wake` keeps its HEALTHY/FULL verdicts, reasons and order exactly as unit 2's first acceptance ledger records them. Its cadence field always names the base `KEEPALIVE_INTERVAL`, or `undeclared` when that is blank. The spec states the line's exact new form and arms it.
3. The suite arms that set or read the tracked key are retired or rewritten to the base-cadence answer, with the assertion floor moved by the measured count.
4. `help/idle-wake.md`'s command block is marked as the other help pages mark a block that runs a kit by its path in gov's checkout, e.g. `<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->` (as on `help/agent-limit.md`).
5. Any size row unit 2 raised that now has headroom is left as it is. Lowering a row is the owner's, per `tools/template-size-limits.txt`.

### Acceptance
The `policy check` leg's `arm_legacy_homes` prints no finding. The `help page commands` leg prints no finding for `help/idle-wake.md`. `git grep -n KEEPALIVE_TRACKED_INTERVAL -- tools help .claude .unattended.conf memory/guides memory/map` prints nothing. `--wake`'s verdict lines are unchanged in unit 2's setups, apart from the cadence field the spec states. Every touched pre-existing check keeps its verdict and bytes.

### Gates
The merge bar at the close.

### Non-goals
No change to `--wake`'s verdicts, reasons or their order. No new key anywhere. `KEEPALIVE_INTERVAL` stays as it is.

### Limitations
The build brief's limitations hold: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md`.

### Reuse
Unit 2's `--wake` arms in `tools/unattended/unattended.test.sh` and its acceptance ledger.
