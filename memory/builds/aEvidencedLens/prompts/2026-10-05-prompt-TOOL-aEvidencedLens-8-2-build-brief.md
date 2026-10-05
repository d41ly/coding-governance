# Build brief — TOOL-aEvidencedLens-8

**Serves:** journal TOOL-aEvidencedLens-8

Build exactly what the unit's spec states (`memory/builds/aEvidencedLens/spec/`, the file whose
status header carries `TOOL-aEvidencedLens-8`), and read the shared invariants in
`2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md` beside this file first. Where the spec and
that brief disagree, the spec wins, and you say so in your return.

This unit edits `tools/workflows/unattended-build.template.js` and re-renders `tools/workflows/unattended-build.js` with `bash tools/workflows/check-protocol-parity.test.sh --render`. Your direct check is a stub run of the rendered harness in a scratch Node script with recording globals, as `tools/workflows/unattended-build.test.sh` does. Update that suite's arms that pin what you changed; do not run it.

The spec is already committed. Your code lands in a SEPARATE commit whose subject names
`TOOL-aEvidencedLens-8` and whose final trailer block carries `Pass: TOOL-aEvidencedLens-8`. Stage only
the paths the main loop declared with `--dispatch`; if you need another, return that need rather than
committing it.

Fast direct checks only inside the pass. No merge bar, no `GATE_*=` prefix, no `*.test.sh` run other
than the `--render` form, no self-test runner: those run once, at VERIFYING. Bound every command
you run. Observe every new refusal or gate clause RED on a staged break against the pass's base before
it lands, and name the break in your return. Temporary files go to the session scratchpad named in
your ground text, never under the repository.
