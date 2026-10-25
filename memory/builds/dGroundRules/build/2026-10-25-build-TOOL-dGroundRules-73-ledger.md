# TOOL-dGroundRules-73 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-73

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: `python tools/policy/check_policy.py --fixture limit-hook-landed-unread` with tools/hooks/agent-cap.js at b8378b2bd^: `limit-hook-landed-unread · no remote, on master · a Workflow call · WRONG: exit 2` (the settings remedy) and the one-remote state the same; with tools/policy/policy-shim.sh at b8378b2bd^: both refusing states `WRONG: exit 2` naming the unread landed limit; `--fixture mirror-landed-parity` with the shim at b8378b2bd^: the `no remote, on master` and `one remote, no remote HEAD, on master` states WRONG on the whole-line judge. GREEN: the fixture greens and `agent-cap.test.sh` `---- 363 passed, 0 failed ----` at 59f02fde9.
