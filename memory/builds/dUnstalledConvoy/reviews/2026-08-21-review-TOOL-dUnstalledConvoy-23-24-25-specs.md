**Serves:** diff-review TOOL-dUnstalledConvoy-23 TOOL-dUnstalledConvoy-24 TOOL-dUnstalledConvoy-25

# Design review — the re-grounding closed the stale-base class and opened a semantics class in its place

**Reviewed range:** `de766cb3...HEAD` (HEAD = `6fcfe367`, 1 commit, 3 files, spec only). **ROUND: 1.**

## Verdict: BLOCKED

**Five blockers, nine highs, four mediums, one low.** This is the second adversarial pass over these
units; the first returned BLOCKED with 21 defects against `de766cb3` and its report is
`2026-08-21-review-TOOL-dUnstalledConvoy-23-24-specs.md`. This diff is three specs and no code, so
every finding is a design defect: a scope item that cannot be built, an acceptance criterion a wrong
implementation also satisfies, a claim about the base that is false, or a fork resolved on a
mechanism the code contradicts.

**Round 1's headline is fixed.** Spec 23 rev-2 no longer names the re-declaration lookup, the `cur`
selection, the narrowing test or the `curgrp` gate; all four are gone, section 3's false
narrowing-refusal boundary is gone, and spec 24's committed-phase premise is correctly retracted with
`fact()` named as the reason. That class is closed. Verified token by token against `d9728f89`.

**What replaces it is a semantics class.** S1's union is resolved as the fix for a terminal red, and
under S1's own window qualifier plus S2's bound it does not remove that red — it cannot, because a
corrective declaration parks at a NEW anchor whose window opens after the offending commit. The
leg's own comment says so in the opposite direction at `check-unattended.sh:1099-1100`. F1 resolves
the only open fork on that sentence and S8 flips `DISPATCH_GRADING` ON with it as the precondition,
so the flip ships a merge-bar red with no in-band exit into a run with no owner turn — verbatim one
of the two failure modes `memory/backlog/TOOL.md:9` charters this unit to design against.

**And spec 25, the left-shift this review's predecessor asked for, does not survive contact with its
own corpus.** Run as written, S1 reds 151 of 225 based specs on 913 of 2202 slash-bearing tokens,
including spec 23 rev-2 in this same commit; S2's own worked example at `:44` reds spec 25 itself.
The gate written to stop a spec from lying about its base is, at rev-1, a gate that reds the two
specs shipped beside it and misses three of the four defects it cites as its motivation.

## Review shape

- **raw 49 · confirmed 44 · refuted 5 · unverified 0 · precision 0.90.**
- After dedupe the 44 confirmed collapse to **19 distinct defects: 5 BLOCKER, 9 HIGH, 4 MEDIUM, 1
  LOW.** Each section names the raw confirmed ids that reached it. Four lenses reached the
  union-does-not-widen defect independently and four reached the window-boundary defect — the same
  convergence pattern round 1 saw on the stale-base defect, and for the same reason: both are
  reachable from the code without reading the spec's argument.
- Every code claim below was re-verified against `d9728f89` before this report was written: the awk
  fold by piping synthetic rows through it, `pass_commit` and the `sibrows` filter by reading them,
  `DISPATCH_GRADING`'s carriers by `git grep` over the tracked tree, spec 25's S1 predicate by
  running it over all 225 based specs at each spec's own base, and rev-1's token set by extracting it
  from `de766cb3`.
- **Not covered:** the full bar was not re-run; the diff is spec-only and touches no gated artifact.
  That is an assumption, not an observation. No claim below rests on it.

---

# BLOCKERS

## B1 — Union does not deliver the in-band exit it is resolved on, so S8 flips the gate ON over a terminal red

*(raw confirmed ids 1, 14, 38)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:60-63`, resolved on
at `:125-127` (F1) and depended on at `:36-37` (S8).

Section 4 says: "Under union a corrective declaration WIDENS the graded set, which is the in-band
exit." That sentence is false under S1's own qualifier — "rows whose window contains the commit" —
combined with S2's upper bound. The arithmetic:

- `--dispatch` sets the group key to `grp=$(GIT rev-parse --short=8 HEAD)`
  (`tools/unattended/unattended.sh:2318`), so a declaration anchors on whatever HEAD is at the moment
  it is made.
- A corrective declaration is by definition made AFTER the offending commit exists, so HEAD has moved
  and the new row anchors at or after that commit.
- `pass_commit` opens `$_pa..HEAD` (`tools/unattended/lib-unattended.sh:82`), exclusive at the bottom,
  so the new row's window cannot contain the commit that is its own anchor.
- Under S2, windows at distinct anchors are disjoint, so for any given commit the union is a
  singleton and union equals last-wins outside the same-anchor case.

The narrow row's window still holds the offending commit, the subset test still fails, and the leg
still reds. This is not a subtle reading — the leg's own comment states it from the other side:
"a post-hoc widening cannot reuse a closed pass's anchor, it lands under a NEW key here and the
original narrow declaration is still graded" (`tools/unattended/check-unattended.sh:1099-1100`), and
`tools/unattended/check-unattended.test.sh:1464-1472` (arm C) exists to guarantee exactly that.

So union delivers no exit. With S8 flipping `DISPATCH_GRADING` ON, an unattended run that commits one
path outside its lane takes a permanent merge-bar red at the push boundary with no owner turn, and
the only remaining moves are a history rewrite or `--no-verify` — the run bypassing the whole bar.
The single reading of union that WOULD deliver the exit is the one without the window qualifier, and
that reading breaks arm C, which is the retraction section 3 lists OUT.

**Fix.** Strike the sentence at `:62` and re-open F1. Union's real and sufficient justification is
the one at `:54-58` — the fold silently discards a declaration the driver's published repair told the
run to make. Say that the in-band exit exists only BEFORE the pass commits (declare again, then
commit), state plainly in sections 4 and 5 that a committed out-of-lane write is TERMINAL, and make
S8's flip conditional on that being an accepted cost with a named owner-facing recovery. Add an
acceptance criterion that DRIVES an escape end to end — red the leg, take the escape, assert green —
rather than asserting one.

**Left-shift gate.** A leg self-test arm that is a CLEARANCE arm, not a verdict arm: for every
refusal check 23 can emit, a fixture that reaches the refusal and then performs the documented
recovery, asserting rc goes 1 to 0. A refusal with no green-after arm is a refusal nobody has proven
is clearable, and this build has now shipped two of those.

## B2 — S2 states no window boundary and AC4 states it exclusively, which turns arm C from RED to green

*(raw confirmed ids 2, 13, 27, 42)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:23` (S2) and `:98`
(AC4).

S2 says a row's window is "bounded above by the next anchor" and never says whether that endpoint is
included. AC4 then spells the exclusive reading outright: "graded only against commits before that
anchor". The two readings differ by exactly the retraction `e42cb5a` was written to end.

Traced against arm C (`tools/unattended/check-unattended.test.sh:1464-1472`), whose fixture is: `drow`
narrow at A0, the offending commit C1 touching `work/stray.txt`, then `drow` wide whose anchor IS C1
because `drow` stamps `git rev-parse --short=8 HEAD` at call time.

- **Inclusive** `A0..C1`: C1 is inside row 1's window, the declared set is `{work/one.txt}`,
  `work/stray.txt` is outside, the leg REDS, arm C passes.
- **Exclusive** (AC4's wording): row 1's window holds only the declaration commit, which `pass_commit`
  skips because it touches nothing but the run-state file (`lib-unattended.sh:84-85`); row 2's window
  is `C1..HEAD`, which excludes C1. C1 is inside NO row's window, both rows fall to the silent
  `report` branch, and arm C goes rc=1 to rc=0.

That is the post-hoc-rewrite defence — the one the widening branch was deleted to secure — disarmed
by a boundary word, with S8 flipping the gate ON over it. Arm C is named nowhere in the spec and
section 3's OUT list does not protect it, so a builder whose only signal is a newly red arm C is
invited to edit the arm.

This is round 1's D6 wholly unaddressed, and an oversight rather than an accepted omission: no OUT
entry mentions the boundary and no OUT entry mentions arm C. D6's second half — an ordering rule for
`next` when two anchors are not ancestors of one another — is also still absent, and an unordered
pair currently yields an empty window rather than a named report.

**Fix.** Write both rules into S2: the window is `<this anchor>..<next anchor>` in git's own sense,
INCLUSIVE of the next anchor's commit, so a commit that is itself an anchor is graded by the row it
closes; and `next` is the next anchor that is a DESCENDANT of this one, with a named report — never
an empty window — when the pair is unordered. Restate AC4 as "graded against commits up to and
including the later anchor". Add arm C at `check-unattended.test.sh:1464-1472` to section 3 as a
do-not-undo pin, and add an acceptance criterion asserting it stays RED after S1 through S3.

**Left-shift gate.** A pinned-arm registry: a tracked list of leg arms that encode a retracted design
(arm C, the narrowing-absence arm at `unattended.test.sh:2721-2727`), with a gate asserting each
still exists and still asserts the same direction. An arm that encodes a retraction is currently
protected by nothing but whoever remembers it.

## B3 — Spec 25's S1 path predicate is undefined and, run as written, reds 151 of 225 specs including spec 23 rev-2

*(raw confirmed ids 3, 19, 39)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-25.md:15-17`, certified by
AC6 at `:87` and AC8 at `:91`.

I ran the predicate as specified — backticked slash-bearing tokens from sections 2 and 4,
`git cat-file -e <base>:<token>` — over every tracked spec with a resolvable base:

    specs-with-resolvable-base=225   slash-tokens=2202   unresolved=913   specs-redding=151

Spec 23 rev-2, shipped in this same commit, reds three times at its own base `d9728f89`:
`unattended.sh` (bare-filename shorthand, `:30`), `work/a` and `work/b` (illustrative fixture lanes,
`:57`), plus the `/.` and `/./` path fragments at `:27`. All verified ABSENT with `git cat-file -e`.
None of them is the defect the check exists to catch.

Four false-positive classes the spec never mentions, each reproduced:

- **`path:line` citations** — `memory/guides/UNATTENDED-PROTOCOL.md:110`, ubiquitous in this corpus.
- **Globs and brace forms** — `builds/*/spec/`, `tools/**/*.js`, `tools/workflows/drift-audit-{code,state}.js`.
- **Placeholders and prose fragments** — `{{MEMORY_ROOT}}/...`, `<gitdir>/gate-logs/<leg>.log`,
  `ceil(N/5)`, `N/A*`.
- **Files the unit CREATES** — decisive, because it is not editorial. A spec whose Scope adds files
  reds on its own scope at its own base by construction; `2026-08-03-spec-aBatchedLintel-1.md` and
  `2026-08-09-spec-aBatchedTribunal-1.md` both do.

So AC6 ("run over the real corpus at its own base the check is green") and AC8 (full bar green) cannot
both hold, and the cutoff does not rescue it: the next spec that adds a file reds on its own scope,
so the check either blocks ordinary specs or is waived into vacuity. F1 at `:99-103` claims the
candidate predicate "is run over the real corpus and its hits AND near-misses printed before it is
wired" — the charter §7 rule — and the measurement above shows that plainly has not happened.

**Fix.** Do what F1 promises, before writing any AC. Then define the population by construction
rather than by shape: strip a `:<line>` or `:<a>-<b>` suffix; exclude any token carrying a glob
metacharacter or a brace or angle bracket; require the token to be rooted at a top-level directory
tracked at that base; declare an exclusion for illustrative fixture prefixes and for bare-filename
shorthand; and exclude paths the spec's own Scope declares it creates. Put the measured hit count in
the spec and restate AC6 as that measured count, not as "green".

**Left-shift gate.** Make the corpus dry-run an artifact, not a promise: the unit lands a committed
`*-red-first.md` carrying the predicate's hit AND near-miss counts over the tracked corpus, and a
hygiene check asserts that any spec introducing a new corpus-wide predicate carries one. The charter
already mandates the practice; nothing currently observes that it happened.

## B4 — Spec 25's own Design section violates spec 25's check, so the rule's first use must be a waiver

*(raw confirmed ids 18, 28-part)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-25.md:43-44`.

S2's population is "identifiers matching a shell-name shape that the spec ALSO co-names with a file".
Line 44 is the textbook instance of it: `` `curgrp` `` written beside
`tools/unattended/unattended.sh` as the worked example. Measured at spec 25's own pinned base:

    git show d9728f89:tools/unattended/unattended.sh | grep -c curgrp   ->   0

So the check reds the spec that defines it. AC3 ("a spec naming only present paths and identifiers
PASSES, so the check is not vacuously strict") and AC6 ("run over the real corpus at its own base the
check is green") cannot both hold, and the only way to land the unit is a grandfather entry for its
own spec — which makes the first use of the rule a waiver. Pushing the cutoff past it is not the
escape either: section 5's rollback bullet at `:70-71` is "set the cutoff forward and the check
measures nothing", and the reuse audit at `:115` wires `pop_guard`, which reds an empty population
whenever the precondition is non-zero (`tools/memory-tree/check-memory-hygiene.sh:177-183`, with
`PRE_SPEC` at `:187`).

**Fix.** Restrict the population to the Scope section only (S2 currently says Scope OR Design; drop
Design), or define an explicit escape for a token the spec marks as deliberately absent — which is
the normal content of a spec explaining what it deleted. Add a fixture for a spec that quotes a
deliberately-absent identifier and assert it PASSES.

**Left-shift gate.** Self-application as a landing condition: any new spec-content check must be run
against its own spec and against the specs beside it in the same commit before it is wired, with the
result recorded. A check whose first act is to grandfather its own author is not a check.

## B5 — AC6's motivating claim is measured false in both directions

*(raw confirmed ids 40, 28-part, and the reverse half of 5 and 20)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-25.md:87-89` (AC6), leaned
on by F1 at `:99-103`.

AC6 asserts that rev-1 of spec 23 "restored into a fixture REDS on all four of its dead identifiers".
I extracted rev-1's sections 2 and 4 from `de766cb3`. Every backticked token, complete:

    /./   DISPATCH_GRADING   anchor..HEAD   cur   curgrp != grp
    lib-unattended.sh   normpath   pass_commit   sibrows   tail -1

The only file those sections name is a bare `lib-unattended.sh`. Against the four "dead items" AC6
cites:

- **"the re-declaration lookup"** and **"the narrowing test"** are plain prose, never backticked. S2's
  predicate cannot see them — and they are the two that made rev-1's S2 and S5-item-1 unbuildable.
- **`cur`** is not shell-name-dead: it has 25 word-matches in `tools/unattended/unattended.sh` at
  base, including a live local in `verb_landed` at `:1319-1324`. A presence test cannot tell dead
  from live; it can only tell absent from present.
- **`curgrp`** appears only inside the multi-token span `` `curgrp != grp` ``, which contains a space
  and an operator. S2 never says the check tokenizes INSIDE a backticked span, so under S2 as written
  it is not a candidate at all.

In the other direction the predicate produces a false positive on the same spec: `sibrows` is a live
driver variable (`tools/unattended/unattended.sh:2331`, 4 matches) and has 0 matches in
`lib-unattended.sh`, so it reds. `DISPATCH_GRADING` reds for the same reason. And if a bare
`lib-unattended.sh` does not resolve as a co-named file at all, rev-1's population is EMPTY and the
check reds on none of the four while reporting green.

So the gate written to prevent this blocker would have let the blocker through while accusing two
correct tokens — the "predicate that never matched its target population" class the charter §7 books
by name. AC6 is the only criterion binding this unit to the defect it exists for.

**Fix.** Build the rev-1 fixture FIRST, run the candidate predicate against it, and write the number
measurement actually produces into AC6 and into F1 — naming which of the four it cannot reach, in
S4's not-checked header. Then decide on that basis whether S2 earns its place, or ship S1 alone with
the corrected population from B3. If S2 stays, widen the search target beyond the co-named file (the
spec's kit directory), because document-scope co-naming is what produces both the miss and the false
positive.

**Left-shift gate.** For any check justified by a historical defect, require the historical artifact
as a committed fixture and an arm asserting the check reds on it. "It would have caught X" is an
assertion about nothing until X is in the suite.

---

# HIGH

## H1 — Union proves "declared before COMMIT", never "declared before WRITE", and AC1 pins the laundering case GREEN

*(raw confirmed ids 4, 30)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:76` (security
bullet), `:91` (AC1), `:36` (S8's precondition).

Section 5 claims union "restores catching a run that is WRONG". What union actually does is make a
declaration retroactive right up to the moment of commit. Two `--dispatch` calls at an unmoved HEAD
park two rows under one key (`unattended.sh:2318`; a unit's own rows are skipped by condition 1 at
`:2380-2392`), so a pass that has ALREADY written outside its lane and not yet committed can declare
the path it wrote and the union covers it — green. `check-unattended.test.sh:1449-1454` (arm A)
already blesses that row shape and cannot see when the write happened, because the laundering sequence
and the sanctioned repair produce a byte-identical file and commit state.

Round 1's D4 asked for the negative control explicitly: declare narrow, write out of lane WITHOUT
committing, re-declare wide at the SAME anchor, commit, assert the leg still REDS. Rev-2's AC1 pins
that shape GREEN — the opposite verdict — and section 5 records security as "unchanged" while S8
flips the gate on with "the two-rows-at-one-anchor case is closed" as its precondition.

Two further points make S8's precondition circular. First, it is satisfied by S1 itself: a guard
reading the same state as the change it guards. Second, section 4's motivating sentence is wrong
about which shape the driver's published repair produces — `--dispatch` stages the run-state file and
the run commits it (`lib-unattended.sh:71-74`), and both existing fixtures do exactly that between
two declarations (`cross-component.test.sh:107-118`, `unattended.test.sh:2710-2716`), so the ordinary
repair lands at DIFFERENT anchors, which the fold already keeps. Union's only reach is the
same-anchor case, which arises only when a run declares twice without committing — which is D4's hole
precisely. Union does not close it; it makes it the intended semantics.

This is not a regression — last-wins at base blesses the same sequence — but the flip's claimed value
is overstated, and the boundary D4 forced was decided silently.

**Fix.** Separate the two directions in section 4: the ordinary commit-between repair is already
correctly folded, union reaches only same-anchor rows, and a same-anchor re-declaration therefore
widens the graded set RETROACTIVELY. Then either accept that in section 3 with the reason, or require
each graded row to be present in the run-state file as of the pass commit's first parent and say so
in S1. Either way, add the D4 negative control beside AC1 in the same fixture, asserting whichever
verdict the design chooses.

**Left-shift gate.** A "what does this prove" line in every check's header, machine-compared against
what its arms actually pin. Check 23's header would have to say "declaration before commit, not
before write" — and a header that says so cannot be misread as a disjointness proof by the next
reader.

## H2 — S2's "co-named with a file" is undefined, and both readings misfire on the real corpus

*(raw confirmed ids 5, 29)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-25.md:19-20` and `:43-44`.

"Co-names" is never scoped — same bullet, same paragraph, same section, or same document. It is not a
pedantic gap; the readings disagree on the very spec that motivated the rule.

**Narrow (nearest file / same bullet).** Spec 23 rev-2's Scope and Design name exactly one resolvable
path, `tools/unattended/check-unattended.sh`. In that file at base, `normpath` has 0 matches and
`sibrows` has 0 — yet both are live (`lib-unattended.sh:38`, `unattended.sh:2331`). The narrow
reading reds two correct tokens on the spec this check protects.

**Wide (any file the spec names anywhere).** This is what lets `cur` through, and it is contradicted
by the spec's own worked example: `:44` asserts that a bare `` `union` `` "is not a candidate at
all", but `union` sits in section 4 one sentence from `tools/unattended/unattended.sh`, where `union`
has 0 matches.

**Fix.** Pin the co-naming scope to one syntactic unit — the same bullet is the only reading that is
not a spelling test — and state it once in S1, with S2 referring to it. Then either widen the search
target to every tracked file in the spec's kit directory, or require the spec to name the file
repo-root-relative beside the identifier and red only when its own bullet names a resolvable file.
Print near-misses over the whole corpus before wiring, and record which reading was chosen in S4's
header.

**Left-shift gate.** A gate whose population is stated in prose must carry the population's measured
SIZE in the same commit. A predicate with an unstated scope is a predicate nobody has counted, and
this repo already reds for a check "satisfied by its own comment prose".

## H3 — Spec 24's feasibility claim for AC2 is false about the base: no unattended fixture builds a linked worktree

*(raw confirmed ids 6, 21, 35, 41)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-24.md:73-74`.

The testing/gates bullet says the cross-tree arm "needs a second worktree in the fixture, which
`adopt-unattended.test.sh` already demonstrates is buildable". Measured at base:

    git show d9728f89:tools/unattended/adopt-unattended.test.sh | grep -ci worktree   ->   0

What that file builds is independent REPOSITORIES with `git init` (`:25-27`, `:104`). Two independent
repos do not share a worktree list, so `git worktree list --porcelain` in one never enumerates the
other — the cited precedent does not demonstrate what the bullet claims. Repo-wide, the only
`git worktree add` in any test is `tools/memory-recall/recall-opened.test.sh`; nothing in the
unattended kit creates a linked worktree at all.

AC2 at `:82` is the only criterion that observes S2, which is this unit's main new behaviour, and its
buildability rests on a demonstration that does not exist. The sentence is also NEW in rev-2 — rev-1
carried no such claim — so it is a fresh unverified assertion about the corpus, in exactly the class
the re-grounding pass existed to eliminate, in the one section (5) that spec 25's own declared
population cannot reach.

The consequence is milder than the class: a builder can `git worktree add` easily enough, and a
two-repo substitution would fail AC2 loudly rather than pass silently. The defect is the false
grounding claim, not infeasibility.

**Fix.** Replace the claim with the real one: no unattended fixture creates a linked worktree,
`tools/memory-recall/recall-opened.test.sh` is the only in-repo precedent, and AC2 costs a new
`git worktree add` helper plus teardown in `unattended.test.sh`. Add an assertion inside AC2's own
fixture that `git worktree list --porcelain` emits two `worktree ` lines, so a two-repo substitution
cannot pass. If a linked-worktree fixture turns out not to be affordable, scope S2 out rather than
pinning it to a criterion nothing can drive.

**Left-shift gate.** This is B4's gate one level up and it is the same rule: a spec's factual claims
about the base belong in the checked population. Spec 25's non-goals currently exclude section 5,
which is where both of this diff's false base claims live. Extend the population to section 5's
backticked tokens, or accept in writing that the gate cannot see the section where feasibility is
argued.

## H4 — Spec 23's AC3 is already green at base, is the wrong measurement for union, and contradicts AC11

*(raw confirmed ids 9, 15, 31)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:95-97`.

The fold key is the item field `<group> <unit>` and the group IS the anchor (`unattended.sh:2318`),
so "one row per `(group, unit)` per distinct anchor" is a restatement of the base behaviour.
Reproduced by piping three synthetic rows through the awk at `check-unattended.sh:1121-1125`:

    in:  AAAA U1 work/a  |  AAAA U1 work/b  |  BBBB U1 work/c
    out: AAAA U1 work/b  |  BBBB U1 work/c

Distinct-anchor rows both survive today, discarding none. AC3's named fixture — "a unit with rows at
two anchors" — is therefore green against the pre-fix code with `row[k] = $0` untouched, so it cannot
appear in AC11's red-first ledger, which at `:114` states without qualification that every arm added
by this unit was observed RED. That is round 1's D17 moved to a new criterion.

Worse, the criterion is self-contradictory on the case that matters. The only case union changes is
two rows at ONE anchor, and there a correct union fold emits ONE row carrying the merged set while
the file holds two — so AC3's row-count equality fails on the right implementation.

**Fix.** Delete the row-count probe and re-aim AC3 at the property union asserts: for a unit with two
rows at ONE anchor, the set the leg grades equals the union of both rows' reason fields, observed by a
commit touching a path present only in the FIRST row and asserted GREEN — which is RED at base — with
AC2 as its control. Move the two-anchor behaviour to section 3 as already-held. And say in S1 whether
union merges the rows or unions at the subset test, because the two differ in how many times the
no-commit branch runs (see H8).

**Left-shift gate.** Make AC11's red-first ledger machine-checkable: the committed `*-red-first.md`
names one staged break per new arm, and a gate asserts every arm the unit adds appears in it. An
already-green criterion cannot produce a ledger row, so the ledger becomes the detector.

## H5 — No acceptance criterion observes S8's flip; AC9's two arms already exist and are green at base

*(raw confirmed ids 10, 16, 34)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:108-110` (AC9),
leaned on by F2 at `:129-131`.

`check-unattended.sh:1115` is `[ -z "${DISPATCH_GRADING:-}" ]`, so blank-is-dark and set-is-graded are
today's behaviour, and the fixture already covers both: `check-unattended.test.sh:79` hard-codes
`DISPATCH_GRADING=1` in its own generated conf, and `:1602` and `:1610` strip the key with `sed -i`
for the dark arms. Neither arm reads the repo's shipped conf.

What S8 actually changes is the shipped default value in `.unattended.conf:144` and
`tools/unattended/.unattended.conf.example:125`, both `DISPATCH_GRADING=""` at base — and no criterion
in AC1 through AC12 observes either file. So the whole AC set passes whether S8 lands, is botched, or
is skipped, while F2 leans on AC9 by name to call the flip reversible. Round 1's D20 unaddressed: the
observation sites moved, the gap did not close.

Section 5 at `:83-84` compounds it. An adopter whose conf was rendered before the flip keeps
`DISPATCH_GRADING=""` and stays silently DARK while the rendered protocol says the grading is on. The
spec never states that. Note also that the existing arms test UNSET, not blank, so the rollback value
section 5 promises is not the one exercised.

**Fix.** Add a criterion over the shipped artifacts: both conf files carry a non-blank
`DISPATCH_GRADING` after S8, and a fixture inheriting the shipped conf
(`cross-component.test.sh:49-51` copies it) actually grades. Keep AC9's pair as a behavioural control,
not a red-first arm, and add the blank-as-distinct-from-unset third state. State in section 5 what a
pre-flip adopter conf gets.

**Left-shift gate.** A conf-default parity leg: for every key `kit.toml` declares, assert the shipped
`.unattended.conf` and `.unattended.conf.example` agree with each other and with what the rendered
protocol table says the default is. Today the value, the example and the prose are three copies that
can drift independently, and S8 is about to move one of them.

## H6 — The driver-side never-closing row is neither IN nor OUT, and it is the exact terminal stall this build exists to remove

*(raw confirmed ids 17, 32, 45)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:146-148` (reuse audit
dropping rev-1's helper); the class appears in neither section 2 nor section 3.

The wedge is live at base and reproduces by reading the code:

- `pass_commit` returns only the FIRST commit after the anchor that names the unit and touches
  anything besides the run-state file (`lib-unattended.sh:79-89`).
- The `sibrows` openness filter tests only THAT commit's diff against the row's declared set and keeps
  the row OPEN when it misses (`unattended.sh:2337-2351`). A later commit that did intersect is never
  examined.
- `sibrows` greps every dispatch row in the file with no group filter, deliberately (`:2320-2327`), so
  condition 1 at `:2380-2391` then refuses every other unit declaring an overlapping path with
  `fail 49 ... also in <who>` — permanently, on an append-only record with no retraction.

Concrete: unit A declares `work/one` at A0, later declares `work/one work/two`, then commits only
`work/two/y.txt` with a subject naming A. Row 1 is printed OPEN forever, and unit B declaring
`work/one` is refused for the rest of the run. Terminal with no owner turn — the failure mode
`memory/backlog/TOOL.md:9` names as a thing to design against.

Round 4's D5 and round 1's D2 both asked for a SECOND, driver-only helper precisely because the two
callers want different answers. Rev-2's reuse audit deletes the helper on the ground that "its two
callers wanted different answers", which is the argument FOR splitting it. Dropping the helper is
defensible; leaving the defect unclassified is not — section 3's OUT list covers condition 1's
REFUSALS and `pass_commit`'s permissiveness, but not the openness computation that feeds them. AC12's
green bar passes over it while S8 turns the grading on above it.

**Fix.** Either add a driver-only `pass_commit_in_set <anchor> <unit> <rel> <declared...>`
(scan-forward, set-filtered) with its own acceptance criteria, leaving `pass_commit` untouched — or
list the never-closing row in section 3 with the reason and the unit that owns it. If it goes IN,
carry round 4's two arms: the `git add -A` declaration commit with one extra tracked file, and
widen-then-write-only-the-new-lane, each asserting a later sibling declaration is ADMITTED, each
beside its control.

**Left-shift gate.** A defect-disposition ledger per unit: every finding a prior round confirmed is
listed in the successor spec as IN, OUT-with-reason, or DEFERRED-to-a-named-unit, and a hygiene check
asserts no confirmed finding from a linked review is unlisted. Three rounds have now lost this class
between revisions, each time by silence rather than by decision.

## H7 — AC1 and AC2 are satisfied by existing green arms, because `drows`' two rows are NESTED

*(raw confirmed id 22)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:91-94`.

`drows` at `check-unattended.test.sh:1442-1447` parks both rows at one anchor, and every caller passes
a nested pair: arm A (`:1449-1454`) and arm B (`:1456-1462`) both use `work/one.txt` then
`work/one.txt work/two.txt`. Row 2 is a superset, so under the BASE last-wins fold the surviving row
already IS the union. Arm A is green at base and arm B reds at base, which is exactly what AC1 and AC2
ask for. An implementation that changes nothing satisfies both, and neither can appear in AC11's
red-first ledger.

The only shape that distinguishes union from last-wins is a NON-nested pair — which is section 4's own
example at `:56-57`, `work/a` then `work/b`.

**Fix.** Require non-nested declared sets in both criteria: row 1 `work/a`, row 2 `work/b`, with a
commit touching both (AC1, RED at base) and a commit touching `work/c` (AC2, its control). Say
explicitly that the existing `drows` fixture cannot serve them.

**Left-shift gate.** Same as H4's: the red-first ledger, machine-asserted against the arms the unit
adds. Every defect in this cluster is the same shape — a criterion whose fixture cannot fail — and one
gate catches all of them.

## H8 — Union silently widens the no-commit branch's path probe, creating a NEW unclearable red

*(raw confirmed id 44)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:18` (S1) and `:25-26`
(S3).

S1 defines the graded set relative to "the commit", but the fold it changes feeds two consumers. The
second is the no-commit branch at `check-unattended.sh:1153-1169`, which runs when there IS no commit
and probes every path in `$dsdecl` over `"$dsgrp"..HEAD` for ANY commit by ANY author.

Merging two same-anchor rows enlarges `$dsdecl`, so a path that last-wins discarded is now probed.
The driver explicitly permits a narrowing re-declaration (`unattended.sh:2422-2423`: "There is no
narrowing refusal"), and under union that narrowing can no longer take effect — the abandoned path
stays in the unit's lane, and any unrelated commit touching it fires
`fail 23 ... a declared path of a dispatched pass moved after the group anchor while no commit names
that pass`. S3 bounds that window's upper END and says nothing about its PATH SET.

S1's commit-relative wording gives this branch no rule at all, and the branch is where a red is
hardest to clear: nothing un-declares a row, and the run has not committed under its own id.

**Fix.** State in S1 which set the no-commit branch uses — the merged set or the individual rows — and
why. If merged, add an arm for the shape above asserting the intended verdict. If per-row, say so
explicitly, because a single fold cannot serve both without the branch reading rows rather than the
folded key.

**Left-shift gate.** A consumer census in the spec of any change to a shared derivation: name every
reader of the value being changed, with a line each on what the change does to it. The fold has two
readers and the spec discusses one — mechanically detectable by grepping for the variable the scope
item names.

## H9 — S6 and AC8 leave the same orphaned widening prose live in the leg and its suite, where S1 makes it contradict the code beneath it

*(raw confirmed id 43)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:30-32` (S6) and
`:106` (AC8).

S6's rationale at `:69-72` is exactly right — a comment describing deleted behaviour, sitting above
the code that deleted it, is where rev-1 got its mental model. It then names one file.

Two more carriers of the identical prose, verified at base:

- `tools/unattended/check-unattended.sh:1090-1101` — "ONE ROW PER (group, unit) — THE LAST. The
  driver's widening repair supersedes an OPEN pass's row and parks the replacement AT THE SAME
  ANCHOR ... the later one is the one that binds."
- `tools/unattended/check-unattended.test.sh:1436-1441` — the same widening story above `drows`.

The driver's widening machinery is gone (`unattended.sh:2409-2423` says so in capitals), so both
describe deleted behaviour today. After S1 the first is worse than stale: "THE LAST … the later one
is the one that binds" would sit directly above a UNION fold — a comment contradicting the code
beneath it, which is the defect S6 exists to remove. AC8's grep is scoped to
`tools/unattended/unattended.sh` plus the library header and cannot see either.

**Fix.** Extend S6 to `check-unattended.sh:1090-1101` and `check-unattended.test.sh:1436-1441`, and
extend AC8's grep to the whole `tools/unattended/` tree for `widening repair`, `SUPERSEDES`,
`the later one is the one that binds` and `RE-DECLARATION RULE`.

**Left-shift gate.** A retired-vocabulary gate: a tracked list of phrases naming deleted mechanisms,
with a leg asserting none appears in the kit. It is one grep, it is exactly the shape of AC8, and
scoping it to the class rather than the instance is charter §7's "gate the CLASS, not the instance".

---

# MEDIUM

## M1 — Spec 24's AC3 pins the vacuous negative, leaving the false-positive direction unarmed

*(raw confirmed ids 7, 48)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-24.md:84-85` (AC3),
glossed at `:70-71`.

Section 5 enumerates three fall-back states and says "S3's negative arm pins the first" — the case
where there are no other worktrees at all. In that fixture `git worktree list --porcelain` returns one
entry, the enumeration finds nothing, and today's message is printed by the fixed and unfixed driver
alike. A fixture that passes by finding nothing.

The discriminating negative is absent from the enumeration and from every criterion: a second worktree
PRESENT, its run-state file for this slug readable, and its phase NOT `LANDING`. An implementation
that enumerates and names that tree as though it held the stranded `LANDING` satisfies AC1 through
AC4 — and an unattended run acting on that message commits a phase that was never evaluated in that
tree. That is precisely what section 4 at `:56-58` says S3 exists to prevent: "replaced one misleading
answer with another".

**Fix.** Re-aim AC3 at "a second worktree exists, its run-state file for this slug is NOT at
`LANDING`, and the refusal is today's message verbatim", inside AC2's own two-worktree fixture so the
presence and absence arms differ by one recorded phase and nothing else. Keep the zero-other-trees
case as a third arm, but stop calling it the negative control.

**Mechanics note, since the brief asked.** `git worktree list --porcelain` does supply what S2 needs —
absolute `worktree <path>` lines, verified in this tree — and `runmd_of` yields the relative tail
`memory/builds/<slug>/RUN.md` (`unattended.sh:239`) while `fact` takes a file path
(`unattended.sh:246-256`), so the composition works. One caveat the spec does not mention: `M` is
`MEMORY_ROOT` read from THIS tree's conf (`unattended.sh:82,90`), so a foreign worktree that declares
a different `MEMORY_ROOT` is missed silently. That belongs in the error-states bullet as a fourth
fall-back.

**Left-shift gate.** A message-arm rule for any refusal that gains a conditional clause: the suite
carries both a clause-present and a clause-absent arm over the SAME fixture, differing by one input.
A negative arm built from a different fixture cannot prove the discriminator works.

## M2 — The docs item names three carriers, misses the manifest every session front-loads, and cites one carrier that does not exist

*(raw confirmed ids 11, 24, 33, 47)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:85-87`.

Grepped the tracked tree at base. The "grading is dark" claim lives at:

- `.unattended.conf:132,144` and `tools/unattended/.unattended.conf.example:113,125` — named.
- `tools/unattended/PROTOCOL.template.md:387` — named. Its installed twin
  `memory/guides/UNATTENDED-PROTOCOL.md:387` cannot drift silently: check 10 at
  `check-unattended.sh:642-657` byte-diffs the pair, so updating the template forces it.
- `memory/guides/SESSION-KICKOFF.md:55-58` — **not named, gated by nothing.** It states the grading
  "ships DARK behind `DISPATCH_GRADING`" and ends "do not treat a green leg as a disjointness proof".
  This is the manifest every session front-loads. After S8 it tells a run that check 23 is inert, so
  the run declares late or loosely and takes a merge-bar red it was told could not happen.
- `tools/unattended/check-unattended.sh:1117` — the leg's own DARK report text, asserted verbatim by
  `check-unattended.test.sh:1605-1606` and stale the moment this unit ships.
- `tools/unattended/kit.toml:38` lists the key; `memory/backlog/TOOL.md:9` is ordinary close-the-row
  bookkeeping.

The item also names a carrier that does not exist: "the driver's own rationale block".
`DISPATCH_GRADING` has **zero** occurrences in `tools/unattended/unattended.sh`. The rationale block
and the DARK text are in the LEG.

Separately, `PROTOCOL.template.md:354-361` and its installed twin still say a re-declaration of an open
pass "widens or no-ops; it never narrows" and that a partly-overlapping set "is read as a narrowing and
refused". Both are false since `e42cb5a`, and under S8 that paragraph tells a run to declare only the
NEW paths — which at a new anchor under S1 plus S2 is precisely what reds check 23. It is in neither
scope nor non-goals.

**Fix.** Enumerate the carriers by path in the docs item: both confs, `kit.toml`,
`PROTOCOL.template.md` (the installed twin follows by check 10), `memory/guides/SESSION-KICKOFF.md`,
and the leg's rationale block plus DARK report text. Replace "the driver's own rationale block" with
the leg's. Add the stale widening/narrowing paragraph and replace it with what is true: append-only
rows, the union rule, and what a pass does when it needs more paths.

**Left-shift gate.** The criterion round 1 already named and rev-2 still lacks: one grep over
`git ls-files` asserting no tracked file claims the grading is dark once S8 lands. Cheap, exact, and
it is the only thing that makes the carrier enumeration verifiable rather than a list someone wrote
from memory.

## M3 — `pop_guard` does not reach S2's real vacuity mode: a spec naming no file gets zero coverage and reports green

*(raw confirmed id 37)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-25.md:115`.

`pop_guard` (`check-memory-hygiene.sh:177-183`) fires when a check's file-level POPULATION is zero
while its un-segmented PRECONDITION is non-zero — a mis-segmented selector. It has no notion of a
matched file contributing zero TOKENS, so it cannot reach S2's actual failure mode. The reuse audit's
claim is accurate about an empty selector and beside the point about an empty token set.

The live instance is in this same commit. Spec 24 rev-2's sections 2 and 4 backtick only `--close`,
`<path>`, `BUILDING`, `LANDING` and `git worktree list --porcelain` — no file path at all — so under
S2's co-naming rule its identifier population is EMPTY and the check is silent over it while the row
reads green. Note that `BUILDING` and `LANDING` are shell-variable-shaped and become candidates the
moment any file is named, so coverage of that spec swings on an unrelated editorial choice.

**Fix.** Report per-spec coverage rather than a repo-level verdict: for each in-population spec, name
how many path tokens and identifier tokens were checked, and treat zero-of-both as an announced SKIP
for that spec — the same shape S1 already gives an unresolvable base. Say it in S4's header so a
green row is never misread as coverage.

**Left-shift gate.** Extend `pop_guard`'s idiom from selectors to tokens: any check that walks a
population and derives a per-item token set announces the count of items that yielded zero tokens.
This leg has redded twice for a skip that looks like a pass, and this is the third shape of it.

## M4 — Spec 25 states its own population two different ways

*(raw confirmed ids 25, 36)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-25.md:15` and `:19` say
"Scope or Design sections" (2 and 4); the first non-goal at `:28-29` excludes "any section other than
2 and 3 and 4", which puts Non-goals INSIDE the population.

It changes real verdicts. Spec 23 rev-2's section 3 backticks exactly `e42cb5a`, `normpath` and
`pass_commit`. Under the wide reading `e42cb5a` is shell-name-shaped and becomes an identifier
candidate that exists in no named file. A builder implementing S1 and S2 literally and a reviewer
reading the non-goal will disagree about coverage, and S4's not-checked header — the artifact meant to
keep a green row honest — gets written from whichever half the builder read.

This is the two-answers-to-one-question shape in the spec whose entire purpose is to stop a document
from disagreeing with the code.

**Fix.** Pick one, state it once in S1, and have S2 and the non-goal refer to it rather than restate
it. If Non-goals is IN, say what an OUT bullet naming deleted machinery is supposed to do, since
naming code that no longer exists is that section's normal content.

**Left-shift gate.** Nothing new is needed — this is charter §6's "a value stated in prose beside the
source that OWNS it rots" applied within one document. The mechanical form is the spec-review habit of
grepping a spec for its own population statement and asserting one occurrence.

---

# LOW

## L1 — AC8's named observation exits non-zero on the outcome it asserts

*(raw confirmed id 49)*

`memory/builds/dUnstalledConvoy/spec/2026-08-21-spec-TOOL-dUnstalledConvoy-23.md:106-107`.

AC8 asserts `grep -c 'RE-DECLARATION RULE' tools/unattended/unattended.sh` returns 0. Verified in this
tree: `grep -c` on a non-matching pattern prints `0` and exits rc=1. The criterion's success case
therefore fails any `&&` chain an arm wires it into — charter §14's booked class, "a PASSING zero-count
check reads as failure". The builder either sees a false red or defuses it with `|| true`, which makes
the assertion unable to fail in either direction.

**Fix.** State the observation as `! grep -q 'RE-DECLARATION RULE' <file>`, so the exit code and the
verdict agree.

**Left-shift gate.** A shell-idiom scan over acceptance criteria and gate scripts for `grep -c` used
as a predicate. The class is already documented in the charter and has no automated detector.

---

# Round 1's 21 defects: disposition

Every row verified against rev-2 rather than taken from the revision log.

| Round 1 | Substance | Status in this diff |
|---|---|---|
| D1 | spec 23 names code its base deleted | **CLOSED.** All four dead references gone; spec 25 is the left-shift, which is itself blocked (B3–B5) |
| D2 | one helper, two callers with different correct answers | **UNADDRESSED — oversight.** Helper dropped, defect unclassified (H6) |
| D3 | graded set undefined when a unit has several rows | **CLOSED in form** by S1; the union's justification is broken (B1) |
| D4 | flip ships over a same-anchor supersession hole | **UNADDRESSED — inverted.** AC1 now pins that case GREEN (H1) |
| D5 | spec 24's S1 reads the wrong source | **CLOSED.** Staged-blob read is OUT with the correct reason |
| D6 | window has no boundary rule and no ordering rule | **UNADDRESSED — oversight.** Neither rule stated; AC4 states the wrong one (B2) |
| D7 | second window runs to HEAD | **CLOSED** by S3 and AC5 |
| D8 | the bounded-window claim was unsupported | **CLOSED.** Section 4 no longer makes it |
| D9 | round 4's D5 second half dropped, no AC | **UNADDRESSED — oversight** (H6, same class as D2) |
| D10 | AC3 not observable, no positive control | **RECURS** in a new spelling (H4) |
| D11 | a new refusal armed, its in-band exit not | **RECURS** as the missing clearance arm (B1) |
| D12 | the rollback F1 leaned on did not exist | **PARTIALLY CLOSED.** AC9 now asserts a rollback but cannot observe the flip (H5) |
| D13 | spec 24's `--abort` parity has no refusal site | **CLOSED.** OUT with `refuse_if_terminal` and check 26 named |
| D14 | the `case`-to-`covers` fix is unarmed | **CLOSED** by S7 and AC10 |
| D15 | section 3 lists a deleted refusal as settled | **CLOSED.** The narrowing-refusal bullet is gone |
| D16 | docs reach two of at least six carriers | **PARTIALLY CLOSED.** Three named; `SESSION-KICKOFF.md` and the leg's DARK text still missed, one named carrier does not exist (M2) |
| D17 | AC4 already green, contradicts AC10 | **RECURS** as AC3 (H4) |
| D18 | AC4 named the wrong observation site | **CLOSED.** rev-2's AC4 pins a fold property hand-written rows can produce; the ordering decision it named is now B2 |
| D19 | `normpath`'s trailing `/.` spelling | **CLOSED** by S4 and AC6 |
| D20 | AC9 cannot distinguish the flip from no flip | **UNADDRESSED — oversight.** Sites moved, gap open (H5) |
| D21 | reuse audit called `normpath` unchanged | **CLOSED.** The audit now says S4 edits it |

**Twelve closed, three partially closed, six live.** Of the six, five are oversights — nothing in
section 3 or the revision log records a decision to leave them — and one (D4) is not merely
unaddressed but decided the other way without saying so.

---

# What these specs got right

Worth stating, because the failure list is long and the revision is genuinely better than rev-1.

- **The re-grounding worked on its own terms.** Spec 23 rev-2's Scope and Design contain no reference
  to deleted machinery. Checked token by token at `d9728f89`. The class that blocked round 1 is closed.
- **S1 is a real finding rev-1 missed entirely**, and it is correct about the code: the fold at
  `check-unattended.sh:1121-1125` does discard all but the last row per key, and the driver's published
  repair (`unattended.sh:2420-2424`) does tell a run to declare again. Those are two answers to one
  question. The disagreement about which answer is right does not touch the diagnosis.
- **Spec 24's retraction is exemplary.** It names `fact()` as the reason its own rev-1 premise was
  false, cites the merge and the commit where `LANDING` actually appears, and drops two scope items
  with reasons rather than quietly rewording them.
- **S6's rationale is the best sentence in the diff** — a comment describing deleted behaviour above
  the code that deleted it is where rev-1 got its mental model. H9 is an argument for applying it
  further, not against it.
- **Spec 25 exists at all.** The instinct to convert a review finding into a gate is right; §7 says so.
  The unit is blocked on measurement it has not done, not on the idea.

# Coverage and limits of this review

- Every code claim was re-verified at `d9728f89`. The awk fold was exercised with synthetic rows; the
  S1 predicate was run over all 225 based specs; `DISPATCH_GRADING` carriers came from `git grep` over
  the tracked tree; rev-1's token set was extracted from `de766cb3`.
- **Not run:** the full bar, the unattended suites, and any fixture. The diff is spec-only and touches
  no gated artifact; the arm-level claims above are traced by reading, not by execution. Arm C's flip
  under the exclusive boundary reading (B2) is traced, not reproduced — reproducing it requires
  implementing S2 first.
- **Not assessed:** whether union versus last-wins is the right semantics at all, as opposed to
  whether the spec's argument for union holds. B1 shows the argument does not; it does not show that
  last-wins is better.
- **Not assessed:** spec 24's S1, which is small, correct about the flow, and uncontested.
