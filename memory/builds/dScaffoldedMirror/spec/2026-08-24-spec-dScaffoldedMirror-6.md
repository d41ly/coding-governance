# TOOL-dScaffoldedMirror-6 — the coverage floor and the LANGS mode ratchet

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling

## 1. Goal

Every fail-closed story in this kit covers the UNDECLARED (extension, predicate) pair and none
covers the declared-dark one, which is the cheap move: one string edit in `LANGS` empties the graded
population and reds nothing. Measured on this worktree — flip `py` from `parser` to `dark` and the
armed share of definition-carrying files collapses from 42.9% to 7.9%, and today that run prints
`lexicon OK` and exits 0. Print the coverage fraction on every run, floor it, and ratchet each
extension's mode so that `parser → probe → dark` is a weakening move that needs a justification
written in place. This is the largest unclosed hole the review found and no design owned it.

## 2. Scope (IN)

- **S1** — every run prints the coverage line, on green as well as on red:
  `coverage — armed N of M definition-carrying file(s) (P%) · floor F%`. Measured today: `54 of 126
  (42.9%)`.
- **S2** — the denominator is derived by a kit-owned COVERAGE SNIFFER that runs over every tracked
  text file regardless of its `LANGS` declaration. §4 states why the denominator cannot come from
  the armed extractors, and what structurally stops the sniffer from becoming a second vocabulary.
- **S3** — `COVERAGE_FLOOR` enters `.lexicon.conf` at `35`, and a run below it REDS naming the
  measured fraction and the floor. §4 derives the number.
- **S4** — the floor is a scalar and therefore a pin with its sign flipped, so it lands with a
  `RATCHETS` row `{"file": ".lexicon.conf", "key": "COVERAGE_FLOOR", "weakens": "down"}` in the same
  commit. The row uses the mechanism `TOOL-dScaffoldedMirror-5` owns; this unit does not restate it.
- **S5** — the `LANGS` mode ratchet. Ranks are `parser` 2, `probe` 1, `dark` 0, absent −1. An
  extension whose rank FALLS between the base and HEAD is a finding unless a comment within
  `RATCHET_LOOKBACK` lines above the `LANGS` declaration names the move as `<ext>: <old> -> <new>`.
- **S6** — the sniffer's own liveness assertion: when at least one extension is declared `dark` and
  present in the corpus, the sniffer must find at least one definition-carrying file among them, or
  the run prints `DEAD SNIFFER` and REDS. Without it a broken denominator reports 100% coverage.
- **S7** — `tools/lexicon/README.md` states what the fraction does NOT measure: extraction quality.

## 3. Non-goals (OUT)

- **No arming of `sh`.** 518 shell definitions of which 433 (83.6%) are off-table would be a 94%
  increase on a 463 population, from a language the kit declares dark by a written law. The sniffer
  COUNTS shell files; nothing grades them.
- **No JS/TS lexer.** The research refused one on ORDER, not cost, and that refusal binds. §4 states
  the structural difference between a lexer and this sniffer, because they will otherwise be
  confused.
- **No per-(extension, predicate) coverage.** Declaring coverage at that resolution multiplies the
  surface sevenfold; the fraction is per-file and the per-predicate question is
  `TOOL-dScaffoldedMirror-2`'s `DEAD PREDICATE`.
- **No new `RATCHETS` primitive for scalars.** `RATCHETS` stays scalars-only for scalars; S5 adds a
  SECOND, differently-shaped ratchet beside it rather than widening the first.
- **No `.ts`/`.tsx` pattern set.** `TOOL-dScaffoldedMirror-13` owns that question and this unit's
  fraction is what will make its answer measurable.

## 4. Design

### The denominator cannot come from the thing it measures

The obvious denominator is "files the extractors saw", and it is the mirror defect one level down:
every file an armed extractor sees is armed, so the fraction is 54/54 = 100% and rises as coverage
falls. The denominator has to be exogenous to the declaration, which means something must count
definition-carrying files in languages the kit deliberately does not extract.

That something is the coverage sniffer, and its contract is narrow enough to state in four lines:

- it runs over every tracked file the kit can read as text, whatever `LANGS` says;
- it returns ONE integer, the number of files in which it saw at least one definition-like line;
- it never returns a name, a line number or an extension-keyed breakdown beyond the count;
- nothing reads its output except the fraction, and no path exists from it to any predicate or to
  `scaffold_lexicon.py`.

Those last two are the structural guard, not a promise. The refused JS/TS lexer was refused because
it would ARM predicates over a corpus nobody has measured and has no independent oracle. A sniffer
that cannot produce a name cannot arm anything, and its wrongness is bounded: a sniffer that
over-counts inflates the denominator and makes coverage look WORSE, which is the safe direction.

It is incomplete by construction and says so on every run, in the §12 sense — the coverage line
carries `sniffer: heuristic` so a reader never mistakes the denominator for an enumeration.

Measured with a shell-function probe of exactly this shape on this worktree at `af4de2d5`:

| | tracked | carrying ≥1 definition |
|---|---|---|
| `.py` (parser, armed) | 44 | 44 |
| `.js` (probe, armed) | 10 | 10 |
| `.sh` (dark) | 82 | 72, holding ~518 definitions |
| total definition-carrying | | **126** |
| armed share | | **54 of 126 = 42.9%** |

### Where the floor goes, and why it is 35 rather than 42.9

A floor at today's value is a ratchet in name and a flaky gate in fact. The denominator is a
population the author does not control: adding two shell scripts moves 54/126 to 54/128 = 42.2% and
reds a commit that changed no declaration. This repo adds `.sh` files routinely — 56 commits since
2026-06-01 add at least one — so a floor at 42.9% would red on ordinary work, and a gate that reds
on ordinary work gets bypassed. That is the same argument the research used to refuse self-declared
wall-clock ceilings, and it applies here unchanged.

A floor far below today's value is decoration: at 10% the `py`→`dark` flip lands at 7.9% and is
caught by 2 points, and a single extension arriving dark clears it forever.

`35` is derived from the two numbers that bracket it. With the numerator held at 54, the denominator
may grow to 154 before 54/154 = 35.06% reds — 28 dark definition-carrying files arriving before the
floor bites. The largest single-commit `.sh` arrival on record in this repo is **3 files**, measured
across the 56 commits since 2026-06-01 that add one, so the headroom is nine times the largest
observed honest move. And the move this unit exists to catch lands at 7.9%, twenty-seven points
under the floor rather than two.

The floor is a scalar in a conf, which is a pin with the sign flipped, and this build's whole thesis
is that a raisable scalar is not pressure. S4 is what stops it being one: lowering `COVERAGE_FLOOR`
is a weakening move that lands in `RATCHETS` and needs its reason written beside it. This is the
first row in that list whose `weakens` is `down`, and the direction is declared per entry precisely
so it can be.

### The mode ratchet, and the move it cannot see

`RATCHETS` is scalars-only and `_scalar_at` (`drift_report.py:166-186`) matches an integer bound to
a key. A per-extension mode is neither, so S5 is a new shape rather than a new row: read `LANGS` at
the base and at HEAD through `lexicon_conf.load_conf` and `langs()` — the kit's own reader, never a
second parser — build `{ext: rank}` at both, and report every extension whose rank fell.

It lives in `drift-audit` rather than in the lexicon checker, because `drift-audit` already owns the
base-versus-HEAD comparison and already reads `.lexicon.conf` through the lexicon's own reader for
`signal_lexicon_ratified_stale` (`drift_report.py:726-762`). Putting a second base comparison inside
the lexicon leg would give this repo two answers to "has the declaration weakened".

The justification matcher is a sibling of `_justified` rather than the same function: `_justified`
compiles a regex over two integers and the mode form is `<ext>: <old> -> <new>` over three tokens.
One function serving both would have to accept either shape, which makes a malformed integer marker
match as a mode marker.

**What the mode ratchet cannot see, stated because the floor exists to cover it:** an extension
arriving for the FIRST time as `dark` has no prior rank, so nothing fell and no finding is produced.
That is the incms shape exactly — 626 `.ts` and 572 `.tsx` files with no pattern set — and it is why
S1 and S3 ship, and ship first. The ratchet catches the flip; the floor catches the arrival.

### Rollout

Two commits, in this order, because they have different risk:

1. S1, S2, S6, S7 — the sniffer, the printed fraction and the liveness assertion. About 15 lines of
   reporting over a ~40-line sniffer, no new declaration, and it cannot red an honest tree except
   through S6.
2. S3, S4, S5 — the floor, its ratchet row and the mode ratchet. About 120 lines, a new conf key and
   a new comparison shape.

The split exists so that a landing-day problem in the ratchet does not hold the fraction, which is
the piece that makes every later measurement in this build readable.

### Files touched (estimate)

`tools/lexicon/lexicon.py` (~55 lines: the sniffer, the fraction, the floor comparison, S6),
`.lexicon.conf` (one key plus its justification block), `tools/lexicon/selftest.py` (the arms in
§6), `tools/drift-audit/drift_report.py` (~90 lines for the mode ratchet and its matcher),
`tools/drift-audit/drift_signals.py` (the S4 row), `tools/lexicon/README.md` (S7).

### Alternatives rejected

- **Denominator = all tracked files.** 54 of 899 is 6.0% and it moves whenever a markdown file
  lands, so it measures documentation volume rather than coverage.
- **Floor as a count rather than a fraction.** `armed >= 54` reds when a Python file is deleted, and
  it says nothing when a thousand dark files arrive.
- **Mode ratchet inside `lexicon.py`.** It would need its own base resolution, which is the second
  answer to a question `drift-audit` already answers.
- **Per-(extension, predicate) modes.** Sevenfold surface for a distinction `DEAD PREDICATE` already
  makes at the point it matters.

## 5. Production-readiness checklist

- **security** — N/A. The sniffer reads tracked files the checker already reads, matches lines with
  a compiled regex, and evaluates nothing.
- **perf / scale** — the sniffer reads every tracked text file rather than only the declared ones:
  899 files here against 54 today. Measured shape on this worktree is well under a second and the
  check is 0.44 s warm. On a 6,168-file adopter this is the unit that changes the cost profile most,
  and the mitigation is that it reads bytes and runs one regex rather than parsing.
- **a11y** — N/A, a CLI checker.
- **i18n** — N/A. The sniffer decodes with `errors="replace"` and counts lines, so a non-UTF-8 file
  degrades to a miss rather than an exception.
- **error / empty / loading states** — an unreadable file counts as not definition-carrying, which
  understates the denominator and therefore overstates coverage; S6 is the assertion that catches
  the degenerate case of that going wrong wholesale. A repo with no dark extension declared skips S6
  and the coverage line says so.
- **observability** — the coverage line is the observability change, and it prints on green. It is
  also the operand every later unit in this build reads when it claims coverage moved.
- **risks** — two. First, the sniffer is a heuristic in a kit whose thesis is that derived standards
  are untrustworthy; the containment is that it produces a single integer and feeds exactly one
  consumer, stated in §4 as structure rather than as a promise. Second, `COVERAGE_FLOOR` is a new
  scalar in a build that is deleting scalars, and S4 is the answer.
- **testing + left-shift gates** — six arms in `tools/lexicon/selftest.py` and one in
  `tools/drift-audit/selftest.py` (§6). The classes are
  `memory/gotchas/vacuous-selector-empty-population.md` for S6 and
  `memory/gotchas/fixture-passes-by-finding-nothing.md` for the sniffer fixtures.
- **migration / rollback** — `COVERAGE_FLOOR` is a new key; a conf without it takes the kit's
  shipped default rather than 0, because an absent floor reading as 0 would be a silently disabled
  gate. Rollback is deleting the key and the row.
- **user docs** — S7, plus the `.lexicon.conf` comment block above the new key, which is where the
  floor's derivation must live so a later session raising or lowering it reads §4's arithmetic
  instead of re-deriving it.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py` runs on this worktree unchanged, it prints
  `coverage — armed 54 of 126 definition-carrying file(s) (42.9%) · floor 35%` and exits 0. Observed
  with no staged break.
- **AC2** — When `LANGS` is edited so `py` reads `py:python-ast:dark` and nothing else changes, the
  same command reports the fraction as `7.9%`, names `COVERAGE_FLOOR`, and exits 1. Today that edit
  prints `lexicon OK` and exits 0; the arm is staged from this tree.
- **AC3** — When a fixture repo declares a new extension as `dark` and that extension carries enough
  definition-carrying files to push the fraction below the floor, the run exits 1 — even though no
  existing `LANGS` row changed. This is the arriving-dark move, which S5 cannot see.
- **AC4** — When `py` is flipped from `parser` to `dark` with no `py: parser -> dark` marker within
  14 lines above the `LANGS` declaration, `python tools/drift-audit/drift_report.py` reports the
  weakening move; with the marker present it reports nothing.
- **AC5** — When `COVERAGE_FLOOR` is lowered from `35` with no `35 -> N` marker beside it, `python
  tools/drift-audit/drift_report.py` reports it, by the same `RATCHETS` row shape every other pin in
  that list uses.
- **AC6** — When the coverage sniffer is broken so it reports no definition-carrying file in any
  dark extension, `python tools/lexicon/lexicon.py` prints `DEAD SNIFFER` and exits 1 rather than
  reporting `100.0%`. Staged by replacing the sniffer's pattern with one that cannot match.
- **AC7** — When `bash tools/run-gates/run-gates.sh` runs after both commits, `lexicon naming
  predicates`, `lexicon selftest`, `lexicon wiring`, `drift-audit selftest` and `drift-audit
  records` are green.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `drift-audit
selftest`, `drift-audit records`, `memory hygiene`. Adds no new gate leg — S1, S3 and S6 are new
refusals inside `lexicon naming predicates`, S5 rides `drift-audit records`, and the arms ride the
two selftest legs. The leg count is not the coverage, and in a unit whose subject is coverage that
is worth saying twice.

## 8. Open questions

- **F1 — is the coverage sniffer a vocabulary the kit will regret shipping?** It is a second reader
  of source files in a kit whose entire diagnosis is that its standards are derived from its
  subject. RECOMMENDATION: ship it, bounded as §4 specifies — one integer out, no names, exactly one
  consumer, and a declared heuristic label on every run. The alternative denominators are 54/54 (the
  mirror) or 54/899 (a documentation-volume metric), and a fraction that cannot fall is worse than a
  heuristic that can be wrong in the safe direction. RESOLVED (agent, 2026-08-24, delegated): ship
  the sniffer under the four-line contract in §4, with S6 as its liveness assertion.
- **F2 — should the floor red, or only warn, in its first release?** A warning would let the
  fraction land without any landing-day risk at all. RECOMMENDATION: red. A warning is the `# NOTE:`
  shape `TOOL-dScaffoldedMirror-2` exists to delete, and the floor is set at 35 precisely so that
  redding is not a landing-day risk — this tree sits 7.9 points above it. RESOLVED (agent,
  2026-08-24, delegated): red, at floor 35, with the two-commit rollout in §4 carrying the risk
  instead.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on recommendation R5 of the `dScaffoldedMirror`
  research pass (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`)
  and on the read-only probe of `incms/main` taken the same day, which is where the arriving-dark
  case in §4 comes from — 626 `.ts` and 572 `.tsx` files with no pattern set, an extension surface
  the mode ratchet is structurally unable to see. R5 leaves the floor VALUE undecided; §4 decides it
  at 35 and derives the number from this repo's own largest observed dark arrival rather than from
  taste.
- rev-1 status 2026-08-24 · KEPT in the six-unit build, S3/S4 CUT by the owner ruling: the coverage floor is a conf scalar this spec's own S4 calls a pin with the sign flipped, and it is defended by a ratchet row `-9` deletes. S1/S2/S5/S6 survive - the printed fraction, its liveness assertion and the mode ratchet are the only control that makes `-2`'s cheap js-dark escape visible. Needs a rev-2 scope pass before building.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py coverage floor fraction dark mode` returns
`compute_coverage` (`tools/codebase-map/map_lib.py`, fan-in 4, SEAM) and its `Coverage` class,
`parse_floors` (`tools/memory-tree/check-arms.py`), and the gate-leg inventory keys `codebase-map
coverage + freshness` and `recall floor`. `compute_coverage` is the top-ranked hit and it is the one
seam this unit is FORBIDDEN to wire through: it answers a different question — claimed inventory
keys over machine-enumerated keys, with four both-direction asserts — and, decisively,
`.lexicon.conf`'s only `LAYERS` rule is `tools/lexicon/* -> tools/codebase-map/*`, so an import
would red this kit's own P3 predicate. That rule exists because this kit must ship self-contained,
and it is the reason `subtokens.py` was ported rather than imported. `parse_floors` reads
memory-tree's arms declaration and shares no grammar with a percentage. No existing seam fits; the
sniffer and the mode comparison are both new, and §4 bounds each one rather than reusing a shape
that answers something else.
