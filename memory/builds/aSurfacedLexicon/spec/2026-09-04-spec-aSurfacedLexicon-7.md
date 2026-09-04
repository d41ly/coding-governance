# TOOL-aSurfacedLexicon-7 — P1 splits into DEBT and UNRULED, and DEBT names its replacement

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Split the P1 verb population into DEBT (the canon can name a replacement) and UNRULED (it cannot),
pin both, and wire the offender line and `--suggest` to `canon.build_form_index()` so a debt offender
actually names the rename it owes. The kit refuses without advising today, and a gate that says no and
nothing else gets waived rather than obeyed.

## 2. Scope (IN)

- **S1** — Classify every P1 offender against `canon.build_form_index()` at grade time. An offender
  whose leading token is a key of that index is DEBT; one that is not is UNRULED. The classification
  is computed once, in the corpus walk, and both the report and the pins read it.
- **S2** — The offender detail line, today `lexicon.py:581`
  (`leading token {verb!r} is not in the declared VERBS table`), gains a canon-backed second half for a
  DEBT offender: the representative and its `canon.read_gloss()`. An UNRULED offender keeps the
  existing wording and gains its per-token site count, because 184 of the 258 distinct unruled tokens
  occur exactly once and a reader needs to know which side of that line a token sits on.
- **S3** — `run_suggest` (`lexicon.py:785-852`) consults `canon.build_form_index()` and
  `canon.read_gloss()` when `build_banned_index(conf)` does not carry the offending token. The conf's
  own inverted NOT clauses keep priority: a declaration that bans a token by name outranks the canon,
  because the owner wrote the negative and the canon did not.
- **S4** — P1 emits two pin rows per armed `vocab` cell, `<ext>.function.debt` and
  `<ext>.function.unruled`, in place of the single `VERB_OFFENDER_PIN` scalar. The `PINS:` block
  grammar itself is `TOOL-aSurfacedLexicon-4`'s; this unit is its first consumer and declares only the
  two row keys and their values.
- **S5** — `--measure` emits both rows for every armed cell, so the pins stay measured rather than
  chosen.
- **S6** — The green and red report lines carry the two counts separately, and their sum, so a reader
  can see that the split moved no verdict.

## 3. Non-goals (OUT)

**The split narrows nothing.** Owner ruling Q1 of 2026-09-04 keeps both populations pinned, so the
gate's reach is unchanged at 461 P1 offenders and no name that reds today greens tomorrow. This unit
is a reporting and advice improvement and is not an enforcement change. Anyone reading the diff and
concluding the unruled population was released has read it wrong.

Also out: the `--as <cell>` surface argument and the convention re-casing, which are
`TOOL-aSurfacedLexicon-8`. The owner-declarable canon overlay and its stamp, which are
`TOOL-aSurfacedLexicon-11`. Draining the 43 debt definitions by renaming them, which is its own unit
and not a precondition for this one. Widening `VERBS` to absorb an unruled token, which is
`TOOL-aSurfacedLexicon-10`'s `--expand` and is bounded by the canon there for the reason
`tools/lexicon/canon.py:19-21` states.

## 4. Design

### Data model

`canon.build_form_index()` returns `{surface form: representative}` over all 20 clusters, each
representative mapping to itself (`tools/lexicon/canon.py:84-95`). One membership test against that
dict is the whole classifier. A P1 offender is a definition whose `leading_verb(name)` is truthy and
absent from the declared `VERBS` table; DEBT is that set intersected with the index's keys, UNRULED is
the remainder.

Measured on this worktree at writing time, over the tree at `cd8ab0d2`:

| Fact | Value |
|---|---|
| P1 graded | 1047 |
| DEBT definitions | 43 |
| UNRULED definitions | 418 |
| Sum | 461 |
| Distinct DEBT tokens | 23 |
| Distinct UNRULED tokens | 258 |
| UNRULED tokens with exactly one site | 184 |
| DEBT tokens `--suggest` names a replacement for today | 5 |
| DEBT definitions those 5 cover | 7 |

Reproduced by a scratchpad script importing `lexicon.extract`, `lexicon.leading_verb`,
`canon.build_form_index` and `lexicon.build_banned_index` over `lexicon.tracked_files(root)`; every
figure above agrees with the research record's own measurement of the same population.

The five tokens are `append`, `compute`, `log`, `search` and `validate`. They are the only DEBT
tokens this repo's declaration happens to name in a NOT clause, which is why the advice half works
for them and for nothing else.

### Inventory

The load-bearing verified fact: `canon` is imported at `tools/lexicon/lexicon.py:84` and its only three
code references are at `:1065`, `:1101` and `:1114`, all inside `run_probe`, whose AST span is
`:1053-1136`. `run_suggest` at `:785-852` reads `load_conf`, `verbs`,
`leading_verb` and `build_banned_index` and never touches the canon. `build_banned_index` at `:771-782`
inverts `build_negatives(conf)`, which is the declaration's own NOT clauses and nothing else. So the
claim that DEBT is the class where the kit can name the fix is false as shipped for 36 of the 43
definitions, and the fix is a two-line graft into a function that already resolves the same question
one source short.

`run_probe` is deleted by `TOOL-aSurfacedLexicon-3`. This unit must not inherit its call site as the
only canon reader, or the graft lands and dies in the same build.

### Migration

`VERB_OFFENDER_PIN="461"` retires in favour of two rows summing to 461. The retirement is a conf edit
and lands with `TOOL-aSurfacedLexicon-12`'s conf rewrite. Until that lands, this unit reads the pair
from the `PINS:` block when present and falls back to the scalar, so it is independently landable and
the bar stays green between the two commits.

### Files touched (estimate)

`tools/lexicon/lexicon.py` (the classifier, the offender line, `run_suggest`, the report lines),
`tools/lexicon/selftest.py` (arms), `.lexicon.conf` (the two pin rows). No new module: `govkit update`
classifies by iterating the receipt at `tools/govkit/govkit.py:5718`, so a file gov newly ships is
outside the classification space, and this unit adds none. ESTIMATE, and it is an estimate because
nothing comparable ships to measure against.

### Alternatives rejected

Merging the two populations into one pin and reporting the split only in prose. Rejected because a
single bucket over two populations is why `VERB_OFFENDER_PIN` moved eleven times and produced no
renames from the second population; the values it ever carried are 384, 412, 415, 417, 450, 452, 455,
458, 460, 461 and 463 twice, per the research record's `git log -p --follow` over `.lexicon.conf`.

Deriving DEBT from the declaration's NOT clauses alone rather than from the canon. That is what ships
today and it is exactly the 5-of-23 result. The declaration's negatives are one alternative per row
(`canon.render_negative` emits `others[0]`), while a cluster carries up to eight.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path, no new egress; the canon is a frozen in-kit tuple.
- perf / scale — one dict membership test per already-extracted definition, inside the existing walk.
  The `lexicon naming predicates` leg ceiling of 300 s in `tools/gate-legs.json` is unchanged and the
  unit adds no second corpus pass.
- a11y — N/A. A stdout report on a gate leg has no rendered surface.
- i18n — N/A here, but see the risks line: `subtokens.py` is ASCII-only and the gap is filed, not fixed.
- error / empty / loading states — a repo whose declaration carries every canon representative has an
  empty DEBT population; the report prints `0` with its denominator rather than omitting the row.
- observability — both counts print on GREEN as well as RED, keeping `lexicon.py:710-716`'s rule that
  a green row is a measurement or it is a mood.
- risks — the classification changes what a pin COUNTS, so a stale single scalar read against the new
  pair would silently pass. The fallback in Migration is the mitigation and it is temporary by design.
- testing + left-shift gates — arms in `tools/lexicon/selftest.py` for each of the three advice paths
  and for the classifier boundary; the observed-RED criterion is AC5.
- migration / rollback — reverting is a single-commit revert; the conf keeps the scalar until
  `TOOL-aSurfacedLexicon-12` removes it.
- user docs — `tools/lexicon/README.md` gains the DEBT/UNRULED vocabulary. The rendered Skill's
  routing line is `TOOL-aSurfacedLexicon-8`'s edit, not this unit's.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --suggest ensure_cache` runs, it names `check_cache`
  and the `check` gloss. Today it prints ``` `ensure` is not in the declared table ```, verified by
  direct run at writing time.
- **AC2** — When `--suggest require_adopted_root` and `--suggest walk_file_keys` run, they name
  `check_adopted_root` and `scan_file_keys`. Both are silent today, verified by direct run.
- **AC3** — When `--suggest append_row` runs, it still answers `add_row` from the declaration's own NOT
  clause rather than from the canon, proving the conf keeps priority over `canon.build_form_index()`.
- **AC4** — When `python tools/lexicon/lexicon.py --check` runs on an unmodified tree, it prints a
  `debt` count of 43 and an `unruled` count of 418 for `py.function`, and their sum equals the 461 the
  single `VERB_OFFENDER_PIN` carries today.
- **AC5** — When a definition named `def ensure_thing():` is staged into a tracked `.py` file,
  `lexicon.py --check` exits 1 with that line classified DEBT and naming `check_thing`; when it is
  unstaged the leg returns to its baseline. The RED is observed before this unit is called done, per
  the build README's rule.
- **AC6** — When a definition named `def demand_thing():` is staged, the same run classifies it UNRULED
  and proposes no replacement, because `demand` is in no cluster. The two messages are textually
  distinct, so a reader can tell a rename from a scoping question.
- **AC7** — When `python tools/lexicon/lexicon.py --measure` runs, it emits `py.function.debt 43` and
  `py.function.unruled 418` as `PINS:` rows, and pasting its output into `.lexicon.conf` leaves
  `--check` green.
- **AC8** — When `tools/lexicon/selftest.py` runs under `GATE_SELFTESTS=1`, an arm asserts that every
  key of `canon.build_form_index()` classifies as DEBT and that a token absent from it classifies as
  UNRULED, so the classifier cannot silently collapse to one bucket.

## 7. Gates

`lexicon naming predicates` (chunk `declarations`, subject `repo`, ceiling 300) is the leg that
carries the verdict and the one the push bar runs. `lexicon selftest` (chunk `selftests`, subject
`kit`, ceiling 880) carries the arms and is invisible to the push boundary unless `GATE_SELFTESTS=1`
is set, which no boundary sets — so an arm added here is on-demand coverage and the spec says so
rather than implying a push-time guarantee. `lexicon wiring` (guard `[]`, ceiling 330) fires on a
conf-only diff and must stay green across the pin-row change. `memory-tree hygiene` grades this spec.
No new gate leg, so no new `testsuite-count-waivers.txt` row and no new wall-clock ceiling is owed.

## 8. Open questions

- **F1 — Keep the UNRULED population pinned, or stop gating it?**
  RESOLVED (owner, 2026-09-04): keep both pinned. The sum stays 461 and the split costs no enforcement
  reach.

- **F2 — When the canon's representative for a DEBT token is not itself a declared `VERBS` row, does
  the offender line propose it anyway?**
  Measured on this repo at writing time: all 20 canon representatives are declared, so the fork has an
  empty population HERE and cannot be decided by observation on this tree. It is not empty for an
  adopter, whose table is a subset of the canon by construction after `--scaffold` seeds only the
  clusters with a live site. Proposing a representative the declaration does not carry hands the author
  a name the gate reds on the next run, which is the same defect `TOOL-aSurfacedLexicon-8` exists to
  close one surface over. Recommendation: propose it, and mark the line explicitly as a name that also
  needs its `VERBS` row, because suppressing the advice leaves the author with a refusal and nothing
  else, which is the defect this unit exists to fix.

- **F3 — Does an UNRULED offender's per-token count come from this cell or from the whole corpus?**
  A token with one site in `py` and four in `js` reads differently under the two. Per-cell keeps every
  number in the report answerable from the row it sits on; corpus-wide is the number an author renaming
  actually wants. Recommendation: per-cell in the row, corpus-wide in the `--list` detail, because the
  pins are per-cell and a row whose count does not reconcile with its own pin is unreadable.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Numbers re-measured on this worktree rather than inherited from
  the research record; the record's own figures reproduced exactly.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "canon form index backing the offender advice and the
suggest verb"` returned `build_form_index [function | tools/lexicon/canon.py | fan-in 3 | SEAM]` as a
ranked candidate, alongside `leading_verb [tools/lexicon/subtokens.py | fan-in 4 | SEAM]` and
`run_suggest [tools/lexicon/lexicon.py | fan-in 0]`. That is the seam this unit extends: the fan-in-3
form index already exists and already answers the exact question the offender line and `--suggest` are
failing to ask it. Nothing new is built to resolve a spelling; one existing seam gains two callers.
The `fan-in 0` on `run_suggest` is the second half of the finding — it is a leaf that resolves the
same question from a strictly smaller source.

Recall terms used: `python tools/memory-recall/query.py "why does the lexicon offender report name no
replacement for a debt spelling" --terms "lexicon canon cluster representative debt offender suggest
replacement verb table mirror anti-mirror pin"` — 36 hits, top records
`TOOL-dScaffoldedMirror-8` (the corpus votes to exclude, never to select) and the rebuild research
record's own MODIFY row for P1.
