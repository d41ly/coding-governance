# TOOL-aWeldedTribunal-2 — acceptance ledger

**Serves:** build TOOL-aWeldedTribunal-2

## What changed

One sweep in `tools/hooks/agent-cap.js`, placed after both scan passes and beside the reassignment
take-back sweep. `GROWS_RECEIVER` is `push|unshift|splice` — the methods that can increase an array's
length — and a match on a name already in `ok` deletes the bound and records a reason keyed by name.
Six arms in `tools/hooks/agent-cap.test.sh`, three denying and three admitting.

## Each criterion, answered

- **AC1** — `const batches = []`, grown with a plain-value `batches.push(f)`, fanned as
  `await boundedParallel(batches.map((f) => () => agent(f.claim)), MAX_VERIFIERS)`, exits **2**, and
  the refusal reads `` `batches` was GROWN by a mutation after its bounded assignment, which takes
  the bound back ``. That is this unit's own message, not the loop ban's.
  **Pre-state observed rather than assumed:** the identical script piped to
  `git show HEAD:tools/hooks/agent-cap.js` — the tree with unit 1 and without unit 2 — exits **0**.
  Round 2's blocker was exactly that rev-2's criterion was green on both sides; this one is not.
- **AC2** — the same script with the `push` removed exits **0**. An empty literal nobody grows is
  legal and stays legal.
- **AC2b** — `push` present but the `.map` fan on a separate line from the `agent()` call exits
  **0**. This is the legal shape, and it is the control that separates this unit's mechanism from an
  over-broad predicate.
- **AC3** — one arm per NEW verb: `unshift` exits **2** and `splice` exits **2**, both naming the
  mutation.
- **AC4** — every tracked harness still exits 0: `check-workflow-syntax.js`, `drift-audit-code.js`,
  `drift-audit-state.js`, `tier2-review.js`, `unattended-build.js`. Matches the recorded baseline.
- **AC5** — `bash tools/hooks/agent-cap.test.sh`: **181 passed, 0 failed, exit 0**. All 175 arms
  standing before this unit still pass.
- **AC6** — `GROWS_RECEIVER` and the marked-branch right-hand-side veto are SEPARATE constants, and
  the comment on the first states the measurement that decided it.

## Why the two vocabularies are not shared, in one line

`concat`, `flat` and `flatMap` return a new array and grow nothing. Applying the right-hand-side
list to a receiver took the bound back from `ALL_LENSES` on this tree — a shipped lens array, on the
strength of a `.concat` that changes nothing. A seventh arm pins that direction: a `.concat` beside a
legal bounded fan still exits 0.

## What this unit does NOT close, stated

Mutation through an alias (`const b = batches; b.push(…)`), and growth by index assignment past the
end or by writing `.length`. Both are named residuals in the spec's §3. The index form is excluded
deliberately: a regex over `name[<expr>] =` matches every ordinary element write and would deny
innocent files, which is the direction this whole build's pre-wiring rule exists to prevent.
