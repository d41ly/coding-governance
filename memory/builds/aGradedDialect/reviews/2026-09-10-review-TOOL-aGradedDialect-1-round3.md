**Serves:** spec-audit TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5

# aGradedDialect — spec-set audit, round 3

*Node `a`, 2026-09-10, branch `branch/lexicon-kit-typescript-34c322`. Tier-2 adversarial pass over
the five-unit set: four primed lens passes, five skeptic batches prompted to REFUTE, one synthesis.
Every claim a finding made about existing code was re-checked at source before it was written here;
where a sub-claim did not survive that re-check it is named inside the finding that carried it.*

**Round: 3.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-1.md@30284eeebe521122c77d32ae9a83b4b0611fc4d1`
- `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md@d375d758180fa7cdfabacee26a500520cb2fc55e`
- `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md@8f4183643e9a3d08d14d7f21a561c7a85086b5b0`
- `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md@cedb0dd6723ffc001a0807e989eb8ed5cf64c54e`
- `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md@5e5a3ef4d33d9fe542074a58ab7f63dc5ddf4e37`

All five files hash to those blobs in the working tree at the time this record was written, checked
with `git hash-object`. Round 2 lost two subjects to mid-round drift and had to carry a re-pin
finding; this round has none, and the pins above are the bytes that were reviewed.

## Verdict: BLOCKED

Two blockers stand, and they are the same two lines of `TOOL-aGradedDialect-5` — the S7/AC7 pair
added at that unit's rev-2. AC7 names a `WIRE-INTO-PROJECT.md` lexicon section that does not exist
in the file (there is no `govkit:entry lexicon` anchor and no lexicon `rm -f` line anywhere), and
S7 scopes the population narrower than AC7 grades it, so a build doing exactly what S7 prescribes
reds its own criterion on `selftest.py`, which `tools/lexicon/kit.toml` already withholds today.
A Tier-1 records unit is being handed a deployer adoption section it never declares, its own §4
Files-touched does not name the file, and `TOOL-aGradedDialect-2` §8 F1 prices its disclosure
resolution on that step landing.

Five highs follow. Three of them are criteria that cannot fail: a circular mode comparison, a
reflexive `--is-ancestor` that certifies the exact tautology it was written to refuse, and a pure
negative satisfiable by a fixture that armed nothing. One is a declared constant nobody compares
against anything. One is a staged break that can come back GREEN, so the arm it certifies would land
with its failing case unobserved — introduced by the rev-3 fold that fixed the scope item above it.

Nothing here overturns a design decision. The `.ts`/`.tsx` mechanism pick, the earned-mode rule, the
frozen corpus and the two-parser split all held for a third round. `TOOL-aGradedDialect-1` drew no
finding that survived a skeptic.

### Review shape

Raw 38, confirmed 18, refuted 20, unverified 0. Precision 0.47.

Precision sits just under the ~0.5 floor §8 names for adding agents rather than tightening scope —
down from 0.55 in round 2, up from 0.15 in round 1. The set is now hardened enough that a fourth
round should tighten the lens priming rather than widen it. The 18 confirmed findings consolidate
into the 13 entries below: four pairs of lenses reached the same defect from different addresses,
and each entry lists the source ids it absorbs so a fold can trace any one back.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted
to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. Nothing in
this run was lost, so the zero counts here are evidence rather than a gap: the unverified set is
genuinely empty, and every lens finding reached a skeptic and was adjudicated. The consolidation in
the table below is a synthesis decision, not a pipeline discard.

**Severity is adjudicated here, not inherited.** Three moves from what the lenses filed. Finding 31
arrived BLOCKER and stays one; finding 13/34 arrived HIGH and is a BLOCKER below, on the standard
round 2 set for its lead blocker — a scope item that reds a correct build. Finding 15 arrived MEDIUM
and is HIGH below: a staged break that comes back green is the assertion-about-nothing class the
charter names by name. Finding 33 arrived HIGH and is MEDIUM below: it is a one-token citation edit
in three places, and its target is broken independently by blocker 1. The integers this record
returns are the ones in this table.

## Findings, severity-ranked

| # | severity | unit | address | one line | source ids |
|---|---|---|---|---|---|
| 1 | BLOCKER | `-5` | §2 S7, §6 AC7, §4 | AC7 names a runbook section the file does not have | 23, 31 |
| 2 | BLOCKER | `-5` | §2 S7 vs §6 AC7 | AC7's bidirectional rule reds on the `selftest.py` the kit already withholds | 13, 34 |
| 3 | HIGH | `-4` | §6 AC1 | S1's only criterion compares the scaffolder's output against the scaffolder's output | 1 |
| 4 | HIGH | `-2` | §2 S4, §6 AC4 | F2's refusal budget is readable, and compared against nothing | 2 |
| 5 | HIGH | `-2` | §4 freeze block, AC3 | `--is-ancestor` is reflexive, so one commit carrying both passes the freeze proof | 22 |
| 6 | HIGH | `-3` | §6 AC9 | a pure negative an unarmed fixture satisfies | 24 |
| 7 | HIGH | `-4` | §7 New arm, §5 | the staged break can come back GREEN | 15 |
| 8 | MEDIUM | `-2` | §5 security, §8 F1, §9 | the containment's payer is cited as S6 three times; it is S7 | 5, 33 |
| 9 | MEDIUM | `-5` | §2 S4, §6 AC4 | the superseding pointer that keeps a DEFERRED spec honest is observed by nothing | 8 |
| 10 | MEDIUM | `-4` | §4 Files touched | a `kit.toml` version edit no scope item declares, on a file with no version in it | 9, 16 |
| 11 | MEDIUM | `-5` | §4, §5, §6 AC6 | the version gate pairs four carriers; the spec says five and AC6 grades the Skill | 28 |
| 12 | LOW | `-2` | §5 perf / scale | the 880 s ceiling is typed beside the manifest that owns it | 21, 30 |
| 13 | LOW | `-3` | §5 observability | "every run prints the mode per armed extension" is wrong on both halves | 29 |

---

### 1. BLOCKER — `TOOL-aGradedDialect-5` §2 S7 and §6 AC7: the runbook has no lexicon section

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §2 S7 and
§6 AC7 (both rev-2 additions), plus §4 Files touched and §5's testing row. Against
`WIRE-INTO-PROJECT.md`, `TOOL-dScaffoldedMirror-15` (DEFERRED) and `TOOL-aHonedRuleset-9` (OPEN).

**What is wrong.** AC7 reads "its lexicon section carries a `rm -f` line". That section does not
exist. `grep -n -i lexicon WIRE-INTO-PROJECT.md` returns lines 120-122 only, which are the §0 kit
menu; the anchored adoption sections are kickoff-manifest (55), playbook (73), memory-tree (150),
drift-audit (215), codebase-map (332), memory-recall (397) and push-main (537), and there is no
`govkit:entry lexicon` anywhere in the file. The only two `rm -f` lines in it are 344 for
codebase-map and 415 for memory-recall. So S7's "gains a `rm -f` line" understates the work by the
whole section that would hold the line, AC7 cannot be observed as written, and §4's Files touched —
written before rev-2 added S7 — does not name `WIRE-INTO-PROJECT.md` at all, so nothing in the
document allocates the work. §5 then claims "no new arm, every criterion observed by an existing
merge-bar leg" over a criterion whose carrier is absent.

**Why it blocks.** `TOOL-aGradedDialect-2` §8 F1 prices its disclosure resolution on this step: with
it the price holds as priced, without it a copy-installing adopter receives the conformance corpus.
The step is also already allocated elsewhere and known missing: `TOOL-dScaffoldedMirror-15` records
`check_runbook_parity.py` exiting 1 over 18 registry entries with no anchored runbook section,
`lexicon` among them at output line 12, and says in as many words that this is "not the lexicon's
own work, and deliberately filed as its own row". `TOOL-aHonedRuleset-9` re-measures that checker as
having zero callers and no gate leg. A Tier-1 records unit whose §3 non-goals include mechanism is
being asked to author a deployer adoption section, and neither the scope item nor the file list
admits it.

**Fix.** S7 states that the file has no lexicon section today, and scopes what this unit writes: a
minimal anchored `<!-- govkit:entry lexicon -->` block in the shape of the codebase-map section at
`WIRE-INTO-PROJECT.md:333`, carrying the `cp -r` line and the `rm -f` line — or an explicit rescope
that hands the step to `TOOL-dScaffoldedMirror-15`, drops AC7, and tells `-2` §8 F1 that its
containment is deferred rather than delivered. AC7 then addresses the section by its anchor rather
than presupposing one. §4's Files touched gains `WIRE-INTO-PROJECT.md`, and §5's "no new arm"
sentence is re-read against the criterion's real carrier.

**Left-shift gate.** `check_runbook_parity.py` already computes this exact population and has zero
callers and no leg — that is `TOOL-aHonedRuleset-9`'s finding, and wiring it is the gate. Add it to
`tools/gate-legs.json` as a shrink-only ratchet keyed to today's 18, so the standing gap is carried
rather than repaired at gunpoint: a kit that gains an anchored section can never lose it, and a new
kit reds until it has one or takes a waiver row. Stage the break by deleting the codebase-map
anchor, confirm RED, unstage. The residue is not machine-gateable and joins the build's checklist:
**a criterion whose subject is a document section is grepped for that section before ratification.**

---

### 2. BLOCKER — `TOOL-aGradedDialect-5` §2 S7 against §6 AC7: the criterion reds a correct build

**Address.** Same file, §2 S7 against §6 AC7. Against `tools/lexicon/kit.toml:38-40`,
`tools/govkit/govkit.py` (`ROLE_KINDS`, `LANDABLE_ROLES`), and `WIRE-INTO-PROJECT.md:344`.

**What is wrong.** S7 scopes the new line to "the gov-only files this build ADDS to
`tools/lexicon/`, chiefly `TOOL-aGradedDialect-2`'s conformance corpus". AC7 requires the `rm -f`
line and `kit.toml`'s withheld set to agree "in either direction", and its Red-when names the exact
failure: "a file withheld from `apply` and not named in the `rm -f`". `tools/lexicon/kit.toml`
already carries `[[files]] include = ["selftest.py"] role = "project-owned"`, citing
`TOOL-aQuenchedHarness-3` and the 2026-08-23 owner ruling; `project-owned` maps to kind `order` in
`ROLE_KINDS` while `LANDABLE_ROLES` is write-only, so that file is withheld from `govkit apply`
today. It is a pre-existing file, so S7 excludes it and AC7 reds on it. `SKILL.template.md` is
arguably in the same position. The precedent AC7 invokes does not rescue the rule either:
codebase-map's own `rm -f` line omits `map_extractors.py`, which its `kit.toml` also withholds, so
the bidirectional demand is stricter than the shape it cites as its model.

**Why it blocks.** The unit cannot land green as scoped — this is round 2's lead-blocker class, a
scope item that reds a correct build, one document later. The fold that discovers it at build time
will either widen S7 silently or waive AC7, and a waived criterion is exactly where the containment
stops being observed while still reading as covered. Worth noting because it is the same defect one
level down: `kit.toml`'s own comment already asserts that "the copy-install path in
`WIRE-INTO-PROJECT.md` … does not read this file, so that runbook removes them separately" — a claim
that is false today for that file, and has been since it was written. §3's non-goals cover
mechanism, gate arms, `-13`'s §4/§8, adoption, figures and the two selftest comments; none of them
is this.

**Fix.** Widen S7 to "every file `tools/lexicon/kit.toml` withholds from `govkit apply`", naming
`selftest.py` beside the corpus (and `SKILL.template.md` if it is non-landable to the kit dir),
citing `TOOL-aQuenchedHarness-3` and the `kit.toml` comment that already promised the runbook step.
Or narrow AC7's equality to the paths this build adds, and record `selftest.py`'s absence as a
pre-existing gap with its own backlog row. Either resolves it; leaving the two ranging over
different populations does not.

**Left-shift gate.** Make the equality a checker rather than a criterion in one spec: one arm over
every `kit.toml` that withholds files from `apply`, asserting each withheld path appears in that
kit's runbook `rm -f` line and each named path is still withheld. It reds on codebase-map's
`map_extractors.py` today, which is the point — that becomes a documented waiver row or a fix, not a
surprise a future spec author rediscovers. Stage the break by dropping the corpus from the lexicon
line, confirm RED, unstage. Checklist residue: **a criterion asserting equality between two sets
names the population both sides range over, and the scope item that builds them uses the same
words.**

---

### 3. HIGH — `TOOL-aGradedDialect-4` §6 AC1: the mode comparison cannot fail

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md`, §6 AC1,
which is the only criterion on S1, the unit's central scope item. Against
`TOOL-aGradedDialect-5` §6 AC1 and `tools/lexicon/lexicon.py`.

**What is wrong.** AC1 compares the emitted `LANGS` mode against "the mode
`python tools/lexicon/lexicon.py` reports for those extensions", and under either reading of that
operand the comparison cannot fail. Over this repo, §3 of this same spec records that
`git ls-files '*.ts' '*.tsx'` returns zero and the local `LANGS` gains no `ts` token, and the only
per-extension mode output is the `lexicon OK — … coverage:` line, printed on exit 0 only — so
nothing prints and there is no operand. Over AC1's own fixture tree, `lexicon.py` builds `declared`
from the CONF via `langs(conf)`, which is the declaration the scaffolder under test just wrote, so
the criterion compares the artifact against itself. `KNOWN_EXTS` is read by nothing at runtime
except `scaffold_lexicon.py` (`KNOWN = lex.KNOWN_EXTS`, identity-asserted at `selftest.py:1349`),
which is precisely why the sibling reaches for it instead.

**Why it matters.** A scaffolder that seeds the wrong mode token passes S1's only criterion. The
"or none" case is caught — AC1's "rather than `ts::dark tsx::dark`" clause traps it — but the
mode-token half, which is the entire content of S1, is circular. This is the identical defect
`TOOL-aGradedDialect-5` AC1 folded at rev-2, whose own log says "the rev-1 wording asked for a
comparison against a string this tree cannot produce". The fold landed in one spec of two.

**Fix.** Adopt the sibling's fix verbatim: assert the emitted `LANGS` mode token equals
`lex.KNOWN_EXTS["ts"][1]` and `lex.KNOWN_EXTS["tsx"][1]` read directly from
`tools/lexicon/lexicon.py`, which is readable whatever the corpus holds and is not produced by the
artifact under test. Keep the existing dotted-key Red-when as it stands.

**Left-shift gate.** A `selftest.py` arm asserting that `--scaffold`'s emitted mode token equals
`KNOWN_EXTS` for EVERY extension the scaffolder can seed, not just the two this build arms — that
gates the class, so the next language armed inherits the check instead of re-specifying it. Stage
the break by flipping one `KNOWN_EXTS` mode, confirm RED, unstage. Checklist residue, now on its
second round: **a fold that fixes a criterion in one spec of a set greps the set for the same
phrasing before it closes.**

---

### 4. HIGH — `TOOL-aGradedDialect-2` §2 S4 and §6 AC4: the refusal budget is declared and unarmed

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md`, §2 S4
(observed by AC4), against AC5 of the same file and AC3/AC4/AC5 of `TOOL-aGradedDialect-3`.

**What is wrong.** F2, the refusal budget, has two clauses: named refusals covering at most 2% of
the corpus's oracle definition sites, and every named refusal represented by at least one fixture
the reader RAISES on. Neither is compared against anything by any criterion in the set. AC4 asserts
only that `TS_FLOOR_REFUSAL_SHARE` and `TS_FIXTURE_MINIMA` are "readable in `selftest.py`". AC2 arms
`TS_FIXTURE_MINIMA`, which is F3; nothing arms the share. AC5 scores `js-regex`, which names no
refusals, so F2 cannot bite there. On the sibling, `-3` AC3 is unterminated-construct raises, AC4 is
a docstring assertion, and AC5 enumerates "recall and precision … compared to the declared floor"
and names no refusal-share computation at all. The conformance runner is this unit's own S5, so the
arm belongs here.

**Why it matters.** §4 states F2's purpose in its own words: "Without a budget F1 is reachable by
refusing everything." A constant that is readable is not a constant that is enforced, so the guard
against a reader clearing the floor by refusing its way to it is declared and unarmed — the
fixture-passes-by-finding-nothing class this same build names, one level up. F2's second clause also
sits awkwardly against `-3` AC4's "the two that have no runtime behaviour to stage", which a fold
should reconcile in the same pass.

**Fix.** Extend AC4, or add AC6, so the conformance runner computes the share of oracle definition
sites covered by the reader's declared refusal list and asserts it against `TS_FLOOR_REFUSAL_SHARE`,
and asserts that each construct named in `parse_ts_defs.__doc__` has at least one fixture on which
the reader raises. Red-when: a refusal list naming a construct no fixture exercises.

**Left-shift gate.** Have the runner PRINT the refusal share every run beside recall and precision,
and red above the constant. A number on the report is a number somebody notices, and it carries its
own liveness: zero refusals over zero fixtures prints as "no refusals declared" rather than as a
reassuring pass, which is the charter's separate rule and the one a bare threshold check would miss.
Stage the break by declaring a refusal covering a third of the corpus, confirm RED, unstage.

---

### 5. HIGH — `TOOL-aGradedDialect-2` §4 and §6 AC3: the freeze proof passes the case it refuses

**Address.** Same file, §4's "Freezing, and what nothing checks" block and §6 AC3.

**What is wrong.** The freeze proof rests on
`git merge-base --is-ancestor <corpus-add-sha> <extractor-first-touch-sha>`, and that command is
REFLEXIVE. Verified live on this tree: `--is-ancestor $H $H` exits 0, and the reversed order exits
1. So a single commit carrying both the corpus JSON and `scan_ts_tokens` makes the two shas equal
and passes the check that exists to prove one preceded the other. AC3's Red-when — "the extractor's
first-touch commit is not a descendant" — does not trap it either, because a commit is its own
descendant.

**Why it matters.** §4 says the corpus lands "in a pass that PRECEDES the first commit touching the
TypeScript extractor", and the degenerate case the check waves through is exactly the
fixtures-and-reader-authored-together shape `TOOL-dScaffoldedMirror-13`'s tautology objection names.
This is the build's whole answer to that objection. §4's candid "what nothing catches" paragraph
lists only the expectation-editing hole, so the document does not know about this one.

**Fix.** In §4's block and in AC3, require the two shas to DIFFER as well as to be ordered: capture
both, assert `[ "$corpus_sha" != "$ext_sha" ]` before `--is-ancestor`, and add a Red-when reading
"the two queries return the SAME sha, which is the fixtures and the reader landing in one pass and
is the case the ordering exists to refuse".

**Left-shift gate.** Move the ordering-and-inequality proof out of prose and into a script — a
`drift-audit` signal is the natural home, since it is a question about whether the record still
describes the tree — and have it print both shas so a reader sees which commits were compared. That
is the liveness assertion the procedure has none of today: a prose check that nobody runs and a
prose check that ran and passed look identical in a review. Stage the break with a scratch repo
where both land in one commit, confirm RED, discard the scratch repo.

---

### 6. HIGH — `TOOL-aGradedDialect-3` §6 AC9: a negative an unarmed fixture satisfies

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md`, §6 AC9
(rev-2 addition). Against `tools/lexicon/lexicon.py` around lines 1479 and 1615, and AC5 of this
same file.

**What is wrong.** AC9 is a pure negative: the run "reports an EMPTY `blind` set and prints no
`DEAD SNIFFER`". `blind = sorted(extractor_carriers - carriers)`, and `extractor_carriers.add(rel)`
runs only under `if funcs or types_` inside `scan_corpus`'s armed branch, with `DEAD SNIFFER`
appended only `if blind`. An empty `blind` is therefore produced equally by a working
`DEFINITION_SNIFF` widening and by a fixture that armed nothing (a conf typo leaving `ts::dark`),
refused to parse (a `SyntaxError` from the new reader), or extracted nothing.

**Why it matters.** The arm would certify a widening that was never made. That is the
fixture-passes-by-finding-nothing class this same spec names in AC5's Red-when, one criterion above
— AC5 already carries the guard ("the arm reports a score over an empty or absent fixture set"), so
the asymmetry is internal to the document. §7's staged-break line certifies the arm at landing only;
it is not a standing liveness assertion, which is the charter's separate rule about a signal that
reports a reassuring zero when it is broken.

**Fix.** AC9 gains a POSITIVE precondition asserted in the same run, before the negative counts: the
run reports non-zero graded populations for `ts` and `tsx`, both fixture files appearing as
extractor carriers. Then add a second Red-when: "the arm reports an empty `blind` set over zero
extractor carriers, which is the fixture proving nothing rather than the sniffer agreeing."

**Left-shift gate.** Make the engine print the extractor-carrier count beside `blind`, and give the
`selftest.py` helper that asserts an empty `blind` a REQUIRED expected-carrier-count argument. Then
a negative assertion cannot be written without stating the population it ranges over, and every
future sniffer arm inherits the guard rather than re-deriving it. Stage the break by pointing the
fixture at an empty directory, confirm RED, unstage.

---

### 7. HIGH — `TOOL-aGradedDialect-4` §7 and §5: the staged break can come back GREEN

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md`, §7's
"New arm" line and §5's testing row, against §2 S4 and §6 AC4 as amended at rev-3.

**What is wrong.** Both carriers still describe the pre-rev-3, mode-keyed break: "point a
`KNOWN_EXTS` parser id at a name `PARSERS` does not hold". Rev-3 amended S4 and AC4 to the permissive
rule — an id that "resolves in `PARSERS` OR in `PATTERN_SETS`". Verified at source:
`PARSERS = {"python-ast", "shell-tokens"}` and `PATTERN_SETS` holds exactly one key, `js-regex`. So
`js-regex` IS a name `PARSERS` does not hold, and it resolves in `PATTERN_SETS`, which satisfies the
permissive rule. A builder following §7 literally stages a break that comes back green.

**Why it matters.** The arm then lands without its failing case ever observed — the
assertion-about-nothing class the charter names by name, introduced by the very fold that fixed the
scope item. Rev-3's own log names only S4 and §3 as amended, so §5 and §7 are the two carriers it
missed: the same one-carrier-of-three mistake it was folding. The second staged break, a
`SEED_CONVENTIONS` value outside `CONVENTIONS`, does red — but it exercises a different clause, so
AC4's resolution arm is still uncertified.

**Fix.** Restate the break in both carriers to match the permissive rule: point a `KNOWN_EXTS`
pattern-set id at a token present in NEITHER `PARSERS` nor `PATTERN_SETS`, on a non-final catalog row
(AC4's own Red-when), and keep the `SEED_CONVENTIONS` half as written.

**Left-shift gate.** The staged break belongs in the arm, not in a sentence: a mutation fixture in
`selftest.py` that applies the break to a copy of the catalog and asserts the checker REDs. Then
"has the failing case been observed" is answered by the suite on every run rather than by a builder
following prose once, and a rule change that invalidates the break reds instead of passing quietly.
Checklist residue: **a fold that amends a rule greps its own spec for every carrier of the old
wording, staged breaks and risk rows included.**

---

### 8. MEDIUM — `TOOL-aGradedDialect-2` §5, §8 F1 and §9: the containment's payer is the wrong item

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md` lines 253
(§5 security row), 333 (§8 F1) and 356 (the rev-3 log). Against `TOOL-aGradedDialect-5` §2.

**What is wrong.** All three name `TOOL-aGradedDialect-5` S6 as the copy-install runbook step. In
spec 5, S6 is the kit version bump — "the lexicon kit version is bumped ONCE for this build",
observed by AC6 — and the `WIRE-INTO-PROJECT.md` `rm -f` line is S7, created new at that unit's
rev-2 with AC7. Cross-confirmed from the other side: spec 3's S7 says the version stamp is spec 5's,
and spec 5 §8 F2 allocates the bump to spec 5 alone.

**Why it matters.** This is the pointer the round-2 fold introduced to give the disclosure decision
a payer. A reader checking whether the containment was allocated opens S6, finds a version bump, and
reads the obligation as unowned — the half-containment the fold was written to close. The cross-read
that is supposed to catch a disagreement between two specs resolves to the wrong row and reports
agreement. Filed HIGH by its lens; MEDIUM here, because it is a one-token edit and the target it
should point at is broken independently by blocker 1.

**Fix.** Retarget all three occurrences to `TOOL-aGradedDialect-5` S7 / AC7, and add the correction
to §9's rev log so the next fold does not re-derive it from scratch.

**Left-shift gate.** A hygiene arm resolving every `TOOL-<slug>-<n> S<k>` / `AC<k>` cross-citation
inside a build folder against the target spec's own numbered lists, reding on a citation whose
target does not exist. Honestly stated: it would NOT have caught this one, because S6 exists — it
catches out-of-range citations and every future renumber, which is the larger population. The rest
goes on the checklist: **a cross-spec S/AC citation is opened and read, never pattern-matched, and a
fold that adds a scope item mid-list re-reads every sibling citing that spec.**

---

### 9. MEDIUM — `TOOL-aGradedDialect-5` §2 S4 and §6 AC4: half the scope item is unobserved

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §2 S4
observed by §6 AC4, against §4's Files touched and §8 F1.

**What is wrong.** S4 scopes two artifacts — the backlog row moving off `DEFERRED` with a re-aimed
pointer, and `TOOL-dScaffoldedMirror-13`'s spec status-header tail gaining a superseding pointer.
AC4 reads only `memory/backlog/TOOL.md`: a non-`DEFERRED` token, a pointer to `builds/aGradedDialect/`,
and hygiene staying green. Nothing in AC1-AC7 reads
`memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-13.md`, which §4's Files
touched names "header tail only"; AC3's grep is scoped to `tools/` and AC5 is the map ratchet.

**Why it matters.** §8 F1 rests its whole resolution on that pointer — "a reader meeting `DEFERRED`
is told where the ruling went" — and in the same breath records that
`drift_report.build_backlog_rows_outliving_specs` watches the opposite direction. So the one
artifact keeping a live-`DEFERRED` spec from reading as current is observed by neither a criterion
nor a drift signal.

**Fix.** Add a clause to AC4: that spec's status-header tail names `builds/aGradedDialect/` as the
superseding record. Red-when: the backlog row moves off `DEFERRED` while that header still points
nowhere.

**Left-shift gate.** Add the mirror direction to `drift-audit`, since the forward one already exists:
a spec whose status header carries a non-terminal status, whose backlog row is no longer `DEFERRED`,
and which names no superseding record, is a signal. That reaches every such pair in the tree rather
than this one, and it costs one predicate beside a function that already walks the population.

---

### 10. MEDIUM — `TOOL-aGradedDialect-4` §4: a version edit no scope item declares

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-4.md`, §4 Files
touched (estimate). Against `TOOL-aGradedDialect-5` §4 and §8 F2, and `TOOL-aGradedDialect-3` S7.

**What is wrong.** The table lists `tools/lexicon/kit.toml` for "the kit version, shared with units 3
and 5 rather than owned here", and the gloss is false on both halves. Unit 3's rev-2 struck the
identical claim from its S7 and Files touched. Unit 5 §8 F2 resolves the bump to unit 5 alone, once,
and says outright that "a sibling spec claiming the same edit is a disagreement a cross-read can
see" — this is that disagreement. And `kit.toml` carries no version literal at all: it declares
`version_from = { file = "lexicon.py", pattern = "^KIT_LEXICON_VERSION = " }`, with the literal
living at `lexicon.py:78`. Unit 4 has no §2 scope item and no §6 criterion touching a version.

**Why it matters.** Three specs give three answers to who touches `kit.toml` for the version, and the
one claiming the edit describes a file that derives the value rather than repeating it. A builder
acting on the row edits the `version_from` pattern or adds a second literal. One overstatement from
the lens is worth recording: `check-kit-versions.sh:242` greps `lexicon.py`, not `kit.toml`, so the
derivation would not break as loudly as the finding claimed. The row is still wrong on its face.

**Fix.** Delete the `kit.toml` row from this unit's Files touched, or restate it as "not touched —
the version is `TOOL-aGradedDialect-5` S6", matching the correction already folded into unit 3.

**Left-shift gate.** Not gateable as prose, and the durable answer is that the carriers are DERIVED:
`check-kit-versions.sh` already enumerates them from `version_from`, so a spec's carrier claim can be
answered by running it rather than by typing a list. Checklist residue: **a Files-touched row with no
scope item and no criterion behind it is deleted, not hedged** — "rather than owned here" is the
hedge that let this one survive two folds.

---

### 11. MEDIUM — `TOOL-aGradedDialect-5` §4, §5 and §6 AC6: the version gate pairs four, not five

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-5.md`, §4's "The
version bump", §5's observability row and §6 AC6. Against `tools/check-kit-versions.sh:250-256`.

**What is wrong.** That script iterates `for kept in lexicon.py canon.py README.md LEXICON.md`, and
its own comment says the Skill is "deliberately absent from the list: it is RENDERED from the
constant and cannot drift". §5 nevertheless says the `kit version markers` leg "reds when the five
carriers disagree", and AC6 asserts "the marker in every carrier" under that gate.

**Why it matters.** AC6 cannot observe the half of S6 that says "the Skill is re-rendered so its
marker agrees". A bump that re-stamps the four kit files and never re-renders
`.claude/skills/lexicon/SKILL.md` leaves AC6 green. Coverage does exist — `lexicon wiring`
byte-compares the rendered Skill, and §7 names that leg — which is exactly the problem: the spec
attributes the coverage to the wrong gate, and a session trusting §4's sentence would ship a stale
Skill marker believing the version gate guards it. This repo already keeps a gotcha for the
multi-carrier stamp trap, whose own remedy names only three carriers.

**Fix.** §4 and §5 say the version gate pairs FOUR carriers and name `lexicon wiring`
(`adopt-lexicon.sh --check`) as the Skill's guard. Split AC6: the four-carrier equality under
`bash tools/check-kit-versions.sh`, plus a second clause requiring `lexicon wiring` green over the
re-rendered Skill. Red-when: the Skill was not re-rendered and AC6 passed anyway.

**Left-shift gate.** Have `check-kit-versions.sh` PRINT the carrier list it compared, so a spec
claiming five against a run printing four is visible in the log rather than only in a review. Cheaper
and more durable: extend the existing "stamps are not one stamp" gotcha with this pair, since it is
the same trap and its remedy is already known to be short.

---

### 12. LOW — `TOOL-aGradedDialect-2` §5: the leg ceiling is typed beside the file that owns it

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-2.md`, §5's
perf / scale row, line 255. Against `tools/gate-legs.json` and `TOOL-aGradedDialect-3` §5.

**What is wrong.** The row reads "It sits inside an 880-second leg ceiling" — a bare literal with no
`figure:` pin and no date. `tools/gate-legs.json` owns it (`"name": "lexicon selftest" … "ceiling":
880`), and the sibling already folded this exact shape out of itself: `-3`'s rev-2 log says its §5
"stated a 300 s leg ceiling against a manifest that declares roughly three times that, which is a
number typed beside the source that owns it and is what this build's README forbids".

**Why it matters.** Correct today, unowned tomorrow — when the manifest moves, one spec in this set
points at it and its sibling states a stale figure, with no gate between them. It is also this
build's own acceptance bar and the repo's charter rule, applied by one of this set's folds and not
the other, so the next fold has to pick a precedent instead of following one.

**Fix.** Use the sibling's wording: the wall-clock ceiling is the `lexicon selftest` row in
`tools/gate-legs.json`, read there and deliberately not typed here.

**Left-shift gate.** Gateable and cheap: a hygiene arm over build-folder records for a bare
multi-digit figure adjacent to "ceiling" that does not name `tools/gate-legs.json` in the same item.
Run the predicate over the real tree and print hits AND near-misses before wiring it — a corpus this
prose-heavy will surface live instances beyond this one, and it may also red innocent rows. If the
false-positive rate is bad, it goes on the checklist instead: **a figure a tracked file owns is
cited, never typed.**

---

### 13. LOW — `TOOL-aGradedDialect-3` §5: the observability row describes output that does not exist

**Address.** `memory/builds/aGradedDialect/spec/2026-09-10-spec-TOOL-aGradedDialect-3.md`, §5's
observability row. Against `tools/lexicon/lexicon.py:1992` and `run()`/`check_pass`.

**What is wrong.** "Every run already prints the mode per armed extension" is wrong on both halves.
The unconditional per-run output is the counts, the self-containment line, the
`coverage — armed N of M` fraction and the UNDECLARED CELL list, none of which carries a mode. The
only mode-per-extension line is `lexicon OK — … coverage: {modes}`, inside `if exit_code == 0`, and
it iterates `declared` — every declared extension including the dark ones, not the armed ones.

**Why it matters.** The overstatement runs in the direction that matters: on a RED run, which is the
run a reader most wants the shipped mode from, there is no mode line at all. A session relying on
this sentence after a failure finds nothing, and AC6's printed verdict is then the only carrier.

**Fix.** Reword the row to name the real site and its condition — the green `lexicon OK` line prints
a mode for every declared extension, dark ones included, and prints nothing on a red run — and state
that the conformance arm's own printed verdict is what carries the mode on a failure.

**Left-shift gate.** One edit removes the falsity instead of documenting it: move the coverage line
out of the green branch so it prints on both verdicts. Stage the break by forcing a red run and
asserting the mode line still prints; that arm then holds the claim true for every future reader of
this row.

---

## What held

- `TOOL-aGradedDialect-1` drew no finding that survived a skeptic, for the first time in three
  rounds. With 4/4 lenses and 5/5 skeptic batches returning, that is evidence rather than a gap.
- The `.ts`/`.tsx` mechanism pick, the earned-mode rule, the two-parser split and the frozen
  conformance corpus were all attacked again and all held.
- Round 2's two blockers are closed. Unit 4's S4 now states the permissive resolution rule — finding
  7 above is that fix's own missed carriers, not a regression of the rule — and the `DEAD SNIFFER`
  obligation now has an owner.
- Eight of the eleven entries below BLOCKER are one class: a claim, an edit or a handoff that lives
  in one carrier and is observed in none. The build's §1 goal is removing prose that answers a
  question the code answers differently, and the set is still committing new instances of it while
  closing the old ones. That is the pattern a fourth round should prime its lenses on first.
