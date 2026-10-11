# dRemeasuredRender — asks

## Asks
- TOOL-dRemeasuredRender-2 · filed 2026-10-11 · the location-probe scanner does not see a probe whose `cd <dir>` carries a redirect before the `&&`: `tools/run-gates/run-gates.test.sh:1298` holds `$( cd "$P" 2>/dev/null && git rev-parse --show-toplevel ...)`, which `tools/gate-lint/sh_hygiene.py --location-probes` grades neither GATED nor scrubbed, while the same line's second probe, with no redirect, was GATED. One such site in gov's tree at 9a8777b8. Widen the `cd` form to admit a redirect, add the selftest arm, and scrub the site. · accept `sh_hygiene.py --location-probes` reports the redirect form GATED until scrubbed, and its `--selftest` carries an arm observed RED at the predicate before the change

## Dispositions
- SEV · TOOL-dRemeasuredRender-2 · LOW · one site in a gov suite that never runs under a hook; adopters receive no new red until the scanner is widened
- KEEP · TOOL-dRemeasuredRender-2 · found while building TOOL-dRemeasuredRender-1 on 2026-10-11 and not adopted: widening the scanner moves the leg's population at every adopter, which is its own unit with its own arm, outside the defect this build was handed
