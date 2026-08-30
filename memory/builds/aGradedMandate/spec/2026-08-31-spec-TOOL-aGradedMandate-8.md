# TOOL-aGradedMandate-8 — the agent-facing carriers corrected, in one render

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-1 · base 396cd9db · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-2 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

Five statements an unattended agent reads are wrong or missing in a way that changes what the agent
DOES. They are collected into one edit of the two kit templates and one adopter render, so the
divergence is repaired once rather than five times.

## 2. Scope (IN)

- **S1** — The Skill says "One item has NO override" and names `authorization-reachable`. The driver
  holds two: `DOD_NO_OVERRIDE="authorization-reachable pieces-complete"`. Name both, and add the
  `--abort` route to the paragraph that offers `--override`.
- **S2** — The Skill's forbidden dispositions for a promoted blocker read "Not parked, not waived,
  and not re-reviewed", which is exhaustive in tone and omits the cheapest exit. Add "not retired".
- **S3** — The Skill's "While it runs" walks nine verbs and never names the one per-pass quality act
  on CODE: `python tools/memory-tree/gotchas.py --for-diff <range>`, which M6 mandates per pass and
  M8 re-mandates over the full range on every closing round. Neither kit carrier mentions it. Name
  it, with the committed-range caveat that makes the pre-commit spelling read as a clean checklist.
- **S4** — All six documented `--record-piece` / `--record-set` invocations spell `--verdict PASS`,
  and `FAIL` appears in no example. Make one example spell `FAIL`, so the instruction layer stops
  priming the answer on the item that takes no override.
- **S5** — The protocol's §2 fact 3 enumerates five parked kinds against the driver's eight and says
  all four listed kinds are surfaced. Correct the enumeration and the surfaced claim, in the
  template and its render, which two legs byte-compare.
- **S6** — Name the diff-driven self-test escalation `TOOL-aGradedMandate-3` adds in the Skill's
  `--close` section, and the retirement split `TOOL-aGradedMandate-5` adds in its `--rescope`
  paragraph, so a run learns about both from the file it actually reads.

## 3. Non-goals (OUT)

- **No edit to a carrier outside this kit.** The charter, the build method and `memory/HYGIENE.md`
  are M3 veto 2 and are out of the prompt's stated scope, which is "any layer of the kit".
- **No new rule.** Every sentence here either states what the code already does or points at a
  section that owns a rule. A gloss that grew into a condition would be the defect the pointer design
  exists to avoid.
- **No render of the DoD set into the Skill.** Enumerating the ten items in an agent-facing carrier
  creates a fourth copy of a set that already has three; only the non-overridable pair is named,
  because that is the pair the agent has to act on at close.

## 4. Design

The edits land in `tools/unattended/SKILL.template.md` and `tools/unattended/PROTOCOL.template.md`,
and the renders `.claude/skills/unattended/SKILL.md` and `memory/guides/UNATTENDED-PROTOCOL.md` are
produced by `bash tools/unattended/adopt-unattended.sh` rather than hand-edited, because the wiring
leg byte-compares the pair and a hand edit is how the two stop agreeing.

### Files touched (estimate)

| File | Why |
|---|---|
| `tools/unattended/SKILL.template.md` | S1, S2, S3, S4, S6 |
| `tools/unattended/PROTOCOL.template.md` | S5 |
| `.claude/skills/unattended/SKILL.md` | render |
| `memory/guides/UNATTENDED-PROTOCOL.md` | render |

### Alternatives rejected

Hand-editing the renders. Rejected by the wiring leg's own existence.

## 5. Production-readiness checklist

- security — N/A. Prose.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the render is verified by the existing wiring leg rather than by eye.
- risks — the Skill carries byte ceilings through the kit's own size checks; the additions are short
  and the render is re-run rather than patched.
- testing + left-shift gates — the machine half is `TOOL-aGradedMandate-9`, which makes the S1 class
  of divergence red rather than ship. S2 to S6 have no machine half and that is stated here.
- migration / rollback — reverting the template and re-rendering.
- user docs — this unit IS the user docs.

## 6. Acceptance criteria

- **AC1** — `grep -c "pieces-complete" .claude/skills/unattended/SKILL.md` is at least 1, and the
  paragraph naming the non-overridable set names both members and the `--abort` route.
- **AC2** — `grep -c "not retired" .claude/skills/unattended/SKILL.md` is at least 1.
- **AC3** — `grep -c "gotchas.py" .claude/skills/unattended/SKILL.md` is at least 1.
- **AC4** — `grep -c -- "--verdict FAIL" .claude/skills/unattended/SKILL.md` is at least 1.
- **AC5** — `bash tools/check-wiring.sh --check` reports the installed Skill matching the tracked
  render, and `bash tools/unattended/run-unattended-gates.sh --checks` reports the protocol pair
  byte-identical.
- **AC6** — The rendered Skill still passes whatever size and shape checks the kit's own leg applies
  to it, verified by `bash tools/unattended/check-unattended.sh`.

## 7. Gates

`unattended skill wiring` · `unattended kit gate` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from findings F10, F6 and F7 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10.

The seam is `tools/unattended/adopt-unattended.sh`, the kit's own renderer, and the existing
convention that the two `*.template.md` files are the sources and the two renders are outputs. No new
mechanism: the directive table in the Skill is already rendered and already joined to the driver in
both directions by the leg, and this unit adds prose to files that pipeline already carries.
