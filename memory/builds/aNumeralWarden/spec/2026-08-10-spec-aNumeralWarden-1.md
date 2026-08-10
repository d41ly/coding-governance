# TOOL-aNumeralWarden-1 — agent-cap enforces the verifier number, not just the helper shape

**Status:** SPECCED · rev-1 · 2026-08-10 · node a · Tier-2 · base 289daf72 · streams tooling

## 1. Goal

`tools/hooks/agent-cap.js` enforces that fan-out routes through the bounded helpers but never reads
the bound itself, so a shipped harness can raise its own verifier count from the caller and every
gate stays green. This unit makes the hook resolve the number and denies the two caller-settable
knobs that currently reach past the cap the charter calls BINDING.

## 2. Scope (IN)

- **S1** — `agent-cap.js` resolves the cap argument at every `boundedParallel(` / `boundedPipeline(`
  CALL SITE through the existing `boundedK` resolver, and denies when it exceeds `MAX_VERIFIERS` or
  cannot be resolved to an integer.
- **S2** — `agent-cap.js` applies the same resolution to a `cap = <K>` default parameter in a helper
  DEFINITION, so a helper defined wide and called bare is denied at the definition.
- **S3** — the `gov:fixed-verifiers` K may no longer resolve through an `|| <literal>` fallback. A K
  that is an identifier must be bound by a direct `const <name> = <int>` assignment.
- **S4** — `gov:bounded-fanout` gains a shape check. The marked line must slice a bare identifier by
  a K that resolves at or under `MAX_VERIFIERS`; a marked line of any other shape is denied.
- **S5** — `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js` drop both
  caller-settable knobs. `MAX_VERIFIERS` and `CAP` become bare integer literals, matching
  `tools/workflows/tier2-review.js:202`.
- **S6** — the stale comment at `drift-audit-code.js:19-21` and `drift-audit-state.js:17-19` is
  corrected or deleted. It claims `agent-cap.js` defaults to 6 in this repo; the file reads 5.
- **S7** — the false override claims at `README.md:50` and `WIRE-INTO-PROJECT.md:388` are removed.
  `AGENT_CAP` never overrode the cap; it only ever rewrote the deny message.
- **S8** — `tools/workflows/check-protocol-parity.test.sh:53` asserts the protocol document's NUMBER,
  not the digit-free phrase `verify-stage agents TOTAL`.
- **S9** — `tools/hooks/agent-cap.test.sh` gains a red and a green arm for each of S1 through S4, and
  stops pinning the deny substring `cap-5` at `:202-203`.
- **S10** — `KIT_AGENT_CAP_VERSION` and its `gov:kit agent-cap@<V>` marker move 1.1 to 1.2 together.

## 3. Non-goals (OUT)

- The enclosing-opener walk in `agent-cap.js:222-240`. Two nested wrappers or 59 lines of distance
  defeat it, which is a structural defect in a different mechanism and needs a statement-level walk
  rather than an opener count. Follow-up row `TOOL-aNumeralWarden-2`.
- Gating a pin RAISE against the base ref. That is the deeper ratchet fix and touches
  `tools/drift-audit/drift_report.py`, not this hook. Follow-up row `TOOL-aNumeralWarden-3`.
- Adding `bash tools/check-wiring.sh --check` to `tools/gate-legs.json`. Cheap and unrelated.
- Reconciling `MAX_LENSES` with `MAX_VERIFIERS`. Surfaced as a fork in §8 because a decision is owed
  before the numbers can diverge further, but no code moves for it in this unit.
- Any change to the ≤5 value itself. This unit makes the existing number enforceable and does not
  argue it.

## 4. Design

### Inventory

Every claim below was read against source at `289daf72`.

| Hole | Site | What passes today |
|---|---|---|
| Cap argument unread | `tools/hooks/agent-cap.js:38` | `CAP` reaches only the deny text at `:337` and `:354-363`; it decides nothing |
| Caller-settable total | `tools/workflows/drift-audit-code.js:51` · `drift-audit-state.js:51` | `a.maxVerifiers \|\| 5` — the hook binds the literal 5 at `:119-120`, the runtime uses the argument |
| Caller-settable concurrency | `drift-audit-code.js:22` · `drift-audit-state.js:20` | `(args && args.cap) \|\| 5`, same inference, same divergence |
| Marker exempts outright | `tools/hooks/agent-cap.js:66` | a `gov:bounded-fanout` line slicing 50 wide returns before any shape check |

The two entry points named in `memory/guides/REVIEW-PROTOCOL.md:32-38` both miss the second row. A
`Workflow({name:'drift-audit-code'})` run supplies no script to the hook at all, and the merge-bar
leg `tools/workflows/check-verifier-fanout.sh` reads the file, sees the `|| 5` fallback, and prints
`clean — 3 workflow script(s) obey the ≤5-verifier rule` at `:84`.

### The predicate change

`boundedK` already exists at `agent-cap.js:103-107` and already resolves an integer literal or an
identifier bound in the file to one. It is called once, at `:135`, for the `gov:fixed-verifiers` K.
S1 and S2 give it two more call sites.

```js
// S1 — at a call site: boundedParallel(thunks, K) / boundedPipeline(items, K, ...stages)
// S2 — at a definition: async function boundedParallel(thunks, cap = K)
// Deny when K is absent-and-the-default-is-wide, resolves above MAX_VERIFIERS, or is unresolvable.
```

S3 narrows the constant binder. `agent-cap.js:119-120` currently records the literal from any
`<expr> || <int>` right-hand side, which is the exact inference that lets `a.maxVerifiers || 5`
present as 5. The `||` form stays usable for ordinary constants but is no longer accepted as the K
of a `gov:fixed-verifiers` line, so the marker's claim keeps meaning what it says.

S4 gives `gov:bounded-fanout` the treatment its sibling already has. The marker becomes a claim whose
shape is checked rather than a blanket exemption, which is the asymmetry the review named as the
single clearest lesson in the hook.

### Migration

An adopter who sets `AGENT_CAP` today gets a rewritten deny message and no behaviour change, so
nothing they rely on is load-bearing. The fork in §8 decides whether a set `AGENT_CAP` becomes a hard
deny or a stderr notice. An adopter running a harness with `args.maxVerifiers` set loses that knob;
no shipped caller passes it, and `tier2-review.js` never had it.

### Rollout

One commit, gated by the full bar. The hook is deployed verbatim into adopting repos, so `S10`'s
version bump is what tells a deployer the contract moved.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/hooks/agent-cap.js` | S1 S2 S3 S4 S10 — the predicate and the version pair |
| `tools/hooks/agent-cap.test.sh` | S9 — eight new arms, one pin removed |
| `tools/workflows/drift-audit-code.js` | S5 S6 |
| `tools/workflows/drift-audit-state.js` | S5 S6 |
| `tools/workflows/check-protocol-parity.test.sh` | S8 |
| `README.md` | S7 |
| `WIRE-INTO-PROJECT.md` | S7 |

### Alternatives rejected

- **Make `AGENT_CAP` the real enforced bound.** Rejected. It converts the cap into the DEFEATABLE
  class the review flagged across 32 other caps, and an environment variable leaves no diff.
- **Count agents at runtime instead of statically.** Rejected. `REVIEW-PROTOCOL.md:42` records that a
  workflow script runs in a sidechain with no hooks, so nothing can observe the spawn.
- **Ban the `||` binding form everywhere.** Rejected as too wide. It is a legitimate default for
  ordinary constants; only its use as a verifier K is the defect.

## 5. Production-readiness checklist

- security — the hook is a guard; every new branch fails closed, matching `agent-cap.js:242-245`.
- perf / scale — N/A. The scan is per-line over one tool-call payload.
- a11y — N/A. No user interface.
- i18n — N/A. Operator-facing English strings only.
- error / empty / loading states — an unresolvable K denies rather than passing; the empty-script
  path at `:325` is unchanged.
- observability — the deny message names the line, the resolved value, and the ceiling.
- risks — a false deny blocks a legitimate review. Mitigated by S9's green arms over the three
  shipped harnesses.
- testing + left-shift gates — `agent-cap.test.sh` plus `check-verifier-fanout.sh`, both already legs.
- migration / rollback — revert is one commit; adopters re-pull on kit update.
- user docs — S7 corrects the two false claims; `memory/guides/REVIEW-PROTOCOL.md:72-74` needs its
  "the hook does NOT parse the helper's numeric argument" paragraph rewritten, since S1 makes it false.

## 6. Acceptance criteria

- **AC1** — When a script calls `boundedParallel(thunks, 99)`, the hook exits 2 and the message names
  the line number and the resolved value 99.
- **AC2** — When a script calls `boundedParallel(thunks, 5)`, the hook exits 0.
- **AC3** — When a helper is defined `async function boundedParallel(t, cap = 99)`, the hook exits 2.
- **AC4** — When a `gov:fixed-verifiers` line uses a K bound by `const MAX_VERIFIERS = a.maxVerifiers
  || 5`, the hook exits 2 naming the fallback form.
- **AC5** — When a `gov:bounded-fanout` line slices 50 wide, the hook exits 2.
- **AC6** — When the three shipped harnesses in `tools/workflows/` are fed to the hook unchanged
  after S5, each exits 0.
- **AC7** — When `memory/guides/REVIEW-PROTOCOL.md:7` is edited to read `≤50`,
  `bash tools/workflows/check-protocol-parity.test.sh` exits non-zero.
- **AC8** — When `bash tools/hooks/agent-cap.test.sh` runs, it exits 0 and reports arms for AC1
  through AC5.
- **AC9** — When `bash tools/check-kit-versions.sh` runs after S10, it exits 0.
- **AC10** — When `grep -rn 'AGENT_CAP' README.md WIRE-INTO-PROJECT.md` runs, no line claims the cap
  is overridable.
- **AC11** — When `bash tools/run-gates.sh` runs, all 40 legs pass.

## 7. Gates

- `tools/hooks/agent-cap.test.sh` — the kit self-test, extended by S9.
- `tools/workflows/check-verifier-fanout.sh` — the committed-harness leg, which delegates to the hook.
- `tools/workflows/check-protocol-parity.test.sh` — extended by S8.
- `tools/check-kit-versions.sh` — the constant and marker pair from S10.
- `tools/memory-tree/check-memory-hygiene.sh` — this spec is corpus and check 12 binds it.
- `bash tools/run-gates.sh` — the full bar at the push boundary.

No new gate leg is added. Every assertion lands in a leg that already runs.

## 8. Open questions

### F1 — what happens when `AGENT_CAP` is set after this unit

`AGENT_CAP` becomes meaningless once the ceiling is the file constant. Options: deny with an
explanatory message so the misconfiguration is discoverable, or ignore it with a one-line stderr
notice. **Recommendation:** deny. A silently-ignored knob that used to appear to work is how the
current false doc claim survived two releases.

### F2 — `MAX_LENSES` is 6 while `MAX_VERIFIERS` is 5

`agent-cap.js:97` admits a 6-element array literal as a bounded receiver, so a six-lens verify stage
passes a rule the charter states at 5. Options: lower `MAX_LENSES` to 5, keep 6 and document that the
lens allowance is a find-stage affordance, or gate the two by stage. **Recommendation:** keep 6 and
document it, because `REVIEW-PROTOCOL.md:94` explicitly prescribes adding lenses rather than skeptics
for a large surface. A decision is owed either way.

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, grounded on the hard-caps audit at base `289daf72`.

## 10. Reuse audit

The seam this unit wires through is `boundedK` at `tools/hooks/agent-cap.js:103-107`, already written
and already called once at `:135` for the `gov:fixed-verifiers` K. S1 through S3 add call sites
rather than a second resolver, which is what keeps one rule with one implementation.

`python tools/codebase-map/reuse_lookup.py "resolve an integer literal or file-bound constant to
check a cap"` did NOT surface it. The map's symbol corpus indexes Python functions and exported
JavaScript names, and `boundedK` is a non-exported function in a `.js` file, so no seam in the kit's
own hook is visible to the kit's own lookup. The seam was found by reading the file. That gap is
recorded as follow-up row `TOOL-aNumeralWarden-4` rather than worked around here.
