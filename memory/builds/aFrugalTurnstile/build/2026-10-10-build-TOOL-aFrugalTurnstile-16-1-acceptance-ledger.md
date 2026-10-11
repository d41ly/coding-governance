# TOOL-aFrugalTurnstile-16 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-16

Built in two sessions: an agent pass wrote the hook, driver and pre-push suite changes and was killed
by a session end before committing; the main loop reviewed that work against the spec, kept it,
added the unattended-suite AC2 comparison, and observed every criterion directly. No merge bar and
no suite ran. Hook cases ran on a scratch fixture under `%TEMP%/aft16` against the hook at the
previous commit 9873a25f and against the edit. Driver cases ran `--close` on the in-place fixture
copied from the TOOL-9 and TOOL-13 arms, with a stub pre-push answering through `core.hooksPath`,
once over a SHA-1 repository and once over a SHA-256 one, against the driver at 9873a25f and the
edit. AC2 ran both `write_bar_green` copies sliced into one scratch repository; it holds at the
previous commit too, since the writers never differed given equal arguments, and a staged copy of
the driver writing another base turned it RED. AC3's refusals existed before this unit (the review's
M4 was a test gap), so it has no RED at the previous commit; the control stamp covers and each
altered stamp is refused. Owed at the close: the pre-push suite's T16 arms, the unattended suite's
AC2 comparison, and every §7 leg.

**Evidences:** TOOL-aFrugalTurnstile-16
- AC1 — `scoped M B` — the hook printed `scoped <M> <B>` where 9873a25f printed `scoped <M>`; the close wrote `gate-bar-green.scoped` with `base` the full green B on both object formats, where 9873a25f fell back to the full bar.
- AC2 — `by` and `stamped` — the two writers' kind scoped records compared byte-identical on every other line; a driver copy writing another base differed on the `base` line.
- AC3 — `covered on main push` — the unaltered runner stamp covered; with a foreign manifest, another manifest blob or another fingerprint the marker grew by one, no `covered on main push` line printed, and the `not covered` line named each reason.
- AC4 — `inherited` — `--decide` printed `scoped <C> -`, the push wrote no `gate-bar-green.scoped` and printed the decline naming the inherited green, where 9873a25f wrote one with base C; the close declined the same way.
- AC5 — `scoped` — over a SHA-256 repository the close honoured `scoped <64-hex> <64-hex>`, ran the bar with `GATE_BASE` set and `GATE_FULL` unset, where 9873a25f printed `did not answer with one decision line` and ran the full bar.
