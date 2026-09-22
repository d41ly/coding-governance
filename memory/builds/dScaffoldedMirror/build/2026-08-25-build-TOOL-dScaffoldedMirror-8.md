# TOOL-dScaffoldedMirror-8 — build record

**Serves:** journal TOOL-dScaffoldedMirror-8

Node `d`, 2026-08-25, base `500a5db6`, unattended run `dScaffoldedMirror`. Spec:
`../spec/2026-08-24-spec-dScaffoldedMirror-8.md`, built at rev-3. Tier-2. The last unit of the build,
and the one that retires the defect that opened it.

## Result — the demo that started this build, re-run

The owner scaffolded a fresh repo on 2026-08-24 and watched six deliberately-bad names pass green,
because the frequency count had promoted `do`, `is`, `get`, `fetch`, `validate` and `calculate` into
the vocabulary on the strength of those very names. The same fixture, scaffolded by the same command
after this unit:

```
src/core/orders.py:9:  P1 verb: validate_order — leading token 'validate' is not in the declared VERBS table
src/core/orders.py:13: P1 verb: calculate_total — leading token 'calculate' is not in the declared VERBS table
src/core/store.py:5:   P1 verb: get_record — leading token 'get' is not in the declared VERBS table
src/core/store.py:9:   P1 verb: fetch_remote — leading token 'fetch' is not in the declared VERBS table
src/core/store.py:13:  P1 verb: do_thing — leading token 'do' is not in the declared VERBS table
src/core/store.py:17:  P1 verb: is_ready — leading token 'is' is not in the declared VERBS table
```

Six of six. And both halves of `TOOL-dScaffoldedMirror-1` closed in the same run:
`SUFFIX_OFFENDER_PIN="1"` is MEASURED (it counts the fixture's `OrderManager`) rather than the
hardcoded `0` that redded on first gate run, and `conf::dark` is seeded whether or not the corpus
carries one.

## The rule, which is the unit

**Which CLUSTERS enter a proposal is decided by the corpus. Which FORM represents one is decided by
the canon — element 0, unconditionally, at every frequency and every dominance.** Two questions, two
deciders; the frequency ranking answered both with the corpus, which is why it legalised whatever a
repo already did most.

A dominance threshold does not fix that. A repo whose sessions all wrote `get_*` has dominance near
1.0, so `get` is adopted silently and with more ceremony. **The polarity arm is the proof**: a corpus
containing exactly one `get_*` and one `fetch_*`, and no `load` anywhere, proposes `read` and `load`
— the two spellings it does not use. A count-based rule proposes `get` or `fetch`. And sixty sites of
an off-canon token do not put it in the table at all.

## Three measurements say the canon is not one agent's taste

Re-checked here, in the selftest rather than in prose:

1. All **11** negative definitions a human wrote for this repo on 2026-08-16 are exactly non-first
   elements of the cluster holding their verb. The canon reproduces a curated table it never saw.
2. **55.2%** of a real adopter's 14,659 definitions already lead with a verb from this table, in a
   repo that has never carried a declaration, and all six commonest off-table leaders land in a
   cluster.
3. Of the ten non-verbs the 2026-08-16 curation deleted, **10 of 10** are unnominatable — eight by
   absence from every cluster, two (`do`, `is`) by the first-element rule.

## Two defects the demo found, and one refinement

**The seed was born failing this unit's own S6 assert.** Fourteen canon glosses, fourteen rows with
no negative — a scaffold handing every adopter a declaration its own checker rejects on the first
run. `canon.render_negative` now emits each cluster's first alternative, so the curator sharpens a
boundary rather than inventing one.

**The `LAYER_OFFENDER_PIN` line carried a trailing comment**, which the conf grammar forbids — *"a
value with spaces is double-quoted and no comment follows it on the line"*. The reader REFUSED the
file the scaffold had just written. The gate caught its own author violating its own declaration
format.

**`--probe` separates ratified-beyond-canon from debt.** Gov's table carries `cmd`, `arm` and `seed`,
which no cluster holds — 38 sites. Reporting those as unnominatable would be a finding against a
decision somebody made deliberately; the canon bounds what a machine may PROPOSE, never what an owner
may declare.

## What S4's cut costs, stated rather than hidden

`--probe --write` and `lexicon-debt.tsv` were cut by the owner's six-unit ruling: no gate reads the
ledger, its artifact would ship `role = "seed"`, and the adopter population is zero. `--probe`
reports the same numbers on demand and `--scaffold` already writes the table. **The cost is that
convergence debt is visible on demand and recorded nowhere, so nothing tracks it falling.** On this
repo that debt is 44 renames across 22 spellings.

**Evidences:** TOOL-dScaffoldedMirror-8
- AC1 — amended rev-3 — it named `--probe --write`, which S4's cut removed; the PROPERTY it asserts is armed against `--scaffold` instead, as `canon: 60 sites of an off-canon token do NOT put it in the proposed table` in `tools/lexicon/selftest.py`
- AC2 — amended rev-3 — same cut verb, same substitution: the polarity property is armed as `POLARITY: a corpus of get and fetch proposes 'read' and 'load', the forms it does not use`, with its companion asserting NEITHER live spelling is proposed
- AC3 — amended rev-3 — it read the DEBT LEDGER, which S4 cut entirely. `python tools/lexicon/lexicon.py --probe` reports the same synonym rows to stdout (`is->check x7, walk->scan x4, make->build x3`) and writes nothing; §9 records what the cut costs
- AC4 — `python tools/lexicon/lexicon.py --probe` — exits 0 against a fixture with no declaration and says so in its first line; armed as `--probe: legal with NO declaration, and exits 0`
- AC5 — amended rev-3 — it asserted `--probe --write` REFUSES on a ratified conf; with the verb cut there is no write path to refuse, and gov's ~70 lines of pin archaeology are safe because nothing can rewrite the conf
- AC6 — `python tools/lexicon/lexicon.py` — a `VERBS` row with no NOT clause reds, naming the row; observed under a staged break that stripped `load`'s negative, armed as `S6: a row with NO negative is a finding`
- AC7 — `python tools/lexicon/lexicon.py` — a declared negative that is itself a row reds, naming the token; observed by pointing a NOT at a declared verb, armed as `S6: a banned token that is itself a row is a finding`
- AC8 — `python tools/lexicon/lexicon.py` — exits 0 on this repo after the backfill, with all 23 rows parsing at least one negative and `VERB_OFFENDER_PIN` unchanged at 384
- AC9 — `bash tools/lexicon/adopt-lexicon.sh --scaffold` — on the owner's original fixture it proposes 15 canon clusters with their negatives, measures `SUFFIX_OFFENDER_PIN="1"`, seeds `conf::dark`, and all six deliberately-bad names are offenders
- AC10 — `python tools/lexicon/selftest.py` — 127 arms green, covering AC1's and AC2's properties under `--scaffold`, AC4, AC6, AC7 and AC9; one arm was itself corrected before landing, having asserted on a string slice rather than on the pin lines
