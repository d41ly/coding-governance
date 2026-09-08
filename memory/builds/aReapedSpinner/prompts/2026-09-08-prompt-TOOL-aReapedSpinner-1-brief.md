# Brief — TOOL-aReapedSpinner-1, the census

**Serves:** journal TOOL-aReapedSpinner-1

What this pass was handed: the unit's spec at rev-4, three spec audits and their folds, and three
measurement records under `build/` — the backend comparison, the live-predicate run, and the
union-graph probe.

What it builds: `census.py`, one bounded read of the process table normalized to a nine-field row,
plus `selftest.py` with fifteen arms.

The four things that are not obvious, each measured rather than reasoned:

- **The primary key is `winpid`.** MSYS rows are 19 of 337 here, and the gate runner dispatches its
  legs as NATIVE processes, so a census keyed on the MSYS id describes 6% of the population and
  structurally excludes what the kit exists to reap.
- **`kind` is decided by the `0x400000` bit** on the `ps -W` PID column. Without a discriminator
  every row grades `msys` — `ps -W` reports a PID for all of them — and the whole native population
  goes to a signal that cannot reach it.
- **BOTH parent graphs are carried.** `win_ppid` is CIM's and defined for every row; `msys_ppid` is
  an overlay absent for the native majority, and that absence means backend visibility, never a
  dead parent.
- **Bytes, not `text=True`.** Measured: a CP1252 byte at offset 66732 killed the read with a
  `UnicodeDecodeError` raised on a reader thread, after which `.stdout` is `None`.
