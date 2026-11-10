# Promotion brief — aSmoothedDispatch: three bar legs this build turned red

**Serves:** research TOOL-aSmoothedDispatch-18

## The brief

### Goal
The bar at `e1781668e` (`bash tools/run-gates/run-gates.sh`) failed 5 of 69 legs, all from this build. Spec 5's missing edge and the driver's refusal ceiling are now fixed (`1038ada92`, `0b5c6db20`). This unit clears the other three legs, `shell hygiene (a loop fed by a command substitution)`, `install-prefix (shipped surface)` and `docs`, without changing what any unit's refusal or split decides.

### Items
1. Shell hygiene. Unit 1's split in the `--writes)` arm of `tools/unattended/unattended.sh` reads each value with `IFS=$' \t\n' read -r -d '' -a _dw <<<"$1"`. The leg's registry pins the driver's `<<<` sites at 2, and the scan now measures 3: "the count may fall with the sites and may not rise". Split the value without a here-string, keeping unit 1's behaviour exactly. Space, tab and newline separate. A carriage return, a vertical tab or a form feed stays inside a path. No glob expands. No IFS or shell-option change leaks past the split. A value with no field still adds one empty path.
2. Install-prefix. Four test lines spell a kit path, and the leg is a pure ban with no waiver: `tools/hooks/scratch-guard.test.sh:1180` (a `reason tools/` text in a dispatch-row fixture), `tools/unattended/unattended.test.sh:7655` and `:7707` (`run-gates/gate-fingerprint.sh` copied and removed in unit 4's cache fixture), and `tools/unattended/unattended.test.sh:7739` (a stub printing `spec-tokens: tools/x.md`). Derive each kit path from the suite's own location or through `resolve_kit_dir`, or respell a fixture text so it names no kit path. Every arm keeps asserting what it asserts.
3. Docs. The `docs` leg reports `UNDOCUMENTED verb:unattended.sh:--help: anchored on no page under help/`. Unit 3 added `--help`; anchor it on the help page that documents the driver's verbs, in that page's existing anchor form.

### Acceptance
The three legs' own commands exit 0 over the tip, run by the main loop. Item 1 also keeps the driver suite's region-four `--writes` arms green, and they still red on unit 8's staged breaks. Item 2's respelled arms still red on the breaks recorded for them in the acceptance ledger.

### Gates
shell hygiene, install-prefix, docs, the unattended kit self-test (regions 3 and 4) and the hooks scratch-guard self-test; then the full bar once.

### Non-goals
Any change to what a refusal refuses or to its message. The refusal ceiling and spec 5's edge, both done. The inherited suite reds filed as asks 10 to 13.
