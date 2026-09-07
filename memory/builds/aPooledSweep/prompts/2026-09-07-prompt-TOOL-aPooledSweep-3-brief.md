# Brief — TOOL-aPooledSweep-3, pool safety observed rather than assumed

**Serves:** journal TOOL-aPooledSweep-3

What this pass was handed: the unit's spec at rev-3, both spec audits, and the runner at a47abd9a.

What it builds: the observation. The private `TMPDIR` per pool slot landed with unit 1's
`_rs_sweep_one` because that is the line that spawns a suite; this pass adds the check that it held,
and the arm that would notice if it stopped holding.

One arm, over the tracked working tree, and the deletion of the second one is the finding rather
than a simplification. Listing the git common dir would red on any sibling session running the bar:
that directory holds `gate-bar-queue`, `gate-ledger.tsv`, `gate-logs`, `gate-run`,
`gate-timings.tsv`, `unattended-landed`, `index`, `logs`, `refs` and `ORIG_HEAD` on this checkout
today, every one written by ordinary tooling, and the window between the two readings is as wide as
the longest suite. An arm asserts it does NOT red, so the two edges are pinned rather than one.

`--untracked-files=no` is a flag and not a default: without it this build's own sweep would have
redded on the review report it had just written.

The liveness assertion is that the command SUCCEEDED, not that its output was non-empty — `git
status --porcelain` is empty on a clean tree, so emptiness is the ordinary case and cannot
distinguish a working probe from a broken one.
