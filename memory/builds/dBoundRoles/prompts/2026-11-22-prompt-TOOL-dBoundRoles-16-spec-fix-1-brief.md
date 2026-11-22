**Serves:** journal TOOL-dBoundRoles-16

# Brief — dBoundRoles: TOOL-dBoundRoles-16 revised over its third builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 16's third builder (run `wf_e3c2d4a9-882`) stopped before its
code on rev-6: the loop kit's role and workflow factories write none of the fields S2 and S5 make required. The
returns are in `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-16-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md` to its next rev so the next builder can
build it as written.

### Items

1. A §8 fork you resolve by M3's rule as a delegated agent resolution, `widens:` and `relaxes:` each a value or `none`.
   New factory flags lose: they are a new public surface (veto 2). Choose among options with no new surface, such as
   the role factory writing a stated default `shapes` and the workflow factory writing a stated default `kind` whose
   kind row supplies `checklist` and `orientation`, or refusing a non-empty `--roles` it cannot complete; probe each
   against HEAD. TOOL-dBoundRoles-21 met the same class for `effort` with a value written at factory time; follow its
   shape where it fits.
2. Add `tools/loop/factories.py`, and `tools/loop/README.md` only if it documents what the factories write, to §4 Files
   touched; state the values the factories write in §4 Migration; add `loop factories fixtures` to §7; keep the
   `role-new` and `workflow-new` cases green; and update the roles README sentence on what `core.py new role` writes.
3. Fold the builder's two notes: arm 30's `scratch` entry and its `judge` row carry their kinds, and §7 or §6 names the
   tag gate's role-bindings join that the `role.*` unit rows arm.
4. Change nothing else. Keep every criterion's number and keep each passable on a correct build and red on the break
   it names. Cite code as `path#symbol` or `path@<blob8>:<line>`; pin any count. Keep the status `INPROGRESS`. One
   revision-log line names this brief and the return by their file stems.
5. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec carries its next rev with every item folded and both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change beyond the items.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md` alone.

### Reuse

`tools/loop/factories.py#write_role` and `#write_workflow`, the seams item 1 extends; TOOL-dBoundRoles-21's spec for
the effort value its factory writes.
