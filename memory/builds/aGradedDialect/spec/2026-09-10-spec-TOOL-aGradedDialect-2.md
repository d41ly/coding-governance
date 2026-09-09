# TOOL-aGradedDialect-2 — the conformance corpus: fixtures a compiler extracted, frozen before the reader exists

**Status:** SPECCED · rev-4 · 2026-09-10 · node a · Tier-2 · base d1357673 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-prompt-TOOL-aGradedDialect-1-spec-brief.md](../prompts/2026-09-10-prompt-TOOL-aGradedDialect-1-spec-brief.md) | journal | TOOL-aGradedDialect-1 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round1.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round1.md) | spec-audit | TOOL-aGradedDialect-1 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round2.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round2.md) | spec-audit | TOOL-aGradedDialect-1 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round3.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round3.md) | spec-audit | TOOL-aGradedDialect-1 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5 |

<!-- /gen:spec-records -->

## 1. Goal

Freeze a definition-site corpus for TypeScript whose inputs are drawn mechanically from real adopter
files and whose expectations are produced by `typescript@5.9.3`, so that `TOOL-aGradedDialect-3`'s
reader is graded by something it did not write and could not have influenced. Declare, in the same
unit, the FLOOR that reader must clear before it may call itself `parser`.

## 2. Scope (IN)

- **S1** — the extraction procedure: how a candidate excerpt is selected from the adopter tree by a
  deterministic rule, how it is widened until the oracle parses it standalone, and how the oracle's
  reading of the COMMITTED bytes becomes that record's expectation. Observed by **AC1** and **AC3**.
- **S2** — the on-disk format: one JSON record per fixture, carrying the excerpt, the oracle's
  functions and types, the construct tags, and the provenance triple. Observed by **AC1**.
- **S3** — the committed sample itself, bounded in size and stratified by construct, so the corpus
  CONTAINS the readings that break a same-line regex rather than only the ones that do not.
  Observed by **AC2**.
- **S4** — the FLOOR: what agreement with the oracle a reader must reach to declare `parser`, what
  refusal budget it may spend getting there, and why each number is what it is. The constants being
  READABLE is observed by **AC4**; the refusal budget being ENFORCED is observed by **AC6**, and the
  two are separate criteria because a ceiling nothing compares against is a number, not a budget.
- **S5** — the conformance runner and its arms in `tools/lexicon/selftest.py`, including the
  liveness case that proves the runner can FAIL: the shipped `js-regex` set scored against this
  corpus must miss the floor. Observed by **AC5** and **AC4**.

## 3. Non-goals (OUT)

- **No extractor.** The reader is `TOOL-aGradedDialect-3`'s. This unit lands with its conformance
  arm announcing a skip, and that unit's acceptance is what removes the skip.
- **No declaration change.** `KNOWN_EXTS`, `LANGS` and the cell matrix are `TOOL-aGradedDialect-4`'s.
  Nothing here adds a `ts` or `tsx` row anywhere, and the format is chosen so that nothing here has
  to: the excerpts are JSON string values, so this repo's tracked corpus gains no TypeScript file
  and no undeclared extension.
- **No import grading.** The oracle collects functions and types. Imports are excluded from the
  floor because the predicate that read them, `P3 layer`, was deleted by `TOOL-aSurfacedLexicon-2`,
  and a floor over a value nothing consumes is ceremony. Verified against source on 2026-09-10:
  `tools/lexicon/LEXICON.md` records the deletion and the kit README carries its epitaph.
- **No whole adopter files, and no vendoring beyond a definition site.** An excerpt is the smallest
  span that parses standalone and reproduces its construct, capped per record. The corpus is
  withheld from `govkit apply` for the same reason the self-tests are.
- **No reproduction of `regex_vs_oracle.py`.** It is not needed here: `TOOL-aGradedDialect-1`'s
  record now carries that script's full source in its own §6, folded at rev-2 on 2026-09-10 as
  round 1's first blocker, and the forward-pointer that used to aim at this spec's §4 is gone. An
  earlier revision of this bullet called that pointer a defect and booked a follow-up for the closing
  fold; both are discharged, and the follow-up is deleted rather than left to be chased.

### Edges

- **consumes-from** `TOOL-aGradedDialect-1` — the oracle script `ts-oracle.js`, reproduced runnable
  in that unit's record §6, and the construct census in its §4.2 that ranks this corpus's strata.
  Without it there is no independent expectation and no evidence for the minima.
- **consumes-from** external — `typescript@5.9.3` and a Node runtime, present in the adopter tree at
  `C:/projects/incms/main` as a dev dependency. Both are used ONCE, offline, at extraction time.
  Nothing this unit commits imports either, and the gate never runs them.
- **hands-off** `TOOL-aGradedDialect-3` — the frozen corpus, the runner that scores a reading
  against it, the declared floor, and the skipping arm that unit flips live.
- **hands-off** `TOOL-aGradedDialect-4` — the declared FLOOR, which is what decides the coverage mode
  that unit's S1 transcribes: `parser` at or above it, `probe` below it. Without the floor there is no
  verdict for that unit to read. The per-record `kind` and JSX construct tags go with it, but as
  secondary evidence only — that unit's §8 F1 is resolved on `TOOL-aGradedDialect-1`'s casing census
  instead, and the tags are what a later role-derived selector would restart from.

## 4. Design

### Data model

One file, `tools/lexicon/ts-conformance-fixtures.json`, holding a JSON array formatted at one record
per line so a review reads which record moved. `.json` rather than `.jsonl` because `json::dark` is
already declared in this repo's `.lexicon.conf` and `jsonl` is not — an undeclared extension present
in the corpus is a named refusal, so a new suffix would red the `lexicon naming predicates` leg for
no gain. A `.gitattributes` row pins it `text eol=lf` beside the existing `tools/gate-legs.json` row.

| field | holds |
|---|---|
| `id` | `<kind>-<construct>-<nnn>`, unique across the corpus |
| `kind` | `ts` or `tsx` — the oracle's `ScriptKind`, and what a reader must be told |
| `src` | the excerpt, verbatim, as a JSON string |
| `funcs` | the oracle's function and method definitions, `[name, line]`, line 1-based within `src` |
| `types` | the oracle's class, interface, type-alias and enum definitions, same shape |
| `constructs` | the census tags this record carries, from §4.2 of unit 1's record |
| `from` | `{path, blob, lines}` — the adopter path, its 40-hex blob sha, and the line range taken |
| `oracle` | the oracle's package and version, `typescript@5.9.3` |
| `extracted` | the extraction date |

`funcs` and `types` are the oracle's reading of the COMMITTED bytes, not of the original file. That
is what makes an excerpt safe to bound: a span that changes meaning when it is cut is rejected by
the oracle rather than silently mis-expected, and the line numbers a reader is graded on are the
ones a reader can actually see.

### The extraction procedure

Run once, offline, on node `a`, against a read-only checkout. It is a procedure rather than a
committed program: the only piece that does not already exist is the selector, and the expectation
half is unit 1's `ts-oracle.js` unchanged.

1. For each construct in §4.2's rank order, list the adopter files carrying it, sorted by path. The
   sort is what makes the draw reproducible; nothing is chosen by eye.
2. Walk that list on a fixed stride sized to the construct's minimum, and at each file take the
   definition site nearest the construct's first occurrence.
3. Widen the span to the smallest enclosing top-level statement and run the oracle over the span
   alone. Accept it when the oracle reports no syntax diagnostic and returns at least one
   definition; otherwise take the next candidate on the stride and RECORD the rejection with its
   reason, so a construct that could not be sampled is visible rather than absent.
4. Cap each accepted span at 60 lines. A site needing more context than that is not a fixture, it
   is a file, and it is skipped with its reason recorded.
5. Write the record with the oracle's reading of the accepted span, its construct tags, and its
   provenance triple.

### The sample, and why its minima are counts rather than shares

The corpus holds between 100 and 150 records, of which at least 40 are `kind: tsx`. Per-construct
minima, in the rank order §4.2 measured:

| construct | minimum records |
|---|---|
| template literal | 30 |
| JSX element | 25 |
| generic call or declaration | 20 |
| nested template expression | 15 |
| regex literal | 10 |

Records overlap — one excerpt commonly carries three of these — so the minima do not sum to the
corpus size. **The §4.2 shares are the ORDER of this table and deliberately not its values.** Those
shares were measured per FILE over 1257 whole files; a 60-line excerpt is far less likely to carry a
given construct than a whole file is, so demanding that 90.3% of excerpts hold a template literal
would select template-heavy code and distort the sample toward one reading. The counts are PINNED
policy with that reason; the shares they are ordered by are unit 1's measurement and are cited, not
restated.

`satisfies`, decorators and overload signatures get no minimum. Unit 1 measured them at 2.9%, 0.1%
and 0.0% of files, and a mechanical draw over a corpus with zero sites cannot produce a fixture. A
construct the draw could not reach is RECORDED as absent with its measured share, and a reader's
refusal of it is then unobservable and is declared unobservable rather than assumed clean.

### The floor

Three parts, all of them declared here and none inherited.

**F1 — exact agreement.** Over every record, the reader's `(name, line)` multiset equals the
oracle's, for `funcs` and for `types`. Not a percentage. The kit's own mode table defines `parser`
as complete over its extension, so any threshold under exact agreement cannot tell a complete reader
from an incomplete one, and any threshold is a number somebody chose.

**F2 — the refusal budget.** A reader may exclude a construct only by naming it in its own header
refusal list, and every named construct must be represented by at least one fixture the reader
RAISES on. The named refusals may cover at most 2% of the corpus's oracle definition sites.
2% is a PINNED policy ceiling, not a measurement: unit 1 measured the constructs a locator genuinely
cannot name at a fraction of one percent, and the oracle already drops computed method keys before
they reach a record, so 2% is an order of magnitude of headroom rather than a licence. Without a
budget F1 is reachable by refusing everything, which is the `fixture-passes-by-finding-nothing`
class one level up.

**F3 — composition.** F1 and F2 are vacuous unless the corpus contains the hard readings, so the
minima above are asserted by the same arm that scores the reader, on every run.

A reader that clears all three may declare `parser`. A reader that does not declares `probe` and
reports incomplete every run. Both outcomes are acceptable; the label over the wrong reading is not.

### The runner, and the proof that it can fail

`selftest.py` gains a loader, the floor constants, and three arms. The runner scores a reading by
calling `extract_text` with a mode and an extractor id, comparing per record, and reporting each
disagreeing record's id with both sides.

The arm that grades the TypeScript reader announces `SKIPPED — no TypeScript extractor declared`
while `PARSERS` and the resolved pattern sets hold no TypeScript entry, naming the arm and the
reason. A skip that looks like a pass is indistinguishable from coverage, so the skip is printed
rather than implied, and `TOOL-aGradedDialect-3` removing it is that unit's business.

The failing case is observed on the day this lands, without the extractor: the shipped `js-regex`
set is scored against this corpus and must MISS the floor. Unit 1 measured that set at 0.6% type
recall against TypeScript, so it fails F1 by a wide margin, and the arm asserting that failure is
what proves the runner is capable of red. A gate whose failing case has never been observed is an
assertion about nothing.

### Freezing, and what nothing checks

The corpus is committed in a pass that PRECEDES the first commit touching the TypeScript extractor.
That ordering is the whole answer to `TOOL-dScaffoldedMirror-13`'s tautology objection, and it is
checkable after the fact:

```bash
corpus_sha=$(git log --diff-filter=A --format=%H -- tools/lexicon/ts-conformance-fixtures.json)
ext_sha=$(git log --format=%H --reverse -S'scan_ts_tokens' -- tools/lexicon/lexicon.py | head -1)
test "$corpus_sha" != "$ext_sha"                       # STRICTLY earlier, not merely not-later
git merge-base --is-ancestor "$corpus_sha" "$ext_sha"
```

**The second query is a `-S` pickaxe and NOT a `--diff-filter=A`, and the difference is the whole
check.** `TOOL-aGradedDialect-3` adds no new file: it extends `tools/lexicon/lexicon.py`, which was
added by `0007b357` on 2026-08-16, weeks before this build opened. Anchoring on that file's birth
made the ancestor test FALSE for a perfectly correct build, so the criterion redded on exactly the
sequencing it exists to certify. Round 1 of the spec audit found it. The pickaxe answers the
question actually being asked — when did the extractor first EXIST — rather than when its host file
was created.

**And the inequality is not decoration: `--is-ancestor` is REFLEXIVE.** A commit is its own
ancestor, so a single pass that added the corpus and the reader together satisfies the ancestor test
perfectly — which is the exact case the ordering exists to refuse, since fixtures frozen in the same
breath as the reader had that reader available to their author. Round 3 found it. The two shas must
DIFFER and be ordered, and the `test` line above is what asserts the first half.

This is a DOCUMENTED CHECK and not a gate leg, because `selftest.py` runs the kit inside a throwaway
git repo and has no history to read there. It is run at the closing review and its result is written
into the review record.

What nothing catches, stated rather than left to be found: a later session may edit an expectation
to make a failing reader pass. Git shows the edit on that path, and the rule is that an expectation
changes only by re-running the oracle — but no arm enforces it, because any digest a session can
recompute is one it can recompute after editing both halves.

### Inventory

| identifier | where | cell |
|---|---|---|
| `tools/lexicon/ts-conformance-fixtures.json` | new file, the frozen corpus | `json` is declared dark |
| `read_ts_fixtures` | `selftest.py` | `py.function` — `--suggest` confirms `read` is on the table |
| `TS_FIXTURES` | `selftest.py`, the loaded corpus | constant, not graded by a verb cell |
| `TS_FLOOR_REFUSAL_SHARE` | `selftest.py`, F2's 2% | constant |
| `TS_FIXTURE_MINIMA` | `selftest.py`, the §4 composition table | constant |
| `check_ts_reading` | `selftest.py`, the runner | `py.function` — `--suggest` REFUSED `grade_ts_reading`: `grade` is unruled and no canon cluster holds it |

### Files touched (estimate)

`tools/lexicon/ts-conformance-fixtures.json` (new), `tools/lexicon/selftest.py` (arms and
constants), `tools/lexicon/kit.toml` (the corpus joins `selftest.py` under `role = "project-owned"`,
so it is withheld from `govkit apply` exactly as the self-tests are), `.gitattributes` (one LF pin).

### Alternatives rejected

| option | why not |
|---|---|
| authored fixtures | `TOOL-dScaffoldedMirror-13` refuses them by name, and they are the tautology this unit exists to close |
| fixtures generated on demand from the adopter tree | `selftest.py`'s own header refuses a kit test that reads a sibling this repo happens to track; it is unrunnable on every other node |
| committed `.ts`/`.tsx` fixture FILES | they would put TypeScript into this repo's tracked corpus, where the kit's own undeclared-extension refusal and its verb predicates would then grade adopter code |
| a percentage floor | `parser` means complete; a percentage cannot separate complete from nearly-complete, and it invites tuning the corpus |

## 5. Production-readiness checklist

- security — the corpus carries bounded excerpts of a third-party tree. Every span is the smallest
  that parses, capped at 60 lines, provenance-stamped, and withheld from `govkit apply`. Extraction
  rejects any candidate whose span carries a credential-shaped literal, and the reviewer reads the
  committed corpus before it lands. **`kit.toml` is only HALF the containment, and saying otherwise
  was a round-2 finding.** A `cp -r` copy-install does not read `kit.toml`, so a copy-installing
  adopter receives the corpus unless the runbook tells them to delete it. `WIRE-INTO-PROJECT.md:340`
  already carries exactly that step for `codebase-map`'s gov-only files; the matching line for this
  corpus is `TOOL-aGradedDialect-5` S7.
- perf / scale — the loader reads one file of at most a few hundred kilobytes and the runner walks
  at most 150 records, with no measurable movement against the wall-clock ceiling it sits inside.
  That ceiling is the `lexicon selftest` row in `tools/gate-legs.json`, read there and deliberately
  not typed here — a figure beside the manifest that owns it is what this build's README forbids.
- error / empty / loading states — an unreadable or empty corpus is a REFUSAL naming the file, never
  a skipped arm; a record missing a declared field names the record id.
- observability — every arm prints the population it judged: the record count, the per-construct
  census, and each disagreeing record id with both readings.
- risks — the adopter tree may move or vanish, which is why the expectations are the oracle's
  reading of the COMMITTED bytes and re-derivation needs that tree only for provenance. The residual
  risk is the corpus being edited to fit a reader, and the freeze section states plainly that
  nothing catches it.
- testing — the runner's failing case is observed at landing by scoring the shipped `js-regex` set
  against the corpus and asserting it misses the floor.
- migration — none. The file is new and nothing reads it before this unit lands.
- user docs — none owed here. `TOOL-aGradedDialect-5` owns every reader-facing carrier, and the
  corpus's own rules live in this spec and in the arm headers.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/selftest.py` runs, the corpus loader reports the record count
  and asserts that every record carries all nine declared fields, that `kind` is `ts` or `tsx`, that
  ids are unique, and that no `funcs` or `types` line exceeds its own record's `src` line count.
  Red when: a record names an expectation at a line its excerpt does not have, which is the shape a
  hand-edited expectation takes.
- **AC2** — When the same run reaches the composition arm, it derives the per-construct census from
  the records' own `constructs` tags and asserts every minimum in §4's table plus at least 40
  `kind: tsx` records.
  `figure:` DERIVED — the arm counts the corpus; the minima it compares against are PINNED policy
  with their reason in §4.
  Red when: a construct falls below its minimum, which is the corpus quietly losing the readings it
  exists to carry.
- **AC3** — When the two §4 queries are run — `git log --diff-filter=A` for the corpus JSON, which
  genuinely is a new file, and `git log --reverse -S'scan_ts_tokens'` over `tools/lexicon/lexicon.py`
  for the extractor, which is not — the corpus's adding commit is an ancestor of the extractor's
  first-touch commit, and the review record for this build states the two shas.
  `cost:` seconds, but it needs repository history, which `selftest.py` does not have in its
  throwaway repo — so it is a documented check run at the closing review, not a gate leg.
  Red when: the extractor's first-touch commit is not a descendant, which would mean the fixtures
  were frozen after the reader existed and the tautology objection is unanswered. Red also when the
  two queries return the SAME sha — `--is-ancestor` is reflexive, so a single pass carrying both the
  corpus and the reader passes an ordering test it should fail, and that is precisely the case the
  ordering exists to refuse. Red also when the
  extractor half is run as `--diff-filter=A` against a path already tracked at this build's base,
  which returns a commit predating the build and refutes a correct ordering.
- **AC4** — When the conformance arm runs with no TypeScript entry in `PARSERS` or the resolved
  pattern sets, it prints `SKIPPED` naming the arm and the missing extractor, and the floor
  constants `TS_FLOOR_REFUSAL_SHARE` and `TS_FIXTURE_MINIMA` are readable in `selftest.py`.
  Red when: the arm passes silently with no extractor present, which is a skip wearing a pass.
- **AC5** — When the runner scores the shipped `js-regex` set against this corpus, it MISSES the
  floor and the arm asserts the miss, printing the shortfall for functions and for types.
  `figure:` DERIVED at run time from the corpus; unit 1's 0.6% type recall is the evidence that the
  miss is not marginal, not a value this arm restates.
  Red when: `js-regex` clears the floor, which would mean the corpus contains nothing a same-line
  regex cannot read and grades no reader at all.

- **AC6** — When the conformance runner scores a reader, it COMPUTES the share of the corpus's
  oracle definition sites covered by that reader's declared refusal list, asserts it at or under
  `TS_FLOOR_REFUSAL_SHARE`, and asserts that every construct named in `parse_ts_defs.__doc__` has at
  least one fixture on which the reader RAISES.
  `figure:` DERIVED at observation time from the corpus and the docstring; no share is written into
  this spec.
  Red when: the refusal list names a construct no fixture exercises, which is a budget spent on a
  refusal nobody demonstrated. Red also when the share is merely READABLE and compared to nothing —
  which is what §4's F2 budget was until round 3, a declared ceiling with no arm reading it, and the
  reason F1 was reachable by refusing enough.
## 7. Gates

`lexicon selftest` · `lexicon naming predicates` · `govkit selfcheck` · `memory hygiene`

New arm: `tools/lexicon/selftest.py` · the shipped `js-regex` set scored against the frozen corpus,
which must miss the floor · no assertion floor moves; `ARMS_FLOORS` does not carry this suite.

New arm: `tools/lexicon/selftest.py` · AC6's budget arm — a reader whose declared refusal list
covers more of the corpus's oracle definition sites than `TS_FLOOR_REFUSAL_SHARE` allows, and a
refusal named in the docstring with no fixture that raises on it · none, same reason

**`lexicon selftest` is `subject = kit`, `chunk = selftests`, so the ORDINARY bar HOLDS it.** Four of
this unit's criteria are observed only inside that leg, so a green `bash tools/run-gates/run-gates.sh`
says nothing about them. This unit's Definition of Done therefore runs
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, or `python tools/lexicon/selftest.py` directly.
Stated here because a criterion observable only inside a held leg, with nothing saying so, is a skip
wearing a pass.

## 8. Open questions

- **F1 — may bounded excerpts of the adopter tree be committed to this repository at all?** The
  options are verbatim bounded excerpts, authored fixtures, and fixtures generated on demand from a
  tree only node `a` has. The second is refused by name in `TOOL-dScaffoldedMirror-13` and the third
  is refused by `selftest.py`'s own header, so only the first survives.
  RESOLVED (agent, 2026-09-10, delegated): commit bounded excerpts. The authority is not this run's
  judgement — `TOOL-dScaffoldedMirror-13`'s revisit test asks in its own words for "fixtures
  extracted from real adopter files rather than authored", which is a ratified decision naming this
  artifact, so the disclosure is priced rather than widened. The constraints in §5's security row
  are the price: smallest parsing span, 60-line cap, provenance stamped, credential-shaped literals
  rejected at extraction, and the corpus withheld from `govkit apply`. "So no adopter receives it"
  was the rev-1 wording and it OVERSTATED the containment: `govkit apply` honours `kit.toml` and a
  `cp -r` does not, so the copy-install path needs its own runbook step, allocated as
  `TOOL-aGradedDialect-5` S7 against the `codebase-map` precedent at `WIRE-INTO-PROJECT.md:340`.
  With that step the price holds as priced; without it, a copy-installing adopter receives the
  corpus, and the honest sentence is the one that says so.
- **F2 — does the floor grade imports?** RESOLVED (agent, 2026-09-10, delegated): no. The oracle
  collects functions and types, the predicate that read imports was deleted with `P3 layer`, and a
  floor over a value nothing consumes would be a criterion no reader could fail meaningfully. The
  return shape stays `(functions, types, imports)` because unit 3 inherits it; the third list is
  simply ungraded, and this spec says so where a reader looks for it rather than leaving unit 3 to
  discover it.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft, authored against unit 1's research record and the kit source.
- rev-2 · 2026-09-10 · §4 · AC3 · folded spec-audit round 1. The freeze proof anchored the
  extractor half on `git log --diff-filter=A -- tools/lexicon/ts-tokens.py`, a file
  `TOOL-aGradedDialect-3` does not create; that unit extends `lexicon.py`, whose own adding commit
  `0007b357` predates this build by weeks, so the ancestor test was FALSE on a correct build. Both
  the §4 block and AC3 now use a `-S'scan_ts_tokens'` pickaxe over `lexicon.py` for the extractor
  half and keep `--diff-filter=A` for the corpus JSON, and AC3's Red-when gained the
  already-tracked-path trap so the same mistake cannot return silently.
- rev-3 · 2026-09-10 · §3 · §5 · §7 · §8 · folded spec-audit round 2. §5's security row and §8 F1
  priced the disclosure on `kit.toml` alone and claimed "no adopter receives it"; a `cp -r`
  copy-install does not read `kit.toml`, so the containment needed a runbook step and now cites one,
  allocated as `TOOL-aGradedDialect-5` S7. §7 now states that `lexicon selftest` is a HELD leg, so
  this unit's DoD runs `GATE_SELFTESTS=1` — four criteria are observable nowhere else and an
  ordinary green bar says nothing about them. §3's `regex_vs_oracle.py` non-goal accused unit 1's
  record of a defect that rev-2 of that record fixed, and booked a closing follow-up for it; both
  are discharged and the follow-up is deleted. Note for a later fold: rev-3 of this spec landed
  after round 2 read it, so round 2's subject blob is not this text.
- rev-4 · 2026-09-10 · S4 · §4 · §5 · AC3 · AC6 · folded spec-audit round 3, the disposal round.
  NEW AC6: §4's F2 refusal budget was declared and read by nothing, so F1's exact-agreement floor
  stayed reachable by refusing enough — the arm now computes the share and asserts each named
  refusal has a fixture that raises. The freeze proof used `--is-ancestor` alone, which is
  REFLEXIVE: one commit carrying both the corpus and the reader passed the ordering test it exists
  to fail, so §4 and AC3 now require the two shas to DIFFER first. §5's perf row typed an 880 s
  ceiling beside `tools/gate-legs.json`, which owns it. Three citations of the containment's payer
  said S6; it is S7.
- rev-3 · 2026-09-10 · §3 · the `hands-off` edge to `TOOL-aGradedDialect-4` named only the
  per-record `kind` and JSX construct tags, which that unit's §8 F1 does not decide on — so the edge
  read as an overreach and hygiene check 12's reciprocity arm redded on this file. It named the wrong
  payload rather than the wrong unit. The real handoff is the declared FLOOR: that unit's S1 has
  always read the mode as `parser` at or above it and `probe` below it, so it rests a scope item on
  this corpus. The edge now names the floor first and the tags as secondary evidence, matching the
  `consumes-from` that unit declared at its own rev-3.

## 10. Reuse audit

The seam this unit extends is the frozen-fixture pattern already shipping in
`tools/lexicon/selftest.py` — `SENTINELS` for the pattern sets and `SHELL_SENTINEL` for the shell
parser — together with `tools/lexicon/lexicon.py:extract_text`'s mode dispatch, which is the call the
runner scores a reading through. Verified against source on 2026-09-10: both constants exist, each is
asserted to yield a non-zero definition count, and `resolve_pattern_sets` returns a new mapping so a
declared set never folds into `PATTERN_SETS`. This unit is the same idea one size up — a sentinel
proves a reader is not INERT, and this corpus proves a reader is COMPLETE — so the format follows the
sentinel's rule that a fixture is keyed on the construct and never on a line in a tracked file.
`python tools/codebase-map/reuse_lookup.py "freeze definition-site fixtures extracted by an external
oracle to grade a source reader"` ranked `extract_text`, `extract` and the
`fixture-passes-by-finding-nothing` gotcha class in the same candidate set, and reported its own
blindness as `unscanned layers: .sh`, so nothing here rests on its silence about shell.

Recall terms used: `lexicon typescript tsx probe parser dark PATTERN_SETS coverage extractor
PascalCase React casing tokenizer adopter`
