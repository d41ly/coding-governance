# Revision — dRedressedBar: TOOL-dRedressedBar-19, the builder's divergence (a glob include claims nothing)

**Serves:** research TOOL-dRedressedBar-19

## The brief

### Goal
DIVERGENCE: S29, the `tools/run-gates/kit.toml` row of §4 "The leg's declarations", and AC29 all specify a `[[files]]` rule `include = ["fixtures/measure-legs/**"]` with `role = "project-owned"`, and say it withholds the fixtures. govkit cannot do that. `rule_sources` (tools/govkit/govkit.py:318-334) drops any include element holding a glob character, and only the exact element `**` is read as a wildcard (`resolve_rule_pool` :6603-6625, `scan_claimed_paths` :6628+). So that rule claims nothing, and the `**` engine rule still ships every fixture.

I probed this directly: a `python -c` loaded run-gates' kit.toml, added the spec's rule, and called `scan_claimed_paths` and `resolve_rule_pool`. The other rules claimed 14 paths, none of them a fixture, and all 12 files under `tools/run-gates/fixtures/measure-legs/` stayed in the `**` engine pool. The repo already recorded this exact trap at `tools/runlog/kit.toml:30-34`: "`fixtures/**` here claimed nothing and `plan` put every fixture under `engine`. Measured with `govkit plan`". That kit names each fixture literally.

If built as written, AC29's string check would pass while nothing was withheld. That is a vacuous pass, and S29's claim that adopters do not receive the fixtures would be false.

What the spec has to say instead:
- S29 and the §4 row: the rule names every fixture under `fixtures/measure-legs/` literally, in the form `tools/runlog/kit.toml:35-38` uses. That is 13 files once S32 adds `forks.sh`.
- AC29: the rule's include list equals what `git ls-files tools/run-gates/fixtures/measure-legs` names, and `govkit.resolve_rule_pool` over the `**` engine rule holds no fixture path.
- AC29's red half: the glob spelling leaves all fixtures in the engine pool.
- Optional, for the spec writer to decide: an arm asserting the list still equals the directory, as the runlog selftest does, so a new fixture reds instead of shipping.

I did not build around this. I wrote no file, staged nothing and committed nothing.

### Items
1. **TOOL-dRedressedBar-19** — bump the rev. Take the builder's restatement of S29 as written above: the `tools/run-gates/kit.toml` `[[files]]` rule names every fixture under `tools/run-gates/fixtures/measure-legs/` literally, in the form `tools/runlog/kit.toml:35-38` uses (13 paths once S32 adds `forks.sh`). AC29 reads that the rule's include list equals what `git ls-files tools/run-gates/fixtures/measure-legs` names, and that `govkit.resolve_rule_pool` over the `**` engine rule holds no fixture path; its red half is the glob spelling, which leaves every fixture in the engine pool. Take the optional arm too, because a list typed beside the directory it describes drifts: an arm, in the selftest that already grades this kit's declarations, that reds when the literal list and the directory differ, as the runlog selftest does. Declare it on a `New arm:` line.
2. **The builder's second fix.** `<p19>` stages `tools/gate-legs.json` (S21), which is on the kickoff manifest's watch list, so the staged ratchet leg (`.githooks/pre-commit:188-195`, C5s at `skills/session-kickoff/manifest-check.sh:1582-1593`) refuses it without a `last-audit` re-stamp. S1 and §4's declarations row: `<p19>` carries its own re-stamp naming the sha before it, as unit 18's pass commit did, and `<p19m>` re-stamps naming `<p19>` so AC1 holds. Add `memory/guides/SESSION-KICKOFF.md` to Files touched for `<p19>`.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades unit 19 READY. S29, the §4 row and AC29 name no glob include.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any spec but 19. No status change.
- No merge to local main and no push without the owner's ask.
