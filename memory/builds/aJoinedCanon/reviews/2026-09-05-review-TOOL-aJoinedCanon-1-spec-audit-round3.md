**Serves:** spec-audit TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11

# Spec audit, ROUND 3 — the class rule worked, and the unit it could not reach carries most of the round

Tier-2 adversarial review of the eleven `aJoinedCanon` specs at rev-4, run after the round-2 fold.
Node `a`, 2026-09-05. Method: a bounded finder fan over the eleven specs plus the sources they cite,
a skeptic pass prompted to refute each finding, then this synthesis. Every citation in every spec was
re-checked against the tree; every named command, flag, leg name and line anchor was either run or
read at source.

**ROUND 3.** Subjects, each pinned at the blob reviewed:

- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md@047a7d08cd3b`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-2.md@5f361fc4c1c4`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-3.md@0890f9016d45`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-4.md@5a7efba34b2d`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-5.md@f02b20c69fb0`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md@df8c5147ad96`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md@08c1fa27e42e`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-8.md@f344acd6e018`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md@6bf564cb4aae`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-10.md@be9b2da56e6c`
- `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md@e92e43180bcc`

## Verdict: BLOCKED

One confirmed blocker. Round 1 returned 2, round 2 returned 1, and this round returns 1 — the count
did not fall, so the convergence rule does not re-arm. The blocker is the same class both prior
blockers were (a population decided by another key's value) arriving one level further down: through
the awk `-v` variable namespace instead of through nesting or scope. Nine highs, seven mediums and
one low sit under it.

The round's headline is that **the class rule worked where it was applied.** Round 2's headline
defect — a ruling folded at its address and never swept to the sibling carrying it — is measurably
rarer here: of the eighteen distinct defects below, ten are in `TOOL-aJoinedCanon-11`, the one unit
the fan did not fold, and the other ten specs carry eight between them. Only two defects are a class
that a sibling closed and this spec missed (H1's ordering and M3's line pin, both in unit 11).
The blocker itself is the exception that proves the cost of a per-spec sweep: it is a **cross-unit**
collision, invisible to any folder reading only its own spec, and unit 3's namespace registry proves
nobody looked — it lists `mcut` as claimed by unit 4 alone, three `order` steps after unit 1 takes it.

Two of the three things flagged for weight came back clean. Unit 1's folder declined part of an
assigned Fix with a stated reason, and the reasoning holds — the declined half would have restated
`BUILD-METHOD` prose beside the source that owns it, which is the class the charter refuses; the
decline is correct and unit 1's defects lie elsewhere (B1, H2, H3). The re-derived figures are a
split verdict: unit 7's re-derivation was run and is right at the address it names but not at the
sibling three bullets down (H9); unit 11's block is stamped `Re-derived at 750ca0ca` and reproduces
at neither that sha nor HEAD (M1).

## Review shape

Raw 38 · confirmed 28 · refuted 10 · unverified 0 · precision 0.74.

The 28 confirmed findings collapse to **18 distinct defects** after de-duplication — four independent
finders reported unit 11's revision-log splice, three reported its figure block, three reported the
`mcut` collision, and two each reported four more. Every collapse is recorded in the `Raw` column
below. Precision is up from round 2 and the refuted ten were mostly style calls on citation
convention, not misreadings of source.

## Findings

| # | Sev | Unit | Address | Defect | Raw |
|---|---|---|---|---|---|
| B1 | blocker | 1, 4 | §4 "The arm" / §2 S4 | `mcut` bound twice on one awk invocation, to two different cutoff keys | 13, 23, 28 |
| H1 | high | 11 | §9 | rev-4's entry spliced into the middle of rev-2's; log reads 1, 2, 4, 3 | 1, 15, 27, 29 |
| H2 | high | 3, 4, 6, 7, 8, 9, 10, 11 | §2 / §7 | eight units edit a `watch:` path and none carries the `last-audit` re-stamp | 2 |
| H3 | high | 1 | §7 | S8 demands the marker moved in every carrier; no `kit version markers` leg | 14 |
| H4 | high | 11 | §2 S3 | the single-batch resolution — the unit's central decision — has no observer | 4, 16 |
| H5 | high | 11 | §2 S5 vs §6 | S5 builds two fixtures; AC3, AC5 and AC6 need three more nothing constructs | 3 |
| H6 | high | 11 | §6 AC5 | `git clone --depth 1` from a local path does not make a shallow clone | 22 |
| H7 | high | 11 | §2 S2 / §4 | the only engine unit that never says which side of the Tier-1 cut its branch sits on | 21 |
| H8 | high | 9 | §6 AC1 | AC1 pins both keys into `optional_keys`; §4's own table makes one required | 6 |
| H9 | high | 7 | §4 bullets 1 and 3 | two values for one derived figure, and the rev-4 log claims the fix | 30 |
| M1 | medium | 11 | §2 "What this arm buys" | figures stamped `Re-derived at 750ca0ca` reproduce at neither that sha nor HEAD | 7, 17, 33 |
| M2 | medium | 11 | §4 Data model | "all 26 existing fixtures" is wrong and pins a count six lower-`order` units move | 8 |
| M3 | medium | 11 | §7 | a bare `:53` line pin into a file unit 9 edits at `order` 9 | 9, 32 |
| M4 | medium | 11 | §4 Files touched | the dossier row has no scope item, no criterion and no leg | 11 |
| M5 | medium | 11 | §2, §10 | two `path:line` citations land on headings, not on the sentence cited | 34 |
| M6 | medium | 5 | §6 AC6 `figure:` | the stated reason for scoping the range is false of the command AC6 runs | 20 |
| M7 | medium | 6 | §2 S4 vs §6 AC13 | S4's "in BOTH confs" half is observed in one conf only | 12, 37 |
| L1 | low | 2 | §4 Alternatives rejected | "excluding only the template" — the script declares four exclusions | 38 |

---

### B1 — blocker — `mcut` is bound twice on the one check-12 awk invocation

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md` §4 "The arm",
the "Where it sits, stated as an exclusion" paragraph, against
`memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-4.md` §4 "The hoist" and its
Inventory row.

Unit 1 (`order` 1) says its `REV_SCOPE_CUTOFF` arm is "guarded by `mcut != \"\"` and by nothing
else" — the only awk variable it ever names for its own key. Unit 4 (`order` 4) claims the same name
for `SPEC_FAILURE_MODE_CUTOFF`: "named `mcut` because `fcut` is already `FORK_MARK_CUTOFF`", with an
Inventory row spelling "one `-v mcut=` on the existing check-12 awk". Unit 3's namespace survey
records only unit 4's claim — "`TOOL-aJoinedCanon-4` has claimed `mcut`" — which is the proof that
no folder in the fan ever saw unit 1's.

**Verified at source.** `tools/memory-tree/check-memory-hygiene.sh` opens check 12's awk with exactly
`-v canon -v canon10 -v cut10 -v mroot -v discalt -v scut -v wcut -v fcut -v ecut`; `grep -c mcut` over
that file returns 0. So `mcut` is genuinely free today and both units will take it, on the same
invocation. A second `-v mcut=` is last-wins for the whole program, so from `order` 4 onward one arm
is graded by the other arm's key while its own conf key still reads as armed.

**Why no fixture catches it.** In this repo both keys take `2026-09-06`, so every corpus run and
every fixture behaves identically. It is live only in an adopter who arms one key and not the other —
the case with no local witness, which is the exact argument unit 1's own placement paragraph makes.
And neither spec's criteria can distinguish it: unit 1's AC6 and unit 4's AC6 each blank their own
key, which blanks the shared binding and turns BOTH arms off, so both criteria pass with both arms
dark. This is round 1's blocker and round 2's blocker in a third disguise.

**Fix.** Give unit 1 its own binding name in §2 S4, in §4 and in its Files-touched row — `rvcut` is
free (`rcut` is unit 9's, `bcut` unit 11's) — and replace both `mcut` occurrences in unit 1 §4. Add
the name to unit 3 §4's namespace survey so the taken list is complete. Then add a criterion to one
of the two specs that arms one key, blanks the other, and asserts the armed arm still fires; no
existing criterion in either spec can tell the collision from a correct build.

**Left-shift.** Extend the build README's "One owner for the `tFixture` number space" rule to cover
the check-12 `-v` binding namespace, one owner per name allocated by `order`, so the next collision
is a README conflict rather than a silent rebind. Mechanically: a self-test arm asserting the check-12
awk invocation binds no name twice — `grep -o ' -v [a-z0-9]*=' | sort | uniq -d` must be empty — which
reds on the duplicate at the commit that introduces it rather than in an adopter's tree.

---

### H1 — unit 11's revision log is spliced and out of order

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §9.

The hand-fold inserted rev-4's entry into the MIDDLE of rev-2's. Verified in the bytes: rev-2 ends
mid-sentence at "folded the owner's ruling on F1: live specs", rev-4's whole entry follows, and
rev-2's tail — "only, and the bypass it accepts became a requirement — S7 states it in check 12's
catalog entry and its twin, AC8 grades it, §3 and §4 stop calling the widening an open decision…" —
sits underneath rev-4 as its continuation. rev-3 is then logged after rev-4, so the sequence reads
1, 2, 4, 3.

**Impact.** The one section this build exists to make readable is unreadable in the one spec the fan
did not fold. rev-2's record is a fragment, and rev-4 now claims authorship of the S7/AC8/§3/§4/§5
moves that round 1's owner-ruling fold made — a resumed session reading the log to find what a fold
invalidated is told the wrong round did the work. The misattribution is mechanical, not merely
visual: `drift_report.py`'s `_REVLOG_RE` entry loop folds every following non-blank line into the
preceding head, and so does the per-entry accumulator `TOOL-aJoinedCanon-1` itself proposes, so the
arm this build ships would bind rev-2's tail to rev-4. Nothing gates it — check 12's §9 walk compares
the header rev only against the maximum `rev-[0-9]+` it sees, which is 4 either way. It is also a
live instance of the descending-rev-order arm `TOOL-dUnstalledConvoy-14` proposes, which unit 1's §3
parks as a non-goal.

**Fix.** Rejoin rev-2's two halves into one entry and move rev-4 below rev-3, so the log reads
1, 2, 3, 4 with each entry's continuation lines under its own head. Then re-check rev-4's scope-token
field against what its entry actually claims once the tail is gone.

**Left-shift.** Unit 1 already ships the §9 entry accumulator; give it one more assertion — rev
numbers within a §9 walk are unique and ascending — and this is a red bar rather than a reading. That
is `TOOL-dUnstalledConvoy-14`'s proposal, and this defect is the reachability evidence it was missing.

---

### H2 — eight units edit a `watch:` path and none owns the `last-audit` re-stamp

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-3.md` §2 (no
re-stamp scope item) and §7 (no `kickoff-manifest ratchet` leg), and the same absence in units 4, 6,
7, 8, 9, 10 and 11.

`memory/guides/SESSION-KICKOFF.md` carries `tools/memory-tree/check-memory-hygiene.sh`,
`.memory-tree.conf`, `tools/gate-legs.json` and `memory/guides/BUILD-METHOD.md` on its `watch:` line,
verified at HEAD. Units 3, 4, 6, 8, 9 and 11 edit the hygiene checker and the conf; unit 7 edits the
conf; unit 10 edits the conf. A grep for `last-audit` or `re-stamp` across the eleven specs returns
hits in units 1 and 2 only.

**Impact.** `kickoff-manifest ratchet` is `subject: repo` with no guard in `tools/gate-legs.json`, so
it runs on every bar, and `manifest-check.sh` check C5 is topological — it reds when the newest
watch-touching commit is not an ancestor of the `last-audit` re-stamp, regardless of body delta. Each
of those eight landings therefore reds the bar for an obligation its own spec names nowhere: no scope
item, no Files-touched row, no criterion, no leg. Unit 1 carries it correctly as S8 plus AC11 plus the
leg, and unit 2 as S10 plus AC10 plus the leg. Nine folders had the predicate in hand — unit 2's own
rev-4 log calls this "H1's class, the largest hit of the round" — and eight of them did not run it
over their own write set.

**Fix.** In each of units 3, 4, 6, 7, 8, 9, 10 and 11: a scope item for the
`memory/guides/SESSION-KICKOFF.md` `last-audit` re-stamp copying unit 2's S10 (including the "no
delta → no touch" half for `last-body-change`), a Files-touched row, a criterion in AC10's shape with
check C5 named as the observed red, and `kickoff-manifest ratchet` in §7.

**Left-shift.** A spec-time arm: for each Files-touched row whose path is on the kickoff manifest's
`watch:` line, require a `last-audit` token somewhere in the spec. That is a join between two files
already in the tree and it is exactly the join this build was commissioned to make.

---

### H3 — unit 1 demands the carrier sweep and names no leg that grades it

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-1.md` §7, against §2
S8 and §4 "Files touched".

S8 requires `KIT_MEMORY_TREE_VERSION` bumped AND "the `gov:kit memory-tree@` marker moved in every
carrier", and §4 spends a paragraph warning that the carrier set is easy to undercount. §7 then names
only `verdict epoch (kit version dates the engine)`, and AC9 runs `check-verdict-epoch.sh` alone.
`kit version markers` appears nowhere in unit 1 — it is named in units 2, 3, 4, 6, 7, 8, 9, 10 and 11,
and unit 5 explicitly records it as not owed, so unit 1 is the sole gap.

**Verified at source.** `tools/check-kit-versions.sh` enumerates
`git ls-files 'tools/memory-tree/*.template.md'` and reds any member whose `gov:kit memory-tree@`
marker disagrees with the constant. Unit 1 edits three such templates — SPEC-TEMPLATE, HYGIENE,
BUILD-METHOD — and bumps the constant, so `kit version markers` is precisely the leg that reds on the
failure mode §4 describes. `verdict epoch` cannot catch it: an advanced constant with a stale marker
satisfies the epoch rule.

This is round 2's H1 class. Units 3, 4, 6, 8, 9 and 11 each swept it and named the hit in their rev-4
logs; unit 1's rev-4 sweep list accounts for B1, M7, M10, M3/L1, M8 and L2 and never mentions H1
either as a hit or as absent — a §9 log claiming a coverage the document does not carry.

**Fix.** Add `kit version markers` to §7 with the sentence the siblings use, and extend AC9 to run
`bash tools/check-kit-versions.sh` beside `check-verdict-epoch.sh`, naming the two staged reds
separately: revert the constant alone for `verdict epoch`, move one carrier and not the rest for
`kit version markers`.

**Left-shift.** Unit 7 already builds the §7 leg-name join. Extend it: a spec whose Files-touched
table names a path matched by a leg's own file glob must name that leg in §7. That converts "which
legs does this unit owe" from a folder's memory into a derivation.

---

### H4 — unit 11's central implementation decision has no observer

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §2 S3,
against §6.

S3 — "the resolution runs as ONE `git cat-file --batch-check` for the whole population, driven by a
sentinel record the existing awk emits, not by a fork per spec" — carries no `Observed by` tag and no
criterion grades it. AC1 and AC2 drive the two fixtures, AC3 the CLOSED exemption, AC4 a whole-tree
green, AC5 the shallow skip, AC6 the blank key, AC7 the arms pin, AC8 the HYGIENE entry, AC9 the
example conf, AC10 the template bullet, AC11 the header. AC6 does use the word "sentinel", but only
in the blank-key off state, which a fork-per-spec implementation satisfies exactly as well.

**Impact.** A build that forks `git cat-file -e` per spec satisfies all eleven criteria. §5's perf
row ("one added process per run, independent of population size") and §4's whole Cost argument then
rest on an unobserved property. Round 2 raised this exact shape as H4 against this exact spec ("a
scope item with no criterion at all"); the fold added an `Observed by` tag to S6 and left S1, S2, S3,
S4, S5 and S7 untagged — the address-not-class close the build README bans, in the spec that got no
adversarial fold.

**Fix.** Add a criterion that fails on the fork-per-spec implementation: run the gate over a fixture
tree of N post-cutoff live specs with a `git` wrapper or a process counter and assert exactly one
`cat-file` invocation regardless of N. Put `Observed by` tags on S1 through S5 and S7.

**Left-shift.** Unit 3 is the arm for exactly this — a scope item names the criterion that observes
it, or says why none does. Unit 11 should be its first fixture: run unit 3's predicate over unit 11
before either lands.

---

### H5 — unit 11's scope builds two fixtures; three criteria need artefacts nothing constructs

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §2 S5, against
§6 AC3, AC5 and AC6.

S5 declares exactly two fixtures — a post-cutoff live spec whose base does not resolve, and one whose
base is the scratch repo's HEAD — and §5's testing bullet repeats "S5's two fixtures". AC3 needs a
post-cutoff CLOSED fixture carrying an unresolvable base, AC5 needs a shallow scratch tree, AC6 needs
a blank-key run. None is built by any scope item.

**Impact.** A builder implementing the scope as written ships two fixtures and cannot observe AC3,
AC5 or AC6. AC3 is not incidental: rev-4 deliberately moved the grandfathering evidence off AC4 and
onto AC3 — "The grandfathering itself is observed by AC3, on a fixture built for it" — so the fold
relocated the observation onto something the unit does not construct. Every sibling enumerates its
fixture set against its criteria; unit 4's S6 names six fixtures and carves out a second scratch tree
for the one criterion the shared conf cannot exercise, which is exactly what AC5 needs here.

**Fix.** Widen S5 to name every fixture and scratch tree the criteria need — the red live fixture,
the green live fixture, a post-cutoff CLOSED fixture with an unresolvable base, a shallow scratch
tree, and the blank-key run — allocated from the `tFixture-190` block, and state which is observed by
which criterion.

**Left-shift.** The reverse of unit 3's join: every criterion's named artefact must be constructed by
some scope item. One arm covers both directions and this build is already writing half of it.

---

### H6 — unit 11's AC5 cannot construct the condition it asserts

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §6 AC5.

AC5 builds its shallow repository with `git clone --depth 1` from a local path. Reproduced live in
this worktree: git prints `warning: --depth is ignored in local clones; use file:// instead`, and
`git rev-parse --is-shallow-repository` then answers `false`.

**Impact.** AC5 asserts that probe answers `true`, that the skip line appears, and that the run exits
0. The first two conjuncts cannot hold in the tree its own command builds, so the criterion is not
loose — it is ungreenable as written, and the surviving "exits 0" is the half a builder will read as
satisfied. Every scratch tree in `tools/memory-tree/check-memory-hygiene.test.sh` is a local
`git init`, so an AC5 fixture is necessarily a local clone. S4 is the arm that keeps this unit from
passing-by-finding-nothing in shallow CI, and it ships with an unobservable observer. §4's shallow
paragraph inherits the same misconception from its `dScaffoldedMirror-7` citation, recording only
that `--is-shallow-repository` was "verified present here, answering `false`".

**Fix.** Clone with `git clone --depth 1 "file://$(pwd)"` (or `--no-local`), and make AC5 assert
`git rev-parse --is-shallow-repository` prints `true` as a PRECONDITION, so a silently-non-shallow
clone fails AC5 rather than passing it. Correct §4's shallow paragraph to say the same.

**Left-shift.** Unit 5 ships criterion preconditions. This is its use case: a criterion whose setup
cannot be shown to have produced the state it grades declares that state as a precondition and
asserts it before the grade.

---

### H7 — unit 11 never states which side of the Tier-1 cut its branch lands on

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §4
"Inventory", the sentinel-emission paragraph, and §2 S2.

`if (hdr ~ /Tier-1/) next` sits in `check-memory-hygiene.sh` with the section-canon `\001` sentinel
and the empty-body walk below it — and that `\001` sentinel is precisely the prior art unit 11's §4
tells the builder to extend. The word "Tier" appears in unit 11 exactly once, in its own status
header. No scope item, design paragraph or criterion says which side of that cut the `\002` emission
lands on, while S2 claims the population is "every selected spec".

**Impact.** If the emission lands below the cut — the natural spot, beside the walks it is told to
copy — every Tier-1 spec's base is never resolved while `BASE_RESOLVE_CUTOFF` reads as armed. Four of
this build's own eleven units are Tier-1. No criterion can tell: AC1 and AC2 name no tier, AC3's
fixture is CLOSED, AC4's green is guaranteed by the terminal-status conjunct by its own admission,
AC5 is the shallow probe and AC6 the blank key. This is B1's class one guard over. Unit 4 carries
AC5 for exactly this cut, with the same source-text citation, so the build's own standard is to state
it.

**Fix.** State in S2 and in §4's Inventory paragraph that the sentinel emission sits ABOVE the
`if (hdr ~ /Tier-1/) next` line, in the both-tiers band the streams and witness ratchets occupy, and
say why — a base sha is a header field on both tiers. Make one of S5's fixtures a Tier-1 spec and say
so in AC1 or AC2, with "the branch was placed below the Tier-1 cut" as its stated break.

**Left-shift.** Unit 4's arm — a criterion names the break that would turn it red — plus a build rule
that any unit adding a branch to check 12 states its position relative to the Tier-1 cut, since three
units in this build reason about that cut and only one writes it down.

---

### H8 — unit 9's sole observer of S4 reds on the correct implementation

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-9.md` §6 AC1,
against §2 S4 and §4 "Files touched".

AC1 requires both new keys to be in `tools/memory-tree/kit.toml`'s `[config] optional_keys`. S4 says
only "[config] key lists" and chooses nothing. The Files-touched row names three lists —
`placeholders`, `required_keys_render` and `optional_keys`. And §4's own blank-value table has
`adopt-memory-tree.sh` refusing to render on a blank `READINESS_ROWS`, which makes it required for
render.

**Verified at HEAD.** The descriptor carries `required_keys_render = ["MEMORY_ROOT"]` and a nine-name
`optional_keys`. Implement the unit as §4 describes — `READINESS_ROWS` in `required_keys_render` —
and AC1's two-line `tomllib` read of `optional_keys` returns one name, not two. AC1 is the only
observer of S4, so the sole grade on that item reds on the design the same spec prescribes. The
criterion was rewritten at rev-4 to close round 2's H6 (the non-existent `govkit.py --selfcheck`
verb) and the replacement pins a placement the scope never chose.

**Fix.** State in S4 which list each key lands in — `READINESS_ROWS` in `required_keys_render` and in
`placeholders` for the SPEC-TEMPLATE rule, `READINESS_ROWS_CUTOFF` in `optional_keys` — and have AC1
read those two lists rather than asserting both names in one.

**Left-shift.** A fold rule with teeth: when a criterion is rewritten, re-read the scope item it
observes and the design paragraph it grades, in the same pass. Round 2's fold rewrote AC1 without
re-reading S4 or §4, and that is a re-read set — which is `TOOL-aJoinedCanon-2`'s entire mechanism.
Unit 2's re-read set should name "the scope item this criterion observes" explicitly.

---

### H9 — unit 7 carries two values for one figure, and its rev-4 log claims the fix

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-7.md` §4 "What the
join reads today", bullets 1 and 3.

Bullet 1 says "27 of the 42 live specs carry no `LEG_LINE` at all" and "31 of the 42 contribute no
graded leg token — the five between them…". Bullet 3 says "the fold measures 26 of 42". Re-derived
here with the checker's own `LIVE`, `LEG_LINE`, `NOT_A_TOKEN` and `NOT_A_LEG` predicates against
`tools/gate-legs.json`: 42 live specs, 27 with no `LEG_LINE`, 31 contributing no graded leg token.
So 27 is right, 26 is wrong, and the gap is four, not five — bullet 1's own arithmetic is against the
discarded 26.

**Impact.** §9's rev-4 entry names this exact correction — "M1: §4's `26 of the 42` was 27,
re-derived today" — so the fold's own log claims a coverage the document does not carry. This is the
round-2 headline shape reproduced inside the fold run under the rule written to stop it: the finding's
address was corrected, the sibling occurrence three bullets down and the sentence whose arithmetic
depends on it were left standing. A builder re-deriving from bullet 3 gets a figure the same section
contradicts.

**Fix.** Correct bullet 3 to 27 and bullet 1's "the five between them" to "the four between them",
re-running the derivation over both rather than editing one to match the other.

**Left-shift.** The cheapest possible gate, and it would have caught this and M1: a derived figure
appears once per spec, or is stated as a command. Unit 5's `figure:` sub-field already carries the
vocabulary — extend it to require the deriving command beside any digit a spec repeats.

---

### M1 — unit 11's "Re-derived at 750ca0ca" block does not reproduce at that sha

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §2, the "What
this arm buys" block, and §4's Cost paragraph.

Measured at `750ca0ca`: 474 specs carry a base over 86 distinct values, and the live population under
this spec's own S2 definition (status not `CLOSED` or `WONTDO`) is 40, every one of them carrying a
base. At HEAD: 485 over 87, 42 live under the strict definition and 51 under S2's, again all carrying
a base. The spec's "477 tracked specs carry a base over 87 distinct values" reproduces at neither
end, and the 87 is a HEAD figure under a `750ca0ca` label. "The live population is 43 specs, 42 of
them carrying a base" implies a base-less live spec that does not exist under any selector run — the
43rd line is the quoted template header inside a file whose real status is CLOSED. §4's "43 forks
today" inherits the same number.

**What does hold.** The 22 files, the 9 unresolvable distinct values and the "all 22 are CLOSED"
claim all reproduce, which is what makes the wrong figures hard to spot. `TOOL-aJoinedCanon-7`,
folded the same day, measures 42 live twice, so two specs in one build disagree on one population.

**Impact.** This block is the unit's entire value argument, stated "plainly because the honest answer
is small", and it is the one place a reader checks whether the arm is worth building. A reviewer told
the figures were re-derived at a named sha has no reason to re-run them.

**Fix.** Re-derive at the sha named, with S2's population definition stated explicitly (not
`check-spec-tokens`' four-status LIVE set, since S2's is the set the arm grades), or drop the digits
and cite the deriving command as unit 8's §4 does.

**Left-shift.** Make `Re-derived at <sha>` a checkable claim rather than a courtesy: require the
deriving command beside the sha, so the next fold can re-run it in one line instead of trusting the
label.

---

### M2 — unit 11 pins a fixture count six lower-`order` units move first

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §4 "Data
model", last paragraph.

"That also grandfathers all 26 existing `base 0123abcd` fixtures in the self-test" does not reproduce
under any counting at either tree: `tools/memory-tree/check-memory-hygiene.test.sh` carries that
literal on 23 lines and 33 times, across roughly 54 distinct fixture spec files. The spec offers no
derivation.

**Impact.** The sentence carries the reason S5 needs only new fixtures rather than a sweep of the
old, so a wrong count is the load-bearing half of that argument. It also breaks build rule 5 head-on
— units 1, 3, 4, 6, 8 and 9 all add fixtures to that file at a lower `order`, so the number is stale
before unit 11 builds — in a spec that correctly derives its kit-version carrier count and AC7's pair
rather than pinning them.

**Fix.** Drop the number and state the property: every existing `base 0123abcd` fixture is dated
before the cutoff and is grandfathered. Or mark it derived-at-build-time with the deriving grep
beside it.

**Left-shift.** Same gate as H9 — a spec's bare integers either appear once or carry their deriving
command. Build rule 5 is currently a rule with no predicate; this is the predicate.

---

### M3 — unit 11 §7 carries a bare `:53` line pin into a shared write set

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §7, the
`kit/dogfood doc parity` bullet.

The bullet ends "both `HYGIENE` and `BUILD-METHOD` pairs at `:53`", pinning into
`tools/memory-tree/kit-dogfood-parity.test.sh`, where `PAIRS=` is line 53 today. Unit 9's
Files-touched table declares that same file at `order` 9 — "the same block byte-identically, plus the
exit-2 path" — two steps before unit 11 builds.

**Impact.** Build rule 6 forbids a line number inside a shared write set, and this is the
class-versus-address failure demonstrated: unit 10's rev-4 converted the identical
`kit-dogfood-parity.test.sh:53` pin to "the `PAIRS` assignment by name", while unit 11's rev-4 log
claims a "class sweep over all 23" that converted only the `run-gates.sh:1110-1111` pin. Same
address, same class, closed in one spec and missed in the other. A bare `:53` also escapes the
self-check unit 6 used, `grep -nE '[a-z-]+\.(sh|md|py):[0-9]'`, which needs a filename before the
colon.

**Fix.** Cite the `PAIRS` assignment by name, as unit 10's §10 now does, and re-run the citation
sweep with a pattern that catches a bare `:<n>` as well as `<file>:<n>`.

**Left-shift.** A spec-time arm: no `:<digits>` citation may name a path in this build's own
Files-touched union. Build rule 6 becomes machine-checkable at zero cost, and it is the second build
rule in this report with no predicate behind it.

---

### M4 — unit 11's dossier row has no owner

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §4 "Files
touched", last row.

`memory/map/features/memory-tree-hygiene.md` ("dossier prose, refreshed on touch") appears nowhere
else in the spec — no scope item, no criterion, no §7 leg. Nothing on the bar covers it either:
`codebase-map coverage + freshness` tests key claims, pinned headings, POSIX keys and artifact
freshness, none of which notices unreferenced prose going stale.

**Impact.** The dossier edit ships absent with all eleven criteria green — the H2/H4 shape the
round-2 fold closed elsewhere in this same spec. Unit 7, the only sibling with a dossier row,
declares it as S6 and grades it with AC7, so the asymmetry is unit 11's, not the build's convention.
Charter §5 makes refreshing a touched dossier a Definition-of-Done item, so this is a declared
obligation with no observer at all.

**Fix.** Promote the row to a scope item stating what the dossier must say — the new arm, its conf
key, the live-only population and the accepted bypass — and grade it in AC10's shape, greping the
dossier for `BASE_RESOLVE_CUTOFF` against its pre-change zero.

**Left-shift.** Every Files-touched row is named by a scope item or by a criterion. That is unit 3's
join applied to the table instead of to §2, and it closes H2, H5 and M4 with one predicate.

---

### M5 — two surviving `path:line` citations land on headings

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-11.md` §2 ("The
class is not hypothetical") and §10.

`memory/builds/dCarriedReceipt/reviews/2026-08-26-review-DEPL-dCarriedReceipt-5-diff-review-round2.md:3`
is the review's H1 title; the base-sha finding it is cited for is at `:7`.
`memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-9.md:205` is the
`## 5. Production-readiness checklist` heading; the absent-sha / shallow-clone / blobless sentence is
the `error / empty / loading states` bullet at `:228`.

**Impact.** Round 1 found two wrong line numbers in this set and round 2 found five more; these two
survived a fold whose §9 claims a sweep of all 23 classes. The strongest defence available is that
the spec uses heading anchors elsewhere and this finding does not flag those — but that shows the
convention was never adjudicated rather than approved: no round examined any `dCarriedReceipt` or
`dScaffoldedMirror` citation, so these survived unchecked. Round 2's own confirmed M1 and M3 are
exactly this shape, so the build has already ruled the class real.

**Fix.** Repoint both, or convert them to text anchors as the siblings did — "the finding opening
`The base sha as handed to this reviewer does not resolve`" and "the `error / empty / loading states`
row of that spec's §5".

**Left-shift.** A citation arm that resolves `path:line` pins into records and checks the line is not
a heading. Cheap, and it catches the whole class rather than the two instances here.

---

### M6 — unit 5's `figure:` justification is false of the command AC6 runs

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-5.md` §6 AC6, the
`figure:` sub-field.

AC6's stated reason for scoping its sed range — "The whole-file count of `PINNED` or `DERIVED` is not
`0` today … which is why the range is scoped and an unscoped grep would not fail before the change" —
is false of the command AC6 actually runs, which greps `PINNED` alone.
`grep -cF 'PINNED' memory/TEMPLATE-SPEC.md` returns 0, so the unscoped form would be red before the
change exactly as the scoped one is. The cited instance, the `order` bullet ending "DERIVED from this
field…", is at line 80 — outside the `## Writing rules` range (85–103) the scoping supposedly
protects, so it is not something the scoping excludes either.

**Impact.** The criterion still works on its placement rationale; its recorded justification does
not. The next fold re-checking it finds a false premise inside the `figure:` field this very unit
invents to make premises checkable. Round 2 graded this shape high on a sibling — a document
asserting a property of itself that is false — and the irony of the location is the whole reason to
fix it rather than shrug.

**Fix.** State the true reason (the scoping keeps AC6 reading the Writing-rules half rather than a
`PINNED` the §6 block may also gain from S1's `figure:` line), or make the grep match the sentence by
scoping `PINNED\|DERIVED` with the DERIVED baseline of 1 at line 80 named as the excluded instance.

**Left-shift.** Nothing mechanical is worth building here. Add it to the fold's re-read set instead:
a criterion carrying a `figure:` premise gets that premise re-run, not re-read.

---

### M7 — unit 6's "in BOTH confs" half has no observer

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-6.md` §2 S4, against
§6 AC13.

S4 ends "Each key's comment, in BOTH confs, states S9's dependency. Observed by AC5, AC6 and AC13."
AC5 grades the label cutoff's grandfathering, AC6 the blank/armed disarm inside fixture confs, and
AC13 is explicitly scoped to `tools/memory-tree/.memory-tree.conf.example` — its own text says "a
whole-file grep will not do, since the example already declares that key elsewhere". A grep of §6
finds `.memory-tree.conf` named nowhere but inside that example path.

**Impact.** Half of a scope item declared as observed is not, and no bar leg covers it — the parity
arm grades declarations and never comments, as AC13 itself says. The impact is bounded, since the
example's comment is the adopter-facing copy and it is the graded one. But the gov conf's comment is
what a session on this repo reads when it wonders why a valued `LEDGER_TOKEN_CUTOFF` grades nothing,
which is the exact confusion S9 exists to prevent. This is round 2's M10 surviving as a partial join,
and a false join reads as coverage where a missing one announces itself.

**Fix.** Extend AC13's second half to run the same contiguous-comment-block grep over
`.memory-tree.conf`, or narrow S4 to the shipped example and say why the local conf does not need it.

**Left-shift.** Unit 3's arm again, sharpened: an `Observed by` tag must cover every clause of its
scope item, so a two-conf item needs two observations or a narrower sentence. Partial coverage is the
failure mode that arm will have most often.

---

### L1 — unit 2 states an exclusion list that source contradicts

**Address.** `memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-2.md` §4,
"Alternatives rejected", the "Spell the pointer as the repo-relative path" entry.

The spec says `check-method-carriers.sh` selects carriers "over every tracked file outside `memory/`,
excluding only `BUILD-METHOD.template.md` itself". The script's own population comment declares four
exclusions with a reason each — `<MEMORY_ROOT>/`, the template, `*.test.sh`, and the leg itself — and
the loop implements all four.

**Impact.** The conclusion survives: `SPEC-TEMPLATE.template.md` is excluded by none of the four, so
the path spelling really would red check 3. But this is a claim about existing code that source
contradicts, offered as the "Verified cost" evidence deciding the pointer spelling, and a later
editor reasoning from "excluding only the template" would conclude a `.test.sh` carrier needs a
registry row, which it does not.

**Fix.** Say "excluding the template, this leg itself and `*.test.sh`", or cite the script's own
exclusion comment block instead of restating the list.

**Left-shift.** None worth building. This is the "point at the source, or gate the pair" charter rule,
and the fix is to point.

---

## What the fold got right

Recorded because round 2's finding that the fold is the defect source is the reason this round exists,
and the number moved.

- **The class rule bit.** Ten of the eighteen defects are in the unit the fan did not fold. The ten
  fan-folded specs carry eight defects between them, and only one of those eight (M3, unit 11's
  copy of a pin unit 10 correctly converted) is the sweep-missed-a-sibling shape that was 93% of
  round 2.
- **Unit 1's declined Fix holds.** The folder declined the half that would have restated
  `BUILD-METHOD` prose beside the source owning it, with that reason stated. The charter's
  "point at the source, or gate the pair" rule backs the decline, and the assigned Fix was the weaker
  half of round 2's ruling. No finding here rests on the declined text.
- **Unit 7's re-derivation was actually run.** Its 27 is correct against the checker's own predicates.
  H9 is not a fabricated re-derivation, it is a real one applied at one address out of three.
- **Round 2's H1 was swept by seven of the nine specs that owed it.** Units 2, 3, 4, 6, 8, 9 and 11
  all name `kit version markers`; unit 5 records it as not owed. Only unit 1 missed it (H3).

## Convergence

The build does not converge this round. Blocker count went 2 → 1 → 1, which is not strictly
decreasing, so the round does not re-arm even though every other number improved. B1 is the whole of
it, and it is a one-token fix plus a namespace rule in the README — but it is a genuine blocker,
because it ships the dead-key-reading-as-armed class inside the build commissioned to close it, and
no criterion in either affected spec can see it.

Three of the eighteen defects (B1, H2, and the `Observed by` half of H4) are cross-unit: no folder
reading only its own spec could find them. That is the structural limit of a per-spec class sweep and
it is the thing to change before round 4. The build README's rules are one-owner rules for the
`tFixture` space and the citation form; they need a third — one owner per shared engine name, and one
predicate run across the whole set rather than eleven times inside eleven files.
