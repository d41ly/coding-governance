# TOOL-dScaffoldedMirror-2 — honest reporting and per-predicate liveness

**Status:** CLOSED · rev-3 · 2026-08-25 · node d · Tier-1 · base 9ddcc5c9 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md](../build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md) | research | — |
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md](../build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md) | spec-audit | TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-13 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 |
| [2026-08-25-build-TOOL-dScaffoldedMirror-2.md](../build/2026-08-25-build-TOOL-dScaffoldedMirror-2.md) | journal | — |
| [2026-08-25-review-TOOL-dScaffoldedMirror-2-14-cumulative.md](../reviews/2026-08-25-review-TOOL-dScaffoldedMirror-2-14-cumulative.md) | diff-review | TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-14 |
| [2026-08-25-review-TOOL-dScaffoldedMirror-2-14-round-2.md](../reviews/2026-08-25-review-TOOL-dScaffoldedMirror-2-14-round-2.md) | diff-review | TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-14 |

<!-- /gen:spec-records -->

## 1. Goal

The lexicon gate cannot currently tell a reader whether it measured anything. It folds two
predicates' populations into one number, prints no count at all on green, and `--measure` reports
four distinct refusal conditions as `# NOTE:` comments while returning 0. Make every predicate report
its own graded population, and make an armed predicate with an empty population RED. This is the
cheapest correct thing in the whole build and it is a precondition for the rest: three later units
route through `--measure`, and every `[[hole]]` discharged by "run the checker" currently inherits a
checker that measures nothing.

## 2. Scope (IN)

- **S1** — split `populations` per PREDICATE rather than per extension. `lexicon.py:455` computes
  `populations[ext] = len(funcs) + len(types_)`; it becomes at least `funcs_per_ext` and
  `types_per_ext` plus a per-predicate roll-up, so P1's population and P2's population are separately
  observable for the same extension.
- **S2 — REPORT, not RED, and rev-2 corrects rev-1 here.** An extension declared `parser` or `probe`
  whose population for a given predicate is 0 is NAMED on every run as `graded=0`, and the run's
  verdict is unchanged. rev-1 made it a refusal; §4 records the two measurements that killed that.
  The extension-level `DEAD PROBE` RED stays exactly as it is today.
- **S3** — the green line reports counts. Every run prints `graded=<n> offenders=<n> waived=<n>` per
  predicate, on green as well as on red, so a green row is a measurement rather than a mood.
- **S4** — `measure_mode` stops returning 0 unconditionally (`lexicon.py:502-512`). When `problems` is
  non-empty it returns 1. The four conditions that currently ride as comments — UNDECLARED
  EXTENSIONS, DEAD PROBE, UNSELECTIVE LAYERS RULE, STALE WAIVERS — become the exit code they always
  described.
- **S5** — the kit README and `LEXICON.md` gain the per-predicate coverage statement, and the gate's
  own header states what it still does NOT check (§7's rule: a structural check reads as a semantic
  one to everybody who did not write it).

## 3. Non-goals (OUT)

- **No change to any predicate's semantics.** P1, P2 and P3 grade exactly the population they grade
  today; this unit changes what is REPORTED about that population and when the run refuses. A verdict
  change would make the unit's own before/after comparison unreadable.
- **No corpus scoping.** The kit still grades itself. rev-1 pointed at `TOOL-dScaffoldedMirror-3`
  for it; that unit is WONTDO as of 2026-08-24 and the non-goal now stands on its own reason —
  scoping moves the graded set, and this unit must hold it still or its own before/after comparison
  is unreadable.
- **No new predicate, no vocabulary change, no pin change.** Phases 2 through 4.
- **No coverage floor.** Reporting the graded fraction is `-6`; this unit reports per-predicate
  counts, which is a different number answering a different question.
- **`.ts`/`.tsx` stay undeclared.** `-13`.

## 4. Design

### Data model

`extract()` already returns `(functions, types, imports)` per file and the caller immediately
discards the distinction. The change is to stop discarding it:

```
populations[ext]            ->  populations[(ext, predicate)]
```

with `predicate` in `{"verb", "suffix", "layer"}` mapping to `functions`, `types` and `imports`
respectively. The existing `DEAD PROBE` scan at `lexicon.py:487-494` iterates declared langs and asks
`not populations.get(ext)`; it becomes a scan over the (ext, predicate) product, which is what makes
S2 fall out of S1 rather than needing its own machinery.

### The failing case is already in the tree

Measured 2026-08-24 on this worktree: **10 tracked `.js` files, 0 `class` definitions.** `.js` is
declared `js-regex:probe`, so it is ARMED, and P2 grades an empty set behind
`populations["js"] = 89` — the 89 being its function count. Today that run prints:

```
lexicon OK — 896 tracked file(s); coverage: .<none>=dark, … .js=probe, .py=parser, …
```

No offender count, no population, exit 0. After this unit it must print `DEAD PREDICATE` naming
`(.js, P2)` and exit 1. **This is the arm, and it needs no staged break** — which is rare enough in
this repo's history to be worth saying out loud, and is why this unit leads the build.

### The second arm, which the first does not buy

A refusal that can only be cleared by deleting the declaration is a refusal that will be cleared by
deleting the declaration. So the unit must also show that declaring the pair dark RESOLVES it and is
itself visible: after declaring js/types dark, the run goes green AND the coverage line names the
pair as dark. Without that arm S2 is a rule with one escape hatch and no record of its use.

### Alternatives rejected

- **Report per-extension counts without splitting per predicate.** Cheaper, and it does not answer
  the question: `.js`'s 89 is a real number that hides the zero. The fold is the defect.
- **Make `DEAD PREDICATE` a `# NOTE:` like its four siblings.** That is the defect this unit exists
  to remove, one level down.
- **Have `--measure` keep returning 0 and put the exit code on the gate only.** `--measure` is
  documented as "print the three pins THIS conf produces; decide nothing", and three later units call
  it as their discharge probe. A probe that cannot fail is not a probe.

### Files touched (estimate)

`tools/lexicon/lexicon.py` (~60 lines, concentrated in `main`'s population build and verdict loop),
`tools/lexicon/selftest.py` (the two arms plus a fixture per shipped pattern set),
`tools/lexicon/README.md` and `tools/lexicon/LEXICON.md` (S5). No conf grammar change, so
`lexicon_conf.py` and `subtokens.py` are untouched.

## 5. Production-readiness checklist

- **security** — N/A. No new input, no new write path, no execution of adopter-supplied values.
- **perf / scale** — zero added compute; the same populations are already computed and then summed.
  The check is 0.44 s warm on gov and ~8 s cold on a 6,168-file adopter, both unchanged.
- **a11y** — N/A, a CLI checker.
- **i18n** — N/A.
- **error / empty / loading states** — the empty state IS the subject: an empty population must be
  distinguishable from a satisfied one, which is the whole unit.
- **observability** — this unit IS the observability change. Counts on green; refusals as exit codes.
- **risks** — the one real risk is landing-day RED on this repo: `(.js, P2)` will red the moment S2
  arms, and the remediation (declare js/types dark, or ship a js class fixture) must land in the SAME
  commit or the bar is red on `main`. Rollback is deleting the kit's three legs, which is the
  standing opt-in property.
- **testing + left-shift gates** — both arms in `tools/lexicon/selftest.py`; the class is
  `memory/gotchas/vacuous-selector-empty-population.md`, which already exists and which this unit is
  a direct instance of.
- **migration / rollback** — none. No persisted artifact changes shape.
- **user docs** — S5. The kit README's coverage table gains the predicate axis.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py` runs on this worktree, its output names the
  `(.js, suffix)` pair with `graded=0`, so the empty population is legible instead of hidden behind
  the folded 89. The run's exit code is UNCHANGED from today's. rev-1 demanded a refusal here; §4
  records why that was wrong.
- **AC2** — When a tree's `.js` files gain a `class` definition, the same command reports a non-zero
  `graded` for `(.js, suffix)`, proving the count is derived rather than a constant. Staged in
  `tools/lexicon/selftest.py`, since this worktree has no JavaScript classes to add.
- **AC3** — When any run succeeds, stdout carries `graded=` , `offenders=` and `waived=` for each of
  the three predicates, on green as well as on red. Asserted by a selftest arm grepping the green
  output, not by reading it.
- **AC4** — When `python tools/lexicon/lexicon.py --measure` runs over a conf carrying an undeclared
  extension, it exits 1. Today it prints `# NOTE:` and exits 0; the arm stages an extension into the
  corpus and asserts the exit code moved.
- **AC5** — When `python tools/lexicon/selftest.py` runs, it covers AC1's REPORT and AC2's
  resolution, and a fixture that stops triggering either fails the suite rather than passing
  silently (`fixture-passes-by-finding-nothing`). rev-2 turned AC1 from a refusal into a report
  and this criterion still said "refusal"; rev-3 is that word, corrected.
- **AC6** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs after the change, it is unchanged
  in output and exit code — this unit does not touch the adoption path.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `memory hygiene`,
`kit version markers` (the `KIT_LEXICON_VERSION` and the two `gov:kit lexicon@` markers move
together). Adds no new gate leg — S2 is a new refusal inside an existing leg, which is deliberate:
the leg count is not the coverage.

## 8. Open questions

- **F1 — does `(.js, P2)` red on landing day, or does the unit ship the dark declaration with it?**
  RECOMMENDATION: ship the declaration in the same commit. The alternative is a red `main` for however
  long the follow-up takes, and this repo has a recorded instance of exactly that costing a second
  full-bar cycle. The dark declaration is honest — there are no JavaScript classes here — and AC2
  makes its use visible rather than silent. RESOLVED (agent, 2026-08-24, delegated): ship the
  declaration in the same commit, per the landing-day risk in §5.
- **F2 — should `DEAD PREDICATE` fire for P3 (imports) as well?** A file with definitions and no
  imports is ordinary, so the naive form would red constantly. RECOMMENDATION: no — P3's liveness is
  already carried by `UNSELECTIVE LAYERS RULE`, and the review measured that the better P3 liveness
  question is on the FROM side (does the FROM layer issue at least one import the resolver resolves to
  a tracked file — 38 issued, 7 resolve today). That is `-8`'s neighbourhood, not this unit's.
  RESOLVED (agent, 2026-08-24, delegated): P3 is out of scope here; the FROM-side assertion is filed
  against the canon unit.

### Why S2 is a report and not a refusal — two measurements

**A per-predicate refusal fires on an HONEST tree and has no discharge.** `.js` here is armed
(`js-regex:probe`) and carries **zero** `class` definitions across 10 tracked files. That is not an
extractor that went inert; it is a repo that does not write JavaScript classes, which is an ordinary
and permanent state. Under rev-1 the only way to clear it was to declare a `(extension, predicate)`
pair dark — and `LANGS` has no pair grammar, so the only reachable discharge was declaring all of
`.js` dark, which drops **45 real P1 offenders** and buys a green bar by deleting coverage. A refusal
whose only discharge is a coverage loss is a refusal that will be discharged that way.

**And the defect it was written for is already covered elsewhere.** Measured: `js-regex` DOES declare
a `types` extractor, so the pair is armed and simply empty. The case rev-1 wanted — a pattern set that
has gone inert — is caught by the frozen SENTINELS fixture in `tools/lexicon/selftest.py`, which
asserts every shipped pattern set still matches its own fixture. The corpus-side arm cannot separate
"inert" from "genuinely none" from one tree; the kit-side arm does not have to.

So the honest split is: the SENTINEL owns inertness, the extension-level `DEAD PROBE` owns "this
extension has files and no definitions at all", and this unit makes the per-predicate zero VISIBLE.
The original complaint — that a reader cannot tell this repo from one with zero findings — is answered
by printing the number, which is what S3 does.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on the `dScaffoldedMirror` research pass
  (`research/2026-08-24-research-lexicon-usefulness.md`, recommendation R1) and on the read-only
  adopter probe of `incms/main` taken the same day.
- rev-1 status 2026-08-24 · KEPT whole in the six-unit build, and the `LANGS` pair-level grammar widening is pulled INTO scope at rev-2. AC2's escape hatch needs that grammar; the only cheap alternative was declaring js dark, which is a 45-offender absorbing move with a green bar.

- rev-2 · 2026-08-25 · folded the spec-set review's B4 and the six-unit ruling. S2 becomes a REPORT:
  a per-predicate refusal fires on a tree that honestly has no JavaScript classes, and its only
  reachable discharge was declaring `.js` dark, which deletes 45 real P1 offenders to buy a green
  bar. §4 carries both measurements. That dissolves B4 rather than answering it — no pair-level
  `LANGS` grammar is needed, so this unit stays Tier-1 and touches no shared contract. AC1 and AC2
  are rewritten to assert the COUNT rather than a refusal. The §3 non-goal that pointed at
  `TOOL-dScaffoldedMirror-3` now stands on its own reason, that unit being WONTDO.

- rev-3 · 2026-08-25 · built and CLOSED. One correction: AC5 still said "AC1's refusal" after rev-2
  made AC1 a report — a spec disagreeing with itself one section apart, which is exactly what M2's
  sub-spec cross-read is for. No mechanism changed.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py population liveness dead probe reporting` returns
`population` (`tools/govkit/refusal_join.py`, fan-in 13, SEAM) and the gotcha class
`vacuous-selector-empty-population.md`. Neither is a seam this unit wires THROUGH — `refusal_join`'s
`population` enumerates declaration branches for a different kit and shares no shape with a
per-predicate definition count, and the gotcha class is the failure mode rather than a mechanism.
The reusable seam that DOES apply is internal: `lexicon.py`'s existing `DEAD PROBE` scan
(`:487-494`), which this unit generalises across the predicate axis rather than duplicating. No new
helper is introduced, which is the intended answer — the defect was a fold, and the repair is to stop
folding.
