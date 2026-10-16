# Brief — dRedressedBar: the landing bar's install-prefix red, the two kit-path spellings units 10 and 14 wrote

**Serves:** research TOOL-dRedressedBar-28

## The prompt

> land it without self tests

The owner's ask, 2026-10-16. `bash tools/push-main.sh --land --slug dRedressedBar` over the prepared merge `30466e129` ran the bar with self-tests held and refused the push: 3 of 71 legs red, every one attributed OWN. Two are records (this README's `## Build-level rules` slot over its 1800 B ceiling, and the kickoff manifest's `last-audit` stamp behind a changed `tools/run-gates/run-gates.sh`) and are fixed in records commits. The third is product code and is this unit.

## The brief

### Goal
The `install-prefix (shipped surface)` leg, `tools/check-install-prefix.sh`, reds at the prepared merge with two kit-path spellings on two lines:

```text
  tools/govkit/entries/settings-merge.kit.toml:48  hooks  probe = { must_exist = "{prefix}/settings-merge.py", must_not_exist = ["{prefix}/hooks/age
  tools/govkit/govkit.py:7950  hooks  # ---- prefix = "scripts"` landed the hook at `scripts/hooks/agent-cap.js`, and settings-m
install-prefix: RED — 406 tracked file(s) graded, 7 render(s) left out as matching their template, 2 kit-path spelling(s) on 2 line(s)
```

Both lines are this build's: the descriptor line from units 10 and 11 (`07feb3b38`, `b65688cde`), the comment from unit 14 (`109fbb4ab`). The ban is pure, with no waiver: a kit segment drains only behind `{prefix}/`, `{kit}/`, `{{TOOL_ROOT}}`, `<prefix>/` or `<tool-root>/` (`tools/check-install-prefix.sh` rule 5, `DRAINED`). Make the leg green by fixing the two spellings at their root, with no change to the checker.

### Items
1. **TOOL-dRedressedBar-28 — order after unit 27.**
   - **The descriptor.** The hit is the `must_not_exist` element `"{prefix}/../hooks/agent-cap.js"`: its `hooks/` follows `../`, not a drained token. One candidate, for the spec to confirm or refute against the code: the term is redundant. `must_not_resolve = "{prefix}/hooks/agent-cap.js"` calls `resolve_kit_dir("hooks", "agent-cap.js", target/<prefix>)` (`tools/govkit/govkit.py` `classify_outcome`), and that resolver reads the receipt, then probes `<here>/hooks` and `<here>/../hooks` (`resolve_kit_dir`, its `probes` tuple), so it already asks both static homes `must_not_exist` names. Settle whether removing the `must_not_exist` term changes any outcome classification: `exists()` against `is_file()`, a missing token, the receipt-less case, and whatever the govkit selftest's arms over this outcome block assert. Correct the descriptor's comment above the block, which says the absence is three terms.
   - **The comment.** `govkit.py`'s unit-14 comment spells the measured landing as a literal path; respell it through a drained token, keeping what was measured.
   - Read every spec in this build that describes the descriptor's absence terms (10, 11, 13 and 17 at least). A CLOSED spec that the change makes false is corrected in a spec-writer pass, `<w28>`, never by the builder.
2. **Tier** per the manifest's tier rule.

### Acceptance
`bash tools/check-install-prefix.sh` exits 0 at the unit's tip, and the leg's red half is the output above. Every govkit selftest arm that grades settings-merge's outcome block reads the same verdict before and after, or the spec names the arm that moves and why.

### Gates
`install-prefix (shipped surface)` · `memory hygiene`

### Non-goals
- No change to `tools/check-install-prefix.sh` or its population, and no waiver.
- No change to settings-merge's adopter or to `resolve_kit_dir`.
- No `tools/unattended/` self-test suite runs (standing owner instruction, 2026-08-23).
- No push beyond the owner's landing ask.
