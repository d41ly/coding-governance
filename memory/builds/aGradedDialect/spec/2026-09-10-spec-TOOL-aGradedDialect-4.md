# TOOL-aGradedDialect-4 — the declaration surface for TypeScript, and the `.tsx` casing row as a declared refusal

**Status:** SPECCED · rev-2 · 2026-09-10 · node a · Tier-2 · base d1357673 · streams tooling · order 4 · ratified 2026-09-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-prompt-TOOL-aGradedDialect-1-spec-brief.md](../prompts/2026-09-10-prompt-TOOL-aGradedDialect-1-spec-brief.md) | journal | TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-5 |
| [2026-09-10-review-TOOL-aGradedDialect-1-round1.md](../reviews/2026-09-10-review-TOOL-aGradedDialect-1-round1.md) | spec-audit | TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-5 |

<!-- /gen:spec-records -->

## 1. Goal

Teach the kit's own catalogs that `.ts` and `.tsx` exist, so an adopter running `--scaffold` over a
TypeScript tree is proposed a real reading instead of the `ts::dark tsx::dark` the tool writes today.
Settle the one casing cell the extension partition cannot answer — `.tsx` functions, whose case is a
function of role — without an exception list and without re-arming the rule
`TOOL-dScaffoldedMirror-13` refused the whole feature over.

## 2. Scope (IN)

- **S1** — `KNOWN_EXTS` in `tools/lexicon/lexicon.py` gains a `ts` row and a `tsx` row, each naming
  its OWN pattern-set id and each at **the mode `TOOL-aGradedDialect-3` EARNED** — `parser` at or
  above `TOOL-aGradedDialect-2`'s floor, `probe` below it. This unit transcribes that verdict and
  never authors it. Observed by **AC1**.
- **S2** — `SEED_CONVENTIONS` in `tools/lexicon/scaffold_lexicon.py` gains all FOUR
  `(extension, surface)` rows, with `("tsx", "function")` written explicitly as `dark` rather than
  left to fall through the `.get` default. The three prescriptive rows are observed by **AC2**; the
  fourth emits the same bytes as the default and is observed by **AC4** instead.
- **S3** — the comment the scaffold emits above `VERB_OFFENDER_PIN` states, from the two figures that
  walk has just measured, what a large offender share means and which door answers it. Observed by
  **AC3**.
- **S4** — one self-test arm asserting that every shipped declaration row RESOLVES: a `parser` id
  against `PARSERS`, a `probe` id against `PATTERN_SETS`, every `SEED_CONVENTIONS` key and value
  against the closed sets in `tools/lexicon/lexicon_conf.py`, and the presence of S2's fourth key.
  Observed by **AC4**.
- **S5** — the emitted `CELLS` block carries the reason the `tsx.function` row is `dark`, stated as a
  rule rather than as a figure measured on somebody else's corpus. Observed by **AC5**.

## 3. Non-goals (OUT)

- **No tokenizer and no `PARSERS` entries.** This unit declares two parser ids; the functions those
  ids resolve to are `TOOL-aGradedDialect-3`'s. A declaration is not an implementation.
- **No new `SELECTOR_KINDS` entry.** §8 resolves the `.tsx` fork against adding one, and §4 records
  why. Re-proposing it is a reopening.
- **No change to the `extract_text` or `PARSERS` call signature.** `TOOL-aGradedDialect-3` declares
  the return shape `(functions, types, imports)` unchanged, and §4 shows the declaration this unit
  chooses precisely so that contract does not have to move.
- **No predicate change.** P1 and P2 grade every extracted function and type whatever any `CELLS` row
  says. Nothing here narrows or widens either.
- **No reader-facing carrier.** `tools/lexicon/LEXICON.md` and the kit README are
  `TOOL-aGradedDialect-5`'s, including the section that currently says this kit does not read
  TypeScript.
- **No edit to this repo's own `.lexicon.conf`.** Verified 2026-09-10: `git ls-files '*.ts' '*.tsx'`
  returns zero on this tree, so its `LANGS` line has no `ts` token to gain and this unit moves no
  verdict here. §5 treats that as the testing risk it is.

### Edges

- **consumes-from** `TOOL-aGradedDialect-3` — the two `PARSERS` entries the ids in S1 name. Without
  them `scan_corpus` refuses every `.ts` file by name, because a `parser` mode whose set id is not in
  `PARSERS` is a named refusal there. That is why this unit's `order` is above that unit's, and it is
  a hard sequence rather than a preference.
- **consumes-from** `TOOL-aGradedDialect-1` — the casing and verb-lead figures the fork in §8 is
  decided on, measured 2026-09-10 against `C:/projects/incms/main` and recorded in that unit's
  research record.
- **hands-off** `TOOL-aGradedDialect-5` — the ruling in `LEXICON.md` and the kit README section on
  arming an unshipped language, both of which describe a world this unit ends.
- **hands-off** external — the role-derived selector kind for React components. §8 refuses it on this
  build's evidence and §4 records the refusal; a later build that wants it starts from there.

## 4. Design

Two catalogs, four seeded rows, one self-test arm. Everything below follows from three properties of
code that already ships, so most of this section is derivation rather than choice.

### Data model

`KNOWN_EXTS` maps an extension token to `(pattern-set-id, mode)`. `SEED_CONVENTIONS` maps an
`(extension, surface)` pair to the convention `--scaffold` proposes for it, defaulting to `dark` for a
pair the kit has no prescription for.

**`<mode>` below is a VERDICT, not a literal, and writing it as one was a round-1 blocker.**
`TOOL-aGradedDialect-3` measures its reader against `TOOL-aGradedDialect-2`'s floor and declares
`parser` at or above it and `probe` below — its S5 and AC6 own that call, and
`TOOL-aGradedDialect-1` §3 forbids anyone else making it. An earlier revision pinned `parser` here in
three places, which would have redded this unit's AC1 on a CORRECT build whose reader honestly scored
below the floor, and left `-3` §8 F1's `probe`-with-a-parser-shaped-id widening with no consumer.
This unit therefore reads the mode from `-3`'s recorded verdict at build time.

| catalog | key | value | why this value |
|---|---|---|---|
| `KNOWN_EXTS` | `ts` | `("ts-tokens", <mode>)` | the mechanism `TOOL-aGradedDialect-1` ratified, at the mode `-3` earned |
| `KNOWN_EXTS` | `tsx` | `("tsx-tokens", <mode>)` | a second id, for the reason below; same mode source |
| `SEED_CONVENTIONS` | `("ts", "function")` | `camel` | TypeScript's published style |
| `SEED_CONVENTIONS` | `("ts", "type")` | `pascal` | TypeScript's published style |
| `SEED_CONVENTIONS` | `("tsx", "type")` | `pascal` | TypeScript's published style |
| `SEED_CONVENTIONS` | `("tsx", "function")` | `dark` | §8, and a DECLARED refusal rather than a default |

**The conventions are PRESCRIPTIVE and the corpus did not choose them.** That is the scaffolder's own
law, printed in the comment it emits above the block: a convention ranked from the tree it grades
makes the gate certify the habit it was installed to change. So `camel` and `pascal` come from
TypeScript's published style, from outside every tree involved. The measured distribution in the
research record — `.ts` functions 94.8% camel and both type surfaces over 99% pascal, on 2026-09-10 —
is CORROBORATION that the prescription is not absurd against a real corpus, and it is not the source
of any row here.

**The fourth row emits nothing new, and that is why it needs its own observation.** `--scaffold`
creates a `CELLS` key for every `(extension, surface)` pair whose extracted population is non-empty
and fills it from `SEED_CONVENTIONS.get(pair, "dark")`, so a `tsx.function` row appears at `dark` with
or without S2's fourth entry. The bytes are identical; what differs is whether the catalog RECORDS a
refusal or merely fails to hold an opinion, and the difference is legible only in the dict. That is
the whole reason AC4 carries the clause rather than AC2, and it is this repo's own rule that an
absent declaration and a declared absence are different bytes, applied one layer in from where the
bytes are.

**Two extensions, not one, and it is forced rather than chosen.** `ext_of` returns the last dot
segment of a basename and `scan_corpus` looks the result up in a plain dict, defaulting to
`("", "dark")`. There is no alias mechanism anywhere in the reader, so an undeclared `tsx` is dark by
default and silently so.

**Two parser IDS, and that one is a trade rather than a derivation.** `extract_text` dispatches
`PARSERS[pset](src)`, which takes the source text and nothing else, so a single shared id gives the
tokenizer no way to know which dialect it was handed. That matters because `<` is a generic in `.ts`
and a JSX element in `.tsx`, and the oracle in the research record distinguishes them by script kind
for exactly that reason. Whether the tokenizer actually needs the distinction is not knowable until
that tokenizer exists, which is `TOOL-aGradedDialect-3`'s. The two options are therefore priced by
what each costs if it turns out wrong. Two ids that turn out to need only one implementation cost one
extra `PARSERS` row binding both names to the same function. One id that turns out to need two costs
a `LANGS` edit in every adopter's committed declaration, which is a migration. The asymmetry decides
it without the evidence, and it leaves `TOOL-aGradedDialect-3` free to bind both ids to one function.

### Inventory

**This unit mints no identifier.** It adds rows to two existing module constants and one group of
module-level `check(...)` calls in `tools/lexicon/selftest.py`, which is the shape every arm in that
file already has. Dict keys are data and no cell grades them: this repo declares `py.function snake`,
`py.type pascal`, `js.function camel` and `sh.function snake`, and it declares no `constant` cell, so
`scan_module_constants` never runs here. Should S4's arm turn out to want a helper, it is a Python
function and lands under `py.function snake`, leading with a canon verb.

### Alternatives rejected

| option | disposition |
|---|---|
| `tsx.function camel`, with the offender count pinned | §8 veto 1 — it arms the exact rule this build's README makes its acceptance bar |
| `tsx.function pascal` | same veto, and it makes the larger half of the population offenders |
| a role-derived `SELECTOR_KINDS` entry | §8 veto 2 — a new public surface in the declaration grammar, and it needs a per-definition fact the frozen return shape does not carry |
| a `case:` selector kind | refused before this unit, in the research record's §5, as the vacuous-selector class: a name selected BECAUSE it is pascal and graded AGAINST pascal cannot fail |
| one shared parser id for both extensions | rejected above on migration cost, not on evidence |

### Files touched (estimate)

| file | change |
|---|---|
| `tools/lexicon/lexicon.py` | two `KNOWN_EXTS` rows |
| `tools/lexicon/scaffold_lexicon.py` | four `SEED_CONVENTIONS` rows, the `CELLS` comment, the verb-pin comment |
| `tools/lexicon/selftest.py` | one arm group for S4 |
| `tools/lexicon/kit.toml` | the kit version, shared with units 3 and 5 rather than owned here |

## 5. Production-readiness checklist

- security — N/A. Nothing here reads untrusted input, opens a network path or writes outside the
  tree the adopter pointed the scaffolder at.
- perf / scale — N/A as a constraint. Both catalogs are read once at import and the S4 arm is an
  in-process comparison of two dicts, with no walk and no subprocess.
- error / empty / loading states — the one state that matters is a `KNOWN_EXTS` row whose parser id
  does not resolve, which `scan_corpus` already turns into a named refusal per file. S4 moves that
  discovery from the adopter's first run to this kit's own self-test.
- observability — the emitted `.lexicon.conf` IS the observable: every row and every comment this
  unit adds is bytes an adopter reads at the moment they meet the decision.
- risks — this repo tracks no `.ts` or `.tsx`, so nothing here can be observed on its own tree and a
  green bar says nothing about it. That is the green-by-absence class, and §6 answers it by resting
  every criterion on a fixture or on a constant rather than on a gov-tree run.
- testing — S4's arm is the left-shift, and it is landed only once its failing case has been watched:
  point a `KNOWN_EXTS` parser id at a name `PARSERS` does not hold, confirm RED, unstage.
- migration — none for this repo. For an adopter who already ran `--scaffold`, the seeded rows arrive
  only on a re-scaffold; an existing declaration is theirs and this unit does not rewrite it.
- user docs — `TOOL-aGradedDialect-5` owns every reader-facing carrier. What this unit writes is the
  comment text inside the generated declaration, which is not documentation about the kit.

## 6. Acceptance criteria

- **AC1** — When `tools/lexicon/scaffold_lexicon.py` runs over a fixture tree carrying one `.ts` and
  one `.tsx` file, the `LANGS` line it emits names `ts` and `tsx` at the mode
  `python tools/lexicon/lexicon.py` reports for those extensions, rather than `ts::dark tsx::dark`.
  `figure:` DERIVED — the mode is read from the tool's own output, never compared to a literal, so
  the criterion holds under either verdict `TOOL-aGradedDialect-3` reaches.
  `fixture:` the end-to-end scaffold arm in `tools/lexicon/selftest.py` builds a temp git repo today
  and commits one `.py` file; this criterion needs two more files in it.
  Red when: the rows are keyed `.ts` and `.tsx` with the dot. `ext_of` returns the token WITHOUT its
  dot, so a dotted key is never looked up, and the seed keeps emitting `dark` while the catalog looks
  correct to a reader.
- **AC2** — When that same run finishes, the `CELLS` block it emits carries `ts.function` at `camel`,
  `ts.type` at `pascal` and `tsx.type` at `pascal`.
  Red when: the criterion is extended to cover the `tsx.function` row here. That row emits `dark`
  whether S2 declares it or the `.get` default supplies it, so an assertion over these bytes cannot
  tell a declared refusal from an absent one and would pass with the row missing. Only the three rows
  that differ from the default belong in an observation over the emitted file.
- **AC3** — When the emitted `.lexicon.conf` is read, the comment above `VERB_OFFENDER_PIN` states
  the offender share as a figure computed from that walk, and names the `CANON:` overlay as the door.
  `figure:` DERIVED. The scaffolder already holds both operands, so nothing new is measured.
  Red when: the sentence carries a literal percentage. The 13.7% and 11.2% verb-lead rates in the
  research record are `C:/projects/incms/main` on 2026-09-10, and writing either into every adopter's
  declaration pins one repo's measurement into another's.
- **AC4** — When `python tools/lexicon/selftest.py` runs, an arm names every `KNOWN_EXTS` row whose
  pattern-set id resolves in neither `PARSERS` nor `PATTERN_SETS`, every `SEED_CONVENTIONS` key or
  value outside `SURFACES` and `CONVENTIONS`, and the absence of an explicit `("tsx", "function")`
  key. That last clause is the ONLY observation that can see S2's fourth row, for the reason AC2
  states.
  `cost:` that leg is `subject = kit` and `chunk = selftests` in `tools/gate-legs.json`, so no push
  boundary runs it. It is `GATE_SELFTESTS=1` or the direct invocation above.
  Red when: the arm iterates the catalog and asserts on the loop's last row alone, which passes
  whenever the broken row is not last. Stage a break on a NON-final row when confirming it.
- **AC5** — When the emitted `CELLS` block is read, the comment on the `tsx.function` row gives the
  RULE — a component is a function that returns JSX, so this cell's case follows role and not surface
  — and cites no percentage.
  Red when: it reads as a to-do. A comment inviting the reader to complete the table re-arms the rule
  §8 refused, and it is the one place an adopter is most likely to act on the invitation.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `memory hygiene`

New arm: `tools/lexicon/selftest.py` · point a `KNOWN_EXTS` parser id at a name `PARSERS` does not
hold, and set one `SEED_CONVENTIONS` value to a token outside `CONVENTIONS` · none, the file declares
no assertion floor.

## 8. Open questions

- **F1 — what convention does the `tsx.function` cell declare?** The population splits by ROLE rather
  than by surface, measured at 69.4% camel and 30.3% pascal on 2026-09-10 in
  `TOOL-aGradedDialect-1`'s research record, because a React component is a function that returns
  JSX. Four options were weighed. **O1** declares `camel` and pins the offenders. **O2** declares
  `pascal`. **O3** declares `dark`. **O4** adds a role-derived `SELECTOR_KINDS` entry keying on
  whether the definition returns JSX.
  RESOLVED (agent, 2026-09-10, delegated): **O3**, `tsx.function` declared `dark`, written as a row
  rather than left to the default.
  O1 and O2 fall to veto 1. This build's README makes `TOOL-dScaffoldedMirror-13`'s four objections
  its acceptance bar, and the first of them is that the kit would arm a casing rule over the
  PascalCase React components. O1 arms that rule; O2 arms its mirror and makes the larger half of the
  population offenders. Either one reopens the objection this build exists to answer.
  O4 falls to veto 2. `SELECTOR_KINDS` is part of the grammar an adopter writes their declaration
  against, so adding a kind is a new public surface; and the selector would need a per-definition fact
  — does this body return JSX — that the return shape `(functions, types, imports)` does not carry
  and that `TOOL-aGradedDialect-3` declares unchanged. The existing `decorator` kind is no help
  either: `extract_decorators` returns `{}` for any parser that is not `python-ast`, so a decorator
  selector on a TypeScript row would select nothing and red as a `DEAD CELL`.
  **O3's price is smaller than the research record priced it, and this is the one place that
  correction is recorded.** That record's §5 lists declaring the cell dark as losing 3108 definitions
  of coverage. Verified against source on 2026-09-10: `measure_conventions` computes verdicts and
  teeth only under `if conv != "dark" and row["graded"]`, and the `DEAD CELL` arm exempts a `dark`
  row explicitly, so what a `dark` cell costs is the CASING verdict on that one cell. P1 grades every
  extracted function and P2 every extracted type whatever any `CELLS` row says, and the row is printed
  on every run, so those 3108 definitions stay extracted, stay verb-graded and stay named. The
  disposition the record called one of three bad ones is the correct one at a fraction of the stated
  price.
  The follow-up O3 leaves open is the role-derived selector itself, recorded in §4 rather than in a
  backlog row, so nothing here mints an id outside this build's roster.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft, authored against the pinned base and the research record.
- rev-2 · 2026-09-10 · S1 · §4 · AC1 · folded spec-audit round 1. The `parser` mode was
  written as a literal in S1, in §4's Data model table and in AC1, one unit before
  `TOOL-aGradedDialect-3` measures it. All three now name it as that unit's earned VERDICT, and AC1
  asserts against the tool's own reported mode instead of a token, so a reader that honestly scores
  below the floor and declares `probe` no longer reds this unit. AC1's dotted-key Red-when is
  unchanged.

## 10. Reuse audit

The seam is `tools/lexicon/lexicon_conf.py:check_declaration` together with the two closed sets
`SURFACES` and `CONVENTIONS` beside it, and `tools/lexicon/subtokens.py:check_convention`, which
`reuse_lookup.py` ranked in the candidate set for the behaviour phrase below. This unit extends the
declaration surface those three already grade rather than adding a second one, which is what makes
S4's arm an assertion over existing constants instead of a new mechanism. Verified against source on
2026-09-10: `check_declaration` holds the three cross-block refusals, `SELECTOR_KINDS` is
`("prefix", "decorator")`, and `SEED_CONVENTIONS` already defaults an unprescribed pair to `dark`, so
S2's fourth row is a declared refusal replacing a defaulted one and not a new behaviour. The probe
reports its own blindness — `unscanned layers: .sh` — so no claim above rests on its silence about
shell, and the adopter shell script `adopt-lexicon.sh` was read directly for the same reason. One
disagreement between a hit and the source is recorded in §8: the research record prices a `dark`
casing cell at the whole extracted population, and `measure_conventions` shows the cost is the
convention verdict alone.

Recall terms used: `lexicon typescript tsx probe parser dark PATTERN_SETS coverage extractor
PascalCase React casing tokenizer adopter`
