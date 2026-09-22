**Serves:** spec-audit TOOL-dScriptedRepeat-1

*Scope note on the line above: this record audits ALL of units 1-10 and its fold produced unit 11.
The `Serves:` line names the build's anchor id alone because the generated records table has a
declared per-entry byte budget and eleven ids overrun it — measured, nine fit and ten do not. The
coverage line in the build README will therefore report the other units as unnamed by any
spec-audit record; that is an artifact of the budget, not of the audit's scope.*

## Verdict: BLOCKED

Fifteen HIGH findings stand confirmed, and one of them (F1 below) wedges every non-playbook
unattended run in the fleet at `--close` the moment unit 6 lands. The spec set is not buildable as
written. It is, however, close: the fold is bounded, and nothing here questions the ten-unit
decomposition, the seven kickoff forks, or the four research forks. What it questions is that four
of the mode's load-bearing artifacts have readers and no writers, that two Definition-of-Done items
are satisfied by recorded failures, and that the one machine refusal the mode rests on exempts the
file that declares its own scope.

**Precision: 24 / (24 + 31) = 0.436.** Raw findings 55, confirmed 24, refuted 31, unverified 0,
lenses 5/5. The 24 confirmed collapse to **21 distinct defects** — three pairs are the same defect
found twice by different lenses (see §4). Precision below ~0.5 is the charter's tighten-scope
signal; here it is explained by the target rather than by the priming, since a rev-1 spec set is a
fresh surface and three of the five lenses ran over the same four spec files.

Scope of this record: the ten specs under `memory/builds/dScriptedRepeat/spec/` and the build
README, at immutable base `7e2ac32f`. Every "the code says X" claim below was re-read against the
tracked source at that sha; the citations here are the re-verified ones, not the lens's originals.

Ref key: `spec-N` = `memory/builds/dScriptedRepeat/spec/2026-08-20-spec-dScriptedRepeat-N.md` ·
`README` = `memory/builds/dScriptedRepeat/README.md`. Every other path is spelled in full.

## 1. The confirmed findings, grouped by spec

Severity is the lens's, adjusted in two places and said so. `F<n>` numbers are this record's and are
referenced by the fold order in §6.

### Spec 6 and spec 7 — the Definition-of-Done items

**F1 · HIGH · the two new core items are mode-blind, and one of them cannot be met outside the
mode.** `pieces-complete` (spec-6 S1/S2/S4/S5, §5 migration row) and `set-checks-recorded` (spec-7
S5) join `DOD_CORE`, which `verb_close` evaluates for EVERY run regardless of mode.

Evidence, re-verified: `tools/unattended/unattended.sh:1650` is `for item in $(dod); do … dod_met
"$slug" "$rel" "$item" "$ck"`, and `verb_close` (1602-1700) carries no mode branch anywhere.
`DOD_CORE` at `:93` is a flat `<item>:<checker>` grammar with no scope field — unlike
`DIRECTIVES_CORE` at `:112`, whose `researched:M12:prompt` third field is exactly what makes a rule
mode-conditional. Spec-6 S2 term 1 is the vacuity guard ("the declared grain resolves and ENUMERATES
at least one piece"), stated with no mode condition. Under `slug` or `prompt` mode there is no
`playbook:` key, no grain and no `pieces:` — spec-4 S1 reads both keys "only when the mode is the
playbook mode" — so term 1 fails, S4 makes the item non-overridable, and spec-6 §4 names `--abort`
as the only exit. Spec-6 §5 asserts the opposite property without establishing it: "a ninth core
item reds any in-flight run of the new mode until met; no existing run has the mode, so nothing in
flight is affected."

The fold: add an explicit FIRST term to spec-6 S2 and spec-7 S5 — when the recorded mode is not the
playbook mode the item is MET and announces itself with a `skipped — <why>` shape, never a silent
pass — and restate it in each spec's S1 and §5 migration row. Implement it as a mode branch in
`dod_met`, not as a grammar change to `DOD_CORE`: refuted finding R5 measured that a naive third
field routes silently down the machine path, so the grammar route needs a splitter the branch does
not. Add an AC to spec-6 observing a `slug`-mode run closing GREEN with both new items present.

**F2 · HIGH · `pieces-complete` mixes two populations inside one predicate, so a tree that already
holds pieces blocks every close.** Spec-6 S2 term 2 ranges over spec-5 S3's tree-wide grain
enumeration while term 3 ranges over the run's own diff. Found twice, by lens 3 and lens 4.

Evidence: spec-5 S3 defines the enumeration as a glob over the tree — "enumerates pieces by the
declared grain, joins each to its record, and classifies every piece as `verified`, `stale`,
`unrecorded` or `orphan-record`". Spec-6 S2 term 2 then demands "every enumerated piece is
`verified`", while term 3 alone says "the count of pieces THIS RUN produced". A corpus predating
adoption classifies every piece `unrecorded`, so term 2 blocks permanently — for the mode the README
calls "explicitly aimed at a growing corpus". Spec-6 §5 considers only "no existing run has the
mode"; spec-5 §5 covers only the empty tree. Spec-7 F1 states the opposite belief ("unit 6
deliberately counts only the run's own pieces"), true of term 3 and false of term 2, and spec-7
contradicts itself on the same axis: §4 decides the set runs over "unit 5's ENUMERATION of pieces
that exist" while F1 calls run-vs-corpus scope "genuinely open".

Lens 4 adds the second-run case, and it is worse than the pre-adoption one: with spec-6 F2 RESOLVED
to "evaluate at close only", any run-1 piece edited since — by a human, a fold, or an owner
amendment — classifies `stale` at run 2's close and blocks a close it has nothing to do with, on a
non-overridable item. Spec-7 S4 binds the set record to "the ordered list of piece content hashes",
so run 2's larger set makes run 1's record stale by construction, which spec-7 S6 arms as a RED.

The fold: give spec-5 S3 two NAMED scopes — `enumerate_run` (grain intersected with this run's
introduced paths) and `enumerate_corpus` (grain over the tree) — and have spec-6 terms 1 and 2 both
name `enumerate_run`, with the corpus census reported and non-blocking. Keep term 1 guarding term
2's vacuity in whatever scope term 2 lands in; refuted finding R18 established that the guard
relationship is real and must survive the rescope. Give spec-7 S4 a run identity so a set record
whose set has grown reads `superseded`, not `stale`. Resolve spec-7 §4 and F1 against the same two
names. Add an AC to spec-6 observing a second run of the same playbook closing green over a tree
already holding the first run's pieces.

**F3 · HIGH · `CORE_FLOOR` is pinned one-sided, so both units' "the floor rises in the same commit
and the leg is green" is green whether the floor rises or not.** Spec-6 AC6, identically spec-7 AC6.

Evidence, re-verified: `tools/unattended/check-unattended.sh:131` is the only arm reading the DoD
half — `if [ -n "${dfloor:-}" ] && [ "$ndod" -lt "$dfloor" ]` — and `:119` is the same one-sided
shape for phases. There is no mirror of the directives' slack arm at `:743`, which reds when
`DIRECTIVES_FLOOR` is declared BELOW the kit's own core count. `DOD_CORE` holds 8 items
(`unattended.sh:93`), `PHASES_CORE` holds 12, and `.unattended.conf:54` reads `CORE_FLOOR="12:8"`;
add a ninth DoD item and leave the conf untouched and `ndod=9 >= dfloor=8` leaves the leg green.
Spec-6 S1 cites the exact recorded failure it means to prevent — "a core set grew in the shipped
example and not in the dogfood conf, leaving the pin slack while the file still looked configured" —
and then specifies no arm that catches it. Contrast spec-10 AC4, which rests on `DIRECTIVES_FLOOR`
and IS backed by `:743`.

The fold: unit 6 adds the missing arm to BOTH halves of `CORE_FLOOR` — `pfloor < nphase` and
`dfloor < ndod` each redding and naming both numbers — and both AC6s are rephrased as the RED
observation: with `DOD_CORE` at nine and the installed conf's dod half still at eight,
`check-unattended.sh` reds, staged and observed before the arm lands.

**F4 · HIGH · `set-checks-recorded` is satisfied by a recorded FAIL, so the unit built to stop a
monoculture green closes green on a set check that failed.** Spec-7 S5 and AC1.

Evidence: S5 reads "It asserts a verdict EXISTS and is bound to this set; it does not assert what
the verdict concluded"; AC1 asks only that "the run records a verdict for each". The
`closing-review-recorded` precedent S5 borrows does not transfer — that item's own source comment at
`unattended.sh:1816-1819` says a verdict grammar cannot be anchored because "`^## Verdict: CLEAN`
matches zero of this corpus's 46 records", a prose-review limitation — whereas spec-7 S1 makes set
checks `GATE <leg>` entries and §3 makes every verdict "binary and anchored". The reading that would
make the item load-bearing is available here and declined. Composed with F5: a run ships N
monocultured pieces, records the repetition check FAIL, and `--close` reports both `pieces-complete`
and `set-checks-recorded` met — verbatim the green the README says this unit exists to prevent.

The fold: split the item's terms. A `GATE`-tagged set check's verdict must be a PASS to satisfy
`set-checks-recorded`, and a recorded FAIL blocks the close naming that check; a `CHECK`-tagged
entry keeps the existence-only limit, and the leg header states which half is which. AC2 gains a
sibling arm that stages a recorded FAIL and observes the block, distinct from AC2's missing-verdict
message.

### Spec 5 — the per-piece record and its reader

**F5 · HIGH · `verified` is a hash-join state, so `pieces-complete` is met by N pieces whose every
declared leg verdict is FAIL, and fork 5 is implemented by nothing.** Spec-5 S3 and AC1, consumed by
spec-6 S2 term 2 and spec-7 S5. Found twice, by lens 2 and lens 5.

Evidence: fork 5 as ruled in `README` is "piece-done is its declared legs green". Spec-5 AC1 reads
"When a piece and its record agree on the content hash, the reader classifies it `verified`", and §4
derives all four states from the join alone. S1 lists "each declared per-piece leg with its verdict"
as record CONTENT, and no scope item or AC in any of the ten specs ever reads those verdicts:
`grep -rn "green" memory/builds/dScriptedRepeat/spec/*.md` returns 13 hits and not one is a
requirement that a declared leg passed. Spec-6 §3 disclaims "No opinion on piece QUALITY". Spec-6's
non-goals assert "unit 5 owns per-piece verdicts", which unit 5 does not do. `verified` is a
semantic word for a structural state, and it is load-bearing because it is the word spec-6 keys
"the build made what was asked" on.

The fold: narrow `verified` to require BOTH the hash join AND every declared per-piece leg verdict
in the record recording a PASS, and add a fifth state (`failed`, or `unverified-verdict`) with its
own message. State in spec-5 §4 that the hash join answers PROVENANCE and the verdict term answers
DONENESS — two questions, two terms. Spec-6 S2 term 2 names the narrowed state, or gains a term 2b
("no enumerated piece records a failing leg") with its own message and its own staged-RED arm.
Spec-5 S6 gains the arm that stages a hash-fresh record carrying one FAIL verdict and observes
`--close` block. Spec-6 AC4's happy path is restated as "exactly `pieces:` pieces, each hash-joined
AND each declared leg recorded PASS".

**F6 · HIGH · nothing in the ten units WRITES the per-piece record or the set record.** Spec-5
S1-S6, §3, AC1-AC7; spec-7 S4-S5. This is the largest single scope gap in the set.

Evidence: spec-5's six scope items are all read-side — the record's shape (S1), the hash join (S2),
the READER (S3), the liveness assertion (S4), reader independence (S5), and arms for the reader
(S6). §3 says only "The record is not authored by hand. It is written by whatever ran the legs" and
"No opinion on WHO ran the legs". Spec-7 S4 defines the set record and S5 a DoD item asserting it
exists; no writer. Spec-10's start paths enumerate orient / ask once / write the build folder /
commit / push / preflight (S1), and for the attended path merely assert it "produces the same
tracked per-piece and set records unit 5 and unit 7 define" (S2) with no mechanism. Spec-9 adds the
only new verb in the set, `--propose`. A grep for a writer across the spec folder returns only
passive phrasings at spec-5:85, spec-5:109 and spec-7:111. Consequence: spec-6 S2 term 2 and spec-7
S5 can only be met by hand-authoring a record, which spec-5 §3 forbids and which spec-5 §5 concedes
the hash join only raises the cost of, "a cost and not a barrier".

The fold: unit 5 owns the WRITER as a scope item — a driver verb (`--record-piece <path> --leg
<name> --verdict <v>`) reusing `verb_park`'s newline, separator and bypass refusals, its exact-line
idempotence and `stage_or_fail` — plus the attended-path equivalent spec-10 S2 needs. Unit 7 owns
the set-record writer the same way. Add an AC observing a record written by the verb and NOT by
hand, and an AC that a piece with no record written classifies `unrecorded` at close rather than
being silently absent from the enumeration.

**F7 · MEDIUM · spec-6 F2 claims to resolve spec-5 F2 but answers only the DoD half, leaving the
leg's verdict on a stale piece undefined.** Spec-5 F2 and AC2, spec-6 F2, spec-8 S3.

Evidence: spec-5 F2 asks a two-moment question — "whether `stale` should RED or WARN ...
Recommendation: red at close, warn during the run — which needs unit 6 to distinguish the two
moments. Deferred to unit 6." Spec-6 F2 answers one: "RESOLVED (agent, 2026-08-20, delegated):
evaluate at close only." The mid-run moment demonstrably exists and is not unit 6's: spec-8 S3
evaluates "at close and again on the bar, so a run cannot pass it by closing before the bar runs",
and spec-5 AC2 observes staleness through the LEG, not through `--close`. After unit 6's resolution
the leg still has no ruling on whether a stale piece reds the bar mid-fold — exactly the case
spec-5 flagged as "the ordinary path during a fold".

The fold: move the resolution into spec-5, where the reader lives. State that the READER always
classifies and never grades; that `check-playbook.sh` reports `stale` as a warning with its count;
and that only `pieces-complete` at `--close` treats `stale` as blocking. Keep spec-6 F2 as a pointer
to that ruling rather than as its owner. Add a spec-5 AC observing a stale piece NOT redding the bar.

### Spec 8 — the scope gate

**F8 · HIGH · the diff population is under-defined in exactly the dimension the research measured at
22.5x, and as literally written it is a SUPERSET of the `BASE..HEAD` range it rejects.** Spec-8 S1
and §4.

Evidence, re-measured at 7e2ac32f against `memory/builds/aSiftedPlaybook/RUN.md`'s own recorded
`base:`/`witness:` pair: `git rev-list $B..$T` returns 30 commits; unioning each commit's own paths
via `git diff-tree -r -m` yields 50 distinct paths, against 41 for `git diff --name-only $B $T`.
Enumerating commits individually does not shrink the population — it GROWS it, because the merged-in
`main` commits the research blames for the surplus are still in `rev-list`
(`build/hard-problems.md:358`, `aSiftedPlaybook` 383 vs 17, "The surplus is `main` merged in
mid-run"). The research's measured repair is explicit at `hard-problems.md:459-460`: "Scope the diff
to `merge-base(fresh remote default tip, HEAD)..HEAD`, never `BASE..HEAD` and never `--no-merges`.
Refuse when the remote does not answer, in the shape `check-unattended.sh:349-355` already uses."
Spec-8 contains no occurrence of `merge-base`, `first-parent`, `ls-remote` or a remote
re-observation — one grep hit for "remote", in the §5 security row.

The fold: replace S1's prose with the measured definition. `M = merge-base(freshly observed remote
default tip, HEAD)`; the population is the paths touched by `M..HEAD` walked on the FIRST-PARENT
chain with merges read as combined diffs; and a NAMED refusal fires when the remote does not answer.
Add the refusal-on-silence to S3 with its own AC, and add an AC reproducing the 22.5x case and
showing the new population returning the authored count.

**F9 · HIGH · the gate exempts the playbook itself, on a stated reason spec-9 explicitly denies, and
the exempted file is the one that declares the gate's own scope.** Spec-8 S2 and AC3, against spec-9
§3. Found twice, by lens 4 and lens 5.

Evidence: spec-8 S2 lists the exemption set as closed and enumerated and includes "the PLAYBOOK
ITSELF, because fork 6's improvement loop edits it", and AC3 asserts "When the run edits the
PLAYBOOK itself, `bash tools/unattended/check-playbook.sh` passes." Spec-9, which owns fork 6, says
the opposite in the same build: "The verb does not EDIT the playbook. A run that rewrites the
checklist it is judged by has no rules; the precedent run refused exactly this and parked it
instead." Fork 6 as ruled in `README` is "A separate register, surfaced at close" — a proposal
register, not an edit path. The hole is load-bearing: the exempted path holds `outputs`, `grain`,
`step_selector`, `legs` and `coverage` (spec-2 S3), and spec-4 S2 reads `outputs` and `grain` from
the playbook blob, so an exempt in-run playbook edit rewrites the declaration binding the NEXT run —
while spec-8 §4 argues the exemption set must be "closed and enumerated rather than pattern-based,
so widening it is a diff somebody reviews". A playbook edit widens the next run's scope without ever
appearing in that diff.

The fold: delete the playbook from spec-8 S2's exemption set and INVERT AC3 — a playbook-mode run's
edit of its own playbook REDS, staged and observed — and record the inversion in spec-8 §9 as a
correction of fork 6's premise, the way spec-9 §4 already corrects it. If the owner rules that
amendment must happen in-run after all, narrow the exemption to the playbook's PROSE sections and
keep the declaration block in scope, since it is the gate's own input. Route owner-instructed
amendment through a non-playbook-mode path (see F17).

**F10 · HIGH · fork 2's machine refusal cannot evaluate on the attended entry point fork 1 created,
and spec-10 tells the reader otherwise.** Spec-8 S1 and AC7, against spec-10 S2 and S5.

Evidence: spec-8 S1 defines its population as "the set of paths the RUN's own commits introduce or
modify", and AC7 gates evaluation on the mode: "When the mode is not the playbook mode, the gate
does not evaluate and reports `skipped`". Both inputs exist only through the driver — the mode is
read from `authorized-by:` at a pinned BASE (`unattended.sh:783-800`) and second-opinioned from the
recorded `mode:` in a run-state file (`check-unattended.sh:467-471`), and the run's commit set is a
run-state property. Spec-10 S2 defines the attended path as one that "writes NO run-state file,
calls no driver verb", so on that path unit 8 has neither a mode nor a run. Spec-10 §4 is honest
about the RECORDS ("the attended path is gated on WHAT IT PRODUCED and not on how it ran") but S5 is
not honest about the REFUSAL: it calls the Skill's prose "the CHECK half of fork 2 ... paired with
unit 8's machine half", true of one entry point and false of the other.

Severity note: the finding is HIGH because a reader building against S5 will believe the refusal
binds where it does not. The FOLD is cheap — prose plus a header line — which is why it sits in the
sentence tier of §6 despite the severity.

The fold: state the attended gap in unit 8's own header alongside the inside-an-output-path class it
already names, and add it to spec-8 §4's "what this gate cannot see". Correct spec-10 S5 to say the
machine half exists only on the unattended path and that on the attended path the refusal is a CHECK
with no pairing. If fork 1's "ONE gate" is meant to bind the refusal on both paths, that is an owner
decision needing a tree-derived trigger — the presence of a per-piece record set under a declared
grain — rather than a run-keyed one; say which of the two the owner ruled.

### Spec 3 — the validity leg

**F11 · HIGH · the `skipped` verdict these specs rest on does not exist in the gate runner's leg
protocol, so `check-playbook.sh` over an empty population exits 0 and the bar prints `GATE ok`.**
Spec-3 AC8, spec-8 AC7, spec-5 §5 error/empty and migration rows.

Evidence, re-verified: `tools/run-gates/run-gates.sh:665` writes the `skip` rc from the GUARD,
serially, before dispatch (`changed "${gp[@]}" || printf 'skip' > "$WORK/$i.rc"`), and `:844-849`
maps a leg's own result — `skip` only from that pre-written file, `reuse` only from the reuse unit,
`0` prints `GATE ok`, anything else `GATE FAIL`. Line 170 states the invariant: "no knob may ever
turn a leg into a PASS or a SKIP". A leg has no channel to say `skipped`. The guard route is closed
too: `tools/run-gates/run-gates.test.sh:135-150` refuses any `guard` pathspec matching no tracked
path ("the leg would skip forever"), and this repo tracks no playbook, so a playbook-path guard is
rejected while a `tools/unattended/` guard leaves the leg running over zero playbooks. Spec-3 S1
defines the population as "every tracked playbook the declaration seam names", which in the repo
that SHIPS the kit is empty forever — so the leg carrying unit 3's validity gate, unit 5's record
reader, unit 7's set records and unit 8's scope refusal prints `GATE ok` on the dogfood bar while
checking nothing. This is the green-by-absence class the charter names, sitting under the mode's
entire enforcement.

The fold: name the verdict channel that EXISTS. The leg exits NON-ZERO when it can name a population
and resolves none of it, and prints an enumerated-count line the run-gates evidence harness asserts.
Ship one tracked fixture playbook under `tools/unattended/` so the dogfood population is never empty
and a `guard` on that path passes the canary. Rewrite spec-3 AC8, spec-8 AC7 and spec-5 §5 to state
the exit code and the exact bar line each state produces — `GATE ok` / `GATE FAIL` / `GATE skip` —
never the bare word "skipped". This fold changes the vocabulary refuted finding R21 leans on; R21's
substance (two different zero-states with a real discriminator) survives the rewrite.

**F12 · MEDIUM (lens said HIGH; contested) · the runnability oracle reduces fork 5's "every named
leg is runnable" to membership in a registry the playbook's own author wrote in the same file, and
the declared `coverage` mode has nothing to grade.** Spec-3 S5, §5 security row, AC4/AC5.

Evidence: fork 5 as ruled in `README` is "A playbook is VALID only if every step is tagged `GATE
<leg>` or `CHECK <why>` and every named leg is runnable." Spec-3 §5 substitutes a weaker predicate:
"It does not EXECUTE a declared leg during validation; runnability is a registry-membership
question, not an invocation." S5 never gives the registry's codomain, and the acceptance set covers
membership only: AC4 is "a `GATE` names a leg absent from the declared `legs` registry", with no AC
for a registry ENTRY whose target does not resolve. The gate therefore compares a document's GATE
tags against a table inside that same document — the class spec-1 §4 names by name, "an
assertion-between-two-derived-values". S5's three coverage modes ("fully resolvable, probe-only, or
explicitly dark") have no observable difference, and AC5 observes only an UNDECLARED mode, never a
declared one being false.

Severity downgraded to MEDIUM because a skeptic REFUTED the twin of this finding (R46): the spec
states the reduction about itself twice and gives its security reason, so the trade-off is declared
rather than hidden, and the objection to the header word RUNNABILITY is naming preference. What
survives both verdicts, and is the whole fold, is the unarmed coverage declaration.

The fold: specify the `legs` registry's codomain in S5 — an argv, or a path that must resolve in the
adopting tree — and add an AC staging a registry entry whose target does not resolve and observing
RED. Define each coverage mode by what the oracle actually does: `resolvable` = every target
resolves, `probe` = existence-only with the incompleteness printed on every run, `dark` = named
refusal. Add an AC that a playbook declaring `resolvable` over an unresolvable target REDS, so the
declaration is GRADED rather than recorded.

**F13 · MEDIUM · the `curated:` question is deferred to a unit that never resolves it, and three
specs give three different answers.** Spec-3 F2, against spec-2 AC5 and spec-4 §8.

Evidence: spec-2 AC5 asserts one answer — "When `curated:` is absent or empty, unit 3's gate REDS."
Spec-3 F2 asserts a different one and hands the decision away: "Recommendation: red only for a
playbook the declaration seam names as ACTIVE for a run; a draft in the tree is not yet a contract.
Resolving this needs unit 4's seam, so it is deferred to that unit rather than guessed here."
Spec-4's §8 carries exactly two forks (`READ_PATH_CEILING`, and where `pieces:` belongs) and its §2
has no notion of an ACTIVE playbook at all. The deferral has no receiver, and fork 4's "frozen and
marked human-curated" is the property left unenforced. The reused precedent shows the resolved
shape: `tools/lexicon/adopt-lexicon.sh:87-97` reds an unratified seed and `:111` refuses to
overwrite a curated declaration, both with arms.

The fold: resolve it in spec-3 rather than deferring. State whether the gate distinguishes a draft
playbook from a bound one and, if it does, define the discriminator in unit 3's own scope — a
`curated:` VALUE, not a run binding — so the gate stays a tree property like unit 5's reader. Make
spec-2 AC5 match, and add the staged-RED arm for an absent `curated:`, since the freeze is the only
machine consequence fork 4 has.

### Spec 2 — the template and the declaration block

**F14 · HIGH · the template does not ship through the mechanism S1 names, and §10's "no new adopter
code" is false against the adopter this kit actually runs.** Spec-2 S1, §10 reuse audit, AC3.

Evidence, re-verified: `tools/unattended/adopt-unattended.sh` never reads `kit.toml`. It hardcodes
exactly two destinations — `SKILL_OUT="$SKILL_DIR/SKILL.md"` at `:137` and
`PROTO_OUT="$ROOT/$PROTO_REL"` at `:140` — renders the first with `render()` and `tr`-copies the
second at `:216-224`, and its own comment at `:197` reads "The adopter installs TWO artifacts, so
--check verifies two." The `[[files]]` rows with `role = "rendered"` in
`tools/unattended/kit.toml` are read by `tools/govkit/govkit.py` for deployment PLACEMENT, not by
the kit's own adopter, and `[check] argv = ["bash", "{kit}/adopt-unattended.sh", "--check"]` is the
gate leg spec-2 §7 names. AC3 ("When `PLAYBOOK-TEMPLATE.template.md` is rendered by the kit's
adopter…") is an observation nothing can make: no code path renders a third artifact.

The fold: move the adopter work IN SCOPE. S1 names the edits to `adopt-unattended.sh` — a third
render or copy destination, a third `--check` arm with its own not-installed and drifted refusals,
the `{{…}}` placeholder arm, and the "TWO artifacts" comment — plus the `[[lf_pin]]` row. §10 drops
the no-new-adopter-code claim. Restate AC3 against the specific new `--check` arm. Folding this
first also settles refuted finding R23: once the third destination exists, `--check`'s byte-compare
is the render gate and AC3's brace-shape grep is redundant rather than wrong.

**F15 · MEDIUM · the declaration block's key list and its reader list are both wrong the moment the
other specs are read.** Spec-2 S3 and §4.

Evidence: S3 makes an exclusivity claim — "Units 3, 4, 6 and 7 read from this one block; none of
them invents a second declaration site" — and §4 pins the keys: `step_selector` · `step_floor` ·
`outputs` · `grain` · `legs` · `coverage` · `curated`. Three contradictions follow. First, spec-7 S1
adds an eighth key in neither list: "A `set_checks` population in the playbook's declaration block."
Second, spec-7 S1 calls it "parallel to the per-piece one" and spec-5 S1 records "each declared
per-piece leg", but no spec declares a per-piece checks key at all — a declaration site referenced
twice and specced nowhere. Third, the reader list is wrong in both directions: spec-4's inventory
names unit 8 as the reader of `outputs`, and unit 8 is absent from spec-2's list, while spec-6 §4
reads nothing from the block at all ("`pieces:` comes from the README blob at BASE (unit 4). The
grain comes from the playbook blob at BASE (unit 4)") yet spec-2 lists unit 6 as a direct reader.

The fold: make S3 POINT rather than enumerate. State that the block's key set is the union of what
units 3, 4, 5, 7 and 8 declare, list the keys in ONE place with an owning-unit column, and add a
unit 3 AC that reds a declaration block carrying a key no unit owns AND a unit that reads a key the
block does not declare — the same both-directions join spec-10 S6 already uses for directives.

### Spec 4 — the declaration seam

**F16 · MEDIUM · the README half of fork 8's hybrid has no reader, and §10 covers the gap with a
reuse claim naming a parser neither the driver nor the leg calls.** Spec-4 S1 vs S2, and §10.

Evidence: S1 requires "Two new build-README front-matter keys, read at BASE: `playbook:` ... and
`pieces:`". S2 then says "The existing front-matter scan is untouched" — but that awk
(`unattended.sh:783-790`) is the only thing that reads this blob, and it emits `slug=` and `mode=`
and nothing else; the leg's independent copy (`check-unattended.sh:444-471`) is the same shape. AC1
("`--preflight` records the resolved playbook path and its blob sha in Run facts") is therefore
unimplementable without touching the scan the spec says stays untouched. §10 covers it with a false
reuse: "Front-matter parsing reuses `gen_build_index.py`'s `parse_front_matter`, which validates
only its required keys and therefore accepts additive ones without change." That function is Python
at `tools/memory-tree/gen_build_index.py:190`, and its only caller is `gen_build_index.py:531`, the
index renderer — no shell reader on this unit's path touches it. What the research measured is that
ADDING keys does not break the index render: a compatibility observation presented as the reuse
decision, which hides that the driver and the leg each need a second awk key pair.

The fold: rewrite S2 to say the front-matter awk gains two KEY-TAGGED emissions in BOTH the driver
and the leg, preserving the existing one-blob-one-parse property, and say plainly that the "No
second GIT show" comment bounds THAT scan and not the playbook read. Replace the §10 reuse sentence:
the reused seam is the driver's own key-tagged awk idiom and the record-then-second-opinion pattern;
`parse_front_matter` is a compatibility check on the index renderer and belongs in §5 migration, not
in the reuse audit.

### Spec 10 — the two start paths

**F17 · HIGH · the owner's first stated verb — create a playbook when none exists — has no owning
unit and is structurally REFUSED by unit 4's own preflight.** Spec-10 S1-S2; spec-4 S1, S3, AC2.

Evidence: `README` quotes the ask verbatim — "with no playbook it researches the topic and the code
it must relate to, then specs and creates a new checklist playbook from a PLAYBOOK TEMPLATE".
Spec-4 S1 makes `playbook:` a build-README key "read at BASE"; S3's FIRST refusal is "`playbook:`
naming a path that does not resolve at BASE"; AC2 stages and observes that refusal. Spec-10 S1's
unattended start path is "orient, ask ONCE if under-determined, write the build folder carrying the
owner's prose plus `playbook:` and `pieces:`, commit, push, preflight" — no playbook-authoring step
anywhere in the ordered list, and S2's attended path has none either. Spec-2 ships the template and
its §3 explicitly excludes a checker and says nothing about an authoring flow. So a no-playbook
start cannot reach preflight, and the research → author → commit sequence that would create one is
owned by no unit in the roster of ten.

The fold, and it needs an owner ruling rather than an edit: unit 10 gains a THIRD start path
(playbook CREATION) as a scope item — run the research loop, author from unit 2's template, commit
the playbook, and only then write the build README naming it, so the playbook is older than the BASE
by construction. State which authorization mode that creation run wears: it cannot be the playbook
mode, since it has no `playbook:` to name and its diff is entirely outside any declared output glob,
which unit 8 would red. If creation is deliberately out of scope for this build, name it in the
`README`'s "What is deliberately NOT in this build" list so its absence is a decision rather than a
hole. This is also where fork 6's owner-instructed AMENDMENT path belongs, per F9.

### Spec 9 — the proposal register

**F18 · MEDIUM · the new STEP field lands in a record grammar written by ONE shared format string,
and the spec picks neither a placement nor a separator guard for it.** Spec-9 S2 and §5.

Evidence, re-verified: `unattended.sh:1891` is `park() { printf '\n%s %s · item %s · reason %s\n'
"$(date …)" "$2" "$3" "$4" >> "$1"; }` — one writer, all kinds. Every reader depends on `reason`
being last and unbounded: `waivers_of` at `:654` is a sed on `… waiver · item \([^ ]*\) · reason
.*$`, check 17 at `check-unattended.sh:503` is `wh=${wl#* waiver · item }; wh=${wh%% · reason *}`,
and `verb_park`'s comment at `:1953` says the item "is read back as the token between ' · item ' and
' · reason '". `verb_park`'s ` · ` refusal screens `$item` ONLY, because reason could not previously
be mis-parsed. Appending `· step <s>` after reason makes it part of every existing reader's greedy
`reason`; inserting it before reason leaves both `step` and `reason` unguarded against a literal
` · `. Spec-9 §5 enumerates three refusals for the new verb (no step, no item, no reason) and no
separator refusal for the step.

The fold: state the placement in S2 — recommend `… · item <i> · step <s> · reason <r>`, keeping
reason line-final — and extend the ` · ` refusal to the step in S1's "reuses `verb_park`'s guards"
list, with its own arm in S7. Say whether `park()` gains a fifth parameter or `--propose` gets its
own writer, and name the parked-region parsers in the leg and `verb_status` as in-scope readers of
the changed row.

**F19 · MEDIUM · fork 6's "surfaced at close" rests on an item the spec calls derived and the driver
treats as agent-ATTESTED.** Spec-9 S5 and §4.

Evidence: S5 states "`parked-decisions-surfaced` already surfaces every parked kind through one
derived key" and §4 repeats "a single derived `parked-surfaced:` line". The source disagrees twice:
`DOD_CORE` spells it `parked-decisions-surfaced:agent` (`unattended.sh:93`) and `dod_met` grades it
with `grep -qE '^parked-surfaced: (yes|true)' "$rel"` (`:1879-1880`) over a line the run itself
writes via `--attest`. Nothing derives it from the parked region; `verb_status`'s count at `:1566`
is a display line, not the item. Under the protocol's §9 a self-written line is exactly what does
not constitute evidence, so the sentence carrying fork 6's whole "surfaced at close" requirement
claims a derivation the kit does not have. A second overclaim sits beside it: S1 says `--propose`
"reuses `verb_park`'s guards wholesale" and §10 says "reused in full", but `verb_park` refuses when
no run-state file exists (`:1940`), so the verb is unavailable on spec-10's attended path.

The fold: correct S5 and §4 to say `parked-decisions-surfaced` is agent-attested, citing
`unattended.sh:1879`. Then either accept that proposals are surfaced by attestation and say so, or
add a derived count term. Name the two reuse limits explicitly in S1 and §10: the verb requires a
run-state file and is therefore unattended-only, and the STEP field is a row-grammar change whose
readers are in scope (F18). Refuted finding R19 established that the wrap-up half IS covered by
construction — the build method derives the owner's open/parked row from parked entries — so the
correction is to the DERIVATION claim, not to the surfacing.

### The build README

**F20 · MEDIUM · the stated build order contradicts four dependencies the specs themselves assert,
and omits two co-landing constraints.** `README`, "The unit set".

Evidence: the README says "Unit 1 publishes the vocabulary every later unit joins against; units 2
and 3 are the artifact and its checker and can run in parallel with 4-8; unit 5 is the prerequisite
for 6 and 7 ... unit 10 is last." Against that: units 5, 7 and 8 deliver every AC through
`check-playbook.sh`, which unit 3 creates, so 3 precedes 5, 7 and 8 rather than running parallel to
them; spec-5 S3 enumerates "by the declared grain" and spec-6 §4 says outright "`pieces:` comes from
the README blob at BASE (unit 4). The grain comes from the playbook blob at BASE (unit 4)", so 4
precedes 5, 6, 7 and 8, which the order never states; spec-6 §5 states a co-landing constraint the
order does not carry ("Unit 8 owns the diff population and this item consumes it; the two must land
together or this term counts the wrong thing"); and spec-7 §5 asserts a second ("`CORE_FLOOR`'s DoD
half moves with unit 6's in one commit"), which contradicts spec-6 S1 ("`CORE_FLOOR`'s DoD half
rises by one in the SAME commit") and spec-7's own AC6. The generated region confirms nothing
machine-checks this: "No spec under this build declares an `order` verb; the build order is whatever
its authored plan states."

The fold: rewrite the README order paragraph as an explicit predecessor list per unit — 1 → all;
2 → 3; 3 → 5, 7, 8; 4 → 5, 6, 7, 8; 5 → 6, 7; 6 and 8 co-land; 10 last — and reconcile the
`CORE_FLOOR` claim by picking one commit-per-unit story, deleting spec-7 §5's "moves with unit 6's
in one commit" or making 6 and 7 an explicit co-landing pair.

### Spec 1 — the mode vocabulary

**F21 · LOW · two prose counts of the same derived population appear in one spec and disagree, in
the unit whose whole subject is not spelling a set twice.** Spec-1 S1 vs §10.

Evidence: S1 reads "It is the fifth vocabulary in this driver and the only one that is a `case` arm
rather than a named set"; §10 reads "This unit adds a FOURTH member of that established pattern
rather than a new mechanism." Re-measured: `check-unattended.sh:76-82` reads FIVE constants through
`core_of` — `PHASES_CORE`, `DOD_CORE`, `DIRECTIVES_CORE`, `PHASES_TERMINAL`, `PHASES_PASSKIND` —
declared at `unattended.sh:82, 83, 89, 93, 112`. So `AUTH_MODES` would be the SIXTH, and BOTH
numerals are wrong. Two passes of this audit produced two different corrected censuses (five and
six), which is itself the argument. Both are counts of a derived population written in prose, the
class the charter bans by name, and the research already found the same defect live in this kit
(`check-unattended.sh:2`, "TWENTY-ONE checks").

The fold: drop both numerals. S1 can say `AUTH_MODES` joins the constants `core_of` already reads;
§10 can say the unit adds a member of that established pattern. Neither sentence needs a count, and
the drain is the repair the research already recommended for the sibling defect in the same file.

## 2. The refuted findings, one line each

Listed so a later reader does not re-raise them. `R<n>` is the raw finding number.

- id R3 — the reader cannot obtain the playbook path, BASE or grain on the bar or the attended path. Refuted: spec-5 S3 defines the reader as "a function in the leg", so the leg computes them; the playbook, its block, the pieces and the records are all TRACKED and readable at HEAD.
- id R5 — spec-6 §4's reason for rejecting a mode-scoped third `DOD_CORE` field misreads `checker_of`. Refuted: the literal example string IS wrong (`${p#*:}` returns `machine:playbook`), but both consumers route a three-field entry silently down the machine path, so the operative warning holds. Carries an erratum, not a defect.
- id R6 — spec-7 AC5 requires observing that set checks RUN through a gate spec-3 says never executes a leg. Refuted: AC5's instrument reads the tracked set record's verdicts; no execution is implied.
- id R7 — spec-3 §4's "an adopter receives no such file" is false, since `govkit.py:2467-2473` writes a target's gate manifest. Refuted: the sentence reads as "not THIS repo's manifest", and the proposed fix touches no scope item, AC or code.
- id R9 — spec-1 S1's "fifth vocabulary" is a prose count of a derived population and is wrong. Refuted on consequence (nothing keys on it); carried as confirmed F21 on the S1-versus-§10 CONTRADICTION, with the same fold.
- id R13 — `step_floor` is a guard reading the state the bug corrupts. Refuted: it is a human's count of intent measured against a machine predicate's output, and spec-2 §3's stated non-goal rules out a kit-derived count.
- id R15 — spec-8 never names where "the RUN's own commits" come from, and the kit's only answer is the run-state file. Refuted: `authorization-reachable` re-derives BASE through `trusted_base`/`resolve_base` (`unattended.sh:436-445`), and the research records the enumeration method.
- id R16 — spec-4 AC7 passes at BASE with no code written. Refuted: it is a backward-compatibility pin, and a compat arm being green before the change is what a compat arm is.
- id R17 — spec-1 AC1's grep cannot match three of the four sites spelling the two-value set. Refuted: two sets were conflated; `:709`/`:714` hold the SCOPE set (`all`/`prompt`), which S4 and S6 own separately.
- id R18 — spec-6 S2 term 1 enumerates the TREE, the same defect S3 repairs for term 3. Refuted: term 1 guards TERM 2's vacuity by design. Its constraint on F2's fold is recorded there.
- id R19 — no observation proves a proposal reaches the owner. Refuted: spec-9 AC5 is that observation, and the wrap-up half is covered by construction. The derivation claim is carried as F19.
- id R20 — the anti-vacuity control runs over an untracked corpus on one node's disk. Refuted: the ACs are one-time build-time MEASUREMENTS whose outputs are tracked here, and the proposed fix collides with spec-2 §3's stated non-goal.
- id R21 — spec-5 gives the zero-piece enumeration two opposite verdicts. Refuted: the two sentences describe different states (no playbook at all versus a declared grain resolving to zero) and spec-3 F2 owns the third. Its vocabulary changes under F11.
- id R22 — spec-8 AC5's dead probe is armed against an unreachable or an ordinary state. Refuted: S1 and S2 name two distinct terms and AC5 measures the pre-exemption set; a liveness assertion over a DoD-unreachable zero is the point of the drift-audit shape.
- id R23 — spec-2 AC3's brace-shape grep tests a shape the template may never contain. Refuted: §7 already names `adopt-unattended.sh --check` as the render gate, and the proposed angle-bracket arm would red the template on its own canon grammar. Settled by F14.
- id R24 — the attended entry point has no declaration seam at all. Refuted: spec-3 S1's population is tracked and plural, not a BASE blob, and gate legs do carry arguments. The residual (who supplies BASE on the attended path) is precision, not impossibility.
- id R26 — "the diff population" names three different sets, and spec-6 counts pieces under `outputs` rather than by `grain`. Refuted: spec-6 S3's countable noun is *pieces* and its contrast is introduced-versus-present; the exemption subtraction is unit 8's verdict step, never re-named.
- id R28 — four units deliver acceptance through one script only unit 3 scopes. Refuted: no spec claims exclusive ownership, each consumer specifies its own blind-spot sentence, and per-mechanism units adding arms to one leg is this build's own decomposition.
- id R30 — the `curated:` deferral lands nowhere. Refuted as a defect: spec-3 F2 is an explicit open question with a recommendation and a named resolver. The three-answer contradiction is carried as F13.
- id R32 — one `step_selector` is asked to serve three tagged populations. Refuted: spec-7 declares its own `set_checks` key, and set verdicts live in their own tracked set record.
- id R34 — spec-7 claims "the same four states" and then enumerates a different four. Refuted: §5's row is the error/empty checklist row, which omits the success state and uses prose synonyms; AC1-AC4 pin the behaviour unambiguously.
- id R35 — spec-10 S6 declares a both-directions join and supplies a one-direction AC. Refuted: S6 is the binding text and says both directions twice more in §5; AC3's incompleteness is editorial.
- id R40 — no unit totals the build's projected read-path spend. Refuted: the ceiling is already an escalated owner fork, and the README deliberately writes no figure per this repo's ban on a derived count in prose.
- id R41 — the new leg lands with no `ARMS_FLOORS` row. Refuted: `check-arms.py --report` shows rows are opt-in across the live population and `--check` exits 0 today; spec-3 S9 already mandates the coverage.
- id R42 — spec-2 F2's "this ADDS to the read path" is false as written. Refuted: that is exactly how a rendered guide enters the read path, and it is a parenthetical inside the fork where the cost gets decided.
- id R43 — spec-1 F1's mode-spelling fork invalidates a filename baked into 17 lines. Refuted: the census already names the `tools/playbook/` collision, and the 17 lines name the ARTIFACT, not the `authorized-by:` value.
- id R44 — the owner-instructed amend path is unspecced and unexcluded. Refuted: spec-9 §3 states both exclusions, and a stated non-goal is not a defect. Distinct from F17, which is CREATION, not amendment.
- id R46 — the runnability oracle never establishes runnability and `dark` has no stated effect. Refuted as a declared trade-off; the unarmed-coverage half is carried as F12, at reduced severity because of this split.
- id R52 — fork 3's "the playbook IS the spec" is implemented by nothing. Refuted: unit 6 is that implementation, and the claimed routine `build-complete` override was asserted rather than reproduced.
- id R53 — the template's highest-value rule is claimed enforced by a gate that declares itself shape-only. Refuted: spec-3 S9 mandates the staged RED and names S7 specifically; S7's written predicate is structural.
- id R54 — "no new execution surface" contradicts S3's set checks running at `--close`. Refuted: the kit ships no set check of its own, and `--close` is a POSITION in the phase vocabulary, not an executor.

## 3. Unverified findings

**None.** All 55 raw findings received a skeptic verdict. Nothing in this record should be read as
"not yet checked" except what §5 names.

## 4. Where the passes disagreed with each other

Three pairs of confirmed findings are the same defect found twice, and two claims received opposite
verdicts. Recorded so the fold does not double-count and a later reader does not treat a split as a
settled question.

| pair | raw findings | disposition |
|------|--------------|-------------|
| duplicate | R10 (lens 2) + R45 (lens 5) | one defect, folded once as F5 |
| duplicate | R38 (lens 4) + R50 (lens 5) | one defect, folded once as F9 |
| duplicate | R25 (lens 3) + R39 (lens 4) | one defect with two symptoms, folded once as F2 |
| split | R27 confirmed vs R46 refuted | same claim; carried as F12 at MEDIUM, narrowed to the half both verdicts support |
| split | R55 confirmed vs R9 refuted | same claim, opposite corrected censuses (five vs six); carried as F21, fold identical under both |

Four refutations CONSTRAIN a confirmed fold rather than opposing it, and the fold is wrong if it
ignores them. R5 says F1 takes the `dod_met` mode branch, not the `DOD_CORE` grammar change. R18
says F2's rescope must keep term 1 guarding term 2's vacuity. R21 says F11's rewrite must preserve
two distinct zero-states. R23 says F14's third `--check` arm makes the brace-shape argument moot.

## 5. What this audit did NOT check

Said plainly, because a green half of an audit reads as a whole one.

- **No implementation was audited, because none exists.** Every "the code says X" claim was verified against tracked source at 7e2ac32f. No specced behaviour was executed, so no AC was observed either passing or failing. Every "unimplementable" verdict is a reading of the specs against existing code, not a build attempt.
- **The six research records under `build/` were not re-audited.** Where a finding cites `hard-problems.md`, it cites the research's own measurement. The one exception is F8, whose 30 / 50 / 41 commit-and-path counts were re-run at this base.
- **The two reference playbooks were not read.** They live in `nicocares`, outside this repo. Every claim resting on their shape, their step counts, or their four measured defects is inherited from the research records and is unverified here. R20 was refuted partly on this ground and that refutation inherits the same limit.
- **No gate was run.** The merge bar, `check-unattended.sh`, the hygiene gate and the template-size gate were read, not executed. The only exceptions are the two `--report` reads cited in R41 and F21.
- **The specs were not graded against `memory/TEMPLATE-SPEC.md`.** Required status headers, fork RESOLVED marks, rev logs and the spec-shape rules were out of scope; the prior build's "rev logs claim forks resolved that carry no RESOLVED mark" class was not re-run over these ten.
- **No budget was totalled.** The read-path and template-size ceilings both bind this build (the README says so), and R40's refutation says the ceiling is an open owner fork — but nobody in this audit computed what the ten units would actually spend. That number is still owed before the first pass.
- **External research citations were not resolved.** Fork 4's "challenge that shape against external checklist and instruction-design literature" produced citations this audit did not follow.
- **Cross-adopter impact was not surveyed.** F1's fleet-wide wedge was reasoned from `DOD_CORE` and `verb_close`; no adopter tree other than gov was inspected, so the blast radius is stated as a mechanism, not as a count of affected repos.
- **Spec-10's Skill prose and the directive-table wording were not audited** beyond the specific sentences F10 and F19 name.
- **No lens covered a11y, i18n, perf or scale.** For a spec set that is correct, and it is named here so nobody reads the §5 rows inside the specs as audited.
- **The fold was not priced.** §6 orders it; it does not estimate it.

## 6. Fold order — mechanism first, sentences second

The fold is cheaper in this order because every sentence in the second tier describes a mechanism in
the first, and folding prose before mechanism means writing some of it twice.

**Tier 1 — the fold changes a MECHANISM** (new scope items, new arms, new code, or an owner ruling
that gates scope). Within the tier, ordered so a later item's target already exists.

| # | fold | spec | severity |
|---|------|------|----------|
| 1 | id F1 — the mode branch in `dod_met`, its `skipped` announcement, and the `slug`-mode close AC | spec-6, spec-7 | HIGH |
| 2 | id F17 — the third start path, or a recorded non-goal; needs an OWNER ruling first | spec-10, `README` | HIGH |
| 3 | id F6 — the per-piece and set-record WRITERS as scope items | spec-5, spec-7 | HIGH |
| 4 | id F5 — `verified` narrowed to hash-join AND every leg PASS, fifth state, staged-RED arm | spec-5, spec-6 | HIGH |
| 5 | id F4 — `set-checks-recorded` split into a GATE half and a CHECK half, with its FAIL arm | spec-7 | HIGH |
| 6 | id F2 — `enumerate_run` and `enumerate_corpus` as named scopes; terms 1 and 2 rescoped | spec-5, spec-6, spec-7 | HIGH |
| 7 | id F11 — the leg's real verdict channel, the non-zero empty-population exit, the tracked fixture playbook | spec-3, spec-5, spec-8 | HIGH |
| 8 | id F8 — the merge-base plus first-parent diff population and its remote-silence refusal | spec-8 | HIGH |
| 9 | id F9 — delete the playbook exemption and INVERT AC3 | spec-8, spec-9 | HIGH |
| 10 | id F3 — the `CORE_FLOOR` slack arm on both halves, both AC6s as RED observations | spec-6, spec-7 | HIGH |
| 11 | id F14 — the adopter's third destination, its `--check` arm, the `[[lf_pin]]` row | spec-2 | HIGH |
| 12 | id F16 — the front-matter awk gains two key-tagged emissions in driver and leg | spec-4 | MEDIUM |
| 13 | id F18 — the STEP field's placement and its separator guard | spec-9 | MEDIUM |
| 14 | id F12 — the `legs` registry codomain and the graded coverage mode | spec-3 | MEDIUM |
| 15 | id F13 — resolve `curated:` in unit 3 with its staged-RED arm | spec-2, spec-3 | MEDIUM |

**Tier 2 — the fold changes a SENTENCE** (prose, a claim, a header, an order, or one AC restated).
Each is cheap once its Tier-1 sibling has landed.

| # | fold | spec | severity |
|---|------|------|----------|
| 16 | id F10 — correct spec-10 S5's pairing claim; add the attended gap to unit 8's header and §4 | spec-8, spec-10 | HIGH |
| 17 | id F15 — spec-2 S3 points at the key union instead of enumerating it, plus one join AC | spec-2 | MEDIUM |
| 18 | id F20 — the predecessor list, and one `CORE_FLOOR` commit story | `README`, spec-7 | MEDIUM |
| 19 | id F7 — move the stale-piece ruling into spec-5; spec-6 F2 becomes a pointer | spec-5, spec-6 | MEDIUM |
| 20 | id F19 — `parked-decisions-surfaced` is attested, not derived; name the two reuse limits | spec-9 | MEDIUM |
| 21 | id F21 — drop both numerals | spec-1 | LOW |

Two erratum-level corrections ride along with no finding of their own: spec-6 §4's `${p#*:}` example
string is literally wrong (it returns `machine:playbook`, per R5), and spec-8's §4 header should
absorb the attended-path blind spot in the same edit as F10.

## 7. What would flip the verdict

BLOCKED clears when Tier 1 items 1 through 11 are folded and each carries the staged-RED observation
its fold names. F1 alone is the difference between a spec set that is expensive and one that is
unsafe to build in order: it is the only finding whose damage reaches runs that have nothing to do
with this mode. Fold it first, even if the owner ruling F17 needs is still outstanding.
