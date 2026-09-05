# TOOL-aSurfacedLexicon-7 — P1 splits into DEBT and UNRULED, and DEBT names its replacement

**Status:** CLOSED · rev-3 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 5 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aSurfacedLexicon-6-acceptance-ledger.md](../build/2026-09-05-build-TOOL-aSurfacedLexicon-6-acceptance-ledger.md) | journal | TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-13 |
| [2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 |
| [2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round2.md) | spec-audit | TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 |
| [2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round1.md](../reviews/2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round1.md) | diff-review | TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 |
| [2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round2.md](../reviews/2026-09-06-review-TOOL-aSurfacedLexicon-2-diff-review-round2.md) | diff-review | TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3 TOOL-aSurfacedLexicon-4 TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-8 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-11 TOOL-aSurfacedLexicon-12 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 |

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
  existing wording and gains its per-token site count, because 201 of the 267 distinct unruled tokens
  occur exactly once and a reader needs to know which side of that line a token sits on.
- **S3** — `run_suggest` (`lexicon.py:785-852`) consults `canon.build_form_index()` and
  `canon.read_gloss()` when `build_banned_index(conf)` does not carry the offending token. The conf's
  own inverted NOT clauses keep priority: a declaration that bans a token by name outranks the canon,
  because the owner wrote the negative and the canon did not. The two sources DISAGREE on this tree
  today, which is what makes the precedence observable rather than assumed — see AC3.
- **S4** — P1 emits two pin rows for every `CELLS` row carrying the `vocab` flag,
  `<ext>.<surface>.debt` and `<ext>.<surface>.unruled`, in place of the single `VERB_OFFENDER_PIN`
  scalar. The `PINS:` block grammar itself is `TOOL-aSurfacedLexicon-4`'s; this unit is its first
  consumer and declares only the row keys and their values. **The emission is scoped to cells that
  exist**: a cell with no `CELLS` row gets no pin row, and the tracked declaration carries no `vocab`
  cell at this unit's order, so the emission over the tracked tree is EMPTY at landing. That is the
  correct result and not an inert one — §4 Migration says why, and AC4 and AC7 are observed against a
  scratch declaration rather than against a tracked block that does not exist.
- **S5** — `--measure` emits both rows for every armed `vocab` cell, so the pins stay measured rather
  than chosen, and it emits them **separated by exactly one blank line** —
  `TOOL-aSurfacedLexicon-4`'s S10 makes two `PINS` rows whose line numbers differ by one a refusal
  inside `load_conf`, and its AC5 hands this unit the obligation by name: "whichever unit emits the
  block emits it blank-separated". Order 2 is before order 5, so that refusal is live when this
  emitter first runs. A dense emission would produce bytes the reader refuses.
- **S6** — The green and red report lines carry the two counts separately, and their sum, so a reader
  can see that the split moved no verdict.

## 3. Non-goals (OUT)

**What the split PRESERVES, and what it ADDS.** Owner ruling Q1 of 2026-09-04 keeps both populations
pinned, so no name that reds today greens tomorrow and the unruled population is not released. Anyone
reading the diff and concluding otherwise has read it wrong. But this IS an enforcement change, and
rev-1 said it was not. `TOOL-aSurfacedLexicon-4`'s S9 makes the pin comparison two-sided: a count that
FALLS reds exactly as one that rises. Under a single scalar, a rename that moves an offender from
`py.function` to `js.function`, or from DEBT to UNRULED inside one cell, holds the total and greens.
Under two rows per cell the same rename reds twice, once for the fall and once for the rise. That is
strictly more reach, priced here rather than discovered on the landing bar, and AC9 is the observed
failing case the build rule owes for it.

Also out: the `--as <cell>` surface argument and the convention re-casing, which are
`TOOL-aSurfacedLexicon-8`. The owner-declarable canon overlay and its stamp, which are
`TOOL-aSurfacedLexicon-11`. Draining the 44 debt definitions by renaming them, which is its own unit
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

Measured at the status header's base, `6c670b02`. Rev-1 attributed this table to an untracked
scratchpad script and to a third sha, `cd8ab0d2`, appearing nowhere else in this build; every row but
the sum has moved since. The derivation now ships with the table, so a second reader lands on the same
figures without rebuilding anything:

```
python - <<'PY'   # run from the repo root; prints every split row of the table below
import sys, collections; sys.path.insert(0, "tools/lexicon")
import lexicon, canon
from pathlib import Path
from lexicon_conf import load_conf
from subtokens import leading_verb
conf = load_conf(".lexicon.conf")
langs = {e: (m, p) for e, p, m in (s.split(":") for s in conf["LANGS"].split())}
verbs, ix, ban = set(conf["VERBS"]), canon.build_form_index(), lexicon.build_banned_index(conf)
g, d, u = collections.Counter(), collections.Counter(), collections.Counter()
dt, ut = collections.Counter(), collections.Counter()
for rel in lexicon.tracked_files(Path(".")):
    ext = lexicon.ext_of(rel)
    if ext not in langs or langs[ext][0] == "dark":
        continue
    got = lexicon.extract(Path(rel), *langs[ext])
    for nm, _ln in (got[0] if got else []):
        g[ext] += 1
        v = leading_verb(nm)
        if not v or v in verbs:
            continue
        (dt if v in ix else ut)[v] += 1
        (d if v in ix else u)[ext] += 1
print("graded", dict(g), "| debt", dict(d), "| unruled", dict(u))
print("distinct debt", len(dt), "| distinct unruled", len(ut),
      "| unruled singletons", sum(1 for c in ut.values() if c == 1))
named = sorted(t for t in dt if t in ban)
print("named by a NOT clause:", named, "covering", sum(dt[t] for t in named))
PY
```

Its output at BASE, verbatim:

```
graded {'py': 976, 'js': 69} | debt {'py': 44} | unruled {'py': 391, 'js': 26}
distinct debt 24 | distinct unruled 267 | unruled singletons 201
named by a NOT clause: ['append', 'compute', 'count', 'log', 'search', 'validate'] covering 8
```

**The figures are stated per CELL, because the corpus total belongs to no cell.** Rev-1's table gave
one column and rev-1's AC4 then handed the whole of it to `py.function`, which is the single-bucket
shape this unit exists to remove:

| Fact | `py.function` | `js.function` | Corpus |
|---|---|---|---|
| P1 graded | 976 | 69 | 1045 |
| DEBT definitions | 44 | 0 | 44 |
| UNRULED definitions | 391 | 26 | 417 |
| Offenders (the cell's own pair) | 435 | 26 | 461 |

The three corpus-wide rows below are not per-cell figures and are not pinned; they are the evidence
for S2's site count and for the advice half's reach. Distinct DEBT tokens 24, distinct UNRULED tokens
267, UNRULED tokens with exactly one site 201. The `graded` and `offenders` rows reconcile against
`python tools/lexicon/lexicon.py --check`, which prints `P1 verb graded=1045 offenders=461 waived=0`
on the unmodified tree; the rest come from the snippet above and from nowhere else.

The six tokens the declaration's own NOT clauses name are `append`, `compute`, `count`, `log`,
`search` and `validate`, covering 8 definitions. They are the only DEBT tokens this repo's declaration
happens to name, which is why the advice half works for them and for nothing else today. `count` is
the sixth because `measure` NOT `count` is a live clause and `count` reached the DEBT set at this base;
rev-1 listed five.

### Inventory

The load-bearing verified fact: `canon` is imported at `tools/lexicon/lexicon.py:84` and its only three
code references are at `:1065`, `:1101` and `:1114`, all inside `run_probe`, whose AST span is
`:1053-1136`. `run_suggest` at `:785-852` reads `load_conf`, `verbs`,
`leading_verb` and `build_banned_index` and never touches the canon. `build_banned_index` at `:771-782`
inverts `build_negatives(conf)`, which is the declaration's own NOT clauses and nothing else. So the
claim that DEBT is the class where the kit can name the fix is false as shipped for 36 of the 44
definitions, and the fix is a two-line graft into a function that already resolves the same question
one source short.

`run_probe` is deleted by `TOOL-aSurfacedLexicon-3`. This unit must not inherit its call site as the
only canon reader, or the graft lands and dies in the same build.

### Migration

**The pin rows do NOT land at this unit's order, and rev-1's Files-touched said they did.**
`TOOL-aSurfacedLexicon-4`'s S5 makes a `PINS` row naming a cell absent from `CELLS` a refusal, placed
in the TAIL of `load_conf` so every reader of the declaration inherits it — including
`tools/lexicon/adopt-lexicon.sh --check`, which is the `lexicon wiring` leg, whose guard is `[]` and
which therefore fires on every bar. Read at their own specs rather than assumed: unit 6 rev-4 arms
exactly one cell at order 4, `py.constant`, and names `py.function`, `py.type` and `js.function` as
the pairs that are non-empty and carry no `CELLS` row; unit 12 rev-5's S14 writes the full `CELLS`
matrix at order 7. So a `py.function.debt` row written at order 5 reds an unguarded leg on the commit
that lands it.

This unit therefore ships the classifier, the report and the EMISSION, and touches `.lexicon.conf`
not at all. The two rows land when unit 12 writes the matrix at order 7 and pastes what this unit's
`--measure` emits. Until then the scalar stands: this unit reads the pair from the `PINS:` block when
present and falls back to `VERB_OFFENDER_PIN`, so it is independently landable and the bar stays green
between the two commits.

**The scalar this unit hands on is 462 ONLY IF the shell cell is not armed before it.** `TOOL-aSurfacedLexicon-5` is order 3 and
its §4 raises `VERB_OFFENDER_PIN` from `461` to `462` in the conf's RAISED-by-name comment form, with
its minted `classify` as the sole arrival, measured there as `graded 1045 -> 1049` against
`offenders 461 -> 462`. `TOOL-aSurfacedLexicon-6` at order 4 cites that raise and records its own
delta as ZERO. Both were opened and read rather than inferred. Which row absorbs the arrival is
decided, not guessed: `classify` is absent from `canon.build_form_index()` — verified, the index
returns 120 keys and `classify` is not among them — so it lands UNRULED, and at order 5 the split
reads `py.function.debt` 44, `py.function.unruled` 392, `js.function.debt` 0, `js.function.unruled`
26. Every later unit budgeting a minted name against a pin budgets it against `unruled` unless its
leading token is a canon key, in which case it goes to `debt`.

None of those four numbers is a literal in a criterion. AC4 states the reconciliation as an identity
between readings taken in ONE run, so a raise landing between order 3 and order 5 moves both sides
and falsifies nothing.

**SEQUENCING, because the generated build-order table will say otherwise.** This unit shares build
order 5 with `TOOL-aSurfacedLexicon-13`, and both Files-touched tables name
`tools/lexicon/lexicon.py` and `tools/lexicon/selftest.py`. Write sets intersect, so BUILD-METHOD
M6 requires the two to be SEQUENCED and forbids dispatching them together. The README's generated
table renders `Parallel: yes` for that step, which it derives from the step holding two units and
not from any disjointness it checked; that over-claim is filed as `TOOL-aSurfacedLexicon-17`
against the generator. Read the write sets, not the column.

**AND THE SHELL CELL IS THE RAISE THAT MATTERS, which rev-2 did not open and therefore did not see.**
`TOOL-aSurfacedLexicon-14` sits at order 4 and arms the shell function cell. Its own measurement:
608 shell function names reach the verb predicate, of which 508 lead with a token the declared table
does not carry — this repo's test-harness idioms. That is not a rounding error against a scalar of
462; it is the dominant term. The four py/js rows above are unaffected, because they are per-cell and
shell is a fourth cell, which is precisely the property this unit exists to deliver — but any
sentence here about the SCALAR is a sentence about a number that unit owns more of than this one
does. This unit therefore states no scalar value as a pass condition, and where it must reason about
one it says under which landing order the reasoning holds.

**A `js.function.debt` pin of `0` is a real row, not a placeholder.** Under S9's two-sided equality a
zero pin can only red upward, which is exactly right: js has no DEBT population today, and the day a
js definition leads with a canon token the bar says so. The row is emitted rather than omitted for
the same reason §5's empty-population line gives — a row printed as `0` with its denominator is a
measurement, and an omitted row is a mood.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/lexicon/lexicon.py` | the classifier, the offender line, `run_suggest`, the report lines, the pin-row emission |
| `tools/lexicon/selftest.py` | the arms for AC8 and AC9 |
| `.lexicon.conf` | **NOT touched** — see Migration; the pin rows land with unit 12's matrix at order 7 |

No new module: `govkit update` classifies by iterating the receipt at `tools/govkit/govkit.py:5718`,
so a file gov newly ships is outside the classification space, and this unit adds none. ESTIMATE, and
it is an estimate because nothing comparable ships to measure against.

**The identifiers this unit mints, and the pin delta they cost.** `VERB_OFFENDER_PIN` has zero
headroom, offenders count per occurrence, and `lexicon naming predicates` guards on `tools/`, so a
commit editing `tools/lexicon/lexicon.py` selects that leg and the push bar runs it. Rev-1 named none
of these and budgeted nothing. Each was run through `python tools/lexicon/lexicon.py --suggest <name>`
on this worktree:

| Identifier | Role | `--suggest` verdict |
|---|---|---|
| `build_offender_census` | the S1 classifier inside the corpus walk | OK — leads with `build`, which the declaration carries |
| `read_debt_gloss` | the S2 canon-backed half of the offender line | OK — leads with `read`, which the declaration carries |
| `render_pin_rows` | the S5 blank-separated `PINS:` emission | OK — leads with `render`, which the declaration carries |
| `measure_pins` | the S6 per-cell counts on the green and red lines | OK — leads with `measure`, which the declaration carries |

**Pin delta: ZERO.** All four lead with a declared verb, so none is a P1 offender and the scalar this
unit inherits at order 5 passes through unchanged. The negative result is stated because unit 5 and
unit 6 both measured rather than assumed, and because `classify` — the obvious name for S1's work — is
NOT in the declared table and would have cost a raise; `--suggest classify_offender` answers that
`classify` is not declared and no row bans it by name. Module-body assignments are not graded by the
verb predicate, so this unit budgets no delta for constants and mints none. Any identifier added in
build that is not in this table owes its own `--suggest` run before the commit lands.

### Alternatives rejected

Merging the two populations into one pin and reporting the split only in prose. Rejected because a
single bucket over two populations is why `VERB_OFFENDER_PIN` moved eleven times and produced no
renames from the second population; the values it ever carried are 384, 412, 415, 417, 450, 452, 455,
458, 460, 461 and 463 twice, per the research record's `git log -p --follow` over `.lexicon.conf`.

Deriving DEBT from the declaration's NOT clauses alone rather than from the canon. That is what ships
today and it is exactly the 6-of-24 result. The declaration's negatives are one alternative per row
(`canon.render_negative` emits `others[0]`), while a cluster carries up to eight.

Declaring the `py.function` cell here so the pin rows could land at order 5. Rejected as a scope
change wearing a bugfix's clothes: unit 6 rev-4 places the `UNDECLARED CELL` arm report-only precisely
because three cells are undeclared at order 4, and unit 12 rev-5 accepted the matrix and its promotion
constant as one commit at order 7. Arming one cell here to make two pin rows landable would split that
commit and hand unit 12 a matrix it did not write half of.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path, no new egress; the canon is a frozen in-kit tuple.
- perf / scale — one dict membership test per already-extracted definition, inside the existing walk.
  The `lexicon naming predicates` leg ceiling of 300 s in `tools/gate-legs.json` is unchanged and the
  unit adds no second corpus pass.
- a11y — N/A. A stdout report on a gate leg has no rendered surface.
- i18n — N/A here, but see the risks line: `subtokens.py` is ASCII-only and the gap is filed, not fixed.
- error / empty / loading states — a repo whose declaration carries every canon representative has an
  empty DEBT population; the report prints `0` with its denominator rather than omitting the row. Same
  rule covers `js.function.debt` at 0 on this tree.
- observability — both counts print on GREEN as well as RED, keeping `lexicon.py:710-716`'s rule that
  a green row is a measurement or it is a mood.
- risks — the classification changes what a pin COUNTS, so a stale single scalar read against the new
  pair would silently pass. The fallback in Migration is the mitigation and it is temporary by design.
  The second risk is the one §3 now prices: the two-sided comparison over per-cell rows reds a
  within-total redistribution that the scalar greens, and AC9 is its observed failing case.
- testing + left-shift gates — arms in `tools/lexicon/selftest.py` for each of the three advice paths,
  for the classifier boundary and for the redistribution RED; the observed-RED criteria are AC5 and
  AC9. Pin delta from this unit's own minted names is zero, measured in §4 Files touched.
- migration / rollback — reverting is a single-commit revert; this unit writes no conf row, so the
  scalar stands untouched until `TOOL-aSurfacedLexicon-12` retires it at order 7.
- user docs — `tools/lexicon/README.md` gains the DEBT/UNRULED vocabulary. The rendered Skill's
  routing line is `TOOL-aSurfacedLexicon-8`'s edit, not this unit's.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --suggest ensure_cache` runs, it names `check_cache`
  and the `check` gloss. Today it prints ``` `ensure` is not in the declared table ```, verified by
  direct run at writing time.
- **AC2** — When `--suggest require_adopted_root` and `--suggest walk_file_keys` run, they name
  `check_adopted_root` and `scan_file_keys`. Both are silent today, verified by direct run.
- **AC3** — When `--suggest install_x` runs, it answers `seed_x` from the declaration's own NOT clause
  and NOT `init_x` from the canon. **The token is chosen because the two sources disagree on it**, and
  rev-1 keyed this criterion on `append`, where both sources return `add` and the criterion therefore
  could not fail whichever way precedence ran. Measured on this worktree: `--suggest install_x` prints
  the advice to use `seed_x`, because the declaration says `seed` and NOT `install`, while
  `canon.build_form_index()["install"]` returns `init`. Three other tokens disagree today — `do`
  (conf `cmd`, canon `run`), `assert` (conf `test`, canon `check`) and `enable` (conf `arm`, canon
  absent) — so a conf edit that collapses the `install` disagreement is a criterion-breaking edit with
  three fallbacks, and the arm in AC8 reds if the last one goes.
- **AC4** — When `python tools/lexicon/lexicon.py --check` runs against a scratch `CELLS` block in the
  working-tree declaration arming `py.function` and `js.function` with `vocab`, the per-cell report
  satisfies three equalities read out of that ONE run: `py.function.debt` plus `py.function.unruled`
  equals `py.function`'s own offender count; `js.function.debt` plus `js.function.unruled` equals
  `js.function`'s; and the four sum to the PYTHON-AND-JAVASCRIPT part of the scalar
  `grep -n VERB_OFFENDER_PIN .lexicon.conf` reports at the landing order — NOT to the scalar itself.
  **That third equality was written against a scalar of 462 and it is wrong by more than a factor of
  two.** `TOOL-aSurfacedLexicon-14` is order 4, one step before this unit, and arming the shell cell
  puts 608 shell function names in front of the same verb predicate, 508 of which lead with a token
  the declared table does not carry. So the scalar at THIS unit's landing order is on the order of
  970 once that unit lands, and 462 if it does not — and this unit must not depend on which, because
  its own §3 says that unit is the one most likely to be deferred. The equality is therefore stated
  over the two cells this unit owns, and the shell contribution is read from the report rather than
  assumed absent. **No literal appears in this criterion**, because rev-1's did: it required a **No literal appears in this criterion**, because rev-1's did: it required a
  `debt` of 43 and an `unruled` of 418 "for `py.function`" and asserted their sum was the corpus 461,
  when `py.function`'s own pair is 435 and the missing 26 are `js.function`'s. Satisfying that
  literally meant folding js into python's row — the single-bucket defect this unit exists to remove.
  The measured split at BASE is in §4's per-cell table and it is context here, not a pass condition.
- **AC5** — When a definition named `def ensure_thing():` is staged into a tracked `.py` file,
  `lexicon.py --check` exits 1 with that line classified DEBT and naming `check_thing`; when it is
  unstaged the leg returns to its baseline. The RED is observed before this unit is called done, per
  the build README's rule.
- **AC6** — When a definition named `def demand_thing():` is staged, the same run classifies it UNRULED
  and proposes no replacement, because `demand` is in no cluster. The two messages are textually
  distinct, so a reader can tell a rename from a scoping question.
- **AC7** — When `python tools/lexicon/lexicon.py --measure` runs against the same scratch `CELLS`
  block AC4 uses, it emits four `PINS:` rows — `py.function.debt`, `py.function.unruled`,
  `js.function.debt`, `js.function.unruled` — **each separated from the next by exactly one blank
  line**, and pasting that output into the scratch declaration leaves `bash
  tools/lexicon/adopt-lexicon.sh --check` at exit 0. The unguarded `adopt-lexicon.sh` path is named
  rather than `--check` alone because that is the reader carrying `TOOL-aSurfacedLexicon-4`'s S10
  refusal, which rev-1's criterion would have tripped: a verbatim paste of two adjacent rows is the
  dense pair S10 refuses, so rev-1 asserted a green the grammar cannot give. When the emission is
  re-run with the separator removed, the same command exits 1 naming both line numbers; that RED is
  observed too, and it is the round-trip of this emitter against that reader.
- **AC8** — When `tools/lexicon/selftest.py` runs under `GATE_SELFTESTS=1`, an arm asserts that every
  key of `canon.build_form_index()` classifies as DEBT and that a token absent from it classifies as
  UNRULED, so the classifier cannot silently collapse to one bucket. A second arm asserts that at
  least one token in the shipped declaration disagrees with `canon.build_form_index()` and that
  `--suggest` follows the declaration for it, so AC3 cannot decay back into a criterion that cannot
  fail without something going red first.
- **AC9** — When a DEBT-leading definition in a tracked `.py` file is renamed to an UNRULED-leading
  token, against the scratch `CELLS` block and its pasted pin rows, `--check` exits 1 naming BOTH
  moved rows — `py.function.debt` fallen by one, `py.function.unruled` risen by one — while the corpus
  offender total is unchanged. This is the failing case §3's enforcement change creates, and the build
  rule that a new predicate is not landed until its RED has been observed applies to it. The same
  rename under the single scalar exits 0, which is the whole point of running it both ways.

## 7. Gates

`lexicon naming predicates` (chunk `declarations`, subject `repo`, ceiling 300) is the leg that
carries the verdict and the one the push bar runs. `lexicon selftest` (chunk `selftests`, subject
`kit`, ceiling 880) carries the arms and is invisible to the push boundary unless `GATE_SELFTESTS=1`
is set, which no boundary sets — so an arm added here is on-demand coverage and the spec says so
rather than implying a push-time guarantee. `lexicon wiring` (guard `[]`, ceiling 330) fires on a
conf-only diff and must stay green; this unit writes no conf row, so what it must not do is emit
bytes that reader refuses, which is AC7. `memory hygiene` (chunk `records`, subject `repo`, no guard
key, ceiling 12720) grades this spec — rev-1 named `memory-tree hygiene`, which is no leg at all: the
two real candidates read out of `tools/gate-legs.json` are `memory hygiene`, unguarded and on every
bar, and `memory-hygiene self-test`, a held kit selftest, and they have opposite reachability at the
push boundary. No new gate leg, so no new `testsuite-count-waivers.txt` row and no new wall-clock
ceiling is owed.

## 8. Open questions

- **F1 — Keep the UNRULED population pinned, or stop gating it?**
  RESOLVED (owner, 2026-09-04): keep both pinned. The sum stays as it stands at the landing order and
  the split releases no name. It does ADD reach on the redistribution case, priced in §3 and observed
  by AC9.

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
- rev-2 · 2026-09-05 · spec-audit round 1 folded, and the base RE-PINNED from `d0a18683` to
  `6c670b02`, which this unit's earlier re-measure pass never reached. §4's measurement table was
  attributed to an untracked scratchpad script and to a third sha; it now ships the derivation as an
  inline snippet whose verbatim output is quoted, is stated PER CELL, and every row but the sum moved.
  AC4 was the load-bearing consequence: it handed the corpus-wide 461 to `py.function`, whose own pair
  is 435, so satisfying it literally meant folding js into python's row — it is now three equalities
  read from one run with no literal in it. The two pin rows LEFT §4 Files touched: unit 4's S5 refuses
  a `PINS` row for an undeclared cell inside `load_conf`, unit 6 arms only `py.constant` at order 4 and
  unit 12's S14 writes the matrix at order 7, all three opened and read, so rows written here would red
  the unguarded `lexicon wiring` leg. AC7 gained unit 4's blank-line separation, which its verbatim
  paste would otherwise have tripped, and now observes the emitter through `adopt-lexicon.sh --check`.
  AC3 was re-keyed from `append`, where conf and canon both answer `add` and the criterion could not
  fail, onto `install`, where they disagree. §3 stopped claiming this is not an enforcement change and
  now prices what the two-sided per-cell comparison adds, with AC9 as its observed RED. §4 Migration
  records unit 5's order-3 raise to 462 and which row absorbs it. §4 Files touched names the four
  minted identifiers with their `--suggest` verdicts and a measured pin delta of zero. §7's
  `memory-tree hygiene` corrected to `memory hygiene`.
- rev-3 · 2026-09-05 · cross-unit reconciliation. AC4's third equality summed the four py/js rows to the
  conf scalar; `TOOL-aSurfacedLexicon-14` is one build order earlier and arming the shell cell puts
  up to 508 more occurrences behind that same scalar, so the equality was wrong by more than a
  factor of two and is now stated over the two cells this unit owns. §4 Migration's scalar claim is
  conditional on whether that unit landed, which its own §3 says is the least certain thing in the
  build. The order-5 write-set intersection with `TOOL-aSurfacedLexicon-13` is pinned here, since
  the generated table asserts a parallelism it derives from the step's cardinality alone —
  `TOOL-aSurfacedLexicon-17`.

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
