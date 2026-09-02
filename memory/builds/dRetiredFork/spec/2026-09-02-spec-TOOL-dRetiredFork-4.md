# TOOL-dRetiredFork-4 — the agent-cap nested-loop fail-open closes

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Absorb the `interpDepths` fix inCMS carries as `KIT_AGENT_CAP_DELTA` D1, filed upstream as
`ABL-aFerriedToolkit-3` and never taken. Measured at that adopter: a marked sequential-agent loop
nested inside another loop exits `0` where the unnested form exits `2`. gov HEAD has zero
occurrences of the fix. This is a fail-open in the hook that enforces the fan-out bound, so a wide
burst that the guard exists to refuse passes when it is written one level deeper.

## 2. Scope (IN)

- **S1** — Absorb the `interpDepths` stack into `tools/hooks/agent-cap.js`, so an `agent(` call's
  enclosing-loop depth is computed rather than inferred from the header line alone.
- **S2** — The refusal message names the enclosing loop, because the hook's contract is that a
  refusal names the first clause that fails.
- **S3** — Arms in `.claude/hooks/agent-cap.test.sh` covering the nested case both ways: the nested
  marked loop REFUSED, and the correctly unnested marked loop still admitted. Observed RED first.
- **S4** — Bump `KIT_AGENT_CAP_VERSION` and every tracked `*.js` carrying a `gov:kit agent-cap@`
  marker, which `tools/check-kit-versions.sh` derives rather than lists.
- **S5** — Restate nothing in the charter. `tools/hooks/README.md` already owns the grammar and
  gains the depth clause there.

## 3. Non-goals (OUT)

- Modelling regex literals in the literal-blanker. inCMS declined it and so does this unit: the
  regex-versus-division ambiguity is a real parser problem, and the shortcut of matching raw text is
  fail-closed in the wrong direction because the hook's own remedy string contains `parallel(` and so
  does every correct `boundedParallel` helper. It stays `ABL-dBriskLanyard-1`.
- Changing the bound. The number is parked at build level.

## 4. Design

### Data model

`interpDepths` is a stack of open-loop positions maintained across the literal-blanked scan. An
`agent(` occurrence is attributed to the innermost open loop, and a marked header whose stack is
non-empty at its own position is refused by the existing "no enclosing loop" clause — which is
already written in `tools/hooks/README.md` and is currently unenforceable because nothing computes
depth.

### Rollout

The hook ships to every adopter and is wired at SessionStart, so a false refusal is loud and
immediate. The two arms in S3 are the whole safety case; there is no flag and no staged rollout,
because a guard behind a default-OFF flag is not a guard.

### Alternatives rejected

Counting `for (` occurrences before the marked header. That is the inference the current code makes
and is exactly what the nested case defeats, because a closed loop and an open one look identical to
a counter.

## 5. Production-readiness checklist

- security — this IS the security surface. The hook bounds fan-out; a fail-open here is the whole
  defect, and the change is fail-closed by construction: an unresolvable depth refuses.
- perf / scale — one integer stack over a scan the hook already performs. No new pass.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a script the scan cannot parse must REFUSE, never admit. That is
  the existing contract and this unit must not weaken it.
- observability — the refusal names the enclosing loop and its line, so an author can act on it.
- risks — a false refusal blocks legitimate work at every adopter simultaneously, since the hook is
  wired at SessionStart. Mitigated by running the existing suite plus S3 before the version bump,
  and by the fact that the admitted-case arm is as load-bearing as the refused-case arm.
- testing + left-shift gates — `.claude/hooks/agent-cap.test.sh` is already a bar leg.
- migration / rollback — reverting is deleting the stack; no data, no receipt, no adopter state.
- user docs — the depth clause in `tools/hooks/README.md`.

## 6. Acceptance criteria

- **AC1** — When a `gov:sequential-agents(3)` loop sits inside another `for` loop,
  `bash .claude/hooks/agent-cap.test.sh` observes the hook exiting `2`, and the pre-change hook
  exited `0` on the same input.
- **AC2** — When the same marked loop has no enclosing loop, the hook still admits it and the
  existing arms are unchanged. Observed via `bash .claude/hooks/agent-cap.test.sh`.
- **AC3** — When the scan cannot resolve a depth, the hook refuses naming the unresolved position. Observed via `bash .claude/hooks/agent-cap.test.sh`.
- **AC4** — After the bump, `bash tools/check-kit-versions.sh` exits `0` and every tracked `*.js`
  carrying the marker agrees with `KIT_AGENT_CAP_VERSION`.
- **AC5** — `bash tools/check-agent-cap-restatement.sh` exits `0`, so the five machine-compared
  values in the charter still agree with the hook.

## 7. Gates

`agent-cap self-test` · `agent-cap restatement parity` · `kit versions` · `workflow syntax` ·
`verifier fan-out`.

## 8. Open questions

- **F1 — does gov credit the adopter in the source, or only in the record?** inCMS found this and
  `TOOL-aGradedDoorway-3` set the precedent of crediting in the file. Recommendation: credit at the
  site, because the next reader asking why the stack exists is owed the measurement that produced it.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, authored from the inCMS `KIT_AGENT_CAP_DELTA` D1 row and
  `ABL-aFerriedToolkit-3`.

## 10. Reuse audit

No existing seam fits. `python tools/codebase-map/reuse_lookup.py` reports the `agent-cap` affordance
seam covering `topLevelArgs`, which is the argument scan this unit sits beside but does not extend —
the depth stack is new state in an existing pass, and there is no fan-in-3 helper for loop-depth
anywhere in the corpus. The nearest prior art is the hook's own literal-blanked view, reused
unchanged.

Recall terms used: `agent-cap`, `fail-open`, `fan-out`, `sequential-agents`, `marker`, `bound`,
`nested loop`, `literal-blanked`, `hook`, `refusal`, `adopter`, `interpDepths`.
