# TOOL-dTrueNorth-11 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-11

No merge bar, no self-test suite and no gate leg but the naming lexicon ran in this pass. Every
criterion was observed by a probe of the manifest, each a scratch script under the run's scratchpad
or the section's own `python3 -c`: a probe loading `tools/check-spec-tokens.py` by path and applying
its `check_guard_trips` to the checker's path over every leg of the manifest, in the working tree and
at the pinned base read by `git show`, corroborated by the checker's `--legs-for` query; and a probe
loading `tools/govkit/govkit.py` by path, building check 7c's inputs through govkit's own readers and
applying 7c's six class tests as its block spells them. The probes stand in for the
`govkit selfcheck` leg's check 7c; that leg, the `build-index selftest` and `memory-hygiene
self-test` legs this guard now runs, and `spec tokens (a spec's own names resolve)` are owed to the
close. The guard is data the runner reads, so no suite arm lands and no RED-first observation is owed.

**Evidences:** TOOL-dTrueNorth-11
- AC1 — `check-spec-tokens.py` — the section's `python3 -c` over `tools/gate-legs.json` printed
  `[['{prefix}/lib/', '{prefix}/memory-tree/', '{prefix}/check-spec-tokens.py'], ['{prefix}/lib/',
  '{prefix}/memory-tree/', '{prefix}/check-spec-tokens.py']]`, the `memory-hygiene self-test` row
  first in manifest order and `build-index selftest` second, each ending with the checker's pathspec.
- AC2 — `tools/gate-legs.json` — the trip probe, `{prefix}` resolved to `tools`, over the 142 legs of
  the working tree tripped 14 legs on `tools/check-spec-tokens.py`, `build-index selftest` and
  `memory-hygiene self-test` among them; over the 142 legs at `271aa59d` it tripped 12, the same list
  less those two, both reading `skips`. `check-spec-tokens.py --legs-for tools/check-spec-tokens.py`
  named both legs as tripped by `tools/check-spec-tokens.py` itself, the other twelve by the broad
  `tools/`.
- AC3 — `exempt` — the class probe, over 29 descriptors and 28 exemptions at tool root `tools`,
  printed `('tools/check-spec-tokens.py', ['exempt'])` for the new pathspec and found every one of
  the manifest's 175 guard pathspecs in exactly one class; with the checker's registry exemption
  dropped it printed `['kit-relative']`, so the probe can class the path as something else.
