# Build brief — TOOL-aEvidencedLens-6

**Serves:** journal TOOL-aEvidencedLens-6

Build exactly what the unit's spec states (`memory/builds/aEvidencedLens/spec/`, the file whose
status header carries `TOOL-aEvidencedLens-6`), and read the shared invariants in
`2026-10-05-prompt-TOOL-aEvidencedLens-1-1-spec-brief.md` beside this file first. Where the spec and
that brief disagree, the spec wins, and you say so in your return.

This unit edits `tools/workflows/tier2-review.template.js` and re-renders `tools/workflows/tier2-review.js` with `bash tools/workflows/check-protocol-parity.test.sh --render` (the one `.test.sh` invocation the gate guard admits, because `--render` is read-only on suites). Your direct check is a stub run: a scratch Node script that evaluates the rendered harness as an AsyncFunction with recording `agent`, `log`, `phase`, `parallel` and `args` globals, as `tools/workflows/tier2-review.test.sh` does. It asserts the prompts and returns this spec's criteria name, and it diffs the diff-kind finder and skeptic prompts against a render taken at the pass's base. Update `tools/workflows/tier2-review.test.sh` arms that pin what you changed; do not run it.

The spec is already committed. Your code lands in a SEPARATE commit whose subject names
`TOOL-aEvidencedLens-6` and whose final trailer block carries `Pass: TOOL-aEvidencedLens-6`. Stage only
the paths the main loop declared with `--dispatch`; if you need another, return that need rather than
committing it.

Fast direct checks only inside the pass. No merge bar, no `GATE_*=` prefix, no `*.test.sh` run other
than the `--render` form, no self-test runner: those run once, at VERIFYING. Bound every command
you run. Observe every new refusal or gate clause RED on a staged break against the pass's base before
it lands, and name the break in your return. Temporary files go to the session scratchpad named in
your ground text, never under the repository.
