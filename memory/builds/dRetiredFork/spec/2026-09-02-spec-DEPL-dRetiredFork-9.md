# DEPL-dRetiredFork-9 — the done-condition names the escape it depends on

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams deployer · order 0 · ratified 2026-09-02

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

PROMOTED from spec-audit round 2, blocker 2. Two criteria written in the same fold round, from two
different round-1 findings, cannot both be satisfied. `DEPL-dRetiredFork-3` AC10 calls itself the
build's done-condition, pins the argv `python tools/govkit/govkit.py update --target
C:/projects/nicocares/main --write`, and requires the run to re-stamp `gov_commit`.
`DEPL-dRetiredFork-1` AC6 accepts a non-zero `unattributed` row count so long as the ledger records
why it cannot fall.

Verified at HEAD: `tools/govkit/govkit.py:6566-6573` withholds that stamp whenever any row carries
`evidence: "unattributed"`, naming `govkit adopt --re-adopt --write` and `--allow-ungraded` as the
only two escapes. AC10's argv carries neither. DEPL-1 S6 states outright that nothing in the set
drives the population down — 32 rows at NicoCares, 30 at inCMS — and no unit scopes either escape.
**So the build can pass every unit and fail its own README, for a reason recorded in a sibling
spec.** This unit decides which escape the done-condition depends on and writes it into both.

## 2. Scope (IN)

- **S1** — Decide the fork in §8 and write the decision into `DEPL-dRetiredFork-3` AC10 IN ITS OWN
  TEXT, naming the flag or the preceding verb it depends on.
- **S2** — Write the SAME sentence into `DEPL-dRetiredFork-1` AC6, so the two agree in writing and
  neither can be read alone.
- **S3** — If the decision is that the count must reach zero, add the scope item that drives it —
  in `DEPL-dRetiredFork-1` or a new unit — because no unit carries one today, and an acceptance
  criterion with no scope item behind it is the shape this build keeps finding.
- **S4** — Record in the build README's Build-level rules that a criterion labelled as the build's
  done-condition is read against every other spec's §2 before the set closes. Round 2 called this
  the manual check that belongs in BUILD-METHOD; recording it here keeps it inside this build until
  someone promotes it upstream.
- **S5** — Both edits are wholesale rewrites of the criteria they touch.

## 3. Non-goals (OUT)

- Building the argv-flag lint the review proposes — resolving a pinned argv's flags against the
  program's own refusal paths. It is deep, and `TOOL-dRetiredFork-20`'s spec lint deliberately stops
  at tokens it can resolve against the tree.
- Driving the `unattributed` population to zero as an act of this unit. This unit decides and
  records; the work, if the decision demands it, is S3's placement.

## 4. Design

### Alternatives rejected

Leaving AC10 as written and treating `--allow-ungraded` as implied. The flag converts the build's
stated verdict into an override, and an override nobody wrote down is one the acceptance ledger
cannot report honestly.

Deleting AC10 and restating the README's done-condition as something the union already reaches. That
is available and it is worse: round 1's B1 established that the union reaches nothing at an adopter,
so the restatement would be a retreat dressed as a correction.

## 5. Production-readiness checklist

- security — N/A. A documentation decision about which flag an acceptance run carries.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the decision must be visible in BOTH criteria, which is S2's whole content; a
  decision recorded once is the shape that produced this blocker.
- risks — choosing `--allow-ungraded` makes the done-condition satisfiable while 31 rows stay
  frozen, which is a real weakening and must be stated as one rather than absorbed quietly.
- testing + left-shift gates — S4's documented manual check; no new leg.
- migration / rollback — text only.
- user docs — none; this is internal build state.

## 6. Acceptance criteria

- **AC1** — `DEPL-dRetiredFork-3` AC10 names the escape it depends on, and its pinned argv either
  carries that flag or is preceded by the verb that clears the condition.
- **AC2** — `DEPL-dRetiredFork-1` AC6 carries the same sentence, verified by a diff of the two
  criteria rather than by reading them separately.
- **AC3** — If the decision requires the count to reach zero, a scope item somewhere in the set
  drives it, named by id in this spec's §9 and present in
  `memory/builds/dRetiredFork/README.md`'s roster.
- **AC4** — `grep -n 'allow-ungraded\|re-adopt' memory/builds/dRetiredFork/spec/` returns a hit in
  both criteria or in neither, never in one.
- **AC5** — `bash tools/memory-tree/check-memory-hygiene.sh` exits `0` after the edits.

## 7. Gates

`memory hygiene` · `build README slot contract` · `build-index selftest`.

## 8. Open questions

- **F1 — does the done-condition require `unattributed` to reach ZERO, or is it observed with
  `--allow-ungraded`?** Zero is the honest reading of the README and needs a scope item nobody has
  written; `--allow-ungraded` is reachable today and makes the build's headline verdict an override.
  There is a third option worth pricing: run `govkit adopt --re-adopt --write` first, which clears
  the rows and, per `TOOL-dRetiredFork-12` F1, discards every other row's recorded base. **This is
  an OWNER TURN.** It decides what "the update runs centrally" means, and M3's veto 2 reserves a
  change to the build's own acceptance for the owner. Recommendation to put to them: zero at
  NicoCares, `--allow-ungraded` at inCMS until its receipt is repaired, both stated in AC10.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. PROMOTED from spec-audit round 2 blocker 2 under BUILD-METHOD
  M4's disposition rule. The withholding branch at `tools/govkit/govkit.py:6566-6573` and the two
  escapes it names were read at `b0108f13` rather than taken from the review.

## 10. Reuse audit

No existing seam fits: this unit decides a contract between two acceptance criteria and builds no
code. `python tools/codebase-map/reuse_lookup.py "resolve a document's backticked tokens against the
tree that owns them"` reports `resolve` (fan-in 25) and `owners_of` (fan-in 3) as the corpus's
resolution seams, and neither reaches a cross-document acceptance agreement, which is why S4 records
a manual check rather than proposing a gate.

Recall terms used: `gov_commit`, `unattributed`, `allow-ungraded`, `re-adopt`, `done-condition`,
`acceptance`, `receipt`, `evidence`, `withhold`, `adopter`, `rung`, `stamp`.
