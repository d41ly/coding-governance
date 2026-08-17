# aBranchedMandate - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 6f705002cd4c21e7a2c7899cac3a0b4a3ce6a8da
phase: VERIFYING
keepalive: 3ff2b805
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 401416faebff58c4527abef9f1a4ae80d244c4f2
anchor-ref: refs/heads/main
base: 401416faebff58c4527abef9f1a4ae80d244c4f2
keepalive-reaped: yes
parked-surfaced: yes

## Parked

Unit 4 of the roster, spec id TOOL-aBranchedMandate-3, is PARKED and DEFERRED rather than built.
The question refused: does the owner's ratification of that rule change still stand now that the
protocol carrying its three-cost price list has changed underneath it? Options seen: re-derive S6b
and S4 against the merged leg and build it; build only the mechanical parts and leave S6b; or park
and hand the re-pricing back. The third was taken, because S6b's obligation is to state the
disposition of five assertions inside a loop that no longer exists — re-specifying a security
predicate rather than re-pointing a citation — and because M3 delegates fork resolution, not scope.
The full drift table is in that spec's rev-5 and the question, options and refusal are in the build
README. Both reached the wrap-up, which is what the attestation above claims.

Recorded by hand, and that is worth naming: no verb writes a park. `park()` is reachable only from
`--close --override` and `--abort`, so a run that parks a unit WITHOUT needing an override and
without aborting has no sanctioned way to put it here, even though protocol section 2 makes this
file the home of parked decisions. Row minted for it.

Also recorded: this run re-ran `--preflight` against its own live slug to observe an acceptance
criterion, and preflight OVERWROTE the live run-state file — keepalive id and anchor pin both. It
was restored from the commit that preceded it, so the pin-time evidence above is the original
observation. Upstream's record rotation retires a TERMINAL record; a non-terminal one is still
overwritten in place. Row minted for that too.

2026-08-17T13:46:06Z decision · item unit 4 re-pricing · reason Owner re-priced 2026-08-17 and chose to build TOOL-aBranchedMandate-3. The earlier park's main reason was a measurement error: the S6b loop exists at check-unattended.sh:295; the grep pattern lacked the quote the source carries. Premises re-derived in spec rev-6.
