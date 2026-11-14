**Serves:** research TOOL-aLightenedLoop-2

# Bar fix — TOOL-aLightenedLoop-2: two reds the merge bar found in the `--wake` unit

## The prompt

> Done means: the build folder and the four specs committed through `/build`, with READY → go, the units built, the closing review and the bar run, then the owner asked to land.

## The brief

### Goal
The merge bar at `9347f5848` read two of its four red legs in TOOL-aLightenedLoop-2's own changes. Fix both in one pass of this unit, with every touched check's verdict, refusal text and rendered bytes otherwise unchanged. The other two reds are already fixed.

### Items
1. Leg `policy check`, arm `arm_legacy_homes`, printed exactly: "legacy homes: stale list at .unattended.conf KEEPALIVE_TRACKED_INTERVAL owner-policy, re-run lists --write" and ".unattended.conf KEEPALIVE_TRACKED_INTERVAL is a new legacy home and the list is shrink-only; carry it as a key in tools/policy/catalogue.toml instead". The new tracked cadence must be a key of the policy catalogue (`tools/policy/catalogue.toml`), read through the policy reader the way other catalogue keys are read. It must not be a new `.unattended.conf` key. Carry its declaration, its reader in `tools/unattended/unattended.sh`, this repository's value of every 30 minutes (cron 7-59/30), and every place unit 2 named the conf key (the conf example, `kit.toml`'s optional keys, protocol §8's row, the Skill and verbs templates and their renders, `help/idle-wake.md`, the feature dossier) over to the catalogue key. `--wake`'s output and its cadence answers must stay exactly as unit 2's ledger records them. `KEEPALIVE_INTERVAL` stays where it is, as a grandfathered legacy home.
2. Leg `help page commands` printed exactly: "docs: RUN help/idle-wake.md:61 the block of 1 command(s): exited 127, the block declares 0: bash: tools/unattended/unattended.sh: No such file or directory". The page's command block runs a kit by its path in gov's checkout, which a scratch adopter does not have. Mark it as the other help pages mark such blocks (`run: no` with its reason), or make it run in an adopter, whichever the docs leg's grammar admits for this page.

### Acceptance
`python tools/policy/check_policy.py`, or the `policy check` leg's argv, prints no `arm_legacy_homes` finding. The `help page commands` leg's argv prints no finding for `help/idle-wake.md`. `--wake` gives the same lines as before, in the same three setups unit 2's ledger used. The pass ledger records each observation.

### Gates
The merge bar at the close.

### Non-goals
No change to `--wake`'s verdicts or text. No new legacy home. No other key moved.

### Limitations
The build brief's limitations hold: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-1-brief.md`.

### Reuse
Any catalogue key the unattended kit already reads through the policy reader, found with `python tools/codebase-map/reuse_lookup.py "read an unattended conf value from the policy catalogue"`.
