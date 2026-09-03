# `tools/workflows/` — the review harness and the gates over it

Three gates in this directory read the tree and delegate their verdict to the agent-cap hook:

| gate | what it judges |
|---|---|
| `check-review-join.sh` | no ref-keyed verdict join, and every agent wave a source scan can see is counted |
| `check-verifier-fanout.sh` | the committed harnesses obey the verify-stage cap |
| `check-workflow-syntax.js` | every workflow script parses |

`tier2-review.js` is the ready-made harness they exist to protect. It carries this directory's
version under **two** kit ids, and both are paired — see its line 3 and `check-kit-versions.sh`.

## How the three find things — stated ONCE, for all of them

**None of these scripts spells an install prefix.** They ran with `tools/` hard-coded until
`TOOL-dRetiredFork-10`, which cost three carve-outs at one adopter and three divergence rows at
another — six hand-maintained records for a path each script can work out from where it is standing.

**The population.** Each shell gate derives the kit directory from its own location and scopes the
population to it:

```sh
HERE="$(cd "$(dirname "$0")" && pwd)"
KIT_PREFIX="$(cd "$HERE/.." && git rev-parse --show-prefix)"   # `tools` here, `scripts` at adopters
```

Two things about that line are load-bearing and neither is obvious.

*Git computes the relative path.* The tempting spelling — subtract `git rev-parse --show-toplevel`
from `pwd` — is broken on MSYS, where `pwd` yields `/c/projects/...` and `--show-toplevel` yields
`C:/projects/...`. The subtraction then leaves the string untouched, the population matches nothing,
and there is no error: measured at population 0 during the unit that wrote this.

*An empty prefix is a real layout.* A kit installed at the repository root has nothing to strip, and
the population is then every `*.js` the repo holds.

`check-workflow-syntax.js` has no prefix filter at all, and that asymmetry is deliberate rather than
an oversight. It applies a `meta`-declaration marker to every candidate, so its population is already
*a file declaring workflow meta* and a prefix was doing nothing but naming a directory. The other two
apply no marker filter, so removing theirs would widen them into files whose own ban tables trip the
predicate — measured, and it reds the bar.

**The predicate.** Three rungs, tried in order, then a refusal:

1. `$HERE/hooks/agent-cap.js`
2. `$HERE/../hooks/agent-cap.js` — gov and NicoCares both resolve here
3. `$ROOT/.claude/hooks/agent-cap.js` — inCMS has no sibling `hooks/` at all, and this is its only copy

The third rung is not a fallback for tidiness; a two-rung chain strands a real adopter, which was
found by testing the derivation against both trees rather than by reasoning about one. A gate that
resolves none of the three **refuses and names what it tried** — it does not pass quietly, which is
the whole point of a gate whose verdict comes from somewhere else.

`.claude/hooks/` in rung 3 is a literal, and it is the one place these scripts do not practise what
they enforce. It is the harness's own convention rather than a prefix an adopter picks, so it stays;
said here rather than left for a reader to find.

## Running them

```bash
bash tools/workflows/check-review-join.sh              # the whole population
bash tools/workflows/check-review-join.sh --explain    # plus the resolved predicate and population
bash tools/workflows/check-verifier-fanout.sh
node tools/workflows/check-workflow-syntax.js
```

Each also accepts explicit files, which is how the suites drive their fixtures. The `--explain`
output is where the resolved predicate path is reported: the default run's bytes are pinned by an
acceptance criterion, so diagnostics that would change them live behind the flag.
