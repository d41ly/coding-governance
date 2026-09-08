# Brief — TOOL-aReapedSpinner-4, the reaper

**Serves:** journal TOOL-aReapedSpinner-4

What this pass was handed: the unit's spec at rev-4, the D8, D9, D17, D20, D21, D22 and D41
findings, and the signal-namespace measurement record.

What it builds: `reap.py` — `run_kill`, `check_survivors`, `--sweep`, `--dry-run`, `--kill` — plus
eleven arms including one that stages a real mixed-namespace tree and kills it.

The four things that are not obvious, each measured:

- **The signal is chosen per row, OPERATIONALLY.** `kill -0` answering decides, because a process
  MSYS did not spawn answers `No such process` to MSYS `kill` and dies only to `taskkill /PID`.
- **`/PID`, one slash.** `//PID` is an MSYS shell idiom; a list argv is not shell-mangled and
  taskkill rejects the doubled form with rc 1.
- **Membership, not re-derivation.** The fence computed the set once; a per-member inheritance
  clause is how rev-2's re-check became unfalsifiable.
- **Verification is a second census.** `kill -9` returns success for a signal DELIVERED, and
  `taskkill /T` printed SUCCESS over one death of four.
