# Brief — TOOL-aPooledSweep-2, the withheld cost verdict

**Serves:** brief TOOL-aPooledSweep-2

What this pass was handed: the unit's spec at rev-3, both spec audits, and the runner at 6ab577de
with unit 1's pool already in it.

What it builds: the claim about what a pooled NUMBER means. A condition tag composed once per run,
`withheld` on every row that ran, a summary count of what was withheld, and — because rev-1 asserted
a `--rank` refusal that turned out not to exist — the refusal itself.

Two things that decide the shape:

- The refusal sits BEFORE the `CONDS` loop, not inside it. A `CONDS` match is what RANKS a row: the
  loop breaks on the first hit and appends to `rows`, and only the for/else fall-through reaches
  `unbacked`. A pooled entry in `CONDS` would have ranked the contended reading.
- `unbacked` is already a total refusal — it names every offending row and raises `SystemExit(1)`.
  That is correct rather than a limitation: a denominator missing its largest members is not a
  majority. So the criterion asserts the total refusal and stages a clean file beside it to prove
  the predicate is not a blanket.

The round-trip arm is the one that earns its keep: it captures the tag from a real `--sweep` and
feeds that exact string to `--rank`, so a spelling drift on either side reds. Building it found a
real defect in unit 1 — the wall watchdog inherited the caller's stdout, so a `$(... --sweep ...)`
capture blocked for the whole wall.
