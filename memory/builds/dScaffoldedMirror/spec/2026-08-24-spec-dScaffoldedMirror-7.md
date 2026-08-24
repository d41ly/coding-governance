# TOOL-dScaffoldedMirror-7 — the marginal-offense-rate signal

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling

## 1. Goal

Nothing in this kit measures the owner's actual demand — are new generations constrained. The one
result that reframes the whole build, 136 definitions and zero offenders since the table landed, is
one agent's afternoon over eight days with a named confound, and re-deriving it today under a
plainly stated keying gives 21.2% instead of 0% (§4). Ship a standing `drift-audit` signal:
offenders ADDED per definition ADDED between a derived base and HEAD, both operands produced at both
shas by the kit's own extractor. Nothing authored, nothing raisable. This unit discharges owner
ruling `TOOL-dScaffoldedMirror-17` — it is what makes the benefit measurable and therefore what
removes F-A5's stated premise — and §4 names exactly what the supersession commit must change and
who writes it.

## 2. Scope (IN)

- **S1** — `signal_lexicon_marginal_offense_rate` in `tools/drift-audit/drift_report.py`, reporting
  offenders added and definitions added over the window, with `gateable: False`.
- **S2** — the base is DERIVED, never declared: the commit that first added `.lexicon.conf`,
  resolved as `git log --diff-filter=A --format=%H -- .lexicon.conf | tail -1`. On this repo that is
  `b0626152`, 2026-08-16. The window is "everything since the declaration existed", which is the
  question the signal asks.
- **S3** — the operand definition is DECLARED in the signal's own docstring and is part of the
  contract, not an implementation detail: a definition is a `(path, name)` pair produced by the
  kit's extractor over the declared armed extensions; added = present at HEAD, absent at base; an
  offender is an added pair whose leading token is outside the table AT HEAD.
- **S4** — `extract_text(src, mode, pset)` splits out of `extract()` (`lexicon.py:182-190`), which
  becomes a two-line path wrapper. The signal reads blobs from git and never writes a tree.
- **S5** — the liveness assertion, three conditions, any one false giving DEAD PROBE rather than a
  number: the base sha resolves in this object store; the definition population at the base is
  non-zero; the definition population at HEAD is non-zero.
- **S6** — a window with zero definitions ADDED is NOT ASKED, not a rate of 0, routed through the
  existing `_build_not_asked` renderer so the three states stay three.
- **S7** — a per-sha cache keyed on `(sha, digest of the VERBS table)`, because a commit's tree is
  immutable but the table that grades it is not.

## 3. Non-goals (OUT)

- **Not gateable, and not on the merge bar.** It is a trend, one bad landing must not red the bar,
  and a rate has no honest pin: any threshold would be the raisable integer this build exists to
  delete, wearing a percentage sign.
- **No authored base.** A declared `MARGINAL_BASE_SHA` would be a pin that moves forward —
  shortening the window hides the stretch it removes — and §4 states what replaces the research's
  stated failing case as a result.
- **No attribution.** The signal reports a rate, not who wrote the offenders. Naming authors is a
  different instrument with a different failure mode.
- **No diff-scoped enforcement.** This repo has three incompatible bases at the push boundary and
  the research killed base-dependent enforcement on that ground; a REPORT over a derived base is not
  enforcement.
- **No change to any predicate or pin value.** The signal reads; it decides nothing.

## 4. Design

### The number nobody has actually pinned down

Re-derived on this worktree at `af4de2d5`, over the same window the research pass used
(`b0626152..HEAD`, 2026-08-16 to 2026-08-24), through the kit's own extractor, `(path, name)`
keying:

| scope | definitions added | offenders added | rate |
|---|---|---|---|
| research pass, as reported | 136 | 0 | 0% |
| all armed files | 236 | 50 | **21.2%** |
| definitions in files NEW in the window | 117 | 5 | 4.3% |
| definitions in files that already existed | 119 | 45 | 37.8% |
| all armed files, excluding `tools/govkit/` | 170 | 18 | 10.6% |

Four scopes, one window, four answers spanning 21 points. The rate is currently a function of an
operand definition nobody wrote down, which is precisely why S3 puts the definition in the contract
rather than in the code.

The confound is named and it is large. The 50 offenders concentrate in `tools/govkit/govkit.py`
(20), `tools/memory-tree/gen_build_index.py` (12) and `tools/govkit/selftest.py` (7) — and
`.lexicon.conf`'s own archaeology already records why: "32 of the 45 are the govkit deployer, which
landed its three new modules and its selftest without the verb table applied". A landing authored on
a branch that predates the table's reach is inside this window, and no scope choice makes that go
away. The research pass's own caveat is the other half of it: the sessions that produced the clean
stretch had just built the kit.

**None of this refutes the research's finding, and the spec says so plainly.** The declaration
plainly does constrain sessions that have read it — the 4.3% rate in files written fresh during the
window is the same result under a stricter keying. What the table above refutes is the idea that the
result is currently a MEASUREMENT. It is an observation whose operands were chosen once, by hand,
after the fact. Making it standing is the whole point of this unit, and it is the only thing that
converts the claim into one a later session can falsify.

### The base, and the failing case that replaces the research's

R6 states the failing case as "set the base to a sha not in the object store". Under S2 that case is
unreachable: there is no base to set. The assertion survives and its trigger changes — a SHALLOW
clone, which CI does routinely, does not contain the adoption commit, and `git cat-file -e
<sha>^{commit}` fails there. That is the same assertion with a reachable trigger, and it is the one
staged in §6.

Deriving the base also removes the only knob. `.lexicon.conf` was added once; the value is a fact
about a commit already made, and shortening the window would require deleting and re-adding the
conf, which is a visible act with its own consequences under `TOOL-dScaffoldedMirror-5`.

### What `live` actually asserts, stated because a liveness flag is usually a lie

Three conditions, each independently falsifiable, and the third is the one that catches the mundane
failure:

| | condition | what makes it false |
|---|---|---|
| L1 | base sha resolves | shallow clone, grafted history, a fresh clone with `--depth` |
| L2 | definition count at base > 0 | the extractor broke, or `LANGS` went dark at the base |
| L3 | definition count at HEAD > 0 | the extractor broke at HEAD |

Any false → DEAD PROBE, and no value is reported. This is distinct from S6: a window in which nobody
added a definition is a real and common state (a records-only stretch), and reporting it as a rate
of 0 would be indistinguishable from a clean one. `_build_not_asked` (`drift_report.py:652-663`)
already exists for exactly that three-way split, and the signal routes through it rather than
inventing a fourth state.

**The class a reviewer will fire at this, answered in advance.**
`memory/gotchas/assertion-between-two-derived-values.md` says a check comparing two values the same
code derives from one source is a tautology. It does not apply here and the distinction is precise:
the same code derives both operands from TWO DIFFERENT SOURCES — the tree at the base and the tree
at HEAD — and a commit's content is exogenous to the checker. The comparison can disagree, and §4's
table is a run in which it did.

### Cost, and where it actually goes

The research pass measures the derive-at-sha at 0.369 s on gov and 3.218 s on incms. Re-derived here
the same work took **2.774 s for both shas**, using one `git show` per file — 108 process spawns.
The difference is not compute. Node `d`'s anti-virus taxes every exec by roughly 0.022 s, which is
`memory/gotchas/process-creation-is-the-suite-cost.md`, and 108 spawns is 2.4 s of it. The shape
that ships therefore reads blobs in ONE batched `git cat-file --batch` per sha rather than per file,
and the per-file figure above is recorded so that a later reading of 2.8 s is diagnosed as spawn
count rather than as a regression.

S7's cache key is `(sha, digest of the VERBS table)` rather than the sha alone. A commit's tree is
immutable, but admitting a verb changes which of its definitions are offenders, so a sha-only key
would serve a stale rate forever after the next curation pass — the same "one fact, two carriers"
shape this build keeps finding.

### Discharging `TOOL-dScaffoldedMirror-17`

The ruling is already ratified in `memory/DECISIONS.md` at HEAD: F-A5's opt-in survives, its REASON
does not. What remains is prose still asserting the dead premise, and it is in two live carriers:

| file | line | what it says |
|---|---|---|
| `tools/lexicon/README.md` | 10 | "not measurable — which is why the kit is opt-in" |
| `memory/map/features/lexicon.md` | 176 | "unmeasurable by construction", and F4 |

Both are edited in THIS unit's commit, each citing `TOOL-dScaffoldedMirror-17` and this signal by
name. The dossier bullet carries a second dead premise in the same sentence — F4's retirement
condition, superseded by `TOOL-dScaffoldedMirror-16` — so it is rewritten rather than trimmed.

Two things are deliberately NOT edited.
`memory/builds/dClosedLexicon/spec/2026-08-16-spec-dClosedLexicon-1.md` states F-A5 at line 205 and
rejects requiring the kit at line 323; a ratified record is superseded, never rewritten, and the
supersession is the DECISIONS row. And the opt-in BEHAVIOUR is untouched: `lexicon.py:394-396` and
`adopt-lexicon.sh:77` keep saying the kit is inert without a conf, because opt-in survives.

Who writes it is this unit's builder, in this unit's commit. A supersession landing in a different
unit's commit than the mechanism that discharges it is a supersession nobody will find, which is the
failure mode `TOOL-dScaffoldedMirror-17` exists to prevent.

### The pin this unit moves, and the phase order it depends on

Every signal in `drift_report.py` leads with `signal_`, and `signal` is off-table — the conf's own
archaeology records the last two arrivals raising the pin 415 → 417 for exactly this reason. So this
unit adds one offender and `VERB_OFFENDER_PIN` moves 463 → 464, which under
`TOOL-dScaffoldedMirror-5` needs a `463 -> 464` marker within 14 lines above the pin. Its helpers
take `measure` and `derive`, both already in the table, so the count is one and not four.

That is only true while this unit lands before `TOOL-dScaffoldedMirror-9`. After the freeze, a
post-freeze offender cannot be grandfathered and cannot be raised away, so the name would have to
change or a waiver would have to carry it. Phase 0 before Phase 4 is what keeps this a one-line pin
move; if the order slips, this becomes a renaming question and the spec should be re-read.

### Files touched (estimate)

`tools/drift-audit/drift_report.py` (~110 lines: the signal, the two derivations, the cache),
`tools/drift-audit/drift_signals.py` (the PINS row), `tools/lexicon/lexicon.py` (~8 lines for S4),
`tools/drift-audit/selftest.py` (the arms in §6), `tools/lexicon/README.md` and
`memory/map/features/lexicon.md` (the supersession), `.lexicon.conf` (the pin move and its marker).

### Alternatives rejected

- **A declared base sha.** A knob that shortens the window is a pin, and the thing it hides is the
  stretch it removes.
- **Rate over commits rather than over definitions.** A commit is not a unit of generation; a
  records commit and a 40-definition landing would weigh the same.
- **Keying on the bare name.** A definition that moved file would read as deleted and re-added,
  inflating both operands. `(path, name)` is the same key `TOOL-dScaffoldedMirror-4` gives the
  waivers, deliberately.
- **Making it gateable at a pin.** §3, and it is the whole argument of this build.

## 5. Production-readiness checklist

- **security** — N/A. Reads blobs from the local object store through `git`, parses them with the
  extractor the check already runs, and writes only a cache under the git dir.
- **perf / scale** — 0.369 s on gov and 3.218 s on incms per the research pass; 2.774 s measured
  here for both shas at 108 spawns, which §4 attributes to process creation. Batched blob reads and
  the S7 cache are what keep it there. Not on the merge bar, so its ceiling is a person's patience
  rather than a gate's.
- **a11y** — N/A, a CLI report.
- **i18n** — N/A. Blobs are decoded with `errors="replace"`, as the extractor already does.
- **error / empty / loading states** — four states and each is distinguishable: a rate, NOT ASKED
  (nothing added), DEAD PROBE (L1-L3), and absent (no `.lexicon.conf`, the existing
  `_resolve_lexicon_conf` guard). Collapsing any two of them is the defect this unit is guarding
  against in its own instrument.
- **observability** — the signal IS the observability change, and it is the first standing
  measurement of the mechanism this kit's value rests on.
- **risks** — the honest risk is that the first standing reading is 21.2% rather than 0%, and reads
  as the kit having failed. It is not: §4's split shows 4.3% in files written fresh in the window
  against 37.8% in files that predate the table, and a trend signal's first reading is a baseline
  rather than a verdict. The mitigation is that the signal ships with §4's table cited in its
  docstring, so the first reader gets the decomposition and not just the number.
- **testing + left-shift gates** — five arms in `tools/drift-audit/selftest.py` (§6). The classes
  are `assertion-between-two-derived-values.md` (answered in §4),
  `vacuous-selector-empty-population.md` (L2, L3) and `process-creation-is-the-suite-cost.md` (the
  batched read).
- **migration / rollback** — none. A new `PINS` entry and a new signal; reverting removes both, and
  the cache is under the git dir and untracked.
- **user docs** — the two supersession edits in §4, plus the `drift-audit` README's signal list.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs on this worktree, it reports
  `lexicon_marginal_offense_rate` with `gateable: False` and a value derived at `b0626152` and at
  HEAD, and the report names both operands rather than only the ratio.
- **AC2** — When the same command runs in a `git clone --depth 1` of this repo, the signal reports
  DEAD PROBE naming the unresolvable base, and no rate is printed. This is the reachable replacement
  for R6's unreachable "point the base at an absent sha" case.
- **AC3** — When the window contains no added definition, the signal renders as NOT ASKED through
  `_build_not_asked` rather than as a rate of `0`. Staged by running the report with base and head
  at the same sha.
- **AC4** — When `.lexicon.conf` is absent from the tree, the signal reports NOT ASKED and the
  report exits with its existing code, so an adopter without the kit is unaffected.
- **AC5** — When a verb is added to `VERBS` and nothing else changes, the second run recomputes
  rather than serving the cached rate, proving the S7 cache key includes the table digest.
- **AC6** — When `bash tools/run-gates/run-gates.sh` runs after the change, `drift-audit selftest`,
  `drift-audit records`, `lexicon naming predicates`, `lexicon selftest` and `lexicon wiring` are
  green, with `VERB_OFFENDER_PIN` at `464` and its `463 -> 464` marker in place.
- **AC7** — When `grep -n "unmeasurable" tools/lexicon/README.md memory/map/features/lexicon.md`
  runs after the change, it returns nothing, and both files instead cite
  `TOOL-dScaffoldedMirror-17` and this signal.

## 7. Gates

Keeps green: `drift-audit selftest`, `drift-audit records`, `drift-audit wiring`, `lexicon naming
predicates`, `lexicon selftest`, `lexicon wiring`, `memory hygiene`, `codebase-map coverage +
freshness` (the dossier edit). Adds no new gate leg — the signal rides the existing `drift-audit
records` leg and its arms ride `drift-audit selftest`. The leg count is not the coverage.

## 8. Open questions

- **F1 — should the signal report one rate, or the four-way decomposition in §4?** One number is
  what a signal row can carry; the decomposition is what makes it readable. RECOMMENDATION: report
  the single contract rate as the value and carry the new-file versus pre-existing split in the
  signal's `detail`, which the JSON already renders and the human table already truncates. That
  keeps the row a row while preserving the split that stops a first reading being misread.
  RESOLVED (agent, 2026-08-24, delegated): one value, the split in `detail`.
- **F2 — does the offender test read the table at HEAD or at the base?** Reading it at the base
  would freeze the standard the window is graded by, which is defensible for a trend.
  RECOMMENDATION: at HEAD, matching `TOOL-dScaffoldedMirror-9`'s ruling 1 that the freeze-time
  derivation reads today's conf — one rule for both, rather than two mechanisms disagreeing about
  which conf grades history. The consequence is stated: admitting a verb retroactively lowers the
  rate, and that shows up as a step in the trend rather than silently. RESOLVED (agent, 2026-08-24,
  delegated): at HEAD, consistent with `-9`.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on recommendation R6 of the `dScaffoldedMirror`
  research pass (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`)
  and on the read-only probe of `incms/main` taken the same day. Two departures are recorded rather
  than folded silently. R6's base is "a recorded base"; S2 DERIVES it from the conf's own adoption
  commit, which removes the last authored operand and makes R6's stated failing case unreachable —
  §4 replaces it with the shallow-clone case, which is the same assertion with a trigger that
  occurs. And R6 carries the 136-definitions/zero-offenders figure forward as context; §4 re-derives
  it and reports 21.2% under a plainly stated keying, which does not overturn the research's
  conclusion but does show that the figure is not yet a measurement.
- rev-1 status 2026-08-24 · KEPT and RE-ORDERED to land FIRST in the six-unit build. Two corrections owed at rev-2: the signal name leads with a token outside the declared table, and this spec's pin move rests on a false premise - two `SIGNALS` entries already lead with `build`. Add the sentence no spec in the set contains: what reading of this signal KILLS the pressure chain.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py signal marginal rate liveness derivation` returns the
`derive_*` family in `tools/playbook/render_playbook.py` (nine functions, all fan-in 0), the gotcha
class `assertion-between-two-derived-values.md`, and the inventory key `derive [lexicon-verbs]`. The
`derive_*` family is a naming echo rather than a seam — each one reads a deploy answer for the
renderer and none of them touches a sha, a tree or a population. The gotcha class is a hazard this
unit must answer, which §4 does, not a mechanism to wire through. The seams that DO fit are internal
to `drift_report.py` and this unit uses all three unchanged: `_resolve_lexicon_conf` (`:624-630`)
for the adopter guard, `_load_lexicon` (`:633-651`) for reading the table through the lexicon's own
reader rather than a second parser, and `_build_not_asked` (`:652-663`) for S6's third state. The
one new seam is `extract_text` (S4), which is a split of `lexicon.py`'s existing `extract` rather
than a second extractor — deriving from a blob without writing a tree is the requirement, and a
second implementation of the extractor would be the `second-implementation-is-not-a-second-opinion`
class in the instrument whose entire value is that both operands come from the same one.
