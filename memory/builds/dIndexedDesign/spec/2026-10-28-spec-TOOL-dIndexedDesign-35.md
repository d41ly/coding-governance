# TOOL-dIndexedDesign-35 — the coverage lens runs as its own one-agent stage, so `SPEC_LENSES` stays at the agent-cap hook's five-lens bound and no checklist share reaches a lens that does not run

**Status:** OPEN · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 4 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |
| [2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`)
confirmed finding **id 28 at HIGH**, report item **H2**, the item's only id.
`TOOL-dIndexedDesign-16` S8 adds a sixth `coverage` entry to the `SPEC_LENSES` array literal of
`tools/workflows/tier2-review.template.js`. The agent-cap hook admits a lens receiver only from an
array literal of at most `MAX_LENSES` elements (`tools/hooks/agent-cap.js:450`, `:929`), and
`MAX_LENSES = 5` (`:461`) is one number the owner ratified on 2026-08-10. With six entries,
`const LENSES = isSpec ? SPEC_LENSES : DIFF_LENSES // gov:fixed-verifiers` stops resolving to a
bounded receiver and the hook denies every spec-audit run, the one unattended-build schedules
included. Dropping the lens inside the Find thunk instead leaves the checklist split, which runs over
`runningLensKeys`, handing a share to a lens that never runs.

This unit keeps `SPEC_LENSES` at five and runs the coverage lens as a separate stage of one `agent()`
call outside any iteration, the shape the harness's `probe` and `synth` calls already have. Raising
`MAX_LENSES` would widen an owner-ratified security bound, which no spec grants. It repairs
`TOOL-dIndexedDesign-16` and builds one step after it, at order 4.

## 2. Scope (IN)

- **S1** — Five spec lenses. `SPEC_LENSES` in `tools/workflows/tier2-review.template.js` keeps exactly
  its five entries, `coherence`, `grounding`, `reuse`, `blast-radius` and `failure-envelope`, and
  `coverage` is a member of neither `SPEC_LENSES`, `DIFF_LENSES` nor `LENS_KEYS`. The `LENSES` ternary
  and its `gov:fixed-verifiers` marker are unchanged. Observed by AC1 and AC2.
- **S2** — The coverage stage. Unit 16 S8's coverage brief becomes the string constant
  `COVERAGE_BRIEF`, and the stage is `phase('Coverage')` holding ONE `await agent(` call reached
  through no loop, `map` or `boundedParallel`, the receiver shape of the `probe` and `synth` calls.
  Under `coverage: 'with'` it runs after the Find stage and its findings join the finder findings,
  each tagged lens `coverage`, before the Verify stage. Under `coverage: 'skip'` it does not run and
  dispatches nothing. Observed by AC2 and AC3.
- **S3** — `only`. Under `coverage: 'only'` the five spec lenses join `skippedLenses`, so each resolves
  to the existing skipped sentinel and dispatches nothing, and the coverage stage is the only finder.
  The checklist split is not computed over an empty running set: no lens takes a share, and the
  record says the checklist was not swept. `renderAuditBinding` still writes `**Serves:** coverage-lens`
  for the run, as unit 16 S8 states. Observed by AC3.
- **S4** — No share for a lens that does not run. In every mode `deriveChecklistShares` runs over
  `runningLensKeys` alone, which never holds `coverage`, so every checklist item belongs to a lens
  that dispatched. Observed by AC4.
- **S5** — The bound probed, not assumed. A new arm feeds the agent-cap hook each rendered harness
  under `tools/workflows/` that spawns agents and requires it admitted, so a seventh array entry or a
  sixth spec lens reds at the pass that adds it. Observed by AC1.

## 3. Non-goals (OUT)

- `MAX_LENSES`, the hook's admission rules and the owner's 2026-08-10 ratification: unchanged. Raising
  the bound is an owner turn (BUILD-METHOD M3 veto 3), and no clause of this build names it.
- The lens brief's content, the `coverage` argument's values, the `coverage-lens` binding and the
  review-shape field `coverage=`: unit 16 S8 and S9. This unit moves where the brief runs.
- The README's lens list and review-shape grammar and the suite's `SHAPE_RE`: report id 29, a MEDIUM,
  batched into `TOOL-dIndexedDesign-38`.
- The five-spec-lens suite arms in `tools/workflows/tier2-review.test.sh` (`:515`, `:686`, `:2172`):
  S1 keeps them true, so none moves.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — its S8 coverage lens, the `coverage` argument's three values and `renderAuditBinding`'s `coverage-lens` line, whose sixth `SPEC_LENSES` entry S1 removes and S2 runs as `phase('Coverage')` (id 28)
- **hands-off** `TOOL-dIndexedDesign-38` — the coverage stage this unit lands, which that unit's README and review-shape item documents beside the five spec lenses (id 29)
- **hands-off** `TOOL-dIndexedDesign-39` — S1 to S4, which that unit's S1 builds inside unit 16's pass commit; this unit's own pass builds S5 and observes AC1 to AC4 (id 1)
- **hands-off** `TOOL-dIndexedDesign-44` — the coverage stage of S2 and S3, whose agent that unit joins to every finder count, dead label, finding join and durable file (id 26)
- **hands-off** `TOOL-dIndexedDesign-46` — S5's agent-cap arm, which that unit deletes, and the stage's lens-yield row and render step (ids 7, 20, 29, 30 and 33)

## 4. Design

### Evidence

- `tools/hooks/agent-cap.js:450-452`: receiver (b) is "an identifier assigned from an ARRAY LITERAL
  with <= MAX_LENSES elements"; `:461` `const MAX_LENSES = 5`, the comment above it naming the owner's
  2026-08-10 ratification; `:929` admits only when `topLevelArgs(inner).length <= MAX_LENSES`. Read
  2026-10-28.
- `tools/workflows/tier2-review.template.js:810-836` holds five `key:` entries in `SPEC_LENSES`;
  `:842` is the `LENSES` ternary, and the comment at `:838-841` calls two sibling array literals and a
  marked ternary "the ONE dialect" the hook admits.
- `:1004` `const probe = await agent(` and `:1721` `const synth = await agent(` are single calls
  outside any iteration, so a third such call needs no bounded receiver.
- `:890-891` derive `skippedLenses` and `runningLensKeys`; `:915` computes `checklistShares` over
  `runningLensKeys`; `:1176-1178` resolve a skipped lens to a sentinel that dispatches nothing.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `COVERAGE_BRIEF` | string constant, `tier2-review.template.js` | none |
| `Coverage` | phase label | none |

### Migration

None: unit 16 lands one order earlier, and no audit record has run the sixth lens.

### Rollout

Live at its pass, order 4, one above unit 16's 3, beside `TOOL-dIndexedDesign-1`, whose write set
holds no workflow file. Between unit 16's pass and this one the rendered harness carries six spec
lenses; no spec audit is scheduled inside that window, since the build run audits before its first
unit. This unit's own `--dispatch` meets unit 16's coverage refusal in that window, because no lens
reading can exist before this unit lands; `TOOL-dIndexedDesign-38` §8 F1 holds how the run passes it.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`: S1 to S4
- `tools/workflows/tier2-review.js`: its render, never the edit
- `tools/workflows/tier2-review.test.sh`: the coverage-stage arm §7 declares
- `tools/hooks/agent-cap.test.sh`: S5's arm

### Alternatives rejected

- **Raise `MAX_LENSES` to 6.** Lost to M3 veto 3: it widens a security bound the owner ratified, and
  the hook's own comment records that six was once a miscount, not an affordance.
- **A third lens array and a nested ternary.** Lost to the dialect comment at `:838-841`, which fixes
  the shape at two sibling literals and one marked ternary; a third receiver is a shape the hook was
  not written to admit.
- **Swap one spec lens out under `only`.** Lost to S3's simpler route: skipping all five through the
  existing sentinel keeps the receiver literal untouched and dispatches only the coverage agent.

## 5. Production-readiness checklist

- security — keeps the owner-ratified fan-out bound intact; S5 makes a breach red at its own pass.
- perf / scale — one extra agent under `with`; under `only` one agent instead of five.
- error / empty / loading states — a dead coverage agent is a missing finder result, deferred as a
  dead lens is; under `skip` nothing is spawned.
- observability — the record names the skipped lenses under `only` and that the checklist was not
  swept.
- risks — the stage's findings must carry lens `coverage` so the verifier and the lens-yield table
  credit them; AC2 checks the tag.
- testing — stub runs of the three modes, the hook over the rendered harness and a six-lens copy.
- migration — none.
- user docs — none under `help/`; `tools/workflows/README.md` is id 29's, in unit 38.

## 6. Acceptance criteria

- **AC1** — When a Workflow payload naming the rendered `tier2-review.js` is piped to `node agent-cap.js`
  in the hooks kit, as the `scriptPath` arm at `agent-cap.test.sh:779` feeds one, the hook admits it;
  a scratch copy whose `SPEC_LENSES` holds a sixth entry is denied naming the lens bound.
  Red when: the rendered harness is denied, or the six-entry copy is admitted.
- **AC2** — When a `node -e` stub run evaluates `tier2-review.js` with `kind: 'spec-audit'` and
  `coverage: 'with'`, it spawns five `find:` agents and one coverage agent, the coverage agent's
  findings reach the Verify stage tagged lens `coverage`, and `grep -c "key: 'coverage'"` over the
  rendered harness prints 0.
  Red when: `coverage` is a `SPEC_LENSES` entry, or its findings skip verification.
- **AC3** — When the same stub run uses `coverage: 'skip'` it spawns no coverage agent; with
  `coverage: 'only'` it spawns the coverage agent alone, no `find:` agent, and its record carries
  `**Serves:** coverage-lens`.
  Red when: a spec lens dispatches under `only`, or the coverage agent dispatches under `skip`.
- **AC4** — When the `coverage: 'with'` and `'skip'` stub runs log their checklist split, no share line
  names `coverage`, and under `'only'` no share line prints.
  Red when: a checklist share goes to `coverage` or to a lens that did not dispatch.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `hook destinations self-test` · `workflow script syntax`

New arm: tools/hooks/agent-cap.test.sh · covers AC1 · every rendered harness under the workflows kit fed through the `scriptPath` arm and required admitted, staged by a scratch copy with a sixth `SPEC_LENSES` entry · none
New arm: tools/workflows/tier2-review.test.sh · covers AC2 AC3 AC4 · the coverage stage under `with`, `skip` and `only`, staged by appending `coverage` to `SPEC_LENSES` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of this build, id 28
  (HIGH, item H2), repairing TOOL-dIndexedDesign-16 S8 and its Files touched.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dIndexedDesign-39, TOOL-dIndexedDesign-44 and TOOL-dIndexedDesign-46, promoted by
  the round-1 spec audit of units 31 to 38; nothing else moved.

## 10. Reuse audit

The seams are the harness's own single-agent stages, `probe` (`tier2-review.template.js:1004`) and
`synth` (`:1721`), and its skipped-lens sentinel (`:1176-1178`), which S3 reuses for `only`.
`python tools/codebase-map/reuse_lookup.py "run one extra review agent outside the lens fan-out"`
ranked `run`, `run_git`, `run_arms` and `extract_run_facts`, none a workflow stage, so no seam fits
beyond the two calls named, each verified at base.

Recall terms used: `python tools/memory-recall/query.py "how does a review harness add a lens without breaking the agent-cap lens bound" --terms "agent-cap MAX_LENSES SPEC_LENSES lens bound fixed-verifiers coverage lens skippedLenses checklist shares"`
