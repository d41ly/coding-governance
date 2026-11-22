# TOOL-dQuietDisk-19 deviation 1 — a Comparison row whose unit states no bound on its metric quotes that unit's git-process bound

**Serves:** deviation TOOL-dQuietDisk-19

- **Departs from:** `TOOL-dQuietDisk-19@rev-5` [Design]
- **Hand-off:** spec-to-code
- **Before:** section 4 "The record" has every Comparison row quote "the bound sentence from that unit's spec, as built", and `met` read that bound against the A-on value. It assumes each owning unit states a bound on each of the four metrics.
- **After:** where the owning unit's spec states no bound on the row's metric, the row quotes the unit's git-process bound for that run kind, and `met` reads that bound. That covers the four `wall ms` rows (units 10, 2 and 11 state no wall-time bound) and the `M2 cold` and `M2 warm` `peak temp` rows (unit 2 states none on peak). A Limits line names those rows. Every other row quotes the bound on its own metric.
- **Cause:** builder discovery
- **Reason:** `met` is `yes` or `no` only, so a row whose unit promised nothing on its metric would need a vacuous `yes` or an untrue `no`. Quoting the unit's git-process bound keeps every row's quote a real sentence of that spec, and the Limits line says the `met` cell of those rows does not grade the row's own metric.
- **Evidence:** a grep of the four owning specs at HEAD for `wall`, `seconds` and `peak` found only cost estimates for wall time and, in unit 2, no peak bound. The spec's AC6 probe printed no `bound-uncited` line over the sixteen rows (PINNED, this pass).
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** usage comparison-bound-quote
- **Caused-by:** TOOL-dQuietDisk-19
