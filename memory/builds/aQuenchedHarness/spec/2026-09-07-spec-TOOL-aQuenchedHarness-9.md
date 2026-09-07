# TOOL-aQuenchedHarness-9 — the held suites that are red, and have been for nobody knows how long

**Status:** DEFERRED · rev-1 · 2026-09-07 · node a · Tier-2 · base faaea5f5 · streams tooling · order 9

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Bring the RED self-test suites back to green, and leave behind a signal that says when one goes red
rather than leaving it to the next build that happens to need its seconds. This unit is DEFERRED: it
was DISCOVERED by `TOOL-aQuenchedHarness-6` while measuring, it is not what this build set out to do,
and folding it in would have replaced a measured cost reduction with an unbounded repair job.

## 2. Scope (IN)

- **S1** — the population is the DECLARED one, `tools/run-gates/selftest-budgets.txt`, run through
  `bash tools/run-gates/run-selftests.sh`. Every row that reds is in scope; a row that reds only on a
  contended box is re-run on a quiet one before it counts.
- **S2** — each red suite is diagnosed to a NAMED cause and either fixed or recorded as WONTFIX with
  the reason, per suite. "The suite is old" is not a cause.
- **S3** — the five reds already measured are the starting set, and each is named here with what was
  observed, so the unit does not begin by re-deriving what this build already paid for.
- **S4** — a signal that a HELD suite has gone red. The whole reason nobody can date these failures
  is that the hold removed them from the bar and put nothing in their place, and
  `tools/run-gates/run-selftests.sh` only reports when a person runs it. Whatever this is, it must
  not put the suites back on the merge bar — that is the 2026-08-23 owner ruling, and it stands.
- **S5** — every fix carries its own failing case observed, per charter §7. These suites exist to
  catch a staged break; a repair that makes one green without anybody seeing it red is the shape the
  whole family is here to prevent.

## 3. Non-goals (OUT)

- Not putting the held suites back on the merge bar. The ruling that removed them is not reversed
  here, and S4 exists precisely because reversing it is the wrong answer to the visibility problem.
- Not porting any suite onto `tools/lib/lib-selftest.sh`. That is `TOOL-aQuenchedHarness-6` and its
  follow-up; a repair and a rebuild in one pass makes a failed diff ambiguous between them.
- Not changing any checker to make its test pass. The suites are the subject; the checkers are not.

## 4. Design

### What was actually observed, and where

Measured on node `a`, 2026-09-07, running the unattended kit's six suites on a FROZEN CLONE at
`c63e4177` under `run-unattended-gates.sh`, while another session held the box. Recorded in
`memory/builds/aQuenchedHarness/build/2026-09-07-build-TOOL-aQuenchedHarness-6-portability-survey.md`
and in this build's parked decisions.

| suite | seconds | declared | verdict |
|---|---|---|---|
| `unattended gate selftest` | 9067 | 3800 | RED, and 2.4x over budget |
| `unattended driver selftest` | 2569 | 970 | RED, and 2.6x over budget |
| `unattended cross-component` | 339 | 300 | RED, and over budget |
| `unattended adopter e2e` | 38 | 120 | RED |
| `unattended playbook selftest` | 418 | 300 | green, over budget |
| `unattended pass-order selftest` | 111 | 600 | green |

**Four of six are red, and every one of them is red at BASE `faaea5f5` too** — verified directly for
the adopter e2e, and by the same argument for the rest: this build changed nothing under
`tools/unattended/` except that kit's `kit.toml` file roles. The two green ones are the two that were
recently rebuilt or are small.

Causes diagnosed so far, each from the suite's own output:

- **`cross-component`** — its fixture's hand-kept `cp` list never grew the verb carrier when
  `TOOL-dFoldedVerdict-5` split `VERBS.template.md` out of the protocol. So checks 10 and 26 fire on
  the FIXTURE, and every arm downstream grades that refusal instead of its own subject. This is the
  `fixture-fails-by-finding-the-wrong-thing` shape the suite's own header warns about, arriving in
  the suite that warns about it. Likely a two-line fix.
- **`driver selftest`** — three `--brief` argument-validation arms expect a refusal naming the forged
  field, and the driver refuses EARLIER with check 49, because the unit is not in the README's
  generated units region. The arms grade the wrong refusal. Either the fixture gives the unit a real
  row, or the arms move to a subject that reaches the intended check.
- **`adopter e2e`** — arms 3b and 4 fail with the rendered `.claude/skills/unattended/SKILL.md`
  absent from the adopting tree. Not diagnosed further.
- **`gate selftest`** — not diagnosed. At 9067 s it is a quarter of the entire declared population
  and is the test of the longest leg on the bar, which is why `TOOL-aQuenchedHarness-7` exists.
- **`govkit selftest`** — the ORIGINAL instance, recorded before this build: two arms red for long
  enough that nobody can say when they broke. Still unverified after this build's `[[exempt_leg]]`
  changes.

### Why S4 is the load-bearing item

The repairs are ordinary work. What makes this unit worth specifying is that **the same thing will
happen again**, and the mechanism is already visible: a suite left the bar in 2026-08, nothing
replaced the signal, and the failures were found in 2026-09 by a build that wanted the SECONDS and
read the verdicts by accident. That is not a discovery process; it is luck.

Candidate shapes, none chosen here: a periodic run whose result is recorded in the tree and whose
STALENESS is what the bar checks (so the bar asserts a fresh verdict exists, not that the suites
pass); a `--since` verdict file `run-selftests.sh` writes and a leg reads; a drift-audit signal, since
`tools/drift-audit/` already exists to answer "does this repo's record still match reality" and this
is exactly that question. The last is the cheapest and is where the reuse audit points.

### Ordering

Diagnose before repairing, and repair the cheap ones first — `cross-component` and `driver` both have
named causes and neither is a redesign. `gate selftest` is last and may be blocked behind
`TOOL-aQuenchedHarness-7`, because a rebuilt checker changes what its suite must assert.

### Alternatives rejected

Folding this into `TOOL-aQuenchedHarness-6` was rejected while the build was live: that unit's job is
a measured cost reduction with a diffable safety property, and an unbounded repair job attached to it
would have made both unfalsifiable. Recording the reds and deferring is what `BUILD-METHOD.md` M10
asks for when a discovery is real but is not this build's.

## 5. Production-readiness checklist

- **security** — none. These suites read and write scratch trees under `mktemp -d`.
- **perf/scale** — directly in scope: four of the six reds are also over budget, and two are over by
  more than 2x. A repair that leaves a suite red-adjacent at 9067 s has fixed the wrong thing.
- **a11y / i18n** — not applicable.
- **error/empty/loading states** — S5 covers it: every repair observes its own failing case.
- **observability** — S4 IS the observability item, and it is the unit's centre.
- **testing/gates** — the suites ARE the tests. The gate question is S4's.
- **migration/rollback** — none; no data or contract moves.
- **help/ docs** — none; no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-selftests.sh` runs on a quiet box at close, it reports
  GREEN, or every remaining red row is named in the wrap-up with a recorded WONTFIX reason.
- **AC2** — When each repaired suite's fix is landed, its failing case has been OBSERVED — the break
  staged, the suite RED, the break removed — and that observation is recorded per suite in a
  `memory/builds/aQuenchedHarness/build/` record naming the staged break and the suite's exit status.
- **AC3** — When a held suite has been red for longer than the declared staleness bound, the signal
  S4 builds REPORTS it, and `bash tools/run-gates/run-gates.sh` still runs no held suite — both
  observed on one tree, because a signal that reports by putting the suites back is the answer this
  unit is forbidden to give.
- **AC4** — When the repairs are done, every repaired row's fourth column in
  `tools/run-gates/selftest-budgets.txt` carries a fresh reading with its condition, and
  `bash tools/run-gates/run-selftests.sh --rank` ranks it rather than refusing it as unbacked.

## 7. Gates

`bash tools/run-gates/run-selftests.sh` on a quiet box · `bash tools/run-gates/run-selftests.sh
--check` · the memory hygiene leg for the records this unit writes · whatever leg S4 produces, with
its own failing case observed.

## 8. Open questions

- **F1 — what shape does S4 take?** OPEN. Three candidates are named in §4 and the reuse audit points
  at the drift-audit kit; none is chosen, because choosing it is a design pass this unit has not had.
- **F2 — is `gate selftest` repairable before `TOOL-aQuenchedHarness-7`, or blocked behind it?** OPEN.
  It is the test of the checker unit 7 rebuilds, so a repair now may be work thrown away.
- **F3 — are the four reds four defects or one?** OPEN. Two have unrelated named causes, which argues
  four; but all four are in one kit that left the bar on one date, which argues the cause is the
  visibility gap and the four are symptoms.

## 9. Revision log

- rev-1 · 2026-09-07 · written by `TOOL-aQuenchedHarness-6` as the disposition of four parked
  decisions, so a cited id stops being an orphan and the owner gets a scoped unit rather than four
  parked lines. DEFERRED from birth: the findings are measured, the repair is not this build's.

## 10. Reuse audit

**Probe result.** `python tools/codebase-map/reuse_lookup.py "held selftest verdict staleness signal"`
over 751 symbols and 19 affordance seams returned NO seam for S4's signal — its top candidates are
`derive_layer_verdict` and `read_gate_verdicts`, both fan-in 1, which is the tool's own way of saying
a name appears and nothing shares it. So there is no verdict-staleness seam to extend, and the
probe's honest answer for that half is that no existing seam fits.

What the probe does NOT see is the layer it declares unscanned — `.sh` — and the seam that matters is
there. `tools/drift-audit/` already exists to answer "does this repo's RECORD of its own
state still match reality", already carries a liveness assertion per signal so a probe that cannot
move prints DEAD PROBE, and already runs as a merge-bar leg (`drift-audit records`). A signal there —
"held suites whose last recorded verdict is older than N days, or absent" — reuses the whole
mechanism including its pin discipline and its report. That is the seam, and S4 should extend it
rather than author a fourth reporting shape. The alternative seams were checked and rejected:
`run-selftests.sh` itself cannot be the signal, because nothing runs it; and a bar leg that runs the
suites is the ruling this unit is forbidden to reverse.

**Recall terms.** `python tools/memory-recall/query.py "how does this repo notice that a check it no
longer runs has gone red" --terms "held leg selftest hold predicate owner ruling staleness bound
recorded green drift signal liveness assertion compensating check"` — the question this unit's S4
answers, in this corpus's own jargon.
