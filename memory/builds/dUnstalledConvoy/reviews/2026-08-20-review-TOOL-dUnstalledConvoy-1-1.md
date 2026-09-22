## Verdict: CLEAN WITH FIXES

**Serves:** spec-audit PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10 TOOL-dUnstalledConvoy-11 TOOL-dUnstalledConvoy-12

# Spec audit — dUnstalledConvoy, the 13-unit set, before any of it is built

A DESIGN review of the spec set at BASE `2dc9df35`. No unit has been built, so every failure below is
a prediction about what happens when one is.

## Review shape

- **confirmed 48 · refuted 44 · precision 0.52.** After dedupe the 48 confirmed collapse to **35
  distinct defects: 14 HIGH, 19 MEDIUM, 2 LOW.** Nothing was downgraded in the merge; the duplicates
  are one defect reached by separate lenses, and each merged section names the lenses that found it.
- **Six findings were raised as BLOCKER and the skeptic downgraded every one.** The reason is
  recorded inside each of those sections, in bold, so the downgrade is auditable rather than silent.
  No BLOCKER survived verification, which is why this is not BLOCKED. It is not a clean bill either.
- **Read the ordering findings first — H12, H13, H14, M6 and M11.** They are one shape: a spec
  obliges a run to use a mechanism that a LATER unit builds. The README's order is TOTAL, so these
  are decidable now and expensive later; once the passes start, the wrong order costs a red bar with
  no in-band repair. M2's cross-read axis "no sub-spec depends on a unit sequenced after it" is the
  rule they break, and M2 says to fix that class before the first code pass.
- Two things this set already does well, which several fixes below could damage if applied
  carelessly: every check-adding unit carries an honest-limit statement in its own design section,
  and several criteria already require the failing case observed RED before landing. Much of the
  refuted set died on exactly those two properties. Do not trade them for coverage.

---

## HIGH

### H1 — the announced skip line violates the leg's own output contract, and no unit owns the contract change
`2026-08-20-spec-TOOL-dUnstalledConvoy-2.md` §2 S5 and §6 AC6 · the same construct in `...-6.md`
S6/AC5, `...-10.md` S6/AC7 and `...-12.md` AC7 · lens: unstated-assumption · **raised as BLOCKER,
downgraded because one unit adopting the contract change closes it — but today none does**

Four units independently specify a check that PRINTS a named skip line and still exits 0.
`tools/unattended/check-unattended.sh:7` states the opposite as its contract: "Exit 0 + no output =
clean. Anything printed is a violation." Its sibling test hard-asserts that three times —
`check-unattended.test.sh:142` compares the run's output against the empty string under the name
"a conforming tree prints nothing", and again at lines 224 and 572 — and the test's runner folds
stderr into stdout, so routing the line to stderr does not escape it either.
`tools/memory-tree/check-memory-hygiene.sh` carries the identical contract line, which is what unit
13's AC7 runs into.

Failure when built: whichever of the four lands first ships the line. TOOL-10's AC7 is decisive — it
requires the skip observed on THIS repo as it stands, and this repo has no dispatch rows anywhere, so
the line prints on every bar run from that commit onward. The `unattended gate selftest` leg then
fails at its GREEN CONTROL, before any red arm is reached. The push boundary reds, and the obvious
repair — deleting the green control — removes the arm that makes every other arm in that file
meaningful.

Fold-in: decide the output channel ONCE, in the unit that lands first, and have the other three cite
it instead of re-specifying a printed line. Three dispositions are viable and the specs must name
which. Amend the leg's header contract and the three green-control arms in the SAME commit as the
first skip line. Or emit the skip only under an explicit report mode, so the default run stays
silent. Or keep the leg silent and move the liveness assertion into the sibling test as a positive
arm. Whichever is chosen, one unit owns it and the other three carry a pointer.

### H2 — unit 13's population contains this build's own specs, and units 12 and 13 state opposite things about it
`2026-08-20-spec-TOOL-dUnstalledConvoy-12.md` §2 S2 with `...-11.md` §4 "Grandfathering" · lens:
underspecification · **raised as BLOCKER, downgraded because the repair is one sentence inside unit
12's own scope and the wrong outcome is a loud red rather than a wrong verdict**

Three sentences across two specs cannot all be true. TOOL-11 §4 sets `ACCEPTANCE_LEDGER_CUTOFF` to
"the day this pair lands". TOOL-12 S2 makes the population "every spec whose status is `CLOSED` and
whose filename date is at or after" that value — inclusive. TOOL-12 §4 then asserts the consequence
is empty: "Every closed spec in this corpus predates the cutoff on the day the pair lands, so the
check's first run sees nothing." Every spec filename in this build carries the date 2026-08-20.

Failure when built: on a same-day landing this build's own closed specs are inside the population the
pair creates, and none carries a ledger, because the grammar did not exist when they closed. TOOL-12
AC7 then FAILS rather than passing blindly, which is the one mercy here. On any later landing date
the population is empty and the mechanism ships never having been exercised on a real unit, which
AC7 also cannot distinguish. Either way the two specs disagree about a config key's semantics, which
is precisely M2's cross-read axis "any config key spelled twice is spelled identically".

Fold-in: resolve it as a stated fork in TOOL-11 §8 with one of two explicit picks. Set the cutoff to
the day AFTER the pair lands, grandfathering this build, and add a TOOL-12 criterion observing that
this build's own closed specs are counted in S7's announced excluded line. Or set it to the build's
own date and add a TOOL-11 scope item requiring a back-filled ledger for every unit closed earlier in
this build, with a TOOL-12 criterion observing those back-filled ledgers pass. Either way TOOL-12
§4's empty-first-run sentence has to be rewritten to match the pick, and TOOL-11 §4 should state the
invariant its sibling keys encode — no already-landed spec is retroactively red — rather than a date
that satisfies it by luck.

### H3 — a correct supersession manufactures an id that unit 9 demands an `add` row for, and unit 8 refuses to write one
`2026-08-20-spec-TOOL-dUnstalledConvoy-6.md` §2 S2 and S3 with `...-5.md` §2 S6 and §4 · lens:
underspecification · **raised as BLOCKER, downgraded because a legal call-before-edit ordering exists
— but no spec states it and the spec that should states its opposite**

TOOL-6 S2 is unconditional: every id present at HEAD and absent at BASE must be accounted for by a
rescope row of act `add` naming that id, and §4's inventory table repeats it verbatim as a refusal.
TOOL-6 S4 separately requires a supersede row's successor to be PRESENT at HEAD. TOOL-5 §4 spells a
supersession as ONE row — kind `rescope`, act `supersede`, original then successor — and TOOL-5 S6
REFUSES an `add` for an id the generated units region already carries.

Failure when built: a run supersedes a unit exactly as unit 7 of the roster authorises. It authors
the replacement spec, retires the original, records one supersede row. The index regenerates, so the
successor is in the units region. Unit 9 of the roster sees it present at HEAD, absent at BASE, finds
no `add` row, and reds the bar. The run calls the verb to repair and TOOL-5 S6 refuses, because the
id is already in the region. The only legal sequence is to record the `add` BEFORE authoring the
spec, which no spec states, no criterion observes, and which contradicts TOOL-5 §4's own sentence
that nothing forces the verb to be called before the edit.

Fold-in: make TOOL-6 S2 accept a supersede row naming the id as its successor as sufficient
accounting, alongside an `add` row. Add a TOOL-6 criterion observing a full supersession end to end —
original flipped to WONTDO, replacement present at HEAD, one supersede row, green; AC4 today covers
only the inverse case. Then either drop TOOL-5 S6's refusal or state the required ordering in TOOL-5
S2 with its own criterion, and correct TOOL-5 §4's honest-limit paragraph, which is false for `add`
as specified.

### H4 — unit 9's phase guard does not bound what it is written to bound, and at check time the phase is always past it
`2026-08-20-spec-TOOL-dUnstalledConvoy-6.md` §8 F1 with §2 S2 · lens: underspecification, reached
independently from two directions

F1 claims that running the check "only from `BUILDING` onward" keeps it "from demanding a record for
ordinary spec authoring". It does not, for two independent reasons. The phase guard decides WHEN the
comparison runs; S2 fixes the comparison window at the run's recorded BASE against HEAD regardless of
phase, and `gen_build_index.py` renders one row per spec file, so a spec authored during SPECCING is
an id present at HEAD and absent at BASE the moment the run enters BUILDING. Separately, the
authoritative run of this leg is the full bar at the push boundary, and `verb_close` ends with
`set_fact "$rel" phase LANDING` (`unattended.sh:1691`). LANDING is "BUILDING onward", so the guard is
wide open exactly when the check judges.

Failure when built: a run classifies a unit MISSING under M2, authors its spec — which M2 mandates —
and reaches the push boundary. The leg reds on a run that did precisely what the method told it to,
and TOOL-6 AC1 is that fixture. The prompt-authorized mode makes it worse: `check_authorization`
accepts an `authorized-by: prompt` record (`unattended.sh:786`), such a run starts with an EMPTY
units region at BASE, and every spec it legitimately authors is unaccounted for. There is no in-band
repair, because TOOL-5 S6 refuses an `add` for an id the region already carries and by check time
every authored spec is in it.

Fold-in: key the exemption on WHEN the id appeared rather than on the phase at check time. Compare
HEAD against the units region as of the commit where the run entered BUILDING, or exclude ids whose
spec was first committed before that boundary. Add a criterion observing that a fixture which
authored a spec during SPECCING and then entered BUILDING does NOT red, and a second stating that a
build whose BASE region names no unit is outside this check entirely. Rewrite F1's rationale, which
is false as it stands.

### H5 — unit 10's refusal drops M6's "together with its generator", so the ordinary declaration is refused
`2026-08-20-spec-TOOL-dUnstalledConvoy-9.md` §2 S5 with §6 AC4, §4 and §10 · lenses: contradiction,
prior-art

M6 condition 3 reads, at `memory/guides/BUILD-METHOD.md:157-158`: "neither touches a shared mutable
record — `memory/DECISIONS.md`, `memory/backlog/*.md`, the run-state file, or a generated index
TOGETHER WITH its generator." The paragraph directly below records the retraction that produced the
qualifier: "Clause 3 once named the build README outright, which was VACUOUS not strict: every pass
changes a spec header it is regenerated from. What collides is two passes RENDERING one artifact, or
one editing a generator another runs." S5 and AC4 drop the qualifier and refuse any generated-index
path outright, while §10 claims S4 and S5 quote conditions 1 and 3 rather than restating them, and
TOOL-8 S2 requires those conditions kept VERBATIM.

Failure when built: hygiene check 9 fails when the generated build index differs from a fresh render,
so every pass touching a spec status header must regenerate and commit `memory/LIVE.md`, the month
ledger shard and the build README's generated region. Under S5 the truthful declaration for the
ORDINARY pass is REFUSED, and a declaration that omits those paths is redded by TOOL-10's subset
test. The mechanism unit 3 of the roster makes MANDATORY is unusable for the common case, and the
method and its enforcing verb now say different things about condition 3.

Fold-in: restate S5 and AC4 to refuse a generated index only when the same declaration, or a
sibling's in the same group, also names its GENERATOR — quoting M6's clause rather than paraphrasing
it. Keep the flat refusal for the run-state file, the decision log and the backlog shards, which M6
does name outright. Add a criterion observing that a declaration naming a generated index ALONE is
ACCEPTED, so the retraction cannot be un-made by a later edit. S4's intersection test already catches
two passes rendering one artifact, so the flat ban buys nothing and costs the declaration.

### H6 — the derivation seam unit 10 leans on does not exist in this kit, and the conf declares two of its three sources nowhere
`2026-08-20-spec-TOOL-dUnstalledConvoy-9.md` §2 S5, §4 "Which of M6's conditions a machine can
decide", §10 Reuse audit · lenses: contradiction, unstated-assumption, prior-art

§4 says "The memory-tree conf declares the memory root, the backlog shard location and the generated
index names", S5 says the set "is derived from the memory-tree conf's roots rather than spelled", and
§10 names "the memory-tree conf loader that already resolves the memory root and the backlog location
for other checks" as an existing seam. Measured: `.memory-tree.conf` declares no backlog shard path
and no generated index names — the live index and the month ledger shard are constructed inside
`gen_build_index.py`, and the `backlog/` segment is a literal in the hygiene engine. The unattended
kit does not read that conf at all: the driver sources `.unattended.conf` alone, its only layout
value is `MEMORY_ROOT`, and neither the driver nor the leg names the decision log, the backlog, the
live index or the ledger anywhere. The cited loader is not in the tree.

Failure when built: the builder has nothing to derive from and takes one of two bad exits. Hardcoding
this repo's paths into the driver is the hardcoded-prefix class S5's own last line forbids, and lands
a dead path in every adopter whose layout differs — a class already OPEN as `TOOL-aSealedCaravan-4`.
Sourcing the memory-tree conf from the unattended driver contradicts TOOL-5 S3's ruling that each kit
is copy-installed standalone, and shelling into the generator is refused by the resolver-ban arm at
`unattended.test.sh:1582`. Either way AC7 exercises only the one value that IS derivable, so three of
the four refusal members ship unverified and the gap reads green.

Fold-in: rewrite S5 to derive what `.unattended.conf` actually declares, and add an explicit DECLARED
extension key for the rest — a shared-records list naming the decision log, the backlog root, the
live index and the ledger root, shipped with a default, with the driver refusing an undeclared one.
Correct §4 to name only the memory root and the family list as derivable, and correct §10, which
cites a seam that does not exist. Extend AC7 to a fixture whose backlog and index names differ, not
only its memory root.

### H7 — unit 11's commit range has no upper bound, so a later sequential commit is graded against a window that has closed
`2026-08-20-spec-TOOL-dUnstalledConvoy-10.md` §2 S2 and S3 · lens: unstated-assumption

S2 selects commits "reachable from the run's tip but not from the row's recorded group anchor, whose
subject names the row's unit id". TOOL-9 S2 defines that anchor as HEAD at declaration time and
records no close marker, so the range is open above. `memory/guides/BUILD-METHOD.md:136` requires the
unit id in the subject of EVERY pass commit, and M6's pass set includes "a spec reviewed" and "a
review's fixes folded in", both of which routinely happen after a concurrent group has ended.

Failure when built: two units are dispatched concurrently at one anchor, each declaring one path.
Later, sequentially, the run folds a review fix for the first and commits with its id in the subject,
touching a test file that was never in that unit's declared set. The commit is inside the range, so
S3's subset test reds at the push boundary. TOOL-10 F1's repair is explicitly scoped to before the
commit, so after the fold the row is already violated, and the alternative — declaring ever-wider
sets up front — empties the disjointness proof of its meaning.

Fold-in: bound the range above. Record a group CLOSE anchor when the concurrent group ends and select
the anchor-to-close range only; or restrict the selection to the FIRST commit after the anchor naming
each unit id and state in S2 that later commits for the same unit are outside the group by
construction. Add a criterion observing a fixture with a post-group sequential commit passing.

### H8 — unit 2's second arm is decided before it reads anything, on the only path the verb is ever invoked
`2026-08-20-spec-TOOL-dUnstalledConvoy-1.md` §2 S2, §4 Inventory, §6 AC2 and AC3 · lenses:
unstated-assumption, prior-art

S2's second arm tests that HEAD is an ancestor of the local default branch. `verb_landed`'s own
header records why it does not call the branch guard: "Landing happens ON the default branch, because
the mandated lander refuses to run anywhere else" — and `tools/push-main.sh:36-40` does refuse,
comparing the checked-out branch against the default and exiting. On that path HEAD IS the local
default-branch ref, and a commit is its own ancestor, so the arm exits 0 unconditionally. §4 prices
the arm's weakness as forgeability by a ref write; the real cost is that no forgery is needed,
because the two operands are the same commit. This is the catalogued
`assertion-between-two-derived-values` class, whose recorded first instance is this same kit.

Failure when built: `check-arms.py` scores the branch ARMED because AC2's and AC3's fixtures stand
somewhere the lander would have refused, and every real landing takes arm 2 the moment the remote arm
fails. LANDED becomes reachable from a clean tree standing on local main with no assertion that the
run's own work is on it, and the witness recorded is main's tip rather than the run's work.
`TOOL-aPacedTurnstile-15` records the live shape this matters for: a primary tree clean and on main
carrying eleven unpushed commits, three of them another build's unreviewed work. This is not the
owner's fork-D decision restated — the owner accepted a local-main witness, not a vacuous one.

Fold-in: anchor arm 2 on a value the run does not trivially satisfy. Assert that the run's OWN branch
tip is an ancestor of the local default branch — false when nothing was merged, true when it was —
and name that ref in S5's refusal text. Alternatively state plainly in S2 and §4 that arm 2 is a
RECORD of the invocation state rather than a test, drop the ancestry language, and make the
observable content the unpushed count plus the anchor kind. Then state in §4 that the arm's failing
case must be observed with the run standing ON the default branch, because a fixture standing off it
cannot distinguish this arm from one that was never called.

### H9 — unit 6 needs a local default-branch NAME the leg does not hold, and the two obvious substitutes are the two the kit banned
`2026-08-20-spec-TOOL-dUnstalledConvoy-2.md` §10 Reuse audit with §2 S2 · lenses: prior-art,
unstated-assumption

§10 states "The local branch name comes from the same symref the loop already reads, so no new
resolution path is introduced." Measured: `check-unattended.sh:231-232` runs the remote symref
advertisement into a variable and keeps only the SHA where the ref is HEAD; the ref NAME line is
never bound to anything. Grepping the whole leg for a default-branch name, a heads or remotes ref, or
the environment override returns the advertisement call and two COMMENTS — one of which, at line 342,
records that `TOOL-aStandingWrit-6` deliberately purged those reads from the BASE path because the
run can write both. The leg holds no default-branch name at all.

Failure when built: S2 needs a local ref to test ancestry against and §10 has told the builder the
value is to hand. It is not. The builder reaches for the environment override or the remote-tracking
ref — the two the kit banned as a reproduced bypass — on the very check that grades a terminal claim;
or hardcodes the name, which reds on any adopter whose default branch is called something else.

A second half is verified separately: the predicate becomes per-clone while its subject travels. The
run-state file is tracked and reaches every node; a local default-branch ref does not. Node `d` lands
locally and commits a local-witness record; node `b` pulls the branch without fast-forwarding its own
default branch, and the same leg reds there on a record that is green where it was written. The leg's
own comment at line 428 states the intent this defeats — "What makes it one is running this same leg
in a clone the run never touched" — and its population includes frozen terminal records from other
nodes.

Fold-in: add a scope item parsing the symref NAME out of the existing advertisement into its own
variable beside the SHA, and resolve the local ref from that. Correct §10 to say a new resolution
path IS introduced, that it derives from the remote advertisement and nothing local, and cite
`TOOL-aStandingWrit-6` as the reason no other source is admissible. Then decide the per-clone
question in S2: either pass when ancestry holds against EITHER the advertised tip or the local
branch, or scope the local arm to the node named in the record and skip elsewhere through the
announced-skip mechanism this unit is already adding.

### H10 — unit 7's shipped rule delegates all of veto 2, and both carve-outs live only in spec commentary
`2026-08-20-spec-TOOL-dUnstalledConvoy-4.md` §2 S2 with §4 "Line budget" and §4 "Why the goal
statement is the invariant" · lenses: unstated-assumption, contradiction

S2 states the bound as ONE invariant — only the build README's goal statement may not be amended —
and says this "replaces veto 2's owner turn for changes made in service of the stated goal". Veto 2
reads, at `BUILD-METHOD.md:73`: "needs a new external dependency, install location, public surface,
or a change to a governance carrier". As written, the M3 text this unit ships delegates dependency,
install-location, public-surface and governance-carrier changes whenever the run judges them
goal-serving — a purpose test the run applies to itself. That is far wider than the owner's recorded
fork A, which is scope authority over UNITS.

The bound the author intended does exist, but only in §4: "a veto this unit deliberately does NOT
relax for M1 itself, since a run raising the budget of the file that states its own limits is the
circularity the whole rule exists to prevent." Spec commentary is not a carrier. A future run reads
M3, not this spec.

Failure when built: this build is the first case. Units 7 and 3 of the roster share seven lines of
headroom in `BUILD-METHOD.md` — measured now, 283 lines against M1's 290. If the pair does not fit,
raising M1's budget is unambiguously in service of the stated goal, so the amended M3 authorises the
run to raise the constant that bounds it. The README's own build-level rule depends on the un-relaxed
veto — "M1's budget is a stated constraint of a governance carrier, and M3 veto 2 makes changing one
an owner turn" — and stops being true in the tree the moment this unit lands. More generally, an
unattended run gains authority to edit the charter, the hygiene document or the shipped template with
no owner turn.

Fold-in: write both carve-outs into S2's rule TEXT, not the commentary. The delegation covers the
build's own scope — retire, supersede, add units and their spec content — and explicitly does NOT
reach veto 2's governance-carrier clause, M1's own budget included. Keep the goal-statement invariant
as a second bound rather than the only one. Both belong in the sentence that gets written into M3.

### H11 — M12 restates the rule unit 7 deletes, and unit 7 declares M12 out of scope on a false ground
`2026-08-20-spec-TOOL-dUnstalledConvoy-4.md` §3 Non-goals ("Any change to M12") · lens:
unstated-assumption

§3 puts M12 out of scope on the ground that "Its closing line already defers to M3's limit on
authority, and it inherits whatever M3 says without an edit." Only the first clause defers.
`BUILD-METHOD.md:278-279` reads: "M3's limit on your authority holds here too — a candidate set whose
options differ in WHAT GETS BUILT is a scope fork, and scope is not delegated." The trailing clause
RESTATES the substantive conclusion in its own words, so it inherits nothing.

Failure when built: S1 deletes M3's park sentence and AC1's grep for that sentence passes, while line
279 still tells every reader — and every unattended run doing M12 candidate research — that scope is
not delegated. The method then carries two contradictory answers to one question inside one file,
which M1 names as a defect HERE whose resolution is deletion, and a run reading M12 during a research
pass parks the fork this build exists to unpark. AC1 cannot catch it: it greps for M3's sentence,
whose bytes differ from M12's.

Fold-in: add M12's trailing clause to S1's edit set — replace "and scope is not delegated" with a
pointer to M3, so the rule has exactly one home — and add a criterion asserting the second spelling
is gone. Re-measure the line budget with the edit included; as a same-line replacement it should be
net zero or negative.

### H12 — the kit-version bump lands one commit before the engine edit, which is the one order `verdict epoch` refuses
`2026-08-20-spec-TOOL-dUnstalledConvoy-11.md` §2 S7 and §6 AC5, with `...-12.md` §4 Files touched and
§7 Gates · lens: unstated-assumption

`tools/memory-tree/check-verdict-epoch.sh:68` names `check-memory-hygiene.sh` as the ENGINE, and its
header states the rule as topological: the NEWEST commit in the range that moves a behaviour-bearing
line of the engine must be an ancestor of, or equal to, the NEWEST commit that changes the kit
version constant. TOOL-11 S7 and AC5 put the marker bump and its carrier sweep in that unit's commit.
The README's total order runs unit 12 of the roster then unit 13, and TOOL-12 S1 adds a check to the
engine file itself.

Failure when built: the engine moves AFTER the bump, so the newest engine commit is a descendant of
the bump commit, and the `verdict epoch (kit version dates the engine)` leg reds at the push boundary
with a message about a constant that does not date its verdicts. The repairs are a SECOND bump, which
means sweeping every kit-version marker a second time, or reordering after the fact. TOOL-12 §7 lists
`memory-tree hygiene`, `memory-tree hygiene selftest`, `harness arms`, `kit version markers` and the
full bar, with no `verdict epoch` — so the build meets this red without having predicted it. TOOL-11
§7 does name the leg, which is what makes the omission easy to miss: the unit that names it is not
the unit that trips it.

Fold-in: move the version bump and the marker sweep out of TOOL-11 S7 into TOOL-12, or into a single
final commit landing after the engine edit, and state in BOTH specs that the bump must be the LAST
commit of the pair. Add `verdict epoch` to TOOL-12 §7. Note in both that the bump has to be
re-checked against any later engine-touching commit in the same range.

### H13 — unit 4's Skill-pair obligation names three mechanisms and none of them is the one that grades it
`2026-08-20-spec-TOOL-dUnstalledConvoy-3.md` §2 S6, §6 AC6, §7 Gates · lenses: contradiction,
underspecification

S6 says both templates "move in the SAME commit as their installed renders, because check 10
byte-compares each pair". Check 10 compares ONE pair: `check-unattended.sh:534` reads "10: the kit
ships what this repo runs. ONE pair", and its failure text names only the shipped protocol and this
repo's installed copy. The Skill template is not byte-identical to its render — it carries
interpolated deploy tokens — so a byte comparison of that pair can never pass. AC6 names
`bash tools/check-wiring.sh --check` as the observation; that script's Skill check reads line endings
and NUL bytes only, and running it reports hooks, agent-cap, scratch, recall, the merge driver, EOL
and the kickoff engine, never the unattended Skill render. §7 then lists `memory-recall skill
wiring`, which belongs to a different kit. The real grader is
`bash tools/unattended/adopt-unattended.sh --check`, wired as the leg `unattended skill wiring`, and
that leg is named by no §7 in this build — including TOOL-5, TOOL-8 and TOOL-9, which all list the
Skill pair in Files touched.

Failure when built: the builder edits the Skill template, sees check 10 green and the wiring check
green, records AC6 satisfied, commits, and reds a leg at the push boundary that no spec in this build
names. A stale render ships; a hand-edited one is exactly the second copy §4 says this unit exists to
avoid.

Fold-in: rewrite S6 so the Skill pair is a RENDER compared by the adopter's check mode after
re-running the adopter, and the protocol pair alone is check 10's. Change AC6 to that command. Add
`unattended skill wiring` to §7 of roster units 3, 5, 8 and 10, and drop `memory-recall skill wiring`
from TOOL-3 §7.

### H14 — unit 3 owes a rescope row at build position 3, while the authority and the verb land at positions 7 and 8
`2026-08-20-spec-TOOL-dUnstalledConvoy-8.md` §2 S6 · lens: contradiction · **raised as BLOCKER,
downgraded because the row can be back-filled one pass before the check lands — an improvisation the
spec does not authorise**

S6 says that if the measurement records E3 or E4 as FAILED, this unit ships the recorded loss
instead, its status goes WONTDO, "which is an amendment under `TOOL-dUnstalledConvoy-4` and owes a
`rescope` row". The README's total order puts this unit at position 3, the authority at position 7
and the verb at position 8.

Failure when built: the measurement records E4 FAILED — S4 aims that test straight at two recorded
merge-driver defects, so it is the likely branch, not the exotic one. At position 3, M3 still reads
verbatim "a fork whose options differ in what gets built is not yours — park it", and
`unattended.sh:2037` answers a rescope call with "unknown argument; the verbs are --preflight,
--plan, --phase, --status, --resume, --close, --landed, --park and --abort". The run's only legal
moves are to park — the exact stall recorded for `dClosedLexicon`, `aWalkedCorpus` and
`cBriefedPilot` — or to flip the status with no record, which the roster check at position 9 then
reds on for the rest of the build. It also breaks M2's cross-read axis "no sub-spec depends on a unit
sequenced after it", which M2 says to fix before the first code pass.

Fold-in: move the authority and the verb ahead of the measurement in the README's total order — they
are prerequisites of the only conditional unit in the build — or rewrite S6 so the failed-measurement
branch PARKS with a park row and defers the status flip and the amendment row to a follow-on pass
after the verb lands, saying so in S6 and AC6. The same reordering closes M11 below.

---

## MEDIUM

### M1 — unit 3 branches on a two-valued reading of a three-valued vocabulary, so an unmeasured criterion ships the inversion
`2026-08-20-spec-TOOL-dUnstalledConvoy-8.md` §2 S6 and §6 AC6, with `...-7.md` §6 AC5 and §2 S5 ·
lens: underspecification

S6 branches on the measurement recording E3 or E4 "as FAILED". TOOL-7 AC5 declares a THREE-valued
per-criterion vocabulary — CLEARED, FAILED or NOT OBSERVED — and TOOL-7 §5 explicitly preserves the
third for a test that cannot run. TOOL-7 §4's losing-conditions table catches some cannot-run causes
and records them as losses, but not all: a blocked worktree creation, budget exhaustion, or a
deferred half of the E4 test land on NOT OBSERVED, S6's condition is then false, and the inversion
ships on a criterion the owner's fork-B decision said must be measured first. Separately, TOOL-7 S5
promises "a single verdict token on its own line" whose legal values are enumerated in neither spec.

Fold-in: one sentence in TOOL-8 S6 treating NOT OBSERVED on E3 or E4 as a non-shipping outcome,
identical to FAILED for this branch, with AC6 amended to match. Declare the closed verdict-token set
in TOOL-7 S5 and add a criterion asserting the emitted token is one of that set.

### M2 — dropping the unit id from a commit subject evades unit 11's whole check, and the evasion looks like the benign case
`2026-08-20-spec-TOOL-dUnstalledConvoy-10.md` §2 S4 with §6 AC3 · lens: underspecification

S2 joins a declaration to commits "whose subject names the row's unit id", and S4 makes a dispatch row
with NO matching commit an announced observation rather than a refusal — justified by M6's rule that
a pass producing no change commits nothing. Those are the same observation: "the pass committed
nothing" and "the pass committed with an id-less subject" produce one identical line. M6's
id-in-subject rule is an instruction with no enforcement anywhere in the tree — no gate reads commit
subjects — so the second case is reachable by accident as well as by design. §4's own vacuity-risk
section enumerates every other empty-comparison route and misses this one; AC3 exercises only the
benign reading.

Fold-in: split the case. Make it a REFUSAL when the commit range between the group anchor and the tip
contains a commit whose subject names no unit id from the group; keep the announced observation only
for a genuinely empty range. Add one criterion per branch — a fixture whose pass committed with an
id-less subject redding, and a fixture with an empty range announcing.

### M3 — two of unit 4's scope items have no criterion, and the parity criteria that stand in for them are true of an untouched pair
`2026-08-20-spec-TOOL-dUnstalledConvoy-3.md` §2 S1 and S5 · lens: underspecification

The criterion set walks the scope list and skips exactly two items: S1, that protocol section 3
states the terminal is reachable on either anchor and that the run-state file records which; and S5,
that the Skill's landing section states the fallback and the two new facts. AC1 and AC6 are parity
checks, and check 10 is a byte diff that is green whatever both sides say and green if neither moved.

Failure when built: the builder edits protocol sections 6, 8 and 9, re-renders, and stops. Every
criterion passes. The protocol's phase section still describes the terminal as remote-observed and
the Skill still tells an operator the only way to land is a remote ancestry test — so the two
documents an unattended run reads at landing time never learn about the arm units 2 and 6 shipped,
while the unit reports every criterion green.

Fold-in: add one criterion per item, in the shape the other five already use — protocol section 3
names both anchors and the recorded anchor-kind fact, observed by grep in the installed protocol; and
the Skill's landing section names the local fallback, both new facts and the pointer to section 9,
observed in the rendered Skill.

### M4 — units 8 and 10 edit the Skill and the protocol without those documents appearing in scope, criteria, gates or the read-path budget
`2026-08-20-spec-TOOL-dUnstalledConvoy-5.md` §4 Files touched and `2026-08-20-spec-TOOL-dUnstalledConvoy-9.md`
§4 Files touched · lens: underspecification

Both tables edit the unattended Skill template and its render, and the installed protocol and its
template. Neither document appears in either spec's §2 Scope, in any criterion, or in §7 — and
`unattended skill wiring` is named by neither. TOOL-5 §5 even claims "the Skill section and the
protocol verb row, in S-scope above", which S1 through S9 do not contain, so the spec contradicts
itself. Separately, the installed protocol is one of the six read-path files (measured: 32 258 B of a
105 944 B path against a 112 987 B ceiling), and the README's build-level rule requires every unit
touching a budgeted carrier to re-measure from its gate. Roster units 4 and 7 carry that criterion;
these two do not.

Failure when built: a builder implements the scope items and ships the verb with no Skill section and
no protocol verb row. Every criterion passes and every named gate is green, because an untouched
template still matches an untouched render. The two documents an unattended run reads to learn which
verbs exist never gain the two verbs this build adds, so the mechanism ships undiscoverable.

Fold-in: promote the Skill section and the protocol verb row into §2 of both specs, give each a
criterion greping for the verb in the rendered Skill and in the protocol's verb section, add
`unattended skill wiring` to §7, and add the read-path re-measurement criterion that roster units 4
and 7 already carry.

### M5 — a declared path containing a space is neither refused nor escaped, and this repo has hit that class twice
`2026-08-20-spec-TOOL-dUnstalledConvoy-9.md` §4 Data model with §2 S7 · lens: underspecification

The row grammar puts the declared path list in a whitespace-delimited free-text field with no quoting
or escape defined. S7 refuses an absolute path, a parent-directory path and an empty declaration; S8
inherits refusals for a newline and for the field separator. Nothing reaches a space, and no criterion
covers one. `tools/check-wiring.sh` carries two comments recording this repo hitting the class — a
path with a space word-split into two nonexistent paths, reported as a green skip over a population
of zero.

Failure when built: a pass declares a path under a directory whose name contains a space. The verb
accepts it and writes one row. Unit 11's subset test splits the field on whitespace, gets two tokens
naming nothing, and every path the pass actually commits falls outside the declared set — so a
CORRECT dispatch reds the bar with a message naming paths that were never declared.

Fold-in: add a refusal in S7 for any declared path containing whitespace, with its own criterion; or
declare an explicit separator for the path list in §4 and use it on both sides, in the verb and in
unit 11's parser.

### M6 — unit 3 points M6 at a verb that lands nine passes later, so the rule ships inert with a dead pointer
`2026-08-20-spec-TOOL-dUnstalledConvoy-8.md` §2 S4 · lens: contradiction · **raised as BLOCKER,
downgraded because the obligation is conditional on a proof the run cannot record, so the method
falls back to sequence rather than self-contradicting**

S4 has M6 state that the proof is RECORDED, pointing at the verb roster unit 10 builds. That unit is
position 10 in the total order and this one is position 3; the dispatch verb does not exist today.
M7 makes the run re-read the method WHOLE at every pass boundary, so from this commit onward the run
itself reads a method section pointing at a flag no reader can invoke, for nine passes.

Fold-in: sequence the verb before this unit, or make S1's obligation explicitly conditional on the
recording verb being present and say in S4 that the pointer is inert until that unit lands. The
reordering proposed in H14 resolves this one too if the dispatch verb moves with it.

### M7 — `.memory-tree.conf` is an undeclared member of seven units' write sets
`2026-08-20-spec-TOOL-dUnstalledConvoy-1.md` §4 Files touched, and the identical shape in `...-2.md`,
`...-5.md`, `...-6.md`, `...-9.md`, `...-10.md` and `...-12.md` · lens: contradiction

Seven specs put the arms-floor bump inside the row for a test file. That constant is declared at
`.memory-tree.conf:178`. No spec except TOOL-11 names that file in its Files-touched table at all, and
TOOL-11 names it for a different key. Several §7 sections make the intent explicit, so the conf edit
is certainly in those units' write sets.

Failure when built: the specs' own path inventories are wrong about a file seven of thirteen units
share, and those tables are the only written path lists this build has — the very lists roster unit
10's intersection refusal and unit 11's subset test are meant to be validated against. Any two of the
seven pass the intersection refusal, get dispatched concurrently, and then either race the same
declaration line or are redded for committing an undeclared path.

Fold-in: add a `.memory-tree.conf` row to the Files-touched table of all seven specs, naming the
arms-floor entry each one moves, and note in the README's build-level rules that this conf is a
build-wide shared write making those seven units mutually non-disjoint.

### M8 — the check inventory two units owe a row to does not exist, and the unit they delegate it to never creates one
`2026-08-20-spec-TOOL-dUnstalledConvoy-6.md` §5 and `2026-08-20-spec-TOOL-dUnstalledConvoy-10.md` §5 ·
lenses: contradiction, unstated-assumption, prior-art

Both discharge their user-documentation obligation with a row in "the protocol's check inventory,
alongside `TOOL-dUnstalledConvoy-3`". The installed protocol has ten sections — the authorization,
the run-state file, the phase vocabulary, the Definition of Done, the keepalive, landing, the verbs,
what a project declares, the boundary the kit claims, the default directive set — and none is a check
inventory; grep for check numbers returns nothing. Roster unit 4's scope covers protocol sections 3,
6, 8 and 9 plus the Skill and the conf example, and it lands five and nine passes earlier. Neither of
these two specs names the protocol template in its own Files-touched table.

Failure when built: two new leg checks land with no contract text anywhere, because each unit
believed another owned the write-up and the section they both name does not exist. The honest
alternatives at that point are an unscoped eleventh protocol section against a read-path margin the
build is already spending, or shipping undocumented.

Fold-in: pick one and say so in both specs. Either drop the line and state that a leg check's
documentation is its own source header — which is what the leg does for all twenty-one existing
checks, and what TOOL-6 S7 and TOOL-10 S7 already require — or scope a real carrier, name the section
each row joins, price it against the read-path ceiling in the unit that writes it, and add the
protocol template pair to that unit's Files-touched table.

### M9 — two specs claim a conf-axis check that does not exist, and split one key's three carriers across two units
`2026-08-20-spec-TOOL-dUnstalledConvoy-2.md` §2 S6 and §6 AC7, with `...-3.md` §2 S3 and §5 · lenses:
contradiction, unstated-assumption, prior-art

TOOL-2 S6 claims all three carriers for the new cutoff key — the project conf, the protocol's key
table and the shipped conf example — while TOOL-3 S3 claims two of them, and TOOL-3 lands first. Both
then lean on a check that is not in the tree: AC7 asserts "the conf-axis check that pairs those three
stays green" and TOOL-3 §5 says the same. The only arm reading the shipped conf example iterates key
NAMES and asserts the DRIVER defaults each in its init block, skipping any key the driver does not
reference; the new key is read by the LEG, so that arm skips it entirely. Nothing anywhere joins a
conf key to the protocol's key table — `TOOL-cSettledDocket-14` is the OPEN row proposing exactly
that gate, and two existing keys are missing from the table today with the bar green.

Failure when built: the example and the protocol table document a key with no declaration and no
reader for two passes, and AC7 is recorded green against a gate that performs no such pairing — the
same defect the OPEN row records, in the same kit, one key later.

Fold-in: give all three carriers to the unit that adds the READER and delete them from TOOL-3 S3.
Replace AC7's last clause with three direct observations — the key present in the project conf, in
the shipped example, and in the protocol's key table, each asserted separately. Correct TOOL-3 §5 to
say the pairing is unchecked and cite the open row. Optionally, make the missing arm part of this
build: it would red immediately on the two keys already absent, which is a failing case observed for
free.

### M10 — the two new cutoff keys have no stated blank-or-absent semantics, and the leg runs under an unset-variable trap
`2026-08-20-spec-TOOL-dUnstalledConvoy-2.md` §2 S4 and S6, with `...-6.md` S6 · lens:
unstated-assumption

Both units introduce a conf key into `tools/unattended/check-unattended.sh`, which runs with unset
variables fatal and pre-declares every conf key it reads in one init block that names neither key.
Neither spec states what an ABSENT or BLANK declaration resolves to, and blank is the adopter's
state: the shipped example ships one of these keys blank and documents blank as an OFF switch, while
the memory-tree conf's sibling key documents the opposite — a blank resolves FORWARD to the shipped
date, precisely because an empty string compares earlier than every date.

Failure when built: an adopter whose conf predates the key runs the bar and the leg dies on an
unbound variable before any check reports — a broken gate rather than a named refusal. If the builder
defaults it to empty instead, the key is a SELECTOR rather than an on/off switch, so blank either
refuses on every record including the frozen ones or silently means never-required, and the check
ships always-on or always-off for every adopter.

Fold-in: state the blank resolution per key, in the shape the memory-tree conf already uses for a
filename-date key, and add both keys to the leg's init block in the Files-touched table. Add an arm
to the leg's sibling test mirroring the driver's defaulted-key arm, so the leg gains the coverage the
driver already has.

### M11 — unit 2's fork is resolvable only under an authority that lands five passes later
`2026-08-20-spec-TOOL-dUnstalledConvoy-7.md` §8 F1 · lens: contradiction

F1 closes with "It is a scope fork under `TOOL-dUnstalledConvoy-4`'s new authority, so a run may
resolve it — and it must record the resolution as an amendment." This unit is position 2 in the total
order; the authority is position 7 and the recording verb is position 8. At position 2, M3 still says
a scope fork is not yours to take, and the verb does not exist. The run parks, which stalls the
conditional chain before it starts. Parking carries a second cost: the spec format requires §8
resolved before a status may go CLOSED, machine-checked, so a parked fork also keeps this unit
non-terminal and blocks the build-complete item.

Fold-in: resolve F1 to a fixed disposition before the build starts, or reorder so the authority and
the verb precede the measurement. The reordering in H14 covers both.

### M12 — unit 8's `add` refusal and its idempotence rule cannot both hold, and §4 does not order the guards
`2026-08-20-spec-TOOL-dUnstalledConvoy-5.md` §2 S6 against S8, with §4 Inventory of refusals · lenses:
unstated-assumption, prior-art

S6 makes an `add` refuse a unit id the generated units region already carries; S8 claims the verb is
idempotent "so a resumed run that re-derives the same amendment does not duplicate the row". The
region is rendered from the specs that exist, so the moment the amendment is performed the id IS in
the region. §4's refusal inventory does not order the guards, and the verb this one inherits from
places its exact-line compare LAST, after every refusal.

Failure when built: a run adds a unit in the natural order — authors the spec, renders the index,
commits, then records the row, which the records-current item pushes it toward in the same commit.
The refusal fires permanently, while unit 9 of the roster demands that row permanently, and unit 7
makes removal structurally refused. The exits are hand-writing the row or leaving the leg red, which
is the wedge shape this build exists to remove.

Fold-in: order the guards explicitly in §4 — run the exact-line idempotence compare FIRST and return
the no-op before any region-membership test — and restate S6 as: an `add` for an id already in the
region AND already carrying a matching row is a no-op; without a matching row it is a refusal. Or
drop S6 and let unit 9's transition check be the sole judge, since it is the one with an independent
second input. Whichever is chosen, state the ordering in the verb's own steps and correct S6's stated
rationale, which describes a transition that DID happen.

### M13 — unit 13's population has no tier filter, so a Tier-1 spec that is legal under the format reds the gate
`2026-08-20-spec-TOOL-dUnstalledConvoy-12.md` §2 S2, S3 and S5 · lens: unstated-assumption

S2's population is every CLOSED spec at or after the cutoff with no tier filter; S3 sources the
criterion set from "the spec's §6"; S5 makes a spec with no criterion labels a REFUSAL.
`memory/TEMPLATE-SPEC.md` gives Tier-1 a light profile in which the section canon is not enforced, so
a Tier-1 spec's §6 need not be Acceptance criteria at all — two closed Tier-1 specs in this corpus
number their criteria under §5 and carry Gates at §6. The sibling witness rule already avoids this by
keying on the HEADING TEXT rather than the number, with one regex covering all three sanctioned label
spellings, a few hundred lines above where the new check goes.

Failure when built: an implementer reading §6 by NUMBER scans a Tier-1 spec's Gates section, finds no
labels, and reds a spec that is legal under the format the same gate enforces. S5 also silently makes
an acceptance-criteria section mandatory for Tier-1 specs, which the format does not require and this
build never states as a format change.

Fold-in: scope S2 to Tier-2 specs, or to specs that actually carry an acceptance-criteria heading.
Re-word S3 and S5 to key on the heading TEXT using the same regex the witness rule uses, extracted
into one shared fragment so the two checks cannot disagree. Say in S5 that the refusal is for a
Tier-2 spec whose acceptance-criteria section names no label, which is a real defect.

### M14 — two reuse audits record a seam the leg does not have, so the builder writes a second id regex one file away
`2026-08-20-spec-TOOL-dUnstalledConvoy-10.md` §10 and `2026-08-20-spec-TOOL-dUnstalledConvoy-6.md` §10 ·
lens: unstated-assumption

TOOL-10 §10 states "The id shape comes from the driver's own `_ids_of` spelling, which the leg already
mirrors." Grepping the leg for that helper returns nothing, and the leg carries no id pattern of any
kind. TOOL-6 has the same unmet dependency — S2 derives two id SETS from the units region — and its
§10 cites only the anchor loop and the region helper.

Failure when built: the builder discovers mid-unit that the id grammar has to be introduced into the
leg for the first time and writes a second spelling of the driver's regex one file away. That is the
class the leg's own header names: "THE CORE SETS ARE READ FROM THE DRIVER, never restated here. A
second spelling is the drift this leg exists to catch." The reuse audit that should have caught it
recorded the opposite of what is in the tree.

Fold-in: correct both §10 sections, and specify the seam the leg does have — it already parses the
driver's core sets out of the driver source, and the id pattern can ride the same parse, or become a
named driver constant the leg extracts. Whichever is chosen, name it in the Files-touched table,
because it is a driver-side edit and not only a leg edit.

### M15 — unit 3's fourth criterion names a joint state that does not exist at its own pass
`2026-08-20-spec-TOOL-dUnstalledConvoy-8.md` §6 AC4 · lens: contradiction

AC4 measures the method file "after this unit AND `TOOL-dUnstalledConvoy-4` have both landed". This
unit is position 3 and that one is position 7, so the observation cannot be taken at this unit's
Definition of Done. The spec format requires each criterion to be an observation that proves THIS
change works. The knock-on is real but bounded: once the ledger check lands, a CLOSED spec owes a
line per criterion, so an unobserved one has to be carried as an amendment.

Fold-in: scope AC4 to this unit's own three-line share measured at its own commit — S7 already states
that share — and move the joint file-wide assertion into `TOOL-dUnstalledConvoy-4` §6, which is the
later of the pair and already measures the file after its edit.

### M16 — unit 3's second criterion is a diff assertion over a paragraph that must reflow
`2026-08-20-spec-TOOL-dUnstalledConvoy-8.md` §6 AC2 · lens: unstated-assumption

AC2 verifies that M6's three conditions are unchanged by showing "no change inside the numbered
list". There is no numbered list. `BUILD-METHOD.md:154` carries the framing sentence S1 replaces AND
the opening of condition (1) on one line, and conditions (2) and (3) are continuation lines of the
same hard-wrapped paragraph through line 159. Any correct implementation changes line 154 whatever
the new sentence's length.

Fold-in: restate AC2 as a CONTENT assertion rather than a diff assertion — extract the paragraph,
strip newlines, and assert the substring from the conditions' opening through their closing sentence
is byte-identical to the same substring at BASE. That is checkable, survives reflow, and is what S2
actually means. Correct §4's "three numbered conditions", which is what the criterion inherited.

### M17 — unit 7 writes an unconditional structural refusal into the method that this repo's own anchor setting does not provide
`2026-08-20-spec-TOOL-dUnstalledConvoy-4.md` §4 "The three acts, and the one refusal" · lens:
unstated-assumption

The §4 table marks DELETE "no — structurally refused" without qualification, and S4 writes that
reason into M2, a governance carrier shipped to every adopter. The refusal is conditional on the
anchor, and this repo declares the weaker one. `check_authorization`'s own comment says so: on the
default-branch anchor the BASE blob is outside the run's reach and it is a real integrity check; on
the branch anchor it is NOT, because the run pushed that tip, and the comment closes "This check does
not close that hole and must not read as though it did." `.unattended.conf` declares the branch
anchor.

Failure when built: the method publishes a guarantee the code explicitly disclaims, in the exact
words the source says it must not read as. Under the weaker anchor a run can push its branch, pin the
BASE to the tip it just pushed with an id already absent, and the subset test compares a BASE the run
authored.

Fold-in: qualify S4 — the removal refusal binds on the default-branch anchor and degrades on the
branch anchor, per the protocol's own boundary section, so a project running the weaker anchor relies
on the run not to delete rather than on the check to refuse it. One clause keeps M2 true for both
adopter configurations.

### M18 — the one scope item that bounds the delegated authority has no criterion
`2026-08-20-spec-TOOL-dUnstalledConvoy-4.md` §2 S2 · lens: underspecification

S2 is the entire bound on the owner's fork-A decision and is what makes "inside the stated goal" a
rule rather than a phrase. The criterion set walks the rest of the scope list and skips it: the
criteria observe the deleted park instruction, the amendment acts, the no-removal rule, the two
budgets and the four-act table, and none observes that M3 STATES the invariant.

Failure when built: the builder rewrites M3's delegation paragraph to delegate scope, which two
criteria reward, and omits or softens the goal-statement invariant. The method then delegates scope
with no stated bound, and no gate notices, because the invariant was never observed anywhere. The
spec's own §5 names the matching risk — a run amending its way out of a hard problem.

Fold-in: add a criterion greping the method file for the invariant — that a run may not amend the
build README's goal statement, named as the bound on delegated scope — and a second asserting vetoes
1 and 3 survive verbatim.

### M19 — the kit README carries the hygiene check count and no spec names it
`2026-08-20-spec-TOOL-dUnstalledConvoy-12.md` §4 Files touched · lens: prior-art

The Files-touched table lists the gate leg's NAME conditionally, "only if it states a check count".
The leg is named `memory hygiene` and carries no count, so that row resolves to nothing. The count
lives at `tools/memory-tree/README.md:18` — twenty-one checks with a numeric breakdown partitioning
them across the shell and four delegates — and a second copy sits in the codebase-map dossier for
this gate. Grep across all thirteen specs finds no README reference, and there is no count-parity
gate anywhere, so a twenty-second check leaves both numbers and the partition silently wrong. Two
OPEN rows already record this class, and the charter states the rule from the other side: no count of
a derived population is written in prose.

Fold-in: replace the conditional row with the kit README named outright, stating which numeric range
the new check takes and which delegation clause its breakdown joins, and name the dossier as the
second carrier. Add a criterion greping the README for the new count. Note in §4 that the charter's
claim about the gate-leg name stating a count is stale, since the leg name states none.

---

## LOW

### L1 — the honest-limit header is a build-level rule and a scope item in seven specs, and no criterion observes it
`README.md` build-level rules, with `...-1.md` §5, `...-2.md` §4, `...-5.md` §4, `...-9.md` §4,
`...-6.md` S7, `...-10.md` S7 and `...-12.md` S8 · lens: underspecification

The README makes the header disclosure a build-level rule and seven specs restate it. Not one carries
a criterion that observes the header text exists. In four of the seven it is a numbered SCOPE item,
and the spec format binds every scope item as verifiable at the Definition of Done, so a builder
skipping it has skipped scope rather than merely a criterion — which is why this is LOW rather than
higher. The cost if it happens is a missing paragraph in a shell comment, repairable at any time.

Fold-in: one criterion per spec, of the shape "the header of the new check or verb states the named
limit, observed by grep".

### L2 — the README's list of template-and-render units names four, and six carry the coupling
`README.md` build-level rules, read against `...-5.md`, `...-9.md` and `...-11.md` §4 Files touched ·
lens: unstated-assumption

The rule "a kit-shipped document and this repo's installed copy are ONE mechanism" enumerates units
3, 4, 8 and 12. Measured from the Files-touched tables, roster units 8 and 10 each move the Skill pair
AND the protocol pair, and roster unit 12 moves two pairs of its own — six units carry the coupling.
It is also a derived list written in prose beside the thing it counts, the class this repo gates
against elsewhere. Each unit's own table is correct, so the misleading text is the planning rule
rather than the operative list.

Fold-in: drop the enumeration and state the rule generally — any unit whose Files-touched names a
kit template moves its render in the same commit.

---

## REFUTED — 44 findings dropped, so the next round does not re-find them

Each line is a raised finding and the reason it did not survive. Where a residual worth taking
survived the refutation, it is named. The 44 refutations collapse to 37 lines the same way the
confirmed set collapses: several were raised by more than one lens against the same text, and those
lines say so.

- PLAY-1 S1/AC1 keeps the trailing "where no hook reaches" clause — refuted three ways: S2 requires
  the ACTUAL reason written "in place of the false one", §3's non-goal forbids upgrading unmeasured
  to does-not-fire, and AC3 forbids the bullet claiming a hook fails to fire in a sidechain. Raised
  three times by three lenses; refuted three times. Residual: AC1's grep could name both strings.
- PLAY-1 AC6 pre-decides an open fork about which backlog shard owns the row — the method sweeps §8
  before any code and requires a rev bump to diverge, so the resolution precedes the measurement.
  §4 already hedges both shards.
- TOOL-8 AC4 and TOOL-4 §4 leave the joint line budget unmeasured — refuted by the ordering itself:
  TOOL-4 is the SECOND lander and its own criterion measures the file after both edits. Survives in
  weaker form as M15 above, which is about the criterion's phrasing, not the coverage.
- TOOL-6 S6 announces four skip cases and only one has a criterion — AC7 sweeps "each skip" over a
  closed enumerated set, so the population is bounded and the sweep is not vacuous.
- TOOL-5 S3 and TOOL-9 S3 have no criterion for a malformed id — §4's refusal inventory lists it and
  a blanket criterion observes each new refusal RED before landing.
- TOOL-2 S4 leaves the no-committed-blob window undefined — that state is unreachable for a landed
  record, and the pre-driver case is exactly the spec's own before-the-cutoff row.
- TOOL-2 S6 and TOOL-11 S5 leave blank-cutoff semantics undeclared — in THIS repo both keys are set
  and observed by criteria. Survives in sharper form as M10, which is about the adopter and the
  unset-variable trap, not about this repo.
- TOOL-11 S2's `Evidences:` line duplicates the `Serves:` binding — refuted at the grammar: `Serves:`
  is a document-level binding that may name several ids, `Evidences:` scopes one block inside such a
  record. Different questions.
- TOOL-10 F1 changes TOOL-9's idempotence rule and TOOL-9 carries no matching fork — the fork's own
  text names the spec it changes, and the method sweeps forks across the whole set before any code.
- TOOL-1 S4/S5/S6 are unobserved — AC5's fixture makes the local arm unreachable, so it IS the remote
  arm's observation, and S6's scenario cannot occur because the arm has no ref to test without the
  helper. Residual: S5's stdout wording is unasserted.
- TOOL-12 S3's three label spellings are exercised by one criterion — §4 requires the same parse, and
  the existing regex covering all three sits inside the same block the new check joins. A mis-parse
  is a loud red, repairable in the same pass.
- TOOL-11 AC6 cannot be observed because the parser lands later — it lands the NEXT pass and the
  criterion says "once that lands"; it never claims the gate selects the hygiene document.
- TOOL-4 S6 and TOOL-8 S4 might cite a non-terminal spec id from product source — both scope items
  point at the VERB, and the README already forbids the citation outright. Measured: the drift signal
  reads 1 of 38 against a pin of 2. Residual: adding the drift leg to §7 in both units costs nothing.
- TOOL-5 S7 inherits six refusals with criteria for two, and S9 has none — a blanket criterion covers
  each new refusal, an unarmed branch reds the harness gate, and S9 is stated four separate times.
- TOOL-7 S6 has no criterion for the rejected-candidate rule — §3 already carries the test that
  rejected each named route, quoted from the prior verdict record.
- TOOL-10 S6's third announced case has no criterion — a tip that is not a descendant produces a
  NON-empty range, so it lands on the announced no-matching-commit branch; and §4 puts both causes in
  one verdict row that a criterion does exercise.
- §7 gate lists name legs with wrong spellings — raised twice. Real, and refuted both times: the
  runner has no name-based leg selector to fail against, every mis-spelling resolves unambiguously by
  prefix, and the charter already requires the green line read from the manifest at emission time.
  Worth a tidy-up pass; not a defect that changes what gets built.
- TOOL-4 §1 says two aborted runs where the README now quotes three — a motivation count in prose is
  on none of the cross-read axes, and nothing in the scope is sized by it. Worth a one-word fix.
- TOOL-5 AC7 names an item-side spelling of a flag the verb does not expose — the inherited guard is
  one predicate over both fields with a single call site, so the reason case arms the whole branch.
- TOOL-11 §3's non-goal head contradicts its own body about attended builds — the body resolves it in
  the same sentence and routes it to a fork that unit 13 already cites as resolved.
- TOOL-11 §5 and TOOL-12 §1 mix roster positions with spec ids — real inconsistency, reproduced. But
  every reference is nonsense under the wrong reading and correct under exactly one, and the README's
  roster table is the position-to-id map. Worth normalising to full ids.
- TOOL-5 §4's rejection of folding into the park verb contradicts §5's observability claim — the
  parked counter is kind-selective over a spelled closed set, so a new kind token is not counted and
  nothing misgrades.
- TOOL-3 §4's byte budget says three other units write read-path files — measured, the README figure
  is not stale and the undercount is decorative, because the mandatory per-unit re-measure is what
  governs. Survives in different form as M4, which is about two units lacking that re-measure.
- TOOL-8 AC2's "numbered list" is unsatisfiable — refuted on the ground that inserting the new
  sentence as its own line leaves the condition lines byte-identical. Kept as M16 in the weaker,
  verified form: the criterion's mechanism is loose, not impossible.
- PLAY-1 S1 deletes one instance of a premise that appears twice — refuted for the same reason as the
  first entry above; AC3 and §3 force the second one out.
- TOOL-5 S3 keys the id shape on an extractor rather than a validator — the leg's check grades
  transitions to rows, never rows to transitions, so a junk row is ignored rather than red forever.
- TOOL-5 S3 points at a Python seam in another kit — STALE, quoting rev-1 text. The spec is at rev-2
  and already reached that conclusion, recording the seam as rejected.
- TOOL-11 S2's second binding key is redundant — refuted at the grammar; dropping it would break the
  multi-id journal case the binding deliberately supports.
- TOOL-10 §4 claims the method already enforces the id-in-subject join — the premise is right and the
  consequence is not: §4's inventory makes the unmatched case an ANNOUNCED observation, so the escape
  is surfaced. Survives as M2, which is about the two cases being indistinguishable, not silent.
- TOOL-11 §4's landing-day cutoff is the wrong idiom for a filename-date key — refuted: a sibling
  filename-date key in the same conf uses landing-day deliberately. Survives as H2, on the narrower
  same-day-landing contradiction.
- TOOL-1 §3 leaves three OPEN backlog rows unclaimed — bookkeeping already bound by the charter's
  Definition of Done and the wrap-up derivation; no unit's behaviour changes either way.
- Four §10 sections record "no function seam above the fan-in threshold" — the probe ANNOUNCES its
  own blindness on every run, the conf declares the dark layer with its reason, and each spec then
  does the by-hand check the tool asks for and names the shell seam it read at source.
- TOOL-9 §5 and TOOL-5 §5 ignore the run-state file's authored-region budget — the 8 KB figure is
  documented but unenforced; the only cap that reds is far above it, and three records already exceed
  8 KB with the bar green. Residual: a risks line naming the budget and its open row is cheap.
- TOOL-2 §4 says eight landed records carry no anchor where the population holds nine — the count IS
  wrong, and the migration is date-keyed rather than count-keyed, so nothing changes. Worth
  correcting the sentence and naming the archived-record class.
- TOOL-7 §4 says no product file moves while S2 dispatches through a workflow — refuted at the tool
  contract: the dispatch accepts an INLINE script, and this repo's own measured calls all use it. No
  file under the workflow directory, no inventory key, no ratchet.
- TOOL-7 S2's scratch prefix makes E3 unable to lose — the prefix is the DECLARED write set, not a
  sandbox; nothing confines the agent to it, and the observation is the real diff. Residual: §4 could
  say which pass kind each dispatched pass performs.
- TOOL-7 S7 overstates that E1 and E2 were measured and hold — the prior record clears only E1's
  inheritance half. Refuted because §4's own test design performs the priming the other half needs
  and AC5 forbids recording a criterion as passing on an argument. Residual: restate S7 in the
  record's two halves.

---

## COVERAGE — what this audit did NOT check

A CLEAN WITH FIXES verdict here is narrow. Read this section before treating it as reassurance.

- **This audited DESIGNS, not code.** Nothing has been built. Every failure above is a prediction
  about a unit that does not exist yet, derived from the spec text plus the current tree. A defect
  that only appears in an implementation choice the spec leaves open is out of reach here by
  construction.
- **No gate was observed RED.** Not one of the new checks in this build exists, so no failing case
  was staged, confirmed and unstaged. Where a finding says a leg "reds", that is derived from reading
  the leg's source and its sibling test, never from running a build that trips it. The build's own
  rule — every new check gets its failing case OBSERVED before it lands — is unaffected by this audit
  and still has to be done per unit.
- **The full bar was never run.** No leg verdict in this record comes from a bar run; leg names,
  contracts and populations were read out of the manifest and the sources. A leg that would red for a
  reason unrelated to these specs is not covered.
- **Cross-build effects were not swept.** The audit read this build's thirteen specs, its README, the
  method, the spec format and the sources those name. Other live builds, other run-state records and
  concurrent work on other nodes were not examined for interaction with these units.
- **Budget arithmetic was spot-checked, not recomputed per unit.** The method file's line count and
  the read-path total were measured once. Each unit still owes its own re-measurement from its own
  gate, per the README's build-level rule, and this record does not discharge any of them.
- **Refuted findings were not re-verified.** The refuted section records the skeptic's reasoning as
  given. A refutation that was itself wrong would pass through this synthesis unchallenged, which is
  why each line names the ground it died on rather than merely asserting it died.
- **Precision was 0.52.** Roughly half of what the finder lenses raised did not survive. That is at
  the low end of the useful band, and it means the confirmed set below is the product of the skeptic
  pass rather than of the finders — a second audit round over the same specs after the fold-in would
  be measuring different text and should not reuse these results.
