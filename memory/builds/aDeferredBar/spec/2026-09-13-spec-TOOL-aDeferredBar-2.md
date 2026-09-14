# TOOL-aDeferredBar-2 — the spec gate: a bar or suite invocation is not an acceptance observation

**Status:** CLOSED · rev-4 · 2026-09-14 · node a · Tier-2 · base b2a330be · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md](../build/2026-09-13-build-TOOL-aDeferredBar-1-1-research-bar-in-a-pass.md) | research | TOOL-aDeferredBar-1 TOOL-aDeferredBar-3 |
| [2026-09-14-build-TOOL-aDeferredBar-2-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-aDeferredBar-2-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-aDeferredBar-2-1-spec-brief.md](../prompts/2026-09-13-prompt-TOOL-aDeferredBar-2-1-spec-brief.md) | journal | — |
| [2026-09-14-prompt-TOOL-aDeferredBar-2-2-build-brief.md](../prompts/2026-09-14-prompt-TOOL-aDeferredBar-2-2-build-brief.md) | journal | — |
| [2026-09-14-review-TOOL-aDeferredBar-1-closing-diff-round1.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-closing-diff-round1.md) | diff-review | TOOL-aDeferredBar-1 TOOL-aDeferredBar-3 |
| [2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round1.md) | spec-audit | TOOL-aDeferredBar-1 TOOL-aDeferredBar-3 |
| [2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aDeferredBar-1-spec-audit-round2.md) | spec-audit | TOOL-aDeferredBar-1 TOOL-aDeferredBar-3 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-spec-tokens.py` gains a fourth join, `bar`: in a live spec dated at or after a new
`.memory-tree.conf` cutoff, a backticked token inside an acceptance-criteria bullet — the section
found by its heading text, so a light-profile spec is graded where its criteria actually sit — or on
the `## 7. Gates` leg line that spells a merge-bar or self-test-suite invocation is a hit. It refuses
the instruction at the cheapest point — the writer, before any child agent reads it — because the
research record under `build/` traced one unit's 68-minute stall to exactly such a token in its AC8.
Tier-2 by the manifest's tier rule: it changes the spec template's rules and a shipped kit's conf.

## 2. Scope (IN)

- **S1** — The join itself in `tools/check-spec-tokens.py`: the predicate, the two populations it
  reads — the acceptance section located by heading text through `AC_HEAD` and
  `extract_acceptance`, the leg line as today — the cutoff read through `read_conf_key`, the hit
  kind `bar`, a refusal text that names the substitute, a report line printed on every run, and a
  REFUSAL of a cutoff value that is not strictly past the date of the commit that set it, naming the
  key, the value and that date (§4 Date gate). Observed by AC1, AC2, AC3, AC4, AC5, AC8, AC15, AC16
  and AC17.
- **S2** — The module docstring: the population list gains the fourth join and says the bullet loop
  now finds the acceptance section by heading text; the WHAT IT DOES NOT CHECK paragraph gains what
  this join cannot see — a path built at runtime, the body of a `sh -c` string, the body of a fenced
  block, and a suite named in prose. Each of those five clauses carries one pinned phrase, spelled in
  §4 Docstring phrases and grepped by AC18, so a clause dropped or half-written reds rather than
  reading as covered.
- **S3** — `--list` prints every near-miss of the predicate as a `NEAR` line, exit 0. Observed by
  AC3 and AC9.
- **S4** — The key `SPEC_DIRECT_CUTOFF` in `.memory-tree.conf` at the relation's answer at the
  build commit — 2026-09-15 by both clauses as measured 2026-09-14, re-derived at that commit and
  again at landing — with a register comment in the idiom of its neighbours that carries both
  clauses of the relation and the reading §4 Rollout records, and a blank row in
  `tools/memory-tree/.memory-tree.conf.example`. Observed by AC8 and AC14.
- **S5** — Ten arms in `tools/check-spec-tokens.test.sh`, sharing one scratch repo per fixture
  family, and its assertion floor `FLOOR_ASSERTIONS` moved from 20 to 32, the count the suite prints
  when every arm runs. Observed by AC1 through AC7, AC15, AC16 and AC17, each arm's fixture exercised
  by the direct checker, and the floor by AC19; the suite's own verdict is the main loop's at
  `VERIFYING`, per the build README's rule 6.
- **S6** — One paragraph in `tools/memory-tree/SPEC-TEMPLATE.template.md` under the §6 rules,
  beside the `SPEC_WITNESS_CUTOFF` and `SPEC_FAILURE_MODE_CUTOFF` paragraphs, stating the rule and
  the substitute; rendered to `memory/TEMPLATE-SPEC.md`. Observed by AC10.
- **S7** — The memory-tree version step: `KIT_MEMORY_TREE_VERSION` in
  `tools/memory-tree/check-memory-hygiene.sh` and the `gov:kit memory-tree@` marker on every
  `tools/memory-tree/*.template.md` and every rendered copy, one step past the value unit 1 leaves.
  Observed by AC11.
- **S8** — The kickoff manifest's `last-audit` re-stamp, owed because `.memory-tree.conf` and the
  engine are both on its `watch:` line. Observed by AC12.
- **S9** — The dossier `memory/map/features/spec-tokens.md` refreshed from three joins to four, and
  the generated map re-rendered if the checker edit moves it. Observed by AC13.
- **S10** — `memory/project/spec-token-waivers.txt` untouched. Observed by AC8.

## 3. Non-goals (OUT)

- The memory hygiene gate gains nothing. The spec-token checker already extracts both populations
  and owns the waiver registry; a second extractor for the same population is the two-mechanisms
  defect M2 exists to prevent.
- No live spec of another build is rewritten, and there is no drain, and nothing in flight is
  folded. What was measured, and where: at `b2a330be`, 23 live specs carry such a token, the newest
  dated 2026-09-04; at `dd8968c4`, the tip this rev-3 was folded against, the count is 24, because
  unit 3's AC9 there backticks a bare suite basename — round-2 M2, whose fold in the same rev-3
  commit as this one takes the count back to 23. Measured 2026-09-14 over every local and remote
  ref (77) and every live worktree by the §4 command, the newest spec filename date anywhere is
  2026-09-13, and four live specs at that date on two other refs carry a bar token — tooling unit 5
  of build aBatchedArm, and kickoff units 1 and 2 plus tooling unit 1 of build aReplayedCard, named
  in full by the round-1 audit and paraphrased here so this file does not cite ids the tree never
  defines. The cutoff — 2026-09-15 as measured 2026-09-14, and the relation's answer at the build
  commit and again at landing — sits strictly past every one of them AND past the day it is set, so
  none reds at its merge and none needs a fold — this build's own three specs included, which are
  dated 2026-09-13 and are therefore not graded either — and a spec any node dates on the setting
  day cannot red either, which is what the relation's second clause buys and what rev-2's value,
  the measuring day itself, did not (round-2 H1).
- The act — a bar run that no spec named — is `TOOL-aDeferredBar-3`'s, and the wording at the
  method's M6 and at the manifest is `TOOL-aDeferredBar-1`'s. This unit sees only the instruction
  as a spec writes it.
- No leg-selection flag for the runner, no environment override for the key
  (`TOOL-aDeclaredBound-2` removed the last such channel), and no change to the waiver registry's
  one-token-per-row grammar.
- The near-miss printing of the three existing joins is not extended; only the new join prints
  `NEAR` lines.
- The `paths` join's RULES do not change. Its bullet loop now finds the acceptance section by
  heading text because the bar join shares that loop, and that is inert for it today: measured
  2026-09-14, the heading-text slice equals the ordinal-6 slice in every one of the 31 live specs on
  this tree, and no live spec on any local or remote ref carries an acceptance heading at another
  ordinal (the six light-profile specs in the tree are all CLOSED). A future live light-profile spec
  is then graded by both joins where its criteria sit, which is the grading the docstring already
  claims for `paths`.
- `TOOL-aKeyedAnnotation-9` — the paths arm redding a unit that names its own deliverable — is
  untouched. This unit creates no file, so it is not exposed to it.

### Edges

- **consumes-from** `TOOL-aDeferredBar-1` — the memory-tree version constant and the render marker
  as unit 1 leaves them; this unit steps one past. Built before unit 1 lands, two bumps contend on
  the one constant line and the nine marker lines it governs.
- **hands-off** external — widening the example-conf parity arm to keys read by tools other than
  the hygiene engine is the open backlog row TOOL-aJoinedCanon-13. This unit adds its key to the
  shipped example by hand, and that arm still cannot see it.

## 4. Design

### Data model

The join is one regex, one heading pattern and one conf key, all module constants beside
`LEGLINE_KEY` and `GATES_HEAD`:

```python
DIRECT_KEY = "SPEC_DIRECT_CUTOFF"
# The acceptance section by HEADING TEXT, the shape GATES_HEAD already has and for the same reason:
# a light-profile spec drops `## 5.` and the ordinal read grades whatever sits sixth.
AC_HEAD = re.compile(r"^## [0-9]+[.] Acceptance criteria[ \t]*$", re.M)
# A merge-bar or suite INVOCATION: the runner or a suite at command position — the token's start
# or a chain separator, past optional VAR=value prefixes, `timeout N` and a bash/sh launcher — or a
# GATE_FULL= / GATE_SELFTESTS= assignment with a NON-EMPTY value anywhere in the token. A
# `path:line` citation fails the trailing lookahead and stays the cites join's; a grep over a suite
# FILE has grep at command position and is not a run; the empty assignment is the OFF spelling.
BAR = re.compile(
    r"(?:^|&&|[;|(])\s*(?:\w+=\S*\s+)*(?:timeout\s+\S+\s+)?(?:bash\s+|sh\s+)?(?:\S*/)?"
    r"(?:run-gates|run-selftests|run-unattended-gates|[^\s/*?]+\.test)\.sh(?=\s|$)"
    r"|(?:^|\s)GATE_(?:FULL|SELFTESTS)=\S")
```

A glob such as `*.test.sh` names a population and is excluded by the character class, the same
exclusion `check_path_shaped` applies; a `path:line` citation fails the trailing lookahead.

`extract_acceptance(text)` is `extract_gates` with `AC_HEAD` in place of `GATES_HEAD`: the section
after the heading up to the next `## `, or `None` when the spec carries no such heading, which the
bullet loop reads as an empty population. It is the one function this unit mints; the lexicon's
`--suggest` accepts it in cell `py.function` on the verb `extract` the declaration already carries
(asked 2026-09-14).

**The one-token alignment with unit 3, and what it is not.** The flag branch requires a non-empty
value after `GATE_FULL=` or `GATE_SELFTESTS=`. `run-gates.sh`'s `changed()` tests
`[ -n "${GATE_FULL:-}" ]`, so `GATE_FULL= bash tools/run-gates/run-gates.sh` is the plain bar and
the empty assignment is the OFF spelling; unit 3's row D1 reads it the same way, so the two
predicates of this build read the one token alike. The plain bar is still not an acceptance
observation, and the runner branch hits that whole token on its own — with or without the prefix —
which is this unit's rule and not a disagreement with unit 3, whose hook permits the plain
diff-scoped bar at `BUILDING` because it grades the ACT and this join grades the INSTRUCTION. What
the alignment does NOT do: a bare `*.test.sh` basename with no launcher inside a backticked §6
bullet stays a hit, because naming a suite as the observation is the exact shape the owner forbade,
and a simple command carrying one of unit 3's read-only verbs stays a hit for the same reason —
fork D stands. Measured at `dd8968c4` over the two graded populations of the 31 live specs, with
the checker's own `TICK`, `LEG_LINE` and `extract_gates` and an `AC_HEAD`-located acceptance
section: the old and new spellings agree on every graded token — 52 tokens in 24 specs — and differ
on none. rev-2 reported one differing token, a bare flag assignment in unit 3, but that was measured
against unit 3 rev-1; unit 3 rev-2 carries that spelling in prose only, and its one graded token at
`dd8968c4` is the bare suite basename in its AC9 that round-2 M2 names, which both spellings hit and
which leaves with M2's fold, taking the carrier count to 23 (round-2 L3).

Measured over the 1164 backticked tokens in the two graded populations of the 28 live specs at
`b2a330be`, this predicate and the brief's substring spelling agree on 49 tokens in 23 specs across
10 builds, newest dated 2026-09-04, and disagree on exactly two: the substring form hits a
`path:line` citation of the runner (a citation is the cites join's) and misses a suite path carrying
`--render` (a suite at command position with an argument is a run). Both disagreements fall the
invocation shape's way, which is what decided fork D in §8. The figures are DERIVED: the join's own
report line and `--list` reproduce them on any tree.

**Populations.** Exactly the two the `paths` and `legs` joins already extract, and read from the
same loops: every `TICK` token of an acceptance bullet as `extract_acceptance(text)` and the bullet
regex return it, and every `TICK` token of a line `LEG_LINE` matches inside `extract_gates(text)`.
The bullet loop's one change is its section: `extract_acceptance(text)` replaces
`extract_section(text, 6)` for BOTH joins, one loop and one population, so a light-profile spec
under `## 5. Acceptance criteria` is graded there and its `## 6. Gates` is never read as a bullet
population. Nothing else: a mention in §4, in a `New arm:` line (a prose prefix keeps it off
`LEG_LINE`), in any prose, or in a fenced block (`TICK` matches inline single backticks only, so a
fence line and its body yield no token) is not a hit.

**Ordering, the one correctness trap.** `NOT_A_TOKEN` (`tools/check-spec-tokens.py:55`) drops any
token opening with `GATE_` before either existing join sees it, and `NOT_A_LEG` drops any token
opening with `bash ` or carrying a slash from the leg join. The live instance that motivates this
build backticks a `GATE_SELFTESTS=` prefix; both exclusions would discard it unread. So the bar test
runs FIRST in each loop, on the raw token, before those `continue` statements. In the leg-line loop
a bar hit then continues, because the token was never a leg; in the bullet loop the paths join still
runs over the token's words, because a tracked runner path resolves either way and the two joins
answer different questions.

**Date gate.** `armed = direct_cut and spec_date >= direct_cut`, with `spec_date` from the existing
`SPEC_DATE` filename regex. A live spec before the cutoff is not graded, but its bar tokens in the
two populations are COUNTED, so the skip announces its size. A blank or absent key is OFF, and the
report line says so together with that same count — the OFF state cannot hide how much it hides.

**The relation, asserted — the one refusal this unit adds.** When the key is set, the checker asks
the tree's own history when that value landed, one spawn:
`git log -1 --format=%cs -G'^SPEC_DIRECT_CUTOFF="?<value>"?$' -- .memory-tree.conf`. A value that
is not STRICTLY PAST that date is refused before any spec is graded, exit 1, on a line naming the
key, the value and the date it saw:

```
spec-tokens: REFUSING — SPEC_DIRECT_CUTOFF <value> is not strictly past <date>, the day the
value was committed; the register's rule is the day AFTER the later of the newest spec filename
date on any ref and the setting commit's own date
```

Why the commit date and not the newest spec date on the tree, which is the arm round-2 H1
sketched: the graded population is the specs dated at or after the cutoff, so from the day after
landing a tree-only "cutoff is not past the newest spec" comparison refuses the very specs the
join exists to grade, and a predicate that cannot tell the graded population from a violated
relation is the vacuous-selector class. The commit date is a standing invariant — a re-derived
value always lands in a commit dated before it — and it is the register's own sentence, "any
value carried across a day boundary is stale by construction", made mechanical: rev-2's value,
2026-09-14 committed on 2026-09-14, is exactly what it refuses, while no spec was dated that day
for the sketched arm to see. It mechanises the second clause outright and the first for every spec
dated no later than the day it was committed; the first clause's ref-wide reading stays a
documented check at the register comment and is observed for this unit by AC8's red-when. An
uncommitted value — the query prints nothing — cannot be checked and is not refused: the bar line
carries `relation unchecked: value not yet committed`, so the pre-commit run of the build commit
itself announces the skip and the push-boundary run, where the value is in history, asserts it.
Measured 2026-09-14 on node `a`: the query costs 0.08 s when the value is in history and 0.33 s
walking the conf's history when it is not; in a one-commit fixture both are the hit cost.

**Docstring phrases.** The five sentences S2 adds each carry one phrase spelled verbatim, without
backticks, and AC18 greps each: `a path built at runtime` · `inside a sh -c string` · `the body of a
fenced block` · `a suite named in prose` · `finds the acceptance section by heading text`. All five
print 0 on this tree today, which is the RED-first observation.

**Hit shape.** `(f, "bar", tok, WHY)` with the token as the third field, so the existing waiver
lookup keys on it unchanged and the existing stale-row rule applies. `WHY` is the refusal text:

```
a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest
flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build
is complete
```

**Report line**, printed on every run beside the `LEGLINE_KEY` line, one of:

```
spec-tokens: bar join · <k> token(s) examined in <n> live spec(s) at/after SPEC_DIRECT_CUTOFF <date> · <p> pre-cutoff live spec(s) carry one and are not graded
spec-tokens: bar join · SPEC_DIRECT_CUTOFF blank (arm off) · <p> live spec(s) carry a bar token
```

The first shape gains ` · relation unchecked: value not yet committed` as a trailing field when the
history query of the Date gate prints nothing, and carries nothing extra when the value is in
history and strictly past its commit date — a skip announces itself; a pass does not decorate.

**`--list` near-misses.** Every `TICK` token of a live spec's whole text that `BAR` matches and that
is not one of that spec's graded-population tokens, plus every graded-population match in a
pre-cutoff spec, prints as `spec-tokens: NEAR   [bar] <spec> :: <token> — <where>` where `<where>` is
`outside the graded population` or `predates SPEC_DIRECT_CUTOFF <date>` — or, when the key is
blank, `SPEC_DIRECT_CUTOFF blank (arm off)` for a graded-population match, so the OFF line's carrier
count has its `--list` counterpart (rev-4). Exit 0, never a hit. A
fenced block's body is not a `TICK` token, so it is neither a hit nor a `NEAR` line: silence is the
design there, and AC3 asserts the silence rather than a line.

**Waiver kind.** A waiver row for a bar hit carries `[bar]` as the first word of its reason column,
the same house convention the `[path]` and `[leg]` rows already follow. The checker keys on the
token and reads no kind; the kind is for the reader dispositioning the row. Stated here so nobody
later builds a kind-reader on the assumption one exists.

**The suite's fixtures.** The ten arms share two scratch repos rather than building ten, because
the cost of this leg is the `git init` and first commit, not the checker (§5). The DATED family —
AC1, AC2, AC3, AC4, AC5, AC15, AC16, AC17 — shares one repo whose committed clean state is the
suite's existing `scratch` fixture plus an empty tracked `tools/run-gates/run-gates.sh`, so the
paths join stays green over a runner token and the only hit an arm can produce is the bar's. The
WAIVER family — AC6, AC7 — shares a second, whose committed clean state is the AC1 fixture, and
that commit is dated `GIT_COMMITTER_DATE=2026-08-31`, the day before its cutoff: the WAIVER family
commits its conf, so without the backdate the Date gate would refuse the fixture instead of grading
it (rev-4, found at build). Every
arm is one edit from its family's committed clean state and is followed by `git add -A` as the
existing arms are — AC17 alone also COMMITS its edit, because the refusal it observes reads the
value's commit date and a staged value is the announced skip, not the refusal; between arms the
repo is returned to the clean state with a single `git reset --hard <clean-sha>`, the sha captured
once after the family's clean-state commit — the DATED family's is the `scratch` commit plus one
adding the runner — never a fresh init. The DATED family's other arms leave their
conf edits uncommitted, so their bar line carries the `relation unchecked` field and their cutoffs
— dated before the fixture's commit day — are never refused. The fixture tokens, spelled here in a
fence so the join never reads them as an instruction:

```
AC1, AC2, AC4, AC5, AC6, AC7, AC15   GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh
AC3, §4 prose                        GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh
AC3, the §7 `New arm:` line          bash tools/check-spec-tokens.test.sh
AC3, the fence body under a §6 bullet, un-backticked   bash tools/run-gates/run-selftests.sh
AC16, no hit                         GATE_FULL= cat tools/gate-legs.json
AC16, hit                            GATE_FULL=1 cat tools/gate-legs.json
AC17, committed conf, no token       SPEC_DIRECT_CUTOFF="2026-09-02"   (the fixture spec's own date)
```

### Inventory

| identifier | kind | where | cell |
|---|---|---|---|
| `SPEC_DIRECT_CUTOFF` | conf key | `.memory-tree.conf`, the shipped example | `conf` is `dark` in `.lexicon.conf`; ungraded |
| `DIRECT_KEY` · `AC_HEAD` · `BAR` | module constants | `tools/check-spec-tokens.py` | the python cell grades definitions, not constants |
| `extract_acceptance` | function | `tools/check-spec-tokens.py` | `py.function`; verb `extract` is in the declaration, `--suggest` OK 2026-09-14 |
| `bar` | hit kind | the hit tuple's second field | not a naming cell |
| `[bar]` | waiver reason prefix | `memory/project/spec-token-waivers.txt` | not a naming cell |

The suite's arms use the existing `scratch` and `arm` helpers and define no function, so the shell
cell is untouched too.

### Migration

N/A — the key is additive under the blank-means-off idiom every sibling cutoff read by this checker
uses. An adopter whose conf predates it sees the join off and announced, never red.

### Rollout

The cutoff is a RELATION rather than a constant, and the relation has TWO clauses: the owner's
ruling at `TOOL-aJoinedCanon-1` §8 F1, recorded on the `REV_SCOPE_CUTOFF` row of
`.memory-tree.conf` and repeated on every cutoff row since, puts a new cutoff strictly past the
newest spec filename date on ANY ref — local, remote, live worktrees — AND past a date this fleet
can still write into, so nothing in flight goes red at its merge and nothing any node dates on the
setting day can either. In the register's own idiom, the value is the day after the LATER of (a)
the newest spec filename date on any ref or worktree and (b) the setting commit's own date,
`git log -1 --format=%cs`, re-derived at the build commit and again at landing. rev-1 measured (a)
at the base only, which the round-1 audit caught (H3); rev-2 applied (a) alone and set the
measuring day itself, which round 2 caught (H1) and which is the class the register comment
records correcting twice for `REV_SCOPE_CUTOFF` and once, a week earlier, for
`SPEC10_EVIDENCE_CUTOFF`. The reading
that produces the value, run 2026-09-14 on node `a` over 77 refs and every worktree of
`git worktree list`: (a) returned `2026-09-13` on every ref that holds a spec at that date and on
every worktree, (b) returned `2026-09-14`, the later is 2026-09-14, and the relation returns
`2026-09-15`. The three commands, which the conf comment carries beside the value and which are
re-run at the build commit and at landing — if the day has rolled, or a sibling has landed a spec
dated later, the relation moves and the key follows it:

```
git for-each-ref --format='%(refname)' refs/heads refs/remotes \
  | while read r; do git ls-tree -r --name-only "$r" -- memory/builds; done \
  | grep -oE '/[0-9]{4}-[0-9]{2}-[0-9]{2}-spec-' | sort -u | tail -1
git worktree list --porcelain | grep '^worktree ' | cut -d' ' -f2 \
  | while read w; do ls "$w"/memory/builds/*/spec/*.md; done 2>/dev/null \
  | grep -oE '/[0-9]{4}-[0-9]{2}-[0-9]{2}-spec-' | sort -u | tail -1
git log -1 --format=%cs
```

The Date gate's refusal is the second clause made mechanical on the tree the checker grades; the
first clause's ref-wide reading has no tree-side form — a bar grades one tree, not the fleet — and
stays a documented check at the register comment, observed for this unit by AC8's red-when.

THE COST, stated rather than buried, in the idiom `BRIEF_RECORDED_CUTOFF` records in
`.unattended.conf`: the join grades ZERO tracked specs on the landing day, this build's own three
included, because the relation puts the cutoff past every spec anywhere and past that day itself.
The ten fixtures of S5 are its entire coverage on day one, and every pre-cutoff carrier is COUNTED
on the report line and listed under `--list`, so the zero is announced and not silent. Its first
real verdict arrives with the first spec dated after landing. There is no waiver clause:
`memory/project/spec-token-waivers.txt` is shrink-only by its header and stays untouched.
`SPEC_DIRECT_CUTOFF` is a merge-bar knob: the conf comment says why the date is the relation's
answer, states both clauses, carries the reading, and says what blank does.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/check-spec-tokens.py` | `DIRECT_KEY`, `AC_HEAD`, `BAR`, `extract_acceptance`, the bullet loop on it, the bar test first in both loops, the date gate, the relation refusal and its one history query, the counts, the report line with its `relation unchecked` field, the `NEAR` printing, the docstring with its five pinned phrases — about 65 lines |
| `tools/check-spec-tokens.test.sh` | ten arms plus one inline `--list` assertion over two shared scratch repos, AC17's arm the only one that commits; `FLOOR_ASSERTIONS` from 20 to 32, the count the suite prints when every arm runs |
| `.memory-tree.conf` | the key at the relation's answer at the build commit — 2026-09-15 as measured 2026-09-14 — with a register comment: what it gates, BOTH clauses of the relation and the three readings that produced the date, the zero-population cost, what blank does |
| `tools/memory-tree/.memory-tree.conf.example` | the key blank, with a comment in the idiom of the `SPEC_LEGLINE_CUTOFF` row; by hand, because the example-parity arm derives its key set from the engine alone |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | one paragraph beside the two §6 cutoff paragraphs; the marker line |
| `memory/TEMPLATE-SPEC.md` | the render of the above |
| `tools/memory-tree/check-memory-hygiene.sh` | the `KIT_MEMORY_TREE_VERSION` line only |
| `tools/memory-tree/HYGIENE.template.md` · `tools/memory-tree/BUILD-METHOD.template.md` · `tools/memory-tree/ANNOTATION-STYLE.template.md` | the marker line only |
| `memory/HYGIENE.md` · `memory/guides/BUILD-METHOD.md` · `memory/guides/ANNOTATION-STYLE.md` | the renders; the marker line only |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp with a delta line in the commit message |
| `memory/map/features/spec-tokens.md` | title and constraints prose: four joins; a paragraph on the bar join and its cutoff |
| `memory/map/generated/` | re-rendered by `python tools/codebase-map/gen_map.py --write` only if `--check` reports drift after the checker edit |
| `memory/project/spec-token-waivers.txt` | untouched; see S10 |

Thirteen carriers for one paragraph and one regex is the kit's own convention, not this unit's
choice: the version lives in one constant and nine marker lines, the kit-versions leg compares them
all, and the parity leg re-renders the four live copies from their templates. The memory note that
a watched-file touch owes stamps in several carriers is what this table is for.

### Alternatives rejected

- **A hygiene-engine check.** Rejected: the spec-token checker already extracts both populations and
  owns the waiver file; a second extractor is a second mechanism for one population.
- **The brief's substring predicate.** Rejected on the corpus measurement above: same count, wrong
  on both tokens where the two disagree, and an end-anchored `.test.sh` is evaded by any redirect
  after the path.
- **`SPEC_BAR_CUTOFF`**, matching the hit kind as `SPEC_LEGLINE_CUTOFF` matches `legline`.
  Rejected for interface agreement across the set: the brief's spelling is the one the sibling
  briefs were written against, and M2's interface axis spells a config key once.
- **Only the unattended suites.** Rejected: the owner's sentence names the class, and the ledger
  shows the costliest suites outside that kit.
- **A drain of the carriers.** Rejected: other builds' live specs, and a terminal spec is frozen.
- **A cutoff at this build's own date, so its three specs are graded.** Rejected by the ratified
  relation: four live specs on two other refs sit at that date and would red at their merge, and
  the waiver registry cannot absorb a class (`TOOL-aKeyedAnnotation-9`).
- **A cutoff at the measuring day**, rev-2's value. Rejected by the relation's second clause: the
  measuring day is one the fleet can still write into, so a spec any node dated that day and gave
  a bar token would red at its merge — the H3 class rev-2 recorded as closed, reopened (round-2 H1).
- **A tree-only relation refusal comparing the cutoff to the newest spec date on the tree**, the
  arm round-2 H1 sketched. Rejected: from the day after landing that comparison refuses the graded
  population itself, and it would not have caught rev-2's actual defect, which no spec date
  exhibited. The commit-date comparison of §4 Date gate catches that defect and holds forever.
- **A file-keyed waiver row.** Rejected: the registry's grammar is one token per row and every
  consumer of it reads that shape; a bar token waived is waived in every spec, which is the same
  latitude a path token has today.
- **A second bullet loop for the bar join over a heading-located section**, leaving `paths` on the
  ordinal. Rejected: every standard spec's bullets would be iterated twice for one answer, and the
  docstring already claims `paths` reads the acceptance section; measured, the switch moves no
  live spec's population anywhere in the fleet.
- **One scratch repo per new arm**, the suite's existing habit. Rejected on the §5 split: the init
  and first commit are the cost, and ten of them would put the leg's projected idle reading within
  ten seconds of its ceiling.

## 5. Production-readiness checklist

- security — N/A. The checker reads tracked files and the conf and writes nothing.
- perf / scale — two legs, priced apart. `spec tokens (a spec's own names resolve)` grows by one
  regex per backticked token over two populations of at most the live-spec count it already prints,
  plus ONE git spawn when the key is set, the Date gate's history query — 0.08 s on a hit and
  0.33 s on a miss, measured 2026-09-14 on node `a`; 1.586 s in the ledger at the base against a
  60 s ceiling, and it moves by under half a second. The leg this unit GROWS is
  `spec-tokens self-test`: 76.061 s idle in the ledger for the suite's 20 scratch repos, worst of
  six readings 80 s per `tools/run-gates/selftest-budgets.txt`, budget row 130 s, ceiling 120 s in
  `tools/gate-legs.json`. The per-repo split, measured 2026-09-14 on node `a` with the suite's own
  `scratch` body: the init and first commit 2.4 s, one checker run 0.8 to 1.2 s, an in-place edit
  plus `git add` 0.4 s. Nine arms each on their own repo would add about 34 s, a projected 110 s
  idle and 114 s from the worst reading — inside the ceiling by six seconds. Two shared repos, one
  reset per arm, add about 24 s for nine arms; the tenth arm adds one checker run, one edit, one
  commit and one reset, about 2 s, and the twelve armed checker runs each pay the history query in
  a one-commit repo, about 1 s in all: a projected 103 s idle and 107 s from the worst reading,
  inside both the ceiling and the budget row. Neither number is re-declared by this unit, because
  both are calibrated from the worst OBSERVED reading and a projection is not an observation: a
  breach at `VERIFYING` is the ceiling doing its job, and the re-declaration then carries a
  reading. The contended case is the owed flagged bar at `VERIFYING`, which runs legs
  concurrently; the split above is idle.
- error / empty / loading states — a blank key is OFF and announced with the carrier count; a key
  set with no live spec at or after it prints `0 live spec(s) at/after`, an empty population that
  names itself, and that IS the landing state (§4 Rollout); a key whose value is not strictly past
  the day it was committed is REFUSED before grading, and a value not yet in history is announced
  as unchecked rather than refused or passed; the existing zero-spec, missing-manifest and
  missing-registry refusals are untouched; a spec with no acceptance heading at all is an empty
  bullet population, as the ordinal read already made it.
- observability — the bar line on every run, green included, with the `relation unchecked` field
  when the value is uncommitted; `NEAR` lines under `--list`; the refusal texts name the substitute
  and the relation respectively.
- risks — seven. (1) `NOT_A_TOKEN` and `NOT_A_LEG` drop the motivating token unread unless the bar
  test runs first; AC1 and AC2 pin the ordering. (2) A sibling spec of this build reds at the bar —
  not at this landing, since none is graded, but at the first rev dated at or after the cutoff; the
  remedy is a fold on that spec, never a waiver row. (3) Built before unit 1 lands, the version
  step collides; `order 2` and the §3 edge sequence it. (4) The example-conf parity arm cannot see
  the key, so the example row is by hand and AC14 observes it. (5) An author evades with a path
  built at runtime or inside `sh -c`; the docstring says so, AC18 pins the saying, and the act is
  unit 3's. (6) The heading-text read moves the `paths` population for a future live light-profile
  spec; that is the grading the docstring claims and the class M6 of the round-1 audit named, and
  AC15 pins it. (7) The relation refusal reads the value's commit date, so the pre-commit run of
  the build commit itself sees an uncommitted value and only announces; the assertion lands at the
  push boundary and at AC8, where the value is in history — and a landing that rolls the day
  without re-deriving the key is exactly what it refuses there.
- testing — ten arms and one inline `--list` assertion, each fixture one edit from its family's
  committed clean state, AC17's committed; every failing case observed RED by the direct checker on
  that fixture before the arm lands, AC15's on today's ordinal read, AC16's on rev-1's regex and
  AC17's on today's checker, which grades that fixture clean instead of refusing it; the five
  docstring phrases of AC18 print 0 today; the suite itself runs at `VERIFYING` under the main
  loop.
- migration — N/A; additive key, blank-means-off.
- user docs — the template paragraph, rendered; the dossier; the checker's own header. This repo
  keeps no `help/` tree.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py` runs in a scratch repo whose conf sets
  `SPEC_DIRECT_CUTOFF` to 2026-09-01 and whose one live spec, dated 2026-09-02, backticks inside a
  §6 bullet a full-bar invocation carrying the self-test flag assignment, it exits 1 and stdout
  carries `[bar]`, that spec's path and the substitute text.
  Red when: exit 0, or the hit is absent because `NOT_A_TOKEN` dropped the `GATE_`-prefixed token
  before the join saw it.
  fixture: the DATED family's shared scratch repo of §4, made under `mktemp -d`; the tree holds
  none. Its conf arms `SPEC_DIRECT_CUTOFF` alone; no second key guards this arm.
- **AC2** — When the same token sits instead as a backticked entry on the §7 leg line, the run exits
  1 and stdout carries `[bar]` for it.
  Red when: `NOT_A_LEG` discards the token unread and the run exits 0 with a clean leg join.
  fixture: as AC1.
- **AC3** — When three distinct bar tokens sit only in §4 prose, in a §7 line opening `New arm:`,
  and as the un-backticked body of a fenced block indented under a §6 bullet,
  `python tools/check-spec-tokens.py` exits 0, and `python tools/check-spec-tokens.py --list`
  prints exactly two `NEAR` lines reading `outside the graded population` — one naming the §4
  token, one the `New arm:` token — and no line of any kind naming the fence body's token.
  Red when: any placement reports as a hit; the `NEAR` count is not two; or a line names the
  fence body's token, which is the fence exclusion of §4 Populations failing.
  fixture: as AC1; the three tokens are spelled in §4's fixture fence.
- **AC4** — When the spec is dated 2026-08-30 against a cutoff of 2026-09-01 and carries the AC1
  token, `python tools/check-spec-tokens.py` exits 0 and its bar line reads
  `1 pre-cutoff live spec(s) carry one and are not graded`.
  Red when: exit 1, or the count reads 0 while the token is present.
  fixture: as AC1.
- **AC5** — When the conf sets the key to the empty string over the AC1 fixture,
  `python tools/check-spec-tokens.py` exits 0 and its bar line reads
  `SPEC_DIRECT_CUTOFF blank (arm off) · 1 live spec(s) carry a bar token`.
  Red when: the line is absent, or the carrier count reads 0 while the token is present.
  fixture: as AC1.
- **AC6** — When `memory/project/spec-token-waivers.txt` in the AC1 fixture gains a row whose token
  is the AC1 token and whose reason opens `[bar]`, `python tools/check-spec-tokens.py` exits 0 and
  reports `1 waiver(s)`.
  Red when: exit 1, or the summary counts 0 waivers.
  fixture: the WAIVER family's shared scratch repo of §4, whose clean state is the AC1 fixture.
- **AC7** — When that row's token is one no spec in the fixture carries,
  `python tools/check-spec-tokens.py` exits 1 and stdout carries `STALE WAIVER`.
  Red when: exit 0.
  fixture: as AC6.
- **AC8** — When `python tools/check-spec-tokens.py` runs on this tree at the build commit, it exits
  0; its bar line reads `0 token(s) examined in 0 live spec(s) at/after SPEC_DIRECT_CUTOFF <date>`
  with no `relation unchecked` field, where `<date>` is the value
  `grep ^SPEC_DIRECT_CUTOFF= .memory-tree.conf` prints and is strictly past BOTH clauses' readings
  at that commit — the newest spec filename date the two §4 Rollout ref and worktree commands
  return, and `git log -1 --format=%cs`; the line's pre-cutoff carrier count equals the number of
  distinct specs on AC9's `NEAR` lines; and
  `git diff --stat b2a330be -- memory/project/spec-token-waivers.txt` prints nothing.
  Red when: a hit at or after the cutoff; a new waiver row; the date the line names is not strictly
  past the newest spec filename date the §4 Rollout commands return at that commit; or the cutoff
  is not strictly past `git log -1 --format=%cs` of the build commit — either being the relation
  carried instead of re-derived, and the second the one the checker itself refuses.
  figure: DERIVED at the build commit; 2026-09-14 was the first-clause reading on 2026-09-14 and
  2026-09-15 the two-clause reading the same day, and neither is pinned. The carrier count is
  DERIVED too: at `b2a330be` this predicate counts 23, at `dd8968c4` 24, and 23 again once round-2
  M2 is folded in unit 3; the brief's 25 was measured with a differently spelled predicate. The
  zero is the designed day-one state, announced on the line and paired with AC9's positive count
  and the S5 fixtures, not a signal that failed to move.
- **AC9** — When `python tools/check-spec-tokens.py --list` runs on this tree at the build commit,
  it exits 0 and prints at least one `NEAR` line reading `predates SPEC_DIRECT_CUTOFF <date>`, with
  `<date>` the same conf value AC8 names, and the number of distinct specs on such lines equals the
  pre-cutoff count AC8's bar line reports and does not include unit 3's spec once round-2 M2 is
  folded there.
  Red when: the two counts disagree, or no `NEAR` line prints while AC8 counts carriers.
  figure: DERIVED, the same run.
- **AC10** — When `grep -c SPEC_DIRECT_CUTOFF tools/memory-tree/SPEC-TEMPLATE.template.md` and
  `grep -c SPEC_DIRECT_CUTOFF memory/TEMPLATE-SPEC.md` run, both print the same count of at least 1,
  and `head -1 memory/TEMPLATE-SPEC.md` carries a `gov:kit memory-tree@` marker equal to the value
  `KIT_MEMORY_TREE_VERSION` holds in `tools/memory-tree/check-memory-hygiene.sh`.
  Red when: the counts differ, which is a template edited and not re-rendered, or the live marker
  lags the constant.
- **AC11** — When `bash tools/check-kit-versions.sh` runs at the build commit it exits 0;
  `git grep -l 'gov:kit memory-tree@2.75' -- tools memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides`
  prints nothing; and the same command with `2.76` prints the derived count of paths — unit 1
  AC7's pathspec and shape, so the sixty frozen records under `memory/builds/` that quote older
  values are outside the population by construction.
  Red when: any path under that pathspec still spells `2.75`, the value unit 1 leaves, or the
  `2.76` count is 0.
  figure: DERIVED by the grep; nine paths under that pathspec at `b2a330be` and on this tree at
  HEAD, where they spell `2.74`.
- **AC12** — When `bash skills/session-kickoff/manifest-check.sh` runs at the build commit, it exits
  0.
  Red when: check 5 names `.memory-tree.conf` or the engine as touched after the manifest's
  `last-audit` stamp.
- **AC13** — When `python tools/codebase-map/gen_map.py --check` runs at the build commit it exits
  0, and `grep -c "Four joins" memory/map/features/spec-tokens.md` prints 1.
  Red when: the generated set drifted from the checker edit and was not re-rendered, or the dossier
  still says three.
- **AC14** — When `grep -c "^SPEC_DIRECT_CUTOFF=\"\"" tools/memory-tree/.memory-tree.conf.example`
  runs, it prints 1.
  Red when: 0 — the shipped example lacks the key and an adopter installs a dead arm reading as
  armed, which no gate catches (TOOL-aJoinedCanon-13).
- **AC15** — When the AC1 fixture's spec is rewritten under the light profile — no
  `## 5. Production-readiness checklist`, its criteria under `## 5. Acceptance criteria` with the
  AC1 token in a bullet, its leg line under `## 6. Gates` — `python tools/check-spec-tokens.py`
  exits 1 and stdout carries `[bar]` for that token.
  Red when: exit 0 — the ordinal read graded `## 6. Gates` as the bullet population and the
  criteria went unread, which is what `extract_section(text, 6)` does on this tree today.
  fixture: as AC1.
- **AC16** — When the AC1 fixture's §6 bullet backticks instead the flag assignment with its value
  removed before a command that is not the runner — the first AC16 line of §4's fixture fence —
  `python tools/check-spec-tokens.py` exits 0 and stdout carries no `[bar]`; and when the value is
  restored — the second AC16 line — it exits 1 and stdout carries `[bar]`.
  Red when: the first run exits 1 with `[bar]`, which is rev-1's flag branch matching the empty
  assignment unit 3's row D1 reads as the OFF spelling; or the second exits 0, the branch matching
  nothing at all.
  fixture: as AC1.
- **AC17** — When the DATED family's conf sets `SPEC_DIRECT_CUTOFF` to 2026-09-02 — the fixture
  spec's own date, and a day not strictly past the commit that sets it — and that conf is
  COMMITTED, `python tools/check-spec-tokens.py` exits 1 and stdout carries `REFUSING`,
  `SPEC_DIRECT_CUTOFF`, `2026-09-02` and the commit's date, and no `[bar]`, `graded` or `NEAR`
  line, because the refusal precedes grading.
  Red when: exit 0 — today's checker grades that fixture clean; or the refusal fires with the value
  merely staged, which is the announced skip of AC1's family read as a refusal; or the line names
  the key without the date it compared against.
  fixture: the DATED family's shared scratch repo of §4, its conf committed for this arm alone
  and the repo reset to the family's clean sha afterwards. Its conf arms `SPEC_DIRECT_CUTOFF`
  alone.
- **AC18** — When `grep -c 'a path built at runtime' tools/check-spec-tokens.py`,
  `grep -c 'inside a sh -c string' tools/check-spec-tokens.py`,
  `grep -c 'the body of a fenced block' tools/check-spec-tokens.py`,
  `grep -c 'a suite named in prose' tools/check-spec-tokens.py` and
  `grep -c 'finds the acceptance section by heading text' tools/check-spec-tokens.py` run at the
  build commit, each prints 1.
  Red when: any prints 0, a docstring clause dropped or reworded away from its pin, or 2, the
  phrase duplicated outside the docstring; all five print 0 on this tree today.
- **AC19** — When `grep -c '^FLOOR_ASSERTIONS=32' tools/check-spec-tokens.test.sh` runs at the
  build commit, it prints 1, and the suite's own `PASS (32 assertions)` line at `VERIFYING` names
  the same count — the twenty existing arms, the ten of S5 with AC16's two runs, and AC3's inline
  `--list` assertion sum to it.
  Red when: 0 — the floor left at 20 while 32 assertions execute, so eleven arms could strand past
  an early exit with the suite green, the green-by-absence class round-1 M8 named.
  figure: PINNED — the floor is a shrink-only literal the suite reads, so the count is static and
  the grep is how a pin is observed.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `memory hygiene` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit/dogfood doc parity` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `line length`

`spec-tokens self-test` is `chunk: selftests`, `subject: kit`, guarded on `tools/`, so an ordinary
bar holds it; the main loop's flagged bar at `VERIFYING` runs it. It is the leg this unit grows and
§5 prices it: 76 s idle in the ledger at the base, 120 s ceiling, 130 s budget row, projected to
about 103 s idle with the two shared scratch repos of §4 and the history query, and neither bound
is re-declared on a projection. `verdict epoch` is named because the constant moves; the move
dates no engine change, which the topological rule permits, and it is the kit-versions leg that
demands it.

New arm: tools/check-spec-tokens.test.sh · ten arms over two shared scratch repos, each arm one edit from its family's committed clean state and reset between arms, AC17's edit committed — a post-cutoff §6 bullet, a §7 leg-line entry, the three not-hit placements in one spec with an inline `--list` count, a pre-cutoff date, a blank key, a clearing `[bar]` row, a stale one, a light-profile spec, the empty and the non-empty flag assignment, and a committed cutoff not strictly past its own commit day — asserted per AC1 through AC7, AC15, AC16 and AC17 · `FLOOR_ASSERTIONS` from 20 to 32, observed by AC19

## 8. Open questions

- **Fork A — hygiene check or spec-token join.** RESOLVED (agent, 2026-09-13, delegated): the
  spec-token checker. It already extracts both populations and owns the waiver file; a hygiene
  check would be a second extractor for one population.
- **Fork B — ban every `*.test.sh` in an AC, or only the unattended suites.** RESOLVED (agent,
  2026-09-13, delegated): every suite. The owner's third sentence names the class, and the ledger
  puts `govkit selftest` at 3445 s and `manifest-check self-test` at 2162 s beside the unattended
  pair.
- **Fork C — cutoff or drain, and which date.** RESOLVED (agent, 2026-09-14, delegated): a cutoff
  at the relation's answer at the build commit, re-derived there and again at landing by BOTH
  clauses of the ratified relation of `TOOL-aJoinedCanon-1` F1 — the day after the later of the
  newest spec filename date on any local or remote ref or live worktree and the setting commit's
  own date — which the §4 Rollout commands measured on 2026-09-14 as 2026-09-13 and 2026-09-14,
  so the value is 2026-09-15 as measured that day. rev-1 took the landing date from a base-only
  measurement, and four live specs at 2026-09-13 on two other refs would have redded at their
  merge (round-1 H3); rev-2 applied the first clause alone and set the measuring day, so a spec
  any node dated that day would have redded at its merge (round-2 H1). Consequence, stated: the
  join grades zero tracked specs on the landing day, this build's three included, and the S5
  fixtures are its coverage on day one; its first real verdict arrives with the first spec dated
  after landing; the four in-flight specs are not graded and are not folded; S10 carries no
  waiver clause. The drain stays rejected: the carriers are other builds' live specs.
- **Fork D — the predicate's shape: the brief's substring spelling, or invocation shape.**
  RESOLVED (agent, 2026-09-13, delegated): invocation shape, on the §4 measurement. Same 49 tokens
  either way; the two disagree on one citation and one suite-with-argument, and the invocation shape
  is right on both. Recorded as a decision rather than a fact-question because the corpus could
  only show where the two differ, not which reading the owner's sentence intends.
- **Fork E — the empty flag assignment: a hit, or the OFF spelling unit 3's row D1 reads.**
  RESOLVED (agent, 2026-09-14, delegated): the OFF spelling; the flag branch requires a non-empty
  value, and the two predicates of this build read the one token alike. This is an alignment on one
  token and NOT a reversal of fork D: a bare `*.test.sh` basename with no launcher inside a
  backticked §6 bullet stays a hit, and so does a run carrying a read-only verb, because naming a
  suite as the observation is the exact shape the owner forbade; the plain bar behind an empty
  assignment stays a hit through the runner branch, which is this unit's rule about the
  INSTRUCTION and no disagreement with a hook that permits the ACT. Round-1 B1 named the
  alternative — widening `BAR` on both counts — and it is refused here.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-14 · spec-audit round 1 folded — H2 · H3 · M1 · M6 · L3 · B1's one-token
  alignment. H2: AC11 takes unit 1 AC7's pathspec and value shape, dropping the same-file-set
  clause that counted sixty frozen records. H3: S4, §3, §4 Rollout, AC8 and Fork C move the cutoff
  to `2026-09-14` by the ratified relation, record the ref-wide reading and its command, state the
  zero-population landing, and delete S10's waiver clause. M1: AC3 expects two `NEAR` lines and
  asserts the fenced placement's silence; §4 says why. M6: S1, S2 and §4 Populations locate the
  acceptance section by heading text through `AC_HEAD` and `extract_acceptance`, the bullet loop
  reads it for both joins with the fleet-wide measurement in §3, and AC15 is the light-profile arm.
  L3: §5 perf and §7 price `spec-tokens self-test` with the measured per-repo split; S5 and §4
  share one scratch repo per fixture family; the ceiling is not re-declared on a projection. B1's
  alignment: §4 `BAR`'s flag branch requires a non-empty value, Fork E records it as no reversal of
  fork D, and AC16 observes both sides. Arms seven to nine, floor 20 to 31.
- rev-3 · 2026-09-14 · spec-audit round 2 folded — H1 · M1 · L1 · L2 · L3. H1: §4 Rollout, S4,
  Fork C and §3 state both clauses of the ratified relation and derive the value as the day after
  the later of the newest spec filename date on any ref or worktree and the setting commit's own
  date, 2026-09-15 by both clauses as measured 2026-09-14 and re-derived at the build commit and
  at landing; AC8's red-when gains the second clause; the landing-day consequence is recorded; and
  the left-shift lands as S1's relation refusal, §4 Date gate, AC17 and the tenth arm of S5 — the
  refusal compares the value to the date of the commit that set it rather than to the newest spec
  date on the tree, because the latter refuses the graded population from the day after landing
  and would not have caught rev-2's defect; §4 Alternatives records both rejections. M1: AC8 and
  AC9 assert the conf's value and the relation instead of a date literal, with AC8's `figure:`
  line naming the two readings taken 2026-09-14; S4 and Fork C state the value as the relation's
  answer at the build commit. L1: S5 and the §7 `New arm:` line pin `FLOOR_ASSERTIONS` at 32,
  observed by AC19. L2: S2 drops `NOT OBSERVED`; §4 Docstring phrases pins five phrases and AC18
  greps each. L3: §3 and §4's alignment paragraph re-measure at `dd8968c4` — the two spellings
  agree on all 52 graded tokens in 24 specs, unit 3's one is the bare suite basename round-2 M2
  names, and the count is 23 once that fold lands. §5 re-prices the two legs for the tenth arm and
  the history query.
- rev-4 · 2026-09-14 · built, and CLOSED in the same commit. Two things the design could not see
  from the desk, both in §4 and neither moving an acceptance criterion. §4 The suite's fixtures: the
  WAIVER family commits its conf, so its clean-state commit is dated `GIT_COMMITTER_DATE=2026-08-31`,
  the day before its cutoff — the Date gate S1 adds would otherwise refuse the AC6 and AC7 fixtures
  instead of grading them, which is the relation working as specified against a fixture rev-3 had
  not priced; and the DATED family's clean sha is captured after a second commit adding the empty
  runner, since the `scratch` helper commits before the runner exists. §4 `--list` near-misses: a
  third `<where>`, `SPEC_DIRECT_CUTOFF blank (arm off)`, for a graded-population match under a
  blank key, so the AC5 OFF line's carrier count has a `--list` counterpart. Every failing case
  observed RED by the direct checker on its staged fixture before its arm was written, AC7's on a
  checker copy with the stale-row rule removed; the corpus measurement of §4 re-taken at
  `2ca014fd`: 23 live carriers, 51 graded tokens, heading-text and ordinal populations identical
  after whitespace in all 30 live specs. AC8's committed form was observed on a throwaway commit
  that was soft-reset before the build commit, since a commit cannot observe itself.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a spec acceptance token that spells a merge-bar
or self-test suite invocation"` ranks `CensusRefused` and `build_self_chain` from the
process-monitor kit as its two seams, both by name stem, neither about specs; the affordance rows it
adds name the run-gates knob set, which is what this unit refuses rather than what it extends. The
seam this unit extends was found by reading the checker: `tools/check-spec-tokens.py`, whose `legs`
and `paths` joins already extract the two populations and whose `read_conf_key` and `SPEC_DATE`
already give a dated, conf-gated arm its shape — `LEGLINE_KEY` is the exact precedent and the join
is written beside it, and `GATES_HEAD` with `extract_gates` is the exact precedent for locating a
section by heading text, which `AC_HEAD` and `extract_acceptance` copy. The map probe printed
`unscanned layers: .sh`, so the suite side was read by hand: `tools/check-spec-tokens.test.sh`'s
`scratch` and `arm` helpers take the ten arms without a new function. Two recall hits changed the
design: TOOL-aJoinedCanon-13 says the example-conf parity arm cannot see a key this checker reads,
so the example row is by hand and observed by AC14; TOOL-aDeclaredBound-2 says the last env
override for a cutoff was removed because the conf already won, so this key gets none. Recall's
TOOL-aKeyedAnnotation-9 was checked and does not bind: this unit creates no file for the paths arm
to red on. The research record's terms were re-run and its finding — no seam for refusing a bar
inside a pass — stands for the ACT, which is unit 3's; for the INSTRUCTION the seam above exists
and is taken.

Recall terms used: `python tools/memory-recall/query.py "which record decided that spec-token joins
are date-gated by a conf cutoff and waived through the token registry, and why a suite run is not
an acceptance observation" --terms "spec-tokens cutoff waiver legline check-spec-tokens acceptance
witness run-gates self-test GATE_SELFTESTS bar-in-pass suite deferred"`.
