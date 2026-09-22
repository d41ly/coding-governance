# Owner ruling — which repair for the harness's install paths

**Serves:** journal TOOL-dPolishedVitrine-1

The owner's choice, verbatim, as the orchestrating session relayed it on node `d`, 2026-09-12. It
travels here as bytes rather than as a reference, because a ruling that lives only in a chat
transcript cannot be re-read by the session that lands this build.

## The question put to the owner

> Which repair?

The finding it was asked about, as the question stated it:

> scripts/workflows/unattended-build.js calls tools/workflows/tier2-review.js,
> tools/workflows/unattended-unit.js and tools/memory-tree/gotchas.py; none exist in nc or core
> (install prefix 'scripts')

## The option chosen

> Derive at install (Recommended)

Described to the owner as:

> The kit fills in the path prefix at install ... One kit release fixes both nc and core.

## The options offered and not chosen

- pass paths in args
- leave it

## What the ruling does and does not settle

It settles the MECHANISM: the harness's paths are derived when the kit is installed, not supplied
by each caller and not left as they are. It does not settle the mechanism's details, which the
spec's §4 records with their grounds. It does not settle the scope question of the unattended
Skill's checklist line either. The orchestrating session put that line in scope under the same
ruling, and the spec's §8 records that as a delegated resolution, not an owner one.

The question named three literals, and the harness carries four. The fourth is the driver command,
which NicoCares had already repathed by hand in its own copy, so it did not appear in NicoCares' list
of broken paths. Core had not repathed it. The spec covers all four.
