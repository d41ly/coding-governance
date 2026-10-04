# Build brief — TOOL-aEvidencedLens-7

**Serves:** journal TOOL-aEvidencedLens-7

Build exactly what the unit's spec states (`memory/builds/aEvidencedLens/spec/`, the file whose
status header carries `TOOL-aEvidencedLens-7`), and read the shared invariants in
`2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md` beside this file first. Where the spec and
that brief disagree, the spec wins, and you say so in your return.

This unit edits `tools/unattended/unattended.sh`'s `--review`. Your direct check is the verb itself against a scratch fixture repository (`git init` under the scratchpad, a minimal `.unattended.conf` and run-state file, as `tools/unattended/unattended.test.sh`'s `mkconf` builds). Observe each new refusal RED before it lands. Update the suite's arms that pin the old refusal; do not run the suite.

The spec is already committed. Your code lands in a SEPARATE commit whose subject names
`TOOL-aEvidencedLens-7` and whose final trailer block carries `Pass: TOOL-aEvidencedLens-7`. Stage only
the paths the main loop declared with `--dispatch`; if you need another, return that need rather than
committing it.

Fast direct checks only inside the pass. No merge bar, no `GATE_*=` prefix, no `*.test.sh` run other
than the `--render` form, no self-test runner: those run once, at VERIFYING. Bound every command
you run. Observe every new refusal or gate clause RED on a staged break against the pass's base before
it lands, and name the break in your return. Temporary files go to the session scratchpad named in
your ground text, never under the repository.
