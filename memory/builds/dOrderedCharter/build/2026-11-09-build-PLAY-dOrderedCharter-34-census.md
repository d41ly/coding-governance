# PLAY-dOrderedCharter-34 — the practice census at the build run, and each gov-only row's disposition

**Serves:** research PLAY-dOrderedCharter-34

The census is `tools/playbook/practice_census.py` over gov's own tree, its predicate the one the spec's
design section states: a row is `gov-only` when its evidence is gov's alone and no role cites it, and
`ship` otherwise. Below is its output at the pass, every row's ruling line, with the evidence lines of the
one `gov-only` row and of the one `foundation` row a leg names (DERIVED at fc6a05462 with this pass applied).

```text
census: practice.yagni · ship
census: practice.reuse · ship
census: practice.consistency · ship
census: practice.core · ship
census: practice.contract · ship
census: practice.derive · ship
census: practice.one-fact · ship
census: practice.spec · ship
census: practice.verify · ship
census: practice.gate · ship
census: practice.class · ship
census: practice.left-shift · ship
census: practice.bar · ship
census: practice.cost · ship
census: practice.small · ship
census: practice.isolate · ship
census: practice.land · ship
census: practice.post-merge · ship
census: practice.reconcile · ship
census: practice.migrations · ship
census: practice.ids · ship
census: practice.memory · ship
census: practice.records · ship
census: practice.docs · ship
census: practice.security · ship
census: practice.risk · ship
census: practice.bound · ship
census: practice.portable · ship
census:   leg 'shell hygiene (a location probe asked from a moved directory)' · ships · enforces practice.portable.paths
census:   leg 'shell hygiene (a fixed-name temp renamed into place)' · ships · enforces practice.portable.temp-files
census:   leg 'encoding posture (text IO names its encoding)' · exempt · enforces practice.portable.encoding
census:   leg 'python resolver (behaviour + inline parity + idiom ban)' · exempt · enforces practice.portable.launch
census:   leg 'python resolver (behaviour + inline parity + idiom ban)' · exempt · enforces practice.portable.interpreter-floor
census:   cited by a role's rules
census: practice.tokens · ship
census: practice.tools · ship
census: practice.roles · ship
census: practice.voice · ship
census: practice.signal · ship
census: practice.formats · ship
census: practice.default · ship
census: practice.solid · ship
census: practice.dry · ship
census: practice.tdd · ship
census: practice.writing · gov-only · stays
census:   leg "tags (the resolver's checks)" · exempt · enforces practice.writing.address
census:   leg "tags (the resolver's checks)" · exempt · enforces practice.writing.retirement
census:   leg 'edges (every declared edge parses, is registered and resolves)' · exempt · enforces practice.writing.typed-relations
census:   leg 'writing practice (records and units)' · exempt · enforces practice.writing.one-subject
census:   leg 'writing practice (records and units)' · exempt · enforces practice.writing.pinned-facts
census:   leg 'writing practice (records and units)' · exempt · enforces practice.writing.one-door
census:   leg 'writing practice (records and units)' · exempt · enforces practice.writing.rationale-apart
census:   leg 'one-owner' · exempt · enforces practice.writing.one-owner
census: 39 row(s) · ship 38 · gov-only 1 · moves 0 · moves, row kept 0 · stays 1
```

## Each gov-only row's disposition

- `practice.writing` rules `gov-only` with `stays`: its line names no path, every leg enforcing one of its
  rule tags is an exempt leg of the registry, no role's `rules:` line cites `writing`, and `foundation` does
  not list it, so no shipped default carries it and gov's charter does not render it. Nothing moves
  (DERIVED at fc6a05462).
- `practice.portable`, the one `foundation` row a leg names, rules `ship`: two of the legs enforcing its
  rule tags are no exempt leg (DERIVED at fc6a05462).

## What the pass applied

The moved set is empty, so `tools/playbook/practices.toml`, `tools/playbook/core-pending.txt`,
`tools/gate-legs.json` and gov's overlay are unedited, and no change record is owed to
PLAY-dOrderedCharter-31. An empty moved set is read as no move, never as coverage of a move's edits.
