# Build brief — TOOL-aEvidencedLens-9

**Serves:** journal TOOL-aEvidencedLens-9

Build exactly what the unit's spec states (`memory/builds/aEvidencedLens/spec/`, the file whose
status header carries `TOOL-aEvidencedLens-9`), and read the shared invariants in
`2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md` beside this file first. Where the spec and
that brief disagree, the spec wins, and you say so in your return.

This unit edits `tools/unattended/check-unattended.sh`. Your direct check is the leg run over a scratch fixture repository holding one run commit that edits `REVIEW_ROUNDS` (RED) and one owner commit that does (GREEN). Update `tools/unattended/check-unattended.test.sh` arms; do not run that suite.

The spec is already committed. Your code lands in a SEPARATE commit whose subject names
`TOOL-aEvidencedLens-9` and whose final trailer block carries `Pass: TOOL-aEvidencedLens-9`. Stage only
the paths the main loop declared with `--dispatch`; if you need another, return that need rather than
committing it.

Fast direct checks only inside the pass. No merge bar, no `GATE_*=` prefix, no `*.test.sh` run other
than the `--render` form, no self-test runner: those run once, at VERIFYING. Bound every command
you run. Observe every new refusal or gate clause RED on a staged break against the pass's base before
it lands, and name the break in your return. Temporary files go to the session scratchpad named in
your ground text, never under the repository.
