# TOOL-aRuledParchment-1 — Port the spec-format discipline into the memory-tree kit

**Status:** CLOSED · rev-1 · 2026-07-15 · node a · Tier-1 · base c78958c7 · ratified upstream 2026-07-14 · review wf_8643be81 (inCMS)

## 1. Goal

Make the canonical spec/design-pass format (status header + nine sections + machine gate) a
reusable part of the memory-tree kit, so every adopting repo gets the same discipline inCMS
ratified — instead of it living as a one-repo customization.

## 2. Scope (IN)

- S1 `SPEC-TEMPLATE.template.md` in the kit, copied to `<MEMORY_ROOT>/TEMPLATE-SPEC.md` at
  scaffold time by `adopt-memory-tree.sh`.
- S2 Check 12 in `check-memory-hygiene.sh`, gated on a new `.memory-tree.conf` key
  `SPEC_FORMAT_CUTOFF` (blank = disabled; adopters set their adoption date).
- S3 The hardened `_unfenced` helper (CR-strip + marker-matched fences), also wired into check 2.
- S4 Seam updates: check-3 root sanction, HYGIENE template + this repo's instance, kit README,
  conf example, adopt-script scaffold + next-steps, `gen-memory-tree.sh` root list, playbook
  design-pass line, generic kickoff SKILL step 3, WIRE-INTO-PROJECT §3, run-gates legs.
- S5 `check-memory-hygiene.test.sh` — fixture self-test covering every check-12 class plus the
  disabled-when-blank contract.
- S6 Dogfood: this repo arms `SPEC_FORMAT_CUTOFF="2026-07-15"`; this spec is the first governed
  file.

## 3. Non-goals (OUT)

- No retrofit of this repo's three pre-existing free-named specs (never match the dated glob).
- No formats for reviews/build/prompts kinds (same follow-up posture as upstream).
- No descriptor-tail adoption in check 5 (check 12's glob already tolerates one if that lands).

## 4. Design

Faithful port of inCMS ARCH-aRuledParchment-1/-2 (adversarially reviewed there: 12 agents,
precision 0.97, all confirmed findings folded upstream before this port). Differences from
upstream are config-mechanical only: the cutoff comes from `.memory-tree.conf` instead of a
hardcoded date, paths derive from `MEMORY_ROOT`, and the check is disabled until a repo opts in —
a kit must not red existing adopters on pull.

### Files touched (estimate)

Kit: 6 files under `tools/memory-tree/` (+1 new template, +1 new test). Repo docs: playbook,
generic SKILL, WIRE, run-gates. Dogfood: conf, `memory/TEMPLATE-SPEC.md`, `memory/HYGIENE.md`,
this build folder, ledger, journal, TREE regen.

## 5. Production-readiness checklist

- security: N/A — read-only doc gate.
- perf / scale: spawn-free date filter; disabled repos pay one `[ -n ]` test.
- a11y / i18n: N/A — agent-facing docs.
- error / empty / loading states: N/A — not a UI.
- observability: heading mismatches print a canonical-vs-actual diff.
- risks: `_unfenced` change also affects checks 2/7 in every adopting repo — covered by this
  repo's full gate run; adopters re-run their own gate on kit pull.
- testing + left-shift gates: S5 self-test wired as a run-gates leg.
- migration / rollback: additive; revert = git revert, conf key simply ignored by old script.
- user docs: kit README + WIRE + adopt-script next-steps updated.

## 6. Acceptance criteria

- AC1 When `SPEC_FORMAT_CUTOFF` is set and a governed spec violates any check-12 rule, the gate
  fails naming the file and rule; when the spec conforms or is Tier-1-light, it stays silent.
- AC2 When `SPEC_FORMAT_CUTOFF` is blank, nonconforming specs produce no check-12 output.
- AC3 `check-memory-hygiene.test.sh` exits 0 (14 assertions, scratch repo).
- AC4 This repo's full gate suite (`tools/run-gates.sh`) is green with the ratchet armed.

## 7. Gates

- `bash tools/run-gates.sh` (memory hygiene 12 checks · template size · all kit self-tests,
  including the new memory-hygiene self-test leg).

## 8. Open questions

none — all format forks were RESOLVED (owner, 2026-07-14) upstream in inCMS; this port adds only
the conf-gating mechanics.

## 9. Revision log

- rev-1 · 2026-07-15 · initial port from inCMS ARCH-aRuledParchment-1/-2.
