# dRemeasuredRender — asks

## Asks
- TOOL-dRemeasuredRender-2 · filed 2026-10-11 · the location-probe scanner does not see a probe whose `cd <dir>` carries a redirect before the `&&`: `tools/run-gates/run-gates.test.sh`, line 1298, holds `$( cd "$P" 2>/dev/null && git rev-parse --show-toplevel ...)`, which `tools/gate-lint/sh_hygiene.py --location-probes` grades neither GATED nor scrubbed, while the same line's second probe, with no redirect, was GATED. One such site in gov's tree at 9a8777b8. Widen the `cd` form to admit a redirect, add the selftest arm, and scrub the site. · accept `sh_hygiene.py --location-probes` reports the redirect form GATED until scrubbed, and its `--selftest` carries an arm observed RED at the predicate before the change
- TOOL-dRemeasuredRender-3 · filed 2026-10-11 · inherited red: leg lexicon naming predicates red at 9b743831, introduced by 6fbe54e8 · seen `{prefix}/lexicon/lexicon.py`@9b743831 run `python {prefix}/lexicon/lexicon.py` · accept the leg is green at the default branch's tip → 6fbe54e8
- TOOL-dRemeasuredRender-4 · filed 2026-10-11 · inherited red: leg playbook render wiring red at 9b743831, introduced by 6fbe54e8 · seen `{prefix}/playbook/adopt-playbook.sh`@9b743831 run `bash {prefix}/playbook/adopt-playbook.sh --target . --check` · accept the leg is green at the default branch's tip → 6fbe54e8

## Dispositions
- SEV · TOOL-dRemeasuredRender-2 · LOW · one site in a gov suite that never runs under a hook; adopters receive no new red until the scanner is widened
- KEEP · TOOL-dRemeasuredRender-2 · found while building TOOL-dRemeasuredRender-1 on 2026-10-11 and not adopted: widening the scanner moves the leg's population at every adopter, which is its own unit with its own arm, outside the defect this build was handed
- SEV · TOOL-dRemeasuredRender-3 · HIGH · a merge-bar leg is red on the default branch
- KEEP · TOOL-dRemeasuredRender-3 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dRemeasuredRender-4 · HIGH · a merge-bar leg is red on the default branch
- KEEP · TOOL-dRemeasuredRender-4 · filed by an unattended run for the owning build; outside this build's goal
