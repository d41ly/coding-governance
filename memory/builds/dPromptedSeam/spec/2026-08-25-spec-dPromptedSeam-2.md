**Serves:** spec TOOL-dPromptedSeam-2

# TOOL-dPromptedSeam-2 — `read_object` cannot say WHY it returned nothing

**Status:** WONTDO · rev-4 · 2026-08-25 · node d · Tier-1 · base 671e953d · streams tooling · superseded by TOOL-dPromptedSeam-3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-review-TOOL-dPromptedSeam-1-2-3-diff-review-round-1.md](../reviews/2026-08-25-review-TOOL-dPromptedSeam-1-2-3-diff-review-round-1.md) | diff-review | TOOL-dPromptedSeam-1 TOOL-dPromptedSeam-3 |
| [2026-08-25-review-TOOL-dPromptedSeam-1-2-3-diff-review-round-2.md](../reviews/2026-08-25-review-TOOL-dPromptedSeam-1-2-3-diff-review-round-2.md) | diff-review | TOOL-dPromptedSeam-1 TOOL-dPromptedSeam-3 |
| [2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-1.md](../reviews/2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-1.md) | spec-audit | TOOL-dPromptedSeam-1 |
| [2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-2.md](../reviews/2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-2.md) | spec-audit | TOOL-dPromptedSeam-1 |

<!-- /gen:spec-records -->

## 1. Goal

`read_object()` reduces an identifier to the concept it names, and `--brief` uses it to surface "one
concept spelled two ways in two kits". It returns the empty string for two DIFFERENT reasons and its
one caller cannot tell them apart: an identifier with no object at all, and an object whose every
token is dead to the stemmer. `--brief` filters on truthiness, so both vanish from its report and the
only drift class it claims to measure is silently narrowed by both. Make the two states
distinguishable and let `--brief` say which. This unit is independent of `TOOL-dPromptedSeam-1`.

## 2. Scope (IN)

- **S1 — the liveness predicate is TWO rules, and both are stated.** A token is dead when it is in
  the inline stopword set OR is shorter than two characters. Both, not one: `boundedK` yields the
  object `k`, and `k` is NOT a stopword — `map_lib._STOPWORDS` is 21 words and holds no single
  letters, which drop by a separate length test. rev-2 authorised only "a stopword-aware verdict"
  while its own AC2 demanded `boundedK` be reported dead, so an implementer shipping exactly what
  the scope allowed would have redded the acceptance criterion. STEMMING IS OUT: this asks whether a
  token survives, never what it stems to.
- **S2 — the return contract is UNCHANGED, and the companion carries the verdict.** `read_object`
  keeps returning the same string it returns today, empty included. A companion reports which of the
  three states produced it: an object with a live stem, an object whose tokens are all dead, or no
  object at all. rev-2 said the helper would report "rather than an empty string", which contradicted
  its own D3 and would have pushed every empty-object name into `--brief`'s listing through the
  truthiness filter at `lexicon.py:916`.
- **S3 — `--brief` consumes the distinction, and its truthiness filter goes.** `lexicon.py:916`
  currently selects on the truthiness of the return, which is what collapses the three states into
  one. It is replaced by an explicit branch on the companion's verdict, so the report separates
  objects that are usable, objects whose tokens are all dead, and identifiers with no object — a
  deliberate output change owned by THIS scope item rather than a side effect of the helper.
- **S4 — arms over the measured population**, not over hand-picked names: a stopword case, a
  minimum-length case (`boundedK`, which the stopword set alone does not catch), a no-object case,
  and a control proving a normal identifier still reports its object as usable. The control is what
  stops four absence-shaped arms passing over a helper that reports everything dead.

## 3. Non-goals (OUT)

- **No change to P1, P2 or P3 grading.** `leading_verb` is untouched; this is about the OBJECT half,
  which no predicate reads.
- **No SECOND authority on what a stopword is.** The lexicon may not import `codebase-map`, so it
  cannot call `map_lib.stems()` and must carry its own list — which S1 enumerates rather than
  gestures at, because the membership IS the contract and rev-2 left it unwritten. The docstring
  records that `map_lib._STOPWORDS` (21 words) plus a two-character minimum is the shape being
  restated and why the ban forbids importing it, so the next reader does not "fix" it by importing.
- **No cross-kit call.** Same layer ban as `-1`.
- **No pin movement.** Object extraction feeds no pin.

## 4. Design

**D1 — RE-MEASURED over the population the code actually sees, because rev-2's was not it.**
`read_object` is called at `lexicon.py:916` and `:936`, both over `got[0]` — FUNCTIONS. rev-2 measured
231 off-table symbols and described the empty cases as "all of them single-token type names", naming
`Candidate`, `Corpus`, `Dossier`. Not one of those is a function, so none was ever in the population.
Re-measured over all 644 tracked function definitions: **129 (20.0%) yield no object at all** — and
they are single-token FUNCTION names, `__init__`, `__str__`, `_bind`, `_budget` — while **16 (2.5%)**
yield an object with no live stem: `_scalar_at` → `at`, `_token_of` → `of`, `anchor_at` → `at`. So
145 of 644, 22.5%, not "a third", and the characterisation was wrong as well as the count.

**D2 — THE FALLBACK IS CUT, and cutting it is the whole simplification.** rev-2 proposed falling
back to the full identifier and priced it on a lookup this kit does not perform: `--brief` has no
corpus query to feed, `--suggest` was resolved against one at §8 Q2, and the cross-kit call that
would have consumed it was withdrawn from `-1`. A mechanism with no consumer is dead code, and its
supporting measurement was taken over the wrong population anyway. What survives is smaller and
every one observable: make the three states distinguishable, and let `--brief` report them. A fallback
acquires a consumer only when something in this kit performs a lookup, and that is a later unit.

**D3 — the helper REPORTS, it does not decide.** `read_object` keeps returning a string and gains a
companion that says whether that string has a live stem. Callers choose what to do. Folding the
fallback into the helper would make one function answer two questions and would change `--brief`'s
output without `--brief` asking.

**D4 — self-matches are excluded by the CALLER.** An identifier being renamed is already in the
corpus and ranks itself; `assemble_shortlist` returning `assemble_shortlist` for the object
`shortlist` is measured behaviour. That filter belongs wherever a lookup happens, which is not this
helper.

## 5. Production-readiness checklist

- **security** — N/A. Pure string function.
- **perf / scale** — N/A. Same single pass over `subtokens` output.
- **a11y** / **i18n** — the ASCII limit in `subtokens` is untouched and remains
  `TOOL-dScaffoldedMirror`'s carried finding; this unit does not widen or narrow it, and says so
  rather than appearing to fix it.
- **error / empty / loading states** — the two states this unit exists to separate ARE this line.
- **observability** — `--brief` prints the split, which is the only surface.
- **risks** — low. The helper has two callers today, both in-kit.
- **testing + left-shift gates** — S4, on `lexicon selftest`. Each arm staged to fail against the
  code it guards, and the control arm is what stops a suite of absences passing on a broken helper.
- **migration / rollback** — none.
- **user docs** — `LEXICON.md`'s `--brief` description gains one sentence.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --brief tools/lexicon/lexicon.py` runs, its report
  names all THREE groups separately, and the no-object group is non-empty for this file — which it
  is, since `lexicon.py` defines `_main` and other single-token functions. A report naming two groups
  passes rev-2's wording and fails this one.
- **AC2** — When the helper is asked for `pin_of` and `boundedK` it reports both dead, and when asked
  for `build_index` it reports `index` live. The two dead cases are dead for DIFFERENT rules —
  `of` by membership, `k` by length — so a helper implementing only the stopword half passes one and
  fails the other, which is what makes S1's two-rule statement observable rather than decorative.
- **AC3** — When the stopword-awareness is reverted in a scratch copy, `python tools/lexicon/selftest.py`
  reds naming the stopword arm; the clean tree reds nothing.
- **AC4** — When `python tools/lexicon/lexicon.py --check` runs, `P1 verb`, `P2 suffix` and `P3 layer`
  report the same graded and offender counts as at base `ee6554c3`, proving no predicate moved. The
  base is this run's, not rev-1's stale one.

## 7. Gates

Rides `lexicon selftest` and `lexicon naming predicates`. Adds no leg. Note that `lexicon selftest`
is `subject = "kit"` and therefore HELD unless `GATE_SELFTESTS=1` — so S4's arms are on-demand
coverage, not every-bar coverage, and this line says so rather than letting §7 read as more than it
is.

## 8. Open questions

- **Q1 — does the stopword set live in the lexicon or come from the caller?** RESOLVED (agent,
  2026-08-25, delegated) by the layer ban: the lexicon cannot read `map_lib`, so it ships its own,
  ENUMERATED in S1 rather than described. The docstring records `map_lib._STOPWORDS` plus the
  two-character minimum as the shape being restated and the ban as the reason it cannot be imported.
- **Q2 — should `--suggest` use the fallback too?** MOOT at rev-3: D2 cuts the fallback from this
  unit entirely, so there is nothing for `--suggest` to use. Kept in the log rather than deleted,
  because the reasoning that killed it — a mechanism with no consumer — is what the audit then
  applied to the fallback itself.

## 9. Revision log

- rev-4 · 2026-08-25 · node d · WONTDO, superseded by TOOL-dPromptedSeam-3. Spec-audit round 2
  proved this unit PREMISE-FALSE: it asserts read_object returns empty for two reasons and that
  both vanish from --brief. The function is four lines with no stopword test, no length test and no
  stemmer; it returns empty for exactly one reason, and the other case is reported loudly and
  wrongly. Retired as a status flip with a successor rather than deleted, per M2.

- rev-3 · 2026-08-25 · node d · OPEN. Spec audit round 1 returned BLOCKED; four blockers were this
  unit's. §4 D1 was measured over 231 off-table SYMBOLS and described the empty cases as single-token
  TYPE names, but `read_object` is called only over FUNCTIONS (`lexicon.py:916`, `:936`) — so the
  population was never the one the code sees, and the headline "a third" was 22.5%. Re-measured: 129
  of 644 empty, 16 stopword-dead. S1 was one rule short — `boundedK` yields `k`, which is not a
  stopword and dies by a length test the scope never mentioned while AC2 demanded it. S2 contradicted
  D3 on the return contract in a way that would have pushed every empty-object name into `--brief`'s
  listing. And the full-identifier fallback had no consumer in this kit at all, so it is CUT. The
  unit is smaller and every criterion is now observable.
- rev-2 · 2026-08-25 · node d · OPEN. §8 Q2 RESOLVED under the standing mandate: a fallback with no
  consumer is dead code, so it is refused before it is written. §10 gains the M5 recall terms.
- rev-1 · 2026-08-25 · node d · OPEN. Surfaced by the spec audit of `TOOL-dPromptedSeam-1`, which
  measured the helper's output over the real population while testing a different claim. Specced as
  its own unit because it is a defect in the lexicon's own helper, improves `--brief` today, needs no
  cross-kit anything, and is smaller than the unit that found it.

## 10. Reuse audit

- `subtokens()` (`tools/lexicon/subtokens.py`) — REUSED unchanged. This unit reads its output and
  does not re-split.
- `read_object()` — EXTENDED in place rather than replaced; its two existing callers keep working.
- `map_lib.stems()` — NOT reused, and the reason is the layer ban rather than preference. Recorded in
  the docstring so the next reader does not "fix" it by importing.

**Recall terms used**, shared with `-1` because M5 is satisfied once for the SET: `lexicon subtokens
port self-contained layers import ban codebase-map map_lib kit independence adopter reuse seam`. The
map probe's behaviour phrase was *"reduce an identifier to the concept it names, dropping the leading
verb"*, and it returned `leading_verb` as the only seam in this area — which is the sibling of the
function this unit fixes and confirms no third implementation exists to extend instead.
