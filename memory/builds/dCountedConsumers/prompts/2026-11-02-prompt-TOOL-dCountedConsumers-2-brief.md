# Brief — dCountedConsumers: the trace signal counts a help page as product

**Serves:** research TOOL-dCountedConsumers-2

## The brief

### Goal
`closed_specs_with_no_product_commit` reads a commit that names a unit and touches `help/` as that unit's product commit. A unit whose whole product is a help page, as the charter's [docs] rule makes it, then stops reading as an offender.

### Items
1. Add `help` to `TRACE_GLOBS` in `tools/drift-audit/drift_signals.py`. Give it a comment of the house's kind saying why: `help/` holds the user-facing pages the docs leg grades, so a pass that writes one is product. Leave `PRODUCT_GLOBS` unchanged, and say why in the same place.
2. The landing's pre-push bar read the signal at 2, against a baseline listing only TOOL-aMooredAnchor-1. The new offender was TOOL-dCountedConsumers-1, whose pass commit `871f3c975` touches only `help/policy.md` and its own records. After the change the signal reads 1, and the baseline set is not touched. Never list the unit: the set is shrink-only, and the gate says so.
3. Check whether any other CLOSED spec's verdict moves when `help` joins. A unit that newly passes is the point of the change. A unit that newly fails would be a defect.

### Acceptance
- `python tools/drift-audit/drift_report.py --check` prints no `new` offender line and no `OVER BASELINE` line for `closed_specs_with_no_product_commit`.
- The signal's value reads 1, against the 2 it read before the change.

### Gates
`drift-audit records` and `drift-audit selftest`, by their exact names in `tools/gate-legs.json`, and the plain bar.

### Non-goals
`PRODUCT_GLOBS`, the shipped `drift_signals.template.py`, the dead probe `discarded_work_landed`, and the baseline set.

### Limitations
`drift_signals.py` is gov's project layer, so an adopter's copy is not changed.

### Reuse
The `TRACE_GLOBS` list and its comment style.

## Owner confirmation

Asked: Land dCountedConsumers on main?

> Land it
