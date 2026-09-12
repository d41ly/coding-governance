# `tools/workflows/` — the review harness and the gates over it

Three gates in this directory read the tree and delegate their verdict to the agent-cap hook:

| gate | what it judges |
|---|---|
| `check-review-join.sh` | no ref-keyed verdict join, and every agent wave a source scan can see is counted |
| `check-verifier-fanout.sh` | the committed harnesses obey the verify-stage cap |
| `check-workflow-syntax.js` | every workflow script parses |

`tier2-review.js` is the ready-made harness they exist to protect. It carries this directory's
version under **two** kit ids, and both are paired — see its line 3 and `check-kit-versions.sh`.

## What this kit RENDERS, and its one renderer

`check-protocol-parity.test.sh --render` writes both artifacts below, and the same script with no
argument is the leg that grades them:

| rendered | from | tokens |
|---|---|---|
| `<memory root>/guides/REVIEW-PROTOCOL.md` | `REVIEW-PROTOCOL.template.md` | `TOOL_ROOT` |
| `unattended-build.js`, beside its template | `unattended-build.template.js` | `KIT_DIR`, `TOOL_ROOT`, `MEMORY_TREE_DIR` |

**Edit the template, never the render.** The build harness names four install paths: the driver,
the bug-class checklist, the review sub-workflow it awaits and the child it hands the caller. A
workflow script has no filesystem when it runs, so it cannot find its siblings, and apply would
write a shipped copy verbatim, naming this repo's `tools/` layout in every adopter. So the kit
renders it instead, and `kit.toml`'s `[[regenerate]]` block re-runs the render on an update run
with `GOVKIT_RERENDER=1`. With `GOVKIT_RERENDER` unset `update` re-renders nothing and prints
nothing about it, and the parity leg is what reds the stale copy at your next bar.

**`MEMORY_TREE_DIR` is probed, not derived.** An adopter may install the memory-tree kit flat in
its tool root, so the tool root plus `memory-tree/` is not an answer. The render takes the first
TRACKED of `{{TOOL_ROOT}}memory-tree/gotchas.py` and `{{TOOL_ROOT}}gotchas.py`. When neither is
tracked it SKIPS the harness pair out loud and still renders and grades the protocol, because this
kit requires only agent-cap and an install without the memory-tree kit is legal. If yours is
somewhere else, run the render with `MEMORY_TREE_DIR=<dir>` exported; an override naming nothing
tracked is refused. That override comes only from the environment, so a tree that needs it on its
bar exports it there too. A template in this directory with no pair in the script is a red, so a
new one cannot ship ungraded.

**An install from before 1.8 rows the harness as an engine file**, and `update` keeps that role, so
it writes gov's own render and cannot move the row. The migration that converges, verified on a
fixture, is in the coding-governance runbook's Maintenance section, under "The build harness is
rendered from review-harness 1.8".

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
