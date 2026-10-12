# Spec brief — TOOL-aBriskPreflight-11: the ceilings instrument prices every fork at the worst host reading on record

**Serves:** research TOOL-aBriskPreflight-11

Promoted from the closing diff review's HIGH H1 (`reviews/2026-10-12-review-TOOL-aBriskPreflight-1-2-3-4-5-6-7-10-diff-review-round1.md`, section "H1"). Read that section whole, then
spec 7 (`spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md`, CLOSED) and its instrument
`build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh` with the two row files it reads.

The mechanism, one: the instrument's K_w is the larger of the floor and EVERY K_m in the rows it
reads, host rows included, as spec 7 §4 says; the driver's three constants and the README section
are re-derived from it and printed byte-identical by it. The skeptic judged two resolutions sound:
widen the instrument to host rows (the spec's own rule; it may push PREFLIGHT_CEILING to GATE_BOUND,
where the instrument exits 1 and the unit parks, as spec 7 intends), or rev spec 7's rule to after-arm
rows only with the reason the old-arm 2.53 s fork reading is excluded. Decide by M3's rule and record
the loser. Keep the README section and the driver comment in step. A self-test fixture with a host
row whose fork cost exceeds every timed row's K_m asserts the printed K_w equals it, observed RED with
the host branch's update dropped. The owner's ruling stands: a wiring check over its ceiling is
killed and refused at check 4; a preflight over its own names the breach and still writes the record.
No new conf key, no raised GATE_BOUND. Order 6.
