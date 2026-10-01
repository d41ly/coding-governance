# Build brief — TOOL-aRepatriatedFork-51

**Serves:** journal TOOL-aRepatriatedFork-51

A unit pass under the aRepatriatedFork mandate, inside the VERIFYING repair pass R1. Build `memory/builds/aRepatriatedFork/spec/2026-10-01-spec-TOOL-aRepatriatedFork-51.md` exactly: `check-brief-recorded.sh` reads a declared waiver registry from HEAD, ported from `check-pass-order.sh`'s, where an absent file waives nothing and a stale row reds. The red-first control is the leg at `6e7cb0df`, which has no registry and reds a committed waiver's fixture.

## How to build this unit

- **Spec before code.** The spec is committed before the code, in its own records commit.
- **Red first.** Write the three registry arms in `tools/unattended/check-brief-recorded.test.sh` and run
  the suite with the `6e7cb0df` leg staged in. The committed and stale arms must fail. Then build the
  registry and run the suite again.
- **Every violation site routes through one function**, so a waived unit is counted, never dropped.
- **Do not write the waiver rows in this unit.** They are records, written afterwards and parked.
- **Windows traps.** Edit with the Edit tool or binary-mode Python. Never `python -` without input.
- **Commit** with the unit id in the subject and `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  last. Never `--no-verify`.
