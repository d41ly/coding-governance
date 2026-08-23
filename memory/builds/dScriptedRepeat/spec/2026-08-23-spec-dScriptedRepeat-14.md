# TOOL-dScriptedRepeat-14 — a build README asserting a mechanism its own spec set has since revised

**Status:** SPECCED · rev-1 · 2026-08-23 · node d · Tier-2 · base abd0f026 · streams tooling

## 1. Goal

Round 3's LOW 11: this build's README said `--counts` takes the recorded FACTS while spec 6 rev-8,
written in the same fold, said it takes a pinned BASE sha and re-parses the blob. Two answers to one
question about the guard on the one Definition-of-Done item that takes no override — and the README is
the file a session opens first. The instance was superseded in place. The class has no reader.

## 2. Scope (IN)

- **S1 — a drift-audit signal over the pair.** The audit's job is exactly this question: does this
  repo's RECORD of its own state still describe it. A build README and its spec set are two records of
  one build, and nothing compares them.
- **S2 — the predicate is a MECHANISM POINTER, not prose similarity.** A README sentence naming a
  shipped mechanism — a flag, a verb, a conf key, a function — where the spec set's LATEST revision
  for the unit that owns it names a different one. Anything vaguer fires on every paraphrase and is
  worth less than nothing, because a signal nobody trusts is one nobody reads.
- **S3 — REPORT ONLY, with a tolerance, like every other signal in that tool.** The audit reports and
  the owner drains. A hard gate over English would be the "gate satisfied by its own comment prose"
  shape this build filed six times.
- **S4 — a LIVENESS assertion, per the audit's own contract.** Every signal there carries one, so a
  probe that cannot move prints DEAD PROBE rather than a reassuring zero. This one's liveness is that
  it found at least one README/spec pair to compare at all.
- **S5 — the honest fallback is declared IN the spec, not discovered during the build.** If S2's
  predicate cannot be made precise enough on this corpus, the unit ships the fold-checklist item
  instead — every owner-ruling bullet naming a shipped mechanism is re-read against the code at fold
  time — and says in the record that the machine version was attempted and refused. A documented check
  is a legitimate outcome; a vague gate is not.

## 3. Non-goals (OUT)

- **Not a general prose-consistency checker.** The population is a build README's mechanism claims
  against that build's own spec set. Not across builds, not against the code, not against the charter.
- **Not blocking a merge.** See S3.
- **Not fixing the instance.** Already superseded in round 4's fold.

## 4. Design

The audit's signals are `signal_*(ctx) -> dict` returning a value, a population and a status, and the
runner renders them in one table with a tolerance per signal. This adds `signal_readme_mechanism_drift`
on that contract.

The tightest predicate available on this corpus: a README line containing a backticked token that also
appears in a spec's revision log at a revision LATER than the README's own last touch, where the
README's sentence and that revision entry make opposite claims about it. The last clause is the hard
one and is what S5 exists for.

**Measured before wiring, per §7** — run the candidate over every build in the tree and print hits AND
near-misses. A predicate that fires on `dScriptedRepeat` alone is tuned to one incident; one that
fires on every build is noise. Neither ships.

## 5. Production-readiness checklist

- **Security** — none.
- **Observability** — one row in the audit's table, with the pair it found, per its existing shape.
- **Perf** — the audit is seconds and no-agents by design; this must not change that. A signal reading
  every spec of every build is bounded by the corpus, and the reading is reported.
- **Migration** — a new signal is additive; a repo with no builds gets a DEAD PROBE row, which is the
  correct answer rather than a zero.

## 6. Acceptance criteria

- **AC1** — a fixture build whose README names a mechanism its spec's later revision replaced is
  reported by `python tools/drift-audit/drift_report.py`, naming both files and both claims.
- **AC2** — a fixture build whose README and spec set agree is NOT reported by
  `python tools/drift-audit/drift_report.py`. Measured over the real corpus too: the false-positive
  count is written into the record whatever it is.
- **AC3** — the round-3 instance reproduces: reconstructing `memory/builds/dScriptedRepeat/README.md`
  at the pre-supersede revision fires this signal, and the current tree does not.
- **AC4** — with no build folder present, `python tools/drift-audit/drift_report.py` reports this
  signal as DEAD PROBE, not 0.
- **AC5** — `python tools/drift-audit/drift_report.py` stays under its own time budget, and the
  reading is recorded in this build's bar-cost record.
- **AC6** — if S5's fallback is taken, this spec's `## 9. Revision log` says so BEFORE the checklist
  item is written, and the refused predicate is described well enough that the next attempt does not
  repeat it.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, plus the drift-audit kit's own self-test.

## 8. Open questions

- **F1 — "later revision" against what clock: the README's git mtime, or a revision number in the
  spec?** RESOLVED (agent, 2026-08-23, delegated): the spec's own revision log, read as data. A git
  mtime moves when a typo is fixed and would call every build drifted the day someone reformats a
  README.
- **F2 — is the tolerance zero, or a pin to drain?** RESOLVED (agent, 2026-08-23, delegated): a pin to
  drain, matching `non_terminal_specs_cited_by_product_source` and its siblings. A new signal at zero
  tolerance reds the audit on day one over a corpus nobody has drained yet, and the audit is
  report-only precisely so that is not a crisis.

## 9. Revision log

- rev-1 · 2026-08-23 · drafted. S5 is written in deliberately: this predicate may not survive contact
  with the corpus, and a spec that has not said what happens then is a spec that will quietly ship a
  vague gate rather than admit the refusal.

## 10. Reuse audit

`drift_report.py`'s signal contract, its liveness convention and its tolerance mechanism all exist.
`gotchas.py`'s record-parsing shows how this repo reads front matter and bodies as data. Nothing new.
