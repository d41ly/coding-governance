# Build brief — TOOL-dRetiredFork-9

**Serves:** journal TOOL-dRetiredFork-9

## Two independent absorptions, both held by adopters

**S1 — a `_`-prefixed subfolder under `spec/` is not a spec.** NicoCares carries `nc carve-out
20/20`. The cause is precise: `git ls-files "$dir/spec/*.md"` uses a GIT PATHSPEC, where `*` crosses
`/` — unlike a shell glob. So `spec/_working/notes.md` is enumerated as a spec, produces a
`NOT A UNIT` row, and sits beside "every tracked spec is terminal". Two enumeration sites carry it:
`spec_ids` and the `--plan` sibling. No config key — `_` is already this tree's marker for "not part
of the set", so the rule is structural.

**S2 — C21 batches two greps instead of `2N`.** inCMS measured 132.2 s to 2.795 s with the verdict
asserted identical. The loop runs `grep -cxF` twice per build README; batched, it is two greps total
over the whole population.

## The trap in batching a per-file grep

`grep -c` omits the filename when given ONE file and prefixes it when given several, so a population
that happens to hold one build README silently changes the output shape. `/dev/null` as a first
argument forces the prefix in both cases. Get this wrong and the check passes over a one-build tree
by parsing nothing.

## What must be proved, not assumed

AC2 requires the batched verdict to be BYTE-IDENTICAL to the per-file loop's, and S3 wants a
verdict-equality arm. A speed-up that changes a verdict is not an optimisation.

## A standing instruction the spec itself flags as unverified

§3 says the unattended kit's `--selftests` must not run on this node, that this is carried in
session memory, that it has NO in-repo carrier, and that it should be confirmed with the owner. I am
honouring it — the seven `*.test.sh` legs left the bar at the owner ruling in `AGENTS.md`, and
`--checks` is the mode I run. Flagged rather than relied on silently.

## Acceptance

AC1-AC3, run rather than asserted, plus `install-prefix` and `--check-format` before committing.
