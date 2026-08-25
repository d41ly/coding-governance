# TOOL-dScaffoldedMirror-13 — the .ts/.tsx darkness, decided rather than inherited

**Status:** DEFERRED · rev-1 · 2026-08-24 · node d · Tier-1 · base 9ddcc5c9 · streams tooling · shrink to a LEXICON.md ruling; the spec itself is not the deliverable

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md](../build/2026-08-24-build-TOOL-dScaffoldedMirror-2-spec-set-review.md) | spec-audit | TOOL-dScaffoldedMirror-2 TOOL-dScaffoldedMirror-3 TOOL-dScaffoldedMirror-4 TOOL-dScaffoldedMirror-5 TOOL-dScaffoldedMirror-6 TOOL-dScaffoldedMirror-7 TOOL-dScaffoldedMirror-8 TOOL-dScaffoldedMirror-9 TOOL-dScaffoldedMirror-10 TOOL-dScaffoldedMirror-11 TOOL-dScaffoldedMirror-12 TOOL-dScaffoldedMirror-14 TOOL-dScaffoldedMirror-15 |

<!-- /gen:spec-records -->

## 1. Goal

The only real gov adopter's primary language is invisible to this kit, and nobody decided that — it
fell out of a lookup table. Measured 2026-08-24 by a read-only run of the kit's own extractor against
`C:/projects/incms/main`: 6,168 tracked files, 626 `.ts` and 572 `.tsx`, no pattern set for either,
armed coverage 1,190 files or 19.3%. This unit produces a DECISION with the evidence beside it and
the consequence written down, so the next session meets a ruling instead of an absence.

## 2. Scope (IN)

- **S1** — state the hole as measured, on the record: the file counts, the armed-coverage fraction,
  and the mechanism that produces the darkness silently (`scaffold_lexicon.py:34,62`).
- **S2** — price the three live options against stated criteria: coverage bought, vocabulary armed
  over an unmeasured corpus, the cost of retreat, and what an adopter is told on day one.
- **S3** — write the decision, with the consequence stated in plain words rather than implied by a
  missing table row.
- **S4** — record it where a reader meets it: `tools/lexicon/LEXICON.md` and the kit README gain the
  ruling and its revisit condition, so an absent `PATTERN_SETS` entry reads as a decision and not as
  an oversight. This is the only file change the unit makes.
- **S5** — hand the resulting armed-coverage figure to `TOOL-dScaffoldedMirror-6`, which owns the
  coverage floor and the `LANGS` mode ratchet. This unit supplies the number; it does not design the
  floor.

## 3. Non-goals (OUT)

- **No lexer.** `WHAT NOT TO BUILD` kills it by name and the objection is ORDER, not cost. Nothing
  in the measurement moved that objection, so reopening it here would be a §8 fork with the killing
  argument quoted — and it is not one.
- **No `PATTERN_SETS` entry, no regex probe set, for either extension.** That is the option this
  unit weighs and refuses; refusing it is the deliverable.
- **No casing predicate and no arming of P1 over TypeScript.** Both are in `WHAT NOT TO BUILD`, and
  the 1,072 PascalCase React bindings on incms are the measured reason.
- **No measurement of incms's TypeScript naming corpus.** That measurement is the precondition the
  research pass names for revisiting the lexer, and performing it here would be the lexer's first
  half wearing a decision unit's clothes.
- **No coverage floor.** `-6` owns it. This unit's output is an input to it.
- **The kit is not adopted on incms.** Deciding what the kit says about `.ts` is a different act from
  installing it there, and the second one is nobody's unit yet.

## 4. Design

### The hole, and why it is silent

`PATTERN_SETS` (`lexicon.py:96-108`) ships exactly one set, `js-regex`. `scaffold_lexicon.py:34`
declares `KNOWN = {"py": ("python-ast", "parser"), "js": ("js-regex", "probe")}` and line 62 seeds
every other present extension as `<ext>::dark`. So an incms adoption gets `ts::dark tsx::dark`
written into its own `.lexicon.conf` by the tool, on the first run, with no refusal and no note. The
gate then prints `lexicon OK` over 19.3% of the tree. The darkness is not a gap someone failed to
close; it is a value the scaffold wrote and nobody read.

### The three options, priced

| option | coverage bought | vocabulary armed | retreat |
|---|---|---|---|
| regex probe, incomplete | +1,198 files, 19.3% → ~38.7% | P1 over an unmeasured corpus | weakening |
| real lexer | same files, better fidelity | same, plus P4/P7 pressure | weakening, plus a deletion |
| named refusal | none | none | strengthening |

"Cost of retreat" is directional under `-6`'s `parser > probe > dark` ratchet: leaving a probe means
arguing a weakening move in place, while arming a dark extension later needs no justification at
all. The adopter is told, respectively, "we partly grade your TypeScript", the same, and "we do not
read TypeScript — wire your own linter".

Three things decide it, and none of them is compute.

**The order objection did not move.** The research killed the lexer because it would arm a casing
rule over 1,072 PascalCase React components and a synonym predicate over a TypeScript corpus nobody
has measured, and because its conformance fixture round-trips through its own reading — the P3
tautology this kit has already recorded once. A regex probe inherits every one of those, minus the
fidelity, plus a second failure mode of its own.

**The kit's one existing probe set is the argument against a second.** `js-regex` is why
`TOOL-dScaffoldedMirror-2` exists: `.js` reports a healthy population of 89 while P2 grades zero
classes behind it, and the run says `lexicon OK`. That is one probe set over 10 files producing a
vacuity the kit could not see. A second probe set over 1,198 files, landed before the first one's
reporting defect is repaired, multiplies a failure mode instead of closing one.

**The retreat is asymmetric and the refusal is the reversible half.** Under `-6`'s mode ratchet
`parser > probe > dark`, going `dark` → `probe` later is a strengthening move that needs no
justification; going `probe` → `dark` is a weakening one that must be argued in place. Shipping the
probe first is choosing the harder direction of travel for the option with the weaker evidence.

### The decision, and the consequence stated

**`.ts` and `.tsx` are declared dark, deliberately, and the kit says so.** The consequence, written
rather than implied: on a repo of incms's shape this kit grades 19.3% of tracked files, reports that
fraction on every run, and has no opinion whatsoever about the naming of the other 80.7%. The
compensating documented check is the one the research already assigned to the casing predicate — the
adopter wires its own language's linter (`@typescript-eslint/naming-convention`, `eslint camelcase`),
which is an installed one-liner with better coverage than a stdlib re-implementation will have. An
exemption is not coverage, so that sentence lands in `LEXICON.md` beside the ruling and not in a
commit message.

This is the same answer the kit already gives `.sh`, which is THIS repo's largest source population
by file count — 82 tracked files against 44 `.py`, roughly 518 definitions, dark by one token in one
string. Answering `.ts` differently from `.sh` would need a reason, and there is not one.

### The revisit condition, named so it can be met

Stated as a test rather than a mood, and taken verbatim from the research pass so it cannot drift:
revisit after `-8` lands, and only with conformance fixtures extracted from real adopter files
rather than authored by the lexer's own author. Until both hold, an entry in `PATTERN_SETS` for
either extension is a reopening of a decision this record closes.

### The edge to `-6`, which is NEW and is stated on both sides

`-6` declares a coverage floor and reds below it. This unit fixes the number an adopter of incms's
shape will show against that floor at 19.3%, which means the floor's declared value determines
whether the kit is adoptable there at all. That edge is not in the build's stated dependency set and
is flagged here as NEW: `-13` does not block `-6` and `-6` does not block `-13`, but `-6` cannot
choose its floor without this ruling, and this ruling is what makes the floor's value a decision
rather than an arithmetic accident. `-6` owns the floor mechanism; nothing about it is designed here.

### Alternatives rejected

- **Leave it undecided and let the scaffold keep writing `ts::dark`.** That is the status quo, and
  the status quo is a value written by a lookup table that no record explains. The next session
  reads an absent `PATTERN_SETS` row as an oversight and re-proposes the lexer, which is the loop
  this unit exists to end.
- **Refuse to scaffold at all on a repo whose majority language is unsupported.** It converts a
  measured 19.3% into zero adopters by construction, and the kit's live adoption count is already
  one.

### Files touched (estimate)

`tools/lexicon/LEXICON.md` and `tools/lexicon/README.md` — the ruling, the consequence, the
compensating check and the revisit condition. No Python changes, so `PATTERN_SETS`, `LANGS` parsing
and every predicate are byte-identical afterwards. One build-record decision paragraph.

## 5. Production-readiness checklist

- **security** — N/A. No code path changes; no input is newly read.
- **perf / scale** — N/A by construction: refusing to add an extractor is the only option in §4 with
  zero compute cost, and saying so is not the argument for it.
- **a11y** — N/A. A CLI kit and its documentation.
- **i18n** — N/A.
- **error / empty / loading states** — the empty state IS the subject. A dark extension yields an
  empty graded population, and the whole ruling is that the emptiness must be VISIBLE and explained
  rather than inferred from a missing row.
- **observability** — the armed-coverage fraction is what makes this ruling auditable, and it is
  printed by `-6`. Without that print, this decision is a paragraph nobody can check against the
  tree; with it, a drift from 19.3% is a signal.
- **risks** — the real risk is that a documented refusal reads as coverage to somebody skimming the
  kit README. Mitigated by stating the percentage, not the word: "grades 19.3% of tracked files on a
  repo of this shape" cannot be misread the way "TypeScript: not supported" can.
- **testing + left-shift gates** — no new arm, and that is honest rather than convenient: there is
  no code to regress. The gate against re-litigation is the written revisit condition, which is a
  documented check and not a machine one.
- **migration / rollback** — N/A. Nothing is migrated; the decision is reversible by meeting the
  revisit condition, which is the point of writing it as a test.
- **user docs** — S4 is the user doc. It is the deliverable, not a follow-up.

## 6. Acceptance criteria

- **AC1** — When `tools/lexicon/LEXICON.md` is read after this unit, it states that `.ts` and `.tsx`
  are dark by decision, gives the `19.3%` armed-coverage figure and the corpus it was measured on,
  and names the compensating check. A reader who has never seen this build learns all three from the
  kit alone.
- **AC2** — When `tools/lexicon/README.md` is read, it carries the revisit condition as a test
  (`-8` landed, fixtures extracted from real adopter files), so a future `PATTERN_SETS` entry has a
  bar to clear rather than an opinion to overcome.
- **AC3** — When the unit lands, `git diff --stat` names no `.py` file under `tools/lexicon/`, and
  `python tools/lexicon/lexicon.py --measure` prints the same three pin lines as at base `9ddcc5c9`.
- **AC4** — When `python tools/lexicon/lexicon.py` runs on this worktree, its coverage line still
  reports `.sh=dark` and no `.ts` entry at all, because this repo tracks zero `.ts` files — verified
  2026-08-24 with `git ls-files`. The ruling is about what an ADOPTER gets, and this repo cannot
  observe it.
- **AC5** — When `-6` declares its coverage floor, the record it cites for the adopter figure is
  this spec, and the number is `19.3%`. A floor chosen without a cited source is the number-in-prose
  defect this build keeps finding.

## 7. Gates

Keeps green: `lexicon naming predicates`, `lexicon selftest`, `lexicon wiring`, `memory hygiene`,
and `kit/dogfood doc parity` — the last one because S4 edits shipped kit documentation, which is
exactly the population that leg grades. Adds no leg.

**What this unit does NOT check.** Nothing, mechanically. It changes no predicate, arms nothing, and
adds no refusal. A green bar after it proves only that the documentation edits did not break a
parity gate; the ruling itself is enforced by a written revisit condition, which a future session
can ignore. That is the honest limit of a decision unit and it is stated rather than dressed up.

## 8. Open questions

- **F1 — regex probe, real lexer, or a named refusal for `.ts`/`.tsx`?** The three are priced in §4.
  RECOMMENDATION: the named refusal. The research pass's order objection is unchanged by the
  measurement, the kit's single existing probe set is the live evidence that a probe set can report
  a healthy population over a graded set of zero, and `dark` → `probe` is the cheap direction to
  travel later while `probe` → `dark` is the expensive one. A named refusal is also what the kit
  already does for this repo's own largest source population. RESOLVED (agent, 2026-08-24,
  delegated): named refusal, with the 19.3% consequence and the compensating linter check written
  into `LEXICON.md`, and the revisit condition stated as a test.
- **F2 — does gov's opinion about `.ts` bind an adopter that wants coverage sooner?** An adopter can
  write its own `PATTERN_SETS` entry today; nothing in the kit prevents it. RECOMMENDATION: say so
  explicitly in the README rather than leaving the refusal reading as a prohibition — the kit
  declines to SHIP a TypeScript extractor and does not decline to run one. RESOLVED (agent,
  2026-08-24, delegated): stated as a permission in the README, one sentence.
- **F3 — does the lexicon kit get adopted on incms at 19.3% armed coverage, or does adoption wait?**
  Genuinely the owner's, and left UNRESOLVED. It depends on `-6`'s floor, which does not exist yet,
  and on whether the owner wants a real adopter more than a high coverage number.
  RECOMMENDATION: adopt at 19.3% with the fraction printed. One adopter grading a fifth of a tree
  produces more evidence than zero adopters grading nothing, and this build's entire diagnosis came
  from measuring rather than from waiting.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, grounded on the `dScaffoldedMirror` research pass
  (`build/2026-08-24-build-TOOL-dScaffoldedMirror-2-lexicon-usefulness-research.md`, demand 3 and
  the `WHAT NOT TO BUILD` entry on a kit-owned JS/TS lexer) and on the read-only probe of
  `incms/main` taken the same day, which supplied the 6,168 / 626 / 572 / 19.3% figures.
- rev-1 status 2026-08-24 · DEFERRED, and the recommendation is to SHRINK it to two sentences in `LEXICON.md` rather than build it: 228 lines for a decision whose headline fork - adopt on incms - it leaves unresolved. The ruling is worth keeping; the spec is not.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py typescript extension pattern coverage extractor dark`
returns `extract` (`tools/lexicon/lexicon.py`, fan-in 9, SEAM) and `compute_coverage`
(`tools/codebase-map/map_lib.py`, fan-in 4, SEAM). **No existing seam fits, and the evidence is that
both hits are seams this unit deliberately declines to touch.** `extract()` is the dispatch point a
new `PATTERN_SETS` entry would wire through — it is the correct seam for the option being REFUSED,
which is the clearest possible signal that the refusal is the whole unit. `compute_coverage` belongs
to the codebase-map kit and computes dossier coverage over inventory keys, sharing the word and
nothing else; the lexicon's own coverage line is built inline in `run()` and is `-6`'s subject in any
case. The lookup also flagged that its `layers bash` corpus has no symbol extractor, which is the
same class of blindness this unit is ruling on one language over — noted, and not a seam either. The
only files this unit edits carry prose, and prose has no seam.
