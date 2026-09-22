# Build brief — TOOL-dRetiredFork-10

**Serves:** journal TOOL-dRetiredFork-10

## What the unit is

Three workflow gates spell `tools/` in their population filter and their hook path. Those literals
generate `nc carve-out 10/20`, `11/20`, `12/20` and inCMS rows 16, 17 and 18 — six declared
divergence rows across two adopters, for a path each script can resolve from its own location.

## The pre-wiring measurement changed the design, and that is why S4 exists

S4 required running the candidate predicate over gov's tree BEFORE wiring, printing hits and
near-misses. It did, and it refuted S2's mechanism:

- a basename anchor on `workflows/` NARROWS review-join's population from 7 to 5, dropping
  `tools/hooks/scratch-guard.js` and `tools/memory-recall/recall-opened.js`
- AC5 requires the population stay at 7
- §5 anticipated the risk as WIDENING, so narrowing was not a foreseen case

**Parked, and building on the derived prefix.** `git rev-parse --show-prefix` from the script's own
directory yields `tools` here and `scripts` at both adopters, reproducing the 7-file population
exactly with no literal in the source. Basename anchoring stays where it belongs — the HOOK path,
which is one file. A subtree cannot be named by a basename when the subtree's NAME is the variable.

## The trap already paid for once

Deriving the prefix by subtracting `git rev-parse --show-toplevel` from `pwd` silently yields an
unmatchable string on MSYS: `pwd` gives `/c/projects/...` and `--show-toplevel` gives
`C:/projects/...`. Measured — population 0, no error. Let git compute the relative path.

## The probe chain must reach three layouts, not two

`$HERE/hooks/agent-cap.js`, then `$HERE/../hooks/agent-cap.js`, then
`$ROOT/.claude/hooks/agent-cap.js`, then REFUSE naming what it tried. The third rung is mandatory:
NicoCares installs hooks at `scripts/hooks/`, and inCMS has no `scripts/hooks/` at all — its only
copy is `.claude/hooks/agent-cap.js`. A two-rung chain strands inCMS.

## What each criterion demands

AC1 byte-identical verdicts and population sizes against the pre-change runs, captured before any
edit · AC2 a fixture installed at `scripts/` resolves and exits 0 · AC3 a fixture whose only hook is
at `.claude/hooks/` resolves · AC4 an unresolvable hook REFUSES naming its probes · AC5 the
pre-wiring run recorded with hits and near-misses, population still 7 · AC6 kit-versions green AND
non-zero with one marker reverted, because the bare green cannot fail.

## The one place this unit does not practise what it enforces

F1, ratified: the third rung `.claude/hooks/` stays a literal, declared in the header as the
harness's own convention rather than an install prefix. Say so where a reader meets it.
