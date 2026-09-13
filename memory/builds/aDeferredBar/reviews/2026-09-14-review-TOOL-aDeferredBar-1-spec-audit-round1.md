**Serves:** spec-audit TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 TOOL-aDeferredBar-3

# aDeferredBar — spec audit of the three-unit set, round 1

*Node `a`, 2026-09-14. A Tier-2 adversarial pass over the three rev-1 specs of the `aDeferredBar`
build, before any unit is built: four primed finder lenses, five batched skeptic passes prompted to
REFUTE every finding, one synthesis. Every claim a surviving finding makes about existing code or
about a sibling spec was re-run at source during synthesis — the nine-token BAR count, the AC11
file count, the anchor-kind tally, the light-profile spec count and the adopter suite's fixture —
and the figures below are what those runs printed on this tree, not what a lens reported.*

**Round: 1.** Subjects, each pinned at the blob it was read at (all three match the working tree
at `27ba9c0c`):

- `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-1.md@5e70799668d6ccfdb730eac6ab1542a965e92f7f`
- `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-2.md@3bbb28862720cff7e14f6ea0f7396a94dfe119e5`
- `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-3.md@09cf2607950b4385721bf98697838213b828d715`

## Verdict: BLOCKED

One blocker, five highs, eight mediums, five lows, after consolidating the twenty-five confirmed
findings into the nineteen below. The blocker sits in unit 3 and is a contradiction between two
documents of the same set: unit 2 §4 spells the `BAR` predicate its gate will run, unit 3 §3 says
"this spec is written to pass the gate `TOOL-aDeferredBar-2` adds", and running that predicate over
unit 3's own §6 bullets with the checker's own extraction yields nine hits. Unit 2's rollout rules
the remedy — a rev bump on the hitting spec, never a waiver — so unit 2 cannot close at order 2
while unit 3 stands as written. The same seven criteria carry the high beside it: six of them name
the withheld suite as their observation, which the build README forbids in so many words and which
unit 3's own hook denies at `BUILDING` once its settings fragment lands.

Two of the highs are design facts rather than wording. Unit 3 keys the hook on `branch-ref:`, a
field the protocol and the driver write only under the run-branch anchor; seventeen of the
forty-four anchored run records in this tree carry no such field, and the hook as designed fires
for none of them. Unit 2 dates its cutoff from a measurement taken at the base only, and four live
specs on two other refs carry bar tokens at that date.

**Decision needed** on the blocker, because two spellings of the fix reach different owners. The
default under unit 2's own §4 is a rev-2 of unit 3 that names the suite in prose. The alternative
is to widen unit 2's `BAR` so that a bare `*.test.sh` basename with no launcher, and a run carrying
one of unit 3's read-only verbs, are not hits — which reverses unit 2's fork D and aligns the two
predicates on the empty `GATE_FULL=` assignment they currently disagree on. That is the owner's
call, recorded in unit 2 §4 and §8 before either unit builds; the fold below assumes the default.

Units 1 and 2 hold no blocker and CONVERGE at round 1 with their fixes folded. Unit 3 holds the
blocker and owes a round 2 after its rev-2.

**Review shape:** raw 49 · confirmed 25 · refuted 24 · unverified 0 · precision 0.51. Precision sits
at the charter's tighten-priming threshold rather than below it; the refuted half was mostly claims
about existing checkers that a source read overturned, and the confirmed half is dense because
three lenses measured rather than argued.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every
lens and every skeptic batch came back, so the finding set is complete as far as a four-lens fan
reaches, and the zero unverified count is a count and not an absence of evidence.

## Findings

| # | Sev | Spec | Address | One line |
|---|-----|------|---------|----------|
| B1 | blocker | 3 | §3 last bullet · §6 AC2–AC6, AC9, AC10 | Nine `BAR` hits in this spec's §6 red unit 2's gate at order 2; the "written to pass it" claim is false |
| H1 | high | 3 | §6 AC2–AC6, AC10 · §4 Files touched · §6 preamble | Six criteria are observed by the withheld suite, which the pass may not run and the hook itself denies |
| H2 | high | 2 | §6 AC11 | The grep lists 69 files at the base, not nine; sixty frozen records can never carry the stepped value |
| H3 | high | 2 | §8 Fork C · §4 Rollout · §3 | The cutoff was measured at the base only; four live specs on two other refs hit it |
| H4 | high | 3 | §2 S2 · §4 The key | `branch-ref:` is absent by design on the default-branch anchor; 17 of 44 anchored records key nothing |
| H5 | high | 3 | §4 Files touched · §5 testing | The S6 UNWIRED arm reds `adopt-unattended.test.sh` on a fixture the unit never touches |
| M1 | medium | 2 | §6 AC3 · §4 Populations | The fenced placement yields no `TICK` token, so the design prints two `NEAR` lines and AC3 demands three |
| M2 | medium | 1 | §7 · §6 · §5 perf | §7 claims every leg is hand-run in §6; `memory hygiene` and `method carriers` are run by no criterion |
| M3 | medium | 1 | §6 AC8 | The grep sees the comment marker only; a half-moved `version: '1.0'` passes |
| M4 | medium | 1 | §6 AC1, AC2 | The five forms and the `summary` rule sit on lines the one grep never reads |
| M5 | medium | 3 | §4 The predicate · §6 AC2, AC5 | No arm exercises command position after a separator or a token as a `grep` argument |
| M6 | medium | 2 | §4 Populations · S2 docstring | §6 is keyed by ordinal; a light-profile spec's Gates section is graded as its acceptance |
| M7 | medium | 1 | §6 AC6 | The size checker grades bytes; the "at or under 350 lines" clause has no observation |
| M8 | medium | 3 | §2 S5 · §6 AC9 | The `project-owned` withholding row is observed by nothing; the `**` engine rule ships a forgotten suite |
| L1 | low | 3 | §2 S8 | Four of S8's five prose carriers have no criterion naming them |
| L2 | low | 3 | §3 Edges · §4 The predicate | Both cite unit 1's AC6 for the `--render` verb; AC6 names a `sed` render and the verb sits in §4 Carrier 3 |
| L3 | low | 2 | §5 perf · §7 | Prices the 1.6 s `spec tokens` leg; the leg this unit grows is the 76 s self-test against a 120 s ceiling |
| L4 | low | 3 | §4 Files touched, the manifest row | A body edit that names `last-audit` only; C9 measures from `last-body-change` |
| L5 | low | 3 | §4 The key, last paragraph | "One live run per branch is the kit's own invariant" restates a rule the protocol records as retired |

Raw-id map, so the transcript reconciles: B1 = 16, 27, 40 · H1 = 1, 17 · H2 = 18, 31 · H3 = 41 ·
H4 = 39 · H5 = 30 · M1 = 2, 23, 32 · M2 = 3 · M3 = 4 · M4 = 5 · M5 = 9 · M6 = 33 · M7 = 34 ·
M8 = 35 · L1 = 15 · L2 = 25 · L3 = 36 · L4 = 37 · L5 = 48. Raw id 2 arrived rated high and 1, 17
and 40 arrived rated high with 16 and 27 as blockers; the severities in the table are this
report's, adjudicated per consolidated finding.

---

### B1 — blocker — unit 3 §3 last bullet, §6 AC2, AC3, AC4, AC5, AC6, AC9, AC10: this spec reds the gate its sibling builds, and says it does not

Unit 2 §4 pins the `BAR` regex verbatim. Run over the two graded populations of all three specs
with the checker's own `extract_section(text, 6)`, its bullet regex `^- .*(?:\n  .*)*`, its `TICK`
and its `LEG_LINE`, units 1 and 2 yield zero hits and unit 3 yields nine, every one in §6:
`gate-guard.test.sh` in AC2, AC3, AC4, AC5, AC6, AC9 and AC10 (a bare `*.test.sh` basename at
token start satisfies the command-position alternation); the empty assignment `GATE_FULL=` in AC3
(the `(?:^|\s)GATE_(?:FULL|SELFTESTS)=` branch has no non-empty-value condition); and
`bash tools/run-gates/run-selftests.sh --kit tools/unattended --list` in AC9 (unit 2's predicate
carries no read-only-verb exception; only unit 3's hook does). Reproduced at synthesis, same nine.

Unit 3 is SPECCED and dated `2026-09-13`, which is unit 2's cutoff, so `spec_date >= direct_cut`
arms it. Unit 2 AC8 asserts the checker exits 0 on this tree at unit 2's build commit, and its
red-when says a hit at or after the cutoff "by construction can only be a spec of this build". Unit
2 §4 Rollout forbids the escape: "fixed there with a rev bump per M2, never waived". So at order 2
the `spec tokens` leg — `subject: repo`, unguarded, on every bar — reds on a document that already
sits in the tree, and unit 2 cannot close until unit 3 is re-revved. Unit 3 §3's "This spec is
written to pass the gate `TOOL-aDeferredBar-2` adds" and its §6 preamble "No criterion names the
bar, a flag prefix or a suite as its observation" are both false against the sibling's design.

The two units also disagree on one token: unit 3's row D1 admits `GATE_FULL=` as the OFF spelling,
unit 2's regex hits it. Two predicates in one build that read the same token two ways is the
one-fact-two-places defect, whichever way it is resolved.

**Fix.** Rev-2 of unit 3, the default under unit 2 §4: name the suite in prose with no backticks
("observed by the withheld suite S5 names, one arm per row"); spell AC3's empty assignment as
"row D1's OFF spelling"; cite AC9's runner by verb ("the self-test runner's `--list` verb" is still
a token — write "the runner's list verb" and observe the budget row by a grep over
`tools/run-gates/selftest-budgets.txt`). The alternative, which is the owner's and not the fold's:
widen unit 2's `BAR` to exempt a bare `*.test.sh` basename with no launcher and a simple command
carrying one of unit 3's `READ_ONLY_VERBS`, matching D1 on the empty assignment, recorded in unit 2
§4 and §8 as a reversal of fork D.

**Left-shift.** The gate that catches this class is unit 2's own, once it exists, and the ordering
of this build put its target document in the tree before it. Two things make the class gateable
earlier: (1) the SPEC stage of `tools/workflows/unattended-build.js` runs
`python tools/check-spec-tokens.py` over the tree after the writer returns and before the spec is
ratified, so a sibling that hits reds at the writer rather than at order 2; (2) one
`spec-tokens self-test` arm whose fixture is TWO specs, the second dated at the cutoff and naming a
suite in an "Observed by" clause, asserted as a hit. A third, for the disagreement: one fixture
token, `GATE_FULL=`, fed to both predicates in one arm, asserting they agree — whichever way the
owner rules.

### H1 — high — unit 3 §6 AC2, AC3, AC4, AC5, AC6, AC10, against §4 Files touched and the §6 preamble: the observation is the suite the pass may not run

AC2, AC3, AC4, AC5 and AC10 read "Observed by `gate-guard.test.sh`", and AC6 requires the suite to
finish and print `PASS (<n> assertions)`. That is a `*.test.sh` run inside the pass. The build
README's fifth rule forbids exactly it ("by the direct invocation of the checker or the hook on a
fixture — never by the suite, which is what this build forbids"), unit 1's child prompt bans "any
`*.test.sh` suite", and unit 2 S5 resolves the identical shape the other way ("each arm's fixture
exercised by the direct checker; the suite's own verdict is the main loop's at `VERIFYING`").

Mechanically the pass cannot make the observation either. This run's `RUN.md` carries
`anchor-kind: run-branch` and `branch-ref: refs/heads/branch/unattended-build-gates-timing-4af880`;
`PHASES_CORE` puts `BUILDING` before `VERIFYING`; unit 3's files table says the settings entry is
"LIVE the moment it lands, hooks being re-read mid-session"; and row D4 matches
`gate-guard.test.sh`. So once S4 lands, the hook denies its own suite for the rest of the pass, and
the spec states no ordering that runs the suite first. The §6 preamble says it itself — "once this
hook is wired the pass that builds it could not observe such a criterion" — and then six criteria
name it. Only AC1 carries the pre-wire caveat.

**Fix.** Mirror unit 2 S5: each arm observed by feeding the hook the arm's fixture stdin directly
(`node` plus the hook path is no deny shape), one command per row, asserting exit code and stderr;
the `PASS (<n> assertions)` line and the `PHASES_CORE` parity verdict move to the §7 `New arm:`
line and to `summary` for the main loop at `VERIFYING`. If direct arms must precede the wiring,
state S4 last in the pass order.

**Left-shift.** B1's gate, once the tokens are prose, reaches this only by accident. The durable
class check is cheap: the SPEC-stage writer prompt unit 1 S2 adds already says "never a `*.test.sh`
suite" — make the hygiene engine's acceptance-witness arm (check 12) red an "Observed by" clause
whose witness is `*.test.sh`-shaped, a one-line widening of a regex it already runs.

### H2 — high — unit 2 §6 AC11: the grep counts sixty frozen records as live carriers

`git grep -l "gov:kit memory-tree@" b2a330be -- tools/memory-tree memory` lists 69 files, and 72
at `27ba9c0c`, not nine. Fifty-nine are records under `memory/builds/` that quote the marker at
values from `1.5` to `2.74` and can never move; the rest are `memory/backlog/TOOL.md` and the
memory-tree dossier. Unit 1's AC7 quotes `gov:kit memory-tree@2.74` verbatim and is CLOSED and
frozen by unit 2's build commit, so "every one carrying the stepped value" reds by construction and
the red-when "any listed file carries the previous value" fires on roughly sixty files. "Nine" is
unit 1 AC7's figure under unit 1's narrower pathspec
(`-- tools memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides`), which does print nine.

**Fix.** Take unit 1 AC7's scope and shape: the previous value (`2.75`, as unit 1 leaves it)
greps empty under that pathspec, and the stepped value prints the derived count; drop "the same
file set it lists at the base".

**Left-shift.** None new. `kit version markers` is the gate over exactly this population; a
criterion that re-derives a leg's population with a different pathspec is the two-mechanisms shape
unit 2 §3 names for the hygiene engine. AC11 should name the leg and nothing wider.

### H3 — high — unit 2 §8 Fork C, §4 Rollout, §3: the cutoff was measured on one ref

The cutoff precedent is an owner ruling, `TOOL-aJoinedCanon-1` §8 F1, recorded in
`.memory-tree.conf`'s `REV_SCOPE_CUTOFF` comment and repeated on every later cutoff row there: a
new cutoff sits strictly past the newest spec filename date on ANY ref — local, remote, live
worktrees — so nothing in flight goes red at its merge. This unit measured at the base only
("Every hit measured at the base predates it"; Fork C: "the newest predates the date by nine days")
and takes its own date.

Run with the spec's own `BAR` over every 2026-09-13-dated spec on every local and remote ref, four
LIVE specs hit: `TOOL-aBatchedArm-5` on `branch/unattended-checks-performance-a37d8d`
(`run-selftests.sh --pooled`, `run-unattended-gates.sh`), and `KICK-aReplayedCard-1`,
`KICK-aReplayedCard-2`, `TOOL-aReplayedCard-1` on `branch/session-orientation-tooling-2faa9f`
(`manifest-check.test.sh`, `scratch-guard.test.sh`). The `spec tokens` leg is `subject: repo` and
unguarded, so each reds its own bar at its merge with `origin/main`. The escape S10 contemplates
does not exist: `memory/project/spec-token-waivers.txt` is SHRINK-ONLY by its header, and
`TOOL-aKeyedAnnotation-9` records that absorbing a class there is unavailable.

**Fix.** Re-derive the date at build time by the ratified relation — strictly past the newest spec
date on any ref or worktree, `2026-09-14` or later on the day it lands — and record the day-one
cost: the arm grades zero specs at landing and the seven fixtures are its coverage. Or, if the
build's own three specs are to be graded, record in §8 Fork C the four in-flight paths, that each
must fold on its own branch before merging, and delete S10's waiver clause. Either way §3's "the
cutoff excludes them by construction" is rewritten to say what was measured and where.

**Left-shift.** The relation is a documented check, not a gate, on every earlier cutoff row, and
this is the first time it was skipped. The cheapest machine form: the conf row's `WHY` comment
carries the `git for-each-ref` reading (newest spec date on any ref, the ref it sits on) the way
the `REV_SCOPE_CUTOFF` comment does, and the unit's build record carries the command. A gate that
enumerates other refs at bar time is the wrong shape — the bar grades a tree, not a fleet.

### H4 — high — unit 3 §2 S2 and §4 The key: the key is absent on the protocol's primary anchor

`branch-ref:` is written by `tools/unattended/unattended.sh:2742` only under `[ -n "$BREF" ]`, the
comment at `:2353` says it is written "only where the project's anchor scope makes the run's own
branch meaningful", and `UNATTENDED-PROTOCOL.md` fact 10 reads "present only when the second anchor
fired". `resolve_base` sets `ANCHOR_KIND=default-branch` whenever the README resolves at the
merge-base — the strict-mandate form, the protocol's primary — and never sets `BREF` on that path.
The spec reads the absence as age ("three older `LANDING` records carry no `branch-ref:` field")
rather than as the declared anchor mode.

Re-tallied at synthesis over every `memory/builds/*/RUN.md`: 17 records are
`anchor-kind: default-branch` and none carries `branch-ref:` (12 LANDED, 3 LANDING, 2 ABORTED —
`aHoistedPass`, the stall that motivates the build, among them); all 27 `run-branch` records carry
it. So the hook keys nothing for any strict-mandate run, and for every adopter whose conf leaves
`ANCHOR_SCOPE` blank, which is the kit default. It reads as wired and never fires there.

**Fix.** Either key on a fact every anchored record carries — have `--preflight` record the local
branch under a distinct fact on both anchors, which is a protocol field-list change and so is named
in S2 and amends fact 10's render — or state in §3 that the refusal covers run-branch-anchored runs
only, with the 17-of-44 figure and the adopter-default consequence, and cite fact 10 in §4.

**Left-shift.** One suite arm whose fixture record is `anchor-kind: default-branch` with no
`branch-ref:` at `BUILDING`, asserted as a DENY and observed RED on the design as written. If the
new fact is added, `check-protocol-parity.test.sh` already grades the field list against the
render and takes the change as one more row.

### H5 — high — unit 3 §4 Files touched (the adopter row) and §5 testing: the sixth `--check` arm reds a suite the unit never names

`tools/unattended/adopt-unattended.test.sh` lines 76 and 119 run `adopt-unattended.sh --check`
inside scratch adopter trees its `seed()` builds — seven kit files and a conf, no
`.claude/settings.json` — and assert exit 0. `adopt-unattended.sh` never touches a settings file
today (zero matches for `settings`). The S6 arm AC10 specifies exits 1 on exactly that state, so
both assertions red, and the files table names no change to the suite.

The suite is not a `tools/gate-legs.json` leg. It is `project-owned` in `kit.toml`, budget row 111
(`unattended adopter e2e`, 60 s), enumerated by `run-unattended-gates.sh` — the compensating check
the descriptor says work touching `tools/unattended/` must print GREEN — and by the owed
`GATE_SELFTESTS=1` bar at `VERIFYING`. It reds there on a fixture the unit never touched.

**Fix.** Add `tools/unattended/adopt-unattended.test.sh` to the files table: `seed()` writes a
`.claude/settings.json` carrying the fragment's marker (or the fixture runs
`settings-merge.py --fragment` before `--check`), with a note on whether the 60 s budget row moves.

**Left-shift.** The suite itself is the gate once its fixture carries the precondition; observe its
new arm RED first by running `--check` in an unseeded scratch tree. Nothing else is owed.

### M1 — medium — unit 2 §6 AC3 and §4 Populations: the third placement cannot print a `NEAR` line

`TICK` is `` `([^`\n]+)` `` and the bullet regex is `^- .*(?:\n  .*)*`. A fence indented two
spaces under a §6 bullet folds into that bullet's text; a fence line and an un-backticked body
yield no `TICK` token at all, so the placement is neither a hit nor a `NEAR` line, and §4 says so
itself ("a fence line and its body yield no token"). Backtick the body inside the fence and the
token joins the graded population as a HIT, exit 1. Under no spelling does the fenced placement
produce a third `NEAR` line while the run exits 0; the design prints two (the §4 prose and the
`New arm:` placements), and AC3's red-when "fewer than three" reds a correct build. The risk is
the builder bending the fixture, after which the arm no longer tests the fence exclusion it was
placed to test.

**Fix.** AC3 expects two `NEAR` lines and asserts separately that the fenced placement is neither
a hit nor a `NEAR` line — silence is the design. Or replace the fenced placement with a backticked
token on a non-bullet prose line inside §6, before the first bullet, which `TICK` sees and the
bullet regex does not, and keep three.

**Left-shift.** The arm, with the right count, observed RED first. Nothing else.

### M2 — medium — unit 1 §7 against §6 and §5: a claim about its own criteria that is false

§7 states "each is observed here by running its own script by hand, which is what §6 names". The
fourteen criteria run `check-template-size.sh`, `check-kit-versions.sh`, `check-verdict-epoch.sh`,
`adopt-unattended.sh --check`, `check-workflow-syntax.js`, `manifest-check.sh` and
`check-spec-tokens.py` — never `check-memory-hygiene.sh` nor `check-method-carriers.sh`, both on
the leg line. §5 compounds it by budgeting "`memory hygiene` 83 s" among the hand-run scripts. Those
two legs read the files S3 and S4 change: the hygiene engine caps the guide S3 grows, and
`check-method-carriers.sh` arm 5 reads the Skill bullet S4 adds. Their first verdict arrives at the
close.

**Fix.** AC15: `bash tools/memory-tree/check-memory-hygiene.sh` and
`bash tools/memory-tree/check-method-carriers.sh` each exit 0 at the build commit; red when either
names `BUILD-METHOD.md` or the Skill render. Or delete the §7 sentence.

**Left-shift.** None; the two legs ARE the gate, and the criterion only names them.

### M3 — medium — unit 1 §6 AC8: the grep sees half the line

Line 44 of `unattended-unit.js` reads `version: '1.0', // gov:kit unattended-unit@1.0 — …` and
`unattended-build.js:3` has the same shape. AC8's commands grep the comment marker only; its
red-when adds "or `meta.version` still reads `1.0`" with no command that can see it. §4 records
that no gate pairs these markers to a constant (`TOOL-aHoistedPass-33`), so a half-moved
`version: '1.0', // gov:kit unattended-unit@1.1` passes every observation in the spec.

**Fix.** Grep the whole line: `grep -c "version: '1.1', // gov:kit unattended-unit@1.1"` prints 1,
and the same for `unattended-build@1.1`.

**Left-shift.** The pairing of engine markers to a constant is the open row
`TOOL-aHoistedPass-33`; this unit cites it and does not build it.

### M4 — medium — unit 1 §6 AC1, AC2: red-whens the command cannot produce

§4 pins a five-line JS literal. AC1's grep matches the header phrase on line 1; the five forms span
lines 1–3 and the `summary` rule sits on line 5. `grep -c` prints 1 for any literal that carries the
header, so AC1's second red-when ("fewer than the five forms §4 pins") is unobservable — and the
forms are the load-bearing content, per the §3 edge that says they are what unit 3's predicate
reads. AC2's phrase and "name it in `summary`" share line 5, so its grep at least sees that line;
nothing distinguishes "return it" from "run it later".

**Fix.** One grep per pinned form and one for the substitute, spelled to stay clear of unit 2's
`GATE_` alternation (which matches `\sGATE_(FULL|SELFTESTS)=` anywhere inside a backticked token):
`grep -cE 'GATE_(FULL|SELFTESTS)= prefix'`, `grep -c 'not run-selftests.sh, not run-unattended-gates.sh'`,
`grep -c 'name it in .summary. and the main loop'`, each printing 1.

**Left-shift.** None; greps over a pinned literal are the observation.

### M5 — medium — unit 3 §4 The predicate against §6 AC2, AC5: the defining property of the grammar has no arm

§4 credits the command-position grammar (`;`, `&&`, `||`, `|`, `(`, `then`, `do`, `else`) with the
D4 delta from 1365 to 1740 and with the whole 8373-row near-miss column. AC2's rows are all
line-start forms (bare, `export`, `env`, `NAME=value`, `timeout`, `bash -c`); AC3's allows are
read-only verbs, the plain bar and the empty assignment; AC5's allows are a quoted token and a
heredoc body, both blanked. No arm places a deny token after a separator, and no arm places one as
the argument of `grep` or `echo` expecting exit 0. A predicate matching only at line start passes
AC2; one matching anywhere passes AC5 and denies `python tools/govkit/govkit.py selfcheck | grep gate-guard.test.sh`
— this unit's own AC9 observation — at `BUILDING`. AC11's corpus probe catches only the opposite
direction.

**Fix.** AC2 gains one row with the flag prefix after `&&` and one after `then`; AC5 gains a bare
suite name as the argument of a `grep`, exit 0.

**Left-shift.** Those two arms, observed RED on a line-start-only and an anywhere predicate
respectively.

### M6 — medium — unit 2 §4 Populations and S2's docstring: §6 by ordinal, Gates by heading

`SEC = ^## %s\.` keys §6 by ordinal; `GATES_HEAD` keys the Gates section by heading text, and
`extract_gates`' own docstring records `TOOL-aJoinedCanon-7` closing exactly this hole for gates
only. `memory/TEMPLATE-SPEC.md` declares the Tier-1 light profile, and six specs in the tree carry
`## 5. Acceptance criteria` (re-counted at synthesis), two of them from `cSpliceWarden` dated
`2026-09-12`. For such a live spec the bar join reads `## 6. Gates` as its bullet population, grades
nothing, and the report line counts it as examined — a silent skip in the class the gate exists
for. §4's exclusion list and §5 risk 5 name other evasions and not this one, and S2's "what this
join cannot see" paragraph is left unspecified.

**Fix.** Locate the acceptance section by heading text for the bar join — an `AC_HEAD` beside
`GATES_HEAD`, `^## [0-9]+[.] Acceptance criteria` — or state the ordinal limit in the docstring's
WHAT IT DOES NOT CHECK paragraph and on the report line.

**Left-shift.** One `spec-tokens self-test` arm whose fixture is a light-profile spec (no §5,
`## 5. Acceptance criteria`) carrying a bar token, asserted as a hit; it is RED on the ordinal read
today.

### M7 — medium — unit 1 §6 AC6: a line clause with no observer

`bash tools/check-template-size.sh memory/guides/BUILD-METHOD.md` prints `26439 / 27648 bytes`
and no line figure; `tools/template-size-limits.txt` says for this subject "WHAT THE LEG DOES NOT
COVER is the LINE half of that budget line. No checker reads it". AC6's "a line count at or under
350" is attributed to a command that cannot produce it, and §4's 341-line PINNED estimate is never
re-measured.

**Fix.** `wc -l memory/guides/BUILD-METHOD.md` at or under 350 as its own observation in AC6, or
drop the clause.

**Left-shift.** The LINE half of the template-size declaration is an unread field on every row;
that is a backlog row for the template-size kit, not this unit's.

### M8 — medium — unit 3 §2 S5 and §6 AC9: the withholding is observed by nothing

`tools/unattended/kit.toml`'s first rule is `include = "**"`, `role = "engine"`; withholding works
only by a later `project-owned` row claiming the file, and govkit has no exclude. AC9's second
clause cannot fire: `govkit.py selfcheck` has no arm asserting a `*.test.sh` in a kit dir is
project-owned (it excludes `.test.sh` from its marker and shell scans), and `check-unattended.sh`
skips `*.test.sh`. `run-selftests.sh --list` reads `selftest-budgets.txt`, not the descriptor. So a
forgotten row ships the suite to every adopter through `**` with every criterion green — the
opposite of what S5 declares.

**Fix.** Give S5 an observation of the role: `python tools/govkit/govkit.py plan` (or a grep on the
descriptor's `project-owned` include list) resolving `gate-guard.test.sh` to project-owned, with a
red-when for the `**` rule claiming it.

**Left-shift.** The class — a `*.test.sh` in a kit directory with a budget row and no
`project-owned` claim — is one `selfcheck` arm in govkit; file it as a backlog row rather than
building it here.

### L1 — low — unit 3 §2 S8: four carriers with no criterion

S8 says "Observed by AC8, AC12, AC13". AC8 observes the version step and template/render parity,
not that the Skill half-sentence exists; AC12 is `test_codebase_map.py` exit 0, which grades
claims, headings, affordances and generated artifacts and nothing about prose being refreshed;
AC13 is `manifest-check.sh` exit 0, which grades the stamp and not the trap line, and nothing greps
the `manifest-audit: delta` commit line. The README paragraph, the Skill half-sentence, the dossier
refresh and the trap line can all be omitted with §6 green.

**Fix.** Pin one phrase per carrier in §4 and grep-count each in a criterion, as unit 1 does for
its five; add the delta-line grep to AC13.

**Left-shift.** None; pinned-phrase greps are the observation.

### L2 — low — unit 3 §3 Edges and §4 The predicate: a citation into the sibling that does not hold

Both say unit 1's AC6 names `kit-dogfood-parity.test.sh --render`. Unit 1's AC6 names a
`sed | diff` render and `check-template-size.sh`; the `--render` verb appears only in unit 1 §4
Carrier 3, and unit 1 §3 says the `sed` render was chosen as "the flag-free alternative" to that
verb. The edge's evidence that unit 1 depends on the read-only rule does not exist where it is
cited.

**Fix.** Cite unit 1 §4 Carrier 3 in both places.

**Left-shift.** None.

### L3 — low — unit 2 §5 perf and §7: the wrong leg is priced

§5 prices `spec tokens` (1.586 s in the ledger, 60 s ceiling) — a leg this unit does not grow. The
leg it grows, `spec-tokens self-test`, has a 120 s ceiling in `tools/gate-legs.json`, one ledger
reading of 76.061 s for 20 scratch repos (about 3.8 s of `git init` + commit + python each on this
node), and `selftest-budgets.txt` records "worst of 6 readings 80s". Seven more repos project to
about 103 s idle, 108 s at the worst reading, and the house rule of worst×1.5 (162 s) already
exceeds the ceiling the spec neither re-declares nor mentions. The owed `GATE_SELFTESTS=1` bar at
`VERIFYING` runs legs concurrently, which is the contended case.

**Fix.** Price the self-test leg in §5 and either re-derive its ceiling in the same commit or have
the seven arms share one scratch repo per fixture family.

**Left-shift.** The ceiling is the gate. A breach is the intended red, not a defect in the gate.

### L4 — low — unit 3 §4 Files touched, the manifest row: half a stamp

The trap line is manifest BODY, and `manifest-check.sh` C9 measures the stall from
`last-body-change`, yet the row names `last-audit` only. Unit 1's S5 in this same build names both
stamps for its own body edit, and the house precedent `a4a512de` advanced both for a traps-section
edit. Following the row as written leaves `last-body-change` at unit 1's parent after a second
body revision — the half-stamp the `stamps` gotcha records a closing review treating as a blocker.
No gate reds it this build (C9 needs ten watched commits), so it lands as a wrong record.

**Fix.** Name both stamps: `last-audit` (datetime advanced, merge-base sha) and
`last-body-change` (the commit's parent), as unit 1 spells it.

**Left-shift.** C9 is the gate, late by design. Nothing new.

### L5 — low — unit 3 §4 The key, last paragraph: a retired invariant asserted as live

"One live run per branch is the kit's own invariant." `UNATTENDED-PROTOCOL.md` states concurrent
runs are PERMITTED, that the rule "replaced an at-most-one-live-run rule … nothing keys on it", and
that the only surviving per-record invariant is one live record per BUILD FOLDER;
`TOOL-aUnblockedFleet-1` records the retirement, and no per-branch uniqueness exists in
`unattended.sh`, `lib-unattended.sh` or `check-unattended.sh`. The design survives — the hook reads
every record on the branch — but the sentence is the refuted-premise shape
`TOOL-cRefutedPremise-1` warns outlives review.

**Fix.** Delete the sentence; keep the deny-if-any-record-is-pre-`VERIFYING` rule as the design.

**Left-shift.** None.

## What this round did not cover, said so a green row is not misread

- No code exists yet; every finding is against a spec, and the refuted 24 are not listed here.
- The four in-flight specs H3 names were read for bar tokens only, not audited.
- The `BAR` reproduction used the checker's extraction helpers imported from
  `tools/check-spec-tokens.py` at `27ba9c0c` and unit 2's regex typed from its §4; the shipped
  regex may differ once built, and unit 2's own AC8 is where that is graded.

## Disposition

- Unit 3: NON-CONVERGED. Rev-2 folds B1, H1, H4, H5, M5, M8, L1, L2, L4, L5; round 2 owed.
- Unit 2: CONVERGED at round 1 with H2, H3, M1, M6, L3 folded — after the owner answers the
  decision above, because it decides whether B1's fold lands in unit 3 or in unit 2 §4.
- Unit 1: CONVERGED at round 1 with M2, M3, M4, M7 folded.
