**Serves:** spec TOOL-dPromptedSeam-4

# TOOL-dPromptedSeam-4 — the stopword parity is checked on demand, so a push can land drift

**Status:** DEFERRED · rev-1 · 2026-08-25 · node d · Tier-1 · base ee6554c3 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`lexicon.DEAD_TOKENS` restates `map_lib._STOPWORDS` because the layer ban forbids importing it, and
`TOOL-dPromptedSeam-3` added the arm that asserts the two are equal. That arm rides
`codebase-map kit selftest`, a `subject: kit` leg the runner HOLDS unless `GATE_SELFTESTS=1`, and
`.githooks/pre-push` sets `GATE_FULL` and not that. So the equality is real, checked, and NOT checked
at the boundary where drift would land. Close that, or record deliberately that it stays open.

Promoted from the closing diff review's round-2 H1 under M4's non-convergence rule.

## 2. Scope (IN)

- **S1 — decide WHERE the assertion runs**, between the options §8 Q1 states, and implement the one
  the owner picks.
- **S2 — make the chosen coverage legible** at `tools/lexicon/lexicon.py`'s `DEAD_TOKENS` comment,
  which currently says "gated on demand, not at the push boundary" — true today, and the sentence
  that must move if S1 moves it.

## 3. Non-goals (OUT)

- **No change to the assertion itself.** It exists, it reads both sets for real, and its failing case
  was observed. This unit is about WHEN it runs, never WHAT it checks.
- **No second parity implementation.** Whatever leg hosts it calls the one arm.
- **No flip of `codebase-map kit selftest` to `subject: repo`.** That is one of Q1's options and it
  is the one this run may not take alone; see §8.

## 4. Design

**D1 — the gap, exactly.** `run-gates.sh` holds every `subject: kit` leg unless `GATE_SELFTESTS=1`.
`.githooks/pre-push` sets `GATE_FULL=1`, which bypasses guards but does not un-hold kit legs. So a
commit that edits `DEAD_TOKENS` and pushes runs the bar without ever running the parity arm.
`TOOL-dPromptedSeam-3` widened the leg's guard to include `tools/lexicon/`, which makes the edit
SELECT the leg — necessary, and not sufficient, because selection does not defeat the hold.

**D2 — why this is not simply fixed here.** The obvious repair, flipping that leg to `subject: repo`,
runs the whole `codebase-map` selftest on every bar and contradicts the standing owner ruling of
2026-08-23 that a kit's self-tests are not merge-bar legs. M3's veto 2 makes a governance-carrier
change an owner turn, so the run parks rather than picking. The other repair, a dedicated
repo-subject leg, is cheap to run and costs four carriers to declare — the leg row, a script, a
`[[gate_leg]]` claim and the map dossier — for one set comparison.

## 5. Production-readiness checklist

- **security** / **perf / scale** / **a11y** / **i18n** — N/A. One frozenset comparison.
- **error / empty / loading states** — N/A.
- **observability** — the arm already prints its verdict either way.
- **risks** — the risk is the one this unit names: drift lands, and the next reader of either set
  believes a check is watching. §5 of `-3` and the `DEAD_TOKENS` comment both now say on-demand.
- **testing + left-shift gates** — the arm exists; this unit only moves where it runs.
- **migration / rollback** — none.
- **user docs** — none; this is gate wiring.

## 6. Acceptance criteria

- **AC1** — When the option Q1 selects is implemented, removing one word from `DEAD_TOKENS` and
  running `bash tools/run-gates/run-gates.sh` with NO extra environment reds, naming the drift.
  Today that command is green on the same break, which is the whole defect.
- **AC2** — When `bash tools/run-gates/run-gates.sh` runs on an unmodified tree, it stays green and
  its wall time is not measurably worse — the cost of whichever host is chosen is paid and named.
- **AC3** — When `tools/lexicon/lexicon.py`'s `DEAD_TOKENS` comment is read after S1, it describes
  the coverage that then exists rather than the coverage that exists today.

## 7. Gates

Whichever leg S1 selects, plus `run-gates canary` if a leg row is added. No leg is added by this
spec; the spec is the decision record.

## 8. Open questions

- **Q1 — where does the assertion run?** PARKED for the owner, not resolvable under this mandate.
  Three options, and the vetoes are why the run cannot pick. **(a)** Flip `codebase-map kit selftest`
  to `subject: repo` — smallest diff, contradicts the 2026-08-23 ruling that kit self-tests stay off
  the bar, so M3 veto 2. **(b)** A dedicated repo-subject leg calling just the parity check — correct
  and honest, costs four declaration carriers for one comparison, and adds a moving part to the
  surface the govkit population gate grades. **(c)** Accept on-demand coverage and stop there — free,
  and it is arguably right: the arm is a kit self-test by nature, the guard now selects it, and the
  comment already says on demand. The run's own lean is **(c)**, because the drift requires someone
  to edit one of two restated sets and the comment now tells them what is and is not watching.

## 9. Revision log

- rev-1 · 2026-08-25 · node d · DEFERRED. Promoted from the closing diff review's round-2 H1 when the
  loop exited NON-CONVERGENT. Specced rather than built because its only open question resolves to a
  governance-carrier change, which M3 veto 2 places outside the standing mandate. DEFERRED and parked
  is the honest terminal for a unit whose decision is not the run's to take; `--close` owes an
  override naming it.

## 10. Reuse audit

- The parity arm in `tools/codebase-map/selftest.py` — the SUBJECT of this unit, not re-implemented.
- `tools/gate-legs.json` and `run-gates.sh`'s hold rule — READ, and the mechanism Q1's options act on.
- No probe was run for this unit beyond the closing review that produced it: it is a promotion of a
  finding, and the finding names its own site. `-3`'s recall terms cover the area.
