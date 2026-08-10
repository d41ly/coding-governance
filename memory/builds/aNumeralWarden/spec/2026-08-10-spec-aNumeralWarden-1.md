# TOOL-aNumeralWarden-1 — agent-cap enforces the verifier number, and reaches the modality it was blind to

**Status:** SPECCED · rev-4 · 2026-08-10 · node a · Tier-2 · base 289daf72 · streams tooling · review wf_154599e2

## 1. Goal

`tools/hooks/agent-cap.js` enforces that fan-out routes through the bounded helpers but never reads
the bound itself, so a shipped harness can raise its own verifier count from the caller and every
gate stays green. This unit makes the hook resolve the number wherever a bound is written, so the
cap the charter calls BINDING is enforced by a predicate rather than by convention.

The hook also reaches only one of the two ways agents get spawned. It is wired on the `Workflow`
tool, so it inspects a workflow SCRIPT; a session that fans out with direct `Agent` tool calls meets
no rule at all. S14 and S15 close that, so this unit has two halves: the hook reads the bound it
enforces, and it sees the modality it was blind to.

## 2. Scope (IN)

- **S1** — `agent-cap.js` resolves the cap argument at every `boundedParallel(` / `boundedPipeline(`
  CALL SITE and denies when it exceeds `MAX_VERIFIERS`. The hook is a per-line scanner with no
  argument walk today, so S1 specifies the EXTRACTION as well as the verdict. Join forward from the
  opening paren until the parens balance, using the bracket walk at `agent-cap.js:161-169` as the
  precedent, split the joined text on TOP-LEVEL commas, and resolve argument 2 through `boundedK`.
  An argument that is a member expression, a spread, or a call result is unresolvable and denies.
- **S2** — when argument 2 is ABSENT, the named helper's own `cap = <K>` DEFAULT governs. S2
  resolves that default the same way and denies a wide or unresolvable one. A bare
  `boundedParallel(thunks)` against a bounded default is allowed.
- **S3** — `boundedK` may no longer resolve an identifier bound by an `<expr> || <int>` right-hand
  side, for EVERY consumer: the `gov:fixed-verifiers` K, the S1 call-site argument and the S2
  default. The bare-reassignment sweep at `agent-cap.js:195-200` is mirrored onto the `consts` map,
  so `let K = 5` followed by `K = 500` no longer resolves to 5.
- **S4** — `gov:bounded-fanout` gains a shape check. The marked line must slice a bare identifier by
  a width token that is EITHER the enclosing helper's own `cap` parameter, which S2 has already
  bounded at the definition, OR a K that `boundedK` resolves at or under `MAX_VERIFIERS`. The
  parameter case is what keeps the three shipped harnesses green; without it S4 denies all of them.
- **S5** — `tools/workflows/drift-audit-code.js` and `tools/workflows/drift-audit-state.js` drop both
  caller-settable knobs. `MAX_VERIFIERS` and `CAP` become bare integer literals, matching
  `tools/workflows/tier2-review.js:202`, and the `maxVerifiers:` and `cap:` lines are struck from the
  `args` documentation blocks at `drift-audit-code.js:45` and `drift-audit-state.js:43`.
- **S6** — the stale comment at `drift-audit-code.js:19-21` and `drift-audit-state.js:17-19` is
  deleted. It claims `agent-cap.js` defaults to 6 in this repo; `agent-cap.js:38` reads 5.
- **S7** — the false `AGENT_CAP` override claim is removed from all three sites a repo-wide grep
  finds: `README.md:50`, `WIRE-INTO-PROJECT.md:388`, and the hook's own header at
  `tools/hooks/agent-cap.js:14-21`. The rationale comment at `tools/hooks/agent-cap.test.sh:198-199`
  is folded into S9, since it cites that header as its reason for asserting nothing about the number.
- **S8** — `tools/workflows/check-protocol-parity.test.sh:53` asserts the protocol document's NUMBER,
  not the digit-free phrase `verify-stage agents TOTAL`.
- **S9** — `tools/hooks/agent-cap.test.sh` gains a red and a green arm for each new branch, each
  asserting the SPECIFIC message its branch emits. It stops pinning the deny substring `cap-5` at
  `:202-203`.
- **S10** — `KIT_AGENT_CAP_VERSION` and its `gov:kit agent-cap@<V>` marker move 1.1 to 1.2, and
  `tools/check-kit-versions.sh` gains the constant-versus-marker reconciliation it already runs for
  four other kits at `:30-34`, `:40-44`, `:50-54` and `:64-70`. Today it presence-checks the constant
  only, so a half-bumped pair passes.
- **S11** — `memory/guides/REVIEW-PROTOCOL.md:72-74` is rewritten. It currently states that the hook
  does not parse the numeric argument, which S1 falsifies, and the predicate at `:48-50` becomes
  imprecise under S3. `tools/workflows/REVIEW-PROTOCOL.template.md` is re-rendered from it with
  `bash tools/workflows/check-protocol-parity.test.sh --render`.
- **S12** — the drift-audit kit's `meta.version` and `gov:kit drift-audit@` markers move in both
  harnesses, because S5 narrows the `args` contract those files ship to adopters, with a migration
  line in `tools/drift-audit/README.md`.
- **S13** — the wired copy `.claude/hooks/agent-cap.js` is re-copied from the kit. It is the file
  `.claude/settings.json:9` actually executes, and `agent-cap.test.sh:215-227` gates the two
  byte-identical.
- **S14** — the matcher widening, which is self-contained and provably a no-op. The `PreToolUse`
  matcher becomes the exact-string LIST `"Workflow|Agent"` in ONE group, which the hook documentation
  evaluates as a list of exact strings separated by `|` — so there is no second fragment, no second
  marker, and no `settings-merge.py` dedup question. The widening changes no behaviour by itself,
  because `agent-cap.js:305` exits 0 on any `tool_name` that is not `Workflow`; the no-op is MEASURED
  by feeding every existing arm of `agent-cap.test.sh` through the hook before and after and
  requiring byte-identical output. This half also fixes `check-wiring.sh`'s `wired()` join, which
  greps the whole of `.claude/settings.json` for the literal `agent-cap.js` and so cannot tell a
  correctly-widened matcher from a stale `Workflow`-only one: it must assert the matcher VALUE, not
  that the file contains the string. Ships alone, in its own commit, ahead of S15.
- **S15** — arity enforcement for direct `Agent` spawns, as an ATOMIC COUNT rather than a modality
  refusal. Per spawn the hook creates a token file with `O_EXCL` under a `session_id`-keyed directory
  in the git common dir, named for the payload's `tool_use_id`, then counts the tokens carrying the
  current `prompt_id` and denies past the cap. Create-and-count with `O_EXCL` is atomic where
  read-then-decide is not: measured on node a, a four-call burst overlapped its hook processes and
  two of four read the same count, so a read-then-decide gate loses updates nondeterministically.
  That measurement refutes a read-then-decide COUNTER; it does not refute counting, and `tool_use_id`
  is precisely the key that makes the count exact. Tokens are keyed per prompt, so a new user prompt
  resets the budget with no cleanup; a TTL sweep drops directories older than the window, and a token
  is removed only by the process that wrote it, per the recorded scar where an unconditional unlink
  let one builder release another's protection.
- **S15 is a deliberate REVERSAL and is argued as one.** This spec's own rejected alternative says
  runtime counting is impossible, and that reasoning holds for the case it was written about: a
  workflow script runs in a sidechain with no hooks, so nothing observes those spawns. The main-loop
  `Agent` case differs in kind — a hook does fire, and the payload carries `session_id`, `prompt_id`
  and `tool_use_id`, all measured present. The rejected alternative is rewritten to name the case it
  rejects instead of reading as a blanket ban, and `memory/guides/REVIEW-PROTOCOL.md` takes the same
  distinction under S11, since it currently states the blanket form.
- **S15 counts every direct `Agent` spawn in a turn, not only review verifiers.** Keying on "is this
  a verify agent" would need a session-to-build binding that no payload field provides. The charter's
  concurrency rule already binds every fan-out, so the cap applies uniformly and needs no binding, no
  run-state file and no phase vocabulary. That is what dissolves the dependency the fold created:
  nothing in this unit reads `TOOL-aUnmannedHelm-1`'s run-state file, so neither build blocks the
  other.

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

Every claim below was read against source at `289daf72` and re-verified at rev-2.

| Hole | Site | What passes today |
|---|---|---|
| Cap argument unread | `tools/hooks/agent-cap.js:38` | `CAP` reaches only the deny text at `:337` and `:354-363`; it decides nothing |
| Caller-settable total | `tools/workflows/drift-audit-code.js:51` · `drift-audit-state.js:51` | `a.maxVerifiers \|\| 5` — the hook binds the literal 5 at `:119-120`, the runtime uses the argument |
| Caller-settable concurrency | `drift-audit-code.js:22` · `drift-audit-state.js:20` | `(args && args.cap) \|\| 5`, same inference, same divergence |
| Marker exempts outright | `tools/hooks/agent-cap.js:66` | a `gov:bounded-fanout` line slicing 50 wide returns before any shape check |
| No argument walk | `tools/hooks/agent-cap.js:111-112` | the scanner is per-line; every shipped call site spans lines |
| Reassignment survives | `tools/hooks/agent-cap.js:195-200` | the sweep deletes from `ok`, never from `consts` |

The two entry points named in `memory/guides/REVIEW-PROTOCOL.md:32-38` both miss the second row. A
`Workflow({name:'drift-audit-code'})` run supplies no script to the hook at all, and the merge-bar
leg `tools/workflows/check-verifier-fanout.sh` reads the file, sees the `|| 5` fallback, and prints
`clean — 3 workflow script(s) obey the ≤5-verifier rule` at `:84`.

### The predicate change

`boundedK` already exists at `agent-cap.js:103-107` and already resolves an integer literal or an
identifier bound in the file to one. It is called once, at `:135`, for the `gov:fixed-verifiers` K.
S1 and S2 give it two more call sites; S3 narrows what it is willing to resolve for all three.

```js
// S1 — call site:  boundedParallel(thunks, K) / boundedPipeline(items, K, ...stages)
// S2 — definition: async function boundedParallel(thunks, cap = K)
// S3 — K is an integer literal, or an identifier bound by a DIRECT `const <name> = <int>` and never
//      reassigned. An `<expr> || <int>` fallback no longer resolves, for any consumer.
```

S3 is deliberately narrower than the alternative rejected below: the `||` form stays legal JavaScript
and stays usable for constants the hook never reads, and only its use as a RESOLVED BOUND is refused.
That is what makes the marker's claim mean what it says, and it is why rev-1's version — which
narrowed the binder for the `gov:fixed-verifiers` K alone — left the concurrency knob resolving to 5
on the S1 path while S5 removed it only by hand in two files.

S4 gives `gov:bounded-fanout` the treatment its sibling already has. The marker becomes a claim whose
shape is checked rather than a blanket exemption, which is the asymmetry the audit named as the
clearest lesson in the hook. The canonical shipped line is
`out.push(...(await parallel(thunks.slice(i, i + cap)))) // gov:bounded-fanout`, whose width token is
the helper's own `cap` PARAMETER; S4 admits that token explicitly, because S2 has already bounded the
default it carries.

### Migration

An adopter who sets `AGENT_CAP` today gets a rewritten deny message and no behaviour change, so
nothing they rely on is load-bearing. The fork in §8 decides whether a set `AGENT_CAP` becomes a hard
deny or a stderr notice. An adopter running a harness with `args.maxVerifiers` or `args.cap` loses
those knobs, which is why S12 moves the drift-audit kit version: `drift-audit-code.js:19-21` tells
adopters the cap varies by adopter, so the contract change must be visible to version detection.

### Rollout

THREE commits, each gated by the full bar, in this order.

1. S1 through S13 — the bound-reading predicate, as specced at rev-2.
2. S14 alone — the matcher widening plus the `check-wiring.sh` join fix. Provably a no-op on
   behaviour, so it lands and is observed before any new predicate exists to confuse the observation.
3. S15 — the atomic count, the only commit that changes what a session is allowed to do.

Reverting commit 3 leaves the widened matcher in place, which is a safe standalone state precisely
because `agent-cap.js:305` exits 0 on a non-`Workflow` tool name. The hook is deployed verbatim into
adopting repos, so S10's version bump tells a deployer the contract moved, and S13's re-copy is what
makes any of it take effect in THIS repo — `.claude/settings.json:9` executes the `.claude/` copy,
not the kit copy, and that re-copy does NOT cover `.claude/settings.json` itself.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/hooks/agent-cap.js` | S1 S2 S3 S4 S7 S10 — the predicate, the header, the version pair |
| `.claude/hooks/agent-cap.js` | S13 — the wired copy, kept byte-identical |
| `tools/hooks/agent-cap.test.sh` | S9 — new arms, the `cap-5` pin removed, the `:198-199` rationale folded |
| `tools/workflows/drift-audit-code.js` | S5 S6 S12 |
| `tools/workflows/drift-audit-state.js` | S5 S6 S12 |
| `tools/workflows/check-protocol-parity.test.sh` | S8 |
| `tools/check-kit-versions.sh` | S10 — the agent-cap constant/marker reconciliation |
| `memory/guides/REVIEW-PROTOCOL.md` | S11 |
| `tools/workflows/REVIEW-PROTOCOL.template.md` | S11 — re-rendered, never hand-edited |
| `tools/drift-audit/README.md` | S12 — the migration line |
| `README.md` | S7 |
| `WIRE-INTO-PROJECT.md` | S7 S14 — `:376-393` publishes the Workflow-only matcher block verbatim |
| `.claude/settings.json` | S14 — the widened matcher; the wiring that actually executes |
| `tools/settings-merge.py` | S14 S15 — the fragment's matcher, its docstring block, the selftest arms that pin it, and its own version pair |
| `tools/check-wiring.sh` | S14 — `wired()` asserts the matcher VALUE, not a file-wide grep |
| `tools/check-wiring.test.sh` | S14 — the arm for a stale Workflow-only matcher |

### Alternatives rejected

- **Make `AGENT_CAP` the real enforced bound.** Rejected. It converts the cap into the DEFEATABLE
  class the audit flagged across 32 other caps, and an environment variable leaves no diff.
- **Count agents spawned INSIDE a workflow script.** Still rejected, and this is the case the
  original rejection was written about: a workflow script runs in a sidechain with no hooks, so
  nothing observes those spawns. S15 does not attempt it; the `Workflow` path stays static.
- **A modality refusal for direct `Agent` spawns** — deny the spawn while a run-state file declares a
  verify phase. Rejected at rev-4. It expresses a KIND, not a cardinality, so it cannot enforce a
  number; it fires only under the unattended driver, leaving interactive sessions unguarded, which is
  the modality that produced the incident; and it needs a session-to-build binding no payload field
  provides.
- **Ban the `||` binding form everywhere in the file.** Rejected as too wide. S3 refuses it only
  where a BOUND is being resolved, which covers every path that matters without touching constants
  the hook never reads.

## 5. Production-readiness checklist

- security — the STATIC rules are a guard and every new branch of them fails closed, matching
  `agent-cap.js:242-245`. S15's count is different and the split is stated rather than blurred: a
  spawn whose token cannot be created is DENIED, but a session whose token directory cannot be
  resolved at all fails OPEN and silently, because a hook that denies every spawn on a filesystem
  hiccup is worse than the burst it prevents. Both directions carry an arm.
- perf / scale — the forward paren join is bounded by the balance point, so the scan stays linear.
- a11y — N/A. No user interface.
- i18n — N/A. Operator-facing English strings only.
- error / empty / loading states — an unresolvable K denies rather than passing; the empty-script
  path at `:325` is unchanged.
- observability — every new deny names its own branch, its line, and the resolved value, so an arm
  can attribute the deny rather than reading a shared exit code.
- risks — a false deny blocks a legitimate review. The specific hazard for the static half is S4
  against the three shipped harnesses, which is why S4 admits the `cap` parameter explicitly and AC9
  regresses all three. For S15 the hazard is a legitimate wide fan-out that is not a review at all,
  since the count does not distinguish verifiers from any other agent; the residual is accepted
  because the charter's concurrency rule already binds every fan-out to the same number. Second
  residual, written down rather than implied: an agent spawned INSIDE a workflow sidechain is still
  uncounted, and always will be.
- testing + left-shift gates — `agent-cap.test.sh` plus `check-verifier-fanout.sh`, both already legs.
- migration / rollback — three commits per the Rollout order, each independently revertible.
  Reverting S15 leaves the widened matcher, which is inert. Adopters re-pull on kit update, signalled
  by S10, S12 and the settings-merge version pair S14 moves.
- user docs — S7 corrects the three override claims and S11 corrects the BINDING protocol document.

## 6. Acceptance criteria

- **AC1** — When a script calls `boundedParallel(thunks, 99)`, the hook exits 2 with a message naming
  the CALL SITE and the resolved value 99.
- **AC2** — When a script calls `boundedParallel(thunks, 5)`, the hook exits 0.
- **AC3** — When the same call is written across lines, with `thunks,` and `500` on their own lines,
  the hook exits 2 naming the call site and 500.
- **AC4** — When a script calls `boundedParallel(thunks)` with no cap against a helper whose default
  is 5, the hook exits 0.
- **AC5** — When a helper is defined `async function boundedParallel(t, cap = 99)`, the hook exits 2
  with a message naming the DEFAULT PARAMETER and the resolved value 99.
- **AC6** — When a script binds `const CAP = (args && args.cap) || 5` and calls
  `boundedParallel(thunks, CAP)`, the hook exits 2 naming the `||` fallback form.
- **AC7** — When a script binds `let K = 5` and later assigns `K = 500`, a `gov:fixed-verifiers` line
  keyed on `K` exits 2.
- **AC8** — When a `gov:bounded-fanout` line slices 50 wide, the hook exits 2 with a message naming
  the marked line and the resolved width 50.
- **AC9** — When each of the three harnesses in `tools/workflows/` is fed to the hook unchanged after
  S5, each exits 0, and `bash tools/workflows/check-verifier-fanout.sh` exits 0.
- **AC10** — When `grep -rn 'maxVerifiers\|args.cap\|defaults to 6' tools/workflows/` runs, it
  returns nothing.
- **AC11** — When `grep -rn 'AGENT_CAP' README.md WIRE-INTO-PROJECT.md tools/hooks/agent-cap.js`
  runs, no line claims the cap is overridable.
- **AC12** — When `memory/guides/REVIEW-PROTOCOL.md:7` is edited to `≤50` and the template is
  re-rendered so byte parity is restored, `bash tools/workflows/check-protocol-parity.test.sh` still
  exits non-zero, naming the missing hard-cap NUMBER. Both files are restored with `git checkout --`
  afterwards. The mirror arm, both copies at `≤5`, exits 0.
- **AC13** — When `bash tools/hooks/agent-cap.test.sh` runs, it exits 0 and its output names one arm
  per new branch.
- **AC14** — When only one of the two agent-cap version literals is bumped,
  `bash tools/check-kit-versions.sh` exits non-zero.
- **AC15** — When `grep -F "does NOT parse the helper's numeric argument" memory/guides/` runs, it
  returns nothing.
- **AC16** — When `bash tools/check-kit-versions.sh` runs after S12, the drift-audit `meta.version`
  and `gov:kit` marker agree at the new value.
- **AC17** — When `.claude/hooks/agent-cap.js` is compared to `tools/hooks/agent-cap.js`, they are
  byte-identical and `agent-cap.test.sh`'s parity arm passes.
- **AC18** — When `bash tools/run-gates.sh` runs, all 40 legs pass.
- **AC19** — When every existing arm of `agent-cap.test.sh` is fed through the hook before and after
  the S14 widening, the output is byte-identical. That is the MEASURED no-op, and the corpus is named:
  the arms of that file at the commit S14 lands on.
- **AC20** — When `.claude/settings.json` carries a Workflow-only matcher, `bash tools/check-wiring.sh
  --check` reports UNWIRED naming the matcher value it found; with `"Workflow|Agent"` it reports ok.
  Both observed. Today's file-wide grep reports ok for both, so the arm fails before the fix.
- **AC21** — When the wiring block is grepped across `WIRE-INTO-PROJECT.md`, `tools/hooks/agent-cap.js`
  and `tools/settings-merge.py`, no site states a matcher narrower than what S14 requires.
- **AC22** — When a real direct `Agent` spawn is made with a throwaway hook wired on that matcher,
  a payload is captured and its `tool_name` recorded. If no payload arrives, F4's fallback applies and
  S15 does not land as specced. This AC runs FIRST, before any S15 code.
- **AC23** — When six `Agent` payloads sharing one `prompt_id` are fed sequentially, the first five
  exit 0 and the sixth exits 2 with a message containing a string unique to this branch, asserted with
  `grep -qF` on the message and never on the exit code, which every branch of this hook shares.
- **AC24** — When the same six are fed CONCURRENTLY, exactly five tokens exist afterwards and exactly
  one deny is emitted. This is the arm the read-then-decide design fails, and it is run repeatedly
  rather than once, because the miscount it guards against is nondeterministic.
- **AC25** — When payloads carrying a fresh `prompt_id` follow a denied turn, they exit 0 with no
  cleanup step run in between.
- **AC26** — When the full `agent-cap.test.sh` suite runs after S15, every pre-existing `Workflow` arm
  passes unchanged, proving the count did not alter the static path.
- **AC27** — When only one of the two `settings-merge` version literals is bumped,
  `bash tools/check-kit-versions.sh` exits non-zero.

## 7. Gates

- `tools/hooks/agent-cap.test.sh` — the kit self-test, extended by S9.
- `tools/workflows/check-verifier-fanout.sh` — the committed-harness leg, which delegates to the hook.
- `tools/workflows/check-protocol-parity.test.sh` — extended by S8, re-rendered by S11.
- `tools/check-kit-versions.sh` — extended by S10, and the S12 pair.
- `tools/memory-tree/check-memory-hygiene.sh` — this spec is corpus and check 12 binds it.
- `tools/check-wiring.test.sh` — extended by S14 with the stale-matcher arm.
- `python tools/settings-merge.py --selftest` — its matcher arms are pinned literals and move with S14.
- `python tools/drift-audit/drift_report.py --check` — `non_terminal_specs_cited_by_product_source`
  sits at its pin with ZERO headroom, and this unit edits files under `tools/` and `.claude/`. No file
  in a product path may cite a non-terminal spec id; cite the run-state path and the phase contract
  instead, and keep build ids in `memory/`, which is deliberately outside that glob set.
- `bash tools/run-gates.sh` — the full bar at the push boundary.

S10 and S14 add assertions to existing legs rather than new legs. No new gate leg is introduced by
this unit.

## 8. Open questions

### F4 — does `PreToolUse` actually fire for a direct `Agent` spawn?

S15 depends on it and it is NOT established. The hook documentation does not enumerate the tool names
usable as a `PreToolUse` matcher, and it documents a SEPARATE `SubagentStart` event for subagent
spawns whose matcher filters on `agent_type` rather than on a tool name. `SubagentStart` explicitly
cannot block: exit 2 shows a notice and the subagent starts regardless.

**First build step, ahead of any S15 code (AC22):** wire a throwaway hook on the `Agent` matcher,
make one spawn, and record whether a payload arrives and what `tool_name` it carries.

**Fallback if it does not fire:** S15 becomes a `SubagentStart` COUNTER that records and reports but
cannot deny. The number then stays unenforced at spawn time for direct `Agent` calls, and that
residual is written into `memory/guides/REVIEW-PROTOCOL.md` under S11's rewrite rather than implied
away — that document already has a section for exactly this, naming where enforcement does NOT reach.

**Recommendation:** measure before speccing further. Do not build S15 on the assumption, and do not
let S14 wait on it, since S14 is inert either way.

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

### F3 — how far S12 bumps the drift-audit kit

S5 narrows an `args` contract the kit ships, which is a breaking change for an adopter passing
`cap` or `maxVerifiers`. Options: a minor bump with a migration line, or a major bump.
**Recommendation:** minor with the migration line, because the removed inputs never worked as
documented on any adopter whose hook enforced the rule.

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, grounded on the hard-caps audit at base `289daf72`.
- rev-2 · 2026-08-10 · folded the Tier-2 review `wf_093ab86e` (26 findings, 20 confirmed, precision
  0.77). S1 gained the argument extraction it never specified; S3 widened from the marker K to every
  `boundedK` consumer, which is the defect that left the concurrency knob resolving to 5; S4 gained
  the `cap` parameter case without which it denied all three shipped harnesses. Added S11 through
  S13 for the BINDING protocol rewrite, the drift-audit kit version and the wired hook copy. Replaced
  the four acceptance criteria that could not fail, and moved every arm from an exit code to the
  specific message its branch emits.

- rev-3 · 2026-08-10 · S14 folded in from `TOOL-aUnmannedHelm-1` per that build's ratified F2. This
  spec now owns every `agent-cap` edit, and `TOOL-aUnmannedHelm-1` depends on it landing. S14 has
  not been reviewed: the fold happened after this spec's Tier-2, so it re-reviews before code, and
  the three forks in §8 remain open.

- rev-4 · 2026-08-10 · folded the scoped Tier-2 on S14, `wf_154599e2`: 28 raw, 25 confirmed,
  precision 0.89, 6 blockers. S14 split at its seam per the owner's ratification — the matcher
  widening and the `check-wiring.sh` join fix stay here as a self-contained S14, and the enforcement
  predicate becomes S15 as an ATOMIC COUNT keyed on `tool_use_id` rather than a modality refusal.
  That choice dissolves the dependency cycle the fold created: S15 reads no run-state file, so
  `TOOL-aUnmannedHelm-1` and this spec no longer block each other. Six review findings died with the
  modality refusal. The rest are folded: acceptance criteria for both halves where there were none,
  the five missing Files-touched rows, the three-commit Rollout, the section 5 security split, the
  gate list, the title and section 1 which described only half the unit, and F4 for the seam this
  unit has not measured.

## 10. Reuse audit

The seam this unit wires through is `boundedK` at `tools/hooks/agent-cap.js:103-107`, already written
and already called once at `:135` for the `gov:fixed-verifiers` K. S1 through S3 add call sites and
narrow the resolver rather than introducing a second one, which is what keeps one rule with one
implementation. The forward paren join S1 needs also has a precedent in the file: the bracket-balance
walk at `:161-169`, which already joins lines until a literal closes.

`python tools/codebase-map/reuse_lookup.py "resolve an integer literal or file-bound constant to
check a cap"` did NOT surface it. The map's symbol corpus indexes Python functions and exported
JavaScript names, and `boundedK` is a non-exported function in a `.js` file, so no seam in the kit's
own hook is visible to the kit's own lookup. The seam was found by reading the file. That gap is
recorded as follow-up row `TOOL-aNumeralWarden-4` rather than worked around here.
