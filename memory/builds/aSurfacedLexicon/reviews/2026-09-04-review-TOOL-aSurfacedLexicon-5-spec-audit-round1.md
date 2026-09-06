**Serves:** spec-audit TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-9 TOOL-aSurfacedLexicon-6

# Spec audit round 1 — the enforcement half, and the four ways it lands red

Tier-2 spec audit · 2026-09-04 · node `a` · build `aSurfacedLexicon` · streams tooling · designs
only, no code exists yet. Auditing DESIGNS, not code: every finding below is about what the three
specs say, and the tree is read only to check what they say against it.

**Subjects**, pinned at the blobs this round read, ROUND 1:
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-5.md@2bddafb4abde8f737a4a3332e0012abf51a52643`,
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-9.md@fd19a09fbcd08ee15cda8feba671f91dd3a2b382`,
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-6.md@3fc88f86326fe8e320fe736de9969a43ca2468ac`.

## Verdict: BLOCKED

Four blockers, thirteen highs, six mediums, after deduplication. Three of the four blockers are the
same shape wearing different clothes: a criterion phrased against `python tools/lexicon/lexicon.py
--check` over the REPO's own `.lexicon.conf`, at a build order where that declaration has nothing
for the criterion to grade. The fourth is arithmetic — the verb-offender pin has exactly zero
headroom and `TOOL-aSurfacedLexicon-5` mints a name into it without moving it, so the landing commit
reds the very leg that unit nominates as where its criteria are observed.

None of the four needs a design change. All four are spelling: say which declaration each criterion
is measured against, and move one pin.

## Review shape

Raw 62 · confirmed 40 · refuted 22 · unverified 0 · precision 0.65. A parallel finder fan followed by
an adversarial skeptic prompted to refute each finding, then this synthesis pass. The forty confirmed
findings deduplicate to the 23 rows below; the raw ids each row folds are named in its address line
so a reader can reconcile this record against the run.

Precision at 0.65 is the healthy end of the band and better than the 0.49 the same build's earlier
spec-audit round scored. The improvement is where the earlier round said it would be: the survivors
are overwhelmingly the findings that ran something.

**Severity is adjudicated in THIS record**, not inherited from the finders. Three rows moved and each
says so in place: H8 down from blocker, M2 down from high, M5 down from high.

## Index

| # | Sev | Subject | Address | One line |
|---|---|---|---|---|
| B1 | blocker | unit 5 | §4 Rollout vs §6 | Seven criteria grade cells the build does not arm until order 7 |
| B2 | blocker | unit 5 | §4 Inventory | `classify` reds the verb pin, which has zero headroom |
| B3 | blocker | unit 6 | §6 AC8, §8 F2 | The mandated guard edit reds `govkit selfcheck` on every bar |
| B4 | blocker | unit 6 | §2 S1 vs §6 AC2 | `UNDECLARED CELL` reds on its own landing commit |
| H1 | high | unit 6 | §4, §6 AC5 | Three stale population pairs gated into the shipped declaration |
| H2 | high | units 5, 6, 9 | §4, §7 | New public defs, no `symbols.json` regen, unguarded push leg |
| H3 | high | unit 5 | §2 S8 | The teeth line has no criterion, so it can ship absent |
| H4 | high | unit 6 | §3 Non-goals | "Seven `py.file` violations" is eight, against a pin of 7 |
| H5 | high | unit 6 | §2 S5 | Arms `py.constant` and states no tree verdict for it |
| H6 | high | unit 6 | §10 | Cites a WONTDO as a ruling and misses the CLOSED prior art |
| H7 | high | unit 9 | §2 S6, §6 AC3 | `DEAD PROBE` already ships; the criterion cannot fail |
| H8 | high | unit 9 | §2 S4, §4 | Three named read sites are DELETED at order 1, not collapsed |
| H9 | high | unit 9 | §2 S4 | Two read sites in `drift-audit` are missed; a gated signal narrows |
| H10 | high | unit 9 | §6 | No criterion runs `--suggest`, the half-wired state S4 exists to end |
| H11 | high | unit 9 | §6 AC7 | Observes a property of the edit, not of the code; cannot fail |
| H12 | high | unit 9 | §4, §8 F2 | Per-key merge over a shipped set lands ungated |
| H13 | high | unit 9 | §6 AC2 | A sibling's landing at order 4 inverts this standing arm |
| M1 | medium | units 5, 6 | §4, §2 S5 | Two specs disagree about which unit arms the first cell |
| M2 | medium | unit 6 | §7 | Never says `lexicon selftest` is invisible to the push bar |
| M3 | medium | unit 6 | §6 AC1, §8 F1 | `.js` figures stale: 8 files not 11, 69 functions not 122 |
| M4 | medium | unit 9 | §5 vs §7 | Two sentences predict opposite verdicts for `lexicon wiring` |
| M5 | medium | unit 9 | §5 i18n | Calls a filed, OPEN backlog row "unfiled" and re-orders it |
| M6 | medium | unit 9 | §8 F1 | Line-keyed cite lands on the wrong backlog record |

## Blockers

### B1 — seven of unit 5's ten criteria grade cells that do not exist at its build order

**Address:** unit 5 §4 `### Rollout` against §6 AC1, AC2, AC3, AC4, AC5, AC7 and AC10, and §7 clause
1. Folds raw ids 1, 19, 35.

Rollout says the predicate "lands inert ... no cell is armed until the conf rewrite unit pastes the
matrix". That unit is `TOOL-aSurfacedLexicon-12` at build order 7; unit 5 is order 3.
`TOOL-aSurfacedLexicon-4` at order 2 says the same thing in its own §4 Migration — the conf rewrite
that pastes the real `CELLS` body "is a later unit", so an absent block resolves to an empty
container. Measured here: `grep -nE '^[A-Z]+:' .lexicon.conf` returns `VERBS:` at 185 and `LAYERS:`
at 215 and nothing else.

Yet AC1 through AC5, AC7 and AC10 are phrased as `python tools/lexicon/lexicon.py --check` grading or
redding `py.function`, `py.type`, `py.file` and `sh.file` on the tracked tree, and §7 says those
verdicts are "observed on the bar" — a leg whose argv reads the repo's own declaration. At order 3
there is no armed cell, so none of the seven can be observed. Unit 5's own Files-touched table has no
`.lexicon.conf` row, which confirms the unit does not intend to arm them itself.

The two criteria the build rule requires be observed RED — AC1's staged `loadUserData` and AC10's
staged `_` — are exactly the ones lost. "A new predicate is not landed until its failing case has
been observed" cannot be satisfied as written. AC6 already says "in a scratch declaration" when it
means one, so the omission in the other seven is not shorthand.

**Fix.** Pick one and say which. Either name in §4 Rollout the minimal `CELLS` rows this unit writes
itself, move them out of unit 12's scope, and strike the inertness sentence; or re-phrase AC1-AC5,
AC7 and AC10 against a scratch declaration the way AC6 is, and rewrite §7 to say the observation
route is a scratch conf rather than the bar's own.

**Left-shift.** A spec-lint arm over `memory/builds/*/spec/*.md`: a criterion naming
`tools/lexicon/lexicon.py --check` must also name the declaration it is measured against — the
tracked conf, a scratch conf, or a fixture repo. A criterion that names none is refused. This class
is a criterion observing a state the build does not reach at that order, and it produced three of
this round's four blockers.

### B2 — `classify` reds the verb-offender pin, and no section moves the pin

**Address:** unit 5 §4 `### Inventory` (the `classify` paragraph), §4 `### Files touched` and §7.
Folds raw ids 37, 48.

Measured in this worktree at `693bcf96`: `python tools/lexicon/lexicon.py --check` prints `P1 verb
graded=1045 offenders=461 waived=0`, and `.lexicon.conf:164` reads `VERB_OFFENDER_PIN="461"`.
Headroom is exactly zero. Offenders are counted per OCCURRENCE, not per distinct name, so §4's
reasoning about `classify` being "one of the 418 UNRULED offenders" does not save it: a new
`def classify` in tracked `subtokens.py` takes the count to 462 and `lexicon.py`'s
`if len(unwaived) > pin` reds. The finder staged the bare def and observed exactly that, then
restored the file; the gate is back at 461.

`TOOL-aSurfacedLexicon-4` S9 converts that comparison to a two-sided equality, so 462 against 461
reds under both the old rule and the new one. The leg that reds is `lexicon naming predicates`, whose
guard is `['tools/', 'skills/session-kickoff/', '.githooks/', '.claude/']` — a diff touching
`tools/lexicon/subtokens.py` selects it — and it is the same leg §7 nominates as where AC1 through
AC7 and AC10 are observed. So the unit reds its own verification leg for a reason no criterion
covers, and §4 Rollout's claim that it lands "without moving a single verdict on the bar" is false.

Keeping the name is the right call and §4's argument for it is sound. The defect is that keeping it
costs a pin raise the spec does not budget.

**Fix.** Add `.lexicon.conf` to the Files-touched table for the pin raise, and add a criterion that
`VERB_OFFENDER_PIN` moves 461 to 462 in the same commit — in the conf's existing RAISED-by-name
comment form, with `classify` named as the sole arrival and the command that measured it. Cite
`memory/backlog/TOOL.md` row `TOOL-aResumedRelay-1` (OPEN), which already refused a rename for this
same engine-name class on the scoping-not-spelling argument §4 re-derives from scratch.

**Left-shift.** An arm in the spec-token checker: for every identifier in a spec's Inventory table,
run `python tools/lexicon/lexicon.py --suggest <name>` and record the verdict in the spec; when the
verdict is an offender, require the spec to name the pin and the new value. `TOOL-aSurfacedLexicon-4`
already tables `--suggest` verdicts for its minted names, so this makes the build's own better habit
the rule.

### B3 — unit 6 mandates a guard edit a sibling already measured as bar-redding

**Address:** unit 6 §6 AC8 and §8 F2, against `TOOL-aSurfacedLexicon-4` §3 and its rev-6 strike.
Folds raw ids 13, 21, 45, 55.

AC8 requires that a conf-only diff select the `lexicon naming predicates` leg, "observed by running
the bar over a conf-only diff before and after the guard edit", and F2 recommends the same edit:
add the root-level `.lexicon.conf` to that leg's guard.

`TOOL-aSurfacedLexicon-4` struck exactly this edit at rev-5/6 after measuring it. `tools/govkit/govkit.py`
requires every guard pathspec to fall into EXACTLY ONE declared class — memory-root-relative,
verbatim `.githooks/` or `.claude/`, renamed `skills/session-kickoff/`, a declared exempt prefix, or
kit-relative `tools/`. A repo-root file matches zero, so `len(classes) != 1` fails with
"guard pathspec '.lexicon.conf' ... falls into 0 declared classes". Verified independently here:
every distinct guard in `tools/gate-legs.json` today is one of those prefixes, no `[[exempt]]` row in
`tools/govkit/registry.toml` names the conf, and the ruling is written in prose in
`tools/lexicon/kit.toml` directly above the block that carries the same guard array a second time.

Worse than F2 states: `govkit selfcheck` carries NO `guard` key (chunk `declarations`, subject
`repo`), so it runs on every bar including the push boundary. F2 prices the edit as "every conf edit
now pays the predicates leg, which is a 300 s ceiling"; the real cost is a red push. AC8 as written
cannot pass. Unit 6 is rev-1 at base `d0a18683` and never saw the strike, and §6 has decided a fork
§8 still presents as undecided.

**Fix.** Strike AC8, adopt unit 4's disposition by reference in F2, and re-route the conf-only
observation AC1 and AC2 depend on. The leg that actually reaches the declaration on a conf-only diff
is `lexicon wiring` (guard `[]`), which shells out through `bash tools/lexicon/adopt-lexicon.sh
--check` to `load_conf`. Either phrase those criteria against that leg and the direct command, or
stage the break in a diff that also carries code under `tools/`. If the guard genuinely must widen,
the class-legal spellings are an `exempts` entry in the govkit registry or a `tools/`-side trigger —
and AC8 then also has to assert `govkit selfcheck` GREEN after the edit.

**Left-shift.** A spec-lint arm: a spec proposing a `guard` edit in `tools/gate-legs.json` must show
`python tools/govkit/govkit.py selfcheck` green with the edit staged. Cheaper still, and it also
catches the second carrier: `govkit`'s parity arm compares a leg's name, subject and chunk and never
its guard, so a guard array duplicated into a `kit.toml` can diverge silently. Extend that comparison
to the guard.

### B4 — unit 6's `UNDECLARED CELL` reds on the commit that lands it

**Address:** unit 6 §2 S1 against §6 AC2 and §4 `### Files touched`. Folds raw id 22.

S1 makes every (extension, surface) pair with a non-empty population and no `CELLS` row a refusal.
§4 Files touched adds exactly ONE row to `.lexicon.conf`, `py.constant`, and AC5 asserts only that
one. Unit 6 is order 4; the conf rewrite that pastes the matrix is order 7.

Measured at `693bcf96`: `py.function` grades 976, `py.type` 41 and `js.function` 69 (the split of the
`P1 verb graded=1045` and `P2 suffix graded=41` lines the run prints). Three non-empty populations
with no `CELLS` row — three refusals fired by S1 on the landing commit itself. AC2's green half,
"unstaging it returns the run to `0`", is unreachable, because the run was never at 0.

The spec has no Rollout section at all, and §5's migration bullet says only "the conf gains rows and
a comment", so nothing in the design confronts what S1 does against a declaration with no matrix.

**Fix.** Add a Rollout section that states it. Either land `UNDECLARED CELL` dark until order 7 —
computed and reported, refusing nothing — or pull the full `CELLS` block into this unit's scope and
out of unit 12's. Then reconcile AC2's "returns the run to `0`" with whichever is chosen.

**Left-shift.** Same arm as B1: a criterion asserting an exit code over the tracked tree must name
the declaration state it assumes. A second, cheaper arm catches the sibling case: a spec introducing
a refusal over a DECLARED population must state what that refusal does when the declaration is empty,
because "empty declaration" is the state every such unit passes through on its own landing.

## Highs

### H1 — three stale population pairs, gated into the shipped declaration

**Address:** unit 6 §4 `### The measured populations this unit ships` and §6 AC5. Folds raw ids 14,
25, 46, 56.

Unit 6 is still pinned to base `d0a18683` while its order-3 sibling was re-pinned to `6c670b02` and
re-measured. Re-derived here at `693bcf96` by a module-body `ast` walk over the 49 files
`git ls-files '*.py'` returns:

| Population rule | spec says | measured now |
|---|---|---|
| All module-body targets, tuple unpack and `AnnAssign` included | 527 / 419 | 544 / 436 |
| Simple single-`Name` targets, `AnnAssign` included | 432 / 413 | 449 / 430 |
| Public simple targets | 331 / 331 | 346 / 346 |

The violation columns 108, 19 and 0 reproduce byte for byte, which proves this is the same reading
against a moved base and not a disagreement about the population.

AC5 mandates that "527 against 419, 432 against 413, and 331 against 331" be written into
`.lexicon.conf` as a shipped comment AND asserted by a `tools/lexicon/selftest.py` arm. So three
wrong numbers become tracked adopter-facing text with a gate certifying them. §4's related figures
move too: "the 47 tracked `.py` files" is 49, and "`py.function` grades all 925" is 976 — which
contradicts unit 5's AC3, "0 violations of 976", outright. This is the spec the build designates as
owning population sizes.

One caveat worth keeping, because it is the deeper defect. Rows 2 and 3 reproduce only when
`AnnAssign` targets are counted; the obvious reading that excludes them gives 406/391 and 312/312.
A finder reading the same prose landed on 556 for row 1 where I measure 544. The spec's stated rule
is not precise enough for a second party to reproduce it, which is why the numbers drifted quietly in
the first place.

**Fix.** Re-pin the status header to the landing base and re-measure all four figures with the
command beside each. State the reading precisely enough to reproduce — whether `AnnAssign` and tuple
targets are in. Then prefer writing the RULE plus its command into the conf comment over three
number pairs nothing re-derives, which is the argument §4 already makes for the rule string beside
the count.

**Left-shift.** A memory-tree hygiene arm: a spec whose status `base` is an ancestor of the build
folder's current base, and which carries a numeric table, reds until re-pinned or explicitly marked
as a historical measurement. The build rule "every number carries the command that produced it" is
gateable one step further — the command has to be re-runnable at the spec's own base.

### H2 — new public defs, no `symbols.json` regen, and the leg that catches it is unguarded

**Address:** unit 5 §4 `### Files touched` and §7; the same omission in units 6 and 9. Folds raw ids
23, 38, 51.

`memory/map/generated/symbols.json` already indexes `subtokens` and `leading_verb` from
`tools/lexicon/subtokens.py`, which declares no `__all__`. Unit 5 mints four public module-level defs
into that exact file — `read_core`, `classify`, `check_convention`, `read_stem` — so the artifact
goes stale in the same diff. The `codebase-map coverage + freshness` leg carries NO `guard` key
(chunk `declarations`, subject `repo`, ceiling 300), so it runs on every bar including the push
boundary, and its freshness arm byte-compares the committed artifact against a live re-derivation.

Unit 5's Files-touched table has no `memory/map/generated/` row, and §7 names `codebase-map kit
selftest` — a guarded `selftests` leg asking a different question — while omitting the unguarded one.
Both siblings carry the obligation for the identical situation: `TOOL-aSurfacedLexicon-3` S10/AC10,
and `TOOL-aSurfacedLexicon-4` S11/AC12, the latter having measured the RED directly. Units 5, 6 and 9
are the outliers.

**Fix.** In all three: add `memory/map/generated/symbols.json` (regen `python
tools/codebase-map/gen_map.py --write`) to the Files-touched table, add `codebase-map coverage +
freshness` to §7, and add a criterion modelled on unit 4's AC12 that observes the STALE failure
first. Name the `memory/map/features/lexicon.md` dossier claim in the same commit, which the charter
DoD requires anyway.

**Left-shift.** A spec-lint arm: a spec whose Files-touched table names a `.py` file under `tools/`
and whose Inventory mints a public module-level def must also name `memory/map/generated/`. The
inputs are both already in the spec; nothing has to be inferred from the tree.

### H3 — the teeth line has no criterion, so an implementation with no teeth passes

**Address:** unit 5 §2 S8, against §6 and §5 observability. Folds raw id 3.

S8 requires every run to print, per armed cell, how many names the OTHER conventions would violate.
No criterion in §6 observes any printed teeth line. AC6 is labelled the teeth arm but observes a
different thing: a one-off re-declaration of `py.function` as `camel` in a scratch declaration
reporting 736 of 976. That is a manual experiment producing the figure the teeth line would print,
not the shipped output.

An implementation that ships no teeth line at all passes all ten criteria — while §5 calls that same
line "the observability requirement, not a nicety: a cell printing zero violations and nothing else
is indistinguishable from a cell that cannot fail". A scope item whose stated purpose is defeating
green-by-absence, itself shipping with no observation.

**Fix.** Add a criterion: on a green `--check` with nothing staged, the run prints a teeth line for
each armed cell, and a `tools/lexicon/selftest.py` arm reds when a cell's row carries a violation
count with no teeth figure beside it.

**Left-shift.** The general arm this round wants most: every Scope (IN) item is named by at least one
§6 criterion, asserted mechanically by id. S8 here, S4 in unit 9, S5 in unit 6 and S6 in unit 9 are
four instances of the same miss in one spec set.

### H4 — "seven `py.file` violations" is eight, against a pin of 7 about to go two-sided

**Address:** unit 6 §3 Non-goals, the `py.file` bullet. Folds raw id 57.

Measured by first-dot stemming over `git ls-files '*.py'`: eight offenders, not seven —
`aiosqlite-seam-conftest`, `check-arms`, `check-kit-placeholders`, `check-recall`, `check-spec-tokens`,
`merge-rows`, `ps-hygiene`, `settings-merge`. Unit 5's AC4 already says eight and names
`check-kit-placeholders.py` as the one that joined.

The seven is load-bearing elsewhere. `memory/backlog/TOOL.md` row `TOOL-aSurfacedLexicon-15` (OPEN)
states seven and records that `TOOL-aSurfacedLexicon-4`'s `PINS` block carries `py.file.conv 7`; unit
4's §4 confirms the row as `{"py.file.conv": 7}`. Unit 4 S9 makes the pin comparison a two-sided
equality against the declared count, so a pin of 7 against a population of 8 reds the moment the cell
is armed. The spec that owns population sizes restates the stale figure instead of reconciling it.

**Fix.** State eight with its command, name the eighth basename, and add an explicit hand-off
correcting unit 4's `py.file.conv` pin row to 8 and the backlog row with it. That row already
sequences the drain after this unit, so it is the natural carrier.

**Left-shift.** A gate the build is already halfway to: `PINS` values in `.lexicon.conf` are DERIVED
figures, so a spec stating one in prose must carry its command, and a checker should compare every
pin in a spec's prose against the pin block it names. This is the charter's "no count of a derived
population is written in prose" applied to specs.

### H5 — unit 6 arms `py.constant` and never states the verdict that arming produces

**Address:** unit 6 §2 S5, against §6. Folds raw id 15.

Enumerating §6: AC1 is `js.type` DEAD CELL, AC2 UNDECLARED CELL, AC3 the report row count, AC4 the
row's shape, AC5 the conf comment, AC6 the empty report, AC7 DEAD PROBE, AC8 the guard. None states
that arming `py.constant` on the public-simple-target population actually yields zero violations.
Measured here it yields 0 of 346, narrowed from 544 module-body targets — a number asserted nowhere
in the spec and discovered only when the bar reds.

The sibling does exactly this: unit 5's AC3 pins "0 violations of 976". So the asymmetry is measured
against the build's own standard, not an invented one. S5 also takes an unstated hard dependency on
unit 5's `screaming` form, which §2 never declares as a prerequisite the way unit 9's S1 does.

**Fix.** Add a criterion: with `py.constant screaming` armed and nothing staged, `--check` reports
the constant cell at 0 violations of its graded count with the rule string present, each number
carrying its command. Add a sentence to S5 naming `TOOL-aSurfacedLexicon-5` as the prerequisite that
supplies the form.

**Left-shift.** Covered by H3's arm (every scope item owns a criterion), plus a narrower one worth
having on its own: a scope item that ARMS a check must state the verdict the arming produces on the
real tree, since "it arms" and "it arms green" are different claims and only the second is a
measurement.

### H6 — the reuse audit cites a WONTDO as a ruling and misses the CLOSED prior art

**Address:** unit 6 §10 and §2 S2. Folds raw ids 58, 59.

Two defects in one section, on adjacent backlog rows.

`memory/backlog/TOOL.md:215` is `TOOL-dScaffoldedMirror-3 · WONTDO`, and that spec's own header reads
"superseded by TOOL-dScaffoldedMirror-8, whose S5 deletes this unit's justification". §10 cites it as
the ruling that "already established the shape this unit's report follows". A WONTDO unit whose
justification was deleted ratified nothing, so the reuse audit certifies prior art that does not
exist.

The record that DID establish the print-on-green shape is `TOOL-dScaffoldedMirror-2 · CLOSED` at
`:214`, and §10 omits it. Its text ends "RED on an armed predicate whose population is 0" — the exact
refusal S2 builds as new. The shipped tree does not have that red: `tools/lexicon/lexicon.py` prints
`armed but grading nothing (reported, not a refusal)`, and a live run emits `.js suffix=0` and exits
0, which I confirmed. So a CLOSED row stands claiming a red that never shipped, nothing records the
descope, and S2 rebuilds the dropped half without saying why it was dropped the first time.

**Fix.** Re-anchor §10 on `TOOL-dScaffoldedMirror-2`; either drop the `-3` citation or re-label it
explicitly as a WONTDO whose report shape was inherited by `-8`, never as an established ruling. Cite
`-2` in S2 as well, record what its closure actually delivered (the per-predicate split and the
green-line counts, not the red), and add a line saying the backlog row needs its claim corrected so a
reader does not find a false CLOSED claim standing.

**Left-shift.** A checker over spec §10 blocks: every cited `FAMILY-slug-seq` is resolved against
`memory/backlog/` and `memory/DECISIONS.md`, and a citation whose status token is `WONTDO` or
`DEFERRED` must carry that token in the citing sentence. The status is machine-readable and the
citation is machine-findable, so this is a grep and a table lookup, not a judgement call.

### H7 — unit 9's `DEAD PROBE` scope item is already shipped, and its criterion cannot fail

**Address:** unit 9 §2 S6 and S7, §6 AC3, §10. Folds raw ids 24, 41.

The refusal already ships. `tools/lexicon/lexicon.py` loops `sorted(declared.items())`, skips
`mode == "dark"`, requires `any(ext_of(f) == ext for f in files)`, and appends
``DEAD PROBE — .{ext} is declared `{mode}` ({pset})`` — every clause S6 describes, pattern-set id
included. I read the arm directly.

So AC3 ("exits non-zero printing `DEAD PROBE` and the pattern-set id; removing the row greens it") is
satisfied by unmodified engine code the moment S1's parser accepts the block. It observes nothing
this unit builds and cannot fail for this unit's reasons.

S7's justification is false against the same shipped code: "without it a zero population satisfies
the DEAD PROBE arm by accident" — the `any(ext_of(f) == ext for f in files)` guard already excludes
an extension with zero tracked files. `INERT DECLARATION` is genuinely new and worth having; it is
being justified by a hole that does not exist. §10's reuse audit ranks `extract` and never looks at
the refusal it is duplicating, while unit 6's §10 correctly lists the same arm as shipped — two specs
in one build disagreeing about whether the code exists.

**Fix.** Rewrite S6 to say the shipped arm already covers a declared set that grades nothing, and
name what this unit actually adds: a pattern set reachable only through a declared `PATTERNS` row is
now inside that arm's population. Re-point AC3 at that. Re-justify S7 on what it really buys — a
named report for a declared-but-unpopulated extension the shipped guard skips SILENTLY.

**Left-shift.** The reuse-audit rule the earlier round already derived, one notch tighter: §10 must
name the shipped code path each Scope (IN) item extends, or state that none exists — and for a unit
adding a refusal, it must enumerate the refusals the target file already carries. Unit 6 did this
correctly in the same build, so the habit exists and only needs to be required.

### H8 — three of unit 9's six named read sites are DELETED at order 1, not collapsed

**Address:** unit 9 §2 S4 and §4 `### Inventory`. Folds raw id 20. **Severity adjudicated down from
the finder's blocker**, because §4's hedge lands an implementer in the right place operationally;
what is wrong is the scope commitment, not the buildability.

S4 puts six `PATTERN_SETS` read sites in scope. Measured: `awk '/^def /' tools/lexicon/lexicon.py`
puts `run_brief` at `:916` and `run_probe` at `:1053`, so S4's `:945`, `:999` and `:1081` all sit
inside them — and `TOOL-aSurfacedLexicon-3` S1 and S2 DELETE both functions outright at build order
1, three orders before this unit lands. §4 misdescribes their fate as sitting inside walks that unit
"collapses into one `scan_corpus`".

Collapsed and deleted are different. A collapsed site still needs the resolved mapping threaded
through it; a deleted one needs nothing. §4's hedge — "the inventory above is smaller" — tells an
implementer to expect fewer sites in `scan_corpus` rather than none of these three. The build's own
house style is to name the deletion: units 10 and 11 each write "`run_probe`, which
`TOOL-aSurfacedLexicon-3` deletes at build order 1".

**Fix.** Rewrite S4 and the §4 table to the three sites that survive order 1 — `:244`, `:557`, `:726`
— and state that `:945`, `:999` and `:1081` are deleted rather than collapsed, citing
`TOOL-aSurfacedLexicon-3` S1 and S2 by name.

**Left-shift.** A spec-lint arm over line-pinned code cites: every `path:NNN` in a spec resolves at
the spec's stated base, and a cite inside a function a same-build sibling deletes is flagged by
name. The sibling specs are in the same folder, so the deletion set is derivable without reading the
tree.

### H9 — two read sites outside the kit are missed, and a gated signal narrows silently

**Address:** unit 9 §2 S4 ("Every read site takes the resolved mapping") and §4 Inventory ("Measured
six of them"). Folds raw id 40.

There are eight, not six. `tools/drift-audit/drift_report.py:827` and `:890` both test
`pset not in lex.PATTERN_SETS` and `continue`, and `:830`/`:937` call `lex.extract` / `lex.extract_text`
positionally with no mapping to pass. `drift_report.py` appears nowhere in §4's Files touched.

Since S3 forbids mutating the module constant, a language armed only through `PATTERNS:` fails both
membership tests and is skipped file by file, so `signal_lexicon_verbs_unused` and
`lexicon_marginal_offense_rate` grade a smaller population while reporting a clean number with
`live` still true from the Python half. That is the exact "both operands from one extractor" property
§3 cites as the reason the `extract` contract is frozen — defeated by the change that cites it, and
it is the green-by-absence class on a gated signal.

**Fix.** Extend the §4 Inventory to the two out-of-kit sites with what each decides, add
`drift_report.py` to Files touched, and add a criterion that a fixture declaring a `PATTERNS`-only
language is SEEN by `python tools/drift-audit/drift_report.py` rather than skipped. Or state as an
explicit non-goal that drift-audit grades shipped sets only, and say what that costs.

**Left-shift.** A scope item saying "every read site" owes a repo-wide derivation, not a
single-file one: `grep -rn 'PATTERN_SETS' --include='*.py'` across the tracked tree, pasted with its
command, is the evidence. Gate it as a spec-lint arm — a Scope (IN) item quantified over "every" must
carry the enumerating command.

### H10 — no criterion runs `--suggest`, so the half-wired state S4 exists to end can ship

**Address:** unit 9 §6, against §2 S4. Folds raw id 8.

Nothing in §6 invokes `--suggest` at all. AC1 and AC2 do implicitly exercise `:557` — an unresolved
`:557` would push the fixture's `ts` file onto `problems` and grade nothing — but the three sites
deciding whether `--suggest` reports an extension as gradeable can keep reading the module constant
while every criterion passes. So can `:726`, the armed-coverage fraction.

The shipped symptom is a kit that grades `.ts` under `--check` and still tells the adopter `.ts` is
ungradeable under `--suggest`, which is the exact half-wired state the block exists to end. No
non-goal excludes `--suggest`.

**Fix.** Add a criterion running `python tools/lexicon/lexicon.py --suggest <name>` in the `ts`
fixture repo and asserting the coverage line counts `.ts` as gradeable, plus one asserting the
armed-coverage fraction moves when the declared language is armed. (Note the interaction with H8: the
surviving site set is `:244`, `:557`, `:726` plus whatever `scan_corpus` holds, so the criterion
should name the BEHAVIOUR, not the line numbers.)

**Left-shift.** H3's arm again, plus one specific to CLIs: a unit changing what a multi-subcommand
tool knows must carry a criterion per SUBCOMMAND whose answer changes. "The engine resolves it" and
"every surface reads the resolution" are two claims.

### H11 — AC7 observes a property of the edit, not of the code

**Address:** unit 9 §6 AC7. Folds raw id 9.

AC7 asserts only that `git diff --stat tools/lexicon/lexicon.py` is empty for a conf-only arming
edit. That is true by construction: adding a `LANGS` triple and `PATTERNS` rows touches no `.py` file
whether or not `KNOWN_EXTS` still gates arming. If the gate remained, the diff would still be empty,
the arming would simply not work, and AC7 would still pass. The criterion S5 rests on observes
nothing — the charter's "a gate you have only ever seen pass is an assertion about nothing", in a
spec rather than in code.

AC1 does happen to observe S5's substance by grading `.ts` in a fixture repo, which is why this is a
high and not a blocker.

**Fix.** Make the observation the outcome: the same conf-only change causes the new extension to be
graded and to stop being reported as ungradeable, with `git diff --stat tools/lexicon/lexicon.py`
empty as a supporting clause rather than the whole criterion.

**Left-shift.** A spec-lint heuristic worth its false-positive rate: a criterion whose assertion is
about the DIFF rather than about a command's output is flagged for review. A diff-shaped assertion is
almost always a property of the action the author is about to take.

### H12 — per-key merge over a shipped set, the case that motivates the block, lands ungated

**Address:** unit 9 §4 `### Data model` and §8 F2. Folds raw id 10.

§4 specifies per-key merge over a shipped set — a declared `js-regex.types` row replaces that part
and leaves `functions` and `imports` untouched — and calls replacement "the case that motivates the
block at all". F2 is the open fork on exactly it.

No criterion observes it. AC1 declares a brand-new `ts-regex` set, AC5 covers the no-block case, AC8
only proves the shipped constant was not mutated, and none declares a row over `js-regex` and checks
the sibling parts survive. The non-goal is about SHIPPING a second set, not about merging over the
shipped one, so nothing excludes it. The behaviour distinguishing per-key merge from per-set
replacement, and the fork's chosen outcome, both land ungated.

**Fix.** Add a criterion declaring `js-regex.types` in this repo's own conf: the `.js` type count
changes, the `.js` function count does not, and — per F2's own mitigation — the run prints the
replaced key. Whichever way F2 resolves, it ships with that criterion.

**Left-shift.** Make it a rule that every fork in §8 owes a §6 criterion for the outcome it
ratifies. Unit 5's own F1 mark says exactly this about itself ("this fork must also gain a §6
criterion; as it stands the choice lands ungated"), so the build has already articulated the rule and
only unevenly applied it. A checker can assert that each RESOLVED fork's id appears in at least one
criterion.

### H13 — a sibling's landing at order 4 inverts unit 9's standing selftest arm

**Address:** unit 9 §3 Non-goals against §6 AC2 and §2 S9. Folds raw id 26.

S9's fixture repo arms `ts` in `LANGS` with two `PATTERNS` rows and no `CELLS` row. AC2 is a standing
`tools/lexicon/selftest.py` arm requiring the fixture to exit 0 once the offending definition is
removed. `TOOL-aSurfacedLexicon-6` lands `UNDECLARED CELL` at order 4, one order after this unit, and
its S1 reds any (extension, surface) pair with a non-empty population and no `CELLS` row — which the
fixture's `ts.function` is by construction. On that landing the fixture reds and AC2's green half
inverts.

The non-goal names the collision and does not price it: "A language armed here with no cell declared
is their UNDECLARED CELL refusal, not this unit's problem to pre-empt." That is a hand-off that lands
nowhere — unit 6 never mentions this fixture.

**Fix.** Have the S9 fixture declare its `ts` `CELLS` rows alongside its `LANGS` triple, which costs
nothing and makes the fixture order-independent. Failing that, state in §3 that AC2's arm is owed an
update by `TOOL-aSurfacedLexicon-6` and name it as a hand-off in that unit's scope.

**Left-shift.** A build-level checker: a non-goal that routes work to a named sibling unit must be
matched by a scope item, criterion or hand-off line in that sibling. Both documents are in the same
folder and the ids are greppable, so a one-way hand-off is machine-detectable.

## Mediums

### M1 — two specs disagree about which unit arms the first cell

**Address:** unit 6 §2 S5 against unit 5 §3 and §4 `### Rollout`, and `TOOL-aSurfacedLexicon-4` §4
Migration. Folds raw id 29.

Unit 6 (order 4) ships `py.constant` armed. Unit 5 (order 3) says flatly "no cell is armed until the
conf rewrite unit pastes the matrix" and makes arming a non-goal ("the conf rewrite arms it"), and
unit 4 says the same. The conf rewrite is `TOOL-aSurfacedLexicon-12` at order 7. Unit 12's own design
confirms unit 6 got there first — it preserves "the `py.constant` population comment". So unit 5's
sentence is false as written, and a reader of unit 5 would refuse the conf edit unit 6 requires. The
arming boundary is load-bearing rather than incidental: unit 6 needs that row for its own S7 liveness
refusal, since a zero-row cell report REFUSES.

**Fix.** State in S5 that this unit arms exactly one cell ahead of the conf rewrite, with the reason,
and amend unit 5's Rollout and unit 4's Migration so "no cell is armed until order 7" is not left
standing as a contradicted absolute. Folds naturally into the B1 and B4 rewrites.

**Left-shift.** A cross-spec consistency arm: an absolute claim about a build-wide state ("no cell is
armed until X") is asserted against every sibling spec's scope items. Cheap version — grep the spec
set for the state's noun and require the claim's author to cite the units checked.

### M2 — unit 6 never says `lexicon selftest` is invisible to the push bar

**Address:** unit 6 §7, against §6 AC3, AC4 and AC5. Folds raw ids 17, 60. **Severity adjudicated
down from one finder's high**, because the criteria themselves name their selftest arms — what is
missing is §7's disclosure and the DoD command, not the arms.

`lexicon selftest` is chunk `selftests`, subject `kit`, guard `['tools/lexicon/']`, ceiling 880.
`GATE_FULL` holds every `chunk = selftests` leg and `GATE_SELFTESTS` is on demand only; nothing at a
push boundary sets it. AC3's row-count arm, AC4's missing-rule-string arm and AC5's armed-row arm are
all selftest-only, and AC4's only RED is one — a red no push-boundary run will produce.

Both siblings state this in their own §7: unit 5 says "It is invisible to the push bar, so this
unit's DoD runs `GATE_SELFTESTS=1`", unit 9 says "nothing at the push boundary runs it". Unit 6's §7
is a bare leg chain that notes only the 880 s ceiling, so a reader takes a green push as covering
arms it never ran.

**Fix.** Expand §7 into per-leg rows with chunk, subject, guard and ceiling as units 5 and 9 have
them, say the leg is reachable only under `GATE_SELFTESTS=1`, and name
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` as this unit's DoD run.

**Left-shift.** A spec-lint arm reading `tools/gate-legs.json`: a criterion whose observation is a
`selftest.py` arm requires the spec's §7 to name that leg's chunk and the env var that reaches it.
Both facts are in the manifest, so the arm derives rather than trusting prose — and it is the
charter's "a skip must announce itself" applied to specs.

### M3 — unit 6's `.js` figures are stale

**Address:** unit 6 §6 AC1 and §8 F1. Folds raw ids 18, 61.

`git ls-files '*.js' | wc -l` returns 8, not AC1's "11 tracked `.js` files"; both were true at
`d0a18683`. F1's "`.js` keeps a healthy 122 functions" measures 69 — the run's `P1 verb graded=1045`
minus the 976 Python definitions.

AC1's substance survives and is worth keeping: the run still prints `.js suffix=0` and exits 0, which
I confirmed, so the `DEAD CELL` failing case is still free to stage and F1's keep-both argument still
holds at 69. The defect is two denominators a reader cannot reproduce, in the spec that owns
population sizes, while its order-3 sibling was re-pinned and re-measured.

**Fix.** Re-pin the header to the landing base and re-measure both with their commands. Keep the 122
only as a `d0a18683` figure if the historical contrast is wanted.

**Left-shift.** Covered by H1's base-freshness arm.

### M4 — unit 9's §5 and §7 predict opposite verdicts for the same leg

**Address:** unit 9 §5 user docs against §7, the `lexicon wiring` bullet. Folds raw ids 11, 33, 43.

§5 says "The rendered Skill needs no change: its `--suggest` routing does not name pattern sets".
§7 says the commented `PATTERNS:` example "trips it until the Skill is re-rendered". Both cannot
hold, and neither has a criterion.

§5 is the right half. `render_skill()` in `tools/lexicon/adopt-lexicon.sh` substitutes only
`{{VERBS_TABLE}}` (from `lexicon_conf.py --print-rows`, VERBS only), the three CLI tokens, `{{CONF}}`
and `{{KIT_VERSION}}`; a commented `PATTERNS:` block moves none of them, comment rows are dropped by
the block scanner, and the byte-compare stays green. This matters because `lexicon wiring` carries
guard `[]` and is therefore the ONLY leg that fires on this unit's conf-only diff — §7 states a red
that cannot happen, in the section that names the gates, and budgets a Skill re-render §4's
Files-touched list does not carry.

**Fix.** Strike the §7 clause, keep §5's sentence, and say what the wiring leg actually asserts here
— that the VERBS render is unaffected. Then give it a criterion, the way unit 5's AC9 gates the same
leg for its own diff.

**Left-shift.** A spec-lint arm: a spec asserting a named gate leg will RED must carry a criterion
observing that red. A predicted red with no criterion is a guess, and this one was wrong.

### M5 — a filed, OPEN backlog row is called "unfiled" and re-ordered

**Address:** unit 9 §5 Production-readiness, the i18n bullet. Folds raw id 52. **Severity adjudicated
down from the finder's high**, because the substance of the bullet — the gap is real, inherited and
widened — is correct; only its status claim and its directive are wrong.

The bullet calls D25 "the unfiled review finding" and says "the build README already owes it a
backlog row before the build starts". The row exists, is OPEN, and names this unit by id:
`memory/backlog/TOOL.md` row `TOOL-aSurfacedLexicon-16`, landed in `bb0eb74b`, whose text reads
"`TOOL-aSurfacedLexicon-9`'s `PATTERNS` block measurably WIDENS the population it applies to". Unit
9's rev-2 was written after that row was on disk. So the spec states a false status and directs a
build-start action that is already complete, with no id a reader could follow.

**Fix.** Replace the unfiled/owes-a-row language with the id `TOOL-aSurfacedLexicon-16`.

**Left-shift.** Covered by H6's citation checker, extended one step: a spec sentence claiming a
finding is UNFILED is checked against the backlog for a row naming that spec's own unit id.

### M6 — a line-keyed cite lands on the wrong backlog record

**Address:** unit 9 §8 F1. Folds raw id 53.

The adopter figures are cited to `memory/backlog/TOOL.md:222`. That line is
`TOOL-dScaffoldedMirror-10 · CLOSED`, the `--suggest`/`--brief` unit, and carries none of the numbers.
The 626 `.ts`, 572 `.tsx`, 1,190-of-6,168 and 19.3% figures live at `:225`,
`TOOL-dScaffoldedMirror-13 · DEFERRED` — which is also the record §10 correctly names as the one this
unit is the ruling for. The spec disagrees with itself two sections apart, and a reader following the
cite cannot check the numbers.

The line-keyed form is itself a class two records already ratified: `TOOL-aLoosenedCeiling-5` and
`TOOL-dSpentCeiling-6` both record that any insertion above a line-pinned row silently unpins it.

**Fix.** Cite by id — `TOOL-dScaffoldedMirror-13` — and drop the line number.

**Left-shift.** A checker over tracked prose: a `memory/backlog/<FAMILY>.md:NNN` cite is refused
outright in favour of the id, which is stable. Two ratified records already argue for it; nothing
enforces it.

## What this round re-measured, with the commands

Run in this worktree at `693bcf96`. Every figure this record asserts about the tree came from one of
these; nothing is inherited from a finder unread.

- `git ls-files '*.py' | wc -l` = 49 · `'*.js'` = 8 · `'*.sh'` = 94 · `'*.test.sh'` = 49.
- `python tools/lexicon/lexicon.py --check` = `P1 verb graded=1045 offenders=461 waived=0`,
  `P2 suffix graded=41`, `P3 layer graded=557`, `coverage — armed 57 of 141 (40.4%)`,
  `armed but grading nothing ... .js suffix=0`, exit 0.
- `grep -n 'VERB_OFFENDER_PIN' .lexicon.conf` = `164:VERB_OFFENDER_PIN="461"`, so headroom is zero.
- `grep -nE '^[A-Z]+:' .lexicon.conf` = `VERBS:` and `LAYERS:` only. No `CELLS`, no `PINS`.
- A module-body `ast` walk over those 49 files: 544/436/108, 449/430/19, 346/346/0 for the three
  constant readings, with `AnnAssign` targets counted; 406/391/15 and 312/312/0 without them.
- First-dot stemming over the same files: 8 `py.file` snake violations, enumerated in H4.
- `tools/gate-legs.json`, read as JSON: `lexicon naming predicates` (declarations, repo, guard
  `['tools/', 'skills/session-kickoff/', '.githooks/', '.claude/']`, 300); `lexicon selftest`
  (selftests, kit, guard `['tools/lexicon/']`, 880); `lexicon wiring` (wiring, repo, guard `[]`, 330);
  `codebase-map coverage + freshness` (declarations, repo, NO guard, 300); `govkit selfcheck`
  (declarations, repo, NO guard, 310). The leg's name key is at line 956, so unit 6 AC8's `:931`
  cite is stale too.
- `tools/lexicon/lexicon.py`, read directly: the `DEAD PROBE` arm ships with the pattern-set id and
  the `any(ext_of(f) == ext for f in files)` guard, and the `armed but grading nothing (reported, not
  a refusal)` line ships as a report.
- `memory/backlog/TOOL.md` rows at `:214` (`-2` CLOSED), `:215` (`-3` WONTDO), `:222` (`-10` CLOSED),
  `:225` (`-13` DEFERRED), `:341` (`-15` OPEN), `:342` (`-16` OPEN).

One figure I did NOT independently derive and am flagging rather than asserting: the 976/69 split of
`P1 verb graded=1045` into Python and JavaScript definitions. The total is measured; the split is the
specs' own and is consistent with the 41 `py.type` the same run prints.

## Notes on the round

**The dominant class, by a distance, is a criterion that observes nothing.** Nine of the 23 rows are
some form of it: a scope item with no criterion (H3, H5, H10, H12), a criterion satisfied by shipped
code (H7), a criterion true by construction (H11), a criterion whose state the build does not reach
(B1, B4), and a criterion a sibling's landing inverts (H13). One spec-lint arm — every Scope (IN)
item is named by at least one §6 criterion, and every RESOLVED fork too — would have caught six of
them before this round ran. It is the cheapest thing on this page.

**The second class is a figure measured at a base the spec never re-pinned.** Unit 6 is still at
`d0a18683` while its siblings moved to `6c670b02`, and every population number in it is wrong at the
run's base — including three the spec proposes to write into a shipped declaration and gate. Unit 5
re-pinned and re-measured at rev-2 and is clean on this axis, so the build knows how; the gap is that
nothing forces it.

**The third is prior art the reuse audit did not check.** Two specs in this set disagree about
whether `DEAD PROBE` exists in shipped code (H7), one cites a WONTDO as a ruling and omits the CLOSED
row that actually established the shape (H6), one calls a filed OPEN row unfiled (M5), and one cites
a backlog line that holds a different record (M6). All four are lookups against files already in the
tree. The earlier spec-audit round's closing note said to read the `kit.toml` of every kit a unit
touches; the same advice extends to resolving every id a §10 cites and printing its status token.

**What is NOT wrong here, and is worth saying because the count above reads harshly.** The
anti-mirror rule holds in all three specs: unit 5 seeds its six forms from a prescriptive source and
uses the corpus only to decide which spellings become debt, and its "why the set is load-bearing"
section is a measurement against the population rather than a standard read off it. The AMBIGUOUS
fork was ratified against the spec's own recommendation on a population nobody had counted, and the
record of the overturn is exemplary. No row below the blockers challenges a design decision; every
one of them is about what the design says it will observe.
