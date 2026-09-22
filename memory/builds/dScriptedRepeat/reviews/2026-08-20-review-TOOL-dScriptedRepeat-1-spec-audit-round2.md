**Serves:** spec-audit TOOL-dScriptedRepeat-1

## Verdict: BLOCKED

Round 2 audits the FOLD, at immutable range `7e2ac32f..cfed037d`. The severity profile has dropped a
long way from round 1 — no fleet-wide wedge, nothing unsafe, and every finding here is a bounded spec
edit. It is still BLOCKED, for one reason stated plainly: four of the eleven units cannot be
implemented from their own specs, because in each case two sentences in the same build order opposite
implementations and neither is marked as the loser.

- Unit 8: its arm list orders the arm its own acceptance criterion now forbids (D1).
- Unit 3: its population is defined two incompatible ways, and the fixture the fold shipped to keep
  that population non-empty falls in the gap (D6, D7).
- Unit 5: `enumerate_run` was defined in terms of a population that needs a run and a network, in the
  same fold that made its reader run on the merge bar with neither (D11).
- Unit 7: a `GATE`-tagged corpus-scoped check both blocks and never blocks (D2).

Six of the fifteen distinct defects need a DECISION rather than a sentence, which is the same Tier-1
shape round 1 used. That is the whole of the blocker; there is no second class of problem here.

**Precision: 20 / (20 + 12) = 0.625.** Raw confirmed 20, refuted 12, unverified 0, lenses 3/3. The 20
confirmed collapse to **15 distinct defects** — five pairs or triples are one defect found by more
than one lens. Precision is up from round 1's 0.436, which is what a folded surface should do.

Scope: the eleven specs under `memory/builds/dScriptedRepeat/spec/` and the build README, at
`cfed037d`. Every "the source says X" claim below was re-read in this worktree; only `RUN.md` moved
between `cfed037d` and the tree I read, so the readings are the fold's own bytes.

Ref key: `spec-N` = `memory/builds/dScriptedRepeat/spec/2026-08-20-spec-dScriptedRepeat-N.md` ·
`README` = `memory/builds/dScriptedRepeat/README.md`. Every other path is spelled in full.

## 1. Does round 1's BLOCKED clear?

Round 1 §7: BLOCKED clears when its Tier-1 items 1 through 11 are folded and each carries the
staged-RED observation its fold names.

**Not fully. Nine of eleven clear on round 1's own terms. Two do not, and one clears its acceptance
criterion while contradicting itself elsewhere in the same spec.**

The distinction the fold blurs, and it matters: a fold item is LANDED IN THE SPEC when the scope item,
the design paragraph and the acceptance-criterion text exist and say the right thing — that is
checkable today, and I checked it. A fold item's staged RED is DEFERRED TO BUILD TIME by construction,
because no code exists; what is checkable now is only whether the AC text NAMES a staged observation
and whether that observation is one somebody could actually make. Every row below grades those two,
never the observation itself.

| # | round-1 fold | landed in the spec | names a staged RED | verdict |
|---|---|---|---|---|
| 1 | F1 — term zero, the `skipped` announcement, the slug-mode close AC | yes: spec-6 S2/S4.0 + AC0, spec-7 S5.0 + AC0 | spec-6 AC0 stages it; spec-7 AC0 says only "Observed" | CLEARS, with a residual |
| 2 | F17 — the third start path, needing an OWNER ruling first | yes, as unit 11 + spec-10 S0 | spec-11 AC3 stages; AC5 names an observation this repo's anchor cannot produce (D13) | DOES NOT CLEAR |
| 3 | F6 — the per-piece and set-record writers as scope items | yes: spec-5 S2/S3, spec-7 S4 + §10 | spec-5 AC8's two arms; no AC observes the SET record written by the verb | CLEARS, with a residual |
| 4 | F5 — `verified` narrowed, the fifth state, the arm | yes: spec-5 S5/S6, spec-6 S4.2 | spec-5 AC5 and spec-6 AC5, both "Staged and observed" | CLEARS |
| 5 | F4 — the GATE/CHECK split and its FAIL arm | yes: spec-7 S5.2 | spec-7 AC3 "Staged and observed", AC4 for the asymmetry | CLEARS |
| 6 | F2 — the two named enumeration scopes | yes: spec-5 S7, spec-6 S3, spec-7 S3 | a rescope, not an arm; spec-6 AC6 observes the census | CLEARS textually, undermined by D11 |
| 7 | F11 — the real verdict channel, the non-zero empty exit, the fixture | yes: spec-3 S9b + AC8, spec-8 AC5 | spec-3 AC8's two arms, spec-8 AC5's exact bar line | CLEARS, and opened D6, D7, D8, D9 |
| 8 | F8 — merge-base plus first-parent, and the remote-silence refusal | yes: spec-8 S1, S1b | AC8 stages the silence; AC6 and AC9 name a measurement nobody can make (D10) | DOES NOT CLEAR |
| 9 | F9 — delete the playbook exemption, INVERT AC3 | yes in S2, §4, AC3, §9 — and NOT in S6 | AC3 "Staged and observed"; S6 still orders the opposite arm (D1) | CLEARS its AC, contradicts itself |
| 10 | F3 — the `CORE_FLOOR` slack arm and its RED observations | yes: spec-6 S7 + AC8, spec-7 S6 consolidating the pair | AC8 "Staged and observed" | CLEARS, with D3 on the commit story |
| 11 | F14 — the third destination, its `--check` arm, the `[[lf_pin]]` row | yes: spec-2 S1 | AC3's two refusal arms | CLEARS |

**Item 2 is the one to read twice.** Round 1 did not merely ask for the third start path; it wrote
"needs an OWNER ruling first". Three owner rulings are recorded (README, "The three owner rulings of
2026-08-20") and none of them is this one. Spec 11 is also the only spec of eleven whose status header
carries no `ratified <date>` pointer, which `memory/TEMPLATE-SPEC.md` makes part of the same
resolved-forks rule the sweep applied everywhere else. That absence is checkable today and it is the
honest signal that the precondition was skipped rather than met.

## 2. Confirmed findings, by spec, with the exact fold

Severity is the lens's. `D<n>` is this record's number and §6 orders the fold by it.

### Spec 8 — the output-scope refusal

**D1 · HIGH · S6's arm list still orders the arm AC3 now forbids.** (L1-1, L3-2 — one defect, two
lenses.) `spec-8:36-38` reads "Arms: an out-of-scope source edit reds; an exemption-set path passes;
the playbook's own edit passes; …" and is byte-identical to base `7e2ac32f`. Against it, S2 now reads
"**The playbook is NOT exempt.**" and AC3 reads "When a `recipe`-mode run edits its own PLAYBOOK,
`check-playbook.sh` REDS. Staged and observed. This INVERTS the previous revision". S6 is the section
§5's testing row points at — it is the instruction `check-playbook.test.sh` is written from. Following
it produces the arm that certifies the hole F9 was folded to close, and whichever of the two is written
second reds the other.

**The fold.** Rewrite S6's third clause to "a `recipe`-mode run's edit of its own playbook REDS, staged
and observed", keeping the exemption-set arm for the five paths S2 enumerates. In the same edit add the
two arms the fold's new acceptance criteria have and S6 does not: the remote-silence refusal (AC8) and
the empty-population non-zero exit (AC5).

**D10 · HIGH · S1's population makes AC6 and AC9 unobservable.** (L2-2.) S1 fixes the population as
`M = merge-base(the freshly observed remote default tip, HEAD)`, first-parent, "Never `BASE..HEAD`".
AC9 asks for that predicate to be run over the `aSiftedPlaybook` build and to "return the authored
count rather than the range's inflated one"; AC6 asks for it over at least three real past builds
before wiring. Re-measured here against that build's own witness `027504e2`: `merge-base --is-ancestor
027504e2 HEAD` is YES and `merge-base HEAD 027504e2` returns `027504e2` itself, so S1's stated form
evaluated with today's remote tip and a landed build's tip yields a merge-base AT that tip — the
authored count is not reachable through the form S1 gives. Since every build in this tree is a landed
one, the charter control these two ACs implement (run the candidate predicate over the real tree and
print hits AND near-misses) is dead as written. *One correction to the lens's evidence: its
`git diff --name-only 027504e2 027504e2` is a self-diff and proves nothing on its own. The finding
survives on the merge-base identity, not on that number.*

**The fold.** Say in S1 that the fresh-remote merge-base is the LIVE-RUN form, and give the
RETROSPECTIVE measurement its own stated form — merge-base against the default-branch tip as of the
build's landing, or the recorded base with merged-in first-parent history excluded. Then restate AC6
and AC9 against that form with the number each returns recorded. If no retrospective form is wanted,
delete AC9's promise of "the authored count" rather than leave an observation nobody can make.

### Spec 3 — the playbook validity gate

**D6 · HIGH · the leg's population is defined two incompatible ways, and everything the fold added
falls in the gap.** (L3-4.) `spec-3:13-14` is untouched by the fold: "a new merge-bar leg over every
tracked playbook **the declaration seam names**". The seam is unit 4 — a build README's `playbook:`
read at BASE, and spec-4 S1 reads it only in `recipe` mode. But S9b's tracked fixture playbook under
`tools/unattended/` is named by no build README; spec-3 §8 F2 resolves on the opposite reading ("A
draft not ready to be graded is not yet a tracked playbook", i.e. tracked implies graded); and spec-11
S3, AC1 and AC3 all rest on "grades it from the moment it is tracked", which a freshly created playbook
satisfies while being named by no README until a LATER run. Nothing in any spec says how a tracked file
is RECOGNISED as a playbook.

**The fold.** Give S1 one membership predicate and make it tree-derived rather than seam-derived: a
tracked file is in the population when it carries the unit-2 declaration block, or matches a declared
conf glob. The seam's `playbook:` then becomes a POINTER INTO that population rather than its
definition. Restate AC8's two arms against that predicate, and add a spec-11 AC observing the leg
grading a newly created playbook no build README names.

**D7 · HIGH · the fixture closes green-by-absence at the playbook level and re-opens it at the piece
level — or reds the dogfood bar forever, and no spec says which.** (L1-3.) S9b ships the fixture "so
the dogfood population is never empty" and rules that the leg "exits NON-ZERO when it can name a
population and resolves none of it"; AC8 arm 2 requires that with the fixture as the only playbook the
leg exits 0. The same leg carries unit 5's reader, and spec-5 S8 says "A zero-piece enumeration reports
as a dead probe, never as a clean run". The fixture declares a `grain` and this repo ships no pieces
under it, so on every bar run the leg CAN name a piece population and resolves none of it — S9b's own
rule then forces non-zero permanently and contradicts AC8 arm 2. `grep -n fixture spec/*.md` shows the
fixture appears only in S9b, AC8 and the rev log: no requirement that it ship pieces, and none that it
ship the per-piece records unit 5 S2 says only the writer verb produces.

**The fold.** Say what the fixture contains. Either it ships pieces plus verb-written records under its
own grain and AC8 arm 2 asserts a non-zero PIECE count too; or S9b states that the piece-level dead
probe is REPORTED and non-blocking on the leg while only `--close` blocks — which is unit 5 S9's
grading rule, and which S9b's "can name a population and resolves none of it" currently overrides.

**D8 · MEDIUM · §5 still declares the empty state legitimate and demands the one verdict no leg can
emit.** (L1-6.) `spec-3:120-121`: "no playbook in the tree is a legitimate state and must report as
SKIPPED with the reason, never as green." S9b, added in the same revision, says "a leg cannot say
`skipped`" and AC8 says the leg exits non-zero and the bar prints `GATE FAIL`. The row was never touched
by the fold, while spec-5's rev-2 log claims the `skipped` claims were replaced. An implementer reading
the production-readiness row rebuilds the green-by-absence path.

**The fold.** Rewrite the row to match S9b: an empty population is NOT legitimate, the leg exits
non-zero, the bar prints `GATE FAIL` with the reason, and a declared selector matching zero lines still
reds via the floor.

**D9 · MEDIUM · "the leg's exit code differs" is unfalsifiable as written.** (L1-7.) `spec-5:78-79`
claims the two zero-states are discriminated by exit code; spec-3 S9b repeats that they stay distinct
but gives ONE rule covering both; spec-5 §5 defers the number ("whose exact exit code and bar line unit
3 owns"); spec-3 AC8 covers only the no-playbook state and spec-5 AC6 only the zero-piece state, naming
no code. No spec names the second code. The skeptic's point stands that this has no build consequence
today, since both states red and `run-gates` maps every non-zero to `GATE FAIL` — which is why it is
MEDIUM and why the cheap fold is legitimate.

**The fold.** Whichever way D7 is ruled: either give each zero-state its own exit code and bar line in
S9b and have spec-5 AC6 and spec-3 AC8 each assert its own; or delete the "and the leg's exit code
differs" clause from `spec-5:79` and let §5's deferral be the whole claim.

### Spec 5 — the per-piece record

**D11 · HIGH · `enumerate_run` now needs a run and a network, in the fold that gave its reader
neither.** (L2-3.) spec-5 S7 defines `enumerate_run` as "the declared grain intersected with the paths
this run introduced, PER UNIT 8'S POPULATION". The same fold made that population depend on "the freshly
observed remote default tip" (spec-8 S1) with a fail-closed refusal on remote silence (S1b). But S10
gives the reader only "the playbook path and BASE as arguments", AC7 requires it to run "in a tree
containing no run-state file at all" and still report the same five counts, and AC6 requires a per-scope
dead probe. The precedent S1b cites is guarded the other way:
`tools/unattended/check-unattended.sh:230` runs the advertisement only
`if [ -n "$adv_remote" ] && [ "$POP" != 0 ]`, with the comment "GUARDED on the population too: with no
run-state file there is nothing whose BASE could be checked, and two network round-trips per bar run
bought exactly nothing", and `:210-212` records that the authoritative run is the pre-push hook "which
has the network by construction" while "An offline diff-scoped run pays it LOUDLY". Units 6 and 7 then
build their whole close on this scope.

**The fold.** State in S7 what `enumerate_run` resolves to when there is no run — either a named refusal
that unit 3's verdict channel carries, in which case AC7 must stop claiming both scopes report; or a
run-independent derivation, for which the piece records' own recorded run identity (spec-7 S4) already
exists. Whichever is picked, say in spec-8 S1b that the remote observation is guarded on there being a
run, the way the precedent it cites is.

### Spec 7 — the set-scoped checks

**D2 · HIGH · F1's resolution contradicts three binding sections of the spec it sits in, and invents a
grammar field nothing declares.** (L2-6, L3-3 — one defect, two lenses.) `spec-7:153-158`: "the
population is declared PER CHECK as `run` or `corpus` … a `corpus`-scoped check WARNS and never blocks".
Against it: S3 (`:20`) fixes one population with no per-check choice; S5 term 2 (`:33`) is
unconditional — "every declared `GATE`-tagged set check records a PASS. A recorded FAIL BLOCKS, naming
the check"; §4 (`:80`) says "The set here is unit 5's `enumerate_run`, never a declared plan". S1
(`:13-15`) pins the entry grammar as `GATE <leg>` or `CHECK <why>` — "One grammar, two populations" —
and carries no scope field, which unit 3's tag grammar does not enforce and unit 2 S3's owning-unit key
union does not mention. S7's arm list has no corpus arm and AC1-AC7 observe no corpus behaviour. So a
`GATE`-tagged corpus-scoped check recording FAIL blocks under S5 and never blocks under F1, and the
added behaviour ships unarmed.

**The fold.** Either re-resolve F1 to `enumerate_run` only, which is what S3, S5 and §4 already say; or
fold the pick into the body properly — add the population field to S1's grammar, to unit 2 S3's
owning-unit key table and to unit 3's tag grammar; rewrite S3 to name both scopes; rewrite S5 term 2 to
"every declared `GATE`-tagged, `run`-scoped set check records a PASS; a `corpus`-scoped entry never
blocks and its census prints"; and add two arms to S7 plus an AC — a corpus-scoped FAIL that does NOT
block, and its census printed. An unobserved non-blocking path is indistinguishable from a check nobody
ran.

### Spec 6 — `pieces-complete`

**D3 · MEDIUM · S1 still says the floor rises by ONE in the commit the fold made a co-landing pair.**
(L2-5, L3-5 — one defect, two lenses.) `spec-6:14-15`: "`CORE_FLOOR`'s DoD half rises by ONE in this
repo's `.unattended.conf` in the SAME commit". `spec-7:36-38` (new): "Units 6 and 7 CO-LAND as one
commit-per-pair so the DoD half of `CORE_FLOOR` moves once, from eight to ten". The README repeats the
composite. `.unattended.conf:54` reads `CORE_FLOOR="12:8"` today, so following S1 literally in the
co-landing commit writes `12:9` against ten core items and reds the bar through unit 6's own new S7
slack arm — the arm working, on the instruction its own spec gave.

**The fold.** Rewrite S1 to the co-landing story: the pair adds two items and the DoD half moves from
eight to ten in that one commit, per unit 7 S6. AC8's staged nine-against-eight state is a
*discretionary* second edit — the skeptic's point that a staged break is artificial by construction is
right, so restating it against ten-against-eight is a clarity improvement, not a correctness one.

### Spec 2 — the playbook template

**D12 · MEDIUM · the both-directions key join has no machine source on one side, and its first victim is
this build's own artifact.** (L2-4.) S3 defines the block's key set as "the UNION of what units 3, 4, 5,
7 and 8 declare"; §4 puts the key table "in the template itself with an owning-unit column"; AC3b
requires `check-playbook.sh` to RED "when the declaration block carries a key no unit owns, or a unit
reads a key the block does not declare". Two problems. First, the union is already short a member:
spec-5 S1 records "each declared per-piece leg with its verdict", S5 and S6 hinge on "every DECLARED
per-piece leg", spec-7 S1 calls `set_checks` "parallel to the per-piece checks key" — and no spec
declares that key. Under AC3b as written, unit 5 reads a key the block does not declare, which is a RED.
Second, "what a unit reads" exists only as spec prose, so the second direction names no machine source;
the precedent (unit 10 S6's directive join) compares a table against the `DIRECTIVES_CORE` shell
constant, which is a real second source.

**The fold.** Give unit 5 a scope item declaring the per-piece checks key. Then state what the checker
actually joins — the template's owning-unit key table against a playbook's declaration block — and
either name a machine source for the units'-reads direction or say plainly that direction is a
documented CHECK. *Round 1 refuted the ownership half of this at R28 and the skeptic refuted it again
here, so do NOT re-raise "unit 3 has no scope item for the join"; per-mechanism units adding arms to one
leg is this build's own decomposition.*

### Spec 11 — authoring a playbook

**D13 · HIGH · the ordering property rests on a refusal that does not fire under the anchor this repo
declares.** (L1-5.) S4: "The playbook must be OLDER than the BASE of any run that names it". AC5: a
single run that creates a playbook and then names it in its own README is REFUSED "because the playbook
does not resolve at that run's BASE… a refusal that already exists rather than one this unit adds".
S7's fourth arm and §10's reuse claim both rest on it. But `.unattended.conf:80-89` in THIS repo
declares `ANCHOR_SCOPE="published"`, and `spec-4:62` says of that anchor, in this same build, "Under the
published anchor the BASE is a tip the run itself pushed, so the run can author both blobs" —
`memory/guides/UNATTENDED-PROTOCOL.md:54` says the same. Spec 10's S1 ordered start path is exactly that
shape: write the build folder, commit, push, preflight. So in the tree where these ACs will be observed,
a creation-and-follow run resolves `playbook:` at its own BASE, unit 4's first refusal does not fire,
and S7's protective arm observes nothing.

*The skeptic refuted the lens-2 form of this claim (see R22 below) on the grounds that the KIT default
is `default-branch` and `published` is opt-in. That half is correct and it is why the ARM is stageable.
It does not reach the finding: gov is the dogfood tree and gov declares `published`.*

**The fold.** Qualify S4 and AC5 by anchor, and pick one of two: name the mechanism that enforces the
split under `published` — for instance unit 4 refusing when the resolved playbook blob's introducing
commit is reachable only through the run's own pushed tip, which needs its own AC in unit 4 — or restate
S4 as a documented CHECK with no machine half under that anchor and say so, the way spec-10 S5 now does
for the attended path. Note in either case that spec-8's non-exempt playbook (S2) reds such a run on the
unattended path, which is a real backstop and a different mechanism from ordering.

### Spec 9 and spec 11 — authority and tier

**D14 · MEDIUM · two of the sweep's delegated marks reach past the authority the build method
delegates.** (L3-6.) `memory/guides/BUILD-METHOD.md:66-67`: "It does not delegate SCOPE: a fork whose
options differ in *what gets built* is not yours — park it". `spec-9:64-68` says of F1's alternative "If
the owner meant region literally, this unit is wrong and the alternative costs a new file outside the
run-state file — which lands outside unit 8's exemption set and needs adding there" — options that
differ in what gets built — and F1 nevertheless marks itself "(agent, 2026-08-20, delegated) …
mechanism rather than scope" against the owner's own words from fork 6 ("A separate register … distinct
region"). Separately, spec 11 is the only spec of eleven whose header carries no `ratified <date>`
pointer, and round 1's fold item 2 said F17 "needs an OWNER ruling first" — the three rulings the README
records do not include adding unit 11.

**The fold.** Re-mark spec-9 F1 as parked for the owner (one line; the built shape stays the fifth
`park()` kind until the owner says otherwise) and put unit 11's existence to the owner as a scope
question. On a yes, stamp spec 11 with its `ratified <date>` pointer like its ten siblings. If the
standing mandate is read as covering it, say so IN spec-11 §8 with the mandate named, so the delegation
is on the record rather than inferred from a missing stamp.

**D15 · MEDIUM · spec-9 is stamped Tier-1 while the fold made it a new write path and a shared-row
grammar change, and the README contradicts the stamp in one sentence.** (L3-9.) `spec-9:3` carries
`· Tier-1 ·`. The charter's §8 first bullet defines Tier 1 as mechanical/additive with **no new write
path** and no shared-contract change. Unit 9 S1 adds the `--propose` verb (a new write path into the
run-state file); S2 changes `park()`'s single format string that `waivers_of`
(`tools/unattended/unattended.sh:654`) and check 17 (`tools/unattended/check-unattended.sh:503`) both
parse; S5b names "the parked-region parsers in the leg and in `verb_status`" as in-scope readers; S4 and
S6 change protocol §2 and §7 and the Skill's verb table. `README:162-163` states the rule and breaks it
in the same sentence: "Every one is Tier 2 except unit 9 — this is a kit contract change throughout,
which the manifest's tier rule makes Tier 2 by definition."

**The fold.** Re-stamp spec-9 as Tier-2 — it already carries all ten sections, so the cost is the review,
not the document — and delete the "except unit 9" clause from the README paragraph.

### The build README

**D5 · MEDIUM · unit 11's predecessor row reproduces the defect the table was added to repair.** (L2-8,
L3-8 — one defect, two lenses.) `README:182` reads `| 11 | 2, 3 |`, in a table the README itself says is
stated as a predecessor list "because the previous prose version contradicted four dependencies the
specs themselves assert". But spec-11 AC4 and AC5 exercise unit 4's preflight resolution and its
refusal, AC2 exercises unit 8's mode gate (its ABSENCE cannot be observed before the refusal exists),
and AC6 exercises unit 6's and unit 7's term zero. None of 4, 6, 7, 8 is in the row.

**The fold.** Change row 11 to `4, 6, 7, 8` (which transitively carries 2, 3 and 5), or split unit 11's
ACs into the ones its own landing proves and the ones the co-landing triple's landing proves, and say
which.

**D4 · LOW · "Ten units." survives beside a generated region reading eleven.** (L1-10, L2-11, L3-8 — one
defect, three lenses.) `README:162` opens the unit-set section "Ten units. One mechanism each, per the
build method's M2." The predecessor table below carries eleven rows, the `roster:units` region carries
eleven, the front-matter `ids:` lists eleven, and `README:254` reads "**Build status:** SPECCED ·
11 unit(s)". This is the charter's "NO count of a derived population is written in prose", and it is the
exact class round 1 folded as F21 in spec-1, reappearing in the fold that created unit 11.

**The fold.** Drop the numeral: "One mechanism per unit, per the build method's M2". The roster region
and the generated block already carry the count and cannot go stale.

## 3. Refuted, one line each — do not re-raise

- R2 — F6's set-record writer IS scoped: spec-7 S4 names "unit 5's writer function through a set-scoped caller" and §10 repeats it, so unit 5's silence is the delegation working; the residual (no AC observes it) is noted in §1 row 3, not a gap.
- R4 — the `CORE_FLOOR` AC8 half: a staged break is artificial by construction, so a nine-against-eight stage the real commit never passes through is exactly what staging is for; the S1 sentence half survives as D3.
- R8 — spec-2 AC3b's ownership: round 1 refuted this class at R28, and binding acceptance in spec-2 compels the arm whether or not spec-3 itemises it; the sharper halves survive as D12.
- R9 — spec-9 §4 DOES carry the F19 correction ten lines below the quoted sentence ("it is an attestation, per S5"), so the rev-2 log is accurate and the residual adjective turns no mechanism.
- R11 — the "reds the bar forever for every adopter" form: round 1's R24 settled that spec-3 S1's population is tracked and plural, and the fixture ships inside `tools/unattended/`; the surviving halves are D6 and D8.
- R17 — spec-3 S9b DOES name the zero-piece state and spec-8 AC5 DOES spell the empty-population exit code and bar line, so neither delegation dangles; the residual clause survives as D9.
- R19 — the `recipe` rename: the README's surviving `playbook` instances are records flagged as verbatim or as older than the spec set, and spec-2's are a section title and a genre description, so no mode value is in play.
- R20 — `superseded` is not a sixth per-piece state: spec-5's five classify a PIECE, spec-7 §5 enumerates the SET record's own five with their messages, and S4 plus AC2/AC3/AC5 name the classifier.
- R22 — the ordering-property refusal IS stageable under the kit's `default-branch` default (`tools/unattended/unattended.sh:403`); **partially overturned** — that ground does not cover this repo, which declares `published`, and D13 carries the surviving half.
- R28 — unit 8's kit-CORE-plus-playbook-EXTENSION exemption set is still enumerated and still a reviewed diff, and §5 already concedes "this is a scope gate, not a security boundary".
- R31 — spec-2 F2's read-path discharge: `.memory-tree.conf:113-120` records the owner's raise and instructs whoever merges to re-run `--measure`, and check 16 reds on overflow, so no pre-totalled prose figure is owed.
- R32 — spec-1 §3's stale non-goal bullet points at §8 F1, which reads RESOLVED (owner) `recipe`; every carrier in the build says `recipe`, so no option survives to be vetoed.

## 4. Unverified

**None.** No finding was carried out of the lens passes unresolved, and every "the source says X" claim
above was re-read in this worktree. Two limits on that are worth naming rather than leaving implied,
because a fully-verified section reads stronger than it is:

- **D13's mechanism is a READING, not an observation.** I verified `.unattended.conf:80-89` declares
  `published` and that `spec-4:62` and `memory/guides/UNATTENDED-PROTOCOL.md:54` both say the BASE is
  then a tip the run itself pushed. I did not run `--preflight` against a staged creation-and-follow run.
- **D10's number is unmeasured.** I confirmed the merge-base identity that kills the retrospective form;
  I did not compute what a corrected retrospective form would return for `aSiftedPlaybook`, so AC9's
  "authored count" still has no figure attached in this record either.

## 5. What this round did NOT check

Stated plainly, because a green half of an audit reads as a whole one.

- **No implementation was audited, because none exists.** No acceptance criterion was observed passing
  or failing. Every "unimplementable" verdict here is a reading of the fold against existing tracked
  source, not a build attempt.
- **No gate was run.** The merge bar, `check-unattended.sh`, `check-playbook.sh` (which does not exist)
  and the hygiene gate were read, never executed. The only commands run were git plumbing —
  `merge-base`, `--is-ancestor`, `log`, `diff --stat` — and file reads.
- **Specs 1, 4 and 10 were read only where a finding cited them.** No lens swept them end to end this
  round; they appear above as evidence for findings owned elsewhere. Their own fold (F16, F18, F10, F21)
  is therefore graded in §1 by presence, not by an adversarial pass.
- **The two reference playbooks were not read.** They live in `nicocares`. Every claim resting on their
  shape, step counts or measured defects is inherited from the research records and is unverified here,
  exactly as in round 1.
- **The six research records under `build/` were not re-audited**, and neither was round 1's own refuted
  set except where a round-2 finding cited it.
- **The specs were graded against `memory/TEMPLATE-SPEC.md` on ONE rule only** — the `ratified <date>`
  pointer, and only because D14 cited it. Section shape, front matter, index caps and the rest were not
  checked.
- **No budget was totalled.** Round 1 recorded this as owed; the owner has since raised
  `READ_PATH_CEILING`, and R31 establishes the convention is to re-run `--measure` at merge. Nobody has
  run it, here or in the fold.
- **Cross-adopter impact was not surveyed.** D13 is measured against THIS repo's `.unattended.conf`
  only; an adopter declaring `default-branch` gets the behaviour R22 describes, and no other adopter
  tree was inspected.
- **No lens covered a11y, i18n, perf or scale**, so the §5 rows inside the specs are unaudited.
- **The fold was not priced.** §6 orders it; it does not estimate it.

## 6. Fold order — mechanism first

Ordered so a later item's target already exists. The first seven change what gets built; the last eight
change a sentence, a row or a stamp.

| # | fold | spec | severity |
|---|---|---|---|
| 1 | id D14 — the two authority questions to the owner; unit 11's `ratified` stamp | spec-9, spec-11 | MEDIUM |
| 2 | id D6 — one membership predicate for the leg's population | spec-3, spec-11 | HIGH |
| 3 | id D7 — what the fixture contains, and whether the piece-level dead probe blocks | spec-3, spec-5 | HIGH |
| 4 | id D11 — what `enumerate_run` resolves to with no run; guard S1b on there being one | spec-5, spec-8 | HIGH |
| 5 | id D10 — the retrospective measurement form, and AC6/AC9 restated against it | spec-8 | HIGH |
| 6 | id D2 — re-resolve spec-7 F1, or fold the scope field into S1, S3, S5, S7 and an AC | spec-7, spec-2, spec-3 | HIGH |
| 7 | id D13 — qualify the ordering property by anchor, or name the mechanism in unit 4 | spec-11, spec-4 | HIGH |
| 8 | id D1 — invert S6's third arm; add the AC5 and AC8 arms it never got | spec-8 | HIGH |
| 9 | id D12 — declare the per-piece checks key; say what AC3b's second direction reads | spec-5, spec-2 | MEDIUM |
| 10 | id D3 — spec-6 S1's co-landing story, eight to ten in one commit | spec-6 | MEDIUM |
| 11 | id D15 — re-stamp spec-9 Tier-2; drop the README's "except unit 9" clause | spec-9, README | MEDIUM |
| 12 | id D8 — spec-3 §5's error/empty row matched to S9b | spec-3 | MEDIUM |
| 13 | id D9 — name the second exit code, or delete the "exit code differs" clause | spec-5, spec-3 | MEDIUM |
| 14 | id D5 — unit 11's predecessor row | README | MEDIUM |
| 15 | id D4 — drop "Ten units." | README | LOW |

Items 2 through 7 are the blocker. Items 8 through 15 are cheap once their Tier-1 sibling has landed,
and none of them would hold a verdict on its own.
