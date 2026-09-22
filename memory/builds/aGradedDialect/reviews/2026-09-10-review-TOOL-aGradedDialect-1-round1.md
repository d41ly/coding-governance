**Serves:** spec-audit TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5

# aGradedDialect — spec-set audit, round 1

Tier-2 adversarial spec audit of the five-unit set, run 2026-09-10 on node `a`, branch
`branch/lexicon-kit-typescript-34c322`. Four lens passes, five skeptic batches, one synthesis.

**Subjects, pinned at the blob each was read at.** ROUND 1.

| unit | subject | blob |
|---|---|---|
| `TOOL-aGradedDialect-1` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-1.md` | `be2992a73854c4baba26542757ad2751e779117c` |
| `TOOL-aGradedDialect-2` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md` | `e8367ab2a651aa819d81bbb313dab9fe515033f3` |
| `TOOL-aGradedDialect-3` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md` | `c86bd3b87000b1bab3b071774d4408e53e5709a2` |
| `TOOL-aGradedDialect-4` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md` | `0e4737055a571cddbb966b5943a5d45d86560411` |
| `TOOL-aGradedDialect-5` | `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md` | `306868344fbbb095bc293a2d1420bd51b90f0a75` |

## Verdict: BLOCKED

Three blockers and one high survived the skeptic. Each of the three blockers is an acceptance
criterion that cannot be observed as written: one names a script that exists nowhere, one pins a
verdict the build has not measured yet, and one proves an ordering with a git query that returns a
commit from three weeks before the build started. None of them is a matter of taste, and all four
findings are repairable by editing the specs — no design decision is overturned here.

The `.ts`/`.tsx` mechanism pick itself survives. The lenses attacked C2 from four directions and
none of the attacks held: the losing conditions really are pre-registered, the oracle really is a
compiler this build does not ship, and the `case:` refusal in unit 1's record §5 is argued rather
than assumed. What is broken is the EVIDENCE CHAIN around that pick, not the pick.

### Review shape

Raw 26, confirmed 4, refuted 22, unverified 0. Precision 0.15.

That precision is well under the ~0.5 floor §8 names, and the reading is about priming rather than
about the specs. Twenty-two findings died on the skeptic because lenses were re-deriving arguments
the specs had already made and lost — three separate lenses filed the `case:` selector as an
unconsidered gap when unit 1's record §5 refuses it explicitly, and the mode-earning rule drew
repeat fire for the same reason. A round 2 over this set should feed the lenses unit 1's §5 and
unit 3's §8 as by-design up front, and should spend its budget on cross-unit contradictions, which
is where all four survivors came from.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted
to unverified, 0 spurious verdicts discarded, 0 duplicates. Nothing in this run was lost, so a zero
count below is evidence rather than a gap: the unverified set is genuinely empty, and no lens
finding went unadjudicated.

---

## Findings, severity-ranked

| # | severity | unit | address | one line |
|---|---|---|---|---|
| 1 | BLOCKER | `-1` | §4 Design, §5, AC3 | AC3 names `regex_vs_oracle.py`, which exists nowhere in the tree |
| 2 | BLOCKER | `-4` | §2 S1, §4 Data model, AC1 | the `parser` mode is hard-coded one unit before unit 3 measures it |
| 3 | BLOCKER | `-2` | §4 freeze block, AC3 | the freeze proof resolves unit 3's extractor by file-add; unit 3 adds no file |
| 4 | HIGH | `-1` | §2 S5, AC5 | AC5 observes the record's §5 alone; the three losses live in §3 and §4 |

---

### 1. BLOCKER — `TOOL-aGradedDialect-1` §4 Design, §5 observability, AC3: the losing test cannot be re-derived by anyone

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-1.md`, §4 Design
(line 64), §5 Production-readiness (the `observability` bullet), and §6 AC3 (line 113). Against
`memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md` §3, and against
`memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md`
§6.

**What is wrong.** §4 asserts "Its §6 carries both probe snippets runnable, so every figure
re-derives", and §5 repeats that claim as the whole observability answer. The record's §6 carries
`ts-oracle.js` and nothing else; `regex_vs_oracle.py` is named in the §6 prose and forwarded to
`spec-TOOL-aGradedDialect-2 §4`, which does not contain it. Unit 2 §3 says so in its own words: the
script's "bytes were not committed", and unit 2 calls the forward-pointer "a defect in that record".
Two specs in one set state opposite facts about the same artifact. A grep over the worktree finds
the name in three markdown files and the script in none; `find` confirms no such file is tracked or
untracked anywhere.

**Why it blocks.** AC3 is the criterion carrying the entire pre-registered losing test — the 22.4%
inter-regex disagreement on the function population, which is what kills C1 and C4 and is quoted
again in unit 3's Alternatives-rejected table as the reason a `ts-regex` `PATTERN_SETS` entry loses.
The number is therefore load-bearing across two units, and it re-derives from nothing. §7 adds no
gate arm for this unit, which is why nothing caught it.

**Fix.** Commit `regex_vs_oracle.py`'s source into the record's §6 beside `ts-oracle.js`, with both
readings' eight patterns included, and delete the forward-pointer. Failing that, amend §4 and §5 to
say ONE snippet is runnable and rewrite AC3 to observe a figure that actually re-derives. Do not
leave the pointer aimed at unit 2 §4 — unit 2 has already declined to carry it, in writing.

**Left-shift gate.** Extend the existing spec-token check into an ARTIFACT-EXISTENCE arm: for every
spec, each backticked token matching `*.py`, `*.js` or `*.sh` inside a scope item or an acceptance
criterion must resolve to a tracked path, to a fenced code block inside a record the spec's
`gen:spec-records` table binds, or to an explicit Files-touched row in the unit that creates it. Red
otherwise. The same arm catches finding 3, so it is one gate for two blockers. Stage the break by
renaming the `ts-oracle.js` fence label, confirm RED, unstage.

---

### 2. BLOCKER — `TOOL-aGradedDialect-4` §2 S1, §4 Data model, AC1: the mode verdict is pre-empted one unit before it is measured

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md`, §2 S1
(line 16), §4's Data model table (lines 76 and 77), and §6 AC1 (line 168). Against
`spec-TOOL-aGradedDialect-1.md` §3 and `spec-TOOL-aGradedDialect-3.md` §2 S5, §3 Edges, AC6 and
AC7.

**What is wrong.** Unit 4 writes the mode as a literal in three places: S1 says the two `KNOWN_EXTS`
rows land "each at mode `parser`", §4's table pins `("ts-tokens", "parser")` and
`("tsx-tokens", "parser")`, and AC1 asserts the emitted `LANGS` line names `ts` and `tsx` "at mode
`parser`". But that token is a VERDICT unit 3 hands over, not a constant. Unit 3 S5 calls it "the
mode verdict this unit hands `TOOL-aGradedDialect-4`", its Edges hand it off in those words, and AC6
makes it measured — `parser` at or above unit 2's floor, `probe` below it. Unit 1 §3 forbids the
claim outright: "No `parser` claim … asserting it here would be the could-not-fail shape." Nothing
in unit 4 conditions its rows on the verdict.

**Why it blocks.** If unit 3's reader scores below the floor and correctly declares `probe`, unit
4's AC1 reds on a CORRECT build, and the only way to green it is to write the label the whole build
exists to refuse. The damage runs the other way too: unit 3 §8 F1 spends two dispatch edits
specifically so a tokenizer-shaped reader is reachable under `probe`, and its AC7 grades exactly
that shape — a `probe` row whose pattern-set id names a parser. Unit 4's declaration never emits
that configuration, so the widening's only consumer is unreachable and F1's cost buys nothing.

**Fix.** In S1 and in §4's table, write the mode as the verdict rather than the literal: "each at
the mode `TOOL-aGradedDialect-3` earned, `parser` or `probe`". Rewrite AC1 to assert that the
`LANGS` line names `ts` and `tsx` at the mode `python tools/lexicon/lexicon.py` prints for those
extensions — the shape unit 5's AC1 already uses, and the reason unit 5 is not implicated in this
finding. Keep AC1's dotted-key Red-when exactly as it stands; it is a good trap and is unrelated.

**Left-shift gate.** A runtime arm in `tools/lexicon/selftest.py`: for every `KNOWN_EXTS` row at
mode `parser`, assert the conformance verdict artifact records a score at or above the declared
floor for that extension, and red when a `parser` row has no conformance score at all. That makes
the label a function of the measurement in code rather than in prose, so no future spec can pin it
by hand. Stage the break by flipping one row to `parser` with the score withheld, confirm RED,
unstage.

---

### 3. BLOCKER — `TOOL-aGradedDialect-2` §4 freeze block, AC3: the ordering proof reds on a correct build

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md`, §4
"Freezing, and what nothing checks" (the shell block at lines 184-186) and §6 AC3 (line 260).
Against `spec-TOOL-aGradedDialect-3.md` §4 "Files touched (estimate)".

**What is wrong.** AC3 proves the corpus was frozen before the extractor existed with
`git log --diff-filter=A -- tools/lexicon/ts-conformance-fixtures.json`, the same query for
`tools/lexicon/ts-tokens.py` (commented "# unit 3's file, whatever it is named"), and
`git merge-base --is-ancestor` between the two. Unit 3 adds no new file. Its §4 states "The seam is
`tools/lexicon/lexicon.py`", and its Files-touched table lists `lexicon.py`, `selftest.py`,
`.lexicon.conf` and the rendered `SKILL.md` — every one of them already tracked. `git log
--diff-filter=A -- tools/lexicon/lexicon.py` returns `0007b357`, dated 2026-08-16, which predates
any corpus commit by weeks.

**Why it blocks.** The ancestor test is FALSE for a perfectly correct build, so AC3 reds on the
sequencing it exists to certify. This is the documented check answering `TOOL-dScaffoldedMirror-13`'s
tautology objection — the build README's own acceptance bar — so the objection ends up unanswered
while a green-looking review record says otherwise. The `whatever it is named` comment shows the
author assumed a new file that unit 3 explicitly does not create; the assumption, not the intent, is
the defect.

**Fix.** Re-anchor the extractor half on the first commit that TOUCHES the extractor rather than the
one that adds its file: `git log --format=%H --reverse -S'scan_ts_tokens' -- tools/lexicon/lexicon.py`
(`-S'ts-tokens'` works equally well), taking its first sha as `<extractor-add-sha>`. Keep the
`--diff-filter=A` form for the corpus JSON, which genuinely is a new file. Update the §4 block and
AC3's Red-when in the same edit, and drop the `ts-tokens.py` filename entirely so no later reader
inherits the assumption.

**Left-shift gate.** Covered by the artifact-existence arm proposed under finding 1: a path named
inside a spec's shell block or acceptance criterion must resolve against `git ls-files` or against
the Files-touched table of the unit that creates it. `tools/lexicon/ts-tokens.py` satisfies neither
and would have redded at ratification. Add a second, cheaper arm beside it — any spec shell block
containing `--diff-filter=A` must name a path that is not already tracked at the build's base sha,
because proving a file's birth is meaningless for a file already born.

---

### 4. HIGH — `TOOL-aGradedDialect-1` §2 S5, AC5: the criterion is red against the record it already has

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-1.md`, §2 S5
(lines 30-31) and §6 AC5 (line 121). Against
`memory/builds/aGradedDialect/build/2026-09-10-build-TOOL-aGradedDialect-1-typescript-extraction-research.md`
§3, §4.1, §4.3 and §5.

**What is wrong.** S5 scopes "record the pick, the three losses with the test that killed each, and
the one problem the pick does not solve", and AC5 narrows the observation to "§5 of the record". The
record's §5 names the pick, the M3 tie-break, the parser-must-be-earned rule, the `.tsx` role-split
problem and the `case:` refusal. The three losses and the tests that killed them are not there: they
live in §3's loses-if table, in §4.1 (C1 and C4 lose, the 22.4% figure) and in §4.3 (C3's veto).
§5's only gesture at them is "the most feature-rich survivor after the vetoes", which names no
candidate and no test.

**Why it is high rather than a blocker.** The work exists and is correct; only the criterion's
address is wrong, and this unit is INPROGRESS with its record already written. It still bites: a
closing review reading AC5 literally must either duplicate §3 and §4 into §5 — one fact in two
carriers with no gate between them, which unit 1 §4 names as this build's own bar — or quietly
reinterpret the criterion, which is how an acceptance criterion stops meaning anything.

**Fix.** Amend AC5 to address the sections that carry each clause: "When the record's §3, §4 and §5
are read, §3 names the four losing conditions, §4.1 and §4.3 report the three losses against them,
and §5 names the pick, the `.tsx` role-split problem and the `case:` refusal by the vacuity
argument." Leave the Red-when unchanged — it is about a claim the record does not make and is still
the right trap.

**Left-shift gate.** Only half of this class is gateable, and the record should say which half. The
cheap arm: an acceptance criterion citing `§N` of a record in the build folder reds when that record
has no section `N`. It would not have caught this one, because §5 exists. The rest belongs in the
build's own recurring-class checklist as a documented manual check, per §7's rule for findings whose
class no gate reaches: **an AC that narrows its observation to ONE section of a record is read
against that record before the spec is ratified, and the section list is widened to wherever the
scope item's clauses actually landed.** Two of this round's four survivors are cross-carrier address
errors, which is what makes the class worth writing down rather than fixing once.

---

## What was attacked and held

Recorded so round 2 does not re-buy it. The mechanism pick (C2) survived four independent attacks:
the losing conditions are pre-registered ahead of the measurements, the oracle is `typescript@5.9.3`
from the adopter tree rather than anything this kit ships, the `case:` selector kind is refused by an
argued vacuity case in the record's §5 rather than overlooked, and the two-parser-ids decision is
argued on migration cost with the trade named as a trade. Unit 5's AC1 phrases the mode against the
tool's own output and is the shape finding 2 asks unit 4 to adopt. Unit 3's refusal list, its
`SyntaxError` contract and its rejection of a new mode token all held.
