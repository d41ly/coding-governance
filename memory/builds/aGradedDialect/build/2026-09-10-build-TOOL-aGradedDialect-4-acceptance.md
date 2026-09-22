**Serves:** journal TOOL-aGradedDialect-4

# Acceptance ledger — TOOL-aGradedDialect-4, the declaration surface

Every observation below was made on node `a` on 2026-09-10, in this run's own worktree.

**This repo tracks ZERO `.ts` and `.tsx` files**, verified again here: `git ls-files '*.ts' '*.tsx'`
returns nothing. So a green gov bar says nothing whatever about the two catalog rows this unit adds,
which is the green-by-absence class. Every criterion below therefore rests on a FIXTURE or on a
constant, never on this tree — the `.ts`/`.tsx` population now lives in the `--scaffold` end-to-end
block's throwaway git repo.

**The leg that observes most of this is HELD by the ordinary bar.** `lexicon selftest` is
`subject = kit`, `chunk = selftests` in `tools/gate-legs.json`, so `bash tools/run-gates/run-gates.sh`
runs none of these arms. They were observed by `python tools/lexicon/selftest.py` directly:
`lexicon selftest OK — 665 arm(s)`, exit 0. The two legs that DO ride an ordinary bar were run too:
`python tools/lexicon/lexicon.py` exits 0 with `lexicon OK — 1864 tracked file(s)`, and
`bash tools/lexicon/adopt-lexicon.sh --check` exits 0 with
`.lexicon.conf parses, ratified, 23 verb(s) declared, Skill in sync, declaration grades clean`.

**How many arms this unit added is DERIVED, not counted by hand.** The suite prints its own arm
count, and it moved 648 -> 665 across this unit's two commits: seventeen new arms, plus one re-formed
and two moved. **The first commit's message says "nine", and it is wrong** — a figure typed beside a
population, which is the class this repo names most often and which its own commit message managed
to break. It is recorded here rather than rewritten there, because history is not edited to make a
record look tidy.

**Evidences:** TOOL-aGradedDialect-4

- AC1 — two arms per extension in the `--scaffold` end-to-end block. The emitted `LANGS` line is
  split into TOKENS and `ts:ts-tokens:parser` and `tsx:tsx-tokens:parser` are required to be members
  of that set, with each expected token built from `lex.KNOWN_EXTS.get(<ext>)` — the catalog the
  scaffolder READS, never what it emits, so the criterion holds under either verdict
  `TOOL-aGradedDialect-3` could have reached. Token membership rather than substring, so `ts:` does
  not match inside `tsx:`. The second arm requires `ts::dark` and `tsx::dark` to be ABSENT from the
  same set, which is what catches the dotted-key defect. Staged red: keying the catalog `".ts"`
  instead of `"ts"` makes the seed emit `LANGS="conf::dark py:python-ast:parser ts::dark
  tsx:tsx-tokens:parser"` and both arms fire.
  **The arm was fixed BY that staged break**, and this is the one correction worth recording: it
  first read `lex.KNOWN_EXTS[<ext>][0]`, so the dotted key raised `KeyError` inside the arm and
  killed the run 8 seconds in — a predicate taken out by the fault it grades. It reads `.get` and
  asserts the row exists.
- AC2 — the emitted `CELLS` rows, read back through `load_conf`, the ONE reader, rather than through
  a second parse of its grammar: `ts.function camel`, `ts.type pascal`, `tsx.type pascal`. The
  `tsx.function` row is deliberately NOT asserted here, because it emits `dark` whether the catalog
  declares it or the `.get` default supplies it. Staged red: seeding `("ts", "function")` under the
  surface token `"func"` leaves `ts.function` seeded `dark` and the arm names it — which is the
  silent-arming-nothing defect, visible in the emitted file only through this arm.
- AC3 — three arms over the comment block directly above `VERB_OFFENDER_PIN` in the emitted conf.
  The first requires a `<n> of <n> definition(s)` figure AND a percent sign; the second requires the
  numerator to be the PIN VALUE the same walk wrote, so a figure invented independently of the walk
  fails; the third requires the block to name `CANON:` as the door. The share is computed in
  `main()` from `verb_offenders` and `total_defs`, with a zero-corpus branch that says the share is
  undefined rather than dividing. Staged red twice: replacing the measured sentence with the
  research record's literal `13.7%` reds the first two arms, and spelling the door `canon overlay`
  without the block-header colon reds the third.
  A FOURTH observation covers the division itself, added on the follow-up commit after the bug-class
  checklist selected `armed-but-unreachable-rule`: the share is a quotient, and a repo of nothing but
  prose extracts zero definitions, so the guarded branch is on a real first-adoption path. Two arms
  over a definitionless fixture repo require the scaffolder to exit 0 and to call the share UNDEFINED
  rather than print a reassuring `0.0%` — zero offenders out of zero definitions is not a clean tree.
  Observed by hand before the arm was written, on a fixture carrying one `.md` file.
- AC4 — three arms in a new group in `tools/lexicon/selftest.py`, all three over CONSTANTS and no
  tree. (1) Every `KNOWN_EXTS` row's pattern-set id must resolve in `PARSERS` **or** in
  `PATTERN_SETS` — MODE-AGNOSTIC, so a tokenizer that honestly scored below the floor and shipped
  as `probe` still resolves, and `resolve_extractor` is deliberately not the operand because it
  answers for a declared PAIR. (2) Every `SEED_CONVENTIONS` key's surface half and every value must
  sit inside `SURFACES` and `CONVENTIONS`. (3) `("tsx", "function")` must be PRESENT at `dark`,
  which is the only observation in the repo that can see S2's fourth row at all.
  Staged red, on a NON-final catalog row each time: pointing `ts` at `no-such-reader` — a token in
  NEITHER catalog, not merely a parser id `PARSERS` lacks — reds arm 1 naming
  `unresolved=['ts:no-such-reader'] of 5 row(s)`; the surface-token break above reds arm 2 naming
  `outside=['ts.func=camel'] of 9 row(s)`; deleting the `("tsx", "function")` row reds arm 3 **and
  nothing else in the 663 arms the first commit shipped**, which is the AC2/AC4 split
  demonstrated rather than argued.
- AC5 — two arms over the comment run directly above the emitted `tsx.function` row. One requires
  the ROLE rule — the words `JSX` and `role` — and the other requires NO percent sign anywhere in
  that run. Both test the row's index first, so an absent row is a failure rather than a vacuous
  pass over an empty string. Staged red: replacing the first emitted line with
  `# TODO pick a case here -- 69.4% of these components are pascal.` reds both, which is exactly the
  to-do-with-a-figure shape AC5's Red-when names.

## The declared staged break, and what it actually did

§5's testing row and §7's `New arm:` line ask for two breaks. Both were run and both redded the
suite. The KNOWN_EXTS half redded it THROUGH THE ARM, named above. The `SEED_CONVENTIONS`-value half
— `("ts", "function"): "camelCase"` — reds it through a TRACEBACK instead: the bad value reaches
`_parse_cells`, and the `--scaffold` and re-scaffold blocks read the seed they write through two
UNGUARDED `load_conf` calls, so the interpreter dies before the arm summary prints at the end. The
arm records its failure first and the record is lost with the summary. That is why the catalog arms
were moved above those fixture blocks, and why the surface-token break above exists: it is the same
clause with a break that stays silent everywhere except the arm. Guarding those two reads is not
this unit's — they belong to the arms that own them, and the spec's rev-5 §9 line says so.

## What the bug-class checklist changed, after the first commit

`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` selected eleven classes over the first
commit. Three of them landed on it and were fixed in the follow-up:

- `two-answers-to-one-question` — the `KNOWN_EXTS` comment quoted `TOOL-aGradedDialect-3`'s score,
  `115 of 115` and `refusal share 0.0000`, beside code that does not measure it. The figures are
  gone and the comment points at the arm that prints them on every run. The `SEED_CONVENTIONS`
  comment restated the ROLE rule the emitted `CELLS` comment already carries; it now points there
  and the rule has one carrier.
- `fixture-passes-by-finding-nothing` — AC1's second arm is an ABSENCE assertion, and an absent
  `LANGS` line leaves the token set empty, where `not in` passes over nothing. It now asserts its
  own population first.
- `armed-but-unreachable-rule` — the zero-corpus branch of the share, described under AC3 above.

The other eight were read and do not land: no shell field parsing, no heredoc-authored regex, no
fence in either record, no arm resting on a substituted shipped value, and every staged break was
reverted before the green run that preceded the commit.

## What this unit did NOT observe, stated rather than left out

- **Nothing here was observed on a repository that actually declares TypeScript.** The end-to-end
  arm scaffolds a throwaway git repo carrying one `.ts` and one `.tsx` file, ratifies the seed and
  runs `adopt-lexicon.sh --check` green over it, which is an adopter's first two commands. It is
  still a fixture of two files, not a real tree. The reader itself was graded against a real one by
  `TOOL-aGradedDialect-2` and `-3`; the DECLARATION was not.
- **The `.tsx` casing fork is answered by a refusal, not by a measurement.** §8 F1 resolves to
  `dark` and the emitted comment states the rule. What a role-derived selector would score is
  unmeasured and stays that way: the option is refused on veto 2 in §8 and recorded in §4.
- **`VERB_OFFENDER_PIN` does not move, and that was checked rather than assumed.**
  `P1 verb graded=` rises 2080 -> 2081 for the one new helper, `offenders=` holds at 984, and
  `py.function.conv` population rises 1320 -> 1321 with zero violations. The helper was named
  through `python tools/lexicon/lexicon.py --suggest read_note_above --as py.function` BEFORE it was
  written, which is why nothing needed absorbing.
- **`.claude/skills/lexicon/SKILL.md` was not re-rendered and did not need to be.** This unit edits
  no `.lexicon.conf`, so the declaration's graded content is byte-identical and `--check` reports
  `Skill in sync`. `memory/map/generated/symbols.json` did not move either: the only new symbol is a
  nested helper inside a `with` block, which the map's extractor does not index as a module symbol.
- **The kit version was not bumped and `tools/lexicon/kit.toml` was not touched.**
  `TOOL-aGradedDialect-5` S6 owns that, per this unit's §4.
- **No `.gitattributes` row was added for `.ts` or `.tsx`.** The fixture files are written into a
  temp directory by the suite and are never tracked here, so there are no bytes for an EOL rule to
  govern. An adopter's tree is theirs.
