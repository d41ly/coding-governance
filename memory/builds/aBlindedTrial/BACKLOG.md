# aBlindedTrial — asks

## Asks

- TOOL-aBlindedTrial-7 · filed 2026-09-21 · a project-wide "spec audits owed by default" declaration: the per-build `spec-audit:` README key is the owner's per-build instrument (TOOL-aBlindedTrial-2), and an adopter wanting the audit on every build has no one-line way to say so; a conf key that pins the `spec-audit` fact for every build would be an ADD in the sense the MUST-by-default ruling allows. Parked from the aBlindedTrial README.
- TOOL-aBlindedTrial-8 · filed 2026-09-21 · a spec's §7 leg line must name every leg in `tools/gate-legs.json` whose `guard` any path in its §4 files-touched trips: unit 4 of aBlindedTrial omitted `scratch-guard self-test` while editing `tools/hooks/scratch-guard.js`, and the closing review found it, not a gate (round 1, F7). Both inputs are machine-readable; a `check-spec-tokens.py` sibling arm.

## Dispositions

- CLOSED · TOOL-aBlindedTrial-7 · by TOOL-aBlindedTrial-2 · a project-wide "spec audits owed by default" declaration: the per-build `spec-audit:` README key is the owner's per-build instrument (TOOL-aBlindedTrial-2), and an adopter wanting the audit on every build has no one-line way to say so; a conf key that pins the `spec-audit` fact for every build would be an ADD in the sense the MUST-by-default ruling allows. Parked from the aBlindedTrial README.
- CLOSED · TOOL-aBlindedTrial-8 · by cf07a157c7397a531ce0d59218072895753c25c2 · a spec's §7 leg line must name every leg in `tools/gate-legs.json` whose `guard` any path in its §4 files-touched trips: unit 4 of aBlindedTrial omitted `scratch-guard self-test` while editing `tools/hooks/scratch-guard.js`, and the closing review found it, not a gate (round 1, F7). Both inputs are machine-readable; a `check-spec-tokens.py` sibling arm.
