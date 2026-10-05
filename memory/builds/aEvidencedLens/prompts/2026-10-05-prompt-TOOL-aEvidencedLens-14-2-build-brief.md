# Build brief — TOOL-aEvidencedLens-14

**Serves:** journal TOOL-aEvidencedLens-14

Build exactly what the unit's spec states (`memory/builds/aEvidencedLens/spec/`, the file whose
status header carries `TOOL-aEvidencedLens-14`), and read the shared invariants in
`2026-10-05-prompt-TOOL-aEvidencedLens-14-1-spec-brief.md` beside this file first. Where the spec and
that brief disagree, the spec wins, and you say so in your return.

This is a PROMOTED unit from the round-1 spec audit. Its spec names the files it edits, and the direct check its §6 requires. Where it edits a workflow template, re-render with `bash tools/workflows/check-protocol-parity.test.sh --render` and check with a scratch stub run, as units 1 to 6 did. Where it edits a checker, observe its new clause RED on a staged break. Update the suite arms that pin what you changed; do not run the suites.

The spec is already committed. Your code lands in a SEPARATE commit whose subject names
`TOOL-aEvidencedLens-14` and whose final trailer block carries `Pass: TOOL-aEvidencedLens-14`. Stage only
the paths the main loop declared with `--dispatch`; if you need another, return that need rather than
committing it.

Fast direct checks only inside the pass. No merge bar, no `GATE_*=` prefix, no `*.test.sh` run other
than the `--render` form, no self-test runner: those run once, at VERIFYING. Bound every command
you run. Observe every new refusal or gate clause RED on a staged break against the pass's base before
it lands, and name the break in your return. Temporary files go to the session scratchpad named in
your ground text, never under the repository.
