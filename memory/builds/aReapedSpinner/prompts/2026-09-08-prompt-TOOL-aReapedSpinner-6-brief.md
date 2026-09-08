# Brief — TOOL-aReapedSpinner-6, the kit skeleton

**Serves:** journal TOOL-aReapedSpinner-6

What this pass was handed: the unit's spec at rev-4, the three spec audits and their folds, and
`tools/drift-audit/` as the structural sibling to copy the descriptor and adopter shape from.

What it builds: `tools/process-monitor/` as a declared govkit entry with NO engine. `kit.toml`,
`.process-monitor.conf`, `adopt-process-monitor.sh` with its non-repairing `--check`, its test
suite, a README stating what the kit does not check, and one `[[entry]]` row in
`tools/govkit/registry.toml`.

The four things that are not obvious, each from an audit finding:

- **`version_from` pins at `adopt-process-monitor.sh`**, not at any `.py`. This unit is forbidden
  from shipping an engine file, and `govkit.py:1194` reds on a `version_from` naming an absent
  file — which would red `govkit selfcheck` and `kit version markers` on every bar until unit 1
  lands, since both are `subject: repo` with no guard (D1).
- **`PROCMON_ROOTS` names no temp or scratch directory**, and AC8's arm asserts it. Every Bash-tool
  shell on this machine carries an `export TEMP=` assignment naming the user's temp directory, so a
  root under it admits every agent session on the box (D11, D16).
- **The roots-admit-this-repo assertion is NOT here.** It needs a census and a closure, neither of
  which exists at `order 1`; it is unit 2's AC15 (D36).
- **The hook's `[[files]]` row is NOT here either.** Unit 5 ships that file and adds its own row;
  declaring a destination for a file no unit has shipped reds the `hook destinations` leg on every
  bar until unit 5 lands (D23).

The unit must land GREEN on a full bar with no engine file present. That is AC6, and it is what
makes the rest of the build's ordering possible.
