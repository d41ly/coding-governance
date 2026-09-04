# Build brief — DEPL-dRetiredFork-3

**Serves:** journal DEPL-dRetiredFork-3

## What this unit is, and why it is the riskiest in the build

Bytes landing is not an update finishing. `UPDATE_ROLE["rendered"]` is `"adopter"` but the
disposition CAPS at report, and no `[adopt].argv` is spawned anywhere in `update`. So every rendered
destination goes one vintage stale on every update.

**Measured at NicoCares: NINE rendered rows, not the spec's eight** — three `SKILL.md` files and
both binding protocols among them. gov has shipped more since `b0108f13`; the measurement wins.

§5 calls it plainly: `update` begins executing target-side code, after a write, with a rollback that
must itself work, in a repository gov does not own.

## Two criteria this run cannot meet, and the reasons are structural

**AC10 is the build's done-condition and requires `--write` against `C:/projects/nicocares/main`.**
Two independent blocks. It is a write to a repository gov does not own, which this run has already
parked twice on §9 grounds. And its own text makes it depend on `DEPL-dRetiredFork-1` S7 driving the
unattributed count to zero — which is the parked decision, so the prerequisite does not exist.

**AC11 requires `check_runbook_parity.py` to exit 0.** It exits 1 with 18 problems today, measured
identically before and after `TOOL-dRetiredFork-16` touched the docs, and no gate leg invokes it.
Filed as `TOOL-dRetiredFork-28`.

## What IS buildable here, and the rollout the spec itself prescribes

§4's Rollout: the re-render step ships **gated OFF by default** for its first release and is flipped
on only "after in-place verification against a fixture and then one adopter". That is the charter's
dark-landing rule applied to the deployer, and it means a first release with the flag off is the
CORRECT shape rather than a partial one.

So: the `[[regenerate]]` declaration and its runner, the re-render step behind the flag, S5's
ordering refusal, and the arms. With the flag off, AC6 requires byte-identical output — which is
also what makes the increment safe to land.

## The one that must not be got wrong

S5/AC9 is the constraint `TOOL-dRetiredFork-14` delegated here and its §5 called the highest risk in
that unit: a wired command must move to the surviving hook copy BEFORE the second copy is withdrawn.
Reversed, the hook is unwired for the window between — a security guard silently off. rev-1 carried
it in scope and observed it nowhere.

## Not this unit

Running an adopter for a kit the target holds INERT — a posture flip, and exactly why "just run
apply" is not the workaround. The `merged` role, whose code says no writer exists yet. And writing a
`generated` file's bytes: §3 disclaims AUTHORSHIP, not INVOCATION, so a gov-declared `[[regenerate]]`
argv IS run while the target's own tooling stays the target's.
