# TOOL-aDeclaredBound-5 — the agent-cap number is single-sourced before it becomes adjustable

**Status:** OPEN · rev-2 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

`5` is asserted as the enforced fan-out cap across the live document surface. While the number is a
file constant every assertion is true. `TOOL-aDeclaredBound-4` makes it adjustable, at which point
each one becomes a second answer. Strip the assertions first, while they are still correct — and
deal first with the one a gate is holding in place.

## 2. Scope (IN)

- **S1** — the population is MEASURED as the first act of the build. The table in section 4 is what
  one grep found at the base sha, it was wrong in both directions when the audit re-ran it, and it
  is recorded as evidence rather than as a contract.
- **S2** — the gate-held assertion is resolved BEFORE any prose moves.
  `memory/guides/REVIEW-PROTOCOL.md` carries the literal `≤5 verify-stage agents TOTAL`, and
  `tools/workflows/check-protocol-parity.test.sh` greps for exactly that string. Stripping the digit
  reds a bar leg. The leg's own comment argues that a digit-free phrase is the failure mode it
  exists to catch, so this is not a matter of updating a literal — it is a decision about what that
  leg asserts, and it is this unit's first scope item rather than a discovery made mid-build.
- **S3** — `tools/workflows/REVIEW-PROTOCOL.template.md` moves with the installed copy. Parity diffs
  the two; editing one is editing half a pair.
- **S4** — a carrier that states the ENFORCED cap stops stating a number and points at the hook.
- **S5** — a carrier that states the KIT'S SHIPPED DEFAULT may keep the number. That is a fact about
  the kit, changes only with a kit release, and becomes a declared pair in
  `tools/check-playbook-parity.sh`, which already exists to assert that a value a document states
  equals the source that owns it.
- **S6** — FROZEN trees are excluded by PATH PREFIX, not by matched text: `memory/builds/`,
  `memory/archive/`, `memory/gotchas/`. These describe what was true when written.
- **S7** — LIVE exceptions are waived by MATCHED TEXT in a shrink-only registry, with a reason per
  row. The two mechanisms are separate because they cannot be one: the phrase `at most 5 agents
  TOTAL` appears in several live carriers AND in frozen records, so a text-keyed waiver written for
  a frozen record would silence every live carrier sharing the sentence. The first draft asked for
  one registry doing both jobs, which the audit showed is unsound.
- **S8** — the gate refuses an EMPTY population rather than passing, and its self-test carries a red
  fixture, a green control and a stale-waiver arm for each of the two mechanisms.

## 3. Non-goals (OUT)

- The value does not change. Every carrier that pointed at 5 points at a cap that is still 5.
- No engine reads anything new. This unit edits prose and adds one gate.
- The concurrency rule and the verify-stage rule are not merged. Two rules, two numbers that happen
  to share a value; `memory/gotchas/concurrency-is-not-a-budget.md` exists from conflating them
  once, and pointing at a declaration must not quietly make them one knob.
- `tools/hooks/agent-cap.js` is untouched. Its constants are unit 4's.

## 4. Design

### The gate-held assertion, and why it is scope item two

`check-protocol-parity.test.sh` asserts the protocol still contains `≤5 verify-stage agents TOTAL`.
That is a deliberate anti-vacuity arm: the leg's comment records that a digit-free paraphrase is
precisely the drift it was written to catch, because a protocol that says "the declared cap" without
a number is a protocol an agent cannot check itself against.

So this unit cannot simply strip that line, and the build must choose:

1. **Keep the number in the protocol and make it a declared pair**, as S5 does for the playbook —
   the protocol states the SHIPPED default and the parity leg's literal becomes a resolved pair
   rather than a frozen string. This keeps the anti-vacuity property and costs one more pair.
2. **Replace the digit with a pointer and give the leg a new anti-vacuity predicate** — the protocol
   must contain a reference to the declaration, and the leg asserts the reference rather than the
   digit.

RECOMMENDATION: option 1. It preserves an arm written for a real defect, it is the same mechanism S5
already needs for the playbook, and option 2 rebuilds an anti-vacuity predicate from scratch to save
one number in one file.

### Inventory, measured and then corrected

| carrier | verdict |
|---|---|
| `AGENTS.md` | states the enforced rule — S4 |
| `README.md` (three sites) | S4, except the "FILE CONSTANT" sentence, which unit 4 rewrites |
| `memory/guides/REVIEW-PROTOCOL.md` | S2's decision, and it carries MORE cap-context sites than the first draft's two |
| `tools/workflows/REVIEW-PROTOCOL.template.md` | S3 — the paired half the first draft missed |
| `parallel-coding-governance.template.md` (two sites) | S5 — declared pair |
| `WIRE-INTO-PROJECT.md` | S4 — missed by the first draft |
| `tools/drift-audit/SKILL.template.md` and its rendered copy | S4 — missed, and rendered, so it moves through the adopter script |
| `tools/drift-audit/README.md` | S4 — missed |
| `memory/map/features/agent-cap.md` | S4 for the live claim; the history sentence is prose about the past and stays |
| `memory/gotchas/concurrency-is-not-a-budget.md` | S6 — frozen |

`skills/session-kickoff/SKILL.md` was listed in the first draft and carries NO cap site. Its only `5`
is a line-count instruction, which makes it the natural green control for the gate's self-test
rather than a carrier. No total is stated here: three lenses produced three different counts, none
reproduced another's, and S1 measures rather than trusts.

### Why this lands BEFORE unit 4

Strip-then-adjust keeps every carrier true throughout. Adjust-then-strip has a window in which the
declaration can hold a value the documents contradict, including a BINDING protocol an agent is
instructed to obey. The second order also makes this unit look optional, which is how it would get
dropped.

### What the gate can and cannot see

It scans for a digit adjacent to fan-out vocabulary. It will not catch "no more than five agents"
in words, and it will not catch a paraphrase that implies a bound without stating one — the same
limit `tools/check-method-carriers.sh` states about itself. The gate's header says so rather than
letting a reader infer completeness.

### Files touched (estimate)

The carriers above, `tools/workflows/check-protocol-parity.test.sh` per S2's decision,
`tools/check-agent-cap-restatement.sh` and its self-test, two registries, a row in
`tools/gate-legs.json`, and the gate-leg descriptor rows a new leg needs.

### Alternatives rejected

- **Gate the carriers against the declaration instead of deleting them.** Rejected: it keeps every
  copy and adds machinery to keep them equal. `AGENTS.md` settled this shape for the kit version —
  a number in prose "rotted twice in a day".
- **Do it inside unit 4.** Rejected by M2: two mechanisms, and a closing diff could not say which
  half a finding landed on.

## 5. Production-readiness checklist

- security — N/A. Prose edits and a read-only scanner.
- perf / scale — one grep-shaped pass over tracked docs.
- a11y · i18n — N/A.
- error / empty / loading states — S8's empty-population refusal.
- observability — the gate names file, line and matched text.
- risks — the honest one is BUILDABILITY: nobody has written the pattern, so its false-positive rate
  over the workflow harnesses and the frozen trees is unmeasured, and the audit named this the
  largest open cost in the build. The first pass measures it before the prose edits begin, and a
  rate that makes the registry a chore is a reason to reconsider option 2 in section 4.
- testing + left-shift gates — the gate IS the left-shift; S8 arms both waiver mechanisms.
- migration / rollback — delete the leg row; the prose edits stand alone.
- user docs — the carriers are the docs.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-agent-cap-restatement.sh` runs BEFORE this unit's prose edits, it
  names the carriers S1 measured; after them, it is silent. The first half is what proves the
  pattern fires rather than passing by finding nothing.
- **AC2** — When a fixture adds a bare fan-out assertion to a live carrier, `bash
  tools/check-agent-cap-restatement.test.sh` observes the gate naming it, and the line-count
  sentence in `skills/session-kickoff/SKILL.md` stays silent as the green control.
- **AC3** — When a live waiver row's matched text is gone, `bash
  tools/check-agent-cap-restatement.test.sh` observes the gate reding as stale; and when a frozen
  path prefix selects nothing, it reds the same way.
- **AC4** — When `bash tools/workflows/check-protocol-parity.test.sh` runs after S2's decision, it
  is green and its assertion is not vacuous — either a resolved pair or the new predicate, per the
  option chosen.
- **AC5** — When `bash tools/check-playbook-parity.sh` runs, S5's shipped-default pair resolves and
  matches the hook's constant, and an unresolvable pair reds rather than comparing empty to empty.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh`, `python
  tools/codebase-map/test_codebase_map.py`, `python tools/govkit/govkit.py selfcheck` and `python
  tools/govkit/selftest.py` run after the leg lands, all four are green. These are the four a new
  leg was MEASURED to trip; the first draft named the coverage assert and the handkept signal,
  which the same measurement recorded as NOT firing.

## 7. Gates

`bash tools/check-agent-cap-restatement.sh` · `bash tools/check-agent-cap-restatement.test.sh` ·
`bash tools/workflows/check-protocol-parity.test.sh` · `bash tools/check-playbook-parity.sh` · `bash
tools/drift-audit/adopt-drift-audit.sh --check` · `bash tools/run-gates.test.sh` · `python
tools/govkit/govkit.py selfcheck` · `python tools/govkit/selftest.py` · `bash
tools/check-testsuite-counts.sh` · `python tools/codebase-map/test_codebase_map.py` · `bash
tools/memory-tree/check-memory-hygiene.sh` · `bash tools/check-template-size.sh` · and `GATE_FULL=1
bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

- **Section 4's two options for the gate-held assertion.** RESOLVED (agent, 2026-08-18, delegated by
  nothing — recorded as a RECOMMENDATION rather than a ratification): option 1, keep the number in
  the protocol as a declared pair. The owner should overrule if they would rather the protocol
  carried no digit at all, because that is a judgement about what an agent can check itself against
  and not a technical one.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded spec-audit round 1, which BLOCKED on this unit. Stripping the digit
  from the review protocol reds `check-protocol-parity.test.sh`, whose assertion is a deliberate
  anti-vacuity arm; that is now S2 and the first thing the build decides. S3 adds the template half
  of a pair the first draft edited alone. The inventory was wrong in both directions — one listed
  carrier has no cap site and four live carriers were missing — and the invented total is gone. S6
  and S7 split one impossible registry into two, because a text-keyed waiver for a frozen record
  would silence the live carriers that share its sentence. AC6 named two gates a prior measurement
  recorded as NOT firing.

## 10. Reuse audit

Satisfied for the set by `TOOL-aDeclaredBound-4` §10.

`tools/check-playbook-parity.sh` already implements S5 and section 4's option 1: it asserts that a
value a document STATES equals the source that OWNS it, through declared pairs held in-script, and
it already refuses a pair whose extraction matches nothing rather than comparing empty to empty.

`tools/check-install-prefix.sh` is the shape for the scanner: a scan of the shipped surface for a
banned spelling, exemptions in a shrink-only registry with a reason per row, and a stale-waiver arm.
S7 departs from it by keying on matched text rather than `<path>:<line>` — the correction
`TOOL-aLoosenedCeiling-5` filed after that registry unpinned itself twice in one build — and S6
departs further by adding a path-prefix mechanism that registry does not have.
