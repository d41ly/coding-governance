# TOOL-dScriptedRepeat-14 — a build README asserting a mechanism its own spec set has since revised

**Status:** CLOSED · rev-4 · 2026-08-23 · node d · Tier-2 · base abd0f026 · streams tooling

## 1. Goal

Round 3's LOW 11: this build's README said `--counts` takes the recorded FACTS while spec 6 rev-8,
written in the same fold, said it takes a pinned BASE sha and re-parses the blob. Two answers to one
question about the guard on the one Definition-of-Done item that takes no override — and the README is
the file a session opens first. The instance was superseded in place. The class has no reader.

## 2. Scope (IN)

- **S1 — a drift-audit signal over the pair.** A build README and its spec set are two records of one
  build, and nothing compares them.
- **S2 — the predicate is a MECHANISM POINTER, not prose similarity.** A README line naming a shipped
  mechanism — a backticked flag, verb, conf key or function — where the spec set's LATEST revision for
  the unit that owns it names a different one. Anything vaguer fires on every paraphrase.
- **S3 — REPORT ONLY, on the `live_backlog_rows_per_shard` shape**: `"gateable": False`, and the
  threshold read as `"tolerance": ctx.pins.get(<name>, 0)`. Rev-1's F2 cited a `gateable: True`
  precedent, which contradicted this line and would have put an English-reading predicate on the
  unguarded `drift-audit records` merge-bar leg.
- **S4 — a LIVENESS assertion on the population that CAN go blind.** Not "did I find a build" — the
  tree always has builds — but "did I find a README line carrying a backticked mechanism token AND a
  spec revision log to compare it against". A signal whose liveness watches a population that cannot
  empty is a liveness assertion in name only.
- **S5 — the SHIP BAND, and it is an acceptance criterion rather than a sentence.** The predicate runs
  over every build in `memory/builds/`, recording hits AND near-misses per build. It ships only if it
  fires on at least one build OTHER than `dScriptedRepeat` and on no more than 25% of the corpus.
  Outside that band the fallback is REQUIRED, not optional.
- **S6 — the fallback, declared here rather than discovered.** Outside the band, the unit ships a
  fold-checklist item — every owner-ruling bullet naming a shipped mechanism is re-read against the
  code at fold time — and this spec's §9 records that the machine version was attempted and refused,
  with enough of the refused predicate written down that the next attempt does not repeat it.
- **S7 — the signal is declared in the shipped conf template's PINS.** An adopter absent from it falls
  back to tolerance 0, which is the failure `live_backlog_rows_per_shard`'s own comment warns trains a
  reader to ignore the line.

## 3. Non-goals (OUT)

- **Not a general prose-consistency checker.** One build's README against that build's own spec set.
- **Not blocking a merge.** See S3.
- **Not fixing the instance**, already superseded in round 4's fold.

## 4. Design

`signal_readme_mechanism_drift(ctx) -> dict` on the existing contract: `value`, `of`, `tolerance`,
`gateable: False`, `live`, `detail`.

The predicate: a README line containing a backticked token that also appears in a spec's revision log
at a revision LATER than the README's own last touch, where the README's sentence and that revision
entry make opposite claims about it. The last clause is the hard one and S5/S6 exist because it may
not survive contact with the corpus.

## 5. Production-readiness checklist

- **Security** — none.
- **Observability** — one row on the audit's table with the pair it found.
- **Perf** — the audit is seconds and no-agents by design. There is no declared time budget for it in
  the tree, so this unit MEASURES the before and after and records both rather than asserting against
  a budget that does not exist.
- **Migration** — additive; S7 keeps an adopter off tolerance 0.

## 6. Acceptance criteria

- **AC1** — a fixture build whose README names a mechanism its spec's later revision replaced is
  reported by `python tools/drift-audit/drift_report.py`, naming both files and both claims.
- **AC2** — a fixture build whose README and spec set agree is NOT reported by
  `python tools/drift-audit/drift_report.py`.
- **AC3** — the round-3 instance reproduces: `memory/builds/dScriptedRepeat/README.md` reconstructed at
  the pre-supersede revision fires the signal, and the current tree does not.
- **AC4** — the liveness is over S4's population: a corpus whose READMEs carry no backticked mechanism
  token reports DEAD PROBE from `python tools/drift-audit/drift_report.py`, not 0.
- **AC5** — the corpus run over `memory/builds/` lands INSIDE S5's band: at least one build other
  than `dScriptedRepeat` fires, and no more than 25% of builds do. Outside the band this AC FAILS and
  S6's fallback is the required outcome — the number is the test, not the writing-down of the number.
- **AC6** — `python tools/drift-audit/drift_report.py` wall readings before and after are both recorded
  in this build's bar-cost record. No budget is asserted, because none is declared in the tree.
- **AC7** — if S6's fallback is taken, this spec's `## 9. Revision log` says so BEFORE the checklist
  item lands in `memory/guides/BUILD-METHOD.md`, describing the refused predicate well enough that the
  next attempt does not repeat it.
- **AC8** — the signal's name appears in the PINS block of `tools/drift-audit/`'s shipped conf
  template, and an adopter conf lacking it is shown to read the declared default rather than 0.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, plus the drift-audit kit's own self-test.

## 8. Open questions

- **F1 — "later revision" against what clock?** RESOLVED (agent, 2026-08-23, delegated): the spec's own
  revision log, read as data. A git mtime moves when a typo is fixed.
- **F2 — tolerance zero, or a pin to drain?** RESOLVED (agent, 2026-08-23, delegated): a pin to drain,
  on the `live_backlog_rows_per_shard` shape — `gateable: False` with `ctx.pins.get(<name>, 0)`. Rev-1
  resolved this by citing a GATEABLE precedent, which contradicted S3; the audit caught it.
- **F3 — what if the band in S5 is met but the signal fires on the build whose incident motivated it
  and one unrelated build only?** RESOLVED (agent, 2026-08-23, delegated): that IS the band and it
  ships. Two independent hits is the minimum evidence that a predicate generalises; demanding more
  from a corpus this size would make the band unreachable and the fallback automatic.

## 9. Revision log

- rev-4 · 2026-08-23 · the round-7 fold. Four defects, all in the new signal, none of them able to red
  a merge — and one of them had already been baked into a shipped pin.
  **MEDIUM 1** — the two sides were dated on different clocks: `author-time` read as UTC against a
  hand-typed LOCAL date in the revision log. At +0300 every README line written between 00:00 and 03:00
  was backdated a day and fired on a same-day revision. 11 of 31 rows were pure artifacts. The blame
  side honours `author-tz` now and **the pin is re-seeded 31 -> 19**, with the reason beside it, because
  a pin measured through a broken instrument makes the later fix read as an improvement.
  **LOW 1** — one row per backtick OCCURRENCE, so a sentence naming a token twice counted twice while
  the pin's own comment said each row is one sentence to re-read. Deduped on `(line, token)`.
  **LOW 3** — `path.split("/")[2]` assumes `MEMORY_ROOT` is one segment; this repo's own manifest records
  `docs/mem` as a real adopter value, where the index lands on the literal `builds` and every README
  grades against every build. The slug is derived from the declared root now.
  **LOW 4** — `live` was computed from two populations gathered BEFORE the blame call, so a blind blame
  reported a clean `ok`. It watches the blame stage now. **Its arm is OWED and says so**: the only
  reproducing route is an unborn HEAD, and the report refuses to run at all on a repo with no commits,
  so no fixture in this harness reaches it. The counter is the fix; the arm is not written.
  Three arms for MEDIUM 1, LOW 1 and LOW 3, each observed RED against the pre-fold signal.
  Minted: `two-readers-of-one-config-one-re-derived` (from blocker 3, filed under unit 13).
  Band after the fold: **19 rows over 7 of 61 READMEs, 11%**, still inside S5's band with 6 builds other
  than this one.
- rev-3 · 2026-08-23 · CLOSED. The signal ships INSIDE S5's band and **AC3 is unreachable**, so
  S6's fallback ships beside it rather than instead of it. Both halves, with the numbers.

  **The signal.** `build_readme_mechanism_drift` in `tools/drift-audit/drift_report.py`, report-only
  on the `live_backlog_rows_per_shard` shape. Named `build_`, not `signal_` as §4 spelled it —
  `signal` is a noun and absent from `.lexicon.conf`'s VERBS table, so a ninth `signal_` would be a
  NEW offender against a pin that grandfathers exactly eight. The reason is already written above
  `build_live_backlog_rows`; §4 simply did not read it.

  **AC5's band, measured:** 31 rows over 8 of 60 build READMEs — **13%**, against a ceiling of 25% —
  and 7 of those 8 are builds other than `dScriptedRepeat`. Spot-checked: `aTetheredRecord`'s README
  says unit 2 ships `--print-bindings` while that unit's own revision log says the `--print-bindings`
  contract was AMENDED by unit 4. That is the class, found in a build nobody was looking at.

  **AC3 IS UNREACHABLE, and the reason is worth more than the criterion.** The motivating instance
  does not contain the same token twice. Reconstructed at `5b0d73c0`, the README says "**`--counts`
  takes the recorded FACTS**" and spec 6 contradicts it — while **never spelling `--counts`
  anywhere in the file**. `git show 5b0d73c0:…spec-dScriptedRepeat-6.md | grep -c -- '--counts'`
  returns 0. No predicate keyed on token identity can ever see that pair, whatever its clock does.
  Two variants were run over the whole corpus before concluding this: strict `revised > line_dated`
  fires on 13% and misses it; same-day-inclusive `>=` fires on **30%** — outside the band — and
  **still** misses it, because the miss is not about dates at all. Recorded at this length so the
  next attempt does not spend the corpus run again.

  **AC7's fallback therefore ships**, in `memory/guides/BUILD-METHOD.md` §M8 and its template: the
  build README is re-read against the code before the build closes, and the guide says in its own
  words that the signal covers only the token-identical subset and why.

  **AC8 shipped its first clause and not its second.** `readme_mechanism_drift` is declared in
  `tools/drift-audit/drift_signals.template.py`'s PINS. The second clause — an adopter without the
  key reading "the declared default rather than 0" — is not implementable and should not have been
  written: the kit cannot ship a measured number for a corpus it has never seen, and a guessed pin is
  the one thing that PINS block forbids by name. What ships instead is the key, commented, with the
  instruction to seed it from the adopter's own first report. This repo pins it at its own measured
  31.

  **Left-shifted after the build, from M8's own checklist:** the token join was a bare substring, so
  `--check` matched a revision naming only `--check-format` — this repo's `id-matched-as-a-substring`
  class. It requires the backticked form now, with an arm and an observed staged RED. The corpus reads
  identically either way, which is luck rather than equivalence.

  **AC6:** `python tools/drift-audit/drift_report.py` ran 4.00 s and 5.16 s before, 6.43 s and 6.50 s
  after — about +2 s, spent on `git blame` for the 8 READMEs that carry a candidate. No budget is
  asserted, because none is declared in the tree.
- rev-2 · 2026-08-23 · the round-1 spec audit's HIGH 5, HIGH 6 and two mediums. F2 now cites the
  report-only precedent it should have cited — rev-1's cited signal was `gateable: True`, which
  contradicted S3's own REPORT ONLY line and would have put this predicate on a merge-bar leg. S5's
  ship band becomes AC5 with numbers in it, because rev-1's only ship/no-ship rule lived in a §4
  sentence and the AC that appeared to test it was satisfied by writing any count down. S4's liveness
  moves off "did I find a build", which cannot empty, onto the token population that can. AC6 stops
  asserting a time budget that does not exist in the tree. S7 adds the PINS declaration.
- rev-1 · 2026-08-23 · drafted.

## 10. Reuse audit

`drift_report.py`'s signal contract, its liveness convention and its tolerance mechanism all exist;
`live_backlog_rows_per_shard` at `drift_report.py:811-826` is the shape this follows, verified by
reading it rather than by recalling it — which is what rev-1's F2 got wrong.
