# Brief — TOOL-aPooledSweep-1, the bounded outer pool

**Serves:** brief TOOL-aPooledSweep-1

What this pass was handed: the unit's spec at rev-3, the round-1 and round-2 spec audits, and
`tools/run-gates/run-selftests.sh` at 96679934.

What it builds: a `--sweep` mode on that runner. It resolves the population through the existing
`read_population`, runs the resolved rows through a bounded outer pool, and reports one verdict line
per suite in DECLARATION order whatever the pool did. It issues no cost verdict at all — that
division is what makes concurrency admissible here and is unit 2's subject.

The four things that are not obvious, each from a review finding:

- The per-suite bound and the run wall are BOTH derived from `selftest-budgets.txt`. Rev-2 borrowed
  the wall from `run-gates.sh --print-profile`, which declares 10800s against a population declaring
  13600s for one suite, so it sat below its own largest per-suite bound.
- `timeout` is resolved over a candidate list and its absence REFUSES. `lib-selftest.sh` runs
  unbounded without it, which is right for arms that are seconds long and fatal for a mode that
  renders every verdict after the pool drains.
- `wait -n` is probed ONCE outside the loop. `wait -n || wait` reads a red suite as a missing
  capability and collapses the pool to a barrier per suite.
- `local k=$1 d="$SWEEP_ROOT/$k"` expands the whole line before `local` assigns anything, so `$k` is
  unbound under `set -u` and every background arm dies silently leaving no verdict file. Found by
  running it, not by reading it.
