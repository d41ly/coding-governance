**Serves:** spec-audit TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5

# aGradedDialect — spec-set audit, round 2

Tier-2 adversarial spec audit of the five-unit set, run 2026-09-10 on node `a`, branch
`branch/lexicon-kit-typescript-34c322`. Four lens passes, five skeptic batches, one synthesis.

**Subjects, pinned at the blob each was commissioned at.** ROUND 2.

| unit | subject | pinned blob | blob as read |
|---|---|---|---|
| `TOOL-aGradedDialect-1` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-1.md` | `e4c5ea860a85931cb8d3ffd99253749c0eca1cda` | same |
| `TOOL-aGradedDialect-2` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md` | `fb59d1ae0d672141997cee1e9a10223fc52c493a` | `f4042323d2e759baf266fd9a2084618e47175852` |
| `TOOL-aGradedDialect-3` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md` | `aefc5e635b2b053f8267e9376f731907e607acb2` | same |
| `TOOL-aGradedDialect-4` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md` | `3575130a1823ee06a1d5c2026b4162ed353fa506` | `f1f73ff925474a1cb9069ce41ea3d6ece8a0d4d1` |
| `TOOL-aGradedDialect-5` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md` | `356519076f9c2ca1eeb7232a33a63bf33779b199` | same |

Units 2 and 4 MOVED after this round was commissioned, in the working tree and uncommitted; both
were reviewed as they now stand, and finding 15 carries the re-pin. The pinned blobs are still real
objects, so a reader can diff either way.

## Verdict: BLOCKED

Two blockers survived. One is a scope item that reds a correct build — unit 4's S4 specifies its new
self-test arm mode-keyed, against the exact configuration unit 3 §8 F1 exists to legalise, and unit
4's own AC4 states the permissive rule three sections lower. The other is an obligation nobody in
the set owns: arming `.ts`/`.tsx` walks into `TOOL-dScaffoldedMirror-6`'s ratified `DEAD SNIFFER`
refusal, measured here against the shipped regex, and the ordinary React file shape reds an
adopter's gate on the run right after `--scaffold`.

Seven highs follow, and six of them are one class: a claim, an edit or a handoff that exists in one
carrier and is observed in none. The build's own §1 goal is removing prose that answers a question
the code answers differently, and the set currently commits several new instances of it while
closing the old ones. None of the findings overturns a design decision. The `.ts`/`.tsx` mechanism
pick, the earned-mode rule and the frozen corpus all held again this round.

### Review shape

Raw 47, confirmed 26, refuted 21, unverified 0. Precision 0.55.

Precision is at the ~0.5 floor §8 names, up from 0.15 in round 1, which is what feeding the lenses
unit 1 §5 and unit 3 §8 as by-design bought. The 26 confirmed findings consolidate into the 15
entries below: several lenses reached the same defect from different addresses, and each entry lists
the source ids it absorbs so a fold can trace any one of them back.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted
to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. Nothing in
this run was lost, so a zero count here is evidence rather than a gap: the unverified set is
genuinely empty and every lens finding was adjudicated. The consolidation in the table below is a
synthesis decision, not a pipeline discard.

**Severity adjudicated here, not inherited.** Four findings arrived filed BLOCKER (the two blob-pin
drifts, each filed twice); their own skeptics wrote that BLOCKER overstated them, and they are one
MEDIUM entry here. Two findings arrived HIGH and are BLOCKER below. The counts in the table are the
ones this record adjudicates.

---

## Findings, severity-ranked

| # | severity | unit | address | one line | source ids |
|---|---|---|---|---|---|
| 1 | BLOCKER | `-4` | §2 S4, §3 Edges | the new self-test arm reds the `probe` build unit 3 legalises | 18, 31, 32 |
| 2 | BLOCKER | `-4` | §2 S1, §5 | arming TS hits the ratified `DEAD SNIFFER` refusal; no unit owns the sniffer | 41 |
| 3 | HIGH | `-3` | §8 F1, §4 | F1 names two edit sites; the armedness predicate lives at four | 30 |
| 4 | HIGH | `-3` | §2 S7, §4 | two units claim the kit version bump; neither observes it | 5, 21, 37 |
| 5 | HIGH | `-5` | §6 AC1 | AC1's comparison operand cannot be produced on this repo | 4, 34 |
| 6 | HIGH | `-5` | §2 S2, §4, AC2 | the modes-table row unit 3 hands over has no receiver | 22, 43 |
| 7 | HIGH | `-5` | §4 carrier table, AC2 | `TWO PARSERS SHIP` has two carriers; the table names one | 23 |
| 8 | HIGH | `-2` | §5 security, §8 F1 | the disclosure price rests on a containment the kit's own record denies | 42 |
| 9 | HIGH | `-5` | §6 AC2 | AC2's zero-hit grep reds the fix §4 prescribes | 44 |
| 10 | MEDIUM | `-5` | §2 S5, §4, AC2 | the map dossier's copy of the falsified claim is observed by nothing | 12 |
| 11 | MEDIUM | `-5` | §2 S1, AC1 | S1's compensating-check clause is dropped by its own criterion | 13 |
| 12 | MEDIUM | `-3` | §5 perf / scale | the `lexicon selftest` ceiling is stated as 300 s; the manifest says 880 | 24 |
| 13 | MEDIUM | `-2` | §7 Gates | four criteria are observed only inside a leg the ordinary bar HOLDS | 26 |
| 14 | MEDIUM | `-2` | §3 non-goals | the `regex_vs_oracle.py` non-goal is stale and books a phantom follow-up | 20, 38, 47 |
| 15 | MEDIUM | `-2`, `-4` | whole file | the review base moved after commissioning; re-pin before the fold | 28, 29, 39, 40 |

---

### 1. BLOCKER — `TOOL-aGradedDialect-4` §2 S4 and §3 Edges: the new gate arm reds a correct build

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md`, §2 S4 and
§3 Edges (`consumes-from TOOL-aGradedDialect-3`, rev-2 text). Against
`spec-TOOL-aGradedDialect-3.md` §2 S2 and §8 F1, and against this same file's §6 AC4.

**What is wrong.** S4 specifies the arm mode-keyed — it resolves "a `parser` id against `PARSERS`, a
`probe` id against `PATTERN_SETS`" — and §3's edge repeats the mapping as the catalog the earned
mode selects. Unit 3 registers `ts-tokens` and `tsx-tokens` in `PARSERS` under BOTH verdicts (S2 has
no verdict branch), and its §8 F1 widens the `probe` branch of `extract_text` to dispatch to
`PARSERS` when the id names one, precisely so a below-floor tokenizer never needs a `PATTERN_SETS`
entry. Unit 3 writes no `PATTERN_SETS` row at all. This file's own AC4 already states the permissive
rule — an id that "resolves in NEITHER `PARSERS` NOR `PATTERN_SETS`" — so scope and criterion
contradict each other inside one document.

**Why it blocks.** On the exact build the rev-2 fold amended this unit to survive — unit 3 honestly
scoring below the floor and declaring `probe` — `KNOWN_EXTS` holds `("ts-tokens", "probe")` with
`ts-tokens` in `PARSERS` only. A builder implementing S4 verbatim ships a self-test arm that reds
that correct build, and the refusal §3's edge predicts is the `mode == "probe" and pset not in sets`
arm F1 removes. Round 1's finding 2 fixed this class in S1, §4 and AC1; the fold landed in one
carrier of three and left the two that specify the new gate.

**Fix.** Restate S4 in AC4's form: every `KNOWN_EXTS` pattern-set id must resolve in `PARSERS` OR
`PATTERN_SETS`, mode-agnostic, with `-3` §8 F1 cited in §4 as the reason a parser id under `probe`
is legal. Rewrite §3's edge to name `PARSERS` under both verdicts; the sequencing argument for
`order` is untouched and survives as written.

**Left-shift gate.** Make the engine own the rule so no spec can restate it wrong: one
`resolve_extractor(mode, pset)` helper in `lexicon.py` that both dispatch sites call, and a
`selftest.py` arm asserting every `KNOWN_EXTS` id resolves through it whatever the mode. Then a
mode-keyed arm cannot be written against a per-mode catalog rule that does not exist in the code.
Stage the break by adding a `probe` row whose id names a parser, confirm the mode-keyed form REDs
and the helper form passes, unstage. The residue — a scope item contradicting its own acceptance
criterion — is not machine-gateable and joins the build's checklist as a documented check: **an
S-item and the AC that claims to observe it are read as a PAIR before ratification, and a predicate
stated in both must be stated identically.** Two of this round's entries are that class.

---

### 2. BLOCKER — `TOOL-aGradedDialect-4` §2 S1 and §5: arming TypeScript walks into the `DEAD SNIFFER` refusal

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md`, §2 S1 and
§5 (risks / testing). The obligation belongs to this unit or to `-3`, whose §4 locator table owns
the definition forms; nothing in the set names it. Against `TOOL-dScaffoldedMirror-6` S6 and
`tools/lexicon/lexicon.py:145` (`DEFINITION_SNIFF`), `:1479` and `:1616`.

**What is wrong.** `DEFINITION_SNIFF` does not match six of the definition forms unit 3's §4 locator
table returns. Measured 2026-09-10 against the shipped regex: `export interface Props`,
`export type Id =`, `export enum`, `export const Card: React.FC = () =>`, `const pick = <T,>(x) =>`
and `export default function App()` all sniff NEGATIVE, while `function f(){}`,
`export function f(){}`, `class Foo{}` and `const g = () => {}` sniff positive. `extractor_carriers`
is populated by `if funcs or types_`, so a `types.ts` carrying only `export interface` and
`export type` — a near-universal shape in a real TypeScript tree — lands in
`blind = extractor_carriers - carriers` and appends the `DEAD SNIFFER` problem, which reds the run.

**Why it blocks.** The refusal is ratified, so this is not a new opinion: the first adopter `.tsx`
file whose definitions are only a typed const arrow and an `interface` reds their gate on the run
right after `--scaffold`, which is the feature's only intended consumer path. This repo tracks zero
`.ts` files, so no gov bar can observe it — the green-by-absence condition §5 names for the other
criteria and then does not answer for this one. Grepping the whole build folder for `sniff` returns
two hits, both in unit 5 and both about a header sentence, so no unit holds the obligation.

**Fix.** Add an S-item — here, or in `-3` whose §4 owns the forms — widening `DEFINITION_SNIFF` to
the TypeScript definition forms the locator returns, cited to `TOOL-dScaffoldedMirror-6` S6. Give
AC1's fixture tree a `.tsx` file whose only definitions are a typed const arrow and an `interface`,
and have the criterion assert the run reports no `DEAD SNIFFER`.

**Left-shift gate.** A `selftest.py` arm per armed language, not per file: for every extension in
`KNOWN_EXTS`, a fixture whose definitions use that language's ordinary forms must produce an empty
`blind` set. That gates the CLASS — the next language armed inherits the check instead of
rediscovering the refusal — and it is observable on a repo that tracks none of the language, which
is the whole difficulty here. Stage the break by dropping `interface` from the widened sniffer,
confirm RED, unstage.

---

### 3. HIGH — `TOOL-aGradedDialect-3` §8 F1 and §4: the armedness predicate lives at four sites, not two

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md`, §8 F1
("Two edits, both in `tools/lexicon/lexicon.py`") and §4 Files touched. Against `lexicon.py:822`,
`:873`, `:1934`, `:2465`, and the comment at `:1354-1357`.

**What is wrong.** F1 names `extract_text` and `scan_corpus`. The predicate
`m == "parser" or (m == "probe" and ps in measured["sets"])` is re-derived verbatim at two more
sites: `run()`'s `armed_exts`, the numerator behind the `lexicon: coverage — armed N of M` line, and
`run_expand`'s armed-extension evidence line. A `probe` row whose pattern-set id names a parser fails
both, because `ts-tokens` lands in `PARSERS` and never in the resolved pattern sets. §10's
verification covered `extract_text`'s two dispatch rules and neither reporting site.

**Why it is high rather than a blocker.** AC7's positive clause ("reports the extension as armed")
would probably catch the shipped symptom at observation time, so the build is unlikely to land
broken. What it does not repair is the design: `.ts`/`.tsx` would be extracted and graded while the
coverage fraction excludes them and `--expand` prints "(none armed)" beside a corpus it just graded.
The engine's own comment names this exact split as the defect `resolve_pattern_sets`-once was bought
to prevent — "two answers to one question, in the two halves of one run" — and `:2459-2463` records
that the `armed` line was already repaired once for the same reason.

**Fix.** Name FOUR edit sites in F1 and §4, and add the armedness predicate as one derived helper
both reporting sites call, so the extractor and the coverage fraction cannot diverge again. Give AC7
a clause asserting the printed `coverage — armed` line counts the fixture's `.ts` files rather than
merely that they extract.

**Left-shift gate.** A source-shape arm on the `lexicon selftest` leg: the armedness predicate may
appear exactly ONCE in `lexicon.py`, as the helper's body — red on a second occurrence of the
`== "probe" and` form outside it. It is a grep, it costs nothing, and it is the only kind of check
that catches a fourth copy being added next year. Stage the break by inlining the predicate at one
call site, confirm RED, unstage.

---

### 4. HIGH — `TOOL-aGradedDialect-3` §2 S7 and §4: two units claim the version bump, neither observes it

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md`, §2 S7 and
§4 Files touched. Against `spec-TOOL-aGradedDialect-5.md` §8 F2 and `spec-TOOL-aGradedDialect-4.md`
§4.

**What is wrong.** S7 scopes "the kit version stamped, and the rendered Skill re-rendered", and §4
lists `lexicon.py` for "the version constant" plus `SKILL.md` "re-rendered because the kit version is
one of its placeholders". Unit 5 §8 F2 resolves the opposite — the bump lands there, once, for the
whole build — and says so in order that "a sibling spec claiming the same edit is a disagreement a
cross-read can see". This is that cross-read. Unit 4 defers correctly ("shared with units 3 and 5
rather than owned here"); unit 3 does not, and grepping unit 3 for `version` returns only the three
claiming lines and no deferral.

**Why it is high.** Worse than a duplicated edit. Unit 3's Files-touched names `lexicon.py` and
`SKILL.md` only, while `tools/check-kit-versions.sh` compares the constant against all its markers,
so unit 3 bumping the constant alone reds `kit version markers` on its own landing — and that leg is
absent from unit 3's §7 gate list, so the red arrives at a boundary the spec never named. The
alternative failure is quieter: unit 3 silently backs out, and S7's version clause becomes
unsatisfiable while AC8 grades only exit 0 and the offender pins, observing nothing either way. This
is the four-carrier stamp trap this repo already keeps a gotcha record for.

**Fix.** Strike the version stamp from S7 and from §4's Files-touched, leaving S7 as the offender-pin
re-measurement plus the Skill re-render, and cite `-5` §8 F2 as the allocation. If the clause stays
instead, add `kit version markers` to §7 and give AC8 a clause asserting every marker equals the
source.

**Left-shift gate.** A hygiene arm over a build folder's spec set: no two specs may list the same
path with the same edit rationale in Files touched, and a build folder may name the kit version
constant in at most one spec. Cheap, exact, and it catches the allocation disagreement at
ratification rather than at the second red. Stage the break by copying unit 5's version row into a
sibling spec, confirm RED, unstage.

---

### 5. HIGH — `TOOL-aGradedDialect-5` §6 AC1: the criterion's comparison operand cannot exist here

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §6 AC1.
Against `lexicon.py:1991-1992` and `:2006`, `.lexicon.conf`'s `LANGS` row, and
`spec-TOOL-aGradedDialect-4.md` §3.

**What is wrong.** AC1 requires the `LEXICON.md` mode token to equal the one
`python tools/lexicon/lexicon.py` "prints for those extensions on a run of this repo". Verified by
running it: the coverage line enumerates `sorted(declared.items())`, and `declared` is built solely
from this repo's `.lexicon.conf` `LANGS` rows, which carry no `ts` or `tsx` token. `git ls-files
'*.ts' '*.tsx'` returns zero here, unit 4 §3 forbids the `LANGS` edit on that ground, and unit 5 §3
forbids any `.lexicon.conf` key. `KNOWN_EXTS` is never printed by any mode, so no other run emits
the operand either.

**Why it is high.** S1's mode clause is the one thing this unit exists to get right, per §5's own
risk list, and it rests on a comparison this repo cannot produce. AC1's Red-when — "says `parser`
where the extractor declares `probe`" — is the correct trap and can never fire. Unlike unit 4's AC1,
this one names "a run of this repo" explicitly, which is what removes the escape.

**Fix.** Point AC1 at a source that exists on this tree: the mode printed by `-3`'s conformance arm
(its AC6 line), or `lex.KNOWN_EXTS["ts"][1]` read directly. Delete "on a run of this repo". Keep the
Red-when exactly as written.

**Left-shift gate.** Make the operand exist rather than only repairing the sentence: have the
conformance arm print one `mode` line per `KNOWN_EXTS` extension into a named artifact, and red on a
`KNOWN_EXTS` extension with no printed mode. Then any criterion of this shape has something to read
on any tree, including an adopter's. Stage the break by withholding one extension's line, confirm
RED, unstage.

---

### 6. HIGH — `TOOL-aGradedDialect-5` §2 S2, §4 and AC2: the handoff unit 3 declares has no receiver

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §2 S2, §4
carrier table and §6 AC2. Against `spec-TOOL-aGradedDialect-3.md` §3 Edges and §8 F1, and
`tools/lexicon/README.md:234` and `:284`.

**What is wrong.** Unit 3's hands-off edge names a specific record obligation: "the kit README's
modes table says a `probe` extractor IS a regex pattern set, which stops being true". Unit 5 accepts
a different one. S2 scopes "the parser sentence under 'Coverage modes'", §4's carrier table — the
spec's authoritative enumeration of what carries claims this build falsifies — lists only the
language list and `TWO PARSERS SHIP`, and AC2 greps only those two literals. The modes-table cell
(`| probe | a regex pattern set | incomplete BY CONSTRUCTION |`) and the sentence at `:284`
("`probe` needs a pattern set, and the kit ships exactly one") are in no scope item, no carrier row
and no criterion.

**Why it is high.** F1's dispatch widening lands under either verdict, so both sentences go false the
moment S6 ships. Unit 3 prices the widening as "the cost is a record" and hands the record here;
nothing collects it, so the kit would ship a tokenizer under a table row saying a probe is a regex
set — one question with two answers, committed inside the build whose §1 goal is closing exactly
that.

**Fix.** Add both lines to §4's carrier table as third and fourth rows, extend AC2 to the modes-table
cell and the "ships exactly one" sentence, and name `-3` §8 F1 as the reason they moved.

**Left-shift gate.** A hygiene arm over the build folder: for every `hands-off` edge in a spec's §3
that names a record obligation, the receiving unit must name the same literal in its §4 carrier table
or in an acceptance criterion — red otherwise. The edge tables are already structured, so this is a
join, not a parser. Stage the break by deleting one carrier row on a spec with a live edge, confirm
RED, unstage.

---

### 7. HIGH — `TOOL-aGradedDialect-5` §4 carrier table and AC2: a two-carrier claim with one carrier named

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §4 carrier
table and §6 AC2. Against `tools/lexicon/README.md:237` and `tools/lexicon/lexicon.py:26`.

**What is wrong.** `grep -rn "TWO PARSERS SHIP"` returns two live carriers: the README, and the engine
module header at `lexicon.py:26`, which also repeats the whole modes table at `:22`. §4 attributes
the claim to the README alone and AC2 greps only the README. After `-3` registers `ts-tokens` and
`tsx-tokens`, four parsers ship and the engine header is false.

**Why it is high.** §4's own rule is that a prose count is fixed by deriving it, and this is the "a
fix naming more than one carrier lands in only one" class this repo's map dossier names — committed
inside the fix for that class. Nothing but the carrier list prevents it: S3 already opens
`lexicon.py` for editing, and `-3` §3 disclaims records entirely, so no unit owns line 26.

**Fix.** Add `tools/lexicon/lexicon.py:26` as a row in §4's table, and make AC2 grep both
`tools/lexicon/README.md` and `tools/lexicon/lexicon.py` for `TWO PARSERS SHIP` with no hit in
either.

**Left-shift gate.** A carrier-completeness arm, and it is the most reusable gate in this round: every
literal quoted in a spec's §4 carrier table is grepped over the whole tracked tree, and the leg reds
when it occurs in a file the table does not list. That converts "did we find every copy?" from a
reviewer's memory into a scan, and it catches finding 10 in the same pass. Stage the break by
deleting one row from a carrier table whose literal has two carriers, confirm RED, unstage.

---

### 8. HIGH — `TOOL-aGradedDialect-2` §5 security and §8 F1: the disclosure price rests on a containment the kit denies

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md`, §5
(security row) and §8 F1. Against `tools/lexicon/kit.toml` lines 34-37
(`TOOL-aQuenchedHarness-3`'s note) and `WIRE-INTO-PROJECT.md`.

**What is wrong.** F1 prices the third-party-source disclosure partly on the corpus being "withheld
from `govkit apply` so no adopter receives it". The record that created that mechanism already bounds
it, in its own words: the withholding "withholds from `govkit apply` ONLY. The copy-install path in
`WIRE-INTO-PROJECT.md` is a plain `cp -r` of the kit dir and does not read this file, so that runbook
removes them separately." That runbook has no lexicon removal line at all —
`grep -in lexicon WIRE-INTO-PROJECT.md` returns only the kit-selection menu at lines 120-123 — while
`codebase-map` gets an explicit `rm -f` at line 344 and `memory-recall` at line 415, both with the
same explanatory sentence.

**Why it is high.** An adopter following the documented copy-install path receives the committed
excerpts of `C:/projects/incms/main` verbatim, so a completeness claim about third-party source is
overstated in a ratified spec. Unit 5 owns every record edit in this build and does not list
`WIRE-INTO-PROJECT.md` among its files touched, so nobody closes it either.

**Fix.** Add the runbook removal line to unit 5's S-list and Files touched, mirroring the
`codebase-map` `rm -f` at `WIRE-INTO-PROJECT.md:344`, and cite it from §5 and §8 F1. Failing that,
restate F1's price plainly: a copy-installing adopter receives the corpus, and here is why that is
acceptable. Either is defensible; the current text is neither.

**Left-shift gate.** A kit-descriptor parity arm: every path a `kit.toml` withholds from `govkit
apply` must also appear in a removal line inside `WIRE-INTO-PROJECT.md`'s section for that kit — red
otherwise. Two kits already satisfy it, so the gate lands green and only the lexicon gap reds. Stage
the break by deleting the `codebase-map` `rm -f` line, confirm RED, unstage.

---

### 9. HIGH — `TOOL-aGradedDialect-5` §6 AC2: the criterion reds the fix its own §4 prescribes

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §6 AC2,
against this same file's §4 carrier table and S5. The sentence is
`tools/lexicon/README.md:284-285`, and the section carries `TOOL-dScaffoldedMirror-13` F2's ratified
permission plus the `PATTERNS:` instructions.

**What is wrong.** §4 prescribes the fix as a narrowing — "TypeScript leaves that list" — and S5
phrases the dossier fix the same way. AC2 demands that
`grep -n "TWO PARSERS SHIP\|could only declare their language" tools/lexicon/README.md` return NO
hit, which a narrowed sentence ("a Go, Rust or C# adopter could only declare their language `dark`")
still matches. The §4-correct implementation reds AC2, and the only edit that greens it deletes the
phrase entirely.

**Why it is high.** A zero-hit grep passes equally on the intended narrowing and on deleting the whole
section, which would drop a ratified permission — the kit declines to SHIP a TypeScript extractor and
does not decline to RUN an adopter's own — along with the `PATTERNS:` block an adopter needs to do
so. The criterion cannot tell the fix from the over-deletion, and the spec disagrees with itself
about which is owed.

**Fix.** Give AC2 a positive half beside the negative: after the edit the section still names Go, Rust
and C#, still teaches the `PATTERNS:` block, still states the kit does not decline to run an
adopter's own extractor, and no longer names TypeScript.

**Left-shift gate.** Not fully gateable, and the record should say so rather than pretend. The cheap
half: an acceptance criterion whose whole observation is a grep asserting ABSENCE reds unless it also
names a positive expectation over the same file — a shape check on the spec, not on the tree. The
rest joins the build's checklist as a documented check: **a criterion that observes a deletion states
what must SURVIVE it.** This class is why finding 1's residue is written down too.

---

### 10. MEDIUM — `TOOL-aGradedDialect-5` §2 S5 and AC2: the dossier's copy of the claim is observed by nothing

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §2 S5, §4
carrier table and §6 AC2. The live sentence is `memory/map/features/lexicon.md:170`.

**What is wrong.** S5 has two halves — claim the new inventory keys, and stop the dossier prose naming
TypeScript among the languages an adopter "could only declare their language `dark`" — and says both
are observed by AC5. AC5 grades key claims and dead keys through `codebase-map coverage +
freshness`, which cannot read a sentence. §4's carrier table names that exact file and claim, and
AC2's grep is scoped to `tools/lexicon/README.md` alone.

**Why it is medium.** The stale sentence survives in a file this build must edit anyway, which is the
two-answers-to-one-question defect the unit exists to close — but it is prose in a dossier rather
than a gate that reds or a shipped behaviour that breaks.

**Fix.** Extend AC2's grep to both files
(`grep -n "could only declare their language" tools/lexicon/README.md memory/map/features/lexicon.md`,
adjusted for the positive half finding 9 asks for), or give S5's prose clause its own criterion and
Red-when.

**Left-shift gate.** Covered by finding 7's carrier-completeness arm: the dossier is a carrier the
table already lists, and grepping every quoted literal tree-wide reds when a listed claim survives
outside the criterion's scope. One gate, two findings.

---

### 11. MEDIUM — `TOOL-aGradedDialect-5` §2 S1 and AC1: the compensating-check clause is dropped by its criterion

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §2 S1 and
§6 AC1.

**What is wrong.** S1 requires the new `LEXICON.md` paragraph to name the earned coverage mode AND
"the compensating check for whatever stays unread". AC1 asserts the mode token alone, and its
Red-when covers only the `parser`-where-`probe`-shipped mismatch.

**Why it is medium.** It bites only on a branch — unit 3 shipping `probe`, or shipping `parser` with a
header refusal list, which `-3` AC4 guarantees exists. On that branch the paragraph lands naming an
exemption with no compensating check beside it, in the one file §4 calls the one a human opens to
decide what goes in a declaration, and the charter forbids exactly that by name. Conditionality is a
reason to write the criterion as a conditional, not to drop it.

**Fix.** Add a clause to AC1: the paragraph names each refusal from `parse_ts_defs.__doc__` and the
check that compensates for it, with a Red-when for a mode token standing alone.

**Left-shift gate.** A scope-to-criterion coverage read is the honest gate here and it is only half
machine-checkable: an S-item containing a conjunction ("and the …") whose AC contains no matching
clause is a heuristic, not a proof. Wire the heuristic as an advisory arm that PRINTS the pairs it
cannot match rather than redding, and keep finding 1's documented pair-read check as the real
control. An advisory arm that names what it could not check is worth more here than a predicate that
would red innocent specs.

---

### 12. MEDIUM — `TOOL-aGradedDialect-3` §5 perf / scale: the leg ceiling is off by a factor of three

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md`, §5 (perf /
scale). Against `spec-TOOL-aGradedDialect-2.md` §5 and `tools/gate-legs.json`.

**What is wrong.** §5 states the `lexicon selftest` leg "carries a 300-second-class ceiling in
`tools/gate-legs.json`". The manifest gives that leg `"ceiling": 880`; 300 belongs to `lexicon naming
predicates`. Unit 2 §5 states 880 for the same leg.

**Why it is medium.** Two sibling specs give a reader two ceilings for one leg, and the unit adding the
most expensive arm — the corpus scoring run — plans against a third of the real headroom while
believing itself close to the limit. Nothing breaks; a design decision is taken on a wrong number.

**Fix.** Drop the figure and point at the `lexicon selftest` row in `tools/gate-legs.json`. Correcting
it to 880 is second best: a number typed beside the source that owns it is what this build's own
README forbids.

**Left-shift gate.** Extend the spec-token check: a spec naming a `tools/gate-legs.json` leg together
with a number in the same sentence must match that leg's manifest value, or state no number at all.
Exact, cheap, and it enforces the derive-don't-author rule where specs actually break it. Stage the
break by editing one figure, confirm RED, unstage.

---

### 13. MEDIUM — `TOOL-aGradedDialect-2` §7 Gates: four criteria observed only inside a leg the bar HOLDS

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md`, §7 Gates,
against its own §6 AC1, AC2, AC4 and AC5.

**What is wrong.** §7 lists `lexicon selftest` as a plain merge-bar gate. That leg is
`chunk = selftests`, `subject = kit` in the manifest, so an ordinary bar holds it — and AC1, AC2, AC4
and AC5 are all observed only inside it, including a New arm (`js-regex` scored against the frozen
corpus) that no push-boundary bar will ever run. `-3` §7 and `-4` AC4 both state the hold explicitly
for the same leg; this spec does not mention it.

**Why it is medium.** A green ordinary bar runs none of this unit's criteria, so its Definition of Done
can be called done on a run that exercised nothing — a skip wearing a pass, which this spec's own AC4
Red-when names as a defect. It is medium rather than high because the leg exists and the run is one
environment variable away; the gap is in what the spec tells its builder.

**Fix.** Add the sentence `-3` §7 already carries: `lexicon selftest` is `subject = kit`,
`chunk = selftests`, so this unit's DoD runs `GATE_SELFTESTS=1` — or `python
tools/lexicon/selftest.py` directly.

**Left-shift gate.** A spec §7 arm: every leg a spec names that is `chunk = selftests` or
`subject = kit` in `tools/gate-legs.json` must be annotated as held within that section (the spec
contains `GATE_SELFTESTS` or `HOLDS` there) — red otherwise. Two of the three kit-work siblings
already pass it. Stage the break by deleting the annotation from `-3` §7, confirm RED, unstage.

---

### 14. MEDIUM — `TOOL-aGradedDialect-2` §3 non-goals: a stale accusation and a phantom follow-up

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md`, §3, the
"No reproduction of `regex_vs_oracle.py`" non-goal. Against
`memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md`
§6 and `spec-TOOL-aGradedDialect-1.md` §9 rev-2.

**What is wrong.** The non-goal asserts that unit 1's record §6 "points at this spec's §4 for that
script's full source" and that "its bytes were not committed", calls the pointer a defect in that
record, and books it as a follow-up for the closing fold. Round 1 filed that as blocker 1 and unit 1
folded it: the record's §6 line 245 now reads "`regex_vs_oracle.py` — the scoring arm, reproduced
HERE in full", the source runs to roughly line 383 with the runnable invocation below it, and the
record states outright that the forward-pointer is gone. Unit 1 §9 rev-2 records the fold. The rev-3
edit to unit 2 did not touch the non-goal, so the staleness is current.

**Why it is medium.** Nothing breaks at build time; the closing fold is dispatched at a defect that no
longer exists, and a reader comparing the two documents trusts the wrong one. For the prior-art lens
it reads as evidence the two were folded independently, which is the more expensive error.

**Fix.** Rewrite the non-goal to say that unit 1's record §6 carries the script runnable (rev-2,
2026-09-10) and that this unit therefore reproduces nothing, and delete the follow-up sentence.

**Left-shift gate.** The inverse of round 1's artifact-existence arm, and it costs the same scan: a
spec asserting an artifact is ABSENT (`was not committed`, `exists nowhere`, `points at`) reds when
the named token resolves to a tracked path or to a fenced block inside a record the build binds.
Round 1's arm catches the claim that a present artifact is missing; this one catches the claim that a
missing artifact is still missing after it landed. Stage the break by re-asserting the old sentence,
confirm RED, unstage.

---

### 15. MEDIUM — `TOOL-aGradedDialect-2` and `-4`, whole file: the review base moved under the round

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md` and
`…-4.md`, both files.

**What is wrong.** The commissioned pins are the HEAD blobs (`fb59d1ae…` and `3575130a…`); the working
tree hashes to `f4042323d2e759baf266fd9a2084618e47175852` and
`f1f73ff925474a1cb9069ce41ea3d6ece8a0d4d1`, and both files carry an uncommitted rev-3 entry in §9 —
unit 2 amending its §3 `hands-off` edge to `-4`, unit 4 declaring the missing `consumes-from` edge to
`-2`.

**Why it is medium rather than the blocker it was filed as, twice.** The drift is additive and confined
to §3's edges and §9. Finding 14's non-goal text, and unit 4's S4, AC4 and the rev-2 `consumes-from`
text findings 1 and 3 index, are byte-identical to the pins, so no other finding in this round is
invalidated by it. The real cost is narrower and still real: a fold agent editing from the pin
clobbers rev-3, and a second reviewer working from the pin reads a different document.

**Fix.** Re-pin the review base to the two hashes above and note in each spec's §9 that rev-3 landed
mid-review, so a later fold can tell which text each round actually read. This record states both,
which is the fix half-applied.

**Left-shift gate.** A hygiene arm over review records: every blob in a review record's pinned-subject
table must either resolve to that path at HEAD, or be accompanied by an "as read" hash that does.
That turns a silent base drift into a red at the moment the review lands, which is the only moment
anyone can still act on it. Stage the break by deleting the "blob as read" column from this record,
confirm RED, unstage.

---

## What was attacked and held

Recorded so round 3 does not re-buy it. Twenty-one findings died on the skeptic, and the pattern is
worth keeping: the mechanism pick (C2) drew fire again from three lenses and held on the same
grounds as round 1 — the losing conditions are pre-registered, the oracle is the adopter tree's
`typescript@5.9.3`, and the `case:` refusal is argued rather than overlooked. Unit 3's refusal list,
its `SyntaxError` contract and its rejection of a new mode token held. Unit 1's record survived
intact this round, which is what round 1's three blockers bought. Unit 4's rev-2 fold to S1, §4 and
AC1 is correct as far as it went — finding 1 is that it did not go far enough, not that it went the
wrong way.

The residue worth naming: five of this round's nine blocker-and-high entries are cross-unit
contradictions, exactly where round 1 predicted the budget should go. Two more are one carrier of a
two-carrier claim. If a round 3 happens, it should spend on the same two seams and skip the mechanism
argument entirely.
