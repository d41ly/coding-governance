**Serves:** research PLAY-dOrderedCharter-77

# Brief: spec 77 — clear the spec-token check and the revision-log shape before dispatch

## The prompt

> I see that a lot of units are being refused this build and that's wasting tokens

— owner, 2026-11-10. The main loop's pre-dispatch check ran the spec-token check with spec 77 live and it redded; the pre-commit fork
check also refused rev-2's revision-log line. Caught here, neither costs a builder.

## The brief

### Goal

Make spec 77 pass the spec-token check as a live spec and the spec template's revision-log rule, keeping its design.

### Items

1. **Acceptance names a suite.** Seven acceptance tokens name a test suite or the self-test runner as the observation, which the check
   refuses ("a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture"):
   `skills/session-kickoff/manifest-check.test.sh` twice, `tools/check-template-size.test.sh` twice,
   `tools/agent-instructions/adopt-agent-instructions.test.sh` once, and `bash tools/run-gates/run-selftests.sh --check` once.
   Restate each criterion as an observation of the checker itself: the leg's checker run over the tree (for example the shell hygiene
   or install-prefix checker naming no offender in those files), or the checker on a staged break. A new suite arm stays on a
   `New arm:` line in the gates section, observed red-first by the main loop, not as an acceptance token.
2. **A guarded leg missing from the leg line.** Files touched names unit 18's ledger, which trips the guard of the leg `recall floor`;
   add that leg to the gates section's leg line.
3. **The revision-log line.** Rev-2's line names no section, scope id or acceptance id, which the template requires; name the ones it
   touched (S15, AC15, F3) without quoting figures, and add this brief's change to the same rev-2 line or a rev-3 line, as the template's
   rule for an uncommitted revision allows.
4. Edit the spec in the repository directly; no builder is running.

### Acceptance

- `python tools/check-spec-tokens.py` reports no hit on spec 77 with its status read live, the pinned-facts check names nothing in
  it, and memory hygiene's spec-shape check passes over it.

### Gates

Run the pinned-facts check and memory hygiene's spec-shape check over the spec and report each; the main loop runs the spec-token check.

### Non-goals

- No code. No edit to any other spec or file. No change to what the unit builds.
