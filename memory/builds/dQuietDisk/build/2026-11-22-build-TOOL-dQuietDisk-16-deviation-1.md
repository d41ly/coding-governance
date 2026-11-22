# TOOL-dQuietDisk-16 deviation 1 — the batch branch reads a reply by its suffix, and the handle's stop closes both pipes

**Serves:** deviation TOOL-dQuietDisk-16

- **Departs from:** `TOOL-dQuietDisk-16@rev-4` [S2, the handle sketch in section 4]
- **Hand-off:** spec-to-code
- **Before:**
  - S2 has a `missing` reply stay None, and an end of stream or a header that does not parse take the spawn branch and mark the handle dead.
  - Section 4's sketch has `remove_process()` close stdin and wait.
- **After:**
  - `tools/govkit/upgrade_steps.py#blob_at` reads a reply ending in ` missing` or ` ambiguous` as None. Any other reply must be three fields with a numeric size, and a short body read marks the handle dead too. An `OSError` or `ValueError` from the pipe is read as an end of stream.
  - `BlobBatch.remove_process()` also tolerates an `OSError` from closing a dead process's stdin, and closes stdout after the wait.
- **Cause:** builder discovery
- **Reason:**
  - git's reply for a missing name is `<name> missing`, and a name holding a space splits into more than two fields. The base's `split()` then read a later word of the path as a size and raised `ValueError`. A suffix test keeps that reply None without marking the handle dead.
  - Section 4 says an ambiguous name is None both ways. `ambiguous` is that reply, and it is no dead stream.
  - A killed process refuses the write and the close, so S2's fallback needs the error read as an end of stream, not raised.
- **Evidence:** the AC3 lines of `2026-11-22-build-TOOL-dQuietDisk-16-1-acceptance-ledger`. They cover a `missing` reply for a spaced path on a live handle, a killed handle answering through the spawn, and a never-started handle's `remove_process()`.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-16
