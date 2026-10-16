# Revision — dRedressedBar: TOOL-dRedressedBar-18 rev-2, F1 and F2 resolved by the owner

**Serves:** research TOOL-dRedressedBar-18

## The brief

### Goal
The owner resolved both of this spec's forks on 2026-10-14. Revise it to rev-2, with every section
the resolutions move made consistent, and a §9 revision line naming what moved.
- **F1 is option (b): a profile does NOT hold the host turnstile.** Mark it
  `RESOLVED (owner, 2026-10-14): (b)` in place. The design and criteria that assumed (a) change. A
  bar nested inside a leg (the canary's, the evidence suite's and any other) now queues at the
  turnstile behind any other bar on the host, and another session's bar can run beside the profile.
  So the record must say, per leg, when a reading was taken while the turnstile was held by someone
  else or while foreign gate work ran. Use the census's `foreign` field and the turnstile's queue
  line, so `derive-ceilings.py` sets such readings aside as it already does. State that a concurrent
  mode reading of a nested-bar leg includes its queue wait, and record that wait apart from its work.
- **F2 is option (b): keep each leg's log redacted only.** Mark it
  `RESOLVED (owner, 2026-10-14): (b)` in place. The raw file is deleted once its redacted copy is
  written, and the criterion that observes "every log kept" reads the redacted copies.

### Items
1. Revise `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-18.md` to rev-2 as the
   goal states. Remove nothing else, and leave §2's scope numbering stable where you can.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades TOOL-dRedressedBar-18
READY, not FORKED, and the spec carries no criterion or design sentence that assumes the turnstile
is held.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to any other spec.
