# TOOL-dGroundRules-18 — a writer split bounded by the agent limit: rule 2 judges `gov:fixed-writers` against `runtime.agents-in-flight` and verifiers against `MAX_VERIFIERS`

**Status:** DEFERRED · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-18-deviation-55.md](../build/2026-10-23-build-TOOL-dGroundRules-18-deviation-55.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-18-deviation-6.md](../build/2026-10-23-build-TOOL-dGroundRules-18-deviation-6.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-18-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-18-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-16 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-19 TOOL-dGroundRules-15 TOOL-dGroundRules-17 TOOL-dGroundRules-20 TOOL-dGroundRules-21 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md`)
exited BOUNDED with finding **id 13 at HIGH**, item **H3**, which no other id shares. This unit is its
promotion. It repairs `TOOL-dGroundRules-10` and builds at order 6, one step after that unit.

`TOOL-dGroundRules-10` §4 moves `boundedK`'s comparand from the clamp to `MAX_VERIFIERS`, 5, while
its §8 F3 keeps `const SPEC_WRITERS = {{FANOUT_CAP}}`, which renders the limit, 6 by default. The
spec-writer split in `tools/workflows/unattended-build.template.js:955` carries
`// gov:fixed-verifiers`, so rule 2 judges K = 6 against 5 and refuses. That unit's AC13 is red as
designed, and live, the hook refuses every `unattended-build` Workflow call. This unit gives a writer
split its own marker, `gov:fixed-writers`, whose K rule 2 judges against the landed agent limit,
while a verifier split stays bounded by `MAX_VERIFIERS`.

## 2. Scope (IN)

- **S1** — The marker. `tools/hooks/agent-cap.js` declares `WRITER_MARK = 'gov:fixed-writers'`
  beside `FIXED_MARK`. A receiver assigned on a line carrying it qualifies when the line spells
  `chunk(x, Math.ceil(x.length / K))` or `splitInto(x, K)` and K resolves, as a literal or an
  integer const of the file, to at most the writer bound. Every other receiver rule is unchanged,
  and a `gov:fixed-verifiers` split's K is still judged against `MAX_VERIFIERS`. Observed by AC1,
  AC2, AC3.
- **S2** — The writer bound. The limit `readPolicy("runtime.agents-in-flight", { repo })` answers,
  read once per hook process and only when the script carries the writer marker, `repo` being the
  payload's `cwd` or, under `--only=scripts`, the working directory. With no `policy-mirror.js` in
  the `policy` kit beside the hooks kit, the bound is `MAX_VERIFIERS`, the stricter answer. A
  `PolicyRefusal` denies, naming its line. Observed by AC2, AC4.
- **S3** — The template. `tools/workflows/unattended-build.template.js:955` carries
  `// gov:fixed-writers` in place of `// gov:fixed-verifiers`, the comment above it says why, and
  `tools/workflows/unattended-build.js` is re-rendered. Observed by AC1.
- **S4** — The case `limit-hook-writer-split` in `CASES` of `tools/policy/check_policy.py`, and its
  guard: the `policy fixtures` row in `tools/gate-legs.json` gains
  `{prefix}/workflows/unattended-build.template.js`, which the case renders. Observed by AC1, AC2,
  AC3.
- **S5** — The deny message for a writer split names `gov:fixed-writers`, the K it read and the
  limit, and says the limit is `runtime.agents-in-flight`. Observed by AC2.

## 3. Non-goals (OUT)

- Changing `MAX_VERIFIERS`, the verifier marker, or what the verify stage may spawn: the review
  protocol's verify total is the hook's, as `TOOL-dGroundRules-10` §8 F2 settled.
- Rendering `SPEC_WRITERS` as the smaller of the limit and five, which needs the verify total
  outside the hook (`TOOL-dGroundRules-10` §8 F3) (§8 F1 here).
- Counting agents in flight: the harness's settings bound concurrency, and the ledger is
  dWellOiledMachine's.

### Edges

- **consumes-from** `TOOL-dGroundRules-10` — rule 2 with `boundedK` against `MAX_VERIFIERS`, rule 7's `readPolicy` read beside the hooks kit, the `{{FANOUT_CAP}}` render through the policy reader, and the `limit-` case fixture
- **hands-off** `TOOL-dGroundRules-25` — the writer receiver in the review protocol, the hooks README's bounds, the map card and the workflows render's version floor (findings 27, 8, 14, 35, 44)
- **hands-off** `TOOL-dGroundRules-30` — `WRITER_MARK`, the writer bound and the template's `gov:fixed-writers` split, which that unit's render asks the installed hook to admit before it writes them (finding 18)

## 4. Design

### Evidence

- `tools/workflows/unattended-build.template.js:942` is `const SPEC_WRITERS = {{FANOUT_CAP}}`, and
  `:955` is `const specGroups = chunk(slices, Math.ceil(slices.length / SPEC_WRITERS)) //
  gov:fixed-verifiers`.
- `tools/hooks/agent-cap.js:491-492` declare `FIXED_MARK` and `MAX_VERIFIERS = 5`;
  `boundedK` (`:551-556`) is the one comparison, and `boundedBranch` (`:628-634`) admits a marked
  split whose K it resolves.
- `TOOL-dGroundRules-10` §4 "The hook after this unit": "`boundedK` compares against
  `MAX_VERIFIERS`"; its F3 keeps the token on `SPEC_WRITERS`; its AC13 pipes each of the four
  renders through `node tools/hooks/agent-cap.js --only=scripts`, expecting exit 0.
- The catalogue default of `runtime.agents-in-flight` is 6 (`TOOL-dGroundRules-1` AC2).
- Rule 7 already locates `policy-mirror.js` in the `policy` kit beside the hooks kit and reads the
  limit with `readPolicy` (`TOOL-dGroundRules-10` S5).

### Rule 2 after this unit

```js
const WRITER_MARK = 'gov:fixed-writers'
// boundedK(tok, consts, bound): bound is MAX_VERIFIERS for FIXED_MARK and readWriterBound() for WRITER_MARK
function readWriterBound(repo) { /* readPolicy once; MAX_VERIFIERS when the helper is absent */ }
```

`boundedK` takes its bound as an argument; its callers pass `MAX_VERIFIERS` everywhere they pass
today's comparand, and the receiver walk passes `readWriterBound(repo)` for a line carrying
`WRITER_MARK`. A line carrying both markers is denied as ambiguous.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `WRITER_MARK` | const, the marker `gov:fixed-writers` | `tools/hooks/agent-cap.js` |
| `readWriterBound` | js.function | `tools/hooks/agent-cap.js` |
| `limit-hook-writer-split` | `CASES` entry | `tools/policy/check_policy.py` |

`readWriterBound` leads with `read`: `lexicon.py --suggest` answered OK for it under `js.function`
on 2026-10-23.

### Files touched (estimate)

- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`
- `tools/policy/check_policy.py`
- `tools/gate-legs.json`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Render `Math.min(limit, MAX_VERIFIERS)`.** §8 F1.
- **Drop the marker and spawn the writers sequentially under `gov:sequential-agents`.** The spec
  stage would run one writer at a time, slowing every build to fix a rule that misjudged a bound.

## 5. Production-readiness checklist

- security — the verify total stays bounded at 5; a writer split is bounded by the landed limit,
  never by a value the script states, and a missing helper falls to the stricter 5.
- perf / scale — one `readPolicy` per hook process, only for a script carrying the writer marker.
- error / empty / loading states — a `PolicyRefusal` denies naming the reader's line; a line with
  both markers denies.
- observability — the deny names the marker, the K and the bound with its key.
- risks — an author marks a verifier split `gov:fixed-writers` to reach the larger bound. The
  marker is a claim the shape check bounds, as `gov:fixed-verifiers` is today; the review protocol
  names verifier receivers, and AC3 pins the verifier bound.
- testing — `limit-hook-writer-split` under `--fixture`, the hook's own suite arm, with AC1 to AC4.
- migration — `tools/workflows/unattended-build.js` re-rendered; no adopter script carries the new
  marker until its renders update with the workflows kit.
- user docs — `tools/hooks/README.md`'s rule 2 paragraph names both markers and their bounds.

## 6. Acceptance criteria

Every command runs from the repository root. The case spells the policy kit's files by bare name,
`check_policy.py`, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `python check_policy.py --fixture limit-hook-writer-split` renders
  `tools/workflows/unattended-build.template.js` at a landed limit of 6 and pipes it through
  `node tools/hooks/agent-cap.js --only=scripts`, it exits 0.
  Red when: the split still carries `gov:fixed-verifiers` and rule 2 refuses K = 6 against 5.
- **AC2** — When the same case renders it at 6 under a landed limit of 4, the hook exits 2 naming
  `gov:fixed-writers`, `6` and `runtime.agents-in-flight`.
  Red when: the writer bound is not read, and a split above the landed limit is admitted.
- **AC3** — When the case pipes a script whose `gov:fixed-verifiers` split has K = 6 under a landed
  limit of 6, the hook exits 2 naming `MAX_VERIFIERS`.
  Red when: the verifier bound moved to the limit along with the writer bound.
- **AC4** — When the case removes `policy-mirror.js` from the fixture and pipes the render at 6, the
  hook exits 2 naming `MAX_VERIFIERS` as the bound used.
  Red when: an absent helper admits a writer split of any width.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out` · `workflow script syntax` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kit version markers` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/policy/check_policy.py (`--fixture limit-hook-writer-split`) · covers AC1 AC2 AC3 AC4 · the split's marker staged back to `gov:fixed-verifiers`, then `readWriterBound` staged to answer `MAX_VERIFIERS` always · none
New arm: tools/hooks/agent-cap.test.sh · covers AC2 AC3 · a writer split above a stub limit and a verifier split at 6, each refused, staged in the suite's own scratch copy by a stub `policy-mirror.js` answering the limit · that suite's assertion count, raised by the arms added

## 8. Open questions

- **F1 — How is the spec-writer split bounded once rule 2 compares to `MAX_VERIFIERS`?** (a) A
  writer marker whose K rule 2 judges against the landed limit, the verifier marker unchanged.
  (b) Render `SPEC_WRITERS` as `Math.min(limit, MAX_VERIFIERS)`. (c) Drop the marker from the split
  and bound it another way. (b) needs the verify total outside the hook, which
  `TOOL-dGroundRules-10` §8 F3 rejected under `[one-fact]` (veto 1 against that ruling). (c)'s only
  other admitted receiver for a loop is `gov:sequential-agents`, which serialises the spec stage and
  fails no criterion but meets fewer than (a), which keeps the stage's width at the limit the owner
  sets. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  grants: PLAY-dClosedLoop-3 the writer marker on rule 2, part of the agent limit's surface
  `cl-dClosedLoop-0016` names · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 13 (HIGH, item H3) of the round-1 spec
  audit, from the review's option (a) and `tools/hooks/agent-cap.js` and the template read at base
  `3708a705`.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-25`, the reciprocal of each
  promotion of the round-1 spec audit of units 13 to 21 that repairs this unit; no scope moved.
- rev-3 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-30 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 22 to 25 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 10. Reuse audit

The seam extended is rule 2's receiver walk in `tools/hooks/agent-cap.js`: `boundedK` and
`boundedBranch` (`:551-634`), which already bind a marked split's K, gain a bound argument instead of
a second walk; the limit is read through `readPolicy`, the helper rule 7 already calls.
`python tools/codebase-map/reuse_lookup.py "judge a bounded split of agent spawns against a writer
bound"` ranked `write`, `write_text`, `boundedParallel` and `write_record`; `boundedParallel` bounds
concurrency, not a split's agent count, so no other seam fits. The recall probe returned
`TOOL-aWireWarden-1`'s ratification of one cap number and `memory/gotchas/concurrency-is-not-a-budget.md`,
which is why the verify total stays a total here; both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how does the agent-cap hook bound a fixed
split of agents" --terms "agent-cap fixed-verifiers bounded split MAX_VERIFIERS SPEC_WRITERS
FANOUT_CAP rule 2 boundedK"`
