# Brief — dRedressedBar: the runner scripts' fixed-name temp writers, H1's class on the bash side

**Serves:** research TOOL-dRedressedBar-24 TOOL-dRedressedBar-21

## The prompt

> Own unit, this build

The owner's answer, 2026-10-15, to spec 21 §8 F1: where the bash fixed-name temp-then-replace writers go.

## The brief

### Goal
Unit 21 removes H1's fixed-name temp pattern from every Python writer under `tools/run-gates/`. Its writer found the same pattern on the bash side: 19 `mv` sites across `tools/run-gates/run-gates.sh`, `tools/run-gates/post-merge.sh` and `tools/run-gates/run-selftests.sh`, plus one Python writer inside a `run-gates.sh` heredoc. Some write under `$WORK`, which sits in the shared temp dir, so the attacker H1 describes can plant a link at the fixed temp name. Give each of them an unpredictable temp, and gate the class with a bash-side static check so a new fixed-name temp writer reds.

### Items
1. **TOOL-dRedressedBar-24** — a new spec, order after unit 23. Enumerate every site from the tree with grep, never from this brief's count, and say which sit under a directory another user can write and which do not. Spec the fix per site (an `mktemp` in the destination's own directory is the usual shape), the static check (which file it lives in, which leg runs it, its population, its red half observed on today's tree), and the leg declarations it needs, each with a `**Readers:**` clause where a name retires. The runner is shipped, so name the kit version move and the manifest re-stamp the pre-commit ratchet will demand for `run-gates.sh`. Mind the two runner hazards the repo records: editing `run-gates.sh` while a bar runs voids that bar, and a long `case`/compound block can hit the Cygwin bash stack ceiling.
2. **TOOL-dRedressedBar-21** — mark §8 F1 `RESOLVED (owner, 2026-10-15): (a)` in place, add the `hands-off TOOL-dRedressedBar-24` edge in §3 (with unit 24's mirrored `consumes-from`), and drop the external hand-off it replaces. Spec 21 is committed at rev-1 and unbuilt, so give it a rev bump and a §9 line.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades units 21 and 24 READY, unit 24 ordered after unit 23.

### Gates
`memory hygiene` · `lexicon naming predicates`

### Non-goals
- No code. No edit to any spec but 21 and 24. No status change.
- No `tools/unattended/` self-test suite runs (standing owner instruction, 2026-08-23).
- No merge to local main and no push without the owner's ask.
