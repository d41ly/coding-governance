# Build brief — TOOL-aRatifiedRulings-3

**Serves:** journal TOOL-aRatifiedRulings-3

The pass this brief was handed to builds unit 3 of `aRatifiedRulings` at rev-3. The spec is
`memory/builds/aRatifiedRulings/spec/2026-09-13-spec-TOOL-aRatifiedRulings-3.md` and it is
authoritative; the ruling it implements is `TOOL-aLeakedHandle-8` in `memory/DECISIONS.md`.

## THE OWNER'S INSTRUCTION, FIRST

**A pass runs the fast diff-scoped gates and nothing held.** The previous pass ran five hours
stacking more than twenty full suite runs concurrently on this box; the owner stopped it. No
self-test suite, no held leg, no `run-gates.sh` bar inside this pass. The full bar is `--close`'s
and the push boundary's, which is M6's own rule.

**This unit's SUBJECT is a suite, so it runs that suite — ONCE per measurement, ALONE, never
concurrently with another run of itself or with a bar.** The spec's acceptance is a before/after
timing plus trace attribution. That is two timed runs of `check-memory-hygiene.test.sh` in this
pass: one before your change on the base bytes (or take the spec's §4 figures, which were measured
on this node at base, and say so), one after. Not seven. Not a shard fan. If you need a third, say
why in the ledger. Every other check is fast and diff-scoped: hygiene `--staged`, spec-tokens,
`--check-format`, line-length, lexicon, shell hygiene, the kickoff-manifest ratchet.

## What the pass builds

The project-keys section of `tools/memory-tree/check-memory-hygiene.test.sh` stops running the whole
checker over a `git archive` of this repository and runs one invocation per arm over the 29-file
fixture the suite already builds and asserts clean. Every red-grading arm asserts the finding's
TEXT, not rc. Candidates A, C and D were each given a losing test before measuring and lost.

## What two audit rounds settled

- **The 900 s ceiling in `tools/gate-legs.json` is not edited.** Section 3.
- **The gate criterion is ATTRIBUTION, deterministic**: zero `git archive` in the trace, the
  stated number of checker invocations. The wall figure is recorded as EVIDENCE with its spread,
  not as the gate — a bound inside the noise is a coin flip.
- **`FLOOR_ASSERTIONS` RISES to the post-change count** in the same commit that measures it.
  §8 F2 is RESOLVED. No assertion is deleted.
- **The suite is RED at base** for a cause outside the four keys — the archive fixture inherits the
  live corpus's hygiene state including `PROJECT_REGISTRY_EXTRA`. Running over the small fixture
  clears that as a consequence. Your before-run cannot print PASS; say so, and make the after-run
  the one that does.
- The suite is `chunk: selftests`, `subject: kit`, guarded on `tools/memory-tree/`; no boundary runs
  it. Disclose that in the ledger.

## The rules this pass is bound by

- Every arm's failing case OBSERVED RED first, with a positive artifact that it ran.
- Commit with the unit id in the subject; then `python tools/memory-tree/gotchas.py --for-diff
  HEAD~1..HEAD` and act on it. Flip the spec status header in the same commit.
- Re-declare WIDER with `--dispatch` before the commit if the set grows.
- `check-memory-hygiene.test.sh` is a memory-tree kit file: editing it owes the kit version
  carriers. Unit 1 already moved the kit 2.69 → 2.70 this build; read `tools/check-kit-versions.sh`
  and the spec's S-items for whether this unit owes a second move or rides the same version.

## What the pass must not do

- No sibling unit's files. No `run-gates.sh` invocation. Never `git stash`.
