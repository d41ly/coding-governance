**Serves:** journal TOOL-dBoundRoles-82

# Brief — dBoundRoles: TOOL-dBoundRoles-82, a new unit closing `TOOL-dBoundRoles-78`

## The prompt

> Build gaps here

— owner, 2026-11-23, ruling the run's hand-off: the gaps its deferred units waited on are built in this run. The
ruling and the five new units are `build/2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling.md`; read it whole.

## The brief

### Goal

Write a new Tier-2 spec, `memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-82.md`, by `memory/TEMPLATE-SPEC.md`: status `OPEN`, `rev-1`, dated 2026-11-23, node d,
base `318e20c9`, `streams tooling`, and the tail `order 23 · closes TOOL-dBoundRoles-78`. It binds by
`**Derived:** PLAY-dClosedLoop-2`, the line this build's promoted units carry (TOOL-dBoundRoles-52 §8 F1). It is
one mechanism: closing the gap the ask names, so that `TOOL-dBoundRoles-20` S5 (a role's `budget` widening as it rises, §8 F8 (ii)) can be built as written.

### The gap

At HEAD, a scalar field's `widens` is an order of listed values (`tools/playbook/overlay_rows.py#read_field_decl`), so an open integer such as a role's `budget` cannot declare that an overlay `amends` may raise it and never lower it. The ask accepts when a scalar field declaring a rising direction admits an `amends` that raises its value and refuses one that lowers it, naming the field.

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
   The seam to extend first: `tools/playbook/overlay_rows.py#read_field_decl`, `FIELD_KEYS` and `PATCH_KEYS`, and the patch check `tools/playbook/row_checks.py#check_rows` applies.
7. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`; pin any count; never set a number
   before a counted noun in prose.
8. `python tools/check-spec-tokens.py --spec memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-82.md` and
   `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-82.md` exit 0 before you return.

### Acceptance

The spec exists, OPEN at rev-1, and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec, no product code, no record but this spec. The consumer's own scope stays its own.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-82.md` alone.

### Reuse

`tools/playbook/overlay_rows.py#read_field_decl`, `FIELD_KEYS` and `PATCH_KEYS`, and the patch check `tools/playbook/row_checks.py#check_rows` applies.

### Revision 1

A first writer (run `wf_fd4c768b-7f1`) authored `memory/builds/dBoundRoles/spec/2026-11-23-spec-TOOL-dBoundRoles-82.md`, and its
commit was refused by hygiene check 12: the spec's §3 **hands-off** bullet to `TOOL-dBoundRoles-20` has no matching
**consumes-from** bullet in `TOOL-dBoundRoles-20`'s spec, which this run does not revise, because the owner's ruling record binds
the relation over that spec. The draft is on disk, uncommitted, and is NOT conforming until that one bullet is
gone. Revise it in place: remove the **hands-off** bullet naming `TOOL-dBoundRoles-20`, keep every other line as written,
**hands-off** bullets naming `external` included, and say in one prose sentence under §3, outside the Edges list,
that `TOOL-dBoundRoles-20` consumes this unit through `build/2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling.md`. Then run
item 8's two checks again.
