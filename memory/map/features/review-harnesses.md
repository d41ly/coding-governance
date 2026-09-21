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
  "orient-counterfactual.js",
  "tier2-review.js",
  "unattended-build.template.js",
]
skill-engines = []
rendered-skills = []
gotcha-classes = ["degradation-known-but-unreported.md", "node-check-is-not-a-syntax-gate.md"]
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

**`tier2-review.js` survives a dead fan (`TOOL-dDerivedDocket-29`).** Every lens and skeptic batch
writes its result under `<git-common-dir>/review-lenses/<key>/` before it returns, and `path` is
required on all three agent schemas. The key is the kind, the round, the pinned subject (the
RESOLVED base and head for a diff review) and a print of `context`, `byDesign` and `priorFindings`.
One probe agent reads the directory first, because the script has no filesystem, and a file is
reused only when its own `key` field matches; a verify file also needs its batch's claim print. Any
null agent makes the return `exit: 'deferred-platform'` with the `pending` labels and no blocker
count, and the build harness returns that deferral instead of throwing. The drift-audit siblings
keep the all-or-nothing fan. Nothing prunes old key directories.

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

**The unattended build harness is RENDERED, not shipped.** `unattended-build.template.js` is the
source, and `check-protocol-parity.test.sh --render` writes `unattended-build.js` beside it with the
kit's own directory, the tool root, and the memory-tree kit's directory filled in. Apply writes an
engine file verbatim, so the four install paths the harness spells used to reach an adopter at
another prefix naming files that adopter did not have. The third token is PROBED from the tracked
tree rather than derived from the prefix, because an adopter may install that kit flat. The harness
is claimed by the unattended dossier and its template here, because this kit renders it.

**The build harness REQUIRES a `scratch` argument, and it is the one path that cannot be rendered.**
The session scratchpad is in the caller's system prompt and nowhere a workflow script can read, and
it changes with every session, so `args` is its only carrier. The parent refuses without it and
refuses one that is not absolute by shape, folds backslashes to `/` once, spells it in `GROUND` —
the preamble every agent it spawns reads — and hands it to every child in `dispatch.args` beside
`repo`, `slug`, `mode`, `driver`, `ground` and `checklist`. `unattended-unit.js` refuses without it
and refuses a `ground` that does not name it, so a hand-composed dispatch cannot hand a child a
different root from the one its grounding sentence tells the agent to use (`TOOL-aProbedUnit-4`).
`tier2-review.js` and the drift-audit siblings still tell their agents nothing about temporary
files.

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
- **`blockers` and `highs` are COUNTED from ids, but the severities are still the synthesis's word.**
  `TOOL-dMergedTally-1` stopped the synthesis agent typing the two integers: it returns `items`, each
  a severity and the raw confirmed ids it merged, and the harness counts over raw ids and returns
  null when an id sits in no item or in two. The typed integers had counted ITEMS against a
  `confirmed` that counts raw findings, and the build harness's disposal guard subtracts one from the
  other. What stays a prompt property is that the item list matches the table the same agent wrote
  into the report: nothing re-reads the record.
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

- **`orient-counterfactual.js` is a MEASUREMENT harness, not a review one, and it is the FIRST
  file here to put the sequential-loop marker on a loop header.** `TOOL-aReplayedCard-5` shipped it: one stage-2
  orientation arm per call, two kickoffs under `for (const i of RUNS)` with `gov:sequential-agents(2)`
  over a marked two-element literal, tokens as `budget.spent()` deltas and wall as the agent's own
  `date` readings, every run under a closed four-value `outcome`, and a single default-type fallback
  spawn OUTSIDE the loop because the hook admits one marked loop per script. It carries no lens, no
  skeptic and no synthesis, so none of the trust accounting above applies to it; what it shares
  with its siblings is the `args` parse-then-refuse guard and the returns-a-record-writes-nothing
  shape. Its agent definition ships beside it as `orient.agent.md`, which the inventory
  does not key — a template the runner copies to `.claude/agents/` by hand is not a workflow script.

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
seam: check-protocol-parity.test.sh — reuse as this kit's ONLY renderer, and as the leg that grades
what it rendered; extend by adding a `PAIRS` row and a `rendered` rule in `kit.toml`, never by
writing a second renderer. A template in the kit dir with no row reds, so a new one cannot ship
ungraded. A token only some templates carry is resolved PER PAIR: an unanswered probe skips, by name
and out loud, only the pairs whose template needs it, so a new token cannot cost an install the
pairs that never use it (`TOOL-dPolishedVitrine-1`, round 1 F3).
