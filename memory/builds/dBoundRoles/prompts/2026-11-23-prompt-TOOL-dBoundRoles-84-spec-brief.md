**Serves:** journal TOOL-dBoundRoles-84

# Brief — dBoundRoles: TOOL-dBoundRoles-84, a new unit closing `TOOL-dDeclaredLoop-120`

## The prompt

> Build gaps here

— owner, 2026-11-23, ruling the run's hand-off: the gaps its deferred units waited on are built in this run. The
ruling and the five new units are `build/2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling.md`; read it whole.

## The brief

### Goal

Write a new Tier-2 spec, `memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-84.md`, by `memory/TEMPLATE-SPEC.md`: status `OPEN`, `rev-1`, dated 2026-11-23, node d,
base `318e20c9`, `streams tooling`, and the tail `order 23 · closes TOOL-dDeclaredLoop-120`. It binds by
`**Derived:** PLAY-dClosedLoop-2`, the line this build's promoted units carry (TOOL-dBoundRoles-52 §8 F1). It is
one mechanism: closing the gap the ask names, so that `TOOL-dBoundRoles-20` S6 (the actor patch and `check_actor_patch`, §8 F8 (iii)) can be built as written.

### The gap

At HEAD, the loop kit's item schema (`tools/loop/item-schema.toml`) declares `actor` a bare scalar with neither `widens` nor `fixed-by` nor `ref`, so the row checks refuse every `amends` of a gov item's actor before an actor-patch check could admit a repository role that returns the item's template. The ask accepts when an `amends` of a gov item's `actor` to a repository role reaches the actor-patch check, which alone admits or refuses it; an `amends` of any other fixed item field is still refused.

### Items

1. Read the ask's row in its home `BACKLOG.md`, `TOOL-dBoundRoles-20`'s spec at its live revision (the clause above and
   its §8), and the code the gap names at HEAD before you write; probe that the gap still holds and say how.
2. Scope the smallest change that meets the ask's accept clause, in the kit that owns the code, additively and
   behind no switch the clause does not ask for. Name every reader of anything you rename or narrow on a
   `**Readers:**` line.
3. §3 Edges: a **hands-off** bullet to `TOOL-dBoundRoles-20` naming what it consumes. Any other unit of this build or
   another whose code you touch is an edge too.
4. §6 criteria each name the command that observes them, pass on a correct build and red on the break they name.
   §7 lists every leg your Files touched trips (`python tools/check-spec-tokens.py --list` prints them) and one
   `New arm:` line per new arm, in the owning kit's own self-test or suite.
5. Resolve every fork by M3 as a delegated agent resolution, with `options`, `pick`, `admitted-by`, `widens:` and
   `relaxes:`. A choice that changes another build's public surface beyond the ask's accept clause is a veto-2 loss.
6. §10 reuse audit, with `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and a recall query, each named.
   The seam to extend first: `tools/loop/item-schema.toml`, the loop kit's composition reader `tools/loop/composition.py#read_composition_at`, `check_item_composition` (TOOL-dDeclaredLoop-24 S4) and the playbook kit's `tools/playbook/overlay_rows.py#read_field_decl`.
7. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`; pin any count; never set a number
   before a counted noun in prose.
8. `python tools/check-spec-tokens.py --spec memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-84.md` and
   `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-84.md` exit 0 before you return.

### Acceptance

The spec exists, OPEN at rev-1, and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, no product code, no record but this spec. The consumer's own scope stays its own.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-84.md` alone.

### Reuse

`tools/loop/item-schema.toml`, the loop kit's composition reader `tools/loop/composition.py#read_composition_at`, `check_item_composition` (TOOL-dDeclaredLoop-24 S4) and the playbook kit's `tools/playbook/overlay_rows.py#read_field_decl`.
