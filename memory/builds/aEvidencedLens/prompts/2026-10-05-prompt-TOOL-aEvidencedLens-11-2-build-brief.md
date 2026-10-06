# Build brief — TOOL-aEvidencedLens-11

**Serves:** journal TOOL-aEvidencedLens-11

Build exactly what the unit's spec states (`memory/builds/aEvidencedLens/spec/`, the file whose
status header carries `TOOL-aEvidencedLens-11`), and read the shared invariants in
`2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md` beside this file first. Where the spec and
that brief disagree, the spec wins, and you say so in your return.

This unit edits carriers through their templates and re-renders them: `tools/memory-tree/BUILD-METHOD.template.md` (its render is checked by the memory-tree kit's own render check), `tools/unattended/SKILL.template.md`, the verbs entry, `tools/memory-tree/README.md` and a new `memory/DECISIONS.md` row. Its direct check is the render-parity check each template names, and a grep showing that no carrier still says spec minors are folded or lists the four old lens names.

The spec is already committed. Your code lands in a SEPARATE commit whose subject names
`TOOL-aEvidencedLens-11` and whose final trailer block carries `Pass: TOOL-aEvidencedLens-11`. Stage only
the paths the main loop declared with `--dispatch`; if you need another, return that need rather than
committing it.

Fast direct checks only inside the pass. No merge bar, no `GATE_*=` prefix, no `*.test.sh` run other
than the `--render` form, no self-test runner: those run once, at VERIFYING. Bound every command
you run. Observe every new refusal or gate clause RED on a staged break against the pass's base before
it lands, and name the break in your return. Temporary files go to the session scratchpad named in
your ground text, never under the repository.
