# TOOL-dWitnessedBar-89 deviation 893 — the canary call site reds on a 3 and certifies nothing, beside the liveness loop

**Serves:** deviation TOOL-dWitnessedBar-89

- **Departs from:** `TOOL-dWitnessedBar-89@rev-4 [S4]`
- **Hand-off:** spec-to-code
- **Before:** S4 states what the liveness loop does on a 3 (`fail=1`, no count, no reason, no `rgf_seen`), and for the canary's call site only that it takes its `unread` slot on a 2 alone, so a 3 prints no `unread` line.
- **After:** on a 3 the canary's call site also sets `fail=1` and leaves `rgf_ok` at 0, printing no slotted line: its visited line is already on stderr from `check_canary_keys`.
- **Cause:** builder discovery
- **Reason:** with no slot taken, `rgf_whats` is empty on a 3, and `[ "${#rgf_whats[@]}" = 0 ] && rgf_ok=1` would certify that the planted CR reached `read_green_file` while the canary visited fewer pairs than `CANARY_KEYS` declares, the "skipped key list read as a pass" consequence the round-1 audit's id 7 names; its corrected fix has the liveness loop and the canary each treat a 3 as a failure. The visited assertion the call site counts would otherwise be one that cannot fail.
- **Evidence:** a stub probe of the edited suite's canary call site and liveness loop with both callees returning 3 printed no `unread` and no `(rc 2)` line and ended with `fail=1`, `rgf_ok=0`, `rgf_seen` empty and `a` moved by the two visited checks alone; `memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-85-spec-audit-round1.md`, M3. (DERIVED from the builder's probe)
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dWitnessedBar-89
