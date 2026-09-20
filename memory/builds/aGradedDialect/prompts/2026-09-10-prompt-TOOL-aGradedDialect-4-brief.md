**Serves:** journal TOOL-aGradedDialect-4

# Build brief — TOOL-aGradedDialect-4, the declaration surface

Your spec is `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md`, at rev-4
and through three audit rounds. Build what it says. Where you would diverge, change the spec first
with a rev bump and a §9 line, then code.

## THE VERDICT IS IN, and it is what your S1 was written to transcribe

`TOOL-aGradedDialect-3` landed at `a69e4af1` and **EARNED `parser`.** Measured against the 115
frozen records: 115 of 115 in exact agreement, function recall and precision 122/122, type 20/20,
refusal share 0.0000 against a 0.02 ceiling. `PARSERS` now holds `ts-tokens` and `tsx-tokens`.

So the two `KNOWN_EXTS` rows you write are `("ts-tokens", "parser")` and `("tsx-tokens", "parser")`.
**Write them as that verdict's value, not as your own choice** — three revisions of your spec were
spent removing a hard-coded `parser` from S1, §4 and AC1, and AC1's operand is deliberately
`lex.KNOWN_EXTS["ts"][1]` read from the catalog rather than anything the scaffolder emits. Do not
reintroduce a literal comparison; the criterion could not fail with one.

## What unit 3 left you

- `resolve_extractor` in `tools/lexicon/lexicon.py` is THE armedness predicate, called at all four
  sites §8 F1 named. Your S4 arm is mode-agnostic and must stay that way: every `KNOWN_EXTS`
  pattern-set id resolves in `PARSERS` **or** in `PATTERN_SETS`. A mode-keyed arm reds a correct
  `probe` build, which is the round-2 blocker your rev-3 fold removed.
- `DEFINITION_SNIFF` is already widened (unit 3's S8), so your `.ts`/`.tsx` fixture files will not
  trip `DEAD SNIFFER`. You do not touch the sniffer; your §3 says so.
- `.claude/skills/lexicon/SKILL.md` was NOT re-rendered by unit 3 because the declaration's graded
  content did not move. If YOUR edits move it, re-render and say so.

## The one fork still open is yours, and §8 is where it is resolved

`.tsx` functions split 69.4% camel / 30.3% pascal by ROLE — a React component is a function that
returns JSX. Your §4's `SEED_CONVENTIONS` table currently seeds `("tsx", "function")` as `dark`, as
a DECLARED refusal rather than a `.get` default, and S5 says the emitted `CELLS` block must carry
the REASON as a rule rather than as a figure measured on somebody else's corpus. Hold that line.

Two things not to re-propose, both already refused with argument:
- a `case:` selector kind — a name selected BECAUSE it is pascal and graded AGAINST pascal cannot
  fail, which is the vacuous-selector class. Unit 1's research record §5 refuses it.
- a `tsx.function` pin at ~943 conv offenders — a two-sided equality that reds on every new
  component the adopter writes.

## The staged break, restated because getting it wrong makes the gate green

Point a `KNOWN_EXTS` pattern-set id at a token present in **neither** `PARSERS` **nor**
`PATTERN_SETS`, on a non-final catalog row. NOT "a parser id `PARSERS` does not hold" — under the
mode-agnostic rule such an id may legitimately resolve through `PATTERN_SETS`, so that break can come
back GREEN and certify nothing. §5's testing row and §7's `New arm:` line both carry the corrected
form; use it.

## Bounds

- This repo tracks ZERO `.ts` files, so nothing you write can be observed on gov's own tree and a
  green bar says nothing about it. §6 rests every criterion on a fixture or on a constant for that
  reason. Keep it that way: a criterion that needs a `.ts` file in this repo is unobservable here.
- `tools/lexicon/kit.toml` is NOT touched. Its Files-touched row says so explicitly.
- Do not bump the kit version. `TOOL-aGradedDialect-5` S6 owns it.
- `lexicon selftest` is a HELD leg. Verify with `python tools/lexicon/selftest.py` directly.
- Your declared write set is `tools/lexicon/lexicon.py`, `tools/lexicon/scaffold_lexicon.py`,
  `tools/lexicon/selftest.py`, your own spec, and your acceptance ledger at
  `memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-4-acceptance.md`.
  Widen it through `--dispatch` BEFORE the commit if you need more — the generated build README and
  `memory/map/generated/symbols.json` are the two both siblings needed.
