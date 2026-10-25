# TOOL-dGroundRules-70 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-70

The acceptance criteria were observed by this unit's builder through the probes its spec names; its build commit carries them. This ledger holds the close's suite-arm observation.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Under the suites, observed by the main loop in scratch clones of `df4912bda`, `4f76c4b39` or `3d86915cf`, each break staged alone and restored: tools/unattended/unattended.test.sh --shard 4/8 at fce5603f8 with verb_dispatch's `sibrows=$(read_open_passes "$rel")` staged to `sibrows=$(awk NF "$rel")`: `FAIL the driver's five readers call it or read_open_passes rather than parsing the rows their own way: expected [5], got [4]` (with the dispatch arms it also breaks, e.g. `FAIL missing: no sibling pass is open`). The second arm, with read_open_passes' own `read_pass_declarations "$1"` call staged to `awk NF "$1"`: `FAIL and read_open_passes itself calls it, so the two readers it serves reach the same derivation: expected [1], got [0]`. GREEN at fce5603f8 `PASS (596 assertions)`.
