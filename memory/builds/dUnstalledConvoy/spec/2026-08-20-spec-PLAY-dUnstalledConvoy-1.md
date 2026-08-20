# PLAY-dUnstalledConvoy-1 — the charter drops a refuted premise while keeping the conclusion it happened to support

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams playbook · ratified 2026-08-20

## 1. Goal

The playbook's §8 asserts that orchestration sidechains inherit "neither your hooks nor the governing
doc". Both halves were measured FALSE. The review protocol was corrected; the charter and the SHIPPED
PRODUCT TEMPLATE were not, so every adopter receives the refuted sentence and it is the sentence that
blocked the parallelism inversion. This unit deletes the premise and keeps the conclusion, which
survives for a different and stated reason.

## 2. Scope (IN)

- **S1** — the clause "inheriting neither your hooks nor the governing doc" is deleted from
  `coding-governance-agents.template.md` §8.
- **S2** — the surviving conclusion is kept and its ACTUAL reason is stated: a sidechain agent holds
  no fan-out tool at all, so the cap has nothing to bind at that depth, and the main loop is where
  the fan-out decision is made. The conclusion is not weakened, because it was never wrong.
- **S3** — the restricted-runtime fact is kept verbatim. Plain JS with no type syntax and no imports
  is true, is load-bearing for anyone writing a workflow script, and was never part of the refuted
  claim.
- **S4** — `AGENTS.md` is RE-RENDERED rather than hand-edited. The sentence sits at line 315, inside
  the `gov:playbook` region that spans lines 76 to 464, so the template is the single source and the
  charter's copy is generated.
- **S5** — the edit is measured against the template's byte ceiling before commit. The margin at BASE
  is 989 bytes of 49 152, and the gate also warns past a recorded high-water.
- **S6** — a backlog row is opened for the drift class itself, because no row covered this one and
  the same shape can recur wherever a correction lands in one carrier of a claim held by several.

## 3. Non-goals (OUT)

- Correcting `memory/guides/REVIEW-PROTOCOL.md`. It was already corrected and carries the measurement.
  Touching it again would be a second answer to a settled question.
- Weakening the enforcement rule. The cap is still enforced at the tool call and still not inside the
  script. S2 keeps the conclusion and replaces only its justification.
- Claiming the `PreToolUse` reach into a sidechain is settled. The prior probe recorded it as
  UNMEASURED, because the matcher covers two tools a sidechain does not hold. The new text must not
  upgrade "unmeasured" to "does not fire".
- Raising the template ceiling. S5 measures; a breach is a fork, not an edit to the constant.
- Any change to `tools/hooks/agent-cap.js` or its README.

## 4. Design

### What was measured, and what each half of the sentence is worth now

| Clause | Status | Evidence |
|---|---|---|
| sidechains inherit no governing doc | **FALSE** | the probe's first message carried the whole charter before it read anything |
| sidechains inherit no hooks | **FALSE** | a `SubagentStart` hook fired and arrived with a verbatim header |
| the runtime is restricted plain JS | true | unchanged, and independently observable |
| the cap is enforced at the tool call, never inside the script | true | and the reason below is not the one the sentence gives |
| a `PreToolUse` hook fires inside a sidechain | **UNMEASURED** | the matcher names two tools a sidechain does not hold, so nothing could fire |

### The trap this unit must not fall into

The refuted premise supports a true conclusion. A correction that deletes the premise and follows the
logic would flip the conclusion and be wrong in a more expensive way — it would tell every adopter
that a workflow script can be trusted to police its own fan-out.

The conclusion survives because a sidechain agent cannot fan out AT ALL: it does not hold the tools
the cap matches. That is a stronger property than being policed, and the prior record says so in
those words. S2's job is to write that reason in place of the false one, in one clause, without
growing the sentence.

### Why the render and not the file

`AGENTS.md` line 315 is inside the `gov:playbook` region. The charter's copy is generated from the
template by `tools/playbook/`, and `bash tools/playbook/adopt-playbook.sh --target . --check`
byte-compares the two as a gate leg. Hand-editing the charter would red that leg and would create the
second copy this unit exists to remove.

### Byte budget, and the known-red neighbour

The template is 48 163 bytes against a 49 152 ceiling, so the margin is 989 bytes and the gate warns
past a recorded high-water as well. The edit replaces a clause with a shorter one and should be net
negative; it is measured with `bash tools/check-template-size.sh` rather than estimated, because that
figure is recorded as having moved twice in one day.

Separately, the `govkit acceptance matrix` leg is RED on clean `main` for an unrelated reason the
kickoff manifest carries as a dated correction, and it blocks every push through the mandated lander.
That is an external blocker on LANDING this unit, not a defect in it, and it is named here so the
build does not diagnose it twice.

### Files touched (estimate)

| File | Change |
|---|---|
| `coding-governance-agents.template.md` | one bullet in §8 |
| `AGENTS.md` | re-rendered, not edited |
| `memory/backlog/PLAY.md` or `memory/backlog/TOOL.md` | one new row, S6 |

### Alternatives rejected

- **Deleting the whole bullet.** Rejected: three of its five claims are true and two of them are the
  only place the charter tells a script author about the runtime and the cap.
- **Keeping the premise with a caveat.** Rejected: a sentence that says a thing and then says it is
  not true is two answers to one question, which is the class this unit is closing.

## 5. Production-readiness checklist

- security — the conclusion being preserved IS the security content. A weakened conclusion would tell
  adopters an unbounded fan-out inside a script is policed when nothing policies it.
- perf / scale — N/A — documentation.
- a11y — N/A — documentation.
- i18n — N/A — documentation.
- error / empty / loading states — N/A — documentation.
- observability — S6's backlog row is what makes the drift CLASS visible after this instance is
  fixed.
- risks (concurrency, data-loss, rollback hazards) — the byte ceiling and the render parity are the
  two ways this unit can red the bar, and both are gated rather than remembered.
- testing + left-shift gates — `playbook render wiring`, `playbook parity` and `template size` all
  read what this unit writes. No new gate: the class is already gated, and this is an instance.
- migration / rollback — none. Adopters re-pull the template on kit update.
- user docs — the template IS the user doc, and the charter is its render.

## 6. Acceptance criteria

- **AC1** — `grep -n "inheriting neither your hooks nor the governing doc"` returns nothing in
  `coding-governance-agents.template.md` and nothing in `AGENTS.md`.
- **AC2** — The surviving bullet still states that the cap is enforced at the tool call and never
  inside the script, and states the no-fan-out-tool reason, observed in `coding-governance-agents.template.md`.
- **AC3** — The bullet does not claim a `PreToolUse` hook fails to fire in a sidechain, because that
  is recorded UNMEASURED.
- **AC4** — `bash tools/playbook/adopt-playbook.sh --target . --check` exits 0, proving `AGENTS.md`
  is the render and not a hand edit.
- **AC5** — `bash tools/check-template-size.sh` reports the file under the ceiling, and the commit
  message carries the measured figure.
- **AC6** — A backlog row exists naming the drift class, and it names the carriers a correction to a
  shared claim must sweep, observed in `memory/backlog/TOOL.md`.

## 7. Gates

`playbook render wiring` · `playbook parity` · `playbook placeholder catalogue` · `template size` ·
`drift-audit records` · the full bar at the push boundary.

## 8. Open questions

- **F1 — RESOLVED (agent, 2026-08-20, delegated): the `TOOL` shard owns the drift-class row. The instance is a playbook-carrier defect but the CLASS is a tooling question about how a correction sweeps every carrier of one claim, and an open row already generalises exactly that for kit-version markers in `TOOL`. Two rows about the same shape belong in one shard so they can close together.**

  The question this settles: which backlog family owns S6's row? The instance is a playbook-carrier defect, so `PLAY`
  fits; the CLASS is a tooling question about how a correction sweeps every carrier of one claim, and
  an open row already generalises exactly that for kit-version markers, in `TOOL`. **Recommendation:
  `TOOL`**, cross-referenced from this spec, so the two rows about "a fix naming more than one
  carrier landing in only one" sit in the same shard and can be closed together.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the charter is rendered from the playbook template and a
gate byte-compares them"` returns the `govkit` affordance seam and the playbook dossiers. The seam is
the existing `gov:playbook` marker region plus `adopt-playbook.sh --check`, both already gate legs;
this unit adds nothing and rides them.

`python tools/memory-recall/query.py "do orchestration sidechains inherit hooks and the governing
doc, and what was measured" --terms "sidechain inherit hooks CLAUDE.md governing doc subagent start
probe agent-cap fan-out tool call PreToolUse unmeasured"` returns the parallelism verdict record and
the evidence document carrying the measurement. Verified at source at writing time: the refuted
clause is present at `coding-governance-agents.template.md` §8 and at `AGENTS.md` line 315, the
latter inside the generated region, and `memory/guides/REVIEW-PROTOCOL.md` carries the correction
that never reached either.

Recall terms used: sidechain inherit hooks CLAUDE.md governing doc subagent start probe agent-cap
fan-out tool call PreToolUse unmeasured.
