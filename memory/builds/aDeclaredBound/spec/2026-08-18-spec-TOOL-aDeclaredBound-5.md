# TOOL-aDeclaredBound-5 — the agent-cap number is single-sourced before it becomes adjustable

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

`5` is asserted as the enforced fan-out cap in at least eight live carriers. While the number is a
file constant every one of them is true. `TOOL-aDeclaredBound-4` makes it adjustable, at which point
every one of them becomes a second answer. Strip the assertions first, while they are still correct.

## 2. Scope (IN)

- **S1** — the measured population is enumerated as the first act of the build, not estimated from
  this spec. A grep for the number in a cap context across every tracked file that is not a frozen
  record is the population; the count below is what it measured on the base sha and is expected to
  move.
- **S2** — a carrier that states the ENFORCED cap stops stating a number and points at the hook. The
  phrasing is "the cap `agent-cap.js` enforces" or "the declared cap", not a figure.
- **S3** — a carrier that states the KIT'S SHIPPED DEFAULT may keep the number, because that is a
  fact about the kit rather than about a repo's setting, and it changes only with a kit release. It
  becomes a DECLARED PAIR in `tools/check-playbook-parity.sh`, which already exists to assert that a
  value the playbook states equals the source that owns it.
- **S4** — a FROZEN record keeps its number and is waived by path. `memory/gotchas/` entries,
  dated build records and archive files describe what was true when written; rewriting them is the
  defect this repo calls editing a landed row.
- **S5** — one gate: no un-waived carrier asserts a bare fan-out number. Modelled on
  `tools/check-install-prefix.sh`, which scans the shipped surface for a banned spelling and keys its
  exemptions in a shrink-only registry with a reason per row.
- **S6** — the waiver registry keys on the MATCHED TEXT, never on `<path>:<line>`. This is the
  correction `TOOL-aLoosenedCeiling-5` filed after the install-prefix registry unpinned itself twice
  in one build; a new registry should not repeat the shape that produced that row.
- **S7** — `memory/guides/REVIEW-PROTOCOL.md` is a read-path member, so this unit measurably
  SHRINKS the charter's mandatory reading. The change is reported in the build record with the
  before and after, because a unit that touches a read-path member should say what it did to the
  budget.

## 3. Non-goals (OUT)

- The value does not change. Every carrier that pointed at 5 points at a cap that is still 5.
- No behaviour changes. This unit edits prose and adds one gate; no engine reads anything new.
- The concurrency rule and the verify-stage rule are not merged. They are two rules with two
  numbers that happen to share a value, and `memory/gotchas/concurrency-is-not-a-budget.md` exists
  because conflating them was a real defect. Pointing at a declaration must not quietly make them
  one knob.
- `tools/hooks/agent-cap.js` is untouched. Its constants are unit 4's.

## 4. Design

### Inventory, measured at the base sha

| carrier | what it asserts | disposition |
|---|---|---|
| `AGENTS.md` | "at most 5 agents TOTAL" as the binding rule | S2 — point |
| `README.md` (three sites) | the cap-5 helpers, the file constant, the per-run budget | S2, except the "FILE CONSTANT" sentence which unit 4 rewrites |
| `memory/guides/REVIEW-PROTOCOL.md` (two sites) | the binding rule and the concurrency heading | S2 — point; this is the read-path member |
| `parallel-coding-governance.template.md` (two sites) | the shipped governance rule | S3 — declared pair, since the template ships to repos that may not adopt the kit |
| `memory/map/features/agent-cap.md` | "two numbers, both 5" plus the history of the 6 | S2 for the live claim, S4 for the historical sentence |
| `skills/session-kickoff/SKILL.md`, `.claude/skills/drift-audit/SKILL.md` | the rule as an instruction to an agent | S2 — point |
| `memory/gotchas/concurrency-is-not-a-budget.md` | the class, with the number as evidence | S4 — frozen |

Eight carriers, twelve sites, measured on `497d25d0`. S1 exists because that count is a measurement
and not a contract: the build re-measures rather than trusting this table.

### Why this lands BEFORE unit 4

Two orders are possible and one has a window in which the tree is wrong. Strip-then-adjust: every
carrier is true throughout, because they stop naming a number that has not yet moved.
Adjust-then-strip: between the two units the declaration can hold a value eight documents contradict,
including a BINDING protocol an agent is instructed to obey. The second order also makes unit 5 look
optional, which is how it would get dropped.

### What the gate can and cannot see

It scans for a number adjacent to fan-out vocabulary. It will not catch "no more than five agents"
spelled in words, and it will not catch a paraphrase that implies a bound without stating one. This
is the same limit `tools/check-method-carriers.sh` states about itself — structural only, a fluent
paraphrase passes — and the gate's header says so rather than letting a reader infer completeness.

### Files touched (estimate)

The eight carriers above, plus `tools/check-agent-cap-restatement.sh` and its self-test, its waiver
registry, one row in `tools/gate-legs.json`, and the four gates that a new leg trips together —
the codebase-map coverage assert, the map freshness byte-compare, the kickoff-manifest ratchet and
drift-audit's handkept-inventory signal.

### Alternatives rejected

- **Leave the carriers and gate them against the declaration.** Rejected: it keeps twelve copies and
  adds machinery to keep them equal, which is more moving parts than deleting eleven of them. The
  kit-version precedent in `AGENTS.md` — a version in prose "rotted twice in a day" — settled this
  shape for this repo already.
- **Do it inside unit 4.** Rejected by M2: two mechanisms, and a closing diff could not tell which
  half a finding landed on.
- **Skip the gate and rely on review.** Rejected: the restatements accumulated under review, which
  is the evidence that review does not catch this class.

## 5. Production-readiness checklist

- security — N/A. Prose edits and a read-only scanner.
- perf / scale — one grep-shaped pass over tracked docs; comparable to the install-prefix leg.
- a11y · i18n — N/A.
- error / empty / loading states — the gate must refuse an EMPTY population rather than pass: a
  scanner whose pattern matches nothing is the vacuous-selector class this repo already names, and
  its own arm has to prove the pattern can fire.
- observability — the gate names the file, the line and the matched text.
- risks — over-broad matching makes the waiver registry a chore and the gate a nuisance; the arm for
  that is a green control on a sentence that legitimately contains the digit.
- testing + left-shift gates — the gate IS the left-shift; its self-test carries a red fixture, a
  green control and a stale-waiver arm.
- migration / rollback — delete the leg row; the prose edits stand on their own.
- user docs — the carriers themselves are the docs.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-agent-cap-restatement.sh` runs on the tree before this unit's
  prose edits, it names at least ten sites; after them, it is silent. The first half is what proves
  the pattern fires.
- **AC2** — When a fixture adds a sentence asserting a bare fan-out number to a live carrier, `bash
  tools/check-agent-cap-restatement.test.sh` observes the gate naming it, and a control sentence
  containing the digit in an unrelated clause stays silent.
- **AC3** — When a waiver row's matched text no longer appears anywhere, `bash
  tools/check-agent-cap-restatement.test.sh` observes the gate reding as stale.
- **AC4** — When `bash tools/check-playbook-parity.sh` runs, the shipped-default pair S3 declares
  resolves and matches `agent-cap.js`'s constant, and an unresolvable pair reds rather than
  comparing empty to empty.
- **AC5** — When `python tools/memory-tree/corpus_ids.py --report` runs, the read path is smaller
  than at this unit's base by the bytes S7 records.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` and `python
  tools/drift-audit/drift_report.py --check` run, the new leg is claimed by a dossier and counted by
  the handkept signal, which is the four-gates-at-once fact `memory/guides/SESSION-KICKOFF.md`
  records about adding a leg.

## 7. Gates

`bash tools/check-agent-cap-restatement.sh` · `bash tools/check-agent-cap-restatement.test.sh` ·
`bash tools/check-playbook-parity.sh` · `bash tools/run-gates.test.sh` · `bash
tools/check-testsuite-counts.sh` · `python tools/codebase-map/test_codebase_map.py` · `python
tools/drift-audit/drift_report.py --check` · `bash tools/memory-tree/check-memory-hygiene.sh` ·
`bash tools/check-template-size.sh` · and `GATE_FULL=1 bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.

## 10. Reuse audit

Two existing seams carry this unit and neither needed inventing.

`tools/check-playbook-parity.sh` already implements S3: it asserts that a value the playbook STATES
equals the source that OWNS it, through declared pairs held in-script, and it already refuses a pair
whose extraction matches nothing rather than comparing empty to empty. The shipped-default figure in
the governance template becomes one more pair.

`tools/check-install-prefix.sh` is the shape for S5: a scan of the shipped surface for a banned
spelling, with deliberate exceptions in a shrink-only registry carrying a reason per row, and a
stale-waiver arm. S6 departs from it in exactly one respect, and does so because that departure is
already filed as `TOOL-aLoosenedCeiling-5` after its line-keyed registry unpinned itself twice
during one build.
