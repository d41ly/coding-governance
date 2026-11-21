**Serves:** research TOOL-dPlacedRequest-43

# Brief — dPlacedRequest: TOOL-dPlacedRequest-43 re-grounded before its build

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

TOOL-dPlacedRequest-43 (order 24, DEFERRED, rev-10) is the next unit to build. It batches 34 minor findings that land
on units this run has since built and CLOSED (among them 1, 5, 19, 24, 28, 30, 31, 33 and 34), and three of its
items reach into other specs: S11 bumps CLOSED spec 33, S22 cuts CLOSED specs over the size figure, and its S24 and
S30 are the items `TOOL-dPlacedRequest-44` S3 and `TOOL-dPlacedRequest-48` S4 rewrite in place at order 25. A builder
cannot write a spec, and the charter's P19 forbids rewriting built work in place. Re-ground the spec so a builder can
build it as written, before it is dispatched, each ruling a fork in §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### Items

1. F-closed-specs: S11's naming line lands in this spec (a line in §4 naming `TOOL-dPlacedRequest-33` the closing mechanism of round-1 findings 33 and 34), and spec 33 and spec 34 are not bumped. Reason: both are CLOSED, and P19 keeps built work out of in-place rewrites. Amend S11 and AC11 so AC11 observes that line here.
2. F-size: S22 narrows to the live specs. The spec-token checker's size join grades only LIVE specs (OPEN, SPECCED, INPROGRESS, BLOCKED), so a CLOSED spec over the figure is not a hit and is not cut. S22 and AC22 measure every live spec of this build at the pass with the checker's size join and, where one is over its cap, name it as an owed spec-writer cut rather than cutting it. Reason: P19, and the gate's own population. Probe the size join's current reading and pin its figures.
3. F-promoted: fold `TOOL-dPlacedRequest-44` S3 and `TOOL-dPlacedRequest-48` S4 in now. S24 and AC24 run unit 44's §4 oracle (the range named by parent, the stated walk, the refusal of an empty walk), and AC30 names unit 48's placed-race arm as the lock's observation; this unit builds the lock (S30) and leaves the arm and the oracle's script to units 44 and 48. Reason: spec 43 is still DEFERRED, so the in-place rewrite those units order is a spec act done here once, before it is built, and never on a CLOSED spec. Record in §9 that units 44 S3 and 48 S4 are folded here.
4. Probe every item against the tree. For each, cite where it now stands by `path#symbol`: an item a landed unit already satisfies is marked so and reduced to its observation, or dropped with the unit that closed it named; an item whose cited symbol, verb, file or field moved is amended to the tree's name; S8 and S23's READER NOT IN TREE marks are replaced with the readers as built (units 1, 24, 5 and 19 are CLOSED). Narrow the unit to what is left, and say what was narrowed.
5. Replace every line citation (a bare `path:line` or `:N`) with a `path#symbol` citation or a blob pin, and every bare file-stem section reference with its alias tag.
6. If an amendment leaves a real choice the tree cannot settle, decide it by the same rung and record it resolved; leave no fork open. Keep the spec within the live-spec size cap the checker reads.

### Acceptance

Spec 43 at rev-11 carries the three resolved forks, every amendment the re-grounding found, `path#symbol`
citations and one §9 line naming this brief; `check-memory-hygiene.sh --only 12,25 --spec`, the spec-token checker
and `bash tools/unattended/unattended.sh --check-specs dPlacedRequest TOOL-dPlacedRequest-43` report nothing.

### Gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the driver's `--check-specs` and the naming
lexicon; no other.

### Non-goals

No product code, no commit, no index render, no status flip (it stays DEFERRED), no spec other than
TOOL-dPlacedRequest-43 (units 44 and 48 are re-grounded at their own dispatch), and no fork left open. Pin every
figure you write with DERIVED or PINNED on its own line, never let a section sign or a section number stand before a
unit word, and never quote a check's hit literally in prose.
