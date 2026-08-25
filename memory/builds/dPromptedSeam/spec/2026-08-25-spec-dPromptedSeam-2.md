**Serves:** spec TOOL-dPromptedSeam-2

# TOOL-dPromptedSeam-2 — `read_object` returns nothing usable for a third of the corpus

**Status:** OPEN · rev-2 · 2026-08-25 · node d · Tier-1 · base 671e953d · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`read_object()` is the lexicon's own helper for reducing an identifier to the concept it names, and
`--brief` uses it to surface "one concept spelled two ways in two kits". Measured against this
corpus it returns nothing usable for roughly a third of identifiers, which silently narrows the only
drift class `--brief` claims to measure. Fix the helper. This unit is independent of
`TOOL-dPromptedSeam-1` and should land first.

## 2. Scope (IN)

- **S1 — a stopword-aware verdict.** `read_object` gains a notion of whether its result has any live
  stem, so a caller can tell "no object" from "an object made entirely of stopwords". Today both
  return a string a caller treats as usable.
- **S2 — a full-identifier fallback for the single-token case.** When an identifier has no object at
  all — every single-token type name — the helper reports that fact rather than an empty string, so
  a caller can fall back to the whole identifier instead of giving up.
- **S3 — `--brief` consumes the distinction.** Its object listing separates gradeable objects from
  identifiers with none, rather than silently dropping the second group from its report.
- **S4 — arms over the measured population**, not over hand-picked names: the stopword cases, the
  single-token cases, and a control proving a normal identifier is unaffected.

## 3. Non-goals (OUT)

- **No change to P1, P2 or P3 grading.** `leading_verb` is untouched; this is about the OBJECT half,
  which no predicate reads.
- **No stopword list of this kit's own.** `map_lib.stems()` already declares one, and a second list
  is the class this repo names. The helper asks whether a stem survives rather than re-deciding what
  a stopword is — and since the lexicon may not import `codebase-map`, the shipped shape is the
  minimal inline set with its provenance recorded, not a copy that pretends to be authoritative.
- **No cross-kit call.** Same layer ban as `-1`.
- **No pin movement.** Object extraction feeds no pin.

## 4. Design

**D1 — the measured population, because the numbers ARE the design.** Over 231 off-table symbols in
this corpus: 68 (29%) yield no object at all, all of them single-token type names — `Candidate`,
`Corpus`, `Dossier`, `Refusal`. A further 15 yield objects that are entirely stopwords: `pin_of` →
`of`, `fan_in` → `in`, `ext_of` → `of`, `boundedK` → `k`. That is a third of the population for
which the helper's answer is unusable and indistinguishable from a usable one.

**D2 — the fallback is the FULL IDENTIFIER, and it was measured before being specced.** For the 68
empty-object cases, querying the whole identifier surfaces a non-self match in 51 (75%): `Dossier` →
`parse_dossier` and `load_dossier_texts`, `Conf` → `load_conf`, `Coverage` → `compute_coverage`. For
the 15 stopword-dead cases it recovers 12: `cache_of` → `build_cache`. The fallback is not a guess.

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

- **AC1** — When `python tools/lexicon/lexicon.py --brief tools/codebase-map/reuse_lookup.py` runs,
  its report separately names the identifiers that yield no gradeable object, and that group is
  non-empty for this file — proving the split is reached rather than merely coded.
- **AC2** — When the helper is asked for `pin_of`, `fan_in` and `boundedK`, it reports each as having
  no live stem, and when asked for `build_index` it reports `index` as live. One arm cannot pass
  without the other failing on a broken helper.
- **AC3** — When the stopword-awareness is reverted in a scratch copy, `python tools/lexicon/selftest.py`
  reds naming the stopword arm; the clean tree reds nothing.
- **AC4** — When `python tools/lexicon/lexicon.py --check` runs, `P1 verb`, `P2 suffix` and `P3 layer`
  report the same graded and offender counts as at base `671e953d`, proving no predicate moved.

## 7. Gates

Rides `lexicon selftest` and `lexicon naming predicates`. Adds no leg. Note that `lexicon selftest`
is `subject = "kit"` and therefore HELD unless `GATE_SELFTESTS=1` — so S4's arms are on-demand
coverage, not every-bar coverage, and this line says so rather than letting §7 read as more than it
is.

## 8. Open questions

- **Q1 — does the stopword set live in the lexicon or come from the caller?** RESOLVED by the layer
  ban: the lexicon cannot read `map_lib`. It ships a minimal inline set whose provenance is recorded
  in the docstring, and the docstring states that `map_lib.stems()` is the larger authority the kit
  deliberately cannot reach.
- **Q2 — should `--suggest` use the fallback too?** RESOLVED (agent, 2026-08-25, delegated): NO.
  `--suggest` has no lookup to feed, so the fallback would be a code path with no consumer — "delete
  over disable" applies before it is written rather than after. The option also leaves MORE open than
  its rival, which is M3's tie-break running the other way. It acquires a consumer only if `-1`
  changes shape, and `-1`'s own Q2 is now resolved against that.

## 9. Revision log

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
