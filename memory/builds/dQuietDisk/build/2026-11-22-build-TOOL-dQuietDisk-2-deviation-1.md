# TOOL-dQuietDisk-2 deviation 1 — a short-sha batch that answers the wrong line count falls back to one read per sha

**Serves:** deviation TOOL-dQuietDisk-2

- **Departs from:** `TOOL-dQuietDisk-2@rev-6` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S6 says every short sha a report line names comes from one `GIT log --no-walk=unsorted --format=%h <sha>... --` after the loop. It names no answer for a batch whose output is not one line per distinct sha.
- **After:** `tools/unattended/check-pass-order.sh` checks the batch's line count against the count of distinct shas. Where the two differ, it spells each sha with one `GIT rev-parse --short`, which is the per-sha read the leg made at the base. Where they agree, as in every probe of this pass, the one batched read stands alone.
- **Cause:** builder discovery
- **Reason:** the rows are filled by position from the batch's lines. A short or long answer, for example from a `log.showSignature` the pinned `GIT` wrapper does not override, would put the wrong short sha in a row or leave the row's internal marker bytes in the output. Falling back to today's read keeps the output byte-identical instead.
- **Evidence:** at every AC1 point and over the repeated-sha fixture, the trace held one `log --no-walk=unsorted` and no `rev-parse --short` (PINNED, this pass's scratch probes, 2026-11-22).
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** ask TOOL-dQuietDisk-2
- **Caused-by:** TOOL-dQuietDisk-2
