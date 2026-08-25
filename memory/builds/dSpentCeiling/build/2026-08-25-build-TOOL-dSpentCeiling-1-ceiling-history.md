# TOOL-dSpentCeiling-1 — the read-path ceiling's movement history, as the retirement exhibit

**Status:** CLOSED · rev-2 · 2026-08-25 · node d · Tier-2 · base 70df24ea · streams tooling

**Serves:** research TOOL-dSpentCeiling-1

This is the comment block that stood above `READ_PATH_CEILING` in `.memory-tree.conf` until the key
was retired. It is moved here rather than deleted because it IS the evidence the retirement rests
on: every raise argued in place, at the time, by someone who had thought about it.

Read it as an argument against itself. Not one paragraph is wrong on its own terms. What none of
them could see, because the instrument never reported it, is that over half of what the budget
measured is rendered from OTHER kits' templates and cannot be trimmed by this repo at all — so most
of these raises were pricing another kit's release against this kit's budget.

**Two lineages, and this is main's.** While this branch retired the key it also raised it one last
time, `135677 -> 161120` at `18cc9b78`, to unblock its own record-keeping. Main never took that step:
it went its own way to `137976`. The block below is MAIN's, because that is the history that
survives the merge; this branch's final raise is recorded in its own commit and in the build journal.
That two branches independently kept raising the same number, for unrelated reasons, in the same
week, is itself the finding.

---

```
# The charter's read path under MEMORY_ROOT: measured 51411 B + 20480 B headroom. One-sided. It has
# grown three times, every time for the same reason and every time deliberately: when the review
# protocol became a charter-cited BINDING document, again when the unattended protocol did, and now
# at 51411 when BUILD-METHOD.md landed (17591 B, the largest single member) in the same merge that
# gave the unattended protocol its boundary section (14408 B, up from ~12k). NEITHER side crossed the
# old 49268 alone; the merge did, which is the check doing exactly its job — a session's mandatory
# reading is a budget, and two binding docs growing at once spends from it visibly.
#
# The fourth movement was a RAISE and a LOWER inside one build, which is why both halves are recorded
# rather than just the surviving number. The kickoff manifest moved from `.claude/` into
# `memory/guides/`, putting its 20,920 B onto the read path for the first time: 74,951 B against the
# old 71,891 ceiling. The raise to 95,431 was scaffolding, explicitly temporary. The trap eviction
# then took the manifest to 12,215 B and the read path to 65,996 — BELOW where it started — so the
# ceiling comes back to a measured 65,996 + 20,480 headroom. The scaffolding did not become the norm.
# The FIFTH movement is a MERGE-INDUCED raise, and the headroom is what actually ran out. The fourth
# set the ceiling to a measured 65,996 + 20,480 headroom = 86,476. That headroom then absorbed 20,942 B
# of growth across many builds and is now spent: measured 86,938 against 86,476, over by 462.
# NEITHER PARENT WAS ILLEGAL, which is the whole shape of this one — node a's tree measured 86,404
# (under by 72 B) and origin/main's 84,551. The union crossed it, exactly as the backlog shard did in
# the same merge. Attributed, base 43eb6b1 -> merged, and it is only four files:
#   +1507  memory/guides/SESSION-KICKOFF.md   node a (aRuledFrontispiece; this reconcile added 10 B)
#    +780  memory/guides/BUILD-METHOD.md      node a (aRuledFrontispiece)
#    +533  memory/DECISIONS.md                origin/main (aWalkedCorpus rows)
#    +101  memory/LIVE.md                     GENERATED, both sides
# UNATTENDED-PROTOCOL.md and REVIEW-PROTOCOL.md did not move at all.
# Raised to the measured 86,938 + the same 20,480 headroom the fourth movement used, rather than to a
# number chosen for this merge — inventing a new headroom policy mid-reconcile is how scaffolding
# becomes the norm, and the fourth movement's own note says so. The alternative was trimming 462 B out
# of binding protocol prose belonging to other builds, mid-merge, which is the fee this repo already
# declined to pay for the TOOL shard in this same commit. What is OWED is a curation pass over the two
# guides that grew: this raise buys room, it does not say 87 KB of mandatory reading is correct.
#
# The SIXTH movement changes the HEADROOM CONVENTION rather than just the number, which is why it
# reads differently from the five above: they each re-spent a 20,480 B allowance, and this one
# retires that figure. 20,480 B had become smaller than a single member of the largest class on this
# path — the binding guides run to 25 KB apiece — so one more guide of that kind could not be
# absorbed by the whole allowance. That is not hypothetical. It is how the third movement happened,
# how the fourth did, and the fifth directly above says the same thing in its own words: the headroom
# is what actually ran out. The fifth declined to invent a new policy MID-RECONCILE, which was right,
# and left the policy question open. TOOL-aLoosenedCeiling answers it with a spec instead.
#
# The convention becomes 25,600 B — one tier up the same binary scale the check-6 class caps use, and
# larger than the largest present member. It is DECLARED as READ_PATH_HEADROOM below rather than
# living inside `corpus_ids.py --measure`, so an adopter whose corpus grows differently can size it
# for their own tree. The engine that reads it is TOOL-aLoosenedCeiling-1, which has LANDED: this
# comment named the window in which the declaration was inert, and that window is closed. Kept as a
# sentence rather than deleted, because the reason it was written still holds: a declaration nothing
# reads is worse than an absent one, since the next reader believes the tree is configured.
#
# The number: 107418 -> 112987, which is 87387 B measured on the merged tree plus 25,600. Measured at
# the MERGE and not at this build's close — the build's own decision rows and its build folder grow
# the read path, and letting a build size the budget it is about to spend from is the ratchet
# inverted. Its original base measurement (86,394) was overtaken by the fifth movement's merge, so
# the figure is re-derived here rather than carried forward, which is the same discipline the fifth
# applied to the fourth.
# SIXTH MOVEMENT, owner-ratified 2026-08-20 for `TOOL-dScriptedRepeat-1`. 112987 -> 131892, which is
# 106292 B measured plus the same 25,600 headroom every movement uses. The fifth movement's
# allowance is spent: 87387 -> 106292 consumed 18,905 of its 25,600 and left 6,695, and playbook
# mode owes a protocol mode row, two DoD table rows, a parked-kind row and eleven units' decision
# appends. Measured BEFORE this build spent any of it, which is STRICTER than the stated
# convention rather than looser: measuring at the merge would bake this build's own spend into the
# base and then add a fresh 25,600 on top. Whoever merges should re-run `--measure`, which is what
# the convention actually asks for.
# RAISED 131892 -> 132320 on 2026-08-23 (TOOL-dScriptedRepeat-15), and the growth is one §7 rule:
# COST IS A VERDICT — a suite declares a wall-clock ceiling, a runner reds on breach, and one
# arriving without a ceiling reds by that fact. It is here because an unaffordable check is a check
# nobody runs, which this repo proved the expensive way: seven legs left the bar for costing 68% of
# it, and the compensating check that replaced them then took an hour and was abandoned mid-run
# repeatedly across two days. The AGENTS.md merge-bar paragraph was compressed in the same commit
# to pay for part of it; 172 B is what the rule costs net.
# RAISED 132320 -> 132600 on 2026-08-23 (TOOL-dScriptedRepeat-15, round-7 fold), a MINIMAL raise
# on the precedent directly above rather than the measure-plus-25,600 jump the tool prints. What
# bought it: one true §B claim in the kickoff manifest (M8 gained the README re-read), a dated
# correction carrying a STANDING OWNER INSTRUCTION - `--selftests` does not run without them
# asking - and two gotcha names on the evicted list. What paid most of it: the 2026-08-20
# correction was PRUNED, because its own condition held; the charter states neither of the two
# numbers it superseded. That is 478 B given back against 634 B spent, and 280 B is the net.
# RAISED 132600 -> 132760 on 2026-08-24 (TOOL-dUnstalledConvoy-26), a MINIMAL raise on the
# precedent directly above rather than the measure-plus-25,600 jump the tool prints. The whole
# overage is ONE true §B claim in the kickoff manifest: the merge bar grew a second variable, and a
# session that does not know `GATE_SELFTESTS=1` exists will run a bar that holds 42 of 85 legs and
# read its green as a whole one. Measured 132476 at the build's base and 132607 at its close, so the
# claim cost +239 gross; 108 B was given back by rewriting the line to its load-bearing minimum in
# the same build, leaving +131 net. The 153 B of margin is the smallest that is not a pin needing
# another movement on the next byte.
#
# WORTH RECORDING SEPARATELY: this ceiling was already breached at the build's own HEAD and nobody
# saw it, because the hygiene leg is GUARDED and a code-only commit never runs it. The breach was
# found by the closing full bar, which is the run that is supposed to find it — but it means a
# guarded leg can hold a red for the length of a build. That is the cost of the guard, paid here.
# RAISED 132760 -> 133950 on 2026-08-24 (TOOL-dScaffoldedMirror-16..19), a MINIMAL raise on the
# precedent directly above rather than the measure-plus-25,600 jump the tool prints. The whole
# overage is FOUR ratified owner decisions landing in one turn, and they are named rather than
# summarised because a raise that has to be archaeologised is a raise nobody can check: F4's
# supersession, F-A5's, gov taking its own pressure, and the noun-led ruling. Measured 132713 at
# the build's base and 133901 with the four rows in, so they cost +1188 gross. NOTHING was given
# back, and that is stated rather than hidden: the four rows were already cut from 665/631/646/554
# chars to under the 300-char index cap before this raise was priced, which is where the 1300 B of
# give-back went. What remains is four one-line index rows at their load-bearing minimum.
#
# WORTH RECORDING, because this build exists to stop exactly this shape: a ceiling raised to absorb
# the raiser's own growth is the `.lexicon.conf` pin defect wearing a different filename. It is
# legitimate HERE only because the growth is four owner rulings rather than uncurated corpus drift,
# because the alternative is not recording ratified decisions, and because the detail they used to
# carry now lives in the build README, which is NOT on the read path. If the next raise cannot say
# that much, it is the defect and not the exception.
# The move, restated within the 14-line window the ratchet reads: 133458 -> 133950. That is the
# ADJACENT pair the ratchet compares -- the value in the conf at its base against the value now --
# and it is not the build-wide span, which is 132760 -> 133950 across two raises. Naming the span
# where the ratchet wants the step is why this line redded once already: it read as a justification
# for a move nobody made. The reasoning for both is the block above; this line exists at all
# because the original marker sat 16 lines up, outside the window, which is a justification nobody
# is credited with rather than one nobody wrote.

# RAISED 132760 -> 133138 on 2026-08-24 (TOOL-dFramedEntrypoint-8), a MINIMAL raise on the
# precedent directly above rather than the measure-plus-25,600 jump the tool prints. The whole
# overage is ONE row in memory/DECISIONS.md: the superseding decision that reverses two ratified
# refusals of a build-README prose template. That row cannot be trimmed to fit - a reversal whose
# record does not name what it reverses, and the re-measurement that makes it true, is the silent
# reversal the unit exists to prevent. Measured 132708 at the build base with 52 B of margin, and
# 132985 after the append, so the row cost +277 gross and nothing was given back. The 153 B of
# margin is the same figure the 2026-08-24 movement above used and is the smallest that is not a
# pin needing another movement on the next byte.
#
# THIS RAISE DELIBERATELY DOES NOT COVER UNIT 1, which grows memory/guides/BUILD-METHOD.md in the
# same build. That unit carries its own S-READPATH item and raises this ceiling again for its own
# charge. Two units charging one budget each price their own charge, which is what the round-2
# spec audit asked for after the first fold priced only one of the two growths round 1 named.
#
# RAISED 133138 -> 133396 on 2026-08-24 (TOOL-dFramedEntrypoint-1), the second of this build's two
# charges and priced separately from the first, exactly as the comment directly above says it would
# be. The growth is memory/guides/BUILD-METHOD.md, 23868 -> 24126 B: M2 now routes the unit
# classification to a named slot, M3 says which slot IS the goal bound a run may not amend, and M4
# routes the runaway-ceiling promotion notice. All three are the pointers that stop the method and a
# canon-gated README contradicting each other the first time a run follows the method on a bound
# file. Measured 133195 before the edit and 133243 after, so the net is +48 with 153 B of margin on
# the same precedent both movements above use. The first draft of this comment said +287, which was
# true of a longer wording of those three pointers and stopped being true when they were compacted
# to fit the file's line budget; the figure is re-derived here rather than carried forward.
#
# WORTH RECORDING: the same edit took that file from 313 lines to 312 against its OWN stated cap of
# 310, which it was already breaching at this build's BASE. Nothing enforces that pair, so nobody
# noticed. The run reduced it by one line and parked the remaining two, because trimming another
# build's method prose is a governance-carrier change and M3's veto 2 does not delegate one.
# RAISED 133396 -> 133458 on 2026-08-25 (TOOL-dFramedEntrypoint-7, closing), for the §B claims the
# kickoff manifest owes. Its check 9 fired at the close: the manifest BODY had not moved across
# fifteen watched commits, which is the ratchet correctly reporting that a build changed what the
# file front-loads while every commit recorded "delta none". Three claims went in - the heading
# canon and its registry, the order verb as the ordering source, and records rendering inside
# their specs. First written as three §B bullets at +1240, which put the manifest 936 B over
# its OWN 25600 limit - and that check says in as many words that the file is trimmed rather
# than the limit raised. Folded into the one trap bullet they supersede, at 389 B against the
# 400 B per-bullet cap, with the detail in the dossier that bullet already links to. Measured
# 133243 before and 133305 after, so the claims cost +62 net rather than +1240. 153 B of
# margin, the same figure every movement above uses.
#
# RAISED 133458 -> 133733 on 2026-08-25, for the OWNER RULINGS on this build's parked decisions.
# One memory/DECISIONS.md row records that the build-README contract grows ORGANICALLY - each
# build's owner conforms their own README on next touch - which is a policy a later session has to
# know before it wonders why the contract binds one file of sixty-two. Measured 133458 before and
# 133580 after, so the row cost +122; 153 B of margin, the same figure every movement above uses.
# The other three rulings are backlog rows and cost this path nothing.
#
# NET ACROSS THIS BUILD: 132760 -> 133733. Two units charged this budget and each priced its own
# charge, which is why the two movements above are recorded separately — but the ratchet reads
# only the endpoints, and a raise and a drain are indistinguishable to it without this line.
# The +698 is three things that could not be shortened away: one memory/DECISIONS.md row
# reversing two ratified refusals with the re-measurement that makes the reversal legible,
# three BUILD-METHOD.md pointers naming which README slot holds each mandated write, and the
# three §B claims above, which the manifest ratchet asked for by name at this build's close.

# BOTH RAISES ABOVE SURVIVE THIS MERGE, and neither is folded into the other. dScaffoldedMirror and
# dFramedEntrypoint raised this ceiling from the same 132760 base on the same day, on separate
# branches, for separate charges — four ratified owner rulings on one side and one superseding
# decision row on the other. A merge that kept only one block would leave a ceiling nobody can
# archaeologise, which is the exact failure the first block spends a paragraph refusing.
#
# The merge itself, restated within the 14-line window the ratchet reads: 132760 -> 134785. The
# value is MEASURED on the merged tree at 134632 B and not computed from either side's number — but
# it turns out to equal base plus BOTH deltas exactly (132607 + 1327 + 698), because the two growths
# land in different files and neither gave anything back. That arithmetic is the whole justification:
# the merge adds no prose of its own, it carries two already-priced charges into one tree. The 153 B
# of margin is dFramedEntrypoint's own figure, kept rather than re-derived.
#
# THE READ PATH IS STILL EFFECTIVELY FULL, and merging did not fix that. A `memory/DECISIONS.md` row
# costs about 295 B under the 300-char index cap, so 153 B of margin does not admit one. The parked
# decision under `TOOL-dScaffoldedMirror` stands unchanged: raise, trim, or leave a section-6
# obligation unmet, and it is the owner's to pick.
#
# THE PAIR THE RATCHET READS IS 134350 -> 135677, and it is the THIRD pair this key has needed in one
# week. The other two are still above and still true: 132760 -> 134785 was the span across
# dScaffoldedMirror and dFramedEntrypoint from their shared base, and 133458 -> 134785 was the step
# the ratchet wanted when main was dFramedEntrypoint's tip. dNarrowedAnchor then landed and moved the
# base again. The ratchet always compares against the value in the conf at ITS base, so the step is
# whatever main last said, and a span is never a substitute for it.
#
# MEASURED 135421 B on the merged tree, plus dNarrowedAnchor's DECLARED 256 B margin rather than this
# branch's earlier 153 — a later, argued doctrine beats an earlier ad-hoc figure, and it is the one
# main now carries. The margin still does not admit a `memory/DECISIONS.md` row at ~295 B, so the
# parked decision under `TOOL-dScaffoldedMirror` is unchanged by any of this: the read path is full,
# and three merges in a row have each priced their own growth without anyone trimming it.

# RAISED 133733 -> 134558 on 2026-08-25, for TOOL-dHonouredPark-2. Measured 133673 before and 134405
# after, so the charge is +732 in THREE parts: +259 for the M1 budget passage, which gains the dated
# 2026-08-25 line raise, the clause naming the BYTE half as the binding one, and the clause saying a
# gate for the pair is unruled — less the 92 B headless sentence tail that raise removed; and +268 for
# one memory/DECISIONS.md row; and +205 for the manifest repair the first two FORCED. 153 B of margin,
# the figure the recent movements use and a deliberate DEPARTURE from the measure-plus-
# READ_PATH_HEADROOM jump the tool prints.
#
# THE THIRD PART IS THE ONE TO KNOW ABOUT, because it caught this unit out. `.memory-tree.conf` and
# `memory/guides/BUILD-METHOD.md` are both on the kickoff manifest's `watch:` list, so touching either
# forces a manifest re-audit bundled into the same commit — and `memory/guides/SESSION-KICKOFF.md` IS
# a read-path member. So a unit that charges this budget and trips the manifest ratchet charges it
# AGAIN, after it thought it was done, and the second movement is discovered by check 16 going red on
# a tree that was green a minute earlier. Price the repair with the edit, not after it.
#
# THE DECISION ROW COST NEARLY THREE TIMES WHAT THE PRIOR ONE DID (+268 against the +122 recorded
# above), which is worth knowing before the next unit prices its own: a row's cost is its prose, and
# this build has three more rows to write against whatever margin is left.
# RAISED 134558 -> 134812 on 2026-08-25, for TOOL-dHonouredPark-3. Measured 134405 before and 134659 after:
# one memory/DECISIONS.md row and nothing else, this unit's subject being outside the read path.
# +254 against the +268 the previous row cost, which is what the note above asked the next unit to
# watch — a row's cost is its prose, and this one was written short on purpose.
# RAISED 134812 -> 135107 on 2026-08-25, for TOOL-dHonouredPark-1. Measured 134659 before and 134954 after:
# one memory/DECISIONS.md row, +295. The unit's subject is 52 build READMEs and two checkers, none of
# which is on this path.
# RAISED 135107 -> 135872 on 2026-08-25, for TOOL-dHonouredPark-4. Measured 134954 before and 135719 after:
# UNATTENDED-PROTOCOL.md gains the paragraph describing what --plan now reads, and one
# memory/DECISIONS.md row. The protocol is edited in tools/unattended/PROTOCOL.template.md and
# RENDERED here; editing the rendered copy directly reds the adopter drift check.
# NET AGAINST MAIN: 135677 -> 135872. The five movements above are this BRANCH's, each priced by the
# unit that charged it from 133733; local main meanwhile reached 135677 by work this branch does not
# carry, so the ratchet's own comparison is that pair and not any step in the narrative.
#
# LOWERED 135872 -> 135564, which TIGHTENS the ratchet and needs no excuse the way a raise does —
# recorded anyway, because a number that moves without a measurement beside it is what this whole
# narrative is against. Each per-unit movement above was correct WHEN MADE; later passes then
# SHRANK the path, the manifest's traps bullet coming back down after breaching its own 400 B cap
# being most of it. Measured 135411, so the ceiling is measured-plus-153 again rather than carrying
# 461 B of slack — the permanent-slack fault the sibling registry's equality pin exists to catch.
# Found by the closing review, which read the tree instead of the narrative.

# THE dHonouredPark MERGE, and BOTH narratives above survive it. main reached 135677 across
# dScaffoldedMirror, dFramedEntrypoint and dNarrowedAnchor; this branch reached 135564 across five
# movements of its own from 133733. Folding either into the other would leave a ceiling nobody can
# archaeologise, which is the failure the first block already spends a paragraph refusing.
#
# THE MARGIN IS 256, NOT 153. main's own text settles this: dNarrowedAnchor's DECLARED 256 supersedes
# dFramedEntrypoint's ad-hoc 153, because a later argued doctrine beats an earlier improvised figure.
# This branch used 153 throughout and adopts main's on arrival rather than carrying its own in.
#
# THE PAIR THE RATCHET READS IS 135677 -> 137976, main's value being the one in the conf at this
# merge's base. MEASURED 137720 B on the merged tree — not computed from either side's arithmetic,
# because the two branches grew different files and only a measurement over the union can say what
# the union costs.
READ_PATH_CEILING="137976"
# The headroom `corpus_ids.py --measure` adds to the measured read path when it prints a ceiling to
# paste back into this file. ABSENT = the kit's shipped default, which TOOL-aLoosenedCeiling-1 sets
# to 25,600 B and which is 20,480 B until it lands. It is advice to an author, never an input to the
# check: check 16 compares against READ_PATH_CEILING alone, because a ceiling computed from a
# headroom would let a growing corpus raise its own budget.
READ_PATH_HEADROOM="25600"
```
