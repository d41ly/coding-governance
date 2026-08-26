# review-harnesses — the workflow scripts, and the trust accounting they do or do not carry

```toml
feature = "review-harnesses"
title = "Workflow review harnesses — one pipeline, three implementations, one hardened"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = [
  "workflow script syntax",
  "review-join ban (no ref-keyed join)",
  "review-join self-test",
  "tier2-review self-test",
]
kits = []
git-hooks = []
workflow-scripts = [
  "check-workflow-syntax.js",
  "drift-audit-code.js",
  "drift-audit-state.js",
  "tier2-review.js",
]
skill-engines = []
rendered-skills = []
gotcha-classes = ["degradation-known-but-unreported.md"]
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/workflows/*",
]
```

## Constraints & why

**A workflow script has no filesystem and cannot import.** Everything it branches on arrives through
`args`, which is delivered as a STRING even when the caller hands it JSON. The consequence that
surprises every new author is that a lens catalogue cannot be read from a declaration file by the
harness itself, and that a shared helper module is not available — `boundedParallel` and `chunk` are
inlined byte-alike into all three harnesses on purpose. The governance template instructs that
duplication explicitly rather than treating it as debt, so the charter's factory-at-instance-two rule
does not apply to these files.

**The fan-out is bounded at the tool call, not in the file.** `tools/hooks/agent-cap.js` reads the
inline `script` string on a `Workflow` call and denies a raw fan-out primitive, an `agent(` fanned
over a receiver it cannot prove bounded, or a bound it cannot resolve to an integer at or below its
own constant. Two authoring traps live here: the batching assignment must be ONE line ending in its
marker comment, and a trailing semicolon on a bound constant declaration defeats the binder.

**A sidechain agent holds no `Agent` tool**, so a harness cannot delegate a review kind to a child
that runs its own lenses. That capability is absent rather than policed, which is why the fan-out
decision has to be made in the orchestrator.

## Shared seams

`tools/workflows/check-review-join.sh` scans every `*.js` under `tools/` with NO marker filter, so a
new harness landing in this directory is graded from its first commit. `check-verifier-fanout.sh`
and `check-workflow-syntax.js` both select their population by the literal `export const meta =`
regex, so a harness spelling that export any other way silently drops out of both. That is a real
selection seam and not a formality.

`check-verifier-fanout.sh` delegates its predicate to `tools/hooks/agent-cap.js` rather than
re-implementing it, which is the shape any second entry point on a hook predicate should copy: one
predicate, two callers.

The three harnesses share a pipeline that is not shared code — primed lenses, batched skeptics
defaulting to refute, one synthesis, joined on an integer the orchestrator assigns.

## Gaps

- **The pipeline is still implemented three times, but the three now carry the same accounting.**
  `TOOL-dTieredTribunal-3` ported it: both drift-audit siblings gained the dead-lens count, the
  dead-skeptic count, the spurious and duplicate and conflict counters, the synthesis-death log, and
  two guarded early returns — one for an all-dead lens fan and one for an empty configured set, which
  are different states and had been collapsible into a `0 === 0` misread. `lensesRun` is the
  SURVIVING count in both, an integer, where `drift-audit-state.js` had returned the configured slug
  list and `drift-audit-code.js` had returned nothing. A disagreeing repeat verdict now DEMOTES its
  finding to unverified instead of keeping whichever arrived first. What remains true is the shape:
  three files, one pipeline, no shared module, because workflow scripts cannot import. A future
  divergence has nothing structural stopping it — only the provenance comments each ported guard now
  carries, naming the unit that originally earned it.
- **`tier2-review.js` takes a review KIND now, and the other two do not.** `TOOL-dTieredTribunal-11`
  gave it a closed two-value `kind` defaulting to `diff-review`, and six things dispatch on it: the
  acquire sentence, the lens catalogue, the context default, the anchor predicate, the finding
  schema's address field, and the record's kind token. A spec audit's anchor is a pinned BLOB per
  subject rather than a commit range, and the lens verifies it with `git hash-object` because the
  orchestrator holds no filesystem — which is what makes that anchor a check that can fail. What
  remains a gap is the other two harnesses, which still know only their own subject, and the fact
  that a kind is a parameter rather than a profile: adding a third would mean a third branch at each
  of the six sites, and the enforcement hook admits no registry that would collapse them.
- **The two enforcement points AGREE now, and the modality gap is closed for one rule.**
  `TOOL-dTieredTribunal-14` lifted the ref-keyed-join ban into `tools/hooks/agent-cap.js` as its fifth
  rule and made `check-review-join.sh` delegate through `--only=join`, so both entry points share one
  predicate and an inline `script` string on a `Workflow` call is judged by it. What remains true is
  the general shape: every OTHER file-scoped scanner in this directory still covers the committed
  harnesses only, and a rule that lives in a gate rather than in the hook is still blind to the
  modality where the defect happens.
- **NEITHER sibling parses `args`.** Both are `const a = args || {}` with no JSON parse, at
  `drift-audit-state.js:47` and `drift-audit-code.js:48`, so a caller handing either a string falls
  back to the current directory — the wrong-repository defect `tier2-review.js` was hardened against
  and neither sibling was. Deliberately out of scope for the port, and tracked as
  `TOOL-dTieredTribunal-4`.

## Reuse affordance

seam: tier2-review.js — reuse as the reference implementation of the pipeline and of every trust
counter; extend by copying a guard together with the comment naming the unit that earned it, because
the provenance is the only thing that stops the guard being deleted as noise later.
seam: check-review-join.sh — reuse for a source-level absence assertion over the harness population.
It no longer HOLDS a predicate: it selects the population and delegates to `agent-cap.js --only=join`,
so extend it by adding a rule to the hook and a member to that closed set, never by re-implementing
one here. Literal blanking is load-bearing and lives in the hook, because the reference harness
necessarily spells the banned expression while documenting it.
seam: agent-cap.js — reuse as the single predicate for any fan-out rule that must reach an inline
script; extend by delegating from a file gate rather than re-implementing, the way
check-verifier-fanout.sh already does.
