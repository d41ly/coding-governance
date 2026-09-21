# TOOL-dDerivedDocket-52 — the introducing commit of a pinned record line, across the rotation rename

**Status:** CLOSED · rev-2 · 2026-09-21 · node d · Tier-2 · base fb07ca25 · streams tooling · order 17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-build-TOOL-dDerivedDocket-52-1-acceptance-ledger.md](../build/2026-09-21-build-TOOL-dDerivedDocket-52-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md) | spec-audit | TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-49 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54 |

<!-- /gen:spec-records -->

## 1. Goal

Unit 18's S2 re-derives a run's `m-base:` from the commit that first recorded it, and announces a
weaker ancestry reading where that commit cannot be found, naming a rotated record as the canonical
case. Rotation is a staged `git mv` inside the SAME folder and the incoming run writes a fresh
`RUN.md` in the same commit, so the rotated path exists and a path-scoped search answers with the
ROTATION commit instead — a wrong sha rather than a missing one, and the announced fallback never
fires. What git RECORDS at that commit is not a rename, which is §4's first measurement and the
reason the obvious floor for such a search is not there either. Give the leg one function that resolves the introducing commit
across the rename, verifies its own answer, and returns a NAMED empty when it cannot, so a rotated
record grades against the value it recorded and an unresolvable one announces instead of reporting
clean.

## 2. Scope (IN)

- **S1** One resolver function in `tools/unattended/check-unattended.sh`, taking a run-state path and
  a literal line, and returning the sha of the OLDEST commit whose copy of that record carried the
  line. It reads the record's own path and, where that path is an archived name, the live `RUN.md`
  beside it, derived from the archive rule rather than matched by a rename heuristic (§4). The walk
  is FLOORED at the start of the queried record's own tenancy of that path, so a search cannot cross
  into an earlier run's copy at the same path (§4). BOTH ends of that window are resolved by a
  path's FIRST TOUCH and never by `--diff-filter=A`, which answers nothing at all where the rotation
  landed inside a merge (§4). Observed by AC1 and AC8.
- **S2** The walk is UNSIMPLIFIED. The candidate enumeration passes `--full-history`, because a
  path-restricted walk drops a commit TREESAME with a parent: a merge that resolves the record to its
  FIRST parent's side prunes the whole branch that touched it, and the introducing commit with it.
  rev-1 named a rotation inside a merge as that shape and it is not — §4 measures both — so the flag
  is kept for the shape that does prune, and the merge case is answered by the first-touch
  resolution instead. Observed by AC4.
- **S3** The answer is VERIFIED before it is returned: the candidate's own copy of the record carries
  the line, and its FIRST PARENT's copy of the record does not, which is what "introduced" means. A
  candidate failing either test is passed over. The floor commit of S1 is the ONE exception, and it is
  not an escape hatch: at the floor the parent's copy is a different run's record at the same path, so
  comparing them is the collision the floor exists to close, and the floor verifies on its own copy
  alone. Observed by AC2 and AC8.
- **S4** An unresolved search returns EMPTY with one line naming the record and the reason, never a
  sha and never silence. The line rides STDERR, the channel `pass_commit` already uses for a named
  refusal from a library function, so this leg's "exit 0 and no output is clean" stdout contract
  keeps its meaning and gains no fourth exception. Four reasons are distinguished by name: the walk was truncated at its cap,
  no candidate verified, the range could not be resolved, and the record's own tenancy floor could not
  be resolved. Observed by AC3, AC6 and AC8.
- **S5** The enumeration is BOUNDED by a cap, applied to the traversal and not only to the loop body,
  and the cap's DIRECTION is stated beside it. The answer sits at the OLDEST end of the window, while
  `rev-list --max-count=N` applies the count during traversal, newest-first, and `--reverse` reverses
  AFTER — so a capped walk keeps the N NEWEST and discards the only end that can hold the answer. The
  cap therefore never SELECTS a window; it DETECTS one deeper than the resolver will grade: `cap+1`
  fetched, at most `cap` graded, and truncation reported from the count actually emitted. That is the
  pattern `tools/unattended/lib-unattended.sh:288-293` implements and
  `tools/unattended/lib-unattended.sh:266-279` explains. The range this item used to cite for its cap
  discipline stopped ten lines short of that explanation, which is how the direction went unstated. A
  truncated walk reports under S4 rather than answering, and that verdict is reached BEFORE any
  candidate is graded, from the whole emitted list and never from a sentinel met mid-walk. The lib's
  sibling walks newest-first and WANTS the first hit it meets, so a mid-walk sentinel costs it
  nothing; this walk's retained commits are the WRONG end of a too-deep window, so a hit met before
  the sentinel is a wrong sha returned in place of the announcement. The enumeration is a command
  substitution and materialises whole regardless, so counting first buys this for nothing.
  Observed by AC6.
- **S6** The function's own header states what it does NOT answer: it answers only inside the queried
  record's own tenancy of the path and says nothing about an earlier run's copy at that same path, and
  it does not follow a record moved out of its build folder. Observed by AC7.
- **S7** Arms for every branch above in `tools/unattended/check-unattended.test.sh`, and that
  SUITE's own executed-assertion floor — `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`, which live in that
  file — moves in the same commit. `.memory-tree.conf`'s `ARMS_FLOORS` does NOT move, and rev-1 was
  wrong to name it: `tools/memory-tree/check-arms.py` keys its branch population on `fail <n> "` call
  sites, so both of its figures count `fail` branches and their arms, and §4's Fail codes row already
  records that this unit adds none. Observed by AC5.

## 3. Non-goals (OUT)

- Pinning or re-deriving any fact. This unit answers "which commit introduced this line"; unit 18's
  S2 and S8 decide what to do with the answer, and their text is unchanged by this unit.
- Retrofitting the leg's THREE existing first-commit reads. Measured at HEAD on 2026-09-20 by
  grepping `--diff-filter=A` over the file: `tools/unattended/check-unattended.sh:508` answers a DATE
  for a cutoff comparison and already follows the rename; `:1313` is check 15's
  `LANDED_ANCHOR_CUTOFF` site and does not follow; `:1502` deliberately does not, because the waiver
  arm selects its population at an exact path and a renamed record is a different file to it. None is
  wrong for its own question, and changing any of them is a separate unit with its own arms. An
  earlier draft of this bullet counted two and missed `:1313`, which is the site the sibling named
  below converts.
- Routing that sibling's first-commit DATING through this resolver. The build keeps BOTH, and the
  reason is not tolerance: `TOOL-dDerivedDocket-22` answers WHEN a record was first committed, this
  unit answers WHICH commit introduced a given LINE, and the signatures differ by that line while the
  answers differ by type. F2 states why `--follow` is right for the first question and wrong for the
  second. Merging them would be one function answering two questions, which is the shape §4's
  verification step exists to refuse one level down.
- Changing the rotation itself. `archive_name_of` and the staged `git mv` keep their behaviour; this
  unit reads the rename, it does not alter it.
- Answering reachability. Whether a commit touching a path is reachable from a merge parent is a
  different predicate with a different unsimplified spelling, and it belongs to the terminal-record
  exclusion.
- Editing `memory/map/features/unattended.md`. This unit mints no inventory key, because the
  codebase map does not scan `.sh` — `python tools/codebase-map/reuse_lookup.py` prints
  `unscanned layers: .sh` on every run — and that dossier measured 20387 B of its 20480 B cap on
  2026-09-20 (PINNED), so a prose refresh there is a net-zero edit that belongs with a unit funding
  it.

### Edges

- **consumes-from** external — the rotation discipline at HEAD: `archive_name_of` builds the archived
  name inside the record's own directory (`tools/unattended/unattended.sh:1692-1698`) and the move is
  a staged `git mv` (`tools/unattended/unattended.sh:2748`). Without that shape the live path beside
  an archived one is not derivable and the resolver has no second path to read.
- **consumes-from** external — the leg's pinned git wrapper, `tools/unattended/lib-unattended.sh:45`,
  so every history read this function makes sees the history that is there.
- **hands-off** `TOOL-dDerivedDocket-18` — the resolved introducing commit its S2 takes as HEAD at
  preflight when it re-derives `m-base:`, the same resolution its S8 uses to find the commit that
  introduced `asks-at-landing:`, and the named empty that makes the ancestry fallback its §4
  announces reachable at last. Without it S2 grades a rotated record against a base nobody recorded.
- **hands-off** `TOOL-dDerivedDocket-22` — the first-commit DATING that unit builds in this same
  file, including the tenancy floor its §4 takes from this unit's close-out. This resolver does not
  change it, is not called by it, and does not make its `--follow` reading wrong; F2 says why the two
  rulings differ. Without this bullet two rotation-aware first-commit resolvers land in one file with
  opposite tool rulings and a reader who meets one is routed to neither, which is what the G7 audit
  found.
- **hands-off** external — retrofitting `tools/unattended/check-unattended.sh:1502` and the
  disposition-date read beside it onto this resolver, deferred outside this build.

## 4. Design

### What rotation actually does, measured

`--preflight` retires a terminal record by renaming it inside its own folder:
`archive_name_of` prints `'%s/RUN.%s.%.8s.md' "${rel%/RUN.md}"`
(`tools/unattended/unattended.sh:1692-1698`) and the move is `GIT mv -f -- "$rel" "$arch"`
(`tools/unattended/unattended.sh:2748`), both sides staged in one operation. So the archived path
EXISTS and its blob carries every line the record ever held. A path-scoped search over that path
alone answers with the rotation commit.

Measured on this tree on 2026-09-20 (PINNED), over
`memory/builds/aPacedTurnstile/RUN.LANDED.a1fd98d8.md`:

| Spelling | Oldest commit it reports | Date |
|---|---|---|
| path-scoped, archived path only | `2d03cb5aaf4727a02888b8b7d1e1f5f358eea9c3` | 2026-08-20 |
| the same, with rename following | `86e56f5ecb3591da2baa88ea53a830d81e6a4029` | 2026-08-18 |
| the two paths together, unsimplified, oldest first | `86e56f5ecb3591da2baa88ea53a830d81e6a4029` | 2026-08-18 |

The first row is the rotation commit and the other two are the run's own preflight commit, two days
earlier. The blob at that commit is the record, read at `RUN.md`.

### What a rotation records, and why the obvious floor is not there

A rotation is neither a rename nor a delete-and-add to git. Measured on this tree on 2026-09-20
(PINNED) with `git show --name-status`, at both of this repo's rotation commits, with rename
detection left on its default and again with `-M` forced:

| Rotation commit | What git records in the build folder |
|---|---|
| `9ea808cfb6e3c5548943f3d83264b2b0fb99430f` | `A` the archived record, `M` the live `RUN.md` |
| `2d03cb5aaf4727a02888b8b7d1e1f5f358eea9c3` | `A` the archived record, `M` the live `RUN.md` |

So the live `RUN.md` is never re-ADDED by the run that takes the path over, and the obvious floor —
the newest commit that ADDED the record at the path being read — is not there to be found. Asking for
it answers the FIRST run's add instead: on `memory/builds/aBoundedVerdict/RUN.md` an add-filtered log
answers `e8be30e9` (2026-08-19, "preflight — the run is live"), while the record living at that path
today was written at `9ea808cf` (2026-08-20, "fresh run record, prior ABORTED retired").

And where a rotation lands inside a MERGE commit, an add search does not answer late — it does not
answer at all. Measured in a scratch repo on 2026-09-21, with the merge itself performing the `git
mv` and writing the fresh record: `--diff-filter=A` over the archived path returns EMPTY under the
plain spelling AND under `--full-history`, because git computes no diff for a merge commit. That is
the class `tools/memory-tree/row_grammar.py:335-340` records for two of this repo's own archives,
and rev-1 read it as a history-simplification problem `--full-history` would fix. It is not. So
BOTH ends of the window are resolved by a path's first TOUCH, which a merge cannot hide, and the
flag earns its place elsewhere: measured the same day with an `-s ours` merge, a simplified walk
loses the commit that introduced the line entirely and answers nothing, while the unsimplified walk
keeps it. That is the shape S2 now cites and AC4 now grades.

### The tenancy floor

A live `RUN.md`'s boundaries are its own first add, plus every commit that ADDED an archived sibling
in the same directory. Each of those is where one run's tenancy of the path ends and the next begins,
and the window follows from them:

- the queried path is the live `RUN.md` — the window runs from the NEWEST boundary to the tip being
  graded;
- the queried path is an archived name — the window runs from the boundary immediately BEFORE that
  path's own add, up to that add, because the record's bytes lived at `RUN.md` for exactly that span;
- the folder holds no archived sibling — the window runs from the path's own first add.

The floor commit is IN the window and is its oldest member, so the enumeration is the floor itself
followed by the commits after it, oldest first. A range spelled to exclude its own left end drops the
preflight commit the search is usually looking for: on `memory/builds/aBoundedVerdict/RUN.md` the
oldest element of `9ea808cf..HEAD` is `324bfd58`, not the floor commit that wrote the record.

**Why the floor is the mechanism and not a refinement.** Measured on the live
`memory/builds/aBoundedVerdict/RUN.md` against the line `anchor-kind: default-branch`, which it
shares with `memory/builds/aBoundedVerdict/RUN.ABORTED.fc79c21d.md` — the two records carry thirteen
identical non-blank lines today, the anchor evidence and the generated boilerplate among them:

| Walk | Window | Answer |
|---|---|---|
| unfloored, the whole path | 40 commits | `e8be30e9`, the FIRST run's preflight |
| floored at `9ea808cf` | 24 commits | `9ea808cf`, the queried record's own preflight |

S3's verification does not catch the unfloored answer and cannot: `e8be30e9`'s first parent carries
no `RUN.md` at all, so "the parent does not have the line" is true of a commit made the day before
the queried record existed. The floor closes this, not the verification step.

A boundary is therefore the FIRST TOUCH of the live record and of every archived sibling beside it,
and the queried path is excluded from that set only when it is itself archived. Keying the exclusion
on "its first touch IS the ceiling" instead reads any record whose only touch is the tip as having no
floor at all — which is every record in a shallow clone, measured on the AC3 fixture during this
unit's build pass, and it turned that fixture's unresolved RANGE into an unresolved FLOOR.

Whether the floor itself resolves is a real question, answered by S4 rather than assumed. At HEAD
every tracked `memory/builds/*/RUN*.md` path resolves a first add under both the plain and the
`--full-history` spellings; two of the twelve files under `memory/archive/` resolve none under
either, which is the class `tools/memory-tree/row_grammar.py:335-340` records for an archive whose
add landed inside a merge. So an unresolvable floor is a named empty, never a silent fall back to an
unfloored walk.

### The resolution

The function takes a run-state path and a literal line, and answers in five steps.

1. **The path set.** The record's own path, plus — when that path is an archived name — the live
   `RUN.md` in the same directory, derived by stripping the archived basename and appending `RUN.md`.
   The derivation mirrors `archive_name_of`'s own rule rather than re-spelling the archived name's
   grammar, so the two cannot drift apart; a record whose path is already `RUN.md` contributes one
   path.
2. **The floor and the ceiling.** The queried record's tenancy window, by the rule above. A floor that
   cannot be resolved is a named empty under S4 and ends the call there.
3. **The candidate walk.** `rev-list --full-history` over that window, limited to the path set, read
   oldest-first and capped. `--full-history` is not a flourish: a path-restricted walk drops a commit
   TREESAME with a parent, so a merge that resolves the record to its first parent's side prunes the
   branch that touched it — measured above, and the same lesson
   `tools/drift-audit/drift_report.py:806-818` carries for the same flag. It does NOT rescue an add
   search inside a merge, which is why neither end of the window is resolved by one. The cap is S5's,
   and its direction matters more than its value: the window is read oldest
   first because the answer lives at that end, and `--max-count` discards that end, so the cap detects
   a window too deep instead of choosing one. The detection is settled before the first candidate is
   graded, for the reason S5 gives.
4. **The first verifying candidate.** Oldest first, read the record's blob at whichever path of the
   set exists at that commit. The candidate is returned when its own copy carries the line AND the
   first parent's copy of the same record does not carry it — including the case where the record
   does not exist at the first parent, which is the ordinary preflight shape. At the FLOOR that second
   test is not applied (S3), because the parent's copy there is another run's record. A candidate
   failing an applicable test is passed over, so a mis-resolved path costs a rejected candidate rather
   than a wrong sha.
5. **The named empty.** Four outcomes return nothing and print one line each, on stderr: the walk hit its cap, so
   the answer is unknown rather than absent; the walk completed and no candidate verified; the range
   or the path set could not be resolved, as in a shallow clone; and the tenancy floor could not be
   resolved. The caller reads the empty and takes unit 18's announced ancestry fallback, which is the
   reading that paragraph was written for.

Why rename following is not the chosen spelling, although the table in the first subsection shows the
rename being findable: it is rename DETECTION, its answer depends on what else moved in the same
commit, and — spelled as `--follow --diff-filter=A`, the only way it answers a first commit — it is
an ADD search, so the merge blindness measured above reaches it whole: no diff is computed for a
merge under any flag. That is the reading rev-2 corrected; rev-1 called it history simplification,
which `--full-history` would have fixed and does not. The path union needs no heuristic and is
decidable by reading the two paths.

**Stated residual.** Two runs cannot share one tenancy window, so the shared-PATH collision above is
closed by construction rather than by luck, and the earlier draft of this paragraph was wrong twice
over. It described the exposure as two runs of one slug branched at the same commit and sharing an
`m-base:` value, when the measured case is two runs a day apart sharing a path and a line of ordinary
anchor boilerplate. It also called the wrong answer conservative, when an answer drawn from another
run's tenancy is not a wider reading of the right commit but a different commit altogether. What
remains:

- A line introduced, removed and re-introduced INSIDE one tenancy answers its first introduction,
  which is what "introduced" means and is not a defect — and it answers the FIRST one only because a
  window deeper than the cap announces before any candidate is graded (S5). Measured on an
  eight-commit fixture at cap 4 carrying exactly that shape: a sentinel met mid-walk returns the
  RE-introduction and prints no reason line, which is the wrong sha wearing the face of an answer.
- A record moved out of its build folder is not followed (S6).
- A floor that cannot be resolved is an unknown answer, not an absent one (S4).

Which fact classes this touches is worth saying plainly, because they are not alike. An `m-base:`
value is a sha and repeats across runs only where two runs branched at one commit. An
`asks-at-landing:` value is a small count and repeats across unrelated runs freely, and unit 18's S8
resolves it through this same function — so the floor is load-bearing for that fact in a way it would
not be for `m-base:` alone.

### Fail codes

None. This unit adds no `fail` branch: it returns a value or a named empty, and the arms that red on
a wrong value are unit 18's. The one output it adds is the reason line of S4, printed beside the
record it concerns.

### Rollout

**Order 17, sharing the step with unit 17.** Unit 18 consumes this resolver and is order 18, so 17 is
the latest step that leaves it in place before its consumer, and every order from 1 to 38 is taken.
Sharing a step is how a promoted unit reaches a consumer at all, and it is legal: a consumes-from
target may share its consumer's order, it may not be LATER than it. A shared value declares a
parallel group, and M6 in `memory/guides/BUILD-METHOD.md` requires parallel
passes only where disjointness is PROVEN. It is not proven for this pair, on clause 1: both passes
write `tools/unattended/check-unattended.sh` and `tools/unattended/check-unattended.test.sh`, and
both move a floor in `.memory-tree.conf`. So the pair runs in sequence. The roster is handed out
ordered by step and then by id, which puts unit 17 first and this unit second — the order this unit
needs anyway, since it must land before unit 18 and has no claim on landing before unit 17.

Dark by construction. Nothing calls the resolver at this unit's commit; unit 18's S2 is its first
caller. The fixtures carry the coverage until then, which is also why no arm here reads the real
tree: no tracked record carries an `asks:` fact until unit 35 arms gov.

### Inventory

One shell function in `tools/unattended/check-unattended.sh`, its floor step, and one reason-line
prefix carrying the named empties of S4 apart, whose count and wording stay in S4. The cap F4 settles
lives INSIDE that function, as `${INTRODUCING_WALK_CAP:-400}`, with no declaration beside it and no
conf key. No new conf key, no new fact, no new verb, no new leg code. The identifier is RECORDED here rather than left for the
build pass to invent, so the naming leg and `spec tokens (a spec's own names resolve)` both have a
name to grade before the function exists. On 2026-09-20,
`python tools/lexicon/lexicon.py --suggest resolve_introducing_commit --as sh.function` answered OK.

| Identifier | Cell | Verb, and why |
|---|---|---|
| `resolve_introducing_commit` | `sh.function` | `resolve`: it turns a record and a line into the commit they denote, and RUNS the candidate — S3's verification — rather than returning the first row a walk offered |

`.lexicon.conf:23` declares `sh` a `parser` coverage mode rather than a dark one, and
`.lexicon.conf:422` declares the `sh.function snake` cell, so `lexicon naming predicates`
(`tools/gate-legs.json:1052`, guarded on `tools/`) grades this identifier at this unit's commit
whether or not the spec claims the leg. §7 now claims it.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh`, whose own
`FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` carry the executed-assertion floor. NOT `.memory-tree.conf`:
see S7.

### Alternatives rejected

- **Rename following as the resolution.** It answers correctly on this tree today, and the table
  above records that. It is still a heuristic whose result depends on what else moved in the rotation
  commit, and as an add search it inherits the merge blindness that hides a rotation landing inside
  a merge from every flag. Kept as the measurement that proves the plain form wrong, not as the
  mechanism.
- **Leaving the resolution in unit 18.** That is the state this finding came out of: one inline
  search, no verification, and a fallback sentence for a case the search never reaches. A resolver
  with no verification step cannot tell a right answer from a wrong one, which is why it is a unit
  and not a clause.
- **Putting the function in `tools/unattended/lib-unattended.sh`.** That file holds the predicates the
  driver and the leg must answer IDENTICALLY (`tools/unattended/lib-unattended.sh:1`). The driver
  never asks this question, so a function there would be a shared seam with one caller, and the file
  is written by two other units of this build in adjacent steps.

## 5. Production-readiness checklist

- security — this resolver reads history and writes nothing. It is a second opinion the run cannot
  move, which is the property it exists to preserve: every input is the commit graph and a tracked
  blob, never a fact the run recorded.
- perf / scale — one floor resolution — a first-touch walk per `RUN*.md` in the record's own folder,
  plus one `rev-list --count` each to order them — and one bounded `rev-list` per record, plus one
  blob read per candidate until the first verifies. The floor is what makes the window small before the cap has to
  bound anything: on `memory/builds/aBoundedVerdict/RUN.md` it takes the walk from 40 commits to 24,
  and the deepest floored window on this tree is 60. The cap bounds the traversal and reports
  truncation, per S5. The profile note at `tools/unattended/lib-unattended.sh:169-171` prices a
  `--follow` walk at 31 git spawns in a full leg run, so this is not the leg's cost centre.
- error / empty / loading states — the named empties of S4 are the whole of this row, and their
  COUNT and their wording stay in S4 rather than being restated here. Restating them is how this row
  came to say three while S4 says four, having missed the tenancy floor the same day's close-out
  added; a second copy of a list is the copy that rots, which is the charter rule this spec argues
  from elsewhere. Each empty prints its own reason and none of them is silent.
- observability — every empty prints one line naming the record and the reason, so a green row can
  never be read as a verified one.
- risks — the stated residual in §4, two records sharing one line, and a cap set too low, which S4
  reports as truncation rather than hiding.
- testing — the arms of S7, each over a scratch fixture repo built by the leg suite; no arm reads the
  real tree, because no tracked record carries the fact these arms grade. One of those fixtures is
  DEEPER than the declared cap and another carries two tenancies at one path, because a fixture that
  is neither gives the correct and the broken spelling the same verdict.
- migration — none. No stored shape changes and no record is rewritten.
- user docs — N/A — the function is leg-internal and no user-facing page describes it; the protocol
  and verb carriers are other units'.

## 6. Acceptance criteria

- **AC1** — When the resolver of `tools/unattended/check-unattended.sh` runs over a fixture repo
  whose mandated record was rotated by a later run's preflight, it RETURNS the run's own preflight
  commit and not the rotation commit, and prints no reason line. The arm extracts the function from
  the leg the way the kit's existing bound arms do
  (`tools/unattended/unattended.test.sh:5347-5349`, which also refuses an empty extraction), so what
  this pass observes is the extracted function over a scratch fixture and not a suite run.
  Red when: the resolution answers with the rotation commit, so a caller re-deriving a base from it
  would take the merge-base of `anchor-sha:` and the rotation commit's first parent, and a correct
  archived record would grade against a value nobody wrote.
  fixture: a scratch repo the leg suite builds; the tracked tree holds no rotated record carrying an
  `asks:` fact today and will not until unit 35 arms gov.
  permission: the criterion asserts the FUNCTION's return, because check 19 grades no `m-base:` fact
  at HEAD — at `tools/unattended/check-unattended.sh:1432-1455` it grades the authorization mode, the
  playbook and the piece count — and unit 18's S2 is the first caller, at a LATER order. The
  check-19 verdict half is therefore observed at unit 18's commit and not in this unit's pass.
- **AC2** — When the fixture's rotation commit and its preflight commit BOTH carry the line, the
  resolver in `tools/unattended/check-unattended.sh` returns the preflight commit, and when a staged candidate's first parent already carries
  the line that candidate is passed over rather than returned.
  Red when: the first candidate of the walk is returned unverified, so a path the walk resolved
  wrongly is indistinguishable from a correct one.
  fixture: the pass-over is only OBSERVABLE where the floor is not itself a candidate, because
  oldest-first the first carrier is otherwise the introduction by construction. The arm therefore
  files an archived sibling in a commit of its own — a boundary that never touched the live record —
  and then touches the record without changing the line. Passed over, the window holds no
  introduction and S4's no-candidate empty is what the resolver prints; returned unverified, the
  resolver answers a commit that introduced nothing. The arm asserts the empty AND its reason line,
  with a control in the same fixture where a genuine introduction IS answered.
- **AC3** — When the resolver in `tools/unattended/check-unattended.sh` runs over a shallow-clone
  fixture in which the introducing commit is not present, it returns empty AND prints one line naming
  the record and the unresolved-range reason, and the arm asserts the line was printed rather than
  only that the return was empty.
  Red when: an unresolvable search returns empty and says nothing, so the caller cannot tell an
  unknown answer from an absent one — the reassuring-zero shape
  `tools/memory-tree/row_grammar.py:335-340` already records for a rotation baseline.
  permission: that the caller then takes unit 18's announced ancestry reading is observed at unit 18's
  commit, for the reason AC1 gives; this criterion asserts only what the resolver returns and prints.
- **AC4** — TWO fixtures, because rev-1 asked one to carry two different measurements and only one
  of them held. (a) When the fixture's rotation lands inside a MERGE commit, the resolver in
  `tools/unattended/check-unattended.sh` still answers the preflight commit, while the obvious
  add-search spelling over the archived path answers NOTHING under the plain spelling and under
  `--full-history` alike — both asserted in the arm, because that measurement is why neither end of
  the window is resolved by an add. (b) When a merge resolves the record to its FIRST parent's side
  (the `-s ours` shape), the resolver answers the pruned side-branch commit that introduced the line,
  and the same fixture graded with the simplified spelling answers nothing at all; that contrast is
  asserted in the arm.
  Red when: the enumeration drops `--full-history`, so a commit TREESAME to the followed parent for
  the record's path is pruned, the resolver answers nothing for a record it could have resolved, and
  it does so with no reason line — an absent answer wearing the face of a clean one.
  new arm: staged RED first. The arm is not allowed to pass until it has been SEEN RED with the
  simplified spelling in place.
- **AC5** — When the arms of S7 land, `tools/unattended/check-unattended.test.sh`'s own
  `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` read higher at this unit's commit than at its parent, read
  with `git show` at both, and `FLOOR_SHARD_1` is unchanged because every new assertion sits in
  region two.
  Red when: arms land and the floor holds, so a later deletion of them is invisible.
  figure: DERIVED at observation time from the two commits; no count is written into this spec.
  The RAISE is counted rather than measured, because this unit's pass may run no suite: it is the
  block's own assertion-helper call sites, and the block was executed once standalone in a replica of
  the suite prologue to confirm the count.
  permission: that the suite still passes AT the raised floor is observed only by running it, which
  this pass may not do; that observation is the build's one post-build bar.
- **AC6** — When the resolver in `tools/unattended/check-unattended.sh` walks a fixture whose tenancy
  window is DEEPER than the declared cap and whose line was introduced at the oldest end of it, it
  returns empty and names truncation, the reason is textually distinct from the no-candidate-verified
  reason, and the arm asserts the same fixture answers correctly once the cap is raised past the
  window.
  Red when: the cap is applied to the loop body rather than to the traversal, so the work is unbounded
  while the verdict looks bounded; or the walk is spelled `--reverse --max-count=<cap>`, which keeps
  the cap newest commits and silently drops the introducing one, so a resolvable record reports no
  candidate; or truncation is discovered mid-walk AFTER candidates have been graded, so a line
  introduced at the oldest end, removed inside the window and re-introduced among the retained newest
  commits is answered with the RE-introduction and no reason line at all; or both empties print one
  reason and an operator cannot tell an unknown answer from an absent one.
  new arm: staged RED first, over a window deeper than the cap, and a SECOND fixture deeper than the
  cap carrying the introduce-remove-re-introduce shape, because a deep window that merely lacks the
  answer cannot tell a walk that announces from one that answers wrongly. A fixture shallower than
  the cap gives the correct and the broken spelling the SAME verdict — which is how the same defect survived the
  last truncation arm written in this kit, recorded at
  `tools/unattended/lib-unattended.sh:272-279`.
- **AC7** — When `git grep -c` runs over `tools/unattended/check-unattended.sh` for the resolver's
  header sentence naming what it does NOT answer, it returns 1 at this unit's commit and 0 at its
  parent, and that sentence names both limits of S6 — the single tenancy, and a record moved out of
  its build folder.
  Red when: the header states only what the function does, so a reader takes the resolution for a
  guarantee it never made.
- **AC8** — When the resolver in `tools/unattended/check-unattended.sh` is asked for a line that a
  fixture's live `RUN.md` shares byte-for-byte with the record a previous run left at that same path,
  it answers the SECOND tenancy's preflight commit, and the arm asserts that the unfloored walk over
  the same fixture answers the FIRST run's commit instead. A second arm points the resolver at a
  fixture whose floor cannot be resolved and asserts the named empty of S4, distinct in text from the
  other three.
  Red when: the walk is floored at the newest ADD of the queried path, which a rotation does not
  create, so the floor lands on the first run's add and closes nothing; or the first-parent test of S3
  is applied AT the floor, where the parent holds another run's record, so a correct answer is passed
  over and the resolver reports no candidate.
  new arm: staged RED first. The arm may not pass until it has been SEEN RED with the unfloored walk
  in place, which is the shape §4's floored-versus-unfloored table measures.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/check-unattended.test.sh` · a rotated mandated record, a record whose
rotation and preflight commits both carry the line, a rotation landing inside a merge, a merge that
prunes the introducing commit from a simplified walk, a shallow clone with the introducing commit
absent, two tenancies at one path sharing a byte-identical line, a folder whose tenancy floor cannot
be resolved, a tenancy window deeper than the cap, and one deeper than the cap whose line is
re-introduced among the retained newest commits · that suite's own `FLOOR_ASSERTIONS` and
`FLOOR_SHARD_2`. NOT `ARMS_FLOORS`, for S7's reason.

## 8. Open questions

- **F1** — Where does the resolver live, `tools/unattended/check-unattended.sh` or
  `tools/unattended/lib-unattended.sh`? Options: (a) the leg, its only caller; (b) the shared library,
  in case the driver ever asks. (b) makes a shared seam with one caller and collides with two other
  units writing that file in adjacent steps.
  RESOLVED (agent, 2026-09-20, delegated): (a). The file's own header says it holds the predicates the
  driver and the leg must answer identically
  (`tools/unattended/lib-unattended.sh:1`), and the driver never asks this question. A later driver
  caller moves it, which is a rename with two call sites and not a design debt.
- **F2** — Rename following or the path union? Options: (a) follow the rename; (b) read the archived
  path and the live `RUN.md` together, unsimplified.
  RESOLVED (agent, 2026-09-20, delegated): (b). Both answer correctly on this tree, measured in §4,
  and (a) is a heuristic that, being an add search, also inherits the merge blindness which hides a
  rotation landing inside a merge — the class `tools/memory-tree/row_grammar.py:335-340` measured on
  this repo's own archives, re-measured under both spellings in §4.
  This ruling is about a SHA and does not overturn `--follow` where the answer is a DATE, which is why
  the build carries two resolvers and not one. A date is compared against a cutoff, so a heuristic
  that picks a neighbouring commit still grades correctly as long as it errs in a known direction —
  `TOOL-dDerivedDocket-22` states its own direction, that a reused path can date a later run's archive
  to an earlier run's first commit and so errs toward grandfathering and never toward a frozen red. A
  sha is not compared, it is RE-DERIVED FROM: unit 18's S2 takes a merge-base from it, so a
  neighbouring commit is a different ancestry rather than a rounded one, and a heuristic whose answer
  depends on what else moved in the rotation commit cannot be trusted with it. Neither ruling is a
  defect in the other, and §3 declares that unit hands-off on this ground.
- **F3** — Does the verification step belong here or in unit 18? Options: (a) here, so the resolver
  cannot return an unverified sha; (b) in the caller, so the resolver stays a thin git read.
  RESOLVED (agent, 2026-09-20, delegated): (a). A resolver that returns a candidate the caller must
  re-check is two answers to one question, and the caller that skipped the re-check is what this
  finding is.
- **F4** — What cap VALUE bounds the candidate walk, and who declares it? Its DIRECTION is no longer
  part of this fork: S5 settles that, and the answer sits at the end `--max-count` discards. What is
  left is the number. The floored window is one run's tenancy of its own path, and the deepest such
  window on this tree at HEAD is 60 commits, on `memory/builds/dRetiredFork/RUN.md` — so any cap at or
  below that truncates on this repo's own deepest record today and the resolver announces instead of
  answering. Options: a constant beside the function; a reuse of the leg's existing bounded-walk cap
  at `tools/unattended/lib-unattended.sh:288-293`; a conf key, which is a new inventory key for a
  number one caller reads. Left OPEN for the build pass to settle against that constant when it reads
  it, with the 60-commit measurement as the floor under any value it picks. S5 binds either way,
  because it fixes the direction and the sentinel, and S4 requires truncation to announce itself.
  RESOLVED (agent, 2026-09-21, delegated): 400, the sibling bound's own default
  (`PASS_ORDER_PREANCHOR_CAP` in `tools/unattended/check-pass-order.sh`), declared INSIDE the
  function as `${INTRODUCING_WALK_CAP:-400}` rather than beside it. The placement is an ARMING
  decision and not a style one: AC1 requires the arms to extract this function with `sed` and source
  it, so a constant one line above the signature would have to be re-declared by the suite — and the
  truncation arms would then grade a cap they wrote themselves, which is the double-you-wrote-it
  shape §4's verification step refuses one level down. The env name is what lets an arm exercise a
  4-commit window without a 400-commit fixture. Not a conf key, for the reason the fork already
  gives: a new inventory key for a number one caller reads.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from the G3 round-2 spec audit's H4, and the same
  day's promotion close-out: the cap gained its DIRECTION (S5, §4 step 3, AC6, F4) after the verifier
  reproduced `--reverse --max-count` keeping the newest commits; the walk gained a TENANCY FLOOR (S1,
  S3, S4, §4, AC8) after the same pass measured an unfloored search answering a previous run's commit
  on `memory/builds/aBoundedVerdict/RUN.md`; the residual and S6 were restated against the shared-PATH
  case; and AC1 now asserts the function's own return, since check 19 grades no `m-base:` fact until
  unit 18 lands · and the verifier pass that followed moved AC1's actor off the suite and onto the
  extracted resolver, and required the truncation verdict to precede grading (S5, §4 step 3, the §4
  residual, AC6, §7) after measuring a mid-walk sentinel answer the re-introduction on an
  eight-commit fixture at cap 4.
  Extended on the same pass, same base and rev, by the G7 round-1 spec audit's fold · H5 (38) · §3's
  non-goals and Edges, §8 F2 and §10 · this spec named `TOOL-dDerivedDocket-22` zero times while that
  unit resolves a first commit with `--follow --diff-filter=A` in the same file, states this unit's
  own tenancy floor in its §4, and records this unit's close-out in its §9 twice — a coupling recorded
  on one side only. The routing DECISION is that the build keeps both resolvers, because one answers a
  DATE and one a SHA; F2 now says why `--follow` is right for the first and wrong for the second, §3
  declares the edge, and §10 stops quoting a `.sh`-blind probe as a negative result. The non-goal's
  count of the leg's existing first-commit reads was also wrong at HEAD, not merely stale: there are
  THREE, and `:1313` was the missing one.
  L1 (11, 13) · §5's error row · it counted three named empties where S4 declares four, having missed
  the tenancy floor the same day's close-out added. The row now points at S4 instead of restating it.
  M4 (21) · §4's Inventory and §7 · filed against `TOOL-dDerivedDocket-53` and true here too, because
  `.lexicon.conf:23` declares `sh` a `parser` mode and `.lexicon.conf:422` a live `sh.function` cell,
  so this unit's new shell function is graded by `lexicon naming predicates` whatever §7 said. §7 now
  lists that leg and §4 records the identifier with its `--suggest` answer.
- rev-2 · 2026-09-21 · S1 · S2 · S4 · S7 · §4 · §5 · AC2 · AC4 · AC5 · §7 · F4 · the building pass,
  against the tree and against scratch fixtures rather than against the base. Four things did not
  hold, and each was measured before it was rewritten.
  (1) **The floor S7 named cannot move.** `ARMS_FLOORS` is not an executed-assertion floor at all:
  `tools/memory-tree/check-arms.py` discovers its population with `fail (\d+) "` and both of its
  figures count `fail` branches and the arms naming their message text. This unit adds no `fail`
  branch — §4's Fail codes row said so from rev-1 — so that pin is unmovable here, and raising it
  would have meant inventing a branch to pin. The floor that DOES move is the suite's own
  `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`. S7, AC5, §4's Files-touched and §7 now name it, and
  `.memory-tree.conf` leaves this unit's write set.
  (2) **`--full-history` does not rescue an add search inside a merge.** Measured in a scratch repo
  on 2026-09-21, with the merge itself performing the rotation: `--diff-filter=A` over the archived
  path returns EMPTY under the plain spelling AND under `--full-history`, because git computes no
  diff for a merge. rev-1 read `tools/memory-tree/row_grammar.py:335-340` as a simplification
  problem that flag would fix. So both ends of the window are now resolved by a path's first TOUCH,
  which a merge cannot hide, and the flag is kept for the shape that genuinely prunes — measured the
  same day, an `-s ours` merge, where the simplified walk loses the introducing commit entirely and
  answers nothing. AC4 now grades both measurements, as two fixtures rather than one.
  (3) **The boundary exclusion had to be keyed on the PATH, not on the ceiling.** Keying it on "this
  boundary's first touch IS the ceiling" reads any record whose only touch is the tip as having no
  floor — which is every record in a shallow clone, and it turned AC3's fixture into an unresolved
  FLOOR rather than the unresolved RANGE that criterion asserts. Caught by the AC3 fixture on its
  first run and recorded in §4.
  (4) **The pass-over of AC2 is not observable oldest-first** unless the floor is itself outside the
  candidate set, because the first carrier is otherwise the introduction by construction. AC2 now
  states the fixture that makes it visible — an archived sibling filed in a commit of its own — and
  what the resolver prints when it fires, which is S4's no-candidate empty and not a different sha.
  Also settled here: F4's cap, at 400 and INSIDE the function for the arming reason F4 now gives;
  and S4's reason-line CHANNEL, stderr, so the leg's stdout contract gains no fourth exception.
  The correction's OTHER HALVES were swept in the same rev rather than left standing: §4's rename-
  following paragraph, its Alternatives-rejected bullet and F2 each called the merge case history
  simplification, which is the reading (2) disproves, and each now names it as add-search blindness.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "finding the commit that introduced a line in a run-state
record across a rename"` prints `unscanned layers: .sh` and ranks only python candidates, the highest
of which, `run`, is a name-token collision. **That is a LIMIT, not a result.** The probe cannot see
the layer this unit writes, so a "no seam" conclusion drawn from it is a probe with no liveness
assertion — the shape charter §7 bans in a gate, arriving in a reuse audit instead. An earlier draft
of this section treated the blindness as a negative result and missed a sibling in this same build.

Two searches the probe cannot make were therefore made by hand. Reading source found the in-tree
prior art: the three first-commit reads already in the leg at
`tools/unattended/check-unattended.sh:508`, `:1313` and `:1502`, which disagree about rename
following on purpose, and the unsimplified-walk rationale at
`tools/drift-audit/drift_report.py:806-818` and `tools/memory-tree/row_grammar.py:335-340`. Grepping
this build's own spec folder for the mechanism's distinguishing command found the sibling §3 now
declares hands-off, which resolves a first commit with `--follow --diff-filter=A` in this same file
and states the same tenancy floor in its own §4. This unit extends none of the three call sites (§3)
and reuses their lesson rather than their code.

Recall terms used: `python tools/memory-recall/query.py "how is the commit that introduced a pinned
run-state line found across a rotation rename" --terms "rotation rename archive_name_of run-state
RUN.md m-base preflight ancestry fallback --follow diff-filter check 19 unattended leg"`. It returned
the rotation-mode record whose measurement of an unresolvable archive baseline §4 cites, and the
half-rotation findings that pin what rotation stages.
