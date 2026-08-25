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
gotcha-classes = []
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

- **The pipeline is implemented three times and only `tier2-review.js` carries its full trust
  accounting.** `drift-audit-state.js` and `drift-audit-code.js` lack the dead-lens count, the
  all-lenses-dead early return, the dead-skeptic count, the spurious and duplicate and conflict
  counters, and the synthesis-death log. `drift-audit-state.js` returns the CONFIGURED lens set, so a
  dead lens is invisible to its caller, and `drift-audit-code.js` returns no lens information at all.
  Both resolve a disagreeing repeat verdict by keeping whichever arrived first. Every gate on the bar
  is green over all of it, which is the point: the loss shows as absence, never as a crash.
- **No harness takes a review-KIND parameter.** The build method forbids `tier2-review.js` on a spec
  audit, which is the majority review kind in this corpus, so every spec audit is driven by a script
  authored from scratch in the session that needs it. The measured consequence is that a field a
  program emits reaches the record far more often than one a document asks a human to remember.
- **A file gate cannot see the modality where the defect actually happens.** An ad-hoc review harness
  is an inline `script` string on a `Workflow` call and is never a file, so every scanner in this
  directory covers the already-compliant committed harnesses and none of the observed failures. Only
  the PreToolUse hook reaches that modality, and the two enforcement points currently disagree: a
  cap-compliant inline script carrying a ref-keyed join passes the hook and fails the file gate.
- **`drift-audit-state.js` parses no `args`.** It is `const a = args || {}` with no JSON parse, so a
  caller handing it a string falls back to the current directory — the wrong-repository defect
  `tier2-review.js` was hardened against and this sibling was not.

## Reuse affordance

seam: tier2-review.js — reuse as the reference implementation of the pipeline and of every trust
counter; extend by copying a guard together with the comment naming the unit that earned it, because
the provenance is the only thing that stops the guard being deleted as noise later.
seam: check-review-join.sh — reuse for a source-level absence assertion over the harness population;
extend by adding a predicate to its awk, and note that comment stripping is load-bearing because the
reference harness necessarily spells the banned expression while documenting it.
seam: agent-cap.js — reuse as the single predicate for any fan-out rule that must reach an inline
script; extend by delegating from a file gate rather than re-implementing, the way
check-verifier-fanout.sh already does.
