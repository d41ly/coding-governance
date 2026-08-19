# TOOL-aDeclaredBound-5 — the agent-cap number is single-sourced before it becomes adjustable

**Status:** CLOSED · rev-5 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling · ratified 2026-08-18

## 1. Goal

`5` is asserted as the enforced fan-out cap across the live document surface. While the number is a
file constant every assertion is true. `TOOL-aDeclaredBound-4` makes it adjustable, at which point
each one becomes a second answer. Strip the assertions first, while they are still correct — and
deal first with the one a gate is holding in place.

## 2. Scope (IN)

- **S1** — the population is MEASURED as the first act of the build. The table in section 4 is what
  one grep found at the base sha, it was wrong in both directions when the audit re-ran it, and it
  is recorded as evidence rather than as a contract.
- **S2** — `memory/guides/REVIEW-PROTOCOL.md` loses the digit and gains a POINTER, and
  `tools/workflows/check-protocol-parity.test.sh` gets a NEW anti-vacuity predicate to replace
  the frozen literal it greps for today. Ratified by the owner over the cheaper alternative of
  keeping the number as a declared pair. This is the first scope item because the leg reds the
  moment the prose moves, and because the replacement predicate is the unit's only genuinely new
  machinery.
- **S2b** — the replacement predicate asserts what the old literal was protecting, which is NOT the
  number. It is SPLIT BY LANDING, ratified by the owner, because its two halves depend on different
  units. **This unit asserts the POINTER SHAPE only**: every section that states a fan-out bound
  names the file that resolves it, which is `tools/hooks/agent-cap.js` today. **Unit 4 adds the
  reads-it half** — that the named declaration is one the hook actually reads — in the same commit
  that makes the hook read it. Rev-4 required both halves here, and neither the conf key nor the
  read exists until unit 4 lands, so the predicate could not be satisfied at this unit's own
  commit while §3 forbids touching the hook.
- **S2c** — the predicate is PER RULE, not per document. The protocol states two bounds in two
  sections — a verify-stage total and a concurrency limit — and §3 insists they stay two rules
  because conflating them was a real defect. One predicate over "the section" cannot bind both, so
  each section that states a bound is checked for its own pointer.
- **S2d** — the CODE-SHAPED sites keep their digits, with the reason stated rather than left to the
  scanner's silence. The protocol instructs an agent to inline a bounded call with a literal width;
  that literal is the argument the hook resolves at the call site, not a restatement of the rule.
  No bound word is adjacent, so S9's scanner never sees them — which means the gate cannot arbitrate
  this and the spec must.
- **S3** — `tools/workflows/REVIEW-PROTOCOL.template.md` moves with the installed copy. Parity diffs
  the two; editing one is editing half a pair.
- **S4** — a carrier that states the ENFORCED cap stops stating a number and points at the file that
  resolves the bound. Same target as S2b's pointer-shape half, named identically in both, because
  rev-4 gave the protocol one target and the other carriers another and said which nowhere.
- **S5** — a carrier that states the KIT'S SHIPPED DEFAULT may keep the number, and the test is the
  SENTENCE rather than the file. Rev-4 applied this to the governance template wholesale, which is
  wrong: that template states the ENFORCED rule in at least three places and never says what the
  kit ships, so "changes only with a kit release" is false for every one of them. Those become S4
  carriers. S5 keeps only a sentence literally phrased as the shipped default, and the pair's
  extraction reads a constant carrying an in-file comment saying it is the default and not the
  enforced bound.
- **S5b** — the declared-pair guarantee is GOV-LOCAL and buys an adopter nothing. The parity gate
  compares the template against this repo's own hook and runs in no adopter tree. Said here because
  S5 otherwise reads as protection that ships.
- **S6** — FROZEN trees are excluded by PATH PREFIX, not by matched text: `memory/builds/`,
  `memory/archive/`, `memory/gotchas/`, and `memory/backlog/`. The fourth was missing and is not a
  waiver case: a backlog row QUOTES a carrier to describe work outstanding, and this build's own
  row for the stale `≤6` in a harness would have been flagged by its own gate. Append-only records
  of past or pending state are the class, and stating it as a prefix keeps AC3's stale-prefix arm
  covering it.
- **S7** — LIVE exceptions are waived by MATCHED TEXT in a shrink-only registry, with a reason per
  row. The two mechanisms are separate because they cannot be one: the phrase `at most 5 agents
  TOTAL` appears in several live carriers AND in frozen records, so a text-keyed waiver written for
  a frozen record would silence every live carrier sharing the sentence. The first draft asked for
  one registry doing both jobs, which the audit showed is unsound.
- **S8** — the gate refuses an EMPTY population rather than passing, and its self-test carries a
  red fixture, a green control and a stale-waiver arm for each of the two mechanisms.
- **S9** — the scanner has THREE constraints and all three are written here, because rev-4 named
  two and the measurement record named two while the run that produced its figure used three.
  (a) a BOUND WORD adjacent to the number, from the alternation the record lists; (b) a fan-out
  NOUN following it, from a closed list — `agents`, `verifiers`, `lens`/`lenses`, `skeptics`,
  `concurrent`, `per verify stage`, `are verify-stage`, `ever run`, `batched`; (c) MARKDOWN ONLY.
  The noun list is the one that was load-bearing and undocumented: without it the pattern matches
  54 lines across 23 files rather than 19 across 11, and it matches the very line AC2 names as the
  gate's green control.
- **S10** — the gate's header states its two blind spots in the register
  `check-method-carriers.sh` uses about its own: the noun list is a LIST, so a carrier phrased
  outside it is invisible; and executable files are out of scope, so a bound stated in a comment
  inside a harness is not seen. Both were OBSERVED during the measurement rather than imagined.

## 3. Non-goals (OUT)

- The value does not change. Every carrier that pointed at 5 points at a cap that is still 5.
- No engine reads anything new. This unit edits prose and adds one gate.
- The concurrency rule and the verify-stage rule are not merged. Two rules, two numbers that happen
  to share a value; `memory/gotchas/concurrency-is-not-a-budget.md` exists from conflating them
  once, and pointing at a declaration must not quietly make them one knob.
- `tools/hooks/agent-cap.js` is untouched. Its constants are unit 4's.

## 4. Design

### The gate-held assertion, and what replaces it

`check-protocol-parity.test.sh` asserts the protocol still contains the bare literal. That is a
deliberate anti-vacuity arm: the leg's comment records that a digit-free paraphrase is precisely
the drift it was written to catch, because a protocol saying "the declared cap" without saying
what to read is a protocol an agent cannot check itself against.

The owner ratified replacing the digit with a pointer and rebuilding that arm, over the cheaper
option of keeping the number as a declared pair. That is the more expensive path and it buys the
thing this unit exists for: afterwards the number lives in exactly ONE place, and the BINDING
document an agent reads sends it there rather than carrying a copy a declared pair would keep
merely CORRECT.

The replacement is NOT "assert a reference exists". A pointer to the wrong thing, or a pointer
in a section that no longer states the rule, would pass such a check while leaving the protocol
as unusable as a bare paraphrase. Hence S2b's two-part predicate. The second half — that the
named file is one the hook actually reads — is what keeps the arm from becoming a spellcheck,
and it is the reason this option costs more than the one it displaced.

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

### What the gate can and cannot see, measured

The pattern was written and run before this unit was scheduled, at the owner's instruction. Three
passes: 276 matching lines across 634 files unfiltered; 55 after S6's frozen-tree exclusion, of
which 30 were false positives; and 18 after S9's two tightenings, of which ZERO are false
positives. The 18 land in the ten carriers this section's table names. Full working, including
the classification of all 55, is in `build/2026-08-18-build-TOOL-aDeclaredBound-5-gate-measurement.md`.

Two blind spots, both OBSERVED rather than predicted, and both S10's to declare:

The noun list is a list. The first tightened pattern silently lost `≤5 batched default-refute
skeptics` in the protocol, twice, because "skeptics" was not in it. A carrier phrased outside the
vocabulary is invisible, which is why S1 measures rather than trusting the gate to enumerate.

Markdown-only has a live cost and here it is: `tools/workflows/tier2-review.js` says `≤5
concurrent` on line 7 and `ONE ≤6-wide wave` on line 128, while its code fans at 5. Stale prose
inside the harness the BINDING protocol points at, predating this build, and a markdown-only gate
cannot see it. Filed as a backlog row rather than folded in, because widening the scope to catch
one comment is what the 64% rate was made of.

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
- risks — buildability was the audit's largest open cost and is now MEASURED at zero false
  positives over 18 hits, so the waiver registry S7 provides may well ship empty. What replaces
  that risk is the false-NEGATIVE one in section 4: a zero-FP pattern is a narrow pattern, and
  narrowness is why it missed two real carriers on its first tightening.
- testing + left-shift gates — the gate IS the left-shift; S8 arms both waiver mechanisms.
- migration / rollback — delete the leg row; the prose edits stand alone.
- user docs — the carriers are the docs.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-agent-cap-restatement.sh` runs BEFORE this unit's prose edits,
  its output equals the CLASSIFIED HIT LIST the build re-measures and records under `build/` at
  this build's own base; after the edits, it is silent. Not a bare integer: rev-4 pinned the build
  to "18 sites across ten files", which no documented pattern reproduced and which had already
  moved with the corpus by the time it was written.
- **AC2** — When a fixture adds a bare fan-out assertion to a live carrier, `bash
  tools/check-agent-cap-restatement.test.sh` observes the gate naming it, and the line-count
  sentence in `skills/session-kickoff/SKILL.md` stays silent as the green control.
- **AC3** — When a live waiver row's matched text is gone, `bash
  tools/check-agent-cap-restatement.test.sh` observes the gate reding as stale; and when a frozen
  path prefix selects nothing, it reds the same way.
- **AC4** — When `bash tools/workflows/check-protocol-parity.test.sh` runs it is green; when a
  fixture protocol carries the rule as a bare paraphrase with NO pointer, the same harness
  observes it reding; and when a fixture names a conf key the hook does not read, it reds too.
  All three: the first proves the arm survived the rewrite, the other two prove it did not
  degrade into asserting that some backticked token is present.
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

RESOLVED (owner, 2026-08-18): the pointer and a new predicate.

- **Section 4's two options for the gate-held assertion.** RESOLVED (owner, 2026-08-18): option
  2 — the protocol carries a POINTER and no digit, and the parity leg gets a new anti-vacuity
  predicate. This OVERRULES the agent's recommendation of option 1, which was argued on cost.
  The owner's reading is the one this unit's own goal implies: a declared pair keeps the number
  correct in two places, and the point of the unit is for it to exist in one. S2b states what
  the replacement must assert, so the rebuild does not quietly weaken what it replaces.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-5 · 2026-08-18 · BUILT and status CLOSED. The scanner's noun list missed `≤5
  verify-stage agents TOTAL` on its first run here — the single line the parity gate froze, and the
  most important carrier in the corpus. Second miss in one unit; S10's warning is a measurement.
- rev-5 · 2026-08-18 · folded spec-audit round 2, which BLOCKED on this unit twice. The ratified
  predicate could not be satisfied at this unit's own landing commit, because its second half needs
  a conf key and a hook read that unit 4 mints later; the owner ratified SPLITTING IT BY LANDING
  and S2b now carries the pointer-shape half alone. S2c makes it per-rule, since the protocol
  states two bounds and §3 insists they stay two. S2d gives the code-shaped sites a stated
  disposition the scanner cannot supply. S5 was applied to a template that states the enforced rule
  rather than a shipped default, and S5b says the pair buys an adopter nothing. S6 gains the
  backlog prefix, which this build's own row would otherwise have tripped. S9 states the third
  constraint — the noun list — without which the pattern matches the line AC2 needs silent.
- rev-4 · 2026-08-18 · folded the gate measurement the owner ordered before any build. S9 fixes
  the two tightenings that take the false-positive rate from 64% to zero, S10 makes the gate
  declare the two blind spots the measurement exposed, section 4 carries the numbers, and AC1
  now names a figure to reproduce. The measurement also found stale prose in `tier2-review.js`
  that this unit's scope deliberately cannot see; filed rather than absorbed.
- rev-3 · 2026-08-18 · fork put to the owner and RESOLVED AGAINST the recommendation: the
  protocol loses the digit and the parity leg is rebuilt. S2 stops being a menu, S2b states what
  the new predicate must assert, section 4 is rewritten around the ratified path, and AC4 gains
  the three-part form that keeps the rebuilt arm from degrading into a spellcheck.
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
