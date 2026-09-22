# TOOL-aBatchedTribunal-1 — the review protocol becomes a gate, not a note

**Status:** CLOSED · rev-3 · 2026-08-09 · node a · Tier-2 · base a938fb0c · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-09-review-TOOL-aBatchedTribunal-1-7.md](../reviews/2026-08-09-review-TOOL-aBatchedTribunal-1-7.md) | diff-review | TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-8 |
| [2026-08-08-review-TOOL-aBatchedTribunal-1-3.md](../../aDrainedSluice/reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md) | diff-review | TOOL-aDrainedSluice-1 TOOL-aDrainedSluice-2 TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-4 TOOL-aDrainedSluice-5 TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

Adopt `memory/review-workflow-protocol.md` (upstream inCMS, binding charter) into this repo, and
dogfood it. The protocol's central rule is **≤5 verify-stage agents TOTAL per review** — batch size
grows with the finding count, the agent count never does — on top of **≤5 concurrent**.

The trigger is not theoretical. Earlier in this session I wrote a bespoke closing-review workflow
whose verify stage was `all.map((f) => () => agent(...))`: one skeptic per finding, 47 agents and
3.65 M subagent tokens in the wave before it. And this repo ALREADY knows the rule — `drift-audit-code.js`
and `drift-audit-state.js` both compute `chunk(indexed, Math.ceil(len / MAX_VERIFIERS))` and one of
them carries the rule as a comment. Two files obey it, one (`tier2-review.js`) does not, and nothing
gates any of them.

The review of rev-1 changed this unit's centre of gravity and the change is the point: **the script
that broke the rule was never a file.** It was an inline `script` string on a `Workflow` tool call.
Measured from this session's transcript: four `Workflow` calls, all with `tool_input.script`, zero
with `scriptPath`. A source gate over `tools/**/*.js` structurally cannot see that, so a gate alone
would have covered four already-compliant harnesses and zero of the observed failures.

## 2. Scope (IN)

- **S1** — the protocol lands at `memory/guides/REVIEW-PROTOCOL.md` (checked against the structure
  lint: `guides` is an accepted, opaque depth-2 directory — the memory root is not), cited from
  `AGENTS.md` as binding, and shipped to adopters as `tools/workflows/REVIEW-PROTOCOL.template.md`.
- **S2** — the numbers are RE-STATED FOR THIS TREE, not transcribed. Upstream's `≤25 agents`,
  `~11–25 total`, its ROI archive path, its node registry, its `settings.agentcap.snippet.json` and
  its `tier2-review-indexed.js` filename are facts about ITS tree. Each is re-measured here, or
  re-pointed at this repo's equivalent, or dropped.
- **S2b** — `guides/` joins `corpus_ids.py`'s present-tense corpus regex, so the new document's
  citations are actually watched by check 15. Without that edit the port's own safety net does not
  cover the port. `DEAD_PATH_PIN` is re-measured after.
- **S3** — `tier2-review.js` stops scaling its verifier count: `chunk(allFindings, 5)` (fixed group
  size → `ceil(N/5)` agents) becomes the bounded-group-count form the two drift-audit harnesses
  already use, `chunk(x, Math.ceil(x.length / MAX_VERIFIERS))` with `MAX_VERIFIERS = 5`. No new
  helper: three files converge on the shape two of them already have.
- **S3b** — the partition is CONTIGUOUS in id order and every group is NON-EMPTY. The harness labels
  batches `verify:ids-<first>-<last>`, so a round-robin split would name a range that does not
  contain most of its ids; and `min(n, len)` groups, never an empty agent.

### The enforcement point, which is the substance of this unit

- **S4** — the arity rule lives in **`tools/hooks/agent-cap.js`**, the `PreToolUse` on the `Workflow`
  TOOL CALL. That is the only place that sees an inline `script`, which is the modality that actually
  failed. It gains a second rule beside the existing raw-primitive ban.
- **S4b** — `agent-cap.js` also reads `tool_input.scriptPath` off disk instead of exiting 0. A node
  hook has `fs`; today a saved script is unscanned, which is a documented hole the moment anyone
  saves the offending script to a file. A `name:`-only run stays unscannable and is DECLARED as such
  rather than implied to be covered.
- **S5** — the predicate is a LEXICAL WHITELIST, not a blacklist, because provenance is undecidable
  from a line: `batches.map((g) => () => agent(...))` is textually identical whether `batches` came
  from a bounded split or from `chunk(all, 1)`. An `agent(` call reached through an iteration
  construct is allowed only when its receiver is either
  **(a)** an identifier assigned exactly once in the file on a line carrying the `gov:fixed-verifiers`
  marker, where that line spells `chunk(<x>, Math.ceil(<x>.length / <K>))` or `splitInto(<x>, <K>)`
  and `<K>` is an integer literal ≤ 5 or an identifier bound in the file by `const <K> = <integer
  literal ≤ 5>`; or
  **(b)** an identifier assigned exactly once from an ARRAY LITERAL whose element count is visible in
  the source and is ≤ 6 — the finder-lens case, where the agent count IS a constant.
  Everything else reds: a `for`/`while`/`forEach` body containing `agent(`, a `.map`/`flatMap`/
  `Array.from` over a receiver with no qualifying assignment, a marked line whose second argument is
  an expression, `all.length`, a parameter, or a literal > 5.
- **S5b** — the marker is copied from what already works. `gov:bounded-fanout` is exactly this shape:
  an author's claim, plus a gate that checks the claim's SHAPE so the claim cannot be made falsely.
  The new marker checks the ARGUMENT, so `chunk(all, 1) // gov:fixed-verifiers` reds.
- **S6** — **ONE implementation of the predicate, two entry points.** `tools/workflows/check-verifier-fanout.sh`
  does not re-implement the rule in awk; it feeds each workflow script to `node tools/hooks/agent-cap.js`
  as a synthesized `{"tool_name":"Workflow","tool_input":{"script":<contents>}}` payload and reports
  what the hook says. A bash copy of a node predicate is the two-answers-to-one-question class this
  repo keeps a catalogue record about, and it would drift the day either side is tightened.
- **S6b** — the gate takes explicit file arguments (the self-test's fixtures live under `mktemp -d`,
  never in the repo, so a red fixture cannot make the merge bar permanently red), carries a
  `SELF_EXCLUDE` for itself and its test, and FAILS on an empty population.

### The cap, and the copies

- **S7** — the concurrency cap moves 6 → 5. The protocol's stated cause — a ~40-agent burst tripped
  the server rate limiter twice, ~3 M tokens wasted — is a fact about the shared service, not about
  the tree that measured it.
- **S7b** — the sites are ENUMERATED, and `AGENTS.md` is not one of them (it carries no number).
  `tools/hooks/agent-cap.js`, `.claude/hooks/agent-cap.js` (measured: byte-identical today, and
  NOTHING gates that), `tools/hooks/agent-cap.test.sh`'s three cap-6 fixtures, `tier2-review.js`'s
  helper default and `meta.description`/`phases`, and `parallel-coding-governance.template.md`
  (digit-for-digit, so the ≤32 KiB gate is unaffected at 32758/32768).
- **S7c** — the two hook copies get a parity assertion of their own. Today `check-wiring.sh` checks
  the hook is WIRED, never that the wired copy matches the kit's.
- **S8** — `AC5` is restated to what the hook can actually decide. `agent-cap.js`'s own header says
  it "doesn't verify the numeric arg — it enforces use the helper", and its self-test passes
  `boundedParallel(...,6)` as an ALLOW case. Asserting "a cap of 6 is denied" would have made a
  builder add unspecced numeric parsing that reds three existing fixtures. The cap constant is
  observable only in the deny text; that is what the test asserts.
- **S9** — `check-review-join.test.sh` pins `version: '1.1'` on `tier2-review.js` by literal, so the
  version bump this unit makes would red it. The pin relaxes to a well-formedness match and gains
  POSITIVE arms for the new construct, matching the existing pattern that asserts the indexed join is
  present rather than only that the old one is absent.
- **S10** — the protocol's other binding rules land as prose in the same document, because they are
  the reasoning that makes the number make sense: precision as the #1 token lever, matching intensity
  to target richness, scaling by lenses not skeptics, stopping the re-review once the design is
  judged clean, and the schema discipline (never hand-serialize a large body; re-state required keys
  per iteration; avoid `additionalProperties:false`).
- **S11** — the closing adversarial review of the `aDrainedSluice` diff, started in the banned shape
  and stopped, is re-run through the batched harness.

## 3. Non-goals (OUT)

- Porting inCMS's ROI archive, node registry, tier TRIGGERS, or file paths. A transcribed path that
  does not exist here is the dead-citation class check 15 exists for — and S2b is what puts the new
  document inside check 15's population so that claim is true rather than decorative.
- A runtime cap. Workflow scripts run in sidechains with no hooks and no filesystem, so nothing can
  count agents as they spawn. Both enforcement points are STATIC and the spec says so.
- Covering a `Workflow({name:'…'})` run of a saved workflow. The hook receives no source for it. That
  hole is declared, not papered over: the saved workflows live in `tools/workflows/` and are covered
  by the merge-bar gate instead.
- Retiring `tier2-review.js`, or introducing a second harness. It is already index-keyed, already
  batched, and already separates `unverified` from `refuted`.
- A `splitInto` helper. The bounded form already exists in two shipped files; adding a third spelling
  of it would be the two-answers class again.

## 4. Design

### Data model

```
MAX_VERIFIERS : a constant, 5, bound by `const MAX_VERIFIERS = <int literal>` (or `a.maxVerifiers || 5`)
batches       : chunk(x, Math.ceil(x.length / MAX_VERIFIERS))  -> min(MAX_VERIFIERS, x.length)
                NON-EMPTY, CONTIGUOUS groups; agent count bounded, batch size grows
marker        : `// gov:fixed-verifiers` on the assignment line, checked for SHAPE not just presence
```

`chunk(x, K)` (fixed group size) and `chunk(x, ceil(len/K))` (fixed group count) differ only in the
second argument, and that difference is the entire mechanical content of the protocol's hard cap.

### Inventory

| File | Change |
|---|---|
| `memory/guides/REVIEW-PROTOCOL.md` | new — the binding document |
| `tools/workflows/REVIEW-PROTOCOL.template.md` | new — the shipped copy |
| `tools/workflows/check-protocol-parity.test.sh` | new — the workflows kit's OWN parity check (the memory-tree kit's `kit-dogfood-parity.test.sh` must not learn about another kit's pairs) |
| `tools/hooks/agent-cap.js` | the fan-out arity rule; reads `scriptPath`; CAP 6 → 5 |
| `.claude/hooks/agent-cap.js` | the wired copy, kept byte-identical |
| `tools/hooks/agent-cap.test.sh` | cap fixtures 6 → 5; arms for the new rule; the copies' parity |
| `tools/workflows/check-verifier-fanout.sh` (+ test) | new gate — delegates the predicate to the hook |
| `tools/workflows/tier2-review.js` | bounded group count, contiguous non-empty, marker, cap 5, version |
| `tools/workflows/drift-audit-{code,state}.js` | the marker on their already-correct lines |
| `tools/workflows/check-review-join.test.sh` | version pin relaxed; positive arms for the new shape |
| `tools/memory-tree/corpus_ids.py` | `guides/` joins the present-tense corpus (+ selftest arm) |
| `.memory-tree.conf` | `DEAD_PATH_PIN` re-measured |
| `parallel-coding-governance.template.md` | cap 6 → 5 (digit-for-digit) |
| `AGENTS.md` · `tools/gate-legs.json` | the protocol named binding; the new legs |
| `memory/gotchas/` | one bug-class record: the linear verify fan-out |

### Migration

None. `tier2-review.js`'s `args` contract is unchanged.

### Rollout

Three commits — the protocol, the enforcement, the dogfood — so the document landing is separable
from the gate.

### Alternatives rejected

- **A source gate alone.** Rejected by measurement: the offending script was an inline tool-call
  string, and `tools/**/*.js` cannot contain one. Zero coverage of the only class that has failed.
- **A blacklist of banned spellings.** Rejected: `batches.map(cb => () => agent(...))` is the SAME
  TEXT before and after the fix. A blacklist can only ban a spelling; the defect is a provenance.
- **Blessing a helper by NAME.** Rejected: `splitInto(all, all.length)` is `chunk`-by-1 wearing the
  blessed name. The gate checks the ARGUMENT.
- **Capping by slicing to 5 batches.** Rejected: silently dropping findings past batch 5 reports a
  clean bill for findings nobody judged — worse than the linear fan-out.
- **Re-implementing the predicate in the bash gate.** Rejected by S6: two implementations of one rule
  drift, and this repo has a catalogue record about exactly that.

## 5. Production-readiness checklist

- security — the hook now reads a file path supplied in the tool call. It only READS, only to scan,
  and a read failure is a NAMED refusal rather than a silent allow.
- perf / scale — this unit is the perf work: a review's verify stage goes from O(findings) agents to
  O(1). Measured baseline: 47 agents / 3.65 M tokens unbatched, 9 agents / 0.81 M batched for the
  rev-1 review of this spec.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — 0 findings skips the verify phase; 1–4 findings spawn that many
  agents, never an empty one; an unreadable `scriptPath` is a named refusal; an empty gate population
  fails.
- observability — the harness logs `<N> findings → <M> verifiers`, so the ratio is in the transcript
  rather than inferred from the agent list.
- risks — a skeptic judging 40 findings at once judges them less carefully than one judging 5. That
  is the protocol's ratified trade; precision (confirmed / (confirmed + refuted)) is the metric, and
  the harness already reports `unverified` separately so a batch that drops ids is visible rather
  than counted as clean. Measured on this spec's own review: 18 confirmed / 20 raw, 0 unverified.
- migration / rollback — three commits; the harness's contract is unchanged.
- user docs — `AGENTS.md`, the kit README, the shipped template.

## 6. Acceptance criteria

- **AC1** — When `splitInto`/`chunk` arithmetic is extracted from `tier2-review.js` and executed for
  N ∈ {0, 1, 4, 5, 7, 70}, it yields `min(N, 5)` groups, none empty, sizes differing by at most one,
  CONTIGUOUS in id order, and the concatenation equals the input exactly once per element.
- **AC2** — When a script fans one agent per finding — as `.map`, as `flatMap`, as `Array.from`, in a
  `for` body, in a `forEach` body, or through a RENAMED receiver — the hook denies it, naming the
  line. All six spellings are fixtures.
- **AC3** — When the marker is applied falsely — `chunk(all, 1) // gov:fixed-verifiers`,
  `splitInto(all, all.length)`, a second argument that is a parameter or a member access, or a
  literal > 5 — the hook denies it.
- **AC4** — When `tier2-review.js`, `drift-audit-code.js` and `drift-audit-state.js` are fed to the
  hook, it allows them; when the fixed lens array is fanned over, that is allowed too.
- **AC5** — When `agent-cap.js` denies anything, its remediation text names cap **5**, and `CAP`
  resolves to 5 with `AGENT_CAP` unset. The allow/deny decision on the raw-primitive rule is
  unchanged, and the hook still does not parse the helper's numeric argument — that check belongs to
  the marker rule, which reads the argument it is given.
- **AC6** — When `tool_input.scriptPath` names a file, the hook scans that file; when the file cannot
  be read, it refuses by name; when only `name:` is given, it exits 0 and the gate's coverage of
  `tools/workflows/` is what carries that case.
- **AC7** — When `tools/hooks/agent-cap.js` and `.claude/hooks/agent-cap.js` differ by a byte, a gate
  leg reds.
- **AC8** — When `memory/guides/REVIEW-PROTOCOL.md` and its shipped template differ, the workflows
  kit's own parity leg reds — and the memory-tree kit's parity gate is not taught about it.
- **AC9** — When the gate's population is empty, it FAILS; its fixtures live outside the repo.
- **AC10** — When the closing review of `aDrainedSluice` is re-run, it runs through the batched
  harness and its verify stage spawns at most 5 agents.
- **AC11** — When the full bar runs, it is green, and `DEAD_PATH_PIN` is re-measured rather than
  inherited.

## 7. Gates

`bash tools/run-gates.sh`. New legs: `check-verifier-fanout.sh` + its self-test, and the workflows
kit's protocol-parity check. The agent-cap self-test grows the new arms and the copy-parity
assertion.

## 8. Open questions

none — the two forks below are RESOLVED; kept for the record.

- **Fork A — cap 5 or keep 6?** RESOLVED: 5. The stated cause is the shared rate limiter, not a
  property of the tree that measured it, and keeping 6 would make this repo's copy of the protocol
  contradict its own first paragraph.
- **Fork B — tracked-only or tracked-plus-untracked for the source gate?** RESOLVED, and the question
  was on the wrong axis: the review measured that the offending script was never a FILE at all. The
  answer is that the primary enforcement point is the hook (which sees the tool call), and the source
  gate is the second line over `tools/workflows/`, tracked-plus-untracked-and-unignored to match the
  JavaScript gates V7 already widened.

## 9. Revision log

- rev-3 · 2026-08-09 · CLOSED. W1 and W2 landed, then the batched closing review of the whole
  session diff found the shipped rule FAILING OPEN: an unrecognised fan-out receiver fell through to
  ALLOW, and five bypasses followed from it — a marker on the agent() line, a `.filter().map()`
  chain, a call-result receiver, a spread literal, `[].concat(x)`, a reassigned receiver, a braceless
  loop body, a marked `.concat()` derivation, and `.reduce()`. All ten are now fixtures, and the
  decision is fail-closed. The same review found `--session` rewriting file bytes unattended over a
  population bounded only by an adopter's `.gitattributes` — settings.json rewritten, a PNG corrupted
  — plus a NUL guard written with a byte bash cannot hold (so it skipped everything), an `xargs`
  word-split that collapsed the population on a spaced path, and floors that never checked whether
  their gate still existed. All fixed here. Four findings stay OPEN as backlog rows rather than being
  fixed under time pressure: they are named in `memory/backlog/TOOL.md`.

- rev-2 · 2026-08-09 · folded the rev-1 review: 20 raw findings, 18 confirmed by 5 batched skeptics,
  0 unverified. Four changes of substance. (1) The enforcement point MOVES to `agent-cap.js` —
  measured from this session's transcript, the offending script was an inline `script` string and a
  file-population gate cannot see one, so rev-1 bought coverage of four already-compliant harnesses
  and none of the observed failure. (2) The predicate becomes a marker-checked WHITELIST, because
  `batches.map(...)` is the same text before and after the fix and only its provenance differs.
  (3) No `splitInto`: `drift-audit-{code,state}.js` already compute the bounded form, so the three
  files converge on the shape two of them have. (4) `AC5` is restated — the hook explicitly does not
  verify the numeric argument, and the drafted AC would have forced unspecced parsing that reds three
  existing ALLOW fixtures. Plus: the document moves to `memory/guides/` (the memory root reds the
  structure lint), `guides/` joins check 15's population, the workflows kit gets its OWN parity check
  rather than teaching the memory-tree kit about it, the version pin in `check-review-join.test.sh`
  relaxes, and `.claude/hooks/agent-cap.js` is named as the second copy with a parity leg.
- rev-1 · 2026-08-09 · initial draft, written from the upstream protocol plus this session's own
  violation of it.

## 10. Reuse audit

The marker mechanism is `gov:bounded-fanout` reused one rule over — an author's claim plus a gate on
the claim's shape — in the file that already implements it. The bounded batch arithmetic is copied
from `drift-audit-code.js`, which already has it, rather than invented; the change to
`tier2-review.js` makes three files agree instead of adding a fourth idea. The predicate has ONE
implementation and the bash gate delegates to it, so there is no second answer to the arity question.
The document follows `HYGIENE.md` + `HYGIENE.template.md`'s copy-and-parity shape, but with the
parity check owned by the workflows kit, since the memory-tree kit's gate must not learn another
kit's pairs. The gate's explicit-file mode, `SELF_EXCLUDE` and empty-population failure are
`check-review-join.sh`'s, whose reasons apply here verbatim.
